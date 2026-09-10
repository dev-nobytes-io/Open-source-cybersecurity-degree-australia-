#!/usr/bin/env python3
"""Verify that the lab guides still hold against the generated dataset.

Writing these guides surfaced several claims that were plausible, published, and
false — a risk-ranking heuristic that measured worse than the thing it was meant
to beat, an entropy result that came out backwards, a capacity model whose two
halves disagreed. Each was caught by running the code rather than trusting it.

This script makes that repeatable, so a change to the generator cannot quietly
invalidate the prose. It checks four things:

  blocks    every embedded ``python3 - <<'PY'`` block runs to completion
  syntax    every standalone ```python block parses
  answers   the five objective answers are still reachable by the method the
            guides actually teach -- not merely present in the answer file
  links     every relative markdown link inside labs/ resolves

The answer check is the one with teeth. `verify.py answer` confirms a value
against a hash; this confirms that the *search described in the guide* still
produces that value. A generator change that breaks the taught method while
leaving the labelled scenario intact would pass the first and fail this.

Usage:  python3 harness/check_guides.py [blocks|syntax|answers|links|all]
"""
from __future__ import annotations

import ast
import collections
import csv
import json
import math
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES = sorted((ROOT / "guides").glob("spl-*.md"))
PAPER = sorted((ROOT / "paper").glob("*.md"))
DATA = ROOT / "data"

# Blocks that reach the network. Syntax-checked, never executed: CI should not
# fail because a third-party API is having a bad afternoon.
NETWORK_MARKERS = ("urllib.request", "dns.google", "ip-api.com")


def _fail(msg):
    print(f"  FAIL  {msg}")
    return 1


def _ok(msg):
    print(f"  PASS  {msg}")
    return 0


# --------------------------------------------------------------------------
# blocks
# --------------------------------------------------------------------------

# Fences nested inside an admonition are indented, and so is their closer. A
# pattern that only recognises a closer at column 0 runs past it and swallows the
# prose that follows, which parses as neither bash nor python.
#
# Note the explicit [^\n] rather than a dot under re.DOTALL: a dot that matches
# newlines inside a repeated group makes this a catastrophic-backtracking pattern
# that hangs on the first long file.
BLOCK_RE = re.compile(
    r"^(?P<indent>[ \t]*)```bash\n"
    r"(?:(?P=indent)[^\n]*\n)*?"
    r"(?P=indent)python3 - <<'PY'\n"
    r"(?P<body>(?:[^\n]*\n)*?)"
    r"(?P=indent)PY\n",
    re.M,
)

PY_FENCE_RE = re.compile(
    r"^(?P<indent>[ \t]*)```python\n"
    r"(?P<body>(?:[^\n]*\n)*?)"
    r"(?P=indent)```[ \t]*$",
    re.M,
)


def check_blocks():
    """Run every embedded heredoc block against a throwaway copy of the data.

    A copy, not the real directory: some blocks are fault injections that
    deliberately corrupt a lookup, and one writes a 29 MB file.
    """
    if not DATA.exists():
        return _fail("no data/ -- run generator/generate.py first")

    errors = 0
    total = 0
    with tempfile.TemporaryDirectory() as tmp:
        sandbox = pathlib.Path(tmp) / "lab"
        sandbox.mkdir()
        shutil.copytree(DATA, sandbox / "data")
        for guide in GUIDES:
            blocks = [m.group("body")
                      for m in BLOCK_RE.finditer(guide.read_text(encoding="utf-8"))]
            for n, body in enumerate(blocks, 1):
                total += 1
                if any(m in body for m in NETWORK_MARKERS):
                    continue
                script = sandbox / f"_{guide.stem}_{n}.py"
                script.write_text(textwrap.dedent(body), encoding="utf-8")
                proc = subprocess.run(
                    [sys.executable, script.name],
                    cwd=sandbox, capture_output=True, text=True, timeout=600,
                )
                if proc.returncode != 0:
                    errors += _fail(
                        f"{guide.name} block {n} exited {proc.returncode}\n"
                        + "\n".join("        " + l
                                    for l in proc.stderr.strip().splitlines()[-6:])
                    )
    if errors:
        return errors
    return _ok(f"all {total} embedded python blocks ran clean")


def check_syntax():
    errors = 0
    total = 0
    for path in GUIDES + PAPER:
        text = path.read_text(encoding="utf-8")
        for n, m in enumerate(PY_FENCE_RE.finditer(text), 1):
            total += 1
            try:
                ast.parse(textwrap.dedent(m.group("body")))
            except SyntaxError as exc:
                errors += _fail(f"{path.name} python block {n}: {exc}")
    if errors:
        return errors
    return _ok(f"all {total} standalone python blocks parse")


# --------------------------------------------------------------------------
# answers -- the taught method must still find the taught answer
# --------------------------------------------------------------------------

def _events(name):
    with open(DATA / "events" / f"{name}.json", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh]


def _entropy(s):
    counts = collections.Counter(s)
    return -sum((n / len(s)) * math.log2(n / len(s)) for n in counts.values())


def _spray_victim():
    """SPL-03 Lab 2: distinct accounts per source, then the one success."""
    events = _events("wineventlog")
    by_src = collections.defaultdict(set)
    for e in events:
        if e.get("EventCode") == 4625:
            by_src[e["src"]].add(e["user"])
    sprayer = max(by_src, key=lambda k: len(by_src[k]))
    if len(by_src[sprayer]) < 15:
        raise AssertionError("no source exceeds the taught threshold of 15 accounts")
    wins = [e["user"] for e in events
            if e.get("EventCode") == 4624 and e["src"] == sprayer]
    if len(wins) != 1:
        raise AssertionError(f"expected exactly one successful spray logon, got {len(wins)}")
    return wins[0]


def _travel_user():
    """SPL-03 Lab 5: geo-velocity, minus service accounts, then weak auth."""
    events = _events("cloud")
    identities = {r["identity"]: r for r in
                  csv.DictReader(open(DATA / "lookups" / "oscd_identities.csv",
                                      encoding="utf-8"))}
    by_user = collections.defaultdict(list)
    for e in events:
        by_user[e["user"]].append(e)

    def km(a, b):
        la1, lo1, la2, lo2 = (math.radians(x) for x in
                              (a["src_lat"], a["src_long"], b["src_lat"], b["src_long"]))
        h = (math.sin((la2 - la1) / 2) ** 2
             + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
        return 6371 * 2 * math.asin(math.sqrt(h))

    candidates = set()
    for user, rows in by_user.items():
        if identities.get(user, {}).get("category") == "service_account":
            continue
        rows.sort(key=lambda e: e["_time"])
        for a, b in zip(rows, rows[1:]):
            hours = (b["_time"] - a["_time"]) / 3600
            if hours <= 0:
                continue
            offshore = "AU" not in (a["src_country"], b["src_country"]) or \
                       a["src_country"] != b["src_country"]
            if km(a, b) > 500 and km(a, b) / hours > 900 and offshore:
                candidates.add(user)
    weak = {e["user"] for e in events
            if e.get("authentication_method") == "legacy"
            or e.get("mfa_result") != "satisfied"}
    hits = candidates & weak
    if len(hits) != 1:
        raise AssertionError(
            f"the taught funnel should narrow to exactly one user, got {len(hits)}: "
            f"{sorted(hits)}")
    return hits.pop()


def _beacon_host():
    """SPL-03 Lab 7: NXDOMAIN rate, then entropy on the leftmost label."""
    events = _events("dns")
    lookups = collections.Counter(e["src_host"] for e in events)
    failures = collections.Counter(e["src_host"] for e in events
                                   if e["reply_code"] == "NXDomain")
    rates = sorted(((failures[h] / lookups[h], h) for h in lookups if lookups[h] >= 20),
                   reverse=True)
    if not rates:
        raise AssertionError("no host has enough lookups to rate")
    high = collections.Counter(
        e["src_host"] for e in events
        if len(e["query"].split(".")[0]) >= 12 and _entropy(e["query"].split(".")[0]) > 3.2)
    if not high:
        raise AssertionError("entropy filter matched nothing")
    top_entropy = high.most_common(1)[0][0]
    if top_entropy != rates[0][1]:
        raise AssertionError(
            "the two independent lines of evidence no longer converge: "
            f"NXDOMAIN rate says {rates[0][1]}, entropy says {top_entropy}")
    return top_entropy


def _insider_user():
    """SPL-09 Lab 3 / SPL-03 Lab 6: cross-department Type 3 breadth."""
    identities = {r["identity"]: r for r in
                  csv.DictReader(open(DATA / "lookups" / "oscd_identities.csv",
                                      encoding="utf-8"))}
    assets = {r["host"]: r for r in
              csv.DictReader(open(DATA / "lookups" / "oscd_assets.csv", encoding="utf-8"))}
    reach = collections.defaultdict(set)
    for e in _events("wineventlog"):
        if e.get("EventCode") != 4624 or e.get("Logon_Type") != "3":
            continue
        ident, asset = identities.get(e["user"]), assets.get(e["dest"])
        if not ident or not asset or ident["category"] == "service_account":
            continue
        if ident["bunit"] != asset["bunit"]:
            reach[e["user"]].add(e["dest"])
    ranked = sorted(reach.items(), key=lambda kv: -len(kv[1]))
    if not ranked or len(ranked[0][1]) < 5:
        raise AssertionError("no user shows the taught cross-department breadth")
    return ranked[0][0]


def _exfil_user():
    """SPL-09 Lab 7 / SPL-02 Lab 7: robust per-user baseline *plus* a floor.

    The modified z-score is scale-free, so a user whose normal day is 2 kB and
    who one day sends 100 kB outranks the person exfiltrating 2.5 GB. The
    statistic is correct and the ranking is useless. The taught method pairs it
    with a materiality floor drawn from the estate's own distribution, which is
    the condition that makes the alert worth an analyst's time.
    """
    daily = collections.defaultdict(float)
    for e in _events("proxy"):
        daily[(e["user"], int(e["_time"] // 86400))] += e["bytes_out"]
    by_user = collections.defaultdict(list)
    for (user, _day), total in daily.items():
        by_user[user].append(total)

    def median(xs):
        s = sorted(xs)
        mid = len(s) // 2
        return s[mid] if len(s) % 2 else (s[mid - 1] + s[mid]) / 2

    everything = sorted(v for vals in by_user.values() for v in vals)
    floor = everything[int(0.99 * len(everything))]

    flagged = []
    for user, vals in by_user.items():
        if len(vals) < 7:
            continue
        logs = [math.log(v + 1) for v in vals]
        med = median(logs)
        dev = median([abs(x - med) for x in logs])
        if dev == 0:
            continue
        for v in vals:
            z = 0.6745 * (math.log(v + 1) - med) / dev
            if z > 3.5 and v > floor:
                flagged.append((z, user))
    if not flagged:
        raise AssertionError(
            "no day is both anomalous for its user and material for the estate")
    return max(flagged)[1]


METHODS = {
    "spl03.lab2.spray_victim": _spray_victim,
    "spl03.lab5.travel_user": _travel_user,
    "spl03.lab7.beacon_host": _beacon_host,
    "spl09.lab3.insider_user": _insider_user,
    "spl09.lab5.exfil_user": _exfil_user,
}


def check_answers():
    if not DATA.exists():
        return _fail("no data/ -- run generator/generate.py first")
    errors = 0
    for key, method in METHODS.items():
        try:
            value = method()
        except AssertionError as exc:
            errors += _fail(f"{key}: the taught method broke -- {exc}")
            continue
        proc = subprocess.run(
            [sys.executable, str(ROOT / "harness" / "verify.py"), "answer", key, value],
            cwd=ROOT, capture_output=True, text=True,
        )
        if proc.returncode != 0 or "PASS" not in proc.stdout:
            errors += _fail(
                f"{key}: the taught method returns {value!r}, which is not the answer")
        else:
            errors += _ok(f"{key}: reachable by the method the guide teaches")
    return errors


# --------------------------------------------------------------------------
# links
# --------------------------------------------------------------------------

LINK_RE = re.compile(r"\[[^\]]*\]\((?!https?://|#|mailto:)([^)#\s]+)")


def check_links():
    errors = 0
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        if "data" in path.parts:
            continue
        base = path.parent
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            checked += 1
            if not (base / target).resolve().exists():
                rel = path.relative_to(ROOT.parent)
                errors += _fail(f"{rel} -> {target} does not exist")
    if errors:
        return errors
    return _ok(f"all {checked} relative links inside labs/ resolve")


MODES = {
    "blocks": check_blocks,
    "syntax": check_syntax,
    "answers": check_answers,
    "links": check_links,
}


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode not in MODES and mode != "all":
        print(f"unknown mode {mode!r}. Use: {', '.join(MODES)}, or all")
        return 2
    modes = MODES if mode == "all" else {mode: MODES[mode]}
    errors = 0
    for name, fn in modes.items():
        print(f"\n[{name}]")
        errors += fn()
    print()
    if errors:
        print(f"{errors} check(s) failed")
        return 1
    print("guide checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
