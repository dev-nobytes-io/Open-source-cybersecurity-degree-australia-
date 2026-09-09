#!/usr/bin/env python3
"""OSCD lab data generator.

Pure standard library — no pip install required, by design. A learner should be
able to produce the dataset on any machine with Python 3.8+.

    python3 generate.py --days 14 --out ../data
    python3 generate.py --seed 42 --days 30 --users 500 --out /tmp/big
    python3 generate.py --with-truth --out ../data-instructor
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from oscdgen.build import generate, risk_index, summarise   # noqa: E402
from oscdgen.emit import write                              # noqa: E402


def main():
    p = argparse.ArgumentParser(description="Generate labelled Splunk lab data.")
    p.add_argument("--seed", type=int, default=1337,
                   help="RNG seed; identical seed gives an identical dataset")
    p.add_argument("--days", type=int, default=14, help="window length in days")
    p.add_argument("--users", type=int, default=220)
    p.add_argument("--servers", type=int, default=40)
    p.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "data"))
    p.add_argument("--with-truth", action="store_true",
                   help="INSTRUCTOR MODE: leave _truth_* fields in the ingested "
                        "events. Do not use for learner datasets.")
    p.add_argument("--benign-rate", type=float, default=0.0075,
                   help="per-event probability of a benign intermediate finding; "
                        "raise to make the risk index noisier")
    args = p.parse_args()

    out = os.path.abspath(args.out)
    print(f"seed={args.seed} days={args.days} users={args.users} -> {out}")

    ds = generate(seed=args.seed, days=args.days,
                  n_users=args.users, n_servers=args.servers)
    rf = risk_index(ds, benign_rate=args.benign_rate)
    written = write(ds, rf, out, include_truth=args.with_truth)

    s = summarise(ds, rf)
    print(f"  events     {s['events_total']:>8,}  "
          f"malicious {s['events_malicious']:>5,}  base rate {s['base_rate']:.5f}")
    print(f"  risk       {s['risk_findings_total']:>8,}  "
          f"malicious {s['risk_findings_malicious']:>5,}  base rate {s['risk_base_rate']:.4f}")
    for k, v in sorted(written.items()):
        print(f"    {k:<14} {v:>8,}")
    if args.with_truth:
        print("  !! INSTRUCTOR MODE: truth labels are inside the events")
    print(f"  summary    {os.path.join(out, 'summary.json')}")


if __name__ == "__main__":
    main()
