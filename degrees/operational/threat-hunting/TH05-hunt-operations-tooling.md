# TH05: Hunt Operations & Tooling

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit turns hunting skills into a repeatable operation. It covers the tooling
and engineering that let a hunt team work efficiently and reproducibly: Jupyter
notebooks with Pandas for analysis and documentation, Velociraptor VQL for
fleet-scale collection, log-platform queries (Elastic/OpenSearch), and converting
findings into Sigma detections. It also covers the operational wrapper —
reproducible hunts, automation, collaboration, and metrics — that distinguishes a
mature hunt capability from a talented individual.

This unit is where the threat-informed-defense loop becomes engineered: hunts are
codified as notebooks and queries, findings flow into detections (OC02) and
intelligence (OC05), and automation keeps the cycle running as the adversary
evolves (ATT&CK v19). In the Australian context, reproducible, well-documented
hunting supports the evidence and assurance expectations of regulated and
critical-infrastructure environments. TH05 builds on TH01–TH04 and F03 (Scripting).

---

## Prerequisites

- TH03 — Host-Based Hunting
- TH04 — Network-Based Hunting
- F03 — Scripting & Automation

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** Jupyter notebooks with Pandas to analyse hunt data and produce
   reproducible, documented hunts.
2. **Apply** Velociraptor VQL to execute and collect hunts across an endpoint
   fleet.
3. **Analyse** log-platform query results (Elastic/OpenSearch) to test hunt
   hypotheses at scale.
4. **Evaluate** hunt tooling and design a reproducible hunt workflow.
5. **Recommend** automation for recurring hunts and the conversion of findings into
   Sigma detections.
6. **Analyse** hunt-program metrics to demonstrate value and guide improvement.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of hunt tooling,
reproducible workflows, and operationalisation.

**Skills (AQF 7.2):** Students develop technical and evaluative skills by building
notebooks, queries, and automation and assessing tooling.

**Application (AQF 7.3):** Students apply tooling to operationalise hunts in
realistic environments and demonstrate value through metrics.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0166 | Perform correlation and analysis across data sets to detect threats | Lab 1 — Hunt Notebook in Jupyter |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Execute fleet-scale hunts and identify anomalous activity | Lab 2 — Fleet Hunt with Velociraptor VQL |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Programming / software development | PROG | Level 3–4 | Lab 1 |

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
| Knowledge | TH05-K01 | Knowledge of the hunt operations model | Topic 1 |
| Knowledge | TH05-K02 | Knowledge of notebooks for reproducible hunting | Topic 2 |
| Knowledge | TH05-K03 | Knowledge of fleet collection and VQL at scale | Topic 3 |
| Knowledge | TH05-K04 | Knowledge of automation, detection hand-off, and hunt metrics | Topic 5; Topic 6 |
| Skill | TH05-S01 | Skill in building a reproducible hunt notebook in Jupyter | Lab 1 |
| Skill | TH05-S02 | Skill in running a fleet hunt with Velociraptor VQL | Lab 2 |
| Ability | TH05-A01 | Ability to operate hunts repeatably across a fleet | Lab 2; Topic 3 |
| Ability | TH05-A02 | Ability to demonstrate hunt program value through metrics | Topic 6; Summative |
| Task | T0166 | Perform correlation and analysis across data sets to detect threats | Lab 1 |
| Task | T0259 | Execute fleet-scale hunts and identify anomalous activity | Lab 2 |

---

## Topics

### Topic 1: The Hunt Operations Model

This topic covers running hunting as an operation: the hunt backlog, cadence,
roles, collaboration, and how hunting interfaces with the SOC, detection
engineering, and CTI. It frames tooling choices as serving reproducibility and
hand-off.

**Key concepts:**
- Hunt backlog, cadence, and roles
- Interfaces to SOC / detection / CTI
- Reproducibility and hand-off as goals

---

### Topic 2: Notebooks for Reproducible Hunting

Jupyter + Pandas makes hunts reproducible and self-documenting. This topic teaches
structuring a hunt notebook: parameterised inputs, data loading, analysis steps
with narrative, visualisations, and a findings section that can be re-run as the
data changes.

**Key concepts:**
- Notebook structure for hunts
- Pandas for filtering, aggregation, and stacking
- Self-documenting, re-runnable analysis

---

### Topic 3: Fleet Collection and VQL at Scale

This topic deepens Velociraptor from TH03 to operational scale: writing VQL hunts,
scheduling collections, and stacking artefacts across a large fleet to surface
outliers — and managing the data volume responsibly.

**Key concepts:**
- VQL hunt authoring and scheduling
- Fleet-wide stacking and outlier surfacing
- Managing collection volume

---

### Topic 4: Log-Platform Hunting at Scale

This topic covers hunting in Elastic/OpenSearch: efficient queries, aggregations,
and pivots across large datasets; building reusable saved searches; and combining
platform queries with notebook analysis.

**Key concepts:**
- Efficient platform queries and aggregations
- Reusable saved searches
- Combining platform + notebook workflows

---

### Topic 5: Automation and Detection Hand-off

This topic teaches automating recurring hunts (scheduled notebooks/queries, alert
on outliers) and the disciplined conversion of findings into Sigma detections for
the SOC — deciding what to automate vs keep as analyst-led, and avoiding alert
fatigue.

**Key concepts:**
- Automating recurring/"reusable" hunts
- Finding → Sigma detection hand-off
- Automate vs analyst-led judgement

---

### Topic 6: Hunt Metrics and Program Value

This topic covers measuring a hunt program: coverage (techniques hunted),
outcomes (findings, detections created, dwell-time reduction), and efficiency, and
communicating value to stakeholders (linking to SC05/SC06) without resorting to
vanity metrics.

**Key concepts:**
- Coverage, outcome, and efficiency metrics
- Avoiding vanity metrics
- Communicating program value

**Australian context:** Metrics framed to evidence assurance and detection maturity
for regulated/critical-infrastructure contexts.

---

## Labs & Exercises

### Lab 1: Hunt Notebook in Jupyter

**Objective:** Build a reproducible hunt notebook using Pandas against log data and
a log platform.

**Prerequisites:**
- Topics 2 and 4 and F03

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Jupyter, Python 3 + Pandas, OpenSearch/Elastic (free), sample log data —
  all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 30 GB disk (within spec; no GPU)

**Instructions:**

1. Create a parameterised Jupyter notebook (e.g. time window, host filter).
2. Load the sample dataset (from file and/or a platform query) into a Pandas
   DataFrame.
3. Implement a hunt: aggregate and stack to surface outliers (e.g. rare parent-
   child process pairs).
4. Add narrative markdown explaining each analytic step.
5. Visualise the key result (e.g. a frequency chart).
6. Write a findings section and re-run the notebook to confirm reproducibility.

**Expected Output:**

A re-runnable, documented hunt notebook that surfaces an outlier, with narrative,
a visualisation, and findings. Learners can re-run it on new data and explain each
step.

**Reflection Questions:**

1. How does a notebook improve on ad-hoc querying for repeatability and hand-off?
2. Which part of this hunt would you automate, and which keep analyst-led?
3. How would you parameterise this to run weekly?

---

### Lab 2: Fleet Hunt with Velociraptor VQL

**Objective:** Author and execute a VQL hunt across a simulated endpoint fleet and
convert a finding into a detection.

**Prerequisites:**
- Topics 3 and 5 and Lab 1

**Environment:**
- Operating System: Velociraptor server + endpoint VM(s) or the provided fleet
  collection
- Tools: Velociraptor (VQL), Sigma, ATT&CK Navigator — all free/OSS
- Minimum hardware: run components sequentially — 6 GB RAM / 2 vCPU / 30 GB disk
  (within spec; no GPU)

**Instructions:**

1. Write a VQL hunt for a chosen technique (e.g. scheduled-task persistence,
   T1053).
2. Execute it across the fleet (or the provided collection) and collect results.
3. Stack the results to identify the outlier host(s).
4. Investigate and confirm the finding with a verdict and ATT&CK (v19) mapping.
5. Convert the confirmed behaviour into a Sigma detection.
6. Document the hunt for re-use (schedule + hand-off note to the SOC).

**Expected Output:**

A working VQL hunt, stacked fleet results identifying an outlier, a confirmed
finding, a Sigma detection, and a re-use/hand-off note. Learners can explain how
this becomes a recurring, automatable hunt.

**Reflection Questions:**

1. How did stacking across the fleet make the outlier obvious?
2. What did you choose to automate vs keep analyst-led, and why?
3. How does the detection hand-off close the threat-informed-defense loop?

---

## Assessment

### Formative Assessment: Tooling Fit Exercise

**Type:** Short-answer exercise with answer key

**Description:** Given hunt scenarios, students choose the right tool (notebook,
VQL, platform query) and justify the choice and the reproducibility approach.
Self-marked.

**Learning Outcomes Assessed:** LO4, LO5

**Feedback mechanism:** Answer key with the recommended tooling and rationale per
scenario.

---

### Summative Assessment: Operationalised Hunt Package

**Type:** Practical project with report

**Description:** Students operationalise a hunt end-to-end: (a) a reproducible
Jupyter notebook, (b) a Velociraptor VQL hunt, (c) at least one Sigma detection
derived from a finding, (d) an automation/cadence plan, and (e) a short report with
proposed hunt metrics. Deliverable: a notebook + VQL + Sigma artefacts and a
2,000–2,500 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Reproducible notebook | LO1, LO3 |
| Fleet VQL hunt | LO2 |
| Workflow & automation design | LO4, LO5 |
| Metrics & value | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Reproducibility | Fully re-runnable, documented, parameterised | Mostly reproducible | Partially | Not reproducible |
| Tooling competence | Skilled notebook + VQL + platform use | Solid use | Basic | Poor |
| Automation & hand-off | Sound automation and detection hand-off | Reasonable | Superficial | Absent |
| Metrics | Meaningful, non-vanity metrics | Adequate | Weak | Missing |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Assurance expectations:** Reproducible, documented hunting framed as evidence
  for regulated and SOCI-covered environments.
- **ACSC advisories:** Provide the techniques operationalised in the labs.
- **ASD Essential Eight:** Recurring hunts target control-bypass behaviours.

---

## Further Reading

**Project Jupyter (2024).** *Jupyter & the Pandas documentation.* https://jupyter.org / https://pandas.pydata.org
> Relevance: The free analysis environment used to build reproducible hunts in Lab 1.

**Velociraptor / Rapid7 (2024).** *VQL & Hunting documentation.* https://docs.velociraptor.app
> Relevance: The free fleet-hunting platform and query language used in Lab 2.

**Lee, R. & Bianco, D. (2016/updated).** *Generating Hypotheses for Successful Threat Hunting & hunt operations guidance.* SANS Institute. https://www.sans.org/white-papers/
> Relevance: Practitioner guidance on running hunts as an operation (Topics 1, 6).

**Australian Cyber Security Centre (2024).** *Event-logging & detection guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian expectations for the telemetry and detection that hunts rely on (Australian source).

**SigmaHQ (2024).** *Sigma rule format.* https://github.com/SigmaHQ/sigma
> Relevance: The detection format used for the hunt→detection hand-off.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | TH05 |
| Unit Title | Hunt Operations & Tooling |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Threat Hunting |
| Prerequisites | TH03, TH04, F03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
