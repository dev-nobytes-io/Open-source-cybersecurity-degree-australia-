# DE02: Data Sources & Log Engineering

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Detections are only as good as the data beneath them. This unit teaches the data
engineering that underpins detection: identifying the right log sources, modelling
and normalising data to a common schema, auditing source coverage against the
techniques you need to detect, and closing visibility gaps. Students learn to treat
data as the foundational dependency of detection — a missing or mis-parsed log
silently defeats even a perfect rule.

In the Australian context, this unit is where the ASD *Essential Eight* logging
requirements and the SOCI Act monitoring obligations become concrete: which logs
must exist, be retained, and be parsed. DE02 builds on F06 (Data & Log Analysis),
OC02, and DE01, and is the prerequisite for writing effective detection logic in
DE03.

---

## Prerequisites

- DE01 — Detection Theory & Philosophy
- F06 — Data & Log Analysis

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** which log sources are required to detect a given set of ATT&CK
   (v19) techniques.
2. **Evaluate** an environment's log coverage and identify visibility gaps.
3. **Apply** data modelling and normalisation to unify disparate log sources.
4. **Design** a logging configuration that meets detection needs within constraints.
5. **Analyse** Australian logging obligations (Essential Eight, SOCI) and their
   detection implications.
6. **Recommend** logging improvements that close the highest-priority detection
   gaps.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of log sources,
data modelling, and coverage analysis for detection.

**Skills (AQF 7.2):** Students develop technical skills by normalising data and
analytical skills by auditing coverage.

**Application (AQF 7.3):** Students apply log engineering to realistic environments,
aligned to Australian logging obligations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Audit log sources and identify coverage gaps for detection | Lab 1 — Log Source Coverage Audit |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0166 | Normalise and model data to support correlation and detection | Lab 2 — Log Normalisation |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 3–4 | Lab 1 |
| Data management | DATM | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Detection Engineering | Practitioner | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | DE02-K01 | Knowledge of log sources and telemetry for detection | Topic 1 |
| Knowledge | DE02-K02 | Knowledge of technique-to-data-source mapping | Topic 2 |
| Knowledge | DE02-K03 | Knowledge of coverage auditing and gap analysis | Topic 3 |
| Knowledge | DE02-K04 | Knowledge of data modelling, normalisation, and Australian logging obligations | Topic 4; Topic 6 |
| Skill | DE02-S01 | Skill in auditing log-source coverage | Lab 1 |
| Skill | DE02-S02 | Skill in normalising logs to a data model | Lab 2 |
| Ability | DE02-A01 | Ability to identify and prioritise data-source gaps | Lab 1; Topic 3 |
| Ability | DE02-A02 | Ability to engineer logging within real-world constraints | Topic 5; Summative |
| Task | T0259 | Audit log sources and identify coverage gaps for detection | Lab 1 |
| Task | T0166 | Normalise and model data to support correlation and detection | Lab 2 |

---

## Topics

### Topic 1: Log Sources and Telemetry for Detection

This topic surveys the detection-relevant log sources — endpoint (Sysmon, EVTX,
EDR), network (firewall, DNS, proxy, Zeek), identity, and cloud — and what each can
and cannot reveal, building on F06 at engineering depth.

**Key concepts:**
- Endpoint, network, identity, cloud telemetry
- What each source reveals and its blind spots
- High-value sources for detection

---

### Topic 2: Technique-to-Data-Source Mapping

This topic teaches mapping the techniques you must detect to the data sources that
reveal them, using ATT&CK (v19) data-source/component definitions and CTID Sensor
Mappings — so logging decisions are driven by detection needs.

**Key concepts:**
- ATT&CK data sources/components
- CTID Sensor Mappings
- Detection-driven logging decisions

---

### Topic 3: Coverage Auditing and Gap Analysis

This topic teaches auditing an environment's actual logging against the required
sources, producing a visibility-gap analysis, and prioritising gaps by the value of
the techniques they block from detection.

**Key concepts:**
- Auditing actual vs required logging
- Visibility-gap analysis
- Prioritising gaps by technique value

---

### Topic 4: Data Modelling and Normalisation

Disparate logs must be unified to detect across them. This topic teaches common
information models (e.g. field normalisation, ECS-style schemas), parsing, and
enrichment — turning heterogeneous logs into queryable, consistent data.

**Key concepts:**
- Common information models and field normalisation
- Parsing and enrichment
- Why normalisation enables cross-source detection

---

### Topic 5: Logging Configuration and Constraints

This topic teaches designing a logging configuration that balances detection needs
against volume, cost, retention, and performance — including what to log, at what
verbosity, and for how long.

**Key concepts:**
- Volume/cost/retention/performance trade-offs
- Verbosity and selective logging
- Retention for detection and investigation

---

### Topic 6: Australian Logging Obligations

This topic makes the Australian requirements concrete: the Essential Eight logging
expectations (e.g. application-control and patch logging, centralised time-synced
logs) and SOCI monitoring obligations, and how they shape the logging design.

**Key concepts:**
- Essential Eight logging expectations
- SOCI monitoring obligations
- Compliance-aligned logging design

**Australian context:** This topic is the Australian logging-obligation landscape
applied to detection.

---

## Labs & Exercises

### Lab 1: Log Source Coverage Audit

**Objective:** Audit an environment's log sources against an ATT&CK technique list
and identify gaps.

**Prerequisites:**
- Topics 1–3 and 6

**Environment:**
- Operating System: any (analysis lab)
- Tools: ATT&CK Navigator (v19), CTID Sensor Mappings, a Windows event-source
  reference, a worksheet — all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take a target ATT&CK technique list (e.g. an Australian-relevant actor's
   techniques).
2. For each technique, list the data sources required to detect it (Sensor
   Mappings).
3. Given an assumed Windows logging baseline, mark each technique
   Covered/Partial/Gap.
4. Identify the highest-value gaps (techniques you cannot currently detect).
5. Map the resulting coverage as a Navigator heatmap.
6. Reference the Essential Eight logging expectation relevant to a key gap.

**Expected Output:**

A technique-to-source mapping, a Covered/Partial/Gap table, a coverage heatmap, and
the Essential Eight tie-in. Learners can justify the highest-priority gap.

**Reflection Questions:**

1. Which gap blocks the most valuable detections, and what log closes it?
2. How does an Essential Eight logging expectation align with your top gap?
3. Where is logging present but not parsed usefully?

---

### Lab 2: Log Normalisation

**Objective:** Normalise log data from three sources into a common schema using
Python.

**Prerequisites:**
- Topics 4 and 5 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Python 3 (standard library + Pandas optional), sample logs from three
  sources — all free/OSS
- Minimum hardware: 2 GB RAM / 2 vCPU / 10 GB disk (within spec; no GPU)

**Instructions:**

1. Inspect three sample log sources in different formats (e.g. JSON, CSV, syslog).
2. Define a common schema (key fields: timestamp, host, user, source IP, action).
3. Write Python parsers to map each source into the common schema.
4. Normalise timestamps to UTC and reconcile field names.
5. Output a unified dataset and verify a cross-source query is now possible.
6. Note any data lost or ambiguous during normalisation.

**Expected Output:**

Three parsers producing a unified, normalised dataset queryable across sources,
with timestamps reconciled and normalisation losses documented. Learners can run a
single query spanning all three sources.

**Reflection Questions:**

1. Which field was hardest to normalise, and why does it matter for detection?
2. What did you lose in normalisation, and is that loss acceptable?
3. How does normalisation change what detections you can now write (DE03)?

---

## Assessment

### Formative Assessment: Source-to-Technique Drill

**Type:** Self-check exercise with answer key

**Description:** Given techniques, students name the required data source(s) and
the log that provides each. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Answer key with the required sources per technique.

---

### Summative Assessment: Log Engineering Plan

**Type:** Practical report

**Description:** For an assigned environment and threat profile, students (a) map
required techniques to data sources, (b) audit coverage and identify prioritised
gaps, (c) design a normalisation approach (with a working sample), and (d)
recommend a logging configuration that meets detection needs and Australian
obligations (Essential Eight/SOCI). Deliverable: 2,500–3,000 word report with a
coverage heatmap and normalisation sample.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Technique-to-source mapping & audit | LO1, LO2 |
| Normalisation design | LO3, LO4 |
| Obligations alignment | LO5 |
| Logging recommendations | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Coverage analysis | Precise, prioritised gap analysis | Sound | Partial | Weak |
| Normalisation | Robust, well-modelled schema | Adequate | Partial | Poor |
| Obligations alignment | Accurate Essential Eight/SOCI tie-in | Mostly accurate | Superficial | Absent |
| Recommendations | Prioritised, constraint-aware | Reasonable | Generic | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Logging expectations (application control, patching,
  centralised time-synced logs) drive the logging design.
- **SOCI Act 2018:** Monitoring obligations for critical infrastructure.
- **ACSC event-logging guidance:** The reference standard for the logging
  configuration.

---

## Further Reading

**Australian Cyber Security Centre (2024).** *Best Practices for Event Logging and Threat Detection.* ACSC. https://www.cyber.gov.au
> Relevance: The authoritative Australian logging guidance for Topics 5–6 (Australian source).

**MITRE ATT&CK (v19, 2026).** *Data Sources & Components.* https://attack.mitre.org/datasources/
> Relevance: The technique-to-data-source mapping used in Topic 2 and Lab 1.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Sensor Mappings to ATT&CK / Mappings Explorer.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The sensor/telemetry mapping resource used in coverage analysis.

**Elastic (2024).** *Elastic Common Schema (ECS) documentation.* https://www.elastic.co/guide/en/ecs/current/
> Relevance: A widely-used common information model supporting Topic 4 and Lab 2.

**ASD Essential Eight Maturity Model (2023).** ACSC. https://www.cyber.gov.au/essential-eight
> Relevance: The Australian logging-maturity expectations referenced in Topic 6 (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DE02 |
| Unit Title | Data Sources & Log Engineering |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Detection Engineering |
| Prerequisites | DE01, F06 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
