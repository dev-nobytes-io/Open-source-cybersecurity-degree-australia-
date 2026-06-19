# TODO — degrees/strategic/

This directory contains the 3 majors for the **Bachelor of Cybersecurity Strategy** (AQF Level 7):

| Major | Directory | Units |
|---|---|---|
| Security Engineering | `security-engineering/` | SE01–SE06 |
| Leadership & CISO | `leadership/` | LD01–LD06 |
| GRC (Governance, Risk & Compliance) | `grc/` | GR01–GR06 |

---

## Prerequisites

All strategic majors require:
- Foundation Year (F01–F06) — completed before starting any major
- Strategic Core (SC01–SC06) — completed before starting any major

**Cross-pathway note (from `docs/structure.md`):** Security Engineering benefits from Operational Core (OC01–OC06) exposure. Learners pursuing the Strategic degree are encouraged to complete at least two Operational Core units as electives.

---

## Status

All 18 unit files across 3 majors are currently **Planned**.

---

## Shared Strategic Considerations

### Australian Regulatory Context (Essential Throughout)

Strategic majors have the strongest regulatory obligations. Every major must embed AU context:

| Major | Primary Australian Frameworks |
|---|---|
| Security Engineering | ASD Essential Eight, NIST SP 800-160 (applied in AU context), IRAP |
| Leadership & CISO | APRA CPS 234 (board reporting), Privacy Act 1988, SOCI Act 2018 |
| GRC | APRA CPS 234, Privacy Act 1988, SOCI Act 2018, ISO 27001, Essential Eight |

### Audience

Strategic degree content should be written for learners who will communicate with boards, executives, regulators, and auditors — not just technical practitioners. Writing style and scenario design should reflect this:

- Case studies should include board-level decision scenarios
- Assessments should include executive communication tasks (reports, briefings, presentations)
- Technical concepts should be explained with business impact framing

---

## Authoring Order (Recommended)

1. **GRC** — Most structured content (ISO 27001, NIST CSF 2.0, APRA CPS 234); clear Australian regulatory obligations
2. **Security Engineering** — High demand role; SABSA, Zero Trust, cloud security well-documented
3. **Leadership & CISO** — Most practitioner-dependent content; needs experienced CISO/Director contributors

---

## What Each Major Directory Needs

Each major directory currently has only a `README.md`. The following files need to be created:

```
degrees/strategic/<major>/
├── README.md              ← Exists — update when units are authored
├── TODO.md                ← This file (exists in each subdirectory)
└── <unit-code>-<title>.md ← 6 unit files per major — NOT YET CREATED
```

---

## Quality Checklist for Each Strategic Major

Before publishing any major:

- [ ] All 6 unit files authored using `templates/unit-template.md`
- [ ] Each unit has correct Bloom's taxonomy level (Levels 4–5 for major units: analyse, evaluate)
- [ ] Each unit references NIST CSF 2.0 where relevant (especially GV.*, ID.* functions)
- [ ] Each unit references at least one Australian regulation or regulatory body
- [ ] All assessments include at least one stakeholder communication or executive output
- [ ] Capstone deliverable documented and portfolio-ready
- [ ] Domain Expert + Practitioner Reviewer sign-off on all units
- [ ] README.md unit status table updated

---

## Capstone Coordination

All 3 strategic capstones (SE06, LD06, GR06) must:

- [ ] Be practical applied projects (not purely theoretical)
- [ ] Produce a documented output suitable for a professional portfolio
- [ ] Be reviewed by at least one practitioner volunteer from the community
- [ ] Reference `templates/student-portfolio/index.html` for portfolio structure

Consider whether any capstones can be combined into a cross-major strategic project (e.g., designing a security program covering GRC + Engineering + Leadership perspectives).
