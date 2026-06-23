# TH03: Host-Based Hunting

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches hunting on the endpoint — where execution, persistence, and
privilege escalation leave their richest evidence. Students learn to hunt across
process activity, persistence mechanisms, and memory, using free endpoint tooling
(Velociraptor for fleet queries, Volatility 3 for memory) and Sysmon/EVTX
telemetry. The emphasis is analyst-level interpretation: distinguishing malicious
from benign on real hosts, where attackers deliberately blend in.

Host hunting operationalises the threat-informed-defense spine: hunts target the
ATT&CK (v19) techniques that manifest on hosts — execution (T1059), scheduled
tasks/services (T1053/T1543), process injection (T1055), and persistence
(T1547) — and findings convert into Sigma detections (OC02). In the Australian
context, host hunting surfaces Essential Eight control bypasses (application
control, restricting macros, admin privileges). TH03 builds on TH01–TH02, F02
(Operating Systems), and OC03 (Malware Analysis).

---

## Prerequisites

- TH02 — ATT&CK for Hunters
- F02 — Operating Systems & Administration
- OC03 — Malware Analysis Fundamentals

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** process and parent-child relationships to identify anomalous
   execution on a host.
2. **Analyse** persistence mechanisms (services, scheduled tasks, autoruns,
   registry run keys) for adversary footholds.
3. **Apply** memory analysis with Volatility 3 to detect process injection and
   hidden artefacts.
4. **Apply** Velociraptor VQL to hunt host artefacts across an endpoint fleet.
5. **Evaluate** host findings to distinguish malicious activity from benign
   administrative behaviour.
6. **Recommend** detections derived from host hunt findings, mapped to ATT&CK.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of host
artefacts, persistence, and memory forensics for hunting.

**Skills (AQF 7.2):** Students develop technical and analytical skills by querying
endpoints and interpreting host evidence.

**Application (AQF 7.3):** Students apply host hunting to realistic endpoints and
convert findings into defensive improvements.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Analyse host/endpoint data to identify anomalous and malicious activity | Lab 1 — Host Artefact & Persistence Hunt |
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0432 | Perform memory analysis to identify injection and hidden artefacts | Lab 2 — Memory Hunt with Volatility 3 |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Security operations | SCAD | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Threat Hunting | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | TH03-K01 | Knowledge of the host as a hunting ground and its key artefacts | Topic 1 |
| Knowledge | TH03-K02 | Knowledge of hunting execution and living-off-the-land behaviour | Topic 2 |
| Knowledge | TH03-K03 | Knowledge of persistence mechanisms and how to hunt them | Topic 3 |
| Knowledge | TH03-K04 | Knowledge of memory forensics and fleet-scale hunting techniques | Topic 4; Topic 5 |
| Skill | TH03-S01 | Skill in hunting host artefacts and persistence | Lab 1 |
| Skill | TH03-S02 | Skill in performing a memory hunt with Volatility 3 | Lab 2 |
| Ability | TH03-A01 | Ability to distinguish benign from malicious host activity at scale | Lab 1; Topic 2 |
| Ability | TH03-A02 | Ability to convert host findings into detections | Topic 6; Summative |
| Task | T0259 | Analyse host/endpoint data to identify anomalous and malicious activity | Lab 1 |
| Task | T0432 | Perform memory analysis to identify injection and hidden artefacts | Lab 2 |

---

## Topics

### Topic 1: The Host as a Hunting Ground

This topic surveys host telemetry and artefacts: process creation (Sysmon Event
ID 1 / Security 4688), parent-child lineage, command lines, image loads, and the
file/registry footprint. It frames the host as where most ATT&CK techniques
ultimately execute.

**Key concepts:**
- Host telemetry sources (Sysmon, EVTX, EDR)
- Process lineage and command-line analysis
- The execution/persistence footprint

---

### Topic 2: Hunting Execution and Living-off-the-Land

Adversaries increasingly abuse legitimate binaries (LOLBins) and interpreters.
This topic teaches hunting execution behaviour — suspicious PowerShell, script
interpreters (T1059), LOLBin abuse, and anomalous parent-child chains (e.g. Office
spawning a shell) — and distinguishing it from legitimate use.

**Key concepts:**
- Command and scripting interpreter abuse (T1059)
- LOLBins and signed-binary proxy execution
- Anomalous process lineage

**Australian context:** Macro and script abuse maps to Essential Eight
mitigations (restrict macros, application control).

---

### Topic 3: Hunting Persistence

This topic covers the persistence locations attackers favour — services (T1543),
scheduled tasks (T1053), registry run keys and startup (T1547), WMI subscriptions —
and how to enumerate and triage them at scale to find the one malicious entry among
thousands of legitimate ones.

**Key concepts:**
- Persistence mechanisms across Windows/Linux
- Enumerating and baselining persistence
- Triage: rare and recently-created entries

---

### Topic 4: Memory Forensics for Hunting

Some evidence lives only in memory. This topic teaches Volatility 3 to hunt for
process injection (T1055), hidden/unlinked processes, injected code, and
suspicious network connections from memory images.

**Key concepts:**
- Acquiring and analysing memory images
- Detecting process injection and hollowing
- Memory-resident network and handle artefacts

---

### Topic 5: Fleet-Scale Hunting with Velociraptor

Hunting one host does not scale. This topic teaches Velociraptor and VQL to run
the same hunt across many endpoints — collecting artefacts, hunting persistence,
and stacking results to surface outliers across the fleet.

**Key concepts:**
- Velociraptor architecture and VQL basics
- Fleet-wide artefact collection
- Stacking/frequency analysis across hosts

---

### Topic 6: From Host Findings to Detections

This topic closes the loop: turning a confirmed host hunt finding into a durable
Sigma detection (OC02), choosing behaviour-based logic over brittle indicators, and
documenting the finding for intelligence and IR.

**Key concepts:**
- Host finding → Sigma detection
- Behaviour over indicator (Pyramid of Pain)
- Documentation and hand-off

**Australian context:** Detections target Essential Eight-relevant host behaviours.

---

## Labs & Exercises

### Lab 1: Host Artefact & Persistence Hunt

**Objective:** Hunt host execution and persistence artefacts across endpoints using
Velociraptor VQL and triage findings.

**Prerequisites:**
- Topics 1–3 and 5

**Environment:**
- Operating System: Velociraptor server + 1–2 Windows endpoint VMs (eval), or the
  provided Velociraptor offline collection
- Tools: Velociraptor (VQL), Sysmon, ATT&CK Navigator — all free/OSS
- Minimum hardware: run components sequentially — 6 GB RAM / 2 vCPU / 30 GB disk
  (within the 8 GB / 4-core / 50 GB spec; no GPU)

**Instructions:**

1. Deploy/connect Velociraptor to the endpoint(s) (or load the offline collection).
2. Run a VQL query to collect scheduled tasks and registry run keys across hosts.
3. Stack the results and identify rare or recently-created entries.
4. Investigate one suspicious persistence entry and confirm or clear it.
5. Run a VQL query for anomalous process lineage (e.g. Office → shell).
6. Map each confirmed finding to its ATT&CK (v19) technique.

**Expected Output:**

VQL query results, a stacked persistence analysis identifying an outlier, an
investigated finding with a verdict, and ATT&CK mappings. Learners can justify the
malicious/benign verdict with evidence.

**Reflection Questions:**

1. How did stacking across hosts surface the outlier you found?
2. Which finding was hardest to call malicious vs benign, and why?
3. Which finding warrants a durable detection, and what would it target?

---

### Lab 2: Memory Hunt with Volatility 3

**Objective:** Use Volatility 3 to detect process injection and hidden artefacts in
a memory image.

**Prerequisites:**
- Topic 4 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM with Volatility 3
- Tools: Volatility 3, a provided memory image containing injection — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 25 GB disk (within spec; no GPU)

**Instructions:**

1. Load the provided memory image in Volatility 3.
2. List processes and identify suspicious parent-child relationships or anomalies.
3. Run injection-detection plugins (e.g. malfind) to find injected code regions.
4. Identify the injected/affected process and the likely technique (T1055).
5. Examine network artefacts in memory for suspicious connections.
6. Document findings and map them to ATT&CK.

**Expected Output:**

A Volatility analysis identifying the injected process and supporting evidence,
network artefacts, and an ATT&CK mapping. Learners can explain why the flagged
region indicates injection.

**Reflection Questions:**

1. Why is some of this evidence only visible in memory?
2. How would you turn this finding into a detection at the endpoint telemetry
   level?
3. What are the limits of memory hunting at fleet scale?

---

## Assessment

### Formative Assessment: Malicious-or-Benign Triage

**Type:** Self-check exercise with answer key

**Description:** Given host artefacts (process trees, persistence entries, command
lines), students classify each as malicious/benign/needs-more-data and justify it.
Self-marked.

**Learning Outcomes Assessed:** LO1, LO5

**Feedback mechanism:** Answer key with the verdict and reasoning for each artefact.

---

### Summative Assessment: Host Hunt Report

**Type:** Practical report

**Description:** Given an endpoint dataset (Velociraptor collection + a memory
image) containing planted adversary activity, students (a) hunt execution and
persistence, (b) perform memory analysis for injection, (c) confirm findings with
verdicts and ATT&CK mappings, and (d) recommend at least two Sigma detections.
Deliverable: 2,500–3,000 word report with query evidence and detections.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Execution & persistence hunt | LO1, LO2 |
| Memory analysis | LO3 |
| Fleet querying (VQL) | LO4 |
| Verdicts & detections | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Host analysis | Thorough, accurate, well-evidenced | Solid with minor gaps | Partial | Inaccurate |
| Memory forensics | Correct injection finding with evidence | Adequate analysis | Weak | Incorrect/missing |
| Verdict quality | Sound malicious/benign judgement | Mostly sound | Inconsistent | Poor |
| Detections | Robust, behaviour-based, mapped | Workable | Brittle | Missing |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Host hunts target macro/script abuse, application-control
  bypass, and admin-privilege misuse.
- **ACSC advisories:** Provide realistic host-level TTPs for hunt scenarios.
- **SOCI Act 2018:** Host detection capability framed as support for
  critical-infrastructure obligations.

---

## Further Reading

**The Volatility Foundation (2024).** *Volatility 3 Documentation.* https://volatility3.readthedocs.io
> Relevance: The free memory-analysis tool and reference used in Lab 2.

**Velociraptor / Rapid7 (2024).** *Velociraptor Documentation & VQL reference.* https://docs.velociraptor.app
> Relevance: The free endpoint-hunting platform and query language used in Labs 1 and the summative.

**MITRE ATT&CK (v19, 2026).** *Enterprise techniques (Execution, Persistence, Defense Evasion).* https://attack.mitre.org
> Relevance: The technique reference for host-based behaviours hunted in this unit.

**Australian Cyber Security Centre (2024).** *Essential Eight & host hardening guidance / advisories.* ACSC. https://www.cyber.gov.au
> Relevance: Australian control and threat context for host hunting (Australian source).

**Sikorski, M. & Honig, A. (2012).** *Practical Malware Analysis.* No Starch Press.
> Relevance: Deep grounding in the host/memory behaviours hunted here, complementing OC03.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | TH03 |
| Unit Title | Host-Based Hunting |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Threat Hunting |
| Prerequisites | TH02, F02, OC03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
