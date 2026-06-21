# DF05: Incident Response Operations

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit turns forensic capability into operational response. Students learn to
execute the full **PICERL** lifecycle under pressure: triaging an alert, scoping
with the forensic skills from DF02–DF04, making containment and eradication
decisions, recovering safely, communicating with stakeholders, and meeting
Australia's mandatory notification obligations. It covers case management (TheHive),
decision logging, and the post-incident report — the deliverable that turns an
incident into organisational learning.

DF05 is where the Australian legal obligations become operational timelines: the
NDB scheme (OAIC), APRA CPS 234 notification, ASD/ACSC reporting, and SOCI
obligations all run in parallel with the technical response. Australian breaches —
Optus, Medibank, Latitude — are used as case studies in how response and
communication succeed or fail. DF05 builds on DF01–DF04 and OC04, and precedes the
capstone DF06.

---

## Prerequisites

- DF02 — Host Forensics
- DF03 — Memory Forensics
- DF04 — Network Forensics

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the full PICERL lifecycle to a simulated incident under realistic
   constraints.
2. **Evaluate** containment, eradication, and recovery options and justify
   decisions.
3. **Analyse** the Australian notification obligations triggered by an incident and
   their timelines.
4. **Apply** case-management and decision-logging practices during response.
5. **Recommend** stakeholder communications appropriate to executives, regulators,
   and customers.
6. **Create** a post-incident report with technical findings, timeline, and lessons
   learned.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of incident-
response operations, decision-making, and Australian notification obligations.

**Skills (AQF 7.2):** Students develop judgement and communication skills by making
response decisions and reporting to varied audiences.

**Application (AQF 7.3):** Students apply IR operations to realistic Australian
incidents, meeting legal obligations and producing professional deliverables.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Incident Responder | PR-CIR-001 | T0041 | Coordinate and perform incident handling across the lifecycle | Lab 1 — Full PICERL Execution |
| NIST NICE DCWF | 2023 | Cyber Crime Investigator | IN-INV-001 | T0103 | Apply legal/notification requirements during response | Lab 2 — Notification & Post-Incident Report |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Incident management | USUP | Level 4–5 | Lab 1 |
| Systems & software assurance | SURE | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Incident Management | Incident Response | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Executing the PICERL Lifecycle

This topic operationalises PICERL/NIST SP 800-61: from alert triage and validation,
through scoping (using DF02–DF04 forensics), to the decision and recovery phases —
under time pressure and incomplete information.

**Key concepts:**
- Triage, validation, and severity
- Scoping with forensic evidence
- Operating under pressure and uncertainty

---

### Topic 2: Containment, Eradication, and Recovery Decisions

This topic teaches the hard decisions: short- vs long-term containment, the
observe-vs-isolate trade-off, eradicating persistence and access, and recovering
safely with verification — aligning each decision to business impact.

**Key concepts:**
- Containment strategies and trade-offs
- Eradicating persistence/access
- Verified recovery and avoiding reinfection

---

### Topic 3: Australian Notification Obligations

This topic details the obligations and timelines: NDB eligible-breach assessment
and notification to the OAIC and individuals; APRA CPS 234 notification (within 72
hours for regulated entities); ASD/ACSC reporting; and SOCI mandatory reporting for
critical infrastructure.

**Key concepts:**
- NDB assessment and notification (OAIC)
- APRA CPS 234 72-hour notification
- ASD/ACSC and SOCI reporting

**Australian context:** This topic is the Australian notification regime in
operational practice.

---

### Topic 4: Case Management and Decision Logging

This topic teaches running an incident as a managed case (TheHive): tracking tasks,
evidence, and observables; maintaining a decision log that records what was decided,
when, by whom, and why — essential for both coordination and later review/legal
defensibility.

**Key concepts:**
- Case management with TheHive
- Decision logs and their evidentiary value
- Coordinating multi-responder incidents

---

### Topic 5: Stakeholder Communication During Incidents

This topic covers communicating in a crisis: executive/board updates, customer and
public messaging, and regulator notifications — tailoring tone, content, accuracy,
and timing per audience, with legal sign-off. It links to SC06 and OC04.

**Key concepts:**
- Audience-appropriate crisis communication
- Accuracy, timing, and legal review
- Consistency across audiences

**Australian context:** Australian breach cases (Optus, Medibank, Latitude)
illustrate communication done well and badly.

---

### Topic 6: Post-Incident Reporting and Lessons Learned

This topic teaches the post-incident report: executive summary, technical findings,
reconstructed timeline, root cause, and prioritised lessons-learned — including a
blameless review that converts findings into detection, logging, and control
improvements (closing the loop to OC02).

**Key concepts:**
- Post-incident report structure
- Root-cause and blameless lessons-learned
- Findings → durable improvements

**Australian context:** Lessons feed both internal defence and ACSC information
sharing.

---

## Labs & Exercises

### Lab 1: Full PICERL Execution

**Objective:** Execute the full PICERL cycle on a simulated compromised host,
documenting decisions in a managed case.

**Prerequisites:**
- Topics 1, 2, and 4

**Environment:**
- Operating System: a simulated incident environment (provided VM/dataset) +
  TheHive
- Tools: TheHive (case management), the DF02–DF04 forensic toolset, a decision-log
  template — all free/OSS
- Minimum hardware: run components sequentially — 6 GB RAM / 2 vCPU / 40 GB disk
  (within the 8 GB / 4-core / 50 GB spec; no GPU)

**Instructions:**

1. Open a case in TheHive from the provided alert; triage and set severity.
2. Scope the incident using forensic evidence (host/memory/network) and record
   findings as observables.
3. Decide and justify a containment strategy; log the decision.
4. Plan eradication (removing persistence/access) and verified recovery.
5. Maintain a decision log throughout (what, when, who, why).
6. Map the response to PICERL phases.

**Expected Output:**

A managed case with a complete decision log, a PICERL-mapped response, and
justified containment/eradication/recovery decisions. Learners can defend each
major decision under questioning.

**Reflection Questions:**

1. Where did the observe-vs-isolate trade-off bite, and how did you resolve it?
2. How did the decision log protect you and the organisation later?
3. Which forensic finding most changed your response decisions?

---

### Lab 2: Notification & Post-Incident Report

**Objective:** Determine notification obligations and produce a professional
post-incident report.

**Prerequisites:**
- Topics 3, 5, and 6 and Lab 1

**Environment:**
- Operating System: any
- Tools: a report template, OAIC/APRA/ACSC/SOCI references (free)
- Minimum hardware: trivial

**Instructions:**

1. From the Lab 1 incident, assess NDB eligibility and "serious harm" likelihood.
2. Determine APRA CPS 234 (if regulated) and SOCI (if critical infrastructure)
   obligations and timeframes; note ASD/ACSC reporting.
3. Draft the regulator and individual notifications meeting required content.
4. Draft executive and customer communications.
5. Write a post-incident report: executive summary, technical findings, timeline,
   root cause, and lessons learned.
6. List prioritised improvements (detections/logging/controls) from the lessons.

**Expected Output:**

A notification determination with timelines, drafted communications, and a complete
post-incident report with a lessons-learned improvement plan. Learners can justify
each notification decision against the criteria.

**Reflection Questions:**

1. Which obligation had the tightest deadline, and how did it shape the response?
2. How did your executive and customer messages differ while staying consistent?
3. Which lesson-learned improvement most reduces recurrence risk?

---

## Assessment

### Formative Assessment: Decision & Notification Drill

**Type:** Scenario exercise with answer key

**Description:** Given incident injects, students state the PICERL phase, the right
next action, and any triggered Australian notification. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with the model action and obligation per inject.

---

### Summative Assessment: Incident Response Operation & Report

**Type:** Practical report

**Description:** From a simulated incident, students (a) execute and document a full
PICERL response in a managed case, (b) make and justify containment/eradication/
recovery decisions, (c) determine and draft all Australian notifications, and (d)
produce a professional post-incident report with a lessons-learned improvement plan.
Deliverable: 3,000–3,500 word report plus case/decision-log artefacts.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| PICERL execution & case management | LO1, LO4 |
| Containment/eradication/recovery decisions | LO2 |
| Notification determination & comms | LO3, LO5 |
| Post-incident report & lessons | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Lifecycle execution | Decisive, well-justified, documented | Sound | Partial | Weak |
| Decision quality | Strong trade-off reasoning | Reasonable | Superficial | Poor |
| Notification accuracy | Correct, well-reasoned, timely | Mostly correct | Partial | Incorrect |
| Communication | Audience-appropriate, accurate, consistent | Clear | Inconsistent | Unclear |
| Report & lessons | Professional report; actionable lessons | Solid | Thin | Poor |

---

## Australian Context

This unit incorporates the following Australian context:

- **NDB scheme (OAIC):** Eligible-breach assessment and notification practised in
  Lab 2.
- **APRA CPS 234:** 72-hour notification for regulated entities.
- **SOCI Act 2018 & ASD/ACSC:** Critical-infrastructure and voluntary reporting.
- **Australian breach case studies:** Optus, Medibank, Latitude for response and
  communication lessons.

---

## Further Reading

**NIST (2012).** *SP 800-61 Rev. 2 — Computer Security Incident Handling Guide.* NIST. https://csrc.nist.gov/pubs/sp/800/61
> Relevance: The incident-handling lifecycle executed in this unit.

**Office of the Australian Information Commissioner (2024).** *Data breach preparation and response.* OAIC. https://www.oaic.gov.au
> Relevance: The authoritative source for NDB assessment and notification (Australian source).

**APRA (2019).** *Prudential Standard CPS 234 Information Security.* APRA. https://www.apra.gov.au
> Relevance: The 72-hour notification obligation for regulated entities (Australian source).

**StrangeBee (2024).** *TheHive Documentation.* https://docs.strangebee.com
> Relevance: The free case-management platform used in Lab 1.

**Australian Cyber Security Centre (2024).** *Cyber incident response & SOCI reporting guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian guidance on response and mandatory reporting (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DF05 |
| Unit Title | Incident Response Operations |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | DFIR |
| Prerequisites | DF02, DF03, DF04 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Privacy Act 1988 (NDB); APRA CPS 234; Security of Critical Infrastructure Act 2018 |
