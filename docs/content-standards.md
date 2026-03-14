# Content Standards

This document defines the mandatory content standards for every unit in the
Open-Source Cybersecurity Degree. All contributors must follow these standards.
Pull requests that do not meet these standards will not be approved.

For the official unit template, see `templates/unit-template.md`.
For the practitioner review checklist, see `templates/review-checklist.md`.

---

## 1. Mandatory Unit Fields

Every unit file must contain all of the following fields. No exceptions.

| Field | Minimum Requirement |
|---|---|
| **Unit Code + Title** | Must follow the naming convention (see Section 2) |
| **Overview** | 1–2 paragraphs; must explain the relevance of this unit to the Australian cybersecurity workforce |
| **Learning Outcomes** | 5–8 outcomes; must use correct Bloom's taxonomy verbs for the unit's layer (see Section 3) |
| **AQF Level 7 Alignment** | Explicit statement mapping the unit to AQF Level 7 descriptors (see `docs/compliance/aqf-teqsa.md`) |
| **Framework Mappings** | Table with columns: Framework, Element, Reference Code; minimum 2 frameworks, at least 1 Australian |
| **Topics** | Minimum 6 topics; each topic must contain substantive content — not just a heading |
| **Labs & Exercises** | Minimum 2 practical labs; each lab must follow the lab design standard (see Section 5) |
| **Assessment** | At least 1 formative + 1 summative assessment; rubric criteria must be stated (see Section 6) |
| **Australian Context** | At least 1 Australian legislation, regulatory body, case study, or threat actor profile per unit |
| **Further Reading** | Minimum 5 annotated references; at least 1 must be an Australian source |
| **Unit Metadata** | Version, Status, Domain Expert, Practitioner Reviewer, Last Reviewed, Framework versions (see template) |

---

## 2. Unit Naming Convention

### Unit Codes

Unit codes follow the format `[PREFIX][NN]` where:
- `PREFIX` is the layer/major identifier (see table below)
- `NN` is a zero-padded two-digit number (01, 02, 03...)

| Prefix | Layer / Major |
|---|---|
| `F` | Foundation Year |
| `OC` | Operational Core |
| `SC` | Strategic Core |
| `TH` | Threat Hunting |
| `DF` | Digital Forensics & Incident Response (DFIR) |
| `CT` | Cyber Threat Intelligence (CTI) |
| `DE` | Detection Engineering |
| `CE` | Cyber Threat Emulation (CTE) |
| `SE` | Security Engineering |
| `LD` | Leadership & CISO |
| `GR` | Governance, Risk & Compliance (GRC) |
| `CAP` | Capstone |

**Examples:** `F01`, `OC03`, `TH06`, `GR02`, `CAP01`

### File and Directory Naming
- All lowercase with hyphens (no spaces, no underscores)
- Unit directory: `[major-slug]/[unit-code]-[unit-title-slug]/`
- Main unit file: `README.md` within the unit directory
- **Example:** `degrees/operational/threat-hunting/th01-hypothesis-driven-hunting/README.md`

---

## 3. Bloom's Taxonomy Requirements

Learning outcomes must use Bloom's taxonomy verbs at the correct cognitive level
for the unit's layer. Using verbs from a lower level than required is not acceptable
(e.g., writing "identify" in a Major unit when "evaluate" is required).

### Cognitive Level Requirements by Layer

| Layer | Bloom's Levels | Example Verbs |
|---|---|---|
| **Foundation Year** (F01–F06) | 1–3: Remember, Understand, Apply | Define, explain, describe, identify, demonstrate, use, implement, perform |
| **Operational/Strategic Core** (OC01–OC06, SC01–SC06) | 3–4: Apply, Analyse | Apply, execute, implement, analyse, compare, differentiate, examine, break down |
| **Major Units** (TH/DF/CT/DE/CE/SE/LD/GR) | 4–5: Analyse, Evaluate | Analyse, evaluate, assess, critique, justify, prioritise, appraise, recommend |
| **Capstone** (CAP01) | 5–6: Evaluate, Create | Evaluate, create, design, develop, produce, construct, synthesise, formulate |

### Bloom's Taxonomy Verb Reference

| Level | Verbs (not exhaustive) |
|---|---|
| 1 — Remember | define, list, recall, recognise, identify, name, state, describe |
| 2 — Understand | explain, summarise, classify, interpret, paraphrase, discuss, illustrate |
| 3 — Apply | apply, use, demonstrate, execute, implement, solve, perform, operate |
| 4 — Analyse | analyse, compare, differentiate, examine, break down, categorise, distinguish |
| 5 — Evaluate | evaluate, assess, critique, justify, prioritise, appraise, recommend, argue |
| 6 — Create | create, design, develop, produce, construct, synthesise, formulate, plan |

### Learning Outcome Format
Each learning outcome must be a complete sentence beginning with "Students will be
able to [Bloom's verb]..."

**Example (Major unit — level 5):**
> Students will be able to evaluate threat intelligence reports for analytical confidence,
> source reliability, and operational relevance in an Australian enterprise context.

---

## 4. Framework Mapping Requirements

Every unit must include a framework mapping table. Requirements:
- Minimum 2 frameworks mapped
- At least 1 framework must be Australian (ASD Cyber Skills Framework is preferred)
- Framework version must be specified
- References must be specific — not just "NIST CSF" but the specific function/category/subcategory

### Mapping Table Format

```markdown
| Framework | Version | Element | Reference Code |
|---|---|---|---|
| NIST NICE DCWF | 2023 | Work Role: Cyber Defense Analyst | PR-CDA-001 |
| SFIA 9 | 2023 | Information security | INAS — Level 3 |
| ASD Cyber Skills Framework | 2024 | Defensive Operations | Threat Detection |
```

### Minimum Framework Coverage by Unit Type

| Unit Type | Required Frameworks |
|---|---|
| All Foundation units | NICE DCWF (any) + ASD Cyber Skills Framework |
| Operational Core/Major | NICE DCWF (Protect & Defend, Investigate, or O&M) + ASD + SFIA 9 |
| Strategic Core/Major | NICE DCWF (Oversee & Govern or Securely Provision) + ASD + SFIA 9 |

For detailed framework mapping compliance requirements, see
`docs/compliance/workforce-frameworks.md`.

---

## 5. Lab Design Standards

Every lab must contain all of the following sections:

```
### Lab [N]: [Lab Title]

**Objective:** What the student will achieve by completing this lab.

**Prerequisites:** What knowledge or completed units are assumed. List specific units (e.g., F01, F03) or tools.

**Environment:** What the student needs to set up. Specify minimum hardware/software requirements. Must use free/OSS tools for Foundation and Core units.

**Instructions:**
Step-by-step numbered instructions. Each step must be actionable (not vague). Expected output or result should be noted where helpful.

**Expected Output:** What a correct completion looks like. May include screenshots, expected terminal output, or file hashes.

**Reflection Questions:** 2–4 questions prompting the student to connect the lab to real-world scenarios, Australian context, or theoretical concepts from the unit.
```

### Tool Requirements

| Unit Layer | Tool Requirement |
|---|---|
| Foundation (F01–F06) | Free/open-source only. No paid tools. |
| Core (OC/SC) | Free/open-source only. No paid tools. |
| Major units | Free/OSS preferred. If a paid tool is referenced, a free alternative must be documented alongside it. |

### Lab Environment Minimum Specification
- Labs must be completable on a machine with: 8 GB RAM, 4-core CPU, 50 GB free disk
- Virtual machine images used in labs must be freely downloadable
- Cloud-based labs must have a free-tier alternative documented

---

## 6. Assessment Design Standards

### Formative Assessment
- Purpose: Low-stakes check on learning progress; feedback-focused
- Examples: quizzes, reflection journals, short answer questions, peer review exercises
- Must be mapped to at least 1 specific Learning Outcome

### Summative Assessment
- Purpose: Evaluation of achieved learning outcomes at end of unit
- Must be mapped to all major Learning Outcomes (minimum 4)
- Must include a rubric with 4 performance levels (see below)
- At least one summative assessment per unit must involve a practical, real-world task

### Rubric Performance Levels

All rubrics must define 4 performance levels:

| Level | Description |
|---|---|
| **Exemplary** | Exceeds expectations; demonstrates deep understanding and sophisticated application |
| **Proficient** | Meets expectations; demonstrates solid understanding and competent application |
| **Developing** | Partially meets expectations; demonstrates basic understanding with gaps |
| **Beginning** | Does not yet meet expectations; demonstrates limited or inaccurate understanding |

### Assessment-Learning Outcome Mapping
Each assessment task must include an explicit mapping table:

```
| Assessment Task | Learning Outcomes Addressed |
|---|---|
| Lab report — Wireshark packet capture | LO1, LO3, LO5 |
| Reflection: Australian privacy obligations | LO2, LO4 |
```

---

## 7. Australian Context Requirements

Every unit must include at least one of the following:
- Reference to an Australian law or regulation relevant to the unit's content
- Reference to an Australian regulatory body (ASD, OAIC, APRA, ACSC, AFP, etc.)
- An Australian threat actor profile, incident case study, or breach example
- A mapped requirement from an Australian framework (ASD Essential Eight, IRAP, TIBER-AU, etc.)

This requirement applies to **every unit** — including Foundation and non-GRC majors.
The Australian context must be woven into the content, not bolted on as a footnote.

---

## 8. Further Reading Standards

| Requirement | Detail |
|---|---|
| Minimum references | 5 per unit |
| Australian sources | At least 1 must be an Australian source (government, AISA, ASD, Australian academic) |
| Annotation | Every reference must have a 1–2 sentence annotation explaining its relevance |
| Currency | References should generally be within 5 years unless they are foundational/seminal works |
| Licence/access | Where possible, link to freely accessible resources; if paywalled, note this |

### Reference Format

```
**Author/Organisation (Year).** *Title.* Publisher/URL.
> Relevance: [1–2 sentences explaining why this is useful for students of this unit.]
```

---

## 9. Content Quality Standards

### Accuracy (Rule R5 from CONTRIBUTING.md)
- Do not include content you are not confident is accurate
- Technical claims must be verifiable against a primary source
- If content is contested or evolving, acknowledge this explicitly in the text

### Attribution (Rule R6 from CONTRIBUTING.md)
- Properly attribute all third-party content
- Do not reproduce copyrighted material without checking licence compatibility with CC BY 4.0
- MITRE ATT&CK content is CC BY 4.0 compatible and may be quoted with attribution
- ASD/ACSC publications are Crown Copyright — check current reuse terms before reproducing

### No Vendor Lock-In (Rule R3 from CONTRIBUTING.md)
- Core units must not require or assume access to any commercial product
- Do not mention specific commercial vendors in core unit content as if they are the
  only option (e.g., "use Splunk to..." should be "use a SIEM such as [OpenSearch/Splunk]...")
- In major units, vendor tools may be referenced but free alternatives must be noted

---

## 10. Unit Status Labels

Units must display one of the following status labels in their metadata:

| Status | Meaning |
|---|---|
| `Draft` | Being authored; not ready for review |
| `Under Review` | PR open; awaiting sign-off |
| `Practitioner Approved` | Domain Expert + Practitioner Reviewer have signed off |
| `Framework Verified` | Framework Custodian has confirmed all mappings are accurate |
| `Published` | Merged to master; publicly available |
| `Framework Review Required` | Framework mapping is outdated; needs updating |
| `Archived` | Retired; no longer current |

See `docs/governance.md` for the full content lifecycle and transition requirements.
