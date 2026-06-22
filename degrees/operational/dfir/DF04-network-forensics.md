# DF04: Network Forensics

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches forensic analysis of network evidence: reconstructing what
crossed the wire from packet captures and flow/Zeek logs to establish
command-and-control, lateral movement, and data exfiltration. Students analyse
PCAP in Wireshark and Zeek, identify C2 beaconing and DNS-based exfiltration,
reconstruct sessions and transferred files, and handle network evidence so it
remains admissible. The forensic framing — integrity, completeness, and
admissibility — distinguishes this from the proactive hunting view.

Network evidence is often the only record of exfiltration — critical for the NDB
"what data left" question — and persists even when an adversary wipes endpoints. In
the Australian context, the integrity practices align with the *Evidence Act 1995*,
and exfiltration findings drive NDB and (for critical infrastructure) SOCI
reporting. DF04 builds on DF01, F01 (Networking), and F06 (Data & Log Analysis),
and feeds DF05 and the capstone DF06.

---

## Prerequisites

- DF01 — DFIR Process & Legal Foundations
- F01 — Networking Fundamentals
- F06 — Data & Log Analysis

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** sound handling and integrity practices to network evidence (PCAP,
   logs).
2. **Analyse** packet captures to reconstruct sessions and transferred content.
3. **Analyse** traffic to identify command-and-control, including beaconing.
4. **Analyse** DNS and protocol data to identify data exfiltration.
5. **Evaluate** network evidence to determine the scope of data movement.
6. **Recommend** defensible findings and network IOCs.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of network
forensics, C2, and exfiltration analysis.

**Skills (AQF 7.2):** Students develop analytical skills by reconstructing sessions
and identifying malicious traffic.

**Application (AQF 7.3):** Students apply network forensics to realistic captures
and produce defensible, admissibility-aware findings.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0432 | Perform network forensic analysis to determine adversary activity | Lab 1 — C2 Reconstruction from PCAP |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0294 | Correlate network data to identify exfiltration and scope | Lab 2 — DNS Exfiltration Analysis |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Systems & software life cycle / assurance | SURE | Level 4–5 | Lab 1, Lab 2 |
| Network support | NTAS | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Incident Management | Digital Forensics | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Network Evidence and Integrity

This topic covers the sources of network evidence (full PCAP, Zeek logs, NetFlow,
proxy/firewall logs), their completeness and retention limits, and handling them
soundly (hashing captures, documenting collection) for admissibility.

**Key concepts:**
- PCAP vs flow vs log evidence and their limits
- Capture integrity and documentation
- Retention as a forensic constraint

---

### Topic 2: Session Reconstruction

This topic teaches reconstructing conversations from PCAP: following TCP/HTTP
streams, reassembling transferred files (carving objects), and establishing who
communicated with whom, when, and what was exchanged.

**Key concepts:**
- Following streams and reassembly
- File/object carving from captures
- Establishing the communication record

---

### Topic 3: Identifying Command-and-Control

This topic teaches recognising C2 forensically: beaconing (periodicity, jitter,
payload regularity), suspicious TLS/HTTP metadata, and rare/long-lived
destinations — establishing the channel and its timeframe (ATT&CK T1071).

**Key concepts:**
- Beaconing signatures and evasive C2
- TLS/HTTP metadata indicators
- Establishing the C2 channel and timeline

---

### Topic 4: Detecting Data Exfiltration

This topic covers identifying exfiltration: large or unusual outbound transfers,
DNS tunnelling (high-entropy/long subdomains, TXT abuse), exfiltration over C2 or
alternative protocols (T1041/T1048), and estimating volume and direction.

**Key concepts:**
- Exfiltration over C2 and alternative channels
- DNS tunnelling/exfiltration signatures
- Estimating exfiltrated volume and direction

**Australian context:** Exfiltration findings drive the NDB "what data left"
determination.

---

### Topic 5: Scoping Data Movement

This topic teaches determining the scope of what moved: correlating network
evidence with host findings (DF02/DF03), distinguishing access from exfiltration,
and producing a defensible estimate of affected data for impact assessment.

**Key concepts:**
- Correlating network with host evidence
- Access vs exfiltration
- Defensible data-impact estimates

---

### Topic 6: Network IOCs and Defensible Findings

This topic teaches extracting durable network indicators, stating confidence and
limits (e.g. encrypted payloads), and documenting method for repeatability and
admissibility (linking to DF01).

**Key concepts:**
- Extracting and prioritising network IOCs
- Stating confidence and analytical limits
- Repeatable, admissibility-aware documentation

**Australian context:** Findings meet the Evidence Act 1995 standard and feed
NDB/SOCI reporting.

---

## Labs & Exercises

### Lab 1: C2 Reconstruction from PCAP

**Objective:** Reconstruct a command-and-control channel from a packet capture and
establish its timeline.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Wireshark, Zeek, a provided PCAP with C2 — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 30 GB disk (within the 8 GB / 4-core /
  50 GB spec; no GPU)

**Instructions:**

1. Record the capture's hash and document its (simulated) collection.
2. Process the PCAP with Zeek; review conn/http/ssl logs.
3. Identify candidate C2 by beaconing characteristics; confirm in Wireshark.
4. Follow the relevant streams; reconstruct what is visible of the channel.
5. Establish the C2 timeframe and map to ATT&CK (v19, T1071).
6. Record network IOCs and the supporting evidence.

**Expected Output:**

A confirmed C2 channel with timing evidence, reconstructed session detail, a
timeframe, ATT&CK mapping, and IOCs. Learners can state what remains hidden behind
encryption and their confidence.

**Reflection Questions:**

1. What could you establish despite encryption, and what could you not?
2. How does the capture's integrity affect the admissibility of these findings?
3. How would you corroborate this C2 with host evidence (DF02/DF03)?

---

### Lab 2: DNS Exfiltration Analysis

**Objective:** Identify DNS-based exfiltration and estimate the scope of data
movement.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Zeek dns logs / a free log platform, Wireshark, Python/Pandas optional —
  all free/OSS
- Minimum hardware: as Lab 1

**Instructions:**

1. Load the provided DNS dataset/PCAP.
2. Identify domains with abnormal query volume and high-entropy/long subdomains.
3. Confirm DNS tunnelling/exfiltration and identify the channel (T1048/T1071.004).
4. Estimate the direction and approximate volume of data moved.
5. Correlate with host evidence to determine what data was likely affected.
6. Produce findings, IOCs, and an NDB-relevant data-impact note.

**Expected Output:**

A confirmed DNS exfiltration finding with volume/entropy evidence, a scope
estimate, correlation to host evidence, and an NDB impact note. Learners can
distinguish abuse from benign high-volume DNS.

**Reflection Questions:**

1. Which evidence most reliably proved exfiltration vs mere querying?
2. How precise is your volume estimate, and what is your confidence?
3. How does this finding drive the NDB notification decision?

---

## Assessment

### Formative Assessment: Traffic Evidence Drill

**Type:** Self-check exercise with answer key

**Description:** Given summarised captures/logs, students identify C2 vs
exfiltration vs benign and state the supporting evidence. Self-marked.

**Learning Outcomes Assessed:** LO3, LO4

**Feedback mechanism:** Answer key with the classification and evidence per item.

---

### Summative Assessment: Network Forensic Report

**Type:** Practical report

**Description:** Given network evidence (PCAP + Zeek logs) containing C2 and
exfiltration, students (a) handle evidence soundly, (b) reconstruct C2, (c) identify
and scope exfiltration, and (d) produce a defensible report with findings, IOCs,
ATT&CK mappings, confidence, and an NDB data-impact assessment. Deliverable:
2,500–3,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Evidence handling | LO1 |
| Session/C2 reconstruction | LO2, LO3 |
| Exfiltration & scoping | LO4, LO5 |
| Defensible findings & IOCs | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Evidence handling | Sound integrity & documentation | Adequate | Gaps | Unsound |
| Traffic analysis | Thorough, accurate, well-evidenced | Solid | Partial | Inaccurate |
| Exfiltration scoping | Defensible scope & impact estimate | Adequate | Weak | Poor |
| Defensible findings | Confidence/limits clear; admissibility-aware | Mostly clear | Inconsistent | Poor |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Evidence Act 1995 (Cth):** Network evidence handled and findings written to the
  admissibility standard.
- **NDB scheme:** Exfiltration findings drive the "what data left" determination.
- **SOCI Act 2018:** Exfiltration scope informs critical-infrastructure reporting.

---

## Further Reading

**Davidoff, S. & Ham, J. (2012).** *Network Forensics: Tracking Hackers through Cyberspace.* Prentice Hall.
> Relevance: The standard network-forensics reference underpinning this unit.

**The Zeek Project (2024).** *Zeek Documentation.* https://docs.zeek.org
> Relevance: The free network-analysis platform used in both labs.

**Wireshark Foundation (2024).** *Wireshark User Guide.* https://www.wireshark.org/docs/
> Relevance: The free packet-analysis tool used for session/C2 reconstruction.

**Office of the Australian Information Commissioner (2024).** *Data breach assessment guidance.* OAIC. https://www.oaic.gov.au
> Relevance: Connects exfiltration findings to NDB impact assessment (Australian source).

**MITRE ATT&CK (v19, 2026).** *Command and Control / Exfiltration techniques.* https://attack.mitre.org
> Relevance: The technique reference for the C2 and exfiltration behaviours analysed here.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DF04 |
| Unit Title | Network Forensics |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | DFIR |
| Prerequisites | DF01, F01, F06 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Evidence Act 1995 (Cth); Privacy Act 1988 (NDB); Security of Critical Infrastructure Act 2018 |
