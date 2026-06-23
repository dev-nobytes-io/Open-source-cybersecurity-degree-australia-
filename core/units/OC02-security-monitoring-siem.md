# OC02: Security Monitoring & SIEM

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit turns log data into detection. It covers how a Security Information and
Event Management (SIEM) platform ingests, normalises, and correlates telemetry,
and how analysts build and tune detections that surface adversary behaviour.
Building on the threat-informed defense paradigm from OC01, the unit treats
detection content as a living asset: as adversaries change techniques, detections,
log sources, and automation must change with them. Students learn to author
detections mapped to MITRE ATT&CK, measure their coverage, and operate the
detection lifecycle in a Security Operations Centre (SOC).

In the Australian context, effective monitoring is the operational expression of
the ACSC's *Best Practices for Event Logging and Threat Detection* and supports
the incident-reporting obligations of the NDB scheme and SOCI Act. OC02 depends on
F06 (Data & Log Analysis) and OC01 (Adversary Tradecraft) and feeds directly into
OC04 (Incident Response) and the Detection Engineering and Threat Hunting majors.

---

## Prerequisites

- F06 — Data & Log Analysis
- OC01 — Adversary Tradecraft & TTPs

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** SIEM architecture: collection, parsing, normalisation, storage,
   correlation, alerting, and the role of detection content.
2. **Apply** detection engineering practice to author rules (e.g. Sigma) mapped to
   MITRE ATT&CK techniques.
3. **Analyse** alerts to triage true vs false positives and tune detections to
   reduce noise without losing coverage.
4. **Apply** threat-informed defense to measure and improve detection coverage
   against prioritised techniques.
5. **Examine** the SOC operating model — alert pipelines, severity, escalation,
   and the detection lifecycle.
6. **Analyse** a detection gap and recommend changes to logging, detections, or
   automation to close it.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of monitoring
architecture, detection engineering, and SOC operations.

**Skills (AQF 7.2):** Students develop technical skills by authoring and tuning
detections and analytical skills by triaging alerts and measuring coverage.

**Application (AQF 7.3):** Students apply these skills in a SIEM lab that mirrors
SOC practice, relating their work to Australian logging guidance and reporting
obligations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0166 | Perform event correlation to gain situational awareness and detect threats | Lab 1 — Building Detections in a SIEM |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0259 | Identify and analyse anomalous network/host activity and tune detections | Lab 2 — Detection Coverage & Tuning |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 4 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 3 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Security Monitoring | Practitioner | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | OC02-K01 | Knowledge of SIEM architecture and the collection→parse→normalise→store→detect pipeline | Topic 1 |
| Knowledge | OC02-K02 | Knowledge of detection engineering and detection-as-code (e.g. Sigma) | Topic 2 |
| Knowledge | OC02-K03 | Knowledge of behaviour-based detection and how to measure coverage | Topic 3; Topic 5 |
| Knowledge | OC02-K04 | Knowledge of the SOC operating model — alert pipeline, severity, and escalation | Topic 6 |
| Skill | OC02-S01 | Skill in authoring SIEM detection rules mapped to ATT&CK techniques | Lab 1 |
| Skill | OC02-S02 | Skill in triaging alerts and tuning detections to reduce false positives | Lab 2 |
| Ability | OC02-A01 | Ability to measure and improve detection coverage using threat-informed defense | Lab 2; Topic 5 |
| Ability | OC02-A02 | Ability to recommend logging or detection changes to close a detection gap | Summative |
| Task | T0166 | Perform event correlation to gain situational awareness and detect threats | Lab 1 |
| Task | T0259 | Identify and analyse anomalous network/host activity and tune detections | Lab 2 |

---

## Topics

### Topic 1: SIEM Architecture and the Data Pipeline

A SIEM is a pipeline: collect telemetry, parse and normalise it to a schema,
store and index it, correlate across sources, and alert. This topic covers each
stage, the trade-offs of data volume vs fidelity, the importance of a common
information model, and why parsing/normalisation quality determines detection
quality. It frames the SIEM as the place where F06's log analysis becomes
continuous detection.

**Key concepts:**
- Collection → parsing/normalisation → storage → correlation → alerting
- Common information models and field normalisation
- Volume, cost, and retention trade-offs

---

### Topic 2: Detection Engineering and Detection-as-Code

Detections are software and should be engineered like it. This topic introduces
detection engineering: writing detections from a hypothesis about adversary
behaviour, expressing them portably with **Sigma**, version-controlling them
(detection-as-code), and testing them. Every detection is mapped to the ATT&CK
technique(s) it targets, making coverage measurable.

**Key concepts:**
- From behavioural hypothesis to detection logic
- Sigma as a portable, vendor-neutral detection format
- Detection-as-code: version control, review, and testing

---

### Topic 3: Robust, Behaviour-Based Detection

Building on the Pyramid of Pain (OC01), this topic teaches detections that target
durable behaviour rather than brittle indicators. It draws on CTID's *Summiting
the Pyramid* to assess how robust an analytic is — how hard it would be for an
adversary to evade — and pushes students to write detections that survive tool and
infrastructure changes.

**Key concepts:**
- Brittle (indicator) vs robust (behaviour) detections
- CTID *Summiting the Pyramid* analytic-robustness scoring
- Designing detections resistant to adversary evasion

---

### Topic 4: Alert Triage and Tuning

A SOC drowns in alerts unless detections are tuned. This topic covers the triage
workflow (validate, scope, decide), distinguishing true positives from false
positives, and the discipline of tuning — reducing noise without creating blind
spots. It introduces precision/recall thinking and the cost of both missed
detections and alert fatigue.

**Key concepts:**
- The triage workflow and enrichment
- True/false positives, precision vs recall, and the cost of each
- Tuning without losing coverage

---

### Topic 5: Measuring Coverage with Threat-Informed Defense

Threat-informed defense demands that coverage be measured, not assumed. This topic
applies CTID tooling — ATT&CK Navigator for coverage heatmaps, Sensor Mappings /
Mappings Explorer to verify the telemetry behind each detection, and Top ATT&CK
Techniques and M3TID to prioritise and assess maturity. Students learn to answer
"which techniques can we actually detect, and which matter most?"

**Key concepts:**
- Coverage heatmaps in ATT&CK Navigator
- Verifying telemetry with Sensor Mappings / Mappings Explorer
- Prioritisation (Top ATT&CK Techniques) and maturity (M3TID)

**Australian context:** Coverage measurement aligns monitoring with the
behaviours highlighted in ACSC advisories.

---

### Topic 6: The SOC Operating Model and the Living Detection Lifecycle

Detection is not a project but a continuous lifecycle. This topic covers the SOC
operating model (tiers or tier-less, alert pipelines, severity, escalation,
hand-off to incident response) and the detection lifecycle: propose → build →
test → deploy → tune → retire. It closes the loop the unit has built toward —
adversary change drives detection change, supported by automation — making the
SOC a living system.

**Key concepts:**
- SOC operating models and escalation to IR (OC04)
- The detection lifecycle as a continuous loop
- Automation (SOAR-style) to sustain the loop at scale

**Australian context:** Connects to ACSC logging/detection guidance and to the
hand-off into NDB/SOCI-relevant incident response.

---

## Labs & Exercises

### Lab 1: Building Detections in a SIEM

**Objective:** Ingest telemetry into a free SIEM, author ATT&CK-mapped detections,
and validate them against simulated adversary activity.

**Prerequisites:**
- Topics 1–3 and F06

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: a free SIEM/log platform (OpenSearch or Splunk Free), Sigma + a Sigma
  converter (sigma-cli), sample telemetry (Sysmon-style + auth logs) — all free
- Minimum hardware: 6 GB RAM / 2 vCPU / 30 GB disk (within the 8 GB / 4-core /
  50 GB spec; single-node; no GPU)

**Instructions:**

1. Ingest the provided endpoint (process-creation) and authentication telemetry
   into the platform; confirm fields are parsed.
2. Pick two ATT&CK techniques present in the data (e.g. T1059 Command and
   Scripting Interpreter, T1053 Scheduled Task/Job).
3. Write a Sigma rule for each, tagged with its ATT&CK technique ID.
4. Convert the Sigma rules to the platform's query language and run them.
5. Confirm each detection fires on the malicious activity and record the matching
   events as evidence.
6. Commit the Sigma rules to a Git repo (detection-as-code).

**Expected Output:**

Two ATT&CK-tagged Sigma rules that fire correctly on the sample data, their
converted queries, evidence of the matches, and a Git history. Learners can
explain the behaviour each rule targets.

**Reflection Questions:**

1. Where do your two detections sit on the Pyramid of Pain, and how robust are
   they to evasion?
2. Why does expressing detections in Sigma (rather than a single vendor's syntax)
   matter operationally?
3. What telemetry would you lose detection of if endpoint logging were disabled?

---

### Lab 2: Detection Coverage & Tuning

**Objective:** Measure detection coverage against a threat profile, tune a noisy
detection, and recommend changes to close the most important gap.

**Prerequisites:**
- Topics 4, 5, and 6 and Lab 1

**Environment:**
- Operating System: as Lab 1
- Tools: the SIEM from Lab 1, ATT&CK Navigator, CTID Top ATT&CK Techniques /
  Sensor Mappings (free)
- Minimum hardware: as Lab 1

**Instructions:**

1. Build a Navigator layer of the techniques in a chosen threat profile (reuse an
   Australian-relevant actor from OC01).
2. Mark which techniques your current detections cover; produce a coverage
   heatmap.
3. Take a deliberately noisy detection (high false-positive rate in the sample
   data) and tune it; record before/after true- and false-positive counts.
4. Use Sensor Mappings to identify the telemetry needed for one uncovered
   high-priority technique.
5. Recommend one new log source, one new detection, and one automation to close
   the highest-priority gap.
6. Re-state the coverage after your recommendations as a target heatmap.

**Expected Output:**

A current and target coverage heatmap, a documented tuning result (false
positives reduced without losing the true positive), and three justified
gap-closing recommendations. Learners can defend why their priority gap matters
most.

**Reflection Questions:**

1. How did tuning trade off precision and recall, and how did you decide the
   balance?
2. Which uncovered technique would you prioritise, and what does threat-informed
   defense say about that choice?
3. How would you automate re-measuring coverage so the SOC keeps pace with a
   changing adversary?

---

## Assessment

### Formative Assessment: Detection Logic Review

**Type:** Peer/self review exercise with answer key

**Description:** Students review a set of draft detections and identify, for each,
the ATT&CK technique targeted, its robustness on the Pyramid of Pain, and a likely
false-positive source. Self- or peer-marked against a key.

**Learning Outcomes Assessed:** LO2, LO3

**Feedback mechanism:** Answer key with the intended technique, robustness rating,
and known false-positive sources for each detection.

---

### Summative Assessment: SOC Detection Coverage Report

**Type:** Practical report

**Description:** Given a SIEM dataset, a threat profile, and an assumed logging
baseline, students must (a) author at least three ATT&CK-mapped detections, (b)
measure current coverage and present a heatmap, (c) triage and tune a provided
noisy detection with before/after metrics, and (d) recommend a prioritised set of
logging, detection, and automation changes framed as a continuous lifecycle.
Deliverable: 2,000–2,500 word report with a Git repo of detections and
Navigator artefacts.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Authored ATT&CK-mapped detections | LO1, LO2 |
| Coverage measurement & heatmap | LO4 |
| Triage & tuning with metrics | LO3 |
| Prioritised gap-closing recommendations | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Detection quality | Robust, correct, well-mapped, behaviour-based | Correct detections, mostly robust | Detections work but brittle/mis-mapped | Detections incorrect or unmapped |
| Coverage analysis | Precise, prioritised, threat-informed | Solid coverage analysis | Partial or generic analysis | Little meaningful analysis |
| Triage & tuning | Clear metrics; noise cut without losing coverage | Effective tuning with metrics | Some tuning; weak metrics | Ineffective or unmeasured tuning |
| Lifecycle framing | Detection treated as a continuous, automated loop | Adequate lifecycle awareness | Superficial lifecycle mention | Treats detection as one-off |
| Communication | Clear, structured, evidence-linked | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC *Best Practices for Event Logging and Threat Detection*:** The reference
  standard for the telemetry and detection practices in both labs.
- **ACSC advisories:** Source of Australian-relevant threat profiles for coverage
  measurement.
- **NDB scheme & SOCI Act:** The downstream reporting obligations that effective
  detection and the hand-off to incident response support.

---

## Further Reading

**SigmaHQ (2024).** *Sigma — Generic Signature Format for SIEM Systems.* https://github.com/SigmaHQ/sigma
> Relevance: The portable detection format authored and converted throughout this unit; free/OSS.

**MITRE Center for Threat-Informed Defense (2024).** *Summiting the Pyramid, Sensor Mappings to ATT&CK, Mappings Explorer, M3TID.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The CTID research used to build robust detections and measure coverage in Topics 3 and 5.

**Australian Cyber Security Centre (2024).** *Best Practices for Event Logging and Threat Detection.* ACSC. https://www.cyber.gov.au
> Relevance: The authoritative Australian guidance underpinning telemetry and detection design (Australian source).

**Roberts, S. & Brown, R. (2017).** *Intelligence-Driven Incident Response.* O'Reilly.
> Relevance: Connects detection and monitoring to the threat-intelligence and IR lifecycle (OC04/OC05).

**Bianco, D. & Cole, C. / Elastic & community (2023).** *Detection Engineering practices and the Detection Maturity Model.* (Freely available community resources.)
> Relevance: Practical grounding in the detection lifecycle and maturity discussed in Topic 6.

**Rob van Os (2024).** *SOC-CMM — SOC Capability Maturity Model.* https://www.soc-cmm.com
> Relevance: The maturity model used to assess and mature security-monitoring capability; this unit's SOC services feed the program-level maturity aggregation in `docs/maturity-models.md` (capability → CSF → NICE/DCWF role → KSATs).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | OC02 |
| Unit Title | Security Monitoring & SIEM |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Operational Core |
| Major / Pathway | Operational |
| Prerequisites | F06, OC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | Privacy Act 1988 (NDB); Security of Critical Infrastructure Act 2018 (contextual) |
