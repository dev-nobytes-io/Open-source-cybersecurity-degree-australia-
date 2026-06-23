# Phase 4 — Practitioner Review

All 66 units are authored to **Draft**. Phase 4 is where practitioners take over:
verifying technical accuracy, workforce relevance, and framework mappings before
units advance toward **Published**. This hub is the entry point.

> **Why this exists:** the authoring AI deliberately flagged everything it could
> not independently verify — NICE/DCWF T-codes, ATT&CK v19 technique IDs, the
> provisional project-local KSAT IDs, the capability mapping, and AQF Level 7
> sufficiency. Phase 4 closes those out with real practitioners.

## The content lifecycle

```
Draft → Under Review → Practitioner Approved → Framework Verified → Published
```

| Stage | Who signs off |
|---|---|
| Under Review | PR open; Domain Expert + Practitioner Reviewer requested |
| Practitioner Approved | **Domain Expert** (technical accuracy) + **Practitioner Reviewer** (workforce relevance) |
| Framework Verified | **Framework Custodian** confirms every mapping is accurate and version-referenced |
| Published | Maintainer, once the above are complete |

Role definitions and transition rules: [`docs/governance.md`](../governance.md).

## Trackers

- **[Unit review dashboard](dashboard.md)** — live per-unit status and reviewer
  assignment across all 66 units (generated from unit metadata).
- **[Framework verification tracker](framework-verification.md)** — the
  Framework Custodian's per-major and repo-wide checklist (NICE/DCWF, ATT&CK v19,
  SFIA 9, ASD, KSAT IDs, capability mapping).

## How to review a unit (or a whole major)

1. Pick a unit from the [dashboard](dashboard.md) that is still **Draft** and
   unassigned. A Domain Expert may take an **entire major** (all six units).
2. Open a **Unit Review Request** issue — template in `.github/ISSUE_TEMPLATE/`
   (one per unit; for a major, open one per unit and reference a tracking issue).
3. Work through [`templates/review-checklist.md`](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/blob/main/templates/review-checklist.md)
   — Domain Expert (Technical Accuracy), Practitioner Reviewer (Practitioner
   Relevance), Framework Custodian (Framework Compliance).
4. Found a wrong/outdated mapping? File a **Framework Mapping Error** issue
   (template in `.github/ISSUE_TEMPLATE/`); see content-standards §4.
5. On sign-off, a maintainer updates the unit's `Status`, `Domain Expert`,
   `Practitioner Reviewer`, and `Last Reviewed` metadata, then regenerates the
   dashboards.

## Program-level audits (repo-wide, not per unit)

These cut across the whole curriculum and are tracked in the root
[`TODO.md`](../../TODO.md) Phase 4 section:

- [ ] **MITRE ATT&CK v19 mapping audit** — re-verify every tactic/technique
      reference against v19's structural changes. IDs are provisional until audited.
- [ ] **NICE/DCWF T-code verification** — confirm every T-code exists in the
      current DCWF and traces to a lab/activity/assessment (the linter enforces
      traceability structurally; a custodian confirms correctness).
- [ ] **KSAT identifier mapping** — map the project-local provisional KSAT IDs
      (`<UNIT>-K01`, …) to official NICE identifiers; see
      [`../ksat-coverage.md`](../ksat-coverage.md).
- [ ] **Capability mapping review** — confirm the operational-capability tagging
      used by the [Program Builder](../program-builder/index.md) and
      [Team Builder](../program-builder/team.md).
- [ ] **AQF Level 7 gap analysis** — independent check that the program meets the
      AQF Level 7 / TEQSA HESF criteria end to end.
- [ ] **Confirm flagged citations** — the exact SANS PIR-guide reference (OC05)
      and the "DF-C2M2" name in [`../maturity-models.md`](../maturity-models.md).

The Framework Custodian items above are tracked in detail, per major, in the
[framework verification tracker](framework-verification.md).
