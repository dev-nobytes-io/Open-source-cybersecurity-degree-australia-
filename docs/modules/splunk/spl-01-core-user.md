# SPL-01: Search Fundamentals — Splunk Core Certified User

> **Part of:** [EXT-SPL — The Splunk Series](index.md)
> **Status:** Draft · **Version:** v0.1 · **Last Reviewed:** 2026-09-09
> **Domain Expert:** _Unassigned_ · **Practitioner Reviewer:** _Unassigned_

!!! warning "Non-credit, vendor-specific"
    See the [series index](index.md) for the R3 carve-out. Nothing here satisfies a
    core-unit requirement.

---

## Target certification

| Field | Value | Verified |
|---|---|---|
| Certification | [Splunk Core Certified User](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-user.html) | 2026-09-09 |
| Level | Entry | 2026-09-09 |
| Prerequisite certification | **None** | 2026-09-09 |
| Prerequisite coursework | **None** | 2026-09-09 |
| Length | 60 minutes | 2026-09-09 |
| Format | 60 multiple choice questions | 2026-09-09 |
| Price | US$130 per attempt | 2026-09-09 |
| Delivery | Pearson VUE | 2026-09-09 |

**Zero-cost achievable: yes.** Free eLearning plus a Splunk Free instance covers this
rung end to end. The only unavoidable cost is the exam fee, and the exam is optional —
the knowledge is the point.

!!! note "Is this rung worth sitting?"
    Commercially, **Core Certified User is usually skipped**. It has no prerequisite and
    is not a prerequisite for anything: Power User does not require it. Most candidates
    go straight to Power User and save US$130. This module exists because the *knowledge*
    is genuinely foundational and everything above depends on it — not because the
    credential is a good buy. Advise learners accordingly.

---

## Overview

Every Splunk skill above this one is a search skill wearing a costume. Clustering exists
to make searches finish; data models exist to make searches fast; risk-based alerting is
a search that runs on a schedule and keeps score. If a learner's mental model of the
search pipeline is wrong, that error propagates all the way to the Architect exam, where
it shows up as an inability to reason about why a distributed search is slow.

So this module is not "SPL syntax". It is the **execution model**: what Splunk does to
your data between the moment you press enter and the moment rows appear. The single most
valuable idea in it is that a Splunk search is a *pipeline of commands operating on an
event stream*, that the pipeline has a cost profile, and that where you put a filter
determines whether the search takes two seconds or two hours.

The second most valuable idea is **search-time schema**. Splunk does not require you to
define fields before indexing. This is the platform's defining design decision and the
source of both its flexibility and most of its performance problems. Learners coming from
a relational or a schema-on-write background consistently get this wrong.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [F06 — Data & Log Analysis](../../../core/units/F06-data-log-analysis.md) | **Assumed prerequisite.** F06 teaches log structure, timestamps, and query thinking vendor-neutrally. SPL-01 is the Splunk dialect of what F06 already taught. |
| [F01 — Networking Fundamentals](../../../core/units/F01-networking-fundamentals.md) | Assumed: hosts, ports, protocols, and what a log line represents. |
| [SPL-02](spl-02-power-user.md) | **Direct successor.** SPL-02 begins where this module stops. |

---

## Learning outcomes

On completion, a learner can:

1. **Explain** the Splunk data pipeline from input through parsing, indexing and search,
   and identify at which stage a given field is created.
2. **Apply** the search-processing language to filter, transform and aggregate events,
   using the pipeline order that minimises work.
3. **Interpret** time in Splunk — the difference between `_time`, index time, and wall
   clock — and select time ranges that answer the question actually asked.
4. **Use** field extraction, `stats` and `eval` to turn raw events into an answer.
5. **Demonstrate** basic reporting and dashboard construction from a saved search.

> Bloom's levels 2–3, appropriate to an entry-level rung. Higher levels appear from
> [SPL-02](spl-02-power-user.md) onward.

---

## Framework mappings

> **Provisional pending Framework Custodian review**, consistent with the rest of the
> repository. These do **not** feed [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0258 | Provide timely detection and reporting of anomalous activity | Lab 2 |
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0295 | Analyse identified malicious activity to determine method of exploitation | Lab 3 |
| 2023 | Data Analyst | DA-ANL-001 | T0342 | Analyse data sources to produce actionable information | Lab 1, Lab 2 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Data visualisation | VISL | Level 2–3 | Lab 4 |
| Security operations | SCAD | Level 2 | Lab 3 |
| Data management | DATM | Level 2 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Defensive Operations | Monitoring & Analysis | Foundational | Lab 2, Lab 3 |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-01-K01 | Knowledge of the Splunk index-time vs search-time schema distinction | Topic 2; Lab 1 |
| Knowledge | SPL-01-K02 | Knowledge of the search pipeline and command cost profile | Topic 3; Lab 2 |
| Knowledge | SPL-01-K03 | Knowledge of time semantics: `_time`, `_indextime`, time zones | Topic 4; Lab 2 |
| Skill | SPL-01-S01 | Skill in writing filtered, ordered SPL that minimises events reaching the search head | Lab 2 |
| Skill | SPL-01-S02 | Skill in aggregating with `stats` and computing with `eval` | Lab 3 |
| Ability | SPL-01-A01 | Ability to translate an investigative question into a search that answers it | Lab 3; Assessment |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — How Splunk sees data | 1–3 | 1 | 8 |
| B — Time | 4 | 2 | 5 |
| C — Searching and the command set | 5–10 | 2, 3, 5 | 20 |
| D — Reporting and visualisation | 11–13 | 4, 6 | 10 |
| E — Lookups and platform | 14–15 | 4, 7 | 10 |
| | | | **~53 hours** |

---

## Blueprint alignment

Verified against the published
[Core Certified User test blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-user.pdf),
retrieved 2026-09-09.

| Domain | Weight | Covered by |
|---|---|---|
| 1.0 Splunk basics (components, uses, apps, user settings, navigation) | 5% | Topics 1, 3 |
| 2.0 **Basic searching** (run, time range, results, refine, timeline, events, control a search job, save results) | **22%** | Topics 3, 4, 6, 13 |
| 3.0 **Using fields in searches** (understand fields, use in searches, fields sidebar) | **20%** | Topics 2, 3, 7 |
| 4.0 Search language fundamentals (search pipeline, specify indexes, `table`, `rename`, `fields`, `dedup`, `sort`) | 15% | Topics 5, 6, 9 |
| 5.0 Basic transforming commands (`top`, `rare`, `stats`) | 15% | Topics 8, 9 |
| 6.0 Reports and dashboards | 12% | Topics 11, 12 |
| 7.0 **Creating and using lookups** | **6%** | Topic 15 |
| 8.0 Scheduled reports and alerts | 5% | Topic 12 |

!!! note "Lookups are examined at this level"
    Domain 7.0 puts **lookup creation and automatic lookups in the entry-level exam**,
    which is earlier than the topic's difficulty suggests. Topic 15 covers it here;
    [SPL-02](spl-02-power-user.md) Topic 5 goes deeper into KV Store, external and
    geospatial lookups for the Advanced Power User level.

**Beyond the blueprint** — Topics 10 (field extraction) and 14 (export and REST) are not
examined at this level. Both are included because they are needed constantly in practice
and because SPL-02 assumes them.

---

## Topics

### Topic 1: What Splunk Actually Is

A distributed search engine over time-series text, not a database. The consequences of
that sentence: no schema declaration, no joins in the relational sense, no update-in-place,
and a cost model driven by how many events must be read off disk and shipped to a search
head.

Introduce the three roles a single-instance install collapses together — **forwarder,
indexer, search head** — because SPL-06 and SPL-07 pull them apart, and a learner who
never knew they were separate will struggle there.

Splunk Enterprise versus Splunk Cloud versus Splunk Free: what differs, and which
constraints apply to this module's labs.

### Topic 2: The Data Pipeline and Search-Time Schema

Input → parsing → indexing → search. What happens at each stage, and critically **which
fields exist when**.

- **Index time:** `host`, `source`, `sourcetype`, `_time`, `index`, `_raw`. Fixed at
  ingest. Getting these wrong is expensive to fix — it means re-indexing.
- **Search time:** everything else. Extracted on the fly, every time, per search.

The trade-off is the platform's central design decision: flexibility at ingest, cost at
search. Learners should be able to state which of the two is cheap to change and why
this makes `sourcetype` decisions strategically important — a theme that returns in
SPL-06 and dominates SPL-08.

The internal fields (`_time`, `_raw`, `_indextime`, `_cd`) and why they behave differently
from ordinary fields.

### Topic 3: Events, Indexes and the Search App

What constitutes an event; multi-line events and why they are the hard case. Indexes as the
unit of storage, retention and access control — the last being the reason index choice is a
security decision, developed in [SPL-06](spl-06-enterprise-admin.md).

The Search & Reporting app: the search bar, the timeline, the events/statistics/
visualisation tabs, the fields sidebar (selected versus interesting fields), and the search
history. Search modes — **fast, smart, verbose** — and what each one does to field
discovery and therefore to performance. Learners who never change the mode never understand
why their field disappeared.

### Topic 4: Time

Time is the axis Splunk is built on and the most common source of wrong answers.

- `_time` (event time, parsed from the event) versus `_indextime` (when Splunk saw it).
- Time-zone handling, and why a misconfigured forwarder produces events "in the future".
- The time-range picker versus `earliest`/`latest` in the search string.
- **Relative time modifiers and snap-to:** `-24h`, `-7d@d`, `@w0`, `+1mon`, and why
  `@d` (snap to midnight) changes results in ways learners do not expect.
- `now()`, `relative_time()` and time arithmetic.
- Why a narrow time range is the single cheapest optimisation available.
- Real-time searches, and why they are usually the wrong tool.

An investigation that uses index time when it needed event time — or vice versa — reaches
a confidently wrong conclusion. Practise both.

### Topic 5: The Search Pipeline and Command Types

SPL as a pipeline of commands joined by `|`. The distinction that matters most:

- **Streaming commands** operate per event and can run distributed on the indexers
  (`eval`, `rex`, `where`, `fields`).
- **Transforming commands** reshape the result set and run on the search head
  (`stats`, `chart`, `timechart`, `top`, `rare`).
- **Generating commands** produce their own results and must lead the pipeline
  (`tstats`, `inputlookup`, `makeresults`, `rest`, `metadata`).
- **Dataset-processing commands** need the whole set before emitting (`sort`, `dedup`).

**The rule:** filter early, transform late. Every event you exclude in the base search is
an event that never crosses the network. This is the seed of the performance reasoning
that the Architect exam tests properly.

### Topic 6: Searching and Filtering

The implied `search` command. Boolean operators (`AND`, `OR`, `NOT` — and the difference
between `NOT` and `!=`, which is a real trap when a field is absent). Comparison operators,
quoting rules, and case sensitivity — field *names* are case-sensitive, values usually are
not.

Wildcards and their cost: why a leading wildcard defeats the index and a trailing one does
not. Searching `_raw` versus searching a field, and why the latter is faster and more
precise.

`fields` to include or exclude, and why trimming the payload early is one of the cheapest
optimisations available.

### Topic 7: `eval` and Calculated Values

`eval` as the general-purpose computation command. Creating, overwriting and conditionally
assigning fields.

Function families introduced here, developed fully in
[SPL-02](spl-02-power-user.md):

- **Comparison and conditional:** `if()`, `case()`, `validate()`, `coalesce()`, `nullif()`
- **String:** `len()`, `lower()`, `upper()`, `substr()`, `replace()`, `trim()`, `split()`
- **Mathematical:** `round()`, `abs()`, `ceiling()`, `floor()`, `pow()`, `sqrt()`
- **Time:** `strftime()`, `strptime()`, `now()`, `relative_time()`
- **Informational:** `isnull()`, `isnotnull()`, `typeof()`, `like()`, `match()`

`where` versus `search`: `where` evaluates an expression and can compare two fields;
`search` matches terms. Learners reach for `search` when they need `where` constantly.

**The null problem.** A field that does not exist is not empty — it is absent, and most
comparisons against it are neither true nor false. `isnull()`, `coalesce()` and
`fillnull` are the tools; understanding *why* they are needed is the actual learning.

### Topic 8: Aggregation with `stats`

`stats` as the workhorse transforming command. Aggregate functions: `count`, `dc`
(distinct count), `sum`, `avg`, `min`, `max`, `median`, `stdev`, `values`, `list`,
`earliest`, `latest`, `range`, `perc<N>`.

The `by` clause and what it does to result cardinality. `count` versus `dc` — a
distinction that silently produces wrong answers when confused. `values` versus `list`
(deduplicated versus not, and the ordering guarantee).

Renaming with `as`, and multiple aggregations in one `stats`.

**Why `stats` is preferable to `transaction`** for almost every grouping problem: it is
faster, distributable, and has no event limit. `transaction` is introduced in
[SPL-02](spl-02-power-user.md) precisely so learners know when *not* to use it.

### Topic 9: Result Manipulation

- `sort` with `-`/`+`, multiple keys, and the default result limit that truncates silently.
- `dedup` — what it keeps, the `sortby` interaction, and why it is often a slower answer
  than `stats`.
- `head` and `tail`.
- `rename`, including wildcard renaming.
- `table` versus `fields` — presentation versus payload reduction, and why the difference
  matters for performance.
- `top` and `rare` as convenience wrappers over `stats`, including `limit`, `showperc`
  and `countfield`.
- `fillnull` and `eventstats` (previewed here, developed in SPL-02).

### Topic 10: Field Extraction at Search Time

The field extractor UI (regex and delimiter modes), and its limits.

`rex` for inline extraction with named capture groups, `sed` mode for masking, and the
`max_match` parameter. `erex` as the example-driven generator that writes a regex for you —
useful for learning, rarely good enough for production.

Extracting from structured data: `spath` for JSON and XML, and automatic key-value
extraction for `key=value` formats.

**The judgement to establish early:** an inline `rex` is a one-off; a persistent extraction
belongs in the knowledge layer ([SPL-02](spl-02-power-user.md)). Copy-pasting the same
`rex` into twenty searches is technical debt being created in real time.

### Topic 11: Reporting Commands and Visualisation

`chart` versus `timechart` versus `stats` — what each produces and when to reach for it.
The `over` and `by` clauses in `chart`, the `span` argument in `timechart`, and
`usenull`/`useother` and their effect on honesty in a chart.

Chart types and matching the visualisation to the question: time series, column, bar, pie
(and why pie is nearly always the wrong choice), scatter, single value, gauge.

`addtotals`, `eventstats` for adding an aggregate back onto rows, and `trendline`.

Formatting: `fieldformat`, and number/time display without corrupting the underlying value —
a distinction that matters when the formatted field is used downstream.

### Topic 12: Saved Searches, Reports, Alerts and Dashboards

Saved searches as the unit of reuse. Reports, scheduling, and the dashboard as a
collection of saved searches with a layout.

Alerts: scheduled versus real-time, trigger conditions, throttling, and alert actions.
Dashboards: panels, inputs and tokens, drilldown, and time-range binding.

Permissions and sharing scope (private / app / global) — a concept that becomes a real
operational problem in [SPL-02](spl-02-power-user.md)'s knowledge-object management and a
governance problem in SPL-06.

!!! warning "Free-licence gap"
    **Alerting is not available on the Splunk Free licence**, and there is no
    authentication, so sharing scope cannot be demonstrated meaningfully. Cover both
    conceptually here; they become hands-on in
    [SPL-06](spl-06-enterprise-admin.md) under a trial licence.

### Topic 13: Reading a Search — the Job Inspector

The job inspector as the primary feedback loop: execution costs, the number of events
scanned versus matched, which commands ran where, and how long each phase took.

Search job lifecycle and artefacts; dispatch directories; job quotas and why a search can
be queued rather than slow.

**This topic is why the module is not just syntax.** A learner who can read the job
inspector can improve their own searches without being told how; one who cannot will write
the same slow search for years. It is also the foundation of the troubleshooting method in
[SPL-07](spl-07-architect.md).

### Topic 14: Getting Results Out

Exporting results (CSV, JSON, XML, PDF) and the export limits that differ from display
limits.

An introduction to the REST API and `| rest` as a search-time way to interrogate the
platform about itself — used heavily from [SPL-04](spl-04-enterprise-security.md) onward
for content inventory.

Sharing a search versus sharing a link versus scheduling a report to a person: three
different answers with different governance implications.

---

### Topic 15: Creating and Using Lookups

Examined in the Core User blueprint at 6%, and the first point at which a learner enriches
data rather than just reading it.

What a lookup is and why it exists: attaching context Splunk does not have to data Splunk
does. A worked example file — the structure of a lookup CSV, and the matching field that
joins it to your events.

Creating a **lookup file**, defining a **lookup definition**, and configuring an
**automatic lookup** so the enrichment applies without anyone remembering to ask for it.
Using `lookup` explicitly in a search, and `inputlookup` to inspect the table itself.

The judgement to plant early: an automatic lookup is invisible enrichment applied to every
search touching that sourcetype. That is powerful and easy to over-apply — a theme
developed in [SPL-02](spl-02-power-user.md) Topic 5.

---

## Labs & exercises

!!! tip "Lab guide: how to actually run these"
    **[SPL-01 lab guide](../../../labs/guides/spl-01.md)** gives the setup, the commands and the
    verification for every lab below — against the
    **[lab environment](../../../labs/README.md)**, a reproducible synthetic estate of
    ~130k labelled events with ground truth, so you can measure a real positive
    predictive value rather than estimate one.

    The split of responsibility: **this page says why each lab exists and what to
    deliver; the guide says how to run it.** Marking criteria stay here.

    All seven labs run on Splunk Free with the lab dataset.

    Self-assess with the **[52-question quiz](quiz.md)**.

All labs run on a **Splunk Enterprise Free** instance. See the
[series safety rules](index.md#safety-authorisation-and-data-handling) before starting —
in particular, a Free instance has **no authentication**, so bind it to localhost or an
isolated lab network and never onboard real personal data.

### Lab 1: Stand Up Splunk and Onboard Data

Install Splunk Enterprise with the Free licence. Add a file-based input of sample log
data. Inspect what Splunk assigned for `host`, `source`, `sourcetype` and `_time`.

**Deliberately break it:** onboard a file with an ambiguous timestamp format and observe
the wrong `_time`. Fix the sourcetype and re-index. The learner must be able to explain
why the fix required re-indexing while a field-extraction fix would not have.

**Deliverable:** a short note stating which fields were fixed at index time and which
could be changed later, with evidence.

### Lab 2: The Cost of Pipeline Order

Take one investigative question. Write it three ways: filter late, filter early, and
filter early with `fields` trimming. Record the job inspector's event counts and run
durations for each.

**Deliverable:** a table of the three variants with timings, and a paragraph explaining
the difference in terms of what ran on the indexer versus the search head.

### Lab 3: Answer an Investigative Question

Given a sample authentication log, determine: which accounts failed to authenticate most
often, from which hosts, and whether any of them subsequently succeeded.

This is a deliberately under-specified question — the learner must decide what "subsequently"
means and defend the time window chosen.

**Deliverable:** the SPL, the answer, and a statement of the assumptions made.

### Lab 4: A Dashboard That Answers a Question

Build a three-panel dashboard from saved searches. Each panel must answer a stated
question; a panel that exists because it looked good is marked down.

**Deliverable:** the dashboard, plus one sentence per panel naming the question it answers.

---

### Lab 5: Drill the Command Set

Given one dataset and fifteen questions, answer each with SPL. The questions are chosen so
that the obvious command is sometimes the wrong one — at least one requires `where` rather
than `search`, one requires `dc` rather than `count`, one requires handling a field that is
absent rather than empty, and one requires `cidrmatch` rather than a string comparison.

**Deliverable:** the fifteen searches, plus a short note on the three you initially got
wrong and why. The wrong answers are the assessed part.

### Lab 6: Read the Job Inspector

Take one search. Run it four ways: fast mode, verbose mode, with a wide time range, and
with a narrow one. Record the job inspector's execution costs for each.

Then find a search in your own history that is slower than it should be and improve it
using only what the inspector told you.

**Deliverable:** the four-way comparison table, and a before/after for the improved search
with the specific inspector metric that pointed at the fix.

---

### Lab 7: Enrich With a Lookup

Build a lookup that maps a technical identifier in your dataset (host, IP or account) to
business context (owner, department, criticality). Create the definition, configure it as
an automatic lookup, and confirm the enriched fields appear without being asked for.

Then answer a question that is **only** answerable with the enrichment — one where the raw
events alone give a technically correct but useless answer.

**Deliverable:** the lookup, the definition, the before/after searches, and one sentence
on what would happen to every search using this sourcetype if the lookup file were
deleted.

---

## Assessment

### Formative: Predict the Cost

Given five SPL searches, rank them by expected cost before running them, then run them and
compare against the job inspector. The learning is in the mismatches.

### Summative: Investigation Report

Given a sample dataset and a scenario prompt, produce a short investigation report: the
question, the searches used, the findings, and — required for full marks — **an explicit
statement of what the data could not tell you**. Confident over-reach on incomplete data
is the failure mode this assessment is designed to catch, and it is the same failure mode
that matters in [OC04](../../../core/units/OC04-incident-response-lifecycle.md).

---

## Australian context

Log retention is a design decision with legal consequences, and it starts at this rung
because retention is set per index (SPL-06) but the *requirement* is set by law.

- The **Privacy Act 1988 (Cth)** and the Australian Privacy Principles govern personal
  information in logs. APP 11.2 requires destruction or de-identification once information
  is no longer needed — which sits in direct tension with "keep everything forever for
  security". Logs routinely contain personal information: usernames, IP addresses, device
  identifiers.
- The **Notifiable Data Breaches** scheme is why an unauthenticated Splunk instance
  holding real data is a reportable problem, not just an untidy one.
- The **ASD Essential Eight** and the **Information Security Manual** set monitoring and
  event-logging expectations that a Splunk deployment is often bought to satisfy;
  the ISM's event-logging guidance is the usual source of an Australian
  organisation's retention baseline.
- The **Security of Critical Infrastructure Act 2018 (Cth)** imposes obligations on
  responsible entities that shape monitoring scope in the sectors most likely to be
  running Splunk at scale.

These are treated properly in [F05](../../../core/units/F05-legal-ethics-compliance.md)
and the SC units (notably [SC03 — Governance, Policy & Compliance](../../../core/units/SC03-governance-policy-compliance.md)); the point here is that a
learner should never treat an index retention setting as a purely technical choice.

---

## Verification status

- **Verified 2026-09-09:** all exam facts in the table above, against the linked official page.
- **Not verified:** the exam code (`SPLK-xxxx`) is not published on the certification-track
  page and is deliberately not stated. Topic coverage **has now been reconciled against the published test blueprint** — see
  [Blueprint alignment](#blueprint-alignment). Sub-objective wording is not reproduced;
  the mapping uses domain titles and weightings only.
- Framework mappings and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [Splunk Core Certified User track](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-user.html) — official exam page and test blueprint link.
- [Splunk free courses](https://www.splunk.com/en_us/training/free-courses.html) — *Intro to Splunk*, *Using Fields*, *Search Under the Hood*, *Intro to Dashboards* cover most of this module.
- [Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference) — the authoritative SPL command reference.
- [About Splunk Free](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configure-splunk-licenses/about-splunk-free) — licence limits.
- [Splunk Search Manual — how search works](https://docs.splunk.com/Documentation/Splunk/latest/Search/Aboutthesearchapp) — the execution model behind Topic 3.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-01 |
| Module Title | Search Fundamentals — Splunk Core Certified User |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 2–3 (Understand / Apply) |
| Notional Hours | ~53 |
| Zero-cost achievable | Yes (excluding the optional exam fee) |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
