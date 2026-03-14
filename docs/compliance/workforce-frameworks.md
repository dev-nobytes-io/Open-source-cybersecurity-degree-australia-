# Workforce Framework Compliance

This document defines the compliance requirements for workforce framework mappings
across all units in the Open-Source Cybersecurity Degree. Every unit must map its
learning outcomes to recognized workforce frameworks.

Workforce framework alignment ensures:
1. Graduates can articulate their skills in terms employers and certifying bodies recognise
2. Content remains current and relevant to the cybersecurity workforce
3. The degree provides a credible bridge to industry certifications and job roles
4. **Students can visually demonstrate their NICE DCWF capabilities to employers** —
   every unit must contribute to a student-facing, employer-readable competency profile

---

## Student-Facing Competency Visibility — Design Requirement

This is a core design requirement of the degree, not an afterthought.

Every unit **must** be authored so that a student can answer the question:
> *"What specific NICE DCWF task codes did I demonstrate in this unit, and where is my evidence?"*

### Unit Authoring Requirements for Competency Visibility

Every unit must include, in its framework mapping table:
- **Work Role Code** — the DCWF work role code (e.g., `PR-CDA-001`)
- **Task Codes (T-codes)** — the specific T-codes demonstrated in labs or assessments
- **Evidence type** — whether each T-code is demonstrated via a lab, assessment, or both

T-codes must be traceable directly to a lab exercise or assessment task in the unit.
A T-code listed in the mapping table with no corresponding lab or assessment is invalid.

### Student Portfolio

Students use two templates to compile their employer-facing competency profile:
- `templates/competency-profile-template.md` — the human-readable skills passport
- `templates/student-portfolio/index.html` — the visual, multi-tab HTML portfolio
  with mermaid diagrams showing NICE DCWF coverage, work role profile, and evidence index

Unit authors must write content that feeds directly into these templates.
Specifically, the T-codes and work role codes documented in each unit's framework
mapping table must be directly usable by students when populating their portfolio.

---

## 1. Mapping Requirements Summary

### Minimum Requirements per Unit

Every unit must be mapped to **at least 2 of the following frameworks**, and
**at least 1 must be Australian:**

| Framework | Identifier | Australian? |
|---|---|---|
| NIST NICE / DoD Cyber Workforce Framework (DCWF) | NICE DCWF | No |
| Skills Framework for the Information Age (SFIA 9) | SFIA 9 | No |
| ASD Cyber Skills Framework | ASD CSF | **Yes** |
| CIISec Skills Framework | CIISec | No (UK, but used in AU) |
| DoD 8140.03 / 8570 (for defence-context units) | DoD 8140 | No |

**The ASD Cyber Skills Framework is the preferred Australian mapping** and is
strongly recommended for all units.

---

## 2. NIST NICE / DoD Cyber Workforce Framework (DCWF)

### About
The NICE Workforce Framework for Cybersecurity (NIST SP 800-181 rev 1) and the
DoD Cyber Workforce Framework (DCWF) define work roles, tasks, knowledge, and skills
for the cybersecurity workforce. The DCWF is the primary operational reference in
Australian Defence and aligned with ACSC guidance.

**Current version:** NIST NICE DCWF (November 2023 update)

### Reference Format

Mappings must specify:
- **Work Role** — the DCWF Work Role name and code (e.g., Cyber Defense Analyst — PR-CDA-001)
- **Tasks (T-codes)** — specific task codes relevant to the unit's learning outcomes
- **Knowledge (K-codes)** — specific knowledge codes addressed by the unit (optional but encouraged)

```markdown
| Framework | Version | Work Role | Work Role Code | Tasks |
|---|---|---|---|---|
| NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0020, T0023, T0166 |
```

### Work Role Alignment by Unit Type

| Unit Layer | Required DCWF Category |
|---|---|
| Operational units (OC, TH, DF, CT, DE, CE) | Protect & Defend (PR), Investigate (IN), or Operate & Maintain (OM) |
| Strategic units (SC, LD, GR, SE) | Oversee & Govern (OV) or Securely Provision (SP) |
| Foundation units | Any DCWF category relevant to content |

### Key DCWF Work Roles for This Degree

| Work Role | Code | Relevant Majors |
|---|---|---|
| Cyber Defense Analyst | PR-CDA-001 | OC, TH, DE |
| Cyber Defense Incident Responder | PR-CIR-001 | OC, DF |
| Vulnerability Assessment Analyst | PR-VAM-001 | CE, DE |
| Threat/Warning Analyst | AN-TWA-001 | CT, TH |
| Cyber Intelligence Planner | AN-PLN-001 | CT |
| Digital Forensics Analyst | IN-FOR-001 | DF |
| Cyber Operations Planner | OP-OPL-001 | CE |
| Security Architect | SP-ARC-001 | SE, SC |
| Systems Security Analyst | SP-SSP-001 | SE, SC |
| Authorizing Official/Designated Representative | OV-LGA-001 | GR, LD |
| Privacy Officer/Privacy Compliance Manager | OV-LGA-002 | GR, LD |
| Information Systems Security Manager | OV-MGT-001 | GR, LD, SC |

---

## 3. Skills Framework for the Information Age (SFIA 9)

### About
SFIA 9 is a globally recognised framework for IT and digital skills. It is widely
used by Australian employers, the Australian Computer Society (ACS), and the
Digital Transformation Agency (DTA) for workforce planning and job design.

**Current version:** SFIA 9 (2023)

### Reference Format

Mappings must specify:
- **Skill Code** — the 4-letter SFIA skill code (e.g., INAS for Information Security)
- **Skill Name** — the full SFIA skill name
- **Level** — SFIA responsibility level (1–7) appropriate for the unit's layer

```markdown
| Framework | Version | Skill | Code | Level |
|---|---|---|---|---|
| SFIA 9 | 2023 | Information security | INAS | 3 |
| SFIA 9 | 2023 | Threat intelligence | THIN | 4 |
```

### SFIA Level Alignment by Degree Layer

| Degree Layer | SFIA Levels |
|---|---|
| Foundation Year | Levels 1–2 (Follow, Assist) |
| Core (Operational/Strategic) | Levels 2–3 (Assist, Apply) |
| Major Units | Levels 3–5 (Apply, Enable, Ensure/Advise) |
| Capstone | Level 4–5 (Enable, Ensure/Advise) |

### Key SFIA Skills for This Degree

| Skill | Code | Relevant Units |
|---|---|---|
| Information security | INAS | All units |
| Cyber security | SCTY | All operational units |
| Threat intelligence | THIN | CT, TH, OC |
| Incident management | USUP | DF, OC, SC |
| Digital forensics | DGFS | DF |
| Penetration testing | PENT | CE |
| Security architecture | SAAR | SE, SC |
| Governance, risk & compliance | GORC | GR, SC, LD |
| Risk management | BURM | GR, SC, LD |
| Information assurance | INAS | GR, SE |
| Security operations | COPS | TH, DE, OC |
| Vulnerability assessment | VUAS | CE, DE |

---

## 4. ASD Cyber Skills Framework

### About
The Australian Signals Directorate (ASD) Cyber Skills Framework defines the
cybersecurity skills needed in the Australian workforce. It is developed by the
Australian Cyber Security Centre (ACSC) and is the primary Australian government
reference for cybersecurity workforce development.

This framework is **mandatory** — every unit must include at least one ASD CSF mapping.

**Current version:** ASD Cyber Skills Framework 2024 (verify current version at
asd.gov.au/cyber-skills-framework before mapping)

### Reference Format

```markdown
| Framework | Version | Domain | Sub-domain | Proficiency |
|---|---|---|---|---|
| ASD Cyber Skills Framework | 2024 | Defensive Operations | Threat Detection and Response | Practitioner |
```

### ASD CSF Proficiency Levels

| Level | Description | Degree Alignment |
|---|---|---|
| Awareness | Basic understanding of concepts | Foundation Year |
| Foundation | Can apply knowledge under supervision | Foundation + Core |
| Practitioner | Can work independently in the domain | Core + early Major |
| Advanced | Can lead, mentor, or specialise | Major units |
| Expert | Thought leader; sets direction and standards | Capstone/senior Major |

### ASD CSF Domains

| Domain | Relevant Units |
|---|---|
| Governance and Risk Management | GR, LD, SC |
| Education and Training | All (meta) |
| Detection and Monitoring | TH, DE, OC |
| Incident Response | DF, OC |
| Threat Intelligence | CT, TH |
| Vulnerability Management | CE, DE |
| Digital Forensics | DF |
| Security Architecture and Engineering | SE, SC |
| Penetration Testing | CE |
| Protective Security | GR, SE, SC |

---

## 5. Framework Currency Requirements

### Version Monitoring

The Framework Custodian is responsible for monitoring new versions of all mapped frameworks.
The following table lists current versions and review triggers:

| Framework | Current Version | Review Trigger |
|---|---|---|
| NIST NICE DCWF | November 2023 | New NIST SP 800-181 revision or DCWF update |
| SFIA | SFIA 9 (2023) | New SFIA release |
| ASD Cyber Skills Framework | 2024 | ASD releases updated version |
| MITRE ATT&CK | v15 (April 2024) | New ATT&CK version release |
| NIST CSF | CSF 2.0 (2024) | New NIST CSF revision |
| ISO 27001/27002 | 2022 editions | New ISO edition |
| ASD Essential Eight | Current (check asd.gov.au) | ASD updates maturity model |

### Framework Review Process

When a new framework version is released:
1. Framework Custodian opens a GitHub Issue with label `framework-update`
2. Affected units are identified and listed in the issue
3. Framework Custodian or nominated contributor updates mappings within 90 days
4. Updated units have their framework version reference updated in metadata
5. Units not yet updated are labelled `Framework Review Required` in their status

### Backwards Compatibility

When a framework version changes:
- Old work role/skill codes may be deprecated
- The Framework Custodian documents the mapping from old codes to new codes
- Units must be updated to reference current codes within 90 days of framework release

---

## 6. Framework Mapping Validation

Before a unit can reach "Framework Verified" status, the Framework Custodian must
confirm:

- [ ] All NICE DCWF Work Role codes are valid (e.g., PR-CDA-001, not a deprecated code)
- [ ] All NICE DCWF Task codes (T-codes) referenced exist in current DCWF
- [ ] SFIA skill codes are valid SFIA 9 codes (4-letter codes)
- [ ] SFIA responsibility levels are appropriate for the unit's degree layer
- [ ] ASD Cyber Skills Framework domain and sub-domain references are current
- [ ] All framework version numbers are explicitly stated in mapping tables
- [ ] No orphaned mappings (all referenced codes exist in the stated framework version)

---

## 7. Certification Bridge Mapping

Each major must document which industry certifications the major prepares students for.
This is recorded in the major's `README.md` and is for guidance only (this degree
does not certify students for specific exams).

| Major | Certification Bridges |
|---|---|
| Threat Hunting | GIAC GCTH, GIAC GDAT, GCDA |
| DFIR | GIAC GCFE, GCFA, GCFR; Cellebrite CCPA |
| CTI | GIAC GCTI; Recorded Future CTI Certified |
| Detection Engineering | GIAC GCED, GDAT; Splunk Core Certified |
| CTE | OSCP, PNPT, GIAC GPEN; CRTO (Cobalt Strike) |
| Security Engineering | CISSP, SABSA SCF; AWS Security Specialty |
| Leadership & CISO | CISM, CISSP, GIAC GSLC |
| GRC | CISM, CRISC, ISO 27001 Lead Auditor; IRAP Assessor (pathway) |

**Note:** Certification bridges are indicative only. Students should verify current
exam objectives against unit content before sitting exams.
