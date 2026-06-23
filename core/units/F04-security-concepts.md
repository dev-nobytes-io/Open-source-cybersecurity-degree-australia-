# F04: Security Concepts & Principles

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit establishes the conceptual vocabulary and mental models that every
other unit in the degree assumes. Before specialising, a practitioner needs a
firm grasp of what security is trying to achieve (confidentiality, integrity,
availability and beyond), how we reason about threats and risk, the core
defensive principles (defence in depth, least privilege, zero trust), and the
foundational technologies — cryptography, authentication, and access control —
that implement those principles. The unit is deliberately concept-led and
tool-light: its job is to make the learner fluent in *why* before later units
focus on *how*.

In the Australian context, these concepts are operationalised by the ASD
*Essential Eight* and the ACSC *Information Security Manual*, which translate
abstract principles into concrete baseline controls. F04 is a prerequisite for
the entire Operational and Strategic core, and it gives Foundation learners the
risk and threat-modelling language they will use for the rest of their careers.

---

## Prerequisites

- F01 — Networking Fundamentals
- F02 — Operating Systems & Administration

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Define** the core security objectives (CIA triad, plus authenticity,
   non-repudiation, and accountability) and explain their trade-offs.
2. **Explain** threat, vulnerability, and risk and describe how they combine to
   determine exposure.
3. **Describe** the foundational defensive principles — defence in depth, least
   privilege, separation of duties, fail-secure, and zero trust.
4. **Demonstrate** a basic threat-modelling process for a simple system using a
   recognised method (e.g. STRIDE).
5. **Explain** the role of cryptography, authentication, and access control in
   enforcing security objectives.
6. **Identify** how the ASD Essential Eight implements these principles as
   baseline controls in the Australian context.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of
foundational security concepts: objectives, risk, defensive principles, and the
core enforcing technologies.

**Skills (AQF 7.2):** Students develop cognitive skills by reasoning about
threats and risk and by constructing a threat model, and communication skills by
articulating security trade-offs.

**Application (AQF 7.3):** Students apply these concepts to model and reason
about a realistic system, mapping principles to the Australian baseline controls
of the Essential Eight and ACSC ISM.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Control Assessor | SP-RSK-002 | T0177 | Perform security reviews and identify gaps in security architecture | Lab 1 — Threat Modelling a Web Application |
| NIST NICE DCWF | 2023 | Information Systems Security Manager | OV-MGT-001 | T0149 | Recommend resource allocations to mitigate identified risks | Lab 2 — Mapping Controls to the Essential Eight |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information security | SCTY | Level 3 | Throughout |
| Risk management | BURM | Level 2 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Technical Foundations | Security Principles | Foundational | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F04-K01 | Knowledge of security objectives (CIA, authenticity, non-repudiation, accountability) | Topic 1 |
| Knowledge | F04-K02 | Knowledge of threat, vulnerability, and risk and how they combine | Topic 2 |
| Knowledge | F04-K03 | Knowledge of defensive principles (defence in depth, least privilege, zero trust) | Topic 3 |
| Knowledge | F04-K04 | Knowledge of cryptography, authentication, and access-control fundamentals | Topic 5 |
| Skill | F04-S01 | Skill in threat modelling a system with STRIDE | Lab 1 |
| Skill | F04-S02 | Skill in mapping controls to principles and the ASD Essential Eight | Lab 2 |
| Ability | F04-A01 | Ability to reason about and prioritise security risks and trade-offs | Lab 1; Summative |
| Ability | F04-A02 | Ability to recommend prioritised, principle-based controls | Lab 2; Summative |
| Task | T0177 | Perform security reviews and identify gaps in security architecture | Lab 1 |
| Task | T0149 | Recommend resource allocations to mitigate identified risks | Lab 2 |

---

## Topics

### Topic 1: Security Objectives — CIA and Beyond

The CIA triad — confidentiality, integrity, availability — is the starting point
for reasoning about security, but it is incomplete. This topic adds authenticity,
non-repudiation, and accountability, and explores the tension between objectives
(e.g. availability vs confidentiality). Learners practise classifying a control
or incident by which objective it protects or violates.

**Key concepts:**
- CIA triad and its extensions
- Trade-offs and prioritisation between objectives
- Mapping controls and incidents to objectives

---

### Topic 2: Threats, Vulnerabilities, and Risk

Risk is the intersection of a threat exploiting a vulnerability to cause impact.
This topic defines each term precisely, introduces threat actors and their
motivations, and frames risk as something to be assessed and treated (accept,
mitigate, transfer, avoid). It establishes the risk vocabulary that SC01 later
develops formally.

**Key concepts:**
- Threat × vulnerability × impact as a model of risk
- Threat actor types and motivations
- Risk treatment options

**Australian context:** The ACSC annual *Cyber Threat Report* is used to ground
threat-actor discussion in the real Australian threat landscape.

---

### Topic 3: Defensive Principles

Good security design follows durable principles. This topic covers defence in
depth, least privilege, separation of duties, fail-secure defaults, complete
mediation, economy of mechanism, and the modern reframing of these ideas as
**zero trust**. Learners learn to recognise these principles (and their absence)
in real designs.

**Key concepts:**
- Defence in depth and layered controls
- Least privilege and separation of duties
- Zero trust as "never trust, always verify"

---

### Topic 4: Threat Modelling

Threat modelling is the structured practice of anticipating how a system could be
attacked, before it is built or deployed. This topic introduces a repeatable
process — define the system, identify assets and entry points, enumerate threats
(using STRIDE), and decide on mitigations. It is the most directly transferable
skill in the unit and recurs in SC02 and the Security Engineering major.

**Key concepts:**
- The threat-modelling process and data-flow diagrams
- STRIDE as a threat-enumeration framework
- From threats to prioritised mitigations

---

### Topic 5: Cryptography, Authentication, and Access Control

Principles need mechanisms. This topic gives a conceptual (not mathematical)
grounding in cryptography (symmetric vs asymmetric, hashing, digital signatures,
PKI/TLS), authentication (something you know/have/are, MFA), and access control
models (DAC, MAC, RBAC, ABAC). The emphasis is on what each provides and when to
use it.

**Key concepts:**
- Symmetric vs asymmetric cryptography; hashing and signatures
- Authentication factors and multi-factor authentication
- Access control models and their trade-offs

**Australian context:** Multi-factor authentication is an Essential Eight
mitigation; this topic explains the security objective it serves.

---

### Topic 6: From Principles to Baseline Controls

This topic closes the loop between abstract principles and the concrete controls
organisations are actually expected to implement. It maps each defensive
principle to baseline controls and introduces the ASD Essential Eight as
Australia's flagship baseline, showing how each of the eight mitigations
implements one or more of the principles covered in the unit.

**Key concepts:**
- From principle to control to configuration
- The ASD Essential Eight and its maturity model
- Why baselines exist and their limits

**Australian context:** The Essential Eight is examined directly as the
Australian baseline, with each mitigation traced back to a principle.

---

## Labs & Exercises

### Lab 1: Threat Modelling a Web Application

**Objective:** Produce a STRIDE threat model for a simple web application,
demonstrating structured threat reasoning.

**Prerequisites:**
- Topics 1–4
- A diagramming tool (draw.io / diagrams.net, free)

**Environment:**
- Operating System: any (this is an analysis lab)
- Tools: draw.io (free, browser or desktop), a text editor
- Minimum hardware: trivial; no GPU; runs on any machine within spec

**Instructions:**

1. Choose a simple system — e.g. a three-tier web app (browser → web/app server
   → database) with a login feature.
2. Draw a data-flow diagram showing components, data flows, and trust boundaries.
3. For each element/flow, enumerate threats using STRIDE (Spoofing, Tampering,
   Repudiation, Information disclosure, Denial of service, Elevation of
   privilege).
4. For each identified threat, record a candidate mitigation and the security
   objective it protects (from Topic 1).
5. Prioritise the threats (high/medium/low) with a one-line justification each.
6. Summarise the top three risks and recommended mitigations.

**Expected Output:**

A data-flow diagram with trust boundaries, a STRIDE threat table with mitigations
and mapped objectives, and a prioritised top-three. Learners can justify why each
top risk was ranked as it was.

**Reflection Questions:**

1. Which STRIDE category produced the most threats for your system, and why?
2. How did adding trust boundaries change which threats you identified?
3. Which of your mitigations correspond to an Essential Eight mitigation?

---

### Lab 2: Mapping Controls to the Essential Eight

**Objective:** Map defensive principles and a set of controls to the ASD
Essential Eight, demonstrating understanding of how principles become baselines.

**Prerequisites:**
- Topics 3, 5, and 6

**Environment:**
- Operating System: any
- Tools: the ACSC Essential Eight Maturity Model (free, online), a spreadsheet
  or markdown table
- Minimum hardware: trivial

**Instructions:**

1. List the eight mitigations of the ASD Essential Eight from the ACSC source.
2. For each mitigation, identify which defensive principle(s) from Topic 3 it
   implements and which security objective(s) from Topic 1 it protects.
3. Given a short scenario (a small business with a default Windows environment),
   assess at a high level which mitigations are likely absent.
4. Recommend an implementation order for the missing mitigations and justify it
   in risk terms.
5. Note one limitation of relying solely on the Essential Eight.

**Expected Output:**

A completed mapping table (mitigation → principle → objective), a gap assessment
for the scenario, and a justified implementation order. Learners can explain why
baselines are necessary but not sufficient.

**Reflection Questions:**

1. Why does the Essential Eight use a maturity model rather than a simple
   pass/fail?
2. Which mitigation would you prioritise for the scenario business, and why?
3. What kinds of threats does the Essential Eight not address well?

---

## Assessment

### Formative Assessment: Concepts & Principles Quiz

**Type:** Self-check quiz with answer key

**Description:** A quiz testing precise use of terminology — distinguishing
threat/vulnerability/risk, classifying controls by objective, and matching
principles to examples. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2, LO3

**Feedback mechanism:** Answer key with explanations and common-misconception
notes.

---

### Summative Assessment: Security Design Analysis

**Type:** Case-study analysis report

**Description:** Students are given a description of a small organisation's IT
environment and a recent (fictional but realistic) incident. They must (a)
identify which security objectives were violated, (b) produce a focused threat
model of the affected system, (c) recommend prioritised controls mapped to
defensive principles and the Essential Eight, and (d) explain the residual risk.
Deliverable: 1,500–2,000 word report with a diagram.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Objective-violation analysis | LO1, LO2 |
| Threat model of affected system | LO4 |
| Prioritised controls + Essential Eight mapping | LO3, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Conceptual accuracy | Precise, correct use of all core concepts | Mostly precise with minor slips | Several conceptual errors | Frequent misuse of core terms |
| Threat modelling | Thorough, well-structured, prioritised model | Solid model with minor gaps | Partial model; weak prioritisation | Little structured modelling |
| Control recommendations | Well-prioritised, justified, correctly mapped | Reasonable, mostly mapped | Generic recommendations, weak mapping | Unjustified or incorrect controls |
| Communication | Clear, structured, professional | Clear with minor lapses | Understandable but disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Examined directly in Topic 6 and Lab 2 as Australia's
  baseline control set, with each mitigation traced to a principle.
- **ACSC Annual Cyber Threat Report:** Grounds the threat-actor discussion in
  Topic 2 in the real Australian threat landscape.
- **ACSC Information Security Manual:** Referenced as the broader Australian
  control framework that the principles inform.

---

## Further Reading

**Anderson, R. (2020).** *Security Engineering (3rd ed.).* Wiley. https://www.cl.cam.ac.uk/~rja14/book.html
> Relevance: A freely available, authoritative treatment of security principles, cryptography, and access control underpinning this unit.

**Shostack, A. (2014).** *Threat Modeling: Designing for Security.* Wiley.
> Relevance: The standard reference for the STRIDE-based threat modelling practised in Lab 1.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au/about-us/reports-and-statistics
> Relevance: The authoritative source on the Australian threat landscape used in Topic 2 (Australian source).

**Australian Cyber Security Centre (2023).** *Essential Eight Maturity Model.* ACSC. https://www.cyber.gov.au/essential-eight
> Relevance: The Australian baseline control set mapped in Topic 6 and Lab 2 (Australian source).

**NIST (2020).** *SP 800-160 Vol. 1 — Systems Security Engineering.* NIST. https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final
> Relevance: Connects security principles to engineering practice, previewing the Security Engineering major.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F04 |
| Unit Title | Security Concepts & Principles |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01, F02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | None directly (ASD Essential Eight / ACSC ISM controls) |
