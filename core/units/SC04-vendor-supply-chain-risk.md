# SC04: Vendor & Supply Chain Risk

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Modern organisations are only as secure as the third parties they depend on. This
unit teaches the management of vendor and supply-chain risk: assessing and
monitoring suppliers, managing the risk introduced by software dependencies and the
software supply chain, and embedding security into contracts and procurement. It
draws on **NIST SP 800-161** (cyber supply-chain risk management), the use of
**SOC 2** reports and **ISO 27001** certificates as third-party assurance, and the
Australian regulatory drivers — **APRA CPS 234** third-party provisions, the
related operational-risk standard **APRA CPS 230**, and **SOCI** supply-chain
considerations.

Supply-chain incidents — from compromised software updates to breached service
providers — are among the highest-impact events in the modern threat landscape, and
they connect directly to the threat-informed defense thinking of the operational
core: a supplier's compromise becomes your incident. SC04 builds on SC01 (risk) and
SC03 (governance/compliance) and supports SC05, the GRC major, and procurement and
vendor-management practice.

---

## Prerequisites

- SC01 — Risk Management Frameworks
- SC03 — Governance, Policy & Compliance

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** the sources and significance of third-party and supply-chain risk.
2. **Apply** a vendor risk-assessment process across the supplier lifecycle
   (onboarding to offboarding).
3. **Analyse** third-party assurance artefacts (SOC 2 reports, ISO 27001
   certificates, questionnaires) to evaluate a supplier.
4. **Apply** software-supply-chain risk practices (dependency, SBOM, NIST SP
   800-161) to assess software risk.
5. **Examine** how Australian regulation (APRA CPS 234/CPS 230, SOCI) governs
   third-party and outsourcing risk.
6. **Analyse** contractual and procurement controls that manage supplier risk.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops coherent knowledge of third-party and
software-supply-chain risk and the assurance and regulatory context around them.

**Skills (AQF 7.2):** Students develop analytical skills by assessing suppliers and
software risk and evaluating assurance evidence.

**Application (AQF 7.3):** Students apply vendor-risk methods to realistic
Australian scenarios, aligning with regulatory and contractual obligations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Control Assessor | SP-RSK-002 | T0177 | Assess third-party security posture against requirements | Lab 1 — Vendor Risk Assessment |
| NIST NICE DCWF | 2023 | Cyber Policy & Strategy Planner | OV-SPP-001 | T0226 | Develop supply-chain risk and procurement security requirements | Lab 2 — Software Supply Chain & Contracts |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Supplier management | SUPP | Level 4 | Lab 1 |
| Information risk management | BURM | Level 4 | Lab 1, Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Third-Party Risk | Practitioner | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | SC04-K01 | Knowledge of the sources and significance of third-party and supply-chain risk | Topic 1 |
| Knowledge | SC04-K02 | Knowledge of the vendor risk lifecycle across the supplier relationship | Topic 2 |
| Knowledge | SC04-K03 | Knowledge of software-supply-chain risk practices (dependencies, SBOM, NIST SP 800-161) | Topic 4 |
| Knowledge | SC04-K04 | Knowledge of Australian regulation governing third-party risk (APRA CPS 234/CPS 230, SOCI) | Topic 5 |
| Skill | SC04-S01 | Skill in performing a vendor risk assessment | Lab 1 |
| Skill | SC04-S02 | Skill in evaluating supply-chain risk and contractual controls | Lab 2 |
| Ability | SC04-A01 | Ability to interpret third-party assurance artefacts (SOC 2 reports, ISO 27001 certificates) | Topic 3; Lab 1 |
| Ability | SC04-A02 | Ability to specify contractual and procurement controls that manage supplier risk | Lab 2; Topic 6 |
| Task | T0177 | Assess third-party security posture against requirements | Lab 1 |
| Task | T0226 | Develop supply-chain risk and procurement security requirements | Lab 2 |

---

## Topics

### Topic 1: Why Supply-Chain Risk Matters

A supplier's weakness is your exposure. This topic frames the problem: the expanding
third-party attack surface, concentration risk (many organisations relying on the
same provider), fourth-party risk (your supplier's suppliers), and the high impact
of supply-chain incidents. It connects to threat-informed defense — supplier
compromise is a real adversary path.

**Key concepts:**
- Third-, fourth-party, and concentration risk
- The expanding outsourced attack surface
- Supply-chain compromise as an adversary technique

**Australian context:** Recent Australian breaches involving third-party providers
illustrate the systemic nature of the risk.

---

### Topic 2: The Vendor Risk Lifecycle

Vendor risk is managed across a lifecycle. This topic covers due diligence at
onboarding, tiering vendors by criticality and data access, ongoing monitoring,
and secure offboarding (revoking access, returning/destroying data). It stresses
proportionality — effort should match the vendor's risk tier.

**Key concepts:**
- Onboarding due diligence and vendor tiering
- Ongoing monitoring and reassessment
- Secure offboarding

---

### Topic 3: Evaluating Third-Party Assurance

Assurance evidence must be read critically. This topic teaches interpreting a
**SOC 2** report (Type I vs Type II, scope, the auditor's opinion, exceptions, and
complementary user-entity controls), reading an **ISO 27001** certificate and its
Statement of Applicability, and using security questionnaires effectively — knowing
their limits.

**Key concepts:**
- SOC 2 Type I vs II, scope, exceptions, and CUECs
- ISO 27001 certificate scope and Statement of Applicability
- Questionnaires: value and limits

---

### Topic 4: Software Supply-Chain Risk

Software is assembled, not written. This topic covers dependency risk (open-source
and transitive dependencies), the **software bill of materials (SBOM)**, build and
update integrity, and **NIST SP 800-161** practices. It connects to OC03 (malware)
and detection thinking — a poisoned dependency is a code-level supply-chain attack.

**Key concepts:**
- Dependency and transitive-dependency risk
- SBOM and component transparency
- Build/update integrity and NIST SP 800-161

---

### Topic 5: Regulatory Drivers for Third-Party Risk

Australian regulation increasingly governs outsourcing. This topic covers **APRA
CPS 234** third-party information-security requirements and the broader operational-
risk standard **APRA CPS 230** (service-provider management and resilience), and
**SOCI** supply-chain considerations for critical infrastructure. Students learn
what regulators expect of third-party governance.

**Key concepts:**
- APRA CPS 234 third-party provisions
- APRA CPS 230 operational-risk and service-provider management
- SOCI supply-chain considerations

**Australian context:** This topic is largely Australian regulatory obligation.

---

### Topic 6: Contractual and Procurement Controls

Risk is also managed on paper. This topic covers embedding security into
procurement and contracts: security schedules, right-to-audit clauses, breach-
notification obligations, data-handling and sub-processor terms, SLAs, and exit
provisions. It frames procurement as the earliest and cheapest point to control
vendor risk.

**Key concepts:**
- Security schedules and right-to-audit
- Breach-notification and data-handling clauses
- Exit provisions and sub-processor control

---

## Labs & Exercises

### Lab 1: Vendor Risk Assessment

**Objective:** Assess a third-party supplier using assurance evidence and produce a
tiered risk decision.

**Prerequisites:**
- Topics 1–3

**Environment:**
- Operating System: any
- Tools: a provided (sample) SOC 2 report and ISO 27001 certificate, a vendor-risk
  template
- Minimum hardware: trivial

**Instructions:**

1. Take a scenario: onboarding a SaaS provider that will process customer personal
   information for an Australian organisation.
2. Tier the vendor by criticality and data sensitivity.
3. Review the sample SOC 2 report: note Type, scope, the opinion, any exceptions,
   and complementary user-entity controls you must implement.
4. Review the ISO 27001 certificate scope and check it covers the relevant service.
5. Identify residual concerns the assurance evidence does not address.
6. Produce a risk decision (approve / approve-with-conditions / reject) with
   conditions and monitoring.

**Expected Output:**

A vendor risk assessment with tiering, a critical reading of the assurance
artefacts (including exceptions and CUECs), residual concerns, and a justified
decision. Learners can explain what the SOC 2/ISO evidence does and does not prove.

**Reflection Questions:**

1. What did the SOC 2 exceptions and CUECs mean for your own obligations?
2. Where did the assurance evidence fall short, and how would you cover the gap?
3. How does this vendor's compromise become your incident (link to OC04)?

---

### Lab 2: Software Supply Chain & Contracts

**Objective:** Assess software-supply-chain risk for an application and draft the
contractual controls to manage a supplier.

**Prerequisites:**
- Topics 4–6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM (for SBOM tooling) or any for the
  contractual part
- Tools: a free SBOM tool (e.g. Syft) and dependency scanner (e.g. Grype/OWASP
  Dependency-Check), a contract-clause template — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 20 GB disk (within spec; no GPU)

**Instructions:**

1. Generate an SBOM for a sample application using a free tool.
2. Scan the dependencies for known vulnerabilities and identify the highest-risk
   components.
3. Assess transitive-dependency and update-integrity risk for the application.
4. Recommend software-supply-chain controls (pinning, signing, SBOM in CI,
   monitoring) aligned to NIST SP 800-161.
5. Draft three contractual security clauses for a supplier of this software (e.g.
   right-to-audit, breach notification, SBOM/patch obligations).
6. Note which Australian regulatory expectation each control supports.

**Expected Output:**

An SBOM and vulnerability findings, prioritised software-supply-chain controls, and
three drafted contractual clauses mapped to regulatory expectations. Learners can
connect technical and contractual controls.

**Reflection Questions:**

1. Which dependency risk surprised you, and how would an SBOM in CI help over time?
2. How do contractual controls complement technical controls for supply-chain
   risk?
3. How would APRA CPS 230/234 shape your requirements for a critical supplier?

---

## Assessment

### Formative Assessment: Assurance Artefact Critique

**Type:** Short-answer exercise with answer key

**Description:** Given excerpts from SOC 2 reports and ISO 27001 certificates,
students identify scope limitations, exceptions, and what each does/doesn't assure.
Self-marked.

**Learning Outcomes Assessed:** LO3

**Feedback mechanism:** Answer key explaining the correct interpretation of each
artefact excerpt.

---

### Summative Assessment: Third-Party Risk Management Plan

**Type:** Practical report

**Description:** For an assigned Australian organisation with a critical supplier and
a software dependency, students (a) assess the vendor using assurance evidence and
tier it, (b) assess software-supply-chain risk with an SBOM, (c) recommend technical
and contractual controls, (d) map obligations to APRA CPS 234/CPS 230 or SOCI as
applicable, and (e) define ongoing monitoring. Deliverable: 2,500–3,000 word report
with assessment, SBOM findings, and contractual clauses.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Vendor assessment & tiering | LO1, LO2, LO3 |
| Software-supply-chain assessment | LO4 |
| Contractual controls | LO6 |
| Regulatory mapping & monitoring | LO5 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Vendor assessment | Critical, well-tiered, evidence-based decision | Solid assessment | Partial assessment | Superficial or uncritical |
| Software-supply-chain analysis | Thorough SBOM-driven analysis with prioritised controls | Adequate analysis | Partial analysis | Little analysis |
| Contractual controls | Precise, enforceable, regulation-aligned clauses | Reasonable clauses | Generic clauses | Weak or missing clauses |
| Regulatory mapping | Accurate APRA/SOCI mapping | Mostly accurate | Superficial | Incorrect/missing |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **APRA CPS 234 & CPS 230:** Third-party information-security and operational-risk/
  service-provider obligations for regulated entities.
- **SOCI Act:** Supply-chain considerations for critical infrastructure.
- **Australian third-party breach experience:** Used to illustrate systemic
  supply-chain risk and the NDB consequences when a provider is breached.

---

## Further Reading

**NIST (2022).** *SP 800-161 Rev. 1 — Cybersecurity Supply Chain Risk Management.* NIST. https://csrc.nist.gov/pubs/sp/800/161/r1/final
> Relevance: The authoritative, free C-SCRM guidance underpinning Topic 4 and Lab 2.

**AICPA (2024).** *SOC 2 reporting & Trust Services Criteria.* AICPA. https://www.aicpa-cima.com
> Relevance: The third-party assurance artefact interpreted in Topic 3 and Lab 1.

**APRA (2023).** *Prudential Standard CPS 230 Operational Risk Management & CPS 234.* APRA. https://www.apra.gov.au
> Relevance: The Australian regulatory drivers for third-party and outsourcing risk (Australian source).

**CISA (2024).** *Software Bill of Materials (SBOM) & supply-chain guidance.* CISA. https://www.cisa.gov/sbom
> Relevance: Practical SBOM and software-supply-chain guidance supporting Lab 2.

**Office of the Australian Information Commissioner (2024).** *Notifiable Data Breaches insights (third-party breaches).* OAIC. https://www.oaic.gov.au
> Relevance: Australian evidence of third-party breach impact and notification consequences (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SC04 |
| Unit Title | Vendor & Supply Chain Risk |
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
| Australian Legislation Referenced | APRA CPS 234; APRA CPS 230; Security of Critical Infrastructure Act 2018; Privacy Act 1988 (NDB) |
