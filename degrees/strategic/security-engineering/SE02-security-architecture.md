# SE02: Security Architecture

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (security architecture/engineering)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit takes the architecture *principles* from SC02 and turns them into *applied
architecture design*: structuring real systems and estates using **SABSA**, designing
**Zero Trust** access (NIST SP 800-207), and architecting security for hybrid and
cloud environments. Where SC02 established the discipline, SE02 builds the artefacts —
logical and physical architectures, trust zones, and reference designs — that an
engineer hands to implementers.

Security architecture is the structural backbone of the Security Engineering major;
its maturity is tracked via **SSE-CMM (ISO/IEC 21827)** in the degree's
capability-maturity cross-walk (`docs/maturity-models.md`). In the Australian context
it is shaped by ASD architecture guidance, the **Australian Government ISM**, and the
**IRAP** assessment framework for systems handling government data. SE02 builds on
SC02 and SE01, and underpins SE03–SE06.

---

## Prerequisites

- SE01 — Secure System Design
- SC02 — Security Architecture Principles

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the SABSA layered model to architect a security solution from business
   requirements.
2. **Design** a Zero Trust access architecture (NIST SP 800-207) for a hybrid-cloud
   scenario.
3. **Analyse** cloud security architecture patterns and shared-responsibility
   boundaries.
4. **Evaluate** an architecture against the Australian Government ISM and IRAP
   expectations.
5. **Design** reference architectures with documented trust zones and controls.
6. **Recommend** an architecture that satisfies business, risk, and regulatory needs.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of applied security
architecture, Zero Trust, and cloud security design.

**Skills (AQF 7.2):** Students develop design skills by producing architectures and
evaluating them against standards.

**Application (AQF 7.3):** Students apply architecture design to realistic
hybrid-cloud Australian scenarios with regulatory alignment.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Architect (652) | SP-ARC-002 | T0050 | Develop and document security architecture | Lab 1 — SABSA Architecture |
| NIST NICE DCWF | 2023 | Enterprise Architect | SP-ARC-001 | T0473 | Apply Zero Trust and cloud patterns to architecture | Lab 2 — Zero Trust for Hybrid Cloud |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Solution architecture | ARCH | Level 5 | Lab 1, Lab 2 |
| Information security | SCTY | Level 5 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Security Architecture | Architecture Design | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Applied SABSA

This topic operationalises SABSA (from SC02): working through the layers (contextual
→ conceptual → logical → physical → component) to derive a traceable architecture
from business attributes and risk, producing real design artefacts.

**Key concepts:**
- The SABSA layers as a design workflow
- Business-attribute-driven architecture
- Traceability from business to component

---

### Topic 2: Zero Trust Architecture (Applied)

This topic teaches designing Zero Trust (NIST SP 800-207): policy decision/enforcement
points, identity-centric access, micro-segmentation, and device trust — applied to a
concrete hybrid-cloud design with a phased adoption path.

**Key concepts:**
- SP 800-207 components in a real design
- Identity-centric access and micro-segmentation
- Phased Zero Trust adoption

---

### Topic 3: Cloud Security Architecture

This topic covers architecting security for cloud and hybrid: the shared-
responsibility model, landing zones, network and identity design in cloud, and
well-architected security guidance — vendor-neutral with worked patterns.

**Key concepts:**
- Shared responsibility and landing zones
- Cloud network/identity architecture
- Well-architected security patterns

---

### Topic 4: Reference Architectures and Patterns

This topic teaches using and producing reference architectures: secure patterns
(segmented tiers, secure service edge, secure data flows), when to apply each, and
documenting them for reuse.

**Key concepts:**
- Reference architectures and secure patterns
- Pattern selection
- Documenting for reuse

---

### Topic 5: Architecture in the Australian Regulatory Context

This topic covers designing to Australian expectations: the Australian Government ISM
controls, the IRAP assessment framework for government-data systems, and how
regulatory context constrains and shapes architecture.

**Key concepts:**
- Australian Government ISM controls
- IRAP assessment framework
- Regulatory constraints on architecture

**Australian context:** This topic is the Australian architecture-regulatory frame
(ISM, IRAP).

---

### Topic 6: Architecture Maturity and Governance

This topic covers governing and maturing the architecture function: architecture
review boards, exceptions, and assessing architecture-engineering maturity with
SSE-CMM (ISO/IEC 21827) — keeping architecture a living, governed capability.

**Key concepts:**
- Architecture governance and review boards
- SSE-CMM (ISO/IEC 21827) maturity
- Continuous architecture practice

---

## Labs & Exercises

### Lab 1: SABSA Architecture (design activity)

**Objective:** Map a fictional organisation's architecture to the SABSA layers and
produce a logical security architecture.

**Prerequisites:**
- Topics 1, 4

**Environment:**
- Operating System: any
- Tools: draw.io / Excalidraw, a SABSA layer template — all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take a fictional Australian organisation with business attributes and risk.
2. Work through the SABSA layers to derive security requirements and a logical
   architecture.
3. Produce a logical architecture diagram with trust zones, identity, and controls.
4. Trace each major control to a business attribute/risk.
5. Identify the reference patterns used.
6. Note one trade-off and its justification.

**Expected Output:**

A SABSA-derived logical architecture with a traceability table and identified
patterns. Learners can justify every control by business need.

**Reflection Questions:**

1. Which control was hardest to trace to a business attribute, and why?
2. Which pattern most improved the design?
3. How would this architecture change for a different risk profile?

---

### Lab 2: Zero Trust for Hybrid Cloud (design activity)

**Objective:** Design a Zero Trust network access model for a hybrid-cloud scenario
and evaluate it against Australian standards.

**Prerequisites:**
- Topics 2, 3, and 5 and Lab 1

**Environment:**
- Operating System: any
- Tools: draw.io, NIST SP 800-207 and ISM references — all free
- Minimum hardware: trivial

**Instructions:**

1. Take a hybrid-cloud scenario (on-prem + cloud, remote workforce).
2. Design a Zero Trust access model: policy decision/enforcement points,
   identity-centric access, micro-segmentation, device trust.
3. Map the design to NIST SP 800-207 tenets.
4. Address the cloud shared-responsibility boundaries.
5. Evaluate against the Australian Government ISM and note IRAP considerations.
6. Propose a phased adoption roadmap.

**Expected Output:**

A Zero Trust hybrid-cloud architecture mapped to SP 800-207, an ISM/IRAP evaluation,
and a phased roadmap. Learners can explain why full Zero Trust is a journey.

**Reflection Questions:**

1. Which Zero Trust change reduces the most risk for the least disruption?
2. How do the cloud shared-responsibility boundaries shape the design?
3. Where do ISM/IRAP requirements constrain your architecture?

---

## Assessment

### Formative Assessment: Pattern & Layer Drill

**Type:** Self-check exercise with answer key

**Description:** Given design needs, students choose the SABSA layer and reference
pattern that apply and justify them. Self-marked.

**Learning Outcomes Assessed:** LO1, LO5

**Feedback mechanism:** Answer key with the layer/pattern and rationale.

---

### Summative Assessment: Security Architecture Design

**Type:** Design report

**Description:** For an assigned Australian organisation, students (a) derive a SABSA
logical architecture, (b) design Zero Trust access for its hybrid-cloud estate, (c)
evaluate against the ISM/IRAP, and (d) document reference patterns, trade-offs, and a
phased roadmap. Deliverable: 2,500–3,000 word design with diagrams and a traceability
table.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| SABSA architecture | LO1, LO5 |
| Zero Trust / cloud design | LO2, LO3 |
| ISM/IRAP evaluation | LO4 |
| Recommendation & roadmap | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Architecture quality | Coherent, traceable, pattern-driven | Sound | Partial | Weak |
| Zero Trust / cloud | Sophisticated, correct application | Adequate | Uneven | Poor |
| Regulatory evaluation | Precise ISM/IRAP evaluation | Mostly | Superficial | Absent |
| Recommendation | Pragmatic, justified roadmap | Reasonable | Generic | Weak |
| Communication | Clear, well-diagrammed | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Australian Government ISM:** The control baseline for architecture evaluation.
- **IRAP:** The assessment framework for systems handling Australian government data.
- **ASD architecture/Zero Trust guidance:** Shapes the design direction.

---

## Further Reading

**SABSA Institute (2024).** *SABSA — Enterprise Security Architecture.* https://sabsa.org
> Relevance: The applied architecture method central to Topic 1 and Lab 1.

**NIST (2020).** *SP 800-207 Zero Trust Architecture.* NIST. https://csrc.nist.gov/pubs/sp/800/207/final
> Relevance: The Zero Trust model applied in Topic 2 and Lab 2 (freely available).

**Australian Cyber Security Centre (2024).** *Australian Government Information Security Manual (ISM) & IRAP.* ACSC. https://www.cyber.gov.au/ism
> Relevance: The Australian control baseline and assessment framework (Australian source).

**ISO/IEC (2008).** *ISO/IEC 21827 — SSE-CMM.* ISO.
> Relevance: The architecture/engineering maturity model for Topic 6 (see `docs/maturity-models.md`).

**Cloud Security Alliance (2024).** *Cloud Controls Matrix & security guidance.* CSA. https://cloudsecurityalliance.org
> Relevance: Vendor-neutral cloud security architecture guidance for Topic 3.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SE02 |
| Unit Title | Security Architecture |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Security Engineering |
| Prerequisites | SE01, SC02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (Australian Government ISM / IRAP) |
