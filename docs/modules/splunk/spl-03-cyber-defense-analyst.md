# SPL-03: Enterprise Security & SOC Practice — Cybersecurity Defense Analyst

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
| Certification | [Splunk Certified Cybersecurity Defense Analyst](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-analyst.html) | 2026-09-09 |
| Level | Analyst (intermediate) | 2026-09-09 |
| Prerequisite certification | **None** | 2026-09-09 |
| Prerequisite coursework | **None** | 2026-09-09 |
| Length | 75 minutes | 2026-09-09 |
| Format | 66 multiple choice questions | 2026-09-09 |
| Price | US$130 per attempt | 2026-09-09 |
| Delivery | Pearson VUE | 2026-09-09 |
| Recommended prior knowledge | Power User–level knowledge of Splunk Enterprise (Splunk's own note — recommended, **not** enforced) | 2026-09-09 |

**Zero-cost achievable: partly.** The analytical content runs on Splunk Free. **Enterprise
Security is a separate premium app and is not available on the Free licence** — the ES
half of this module requires a trial. Plan accordingly (see
[lab substrate](index.md#lab-substrate-what-you-can-actually-build)).

!!! success "The gate-free security track"
    The **entire** Cybersecurity Defense track — Analyst, Engineer, Architect — publishes
    **no formal prerequisite certifications**. Compared to the Architect/Consultant track,
    which is the most heavily gated in the portfolio, this is the fastest route to a
    Splunk credential for someone already working in a SOC. For a graduate of the
    [Detection Engineering](../../../degrees/operational/detection-engineering/README.md)
    or [Threat Hunting](../../../degrees/operational/threat-hunting/README.md) major, CDA
    is the highest-value first exam.

    Splunk *recommends* Power User–level knowledge. Take that seriously even though it is
    not enforced: [SPL-02](spl-02-power-user.md) is genuinely assumed here.

---

## Overview

This is the module where the series stops being about a log platform and starts being
about a SOC.

The degree already teaches SOC practice properly:
[OC02](../../../core/units/OC02-security-monitoring-siem.md) for monitoring and SIEM
operation, [OC04](../../../core/units/OC04-incident-response-lifecycle.md) for the
incident lifecycle, [TH01](../../../degrees/operational/threat-hunting/TH01-hunting-methodology-process.md)
for hunting methodology, and the [DE](../../../degrees/operational/detection-engineering/README.md)
major for detection engineering. **SPL-03 does not re-teach any of that.** It teaches how
those disciplines are expressed in Splunk Enterprise Security, and — more usefully — where
the tool's model and the discipline's model disagree.

Three ideas carry the module.

**Notables are not alerts.** ES's correlation searches produce notable events with
ownership, status and disposition. That workflow is a case-management system, and treating
it as a queue of alerts to close is how SOCs end up with a 90% false-positive rate and an
analyst who stops reading them.

**Risk-based alerting is the important idea in modern Splunk.** Instead of alerting on
each suspicious event, RBA attributes risk scores to objects (a user, a host) and alerts
when accumulated risk crosses a threshold. This directly attacks alert fatigue, and it
maps unusually well onto MITRE ATT&CK: individually-weak signals across multiple tactics
aggregate into a strong one. It is also the feature most often deployed badly, because
scoring is a judgement problem disguised as a configuration problem.

**Asset and identity enrichment is what makes any of it work.** An alert on `10.1.4.22`
is not actionable. An alert on *the finance director's laptop* is. ES's Asset & Identity
framework is the lookup problem from [SPL-02](spl-02-power-user.md) promoted to a
first-class capability, and it is usually the least well-maintained part of a real
deployment.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [SPL-02](spl-02-power-user.md) | **Assumed.** CIM compliance is a hard requirement for ES — see the warning below. |
| [OC02 — Security Monitoring & SIEM](../../../core/units/OC02-security-monitoring-siem.md) | **Assumed core unit.** Vendor-neutral SIEM operation, triage and monitoring theory. |
| [OC04 — Incident Response Lifecycle](../../../core/units/OC04-incident-response-lifecycle.md) | **Assumed.** The notable workflow is mapped onto PICERL in Topic 4. |
| [OC01 — Adversary Tradecraft](../../../core/units/OC01-adversary-tradecraft.md), [OC05 — Threat Intelligence](../../../core/units/OC05-threat-intelligence-fundamentals.md) | Threat context and intelligence handling; ES's threat-intelligence framework is the tooling expression of OC05. |
| [TH01 — Hunting Methodology](../../../degrees/operational/threat-hunting/TH01-hunting-methodology-process.md) | **Directly relevant.** TH01 already uses **PEAK**, which is Splunk/SURGe's own framework — see [`docs/maturity-models.md`](../../maturity-models.md). Topic 6 runs PEAK hunts in ES. |
| [DE03](../../../degrees/operational/detection-engineering/DE03-writing-detection-logic.md), [DE05](../../../degrees/operational/detection-engineering/DE05-detection-operations-management.md) | Detection authoring and lifecycle management; correlation searches are the ES form. |
| [SPL-04](spl-04-enterprise-admin.md) | Successor for the platform-administration path. |

!!! danger "ES is only as good as your CIM compliance"
    Enterprise Security is built entirely on CIM data models. **Non-compliant data is
    invisible to ES**, silently. The most common reason a real ES deployment
    underperforms is not tuning — it is that half the data sources were never properly
    normalised. If a learner has not done [SPL-02](spl-02-power-user.md) Lab 2, this
    module will teach them the wrong lesson about why ES "doesn't work".

---

## Learning outcomes

On completion, a learner can:

1. **Apply** the ES notable-event workflow to triage, investigate and dispose of security
   events with defensible reasoning.
2. **Analyse** correlation search logic and **evaluate** its false-positive and
   false-negative behaviour against real data.
3. **Design** a risk-based alerting scheme — risk objects, scores and thresholds — and
   **justify** the scoring decisions.
4. **Evaluate** detection coverage against MITRE ATT&CK and produce an honest gap
   statement distinguishing "not detected" from "not logged".
5. **Conduct** a structured threat hunt using the PEAK framework and convert a finding
   into durable detection content.
6. **Assess** the operational health of a detection estate: alert quality, tuning debt
   and silent failure.

> Bloom's 3–5, consistent with an analyst-level rung and with the operational-layer
> minimum in [`docs/content-standards.md`](../../content-standards.md).

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0258 | Provide timely detection and reporting of anomalous activity | Lab 1, Lab 2 |
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0295 | Analyse identified malicious activity to determine method of exploitation | Lab 2, Lab 5 |
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0166 | Engineer correlation and automated response | Lab 3, Lab 4 |
| 2023 | Cyber Defense Incident Responder | PR-CIR-001 | T0041 | Coordinate and perform incident handling across the lifecycle | Lab 2 |
| 2023 | Threat/Warning Analyst | AN-TWA-001 | T0748 | Monitor and report on adversary activities and trends | Lab 5, Lab 6 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Security operations | SCAD | Level 4 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 4 | Lab 5, Lab 6 |
| Incident management | USUP | Level 3–4 | Lab 2 |
| Conformance review | CORE | Level 3 | Lab 4 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Defensive Operations | Monitoring & Analysis | Practitioner–Advanced | Lab 1, Lab 2 |
| Defensive Operations | Incident Response | Practitioner | Lab 2 |
| Defensive Operations | Threat Hunting | Practitioner | Lab 6 |

### MITRE ATT&CK

Coverage assessment is a **topic** in this module rather than a technique list — Topic 5
and Lab 4 assess a detection estate against the matrix. Technique IDs referenced in lab
material are stated against **v19** for consistency with the rest of the repository, and
both the version pin and specific IDs are **provisional pending Framework Custodian
verification**.

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-03-K01 | Knowledge of the ES notable-event lifecycle and its relationship to case management | Topic 3–4; Lab 1 |
| Knowledge | SPL-03-K02 | Knowledge of risk-based alerting mechanics: risk objects, scores, thresholds | Topic 7; Lab 3 |
| Knowledge | SPL-03-K03 | Knowledge of the Asset & Identity framework and its role in actionability | Topic 2; Lab 1 |
| Knowledge | SPL-03-K04 | Knowledge of ATT&CK-based coverage assessment and its limits | Topic 5; Lab 4 |
| Skill | SPL-03-S01 | Skill in triaging and disposing of notables with recorded reasoning | Lab 1 |
| Skill | SPL-03-S02 | Skill in authoring and tuning correlation searches | Lab 2, Lab 3 |
| Skill | SPL-03-S03 | Skill in conducting a PEAK-structured hunt and productising the result | Lab 6 |
| Ability | SPL-03-A01 | Ability to distinguish a detection gap from a telemetry gap | Lab 4; Summative |
| Ability | SPL-03-A02 | Ability to judge whether an alert should exist at all | Lab 3; Formative 2 |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — ES foundations | 1–2 | 1 | 8 |
| B — Notables and investigation | 3–4 | 1, 2 | 12 |
| C — Detection and coverage | 5–6 | 2, 4 | 12 |
| D — Risk-based alerting | 7 | 3 | 8 |
| E — Hunting and operations | 8–9 | 5, 6 | 10 |
| | | | **~50 hours** |

---

## Topics

### Topic 1: What Enterprise Security Is

ES as a premium app layered on Splunk Enterprise, not a separate product. Its dependency
chain: data → CIM compliance → data models → ES content. The security posture dashboards,
and why they are the least useful part of the product for an analyst.

Cover the licensing and deployment reality honestly: ES is expensive, it is sized
separately, and its resource demands drive architecture decisions that reappear in
[SPL-05](spl-05-architect.md).

### Topic 2: Asset & Identity

The framework, its lookups, and how enrichment attaches business context to a technical
event. Asset criticality, identity categories, and the maintenance problem — asset data
is always stale because the source of truth is a CMDB nobody updates.

**The analytical point:** severity without business context is noise. This is where the
lookup discipline from [SPL-02](spl-02-power-user.md) Topic 3 becomes an operational
capability.

### Topic 3: Correlation Searches and Notables

How correlation searches generate notables; adaptive response actions; the notable's
fields, urgency calculation, and the difference between urgency and severity.

Reading ES's out-of-the-box content critically: much of it is a starting point, not a
production detection, and shipping it untuned is the origin of most alert fatigue.

### Topic 4: The Investigation Workflow

Incident review, ownership, status transitions, and the investigation workbench. Mapping
the ES workflow onto the PICERL phases taught in
[OC04](../../../core/units/OC04-incident-response-lifecycle.md), and being explicit about
where the tool does *not* support the discipline — ES is weak on the lessons-learned phase,
and that work happens elsewhere.

Disposition discipline: closing a notable without recording *why* destroys the data you
need to tune it later.

### Topic 5: Coverage, ATT&CK and the Two Kinds of Gap

Assessing what a detection estate actually covers. The distinction that matters more than
any other in this module:

- A **detection gap** — the telemetry exists, no rule looks at it. Cheap to fix.
- A **telemetry gap** — nothing is logging it. The rule cannot exist until data engineering
  happens first.

Conflating them produces coverage claims that are false, and a coverage heat map that is
green where it should be grey. This is the same honesty DE02 requires about telemetry, and
the same one [SPL-02](spl-02-power-user.md) Lab 2 requires in its gap statement.

### Topic 6: Detection Content Sources

Splunk Security Content / ESCU as delivered detection content, Sigma and its conversion
to SPL, and the maintenance burden of adopted content. What to take, what to adapt, what
to write yourself — and the fact that adopted content you do not understand is content you
cannot tune.

### Topic 7: Risk-Based Alerting

The module's centrepiece. Risk objects and risk index; assigning risk scores to events;
risk incident rules that fire on accumulated score; and the mapping onto ATT&CK tactics so
that a spread of weak signals across the kill chain aggregates into one strong one.

**Where RBA goes wrong:** scores assigned by feel and never calibrated; thresholds that
never fire or always fire; risk attribution to the wrong object; and the failure to
re-baseline as the estate changes. Scoring is a judgement problem, and the module treats
it as one.

### Topic 8: Threat Hunting in Splunk with PEAK

**PEAK** — Prepare, Execute, Act with Knowledge — is Splunk/SURGe's own hunting framework
and is already the hunt-maturity model cited in
[`docs/maturity-models.md`](../../maturity-models.md) and taught in
[TH01](../../../degrees/operational/threat-hunting/TH01-hunting-methodology-process.md).
This topic runs the three PEAK hunt types (hypothesis-driven, baseline, model-assisted) in
Splunk, and — the part that matters — closes the loop by converting a hunt finding into a
correlation search or an RBA contribution.

A hunt that ends in a report and no durable detection has produced knowledge that expires.

### Topic 9: Detection Operations and Alert Quality

Measuring the estate: true/false positive rates, time-to-triage, notables never actioned,
detections that have not fired in six months (broken, or genuinely rare?). Tuning debt as
a managed backlog.

The silent-failure problem from [SPL-02](spl-02-power-user.md) Lab 4 returns here at
estate scale. Connects directly to
[DE05](../../../degrees/operational/detection-engineering/DE05-detection-operations-management.md).

---

## Labs & exercises

!!! warning "Licensing"
    Labs 1, 3 and 4 require **Enterprise Security**, which is not available on the Splunk
    Free licence. Run them inside a trial window as a continuous block. Labs 2, 5 and 6
    can be adapted to run on core Splunk without ES.

Observe the [series safety rules](index.md#safety-authorisation-and-data-handling). Attack
telemetry generation is offensive tooling and runs only in an isolated lab.

### Lab 1: Triage a Notable Queue

Given a populated incident-review queue, triage a shift's worth of notables: assign,
investigate, dispose, and record reasoning for each.

**Deliverable:** the dispositions plus a written reflection identifying which notables
should never have been raised, and what change to the correlation search would have
prevented each.

### Lab 2: Author and Tune a Correlation Search

Write a correlation search for a specified adversary behaviour. Run it against data
containing both the behaviour and realistic benign activity. Measure the false-positive
rate, then tune.

**Deliverable:** version 1, version 2, the measured rates for each, and an explicit
statement of what detection sensitivity was traded away in tuning.

### Lab 3: Design a Risk-Based Alerting Scheme

For a set of ten security-relevant behaviours, assign risk scores, choose risk objects,
and set a threshold. Run it against data. Measure how many risk incidents fired and how
many were worth investigating.

**Deliverable:** the scheme, the results, and a **calibration note** — how you would
adjust the scores given what fired. Full marks require defending at least one score you
got wrong.

### Lab 4: Coverage Assessment

Assess a detection estate against a chosen ATT&CK tactic. Produce a coverage map that
distinguishes covered / detection gap / **telemetry gap**.

**Deliverable:** the map plus a prioritised remediation plan that correctly routes
telemetry gaps to data engineering rather than to detection engineering.

### Lab 5: Adopt and Adapt Detection Content

Take a detection from Splunk Security Content or convert one from Sigma. Get it running.
Determine whether it works in *this* environment — and if it does not, diagnose whether
the cause is logic, normalisation, or missing telemetry.

**Deliverable:** the working detection, or a documented reason it cannot work here.

### Lab 6: A PEAK Hunt, Productised

Run a hypothesis-driven hunt using the PEAK framework as taught in
[TH01](../../../degrees/operational/threat-hunting/TH01-hunting-methodology-process.md).
Whatever the outcome, convert the hunt into durable content — a correlation search, an
RBA contribution, or a documented negative result with the search that would find it next
time.

**Deliverable:** the hunt record and the durable artefact. A hunt with no artefact fails
this lab.

---

## Assessment

### Formative 1: Read the Notable

Given six notables with their underlying events, decide escalate / close / needs-more-data
for each and justify in two sentences. Assesses triage judgement under incomplete
information.

### Formative 2: Should This Alert Exist?

Given five correlation searches, judge whether each should be in production at all.
At least one should be deleted rather than tuned. The learning is that deletion is a
legitimate and under-used tuning outcome.

### Summative: SOC Detection Review

Given a scenario organisation with a described estate, a set of deployed detections and a
sample of triaged notables, deliver a detection review: coverage assessment with the
two-gap distinction, alert-quality metrics, an RBA proposal, a tuning backlog, and a
prioritised recommendation.

Full marks require an honest statement of **what the organisation cannot currently detect
and what it would cost to change that** — including the cases where the answer is
"more telemetry, not more rules".

---

## Australian context

- **ASD Essential Eight and the ISM.** Monitoring and event-logging maturity is where a
  Splunk deployment is usually pointed. Maturity Level requirements shape what must be
  logged and retained; an ES deployment is frequently the evidence that a monitoring
  control is operating. Practise stating what the platform genuinely proves versus what
  it is claimed to prove.
- **ACSC reporting obligations.** Incident reporting to the ACSC, and the **SOCI Act
  2018 (Cth)** mandatory cyber-incident reporting timeframes for responsible entities of
  critical infrastructure assets, mean notable disposition has an external consequence:
  a misclassified notable can be a missed statutory reporting deadline.
- **Notifiable Data Breaches.** Under the **Privacy Act 1988 (Cth)**, an eligible data
  breach triggers assessment and notification obligations. The point at which an analyst
  disposes of a notable is often the point at which that clock does or does not start.
- **APRA CPS 234** for regulated financial entities imposes information-security capability
  and incident-notification requirements that flow directly into SOC process design.
- **ACSC threat advisories** are a legitimate hunt-hypothesis source for Lab 6 and connect
  the module to [OC05](../../../core/units/OC05-threat-intelligence-fundamentals.md).
- **Employee monitoring and surveillance law** (e.g. the NSW *Workplace Surveillance Act
  2005*) constrains user-behaviour analytics and RBA on user risk objects. Scoring a named
  employee's behaviour is a surveillance activity; it needs a basis, not just a use case.

---

## Verification status

- **Verified 2026-09-09:** all exam facts in the table above, against the linked official
  page — including that **no prerequisite certification and no prerequisite coursework**
  are required, and Splunk's own note recommending Power User–level knowledge.
- **Verified 2026-09-09:** the Cybersecurity Defense Engineer and Cybersecurity Defense
  Architect pages likewise publish no prerequisites. Given they sit above CDA in the
  marketing sequence, **confirm whether an unpublished gate exists** before advising a
  learner on the full security track.
- **Not verified:** exam codes are not published and are deliberately not stated. Topic
  coverage is the module author's reading of the platform and has **not** been reconciled
  against Splunk's published test blueprint.
- **Not verified:** the licence terms and current availability of the BOTS datasets,
  `attack_range`, and Splunk Security Content / ESCU. These must be confirmed by the
  Domain Expert **before Labs 4, 5 and 6 are made assessable**.
- Framework mappings, ATT&CK v19 pin and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [Cybersecurity Defense Analyst track](https://www.splunk.com/en_us/training/certification-track/splunk-certified-cybersecurity-defense-analyst.html) — official exam page and test blueprint.
- [Splunk free courses](https://www.splunk.com/en_us/training/free-courses.html) — *Introduction to Enterprise Security*, *SOC Essentials: Investigating with Splunk ES*, and *SOC Essentials: Introduction to Threat Hunting* are all free and map closely to this module.
- [Splunk Enterprise Security documentation](https://docs.splunk.com/Documentation/ES) — the authoritative reference for Topics 1–4.
- [PEAK threat hunting framework](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html) — Splunk/SURGe; already cited in [`docs/maturity-models.md`](../../maturity-models.md).
- [Splunk Security Content (ESCU)](https://research.splunk.com/) — the delivered detection library used in Lab 5.
- [MITRE ATT&CK](https://attack.mitre.org/) — the coverage framework for Topic 5 and Lab 4.
- [ACSC Essential Eight Maturity Model](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-maturity-model) — the Australian monitoring baseline.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-03 |
| Module Title | Enterprise Security & SOC Practice — Cybersecurity Defense Analyst |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 3–5 (Apply / Analyse / Evaluate) |
| Notional Hours | ~50 |
| Zero-cost achievable | Partly — ES labs require a trial licence |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
