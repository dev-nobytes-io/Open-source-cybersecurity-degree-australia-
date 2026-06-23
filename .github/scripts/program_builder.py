#!/usr/bin/env python3
"""Program Builder — compose a study program and visualise the education gained.

Pick a designed degree preset, one or more majors, or an arbitrary set of
individual courses, and this renders a Markdown report of the KSAT (Knowledge,
Skills, Abilities, Tasks) education the selection delivers, using Mermaid:

  * a horizontal bar chart of NICE/DCWF work-role completion (% of each role's
    catalogue KSATs the selection covers);
  * four radar ("spider web") charts — one each for Knowledge, Skills,
    Abilities, and Tasks — plotting the selection against the full catalogue
    across every degree domain;
  * a pie chart of the selection's KSAT composition; and
  * a flowchart of the program structure by domain.

Every chart is backed by a plain table so the data survives even where a viewer
does not render Mermaid radar/xychart (these require Mermaid v11.6+ / v10.3+).

Examples
--------
  # A full designed degree (shared core + every major in the degree):
  python3 .github/scripts/program_builder.py --preset operations-degree

  # Shared core + a single major:
  python3 .github/scripts/program_builder.py --major TH --name "Threat Hunting"

  # Hand-pick individual courses (no core unless you add --core):
  python3 .github/scripts/program_builder.py --units F01,F06,OC02,TH03 --no-core

  # Regenerate the example pages committed under docs/program-builder/:
  python3 .github/scripts/program_builder.py --build-docs

KSAT IDs are project-local (provisional) pending Framework Custodian mapping to
official NICE/DCWF identifiers.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
UNIT_FILE_RE = re.compile(r"^(F|OC|SC|TH|DF|CT|DE|CE|SE|LD|GR|CAP)\d{2}-.*\.md$")
TYPE_LETTER = {"knowledge": "K", "skill": "S", "ability": "A", "task": "T"}
TYPE_NAME = {"K": "Knowledge", "S": "Skill", "A": "Ability", "T": "Task"}

# Prefix -> (domain label, short radar-axis label)
DOMAINS: dict[str, tuple[str, str]] = {
    "F": ("Foundation", "Foundation"),
    "OC": ("Operational Core", "Op Core"),
    "SC": ("Strategic Core", "Str Core"),
    "TH": ("Threat Hunting", "Threat Hunt"),
    "DF": ("DFIR", "DFIR"),
    "CT": ("Cyber Threat Intelligence", "CTI"),
    "DE": ("Detection Engineering", "Detection"),
    "CE": ("Cyber Threat Emulation", "Emulation"),
    "SE": ("Security Engineering", "Sec Eng"),
    "LD": ("Leadership & CISO", "Leadership"),
    "GR": ("Governance, Risk & Compliance", "GRC"),
}
DOMAIN_ORDER = list(DOMAINS)
SHARED_CORE = ["F", "OC", "SC"]
DEGREE_MAJORS = {
    "operational": ["TH", "DF", "CT", "DE", "CE"],
    "strategic": ["SE", "LD", "GR"],
}

# Named presets used for the committed example pages and quick CLI use.
PRESETS: dict[str, dict] = {
    "operations-degree": {
        "name": "Bachelor of Cybersecurity Operations (full degree)",
        "core": True, "degree": "operational",
        "blurb": "Shared core plus all five operational majors — the complete "
                 "operational degree surface.",
    },
    "strategy-degree": {
        "name": "Bachelor of Cybersecurity Strategy (full degree)",
        "core": True, "degree": "strategic",
        "blurb": "Shared core plus all three strategic majors — the complete "
                 "strategic degree surface.",
    },
    "threat-hunting": {
        "name": "Operations + Threat Hunting major",
        "core": True, "majors": ["TH"],
        "blurb": "A realistic single-major program: the 18-unit shared core plus "
                 "the six Threat Hunting units.",
    },
    "detection-engineering": {
        "name": "Operations + Detection Engineering major",
        "core": True, "majors": ["DE"],
        "blurb": "Shared core plus the six Detection Engineering units.",
    },
    "ciso-leadership": {
        "name": "Strategy + Leadership & CISO major",
        "core": True, "majors": ["LD"],
        "blurb": "Shared core plus the six Leadership & CISO units.",
    },
    "grc": {
        "name": "Strategy + GRC major",
        "core": True, "majors": ["GR"],
        "blurb": "Shared core plus the six Governance, Risk & Compliance units.",
    },
}


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #
def prefix_of(code: str) -> str:
    m = re.match(r"^([A-Z]+)\d", code)
    return m.group(1) if m else ""


def section(text: str, heading: str, level: str = "###") -> str:
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


class Unit:
    def __init__(self, path: Path):
        text = path.read_text(encoding="utf-8")
        self.code = (meta(text, "Unit Code") or path.name.split("-", 1)[0]).strip()
        self.title = meta(text, "Unit Title") or path.stem
        self.prefix = prefix_of(self.code)
        self.domain = DOMAINS.get(self.prefix, ("Other", "Other"))[0]
        # KSAT counts and items.
        self.counts = {"K": 0, "S": 0, "A": 0, "T": 0}
        for row in table_rows(section(text, "NICE/DCWF KSATs"))[1:]:
            if len(row) >= 3:
                letter = TYPE_LETTER.get(row[0].strip().lower())
                if letter:
                    self.counts[letter] += 1
        self.total = sum(self.counts.values())
        # Work-role codes (normalised to the role code column).
        self.roles: dict[str, str] = {}
        for row in table_rows(section(text, "NIST NICE DCWF"))[1:]:
            if len(row) >= 4 and row[2] and row[2].lower() not in ("work role", ""):
                code = re.sub(r"\s*\(.*?\)\s*", "", row[3]).strip()
                name = re.sub(r"\s*\(.*?\)\s*", "", row[2]).strip()
                if code:
                    self.roles.setdefault(code, name)


def load_units() -> dict[str, Unit]:
    units: dict[str, Unit] = {}
    for root in (ROOT / "core/units", ROOT / "degrees"):
        if root.exists():
            for p in sorted(root.rglob("*.md")):
                if UNIT_FILE_RE.match(p.name):
                    u = Unit(p)
                    units[u.code] = u
    return units


# --------------------------------------------------------------------------- #
# Selection
# --------------------------------------------------------------------------- #
def resolve_selection(units: dict[str, Unit], *, core: bool, degree: str | None,
                      majors: list[str], explicit: list[str]) -> list[str]:
    prefixes: list[str] = []
    if explicit:
        chosen = [c for c in explicit if c in units]
        unknown = [c for c in explicit if c not in units]
        if unknown:
            print(f"warning: unknown unit code(s) ignored: {', '.join(unknown)}", file=sys.stderr)
        if core:
            prefixes += SHARED_CORE
        sel = set(chosen)
        sel |= {c for c, u in units.items() if u.prefix in prefixes}
        return sorted(sel, key=lambda c: (DOMAIN_ORDER.index(units[c].prefix)
                                          if units[c].prefix in DOMAIN_ORDER else 99, c))
    if core:
        prefixes += SHARED_CORE
    if degree:
        prefixes += DEGREE_MAJORS.get(degree, [])
    prefixes += [m for m in majors if m in DOMAINS]
    sel = {c for c, u in units.items() if u.prefix in prefixes}
    return sorted(sel, key=lambda c: (DOMAIN_ORDER.index(units[c].prefix)
                                      if units[c].prefix in DOMAIN_ORDER else 99, c))


# --------------------------------------------------------------------------- #
# Metrics
# --------------------------------------------------------------------------- #
def role_completion(units: dict[str, Unit], selected: list[str]):
    """Return rows of (code, name, sel_ksats, total_ksats, pct) sorted by pct desc."""
    sel = set(selected)
    universe: dict[str, int] = defaultdict(int)
    covered: dict[str, int] = defaultdict(int)
    name_of: dict[str, str] = {}
    for code, u in units.items():
        for rcode, rname in u.roles.items():
            name_of.setdefault(rcode, rname)
            universe[rcode] += u.total
            if code in sel:
                covered[rcode] += u.total
    rows = []
    for rcode in universe:
        tot = universe[rcode]
        cov = covered[rcode]
        pct = round(100 * cov / tot) if tot else 0
        rows.append((rcode, name_of[rcode], cov, tot, pct))
    rows.sort(key=lambda r: (-r[4], r[0]))
    return rows


def domain_type_matrix(units: dict[str, Unit], selected: list[str]):
    """available[prefix][letter] and covered[prefix][letter] over present domains."""
    sel = set(selected)
    available = {p: {"K": 0, "S": 0, "A": 0, "T": 0} for p in DOMAIN_ORDER}
    covered = {p: {"K": 0, "S": 0, "A": 0, "T": 0} for p in DOMAIN_ORDER}
    for code, u in units.items():
        if u.prefix not in available:
            continue
        for k in "KSAT":
            available[u.prefix][k] += u.counts[k]
            if code in sel:
                covered[u.prefix][k] += u.counts[k]
    present = [p for p in DOMAIN_ORDER if any(available[p].values())]
    return present, available, covered


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def fence(body: str) -> list[str]:
    return ["```mermaid", body.rstrip(), "```", ""]


def render(units: dict[str, Unit], selected: list[str], *, name: str, blurb: str) -> str:
    sel_units = [units[c] for c in selected]
    totals = {"K": 0, "S": 0, "A": 0, "T": 0}
    for u in sel_units:
        for k in "KSAT":
            totals[k] += u.counts[k]
    grand = sum(totals.values())
    catalogue_total = sum(u.total for u in units.values())

    out: list[str] = []
    out.append(f"# Program: {name}")
    out.append("")
    out.append("> **Generated** by `.github/scripts/program_builder.py`. Do not edit by hand.")
    out.append("> KSAT IDs are project-local (provisional) pending Framework Custodian")
    out.append("> mapping to official NICE/DCWF identifiers. Charts use Mermaid radar")
    out.append("> (v11.6+) and xychart (v10.3+); each is backed by a table below it.")
    out.append("")
    if blurb:
        out.append(blurb)
        out.append("")
    out.append(f"**Selection:** {len(sel_units)} of {len(units)} units · "
               f"**{grand}** KSAT items "
               f"({totals['K']} K · {totals['S']} S · {totals['A']} A · {totals['T']} T) · "
               f"**{round(100 * grand / catalogue_total) if catalogue_total else 0}%** of the "
               f"full catalogue ({catalogue_total} items).")
    out.append("")

    # Selected units grouped by domain.
    by_domain: dict[str, list[Unit]] = defaultdict(list)
    for u in sel_units:
        by_domain[u.prefix].append(u)
    out.append("## Selected courses")
    out.append("")
    out.append("| Domain | Units |")
    out.append("|---|---|")
    for p in DOMAIN_ORDER:
        if by_domain.get(p):
            codes = ", ".join(u.code for u in by_domain[p])
            out.append(f"| {DOMAINS[p][0]} | {codes} |")
    out.append("")

    # --- 1. Role completion (horizontal bar) ---
    rows = [r for r in role_completion(units, selected) if r[3] > 0]
    out.append("## NICE/DCWF work-role completion")
    out.append("")
    out.append("Percentage of each work role's catalogue KSATs delivered by this selection "
               "(a role's KSAT universe is the sum of KSATs across every unit that develops it).")
    out.append("")
    if rows:
        codes = ", ".join(f'"{r[0]}"' for r in rows)
        pcts = ", ".join(str(r[4]) for r in rows)
        body = (
            "xychart-beta horizontal\n"
            '  title "Work-role KSAT completion (%)"\n'
            f"  x-axis [{codes}]\n"
            '  y-axis "Percent complete" 0 --> 100\n'
            f"  bar [{pcts}]"
        )
        out += fence(body)
        out.append("| Work role | Code | Covered | Catalogue | % |")
        out.append("|---|---|---|---|---|")
        for rcode, rname, cov, tot, pct in rows:
            out.append(f"| {rname} | {rcode} | {cov} | {tot} | {pct}% |")
        out.append("")

    # --- 2. Four radar charts (K, S, A, T) ---
    present, available, covered = domain_type_matrix(units, selected)
    out.append("## KSAT coverage by domain (spider charts)")
    out.append("")
    out.append("Each axis is a degree domain. The **Catalogue** curve is everything on offer; "
               "the **Selected** curve is what this program delivers. The gap between them is "
               "the breadth not taken.")
    out.append("")
    for letter in "KSAT":
        axis_max = max([available[p][letter] for p in present] + [1])
        axes = ", ".join(f'{p.lower()}["{DOMAINS[p][1]}"]' for p in present)
        avail_vals = ", ".join(str(available[p][letter]) for p in present)
        sel_vals = ", ".join(str(covered[p][letter]) for p in present)
        body = (
            "radar-beta\n"
            f"  title {TYPE_NAME[letter]} coverage by domain\n"
            f"  axis {axes}\n"
            f'  curve cat["Catalogue"]{{{avail_vals}}}\n'
            f'  curve sel["Selected"]{{{sel_vals}}}\n'
            f"  max {axis_max}\n"
            "  min 0"
        )
        out.append(f"### {TYPE_NAME[letter]}")
        out.append("")
        out += fence(body)
    # Backing table for the radars.
    out.append("**Domain × type — Selected / Catalogue**")
    out.append("")
    out.append("| Domain | Knowledge | Skills | Abilities | Tasks |")
    out.append("|---|---|---|---|---|")
    for p in present:
        cells = " | ".join(f"{covered[p][k]} / {available[p][k]}" for k in "KSAT")
        out.append(f"| {DOMAINS[p][0]} | {cells} |")
    out.append("")

    # --- 3. KSAT composition (pie) ---
    out.append("## KSAT composition of this program")
    out.append("")
    body = (
        'pie showData\n'
        '  title KSAT composition\n'
        f'  "Knowledge" : {totals["K"]}\n'
        f'  "Skills" : {totals["S"]}\n'
        f'  "Abilities" : {totals["A"]}\n'
        f'  "Tasks" : {totals["T"]}'
    )
    out += fence(body)

    # --- 4. Program structure (flowchart) ---
    out.append("## Program structure")
    out.append("")
    lines = ["flowchart LR", "  P([" + name.replace('"', "'") + "])"]
    for i, p in enumerate(DOMAIN_ORDER):
        if by_domain.get(p):
            nid = f"D{i}"
            label = f"{DOMAINS[p][0]}<br/>{len(by_domain[p])} units"
            lines.append(f'  P --> {nid}["{label}"]')
    out += fence("\n".join(lines))

    out.append("---")
    out.append("")
    out.append("_Build your own: "
               "`python3 .github/scripts/program_builder.py --help`._")
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_one(units, *, core, degree, majors, explicit, name, blurb, out_path) -> str:
    selected = resolve_selection(units, core=core, degree=degree, majors=majors, explicit=explicit)
    if not selected:
        print("error: selection is empty", file=sys.stderr)
        raise SystemExit(2)
    md = render(units, selected, name=name, blurb=blurb)
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(ROOT)} — {len(selected)} units")
    else:
        sys.stdout.write(md)
    return md


def build_docs(units) -> int:
    base = ROOT / "docs/program-builder"
    index = ["# Program Builder", "",
             "> Generated examples from `.github/scripts/program_builder.py`. "
             "Compose your own program from the designed degrees, one or more majors, "
             "or an arbitrary set of courses, and see the education it delivers as "
             "NICE/DCWF role completion and KSAT coverage.",
             "",
             "## How to build a program", "",
             "```bash",
             "# A designed degree (shared core + every major in the degree):",
             "python3 .github/scripts/program_builder.py --preset operations-degree",
             "",
             "# Shared core + a single major:",
             'python3 .github/scripts/program_builder.py --major TH --name "Threat Hunting"',
             "",
             "# Hand-pick individual courses:",
             "python3 .github/scripts/program_builder.py --units F01,F06,OC02,TH03 --no-core",
             "```",
             "",
             "## Example programs", ""]
    for key, cfg in PRESETS.items():
        out_path = base / f"{key}.md"
        build_one(units, core=cfg.get("core", True), degree=cfg.get("degree"),
                  majors=cfg.get("majors", []), explicit=[], name=cfg["name"],
                  blurb=cfg.get("blurb", ""), out_path=out_path)
        index.append(f"- [{cfg['name']}]({key}.md) — {cfg.get('blurb', '')}")
    index.append("")
    (base / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"Wrote {(base / 'index.md').relative_to(ROOT)}")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Compose a study program and visualise the KSAT education gained.")
    ap.add_argument("--preset", choices=sorted(PRESETS), help="named preset")
    ap.add_argument("--degree", choices=sorted(DEGREE_MAJORS), help="include all majors of a degree")
    ap.add_argument("--major", action="append", default=[], metavar="CODE",
                    help="major prefix to include (repeatable), e.g. TH, DE, GR")
    ap.add_argument("--units", default="", help="comma-separated individual unit codes")
    ap.add_argument("--core", dest="core", action="store_true", default=None,
                    help="include the 18-unit shared core (default on unless --units given)")
    ap.add_argument("--no-core", dest="core", action="store_false", help="exclude the shared core")
    ap.add_argument("--name", default=None, help="program name for the report")
    ap.add_argument("--out", default=None, help="output file (default: stdout)")
    ap.add_argument("--build-docs", action="store_true", help="regenerate docs/program-builder/ examples")
    ap.add_argument("--list", action="store_true", help="list presets, degrees, majors, and units")
    args = ap.parse_args(argv)

    units = load_units()
    if not units:
        print("error: no units found", file=sys.stderr)
        return 1

    if args.list:
        print("Presets:", ", ".join(sorted(PRESETS)))
        print("Degrees:", ", ".join(f"{d} ({'+'.join(DEGREE_MAJORS[d])})" for d in DEGREE_MAJORS))
        print("Majors :", ", ".join(f"{p} ({DOMAINS[p][0]})" for p in DOMAIN_ORDER if p not in SHARED_CORE))
        print(f"Units  : {len(units)} total")
        return 0

    if args.build_docs:
        return build_docs(units)

    explicit = [c.strip().upper() for c in args.units.split(",") if c.strip()]
    if args.preset:
        cfg = PRESETS[args.preset]
        core = cfg.get("core", True)
        degree = cfg.get("degree")
        majors = cfg.get("majors", [])
        name = args.name or cfg["name"]
        blurb = cfg.get("blurb", "")
    else:
        core = args.core if args.core is not None else (not explicit)
        degree = args.degree
        majors = [m.strip().upper() for m in args.major]
        name = args.name or "Custom program"
        blurb = ""

    out_path = (ROOT / args.out) if args.out else None
    build_one(units, core=core, degree=degree, majors=majors, explicit=explicit,
              name=name, blurb=blurb, out_path=out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
