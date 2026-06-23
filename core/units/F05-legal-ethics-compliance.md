# F05: Legal, Ethics & Australian Compliance

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Cybersecurity is practised within a legal and ethical framework, and a
practitioner who ignores it can cause serious harm — to others and to their own
career. This unit gives learners working knowledge of the Australian legislation
that governs computer access, privacy, data breaches, and critical
infrastructure, alongside the professional ethics and authorisation boundaries
that separate legitimate security work from criminal conduct. It is the unit that
makes the rest of the degree safe to practise: the same `nmap` command is
professional in one context and an offence in another, and the difference is
authorisation and law.

The unit is explicitly Australian. It covers the *Cybercrime Act 2001*, the
*Privacy Act 1988* and Australian Privacy Principles, the Notifiable Data
Breaches scheme, and the *Security of Critical Infrastructure Act 2018* (SOCI),
together with the roles of regulators such as the OAIC, ACSC/ASD, and the AFP.
F05 is a prerequisite for every offensive or investigative unit in the degree,
including OC06 (Offensive Security Concepts), the CTE major, and the DFIR major.

---

## Prerequisites

- F01 — Networking Fundamentals (for technical context)

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Describe** the key Australian laws governing computer access, privacy, data
   breaches, and critical infrastructure, and explain what conduct each governs.
2. **Explain** the Australian Privacy Principles and the obligations of the
   Notifiable Data Breaches scheme.
3. **Identify** when an activity requires explicit authorisation and describe the
   legal consequences of acting without it.
4. **Demonstrate** the construction of a basic rules-of-engagement /
   authorisation document for a security activity.
5. **Explain** professional ethics codes and how they guide conduct where the law
   is silent or ambiguous.
6. **Describe** the roles and powers of the relevant Australian regulators and
   how to interact with them.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of the
Australian legal, regulatory, and ethical environment for cybersecurity.

**Skills (AQF 7.2):** Students develop cognitive and communication skills by
analysing scenarios for legal and ethical issues and by drafting authorisation
documentation.

**Application (AQF 7.3):** Students apply this knowledge to realistic
professional scenarios, producing the authorisation and breach-response artefacts
an Australian practitioner is expected to handle.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Legal Advisor | OV-LGA-001 | T0098 | Develop and review policies/agreements ensuring legal and regulatory compliance | Lab 1 — Drafting Rules of Engagement |
| NIST NICE DCWF | 2023 | Privacy Officer/Privacy Compliance Manager | OV-LGA-002 | T0863 | Ensure organisational compliance with privacy and data-breach obligations | Lab 2 — Notifiable Data Breach Tabletop |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information governance | IRMG | Level 3 | Throughout |
| Personal data protection | PEDP | Level 3 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Legal & Regulatory | Foundational | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F05-K01 | Knowledge of Australian computer-crime law (Cybercrime Act 2001) and the authorisation concept | Topic 1; Lab 1 |
| Knowledge | F05-K02 | Knowledge of the Privacy Act 1988 and the Australian Privacy Principles | Topic 2 |
| Knowledge | F05-K03 | Knowledge of the Notifiable Data Breaches scheme and SOCI Act obligations | Topic 3; Topic 4 |
| Knowledge | F05-K04 | Knowledge of Australian regulators (OAIC, ACSC/ASD, AFP, APRA) and their roles | Topic 6 |
| Skill | F05-S01 | Skill in constructing a rules-of-engagement / authorisation document | Lab 1 |
| Skill | F05-S02 | Skill in performing an NDB eligible-breach assessment and notification | Lab 2 |
| Ability | F05-A01 | Ability to determine when an activity requires explicit authorisation | Lab 1; Formative |
| Ability | F05-A02 | Ability to apply professional ethics where the law is silent or ambiguous | Topic 5; Summative |
| Task | T0098 | Develop and review policies/agreements ensuring legal and regulatory compliance | Lab 1 |
| Task | T0863 | Ensure organisational compliance with privacy and data-breach obligations | Lab 2 |

---

## Topics

### Topic 1: Computer Crime Law — The Cybercrime Act 2001

The *Cybercrime Act 2001* (Cth) and the related Commonwealth Criminal Code
offences govern unauthorised access to, modification of, and impairment of
computer data. This topic explains what constitutes "unauthorised" access, why
authorisation is the pivotal concept for security professionals, and the
penalties involved. It establishes the legal reason why every offensive or
investigative technique in the degree must be performed only with explicit
authorisation.

**Key concepts:**
- Unauthorised access, modification, and impairment offences
- "Authorisation" as the line between professional work and crime
- State and territory equivalents to Commonwealth offences

**Australian context:** This entire topic is Australian law; it is the legal
spine of the degree's ethics requirements.

---

### Topic 2: Privacy — The Privacy Act and the APPs

The *Privacy Act 1988* (Cth) and the 13 Australian Privacy Principles (APPs)
govern how organisations collect, use, store, and disclose personal information.
This topic covers what counts as personal and sensitive information, the key
APPs most relevant to security (security of personal information, access and
correction, cross-border disclosure), and who the Act applies to.

**Key concepts:**
- Personal vs sensitive information
- The 13 Australian Privacy Principles (with a security focus on APP 11)
- Who is covered, and current reform directions

**Australian context:** The Privacy Act and APPs are the core Australian data
protection regime.

---

### Topic 3: Data Breaches — The NDB Scheme

The Notifiable Data Breaches (NDB) scheme requires organisations covered by the
Privacy Act to notify affected individuals and the OAIC of eligible data breaches
likely to result in serious harm. This topic covers what triggers notification,
the assessment timeline, the content of a notification, and the practitioner's
role in breach response. It links directly to OC04 (Incident Response).

**Key concepts:**
- What makes a breach "eligible" and "likely to result in serious harm"
- The 30-day assessment obligation and notification content
- The security practitioner's role in supporting NDB compliance

**Australian context:** The NDB scheme is administered by the OAIC and is central
to Australian incident response.

---

### Topic 4: Critical Infrastructure — The SOCI Act

The *Security of Critical Infrastructure Act 2018* (SOCI), as amended, imposes
obligations on responsible entities for critical infrastructure assets —
including risk management programs and mandatory cyber incident reporting to the
ACSC. This topic explains which sectors are covered, the reporting timeframes,
and why critical infrastructure carries heightened obligations.

**Key concepts:**
- Covered sectors and the concept of a responsible entity
- Mandatory incident reporting timeframes to the ACSC
- Risk management program obligations

**Australian context:** SOCI is a distinctively Australian regime reshaping
critical-infrastructure security obligations.

---

### Topic 5: Professional Ethics

Where the law is silent, ethics guides conduct. This topic covers professional
codes (e.g. AISA's code of conduct, (ISC)² and broader practitioner ethics),
responsible disclosure of vulnerabilities, conflicts of interest, and the
handling of sensitive data discovered during work. It develops the judgement to
act well in grey areas that legislation does not fully address.

**Key concepts:**
- Professional codes of conduct and their common themes
- Responsible/coordinated vulnerability disclosure
- Handling incidental discovery of sensitive or illegal material

**Australian context:** AISA (Australian Information Security Association) is
referenced as the leading Australian professional body.

---

### Topic 6: Regulators and Authorisation in Practice

This topic brings law and ethics into daily practice. It covers the roles of the
OAIC, ACSC/ASD, AFP, and sector regulators (e.g. APRA), how and when to engage
them, and — crucially — how authorisation works in real engagements: scope,
rules of engagement, written permission, and the consequences of scope creep. It
is the practical bridge to the offensive and investigative units.

**Key concepts:**
- Roles and powers of key Australian regulators
- Building a defensible authorisation: scope, RoE, written approval
- Scope creep and its legal consequences

**Australian context:** Directly covers the Australian regulator landscape.

---

## Labs & Exercises

### Lab 1: Drafting Rules of Engagement

**Objective:** Draft a rules-of-engagement / authorisation document for a
hypothetical internal security assessment, demonstrating how authorisation is
established lawfully.

**Prerequisites:**
- Topics 1, 5, and 6

**Environment:**
- Operating System: any (this is a documentation lab)
- Tools: a word processor or markdown editor (free)
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario: an organisation asks you to assess the security of its
   internal web portal.
2. Draft an authorisation/RoE document that includes: parties and signatories,
   in-scope and explicitly out-of-scope systems, permitted techniques, testing
   window, data-handling rules, and an emergency-stop contact.
3. Add a clause referencing the *Cybercrime Act 2001* to make clear that activity
   outside scope is unauthorised access.
4. Add a data-handling clause referencing Privacy Act / APP 11 obligations for
   any personal information encountered.
5. Identify three ways scope creep could occur and how the document prevents
   each.

**Expected Output:**

A complete, signable RoE document with clear scope boundaries, legal references,
and data-handling rules. Learners can explain why each clause exists and which
law or principle it protects against breaching.

**Reflection Questions:**

1. Why is written, scoped authorisation the single most important protection for
   a security professional under the Cybercrime Act?
2. How would the RoE change if the assessment involved a critical-infrastructure
   asset under SOCI?
3. What ethical obligations apply if you discover evidence of a real, unrelated
   crime during the assessment?

---

### Lab 2: Notifiable Data Breach Tabletop

**Objective:** Work through a simulated data breach and produce the assessment
and notification artefacts required under the NDB scheme.

**Prerequisites:**
- Topics 2, 3, and 6

**Environment:**
- Operating System: any
- Tools: the OAIC NDB guidance (free, online), a document editor
- Minimum hardware: trivial

**Instructions:**

1. Read the provided breach scenario (e.g. a misconfigured database exposing
   customer records).
2. Assess whether the breach is "eligible" and "likely to result in serious
   harm", documenting your reasoning against OAIC criteria.
3. Draft the statement that would be provided to the OAIC and to affected
   individuals, including the required content elements.
4. Build a short timeline showing the 30-day assessment obligation and key
   decision points.
5. Identify which other obligations might apply if the entity were also a SOCI
   responsible entity (parallel ACSC reporting).

**Expected Output:**

A documented eligibility assessment with reasoning, a draft OAIC/individual
notification meeting the required content, and a compliance timeline. Learners
can justify the notify/not-notify decision against OAIC criteria.

**Reflection Questions:**

1. What factors most influence whether a breach is "likely to result in serious
   harm"?
2. How do the NDB scheme and SOCI reporting obligations interact for a critical
   infrastructure entity?
3. How does early, well-documented incident response (OC04) make NDB compliance
   easier?

---

## Assessment

### Formative Assessment: Legal Scenario Spotting

**Type:** Short-answer scenario exercise with answer key

**Description:** Students are given short vignettes (e.g. "a colleague scans a
partner's network without asking") and must identify the law/principle at issue
and whether the conduct is lawful/ethical. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3, LO5

**Feedback mechanism:** Answer key identifying the relevant law/principle and the
reasoning for each vignette.

---

### Summative Assessment: Compliance & Ethics Case Study

**Type:** Case-study analysis report

**Description:** Students analyse a realistic scenario in which an organisation
suffers an incident with legal, privacy, and ethical dimensions. They must (a)
identify all applicable Australian legislation and obligations, (b) determine
notification requirements under the NDB scheme (and SOCI if applicable), (c)
assess any ethical issues in the organisation's response, and (d) recommend a
compliant, ethical course of action. Deliverable: 1,500–2,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Identification of applicable law | LO1, LO3 |
| NDB / SOCI notification analysis | LO2, LO6 |
| Ethical analysis & recommendation | LO5 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Legal accuracy | Identifies all relevant laws/obligations correctly | Identifies most with minor gaps | Identifies some; notable omissions | Misidentifies or omits key law |
| Regulatory/notification analysis | Correct, well-reasoned notification decisions | Mostly correct with small gaps | Partial or weakly reasoned | Incorrect notification analysis |
| Ethical reasoning | Nuanced, principled, well-justified | Sound ethical analysis | Basic, surface-level analysis | Little or no ethical reasoning |
| Communication | Clear, structured, professional | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit is Australian context throughout. Key elements:

- **Cybercrime Act 2001 (Cth):** The basis for the authorisation requirement that
  governs all offensive/investigative work in the degree (Topic 1, Lab 1).
- **Privacy Act 1988 (Cth) & Australian Privacy Principles:** The data protection
  regime, with APP 11 (security) emphasised (Topic 2).
- **Notifiable Data Breaches scheme (OAIC):** Breach assessment and notification
  obligations practised in Lab 2.
- **Security of Critical Infrastructure Act 2018 (Cth):** Critical-infrastructure
  obligations and ACSC reporting (Topic 4).
- **Regulators:** OAIC, ACSC/ASD, AFP, APRA roles and powers (Topic 6).
- **AISA:** The Australian professional body referenced for ethics (Topic 5).

---

## Further Reading

**Office of the Australian Information Commissioner (2024).** *Australian Privacy Principles & Data Breach Preparation and Response guides.* OAIC. https://www.oaic.gov.au
> Relevance: The authoritative source for the Privacy Act, APPs, and NDB scheme central to this unit (Australian source).

**Australian Government (2018).** *Security of Critical Infrastructure Act 2018 (Cth).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The primary legislation behind Topic 4; students should read the current consolidated version (Australian source).

**Australian Government (2001).** *Cybercrime Act 2001 (Cth) & Criminal Code computer offences.* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The legal foundation for the authorisation concept underpinning the entire degree (Australian source).

**Australian Information Security Association (2024).** *AISA Code of Conduct.* AISA. https://www.aisa.org.au
> Relevance: The leading Australian professional body's ethics code, used in Topic 5 (Australian source).

**Cyber Security Cooperative Research Centre / academic commentary (2023).** *Australian cyber law and policy analyses.* (Freely available CSCRC publications.) https://cybersecuritycrc.org.au
> Relevance: Accessible Australian analysis connecting legislation to practice for the case-study assessment (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F05 |
| Unit Title | Legal, Ethics & Australian Compliance |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Cybercrime Act 2001; Privacy Act 1988 (APPs, NDB scheme); Security of Critical Infrastructure Act 2018 |
