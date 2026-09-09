# SPL-05: SOAR & Security Automation — Playbooks, Apps and Orchestration

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
| Certification | [Splunk SOAR Certified Automation Developer](https://www.splunk.com/en_us/training/certification-track/splunk-soar-certified-automation-developer.html) | 2026-09-09 |
| Status | **Legacy Certification** | 2026-09-09 |
| Level | Professional | 2026-09-09 |
| Prerequisite certification | **None listed** | 2026-09-09 |
| Prerequisite coursework | **None specified** | 2026-09-09 |
| Length | 60 minutes | 2026-09-09 |
| Format | 45 multiple choice questions | 2026-09-09 |
| Price | US$130 per attempt | 2026-09-09 |
| Delivery | Pearson VUE | 2026-09-09 |

!!! danger "This certification is Legacy — the skill is not"
    Splunk introduced the **Legacy Certification** category on **1 January 2026**. Legacy
    credentials stay valid and recognised but are **no longer refreshed with product
    releases**. `Splunk SOAR Certified Automation Developer` is one of them, and Splunk's
    page **names no replacement**.

    **So why does this module exist?** Because security automation is not going away — it
    is the fastest-growing part of SOC practice, and the reason it matters is arithmetic:
    a SOC that triages every alert by hand does not scale past its headcount. The
    credential is fading; the capability is the opposite.

    Treat this module as **skills content with an uncertain credential**. A learner should
    not plan a career around this exam. They should absolutely learn to build playbooks.

!!! warning "Recertification policy changed"
    From **1 March 2026** Splunk no longer offers recertification through coursework
    completion. Certifications run a **three-year lifecycle** from the date the
    highest-level certification was achieved.

**Zero-cost achievable: no.** Splunk SOAR is a separate licensed product. Community or
trial editions have historically existed but their current availability and terms are
**unverified** — see [Verification status](#verification-status). Much of the *transferable*
content can be practised with any automation tooling.

---

## Overview

[SPL-04](spl-04-enterprise-security.md) ends at the adaptive response action. This module
starts there.

SOAR — Security Orchestration, Automation and Response — is the layer that takes a
detection and *does something about it*: enriches it from a dozen sources, decides, acts,
and records what happened. Done well it removes the mechanical parts of triage and gives
analysts back the judgement work. Done badly it is an unauditable machine that blocks a
CEO's account at 2am because a threat feed had a bad day.

Three themes, and the third is the one that matters most.

**Enrichment is the safe, high-value automation and it is under-used.** Most of a tier-1
analyst's time goes on gathering context: who owns this host, is this hash known, has this
IP appeared before, is this user on leave. All of that is deterministic, read-only, and
reversible — which makes it the automation with the best ratio of value to risk. Teams
routinely skip it to build dramatic containment playbooks instead.

**Action requires a decision boundary.** Every automated action needs an answer to: is it
reversible, what is the blast radius, what happens if the input was wrong, and who is
accountable. This is the same reasoning [EXT-ANS](../ansible-security-automation.md)
applies to infrastructure automation, and the same conclusion holds — the irreversible
action needs a human, and a containment playbook is a self-authorised denial-of-service
capability.

**A playbook is production software.** It has inputs you do not control, external
dependencies that fail, error paths, and a need for version control, testing and review.
Teams that treat playbooks as configuration rather than code discover this during an
incident.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [SPL-04](spl-04-enterprise-security.md) | **Direct predecessor.** ES adaptive response is the handoff into SOAR. |
| [SPL-03](spl-03-cyber-defense-analyst.md) | The analyst workflow that automation is meant to relieve. Automating a process you have not performed manually is how bad playbooks get built. |
| [OC04 — Incident Response Lifecycle](../../../core/units/OC04-incident-response-lifecycle.md) | **Assumed core unit.** Playbooks implement PICERL phases; containment decisions are OC04's subject matter. |
| [SE04 — Detection & Response Engineering](../../../degrees/strategic/security-engineering/SE04-detection-response-engineering.md) | **The core unit this applies.** Response engineering, vendor-neutral. |
| [F03 — Scripting & Automation](../../../core/units/F03-scripting-automation.md) | **Assumed.** Playbook development is Python; custom apps definitely are. |
| [EXT-ANS](../ansible-security-automation.md) | **Strong parallel.** Its blast-radius, reversibility and control-plane-security arguments transfer directly and are not repeated here. |
| [F05 — Legal, Ethics & Compliance](../../../core/units/F05-legal-ethics-compliance.md) | Automated action against systems and accounts has legal consequences. |

---

## Learning outcomes

On completion, a learner can:

1. **Explain** SOAR architecture — ingestion, containers, artefacts, assets, apps and
   actions — and how a detection becomes a case.
2. **Design** an automation decision boundary distinguishing enrichment, reversible action
   and irreversible action, and **justify** where human approval is required.
3. **Build** playbooks using both visual and code editors, including branching, filtering,
   decision blocks and error handling.
4. **Develop** a custom app or action to integrate an unsupported product.
5. **Implement** case management: severity, ownership, SLA, evidence and audit trail.
6. **Evaluate** automation effectiveness with honest metrics, and **assess** when a
   playbook should be retired rather than extended.
7. **Assess** the SOAR platform itself as a high-value target with privileged credentials
   into every connected system.

> Bloom's 3–6.

---

## Framework mappings

> **Provisional pending Framework Custodian review.** These do **not** feed
> [`docs/ksat-coverage.md`](../../ksat-coverage.md).

### NIST NICE DCWF

| Version | Work Role | Code | T-Code | Task | Demonstrated in |
|---|---|---|---|---|---|
| 2023 | Cyber Defense Analyst | PR-CDA-001 | T0166 | Engineer correlation and automated response | Lab 2, Lab 3 |
| 2023 | Cyber Defense Incident Responder | PR-CIR-001 | T0041 | Coordinate and perform incident handling across the lifecycle | Lab 3, Lab 5 |
| 2023 | Cyber Defense Incident Responder | PR-CIR-001 | T0278 | Collect and preserve evidence and establish an incident timeline | Lab 5 |
| 2023 | Software Developer | SP-DEV-001 | T0011 | Develop and maintain software solutions | Lab 4 |
| 2023 | System Administrator | OM-ADM-001 | T0431 | Automate administration tasks across platforms | Lab 2 |

### SFIA 9

| Skill | Code | Level | Demonstrated in |
|---|---|---|---|
| Security operations | SCAD | Level 4 | Lab 2, Lab 3 |
| Software design / development | SWDN / PROG | Level 4 | Lab 4 |
| Incident management | USUP | Level 4 | Lab 5 |
| Systems integration and build | SINT | Level 4 | Lab 4 |
| Continuity management | COPL | Level 4 | Lab 3 (rollback paths) |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated in |
|---|---|---|---|
| Defensive Operations | Incident Response | Practitioner–Advanced | Lab 3, Lab 5 |
| Defensive Operations | Security Automation | Advanced | Lab 2, Lab 4 |
| Secure Systems | Platform Security | Practitioner | Lab 6 |

### MITRE ATT&CK

Techniques relevant to **abuse of** the SOAR platform (Topic 12, Lab 6). Stated against
**v19** for repository consistency; version pin and IDs **provisional pending Framework
Custodian verification**.

| Technique | ID | Relevance |
|---|---|---|
| Valid Accounts | T1078 | SOAR service accounts hold privileged credentials into every connected system and are rarely rotated. |
| Software Deployment Tools | T1072 | A SOAR platform with response actions is, functionally, a remote-execution system across the estate. |
| Unsecured Credentials: Credentials In Files | T1552.001 | Asset configurations, custom app code and playbook parameters holding secrets. |
| Supply Chain Compromise: Compromise Software Supply Chain | T1195.002 | Third-party apps and connectors installed from a marketplace. |
| Impair Defenses: Disable or Modify Tools | T1562.001 | Modifying a playbook to suppress response is a durable, low-noise defence-evasion technique. |

### Project-local KSATs

| Type | ID | Statement | Demonstrated in |
|---|---|---|---|
| Knowledge | SPL-05-K01 | Knowledge of SOAR architecture: containers, artefacts, assets, apps, actions | Topic 2; Lab 1 |
| Knowledge | SPL-05-K02 | Knowledge of the automation decision boundary and reversibility | Topic 4; Lab 3 |
| Knowledge | SPL-05-K03 | Knowledge of playbook control flow, blocks and error handling | Topic 5–6; Lab 2 |
| Knowledge | SPL-05-K04 | Knowledge of the app/connector model and custom action development | Topic 8; Lab 4 |
| Knowledge | SPL-05-K05 | Knowledge of case management, evidence and audit trail | Topic 9; Lab 5 |
| Knowledge | SPL-05-K06 | Knowledge of the SOAR platform as a privileged target | Topic 12; Lab 6 |
| Skill | SPL-05-S01 | Skill in building enrichment playbooks with error handling | Lab 2 |
| Skill | SPL-05-S02 | Skill in building guarded response playbooks with approval and rollback | Lab 3 |
| Skill | SPL-05-S03 | Skill in developing a custom app/action in Python | Lab 4 |
| Ability | SPL-05-A01 | Ability to decide what must not be automated | Lab 3; Formative 1 |
| Ability | SPL-05-A02 | Ability to design a playbook that fails safely on bad input | Lab 2; Lab 3 |
| Ability | SPL-05-A03 | Ability to measure automation value honestly and retire a playbook | Lab 7; Summative |

---

## Module structure

| Part | Topics | Labs | Notional hours |
|---|---|---|---|
| A — Platform and model | 1–3 | 1 | 10 |
| B — The decision boundary | 4 | — | 6 |
| C — Playbook development | 5–7 | 2, 3 | 18 |
| D — Integration | 8 | 4 | 10 |
| E — Case management | 9–10 | 5 | 10 |
| F — Operating and defending | 11–13 | 6, 7 | 14 |
| G — Analyst experience and integration | 14–15 | 8 | 14 |
| | | | **~82 hours** |

---

## Blueprint alignment

Verified against the published
[SOAR Certified Automation Developer test blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-soar-automation-developer.pdf),
retrieved 2026-09-09. Eighteen domains, almost all at 5% — a broad, shallow exam covering
the whole product.

| Domain | Weight | Covered by |
|---|---|---|
| 1.0 Deployment, installation, initial configuration (operating concepts, architecture, licences) | 5% | Topics 2, 3 |
| 2.0 User management (authentication, users, roles) | 5% | Topic 3 |
| 3.0 Apps, assets and playbooks (configure apps/assets/ingestion assets, **labels and SLAs**, manage playbooks) | 5% | Topics 2, 8 |
| 4.0 **Analyst queue** (queue, search, filters, indicator view) | 5% | Topic 14 |
| 5.0 **The investigation page** (work events, run actions manually, run playbooks manually, file tab) | 10% | Topic 14 |
| 6.0 Case management and workbooks (**mark items as evidence**) | 5% | Topics 9, 10 |
| 7.0 Customizations (severity, **CEF fields**, status values, workbooks, **global custom fields**) | 5% | Topics 2, 14 |
| 8.0 System maintenance (reports, health displays, health logs) | 5% | Topic 11 |
| 9.0 Introduction to playbooks (automation best practices, capabilities, app actions, **I2A2 design methodology**) | 5% | Topics 4, 5 |
| 10.0 Visual playbook editor | 5% | Topic 5 |
| 11.0 Logic, filters and user interaction (decision, filter, **join options**, prompts) | 5% | Topics 5, 7 |
| 12.0 **Formatted output and data access** (format blocks, action-result structure, **datapaths**, utility block) | 5% | Topics 5, 6 |
| 13.0 Modular playbook development (child playbooks, data exchange) | 5% | Topic 5 |
| 14.0 **Custom lists and data routing** | 5% | Topic 15 |
| 15.0 **Configuring external Splunk search** (externalise search, configure both sides, reindex, Phantom Reporting app) | 5% | Topic 15 |
| 16.0 **Integrating SOAR into Splunk** (**Splunk App for SOAR Export**, **send ES notables to SOAR**, Splunk app in SOAR, Splunk search from playbooks) | **10%** | Topic 15 |
| 17.0 Custom coding (**global block**, custom function blocks, writing and testing custom SOAR code) | 5% | Topics 5, 8 |
| 18.0 Using REST (SOAR REST API, **Django queries**, REST from other systems) | 5% | Topic 15 |

!!! note "15% of this exam is the Splunk↔SOAR integration"
    Domains 15.0 and 16.0 together carry **15%** — externalising SOAR's search to Splunk,
    and pushing ES notables into SOAR. That integration is the reason most organisations
    own both products, and it is covered in Topic 15.

**Beyond the blueprint** — Topics 1 (what SOAR is for), 4 (the decision boundary), 11
(measuring automation honestly), 12 (defending the platform) and 13 (the operating model)
are not examined. Topic 4 is the most important topic in the module regardless: the
blueprint tests whether you *can* automate an action, not whether you *should*.

---

## Topics

### Topic 1: What SOAR Is For — and What It Is Not

The honest framing. SOAR is bought to reduce mean time to respond and to relieve analyst
load; it delivers when the SOC already has repeatable processes, and fails when it is
bought to *create* process discipline it does not have.

**The precondition:** you cannot automate a process you have not performed manually and
documented. A playbook is the encoding of a decision procedure — if the procedure is
undefined, the playbook encodes confusion at machine speed.

SOAR versus adaptive response in ES versus scripting: when each is the right answer, and
the observation that a great deal of what teams buy SOAR for is achievable with the
scheduled searches and adaptive responses they already own.

### Topic 2: Architecture and the Object Model

The core objects: **containers** (an event or case), **artefacts** (the observables within
a container), **assets** (configured connections to external products), **apps** (the
integrations that provide actions), **actions**, and **playbooks**.

Ingestion: connectors that pull events in, the ES-to-SOAR handoff, and container
deduplication. Severity, status, ownership and labels — labels being the routing mechanism
that decides which playbook runs.

The **Common Event Format** normalisation SOAR applies to artefacts, and why artefact CEF
field naming determines whether a playbook can find the observable it needs.

### Topic 3: Deployment and Configuration

Deployment models and sizing considerations. Asset configuration and the credential
problem: every asset holds credentials into a production system, and the aggregate is the
most privileged credential store in the organisation.

Roles and permissions, tenancy where multi-tenant deployment applies, and the separation
between who may *write* a playbook and who may *run* one — a segregation-of-duties control
that most deployments do not implement.

### Topic 4: The Automation Decision Boundary

**The most important topic in this module.** A taxonomy every action must be placed in
before it is built:

| Class | Examples | Automation posture |
|---|---|---|
| **Read-only enrichment** | Reputation lookup, asset owner, sandbox detonation, prior-sighting search | Automate freely. Highest value, lowest risk. |
| **Reversible action** | Tag a host, open a ticket, notify, quarantine a file to a holding area | Automate with logging and an easy undo. |
| **Disruptive but recoverable** | Disable an account, isolate a host from the network | Automate **with approval** for high-value assets; require a documented reversal. |
| **Irreversible** | Delete data, wipe a device, terminate production workloads, block at a shared perimeter | **Never fully automatic.** Human decision, recorded. |

The tests to apply to every action: reversibility, blast radius, what happens if the
triggering input was a false positive, and who is accountable when it fires wrongly.

**The uncomfortable point:** an automated containment capability is an authorised
denial-of-service capability pointed at your own organisation. That is acceptable and
sometimes necessary — but it must be a deliberate decision with a named owner, not an
emergent property of someone's weekend playbook.

### Topic 5: Playbook Development — Structure and Control Flow

**The I2A2 design methodology** — Inputs, Interactions, Actions, Outputs — which the
blueprint names explicitly (domain 9.4) and which is genuinely useful: decide what the
playbook receives, where a human is involved, what it does, and what it produces, *before*
opening the editor.

The visual editor and the underlying Python. Blocks: **action**, **filter**, **decision**,
**format**, **prompt**, **utility**, **API**, **code/custom function** and **end**. The
**global block** and when not to use it. Datapaths — how a playbook
addresses artefact and action-result data — which is the single biggest source of playbook
defects.

Control flow: branching, parallel execution and join semantics, and why a playbook that
assumes ordering it has not enforced fails intermittently and unreproducibly.

Input and output playbooks, and calling one playbook from another for reuse.

### Topic 6: Playbook Development — Robustness

The topic that separates a demo playbook from a production one.

Error handling: an action that fails, an asset that is unreachable, an API that
rate-limits, a response schema that changed. Timeouts. Idempotency — what happens when the
same container is processed twice.

Handling missing or malformed artefacts. Defensive datapath access. Logging enough to
reconstruct what a playbook did during a post-incident review.

**Failing safe:** when a playbook cannot complete, the correct behaviour is almost always
to stop, record, and escalate to a human — not to proceed on partial data.

### Topic 7: Prompts, Approval and Human-in-the-Loop

The prompt block as the implementation of the decision boundary. Designing an approval
request that gives the approver enough context to decide — and the recognition that an
approver who always clicks yes is not a control.

Timeouts on approvals and what happens when nobody responds at 3am. Escalation paths.
Recording the approval decision as part of the audit trail.

### Topic 8: Apps, Connectors and Custom Development

The app model: how an app supplies actions, the app JSON, action parameters and result
schemas. Configuring and testing assets.

**Developing a custom app** in Python for a product with no supported integration: the
connector class, `handle_action`, test connectivity, parameter and output schema
definitions, and error and status reporting.

Supply-chain caution: a third-party app runs with the credentials you give it, inside your
response platform. Marketplace apps are dependencies to review, not features to install —
the same argument as [EXT-ANS](../ansible-security-automation.md) Topic 4 on collections.

### Topic 9: Case Management, Evidence and Audit

Cases versus events. Severity and SLA. Ownership and handoff. Evidence collection and
attachment. Notes and the investigative record.

The **audit trail** as the primary control on automation: every action, who or what
invoked it, on what input, with what result. Without a reconstructable trail, an automated
response cannot be reviewed after an incident — which makes it unusable in any regulated
context.

Where SOAR case management stops and an enterprise ticketing system starts, and the
integration in between.

### Topic 10: Workbooks and Process Encoding

Workbooks as the semi-automated middle ground: a structured task list guiding an analyst
through a procedure, with automation attached to individual tasks.

**Why this is often the right answer.** Full automation of an investigative process is
frequently the wrong goal; encoding the process as a checklist with automated enrichment at
each step captures most of the value at a fraction of the risk, and it produces consistency
across analysts — which is a quality problem more than a speed problem.

Mapping workbook phases onto PICERL from
[OC04](../../../core/units/OC04-incident-response-lifecycle.md).

### Topic 11: Measuring Automation Honestly

Metrics that mean something: time saved per playbook run against build and maintenance
cost, playbook success and failure rates, actions requiring human correction, and cases
where automation made things worse.

**The vanity metrics to distrust:** "actions automated" and "hours saved" computed from an
assumed manual duration. A playbook that runs ten thousand times and saves nothing real is
counted as a success by both.

**Retiring playbooks.** Automation accumulates. Playbooks bound to products no longer in
use, or to a process that has changed, become quiet liabilities. Reviewing and deleting is
part of the job, exactly as it is for detection content in
[SPL-04](spl-04-enterprise-security.md) Topic 10.

### Topic 12: Defending the SOAR Platform

The platform holds privileged credentials into every connected system and can execute
actions across the estate. It is the highest-value target in the security stack, and
compromising it grants both intelligence and the ability to suppress response.

- **Credential management** for assets, rotation, and least-privilege scoping of each
  integration — the integration that only needs read access should only have read access.
- **Playbook integrity:** who may modify a playbook, code review, and detecting
  unauthorised change. A modified playbook that quietly stops containing is a durable,
  low-noise defence-evasion technique (ATT&CK T1562.001).
- **Monitoring the platform in Splunk** — SOAR's own audit log as a data source, and
  detections for anomalous action volume or out-of-hours playbook modification.
- **Segregation of duties** between playbook authors, approvers and operators.

Directly parallel to [EXT-ANS](../ansible-security-automation.md) Topic 13 on the
automation control plane; the argument is the same and the stakes are higher.

### Topic 13: SOAR in a Real Operating Model

Where automation sits across tiers, and the honest observation that SOAR is often deployed
to compensate for alert quality problems that should be fixed upstream in
[SPL-04](spl-04-enterprise-security.md).

**The order of operations:** tune the detection, then automate the response. Automating
triage of a noisy detection industrialises the noise and makes the underlying problem
harder to see, because the pain that would have forced a fix has been absorbed by a machine.

---

### Topic 14: The Analyst Experience — Queue, Investigation and Customisation

What the people using your playbooks actually see, and 20% of the blueprint.

**The analyst queue**: working the event list, search features, building filters, and the
**indicator view** that surfaces observables shared across containers — the fastest route
to "have we seen this before?".

**The investigation page**: examining an event, **running actions manually** and reading
action results, **running a playbook manually** against a container, and the file tab for
storing related artefacts.

**Customisation** (domain 7.0): severity levels, status values, **CEF field definitions**,
workbook templates, and **global custom fields** on containers. These are the settings that
make SOAR match your SOC's vocabulary rather than forcing the reverse — and getting the CEF
field naming right is what lets playbooks find observables reliably.

### Topic 15: Integration — SOAR and Splunk Together

**15% of the blueprint**, and the reason most organisations own both products.

**Configuring external Splunk search** (domain 15.0): externalising SOAR's search to a
Splunk instance, why that is worth doing (SOAR's own search is not built for volume),
configuring both sides, `reindex` to push existing content across, and the Phantom
Reporting app.

**Integrating SOAR into Splunk** (domain 16.0): the **Splunk App for SOAR Export**,
**sending Enterprise Security notables to SOAR** — the handoff that connects
[SPL-04](spl-04-enterprise-security.md) Topic 6's adaptive response to this module —
installing the Splunk app inside SOAR, and calling Splunk search from within a playbook.

**Custom lists and data routing** (domain 14.0): creating lists, reading them from
playbooks, and using them as allow/deny or routing tables. The practical mechanism for
"do not action anything on this list of critical servers".

**The REST API** (domain 18.0): SOAR's REST capabilities, **Django-style queries** for
searching SOAR data, and driving SOAR from other systems. This is how SOAR becomes a
component of a larger automation estate rather than a silo.

---

## Labs & exercises

!!! danger "Platform access is a real constraint"
    Splunk SOAR is a licensed product and its free/community availability is
    **unverified** — see [Verification status](#verification-status). Where a SOAR instance
    is unavailable, **Labs 1, 3, 5 and 7 can be completed as design exercises** and remain
    the most valuable in the module; Labs 2, 4 and 6 need a platform, and Lab 4's transferable
    content can be practised by writing an integration against any API.

    Confirm platform availability before scheduling this module.

Observe the [series safety rules](index.md#safety-authorisation-and-data-handling). Response
playbooks act on real systems: run them only against infrastructure you own or have written
authorisation to test.

### Lab 1: Map a Process Before Automating It — *no platform required*

Take one real triage process (e.g. a suspicious-authentication alert). Document it as
performed manually: every decision point, every source consulted, every outcome.

Then classify each step against the Topic 4 decision boundary.

**Deliverable:** the process map with each step classified, and a statement of which steps
should **not** be automated and why. This lab gates the rest of the module — automating an
undocumented process is the failure this prevents.

### Lab 2: An Enrichment Playbook That Fails Well

Build a playbook that enriches an artefact from at least three sources. Then break each
source in turn — unreachable asset, rate limit, malformed response, missing artefact — and
make the playbook handle each without producing a wrong answer.

**Deliverable:** the playbook, evidence of behaviour under each failure, and the logging
output showing what an analyst would see.

### Lab 3: A Guarded Response Playbook — *design achievable without a platform*

Build (or design in full) a containment playbook with an approval prompt, a documented
reversal procedure, and a bounded target set.

Then have a peer supply a **false-positive input** and demonstrate that the playbook does
not cause harm.

**Deliverable:** the playbook, the reversal procedure, the approval design with its
timeout and escalation behaviour, and the false-positive test result.

### Lab 4: Build a Custom App

Develop a custom app providing at least two actions against an API of your choice
(a public API is fine). Include test connectivity, parameter validation, error handling and
a documented output schema.

**Deliverable:** the app code, evidence of both actions working, and evidence of correct
behaviour on an authentication failure and a malformed response.

### Lab 5: Case Management and the Audit Trail — *no platform required*

Design the case model for a described SOC: severity definitions, SLA, ownership and
handoff, evidence requirements, and the audit fields needed to reconstruct an automated
response after the fact.

**Deliverable:** the case model, plus a worked reconstruction — given a hypothetical
automated containment that fired wrongly, show that your audit design answers what fired,
on what input, who approved it, and what it changed.

### Lab 6: Attack Your Own Automation

In an isolated lab, assess the SOAR platform as a target: enumerate the privileges its
asset credentials hold, and determine what an attacker with playbook-edit access could
suppress.

**Deliverable:** a threat model, a least-privilege re-scoping proposal for at least three
assets, and a detection for unauthorised playbook modification.

### Lab 7: Measure and Retire — *no platform required*

Given a portfolio of playbooks with run statistics, assess each: is it delivering value, is
it maintained, is it still relevant?

**Deliverable:** a portfolio assessment with a retirement recommendation for at least one
playbook, and an honest critique of the "hours saved" metric as presented.

---

### Lab 8: Wire ES to SOAR — *platform required*

Configure the ES→SOAR handoff end to end: install the Splunk App for SOAR Export, send a
correlation search's notable to SOAR as a container, and have a playbook trigger on its
label.

Then close the loop the other way: call a Splunk search from inside the playbook to enrich
the container, and write the outcome back so it is visible in ES.

**Deliverable:** the working integration, evidence of a notable traversing both directions,
and a note on what happens to the container when the ES notable is later closed by an
analyst — the state-synchronisation problem nobody designs for up front.

---

## Assessment

### Formative 1: Automate or Not?

Given twelve candidate actions, place each in the Topic 4 taxonomy and state the automation
posture. At least two must be identified as never-automate, with reasoning.

### Formative 2: Why Did This Playbook Do That?

Given a playbook and a log of an incorrect run, diagnose the defect. Cases should include a
datapath error, an unhandled failure, and a race from unenforced ordering.

### Summative: Automation Programme Design

For a described SOC with stated alert volumes, tooling and headcount:

1. A process inventory with automation candidates ranked by value and risk.
2. The decision boundary applied, with a documented never-automate list.
3. An enrichment playbook design with error handling.
4. A guarded response playbook with approval, reversal and bounded scope.
5. A case model and audit design.
6. A platform security assessment with least-privilege credential scoping.
7. An honest measurement plan, including how you would detect that a playbook has become
   harmful.
8. **A statement of what should be fixed upstream instead of automated.**

Item 8 carries disproportionate weight. A programme that automates around a detection
quality problem rather than fixing it is marked as a failure of judgement.

---

## Australian context

- **Automated action has legal weight.** Disabling accounts, isolating hosts or blocking
  traffic are interferences with computer systems. Where they touch systems outside your
  organisation's control — a shared platform, a partner network, a customer tenancy — the
  *Criminal Code Act 1995* (Cth) Part 10.7 offences turn on **authorisation**. Automated
  action must be inside a documented authorisation boundary, and "the playbook did it" is
  not a defence. Grounded in [F05](../../../core/units/F05-legal-ethics-compliance.md).
- **Automated action against employees engages workplace law.** Disabling an employee's
  account or isolating their device has employment consequences and may engage surveillance
  legislation (e.g. NSW *Workplace Surveillance Act 2005*) and the **Fair Work Act 2009
  (Cth)** where it affects someone's ability to work. Automation does not remove the
  requirement for a defensible basis.
- **SOCI Act 2018 (Cth) and critical infrastructure.** Responsible entities have
  risk-management-program obligations, and an automated response capability that can
  disrupt operational systems is itself an operational risk requiring assessment. In OT and
  critical-infrastructure contexts, automated containment can be more dangerous than the
  intrusion — a rule of thumb worth stating plainly to learners.
- **APRA CPS 234 and CPS 230.** Regulated entities must demonstrate that controls operate
  and manage operational risk in critical operations. An automated response with no
  reconstructable audit trail cannot be evidenced to a regulator, which makes the Topic 9
  audit design a compliance artefact.
- **Privacy Act 1988 (Cth).** Enrichment playbooks aggregate personal information —
  identity, device, location, behaviour — into a case record, often from sources that were
  separate by design. Automated aggregation is still collection, and APP 11 still applies
  to the resulting case data.
- **Mandatory reporting timeframes** under SOCI and the **Notifiable Data Breaches**
  scheme mean a playbook that closes a case automatically can suppress the human assessment
  that would have started a statutory clock. Auto-closure is a reporting risk, not just an
  efficiency feature.

---

## Verification status

- **Verified 2026-09-09:** exam facts above against the official page, including that this
  certification is marked a **Legacy Certification** and that Splunk **names no
  replacement**.
- **Verified 2026-09-09** (Splunk's certification-changes FAQ): Legacy Certification
  category introduced **1 January 2026**; recertification by coursework ends **1 March
  2026**; **three-year lifecycle** from the highest-level certification achieved.
- **NOT VERIFIED — blocking for lab planning.** The current availability, edition and
  licence terms of Splunk SOAR for learning use (community edition, trial, or developer
  licence). Labs are written so the highest-value ones (1, 3, 5, 7) run as design exercises
  without a platform, but **platform availability must be confirmed before this module is
  scheduled**.
- **Not verified:** the exam code is not published and is deliberately not stated. Topic coverage **has now been reconciled against the published test blueprint** — see
  [Blueprint alignment](#blueprint-alignment). Sub-objective wording is not reproduced;
  the mapping uses domain titles and weightings only. Product terminology and the block set differ
  between Phantom-era and current Splunk SOAR releases, and between on-premises and cloud
  editions — this module is **not pinned to a SOAR version**, which must be fixed at review.
- **Uncertain credential.** Because the certification is Legacy with no named successor,
  the Domain Expert should decide whether this module is presented as certification
  preparation at all, or purely as skills content. The series' current position is the
  latter.
- Framework mappings, ATT&CK v19 pin and KSAT IDs are provisional per the
  [series verification status](index.md#verification-status).

---

## Further reading

- [SOAR Certified Automation Developer track (Legacy)](https://www.splunk.com/en_us/training/certification-track/splunk-soar-certified-automation-developer.html) — official exam page.
- [Upcoming Splunk Certification Changes (PDF)](https://www.splunk.com/en_us/pdfs/training/splunk-certification-changes.pdf) — the Legacy category and recertification change.
- [Splunk SOAR documentation](https://docs.splunk.com/Documentation/SOAR) — the authoritative product reference.
- [Splunk SOAR app development documentation](https://docs.splunk.com/Documentation/SOARapp) — Topic 8 and Lab 4.
- [Splunk free courses](https://www.splunk.com/en_us/training/free-courses.html) — SOAR playbook courses are in the free catalogue.
- [EXT-ANS Topic 6 and Topic 13](../ansible-security-automation.md) — the response-action taxonomy and control-plane threat model this module builds on.
- [ACSC Incident Response guidance](https://www.cyber.gov.au/resources-business-and-government/governance-and-user-education/incident-response) — Australian IR expectations that constrain automated response.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | SPL-05 |
| Module Title | SOAR & Security Automation — Playbooks, Apps and Orchestration |
| Series | [EXT-SPL](index.md) |
| Status | Draft |
| Bloom's Level | 3–6 (Apply / Analyse / Evaluate / Create) |
| Notional Hours | ~82 |
| Zero-cost achievable | **No** — licensed product; free-tier availability unverified |
| Credential note | **Legacy Certification, no named successor.** Treat as skills content, not exam preparation. |
| Facts verified | 2026-09-09 |
| Licence | CC BY 4.0 |
