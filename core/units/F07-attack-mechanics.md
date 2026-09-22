# F07: Attack Mechanics

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-09-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

The Foundation year so far has taught the *primitives* of attack in isolation:
F01 gives the learner TCP port-state and the anatomy of an HTTP request; F02
gives the Windows identity substrate and the Linux privilege model; F04 gives
the ATT&CK vocabulary and an economic picture of how initial access is bought
and sold. What no unit has yet done is *assemble* those primitives into a single
picture of how an intrusion actually works, end to end — and let the learner run
a technique with their own hands. That is the job of F07. It is the shared attack
spine that both degrees stand on: every defender is better for having walked, in
a controlled way, the path an attacker walks.

This unit is deliberately an *integration* unit, not a re-teaching unit. It
references the primitives rather than duplicating them, and it stays at
Foundation altitude: the learner describes and explains the mechanism of each
intrusion phase, and demonstrates or performs a small number of bounded
techniques against isolated, self-hosted targets they own. The deeper work —
analysing an adversary's tradecraft, evaluating a control's effectiveness,
building an attack chain from scratch — is explicitly the next layer's job and is
named as such throughout. In the Australian context the whole of F07 sits behind
the authorisation regime taught in F05: the same command is professional practice
inside a signed engagement and a Commonwealth offence outside one, and F07 is the
first unit where the learner actually runs the command, so that boundary is made
concrete rather than abstract.

---

## Prerequisites

- F01 — Networking Fundamentals (TCP port-state, HTTP anatomy, ARP/name resolution)
- F02 — Operating Systems & Administration (Linux privilege model, Windows identity substrate)
- F04 — Security Concepts & Principles (ATT&CK-as-vocabulary, threat/risk, the initial-access economy)
- F05 — Legal, Ethics & Australian Compliance (**load-bearing**: the authorisation regime that makes this unit lawful to practise)

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Describe** the phases of an intrusion as a chained ATT&CK tactic sequence and explain how each phase creates the preconditions for the next.
2. **Explain** how reconnaissance and initial-access techniques are built on the network and protocol primitives from F01 and the initial-access economy from F04.
3. **Demonstrate** a bounded reconnaissance-to-foothold chain against an isolated, self-hosted target using free tooling.
4. **Perform** a Linux privilege-escalation technique arising from a SUID or `sudo` misconfiguration on a learner-owned virtual machine.
5. **Explain** the identity-based attack paths that arise from the Windows authentication substrate covered in F02 — including why a Kerberos service ticket is offline-crackable — without reproducing them on proprietary infrastructure.
6. **Demonstrate** the two most common web-application attacks — SQL injection and cross-site scripting — against a deliberately vulnerable, self-hosted application built on the HTTP anatomy from F01.
7. **Identify** the defensive artefact each technique leaves behind and explain its value to a defender, deferring deeper detection and adversary analysis to the Operational Core.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of how
an intrusion is structured as a chained lifecycle and of the mechanics of the
most common techniques at each phase — reconnaissance, initial access, execution,
persistence, privilege escalation, and web-application attack — integrating the
networking, operating-system, and security-concept foundations laid earlier.

**Skills (AQF 7.2):** Students develop technical skills by performing bounded
offensive techniques in an isolated lab, and cognitive skills by explaining the
causal chain between phases and by pairing each technique with the artefact it
leaves for a defender.

**Application (AQF 7.3):** Students apply these skills only within self-hosted,
egress-blocked lab environments under the explicit authorisation model taught in
F05, mirroring the entitlement boundary that separates lawful professional
testing from a Criminal Code Act offence in Australia.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Exploitation Analyst | AN-EXP-001 | T0266 | Conduct authorised penetration testing on in-scope assets to identify exploitable conditions | Lab 1 — Recon-to-Foothold on an Isolated Target |
| NIST NICE DCWF | 2023 | Vulnerability Assessment Analyst | PR-VAM-001 | T0028 | Conduct and support authorised assessment of hosts and applications for exploitable weaknesses | Lab 2 — Linux Privilege Escalation; Lab 3 — Web Application Attacks |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0294 | Correlate activity across data sets to recognise the artefacts a technique produces | Assessment — Attack-and-Artefact Report |

> **Provisional mapping.** The work-role codes and T-code task statements above
> are the author's best reading and are **provisional pending Framework Custodian
> verification**. Consistent with the repo-wide framework-mapping audit, no T-code
> statement here should be treated as the official DCWF wording until verified.

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 3 | Lab 1, Lab 3 |
| Information security | SCTY | Level 2 | Throughout |

> SFIA code/level assignments are the author's reading and are **provisional**
> pending Framework Custodian review.

### ASD Cyber Skills Framework

> The ASD CSF domain/sub-domain names below are **provisional** pending Framework
> Custodian verification against the current framework; "Offensive Operations" and
> the sub-domain labels are the author's best mapping, not a verified one.

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Operations | Penetration Testing (foundational technique) | Foundational | Lab 1, Lab 2, Lab 3 |
| Technical Foundations | Attacker Tradecraft Awareness | Foundational | Topics 1–6 |

### MITRE ATT&CK

Techniques introduced at a foundational, mechanism-level depth in this unit. The
learner performs a bounded subset in the labs; the remainder are described so the
learner can recognise them.

| Technique | ID | Introduced In |
|---|---|---|
| Active Scanning | T1595 | Topic 2; Lab 1 |
| Exploit Public-Facing Application | T1190 | Topic 5; Lab 3 |
| Valid Accounts | T1078 | Topic 2; Lab 1 |
| Command and Scripting Interpreter | T1059 | Topic 3 |
| Scheduled Task/Job: Cron | T1053.003 | Topic 3 |
| Create or Modify System Process: Systemd Service | T1543.002 | Topic 3 |
| Boot or Logon Autostart Execution: Registry Run Keys | T1547.001 | Topic 3 |
| Abuse Elevation Control Mechanism: Setuid and Setgid | T1548.001 | Topic 4; Lab 2 |
| Abuse Elevation Control Mechanism: Sudo and Sudo Caching | T1548.003 | Topic 4; Lab 2 |
| Steal or Forge Kerberos Tickets: Kerberoasting | T1558.003 | Topic 4 (observe-the-artefact only) |
| OS Credential Dumping: LSASS Memory | T1003.001 | Topic 4 (observe-the-artefact only) |

> ATT&CK technique IDs are stated against **v19** for consistency with the rest of
> the repository. Both the version pin and these specific IDs are **provisional
> pending Framework Custodian verification.** The unit describes the ATT&CK tactic
> sequence by name (reconnaissance → resource development → initial access →
> execution → persistence → privilege escalation → defence evasion → credential
> access → discovery → lateral movement → collection → command and control →
> exfiltration → impact); the exact count of tactics in v19 is a Custodian item and
> is not relied upon in the content.

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F07-K01 | Knowledge of the intrusion lifecycle as a chained ATT&CK tactic sequence | Topic 1 |
| Knowledge | F07-K02 | Knowledge of reconnaissance and initial-access mechanics built on port-state, HTTP, and the initial-access economy | Topic 2; Lab 1 |
| Knowledge | F07-K03 | Knowledge of execution and host-persistence locations on Linux and Windows | Topic 3 |
| Knowledge | F07-K04 | Knowledge of Linux privilege-escalation paths and the identity-based attack paths on the Windows substrate | Topic 4; Lab 2 |
| Knowledge | F07-K05 | Knowledge of SQL injection and cross-site scripting as consequences of HTTP/trust-boundary handling | Topic 5; Lab 3 |
| Skill | F07-S01 | Skill in performing a bounded reconnaissance-to-foothold chain against an isolated target | Lab 1 |
| Skill | F07-S02 | Skill in performing a Linux SUID/sudo privilege escalation on a learner-owned VM | Lab 2 |
| Skill | F07-S03 | Skill in performing SQL injection and cross-site scripting against a self-hosted vulnerable app | Lab 3 |
| Ability | F07-A01 | Ability to pair each technique with the defensive artefact it leaves | Topic 6; Summative |
| Ability | F07-A02 | Ability to keep offensive activity within an authorised, isolated boundary | Labs 1–3; Safety section |
| Task | T0266 | Conduct authorised penetration testing to identify exploitable conditions | Lab 1 |
| Task | T0028 | Conduct and support authorised assessment of hosts and applications | Lab 2; Lab 3 |
| Task | T0294 | Correlate activity to recognise the artefacts a technique produces | Assessment |

---

## Topics

### Topic 1: The Intrusion as a Chained Lifecycle

An intrusion is not a single event; it is a *sequence* in which each phase creates
the preconditions for the next. F04 introduced ATT&CK as a vocabulary — a shared
set of names for adversary behaviour. This topic uses that vocabulary as a
*kill-sequence*: the attacker moves, in a recognisable order, from learning about
a target, through getting in, to running code, staying in, gaining power, moving
around, and finally acting on the objective. The value of thinking in a chain is
that it is also a *defender's* asset: a chain has links, and a link broken early
is cheaper to break than one broken late.

Reading the sequence at Foundation level means being able to name the tactics in
order and explain, for a given technique, which tactic it serves and what it makes
possible next. Reconnaissance yields the exposed services that initial access
exploits; initial access yields the foothold that execution runs code on;
execution yields the persistence that survives a reboot; persistence and
privilege escalation together yield the durable, powerful access that lateral
movement and collection depend on. The learner does not yet *analyse* an
adversary's choices across the chain — that is Operational Core work (OC01) — but
they can trace the causal thread.

**Key concepts:**
- The ATT&CK tactic sequence read as an ordered kill-sequence, not a checklist
- Preconditions: how each phase enables the next
- "Break the chain early": why defenders care about the order
- Techniques vs tactics vs procedures, revisited from F04

**Australian context:** The ACSC *Annual Cyber Threat Report* describes real
intrusions against Australian organisations in exactly these lifecycle terms;
reading one report through the ATT&CK sequence is the bridge from vocabulary to
narrative.

---

### Topic 2: Reconnaissance and Initial Access

Reconnaissance is the attacker learning what F01 taught the learner to see: which
hosts are up, which TCP/UDP ports are in which state, what service and version
answers on each, and what an HTTP response header or page discloses. This topic
builds directly on F01's port-state model and HTTP anatomy — a `SYN/ACK` is an
open port to the scanner exactly as it was to the learner in F01 — and reframes
that same knowledge from the attacker's side. It distinguishes passive
reconnaissance (public data, DNS, certificate transparency) from active scanning
(ATT&CK T1595), and explains why the noisy part is the active part.

Initial access is how the attacker turns knowledge into a foothold. F04 framed
initial access as a *commodity*: phishing kits, exploited public-facing
applications (T1190), and — very commonly — valid accounts (T1078) obtained from
credential markets rather than "hacked". This topic keeps that economic framing:
the cheapest reliable route in is usually a working username and password, not a
zero-day. The learner performs the technical half of this in Lab 1 against an
isolated target — enumerate, identify a weak or exposed service, and use a
discovered credential or documented weakness to obtain a shell — while
understanding that in the real economy the credential would more often be *bought*
than *found*.

**Key concepts:**
- Passive vs active reconnaissance; active scanning as T1595
- Mapping F01 port-state and service/version detection to an attacker's target picture
- Initial access as commodity: T1190 (exploit public-facing app) and T1078 (valid accounts)
- Why "valid accounts" is the quiet, common route in

**Australian context:** ACSC advisories repeatedly identify exploitation of
unpatched internet-facing services and use of stolen credentials as leading
initial-access vectors against Australian entities.

---

### Topic 3: Execution and Host Persistence

Once inside, the attacker must *run code* and then *survive*. Execution (ATT&CK
T1059, Command and Scripting Interpreter) is usually through the interpreters that
F02 taught the learner to administer with — `bash`, PowerShell, `cmd` — which is
precisely why "living off the land" is attractive: the tooling is already trusted
and present. This topic explains what runs, in whose context, and how it is
launched, connecting back to F02's process model (parent/child process trees are
both an attacker's cover and a defender's tell).

Persistence is where the attacker hides the ability to come back. This topic maps
the common locations to the F02 substrate the learner already knows: on Linux,
cron jobs (T1053.003) and systemd services/timers (T1543.002); on Windows,
scheduled tasks, services, and registry Run keys (T1547.001). The framing is "what
runs, where it hides" — every persistence mechanism is a legitimate OS feature
being repurposed, which is why persistence is discovered by *inventorying* those
features and noticing what does not belong (exactly the triage skill F02 built).

**Key concepts:**
- Execution via native interpreters (T1059); living-off-the-land rationale
- Process context and parent/child trees as cover and as tell
- Linux persistence: cron (T1053.003), systemd units (T1543.002)
- Windows persistence: scheduled tasks, services, Run keys (T1547.001)

**Australian context:** ASD *Essential Eight* application control and
restriction of administrative privileges directly constrain both execution and
persistence; this topic previews why those mitigations sit where they do.

---

### Topic 4: Privilege Escalation and the Identity Dimension

A foothold is rarely privileged enough. Privilege escalation is how the attacker
turns a low-privilege account into a powerful one, and it splits cleanly along the
F02 line between Linux and Windows.

On **Linux**, escalation is usually a *misconfiguration*, not an exploit: a SUID
binary that runs as root but can be coerced into running arbitrary commands
(ATT&CK T1548.001), or a `sudo` rule that permits a program which can shell out or
read arbitrary files (T1548.003). This is mechanically transparent and safe to
perform, and the learner does exactly that in Lab 2, building on F02's setuid and
`sudo` material. The reference corpus for "which trusted binary can be abused, and
how" is GTFOBins.

On **Windows**, the powerful attack paths are *identity* paths, built on the
substrate F02 introduced. This topic explains, conceptually, why they work: a
Kerberos service ticket (TGS) is encrypted with a key derived from the service
account's password, so an attacker who can request one (Kerberoasting, T1558.003)
can take it offline and brute-force the account password without touching the
domain again — *that* is why a weak service-account password is catastrophic. It
also explains why credentials cached in LSASS memory (T1003.001) are a prize, and
why NTLM's password-equivalent hashes enable pass-the-hash. Crucially, F07 keeps
all of this **observe-the-artefact**: the learner inspects pre-captured data or a
free Samba AD DC, and does *not* run ticket extraction or LSASS dumping, because a
the identity dimension is kept observe-the-artefact not because the request side
cannot be shown on free tooling (a Samba AD DC issues real service tickets, and an
offline crack of an exported ticket needs no Windows at all), but because the
high-impact paths that complete these attacks — LSASS memory dumping and true
DCSync replication — do need a live Windows DC and are out of F07's scope (see the
Safety section and Lab notes). Deeper exploitation of
these paths is CE/DFIR-major work; F07 gives the learner the mechanism and the
artefact only.

**Key concepts:**
- Linux privilege escalation: SUID/SGID abuse (T1548.001), `sudo` misconfiguration (T1548.003), GTFOBins
- Why a Kerberos service ticket is offline-crackable (Kerberoasting, T1558.003) — conceptual, tied to F02
- LSASS-resident credentials (T1003.001) and NTLM hash equivalence, conceptual
- Observe-the-artefact vs reproduce-the-technique, and why the free path stops where it does

**Australian context:** "Restrict administrative privileges" is an Essential
Eight mitigation precisely because privilege escalation is the pivot that turns a
minor foothold into a domain-wide incident.

---

### Topic 5: Web Application Attacks — Injection and Cross-Site Scripting

Across the degree, OC06 names web applications among the attack surfaces it
surveys, but this is the only unit that teaches the actual vulnerability classes —
SQL injection and cross-site scripting — as mechanism rather than naming the
category. This
topic is their only home, and it is placed here because it is a direct consequence
of F01's HTTP anatomy. Every web attack is a request the application trusted when
it should not have.

**SQL injection (SQLi)** occurs when user-supplied input is concatenated into a
database query instead of being passed as a bound parameter, so the input can
change the query's *structure* — turning a login check into "always true", or
adding a `UNION SELECT` that returns other tables' data. The learner performs both
an authentication bypass and a UNION-based data extraction in Lab 3. The
underlying defect is CWE-89, and it is A03:2021 (Injection) in the OWASP Top Ten.

**Cross-site scripting (XSS)** occurs when an application reflects or stores
user-supplied input into a page without encoding it, so the browser executes
attacker-supplied script in the victim's session. The learner triggers reflected
and stored XSS in Lab 3. The defect is CWE-79. Both attacks map, at the ATT&CK
level, to Exploit Public-Facing Application (T1190), but the precise taxonomy for
web defects is OWASP/CWE, and the topic uses those deliberately.

At Foundation altitude the learner demonstrates the mechanism and states the fix
in one line (parameterised queries for SQLi; contextual output encoding for XSS).
Systematic web-application testing methodology and exploitation depth are OWASP
WSTG / CE-major work and are named as the next step.

**Key concepts:**
- SQL injection: authentication bypass and UNION-based extraction (CWE-89, OWASP A03:2021)
- Cross-site scripting: reflected vs stored (CWE-79)
- Why both are trust-boundary failures rooted in F01's request/response model
- The one-line fixes: parameterised queries; contextual output encoding

**Australian context:** Web-facing services holding personal information sit
squarely under the *Privacy Act 1988* APP 11 (security of personal information)
taught in F05; a SQLi that dumps a customer table is the technical event behind a
Notifiable Data Breach.

---

### Topic 6: From Attack to Defence — Every Technique Leaves an Artefact

This topic closes F07 back to its defensive purpose, and it is what keeps the unit
defensive-first: for every technique in Topics 2–5, the learner names the
*artefact* it leaves and why a defender values it. Attacks are not magic; they
touch logs, files, memory, and the network, and each touch is evidence.

The pairing is concrete. Active scanning leaves connection attempts and unusual
port-touch patterns in network and host logs. Initial access via valid accounts
leaves authentication events — often a successful logon from an unusual source or
time. Execution leaves process-creation records (the parent/child anomaly of F02).
Persistence leaves a new cron entry, systemd unit, scheduled task, or Run key —
discoverable by the F02 inventory-and-triage skill. Linux privilege escalation
leaves `sudo` and audit records; the Kerberos and LSASS paths leave characteristic
ticket-request and process-access events. SQLi and XSS leave web-server request
logs and application errors. F07 stops at *identifying* these artefacts and
explaining their value; the *analysis* of them — building detections, correlating
across sources, hunting — is exactly the Operational Core's job (OC01 onwards) and
is named here as the next layer so the learner knows where the road goes.

**Key concepts:**
- Technique → artefact pairing for every technique in Topics 2–5
- Where artefacts live: network logs, auth logs, process-creation, file system, application logs
- Why "attacks leave evidence" is the foundation of detection
- The explicit hand-off: detection analysis and threat hunting are the next layer (OC01/DFIR/DE)

**Australian context:** The artefacts named here are the raw material for the
telemetry and monitoring expectations in the ACSC ISM and for the incident
reporting obligations under the SOCI Act introduced in F05.

---

## Labs & Exercises

All three labs run locally on free/open-source tooling within the project's
standard specification (8 GB RAM, 4-core CPU, 50 GB disk). All targets are
self-hosted and isolated. **Read the Safety, Authorisation & Isolation section
before any lab.** No cloud account, no commercial licence, and no target that the
learner does not own is used at any point.

---

### Lab 1: Recon-to-Foothold on an Isolated Target

**Objective:** Perform a bounded reconnaissance-to-foothold chain — enumerate an
isolated target, identify an exposed weakness, and obtain a shell — demonstrating
the initial phases of the intrusion lifecycle end to end.

**Prerequisites:**
- Topics 1 and 2; F01 (port-state, HTTP); F05 (authorisation)
- An isolated, **host-only** virtual network with egress verified blocked

**Environment:**
- Operating Systems: one analyst VM (Ubuntu 22.04 LTS or Kali Linux) and one
  deliberately vulnerable target VM (Metasploitable 2, a free/OSS target image)
- Tools: `nmap`, `whatweb`/`nikto`, `searchsploit`, `curl`, `ssh`, `netcat`,
  and (optionally) `hydra` — all free/OSS
- Minimum hardware: analyst VM 3 GB RAM / 2 vCPU / 20 GB; target VM 1 GB RAM /
  1 vCPU / 8 GB — total well within the 8 GB / 4-core / 50 GB spec; no GPU
- **Network:** both VMs on a host-only/internal network with no route to the
  internet or the host LAN; snapshot both before starting

**Instructions:**

1. Snapshot both VMs. Confirm isolation: from the target, verify that a ping to a
   public address and a DNS lookup both fail (egress blocked). Record the evidence.
2. From the analyst VM, run host discovery on the lab subnet
   (`nmap -sn <subnet>`), then a service/version scan of the target
   (`nmap -sV <target-ip>`). Record open ports, services, and versions.
3. Fingerprint any web service with `whatweb <target-ip>` and review one HTTP
   response with `curl -I`, relating each header back to F01's HTTP anatomy.
4. For the most promising service, search for documented weaknesses
   (`searchsploit <service> <version>`) and read the description — **do not run
   anything yet**. Note whether the weakness is a known vulnerability or simply a
   weak/default credential.
5. Obtain a foothold by the simplest documented route (for example, logging in to
   an exposed service with a weak or default credential you have identified).
   Confirm the shell with `id` and `hostname`.
6. Record the exact commands and outputs as an evidence trail, and state in one
   line which ATT&CK tactic each step served.
7. Revert both VMs to the pre-lab snapshot when finished.

**Expected Output:**

An evidence trail showing: verified egress isolation; an enumeration result
(ports, services, versions); a web fingerprint tied to an HTTP header; the
identified weakness; and a confirmed foothold shell (`id` output). The learner
labels each step with its ATT&CK tactic and states plainly that all activity
stayed within the isolated lab.

**Reflection Questions:**

1. Which of your enumeration steps were "active" (and therefore noisy), and what
   artefact would each leave for a defender? (Links forward to Topic 6.)
2. F04 framed initial access as a commodity. If this foothold were a *bought*
   valid credential rather than a found weakness, how would the evidence trail
   differ — and would it be easier or harder to detect?
3. Under the *Criminal Code Act 1995* (Cth), what single fact makes this exact
   activity lawful here and an offence against a target you do not own?

---

### Lab 2: Linux Privilege Escalation (SUID / sudo)

**Objective:** Perform a Linux privilege escalation arising from a SUID binary or
`sudo` misconfiguration on a learner-owned VM, demonstrating the mechanism rather
than reciting it.

**Prerequisites:**
- Topic 4; F02 (Linux permission/setuid and `sudo` model)
- A learner-owned Linux VM the learner may deliberately misconfigure

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM (learner-owned)
- Tools: native shell, `find`, `sudo`, `ls`; GTFOBins as a reference (free/OSS)
- Minimum hardware: 2 GB RAM / 1 vCPU / 15 GB — trivially within spec; no GPU
- Snapshot the VM before starting

**Instructions:**

1. Snapshot the VM. Create a low-privilege user and log in as that user.
2. As root, introduce **one** deliberate misconfiguration for the exercise — for
   example, set the SUID bit on a binary that can spawn a shell or read arbitrary
   files (`chmod u+s`), *or* add a `sudo` NOPASSWD rule permitting such a binary.
   Record exactly what you changed.
3. As the low-privilege user, enumerate escalation opportunities: find SUID
   binaries with `find / -perm -4000 -type f 2>/dev/null`, and check `sudo -l`.
4. Consult GTFOBins for the identified binary to find the documented abuse method.
5. Perform the escalation and confirm success with `id` (expect `uid=0(root)`).
6. Record the full command sequence and, in one line each, name the ATT&CK
   sub-technique (T1548.001 for SUID, T1548.003 for `sudo`) and the artefact the
   escalation left (audit/`sudo` log entry).
7. Revert the VM to the pre-lab snapshot.

**Expected Output:**

Evidence of the introduced misconfiguration, the enumeration output that revealed
it, the GTFOBins-documented abuse, and a confirmed root shell (`id` output),
together with the ATT&CK sub-technique label and the log artefact the action
produced.

**Reflection Questions:**

1. Your escalation abused a *legitimate* feature. What does that imply about
   detecting privilege escalation versus preventing it through configuration?
2. F02 taught "restrict administrative privileges" as an Essential Eight
   mitigation. Which specific misconfiguration in this lab would that mitigation
   have prevented?
3. This lab is safe to *perform*; the Windows Kerberoasting path in Topic 4 is
   only *observed*. Explain, in terms of the free-tooling constraint, why the unit
   draws that line.

---

### Lab 3: Web Application Attacks (SQLi and XSS)

**Objective:** Demonstrate SQL injection and cross-site scripting against a
deliberately vulnerable, self-hosted web application, connecting each attack to
the HTTP request/response model from F01 and to its one-line fix.

**Prerequisites:**
- Topic 5; F01 (HTTP anatomy)
- A self-hosted vulnerable application running locally

**Environment:**
- Operating System: any host capable of running Docker or a single VM
- Target: **OWASP Juice Shop** (Docker image) *or* **DVWA** — both free/OSS,
  designed to be attacked, and intended to run only on an isolated local host
- Tools: a web browser with developer tools, `curl`; optionally the free tier of
  an intercepting proxy (OWASP ZAP) — all free/OSS
- Minimum hardware: 2 GB RAM / 2 vCPU / 15 GB — within spec; no GPU
- **Network:** bind the target to `localhost` only; do not expose it on any
  network. Snapshot/checkpoint before starting

**Instructions:**

1. Start the vulnerable app bound to localhost and confirm it is not reachable
   from any other host on the network.
2. **SQL injection — authentication bypass:** in a login field, submit an input
   that closes the string and forces a true condition (e.g. `' OR 1=1 --`).
   Observe the bypass. Capture the request in developer tools and relate it to
   F01's HTTP anatomy.
3. **SQL injection — data extraction:** on a parameter reflected into a query,
   craft a `UNION SELECT` that returns data from another column/table. Record the
   payload and the extracted data (which is synthetic lab data only).
4. **Reflected XSS:** submit `<script>alert(document.domain)</script>` (or the
   app's documented equivalent) into a parameter reflected into the page; observe
   execution.
5. **Stored XSS:** submit a script payload into a field the app stores and later
   renders (e.g. a comment/review); reload and observe execution for any viewer.
6. For each of the four, write one line naming the defect (CWE-89 or CWE-79), the
   OWASP category, and the one-line fix (parameterised queries; contextual output
   encoding).
7. Tear down / revert when finished.

**Expected Output:**

Evidence of a working authentication bypass, a UNION-based extraction of synthetic
data, and both reflected and stored XSS, each captured with the request/response
and annotated with its CWE, OWASP category, and one-line remediation. All activity
confined to the localhost-bound target.

**Reflection Questions:**

1. Both SQLi and XSS are "the application trusted input it should not have."
   Explain that single sentence using your captured requests.
2. A stored XSS payload persists and runs for other users. Which security
   objective from F04 (confidentiality, integrity, availability, …) does that most
   directly violate, and why?
3. If this application held real customer data, which Australian obligation from
   F05 would a successful SQLi extraction most likely trigger?

---

## Assessment

### Formative Assessment: Chain-and-Artefact Quiz

**Type:** Self-check quiz with answer key

**Description:** A short quiz that (a) presents techniques and asks the learner to
place each in the correct ATT&CK tactic and state what it enables next, and (b)
pairs each technique with the artefact it leaves. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2, LO7

**Feedback mechanism:** Answer key with the correct tactic placement, the
enabling relationship, and the expected artefact for each item.

---

### Summative Assessment: Attack-and-Artefact Report

**Type:** Practical report

**Description:** Working only within the isolated lab, the student executes the
bounded chain from Lab 1 and one technique each from Lab 2 and Lab 3, then writes a
report that (a) narrates the activity as a chained ATT&CK sequence, (b) documents
each technique's mechanism with captured evidence, (c) for each technique, names
the defensive artefact it produced and explains its value to a defender, and (d)
states, for the whole exercise, the authorisation and isolation facts that made it
lawful under the *Criminal Code Act 1995* (Cth). All portfolio artefacts must be
sanitised (no real credentials, no target the learner does not own). The report
explicitly stops at *identifying* artefacts; deeper detection analysis is noted as
Operational Core work. Deliverable: 1,500–2,000 words with annotated evidence.

**Learning Outcomes Assessed:** LO1, LO3, LO4, LO5, LO6, LO7

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Narrate the activity as a chained ATT&CK sequence | LO1 |
| Execute and document the recon-to-foothold chain | LO3 |
| Execute and document a privilege-escalation and a web technique | LO4, LO6 |
| Pair each technique with its defensive artefact | LO7 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Technique execution & evidence | All techniques performed correctly with precise, reproducible evidence | Techniques performed with minor gaps in evidence | Some techniques incomplete or weakly evidenced | Techniques not demonstrated |
| Lifecycle narrative | Chain is accurate, correctly sequenced, and causally explained | Mostly accurate sequence with minor slips | Partial or loosely ordered narrative | No coherent chain |
| Attack-to-defence pairing | Every technique paired with the correct artefact and its defensive value | Most techniques correctly paired | Some pairings missing or incorrect | Little or no artefact reasoning |
| Authorisation & isolation | Boundary facts stated precisely and tied to the Criminal Code Act; artefacts sanitised | Boundary stated with minor gaps | Boundary asserted but vague | Boundary absent or artefacts unsanitised |

---

## Australian Context

This unit incorporates the following Australian context:

- **Criminal Code Act 1995 (Cth) sch 1 Pt 10.7:** The Commonwealth computer
  offences (the provisions inserted by the *Cybercrime Act 2001*) are the legal
  reason every technique in F07 is confined to isolated, learner-owned targets;
  s 476.2 makes entitlement the test of whether access is unauthorised, and
  ss 478.3/478.4 turn on *intent* when it comes to holding or supplying data or
  tooling. Woven through the Safety section and the summative assessment.
- **ASD Essential Eight & ACSC ISM:** Referenced to connect execution, persistence,
  and privilege-escalation techniques to the mitigations (application control,
  restricting administrative privileges, patching) that constrain them.
- **ACSC Annual Cyber Threat Report:** Used in Topic 1 to ground the intrusion
  lifecycle in real intrusions against Australian organisations.
- **Privacy Act 1988 (APP 11) & the Notifiable Data Breaches scheme:** Used in
  Topic 5 and Lab 3 reflections to connect a web-application data extraction to the
  Australian breach-notification consequence.

---

## Further Reading

**MITRE (2024).** *MITRE ATT&CK — Enterprise Matrix.* MITRE. https://attack.mitre.org
> Relevance: The canonical reference for the tactics and technique IDs used throughout this unit; students read techniques at the mechanism level (ATT&CK version pin is provisional — see the mapping note).

**OWASP Foundation (2021–2024).** *OWASP Top Ten, Web Security Testing Guide, and OWASP Juice Shop.* OWASP. https://owasp.org
> Relevance: The free/OSS basis for Topic 5 and Lab 3; the WSTG is named as the next-layer methodology for systematic web testing.

**GTFOBins project (ongoing).** *GTFOBins.* https://gtfobins.github.io
> Relevance: The freely available reference for the SUID/`sudo` abuse techniques the learner performs in Lab 2.

**Australian Cyber Security Centre (2024).** *Information Security Manual & Essential Eight Maturity Model.* ACSC. https://www.cyber.gov.au/ism
> Relevance: The Australian baseline connecting each attack phase to the mitigation that constrains it (Australian source).

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au/about-us/reports-and-statistics
> Relevance: Grounds the intrusion lifecycle of Topic 1 in real Australian intrusions and initial-access trends (Australian source).

**Australian Government (1995).** *Criminal Code Act 1995 (Cth) — Schedule 1, Part 10.7 (computer offences), incl. ss 476.2, 478.3, 478.4.* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The primary legislation defining the entitlement and intent boundaries that make this unit lawful to practise (Australian source).

**Stuttard, D. & Pinto, M. (2011).** *The Web Application Hacker's Handbook (2nd ed.).* Wiley.
> Relevance: A deeper reference for the web-application attacks introduced in Topic 5, for students who continue into the offensive major.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F07 |
| Unit Title | Attack Mechanics |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01, F02, F04, F05 |
| Offensive Content | Yes |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-09-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (provisional) |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) sch 1 Pt 10.7 (ss 476.2, 478.3, 478.4); Privacy Act 1988 (APP 11, NDB scheme) |

---

## Safety, Authorisation & Isolation

**Read this before any lab. F07 is the first unit in the degree where you run
offensive technique, so the boundary is not abstract — it is the difference
between coursework and a Commonwealth offence.**

Under the *Criminal Code Act 1995* (Cth) Schedule 1, Part 10.7, whether access to
or modification of a computer is *unauthorised* turns on **entitlement** (s 476.2):
you are entitled to do these things to systems you own or have written
authorisation to test, and to nothing else. "It was for a course" is not a
defence. Sections 478.3 and 478.4 further turn on **intent**: possessing,
producing, supplying, or obtaining data or tooling *with the intent* of committing
a computer offence is itself an offence — which is why this unit commits no
weaponised tooling to the repository and why your portfolio artefacts must be
sanitised.

**Rules for this unit:**

1. **Isolated, self-hosted targets only.** Every target in F07 is a virtual
   machine or container you own, running on a **host-only / internal** network.
   Your home, employer, or university network is **not** your lab, and neither is
   any host on it that you do not own.
2. **Verify egress is blocked.** Before attacking, confirm from the target that it
   cannot reach the internet (a failed ping and a failed DNS lookup). Record the
   evidence. Nothing you do should be able to leave the lab.
3. **Snapshot and revert.** Snapshot every VM before a lab and revert afterwards.
   The vulnerable targets (Metasploitable 2, DVWA, Juice Shop) are deliberately
   insecure and must never persist on a reachable network.
4. **Observe-the-artefact for identity attacks.** The Windows Kerberos and LSASS
   paths in Topic 4 are studied by inspecting pre-captured data or a free Samba AD
   DC — not reproduced. A faithful reproduction requires Windows Server evaluation
   media and tooling (and Sysmon for the richest telemetry) that are proprietary
   and outside the free-path constraint (R3); the unit states plainly what the
   free path cannot reproduce rather than pretending otherwise.
5. **No weaponised tooling committed; artefacts sanitised.** Do not commit exploit
   code, real credentials, keys, or live target details to any repository. Portfolio
   evidence uses synthetic lab data only.

This is the same authorisation boundary taught in
[F05](F05-legal-ethics-compliance.md) and developed in the offensive major; F07
simply makes it concrete by being the first place you cross from reading about a
technique to running one.