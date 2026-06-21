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
- [ ] `core/units/SC01-risk-management-frameworks.md`
- [ ] `core/units/SC02-security-architecture.md`
- [ ] `core/units/SC03-governance-policy-compliance.md`
- [ ] `core/units/SC04-vendor-supply-chain-risk.md`
- [ ] `core/units/SC05-security-program-management.md`
- [ ] `core/units/SC06-stakeholder-communication.md`
- [ ] `core/units/README.md` status table updated

---

## Sprint 4 — Contribution Infrastructure

**Goal:** Make the project safe for multiple contributors so unit-authoring can
scale beyond the maintainers.

**Source TODOs:** root `TODO.md` "Contributing Infrastructure".

**Deliverables**
- [ ] Issue templates: "New Unit Draft", "Unit Review Request", "Framework Mapping Error"
- [ ] `STATUS.md` (or README dashboard) showing every unit's lifecycle status
- [ ] Contributor onboarding checklist
- [ ] Unit-assignment system (so contributors don't duplicate work)
- [ ] GitHub Actions CI to lint unit files against required template sections

---

## Sprint 5 — Documentation Gaps

**Goal:** Close the documentation gaps that block accreditation work.

**Source TODOs:** root `TODO.md` "Documentation Gaps", `docs/*/TODO.md`.

**Deliverables**
- [ ] Verify `docs/frameworks.md` tables against latest versions (SFIA 9, NICE DCWF 2023, ASD CSF 2024)
- [ ] Expand `docs/accreditation.md` TEQSA pathway section
- [ ] Define disputed-content escalation process in `docs/governance.md`
- [ ] Live unit status dashboard in root `README.md`

---

## Sprint 6+ — Major Units (Phase 3)

**Goal:** Author the 8 majors × 6 units = 48 major-unit files.

**Source TODOs:** `degrees/**/TODO.md`.

Sequenced one major per sprint after the shared core is complete. Bloom's levels
4–5 (Analyse/Evaluate); major units may reference paid tools provided a free
alternative is documented.

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

*(Add rows as resources are supplied.)*
