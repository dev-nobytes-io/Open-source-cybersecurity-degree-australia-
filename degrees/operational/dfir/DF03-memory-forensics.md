# DF03: Memory Forensics

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Memory holds evidence that exists nowhere else: running processes, injected code,
decrypted data, credentials, and live network connections. This unit teaches
forensic memory analysis with Volatility 3 — acquiring memory soundly, enumerating
processes and detecting injection, recovering credentials and network artefacts,
and extracting memory-resident indicators of compromise. The forensic framing
(integrity, repeatability, admissibility) distinguishes this from the hunting view
in the Threat Hunting major.

Memory forensics is decisive in modern intrusions where adversaries operate
fileless or in-memory to evade disk forensics. In the Australian context, memory
evidence is subject to the same *Evidence Act 1995* integrity expectations as disk
evidence, and what is recovered (e.g. exposed credentials or data) directly informs
NDB impact assessments. DF03 builds on DF01–DF02 and OC03 (Malware Analysis), and
feeds DF05 and the capstone DF06.

---

## Prerequisites

- DF02 — Host Forensics
- OC03 — Malware Analysis Fundamentals

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** sound memory-acquisition practices and verify image integrity.
2. **Analyse** processes and their relationships in a memory image to identify
   anomalies.
3. **Analyse** memory for process and code injection (e.g. T1055).
4. **Apply** techniques to recover credentials, network connections, and artefacts
   from memory.
5. **Evaluate** memory-resident indicators to determine adversary activity.
6. **Recommend** findings and IOCs derived from memory analysis in a defensible
   manner.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of volatile-memory
structures and analysis techniques.

**Skills (AQF 7.2):** Students develop technical and analytical skills by analysing
memory images for injection, credentials, and network artefacts.

**Application (AQF 7.3):** Students apply memory forensics to realistic images and
produce defensible findings and IOCs.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0432 | Perform memory analysis to determine malicious activity | Lab 1 — Process & Injection Analysis |
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0396 | Recover artefacts and IOCs to support the investigation | Lab 2 — Credentials & Network Artefacts |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Systems & software life cycle / assurance | SURE | Level 4–5 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Incident Management | Digital Forensics | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | DF03-K01 | Knowledge of memory acquisition and integrity | Topic 1 |
| Knowledge | DF03-K02 | Knowledge of process analysis in memory | Topic 2 |
| Knowledge | DF03-K03 | Knowledge of detecting code and process injection | Topic 3 |
| Knowledge | DF03-K04 | Knowledge of recovering credentials and network/handle artefacts from memory | Topic 4; Topic 5 |
| Skill | DF03-S01 | Skill in analysing processes and injection in memory | Lab 1 |
| Skill | DF03-S02 | Skill in recovering credentials and network artefacts | Lab 2 |
| Ability | DF03-A01 | Ability to identify in-memory-only adversary activity | Lab 1; Topic 3 |
| Ability | DF03-A02 | Ability to derive memory IOCs and defensible findings | Topic 6; Summative |
| Task | T0432 | Perform memory analysis to determine malicious activity | Lab 1 |
| Task | T0396 | Recover artefacts and IOCs to support the investigation | Lab 2 |

---

## Topics

### Topic 1: Memory Acquisition and Integrity

This topic covers acquiring memory soundly (live acquisition tools, the smearing/
consistency problem), the order-of-volatility rationale for capturing memory early,
and hashing the image for integrity — the memory counterpart to DF02's imaging.

**Key concepts:**
- Live memory acquisition and its challenges
- Why memory is captured early (volatility)
- Integrity and documentation of memory images

---

### Topic 2: Process Analysis

This topic teaches enumerating processes from memory, reconstructing parent-child
relationships, detecting hidden/unlinked processes, and spotting anomalies
(unexpected parents, masquerading names, suspicious paths).

**Key concepts:**
- Process listing and reconstruction from memory
- Hidden/unlinked process detection
- Masquerading and lineage anomalies

---

### Topic 3: Detecting Code and Process Injection

Injection is the hallmark of evasive malware. This topic teaches detecting injected
and hollowed processes, suspicious memory regions (RWX, unbacked executable
memory), and reflectively-loaded code — mapping to ATT&CK process injection
(T1055).

**Key concepts:**
- Process injection/hollowing detection
- Suspicious memory regions (RWX/unbacked)
- Reflective/in-memory code loading

---

### Topic 4: Recovering Credentials and Secrets

This topic covers recovering authentication material and secrets from memory
(cached credentials, tokens, keys) and what their presence implies for scope and
NDB impact — handled within the legal/privacy constraints from DF01.

**Key concepts:**
- Credential/secret recovery from memory
- Scope and impact implications
- Handling recovered secrets lawfully and securely

**Australian context:** Recovered credentials/data feed NDB "serious harm"
assessments and must be handled per Privacy Act obligations.

---

### Topic 5: Network and Handle Artefacts

This topic teaches recovering network connections, listening sockets, open handles,
loaded modules, and command-line arguments from memory to establish C2 and
adversary actions when disk/network logs are missing.

**Key concepts:**
- Network connections and sockets from memory
- Handles, modules, and command lines
- Corroborating C2 from memory evidence

---

### Topic 6: Memory IOCs and Defensible Findings

This topic teaches extracting durable indicators from memory, distinguishing
fact from inference, stating confidence, and documenting the method so findings are
repeatable and admissibility-aware (linking to DF01).

**Key concepts:**
- Extracting and prioritising memory IOCs
- Fact vs inference and confidence
- Repeatable, admissibility-aware documentation

**Australian context:** Findings meet the Evidence Act 1995 standard and feed NDB
assessments.

---

## Labs & Exercises

### Lab 1: Process & Injection Analysis

**Objective:** Analyse a memory image to enumerate processes and detect injection.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Volatility 3, a provided memory image with injection — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 30 GB disk (within the 8 GB / 4-core /
  50 GB spec; no GPU)

**Instructions:**

1. Load the memory image in Volatility 3 and record its hash.
2. Enumerate processes and reconstruct parent-child relationships; flag anomalies.
3. Run injection-detection (e.g. malfind) to find suspicious memory regions.
4. Identify the injected/affected process and the technique (T1055).
5. Examine loaded modules and command lines for the suspect process.
6. Record evidence-linked findings and map to ATT&CK (v19).

**Expected Output:**

A process analysis flagging anomalies, an identified injected process with
supporting evidence, and ATT&CK mappings. Learners can explain why the flagged
region indicates injection.

**Reflection Questions:**

1. Why would this evidence be absent from a disk image?
2. How confident are you in the injection finding, and on what basis?
3. How would you preserve this memory evidence to satisfy the Evidence Act 1995?

---

### Lab 2: Credentials & Network Artefacts

**Objective:** Recover credentials and network artefacts from memory and assess
their impact.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Volatility 3 (relevant plugins) — all free/OSS
- Minimum hardware: as Lab 1

**Instructions:**

1. From the memory image, enumerate network connections and listening sockets.
2. Identify suspicious external connections (potential C2) and the owning process.
3. Recover credential material/secrets present in memory.
4. Assess what the recovered material implies for incident scope and NDB impact.
5. Document handling of the recovered secrets per Privacy Act obligations.
6. Summarise findings and IOCs with confidence statements.

**Expected Output:**

Recovered network artefacts (with the C2 candidate and owning process), recovered
credential evidence, an impact/NDB assessment, and documented lawful handling.
Learners can connect the memory evidence to the broader incident.

**Reflection Questions:**

1. How do memory network artefacts corroborate (or fill gaps in) network logs?
2. What does the recovered credential material mean for the breach's scope?
3. How did you handle the recovered secrets to stay within Privacy Act obligations?

---

## Assessment

### Formative Assessment: Memory Anomaly Drill

**Type:** Self-check exercise with answer key

**Description:** Given Volatility output excerpts, students identify anomalies
(injection, hidden processes, suspicious connections) and state the evidence.
Self-marked.

**Learning Outcomes Assessed:** LO2, LO3

**Feedback mechanism:** Answer key with the anomaly and evidence per excerpt.

---

### Summative Assessment: Memory Forensic Report

**Type:** Practical report

**Description:** Given a memory image with planted adversary activity, students (a)
verify integrity, (b) analyse processes and detect injection, (c) recover
credentials and network artefacts, and (d) produce a defensible report with
evidence, confidence, IOCs, ATT&CK mappings, and an NDB impact note. Deliverable:
2,500–3,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Acquisition/integrity | LO1 |
| Process & injection analysis | LO2, LO3 |
| Credentials & network recovery | LO4 |
| Findings, IOCs, impact | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Memory analysis | Thorough, accurate, well-evidenced | Solid | Partial | Inaccurate |
| Injection detection | Correct with strong evidence | Adequate | Weak | Incorrect/missing |
| Artefact recovery | Effective credential/network recovery + impact | Adequate | Partial | Poor |
| Defensible findings | Fact/inference clear; admissibility-aware | Mostly clear | Inconsistent | Poor |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Evidence Act 1995 (Cth):** Memory acquisition and findings written to the
  admissibility standard.
- **Privacy Act 1988 & NDB:** Recovered credentials/data handled lawfully and used
  to assess breach impact.
- **Australian breach case studies:** Used to frame in-memory/fileless intrusion
  scenarios.

---

## Further Reading

**The Volatility Foundation (2024).** *Volatility 3 Documentation.* https://volatility3.readthedocs.io
> Relevance: The free memory-forensics framework used throughout this unit.

**Ligh, M. et al. (2014).** *The Art of Memory Forensics.* Wiley.
> Relevance: The definitive reference on memory analysis underpinning every topic.

**MITRE ATT&CK (v19, 2026).** *Process Injection (T1055) and related techniques.* https://attack.mitre.org
> Relevance: The technique reference for the injection behaviour analysed in Lab 1.

**Office of the Australian Information Commissioner (2024).** *Data breach assessment guidance.* OAIC. https://www.oaic.gov.au
> Relevance: Connects recovered memory evidence to NDB impact assessment (Australian source).

**SANS DFIR (2024).** *Memory forensics references.* SANS Institute. https://www.sans.org/posters/
> Relevance: Freely available practical references for memory analysis workflows.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DF03 |
| Unit Title | Memory Forensics |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | DFIR |
| Prerequisites | DF02, OC03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Evidence Act 1995 (Cth); Privacy Act 1988 (NDB) |
