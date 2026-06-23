# CT02: Threat Actor Research & Profiling

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches the analytic core of CTI: researching and profiling threat
actors. Students learn to model intrusions with the **Diamond Model**, build
ATT&CK-based actor profiles, track groups and campaigns over time, and apply
attribution *methodology* rigorously and responsibly. A deliberate emphasis of the
unit — and a sign-off requirement — is that students learn how attribution is
*reasoned about*, not how to make confident public attributions; attribution is
treated as a probabilistic, evidence-graded analytic judgement.

Actor profiling produces the operational intelligence that drives hunting, detection,
and response: knowing how a relevant group behaves lets defenders prioritise. In the
Australian context, the ACSC reports on actors targeting Australian sectors and the
APAC region; this unit uses those reports as research material while teaching method
over conclusion. CT02 builds on CT01 and OC01, and feeds CT03–CT06.

---

## Prerequisites

- CT01 — Intelligence Tradecraft
- OC01 — Adversary Tradecraft & TTPs

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the Diamond Model of Intrusion Analysis to a known intrusion.
2. **Analyse** a threat actor's behaviour and build an ATT&CK (v19) actor profile.
3. **Evaluate** attribution evidence using a structured, confidence-graded
   methodology.
4. **Synthesise** open-source reporting into a coherent actor/campaign profile.
5. **Analyse** how actor profiles inform defensive prioritisation.
6. **Recommend** an actor profile suitable for an operational consumer, with
   appropriate caveats.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of intrusion
analysis models, actor profiling, and attribution methodology.

**Skills (AQF 7.2):** Students develop analytical and synthesis skills by modelling
intrusions and building evidence-graded profiles.

**Application (AQF 7.3):** Students apply profiling to Australian-relevant actors,
producing operationally useful, appropriately-caveated intelligence.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Threat/Warning Analyst (621) | AN-TWA-001 | T0707 | Analyse adversary activity to produce actor/campaign intelligence | Lab 1 — Diamond Model of an Intrusion |
| NIST NICE DCWF | 2023 | All-Source Analyst (611) | AN-ASA-001 | T0751 | Synthesise multi-source reporting into finished actor profiles | Lab 2 — ATT&CK Actor Profile |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 5 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Threat Intelligence | Threat Analysis | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CT02-K01 | Knowledge of the Diamond Model | Topic 1 |
| Knowledge | CT02-K02 | Knowledge of ATT&CK actor profiling | Topic 2 |
| Knowledge | CT02-K03 | Knowledge of campaign and group tracking | Topic 3 |
| Knowledge | CT02-K04 | Knowledge of attribution methodology as method, not verdict | Topic 4 |
| Skill | CT02-S01 | Skill in building a Diamond Model of an intrusion | Lab 1 |
| Skill | CT02-S02 | Skill in producing an ATT&CK actor profile | Lab 2 |
| Ability | CT02-A01 | Ability to turn an actor profile into a defensive priority | Lab 2; Topic 5 |
| Ability | CT02-A02 | Ability to reason about attribution confidence | Topic 4; Summative |
| Task | T0707 | Analyse adversary activity to produce actor/campaign intelligence | Lab 1 |
| Task | T0751 | Synthesise multi-source reporting into finished actor profiles | Lab 2 |

---

## Topics

### Topic 1: The Diamond Model

The Diamond Model analyses intrusions across four vertices — adversary,
capability, infrastructure, victim — linked by meta-features. This topic teaches
populating and pivoting across the diamond to develop and connect intrusion events.

**Key concepts:**
- The four vertices and meta-features
- Pivoting across the diamond
- Linking events into activity threads

---

### Topic 2: ATT&CK Actor Profiling

This topic teaches building an actor profile in ATT&CK terms: collecting known
techniques from ATT&CK Groups/Software and reporting, building a Navigator layer,
and distinguishing signature behaviour from commodity tooling.

**Key concepts:**
- ATT&CK Groups/Software as profile sources
- Building and annotating Navigator layers
- Signature vs commodity behaviour

**Australian context:** Profiles are built for actors the ACSC reports as active
against Australian/APAC sectors.

---

### Topic 3: Campaign and Group Tracking

Actors evolve. This topic covers tracking campaigns and groups over time: clustering
activity, naming conventions and the "attribution by different vendors" problem, and
maintaining living profiles as new reporting arrives.

**Key concepts:**
- Activity clustering and campaign tracking
- The multi-vendor naming problem
- Maintaining living profiles

---

### Topic 4: Attribution Methodology (Method, Not Verdicts)

This topic teaches how attribution is reasoned about — combining technical,
infrastructural, and behavioural evidence with confidence levels — while
emphasising that responsible analysts rarely make confident public attributions and
must avoid overreach. The focus is methodology and caveat, not naming.

**Key concepts:**
- Layers of attribution evidence
- Confidence and the limits of attribution
- Avoiding analytic overreach (responsibility)

**Australian context:** Public attribution is a government function (e.g. ASD/
Government statements); analysts support, not pre-empt, it.

---

### Topic 5: From Profile to Defensive Priority

This topic connects profiling to action: translating an actor profile into
prioritised techniques to hunt/detect (linking to TH02/OC02) and into intelligence
that informs risk decisions.

**Key concepts:**
- Profile → prioritised techniques
- Informing hunting/detection priorities
- Informing risk decisions

---

### Topic 6: Producing the Actor Profile

This topic teaches packaging a profile for a consumer: structure, evidence and
sourcing, confidence statements, and consumer-appropriate language — a finished
product, not a research dump.

**Key concepts:**
- Profile structure and sourcing
- Confidence and caveats
- Consumer-appropriate finished products

**Australian context:** Profiles cite publicly attributed Australian incident
examples where available, with method emphasised.

---

## Labs & Exercises

### Lab 1: Diamond Model of an Intrusion

**Objective:** Apply the Diamond Model to a known, publicly documented intrusion.

**Prerequisites:**
- Topics 1 and 3

**Environment:**
- Operating System: any (analysis lab)
- Tools: a Diamond Model template, public intrusion reporting / ACSC advisories
  (free)
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Select a publicly documented intrusion (e.g. from an ACSC advisory or vendor
   report).
2. Populate all four Diamond vertices with evidence and sourcing.
3. Add meta-features (timestamp, phase, result) and link related events.
4. Pivot from one vertex (e.g. infrastructure) to hypothesise related activity.
5. State the confidence in each vertex and note evidence gaps.
6. Summarise the activity thread the diamond reveals.

**Expected Output:**

A fully populated Diamond Model with sourced vertices, meta-features, a pivot, and
confidence statements. Learners can justify each vertex from the reporting.

**Reflection Questions:**

1. Which vertex was best/worst supported by evidence, and why?
2. What did pivoting reveal that a single event did not?
3. Where would overreaching on attribution be a risk here?

---

### Lab 2: ATT&CK Actor Profile

**Objective:** Build an ATT&CK v19 actor profile from open-source reporting for an
Australian-relevant actor.

**Prerequisites:**
- Topics 2, 4, and 6 and Lab 1

**Environment:**
- Operating System: any
- Tools: ATT&CK Navigator (v19), ATT&CK Group pages, ACSC/vendor reporting (free)
- Minimum hardware: trivial

**Instructions:**

1. Choose an actor the ACSC reports as relevant to Australia/APAC.
2. Collect its known techniques from ATT&CK Groups/Software and reporting.
3. Build a Navigator layer; distinguish signature from commodity behaviour.
4. Apply attribution methodology: state the evidence and confidence, with explicit
   caveats (no overreach).
5. Translate the profile into the top techniques to hunt/detect.
6. Package a short, consumer-ready actor profile.

**Expected Output:**

A Navigator actor layer, an evidence/confidence assessment with caveats, prioritised
techniques, and a consumer-ready profile. Learners can defend the method while
acknowledging attribution limits.

**Reflection Questions:**

1. How did you separate signature behaviour from commodity tooling, and why does it
   matter?
2. Where did you deliberately stop short of attribution overreach?
3. How would this profile change a SOC's hunting priorities?

---

## Assessment

### Formative Assessment: Diamond & Attribution Drill

**Type:** Self-check exercise with answer key

**Description:** Given intrusion snippets, students place evidence on the Diamond
Model and rate attribution confidence with caveats. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with model placements and confidence reasoning.

---

### Summative Assessment: Threat Actor Profile

**Type:** Analytical report

**Description:** For an Australian-relevant actor, students (a) analyse an intrusion
with the Diamond Model, (b) build an ATT&CK v19 actor profile, (c) apply attribution
methodology with confidence and caveats, and (d) translate the profile into
defensive priorities for an operational consumer. Deliverable: 2,500–3,000 word
profile with Navigator and Diamond artefacts. **Must teach/apply method, not assert
confident public attribution.**

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Diamond Model analysis | LO1 |
| ATT&CK actor profile | LO2, LO4 |
| Attribution methodology & caveats | LO3 |
| Defensive priorities & product | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Intrusion analysis | Rigorous, sourced Diamond Model | Sound | Partial | Weak |
| Actor profiling | Accurate, well-evidenced ATT&CK profile | Mostly accurate | Several errors | Inaccurate |
| Attribution responsibility | Appropriately caveated, no overreach | Mostly appropriate | Some overreach | Unsupported claims |
| Defensive translation | Clear, prioritised, actionable | Reasonable | Generic | Absent |
| Communication | Clear, consumer-appropriate | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories & Annual Cyber Threat Report:** Research material on actors
  targeting Australian/APAC sectors.
- **Public attribution as a government function:** Analysts support, not pre-empt,
  ASD/Government attribution statements.
- **Australian incident examples:** Used (publicly attributed only) with method
  emphasised over conclusion.

---

## Further Reading

**Caltagirone, S., Pendergast, A. & Betz, C. (2013).** *The Diamond Model of Intrusion Analysis.* https://www.activeresponse.org/the-diamond-model/
> Relevance: The core analytic model of this unit; freely available.

**MITRE ATT&CK (v19, 2026).** *Groups & Software.* The MITRE Corporation. https://attack.mitre.org/groups/
> Relevance: The actor/technique reference for profiling; CC BY 4.0.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Attack Flow & actor methodology.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: Supports campaign modelling and behaviour-based profiling.

**Australian Cyber Security Centre (2024).** *Threat advisories & Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au
> Relevance: Australian-relevant actor reporting used as research material (Australian source).

**Rid, T. & Buchanan, B. (2015).** *Attributing Cyber Attacks.* Journal of Strategic Studies.
> Relevance: A rigorous treatment of attribution as graded, probabilistic judgement (Topic 4).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CT02 |
| Unit Title | Threat Actor Research & Profiling |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | CTI |
| Prerequisites | CT01, OC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (ACSC reporting context) |
