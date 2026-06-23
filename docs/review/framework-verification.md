# Framework Verification Tracker

The **Framework Custodian**'s checklist for advancing units to **Framework
Verified**. It complements the per-unit Framework Compliance section in
[`templates/review-checklist.md`](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/blob/main/templates/review-checklist.md): this page
tracks coverage across the whole curriculum so nothing is missed.

Report any problem found with a **Framework Mapping Error** issue (template in
`.github/ISSUE_TEMPLATE/`). Mapping standards — including the Employer Visibility
rule (every T-code traces to evidence) — are in
[`docs/content-standards.md`](../content-standards.md) §4.

> KSAT identifiers and the operational-capability mapping are **project-local and
> provisional**. Verifying and mapping them to official NICE identifiers is itself
> a Phase 4 task (see below).

## Per-unit checks (every unit)

For each unit the custodian confirms:

- [ ] **NICE/DCWF work roles** — each role code is current and correctly named.
- [ ] **NICE/DCWF T-codes** — each exists in the current DCWF and **traces to a
      specific lab/activity/assessment** (no orphan T-codes).
- [ ] **NICE/DCWF KSATs** — Knowledge/Skill/Ability/Task rows are accurate; the
      provisional `<UNIT>-K/S/A` IDs are mapped to official identifiers where one
      exists, and Task rows reconcile with the work-role T-codes.
- [ ] **SFIA 9** — skill code and level are appropriate for the unit's layer.
- [ ] **ASD framework** — at least one Australian framework mapping, current year.
- [ ] **Version strings** — NICE DCWF 2023, SFIA 9, ASD CSF 2024, MITRE ATT&CK
      **v19** stated and consistent (the linter warns on drift).

## Repo-wide audits

- [ ] **MITRE ATT&CK v19 audit** — every tactic/technique reference re-verified
      against v19's structural changes (root `TODO.md`). IDs provisional until done.
- [ ] **KSAT → official NICE identifier mapping** — across all 66 units
      ([`../ksat-coverage.md`](../ksat-coverage.md)).
- [ ] **Operational-capability mapping** — the unit→capability tags behind the
      [Program Builder](../program-builder/index.md) reviewed and confirmed.
- [ ] **Maturity-model cross-walk** — confirm the "DF-C2M2" reference and the
      model→capability→CSF→role→KSAT chain in [`../maturity-models.md`](../maturity-models.md).

## Per-major progress

Sign off a major once all six of its units are Framework Verified.

| Major / Section | Units | NICE roles/T-codes | ATT&CK v19 | SFIA 9 | ASD | KSAT IDs | Status |
|---|---|---|---|---|---|---|---|
| Foundation | F01–F06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Operational Core | OC01–OC06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Strategic Core | SC01–SC06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Threat Hunting | TH01–TH06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| DFIR | DF01–DF06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Cyber Threat Intelligence | CT01–CT06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Detection Engineering | DE01–DE06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Cyber Threat Emulation | CE01–CE06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Security Engineering | SE01–SE06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Leadership & CISO | LD01–LD06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |
| Governance, Risk & Compliance | GR01–GR06 | ☐ | ☐ | ☐ | ☐ | ☐ | Not started |

Per-unit status is on the [review dashboard](dashboard.md).
