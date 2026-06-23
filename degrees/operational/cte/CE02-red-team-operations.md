# CE02: Red Team Operations

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (red team / emulation experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must review dual-use risk)_

---

## Overview

This unit teaches the operational discipline of red teaming: how an authorised
emulation team plans and runs an operation, manages command-and-control (C2)
infrastructure, exercises tradecraft, and maintains operational security (OPSEC) —
all within the scoped, lawful, isolated-lab framing established in CE01. The focus
is on *understanding adversary operations well enough to test and improve detection*,
not on enabling unauthorised activity: every concept is taught so a defender or an
authorised operator can reason about what an adversary does and how it is detected.

Red team operations sit at the heart of threat-informed defense — running real
adversary behaviour against an environment reveals what defenders can and cannot
see. In the Australian context this work is performed only under the authorisation
regime of CE01 (Criminal Code Act 1995 Part 10.7). CE02 builds on CE01 and OC06, and
all lab work is conducted in fully isolated environments with no external network
access. Open-source C2 frameworks are used for learning; commercial tooling (e.g.
Cobalt Strike) is referenced conceptually only.

---

## Prerequisites

- CE01 — Offensive Foundations & Ethics
- OC06 — Offensive Security Concepts

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** the phases and structure of an authorised red team operation.
2. **Apply** an open-source C2 framework in an isolated lab to understand operator
   workflow and the telemetry it generates.
3. **Evaluate** operational security (OPSEC) considerations and how attacker
   infrastructure can be fingerprinted by defenders.
4. **Analyse** common tradecraft in ATT&CK terms and the artefacts it leaves for
   detection.
5. **Design** a red team operational plan within an authorised scope.
6. **Evaluate** the defender's view of an operation to inform detection improvement.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of red team
operations, C2, and tradecraft from a detection-aware perspective.

**Skills (AQF 7.2):** Students develop technical and analytical skills by operating
in an isolated lab and analysing the detectable artefacts produced.

**Application (AQF 7.3):** Students apply red team operations within an authorised,
isolated framework to improve defensive visibility.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Exploitation Analyst (711) | AN-EXP-001 | T0591 | Conduct authorised adversary operations to test defences | Lab 1 — C2 Operator Workflow (isolated) |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Analyse the detectable artefacts of adversary operations | Lab 2 — OPSEC & Infrastructure Fingerprinting |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 4–5 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Cyber | Red Team Operations | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CE02-K01 | Knowledge of how a red team operation is structured | Topic 1 |
| Knowledge | CE02-K02 | Knowledge of command-and-control concepts | Topic 2 |
| Knowledge | CE02-K03 | Knowledge of tradecraft, ATT&CK mapping, and operational security | Topic 3; Topic 4 |
| Knowledge | CE02-K04 | Knowledge of Active Directory and lateral-movement concepts | Topic 5 |
| Skill | CE02-S01 | Skill in operating a C2 workflow in an isolated lab | Lab 1 |
| Skill | CE02-S02 | Skill in analysing OPSEC and infrastructure fingerprints | Lab 2 |
| Ability | CE02-A01 | Ability to plan an authorised red team operation | Lab 1; Topic 6 |
| Ability | CE02-A02 | Ability to reason about the detectable artefacts of operations | Lab 2; Topic 4 |
| Task | T0591 | Conduct authorised adversary operations to test defences | Lab 1 |
| Task | T0259 | Analyse the detectable artefacts of adversary operations | Lab 2 |

---

## Topics

### Topic 1: The Red Team Operation

This topic covers the structure of an authorised operation: objectives tied to the
client's questions, the operational lifecycle, team roles, deconfliction with the
client, and how success is measured by detection/response outcomes rather than
"getting in".

**Key concepts:**
- Objectives tied to defensive questions
- Operational lifecycle and team roles
- Deconfliction and success measured by detection

---

### Topic 2: Command-and-Control Concepts

This topic teaches C2 conceptually and through isolated-lab use of open-source
frameworks (e.g. Sliver, Havoc): the operator/agent model, listeners and callbacks,
and — critically — the network and host artefacts C2 generates that defenders watch
for (linking to OC02/DE/TH).

**Key concepts:**
- The C2 operator/agent model
- Listeners, callbacks, and beaconing (the defender's view)
- C2 artefacts as detection opportunities

---

### Topic 3: Tradecraft and ATT&CK

This topic frames common red team tradecraft (initial access, execution,
persistence, lateral movement) in ATT&CK (v19) terms, emphasising what each
technique leaves behind for detection — so students reason as detection-aware
operators.

**Key concepts:**
- Tradecraft mapped to ATT&CK techniques
- The artefacts each technique generates
- Detection-aware operation

---

### Topic 4: Operational Security

This topic covers OPSEC from both sides: how operators manage their footprint, and —
the defensive payoff — how attacker infrastructure and tooling can be fingerprinted
and detected (e.g. C2 profiles, certificate patterns, JA3/JA4-style fingerprints).

**Key concepts:**
- Operator OPSEC and footprint management
- Infrastructure/tooling fingerprinting (defender side)
- Turning OPSEC failures into detections

---

### Topic 5: Active Directory and Lateral Movement (Concepts)

This topic covers, at a conceptual and detection-focused level, how adversaries
abuse identity and move laterally in enterprise (AD) environments, and how those
behaviours are surfaced (e.g. BloodHound CE for attack-path analysis from the
defender's perspective).

**Key concepts:**
- Identity abuse and lateral-movement concepts
- Attack-path analysis (BloodHound CE)
- Detecting lateral movement

---

### Topic 6: Planning an Authorised Operation

This topic teaches building an operational plan within scope: objectives, the
techniques to be tested (and explicitly excluded), deconfliction, and how the plan
maps to the detection outcomes the client wants evaluated.

**Key concepts:**
- Objective-driven operational planning
- In/out technique selection within scope
- Mapping the plan to detection outcomes

---

## Labs & Exercises

### Lab 1: C2 Operator Workflow (isolated lab)

**Objective:** Use an open-source C2 framework in a fully isolated lab to understand
the operator workflow and the telemetry it generates for defenders.

**Prerequisites:**
- Topics 1–3; CE01 authorisation framing

**Environment:**
- Operating System: a **fully isolated** lab (no external network) with an attacker
  VM and a target VM you own
- Tools: an open-source C2 (Sliver or Havoc), Sysmon on the target — all free/OSS
- Minimum hardware: run sequentially — 6 GB RAM / 2 vCPU / 30 GB disk (within the
  8 GB / 4-core / 50 GB spec; no GPU). **No external network access.**

**Instructions:**

1. Confirm the lab is fully isolated and snapshot both VMs.
2. Stand up the open-source C2 and a listener in the isolated network.
3. Establish a session to the target you own and review the operator console.
4. Perform a benign post-exploitation action permitted in the lab (e.g. enumerate
   the local host) and observe the workflow.
5. On the target, capture the Sysmon/host and network telemetry the activity
   generated.
6. Map the generated artefacts to ATT&CK (v19) and note what a defender would see.

**Expected Output:**

Evidence of a C2 session in the isolated lab, the host/network telemetry the
activity generated, and an ATT&CK mapping of the detectable artefacts. Learners can
explain the defender's view of the operation and confirm isolation throughout.

**Reflection Questions:**

1. Which artefact most reliably reveals this C2 to a defender?
2. How would a detection in OC02/DE catch this beaconing?
3. Why is isolation non-negotiable for this lab?

---

### Lab 2: OPSEC & Infrastructure Fingerprinting (analysis activity)

**Objective:** Analyse how attacker infrastructure and tooling can be fingerprinted
and detected.

**Prerequisites:**
- Topics 4–5 and Lab 1

**Environment:**
- Operating System: any (analysis activity using lab-captured data and public
  fingerprinting references)
- Tools: the Lab 1 captures, ATT&CK Navigator, public C2-fingerprinting references —
  all free
- Minimum hardware: trivial

**Instructions:**

1. From the Lab 1 captures, identify the fingerprintable characteristics of the C2
   (timing, TLS/cert patterns, default profiles).
2. Research how the chosen C2's defaults are publicly fingerprinted by defenders.
3. Identify which OPSEC failures would make the operation easy to detect.
4. Map each fingerprint to a candidate detection (Sigma/Zeek — link to DE/TH).
5. Recommend how a defender would hunt for this infrastructure.
6. Summarise the detection opportunities the operation created.

**Expected Output:**

A fingerprint/OPSEC analysis with candidate detections and a defender hunt approach.
Learners can connect operator OPSEC choices to concrete detection opportunities.

**Reflection Questions:**

1. Which fingerprint is hardest for an operator to remove, and why is that good for
   defenders?
2. How does this analysis improve a detection library (DE)?
3. What is the defensive value of understanding offensive OPSEC?

---

## Assessment

### Formative Assessment: Artefact-to-ATT&CK Drill

**Type:** Self-check exercise with answer key

**Description:** Given red team actions, students identify the ATT&CK technique and
the detectable artefact each produces. Self-marked.

**Learning Outcomes Assessed:** LO4

**Feedback mechanism:** Answer key with the technique and artefact per action.

---

### Summative Assessment: Operation Plan & Detectability Report

**Type:** Practical report

**Description:** For an authorised, scoped scenario, students (a) design a red team
operational plan within scope, (b) describe the C2 and tradecraft (conceptually) to
be tested, (c) analyse the detectable artefacts and OPSEC/fingerprint exposure, and
(d) recommend the detections a defender should have. All framed within the CE01
authorisation regime. Deliverable: 2,500–3,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Operational plan | LO1, LO5 |
| C2/tradecraft (detection-aware) | LO2, LO4 |
| OPSEC & detectability | LO3 |
| Detection recommendations | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Operational understanding | Sophisticated, scope-disciplined plan | Sound | Partial | Weak |
| Detection-aware tradecraft | Every technique tied to artefacts | Mostly | Partial | Missing |
| OPSEC analysis | Insightful fingerprint/detection link | Adequate | Superficial | Poor |
| Detection recommendations | Actionable, defender-focused | Reasonable | Generic | Absent |
| Safety & ethics | Rigorous authorisation/isolation framing | Adequate | Minor gaps | Unsafe |

---

## Australian Context

This unit incorporates the following Australian context:

- **Criminal Code Act 1995 (Cth) Part 10.7:** All operations framed within the CE01
  authorisation regime.
- **ACSC advisories:** Provide realistic Australian adversary tradecraft to emulate.
- **Detection-aware framing:** Operations are evaluated by what Australian defenders
  (Essential Eight-aligned) can detect.

---

## Further Reading

**MITRE Center for Threat-Informed Defense (2024–2026).** *Adversary Emulation Library & M3TID.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: Structured emulation methodology and threat-informed-defense maturity (M3TID); see also `docs/maturity-models.md`.

**BishopFox / open-source community (2024).** *Sliver C2 documentation.* https://github.com/BishopFox/sliver
> Relevance: The free C2 framework used for isolated-lab learning in Lab 1.

**SpecterOps (2024).** *BloodHound Community Edition documentation.* https://github.com/SpecterOps/BloodHound
> Relevance: The free attack-path-analysis tool used (defensively) in Topic 5.

**Australian Cyber Security Centre (2024).** *Threat advisories.* ACSC. https://www.cyber.gov.au
> Relevance: Australian adversary tradecraft for realistic, detection-aware emulation (Australian source).

**MITRE ATT&CK (v19, 2026).** *Enterprise techniques.* https://attack.mitre.org
> Relevance: The taxonomy for framing tradecraft and its detectable artefacts.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CE02 |
| Unit Title | Red Team Operations |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Cyber Threat Emulation |
| Prerequisites | CE01, OC06 |
| Domain Expert | _Unassigned — required before Practitioner Approved (red team experience)_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved (dual-use review)_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) Part 10.7 (contextual) |
