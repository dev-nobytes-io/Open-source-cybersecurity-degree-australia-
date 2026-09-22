# ELK-04: Detection Rules, EQL and the Security App

> **Module type:** Extension module (vendor-specific elective) — part of [EXT-ELK](index.md)
> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-09-13
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

!!! warning "Not a credit-bearing unit"
    See the [series index](index.md). ELK-04 carries no credit points and does not feed
    [`docs/ksat-coverage.md`](../../ksat-coverage.md). Product behaviour is cited to
    Elastic's documentation as read on 2026-09-13; the
    [verification table](#verification-status) records what to re-check — including one
    subscription-tier question the documentation answers two ways.

---

## Overview

[DE03](../../../degrees/operational/detection-engineering/DE03-writing-detection-logic.md)
teaches detection logic in Sigma, SPL and KQL;
[DE05](../../../degrees/operational/detection-engineering/DE05-detection-operations-management.md)
teaches running a detection programme. This module is where both land on the Elastic
Security app: the **seven rule types** the detection engine runs, what each is for and
what each costs; **EQL**, the language whose `sequence` is the reason the platform can
express "this, then that, on the same host, within five minutes"; the **prebuilt rules**
Elastic ships — hundreds, "disabled by default", tagged to MITRE ATT&CK — and the
licence position of using, tuning and editing them; **exceptions**, which suppress alerts
"without requiring changes to the underlying detection rules"; the **alert** document a
rule writes (`event.kind: signal`, the `kibana.alert.*` fields) and its lifecycle; and
**cases**, where alerts become an investigation.

The lab dataset supplies the targets: the password spray, the impossible travel, the
`certutil` download, the lateral movement, the DGA beacon, the exfiltration and the
insider — each with ground truth held out, so the learner can measure a rule's precision
rather than admire its logic. ELK-02's ECS crosswalk is what makes the rules writable at
all: every field a rule names is one the pipeline produced.

It does **not** teach detection theory, Sigma, or the rule-writing craft — those are
DE01/DE03 — nor detection operations (DE05), nor Splunk's equivalents (SPL-03, SPL-09).
Primary sources: Elastic's *Create a detection rule*, *EQL*, *Install and manage
prebuilt rules*, *Rule exceptions*, *View alert details* and *Cases* documentation, and
the `elastic/detection-rules` repository.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [ELK-02](elk-02-ingest-pipelines-ecs-data-streams.md) | **Predecessor.** The ECS fields rules name; `event.kind: alert` (the IDS) vs `signal` (rules). |
| [DE03 — Writing Detection Logic](../../../degrees/operational/detection-engineering/DE03-writing-detection-logic.md) | **Prerequisite.** Sigma, KQL and translation; ELK-04 is where the KQL side of DE03 Topic 3 runs. |
| [DE01 — Detection Theory & Philosophy](../../../degrees/operational/detection-engineering/DE01-detection-theory-philosophy.md) | Durability, coverage and ATT&CK — the reasoning behind Topic 6. |
| [DE05 — Detection Operations Management](../../../degrees/operational/detection-engineering/DE05-detection-operations-management.md) | Tuning, metrics and lifecycle; exceptions (Topic 5) are its main tool on this platform. |
| [DE04 — Adversary Simulation & Detection](../../../degrees/operational/detection-engineering/DE04-adversary-simulation-detection.md) | Verifying that rules fire — Lab 3 measures precision with ground truth instead. |
| [OC04 — Incident Response Lifecycle](../../../core/units/OC04-incident-response-lifecycle.md) | Where a case goes after Topic 8. |
| [EXT-SPL SPL-03](../splunk/spl-03-cyber-defense-analyst.md), [SPL-09](../splunk/spl-09-detection-analytics.md) | The same scenarios detected on the other platform; compare precision. |
| [ELK-05](elk-05-opensearch-alternative-and-migration.md) | The OpenSearch counterpart: Sigma-based detectors and findings. |

---

## Prerequisites

- [ELK-02](elk-02-ingest-pipelines-ecs-data-streams.md) Lab 2 complete (ECS-shaped streams)
- [DE03 — Writing Detection Logic](../../../degrees/operational/detection-engineering/DE03-writing-detection-logic.md) (hard)
- [DE01](../../../degrees/operational/detection-engineering/DE01-detection-theory-philosophy.md) (recommended)

---

## Learning outcomes

On completion, a learner can:

1. **Differentiate** the seven detection rule types by what each can and cannot express,
   and **select** the type for a stated behaviour.
2. **Construct** EQL queries and sequences over ECS-shaped events, including `by`,
   `maxspan` and `until`, and **explain** why a sequence needs `event.category`.
3. **Implement** custom rules for the lab dataset's scenarios, **measure** their precision
   against ground truth, and **tune** them with exceptions rather than edits.
4. **Evaluate** the prebuilt rule set for a stated estate — coverage by ATT&CK tag,
   applicability by data source, licence position for editing — and **justify** an
   enablement plan.
5. **Analyse** the alert document and its lifecycle, and **relate** rule severity and
   risk score to triage order.
6. **Assess** a rule as code under version control, with tests, and **recommend** a
   promotion process from repository to the running engine.

> Bloom's 3–5; see [`docs/content-standards.md`](../../content-standards.md).

---

## AQF Level 7 Alignment

Applies a formal query language to labelled data, measures outcomes quantitatively, and
requires judgement about coverage, tuning and licence constraints — the application,
analysis and evaluation descriptors at Level 7.

> Notional; ELK-04 is not credit-bearing and has not been assessed through
> [`docs/compliance/aqf-teqsa.md`](../../compliance/aqf-teqsa.md).

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0166 | (paraphrase) Perform event correlation to detect intrusions | Lab 2, Lab 3 |
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0258 | (paraphrase) Provide timely detection and characterisation of anomalous activity | Lab 3 |
| 2023 | Cyber Defense Infrastructure Support | PR-INF-001 | T0335 | (paraphrase) Build and maintain detection content on monitoring infrastructure | Lab 2, Summative |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Information security | SCTY | Level 4 | Labs 2–3, Summative |
| Methods and tools | METL | Level 4 | Lab 2 |
| Data management | DATM | Level 4 | Topic 7 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Defensive Operations | Threat Detection | Practitioner–Advanced | Labs 2–3, Summative |
| Defensive Operations | Incident Response | Practitioner | Topic 8, Lab 3 |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | ELK-04-K01 | Knowledge of the seven detection rule types and what each expresses | Topic 1; Lab 1 |
| Knowledge | ELK-04-K02 | Knowledge of EQL syntax, sequences, and the `@timestamp`/`event.category` requirement | Topic 2; Lab 2 |
| Knowledge | ELK-04-K03 | Knowledge of prebuilt rules: installation, enablement, tagging, update behaviour and licence position | Topic 4; Lab 1 |
| Knowledge | ELK-04-K04 | Knowledge of exceptions and shared exception lists as the tuning mechanism | Topic 5; Lab 3 |
| Knowledge | ELK-04-K05 | Knowledge of the alert document, its fields and workflow states, and of cases | Topics 7–8 |
| Skill | ELK-04-S01 | Skill in writing and scheduling custom rules, including EQL sequences, over ECS data | Lab 2 |
| Skill | ELK-04-S02 | Skill in measuring rule precision against labelled ground truth | Lab 3 |
| Skill | ELK-04-S03 | Skill in managing rules as versioned TOML with tests | Topic 9; Summative |
| Ability | ELK-04-A01 | Ability to choose the rule type for a behaviour and defend it | Lab 1; Summative |
| Ability | ELK-04-A02 | Ability to tune with exceptions without degrading the rule | Lab 3 |
| Ability | ELK-04-A03 | Ability to plan prebuilt-rule enablement by coverage and applicability, stating licence constraints | Lab 1; Summative |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — Rule types and EQL | 1–3 | 2 | 6 |
| B — Prebuilt rules and exceptions | 4–5 | 1, 3 | 6 |
| C — Coverage, alerts, cases | 6–8 | 3 | 6 |
| D — Rules as code | 9 | — | 4 |
| | | | **~22 hours** |

---

## Topics

### Topic 1: The Seven Rule Types

The detection engine runs a rule on a **schedule** — an interval plus a look-back window
that overlaps the previous run — and writes an alert for each match. The rule *type*
decides what "match" can mean:

| Type | What it expresses | Typical use | Note |
|---|---|---|---|
| **Custom query** | A KQL or Lucene query; every hit is an alert | Single-event indicators: a known-bad process name, a disabled account logging on | The DE03 KQL path; cheapest to run |
| **Threshold** | A query whose hits, grouped by a field, exceed a count in the window | Password spray: many failures per source; scanning: many destinations per host | The count is the detection, not the event |
| **Event correlation (EQL)** | An EQL query, including **sequences** of events | Parent–child process chains; download-then-execute; logon-then-lateral | Topic 2 |
| **Indicator match** | Events whose field values match an indicator index | Threat-intelligence IPs, hashes, domains against traffic | Needs an indicator source (OC05, CT03) |
| **New terms** | A field value seen for the first time in a history window | First sign-in from a new country per user; new process on a host | Baseline-shaped, without statistics |
| **ES\|QL** | An ES\|QL query, including aggregations, as a rule | Ratios and statistics the others cannot compute | The newest type; check its version availability |
| **Machine learning** | An anomaly-detection job's results above a score | Rare process, unusual bytes | **Paid tier** (Platinum per the subscriptions page) |

The choice is a design decision with a cost: a threshold rule that could have been a
custom query with a `sequence` wastes engine time; an EQL sequence that could have been a
threshold is fragile to event ordering. Lab 1 makes the learner choose per scenario before
writing anything.

### Topic 2: EQL — Categories, Sequences and the Fields They Need

EQL queries "event-based time series data" and "excels at expressing relationships
between events across different categories and timeframes". The basic form is
`[event_category] where [condition]`:

```
process where process.name == "certutil.exe" and process.command_line : "*-urlcache*"
```

The distinguishing form is the **sequence** — ordered events, joined `by` shared field
values, bounded `with maxspan`, optionally terminated by `until`, with `!` matching a
*missing* event:

```
sequence by host.name with maxspan=2m
  [process where process.name == "certutil.exe"]
  [process where process.parent.name == "certutil.exe" and process.name == "rundll32.exe"]
```

Both forms require `@timestamp` and `event.category` on every document "unless using the
`any` keyword" — which is why ELK-02's categorisation was not optional. The lab's
`lolbin_download` scenario is exactly this sequence; `lateral_movement` is an
authentication event followed by a remote-execution process on the *reached* host, which
needs `by` on a field both events carry — a design question the learner meets in Lab 2.

### Topic 3: Scheduling, Look-Back and the Cost of Rules

Every rule runs on an interval and searches a window that reaches back further than the
interval, so late-arriving events are not missed; the price is duplicate consideration of
the overlap, which the engine de-duplicates per rule. Three engineering consequences:

- **Ingest latency bounds detection latency.** A rule cannot alert on an event that has
  not arrived; SA-05's timeliness expectation and ELK-01's collection health are upstream
  of every rule.
- **Sequences are bounded by `maxspan`, not by the schedule.** A sequence whose events
  straddle two runs still matches if within `maxspan` and the look-back.
- **Rules consume the cluster.** Dozens of EQL sequences over large streams on a short
  interval are a capacity input to ELK-03's model, not an afterthought.

### Topic 4: Prebuilt Rules — What Elastic Ships, and What You May Do With It

Elastic provides "hundreds of prebuilt detection rules that cover common attack
techniques across multiple platforms", installed from the Security app, "disabled by
default", and enabled individually or in bulk. They are tagged by MITRE ATT&CK tactic and
technique, operating system, data source, severity and rule type (including "building
block" rules that feed others). Their source is the `elastic/detection-rules` repository —
TOML files with a Python CLI, unit tests and schema validation — "licensed under the
Elastic License v2" and "designed to be used in the context of the Detection Engine".

The licence position, as the documentation reads on 2026-09-13:

| Action | Tier |
|---|---|
| Install, enable, add exceptions | "available across all subscription levels" per the prebuilt-rules page |
| Edit a prebuilt rule directly; review field-level update changes; resolve update conflicts; revert to Elastic's version | Enterprise and Serverless Complete |
| Duplicate a prebuilt rule and customise the copy | All tiers (the documented path for other tiers) |
| Machine-learning rules | Paid (Platinum per the subscriptions page) |

!!! warning "Two pages, two readings"
    The subscriptions comparison as summarised on the same day placed the "SIEM detection
    engine (prebuilt rules)" under Platinum; the prebuilt-rules documentation states core
    capabilities are available at all levels. This module follows the more specific
    page, and the [verification table](#verification-status) carries the item until a
    reviewer confirms against the live subscriptions page. Every lab here uses **custom**
    rules, so the answer does not change what a learner can do.

Enablement is a design task, not a click: a rule for a data source you do not collect
fires never and costs engine time; a rule for a technique your threat model does not
prioritise fires and costs analyst time. Lab 1 plans it by ATT&CK coverage (DE01 Topic 5)
crossed with the SA-05 source register.

### Topic 5: Exceptions — Tuning Without Editing

An exception holds "source event conditions that determine when alerts shouldn't be
generated". Exceptions for a single rule live on that rule; **shared exception lists**
"group exceptions together and then associate them with multiple rules"; **value lists**
"allow you to match an exception against a list of possible values". The point is
operational: tuning becomes data, not code. The rule stays as shipped or as reviewed;
the organisation's known-good — the vulnerability scanner, the backup service account,
the jump host — is expressed once and applied to every rule it affects, and survives a
prebuilt-rule update, which "preserve[s] exceptions and tuning".

DE05's tuning discipline applies: every exception has an owner, a reason and a review
date, or it is a permanent blind spot nobody remembers creating.

### Topic 6: Coverage — Rules Against ATT&CK and Against Your Sources

Two matrices, and the design lives in their intersection:

| Matrix | Axis | Question |
|---|---|---|
| Technique coverage | ATT&CK technique × enabled rules | Which prioritised techniques (OC05's PIRs, DE01 Topic 5) have no rule? |
| Source applicability | Rule's data source × collected streams (ELK-01) | Which enabled rules can never fire because the source is absent? |

The Security app can render the first from rule tags; the second is the learner's
spreadsheet against the SA-05 register. Lab 1 produces both; the honest output is usually
a short list of rules to enable and a longer list of sources to onboard.

### Topic 7: The Alert Document and Its Lifecycle

A rule writes an alert document with `event.kind: signal` — ECS reserves the value for
"alert documents that are created by rules executing within the Kibana alerting
framework" — carrying the rule's identity and settings in `kibana.alert.*` fields:
`kibana.alert.rule.name`, `kibana.alert.severity` and `kibana.alert.risk_score`
(inherited from the rule), `kibana.alert.workflow_status` (the analyst's state), and an
"alert reason" that "describes the source event that generated the alert". Alerts sit in
their own index, separate from the source streams, so a search over `logs-*` never
returns them and a search over alerts never returns raw events.

Severity and risk score are rule *attributes*, set by the author: a triage queue sorted
by them is sorted by the author's judgement, not by evidence. SPL-09's argument about
calibrating risk scores applies here unchanged, and the lab's held-out ground truth is
what lets a learner check whether high severity actually means high precision.

### Topic 8: Cases — Where an Alert Becomes an Investigation

A case lets a team "collect and share information about security incidents and
investigations": alerts (with closing reasons), events, indicators, timelines, entities,
comments and files attach to it; metrics track alerts, hosts and users, and time open, in
progress and to closure; and cases integrate with "external ticketing systems like Jira,
ServiceNow, and IBM Resilient". Rules can create cases automatically. Whether an
organisation's external connector needs a paid tier is not stated on the cases page and
is left for the verification table.

The architectural point for this series: the case is the hand-off from ELK-04 to OC04 —
the record an incident responder inherits. A case with no closing reason on its alerts is
a detection-operations gap (DE05), and a case whose timeline cannot be exported is an
evidence-handling gap (OC04 Topic 4).

### Topic 9: Rules Are Code

Elastic's own rules are TOML in a repository with tests; yours should be too. The
`detection-rules` tooling and the Kibana rule import/export API make it possible to keep
rules in version control, validate them against the schema, run unit tests, and promote
them to the engine by pipeline rather than by hand. The pattern, and where each piece
lives:

| Step | Artefact | Where taught |
|---|---|---|
| Author | TOML rule with ATT&CK tags and a false-positive note | DE03, this module |
| Test | Sample events that must and must not match; precision against ground truth | Lab 3 |
| Review | Pull request; DE05's acceptance criteria | DE05 |
| Promote | Import to the engine; enable; record the version | This module, Summative |
| Tune | Exceptions as data, reviewed | Topic 5 |

---

## Labs & exercises

### Lab 1 📄: Choose the Type, Plan the Enablement

**Objective:** For each lab scenario, choose the rule type and justify it; then plan a
prebuilt-rule enablement for the SA-05 estate by coverage and applicability.

**Prerequisites:** Topics 1, 4, 6; `labs/docs/data-model.md` scenarios; the SA-05 register.

**Environment:** No tooling required.

**Instructions:**
1. For the eight scenarios (`password_spray`, `impossible_travel`, `lolbin_download`,
   `lateral_movement`, `dga_c2`, `beacon_c2`, `exfil_volume`, `insider_collection`),
   choose a rule type, state the fields it needs (from the ELK-02 crosswalk), and give the
   reason another type would be worse.
2. Take twenty prebuilt rule titles with their tags (from the Security app or the
   repository) and mark each: applicable to a collected source or not; covers a
   prioritised technique or not; editable on your tier or duplicate-and-edit.
3. Produce the technique-coverage and source-applicability matrices for the twenty, and a
   ten-line enablement plan with the sources that would need onboarding first.

**Expected output:** The type-selection table with reasons; the two matrices; the plan.
Marked on the quality of the reasons, not on agreement with a key.

**Reflection questions:**
1. Which scenario tempted you toward an ML rule, and what would it cost to find out whether ML was needed?
2. How many of the twenty prebuilt rules would fire on the estate as it is collected today?

### Lab 2 ✅: Write the Rules

**Objective:** Implement custom rules for at least four scenarios — one custom query, one
threshold, one EQL sequence, one new-terms — on the ECS-shaped lab streams, and see them
fire.

**Prerequisites:** ELK-02 Lab 2; Topics 1–3.

**Environment:** `labs/docker/compose.elastic.yml` (Basic); the Security app.

**Instructions:**
1. Custom query: the `certutil` download as a single-event rule on `process.command_line`.
2. Threshold: the password spray as failed authentications grouped by `source.ip` over
   the window, with the threshold set from the benign baseline (SPL-09 Lab 2's arithmetic
   applies).
3. EQL sequence: `certutil` then `rundll32` by `host.name` within `maxspan=2m`; then the
   lateral-movement sequence — decide the `by` field and explain the choice.
4. New terms: first sign-in per `user.name` from a new `source.geo.country_iso_code`
   (or the crosswalked equivalent) with a history window that predates the scenario.
5. Schedule each with an interval and look-back you justify from the dataset's timestamp
   spread; run them; confirm alerts appear with `event.kind: signal` and the expected
   `kibana.alert.rule.name`.

**Expected output:** The four rule definitions (exported), their schedules with
reasoning, and alert evidence.

**Reflection questions:**
1. Your threshold fired on the spray. What else did it fire on, and why?
2. Which `by` field made the lateral-movement sequence work, and what would break it?

### Lab 3 ✅: Measure, Tune, Case

**Objective:** Measure each Lab 2 rule's precision against ground truth, tune with
exceptions rather than edits, and turn one alert set into a case.

**Prerequisites:** Lab 2; Topics 5, 7, 8; `labs/data/truth/ground_truth.csv` (instructor
data — see `labs/docs/ground-truth.md`).

**Environment:** As Lab 2; a small Python script over the exported alerts and the truth file.

**Instructions:**
1. Export the alerts. Join them to ground truth on the source event (host, user, time
   window). Compute precision per rule and the false-positive count.
2. For the noisiest rule, write a shared exception list that removes the false positives
   by their actual cause (a service account, a scanner host, a benign process path) —
   not by excluding the true positives' neighbours. Re-run; re-measure.
3. Record, for each exception: owner, reason, review date.
4. Create a case from the beacon alerts; attach the DNS and firewall events that
   corroborate them (ELK-02's crosswalk makes the join possible); set a closing reason on
   one alert.
5. Compare the precision of your rules with the same scenarios' detections in SPL-03 and
   SPL-09, if you have done them.

**Expected output:** The precision table before and after tuning; the exception list
with metadata; the case with corroborating events.

**Reflection questions:**
1. Which exception would you refuse to write, because it would hide the attack it was tuned against?
2. Severity said one thing; measured precision said another. Which does the triage queue follow, and who decides?

---

## Assessment

### Formative 1: Which Type?

Twelve one-line behaviours; name the rule type and the two ECS fields it needs. Maps to
LO1, LO2.

### Formative 2: Read the Alert

An alert document; identify the rule, its severity and score, the workflow status, the
source event, and one reason it might be a false positive. Maps to LO5.

### Summative: The Detection Pack

For the lab dataset: (1) type selection and enablement plan with matrices (Lab 1); (2)
four custom rules as versioned TOML with test events (Lab 2, Topic 9); (3) precision
measurement before and after tuning, with the exception list and its metadata (Lab 3);
(4) a promotion process from repository to engine, stating the licence constraints on
prebuilt-rule editing. Maps to LO1–LO6.

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Type selection and enablement | Every choice reasoned; matrices complete; plan sequenced by source onboarding | Choices reasoned; matrices present | Choices without reasons | Absent |
| Rules as code | TOML with tags, notes and test events; all fire | Rules fire; partial tests | Some rules fire | None fire |
| Measurement and tuning | Precision measured before/after; exceptions target causes; metadata complete | Measured; exceptions present | Measured only | No measurement |
| Promotion process | Repository-to-engine with review, versioning and licence constraints | Process described | Sketch | Absent |

| Assessment task | Learning outcomes addressed |
|---|---|
| Formative 1 | LO1, LO2 |
| Formative 2 | LO5 |
| Summative | LO1, LO2, LO3, LO4, LO5, LO6 |

---

## Australian context

ASD's *Best practices for event logging and threat detection* frames detection as
something that follows from what is collected and how quickly it is ingested; Topic 3's
point that ingest latency bounds detection latency is the operational form of that, and
the source-applicability matrix of Topic 6 is how an Australian organisation avoids
enabling prebuilt rules for telemetry it does not hold. Where the collected data
includes personal information, exceptions and cases are both places that information
recurs: an exception list naming individuals, or a case that attaches their events, is
itself a record subject to the Privacy Act 1988 (Cth), and the retention of the alert and
case indices belongs in SA-05 Lab 2's register alongside the source streams.

For responsible entities under the Security of Critical Infrastructure Act 2018 (Cth),
the case is also the starting point of any mandatory notification clock (DF05 Topic 3):
a case whose creation time, alerts and closing reasons are recorded is evidence of when
the entity *knew*. Design the case workflow with that in mind before the first incident,
not during it.

---

## Verification status

| Item | Status | Action required |
|---|---|---|
| The seven rule types | Verified 2026-09-13 against *Create a detection rule* | Re-verify per release (ES\|QL rules are recent) |
| EQL syntax, sequence keywords, required fields | Verified 2026-09-13 against the EQL reference | Re-verify |
| Prebuilt rules: disabled by default; tags; editing/update behaviour by tier; "available across all subscription levels" for install/enable/exceptions | Verified 2026-09-13 against the prebuilt-rules page | **Reconcile with the subscriptions page**, which as summarised places prebuilt rules under Platinum |
| `elastic/detection-rules`: TOML, tests, Elastic License v2 | Verified 2026-09-13 against the repository README | — |
| Exceptions, shared lists, value lists | Verified 2026-09-13 | — |
| Alert fields (`kibana.alert.rule.name`, `severity`, `risk_score`, `workflow_status`, alert reason) | Verified 2026-09-13 against *View alert details* | Alert index name pattern **not read** — author's knowledge; confirm |
| Rule schedule interval and look-back behaviour, de-duplication | **Author's knowledge** | Verify against the rule-schedule documentation |
| Cases: attachments, metrics, external systems, rule-created cases | Verified 2026-09-13 | Connector tier requirement **not stated** on the page — confirm |
| ML rules as a paid tier | Per the subscriptions page as summarised | Confirm |
| NICE T-codes (paraphrased), SFIA levels, ASD CSF sub-domains, KSAT IDs | Provisional | Framework Custodian |

---

## Further reading

**Elastic (2026).** *Create a detection rule.* https://www.elastic.co/docs/solutions/security/detect-and-alert/create-detection-rule
> Relevance: the seven rule types and their settings — Topic 1 and Lab 2.

**Elastic (2026).** *Event Query Language (EQL).* https://www.elastic.co/docs/reference/query-languages/eql
> Relevance: sequences and their required fields — Topic 2.

**Elastic (2026).** *Install and manage Elastic prebuilt rules.* https://www.elastic.co/docs/solutions/security/detect-and-alert/install-manage-elastic-prebuilt-rules
> Relevance: what ships, how it updates, and what each tier may do — Topic 4.

**Elastic (2026).** *Rule exceptions.* https://www.elastic.co/docs/solutions/security/detect-and-alert/rule-exceptions
> Relevance: tuning as data — Topic 5 and Lab 3.

**Elastic (2026).** *Cases.* https://www.elastic.co/docs/solutions/security/investigate/cases
> Relevance: the investigation record and the hand-off to incident response — Topic 8.

**Elastic (2026).** *elastic/detection-rules* (GitHub). https://github.com/elastic/detection-rules
> Relevance: rules as code, the CLI and tests — Topic 9; licence Elastic License v2.

**ASD (2024).** *Best practices for event logging and threat detection.* https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-monitoring/best-practices-event-logging-threat-detection
> Relevance: detection as a consequence of collection and timeliness — the Australian context section.

**Open-source degree (2026).** *EXT-SPL SPL-09 — Detection Analytics, Risk Scoring & the Mathematics Behind Them.* [spl-09-detection-analytics.md](../splunk/spl-09-detection-analytics.md)
> Relevance: the precision and calibration arguments Lab 3 applies to Elastic alerts.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | ELK-04 |
| Module Title | Detection Rules, EQL and the Security App |
| Module Type | Extension module (vendor-specific elective; **not** credit-bearing) |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 0 CP — outside the 160 CP degree structure |
| Notional Hours | ~22 |
| Extends | ELK-02; DE03; DE05 |
| Related Units | DE01, DE04, OC04, OC05, EXT-SPL SPL-03 and SPL-09 |
| Prerequisites | ELK-02 Lab 2; DE03; DE01 recommended |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-09-13 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 3–5 (Apply, Analyse, Evaluate) |
| Australian Legislation Referenced | Privacy Act 1988 (Cth); Security of Critical Infrastructure Act 2018 (Cth) |
| Tooling Licence Position | Self-managed Elastic Basic (free) with custom rules; ML rules and direct prebuilt-rule editing named as paid, never required |
| Licence | CC BY 4.0 |
