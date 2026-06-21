# OC04: Incident Response Lifecycle

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches students to respond to security incidents in a structured,
repeatable way using the established incident-response (IR) lifecycle. It covers
preparation, detection and analysis, containment, eradication, recovery, and
post-incident activity — anchored in **NIST SP 800-61** and the **PICERL** model —
and connects each phase to the threat-informed defense loop that runs through the
operational core: every incident yields TTPs and lessons that should update
detections, logging, infrastructure, and automation. Students also learn the
human side of IR: coordination, communication, evidence handling, and a blameless
post-incident review culture that turns incidents into durable improvement.

In the Australian context, IR is tightly bound to legal obligations: the
Notifiable Data Breaches scheme (OAIC) and mandatory incident reporting under the
SOCI Act both depend on competent, well-documented response. OC04 builds on F05
(Legal/Ethics), F06 (Data & Log Analysis), and OC02 (Security Monitoring), and is
a prerequisite for the DFIR major.

---

## Prerequisites

- F05 — Legal, Ethics & Australian Compliance
- F06 — Data & Log Analysis
- OC02 — Security Monitoring & SIEM

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the incident-response lifecycle (NIST SP 800-61 / PICERL) to a
   realistic incident scenario.
2. **Analyse** evidence across host, network, and log sources to scope an incident
   and establish a timeline.
3. **Apply** containment, eradication, and recovery actions appropriate to an
   incident's nature and business context.
4. **Examine** the legal and regulatory obligations triggered by an incident in
   the Australian context (NDB, SOCI).
5. **Apply** evidence-handling and chain-of-custody practices suitable for
   potential legal proceedings.
6. **Analyse** an incident in a blameless post-incident review and derive
   improvements that feed the threat-informed defense loop.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of the IR
lifecycle, evidence handling, and the Australian legal context of incident
response.

**Skills (AQF 7.2):** Students develop analytical skills by scoping incidents and
building timelines, and communication skills through coordination and reporting.

**Application (AQF 7.3):** Students apply the lifecycle to realistic scenarios,
meeting Australian notification obligations and producing improvements that
strengthen ongoing defence.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Incident Responder | PR-CIR-001 | T0041 | Coordinate and perform incident handling across the response lifecycle | Lab 1 — Incident Response Tabletop |
| NIST NICE DCWF | 2023 | Cyber Defense Incident Responder | PR-CIR-001 | T0278 | Collect and preserve evidence and establish an incident timeline | Lab 2 — Scoping & Timeline with Chain of Custody |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Incident management | USUP | Level 4 | Lab 1 |
| Security operations | SCAD | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Incident Management | Incident Response | Practitioner | Lab 1, Lab 2 |

---

## Topics

### Topic 1: The IR Lifecycle and Preparation

Incident response succeeds or fails on preparation. This topic introduces the
NIST SP 800-61 lifecycle and the PICERL model, the IR plan, roles (incident
commander, analysts, comms, legal), runbooks, and the tooling and access an IR
team needs in place *before* an incident. It frames preparation as the phase that
determines how every other phase will go.

**Key concepts:**
- NIST SP 800-61 lifecycle and PICERL
- IR plans, roles, and runbooks
- Readiness: tooling, access, and retainers

**Australian context:** Preparation includes pre-agreed notification paths for the
NDB scheme and SOCI reporting.

---

### Topic 2: Detection, Triage, and Analysis

This phase turns an alert into an understood incident. Building on OC02, it covers
validating and triaging alerts, scoping (which hosts, accounts, and data are
involved), and analysis to determine the adversary's actions in ATT&CK terms.
Accurate scoping is the hinge on which containment and notification decisions
turn.

**Key concepts:**
- Validation, triage, and severity classification
- Scoping the blast radius across hosts, accounts, and data
- Analysis and ATT&CK characterisation of adversary actions

---

### Topic 3: Containment, Eradication, and Recovery

This topic covers the decisions at the heart of response: short- and long-term
containment (isolate vs observe), eradication (removing persistence and access),
and recovery (safely restoring operations and verifying the threat is gone). It
stresses the trade-offs — e.g. immediate isolation vs preserving intelligence —
and aligning actions to business impact.

**Key concepts:**
- Short- vs long-term containment and the observe/isolate trade-off
- Eradicating persistence and revoking adversary access
- Recovery, validation, and avoiding reinfection

---

### Topic 4: Evidence Handling and Chain of Custody

Incidents can become legal matters. This topic covers sound evidence handling:
order of volatility, forensic imaging principles, hashing for integrity, and
chain-of-custody documentation. It links to the *Australian Evidence Act 1995* and
the standards that make evidence admissible, reinforcing F05.

**Key concepts:**
- Order of volatility and sound acquisition
- Integrity through hashing and documentation
- Chain of custody and admissibility (Evidence Act 1995)

**Australian context:** Evidence handling is tied to Australian admissibility
requirements.

---

### Topic 5: Legal Obligations and Communication

Response is also a communication and compliance exercise. This topic covers
internal and external communication, working with legal and executives, and the
Australian notification obligations: assessing and reporting eligible data
breaches under the NDB scheme and mandatory cyber-incident reporting to the ACSC
under the SOCI Act, including timeframes.

**Key concepts:**
- Stakeholder and crisis communication
- NDB scheme assessment and notification (OAIC)
- SOCI Act incident reporting to the ACSC and timeframes

**Australian context:** This topic is largely Australian legal obligation in
practice.

---

### Topic 6: Post-Incident Activity and the Defensive Loop

The final phase is where organisations either learn or repeat. This topic covers
post-incident review, including a **blameless review culture** that focuses on
systems and process rather than individual fault, and the practice of converting
findings into concrete improvements — new detections, log sources, hardening, and
automation. This is the explicit hand-back to the threat-informed defense loop:
the incident's TTPs update OC01/OC02 coverage.

**Key concepts:**
- Blameless post-incident review (as part of lessons-learned)
- From findings to detection, logging, and automation changes
- Feeding incident-derived TTPs back into threat-informed defense

**Australian context:** Lessons learned feed both internal defence and ACSC
information-sharing.

---

## Labs & Exercises

### Lab 1: Incident Response Tabletop

**Objective:** Run a structured tabletop exercise through the full IR lifecycle for
a realistic Australian-context incident, making and documenting phase decisions.

**Prerequisites:**
- Topics 1, 3, 5, and 6

**Environment:**
- Operating System: any (facilitated exercise)
- Tools: the provided scenario pack, an IR plan template, a decision log (free)
- Minimum hardware: trivial

**Instructions:**

1. Assign roles (incident commander, analyst, comms, legal/compliance).
2. Work through the injected scenario (e.g. ransomware affecting an Australian
   mid-size firm) phase by phase.
3. At each phase, record the decision made and its justification in a decision
   log.
4. At the detection/analysis phase, characterise the adversary actions in ATT&CK
   terms.
5. At the legal phase, decide whether the NDB scheme is triggered and whether SOCI
   reporting applies, with reasoning and timeframes.
6. Conclude with a blameless lessons-learned discussion and list three defensive
   improvements.

**Expected Output:**

A completed decision log across all phases, an NDB/SOCI determination with
reasoning, and three defensive improvements mapped to detections/logging/
automation. Learners can justify each major decision.

**Reflection Questions:**

1. Which phase was hardest to decide in, and what information would have helped?
2. How did the NDB/SOCI obligations shape your containment and communication
   timing?
3. Which lessons-learned improvement would most reduce the chance or impact of a
   recurrence?

---

### Lab 2: Scoping & Timeline with Chain of Custody

**Objective:** Scope a simulated intrusion from evidence, build a defensible
timeline, and maintain chain of custody.

**Prerequisites:**
- Topics 2 and 4 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: the SIEM/log platform from OC02, hashing utilities, a chain-of-custody
  template — all free/OSS
- Minimum hardware: 6 GB RAM / 2 vCPU / 30 GB disk (within spec; no GPU)

**Instructions:**

1. Receive the provided evidence set (disk artefacts/log exports) and record each
   item in a chain-of-custody form with hashes.
2. Scope the incident: identify affected hosts, accounts, and data from the
   evidence.
3. Build a chronological, multi-source timeline of the adversary's actions
   (reuse F06 correlation skills), mapping actions to ATT&CK.
4. Determine the likely initial access and the extent of compromise.
5. Identify which data was affected and assess NDB "serious harm" likelihood.
6. Produce a short incident report with the timeline, scope, and a chain-of-custody
   appendix.

**Expected Output:**

A chain-of-custody record with verified hashes, a scoped multi-source timeline
mapped to ATT&CK, and an incident report with an NDB harm assessment. Each
timeline entry cites its evidence.

**Reflection Questions:**

1. How did maintaining chain of custody constrain how you handled the evidence?
2. Where were the gaps in the available telemetry, and how would better logging
   (OC02) have changed your timeline?
3. How does your scope determination affect the NDB notification decision?

---

## Assessment

### Formative Assessment: Phase Decision Drills

**Type:** Scenario exercise with answer key

**Description:** Students are given short incident injects and must state the
correct IR phase, the appropriate next action, and any Australian legal trigger.
Self-marked.

**Learning Outcomes Assessed:** LO1, LO4

**Feedback mechanism:** Answer key with the model action and legal trigger for
each inject.

---

### Summative Assessment: Incident Response Report & Improvement Plan

**Type:** Practical report

**Description:** From a provided multi-source evidence set and scenario, students
produce a full IR report that (a) walks the lifecycle decisions taken, (b)
presents a scoped, ATT&CK-mapped timeline with chain of custody, (c) determines
NDB and (if applicable) SOCI obligations with timeframes, and (d) delivers a
blameless post-incident review with a prioritised improvement plan that updates
detections, logging, and automation. Deliverable: 2,500–3,000 word report with a
chain-of-custody appendix.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Lifecycle decision narrative | LO1, LO3 |
| Scoped timeline + chain of custody | LO2, LO5 |
| NDB/SOCI determination | LO4 |
| Blameless review + improvement plan | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Lifecycle application | All phases handled correctly with justified decisions | Mostly correct with minor gaps | Several phase errors | Lifecycle misapplied |
| Evidence & timeline | Precise, well-evidenced timeline; sound custody | Solid timeline with small gaps | Partial timeline; weak custody | Poor timeline/custody |
| Legal/regulatory analysis | Correct, well-reasoned NDB/SOCI determination | Mostly correct determination | Partial or weakly reasoned | Incorrect determination |
| Improvement & defensive loop | Insightful, prioritised, blameless; clearly feeds TID | Solid improvements | Generic improvements | Little or no improvement plan |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Notifiable Data Breaches scheme (OAIC):** Assessment and notification decisions
  are made in both labs and the summative report.
- **Security of Critical Infrastructure Act 2018:** Mandatory ACSC incident
  reporting and timeframes are applied where the scenario entity is in scope.
- **Australian Evidence Act 1995:** Underpins the evidence-handling and chain-of-
  custody practices in Topic 4 and Lab 2.

---

## Further Reading

**NIST (2012, r2 forthcoming).** *SP 800-61 — Computer Security Incident Handling Guide.* NIST. https://csrc.nist.gov/pubs/sp/800/61
> Relevance: The authoritative incident-handling lifecycle anchoring this unit.

**SANS (2024).** *Incident Handler's Handbook & incident-response process guidance.* SANS Institute. https://www.sans.org/white-papers/
> Relevance: Practitioner-oriented detail on the PICERL phases used throughout the unit.

**Office of the Australian Information Commissioner (2024).** *Data breach preparation and response.* OAIC. https://www.oaic.gov.au
> Relevance: The authoritative source for NDB assessment and notification practised in the labs (Australian source).

**Australian Cyber Security Centre (2024).** *Cyber incident response & SOCI reporting guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian guidance on incident response and mandatory reporting timeframes (Australian source).

**Luttgens, J., Pepe, M. & Mandia, K. (2014).** *Incident Response & Computer Forensics (3rd ed.).* McGraw-Hill.
> Relevance: Deep practitioner reference for scoping, evidence handling, and timelines (Lab 2).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | OC04 |
| Unit Title | Incident Response Lifecycle |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Operational Core |
| Major / Pathway | Operational |
| Prerequisites | F05, F06, OC02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | Privacy Act 1988 (NDB scheme); Security of Critical Infrastructure Act 2018; Evidence Act 1995 |
