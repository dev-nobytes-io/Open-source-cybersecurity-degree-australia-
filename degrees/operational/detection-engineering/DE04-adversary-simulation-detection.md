# DE04: Adversary Simulation for Detection

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Detections must be proven, not assumed. This unit teaches validating detection
logic by safely simulating adversary behaviour and confirming detections fire as
intended. Students use **Atomic Red Team** to execute ATT&CK (v19) techniques in an
isolated lab, build a detection-testing pipeline (simulate → collect → convert →
detect → verify), and apply purple-team basics to turn missed techniques into new
detections. The unit closes the build–test loop at the heart of detection
engineering.

Simulation-driven validation is how a team knows its threat-informed defense
actually works. In the Australian context, validation scenarios are drawn from ACSC
advisories, ensuring detections are proven against the behaviours seen locally. All
execution is authorised and isolated, respecting the legal boundaries from F05/OC06.
DE04 builds on DE03 and OC06, and feeds DE05 and the DE06 capstone.

---

## Prerequisites

- DE03 — Writing Detection Logic
- OC06 — Offensive Security Concepts

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** Atomic Red Team to safely simulate ATT&CK (v19) techniques in an
   isolated lab.
2. **Evaluate** whether detections fire correctly against simulated behaviour.
3. **Build** a detection-testing pipeline integrating simulation, conversion, and a
   SIEM.
4. **Analyse** detection gaps revealed by simulation and their root causes.
5. **Apply** purple-team practice to convert missed techniques into new detections.
6. **Recommend** validated detection improvements based on test evidence.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of detection
validation and simulation.

**Skills (AQF 7.2):** Students develop technical skills by building testing
pipelines and analytical skills by diagnosing gaps.

**Application (AQF 7.3):** Students apply simulation to validate and improve
detections against Australian-relevant behaviours.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Validate detections by simulating adversary behaviour | Lab 1 — Atomic Red Team Validation |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0294 | Build pipelines to test and correlate detection coverage | Lab 2 — Detection Testing Pipeline |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 4 | Lab 1, Lab 2 |
| Testing | TEST | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Detection Engineering | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Why Validate Detections

This topic establishes the case for validation: untested detections silently fail,
and "we have a rule" is not "we can detect". It introduces validation as a
first-class engineering activity and the safety/authorisation boundaries for
simulation.

**Key concepts:**
- Untested detections fail silently
- Validation as engineering, not afterthought
- Authorisation and isolation for simulation

---

### Topic 2: Atomic Red Team

This topic teaches Atomic Red Team: ATT&CK-mapped atomic tests, executing them
safely in an isolated lab, understanding what each test does, and capturing the
telemetry it generates.

**Key concepts:**
- Atomic tests mapped to ATT&CK (v19)
- Safe execution in isolation
- Capturing generated telemetry

---

### Topic 3: Verifying Detections Fire

This topic teaches the verification step: confirming that the relevant detection
fires when a technique is executed, that it matches the right event, and that the
alert is actionable — and recording detected vs missed.

**Key concepts:**
- Mapping a test to its expected detection
- Confirming the alert fires on the right event
- Recording detected/missed outcomes

---

### Topic 4: Building a Detection-Testing Pipeline

This topic teaches assembling a repeatable pipeline: simulate (Atomic) → collect
(telemetry to SIEM) → convert (Sigma to platform) → detect → verify — so validation
becomes automatable and repeatable.

**Key concepts:**
- The simulate→collect→detect→verify pipeline
- Automating and repeating validation
- Pipeline as part of detection-as-code

---

### Topic 5: Gap Analysis and Root Cause

This topic teaches diagnosing why a technique was missed: missing telemetry
(DE02), flawed rule logic (DE03), or conversion error — and choosing the correct
fix for each cause.

**Key concepts:**
- Missed-technique root causes (data vs logic vs conversion)
- Matching the fix to the cause
- Re-validating after a fix

---

### Topic 6: Purple Teaming for Detection

This topic teaches the purple-team loop: red executes, blue verifies, and every
missed technique becomes a new or improved detection — turning validation into
continuous improvement (linking to OC06).

**Key concepts:**
- The purple-team feedback loop
- Missed technique → new detection
- Continuous validation cadence

**Australian context:** Validation scenarios are drawn from ACSC advisories.

---

## Labs & Exercises

### Lab 1: Atomic Red Team Validation

**Objective:** Execute Atomic Red Team tests in an isolated lab and verify that
detections fire correctly.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: an isolated Windows VM (eval) with telemetry → a free SIEM
  (OpenSearch/Splunk Free)
- Tools: Invoke-AtomicRedTeam, Sysmon, Sigma rules from DE03, a free SIEM — all
  free/OSS
- Minimum hardware: run sequentially — 6 GB RAM / 2 vCPU / 30 GB disk (within the
  8 GB / 4-core / 50 GB spec; no GPU). **Isolated network only.**

**Instructions:**

1. Confirm the lab is isolated and snapshot the VM.
2. Select a small set of Atomic tests matching detections from DE03.
3. Ensure telemetry flows to the SIEM.
4. Execute each test and observe whether the matching detection fires.
5. Record detected vs missed, with the evidence (the firing event).
6. Map the results as a Navigator layer (detected/missed) and revert the VM.

**Expected Output:**

A detected/missed record with firing-event evidence and a Navigator coverage layer,
all within an isolated lab. Learners can show the exact event that each detection
matched.

**Reflection Questions:**

1. Which test was missed, and was it a data, logic, or conversion problem?
2. How did real simulation differ from your expectation of the rule?
3. Why is isolation essential when running Atomic tests?

---

### Lab 2: Detection Testing Pipeline

**Objective:** Build a repeatable pipeline integrating Atomic Red Team, Sigma
conversion, and a SIEM, and use it to close a gap.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: the Lab 1 isolated environment + sigma-cli
- Tools: Invoke-AtomicRedTeam, sigma-cli, the free SIEM, ATT&CK Navigator — all
  free/OSS
- Minimum hardware: as Lab 1

**Instructions:**

1. Script the pipeline steps: run a chosen Atomic test, convert the matching Sigma
   rule, query the SIEM, and report detected/missed.
2. Run the pipeline across a small technique set and produce a coverage report.
3. Identify one missed technique and diagnose its root cause.
4. Fix the cause (new/adjusted rule or logging) and re-run to confirm the fix.
5. Document the new/validated detection and its evidence.
6. Define a cadence for re-running this validation.

**Expected Output:**

A working (even if lightly scripted) testing pipeline, a coverage report, a
diagnosed-and-fixed gap with re-validation evidence, and a re-run cadence. Learners
can explain how the pipeline makes validation repeatable.

**Reflection Questions:**

1. What did automating validation reveal that manual testing missed?
2. How did you confirm your fix actually closed the gap?
3. How does this pipeline support the purple-team loop?

---

## Assessment

### Formative Assessment: Detected-or-Missed Drill

**Type:** Self-check exercise with answer key

**Description:** Given simulation results and rules, students determine whether each
technique would be detected and, if not, the likely root cause. Self-marked.

**Learning Outcomes Assessed:** LO2, LO4

**Feedback mechanism:** Answer key with the detection outcome and root cause.

---

### Summative Assessment: Detection Validation Report

**Type:** Practical report

**Description:** For an assigned technique set (Australian-relevant actor), students
(a) simulate the techniques with Atomic Red Team in isolation, (b) verify detection
coverage, (c) build/describe a testing pipeline, (d) diagnose and fix at least one
gap with re-validation, and (e) recommend validated improvements as a purple-team
loop. Deliverable: 2,000–2,500 word report with a coverage layer and evidence.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Simulation & verification | LO1, LO2 |
| Testing pipeline | LO3 |
| Gap diagnosis & fix | LO4, LO5 |
| Validated improvements | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Safe simulation | Rigorous isolation; correct execution | Adequate | Minor gaps | Unsafe |
| Verification | Precise detected/missed with evidence | Sound | Partial | Weak |
| Pipeline | Repeatable, well-structured | Workable | Manual/partial | Absent |
| Gap remediation | Correct root cause + validated fix | Adequate | Partial | Incorrect |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories:** Source of the techniques used for validation scenarios.
- **Cybercrime Act 2001 (isolation/authorisation):** Simulation stays within
  authorised, isolated labs (reinforcing F05/OC06).
- **ASD Essential Eight:** Validation confirms detection of control-bypass
  behaviours.

---

## Further Reading

**Red Canary (2024).** *Atomic Red Team & Invoke-AtomicRedTeam.* https://github.com/redcanaryco/atomic-red-team
> Relevance: The free, ATT&CK-mapped simulation library used throughout this unit.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Adversary Emulation Library.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: Realistic emulation plans complementing atomic tests.

**SigmaHQ / pySigma (2024).** *Conversion tooling.* https://github.com/SigmaHQ/pySigma
> Relevance: The conversion step in the detection-testing pipeline.

**Australian Cyber Security Centre (2024).** *Threat advisories.* ACSC. https://www.cyber.gov.au
> Relevance: Australian-relevant validation scenarios (Australian source).

**Applebaum, A. et al. / MITRE (2024).** *Purple-teaming and emulation methodology.* The MITRE Corporation. https://attack.mitre.org/resources/
> Relevance: Methodology for the purple-team loop in Topic 6.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DE04 |
| Unit Title | Adversary Simulation for Detection |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Detection Engineering |
| Prerequisites | DE03, OC06 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Cybercrime Act 2001 (contextual) |
