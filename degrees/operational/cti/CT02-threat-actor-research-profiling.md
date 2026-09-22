# CT02: Threat Actor Research & Profiling

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit teaches the analytic core of CTI: researching and profiling threat
actors. Students learn to model intrusions with the **Diamond Model**, build
ATT&CK-based actor profiles, track groups and campaigns over time, and apply
attribution *methodology* rigorously and responsibly. A deliberate emphasis of the
unit — and a sign-off requirement — is that students learn how attribution is
*reasoned about*, not how to make confident public attributions; attribution is
treated as a probabilistic, evidence-graded analytic judgement.

Actor profiling produces the operational intelligence that drives hunting, detection,
and response: knowing how a relevant group behaves lets defenders prioritise. In the
Australian context, the ACSC reports on actors targeting Australian sectors and the
APAC region; this unit uses those reports as research material while teaching method
over conclusion. CT02 builds on CT01 and OC01, and feeds CT03–CT06.

---

## Prerequisites

- CT01 — Intelligence Tradecraft
- OC01 — Adversary Tradecraft & TTPs

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Apply** the Diamond Model of Intrusion Analysis to a known intrusion.
2. **Analyse** a threat actor's behaviour and build an ATT&CK (v19) actor profile.
3. **Evaluate** attribution evidence using a structured, confidence-graded
   methodology.
4. **Synthesise** open-source reporting into a coherent actor/campaign profile.
5. **Analyse** how actor profiles inform defensive prioritisation.
6. **Recommend** an actor profile suitable for an operational consumer, with
   appropriate caveats.

7. **Evaluate** how profiling a financially motivated criminal organisation (e.g. a
   ransomware-as-a-service operation) differs methodologically from profiling a
   nation-state actor.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops specialised knowledge of intrusion
analysis models, actor profiling, and attribution methodology.

**Skills (AQF 7.2):** Students develop analytical and synthesis skills by modelling
intrusions and building evidence-graded profiles.

**Application (AQF 7.3):** Students apply profiling to Australian-relevant actors,
producing operationally useful, appropriately-caveated intelligence.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Threat/Warning Analyst (621) | AN-TWA-001 | T0707 | Analyse adversary activity to produce actor/campaign intelligence | Lab 1 — Diamond Model of an Intrusion |
| NIST NICE DCWF | 2023 | All-Source Analyst (611) | AN-ASA-001 | T0751 | Synthesise multi-source reporting into finished actor profiles | Lab 2 — ATT&CK Actor Profile; Lab 3 — RaaS Operation Profile |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information assurance / security | INAS | Level 4–5 | Lab 1, Lab 2 |
| Threat intelligence | THIN | Level 5 | Lab 2, Lab 3 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Threat Intelligence | Threat Analysis | Practitioner–Advanced | Lab 1, Lab 2, Lab 3 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | CT02-K01 | Knowledge of the Diamond Model | Topic 1 |
| Knowledge | CT02-K02 | Knowledge of ATT&CK actor profiling | Topic 2 |
| Knowledge | CT02-K03 | Knowledge of campaign and group tracking | Topic 3 |
| Knowledge | CT02-K04 | Knowledge of attribution methodology as method, not verdict | Topic 4 |
| Skill | CT02-S01 | Skill in building a Diamond Model of an intrusion | Lab 1 |
| Skill | CT02-S02 | Skill in producing an ATT&CK actor profile | Lab 2 |
| Ability | CT02-A01 | Ability to turn an actor profile into a defensive priority | Lab 2; Topic 5 |
| Ability | CT02-A02 | Ability to reason about attribution confidence | Topic 4; Summative |

| Knowledge | CT02-K05 | Knowledge of the RaaS operating model and the financially motivated criminal ecosystem as an intelligence target | Topic 7 |
| Skill | CT02-S03 | Skill in profiling a government-attributed RaaS operation from public, co-sealed advisories | Lab 3 |
| Ability | CT02-A03 | Ability to evaluate how criminal-organisation profiling differs from nation-state profiling and to account for the affiliate confounder | Topic 7; Lab 3; Summative |
| Task | T0707 | Analyse adversary activity to produce actor/campaign intelligence | Lab 1 |
| Task | T0751 | Synthesise multi-source reporting into finished actor profiles | Lab 2 |

---

## Topics

### Topic 1: The Diamond Model

The Diamond Model analyses intrusions across four vertices — adversary,
capability, infrastructure, victim — linked by meta-features. This topic teaches
populating and pivoting across the diamond to develop and connect intrusion events.

**Key concepts:**
- The four vertices and meta-features
- Pivoting across the diamond
- Linking events into activity threads

---

### Topic 2: ATT&CK Actor Profiling

This topic teaches building an actor profile in ATT&CK terms: collecting known
techniques from ATT&CK Groups/Software and reporting, building a Navigator layer,
and distinguishing signature behaviour from commodity tooling.

**Key concepts:**
- ATT&CK Groups/Software as profile sources
- Building and annotating Navigator layers
- Signature vs commodity behaviour

**Australian context:** Profiles are built for actors the ACSC reports as active
against Australian/APAC sectors.

---

### Topic 3: Campaign and Group Tracking

Actors evolve. This topic covers tracking campaigns and groups over time: clustering
activity, naming conventions and the "attribution by different vendors" problem, and
maintaining living profiles as new reporting arrives.

**Key concepts:**
- Activity clustering and campaign tracking
- The multi-vendor naming problem
- Maintaining living profiles

---

### Topic 4: Attribution Methodology (Method, Not Verdicts)

This topic teaches how attribution is reasoned about — combining technical,
infrastructural, and behavioural evidence with confidence levels — while
emphasising that responsible analysts rarely make confident public attributions and
must avoid overreach. The focus is methodology and caveat, not naming.

**Key concepts:**
- Layers of attribution evidence
- Confidence and the limits of attribution
- Avoiding analytic overreach (responsibility)

**Australian context:** Public attribution is a government function (e.g. ASD/
Government statements); analysts support, not pre-empt, it.

---

### Topic 5: From Profile to Defensive Priority

This topic connects profiling to action: translating an actor profile into
prioritised techniques to hunt/detect (linking to TH02/OC02) and into intelligence
that informs risk decisions.

**Key concepts:**
- Profile → prioritised techniques
- Informing hunting/detection priorities
- Informing risk decisions

---

### Topic 6: Producing the Actor Profile

This topic teaches packaging a profile for a consumer: structure, evidence and
sourcing, confidence statements, and consumer-appropriate language — a finished
product, not a research dump.

**Key concepts:**
- Profile structure and sourcing
- Confidence and caveats
- Consumer-appropriate finished products

**Australian context:** Profiles cite publicly attributed Australian incident
examples where available, with method emphasised.


---

### Topic 7: The Cybercriminal Organisation as an Intelligence Target

Most of the models earlier in this unit were shaped by nation-state intrusion
analysis. A financially motivated criminal organisation — above all a
ransomware-as-a-service (RaaS) operation — is a structurally different intelligence
target, and methods tuned for a single, coherent state actor mislead when applied to
it. F04 (Foundation) introduces this ecosystem at a vocabulary level; this topic does
not restate those definitions but **analyses and evaluates the criminal organisation
as a target**: how its operating model shapes the evidence an analyst sees, and where
profiling and attribution have to be done differently.

**RaaS as an operating model.** In a RaaS operation an *operator* maintains the
ransomware and supporting infrastructure and recruits *affiliates* who conduct the
intrusions in exchange for a share of each ransom. Government reporting describes the
split directly: CISA and partners — with ASD's ACSC among the authoring agencies —
state that a RaaS group "maintains the functionality of a particular ransomware
variant, sells access to that ransomware variant to individuals or groups of
operators (often referred to as 'affiliates')" (Understanding Ransomware Threat
Actors: LockBit, AA23-165A). The consequence is the core analytic point of this
topic: because affiliates are numerous and *unconnected*, the same brand spans widely
different tradecraft. The same advisory notes that LockBit attacks "vary
significantly in observed tactics, techniques, and procedures (TTPs)" precisely
because of "the large number of unconnected affiliates in the operation." This is why
"sophistication" is a poor risk proxy — the point F04 introduces and this topic
operationalises: an unremarkable affiliate wielding a capable operator's tooling can
still be devastating, and the brand name tells an analyst little about the specific
intrusion in front of them.

**Initial-access brokers (IABs).** A distinct market tier sells footholds — valid
accounts, VPN/RDP access, web shells — to affiliates and operators. For the analyst
this *decouples* the initial-access phase from the ransomware phase: the actor who
breached the perimeter is frequently not the actor who deployed the ransomware. That
fragments the intrusion timeline and undercuts any assumption of a single actor
moving linearly from access to impact.

**Double extortion and leak-site economics as an intelligence source.** Since 2021,
RaaS operations have exfiltrated data and threatened to publish it on leak sites
(AA23-165A). A leak site is a valuable but *biased* source. It can indicate which
victims did not pay (or were named to pressure them), the operation's tempo, and its
sector focus. It does **not** reveal the total victim count (payers are absent by
design), whether a listing is truthful, or whether a named "victim" is even real —
victim naming is a pressure and marketing instrument, not a register, and
over-represents non-payers. Treating a leak site as a census is a selection-bias
error.

**Profiling a criminal org versus a nation-state.** Attribution here targets a
*brand/operation*, and sometimes a named individual behind an operator persona,
rather than a government. The affiliate confounder cuts both ways: shared operator
tooling inflates apparent cohesion across intrusions, while divergent affiliate TTPs
fragment it — so behavioural clustering that works for a coherent state team is
unreliable for a RaaS brand. Consistent with Topic 4, the analyst attributes to a
method-graded confidence and treats public naming as a government function (a
sanction or an indictment), not an analyst verdict.

**Boundary (method, not tradecraft).** This topic uses published secondary reporting
and analytic method only. It does not cover operational tradecraft and does not direct
students to live criminal infrastructure, forums, or markets. Actors are named only
where a government has attributed them (an ASD/ACSC or allied co-sealed advisory, or
an Australian sanction), and are framed as methodology, not verdicts.

**Key concepts:**
- The RaaS operator/affiliate split, revenue share, and why unconnected affiliates fragment TTPs
- Initial-access brokers as a market tier that decouples the intrusion timeline
- Leak-site and double-extortion economics as a biased intelligence source (selection bias in victim naming)
- Attribution to a brand/operator/named individual versus a government, and the affiliate confounder

**Australian context:** The ACSC Annual Cyber Threat Report identifies ransomware and
data-theft extortion among the most destructive threats to Australian organisations.
Government attribution of criminal actors is consequential here: Australia has
sanctioned named individuals under the *Autonomous Sanctions Act 2011* (Aleksandr
Ermakov, 2024, for the Medibank Private breach; Dmitry Khoroshev / "LockBitSupp",
2024, for his leadership role in LockBit). The *Cyber Security Act 2024* adds a
ransomware-payment reporting duty that an analyst supporting an Australian
organisation must treat as both an intelligence signal and a reporting obligation.

---

## Labs & Exercises

### Lab 1: Diamond Model of an Intrusion

**Objective:** Apply the Diamond Model to a known, publicly documented intrusion.

**Prerequisites:**
- Topics 1 and 3

**Environment:**
- Operating System: any (analysis lab)
- Tools: a Diamond Model template, public intrusion reporting / ACSC advisories
  (free)
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Select a publicly documented intrusion (e.g. from an ACSC advisory or vendor
   report).
2. Populate all four Diamond vertices with evidence and sourcing.
3. Add meta-features (timestamp, phase, result) and link related events.
4. Pivot from one vertex (e.g. infrastructure) to hypothesise related activity.
5. State the confidence in each vertex and note evidence gaps.
6. Summarise the activity thread the diamond reveals.

**Expected Output:**

A fully populated Diamond Model with sourced vertices, meta-features, a pivot, and
confidence statements. Learners can justify each vertex from the reporting.

**Reflection Questions:**

1. Which vertex was best/worst supported by evidence, and why?
2. What did pivoting reveal that a single event did not?
3. Where would overreaching on attribution be a risk here?

---

### Lab 2: ATT&CK Actor Profile

**Objective:** Build an ATT&CK v19 actor profile from open-source reporting for an
Australian-relevant actor.

**Prerequisites:**
- Topics 2, 4, and 6 and Lab 1

**Environment:**
- Operating System: any
- Tools: ATT&CK Navigator (v19), ATT&CK Group pages, ACSC/vendor reporting (free)
- Minimum hardware: trivial

**Instructions:**

1. Choose an actor the ACSC reports as relevant to Australia/APAC.
2. Collect its known techniques from ATT&CK Groups/Software and reporting.
3. Build a Navigator layer; distinguish signature from commodity behaviour.
4. Apply attribution methodology: state the evidence and confidence, with explicit
   caveats (no overreach).
5. Translate the profile into the top techniques to hunt/detect.
6. Package a short, consumer-ready actor profile.

**Expected Output:**

A Navigator actor layer, an evidence/confidence assessment with caveats, prioritised
techniques, and a consumer-ready profile. Learners can defend the method while
acknowledging attribution limits.

**Reflection Questions:**

1. How did you separate signature behaviour from commodity tooling, and why does it
   matter?
2. Where did you deliberately stop short of attribution overreach?
3. How would this profile change a SOC's hunting priorities?


---

### Lab 3: Profiling a Government-Attributed RaaS Operation from Public Advisories

**Objective:** Analyse a government-attributed ransomware-as-a-service operation as an
intelligence target using only public, co-sealed advisories and ACSC reporting, and
evaluate where the operation's affiliate structure limits what can be attributed.

**Prerequisites:**
- Topic 7, Topics 2 and 4, and Lab 2

**Environment:**
- Operating System: any (analysis lab)
- Tools: the CISA/ACSC co-sealed LockBit advisories (AA23-165A, and the ASD's
  ACSC-co-sealed Citrix Bleed advisory AA23-325A), the ACSC Ransomware Profile —
  LockBit 3.0, and ATT&CK Navigator/Groups (v19) — all free
- Minimum hardware: trivial; within the 8 GB / 4-core / 50 GB spec

**Instructions:**

1. Read the co-sealed advisories and identify, in the source's own words, the
   operator/affiliate split and the revenue-share model.
2. Extract the reported TTPs and note explicitly where the advisory attributes
   variation to *unconnected affiliates* rather than to a single actor.
3. Build an ATT&CK v19 layer from the advisory-reported techniques. Mark every
   technique mapping **provisional (pending Framework Custodian verification)**, and
   annotate which behaviours are affiliate-variable versus operator-consistent (e.g.
   the ransomware and leak-site behaviour).
4. Assess the leak-site evidence from the advisories' descriptions only: state what
   victim naming does and does not support (selection bias; payers absent). Do **not**
   access any live leak site, forum, or criminal infrastructure.
5. Distinguish attribution to the brand/operation from attribution to the named,
   government-sanctioned individual (Khoroshev / "LockBitSupp"); cite the government
   action rather than asserting your own verdict.
6. Write a short intelligence note: what a defender can rely on, what the affiliate
   confounder makes uncertain, and how the *Cyber Security Act 2024* reporting duty
   would bear on an Australian victim.

**Expected Output:**

An advisory-sourced ATT&CK layer with affiliate-variance annotations and
provisional-mapping flags, a written critique of the leak site as a biased source,
and a one-page note that separates brand, operator, and named-individual attribution
with explicit confidence and caveats.

**Reflection Questions:**

1. Why does "sophistication" fail as a risk proxy for a RaaS brand, and how did the
   affiliate structure show up in the advisory's reported TTPs?
2. What did the leak-site evidence tell you, and what did selection bias hide?
3. How does attributing to a government-sanctioned individual differ from an analyst
   making their own public attribution (link to Topic 4)?

---

## Assessment

### Formative Assessment: Diamond & Attribution Drill

**Type:** Self-check exercise with answer key

**Description:** Given intrusion snippets, students place evidence on the Diamond
Model and rate attribution confidence with caveats. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3

**Feedback mechanism:** Answer key with model placements and confidence reasoning.

---

### Summative Assessment: Threat Actor Profile

**Type:** Analytical report

**Description:** For an Australian-relevant actor, students (a) analyse an intrusion
with the Diamond Model, (b) build an ATT&CK v19 actor profile, (c) apply attribution
methodology with confidence and caveats, and (d) translate the profile into
defensive priorities for an operational consumer.
 Where the chosen actor is a
financially motivated criminal organisation (e.g. a government-attributed
ransomware-as-a-service operation), students additionally evaluate how the
operator/affiliate split and the affiliate confounder change the profiling method and
the attribution target (brand, operator, or named individual). Deliverable: 2,500–3,000 word
profile with Navigator and Diamond artefacts. **Must teach/apply method, not assert
confident public attribution.**

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6, LO7

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Diamond Model analysis | LO1 |
| ATT&CK actor profile | LO2, LO4 |
| Attribution methodology & caveats | LO3 |
| Defensive priorities & product | LO5, LO6 |

| Criminal-org vs nation-state profiling (where applicable) | LO7 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Intrusion analysis | Rigorous, sourced Diamond Model | Sound | Partial | Weak |
| Actor profiling | Accurate, well-evidenced ATT&CK profile | Mostly accurate | Several errors | Inaccurate |
| Attribution responsibility | Appropriately caveated, no overreach | Mostly appropriate | Some overreach | Unsupported claims |
| Defensive translation | Clear, prioritised, actionable | Reasonable | Generic | Absent |
| Communication | Clear, consumer-appropriate | Clear with minor lapses | Disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC advisories & Annual Cyber Threat Report:** Research material on actors
  targeting Australian/APAC sectors.
- **Public attribution as a government function:** Analysts support, not pre-empt,
  ASD/Government attribution statements.
- **Australian incident examples:** Used (publicly attributed only) with method
  emphasised over conclusion.

- **Government attribution of named cybercriminals:** Australia has sanctioned
  Aleksandr Ermakov (2024, Medibank Private breach) and Dmitry Khoroshev /
  "LockBitSupp" (2024, LockBit leadership) under the *Autonomous Sanctions Act 2011* —
  used as examples of attribution as a government (not analyst) function.
- **Cyber Security Act 2024:** its ransomware-payment reporting duty is treated as
  both an intelligence signal and a reporting obligation an analyst supporting an
  Australian organisation must account for.
- **ACSC Annual Cyber Threat Report:** identifies ransomware and data-theft extortion
  among the most destructive threats to Australian organisations; used as research
  material.

---

## Further Reading

**Caltagirone, S., Pendergast, A. & Betz, C. (2013).** *The Diamond Model of Intrusion Analysis.* https://www.activeresponse.org/the-diamond-model/
> Relevance: The core analytic model of this unit; freely available.

**MITRE ATT&CK (v19, 2026).** *Groups & Software.* The MITRE Corporation. https://attack.mitre.org/groups/
> Relevance: The actor/technique reference for profiling; CC BY 4.0.

**MITRE Center for Threat-Informed Defense (2024–2026).** *Attack Flow & actor methodology.* CTID. https://github.com/center-for-threat-informed-defense
> Relevance: Supports campaign modelling and behaviour-based profiling.

**Australian Cyber Security Centre (2024).** *Threat advisories & Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au
> Relevance: Australian-relevant actor reporting used as research material (Australian source).

**Rid, T. & Buchanan, B. (2015).** *Attributing Cyber Attacks.* Journal of Strategic Studies.
> Relevance: A rigorous treatment of attribution as graded, probabilistic judgement (Topic 4).


**CISA, FBI, MS-ISAC & partners including ASD's ACSC (2023).** *Understanding Ransomware Threat Actors: LockBit (AA23-165A).* CISA. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
> Relevance: A government co-sealed advisory (ASD's ACSC among the authoring agencies) describing the RaaS operator/affiliate model and stating that unconnected affiliates make observed TTPs vary; the primary source for Topic 7 and Lab 3.

**Australian Signals Directorate / ACSC (2024).** *Australia's second ever cyber sanction imposed (LockBit — Dmitry Khoroshev).* ASD. https://www.cyber.gov.au/about-us/view-all-content/news-and-media/australias-second-ever-cyber-sanction-imposed
> Relevance: Australian government attribution and sanction of a named RaaS operator under the Autonomous Sanctions Act 2011; an example of attribution as a government function (Australian source).

**Parliament of Australia (2024–2025).** *Cyber Security Act 2024 (Cth); Cyber Security (Ransomware Payment Reporting) Rules 2025.* Federal Register of Legislation. https://www.legislation.gov.au/F2025L00278
> Relevance: Establishes the ransomware-payment reporting duty relevant to intelligence and reporting considerations for Australian organisations (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | CT02 |
| Unit Title | Threat Actor Research & Profiling |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Major |
| Major / Pathway | CTI |
| Prerequisites | CT01, OC01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Framework Version — MITRE ATT&CK | v19 (2026) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate) |
| Australian Legislation Referenced | Autonomous Sanctions Act 2011; Cyber Security Act 2024 (ransomware-payment reporting) — as method/reporting context |
