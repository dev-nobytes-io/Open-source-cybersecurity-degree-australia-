# SE06: Capstone — Architecture Design

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (security architecture/engineering)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

The Security Engineering capstone integrates the whole major into a single secure
architecture design for a defined Australian organisation. Students elicit business
and security requirements, produce logical/physical/data-flow architectures, threat
model the design, apply Zero Trust and IAM, select and justify controls, map
Australian regulatory requirements, and produce a residual-risk register — a
portfolio-grade design document. It is assessed at the highest cognitive levels:
students **create**, **evaluate**, and **justify** a complete architecture.

The capstone is the apex of the Security Engineering thesis — security built in by
design, traceable from business need to control, and measured against engineering
maturity (SSE-CMM/BSIMM/OWASP SAMM, see `docs/maturity-models.md`). The scenario is an
Australian organisation in a regulated sector (e.g. financial institution), mapping
APRA CPS 234, the ASD Essential Eight/ISM, and the Privacy Act. SE06 requires
SE01–SE05 and the strategic core.

---

## Prerequisites

- SE01 — Secure System Design
- SE02 — Security Architecture
- SE03 — Identity & Access Management
- SE04 — Detection & Response Engineering
- SE05 — Security in Cloud & DevSecOps

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** a complete secure architecture from business and security
   requirements.
2. **Create** logical, physical, and data-flow architecture artefacts.
3. **Evaluate** the architecture via threat modelling and control selection.
4. **Design** Zero Trust and IAM into the architecture.
5. **Evaluate** the architecture against Australian regulatory requirements and
   residual risk.
6. **Justify** the design and its trade-offs to a technical and governance audience.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** The capstone consolidates specialised security-engineering
knowledge into an integrated architecture.

**Skills (AQF 7.2):** Students demonstrate the highest-order skills — creating,
evaluating, and justifying a complete architecture independently.

**Application (AQF 7.3):** Students apply security engineering with professional
accountability for an Australian regulated organisation.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Architect (652) | SP-ARC-002 | T0050 | Design and document a complete security architecture | Lab 1 — Architecture & Threat Model |
| NIST NICE DCWF | 2023 | Enterprise Architect | SP-ARC-001 | T0473 | Justify control selection and regulatory alignment | Lab 2 — Controls, Risk & Justification |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Solution architecture | ARCH | Level 5–6 | Lab 1, Lab 2 |
| Information security | SCTY | Level 5 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Security Architecture | Architecture Design | Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | SE06-K01 | Knowledge of scoping an architecture to requirements | Topic 1 |
| Knowledge | SE06-K02 | Knowledge of architecture artefacts | Topic 2 |
| Knowledge | SE06-K03 | Knowledge of threat modelling and control selection | Topic 3 |
| Knowledge | SE06-K04 | Knowledge of Zero Trust, IAM, regulatory mapping, and residual risk | Topic 4; Topic 5 |
| Skill | SE06-S01 | Skill in producing an architecture and threat model | Lab 1 |
| Skill | SE06-S02 | Skill in selecting controls and justifying residual risk | Lab 2 |
| Ability | SE06-A01 | Ability to design a complete, defensible security architecture | Lab 1; Lab 2 |
| Ability | SE06-A02 | Ability to justify control selection and regulatory alignment | Topic 6; Summative |
| Task | T0050 | Design and document a complete security architecture | Lab 1 |
| Task | T0473 | Justify control selection and regulatory alignment | Lab 2 |

---

## Topics

> The capstone is a supervised, integrative design project. These "topics" are the
> phases and guidance; the substantive work is the student's own architecture.

### Topic 1: Scope and Requirements

This phase defines the Australian regulated-sector organisation, elicits business and
security requirements, and sets success criteria, agreed with the supervisor.

**Key concepts:**
- Regulated-sector scenario and context
- Business and security requirements
- Success criteria

---

### Topic 2: Architecture Artefacts

Students produce the core artefacts: logical, physical, and data-flow architectures
(SE02), with trust zones and data classification.

**Key concepts:**
- Logical/physical/data-flow architectures
- Trust zones and data classification
- Traceability to requirements

---

### Topic 3: Threat Model and Control Selection

Students threat model the architecture (SE01) and select controls with rationale,
tracing each to a threat/requirement.

**Key concepts:**
- Architecture threat modelling
- Control selection with rationale
- Threat → control traceability

---

### Topic 4: Zero Trust and IAM

Students design Zero Trust access (SE02) and the IAM architecture (SE03) into the
design, including privileged access.

**Key concepts:**
- Zero Trust access design
- IAM/PAM architecture
- Identity as the control plane

---

### Topic 5: Regulatory Mapping and Residual Risk

Students map the architecture to Australian regulatory requirements (APRA CPS 234,
ASD Essential Eight/ISM, Privacy Act) and produce a residual-risk register.

**Key concepts:**
- Regulatory mapping (APRA/ASD/Privacy)
- Residual-risk register
- Risk acceptance and treatment

**Australian context:** APRA CPS 234, ASD Essential Eight/ISM, Privacy Act mapping.

---

### Topic 6: Justification and Maturity

Students justify the design and trade-offs to technical and governance audiences and
reflect on the engineering maturity (SSE-CMM/BSIMM/SAMM) the design embodies, plus
package a portfolio artefact.

**Key concepts:**
- Justifying design and trade-offs
- Engineering maturity reflection
- Portfolio artefact

---

## Labs & Exercises

### Lab 1: Architecture & Threat Model (capstone deliverable)

**Objective:** Produce the architecture artefacts and threat model for the scenario.

**Prerequisites:**
- Topics 1–4

**Environment:**
- No technical environment — a design deliverable using draw.io and the Microsoft
  Threat Modelling Tool. Any device within the 8 GB / 4-core / 50 GB spec.

**Instructions:**

1. Confirm the Australian regulated-sector scenario, requirements, and success
   criteria with your supervisor.
2. Produce logical, physical, and data-flow architectures with trust zones.
3. Threat model the architecture and identify key risks.
4. Design Zero Trust access and the IAM/PAM architecture.
5. Select controls, tracing each to a threat/requirement.
6. Ensure the artefacts are internally consistent and traceable.

**Expected Output:**

A consistent set of architecture artefacts (logical/physical/data-flow), a threat
model, Zero Trust + IAM design, and a traceable control set. Learners can defend the
architecture's coherence and traceability.

**Reflection Questions:**

1. Which requirement most shaped the architecture, and why?
2. Which threat drove the most control selection?
3. Where did Zero Trust/IAM most reduce risk?

---

### Lab 2: Controls, Risk & Justification (capstone deliverable)

**Objective:** Complete the control rationale, regulatory mapping, residual-risk
register, and design justification.

**Prerequisites:**
- Topics 5–6 and Lab 1

**Environment:**
- No technical environment — a design/analysis deliverable using
  `templates/student-portfolio/index.html`. Any device.

**Instructions:**

1. Document the control selection with rationale (threat/requirement-traced).
2. Map the architecture to APRA CPS 234, ASD Essential Eight/ISM, and the Privacy
   Act.
3. Produce a residual-risk register with treatment/acceptance.
4. Write the design justification for technical and governance audiences.
5. Reflect on the engineering maturity (SSE-CMM/BSIMM/SAMM) the design embodies.
6. Package the capstone as a portfolio artefact and submit for community
   practitioner review.

**Expected Output:**

A complete secure architecture design document with control rationale, regulatory
mapping, residual-risk register, justification, and a portfolio artefact suitable for
employer review.

**Reflection Questions:**

1. Which residual risk is hardest to accept, and how did you justify it?
2. How did regulatory requirements constrain the design?
3. What does the design reveal about your engineering maturity?

---

## Assessment

### Formative Assessment: Design Review Gate

**Type:** Supervisor/peer review of the architecture and threat model

**Description:** Before completing the design, the architecture artefacts and threat
model are reviewed for coherence and traceability; students revise. A go/no-go gate
into the final design.

**Learning Outcomes Assessed:** LO1, LO2, LO3

**Feedback mechanism:** Structured feedback against a design rubric; revision
required before Lab 2.

---

### Summative Assessment: Secure Architecture Design Document

**Type:** Architecture design document with portfolio artefact

**Description:** The complete deliverable: business/security requirements; logical,
physical, and data-flow architectures; threat model; Zero Trust + IAM design;
control selection with rationale; APRA/ASD/Privacy mapping; residual-risk register;
and a design justification — packaged as a portfolio artefact and reviewed by a
community practitioner. Deliverable: design document (~4,000–5,000 words) with
diagrams.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Requirements & artefacts | LO1, LO2 |
| Threat model & controls | LO3 |
| Zero Trust & IAM | LO4 |
| Regulatory mapping & risk | LO5 |
| Justification | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Architecture quality | Coherent, traceable, complete | Sound | Partial | Weak |
| Threat model & controls | Rigorous; controls justified | Adequate | Gaps | Poor |
| Zero Trust & IAM | Sophisticated, correct | Reasonable | Uneven | Poor |
| Regulatory & risk | Precise mapping; honest residual risk | Mostly | Superficial | Absent |
| Justification | Compelling for both audiences | Clear | Mixed | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Regulated-sector scenario:** An Australian organisation (e.g. financial
  institution).
- **APRA CPS 234, ASD Essential Eight/ISM, Privacy Act:** Mapped in the design.
- **IRAP considerations:** Where government data is in scope.

---

## Further Reading

**SABSA Institute (2024).** *SABSA — Enterprise Security Architecture.* https://sabsa.org
> Relevance: The architecture method underpinning the capstone design.

**NIST (2018, 2020).** *SP 800-160 & SP 800-207 (Zero Trust).* NIST. https://csrc.nist.gov
> Relevance: The systems-security-engineering and Zero Trust basis for the design.

**Australian Cyber Security Centre (2024).** *ISM, Essential Eight & IRAP.* ACSC. https://www.cyber.gov.au/ism
> Relevance: The Australian control baseline and assessment context for the capstone (Australian source).

**APRA (2019).** *Prudential Standard CPS 234.* APRA. https://www.apra.gov.au
> Relevance: The regulatory obligations the design must map (Australian source).

**Templates — Student Portfolio.** `templates/student-portfolio/index.html` (this repository).
> Relevance: The portfolio artefact format the capstone deliverable must populate (Australian-context degree resource).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SE06 |
| Unit Title | Capstone — Architecture Design |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 24 CP |
| Degree Layer | Capstone |
| Major / Pathway | Security Engineering |
| Prerequisites | SE01, SE02, SE03, SE04, SE05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 5–6 (Evaluate, Create) |
| Australian Legislation Referenced | APRA CPS 234; Privacy Act 1988; ASD Essential Eight/ISM |
