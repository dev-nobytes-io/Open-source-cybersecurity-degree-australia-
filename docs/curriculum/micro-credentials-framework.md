# Micro-Credentials Framework

This document defines how individual units and skill clusters within the degree
map to micro-credentials and digital badges. It enables learners to gain partial
recognition without completing the full degree.

---

## 1. Purpose

Not every learner will complete the full 168 CP degree. Some want to upskill in
a specific area. Some want formal evidence of a subset of skills. Some employers
want to develop staff in targeted competencies, not through a full degree.

The micro-credentials framework provides a modular recognition layer that:
- Recognises completion of individual units or clusters
- Maps directly to NICE DCWF work roles and SFIA skill levels
- Is portable — learners can present micro-credentials to employers independently
- Feeds into the full degree for those who continue

---

## 2. Micro-Credential Tiers

### Tier 1 — Unit Badge

Awarded on completion of a single unit. Minimum requirements:
- All labs completed and documented
- Formative assessment completed
- Summative assessment completed with majority Proficient or above

**Badge name format:** `[Unit Code] — [Unit Title]`
**Example:** `F06 — Data & Log Analysis`

### Tier 2 — Layer Certificate

Awarded on completion of all units in a degree layer:
- Foundation Year Certificate (F01–F06)
- Operational Core Certificate (OC01–OC06)
- Strategic Core Certificate (SC01–SC06)
- [Major] Specialist Certificate (e.g., Threat Hunting Specialist Certificate — TH01–TH06)

### Tier 3 — Pathway Certificate

Awarded on completion of Foundation + Core + Major (no capstone):
- Bachelor of Cybersecurity Operations (Pre-Capstone) Certificate
- Bachelor of Cybersecurity Strategy (Pre-Capstone) Certificate

### Tier 4 — Degree Completion

Full degree completion (Foundation + Core + Major + Capstone).

---

## 3. NICE DCWF Work Role Badges

Separate from the layer/unit badge structure, Work Role Badges are awarded when
a student has demonstrated all mapped T-codes for a specific NICE DCWF work role.

Work Role Badges are the most employer-relevant micro-credential — they speak
directly in the language of job descriptions and workforce frameworks.

| Badge | Work Role Code | Demonstration Requirements |
|---|---|---|
| Cyber Defense Analyst Badge | PR-CDA-001 | All T-codes for PR-CDA-001 demonstrated across units |
| Cyber Defense Incident Responder Badge | PR-CIR-001 | All T-codes for PR-CIR-001 demonstrated |
| Digital Forensics Analyst Badge | IN-FOR-001 | All T-codes for IN-FOR-001 demonstrated |
| Threat/Warning Analyst Badge | AN-TWA-001 | All T-codes for AN-TWA-001 demonstrated |
| Security Architect Badge | SP-ARC-001 | All T-codes for SP-ARC-001 demonstrated |
| IS Security Manager Badge | OV-MGT-001 | All T-codes for OV-MGT-001 demonstrated |

---

## 4. SFIA Skill Level Badges

SFIA Skill Badges are awarded when a student demonstrates a specific SFIA skill
at a specific responsibility level, evidenced by unit assessments.

| Badge | SFIA Code | Level | Demonstrating Units |
|---|---|---|---|
| Information Security Level 2 | INAS | 2 | F04, F05 |
| Information Security Level 3 | INAS | 3 | OC02, SC03 |
| Cyber Security Level 3 | SCTY | 3 | OC01–OC04 |
| Cyber Security Level 4 | SCTY | 4 | Major units (operational) |
| Threat Intelligence Level 3 | THIN | 3 | OC05, CT01–CT03 |
| Threat Intelligence Level 4 | THIN | 4 | CT04–CT06 |
| Incident Management Level 3 | USUP | 3 | OC04, DF01–DF02 |
| Risk Management Level 3 | BURM | 3 | SC01, GR01 |
| Governance Risk Compliance Level 3 | GORC | 3 | SC03, GR01–GR03 |

---

## 5. Digital Badge Implementation

### Current Status

Digital badges are not yet technically implemented. This framework defines the
standard; implementation is planned as a future milestone.

### Planned Implementation

Digital badges will be implemented using the **Open Badges 3.0** standard
(IMS Global / 1EdTech), which supports:
- Verifiable credentials (cryptographically signed)
- Portability to LinkedIn, Credly, and other platforms
- Embedded evidence links (students can attach portfolio evidence)

**Issue mechanism:**
For self-directed learners: self-issued badges with evidence attestation
(the student signs their own badge and attaches their evidence)

For facilitated delivery partners: partner-issued badges using the delivery
partner's issuing credentials

**Verification:**
Badges link to the student's public portfolio evidence (GitHub repository).
Employers can verify the evidence directly — the badge is a pointer to the
evidence, not a standalone credential.

### Interim Approach (Until Implementation)

Until digital badges are implemented, students should:
1. Record all completed units and work roles in their competency profile
2. Document evidence in their portfolio (GitHub repository)
3. Reference the competency profile on LinkedIn under "Licences & Certifications"
   with this repository as the issuing organisation URL

---

## 6. Employer Recognition

Micro-credentials from this degree carry weight when:
- The employer understands NICE DCWF work roles (common in government, defence, financial services)
- The student can demonstrate the evidence behind the badge
- The badge links to a portfolio showing actual lab work and assessments

The badge itself is a signpost. The portfolio is the evidence. Employers who ask
"can you show me what you did?" are asking the right question — and a student with
a strong portfolio can answer it.
