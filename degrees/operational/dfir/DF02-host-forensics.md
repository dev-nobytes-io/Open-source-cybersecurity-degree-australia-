# DF02: Host Forensics

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches disk-level forensic analysis: acquiring a forensically sound disk
image, verifying its integrity, and analysing the artefacts that reconstruct what
happened on a host. Students work with Windows and Linux artefacts — the Master
File Table (MFT), prefetch, LNK and jump lists, registry hives, event logs, and
browser/user artefacts — and build forensic timelines with Plaso/log2timeline. The
emphasis is rigorous, repeatable analysis whose results would survive the
admissibility scrutiny established in DF01.

Host forensics is the evidentiary core of most investigations: it answers when an
intrusion began, what executed, what persisted, and what was accessed. In the
Australian context, the integrity practices here are what satisfy the *Evidence Act
1995*, and the findings feed NDB "what data was affected" assessments. DF02 builds
on DF01, F02 (Operating Systems), and OC03 (Malware Analysis), and precedes DF03
(Memory) and the capstone DF06.

---

## Prerequisites

- DF01 — DFIR Process & Legal Foundations
- F02 — Operating Systems & Administration

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** forensically sound disk-imaging and hash-verification procedures.
2. **Analyse** Windows artefacts (MFT, prefetch, LNK, registry, event logs) to
   reconstruct host activity.
3. **Analyse** Linux host artefacts (logs, file metadata, user activity) for
   evidence.
4. **Construct** a forensic timeline from host artefacts using Plaso/log2timeline.
5. **Evaluate** artefact evidence to determine execution, persistence, and access.
6. **Recommend** findings in a defensible, admissibility-aware manner.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of disk forensics
and host artefacts across Windows and Linux.

**Skills (AQF 7.2):** Students develop technical and analytical skills by imaging,
analysing artefacts, and constructing timelines.

**Application (AQF 7.3):** Students apply host forensics to realistic images and
produce defensible, admissibility-aware findings.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0432 | Perform forensic analysis of digital media to determine activity | Lab 1 — Imaging & Windows Artefact Analysis |
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0396 | Construct forensic timelines to reconstruct events | Lab 2 — Timeline Construction with Plaso |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Systems & software life cycle / assurance | SURE | Level 4–5 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Incident Management | Digital Forensics | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Forensic Imaging and Verification

This topic teaches acquiring a forensically sound image: write-blocking, imaging
formats (raw/E01), and hash verification (acquisition vs verification hashes) to
prove the working copy matches the source. It connects directly to DF01's chain of
custody.

**Key concepts:**
- Write-blocking and imaging formats (raw, E01)
- Acquisition vs verification hashing
- Working on copies, never originals

---

### Topic 2: The Windows File System and MFT

NTFS metadata is a rich evidence source. This topic covers the MFT, file
timestamps (the $STANDARD_INFORMATION vs $FILE_NAME "MACB" times and timestomping
detection), deleted-file recovery, and what file system metadata reveals.

**Key concepts:**
- MFT structure and resident/non-resident data
- MACB timestamps and timestomping detection
- Deleted-file recovery via the file system

---

### Topic 3: Windows Execution and Persistence Artefacts

This topic covers the artefacts that prove what ran and what persisted: prefetch
(execution evidence), Amcache/Shimcache, LNK files and jump lists (file access),
registry hives (run keys, services, UserAssist), and the Windows event logs.

**Key concepts:**
- Prefetch, Amcache/Shimcache (execution)
- LNK/jump lists (access), registry (persistence)
- Event logs for authentication and process creation

---

### Topic 4: Linux Host Artefacts

This topic covers Linux forensics: syslog/journald, auth logs, bash history,
cron/systemd persistence, file timestamps and inodes, and SUID/permission
anomalies — the Linux counterparts to the Windows artefacts.

**Key concepts:**
- Linux logs (syslog/journald/auth) and shell history
- cron/systemd persistence
- File metadata, inodes, and permission anomalies

---

### Topic 5: Forensic Timelines

A timeline turns scattered artefacts into a narrative. This topic teaches building
super-timelines with Plaso/log2timeline, filtering the noise, and correlating
artefacts to reconstruct the sequence of an intrusion.

**Key concepts:**
- Super-timelines with Plaso/log2timeline
- Filtering and pivoting on a timeline
- Reconstructing the intrusion narrative

---

### Topic 6: From Artefacts to Defensible Findings

This topic teaches synthesising artefacts into findings that are accurate,
evidence-linked, and admissibility-aware: stating confidence, distinguishing fact
from inference, and documenting the analytic method so it is repeatable.

**Key concepts:**
- Fact vs inference; stating confidence
- Evidence-linked, repeatable findings
- Admissibility-aware documentation (links to DF01)

**Australian context:** Findings must meet the Evidence Act 1995 standard from
DF01, and inform NDB data-impact assessments.

---

## Labs & Exercises

### Lab 1: Imaging & Windows Artefact Analysis

**Objective:** Acquire/verify a disk image and analyse Windows artefacts to
reconstruct host activity.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: Windows or Linux analysis VM
- Tools: FTK Imager (free), Autopsy / The Sleuth Kit, registry/prefetch parsers —
  all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 40 GB disk (within the 8 GB / 4-core /
  50 GB spec; no GPU)

**Instructions:**

1. Acquire (or load) the provided disk image; record acquisition and verification
   hashes and confirm they match.
2. Open the image in Autopsy / Sleuth Kit.
3. Analyse prefetch/Amcache to identify suspicious program execution.
4. Examine registry run keys and services for persistence.
5. Review LNK/jump lists and event logs to establish file access and logons.
6. Map confirmed activity to ATT&CK (v19) and note the evidence for each finding.

**Expected Output:**

Verified image hashes, a set of evidence-linked findings (execution, persistence,
access), and ATT&CK mappings. Learners can show the artefact behind each claim.

**Reflection Questions:**

1. Which artefact most reliably proved execution, and why?
2. How would timestomping have affected your findings, and how would you detect it?
3. How do your verification hashes support admissibility under the Evidence Act
   1995?

---

### Lab 2: Timeline Construction with Plaso

**Objective:** Build and analyse a forensic super-timeline to reconstruct an
intrusion sequence.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Plaso/log2timeline, a timeline viewer (Timesketch optional) — all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 40 GB disk (within spec; no GPU)

**Instructions:**

1. Run log2timeline against the image (or provided artefacts) to generate a Plaso
   storage file.
2. Produce a filtered timeline around the suspected incident window.
3. Identify the earliest evidence of compromise and the sequence that followed.
4. Correlate at least three artefact types into a coherent narrative.
5. Note any anti-forensic indicators (e.g. timestamp anomalies, log clearing).
6. Summarise the reconstructed sequence with evidence references.

**Expected Output:**

A filtered super-timeline, an evidence-referenced intrusion narrative, and any
anti-forensic indicators. Learners can defend the start time and sequence of the
intrusion.

**Reflection Questions:**

1. How did the timeline change your understanding versus isolated artefacts?
2. What would you do if a key log had been cleared?
3. How precise is your "initial compromise" time, and what is your confidence?

---

## Assessment

### Formative Assessment: Artefact Identification Drill

**Type:** Self-check exercise with answer key

**Description:** Given artefact excerpts (prefetch, registry, MFT, Linux logs),
students state what each proves and its evidentiary weight. Self-marked.

**Learning Outcomes Assessed:** LO2, LO3

**Feedback mechanism:** Answer key with the correct interpretation and weight per
artefact.

---

### Summative Assessment: Host Forensic Report

**Type:** Practical report

**Description:** Given a forensic disk image with planted intrusion activity,
students (a) verify image integrity, (b) analyse Windows/Linux artefacts, (c)
construct a forensic timeline, and (d) produce a defensible report with findings,
evidence, confidence statements, and ATT&CK mappings — written to the admissibility
standard from DF01. Deliverable: 2,500–3,000 word report with evidence appendix.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Image verification | LO1 |
| Windows/Linux artefact analysis | LO2, LO3 |
| Timeline construction | LO4 |
| Defensible findings | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Forensic soundness | Rigorous imaging/verification & method | Sound | Gaps | Unsound |
| Artefact analysis | Thorough, accurate, well-evidenced | Solid | Partial | Inaccurate |
| Timeline | Precise, correlated, narrative-driven | Sound | Partial | Weak |
| Defensible findings | Fact/inference clear; admissibility-aware | Mostly clear | Inconsistent | Poor |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Evidence Act 1995 (Cth):** Imaging/verification and findings written to the
  admissibility standard from DF01.
- **NDB scheme:** Host findings inform the "what data was affected" assessment.
- **Australian breach case studies:** Used to frame realistic host-forensic
  scenarios (e.g. data-theft intrusions).

---

## Further Reading

**Carrier, B. (2005).** *File System Forensic Analysis.* Addison-Wesley.
> Relevance: The definitive reference on file-system forensics underpinning Topics 2–3.

**The Sleuth Kit / Autopsy (2024).** *Documentation.* https://www.sleuthkit.org
> Relevance: The free disk-forensics toolkit used in Lab 1.

**log2timeline / Plaso (2024).** *Plaso Documentation.* https://plaso.readthedocs.io
> Relevance: The free super-timeline tool used in Lab 2.

**SANS DFIR (2024).** *Windows Forensic Analysis posters & artefact references.* SANS Institute. https://www.sans.org/posters/
> Relevance: Practical, freely available references for the Windows artefacts in Topic 3.

**Australian Cyber Security Centre (2024).** *Incident response & evidence-handling guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian guidance framing host forensics within incident response (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DF02 |
| Unit Title | Host Forensics |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | DFIR |
| Prerequisites | DF01, F02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Evidence Act 1995 (Cth); Privacy Act 1988 (NDB, contextual) |
