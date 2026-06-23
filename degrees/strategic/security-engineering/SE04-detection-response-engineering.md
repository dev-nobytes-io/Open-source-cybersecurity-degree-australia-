# SE04: Detection & Response Engineering

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (security architecture/engineering)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches the *engineering* of detection and response capability — designing
the SIEM/SOAR/XDR platforms and automation pipelines that the operational majors
(OC02, Detection Engineering) run on. Where the Detection Engineering major focuses
on authoring detections, SE04 focuses on architecting the platform: data pipelines,
storage and scaling, correlation, automation/orchestration, and the integration of
detection and response into a coherent, maintainable system.

This is the architectural backbone beneath threat-informed defense: a well-engineered
detection-and-response platform is what makes operational capability (and its
maturity — SOC-CMM/DML, see `docs/maturity-models.md`) achievable at scale. In the
Australian context the platform must satisfy ACSC logging expectations and support
NDB/SOCI reporting. SE04 builds on SE02, OC02 (Security Monitoring), and benefits from
the Detection Engineering major; it feeds SE05–SE06.

---

## Prerequisites

- SE02 — Security Architecture
- OC02 — Security Monitoring & SIEM

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** a SIEM architecture: collection, normalisation, storage, correlation,
   and alerting.
2. **Analyse** scaling, cost, and retention trade-offs in a detection platform.
3. **Design** SOAR automation pipelines and playbooks for response.
4. **Evaluate** XDR and integrated detection-and-response architectures.
5. **Analyse** the platform's alignment with ACSC logging and AU reporting needs.
6. **Recommend** a detection-and-response platform architecture for an organisation.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of detection-and-
response platform engineering.

**Skills (AQF 7.2):** Students develop design and automation skills by architecting
SIEM/SOAR and building playbooks.

**Application (AQF 7.3):** Students apply platform engineering to realistic
Australian organisations with logging/reporting alignment.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Architect (652) | SP-ARC-002 | T0050 | Design detection-and-response platform architecture | Lab 1 — SIEM Architecture Design |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0166 | Engineer correlation and automated response | Lab 2 — SOAR Playbook |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Solution architecture | ARCH | Level 4–5 | Lab 1 |
| Security operations | SCAD | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Security Architecture | Detection & Response Engineering | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | SE04-K01 | Knowledge of detection-and-response platform architecture | Topic 1 |
| Knowledge | SE04-K02 | Knowledge of SIEM architecture | Topic 2 |
| Knowledge | SE04-K03 | Knowledge of data-pipeline engineering and SOAR automation | Topic 3; Topic 4 |
| Knowledge | SE04-K04 | Knowledge of XDR and integrated architectures aligned with Australian needs | Topic 5; Topic 6 |
| Skill | SE04-S01 | Skill in designing a SIEM architecture | Lab 1 |
| Skill | SE04-S02 | Skill in building a SOAR playbook | Lab 2 |
| Ability | SE04-A01 | Ability to engineer a scalable detection-and-response platform | Lab 1; Topic 3 |
| Ability | SE04-A02 | Ability to automate correlation and response | Lab 2; Topic 4 |
| Task | T0050 | Design detection-and-response platform architecture | Lab 1 |
| Task | T0166 | Engineer correlation and automated response | Lab 2 |

---

## Topics

### Topic 1: Detection-and-Response Platform Architecture

This topic frames the platform as an engineered system: the data pipeline
(collection → normalisation → storage → correlation → alerting → response) and the
architectural decisions that determine whether operational detection can succeed.

**Key concepts:**
- The end-to-end detection-and-response pipeline
- Architecture decisions and their operational impact
- Platform vs content (engineering vs DE major)

---

### Topic 2: SIEM Architecture

This topic covers SIEM design: ingestion and parsing at scale, the common information
model, hot/warm/cold storage, indexing, and correlation — and the cost/volume/
retention trade-offs that dominate real deployments.

**Key concepts:**
- Ingestion, parsing, and normalisation at scale
- Storage tiers and retention
- Cost/volume/performance trade-offs

---

### Topic 3: Data Pipeline Engineering

This topic covers engineering the telemetry pipeline: collectors and forwarders,
parsing/enrichment, routing and filtering, and ensuring data quality (the dependency
beneath every detection, linking to DE02).

**Key concepts:**
- Collectors, forwarders, and routing
- Parsing, enrichment, and data quality
- Filtering for signal and cost

---

### Topic 4: SOAR and Automation

This topic teaches orchestration and automation: SOAR concepts, playbook design for
common incident types, human-in-the-loop vs full automation, and integrating SOAR
with the SIEM and ticketing.

**Key concepts:**
- SOAR concepts and playbook design
- Human-in-the-loop vs full automation
- Integration with SIEM/ticketing

---

### Topic 5: XDR and Integrated Architectures

This topic covers XDR and integrated detection-and-response: consolidating endpoint,
network, identity, and cloud telemetry and response, the trade-offs of integrated vs
best-of-breed, and vendor-neutral design considerations.

**Key concepts:**
- XDR and telemetry consolidation
- Integrated vs best-of-breed
- Vendor-neutral design

---

### Topic 6: Platform Alignment with Australian Needs

This topic covers engineering the platform to Australian expectations: ACSC
event-logging guidance, retention for investigation, and supporting NDB/SOCI
incident-reporting and the operational maturity (SOC-CMM) the platform enables.

**Key concepts:**
- ACSC logging/retention alignment
- Supporting NDB/SOCI reporting
- Enabling operational maturity (SOC-CMM)

**Australian context:** ACSC event-logging guidance and NDB/SOCI reporting needs.

---

## Labs & Exercises

### Lab 1: SIEM Architecture Design (design activity)

**Objective:** Design a SIEM deployment defining data sources, normalisation, and
correlation for an organisation.

**Prerequisites:**
- Topics 1–3 and 6

**Environment:**
- Operating System: any
- Tools: draw.io, ACSC logging reference, ATT&CK Navigator — all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take a fictional Australian organisation (size, estate, regulatory context).
2. Identify the required data sources (technique-driven, linking to DE02).
3. Design the ingestion/normalisation pipeline and storage/retention tiers.
4. Define a correlation approach and alert routing.
5. Estimate the cost/volume/retention trade-offs.
6. Map the design to ACSC logging expectations and NDB/SOCI retention needs.

**Expected Output:**

A SIEM architecture with data sources, pipeline, storage/retention, correlation, and
ACSC/NDB/SOCI alignment. Learners can justify the trade-offs.

**Reflection Questions:**

1. Which trade-off (cost vs coverage vs retention) was hardest, and how did you
   resolve it?
2. How does the data pipeline determine detection success (DE02)?
3. How does retention support NDB/SOCI reporting?

---

### Lab 2: SOAR Playbook (build activity)

**Objective:** Build a SOAR playbook for a common incident type in an open-source
platform.

**Prerequisites:**
- Topics 4–5 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: an open-source SOAR (Shuffle or n8n) — all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 25 GB disk (within spec; no GPU)

**Instructions:**

1. Stand up the open-source SOAR in the lab.
2. Choose a common incident type (e.g. phishing triage).
3. Design the playbook: triggers, enrichment, decision points, and actions.
4. Mark which steps are automated vs human-in-the-loop and justify.
5. Implement a basic version of the playbook in the SOAR.
6. Document how it integrates with a SIEM and ticketing.

**Expected Output:**

A working (basic) SOAR playbook for the chosen incident type, with automated vs
human steps justified and integration documented. Learners can explain where full
automation is and isn't appropriate.

**Reflection Questions:**

1. Which step did you keep human-in-the-loop, and why?
2. How does automation change response time and consistency?
3. What is the risk of over-automating response?

---

## Assessment

### Formative Assessment: Pipeline Decision Drill

**Type:** Self-check exercise with answer key

**Description:** Given platform requirements, students make ingestion/storage/
automation decisions and justify the trade-offs. Self-marked.

**Learning Outcomes Assessed:** LO2, LO3

**Feedback mechanism:** Answer key with the recommended decisions and rationale.

---

### Summative Assessment: Detection & Response Platform Design

**Type:** Design report

**Description:** For an assigned Australian organisation, students (a) design a SIEM
architecture and data pipeline, (b) design SOAR automation for a key incident type,
(c) evaluate an XDR/integrated option, and (d) align the platform to ACSC logging and
NDB/SOCI needs. Deliverable: 2,500–3,000 word design with diagrams and a playbook.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| SIEM architecture | LO1, LO2 |
| SOAR automation | LO3 |
| XDR evaluation | LO4 |
| AU alignment & recommendation | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Platform architecture | Coherent, scalable, justified | Sound | Partial | Weak |
| Automation design | Effective, appropriately scoped | Adequate | Over/under-automated | Poor |
| Integration & XDR | Sophisticated evaluation | Reasonable | Superficial | Absent |
| AU alignment | Precise ACSC/NDB/SOCI alignment | Mostly | Superficial | Absent |
| Communication | Clear, well-diagrammed | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC event-logging guidance:** The reference for the platform's logging design.
- **NDB scheme & SOCI Act:** Retention and reporting needs the platform must support.
- **SOC-CMM:** The platform enables operational SOC maturity (see
  `docs/maturity-models.md`).

---

## Further Reading

**Australian Cyber Security Centre (2024).** *Best Practices for Event Logging and Threat Detection.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian logging guidance the platform must satisfy (Australian source).

**OpenSearch / Elastic (2024).** *Architecture & scaling documentation.* https://opensearch.org/docs/
> Relevance: Reference for SIEM/data-platform architecture and scaling (Topic 2).

**Shuffle / n8n (2024).** *Open-source SOAR/automation documentation.* https://shuffler.io / https://n8n.io
> Relevance: The free SOAR platforms used in Lab 2.

**Gartner / vendor-neutral XDR analyses (2024).** *XDR architecture concepts.* (Freely available summaries.)
> Relevance: Concepts for the XDR/integrated-architecture evaluation in Topic 5.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Sensor Mappings to ATT&CK.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: Linking platform data sources to detection coverage (Topic 3; see `docs/maturity-models.md`).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SE04 |
| Unit Title | Detection & Response Engineering |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Security Engineering |
| Prerequisites | SE02, OC02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Privacy Act 1988 (NDB); Security of Critical Infrastructure Act 2018 (contextual) |
