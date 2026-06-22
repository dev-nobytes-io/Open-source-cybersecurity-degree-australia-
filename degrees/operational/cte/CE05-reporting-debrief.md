# CE05: Reporting & Debrief

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (red team / emulation experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must review dual-use risk)_

---

## Overview

An emulation is only as valuable as the improvement it drives, and improvement
depends on reporting and debrief. This unit teaches communicating emulation results
to two audiences: a **technical** findings report that detection and defence teams
can act on, and an **executive** summary that leadership can use to make decisions —
including the **TIBER-AU** report format used for threat-intelligence-led testing in
the Australian financial sector. It also covers the purple-team debrief that turns an
operation into shared organisational learning.

Reporting closes the threat-informed-defense loop: findings become prioritised
detection, logging, and control improvements, and the maturity of the defence is
expressed in terms leadership understands (linking to LD03/SC06 and the maturity
models). CE05 builds on CE03–CE04 and OC05/SC06, and prepares students for the CE06
capstone's reporting deliverables.

---

## Prerequisites

- CE04 — Purple Team Operations
- SC06 — Stakeholder Communication (or equivalent)

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Create** a technical findings report that defenders can act on.
2. **Create** an executive summary that communicates emulation results to
   leadership.
3. **Apply** the TIBER-AU reporting format to a threat-led engagement.
4. **Analyse** how to translate emulation findings into prioritised defensive
   improvements.
5. **Evaluate** the purple-team debrief as a learning mechanism.
6. **Recommend** a remediation/detection-improvement plan from emulation findings.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of emulation
reporting, debrief, and the TIBER-AU format.

**Skills (AQF 7.2):** Students develop communication and synthesis skills by
producing technical and executive reporting.

**Application (AQF 7.3):** Students apply reporting to drive defensive improvement in
the Australian regulated-sector context.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Policy & Strategy Planner | OV-SPP-001 | T0445 | Produce reporting that communicates results and drives improvement | Lab 1 — Technical & Executive Report |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Translate findings into prioritised detection improvements | Lab 2 — TIBER-AU-Style Report |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 4–5 | Lab 1, Lab 2 |
| Stakeholder relationship management | RLMT | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Cyber | Reporting & Communication | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Reporting for Two Audiences

This topic establishes the dual-audience nature of emulation reporting: defenders
need detailed, actionable technical findings; leadership needs concise,
risk-and-decision-framed summaries. Both must be accurate and consistent.

**Key concepts:**
- Technical vs executive audiences
- Actionability vs decision-framing
- Accuracy and consistency across both

---

### Topic 2: The Technical Findings Report

This topic teaches structuring a technical report: the emulation narrative,
techniques executed (ATT&CK v19), what was detected vs missed, the evidence, and
prioritised, specific recommendations defenders can implement.

**Key concepts:**
- Emulation narrative and ATT&CK mapping
- Detected/missed with evidence
- Specific, prioritised recommendations

---

### Topic 3: The Executive Summary

This topic teaches the executive summary: leading with the "so what" (how well would
we detect this actor?), expressing results as risk and readiness, and recommending
investment — jargon-free (linking to LD03/SC06).

**Key concepts:**
- Leading with detection/readiness outcomes
- Results as risk and readiness
- Investment-relevant recommendations

---

### Topic 4: TIBER-AU Reporting

This topic covers the TIBER-AU framework's reporting expectations for
threat-intelligence-led red teaming in the Australian financial sector: the
intelligence-led basis, the structured report, and the role of the test outcomes in
regulatory/board assurance.

**Key concepts:**
- TIBER-AU report structure and expectations
- Intelligence-led basis of the test
- Outcomes for assurance

**Australian context:** TIBER-AU is the Australian threat-led testing/reporting
framework.

---

### Topic 5: The Purple-Team Debrief

This topic teaches running an effective debrief: a blameless review of what was
detected and missed, capturing detection hypotheses, and ensuring shared learning
between red and blue (linking to OC04 lessons-learned culture).

**Key concepts:**
- Blameless debrief
- Capturing detection hypotheses
- Shared red/blue learning

---

### Topic 6: From Findings to Improvement Plan

This topic teaches converting findings into a prioritised improvement plan
(detections, logging, controls), tracking it to closure, and expressing the
resulting maturity gain (DML/M3TID/SOC-CMM — see `docs/maturity-models.md`).

**Key concepts:**
- Findings → prioritised improvement plan
- Tracking to closure
- Expressing the maturity gain

**Australian context:** Improvements target Essential Eight-relevant detection and
SOCI obligations.

---

## Labs & Exercises

### Lab 1: Technical & Executive Report (deliverable activity)

**Objective:** Write a technical findings report and a one-page executive summary for
a fictional emulation engagement.

**Prerequisites:**
- Topics 1–3

**Environment:**
- No technical environment — a reporting deliverable using a prior emulation's
  results (e.g. from CE03/CE04). Any device within the 8 GB / 4-core / 50 GB spec.

**Instructions:**

1. Take the results of a prior emulation (detected/missed, evidence).
2. Write a technical findings report: narrative, ATT&CK (v19) mapping, detected/
   missed, evidence, and prioritised recommendations.
3. Write a one-page executive summary leading with "how well would we detect this
   actor?" in risk/readiness terms.
4. Ensure the two are consistent and accurate.
5. Include a prioritised improvement list for defenders.
6. State the maturity gain the improvements would deliver.

**Expected Output:**

A technical findings report plus a one-page executive summary, consistent and
audience-appropriate, with prioritised improvements. Learners can state the core
result in one sentence for the executive.

**Reflection Questions:**

1. What did you include for defenders that you cut for executives, and why?
2. How did you express detection results as risk/readiness?
3. Which recommendation most improves detection maturity?

---

### Lab 2: TIBER-AU-Style Report (deliverable activity)

**Objective:** Produce a TIBER-AU-style threat-intelligence-led red team report for a
fictional Australian financial-sector engagement.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- No technical environment — a reporting deliverable using TIBER-AU references. Any
  device.

**Instructions:**

1. Take a fictional Australian financial-sector engagement with an
   intelligence-led scenario.
2. Structure the report per TIBER-AU expectations (intelligence basis, scenario,
   findings, outcomes).
3. Present the detection/response outcomes for assurance purposes.
4. Provide a prioritised remediation/detection-improvement plan.
5. Frame the outcomes for board/regulatory assurance.
6. Note the maturity baseline and target the engagement implies.

**Expected Output:**

A TIBER-AU-style report with an intelligence-led basis, assurance-framed outcomes,
and a remediation plan. Learners can explain how the report supports regulatory/board
assurance.

**Reflection Questions:**

1. How does the intelligence-led basis change the report versus a generic red team?
2. How are the outcomes framed for assurance rather than just findings?
3. How would this report inform the CISO strategy (LD02)?

---

## Assessment

### Formative Assessment: Audience-Fit Drill

**Type:** Short exercise with answer key

**Description:** Given emulation findings, students write the technical line and the
executive line for each. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Answer key with model technical and executive framings.

---

### Summative Assessment: Emulation Reporting Package

**Type:** Reporting portfolio

**Description:** For a fictional engagement, students produce (a) a technical findings
report, (b) an executive summary, (c) a TIBER-AU-style report for a financial-sector
scenario, and (d) a prioritised improvement plan with a maturity note. Deliverable: a
reporting portfolio (~2,500–3,000 words across artefacts).

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Technical report | LO1, LO4 |
| Executive summary | LO2 |
| TIBER-AU report | LO3 |
| Debrief & improvement plan | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Technical reporting | Detailed, actionable, evidence-linked | Sound | Partial | Weak |
| Executive communication | Clear risk/readiness framing | Adequate | Technical/unclear | Poor |
| TIBER-AU understanding | Accurate, assurance-framed | Reasonable | Superficial | Absent |
| Improvement plan | Prioritised, maturity-aware | Reasonable | Generic | Absent |
| Communication | Professional, consistent | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **TIBER-AU:** The Australian threat-led testing/reporting framework (Topic 4,
  Lab 2).
- **ASD Essential Eight & SOCI:** Improvement plans target Australian monitoring
  obligations.
- **Board/regulatory assurance:** Outcomes framed for the Australian regulated
  sector.

---

## Further Reading

**Reserve Bank of Australia / CFR (2024).** *TIBER-AU framework.* https://www.rba.gov.au
> Relevance: The Australian threat-led testing/reporting framework central to Topic 4 and Lab 2 (Australian source).

**MITRE Center for Threat-Informed Defense (2024–2026).** *Adversary Emulation Library & M3TID.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: Emulation outcomes and maturity framing for reporting (see `docs/maturity-models.md`).

**CREST (2024).** *Red team reporting guidance.* CREST. https://www.crest-approved.org
> Relevance: Professional standards for emulation reporting structure and quality.

**Australian Cyber Security Centre (2024).** *Incident & assurance reporting guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian reporting and assurance expectations (Australian source).

**Heath, C. & Heath, D. (2007).** *Made to Stick.* Random House.
> Relevance: Communication principles for clear executive summaries.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CE05 |
| Unit Title | Reporting & Debrief |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Cyber Threat Emulation |
| Prerequisites | CE04, SC06 |
| Domain Expert | _Unassigned — required before Practitioner Approved (red team experience)_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved (dual-use review)_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (TIBER-AU; Criminal Code Act 1995 context) |
