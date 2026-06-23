# CE06: Capstone — Emulation Exercise

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (red team / emulation experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must review dual-use risk)_

---

## Overview

The CTE capstone integrates the entire major into a single, full threat-emulation
operation conducted jointly with a detection team. Students select a threat actor,
build an intelligence-driven CTID emulation plan, document authorisation and rules of
engagement, execute the operation against an isolated lab with active blue-team
participation, run a purple-team debrief, and deliver both a technical findings
report and a TIBER-AU-style executive summary — feeding detection gaps into an
improvement plan. It is assessed at the highest cognitive levels: students
**create**, **execute**, and **evaluate** a complete emulation.

The capstone is the apex of the operational degree's threat-informed-defense thesis:
a controlled, authorised replication of a real adversary that measurably improves the
defence and its maturity (M3TID/SOC-CMM — see `docs/maturity-models.md`). All work is
strictly within the CE01 authorisation regime, in fully isolated environments, with
the dual-use safety requirements of the major enforced. CE06 requires CE01–CE05 and
the operational core.

---

## Prerequisites

- CE01 — Offensive Foundations & Ethics
- CE02 — Red Team Operations
- CE03 — ATT&CK-Based Emulation
- CE04 — Purple Team Operations
- CE05 — Reporting & Debrief

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** an intelligence-driven, authorised emulation operation end-to-end.
2. **Create** a CTID-methodology emulation plan with documented rules of engagement.
3. **Execute** the operation against an isolated lab with active detection-team
   participation.
4. **Evaluate** detection coverage and conduct a purple-team debrief.
5. **Create** technical and TIBER-AU-style executive reporting.
6. **Recommend** a detection-improvement plan that feeds back into defence and
   maturity.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** The capstone consolidates specialised emulation knowledge
into an integrated, authorised operation.

**Skills (AQF 7.2):** Students demonstrate the highest-order skills — creating,
executing, and evaluating a complete emulation independently and safely.

**Application (AQF 7.3):** Students apply emulation with professional accountability,
within the Australian authorisation regime, to improve defence.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Exploitation Analyst (711) | AN-EXP-001 | T0591 | Plan and execute a full authorised emulation operation | Lab 1 — Plan & Execute |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Evaluate detection and deliver improvement from emulation | Lab 2 — Debrief, Report & Improve |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 5 | Lab 1, Lab 2 |
| Security operations | SCAD | Level 4–5 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Cyber | Adversary Emulation & Purple Teaming | Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CE06-K01 | Knowledge of scenario, intelligence, and authorisation for an exercise | Topic 1 |
| Knowledge | CE06-K02 | Knowledge of emulation plan development | Topic 2 |
| Knowledge | CE06-K03 | Knowledge of execution with an active blue team | Topic 3 |
| Knowledge | CE06-K04 | Knowledge of detection evaluation, purple debrief, and reporting | Topic 4; Topic 5 |
| Skill | CE06-S01 | Skill in planning and executing an isolated emulation operation | Lab 1 |
| Skill | CE06-S02 | Skill in debriefing, reporting, and improving | Lab 2 |
| Ability | CE06-A01 | Ability to run a full authorised emulation end to end | Lab 1; Lab 2 |
| Ability | CE06-A02 | Ability to deliver measurable defensive improvement and maturity | Topic 6; Summative |
| Task | T0591 | Plan and execute a full authorised emulation operation | Lab 1 |
| Task | T0259 | Evaluate detection and deliver improvement from emulation | Lab 2 |

---

## Topics

> The capstone is a supervised, integrative operation. These "topics" are the phases
> and guidance; the substantive work is the student's own emulation, conducted
> safely under authorisation in an isolated lab.

### Topic 1: Scenario, Intelligence, and Authorisation

This phase defines the threat scenario and actor (intelligence-driven), the isolated
lab, and the rules of engagement and authorisation (CE01), agreed with the
supervisor.

**Key concepts:**
- Intelligence-driven scenario and actor selection
- Isolated lab definition
- Rules of engagement and authorisation

---

### Topic 2: Emulation Plan Development

Students build the CTID-methodology emulation plan: techniques (ATT&CK v19),
sequencing (Attack Flow), and the detection outcomes to be tested.

**Key concepts:**
- CTID plan development
- Technique sequencing
- Detection outcomes to test

---

### Topic 3: Execution with Active Blue Team

Students execute the operation in the isolated lab with active detection-team
participation, documenting each step and the telemetry generated.

**Key concepts:**
- Authorised, isolated execution
- Active blue-team participation
- Documenting execution and telemetry

---

### Topic 4: Detection Evaluation and Purple Debrief

Students evaluate detection coverage (detected/missed) and run a blameless
purple-team debrief capturing shared learning and detection hypotheses.

**Key concepts:**
- Coverage evaluation
- Blameless purple-team debrief
- Capturing detection hypotheses

---

### Topic 5: Reporting

Students produce a technical findings report and a TIBER-AU-style executive summary
(CE05), consistent and audience-appropriate.

**Key concepts:**
- Technical findings report
- TIBER-AU-style executive summary
- Consistency and accuracy

---

### Topic 6: Improvement and Maturity

Students convert detection gaps into a prioritised improvement plan and express the
maturity gain (M3TID/SOC-CMM), plus package a portfolio artefact.

**Key concepts:**
- Gaps → prioritised improvement plan
- Maturity gain (M3TID/SOC-CMM)
- Portfolio artefact

**Australian context:** Improvements target Essential Eight-relevant detection and
SOCI obligations.

---

## Labs & Exercises

### Lab 1: Plan & Execute (isolated capstone operation)

**Objective:** Plan and execute the full authorised emulation operation against an
isolated lab with active detection-team participation.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: a **fully isolated** capstone lab (target VM(s), a free SIEM with
  detections, and a detection-team role) — no external network access
- Tools: CTID emulation plan, Atomic Red Team, open-source C2 (CE02), ATT&CK
  Navigator, Sigma — all free/OSS
- Minimum hardware: run sequentially — within the 8 GB / 4-core / 50 GB spec; no GPU.
  **No external network access; authorisation/RoE in place.**

**Instructions:**

1. Confirm scenario, isolation, and approved RoE with your supervisor.
2. Finalise the CTID emulation plan (techniques, sequence, detection outcomes).
3. Execute the operation in the isolated lab with the blue role watching.
4. Record each technique's detected/missed result with evidence.
5. Document the operation (steps, telemetry, deconfliction).
6. Produce a Navigator coverage layer (detected/missed).

**Expected Output:**

A documented, authorised, isolated emulation operation with a detected/missed
coverage layer and full execution record. Learners can demonstrate scope discipline
and isolation throughout.

**Reflection Questions:**

1. Which technique most challenged the detection team, and why?
2. Where did the plan need real-time adjustment, and how did you stay in scope?
3. How faithful was the operation to the chosen actor?

---

### Lab 2: Debrief, Report & Improve (capstone deliverable)

**Objective:** Run the purple-team debrief and deliver the reporting and improvement
plan.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- No offensive execution — a debrief, reporting, and planning deliverable using
  `templates/student-portfolio/index.html`. Any device.

**Instructions:**

1. Run a blameless purple-team debrief with the blue role; capture detection
   hypotheses.
2. Write the technical findings report (narrative, ATT&CK v19, detected/missed,
   evidence).
3. Write a TIBER-AU-style executive summary framing detection/readiness outcomes.
4. Convert the gaps into a prioritised detection-improvement plan (new detections,
   logging).
5. Express the maturity gain (M3TID/SOC-CMM).
6. Package the capstone as a portfolio artefact and submit for community
   practitioner review.

**Expected Output:**

A purple-team debrief record, a technical report, a TIBER-AU-style executive summary,
a prioritised improvement plan, a maturity statement, and a portfolio artefact
suitable for employer review.

**Reflection Questions:**

1. Which detection gap most improves the defence if closed, and how?
2. How well did your reporting serve both defenders and executives?
3. What does this operation reveal about the organisation's detection maturity?

---

## Assessment

### Formative Assessment: Plan & Authorisation Gate

**Type:** Supervisor/peer review of scenario, plan, and RoE

**Description:** Before execution, the scenario, emulation plan, and rules of
engagement are reviewed for fidelity, scope safety, and dual-use risk; students
revise. A go/no-go gate into execution.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Structured feedback against a plan/safety rubric; revision
required before Lab 1.

---

### Summative Assessment: Full Emulation Operation

**Type:** End-to-end emulation operation with reporting and portfolio artefact

**Description:** The complete operation: intelligence-driven CTID emulation plan with
documented RoE/authorisation; isolated, authorised execution with active blue-team
participation; coverage evaluation and purple-team debrief; technical and TIBER-AU-
style reporting; a detection-improvement plan with a maturity statement; and a
portfolio artefact — subject to community practitioner review. Deliverable: full
operation package (report ~4,000–5,000 words plus plan, coverage, and improvement
artefacts).

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Plan & authorisation | LO1, LO2 |
| Isolated execution | LO3 |
| Coverage & debrief | LO4 |
| Reporting | LO5 |
| Improvement & maturity | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Plan & fidelity | Faithful, intelligence-driven, scoped | Sound | Partial | Weak |
| Execution & safety | Rigorous, authorised, isolated, documented | Adequate | Minor gaps | Unsafe |
| Coverage & debrief | Precise coverage; effective blameless debrief | Solid | Partial | Weak |
| Reporting | Employer-grade technical + executive | Professional | Mixed | Poor |
| Improvement & maturity | Prioritised; clear maturity gain | Reasonable | Generic | Absent |

---

## Australian Context

This unit incorporates the following Australian context:

- **Criminal Code Act 1995 (Cth) Part 10.7:** All execution within the CE01
  authorisation regime, isolated lab only.
- **TIBER-AU:** The executive reporting format for the capstone.
- **ACSC-reported actors & Essential Eight:** The scenario and the detection
  improvements target Australian-relevant threats and obligations.

---

## Further Reading

**MITRE Center for Threat-Informed Defense (2024–2026).** *Adversary Emulation Library, Attack Flow, M3TID.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The methodology, sequencing, and maturity model the capstone integrates (see `docs/maturity-models.md`).

**Reserve Bank of Australia / CFR (2024).** *TIBER-AU framework.* https://www.rba.gov.au
> Relevance: The executive reporting format for the capstone (Australian source).

**Red Canary (2024).** *Atomic Red Team.* https://github.com/redcanaryco/atomic-red-team
> Relevance: The free technique-execution library for the operation.

**Australian Cyber Security Centre (2024).** *Threat advisories & Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian threat context grounding the capstone scenario (Australian source).

**Templates — Student Portfolio.** `templates/student-portfolio/index.html` (this repository).
> Relevance: The portfolio artefact format the capstone deliverable must populate (Australian-context degree resource).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CE06 |
| Unit Title | Capstone — Emulation Exercise |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 24 CP |
| Degree Layer | Capstone |
| Major / Pathway | Cyber Threat Emulation |
| Prerequisites | CE01, CE02, CE03, CE04, CE05 |
| Domain Expert | _Unassigned — required before Practitioner Approved (red team experience)_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved (dual-use review)_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 5–6 (Evaluate, Create) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) Part 10.7; TIBER-AU |
