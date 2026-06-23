# DE03: Writing Detection Logic

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This is the hands-on core of the major: writing, converting, and testing detection
logic. Students author detections in **Sigma** (the vendor-neutral standard),
convert them to platform query languages (**SPL**, **KQL**), and write **YARA**
rules for file-based detection — all mapped to ATT&CK (v19) and tested against
sample data. The emphasis is on durable, low-false-positive logic and on the
discipline of testing every rule before it is trusted.

Writing good detection logic is where threat-informed defense becomes concrete
code. In the Australian context, the techniques targeted are those reported by the
ACSC as active against Australian organisations. DE03 builds on DE01 (theory), DE02
(data), and OC02 (SIEM/Sigma), and feeds DE04 (testing) and the DE06 capstone.

---

## Prerequisites

- DE02 — Data Sources & Log Engineering
- OC02 — Security Monitoring & SIEM

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** Sigma detection rules for specified ATT&CK (v19) techniques.
2. **Apply** rule conversion to translate Sigma into SPL and KQL.
3. **Build** YARA rules for file-based detection from static indicators.
4. **Evaluate** detection logic against sample data for true/false positives.
5. **Analyse** rules for evasion weaknesses and refine them.
6. **Recommend** a tested, ATT&CK-mapped rule set for a technique group.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of detection
languages and rule construction.

**Skills (AQF 7.2):** Students develop technical skills by writing, converting, and
testing detection rules.

**Application (AQF 7.3):** Students apply rule-writing to real techniques and
produce tested, deployable detection logic.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Develop and test detection logic for adversary techniques | Lab 1 — Writing Sigma Rules |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0294 | Convert and validate detections across platforms | Lab 2 — Conversion & Testing |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 4 | Lab 1, Lab 2 |
| Programming / software development | PROG | Level 3–4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Detection Engineering | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | DE03-K01 | Knowledge of the Sigma rule standard | Topic 1 |
| Knowledge | DE03-K02 | Knowledge of translating behaviour into detection logic | Topic 2 |
| Knowledge | DE03-K03 | Knowledge of rule conversion (Sigma to SPL/KQL) and YARA | Topic 3; Topic 4 |
| Knowledge | DE03-K04 | Knowledge of testing, false-positive analysis, and evasion-resistant rules | Topic 5; Topic 6 |
| Skill | DE03-S01 | Skill in writing Sigma rules | Lab 1 |
| Skill | DE03-S02 | Skill in converting and testing detections across platforms | Lab 2 |
| Ability | DE03-A01 | Ability to author behaviour-based, evasion-resistant detections | Lab 1; Topic 6 |
| Ability | DE03-A02 | Ability to validate detections and manage false positives | Lab 2; Topic 5 |
| Task | T0259 | Develop and test detection logic for adversary techniques | Lab 1 |
| Task | T0294 | Convert and validate detections across platforms | Lab 2 |

---

## Topics

### Topic 1: The Sigma Rule Standard

This topic teaches the Sigma format in depth: logsource, detection (selections,
conditions), modifiers, fields, false-positive notes, level, and ATT&CK tagging —
and why a vendor-neutral standard matters for portability and sharing.

**Key concepts:**
- Sigma structure: logsource, detection, condition
- Modifiers, fields, and metadata
- ATT&CK tagging and portability

---

### Topic 2: Translating Behaviour into Logic

This topic teaches turning a behavioural hypothesis into precise logic: identifying
the observable fields, expressing the behaviour specifically enough to avoid noise
but generally enough to catch variants, and reasoning about the boundary.

**Key concepts:**
- Behaviour → observable fields → logic
- Specificity vs generality trade-off
- Reasoning about rule boundaries

---

### Topic 3: Rule Conversion (Sigma → SPL/KQL)

This topic teaches converting Sigma to platform query languages with pySigma/sigma-
cli and by hand, understanding backend differences, and validating that the
converted query preserves the rule's intent.

**Key concepts:**
- pySigma / sigma-cli conversion
- SPL and KQL idioms
- Validating conversion fidelity

---

### Topic 4: YARA for File-Based Detection

This topic teaches YARA: strings and conditions, writing rules from durable static
features (not just hashes), and using YARA for malware family detection — connecting
to OC03/CT03.

**Key concepts:**
- YARA strings and conditions
- Durable static features over hashes
- Family-level detection

---

### Topic 5: Testing and False-Positive Analysis

A rule is not trusted until tested. This topic teaches testing rules against
sample malicious and benign data, measuring true/false positives, and tuning to
reduce noise without losing the true positive.

**Key concepts:**
- Testing against malicious + benign data
- Measuring true/false positives
- Tuning without losing coverage

---

### Topic 6: Evasion-Resistant Rules

This topic teaches anticipating evasion: how adversaries bypass brittle logic
(obfuscation, alternate paths), and how CTID *Summiting the Pyramid* helps assess
and improve analytic robustness.

**Key concepts:**
- Common evasion against detections
- Robustness assessment (Summiting the Pyramid)
- Designing resilient logic

**Australian context:** Rules target techniques from ACSC advisories, validated to
resist realistic evasion.

---

## Labs & Exercises

### Lab 1: Writing Sigma Rules

**Objective:** Write five Sigma rules for ATT&CK Execution-tactic techniques and tag
them correctly.

**Prerequisites:**
- Topics 1, 2, and 5

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: a text editor, sigma-cli, sample endpoint telemetry, ATT&CK Navigator
  (v19) — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 20 GB disk (within the 8 GB / 4-core /
  50 GB spec; no GPU)

**Instructions:**

1. Choose five Execution-tactic techniques present in the sample telemetry.
2. Write a Sigma rule for each: correct logsource, specific detection, condition,
   false-positive notes, level, and ATT&CK (v19) tag.
3. Validate each rule's syntax with sigma-cli.
4. Run each against the sample data and confirm it fires on the malicious activity.
5. Note the false-positive risk for each rule.
6. Commit the rules to a Git repository (detection-as-code).

**Expected Output:**

Five valid, ATT&CK-tagged Sigma rules that fire correctly on the sample data, with
false-positive notes, committed to Git. Learners can explain the behaviour each
rule targets.

**Reflection Questions:**

1. Which rule risked the most false positives, and how did you constrain it?
2. Where did you trade specificity for catching variants?
3. Which rule is most evasion-resistant, and why?

---

### Lab 2: Conversion & Testing

**Objective:** Convert Sigma rules to SPL and KQL, write a YARA rule, and test all
against sample data.

**Prerequisites:**
- Topics 3, 4, and 6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM (+ a free SIEM: OpenSearch/Splunk Free)
- Tools: sigma-cli/pySigma, YARA, a free SIEM, sample data — all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 30 GB disk (within spec; no GPU)

**Instructions:**

1. Convert two Lab 1 Sigma rules to SPL and KQL; verify the queries preserve intent.
2. Run the converted SPL query in the free SIEM against ingested sample data.
3. Write a YARA rule for a provided malware family using durable static features.
4. Test the YARA rule against the sample (matches the family, not just one hash).
5. Measure true/false positives for one detection and tune it.
6. Document the tested rule set with evidence.

**Expected Output:**

Converted SPL/KQL queries verified against sample data, a working YARA rule that
matches the family, a tuning result with metrics, and documented evidence. Learners
can explain backend differences encountered in conversion.

**Reflection Questions:**

1. What changed between the Sigma rule and its SPL/KQL conversions?
2. Why is your YARA rule more durable than a hash match?
3. How did tuning trade precision against recall?

---

## Assessment

### Formative Assessment: Rule Critique

**Type:** Self/peer review exercise with answer key

**Description:** Given draft Sigma/YARA rules, students identify syntax issues,
false-positive risks, and evasion weaknesses, and rewrite the weakest. Self-marked.

**Learning Outcomes Assessed:** LO1, LO5

**Feedback mechanism:** Answer key with corrected rules and rationale.

---

### Summative Assessment: Tested Detection Rule Set

**Type:** Practical project with report

**Description:** For an assigned ATT&CK technique group (from an Australian-relevant
actor), students (a) write a set of Sigma rules, (b) convert key rules to SPL/KQL,
(c) write at least one YARA rule, and (d) test all rules against sample data with
false-positive analysis and evasion assessment. Deliverable: a Git repo of tested,
ATT&CK-tagged rules + a 2,000–2,500 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Sigma rule set | LO1 |
| Conversion (SPL/KQL) | LO2 |
| YARA rule | LO3 |
| Testing, FP analysis, evasion | LO4, LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Rule quality | Precise, durable, well-tagged | Correct with minor issues | Works but brittle | Incorrect |
| Conversion | Faithful SPL/KQL with backend awareness | Mostly faithful | Partial | Broken |
| YARA | Durable, family-level rule | Adequate | Hash-like | Poor |
| Testing & evasion | Rigorous FP analysis + evasion assessment | Adequate | Partial | Untested |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories:** Source of the techniques and behaviours detections target.
- **ASD Essential Eight:** Detections support monitoring of control-bypass
  behaviours.
- **Community sharing:** Vendor-neutral Sigma enables contribution to Australian
  sharing communities.

---

## Further Reading

**SigmaHQ (2024).** *Sigma specification & rule repository.* https://github.com/SigmaHQ/sigma
> Relevance: The detection standard and reference rules used throughout this unit.

**pySigma / sigma-cli (2024).** *Documentation.* https://github.com/SigmaHQ/pySigma
> Relevance: The free conversion tooling used in Topic 3 and Lab 2.

**VirusTotal / YARA (2024).** *YARA documentation.* https://virustotal.github.io/yara/
> Relevance: The file-detection tool used in Topic 4 and Lab 2.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Summiting the Pyramid.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The analytic-robustness method for Topic 6.

**Australian Cyber Security Centre (2024).** *Threat advisories.* ACSC. https://www.cyber.gov.au
> Relevance: Australian-relevant techniques targeted by the detections (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DE03 |
| Unit Title | Writing Detection Logic |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Detection Engineering |
| Prerequisites | DE02, OC02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (ACSC advisory context) |
