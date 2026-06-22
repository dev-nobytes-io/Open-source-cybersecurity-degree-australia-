# SE05: Security in Cloud & DevSecOps

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (security architecture/engineering)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches securing modern cloud-native delivery: hardening infrastructure as
code (IaC), securing containers, and embedding security into CI/CD pipelines
(DevSecOps). Students learn to shift security left into the build and deploy
pipeline — scanning IaC against benchmarks, integrating SAST/DAST, and enforcing
secure configuration automatically — so that security scales with the speed of cloud
delivery rather than blocking it.

DevSecOps is where the secure-design principles of SE01 meet the reality of
continuous delivery. In the Australian context it operationalises the ASD Essential
Eight (application control, patching, MFA) within automated pipelines, and its
maturity is tracked via the software-assurance models (BSIMM/OWASP SAMM) in
`docs/maturity-models.md`. SE05 builds on SE01–SE02, F03 (Scripting/IaC), and benefits
from OC06; it feeds the SE06 capstone.

---

## Prerequisites

- SE02 — Security Architecture
- F03 — Scripting & Automation

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Analyse** infrastructure-as-code for security misconfiguration against
   benchmarks.
2. **Apply** container security practices across image, registry, and runtime.
3. **Design** a secure CI/CD pipeline with integrated security gates.
4. **Apply** SAST/DAST and IaC scanning in a pipeline.
5. **Analyse** DevSecOps controls against the ASD Essential Eight.
6. **Recommend** a DevSecOps approach that secures delivery without blocking it.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of cloud-native and
DevSecOps security engineering.

**Skills (AQF 7.2):** Students develop technical skills by scanning IaC and
integrating security into pipelines.

**Application (AQF 7.3):** Students apply DevSecOps to realistic delivery pipelines
aligned to Australian baseline controls.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Secure Software Assessor | SP-DEV-002 | T0111 | Integrate and assess security in the delivery pipeline | Lab 2 — SAST/DAST in CI/CD |
| NIST NICE DCWF | 2023 | Security Architect (652) | SP-ARC-002 | T0050 | Design secure cloud/IaC configuration | Lab 1 — IaC Security Audit |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Solution architecture | ARCH | Level 4 | Lab 1 |
| Systems & software life cycle / assurance | SURE | Level 4 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Security Architecture | Cloud & DevSecOps | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: DevSecOps Principles

This topic frames DevSecOps: shifting security left, automating security gates, and
making security a shared responsibility across dev/ops/sec — securing speed rather
than opposing it.

**Key concepts:**
- Shift-left and automated gates
- Shared responsibility
- Securing delivery velocity

---

### Topic 2: Infrastructure as Code Security

This topic teaches securing IaC: scanning Terraform/templates against benchmarks
(e.g. CIS), policy-as-code, drift, and the security advantage of reviewable,
versioned infrastructure (building on F03).

**Key concepts:**
- IaC scanning against benchmarks (CIS)
- Policy-as-code
- Drift and reviewable infrastructure

---

### Topic 3: Container Security

This topic covers securing containers across the lifecycle: image hygiene and
minimal base images, registry/scanning, runtime security, and orchestration
(Kubernetes) security basics.

**Key concepts:**
- Image hygiene and scanning
- Registry and supply-chain integrity
- Runtime and orchestration security

---

### Topic 4: Secure CI/CD Pipelines

This topic teaches hardening the pipeline itself: securing the build system, secrets
management, signing/provenance, and the security gates (SAST/DAST/SCA/IaC scan) that
run in the pipeline.

**Key concepts:**
- Pipeline hardening and secrets management
- Build provenance/signing (supply chain)
- Security gates in the pipeline

---

### Topic 5: Application Security Testing

This topic covers the testing types and their place in the pipeline: SAST, DAST, SCA
(dependency scanning, linking to SC04 supply chain), and how to tune them to avoid
blocking delivery with noise.

**Key concepts:**
- SAST, DAST, SCA and where each fits
- Tuning to reduce false positives
- Risk-based gating

---

### Topic 6: DevSecOps, Essential Eight, and Maturity

This topic aligns DevSecOps to the ASD Essential Eight (application control,
patching, MFA in pipelines) and to software-assurance maturity (BSIMM/OWASP SAMM —
see `docs/maturity-models.md`), framing DevSecOps as a maturing capability.

**Key concepts:**
- Essential Eight in pipelines
- BSIMM/OWASP SAMM maturity
- DevSecOps as a maturing capability

**Australian context:** Essential Eight application control, patching, and MFA
realised in automated delivery.

---

## Labs & Exercises

### Lab 1: IaC Security Audit (analysis activity)

**Objective:** Audit an Infrastructure-as-Code template against benchmarks and
produce a remediation plan.

**Prerequisites:**
- Topics 1–2 and F03

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Terraform, Checkov (IaC scanning) — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 20 GB disk (within the 8 GB / 4-core / 50 GB
  spec; no GPU)

**Instructions:**

1. Take a provided Terraform template (with deliberate misconfigurations).
2. Scan it with Checkov against benchmark policies.
3. Triage the findings by severity and false-positive likelihood.
4. Remediate the highest-severity issues in the template and re-scan.
5. Note which findings map to ASD Essential Eight expectations.
6. Recommend policy-as-code guardrails to prevent recurrence.

**Expected Output:**

A scan-driven IaC audit with triaged findings, remediation and re-scan evidence,
Essential Eight mapping, and policy-as-code recommendations. Learners can explain
which misconfigurations carried the most risk.

**Reflection Questions:**

1. Which misconfiguration was most dangerous, and why?
2. How does policy-as-code prevent the issue recurring?
3. Which findings map to Essential Eight, and how?

---

### Lab 2: SAST/DAST in CI/CD (build activity)

**Objective:** Integrate a SAST/DAST tool into a sample CI/CD pipeline with a
security gate.

**Prerequisites:**
- Topics 3–6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: a Git repo + CI runner (e.g. GitHub Actions/GitLab CI locally or
  equivalent), Semgrep (SAST), a sample app — all free/free-tier
- Minimum hardware: 6 GB RAM / 2 vCPU / 25 GB disk (within spec; no GPU)

**Instructions:**

1. Take a sample application repository with a CI pipeline.
2. Integrate Semgrep (SAST) as a pipeline stage.
3. Configure a risk-based gate (fail on high-severity, warn on lower).
4. Run the pipeline; review the findings and tune to reduce noise.
5. Add a dependency-scan (SCA) step and note its supply-chain link (SC04).
6. Document how the gates secure delivery without blocking it.

**Expected Output:**

A CI pipeline with integrated SAST (and SCA) and a risk-based gate, with tuned
findings and documentation of the delivery trade-off. Learners can justify the gate
thresholds.

**Reflection Questions:**

1. How did you set the gate to avoid blocking delivery with noise?
2. Where does SCA connect to supply-chain risk (SC04)?
3. What does this pipeline reveal about the team's DevSecOps maturity (SAMM)?

---

## Assessment

### Formative Assessment: Misconfig & Gate Drill

**Type:** Self-check exercise with answer key

**Description:** Given IaC findings and pipeline scenarios, students set risk-based
gates and map issues to Essential Eight. Self-marked.

**Learning Outcomes Assessed:** LO1, LO5

**Feedback mechanism:** Answer key with the gating decisions and mappings.

---

### Summative Assessment: DevSecOps Design & Implementation

**Type:** Practical report

**Description:** For an assigned cloud-native delivery scenario, students (a) audit
and remediate IaC, (b) design container and pipeline security, (c) integrate SAST/
DAST/SCA with risk-based gates, and (d) align the approach to the Essential Eight and
assess DevSecOps maturity (SAMM/BSIMM). Deliverable: a pipeline + a 2,500–3,000 word
report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| IaC audit & remediation | LO1 |
| Container & pipeline security | LO2, LO3 |
| SAST/DAST/SCA integration | LO4 |
| Essential Eight & maturity | LO5, LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| IaC & container security | Thorough, benchmark-driven | Sound | Partial | Weak |
| Pipeline security | Well-gated, secrets-safe, signed | Adequate | Gaps | Poor |
| Testing integration | Effective, tuned, risk-based | Reasonable | Noisy/blocking | Poor |
| E8 & maturity | Precise mapping; maturity-aware | Mostly | Superficial | Absent |
| Communication | Clear, professional | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Application control, patching, and MFA realised in
  automated pipelines.
- **ACSC cloud/secure-configuration guidance:** Reference for IaC and container
  hardening.
- **DevSecOps maturity:** Tracked via BSIMM/OWASP SAMM (see `docs/maturity-models.md`).

---

## Further Reading

**Bridgecrew / Checkov (2024).** *Checkov Documentation.* https://www.checkov.io
> Relevance: The free IaC-scanning tool used in Lab 1.

**Semgrep (2024).** *Semgrep Documentation.* https://semgrep.dev/docs/
> Relevance: The free SAST tool integrated in Lab 2.

**CIS (2024).** *CIS Benchmarks (cloud, container, IaC).* Center for Internet Security. https://www.cisecurity.org/cis-benchmarks
> Relevance: The benchmark policies used to audit IaC and containers.

**OWASP (2024).** *OWASP SAMM & DevSecOps guidance / BSIMM.* https://owaspsamm.org / https://www.bsimm.com
> Relevance: The software-assurance maturity models for Topic 6 (see `docs/maturity-models.md`).

**Australian Cyber Security Centre (2024).** *Cloud security & Essential Eight guidance.* ACSC. https://www.cyber.gov.au
> Relevance: Australian cloud/secure-configuration expectations (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SE05 |
| Unit Title | Security in Cloud & DevSecOps |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Security Engineering |
| Prerequisites | SE02, F03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | None directly (ASD Essential Eight) |
