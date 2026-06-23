# Framework Alignment Reference

> This document maps every degree component to the industry and education frameworks it addresses. It is the primary reference for demonstrating that this degree produces workforce-ready graduates aligned to recognised standards.

> 📊 For NICE/DCWF coverage specifically: the [KSAT Coverage Map](ksat-coverage.md)
> is the full text index, and the interactive [Program Builder](program-builder/index.md)
> visualises work-role completion and KSAT coverage for any course selection you make.

---

## Framework Index

| Framework | Type | Relevance |
|---|---|---|
| **TEQSA / AQF Level 7** | Education standard | Governs the academic rigour and qualification level of all units |
| **NIST NICE / DCWF** | Workforce framework | Maps roles, tasks, knowledge, and skills to cybersecurity work categories |
| **DoD 8140 / DoD 8570** | Workforce framework | US DoD workforce qualification requirements; referenced by AU defence sector |
| **SFIA 9** | Skills framework | Skills Framework for the Information Age — professional skills and levels |
| **CIISec Skills Framework** | Skills framework | Chartered Institute of Information Security — practitioner competencies |
| **ASD Cyber Skills Framework** | Skills framework | Australian Signals Directorate workforce skills framework |
| **MITRE ATT&CK** | Threat framework | Adversary tactics, techniques, and procedures taxonomy |
| **MITRE CTID** | Threat framework | Center for Threat-Informed Defense — emulation and detection methodology |
| **NIST CSF 2.0** | Security framework | NIST Cybersecurity Framework — Govern, Identify, Protect, Detect, Respond, Recover |
| **NIST SP 800 Series** | Technical standards | NIST Special Publications — detailed security guidance |
| **NIST SP 800-61** | Incident response | Computer Security Incident Handling Guide |
| **PICERL** | Incident response | Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned |
| **ISO 27001/27002** | Security standard | International information security management standard |
| **ASD Essential Eight** | Security controls | Australian Government baseline security controls |
| **APRA CPS 234** | Regulatory | Australian Prudential Regulation Authority — information security standard |
| **SOC-CMM** | Capability maturity | SOC Capability Maturity Model (security operations) |
| **CTI-CMM** | Capability maturity | Cyber Threat Intelligence Capability Maturity Model |
| **SIM3** | Capability maturity | Security Incident Management Maturity Model (IR/CSIRT/DFIR) |
| **Hunting Maturity Model / PEAK** | Capability maturity | Threat-hunting maturity and process |
| **Detection Maturity Level (DML) / M3TID** | Capability maturity | Detection maturity; Measure/Maximize/Mature Threat-Informed Defense (CTID) |
| **C2M2 / O-ISM3 / CMMI** | Program maturity | Enterprise cyber program, ISMS, and process maturity |

> See [`docs/maturity-models.md`](maturity-models.md) for the full capability-maturity
> cross-walk (model → capability/service → NIST CSF 2.0 → NICE/DCWF role → KSATs),
> spanning both the Operational and Strategic degrees.

---

## NIST NICE / DCWF Mapping

The NIST Workforce Framework for Cybersecurity (NICE) and the DoD Cyber Workforce Framework (DCWF) both use Work Roles composed of Tasks, Knowledge (K), Skills (S), and Abilities (A).

```mermaid
graph LR
    subgraph NICE["NIST NICE Work Role Categories"]
        N1["Securely Provision (SP)"]
        N2["Operate & Maintain (OM)"]
        N3["Oversee & Govern (OV)"]
        N4["Protect & Defend (PD)"]
        N5["Analyse (AN)"]
        N6["Collect & Operate (CO)"]
        N7["Investigate (IN)"]
    end

    N4 --> TH["Threat Hunting Major"]
    N4 --> DE["Detection Eng. Major"]
    N7 --> DFIR["DFIR Major"]
    N5 --> CTI["CTI Major"]
    N6 --> CTE["CTE Major"]
    N1 --> SE["Security Eng. Major"]
    N3 --> LD["Leadership Major"]
    N3 --> GRC["GRC Major"]
```

### NICE Work Role to Major Mapping

| NICE Work Role | DCWF Code | Degree Major |
|---|---|---|
| Cyber Defense Analyst | 511 | Detection Engineering, Threat Hunting |
| Cyber Defense Incident Responder | 531 | DFIR |
| Threat/Warning Analyst | 621 | CTI |
| All-Source Analyst | 611 | CTI |
| Vulnerability Assessment Analyst | 541 | CTE |
| Exploitation Analyst | 711 | CTE |
| System Security Analyst | 461 | Security Engineering |
| Security Architect | 652 | Security Engineering |
| Cyber Policy & Strategy Planner | 752 | GRC, Leadership |
| Executive Cyber Leadership | 901 | Leadership |
| Information Systems Security Manager | 722 | GRC, Leadership |

---

## MITRE ATT&CK Coverage by Major

ATT&CK is structured as Tactics → Techniques → Sub-techniques. Each major engages with ATT&CK differently:

```mermaid
mindmap
  root((MITRE ATT&CK))
    Threat Hunting
      All 14 tactics
      Hunting by technique
      Navigator proficiency
    DFIR
      Impact, Exfiltration, C2
      Execution, Persistence
      Lateral Movement
    CTI
      Actor-technique mapping
      Campaign analysis
      Group profiles
    Detection Engineering
      Detection-per-technique
      Coverage gap analysis
      Sigma rule authoring
    Cyber Threat Emulation
      Emulation plan execution
      All 14 tactics
      Sub-technique precision
```

### ATT&CK Tactic Coverage by Major

| Tactic | TH | DFIR | CTI | DE | CTE |
|---|---|---|---|---|---|
| Reconnaissance | Partial | | Full | Partial | Full |
| Resource Development | Partial | | Full | Partial | Full |
| Initial Access | Full | Full | Full | Full | Full |
| Execution | Full | Full | Full | Full | Full |
| Persistence | Full | Full | Full | Full | Full |
| Privilege Escalation | Full | Full | Partial | Full | Full |
| Defense Evasion | Full | Full | Full | Full | Full |
| Credential Access | Full | Full | Partial | Full | Full |
| Discovery | Full | Full | Partial | Full | Full |
| Lateral Movement | Full | Full | Full | Full | Full |
| Collection | Partial | Full | Partial | Full | Full |
| C2 | Full | Full | Full | Full | Full |
| Exfiltration | Full | Full | Full | Full | Full |
| Impact | Partial | Full | Full | Full | Full |

---

## NIST CSF 2.0 Function Mapping

NIST CSF 2.0 organises controls into six functions: **Govern, Identify, Protect, Detect, Respond, Recover**.

```mermaid
pie title NIST CSF 2.0 Coverage Distribution
    "Govern (GV)" : 15
    "Identify (ID)" : 15
    "Protect (PR)" : 15
    "Detect (DE)" : 25
    "Respond (RS)" : 20
    "Recover (RC)" : 10
```

| CSF 2.0 Function | Primary Coverage | Secondary Coverage |
|---|---|---|
| **GV — Govern** | GRC, Leadership | Security Engineering |
| **ID — Identify** | GRC, Security Engineering | CTI |
| **PR — Protect** | Security Engineering, GRC | Detection Engineering |
| **DE — Detect** | Detection Engineering, Threat Hunting | DFIR |
| **RS — Respond** | DFIR | Threat Hunting, CTI |
| **RC — Recover** | DFIR | GRC, Leadership |

---

## SFIA 9 Skills Mapping

SFIA (Skills Framework for the Information Age) defines 121 skills across 7 responsibility levels (1=Follow to 7=Set strategy).

| SFIA Skill Code | SFIA Skill Name | Degree Major | SFIA Level |
|---|---|---|---|
| INAS | Information Assurance | Threat Hunting, CTI | 3–5 |
| SCAD | Security Administration | Detection Engineering | 3–4 |
| PENT | Penetration Testing | CTE | 4–5 |
| SURE | Systems & Software Assurance | DFIR, Security Engineering | 4–5 |
| ARCH | Solution Architecture | Security Engineering | 5–6 |
| IRMG | Information Risk Management | GRC | 5–6 |
| MANA | Management | Leadership | 6–7 |
| PROG | Programming | Foundation | 3 |
| NTAS | Network Support | Foundation | 3 |
| ITOP | IT Operations | Foundation | 2–3 |
| CNSL | Consultancy | GRC, Leadership | 5–6 |

---

## ASD Cyber Skills Framework

The Australian Signals Directorate Cyber Skills Framework (ASD CSF) defines competencies specific to the Australian context.

> Note: The ASD CSF is aligned with but distinct from the NICE framework. It incorporates Australian legislative and regulatory context.

| ASD CSF Domain | Degree Coverage |
|---|---|
| Cyber Defence | Detection Engineering, Threat Hunting |
| Incident Management | DFIR |
| Threat Intelligence | CTI |
| Offensive Cyber | CTE |
| Security Architecture | Security Engineering |
| Cyber Governance | GRC, Leadership |
| Technical Foundations | Foundation Year |

---

## CIISec Skills Framework

The Chartered Institute of Information Security defines competency areas for information security professionals.

| CIISec Area | Degree Coverage |
|---|---|
| Cyber Operations | Threat Hunting, DFIR, Detection Engineering |
| Threat Intelligence & Investigation | CTI, Threat Hunting |
| Digital Forensics | DFIR |
| Penetration Testing & Red Teaming | CTE |
| Security Architecture | Security Engineering |
| Governance, Risk & Compliance | GRC |
| Security Management | Leadership |

---

## Australian Regulatory Framework Mapping

| Regulation / Standard | Unit Coverage |
|---|---|
| **Privacy Act 1988** | F05, GR04 |
| **Notifiable Data Breaches (NDB) scheme** | F05, DF05, GR04 |
| **Security of Critical Infrastructure Act 2018** | F05, GR04 |
| **APRA CPS 234** | GR04, SC03 |
| **ASD Essential Eight** | F04, DE02, GR03 |
| **Australian Government ISM** | GR03, SE02 |
| **IRAP assessment process** | GR05 |
| **Australian Evidence Act 1995** | DF01 |
| **Cybercrime Act 2001** | F05, CE01 |
| **TIBER-AU** | CE05 |

---

## Certification Alignment

This degree does not replace certifications — it prepares learners to pursue them with a structured foundation. Mapped certifications are recommended, not required.

```mermaid
graph TD
    subgraph ENTRY["Entry-Level Certifications"]
        C1["CompTIA Security+"]
        C2["CompTIA CySA+"]
        C3["BTL1 / BTL2"]
    end

    subgraph MID["Mid-Level Certifications"]
        C4["GIAC GCIH"]
        C5["GIAC GCFE / GCFA"]
        C6["GIAC GCTI"]
        C7["GIAC GDAT"]
        C8["eCIR / eCTHP"]
        C9["OSCP"]
    end

    subgraph SENIOR["Senior Certifications"]
        C10["GIAC GPEN / GRTOP"]
        C11["CISSP"]
        C12["CISM"]
        C13["CRISC"]
        C14["SABSA SCF"]
        C15["ISO 27001 Lead Impl."]
    end

    Foundation --> C1 & C2 & C3
    TH_DFIR["Threat Hunting / DFIR"] --> C4 & C5 & C8
    CTI_DE["CTI / Detection Eng."] --> C6 & C7
    CTE_M["CTE Major"] --> C9 & C10
    GRC_LD["GRC / Leadership"] --> C11 & C12 & C13 & C14 & C15
```

---

## Capability Maturity Models

Capability maturity models are integrated across **both** degrees so that
operational capability development and strategic program/governance/risk
development stay aligned (see [`docs/maturity-models.md`](maturity-models.md) for
the full cross-walk).

| Model | Capability assessed | Degree home |
|---|---|---|
| SOC-CMM | Security operations / SOC (incl. Services) | OC02; operational majors |
| CTI-CMM | Cyber threat intelligence | OC05; CTI major |
| SIM3 | Incident management / DFIR (CSIRT) | OC04; DFIR major |
| Hunting Maturity Model + PEAK | Threat hunting | Threat Hunting major |
| Detection Maturity Level (DML) + M3TID | Detection engineering / TID | Detection Engineering major |
| C2M2 | Enterprise cyber program | SC03, SC05 |
| O-ISM3 | Information security management system | SC03, SC05 |
| SSE-CMM (ISO/IEC 21827) | Systems security engineering | Security Engineering major (SE01/SE02) |
| BSIMM + OWASP SAMM | Software security / assurance | Security Engineering major (SE01/SE05) |
| OCEG GRC Capability Model | Governance, risk & compliance | GRC major (GR01/GR06) |
| RIMS Risk Maturity Model | Risk management | GRC major (GR02) |
| CMMI | General process maturity | SC05; LD02 (reference) |
| NIST CSF 2.0 Tiers | Program/risk governance posture | SC01, SC05; LD02 |
| ASD Essential Eight Maturity Model | Baseline mitigations | F04, SC05, LD02 |

> The strategic program units (SC01 risk, SC03 governance, SC05 program management)
> and the Leadership major **consume the operational maturity scores as inputs** —
> program maturity aggregates capability maturity. This is the mechanism that
> prevents an operational/strategic development mismatch.

---

## Framework Currency & Maintenance

Industry frameworks are living documents. This repo must track version currency.
The table below is the canonical version reference; every unit's framework
mappings must use these versions until the Framework Custodian updates them.

| Framework | Version used in this repo | Last verified | Review frequency | Currency note |
|---|---|---|---|---|
| NIST CSF | 2.0 (2024) | 2026-06-21 | Major version change | Current. 2.0 introduced the **Govern** function (used in SC03/SC05). |
| NIST NICE | SP 800-181r1 (2020) + 2025 components data | 2026-06-21 | Major version change | NICE now maintains Tasks/Knowledge/Skills as versioned component data — re-verify against the live NICE site. |
| DCWF | 2023 | 2026-06-21 | Annual | DCWF work-role/T-code IDs in unit mappings must be re-confirmed against the current release at Framework Custodian sign-off. |
| SFIA | Version 9 (2023) | 2026-06-21 | Major version change | Current — SFIA 9 is the latest major version. |
| ASD Cyber Skills Framework | 2024 | 2026-06-21 | ASD revision | Used for the ASD CSF mapping in every unit. Re-verify domain/sub-domain labels against the current ASD publication. |
| ASD Essential Eight | November 2023 maturity model | 2026-06-21 | Quarterly ASD review | Confirm against the latest ACSC Essential Eight Maturity Model. |
| MITRE ATT&CK | **v19 (2026)** | 2026-06-21 | Bi-annual (April, October) | **Current is v19, which introduced significant structural changes.** A repo-wide audit of every ATT&CK technique/tactic reference and mapping is required — see the audit task in the root `TODO.md`. Treat existing technique IDs as provisional until re-verified against v19. |
| ISO/IEC 27001 | 2022 edition | 2026-06-21 | Major version change | Current. Paywalled standard — referenced, not reproduced. |
| NIST SP 800-61 | Rev. 2 (with Rev. 3 in progress) | 2026-06-21 | Major version change | OC04 cites 800-61; check whether Rev. 3 has finalised and update if so. |
| Capability maturity models (SOC-CMM, CTI-CMM, SIM3, HMM, DML, M3TID, C2M2, O-ISM3) | current editions | 2026-06-21 | Per model release | Integrated via `docs/maturity-models.md`. Re-verify on each model's new release. **"DF-C2M2"** name to be confirmed (SIM3 used as the IR/DFIR maturity model). |

### Currency Review Log

| Date | Reviewer | Outcome |
|---|---|---|
| 2026-06-21 | _initial structural review_ | Versions reconciled across `docs/frameworks.md` and all 18 core units. Flagged NICE/DCWF T-codes as requiring live re-verification at Framework Custodian sign-off. |
| 2026-06-21 | _maintainer note_ | **MITRE ATT&CK confirmed current at v19** (significant structural changes vs v16). Version pointers updated repo-wide; full technique/tactic **mapping audit raised as a tracked task** — existing technique IDs are provisional until re-verified against v19. |

> When a framework releases a new major version, a GitHub Issue should be raised
> (use the **Framework Mapping Error** issue template) to audit and update affected
> units. The Framework Custodian initiates this within 90 days of release per
> [`docs/governance.md`](governance.md) §3. Record each review as a row in the
> log above.
