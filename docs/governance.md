# Governance Model

This document defines the formal governance model for the Open-Source Cybersecurity
Degree. It establishes roles, decision-making processes, the content lifecycle, and
versioning policy. All contributors and maintainers must operate within this framework.

---

## 1. Governance Roles

### Maintainer
- Overall stewards of the repository
- Sole authority to merge pull requests into `master`
- Approve structural changes (new units, unit retirement, prerequisite changes)
- Responsible for enforcing governance rules and content standards
- Must have a demonstrated background in cybersecurity education or workforce development

### Domain Expert
- Unit-level subject matter authority for a specific major or discipline
- Must have **active professional experience** in the domain (currently practicing or
  within 2 years of active practice)
- Signs off on technical accuracy before a unit can reach "Practitioner Approved" status
- Assigned per unit or per major; a single Domain Expert may cover an entire major
- Listed in unit metadata

### Practitioner Reviewer
- Reviews content for real-world applicability and workforce relevance
- Distinct from Domain Expert (may be the same person for small majors or niche areas)
- Must confirm that learning outcomes reflect actual tasks performed in industry
- Signs off on the Practitioner Relevance section of the review checklist

### Framework Custodian
- Owns the accuracy of framework mappings across the entire degree
- Monitors framework version updates (NICE DCWF, SFIA, ASD Cyber Skills Framework,
  MITRE ATT&CK, ISO 27001, NIST CSF, etc.)
- Initiates review processes when a new framework version is released
- Updates `docs/frameworks.md` to reflect current framework versions

### Community Contributor
- Anyone who submits a pull request or raises an issue
- No merge authority
- Subject to the same content standards and code of conduct as all roles
- Contributions reviewed against `docs/content-standards.md` and `templates/unit-template.md`

---

## 2. Content Lifecycle

Every unit moves through the following mandatory states. Transitions require the
specified approvals — no unit may skip a state.

```
Draft → Under Review → Practitioner Approved → Framework Verified → Published → Archived
```

### State Definitions

| State | Description | Who Sets It |
|---|---|---|
| **Draft** | Content is being authored; not ready for review | Contributor |
| **Under Review** | PR open; awaiting Domain Expert + Practitioner Reviewer sign-off | Contributor (via PR) |
| **Practitioner Approved** | Domain Expert + Practitioner Reviewer have signed off | Maintainer (after review) |
| **Framework Verified** | Framework Custodian has confirmed all mappings are accurate and current | Framework Custodian |
| **Published** | Content is merged to master and publicly available | Maintainer |
| **Archived** | Content is retired; superseded or no longer current | Maintainer |

### Transition Requirements

| Transition | Required Approvals |
|---|---|
| Draft → Under Review | Contributor opens PR; self-checks against `templates/review-checklist.md` |
| Under Review → Practitioner Approved | Domain Expert signs off (technical accuracy) + Practitioner Reviewer signs off (workforce relevance) |
| Practitioner Approved → Framework Verified | Framework Custodian confirms all framework mappings are accurate and version-referenced |
| Framework Verified → Published | Maintainer merges PR |
| Published → Archived | Maintainer decision; deprecation notice added; content moved to `archive/` |

---

## 3. Decision-Making Process

### Typo and Formatting Fixes
- **Who decides:** Any Maintainer
- **Process:** Direct merge; no review required
- **Examples:** Spelling corrections, broken links, formatting inconsistencies

### New Content (Unit Authoring)
- **Who decides:** Domain Expert + Practitioner Reviewer (technical sign-off) + Maintainer (merge)
- **Process:** Full content lifecycle (Draft → Published)
- **Examples:** New topic content, new lab exercises, new assessment tasks

### Structural Changes
- **Who decides:** Maintainer consensus (all active Maintainers must agree)
- **Process:** Issue raised, discussed openly for a minimum of 7 days before action
- **Examples:** Adding or retiring a unit, changing prerequisites, restructuring a major,
  changing the credit point value of a unit

### Framework Mapping Updates
- **Who decides:** Framework Custodian (with Maintainer approval to merge)
- **Process:** Framework Custodian initiates review within 90 days of a new framework
  version release; affected units flagged; updated mappings submitted as PRs
- **Examples:** NICE DCWF version update, new SFIA release, ASD Cyber Skills Framework revision

### Governance Rule Changes (this document + CONTRIBUTING.md)
- **Who decides:** Maintainer consensus after community input
- **Process:** Proposed change published as a GitHub Issue with label `governance`;
  14-day public comment period; Maintainer consensus required to approve
- **Examples:** Adding a new role, changing review requirements, modifying lifecycle states

### Accreditation and Recognition Decisions
- **Who decides:** Maintainers in consultation with external advisors as appropriate
- **Process:** Documented in `docs/accreditation.md` with rationale
- **Examples:** Pursuing TEQSA registration, seeking AISA/ACS endorsement

---

## 4. Versioning Policy

### Curriculum Versioning
- The degree curriculum is versioned using the format `YEAR.SEMESTER`
  - Example: `2026.1` (first semester 2026), `2026.2` (second semester 2026)
- A new version is declared when a batch of content reaches "Published" status at the
  end of a development cycle
- Version history maintained in `CHANGELOG.md` (to be created when first version publishes)

### Unit Versioning
- Individual units are versioned using semantic versioning: `vMAJOR.MINOR`
  - `v1.0` — Initial publication
  - `v1.1` — Minor update (clarification, additional examples, minor corrections)
  - `v2.0` — Major revision (significant content rewrite, learning outcome changes,
    assessment redesign)
- Unit version is recorded in the Unit Metadata section of each unit file

### Framework Reference Versioning
- All framework references must specify the version used
  - Example: `SFIA 9 (2023)`, `NIST NICE DCWF (November 2023)`, `MITRE ATT&CK v19`
- When a new framework version is released, the Framework Custodian initiates a review
  cycle; units are updated and version references incremented accordingly

### Breaking Changes
- A breaking change is any change that affects prerequisite pathways, credit point values,
  or learning outcome scope
- Breaking changes require:
  1. A migration notice in the unit file explaining what changed and why
  2. An entry in `CHANGELOG.md`
  3. Maintainer consensus approval

---

## 5. Conflict Resolution

If there is disagreement between contributors or reviewers:

1. **Good faith discussion** — Raise the disagreement as a comment on the relevant PR or Issue
2. **Maintainer review** — If unresolved, a Maintainer reviews the evidence and makes a decision
3. **Consensus escalation** — If a Maintainer's decision is contested, all active Maintainers
   vote; majority rules
4. **External consultation** — For technical disputes (e.g., framework mapping accuracy),
   an independent Domain Expert may be consulted

All decisions are documented publicly in the relevant PR or Issue thread.

### 5.1 Disputed Content & Framework Mappings — Escalation

Section 5 covers general disagreement. Disputes about **content accuracy** or
**framework-mapping correctness** carry extra weight because they affect the
credibility of the degree and the "employer visibility" guarantee (every T-code must
trace to real evidence). They follow this dedicated, time-boxed escalation ladder.

**What counts as a disputed-content matter**

- A factual/technical claim in a unit is challenged as inaccurate or unsafe
- A framework mapping (NICE DCWF T-code, SFIA level, ASD/ATT&CK reference) is
  challenged as wrong, retired, mis-versioned, or unsupported by a lab/assessment
- Two reviewers reach incompatible conclusions on technical accuracy

**Escalation ladder**

| Step | Action | Owner | Target time |
|---|---|---|---|
| 1. Raise | Open an issue (use **Framework Mapping Error** for mappings) or comment on the PR, citing the specific claim/mapping and a primary source | Anyone | — |
| 2. Author response | The unit author responds with evidence or accepts the correction | Author | 7 days |
| 3. Expert review | If unresolved, the relevant **Domain Expert** (content) or **Framework Custodian** (mappings) adjudicates against primary sources | Domain Expert / Framework Custodian | 14 days |
| 4. Maintainer decision | If still contested, a **Maintainer** decides on the documented evidence | Maintainer | 7 days |
| 5. Independent expert | For deep technical splits, an **independent Domain Expert** (not previously involved) is consulted; their finding is decisive for the technical question | Maintainers (appoint) | as needed |

**Evidence standard**

- Technical claims must be supported by a **primary source** (vendor/standards-body
  documentation, the framework's own publication, peer-reviewed work). Blog posts and
  secondary summaries may inform but do not by themselves settle a dispute.
- For framework mappings, the authoritative version is the one recorded in the
  currency table in [`docs/frameworks.md`](frameworks.md). A mapping is only valid if
  the cited code exists in that version **and** traces to a specific lab/assessment.

**Status of content while disputed**

- A **Published** unit under an open accuracy/mapping dispute is labelled
  **`Framework Review Required`** (mappings) or flagged in its metadata (content) until
  resolved; it remains available but carries the notice.
- A unit **in review** does not advance to `Practitioner Approved` or
  `Framework Verified` while a relevant dispute is open.
- Resolutions are recorded in the originating issue/PR and, for mappings, as a row in
  the Currency Review Log in `docs/frameworks.md`.

**Conflicts of interest**

Anyone with a conflict (e.g. a vendor relationship affecting a tool/mapping
recommendation, or authorship of the disputed content) must disclose it and recuse
from adjudicating that dispute.

---

## 6. Becoming a Maintainer or Domain Expert

### Maintainer
- Demonstrated sustained contribution to the project (minimum 6 months, multiple merged PRs)
- Nominated by an existing Maintainer
- Approved by Maintainer consensus
- No limit on number of Maintainers

### Domain Expert
- Active professional experience in the relevant domain
- Submit a brief professional background in the PR for the unit(s) you are reviewing
- Approved by a Maintainer
- Domain Experts are listed in the unit metadata of units they have reviewed

### Framework Custodian
- Strong familiarity with at least 2 of the mapped frameworks (NICE, SFIA, ASD, MITRE ATT&CK)
- Nominated and approved by Maintainer consensus
- One Framework Custodian role; may be held by a Maintainer

---

## 7. Code of Conduct

All participants are expected to:
- Act professionally and respectfully
- Prioritize accuracy and learner outcomes over speed
- Disclose any conflicts of interest (e.g., vendor relationships affecting tool recommendations)
- Follow the 7 core contribution rules in `CONTRIBUTING.md`

Violations are handled by Maintainers. Severe or repeated violations may result in
removal from the project.
