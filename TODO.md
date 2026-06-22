# TODO — Root

This is the top-level tracking file for the Open Source Cybersecurity Degree Australia project. The project is currently completing Phase 1 (Foundation) and moving into Phase 2 (Content).

---

## Project Phase Status

- [x] Phase 1 — Repository governance established
- [x] Phase 1 — Degree architecture documented in `docs/structure.md`
- [x] Phase 1 — Framework mapping tables created in `docs/frameworks.md`
- [x] Phase 2 — Foundation year units authored (F01–F06) _(Draft — pending practitioner review)_
- [x] Phase 2 — Operational core units authored (OC01–OC06) _(Draft — pending practitioner review)_
- [x] Phase 2 — Strategic core units authored (SC01–SC06) _(Draft — pending practitioner review)_
- [ ] Phase 3 — All major unit content written (8 majors × 6 units = 48 unit files) _(in progress: Threat Hunting + DFIR + CTI drafted (18 units); 5 majors remaining)_
- [ ] Phase 4 — Practitioner review of each major completed
- [ ] Phase 4 — Framework mappings independently verified
- [ ] Phase 4 — AQF Level 7 gap analysis completed
- [ ] Phase 5 — TEQSA formal alignment pathway explored
- [ ] Phase 5 — Industry body endorsement sought
- [ ] Phase 5 — Employer recognition programme established

---

## Immediate Actions (Phase 2 Priority)

### 1. Author Foundation Year Units
All 6 foundation units must be authored using `templates/unit-template.md`. Each file belongs in `core/units/`.

| Unit | File to Create | Priority |
|---|---|---|
| F01 — Networking Fundamentals | `core/units/F01-networking-fundamentals.md` | High |
| F02 — Operating Systems & Administration | `core/units/F02-operating-systems.md` | High |
| F03 — Scripting & Automation | `core/units/F03-scripting-automation.md` | High |
| F04 — Security Concepts & Principles | `core/units/F04-security-concepts.md` | High |
| F05 — Legal, Ethics & Australian Compliance | `core/units/F05-legal-ethics-compliance.md` | High |
| F06 — Data & Log Analysis | `core/units/F06-data-log-analysis.md` | High |

### 2. Author Operational Core Units
| Unit | File to Create |
|---|---|
| OC01 — Adversary Tradecraft & TTPs | `core/units/OC01-adversary-tradecraft.md` |
| OC02 — Security Monitoring & SIEM | `core/units/OC02-security-monitoring-siem.md` |
| OC03 — Malware Analysis Fundamentals | `core/units/OC03-malware-analysis.md` |
| OC04 — Incident Response Lifecycle | `core/units/OC04-incident-response-lifecycle.md` |
| OC05 — Threat Intelligence Fundamentals | `core/units/OC05-threat-intelligence-fundamentals.md` |
| OC06 — Offensive Security Concepts | `core/units/OC06-offensive-security-concepts.md` |

### 3. Author Strategic Core Units
| Unit | File to Create |
|---|---|
| SC01 — Risk Management Frameworks | `core/units/SC01-risk-management-frameworks.md` |
| SC02 — Security Architecture Principles | `core/units/SC02-security-architecture.md` |
| SC03 — Governance, Policy & Compliance | `core/units/SC03-governance-policy-compliance.md` |
| SC04 — Vendor & Supply Chain Risk | `core/units/SC04-vendor-supply-chain-risk.md` |
| SC05 — Security Program Management | `core/units/SC05-security-program-management.md` |
| SC06 — Stakeholder Communication | `core/units/SC06-stakeholder-communication.md` |

---

## Contributing Infrastructure

- [x] Set up issue templates for practitioner review volunteers (`.github/ISSUE_TEMPLATE/`)
- [x] Create a contributor onboarding checklist (beyond `CONTRIBUTING.md`) — `docs/contributor-onboarding.md`
- [x] Establish a unit assignment system so contributors don't duplicate work — `docs/unit-assignments.md`
- [x] Add a status dashboard (`STATUS.md`) showing which units are Draft / In Review / Published
- [x] Define a CI/CD check (GitHub Actions) to lint unit files against `templates/unit-template.md` required sections
- [x] Add issue templates: "New Unit Draft", "Unit Review Request", "Framework Mapping Error"

---

## Documentation Gaps

- [x] `docs/frameworks.md` — verified framework versions against a currency table + review log; flagged MITRE ATT&CK as likely superseded and DCWF/NICE codes for live re-verification
- [x] `docs/accreditation.md` — expanded TEQSA pathway (routes, HESF evidence mapping, provider-readiness checklist, dependencies)
- [x] `docs/governance.md` — defined disputed-content & framework-mapping escalation process (§5.1)
- [x] Root `README.md` — added a live curriculum status summary linking to `STATUS.md`
- [ ] **MITRE ATT&CK v19 mapping audit (repo-wide)** — version pointers updated to v19; now re-verify every ATT&CK tactic/technique reference and mapping across all units against v19's significant structural changes. Track via a "Framework Mapping Error" issue per affected unit. Existing technique IDs are provisional until audited.

---

## How Each Unit Must Be Completed

Every unit file must satisfy ALL of the following before it can be merged:

1. Uses `templates/unit-template.md` exactly — no sections removed
2. Learning outcomes use correct Bloom's taxonomy verbs for the layer (see `docs/content-standards.md`)
3. Minimum 2 framework mappings with at least 1 Australian framework (ASD CSF preferred)
4. Minimum 6 substantive topics with actual educational content (no placeholder headings)
5. Minimum 2 complete labs with objectives, environment, steps, expected output, and reflection questions
6. At least 1 formative + 1 summative assessment with a 4-level rubric
7. Australian context section references at least one AU legislation, regulator, or case study
8. Minimum 5 annotated references, at least 1 Australian source
9. Unit metadata table fully completed
10. Signed off by Domain Expert + Practitioner Reviewer (names in metadata)

See `templates/review-checklist.md` for the full pre-merge sign-off checklist.
