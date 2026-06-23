# CT03: Technical Intelligence

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches the production of technical and operational intelligence: working
with indicators of compromise (IOCs), analysing adversary infrastructure, and
pivoting across data sources to expand and connect findings. Students enrich
indicators with free OSINT services, trace command-and-control infrastructure from
one artefact to related domains and certificates, and turn raw technical data into
intelligence that a SOC or detection team can act on — always weighing indicator
durability (the Pyramid of Pain).

Technical intelligence is the most immediately actionable CTI output: it feeds
detections, hunts, and blocking decisions. In the Australian context, indicators
flow through ACSC advisories and community sharing; analysts both consume and
contribute. CT03 builds on CT01–CT02, OC03 (Malware Analysis), and F06 (Data &
Log Analysis), and feeds CT05 (sharing) and CT06.

---

## Prerequisites

- CT02 — Threat Actor Research & Profiling
- OC03 — Malware Analysis Fundamentals

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** indicators of compromise and assess their durability and value.
2. **Apply** OSINT enrichment to expand context around indicators.
3. **Analyse** adversary infrastructure and pivot to related artefacts.
4. **Evaluate** the reliability and relevance of technical sources.
5. **Synthesise** technical findings into actionable intelligence for SOC/detection
   consumers.
6. **Recommend** indicators and detections derived from technical analysis.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of IOC analysis,
infrastructure pivoting, and technical-intelligence production.

**Skills (AQF 7.2):** Students develop analytical skills by enriching and pivoting on
indicators and synthesising findings.

**Application (AQF 7.3):** Students apply technical intelligence to realistic data
and produce actionable outputs for operational consumers.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | All-Source Analyst (611) | AN-ASA-001 | T0751 | Analyse and enrich technical indicators to produce intelligence | Lab 1 — IOC Enrichment |
| NIST NICE DCWF | 2023 | Threat/Warning Analyst (621) | AN-TWA-001 | T0708 | Analyse infrastructure and pivot to related adversary artefacts | Lab 2 — Infrastructure Pivoting |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Threat Intelligence | Technical Analysis | Practitioner–Advanced | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CT03-K01 | Knowledge of indicators of compromise and their value | Topic 1 |
| Knowledge | CT03-K02 | Knowledge of OSINT enrichment | Topic 2 |
| Knowledge | CT03-K03 | Knowledge of infrastructure analysis and pivoting | Topic 3 |
| Knowledge | CT03-K04 | Knowledge of malware-derived intelligence and source reliability | Topic 4; Topic 5 |
| Skill | CT03-S01 | Skill in enriching IOCs | Lab 1 |
| Skill | CT03-S02 | Skill in pivoting across adversary infrastructure | Lab 2 |
| Ability | CT03-A01 | Ability to produce actionable technical intelligence | Topic 6; Summative |
| Ability | CT03-A02 | Ability to assess the reliability of technical sources | Topic 5; Lab 1 |
| Task | T0751 | Analyse and enrich technical indicators to produce intelligence | Lab 1 |
| Task | T0708 | Analyse infrastructure and pivot to related adversary artefacts | Lab 2 |

---

## Topics

### Topic 1: Indicators of Compromise and Their Value

This topic covers IOC types (hashes, IPs, domains, URLs, mutexes, certificates) and
critically assesses their value and durability using the Pyramid of Pain — why
behaviour and infrastructure patterns outlast atomic indicators.

**Key concepts:**
- IOC types and lifecycle
- Durability and the Pyramid of Pain
- IOC value vs volume

---

### Topic 2: OSINT Enrichment

This topic teaches enriching indicators with free OSINT: reputation and detection
context (VirusTotal free), exposure data (Shodan free), passive DNS, and WHOIS —
and the OPSEC of doing so without tipping off the adversary.

**Key concepts:**
- Enrichment services (VirusTotal, Shodan, passive DNS, WHOIS)
- Building context around an indicator
- Enrichment OPSEC

---

### Topic 3: Infrastructure Analysis and Pivoting

Adversary infrastructure has structure. This topic teaches pivoting: from an IP to
hosted domains, from a certificate to related hosts, from a registrant pattern to
a cluster — expanding a single indicator into an infrastructure picture.

**Key concepts:**
- Pivoting across IPs, domains, certificates, registrants
- Clustering related infrastructure
- Maltego-style link analysis

---

### Topic 4: Malware-Derived Intelligence

This topic connects to OC03: extracting intelligence from malware analysis (C2
configs, capabilities, family classification) and turning it into IOCs and
ATT&CK-mapped behaviours for technical consumers.

**Key concepts:**
- C2 configs and capability extraction
- Family classification and YARA
- Behaviour → ATT&CK mapping

---

### Topic 5: Source Reliability for Technical Intelligence

Technical sources vary in trustworthiness. This topic teaches evaluating feeds and
OSINT for reliability, false-positive risk, and relevance, and avoiding the
over-blocking and alert-fatigue that low-quality indicators cause.

**Key concepts:**
- Feed/source reliability and false positives
- Relevance filtering
- Avoiding over-blocking

---

### Topic 6: Producing Actionable Technical Intelligence

This topic teaches synthesising technical findings into outputs a SOC/detection team
can use immediately — prioritised, durable indicators and detection logic — with
clear provenance and confidence, ready for CT05 sharing.

**Key concepts:**
- From findings to prioritised, durable indicators
- Detection logic from technical intelligence
- Provenance and confidence

**Australian context:** Outputs are framed for contribution to ACSC/community
sharing (developed in CT05).

---

## Labs & Exercises

### Lab 1: IOC Enrichment

**Objective:** Enrich a set of indicators with free OSINT and assess their value.

**Prerequisites:**
- Topics 1, 2, and 5

**Environment:**
- Operating System: any (with internet for OSINT lookups)
- Tools: VirusTotal (free), Shodan (free), passive DNS/WHOIS lookups, a worksheet —
  all free-tier
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take the provided IOC set (hashes, IPs, domains).
2. Enrich each with VirusTotal (detections/relations), Shodan (exposure), and
   passive DNS/WHOIS.
3. Assess each indicator's durability (Pyramid of Pain) and false-positive risk.
4. Note the OPSEC of your lookups (what could tip off an adversary).
5. Prioritise the indicators by value for defensive use.
6. Record provenance and confidence for each.

**Expected Output:**

An enriched, prioritised IOC table with durability, false-positive risk, provenance,
and confidence. Learners can explain why some indicators are worth acting on and
others are not.

**Reflection Questions:**

1. Which indicator was most durable, and which would the adversary change easiest?
2. What OSINT lookup risked tipping off the adversary, and how would you mitigate
   it?
3. Which indicators would you actually deploy, and as what (block/alert/hunt)?

---

### Lab 2: Infrastructure Pivoting

**Objective:** Pivot from a known indicator to related adversary infrastructure.

**Prerequisites:**
- Topics 3–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: Maltego Community Edition, passive DNS, certificate/WHOIS lookups (free-
  tier) — all free
- Minimum hardware: 4 GB RAM / 2 vCPU / 15 GB disk (within spec; no GPU)

**Instructions:**

1. Start from a known malicious IP or domain.
2. Pivot to hosted domains, shared certificates, and registrant patterns.
3. Build a link graph (Maltego CE) of the related infrastructure.
4. Cluster the infrastructure and assess whether it forms a coherent set.
5. State confidence and the limits of the pivot (e.g. shared hosting noise).
6. Produce the resulting indicators and an ATT&CK (v19) mapping where relevant.

**Expected Output:**

An infrastructure link graph, a clustered set with confidence and caveats, and the
resulting indicators. Learners can distinguish genuine adversary infrastructure from
shared-hosting noise.

**Reflection Questions:**

1. Which pivot was most productive, and which produced noise?
2. How confident are you that the cluster is one actor's infrastructure?
3. How would you hand these indicators to detection (CT05/OC02)?

---

## Assessment

### Formative Assessment: Indicator Value Drill

**Type:** Self-check exercise with answer key

**Description:** Given enriched indicators, students rate durability, false-positive
risk, and deployment recommendation. Self-marked.

**Learning Outcomes Assessed:** LO1, LO4

**Feedback mechanism:** Answer key with the value assessment per indicator.

---

### Summative Assessment: Technical Intelligence Report

**Type:** Practical report

**Description:** Given an indicator set and scenario, students (a) enrich and assess
the indicators, (b) pivot to related infrastructure, (c) evaluate source reliability,
and (d) produce actionable technical intelligence (prioritised indicators +
detection logic) with provenance and confidence, ready for sharing. Deliverable:
2,000–2,500 word report with a link graph.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| IOC enrichment & value | LO1, LO2 |
| Infrastructure pivoting | LO3 |
| Source reliability | LO4 |
| Actionable output | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| IOC analysis | Insightful durability/value assessment | Sound | Partial | Weak |
| Pivoting | Productive, well-reasoned, caveated | Adequate | Noisy/partial | Poor |
| Source evaluation | Rigorous reliability/relevance filtering | Reasonable | Superficial | Absent |
| Actionability | Prioritised, deployable, provenance-clear | Adequate | Generic | Not actionable |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories & indicator sharing:** Both a source of indicators and the
  destination for contributed technical intelligence.
- **Community sharing (MISP/TISN context):** Framed as where technical intelligence
  strengthens collective Australian defence (developed in CT05).
- **Cybercrime Act 2001 / OPSEC:** Enrichment and pivoting respect legal and OPSEC
  boundaries from F05/CT01.

---

## Further Reading

**Bianco, D. (2013).** *The Pyramid of Pain.* https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html
> Relevance: The durability framework central to assessing IOC value (Topic 1).

**VirusTotal & Shodan (2024).** *Documentation (free tiers).* https://docs.virustotal.com / https://help.shodan.io
> Relevance: The free enrichment services used in Lab 1.

**Maltego (2024).** *Maltego Community Edition documentation.* https://docs.maltego.com
> Relevance: The free link-analysis tool used for pivoting in Lab 2.

**Australian Cyber Security Centre (2024).** *Threat advisories & indicators.* ACSC. https://www.cyber.gov.au
> Relevance: Australian indicator sources and the sharing destination (Australian source).

**Roberts, S. & Brown, R. (2017).** *Intelligence-Driven Incident Response.* O'Reilly.
> Relevance: Connects technical intelligence to detection and response workflows.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CT03 |
| Unit Title | Technical Intelligence |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | CTI |
| Prerequisites | CT02, OC03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Cybercrime Act 2001 (contextual) |
