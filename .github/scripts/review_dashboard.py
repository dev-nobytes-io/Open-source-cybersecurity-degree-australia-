#!/usr/bin/env python3
"""Generate the Phase 4 review dashboard from unit metadata.

Reads each unit's Unit Metadata table (Status, Domain Expert, Practitioner
Reviewer, Last Reviewed, Degree Layer, Major / Pathway) and writes a live
review-status dashboard to docs/review/dashboard.md:

  * counts by lifecycle status and by reviewer assignment,
  * per-section tables (Foundation, cores, each major) with sign-off state.

Run whenever unit review metadata changes (same cadence as the other generators):

    python3 .github/scripts/review_dashboard.py

The content lifecycle and roles are defined in docs/governance.md.
"""
from __future__ import annotations

import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/review/dashboard.md"
UNIT_FILE_RE = re.compile(r"^(F|OC|SC|TH|DF|CT|DE|CE|SE|LD|GR|CAP)\d{2}-.*\.md$")

LIFECYCLE = ["Draft", "Under Review", "Practitioner Approved", "Framework Verified", "Published"]
GROUP_OF = {"F": "Foundation", "OC": "Operational Core", "SC": "Strategic Core"}
MAJOR_NAME = {
    "TH": "Threat Hunting", "DF": "DFIR", "CT": "Cyber Threat Intelligence",
    "DE": "Detection Engineering", "CE": "Cyber Threat Emulation",
    "SE": "Security Engineering", "LD": "Leadership & CISO",
    "GR": "Governance, Risk & Compliance",
}
GROUP_ORDER = ["Foundation", "Operational Core", "Strategic Core"] + list(MAJOR_NAME.values())


def prefix_of(code: str) -> str:
    m = re.match(r"^([A-Z]+)\d", code)
    return m.group(1) if m else ""


def meta(text: str, field: str) -> str:
    m = re.search(r"^\|\s*" + re.escape(field) + r"\s*\|\s*(.+?)\s*\|", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def assigned(val: str) -> bool:
    return bool(val) and not val.lstrip("_").lower().startswith("unassigned")


def cell(val: str) -> str:
    return val if assigned(val) else "—"


def unit_files() -> list[Path]:
    files = []
    for root in (ROOT / "core/units", ROOT / "degrees"):
        if root.exists():
            files.extend(p for p in root.rglob("*.md") if UNIT_FILE_RE.match(p.name))
    return sorted(files)


def main() -> int:
    rows = []  # (group, code, title, status, de, pr, last)
    for path in unit_files():
        text = path.read_text(encoding="utf-8")
        code = (meta(text, "Unit Code") or path.name.split("-", 1)[0]).strip()
        prefix = prefix_of(code)
        group = GROUP_OF.get(prefix) or MAJOR_NAME.get(prefix, "Other")
        rows.append((
            group, code,
            meta(text, "Unit Title") or path.stem,
            meta(text, "Status") or "Draft",
            meta(text, "Domain Expert"),
            meta(text, "Practitioner Reviewer"),
            meta(text, "Last Reviewed"),
        ))

    total = len(rows)
    by_status = defaultdict(int)
    de_assigned = pr_assigned = 0
    for r in rows:
        by_status[r[3]] += 1
        de_assigned += assigned(r[4])
        pr_assigned += assigned(r[5])

    out = []
    out.append("# Phase 4 — Unit Review Dashboard")
    out.append("")
    out.append("> **Generated** by `.github/scripts/review_dashboard.py` from each unit's")
    out.append("> Unit Metadata. Do not edit by hand. Process, roles, and the lifecycle:")
    out.append("> [review hub](index.md) · [`docs/governance.md`](../governance.md).")
    out.append("")
    out.append("To move a unit forward, open a **Unit Review Request** issue (template in")
    out.append("`.github/ISSUE_TEMPLATE/`) and complete `templates/review-checklist.md`.")
    out.append("")

    out.append("## Lifecycle status")
    out.append("")
    out.append("| Status | Units |")
    out.append("|---|---|")
    for s in LIFECYCLE:
        out.append(f"| {s} | {by_status.get(s, 0)} |")
    extra = sorted(s for s in by_status if s not in LIFECYCLE)
    for s in extra:
        out.append(f"| {s} (non-standard) | {by_status[s]} |")
    out.append(f"| **Total** | **{total}** |")
    out.append("")
    out.append(f"**Reviewer assignment:** Domain Expert assigned on {de_assigned}/{total} · "
               f"Practitioner Reviewer assigned on {pr_assigned}/{total}.")
    out.append("")
    if by_status.get("Draft", 0) == total:
        out.append("> All units are **Draft** — Phase 4 (practitioner review) has not yet begun. "
                   "This dashboard will track progress as reviewers sign off.")
        out.append("")

    out.append("## By section")
    out.append("")
    groups = defaultdict(list)
    for r in rows:
        groups[r[0]].append(r)
    for g in GROUP_ORDER + [g for g in groups if g not in GROUP_ORDER]:
        if g not in groups:
            continue
        out.append(f"### {g}")
        out.append("")
        out.append("| Unit | Title | Status | Domain Expert | Practitioner Reviewer | Last Reviewed |")
        out.append("|---|---|---|---|---|---|")
        for _, code, title, status, de, pr, last in sorted(groups[g], key=lambda r: r[1]):
            out.append(f"| {code} | {title} | {status} | {cell(de)} | {cell(pr)} | {cell(last)} |")
        out.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} — {total} units; "
          f"status: " + ", ".join(f"{k}={by_status[k]}" for k in LIFECYCLE if by_status.get(k)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
