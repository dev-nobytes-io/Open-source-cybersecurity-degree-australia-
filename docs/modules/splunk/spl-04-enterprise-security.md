# SPL-04: Enterprise Security Engineering — Building and Running Splunk ES

> **Part of:** [EXT-SPL — The Splunk Series](index.md)
> **Status:** Draft · **Version:** v0.1 · **Last Reviewed:** 2026-09-09
> **Domain Expert:** _Unassigned_ · **Practitioner Reviewer:** _Unassigned_

!!! warning "Non-credit, vendor-specific"
    See the [series index](index.md) for the R3 carve-out. Nothing here satisfies a
    core-unit requirement.

---

## Target certifications

This module has an unusual credential situation and the series is explicit about it.

| Field | ES Certified Admin **(Legacy)** | Cybersecurity Defense Engineer |
|---|---|---|
| Official page | [link](https://www.splunk.com/en_us/training/certification-track/splunk-es-certified-admin.html) | [link](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-engineer.html) |
| Status | **Legacy Certification** | Current |
| Level | Professional | Professional |
| Prerequisite certification | None listed | **None published** |
| Prerequisite coursework | None specified | None published |
| Length | 60 minutes | 75 minutes |
| Format | 48 multiple choice questions | 60 multiple choice questions |
| Price | US$130 per attempt | US$130 per attempt |
| Delivery | Pearson VUE | Pearson VUE |

*All facts verified 2026-09-09.*

!!! danger "ES Certified Admin is a Legacy Certification — do not target it"
    Splunk introduced a **Legacy Certification** category on **1 January 2026**. Legacy
    credentials remain valid and are still recognised, but they are **no longer updated
    with product releases**. `Splunk Enterprise Security Certified Admin` is one of them.

    **Practical advice:** a learner starting today should target the
    **Cybersecurity Defense Engineer** credential, not the legacy ES Admin exam. Splunk's
    page does not name a direct replacement, so this is the series' reading of the
    situation, not a Splunk statement — see [Verification status](#verification-status).

    **The content in this module is not legacy.** ES is the product Australian SOCs
    actually run. Teach it regardless of which exam a learner sits.

!!! warning "Recertification policy changed"
    From **1 March 2026** Splunk **no longer offers recertification through coursework
    completion**. Certifications operate on a **three-year lifecycle** from the date the
    highest-level certification was achieved. Anyone planning a multi-year certification
    path needs to know this before they start, not after.

**Zero-cost achievable: no.** Enterprise Security is a **premium app** and is not
available on the Splunk Free licence. This module requires a trial licence throughout.


!!! warning "ES 8 renamed this vocabulary — verified 2026-09-09"
    Splunk Enterprise Security 8 uses **detection** (was correlation search), **finding**
    (was notable) and **intermediate finding** (was risk event / risk notable), and
    `entity` / `entity_type` in the `risk` index (was `risk_object` /
    `risk_object_type`). This module still uses the pre-ES 8 vocabulary throughout,
    because that is what the exam blueprints and most published material use.

    [SPL-09](spl-09-detection-analytics.md) uses the ES 8 terms and carries the full
    mapping table. **Check field names against your ES version before copying any SPL.**

!!! danger "Splunk UBA is End of Sale — verified 2026-09-09"
    The standalone **Splunk UBA** appliance reached **End of Sale in December 2025** and
    **End of Support in January 2027**. UEBA capability is now native to **ES Premier**.

    Teach the *methods*, not the product — they survive the transition and can be
    explained to an analyst. [SPL-09](spl-09-detection-analytics.md) Part D develops them
    (Mahalanobis distance, PCA peer groups, spectral graph methods, heat-kernel risk
    propagation).

---

## Overview

[SPL-03](spl-03-cyber-defense-analyst.md) taught you to *use* Enterprise Security as an
analyst. This module is about **building and running it** — the engineering role that sits
between the platform administrator and the SOC analyst, and the one most Australian
organisations under-staff.

The distinction matters. An analyst asks "is this notable real?". An ES engineer asks
"why does this correlation search produce forty notables a night, why is the Asset &
Identity framework six months stale, why did the data model acceleration fall behind, and
why is the threat-intelligence framework silently dropping half its feed?" Those are
different jobs, and the second one is where ES deployments live or die.

Three themes.

**ES is an application with a dependency stack, and every layer can fail silently.** Data
→ CIM compliance → data models → acceleration → correlation searches → notables → risk.
A break anywhere upstream produces *no error* downstream, just fewer results. Diagnosing
which layer broke is the core engineering skill, and it is the same evidence-first method
[SPL-07](spl-07-architect.md) applies to the platform.

**ES is expensive in a way that shapes architecture.** ES drives data-model acceleration
across the whole CIM, which is a standing load on the indexing tier. Sizing an ES
deployment is not sizing Splunk plus a bit — it is a materially different capacity model,
which is why [SPL-07](spl-07-architect.md) treats it as a separate input.

**Content management is a software-delivery problem.** Correlation searches, risk rules,
lookups and dashboards are code. They need version control, a test path, a promotion
route from dev to production, and a way to tell when one has silently stopped working.
Most ES deployments manage them by editing production directly, which is exactly as bad as
it sounds.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [SPL-02](spl-02-power-user.md) | **Hard prerequisite.** ES runs entirely on CIM data models. Without SPL-02 the failures in this module are unreadable. |
| [SPL-03](spl-03-cyber-defense-analyst.md) | **Direct predecessor.** SPL-03 is the analyst view; SPL-04 is the engineer view of the same product. |
| [SE04 — Detection & Response Engineering](../../../degrees/strategic/security-engineering/SE04-detection-response-engineering.md) | **The core unit this applies.** SE04 teaches detection and response engineering vendor-neutrally. |
| [DE05 — Detection Operations & Management](../../../degrees/operational/detection-engineering/DE05-detection-operations-management.md) | **Directly relevant.** Content lifecycle, alert quality and tuning debt are DE05's subject; this is the ES implementation. |
| [DE06 — Capstone: Detection Library](../../../degrees/operational/detection-engineering/DE06-capstone-detection-library.md) | The detection-as-code discipline applied to ES content. |
| [SPL-05](spl-05-soar.md) | **Direct successor.** Adaptive response actions in ES are the handoff point into SOAR. |
| [SPL-06](spl-06-enterprise-admin.md) | Platform administration underneath ES; the two are often the same person and should not be. |

---

## Learning outcomes

On completion, a learner can:

1. **Install**, configure and validate an Enterprise Security deployment, including its
   data-model acceleration and index requirements.
2. **Diagnose** a failure anywhere in the ES dependency stack and identify the layer at
   fault with evidence.
3. **Configure** the Asset & Identity framework and **evaluate** the maintenance process
   that keeps it accurate.
4. **Build** and **tune** correlation searches, adaptive response actions and risk rules
   against measured false-positive rates.
5. **Design** a risk-based alerting model end to end, including risk factors and
   attribution.
6. **Implement** a content lifecycle — version control, test path, promotion, and
   detection of silent failure.
7. **Assess** ES capacity impact and **justify** the acceleration configuration chosen.

> Bloom's 3–6.

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0166 | Engineer correlation and automated response | Lab 3, Lab 4, Lab 5 |
| 2023 | Cyber Defense Infrastructure Support | PR-INF-001 | T0335 | Build and maintain monitoring-system content and infrastructure | Lab 1, Lab 2 |
| 2023 | Security Architect | SP-ARC-002 | T0050 | Design security architecture and supporting infrastructure | Lab 7 |
| 2023 | Systems Developer | SP-SYS-002 | T0014 | Design and develop data structures and content | Lab 6 |
| 2023 | Threat/Warning Analyst | AN-TWA-001 | T0748 | Monitor and report adversary activity and trends | Lab 2 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Security operations | SCAD | Level 4–5 | Lab 3, Lab 4 |
| Systems installation and removal | HSIN | Level 4 | Lab 1 |
| Configuration management | CFMG | Level 4 | Lab 6 |
| Release and deployment | RELM | Level 4 | Lab 6 |
| Data management | DATM | Level 4 | Lab 2 |
| Capacity management | CPMG | Level 4 | Lab 7 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Defensive Operations | Detection Engineering | Advanced | Lab 3, Lab 4 |
| Defensive Operations | Monitoring Infrastructure | Practitioner–Advanced | Lab 1, Lab 7 |
| Secure Systems | Data Engineering & Normalisation | Advanced | Lab 2 |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-04-K01 | Knowledge of the ES dependency stack and its silent-failure modes | Topic 2; Lab 2 |
| Knowledge | SPL-04-K02 | Knowledge of ES installation, index and acceleration requirements | Topic 1; Lab 1 |
| Knowledge | SPL-04-K03 | Knowledge of the Asset & Identity framework and its data sources | Topic 4; Lab 2 |
| Knowledge | SPL-04-K04 | Knowledge of correlation search anatomy and adaptive response | Topic 5–6; Lab 3 |
| Knowledge | SPL-04-K05 | Knowledge of the risk framework: risk objects, factors, attribution | Topic 7; Lab 4 |
| Knowledge | SPL-04-K06 | Knowledge of the threat-intelligence framework and its failure modes | Topic 8; Lab 5 |
| Knowledge | SPL-04-K07 | Knowledge of ES capacity impact and acceleration cost | Topic 12; Lab 7 |
| Skill | SPL-04-S01 | Skill in installing and validating an ES deployment | Lab 1 |
| Skill | SPL-04-S02 | Skill in diagnosing a break in the ES dependency stack | Lab 2 |
| Skill | SPL-04-S03 | Skill in authoring and tuning correlation searches with adaptive response | Lab 3 |
| Skill | SPL-04-S04 | Skill in implementing an ES content lifecycle under version control | Lab 6 |
| Ability | SPL-04-A01 | Ability to distinguish a content problem from a data problem | Lab 2; Formative 2 |
| Ability | SPL-04-A02 | Ability to keep asset and identity data accurate as a sustained process | Lab 2; Summative |
| Ability | SPL-04-A03 | Ability to justify ES acceleration configuration against its indexer cost | Lab 7; Summative |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — Deploying ES | 1–3 | 1 | 12 |
| B — The frameworks | 4, 8, 9 | 2, 5 | 14 |
| C — Detection content | 5–6, 10 | 3, 6 | 16 |
| D — Risk-based alerting | 7 | 4 | 10 |
| E — Advanced analytics | 11 | — | 6 |
| F — Capacity and operations | 12–13 | 7 | 12 |
| G — Glass tables, forensics and add-ons | 14 | 8 | 10 |
| | | | **~80 hours** |

---

## Blueprint alignment

Two blueprints apply, and together they justify this module's shape.

**[Cybersecurity Defense Engineer](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-cybersecurity-defense-engineer.pdf)**
(current credential, retrieved 2026-09-09) — five domains:

| Domain | Weight | Covered by |
|---|---|---|
| 1.0 Data engineering (data review and analysis, performant indexing, normalisation) | 10% | Topic 2, [SPL-02](spl-02-power-user.md) |
| 2.0 **Detection engineering** (create and tune correlation searches; incorporate context; risk-based modifiers; effective notables/findings; **detection lifecycle**) | **40%** | Topics 5–7, 10 |
| 3.0 Building security processes and programs (threat intelligence; risk and detection prioritisation; **documentation and SOPs**) | 20% | Topics 8, 13 |
| 4.0 **Automation and efficiency** (automation for SOPs; case management; **REST APIs**; **SOAR playbooks**; comparing ES and SOAR integration) | **20%** | Topic 6, [SPL-05](spl-05-soar.md) |
| 5.0 Auditing and reporting (security metrics; security reports; program dashboards) | 10% | Topic 13 |

**[ES Certified Admin (Legacy)](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-es-admin.pdf)**
— twelve domains, still the most precise published description of ES administration:

| Domain | Weight | Covered by |
|---|---|---|
| 1.0 ES introduction | 5% | Topic 1 |
| 2.0 Monitoring and investigation (security posture, incident review, notable management, investigations) | 10% | Topic 9, [SPL-03](spl-03-cyber-defense-analyst.md) |
| 3.0 Security intelligence tools | 5% | Topic 8 |
| 4.0 **Forensics, glass tables and navigation control** | 10% | Topic 14 |
| 5.0 ES deployment (topologies, checklist, indexing strategy, ES data models) | 10% | Topics 1–2 |
| 6.0 **Installation and configuration** (prepare environment, install on a search head, ES accounts and roles, post-install tasks) | **15%** | Topics 1, 3 |
| 7.0 Validating ES data (plan inputs, configure technology add-ons) | 10% | Topic 2 |
| 8.0 **Custom add-ons (Add-on Builder)** | 5% | Topic 14 |
| 9.0 Tuning correlation searches (scheduling and sensitivity) | 10% | Topic 5 |
| 10.0 Creating correlation searches (custom searches, adaptive responses, **search export/import**) | 10% | Topics 5–6, 10 |
| 11.0 Lookups and identity management (ES-specific lookups, lookup lists) | 5% | Topic 4 |
| 12.0 Threat intelligence framework; **user activity analysis** | 5% | Topic 8 |

!!! success "Detection engineering is 40% of the current credential"
    The CD Engineer blueprint puts **40%** on creating, tuning and maintaining detections —
    and names the **detection lifecycle** explicitly (domain 2.5). Topic 10's treatment of
    content as software delivery is not editorialising; it is the largest examined domain.

    Note also that domain 4.0 (20%) is **automation** — SOAR playbooks, REST APIs and case
    management. [SPL-05](spl-05-soar.md) is not optional for this credential.

---

## Topics

### Topic 1: Installing and Validating ES

ES as a premium app with real prerequisites: supported Splunk versions, search-head
requirements, the indexes it creates (`notable`, `risk`, `threat_activity`,
`endpoint_summary` and others), and the technology add-ons it depends on.

Installation on a single search head versus a search head cluster — the deployer path,
and why ES on a SHC is meaningfully harder than the documentation implies. Post-install
validation: confirming data models populate, acceleration completes, and the essential
dashboards return data.

### Topic 2: The Dependency Stack and Silent Failure

The module's organising diagnostic. Every ES capability rests on the layer below it:

```
raw data → sourcetype/parsing → CIM compliance (TAs) → data models
        → acceleration → correlation searches → notables → risk → dashboards
```

Working the stack downward when something is empty. `| datamodel` and `| tstats` against a
model to prove population; the data-model audit dashboards; acceleration status and
backfill; `| rest` for content inventory.

**The examinable instinct:** an empty ES dashboard almost never means "ES is broken". It
means a layer beneath it is empty, and there is a specific search that proves which one.

### Topic 3: ES Configuration and General Settings

Index and data-model configuration, retention for ES's own indexes, per-panel and global
settings, navigation customisation, permissions for ES roles (`ess_admin`, `ess_analyst`,
`ess_user`), and the correlation-search scheduling window.

Domain configuration: Access, Endpoint, Network, Identity, Threat, Audit — what each
domain expects as input and which dashboards die without it.

### Topic 4: The Asset & Identity Framework

Asset and identity lookups, their expected fields, and the merge process that produces the
combined lookups ES actually searches. Categories, priorities, `bunit`, and how they feed
notable urgency.

**Sourcing the data:** CMDB, Active Directory, cloud inventory, DHCP — and the fact that
none of them is complete. Automating the refresh, detecting staleness, and handling the
asset that appears in no system of record.

**Why this is the most under-maintained part of every ES deployment:** it has no immediate
failure mode. Stale asset data does not error; it just quietly makes urgency wrong, which
makes triage priority wrong, which wastes analyst time invisibly.

### Topic 5: Correlation Search Anatomy

The full structure: search string, scheduling and cron, time window and the lag problem,
throttling (window duration and fields), the notable-generating adaptive response, and
severity/urgency assignment.

Real-time versus scheduled correlation searches and why scheduled is almost always right.
Search-window drift, missed events at boundaries, and why `earliest`/`latest` on a
scheduled search is a correctness issue rather than a preference.

Writing correlation searches against **data models with `tstats`** rather than raw events —
the performance difference that decides whether a detection can run every five minutes.

### Topic 6: Adaptive Response

The adaptive response framework: what actions ship with ES, what add-ons provide, and how
an action is invoked from a correlation search or manually from Incident Review.

Action types: notable creation, risk modifier, email, ticketing, and the handoff into
[SOAR](spl-05-soar.md). Building a custom adaptive response action.

**The judgement:** which responses may be automatic, which need a human, and the
irreversibility test — the same decision boundary
[EXT-ANS](../ansible-security-automation.md) applies to automation generally. An automated
containment that severs network access is a self-inflicted denial of service if it fires
on a false positive.

### Topic 7: The Risk Framework and Risk-Based Alerting

Risk objects and object types, risk modifiers, the `risk` index, and risk incident rules
that fire on accumulated score.

**Risk factors** — conditional multipliers that raise or lower a score based on context
(the asset's criticality, whether the identity is privileged, time of day). This is what
makes RBA proportionate rather than arithmetic.

Attribution: choosing the right risk object matters more than the score. Attributing to a
host when the story is about a user produces a risk narrative nobody can act on.

Calibration as an ongoing process: baselining the score distribution, setting a threshold
that fires a workable number of times per day, and re-baselining when the estate changes.
Mapping risk events to ATT&CK tactics so that breadth across the kill chain, not just
depth, drives escalation.

### Topic 8: The Threat Intelligence Framework

Threat-intelligence downloads, local intel, and the parsing pipeline that turns a feed into
`threat_*` collections. Supported formats — STIX/TAXII, OpenIOC, CSV — and custom feeds.

Matching: which fields ES compares against which intel type, and where matches surface.

**The failure modes practitioners actually hit:** a feed that stops updating with no alarm,
intel with no expiry filling the KV store, low-quality indicators generating constant
matches, and the absence of any confidence or source weighting. Connects to
[OC05](../../../core/units/OC05-threat-intelligence-fundamentals.md) — a feed you cannot
evaluate is a feed you should not ingest.

### Topic 9: Investigations, Workbench and Case Management

The investigation workbench, artefacts and their expansion, investigation timelines, and
attaching notables and searches to an investigation.

Where ES's case management stops and a real case-management or ticketing system starts —
an honest assessment, because most mature SOCs run ES alongside a ticketing platform rather
than inside it.

### Topic 10: Content Management as Software Delivery

Correlation searches, lookups, macros and dashboards as **code**. Version control for ES
content, the dev → test → production promotion path, and change review.

Splunk Security Content / ESCU as an upstream dependency: adopting, pinning, and adapting
delivered content, and the maintenance cost of content you did not write. Sigma conversion
as an alternative source.

**Detecting silent failure at estate scale:** which correlation searches have not fired in
90 days, which are skipping, which return errors. A detection that silently stopped is
worse than no detection, because it is counted as coverage.

### Topic 11: Advanced Analytics — UEBA and MLTK

Where statistical and machine-learning approaches genuinely help, and where they are sold
harder than they work.

The Machine Learning Toolkit in a security context: outlier detection, forecasting, and
the `anomalydetection`, `cluster` and density-function approaches. Behavioural baselining
with `streamstats` and `eventstats` as the honest low-tech alternative that solves most of
the same problems.

**The critical stance to teach:** an unexplainable alert is an untriageable alert. A model
that flags an account without a human-readable reason produces work, not detection. Judge
these tools by whether an analyst can act on the output.

### Topic 12: ES Capacity and Performance

Why ES changes the sizing conversation: CIM data-model acceleration across every enabled
model is a standing indexer load, correlation searches add scheduled-search concurrency,
and the risk framework adds its own write volume.

Diagnosing ES performance problems: acceleration falling behind, skipped correlation
searches, search concurrency exhaustion, and oversized knowledge bundles.

Tuning levers: which models to accelerate, acceleration time ranges, correlation-search
scheduling spread, and summary-range trade-offs. Feeds directly into
[SPL-07](spl-07-architect.md) Topic 6.

### Topic 13: Upgrades and Operating ES Over Time

ES upgrade planning, content migration, and what customisation survives. Why heavy
in-place customisation of shipped content is a future upgrade problem, and how to layer
customisations so they survive.

Operational health: an ES health-check routine, and the periodic review that catches
asset-data decay, dead detections and acceleration drift before an incident does.

---

### Topic 14: Glass Tables, Forensics Dashboards and Custom Add-ons

The remaining examined ES surface, drawn from the legacy ES Admin blueprint.

**Forensics dashboards** — the per-domain investigative dashboards (Access, Endpoint,
Network, Identity) and what each answers. Distinct from the posture dashboards, and far
more useful to an analyst.

**Glass tables** — ES's service-status visualisation, where you draw a representation of a
business service or control chain and bind live metrics to it. Genuinely valuable for
communicating security posture to non-analysts, and frequently built once and never
maintained. Building one that stays true as the estate changes is the actual skill.

**Navigation and dashboard permissions** — controlling what each ES role sees, which is
both a usability decision and an access-control one.

**Custom add-ons with the Add-on Builder** (domain 8.0): designing an add-on for a data
source with no supported TA — field extractions, CIM mapping, and packaging. This is the
practical answer to the CIM-compliance gap identified in
[SPL-02](spl-02-power-user.md) Lab 2, and it is how an organisation onboards a product
Splunkbase does not cover.

**Search export/import** (domain 10.3) for moving correlation searches between
environments — the manual predecessor to the version-controlled promotion path in Topic 10.

**User activity analysis** (domain 12.2) and where ES's built-in behavioural views sit
relative to the UEBA and MLTK discussion in Topic 11.

---

## Labs & exercises

!!! danger "Trial licence required throughout"
    Enterprise Security is a premium app and does not run on the Splunk Free licence.
    Provision a trial and run this module as a continuous block. Reuse the
    [SPL-07](spl-07-architect.md) environment if you are running both.

Observe the [series safety rules](index.md#safety-authorisation-and-data-handling).

### Lab 1: Deploy and Validate ES

Install ES onto a lab search head. Configure indexes, enable data models, run acceleration,
and validate with evidence that each model populates.

**Deliverable:** a post-install validation report — per data model, the search proving it
is populated, and the acceleration completion state. An install that "looks fine" on the
dashboards but has three empty models fails this lab.

### Lab 2: Diagnose the Dependency Stack

Given an ES deployment with three injected faults at different layers (a broken TA, a
stalled acceleration, and a stale Asset & Identity lookup), diagnose each using the Topic 2
method.

**Deliverable:** for each fault, the layer identified and the specific search that proved
it. Then build the Asset & Identity refresh and staleness-detection process that would
have caught the third fault.

### Lab 3: Build, Tune and Respond

Author a correlation search against a data model using `tstats`. Attach an adaptive
response. Run against data containing both true and benign activity. Measure the
false-positive rate, tune, and measure again.

**Deliverable:** both versions, both measured rates, the throttling configuration and its
justification, and a statement of the sensitivity traded away.

### Lab 4: A Calibrated Risk Model

Build an RBA implementation: risk modifiers across at least ten behaviours, at least two
risk factors, chosen risk objects, and a risk incident rule. Run it and measure how many
incidents fired and how many were worth investigating.

**Deliverable:** the model, the score distribution, and a calibration note adjusting at
least one score or factor you got wrong, with reasoning.

### Lab 5: Threat Intelligence, Including Its Failure

Configure a threat-intelligence feed. Confirm matches surface. Then break it — let the feed
go stale — and build the monitoring that detects a feed which has stopped updating.

**Deliverable:** the working configuration, the staleness detection, and an assessment of
the feed's indicator quality: what fraction produced actionable matches.

### Lab 6: ES Content Under Version Control

Put a set of ES content into version control with a promotion path from a dev instance to
production. Include a test that content behaves as intended before promotion.

**Deliverable:** the repository, the promotion procedure, and a "dead content" report
identifying detections that have not fired and classifying each as broken or genuinely rare.

### Lab 7: Size ES

Given a stated ingest volume, enabled data models, correlation-search count and schedule,
produce the ES capacity impact: additional indexer load from acceleration, search
concurrency required, and storage for summaries and the risk index.

**Deliverable:** the model with assumptions stated, plus a tuning recommendation for a
deployment that is 30% under-provisioned — which models you would stop accelerating and
what detection capability that costs.

---

### Lab 8: Build an Add-on for an Unsupported Source

Take a data source with no Splunkbase TA. Use the Add-on Builder to produce a working
add-on: field extractions, CIM mapping to the correct data model, and eventfmt/packaging.

Validate it the way Lab 2 validates any source — prove the CIM data model populates from
your add-on, not merely that the app installs.

**Deliverable:** the add-on, the CIM validation evidence, and the gap statement listing
every CIM field you could not populate and what telemetry the vendor would have to emit for
you to populate it.

---

## Assessment

### Formative 1: Which Layer Is Empty?

Six symptoms of empty or wrong ES output. For each, name the most probable layer and the
search you would run first to confirm.

### Formative 2: Content Problem or Data Problem?

Given five failing detections, classify each as a content defect, a normalisation defect,
or a telemetry gap — and state what a fix costs in each case. The distinction determines
which team owns it.

### Summative: ES Engineering Package

For a described organisation with an existing ES deployment, stated data sources, a
detection requirement set and a capacity ceiling:

1. Deployment validation report against the dependency stack.
2. Asset & Identity sourcing and maintenance process.
3. A detection content set with measured false-positive rates and throttling.
4. A calibrated risk model with factors and attribution rationale.
5. Threat-intelligence configuration with quality assessment and staleness monitoring.
6. A content lifecycle with version control and dead-content detection.
7. ES capacity impact with a tuning recommendation.
8. **A statement of what this deployment cannot detect, and why.**

Item 8 carries disproportionate weight, and must distinguish detection gaps from telemetry
gaps — the same discipline as [SPL-03](spl-03-cyber-defense-analyst.md) Topic 5.

---

## Australian context

- **ES is frequently bought as a compliance artefact.** ASD **Essential Eight** monitoring
  maturity and **ISM** event-logging expectations drive the purchase; the engineering job
  is to deliver genuine detection *and* the evidence, while being honest that a deployment
  optimised for audit evidence is not automatically one that detects intrusions.
- **Asset criticality is a business-continuity input, not a technical field.** Under the
  **SOCI Act 2018 (Cth)**, responsible entities must understand which assets are critical.
  The Asset & Identity framework is where that determination becomes operational — and
  where a wrong `priority` value silently mis-prioritises real incidents.
- **Risk-based alerting on user risk objects is workplace surveillance.** Scoring a named
  employee's behaviour engages surveillance law (e.g. the NSW *Workplace Surveillance Act
  2005*) and the **Privacy Act 1988 (Cth)**. It needs a documented basis, notice, and a
  retention decision for the risk index — which accumulates a behavioural profile per
  person by design. Treat the risk index as personal information, because it is.
- **Threat intelligence has handling obligations.** Feeds shared under **TLP** restrictions,
  or received through ACSC partnerships, carry redistribution limits that a Splunk lookup
  does not enforce. Who can search the intel collections is a governance decision.
- **APRA CPS 234** regulated entities must be able to demonstrate their security controls
  operate. A dead correlation search counted as coverage is a control failure that an
  audit should catch and usually does not — which is why the Lab 6 dead-content report is
  an assurance artefact, not just hygiene.

---

## Verification status

- **Verified 2026-09-09:** exam facts for both certifications above, against their official
  pages, including that **ES Certified Admin is marked a Legacy Certification** and that
  Cybersecurity Defense Engineer publishes **no prerequisites**.
- **Verified 2026-09-09** (Splunk's certification-changes FAQ): the Legacy Certification
  category was introduced **1 January 2026**; legacy credentials remain valid but are not
  refreshed with product updates. Recertification through coursework completion ends
  **1 March 2026**, and certifications run on a **three-year lifecycle** from the date the
  highest-level certification was achieved.
- **NOT verified — this series' reading, not Splunk's statement:** that Cybersecurity
  Defense Engineer is the intended successor to ES Certified Admin. Splunk's page names no
  replacement. Confirm before advising a learner.
- **Not verified:** exam codes are not published and are deliberately not stated. Topic coverage **has now been reconciled against the published test blueprint** — see
  [Blueprint alignment](#blueprint-alignment). Sub-objective wording is not reproduced;
  the mapping uses domain titles and weightings only. ES feature names and dashboard locations change
  materially between ES versions — this module is **not pinned to an ES version**, which
  must be fixed at review.
- **Requires a currently-practising reviewer** with production ES engineering experience.
- Framework mappings and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [ES Certified Admin track (Legacy)](https://www.splunk.com/en_us/training/certification-track/splunk-es-certified-admin.html) and [Cybersecurity Defense Engineer track](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-engineer.html) — official exam pages.
- [Upcoming Splunk Certification Changes (PDF)](https://www.splunk.com/en_us/pdfs/training/splunk-certification-changes.pdf) — the Legacy Certification category and the recertification policy change.
- [Splunk Recertification Policy](https://www.splunk.com/en_us/training/recertification.html) — the three-year lifecycle.
- [Splunk Enterprise Security documentation](https://docs.splunk.com/Documentation/ES) — the authoritative product reference for every topic here.
- [Splunk Common Information Model](https://docs.splunk.com/Documentation/CIM) — the dependency ES rests on.
- [Splunk Security Content / ESCU](https://research.splunk.com/) — upstream detection content for Topic 10.
- [Splunk free courses](https://www.splunk.com/en_us/training/free-courses.html) — *Introduction to Enterprise Security*, detection engineering and SOC operations courses are free.
- [ACSC Essential Eight Maturity Model](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-maturity-model) — the usual Australian driver behind an ES purchase.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-04 |
| Module Title | Enterprise Security Engineering — Building and Running Splunk ES |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 3–6 (Apply / Analyse / Evaluate / Create) |
| Notional Hours | ~80 |
| Zero-cost achievable | **No** — ES is a premium app; trial licence required throughout |
| Credential note | ES Certified Admin is **Legacy**; target Cybersecurity Defense Engineer instead |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
