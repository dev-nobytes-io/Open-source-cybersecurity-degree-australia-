# CT06: Capstone — Intelligence Product

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

The CTI capstone integrates the entire major into the production of a single
finished intelligence product, taken from a Priority Intelligence Requirement
through collection, processing, structured analysis, and dissemination. Students
define a PIR for a named (fictional or anonymised) Australian organisation, build
and execute a collection plan across multiple source types, analyse using the
Diamond Model or another structured methodology, produce a finished product at the
appropriate level, represent the threat in STIX 2.1, and document dissemination —
delivering a portfolio-grade artefact suitable for employer review.

The capstone exercises the full intelligence cycle that the major teaches and the
threat-informed-defense thesis of the degree: requirement-driven intelligence that
changes a decision. It is assessed at the highest cognitive levels — students
**create** finished intelligence and **evaluate** its sufficiency against the PIR.
CT06 requires CT01–CT05 and the operational core, especially OC05.

---

## Prerequisites

- CT01 — Intelligence Tradecraft
- CT02 — Threat Actor Research & Profiling
- CT03 — Technical Intelligence
- CT04 — Strategic Intelligence
- CT05 — CTI Platforms & Sharing

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** a PIR and collection plan for a defined Australian organisation.
2. **Evaluate** and process multi-source collection into assessed findings.
3. **Create** a finished intelligence product using a structured methodology.
4. **Create** a STIX 2.1 representation of the threat and a dissemination plan.
5. **Evaluate** the product's sufficiency against the originating PIR.
6. **Recommend** decisions or actions the intelligence supports, with appropriate
   confidence and caveats.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** The capstone consolidates specialised CTI knowledge into an
integrated, requirement-driven product.

**Skills (AQF 7.2):** Students demonstrate the highest-order skills — designing,
creating, and evaluating finished intelligence independently.

**Application (AQF 7.3):** Students apply the full intelligence cycle for an
Australian organisation and produce an employer-grade deliverable.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | All-Source Analyst (611) | AN-ASA-001 | T0751 | Produce finished all-source intelligence answering a requirement | Lab 1 — Collection & Analysis |
| NIST NICE DCWF | 2023 | Threat/Warning Analyst (621) | AN-TWA-001 | T0710 | Disseminate finished intelligence to consumers | Lab 2 — Finished Product & Dissemination |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 5 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Threat Intelligence | Intelligence Production | Advanced | Lab 1, Lab 2 |

---

## Topics

> The capstone is a supervised, integrative project. These "topics" are the
> production phases and guidance; the substantive work is the student's own
> intelligence product.

### Topic 1: Capstone Scope and the PIR

This phase defines the named Australian organisation, the decision context, the
PIR, deliverables, and success criteria, agreed with the supervisor.

**Key concepts:**
- Organisation, decision context, and PIR
- Deliverables and success criteria
- The intelligence level required

---

### Topic 2: Collection Planning and Execution

Students build and execute a collection plan against the PIR, drawing on at least
three distinct source types, with OPSEC and source grading.

**Key concepts:**
- Collection plan against the PIR
- Multiple source types and grading
- Collection OPSEC

---

### Topic 3: Processing and Structured Analysis

Students process collection into assessed findings using a structured methodology
(Diamond Model and/or competing hypotheses), with confidence and caveats.

**Key concepts:**
- Processing collection into findings
- Structured analysis and bias control
- Confidence and caveats

---

### Topic 4: Producing the Finished Product

Students write the finished intelligence product at the appropriate level
(technical/operational/strategic), consumer-tailored, with clear bottom-line-up-front
and sourcing.

**Key concepts:**
- Finished-product structure and BLUF
- Consumer-appropriate level and language
- Sourcing and confidence

---

### Topic 5: Structured Representation and Dissemination

Students represent the threat in STIX 2.1 and document a dissemination plan (who,
how, at what TLP, through which channel/platform), enabling onward use.

**Key concepts:**
- STIX 2.1 representation of the product
- Dissemination plan and TLP
- Enabling onward, machine-actionable use

**Australian context:** Dissemination considers ACSC/TISN sharing where relevant.

---

### Topic 6: Evaluation and Decision Support

Students evaluate whether the product answers the PIR, state the decisions it
supports, and reflect on gaps and next collection — closing the cycle.

**Key concepts:**
- Sufficiency against the PIR
- Decisions supported
- Gaps and the next iteration

---

## Labs & Exercises

### Lab 1: Collection & Analysis

**Objective:** Execute the collection plan and produce assessed findings against the
PIR.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: any for analysis; a CTI platform (MISP/OpenCTI) optional
- Tools: the major's free toolset — ATT&CK Navigator, VirusTotal/Shodan free,
  Maltego CE, Python `stix2`, MISP/OpenCTI — all free/free-tier
- Minimum hardware: within the 8 GB / 4-core / 50 GB spec; run platforms
  single-node; no GPU

**Instructions:**

1. Confirm the PIR, scope, and success criteria with your supervisor.
2. Build and execute the collection plan across ≥3 source types, with grading and
   OPSEC.
3. Process the collection into assessed findings.
4. Apply a structured methodology (Diamond Model and/or ACH) with confidence.
5. Map relevant techniques to ATT&CK (v19).
6. Record the evidence and sourcing supporting each finding.

**Expected Output:**

A documented collection effort across ≥3 source types and assessed, structured
findings with confidence and sourcing, mapped to ATT&CK. The analysis is traceable
to the PIR.

**Reflection Questions:**

1. Which source type was most valuable for this PIR, and which underdelivered?
2. Where did structured analysis change your assessment?
3. What collection gap remains, and how would you close it?

---

### Lab 2: Finished Product & Dissemination

**Objective:** Produce the finished intelligence product, its STIX representation,
and a dissemination plan; evaluate against the PIR.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: a report template, Python `stix2`, `templates/student-portfolio/index.html`
  — all free
- Minimum hardware: trivial

**Instructions:**

1. Write the finished product at the appropriate level with BLUF and sourcing.
2. Produce a valid STIX 2.1 representation of the threat actor/threat.
3. Document a dissemination plan (consumers, channel, TLP).
4. Evaluate whether the product answers the PIR and state the decisions it supports.
5. Note gaps and the next collection iteration.
6. Package a portfolio artefact and submit for community practitioner review.

**Expected Output:**

A finished intelligence product, a valid STIX 2.1 representation, a dissemination
plan, a sufficiency evaluation against the PIR, and a portfolio artefact suitable
for employer review.

**Reflection Questions:**

1. Does the product actually answer the PIR — and how do you know?
2. How did you pitch the level/language to the intended consumer?
3. If you re-ran this, what collection or analysis would you change?

---

## Assessment

### Formative Assessment: PIR & Plan Gate

**Type:** Supervisor/peer review of the PIR and collection plan

**Description:** Before collection, the PIR, scope, and collection plan are reviewed
for feasibility and decision-linkage; students revise. A go/no-go gate into the
capstone.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Structured feedback against a plan rubric; revision required.

---

### Summative Assessment: Finished Intelligence Product

**Type:** End-to-end intelligence product with STIX, dissemination, and portfolio
artefact

**Description:** The complete product: a defined PIR, a documented collection plan,
multi-source collection and structured analysis, a finished product at the
appropriate level, a STIX 2.1 representation, a dissemination plan, a sufficiency
evaluation against the PIR, and a portfolio artefact — subject to community
practitioner review. Deliverable: full product package (report ~4,000–5,000 words
plus STIX and dissemination artefacts).

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| PIR & collection plan | LO1, LO2 |
| Structured analysis | LO3 |
| Finished product & STIX | LO4 |
| Dissemination & evaluation | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Requirement-driven design | PIR clearly drives the whole product | Sound linkage | Partial | Weak |
| Collection & analysis | Rigorous, multi-source, structured | Solid | Partial | Weak |
| Finished product | Employer-grade, consumer-pitched, sourced | Professional | Mixed | Poor |
| STIX & dissemination | Valid STIX; sound dissemination/TLP | Adequate | Superficial | Poor |
| Evaluation | Honest sufficiency assessment & next steps | Reasonable | Thin | Absent |

---

## Australian Context

This unit incorporates the following Australian context:

- **Named Australian organisation scenario:** The PIR and product target an
  Australian (fictional/anonymised) organisation.
- **ASD Annual Cyber Threat Report & ACSC advisories:** Collection sources.
- **ACSC/TISN sharing:** Considered in the dissemination plan.

---

## Further Reading

**SANS (2024).** *FOR578 CTI & finished-intelligence writing guidance.* SANS Institute. https://www.sans.org/cyber-security-courses/cyber-threat-intelligence/
> Relevance: Practitioner guidance on producing finished intelligence for the capstone.

**Caltagirone, S., Pendergast, A. & Betz, C. (2013).** *The Diamond Model of Intrusion Analysis.* https://www.activeresponse.org/the-diamond-model/
> Relevance: The structured methodology applied in the capstone analysis.

**OASIS (2021).** *STIX 2.1 Specification.* OASIS. https://oasis-open.github.io/cti-documentation/
> Relevance: The standard for the capstone's structured threat representation.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report & advisories.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian collection sources grounding the capstone (Australian source).

**Templates — Student Portfolio.** `templates/student-portfolio/index.html` (this repository).
> Relevance: The portfolio artefact format the capstone deliverable must populate (Australian-context degree resource).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CT06 |
| Unit Title | Capstone — Intelligence Product |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 24 CP |
| Degree Layer | Capstone |
| Major / Pathway | CTI |
| Prerequisites | CT01, CT02, CT03, CT04, CT05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 5–6 (Evaluate, Create) |
| Australian Legislation Referenced | None directly (ACSC reporting / TISN sharing context) |
