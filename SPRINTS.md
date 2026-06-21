# Sprint Plan — Open Source Cybersecurity Degree (Australia)

This plan converts the scattered `TODO.md` backlog across the repository into
time-boxed, deliverable-focused sprints. It is derived from the root `TODO.md`
phase status and the per-directory TODO files in `core/`, `degrees/`, `docs/`,
and `templates/`.

> **Convention:** Each sprint has a goal, a definition of done, and a checklist.
> Units are authored against `templates/unit-template.md` and must satisfy the
> 10-point completion bar in the root `TODO.md` and `docs/content-standards.md`.

---

## Sprint 1 — Foundation Year Content (Phase 2 Priority)

**Goal:** Author all six Foundation Year units (F01–F06) to template-complete
Draft status so the shared first year of both degrees has real content.

**Source TODOs:** root `TODO.md` §1, `core/units/TODO.md`.

**Deliverables**
- [x] `core/units/F01-networking-fundamentals.md`
- [x] `core/units/F02-operating-systems.md`
- [x] `core/units/F03-scripting-automation.md`
- [x] `core/units/F04-security-concepts.md`
- [x] `core/units/F05-legal-ethics-compliance.md`
- [x] `core/units/F06-data-log-analysis.md`
- [x] `core/units/README.md` status table updated `Planned → Draft`

**Status:** ✅ Complete — all six Foundation units authored to Draft (2026-06-21).

**Definition of done:** Each unit has ≥6 substantive topics, ≥2 complete labs
(free/OSS tools only), formative + summative assessment with a 4-level rubric,
≥2 framework mappings (incl. ASD CSF), an Australian context section, and ≥5
annotated references with ≥1 Australian source.

---

## Sprint 2 — Operational Core Content

**Goal:** Author the six Operational Core units (OC01–OC06) — the operational
half of Year 2.

**Source TODOs:** root `TODO.md` §2, `core/units/TODO.md`.

**Deliverables**
- [x] `core/units/OC01-adversary-tradecraft.md`
- [x] `core/units/OC02-security-monitoring-siem.md`
- [x] `core/units/OC03-malware-analysis.md`
- [x] `core/units/OC04-incident-response-lifecycle.md`
- [x] `core/units/OC05-threat-intelligence-fundamentals.md` *(Priority Intelligence Requirements — Red Hat PIR process per SANS CTI material)*
- [x] `core/units/OC06-offensive-security-concepts.md`
- [x] `core/units/README.md` status table updated

**Definition of done:** As Sprint 1, but Bloom's levels 3–4 (Apply/Analyse) and
framework coverage incl. NICE DCWF Protect & Defend / Investigate + SFIA 9.

**Status:** ✅ Complete — all six Operational Core units authored to Draft
(2026-06-21). Threat-informed defense (MITRE ATT&CK + CTID) is the connective
thread across all six units per practitioner direction.

---

## Sprint 3 — Strategic Core Content

**Goal:** Author the six Strategic Core units (SC01–SC06) — the strategic half
of Year 2.

**Source TODOs:** root `TODO.md` §3, `core/units/TODO.md`.

**Deliverables**
- [x] `core/units/SC01-risk-management-frameworks.md`
- [x] `core/units/SC02-security-architecture.md`
- [x] `core/units/SC03-governance-policy-compliance.md`
- [x] `core/units/SC04-vendor-supply-chain-risk.md`
- [x] `core/units/SC05-security-program-management.md`
- [x] `core/units/SC06-stakeholder-communication.md`
- [x] `core/units/README.md` status table updated

**Status:** ✅ Complete — all six Strategic Core units authored to Draft
(2026-06-21). Frameworks per practitioner direction: NIST CSF 2.0 + ISO 27001
backbones, SABSA/Zero Trust/SP 800-160 for SC02, APRA CPS 234/CPS 230 + SOCI +
ISM/IRAP, and a **compliance-as-revenue** thread (IRAP→gov, SOC 2/APRA→finance,
ISO 27001 broad) woven through SC01, SC03, SC05, and SC06.

> **Milestone:** All 18 shared core units (Foundation + Operational + Strategic)
> are now authored to Draft. The shared curriculum spine of both degrees is
> complete. Remaining: Sprint 4 (infrastructure), Sprint 5 (docs), Sprint 6+
> (48 major units).

---

## Sprint 4 — Contribution Infrastructure

**Goal:** Make the project safe for multiple contributors so unit-authoring can
scale beyond the maintainers.

**Source TODOs:** root `TODO.md` "Contributing Infrastructure".

**Deliverables**
- [x] Issue templates: "New Unit Draft", "Unit Review Request", "Framework Mapping Error" (+ `config.yml`)
- [x] `STATUS.md` dashboard showing every unit's lifecycle status (linked from README)
- [x] Contributor onboarding checklist (`docs/contributor-onboarding.md`)
- [x] Unit-assignment register (`docs/unit-assignments.md`)
- [x] GitHub Actions CI to lint unit files against required template sections (`.github/scripts/lint_units.py` + `.github/workflows/lint-units.yml`)

**Status:** ✅ Complete (2026-06-21). The unit linter validates all 18 existing
units (required sections, ≥6 topics, ≥2 labs, 4-level rubric, ≥5 annotated refs
incl. an Australian source, ASD mapping, metadata fields, no leftover
placeholders) and runs on every PR touching unit files.

---

## Sprint 5 — Documentation Gaps

**Goal:** Close the documentation gaps that block accreditation work.

**Source TODOs:** root `TODO.md` "Documentation Gaps", `docs/*/TODO.md`.

**Deliverables**
- [x] Verify `docs/frameworks.md` tables against latest versions — currency table + review log; ATT&CK flagged as likely superseded
- [x] Expand `docs/accreditation.md` TEQSA pathway section — routes, HESF evidence mapping, provider-readiness checklist
- [x] Define disputed-content escalation process in `docs/governance.md` (§5.1)
- [x] Live unit status dashboard in root `README.md` (summary table → `STATUS.md`)

**Status:** ✅ Complete (2026-06-21).

---

## Sprint 6+ — Major Units (Phase 3)

**Goal:** Author the 8 majors × 6 units = 48 major-unit files.

**Source TODOs:** `degrees/**/TODO.md`.

Sequenced one major per sprint after the shared core is complete. Bloom's levels
4–5 (Analyse/Evaluate), capstones 5–6 (Evaluate/Create); major units may reference
paid tools provided a free alternative is documented.

### Sprint 6 — Threat Hunting major ✅ Complete (2026-06-21)

- [x] `TH01-hunting-methodology-process.md` (TaHiTI, hypothesis design, maturity)
- [x] `TH02-attack-for-hunters.md` (ATT&CK v19, Navigator, CTID prioritisation)
- [x] `TH03-host-based-hunting.md` (Velociraptor VQL, Volatility 3)
- [x] `TH04-network-based-hunting.md` (Zeek/Wireshark, beaconing, DNS exfil)
- [x] `TH05-hunt-operations-tooling.md` (Jupyter/Pandas, fleet VQL, Sigma)
- [x] `TH06-capstone-hunt-operation.md` (end-to-end capstone, Bloom's 5–6, 24 CP)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Free/OSS tooling throughout; threat-informed-defense spine continued; ATT&CK
**v19** used (technique IDs provisional pending the repo-wide v19 audit).

### Sprint 7 — DFIR major ✅ Complete (2026-06-21)

- [x] `DF01-dfir-process-legal-foundations.md` (PICERL/800-61, Evidence Act 1995)
- [x] `DF02-host-forensics.md` (Autopsy/Sleuth Kit, MFT/registry, Plaso timelines)
- [x] `DF03-memory-forensics.md` (Volatility 3, injection, credentials)
- [x] `DF04-network-forensics.md` (Wireshark/Zeek, C2, DNS exfil)
- [x] `DF05-incident-response-operations.md` (PICERL ops, NDB/APRA/SOCI, TheHive)
- [x] `DF06-capstone-ir-simulation.md` (end-to-end IR, Bloom's 5–6, 24 CP)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Strongest AU-legal major: Evidence Act 1995 admissibility throughout, full
NDB/APRA CPS 234/SOCI notification coverage, and Optus/Medibank/Latitude case
studies. Free/OSS tooling; ATT&CK v19 (technique IDs provisional pending audit).

### Remaining majors (Planned)

Operational: CTI, Detection Engineering, CTE. Strategic: Security Engineering,
Leadership & CISO, GRC. (6 majors × 6 = 36 units.)

---

## Resource Inputs from Practitioners

This project is practitioner-led. Where a maintainer has a preferred real-world
process or reference, it is captured here and woven into the relevant unit
rather than reinvented.

| Topic / Unit | Practitioner-supplied resource | Status |
|---|---|---|
| Threat-informed defense (all OC units) | MITRE ATT&CK + MITRE CTID body of work as the organising philosophy; defence as a living system that adapts to changing adversary behaviour | ✅ Incorporated across OC01–OC06 |
| Priority Intelligence Requirements (OC05) | Red Hat **Priority Intelligence Requirements** (PIR) process, as referenced in the SANS CTI body of knowledge (FOR578) | ✅ Incorporated in OC05 — exact SANS guide citation to confirm at review |
| Blameless post-incident review (OC04) | Covered within OC04's lessons-learned topic (per maintainer scope) | ✅ Incorporated in OC04 |
| Strategic Core control backbones (SC01, SC03) | NIST CSF 2.0 (Govern/Identify) + ISO 27001:2022 | ✅ Incorporated in SC01–SC06 |
| Security architecture (SC02) | SABSA + Zero Trust (NIST SP 800-207) + NIST SP 800-160 | ✅ Incorporated in SC01–SC06 |
| Australian regulatory regimes (SC03, SC04, SC05) | APRA CPS 234 + SOCI risk-management program + Australian Government ISM / IRAP | ✅ Incorporated in SC01–SC06 |
| Compliance-as-revenue framing (SC03, SC05) | Position compliance as a commercial/market-access enabler ("frameworks that make money"); map framework choice to industry — **IRAP** for government, **SOC 2** and **APRA CPS 234** for finance/other industries, ISO 27001 broadly | ✅ Incorporated in SC01–SC06 — distinctive angle to weave through governance/program units |

*(Add rows as resources are supplied.)*
