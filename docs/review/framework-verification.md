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
>
> The official-looking **`T####` codes and their task statements are equally
> provisional** and are *not* covered by the project-local caveat above: they are
> external DCWF identifiers, and none has been verified against a DCWF primary
> source. See the T-code statement divergence audit below.

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
- [ ] **T-code statement reconciliation** — 29 codes carry divergent, unverified
      task statements across 252 of 262 mapping rows. See the audit below.
- [ ] **Operational-capability mapping** — the unit→capability tags behind the
      [Program Builder](../program-builder/index.md) reviewed and confirmed.
- [ ] **Maturity-model cross-walk** — confirm the "DF-C2M2" reference and the
      model→capability→CSF→role→KSAT chain in [`../maturity-models.md`](../maturity-models.md).

## T-code statement divergence audit (2026-09-21)

A repo-wide audit of the `### NIST NICE DCWF` and `### NICE/DCWF KSATs`
mapping tables found that **the same NICE/DCWF T-code carries different task
statements in different units**. The statements were written per-unit to
describe that unit's activity, rather than transcribed from the DCWF. A T-code
is an external identifier with one official meaning, so units currently
disagree with each other about what a given code denotes.

**Scope:** 29 of 34 distinct T-codes, affecting 252 of 262
mapping rows (96%). This is an **R1** (framework mapping is mandatory) integrity
issue, not a cosmetic one: `docs/ksat-coverage.md` is generated from these tables
and republishes the contradictory statements side by side as curriculum coverage.

**No statement in this repository has been verified against a DCWF primary
source.** Until the Framework Custodian does so, every T-code task statement
is provisional — including those that happen to be correct.

> **Deliberately not auto-corrected.** Rewording these to a single statement
> would replace one set of unverified text with another. The codes and statements
> are left in place and marked provisional so the custodian can verify each
> against the DCWF, rather than inheriting a plausible-looking guess.

### Divergence by code

| T-code | Distinct statements | Rows | Units affected |
|---|---|---|---|
| `T0259` | 16 | 32 | CE02, CE03, CE04, CE05, CE06, DE01, DE02, DE03, DE04, DE05, DE06, F06, OC02, TH03, TH05, TH06 |
| `T0177` | 8 | 16 | F04, GR02, GR03, GR05, GR06, SC01, SC03, SC04 |
| `T0294` | 8 | 14 | DE03, DE04, DE06, DF04, F01, OC03, TH04 |
| `T0050` | 7 | 14 | SC02, SE01, SE02, SE03, SE04, SE05, SE06 |
| `T0432` | 7 | 14 | DF01, DF02, DF03, DF04, DF06, OC03, TH03 |
| `T0569` | 7 | 14 | CT01, DE01, OC01, OC05, TH01, TH02, TH06 |
| `T0166` | 6 | 10 | DE02, F06, OC02, SE04, TH05 |
| `T0149` | 5 | 12 | F04, GR02, LD02, LD06, SC01, SC05 |
| `T0151` | 5 | 6 | LD03, LD05 |
| `T0591` | 5 | 10 | CE02, CE03, CE04, CE06, OC06 |
| `T0707` | 5 | 10 | CT01, CT02, OC01, OC05, TH01 |
| `T0751` | 5 | 10 | CT02, CT03, CT04, CT05, CT06 |
| `T0041` | 4 | 8 | DF05, DF06, OC04, SC06 |
| `T0226` | 4 | 8 | GR01, GR03, SC03, SC04 |
| `T0431` | 4 | 6 | F02, F03, SE03 |
| `T0445` | 4 | 8 | CE05, LD02, SC05, SC06 |
| `T0098` | 3 | 6 | CE01, F05, GR04 |
| `T0147` | 3 | 6 | GR01, GR06, LD01 |
| `T0473` | 3 | 6 | SC02, SE02, SE06 |
| `T0708` | 3 | 6 | CT03, CT05, TH02 |
| `T0001` | 2 | 4 | LD01, LD06 |
| `T0023` | 2 | 4 | F01, TH04 |
| `T0028` | 2 | 4 | CE01, OC06 |
| `T0103` | 2 | 4 | DF01, DF05 |
| `T0111` | 2 | 4 | SE01, SE05 |
| `T0163` | 2 | 4 | DE05, F02 |
| `T0396` | 2 | 4 | DF02, DF03 |
| `T0710` | 2 | 4 | CT04, CT06 |
| `T0863` | 2 | 4 | F05, GR04 |

### Worked example — `T0259`

The worst case: 16 different statements across 32 rows.

- `core/units/F06-data-log-analysis.md:81` — “Identify and analyse anomalous activity in log and event data”
- `core/units/OC02-security-monitoring-siem.md:77` — “Identify and analyse anomalous network/host activity and tune detections”
- `degrees/operational/cte/CE02-red-team-operations.md:74` — “Analyse the detectable artefacts of adversary operations”
- `degrees/operational/cte/CE03-attack-based-emulation.md:74` — “Analyse detection outcomes from emulated adversary behaviour”
- `degrees/operational/cte/CE04-purple-team-operations.md:70` — “Validate and improve detections through collaborative testing”
- `degrees/operational/cte/CE05-reporting-debrief.md:71` — “Translate findings into prioritised detection improvements”
- `degrees/operational/cte/CE06-capstone-emulation-exercise.md:76` — “Evaluate detection and deliver improvement from emulation”
- `degrees/operational/detection-engineering/DE01-detection-theory-philosophy.md:73` — “Evaluate detection logic for quality and coverage”
- `degrees/operational/detection-engineering/DE02-data-sources-log-engineering.md:70` — “Audit log sources and identify coverage gaps for detection”
- `degrees/operational/detection-engineering/DE03-writing-detection-logic.md:66` — “Develop and test detection logic for adversary techniques”
- `degrees/operational/detection-engineering/DE04-adversary-simulation-detection.md:70` — “Validate detections by simulating adversary behaviour”
- `degrees/operational/detection-engineering/DE05-detection-operations-management.md:71` — “Tune detections and manage alert quality”
- `degrees/operational/detection-engineering/DE06-capstone-detection-library.md:74` — “Build and test a detection library for a threat scenario”
- `degrees/operational/threat-hunting/TH03-host-based-hunting.md:74` — “Analyse host/endpoint data to identify anomalous and malicious activity”
- `degrees/operational/threat-hunting/TH05-hunt-operations-tooling.md:75` — “Execute fleet-scale hunts and identify anomalous activity”
- `degrees/operational/threat-hunting/TH06-capstone-hunt-operation.md:79` — “Execute host/network hunts and report findings with detections”

### Custodian actions

- [ ] Obtain the DCWF source of record (work-role career-pathway material) and
      record the artifact name, version and retrieval date here.
- [ ] For each of the 29 codes, transcribe the official statement and reconcile
      every row against it.
- [ ] Withdraw any code whose official statement does not cover the unit's
      activity, rather than re-wording the activity to fit the code.
- [ ] Re-run `.github/scripts/ksat_coverage.py` once reconciled.

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
