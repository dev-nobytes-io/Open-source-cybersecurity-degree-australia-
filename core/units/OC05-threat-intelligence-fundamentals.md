# OC05: Threat Intelligence Fundamentals

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Cyber threat intelligence (CTI) is the discipline of turning data about adversaries
into decisions defenders can act on. This unit teaches the CTI lifecycle —
direction, collection, processing, analysis, dissemination, and feedback — with
**Priority Intelligence Requirements (PIRs)** as the centre of gravity. PIRs are
the prioritised questions that drive everything an intelligence function does;
without them, collection is aimless and analysis is unfocused. The unit adopts the
**Red Hat Priority Intelligence Requirements process** (as referenced in the SANS
cyber-threat-intelligence body of knowledge) as its working method for defining,
structuring, and operationalising PIRs.

CTI is the engine of threat-informed defense: well-formed PIRs, answered through
analysis mapped to MITRE ATT&CK and CTID research, are exactly what tell a
SOC which detections, logs, infrastructure, and automation to change as the
adversary changes. In the Australian context, CTI consumes and contributes to
ACSC advisories and community sharing (MISP, ISACs). OC05 builds on OC01
(Adversary Tradecraft) and supports OC02, OC04, and the CTI, Threat Hunting, and
Detection Engineering majors.

---

## Prerequisites

- OC01 — Adversary Tradecraft & TTPs
- F06 — Data & Log Analysis

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** the cyber threat intelligence lifecycle and the role of each phase.
2. **Apply** the Priority Intelligence Requirements (PIR) process to define and
   structure prioritised intelligence requirements for an organisation.
3. **Differentiate** strategic, operational, and tactical intelligence and match
   each to its consumer.
4. **Apply** structured analytic techniques and models (Diamond Model, ATT&CK,
   the kill chain) to analyse adversary activity.
5. **Analyse** source reliability and analytic confidence, and disseminate
   finished intelligence appropriately.
6. **Examine** how PIR-driven CTI feeds the threat-informed defense loop and
   Australian community sharing.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of the CTI
lifecycle, intelligence requirements, analytic models, and dissemination.

**Skills (AQF 7.2):** Students develop analytical skills by defining PIRs,
applying structured analysis, and assessing confidence and source reliability.

**Application (AQF 7.3):** Students apply CTI methods to produce
requirement-driven, decision-useful intelligence in an Australian organisational
context.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Threat/Warning Analyst | AN-TWA-001 | T0707 | Analyse and report adversary activity against intelligence requirements | Lab 2 — Producing Finished Intelligence |
| NIST NICE DCWF | 2023 | All-Source Analyst | AN-ASA-001 | T0569 | Apply threat frameworks to develop and answer intelligence requirements | Lab 1 — Building Priority Intelligence Requirements |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Threat intelligence | THIN | Level 4 | Lab 1, Lab 2 |
| Information analysis | ANAL | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Threat Intelligence | Intelligence Production | Practitioner | Lab 1, Lab 2 |

---

## Topics

### Topic 1: The CTI Lifecycle

Intelligence is produced through a disciplined cycle: **direction** (what do we
need to know?), **collection**, **processing**, **analysis**, **dissemination**,
and **feedback**. This topic introduces each phase and stresses that the cycle is
iterative and driven from the direction phase — intelligence that does not answer
a decision-maker's question is noise.

**Key concepts:**
- The six phases of the intelligence cycle
- Direction as the driver of everything downstream
- Feedback making the cycle iterative

---

### Topic 2: Priority Intelligence Requirements (PIRs)

PIRs are the prioritised, decision-focused questions an intelligence function
exists to answer. This topic teaches the **Red Hat PIR process** (as referenced in
SANS CTI guidance): how to elicit requirements from stakeholders, write PIRs that
are specific, prioritised, and tied to a decision, decompose them into more
granular intelligence requirements and indicators, and use them to direct
collection and focus analysis. Strong PIRs are the difference between a CTI
function that drives defence and one that merely curates feeds.

**Key concepts:**
- What makes a good PIR: decision-linked, specific, prioritised
- Eliciting requirements from stakeholders
- Decomposing PIRs into intelligence requirements and collection tasking

**Australian context:** PIRs are framed to address the threats most relevant to
the organisation's Australian sector and the ACSC threat landscape.

---

### Topic 3: Levels of Intelligence and Their Consumers

Intelligence serves different audiences. This topic distinguishes **strategic**
(risk and trends for executives), **operational** (campaigns and actor behaviour
for defence planning), and **tactical** (indicators and TTPs for the SOC)
intelligence, and teaches matching the product, language, and cadence to each
consumer. It connects each level back to the PIRs it answers.

**Key concepts:**
- Strategic vs operational vs tactical intelligence
- Matching product and language to consumer
- Linking each level to its PIRs

---

### Topic 4: Analytic Models and Structured Analysis

Good analysis is structured to resist bias. This topic covers the core models —
the **Diamond Model** of intrusion analysis, the **cyber kill chain**, and
**MITRE ATT&CK** as the behavioural backbone — and structured analytic techniques
such as the Analysis of Competing Hypotheses. CTID resources (Attack Flow, actor
technique profiles) support modelling adversary campaigns.

**Key concepts:**
- Diamond Model and kill chain
- ATT&CK for actor/campaign behavioural analysis
- Structured analytic techniques to counter bias

---

### Topic 5: Source Evaluation, Confidence, and Dissemination

Intelligence must carry honest caveats. This topic covers grading source
reliability and information credibility (admiralty-style), expressing analytic
confidence and estimative language, and disseminating finished intelligence in the
right format — including structured, machine-readable sharing via **STIX/TAXII**
and platforms such as **MISP** and **OpenCTI**.

**Key concepts:**
- Source reliability and information credibility grading
- Analytic confidence and estimative language
- Dissemination: written products and STIX/TAXII/MISP

---

### Topic 6: PIR-Driven CTI in the Threat-Informed Defense Loop

This topic closes the loop. PIR-driven intelligence is what tells the rest of the
operational core what to change: answered PIRs yield prioritised TTPs that update
detections (OC02), inform IR (OC04), and shape hunting and emulation. As the
adversary evolves, PIRs are revisited and the cycle re-runs — making CTI the
steering function of a living, threat-informed defence. It also covers
contributing back to Australian community sharing.

**Key concepts:**
- From answered PIRs to detection, logging, and automation changes
- Revisiting PIRs as the threat landscape shifts
- Contributing to ACSC/community sharing

**Australian context:** Positions the organisation as both consumer and
contributor in the Australian sharing ecosystem.

---

## Labs & Exercises

### Lab 1: Building Priority Intelligence Requirements

**Objective:** Apply the Red Hat PIR process to build a prioritised, decision-linked
PIR set for a scenario organisation and decompose it into collection tasking.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: any (analysis lab)
- Tools: a document/spreadsheet, ATT&CK Navigator, ACSC threat reporting (free)
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario organisation (e.g. an Australian health-sector provider) and
   identify its key decisions and assets at risk.
2. Using the Red Hat PIR process, draft 3–5 PIRs, each tied to a specific decision
   and prioritised.
3. Decompose each PIR into more granular intelligence requirements and the
   indicators/data that would answer them.
4. Map the relevant adversary techniques (from ACSC reporting + ATT&CK) to each
   PIR in a Navigator layer.
5. Define collection tasking for each requirement (what sources, internal and
   external).
6. State how each PIR's answer would change a defensive decision.

**Expected Output:**

A prioritised PIR set tied to decisions, decomposed into requirements and
collection tasking, with an ATT&CK layer. Learners can explain why each PIR
matters to this organisation.

**Reflection Questions:**

1. How did tying PIRs to decisions change what you chose to prioritise?
2. Which PIR would be hardest to collect against, and how would you task around
   that?
3. How would these PIRs differ for an organisation in a different Australian
   sector?

---

### Lab 2: Producing Finished Intelligence

**Objective:** Analyse adversary activity against a PIR and produce a finished,
appropriately-caveated intelligence product with structured indicators.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: any (MISP/OpenCTI optionally in a local VM)
- Tools: ATT&CK, Diamond Model template, a MISP or OpenCTI instance (free/OSS,
  optional), a report template
- Minimum hardware: trivial for analysis; 6 GB RAM / 2 vCPU if running MISP/
  OpenCTI locally (within spec; no GPU)

**Instructions:**

1. Select one PIR from Lab 1 and a provided dataset of reporting/indicators
   relevant to it.
2. Analyse the activity using the Diamond Model and map TTPs to ATT&CK.
3. Apply a structured technique (e.g. competing hypotheses) to reach an assessment.
4. Grade source reliability and state analytic confidence using estimative
   language.
5. Produce a finished product appropriate to a chosen consumer level (strategic/
   operational/tactical) that answers the PIR.
6. Express the tactical indicators in a structured format (STIX/MISP) suitable for
   sharing.

**Expected Output:**

A finished intelligence product that explicitly answers the PIR, with Diamond/
ATT&CK analysis, graded sources, a confidence statement, and structured shareable
indicators. Learners can trace the product back to the PIR it serves.

**Reflection Questions:**

1. How did the consumer level change the language and content of your product?
2. How confident were you, and what would raise or lower that confidence?
3. How would the tactical indicators feed the detections in OC02 — and what would
   you contribute to Australian community sharing?

---

## Assessment

### Formative Assessment: PIR Quality Critique

**Type:** Self/peer review exercise with answer key

**Description:** Students are given a set of draft PIRs of varying quality and must
critique each against the Red Hat PIR criteria (decision-linked, specific,
prioritised, collectable) and rewrite the weakest. Self-marked.

**Learning Outcomes Assessed:** LO2

**Feedback mechanism:** Answer key with a model critique and rewrite for each PIR.

---

### Summative Assessment: Intelligence Requirements & Finished Product

**Type:** Analytical report

**Description:** For an assigned Australian-context organisation, students (a) build
a prioritised PIR set using the Red Hat PIR process, (b) select one PIR and produce
a finished intelligence product analysed with the Diamond Model and ATT&CK, (c)
grade sources and state confidence, and (d) explain how the answered PIR updates
the organisation's threat-informed defence and what is contributed to community
sharing. Deliverable: 2,000–2,500 word report with PIR set, Navigator layer, and
structured indicators.

**Learning Outcomes Assessed:** LO1, LO2, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Prioritised PIR set | LO1, LO2 |
| Finished product with Diamond/ATT&CK analysis | LO4 |
| Source grading & confidence | LO5 |
| TID-loop & sharing discussion | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| PIR quality | PIRs are decision-linked, specific, prioritised, collectable | Mostly strong PIRs | PIRs vague or weakly prioritised | PIRs not decision-linked |
| Analytic rigour | Strong model use; bias-resistant; well-reasoned | Sound analysis | Partial or shallow analysis | Little structured analysis |
| Confidence & sourcing | Honest, well-justified grading and confidence | Adequate grading and confidence | Superficial caveats | Missing or misleading caveats |
| Decision usefulness | Product clearly answers the PIR and drives a decision | Product answers the PIR | Product loosely tied to PIR | Product does not answer a PIR |
| Communication | Clear, consumer-appropriate, professional | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC threat reporting & advisories:** Used as collection sources and to ground
  PIRs in the Australian threat landscape.
- **Australian community sharing (MISP / ISACs / ACSC partnerships):** Framed as
  the destination for contributed intelligence.
- **Sector relevance:** PIR labs use Australian-sector scenarios (e.g. health,
  critical infrastructure) so requirements reflect real local risk.

---

## Further Reading

**Red Hat (2023).** *Priority Intelligence Requirements (PIR) process.* Red Hat Product Security / threat intelligence guidance.
> Relevance: The working PIR method adopted in Topic 2 and Lab 1, as referenced in the SANS CTI body of knowledge (confirm exact SANS guide citation at review).

**SANS (2024).** *FOR578 Cyber Threat Intelligence & CTI white papers.* SANS Institute. https://www.sans.org/cyber-security-courses/cyber-threat-intelligence/
> Relevance: The CTI body of knowledge that references the PIR process and underpins the lifecycle taught here.

**Caltagirone, S., Pendergast, A. & Betz, C. (2013).** *The Diamond Model of Intrusion Analysis.* https://www.activeresponse.org/the-diamond-model/
> Relevance: The intrusion-analysis model applied in Topic 4 and Lab 2; freely available.

**MITRE ATT&CK & CTID (v19, 2026).** *ATT&CK, Attack Flow, actor profiles.* https://attack.mitre.org / https://github.com/center-for-threat-informed-defense
> Relevance: The behavioural backbone and campaign-modelling tooling for CTI analysis.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report & advisories.* ACSC. https://www.cyber.gov.au
> Relevance: The primary Australian collection source and the model for contributing intelligence (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | OC05 |
| Unit Title | Threat Intelligence Fundamentals |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Operational Core |
| Major / Pathway | Operational |
| Prerequisites | OC01, F06 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | None directly (ACSC threat reporting context) |
