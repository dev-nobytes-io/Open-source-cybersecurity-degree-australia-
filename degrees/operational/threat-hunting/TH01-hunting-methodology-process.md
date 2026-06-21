# TH01: Hunting Methodology & Process

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Threat hunting is the proactive, analyst-driven search for adversary activity that
has evaded automated detection. This unit establishes the *discipline* behind it:
how to run hunts as a repeatable, documented process rather than ad-hoc poking
around. It centres on the **TaHiTI** (Targeted Hunting integrating Threat
Intelligence) methodology, hypothesis design, the hunt loop, and the documentation
and metrics that make hunting a maturing capability. It is the methodological
foundation for the rest of the Threat Hunting major.

The unit is built on the threat-informed defense thinking from the operational
core: hunts are driven by intelligence about real adversary behaviour (MITRE
ATT&CK v19, CTID research, ACSC advisories), and their output feeds detection,
logging, and automation. In the Australian context, mature hunting helps
organisations meet ASD Essential Eight expectations and SOCI detection
obligations. TH01 builds on OC01 (Adversary Tradecraft) and OC02 (Security
Monitoring) and precedes the technique- and data-specific units TH02–TH05.

---

## Prerequisites

- OC01 — Adversary Tradecraft & TTPs
- OC02 — Security Monitoring & SIEM
- OC05 — Threat Intelligence Fundamentals

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** a threat scenario to formulate a testable, intelligence-driven hunt
   hypothesis using the TaHiTI methodology.
2. **Evaluate** hunt methodologies (TaHiTI, PEAK, the hunting maturity model) and
   select an appropriate approach for a given organisation.
3. **Design** a structured hunt plan with scope, data requirements, and success
   criteria.
4. **Analyse** the relationship between hunting, detection engineering, and
   intelligence in a continuous loop.
5. **Recommend** improvements to an organisation's hunting maturity based on a
   structured assessment.
6. **Evaluate** the outputs of a hunt and justify which findings should become
   detections.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of hunting
methodology, hypothesis design, and hunt-program maturity.

**Skills (AQF 7.2):** Students develop high-order cognitive skills by formulating
and evaluating hypotheses and critiquing methodologies.

**Application (AQF 7.3):** Students apply methodology to design defensible hunt
plans for realistic Australian organisations and recommend maturity improvements.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0569 | Apply cyber threat frameworks to drive hunting against adversary behaviour | Lab 1 — Hunt Hypothesis with TaHiTI |
| NIST NICE DCWF | 2023 | Threat/Warning Analyst | AN-TWA-001 | T0707 | Analyse threat information to plan and prioritise hunts | Lab 2 — Hunt Program Maturity Assessment |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Threat Hunting | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: What Hunting Is (and Is Not)

This topic positions hunting against reactive monitoring and alert triage. Hunting
assumes a breach and proactively seeks it; it is hypothesis-led, not alert-led. The
topic covers the value proposition (finding what automation misses, improving
detections, understanding the environment) and the conditions under which hunting
is worthwhile.

**Key concepts:**
- Hunting vs alerting vs incident response
- The "assume breach" mindset
- When hunting pays off (and when to invest in detection instead)

---

### Topic 2: The TaHiTI Methodology

TaHiTI structures hunting into three phases — initiate (from a trigger/hypothesis),
hunt (investigate via abstract → concrete analytics), and finalise (document and
hand off). This topic teaches the full TaHiTI process, the hunt backlog, and how
threat intelligence (PIRs from OC05) feeds the trigger phase.

**Key concepts:**
- TaHiTI three phases and the hunt backlog
- Intelligence-driven triggers (linking to PIRs)
- Abstract-to-concrete investigation

**Australian context:** ACSC advisories are framed as a primary trigger source for
the initiate phase.

---

### Topic 3: Designing a Hunt Hypothesis

A hunt is only as good as its hypothesis. This topic teaches writing hypotheses
that are specific, testable, and tied to adversary behaviour — e.g. "an adversary
is using scheduled tasks (T1053) for persistence on domain controllers". It covers
hypothesis sources (intelligence, anomalies, crown-jewel analysis) and avoiding
hypotheses that cannot be tested with available data.

**Key concepts:**
- Specific, testable, behaviour-linked hypotheses
- Hypothesis sources and prioritisation
- Matching hypotheses to available data

---

### Topic 4: The Hunt Loop and Data Requirements

This topic covers running the hunt: identifying the data sources needed, scoping,
iterating between broad and narrow queries, and recognising when to pivot,
conclude, or escalate to incident response. It connects to the visibility/data-
source thinking from OC01/OC02.

**Key concepts:**
- Data requirements and visibility gaps
- Iterating: broaden, narrow, pivot
- Escalation to IR vs continuation

---

### Topic 5: Documentation, Metrics, and Maturity

Hunting that is not documented cannot be repeated or improved. This topic covers
the hunt report, the reusable hunt (turning a successful hunt into a repeatable
playbook or detection), hunt metrics (coverage, findings, detections created), and
maturity models (the Hunting Maturity Model; the PEAK framework) for assessing and
growing a program.

**Key concepts:**
- Hunt documentation and reusable playbooks
- Meaningful hunt metrics (not vanity)
- Hunting Maturity Model / PEAK

---

### Topic 6: Closing the Loop — Hunt to Detection to Intelligence

This topic frames hunting as part of a continuous cycle: findings become Sigma
detections (OC02), enrich intelligence and PIRs (OC05), and inform emulation
(OC06). It teaches deciding which findings warrant a durable detection (high on the
Pyramid of Pain) versus a one-off note.

**Key concepts:**
- Hunt findings → detections (hand-off to OC02)
- Hunt findings → intelligence and PIR refinement
- Choosing what to operationalise

**Australian context:** Operationalised findings strengthen Essential Eight-aligned
detection and SOCI detection obligations.

---

## Labs & Exercises

### Lab 1: Hunt Hypothesis with TaHiTI

**Objective:** Use TaHiTI to turn an Australian-relevant threat scenario into a
documented, testable hunt hypothesis and plan.

**Prerequisites:**
- Topics 2–4

**Environment:**
- Operating System: any (analysis lab)
- Tools: a hunt-plan template, ATT&CK Navigator (v19), an ACSC advisory (free)
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Select a recent ACSC advisory describing a threat actor or campaign.
2. Apply TaHiTI's initiate phase: define the trigger and a prioritised hypothesis.
3. Map the relevant ATT&CK (v19) techniques to the hypothesis in Navigator.
4. Specify the data sources required to test it and identify any visibility gaps.
5. Define success criteria and what a positive/negative result would mean.
6. Document the plan in the hunt-plan template.

**Expected Output:**

A TaHiTI-structured hunt plan: trigger, testable hypothesis, ATT&CK mapping, data
requirements, visibility gaps, and success criteria. Learners can defend why the
hypothesis is testable with the available data.

**Reflection Questions:**

1. How did intelligence (the advisory) sharpen your hypothesis versus a generic
   hunt?
2. Which visibility gap most threatens your ability to test the hypothesis?
3. Which outcome of this hunt would justify a new detection, and why?

---

### Lab 2: Hunt Program Maturity Assessment

**Objective:** Assess a scenario organisation's hunting maturity and recommend
improvements.

**Prerequisites:**
- Topics 5 and 6

**Environment:**
- Operating System: any
- Tools: a maturity-model reference (Hunting Maturity Model / PEAK), a worksheet
- Minimum hardware: trivial

**Instructions:**

1. Read the scenario describing an organisation's current hunting practices, data,
   and tooling.
2. Assess its current maturity level against the Hunting Maturity Model and note
   evidence.
3. Identify the two biggest constraints (e.g. data coverage, automation, skills).
4. Recommend a prioritised set of improvements to raise maturity by one level.
5. Define metrics to track whether maturity is improving.
6. Tie at least one recommendation to closing the hunt→detection loop.

**Expected Output:**

A maturity assessment with evidence, prioritised improvement recommendations, and
tracking metrics. Learners can justify the realistic next maturity level.

**Reflection Questions:**

1. Why is data coverage usually the binding constraint on hunting maturity?
2. How would you avoid vanity metrics in measuring hunt value?
3. How does maturity in hunting reinforce threat-informed defense overall?

---

## Assessment

### Formative Assessment: Hypothesis Critique

**Type:** Self/peer review exercise with answer key

**Description:** Students critique a set of draft hunt hypotheses for specificity,
testability, and behaviour linkage, and rewrite the weak ones. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with a model critique and rewrite for each
hypothesis.

---

### Summative Assessment: Hunt Plan & Maturity Brief

**Type:** Analytical report

**Description:** For an assigned Australian organisation and threat profile,
students produce (a) a TaHiTI-structured hunt plan with ATT&CK mapping and data
requirements, (b) a maturity assessment of the organisation's hunting capability,
and (c) a prioritised improvement roadmap that closes the hunt→detection→
intelligence loop. Deliverable: 2,500–3,000 word report with a Navigator layer.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| TaHiTI hunt plan | LO1, LO3 |
| Methodology selection & loop analysis | LO2, LO4 |
| Maturity assessment & roadmap | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Hypothesis & plan | Sharp, testable, well-scoped, intelligence-driven | Sound plan with minor gaps | Vague or weakly testable | Untestable or unscoped |
| Methodology judgement | Insightful selection and loop analysis | Reasonable judgement | Superficial | Misapplied methodology |
| Maturity assessment | Evidence-based, realistic, prioritised | Solid assessment | Partial assessment | Weak or unevidenced |
| Loop integration | Findings clearly drive detection/intel | Adequate integration | Mentioned only | Absent |
| Communication | Clear, professional, evidence-linked | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories & ASD Annual Cyber Threat Report:** Primary hunt triggers and
  hypothesis sources.
- **ASD Essential Eight:** Hunts framed around control-bypass behaviours.
- **SOCI Act 2018:** Hunting positioned as support for critical-infrastructure
  detection obligations.

---

## Further Reading

**Bianco, D. & Hunting community (2023).** *The Hunting Maturity Model & PEAK Threat Hunting Framework.* https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html
> Relevance: The maturity and process frameworks central to Topics 5–6 (freely available).

**de Boer, M. et al. (2018).** *TaHiTI: Targeted Hunting integrating Threat Intelligence.* (Dutch financial sector CTI working group.)
> Relevance: The hunting methodology this unit is built on; freely available.

**MITRE ATT&CK (v19, 2026).** *ATT&CK for Enterprise.* The MITRE Corporation. https://attack.mitre.org
> Relevance: The behavioural taxonomy used to ground hunt hypotheses and plans.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report & advisories.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian source of real threat triggers used in both labs (Australian source).

**Roberts, S. & Brown, R. (2017).** *Intelligence-Driven Incident Response.* O'Reilly.
> Relevance: Connects intelligence, hunting, and response in the continuous loop of Topic 6.

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | TH01 |
| Unit Title | Hunting Methodology & Process |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Threat Hunting |
| Prerequisites | OC01, OC02, OC05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
