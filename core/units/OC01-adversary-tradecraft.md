# OC01: Adversary Tradecraft & TTPs

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches students to think like an adversary so they can defend like a
professional. It covers how real intrusion sets operate — their tactics,
techniques, and procedures (TTPs) — using **MITRE ATT&CK** as the common
taxonomy and **threat-informed defense** as the organising philosophy. The
central idea is that defence is a living system: adversary behaviour changes
constantly, and detections, logging, infrastructure, and automation must adapt to
that changing reality rather than sit static. Students learn to read adversary
behaviour, map it to ATT&CK, and reason about which behaviours are observable and
defensible.

Threat-informed defense (TID), as developed by the **MITRE Center for
Threat-Informed Defense (CTID)**, reframes security operations around what
adversaries actually do. In the Australian context, this is exactly the posture
the ACSC promotes through its threat advisories and the ASD *Cyber Threat
Report*: prioritise defences against the behaviours seen in the real threat
landscape. OC01 is the first operational unit and the conceptual backbone for
OC02 (Security Monitoring), OC05 (Threat Intelligence), OC06 (Offensive Security
Concepts), and the Threat Hunting, Detection Engineering, and CTE majors.

---

## Prerequisites

- F04 — Security Concepts & Principles
- F06 — Data & Log Analysis

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the MITRE ATT&CK framework to describe and categorise adversary
   behaviour across tactics, techniques, and sub-techniques.
2. **Analyse** an intrusion narrative to extract TTPs and represent them in
   ATT&CK Navigator and an Attack Flow.
3. **Differentiate** indicators along the Pyramid of Pain and explain why
   behaviour-based detection is more durable than atomic indicators.
4. **Apply** threat-informed defense to prioritise defensive effort against the
   techniques most relevant to a given organisation.
5. **Examine** how CTID resources (emulation library, sensor mappings, M3TID)
   support a continuously adapting defence.
6. **Analyse** the gap between an organisation's current visibility and the
   techniques it most needs to detect.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of adversary
behaviour and the threat-informed defense paradigm, anchored in MITRE ATT&CK and
CTID research.

**Skills (AQF 7.2):** Students develop cognitive and analytical skills by
deconstructing intrusions into TTPs, mapping them to a structured taxonomy, and
reasoning about detection and visibility.

**Application (AQF 7.3):** Students apply these skills to prioritise defensive
effort for a realistic organisation against the Australian threat landscape,
using ATT&CK and CTID tooling as a professional would.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0569 | Apply cyber threat frameworks (e.g. MITRE ATT&CK) to characterise adversary behaviour | Lab 1 — Mapping an Intrusion to ATT&CK |
| NIST NICE DCWF | 2023 | Threat/Warning Analyst | AN-TWA-001 | T0707 | Analyse threat information to identify adversary tactics, techniques, and procedures | Lab 2 — Threat-Informed Prioritisation with Navigator |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Threat intelligence | THIN | Level 4 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Threat Analysis | Practitioner | Lab 1, Lab 2 |

---

## Topics

### Topic 1: The Threat-Informed Defense Paradigm

Threat-informed defense is the practice of applying a deep understanding of
adversary behaviour to the design, operation, and continuous improvement of
defences. This topic introduces the TID philosophy: defences should be driven by
what adversaries actually do, measured against real behaviour, and continuously
adapted as the threat landscape shifts. It contrasts TID with compliance-driven
and tool-driven security, and introduces CTID as the body advancing the discipline
through open research.

**Key concepts:**
- Threat-informed defense vs compliance-driven and tool-driven security
- Defence as a living system that adapts to a changing adversary
- The role of MITRE CTID and its open-source body of work

**Australian context:** The ACSC's advisory-led, behaviour-focused guidance
exemplifies threat-informed defense at a national level.

---

### Topic 2: MITRE ATT&CK as a Common Language

ATT&CK is a curated knowledge base of adversary tactics (the "why"), techniques
and sub-techniques (the "how"), and procedures (specific implementations). This
topic teaches fluency in the model: navigating the matrix, reading a technique
page (detection, mitigation, data sources), and using ATT&CK as the shared
vocabulary that connects intel, detection, response, and emulation.

**Key concepts:**
- Tactics, techniques, sub-techniques, and procedures
- Reading a technique: detections, mitigations, and data sources
- ATT&CK as the lingua franca across the security lifecycle

---

### Topic 3: The Intrusion Lifecycle and Procedures

Adversaries chain techniques together to achieve objectives. This topic walks the
end-to-end intrusion lifecycle — initial access, execution, persistence, privilege
escalation, defense evasion, credential access, discovery, lateral movement,
collection, command and control, exfiltration, impact — and examines real
procedures for representative techniques. Students learn to see an intrusion as a
sequence of choices, each of which is an opportunity to detect.

**Key concepts:**
- The intrusion lifecycle as chained tactics
- Procedures: how the same technique varies between actors
- Every adversary choice is a potential detection opportunity

---

### Topic 4: The Pyramid of Pain and Durable Detection

Not all indicators are equal. The Pyramid of Pain ranks indicators by how much
effort it costs an adversary to change them — hash values and IPs are trivial to
change; tools and TTPs are expensive. This topic explains why behaviour-based
detection (high on the pyramid) is more durable than atomic indicators, and why
threat-informed defense focuses effort there. It links directly to detection
engineering (OC02) and CTID's *Summiting the Pyramid* research on robust
analytics.

**Key concepts:**
- The Pyramid of Pain and indicator durability
- Why TTP-level detection survives adversary change
- CTID *Summiting the Pyramid* and analytic robustness

---

### Topic 5: CTID Tooling for a Living Defence

CTID produces open resources that operationalise TID. This topic surveys the most
useful: the **Adversary Emulation Library** (test plans modelled on real actors),
**ATT&CK Navigator** (visualising coverage and priorities), **Attack Flow**
(modelling sequences of techniques), **Sensor Mappings to ATT&CK** and **Mappings
Explorer** (what telemetry covers which techniques), **Top ATT&CK Techniques**
(prioritisation), and **M3TID** (measuring threat-informed-defense maturity).
Students learn what each is for and when to reach for it.

**Key concepts:**
- Adversary Emulation Library and Attack Flow
- Navigator and Mappings Explorer for coverage analysis
- M3TID for measuring and maturing TID

**Australian context:** These open tools let Australian organisations of any size
adopt threat-informed defense without commercial licensing.

---

### Topic 6: From Behaviour to Visibility — Closing the Loop

Threat-informed defense is only real if it changes what you can see and do. This
topic ties the unit together: given a set of prioritised techniques, determine
the data sources and telemetry needed to detect them, identify visibility gaps,
and feed those gaps back into logging, detection, infrastructure, and automation
changes. This is the feedback loop that makes defence a living organism — the core
idea the rest of the operational core builds on.

**Key concepts:**
- Technique → required data source → telemetry → detection
- Identifying and closing visibility gaps
- The continuous loop: behaviour change drives defensive change

**Australian context:** Connects to the ACSC's event-logging guidance — visibility
is the precondition for detecting prioritised techniques.

---

## Labs & Exercises

### Lab 1: Mapping an Intrusion to ATT&CK

**Objective:** Deconstruct a documented intrusion into its TTPs, map them to MITRE
ATT&CK, and represent the sequence as an Attack Flow.

**Prerequisites:**
- Topics 2, 3, and 4

**Environment:**
- Operating System: any (analysis lab)
- Tools: MITRE ATT&CK website, ATT&CK Navigator (free, runs locally or in
  browser), CTID Attack Flow Builder (free) — all free/OSS
- Minimum hardware: trivial; no GPU; within spec

**Instructions:**

1. Read the provided intrusion report (e.g. an ACSC advisory or a public incident
   write-up).
2. Extract each distinct adversary behaviour and assign the matching ATT&CK
   tactic and technique/sub-technique ID.
3. Build a layer in ATT&CK Navigator highlighting the techniques observed.
4. Construct an Attack Flow showing the order in which techniques were chained.
5. For three techniques, record the ATT&CK-listed data sources that would reveal
   them.
6. Note any technique you could *not* confidently map and explain the ambiguity.

**Expected Output:**

A Navigator layer and an Attack Flow for the intrusion, a TTP table with
technique IDs, and the data sources for three techniques. Learners can justify
each mapping against evidence in the report.

**Reflection Questions:**

1. Which techniques in this intrusion sat high on the Pyramid of Pain, and why
   would detecting them hurt the adversary most?
2. Where did the report leave behaviour ambiguous, and how would that ambiguity
   affect a real detection effort?
3. How would this Attack Flow change if the adversary swapped one tool for
   another? Which detections would survive?

---

### Lab 2: Threat-Informed Prioritisation with Navigator

**Objective:** Use threat-informed defense to prioritise which techniques a given
organisation should detect first, and identify its visibility gaps.

**Prerequisites:**
- Topics 1, 5, and 6 and Lab 1

**Environment:**
- Operating System: any
- Tools: ATT&CK Navigator, CTID Top ATT&CK Techniques and Sensor Mappings/
  Mappings Explorer (free), a spreadsheet
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario organisation (e.g. a mid-size Australian services firm,
   Windows/AD estate, cloud email).
2. Select two relevant threat profiles (e.g. an actor from an ACSC advisory plus
   a commodity ransomware pattern) and build a combined Navigator layer of their
   techniques.
3. Use CTID Top ATT&CK Techniques to rank the overlapping techniques by
   prioritisation signal.
4. Using Sensor Mappings / Mappings Explorer, list the telemetry/data sources
   needed to detect the top 10 techniques.
5. Compare against the organisation's assumed current logging (from F06/OC02
   knowledge) and mark each technique as Covered / Partial / Gap.
6. Recommend three concrete changes (a new log source, a detection, or an
   automation) to close the most important gaps.

**Expected Output:**

A prioritised technique list, a coverage map (Covered/Partial/Gap), and three
justified recommendations to close gaps. Learners can explain why their top
priorities reflect the organisation's real threat exposure.

**Reflection Questions:**

1. How did threat-informed prioritisation change what you would defend first
   compared with a generic "harden everything" approach?
2. Which visibility gap would you close first, and what telemetry change does it
   require?
3. How would you re-run this prioritisation in six months as the threat landscape
   shifts — and why is that recurring cycle the essence of threat-informed
   defense?

---

## Assessment

### Formative Assessment: ATT&CK Technique Identification

**Type:** Self-check exercise with answer key

**Description:** Students are given short behavioural descriptions ("the malware
created a scheduled task to re-launch at logon") and must assign the correct
ATT&CK tactic and technique ID. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with the correct technique IDs and a note on
common mis-mappings.

---

### Summative Assessment: Threat-Informed Defense Brief

**Type:** Analytical report

**Description:** Given an Australian-relevant threat profile and a target
organisation, students produce a threat-informed defense brief that (a) maps the
actor's TTPs to ATT&CK with an Attack Flow, (b) prioritises techniques using a
defensible method, (c) analyses the organisation's visibility gaps against the
required data sources, and (d) recommends a prioritised set of detection,
logging, infrastructure, and automation changes — explicitly framed as an
adaptive loop. Deliverable: 2,000–2,500 word brief with Navigator/Attack Flow
artefacts.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| TTP mapping + Attack Flow | LO1, LO2 |
| Technique prioritisation | LO3, LO4 |
| Visibility-gap analysis & recommendations | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| ATT&CK mapping accuracy | All TTPs correctly mapped with precise IDs and sequence | Mostly correct mapping with minor errors | Several mapping errors | Frequent misidentification |
| Threat-informed prioritisation | Insightful, well-justified, tied to real threat exposure | Sound prioritisation with valid rationale | Generic prioritisation, weak rationale | Unprioritised or unjustified |
| Visibility-gap analysis | Precise gap analysis tied to data sources; actionable recs | Solid analysis with adequate recs | Partial analysis; vague recs | Little meaningful analysis |
| Adaptive framing | Clearly frames defence as a continuous, adapting loop | Acknowledges adaptation adequately | Mentions adaptation superficially | Treats defence as static |
| Communication | Clear, structured, professional, evidence-linked | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories & Annual Cyber Threat Report:** Used as the source of
  Australian-relevant threat profiles for both labs and the summative brief.
- **ASD Essential Eight & ACSC event-logging guidance:** Connected to the
  visibility requirements for detecting prioritised techniques.
- **Open CTID tooling:** Emphasised as enabling Australian organisations of any
  size to adopt threat-informed defense without commercial licensing.

---

## Further Reading

**MITRE ATT&CK (2024).** *ATT&CK for Enterprise.* The MITRE Corporation. https://attack.mitre.org
> Relevance: The core knowledge base used throughout this unit; CC BY 4.0, freely usable.

**MITRE Center for Threat-Informed Defense (2024).** *Adversary Emulation Library, Attack Flow, Summiting the Pyramid, Top ATT&CK Techniques, M3TID.* CTID. https://ctid.mitre.org / https://github.com/center-for-threat-informed-defense
> Relevance: The open CTID research and tooling that operationalise threat-informed defense across this unit.

**Bianco, D. (2013).** *The Pyramid of Pain.* https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html
> Relevance: The foundational concept behind durable, behaviour-based detection in Topic 4.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report & threat advisories.* ACSC. https://www.cyber.gov.au/about-us/reports-and-statistics
> Relevance: The authoritative source on Australian-relevant adversary behaviour used in both labs (Australian source).

**Strom, B. et al. (2018/updated).** *MITRE ATT&CK: Design and Philosophy.* The MITRE Corporation. https://attack.mitre.org/resources/
> Relevance: Explains the structure and intent of ATT&CK, supporting correct, defensible mapping.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | OC01 |
| Unit Title | Adversary Tradecraft & TTPs |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Operational Core |
| Major / Pathway | Operational |
| Prerequisites | F04, F06 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | None directly (ACSC threat reporting / Essential Eight context) |
