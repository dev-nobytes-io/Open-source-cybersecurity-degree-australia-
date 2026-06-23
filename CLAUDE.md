# CLAUDE.md — guidance for AI agents working in this repository

This is an open-source **Australian cybersecurity degree** (two AQF Level 7 /
TEQSA-aligned degrees, 66 units, mapped to NICE/DCWF, SFIA 9, ASD, MITRE ATT&CK).
Read this file at the start of a session, and **re-read the rule documents below
every now and then** — at minimum before any substantial content change, and
periodically during long sessions so the rules stay fresh rather than drifting
from memory.

## Re-read these regularly (canonical rules — memory is not a substitute)

| Document | What it governs |
|---|---|
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Core rules **R1–R7**, PR process, naming, licensing (CC BY 4.0) |
| [`docs/content-standards.md`](docs/content-standards.md) | **Authoritative** unit structure, mandatory sections, Bloom's levels by layer, framework-mapping + KSAT spec |
| [`docs/governance.md`](docs/governance.md) | Roles (Domain Expert, Practitioner Reviewer, Framework Custodian) and the content lifecycle |
| [`docs/review/index.md`](docs/review/index.md) | Phase 4 review process, dashboards, framework-verification tracker |
| [`docs/compliance/`](docs/compliance/) | AQF/TEQSA, workforce-framework, and delivery requirements |
| [`STATUS.md`](STATUS.md) · [`SPRINTS.md`](SPRINTS.md) · [`TODO.md`](TODO.md) | Current state, sprint log, open work |

**Core rules in one line each (see CONTRIBUTING.md for the full text):**
R1 framework mapping is mandatory · R2 practitioner review for major content ·
R3 no vendor lock-in in core content (free/OSS labs) · R4 Australian context
required for legal/regulatory topics · R5 accuracy over speed (flag what you
can't verify) · R6 no plagiarism · R7 respectful conduct.

> The **authoritative** unit structure is `docs/content-standards.md` as enforced
> by `.github/scripts/lint_units.py` — the prose example in CONTRIBUTING.md is a
> simplified sketch. When they differ, follow the standards doc + the linter.

## Working conventions for agents

- **Verify, don't assume.** Before claiming a change follows the rules, check it
  (lint, build, grep). Report failures honestly; flag anything provisional.
- **Provisional / pending practitioner sign-off:** project-local KSAT IDs
  (`<UNIT>-K01`…), the Program Builder capability mapping, MITRE ATT&CK **v19**
  technique IDs, and exact citations (SANS PIR guide, "DF-C2M2"). Don't present
  these as verified; they are Phase 4 items.
- **Prefer generators over hand-editing generated files.** These read the units
  and must be re-run when unit content changes (the files say "do not edit by
  hand"):
  - `python3 .github/scripts/ksat_coverage.py` → `docs/ksat-coverage.md`
  - `python3 .github/scripts/program_builder.py` → `docs/program-builder/index.md` + `team.md`
  - `python3 .github/scripts/review_dashboard.py` → `docs/review/dashboard.md`
- **Always pass the checks before committing:**
  - `python3 .github/scripts/lint_units.py` (0 errors required; warnings are advisory)
  - `python3 .github/prepare_wiki.py && python3 -m mkdocs build --strict` (exit 0)
- **Naming:** unit-code prefixes are `F, OC, SC, TH, DF, CT, DE, CE, SE, LD, GR`
  (+ `CAP`); files `lowercase-with-hyphens`.
- **MkDocs staging:** `docs_dir` is `wiki_src/`, populated by `prepare_wiki.py`,
  which only copies `*.md` and renames `templates/` → `resources/`. Self-contained
  interactive pages embed their own data/JS so no extra assets need staging; link
  to repo files (e.g. `templates/…`) by full GitHub URL to survive `--strict`.

## Git / PR conventions

- Commit messages end with the **Co-Authored-By** and **Claude-Session** trailers
  exactly as given in the runtime instructions. PR bodies end with the **"Generated
  with Claude Code"** footer + session link. Open PRs as **draft**.
- **Do not** put the exact model identifier in commit messages, PR titles/bodies,
  code comments, or any committed file — keep it to chat only.
- Push with `git push -u origin <branch>`; after pushing, open (or update) a PR.
- **Branch policy:** if the runtime instructions name a designated branch, develop
  there and don't push elsewhere without explicit permission. Otherwise, one
  feature branch per PR (e.g. `claude/<short-topic>`) off `main` is the norm.
  Never commit directly to `main`.
- Use the **GitHub MCP tools** (`mcp__github__*`), not the `gh` CLI.
