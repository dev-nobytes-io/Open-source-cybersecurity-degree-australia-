# SPL-06: Implementation & Consulting Practice — Splunk Core Certified Consultant

> **Part of:** [EXT-SPL — The Splunk Series](index.md)
> **Status:** Draft · **Version:** v0.1 · **Last Reviewed:** 2026-09-09
> **Domain Expert:** _Unassigned_ · **Practitioner Reviewer:** _Unassigned — must hold Core Certified Consultant_

!!! warning "Non-credit, vendor-specific"
    See the [series index](index.md) for the R3 carve-out. Nothing here satisfies a
    core-unit requirement.

---

## Target certification

| Field | Value | Verified |
|---|---|---|
| Certification | [Splunk Core Certified Consultant](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-consultant.html) | 2026-09-09 |
| Level | **Expert** — the top of the platform ladder | 2026-09-09 |
| Prerequisite certifications | **All four**: Core Certified Power User, Core Certified Advanced Power User\*, Enterprise Certified Admin, Enterprise Certified Architect | 2026-09-09 |
| Prerequisite coursework | **2 mandatory for registration**; 6 in the published track (below) | 2026-09-09 |
| Length | 120 minutes | 2026-09-09 |
| Format | 86 multiple choice questions | 2026-09-09 |
| Price | US$130 per attempt | 2026-09-09 |
| Delivery | Pearson VUE | 2026-09-09 |

!!! note "Naming"
    The certification is **Splunk Core Certified Consultant**. "Splunk Certified
    Consultant" is a common informal shortening and will not find the official page.

### The prerequisite chain in full

This is the most heavily gated credential in the Splunk portfolio. The chain is
cumulative, not alternative:

```mermaid
graph LR
    PU["Core Certified<br/>Power User"] --> APU["Core Certified<br/>Advanced Power User *"]
    PU --> EA["Enterprise<br/>Certified Admin"]
    EA --> ARCH["Enterprise<br/>Certified Architect"]
    APU --> CONS["Core Certified<br/>Consultant"]
    ARCH --> CONS
    CONS --> AUTH["Email request to<br/>splunk_certification@cisco.com"]
    AUTH --> EXAM["Exam authorisation"]
```

\* **The one published substitution in the entire ladder.** *In lieu of* earning the
Advanced Power User certification, candidates may instead complete **all 14 courses
recommended for the Advanced Power User certification**. No other rung offers a
substitution.

### The coursework gate

**Required to qualify for exam registration — both:**

1. `Core Consultant Labs`
2. `Services: Core Implementation`

**Also named in the published track:** `Indexer Cluster Implementation`,
`Distributed Search Migration`, `Implementation Fundamentals`, `Architect Implementation 1–3`.

!!! danger "Authorisation is manual, and eligibility may be restricted"
    Unlike [Architect](spl-05-architect.md), where authorisation arrives automatically,
    **Consultant authorisation must be requested**. Candidates who are Splunk Enterprise
    Certified Architects and have completed the required coursework **must email
    `splunk_certification@cisco.com`** to request their Core Consultant exam
    authorisation.

    **`Core Consultant Labs` is reported to require the Architect certification as a
    precondition, and the Consultant track as a whole is oriented toward Splunk partners
    and employees.** A learner outside that channel may be unable to register at any
    price. This is reported by practitioners rather than stated on the exam page — see
    [Verification status](#verification-status).

    **Confirm eligibility before committing time or money to this track.** Advising a
    learner to pursue a credential they cannot register for is the worst failure mode
    available to this series.

**Zero-cost achievable: no.** Four prerequisite certifications, mandatory paid coursework
at two levels, restricted-access labs, and manual authorisation. This is an
employer-sponsored track for people working at Splunk or a Splunk partner.

---

## Overview

!!! info "Read this module even if you will never sit the exam"
    The credential is gated. **The content is not.** Implementation discipline —
    standardised base configurations, requirements you can actually verify, migrations
    that can be rolled back, and telling a client something they do not want to hear — is
    the most transferable material in the entire series. It applies to any platform
    engagement, and it is genuinely useful to a graduate who will never touch the exam.

    Treat SPL-06 as the capstone of the series. The exam is optional; the practice is not.

Every module before this one asked *can you build it?* This one asks *can you build it for
someone else, on their estate, against their constraints, and leave them able to run it?*

That is a different discipline, and three things characterise it.

**Standardisation beats cleverness.** The single most valuable artefact in Splunk
consulting is the **base configuration** — a standardised, documented set of `.conf`
settings applied consistently across every deployment. Splunk's own consultant courseware
centres on this, including the props-and-transforms settings practitioners refer to as the
"Great 8". A bespoke deployment that only its author understands is a liability handed to
the client, however elegant it is.

**Requirements are extracted, not received.** Clients ask for a SIEM and mean a compliance
artefact, or a dashboard for an executive, or a fix for an incident that already happened.
The consultant's first job is to find the requirement behind the request, and the second is
to say when the stated budget cannot buy the stated outcome. That conversation is where
consulting engagements are won or lost, and it is the same stakeholder-communication skill
[SC06](../../../core/units/SC06-stakeholder-communication.md) teaches.

**You leave.** An engagement ends. Everything you built must survive your departure:
documented, handed over, and operable by people who were not in the room. Design decisions
that depend on the designer are defects.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [SPL-05](spl-05-architect.md) | **Enforced prerequisite** (via the Architect certification), and the design skills applied here. |
| [SPL-02](spl-02-power-user.md) | **Enforced prerequisite** (via Power User and Advanced Power User). Base configs are largely knowledge-layer and parsing standardisation. |
| [SE06 — Capstone: Architecture Design](../../../degrees/strategic/security-engineering/SE06-capstone-architecture-design.md) | **Closest degree analogue.** A defensible design delivered to a stakeholder under constraint. |
| [SC06 — Stakeholder Communication](../../../core/units/SC06-stakeholder-communication.md) | **Directly relevant.** Requirements elicitation, difficult conversations, and reporting to non-technical audiences. |
| [SC04 — Vendor & Supply Chain Risk](../../../core/units/SC04-vendor-supply-chain-risk.md) | The client's side of the engagement: you *are* the third party. |
| [SC05 — Security Program Management](../../../core/units/SC05-security-program-management.md) | Scoping, sequencing and delivering work that outlives the engagement. |
| [Leadership major](../../../degrees/strategic/leadership/README.md) | Professional practice, influence without authority, and client relationship management. |

---

## Learning outcomes

On completion, a learner can:

1. **Elicit** requirements from a client whose stated request differs from their actual
   need, and **document** them in verifiable form.
2. **Design** and **apply** a standardised base configuration, and **justify** deviation
   from it where a client constraint genuinely requires one.
3. **Plan** and **execute** an implementation or migration with staged validation and
   rollback at each stage.
4. **Evaluate** an existing deployment against good practice and **produce** a prioritised,
   costed remediation roadmap.
5. **Communicate** a technical recommendation — including an unwelcome one — to a
   non-technical decision-maker.
6. **Create** handover documentation sufficient for a team that was not present to operate
   the deployment.

> Bloom's 4–6, expert level.

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Enterprise Architect | SP-ARC-001 | T0473 | Document and address organisational requirements in system design | Lab 1, Lab 5 |
| 2023 | Security Architect | SP-ARC-002 | T0050 | Design system security architecture and supporting infrastructure | Lab 2, Lab 4 |
| 2023 | Systems Requirements Planner | SP-SRP-001 | T0033 | Define baseline system security requirements | Lab 1 |
| 2023 | Systems Requirements Planner | SP-SRP-001 | T0454 | Translate functional requirements into technical solutions | Lab 1, Lab 4 |
| 2023 | System Administrator | OM-ADM-001 | T0431 | Automate and standardise system administration | Lab 2 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Consultancy | CNSL | Level 5 | Lab 1, Lab 5 |
| Requirements definition and management | REQM | Level 5 | Lab 1 |
| Solution architecture | ARCH | Level 5 | Lab 4 |
| Configuration management | CFMG | Level 5 | Lab 2 |
| Release and deployment | RELM | Level 4–5 | Lab 3 |
| Stakeholder relationship management | RLMT | Level 5 | Lab 5 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Security Architecture | Platform & Infrastructure Design | Advanced | Lab 2, Lab 4 |
| Governance & Risk | Advice & Assurance | Advanced | Lab 1, Lab 5 |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-06-K01 | Knowledge of base-configuration methodology and standardised parsing settings | Topic 2; Lab 2 |
| Knowledge | SPL-06-K02 | Knowledge of implementation methodology and staged validation | Topic 3; Lab 3 |
| Knowledge | SPL-06-K03 | Knowledge of migration patterns and their rollback constraints | Topic 4; Lab 3 |
| Knowledge | SPL-06-K04 | Knowledge of health-assessment method for an existing deployment | Topic 5; Lab 4 |
| Skill | SPL-06-S01 | Skill in eliciting and documenting verifiable requirements | Lab 1 |
| Skill | SPL-06-S02 | Skill in applying and defending a standardised base configuration | Lab 2 |
| Skill | SPL-06-S03 | Skill in producing operable handover documentation | Lab 5 |
| Ability | SPL-06-A01 | Ability to tell a client their stated budget cannot buy their stated outcome | Lab 5; Summative |
| Ability | SPL-06-A02 | Ability to prioritise remediation by risk and cost rather than by ease | Lab 4 |
| Ability | SPL-06-A03 | Ability to design so the deployment survives the consultant's departure | Lab 5; Summative |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — The engagement | 1 | 1 | 8 |
| B — Standardisation | 2 | 2 | 12 |
| C — Implementation and migration | 3–4 | 3 | 14 |
| D — Assessment and remediation | 5 | 4 | 10 |
| E — Communication and handover | 6–7 | 5 | 12 |
| | | | **~56 hours** |

---

## Topics

### Topic 1: The Engagement and the Real Requirement

Scoping, statements of work, and the gap between what a client asks for and what they
need. Common patterns: the compliance-driven deployment where nobody will read the alerts,
the executive dashboard as the actual deliverable, the "we bought Splunk, now what"
engagement, and the rescue of a deployment someone else abandoned.

Turning requirements into something **verifiable**. "Improve our security monitoring" is
not a requirement; "detect and alert on privileged account creation across all domain
controllers within five minutes, with evidence retained twelve months" is. The second can
be tested at handover. The first can be argued about forever, which is how engagements go
bad.

Scope creep, change control, and the observation that the most expensive words in
consulting are "while we're in there".

### Topic 2: Base Configurations and Standardisation

The consultant's core artefact. A standardised, documented, version-controlled set of
configurations applied consistently: `props.conf` and `transforms.conf` settings for
correct parsing, index definitions, forwarder outputs, and the deployment apps that carry
them.

Splunk's consultant courseware centres on this and on the props settings practitioners
call the **"Great 8"** — the parsing settings that, set explicitly, prevent the great
majority of onboarding defects. The principle generalises well beyond Splunk: **set the
things that matter explicitly rather than relying on inference**, because inference works
until the day the data changes shape.

Why standardisation wins: it is reviewable, it is transferable between engagements, it
makes defects diagnosable, and it means the client's estate looks like every other client's
estate to the next consultant. Deviation is allowed — but it must be justified and
documented, or it is just drift with a better story.

### Topic 3: Implementation Method

Sequencing a build: infrastructure, cluster, data onboarding, knowledge layer, content,
handover. Validation gates between stages, and the discipline of not proceeding past a
failed gate because the schedule says so.

Onboarding at scale: the standard process from [SPL-04](spl-04-enterprise-admin.md)
Topic 3 applied to fifty sources with a prioritisation order, driven by which detections
the client actually needs (which is [SPL-03](spl-03-cyber-defense-analyst.md)'s two-gap
distinction, used as a planning input rather than an assessment output).

Working in someone else's change-management process, with someone else's approvals, on
someone else's production estate.

### Topic 4: Migration

Version upgrades, single-site to multi-site, self-managed to Splunk Cloud, and
consolidation of deployments after an acquisition — the last being extremely common and
extremely messy.

Data migration constraints, index compatibility, and knowledge-object portability. The
recurring problem: the knowledge layer is what makes the data useful, and it is the part
that migrates worst.

**Rollback planning at each stage**, and identifying the point of no return honestly.
A migration plan without a stated point of no return has one anyway — it is just undocumented.

### Topic 5: Health Assessment of an Existing Deployment

The engagement type most consultants meet most often: an estate that grew organically for
five years and now underperforms.

A structured assessment method: configuration hygiene (`btool` at estate scale), index and
retention correctness, data-onboarding quality and CIM compliance, knowledge-layer debt
(the audit from [SPL-02](spl-02-power-user.md) Lab 5), search and scheduler performance,
capacity headroom against the model from [SPL-05](spl-05-architect.md) Topic 6, and
detection-content health from [SPL-03](spl-03-cyber-defense-analyst.md) Topic 9.

Producing a **prioritised, costed roadmap** — ordered by risk and value, not by what is
easiest to fix or most interesting to the consultant. Distinguishing what must be fixed
now, what can be deferred, and what should simply be accepted and documented as residual
risk.

### Topic 6: Communicating the Unwelcome

The skill that most distinguishes a senior consultant, and the one vendor courseware
teaches least.

- Telling a client their deployment is badly built, without making an enemy of the person
  who built it — who is usually in the room and will implement your recommendations.
- Telling a client their budget cannot buy their outcome, with the options that follow:
  reduce scope, increase budget, or accept the risk explicitly.
- Presenting to executives: what to include, what to leave out, and the discipline of
  leading with the decision required rather than the analysis performed.
- Writing a recommendation that survives being forwarded without you attached to it.

Grounded in [SC06](../../../core/units/SC06-stakeholder-communication.md).

### Topic 7: Handover and Leaving Well

Documentation that is actually operable: runbooks, the base config and its rationale, the
decision register, known limitations, and the things you would fix with more time.

Knowledge transfer to a team that was not present for the decisions. Sustainable
operations — a deployment that requires a consultant on retainer to remain healthy is a
failed engagement, even though it is a profitable one.

**The decision register** is the highest-value handover artefact and the one most often
skipped: not what was built, but *why it was built that way and what was rejected*. Without
it, the next person to touch the estate will re-litigate every decision from scratch,
usually badly.

---

## Labs & exercises

!!! note "These labs are mostly not technical"
    Labs 1, 4 and 5 need no Splunk instance at all and are the most valuable in the module.
    Labs 2 and 3 need a lab deployment — reuse the [SPL-05](spl-05-architect.md) cluster
    inside the same trial window.

    Because the certification's own labs are access-restricted, these are written to be
    runnable **outside** Splunk's partner channel. They do not substitute for
    `Core Consultant Labs` for registration purposes and cannot — see
    [the coursework gate](#the-coursework-gate).

### Lab 1: Find the Real Requirement

Given a client brief that states the wrong requirement (provided scenario, or role-played
with a peer), conduct requirements elicitation and produce a verifiable requirements
document.

**Deliverable:** the requirements, each with a stated acceptance test, plus a short note on
**what the client asked for, what they actually need, and how you established the
difference**. That note is the assessed artefact.

### Lab 2: Build a Base Configuration

Produce a documented, version-controlled base configuration: index definitions, parsing
standards with the key `props.conf` settings explicit, forwarder outputs, and deployment
apps to carry them. Apply it to a lab deployment and onboard three dissimilar sources
using only the standard.

**Deliverable:** the base config in version control with a README explaining every
non-obvious setting, plus one documented, justified deviation.

### Lab 3: Staged Migration with Rollback

Migrate a lab deployment (e.g. single-site to clustered, or a version upgrade across a
cluster). Define stages, validation gates and rollback procedures **before** starting.

Then have a peer inject a failure at a stage of their choosing, and execute the rollback.

**Deliverable:** the plan, evidence of the executed rollback, and an honest account of what
the plan did not anticipate.

### Lab 4: Health Assessment and Roadmap

Given an intentionally degraded deployment (or a documented case study), conduct a
structured health assessment and produce a prioritised, costed remediation roadmap.

**Deliverable:** findings with evidence, a roadmap ordered by risk and value with effort
estimates, and an explicit "accept and document" category. A roadmap where everything is
priority one is a failed roadmap.

### Lab 5: Deliver the Bad News, Then Hand Over

Two parts, both assessed on communication.

1. Present the Lab 4 findings to a role-played client stakeholder whose team built the
   deployment you are criticising, and to an executive who wants to know why it will cost
   more than expected.
2. Produce the handover pack: runbooks, decision register, known limitations.

**Deliverable:** the presentation (or a recording), the handover pack, and a reflection on
what you would say differently. The decision register is weighted most heavily.

---

## Assessment

### Formative 1: Rewrite the Requirement

Given six vague client statements, rewrite each as a verifiable requirement with an
acceptance test, and name the question you would have to ask the client to do so honestly.

### Formative 2: What Would You Not Fix?

Given a health-assessment finding list, select the items you would recommend **accepting**
rather than remediating, and defend each. Assesses proportionality — the consultant failure
mode is recommending everything.

### Summative: Engagement Package

For a described Australian client with a stated budget, a compliance driver, an existing
degraded deployment and an unrealistic expectation:

1. Verifiable requirements, with the gap between stated request and actual need made explicit.
2. Target architecture with a base-configuration standard.
3. Implementation or migration plan with staged validation and rollback.
4. Prioritised, costed roadmap including an accepted-risk category.
5. An executive communication delivering at least one unwelcome message.
6. A handover pack including a decision register.
7. **A statement of what you recommended against, and why.**

Items 5 and 7 carry disproportionate weight. A package that gives the client everything
they asked for, within a budget that cannot support it, and without a single documented
disagreement, is marked as a failure of professional judgement — not rewarded as
customer service.

---

## Australian context

- **Professional and contractual liability.** A consultant's design advice carries
  obligations under Australian Consumer Law and the engagement contract. Recommendations
  should be recorded, and so should the client's decision to reject one. The decision
  register in Topic 7 is a professional-protection artefact as much as a technical one.
- **The client's third-party risk obligations are your engagement conditions.** Under
  **APRA CPS 234** a regulated entity must ensure information-security capability of
  third parties handling its information assets, and **CPS 230** adds operational-risk and
  service-provider management requirements. The **SOCI Act 2018 (Cth)** imposes analogous
  expectations for critical-infrastructure responsible entities. When you consult for these
  organisations, you are the third party in someone's risk register — which is
  [SC04](../../../core/units/SC04-vendor-supply-chain-risk.md) viewed from the other side.
- **Consultant access to client data is a privacy exposure.** Building and troubleshooting
  a Splunk deployment means searching real production logs containing personal information
  under the **Privacy Act 1988 (Cth)**. Access scope, duration and offshore access by
  distributed delivery teams all need to be settled in the engagement, not assumed.
- **IRAP and government engagements.** Consulting on Australian Government systems brings
  personnel security-clearance requirements, the **Hosting Certification Framework** for
  hosting arrangements, and ISM-aligned assessment. These constrain who may perform the
  work, not just how.
- **Essential Eight and ISM as the usual compliance driver.** Most Australian Splunk
  engagements have a compliance trigger behind them. The consulting skill is delivering
  genuine monitoring capability *and* the evidence artefact, while being honest that the
  two are not the same thing — and that a client who only wants the second is buying
  something that will not detect an intrusion.
- **The market reality.** The Australian Splunk consulting market is small and
  relationship-driven. Reputation compounds, and so does the consequence of a deployment
  handed over in a state only its author understands.

---

## Verification status

- **Verified 2026-09-09:** all exam facts above, against the linked official page and the
  [Consultant track flowchart](https://www.splunk.com/en_us/pdfs/training/splunk-core-certified-consultant-track.pdf) —
  Expert level, 120 minutes, 86 questions, US$130, Pearson VUE.
- **Verified 2026-09-09:** the prerequisite chain is **cumulative** — all four
  certifications, not one of them. An earlier reading of the HTML page as "one of the
  following" was contradicted by the track flowchart, which lists all four under
  *Prerequisite Certification(s)*; the flowchart is treated as authoritative here.
- **Verified 2026-09-09:** `Core Consultant Labs` and `Services: Core Implementation` are
  the two courses required to qualify for exam registration; the four additional track
  courses; manual authorisation via `splunk_certification@cisco.com`; and the
  14-course substitution for Advanced Power User.
- **NOT VERIFIED — and consequential.** The restriction of `Core Consultant Labs` /
  `Services: Core Implementation` to Splunk partners and employees, and the report that
  `Core Consultant Labs` requires the Architect certification as a precondition, come from
  **practitioner community reports, not from Splunk's published exam page**. Splunk does
  not publish eligibility criteria for these courses.

    !!! danger "Confirm before advising any learner"
        This must be confirmed with Splunk Education directly before a learner is advised
        to pursue the Consultant track. If the restriction holds, the credential is
        unavailable to learners outside the partner channel regardless of ability, and
        this module should be presented as **content without a reachable credential**.

- **Not verified:** the exam code is not published and is deliberately not stated. Course
  pricing varies by region and is deliberately not quoted. The "Great 8" props settings
  are named as practitioner terminology; the exact set has **not** been verified against
  current courseware and no specific settings are listed here. Topic coverage is the
  module author's reading of consulting practice and has **not** been reconciled against
  Splunk's published test blueprint.
- **Requires a currently-certified reviewer.** This module must not reach Practitioner
  Approved without review by someone holding a **current** Core Certified Consultant
  certification, who can confirm both the eligibility question and the base-configuration
  content.
- Framework mappings and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [Core Certified Consultant track](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-consultant.html) — official exam page and test blueprint.
- [Consultant track flowchart (PDF)](https://www.splunk.com/en_us/pdfs/training/splunk-core-certified-consultant-track.pdf) — the source for the cumulative prerequisite chain, the coursework gate, the email authorisation, and the 14-course substitution.
- [Core Consultant Labs course description (PDF)](https://www.splunk.com/en_us/pdfs/training/core-consultant-labs-course-description.pdf) — course content and stated preconditions.
- [Core Implementation training course description (PDF)](https://www.splunk.com/en_us/pdfs/training/core-implementation-training-course-description.pdf) — the second mandatory course.
- [Splunk Validated Architectures](https://www.splunk.com/en_us/pdfs/tech-brief/splunk-validated-architectures.pdf) — Splunk's own reference topologies; the standardisation argument in Topic 2 applied to whole deployments.
- [Splunk Enterprise Admin Manual — configuration file precedence](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Wheretofindtheconfigurationfiles) — the mechanics underneath base configurations.
- [APRA CPS 234](https://www.apra.gov.au/information-security) and [CPS 230](https://www.apra.gov.au/operational-risk-management) — the client-side obligations that become engagement conditions.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-06 |
| Module Title | Implementation & Consulting Practice — Splunk Core Certified Consultant |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 4–6 (Analyse / Evaluate / Create) |
| Notional Hours | ~56 |
| Zero-cost achievable | **No** — four prerequisite certifications, mandatory paid coursework, restricted-access labs, manual authorisation |
| Credential reachable outside the partner channel? | **Unconfirmed — see [Verification status](#verification-status)** |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
