# SPL-04: Platform Administration — Splunk Enterprise Certified Admin

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
| Certification | [Splunk Enterprise Certified Admin](https://www.splunk.com/en_us/training/certification-track/splunk-enterprise-certified-admin.html) | 2026-09-09 |
| Level | Administrator (professional) | 2026-09-09 |
| Prerequisite certification | **Splunk Core Certified Power User** — enforced | 2026-09-09 |
| Prerequisite coursework | **None published** | 2026-09-09 |
| Length | 60 minutes | 2026-09-09 |
| Format | 56 multiple choice questions | 2026-09-09 |
| Price | US$130 per attempt | 2026-09-09 |
| Delivery | Pearson VUE | 2026-09-09 |

**Zero-cost achievable: partly.** Indexes, inputs, forwarders and apps run on Splunk Free.
**Users, roles and authentication do not exist on the Free licence at all**, and they are
a core exam topic — that half of the module requires a trial licence.

!!! info "This rung is the gate to the whole architecture track"
    Enterprise Certified Admin is not optional if a learner wants
    [Architect](spl-05-architect.md) or [Consultant](spl-06-consultant.md). It is the
    enforced prerequisite for Architect, and Architect is in turn enforced for Consultant.

    It is also the **last rung with no mandatory vendor coursework**. Everything above
    this point requires paid instructor-led courses to even register for the exam. If a
    self-funding learner is going to stop somewhere, this is the natural place —
    Power User plus Enterprise Admin, both reachable for US$260 in exam fees and free
    courseware.

---

## Overview

[SPL-01](spl-01-core-user.md) and [SPL-02](spl-02-power-user.md) treated Splunk as a thing
that answers questions. This module is about **the thing being run by someone who is
accountable when it stops**.

The subject matter is unglamorous and it is where real deployments actually fail: data
gets onboarded with the wrong sourcetype and nobody notices for six months; an index has
no retention policy and fills a disk; a forwarder stops sending and the first anyone knows
is when an investigation finds a hole in the timeline; a role grants search access to an
index containing payroll data.

Three themes run through it.

**Configuration is files, layered.** Splunk's UI writes `.conf` files, and the files are
the truth. Understanding the layering and precedence — and being able to prove which
setting won with `btool` — is the skill that separates an administrator from a person who
clicks things. It is also, directly, the most-tested reasoning skill on the Architect exam.

**Data onboarding is a design act, not a task.** `index`, `sourcetype`, `host` and
timestamp parsing are fixed at index time; getting them wrong means re-indexing. The
sourcetype decision made in five minutes at onboarding determines whether the data is
usable by [SPL-03](spl-03-cyber-defense-analyst.md)'s CIM-dependent content for the rest
of its retention life.

**Monitoring the monitoring.** The failure mode unique to a logging platform is *silent
absence*. A missing detection is visible; missing data is not. Forwarder health,
licence-volume tracking and data-source heartbeat monitoring are the controls that make
absence visible, and they are the topic administrators most often skip.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [SPL-02](spl-02-power-user.md) | **Enforced prerequisite** (via the Power User certification) and genuinely assumed. |
| [F02 — Operating Systems & Administration](../../../core/units/F02-operating-systems.md) | **Assumed core unit.** Linux/Windows administration, services, filesystems, permissions. |
| [F03 — Scripting & Automation](../../../core/units/F03-scripting-automation.md) | Deployment at scale is automated; the deployment server is a configuration-management system with Splunk-specific semantics. Compare [EXT-ANS](../ansible-security-automation.md). |
| [DE02 — Data Sources & Log Engineering](../../../degrees/operational/detection-engineering/DE02-data-sources-log-engineering.md) | **Assumed core unit.** Onboarding here is DE02's theory made operational. |
| [SPL-05](spl-05-architect.md) | **Direct successor.** SPL-05 takes every single-instance concept here and distributes it. |

---

## Learning outcomes

On completion, a learner can:

1. **Explain** the Splunk configuration file layering and **demonstrate** resolution of a
   precedence conflict using `btool`.
2. **Design** an index strategy — separation, sizing, retention — and **justify** it
   against retention obligations and search patterns.
3. **Implement** data inputs across the common types and **evaluate** the correctness of
   index-time field assignment before data volume makes it expensive to fix.
4. **Deploy** and manage universal forwarders at scale using the deployment server.
5. **Create** a role-based access model that enforces least privilege over index contents.
6. **Assess** platform health — licence usage, forwarder connectivity, data-source
   continuity — and detect the absence of expected data.

> Bloom's 3–6.

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | System Administrator | OM-ADM-001 | T0431 | Automate system administration tasks across platforms | Lab 3 |
| 2023 | System Administrator | OM-ADM-001 | T0435 | Manage accounts, network rights and access to systems | Lab 4 |
| 2023 | Cyber Defense Infrastructure Support | PR-INF-001 | T0335 | Build and maintain content and infrastructure for monitoring systems | Lab 1, Lab 2, Lab 5 |
| 2023 | Data Analyst | DA-ANL-001 | T0342 | Analyse data sources to produce actionable information | Lab 2 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Configuration management | CFMG | Level 4 | Lab 1, Lab 3 |
| Systems installation and removal | HSIN | Level 3–4 | Lab 3 |
| Availability management | AVMT | Level 4 | Lab 5 |
| Identity and access management | IAMT | Level 4 | Lab 4 |
| Storage management | STMG | Level 3–4 | Lab 1 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Secure Systems | Secure Configuration & Hardening | Practitioner | Lab 1, Lab 4 |
| Secure Systems | Platform Administration | Practitioner–Advanced | Lab 3, Lab 5 |
| Defensive Operations | Monitoring & Analysis | Practitioner | Lab 5 |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-04-K01 | Knowledge of `.conf` layering and precedence resolution | Topic 1; Lab 1 |
| Knowledge | SPL-04-K02 | Knowledge of index architecture: buckets, lifecycle, retention settings | Topic 2; Lab 1 |
| Knowledge | SPL-04-K03 | Knowledge of input types and index-time field assignment | Topic 3; Lab 2 |
| Knowledge | SPL-04-K04 | Knowledge of forwarder topologies and deployment-server semantics | Topic 4; Lab 3 |
| Knowledge | SPL-04-K05 | Knowledge of the Splunk RBAC model and index-level access control | Topic 5; Lab 4 |
| Skill | SPL-04-S01 | Skill in diagnosing configuration conflicts with `btool` | Lab 1 |
| Skill | SPL-04-S02 | Skill in onboarding a source with correct index-time fields | Lab 2 |
| Skill | SPL-04-S03 | Skill in managing forwarders at scale via deployment server | Lab 3 |
| Ability | SPL-04-A01 | Ability to design least-privilege index access against a real data-sensitivity map | Lab 4 |
| Ability | SPL-04-A02 | Ability to detect the *absence* of expected data | Lab 5; Summative |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — Configuration and indexes | 1–2 | 1 | 10 |
| B — Getting data in | 3–4 | 2, 3 | 14 |
| C — Access control | 5 | 4 | 8 |
| D — Operating the platform | 6–8 | 5 | 13 |
| | | | **~45 hours** |

---

## Topics

### Topic 1: Configuration Files and Precedence

`$SPLUNK_HOME/etc` layout: `system/default`, `system/local`, app `default` and `local`,
and user context. The precedence rules, and the fact that **`default` is never edited** —
a rule learners break once and then never again.

`btool` as the tool that answers "which setting actually applied?", and the discipline of
using it before forming a theory. This is the highest-value debugging skill in the
platform and it is directly load-bearing for [SPL-05](spl-05-architect.md).

### Topic 2: Indexes, Buckets and Retention

Index architecture: hot, warm, cold, frozen. Bucket lifecycle and what triggers each
transition. `maxTotalDataSizeMB`, `frozenTimePeriodInSecs`, and the fact that **the smaller
of size and time wins** — the setting that silently destroys data organisations believed
they had retained.

Index design as a security decision: separation by data sensitivity is the mechanism by
which access control in Topic 5 becomes possible, because Splunk's RBAC is index-scoped.
An estate with one big index cannot enforce least privilege, and that is an architecture
mistake made at onboarding time.

Retention as a legal question — see [Australian context](#australian-context).

### Topic 3: Getting Data In

Input types: monitor, upload, network (TCP/UDP), scripted, HTTP Event Collector, and
modular inputs. Choosing among them.

Parsing: line breaking, timestamp recognition, and event breaking, with the observation
that most bad onboarding is a timestamp problem. Sourcetype assignment and why renaming a
sourcetype later is not a fix for the data already indexed.

**Onboarding checklist discipline:** verify index, sourcetype, host, timestamp and line
breaking on a sample *before* opening the tap. Ten minutes here saves a re-index later.

### Topic 4: Forwarders and the Deployment Server

Universal versus heavy forwarders, and when the extra weight of a heavy forwarder is
justified. `outputs.conf`, load balancing across indexers, indexer acknowledgement, and
persistent queues for when the indexing tier is unavailable.

The deployment server, server classes and apps: configuration management for the Splunk
estate. This is the same problem [EXT-ANS](../ansible-security-automation.md) solves for
the OS layer, with Splunk-specific semantics — and the same blast-radius concern applies,
because a bad app pushed to every forwarder is an estate-wide incident.

### Topic 5: Users, Roles and Least Privilege

Authentication (native, LDAP, SAML) and the role model: capabilities, index access,
search filters, and role inheritance.

The design problem: security telemetry contains, in aggregate, some of the most sensitive
data in the organisation — authentication records, user behaviour, and often payload
fragments. "Everyone in security can search everything" is the default and it is usually
wrong. Index separation from Topic 2 is what makes a defensible answer possible.

!!! danger "Free-licence gap"
    **Splunk Free has no authentication, no users and no roles** — you are dropped straight
    into Splunk Web as an admin-level user with no login. This entire topic requires a
    **trial licence** to practise, and it is examinable. It is also why a Free instance
    must never hold real data: anyone who can reach the port is an administrator.

### Topic 6: Licensing and Volume Management

Licence model, volume tracking, warnings and violations. On the Free licence: 500 MB/day,
a bulk-load allowance above the cap only twice in any 30-day period, and — the consequence
that surprises people — **exceed too often and Splunk keeps indexing but disables search**.

Licence management is capacity management with a commercial edge, and it is the constraint
that forces the filtering and routing decisions in Topic 7.

### Topic 7: Filtering and Routing Data

Dropping unwanted events at the heavy forwarder, routing by sourcetype, and index-time
field extraction — with the standing warning that index-time work is expensive and
permanent, so the bar for doing it is high.

**The judgement:** every event dropped saves licence and storage, and is unavailable
forever if you need it. Filtering decisions are made under uncertainty about future
investigations, and they should be documented as decisions, not buried in a `transforms.conf`.

### Topic 8: Monitoring the Platform — and the Absence of Data

The Monitoring Console. Forwarder connectivity, indexing latency, skipped searches, queue
saturation.

**The distinctive failure mode of a logging platform is silent absence.** A source that
stops sending produces no error in the SOC — it produces nothing, which looks exactly like
a quiet day. Building data-source continuity monitoring (expected sources, expected
volumes, alert on absence) is the control, and it is the single most valuable thing an
administrator can build for the analysts in [SPL-03](spl-03-cyber-defense-analyst.md).

---

## Labs & exercises

!!! warning "Licensing"
    Labs 1, 2, 3 and 5 run on **Splunk Free** (alerting in Lab 5 requires a trial). **Lab 4
    requires a trial licence** — authentication does not exist on Free.

Observe the [series safety rules](index.md#safety-authorisation-and-data-handling). Never
onboard real production or personal data into a lab instance.

### Lab 1: Index Design and a Precedence Conflict

Design and build an index strategy for a described organisation with three data
sensitivities and two retention obligations. Then deliberately create a configuration
precedence conflict across app and system layers, and resolve it using `btool`.

**Deliverable:** the index design with justification for each retention setting, plus a
walkthrough of the conflict diagnosis showing which layer won and why.

### Lab 2: Onboard a Source Correctly — and Incorrectly

Onboard a log source with a non-obvious timestamp format. First do it carelessly: observe
wrong `_time`, wrong line breaking, wrong sourcetype. Then do it properly with a
sample-first checklist.

**Deliverable:** both configurations, evidence of the failure modes, and a written
onboarding checklist you would give to a colleague.

### Lab 3: Manage Forwarders at Scale

Deploy universal forwarders. Use the deployment server with server classes to push a
configuration app. Then push a **bad** configuration and recover from it.

**Deliverable:** the working topology, plus a note on blast radius — how many hosts the
bad push reached, how you detected it, and what would have limited it. Compare against
the blast-radius discipline in [EXT-ANS](../ansible-security-automation.md).

### Lab 4: Least-Privilege Access Model — *trial licence required*

Given a data-sensitivity map (security telemetry, HR-adjacent logs, payment-system logs)
and four job functions, design and implement roles enforcing least privilege. Test by
attempting access you should not have.

**Deliverable:** the role model, the test evidence, and a justification of each grant.
"Security team gets everything" must be either defended explicitly or abandoned.

### Lab 5: Detect the Absence of Data

Build data-source continuity monitoring. Then stop a forwarder and confirm you are told.

**Deliverable:** the monitoring content, evidence it fired, and the expected-source
inventory it depends on. State how the inventory is maintained — an inventory nobody
updates is the actual failure mode.

---

## Assessment

### Formative 1: Which Layer Won?

Given a set of `.conf` files across layers and a resulting behaviour, predict the effective
configuration, then verify with `btool`.

### Formative 2: The Retention Trap

Given index settings and a stated retention obligation, determine how much data the
organisation *actually* retains. At least one case must expose the size-versus-time
interaction destroying data earlier than the policy claims.

### Summative: Administration Design Package

For a described organisation: an index and retention design mapped to obligations, an
onboarding standard, a forwarder topology with deployment strategy, a role model, and a
platform-health monitoring plan including absence detection.

Full marks require a **filtering and routing proposal with an explicit statement of what
is being discarded and the investigative risk that creates**.

---

## Australian context

Retention and access design are where Australian obligations bite hardest on a Splunk
administrator, and they pull in opposite directions.

- **Privacy Act 1988 (Cth)** — APP 11.2 requires destruction or de-identification of
  personal information no longer needed. Logs routinely contain personal information.
  Indefinite retention "for security" is not automatically defensible.
- **ASD Information Security Manual** — event-logging and retention guidance is the usual
  source of an Australian organisation's baseline retention period, and is frequently
  longer than the business would otherwise choose.
- **Essential Eight** — monitoring and logging maturity requirements shape what must be
  centrally collected, which drives licence volume, which drives the Topic 7 filtering
  decisions. The chain from control to cost is direct and worth making explicit to
  learners.
- **SOCI Act 2018 (Cth)** — critical-infrastructure responsible entities have
  risk-management-program obligations that reach into logging scope and incident
  reporting.
- **APRA CPS 234** — regulated financial entities must maintain information-security
  capability and be able to demonstrate control operation; log retention is often the
  evidence.
- **Data sovereignty and IRAP** — where indexed data physically resides matters for
  government and IRAP-assessed workloads. This becomes a full design constraint in
  [SPL-05](spl-05-architect.md), but the index-location decision starts here.
- **Workplace surveillance law** (e.g. NSW *Workplace Surveillance Act 2005*) constrains
  monitoring of employees and interacts with the role model in Topic 5: who may search
  logs about a named individual is a governance question, not just a capability grant.

**The genuine tension to teach:** ISM and Essential Eight push retention up; the Privacy
Act pushes it down; licence cost pushes volume down; incident investigation pushes it up.
There is no setting that satisfies all four. The administrator's job is to make the
trade-off explicit and get it signed off — not to pick a number quietly. Covered as a
governance problem in [SC03](../../../core/units/SC03-governance-policy-compliance.md) and
[F05](../../../core/units/F05-legal-ethics-compliance.md).

---

## Verification status

- **Verified 2026-09-09:** all exam facts above, against the linked official page —
  including that **Core Certified Power User is an enforced prerequisite** and that Splunk
  publishes **no mandatory prerequisite coursework** for this rung.
- **Verified 2026-09-09:** Splunk Free licence limits and disabled features (500 MB/day; no
  authentication, users, roles, alerting, distributed search or ingest actions; bulk load
  above the cap permitted twice per 30 days; search disabled after repeated violations).
- **Not verified:** the exam code is not published and is deliberately not stated.
  Recommended-course lists exist but are not authoritative for registration. Topic
  coverage is the module author's reading of the platform and has **not** been reconciled
  against Splunk's published test blueprint.
- Framework mappings and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [Enterprise Certified Admin track](https://www.splunk.com/en_us/training/certification-track/splunk-enterprise-certified-admin.html) — official exam page and test blueprint.
- [Splunk Enterprise Admin Manual](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Whatsinthismanual) — the authoritative reference for Topics 1, 2, 5 and 6.
- [Getting Data In manual](https://docs.splunk.com/Documentation/Splunk/latest/Data/WhatSplunkcanmonitor) — Topics 3, 4 and 7.
- [About Splunk Free](https://help.splunk.com/en/splunk-enterprise/administer/admin-manual/10.4/configure-splunk-licenses/about-splunk-free) — the licence constraints that shape every lab in this module.
- [Managing Indexers and Clusters of Indexers](https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Aboutindexesandindexers) — bucket lifecycle and retention.
- [ASD Information Security Manual](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism) — event logging and retention guidance.
- [OAIC — Australian Privacy Principles](https://www.oaic.gov.au/privacy/australian-privacy-principles) — APP 11 and the retention constraint.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-04 |
| Module Title | Platform Administration — Splunk Enterprise Certified Admin |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 3–6 (Apply / Analyse / Evaluate / Create) |
| Notional Hours | ~45 |
| Zero-cost achievable | Partly — Lab 4 (authentication/RBAC) requires a trial licence |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
