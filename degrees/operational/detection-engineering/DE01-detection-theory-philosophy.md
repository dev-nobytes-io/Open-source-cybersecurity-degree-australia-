# DE01: Detection Theory & Philosophy

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit establishes the theory and philosophy that make detection engineering a
discipline rather than a pile of rules. Students learn why detections exist, what
makes a detection *good*, and how to reason about durability, coverage, and alert
quality. It anchors on the **Pyramid of Pain**, **detection-as-code**, the
detection engineering lifecycle, and the principle that the goal is reliable,
actionable signal — not maximum rules. It is the conceptual foundation for the
data, logic, testing, and operations units that follow.

Detection engineering is the build-side of threat-informed defense: it converts
adversary knowledge (ATT&CK v19, CTI) into durable detections and measures coverage
honestly. In the Australian context, detection capability underpins the ASD
Essential Eight monitoring expectations and SOCI detection obligations. DE01 builds
on OC01 (Adversary Tradecraft) and OC02 (Security Monitoring & SIEM) and precedes
DE02–DE06.

---

## Prerequisites

- OC01 — Adversary Tradecraft & TTPs
- OC02 — Security Monitoring & SIEM

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** detections by where they sit on the Pyramid of Pain and their
   durability against adversary change.
2. **Evaluate** detection quality across false-positive risk, coverage, and evasion
   potential.
3. **Analyse** the detection engineering lifecycle and the detection-as-code
   paradigm.
4. **Evaluate** detection coverage against the MITRE ATT&CK (v19) framework.
5. **Analyse** how detection maps to the NIST CSF 2.0 Detect function.
6. **Recommend** improvements to a set of detections based on a quality assessment.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of detection
theory, quality, and lifecycle.

**Skills (AQF 7.2):** Students develop evaluative skills by assessing detection
durability, quality, and coverage.

**Application (AQF 7.3):** Students apply detection theory to evaluate and improve
real detections against Australian monitoring expectations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0569 | Apply threat frameworks to design and evaluate detections | Lab 1 — Pyramid of Pain Mapping |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Evaluate detection logic for quality and coverage | Lab 2 — Detection Quality Review |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 3–4 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Detection Engineering | Practitioner | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Why Detection Engineering Exists

This topic frames detection as the bridge from threat knowledge to actionable
alerts, distinguishes detection engineering from alerting and hunting, and
introduces the detection engineering lifecycle (intelligence → data → write → test
→ operationalise → tune).

**Key concepts:**
- Detection as threat-knowledge-to-alert
- DE vs alerting vs hunting
- The detection engineering lifecycle

---

### Topic 2: The Pyramid of Pain and Durability

This topic deepens the Pyramid of Pain for detection: why TTP- and behaviour-level
detections cost adversaries more than atomic indicators, and how to deliberately
target durable levels of the pyramid.

**Key concepts:**
- Indicator durability across the pyramid
- Targeting TTP/behaviour-level detection
- Cost-to-the-adversary thinking

---

### Topic 3: What Makes a Good Detection

This topic defines detection quality: precision vs recall, false-positive and
false-negative cost, specificity, robustness to evasion, and actionability
(can an analyst do something with the alert?).

**Key concepts:**
- Precision/recall and error costs
- Specificity and evasion-resistance
- Actionability and alert fatigue

---

### Topic 4: Detection-as-Code

This topic treats detections as software: version control, peer review, testing,
and CI/CD for detection content (Sigma in Git), enabling reproducibility, auditability,
and collaboration.

**Key concepts:**
- Detections in version control
- Peer review and testing of detections
- CI/CD for detection content

---

### Topic 5: Coverage and ATT&CK

This topic teaches reasoning about coverage: mapping detections to ATT&CK (v19),
building coverage heatmaps in Navigator, and honestly distinguishing "have data"
from "have a detection" from "have a tested detection".

**Key concepts:**
- Detection-to-technique mapping
- Coverage heatmaps in Navigator
- Honest coverage accounting

---

### Topic 6: Detection and the NIST CSF 2.0 Detect Function

This topic maps detection engineering to NIST CSF 2.0 — DE.AE (Adverse Event
Analysis) and DE.CM (Continuous Monitoring) — and to the Australian monitoring
expectations of the Essential Eight, framing detection as a governed capability.

**Key concepts:**
- NIST CSF 2.0 DE.AE and DE.CM
- Detection as a governed capability
- Alignment to Essential Eight monitoring

**Australian context:** Detection capability is aligned to ASD Essential Eight
monitoring and SOCI obligations.

---

## Labs & Exercises

### Lab 1: Pyramid of Pain Mapping

**Objective:** Map a set of existing detections to the Pyramid of Pain and assess
durability.

**Prerequisites:**
- Topics 1–2

**Environment:**
- Operating System: any (analysis lab)
- Tools: a provided set of detection rules, ATT&CK Navigator (v19) — all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take the provided set of detections (mix of indicator- and behaviour-based).
2. Classify each by its Pyramid of Pain level.
3. For each, assess how easily an adversary could evade it.
4. Map each detection to its ATT&CK (v19) technique in Navigator.
5. Identify which detections are most/least durable and why.
6. Recommend which to keep, improve, or retire.

**Expected Output:**

A classified detection set with Pyramid level, evasion assessment, ATT&CK mapping,
and keep/improve/retire recommendations. Learners can justify the durability
ranking.

**Reflection Questions:**

1. Which detection would survive the adversary swapping tools, and which would not?
2. How does targeting a higher pyramid level change detection design?
3. Which retirement would reduce noise without losing real coverage?

---

### Lab 2: Detection Quality Review

**Objective:** Evaluate a set of detection rules for quality and recommend
improvements.

**Prerequisites:**
- Topics 3–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: provided detection rules + sample data, ATT&CK Navigator — all free
- Minimum hardware: trivial

**Instructions:**

1. Review each provided rule for false-positive risk against the sample data.
2. Assess coverage gaps relative to a target ATT&CK technique set.
3. Identify evasion weaknesses in each rule.
4. Rate each rule's actionability for an analyst.
5. Map the current coverage as a Navigator heatmap (data vs detection vs tested).
6. Produce a prioritised improvement plan.

**Expected Output:**

A quality review (false-positive risk, coverage gaps, evasion, actionability), a
coverage heatmap, and a prioritised improvement plan. Learners can defend their
quality judgements with evidence from the sample data.

**Reflection Questions:**

1. Which quality dimension mattered most for these rules, and why?
2. Where did "have data" not mean "have a detection"?
3. How would detection-as-code have prevented some of these issues?

---

## Assessment

### Formative Assessment: Detection Quality Drill

**Type:** Self-check exercise with answer key

**Description:** Given detection rules, students rate Pyramid level, false-positive
risk, and evasion potential. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Answer key with the quality assessment per rule.

---

### Summative Assessment: Detection Portfolio Evaluation

**Type:** Analytical report

**Description:** Given an organisation's detection set, threat profile, and data
baseline, students (a) classify detections on the Pyramid of Pain, (b) evaluate
quality and coverage against ATT&CK (v19), (c) map to NIST CSF 2.0 Detect and
Essential Eight monitoring, and (d) recommend a prioritised improvement plan framed
as a detection-as-code lifecycle. Deliverable: 2,500–3,000 word report with a
coverage heatmap.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Pyramid classification | LO1 |
| Quality & coverage evaluation | LO2, LO4 |
| Lifecycle & CSF/Essential Eight mapping | LO3, LO5 |
| Improvement plan | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Durability analysis | Insightful Pyramid/evasion reasoning | Sound | Partial | Weak |
| Quality evaluation | Rigorous, evidence-based | Adequate | Superficial | Poor |
| Coverage & mapping | Honest, ATT&CK/CSF-mapped | Mostly sound | Partial | Inaccurate |
| Improvement plan | Prioritised, lifecycle-framed | Reasonable | Generic | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Monitoring expectations frame detection as a governed
  capability (Topic 6).
- **SOCI Act 2018:** Detection obligations for critical infrastructure.
- **ACSC advisories:** Source of the behaviours that durable detections target.

---

## Further Reading

**Bianco, D. (2013).** *The Pyramid of Pain.* https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html
> Relevance: The durability framework central to Topics 2 and the labs.

**Roth, F. & SigmaHQ community (2024).** *Detection Engineering & Sigma philosophy.* https://github.com/SigmaHQ/sigma
> Relevance: The detection-as-code and rule-quality thinking underpinning this unit.

**NIST (2024).** *Cybersecurity Framework 2.0 — Detect function (DE.AE, DE.CM).* NIST. https://www.nist.gov/cyberframework
> Relevance: The governance mapping for detection in Topic 6.

**Australian Cyber Security Centre (2024).** *Best Practices for Event Logging and Threat Detection.* ACSC. https://www.cyber.gov.au
> Relevance: Australian monitoring/detection expectations aligned in Topic 6 (Australian source).

**MITRE ATT&CK (v19, 2026).** *ATT&CK for Enterprise.* https://attack.mitre.org
> Relevance: The technique taxonomy used for coverage mapping.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DE01 |
| Unit Title | Detection Theory & Philosophy |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Detection Engineering |
| Prerequisites | OC01, OC02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
