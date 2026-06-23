# CT05: CTI Platforms & Sharing

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches the platforms and standards that operationalise CTI at scale:
**MISP** and **OpenCTI** for managing and correlating intelligence, and **STIX 2.1
/ TAXII 2.1** for representing and exchanging it in a structured, machine-readable
way. Students model intelligence as STIX objects, build and query a CTI platform,
ingest and share feeds, and apply the **MITRE CTID** body of work to enrich and
standardise their intelligence. The unit turns the analytic outputs of CT01–CT04
into shareable, automatable assets.

Sharing is a force multiplier: intelligence that stays in one team is worth a
fraction of intelligence that flows through a community. In the Australian context,
sharing operates through ACSC partnerships and the Trusted Information Sharing
Network (TISN) for critical infrastructure. CT05 builds on CT03 (technical
intelligence) and OC05, and directly enables the CT06 capstone's dissemination
requirement.

---

## Prerequisites

- CT03 — Technical Intelligence
- F03 — Scripting & Automation

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** STIX 2.1 to represent threat actors, malware, and relationships.
2. **Analyse** the role of TAXII 2.1 in exchanging structured intelligence.
3. **Apply** a CTI platform (MISP/OpenCTI) to manage, correlate, and query
   intelligence.
4. **Evaluate** the trust, quality, and handling considerations of intelligence
   sharing.
5. **Apply** MITRE CTID resources to enrich and standardise intelligence.
6. **Recommend** a sharing approach appropriate to an Australian organisation and
   community.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of CTI platforms,
structured-intelligence standards, and sharing models.

**Skills (AQF 7.2):** Students develop technical skills by modelling STIX, operating
platforms, and managing feeds.

**Application (AQF 7.3):** Students apply platforms and standards to operationalise
and share intelligence in an Australian community context.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | All-Source Analyst (611) | AN-ASA-001 | T0751 | Represent and exchange structured intelligence | Lab 1 — STIX 2.1 Objects |
| NIST NICE DCWF | 2023 | Threat/Warning Analyst (621) | AN-TWA-001 | T0708 | Manage and correlate intelligence in a platform | Lab 2 — MISP/OpenCTI Workflow |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Programming / software development | PROG | Level 3–4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Threat Intelligence | Intelligence Sharing | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CT05-K01 | Knowledge of structured intelligence with STIX 2.1 | Topic 1 |
| Knowledge | CT05-K02 | Knowledge of exchanging intelligence with TAXII 2.1 | Topic 2 |
| Knowledge | CT05-K03 | Knowledge of CTI platforms (MISP, OpenCTI) and handling/trust models | Topic 3; Topic 4 |
| Knowledge | CT05-K04 | Knowledge of MITRE CTID for standardisation and enrichment | Topic 5 |
| Skill | CT05-S01 | Skill in modelling intelligence as STIX 2.1 objects | Lab 1 |
| Skill | CT05-S02 | Skill in operating a MISP/OpenCTI workflow | Lab 2 |
| Ability | CT05-A01 | Ability to design an intelligence-sharing approach | Topic 6; Summative |
| Ability | CT05-A02 | Ability to apply handling and quality controls to shared intelligence | Topic 4; Lab 2 |
| Task | T0751 | Represent and exchange structured intelligence | Lab 1 |
| Task | T0708 | Manage and correlate intelligence in a platform | Lab 2 |

---

## Topics

### Topic 1: Structured Intelligence with STIX 2.1

STIX 2.1 is the standard for representing intelligence as objects and relationships.
This topic covers the core STIX Domain Objects (threat-actor, malware, indicator,
attack-pattern, etc.), relationships, and why structure enables automation.

**Key concepts:**
- STIX Domain Objects and relationships
- Indicators, patterns, and observed-data
- Why structure enables automation

---

### Topic 2: Exchanging Intelligence with TAXII 2.1

TAXII 2.1 is the transport for STIX. This topic covers TAXII collections and
channels, push/pull exchange, and how organisations subscribe to and contribute
feeds.

**Key concepts:**
- TAXII collections and exchange models
- Subscribing to and serving feeds
- STIX-over-TAXII in practice

---

### Topic 3: CTI Platforms — MISP and OpenCTI

This topic teaches the two leading open platforms: MISP (event/attribute sharing,
correlation, communities) and OpenCTI (knowledge-graph model, connectors). It
covers ingesting, correlating, and querying intelligence and building useful views.

**Key concepts:**
- MISP events/attributes and communities
- OpenCTI knowledge graph and connectors
- Ingestion, correlation, and querying

---

### Topic 4: Trust, Quality, and Handling

Sharing requires trust and discipline. This topic covers the Traffic Light Protocol
(TLP) and handling caveats, feed quality and false-positive management, deduplication,
and the trust models of sharing communities.

**Key concepts:**
- TLP and handling caveats
- Feed quality and deduplication
- Community trust models

**Australian context:** Sharing through ACSC partnerships and TISN for critical
infrastructure, with appropriate handling.

---

### Topic 5: MITRE CTID for Standardisation and Enrichment

This topic applies the CTID body of work: mapping intelligence to ATT&CK (v19),
using Attack Flow to represent sequences, and leveraging Mappings Explorer to
relate ATT&CK to controls/sensors — standardising intelligence for consumption.

**Key concepts:**
- ATT&CK-mapping intelligence (CTID)
- Attack Flow for sequence representation
- Mappings Explorer for control/sensor context

---

### Topic 6: Designing a Sharing Approach

This topic teaches designing how an organisation shares: what to share with whom,
at what TLP, through which platform/community, and how to balance contribution
against OPSEC and sensitivity — turning the organisation into a good community
citizen.

**Key concepts:**
- What/with-whom/how-to-share decisions
- Balancing contribution against OPSEC/sensitivity
- Being a good sharing-community citizen

**Australian context:** Designing sharing for ACSC/TISN participation.

---

## Labs & Exercises

### Lab 1: STIX 2.1 Objects

**Objective:** Programmatically create STIX 2.1 objects representing a threat actor,
malware, and their relationship.

**Prerequisites:**
- Topics 1–2 and F03

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Python 3 + the `stix2` library — all free/OSS
- Minimum hardware: 2 GB RAM / 2 vCPU / 10 GB disk (within the 8 GB / 4-core /
  50 GB spec; no GPU)

**Instructions:**

1. Set up a Python environment with the `stix2` library.
2. Create a `threat-actor` STIX object and a `malware` object with required
   properties.
3. Create an `indicator` with a STIX pattern and an `attack-pattern` referencing an
   ATT&CK (v19) technique.
4. Create `relationship` objects linking them (e.g. actor *uses* malware).
5. Bundle the objects and validate the output against the STIX 2.1 schema.
6. Add TLP marking to the objects.

**Expected Output:**

A schema-valid STIX 2.1 bundle with actor, malware, indicator, attack-pattern,
relationships, and TLP markings. Learners can explain each object and relationship.

**Reflection Questions:**

1. How does the relationship model make this intelligence machine-actionable?
2. Why does the TLP marking matter when this bundle is shared?
3. How would a consumer ingest this via TAXII?

---

### Lab 2: MISP/OpenCTI Workflow

**Objective:** Ingest a feed into a CTI platform and produce a useful view for a
specific threat.

**Prerequisites:**
- Topics 3–6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: MISP and/or OpenCTI (free/OSS), a sample feed — run single-node
- Minimum hardware: 8 GB RAM / 4 vCPU / 40 GB disk (at the spec ceiling; run one
  platform at a time; no GPU)

**Instructions:**

1. Stand up MISP or OpenCTI single-node (or use the provided instance).
2. Ingest a sample feed (or the STIX bundle from Lab 1).
3. Correlate the new intelligence with existing data and review the relationships.
4. Build a view/dashboard focused on a specific threat actor or campaign.
5. Apply TLP/handling and identify what you would and would not share onward.
6. Map the actor's techniques to ATT&CK (v19) within the platform.

**Expected Output:**

A populated platform with correlated intelligence, a threat-focused view/dashboard,
applied TLP handling, and an ATT&CK mapping. Learners can explain the correlation
and their sharing decisions.

**Reflection Questions:**

1. What did correlation reveal that the raw feed did not?
2. Which items would you not share onward, and why?
3. How would this platform support the CT06 capstone's dissemination?

---

## Assessment

### Formative Assessment: STIX & TLP Drill

**Type:** Self-check exercise with answer key

**Description:** Given intelligence snippets, students choose the correct STIX object
types/relationships and the appropriate TLP. Self-marked.

**Learning Outcomes Assessed:** LO1, LO4

**Feedback mechanism:** Answer key with the correct STIX modelling and TLP.

---

### Summative Assessment: Platform & Sharing Package

**Type:** Practical project with report

**Description:** Students (a) model a threat as a valid STIX 2.1 bundle, (b) ingest
and correlate it in MISP/OpenCTI with a threat-focused view, (c) apply CTID ATT&CK
mapping, and (d) produce a sharing design (what/with-whom/TLP/platform) appropriate
to an Australian community. Deliverable: STIX bundle + platform export + a
1,500–2,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| STIX modelling | LO1, LO2 |
| Platform workflow | LO3 |
| CTID enrichment | LO5 |
| Sharing design | LO4, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| STIX modelling | Schema-valid, well-structured, relationship-rich | Valid with minor gaps | Partial | Invalid |
| Platform use | Skilled correlation and views | Solid | Basic | Poor |
| Standardisation (CTID) | Apt ATT&CK mapping/enrichment | Adequate | Superficial | Absent |
| Sharing design | Sound trust/TLP/OPSEC decisions | Reasonable | Generic | Poor |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC partnerships:** A primary Australian sharing relationship.
- **TISN (Trusted Information Sharing Network):** Critical-infrastructure sharing
  context for the sharing-design work.
- **TLP and handling:** Applied so contributions respect sensitivity within
  Australian communities.

---

## Further Reading

**OASIS (2021).** *STIX 2.1 & TAXII 2.1 Specifications.* OASIS. https://oasis-open.github.io/cti-documentation/
> Relevance: The authoritative standards modelled in Topics 1–2 and Lab 1.

**MISP Project (2024).** *MISP Documentation.* https://www.misp-project.org/documentation/
> Relevance: The free sharing platform used in Lab 2.

**OpenCTI / Filigran (2024).** *OpenCTI Documentation.* https://docs.opencti.io
> Relevance: The free knowledge-graph CTI platform used in Lab 2.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Attack Flow, Mappings Explorer.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The CTID resources used to standardise and enrich intelligence (Topic 5).

**Australian Cyber Security Centre (2024).** *Threat sharing & partnership programs.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian sharing ecosystem (ACSC/TISN) the sharing design targets (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CT05 |
| Unit Title | CTI Platforms & Sharing |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | CTI |
| Prerequisites | CT03, F03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (ACSC/TISN sharing context) |
