# F02: Operating Systems & Administration

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Operating systems are where security controls are configured, where attackers
gain and keep access, and where forensic evidence lives. This unit gives learners
working competency in administering both Linux and Windows: the file systems,
the process and service models, user and privilege management, logging
subsystems, and the hardening steps that turn a default install into a defensible
host. The emphasis is hands-on administration, because a defender who cannot
navigate a host cannot investigate one.

In the Australian context, host hardening maps directly to several of the ASD
*Essential Eight* mitigations (application control, restricting administrative
privileges, patching applications and operating systems) and to the host-based
controls in the ACSC *Information Security Manual*. F02 is a prerequisite for
F06 (Data & Log Analysis), OC03 (Malware Analysis), OC04 (Incident Response),
and the DFIR major, all of which assume the learner can confidently operate the
systems they are defending.

The unit also carries the degree's **identity substrate**. Windows authentication
— where the secret that proves an identity is actually held, how NTLM and
Kerberos carry a proof of knowledge across a network, and what each exchange
leaves behind in a log — is the mechanism that almost every later attack and
detection in the programme stands on. F02 teaches that mechanism as *protocol
and design property*, and names each well-known attack only as the consequence
that follows from it. Performing those attacks is CTE-major work (CE01–CE03)
under CE01's authorisation regime and the *Criminal Code Act 1995* (Cth) Part
10.7; no lab in this unit executes one.

---

## Prerequisites

- F01 — Networking Fundamentals (recommended concurrent or prior)

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Describe** the core architecture of modern operating systems: the kernel,
   processes, memory, file systems, and the user/kernel boundary.
2. **Demonstrate** administrative tasks on both Linux and Windows, including file
   system navigation, process and service management, and package/software
   management.
3. **Explain** the user, group, and privilege models of Linux and Windows,
   including how privilege escalation paths arise.
4. **Use** native logging and auditing subsystems (journald/syslog, Windows
   Event Log) to observe system activity.
5. **Implement** baseline host-hardening steps and map them to ASD Essential
   Eight mitigations.
6. **Identify** common indicators of a misconfigured or compromised host through
   inspection of accounts, services, scheduled tasks, and logs.
7. **Explain** how NTLM and Kerberos authenticate a principal on a Windows
   network — including why possession of an NT hash is operationally equivalent
   to possession of the password, and why a Kerberos service ticket can be
   attacked offline — as consequences of stated protocol design properties.
8. **Identify**, in host and directory authentication telemetry — Windows logon
   types, Kerberos ticket-request records, directory object-access records, and
   Linux `auditd` syscall records — the artefacts that distinguish routine
   authentication from credential and ticket abuse.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of
operating system architecture and administration across the two platform
families that dominate enterprise environments.

**Skills (AQF 7.2):** Students develop technical skills by performing
administrative and hardening tasks at the command line and through native
tooling, and cognitive skills by interpreting system state and logs.

**Application (AQF 7.3):** Students apply these skills to harden and inspect
hosts in a lab that mirrors enterprise administration, mapping their work to the
Essential Eight and ACSC ISM host controls.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | System Administrator | OM-ADM-001 | T0431 | Perform system administration on specialized cyber defense applications and systems | Lab 1 — Linux & Windows Administration |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0163 | Perform cyber defense trend analysis and reporting using host data | Lab 2 — Host Hardening & Inspection |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| IT infrastructure | ITOP | Level 3 | Lab 1 |
| Security administration | SCAD | Level 3 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Technical Foundations | Systems Administration | Foundational | Lab 1, Lab 2 |

### MITRE ATT&CK (v19)

> ATT&CK techniques are named in this unit **as consequences of protocol and
> operating-system design**, so that later units inherit a shared vocabulary.
> **No technique in this table is executed in an F02 lab**; execution is
> CTE-major work (CE01–CE03) under CE01's authorisation regime. Technique IDs
> are provisional pending Framework Custodian verification against the v19
> catalogue (see CLAUDE.md).

| Framework | Version | Technique | ID | Design property it follows from | Referenced In |
|---|---|---|---|---|---|
| MITRE ATT&CK | v19 | OS Credential Dumping: LSASS Memory | T1003.001 | LSASS holds reusable authenticators in process memory for the life of a session, because that is what single sign-on is | Topic 5 |
| MITRE ATT&CK | v19 | OS Credential Dumping: DCSync | T1003.006 | Replication is a delegable directory *right*, not an exploit | Topic 5; Topic 6 |
| MITRE ATT&CK | v19 | Use Alternate Authentication Material: Pass the Hash | T1550.002 | The input to the NTLM response function is the hash, not the password | Topic 5; Lab 3 |
| MITRE ATT&CK | v19 | Steal or Forge Kerberos Tickets: Kerberoasting | T1558.003 | A TGS-REP is encrypted with the long-term key of the account owning the SPN, and any authenticated principal may request one | Topic 5; Lab 3 |
| MITRE ATT&CK | v19 | System Binary Proxy Execution | T1218 | Signed vendor binaries are trusted by publisher, not by behaviour | Topic 1 |
| MITRE ATT&CK | v19 | Access Token Manipulation: Token Impersonation/Theft | T1134.001 | A Windows access check evaluates the token, not the account name | Topic 4 |
| MITRE ATT&CK | v19 | Abuse Elevation Control Mechanism: Setuid and Setgid | T1548.001 | `execve()` of a file with the setuid bit transitions the effective UID to the file owner | Topic 4; Lab 2 |
| MITRE ATT&CK | v19 | Abuse Elevation Control Mechanism: Sudo and Sudo Caching | T1548.003 | `sudo` delegates by rule; a permissive rule delegates everything the named program can reach | Topic 4; Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F02-K01 | Knowledge of operating-system architecture (kernel, processes, memory, file systems) | Topic 1 |
| Knowledge | F02-K02 | Knowledge of Linux and Windows administration and the user/group/privilege models | Topic 2; Topic 3; Topic 4 |
| Knowledge | F02-K03 | Knowledge of host logging/auditing subsystems and persistence locations | Topic 5; Topic 6 |
| Skill | F02-S01 | Skill in performing administrative tasks across Linux and Windows | Lab 1 |
| Skill | F02-S02 | Skill in inspecting a host for compromise indicators | Lab 2 |
| Ability | F02-A01 | Ability to apply baseline host hardening mapped to the Essential Eight | Lab 2; Summative |
| Ability | F02-A02 | Ability to distinguish benign from suspicious host state | Lab 2; Summative |
| Knowledge | F02-K04 | Knowledge of the Windows authentication substrate — LSASS-held authenticators, NTLM challenge-response, and the Kerberos AS/TGS exchanges — and the design properties that make credential and ticket abuse possible | Topic 5; Lab 3 |
| Knowledge | F02-K05 | Knowledge of the process/thread/handle model, execution provenance, executable loading (PE and ELF), and signed-binary (LOLBin) abuse | Topic 1 |
| Knowledge | F02-K06 | Knowledge of the authentication and directory records that evidence logon, Kerberos ticket issuance and object access (Windows 4624/4625/4768/4769/4662; Linux auditd syscall records) | Topic 6; Lab 3 |
| Skill | F02-S03 | Skill in reading a Kerberos exchange from the wire, the client ticket cache, and the resulting audit records | Lab 3 |
| Skill | F02-S04 | Skill in tracing a privilege transition — the Linux effective-UID change, the Windows service/token path — back to the configuration that enabled it | Topic 4; Lab 2 |
| Ability | F02-A03 | Ability to explain an attack as the consequence of a named protocol or OS design property rather than as a tool invocation | Topic 4; Topic 5; Summative |
| Task | T0431 | Perform system administration on specialized cyber defense systems | Lab 1 |
| Task | T0163 | Perform cyber defense trend analysis and reporting using host data | Lab 2 |

---

## Topics

### Topic 1: Operating System Architecture

Every OS mediates between hardware and applications. This topic covers the kernel
and its responsibilities (scheduling, memory management, device I/O), the
distinction between user mode and kernel mode, the process lifecycle, and how
system calls cross the boundary. Understanding this boundary is essential later:
much of malware tradecraft and EDR detection lives precisely at the user/kernel
interface.

**Key concepts:**
- Kernel vs user space and the system-call boundary
- The process lifecycle and process trees (parent/child relationships)
- Virtual memory and why memory artefacts matter forensically

---

### Topic 2: Linux Administration

Linux dominates servers, cloud workloads, and security tooling. This topic
covers the file system hierarchy, permissions (rwx, ownership, SUID/SGID),
package management (apt/dnf), the systemd service and unit model, and process
inspection. Learners gain fluency at the shell, which is the working environment
for most of the later operational units.

**Key concepts:**
- File system hierarchy standard and permission/ownership model
- systemd units, services, and timers
- Process inspection: `ps`, `top`, `/proc`, and signals

---

### Topic 3: Windows Administration

Windows dominates the corporate endpoint and identity estate. This topic covers
the NTFS permission model, the registry, services and scheduled tasks, and the
basics of Active Directory as an identity and policy backbone. It introduces
PowerShell as the administrative and automation surface (developed further in
F03). Active Directory misconfiguration is one of the most common enterprise
attack paths, so foundational AD literacy is essential.

**Key concepts:**
- NTFS permissions, the registry, services, and scheduled tasks
- Local vs domain accounts; introduction to Active Directory
- PowerShell as the primary Windows automation surface

**Australian context:** ACSC publishes specific hardening guidance for Microsoft
Windows and Active Directory; this topic primes students to apply it.

---

### Topic 4: Users, Groups, and Privilege

Both platforms implement least privilege through accounts, groups, and
privilege tokens — and both are routinely undermined by over-privileged
accounts. This topic compares the Linux model (users, groups, sudo) with the
Windows model (SIDs, groups, UAC, privileged groups such as Domain Admins), and
then works **one escalation path on each platform all the way down to the
mechanism**. The aim is that a learner can say what the kernel or the service
control manager actually does, not which tool to run.

**Linux: the UID triple and the `execve` transition.** A Linux process does not
have "a" user ID. It has a *real* UID (who you are), an *effective* UID (who the
kernel uses for permission checks), and a *saved set-user-ID* (what the effective
UID may be restored to). When a process calls `execve()` on a file whose **setuid
bit** is set, the kernel sets the new effective UID to the **owner of the file**.
That is the whole mechanism: `/usr/bin/passwd` is owned by root with the setuid
bit set, so an ordinary user running it briefly executes with effective UID 0,
which is how an unprivileged user edits `/etc/shadow`. All four IDs are visible
at once in the `Uid:` line of `/proc/<pid>/status`, and Lab 2 has the learner
read it. The design property, stated plainly: **a setuid-root program is a
root-privileged program whose arguments and environment are chosen by an
unprivileged caller.** Every setuid binary is therefore a promise that the
program validates everything it is handed — and any setuid binary that will write
to a caller-named path, execute a caller-named command, or hand back a shell is
not a vulnerability *in* the kernel but a delegation the administrator made
(T1548.001). Finding them is an inventory question: `find / -perm -4000 -type f`.

**Linux: what a sudo rule really delegates.** `sudo` is itself a setuid-root
program. It reads `/etc/sudoers` (and `/etc/sudoers.d/`), matches a rule of the
form *user host = (runas) command*, and if a rule matches it `execve`s the named
command with effective UID 0. The subtlety that catches administrators is that
the rule delegates **the named program's full capability**, not the
administrator's intention. A rule granting a text editor grants root file write,
because editors open shells and write arbitrary paths. A rule using a wildcard in
a path grants everything the wildcard can match. A rule granting an interpreter
grants root, unconditionally. `sudo -l` prints exactly what the current user has
been delegated and is the first command in any privilege review (T1548.003).

**Windows: the token is the subject.** A Windows access check does not evaluate
an account name; it evaluates the **access token** attached to the thread — a list
of SIDs (the user and every group), a list of privileges, and an integrity level.
Two consequences. First, UAC: when an administrator logs on, Windows mints *two*
tokens, a filtered one used by default and a full one used after elevation.
Microsoft is explicit that UAC is a convenience mechanism, not a security
boundary, and learners should not reason about it as one. Second, because the
token is the subject, **obtaining someone else's token is equivalent to becoming
them** for access-check purposes. A process holding `SeImpersonatePrivilege` may
adopt a token that a client hands it over a named pipe or RPC — and service
accounts hold that privilege by default, which is why "this code runs as a service
account" and "this code can become SYSTEM" are much closer together than the
account names suggest (T1134.001).

**Windows: the service-binary path.** The service control manager starts a
service by executing the path in the service's registry record, under the account
that record names — very often LocalSystem. Nothing in that sequence re-validates
who controls the file. So if a non-administrative principal can write to the
service binary, or to the directory containing it, or if the `ImagePath` is
**unquoted and contains spaces** so that `C:\Program Files\App\svc.exe` causes the
SCM to try `C:\Program.exe` first, then whatever that principal places there is
executed with a SYSTEM token at the next service start. The escalation is not an
exploit; it is the SCM doing exactly what it is designed to do with a path an
administrator did not lock down. The check is an ACL question — `icacls` on the
binary and on every directory along its path — and it is the reason service
inventories are reviewed for permissions, not just for whether the service is
needed. *ATT&CK groups this family under Hijack Execution Flow (T1574); the
specific sub-technique ID is pending Framework Custodian verification against v19
and is deliberately not asserted here.*

**Key concepts:**
- Linux real/effective/saved UIDs; the `execve` setuid transition; reading
  `/proc/<pid>/status`; `find / -perm -4000`
- Sudo rule grammar, and why a rule delegates the program's full capability
  rather than the administrator's intent; `sudo -l` as the review command
- Windows access tokens as the subject of every access check; the UAC split
  token, and why UAC is not a security boundary
- `SeImpersonatePrivilege` and why service accounts sit close to SYSTEM
- The SCM service-binary path: weak binary/directory ACLs and unquoted
  `ImagePath`; `icacls` as the review command

**Australian context:** "Restrict administrative privileges" is an Essential
Eight mitigation; this topic is its technical foundation. ASD's *Detecting and
Mitigating Active Directory Compromises* (2024) treats over-privileged accounts
and delegated rights as a primary compromise pathway, and the review commands
above are how that guidance is operationalised on a single host.

---

### Topic 5: The Windows Identity Substrate — Where Secrets Live, NTLM, and Kerberos

Topic 4 established that a Windows access check evaluates a token. This topic
asks the prior question: **what proves you are entitled to that token, where is
the thing that proves it, and what does the proof look like on the wire?** Almost
every credential attack the later units name is a direct consequence of the
answers. The unit teaches the protocol and the design property; it does not teach
how to run the attacks, which is CE-major work.

#### Where the secret actually lives

On a Windows host, authentication is performed by the **Local Security Authority
Subsystem Service**, `lsass.exe`. So that a user is not re-prompted for every
resource they touch, LSASS retains **authenticators** — material sufficient to
answer an authentication challenge — in its process memory for the life of each
logon session: the NT hash of the password, Kerberos tickets and their session
keys, and further derived material depending on the providers in use. This is not
a defect. It is what single sign-on *is*. A system that never retained anything
reusable would have to ask for the password again at every hop.

The consequence is exact, and it has the shape of Topic 1: **anyone who can open
a handle to `lsass.exe` with memory-read rights holds every session's
authenticators on that host** (T1003.001). The vulnerable object is a handle, and
so every mitigation is about handles. *LSA Protection* runs LSASS as a protected
process so the kernel refuses a read handle even to an ordinary administrator
process. *Credential Guard* moves the secrets into a virtualisation-isolated
process, so the handle, if obtained, no longer leads anywhere useful. At rest,
local account material lives in the **SAM** registry hive; domain account material
lives only in the directory database on a domain controller (`ntds.dit`) and never
on the workstation — which is why "can this host be made to reveal domain
secrets" is a different question from "can this host be made to reveal its own".

One fact about the NT hash carries the rest of the topic: it is the **MD4 digest
of the UTF-16LE password, with no salt and no iteration**. No salt means identical
passwords produce identical hashes across every account and every machine in the
estate. No iteration means guessing is fast.

#### NTLM: challenge-response, and why the hash *is* the password

NTLM authenticates in three messages:

1. **NEGOTIATE** — client to server, announcing capabilities.
2. **CHALLENGE** — server to client, carrying an 8-byte server nonce.
3. **AUTHENTICATE** — client to server, carrying a *response* computed over the
   challenge, keyed by material derived from the user's **NT hash**. (In NTLMv2
   the response is an HMAC keyed by a value that is itself an HMAC of the NT
   hash, over the challenge, a client challenge and a target-information blob.
   The keying material is still the NT hash.)

The server, or the domain controller acting for it over Netlogon, computes the
same function and compares. Read the third message again and the central fact of
this unit falls out: **the password never crosses the wire, and nothing in the
protocol ever needs the password — only the hash.** Therefore *possession of the
NT hash is operationally equivalent to possession of the password for the purpose
of authenticating.*

That single property is the entirety of pass-the-hash (T1550.002). There is no
cracking step, no exploit, and nothing malformed on the wire. The attacker
supplies a hash they stole where the client would have supplied a hash derived
from a typed password, and the protocol succeeds exactly as designed. A learner
who holds this property can derive the defensive consequences without being told
them:

- **Rotation is the actual remedy.** Changing the password invalidates the stolen
  material; nothing else does.
- **Shared local passwords multiply.** If the local Administrator account has the
  same password on 500 machines, it has the same hash on 500 machines, and one
  compromise is 500 compromises. Per-machine unique local passwords (the LAPS
  pattern) exist to break exactly this.
- **Relay is the same property viewed sideways.** NTLM by itself does not bind an
  exchange to the service the client intended to reach, so without signing or
  channel-binding protections an attacker in the path can relay a client's
  authentication to a *different* service and be accepted.

#### Kerberos: tickets, SPNs, and the key that encrypts them

Kerberos involves three parties: the client, the **KDC** (running on every domain
controller, comprising an Authentication Service and a Ticket-Granting Service),
and the target service. Every principal — user, computer, service account —
shares a **long-term key** with the KDC, derived from its password.

**AS-REQ / AS-REP — getting a ticket-granting ticket.** The client asks the AS
for a TGT. With pre-authentication enabled it proves it knows its long-term key
by including a timestamp encrypted with that key; the KDC decrypts it and checks
the clock skew. The AS-REP comes back with two encrypted parts:

- the **TGT** itself, encrypted with the **`krbtgt` account's key** — the client
  cannot read this and is not meant to; it simply carries it; and
- a copy of the **session key**, encrypted with the **client's own long-term
  key**, which the client *can* read.

Two design consequences. If pre-authentication is *disabled* on an account,
anyone may request an AS-REP for it and receive material encrypted under that
account's password-derived key — attackable offline, with no credentials required
to ask. And because online password guessing is evaluated at the KDC, guessing
leaves its evidence there rather than on the target host.

**TGS-REQ / TGS-REP — getting a service ticket.** To reach a service the client
presents its TGT to the TGS together with the **SPN** of the target. A *service
principal name* has the form `service/host:port` — for example
`MSSQLSvc/db01.corp.example:1433` — and it is an **attribute on the account the
service runs as**. The SPN is how the KDC answers the only question it needs to
answer: *which key do I encrypt this ticket with?* The TGS returns a **service
ticket encrypted with the long-term key of the account that owns the SPN**, plus
a service session key for the client.

**Presentation.** The client sends the service ticket to the service in an
AP-REQ. The service decrypts it with its own key. **The service does not contact
the KDC.** That is the design's great virtue — it scales, and it survives a KDC
being momentarily unreachable — and it is also the property everything else hangs
on: the ticket can be validated offline by anything holding the key, which means
it can also be *attacked* offline by anything holding the ciphertext.

**Kerberoasting follows in one step** (T1558.003). Any authenticated domain
principal may request a service ticket for any SPN — again, not a bug: that is
precisely how a client with a TGT reaches a service, and the KDC has no basis to
refuse. Now apply the key question. If the SPN sits on a **computer account** or a
group Managed Service Account, the long-term key derives from a machine-managed
password of around 120 characters, rotated automatically, and offline attack is
futile. If the SPN sits on an ordinary **user account**, the key derives from a
human-chosen password — and the requester walks away holding ciphertext they can
attack at their leisure, with no further traffic to the domain and nothing for the
domain to observe after the request. The lever that decides how cheap that attack
is, is the **encryption type**: a ticket issued under RC4-HMAC is markedly cheaper
to attack than one issued under AES. So the mitigation is not "stop ticket
requests" — it cannot be. It is: minimise user accounts carrying SPNs, move those
that must exist to gMSAs, and disable RC4. This is exactly the guidance ASD gives
in *Detecting and Mitigating Active Directory Compromises*.

**One more right worth naming.** Directory replication is a delegable *right*, not
an exploit: a principal granted the replication extended rights can ask a domain
controller to replicate secrets to it and receive them through the normal
replication interface (T1003.006). The defence is the same shape as everything
else in this topic — audit who holds the right, and audit its use, which Topic 6
picks up as event 4662.

> **Scope and authorisation.** This topic teaches the exchanges, the artefacts
> and the design properties. Requesting service tickets in bulk, extracting
> ticket material, cracking it, or replaying a hash against a host is **not**
> performed anywhere in F02. That work belongs to the CTE major (CE01–CE03) and
> is governed by CE01's authorisation regime; conducting it against a system you
> are not authorised to test is an offence under the *Criminal Code Act 1995*
> (Cth) Part 10.7.

**Key concepts:**
- LSASS holds reusable authenticators because single sign-on requires it; the
  attack surface is a *handle*, and LSA Protection and Credential Guard are
  handle-shaped mitigations
- SAM (local) vs `ntds.dit` (domain) as the at-rest stores
- The NT hash: unsalted, uniterated MD4 of the UTF-16LE password
- NTLM NEGOTIATE / CHALLENGE / AUTHENTICATE; the response is keyed by the hash,
  so the hash is equivalent to the password for authentication
- Consequences of hash equivalence: rotation as the real remedy, shared local
  passwords as a multiplier, and relay as the unbound-exchange case
- Kerberos AS-REQ/AS-REP: pre-authentication, the TGT encrypted to `krbtgt`, the
  session key encrypted to the client
- Kerberos TGS-REQ/TGS-REP: the SPN as the account attribute that selects the
  key; the service ticket encrypted with the service account's long-term key
- Why the service never contacts the KDC, and why offline validation implies
  offline attackability
- Kerberoasting as the consequence: user-account SPNs vs gMSAs, and encryption
  type as the cost lever
- Replication as a delegable right (the DCSync shape)

**Australian context:** ASD's *Detecting and Mitigating Active Directory
Compromises* (first published September 2024) is the Australian reference for
this topic. It describes the SPN/TGS mechanism in the same terms used here,
names event 4769 as the record generated per service-ticket request, and gives
the gMSA migration as the mitigation. Learners should read the mechanism in this
topic and the mitigation in that publication together.

---

### Topic 6: System Logging and Auditing

A host that is not logged cannot be investigated. This topic covers Linux logging
(syslog, journald, auditd) and Windows logging (the Event Log, with Sysmon as an
optional augmentation), what each captures by default, and how to enable richer
auditing. It is the host-side companion to F06's log analysis — and it is where
the learner meets the specific records that evidence Topics 1, 4 and 5. An
attack the learner can explain but cannot *see* is not yet teachable as
detection.

**Windows: the records that matter, and where they live.**

- **4624 — successful logon.** The field that carries the meaning is the **logon
  type**, which says *how* the session was established: `2` interactive (at the
  console), `3` network (SMB and most remote resource access — the type that
  carries NTLM and Kerberos across the wire), `4` batch, `5` service, `7`
  unlock, `8` network cleartext, `9` new credentials (`runas /netonly`), `10`
  RemoteInteractive (RDP), `11` CachedInteractive (cached domain credentials).
  The record also names the **authentication package**, so "was this session
  authenticated by NTLM or by Kerberos" is answerable from 4624 alone — which
  makes NTLM usage inventoriable, and therefore reducible.
- **4625 — failed logon**, carrying a status and sub-status that give the
  *reason*: wrong password, disabled account, no such user, outside permitted
  hours. The distribution is the signal. Many 4625s across many accounts from one
  source with the same sub-status is a spray; many against one account is a brute
  force. Learners must also reason about **which host's log should hold the
  record**, because that depends on where the logon was attempted and which
  authority evaluated it.
- **4768 — a Kerberos TGT was requested** and **4769 — a Kerberos service ticket
  was requested**, with **4771** for pre-authentication failure. These are
  produced on the **domain controller**, not on the workstation, which is a
  collection fact before it is an analysis fact. The 4769 record carries the
  **service name** (the account owning the SPN) and the **ticket encryption
  type**; a burst of 4769 events with encryption type `0x17` (RC4-HMAC) naming
  many distinct SPNs, from one account, in a short window, is the Kerberoasting
  signature that Topic 5's mechanism predicts. Note that the signature is a
  *distribution over ordinary events* — every individual 4769 is normal.
- **4662 — an operation was performed on an object.** This is directory-service
  object access; it names the object and the properties or extended rights
  involved **by GUID**. It appears only where directory-service auditing and the
  relevant SACLs are configured, and it is the record on which replication-right
  abuse detection rests.
- **4688 — a process was created.** With the *Include command line in process
  creation events* policy enabled, 4688 carries the command line and the creator
  process — the native, no-extra-software source for the provenance reasoning of
  Topic 1.

A caution the learner should carry into the detection units: **these records
exist on the host but may not reach the collector.** ASD's own event-logging and
forwarding guidance is candid that Kerberos logon events are frequently dropped
at the subscription for volume — the point developed at length in the repository's
SA-05 logging-architecture module. A sound design documents its blind spots and
where the un-forwarded data still resides.

**Linux: `auditd`, and the identity that survives `sudo`.** The kernel audit
subsystem records at the **syscall** level, which is a different and complementary
kind of evidence. Rules are either syscall rules or watches:

```
-a always,exit -F arch=b64 -S execve -k exec-trace
-w /etc/sudoers.d/ -p wa -k sudoers-change
```

Every rule carries a key (`-k`), and `ausearch -k exec-trace` retrieves its
records. Because the recorder sits at the syscall boundary, an `execve` record
carries the argv **and** the `uid`, `euid` and `auid` at the moment of the call —
which is precisely the effective-UID transition taught in Topic 4, made visible.
The `auid` (login UID) is the identity established when the session began and is
not changed by a subsequent `su` or `sudo`, which is what makes "which human did
this" answerable across a privilege change. Alongside it, journald and
`/var/log/auth.log` record the sudo invocation itself, including the rule that
matched.

**The honest comparison.** Windows has rich, typed, high-level events but no
native syscall recorder; Linux has a syscall recorder but no native notion of a
"logon type". The tool that usually fills the Windows gap, **Sysmon, is free of
charge but proprietary** Microsoft Sysinternals software — it is not open source,
and under R3 it can never be the only path in this degree. Where a fully
open-source path is required: native **4688 with command-line auditing** covers
process creation with parentage, and the Windows Event Log covers authentication.
But the cross-process **handle-access** telemetry — the record of one process
opening `lsass.exe` with read rights, which Topics 1 and 5 identify as the single
highest-value Windows signal — has **no native equivalent**. That is a genuine
gap in the free path, and this unit states it rather than papering over it.

**Key concepts:**
- journald/syslog vs Windows Event Log: structure and default coverage
- 4624 logon types (2/3/4/5/7/8/9/10/11) and the authentication package field
- 4625 status/sub-status, and reasoning about which host holds the record
- 4768/4769/4771 on the domain controller; service name and ticket encryption
  type as the Kerberoasting levers; the signature as a distribution, not an event
- 4662 as directory object access, and why it depends on SACL configuration
- 4688 with command-line auditing as the native process-provenance source
- `auditd` syscall rules, watches, keys, `ausearch`; `uid`/`euid`/`auid` and why
  `auid` attributes an action to a human across a privilege change
- Collection reality: forwarded ≠ generated; documenting blind spots
- Sysmon is free of charge but proprietary; the native-only path and its one
  irreducible gap

**Australian context:** ASD/ACSC event-logging and forwarding guidance and the
ACSC ISM set the Australian expectations for what is generated, forwarded and
retained; the Essential Eight's monitoring expectations are what these records
serve.

---

### Topic 7: Host Hardening and Compromise Indicators

This topic brings the unit together: applying baseline hardening (patching,
disabling unnecessary services, enforcing least privilege, configuring logging)
and then inspecting a host for signs of trouble — unexpected accounts, unusual
services or scheduled tasks, suspicious autoruns, and anomalous logs. It maps
each hardening action to an Essential Eight mitigation.

**Key concepts:**
- A baseline hardening checklist mapped to the Essential Eight
- Persistence locations attackers favour (services, tasks, autoruns, cron)
- Triage inspection: accounts, listening ports, scheduled tasks, logs

**Australian context:** Directly operationalises the patching, application
control, and privilege-restriction mitigations of the Essential Eight.

---

## Labs & Exercises

### Lab 1: Linux & Windows Administration

**Objective:** Perform equivalent administrative tasks on both Linux and Windows
to demonstrate cross-platform competency.

**Prerequisites:**
- Topics 1–3
- Two local VMs: Ubuntu 22.04 LTS and Windows 10/11 (evaluation edition)

**Environment:**
- Operating Systems: Ubuntu 22.04 LTS and Windows 10/11 evaluation VMs
- Tools: native shells (bash, PowerShell); all built-in/free
- Minimum hardware: run one VM at a time — 4 GB RAM / 2 vCPU / 25 GB disk per VM
  (within the 8 GB / 4-core / 50 GB spec; no GPU)

**Instructions:**

1. **(Linux)** Create a non-privileged user, add it to a group, and grant it a
   single sudo command via `/etc/sudoers.d/`. Verify with `sudo -l` as that user.
2. **(Linux)** List running services with `systemctl list-units --type=service`;
   identify one non-essential service and disable it with `systemctl disable --now`.
3. **(Linux)** Inspect a running process tree with `ps -ef --forest` and record a
   parent/child relationship.
4. **(Windows)** Create a standard (non-admin) local user via `Settings` or
   `net user`; confirm it is not in the Administrators group with
   `net localgroup Administrators`.
5. **(Windows)** List services with `Get-Service` and scheduled tasks with
   `Get-ScheduledTask`; identify one of each and describe its purpose.
6. **(Windows)** Use `Get-Process` and inspect the parent of a process with a
   short PowerShell snippet; record a parent/child relationship.

**Expected Output:**

Evidence (command output/screenshots) of: a new least-privilege Linux user with
a scoped sudo right; a disabled non-essential Linux service; a process tree
relationship on each OS; and a new non-admin Windows user. Learners should be
able to explain why each account was created without admin rights.

**Reflection Questions:**

1. How does the Linux sudo model compare with Windows UAC for enforcing least
   privilege?
2. Which Essential Eight mitigation does creating non-admin users support, and
   why?
3. Where would an attacker most likely try to establish persistence on each OS?

---

### Lab 2: Host Hardening & Inspection

**Objective:** Apply a baseline hardening checklist to a host, then inspect it
for compromise indicators, mapping each action to an Essential Eight mitigation.

**Prerequisites:**
- Topics 4, 6 and 7, and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS *or* Windows 10/11 VM (learner chooses one
  to harden, then inspects the other)
- Tools (Linux — fully free/OSS): native tooling plus `auditd`, `auditctl`,
  `ausearch`, and a C compiler (`build-essential`) for step 4
- Tools (Windows): native tooling plus Windows Advanced Audit Policy — in
  particular **Event ID 4688 with "Include command line in process creation
  events" enabled**, which is the built-in, open-path process-creation record.
  **Sysmon is free of charge but proprietary** (Microsoft Sysinternals; not open
  source), so under R3 it is optional enrichment and never the only path.
  **Windows 10/11 evaluation media is likewise free of charge but proprietary
  and time-limited**; a learner who cannot or will not run it may complete this
  lab entirely on Linux and obtain the Windows-side artefacts from the
  pre-captured EVTX used in Lab 3.
- Minimum hardware: as Lab 1

**Instructions:**

1. Produce a baseline state snapshot: listening ports (`ss -tlnp` / `netstat
   -ano`), local accounts, services, and scheduled tasks/cron jobs.
2. Apply at least four hardening actions and map each to an Essential Eight
   mitigation — e.g. apply pending updates (patch OS), remove an unneeded
   account (restrict privileges), disable an unused service, enable richer
   logging (auditd on Linux; Advanced Audit Policy with 4688 command-line
   auditing on Windows).
3. Re-snapshot and diff against the baseline; record what changed.
4. **(Linux — observe the effective-UID transition.)** Write a short C program
   that prints `getuid()` and `geteuid()`, then sleeps for 30 seconds. Compile
   it, `chown root:root` the binary and set the setuid bit (`chmod u+s`). Run it
   **as your unprivileged user**, and while it sleeps, read the `Uid:` line of
   `/proc/<pid>/status` from a second shell. Record all four values (real,
   effective, saved-set, filesystem) and state in one sentence which one the
   kernel uses for permission checks and why it changed. Then inventory the
   host's existing setuid binaries with `find / -perm -4000 -type f 2>/dev/null`
   and pick one, explaining what capability the administrator delegated by
   setting that bit.
5. **(Linux — read a sudo rule as a delegation.)** Add a `/etc/sudoers.d/` rule
   granting your unprivileged user one command that can write an arbitrary file
   or launch a subprocess (an editor, or `find` with `-exec`). Run `sudo -l` as
   that user and record exactly what is delegated. **Without exploiting it**,
   write one paragraph explaining why this rule delegates root file-write or
   root command execution rather than the narrow capability its author intended.
   Replace it with a rule that does not, and confirm the change with `sudo -l`.
6. **(Linux — evidence the transition.)** Load the audit rules
   `-a always,exit -F arch=b64 -S execve -k exec-trace` and
   `-w /etc/sudoers.d/ -p wa -k sudoers-change`, repeat steps 4 and 5, and
   retrieve the records with `ausearch -k`. In the `execve` record, identify the
   `uid`, `euid` and `auid` fields, and state which of them attributes the action
   to a human and why it is the one that survives a privilege change.
7. Introduce a benign "indicator" (e.g. a scheduled task that runs `whoami`
   hourly) to simulate persistence.
8. Hunt for the indicator using only inspection commands — list scheduled
   tasks/cron, check recently created accounts, and review logs for its creation.
9. Document how you found it and what log entry recorded its creation. If you
   hardened the Windows host, cite the 4688 record and its command line; if
   Linux, cite the `auditd` record and its key.

**Expected Output:**

A before/after hardening diff with each action mapped to an Essential Eight
mitigation, and a short writeup showing the planted persistence indicator was
located through inspection, citing the specific log event that recorded it.

**Reflection Questions:**

1. Which of your hardening actions would have the greatest impact on an
   attacker, and why?
2. Why is logging itself a hardening control rather than just a monitoring one?
3. How does the ACSC's Windows/Linux hardening guidance compare with the
   baseline you applied?

---

### Lab 3: Observing the Kerberos Exchange and Its Artefacts

**Objective:** Observe one complete Kerberos authentication end to end — on the
wire, in the client's ticket cache, and in the resulting audit records — and
explain, **from the evidence you collected rather than from memory**, why a
service ticket for a user-account SPN can be attacked offline. No attack is
performed and no ticket material is extracted or cracked.

> **Authorisation.** Every action in this lab occurs inside a domain you
> provision yourself, on virtual machines you own. Requesting tickets, capturing
> authentication traffic, or enumerating SPNs in a domain you do not own or
> administer is unauthorised access under the *Criminal Code Act 1995* (Cth)
> Part 10.7. CE01 sets out the authorisation regime for work of that kind; this
> unit does not conduct it.

**Prerequisites:**
- Topics 1, 4, 5 and 6, and Lab 1
- F01 (packet capture and filtering)

**Environment (primary path — fully free/OSS):**
- **VM A — domain controller:** Ubuntu 22.04 LTS or Debian 12 running **Samba 4
  as an Active Directory DC** (`samba-ad-dc`, provisioned with `samba-tool domain
  provision`). 1.5 GB RAM / 1 vCPU / 12 GB disk.
- **VM B — client:** Ubuntu 22.04 LTS with `krb5-user` (MIT `kinit`, `klist`,
  `kvno`), `ldap-utils`, `smbclient` and Wireshark. 2 GB RAM / 1 vCPU / 15 GB
  disk.
- **Both VMs running together: ~3.5 GB RAM, 2 vCPU, ~27 GB disk** — inside the
  8 GB / 4-core / 50 GB specification, with headroom.
- **Pre-captured Windows artefacts:** an openly published EVTX sample set
  containing 4624, 4625, 4768, 4769 and 4662 records (for example the OTRF
  *Security-Datasets* project or a comparable open corpus), read with a free EVTX
  parser such as `python-evtx` or `evtx_dump`. **Check the corpus licence before
  redistributing it with course materials** — licensing on some public EVTX
  collections is disputed. No Windows licence is required to *read* EVTX data.
- **Reduced-setup variant (recommended where time is tight):** run steps 1–2 from
  a supplied provisioning script (cloud-init or Vagrantfile) rather than by hand,
  or use a supplied Kerberos pcap and skip VM A entirely, completing steps 3–10
  on a single VM. This removes roughly three hours of setup without losing any
  learning outcome.

**Instructions:**

1. Provision the DC on VM A: `samba-tool domain provision` with a lab realm
   (e.g. `LAB.INTERNAL`) and the DC server role. Point VM B's resolver and
   `/etc/krb5.conf` at it, and confirm time synchronisation between the two VMs
   — Kerberos will refuse a skewed client, which is itself a design property
   worth noting.
2. Create two accounts with `samba-tool user create`: `alice`, an ordinary user,
   and `svc_db`, standing in for a service account. Register a service principal
   name on the **user** account `svc_db` — e.g.
   `MSSQLSvc/db01.lab.internal:1433` — using `samba-tool spn add`. Write down in
   one sentence what you have just created: an attribute on a *user* object that
   tells the KDC which key to encrypt a ticket with.
3. On VM B, start a Wireshark capture filtered to Kerberos (TCP/UDP port 88).
   Obtain a TGT with `kinit alice`. Stop the capture and locate the **AS-REQ**
   and **AS-REP**. In the AS-REQ, find the pre-authentication data. In the
   AS-REP, find the two encrypted parts, and state from the packet which one the
   client can decrypt and which one it cannot — and why it carries the one it
   cannot.
4. Run `klist`. Record the `krbtgt/...` principal, the validity window and the
   ticket flags. Run `klist -e` and record the encryption type.
5. Request a service ticket **without ever contacting the service**:
   `kvno MSSQLSvc/db01.lab.internal:1433`. Re-run `klist` — a second ticket is
   now cached. In a fresh capture, identify the **TGS-REQ** and **TGS-REP**, and
   note that the TGT is *presented* inside the TGS-REQ.
6. Answer these from your evidence, not from the topic notes: which key encrypts
   the service ticket you just obtained; which party can decrypt it; and whether
   the KDC was contacted at the moment a ticket would be presented to a service.
   Then explain in two or three sentences why (a) any authenticated principal can
   obtain this ticket and (b) it is therefore attackable offline if `svc_db`'s
   password is human-chosen. **Do not attempt to extract or crack it.**
7. Repeat step 5 against an SPN held by a **computer** account (e.g.
   `host/<dc>.lab.internal`) and compare the two cases. State what changes about
   the offline-attack proposition, and explain from that comparison why group
   Managed Service Accounts exist.
8. Enable Samba's JSON audit logging on the DC (the `auth_json_audit` /
   `authz_json_audit` debug classes — follow the Samba wiki's *Setting up Audit
   Logging* page for the syntax your version uses) and repeat step 3. Locate the
   `Authentication` JSON record the KDC emits and identify which fields carry
   "who", "from where" and "succeeded or failed".
9. Open the pre-captured Windows EVTX set. Locate one **4768** and one **4769**.
   In the 4769, read the **Service Name** and the **Ticket Encryption Type**, and
   state which value indicates RC4-HMAC and why that value is the lever a
   detection would key on. Locate a **4624** and read its logon type and
   authentication package; locate a **4625** and read its failure sub-status;
   locate a **4662** and identify the object and the rights GUIDs.
10. Build the comparison table below. The third column is the point of the lab —
    fill it in honestly.

| Artefact | What the Samba/OSS path showed me | What the Windows EVTX showed me | What **neither** showed me |
|---|---|---|---|
| TGT request (AS) | | | |
| Service-ticket request (TGS) | | | |
| Interactive/network logon | | | |
| Directory object access | | | |

**What this lab cannot reproduce — state it plainly to learners:**

- **LSASS artefacts.** There is no `lsass.exe` anywhere on the free path. Samba
  keeps its secrets in `secrets.tdb` and `sam.ldb` on disk, not in a protected
  process, so **none** of the LSASS telemetry can be produced or observed here: a
  process opening `lsass.exe` with read-memory rights, the corresponding
  cross-process handle-access record, LSA Protection refusing the handle, or
  Credential Guard's isolation. Learners meet the concept in Topic 5 and the
  artefact only if the pre-captured corpus happens to contain one.
- **True DCSync replication events.** Samba implements DRSUAPI replication
  between Samba DCs, but it does **not** emit Windows Security Event 4662 with
  the replication extended-right GUIDs. Its analogue is a
  `dsdbChange` JSON record on an entirely different schema (Samba emits a single
  `dsdbChange` record type; replication is one of the ways a change can arrive,
  not a separate record). A
  genuine 4662 DCSync artefact must come from pre-captured Windows data.
- **The Windows event field schema.** A Samba JSON audit record is not a 4768 or
  4769 event. In particular the **Ticket Encryption Type** field — the actual
  Kerberoasting detection lever — is a Windows Event Log field and has no Samba
  equivalent. Do not tell learners the Samba record substitutes for it. A modern Samba 4 AD DC negotiates **AES**
  (etype 18, `aes256-cts-hmac-sha1-96`) by default, so a learner watching this
  lab's own traffic will see AES every time and will **never** observe the
  RC4-HMAC (`0x17`) value the Kerberoasting lever keys on. That value must be
  read from the pre-captured Windows corpus in step 9. The wire
  capture *does* expose the negotiated encryption type, so the **protocol** point
  survives on the free path; the **detection-engineering** point requires the
  EVTX.
- **NTLM in anger.** The NTLM three-message exchange can be observed against
  Samba over SMB by forcing a single non-Kerberos connection, which is enough to
  see the challenge and the response. Pass-the-hash against a Windows host is not
  performed in this unit at all.

**Expected Output:**

An annotated packet list showing AS-REQ, AS-REP, TGS-REQ and TGS-REP with the
encrypted parts identified; `klist` and `klist -e` output before and after the
service-ticket request; the Samba `Authentication` JSON record with its "who /
from where / outcome" fields marked; the five Windows event records with the
named fields highlighted; and the completed comparison table with a **populated
third column**. A learner has succeeded when they can state which key encrypts
the service ticket and why that single fact makes Kerberoasting possible, without
referring to any tool.

**Reflection Questions:**

1. The service never contacted the KDC to validate the ticket you obtained. Name
   one real advantage of that design, and the consequence an attacker relies on.
2. You obtained a ticket for `svc_db` without holding any right to the database.
   Is that a vulnerability? Justify your answer in terms of what Kerberos is
   designed to prove and to whom.
3. ASD's *Detecting and Mitigating Active Directory Compromises* recommends
   moving SPN-bearing accounts to group Managed Service Accounts. Using only what
   you observed in steps 5 and 7, explain the mechanism by which that mitigation
   works.
4. Which finding in your comparison table could you not have made on the free
   path alone, and what would you need — lawfully — in order to make it?

---

## Assessment

### Formative Assessment: Command Equivalence Worksheet

**Type:** Short-answer worksheet with answer key

**Description:** Students complete a table of equivalent administrative tasks
across Linux and Windows (e.g. "list services", "create user", "view auth
events") and note the command for each. A second short table asks for the meaning
of each of the following and the host on which it is generated: 4624 with logon
types 2, 3 and 10; 4625; 4768; 4769 and its ticket-encryption-type field; 4662;
4688; and, on Linux, an `auditd` `execve` record's `uid`, `euid` and `auid`.
Self-marked.

**Learning Outcomes Assessed:** LO2, LO3, LO4, LO7, LO8

**Feedback mechanism:** Provided answer key with the canonical command for each
task on each platform.

---

### Summative Assessment: Host Hardening & Triage Report

**Type:** Practical report

**Description:** Students are given a deliberately weakened VM (excess accounts,
unnecessary services, weak logging, a planted persistence mechanism). They must
(a) document the initial insecure state, (b) apply and justify a hardening plan
mapped to the Essential Eight, (c) locate and explain the planted persistence,
and (d) recommend monitoring to detect a recurrence. Deliverable: 1,500–2,000
word report with evidence.

**Learning Outcomes Assessed:** LO2, LO3, LO4, LO5, LO6, LO7, LO8

The scenario pack supplied with the VM includes a small set of pre-captured
domain authentication records (4624, 4625, 4768, 4769, 4662). Part (c) requires
students to cite the authentication and process-creation evidence for the
persistence they find — the logon type that established the session, the
process-creation record, and, where the scenario is domain-joined, the relevant
ticket-request records — and to state in one paragraph which design property of
the protocol involved made the observed behaviour possible. **The report's word
count is unchanged: this requirement redistributes the existing scope rather
than extending it.**

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Initial-state documentation | LO2, LO6 |
| Hardening plan + Essential Eight mapping | LO3, LO5 |
| Persistence detection + log evidence | LO4, LO6, LO8 |
| Authentication-artefact reading + design-property explanation | LO7, LO8 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Administration competency | Performs all tasks correctly on both OSes with idiomatic commands | Performs tasks correctly with minor inefficiencies | Completes most tasks with errors | Unable to complete core tasks |
| Hardening & Essential Eight mapping | Comprehensive, correctly mapped, well justified | Solid hardening with valid mappings | Partial hardening; weak mapping | Minimal or incorrect hardening |
| Detection of compromise indicator | Finds indicator and cites exact log evidence | Finds indicator with adequate evidence | Finds indicator without strong evidence | Fails to locate indicator |
| Authentication-artefact reading | Reads the correct records, interprets logon type / ticket fields accurately, and explains the enabling design property in protocol terms | Reads the correct records and interprets the main fields, with a serviceable explanation | Identifies some records but misreads fields or explains by naming an attack rather than a mechanism | Cannot locate or interpret the relevant records |
| Communication | Clear, structured, correct terminology | Clear with minor lapses | Disorganised but understandable | Unclear or incorrect |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Patching, application control, and restricting
  administrative privileges are mapped to concrete hardening actions in Lab 2 and
  the summative report.
- **ACSC ISM and Windows hardening guidance:** Used as the reference standard for
  host and Active Directory hardening.
- **ACSC advisories on privilege misuse:** Referenced to motivate least-privilege
  account design in Lab 1.
- **ASD *Detecting and Mitigating Active Directory Compromises* (2024):** The
  Australian reference for Topic 5. It describes the SPN/service-ticket mechanism
  in the same terms this unit teaches it, names event 4769 as the record produced
  per service-ticket request, and gives the mitigation — minimise SPN-bearing
  user objects and move them to group Managed Service Accounts. Topic 5 teaches
  the mechanism; this publication supplies the Australian control response.
- **ASD/ACSC event-logging and forwarding guidance:** Sets the Australian
  expectation for what is generated, forwarded and retained, and is candid that
  high-volume Kerberos events are often dropped at the subscription — the blind
  spot Topic 6 requires learners to document.
- **Criminal Code Act 1995 (Cth) Part 10.7 (contextual):** Frames the scope
  boundary of Topic 5 and Lab 3. The unit observes protocols in a
  self-provisioned lab domain; conducting the corresponding attacks against a
  system without authorisation is an offence, and that work sits in the CTE major
  under CE01's authorisation regime.

---

## Further Reading

**Australian Cyber Security Centre (2024).** *Hardening Microsoft Windows / Restricting Administrative Privileges.* ACSC. https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight
> Relevance: The primary Australian reference for the hardening actions performed in this unit (Australian source).

**Russinovich, M., Solomon, D. & Ionescu, A. (2017).** *Windows Internals (7th ed.).* Microsoft Press.
> Relevance: Authoritative depth on Windows processes, services, and the registry behind Topic 3.

**Nemeth, E. et al. (2017).** *UNIX and Linux System Administration Handbook (5th ed.).* Addison-Wesley.
> Relevance: The standard reference for the Linux administration skills in Topic 2 and Lab 1.

**Microsoft (2024).** *Sysmon — Sysinternals.* https://learn.microsoft.com/sysinternals/downloads/sysmon
> Relevance: The free tool used to augment Windows logging in Lab 2; freely downloadable.

**Australian Cyber Security Centre (2024).** *Information Security Manual — System hardening guidelines.* ACSC. https://www.cyber.gov.au/ism
> Relevance: Australian baseline for host controls, used to benchmark the learner's hardening in Lab 2 (Australian source).

**Australian Signals Directorate (2024).** *Detecting and Mitigating Active Directory Compromises.* ASD/ACSC. https://www.cyber.gov.au/business-government/detecting-responding-to-threats/detecting-and-mitigating-active-directory-compromises
> Relevance: The primary Australian reference for Topic 5 and Lab 3. Describes the SPN/service-ticket mechanism, names event 4769 as the per-request record, and gives the gMSA and RC4 mitigations that Lab 3's reflection questions turn on (Australian source).

**Neuman, C., Yu, T., Hartman, S. & Raeburn, K. (2005).** *RFC 4120 — The Kerberos Network Authentication Service (V5).* IETF. https://www.rfc-editor.org/rfc/rfc4120
> Relevance: The normative specification behind Topic 5's AS-REQ/AS-REP and TGS-REQ/TGS-REP treatment; students verify the packet structures they capture in Lab 3 against it rather than against secondary summaries.

**Microsoft (2024).** *MS-NLMP — NT LAN Manager (NTLM) Authentication Protocol.* Microsoft Open Specifications. https://learn.microsoft.com/openspecs/windows_protocols/ms-nlmp/
> Relevance: The open specification for the NEGOTIATE/CHALLENGE/AUTHENTICATE exchange in Topic 5, and the primary source for the claim that the response is keyed by the NT hash rather than the password.

**The Samba Team (2024).** *Setting up Audit Logging / Interpreting JSON Audit Logs.* SambaWiki. https://wiki.samba.org/index.php/Setting_up_Audit_Logging
> Relevance: The configuration and record-schema reference for Lab 3's free/OSS domain controller, and the source for what the Samba audit path does and does not record compared with the Windows Event Log.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F02 |
| Unit Title | Operating Systems & Administration |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01 (recommended) |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) Part 10.7 (contextual — scope boundary for Topic 5 / Lab 3); otherwise ASD Essential Eight / ACSC ISM controls |
