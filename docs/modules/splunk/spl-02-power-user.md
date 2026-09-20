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
    It does not help anyone outside the Consultant track — see [SPL-08](spl-08-consultant.md).

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
isn't. That failure is diagnosed in SPL-06 and prevented in SPL-08.

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
| [SPL-03](spl-03-cyber-defense-analyst.md), [SPL-06](spl-06-enterprise-admin.md) | **Both depend on this module.** ES requires CIM; administration requires understanding what knowledge objects cost. |

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
| A — The knowledge layer | 1–6 | 1 | 20 |
| B — The command and function set | 7–11 | 6, 7 | 24 |
| C — Normalisation and CIM | 12–13 | 2, 4 | 14 |
| D — Performance and acceleration | 14, 20 | 3 | 16 |
| E — Advanced constructs and analytics | 15–17 | 7 | 12 |
| F — Governance of the knowledge layer | 18–19 | 5 | 8 |
| **G — Dashboards and Simple XML (33% of the APU exam)** | **21–25** | **8** | **30** |
| | | | **~124 hours** |

---

## Blueprint alignment

Verified against the published test blueprints
([Power User](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-power-user.pdf),
[Advanced Power User](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-advanced-power-user.pdf)),
both retrieved 2026-09-09.

**Power User** — 10 domains. Note how heavily it weights knowledge objects and event
correlation, and that it contains **no acceleration or `tstats` content at all**.

| Domain | Weight | Covered by |
|---|---|---|
| 1.0 Transforming commands for visualizations (`chart`, `timechart`) | 5% | Topic 7 (and [SPL-01](spl-01-core-user.md) Topic 11) |
| 2.0 Filtering and formatting (`eval`, `search`/`where`, `fillnull`) | 10% | Topic 7 |
| 3.0 **Correlating events (transactions, grouping, `transaction` vs `stats`)** | **15%** | Topic 11 |
| 4.0 Creating and managing fields (Field Extractor: regex, delimiter) | 10% | Topic 3 |
| 5.0 Field aliases and calculated fields | 10% | Topic 1 |
| 6.0 Tags and event types | 10% | Topic 6 |
| 7.0 Macros (arguments, variables) | 10% | Topic 6 |
| 8.0 **Workflow actions (GET, POST, Search)** | **10%** | Topic 6 |
| 9.0 Data models and pivot | 10% | Topic 13 |
| 10.0 CIM add-on | 10% | Topic 12 |

**Advanced Power User** — 22 domains. The distribution is the surprise:

| Domain group | Weight | Covered by |
|---|---|---|
| 1.0–2.0 Statistical commands and `eval` functions | 8% | Topics 7–8 |
| 3.0 Lookups (advanced options, KV Store, external, geospatial) | 4% | Topic 5 |
| 4.0 Alerts (log events, lookups in alerts, webhooks) | 4% | Topic 6 + [SPL-01](spl-01-core-user.md) Topic 12 |
| 5.0 Advanced field creation (`erex`, `rex`, regex performance) | 4% | Topic 3 |
| 6.0 Self-describing data (`spath`, `multikv`) | 3% | Topic 4 |
| 7.0 Advanced search macros (nesting, previewing) | 3% | Topic 6 |
| 8.0–9.0 Acceleration (reports, summary indexing, data models, `tsidx`, `tstats`) | 8% | Topic 14 |
| 10.0–11.0 Using search efficiently; search tuning (Lispy, `TERM`) | 7% | Topics 15, 20 |
| 12.0–13.0 Manipulating data (`bin`, `xyseries`, `untable`, `foreach`); multivalue | 13% | Topics 9, 15 |
| 14.0 Advanced transactions | 5% | Topic 11 |
| 15.0 Working with time | 2% | [SPL-01](spl-01-core-user.md) Topic 4 |
| 16.0 Subsearches (caveats, when not to, troubleshooting, `append`) | 6% | Topic 10 |
| **17.0–22.0 Dashboards: Simple XML, forms and tokens, performance, customisation, drilldowns, advanced behaviours** | **33%** | **Topics 21–25** |

!!! warning "A third of the Advanced Power User exam is dashboard development"
    Domains 17.0–22.0 total **33%** — Simple XML views, form inputs and tokens, base and
    post-process searches, event annotations, drilldowns and event handlers. That is more
    than acceleration, subsearches, multivalue and transactions combined.

    This is counter-intuitive: the credential reads as a search-mastery certification and
    is in substantial part a dashboard-development certification. Candidates who prepare
    only on SPL routinely fail it, and an earlier draft of this module would have led them
    to do exactly that.

**Beyond the blueprint** — Topics 2 (precedence and `btool`), 16 (statistical/predictive
commands), 17 (SPL2), 18 (permissions) and 19 (knowledge debt) are practitioner content,
not examined at this level. Topic 2 is examined in
[SPL-06](spl-06-enterprise-admin.md); the rest are included because they matter in
production.

---

## Topics

### Topic 1: The Knowledge Object Taxonomy

Field extractions (regex and delimiter), field aliases, calculated fields, event types,
tags, workflow actions, lookups, macros, data models, and saved searches. What each one is
*for*, and — the part learners get wrong — the fact that several of them can solve the same
problem with very different maintenance costs.

The judgement to develop: an alias is cheap and reversible; a regex extraction is brittle;
an index-time change is expensive and permanent. Choose accordingly.

### Topic 2: Precedence, App Context and `btool`

Configuration precedence in Splunk is a genuine source of production incidents. App
context, user context, and the layering of `props.conf` and `transforms.conf`. Why the same
search returns different fields for two users.

`btool` as the tool that answers "which setting actually applied?" —
`splunk btool props list --debug` and reading the output. The discipline of proving
precedence before forming a theory.

This is the seed of a skill the Architect exam tests hard, and the single most useful
debugging technique in the platform.

### Topic 3: Field Extraction in Depth

Regular expressions for Splunk: named capture groups, non-greedy matching, anchoring, and
character classes. The performance difference between a well-anchored regex and one that
backtracks.

`rex` (inline), `erex` (example-driven), the field extractor UI, and persistent extractions
in `props.conf`/`transforms.conf`. `REPORT` versus `EXTRACT` versus `TRANSFORMS` and what
each implies about when extraction happens.

Delimiter-based extraction for CSV-like data. Multi-value extraction with `max_match`.
`sed`-mode `rex` for masking sensitive values at search time — with the caveat that this is
presentation, not protection: the data is still in the index.

**Search-time versus index-time extraction:** the decision, its cost, and why the default
answer is search-time.

### Topic 4: Structured Data — JSON, XML and Key-Value

`spath` for JSON and XML path extraction, including array handling and the `{}` notation.
Automatic extraction for `key=value` data and `KV_MODE` settings. `xmlkv` and `extract`.

Working with nested and deeply-nested JSON, which is now the common case for cloud and API
telemetry. Flattening strategies and their cost.

`tojson` and `fromjson` for constructing and parsing structured values in-pipeline.

### Topic 5: Lookups — Enrichment in Every Form

- **File-based (CSV)** lookups: definition, matching, output fields, case sensitivity, and
  size limits.
- **KV Store** collections: when to use them over CSV, `inputlookup`/`outputlookup` against
  a collection, and their role in stateful content.
- **Automatic lookups** and their cost — invisible enrichment applied to every search
  touching a sourcetype, which is powerful and easy to over-apply.
- **External (scripted)** lookups for dynamic enrichment.
- **Geospatial** lookups and `iplocation` for geographic enrichment.
- **Time-bounded** lookups, which matter when the mapping changes over time (an IP that
  belonged to a different host last month).

Commands: `lookup`, `inputlookup`, `outputlookup`, and the `append`/`OVERWRITE` semantics
that silently destroy data when misunderstood.

Enrichment is where a SOC turns an IP address into an asset owner and a business
criticality. That mapping is the difference between an alert and a decision — the same
problem [OC02](../../../core/units/OC02-security-monitoring-siem.md) raises conceptually,
and it becomes the Asset & Identity framework in
[SPL-04](spl-04-enterprise-security.md).

### Topic 6: Macros, Event Types, Tags and Workflow Actions

**Macros:** arguments, validation, and nesting. Macros as the mechanism for not repeating
yourself, and the readability cost when they nest three deep.

**Event types:** naming a search condition so it can be referenced as a field. **Tags:**
attaching vocabulary to field-value pairs, and the tag-based abstraction that CIM depends
on — `tag=authentication` working across every compliant source is the whole point.

**Workflow actions:** GET/POST/search actions that let an analyst pivot from an event to an
external system or another search. Under-used, and one of the cheapest wins in analyst
efficiency.

### Topic 7: The `eval` Function Library

The Advanced Power User expects fluency here, not familiarity. Worked coverage by family:

| Family | Functions |
|---|---|
| **Conditional** | `if`, `case`, `validate`, `coalesce`, `nullif`, `in`, `searchmatch` |
| **String** | `len`, `lower`, `upper`, `substr`, `replace`, `trim`/`ltrim`/`rtrim`, `split`, `mvjoin`, `urldecode`, `spath` |
| **Comparison/Info** | `isnull`, `isnotnull`, `isnum`, `isstr`, `typeof`, `like`, `match`, `cidrmatch` |
| **Mathematical** | `abs`, `ceiling`, `floor`, `round`, `sigfig`, `pow`, `sqrt`, `exp`, `ln`, `log`, `pi` |
| **Statistical** | `max`, `min`, `random`, `sum` (row-wise, distinct from `stats` aggregates) |
| **Time** | `now`, `time`, `strftime`, `strptime`, `relative_time`, `strptime` format specifiers |
| **Multivalue** | `mvcount`, `mvindex`, `mvfilter`, `mvjoin`, `mvappend`, `mvdedup`, `mvsort`, `mvzip`, `mvmap`, `mvrange` |
| **Cryptographic** | `md5`, `sha1`, `sha256`, `sha512` |
| **Conversion** | `tonumber`, `tostring` (including the `"commas"`, `"duration"`, `"hex"` formats) |
| **JSON** | `json_extract`, `json_keys`, `json_valid`, `json_object`, `json_array` |

`cidrmatch` deserves specific attention: subnet matching in security work is constant and
learners routinely do it wrong with string comparison.

**The null-handling theme** runs through all of it. An absent field is not an empty one,
and most functions return null on null input — which propagates silently through the rest
of the pipeline.

### Topic 8: The `stats` Family — `eventstats`, `streamstats`, `tstats`

The four commands that look similar and behave completely differently:

- **`stats`** — aggregates and *replaces* the result set.
- **`eventstats`** — aggregates and *appends the result to every row*, preserving events.
  The tool for "compare this event to the average".
- **`streamstats`** — computes a *running* aggregate in order, with `window`, `current`,
  `time_window`, `global` and `reset_on_change`. The tool for sequence and rate-of-change
  problems: failed logins in a rolling window, time between events, first-seen detection.
- **`tstats`** — operates on indexed and modelled fields only, and is therefore orders of
  magnitude faster. Constraints, `prestats`, `summariesonly`, and the `append` pattern.

**Behavioural baselining with `eventstats` and `streamstats`** is the honest, explainable
alternative to machine learning for most anomaly problems, and it is a recurring theme from
[SPL-04](spl-04-enterprise-security.md) Topic 11.

Also: `sistats`/`sitimechart` and the summary-indexing family, and when they still beat
data-model acceleration.

### Topic 9: Multivalue Fields

Where multivalue fields come from, and why they surprise people — a field that is
sometimes single and sometimes multi produces intermittent bugs.

Commands: `mvexpand` (and its memory limits, which are a real operational constraint),
`mvcombine`, `makemv`, `nomv`. The `eval` multivalue functions from Topic 7 applied
properly.

Multivalue fields in `stats` and `where` clauses: what `=` means when the left side has
three values. This is a genuinely counter-intuitive area and worth explicit drilling.

### Topic 10: Correlating Datasets — Subsearches, `join`, `append`, `union`

The commands learners over-use and practitioners avoid:

- **Subsearches** — the `[ ... ]` syntax, `format`, `return`, and the hard limits
  (result count and time) that cause a subsearch to be **silently truncated**, producing a
  wrong answer with no error. This is one of the most dangerous behaviours in SPL.
- **`join`** — types, and why it is usually the wrong answer: slow, subject to subsearch
  limits, and almost always replaceable.
- **`append`, `appendcols`, `appendpipe`, `union`** — and their ordering and column
  semantics.
- **`set`** — union, diff and intersect over two result sets.

**The `stats`-based alternative.** Nearly every `join` can be rewritten as a single search
across both datasets followed by `stats ... by <key>`. It is faster, has no truncation
limit, and is the idiom experienced Splunk practitioners actually use. Teaching this
rewrite explicitly is one of the highest-value things in the module.

`lookup` as the third option when one side is small and static.

### Topic 11: `transaction` and Sequence Analysis

`transaction` with `startswith`, `endswith`, `maxspan`, `maxpause` and `maxevents`.
Transaction fields (`duration`, `eventcount`).

**When `transaction` is genuinely right** — when you need the events themselves grouped and
the grouping depends on ordering or start/end markers — and when `stats by` is the correct
and much faster answer. The default assumption should be `stats`; `transaction` must be
argued for.

Sequence detection with `streamstats` as a third approach.

### Topic 12: The Common Information Model

CIM as a set of data models with agreed field names, and the Splunk Add-on as the usual
unit of CIM compliance. The major models a security practitioner lives in: Authentication,
Network Traffic, Web, Endpoint, Malware, Change, Intrusion Detection, Email, Certificates.

Working through a data source that is *not* compliant: identifying which model it belongs
to, which fields are missing, and what to alias, extract or tag. The CIM validation
dashboards in the CIM add-on.

**The strategic point:** CIM compliance is what makes detection content portable. A Sigma
rule, an ESCU detection, or a correlation search written against `Authentication` works
across every compliant source and none of the non-compliant ones. Detection content is only
as good as the normalisation beneath it — which is exactly DE02's argument, in Splunk's
vocabulary.

### Topic 13: Data Models

Datasets (event, search, transaction), objects, constraints, attributes and inheritance.
Building a data model from scratch and mapping events into it. Calculated and lookup
attributes within a model.

`pivot` and the Pivot UI as the non-SPL interface, and why analysts who only know pivot hit
a ceiling. `datamodel` command syntax for searching a model directly.

### Topic 14: Acceleration, `tsidx` and Performance

**The Advanced Power User core.** How report and data-model acceleration actually work,
what a `tsidx` summary contains, and where it lives. Acceleration time ranges, backfill,
and rebuild.

`tstats` in depth: syntax against accelerated models, `summariesonly=true` versus `false`
and the correctness implication of each, `allow_old_summaries`, and combining `tstats` with
`tstats append` for federated results.

The trade-off to internalise: acceleration buys search speed with **indexer CPU and disk**.
A deployment with every data model accelerated and a modest indexing tier has moved its
performance problem rather than solved it. This is the first genuinely architectural
judgement in the series and it returns in [SPL-07](spl-07-architect.md).

Also: summary indexing, `collect`, and when it is still the right answer over acceleration.

### Topic 15: Advanced Search Constructs

- **`foreach`** — iterating over fields, including wildcard field sets, for
  normalisation work that would otherwise be twenty near-identical `eval` statements.
- **`map`** — running a search per result, and the strong warning that it is slow and
  usually indicates the problem should be solved differently.
- **`makeresults`** — generating synthetic events for testing, which is how you unit-test
  SPL logic without waiting for real data.
- **`eventstats`/`streamstats` composition** for multi-pass logic.
- **`bin`/`bucket`** for manual time and numeric bucketing.
- **`untable`/`xyseries`** for reshaping result sets between wide and long form — the
  commands people need for charting and never remember.
- **`addinfo`**, `addtotals`, `accum`, `delta`.

### Topic 16: Statistical and Predictive Commands

Where SPL's built-in analytics genuinely help:

`anomalydetection`, `anomalies`, `outlier`, `cluster`, `predict`, `trendline`, `x11`.
`rare` and `top` as first-pass outlier tools. `associate` and `correlate` for relationship
discovery.

The Machine Learning Toolkit as an adjacent option, treated properly in
[SPL-04](spl-04-enterprise-security.md) Topic 11.

**The stance to establish here:** an unexplainable result is an untriageable result. These
commands are useful when a human can see *why* something was flagged. Prefer the
`streamstats` baseline you can explain to the clustering you cannot.

### Topic 17: SPL2

What SPL2 is, where it currently applies, and how it differs from SPL. Splunk publishes
free SPL2 courseware and it appears in the certification blueprints.

Treated as **awareness-level** here rather than depth: SPL2's rollout across the product
line is still in progress, and this module does not assert a migration timeline. Flagged
for re-verification.

### Topic 18: Permissions, Naming and App Context

Private / app / global scope. Why a knowledge object that works for its author and nobody
else is the most common support ticket in a Splunk deployment. Naming conventions, and the
fact that the knowledge layer is shared mutable state across every team using the platform.

Knowledge object precedence when two apps define the same object. Exporting objects between
apps.

!!! warning "Free-licence gap"
    Splunk Free has **no authentication, no users and no roles**, so permission scoping
    cannot be demonstrated hands-on. Cover it conceptually here; it becomes practical in
    [SPL-06](spl-06-enterprise-admin.md) under a trial licence.

### Topic 19: Knowledge as Technical Debt

Orphaned objects, duplicated extractions, lookups nobody owns, macros that encode a
business rule that changed two years ago. Reviewing and retiring knowledge objects, and
using `| rest` to inventory what exists.

This is the topic vendor courseware skips and practitioners care about most. A five-year-old
Splunk deployment is usually 30% useful knowledge objects and 70% archaeology.

### Topic 20: Search Tuning Internals — Lispy, TERM and Pre-Filtering

The blueprint's *More Search Tuning* domain, and the part of Splunk performance that most
practitioners never learn.

Pre-filtering search data. **Lispy** — the internal representation Splunk derives from
your search to decide which index buckets and terms to read — and how to see it in the job
inspector. How boolean operators and wildcards change the lispy expression, and why a
leading wildcard produces a lispy that matches everything.

The **`TERM()` directive**: forcing Splunk to treat a string as a single indexed term,
which is dramatically faster for values containing minor segmenters (IP addresses, GUIDs,
paths). Knowing when `TERM()` helps and when it silently returns nothing is a genuine
practitioner skill.

### Topic 21: Simple XML and Dashboard Prototyping

**The Advanced Power User blueprint devotes roughly a third of the exam to dashboard
development.** This is not a peripheral topic.

Simple XML syntax for views: the document structure, rows, panels, and the search element.
Building a view from scratch rather than from the UI, and reading the XML behind a
UI-built dashboard.

Best practices for creating views, and **troubleshooting views** — the malformed XML, the
search that works in the search bar and not in the panel, and the panel that renders empty.

### Topic 22: Forms, Tokens and Inputs

**How tokens work** — the substitution model that makes a dashboard interactive, and the
single concept that unlocks everything in Topics 23–25.

Form inputs: text, dropdown, radio, checkbox, multiselect, and time. Setting and consuming
tokens. Default and initial values, and the difference between them.

**Cascading inputs** — where one input's selection populates another's choices, which is
where token dependency ordering starts to matter.

**Token filters** (`$token$`, `$token|s$`, `$token|n$`) and why the unfiltered form is an
injection risk in a dashboard that accepts user input.

### Topic 23: Drilldowns

Types of drilldown: none, row, cell, chart-area, and custom. **Predefined tokens**
(`$click.value$`, `$click.name$`, `$row.<field>$`, `$earliest$`, `$latest$`) and which are
available in which context — a common source of "my drilldown does nothing".

Dynamic drilldowns: passing tokens to another dashboard, to a search, or to an external
URL. Contextual drilldowns that change behaviour based on what was clicked.

### Topic 24: Dashboard Performance

**Base and post-process searches** — the single most important dashboard performance
technique. One base search feeding several post-process panels instead of six panels each
running their own search.

The constraints candidates get wrong: post-process searches inherit the base search's
results, the base search has a result limit that silently truncates, and a transforming
command in the base changes what the post-process can do.

Using `tstats` in dashboard panels. Panel refresh and delay times, and scheduling a
dashboard's searches rather than running them on load.

### Topic 25: Advanced Dashboard Behaviours

Customising chart and panel properties in XML rather than the UI. Disabling search-access
features (export, open-in-search) for dashboards shown to non-analyst audiences.

**Event annotations** — overlaying discrete events (deployments, incidents, change windows)
onto a time chart, which is how a dashboard stops showing *what* happened and starts
showing *why*.

Event handlers and event actions. Simple XML extensions, and the boundary at which a
requirement stops being a dashboard and becomes an app — a judgement worth making
explicitly, because Simple XML extended far enough becomes unmaintainable.


---

## Labs & exercises

!!! tip "Lab guide: how to actually run these"
    **[SPL-02 lab guide](../../../labs/guides/spl-02.md)** gives the setup, the commands and the
    verification for every lab below — against the
    **[lab environment](../../../labs/README.md)**, a reproducible synthetic estate of
    ~130k labelled events with ground truth, so you can measure a real positive
    predictive value rather than estimate one.

    The split of responsibility: **this page says why each lab exists and what to
    deliver; the guide says how to run it.** Marking criteria stay here.

    Seven of eight run on Splunk Free; Lab 3's acceleration needs a trial, and the guide gives the design-only path where a licence is unavailable.

    Self-assess with the **[52-question quiz](quiz.md)**.

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

### Lab 6: Eliminate the `join`

Given three searches written with `join`, `append` and a subsearch, rewrite each as a
single search using `stats by` or `lookup`. Measure both versions.

Then demonstrate the **silent subsearch truncation**: construct a subsearch that exceeds
the result limit and show that it returns a confidently wrong answer with no error.

**Deliverable:** the three rewrites with before/after timings, and evidence of the
truncation failure with a note on how you would have detected it in production. This is the
single most valuable SPL habit in the module.

### Lab 7: Baseline Without Machine Learning

Using `streamstats` and `eventstats`, build a behavioural baseline that flags a user whose
activity departs from their own recent norm — not a global threshold.

Handle the multivalue and null cases correctly; the lab dataset should contain both.

**Deliverable:** the search, the flagged results, and an explanation an analyst could read
of *why* each result was flagged. Then state what an ML approach would add and what it
would cost in explainability.

---

### Lab 8: Build a Real Dashboard in Simple XML

Build a dashboard **in Simple XML**, not by clicking. It must include: at least three
form inputs with one **cascading** pair, a **base search with two post-process panels**, a
**dynamic drilldown** passing tokens to a second view, and an **event annotation** overlay
on a time chart.

Then measure it: compare load time against a naive version where every panel runs its own
search.

**Deliverable:** the XML, the performance comparison, and a note on which token filter you
used on any input whose value reaches a search, and why. A dashboard that interpolates a
raw `$token$` into a search is marked down as an injection defect.

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
  [SPL-07](spl-07-architect.md), where deployment location becomes a design decision.

---

## Verification status

- **Verified 2026-09-09:** all exam facts in the table above, against the linked official
  pages; the Advanced Power User 14-course substitution (Consultant track only).
- **Not verified:** exam codes are not published and are deliberately not stated. Splunk
  publishes **no mandatory prerequisite coursework** for either rung — recommended-course
  lists exist but are not authoritative for registration. Topic coverage **has now been reconciled against the published test blueprint** — see
  [Blueprint alignment](#blueprint-alignment). Sub-objective wording is not reproduced;
  the mapping uses domain titles and weightings only.
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
| Notional Hours | ~124 |
| Zero-cost achievable | Yes (excluding exam fees) |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
