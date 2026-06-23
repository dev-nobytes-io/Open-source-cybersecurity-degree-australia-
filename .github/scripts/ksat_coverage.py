#!/usr/bin/env python3
"""Generate a NICE/DCWF KSAT coverage map from the unit content.

Parses each unit's `### NICE/DCWF KSATs` table (Type | ID | Statement |
Demonstrated In) and its `### NIST NICE DCWF` work-role table, then writes a
coverage report to docs/ksat-coverage.md:

  * per-unit K/S/A/T counts,
  * totals by degree layer,
  * distinct work-role coverage across the curriculum,
  * a full KSAT index.

This is the metrics backbone for education-coverage maps. Run it whenever KSAT
content changes:  python3 .github/scripts/ksat_coverage.py

KSAT IDs are project-local (provisional) pending Framework Custodian mapping to
official NICE/DCWF identifiers.
"""
from __future__ import annotations

import re
from pathlib import Path
from collections import defaultdict

UNIT_FILE_RE = re.compile(r"^(F|OC|SC|TH|DF|CT|DE|CE|SE|LD|GR|CAP)\d{2}-.*\.md$")
TYPE_LETTER = {"knowledge": "K", "skill": "S", "ability": "A", "task": "T"}
LAYER_ORDER = ["Foundation", "Operational Core", "Strategic Core", "Major", "Capstone"]


def unit_files() -> list[Path]:
    files: list[Path] = []
    for root in (Path("core/units"), Path("degrees")):
        if root.exists():
            files.extend(p for p in root.rglob("*.md") if UNIT_FILE_RE.match(p.name))
    return sorted(files)


def section(text: str, heading: str, level: str = "##") -> str:
    m = re.search(
        r"^" + level + r"\s+" + re.escape(heading) + r"\s*$(.*?)(?=^" + level[:1] + r"{1,3}\s|\Z)",
        text, re.MULTILINE | re.DOTALL,
    )
    return m.group(1) if m else ""


def meta(text: str, field: str) -> str:
    m = re.search(r"^\|\s*" + re.escape(field) + r"\s*\|\s*(.+?)\s*\|", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|[\s:|-]+\|$", line):
            continue
        rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


def main() -> int:
    files = unit_files()
    per_unit = []          # (code, title, layer, {K,S,A,T: count})
    by_layer = defaultdict(lambda: defaultdict(int))
    roles = defaultdict(set)   # "code — role" -> set(unit codes)
    ksat_index = []        # (unit_code, type_letter, id, statement)
    missing = []

    for path in files:
        text = path.read_text(encoding="utf-8")
        code = meta(text, "Unit Code") or path.name.split("-", 1)[0]
        title = meta(text, "Unit Title") or path.stem
        layer = meta(text, "Degree Layer") or "Unknown"

        # Work roles from the DCWF table.
        nice = section(text, "NIST NICE DCWF", "###")
        for row in table_rows(nice)[1:] if table_rows(nice) else []:
            if len(row) >= 4 and row[2] and row[2].lower() not in ("work role", ""):
                roles[f"{row[3]} — {row[2]}"].add(code)

        # KSATs.
        ksat = section(text, "NICE/DCWF KSATs", "###")
        counts = {"K": 0, "S": 0, "A": 0, "T": 0}
        rows = table_rows(ksat)
        data = rows[1:] if rows else []
        if not data:
            missing.append(code)
        for row in data:
            if len(row) < 3:
                continue
            letter = TYPE_LETTER.get(row[0].strip().lower())
            if not letter:
                continue
            counts[letter] += 1
            ksat_index.append((code, letter, row[1], row[2]))
        per_unit.append((code, title, layer, counts))
        for k, v in counts.items():
            by_layer[layer][k] += v

    # --- Render ---
    out = []
    out.append("# NICE/DCWF KSAT Coverage Map")
    out.append("")
    out.append("> **Generated** by `.github/scripts/ksat_coverage.py` from the units'")
    out.append("> `### NICE/DCWF KSATs` tables. Do not edit by hand. KSAT IDs are")
    out.append("> project-local (provisional) pending Framework Custodian mapping to official")
    out.append("> NICE/DCWF identifiers. See [`docs/maturity-models.md`](maturity-models.md).")
    out.append("")
    total = {"K": 0, "S": 0, "A": 0, "T": 0}
    for layer in by_layer:
        for k in total:
            total[k] += by_layer[layer][k]
    out.append(f"**Totals:** {total['K']} Knowledge · {total['S']} Skills · "
               f"{total['A']} Abilities · {total['T']} Tasks "
               f"across {len(files) - len(missing)}/{len(files)} units with KSATs authored.")
    out.append("")
    if missing:
        out.append(f"**KSATs pending ({len(missing)}):** {', '.join(sorted(missing))}")
        out.append("")

    out.append("## Coverage by degree layer")
    out.append("")
    out.append("| Layer | Knowledge | Skills | Abilities | Tasks |")
    out.append("|---|---|---|---|---|")
    for layer in LAYER_ORDER + [l for l in by_layer if l not in LAYER_ORDER]:
        if layer in by_layer:
            c = by_layer[layer]
            out.append(f"| {layer} | {c['K']} | {c['S']} | {c['A']} | {c['T']} |")
    out.append("")

    out.append("## Coverage by unit")
    out.append("")
    out.append("| Unit | Title | Layer | K | S | A | T |")
    out.append("|---|---|---|---|---|---|---|")
    for code, title, layer, c in per_unit:
        out.append(f"| {code} | {title} | {layer} | {c['K']} | {c['S']} | {c['A']} | {c['T']} |")
    out.append("")

    out.append("## Work-role coverage (NICE/DCWF)")
    out.append("")
    out.append("| Work role (code) | Units |")
    out.append("|---|---|")
    for role in sorted(roles):
        out.append(f"| {role} | {', '.join(sorted(roles[role]))} |")
    out.append("")

    out.append("## KSAT index")
    out.append("")
    out.append(f"{len(ksat_index)} KSAT items authored. Each is identifiable for coverage")
    out.append("metrics; statements are derived from unit content.")
    out.append("")
    out.append("| ID | Type | Unit | Statement |")
    out.append("|---|---|---|---|")
    type_name = {"K": "Knowledge", "S": "Skill", "A": "Ability", "T": "Task"}
    for code, letter, kid, stmt in sorted(ksat_index, key=lambda r: (r[0], r[1], r[2])):
        out.append(f"| {kid} | {type_name[letter]} | {code} | {stmt} |")
    out.append("")

    dest = Path("docs/ksat-coverage.md")
    dest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {dest} — {len(ksat_index)} KSAT items across "
          f"{len(files) - len(missing)}/{len(files)} units ({len(missing)} pending).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
