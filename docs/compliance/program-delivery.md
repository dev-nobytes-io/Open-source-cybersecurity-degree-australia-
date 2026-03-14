# Program Delivery Standards

This document defines the standards for how the Open-Source Cybersecurity Degree
is delivered. It covers accessibility, open licensing compliance, quality assurance
cycles, and version control practices.

These standards apply to all content in the repository and must be considered by
all contributors and maintainers.

---

## 1. Accessibility Standards

All content published in this repository must be accessible to the widest possible
audience. This includes people with disabilities, people on slow connections, and
people using non-standard devices.

### WCAG 2.1 AA Compliance

All content must comply with the Web Content Accessibility Guidelines (WCAG) 2.1
at the AA conformance level.

**For markdown files:**
- Use proper heading hierarchy (`#` → `##` → `###`); do not skip heading levels
- Do not use heading formatting for emphasis — use `**bold**` or `*italic*` instead
- All images must have descriptive alt text (in markdown: `![Descriptive alt text](image.png)`)
- Do not use colour as the only means of conveying information (e.g., red = bad,
  green = good must also be conveyed by text or symbol)
- Tables must have column headers
- Abbreviations must be spelled out on first use in each document

**For embedded images and diagrams:**
- Screenshots must include a text description of what the screenshot shows
- Network diagrams and architecture diagrams must be accompanied by a textual description
  sufficient to convey the same information
- Do not embed text within images

**For lab instructions:**
- Provide clear step-by-step instructions that do not require simultaneous visual and
  technical attention (i.e., instructions must be readable alongside the task)
- Where colour is used in terminal output, also describe what the colour means in text

### Hardware Accessibility

Labs must be completable on widely accessible consumer hardware:
- **Minimum spec:** 8 GB RAM, quad-core CPU (Intel Core i5/Ryzen 5 equivalent or better),
  50 GB free disk space
- If a lab requires more resources, this must be stated clearly in the lab prerequisites
- Where possible, provide a lightweight alternative configuration for resource-constrained environments
- Virtual machine images must be downloadable for free
- Cloud-based labs must document a free-tier configuration

### Language Accessibility
- Write in plain English (CEFR B2 level or above)
- Avoid unnecessary jargon; where technical terms are necessary, define them on first use
- Do not use idioms or cultural references that assume Australian cultural familiarity
  (the degree has an international audience despite its Australian focus)
- Australian English spelling is used (e.g., "organisation", "colour", "analyse")

---

## 2. Open Licensing Compliance

### Licence
All content in this repository is published under the
**Creative Commons Attribution 4.0 International (CC BY 4.0)** licence.

This means:
- Anyone may copy, redistribute, adapt, or build upon this content for any purpose
- Attribution must be given to the original contributors and this project
- No additional restrictions may be placed on the content by downstream users

### What This Means for Contributors

**You may include:**
- Original content you have authored
- Content from other CC BY 4.0 or CC0 licensed sources (with attribution)
- MITRE ATT&CK content (licensed CC BY 4.0)
- NIST publications (US Government public domain — compatible with CC BY 4.0)
- ASD/ACSC publications — check current reuse terms at `asd.gov.au`; Crown Copyright
  applies; check if the specific publication permits reproduction

**You may not include:**
- Verbatim reproduction of copyrighted content without a compatible open licence
- Content from paywalled sources reproduced without permission
- Content from textbooks or journals under All Rights Reserved
- Vendor documentation under proprietary licences

**Attribution format:**

When quoting or adapting third-party CC BY 4.0 content:
> Adapted from [Title] by [Author/Organisation], licensed under CC BY 4.0.
> Original available at [URL].

### Tool Licensing
- Tools referenced in Foundation and Core labs must be free/open-source software (FOSS)
- FOSS licence compatibility with CC BY 4.0 is not required (different licence type),
  but tools must be freely downloadable without registration or purchase
- Tools in Major labs may be commercial provided a free alternative is documented

---

## 3. Quality Assurance Cycle

### Annual Review Cycle

Every unit with "Published" status undergoes an annual review:

| Activity | Timing | Owner |
|---|---|---|
| Annual review trigger | End of each calendar year | Maintainer |
| Unit currency assessment | Domain Expert confirms content is still current | Domain Expert |
| Framework mapping review | Framework Custodian confirms mappings are current | Framework Custodian |
| Australian context review | Confirm Australian legislation/regulatory references are current | Practitioner Reviewer |
| Lab tool verification | Confirm all lab tools are still available, free, and work as described | Contributor |
| Review outcome | Unit re-confirmed as current, OR moved to "Framework Review Required" / "Under Review" | Maintainer |

### Trigger-Based Review

A unit is moved to "Under Review" or "Framework Review Required" when any of the
following events occur:

| Trigger | Required Action |
|---|---|
| New framework version released (NICE, SFIA, ASD CSF, ATT&CK, etc.) | Framework Custodian reviews affected units within 90 days |
| Significant change to Australian legislation (Privacy Act, SOCI Act, etc.) | Domain Expert reviews affected units within 60 days |
| Major threat landscape shift (new TTP category in ATT&CK, significant Australian incident) | Domain Expert determines if content update is required within 30 days |
| Lab tool is discontinued, paywalled, or significantly changed | Contributor or Maintainer updates lab instructions within 30 days |
| ASD Essential Eight maturity model updated | Framework Custodian and Domain Expert review GR, SC, and F05 units within 60 days |

### Community-Initiated Review

Any community member may raise a "Currency Review" issue at any time by creating
a GitHub Issue with the label `content-review` and describing:
- Which unit is affected
- What has changed (the trigger for the review)
- Suggested correction (if known)

Maintainers respond to `content-review` issues within 14 days to confirm whether
a review is warranted and assign ownership.

---

## 4. Version Control Standards

### Branch Strategy
- `master` — contains only published, reviewed content
- `develop` — (optional) staging branch for content under development
- Feature branches — `[contributor]/[unit-code]-[description]` (e.g., `jsmith/th01-initial-content`)
- Hotfix branches — `hotfix/[unit-code]-[description]` (e.g., `hotfix/f05-privacy-act-update`)

### Commit Message Standards
Commit messages must be descriptive and follow this format:

```
[unit-code] Short description of change (50 chars max)

Longer description if needed (72 chars per line max).
Explain WHY the change was made, not just what changed.

Fixes #123 (if closing an issue)
```

**Examples:**
- `[F05] Update Privacy Act reference to 2024 amendments`
- `[TH02] Add TAXII 2.1 lab exercise`
- `[governance] Add Framework Custodian role definition`

### File Versioning
Unit files include a `Version` field in their metadata section. Version numbers follow
semantic versioning (`vMAJOR.MINOR`):

| Change Type | Version Bump | Example |
|---|---|---|
| Minor update (clarification, typo, additional example) | MINOR +1 | v1.0 → v1.1 |
| Framework mapping update | MINOR +1 | v1.2 → v1.3 |
| Content addition (new topic, new lab) | MINOR +1 | v1.3 → v1.4 |
| Learning outcome change | MAJOR +1 | v1.4 → v2.0 |
| Assessment redesign | MAJOR +1 | v2.0 → v3.0 |
| Substantial content rewrite | MAJOR +1 | v1.x → v2.0 |

### Curriculum Versioning
The overall degree curriculum is versioned as `YEAR.SEMESTER`:
- `2026.1` — first semester 2026
- `2026.2` — second semester 2026
- A new curriculum version is tagged in git when a cohort of units is published together

### Archival Policy
When a unit is retired:
1. The unit's status is updated to `Archived` in its metadata
2. A deprecation notice is added at the top of the unit file explaining why it was retired
3. The unit directory is moved to `archive/[major]/[unit-code]/`
4. A CHANGELOG.md entry records the retirement
5. The degree structure document (`docs/structure.md`) is updated

Archived content remains accessible in the repository — it is not deleted.

---

## 5. Content Integrity

### No Plagiarism (Rule R6 from CONTRIBUTING.md)
- All original content must be authored by the contributor
- Third-party content must be attributed (see Section 2 of this document)
- Paraphrasing copyrighted content without attribution is not acceptable

### Accuracy Before Speed (Rule R5 from CONTRIBUTING.md)
- Do not publish content you are not confident is accurate
- If a topic is evolving or contested, state this explicitly in the content
- Prefer "this is the current industry consensus as of [year]" over stating contested
  positions as fact

### No Vendor Promotion
- Content must not read as marketing material for any vendor or product
- Where vendor tools are mentioned, they must be contextualised within a broader
  landscape of alternatives
- Contributors must disclose vendor relationships in their PR description if their
  content references tools from vendors they are affiliated with

---

## 6. Delivery Environment Standards

### Markdown Rendering
All content is written in GitHub Flavored Markdown (GFM). Content must render
correctly in standard GitHub markdown rendering. Contributors should preview their
markdown before submitting a PR.

### Link Integrity
- All hyperlinks must be tested before submission
- Links to Australian government websites (asd.gov.au, oaic.gov.au, etc.) should
  use stable URL patterns where possible
- Where a resource may move, use the organisation's homepage + navigation path
  rather than a deep link
- Dead links in published content should be reported via GitHub Issues with label `dead-link`

### Image and File Size
- Images should be compressed; maximum file size 500 KB per image
- Prefer SVG for diagrams where possible (scalable and accessible)
- Do not commit binary files (.exe, .zip, VM images) to the repository;
  link to external download sources instead
- Total repository size should be managed; large binary assets should be hosted
  externally (e.g., lab VM images on a CDN or cloud storage)
