# DE05: Detection Operations & Management

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit covers running a detection capability over time: managing a detection
library as a living asset, measuring alert quality, tuning systematically, and
governing the detection lifecycle from proposal to retirement. Students learn the
operational discipline — metrics, workflows, version control, and CI/CD — that
keeps detections effective as the environment and the adversary change, and that
prevents the slow decay into alert fatigue.

Detection operations is where threat-informed defense is *sustained*: coverage is
re-measured, detections are tuned against real noise, and the library evolves with
the threat landscape (ATT&CK v19, CTI). In the Australian context, a managed
detection capability evidences the monitoring maturity expected under the Essential
Eight and SOCI. DE05 builds on DE01–DE04 and connects to OC02 and SC05 (program
management). It precedes the DE06 capstone.

---

## Prerequisites

- DE03 — Writing Detection Logic
- DE04 — Adversary Simulation for Detection

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** alert quality using meaningful detection metrics.
2. **Apply** systematic tuning workflows to reduce noise without losing coverage.
3. **Design** a detection lifecycle (propose → build → test → deploy → tune →
   retire).
4. **Apply** detection-as-code practices (version control, review, CI/CD) to manage
   a library.
5. **Evaluate** detection coverage and prioritise development against the threat
   landscape.
6. **Recommend** operational improvements that sustain a detection capability.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of detection
operations, metrics, and lifecycle management.

**Skills (AQF 7.2):** Students develop analytical and management skills by measuring,
tuning, and governing detections.

**Application (AQF 7.3):** Students apply operations practice to sustain a detection
capability aligned to Australian monitoring expectations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Tune detections and manage alert quality | Lab 1 — Alert Tuning |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0163 | Perform trend analysis and manage the detection lifecycle | Lab 2 — Detection Lifecycle & Metrics |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 4 | Lab 1 |
| Service level management | SLMO | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Detection Engineering | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Alert Quality Metrics

This topic defines the metrics that matter: precision, recall, false-positive rate,
alert volume per detection, time-to-triage, and signal-to-noise — and warns against
vanity metrics (e.g. "number of rules").

**Key concepts:**
- Precision, recall, FP rate, alert volume
- Signal-to-noise and time-to-triage
- Avoiding vanity metrics

---

### Topic 2: Systematic Tuning

This topic teaches tuning as a disciplined workflow: identifying noisy detections,
diagnosing the noise source, applying allow-lists/refinements without creating blind
spots, and documenting every tuning decision.

**Key concepts:**
- Identifying and diagnosing noisy detections
- Refinement vs blind spots
- Documenting tuning decisions

---

### Topic 3: The Detection Lifecycle

This topic teaches governing detections through states — proposed, in development,
testing, deployed, tuned, deprecated/retired — with criteria and ownership for each
transition.

**Key concepts:**
- Lifecycle states and transitions
- Ownership and criteria per state
- Retiring detections responsibly

---

### Topic 4: Detection-as-Code Operations

This topic operationalises detection-as-code: a Git-based rule repository, peer
review, automated testing in CI, and controlled deployment to the SIEM — bringing
software-engineering rigour to detections.

**Key concepts:**
- Git-based rule repository and review
- CI testing of detections
- Controlled deployment

---

### Topic 5: Coverage Management and Prioritisation

This topic teaches managing coverage over time: re-measuring against ATT&CK (v19)
and the current threat landscape, prioritising new detection development by threat
relevance, and reporting coverage to stakeholders.

**Key concepts:**
- Re-measuring coverage over time
- Threat-informed development prioritisation
- Coverage reporting

**Australian context:** Coverage prioritisation reflects the Australian threat
landscape (ACSC reporting).

---

### Topic 6: Sustaining the Capability

This topic addresses the long game: preventing detection decay (environment drift,
log changes), managing technical debt in the library, team workflows, and
demonstrating the capability's value (linking to SC05/SC06).

**Key concepts:**
- Detection decay and drift
- Managing library technical debt
- Demonstrating capability value

**Australian context:** A managed capability evidences Essential Eight/SOCI
monitoring maturity.

---

## Labs & Exercises

### Lab 1: Alert Tuning

**Objective:** Analyse a set of alerts for tuning opportunities and produce a tuning
recommendation report.

**Prerequisites:**
- Topics 1–2

**Environment:**
- Operating System: any (with a free SIEM: OpenSearch/Splunk Free) or provided
  alert dataset
- Tools: a free SIEM or alert dataset, a spreadsheet — all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 30 GB disk (within the 8 GB / 4-core /
  50 GB spec; no GPU)

**Instructions:**

1. Analyse the provided alert dataset; compute volume and false-positive rate per
   detection.
2. Identify the noisiest detections and diagnose the noise source.
3. Propose specific tuning for each (refinement/allow-list) without creating blind
   spots.
4. Estimate the before/after true- and false-positive impact.
5. Document each tuning decision and its justification.
6. Flag any detection that should be retired rather than tuned.

**Expected Output:**

A tuning recommendation report with per-detection metrics, diagnosed noise sources,
specific tunings, before/after estimates, and documented decisions. Learners can
justify that tuning preserves real coverage.

**Reflection Questions:**

1. Which tuning carried the greatest blind-spot risk, and how did you mitigate it?
2. Which detection was beyond tuning, and why retire it?
3. How would you measure whether the tuning worked after deployment?

---

### Lab 2: Detection Lifecycle & Metrics

**Objective:** Design a detection lifecycle and metrics regime for a managed
library, with a detection-as-code workflow.

**Prerequisites:**
- Topics 3–6 and Lab 1

**Environment:**
- Operating System: any (with Git)
- Tools: Git, a rule repository (Sigma), ATT&CK Navigator (v19) — all free/OSS
- Minimum hardware: trivial

**Instructions:**

1. Define lifecycle states and transition criteria/ownership for a detection
   library.
2. Set up a Git-based rule repository structure with a review/CI outline.
3. Define a metrics regime (the 4–6 metrics you would track and report).
4. Re-measure coverage of a sample library against a target ATT&CK technique set.
5. Prioritise the next three detections to develop, by threat relevance.
6. Produce a one-page capability report for a stakeholder.

**Expected Output:**

A documented lifecycle, a Git repo structure with review/CI outline, a metrics
regime, a re-measured coverage view, a prioritised development backlog, and a
capability report. Learners can defend the metrics as non-vanity and decision-useful.

**Reflection Questions:**

1. Which metric best demonstrates capability value to a stakeholder?
2. How does detection-as-code reduce risk in deploying changes?
3. How would you keep coverage current as the threat landscape shifts?

---

## Assessment

### Formative Assessment: Metric & Tuning Drill

**Type:** Self-check exercise with answer key

**Description:** Given alert statistics, students identify the worst detections,
recommend tuning vs retirement, and select non-vanity metrics. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Answer key with the recommended action and metrics.

---

### Summative Assessment: Detection Operations Plan

**Type:** Practical report

**Description:** For an assigned detection library and environment, students (a)
analyse alert quality and propose tuning, (b) design a detection lifecycle and
detection-as-code workflow, (c) define a metrics regime, and (d) re-measure coverage
and produce a prioritised development backlog with a capability report. Deliverable:
2,500–3,000 word report with metrics and a coverage view.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Alert analysis & tuning | LO1, LO2 |
| Lifecycle & detection-as-code | LO3, LO4 |
| Coverage & prioritisation | LO5 |
| Capability improvements | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Metrics & tuning | Rigorous, non-vanity, blind-spot-aware | Sound | Partial | Weak |
| Lifecycle & DaC | Well-governed, software-grade workflow | Adequate | Partial | Absent |
| Coverage management | Threat-informed, prioritised | Reasonable | Generic | Weak |
| Capability value | Clear, stakeholder-ready | Adequate | Thin | Poor |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight & SOCI:** A managed detection capability evidences
  monitoring maturity and obligations.
- **ACSC threat landscape:** Drives coverage prioritisation and development backlog.
- **ACSC event-logging guidance:** Underpins the data the detections depend on.

---

## Further Reading

**Bianco, D. & community (2024).** *Detection Maturity Model & detection operations.* (Freely available community resources.)
> Relevance: The maturity and operations thinking underpinning Topics 1, 3, and 6.

**SigmaHQ / pySigma (2024).** *Rule management & CI.* https://github.com/SigmaHQ
> Relevance: The detection-as-code tooling for Topic 4 and Lab 2.

**Brotby, K. & Hinson, G. (2016).** *PRAGMATIC Security Metrics.* CRC Press.
> Relevance: Designing the non-vanity metrics regime in Topic 1.

**Australian Cyber Security Centre (2024).** *Best Practices for Event Logging and Threat Detection.* ACSC. https://www.cyber.gov.au
> Relevance: Australian monitoring expectations a managed capability must meet (Australian source).

**MITRE ATT&CK (v19, 2026).** *ATT&CK for Enterprise.* https://attack.mitre.org
> Relevance: The basis for coverage re-measurement in Topic 5.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DE05 |
| Unit Title | Detection Operations & Management |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Detection Engineering |
| Prerequisites | DE03, DE04 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
