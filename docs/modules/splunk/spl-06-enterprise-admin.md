# SPL-06: Platform Administration — Splunk Enterprise Certified Admin

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
    [Architect](spl-07-architect.md) or [Consultant](spl-08-consultant.md). It is the
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
| [SPL-07](spl-07-architect.md) | **Direct successor.** SPL-07 takes every single-instance concept here and distributes it. |

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
| Knowledge | SPL-06-K01 | Knowledge of `.conf` layering and precedence resolution | Topic 1; Lab 1 |
| Knowledge | SPL-06-K02 | Knowledge of index architecture: buckets, lifecycle, retention settings | Topic 2; Lab 1 |
| Knowledge | SPL-06-K03 | Knowledge of input types and index-time field assignment | Topic 3; Lab 2 |
| Knowledge | SPL-06-K04 | Knowledge of forwarder topologies and deployment-server semantics | Topic 4; Lab 3 |
| Knowledge | SPL-06-K05 | Knowledge of the Splunk RBAC model and index-level access control | Topic 5; Lab 4 |
| Skill | SPL-06-S01 | Skill in diagnosing configuration conflicts with `btool` | Lab 1 |
| Skill | SPL-06-S02 | Skill in onboarding a source with correct index-time fields | Lab 2 |
| Skill | SPL-06-S03 | Skill in managing forwarders at scale via deployment server | Lab 3 |
| Ability | SPL-06-A01 | Ability to design least-privilege index access against a real data-sensitivity map | Lab 4 |
| Ability | SPL-06-A02 | Ability to detect the *absence* of expected data | Lab 5; Summative |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — Install, CLI and configuration | 1–3 | 1 | 14 |
| B — Indexes and retention | 4 | 1 | 10 |
| C — Getting data in | 5–8 | 2, 3, 6 | 24 |
| D — Access control and licensing | 9–10 | 4 | 12 |
| E — Platform services | 11–13 | 6 | 12 |
| F — Operating, monitoring and troubleshooting | 14–16 | 5, 7 | 16 |
| G — Distributed search | 17 | 8 | 8 |
| | | | **~96 hours** |

---

## Blueprint alignment

Verified against the published
[Enterprise Certified Admin test blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-enterprise-admin.pdf),
retrieved 2026-09-09. Seventeen domains, most weighted at 5%.

| Domain | Weight | Covered by |
|---|---|---|
| 1.0 Splunk admin basics (components) | 5% | Topic 1 |
| 2.0 License management (types, violations) | 5% | Topic 10 |
| 3.0 Configuration files (directory structure, layering, precedence, `btool`) | 5% | Topic 3 |
| 4.0 **Splunk indexes** (structure, bucket types, **data integrity check**, `indexes.conf`, **fishbucket**, retention) | **10%** | Topic 4 |
| 5.0 User management (roles, custom role, add users) | 5% | Topic 9 |
| 6.0 Authentication (LDAP, other options, **multifactor**) | 5% | Topic 9 |
| 7.0 Getting data in (input basics, forwarder types, CLI input) | 5% | Topics 5, 7 |
| 8.0 **Distributed search** (how it works, search head and peers, **search groups**, **search head scaling options**) | **10%** | Topic 17 |
| 9.0 Getting data in — staging (three phases, input options) | 5% | Topics 2, 5 |
| 10.0 Configuring forwarders | 5% | Topic 7 |
| 11.0 **Forwarder management** (deployment server, deployment apps, clients, client groups, monitoring) | **10%** | Topic 8 |
| 12.0 Monitor inputs (file/directory, optional settings, remote deploy) | 5% | Topic 5 |
| 13.0 Network and scripted inputs | 5% | Topic 5 |
| 14.0 Agentless inputs (**WMI**, HTTP Event Collector) | 5% | Topic 5 |
| 15.0 Fine tuning inputs (input-phase defaults, sourcetype fine-tuning, charset) | 5% | Topic 6 |
| 16.0 Parsing phase (defaults, line breaking, timestamps/time zones, **Data Preview**) | 5% | Topic 6 |
| 17.0 Manipulating raw data (transformations, mask/delete, override sourcetype/host, route to index, drop events, `SEDCMD`) | 5% | Topic 11 |

!!! note "Distributed search is examined here, not only at Architect level"
    Domain 8.0 carries **10%** — how distributed search works, the search head and peer
    roles, configuring a distributed search group, and search head scaling options. It is
    covered in Topic 17 at admin depth; [SPL-07](spl-07-architect.md) Topic 5 takes it to
    architect depth. An earlier draft deferred all of it to SPL-07, which would have left
    a gap worth a tenth of this exam.

**Beyond the blueprint** — Topics 2 (CLI/REST), 12 (KV Store), 13 (search head
administration), 14 (Monitoring Console), 15 (backup and upgrades) and 16 (troubleshooting
method) are not in this blueprint. They are included because they are unavoidable in
production and because [SPL-07](spl-07-architect.md) and
[SPL-08](spl-08-consultant.md) assume them.

---

## Topics

### Topic 1: Installation, Directory Layout and Startup

Installing Splunk Enterprise on Linux and Windows. `$SPLUNK_HOME` layout: `bin`, `etc`,
`var`, and where each kind of state lives. Running as a non-root user, the boot-start
mechanism, and file-descriptor and `THP`/`ulimit` requirements that cause obscure
performance problems when unset.

Instance roles and what a single-instance install is collapsing together.

### Topic 2: The Splunk CLI and REST API

The CLI as the administrator's primary interface: `splunk start|stop|restart|status`,
`splunk add|edit|remove`, `splunk list`, `splunk search`, `splunk btool`, `splunk cmd`,
`splunk diag`, `splunk show`, `splunk apply cluster-bundle`, `splunk validate`.

The management port, the REST API (`/services/...`), and `| rest` from the search bar.
Automating administration through the API rather than the UI, and why every serious
deployment ends up doing so — the same argument as
[F03](../../../core/units/F03-scripting-automation.md).

### Topic 3: Configuration Files and Precedence

`$SPLUNK_HOME/etc` layout: `system/default`, `system/local`, app `default` and `local`, and
user context. The precedence rules, and the fact that **`default` is never edited** — a
rule learners break once and then never again.

`btool` as the tool that answers "which setting actually applied?"
(`splunk btool inputs list --debug`), and the discipline of using it before forming a
theory. This is the highest-value debugging skill in the platform and it is load-bearing
for [SPL-07](spl-07-architect.md).

**The files an administrator actually lives in:** `inputs.conf`, `outputs.conf`,
`props.conf`, `transforms.conf`, `indexes.conf`, `server.conf`, `web.conf`,
`authentication.conf`, `authorize.conf`, `limits.conf`, `savedsearches.conf`,
`macros.conf`, `deploymentclient.conf`, `serverclass.conf`, `app.conf`, `distsearch.conf`.
What each governs and where it belongs.

### Topic 4: Indexes, Buckets and Retention

Index architecture: hot, warm, cold, frozen, thawed. Bucket lifecycle and what triggers
each transition. Bucket naming and what it tells you.

The settings that matter: `homePath`, `coldPath`, `thawedPath`, `maxTotalDataSizeMB`,
`frozenTimePeriodInSecs`, `maxHotBuckets`, `maxWarmDBCount`, `maxDataSize`,
`coldToFrozenDir` and `coldToFrozenScript`.

**The smaller of size and time wins** — the setting that silently destroys data an
organisation believed it had retained. Test this, do not assume it.

Index design as a security decision: separation by data sensitivity is the mechanism by
which access control in Topic 9 becomes possible, because Splunk's RBAC is index-scoped. An
estate with one big index cannot enforce least privilege, and that is an architecture
mistake made at onboarding time.

**Index data integrity control** (`enableDataIntegrityControl`) and hash validation for
tamper-evidence — relevant wherever logs are evidence, and examined in domain 4.0.

The **fishbucket**: how Splunk tracks how far it has read into a monitored file, where that
state lives, and the consequences of deleting it (re-indexing everything) or of a file
whose CRC collides with another (data silently not indexed). This is a favourite exam
topic and a real-world incident cause.

Metrics indexes and when to use them over event indexes.

### Topic 5: Getting Data In — Inputs

Input types and their trade-offs:

- **Monitor** inputs: `monitor://`, whitelist/blacklist, `crcSalt`, `followTail`, and the
  file-tracking problems that produce duplicate or missing data.
- **Batch** inputs and destructive read.
- **Network** inputs: TCP and UDP, and why UDP loses data silently under load.
- **Scripted** inputs and modular inputs.
- **HTTP Event Collector (HEC):** tokens, acknowledgement, indexer acknowledgement, and
  the raw versus event endpoints. HEC is how most modern and cloud-native sources arrive.
- **Windows-specific:** event logs, performance monitoring, registry, and **WMI**
  (agentless) inputs — WMI is examined explicitly in domain 14.0 alongside HEC.
- **Files and directories versus agents:** when a forwarder is required.

### Topic 6: Parsing — `props.conf` and `transforms.conf`

The settings that determine whether data is usable, and the ones the consultant track calls
the parsing essentials:

- `SHOULD_LINEMERGE`, `LINE_BREAKER`, `BREAK_ONLY_BEFORE`, `MUST_BREAK_AFTER`
- `TIME_PREFIX`, `TIME_FORMAT`, `MAX_TIMESTAMP_LOOKAHEAD`, `TZ`, `DATETIME_CONFIG`
- `TRUNCATE`, `CHARSET`, `EVENT_BREAKER` (for forwarder-side breaking)
- `KV_MODE`, `REPORT`, `EXTRACT`, `FIELDALIAS`, `EVAL`, `LOOKUP`

**Setting these explicitly rather than relying on inference** is the difference between an
onboarding that works forever and one that breaks when the data changes shape. This is the
foundation of the base-configuration discipline in [SPL-08](spl-08-consultant.md).

Sourcetype assignment, sourcetype renaming, and why renaming later does not fix data
already indexed.

**Data Preview** as the pre-flight check — validating event breaking, timestamps and
sourcetype assignment against a sample *before* opening the tap. Examined in domain 16.0
and the single cheapest defect-prevention step in Splunk administration.

### Topic 7: Forwarders and Deployment

Universal versus heavy forwarders, and when the extra weight of a heavy forwarder is
justified (parsing, filtering, routing — everything else argues for universal).

`outputs.conf`: indexer discovery, load balancing, `autoLB` and `autoLBFrequency`,
indexer acknowledgement (`useACK`), persistent queues, and `maxQueueSize`. Forwarder
throughput limits in `limits.conf` (`maxKBps`) and why the default throttle surprises people
during a backfill.

Intermediate forwarding tiers and their cost. Forwarder installation at scale and
deployment automation.

### Topic 8: The Deployment Server and Apps

Deployment server, server classes, client filtering, and deployment apps. `serverclass.conf`
and `deploymentclient.conf`. Reload versus restart behaviour on app deployment.

App and add-on management generally: installing from Splunkbase, app structure
(`default`/`local`/`metadata`), `app.conf`, and the discipline of never editing an app's
`default` directory.

**Blast radius:** the deployment server is a configuration-management system, and a bad app
pushed to every forwarder is an estate-wide incident. The same discipline as
[EXT-ANS](../ansible-security-automation.md) applies.

### Topic 9: Users, Roles and Authentication

Authentication methods: native, **LDAP** (examined explicitly — strategies, group-to-role
mapping, and bind-account failure modes), SAML/SSO, and the steps to enable
**multifactor authentication**, which domain 6.0 calls out directly.
`authentication.conf` and `authorize.conf`.

The role model: capabilities, index access (`srchIndexesAllowed`/`srchIndexesDefault`),
**search filters** (`srchFilter`) for row-level restriction, role inheritance, and the
search quotas and disk quotas that prevent one user from consuming the cluster.

The design problem: security telemetry contains, in aggregate, some of the most sensitive
data in the organisation. "Everyone in security can search everything" is the default and
usually wrong. Index separation from Topic 4 is what makes a defensible answer possible.

!!! danger "Free-licence gap"
    **Splunk Free has no authentication, no users and no roles** — you are dropped straight
    into Splunk Web as an admin-level user with no login. This entire topic requires a
    **trial licence** to practise, and it is examinable. It is also why a Free instance must
    never hold real data: anyone who can reach the port is an administrator.

### Topic 10: Licensing and Volume Management

Licence types, licence manager and peers, licence pools and stacks, warnings and violations.
Volume tracking and the licence usage dashboards.

On the Free licence: 500 MB/day, a bulk-load allowance above the cap only twice in any
30-day period, and — the consequence that surprises people — **exceed too often and Splunk
keeps indexing but disables search**.

Licence management is capacity management with a commercial edge, and it is the constraint
that forces the filtering and routing decisions in Topic 11.

### Topic 11: Filtering, Routing and Index-Time Transformation

Dropping unwanted events at the heavy forwarder (`nullQueue`), routing by sourcetype or
content to different indexes or outputs, cloning to multiple destinations, and index-time
field extraction — with the standing warning that index-time work is expensive and
permanent, so the bar for doing it is high.

Masking sensitive data at index time with `SEDCMD`, and the important caveat that this
genuinely removes the data, unlike search-time masking. Which means it is both the right
control for secrets and an irreversible loss if applied wrongly.

**The judgement:** every event dropped saves licence and storage, and is unavailable
forever if you need it. Filtering decisions are made under uncertainty about future
investigations, and should be documented as decisions rather than buried in a
`transforms.conf`.

### Topic 12: The KV Store

KV Store collections, `collections.conf`, and their use by lookups and apps. Sizing,
backup and restore, and the failure modes — a KV Store that will not start is a common and
alarming incident.

Relevant because ES, ITSI and much custom content depend on it entirely.

### Topic 13: Search Head Administration

Search head configuration: `limits.conf` concurrency settings, scheduler behaviour, skipped
searches and their diagnosis, dispatch directory management, and search artefact retention.

Scheduled search management: priority, scheduling windows, and spreading load. Workload
management concepts where available.

Knowledge object administration at scale: orphaned objects after a user departs, and the
reassignment process.

### Topic 14: Monitoring the Platform — and the Absence of Data

The Monitoring Console: setup in standalone and distributed modes, and the health checks it
provides. Forwarder connectivity, indexing latency, skipped searches, queue saturation
(and reading which queue is blocked as a diagnostic).

Splunk's own `_internal`, `_audit` and `_introspection` indexes as the primary
troubleshooting data source.

**The distinctive failure mode of a logging platform is silent absence.** A source that
stops sending produces no error in the SOC — it produces nothing, which looks exactly like a
quiet day. Building data-source continuity monitoring (expected sources, expected volumes,
alert on absence) is the control, and it is the single most valuable thing an administrator
can build for the analysts in [SPL-03](spl-03-cyber-defense-analyst.md).

### Topic 15: Backup, Recovery and Upgrades

What actually needs backing up: configuration, apps, the knowledge layer, KV Store — all
harder to reconstruct than the indexed data itself.

Upgrade planning: version compatibility between tiers, upgrade ordering, testing, and
rollback. `splunk diag` for support cases.

### Topic 16: Troubleshooting Method

A structured approach before the distributed complexity of [SPL-07](spl-07-architect.md):
identify the symptom precisely, locate the tier, gather evidence from `_internal` and the
Monitoring Console, form one hypothesis, and test it.

The common presentations: data not arriving, data arriving with wrong fields, data arriving
late, searches slow, searches returning wrong results, and the instance that will not start.

---

### Topic 17: Distributed Search at Admin Level

**Examined at 10%** — the largest single domain in this blueprint alongside indexes and
forwarder management.

How distributed search works: the search head decomposes a search, distributes the
streaming portion to search peers, and reduces the results centrally. What this implies
about where work happens and why an under-provisioned search head bottlenecks an otherwise
healthy indexing tier.

The roles of **search head** and **search peers**, and the fact that an indexer is a search
peer — the same machine wearing a second hat.

Configuring a **distributed search group** in `distsearch.conf`, adding search peers, and
the certificate and authentication requirements between them.

**Search head scaling options** and their thresholds: a single search head, independent
search heads, and search head clustering. When each is appropriate — and the honest
observation that a search head cluster is often bought before it is needed. Developed at
architect depth in [SPL-07](spl-07-architect.md) Topics 4–5.

The knowledge bundle: what the search head ships to the peers, and why an oversized bundle
degrades every search on the deployment.

---

## Labs & exercises

!!! tip "Lab guide: how to actually run these"
    **[SPL-06 lab guide](../../../labs/guides/spl-06.md)** gives the setup, the commands and the
    verification for every lab below — against the
    **[lab environment](../../../labs/README.md)**, a reproducible synthetic estate of
    ~130k labelled events with ground truth, so you can measure a real positive
    predictive value rather than estimate one.

    The split of responsibility: **this page says why each lab exists and what to
    deliver; the guide says how to run it.** Marking criteria stay here.

    **Lab 3 no longer needs a trial.** The guide ships a deployment server and three universal forwarders that run on the Free licence, so the server-class and blast-radius work is fully runnable. Labs 4, 5 and 8 still need a trial for authentication, alerting and distributed search.

    Conf-file work: **[nine exercises with marking keys](../../../labs/paper/conf-practice.md)**.

    Self-assess with the **[52-question quiz](quiz.md)**.

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

### Lab 6: Parse It Properly, Then Route and Mask It

Onboard a source via HEC and a second via a monitor input. Set the parsing settings from
Topic 6 **explicitly** — line breaking, timestamp, truncation, charset — rather than
relying on inference.

Then configure a heavy forwarder to route two sourcetypes to different indexes, drop a
third to `nullQueue`, and mask a secret with `SEDCMD`.

**Deliverable:** the working configuration, evidence that the masked value is genuinely
absent from the index (not merely hidden at search time), and a written note on what the
`nullQueue` decision costs you if you later need that data.

### Lab 7: Diagnose Five Faults

Given an instance with five injected faults — data not arriving, wrong timestamps, a
blocked queue, a skipped scheduled search, and an instance that will not start — diagnose
each using the Topic 16 method and `_internal`.

**Deliverable:** for each fault, the evidence gathered and the order you gathered it in.
Marked on method, not speed.

---

### Lab 8: Stand Up Distributed Search

Configure a search head with two search peers. Verify the peers are reachable and that a
search executes distributed rather than locally — prove it from the job inspector, not
from the absence of errors.

Then break it two ways: stop a peer mid-search, and add a large automatic lookup to inflate
the knowledge bundle. Observe and record what each does to results and to search time.

**Deliverable:** the working configuration, the job-inspector evidence of distribution, and
the two failure observations with an explanation of what the bundle size cost you.

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
  [SPL-07](spl-07-architect.md), but the index-location decision starts here.
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
  Recommended-course lists exist but are not authoritative for registration. Topic coverage **has now been reconciled against the published test blueprint** — see
  [Blueprint alignment](#blueprint-alignment). Sub-objective wording is not reproduced;
  the mapping uses domain titles and weightings only.
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
| Module Code | SPL-06 |
| Module Title | Platform Administration — Splunk Enterprise Certified Admin |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 3–6 (Apply / Analyse / Evaluate / Create) |
| Notional Hours | ~96 |
| Zero-cost achievable | Partly — Lab 4 (authentication/RBAC) requires a trial licence |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
