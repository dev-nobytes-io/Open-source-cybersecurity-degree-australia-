# DF06: Capstone — IR Simulation

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

The DFIR capstone integrates the entire major into a single end-to-end incident
response on a simulated compromised network. Students take an incident from initial
detection and triage, through forensically sound evidence collection, host, memory,
and network forensics, full PICERL execution, mandatory Australian notification
assessment, and a professional post-incident report — producing a portfolio-grade
deliverable suitable for employer review. It is assessed at the highest cognitive
levels: students **design** and **create** a complete response and **evaluate** its
outcomes.

The capstone exercises the major's defining strength — DFIR under real Australian
legal obligations. Evidence is handled to the *Evidence Act 1995* standard; the
notification assessment spans NDB, APRA, ASD/ACSC, and SOCI; and the scenario draws
on the kind of incidents seen in major Australian breaches. DF06 requires DF01–DF05
and the operational core, especially OC04.

---

## Prerequisites

- DF01 — DFIR Process & Legal Foundations
- DF02 — Host Forensics
- DF03 — Memory Forensics
- DF04 — Network Forensics
- DF05 — Incident Response Operations

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** an end-to-end incident response for a simulated compromised network.
2. **Create** forensically sound evidence collection with a defensible chain of
   custody.
3. **Evaluate** host, memory, and network evidence to reconstruct the incident.
4. **Create** a professional post-incident report and portfolio artefact.
5. **Evaluate** and execute Australian notification obligations (NDB, APRA, SOCI).
6. **Evaluate** the response's effectiveness and recommend improvements.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** The capstone consolidates specialised DFIR knowledge into
an integrated, legally-aware operation.

**Skills (AQF 7.2):** Students demonstrate the highest-order skills — designing,
creating, and evaluating a complete response independently.

**Application (AQF 7.3):** Students apply the full DFIR skill set with professional
accountability under Australian legal obligations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Incident Responder | PR-CIR-001 | T0041 | Coordinate and perform full-lifecycle incident handling | Lab 1 — Detection to Forensics |
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0432 | Perform multi-source forensic analysis and reporting | Lab 2 — Reporting & Notification |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Systems & software assurance | SURE | Level 5 | Lab 1, Lab 2 |
| Incident management | USUP | Level 4–5 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Incident Management | Incident Response & Digital Forensics | Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | DF06-K01 | Knowledge of scoping and readiness for an IR simulation | Topic 1 |
| Knowledge | DF06-K02 | Knowledge of detection, triage, and evidence collection | Topic 2 |
| Knowledge | DF06-K03 | Knowledge of multi-source forensic analysis | Topic 3 |
| Knowledge | DF06-K04 | Knowledge of PICERL execution, notification, and reporting | Topic 4; Topic 5 |
| Skill | DF06-S01 | Skill in moving from detection to forensics on a live incident | Lab 1 |
| Skill | DF06-S02 | Skill in producing reporting and notifications | Lab 2 |
| Ability | DF06-A01 | Ability to run a full-lifecycle incident response | Lab 1; Lab 2 |
| Ability | DF06-A02 | Ability to self-evaluate and improve response practice | Topic 6; Summative |
| Task | T0041 | Coordinate and perform full-lifecycle incident handling | Lab 1 |
| Task | T0432 | Perform multi-source forensic analysis and reporting | Lab 2 |

---

## Topics

> The capstone is a supervised, integrative project. These "topics" are the
> operation's phases and guidance; the substantive work is the student's own
> response.

### Topic 1: Capstone Scope and Readiness

This phase defines the scenario, the simulated network, rules of engagement,
deliverables, and success criteria, agreed with the supervisor. It covers the
preparation expected before "day one" of an incident.

**Key concepts:**
- Scenario, environment, and rules of engagement
- Deliverables and success criteria
- Preparation and tooling readiness

---

### Topic 2: Detection, Triage, and Evidence Collection

Students begin from a simulated alert: triage, establish scope, and collect
evidence with a defensible chain of custody and correct order of volatility (DF01).

**Key concepts:**
- Alert triage and initial scoping
- Order-of-volatility acquisition
- Chain of custody from the first action

---

### Topic 3: Multi-Source Forensic Analysis

Students apply host (DF02), memory (DF03), and network (DF04) forensics and
correlate the evidence into a coherent reconstruction of the incident.

**Key concepts:**
- Host + memory + network analysis
- Cross-source correlation
- Reconstructing the intrusion

---

### Topic 4: PICERL Response Execution

Students execute the full PICERL cycle (DF05): containment, eradication, and
recovery decisions, documented in a managed case with a decision log.

**Key concepts:**
- Containment/eradication/recovery decisions
- Case management and decision logging
- Operating under time pressure

---

### Topic 5: Notification, Reporting, and Communication

Students assess and execute Australian notification obligations (NDB/APRA/SOCI),
draft stakeholder communications, and write the post-incident report (executive
summary, technical findings, timeline, root cause).

**Key concepts:**
- Notification assessment and execution
- Stakeholder/regulator communication
- Professional post-incident reporting

**Australian context:** Full NDB/APRA/ASD-ACSC/SOCI obligations applied to the
scenario.

---

### Topic 6: Self-Evaluation and Improvement

Students evaluate their response against the success criteria and produce a
prioritised improvement plan (detections, logging, controls) — a blameless
lessons-learned that closes the loop, plus a portfolio artefact.

**Key concepts:**
- Honest self-evaluation against criteria
- Prioritised improvement plan
- Portfolio artefact for employer review

---

## Labs & Exercises

### Lab 1: Detection to Forensics

**Objective:** Triage the incident, collect evidence soundly, and perform
multi-source forensic analysis on the simulated network.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: the provided simulated compromised network (multiple
  VMs/images/captures) + TheHive
- Tools: the full DFIR toolset — Autopsy/Sleuth Kit, Volatility 3, Wireshark/Zeek,
  Plaso, Velociraptor, TheHive — all free/OSS
- Minimum hardware: run components sequentially — within the 8 GB / 4-core / 50 GB
  spec; no GPU

**Instructions:**

1. Triage the provided alert; open and scope a case in TheHive.
2. Collect evidence with documented chain of custody and verification hashes.
3. Perform host forensics (artefacts + timeline) on the affected system(s).
4. Perform memory forensics (processes, injection, credentials, connections).
5. Perform network forensics (C2, exfiltration scope).
6. Correlate all sources into a reconstructed incident with evidence references.

**Expected Output:**

A managed case with sound chain of custody, multi-source forensic findings, and a
correlated incident reconstruction with evidence references and ATT&CK (v19)
mappings. The work is admissibility-aware throughout.

**Reflection Questions:**

1. Which source was decisive, and which filled gaps the others left?
2. Where was your reconstruction least certain, and why?
3. How does your evidence handling satisfy the Evidence Act 1995?

---

### Lab 2: Reporting & Notification

**Objective:** Execute PICERL decisions, assess Australian notifications, and
deliver the post-incident report and portfolio artefact.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: any for reporting; the Lab 1 case for response decisions
- Tools: report template, OAIC/APRA/ACSC/SOCI references, `templates/student-
  portfolio/index.html` — all free
- Minimum hardware: trivial

**Instructions:**

1. From the Lab 1 findings, decide and justify containment/eradication/recovery.
2. Assess NDB eligibility and APRA/SOCI obligations with timeframes; draft the
   notifications.
3. Draft executive and customer communications.
4. Write the post-incident report: executive summary, technical findings, timeline,
   root cause, lessons learned.
5. Produce a prioritised improvement plan (detections/logging/controls).
6. Package a portfolio artefact and submit for community practitioner review.

**Expected Output:**

A justified response, a complete notification determination with drafts, a
professional post-incident report, an improvement plan, and a portfolio artefact
suitable for employer review.

**Reflection Questions:**

1. How well did your response meet the success criteria you set?
2. Which notification decision was hardest, and why?
3. If you re-ran this incident, what would you change in method or tooling?

---

## Assessment

### Formative Assessment: Readiness & Plan Gate

**Type:** Supervisor/peer review of scope and approach

**Description:** Before execution, the scenario scope, evidence-handling plan, and
notification awareness are reviewed; students revise based on feedback. A go/no-go
gate into the operation.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Structured supervisor/peer feedback; revision required
before Lab 1.

---

### Summative Assessment: End-to-End IR Simulation

**Type:** Full incident response operation with report and portfolio artefact

**Description:** The complete operation: detection/triage, sound evidence
collection, multi-source forensics, full PICERL response, Australian notification
assessment and drafts, a professional post-incident report, an improvement plan, a
self-evaluation, and a portfolio artefact — subject to community practitioner
review. Deliverable: full operation package (report ~4,000–5,000 words plus
case/forensic artefacts).

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Design & evidence collection | LO1, LO2 |
| Multi-source forensic analysis | LO3 |
| Report & portfolio | LO4 |
| Notification execution | LO5 |
| Self-evaluation & improvement | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Design & evidence handling | Rigorous, admissibility-grade | Sound | Gaps | Unsound |
| Multi-source forensics | Thorough, correlated, accurate | Solid | Partial | Weak |
| Reporting & portfolio | Employer-grade, clear | Professional | Disorganised | Unclear |
| Notification & legal | Correct, timely, well-reasoned | Mostly correct | Partial | Incorrect |
| Self-evaluation | Insightful, honest, improvement-focused | Reasonable | Superficial | Absent |

---

## Australian Context

This unit incorporates the following Australian context:

- **Evidence Act 1995 (Cth):** Evidence handled and findings written to the
  admissibility standard throughout.
- **NDB / APRA CPS 234 / SOCI / ASD-ACSC:** Full notification assessment applied to
  the scenario.
- **Australian breach case studies:** The scenario reflects the profile of major
  Australian incidents.

---

## Further Reading

**NIST (2012).** *SP 800-61 Rev. 2 — Computer Security Incident Handling Guide.* NIST. https://csrc.nist.gov/pubs/sp/800/61
> Relevance: The lifecycle the capstone executes end-to-end.

**Australian Government (1995).** *Evidence Act 1995 (Cth).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The admissibility standard governing the capstone's evidence handling (Australian source).

**Office of the Australian Information Commissioner (2024).** *Data breach preparation and response.* OAIC. https://www.oaic.gov.au
> Relevance: The NDB obligations assessed and executed in the capstone (Australian source).

**Luttgens, J., Pepe, M. & Mandia, K. (2014).** *Incident Response & Computer Forensics (3rd ed.).* McGraw-Hill.
> Relevance: A comprehensive practitioner reference spanning the whole capstone.

**Templates — Student Portfolio.** `templates/student-portfolio/index.html` (this repository).
> Relevance: The portfolio artefact format the capstone deliverable must populate (Australian-context degree resource).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DF06 |
| Unit Title | Capstone — IR Simulation |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 24 CP |
| Degree Layer | Capstone |
| Major / Pathway | DFIR |
| Prerequisites | DF01, DF02, DF03, DF04, DF05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 5–6 (Evaluate, Create) |
| Australian Legislation Referenced | Evidence Act 1995 (Cth); Privacy Act 1988 (NDB); APRA CPS 234; Security of Critical Infrastructure Act 2018 |
