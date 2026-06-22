# CT01: Intelligence Tradecraft

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit establishes the tradecraft that separates cyber threat intelligence (CTI)
from mere data collection: the intelligence cycle, **Priority Intelligence
Requirements (PIRs)**, source and collection management, analytic rigour, and the
operational security (OPSEC) that protects an intelligence function. It deepens the
CTI foundations from OC05 to analyst/evaluator level, treating intelligence as a
requirements-driven discipline whose purpose is to answer a decision-maker's
question — not to accumulate indicators.

CTI is the steering function of threat-informed defense: well-formed PIRs direct
collection and analysis, and finished intelligence tells hunting, detection, and
leadership what to do. In the Australian context, the ASD *Annual Cyber Threat
Report* is a primary source for shaping PIRs against the real local threat
landscape. CT01 builds on OC05 (Threat Intelligence Fundamentals) and sets the
foundation for CT02–CT06.

---

## Prerequisites

- OC05 — Threat Intelligence Fundamentals
- OC01 — Adversary Tradecraft & TTPs

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** a decision-maker's needs to derive Priority Intelligence
   Requirements using a structured process.
2. **Apply** the intelligence cycle (direction → collection → processing →
   analysis → dissemination → feedback) to a scenario.
3. **Evaluate** sources for reliability and information for credibility.
4. **Apply** structured analytic techniques to reduce cognitive bias.
5. **Analyse** the OPSEC requirements of an intelligence function.
6. **Recommend** a collection plan that satisfies a set of PIRs.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of intelligence
tradecraft, requirements, and analytic methodology.

**Skills (AQF 7.2):** Students develop high-order analytical skills by deriving
requirements, evaluating sources, and applying structured techniques.

**Application (AQF 7.3):** Students apply tradecraft to design requirement-driven
collection for realistic Australian organisations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Threat/Warning Analyst (621) | AN-TWA-001 | T0707 | Develop and answer intelligence requirements through analysis | Lab 1 — Writing Priority Intelligence Requirements |
| NIST NICE DCWF | 2023 | All-Source Analyst (611) | AN-ASA-001 | T0569 | Apply analytic frameworks and the intelligence cycle | Lab 2 — Intelligence Cycle & Collection Plan |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 4–5 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Threat Intelligence | Intelligence Production | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: What Intelligence Is

This topic distinguishes intelligence (analysed, requirement-driven, decision-
supporting) from information and data. It introduces the intelligence levels
(technical, operational, strategic) and the principle that intelligence must answer
a question someone needs answered.

**Key concepts:**
- Data vs information vs intelligence
- The three intelligence levels and their consumers
- Requirement-driven production

---

### Topic 2: Priority Intelligence Requirements

PIRs are the prioritised, decision-linked questions that drive everything. This
topic deepens OC05's treatment: eliciting requirements from stakeholders, writing
specific and prioritised PIRs, and decomposing them into intelligence requirements
and indicators that direct collection.

**Key concepts:**
- Decision-linked, specific, prioritised PIRs
- Eliciting requirements from stakeholders
- Decomposition into collection tasking

**Australian context:** The ASD Annual Cyber Threat Report informs PIRs grounded in
the Australian threat landscape.

---

### Topic 3: The Intelligence Cycle

This topic covers the full cycle — direction, collection, processing, analysis,
dissemination, feedback — as an iterative, requirements-driven loop, and the common
failure modes (collection without direction, analysis without dissemination).

**Key concepts:**
- The six phases and their interdependence
- Iteration and feedback
- Common failure modes

---

### Topic 4: Source Evaluation and Collection Management

This topic teaches managing sources and collection: the disciplines (OSINT, technical,
human-reporting), grading source reliability and information credibility
(admiralty-style), and building a collection plan that maps sources to requirements
while avoiding over-collection.

**Key concepts:**
- Collection disciplines and source types
- Source reliability and information credibility grading
- Collection planning against requirements

---

### Topic 5: Structured Analytic Techniques

Analysis must resist bias. This topic covers cognitive biases in intelligence and
structured analytic techniques — Analysis of Competing Hypotheses, key assumptions
check, and the use of estimative language and confidence levels.

**Key concepts:**
- Cognitive biases in analysis
- Analysis of Competing Hypotheses; key assumptions check
- Estimative language and confidence

---

### Topic 6: OPSEC for Intelligence Operations

Intelligence work can expose the analyst and the organisation. This topic covers
OPSEC: safe research/attribution practices, managed-attribution and sock-puppet
considerations, protecting sources and methods, and the legal/ethical boundaries of
collection (linking to F05).

**Key concepts:**
- Research OPSEC and managed attribution
- Protecting sources and methods
- Legal/ethical collection boundaries

**Australian context:** Collection must respect the Cybercrime Act 2001 and Privacy
Act boundaries established in F05.

---

## Labs & Exercises

### Lab 1: Writing Priority Intelligence Requirements

**Objective:** Derive and decompose PIRs for a fictional Australian organisation
facing a defined threat.

**Prerequisites:**
- Topics 1–2

**Environment:**
- Operating System: any (analysis lab)
- Tools: a PIR/collection template, the ASD Annual Cyber Threat Report (free)
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take the scenario: a fictional Australian utility facing ransomware groups.
2. Identify the key decisions the organisation's leaders must make.
3. Write three PIRs, each decision-linked, specific, and prioritised.
4. Decompose each PIR into intelligence requirements and indicators.
5. Identify the source types that would answer each requirement.
6. State how each PIR's answer would change a defensive decision.

**Expected Output:**

Three decision-linked PIRs decomposed into requirements and indicators, with source
types. Learners can explain why each PIR matters to this organisation's decisions.

**Reflection Questions:**

1. How did tying PIRs to decisions change what you prioritised?
2. Which PIR is hardest to collect against, and how would you adapt?
3. How does the ASD threat report shape PIRs for an Australian utility?

---

### Lab 2: Intelligence Cycle & Collection Plan

**Objective:** Map a scenario through the intelligence cycle and produce a
collection plan.

**Prerequisites:**
- Topics 3–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: an intelligence-cycle/collection template
- Minimum hardware: trivial

**Instructions:**

1. Take the PIRs from Lab 1 and walk them through each phase of the cycle.
2. Build a collection plan mapping sources to requirements, graded for reliability.
3. Note processing/analysis steps and a dissemination approach per consumer level.
4. Identify the OPSEC precautions needed for the collection.
5. Apply a structured technique (e.g. key assumptions check) to one requirement.
6. Define the feedback mechanism that would refine the PIRs.

**Expected Output:**

A cycle walkthrough, a graded collection plan, OPSEC precautions, and a feedback
mechanism. Learners can justify the source-to-requirement mapping and OPSEC choices.

**Reflection Questions:**

1. Where is your plan most likely to fail, and how would feedback catch it?
2. Which OPSEC precaution is most important for this collection, and why?
3. How did the structured technique change your view of a requirement?

---

## Assessment

### Formative Assessment: PIR & Source-Grading Drill

**Type:** Self/peer review exercise with answer key

**Description:** Students critique draft PIRs against the quality criteria and grade
a set of sources for reliability/credibility, rewriting the weakest. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with model PIRs and source gradings.

---

### Summative Assessment: Intelligence Requirements & Collection Plan

**Type:** Analytical report

**Description:** For an assigned Australian organisation and threat context, students
(a) derive a prioritised PIR set, (b) walk it through the intelligence cycle, (c)
produce a graded collection plan, (d) specify OPSEC precautions, and (e) apply a
structured analytic technique and state how feedback will refine the requirements.
Deliverable: 2,500–3,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Prioritised PIRs | LO1 |
| Intelligence-cycle walkthrough | LO2 |
| Graded collection plan | LO3, LO6 |
| Structured technique & OPSEC | LO4, LO5 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| PIR quality | Decision-linked, specific, prioritised | Mostly strong | Vague | Not decision-linked |
| Cycle & collection | Coherent, requirement-driven plan | Sound | Partial | Weak |
| Source evaluation | Rigorous, justified grading | Adequate | Superficial | Poor |
| Analytic rigour & OPSEC | Bias-aware; sound OPSEC | Reasonable | Thin | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Annual Cyber Threat Report:** Primary source for grounding PIRs in the
  Australian threat landscape.
- **Cybercrime Act 2001 & Privacy Act 1988:** Legal boundaries on collection (OPSEC
  topic), reinforcing F05.
- **Australian sector scenarios:** PIR labs use Australian-sector contexts (e.g.
  utilities/critical infrastructure).

---

## Further Reading

**Red Hat (2023).** *Priority Intelligence Requirements (PIR) process.* Red Hat threat-intelligence guidance.
> Relevance: The PIR method deepened from OC05; as referenced in the SANS CTI body of knowledge (confirm exact SANS citation at review).

**SANS (2024).** *FOR578 Cyber Threat Intelligence & CTI white papers.* SANS Institute. https://www.sans.org/cyber-security-courses/cyber-threat-intelligence/
> Relevance: The CTI body of knowledge underpinning the tradecraft in this unit.

**Heuer, R. (1999).** *Psychology of Intelligence Analysis.* CIA Center for the Study of Intelligence.
> Relevance: The foundational text on cognitive bias and structured analysis (Topic 5); freely available.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au/about-us/reports-and-statistics
> Relevance: The Australian threat-landscape source for PIR development (Australian source).

**US Government (2009).** *A Tradecraft Primer: Structured Analytic Techniques.* (Publicly available.)
> Relevance: Practical structured analytic techniques applied in Topic 5 and the labs.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CT01 |
| Unit Title | Intelligence Tradecraft |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | CTI |
| Prerequisites | OC05, OC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Cybercrime Act 2001; Privacy Act 1988 (contextual) |
