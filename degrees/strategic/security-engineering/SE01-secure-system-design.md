# SE01: Secure System Design

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (security architecture/engineering)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches building security into systems from the start rather than bolting
it on. Students learn the secure software/system development lifecycle (secure SDLC),
threat modelling as a design activity, deriving and specifying security requirements,
and the principle of secure defaults — grounded in **NIST SP 800-160** systems
security engineering. The discipline is preventive: most vulnerabilities are design
decisions, and the cheapest place to fix them is before they are built.

Secure design is the foundation of the Security Engineering major and the engineering
counterpart to the architecture principles in SC02. Its maturity is measured by
software-assurance models — **BSIMM** and **OWASP SAMM** (with **SSE-CMM / ISO/IEC
21827** at the systems level), now part of the degree's capability-maturity cross-walk
(`docs/maturity-models.md`). In the Australian context, secure defaults align with
the ASD Essential Eight. SE01 builds on F04 (Security Concepts) and SC02, and
underpins SE02–SE06.

---

## Prerequisites

- SC02 — Security Architecture Principles
- F04 — Security Concepts & Principles

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** a system design for security weaknesses using threat modelling.
2. **Apply** secure-SDLC practices across the development lifecycle.
3. **Design** security requirements and secure defaults for a system.
4. **Evaluate** a design against NIST SP 800-160 systems-security-engineering
   principles.
5. **Analyse** the maturity of a secure-development capability using BSIMM/OWASP
   SAMM.
6. **Recommend** design improvements that reduce risk by construction.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of secure system
design, threat modelling, and systems security engineering.

**Skills (AQF 7.2):** Students develop design and evaluative skills by threat
modelling and specifying security requirements.

**Application (AQF 7.3):** Students apply secure design to realistic systems aligned
to Australian secure-configuration expectations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Architect (652) | SP-ARC-002 | T0050 | Define security requirements and secure design for systems | Lab 1 — Threat Model a Web App |
| NIST NICE DCWF | 2023 | Secure Software Assessor | SP-DEV-002 | T0111 | Assess designs against secure engineering principles | Lab 2 — SP 800-160 Design Audit |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Solution architecture | ARCH | Level 4–5 | Lab 1, Lab 2 |
| Systems & software life cycle / assurance | SURE | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Security Architecture | Secure Design | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | SE01-K01 | Knowledge of security-by-design principles | Topic 1 |
| Knowledge | SE01-K02 | Knowledge of the secure SDLC | Topic 2 |
| Knowledge | SE01-K03 | Knowledge of threat modelling as a design activity | Topic 3 |
| Knowledge | SE01-K04 | Knowledge of security requirements and NIST SP 800-160 systems security engineering | Topic 4; Topic 5 |
| Skill | SE01-S01 | Skill in threat modelling a web application | Lab 1 |
| Skill | SE01-S02 | Skill in auditing a design against SP 800-160 | Lab 2 |
| Ability | SE01-A01 | Ability to derive security requirements from a threat model | Lab 1; Topic 4 |
| Ability | SE01-A02 | Ability to assess a design against secure-engineering principles | Lab 2; Topic 6 |
| Task | T0050 | Define security requirements and secure design for systems | Lab 1 |
| Task | T0111 | Assess designs against secure engineering principles | Lab 2 |

---

## Topics

### Topic 1: Security by Design

This topic establishes the case for designing security in: most vulnerabilities
originate in design, fixing them late is expensive, and secure defaults reduce the
attack surface for everyone. It introduces secure-by-design/default as a principle
(linking to F04/SC02).

**Key concepts:**
- Vulnerabilities as design decisions
- Cost of late remediation
- Secure-by-design and secure defaults

---

### Topic 2: The Secure SDLC

This topic covers integrating security across the lifecycle: requirements, design,
implementation, verification, and operations — and the gates and activities at each
stage (threat modelling, design review, testing).

**Key concepts:**
- Security activities per lifecycle stage
- Design reviews and security gates
- Shifting security left

---

### Topic 3: Threat Modelling as Design

This topic teaches threat modelling at engineering depth (building on F04): data-flow
diagrams, trust boundaries, STRIDE enumeration, and turning threats into prioritised
design mitigations and requirements.

**Key concepts:**
- Data-flow diagrams and trust boundaries
- STRIDE at design depth
- Threats → mitigations → requirements

---

### Topic 4: Security Requirements

This topic teaches deriving and specifying security requirements: from risk and
threat models, expressed testably, and traced through design and verification (so
every requirement is justified and checkable).

**Key concepts:**
- Deriving requirements from risk/threats
- Testable, traceable requirements
- Abuse/misuse cases

---

### Topic 5: NIST SP 800-160 Systems Security Engineering

This topic covers the systems-security-engineering view: applying SP 800-160
principles and lifecycle processes to engineer trustworthy systems, and auditing a
design against them.

**Key concepts:**
- SP 800-160 principles and processes
- Trustworthiness and assurance
- Design auditing against the standard

---

### Topic 6: Secure-Development Maturity

This topic connects secure design to capability maturity: **BSIMM** (observed
practices) and **OWASP SAMM** (prescriptive software-assurance maturity), plus
**SSE-CMM (ISO/IEC 21827)** at the systems level — assessing and maturing a
secure-development capability (see `docs/maturity-models.md`).

**Key concepts:**
- BSIMM and OWASP SAMM
- SSE-CMM (ISO/IEC 21827)
- Assessing/maturing secure development

**Australian context:** Secure defaults map to ASD Essential Eight configuration
expectations.

---

## Labs & Exercises

### Lab 1: Threat Model a Web Application

**Objective:** Produce a design-level threat model and derive security requirements.

**Prerequisites:**
- Topics 1–4

**Environment:**
- Operating System: any (analysis lab)
- Tools: Microsoft Threat Modelling Tool (free) or draw.io, a requirements template —
  all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take a fictional web application (e.g. customer portal with auth and a database).
2. Build a data-flow diagram with trust boundaries.
3. Enumerate threats with STRIDE per element/flow.
4. Derive prioritised, testable security requirements from the threats.
5. Specify secure defaults for the system.
6. Trace each top threat to a requirement and a verification method.

**Expected Output:**

A threat model (DFD + STRIDE table), prioritised security requirements with secure
defaults, and a threat→requirement→verification trace. Learners can justify each
requirement by the threat it mitigates.

**Reflection Questions:**

1. Which STRIDE category produced the most design risk, and why?
2. Which secure default most reduces the attack surface?
3. How would these requirements be verified later in the SDLC?

---

### Lab 2: SP 800-160 Design Audit

**Objective:** Audit a set of system design decisions against NIST SP 800-160
principles and produce a gap analysis.

**Prerequisites:**
- Topics 5–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: the NIST SP 800-160 reference, a gap-analysis template — all free
- Minimum hardware: trivial

**Instructions:**

1. Take a provided set of system design decisions.
2. Assess each against relevant SP 800-160 principles (e.g. least privilege,
   mediated access, trustworthiness).
3. Identify gaps and the risk each creates.
4. Assess the secure-development maturity implied (BSIMM/SAMM level).
5. Recommend prioritised design improvements.
6. Map secure-default gaps to ASD Essential Eight.

**Expected Output:**

A gap analysis against SP 800-160 with risks, a maturity read, and prioritised
improvements mapped to Essential Eight. Learners can defend the gap prioritisation.

**Reflection Questions:**

1. Which gap most undermines system trustworthiness, and why?
2. What does the design reveal about the team's secure-development maturity?
3. Which improvement gives the most risk reduction by construction?

---

## Assessment

### Formative Assessment: Threat-to-Requirement Drill

**Type:** Self-check exercise with answer key

**Description:** Given design threats, students derive a testable security requirement
and a secure default for each. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with model requirements and defaults.

---

### Summative Assessment: Secure Design Specification

**Type:** Design report

**Description:** For an assigned system, students (a) produce a design-level threat
model, (b) derive prioritised, testable security requirements and secure defaults,
(c) audit the design against NIST SP 800-160, and (d) assess secure-development
maturity (BSIMM/SAMM) and recommend improvements. Deliverable: 2,500–3,000 word
specification with a threat model.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Threat model | LO1 |
| Requirements & secure defaults | LO2, LO3 |
| SP 800-160 audit | LO4 |
| Maturity & improvements | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Threat modelling | Thorough, prioritised, design-level | Sound | Partial | Weak |
| Requirements | Testable, traceable, justified | Adequate | Vague | Poor |
| SP 800-160 audit | Precise, principle-grounded | Mostly | Superficial | Inaccurate |
| Maturity & improvement | Insightful BSIMM/SAMM read; actionable | Reasonable | Generic | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Secure defaults and configuration expectations.
- **ACSC secure-configuration guidance:** Reference for secure defaults.
- **Australian secure-by-design direction:** Government/ACSC secure-by-design
  messaging frames the unit's philosophy.

---

## Further Reading

**NIST (2018).** *SP 800-160 Vol. 1 — Systems Security Engineering.* NIST. https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final
> Relevance: The systems-security-engineering basis for Topics 5 and Lab 2.

**Shostack, A. (2014).** *Threat Modeling: Designing for Security.* Wiley.
> Relevance: The threat-modelling method applied in Topic 3 and Lab 1.

**BSIMM & OWASP SAMM (2024).** *Software security maturity models.* https://www.bsimm.com / https://owaspsamm.org
> Relevance: The secure-development maturity models for Topic 6 (see `docs/maturity-models.md`).

**ISO/IEC (2008).** *ISO/IEC 21827 — Systems Security Engineering Capability Maturity Model (SSE-CMM).* ISO.
> Relevance: The systems-level security-engineering maturity model (paid standard).

**Australian Cyber Security Centre (2024).** *Secure-by-Design & Essential Eight guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian secure-configuration/secure-by-design expectations (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SE01 |
| Unit Title | Secure System Design |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Security Engineering |
| Prerequisites | SC02, F04 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (ASD Essential Eight / secure-by-design) |
