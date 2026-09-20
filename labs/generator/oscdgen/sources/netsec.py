"""Firewall session and IDS alert events, CIM Network_Traffic + Intrusion_Detection.

Both are *derived* from traffic the generator already emits rather than drawn
independently, because that is how the real devices see the world: the edge
firewall logs the same egress the web log records, and the IDS alerts on a
subset of it. Deriving keeps the three views consistent — the beacon host's
callbacks, the exfil chunks and the insider's uploads appear in all three with
matching times, hosts and volumes — which is what the SA-05 integration labs
need in order to teach cross-source correlation rather than single-log search.

Design rules, each of which a lab depends on:

* **Every web egress has a firewall session.** So `index=fw action=allowed` is a
  second, independently formatted view of the web log. A learner who reconciles
  the two finds the counts agree; a learner who onboards the firewall with the
  wrong timestamp format finds they do not. That reconciliation is SA-05 Lab 2.
* **Blocked sessions are noise, not an answer key.** Policy denies (workstations
  trying admin ports outbound) are spread across many hosts, so
  `action=blocked` alone identifies nothing.
* **IDS alerts are mostly false positives.** Informational and policy
  signatures dominate; the true positives (DGA lookups, the beacon channel, the
  exfil transfers, the certutil download) sit inside that noise at a realistic
  precision, so triaging the alert stream is analysis, not lookup.
* **DNS is not on the edge firewall.** Lookups go to the internal resolver, so
  there is no 53/udp session per query. This is stated in the data model so a
  learner does not go looking for it.

Signature names are written in the ET Open *style* for familiarity; the IDs are
in a private range and correspond to no real rule.
"""
from __future__ import annotations

import hashlib
import random

FW_DEVICE = "fw-edge-01"
IDS_DEVICE = "ids-egress-01"

# Outbound ports policy blocks from workstations. The denies these produce are
# the ordinary background of any estate and must not concentrate on the
# scenario hosts.
BLOCKED_PORTS = {445: "deny-outbound-smb", 3389: "deny-outbound-rdp",
                 22: "deny-outbound-ssh", 23: "deny-outbound-telnet",
                 8080: "deny-outbound-alt-http"}

# Informational / policy signatures — the false-positive mass.
NOISE_SIGS = [
    (2100001, "ET INFO TLS Handshake to CDN edge", "Not Suspicious Traffic", 3),
    (2100002, "ET INFO Observed DNS over HTTPS Domain", "Potentially Bad Traffic", 3),
    (2100003, "ET POLICY Dropbox Client Broadcasting", "Potential Corporate Privacy Violation", 3),
    (2100004, "SURICATA STREAM excessive retransmissions", "Generic Protocol Command Decode", 3),
    (2100005, "ET POLICY Windows Update P2P Activity", "Potential Corporate Privacy Violation", 3),
    (2100006, "ET INFO HTTP Request to a *.com.au Domain with Long URI", "Not Suspicious Traffic", 3),
    (2100007, "ET POLICY curl User-Agent Outbound", "Attempted Information Leak", 2),
]

SIG_DGA = (2900001, "ET DNS Query to a DGA-pattern domain (uncommon TLD)", "Malware Command and Control Activity", 2)
SIG_BEACON = (2900002, "ET MALWARE Possible periodic C2 callback (small TLS session)", "Malware Command and Control Activity", 1)
SIG_EXFIL = (2900003, "ET POLICY Large outbound transfer to file-sharing service", "Potential Corporate Privacy Violation", 2)
SIG_LOLBIN = (2900004, "ET POLICY certutil User-Agent download", "Potentially Bad Traffic", 2)

_TRUTH = ("_truth_scenario", "_truth_technique", "_truth_note")


def _inherit(child, parent):
    for k in _TRUTH:
        if k in parent:
            child[k] = parent[k]
    return child


def ip_for(domain):
    """A stable external IP for a domain, so the same site resolves the same way
    every time it appears — and differently from every other site."""
    h = hashlib.md5(domain.encode("utf-8")).digest()
    return "104.%d.%d.%d" % (16 + h[0] % 11, h[1], 1 + h[2] % 254)


def fw_event(rng, ts, asset, dest_ip, dest_port, action, bytes_out=0, bytes_in=0,
             rule="allow-outbound-web", transport="tcp", app="ssl", direction="outbound"):
    return {
        "_time": ts,
        "sourcetype": "fw",
        "index": "fw",
        "dvc": FW_DEVICE,
        "src": asset.ip,
        "src_host": asset.host,
        "src_port": rng.randint(49152, 65535),
        "dest_ip": dest_ip,
        "dest_port": dest_port,
        "transport": transport,
        "app": app,
        "action": action,
        "rule": rule,
        "direction": direction,
        "bytes_out": int(bytes_out),
        "bytes_in": int(bytes_in),
    }


def ids_alert(rng, ts, asset, dest_ip, dest_port, sig, transport="tcp"):
    sid, name, category, severity = sig
    return {
        "_time": ts,
        "sourcetype": "ids",
        "index": "ids",
        "dvc": IDS_DEVICE,
        "ids_type": "network",
        "src": asset.ip,
        "src_host": asset.host,
        "dest_ip": dest_ip,
        "dest_port": dest_port,
        "transport": transport,
        "signature_id": sid,
        "signature": name,
        "category": category,
        "severity": severity,
        "action": "alerted",
    }


def derive(rng, org, events):
    """Firewall sessions and IDS alerts implied by the events already generated.

    Deterministic for a given ``rng`` and event list; the caller passes a
    dedicated ``random.Random`` so this cannot perturb the base dataset.
    """
    assets = {a.host: a for a in org.assets}
    ip_of = {a.host: a.ip for a in org.assets}
    out = []
    dns_answer = {}

    for e in events:
        idx = e.get("index")
        scenario = e.get("_truth_scenario")
        host = e.get("src_host") or e.get("dest")
        asset = assets.get(host)

        if idx == "dns":
            if e.get("reply_code") == "NoError":
                dns_answer[e["query"]] = e["answer"]
            # The IDS sees the resolver's upstream queries; DGA-pattern names
            # trip a signature some of the time.
            if scenario == "dga_c2" and asset and rng.random() < 0.15:
                out.append(_inherit(
                    ids_alert(rng, e["_time"] + 0.05, asset, "10.10.0.53", 53,
                              SIG_DGA, transport="udp"), e))
            continue

        if idx == "proxy" and asset:
            dest_ip = dns_answer.get(e["dest"]) or ip_for(e["dest"])
            port = 80 if e["url"].startswith("http://") else 443
            fw = _inherit(fw_event(rng, e["_time"] + 0.02, asset, dest_ip, port,
                                   "allowed", e["bytes_out"], e["bytes_in"],
                                   app="web-browsing" if port == 80 else "ssl"), e)
            out.append(fw)

            if scenario == "beacon_c2":
                if rng.random() < 0.35:
                    out.append(_inherit(ids_alert(rng, e["_time"] + 0.1, asset,
                                                  dest_ip, port, SIG_BEACON), e))
            elif scenario == "exfil_volume":
                if rng.random() < 0.33:
                    out.append(_inherit(ids_alert(rng, e["_time"] + 0.1, asset,
                                                  dest_ip, port, SIG_EXFIL), e))
            elif scenario is None:
                # Policy denies and informational alerts, spread thinly.
                if rng.random() < 0.02:
                    p = rng.choice(list(BLOCKED_PORTS))
                    out.append(fw_event(rng, e["_time"] + rng.uniform(1, 900), asset,
                                        ip_for(e["dest"] + str(p)), p, "blocked",
                                        rule=BLOCKED_PORTS[p], app="unknown"))
                if rng.random() < 0.0025:
                    out.append(ids_alert(rng, e["_time"] + 0.1, asset, dest_ip, port,
                                         rng.choice(NOISE_SIGS)))
            continue

        if idx == "sysmon" and scenario == "lolbin_download" and asset \
                and e.get("process_name", "").lower() == "certutil.exe":
            cmd = e.get("process", "")
            stage = cmd.split("http://", 1)[1].split("/", 1)[0] if "http://" in cmd else "198.51.100.7"
            out.append(_inherit(fw_event(rng, e["_time"] + 0.4, asset, stage, 80, "allowed",
                                         bytes_out=rng.randint(300, 700),
                                         bytes_in=rng.randint(180_000, 900_000),
                                         app="web-browsing"), e))
            out.append(_inherit(ids_alert(rng, e["_time"] + 0.5, asset, stage, 80,
                                          SIG_LOLBIN), e))
            continue

        if idx == "wineventlog" and scenario == "lateral_movement":
            # East-west: the session the remote-execution rides on, seen by the
            # internal segmentation firewall rather than the edge.
            dest = assets.get(e.get("dest"))
            src_ip = e.get("src")
            if dest and src_ip:
                src = type("A", (), {"ip": src_ip,
                                     "host": next((h for h, ip in ip_of.items() if ip == src_ip), src_ip)})()
                for port, app in ((445, "smb"), (135, "msrpc")):
                    out.append(_inherit(fw_event(rng, e["_time"] + rng.uniform(0.5, 4), src,
                                                 dest.ip, port, "allowed",
                                                 bytes_out=rng.randint(4_000, 40_000),
                                                 bytes_in=rng.randint(2_000, 20_000),
                                                 rule="allow-internal-admin", app=app,
                                                 direction="internal"), e))
            continue

    # A little internal policy noise so east-west denies exist outside the scenario.
    workstations = [a for a in org.assets if a.role == "workstation"]
    servers = [a for a in org.assets if a.role != "workstation"]
    if workstations and servers and events:
        t0, t1 = events[0]["_time"], events[-1]["_time"]
        for _ in range(int((t1 - t0) / 86400 * 6)):
            a = rng.choice(workstations)
            out.append(fw_event(rng, rng.uniform(t0, t1), a, rng.choice(servers).ip,
                                rng.choice([3389, 22, 5985]), "blocked",
                                rule="deny-workstation-to-server-admin", app="unknown",
                                direction="internal"))

    return out
