# CE01: Offensive Foundations & Ethics

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (red team / emulation experience)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must review dual-use risk)_

---

## Overview

This unit is the ethical and legal foundation on which the entire Cyber Threat
Emulation major rests. Before any adversary technique is studied, students must
understand that emulation is lawful **only** within an authorised, scoped
engagement, and that the line between professional red teaming and a criminal
offence is *written authorisation*. The unit covers Australian computer-crime law,
rules of engagement, scope discipline, data handling, responsible disclosure, and
the threat-intelligence-led testing frameworks (TIBER-AU) used in regulated sectors.

Emulation exists to make defenders better: every technique is framed as a test of
detection and response, conducted in isolated environments under explicit
permission. In the Australian context the governing law is the **Criminal Code Act
1995 (Cth) Part 10.7** (computer offences) alongside the *Cybercrime Act 2001*, with
the *Privacy Act 1988* applying to any personal data encountered. CE01 builds on
OC06 (Offensive Security Concepts) and F05 (Legal/Ethics) and is the prerequisite
gate for CE02–CE06. Per the major's safety rules, this legal framing is revisited in
every subsequent unit.

---

## Prerequisites

- OC06 — Offensive Security Concepts
- F05 — Legal, Ethics & Australian Compliance

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** what constitutes authorised vs unauthorised access under Australian
   computer-crime law.
2. **Design** a rules-of-engagement and authorisation document for an emulation
   engagement.
3. **Evaluate** an authorisation scope to determine what is and is not permitted.
4. **Apply** scope-discipline, data-handling, and responsible-disclosure practices.
5. **Analyse** the role of threat-intelligence-led testing frameworks (TIBER-AU) in
   the Australian regulated sector.
6. **Evaluate** the ethical and dual-use responsibilities of an emulation
   practitioner.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of the legal,
ethical, and authorisation framework for adversary emulation in Australia.

**Skills (AQF 7.2):** Students develop judgement and drafting skills by constructing
and evaluating authorisation and scope.

**Application (AQF 7.3):** Students apply this framework to ensure all emulation is
lawful, scoped, and ethical in the Australian context.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Policy & Strategy Planner | OV-SPP-001 | T0098 | Develop and review agreements ensuring legal/regulatory compliance for testing | Lab 1 — Rules of Engagement |
| NIST NICE DCWF | 2023 | Vulnerability Assessment Analyst | PR-VAM-001 | T0028 | Conduct authorised assessment within a defined, lawful scope | Lab 2 — Scope & Legal Review |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 4 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Cyber | Authorised Testing & Ethics | Practitioner | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CE01-K01 | Knowledge of how emulation, pentest, and attack differ | Topic 1 |
| Knowledge | CE01-K02 | Knowledge of Australian computer-crime law | Topic 2 |
| Knowledge | CE01-K03 | Knowledge of authorisation, rules of engagement, and scope discipline | Topic 3; Topic 4 |
| Knowledge | CE01-K04 | Knowledge of responsible disclosure, professional ethics, and TIBER-AU | Topic 5; Topic 6 |
| Skill | CE01-S01 | Skill in drafting rules of engagement | Lab 1 |
| Skill | CE01-S02 | Skill in performing a scope and legal review | Lab 2 |
| Ability | CE01-A01 | Ability to determine when offensive activity is lawfully authorised | Lab 2; Topic 3 |
| Ability | CE01-A02 | Ability to apply professional ethics to offensive work | Topic 5; Summative |
| Task | T0098 | Develop and review agreements ensuring legal/regulatory compliance for testing | Lab 1 |
| Task | T0028 | Conduct authorised assessment within a defined, lawful scope | Lab 2 |

---

## Topics

### Topic 1: Emulation vs Pentest vs Attack

This topic distinguishes adversary emulation (testing whether defenders detect a
*specific* actor's behaviour) from penetration testing (finding vulnerabilities) and
from criminal attack (no authorisation). It establishes emulation's defensive
purpose: improving detection and response.

**Key concepts:**
- Emulation vs pentest vs red team vs crime
- Emulation's defensive purpose
- Why authorisation defines legitimacy

---

### Topic 2: Australian Computer-Crime Law

This topic covers the law in detail: the **Criminal Code Act 1995 (Cth) Part 10.7**
computer offences (unauthorised access, modification, impairment), the *Cybercrime
Act 2001*, what "unauthorised" means, state/territory provisions, and the penalties —
establishing why scope is a legal boundary, not a guideline.

**Key concepts:**
- Criminal Code Act 1995 Part 10.7 offences
- "Unauthorised" access and the role of permission
- State/territory provisions and penalties

**Australian context:** This topic is Australian computer-crime law applied to
emulation.

---

### Topic 3: Authorisation and Rules of Engagement

This topic teaches what makes authorisation valid and complete: written permission
from someone with authority, defined scope (in/out), permitted techniques, timing,
emergency-stop, and the legal clauses that protect both parties.

**Key concepts:**
- Valid written authorisation
- Rules of engagement components
- Emergency-stop and deconfliction

---

### Topic 4: Scope Discipline and Data Handling

This topic covers operating within scope: never exceeding it, escalating (not
exploiting) out-of-scope findings, and handling any credentials or personal data
encountered per evidence and Privacy Act obligations.

**Key concepts:**
- Staying within scope; escalating out-of-scope findings
- Handling credentials/sensitive data lawfully
- Privacy Act obligations during testing

**Australian context:** Privacy Act 1988 obligations for personal data encountered.

---

### Topic 5: Responsible Disclosure and Professional Ethics

This topic covers reporting findings only to the authorising client, never to third
parties without consent, professional codes, and the dual-use responsibility of
emulation knowledge.

**Key concepts:**
- Client-only disclosure; no third-party leakage
- Professional ethics codes
- Dual-use responsibility

---

### Topic 6: Threat-Led Testing and TIBER-AU

This topic introduces threat-intelligence-led red teaming and the **TIBER-AU**
framework (the Australian adaptation of TIBER-EU) used in the financial sector,
including its phases and the role of regulators and intelligence in scoping a
realistic, controlled test.

**Key concepts:**
- Threat-intelligence-led testing
- TIBER-AU phases and roles
- Realistic, controlled, regulator-aware testing

**Australian context:** TIBER-AU is the Australian threat-led testing framework.

---

## Labs & Exercises

### Lab 1: Rules of Engagement (deliverable activity)

**Objective:** Draft a complete rules-of-engagement and authorisation document for a
fictional emulation engagement.

**Prerequisites:**
- Topics 1–4

**Environment:**
- No technical environment — a documentation deliverable. Any device within the
  8 GB / 4-core / 50 GB spec.

**Instructions:**

1. Take a fictional Australian organisation commissioning an authorised emulation.
2. Draft the RoE: parties/signatories, in-scope and explicitly out-of-scope assets,
   permitted techniques, testing window, and emergency-stop/deconfliction contacts.
3. Add a clause referencing the Criminal Code Act 1995 (Cth) Part 10.7 establishing
   that out-of-scope activity is unauthorised access.
4. Add a data-handling clause for any personal information encountered (Privacy Act).
5. Add a responsible-disclosure clause (client-only).
6. Identify three ways scope creep could occur and how the document prevents each.

**Expected Output:**

A complete, signable RoE/authorisation document with scope boundaries, legal
references, data-handling, and disclosure clauses. Learners can justify why each
clause exists and which law/obligation it protects against breaching.

**Reflection Questions:**

1. Why is written, scoped authorisation the single most important protection under
   the Criminal Code Act?
2. How would the RoE change for a TIBER-AU engagement?
3. What ethical obligations apply if you find evidence of a real, unrelated crime?

---

### Lab 2: Scope & Legal Review (analysis activity)

**Objective:** Review an authorisation scope, determine what is and is not
permitted, and identify the Australian legal implications.

**Prerequisites:**
- Topics 2–5

**Environment:**
- No technical environment — an analysis activity using a provided scope document.
  Any device.

**Instructions:**

1. Read the provided (fictional) authorisation scope and proposed activities.
2. Classify each proposed activity as in-scope / out-of-scope / ambiguous.
3. For each out-of-scope or ambiguous item, identify the legal risk under the
   Criminal Code Act 1995 Part 10.7.
4. Recommend how to make ambiguous items compliant (clarify scope, seek written
   approval).
5. Identify any activity that would trigger Privacy Act obligations.
6. Produce a short go/no-go assessment for the engagement.

**Expected Output:**

A classified activity list with legal-risk analysis, compliance recommendations, and
a go/no-go assessment. Learners can defend each classification against the law and
scope.

**Reflection Questions:**

1. Which ambiguous activity was riskiest, and how did you resolve it?
2. How does acting on an ambiguous scope expose the practitioner personally?
3. Why must out-of-scope findings be escalated rather than explored?

---

## Assessment

### Formative Assessment: Authorised-or-Not Drill

**Type:** Scenario exercise with answer key

**Description:** Given proposed activities and a scope, students judge whether each
is lawful/authorised and what would make it compliant. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with the compliance judgement and reasoning.

---

### Summative Assessment: Engagement Authorisation Package

**Type:** Practical report

**Description:** For a fictional Australian engagement, students produce (a) a
complete RoE/authorisation package, (b) a scope review with legal-risk analysis
under the Criminal Code Act 1995 Part 10.7, (c) data-handling and disclosure
provisions (Privacy Act), and (d) a short analysis of how a TIBER-AU engagement would
differ. Deliverable: 2,000–2,500 word package.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| RoE/authorisation package | LO2, LO4 |
| Scope & legal-risk review | LO1, LO3 |
| Disclosure/ethics & TIBER-AU | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Legal accuracy | Precise, correct AU computer-crime law | Mostly correct | Partial | Incorrect |
| Authorisation & scope | Complete, defensible RoE and scope control | Sound | Gaps | Weak |
| Ethics & data handling | Rigorous disclosure/Privacy handling | Adequate | Superficial | Poor |
| TIBER-AU understanding | Accurate threat-led framing | Reasonable | Vague | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Criminal Code Act 1995 (Cth) Part 10.7 & Cybercrime Act 2001:** The legal basis
  for the authorisation requirement central to the major.
- **Privacy Act 1988:** Obligations for personal data encountered during testing.
- **TIBER-AU:** The Australian threat-intelligence-led red-team framework.

---

## Further Reading

**Australian Government (1995).** *Criminal Code Act 1995 (Cth) — Part 10.7 Computer offences.* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The primary Australian computer-crime law governing authorisation (Australian source).

**Reserve Bank of Australia / CFR (2024).** *TIBER-AU framework.* https://www.rba.gov.au
> Relevance: The Australian threat-intelligence-led red-team framework introduced in Topic 6 (Australian source).

**MITRE Center for Threat-Informed Defense (2024–2026).** *Adversary Emulation Library.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The emulation methodology framed within authorised engagements across the major.

**CREST (2024).** *Guidance for assured, authorised penetration testing & red teaming.* CREST. https://www.crest-approved.org
> Relevance: Professional standards for scope, ethics, and conduct in authorised engagements.

**Office of the Australian Information Commissioner (2024).** *Privacy guidance.* OAIC. https://www.oaic.gov.au
> Relevance: Privacy Act obligations for personal data encountered during testing (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CE01 |
| Unit Title | Offensive Foundations & Ethics |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Cyber Threat Emulation |
| Prerequisites | OC06, F05 |
| Domain Expert | _Unassigned — required before Practitioner Approved (red team experience)_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved (dual-use review)_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) Part 10.7; Cybercrime Act 2001; Privacy Act 1988 |
