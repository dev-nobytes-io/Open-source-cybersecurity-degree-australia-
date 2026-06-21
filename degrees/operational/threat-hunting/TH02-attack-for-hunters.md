# TH02: ATT&CK for Hunters

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit makes MITRE ATT&CK an operational hunting tool rather than a reference
poster. It teaches hunters to translate adversary techniques into hunt plans:
prioritising techniques by relevance and detectability, using ATT&CK Navigator to
map coverage and plan hunts, and applying CTID research (Top ATT&CK Techniques,
Sensor Mappings, Attack Flow) to decide what to hunt and how. It assumes the
ATT&CK literacy from OC01 and deepens it to analyst/evaluator level.

> **ATT&CK version note:** This unit uses **ATT&CK v19**. v19 introduced
> significant structural changes; technique identifiers in this unit are written
> against stable techniques but are subject to the repo-wide v19 mapping audit
> tracked in the root `TODO.md`. Always confirm a technique's current ID and
> structure on attack.mitre.org before relying on it in a live hunt.

In the Australian context, ATT&CK-based prioritisation is what lets a hunt team
focus on the techniques real actors use against Australian sectors (per ACSC
reporting) instead of hunting everything. TH02 builds on TH01 and feeds the
data-specific hunting units TH03–TH05.

---

## Prerequisites

- TH01 — Hunting Methodology & Process
- OC01 — Adversary Tradecraft & TTPs

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** an adversary group's behaviour and represent it as an ATT&CK
   (v19) technique profile in Navigator.
2. **Prioritise** techniques for hunting based on threat relevance, detectability,
   and available data.
3. **Design** an ATT&CK-driven hunt plan that sequences techniques using Attack
   Flow.
4. **Evaluate** an organisation's hunt coverage against a threat profile and
   identify the highest-value gaps.
5. **Analyse** the data sources required to hunt a given technique using CTID
   Sensor Mappings.
6. **Recommend** which techniques to hunt first for a given Australian
   organisation and justify the choice.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of ATT&CK as a
hunting and coverage-analysis instrument.

**Skills (AQF 7.2):** Students develop analytical and evaluative skills by
profiling actors, prioritising techniques, and analysing coverage.

**Application (AQF 7.3):** Students apply ATT&CK-driven planning to real Australian
threat profiles, producing prioritised, data-grounded hunt plans.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0569 | Apply ATT&CK to characterise adversary behaviour and plan hunts | Lab 1 — Actor Technique Profile & Hunt Plan |
| NIST NICE DCWF | 2023 | Threat/Warning Analyst | AN-TWA-001 | T0708 | Analyse coverage gaps and prioritise techniques for detection/hunting | Lab 2 — Coverage Gap Prioritisation |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Threat Hunting | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: ATT&CK as an Operational Instrument

This topic re-frames ATT&CK from taxonomy to tool: a structure for planning,
prioritising, and measuring hunts. It revisits tactics/techniques/sub-techniques/
procedures at hunter depth and introduces the v19 structure and its implications
for technique referencing.

**Key concepts:**
- ATT&CK as planning/measurement instrument
- Procedures vs techniques for hunters
- Working with the v19 structure

---

### Topic 2: Building Actor Technique Profiles

This topic teaches profiling a threat group: collecting its known techniques from
intelligence and ATT&CK group pages, building a Navigator layer, and reasoning
about which behaviours are most characteristic. It connects to CTI (OC05) actor
analysis.

**Key concepts:**
- ATT&CK Groups and Software as profile sources
- Building and annotating Navigator layers
- Distinguishing signature vs commodity behaviour

**Australian context:** Profiles are built for actors reported by the ACSC as
active against Australian sectors.

---

### Topic 3: Prioritising Techniques for Hunting

You cannot hunt everything. This topic teaches prioritisation by threat relevance
(does a relevant actor use it?), detectability (is there data and a durable
analytic?), and impact. It applies CTID **Top ATT&CK Techniques** as a
prioritisation input and the Pyramid of Pain for durability.

**Key concepts:**
- Prioritisation criteria: relevance, detectability, impact
- CTID Top ATT&CK Techniques
- Durability via the Pyramid of Pain

---

### Topic 4: Technique-to-Data Mapping

A technique is only huntable if the right data exists. This topic uses CTID
**Sensor Mappings** / Mappings Explorer to determine the telemetry needed for a
technique and to expose visibility gaps before a hunt begins.

**Key concepts:**
- Technique → required data source → sensor
- Sensor Mappings / Mappings Explorer
- Identifying gaps pre-hunt

---

### Topic 5: Sequencing Hunts with Attack Flow

Adversaries chain techniques; hunts can follow the chain. This topic uses CTID
**Attack Flow** to model likely technique sequences, letting a hunter pivot from
one observed behaviour to the next expected one.

**Key concepts:**
- Modelling technique sequences with Attack Flow
- Pivoting along the chain during a hunt
- Anticipating the next technique

---

### Topic 6: Measuring and Communicating Coverage

This topic teaches representing hunt/detection coverage as a Navigator heatmap,
distinguishing "have data" from "have hunted" from "have a detection", and
communicating coverage and gaps to stakeholders (linking to SC06 communication).

**Key concepts:**
- Coverage heatmaps and their honest interpretation
- Data vs hunted vs detected
- Communicating coverage to decision-makers

**Australian context:** Coverage is assessed against Essential Eight-relevant
behaviours and Australian actor profiles.

---

## Labs & Exercises

### Lab 1: Actor Technique Profile & Hunt Plan

**Objective:** Profile an Australian-relevant adversary in ATT&CK v19 and build a
prioritised, sequenced hunt plan.

**Prerequisites:**
- Topics 1–5

**Environment:**
- Operating System: any
- Tools: ATT&CK Navigator (v19), CTID Top ATT&CK Techniques / Attack Flow (free),
  ACSC reporting
- Minimum hardware: trivial; within spec

**Instructions:**

1. Choose an actor/campaign reported by the ACSC as relevant to an Australian
   sector.
2. Build a Navigator layer of the actor's techniques from ATT&CK Group pages and
   the advisory.
3. Prioritise the techniques using CTID Top ATT&CK Techniques and the Pyramid of
   Pain.
4. Build an Attack Flow for the most likely technique sequence.
5. Produce a hunt plan: which techniques to hunt, in what order, and why.
6. Note one technique you would *not* hunt and justify deprioritising it.

**Expected Output:**

A Navigator actor layer, a prioritised technique list, an Attack Flow, and a
sequenced hunt plan. Learners can justify both their priorities and their
deprioritisations.

**Reflection Questions:**

1. How did prioritisation change which techniques you'd hunt first?
2. Where did v19's structure affect how you referenced a technique?
3. How would the plan change for a different Australian sector?

---

### Lab 2: Coverage Gap Prioritisation

**Objective:** Assess hunt/detection coverage against a threat profile and
prioritise the gaps worth closing.

**Prerequisites:**
- Topics 4 and 6 and Lab 1

**Environment:**
- Operating System: any
- Tools: ATT&CK Navigator, CTID Sensor Mappings / Mappings Explorer (free), a
  spreadsheet
- Minimum hardware: trivial

**Instructions:**

1. Take the actor layer from Lab 1 and an assumed logging baseline.
2. For each priority technique, use Sensor Mappings to list required telemetry.
3. Mark each technique Covered / Partial / Gap based on the assumed data.
4. Build a coverage heatmap distinguishing "have data" vs "have hunted".
5. Prioritise the top three gaps to close (data source, hunt, or detection).
6. Write a short stakeholder-facing coverage summary.

**Expected Output:**

A coverage heatmap, a Covered/Partial/Gap technique table, and three prioritised
gap-closing recommendations with a stakeholder summary. Learners can defend the
prioritisation against the organisation's real exposure.

**Reflection Questions:**

1. Which gap was a data problem vs an analytic problem, and how does the fix
   differ?
2. How would you communicate this coverage honestly to a non-technical
   stakeholder?
3. How does closing these gaps feed the broader threat-informed defense loop?

---

## Assessment

### Formative Assessment: Technique Prioritisation Drill

**Type:** Self-check exercise with answer key

**Description:** Given an actor's technique set and an assumed data baseline,
students rank techniques for hunting and justify each ranking. Self-marked.

**Learning Outcomes Assessed:** LO2, LO5

**Feedback mechanism:** Answer key with a model ranking and rationale.

---

### Summative Assessment: ATT&CK-Driven Hunt Coverage Report

**Type:** Analytical report

**Description:** For an assigned Australian actor and organisation, students (a)
build an ATT&CK v19 actor profile, (b) prioritise and sequence techniques into a
hunt plan, (c) analyse coverage against required telemetry, and (d) recommend a
prioritised set of hunts/data/detections to close the highest-value gaps.
Deliverable: 2,500–3,000 word report with Navigator and Attack Flow artefacts.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Actor technique profile | LO1 |
| Prioritised, sequenced hunt plan | LO2, LO3 |
| Coverage & data analysis | LO4, LO5 |
| Gap-closing recommendations | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| ATT&CK profiling | Accurate, well-evidenced v19 profile | Mostly accurate | Several errors | Inaccurate profile |
| Prioritisation | Insightful, criteria-driven, justified | Sound prioritisation | Generic | Unjustified |
| Coverage analysis | Precise, data-grounded gap analysis | Solid analysis | Partial | Weak |
| Recommendations | High-value, prioritised, actionable | Reasonable | Generic | Absent |
| Communication | Clear, professional, honest about gaps | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories & Annual Cyber Threat Report:** Source of Australian-relevant
  actor profiles for both labs.
- **ASD Essential Eight:** Coverage assessed against control-bypass behaviours.
- **Australian sector relevance:** Profiles and prioritisation reflect the actors
  targeting specific Australian sectors.

---

## Further Reading

**MITRE ATT&CK (v19, 2026).** *ATT&CK for Enterprise, Groups & Software.* The MITRE Corporation. https://attack.mitre.org
> Relevance: The core knowledge base for actor profiling and technique referencing; CC BY 4.0.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Top ATT&CK Techniques, Sensor Mappings to ATT&CK, Mappings Explorer, Attack Flow.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The prioritisation, data-mapping, and sequencing tooling used throughout this unit.

**Bianco, D. (2013).** *The Pyramid of Pain.* https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html
> Relevance: Underpins durability-based technique prioritisation in Topic 3.

**Australian Cyber Security Centre (2024).** *Threat advisories & Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian source of actor TTPs used to build profiles (Australian source).

**Strom, B. et al. (updated).** *MITRE ATT&CK: Design and Philosophy.* The MITRE Corporation. https://attack.mitre.org/resources/
> Relevance: Ensures correct, defensible use of the ATT&CK structure (important given v19 changes).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | TH02 |
| Unit Title | ATT&CK for Hunters |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Threat Hunting |
| Prerequisites | TH01, OC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (ACSC threat reporting context) |
