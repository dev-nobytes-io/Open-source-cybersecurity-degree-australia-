# OC06: Offensive Security Concepts

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit introduces offensive security from a defender's perspective: to defend
effectively you must understand how attacks are actually carried out. It covers the
penetration-testing and adversary-emulation mindset, the phases of an engagement,
common attack techniques against networks, web applications, and identity, and —
crucially — how offensive activity is conducted **legally, ethically, and within
scope**. Consistent with the operational core's threat-informed defense theme, the
unit frames offence as a way to *validate* defence: emulating real adversary TTPs
(MITRE ATT&CK) and CTID adversary-emulation methodology tells defenders whether
their detections, logging, and controls actually work.

The unit is deliberately concept- and authorisation-led. Every technique is taught
inside an isolated lab under explicit authorisation, anchored to the *Cybercrime
Act 2001* and the rules-of-engagement discipline from F05. OC06 builds on F04, F05,
and OC01, and is the gateway to the Cyber Threat Emulation (CTE) major and a
strong complement to the Threat Hunting and Detection Engineering majors.

---

## Prerequisites

- F04 — Security Concepts & Principles
- F05 — Legal, Ethics & Australian Compliance
- OC01 — Adversary Tradecraft & TTPs

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** the legal and ethical framework for authorised offensive security in
   Australia and construct appropriate rules of engagement.
2. **Apply** the phases of a penetration test / adversary emulation engagement.
3. **Demonstrate** common reconnaissance, exploitation, and post-exploitation
   techniques in an isolated lab.
4. **Apply** MITRE ATT&CK and CTID adversary-emulation methodology to plan and
   execute behaviour-based emulation.
5. **Analyse** offensive results to validate defensive coverage and recommend
   detection and control improvements.
6. **Examine** the purple-team model as a continuous loop that strengthens
   threat-informed defense.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of offensive
techniques, engagement methodology, and the legal/ethical framework governing them.

**Skills (AQF 7.2):** Students develop technical skills by executing techniques in
a controlled lab and analytical skills by translating results into defensive
improvement.

**Application (AQF 7.3):** Students apply offensive methods within an authorised,
Australian-legal framework to validate and improve real defences.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Vulnerability Assessment Analyst | PR-VAM-001 | T0028 | Conduct authorised assessments to identify and exploit vulnerabilities | Lab 1 — Authorised Engagement in an Isolated Lab |
| NIST NICE DCWF | 2023 | Exploitation Analyst | AN-EXP-001 | T0591 | Apply adversary emulation to validate defensive coverage | Lab 2 — ATT&CK-Based Emulation & Purple Teaming |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Penetration testing | PENT | Level 4 | Lab 1, Lab 2 |
| Information security | SCTY | Level 4 | Throughout |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Offensive Cyber | Authorised Testing & Emulation | Practitioner | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | OC06-K01 | Knowledge of the legal/ethical framework and rules of engagement for authorised offensive security in Australia | Topic 1 |
| Knowledge | OC06-K02 | Knowledge of penetration-test / adversary-emulation engagement methodology | Topic 2 |
| Knowledge | OC06-K03 | Knowledge of reconnaissance, exploitation, and post-exploitation techniques | Topic 3; Topic 4 |
| Knowledge | OC06-K04 | Knowledge of the purple-team model as a continuous improvement loop | Topic 6 |
| Skill | OC06-S01 | Skill in conducting an authorised engagement in an isolated lab | Lab 1 |
| Skill | OC06-S02 | Skill in planning and running ATT&CK-based emulation and purple teaming | Lab 2 |
| Ability | OC06-A01 | Ability to analyse offensive results to validate defensive coverage | Lab 2; Topic 5 |
| Ability | OC06-A02 | Ability to recommend defensive improvements from emulation findings | Summative |
| Task | T0028 | Conduct authorised assessments to identify and exploit vulnerabilities | Lab 1 |
| Task | T0591 | Apply adversary emulation to validate defensive coverage | Lab 2 |

---

## Topics

### Topic 1: Authorisation, Ethics, and Rules of Engagement

Offensive security without authorisation is a crime. This topic — the
non-negotiable foundation — covers the legal framework (*Cybercrime Act 2001*),
scoping, rules of engagement, written permission, safe-handling of findings, and
responsible disclosure. It extends F05 into the offensive context, where the
margin for error is smallest.

**Key concepts:**
- Authorisation as the line between testing and crime
- Scope, rules of engagement, and emergency-stop
- Responsible disclosure and handling sensitive findings

**Australian context:** Grounded in the Cybercrime Act 2001 and F05 authorisation
practice.

---

### Topic 2: Engagement Methodology

Offensive work follows a methodology. This topic covers the phases — planning and
scoping, reconnaissance, vulnerability identification, exploitation, post-
exploitation, and reporting — and contrasts vulnerability assessment, penetration
testing, red teaming, and adversary emulation, including when each is appropriate.

**Key concepts:**
- Engagement phases from scoping to reporting
- Vulnerability assessment vs pentest vs red team vs emulation
- Choosing the right type for the objective

---

### Topic 3: Reconnaissance and Initial Access

This topic covers how adversaries gather information and gain a foothold: passive
and active reconnaissance, service and vulnerability enumeration, common initial-
access vectors (phishing concepts, exposed services, weak credentials), all
demonstrated against isolated lab targets and mapped to ATT&CK initial-access
techniques.

**Key concepts:**
- Passive vs active reconnaissance
- Enumeration and vulnerability identification
- Initial-access vectors (ATT&CK Initial Access)

---

### Topic 4: Exploitation and Post-Exploitation

This topic covers turning a foothold into impact: exploitation fundamentals,
privilege escalation, credential access, lateral movement, and persistence —
emphasising the defender's view of what each leaves behind. Tooling (e.g.
Metasploit, much of whose tooling and modules are extensible in Lua, per F03) is
used in the lab, always against authorised targets.

**Key concepts:**
- Exploitation and privilege escalation
- Credential access and lateral movement
- Persistence and the artefacts each technique generates

**Australian context:** Techniques are mapped to the behaviours ACSC advisories
report in real Australian intrusions.

---

### Topic 5: Adversary Emulation and Validating Defence

This is where offence serves threat-informed defense. This topic teaches building
and executing an adversary-emulation plan from real actor TTPs using the **CTID
Adversary Emulation Library** and ATT&CK, then comparing what the emulation did
against what the defence detected. The output is a coverage validation: which
techniques were seen, which were missed, and why.

**Key concepts:**
- Building emulation plans from real actor TTPs (CTID library)
- Executing emulation safely in a lab
- Comparing emulated behaviour against detection (coverage validation)

---

### Topic 6: Purple Teaming and the Continuous Loop

The unit culminates in the purple-team model: red and blue working together so
that every emulated technique either confirms a detection or produces a new one.
This topic frames purple teaming as the mechanism that keeps detections, logging,
infrastructure, and automation honest against a changing adversary — the offensive
half of the living, threat-informed defence loop.

**Key concepts:**
- The purple-team model and feedback loop
- From a missed technique to a new detection (hand-off to OC02)
- Continuous validation as adversary behaviour evolves

**Australian context:** Connects to TIBER-AU-style intelligence-led testing as the
mature Australian expression of emulation (previewing the CTE major).

---

## Labs & Exercises

### Lab 1: Authorised Engagement in an Isolated Lab

**Objective:** Execute a small authorised engagement against a deliberately
vulnerable target in an isolated lab, following methodology and rules of
engagement.

**Prerequisites:**
- Topics 1–4

**Environment:**
- Operating System: Kali Linux (free) attacker VM + a deliberately vulnerable
  target VM (e.g. Metasploitable / a vulnerable web app), on a **host-only/internal
  network**
- Tools: nmap, a web proxy (e.g. OWASP ZAP), Metasploit Framework — all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 30 GB disk total (within the 8 GB /
  4-core / 50 GB spec; no GPU). **Isolated network only — no external targets.**

**Instructions:**

1. Write a short rules-of-engagement note for the lab defining scope (the target
   VM only), permitted techniques, and an emergency stop. Confirm isolation.
2. Reconnaissance: enumerate the target's services with nmap; record findings.
3. Identify a vulnerability in an exposed service or the web app.
4. Exploit it in the lab to gain access; document each step and the ATT&CK
   technique it represents.
5. Perform one post-exploitation action (e.g. enumerate users) and note the
   artefacts it would leave.
6. Write a concise engagement report: findings, evidence, ATT&CK mapping, and
   remediation recommendations.

**Expected Output:**

A rules-of-engagement note, a documented kill-chain from recon to post-
exploitation with ATT&CK mappings, and a remediation-focused report. Learners
explicitly confirm all activity stayed within the isolated lab.

**Reflection Questions:**

1. Which of your actions would a defender most easily detect, and which would be
   hardest? (Links to OC02.)
2. How did operating under rules of engagement change how you worked?
3. What is the single remediation that would most reduce this target's risk?

---

### Lab 2: ATT&CK-Based Emulation & Purple Teaming

**Objective:** Build and run a small ATT&CK-based emulation, then validate
detection coverage as a purple-team exercise.

**Prerequisites:**
- Topics 5 and 6 and Lab 1; access to the SIEM from OC02

**Environment:**
- Operating System: the Lab 1 attacker/target VMs plus the OC02 SIEM ingesting the
  target's telemetry
- Tools: CTID Adversary Emulation Library plan, ATT&CK Navigator, the SIEM, an
  emulation tool (e.g. Atomic Red Team / Caldera — free/OSS)
- Minimum hardware: as Lab 1 (run components sequentially if RAM-constrained)

**Instructions:**

1. Select a small set of techniques from a CTID adversary-emulation plan relevant
   to an Australian-sector scenario.
2. Ensure the target's telemetry is flowing to the SIEM (reuse OC02 detections).
3. Execute each emulated technique in the isolated lab.
4. For each technique, record whether the SIEM detected it (and which detection
   fired) — produce a Navigator layer coloured by detected/missed.
5. For one missed technique, author a new detection (Sigma) that would catch it.
6. Write a purple-team report: coverage results, the new detection, and
   recommended logging/automation changes.

**Expected Output:**

A coverage Navigator layer (detected vs missed), evidence of detections firing, at
least one new detection for a missed technique, and a purple-team report. Learners
can trace each missed technique to a concrete defensive improvement.

**Reflection Questions:**

1. Which techniques were missed, and what was the root cause — missing telemetry or
   missing detection?
2. How does running this emulation periodically keep the defence aligned with a
   changing adversary?
3. How would TIBER-AU-style intelligence-led testing scale this approach for a
   regulated Australian organisation?

---

## Assessment

### Formative Assessment: Scope & Legality Check

**Type:** Scenario exercise with answer key

**Description:** Students are given proposed offensive activities and must judge,
for each, whether it is in scope and lawful given a sample RoE, and what would make
it compliant. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Answer key with the compliance judgement and reasoning for
each scenario.

---

### Summative Assessment: Emulation & Defensive Validation Report

**Type:** Practical report

**Description:** Students plan and execute (in the isolated lab) a small,
authorised ATT&CK-based emulation against a target wired to the OC02 SIEM, then (a)
present a rules-of-engagement note, (b) document the emulated techniques with
ATT&CK mappings, (c) validate detection coverage (detected vs missed), (d) author
at least one new detection for a gap, and (e) recommend prioritised detection,
logging, and automation improvements framed as a purple-team loop. Deliverable:
2,000–2,500 word report with Navigator artefacts and the new detection.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Rules of engagement | LO1, LO2 |
| Emulation execution + ATT&CK mapping | LO3, LO4 |
| Coverage validation + new detection | LO5 |
| Purple-team improvement plan | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Authorisation & ethics | Rigorous RoE, fully scoped and lawful | Adequate RoE and scope | Minor scope/ethics gaps | Unsafe or unauthorised activity |
| Technique execution | Correct, well-documented, ATT&CK-mapped | Mostly correct execution | Partial or weakly mapped | Incorrect or undocumented |
| Coverage validation | Precise detected/missed analysis with root cause | Solid coverage analysis | Partial analysis | Little meaningful validation |
| Defensive improvement | Strong new detection(s); prioritised, loop-framed | Workable improvements | Generic improvements | Little or no improvement |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Cybercrime Act 2001 (Cth):** The legal basis for authorisation, central to
  Topic 1 and both labs.
- **ACSC advisories:** Source of real Australian adversary TTPs for emulation.
- **TIBER-AU:** Introduced as the mature, intelligence-led Australian testing
  framework that scales emulation (preview of the CTE major).

---

## Further Reading

**MITRE Center for Threat-Informed Defense (2024).** *Adversary Emulation Library & Attack Flow.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: The emulation plans and methodology used in Topic 5 and Lab 2; free/OSS.

**Red Canary (2024).** *Atomic Red Team.* https://github.com/redcanaryco/atomic-red-team
> Relevance: The free, ATT&CK-mapped test library used for safe technique emulation in Lab 2.

**OWASP (2024).** *Web Security Testing Guide & ZAP.* https://owasp.org/www-project-web-security-testing-guide/
> Relevance: The free methodology and tooling for the web-application testing in Lab 1.

**Australian Cyber Security Centre (2024).** *Threat advisories & TIBER-AU information.* ACSC / RBA. https://www.cyber.gov.au
> Relevance: Australian adversary TTPs and the intelligence-led testing context (Australian source).

**Penetration Testing Execution Standard (PTES) / OSSTMM (2024).** *Testing methodologies.* http://www.pentest-standard.org
> Relevance: Freely available engagement methodologies supporting Topic 2.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | OC06 |
| Unit Title | Offensive Security Concepts |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Operational Core |
| Major / Pathway | Operational |
| Prerequisites | F04, F05, OC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | Cybercrime Act 2001 (Cth) |
