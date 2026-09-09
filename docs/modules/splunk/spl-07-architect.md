# SPL-07: Architecture & Deployment — Splunk Enterprise Certified Architect

> **Part of:** [EXT-SPL — The Splunk Series](index.md)
> **Status:** Draft · **Version:** v0.1 · **Last Reviewed:** 2026-09-09
> **Domain Expert:** _Unassigned_ · **Practitioner Reviewer:** _Unassigned — must hold Enterprise Certified Architect_

!!! warning "Non-credit, vendor-specific"
    See the [series index](index.md) for the R3 carve-out. Nothing here satisfies a
    core-unit requirement.

---

## Target certification

| Field | Value | Verified |
|---|---|---|
| Certification | [Splunk Enterprise Certified Architect](https://www.splunk.com/en_us/training/certification-track/splunk-enterprise-certified-architect.html) | 2026-09-09 |
| Level | **Expert** | 2026-09-09 |
| Prerequisite certifications | **Splunk Core Certified Power User** *and* **Splunk Enterprise Certified Admin** — both enforced | 2026-09-09 |
| Prerequisite coursework | **Four courses, all mandatory** (below) | 2026-09-09 |
| Length | 90 minutes | 2026-09-09 |
| Format | 85 multiple choice questions | 2026-09-09 |
| Price | US$130 per attempt | 2026-09-09 |
| Delivery | Pearson VUE | 2026-09-09 |

### The mandatory coursework gate

**All four** of these are required to qualify for exam registration:

1. `Architecting Splunk Enterprise Deployments`
2. `Troubleshooting Splunk Enterprise`
3. `Splunk Cluster Administration`
4. `Splunk Enterprise Deployment Practical Lab`

!!! success "Authorisation is automatic — no email needed"
    A candidate who **already holds Enterprise Certified Admin** and has completed all four
    courses **automatically receives exam authorisation within 5–7 business days of
    receiving their passing lab results**.

    This is the material difference between the Architect and
    [Consultant](spl-08-consultant.md) tracks: Architect authorisation arrives on its own;
    Consultant authorisation must be requested by email.

!!! note "Naming variance"
    Splunk's exam page names course 4 *Splunk Enterprise Deployment Practical Lab*; the
    track flowchart names it *Splunk Deployment Practical Lab*. Same course. Note 4 is a
    **practical lab with assessed results** — the automatic authorisation is triggered by
    passing it, not by enrolling.

**Zero-cost achievable: no.** Two reasons, and both are hard blocks:

- **The coursework is paid, instructor-led and mandatory.** There is no self-study route to
  exam registration at this rung. Treat this track as employer-sponsored.
- **Splunk Free has no distributed search and no clustering.** Every architectural concept
  in this module is invisible on the Free licence. Labs require a **trial licence** and
  multiple instances.

---

## Overview

This is the module the series' [architecture question](index.md#the-certification-ladder)
points at, and it is where Splunk stops being a product you configure and becomes a
**distributed system you design under constraint**.

Everything before this module assumed one machine. The moment there is more than one, a
different class of question appears: where does the data live, how many copies, what
happens when a node dies mid-search, how do you get a consistent answer from an
inconsistent cluster, and — the question that actually decides real deployments — **how
much hardware do you need, and can you defend the number to someone who does not want to
pay for it?**

Three things distinguish this module from everything below it.

**Sizing is the deliverable.** The single most valuable Architect skill is producing a
defensible capacity model: ingest volume, retention, search concurrency and replication
factors turned into an indexer count and a storage figure, with the assumptions stated. An
architect who cannot show their working produces a design nobody can review and nobody can
fund.

**Replication and search factors are a data-durability decision, not a checkbox.** Choosing
RF and SF is choosing how much data loss and how much search unavailability the
organisation accepts, and multiplying storage cost accordingly. It is the same
availability-versus-cost trade-off
[SE01](../../../degrees/strategic/security-engineering/SE01-secure-system-design.md) and
[SE02](../../../degrees/strategic/security-engineering/SE02-security-architecture.md) teach
as a general discipline, in a form where the arithmetic is unambiguous.

**Troubleshooting is an architectural skill.** One of the four mandatory courses is
troubleshooting, and this is not an accident. In a distributed deployment, "the search is
slow" has a dozen possible causes across four tiers. The diagnostic method — narrow the
tier, then the component, then prove it with data from the Monitoring Console and the job
inspector — is what the exam actually tests, and it rests on the `btool` and precedence
discipline from [SPL-06](spl-06-enterprise-admin.md) Topic 1.

### A second architect certification

Splunk also offers the **[Certified Cybersecurity Defense Architect](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-architect.html)**
(Expert, 75 minutes, 67 questions, US$130, Pearson VUE, **no published prerequisites**).
The two are different jobs sharing a word:

| | Enterprise Certified Architect | Cybersecurity Defense Architect |
|---|---|---|
| Designs | The Splunk platform — indexers, clusters, capacity, resilience | The security detection and response capability built on it |
| Prerequisites | Power User **and** Enterprise Admin, plus 4 mandatory courses | **None published** |
| Natural predecessor here | [SPL-06](spl-06-enterprise-admin.md) | [SPL-03](spl-03-cyber-defense-analyst.md) |
| Degree analogue | [SE01](../../../degrees/strategic/security-engineering/SE01-secure-system-design.md) / [SE02](../../../degrees/strategic/security-engineering/SE02-security-architecture.md) | [SE04](../../../degrees/strategic/security-engineering/SE04-detection-response-engineering.md) |

**This module's primary target is the Enterprise Certified Architect.** Topic 9 covers the
security-architecture layer that the Cybersecurity Defense Architect exam addresses,
because a platform architect who cannot reason about the security capability the platform
exists to serve is designing in a vacuum. A learner targeting only the Cybersecurity
Defense Architect credential can take Topic 9 with [SPL-03](spl-03-cyber-defense-analyst.md)
and skip the clustering mechanics — but should be aware that the "no published
prerequisites" claim is [flagged for verification](index.md#verification-status).

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [SPL-06](spl-06-enterprise-admin.md) | **Enforced prerequisite** (via Enterprise Certified Admin). Every concept here is a distributed version of one taught there. |
| [SE02 — Security Architecture](../../../degrees/strategic/security-engineering/SE02-security-architecture.md) | **The core architecture unit.** SE02 teaches architecture method — SABSA, Zero Trust, NIST SP 800-160. SPL-07 applies that method to a distributed log platform where the constraints are numeric and the trade-offs are priced. |
| [SC02 — Security Architecture (Strategic Core)](../../../core/units/SC02-security-architecture.md) | Strategic-core architecture grounding. |
| [SE01 — Secure System Design](../../../degrees/strategic/security-engineering/SE01-secure-system-design.md) | Availability, resilience and failure-mode reasoning. |
| [SE04 — Detection & Response Engineering](../../../degrees/strategic/security-engineering/SE04-detection-response-engineering.md) | Topic 9; the Cybersecurity Defense Architect angle. |
| [SE05 — Security in Cloud & DevSecOps](../../../degrees/strategic/security-engineering/SE05-security-cloud-devsecops.md) | Cloud deployment, Splunk Cloud, and data-residency constraints in Topic 8. |
| [SE06 — Capstone: Architecture Design](../../../degrees/strategic/security-engineering/SE06-capstone-architecture-design.md) | The summative here is deliberately shaped like an SE06 deliverable. |
| [SPL-08](spl-08-consultant.md) | Successor — implementation practice, and the next rung. |

---

## Learning outcomes

On completion, a learner can:

1. **Design** a distributed Splunk deployment topology appropriate to a stated ingest
   volume, retention obligation, search load and availability requirement.
2. **Produce** a defensible capacity model with assumptions stated, and **justify** the
   indexer count and storage figure to a non-technical approver.
3. **Evaluate** replication and search factor choices against data-durability requirements
   and their storage-cost multiple.
4. **Analyse** index-cluster and search-head-cluster behaviour under failure, including
   captaincy loss and node failure mid-search.
5. **Diagnose** performance and correctness problems across the forwarding, indexing,
   search and knowledge tiers using a structured method.
6. **Assess** a deployment against availability, disaster-recovery and data-residency
   requirements, and **create** a migration or scaling plan with a rollback path.

> Bloom's 4–6, consistent with an expert-level rung and with the strategic-layer
> expectations in [`docs/content-standards.md`](../../content-standards.md).

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Security Architect | SP-ARC-002 | T0050 | Design system security architecture and supporting infrastructure | Lab 1, Summative |
| 2023 | Enterprise Architect | SP-ARC-001 | T0473 | Document and address organisational requirements in system design | Lab 1, Lab 5 |
| 2023 | Systems Developer | SP-SYS-002 | T0014 | Design and develop system architectures and data structures | Lab 2 |
| 2023 | Cyber Defense Infrastructure Support | PR-INF-001 | T0335 | Build and maintain monitoring infrastructure | Lab 2, Lab 3 |
| 2023 | System Administrator | OM-ADM-001 | T0431 | Automate and scale system administration | Lab 3 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Solution architecture | ARCH | Level 5 | Lab 1, Summative |
| Capacity management | CPMG | Level 5 | Lab 1 |
| Availability management | AVMT | Level 5 | Lab 4 |
| Systems installation and removal | HSIN | Level 4 | Lab 2 |
| Problem management | PBMG | Level 4–5 | Lab 3 |
| Systems & software life cycle / assurance | SURE | Level 4 | Lab 5 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Security Architecture | Platform & Infrastructure Design | Advanced | Lab 1, Lab 2, Summative |
| Secure Systems | Resilience & Availability | Advanced | Lab 4 |
| Defensive Operations | Monitoring Infrastructure | Advanced | Lab 3, Topic 9 |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-07-K01 | Knowledge of Splunk tier roles and reference topologies at each scale | Topic 1–2; Lab 1 |
| Knowledge | SPL-07-K02 | Knowledge of index clustering, replication/search factors and bucket replication | Topic 3; Lab 2 |
| Knowledge | SPL-07-K03 | Knowledge of search head clustering, captaincy and knowledge-bundle replication | Topic 4; Lab 2 |
| Knowledge | SPL-07-K04 | Knowledge of distributed search execution and its failure modes | Topic 5; Lab 3 |
| Knowledge | SPL-07-K05 | Knowledge of capacity drivers: ingest, retention, concurrency, acceleration | Topic 6; Lab 1 |
| Knowledge | SPL-07-K06 | Knowledge of DR, multi-site clustering and data-residency constraints | Topic 8; Lab 4 |
| Skill | SPL-07-S01 | Skill in producing a capacity model with explicit assumptions | Lab 1 |
| Skill | SPL-07-S02 | Skill in building and recovering an index cluster | Lab 2, Lab 4 |
| Skill | SPL-07-S03 | Skill in structured multi-tier performance diagnosis | Lab 3 |
| Ability | SPL-07-A01 | Ability to defend a sizing decision to a non-technical approver | Lab 1; Summative |
| Ability | SPL-07-A02 | Ability to design for a stated failure tolerance rather than for maximum resilience | Lab 4; Summative |
| Ability | SPL-07-A03 | Ability to plan a migration with a rollback path | Lab 5 |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — Topology and tiers | 1–2 | 1 | 12 |
| B — Clustering | 3–4 | 2 | 18 |
| **C — Distributed search, tuning, troubleshooting (30% of exam)** | 5, 9, 10 | 3 | **32** |
| D — Capacity, sizing and storage | 6–7 | 1, 6 | 20 |
| E — Deployment and change | 8 | 5 | 8 |
| F — Resilience, residency and cloud | 11–12 | 4, 5 | 16 |
| G — Ingest and security architecture | 13–15 | 4, 7 | 16 |
| H — Migration, cost and constraint | 16–17 | 5, 7 | 12 |
| | | | **~134 hours** |

---

## Blueprint alignment

Verified against the published
[Enterprise Certified Architect test blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-architect.pdf),
retrieved 2026-09-09. Twenty domains.

| Domain group | Weight | Covered by |
|---|---|---|
| 1.0–2.0 Deployment plan and process; project requirements | 7% | Topics 2, 6 |
| 3.0 Index design and non-SmartStore storage estimation | 5% | Topics 6, 7 |
| 4.0 Resource planning (sizing, disk, hardware per component, **ES and ITSI sizing**, security/privacy/integrity) | 7% | Topics 1, 6, 14 |
| 5.0 Clustering overview (storage/disk, SHC requirements) | 5% | Topics 3, 4 |
| 6.0 Forwarder and deployment best practices; configuration management | 6% | Topics 8, 13 |
| 7.0 Performance tuning (`limits.conf`, `indexes.conf` bucket size, `props.conf`, search performance) | 5% | Topic 9 |
| **8.0–13.0 Troubleshooting** (diagnostic tools; internal logs and indexes; licensing and crash; input; search and job inspector; forwarding and deployment server) | **30%** | Topic 10 |
| 14.0 Large-scale deployment (server roles in clusters, licence manager in a cluster) | 5% | Topics 1, 2 |
| 15.0–17.0 Single-site and multisite indexer clusters; **cluster management** (storage options, **peer offline and decommission**, **manager app bundles**, **Monitoring Console for clusters**) | 17% | Topics 3, 11 |
| 18.0–19.0 Search head cluster; SHC management (**deployer, captaincy transfer, member add/decommission**) | 10% | Topic 4 |
| 20.0 KV Store collection and lookup management in clusters | 3% | Topic 4 |

!!! warning "Troubleshooting is 30% of this exam"
    Domains 8.0–13.0 together carry **30%** — more than clustering, more than sizing. One
    of the four mandatory prerequisite courses is `Troubleshooting Splunk Enterprise`, and
    the weighting confirms it is not a footnote.

    Topic 10 is correspondingly the largest topic in this module. Candidates who prepare
    on architecture and clustering alone are preparing for two thirds of the exam.

!!! note "SmartStore is *not* the emphasis"
    The blueprint twice specifies **non-SmartStore** storage estimation (domains 3.2 and
    5.1). Topic 7 covers SmartStore because it is a real and increasingly common
    architectural choice, but a candidate should size the conventional way for the exam.

**Beyond the blueprint** — Topics 12 (residency and cloud), 15 (designing the detection
capability) and 17 (cost and constraint) are not examined. They are included because they
are what the role actually requires in an Australian context, and Topic 15 addresses the
separate [Cybersecurity Defense Architect](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-architect.html)
credential.

---

## Topics

### Topic 1: The Tiers, Separated

Forwarding, indexing, search and management tiers as distinct roles with distinct resource
profiles. Which tier is CPU-bound, which is I/O-bound, and why that determines hardware
choice rather than the other way round. Reference hardware, and why "reference" is a floor
and not a target.

The management components learners rarely meet before this rung: **cluster manager**,
**deployer**, **deployment server**, **licence manager**, **Monitoring Console**, **KV Store
members**. What each one does, what breaks when it is unavailable, and — a favourite exam
theme — which of them can safely be co-located and which cannot.

### Topic 2: Reference Topologies and Splunk Validated Architectures

Single instance → distributed non-clustered → indexer cluster → search head cluster →
multi-site. What drives each transition, expressed as a threshold rather than a preference:
ingest volume, search concurrency, availability requirement, geography.

**Splunk Validated Architectures (SVAs)**: the published topology categories, the pillars
(availability, performance, scalability, security, manageability), and how to select a
topology from stated requirements rather than from ambition.

**The architectural judgement:** every step up buys something and costs operational
complexity. An organisation running a multi-site cluster it does not need has bought a
harder job. Being able to say "you do not need this yet" is an architect skill, and one the
vendor's own courseware has no incentive to teach.

### Topic 3: Index Clustering

Cluster manager, peers, and the mechanics of bucket replication. **Replication factor**
(how many copies of the data) and **search factor** (how many are searchable), and the
storage multiple each implies.

Bucket states — searchable, non-searchable, primary — and the fix-up process. What happens
when a peer fails: which buckets go non-searchable, how the cluster remediates, and how
long it takes. Rolling restarts, maintenance mode, and the cluster bundle
(`apply cluster-bundle`) as the configuration path.

Indexer discovery so forwarders find peers without a static list. Data rebalancing after a
peer is added.

**Cluster management and administration** (examined at 7%): storage utilisation options,
**taking a peer offline versus decommissioning it** and why the distinction matters to
bucket fix-up, **manager app bundles** as the configuration path, and using the
**Monitoring Console in an indexer-cluster environment**.

**The decision to teach properly:** RF and SF are a statement about how much data loss and
search unavailability the business accepts, priced in storage. RF=3/SF=2 is not "more safe" —
it is a specific cost for a specific tolerance, traceable to a requirement someone signed.

### Topic 4: Search Head Clustering

Captain election, what the captain does, and captaincy transfer — including the failure
mode where a cluster cannot elect one.

**Knowledge-bundle replication** — the mechanism by which the knowledge layer from
[SPL-02](spl-02-power-user.md) reaches the indexers, and a common source of both
performance problems (oversized bundles, and the `distsearch.conf` blacklist that fixes
them) and correctness problems (stale bundles).

The **deployer** versus the **deployment server**: two similarly-named components doing
different jobs, and a reliable source of confusion. Configuration management for a search
head cluster, and why you must not edit a member directly. Search head cluster member
replacement and recovery.

KV Store clustering and its own quorum behaviour, which fails independently of the search
head cluster and surprises people.

### Topic 5: Distributed Search

How a search is decomposed and distributed: what runs on the indexers (streaming) and what
runs on the search head (transforming) — the [SPL-01](spl-01-core-user.md) Topic 5
distinction, now with a network between the two and real consequences.

Search peers, `distsearch.conf`, and search head pooling history. Search concurrency limits,
scheduler behaviour, skipped searches, and why the scheduler is usually the first thing to
break at scale.

**Federated search** for querying across deployments, and its constraints.

### Topic 6: Capacity Planning and Sizing

The module's centrepiece and the deliverable that defines the role.

Inputs to the model: daily ingest volume, growth rate, **compression and indexing overhead
ratios** (raw versus `tsidx` versus total on disk), retention by index, replication and
search factors, search concurrency (scheduled and ad hoc), data-model acceleration load (the
cost from [SPL-02](spl-02-power-user.md) Topic 14, now at estate scale), and premium app
overhead — **Enterprise Security is sized separately and substantially**, per
[SPL-04](spl-04-enterprise-security.md) Topic 12.

Outputs: indexer count, storage by tier, search head count, IOPS requirements, and network
between tiers.

**Assumptions are the deliverable.** A sizing with an unstated compression ratio, an
unstated peak-to-average ratio or an unstated concurrency assumption is not reviewable.
Learners must produce a model someone else can disagree with — every number traceable to a
stated input.

Cover the reality that ingest estimates from stakeholders are consistently wrong, usually
low, and that the model must include headroom and a re-forecast trigger.

### Topic 7: Storage Architecture and SmartStore

Storage tiers and their performance requirements: hot on the fastest storage available,
warm, cold on cheaper media, frozen off-platform.

**SmartStore**: decoupling compute from storage using object storage, the local cache and
its eviction behaviour, and the workloads for which it is and is not appropriate. The
trade-off is search latency on cache misses against a very different cost curve — and it
changes the sizing model in Topic 6 materially.

Archiving to frozen, `coldToFrozenScript`, and the restore-from-frozen path that
organisations assume works and rarely test.

### Topic 8: Deployment, Configuration Management and Change

Managing configuration across a distributed estate: the deployment server for forwarders,
the deployer for search head clusters, the cluster manager for indexers. Which tool owns
which tier, and the errors that follow from using the wrong one.

Version upgrades and their ordering constraints — upgrade order in a clustered deployment
is not optional and getting it wrong is an outage. Rolling upgrade procedures.

Blast radius again, at architecture scale: a bad push to a cluster is worse than a bad push
to a host. The discipline is the same one
[EXT-ANS](../ansible-security-automation.md) teaches for OS automation.

### Topic 9: Performance Tuning

Reading the platform's own telemetry: `_internal` metrics, queue fill ratios and what a
blocked queue upstream implies about the tier below it, indexing latency, and search
concurrency saturation.

Tuning levers by tier: parsing and typing queue sizing, pipeline sets, indexer parallelism,
search concurrency and quota settings in `limits.conf`, scheduler priority and window
spreading, and workload management to protect interactive searches from scheduled load.

Diagnosing the search that is slow for a *knowledge* reason — an oversized bundle, an
automatic lookup applied estate-wide, an un-accelerated model — rather than a hardware one.

### Topic 10: Structured Troubleshooting at Distributed Scale

The examinable skill, and one of the four mandatory Architect courses.

**The diagnostic method:**

1. Narrow to a tier — forwarding, indexing, search or knowledge?
2. Narrow to a component within it.
3. **Prove it with evidence** — Monitoring Console, job inspector, `_internal`, `btool`,
   `diag` — before changing anything.

Practise the common presentations: slow searches, indexing lag, queue blockage, skipped
scheduled searches, uneven data distribution across peers, bucket fix-up that never
completes, a search head cluster that will not elect a captain, and results that are
*wrong* rather than slow (usually a bundle or precedence problem).

**The blueprint's troubleshooting domains, each examined separately:**

- **Diagnostic resources and tools** (8.0) — `splunk diag`, the Monitoring Console, the
  job inspector, `btool`, and what to collect before opening a support case.
- **Splunk's internal log files and internal indexes** (9.0) — `_internal`, `_audit`,
  `_introspection`, `_telemetry`; `splunkd.log` and its channels; and which log answers
  which question. This is the most examinable single skill in the group.
- **Licensing and crash problems** (10.0) — licence warnings and violations and their
  effect on search; reading a crash log and the common causes (memory, ulimits, disk).
- **Configuration and input problems** (11.0) — data not arriving, arriving twice, or
  arriving wrong; the fishbucket; monitor-input CRC behaviour.
- **Search problems** (12.0) — the job inspector as the primary instrument; skipped and
  queued searches; concurrency limits; and the wrong-results class of failure.
- **Deployment problems** (13.0) — forwarding failures, S2S connectivity, and deployment
  server issues including clients that never phone home.

### Topic 11: Multi-Site, Disaster Recovery and Resilience

Multi-site index clustering: site replication and search factors, site affinity for search,
and forwarder site awareness. The failure scenarios multi-site does and does not protect
against.

RPO and RTO for a log platform, and the observation that "we lost four hours of logs" is a
*detection* outage and potentially a compliance one, not merely an inconvenience.

Backup and recovery of what actually matters: configuration and the knowledge layer, which
are harder to reconstruct than the data. Cluster manager loss and recovery. Testing the
recovery path rather than documenting it.

### Topic 12: Data Residency, Cloud and Splunk Cloud

**Data residency** as a hard architectural constraint for Australian workloads — see
[Australian context](#australian-context). Where buckets physically live is a design input,
not a deployment detail, and it can rule out topologies that are otherwise optimal.

Splunk Cloud versus self-managed: what the architect still owns in each model, what changes
about configuration management, and the migration path. Hybrid deployments and their
particular awkwardness.

Deploying on cloud infrastructure: instance sizing, storage classes, availability zones as a
site analogue, and the cost model that differs from on-premises in ways that surprise
finance.

### Topic 13: Designing the Data Onboarding Architecture

Not "how do I onboard a source" (that is [SPL-06](spl-06-enterprise-admin.md)) but "how does
this organisation onboard sources at scale, repeatably". Ingest patterns: forwarder,
syslog collection tier, HEC, API pull, cloud-native.

The syslog problem specifically — UDP loss, the need for a collection tier, and the common
architecture using a syslog daemon writing to files monitored by a forwarder rather than
Splunk receiving syslog directly.

Ingest actions and edge processing as filtering options, and where filtering should happen
in the pipeline.

### Topic 14: The Security Architecture of the Platform Itself

The platform holding the organisation's security telemetry is itself a target — a
high-value one, because it contains both the evidence of intrusion and the means to
suppress it.

- **Hardening the deployment:** TLS between all tiers, certificate management and rotation,
  authentication integration, and the management ports that should not be reachable.
- **The insider and integrity problem:** an administrator can alter retention, drop data at
  a heavy forwarder, or edit a knowledge object so a detection silently returns nothing.
  Splunk's own audit logging, and the uncomfortable question of who watches it. Compare the
  control-plane threat model in [EXT-ANS](../ansible-security-automation.md) Topic 13 — the
  same argument applies here and matters more.
- **Segregation of duties** between platform administration and detection content ownership,
  which the RBAC model from [SPL-06](spl-06-enterprise-admin.md) Topic 9 must actually
  enforce.
- Data-at-rest and data-in-transit protection, and their performance cost.

### Topic 15: Designing the Detection Capability

The [Cybersecurity Defense Architect](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-architect.html)
layer, and the direct application of
[SE04](../../../degrees/strategic/security-engineering/SE04-detection-response-engineering.md).

Designing the security capability rather than just the platform: data-source coverage
against detection requirements, where detection runs, how content is promoted to
production, how ES and SOAR fit the topology, and how the whole thing degrades when a tier
is lost.

**The architect's version of the two-gap distinction:** which detection requirements are
unmet because of missing content, and which because the architecture never collects the
telemetry. The second is an architecture problem and it is the architect's to fix.

### Topic 16: Migration and Consolidation

Migration patterns: version upgrades, single-site to multi-site, self-managed to Splunk
Cloud, and the consolidation of multiple deployments after an acquisition — the last being
common and messy.

Data migration constraints, index compatibility, and knowledge-object portability. The
recurring problem: the knowledge layer is what makes the data useful, and it is the part
that migrates worst.

**Rollback planning at each stage**, and identifying the point of no return honestly. A
migration plan without a stated point of no return has one anyway — it is just undocumented.

### Topic 17: Cost, Constraint and the Design That Fits

The topic vendor courseware omits. Real Australian organisations outside the largest
enterprises cannot fund the reference architecture. An architect who can only design the
ideal deployment is not useful here.

Designing within a budget ceiling: which pillar to sacrifice first, what to defer, what to
accept as residual risk, and how to state that clearly enough that the business can
genuinely choose. Licensing models as an architectural input rather than a procurement
afterthought.

**Presenting a design to someone who does not want to pay for it** — the skill that decides
whether the design ever gets built. Developed further in [SPL-08](spl-08-consultant.md).

---

## Labs & exercises

!!! tip "Lab guide: how to actually run these"
    **[SPL-07 lab guide](../../../labs/guides/spl-07.md)** gives the setup, the commands and the
    verification for every lab below — against the
    **[lab environment](../../../labs/README.md)**, a reproducible synthetic estate of
    ~101k labelled events with ground truth, so you can measure a real positive
    predictive value rather than estimate one.

    The split of responsibility: **this page says why each lab exists and what to
    deliver; the guide says how to run it.** Marking criteria stay here.

    Labs 1, 5, 6 and 7 need no licence at all and feed the other three — do them first. The guide's capacity model is worked end to end, so the cluster labs can be built to a number rather than to a guess.

    Self-assess with the **[52-question quiz](quiz.md)**.

!!! danger "All labs require a trial licence and multiple instances"
    **Splunk Free has no distributed search and no clustering** — none of these labs can
    run on it. Provision a trial and run the whole module as one continuous block inside
    the trial window. Starting the trial before you are ready to commit the time is the
    most common avoidable mistake in this series.

    Containers or VMs on a single host are sufficient for Labs 2–4. Lab 1 is a paper
    exercise and needs no licence at all — **do it first**.

Observe the [series safety rules](index.md#safety-authorisation-and-data-handling).

### Lab 1: Size a Deployment — *no licence required*

Given a scenario: stated daily ingest, growth rate, retention obligations per data class,
search concurrency, an ES deployment, and an availability requirement — produce a capacity
model and a topology recommendation.

Then present it in **two forms**: the technical model, and a one-page justification for a
finance approver who will ask why it cannot be half the size.

**Deliverable:** the model with every assumption stated and traceable, the topology, and
the one-pager. Marked on defensibility, not on arriving at a particular number. A model
with hidden assumptions fails regardless of whether its answer is right.

### Lab 2: Build an Index Cluster and a Search Head Cluster

Stand up a cluster manager, three peers, and a search head cluster with a deployer. Set
RF and SF deliberately and verify replication actually occurred.

**Deliverable:** the working cluster, evidence of bucket replication, and a statement of
the storage multiple your RF/SF choice implies against the raw ingest figure.

### Lab 3: Structured Diagnosis of a Broken Deployment

Presented with a deployment exhibiting a performance or correctness fault (injected by an
instructor, or self-injected from a provided fault list), diagnose it using the Topic 5
method.

Run at least three faults across different tiers, including **one where the results are
wrong rather than slow**.

**Deliverable:** for each fault, a diagnosis log showing the evidence gathered at each
step. Marked on **method, not on speed** — a lucky guess with no evidence trail scores
zero. This is the closest lab to what the Architect exam actually assesses.

### Lab 4: Fail It

With the Lab 2 cluster running and searches executing: kill an indexer peer mid-search.
Kill the search head captain. Kill the cluster manager. For each, record what the user
experienced, what the cluster did, how long remediation took, and what was lost.

Then repeat with a different RF/SF and compare.

**Deliverable:** a failure-mode table, plus a recommendation on RF/SF for a stated business
tolerance — with the cost multiple attached. Designing for maximum resilience regardless
of requirement is marked down as an architecture failure, not rewarded as caution.

### Lab 5: Plan a Migration

Given an existing single-site deployment and a requirement to move to multi-site with a
data-residency constraint, produce a migration plan: sequencing, upgrade ordering,
validation gates, and a **rollback path at each stage**.

**Deliverable:** the plan, plus an explicit statement of the point of no return and what
mitigates it.

---

### Lab 6: Storage Architecture and the SmartStore Trade-off — *no licence required*

Take the Lab 1 capacity model. Re-cost it three ways: all-local storage with conventional
tiering; SmartStore with object storage and a local cache; and a hybrid.

**Deliverable:** the three cost models with their assumptions, a search-latency assessment
for each, and a recommendation tied to a stated workload profile. State explicitly which
workloads would be *worse* under SmartStore and why.

### Lab 7: Design the Detection Capability, Not Just the Platform

Given a set of detection requirements and an ATT&CK coverage target, design the
architecture that supports them: data sources and their ingest paths, where ES and SOAR
sit, where detection executes, and how content reaches production.

Then identify which requirements cannot be met by *any* content because the architecture
does not collect the telemetry.

**Deliverable:** the capability architecture, the ingest design, and the architecture-level
telemetry-gap statement with the cost of closing each gap. This is the
[Cybersecurity Defense Architect](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-architect.html)
deliverable.

---

## Assessment

### Formative 1: Which Tier Is Lying?

Six symptom descriptions from a distributed deployment. For each, name the most probable
tier and the *first* piece of evidence you would gather. Assesses diagnostic instinct
before method is applied.

### Formative 2: Challenge the Sizing

Given a capacity model containing at least two unsound assumptions, identify them and
state what you would need to know to correct them. Assesses the review skill an architect
is paid for.

### Summative: Architecture Design Package

For a described Australian organisation with stated ingest, retention obligations, an
availability requirement, a data-residency constraint and a budget ceiling:

1. Topology design with justification for each tier decision.
2. Capacity model with all assumptions stated.
3. RF/SF recommendation traced to a business tolerance, with cost impact.
4. DR design with RPO/RTO.
5. Platform security architecture (Topic 9), including the insider-integrity control.
6. A migration or build plan with rollback paths.
7. **A statement of what the design does not do** and the residual risk accepted.

Item 7 carries disproportionate weight. A design presented as having no trade-offs is
either dishonest or not understood, and the same standard applies in
[SE06](../../../degrees/strategic/security-engineering/SE06-capstone-architecture-design.md).

---

## Australian context

Architecture is where Australian regulatory constraints stop being advisory and start
eliminating design options.

- **Data sovereignty and residency.** For Australian Government workloads and
  IRAP-assessed environments, *where indexed data physically resides* is a design input
  that can rule out otherwise-optimal topologies — including some multi-site and cloud
  configurations. The **Hosting Certification Framework** constrains which providers and
  facilities are acceptable for government hosting. Decide residency before topology, not
  after.
- **ASD Information Security Manual and IRAP.** An IRAP assessment will examine the
  monitoring platform itself: its hardening, its access control, its audit trail, and its
  segregation of duties. Topic 9 is not optional content for government-adjacent work.
- **Essential Eight** monitoring maturity drives ingest volume, which drives capacity,
  which drives cost. Learners should be able to trace a control requirement all the way to
  an indexer count — that chain is exactly what an architect is asked to justify.
- **SOCI Act 2018 (Cth).** Responsible entities for critical infrastructure assets have
  risk-management-program obligations covering availability and resilience of systems
  their security depends on. A log platform's RPO/RTO is in scope, and "we lost four hours
  of logs" may be a reportable degradation of a security control.
- **APRA CPS 234 and CPS 230.** Regulated financial entities must maintain information
  security capability proportionate to threat, and manage operational risk in critical
  operations — both bear directly on availability design and on third-party/cloud
  arrangements for a security-critical platform.
- **Privacy Act 1988 (Cth).** Replication multiplies copies of personal information across
  sites and jurisdictions. An RF=3 multi-site design is a decision to hold six copies of
  whatever personal information the logs contain, in more than one place. That is a
  privacy design decision, and APP 11 applies to every copy.
- **Cost is a real constraint and pretending otherwise is not rigour.** Australian
  organisations outside the largest enterprises routinely cannot fund the reference
  architecture. An architect who can only design the ideal deployment is not useful here.
  Designing a defensible deployment *within* a budget ceiling — and stating the residual
  risk plainly — is the actual job, and it is what the summative assesses.

Governance framing for these obligations sits in
[SC01](../../../core/units/SC01-risk-management-frameworks.md),
[SC03](../../../core/units/SC03-governance-policy-compliance.md) and
[F05](../../../core/units/F05-legal-ethics-compliance.md).

---

## Verification status

- **Verified 2026-09-09:** all exam facts above, against the linked official page —
  Expert level, 90 minutes, 85 questions, US$130, Pearson VUE; **both** prerequisite
  certifications; **all four** mandatory courses.
- **Verified 2026-09-09** (from the [Architect track flowchart](https://www.splunk.com/en_us/pdfs/training/splunk-enterprise-certified-architect-track.pdf)):
  the four courses are required to qualify for exam registration, and a candidate who is
  already Enterprise Certified Admin and has completed them **automatically receives exam
  authorisation within 5–7 business days of receiving passing lab results**. The flowchart
  also names Core Certified Consultant as the recommended next step.
- **Verified 2026-09-09:** Cybersecurity Defense Architect exam facts (Expert, 75 minutes,
  67 questions, US$130, Pearson VUE, no published prerequisites).
- **Not verified:** the exam code is not published and is deliberately not stated.
  Instructor-led course pricing varies by region and is deliberately not quoted. Topic coverage **has now been reconciled against the published test blueprint** — see
  [Blueprint alignment](#blueprint-alignment). Sub-objective wording is not reproduced;
  the mapping uses domain titles and weightings only.
- **Flagged:** the Cybersecurity Defense Architect page publishes **no** prerequisites
  despite sitting above Analyst and Engineer in the marketing sequence. Confirm whether an
  unpublished gate exists before advising a learner on that track.
- **Requires a currently-certified reviewer.** Clustering mechanics, fix-up behaviour and
  sizing heuristics change between Splunk versions. This module must not reach
  Practitioner Approved without review by someone holding a **current** Enterprise
  Certified Architect certification.
- Framework mappings and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [Enterprise Certified Architect track](https://www.splunk.com/en_us/training/certification-track/splunk-enterprise-certified-architect.html) — official exam page and test blueprint.
- [Architect track flowchart (PDF)](https://www.splunk.com/en_us/pdfs/training/splunk-enterprise-certified-architect-track.pdf) — the source for the automatic-authorisation rule.
- [Distributed Deployment Manual](https://docs.splunk.com/Documentation/Splunk/latest/Deploy/Distributedoverview) — Topics 1, 2 and 5.
- [Managing Indexers and Clusters of Indexers](https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Aboutclusters) — Topic 3.
- [Distributed Search Manual](https://docs.splunk.com/Documentation/Splunk/latest/DistSearch/AboutSHC) — Topic 4, search head clustering.
- [Capacity Planning Manual](https://docs.splunk.com/Documentation/Splunk/latest/Capacity/Summaryofperformancerecommendations) — Topic 6, the authoritative sizing reference.
- [Troubleshooting Manual](https://docs.splunk.com/Documentation/Splunk/latest/Troubleshooting/WelcometoSplunkEnterpriseTroubleshooting) — Topic 5.
- [Securing Splunk Enterprise](https://docs.splunk.com/Documentation/Splunk/latest/Security/Whatyoucansecure) — Topic 9.
- [Cybersecurity Defense Architect track](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-architect.html) — the parallel security-architecture credential.
- [ASD Information Security Manual](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/ism) and [Hosting Certification Framework](https://www.hostingcertification.gov.au/) — the residency and assurance constraints in Topic 8.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-07 |
| Module Title | Architecture & Deployment — Splunk Enterprise Certified Architect |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 4–6 (Analyse / Evaluate / Create) |
| Notional Hours | ~134 |
| Zero-cost achievable | **No** — mandatory paid coursework; clustering labs require a trial licence |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
