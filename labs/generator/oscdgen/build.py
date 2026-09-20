"""Assemble a complete labelled dataset."""
from __future__ import annotations

import json
import math
import os
import random
from collections import Counter, defaultdict

from . import rng as R
from .profile import build_org, asset_rows, identity_rows
from .sources import auth, process, network, cloud, netsec
from . import scenarios as S

TRUTH_KEYS = ("_truth_scenario", "_truth_technique", "_truth_note")


def _server_footprint(rng, org):
    """The handful of servers each person routinely reaches.

    Without this, every ordinary user authenticates only to their own workstation,
    the user x resource matrix is rank-deficient, and behavioural peer grouping
    (SPL-09 Lab 6) has nothing to group: the only accounts with any breadth of
    access are the service accounts, so every "behavioural outlier" is a service
    account and the technique looks useless. Real people reach file servers,
    application servers and a jump host, mostly within their own department.
    """
    servers = [a for a in org.assets if a.role != "workstation"]
    by_dept = {}
    for a in servers:
        by_dept.setdefault(a.department, []).append(a)
    shared = [a for a in servers if a.role == "jump_host"] or servers[:2]

    footprint = {}
    for ident in org.identities:
        if ident.category == "service_account":
            footprint[ident.user] = rng.sample(servers, min(12, len(servers)))
            continue
        own = by_dept.get(ident.department, [])
        n_own = min(len(own), rng.randint(1, 3))
        picks = rng.sample(own, n_own) if own else []
        # A minority also use shared infrastructure. This is the tail that makes
        # peer groups differ from the org chart in interesting ways.
        if rng.random() < 0.35 and shared:
            picks = picks + [rng.choice(shared)]
        if rng.random() < 0.10 and servers:
            picks = picks + [rng.choice(servers)]      # genuine cross-department use
        footprint[ident.user] = picks or [rng.choice(servers)]
    return footprint


def _benign_day(rng, org, day_start, out, footprint):
    """One day of ordinary activity, modulated by seasonality."""
    ws = {a.host: a for a in org.assets if a.role == "workstation"}
    for ident in org.identities:
        a = ws.get(ident.workstation)
        if a is None:
            a = rng.choice([x for x in org.assets if x.role != "workstation"])
        # Sample activity across the day, weighted by the seasonal factor.
        for hour in range(24):
            ts0 = day_start + hour * 3600
            factor = R.seasonal_factor(ts0)
            if ident.category == "service_account":
                factor = 0.85 + 0.15 * factor      # service accounts barely sleep
            lam = 1.7 * factor * ident.activity
            for _ in range(R.negbin(rng, lam, 3.0)):
                ts = ts0 + rng.uniform(0, 3600)
                roll = rng.random()
                if roll < 0.22:
                    # Most authentication is to your own workstation; a minority
                    # reaches a server you routinely use.
                    target = a
                    if rng.random() < 0.28:
                        target = rng.choice(footprint[ident.user])
                        out.append(auth.event(rng, ts, ident, target,
                                              success=True, src_ip=a.ip,
                                              logon_type="3"))
                        continue
                    out.extend(auth.benign_burst(rng, ts, ident, target))
                elif roll < 0.55:
                    out.append(process.benign(rng, ts, ident, a))
                elif roll < 0.90:
                    if rng.random() < BENIGN_NXDOMAIN_RATE:
                        # Resolves to nothing and goes no further: no proxy event
                        # follows a failed lookup.
                        out.append(network.dns_event(
                            rng, ts, a, network.failed_lookup(rng), answer=False))
                    else:
                        dom = network.benign_domain(rng)
                        out.append(network.proxy_event(rng, ts, ident, a, domain=dom))
                        if rng.random() < 0.45:
                            out.append(network.dns_event(rng, ts - 0.3, a, dom))
                else:
                    out.append(cloud.signin(rng, ts, ident, "AU", success=True))
            # Occasional benign offshore sign-in: real travel, real false positive.
            if rng.random() < 0.0012:
                out.append(cloud.signin(rng, ts0 + rng.uniform(0, 3600), ident,
                                        rng.choice(["NZ", "SG"]), success=True))


# Share of benign DNS lookups that fail. Set to zero and `reply_code=NXDomain`
# becomes a free answer key for the C2 host (SPL-03 Lab 7).
BENIGN_NXDOMAIN_RATE = 0.05


def generate(seed=1337, days=14, n_users=220, n_servers=40, start_ts=None):
    rng = random.Random(seed)
    org = build_org(rng, n_users=n_users, n_servers=n_servers)

    if start_ts is None:
        # Anchor to a Monday 00:00 UTC so weekly seasonality is aligned and
        # reproducible regardless of when the generator is run.
        start_ts = 1757030400 - (days * 86400)      # 2025-09-05-ish, minus window
        start_ts -= start_ts % 86400
        start_ts -= ((start_ts // 86400) + 3) % 7 * 86400
    end_ts = start_ts + days * 86400

    events = []
    footprint = _server_footprint(rng, org)
    for d in range(days):
        _benign_day(rng, org, start_ts + d * 86400, events, footprint)

    # ---- scenarios -------------------------------------------------------
    injected = {}
    mid = start_ts + (days // 2) * 86400

    ev, spray_victim = S.password_spray(rng, org, mid + 2 * 3600)
    events += ev
    injected["password_spray"] = {"victim": spray_victim.user}

    ev, travel_user = S.impossible_travel(rng, org, mid + 9 * 3600)
    events += ev
    injected["impossible_travel"] = {"user": travel_user.user}

    ws = {a.host: a for a in org.assets}
    host = ws.get(spray_victim.workstation) or rng.choice(org.assets)
    events += S.lolbin_download(rng, org, mid + 3 * 3600, spray_victim, host)
    injected["lolbin_download"] = {"user": spray_victim.user, "host": host.host}

    ev, hops = S.lateral_movement(rng, org, mid + 4 * 3600, spray_victim)
    events += ev
    injected["lateral_movement"] = {"user": spray_victim.user,
                                    "hosts": [h.host for h in hops]}

    beacon_host = rng.choice([a for a in org.assets if a.role == "workstation"])
    events += S.dga_beacon(rng, org, mid + 5 * 3600, beacon_host)
    injected["dga_c2"] = {"host": beacon_host.host}

    exfil_user = rng.choice([i for i in org.identities
                             if i.department == "finance" and i.category == "employee"])
    exfil_host = ws.get(exfil_user.workstation) or rng.choice(org.assets)
    events += S.exfiltration(rng, org, mid + 20 * 3600, exfil_user, exfil_host)
    injected["exfil_volume"] = {"user": exfil_user.user, "host": exfil_host.host}

    insider = rng.choice([i for i in org.identities
                          if i.category == "employee" and i.user != exfil_user.user])
    events += S.insider_slow_collection(rng, org, start_ts, end_ts, insider, org.assets)
    injected["insider_collection"] = {"user": insider.user}

    events.sort(key=lambda e: e["_time"])

    # ---- derived network security telemetry ---------------------------
    # Firewall sessions and IDS alerts are implied by the traffic above and
    # carry its labels, so the three views of one connection agree. A
    # separate RNG keeps the base dataset byte-identical to earlier seeds.
    events += netsec.derive(random.Random(seed + 2), org, events)
    events.sort(key=lambda e: e["_time"])
    return {"org": org, "events": events, "injected": injected,
            "start": start_ts, "end": end_ts, "seed": seed, "days": days}


# ---------------------------------------------------------------------------

def risk_index(dataset, seed=None, malicious_sample_rate=0.35, benign_rate=0.0075):
    """Synthetic intermediate findings for the RBA labs.

    Splunk ES is a premium app the labs cannot assume, but SPL-09 Part C only
    needs a populated ``risk`` index. Generating one directly is not a
    compromise: it means the learner knows the ground truth and can compute a
    real predictive value, which an ES trial would not give them.

    Scores here are deliberately **uncalibrated** — plausible-looking numbers
    someone picked by feel. Fitting them properly is SPL-09 Lab 4.
    """
    rng = random.Random(seed if seed is not None else dataset["seed"] + 1)
    detections = {
        "Excessive Failed Authentications": (20, "user"),
        "Authentication From New Country": (35, "user"),
        "LOLBin Download Behaviour": (60, "system"),
        "Anomalous Parent Child Process": (45, "system"),
        "Remote Execution Observed": (55, "system"),
        "High Entropy Domain Lookup": (25, "system"),
        "Regular Outbound Callback": (40, "system"),
        "Large Outbound Transfer": (50, "user"),
        "Access Outside Peer Group": (30, "user"),
        "Legacy Authentication Protocol": (15, "user"),
    }
    scenario_map = {
        "password_spray": ["Excessive Failed Authentications"],
        "impossible_travel": ["Authentication From New Country", "Legacy Authentication Protocol"],
        "lolbin_download": ["LOLBin Download Behaviour", "Anomalous Parent Child Process"],
        "lateral_movement": ["Remote Execution Observed", "Excessive Failed Authentications"],
        "dga_c2": ["High Entropy Domain Lookup"],
        "beacon_c2": ["Regular Outbound Callback"],
        "exfil_volume": ["Large Outbound Transfer"],
        "insider_collection": ["Access Outside Peer Group", "Large Outbound Transfer"],
    }
    findings = []

    for e in dataset["events"]:
        scenario = e.get("_truth_scenario")
        if scenario:
            names = scenario_map.get(scenario, [])
            if not names or rng.random() > malicious_sample_rate:
                continue
            name = rng.choice(names)
        else:
            # Benign contributions are the false-positive mass, and they must
            # dominate. A risk index where most findings are real would invert
            # the base-rate lesson of SPL-09 Part B and make Lab 2's arithmetic
            # and Lab 4's calibration meaningless. Defaults give roughly a 1-in-10
            # malicious rate; lower `benign_rate` to make the labs easier.
            if rng.random() > benign_rate:
                continue
            name = rng.choice(list(detections))

        base, obj_type = detections[name]
        if obj_type == "user":
            entity = e.get("user")
        elif e.get("index") in ("proxy", "dns"):
            # In web and DNS events `dest` is the remote domain. Risk attaches to
            # the host that made the request, not to the site it contacted.
            entity = e.get("src_host")
        else:
            entity = e.get("dest") or e.get("src_host")
        if not entity or entity == "-":
            continue
        findings.append({
            "_time": e["_time"],
            "index": "risk",
            "sourcetype": "stash",
            "search_name": name,
            "entity": entity,
            "entity_type": obj_type,
            "risk_score": max(1, int(rng.gauss(base, base * 0.18))),
            "risk_message": f"{name} observed for {entity}",
            "_truth_scenario": scenario or "benign",
            "_truth_technique": e.get("_truth_technique", "-"),
        })
    findings.sort(key=lambda f: f["_time"])
    return findings


def summarise(dataset, findings):
    truth = Counter(e.get("_truth_scenario", "benign") for e in dataset["events"])
    mal = sum(v for k, v in truth.items() if k != "benign")
    total = len(dataset["events"])
    rf = Counter(f["_truth_scenario"] for f in findings)
    rmal = sum(v for k, v in rf.items() if k != "benign")
    return {
        "events_total": total,
        "events_malicious": mal,
        "base_rate": mal / total if total else 0.0,
        "by_scenario": dict(truth),
        "risk_findings_total": len(findings),
        "risk_findings_malicious": rmal,
        "risk_base_rate": rmal / len(findings) if findings else 0.0,
        "entities": len(dataset["org"].identities),
        "assets": len(dataset["org"].assets),
        "window_days": dataset["days"],
        "seed": dataset["seed"],
    }
