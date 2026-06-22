# TODO — degrees/strategic/grc/

**Major:** GRC (Governance, Risk & Compliance)
**Degree:** Bachelor of Cybersecurity Strategy
**Year:** 3
**Units:** GR01–GR06

All units are currently **Planned**. No unit files have been authored yet.

**Update (2026-06-21):** All six units (GR01–GR06) authored to **Draft** and pass the
unit linter. GRC-level maturity (OCEG GRC Capability Model, RIMS Risk Maturity Model)
added to `docs/maturity-models.md`. **This completes all 66 units of the degree.**
GR04 in particular must be reviewed by someone with direct AU regulatory knowledge
(APRA/OAIC/ASD), and ISO 27001:2022 / current Essential Eight content verified at
sign-off.

GRC has the richest Australian regulatory content of any major. It maps directly to real Australian compliance obligations (APRA CPS 234, Privacy Act 1988, SOCI Act 2018) and the frameworks employers use to evaluate GRC practitioners (ISO 27001, NIST CSF 2.0, Essential Eight).

---

## Files to Create

| File | Unit | Description |
|---|---|---|
| `GR01-security-governance-design.md` | GR01 | Policy hierarchy, roles and accountability, governance structures |
| `GR02-risk-management-in-practice.md` | GR02 | Risk registers, bow-tie analysis, treatment options, risk appetite |
| `GR03-compliance-frameworks.md` | GR03 | ISO 27001, NIST CSF 2.0, ASD Essential Eight — implementation and assessment |
| `GR04-australian-regulatory-environment.md` | GR04 | APRA CPS 234, Privacy Act 1988, SOCI Act 2018, NDB scheme |
| `GR05-audit-assurance.md` | GR05 | Control testing, internal audit methodology, IRAP assessment process |
| `GR06-capstone-grc-program-design.md` | GR06 | Design a GRC program for a defined Australian organisation (capstone) |

---

## Bloom's Taxonomy Requirements

Units GR01–GR05: **Levels 4–5** (analyse, evaluate, design, apply)
Capstone GR06: **Levels 5–6** (create, design, evaluate, recommend)

Example verbs: design, construct, evaluate, assess, recommend, apply, map, audit, develop

---

## Framework Mapping Requirements

| Framework | Required |
|---|---|
| NIST CSF 2.0 GV.* (Govern function) | Yes — GR01, GR02, GR03 |
| NIST CSF 2.0 ID.* (Identify function) | Yes — GR02 risk management |
| ISO 27001:2022 | Yes — GR03 implementation |
| ISO 27005:2022 | Yes — GR02 risk management |
| APRA CPS 234 | Yes — GR04 |
| ASD Essential Eight | Yes — GR03 |
| NIST SP 800-37 (RMF) | Yes — GR02, GR05 |
| SFIA 9 (IRMG) | Yes — at least 2 units |
| NIST NICE DCWF | Yes — T-codes traceable to activities |
| CIISec | Recommended |

---

## Activity Requirements

At least 8 practical activities total. GRC activities are less tool-intensive and more document/analysis-driven.

### Required Activities Across the Major

| Unit | Activity Ideas |
|---|---|
| GR01 | Activity: Design a security policy hierarchy for a fictional mid-size Australian organisation (policies, standards, procedures, guidelines) |
| GR01 | Activity: Create a RACI matrix for cybersecurity governance roles in a fictional financial services organisation |
| GR02 | Activity: Build a risk register with 10 entries using a bow-tie analysis for the top 3 risks |
| GR02 | Activity: Define a risk appetite statement for a fictional organisation and use it to prioritise 5 treatment decisions |
| GR03 | Activity: Map an organisation's existing controls against ISO 27001:2022 Annex A; identify gaps |
| GR03 | Activity: Conduct an Essential Eight assessment using the official ASD assessment guide (against a fictional environment description) |
| GR04 | Activity: Determine whether a fictional data breach triggers NDB notification obligations; draft the OAIC notification |
| GR04 | Activity: Map a fictional financial institution's security controls against APRA CPS 234 requirements |
| GR05 | Activity: Design an internal audit plan for ISO 27001 for a fictional organisation |
| GR05 | Activity: Complete a simulated IRAP-style assessment on a fictional government system description |
| GR06 | Capstone: Design a full GRC program for a fictional Australian organisation |

**Tools for this major:**
- Excel / Google Sheets (risk registers, gap analysis — accessible to all learners)
- NIST CSF 2.0 Reference Tool (free, NIST website)
- ASD Essential Eight Assessment Guides (free, ASD website)
- ISO 27001 Annex A checklist templates (various free versions available)
- draw.io (policy hierarchy and governance diagrams)

---

## Australian Context (Core to This Major)

GR04 is entirely Australian-context focused, but Australian regulatory content must appear throughout:

- [ ] **GR01** — APRA CPS 234 board and governance obligations; ASIC cybersecurity expectations for financial services
- [ ] **GR02** — APRA Prudential Practice Guide CPG 234; ISO 27005 risk management applied to Australian financial sector
- [ ] **GR03** — ASD Essential Eight Maturity Model (Australian government mandated); ISM (Information Security Manual)
- [ ] **GR04** — Deep dive: Privacy Act 1988 and the NDB scheme; SOCI Act 2018 and critical infrastructure obligations; APRA CPS 234; OAIC enforcement examples
- [ ] **GR05** — IRAP (Information Security Registered Assessors Program) — Australian government cloud assessment; ASAE 3402 (AU auditing standard)
- [ ] **GR06** — Capstone scenario must be an Australian organisation with defined regulatory obligations

---

## Capstone Unit (GR06) Requirements

The capstone must produce a **complete GRC program design**:

- [ ] Fictional (or anonymised) Australian organisation with defined sector and regulatory obligations
- [ ] Governance structure designed (roles, policies, committee charters)
- [ ] Risk management framework selected and implemented (with rationale)
- [ ] Risk register produced (minimum 10 risks with bow-tie for top 3)
- [ ] Compliance framework selected (ISO 27001 or NIST CSF 2.0 + Essential Eight) with gap analysis
- [ ] Regulatory obligations mapped (at minimum: Privacy Act, one sector-specific obligation)
- [ ] Audit plan developed for first compliance cycle
- [ ] Risk treatment plan with priorities and owners
- [ ] Community practitioner review of the capstone
- [ ] Deliverable suitable for professional portfolio (reference `templates/student-portfolio/index.html`)

---

## Certification Bridge Alignment

This major maps directly to several industry certifications. Unit content should align with exam domains:

| Certification | Primary Unit Alignment |
|---|---|
| CISM (ISACA) | GR01 (domain 1 & 2), GR02 (domain 2), GR03 (domain 3) |
| ISO 27001 Lead Implementer | GR01, GR03, GR06 |
| ISO 27001 Lead Auditor | GR05, GR06 |
| CRISC (ISACA) | GR02, GR05 |
| IRAP Assessor pathway | GR05 |

Unit content does not need to teach to the exam — but it should ensure learners who complete the major have the foundational knowledge to pursue these certifications with reasonable supplemental study.

---

## Sign-off Requirements

Before any unit can be merged:

- [ ] Domain Expert with active GRC / risk / compliance experience named in metadata
- [ ] Practitioner Reviewer (different from Domain Expert) named in metadata
- [ ] GR04 reviewed by someone with direct knowledge of AU regulatory environment (APRA, OAIC, ASD)
- [ ] ISO 27001:2022 content verified against the 2022 version (not the 2013 edition)
- [ ] Essential Eight content verified against current ASD maturity model version

See `templates/review-checklist.md` for the full pre-merge checklist.
