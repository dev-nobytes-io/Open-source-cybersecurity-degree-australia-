# GR01: Security Governance Design

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (GRC/risk/compliance experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches the design of security governance: the structures, policies, roles,
and accountabilities through which an organisation directs and oversees its security.
Students learn to build a policy hierarchy (policy → standard → procedure →
guideline), assign accountability with tools like RACI, and design the governance
bodies (board oversight, steering committees) that connect strategy, risk, and
operations — anchored on the **NIST CSF 2.0 Govern** function.

Governance is the foundation of the GRC major and of the whole compliance-as-revenue
thesis from SC03: well-designed governance is what auditors, regulators, and
customers rely on. In the Australian context it is shaped by **APRA CPS 234** board
and senior-management obligations and **ASIC** cyber expectations for financial
services. GRC maturity is tracked via the **OCEG GRC Capability Model** (see
`docs/maturity-models.md`). GR01 builds on SC03 (Governance) and SC05, and underpins
GR02–GR06.

---

## Prerequisites

- SC03 — Governance, Policy & Compliance
- SC01 — Risk Management Frameworks

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** a security governance structure with clear roles and accountability.
2. **Apply** the policy hierarchy to author fit-for-purpose governance documents.
3. **Analyse** the NIST CSF 2.0 Govern function and apply it to an organisation.
4. **Evaluate** board and senior-management obligations under APRA CPS 234.
5. **Design** accountability tools (e.g. RACI) for cybersecurity governance.
6. **Recommend** a governance design appropriate to an organisation's sector and
   risk.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of security
governance design and the Australian governance-regulatory context.

**Skills (AQF 7.2):** Students develop design and analytical skills by building
governance structures, policies, and accountability tools.

**Application (AQF 7.3):** Students apply governance design to realistic Australian
organisations with regulatory alignment.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Policy & Strategy Planner (752) | OV-SPP-001 | T0226 | Develop security policies, standards, and governance artefacts | Activity 1 — Policy Hierarchy |
| NIST NICE DCWF | 2023 | Information Systems Security Manager (722) | OV-MGT-001 | T0147 | Define governance roles and accountability | Activity 2 — Governance RACI |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information management / governance | GOVN | Level 5 | Activity 1, Activity 2 |
| Information risk management | IRMG | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Governance Design | Practitioner–Advanced | Activity 1, Activity 2 |

---

## Topics

### Topic 1: What Security Governance Is

This topic frames governance as direction and oversight: setting objectives,
allocating accountability, and ensuring security serves the organisation's strategy
and risk appetite — distinct from management and operations.

**Key concepts:**
- Direction and oversight vs management
- Accountability and authority
- Governance serving strategy and risk

---

### Topic 2: The NIST CSF 2.0 Govern Function

This topic covers the Govern function introduced in CSF 2.0: organisational context,
risk management strategy, roles/responsibilities, policy, and oversight — and how it
connects the other CSF functions.

**Key concepts:**
- CSF 2.0 Govern categories
- Govern as the connective function
- Applying Govern to an organisation

---

### Topic 3: The Policy Hierarchy

This topic teaches building governance documents: policy (intent/authority), standard
(mandatory specifics), procedure (steps), guideline (recommended practice), plus the
lifecycle (drafting, approval, exception, review) — enforceable, not shelfware.

**Key concepts:**
- Policy/standard/procedure/guideline
- Document lifecycle and exceptions
- Enforceable, usable governance documents

---

### Topic 4: Roles, Accountability, and RACI

This topic teaches assigning accountability: governance roles (board, executive,
CISO, risk/audit committees, asset/risk owners) and tools like RACI to make
responsibility explicit and avoid gaps/overlaps.

**Key concepts:**
- Governance roles and committees
- RACI and accountability mapping
- Avoiding gaps and overlaps

---

### Topic 5: Australian Governance Obligations

This topic covers the Australian frame: APRA CPS 234 board/senior-management
obligations, ASIC cyber expectations for financial services, and how governance must
be evidenced to regulators.

**Key concepts:**
- APRA CPS 234 board/senior-management obligations
- ASIC cyber expectations
- Evidencing governance to regulators

**Australian context:** This topic is the Australian governance-regulatory frame.

---

### Topic 6: Governance Maturity

This topic connects governance to capability maturity: assessing and maturing the GRC
function with the **OCEG GRC Capability Model** and program models (C2M2/CSF Tiers),
keeping governance a living, improving capability (see `docs/maturity-models.md`).

**Key concepts:**
- OCEG GRC Capability Model
- C2M2 / CSF Tiers for program maturity
- Governance as a maturing capability

---

## Labs & Exercises

### Lab 1: Policy Hierarchy (deliverable activity)

**Objective:** Design a security policy hierarchy for a fictional mid-size Australian
organisation.

**Prerequisites:**
- Topics 1–3

**Environment:**
- No technical environment — a documentation deliverable using draw.io and NIST CSF
  2.0 / ISO 27001 references. Any device within the 8 GB / 4-core / 50 GB spec.

**Instructions:**

1. Take a fictional mid-size Australian organisation (sector, size, risk).
2. Design the policy hierarchy: a top-level security policy plus the standards,
   procedures, and guidelines beneath it.
3. Draft one policy and one supporting standard in full.
4. Define the document lifecycle (approval, exceptions, review cadence).
5. Map the policy set to the NIST CSF 2.0 Govern outcomes.
6. Note how the hierarchy would be evidenced in an audit.

**Expected Output:**

A policy hierarchy with one complete policy and standard, lifecycle, and CSF Govern
mapping. Learners can explain why the documents are enforceable and audit-ready.

**Reflection Questions:**

1. Where is the line between policy and standard, and why does it matter?
2. How would this hierarchy be evidenced to APRA or an ISO 27001 auditor?
3. What makes a policy shelfware, and how did you avoid it?

---

### Lab 2: Governance RACI (deliverable activity)

**Objective:** Create a RACI matrix for cybersecurity governance roles in a fictional
financial-services organisation.

**Prerequisites:**
- Topics 4–6

**Environment:**
- No technical environment — a deliverable (spreadsheet/table). Any device.

**Instructions:**

1. Take a fictional Australian financial-services organisation.
2. List the key governance activities (policy approval, risk acceptance, incident
   escalation, audit, etc.).
3. Identify the roles (board, executive, CISO, risk/audit committee, owners).
4. Build a RACI matrix mapping roles to activities.
5. Check for accountability gaps and overlaps and resolve them.
6. Map the board/senior-management accountabilities to APRA CPS 234.

**Expected Output:**

A complete governance RACI with no accountability gaps, mapped to APRA CPS 234
board/senior-management obligations. Learners can justify each accountability
assignment.

**Reflection Questions:**

1. Which activity was hardest to assign accountability for, and why?
2. How does APRA CPS 234 shape board vs management accountability?
3. Where would an accountability gap create real risk?

---

## Assessment

### Formative Assessment: Document-Type Drill

**Type:** Self-check exercise with answer key

**Description:** Given governance statements, students classify each as policy/
standard/procedure/guideline and assign accountability. Self-marked.

**Learning Outcomes Assessed:** LO2, LO5

**Feedback mechanism:** Answer key with the document type and accountability.

---

### Summative Assessment: Governance Design

**Type:** Design report

**Description:** For an assigned Australian organisation, students (a) design a
governance structure with roles and committees, (b) build a policy hierarchy with a
complete policy/standard, (c) produce a governance RACI, and (d) map board/senior-
management obligations to APRA CPS 234 and assess governance maturity (OCEG).
Deliverable: 2,500–3,000 word design.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Governance structure | LO1, LO3 |
| Policy hierarchy | LO2 |
| RACI & accountability | LO5 |
| APRA mapping & maturity | LO4, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Governance design | Clear, accountable, sector-fit | Sound | Partial | Weak |
| Policy quality | Enforceable, audit-ready | Adequate | Vague | Unusable |
| Accountability | Complete RACI, no gaps | Mostly | Some gaps | Poor |
| Regulatory & maturity | Precise APRA mapping; maturity-aware | Mostly | Superficial | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **APRA CPS 234:** Board and senior-management governance obligations.
- **ASIC cyber expectations:** Governance expectations for financial services.
- **OCEG GRC Capability Model:** Governance maturity (see `docs/maturity-models.md`).

---

## Further Reading

**NIST (2024).** *Cybersecurity Framework 2.0 — Govern function.* NIST. https://www.nist.gov/cyberframework
> Relevance: The governance function anchoring Topic 2.

**APRA (2019).** *Prudential Standard CPS 234 & CPG 234 guidance.* APRA. https://www.apra.gov.au
> Relevance: The Australian governance obligations central to Topic 5 (Australian source).

**OCEG (2024).** *GRC Capability Model ("Red Book").* OCEG. https://www.oceg.org
> Relevance: The GRC maturity/capability model for Topic 6 (see `docs/maturity-models.md`).

**ISACA (2024).** *CISM — Information Security Governance.* ISACA. https://www.isaca.org
> Relevance: The governance grounding and certification bridge for this major.

**ASIC (2024).** *Cyber resilience guidance for regulated entities.* ASIC. https://www.asic.gov.au
> Relevance: Australian regulator expectations for cyber governance (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | GR01 |
| Unit Title | Security Governance Design |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | GRC |
| Prerequisites | SC03, SC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | APRA CPS 234 (board/governance obligations) |
