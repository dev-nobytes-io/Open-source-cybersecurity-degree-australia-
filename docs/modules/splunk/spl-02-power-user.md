# SPL-02: Knowledge Objects & Data Models — Power User and Advanced Power User

> **Part of:** [EXT-SPL — The Splunk Series](index.md)
> **Status:** Draft · **Version:** v0.1 · **Last Reviewed:** 2026-09-09
> **Domain Expert:** _Unassigned_ · **Practitioner Reviewer:** _Unassigned_

!!! warning "Non-credit, vendor-specific"
    See the [series index](index.md) for the R3 carve-out. Nothing here satisfies a
    core-unit requirement.

---

## Target certifications

This module covers **two** rungs, because they are continuous in content and because the
first is the most commercially important credential in the entire ladder.

| Field | Core Certified Power User | Core Certified Advanced Power User |
|---|---|---|
| Official page | [link](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-power-user.html) | [link](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-advanced-power-user.html) |
| Level | Entry | Intermediate |
| Prerequisite certification | **None** | **Core Certified Power User** |
| Prerequisite coursework | **None published** | **None published** |
| Length | 60 minutes | 60 minutes |
| Format | 65 multiple choice questions | 70 multiple choice questions |
| Price | US$130 per attempt | US$130 per attempt |
| Delivery | Pearson VUE | Pearson VUE |

*All facts verified 2026-09-09.*

!!! success "This is the load-bearing certification"
    **Core Certified Power User is the single most valuable rung in the ladder**, for two
    reasons. First, it is the prerequisite for *both* the Enterprise Admin track (and
    therefore Architect, and therefore Consultant) and it is the knowledge baseline Splunk
    recommends for the Cybersecurity Defense Analyst. Second, it has **no prerequisite of
    its own and no mandatory coursework** — it is the highest-value credential a
    self-funding learner can reach for US$130 and free courseware.

    This is also the credential that
    [`docs/structure.md`](../../structure.md) and
    [`docs/compliance/workforce-frameworks.md`](../../compliance/workforce-frameworks.md)
    mean when they list *"Splunk Core Certified"* as a Detection Engineering bridge.

**Zero-cost achievable: yes**, for both rungs. Everything in this module runs on a Splunk
Free instance except scheduled/accelerated data-model behaviour, noted where relevant.

!!! note "The Advanced Power User substitution"
    For the Consultant track only, Splunk permits candidates to complete **all 14 courses
    recommended for the Advanced Power User certification** *in lieu of* earning the
    certification itself. This is the only published substitution anywhere in the ladder.
    It does not help anyone outside the Consultant track — see [SPL-06](spl-06-consultant.md).

---

## Overview

[SPL-01](spl-01-core-user.md) taught searching. This module is about **not searching from
scratch every time** — and that turns out to be the whole game.

A Splunk deployment succeeds or fails on its **knowledge layer**: the extractions,
aliases, tags, event types, lookups and data models that turn raw vendor-specific logs
into something a detection engineer can write against once and have it work across
twenty log sources. Without that layer, every detection is bespoke to one product's log
format and breaks when the vendor changes it. With it, a single search covers the
category.

The organising idea is the **Common Information Model (CIM)** — Splunk's normalisation
standard. CIM is why `Authentication.action=failure` works whether the underlying events
came from Windows, Linux, Okta or a firewall. Everything in
[SPL-03](spl-03-cyber-defense-analyst.md) depends on data being CIM-compliant, and the
most common reason Enterprise Security "doesn't work" at a real customer site is that it
isn't. That failure is diagnosed in SPL-04 and prevented in SPL-06.

The Advanced Power User half adds the performance dimension: **accelerated data models
and `tstats`**. The difference between a search that scans raw events and one that hits a
`tsidx` summary is often two orders of magnitude, and it is the difference between a
detection that can run every five minutes and one that cannot run at all.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [SPL-01](spl-01-core-user.md) | **Direct prerequisite.** Search pipeline, time, `stats`, `eval`. |
| [DE02 — Data Sources & Log Engineering](../../../degrees/operational/detection-engineering/DE02-data-sources-log-engineering.md) | **Assumed core unit.** DE02 teaches normalisation, data modelling and telemetry gaps vendor-neutrally. SPL-02 is CIM as one concrete implementation of that theory. |
| [DE03 — Writing Detection Logic](../../../degrees/operational/detection-engineering/DE03-writing-detection-logic.md) | DE03 already teaches SPL alongside KQL, YARA and Sigma. SPL-02 goes deeper on the Splunk side only. |
| [F06 — Data & Log Analysis](../../../core/units/F06-data-log-analysis.md) | Assumed. |
| [SPL-03](spl-03-cyber-defense-analyst.md), [SPL-04](spl-04-enterprise-admin.md) | **Both depend on this module.** ES requires CIM; administration requires understanding what knowledge objects cost. |

---

## Learning outcomes

On completion, a learner can:

1. **Create** the full range of knowledge objects — field extractions, aliases,
   calculated fields, event types, tags, lookups and macros — and select the right one for
   a given normalisation problem.
2. **Analyse** a non-compliant data source against the Common Information Model and
   produce the mapping required to bring it into compliance.
3. **Design** a data model, and **evaluate** when acceleration is justified against its
   storage and indexer cost.
4. **Apply** `tstats` and accelerated data models to make an expensive search viable.
5. **Evaluate** knowledge-object permissions and naming as a governance problem, not a
   convenience setting.
6. **Justify** the choice between a search-time extraction and an index-time change.

> Bloom's 3–5. The step from "create objects" to "judge what they cost" is what separates
> the two rungs this module covers.

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0166 | Engineer correlation and automated response | Lab 4, Lab 5 |
| 2023 | Data Analyst | DA-ANL-001 | T0342 | Analyse data sources to produce actionable information | Lab 1, Lab 2 |
| 2023 | Systems Developer | SP-SYS-002 | T0014 | Design and develop data structures and models | Lab 3 |
| 2023 | Cyber Defense Infrastructure Support | PR-INF-001 | T0335 | Build and maintain content for monitoring systems | Lab 2, Lab 4 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Data modelling and design | DTAN | Level 4 | Lab 2, Lab 3 |
| Data management | DATM | Level 3–4 | Lab 1, Lab 5 |
| Security operations | SCAD | Level 3–4 | Lab 4 |
| Systems & software life cycle / assurance | SURE | Level 3 | Lab 5 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Defensive Operations | Monitoring & Analysis | Practitioner | Lab 4 |
| Secure Systems | Data Engineering & Normalisation | Practitioner | Lab 2, Lab 3 |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-02-K01 | Knowledge of the knowledge-object taxonomy and its precedence rules | Topic 1–2; Lab 1 |
| Knowledge | SPL-02-K02 | Knowledge of the Common Information Model and its role in portable detection | Topic 4; Lab 2 |
| Knowledge | SPL-02-K03 | Knowledge of data-model acceleration mechanics and cost | Topic 6; Lab 3 |
| Knowledge | SPL-02-K04 | Knowledge of knowledge-object permission scoping and app context | Topic 7; Lab 5 |
| Skill | SPL-02-S01 | Skill in authoring extractions, lookups and macros for reuse | Lab 1 |
| Skill | SPL-02-S02 | Skill in mapping a non-compliant source to CIM | Lab 2 |
| Skill | SPL-02-S03 | Skill in rewriting a raw search as `tstats` against an accelerated model | Lab 3 |
| Ability | SPL-02-A01 | Ability to judge acceleration cost against detection benefit | Lab 3; Summative |
| Ability | SPL-02-A02 | Ability to diagnose a broken detection as a normalisation failure rather than a logic failure | Lab 4; Formative 2 |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — The knowledge layer | 1–3 | 1 | 10 |
| B — Normalisation and CIM | 4–5 | 2, 4 | 12 |
| C — Performance | 6 | 3 | 10 |
| D — Governance of the knowledge layer | 7–8 | 5 | 8 |
| | | | **~40 hours** |

---

## Topics

### Topic 1: The Knowledge Object Taxonomy

Field extractions (regex and delimiter), field aliases, calculated fields, event types,
tags, workflow actions, lookups, and macros. What each one is *for*, and — the part
learners get wrong — the fact that several of them can solve the same problem with very
different maintenance costs.

The judgement to develop: an alias is cheap and reversible; a regex extraction is
brittle; an index-time change is expensive and permanent. Choose accordingly.

### Topic 2: Precedence and Why Your Field Is Wrong

Configuration precedence in Splunk is a genuine source of production incidents. App
context, user context, and the layering of `props.conf` and `transforms.conf`. Why the
same search returns different fields for two users, and how to prove which configuration
won using `btool`.

This topic is the seed of a skill the Architect exam tests hard, and it is the single most
useful debugging technique in the platform.

### Topic 3: Lookups and Macros — Enrichment and Reuse

File-based, KV-store and external lookups; automatic lookups and their cost. Macros as
the mechanism for not repeating yourself, with arguments.

Enrichment is where a SOC turns an IP address into an asset owner and a business
criticality. That mapping is the difference between an alert and a decision — it is the
same asset-and-identity problem that
[OC02](../../../core/units/OC02-security-monitoring-siem.md) raises conceptually, and it
becomes the Asset & Identity framework in [SPL-03](spl-03-cyber-defense-analyst.md).

### Topic 4: The Common Information Model

CIM as a set of data models with agreed field names, and the Splunk Add-on as the usual
unit of CIM compliance. Working through a data source that is *not* compliant: identifying
which model it belongs to, which fields are missing, and what to alias, extract or tag.

**The strategic point:** CIM compliance is what makes detection content portable. A Sigma
rule, an ESCU detection, or a correlation search written against `Authentication` works
across every compliant source and none of the non-compliant ones. Detection content is
only as good as the normalisation beneath it — which is exactly DE02's argument, in
Splunk's vocabulary.

### Topic 5: Data Models

Datasets, objects, constraints, and inheritance. Building a data model from scratch and
mapping events into it. `pivot` as the non-SPL interface, and why analysts who only know
pivot hit a ceiling.

### Topic 6: Acceleration, `tsidx` and `tstats`

**The Advanced Power User core.** How report and data-model acceleration actually work,
what a `tsidx` summary contains, and where it lives. `tstats` syntax and its constraints —
in particular that it operates on indexed and modelled fields, not arbitrary search-time
extractions, which is why it is fast and why it sometimes cannot answer your question.

The trade-off to internalise: acceleration buys search speed with **indexer CPU and
disk**. A deployment with every data model accelerated and a modest indexing tier is a
deployment that has moved its performance problem rather than solved it. This is the
first genuinely architectural judgement in the series and it returns in
[SPL-05](spl-05-architect.md).

Also cover: summary indexing, and when it is still the right answer over acceleration.

### Topic 7: Permissions, Naming and App Context

Private / app / global scope. Why a knowledge object that works for its author and
nobody else is the most common support ticket in a Splunk deployment. Naming conventions,
and the fact that the knowledge layer is shared mutable state across every team using the
platform.

!!! warning "Free-licence gap"
    Splunk Free has **no authentication, no users and no roles**, so permission scoping
    cannot be demonstrated hands-on. Cover it conceptually here; it becomes practical in
    [SPL-04](spl-04-enterprise-admin.md) under a trial licence.

### Topic 8: Knowledge as Technical Debt

Orphaned objects, duplicated extractions, lookups nobody owns, macros that encode a
business rule that changed two years ago. Reviewing and retiring knowledge objects.

This is the topic vendor courseware skips and practitioners care about most. A five-year-old
Splunk deployment is usually 30% useful knowledge objects and 70% archaeology.

---

## Labs & exercises

Labs 1–3 and 5 run on **Splunk Free**. Lab 3's acceleration behaviour is observable but
scheduled acceleration is best seen under a trial licence. Observe the
[series safety rules](index.md#safety-authorisation-and-data-handling).

### Lab 1: Build the Knowledge Layer for a Messy Source

Take a deliberately awkward log source (inconsistent delimiters, embedded key-value pairs,
a timestamp in a non-obvious position). Produce a working set of extractions, aliases and
an event type.

**Deliverable:** the objects, plus a written justification of *why each type was chosen*.
Solving everything with regex is marked down.

### Lab 2: Make a Source CIM-Compliant

Given a non-compliant source, map it to the appropriate CIM data model. Prove compliance
by running a stock CIM-based search and getting correct results.

**Deliverable:** the mapping, the passing search, and a gap statement listing every CIM
field that could **not** be populated and what telemetry would be needed to populate it.
The gap statement is the most valuable artefact — it is the same discipline DE02 teaches
as telemetry-gap analysis.

### Lab 3: Accelerate, and Pay For It

Write an expensive search over a large sample dataset. Record its runtime. Build and
accelerate a data model that answers the same question; rewrite as `tstats`; record the
runtime again. Then measure the **storage consumed by the acceleration summary** and the
indexer load while it builds.

**Deliverable:** a before/after table covering search time, disk cost and build cost, and
a recommendation on whether acceleration is justified here. "It got faster" is not a
sufficient answer.

### Lab 4: Break a Detection with Normalisation

Take a working CIM-based detection. Introduce a realistic normalisation regression — a
vendor changes a field name in an upgrade. Observe the detection silently return zero
results.

**Deliverable:** a description of how you would have *detected the detection failing*.
Silent failure of a security control is the point of this lab, and it connects directly
to [DE05 — Detection Operations](../../../degrees/operational/detection-engineering/DE05-detection-operations-management.md).

### Lab 5: Audit a Knowledge Layer

Given an app with accumulated knowledge objects, produce an inventory: what exists, what
is used, what is orphaned, what is duplicated.

**Deliverable:** a retirement proposal with a risk note for each object proposed for
removal.

---

## Assessment

### Formative 1: Which Object?

Given eight normalisation problems, choose the knowledge object type for each and defend
the choice in one sentence. Assesses judgement, not recall.

### Formative 2: Why Is This Search Empty?

Five searches returning no results for five different reasons — permissions/app context,
a normalisation regression, a `tstats` field that isn't in the model, a time-range error,
and precedence. Diagnose each. This is the diagnostic skill the Architect exam assumes.

### Summative: Normalisation and Performance Case

Given a scenario with three log sources, a set of detections the SOC needs to run, and a
stated indexing tier capacity: deliver a knowledge-layer design including CIM mapping,
an acceleration recommendation with justified cost, a telemetry-gap statement, and a
naming/permission convention.

Full marks require an explicit statement of **what you chose not to accelerate and why**.

---

## Australian context

- **Enrichment and personal information.** Lookups that map IP or username to a named
  individual, their role, or their department turn machine data into personal information
  under the **Privacy Act 1988 (Cth)**. Asset-and-identity enrichment is operationally
  necessary and privacy-relevant at the same time; the lookup is the point where that
  transformation happens, and it should be a deliberate, documented decision.
- **Employee monitoring.** In NSW the *Workplace Surveillance Act 2005*, and comparable
  obligations elsewhere, constrain how employee activity may be monitored and require
  notice. A knowledge layer that makes per-user activity trivially searchable is a
  surveillance capability regardless of the intent behind it. Covered properly in
  [F05](../../../core/units/F05-legal-ethics-compliance.md).
- **ISM and Essential Eight event logging.** The normalisation work in this module is
  what makes centralised logging *useful* rather than merely present. An organisation can
  satisfy a logging control on paper and still be unable to answer an incident question —
  the gap statement from Lab 2 is the honest version of that assessment.
- **Data sovereignty.** Where lookups and KV-store collections live matters for
  IRAP-assessed and government workloads. Raised properly in
  [SPL-05](spl-05-architect.md), where deployment location becomes a design decision.

---

## Verification status

- **Verified 2026-09-09:** all exam facts in the table above, against the linked official
  pages; the Advanced Power User 14-course substitution (Consultant track only).
- **Not verified:** exam codes are not published and are deliberately not stated. Splunk
  publishes **no mandatory prerequisite coursework** for either rung — recommended-course
  lists exist but are not authoritative for registration. Topic coverage is the module
  author's reading of the platform and has **not** been reconciled against the published
  test blueprints.
- The claim that "Splunk Core Certified" in
  [`docs/structure.md`](../../structure.md) and
  [`docs/compliance/workforce-frameworks.md`](../../compliance/workforce-frameworks.md)
  means **Core Certified Power User** is this series' reading, and those documents should
  be updated to say so — tracked in [`docs/TODO.md`](../../TODO.md).
- Framework mappings and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [Core Certified Power User track](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-power-user.html) and [Advanced Power User track](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-advanced-power-user.html) — official exam pages and test blueprints.
- [Splunk Common Information Model documentation](https://docs.splunk.com/Documentation/CIM) — the normalisation standard this module is built around.
- [Knowledge Manager Manual](https://docs.splunk.com/Documentation/Splunk/latest/Knowledge/WhatisSplunkknowledge) — the authoritative reference for every object type in Topic 1.
- [Splunk free courses](https://www.splunk.com/en_us/training/free-courses.html) — knowledge objects, data models, statistical processing and SPL2 fundamentals are all in the free catalogue.
- [`tstats` command reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Tstats) — Topic 6.
- [Splunkbase](https://splunkbase.splunk.com/) — technology add-ons are the usual delivered form of CIM compliance.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-02 |
| Module Title | Knowledge Objects & Data Models — Power User and Advanced Power User |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 3–5 (Apply / Analyse / Evaluate) |
| Notional Hours | ~40 |
| Zero-cost achievable | Yes (excluding exam fees) |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
