#!/usr/bin/env python3
"""Lint unit content files against the mandatory template structure and the
content-standards quality rules.

Two severities:
  * ERROR   — fails the build (exit 1). Structural/objective rules the whole
              curriculum is expected to satisfy.
  * WARNING — reported but does not fail the build (exit 0). Advisory checks
              (e.g. Bloom's-verb level, framework-version consistency, internal
              links) that surface items for practitioner review without blocking
              CI on legitimate edge cases.

Usage:
    python3 .github/scripts/lint_units.py [path ...]

With no arguments it lints every unit file under `core/units/` and `degrees/`.
Exit code 0 = no errors (warnings allowed); 1 = one or more errors.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Unit files are named like F01-..., OC03-..., SC02-..., TH01-..., CAP01-...
UNIT_FILE_RE = re.compile(r"^(F|OC|SC|TH|DF|CT|DE|CE|SE|LD|GR|CAP)\d{2}-.*\.md$")
# A unit code token, e.g. F01, OC06, TH02, GR06.
CODE_RE = re.compile(r"\b(?:F|OC|SC|TH|DF|CT|DE|CE|SE|LD|GR|CAP)\d{2}\b")

REQUIRED_SECTIONS = [
    "Overview", "Prerequisites", "Learning Outcomes", "AQF Level 7 Alignment",
    "Framework Mappings", "Topics", "Labs & Exercises", "Assessment",
    "Australian Context", "Further Reading", "Unit Metadata",
]
MIN_TOPICS = 6
MIN_LABS = 2
MIN_REFERENCES = 5
REQUIRED_METADATA = ["Unit Code", "Unit Title", "Status", "Degree Layer", "Bloom's Level"]
PLACEHOLDER_TOKENS = [
    "YYYY-MM-DD", "[Unit Code]", "[Unit Title]", "[Bloom's verb]",
    "[complete outcome statement]", "[Lab Title]", "[Title]", "[Name / GitHub handle",
]

# Bloom's verb → level (1–6), from docs/content-standards.md §3.
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
# Degree Layer → minimum acceptable Bloom's level (content-standards §3).
LAYER_MIN_LEVEL = {
    "Foundation": 1, "Operational Core": 3, "Strategic Core": 3,
    "Major": 4, "Capstone": 5,
}
# Canonical framework version strings (token that must appear if the row exists).
VERSION_EXPECT = {
    "NICE DCWF": "2023", "SFIA": "SFIA 9", "ASD CSF": "2024", "MITRE ATT&CK": "v19",
}


def find_unit_files(paths: list[str]) -> list[Path]:
    if paths:
        selected = []
        for p in paths:
            path = Path(p)
            if UNIT_FILE_RE.match(path.name):
                selected.append(path)
            else:
                print(f"SKIP {path} (not a unit file)")
        return selected
    files: list[Path] = []
    for root in (Path("core/units"), Path("degrees")):
        if root.exists():
            files.extend(p for p in root.rglob("*.md") if UNIT_FILE_RE.match(p.name))
    return sorted(files)


def section_body(text: str, heading: str) -> str:
    m = re.search(
        r"^##\s+" + re.escape(heading) + r"\s*$(.*?)(?=^##\s|\Z)",
        text, re.MULTILINE | re.DOTALL,
    )
    return m.group(1) if m else ""


def metadata_value(text: str, field: str) -> str | None:
    """Return the value cell of a `| Field | Value |` metadata row."""
    m = re.search(r"^\|\s*" + re.escape(field) + r"\s*\|\s*(.+?)\s*\|", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def subsection_table_rows(text: str, subheading: str) -> list[list[str]]:
    """Return data rows (as cell lists) of the first markdown table under a `### subheading`."""
    body = re.search(
        r"^###\s+" + re.escape(subheading) + r"\s*$(.*?)(?=^###\s|^##\s|\Z)",
        text, re.MULTILINE | re.DOTALL,
    )
    if not body:
        return []
    rows = []
    for line in body.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s:|-]+\|$", line):  # separator row
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows[1:] if rows else []  # drop header row


def extract_codes(block: str) -> set[str]:
    return set(CODE_RE.findall(block))


def lint_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")

    # --- Structural (ERROR) ---
    if not re.search(r">\s*\*\*Status:\*\*", text):
        errors.append("missing '> **Status:**' header block")
    present = set(re.findall(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    for section in REQUIRED_SECTIONS:
        if section not in present:
            errors.append(f"missing required section: ## {section}")
    if len(re.findall(r"^###\s+Topic\s+\d+", text, re.MULTILINE)) < MIN_TOPICS:
        errors.append(f"fewer than {MIN_TOPICS} topics")
    if len(re.findall(r"^###\s+Lab\s+\d+", text, re.MULTILINE)) < MIN_LABS:
        errors.append(f"fewer than {MIN_LABS} labs")

    assessment = section_body(text, "Assessment")
    if "Formative Assessment" not in assessment:
        errors.append("Assessment missing a Formative Assessment")
    if "Summative Assessment" not in assessment:
        errors.append("Assessment missing a Summative Assessment")
    for level in ("Exemplary", "Proficient", "Developing", "Beginning"):
        if level not in assessment:
            errors.append(f"summative rubric missing '{level}' level")

    further = section_body(text, "Further Reading")
    if len([ln for ln in further.splitlines() if ln.strip().startswith(">")]) < MIN_REFERENCES:
        errors.append(f"fewer than {MIN_REFERENCES} annotated references")
    if "Australian source" not in further:
        errors.append("Further Reading must flag at least 1 'Australian source'")

    mappings = section_body(text, "Framework Mappings")
    if "ASD" not in mappings:
        errors.append("Framework Mappings must include an ASD (Australian) framework")

    metadata = section_body(text, "Unit Metadata")
    for field in REQUIRED_METADATA:
        if field not in metadata:
            errors.append(f"Unit Metadata missing field: {field}")

    for token in PLACEHOLDER_TOKENS:
        if token in text:
            errors.append(f"leftover template placeholder: {token!r}")

    # --- NICE DCWF T-code traceability (ERROR) ---
    nice_rows = subsection_table_rows(text, "NIST NICE DCWF")
    for row in nice_rows:
        if len(row) < 2:
            continue
        demonstrated_in = row[-1]
        if not demonstrated_in or demonstrated_in in {"—", "-", ""}:
            errors.append("NICE DCWF row has an empty 'Demonstrated In' (T-code not traceable)")
        elif not re.search(r"Lab|Activity|Assessment|Throughout", demonstrated_in, re.I):
            errors.append(
                f"NICE DCWF 'Demonstrated In' does not reference a lab/activity/assessment: {demonstrated_in!r}"
            )

    # --- Framework-version consistency (WARNING) ---
    for label, expect in VERSION_EXPECT.items():
        val = metadata_value(text, f"Framework Version — {label}")
        if val and expect not in val:
            warnings.append(f"framework version for {label} is {val!r}; expected to contain {expect!r}")

    # --- Bloom's-verb level vs layer (WARNING) ---
    layer = metadata_value(text, "Degree Layer")
    min_level = None
    if layer:
        for key, lvl in LAYER_MIN_LEVEL.items():
            if key.lower() in layer.lower():
                min_level = lvl
                break
    if min_level:
        lo_block = section_body(text, "Learning Outcomes")
        for m in re.finditer(r"^\d+\.\s+\*\*([A-Za-z]+)\*\*", lo_block, re.MULTILINE):
            verb = m.group(1).lower()
            lvl = BLOOM_VERB_LEVEL.get(verb)
            # One-level tolerance: the per-major TODOs sanction "apply" (L3) at
            # major level, so only flag verbs clearly below the layer's intent.
            if lvl is not None and lvl < min_level - 1:
                warnings.append(
                    f"learning-outcome verb '{m.group(1)}' (Bloom L{lvl}) is well below the "
                    f"expected L{min_level} for a {layer} unit"
                )

    # --- Internal markdown link resolution (WARNING) ---
    for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = m.group(1).split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not target.endswith(".md"):
            continue
        if not (path.parent / target).resolve().exists():
            warnings.append(f"internal link target not found: {target!r}")

    return errors, warnings


def check_prerequisite_graph(files: list[Path]) -> list[str]:
    """Cross-file ERROR checks: prerequisite codes exist, and the graph is acyclic."""
    errors: list[str] = []
    code_of: dict[Path, str] = {}
    prereqs: dict[str, set[str]] = {}
    for path in files:
        m = re.match(r"^([A-Z]+\d{2})-", path.name)
        if not m:
            continue
        code = m.group(1)
        code_of[path] = code
        text = path.read_text(encoding="utf-8")
        block = section_body(text, "Prerequisites")
        meta = metadata_value(text, "Prerequisites") or ""
        refs = (extract_codes(block) | extract_codes(meta)) - {code}
        prereqs[code] = refs
    all_codes = set(code_of.values())
    for code, refs in prereqs.items():
        for r in sorted(refs):
            if r not in all_codes:
                errors.append(f"{code}: prerequisite {r} does not correspond to any unit")

    # Cycle detection (DFS over the prerequisite graph, ignoring unknown refs).
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {c: WHITE for c in all_codes}

    def visit(node: str, stack: list[str]) -> None:
        colour[node] = GREY
        for nxt in sorted(prereqs.get(node, set())):
            if nxt not in all_codes:
                continue
            if colour[nxt] == GREY:
                cycle = " → ".join(stack[stack.index(nxt):] + [nxt]) if nxt in stack else f"{node} → {nxt}"
                errors.append(f"prerequisite cycle detected: {cycle}")
            elif colour[nxt] == WHITE:
                visit(nxt, stack + [nxt])
        colour[node] = BLACK

    for c in sorted(all_codes):
        if colour[c] == WHITE:
            visit(c, [c])
    return errors


def main(argv: list[str]) -> int:
    files = find_unit_files(argv[1:])
    if not files:
        print("No unit files found to lint.")
        return 0

    total_errors = 0
    total_warnings = 0
    for path in files:
        errors, warnings = lint_file(path)
        total_errors += len(errors)
        total_warnings += len(warnings)
        status = "FAIL" if errors else ("WARN" if warnings else "PASS")
        print(f"{status} {path}")
        for e in errors:
            print(f"  ERROR: {e}")
        for w in warnings:
            print(f"  warn:  {w}")

    # Cross-file prerequisite graph (only when linting the full set).
    if not argv[1:]:
        graph_errors = check_prerequisite_graph(files)
        if graph_errors:
            total_errors += len(graph_errors)
            print("FAIL <prerequisite graph>")
            for e in graph_errors:
                print(f"  ERROR: {e}")
        else:
            print("PASS <prerequisite graph> (all prerequisites exist; acyclic)")

    print()
    print(f"{len(files)} unit file(s); {total_errors} error(s), {total_warnings} warning(s).")
    if total_errors:
        print("Linting FAILED.")
        return 1
    print("Linting passed (warnings do not fail the build).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
