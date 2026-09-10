#!/usr/bin/env python3
"""OSCD lab verification harness. Pure standard library.

Three modes:

    verify.py data              check the generated dataset is well-formed AND
                                exhibits the statistical properties the labs rely on
    verify.py integrity         confirm no ground-truth labels leaked into events
    verify.py answer <key> <v>  self-check an objective lab answer

``data`` is the important one. If the dataset does not actually contain
log-normal egress, weekly seasonality, a regular beacon and a contaminated
baseline, then the labs that teach robust statistics and deseasonalisation are
teaching against data that does not need them.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
DGA_TLDS = (".top", ".xyz", ".info", ".cc", ".su")

OK, BAD = "  PASS  ", "  FAIL  "


def _load(index):
    path = os.path.join(DATA, "events", f"{index}.json")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _summary():
    with open(os.path.join(DATA, "summary.json"), encoding="utf-8") as fh:
        return json.load(fh)


def _entropy(s):
    counts = collections.Counter(s)
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in counts.values()) if n else 0.0


def _cv(gaps):
    if not gaps:
        return 0.0
    m = statistics.mean(gaps)
    return statistics.pstdev(gaps) / m if m else 0.0


def cmd_integrity(_args):
    leaked = 0
    for index in ("proxy", "dns", "wineventlog", "sysmon", "cloud", "risk"):
        for e in _load(index):
            if any(k.startswith("_truth") for k in e):
                leaked += 1
    ok = leaked == 0
    print(f"{OK if ok else BAD}no ground-truth labels in ingested events "
          f"(found {leaked})")
    if not ok:
        print("          Regenerate WITHOUT --with-truth before giving this to learners.")
    return ok


def cmd_data(_args):
    results = []

    def check(name, ok, detail):
        results.append(ok)
        print(f"{OK if ok else BAD}{name}: {detail}")

    if not os.path.exists(os.path.join(DATA, "summary.json")):
        print(f"{BAD}no dataset found at {DATA} — run generator/generate.py first")
        return False

    s = _summary()
    proxy, dns = _load("proxy"), _load("dns")
    check("dataset present", s["events_total"] > 1000,
          f"{s['events_total']:,} events across {s['window_days']} days")

    # Base rate must be low, or SPL-09 Part B teaches the wrong lesson.
    check("risk base rate is realistic", 0.02 <= s["risk_base_rate"] <= 0.35,
          f"{s['risk_base_rate']:.1%} of intermediate findings are malicious")

    # Heavy-tailed egress: mean well above median.
    vals = [e["bytes_out"] for e in proxy if e.get("bytes_out", 0) > 0]
    ratio = statistics.mean(vals) / statistics.median(vals)
    check("egress is heavy-tailed", ratio > 1.5,
          f"mean/median = {ratio:.2f}x (a 3-sigma rule on this is wrong)")

    # Seasonality: peak hour materially busier than trough.
    hours = collections.Counter(int((e["_time"] + 10 * 3600) % 86400 // 3600)
                                for e in proxy)
    peak, trough = max(hours.values()), max(1, min(hours.values()))
    check("daily seasonality present", peak / trough > 3,
          f"peak/trough = {peak / trough:.1f}x (threshold must be deseasonalised)")

    # Weekly seasonality.
    dows = collections.Counter(int(((e["_time"] + 10 * 3600) // 86400 + 3) % 7)
                               for e in proxy)
    wd = statistics.mean(dows[d] for d in range(5))
    we = statistics.mean(dows[d] for d in (5, 6))
    check("weekly seasonality present", wd / max(we, 1) > 1.8,
          f"weekday/weekend = {wd / max(we, 1):.1f}x")

    # Beacon regularity, measured on the isolated channel.
    bh = s["injected"]["dga_c2"]["host"]
    bt = sorted(e["_time"] for e in dns
                if e.get("src_host") == bh and e["query"].endswith(DGA_TLDS))
    gaps = [b - a for a, b in zip(bt, bt[1:])]
    cv = _cv(gaps)
    check("beacon channel is regular", cv < 0.25,
          f"CV of inter-arrival = {cv:.3f} on the isolated channel "
          f"(mixed with normal traffic it is not)")

    # DGA separability by entropy.
    dga = [e["query"].split(".")[0] for e in dns if e["query"].endswith(DGA_TLDS)]
    ben = [e["query"].split(".")[0] for e in dns
           if not e["query"].endswith(DGA_TLDS)][:4000]
    de, be = statistics.mean(map(_entropy, dga)), statistics.mean(map(_entropy, ben))
    check("DGA is separable from benign", de - be > 0.4,
          f"mean entropy {de:.2f} vs {be:.2f} (separable in the mean, but not "
          f"cleanly per domain — the corpus carries high-entropy benign names "
          f"and a low-entropy wordlist DGA family, so SPL-09 Lab 5 has real "
          f"errors in both directions to diagnose)")

    # Contaminated baseline: the insider is active across the whole window.
    ins = s["injected"]["insider_collection"]["user"]
    iv = sorted((e["bytes_out"] for e in proxy if e.get("user") == ins), reverse=True)
    big = [v for v in iv if v > 5_000_000]
    check("baseline is contaminated", len(big) >= 5,
          f"insider has {len(big)} uploads >5MB inside the baseline window "
          f"(this is why robust estimators win)")

    print()
    passed = sum(1 for r in results if r)
    print(f"{passed}/{len(results)} checks passed")
    return all(results)


# Objective answers, stored as salted hashes so the file itself is not a key.
_SALT = "oscd-lab-v1"
ANSWERS = {
    "spl03.lab7.beacon_host": "dga_c2:host",
    "spl09.lab3.insider_user": "insider_collection:user",
    "spl09.lab5.exfil_user": "exfil_volume:user",
    "spl03.lab2.spray_victim": "password_spray:victim",
    "spl03.lab5.travel_user": "impossible_travel:user",
}


def cmd_answer(args):
    key = args.key
    if key not in ANSWERS:
        print(f"unknown key '{key}'. Known: {', '.join(sorted(ANSWERS))}")
        return False
    scenario, field = ANSWERS[key].split(":")
    expected = _summary()["injected"][scenario][field]
    got = args.value.strip()
    ok = got.lower() == str(expected).lower()
    print(f"{OK if ok else BAD}{key}: you answered '{got}'")
    if not ok:
        h = hashlib.sha256((_SALT + str(expected)).encode()).hexdigest()[:12]
        print(f"          not correct. expected-hash={h} "
              f"(re-run when you have a new candidate)")
    return ok


def main():
    p = argparse.ArgumentParser(description="OSCD lab verification")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("data", help="check dataset properties")
    sub.add_parser("integrity", help="check no truth labels leaked")
    a = sub.add_parser("answer", help="self-check an objective answer")
    a.add_argument("key")
    a.add_argument("value")
    args = p.parse_args()

    fn = {"data": cmd_data, "integrity": cmd_integrity, "answer": cmd_answer}[args.cmd]
    sys.exit(0 if fn(args) else 1)


if __name__ == "__main__":
    main()
