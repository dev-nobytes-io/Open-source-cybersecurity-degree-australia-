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
| A — How Splunk sees data | 1–2 | 1 | 6 |
| B — Searching | 3–5 | 2, 3 | 12 |
| C — Reporting | 6–7 | 4 | 7 |
| | | | **~25 hours** |

---

## Topics

### Topic 1: What Splunk Actually Is

A distributed search engine over time-series text, not a database. The consequences of
that sentence: no schema declaration, no joins in the relational sense, no update-in-place,
and a cost model driven by how many events must be read off disk and shipped to a search
head.

Introduce the three roles a single-instance install collapses together — **forwarder,
indexer, search head** — because SPL-04 and SPL-05 pull them apart, and a learner who
never knew they were separate will struggle there.

### Topic 2: The Data Pipeline and Search-Time Schema

Input → parsing → indexing → search. What happens at each stage, and critically **which
fields exist when**.

- **Index time:** `host`, `source`, `sourcetype`, `_time`, `index`. Fixed at ingest.
  Getting these wrong is expensive to fix — it means re-indexing.
- **Search time:** everything else. Extracted on the fly, every time, per search.

The trade-off is the platform's central design decision: flexibility at ingest, cost at
search. Learners should be able to state which of the two is cheap to change and why
this makes `sourcetype` decisions strategically important — a theme that returns in
SPL-04 and dominates SPL-06.

### Topic 3: The Search Pipeline

SPL as a pipeline of commands joined by `|`. The distinction that matters most:

- **Streaming commands** operate per event and can run distributed on the indexers.
- **Transforming commands** (`stats`, `chart`, `timechart`, `top`) reshape the result set
  and run on the search head.

**The rule:** filter early, transform late. Every event you exclude in the base search is
an event that never crosses the network. This is the seed of the performance reasoning
that the Architect exam tests properly.

### Topic 4: Time

Time is the axis Splunk is built on and the most common source of wrong answers.

- `_time` (event time, parsed from the event) vs `_indextime` (when Splunk saw it).
- Time-zone handling, and why a misconfigured forwarder produces events "in the future".
- Why a narrow time range is the single cheapest optimisation available.
- Real-time searches, and why they are usually the wrong tool.

An investigation that uses index time when it needed event time — or vice versa — reaches
a confidently wrong conclusion. Practise both.

### Topic 5: Fields, Filtering and `eval`

Automatic vs interesting fields; the fields sidebar; `fields` to reduce payload. Comparison
and boolean logic, wildcards and their cost. `eval` for computed values, `where` versus
`search`, and the `if`/`case` constructs learners will use constantly from SPL-02 onward.

### Topic 6: Aggregation and Reporting

`stats` and its aggregate functions; `by` clauses; `dedup`, `sort`, `head`. `top` and
`rare` as convenience wrappers over `stats`. `timechart` versus `chart` versus `stats`,
and choosing between them deliberately rather than by habit.

### Topic 7: Saving Work — Reports, Alerts and Dashboards

Saved searches as the unit of reuse. Reports, and the dashboard as a collection of saved
searches with a layout. Permissions and sharing scope (private / app / global) — a
concept that becomes a real operational problem in SPL-02's knowledge-object management
and a governance problem in SPL-04.

!!! warning "Free-licence gap"
    **Alerting is not available on the Splunk Free licence**, and there is no
    authentication, so sharing scope cannot be demonstrated meaningfully. Cover both
    conceptually here; they become hands-on in [SPL-04](spl-04-enterprise-admin.md) under
    a trial licence.

---

## Labs & exercises

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
because retention is set per index (SPL-04) but the *requirement* is set by law.

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
  page and is deliberately not stated. Topic coverage is the module author's reading of the
  platform and has **not** been reconciled against Splunk's published test blueprint.
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
| Notional Hours | ~25 |
| Zero-cost achievable | Yes (excluding the optional exam fee) |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
