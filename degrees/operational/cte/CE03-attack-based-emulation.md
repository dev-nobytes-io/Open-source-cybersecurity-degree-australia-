# CE03: ATT&CK-Based Emulation

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (red team / emulation experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must review dual-use risk)_

---

## Overview

This unit teaches structured, intelligence-driven adversary emulation using **MITRE
CTID** methodology and the **Adversary Emulation Library**. Rather than testing
generic offensive techniques, students learn to emulate a *specific* threat actor's
behaviour — building or adapting an ATT&CK-based emulation plan from threat
intelligence, then executing it (in an isolated lab, under CE01 authorisation) to
test whether defenders detect that actor. This is the discipline that makes
emulation a precise, repeatable test of threat-informed defense rather than ad-hoc
red teaming.

Emulation plans connect the whole operational degree: intelligence (CTI) selects the
actor, the plan encodes ATT&CK (v19) techniques, and the results feed detection
(DE) and hunting (TH). In the Australian context, plans are adapted to the threat
actors the ACSC reports as relevant to Australian sectors. CE03 builds on CE01–CE02,
OC01 (Adversary Tradecraft), and OC05 (CTI), and feeds CE04 (purple team) and the
CE06 capstone. Maturity of this capability is measured with **M3TID** (see
`docs/maturity-models.md`).

---

## Prerequisites

- CE02 — Red Team Operations
- OC01 — Adversary Tradecraft & TTPs

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** an adversary's behaviour and select a CTID emulation plan that
   represents it.
2. **Design** an ATT&CK-based emulation plan adapted to a specific organisation's
   threat model.
3. **Apply** a CTID emulation plan's procedures in an isolated, authorised lab.
4. **Evaluate** the fidelity of an emulation to the real adversary it represents.
5. **Analyse** the detection outcomes an emulation produces.
6. **Recommend** emulation-derived improvements to detection and defence.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of structured,
intelligence-driven adversary emulation.

**Skills (AQF 7.2):** Students develop design and analytical skills by building and
executing emulation plans and evaluating fidelity and detection.

**Application (AQF 7.3):** Students apply CTID methodology to emulate
Australian-relevant actors and drive defensive improvement.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Exploitation Analyst (711) | AN-EXP-001 | T0591 | Develop and execute adversary emulation plans to test defences | Lab 1 — Adapt a CTID Emulation Plan |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Analyse detection outcomes from emulated adversary behaviour | Lab 2 — Execute & Evaluate Detection |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 4–5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Cyber | Adversary Emulation | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CE03-K01 | Knowledge of what adversary emulation is | Topic 1 |
| Knowledge | CE03-K02 | Knowledge of CTID methodology and the Adversary Emulation Library | Topic 2 |
| Knowledge | CE03-K03 | Knowledge of building and adapting an emulation plan | Topic 3 |
| Knowledge | CE03-K04 | Knowledge of executing emulation and evaluating fidelity and detection | Topic 4; Topic 5 |
| Skill | CE03-S01 | Skill in adapting a CTID emulation plan | Lab 1 |
| Skill | CE03-S02 | Skill in executing and evaluating detection from emulation | Lab 2 |
| Ability | CE03-A01 | Ability to run an authorised, isolated emulation faithfully | Lab 2; Topic 4 |
| Ability | CE03-A02 | Ability to translate emulation outcomes into defensive improvement | Topic 6; Summative |
| Task | T0591 | Develop and execute adversary emulation plans to test defences | Lab 1 |
| Task | T0259 | Analyse detection outcomes from emulated adversary behaviour | Lab 2 |

---

## Topics

### Topic 1: What Adversary Emulation Is

This topic distinguishes emulation (replicating a specific actor's TTPs to test
detection) from generic red teaming, and establishes the intelligence-driven,
ATT&CK-anchored, repeatable nature of emulation.

**Key concepts:**
- Emulation vs generic red teaming
- Intelligence-driven, actor-specific testing
- Repeatability and ATT&CK anchoring

---

### Topic 2: CTID Methodology and the Emulation Library

This topic teaches the MITRE CTID adversary-emulation methodology and the public
Adversary Emulation Library: the structure of an emulation plan (intelligence
summary, phases, procedures), and how to select a plan that matches a relevant
actor.

**Key concepts:**
- CTID emulation methodology
- Emulation-plan structure
- Selecting a plan for a relevant actor

---

### Topic 3: Building and Adapting a Plan

This topic teaches adapting a plan to a specific organisation: tailoring techniques
to the target's environment and threat model, scoping safely, and ensuring the plan
remains a faithful representation of the actor.

**Key concepts:**
- Tailoring a plan to a target environment
- Safe scoping of procedures
- Maintaining fidelity to the actor

**Australian context:** Plans are adapted for actors the ACSC reports as relevant to
Australian sectors.

---

### Topic 4: Executing an Emulation (Isolated, Authorised)

This topic covers running an emulation under CE01 authorisation in an isolated lab:
sequencing techniques (using Attack Flow), using Atomic Red Team for atomic steps,
documenting execution, and generating the telemetry defenders will analyse.

**Key concepts:**
- Sequenced execution (Attack Flow)
- Atomic Red Team for atomic procedures
- Documented, isolated, authorised execution

---

### Topic 5: Evaluating Fidelity and Detection

This topic teaches assessing two things: how faithfully the emulation represented the
real actor, and what defenders detected — producing the detected/missed picture that
drives improvement.

**Key concepts:**
- Fidelity assessment
- Detected vs missed analysis
- Coverage representation (Navigator)

---

### Topic 6: From Emulation to Defensive Improvement

This topic closes the loop: turning emulation results into prioritised detection,
logging, and control improvements (feeding DE/TH), and measuring the capability's
maturity with M3TID.

**Key concepts:**
- Results → prioritised defensive improvements
- Feeding detection/hunting
- M3TID maturity measurement

**Australian context:** Improvements target Essential Eight-relevant detection gaps.

---

## Labs & Exercises

### Lab 1: Adapt a CTID Emulation Plan (design activity)

**Objective:** Select a CTID emulation plan and adapt it to a fictional Australian
organisation's threat model.

**Prerequisites:**
- Topics 1–3; CE01 authorisation framing

**Environment:**
- No offensive execution — a planning/design activity using the public CTID
  Adversary Emulation Library and ATT&CK Navigator. Any device within the
  8 GB / 4-core / 50 GB spec.

**Instructions:**

1. Choose an actor the ACSC reports as relevant to an Australian sector.
2. Select the closest CTID emulation plan (or assemble one from ATT&CK Group data).
3. Build a Navigator layer of the plan's techniques.
4. Adapt the plan to a fictional Australian organisation's environment and threat
   model, scoping safely.
5. Sequence the techniques with an Attack Flow.
6. Define the detection outcomes the emulation is designed to test.

**Expected Output:**

An adapted, scoped emulation plan with a Navigator layer, an Attack Flow, and stated
detection outcomes. Learners can justify the plan's fidelity to the actor and its
fit to the organisation.

**Reflection Questions:**

1. Where did you adapt the plan, and did it stay faithful to the actor?
2. Which technique best tests the organisation's detection?
3. How does intelligence make this emulation more valuable than generic testing?

---

### Lab 2: Execute & Evaluate Detection (isolated lab)

**Objective:** Execute the initial steps of an emulation plan in an isolated lab and
evaluate what was detected.

**Prerequisites:**
- Topics 4–6 and Lab 1; a SIEM (from OC02/DE) ingesting target telemetry

**Environment:**
- Operating System: a **fully isolated** lab (no external network) with target VM(s)
  and a free SIEM (OpenSearch/Splunk Free)
- Tools: Atomic Red Team, the open-source C2 from CE02 (optional), ATT&CK Navigator —
  all free/OSS
- Minimum hardware: run sequentially — within the 8 GB / 4-core / 50 GB spec; no
  GPU. **No external network access.**

**Instructions:**

1. Confirm isolation; ensure target telemetry flows to the SIEM.
2. Execute the first few techniques of the adapted plan (e.g. via Atomic Red Team).
3. For each technique, record whether a detection fired (detected/missed) with
   evidence.
4. Produce a Navigator coverage layer (detected/missed).
5. Assess the fidelity of the executed steps to the actor.
6. Recommend one new detection for a missed technique (hand-off to DE).

**Expected Output:**

A documented execution with a detected/missed coverage layer, a fidelity assessment,
and a detection recommendation — all within an isolated, authorised lab. Learners can
trace each missed technique to a defensive improvement.

**Reflection Questions:**

1. Which technique was missed, and what was the root cause (data/logic)?
2. How faithful was the execution to the real actor, and does it matter for the test?
3. How would you measure this capability's maturity with M3TID?

---

## Assessment

### Formative Assessment: Plan-to-Actor Drill

**Type:** Self-check exercise with answer key

**Description:** Given actor profiles, students select the most appropriate CTID
emulation plan and justify the fit. Self-marked.

**Learning Outcomes Assessed:** LO1

**Feedback mechanism:** Answer key with the recommended plan and rationale.

---

### Summative Assessment: Adversary Emulation Plan & Results

**Type:** Practical report

**Description:** For an Australian-relevant actor and a fictional organisation,
students (a) select and adapt a CTID emulation plan, (b) execute its initial steps in
an isolated lab, (c) evaluate fidelity and detection coverage, and (d) recommend
prioritised defensive improvements with an M3TID maturity note. Deliverable:
2,500–3,000 word report with Navigator/Attack Flow artefacts.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Plan selection & adaptation | LO1, LO2 |
| Isolated execution | LO3 |
| Fidelity & detection evaluation | LO4, LO5 |
| Defensive improvements | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Plan fidelity | Faithful, well-adapted, scoped | Sound | Partial | Weak |
| Execution | Correct, documented, isolated | Adequate | Partial | Unsafe/incomplete |
| Detection evaluation | Precise detected/missed with evidence | Solid | Partial | Weak |
| Improvement & maturity | Prioritised; M3TID-aware | Reasonable | Generic | Absent |
| Safety & ethics | Rigorous authorisation/isolation | Adequate | Minor gaps | Unsafe |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC-reported actors:** Emulation plans are adapted to Australian-relevant
  threat actors.
- **Criminal Code Act 1995 Part 10.7:** Execution is within the CE01 authorisation
  regime, isolated lab only.
- **ASD Essential Eight:** Defensive improvements target Essential Eight-relevant
  detection gaps.

---

## Further Reading

**MITRE Center for Threat-Informed Defense (2024–2026).** *Adversary Emulation Library, Attack Flow, M3TID.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The emulation methodology, plans, sequencing, and maturity model central to this unit (see `docs/maturity-models.md`).

**Red Canary (2024).** *Atomic Red Team.* https://github.com/redcanaryco/atomic-red-team
> Relevance: The free, ATT&CK-mapped library for executing atomic procedures in Lab 2.

**MITRE ATT&CK (v19, 2026).** *Groups, Software & techniques.* https://attack.mitre.org
> Relevance: The actor/technique reference for building faithful emulation plans.

**Australian Cyber Security Centre (2024).** *Threat advisories & Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au
> Relevance: Australian-relevant actors and TTPs to emulate (Australian source).

**Applebaum, A. et al. / MITRE (2024).** *Adversary emulation methodology.* The MITRE Corporation. https://attack.mitre.org/resources/
> Relevance: The methodological basis for structured, intelligence-driven emulation.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CE03 |
| Unit Title | ATT&CK-Based Emulation |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Cyber Threat Emulation |
| Prerequisites | CE02, OC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved (red team experience)_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved (dual-use review)_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) Part 10.7 (contextual) |
