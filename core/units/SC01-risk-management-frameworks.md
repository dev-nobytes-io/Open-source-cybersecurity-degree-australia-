# SC01: Risk Management Frameworks

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches students to manage cybersecurity risk the way organisations
actually need it managed: as a structured, repeatable, decision-driving
discipline rather than a gut feeling. It covers the major risk frameworks —
**NIST CSF 2.0**, the **NIST Risk Management Framework (SP 800-37/800-30)**, and
**ISO/IEC 27001:2022 with ISO 27005** — and the practice of identifying,
analysing, evaluating, and treating risk. It also introduces risk quantification
(including FAIR-style thinking) so risk can be expressed in terms executives and
boards understand: likely financial impact, not just "high/medium/low".

A theme that runs through the entire Strategic Core starts here: **good risk and
compliance management is a commercial enabler, not just a cost.** Demonstrable
risk management unlocks markets, contracts, and customer trust — an Australian
financial services firm needs it for **APRA CPS 234**, a government supplier needs
it for **IRAP/ISM**, and a SaaS vendor needs **SOC 2** to close enterprise deals.
SC01 builds on F04 (Security Concepts) and underpins SC03 (Governance), SC05
(Program Management), and the GRC and Leadership majors.

---

## Prerequisites

- F04 — Security Concepts & Principles
- F05 — Legal, Ethics & Australian Compliance

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** the purpose and structure of the major risk frameworks (NIST CSF
   2.0, NIST RMF, ISO 27001/27005) and when each is used.
2. **Apply** a risk-assessment process to identify, analyse, and evaluate
   cybersecurity risks for an organisation.
3. **Analyse** risks using both qualitative and quantitative methods, including
   risk quantification in financial terms.
4. **Apply** risk-treatment decisions (mitigate, transfer, avoid, accept) and
   document them in a risk register.
5. **Examine** how Australian regulatory regimes (APRA CPS 234, SOCI) impose risk-
   management obligations.
6. **Analyse** how a credible risk-management posture functions as a commercial
   enabler across different industries.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of risk-management
frameworks, methods, and the Australian regulatory context for risk.

**Skills (AQF 7.2):** Students develop analytical skills by assessing and
quantifying risk and communication skills by articulating risk to decision-makers.

**Application (AQF 7.3):** Students apply a full risk process to a realistic
Australian organisation, producing the artefacts (risk register, treatment plan)
used in professional practice.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Control Assessor | SP-RSK-002 | T0177 | Perform risk assessments and identify gaps in security posture | Lab 1 — Risk Assessment & Register |
| NIST NICE DCWF | 2023 | Information Systems Security Manager | OV-MGT-001 | T0149 | Recommend resource allocations to mitigate identified risks | Lab 2 — Risk Quantification & Treatment |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information risk management | BURM | Level 4 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Risk Management | Practitioner | Lab 1, Lab 2 |

---

## Topics

### Topic 1: What Risk Management Is For

Risk management exists to support decisions under uncertainty. This topic defines
risk (likelihood × impact against assets), distinguishes inherent from residual
risk, introduces risk appetite and tolerance, and frames the whole discipline as
serving business decisions — including the decision to invest in controls that
open commercial opportunities.

**Key concepts:**
- Risk, inherent vs residual, appetite and tolerance
- Risk as decision support, not paperwork
- The cost/enabler duality of risk management

---

### Topic 2: The Major Frameworks

This topic surveys the frameworks and their fit. **NIST CSF 2.0** provides an
outcome-based common language across six functions (Govern, Identify, Protect,
Detect, Respond, Recover). **NIST RMF (SP 800-37)** provides a rigorous,
control-based process (categorise → select → implement → assess → authorise →
monitor) drawing on SP 800-30 for assessment. **ISO/IEC 27001:2022** provides a
certifiable management-system standard, with **ISO 27005** for risk. Students
learn to choose and combine them.

**Key concepts:**
- NIST CSF 2.0 functions and the new Govern function
- NIST RMF process and SP 800-30 risk assessment
- ISO 27001:2022 ISMS and ISO 27005

---

### Topic 3: The Risk Assessment Process

This topic teaches the practical assessment workflow: establish context and scope,
identify assets and threats (reusing F04/OC01 threat thinking), identify
vulnerabilities, analyse likelihood and impact, and evaluate against appetite. The
output is a defensible, prioritised view of risk.

**Key concepts:**
- Context, scope, and asset identification
- Threat/vulnerability identification and likelihood/impact analysis
- Evaluation against risk appetite

---

### Topic 4: Quantifying Risk

"High/medium/low" rarely drives investment. This topic introduces quantitative
risk analysis — expected loss, ranges and probabilities, and FAIR-style
factor analysis — so risk can be expressed as likely financial exposure. It
covers the strengths and limits of quantification and how to communicate
uncertainty honestly.

**Key concepts:**
- Qualitative vs quantitative analysis
- FAIR-style loss-event frequency × magnitude
- Communicating ranges and uncertainty

---

### Topic 5: Risk Treatment and the Register

Risk identified must be risk decided. This topic covers the four treatment
options (mitigate, transfer, avoid, accept), selecting controls, the role of cyber
insurance (transfer), documenting decisions and owners in a **risk register**, and
tracking residual risk over time. It stresses that accepting risk is a legitimate,
documented decision — not a failure.

**Key concepts:**
- Treatment options and control selection
- The risk register: owners, decisions, residual risk
- Risk transfer and cyber insurance

---

### Topic 6: Regulatory Risk Obligations and the Commercial Case

This topic connects risk management to obligation and opportunity. On the
obligation side: **APRA CPS 234** requires regulated entities to manage
information-security risk, and the **SOCI Act** mandates a risk-management program
for critical infrastructure. On the opportunity side: a credible posture is what
lets a firm win government work (**IRAP/ISM**), enterprise SaaS deals (**SOC 2**),
and regulated-sector contracts (**APRA**, **ISO 27001**). Students learn to map
the right regime to the right industry.

**Key concepts:**
- APRA CPS 234 and SOCI risk-management obligations
- Compliance as market access (IRAP, SOC 2, ISO 27001, APRA) by industry
- Building the commercial case for risk investment

**Australian context:** Centres on APRA CPS 234, SOCI, and the IRAP/ISM regime.

---

## Labs & Exercises

### Lab 1: Risk Assessment & Register

**Objective:** Conduct a structured risk assessment for a scenario organisation and
produce a prioritised risk register.

**Prerequisites:**
- Topics 1–3 and 5

**Environment:**
- Operating System: any (analysis lab)
- Tools: a spreadsheet or risk-register template, NIST CSF 2.0 and ISO 27001 Annex
  A references (free)
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario organisation (e.g. an Australian regional health provider) and
   define the assessment context and scope.
2. Identify key assets and the threats to them (reuse OC01/threat-landscape
   knowledge).
3. For 8–10 risks, analyse likelihood and impact on a defined scale and compute a
   rating.
4. Map each risk to the relevant NIST CSF 2.0 function and an ISO 27001 Annex A
   control area.
5. Record each risk in a register with owner, current controls, and rating.
6. Identify the top five risks against a stated risk appetite.

**Expected Output:**

A completed risk register of 8–10 risks with ratings, framework mappings, owners,
and a justified top-five. Learners can explain their prioritisation against
appetite.

**Reflection Questions:**

1. Where did qualitative ratings feel imprecise, and which risks would benefit from
   quantification?
2. How did mapping to NIST CSF and ISO 27001 change how you'd communicate the
   register?
3. Which risks are driven by an Australian regulatory obligation?

---

### Lab 2: Risk Quantification & Treatment

**Objective:** Quantify a key risk in financial terms and produce a justified
treatment recommendation, including the commercial case.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: a spreadsheet (for a simple FAIR-style model), the Lab 1 register
- Minimum hardware: trivial

**Instructions:**

1. Select one top risk from Lab 1's register.
2. Build a simple quantitative model: estimate loss-event frequency and a range for
   loss magnitude; compute an annualised loss exposure range.
3. Propose a treatment (mitigate/transfer/avoid/accept) with the control(s) or
   insurance involved and their indicative cost.
4. Compare the exposure reduction against the treatment cost (a basic cost-benefit
   view).
5. Add the commercial case: which market/contract/customer-trust outcome the
   treatment also enables (e.g. SOC 2 for enterprise deals, IRAP for government).
6. Write a one-page recommendation for a decision-maker.

**Expected Output:**

A quantified exposure range, a costed treatment recommendation with cost-benefit
reasoning, and an explicit commercial-enabler argument. Learners can defend the
recommendation to a non-technical decision-maker.

**Reflection Questions:**

1. How did expressing risk in dollars change the persuasiveness of your case?
2. What are the limits of your quantification, and how did you communicate
   uncertainty?
3. For a different industry (government vs fintech), how would the commercial case
   change?

---

## Assessment

### Formative Assessment: Framework Fit Exercise

**Type:** Short-answer exercise with answer key

**Description:** Given several organisations (a bank, a government supplier, a SaaS
startup, a hospital), students select the most appropriate risk/compliance
framework(s) and justify the choice. Self-marked.

**Learning Outcomes Assessed:** LO1, LO5, LO6

**Feedback mechanism:** Answer key with the recommended framework(s) and rationale
per organisation.

---

### Summative Assessment: Risk Management Report

**Type:** Practical report

**Description:** For an assigned Australian organisation, students (a) conduct a
risk assessment and produce a register, (b) quantify the top risk in financial
terms, (c) recommend treatments with cost-benefit reasoning, (d) map obligations
to the relevant Australian regime (APRA/SOCI/IRAP as applicable), and (e) argue the
commercial case for the recommended investment. Deliverable: 2,500–3,000 word
report with a risk register and quantification model.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Risk assessment & register | LO1, LO2 |
| Quantification of top risk | LO3 |
| Treatment recommendations | LO4 |
| Regulatory mapping & commercial case | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Risk analysis | Rigorous, well-prioritised, framework-mapped | Solid analysis with minor gaps | Partial analysis | Superficial or flawed |
| Quantification | Sound model; honest about uncertainty | Adequate quantification | Weak or unclear model | Little/no quantification |
| Treatment & cost-benefit | Well-justified, costed, decision-ready | Reasonable treatment | Generic treatment | Unjustified treatment |
| Regulatory & commercial framing | Insightful obligation + enabler mapping by industry | Valid mapping | Superficial mapping | Missing or incorrect |
| Communication | Clear, executive-ready | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **APRA CPS 234:** Information-security risk-management obligation for APRA-
  regulated entities (Topic 6, assessment).
- **Security of Critical Infrastructure Act 2018:** Mandatory risk-management
  program for critical infrastructure (Topic 6).
- **IRAP / Australian Government ISM & SOC 2:** Framed as market-access enablers
  mapped to government and commercial industries respectively.

---

## Further Reading

**NIST (2024).** *Cybersecurity Framework (CSF) 2.0.* NIST. https://www.nist.gov/cyberframework
> Relevance: The outcome-based framework and common language used throughout this unit.

**NIST (2018/2012).** *SP 800-37 Rev. 2 (RMF) & SP 800-30 (Risk Assessment).* NIST. https://csrc.nist.gov
> Relevance: The rigorous risk-management and assessment processes in Topics 2–3.

**ISO/IEC (2022).** *ISO/IEC 27001:2022 & ISO/IEC 27005.* ISO.
> Relevance: The certifiable ISMS and risk standards central to the commercial-enabler theme (note: paywalled standard).

**APRA (2019).** *Prudential Standard CPS 234 Information Security.* APRA. https://www.apra.gov.au
> Relevance: The Australian prudential obligation driving risk management in regulated finance (Australian source).

**Freund, J. & Jones, J. (2014).** *Measuring and Managing Information Risk: A FAIR Approach.* Butterworth-Heinemann.
> Relevance: The quantification approach applied in Topic 4 and Lab 2.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SC01 |
| Unit Title | Risk Management Frameworks |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Strategic Core |
| Major / Pathway | Strategic |
| Prerequisites | F04, F05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | APRA CPS 234; Security of Critical Infrastructure Act 2018 |
