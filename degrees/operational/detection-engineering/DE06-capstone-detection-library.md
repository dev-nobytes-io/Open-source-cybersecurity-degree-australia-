# DE06: Capstone — Detection Library

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

The capstone integrates the entire Detection Engineering major into a single
deliverable: a tested, documented detection rule library for a defined threat
scenario. Students scope a threat, map required data sources, author 10+ Sigma
rules, validate every rule with Atomic Red Team (or equivalent), conduct
false-positive analysis, produce an ATT&CK (v19) coverage map, and export a
deployment-ready library — a portfolio-grade artefact suitable for employer review.
It is assessed at the highest cognitive levels: students **create** and **evaluate**
a complete detection capability for a scenario.

The capstone realises the threat-informed-defense build loop end-to-end:
intelligence → data → detection → validation → coverage. In the Australian context,
the scenario references an ACSC-identified threat group or advisory, and the library
evidences the kind of detection maturity expected under the Essential Eight and
SOCI. DE06 requires DE01–DE05 and the operational core.

---

## Prerequisites

- DE01 — Detection Theory & Philosophy
- DE02 — Data Sources & Log Engineering
- DE03 — Writing Detection Logic
- DE04 — Adversary Simulation for Detection
- DE05 — Detection Operations & Management

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** the scope and data-source mapping for a detection library targeting a
   defined threat.
2. **Create** a library of 10+ ATT&CK-mapped Sigma detection rules.
3. **Evaluate** every rule through simulation-based testing and false-positive
   analysis.
4. **Create** an ATT&CK (v19) coverage map and a deployment-ready export.
5. **Evaluate** the library's coverage and quality against the threat scenario.
6. **Recommend** maintenance and improvement for the library over time.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** The capstone consolidates specialised detection-engineering
knowledge into an integrated, tested deliverable.

**Skills (AQF 7.2):** Students demonstrate the highest-order skills — creating and
evaluating a complete detection library independently.

**Application (AQF 7.3):** Students apply the full detection-engineering cycle to an
Australian-relevant threat and produce an employer-grade artefact.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Build and test a detection library for a threat scenario | Lab 1 — Build & Test the Library |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0294 | Analyse coverage and produce deployment-ready content | Lab 2 — Coverage, FP Analysis & Export |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 4 | Lab 1, Lab 2 |
| Programming / software development | PROG | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Detection Engineering | Advanced | Lab 1, Lab 2 |

---

## Topics

> The capstone is a supervised, integrative project. These "topics" are the
> production phases and guidance; the substantive work is the student's own
> detection library.

### Topic 1: Capstone Scope and Threat Scenario

This phase defines the threat scenario (e.g. ransomware pre-deployment, APT lateral
movement), referencing an ACSC-identified group or advisory, plus deliverables and
success criteria, agreed with the supervisor.

**Key concepts:**
- Scenario selection (ACSC-grounded)
- Deliverables and success criteria
- Scoping the technique set

---

### Topic 2: Data Source Mapping

Students map the scenario's techniques to the required data sources (DE02),
documenting what logs the library depends on and any visibility gaps to flag.

**Key concepts:**
- Technique-to-data-source mapping
- Documenting log dependencies
- Flagging visibility gaps

---

### Topic 3: Authoring the Rule Set

Students author 10+ Sigma rules (DE03) covering the scenario's techniques, each
ATT&CK (v19)-tagged with false-positive notes and a level.

**Key concepts:**
- Authoring a coherent rule set
- ATT&CK tagging and metadata
- Specificity vs variant-coverage

---

### Topic 4: Validation and False-Positive Analysis

Students validate every rule with Atomic Red Team (DE04) and conduct false-positive
analysis against benign data, recording evidence of testing.

**Key concepts:**
- Simulation-based validation of each rule
- False-positive analysis
- Evidence of testing

---

### Topic 5: Coverage Mapping and Export

Students produce an ATT&CK Navigator coverage map (detected/tested) and export the
library in Sigma format, deployment-ready, with documentation.

**Key concepts:**
- Coverage map (Navigator)
- Deployment-ready Sigma export
- Library documentation

**Australian context:** Coverage reflects an ACSC-identified threat and Essential
Eight monitoring expectations.

---

### Topic 6: Evaluation and Maintenance

Students evaluate the library against the scenario (coverage, quality, gaps) and
recommend a maintenance/improvement plan, plus package a portfolio artefact for
review.

**Key concepts:**
- Self-evaluation against the scenario
- Maintenance/improvement plan
- Portfolio artefact

---

## Labs & Exercises

### Lab 1: Build & Test the Library

**Objective:** Author and validate the detection rule library for the scenario.

**Prerequisites:**
- Topics 1–4

**Environment:**
- Operating System: an isolated test environment (Windows VM + free SIEM) + sigma-cli
- Tools: Sigma/sigma-cli, free SIEM (OpenSearch/Splunk Free), Invoke-AtomicRedTeam,
  ATT&CK Navigator (v19), Git — all free/OSS
- Minimum hardware: run sequentially — within the 8 GB / 4-core / 50 GB spec; no
  GPU. **Isolated network for simulation.**

**Instructions:**

1. Confirm the scenario scope and technique set with your supervisor.
2. Map the techniques to required data sources; document dependencies.
3. Author 10+ Sigma rules covering the techniques, ATT&CK (v19)-tagged.
4. Validate each rule by executing the matching Atomic test in isolation.
5. Record detected/missed with firing-event evidence; fix misses and re-validate.
6. Commit the library and test evidence to Git.

**Expected Output:**

A Git repository of 10+ ATT&CK-tagged Sigma rules, each validated with test
evidence (and misses fixed), plus documented data dependencies. Learners can show
the firing event for each tested rule.

**Reflection Questions:**

1. Which technique was hardest to detect reliably, and why?
2. Which miss did you fix, and what was its root cause?
3. Where did you trade specificity for catching variants?

---

### Lab 2: Coverage, FP Analysis & Export

**Objective:** Produce the coverage map, false-positive analysis, and
deployment-ready export.

**Prerequisites:**
- Topics 5–6 and Lab 1

**Environment:**
- Operating System: the Lab 1 environment
- Tools: ATT&CK Navigator (v19), the free SIEM, sigma-cli, `templates/student-
  portfolio/index.html` — all free
- Minimum hardware: as Lab 1

**Instructions:**

1. Run each rule against benign sample data and record false-positive rates.
2. Tune any noisy rules (DE05) without losing the true positive.
3. Produce an ATT&CK Navigator coverage map (techniques detected/tested).
4. Export the library in Sigma format, documented and deployment-ready.
5. Evaluate the library against the scenario (coverage, quality, gaps).
6. Package a portfolio artefact and submit for community practitioner review.

**Expected Output:**

A false-positive analysis with tuning, a coverage map, a documented deployment-ready
Sigma export, a self-evaluation, and a portfolio artefact suitable for employer
review.

**Reflection Questions:**

1. What is your honest coverage of the scenario, and where are the gaps?
2. Which rule needed the most tuning, and how did you preserve coverage?
3. If you maintained this library for a year, what would you prioritise?

---

## Assessment

### Formative Assessment: Scope & Plan Gate

**Type:** Supervisor/peer review of scope, technique set, and data mapping

**Description:** Before building, the scenario scope, technique set, and data-source
mapping are reviewed for feasibility; students revise. A go/no-go gate into the
build.

**Learning Outcomes Assessed:** LO1

**Feedback mechanism:** Structured feedback against a plan rubric; revision required.

---

### Summative Assessment: Tested Detection Library

**Type:** Detection library with testing evidence, coverage map, and portfolio
artefact

**Description:** The complete deliverable: a defined scenario, data-source mapping,
10+ validated Sigma rules with testing evidence, false-positive analysis, an ATT&CK
(v19) coverage map, a deployment-ready Sigma export, a self-evaluation, and a
maintenance plan — subject to community practitioner review. Deliverable: a Git
repository of the library + a 3,000–4,000 word report and portfolio artefact.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Scope & data mapping | LO1 |
| Rule library | LO2 |
| Validation & FP analysis | LO3 |
| Coverage map & export | LO4 |
| Evaluation & maintenance | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Library quality | 10+ durable, well-tagged, tested rules | Solid library | Partial/brittle | Inadequate |
| Validation | Every rule tested with evidence; misses fixed | Most tested | Partial | Untested |
| FP analysis & tuning | Rigorous; coverage preserved | Adequate | Superficial | Poor |
| Coverage & export | Honest map; clean deployment-ready export | Sound | Partial | Poor |
| Evaluation & portfolio | Insightful; employer-grade artefact | Professional | Thin | Poor |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC-identified threat:** The capstone scenario references an ACSC group or
  advisory.
- **ASD Essential Eight & SOCI:** The library evidences monitoring/detection
  maturity expectations.
- **ACSC event-logging guidance:** Underpins the data the library depends on.

---

## Further Reading

**SigmaHQ (2024).** *Sigma specification & rule repository.* https://github.com/SigmaHQ/sigma
> Relevance: The standard and reference rules for the capstone library.

**Red Canary (2024).** *Atomic Red Team.* https://github.com/redcanaryco/atomic-red-team
> Relevance: The validation library used to test every rule.

**MITRE ATT&CK (v19, 2026).** *ATT&CK for Enterprise & Navigator.* https://attack.mitre.org
> Relevance: The technique taxonomy and coverage-mapping tool for the capstone.

**Australian Cyber Security Centre (2024).** *Threat advisories & event-logging guidance.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian threat scenario and logging basis for the capstone (Australian source).

**Templates — Student Portfolio.** `templates/student-portfolio/index.html` (this repository).
> Relevance: The portfolio artefact format the capstone deliverable must populate (Australian-context degree resource).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DE06 |
| Unit Title | Capstone — Detection Library |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 24 CP |
| Degree Layer | Capstone |
| Major / Pathway | Detection Engineering |
| Prerequisites | DE01, DE02, DE03, DE04, DE05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 5–6 (Evaluate, Create) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
