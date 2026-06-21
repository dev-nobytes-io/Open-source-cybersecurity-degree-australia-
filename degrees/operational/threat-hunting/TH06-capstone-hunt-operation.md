# TH06: Capstone — Hunt Operation

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

The capstone integrates the entire Threat Hunting major into a single, end-to-end
hunt operation against a simulated compromised environment. Students take a hunt
from intelligence-driven hypothesis (TaHiTI), through ATT&CK-based planning, host
and network execution, analysis and verdict, to a professional hunt report and the
conversion of findings into detections. It is assessed at the highest cognitive
levels — students **design** and **create** a complete operation and **evaluate**
its outcomes — and produces a portfolio-grade deliverable suitable for employer
review.

The capstone is the culmination of the threat-informed-defense thesis that runs
through the whole degree: a hunter, driven by intelligence about real adversary
behaviour (ATT&CK v19, ACSC reporting), proactively finds what automation missed
and feeds the result back into detection, logging, and automation. In the
Australian context, the operation is scenario-grounded in ACSC advisories and
mapped to Essential Eight and SOCI-relevant obligations. TH06 requires TH01–TH05
and the operational core.

---

## Prerequisites

- TH01 — Hunting Methodology & Process
- TH02 — ATT&CK for Hunters
- TH03 — Host-Based Hunting
- TH04 — Network-Based Hunting
- TH05 — Hunt Operations & Tooling

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** a complete, intelligence-driven hunt operation for a defined scenario
   and environment.
2. **Create** an ATT&CK-mapped hunt plan integrating host and network hypotheses.
3. **Evaluate** evidence across host and network data to reach defensible verdicts.
4. **Create** a professional hunt report and a portfolio artefact suitable for
   employer review.
5. **Design** detections and recommendations that operationalise the hunt's
   findings.
6. **Evaluate** the operation's effectiveness and recommend improvements to the
   hunt program.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** The capstone consolidates specialised knowledge across the
hunting discipline into an integrated operation.

**Skills (AQF 7.2):** Students demonstrate the highest-order cognitive and technical
skills — designing, creating, and evaluating a full operation independently.

**Application (AQF 7.3):** Students apply the complete skill set with professional
accountability, producing employer-grade deliverables in an Australian context.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0569 | Apply threat frameworks to design and conduct a full hunt operation | Lab 1 — Hunt Design & Planning |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst (511) | PR-CDA-001 | T0259 | Execute host/network hunts and report findings with detections | Lab 2 — Execution, Reporting & Detection Hand-off |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 5 | Lab 1, Lab 2 |
| Security operations | SCAD | Level 4–5 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Threat Hunting | Advanced | Lab 1, Lab 2 |

---

## Topics

> The capstone is delivered as a supervised project. These "topics" are the
> operation's phases and the guidance for each; the substantive work is the
> student's own hunt.

### Topic 1: Capstone Scope and Success Criteria

This phase defines the operation: the scenario, the environment, the rules of
engagement, the deliverables, and what "success" means. Students agree scope with
their supervisor and plan their time across the operation.

**Key concepts:**
- Scenario, environment, and rules of engagement
- Deliverables and success criteria
- Project planning and time-boxing

---

### Topic 2: Intelligence-Driven Hypothesis (TaHiTI)

Students apply TaHiTI to turn the scenario's intelligence (an ACSC-style advisory)
into prioritised, testable hypotheses, documented in the hunt backlog.

**Key concepts:**
- From advisory to prioritised hypotheses
- Documenting the hunt backlog
- Linking hypotheses to decisions/assets

---

### Topic 3: ATT&CK-Mapped Hunt Plan

Students build the plan: techniques to hunt (ATT&CK v19), the sequence (Attack
Flow), the data required, and the host/network split — integrating TH02–TH04.

**Key concepts:**
- Technique selection, prioritisation, and sequencing
- Data requirements and visibility gaps
- Integrated host + network plan

---

### Topic 4: Execution Across Host and Network

Students execute the hunt with the TH05 toolset (Velociraptor VQL, Jupyter/Pandas,
Zeek/Wireshark, log platform), collecting evidence and iterating between broad and
narrow analysis.

**Key concepts:**
- Disciplined, documented execution
- Iterating and pivoting on evidence
- Maintaining reproducibility throughout

---

### Topic 5: Analysis, Verdict, and Reporting

Students analyse the evidence, reach defensible verdicts (using structured analysis
to avoid bias), and produce a professional hunt report with a clear narrative,
evidence, and confidence statements.

**Key concepts:**
- Evidence synthesis and structured analysis
- Defensible verdicts and confidence
- Professional, audience-aware reporting

---

### Topic 6: Operationalising Findings and Self-Evaluation

Students convert findings into at least two Sigma detections and recommendations
(logging/automation), then evaluate their own operation against its success
criteria and recommend program improvements — closing the loop.

**Key concepts:**
- Findings → detections and recommendations
- Honest self-evaluation against criteria
- Program-improvement recommendations

**Australian context:** Findings and recommendations are tied to Essential
Eight/SOCI-relevant detection obligations.

---

## Labs & Exercises

### Lab 1: Hunt Design & Planning

**Objective:** Produce the complete plan for the capstone hunt operation before
execution.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: any for planning; the capstone range is provisioned for Lab 2
- Tools: ATT&CK Navigator (v19), CTID Attack Flow, a hunt-plan template (free)
- Minimum hardware: trivial for planning; within spec

**Instructions:**

1. Confirm scope, environment, and success criteria with your supervisor.
2. Apply TaHiTI to derive prioritised, testable hypotheses from the scenario
   advisory.
3. Build an ATT&CK v19 Navigator layer and an Attack Flow for the expected activity.
4. Specify data requirements and the host/network hunt split.
5. Define the verdict criteria and the deliverables.
6. Submit the plan for supervisor approval before execution.

**Expected Output:**

An approved, complete hunt plan: scope, hypotheses, ATT&CK layer, Attack Flow, data
requirements, and success criteria. The plan is detailed enough for another hunter
to execute.

**Reflection Questions:**

1. Which hypothesis is most likely to yield findings, and why?
2. Where are your biggest visibility risks, and how will you mitigate them?
3. How will you avoid confirmation bias during execution?

---

### Lab 2: Execution, Reporting & Detection Hand-off

**Objective:** Execute the planned hunt end-to-end and deliver the report,
detections, and portfolio artefact.

**Prerequisites:**
- Topics 4–6 and Lab 1 (approved plan)

**Environment:**
- Operating System: the provided capstone range (compromised simulated environment)
- Tools: Velociraptor, Jupyter/Pandas, Zeek/Wireshark, log platform, Sigma — all
  free/OSS
- Minimum hardware: run components sequentially — within the 8 GB / 4-core / 50 GB
  spec; no GPU

**Instructions:**

1. Execute the host and network hunts per the approved plan, documenting as you go
   (reproducible notebooks/queries).
2. Collect and synthesise evidence; reach defensible verdicts using structured
   analysis.
3. Produce a professional hunt report: scenario, hypotheses, method, findings,
   evidence, ATT&CK v19 mapping, and confidence.
4. Convert findings into at least two Sigma detections.
5. Recommend logging/automation improvements and program changes.
6. Package a portfolio artefact (reference `templates/student-portfolio/index.html`)
   and submit for community practitioner review.

**Expected Output:**

A complete hunt operation: documented execution, a professional report with
ATT&CK-mapped findings and verdicts, ≥2 Sigma detections, recommendations, and a
portfolio artefact. The package is suitable for employer review.

**Reflection Questions:**

1. How well did the outcome match your hypotheses, and what does that tell you?
2. Which finding most improves the environment's defence, and how?
3. If you re-ran this operation, what would you change in method or tooling?

---

## Assessment

### Formative Assessment: Plan Review Gate

**Type:** Supervisor/peer review of the Lab 1 plan

**Description:** The hunt plan is reviewed before execution against scope,
testability, ATT&CK mapping, and data feasibility. Students revise based on
feedback. Acts as a go/no-go gate into execution.

**Learning Outcomes Assessed:** LO1, LO2

**Feedback mechanism:** Structured supervisor/peer feedback against a plan rubric;
revision required before Lab 2.

---

### Summative Assessment: Capstone Hunt Operation

**Type:** End-to-end hunt operation with professional report and portfolio artefact

**Description:** The complete operation: an approved plan, a documented execution
across host and network, a professional hunt report with ATT&CK v19-mapped findings
and defensible verdicts, at least two Sigma detections, recommendations, a
self-evaluation against success criteria, and a portfolio artefact. Subject to
community practitioner review. Deliverable: full operation package (report
~4,000–5,000 words plus artefacts).

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Hunt design & plan | LO1, LO2 |
| Execution & evidence analysis | LO3 |
| Professional report & portfolio | LO4 |
| Detections & recommendations | LO5 |
| Self-evaluation & program improvement | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Design & planning | Sophisticated, intelligence-driven, feasible plan | Sound plan | Partial plan | Weak/infeasible |
| Execution & analysis | Rigorous, reproducible, bias-aware; correct verdicts | Solid execution | Partial or inconsistent | Poor |
| Reporting & portfolio | Employer-grade, clear, evidence-linked | Professional with minor gaps | Disorganised | Unclear |
| Operationalisation | Robust detections + actionable recommendations | Workable | Generic | Missing |
| Self-evaluation | Insightful, honest, improvement-focused | Reasonable | Superficial | Absent |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories:** The capstone scenario is grounded in a real ACSC-style
  advisory and Australian-relevant actor TTPs.
- **ASD Essential Eight:** Findings and recommendations target control-bypass
  behaviours.
- **SOCI Act 2018:** The operation is framed in terms of critical-infrastructure
  detection obligations where applicable.

---

## Further Reading

**MITRE ATT&CK (v19, 2026).** *ATT&CK for Enterprise.* The MITRE Corporation. https://attack.mitre.org
> Relevance: The taxonomy underpinning the capstone's planning, mapping, and reporting.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Adversary Emulation Library, Attack Flow.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: Supports realistic scenario design and technique sequencing in the capstone.

**SANS (2024).** *Threat hunting & hunt-reporting white papers (FOR508/FOR578 ecosystem).* SANS Institute. https://www.sans.org/white-papers/
> Relevance: Professional reporting and operations practice for the capstone deliverable.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report & advisories.* ACSC. https://www.cyber.gov.au
> Relevance: The Australian threat context grounding the capstone scenario (Australian source).

**Templates — Student Portfolio.** `templates/student-portfolio/index.html` (this repository).
> Relevance: The portfolio artefact format that the capstone deliverable must populate (Australian-context degree resource).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | TH06 |
| Unit Title | Capstone — Hunt Operation |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 24 CP |
| Degree Layer | Capstone |
| Major / Pathway | Threat Hunting |
| Prerequisites | TH01, TH02, TH03, TH04, TH05 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 5–6 (Evaluate, Create) |
| Australian Legislation Referenced | Security of Critical Infrastructure Act 2018 (contextual) |
