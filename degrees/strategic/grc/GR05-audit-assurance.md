# GR05: Audit & Assurance

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (audit/assurance experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches how compliance is *proven*: control testing, internal audit
methodology, and the formal assurance processes that give regulators, boards, and
customers confidence. Students learn to plan and run an audit, design and execute
control tests, gather and evaluate evidence, and report findings — including the
**IRAP** assessment process for Australian government systems and the **ASAE 3402**
assurance standard.

Audit and assurance close the GRC loop: governance and controls only count if they
can be evidenced and independently verified. In the Australian context this includes
IRAP (government cloud/data assessment) and ASAE 3402 (Australian auditing standard
for service-organisation controls). GR05 builds on GR03 (frameworks) and GR04
(regulatory), and feeds the GR06 capstone. It is the primary unit for ISO 27001 Lead
Auditor and IRAP-assessor pathways.

---

## Prerequisites

- GR03 — Compliance Frameworks
- GR04 — Australian Regulatory Environment

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** an internal audit plan for a compliance framework (e.g. ISO 27001).
2. **Apply** control-testing methods to gather and evaluate audit evidence.
3. **Analyse** the difference between control design and operating effectiveness.
4. **Evaluate** the IRAP assessment process for an Australian government system.
5. **Analyse** assurance standards (ASAE 3402) and their use.
6. **Recommend** audit findings and a remediation/assurance approach.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of audit
methodology, control testing, and Australian assurance processes.

**Skills (AQF 7.2):** Students develop analytical skills by planning audits, testing
controls, and evaluating evidence.

**Application (AQF 7.3):** Students apply audit and assurance to realistic Australian
organisations and government systems.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Control Assessor (SP-RSK-002) | SP-RSK-002 | T0177 | Plan and perform control assessment and audit | Activity 1 — ISO 27001 Audit Plan |
| NIST NICE DCWF | 2023 | Security Control Assessor (SP-RSK-002) | SP-RSK-002 | T0178 | Test controls and evaluate evidence | Activity 2 — IRAP-Style Assessment |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information risk management | IRMG | Level 5 | Activity 1 |
| Quality assurance / audit | QUAS | Level 4–5 | Activity 1, Activity 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Audit & Assurance | Practitioner–Advanced | Activity 1, Activity 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | GR05-K01 | Knowledge of the role of audit and assurance | Topic 1 |
| Knowledge | GR05-K02 | Knowledge of audit planning | Topic 2 |
| Knowledge | GR05-K03 | Knowledge of control testing and evidence | Topic 3 |
| Knowledge | GR05-K04 | Knowledge of findings/reporting, IRAP, and assurance standards (ASAE 3402) | Topic 4; Topic 6 |
| Skill | GR05-S01 | Skill in producing an ISO 27001 audit plan | Lab 1 |
| Skill | GR05-S02 | Skill in performing an IRAP-style assessment | Lab 2 |
| Ability | GR05-A01 | Ability to test controls and evaluate evidence | Lab 2; Topic 3 |
| Ability | GR05-A02 | Ability to report findings credibly to stakeholders | Lab 1; Topic 4 |
| Task | T0177 | Plan and perform control assessment and audit | Lab 1 |
| Task | T0178 | Test controls and evaluate evidence | Lab 2 |

---

## Topics

### Topic 1: The Role of Audit and Assurance

This topic frames audit/assurance as independent verification that controls exist and
work — giving boards, regulators, and customers confidence. It distinguishes internal
audit, external audit/certification, and assurance engagements.

**Key concepts:**
- Independent verification and confidence
- Internal vs external audit vs assurance
- Lines of defence

---

### Topic 2: Audit Planning

This topic teaches planning an audit: scope and objectives, risk-based audit
universe, the audit programme, sampling, and the schedule — for a compliance cycle
(e.g. ISO 27001 internal audit).

**Key concepts:**
- Scope, objectives, and risk-based planning
- Audit programme and sampling
- Audit schedule for a compliance cycle

---

### Topic 3: Control Testing and Evidence

This topic teaches testing controls: design vs operating effectiveness, test methods
(inquiry, observation, inspection, re-performance), evidence sufficiency, and
documenting workpapers that support conclusions.

**Key concepts:**
- Design vs operating effectiveness
- Test methods and evidence sufficiency
- Workpapers and conclusions

---

### Topic 4: Findings and Reporting

This topic teaches turning test results into findings: rating severity, root cause,
management response, and reporting to the audit committee — and tracking remediation
to closure.

**Key concepts:**
- Findings: severity, root cause, response
- Reporting to the audit committee
- Tracking remediation

---

### Topic 5: IRAP and Australian Government Assurance

This topic covers the **IRAP** (Information Security Registered Assessors Program)
process for assessing systems handling Australian government data against the ISM, the
assessor role, and the assessment lifecycle and outputs.

**Key concepts:**
- IRAP purpose and assessor role
- ISM-based assessment
- IRAP lifecycle and outputs

**Australian context:** IRAP is the Australian government assessment program.

---

### Topic 6: Assurance Standards (ASAE 3402)

This topic covers formal assurance: **ASAE 3402** (the Australian standard for
assurance over service-organisation controls, akin to SOC 2/ISAE 3402), Type 1 vs
Type 2, and how organisations use assurance reports for third-party trust (linking to
SC04).

**Key concepts:**
- ASAE 3402 and service-organisation assurance
- Type 1 vs Type 2
- Assurance reports for third-party trust

**Australian context:** ASAE 3402 is the Australian assurance standard.

---

## Labs & Exercises

### Lab 1: ISO 27001 Audit Plan (deliverable activity)

**Objective:** Design an internal audit plan for ISO 27001 for a fictional
organisation.

**Prerequisites:**
- Topics 1–4

**Environment:**
- No technical environment — a deliverable using ISO 27001:2022 and a control set
  (e.g. from GR03). Any device within the 8 GB / 4-core / 50 GB spec.

**Instructions:**

1. Take a fictional Australian organisation pursuing ISO 27001.
2. Define the audit scope, objectives, and a risk-based audit programme.
3. For five controls, design specific tests (method, sample, evidence sought).
4. Define how you would distinguish design from operating effectiveness.
5. Define the findings rating scale and reporting approach.
6. Produce the audit schedule for the first compliance cycle.

**Expected Output:**

An ISO 27001 internal audit plan with scope, a risk-based programme, control tests
for five controls, a findings/reporting approach, and a schedule. Learners can justify
the risk-based prioritisation.

**Reflection Questions:**

1. Which control was hardest to design a test for, and why?
2. How would you tell design effectiveness from operating effectiveness?
3. What evidence would convince an external certification auditor?

---

### Lab 2: IRAP-Style Assessment (analysis activity)

**Objective:** Complete a simulated IRAP-style assessment of a fictional government
system description.

**Prerequisites:**
- Topics 5–6 and Lab 1

**Environment:**
- No technical environment — an analysis deliverable using the ISM and IRAP guidance
  (free). Any device.

**Instructions:**

1. Take a fictional Australian government system description.
2. Select a sample of ISM controls relevant to the system.
3. Assess the implementation and effectiveness of each against the ISM.
4. Record the evidence and any deficiencies.
5. Produce assessment findings and a recommendation on the system's suitability.
6. Note the residual risks for the authorising officer's decision.

**Expected Output:**

An IRAP-style assessment with ISM control evaluations, evidence, findings, and a
suitability recommendation with residual risks. Learners can explain the assessor's
role and the basis for the recommendation.

**Reflection Questions:**

1. Which ISM control deficiency most affects suitability, and why?
2. How does the assessor's role differ from the system owner's?
3. How do residual risks inform the authorisation decision?

---

## Assessment

### Formative Assessment: Test-Design Drill

**Type:** Self-check exercise with answer key

**Description:** Given controls, students design an appropriate test (method, sample,
evidence) and state whether it tests design or operating effectiveness. Self-marked.

**Learning Outcomes Assessed:** LO2, LO3

**Feedback mechanism:** Answer key with model tests and effectiveness type.

---

### Summative Assessment: Audit & Assurance Plan

**Type:** Practical report

**Description:** For an assigned Australian organisation, students (a) design an
internal audit plan for a framework, (b) design and document control tests with an
evidence approach, (c) complete an IRAP-style assessment of a government system, and
(d) recommend findings and an assurance approach (including ASAE 3402 where relevant).
Deliverable: 2,500–3,000 word report with audit plan and tests.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Audit plan | LO1 |
| Control tests & evidence | LO2, LO3 |
| IRAP assessment | LO4 |
| Assurance approach & findings | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Audit planning | Rigorous, risk-based, complete | Sound | Partial | Weak |
| Control testing | Apt methods; design vs operating clear | Adequate | Partial | Poor |
| IRAP/assurance | Accurate ISM/IRAP/ASAE understanding | Mostly | Superficial | Inaccurate |
| Findings & recommendation | Evidence-based, actionable | Reasonable | Generic | Weak |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **IRAP:** The Australian government assessment program (Topic 5, Lab 2).
- **Australian Government ISM:** The control baseline assessed in IRAP.
- **ASAE 3402:** The Australian assurance standard for service-organisation controls.

---

## Further Reading

**Australian Cyber Security Centre (2024).** *IRAP & Information Security Manual.* ACSC. https://www.cyber.gov.au/ism
> Relevance: The IRAP process and ISM baseline for Topic 5 and Lab 2 (Australian source).

**AUASB (2024).** *ASAE 3402 — Assurance Reports on Controls at a Service Organisation.* Auditing and Assurance Standards Board. https://www.auasb.gov.au
> Relevance: The Australian assurance standard for Topic 6 (Australian source).

**ISO/IEC (2022).** *ISO/IEC 27001:2022 & ISO 19011 (auditing management systems).* ISO.
> Relevance: The ISMS and audit-methodology basis for Topics 2–4 (paid standards).

**ISACA (2024).** *CRISC / IS audit guidance.* ISACA. https://www.isaca.org
> Relevance: Control-testing and assurance grounding; certification bridge (CRISC, ISO Lead Auditor).

**IIA (2024).** *International Standards for the Professional Practice of Internal Auditing.* Institute of Internal Auditors. https://www.theiia.org
> Relevance: Internal-audit methodology underpinning Topics 1–4.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | GR05 |
| Unit Title | Audit & Assurance |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | GRC |
| Prerequisites | GR03, GR04 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (IRAP/ISM; ASAE 3402 assurance standard) |
