#!/usr/bin/env python3
"""Build the live Program Builder page.

This does NOT pre-render diagrams. It parses the units once and emits a single
self-contained page (`docs/program-builder/index.md`) that embeds the dataset
plus a small vanilla-JS app (`program_builder_app.js`). In the browser the user
ticks courses — grouped by degree / year / major, with search — and a set of
employability views update in real time:

  - NICE/DCWF work-role completion bars;
  - four radar ("spider web") charts on *different* category systems, framed
    around "what can I employ this person to do?":
      1. Operational capabilities / use-cases,
      2. NICE/DCWF work categories,
      3. Cognitive depth (Bloom's taxonomy of the learning outcomes),
      4. Learning mix (Knowledge / Skills / Abilities / Tasks);
  - a KSAT-composition donut;
  - and Save / Load (JSON) plus a printable program report.

Re-run this only when unit content changes (to refresh the embedded dataset),
the same cadence as `ksat_coverage.py`:

    python3 .github/scripts/program_builder.py

KSAT IDs and the capability mapping are project-local (provisional) pending
Framework Custodian mapping to official NICE/DCWF identifiers.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP_JS = Path(__file__).resolve().parent / "program_builder_app.js"
OUT = ROOT / "docs/program-builder/index.md"

UNIT_FILE_RE = re.compile(r"^(F|OC|SC|TH|DF|CT|DE|CE|SE|LD|GR|CAP)\d{2}-.*\.md$")
TYPE_LETTER = {"knowledge": "K", "skill": "S", "ability": "A", "task": "T"}

DOMAINS = {
    "F": ("Foundation", "Foundation"), "OC": ("Operational Core", "Op Core"),
    "SC": ("Strategic Core", "Str Core"), "TH": ("Threat Hunting", "Threat Hunt"),
    "DF": ("DFIR", "DFIR"), "CT": ("Cyber Threat Intelligence", "CTI"),
    "DE": ("Detection Engineering", "Detection"), "CE": ("Cyber Threat Emulation", "Emulation"),
    "SE": ("Security Engineering", "Sec Eng"), "LD": ("Leadership & CISO", "Leadership"),
    "GR": ("Governance, Risk & Compliance", "GRC"),
}
DOMAIN_ORDER = list(DOMAINS)
DEGREE_OF = {p: "Shared Core" for p in ("F", "OC", "SC")}
DEGREE_OF.update({p: "Operational" for p in ("TH", "DF", "CT", "DE", "CE")})
DEGREE_OF.update({p: "Strategic" for p in ("SE", "LD", "GR")})
DEGREE_ORDER = ["Shared Core", "Operational", "Strategic"]
YEAR_OF = {
    "F": "Year 1 · Foundation", "OC": "Year 2 · Operational Core",
    "SC": "Year 2 · Strategic Core",
}
SHARED = ["F", "OC", "SC"]
OPS_MAJORS = ["TH", "DF", "CT", "DE", "CE"]
STR_MAJORS = ["SE", "LD", "GR"]

# Bloom's verb -> cognitive level (kept in sync with lint_units.py).
BLOOM_VERB_LEVEL = {
    "define": 1, "list": 1, "recall": 1, "recognise": 1, "identify": 1, "name": 1, "state": 1,
    "describe": 2, "explain": 2, "summarise": 2, "classify": 2, "interpret": 2,
    "paraphrase": 2, "discuss": 2, "illustrate": 2,
    "apply": 3, "use": 3, "demonstrate": 3, "execute": 3, "implement": 3, "solve": 3,
    "perform": 3, "operate": 3,
    "analyse": 4, "compare": 4, "differentiate": 4, "examine": 4, "categorise": 4,
    "distinguish": 4, "break": 4,
    "evaluate": 5, "assess": 5, "critique": 5, "justify": 5, "prioritise": 5,
    "appraise": 5, "recommend": 5, "argue": 5,
    "create": 6, "design": 6, "develop": 6, "produce": 6, "construct": 6,
    "synthesise": 6, "formulate": 6, "plan": 6,
}
BLOOM_LABELS = ["Remember", "Understand", "Apply", "Analyse", "Evaluate", "Create"]

# Employer-facing capability ("what can I employ them to do?"). Curated mapping,
# project-local/provisional. Per-prefix default with per-code overrides.
CAPABILITY_ORDER = [
    "Foundations", "Detect & Monitor", "Respond & Recover", "Hunt",
    "Investigate / Forensics", "Threat Intelligence", "Emulate / Offensive",
    "Architect & Engineer", "Govern, Risk & Comply", "Lead & Communicate",
]
CAP_BY_PREFIX = {
    "F": "Foundations", "TH": "Hunt", "DF": "Investigate / Forensics",
    "CT": "Threat Intelligence", "DE": "Detect & Monitor", "CE": "Emulate / Offensive",
    "SE": "Architect & Engineer", "LD": "Lead & Communicate", "GR": "Govern, Risk & Comply",
}
CAP_BY_CODE = {
    "F05": "Govern, Risk & Comply", "F06": "Detect & Monitor",
    "OC01": "Detect & Monitor", "OC02": "Detect & Monitor", "OC03": "Investigate / Forensics",
    "OC04": "Respond & Recover", "OC05": "Threat Intelligence", "OC06": "Emulate / Offensive",
    "SC01": "Govern, Risk & Comply", "SC02": "Architect & Engineer", "SC03": "Govern, Risk & Comply",
    "SC04": "Govern, Risk & Comply", "SC05": "Lead & Communicate", "SC06": "Lead & Communicate",
    "DF05": "Respond & Recover", "DF06": "Respond & Recover", "SE04": "Detect & Monitor",
}

# NICE/DCWF work category from the role-code prefix.
NICE_OF = {
    "AN": "Analyze", "CO": "Collect & Operate", "IN": "Investigate", "OM": "Operate & Maintain",
    "OV": "Oversee & Govern", "PR": "Protect & Defend", "SP": "Securely Provision",
}
NICE_ORDER = ["Protect & Defend", "Analyze", "Investigate", "Operate & Maintain",
              "Securely Provision", "Oversee & Govern", "Collect & Operate"]


def prefix_of(code: str) -> str:
    m = re.match(r"^([A-Z]+)\d", code)
    return m.group(1) if m else ""


def sub_section(text: str, heading: str) -> str:
    m = re.search(r"^###\s+" + re.escape(heading) + r"\s*$(.*?)(?=^#{1,3}\s|\Z)",
                  text, re.MULTILINE | re.DOTALL)
    return m.group(1) if m else ""


def top_section(text: str, heading: str) -> str:
    m = re.search(r"^##\s+" + re.escape(heading) + r"\s*$(.*?)(?=^##\s|\Z)",
                  text, re.MULTILINE | re.DOTALL)
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


def parse_units() -> list[dict]:
    units = []
    for root in (ROOT / "core/units", ROOT / "degrees"):
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if not UNIT_FILE_RE.match(path.name):
                continue
            text = path.read_text(encoding="utf-8")
            code = (meta(text, "Unit Code") or path.name.split("-", 1)[0]).strip()
            prefix = prefix_of(code)

            counts = {"K": 0, "S": 0, "A": 0, "T": 0}
            ksats = []
            for row in table_rows(sub_section(text, "NICE/DCWF KSATs"))[1:]:
                if len(row) >= 3:
                    letter = TYPE_LETTER.get(row[0].strip().lower())
                    if letter:
                        counts[letter] += 1
                        dem = row[3] if len(row) >= 4 else ""
                        ksats.append([letter, row[1], row[2], dem])

            roles: dict[str, str] = {}
            for row in table_rows(sub_section(text, "NIST NICE DCWF"))[1:]:
                if len(row) >= 4 and row[2] and row[2].lower() not in ("work role", ""):
                    rcode = re.sub(r"\s*\(.*?\)\s*", "", row[3]).strip()
                    rname = re.sub(r"\s*\(.*?\)\s*", "", row[2]).strip()
                    if rcode:
                        roles.setdefault(rcode, rname)

            bloom = [0, 0, 0, 0, 0, 0]
            lo = top_section(text, "Learning Outcomes")
            for m in re.finditer(r"^\d+\.\s+\*\*([A-Za-z]+)\*\*", lo, re.MULTILINE):
                lvl = BLOOM_VERB_LEVEL.get(m.group(1).lower())
                if lvl:
                    bloom[lvl - 1] += 1

            units.append({
                "code": code,
                "title": meta(text, "Unit Title") or path.stem,
                "prefix": prefix,
                "degree": DEGREE_OF.get(prefix, "Shared Core"),
                "year": YEAR_OF.get(prefix, "Year 3 · Specialisation"),
                "area": DOMAINS.get(prefix, ("Other", "Other"))[0],
                "cap": CAP_BY_CODE.get(code, CAP_BY_PREFIX.get(prefix, "Foundations")),
                "k": counts["K"], "s": counts["S"], "a": counts["A"], "t": counts["T"],
                "bloom": bloom,
                "roles": [[c, n] for c, n in roles.items()],
                "ksats": ksats,
            })
    order = {p: i for i, p in enumerate(DOMAIN_ORDER)}
    units.sort(key=lambda u: (order.get(u["prefix"], 99), u["code"]))
    return units


def codes_for(units, prefixes) -> list[str]:
    s = set(prefixes)
    return [u["code"] for u in units if u["prefix"] in s]


def build_presets(units) -> list[dict]:
    presets = [
        {"label": "Operations degree", "units": codes_for(units, SHARED + OPS_MAJORS)},
        {"label": "Strategy degree", "units": codes_for(units, SHARED + STR_MAJORS)},
        {"label": "Shared core", "units": codes_for(units, SHARED)},
        {"label": "All 66 courses", "units": [u["code"] for u in units]},
    ]
    for p in OPS_MAJORS + STR_MAJORS:
        presets.append({"label": "Core + " + DOMAINS[p][0], "units": codes_for(units, SHARED + [p])})
    return presets


STYLE = """<style>
.pb-app{--pb-sel:#7e57c2;}
.pb-topbar{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin:.4rem 0 1rem;}
.pb-name{flex:1 1 16rem;padding:.45rem .6rem;border:1px solid #cfd4da;border-radius:6px;font-size:.9rem;}
.pb-actions{display:flex;gap:.4rem;flex-wrap:wrap;}
.pb-act{font-size:.78rem;padding:.4rem .7rem;border:1px solid var(--pb-sel);background:var(--pb-sel);color:#fff;border-radius:6px;cursor:pointer;}
.pb-act.pb-ghost{background:transparent;color:var(--pb-sel);}
.pb-grid{display:grid;grid-template-columns:340px 1fr;gap:1.4rem;align-items:start;}
@media(max-width:900px){.pb-grid{grid-template-columns:1fr;}}
.pb-app input[type=search]{width:100%;padding:.45rem .6rem;margin:.2rem 0 .6rem;border:1px solid #cfd4da;border-radius:6px;font-size:.85rem;}
.pb-presets{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:.6rem;}
.pb-btn{font-size:.72rem;padding:.28rem .5rem;border:1px solid var(--pb-sel);background:transparent;color:var(--pb-sel);border-radius:14px;cursor:pointer;}
.pb-btn:hover{background:var(--pb-sel);color:#fff;}
.pb-btn-clear{border-color:#b0bec5;color:#607d8b;}
.pb-tree{max-height:560px;overflow:auto;border:1px solid #e3e6ea;border-radius:8px;padding:.4rem .6rem;}
.pb-deg{margin:.2rem 0;}
.pb-deg>summary{cursor:pointer;font-weight:700;list-style:none;display:flex;align-items:center;gap:.4rem;padding:.25rem 0;}
.pb-deg>summary::-webkit-details-marker{display:none;}
.pb-count{margin-left:auto;font-size:.7rem;color:#78909c;font-weight:600;}
.pb-year{font-size:.7rem;text-transform:uppercase;letter-spacing:.04em;color:#90a4ae;margin:.5rem 0 .1rem;}
.pb-area{margin:.1rem 0 .3rem .2rem;}
.pb-area-h{display:flex;align-items:center;gap:.4rem;font-weight:600;font-size:.8rem;cursor:pointer;}
.pb-unit{display:flex;align-items:center;gap:.4rem;font-size:.8rem;padding:.08rem 0 .08rem 1.3rem;cursor:pointer;}
.pb-unit:hover{background:rgba(126,87,194,.07);border-radius:4px;}
.pb-code{font-weight:600;flex:0 0 auto;min-width:3.2em;}
.pb-title{color:#546e7a;}
.pb-summary{font-size:.92rem;margin:.2rem 0 1rem;padding:.5rem .7rem;background:rgba(126,87,194,.08);border-radius:8px;}
.pb-bar-row{display:flex;align-items:center;gap:.5rem;margin:.18rem 0;font-size:.78rem;}
.pb-bar-label{flex:0 0 6.5em;font-weight:600;}
.pb-bar-track{flex:1 1 auto;height:14px;background:#eceff1;border-radius:7px;overflow:hidden;}
.pb-bar-fill{height:100%;background:var(--pb-sel);border-radius:7px;transition:width .25s;}
.pb-bar-fill.pb-bar-zero{background:#cfd8dc;}
.pb-bar-pct{flex:0 0 2.8em;text-align:right;font-variant-numeric:tabular-nums;color:#546e7a;}
.pb-radars{display:grid;grid-template-columns:repeat(2,1fr);gap:.4rem;}
@media(max-width:560px){.pb-radars{grid-template-columns:1fr;}}
.pb-help{font-size:.78rem;color:#607d8b;margin:.1rem 0 .4rem;}
.pb-radar-card h4{margin:.4rem 0 0;font-size:.85rem;}
.pb-radar-card p{margin:.1rem 0 0;font-size:.72rem;color:#78909c;}
.pb-radar{width:100%;height:auto;color:#455a64;}
.pb-legend-row{font-size:.72rem;color:#78909c;margin:.2rem 0 .8rem;}
.pb-legend-row .pb-sw{display:inline-block;width:.7em;height:.7em;border-radius:2px;margin:0 .3rem 0 .8rem;vertical-align:middle;}
.pb-donut-wrap{display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap;}
.pb-donut{width:130px;height:130px;color:#37474f;}
.pb-legend{display:flex;flex-direction:column;gap:.25rem;font-size:.8rem;}
.pb-legend-item{display:flex;align-items:center;}
.pb-swatch{display:inline-block;width:.8em;height:.8em;border-radius:2px;margin-right:.4rem;}
[data-md-color-scheme=slate] .pb-tree{border-color:#37474f;}
[data-md-color-scheme=slate] .pb-bar-track{background:#37474f;}
</style>"""

CONTAINER = """<div class="pb-app" markdown="0">
<div class="pb-topbar">
<input id="pb-name" class="pb-name" type="text" placeholder="Name this program (e.g. SOC Analyst pathway)…" aria-label="Program name">
<div class="pb-actions">
<button id="pb-save" class="pb-act pb-ghost" type="button">Save</button>
<button id="pb-load" class="pb-act pb-ghost" type="button">Load</button>
<button id="pb-print" class="pb-act" type="button">Print report</button>
<input id="pb-file" type="file" accept="application/json,.json" hidden>
</div>
</div>
<div class="pb-grid">
<div class="pb-controls">
<input id="pb-search" type="search" placeholder="Search courses by code or title…" aria-label="Search courses">
<div id="pb-presets" class="pb-presets"></div>
<div id="pb-tree" class="pb-tree"></div>
</div>
<div class="pb-output">
<div id="pb-summary" class="pb-summary"></div>
<h3>NICE/DCWF work-role completion</h3>
<div id="pb-bars"></div>
<h3>What can I employ this person to do?</h3>
<p class="pb-help">Each chart compares <b>this program</b> (filled) against the <b>full catalogue</b> (outer ring), per axis — the shape shows where it is strong or thin. The <b>Capability profile</b> reads the KSATs as employability, each tied to the matching depth of learning: <b>Knows</b> = knowledge &amp; understanding, <b>Can do</b> = skills &amp; application, <b>Unique</b> = abilities, evaluation &amp; creation (distinctive judgement), <b>Has done</b> = tasks &amp; analysis performed.</p>
<div class="pb-legend-row"><span class="pb-sw" style="background:#9aa7b4"></span>Full catalogue (reference)<span class="pb-sw" style="background:#7e57c2"></span>This program</div>
<div id="pb-radars" class="pb-radars"></div>
<h3>Learning composition</h3>
<div id="pb-donut"></div>
</div>
</div>
</div>"""


def main() -> int:
    units = parse_units()
    nice_present = [c for c in NICE_ORDER if any(
        NICE_OF.get(r[0].split("-")[0]) == c for u in units for r in u["roles"])]
    data = {
        "units": units,
        "degreeOrder": DEGREE_ORDER,
        "presets": build_presets(units),
        "capabilityOrder": CAPABILITY_ORDER,
        "niceOf": NICE_OF,
        "niceOrder": nice_present,
        "bloomLabels": BLOOM_LABELS,
    }
    app_js = APP_JS.read_text(encoding="utf-8")
    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    intro = [
        "# Program Builder",
        "",
        "**Build your own program — no scripts, no installs.** Tick the courses you "
        "want (use the search box and the presets, or expand the groups below), from "
        "a designed-degree preset, one or more majors, or any individual mix. As you "
        "select, the views below redraw instantly to answer one question: **what can "
        "I employ this person to do?**",
        "",
        "- **Work-role completion** — how fully the program covers each NICE/DCWF role.",
        "- **Four capability lenses** (each a *different* category system): operational "
        "capabilities/use-cases, NICE work categories, cognitive depth (Bloom's), and "
        "the knowledge-vs-doing mix.",
        "- **Save / Load** a selection as JSON, or **Print** a full program report "
        "(courses, coverage, and every KSAT).",
        "",
        "Courses are grouped by **degree → year → major**; each group has a "
        "select-all checkbox. The full text index lives at "
        "[`../ksat-coverage.md`](../ksat-coverage.md).",
        "",
        "!!! note \"Viewing this on the published docs site\"",
        "    The live charts run in your browser, so use the published documentation "
        "site (GitHub Pages). On GitHub's raw file view the JavaScript does not run, "
        "so you would see the page text but not the interactive picker or charts.",
        "",
        "<!-- Dataset regenerated by maintainers with "
        "`python3 .github/scripts/program_builder.py` whenever unit content changes; "
        "readers never run anything. KSAT IDs and the capability mapping are "
        "project-local (provisional) pending Framework Custodian mapping. -->",
        "",
    ]
    page = "\n".join(intro) + STYLE + "\n" + CONTAINER + "\n"
    page += '<script>window.PROGRAM_DATA=' + data_json + ';</script>\n'
    page += "<script>\n" + app_js + "\n</script>\n"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} — {len(units)} units embedded "
          f"({len(data_json)} bytes data, {len(app_js)} bytes app).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
