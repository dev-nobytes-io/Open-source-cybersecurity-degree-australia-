# DF01: DFIR Process & Legal Foundations

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit establishes the process discipline and legal foundations that make
digital forensics and incident response (DFIR) defensible. Before touching a disk
image or a memory dump, a practitioner must understand the incident-response
lifecycle, how to handle evidence so it survives legal scrutiny, and the Australian
legal obligations that govern an investigation. The unit anchors on **PICERL** and
**NIST SP 800-61**, the **chain of custody**, and the **Evidence Act 1995 (Cth)** —
the rules that determine whether the work a forensic analyst does will hold up in
court or before a regulator.

DFIR carries the strongest legal obligations of any major in this degree: an
investigation routinely intersects the *Evidence Act 1995*, the *Privacy Act 1988*,
the Notifiable Data Breaches scheme, APRA notification rules, and the SOCI Act. DF01
sets these foundations for the technical units that follow (DF02–DF04), the
operational unit DF05, and the capstone DF06. It builds directly on OC04 (Incident
Response Lifecycle) and F05 (Legal, Ethics & Australian Compliance).

---

## Prerequisites

- OC04 — Incident Response Lifecycle
- F05 — Legal, Ethics & Australian Compliance

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the PICERL / NIST SP 800-61 incident-response lifecycle to a
   simulated incident.
2. **Apply** chain-of-custody documentation and evidence-handling practices that
   preserve integrity and admissibility.
3. **Analyse** the admissibility of digital evidence under the Evidence Act 1995
   (Cth).
4. **Evaluate** the Australian legal and privacy obligations triggered by an
   investigation (Privacy Act, NDB, APRA, SOCI).
5. **Analyse** the order of volatility to prioritise evidence acquisition.
6. **Recommend** a defensible investigation plan for a given incident scenario.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of the DFIR
lifecycle, evidence handling, and the Australian legal framework for investigations.

**Skills (AQF 7.2):** Students develop analytical and judgement skills by assessing
admissibility, obligations, and acquisition priorities.

**Application (AQF 7.3):** Students apply these foundations to plan defensible
investigations that meet Australian legal and regulatory requirements.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Forensics Analyst | IN-FOR-002 | T0432 | Plan and perform evidence collection preserving integrity for legal use | Lab 1 — Chain of Custody & Evidence Plan |
| NIST NICE DCWF | 2023 | Cyber Crime Investigator | IN-INV-001 | T0103 | Apply legal and policy requirements to a cyber investigation | Lab 2 — PICERL Mapping & Legal Obligations |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Systems & software life cycle / assurance | SURE | Level 4 | Lab 1 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Incident Management | Digital Forensics | Practitioner | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | DF01-K01 | Knowledge of the DFIR lifecycle | Topic 1 |
| Knowledge | DF01-K02 | Knowledge of chain of custody and evidence integrity | Topic 2 |
| Knowledge | DF01-K03 | Knowledge of order of volatility and acquisition strategy | Topic 3 |
| Knowledge | DF01-K04 | Knowledge of the Evidence Act 1995, admissibility, and privacy/notification obligations | Topic 4; Topic 5 |
| Skill | DF01-S01 | Skill in building a chain-of-custody and evidence plan | Lab 1 |
| Skill | DF01-S02 | Skill in mapping an incident to PICERL with legal obligations | Lab 2 |
| Ability | DF01-A01 | Ability to acquire evidence in a forensically sound, defensible manner | Lab 1; Topic 3 |
| Ability | DF01-A02 | Ability to determine the legal obligations an incident triggers | Lab 2; Topic 6 |
| Task | T0432 | Plan and perform evidence collection preserving integrity for legal use | Lab 1 |
| Task | T0103 | Apply legal and policy requirements to a cyber investigation | Lab 2 |

---

## Topics

### Topic 1: The DFIR Lifecycle

This topic frames DFIR as a disciplined lifecycle, integrating PICERL (Preparation,
Identification, Containment, Eradication, Recovery, Lessons Learned) with NIST SP
800-61. It positions forensics within incident response — forensics answers "what
happened and how", IR drives "what we do about it".

**Key concepts:**
- PICERL phases and NIST SP 800-61 alignment
- Forensics vs incident response (and their overlap)
- Preparation as the determinant of everything downstream

---

### Topic 2: Chain of Custody and Evidence Integrity

Evidence that cannot be trusted is worthless. This topic teaches chain-of-custody
documentation, write-blocking, cryptographic hashing for integrity, secure storage,
and the discipline of recording who handled what, when, and why — the spine of
admissibility.

**Key concepts:**
- Chain-of-custody documentation
- Write-blocking and forensic soundness
- Hashing for integrity and verification

**Australian context:** These practices are what satisfy the Evidence Act 1995
requirements introduced in Topic 4.

---

### Topic 3: Order of Volatility and Acquisition Strategy

Some evidence vanishes in seconds. This topic teaches the order of volatility
(CPU/registers → memory → network state → disk → backups) and how it drives
acquisition priorities, plus the trade-off between preserving evidence and
containing an active threat.

**Key concepts:**
- The order of volatility
- Live vs dead acquisition
- Balancing preservation against containment

---

### Topic 4: Evidence Act 1995 and Admissibility

This topic covers the Australian legal test for admitting electronic evidence under
the *Evidence Act 1995 (Cth)*: authenticity, integrity, relevance, and the role of
documentation and expert testimony. It explains how forensic process choices
directly affect whether evidence is admissible.

**Key concepts:**
- Admissibility: authenticity, integrity, relevance
- How process defects exclude evidence
- The analyst as potential expert witness

**Australian context:** This topic is Australian evidence law applied to forensics.

---

### Topic 5: Privacy and Investigative Obligations

Investigations handle personal information and can themselves create obligations.
This topic covers the *Privacy Act 1988* and APPs as they apply to evidence
handling, the limits on collection/use during an investigation, and the duty to
protect investigation data.

**Key concepts:**
- Privacy Act/APP obligations during investigations
- Minimising and protecting personal information handled
- Lawful basis for investigative collection

**Australian context:** Privacy Act/APP obligations in the investigative context.

---

### Topic 6: Reporting and Notification Obligations Overview

This topic previews the notification landscape that DF05 develops: the NDB scheme
(OAIC), APRA CPS 234 notification, ASD/ACSC voluntary reporting, and SOCI
mandatory reporting — establishing that response and reporting run in parallel from
the moment an incident is identified.

**Key concepts:**
- NDB, APRA, ASD/ACSC, and SOCI obligations at a glance
- Parallel response and reporting timelines
- Why legal/comms must be engaged early

**Australian context:** The full Australian incident-notification landscape.

---

## Labs & Exercises

### Lab 1: Chain of Custody & Evidence Plan

**Objective:** Document a simulated evidence collection with a defensible chain of
custody and acquisition plan.

**Prerequisites:**
- Topics 1–4

**Environment:**
- Operating System: any (documentation lab)
- Tools: a chain-of-custody template, a hashing utility (sha256sum), the Evidence
  Act 1995 reference — all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take a scenario: a compromised workstation must be preserved for investigation.
2. Build an acquisition plan ordered by volatility (what to collect first and why).
3. For each evidence item, complete a chain-of-custody record (identifier, handler,
   time, hash, storage).
4. Hash a sample evidence file and record the value; explain how this proves
   integrity.
5. Identify two process choices that would jeopardise admissibility under the
   Evidence Act 1995 and how you avoided them.
6. Note any personal-information handling and the Privacy Act consideration.

**Expected Output:**

An acquisition plan ordered by volatility, complete chain-of-custody records with
hashes, and a short admissibility note. Learners can explain how each step supports
admissibility under the Evidence Act 1995.

**Reflection Questions:**

1. Which evidence would you lose first if you delayed acquisition, and why?
2. How would a broken chain of custody be exploited by opposing counsel?
3. What privacy obligations applied to the data you handled?

---

### Lab 2: PICERL Mapping & Legal Obligations

**Objective:** Map a simulated incident to PICERL and identify all triggered
Australian legal/notification obligations.

**Prerequisites:**
- Topics 1, 5, and 6

**Environment:**
- Operating System: any
- Tools: a decision-log template, OAIC/APRA/ACSC/SOCI references (free)
- Minimum hardware: trivial

**Instructions:**

1. Read the provided incident scenario (e.g. a breach exposing customer records at
   an Australian company).
2. Map the incident's events to PICERL phases in a decision log.
3. At the identification/containment phases, determine which obligations are
   triggered: NDB (OAIC), APRA CPS 234 (if regulated), ASD/ACSC, SOCI (if critical
   infrastructure).
4. Record the notification timeframe for each applicable obligation.
5. Identify the decision points where legal/comms must be engaged.
6. Reference a relevant Australian breach case (e.g. Medibank, Optus, Latitude) to
   illustrate consequences.

**Expected Output:**

A PICERL-mapped decision log with triggered obligations and timeframes, and a short
comparison to a real Australian breach. Learners can justify each notification
determination.

**Reflection Questions:**

1. How do the response and notification timelines interact and constrain each
   other?
2. Which obligation has the tightest timeframe, and how does that shape early
   decisions?
3. What did the referenced Australian breach reveal about getting this wrong?

---

## Assessment

### Formative Assessment: Admissibility & Obligation Drill

**Type:** Scenario exercise with answer key

**Description:** Given short scenarios, students judge whether evidence is
admissible and which Australian obligations are triggered. Self-marked.

**Learning Outcomes Assessed:** LO3, LO4

**Feedback mechanism:** Answer key with the admissibility/obligation reasoning per
scenario.

---

### Summative Assessment: Investigation Plan & Legal Brief

**Type:** Analytical report

**Description:** For an assigned Australian incident scenario, students produce (a)
a PICERL-aligned investigation plan, (b) an acquisition strategy ordered by
volatility with chain-of-custody approach, (c) an admissibility analysis under the
Evidence Act 1995, and (d) a legal/notification brief covering Privacy Act, NDB,
APRA, and SOCI as applicable. Deliverable: 2,500–3,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Investigation plan (PICERL) | LO1, LO6 |
| Acquisition & custody strategy | LO2, LO5 |
| Admissibility analysis | LO3 |
| Legal/notification brief | LO4 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Process & lifecycle | Rigorous PICERL-aligned plan | Sound plan | Partial | Weak |
| Evidence handling | Defensible custody & acquisition | Adequate | Gaps | Unsound |
| Legal accuracy | Precise admissibility & obligation analysis | Mostly correct | Partial | Incorrect |
| Australian context | Apt use of AU law and case study | Adequate | Superficial | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Evidence Act 1995 (Cth):** The admissibility framework central to Topic 4 and
  both labs.
- **Privacy Act 1988 & APPs:** Obligations when handling personal information in
  investigations.
- **NDB / APRA CPS 234 / ASD-ACSC / SOCI:** The notification landscape (Topic 6,
  Lab 2).
- **Australian breach case studies:** Medibank, Optus, Latitude used to illustrate
  consequences.

---

## Further Reading

**Australian Government (1995).** *Evidence Act 1995 (Cth).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The primary legislation governing admissibility of digital evidence (Australian source).

**NIST (2012).** *SP 800-61 Rev. 2 — Computer Security Incident Handling Guide.* NIST. https://csrc.nist.gov/pubs/sp/800/61
> Relevance: The incident-handling lifecycle anchoring this unit alongside PICERL.

**NIST (2006).** *SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response.* NIST. https://csrc.nist.gov/pubs/sp/800/86/final
> Relevance: Foundational guidance on forensic process, order of volatility, and evidence handling.

**Office of the Australian Information Commissioner (2024).** *Notifiable Data Breaches & APP guidance.* OAIC. https://www.oaic.gov.au
> Relevance: The Australian breach-notification and privacy obligations covered in Topics 5–6 (Australian source).

**Casey, E. (2011).** *Digital Evidence and Computer Crime (3rd ed.).* Academic Press.
> Relevance: The standard reference on digital evidence, admissibility, and forensic process.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | DF01 |
| Unit Title | DFIR Process & Legal Foundations |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | DFIR |
| Prerequisites | OC04, F05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Evidence Act 1995 (Cth); Privacy Act 1988 (APPs, NDB); APRA CPS 234; Security of Critical Infrastructure Act 2018 |
