# Curriculum Map

This document provides a single-view map of the entire degree, showing how every
unit relates to AQF Level 7 descriptors, NICE DCWF categories, SFIA skill levels,
Bloom's taxonomy levels, and assessment types.

It is intended for accreditation reviewers, institutional partners, and educators
who need to understand the degree at a glance.

---

## 1. Degree Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│  LAYER 1 — FOUNDATION YEAR (All students · 48 CP)                      │
│  F01  F02  F03  F04  F05  F06                                           │
│  Bloom's 1–3 · SFIA 1–2 · ASD Awareness–Foundation                     │
└─────────────────────────────────┬───────────────────────────────────────┘
                                  │
            ┌─────────────────────┴─────────────────────┐
            │                                           │
┌───────────▼──────────────┐             ┌──────────────▼──────────────┐
│  OPERATIONAL CORE (48 CP)│             │  STRATEGIC CORE (48 CP)     │
│  OC01–OC06               │             │  SC01–SC06                  │
│  Bloom's 3–4 · SFIA 2–3  │             │  Bloom's 3–4 · SFIA 2–3     │
└───────────┬──────────────┘             └──────────────┬──────────────┘
            │                                           │
   ┌────────┴────────┐                        ┌────────┴────────┐
   │  OPERATIONAL    │                        │  STRATEGIC      │
   │  MAJORS (72 CP) │                        │  MAJORS (72 CP) │
   │  Bloom's 4–6    │                        │  Bloom's 4–6    │
   │  SFIA 3–5       │                        │  SFIA 3–5       │
   │                 │                        │                 │
   │ · Threat Hunting│                        │ · Sec. Eng.     │
   │ · DFIR          │                        │ · Leadership    │
   │ · CTI           │                        │ · GRC           │
   │ · Detection Eng.│                        │                 │
   │ · CTE           │                        │                 │
   └─────────────────┘                        └─────────────────┘
```

---

## 2. Foundation Year — Unit Map

| Code | Title | AQF Descriptor | NICE DCWF Category | SFIA Level | Bloom's | Assessment Type |
|---|---|---|---|---|---|---|
| F01 | Networking Fundamentals | Knowledge + Skills | Any (infrastructure) | 1–2 | 1–3 | Lab report + practical quiz |
| F02 | OS & Administration | Knowledge + Skills | OM — Operate & Maintain | 1–2 | 1–3 | Lab report + practical quiz |
| F03 | Scripting & Automation | Skills + Application | SP — Securely Provision | 1–2 | 2–3 | Code + commentary |
| F04 | Security Concepts & Principles | Knowledge | PR — Protect & Defend | 1–2 | 1–3 | Short answer + scenario |
| F05 | Legal, Ethics & Australian Compliance | Knowledge + Application | OV — Oversee & Govern | 1–2 | 2–3 | Case study analysis |
| F06 | Data & Log Analysis | Skills + Application | PR — Protect & Defend | 1–2 | 2–3 | Lab report + query exercise |

**Foundation Year coverage summary:**
- AQF: Primarily Knowledge descriptor; Skills and Application introduced
- NICE DCWF: Foundational coverage across PR, OM, SP, OV categories
- SFIA: Levels 1–2 (Follow, Assist)
- Bloom's: Levels 1–3 (Remember, Understand, Apply)

---

## 3. Operational Core — Unit Map

| Code | Title | AQF Descriptor | NICE DCWF | SFIA Level | Bloom's | Assessment Type |
|---|---|---|---|---|---|---|
| OC01 | Adversary Tradecraft & TTPs | Knowledge + Skills | AN — Analyse | 2–3 | 3–4 | ATT&CK mapping exercise |
| OC02 | Security Monitoring & SIEM | Skills + Application | PR — Protect & Defend | 2–3 | 3–4 | Detection use case + lab |
| OC03 | Malware Analysis Fundamentals | Skills + Application | AN — Analyse | 2–3 | 3–4 | Malware analysis report |
| OC04 | Incident Response Lifecycle | Skills + Application | PR — Protect & Defend | 2–3 | 3–4 | IR playbook + tabletop |
| OC05 | Threat Intelligence Fundamentals | Knowledge + Skills | AN — Analyse | 2–3 | 3–4 | Intelligence report |
| OC06 | Offensive Security Concepts | Skills + Application | CO — Collect & Operate | 2–3 | 3–4 | Recon report + ethics analysis |

---

## 4. Strategic Core — Unit Map

| Code | Title | AQF Descriptor | NICE DCWF | SFIA Level | Bloom's | Assessment Type |
|---|---|---|---|---|---|---|
| SC01 | Risk Management Frameworks | Knowledge + Application | OV — Oversee & Govern | 2–3 | 3–4 | Risk assessment |
| SC02 | Security Architecture Principles | Knowledge + Skills | SP — Securely Provision | 2–3 | 3–4 | Architecture design exercise |
| SC03 | Governance, Policy & Compliance | Knowledge + Application | OV — Oversee & Govern | 2–3 | 3–4 | Policy document |
| SC04 | Vendor & Supply Chain Risk | Application | OV — Oversee & Govern | 2–3 | 3–4 | Vendor risk assessment |
| SC05 | Security Program Management | Application | OV — Oversee & Govern | 3 | 3–4 | Program roadmap |
| SC06 | Stakeholder Communication | Application | OV — Oversee & Govern | 3 | 3–4 | Board presentation |

---

## 5. Major-Level Coverage Map

### Operational Majors

| Major | NICE DCWF Primary | ATT&CK Coverage | SFIA Level | Bloom's | Capstone Output |
|---|---|---|---|---|---|
| Threat Hunting | PR-CDA-001, AN-TWA-001 | All 14 tactics | 3–5 | 4–6 | Hunt report + hypothesis library |
| DFIR | PR-CIR-001, IN-FOR-001 | Execution, Persistence, Exfiltration focus | 3–5 | 4–6 | Forensic investigation report |
| CTI | AN-TWA-001, AN-ASA-001 | All tactics (analytical) | 3–5 | 4–6 | Finished intelligence product |
| Detection Engineering | PR-CDA-001 | All 14 tactics (detection focus) | 3–5 | 4–6 | Detection library + coverage report |
| CTE | OP-OPL-001, PR-VAM-001 | Red team technique coverage | 3–5 | 4–6 | Emulation plan + assessment report |

### Strategic Majors

| Major | NICE DCWF Primary | Key Frameworks | SFIA Level | Bloom's | Capstone Output |
|---|---|---|---|---|---|
| Security Engineering | SP-ARC-001, SP-SSP-001 | NIST SP 800-160, SABSA, Zero Trust | 3–5 | 4–6 | Architecture design document |
| Leadership & CISO | OV-MGT-001, OV-EXL-001 | NIST CSF 2.0, CISM domains | 4–5 | 4–6 | 3-year security strategy + board brief |
| GRC | OV-LGA-001, OV-LGA-002 | ISO 27001, NIST CSF, APRA CPS 234 | 3–5 | 4–6 | Compliance framework + audit plan |

---

## 6. AQF Level 7 Descriptor Coverage Map

| AQF Descriptor | Primary Units | Secondary Units |
|---|---|---|
| **Knowledge** — Broad and coherent knowledge | F01–F06, OC01–OC06, SC01–SC06 | All major units |
| **Skills** — Cognitive and technical skills to analyse and evaluate | F03, F06, OC02–OC06, SC01–SC06 | All major units |
| **Application** — Autonomy, judgement, responsibility | F05, OC04, SC03–SC06 | Major units + capstone |

---

## 7. Australian Regulatory Framework Coverage Map

| Legislation / Framework | Primary Units | Notes |
|---|---|---|
| Privacy Act 1988 (Cth) | F05, GR01, DF04 | Mandatory in all units with data handling content |
| Notifiable Data Breaches (NDB) scheme | F05, OC04, DF01 | Mandatory in incident response units |
| Security of Critical Infrastructure Act 2018 | F05, SC01, GR02 | Coverage in risk and governance units |
| APRA CPS 234 | SC01, GR04 | Financial sector context in GRC major |
| ASD Essential Eight | F04, SC02, GR03 | Referenced across all layers |
| Australian Evidence Act 1995 | F05, DF04, DF05 | Digital forensics admissibility |
| Criminal Code Act 1995 (Cth) | F05, CE01 | Unauthorised access provisions |
| IRAP (ISM) | GR05, GR06 | GRC major; government sector focus |
| TIBER-AU | CE05, CE06 | CTE major; threat-led testing methodology |

---

## 8. Bloom's Taxonomy Progression Across the Degree

```
Foundation       Core            Major            Capstone
─────────────    ─────────────   ──────────────   ──────────────
1. Remember  ──► 3. Apply    ──► 4. Analyse   ──► 5. Evaluate
2. Understand    4. Analyse      5. Evaluate   ──► 6. Create
3. Apply
```

Each layer builds on the previous. A student who has not developed Apply-level
skills in Foundation will struggle with the Analyse requirements of Core units.
The prerequisite structure enforces this progression.

---

## 9. Credit Point and Volume of Learning Summary

| Component | Units | CP Each | Total CP | Student Hours (est.) |
|---|---|---|---|---|
| Foundation Year | 6 | 8 | 48 | 720–840 |
| Degree Core | 6 | 8 | 48 | 720–840 |
| Major Units | 6 | 8 | 48 | 720–840 |
| Capstone | 1 | 24 | 24 | 360–480 |
| **Total** | **19** | | **168** | **2,520–3,000** |

168 CP at 15–20 hours per credit point = 2,520–3,360 total hours.
This is consistent with a 3-year full-time equivalent degree at AQF Level 7.
