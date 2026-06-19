# TODO — docs/quality/

This directory contains documents governing the ongoing quality assurance of the degree program.

**Files in this directory:**
- `annual-review-schedule.md` — When and how each unit is reviewed each year
- `equity-and-inclusion.md` — Equity, diversity, and inclusion commitments and practices

---

## annual-review-schedule.md

### Purpose

Defines the systematic review cycle that keeps unit content current, accurate, and framework-aligned.

### Actions

- [ ] **Define the annual review calendar** — set specific months for each review type:
  - Framework version check (Q1 — after NIST/ASD/MITRE annual releases)
  - Australian legislation and regulatory check (Q2)
  - Tool version and availability check (Q3)
  - Full unit content review (Q4)
- [ ] **Define what triggers an off-cycle emergency review:**
  - Major NIST publication (new SP 800 series, CSF revision)
  - ASD Essential Eight maturity model update
  - Privacy Act amendment or new OAIC guidance
  - New APRA prudential standard
  - ATT&CK major version release (v15+)
  - Critical tool deprecation (e.g., a lab tool is no longer maintained or free)
- [ ] **Define the review process for each trigger:**
  - Who is responsible (unit Domain Expert, Framework Custodian, or designated reviewer)
  - What changes require a version increment vs. minor correction
  - How learners currently studying a unit are notified of changes
- [ ] **Create a unit review log template** — a simple table in each unit's metadata tracking when it was last reviewed and by whom
- [ ] **Define the "sunset" policy** — what happens to a unit that cannot find a Domain Expert for review (it should be unpublished until reviewed, not left outdated)
- [ ] **Create a framework change watchlist** — a monitored list of RSS feeds, mailing lists, or websites to monitor for relevant changes:
  - NIST CSRC (csrc.nist.gov) — CSF, SP 800 series
  - ASD/ACSC (cyber.gov.au) — Essential Eight, ISM, advisories
  - MITRE (attack.mitre.org, ctid.mitre-engenuity.org) — ATT&CK, CTID
  - APRA (apra.gov.au) — CPS 234, CPG 234
  - OAIC (oaic.gov.au) — NDB, Privacy Act guidance
  - Sigma (github.com/SigmaHQ/sigma) — rule format changes
  - SFIA (sfia-online.org) — framework updates

---

## equity-and-inclusion.md

### Purpose

Documents the commitments and practices that ensure the degree is genuinely accessible and inclusive.

### Actions

- [ ] **Accessibility:**
  - [ ] Define WCAG 2.1 AA as the minimum accessibility standard for all content
  - [ ] Require alt text for all images and diagrams in unit files
  - [ ] Ensure Mermaid diagrams have text alternatives (since not all screen readers parse them)
  - [ ] Require that all videos (if added) have closed captions
  - [ ] Define the minimum hardware spec as the accessibility floor — content must be usable on 8 GB RAM / 4-core / 50 GB disk, with no requirement for paid subscriptions

- [ ] **Language accessibility:**
  - [ ] Define plain English as the standard — avoid jargon without explanation
  - [ ] Define a reading level target for Foundation Year units (write for someone who has not studied computing before)
  - [ ] Add a glossary document to the `docs/` directory for technical terms used across the degree

- [ ] **Representation:**
  - [ ] Review case studies and examples for diversity — scenarios should not default to generic US/Western contexts
  - [ ] Ensure Australian case studies include examples from diverse sectors and regions
  - [ ] Consider diverse learner personas in lab design (different OS preferences, different prior experience levels)

- [ ] **Economic accessibility:**
  - [ ] Enforce the no-commercial-tools requirement in Foundation and Core labs
  - [ ] Major labs should document free alternatives wherever commercial tools are cited
  - [ ] Ensure labs work on consumer hardware — no requirement for cloud credits or enterprise licences
  - [ ] Add a "no-cost learning path" callout in the student handbook showing all free resources

- [ ] **Inclusion in governance:**
  - [ ] Set a target for IAB diversity (gender, sector, geography across Australia)
  - [ ] Define a pathway for practitioners from underrepresented groups to contribute content
  - [ ] Add a code of conduct to the repository (`CODE_OF_CONDUCT.md`) covering contributor and community interactions
  - [ ] Define how the project responds to complaints about exclusionary content or contributor behaviour

- [ ] **Create `CODE_OF_CONDUCT.md` in the repository root** — reference the Contributor Covenant as a starting point
