# Practitioner Review Checklist

This checklist must be completed by the **Domain Expert** and **Practitioner Reviewer**
before a unit can advance from "Under Review" to "Practitioner Approved" status.

Copy this checklist into the Pull Request description and complete it. Both reviewers
must sign off. The Framework Custodian completes the Framework Compliance section
before the unit advances to "Framework Verified".

See `docs/governance.md` for role definitions and the full content lifecycle.

---

## How to Use This Checklist

1. **Contributor** opens a PR for a unit that is ready for review
2. **Contributor** copies this checklist into the PR description and completes
   the self-assessment section
3. **Domain Expert** completes the Technical Accuracy section and signs off
4. **Practitioner Reviewer** completes the Practitioner Relevance section and signs off
5. **Framework Custodian** completes the Framework Compliance section and signs off
6. **Maintainer** reviews all sign-offs and merges if all checks pass

---

## Section 0 — Contributor Self-Assessment

*To be completed by the contributor before requesting review.*

**Unit Code & Title:** [e.g., TH01: Introduction to Hypothesis-Driven Hunting]

**Contributor GitHub handle:** @[handle]

**Brief description of changes in this PR:**

[2–4 sentences describing what was added or changed]

### Content Standards Self-Check (docs/content-standards.md)

- [ ] Unit follows `templates/unit-template.md` exactly — no missing sections
- [ ] Unit Code follows naming convention (correct PREFIX + NN format)
- [ ] Overview explains relevance to the Australian cybersecurity workforce
- [ ] Learning outcomes (5–8) use correct Bloom's verbs for this unit's layer
- [ ] AQF Level 7 Alignment section addresses all 3 descriptors (Knowledge, Skills, Application)
- [ ] Framework mappings table has minimum 2 frameworks, at least 1 Australian
- [ ] Framework versions are explicitly stated in all mappings
- [ ] Minimum 6 topics; each has substantive content (not just headings)
- [ ] Minimum 2 labs; each follows the lab design standard (Objective/Prerequisites/Environment/Instructions/Expected Output/Reflection)
- [ ] Labs use only free/OSS tools (for Foundation and Core units)
- [ ] Minimum 1 formative + 1 summative assessment
- [ ] Summative assessment has a rubric with 4 performance levels
- [ ] Australian context section is present and incorporated into content (not bolted on)
- [ ] Minimum 5 annotated further reading references, including at least 1 Australian source
- [ ] Unit Metadata section is complete
- [ ] All hyperlinks tested and working
- [ ] Markdown renders correctly (checked GitHub preview or equivalent)
- [ ] Content is written in Australian English

---

## Section 1 — Technical Accuracy

*To be completed by the Domain Expert.*

**Domain Expert name:** [Full name]
**Domain Expert GitHub handle:** @[handle]
**Domain / professional background:** [Brief: current role, years experience in this domain]
**Date of review:** [YYYY-MM-DD]

### Technical Content

- [ ] All technical claims are accurate as of the review date
- [ ] Technical terminology is used correctly throughout
- [ ] No outdated techniques, deprecated tools, or superseded standards are presented as current
- [ ] Where content is evolving or contested, this is explicitly acknowledged in the text
- [ ] Tool versions referenced in labs are current and available

### Lab Verification

- [ ] Lab instructions are clear, complete, and step-by-step
- [ ] Lab instructions produce the stated expected output when followed correctly
- [ ] Lab environment setup instructions are accurate and sufficient
- [ ] All tools referenced in labs are confirmed free/OSS (for Foundation and Core units)
- [ ] Lab minimum hardware spec is realistic for the stated environment

### No Vendor Bias

- [ ] No content reads as marketing material for a specific vendor
- [ ] Where vendor tools are mentioned, alternatives are noted or the landscape is contextualised
- [ ] Contributor has disclosed any vendor affiliations relevant to this content (see PR description)

**Domain Expert sign-off:**
> I confirm that the technical content of this unit is accurate, current, and
> appropriate for an AQF Level 7 bachelor-level qualification.
>
> **Signed:** [Name] | **Date:** [YYYY-MM-DD]

---

## Section 2 — Practitioner Relevance

*To be completed by the Practitioner Reviewer.*

**Practitioner Reviewer name:** [Full name]
**Practitioner Reviewer GitHub handle:** @[handle]
**Current role:** [Title, organisation type — e.g., "Senior Threat Analyst, ASX-listed bank"]
**Years in domain:** [N years]
**Date of review:** [YYYY-MM-DD]

### Workforce Relevance

- [ ] Learning outcomes reflect skills actually required in the Australian workforce for this role
- [ ] Content reflects current real-world practice (not just textbook knowledge)
- [ ] The difficulty and depth of content is appropriate for someone entering this specialisation
- [ ] Unit prepares students for the kinds of tasks listed in the DCWF/SFIA mappings

### Australian Context

- [ ] Australian legislation references are accurate and current
- [ ] Regulatory body references (OAIC, ASD, APRA, AFP, etc.) are correct and current
- [ ] Australian case studies or incident examples are accurate and appropriately contextualised
- [ ] ASD Essential Eight or other Australian framework references are current

### Assessment Relevance

- [ ] Summative assessment reflects a task that practitioners actually perform in industry
- [ ] Assessment rubric criteria reflect genuine performance differences recognisable to practitioners
- [ ] Formative assessment provides useful feedback for students developing this skill

### Further Reading

- [ ] Recommended resources are practically useful (not just academic)
- [ ] At least one Australian source is included and is relevant
- [ ] Resources are current; no significantly outdated materials that may mislead students

**Practitioner Reviewer sign-off:**
> I confirm that the content of this unit reflects current industry practice,
> is relevant to the Australian cybersecurity workforce, and that the learning
> outcomes and assessments prepare students for real-world roles.
>
> **Signed:** [Name] | **Date:** [YYYY-MM-DD]

---

## Section 3 — Framework Compliance

*To be completed by the Framework Custodian.*

**Framework Custodian name:** [Full name]
**Framework Custodian GitHub handle:** @[handle]
**Date of review:** [YYYY-MM-DD]

### NIST NICE / DCWF

- [ ] All DCWF Work Role codes are valid (checked against current DCWF: November 2023 or later)
- [ ] Work Role codes are in the correct format (e.g., PR-CDA-001)
- [ ] Task codes (T-codes), if referenced, exist in the current DCWF
- [ ] Work Role categories are appropriate for this unit type (Operational → PR/IN/OM; Strategic → OV/SP)
- [ ] Framework version is explicitly stated in the mapping table

### SFIA 9

- [ ] All SFIA skill codes are valid 4-letter codes from SFIA 9
- [ ] SFIA responsibility levels (1–7) are appropriate for this unit's degree layer
  (Foundation: 1–2; Core: 2–3; Major: 3–5)
- [ ] Framework version is explicitly stated in the mapping table

### ASD Cyber Skills Framework

- [ ] At least 1 ASD CSF mapping is present (mandatory for all units)
- [ ] Domain and sub-domain references match the current ASD CSF
- [ ] Proficiency levels are appropriate for this unit's degree layer
- [ ] Framework version is explicitly stated in the mapping table

### Bloom's Taxonomy Alignment

- [ ] Learning outcome verbs are at the correct Bloom's level for this unit's layer:
  - Foundation: Levels 1–3 ✓ / ✗
  - Core: Levels 3–4 ✓ / ✗
  - Major: Levels 4–5 ✓ / ✗
  - Capstone: Levels 5–6 ✓ / ✗
- [ ] No learning outcome uses a verb below the required level for this layer

### AQF Compliance

- [ ] AQF Level 7 Alignment section addresses all 3 descriptors (Knowledge, Skills, Application)
- [ ] Learning outcomes are consistent with AQF Level 7 graduate capabilities
- [ ] Content volume is proportionate to 8 credit points (see docs/compliance/aqf-teqsa.md §1.4)
  - Minimum 6 substantive topics ✓ / ✗
  - Minimum 2 practical labs ✓ / ✗
  - Minimum 1 formative + 1 summative assessment ✓ / ✗

**Framework Custodian sign-off:**
> I confirm that all framework mappings in this unit are accurate, current, and
> appropriately referenced, and that the unit meets AQF Level 7 compliance requirements.
>
> **Signed:** [Name] | **Date:** [YYYY-MM-DD]

---

## Section 4 — Maintainer Final Check

*To be completed by the Maintainer before merging.*

**Maintainer GitHub handle:** @[handle]
**Date of review:** [YYYY-MM-DD]

- [ ] Section 0 (Contributor Self-Assessment) — completed
- [ ] Section 1 (Technical Accuracy) — Domain Expert sign-off received
- [ ] Section 2 (Practitioner Relevance) — Practitioner Reviewer sign-off received
- [ ] Section 3 (Framework Compliance) — Framework Custodian sign-off received
- [ ] Unit status updated to `Practitioner Approved` or `Framework Verified` as appropriate
- [ ] No open review comments remain unresolved
- [ ] PR does not introduce any licensing, vendor, or attribution issues
- [ ] All CI checks pass (if applicable)

**Maintainer sign-off:**
> All required reviews have been completed. This unit meets the content standards,
> compliance requirements, and quality bar for publication.
>
> **Merging as:** [Practitioner Approved / Framework Verified / Published]
>
> **Signed:** @[handle] | **Date:** [YYYY-MM-DD]
