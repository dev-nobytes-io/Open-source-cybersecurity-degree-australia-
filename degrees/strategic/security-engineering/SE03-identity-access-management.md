# SE03: Identity & Access Management

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved (security architecture/engineering)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Identity is the modern security perimeter, and this unit teaches its engineering:
designing identity and access management (IAM) architectures, privileged access
management (PAM), federation and single sign-on (SAML 2.0 / OIDC), multi-factor
authentication, and directory services. The emphasis is on architecting identity so
that access is least-privilege, auditable, and resilient — because most modern
intrusions are, ultimately, identity compromises.

IAM is central to Zero Trust (SE02) and to nearly every control framework. In the
Australian context it is shaped by **APRA CPS 234** access-control requirements,
the ASD Essential Eight (MFA, restrict admin privileges), and **Privacy Act 1988**
obligations for the personal data that identity systems hold. SE03 builds on SE02 and
F02 (Operating Systems/AD), and feeds SE04–SE06.

---

## Prerequisites

- SE02 — Security Architecture
- F02 — Operating Systems & Administration

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Design** an IAM architecture for an organisation, including directory and
   lifecycle.
2. **Analyse** privileged access risks and design PAM controls.
3. **Apply** federation and SSO (SAML 2.0 / OIDC) in a lab environment.
4. **Evaluate** authentication design, including MFA and phishing-resistant methods.
5. **Analyse** IAM against APRA CPS 234, Essential Eight, and Privacy Act
   obligations.
6. **Recommend** an IAM design that enforces least privilege and auditability.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of IAM, PAM,
federation, and authentication design.

**Skills (AQF 7.2):** Students develop design and technical skills by architecting
IAM and configuring federation.

**Application (AQF 7.3):** Students apply IAM engineering to realistic Australian
organisations with regulatory alignment.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Architect (652) | SP-ARC-002 | T0050 | Design identity and access management architecture | Lab 1 — IAM & PAM Design |
| NIST NICE DCWF | 2023 | System Administrator | OM-ADM-001 | T0431 | Configure federated identity and authentication | Lab 2 — Federation with OIDC/SAML |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Solution architecture | ARCH | Level 4–5 | Lab 1 |
| Identity & access management | IAMT | Level 4 | Lab 1, Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Security Architecture | Identity & Access | Practitioner–Advanced | Lab 1, Lab 2 |

---

## Topics

### Topic 1: Identity as the Perimeter

This topic frames identity as the primary control plane: most breaches involve
credential or identity abuse, and Zero Trust (SE02) makes identity central. It
introduces the IAM domains (authentication, authorisation, administration, audit).

**Key concepts:**
- Identity as the modern perimeter
- The IAM domains (AAA + audit)
- Identity in Zero Trust

---

### Topic 2: IAM Architecture and Lifecycle

This topic covers designing IAM: directory services, identity lifecycle
(joiner/mover/leaver), provisioning/de-provisioning, role/attribute-based access, and
access certification — engineering least privilege at scale.

**Key concepts:**
- Directory services and identity stores
- Joiner/mover/leaver lifecycle
- RBAC/ABAC and access certification

---

### Topic 3: Privileged Access Management

Privileged accounts are the crown jewels. This topic covers PAM design: vaulting,
just-in-time access, session monitoring, and breaking glass — and how PAM implements
the Essential Eight "restrict administrative privileges" mitigation.

**Key concepts:**
- PAM: vaulting, JIT, session monitoring
- Tiering and break-glass
- Essential Eight privilege restriction

**Australian context:** Maps to the Essential Eight "restrict administrative
privileges" mitigation.

---

### Topic 4: Federation and Single Sign-On

This topic teaches federation: SAML 2.0 and OIDC/OAuth 2.0 flows, identity providers
and relying parties, token handling, and the security considerations of SSO (and its
blast radius).

**Key concepts:**
- SAML 2.0 and OIDC/OAuth 2.0 flows
- IdP/RP trust and token handling
- SSO benefits and blast-radius risk

---

### Topic 5: Authentication and MFA

This topic covers authentication design: factors, MFA, and phishing-resistant methods
(FIDO2/passkeys), and designing authentication that is both strong and usable —
mapping to the Essential Eight MFA mitigation.

**Key concepts:**
- Authentication factors and MFA
- Phishing-resistant authentication (FIDO2/passkeys)
- Strength vs usability

**Australian context:** Maps to the Essential Eight multi-factor authentication
mitigation.

---

### Topic 6: IAM Governance and Compliance

This topic covers governing identity: access reviews, segregation of duties, audit,
and aligning IAM to APRA CPS 234 access requirements and Privacy Act obligations for
the personal data identity systems hold.

**Key concepts:**
- Access reviews and segregation of duties
- IAM audit and evidence
- APRA CPS 234 / Privacy Act alignment

**Australian context:** APRA CPS 234 access control and Privacy Act 1988 obligations.

---

## Labs & Exercises

### Lab 1: IAM & PAM Design (design activity)

**Objective:** Design an IAM architecture with privileged-access controls for a
fictional organisation.

**Prerequisites:**
- Topics 1–3 and 6

**Environment:**
- Operating System: any
- Tools: draw.io, an IAM design template — all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Take a fictional Australian organisation (sector, size, regulatory context).
2. Design the IAM architecture: directory, lifecycle, RBAC/ABAC, certification.
3. Design PAM controls (vaulting, JIT, session monitoring, tiering, break-glass).
4. Map privileged controls to the Essential Eight "restrict admin privileges".
5. Address APRA CPS 234 access requirements and Privacy Act data handling.
6. Identify the top three identity risks and how the design mitigates them.

**Expected Output:**

An IAM + PAM architecture with lifecycle, access model, privileged controls, and
regulatory alignment. Learners can justify least-privilege and auditability by
design.

**Reflection Questions:**

1. Which identity risk is hardest to mitigate, and how did you address it?
2. How does your PAM design implement Essential Eight privilege restriction?
3. What Privacy Act obligations does the identity store create?

---

### Lab 2: Federation with OIDC/SAML (config activity)

**Objective:** Configure federated identity (SAML 2.0 or OIDC) in a lab environment.

**Prerequisites:**
- Topics 4–5 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Keycloak (open-source IdP), a sample relying-party app — all free/OSS
- Minimum hardware: 4 GB RAM / 2 vCPU / 20 GB disk (within spec; no GPU)

**Instructions:**

1. Stand up Keycloak as an identity provider in the lab.
2. Configure a realm, a user, and a client (relying party) using OIDC (or SAML 2.0).
3. Complete an authentication flow from the relying party through the IdP.
4. Enable MFA for the user and re-test the flow.
5. Inspect the tokens/assertions and note the security-relevant claims.
6. Document the trust relationship and one risk of the SSO design.

**Expected Output:**

A working federated authentication flow with MFA, an inspection of the
tokens/assertions, and a documented trust relationship and risk. Learners can explain
the OIDC/SAML flow and its security considerations.

**Reflection Questions:**

1. What is the blast radius if the IdP is compromised, and how would you reduce it?
2. Why is phishing-resistant MFA preferable, and where would you require it?
3. Which token claims matter most for authorisation decisions?

---

## Assessment

### Formative Assessment: IAM Control Drill

**Type:** Self-check exercise with answer key

**Description:** Given access scenarios, students select the appropriate IAM/PAM
control and map it to the relevant Essential Eight mitigation. Self-marked.

**Learning Outcomes Assessed:** LO2, LO5

**Feedback mechanism:** Answer key with the control and mapping.

---

### Summative Assessment: IAM Architecture Design

**Type:** Design report

**Description:** For an assigned Australian organisation, students (a) design an IAM
architecture with lifecycle and access model, (b) design PAM controls, (c) specify
federation and MFA, and (d) align the design to APRA CPS 234, the Essential Eight,
and the Privacy Act. Deliverable: 2,500–3,000 word design with diagrams.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| IAM architecture | LO1, LO6 |
| PAM design | LO2 |
| Federation & MFA | LO3, LO4 |
| Regulatory alignment | LO5 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| IAM design | Least-privilege, auditable, lifecycle-complete | Sound | Partial | Weak |
| PAM design | Robust privileged controls | Adequate | Gaps | Poor |
| Federation & MFA | Correct, secure, phishing-resistant | Mostly | Uneven | Poor |
| Regulatory alignment | Precise APRA/E8/Privacy mapping | Mostly | Superficial | Absent |
| Communication | Clear, well-diagrammed | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **APRA CPS 234:** Access-control requirements for regulated entities.
- **ASD Essential Eight:** MFA and restrict-administrative-privileges mitigations.
- **Privacy Act 1988:** Obligations for personal data held in identity systems.

---

## Further Reading

**NIST (2017+).** *SP 800-63 Digital Identity Guidelines.* NIST. https://pages.nist.gov/800-63-3/
> Relevance: The authoritative guidance on identity proofing and authentication (Topics 1, 5).

**Keycloak (2024).** *Keycloak Documentation.* https://www.keycloak.org/documentation
> Relevance: The free identity provider used for the federation lab.

**OpenID Foundation & OASIS (2024).** *OpenID Connect & SAML 2.0 specifications.* https://openid.net / https://www.oasis-open.org
> Relevance: The federation protocols configured in Lab 2.

**APRA (2019).** *Prudential Standard CPS 234 — access control.* APRA. https://www.apra.gov.au
> Relevance: The Australian access-control obligations for Topic 6 (Australian source).

**Australian Cyber Security Centre (2024).** *Essential Eight — MFA & restrict admin privileges.* ACSC. https://www.cyber.gov.au/essential-eight
> Relevance: The Australian MFA/privilege mitigations mapped throughout (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | SE03 |
| Unit Title | Identity & Access Management |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | Security Engineering |
| Prerequisites | SE02, F02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | APRA CPS 234; Privacy Act 1988 |
