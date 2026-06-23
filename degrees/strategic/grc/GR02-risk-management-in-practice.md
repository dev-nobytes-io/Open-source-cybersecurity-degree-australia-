# GR02: Risk Management in Practice

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (GRC/risk experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit takes the risk frameworks from SC01 and turns them into operating practice:
building and maintaining a risk register, analysing risks with techniques like
bow-tie analysis, defining and applying a risk appetite, and making and documenting
treatment decisions. Students learn to run risk management as an ongoing,
decision-driving discipline grounded in **ISO/IEC 27005:2022** and the **NIST RMF
(SP 800-37)**.

Risk is the centre of GRC and the input to governance and compliance decisions. In
the Australian context it is shaped by **APRA CPG 234** guidance and the risk-
management expectations of the SOCI Act. Risk maturity is tracked with the **RIMS
Risk Maturity Model** (see `docs/maturity-models.md`), and — per the maturity
integration — operational capability maturity gaps feed this register as risk inputs.
GR02 builds on SC01 and GR01, and feeds GR03–GR06.

---

## Prerequisites

- GR01 — Security Governance Design
- SC01 — Risk Management Frameworks

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** a risk-assessment process to build and maintain a risk register.
2. **Analyse** risks using bow-tie analysis to expose causes, controls, and
   consequences.
3. **Design** a risk appetite statement and use it to prioritise treatment.
4. **Apply** treatment decisions (mitigate/transfer/avoid/accept) with owners and
   documentation.
5. **Evaluate** risk using ISO 27005 and NIST RMF processes.
6. **Recommend** a risk-management approach that drives decisions for an organisation.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of operational risk
management, analysis techniques, and the Australian risk-regulatory context.

**Skills (AQF 7.2):** Students develop analytical skills by assessing risk, building
registers, and applying bow-tie analysis.

**Application (AQF 7.3):** Students apply risk management to realistic Australian
organisations, producing decision-useful artefacts.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Control Assessor (SP-RSK-002) | SP-RSK-002 | T0177 | Perform risk assessment and maintain a risk register | Activity 1 — Risk Register & Bow-Tie |
| NIST NICE DCWF | 2023 | Information Systems Security Manager (722) | OV-MGT-001 | T0149 | Recommend treatment and resource allocation for risk | Activity 2 — Appetite & Treatment |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information risk management | IRMG | Level 5 | Activity 1, Activity 2 |
| Information management / governance | GOVN | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Risk Management | Practitioner–Advanced | Activity 1, Activity 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | GR02-K01 | Knowledge of risk management as a practice | Topic 1 |
| Knowledge | GR02-K02 | Knowledge of the risk register | Topic 2 |
| Knowledge | GR02-K03 | Knowledge of bow-tie analysis | Topic 3 |
| Knowledge | GR02-K04 | Knowledge of risk appetite, treatment, ISO 27005, and NIST RMF | Topic 4; Topic 6 |
| Skill | GR02-S01 | Skill in building a risk register and bow-tie | Lab 1 |
| Skill | GR02-S02 | Skill in setting appetite and selecting treatment | Lab 2 |
| Ability | GR02-A01 | Ability to operate a risk register in practice | Lab 1; Topic 2 |
| Ability | GR02-A02 | Ability to align treatment with appetite and resources | Lab 2; Topic 4 |
| Task | T0177 | Perform risk assessment and maintain a risk register | Lab 1 |
| Task | T0149 | Recommend treatment and resource allocation for risk | Lab 2 |

---

## Topics

### Topic 1: Risk Management as Practice

This topic frames risk management as an ongoing operating discipline (not a one-off
assessment): the cycle of identify → analyse → evaluate → treat → monitor, run
continuously and feeding governance decisions.

**Key concepts:**
- The continuous risk-management cycle
- Risk as decision support
- Inputs from capability maturity (anti-mismatch wiring)

---

### Topic 2: The Risk Register

This topic teaches building and maintaining a register: risk statements
(cause→event→consequence), likelihood/impact scales, inherent vs residual risk,
owners, and keeping it current and decision-useful rather than a compliance artefact.

**Key concepts:**
- Well-formed risk statements
- Likelihood/impact, inherent vs residual
- Owners and currency

---

### Topic 3: Bow-Tie Analysis

This topic teaches bow-tie analysis: mapping threats/causes → top event →
consequences, with preventive controls on the left and mitigating controls on the
right — exposing control gaps for the most significant risks.

**Key concepts:**
- Bow-tie structure (causes, event, consequences)
- Preventive vs mitigating controls
- Exposing control gaps

---

### Topic 4: Risk Appetite and Tolerance

This topic teaches defining risk appetite and tolerance and using them to drive
decisions: a usable appetite statement that prioritises treatment and clarifies what
risk the organisation will and won't accept.

**Key concepts:**
- Appetite vs tolerance
- Writing a usable appetite statement
- Driving treatment prioritisation

---

### Topic 5: Risk Treatment

This topic teaches treatment: the four options (mitigate/transfer/avoid/accept),
control selection, the role of cyber insurance (transfer), documented acceptance, and
tracking residual risk over time.

**Key concepts:**
- Treatment options and control selection
- Risk transfer and insurance
- Documented acceptance and residual tracking

---

### Topic 6: ISO 27005, NIST RMF, and Australian Guidance

This topic situates practice in the standards: ISO/IEC 27005:2022 risk management,
the NIST RMF (SP 800-37) process, and Australian guidance (APRA CPG 234), and
introduces risk maturity (RIMS RMM).

**Key concepts:**
- ISO 27005:2022 and NIST RMF
- APRA CPG 234 risk guidance
- RIMS Risk Maturity Model

**Australian context:** APRA CPG 234 risk-management guidance for the financial
sector.

---

## Labs & Exercises

### Lab 1: Risk Register & Bow-Tie (deliverable activity)

**Objective:** Build a risk register and apply bow-tie analysis to the top risks.

**Prerequisites:**
- Topics 1–3

**Environment:**
- No technical environment — a deliverable using a spreadsheet and draw.io. Any
  device within the 8 GB / 4-core / 50 GB spec.

**Instructions:**

1. Take a fictional Australian organisation with a described context.
2. Build a risk register of 10 well-formed risks (cause→event→consequence) with
   likelihood/impact and owners.
3. Compute inherent and residual ratings.
4. Select the top 3 risks and produce a bow-tie for each (causes, event,
   consequences, preventive/mitigating controls).
5. Identify control gaps exposed by the bow-ties.
6. Note which risks are driven by Australian regulatory obligations or by capability-
   maturity gaps (link to `docs/maturity-models.md`).

**Expected Output:**

A 10-entry risk register with ratings and owners, three bow-tie analyses, and an
identified set of control gaps. Learners can defend the top-risk prioritisation.

**Reflection Questions:**

1. Which bow-tie exposed the most surprising control gap?
2. How did inherent vs residual rating change the prioritisation?
3. Which risk came from a capability-maturity gap (e.g. weak detection)?

---

### Lab 2: Appetite & Treatment (deliverable activity)

**Objective:** Define a risk appetite statement and use it to prioritise treatment
decisions.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- No technical environment — a deliverable (document + register). Any device.

**Instructions:**

1. For the Lab 1 organisation, draft a risk appetite statement (and tolerances).
2. Apply the appetite to the register to prioritise 5 treatment decisions.
3. For each, select a treatment option (mitigate/transfer/avoid/accept) and rationale.
4. Assign owners and define residual-risk tracking.
5. Document any risk acceptance with justification and authority.
6. Map the approach to ISO 27005 / NIST RMF and APRA CPG 234.

**Expected Output:**

A risk appetite statement and five justified, owned treatment decisions with
documented acceptance and standards mapping. Learners can defend each treatment
against the appetite.

**Reflection Questions:**

1. How did the appetite change which risks you treated first?
2. Which risk did you accept, and how did you justify it?
3. Where would risk transfer (insurance) be appropriate, and what are its limits?

---

## Assessment

### Formative Assessment: Risk-Statement Drill

**Type:** Self-check exercise with answer key

**Description:** Given vague risk entries, students rewrite them as well-formed
cause→event→consequence statements with appropriate ratings. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Answer key with model risk statements and ratings.

---

### Summative Assessment: Risk Management Package

**Type:** Practical report

**Description:** For an assigned Australian organisation, students (a) build a risk
register with bow-tie analysis for the top risks, (b) define a risk appetite, (c)
produce prioritised, owned treatment decisions, and (d) map the approach to ISO
27005/NIST RMF/APRA CPG 234 and assess risk maturity (RIMS RMM). Deliverable:
2,500–3,000 word package with register and bow-ties.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Risk register & bow-tie | LO1, LO2 |
| Appetite | LO3 |
| Treatment | LO4 |
| Standards mapping & maturity | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Risk analysis | Rigorous register + insightful bow-ties | Sound | Partial | Weak |
| Appetite | Usable, decision-driving | Adequate | Vague | Poor |
| Treatment | Well-justified, owned, documented | Reasonable | Generic | Unjustified |
| Standards & maturity | Accurate ISO/RMF/CPG mapping; maturity-aware | Mostly | Superficial | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **APRA CPG 234:** Risk-management guidance for the financial sector.
- **SOCI Act risk-management program:** Critical-infrastructure risk obligations.
- **RIMS Risk Maturity Model:** Risk maturity (see `docs/maturity-models.md`).

---

## Further Reading

**ISO/IEC (2022).** *ISO/IEC 27005:2022 — Information security risk management.* ISO.
> Relevance: The risk-management standard central to Topics 5–6 (paid standard).

**NIST (2018, 2012).** *SP 800-37 Rev. 2 (RMF) & SP 800-30.* NIST. https://csrc.nist.gov
> Relevance: The risk-management and assessment processes applied in this unit.

**APRA (2019).** *Prudential Practice Guide CPG 234.* APRA. https://www.apra.gov.au
> Relevance: Australian risk-management guidance for the financial sector (Australian source).

**RIMS (2024).** *RIMS Risk Maturity Model.* RIMS. https://www.rims.org
> Relevance: The risk-maturity model for Topic 6 (see `docs/maturity-models.md`).

**CGE / bow-tie methodology references (2024).** *Bow-Tie Risk Analysis.* (Freely available summaries.)
> Relevance: The bow-tie technique applied in Topic 3 and Lab 1.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | GR02 |
| Unit Title | Risk Management in Practice |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | GRC |
| Prerequisites | GR01, SC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | APRA CPS 234 / CPG 234; Security of Critical Infrastructure Act 2018 (contextual) |
