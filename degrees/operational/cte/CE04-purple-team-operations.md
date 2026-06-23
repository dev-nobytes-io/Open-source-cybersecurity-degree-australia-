# CE04: Purple Team Operations

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (red/purple team experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must review dual-use risk)_

---

## Overview

Purple teaming is where emulation delivers its greatest defensive value: red and
blue work *together* so that every emulated technique either confirms a detection or
produces a new one. This unit teaches collaborative testing — running techniques
with the detection team watching, analysing the detection gaps revealed, and feeding
improvements straight back into detection engineering and hunting. It is the
operational embodiment of threat-informed defense as a continuous loop, and the
point at which the offensive and defensive halves of the degree meet.

Purple teaming directly improves an organisation's measurable capability maturity
(SOC-CMM, DML/M3TID — see `docs/maturity-models.md`): a recurring purple-team cadence
is one of the strongest drivers of detection maturity. In the Australian context,
exercises emulate ACSC-reported actors and target Essential Eight-relevant detection.
CE04 builds on CE03, DE04 (Adversary Simulation for Detection), and OC06, and feeds
the CE06 capstone.

---

## Prerequisites

- CE03 — ATT&CK-Based Emulation
- DE04 — Adversary Simulation for Detection (or equivalent detection knowledge)

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** the purple-team model and how it differs from siloed red/blue work.
2. **Apply** collaborative testing to run techniques jointly with a detection team.
3. **Analyse** detection gaps revealed by a purple-team exercise and their root
   causes.
4. **Design** a purple-team exercise that targets a prioritised set of techniques.
5. **Evaluate** detection coverage outcomes and prioritise improvements.
6. **Recommend** a continuous purple-team cadence to mature detection capability.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of collaborative
purple-team operations and detection-gap analysis.

**Skills (AQF 7.2):** Students develop analytical and collaborative skills by running
exercises and diagnosing gaps.

**Application (AQF 7.3):** Students apply purple teaming to improve and mature
detection capability against Australian-relevant threats.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Validate and improve detections through collaborative testing | Lab 1 — Purple Team Exercise |
| NIST NICE DCWF | 2023 | Exploitation Analyst (711) | AN-EXP-001 | T0591 | Execute techniques jointly to reveal detection gaps | Lab 2 — Detection Gap Analysis |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 4–5 | Lab 1 |
| Security operations | SCAD | Level 4 | Lab 1, Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Cyber | Purple Team Operations | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CE04-K01 | Knowledge of the purple-team model | Topic 1 |
| Knowledge | CE04-K02 | Knowledge of running a collaborative exercise | Topic 2 |
| Knowledge | CE04-K03 | Knowledge of detection gap analysis and exercise design | Topic 3; Topic 4 |
| Knowledge | CE04-K04 | Knowledge of turning gaps into improvements and continuous maturity | Topic 5; Topic 6 |
| Skill | CE04-S01 | Skill in running a collaborative purple-team exercise | Lab 1 |
| Skill | CE04-S02 | Skill in performing detection gap analysis | Lab 2 |
| Ability | CE04-A01 | Ability to design a purple-team exercise that closes gaps | Lab 1; Topic 4 |
| Ability | CE04-A02 | Ability to drive continuous improvement through purple teaming | Topic 6; Summative |
| Task | T0259 | Validate and improve detections through collaborative testing | Lab 1 |
| Task | T0591 | Execute techniques jointly to reveal detection gaps | Lab 2 |

---

## Topics

### Topic 1: The Purple-Team Model

This topic teaches purple teaming as a collaborative model: red executes, blue
observes and validates, and both work to maximise *learning* and detection
improvement rather than to "win". It contrasts this with adversarial, siloed
red/blue engagements.

**Key concepts:**
- Collaborative vs adversarial testing
- Shared goal: detection improvement
- Roles and facilitation

---

### Topic 2: Running a Collaborative Exercise

This topic covers executing a purple-team exercise: technique-by-technique
execution with the detection team watching live, capturing what fired (and what
didn't), and the real-time dialogue that turns a miss into an immediate detection
hypothesis.

**Key concepts:**
- Technique-by-technique joint execution
- Live capture of detected/missed
- Real-time red/blue dialogue

---

### Topic 3: Detection Gap Analysis

This topic teaches analysing the gaps revealed: diagnosing whether a miss is a data
gap (DE02), a logic gap (DE03), or a coverage gap, and prioritising the gaps by the
value of the techniques behind them.

**Key concepts:**
- Diagnosing miss root causes (data/logic/coverage)
- Prioritising gaps by technique value
- Producing a gap-analysis record

---

### Topic 4: Designing a Purple-Team Exercise

This topic teaches planning an exercise: selecting a prioritised technique set
(intelligence-driven, from CE03/CTI), defining objectives and success criteria, and
scoping safely within the CE01 authorisation regime.

**Key concepts:**
- Intelligence-driven technique selection
- Objectives and success criteria
- Safe scoping and facilitation

**Australian context:** Technique sets reflect ACSC-reported Australian threats.

---

### Topic 5: From Gaps to Improvements

This topic teaches converting gaps into action: authoring new detections (Sigma),
recommending logging changes, and validating that the fix closes the gap — feeding
the detection-engineering lifecycle (DE05).

**Key concepts:**
- Gap → new detection / logging change
- Validating the fix
- Feeding the detection lifecycle

---

### Topic 6: Continuous Purple Teaming and Maturity

This topic frames purple teaming as a recurring cadence, not a one-off, and connects
it to capability maturity: regular exercises drive measurable improvement in
detection maturity (DML/M3TID) and SOC capability (SOC-CMM).

**Key concepts:**
- Purple teaming as a cadence
- Driving detection/SOC maturity
- Measuring improvement over time

**Australian context:** Maturing detection supports Essential Eight monitoring and
SOCI obligations.

---

## Labs & Exercises

### Lab 1: Purple Team Exercise (collaborative lab)

**Objective:** Run a purple-team exercise: execute techniques jointly and document
detection outcomes.

**Prerequisites:**
- Topics 1–4; a SIEM with detections (from DE)

**Environment:**
- Operating System: a **fully isolated** lab with a target VM, a free SIEM
  (OpenSearch/Splunk Free), and detections from DE; ideally run as a red/blue pair
- Tools: Atomic Red Team, ATT&CK Navigator, Sigma — all free/OSS
- Minimum hardware: run sequentially — within the 8 GB / 4-core / 50 GB spec; no
  GPU. **No external network access.**

**Instructions:**

1. Confirm isolation; ensure detections and telemetry are in place.
2. Select a small, prioritised technique set (from a CE03 plan).
3. Execute each technique while the (simulated) blue role watches the SIEM.
4. Record detected/missed for each, with the firing event as evidence.
5. For each miss, capture an immediate detection hypothesis.
6. Produce a Navigator coverage layer (detected/missed).

**Expected Output:**

A documented purple-team run with a detected/missed coverage layer and detection
hypotheses for misses — within an isolated lab. Learners can show the live red/blue
dialogue value.

**Reflection Questions:**

1. Which miss surprised the blue role, and why?
2. How did real-time collaboration speed up the detection hypothesis?
3. Which technique most needs a durable detection?

---

### Lab 2: Detection Gap Analysis (analysis activity)

**Objective:** Produce a detection gap analysis report from the purple-team exercise
and recommend improvements.

**Prerequisites:**
- Topics 3, 5, and 6 and Lab 1

**Environment:**
- Operating System: any (analysis activity using Lab 1 results)
- Tools: the Lab 1 coverage layer, Sigma, ATT&CK Navigator — all free/OSS
- Minimum hardware: trivial

**Instructions:**

1. For each missed technique, diagnose the root cause (data/logic/coverage).
2. Prioritise the gaps by the value of the techniques behind them.
3. Author at least one new detection (Sigma) for a high-priority gap.
4. Recommend any logging change needed (link to DE02).
5. Define how you would validate the fixes.
6. Recommend a purple-team cadence and the maturity metric you would track.

**Expected Output:**

A detection gap analysis with diagnosed/prioritised gaps, at least one new detection,
validation approach, and a cadence/maturity recommendation. Learners can connect
each gap to a concrete, validated improvement.

**Reflection Questions:**

1. Which gap was a data problem vs a logic problem, and how does the fix differ?
2. How would a regular purple-team cadence change detection maturity over a year?
3. How does this feed SOC-CMM / M3TID maturity (see `docs/maturity-models.md`)?

---

## Assessment

### Formative Assessment: Gap Root-Cause Drill

**Type:** Self-check exercise with answer key

**Description:** Given purple-team results, students diagnose each miss's root cause
and the appropriate fix. Self-marked.

**Learning Outcomes Assessed:** LO3

**Feedback mechanism:** Answer key with the root cause and fix per miss.

---

### Summative Assessment: Purple-Team Exercise & Improvement Plan

**Type:** Practical report

**Description:** Students (a) design a purple-team exercise for a prioritised
technique set, (b) run it (isolated lab) and record coverage, (c) produce a detection
gap analysis with root causes, and (d) deliver an improvement plan (new detections,
logging, cadence) with a maturity metric. Deliverable: 2,500–3,000 word report with
a coverage layer and at least one new detection.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Exercise design | LO1, LO4 |
| Joint execution & coverage | LO2 |
| Gap analysis | LO3, LO5 |
| Improvement plan & cadence | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Collaboration & execution | Skilful, well-documented joint run | Sound | Partial | Weak |
| Gap analysis | Precise root-cause + prioritisation | Adequate | Superficial | Poor |
| Improvements | Robust detections + validation | Reasonable | Generic | Absent |
| Maturity framing | Clear cadence/maturity link | Adequate | Mentioned | Missing |
| Safety & ethics | Rigorous authorisation/isolation | Adequate | Minor gaps | Unsafe |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC-reported actors:** Exercises emulate Australian-relevant threats.
- **ASD Essential Eight & SOCI:** Detection improvements support monitoring
  obligations.
- **Capability maturity:** Purple teaming is tied to SOC-CMM/M3TID maturity (see
  `docs/maturity-models.md`).

---

## Further Reading

**MITRE Center for Threat-Informed Defense (2024–2026).** *M3TID & Adversary Emulation Library.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The threat-informed-defense maturity model and emulation methodology behind purple teaming (see `docs/maturity-models.md`).

**Red Canary (2024).** *Atomic Red Team.* https://github.com/redcanaryco/atomic-red-team
> Relevance: The free technique-execution library used in the exercises.

**SigmaHQ (2024).** *Sigma rule format.* https://github.com/SigmaHQ/sigma
> Relevance: The detection format for converting gaps into detections.

**Australian Cyber Security Centre (2024).** *Threat advisories & event-logging guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian threats and logging expectations for the exercises (Australian source).

**Scythe / purple-team community (2024).** *Purple Team Exercise Framework (PTEF).* https://github.com/scythe-io/purple-team-exercise-framework
> Relevance: A free, structured purple-team exercise methodology supporting Topic 4.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CE04 |
| Unit Title | Purple Team Operations |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Cyber Threat Emulation |
| Prerequisites | CE03, DE04 |
| Domain Expert | _Unassigned — required before Practitioner Approved (purple team experience)_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved (dual-use review)_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) Part 10.7 (contextual) |
