# SC05: Security Program Management

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches students to build and run a security program: the structures,
roadmap, budget, metrics, and people that turn strategy into sustained capability.
It covers establishing a program against a backbone framework (**NIST CSF 2.0**),
assessing and maturing capability, prioritising and funding initiatives, measuring
performance, and managing the security team and its place in the wider business.
The unit treats the security program as a business function that must justify its
investment and demonstrate return — including the way a maturing program unlocks
the compliance certifications (SC03) that open markets.

Program management is where risk (SC01), architecture (SC02), governance/compliance
(SC03), and vendor risk (SC04) come together as a coherent, funded, measured whole.
In the Australian context, program maturity is benchmarked against the **Essential
Eight Maturity Model** and shaped by APRA/SOCI obligations and the value of IRAP/
SOC 2/ISO certification. SC05 supports SC06 (Stakeholder Communication) and the
Leadership and GRC majors.

---

## Prerequisites

- SC01 — Risk Management Frameworks
- SC03 — Governance, Policy & Compliance

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** the components of a security program and how it delivers strategy.
2. **Apply** a capability/maturity assessment using a recognised model (NIST CSF
   2.0 tiers, Essential Eight Maturity Model).
3. **Apply** prioritisation and roadmapping to sequence security initiatives under
   constraints.
4. **Analyse** a security budget and build a business case that ties spend to risk
   reduction and commercial enablement.
5. **Examine** security metrics and reporting (KPIs/KRIs) that demonstrate program
   performance.
6. **Analyse** team structure, roles, and resourcing for a security function.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of security-program
structure, maturity, metrics, and resourcing.

**Skills (AQF 7.2):** Students develop planning and analytical skills by building
roadmaps, budgets, and metrics, and management skills by structuring a team.

**Application (AQF 7.3):** Students apply program-management methods to a realistic
Australian organisation, producing a funded, measured, maturity-driven plan.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Information Systems Security Manager | OV-MGT-001 | T0149 | Recommend resource allocations and manage the security program | Lab 1 — Maturity Assessment & Roadmap |
| NIST NICE DCWF | 2023 | Cyber Policy & Strategy Planner | OV-SPP-001 | T0445 | Develop security strategy, metrics, and reporting | Lab 2 — Budget Business Case & Metrics |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Management | MANA | Level 5 | Lab 2 |
| Information security | SCTY | Level 5 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Program Management | Practitioner | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Anatomy of a Security Program

A security program is the organised sum of strategy, governance, people, process,
technology, and measurement. This topic defines the program's components, its
relationship to the business strategy, and the role of the security leader in
aligning them. It frames the program as a value-delivering function, not a cost
centre.

**Key concepts:**
- Program components and their interdependence
- Alignment to business strategy
- Security as a value function

---

### Topic 2: Capability and Maturity Assessment

You cannot improve what you cannot assess. This topic teaches assessing current
capability against a maturity model — NIST CSF 2.0 implementation tiers and the
**Essential Eight Maturity Model** — to produce a baseline and a target. It covers
honest self-assessment, evidence, and setting a realistic target maturity.

**Key concepts:**
- NIST CSF 2.0 tiers and the Essential Eight Maturity Model
- Baseline vs target maturity
- Evidence-based, honest assessment

**Australian context:** The Essential Eight Maturity Model is the Australian
benchmark used here.

---

### Topic 3: Prioritisation and Roadmapping

Resources are finite. This topic teaches sequencing initiatives by risk reduction,
dependency, effort, and commercial value into a phased roadmap. It connects
prioritisation to the SC01 risk register and the SC03 compliance goals (e.g.
sequencing toward a SOC 2 or IRAP milestone).

**Key concepts:**
- Prioritisation by risk, dependency, effort, and value
- Phased roadmaps and milestones
- Sequencing toward compliance/commercial milestones

---

### Topic 4: Budgeting and the Business Case

Programs run on money. This topic covers building and defending a security budget:
capex vs opex, cost categories, and — critically — the business case that ties
spend to risk reduction (SC01 quantification) and to commercial enablement (the
markets a certification unlocks, per SC03). Students learn to speak the language of
investment and return.

**Key concepts:**
- Security budgeting (capex/opex, cost categories)
- Tying spend to quantified risk reduction
- The commercial-enablement argument for security spend

---

### Topic 5: Metrics, KPIs, and Reporting

A program proves its worth with measurement. This topic covers designing metrics
that matter — leading vs lagging, KPIs (performance) vs KRIs (risk) — avoiding
vanity metrics, and reporting in a way that drives decisions. It links to SC06's
stakeholder communication and to the operational metrics from OC02.

**Key concepts:**
- Leading vs lagging metrics; KPIs vs KRIs
- Avoiding vanity metrics
- Decision-driving reporting

---

### Topic 6: People — Team, Roles, and Resourcing

Programs are delivered by people. This topic covers structuring a security team
(build vs buy vs MSSP), key roles and their workforce-framework mappings (NICE/
ASD/SFIA), skills development, and managing burnout and retention in a high-demand
field. It connects resourcing decisions to the program roadmap and budget.

**Key concepts:**
- Team structures; in-house vs outsourced/MSSP
- Roles mapped to NICE/ASD/SFIA
- Skills, retention, and sustainable resourcing

**Australian context:** Addresses the Australian cyber-skills shortage as a real
resourcing constraint.

---

## Labs & Exercises

### Lab 1: Maturity Assessment & Roadmap

**Objective:** Assess a scenario organisation's security maturity and build a phased
improvement roadmap.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: any
- Tools: NIST CSF 2.0 and Essential Eight Maturity Model references (free), a
  spreadsheet
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario organisation with a described current state.
2. Assess current maturity against the Essential Eight Maturity Model and NIST CSF
   2.0 tiers; record a baseline.
3. Set a realistic target maturity with justification.
4. Identify the gap initiatives needed to close baseline→target.
5. Prioritise the initiatives (risk, dependency, effort, value) into a phased
   roadmap.
6. Tie at least one phase to a compliance/commercial milestone (e.g. SOC 2
   readiness).

**Expected Output:**

A maturity baseline and target, a prioritised gap-closing roadmap with phases, and
at least one compliance/commercial milestone. Learners can justify the sequencing.

**Reflection Questions:**

1. Why is a realistic target maturity better than "maximum everywhere"?
2. How did risk and commercial value interact in your prioritisation?
3. Which initiative gives the best risk reduction per dollar?

---

### Lab 2: Budget Business Case & Metrics

**Objective:** Build a security budget business case and a metrics set that
demonstrates program performance.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: any
- Tools: a spreadsheet, the Lab 1 roadmap and an SC01-style risk quantification
- Minimum hardware: trivial

**Instructions:**

1. Take the top roadmap initiatives from Lab 1 and estimate their cost (capex/opex).
2. For each, articulate the risk reduction (link to quantified exposure) and any
   commercial enablement (markets/contracts unlocked).
3. Build a one-page budget business case prioritising the spend.
4. Design five metrics for the program: at least two leading, one KRI, and one tied
   to a commercial outcome.
5. Define how each metric is collected and reported, and to whom.
6. Draft a sample one-page board-level metrics summary.

**Expected Output:**

A prioritised budget business case linking spend to risk and commercial value, a
five-metric set with collection/reporting defined, and a board-level summary.
Learners can defend the budget to an executive audience.

**Reflection Questions:**

1. Which is more persuasive to a board — risk reduction or commercial enablement —
   and when?
2. How did you avoid vanity metrics?
3. How would these metrics feed the stakeholder communication in SC06?

---

## Assessment

### Formative Assessment: Metric Quality Critique

**Type:** Short-answer exercise with answer key

**Description:** Given a set of proposed security metrics, students classify each
(leading/lagging, KPI/KRI, vanity?) and rewrite the weak ones to be
decision-driving. Self-marked.

**Learning Outcomes Assessed:** LO5

**Feedback mechanism:** Answer key with the classification and improved metric for
each item.

---

### Summative Assessment: Security Program Plan

**Type:** Strategy report

**Description:** For an assigned Australian organisation, students produce a security
program plan that (a) assesses current vs target maturity, (b) presents a prioritised
roadmap, (c) builds a budget business case tying spend to risk reduction and
commercial enablement, (d) defines a metrics-and-reporting set, and (e) proposes a
team structure and resourcing approach. Deliverable: 3,000–3,500 word plan with
maturity assessment, roadmap, budget case, and metrics.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Maturity assessment | LO1, LO2 |
| Roadmap | LO3 |
| Budget business case | LO4 |
| Metrics & reporting | LO5 |
| Team & resourcing | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Maturity & roadmap | Honest assessment; pragmatic, prioritised roadmap | Solid assessment and roadmap | Partial or unrealistic | Weak or absent |
| Budget business case | Compelling link of spend to risk + commercial value | Reasonable case | Generic case | No real case |
| Metrics | Decision-driving, balanced, no vanity | Mostly sound metrics | Some vanity metrics | Poor metrics |
| Team & resourcing | Realistic, role-mapped, sustainable | Reasonable structure | Generic structure | Unrealistic |
| Communication | Executive-ready, clear | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **Essential Eight Maturity Model:** The Australian benchmark for the maturity
  assessment in Topic 2 and Lab 1.
- **APRA / SOCI obligations:** Shape program priorities and resourcing for regulated
  and critical-infrastructure entities.
- **Australian cyber-skills shortage:** Treated as a real resourcing constraint in
  Topic 6.

---

## Further Reading

**NIST (2024).** *Cybersecurity Framework 2.0 (tiers & profiles).* NIST. https://www.nist.gov/cyberframework
> Relevance: The backbone framework for program structure and maturity in Topics 1–2.

**Australian Cyber Security Centre (2023).** *Essential Eight Maturity Model.* ACSC. https://www.cyber.gov.au/essential-eight
> Relevance: The Australian maturity benchmark used in Lab 1 (Australian source).

**Brotby, K. & Hinson, G. (2016).** *PRAGMATIC Security Metrics.* CRC Press.
> Relevance: A practical guide to designing the decision-driving metrics in Topic 5.

**(ISC)² / ISACA (2024).** *CISM / security management body of knowledge.* ISACA. https://www.isaca.org
> Relevance: Professional grounding in security program management and governance.

**AISA (2024).** *Australian Cyber Security Skills & workforce material.* AISA. https://www.aisa.org.au
> Relevance: Australian workforce context for the resourcing decisions in Topic 6 (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SC05 |
| Unit Title | Security Program Management |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Strategic Core |
| Major / Pathway | Strategic |
| Prerequisites | SC01, SC03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–4 (Apply, Analyse) |
| Australian Legislation Referenced | None directly (Essential Eight / APRA / SOCI context) |
