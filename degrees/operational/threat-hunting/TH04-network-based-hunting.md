# TH04: Network-Based Hunting

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches hunting in network telemetry — where command-and-control,
exfiltration, and lateral movement are visible even when endpoint evidence is
missing or wiped. Students learn to hunt with Zeek logs and Wireshark/PCAP: finding
C2 beaconing, anomalous DNS (tunnelling and exfiltration), suspicious TLS, and
lateral-movement patterns. The emphasis is on behavioural and statistical
techniques that survive the adversary changing infrastructure.

Network hunting extends the threat-informed-defense spine to the wire: hunts target
ATT&CK (v19) techniques such as application-layer C2 (T1071), DNS (T1071.004),
exfiltration over C2/alternative protocols (T1041/T1048), and ingress tool transfer
(T1105), and findings become network detections. In the Australian context,
network hunting supports detecting the C2 and exfiltration behaviours reported in
ACSC advisories and underpins SOCI detection obligations. TH04 builds on F01
(Networking), F06 (Data & Log Analysis), and TH02.

---

## Prerequisites

- TH02 — ATT&CK for Hunters
- F01 — Networking Fundamentals
- F06 — Data & Log Analysis

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** network telemetry (Zeek logs, PCAP) to identify anomalous
   communication patterns.
2. **Apply** beaconing-detection techniques to identify command-and-control
   activity.
3. **Analyse** DNS telemetry to detect tunnelling and exfiltration.
4. **Evaluate** TLS and HTTP metadata to surface suspicious sessions despite
   encryption.
5. **Apply** statistical and frequency analysis to separate malicious traffic from
   benign noise.
6. **Recommend** network detections derived from hunt findings, mapped to ATT&CK.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of network
telemetry analysis for hunting C2, exfiltration, and lateral movement.

**Skills (AQF 7.2):** Students develop analytical skills by interpreting flows,
DNS, and TLS metadata and applying statistical techniques.

**Application (AQF 7.3):** Students apply network hunting to realistic datasets and
convert findings into network detections.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0023 | Characterize and analyze network traffic to identify anomalous activity | Lab 1 — Beaconing Hunt in Zeek/PCAP |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0294 | Conduct correlation across data sets to detect exfiltration | Lab 2 — DNS Exfiltration Hunt |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Network support | NTAS | Level 4 | Lab 1 |

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
| Knowledge | TH04-K01 | Knowledge of network telemetry sources for hunting | Topic 1 |
| Knowledge | TH04-K02 | Knowledge of command-and-control beaconing behaviour | Topic 2 |
| Knowledge | TH04-K03 | Knowledge of DNS, TLS, and HTTP metadata hunting | Topic 3; Topic 4 |
| Knowledge | TH04-K04 | Knowledge of statistical and frequency techniques for network hunting | Topic 5 |
| Skill | TH04-S01 | Skill in hunting beaconing in Zeek/PCAP | Lab 1 |
| Skill | TH04-S02 | Skill in hunting DNS tunnelling and exfiltration | Lab 2 |
| Ability | TH04-A01 | Ability to surface low-and-slow C2 from network metadata | Lab 1; Topic 5 |
| Ability | TH04-A02 | Ability to convert network findings into detections | Topic 6; Summative |
| Task | T0023 | Characterize and analyze network traffic to identify anomalous activity | Lab 1 |
| Task | T0294 | Conduct correlation across data sets to detect exfiltration | Lab 2 |

---

## Topics

### Topic 1: Network Telemetry for Hunting

This topic surveys what hunters work with: Zeek logs (conn, dns, http, ssl, files),
NetFlow/IPFIX, and full PCAP — and the fidelity/volume trade-offs. It establishes
how to choose the right data for a given hunt.

**Key concepts:**
- Zeek logs, flow data, and PCAP trade-offs
- Key fields per protocol for hunting
- Sensor placement and visibility

---

### Topic 2: Hunting Command-and-Control Beaconing

C2 often beacons on a regular interval. This topic teaches detecting beaconing
through timing regularity (low jitter), consistent payload sizes, and long-lived or
rare destinations — and recognising jittered/sleeping C2 (T1071, T1571).

**Key concepts:**
- Beaconing signatures: periodicity, jitter, payload size
- Identifying rare/long-lived destinations
- Evasive C2 (jitter, domain fronting concepts)

**Australian context:** C2 patterns from ACSC advisories used as hunt scenarios.

---

### Topic 3: DNS Hunting — Tunnelling and Exfiltration

DNS is a favourite covert channel. This topic teaches hunting DNS abuse:
high-entropy or long subdomains, high query volume to one domain, unusual record
types, and TXT-based tunnelling (T1071.004, T1048).

**Key concepts:**
- DNS tunnelling and exfiltration signatures
- Entropy, length, and volume heuristics
- Distinguishing CDNs/telemetry from abuse

---

### Topic 4: TLS and HTTP Metadata Hunting

Encryption hides payloads, not metadata. This topic teaches hunting on TLS
metadata (SNI, JA3/JA4-style fingerprints, certificate anomalies, self-signed
certs) and HTTP metadata (user-agents, URI patterns) to surface suspicious sessions
without decryption.

**Key concepts:**
- TLS metadata: SNI, fingerprints, cert anomalies
- HTTP metadata: user-agents, URIs
- Hunting despite encryption

---

### Topic 5: Statistical and Frequency Techniques

Volume hides threats; statistics reveal them. This topic applies frequency analysis
("least frequency of occurrence"), aggregation, and baselining to network data to
surface the rare and anomalous — the network counterpart to F06's techniques.

**Key concepts:**
- Frequency/rarity analysis on network data
- Baselining normal communication
- Aggregation and outlier detection

---

### Topic 6: From Network Findings to Detections

This topic converts confirmed network findings into durable detections (Zeek
scripts, Sigma for network/proxy logs) and documents indicators for intelligence —
preferring behavioural analytics over brittle IP/domain blocklists.

**Key concepts:**
- Network finding → detection (Zeek/Sigma)
- Behaviour over blocklists (Pyramid of Pain)
- Indicator documentation and sharing

**Australian context:** Detections target C2/exfiltration behaviours reported by
the ACSC; indicators can feed community sharing.

---

## Labs & Exercises

### Lab 1: Beaconing Hunt in Zeek/PCAP

**Objective:** Hunt for C2 beaconing in network telemetry and confirm the channel.

**Prerequisites:**
- Topics 1, 2, and 5

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Zeek, Wireshark, a provided PCAP containing beaconing — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 25 GB disk (within spec; no GPU)

**Instructions:**

1. Process the provided PCAP with Zeek to generate conn/dns/http/ssl logs.
2. Aggregate connections by source/destination pair; compute connection counts and
   intervals.
3. Identify candidate beaconing: regular intervals, consistent sizes, rare
   destination.
4. Confirm in Wireshark by inspecting the candidate sessions.
5. Determine the likely C2 protocol and map to ATT&CK (v19, e.g. T1071).
6. Record the indicators and the behavioural signature.

**Expected Output:**

A beaconing finding with timing/size evidence, confirmation in Wireshark, the C2
protocol, and an ATT&CK mapping. Learners can explain the behavioural signature
that identified it.

**Reflection Questions:**

1. How would jitter or a longer sleep interval have affected your detection?
2. Why is the behavioural signature more durable than the destination IP?
3. How would you express this as a Zeek/Sigma detection?

---

### Lab 2: DNS Exfiltration Hunt

**Objective:** Hunt for DNS-based exfiltration/tunnelling in DNS log data.

**Prerequisites:**
- Topics 3 and 5 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Zeek dns logs or a free log platform (OpenSearch), Python/Pandas optional —
  all free/OSS
- Minimum hardware: as Lab 1

**Instructions:**

1. Load the provided DNS log dataset.
2. Aggregate queries per domain; identify domains with abnormally high query volume.
3. Compute subdomain length/entropy and flag high-entropy, long subdomains.
4. Examine record types for unusual TXT/NULL usage.
5. Confirm the exfiltration channel and estimate the data direction/volume.
6. Map to ATT&CK (v19) and record indicators.

**Expected Output:**

A DNS exfiltration finding supported by volume/entropy evidence, the identified
channel, and an ATT&CK mapping. Learners can distinguish the abuse from benign
high-volume DNS (e.g. CDNs).

**Reflection Questions:**

1. Which heuristic (volume, entropy, record type) was most decisive, and why?
2. How would you avoid false positives from legitimate high-volume domains?
3. What detection would you deploy, and where would it run?

---

## Assessment

### Formative Assessment: Traffic Anomaly Spotting

**Type:** Self-check exercise with answer key

**Description:** Given summarised flow/DNS/TLS records, students identify which are
anomalous and name the likely technique. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with the anomaly and technique for each record
set.

---

### Summative Assessment: Network Hunt Report

**Type:** Practical report

**Description:** Given a network dataset (Zeek logs + PCAP) containing C2 and
exfiltration, students (a) hunt for beaconing, (b) hunt for DNS/exfiltration, (c)
use TLS/HTTP metadata and frequency analysis to confirm, and (d) recommend at least
two network detections mapped to ATT&CK. Deliverable: 2,500–3,000 word report with
evidence and detections.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Beaconing hunt | LO1, LO2 |
| DNS/exfiltration hunt | LO3 |
| TLS/HTTP + statistical confirmation | LO4, LO5 |
| Detections | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Network analysis | Thorough, accurate, well-evidenced | Solid with minor gaps | Partial | Inaccurate |
| Technique use | Apt statistical/metadata techniques | Adequate techniques | Basic | Poor |
| Verdict & mapping | Correct, ATT&CK-mapped findings | Mostly correct | Inconsistent | Incorrect |
| Detections | Robust, behaviour-based | Workable | Brittle | Missing |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories:** Provide real C2 and exfiltration TTPs as hunt scenarios.
- **SOCI Act 2018:** Network detection capability framed as support for
  critical-infrastructure obligations.
- **ASD Essential Eight & ISM:** Egress control and monitoring expectations inform
  hunt and detection recommendations.

---

## Further Reading

**The Zeek Project (2024).** *Zeek Documentation.* https://docs.zeek.org
> Relevance: The free network-analysis platform and log reference used in both labs.

**Bejtlich, R. (2013).** *The Practice of Network Security Monitoring.* No Starch Press.
> Relevance: Foundational network-monitoring and hunting practice underpinning this unit.

**MITRE ATT&CK (v19, 2026).** *Command and Control / Exfiltration techniques.* https://attack.mitre.org
> Relevance: The technique reference for the network behaviours hunted here.

**Australian Cyber Security Centre (2024).** *Threat advisories & event-logging guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian C2/exfiltration TTPs and logging expectations (Australian source).

**Active Countermeasures (2024).** *RITA / beacon-analysis methodology.* https://www.activecountermeasures.com
> Relevance: A free, practical reference for the beaconing-analysis techniques in Lab 1.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | TH04 |
| Unit Title | Network-Based Hunting |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Threat Hunting |
| Prerequisites | TH02, F01, F06 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
