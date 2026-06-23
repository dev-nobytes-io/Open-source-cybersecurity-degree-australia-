# GR03: Compliance Frameworks

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (GRC/compliance experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches implementing and assessing the compliance frameworks that
organisations are measured against: **ISO/IEC 27001:2022**, **NIST CSF 2.0**, and the
**ASD Essential Eight**. Students learn to map controls to a framework, conduct a gap
analysis, and run a maturity/control assessment — the core working skills of a GRC
practitioner, and the mechanism behind the compliance-as-revenue thesis (certification
opens markets).

In the Australian context the **Essential Eight Maturity Model** is government-
mandated and widely expected, the **ISM** is the government control baseline, and ISO
27001 is the dominant commercial certification. GR03 builds on SC03 and GR01–GR02,
and feeds GR05 (audit) and the GR06 capstone. ISO 27001:2022 content must be verified
against the 2022 edition (not 2013) at sign-off.

---

## Prerequisites

- GR01 — Security Governance Design
- SC03 — Governance, Policy & Compliance

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** ISO/IEC 27001:2022 to map an organisation's controls and identify gaps.
2. **Analyse** the NIST CSF 2.0 functions/categories for compliance assessment.
3. **Apply** the ASD Essential Eight Maturity Model to assess an environment.
4. **Evaluate** which framework(s) fit an organisation's industry and goals.
5. **Design** a control-mapping/crosswalk that satisfies multiple frameworks.
6. **Recommend** a prioritised path to compliance/certification.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of the major
compliance frameworks and their assessment.

**Skills (AQF 7.2):** Students develop analytical skills by mapping controls,
identifying gaps, and assessing maturity.

**Application (AQF 7.3):** Students apply framework implementation/assessment to
realistic Australian organisations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Control Assessor (SP-RSK-002) | SP-RSK-002 | T0177 | Assess controls against frameworks and identify gaps | Activity 1 — ISO 27001 Gap Analysis |
| NIST NICE DCWF | 2023 | Cyber Policy & Strategy Planner (752) | OV-SPP-001 | T0226 | Develop compliance and control requirements | Activity 2 — Essential Eight Assessment |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information risk management | IRMG | Level 4–5 | Activity 1 |
| Compliance management | CORE | Level 4 | Activity 1, Activity 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Compliance & Assessment | Practitioner–Advanced | Activity 1, Activity 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | GR03-K01 | Knowledge of the compliance landscape | Topic 1 |
| Knowledge | GR03-K02 | Knowledge of implementing ISO/IEC 27001:2022 | Topic 2 |
| Knowledge | GR03-K03 | Knowledge of applying NIST CSF 2.0 | Topic 3 |
| Knowledge | GR03-K04 | Knowledge of assessing the Essential Eight and control mapping/crosswalks | Topic 4; Topic 5 |
| Skill | GR03-S01 | Skill in performing an ISO 27001 gap analysis | Lab 1 |
| Skill | GR03-S02 | Skill in assessing the Essential Eight | Lab 2 |
| Ability | GR03-A01 | Ability to map one control set across multiple frameworks | Lab 1; Topic 5 |
| Ability | GR03-A02 | Ability to choose and sequence compliance for an organisation | Topic 6; Summative |
| Task | T0177 | Assess controls against frameworks and identify gaps | Lab 1 |
| Task | T0226 | Develop compliance and control requirements | Lab 2 |

---

## Topics

### Topic 1: The Compliance Landscape

This topic surveys the frameworks and their purposes: ISO 27001 (certifiable ISMS),
NIST CSF 2.0 (outcome-based common language), and the Essential Eight (baseline
mitigations) — and how organisations use them together.

**Key concepts:**
- ISO 27001 vs NIST CSF vs Essential Eight
- Certification vs assessment vs baseline
- Using frameworks together

---

### Topic 2: Implementing ISO/IEC 27001:2022

This topic teaches the ISO 27001:2022 ISMS: the management-system clauses, Annex A
controls, the Statement of Applicability, and the implementation lifecycle toward
certification.

**Key concepts:**
- ISMS clauses and Annex A (2022)
- Statement of Applicability
- Implementation toward certification

---

### Topic 3: Applying NIST CSF 2.0

This topic teaches using CSF 2.0 for assessment: functions/categories/subcategories,
profiles (current vs target), and tiers — producing an outcome-based view of
compliance posture.

**Key concepts:**
- CSF 2.0 functions/categories/subcategories
- Current vs target profiles
- Implementation tiers

---

### Topic 4: Assessing the Essential Eight

This topic teaches assessing the ASD Essential Eight using the official maturity
model and assessment guidance: the eight mitigations, Maturity Levels 0–3, and
producing a credible, evidence-based assessment.

**Key concepts:**
- The eight mitigations and Maturity Levels 0–3
- ASD assessment methodology
- Evidence-based maturity assessment

**Australian context:** The Essential Eight Maturity Model is government-mandated in
Australia.

---

### Topic 5: Control Mapping and Crosswalks

This topic teaches mapping one control set across multiple frameworks (ISO 27001 ↔
CSF ↔ Essential Eight ↔ ISM) so a single control satisfies many requirements,
reducing duplication ("test once, satisfy many" — building on SC03).

**Key concepts:**
- Control crosswalks across frameworks
- Unified control sets
- Reducing duplication

---

### Topic 6: Choosing and Sequencing Compliance

This topic teaches selecting framework(s) by industry and goal (linking to the
compliance-as-revenue thesis) and sequencing a prioritised path to compliance/
certification with a gap-driven roadmap.

**Key concepts:**
- Framework selection by industry/goal
- Gap-driven compliance roadmap
- Compliance as commercial enabler

**Australian context:** Framework choice mapped to Australian markets (IRAP/ISM for
government, ISO 27001/APRA for commercial — see SC03).

---

## Labs & Exercises

### Lab 1: ISO 27001 Gap Analysis (analysis activity)

**Objective:** Map an organisation's controls against ISO/IEC 27001:2022 Annex A and
identify gaps.

**Prerequisites:**
- Topics 1, 2, and 5

**Environment:**
- No technical environment — an analysis deliverable using an ISO 27001:2022 Annex A
  checklist (free templates) and a spreadsheet. Any device within the 8 GB / 4-core /
  50 GB spec.

**Instructions:**

1. Take a fictional Australian organisation with a described control environment.
2. Map its existing controls against ISO 27001:2022 Annex A.
3. Identify gaps (missing/partial controls) and rate their severity.
4. Draft a Statement of Applicability extract for a sample of controls.
5. Crosswalk a sample of controls to NIST CSF and the Essential Eight.
6. Recommend a prioritised remediation path toward certification.

**Expected Output:**

An ISO 27001:2022 control mapping with rated gaps, a sample SoA, a crosswalk, and a
prioritised remediation path. Learners can defend the gap prioritisation.

**Reflection Questions:**

1. Which gap most threatens certification, and why?
2. How much duplication did the crosswalk remove?
3. How would you evidence a mapped control in an audit (GR05)?

---

### Lab 2: Essential Eight Assessment (analysis activity)

**Objective:** Conduct an Essential Eight maturity assessment against a fictional
environment using the official ASD guidance.

**Prerequisites:**
- Topics 3–4 and Lab 1

**Environment:**
- No technical environment — an analysis deliverable using the ASD Essential Eight
  assessment guides (free). Any device.

**Instructions:**

1. Take a fictional environment description (current controls and configurations).
2. Assess each of the eight mitigations against Maturity Levels 0–3 using the ASD
   methodology.
3. Record the evidence supporting each rating.
4. Determine the overall maturity level and the gaps to the next level.
5. Recommend a prioritised path to raise maturity by one level.
6. Map the assessment to the organisation's risk register (GR02).

**Expected Output:**

An Essential Eight assessment with per-mitigation maturity ratings, evidence, an
overall level, and a prioritised improvement path. Learners can justify each rating
against the ASD methodology.

**Reflection Questions:**

1. Which mitigation was hardest to assess, and why?
2. Why does ASD use a maturity model rather than pass/fail?
3. Which improvement gives the most risk reduction toward the next level?

---

## Assessment

### Formative Assessment: Framework-Fit Drill

**Type:** Short-answer exercise with answer key

**Description:** Given organisations, students select the appropriate framework(s) and
justify the choice commercially and by industry. Self-marked.

**Learning Outcomes Assessed:** LO4

**Feedback mechanism:** Answer key with recommended frameworks and rationale.

---

### Summative Assessment: Compliance Assessment & Roadmap

**Type:** Practical report

**Description:** For an assigned Australian organisation, students (a) conduct an ISO
27001:2022 gap analysis, (b) conduct an Essential Eight maturity assessment, (c)
produce a multi-framework control crosswalk, and (d) recommend a prioritised path to
compliance/certification tied to the organisation's commercial goals. Deliverable:
2,500–3,000 word report with gap analysis and crosswalk.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| ISO 27001 gap analysis | LO1, LO5 |
| Essential Eight assessment | LO3 |
| Framework selection | LO2, LO4 |
| Compliance roadmap | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Framework knowledge | Precise, current (2022/E8) application | Mostly | Partial | Inaccurate |
| Gap analysis | Rigorous, evidence-based, prioritised | Sound | Partial | Weak |
| Crosswalk | Real duplication removed | Adequate | Partial | Poor |
| Roadmap & commercial fit | Prioritised, industry-fit | Reasonable | Generic | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight Maturity Model:** Government-mandated baseline assessed in
  Lab 2.
- **Australian Government ISM:** The government control baseline in crosswalks.
- **Framework-to-market mapping:** IRAP/ISM (government), ISO 27001/APRA
  (commercial).

---

## Further Reading

**ISO/IEC (2022).** *ISO/IEC 27001:2022 & Annex A.* ISO.
> Relevance: The certifiable ISMS standard implemented in Topic 2 and Lab 1 (paid standard; use the 2022 edition).

**NIST (2024).** *Cybersecurity Framework 2.0 & Reference Tool.* NIST. https://www.nist.gov/cyberframework
> Relevance: The outcome-based framework applied in Topic 3 (free reference tool).

**Australian Cyber Security Centre (2023).** *Essential Eight Maturity Model & assessment guidance.* ACSC. https://www.cyber.gov.au/essential-eight
> Relevance: The government-mandated baseline assessed in Lab 2 (Australian source).

**Australian Cyber Security Centre (2024).** *Information Security Manual (ISM).* ACSC. https://www.cyber.gov.au/ism
> Relevance: The Australian government control baseline used in crosswalks (Australian source).

**ISACA (2024).** *CISM — Information Security Program / compliance.* ISACA. https://www.isaca.org
> Relevance: Compliance-assessment grounding and certification bridge.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | GR03 |
| Unit Title | Compliance Frameworks |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | GRC |
| Prerequisites | GR01, SC03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (ASD Essential Eight / ISM) |
