# SC02: Security Architecture Principles

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches students to design security into systems rather than bolt it on
afterwards. It covers the discipline of security architecture: translating
business requirements and risk into a coherent set of structures, controls, and
patterns. The unit is anchored on three complementary bodies of work — **SABSA**
(a business-driven architecture method), **Zero Trust** (NIST SP 800-207), and
**NIST SP 800-160** (systems security engineering) — and teaches students to apply
architectural principles, reference patterns, and trust models to real designs.

Security architecture is where the strategic and operational halves of the degree
meet: an architecture exists to make the threat-informed defense of the
operational core achievable and sustainable, and to satisfy the risk and
compliance obligations of the strategic core. In the Australian context,
architecture decisions are shaped by the **Australian Government ISM**, the
**Essential Eight**, and Zero Trust directions in government and industry. SC02
builds on F01–F04 and SC01, and feeds the Security Engineering major.

---

## Prerequisites

- F04 — Security Concepts & Principles
- SC01 — Risk Management Frameworks

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** the role and layers of security architecture and how business and
   risk drive architectural decisions.
2. **Apply** the SABSA approach to derive security requirements from business
   context.
3. **Analyse** a system design against architectural principles (defence in depth,
   least privilege, segmentation, secure-by-design).
4. **Apply** Zero Trust principles (NIST SP 800-207) to a network/identity
   architecture.
5. **Examine** secure systems engineering practice (NIST SP 800-160) and reference
   architectures.
6. **Analyse** an architecture for alignment with Australian standards (ISM,
   Essential Eight) and risk obligations.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of security
architecture methods, trust models, and secure-systems-engineering practice.

**Skills (AQF 7.2):** Students develop analytical and design skills by deriving
requirements and evaluating and improving architectures.

**Application (AQF 7.3):** Students apply architecture methods to realistic
systems, aligning designs with Australian standards and risk obligations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Architect | SP-ARC-002 | T0050 | Define and document security architecture and design requirements | Lab 1 — SABSA-Driven Architecture |
| NIST NICE DCWF | 2023 | Enterprise Architect | SP-ARC-001 | T0473 | Apply secure design and Zero Trust principles to system architecture | Lab 2 — Zero Trust Redesign |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Solution architecture | ARCH | Level 5 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Security Architecture | Secure Design | Practitioner | Lab 1, Lab 2 |

---

## Topics

### Topic 1: What Security Architecture Is

Security architecture is the structured translation of business intent and risk
into a coherent system of controls and patterns. This topic positions architecture
relative to enterprise architecture, distinguishes architecture from engineering
and operations, and introduces the idea of architectural layers (contextual,
conceptual, logical, physical, component) that recur in SABSA.

**Key concepts:**
- Architecture as business/risk translation
- Architecture vs engineering vs operations
- Architectural layers and traceability

---

### Topic 2: Business-Driven Architecture with SABSA

SABSA derives security from business requirements rather than from a control
checklist. This topic teaches the SABSA approach: starting from business
attributes and risk, working down through conceptual and logical layers to
physical and component decisions, maintaining traceability so every control exists
for a business reason. This traceability is also what makes architecture
defensible to auditors and customers.

**Key concepts:**
- Business attributes and risk as the starting point
- The SABSA layered model and traceability
- Justifying controls by business need

---

### Topic 3: Architectural Principles and Patterns

This topic covers the durable principles (defence in depth, least privilege,
segmentation, fail-secure, secure-by-design/default, minimise attack surface) and
common reference patterns (tiered architectures, DMZs, secure service edges,
identity-centric designs). Students learn to recognise principles in — or absent
from — a design and to apply patterns appropriately.

**Key concepts:**
- Core architectural principles
- Reference patterns and when to use them
- Recognising principle violations in designs

---

### Topic 4: Zero Trust Architecture

Zero Trust replaces implicit network trust with continuous, explicit verification.
This topic teaches the NIST SP 800-207 model: the policy decision/enforcement
points, identity as the new perimeter, micro-segmentation, device trust, and
least-privilege access per request. It contrasts Zero Trust with perimeter models
and addresses pragmatic, phased adoption.

**Key concepts:**
- NIST SP 800-207 components and tenets
- Identity-centric security and micro-segmentation
- Pragmatic, phased Zero Trust adoption

**Australian context:** Zero Trust aligns with directions in the Australian
Government ISM and broader public-sector modernisation.

---

### Topic 5: Secure Systems Engineering and Reference Architectures

This topic covers building security in across the system lifecycle using NIST SP
800-160 systems-security-engineering principles, secure SDLC integration, and the
use of reference architectures and cloud well-architected security guidance.
It connects design decisions to the operational telemetry and controls the rest
of the degree relies on.

**Key concepts:**
- NIST SP 800-160 lifecycle-based security engineering
- Secure SDLC and security in design reviews
- Reference and cloud well-architected security

---

### Topic 6: Evaluating Architecture Against Standards and Risk

Architecture must satisfy obligations and risk. This topic teaches evaluating a
design against the **Australian Government ISM** and **Essential Eight**, against
the risk register from SC01, and against architectural principles — producing a
gap analysis and an improvement roadmap. It frames architecture review as a
recurring activity, not a one-off.

**Key concepts:**
- Evaluating designs against ISM/Essential Eight
- Architecture gap analysis and roadmaps
- Architecture review as a continuous practice

**Australian context:** Uses the ISM and Essential Eight as the evaluation
baseline.

---

## Labs & Exercises

### Lab 1: SABSA-Driven Architecture

**Objective:** Use a SABSA-style approach to derive security requirements and a
logical architecture from business context.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: any
- Tools: draw.io / diagrams.net (free), a requirements template
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario (e.g. an Australian fintech launching a customer portal) and
   capture its key business attributes and top risks (reuse SC01).
2. Derive conceptual security requirements from those attributes.
3. Develop a logical architecture diagram showing trust zones, identity, data
   flows, and key controls.
4. Trace each major control back to the business attribute/risk it serves.
5. Identify which architectural principles your design embodies.
6. Note one trade-off you made and why.

**Expected Output:**

A logical architecture diagram with a traceability table (control → business
attribute/risk) and a principle checklist. Learners can justify every control by
business need.

**Reflection Questions:**

1. How did starting from business attributes change the design versus a control-
   checklist approach?
2. Which control was hardest to justify, and what does that suggest?
3. How would this traceability help in a SOC 2 or ISO 27001 audit?

---

### Lab 2: Zero Trust Redesign

**Objective:** Redesign a traditional perimeter architecture toward Zero Trust and
evaluate it against Australian standards.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: draw.io, NIST SP 800-207 and ISM/Essential Eight references (free)
- Minimum hardware: trivial

**Instructions:**

1. Start from a provided legacy perimeter architecture (flat internal network,
   VPN, implicit trust).
2. Identify the implicit-trust assumptions and the risks they create.
3. Redesign toward Zero Trust: identity-centric access, micro-segmentation, policy
   decision/enforcement points, device trust.
4. Map the redesign to NIST SP 800-207 tenets.
5. Evaluate the redesign against the Essential Eight and relevant ISM controls;
   note residual gaps.
6. Propose a phased adoption roadmap (what first, what later, and why).

**Expected Output:**

A before/after architecture, a mapping to SP 800-207 tenets, an Essential
Eight/ISM evaluation, and a phased roadmap. Learners can explain why full Zero
Trust is a journey, not a switch.

**Reflection Questions:**

1. Which Zero Trust change reduces the most risk for the least disruption?
2. How does identity-centric design change the operational telemetry the SOC
   needs (link to OC02)?
3. Where do Australian standards push for, or constrain, your design?

---

## Assessment

### Formative Assessment: Principle & Pattern Review

**Type:** Design-critique exercise with answer key

**Description:** Given several small architecture diagrams, students identify which
principles are present or violated and suggest a pattern to fix each weakness.
Self-marked.

**Learning Outcomes Assessed:** LO3, LO4

**Feedback mechanism:** Answer key identifying the principle issues and suggested
patterns per diagram.

---

### Summative Assessment: Security Architecture Design & Review

**Type:** Design report

**Description:** For an assigned Australian organisation, students (a) derive
security requirements from business context (SABSA-style), (b) produce a logical
architecture with Zero Trust principles, (c) trace controls to business/risk, (d)
evaluate the design against the ISM/Essential Eight and the SC01 risk register, and
(e) deliver a prioritised improvement roadmap. Deliverable: 2,500–3,000 word report
with diagrams and a traceability/evaluation table.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Requirements derivation (SABSA) | LO1, LO2 |
| Architecture with Zero Trust | LO3, LO4 |
| Standards/risk evaluation & roadmap | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Business-driven design | Every control traced to business/risk | Mostly traced design | Partial traceability | Control-checklist with no traceability |
| Principle & Zero Trust application | Sophisticated, correct application | Sound application | Partial or uneven | Principles largely absent |
| Standards evaluation | Precise ISM/Essential Eight evaluation with gaps | Solid evaluation | Superficial evaluation | Little meaningful evaluation |
| Roadmap | Pragmatic, prioritised, justified | Reasonable roadmap | Generic roadmap | No clear roadmap |
| Communication | Clear, professional, well-diagrammed | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Australian Government ISM:** The control baseline for architecture evaluation
  (Topic 6, both labs).
- **ASD Essential Eight:** Used to assess architectural maturity.
- **Zero Trust in Australian government/industry:** Framed as a current direction
  shaping local architecture decisions.

---

## Further Reading

**SABSA Institute (2024).** *SABSA — Enterprise Security Architecture.* https://sabsa.org
> Relevance: The business-driven architecture method anchoring Topic 2 and Lab 1.

**NIST (2020).** *SP 800-207 Zero Trust Architecture.* NIST. https://csrc.nist.gov/pubs/sp/800/207/final
> Relevance: The authoritative, freely available Zero Trust model used in Topic 4 and Lab 2.

**NIST (2018).** *SP 800-160 Vol. 1 — Systems Security Engineering.* NIST. https://csrc.nist.gov
> Relevance: The systems-security-engineering basis for Topic 5.

**Australian Cyber Security Centre (2024).** *Australian Government Information Security Manual (ISM).* ACSC. https://www.cyber.gov.au/ism
> Relevance: The Australian control baseline used to evaluate architectures (Australian source).

**Sherwood, J., Clark, A. & Lynas, D. (2005).** *Enterprise Security Architecture: A Business-Driven Approach.* CRC Press.
> Relevance: The foundational SABSA text supporting requirements derivation.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SC02 |
| Unit Title | Security Architecture Principles |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Strategic Core |
| Major / Pathway | Strategic |
| Prerequisites | F04, SC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | None directly (Australian Government ISM / Essential Eight) |
