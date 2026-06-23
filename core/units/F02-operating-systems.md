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
Windows model (SIDs, groups, UAC, privileged groups such as Domain Admins) and
introduces how privilege-escalation paths form.

**Key concepts:**
- Linux sudo and the principle of least privilege
- Windows access tokens, UAC, and privileged groups
- How misconfiguration creates escalation paths

**Australian context:** "Restrict administrative privileges" is an Essential
Eight mitigation; this topic is its technical foundation.

---

### Topic 5: System Logging and Auditing

A host that is not logged cannot be investigated. This topic covers Linux logging
(syslog, journald, auditd) and Windows logging (the Event Log, Sysmon as a free
augmentation), what each captures by default, and how to enable richer auditing.
It is the host-side companion to F06's log analysis.

**Key concepts:**
- journald/syslog vs Windows Event Log: structure and default coverage
- Process-creation and authentication events as high-value telemetry
- Augmenting native logging with free tooling (auditd, Sysmon)

---

### Topic 6: Host Hardening and Compromise Indicators

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
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS *or* Windows 10/11 VM (learner chooses one
  to harden, then inspects the other)
- Tools: native tooling plus free augmentation (auditd on Linux, Sysmon on
  Windows)
- Minimum hardware: as Lab 1

**Instructions:**

1. Produce a baseline state snapshot: listening ports (`ss -tlnp` / `netstat
   -ano`), local accounts, services, and scheduled tasks/cron jobs.
2. Apply at least four hardening actions and map each to an Essential Eight
   mitigation — e.g. apply pending updates (patch OS), remove an unneeded
   account (restrict privileges), disable an unused service, enable richer
   logging (auditd/Sysmon).
3. Re-snapshot and diff against the baseline; record what changed.
4. Introduce a benign "indicator" (e.g. a scheduled task that runs `whoami`
   hourly) to simulate persistence.
5. Hunt for the indicator using only inspection commands — list scheduled
   tasks/cron, check recently created accounts, and review logs for its creation.
6. Document how you found it and what log entry recorded its creation.

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

## Assessment

### Formative Assessment: Command Equivalence Worksheet

**Type:** Short-answer worksheet with answer key

**Description:** Students complete a table of equivalent administrative tasks
across Linux and Windows (e.g. "list services", "create user", "view auth
events") and note the command for each. Self-marked.

**Learning Outcomes Assessed:** LO2, LO3, LO4

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

**Learning Outcomes Assessed:** LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Initial-state documentation | LO2, LO6 |
| Hardening plan + Essential Eight mapping | LO3, LO5 |
| Persistence detection + log evidence | LO4, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Administration competency | Performs all tasks correctly on both OSes with idiomatic commands | Performs tasks correctly with minor inefficiencies | Completes most tasks with errors | Unable to complete core tasks |
| Hardening & Essential Eight mapping | Comprehensive, correctly mapped, well justified | Solid hardening with valid mappings | Partial hardening; weak mapping | Minimal or incorrect hardening |
| Detection of compromise indicator | Finds indicator and cites exact log evidence | Finds indicator with adequate evidence | Finds indicator without strong evidence | Fails to locate indicator |
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
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | None directly (ASD Essential Eight / ACSC ISM controls) |
