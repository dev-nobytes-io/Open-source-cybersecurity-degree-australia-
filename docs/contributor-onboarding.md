# Contributor Onboarding Checklist

Welcome. This checklist takes you from "I want to help" to your first merged
contribution. It complements [`CONTRIBUTING.md`](../CONTRIBUTING.md) (the rules)
by giving you an ordered, practical path. If anything here conflicts with
`CONTRIBUTING.md`, `CONTRIBUTING.md` wins.

---

## 1. Get oriented

- [ ] Read [`CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution rules and PR process
- [ ] Skim [`docs/content-standards.md`](content-standards.md) — the mandatory bar every unit must meet
- [ ] Skim [`docs/governance.md`](governance.md) — the content lifecycle and who signs off
- [ ] Look at a finished example unit (e.g. `core/units/F01-networking-fundamentals.md`) to see the standard

## 2. Find work that isn't already taken

- [ ] Open the [unit status dashboard](../STATUS.md) and pick a unit marked ⬜ Planned
- [ ] Check the [unit assignment register](unit-assignments.md) — make sure no one has claimed it
- [ ] Check open issues for an existing "New Unit Draft" claim on that unit

## 3. Claim it

- [ ] Open a **New Unit Draft** issue (Issues → New issue → "New Unit Draft")
- [ ] Add a row (or update the row) for your unit in [`docs/unit-assignments.md`](unit-assignments.md) via a small PR
- [ ] This prevents two people drafting the same unit

## 4. Author the unit

- [ ] Copy `templates/unit-template.md` to the correct path (see naming rules in `docs/content-standards.md` §2)
- [ ] Fill in **every** section — do not delete template sections
- [ ] Use the correct **Bloom's level** for the layer (Foundation 1–3, Core 3–4, Major 4–5, Capstone 5–6)
- [ ] Write **≥ 6 substantive topics** (real content, not headings)
- [ ] Write **≥ 2 complete labs** — free/OSS tools for Foundation/Core; within 8 GB RAM / 4-core / 50 GB
- [ ] Write **1 formative + 1 summative** assessment, with a **4-level rubric**
- [ ] Complete **framework mappings** — ≥ 2 frameworks, ≥ 1 Australian (ASD), every T-code traceable to a lab/assessment
- [ ] Add **Australian context** woven through the content
- [ ] Add **≥ 5 annotated references**, ≥ 1 Australian source
- [ ] Complete the **Unit Metadata** table
- [ ] Remove all `[bracketed placeholders]`

## 5. Self-check before opening a PR

- [ ] Run the linter locally: `python3 .github/scripts/lint_units.py core/units/<your-file>.md`
- [ ] Fix every **ERROR** it reports — errors fail CI (warnings are advisory and do not)
- [ ] The linter checks: required sections, ≥6 topics / ≥2 labs, 4-level rubric, ≥5
  refs (incl. an Australian source), an ASD framework mapping, metadata fields, no
  leftover placeholders, **every NICE DCWF T-code traceable to a named lab/activity/
  assessment**, and (across the full set) that **prerequisites exist and form an
  acyclic graph**. Advisory warnings cover Bloom's-verb level, framework-version
  consistency, and internal-link resolution.
- [ ] Run the full set too (`python3 .github/scripts/lint_units.py`) so the
  prerequisite-graph check runs — the same as CI
- [ ] If you changed unit content, **regenerate the dashboards** and commit them
  (CI fails if they're stale): `python3 .github/scripts/ksat_coverage.py`,
  `python3 .github/scripts/program_builder.py`, `python3 .github/scripts/review_dashboard.py`
- [ ] Build the docs strictly (as CI does):
  `python3 .github/prepare_wiki.py && python3 -m mkdocs build --strict`
- [ ] Update the unit's row in [`STATUS.md`](../STATUS.md) to 🟡 Draft

## 6. Open the PR and request review

- [ ] Open a pull request; the **QA / QC** check must pass (it runs the linter,
  validates the builder JavaScript, confirms the generated dashboards are up to
  date, and builds the docs with `--strict`)
- [ ] Open a **Unit Review Request** issue (or link the PR) and tag a Domain Expert and Practitioner Reviewer
- [ ] Respond to review feedback; reviewers sign off per `docs/governance.md`
- [ ] On merge, update `STATUS.md` and `docs/unit-assignments.md` to reflect the new status

---

## First contribution too big?

You don't have to author a whole unit to help. Good smaller first contributions:

- Fix a **framework mapping** (open a "Framework Mapping Error" issue or PR)
- Add or improve an **annotated reference** in an existing unit
- Improve a **lab's** clarity or expected-output description
- Strengthen the **Australian context** in a unit with a relevant case study

See you in the pull requests.
