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

7. **Analyse** the packets produced by a port scan to determine whether a port
   is open, closed or filtered, independently of the scanner's own label.
8. **Explain** the structure of an HTTP request and response — request line,
   headers, methods, status classes and session cookies — and identify each
   element in a capture.
9. **Distinguish** the local-segment resolution behaviours that carry no
   authentication (ARP, LLMNR/NBT-NS) from authenticated exchanges, and explain
   from a capture why they can be abused.
10. **Explain** the basis on which each capture in this unit is lawful, with
    reference to the *Telecommunications (Interception and Access) Act 1979*
    (Cth) as taught in [F05](F05-legal-ethics-compliance.md).

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

| Knowledge | F01-K04 | Knowledge of the TCP connection state machine and how a scanner infers port state from a response | Topic 7; Lab 3 |
| Knowledge | F01-K05 | Knowledge of HTTP request/response structure, status classes, and cookie-based session state | Topic 8; Lab 4 |
| Knowledge | F01-K06 | Knowledge of unauthenticated local-segment resolution (ARP, LLMNR/NBT-NS) and of DNS as a data-carrying channel | Topic 9; Lab 4 |
| Skill | F01-S03 | Skill in justifying a scanner's port-state output from the captured packets | Lab 3 |
| Skill | F01-S04 | Skill in reading an HTTP conversation, including session-cookie issue and replay, from a capture | Lab 4 |
| Ability | F01-A03 | Ability to state the legal basis for a given packet capture under Australian interception law | Lab 1; Lab 3; Lab 4 |
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


---

### Topic 7: Reading Port State from the Packet

Lab 2 has the learner run `nmap -sn` and `nmap -sV` and write down what nmap
says. This topic is about not believing it. `open`, `closed` and `filtered` are
not properties a port possesses; they are **inferences the scanner draws from
what came back**. A practitioner who cannot reconstruct the inference cannot
tell a real result from an artefact of the network in between.

**The handshake is the probe.** TCP is connection-oriented: before any
application data moves, the two stacks synchronise sequence numbers (RFC 9293).
The client sends a segment with the **SYN** flag set; the server answers
**SYN+ACK**; the client replies **ACK** and the connection is ESTABLISHED. The
decisive point for scanning is that **the target's TCP stack answers the first
segment by itself, before the listening application is involved at all.** A
single SYN is therefore a complete question, and the answer is determined by
kernel state, not by the service.

| What comes back | What it establishes | nmap's label |
|---|---|---|
| SYN+ACK | A socket is in LISTEN; the stack is offering to complete the handshake | `open` |
| RST (usually RST+ACK) | The host is reachable and its stack is answering — nothing is listening | `closed` |
| ICMP unreachable (type 3, codes 1, 2, 3, 9, 10, 13) | Something on the path is refusing on the host's behalf | `filtered` |
| Nothing, after retransmission | No conclusion is available | `filtered` |

**`open` and `closed` are both answers from the target's own stack; `filtered`
is not.** That asymmetry is the whole topic. Note from the table that `filtered`
covers two distinct situations — an explicit ICMP refusal *by something on the
path*, and no reply at all — so the label tells you the target's stack did not
answer for itself, not that nothing answered. A RST is *informative*: it proves
the probe reached a live stack that was permitted to reply. Silence proves
nothing — it is
equally consistent with an inbound drop, an outbound drop of the reply, a dead
host, ordinary packet loss, or a rate limiter that stopped answering after the
fifth probe. nmap encodes this honestly in six states rather than three:
`open`, `closed`, `filtered`, `unfiltered` (the port responded to an ACK probe
but whether it is open could not be determined), and the compound
`open|filtered` and `closed|filtered`, which exist precisely where a scan type
cannot separate the two — UDP, and the FIN/NULL/Xmas scans, where a
non-response is the expected result for an open port.

**Half-open versus connect.** A SYN scan (`-sS`) sends a RST in place of the
final ACK, so the connection never reaches ESTABLISHED; a connect scan (`-sT`)
uses the operating system's `connect()` and completes the handshake. The
difference is plainly visible as the third packet in a capture. What follows
from it is narrower than the word "stealth" suggests: every firewall, flow
collector and network sensor on the path sees the SYN either way. What changes
is only whether an application that logs *accepted connections* ever sees one —
and whether a given application logs a bare connect-and-close at all depends
entirely on that application.

**UDP has no handshake**, so the inference is different again: a reply from the
application means `open`, an ICMP port-unreachable (type 3, code 3) means
`closed`, and silence means `open|filtered`. Host-level ICMP rate limiting is
why a UDP scan is slow — the scanner must wait out the limiter to distinguish
"no answer yet" from "no answer".

**Three ways the label lies.** A firewall configured to reject with a TCP reset
answers on the host's behalf, so a filtered port reports `closed`. A SYN proxy,
load balancer, tarpit or honeypot that answers SYN+ACK on every port makes an
entire host look `open`. A rate limiter or IPS that starts dropping after a
threshold turns genuinely open ports into `filtered`, and the result changes if
you scan again more slowly. The defence against all three is the same: capture
your own scan, read the responses, use `--reason` — which prints the evidence
nmap actually used (`syn-ack`, `reset`, `no-response`, `host-unreach`) rather
than the conclusion — and treat a scan as a measurement with error bars.

One local-segment detail surprises people: on an Ethernet network nmap must
resolve each target's MAC address before it can send anything, so a scan of a
local /24 opens with a burst of ARP requests. That is both the loudest artefact
the scan produces and the subject of Topic 9.

**Key concepts:**
- The three-way handshake as the probe; the target's stack answers before the
  application does
- SYN+ACK, RST and ICMP unreachable as evidence; silence as the absence of
  evidence
- nmap's six states, `--reason`, and where the compound states come from
- `-sS` versus `-sT` on the wire, and the limits of "stealth"
- Middleboxes that answer for the host, and why the printed state is an
  inference

**Australian context:** The ACSC ISM and the Essential Eight both expect inbound
and outbound traffic to be restricted, so `filtered` is the *expected* result
when scanning a well-configured gateway from outside — and a `closed` from
outside is itself a finding, because it proves the probe reached the host. On
the legal side, this unit's scanning stays inside an isolated lab. Whether a
bare port scan amounts to "access to data held in a computer" under
*Criminal Code Act 1995* (Cth) sch 1 Part 10.7 is contested; what is not
contested is that the offences turn on **authorisation**, and that the lab's
isolation is what keeps the question academic. See
[F05](F05-legal-ethics-compliance.md). Relevant adversary behaviour: MITRE
ATT&CK T1595.001 (Active Scanning: Scanning IP Blocks) and T1046 (Network
Service Discovery).

---

### Topic 8: The Anatomy of an HTTP Request

Topic 4 established what a normal HTTP exchange looks like from the outside.
This topic opens it. HTTP is a **text protocol carried over a TCP connection**:
once the handshake of Topic 7 completes, the client simply writes characters,
and the structure of those characters is the entire protocol. Everything a later
unit will teach about web attack and defence is a consequence of that structure,
so the structure has to be learned first.

**The request.** The first line is the **request line**: a method, a space, the
request target, a space, the HTTP version, then CRLF. After it come **header
field lines**, one per line, each `name: value` and CRLF. Then a **bare CRLF** —
an empty line — and then, optionally, a body. That empty line is the *only*
thing separating metadata from content. Nothing else marks the boundary, which
is why control characters in header values matter so much in later units.

```
GET /index.html HTTP/1.1
Host: example.internal
User-Agent: curl/7.81.0
Accept: */*

```

**Methods are promises, not controls.** RFC 9110 defines `GET` (retrieve; *safe*
and *idempotent*), `HEAD` (a GET whose response carries no body — this is what
`curl -I` sends), `POST` (neither safe nor idempotent), `PUT`, `DELETE`,
`OPTIONS` and others. "Safe" means the method is not expected to change server
state. It is a semantic undertaking by the application author, and **nothing in
the protocol enforces it**: a `GET` can and often does change state. That gap
between what a method promises and what an application does is the root of a
whole family of later problems, and it is visible from the request line alone.

**The response** mirrors the request: a **status line** (version, status code,
reason phrase), headers, a blank line, then the body. The five status classes
carry most of the meaning — **1xx** informational, **2xx** success, **3xx**
redirection, **4xx** client error, **5xx** server error. For a defender the
individual codes matter too: `401` (not authenticated) is a different statement
from `403` (authenticated and refused), which is a different statement again
from `404` (no such resource) — and the *ratio* between them from one source
address is what enumeration looks like in a log, which is the bridge to F06's
frequency analysis.

**Headers that carry security meaning.** `Host` names the virtual host and is
the only reason one IP address can serve many sites — it is the plaintext twin
of the TLS SNI value recorded in Lab 1. `User-Agent` is asserted by the client
and trivially forged, so it is evidence of habit, never of identity.
`Content-Length` and `Transfer-Encoding: chunked` are two different ways of
saying where the body ends. `Authorization` and `Cookie` carry credentials.

**HTTP is stateless, and sessions are manufactured.** Each request stands alone;
the server has no memory of the previous one. The state we experience as "being
logged in" is constructed: the server issues `Set-Cookie: session=<opaque
value>` in a response, and the client replays `Cookie: session=<value>` on every
subsequent request to that origin. **After login, the session identifier *is*
the authentication for every request** — whoever holds the string is the user.
The whole of session security follows from that single fact: the value must be
unpredictable (entropy), must never travel in plaintext (`Secure`, and TLS),
should be unreadable from page script (`HttpOnly`), and should be restricted in
cross-site requests (`SameSite`). Those attributes appear **only in
`Set-Cookie`** — the browser enforces them and the `Cookie` header sent back
carries the bare name and value, so the server never sees them again. A
practitioner who has watched a cookie issued and replayed in a capture
understands session hijacking without needing it demonstrated.

**One page is many cycles.** A single HTML response triggers further requests for
scripts, styles and images; persistent connections reuse one TCP connection for
several exchanges. HTTP/2 multiplexes many streams over one connection, and
HTTP/3 runs over QUIC on UDP — which has a direct practical consequence for
Lab 1: "Follow TCP Stream" reconstructs one conversation only while there is one
conversation per connection to follow.

This topic stops at reading the cycle. Attacks against it — injection into the
request, script in the response, or a server coerced into making requests of its
own — belong to later units; they are unreadable without this substrate.

**Key concepts:**
- Request line, header block, the CRLF that terminates it, and the body
- Method semantics (safe, idempotent) as application promises the protocol does
  not enforce
- Status classes, and the defensive meaning of 401 versus 403 versus 404
- `Host` as the plaintext twin of TLS SNI; `User-Agent` as an unverifiable claim
- Statelessness, and the `Set-Cookie` → `Cookie` loop that manufactures a session
- Cookie attributes as client-side enforcement the server never sees again

**Australian context:** A stolen session identifier gives an attacker exactly
what the account can see, without any password being broken. Whether such access
becomes a notifiable data breach is [F05](F05-legal-ethics-compliance.md)'s
question, under the Privacy Act's NDB scheme; the point here is that the
technical event that triggers it is a string replayed in a header, and it is
visible on the wire.

---

### Topic 9: Trust on the Local Segment — ARP, Name Resolution and DNS

The protocols that make a local network usable were designed for a cooperative
segment. They carry no authentication at all, so on a shared network **the first
host to answer wins**. This topic is observational: the learner reads the
behaviour in a capture and reasons about what the receiving host could possibly
have checked. The answer, repeatedly, is nothing.

**ARP (RFC 826) verifies nothing.** A host that needs the MAC address for an IP
on its own subnet broadcasts "who has 10.0.0.5?"; a reply arrives carrying a
sender MAC and the receiving stack caches it. There is no signature, no nonce,
no binding to any prior state — the frame format contains no field a receiver
could use to test the claim. Implementations also accept **unsolicited**
(gratuitous) replies and update the cache from them, because that is how a
failover address legitimately moves between machines. What is observable in a
capture: two replies to one request, one MAC claiming several IPs, or a cache
entry that changes while the real owner has not moved. Wireshark raises expert
information when it sees a duplicate address in use. The abuse built on this is
MITRE ATT&CK **T1557.002** (Adversary-in-the-Middle: ARP Cache Poisoning); the
learner here observes only the mechanism that makes it possible.

**Name resolution falls back to asking the room.** A client resolves a name from
its hosts file, then DNS. If DNS says the name does not exist — or no DNS server
is configured — Windows clients have historically fallen back to **LLMNR**
(RFC 4795; UDP 5355, multicast 224.0.0.252 and ff02::1:3) and then **NBT-NS**
(RFC 1001/1002; UDP 137, broadcast). Apple and Linux hosts use **mDNS**
(UDP 5353). Each of these sends the question to *every host on the segment* and
accepts an answer from whichever replies. Nothing in the query limits who may
reply, and nothing in the reply demonstrates any right to the name.

That is why name-resolution poisoning works, and why it is so productive in
practice: the queries that reach this fallback are mistakes — a mistyped share
name, a stale drive mapping, a `wpad` lookup, a decommissioned server still in
someone's shortcuts. A host that answers "yes, that is me" receives a connection
the client believed was going somewhere trusted, and for SMB or HTTP
authentication the client may offer credential material as part of connecting.
The behaviour is catalogued as **T1557.001** (LLMNR/NBT-NS Poisoning and SMB
Relay). The mitigation is to disable the fallback, which is tolerable precisely
because a healthy DNS makes it unnecessary.

**DNS is a resolution protocol and a transport.** The query name (QNAME) is a
field **the client fills in**, and an internal resolver will forward it to
whoever is authoritative for that zone — on the client's behalf, from the
resolver's own permitted egress, in environments where the client itself has no
direct route out. Whatever was encoded into the name arrives at a server the
attacker controls, and the answer (TXT and other record types can carry
arbitrary strings) travels back the same way. That is the structural reason DNS
is a covert channel: not a flaw, but the resolution service working exactly as
designed on data an endpoint chose.

**Scope, stated deliberately.** F01 stops at that structure. The *detection* of
DNS tunnelling and exfiltration — subdomain entropy and length, query volume per
domain, record-type distribution, and separating abuse from legitimately noisy
CDN and telemetry traffic — is taught at depth in
[TH04](../../degrees/operational/threat-hunting/TH04-network-based-hunting.md)
Topic 3 and
[DF04](../../degrees/operational/dfir/DF04-network-forensics.md) Topic 4, with
forensic scoping of the data moved in DF04 Topic 5. This unit does not repeat
them, and should not: a learner arrives at those units already knowing *why* a
name can carry data, which is the question the heuristics assume has been
answered. Related techniques: **T1071.004** (Application Layer Protocol: DNS)
and **T1048** (Exfiltration Over Alternative Protocol).

**Key concepts:**
- ARP has no field a receiver can verify; caches accept unsolicited replies
- The DNS → LLMNR → NBT-NS fallback broadcasts the question to the whole segment
- Poisoning succeeds on mistakes: typos, stale mappings, `wpad`
- The QNAME as client-controlled data the resolver carries outbound
- Observable artefacts: duplicate replies, one MAC for many IPs, multicast name
  queries for names that do not exist

**Australian context:** The ACSC ISM and the Essential Eight treat egress
control and monitoring as baseline expectations, and DNS is the standard
counter-example — the one outbound path that is almost never blocked, because
blocking it breaks everything. Capturing this behaviour is itself regulated:
every observation in this unit is made on traffic the learner generated, on an
isolated segment, for the reasons set out in
[F05](F05-legal-ethics-compliance.md) and repeated in each lab.

---

## Labs & Exercises

### Lab 1: Capturing & Reading Live Traffic

**Objective:** Capture live network traffic and analyse a DNS-then-HTTP exchange
to demonstrate understanding of protocol behaviour across layers.

**Prerequisites:**
- Topics 1, 4, and 6
- [F05](F05-legal-ethics-compliance.md) § *Interception, Surveillance and
  Monitoring* — read it before you capture anything
- A local lab VM with internet access, on a network you own or administer

**Before you capture — the legal position:**

In Australia packet capture is not a neutral act. The *Telecommunications
(Interception and Access) Act 1979* (Cth) s 7(1) **prohibits** intercepting a
communication passing over a telecommunications system, and it reaches doing an
act that *enables* interception — it is a prohibition with narrow exceptions,
not a permission to monitor. What makes this lab lawful is narrow and specific:
**you generate every packet you capture**, so nothing is recorded without the
knowledge of the person making the communication, and you capture only your own
host's traffic. Two changes to your *method* — not your intention — would remove
that basis: capturing traffic you did not generate (anything from another
person's device on the same segment), and putting the interface into promiscuous
mode on a network you share. Do neither. The *Surveillance Devices Act 2004*
(Cth) is a law-enforcement authorising statute and confers nothing on you; State
and Territory surveillance-devices law, and workplace surveillance legislation
in some jurisdictions, may apply on top. F05 sets out the exceptions in full,
including the **written** s 7(2)(aaa) network-protection authorisation that
professional monitoring actually depends on.

**Environment:**
- Operating System: Ubuntu 22.04 LTS (desktop) in a local VM
- Tools: Wireshark and `tcpdump` (both free/OSS)
- Minimum hardware: 4 GB RAM allocated to the VM, 2 vCPU, 15 GB disk (well
  within the 8 GB / 4-core / 50 GB spec; no GPU required)

**Instructions:**

1. Launch the VM and confirm network connectivity with `ip addr` and
   `ip route` — record the host's IP, subnet mask (CIDR), and default gateway.
2. Start a capture scoped to your own traffic, with promiscuous mode **off**:
   `sudo tcpdump -p -i <your-interface> -w lab1.pcap host <your-ip>` — using the
   interface and address you recorded in step 1, not `any`. `-p` stops `tcpdump`
   from requesting promiscuous mode (it cannot un-set promiscuous mode that
   something else has already requested), and the `host` filter discards frames
   that are not yours before they ever reach the file. `-i any` does the
   opposite: it captures every interface at once. Leave the capture running.
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

4. Name the specific fact about *this* capture that makes it lawful under the
   framing in [F05](F05-legal-ethics-compliance.md), then describe one change to
   your method — not to your intention — that would remove it.

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


---

### Lab 3: Why a Port Answers the Way It Does

**Objective:** Produce open, closed and filtered ports deliberately on a host you
control, capture the same scan from both ends, and justify every state `nmap`
prints from the packets rather than from the label.

**Prerequisites:**
- Topics 3, 6, and 7
- Lab 2 completed

**Environment:**
- Operating System: two Ubuntu 22.04 LTS VMs — *scanner* and *target* — on a
  **host-only / internal** network
- Tools: `nmap`, `tcpdump`, Wireshark, `iptables`, `python3` (all free/OSS, all
  in the Ubuntu main repository)
- Minimum hardware: 2 GB RAM / 1 vCPU / 10 GB per VM — 4 GB / 2 vCPU / 20 GB for
  the pair, well within the 8 GB / 4-core / 50 GB spec; no GPU, no licence

**Authorisation and legal basis:** both endpoints are yours, the segment is
host-only, and every packet you capture is one you generated. That is what makes
this lab lawful, and it is the same basis Lab 1 relies on — see
[F05](F05-legal-ethics-compliance.md) § *Interception, Surveillance and
Monitoring*. Do not substitute a host you do not own, and do not move this lab
onto a network you share.

**Instructions:**

1. On the **target**, create four conditions:
   - **8000 — a real listener:** `python3 -m http.server 8000`
   - **8001 — nothing listening,** no firewall rule
   - **8002 — silently discarded:**
     `sudo iptables -A INPUT -p tcp --dport 8002 -j DROP`
   - **8003 — refused by the firewall on the host's behalf:**
     `sudo iptables -A INPUT -p tcp --dport 8003 -j REJECT --reject-with tcp-reset`

   Record the resulting ruleset with `sudo iptables -L INPUT -n -v`.
2. Start a capture on **each** VM, with promiscuous mode off:
   `sudo tcpdump -p -i <iface> -w lab3-<role>.pcap 'tcp portrange 8000-8003 or arp or icmp'`
3. From the **scanner**, run
   `sudo nmap -sS -Pn --reason -p 8000-8003 <target-ip>` and record the state
   **and the reason** for each port.
4. Stop both captures. From the packets — not from the nmap output — complete
   this table:

   | Port | Probe sent | Response at scanner | Probe seen at target | nmap state | nmap reason | Packet no. |
   |---|---|---|---|---|---|---|

5. Ports 8001 and 8003 both report `closed`. Using **only** the scanner capture,
   explain why that label cannot distinguish "nothing is listening" from "a
   firewall answered for the host". Then state what the target capture adds, and
   note that if the rejecting device were a different hop, artefacts such as the
   IP TTL or IP ID of the RST might betray it — on a single host they will not.
6. Compare the two captures for port 8002. The target capture shows the SYN
   arriving; the scanner capture shows nothing coming back. On Linux a `tcpdump`
   tap sees an **inbound** packet before netfilter decides to drop it (outbound
   packets are seen after netfilter), which is why the target's own capture can
   prove the probe was delivered and the scanner's cannot. In one sentence,
   state what `filtered` therefore means and what it does not.
7. Re-run as a connect scan:
   `sudo nmap -sT -Pn --reason -p 8000-8003 <target-ip>`. In the capture for port
   8000, find the **third** packet of the handshake: under `-sS` it is a RST and
   the connection never reaches ESTABLISHED; under `-sT` it is an ACK and it
   does. Explain what follows for what each scan can leave in an application's
   own logs — and note that whether an application logs a bare connect-and-close
   at all depends entirely on that application.
8. Run `sudo nmap -sU -Pn --reason -p 53,123 <target-ip>`. UDP has no handshake:
   record which port comes back `closed` (ICMP type 3, code 3) and which comes
   back `open|filtered`, and explain in one sentence why the compound state has
   to exist.
9. Filter the scanner capture on `arp`. Find the ARP exchange that preceded the
   first TCP probe and record the target's MAC address. Keep this capture — you
   will return to it in Lab 4.
10. **Clean up:** remove the two rules
    (`sudo iptables -D INPUT -p tcp --dport 8002 -j DROP` and the matching
    `-D` for 8003) and confirm with `sudo iptables -L INPUT -n -v`. They will not
    survive a reboot unless you have installed something to persist them, but
    leaving them in place will confuse your next lab.

**Expected Output:**

A completed port-state table with a packet number in every row; a short written
justification of each state from the packets; an explicit statement of the
8001/8003 ambiguity and of what resolves it; the `-sS` versus `-sT` third-packet
comparison; and the ARP exchange. A learner who has done this can be handed any
scan output and answer the only question that matters — what is the evidence?

**Reflection Questions:**

1. If the DROP rule were on a gateway between you and the target rather than on
   the target itself, which cells of your table would change and which would not?
2. A device that answers SYN+ACK on every port makes a whole host look `open`.
   From the capture alone, name two features that would distinguish that from a
   host genuinely running thousands of services.
3. The ISM and Essential Eight expect inbound and outbound traffic to be
   restricted. From outside a correctly configured gateway, which state should
   dominate a scan — and what does a `closed` result tell an attacker that a
   `filtered` result does not?
4. Under the framing in [F05](F05-legal-ethics-compliance.md), what single change
   to this lab's setup would remove its lawful basis?

---

### Lab 4: Reading an HTTP Conversation — and the Name That Started It

**Objective:** Read an HTTP request and response byte by byte from a capture,
watch a session identifier being issued and replayed, and observe what a host
does on the wire when DNS cannot answer a name.

**Prerequisites:**
- Topics 4, 6, 8, and 9
- Lab 3 completed (same two VMs, same isolated segment)

**Environment:**
- Operating System: the two Ubuntu 22.04 LTS VMs from Lab 3, host-only network
- Tools: `python3` (standard library only), `curl`, `tcpdump`, Wireshark,
  optionally `netcat` and Samba's `nmbd` — all free/OSS and in the Ubuntu main
  repository
- Minimum hardware: as Lab 3

**Authorisation and legal basis:** as Lab 3 — both hosts are yours, the segment
is isolated, and you generate every packet you capture. See
[F05](F05-legal-ethics-compliance.md).

**Instructions:**

*Part A — the request on the wire*

1. On the **target**, serve a directory: `python3 -m http.server 8000`.
2. On the **client**, start a capture:
   `sudo tcpdump -p -i <iface> -w lab4.pcap 'tcp port 8000 or tcp port 8001 or udp port 53 or udp port 5355 or udp port 5353 or udp port 137 or arp'`
3. Run `curl -v http://<target-ip>:8000/`. In curl's output, the lines beginning
   `>` are what you sent and `<` is what came back. Label, on paper, the request
   line, the method, the request target, the version, every header, and the
   blank line.
4. In Wireshark, apply the display filter `http.request`, select the packet, and
   use **Follow → TCP Stream** to see the raw bytes. Confirm that the empty line
   between the headers and the body is the only boundary marker present.
5. Run `curl -I http://<target-ip>:8000/` and compare. `HEAD` returns the same
   headers with no body: explain why a `Content-Length` header can be present
   when no body follows it.
6. Request a path that does not exist, then repeat with `curl -X POST`. Record
   the status code returned in each case and which class it falls into — do not
   assume; read it off the wire.
7. Prove HTTP is text by writing a request by hand:
   `printf 'GET / HTTP/1.1\r\nHost: test\r\n\r\n' | nc <target-ip> 8000`.
   (Netcat variants differ: the OpenBSD `nc` in Ubuntu takes `nc host port`,
   while other builds may need different flags — check `man nc` on your image.)

*Part B — how a session is manufactured*

8. Write a short `http.server` script (about fifteen lines, standard library
   only — this is F03's skill applied) that, when a request arrives with **no**
   `Cookie` header, responds with
   `Set-Cookie: session=<secrets.token_hex(16)>`, and when a cookie **is**
   present, echoes the value it received. Run it on port 8001.
9. Run `curl -v -c jar.txt http://<target-ip>:8001/` and then
   `curl -v -b jar.txt http://<target-ip>:8001/`. Find `Set-Cookie` in the first
   response and `Cookie` in the second request, and locate both in the capture.
10. Answer in writing: what does the server know about the second request that it
    did not know about the first, and what is the *entire* evidence for it?
11. Re-issue the cookie with `Secure; HttpOnly; SameSite=Lax` appended. Confirm
    from the capture that those attributes appear **only** in `Set-Cookie` and
    never in the `Cookie` header sent back. State who enforces them, and what
    follows for a server trying to verify that they were honoured.

*Part C — the name that started it*

12. From the client, request a hostname with no DNS record:
    `curl -v http://labweb-nonexistent:8000/`. Watch for the DNS query, the
    negative answer, and — if the client is configured for it — an LLMNR query.
    On Ubuntu this is systemd-resolved's behaviour; check it with
    `resolvectl status` and the `LLMNR=` setting in
    `/etc/systemd/resolved.conf`. **If no LLMNR packet appears, that is a valid
    result:** record the configuration that produced it.
13. Filter the capture on `llmnr` (and `mdns`, `nbns`). For any query you find,
    note the destination address and port and answer: which hosts on this segment
    were entitled to reply, and which field of the packet decides that?
14. **NBT-NS caveat (R3).** NBT-NS is a Windows client behaviour, and Windows
    evaluation media is proprietary — so it is not a required step here. Either
    (a) run Samba's `nmbd` on a Linux VM (free/OSS, in Ubuntu main) to put
    NetBIOS name-service traffic on the segment and capture it, or (b) treat
    this step as reading only. **Neither substitute reproduces a Windows
    client's fallback *ordering* (DNS → LLMNR → NBT-NS)** — state that
    limitation explicitly in your write-up rather than implying you observed it.
15. Filter on `arp` and find the resolution of the target that preceded your
    first TCP connection (compare it with the one you kept from Lab 3). Write one
    sentence naming the field in the ARP reply that the receiving host verifies.

**Expected Output:**

An annotated request and response with every structural element labelled and
tied to a packet; a cookie trace showing issue-then-replay with packet
references and a written statement of what the session identifier alone proves;
the LLMNR/mDNS and ARP observations; and an explicit note of what could **not**
be reproduced on free/OSS software and why.

**Reflection Questions:**

1. A `User-Agent` string says the client is a particular browser. What does that
   prove, and what would have to change for a client's claim about itself to be
   trustworthy?
2. The session identifier is replayed on every request. Name three distinct
   places it could be stolen from, and say which of them TLS does **not**
   protect.
3. LLMNR answers a question DNS declined. Propose one control in the spirit of
   the ISM or Essential Eight, and say what would break if you applied it.
4. [TH04](../../degrees/operational/threat-hunting/TH04-network-based-hunting.md)
   hunts DNS tunnelling using subdomain entropy and query volume. From what you
   saw of the QNAME in step 12, explain why a query name is a usable carrier of
   data in the first place — the question those heuristics assume you have
   already answered.

---

## Assessment

### Formative Assessment: Protocol Behaviour Quiz

**Type:** Self-check quiz with answer key

**Description:** A short quiz covering layer identification, subnet calculations,
"normal vs abnormal" protocol behaviour, and two mechanism sets: given a response
to a TCP probe (SYN+ACK, RST, ICMP unreachable, or nothing), name the state and
say what it does **not** establish; and given a block of HTTP request or response
text, name every structural element and the status class. Students self-mark
against the provided key and note any topic to revisit.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO7, LO8

**Feedback mechanism:** Self-check answer key with explanations for each item.

---

### Summative Assessment: Network Investigation Report

**Type:** Practical lab report

**Description:** Students are given (or capture) a PCAP and a brief scenario:
"A workstation on an isolated lab subnet is behaving unexpectedly." They must
(a) identify the host's addressing and likely role, (b) characterise the
observed traffic by protocol, (c) justify, from the packets, the state of any
scanned port visible in the capture and state what the evidence cannot settle,
(d) read any HTTP conversation present down to the request line, headers and any
session identifier, (e) flag any unauthenticated local-segment resolution (ARP,
LLMNR/NBT-NS) that appears and explain why it is abusable, (f) relate their
findings to one ASD Essential Eight mitigation, and (g) state the basis on which
capturing that traffic would have been lawful. The capture may be one the
student generated in Labs 3 and 4. Deliverable: a 1,500–2,000 word report with
annotated screenshots.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6, LO7, LO8, LO9, LO10

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Addressing & role identification | LO1, LO2 |
| Protocol characterisation of the capture | LO3, LO4 |

| Port-state justification from the packets | LO7 |
| HTTP conversation read down to its elements | LO8 |
| Unauthenticated local-segment resolution identified | LO9 |
| Lawful basis for the capture | LO10 |

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
- **Criminal Code Act 1995 (Cth) sch 1 Part 10.7:** The operative computer
  offences. The *Cybercrime Act 2001* (Cth) is the amending Act that inserted
  them and is a historical citation, not the law a practitioner applies. Labs 2
  and 3 stay inside an isolated lab because the offences turn on
  **authorisation** — see [F05](F05-legal-ethics-compliance.md), which sets out
  Part 10.7 in full.
- **Telecommunications (Interception and Access) Act 1979 (Cth):** Governs packet
  capture. Section 7(1) **prohibits** intercepting a communication passing over a
  telecommunications system, with narrow exceptions — it is not a permission to
  monitor. Labs 1, 3 and 4 rely on the narrowest basis available: the learner
  generates every captured packet, on an isolated segment, so nothing is recorded
  without the knowledge of the person making the communication. F05 sets out the
  exceptions, including the written s 7(2)(aaa) network-protection authorisation
  that professional monitoring depends on.
- **Surveillance Devices Act 2004 (Cth), with State and Territory surveillance-
  devices and workplace-surveillance law:** The Commonwealth Act confers powers
  on law enforcement; it is not a source of permission for a student or a
  corporate security team. Private monitoring is constrained by State and
  Territory surveillance-devices law and, in some jurisdictions, dedicated
  workplace surveillance legislation. Jurisdiction-specific; treated in F05.

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


**Eddy, W. (ed.) (2022).** *RFC 9293: Transmission Control Protocol (TCP).* IETF. https://www.rfc-editor.org/rfc/rfc9293.html
> Relevance: The current normative TCP specification (it obsoletes RFC 793); the connection state machine that Topic 7 and Lab 3 reason from.

**Fielding, R., Nottingham, M. & Reschke, J. (eds.) (2022).** *RFC 9110: HTTP Semantics.* IETF. https://www.rfc-editor.org/rfc/rfc9110.html
> Relevance: The authority for the methods, status classes and header-field semantics read in Topic 8 and Lab 4, including what "safe" and "idempotent" actually promise.

**Barth, A. (2011).** *RFC 6265: HTTP State Management Mechanism.* IETF. https://www.rfc-editor.org/rfc/rfc6265.html
> Relevance: Defines Set-Cookie and Cookie and the attribute model that makes session identifiers the whole of web session security.

**Aboba, B., Thaler, D. & Esibov, L. (2007).** *RFC 4795: Link-Local Multicast Name Resolution (LLMNR).* IETF. https://www.rfc-editor.org/rfc/rfc4795.html
> Relevance: The fallback name-resolution protocol observed in Topic 9 and Lab 4 — read with its Security Considerations, which state the trust assumptions the abuse depends on.

**Australian Government (1979).** *Telecommunications (Interception and Access) Act 1979 (Cth).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The prohibition that governs every capture in this unit; read with F05's treatment before Lab 1 (Australian source).

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

| Offensive Content | No — Labs 2 and 3 run host discovery and port scans, but only against the learner's own hosts on an isolated host-only segment, and no lab has the learner run an exploit or a credential attack. Classification confirmed at Practitioner Review |
| Prerequisites | None |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |

| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 1–4 (Remember, Understand, Apply, Analyse) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) sch 1 Pt 10.7 (Cybercrime Act 2001 (Cth) as the amending Act — historical citation); Telecommunications (Interception and Access) Act 1979 (Cth); Surveillance Devices Act 2004 (Cth) |
