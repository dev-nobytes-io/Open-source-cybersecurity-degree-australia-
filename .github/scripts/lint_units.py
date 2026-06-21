#!/usr/bin/env python3
"""Lint unit content files against the mandatory template structure.

This checker enforces the structural requirements from
`docs/content-standards.md` and `templates/unit-template.md`. It is intentionally
structural — it cannot judge the *quality* of content (that is what practitioner
review is for), but it catches missing sections, too-few topics/labs/references,
missing rubrics, and leftover template placeholders before a PR is reviewed.

Usage:
    python3 .github/scripts/lint_units.py [path ...]

With no arguments it lints every unit file under `core/units/` and `degrees/`.
Exit code 0 = all files pass; 1 = one or more files failed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Unit files are named like F01-..., OC03-..., SC02-..., TH01-..., CAP01-...
UNIT_FILE_RE = re.compile(r"^(F|OC|SC|TH|DF|CT|DE|CE|SE|LD|GR|CAP)\d{2}-.*\.md$")

# Required top-level (##) sections, in no particular order.
REQUIRED_SECTIONS = [
    "Overview",
    "Prerequisites",
    "Learning Outcomes",
    "AQF Level 7 Alignment",
    "Framework Mappings",
    "Topics",
    "Labs & Exercises",
    "Assessment",
    "Australian Context",
    "Further Reading",
    "Unit Metadata",
]

# Minimums from docs/content-standards.md.
MIN_TOPICS = 6
MIN_LABS = 2
MIN_REFERENCES = 5

# Required metadata fields (substring match within the metadata table).
REQUIRED_METADATA = [
    "Unit Code",
    "Unit Title",
    "Status",
    "Degree Layer",
    "Bloom's Level",
]

# Leftover template placeholders that must never appear in a finished unit.
PLACEHOLDER_TOKENS = [
    "YYYY-MM-DD",
    "[Unit Code]",
    "[Unit Title]",
    "[Bloom's verb]",
    "[complete outcome statement]",
    "[Lab Title]",
    "[Title]",
    "[Name / GitHub handle",
]


def find_unit_files(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p) for p in paths]
    roots = [Path("core/units"), Path("degrees")]
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(
                p for p in root.rglob("*.md") if UNIT_FILE_RE.match(p.name)
            )
    return sorted(files)


def section_body(text: str, heading: str) -> str:
    """Return the text under a `## heading` up to the next `## `."""
    pattern = re.compile(
        r"^##\s+" + re.escape(heading) + r"\s*$(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(text)
    return m.group(1) if m else ""


def lint_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    # Status header near the top.
    if not re.search(r">\s*\*\*Status:\*\*", text):
        errors.append("missing '> **Status:**' header block")

    # Required sections.
    present = set(re.findall(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    for section in REQUIRED_SECTIONS:
        if section not in present:
            errors.append(f"missing required section: ## {section}")

    # Topic / Lab counts.
    topics = re.findall(r"^###\s+Topic\s+\d+", text, re.MULTILINE)
    if len(topics) < MIN_TOPICS:
        errors.append(f"only {len(topics)} topics; need >= {MIN_TOPICS}")
    labs = re.findall(r"^###\s+Lab\s+\d+", text, re.MULTILINE)
    if len(labs) < MIN_LABS:
        errors.append(f"only {len(labs)} labs; need >= {MIN_LABS}")

    # Assessment: formative + summative + a 4-level rubric.
    assessment = section_body(text, "Assessment")
    if "Formative Assessment" not in assessment:
        errors.append("Assessment section missing a Formative Assessment")
    if "Summative Assessment" not in assessment:
        errors.append("Assessment section missing a Summative Assessment")
    for level in ("Exemplary", "Proficient", "Developing", "Beginning"):
        if level not in assessment:
            errors.append(f"summative rubric missing '{level}' level")

    # Further Reading: count annotation blockquote lines.
    further = section_body(text, "Further Reading")
    annotations = [ln for ln in further.splitlines() if ln.strip().startswith(">")]
    if len(annotations) < MIN_REFERENCES:
        errors.append(
            f"only {len(annotations)} annotated references; need >= {MIN_REFERENCES}"
        )
    if "Australian source" not in further:
        errors.append("Further Reading must flag at least 1 'Australian source'")

    # Framework mappings: ASD must appear (at least 1 Australian framework).
    mappings = section_body(text, "Framework Mappings")
    if "ASD" not in mappings:
        errors.append("Framework Mappings must include an ASD (Australian) framework")

    # Metadata fields.
    metadata = section_body(text, "Unit Metadata")
    for field in REQUIRED_METADATA:
        if field not in metadata:
            errors.append(f"Unit Metadata missing field: {field}")

    # Leftover placeholders.
    for token in PLACEHOLDER_TOKENS:
        if token in text:
            errors.append(f"leftover template placeholder: {token!r}")

    return errors


def main(argv: list[str]) -> int:
    files = find_unit_files(argv[1:])
    if not files:
        print("No unit files found to lint.")
        return 0

    total_errors = 0
    for path in files:
        errors = lint_file(path)
        if errors:
            total_errors += len(errors)
            print(f"FAIL {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"PASS {path}")

    print()
    if total_errors:
        print(f"Linting failed: {total_errors} issue(s) across unit files.")
        return 1
    print(f"All {len(files)} unit file(s) passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
