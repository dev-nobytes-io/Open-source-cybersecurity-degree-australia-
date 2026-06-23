# F01: Networking Fundamentals

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit builds the network literacy every cybersecurity practitioner depends
on. Before a learner can hunt threats, analyse malware traffic, or engineer
detections, they must be able to read a packet, reason about how data moves
between hosts, and explain why a given protocol behaves the way it does. The
unit covers the TCP/IP model, addressing and routing, the protocols that carry
the bulk of enterprise traffic, and the practical skill of capturing and
interpreting that traffic with free tools.

In the Australian context, network competency underpins the technical controls
in the ASD *Essential Eight* and the ACSC *Information Security Manual* (ISM) —
network segmentation, restriction of inbound/outbound traffic, and monitoring
all assume a practitioner who understands the wire. F01 sits at the base of both
the Operational and Strategic degree pathways and is a prerequisite for almost
every later unit, including F06 (Data & Log Analysis), OC02 (Security Monitoring
& SIEM), and the Threat Hunting and DFIR majors.

---

## Prerequisites

- None (entry-level foundation unit)

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Describe** the layers of the TCP/IP and OSI models and explain the role of
   each layer in moving data between hosts.
2. **Explain** how IPv4/IPv6 addressing, subnetting, and routing direct traffic
   across local and wide-area networks.
3. **Identify** common application-layer protocols (DNS, HTTP/HTTPS, DHCP, SMTP)
   and describe their normal behaviour on the wire.
4. **Demonstrate** packet capture and analysis using free tools to inspect live
   and stored network traffic.
5. **Use** command-line utilities to enumerate hosts, services, and routes on a
   permitted lab network.
6. **Explain** the security relevance of network segmentation and traffic
   filtering with reference to the ASD Essential Eight and ACSC ISM.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of
computer networking by covering the TCP/IP and OSI reference models, addressing
and routing, core application protocols, and the principles of network security
controls.

**Skills (AQF 7.2):** Students develop cognitive and technical skills by
analysing captured traffic, interpreting protocol exchanges, and selecting and
operating command-line networking tools to investigate a network.

**Application (AQF 7.3):** Students apply this knowledge in an authorised lab
context that mirrors enterprise network investigation, relating findings to
Australian baseline controls (Essential Eight, ACSC ISM) and explaining the
security implications of observed traffic.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0023 | Characterize and analyze network traffic to identify anomalous activity and potential threats | Lab 1 — Capturing & Reading Live Traffic |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0294 | Conduct research, analysis, and correlation across a wide variety of data sets | Lab 2 — Mapping a Network from the Command Line |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Network support | NTAS | Level 3 | Lab 1, Lab 2 |
| Information security | SCAD | Level 2 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Technical Foundations | Networking | Foundational | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F01-K01 | Knowledge of the TCP/IP and OSI models and how each layer moves data | Topic 1; Topic 3 |
| Knowledge | F01-K02 | Knowledge of IP addressing, subnetting, and routing | Topic 2; Lab 2 |
| Knowledge | F01-K03 | Knowledge of common application protocols (DNS, HTTP/S, DHCP, SMTP) and their normal behaviour | Topic 4; Lab 1 |
| Skill | F01-S01 | Skill in capturing and analysing network traffic with free tools | Lab 1 |
| Skill | F01-S02 | Skill in enumerating hosts, services, and routes from the command line | Lab 2 |
| Ability | F01-A01 | Ability to distinguish normal from anomalous traffic on the wire | Lab 1; Summative |
| Ability | F01-A02 | Ability to relate network segmentation/filtering to ASD Essential Eight controls | Topic 5; Summative |
| Task | T0023 | Characterize and analyze network traffic to identify anomalous activity | Lab 1 |
| Task | T0294 | Conduct research, analysis, and correlation across a variety of data sets | Lab 2 |

---

## Topics

### Topic 1: The TCP/IP and OSI Models

Networks are layered so that each function — physical signalling, addressing,
reliable delivery, application semantics — can be designed and reasoned about
independently. The OSI model defines seven conceptual layers; the TCP/IP model
collapses these into four practical layers (Link, Internet, Transport,
Application) that map to how real systems are built. Understanding the layered
model lets a practitioner locate a problem: a failure to resolve a name is an
application/transport issue, whereas a failure to reach a default gateway is an
Internet/Link issue.

**Key concepts:**
- Encapsulation and decapsulation as data moves down and up the stack
- Mapping OSI layers to TCP/IP layers and to real protocols
- Protocol data units: frames, packets, segments, data

**Australian context:** The ACSC ISM's network controls are written in
layered terms (gateway, network, host); reasoning by layer is how practitioners
translate ISM guidance into configuration.

---

### Topic 2: IP Addressing and Subnetting

Every host on an IP network needs an address and a way to know which other
addresses are "local". This topic covers IPv4 structure, CIDR notation, subnet
masks, private vs public ranges (RFC 1918), and the basics of IPv6. Subnetting
is the skill of dividing an address space into smaller networks — the
foundation of network segmentation, which is itself a security control.

**Key concepts:**
- CIDR notation and calculating network/broadcast/host ranges
- Private address ranges and Network Address Translation (NAT)
- IPv6 addressing basics and why dual-stack environments matter

**Australian context:** Network segmentation is a recurring theme in ACSC
guidance for limiting lateral movement; subnetting is the mechanism behind it.

---

### Topic 3: Routing and Switching

Switches move frames within a network using MAC addresses; routers move packets
between networks using IP addresses and routing tables. This topic explains how
a packet travels from source to destination, the role of the default gateway,
ARP for local resolution, and how routing decisions are made. Learners trace a
path end to end and explain each hop.

**Key concepts:**
- The forwarding decision: local delivery vs routing to a gateway
- ARP and the MAC/IP relationship
- Routing tables and the meaning of a default route

---

### Topic 4: Core Application Protocols

DNS resolves names to addresses; DHCP assigns addresses automatically; HTTP/HTTPS
carries web traffic; SMTP carries mail. Knowing what "normal" looks like for
these protocols is the prerequisite for spotting "abnormal". This topic walks
through a normal exchange for each protocol and highlights the fields a defender
watches (DNS query types, TLS SNI, HTTP host headers).

**Key concepts:**
- The DNS resolution sequence and record types
- The TLS handshake at a high level and what remains visible after encryption
- Why plaintext protocols are a risk and how encrypted equivalents differ

**Australian context:** DNS abuse and phishing infrastructure feature heavily in
ACSC advisories; recognising DNS behaviour is an entry skill for later CTI work.

---

### Topic 5: Network Security Fundamentals

This topic introduces the defensive concepts that the rest of the degree builds
on: firewalls and access control lists, network segmentation and zoning, the
difference between north-south and east-west traffic, and the role of monitoring
points (taps, span ports). It frames these against the ASD Essential Eight and
the principle of restricting both inbound and outbound traffic.

**Key concepts:**
- Stateful vs stateless filtering
- Segmentation, micro-segmentation, and the blast-radius concept
- Where to place sensors so traffic is actually visible

**Australian context:** The Essential Eight and ISM both treat egress filtering
and segmentation as baseline controls; this topic connects the theory to those
requirements.

---

### Topic 6: Reading Traffic — Captures and Flows

Full packet capture (PCAP) gives the richest view but does not scale; flow data
(NetFlow/IPFIX, Zeek logs) scales but summarises. Practitioners must understand
both. This topic introduces capture tools (Wireshark, tcpdump), display and
capture filters, and the idea of session/flow records as the bridge between raw
packets and the log analysis covered in F06.

**Key concepts:**
- PCAP vs flow data trade-offs (fidelity vs volume)
- Display filters vs capture filters
- Following a TCP stream to reconstruct a conversation

---

## Labs & Exercises

### Lab 1: Capturing & Reading Live Traffic

**Objective:** Capture live network traffic and analyse a DNS-then-HTTP exchange
to demonstrate understanding of protocol behaviour across layers.

**Prerequisites:**
- Topics 1, 4, and 6
- A local lab VM with internet access on a network the learner owns/controls

**Environment:**
- Operating System: Ubuntu 22.04 LTS (desktop) in a local VM
- Tools: Wireshark and `tcpdump` (both free/OSS)
- Minimum hardware: 4 GB RAM allocated to the VM, 2 vCPU, 15 GB disk (well
  within the 8 GB / 4-core / 50 GB spec; no GPU required)

**Instructions:**

1. Launch the VM and confirm network connectivity with `ip addr` and
   `ip route` — record the host's IP, subnet mask (CIDR), and default gateway.
2. Start a capture: `sudo tcpdump -i any -w lab1.pcap` and leave it running.
3. In a second terminal, run `dig www.cyber.gov.au` then
   `curl -I https://www.cyber.gov.au`.
4. Stop the capture with `Ctrl+C` and open `lab1.pcap` in Wireshark.
5. Apply the display filter `dns` and locate the query and response for
   `www.cyber.gov.au`. Record the resolved IP address(es) and the record type.
6. Apply the filter `tls.handshake.type == 1` and find the Client Hello; record
   the Server Name Indication (SNI) value.
7. Right-click a packet in the TLS session and choose **Follow → TCP Stream** to
   observe that the application data is encrypted.

**Expected Output:**

A saved `lab1.pcap`; a recorded DNS A-record answer for the target domain; a
recorded SNI value matching the domain; and a short note confirming that, after
the TLS handshake, the HTTP payload is not readable in plaintext. Successful
learners can point to the exact packet for each step.

**Reflection Questions:**

1. Which fields remained visible to a network defender after TLS encryption, and
   why does that matter for monitoring?
2. The ACSC publishes guidance on encrypted DNS. How would DNS-over-HTTPS change
   what you observed in step 5, and what is the defensive trade-off?
3. If you only had flow data (not full PCAP), which of your findings could you
   still recover and which would you lose?

---

### Lab 2: Mapping a Network from the Command Line

**Objective:** Use command-line tools to enumerate hosts, services, and routes
on an authorised lab subnet and produce a simple network map.

**Prerequisites:**
- Topics 2, 3, and 5
- A second VM (or the host) on the same isolated lab network as Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS in a local VM (host-only / internal network)
- Tools: `nmap`, `ip`, `traceroute`, `arp` (all free/OSS)
- Minimum hardware: as Lab 1; the lab network must be **host-only/internal** so
  no scanning leaves the lab

**Instructions:**

1. Confirm you are on an isolated host-only network — verify with `ip addr` that
   the address is in a private range and not your home/work LAN.
2. Identify the local subnet from your IP and CIDR mask.
3. Run a host-discovery sweep: `nmap -sn 10.0.0.0/24` (substitute your subnet).
   Record live hosts.
4. For one discovered host, run a service scan: `nmap -sV <target-ip>` and record
   open ports and identified services.
5. Run `ip route` and `traceroute <target-ip>` and document the path/hops.
6. View the local ARP cache with `ip neigh` and match MAC addresses to IPs.
7. Draw a simple diagram (hand-drawn or in draw.io) showing hosts, addresses,
   open services, and the gateway.

**Expected Output:**

A list of live hosts on the lab subnet, a service inventory for at least one
host, a recorded route, and a network diagram. Learners must state explicitly
that all scanning stayed within the isolated lab.

**Reflection Questions:**

1. Why is unauthorised port scanning a legal and ethical problem in Australia,
   and which legislation is relevant? (Links forward to F05.)
2. How would network segmentation change what host discovery reveals?
3. Which of these enumeration steps would generate detectable artefacts in a
   SIEM, and what would they look like? (Links forward to F06/OC02.)

---

## Assessment

### Formative Assessment: Protocol Behaviour Quiz

**Type:** Self-check quiz with answer key

**Description:** A short quiz covering layer identification, subnet calculations,
and "normal vs abnormal" protocol behaviour. Students self-mark against the
provided key and note any topic to revisit.

**Learning Outcomes Assessed:** LO1, LO2, LO3

**Feedback mechanism:** Self-check answer key with explanations for each item.

---

### Summative Assessment: Network Investigation Report

**Type:** Practical lab report

**Description:** Students are given (or capture) a PCAP and a brief scenario:
"A workstation on an isolated lab subnet is behaving unexpectedly." They must
(a) identify the host's addressing and likely role, (b) characterise the
observed traffic by protocol, (c) flag any traffic worth a defender's attention
and justify why, and (d) relate their findings to one ASD Essential Eight
mitigation. Deliverable: a 1,200–1,500 word report with annotated screenshots.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Addressing & role identification | LO1, LO2 |
| Protocol characterisation of the capture | LO3, LO4 |
| Defensive interpretation + Essential Eight link | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Protocol analysis accuracy | Correctly identifies all major protocols and explains their behaviour precisely | Identifies major protocols with minor errors | Identifies some protocols; several errors | Misidentifies most traffic |
| Use of tools & evidence | Filters and evidence are precise; every claim is backed by a referenced packet | Mostly precise evidence with small gaps | Evidence is partial or loosely linked | Little or no evidence provided |
| Defensive reasoning | Insightful, correctly tied to Essential Eight/ISM | Sound reasoning with a valid control link | Basic reasoning; weak control link | No meaningful defensive interpretation |
| Communication | Clear, well-structured, correct terminology | Clear with minor lapses | Understandable but disorganised | Unclear or incorrect terminology |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Network segmentation and restriction of inbound/
  outbound traffic are framed as baseline mitigations; the summative assessment
  requires students to connect findings to an Essential Eight control.
- **ACSC Information Security Manual (ISM):** Used as the reference for gateway,
  network, and host controls and for guidance on encrypted DNS.
- **Cybercrime Act 2001 (Cth):** Introduced in Lab 2's reflection to establish
  why scanning must stay within authorised, isolated networks (developed fully
  in F05).

---

## Further Reading

**Kurose, J. & Ross, K. (2021).** *Computer Networking: A Top-Down Approach (8th ed.).* Pearson.
> Relevance: The standard undergraduate networking text; gives the depth behind every topic in this unit.

**Australian Cyber Security Centre (2024).** *Information Security Manual.* ACSC. https://www.cyber.gov.au/ism
> Relevance: The Australian baseline for network controls and the primary local reference for this unit (Australian source).

**Australian Cyber Security Centre (2023).** *Essential Eight Maturity Model.* ACSC. https://www.cyber.gov.au/essential-eight
> Relevance: Connects networking controls to Australia's flagship baseline mitigations (Australian source).

**Sanders, C. (2017).** *Practical Packet Analysis (3rd ed.).* No Starch Press.
> Relevance: A hands-on guide to Wireshark that directly supports Lab 1 and the summative report.

**Lyon, G. (2009).** *Nmap Network Scanning.* Nmap Project. https://nmap.org/book/
> Relevance: The authoritative, freely available reference for the discovery and service-scanning techniques used in Lab 2.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F01 |
| Unit Title | Networking Fundamentals |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | None |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Cybercrime Act 2001 (Cth) |
