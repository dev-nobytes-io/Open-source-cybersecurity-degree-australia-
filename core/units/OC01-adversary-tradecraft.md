# OC01: Adversary Tradecraft & TTPs

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches students to think like an adversary so they can defend like a
professional. It covers how real intrusion sets operate — their tactics,
techniques, and procedures (TTPs) — using **MITRE ATT&CK** as the common
taxonomy and **threat-informed defense** as the organising philosophy. The
central idea is that defence is a living system: adversary behaviour changes
constantly, and detections, logging, infrastructure, and automation must adapt to
that changing reality rather than sit static. Students learn to read adversary
behaviour, map it to ATT&CK, and reason about which behaviours are observable and
defensible.

Threat-informed defense (TID), as developed by the **MITRE Center for
Threat-Informed Defense (CTID)**, reframes security operations around what
adversaries actually do. In the Australian context, this is exactly the posture
the ACSC promotes through its threat advisories and the ASD *Cyber Threat
Report*: prioritise defences against the behaviours seen in the real threat
landscape. OC01 is the first operational unit and the conceptual backbone for
OC02 (Security Monitoring), OC05 (Threat Intelligence), OC06 (Offensive Security
Concepts), and the Threat Hunting, Detection Engineering, and CTE majors.

---

## Prerequisites

- F01 — Networking Fundamentals
- F02 — Operating Systems & Administration
- F04 — Security Concepts & Principles
- F06 — Data & Log Analysis

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the MITRE ATT&CK framework to describe and categorise adversary
   behaviour across tactics, techniques, and sub-techniques.
2. **Analyse** an intrusion narrative to extract TTPs and represent them in
   ATT&CK Navigator and an Attack Flow.
3. **Differentiate** indicators along the Pyramid of Pain and explain why
   behaviour-based detection is more durable than atomic indicators.
4. **Apply** threat-informed defense to prioritise defensive effort against the
   techniques most relevant to a given organisation.
5. **Examine** how CTID resources (emulation library, sensor mappings, M3TID)
   support a continuously adapting defence.
6. **Analyse** the gap between an organisation's current visibility and the
   techniques it most needs to detect.
7. **Examine** a representative adversary technique to explain its procedure, the
   telemetry and host artefacts it leaves behind, and how the procedure varies
   between threat actors.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of adversary
behaviour and the threat-informed defense paradigm, anchored in MITRE ATT&CK and
CTID research.

**Skills (AQF 7.2):** Students develop cognitive and analytical skills by
deconstructing intrusions into TTPs, mapping them to a structured taxonomy, and
reasoning about detection and visibility.

**Application (AQF 7.3):** Students apply these skills to prioritise defensive
effort for a realistic organisation against the Australian threat landscape,
using ATT&CK and CTID tooling as a professional would.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0569 | Apply cyber threat frameworks (e.g. MITRE ATT&CK) to characterise adversary behaviour | Lab 1 — Mapping an Intrusion to ATT&CK |
| NIST NICE DCWF | 2023 | Threat/Warning Analyst | AN-TWA-001 | T0707 | Analyse threat information to identify adversary tactics, techniques, and procedures | Lab 2 — Threat-Informed Prioritisation with Navigator |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Threat intelligence | THIN | Level 4 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Threat Analysis | Practitioner | Lab 1, Lab 2 |

### MITRE ATT&CK Techniques (Topic 3)

> The technique IDs below index the worked catalogue in Topic 3. They are
> **provisional** pending Framework Custodian verification against MITRE ATT&CK
> v19; they are teaching references, not official NICE/DCWF task mappings, and no
> "official" task statement is asserted for them.

| Tactic | Technique | ID | Analysed in Topic 3 as | Primary telemetry / data source |
|---|---|---|---|---|
| Initial Access | Phishing | T1566 | Lure delivery and the Office/archive → interpreter process break | Email gateway logs; process creation (Event ID 4688 / Sysmon 1) |
| Execution | Command and Scripting Interpreter | T1059 | In-memory / interpreter execution and obfuscation | PowerShell Script Block Logging (Event ID 4104); process creation |
| Persistence | Scheduled Task/Job | T1053.005 | Re-launch on trigger; Run-key / service / cron variants | Event ID 4698; TaskScheduler/Operational; `Tasks\` + registry |
| Privilege Escalation | Abuse Elevation Control Mechanism | T1548 | UAC bypass / sudo / setuid abuse of legitimate paths | Integrity-level mismatch in process creation; `auth.log`/auditd |
| Credential Access | OS Credential Dumping: LSASS Memory | T1003.001 | Theft of NTLM / Kerberos material from LSASS | Handle to lsass (Sysmon 10); 4656/4663; minidump file |
| Lateral Movement | Remote Services | T1021 | RDP / SMB / WinRM movement with stolen credentials | Logon events (4624 type 10/3, 4672); 5140/5145; 7045 |
| Command and Control | Application Layer Protocol | T1071 | HTTPS / DNS beaconing that mimics normal traffic | Proxy/DNS logs; beacon periodicity; TLS/JA3 fingerprint |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | OC01-K01 | Knowledge of MITRE ATT&CK as a common language for adversary tactics, techniques, and procedures | Topic 2 |
| Knowledge | OC01-K02 | Knowledge of representative adversary techniques across the intrusion lifecycle — their procedures, the telemetry/artefacts they leave, and how they vary between actors | Topic 3 |
| Knowledge | OC01-K03 | Knowledge of the Pyramid of Pain and what makes a detection durable | Topic 4 |
| Knowledge | OC01-K04 | Knowledge of threat-informed defense and CTID tooling (emulation library, sensor mappings, M3TID) | Topic 1; Topic 5 |
| Skill | OC01-S01 | Skill in extracting TTPs from an intrusion narrative and mapping them to ATT&CK | Lab 1 |
| Skill | OC01-S02 | Skill in visualising and prioritising coverage with ATT&CK Navigator | Lab 2 |
| Ability | OC01-A01 | Ability to prioritise defensive effort against the TTPs most relevant to an organisation | Lab 2; Topic 6 |
| Ability | OC01-A02 | Ability to identify gaps between current visibility and adversary behaviour | Topic 6; Summative |
| Task | T0569 | Apply cyber threat frameworks (e.g. MITRE ATT&CK) to characterise adversary behaviour | Lab 1 |
| Task | T0707 | Analyse threat information to identify adversary tactics, techniques, and procedures | Lab 2 |

---

## Topics

### Topic 1: The Threat-Informed Defense Paradigm

Threat-informed defense is the practice of applying a deep understanding of
adversary behaviour to the design, operation, and continuous improvement of
defences. This topic introduces the TID philosophy: defences should be driven by
what adversaries actually do, measured against real behaviour, and continuously
adapted as the threat landscape shifts. It contrasts TID with compliance-driven
and tool-driven security, and introduces CTID as the body advancing the discipline
through open research.

**Key concepts:**
- Threat-informed defense vs compliance-driven and tool-driven security
- Defence as a living system that adapts to a changing adversary
- The role of MITRE CTID and its open-source body of work

**Australian context:** The ACSC's advisory-led, behaviour-focused guidance
exemplifies threat-informed defense at a national level.

---

### Topic 2: MITRE ATT&CK as a Common Language

ATT&CK is a curated knowledge base of adversary tactics (the "why"), techniques
and sub-techniques (the "how"), and procedures (specific implementations). This
topic teaches fluency in the model: navigating the matrix, reading a technique
page (detection, mitigation, data sources), and using ATT&CK as the shared
vocabulary that connects intel, detection, response, and emulation.

**Key concepts:**
- Tactics, techniques, sub-techniques, and procedures
- Reading a technique: detections, mitigations, and data sources
- ATT&CK as the lingua franca across the security lifecycle

---

### Topic 3: The Intrusion Lifecycle — A Worked Technique Catalogue

Naming the tactics is not the same as understanding the attack. This topic
replaces a checklist of lifecycle phases with a worked catalogue of the techniques
a defender must actually recognise. Each entry is examined at the level that
matters operationally: what the adversary concretely does (the **procedure**),
what that activity **leaves behind** for a defender to find (the telemetry and
host artefacts — the "opportunity to detect" the lifecycle framing only gestures
at), and how the same technique is realised differently by different actors (the
point of the word *procedures*). This is analysis of behaviour, not execution:
OC01 reasons about attacks from the defender's chair. Running a technique against
a live target is a hands-on activity governed by the authorisation regime taught
in F05/CE01 and by Part 10.7 of the *Criminal Code Act 1995* (Cth), and is
deferred to the Cyber Threat Emulation major; **no lab in this unit executes an
attack.**

The catalogue builds on the Foundation substrate and does not re-teach it. Where
an entry turns on how Windows authentication or a Linux privilege primitive works,
it references **F02** (the process and identity substrate) and **F01** (TCP port
state, HTTP and DNS anatomy, ARP) and analyses the *attack* that abuses the
primitive rather than re-explaining the primitive. Throughout, the vendor-neutral
evidence is the native Windows Security event log and Linux `auditd`/`journald`
(F02 Topic 5); Sysmon is named where its view is sharper, but it is a free
(Microsoft Sysinternals) *closed-source* augmentation, not a requirement.

**T1566 — Phishing (Initial Access).**
- *Procedure:* the adversary delivers a lure by email — a weaponised attachment
  (a macro-enabled Office document, or an ISO/LNK bundle that sidesteps the
  mark-of-the-web) or a link to a credential-harvest page or payload. Execution
  begins when the user opens it and the Office application or archive handler
  spawns a child process (e.g. `winword.exe` → `powershell.exe`) — the anomalous
  parent/child break F02 Topic 1 teaches you to read.
- *Leaves behind:* at the gateway, mail headers, sender/return-path mismatch, and
  sending-domain and URL reputation; on the host, a process-creation record
  (Security Event ID 4688 with the full command line, or Sysmon Event ID 1)
  showing an Office or archive process as the parent of a script interpreter —
  the ancestry is itself the detection.
- *Varies by actor:* commodity crimeware mails high volumes of macro documents or
  ISO+LNK bundles; targeted actors craft low-volume spearphishing (T1566.001
  attachment, T1566.002 link) tailored to a named recipient, increasingly using
  HTML smuggling to reconstruct the payload in the browser and evade gateway
  scanning.

**T1059 — Command and Scripting Interpreter (Execution).**
- *Procedure:* rather than dropping a compiled binary, the adversary runs commands
  through an interpreter already on the host — PowerShell (.001), the Windows
  command shell (.003), or a Unix shell (.004) — often an encoded or obfuscated
  one-liner that downloads and runs the next stage in memory.
- *Leaves behind:* PowerShell Script Block Logging records the deobfuscated script
  (Microsoft-Windows-PowerShell/Operational Event ID 4104; module logging adds
  4103); process-creation auditing (4688 / Sysmon 1) captures the command line,
  including the tell-tale `-enc`/`-EncodedCommand` and download cradles; on Linux,
  `auditd` `execve` records the invocation.
- *Varies by actor:* less capable actors paste heavily obfuscated encoded commands
  that script-block logging happily records in clear; more capable actors "live
  off the land," preferring signed LOLBins or in-memory .NET to minimise
  script-block and on-disk evidence — which is why process ancestry and network
  egress often detect them when the command text does not.

**T1053.005 — Scheduled Task (Persistence).**
- *Procedure:* to survive reboot and logoff, the adversary registers a scheduled
  task that re-launches the payload on a trigger (at logon, on a timer). This is
  the same mechanism F02 Lab 2 plants as a benign indicator — here analysed as the
  adversary's persistence choice.
- *Leaves behind:* Security Event ID 4698 (a scheduled task was created), the
  TaskScheduler/Operational log, an XML task definition under
  `C:\Windows\System32\Tasks\`, and an entry under the registry `TaskCache` key —
  multiple, correlatable artefacts.
- *Varies by actor:* some actors instead use a Registry Run key or Startup-folder
  entry (T1547.001), a new Windows service (System Event ID 7045), or a cron job /
  systemd timer on Linux (F02 Topic 2). Each choice trades stealth against
  reliability and writes to a different, baseline-able location.

**T1548 — Abuse Elevation Control Mechanism (Privilege Escalation).**
- *Procedure:* holding a standard-user token (F02 Topic 4), the adversary abuses a
  legitimate elevation path rather than a kernel exploit — bypassing User Account
  Control by hijacking an auto-elevating binary's registry handler (.002), or
  abusing `sudo`/sudo caching (.003) or a `setuid` binary (.001) on Linux — to
  obtain a high-integrity or root context.
- *Leaves behind:* on Windows, a high-integrity process whose parent is a
  medium-integrity user process, plus the registry write to the hijacked `HKCU`
  handler; on Linux, `auth.log`/`auditd` records of `sudo` invocation and `execve`
  of setuid binaries.
- *Varies by actor:* UAC-bypass techniques are tied to specific auto-elevate
  binaries and are swapped frequently as Microsoft closes them; Linux actors lean
  on misconfigured `sudoers` and world-writable setuid paths — F02 Topic 4's "how
  misconfiguration creates escalation paths," now seen from the attacker's side.

**T1003.001 — OS Credential Dumping: LSASS Memory (Credential Access).**
- *Procedure:* the adversary reads the memory of the LSASS process to extract
  cached credential material — NTLM hashes and Kerberos tickets — which can be
  replayed (pass-the-hash) or used to request service tickets, without cracking a
  password. This turns on the Windows identity substrate F02 teaches (LSASS, NTLM
  hash equivalence, Kerberos AS-REQ/TGS-REQ); OC01 analyses the *theft*, not the
  protocol.
- *Leaves behind:* a handle opened to `lsass.exe` with high access rights —
  Sysmon Event ID 10 (ProcessAccess) with GrantedAccess masks such as
  `0x1010`/`0x1410` is the classic signal; a SACL on `lsass` produces Security
  Events 4656/4663; a dropped minidump (e.g. `lsass.dmp`) is a file-creation
  artefact (Sysmon 11).
- *Varies by actor:* commodity intrusions run Mimikatz or `procdump` directly
  against LSASS; stealthier actors use the built-in `comsvcs.dll` MiniDump export
  or direct syscalls to avoid loading a flagged tool, and mature actors may skip
  LSASS for ticket-based theft — which is why detection anchors on *access to
  lsass* rather than any one tool name (Pyramid of Pain, Topic 4).

**T1021 — Remote Services (Lateral Movement).**
- *Procedure:* with harvested credentials, the adversary moves host-to-host over
  legitimate remote-access services — RDP (.001), SMB / Windows admin shares
  (.002), or WinRM (.006) — so the traffic blends with normal administration.
  F01's TCP port-state view (445, 3389, 5985) frames what is reachable.
- *Leaves behind:* an authentication event on the destination — Security Event
  4624 with logon type 10 (RemoteInteractive) for RDP or type 3 (Network) for
  SMB/WinRM, often paired with 4672 for privileged logons; SMB admin-share use
  adds 5140/5145; a PsExec-style push installs a transient service (System Event
  7045). The source→destination pairing across hosts is the signal.
- *Varies by actor:* hands-on-keyboard actors favour interactive RDP; automated
  tooling prefers SMB/PsExec or WMI/WinRM for scripted spread — the logon type
  recorded in Event 4624 is often what distinguishes them.

**T1071 — Application Layer Protocol (Command and Control).**
- *Procedure:* the implant beacons out to adversary infrastructure over an
  ordinary application protocol — HTTPS (.001) or DNS (.004) — so the channel
  survives egress filtering by looking like normal web or name-resolution traffic.
  F01's HTTP request anatomy, TLS SNI, and DNS query behaviour are exactly what is
  being imitated.
- *Leaves behind:* at the proxy/resolver, regular beaconing at a near-fixed
  interval (with jitter), a uniform or rare user-agent, a stable TLS/JA3
  fingerprint, or an unusual volume of long/encoded DNS subdomains (tunnelling).
  The periodicity, not the destination, is the durable signal.
- *Varies by actor:* framework-driven actors run HTTPS beacons with malleable
  profiles that mimic a named web service; lower-resourced actors use plain HTTP
  or DNS tunnelling; some blend into sanctioned SaaS to defeat domain reputation —
  which is why C2 detection is behavioural (beacon cadence) rather than
  indicator-based.

**Key concepts:**
- Every technique is a procedure that leaves telemetry: technique → artefact →
  detection opportunity
- The same technique varies between actors; durable detection targets the
  invariant behaviour, not the tool (links forward to the Pyramid of Pain, Topic 4)
- The catalogue builds on F01 (port state, HTTP/DNS, ARP) and F02 (process trees,
  tokens, scheduled tasks, the identity substrate) — attacks analysed, primitives
  not re-taught

**Australian context:** ACSC advisories describe these techniques in the wild
against Australian targets (credential theft and living-off-the-land tradecraft
recur across ransomware and state-actor advisories), and the ASD event-logging and
Windows-hardening guidance names the very telemetry — process creation, PowerShell
logging, scheduled-task auditing — this catalogue relies on. Analysing these
behaviours is lawful defensive study; executing them against a system without
authorisation engages Part 10.7 of the *Criminal Code Act 1995* (Cth), which is
why hands-on emulation is confined to the authorised environment taught in
F05/CE01.

---

### Topic 4: The Pyramid of Pain and Durable Detection

Not all indicators are equal. The Pyramid of Pain ranks indicators by how much
effort it costs an adversary to change them — hash values and IPs are trivial to
change; tools and TTPs are expensive. This topic explains why behaviour-based
detection (high on the pyramid) is more durable than atomic indicators, and why
threat-informed defense focuses effort there. It links directly to detection
engineering (OC02) and CTID's *Summiting the Pyramid* research on robust
analytics.

**Key concepts:**
- The Pyramid of Pain and indicator durability
- Why TTP-level detection survives adversary change
- CTID *Summiting the Pyramid* and analytic robustness

---

### Topic 5: CTID Tooling for a Living Defence

CTID produces open resources that operationalise TID. This topic surveys the most
useful: the **Adversary Emulation Library** (test plans modelled on real actors),
**ATT&CK Navigator** (visualising coverage and priorities), **Attack Flow**
(modelling sequences of techniques), **Sensor Mappings to ATT&CK** and **Mappings
Explorer** (what telemetry covers which techniques), **Top ATT&CK Techniques**
(prioritisation), and **M3TID** (measuring threat-informed-defense maturity).
Students learn what each is for and when to reach for it.

**Key concepts:**
- Adversary Emulation Library and Attack Flow
- Navigator and Mappings Explorer for coverage analysis
- M3TID for measuring and maturing TID

**Australian context:** These open tools let Australian organisations of any size
adopt threat-informed defense without commercial licensing.

---

### Topic 6: From Behaviour to Visibility — Closing the Loop

Threat-informed defense is only real if it changes what you can see and do. This
topic ties the unit together: given a set of prioritised techniques, determine
the data sources and telemetry needed to detect them, identify visibility gaps,
and feed those gaps back into logging, detection, infrastructure, and automation
changes. This is the feedback loop that makes defence a living organism — the core
idea the rest of the operational core builds on.

**Key concepts:**
- Technique → required data source → telemetry → detection
- Identifying and closing visibility gaps
- The continuous loop: behaviour change drives defensive change

**Australian context:** Connects to the ACSC's event-logging guidance — visibility
is the precondition for detecting prioritised techniques.

---

## Labs & Exercises

### Lab 1: Mapping an Intrusion to ATT&CK

**Objective:** Deconstruct a documented intrusion into its TTPs, map them to MITRE
ATT&CK, and represent the sequence as an Attack Flow.

**Prerequisites:**
- Topics 2, 3, and 4

**Environment:**
- Operating System: any (analysis lab)
- Tools: MITRE ATT&CK website, ATT&CK Navigator (free, runs locally or in
  browser), CTID Attack Flow Builder (free) — all free/OSS
- Minimum hardware: trivial; no GPU; within spec

**Instructions:**

1. Read the provided intrusion report (e.g. an ACSC advisory or a public incident
   write-up).
2. Extract each distinct adversary behaviour and assign the matching ATT&CK
   tactic and technique/sub-technique ID.
3. Build a layer in ATT&CK Navigator highlighting the techniques observed.
4. Construct an Attack Flow showing the order in which techniques were chained.
5. For three techniques, record the ATT&CK-listed data sources that would reveal
   them.
6. Note any technique you could *not* confidently map and explain the ambiguity.

**Expected Output:**

A Navigator layer and an Attack Flow for the intrusion, a TTP table with
technique IDs, and the data sources for three techniques. Learners can justify
each mapping against evidence in the report.

**Reflection Questions:**

1. Which techniques in this intrusion sat high on the Pyramid of Pain, and why
   would detecting them hurt the adversary most?
2. Where did the report leave behaviour ambiguous, and how would that ambiguity
   affect a real detection effort?
3. How would this Attack Flow change if the adversary swapped one tool for
   another? Which detections would survive?

---

### Lab 2: Threat-Informed Prioritisation with Navigator

**Objective:** Use threat-informed defense to prioritise which techniques a given
organisation should detect first, and identify its visibility gaps.

**Prerequisites:**
- Topics 1, 5, and 6 and Lab 1

**Environment:**
- Operating System: any
- Tools: ATT&CK Navigator, CTID Top ATT&CK Techniques and Sensor Mappings/
  Mappings Explorer (free), a spreadsheet
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario organisation (e.g. a mid-size Australian services firm,
   Windows/AD estate, cloud email).
2. Select two relevant threat profiles (e.g. an actor from an ACSC advisory plus
   a commodity ransomware pattern) and build a combined Navigator layer of their
   techniques.
3. Use CTID Top ATT&CK Techniques to rank the overlapping techniques by
   prioritisation signal.
4. Using Sensor Mappings / Mappings Explorer, list the telemetry/data sources
   needed to detect the top 10 techniques.
5. Compare against the organisation's assumed current logging (from F06/OC02
   knowledge) and mark each technique as Covered / Partial / Gap.
6. Recommend three concrete changes (a new log source, a detection, or an
   automation) to close the most important gaps.

**Expected Output:**

A prioritised technique list, a coverage map (Covered/Partial/Gap), and three
justified recommendations to close gaps. Learners can explain why their top
priorities reflect the organisation's real threat exposure.

**Reflection Questions:**

1. How did threat-informed prioritisation change what you would defend first
   compared with a generic "harden everything" approach?
2. Which visibility gap would you close first, and what telemetry change does it
   require?
3. How would you re-run this prioritisation in six months as the threat landscape
   shifts — and why is that recurring cycle the essence of threat-informed
   defense?

---

## Assessment

### Formative Assessment: ATT&CK Technique Identification

**Type:** Self-check exercise with answer key

**Description:** Students are given short behavioural descriptions ("the malware
created a scheduled task to re-launch at logon") and must assign the correct
ATT&CK tactic and technique ID. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3, LO7

**Feedback mechanism:** Answer key with the correct technique IDs and a note on
common mis-mappings.

---

### Summative Assessment: Threat-Informed Defense Brief

**Type:** Analytical report

**Description:** Given an Australian-relevant threat profile and a target
organisation, students produce a threat-informed defense brief that (a) maps the
actor's TTPs to ATT&CK with an Attack Flow, (b) prioritises techniques using a
defensible method, (c) analyses the organisation's visibility gaps against the
required data sources, and (d) recommends a prioritised set of detection,
logging, infrastructure, and automation changes — explicitly framed as an
adaptive loop. Deliverable: 2,000–2,500 word brief with Navigator/Attack Flow
artefacts.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6, LO7

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| TTP mapping + Attack Flow | LO1, LO2, LO7 |
| Technique prioritisation | LO3, LO4 |
| Visibility-gap analysis & recommendations | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| ATT&CK mapping accuracy | All TTPs correctly mapped with precise IDs and sequence | Mostly correct mapping with minor errors | Several mapping errors | Frequent misidentification |
| Threat-informed prioritisation | Insightful, well-justified, tied to real threat exposure | Sound prioritisation with valid rationale | Generic prioritisation, weak rationale | Unprioritised or unjustified |
| Visibility-gap analysis | Precise gap analysis tied to data sources; actionable recs | Solid analysis with adequate recs | Partial analysis; vague recs | Little meaningful analysis |
| Adaptive framing | Clearly frames defence as a continuous, adapting loop | Acknowledges adaptation adequately | Mentions adaptation superficially | Treats defence as static |
| Communication | Clear, structured, professional, evidence-linked | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories & Annual Cyber Threat Report:** Used as the source of
  Australian-relevant threat profiles for both labs and the summative brief.
- **ASD Essential Eight & ACSC event-logging guidance:** Connected to the
  visibility requirements for detecting prioritised techniques.
- **Open CTID tooling:** Emphasised as enabling Australian organisations of any
  size to adopt threat-informed defense without commercial licensing.

---

## Further Reading

**MITRE ATT&CK (v19, 2026).** *ATT&CK for Enterprise.* The MITRE Corporation. https://attack.mitre.org
> Relevance: The core knowledge base used throughout this unit; CC BY 4.0, freely usable.

**MITRE Center for Threat-Informed Defense (2024).** *Adversary Emulation Library, Attack Flow, Summiting the Pyramid, Top ATT&CK Techniques, M3TID.* CTID. https://ctid.mitre.org / https://github.com/center-for-threat-informed-defense
> Relevance: The open CTID research and tooling that operationalise threat-informed defense across this unit.

**Bianco, D. (2013).** *The Pyramid of Pain.* https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html
> Relevance: The foundational concept behind durable, behaviour-based detection in Topic 4.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report & threat advisories.* ACSC. https://www.cyber.gov.au/about-us/reports-and-statistics
> Relevance: The authoritative source on Australian-relevant adversary behaviour used in both labs (Australian source).

**Strom, B. et al. (2018/updated).** *MITRE ATT&CK: Design and Philosophy.* The MITRE Corporation. https://attack.mitre.org/resources/
> Relevance: Explains the structure and intent of ATT&CK, supporting correct, defensible mapping.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | OC01 |
| Unit Title | Adversary Tradecraft & TTPs |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Operational Core |
| Major / Pathway | Operational |
| Prerequisites | F01, F02, F04, F06 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | None directly (ACSC threat reporting / Essential Eight context) |
