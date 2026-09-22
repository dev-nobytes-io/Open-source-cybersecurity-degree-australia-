# F04: Security Concepts & Principles

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

This unit establishes the conceptual vocabulary and mental models that every
other unit in the degree assumes. Before specialising, a practitioner needs a
firm grasp of what security is trying to achieve (confidentiality, integrity,
availability and beyond), how we reason about threats and risk, the core
defensive principles (defence in depth, least privilege, zero trust), and the
foundational technologies — cryptography, authentication, and access control —
that implement those principles. The unit is deliberately concept-led and
tool-light: its job is to make the learner fluent in *why* before later units
focus on *how*.



The unit has two halves. The first five topics are defender-side: objectives,
risk, principles, and the mechanisms that enforce them. Topics 7 and 8 turn the
system around and look at the adversary — first the shared vocabulary the rest of
this degree uses to describe what attackers do (MITRE ATT&CK), then the economy
the financially motivated ones operate in. Both are primitives, not integration:
they exist so that later units can say "T1190" or "initial-access broker" without
stopping to explain themselves.

---

## Prerequisites

- F01 — Networking Fundamentals
- F02 — Operating Systems & Administration

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Define** the core security objectives (CIA triad, plus authenticity,
   non-repudiation, and accountability) and explain their trade-offs.
2. **Explain** threat, vulnerability, and risk and describe how they combine to
   determine exposure.
3. **Describe** the foundational defensive principles — defence in depth, least
   privilege, separation of duties, fail-secure, and zero trust.
4. **Demonstrate** a basic threat-modelling process for a simple system using a
   recognised method (e.g. STRIDE).
5. **Explain** the role of cryptography, authentication, and access control in
   enforcing security objectives.

7. **Explain** the MITRE ATT&CK hierarchy — tactic, technique, sub-technique and
   procedure — stating what each level is used for and what it cannot do.
8. **Describe** the division of labour in the financially motivated cybercriminal
   economy and explain why it makes initial access a commodity and adversary
   "sophistication" a poor proxy for risk.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of
foundational security concepts: objectives, risk, defensive principles, and the
core enforcing technologies.

**Skills (AQF 7.2):** Students develop cognitive skills by reasoning about
threats and risk and by constructing a threat model, and communication skills by
articulating security trade-offs.

**Application (AQF 7.3):** Students apply these concepts to model and reason
about a realistic system, mapping principles to the Australian baseline controls
of the Essential Eight and ACSC ISM.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Security Control Assessor | SP-RSK-002 | T0177 | Perform security reviews and identify gaps in security architecture | Lab 1 — Threat Modelling a Web Application |
| NIST NICE DCWF | 2023 | Information Systems Security Manager | OV-MGT-001 | T0149 | Recommend resource allocations to mitigate identified risks | Lab 2 — Mapping Controls to the Essential Eight; Lab 3 — The Ransomware Supply Chain |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information security | SCTY | Level 3 | Throughout |

| Threat intelligence | THIN | Level 2 | Topic 8, Lab 3 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|


### MITRE ATT&CK

> Version pinned repo-wide at **v19** (content version observed as v19.2 on
> attack.mitre.org at the time of drafting). The root `TODO.md` records an open
> repo-wide audit of every ATT&CK reference against v19's structural changes, so
> treat the IDs below as **provisional** pending Framework Custodian sign-off.
> v19 split the former *Defense Evasion* tactic into **Stealth** (TA0005, which
> kept the old ID) and **Defense Impairment** (TA0112, new). Material written
> before v19 — including the coverage table in this repository's own
> `docs/frameworks.md` — still shows the older fourteen-tactic list.

| Framework | Version | Tactic | Technique | ID | Demonstrated In |
|---|---|---|---|---|---|
| MITRE ATT&CK | v19 | Resource Development | Acquire Access | T1650 | Topic 8; Lab 3 |
| MITRE ATT&CK | v19 | Initial Access | Exploit Public-Facing Application | T1190 | Topic 7; Lab 1 |
| MITRE ATT&CK | v19 | Initial Access | External Remote Services | T1133 | Lab 1 |
| MITRE ATT&CK | v19 | Initial Access | Phishing | T1566 | Topic 7; Lab 1 |
| MITRE ATT&CK | v19 | Initial Access | Drive-by Compromise | T1189 | Lab 1 |
| MITRE ATT&CK | v19 | Initial Access (multi-tactic) | Valid Accounts | T1078 | Topic 7; Lab 1 |
| MITRE ATT&CK | v19 | Impact | Data Encrypted for Impact | T1486 | Topic 8; Lab 1; Lab 3 |
| MITRE ATT&CK | v19 | Impact | Financial Theft | T1657 | Topic 8 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F04-K01 | Knowledge of security objectives (CIA, authenticity, non-repudiation, accountability) | Topic 1 |
| Knowledge | F04-K02 | Knowledge of threat, vulnerability, and risk and how they combine | Topic 2 |
| Knowledge | F04-K03 | Knowledge of defensive principles (defence in depth, least privilege, zero trust) | Topic 3 |

| Knowledge | F04-K05 | Knowledge of the MITRE ATT&CK tactic/technique/sub-technique/procedure hierarchy and the purpose and limits of each level | Topic 7 |
| Knowledge | F04-K06 | Knowledge of the financially motivated cybercriminal division of labour (developer, affiliate, initial-access broker, infrastructure provider, extortion platform, launderer) | Topic 8 |
| Skill | F04-S01 | Skill in threat modelling a system with STRIDE | Lab 1 |

| Skill | F04-S03 | Skill in grounding a threat model in a published, attributed adversary behaviour set and distinguishing evidenced from unevidenced threats | Lab 1 |
| Ability | F04-A01 | Ability to reason about and prioritise security risks and trade-offs | Lab 1; Summative |

| Ability | F04-A03 | Ability to reason from adversary economics to defensive priorities and to the Australian obligations a payment decision triggers | Lab 3; Summative |
| Task | T0177 | Perform security reviews and identify gaps in security architecture | Lab 1 |
| Task | T0149 | Recommend resource allocations to mitigate identified risks | Lab 2 |

---

## Topics

### Topic 1: Security Objectives — CIA and Beyond

The CIA triad — confidentiality, integrity, availability — is the starting point
for reasoning about security, but it is incomplete. This topic adds authenticity,
non-repudiation, and accountability, and explores the tension between objectives
(e.g. availability vs confidentiality). Learners practise classifying a control
or incident by which objective it protects or violates.

**Key concepts:**
- CIA triad and its extensions
- Trade-offs and prioritisation between objectives
- Mapping controls and incidents to objectives

---

### Topic 2: Threats, Vulnerabilities, and Risk

Risk is the intersection of a threat exploiting a vulnerability to cause impact.
This topic defines each term precisely, introduces threat actors and their
motivations, and frames risk as something to be assessed and treated (accept,
mitigate, transfer, avoid). It establishes the risk vocabulary that SC01 later
develops formally.

**Key concepts:**
- Threat × vulnerability × impact as a model of risk
- Threat actor types and motivations
- Risk treatment options

**Australian context:** ASD's *Annual Cyber Threat Report* grounds threat-actor
discussion in the real Australian threat landscape.

**Where this goes next:** this topic names the actor *categories*. It does not
give you a way to say what an actor actually did, and it does not explain how the
financially motivated ones are organised. Topic 7 supplies the vocabulary and
Topic 8 supplies the economics — read the three together.

---

### Topic 3: Defensive Principles

Good security design follows durable principles. This topic covers defence in
depth, least privilege, separation of duties, fail-secure defaults, complete
mediation, economy of mechanism, and the modern reframing of these ideas as
**zero trust**. Learners learn to recognise these principles (and their absence)
in real designs.

**Key concepts:**
- Defence in depth and layered controls
- Least privilege and separation of duties
- Zero trust as "never trust, always verify"

---

### Topic 4: Threat Modelling

Threat modelling is the structured practice of anticipating how a system could be
attacked, before it is built or deployed. This topic introduces a repeatable
process — define the system, identify assets and entry points, enumerate threats
(using STRIDE), and decide on mitigations. It is the most directly transferable
skill in the unit and recurs in SC02 and the Security Engineering major.

**Key concepts:**
- The threat-modelling process and data-flow diagrams
- STRIDE as a threat-enumeration framework
- From threats to prioritised mitigations

---

### Topic 5: Cryptography, Authentication, and Access Control

Principles need mechanisms. This topic gives a conceptual (not mathematical)
grounding in cryptography (symmetric vs asymmetric, hashing, digital signatures,
PKI/TLS), authentication (something you know/have/are, MFA), and access control
models (DAC, MAC, RBAC, ABAC). The emphasis is on what each provides and when to
use it.

**Key concepts:**
- Symmetric vs asymmetric cryptography; hashing and signatures
- Authentication factors and multi-factor authentication
- Access control models and their trade-offs

**Australian context:** Multi-factor authentication is an Essential Eight
mitigation; this topic explains the security objective it serves.

---

### Topic 6: From Principles to Baseline Controls

This topic closes the loop between abstract principles and the concrete controls
organisations are actually expected to implement. It maps each defensive
principle to baseline controls and introduces the ASD Essential Eight as
Australia's flagship baseline, showing how each of the eight mitigations
implements one or more of the principles covered in the unit.

**Key concepts:**
- From principle to control to configuration
- The ASD Essential Eight and its maturity model
- Why baselines exist and their limits



### Topic 7: ATT&CK as Shared Vocabulary

Topic 2 gave you actor *categories*. It gave you no way to say what an actor
actually did. MITRE ATT&CK is the vocabulary the rest of this degree uses for
that, and it has four levels. The commonest mistake — in student work and in
industry — is using one level to do another level's job.

**Tactic — the adversary's goal at a moment.** A tactic answers *why* a behaviour
happened: they needed credentials, they needed to get the data out. Enterprise
ATT&CK v19 has **fifteen** tactics:

| # | Tactic | ID |
|---|---|---|
| 1 | Reconnaissance | TA0043 |
| 2 | Resource Development | TA0042 |
| 3 | Initial Access | TA0001 |
| 4 | Execution | TA0002 |
| 5 | Persistence | TA0003 |
| 6 | Privilege Escalation | TA0004 |
| 7 | Stealth | TA0005 |
| 8 | Defense Impairment | TA0112 |
| 9 | Credential Access | TA0006 |
| 10 | Discovery | TA0007 |
| 11 | Lateral Movement | TA0008 |
| 12 | Collection | TA0009 |
| 13 | Command and Control | TA0011 |
| 14 | Exfiltration | TA0010 |
| 15 | Impact | TA0040 |

Two are routinely dropped from summaries, and both matter here.
**Reconnaissance** (TA0043) and **Resource Development** (TA0042) describe what an
adversary does *before* touching your network — and Resource Development is where
the criminal supply chain of Topic 8 lives. Buying a foothold from a broker is
`T1650` Acquire Access, a Resource Development technique. A defender who believes
the kill chain begins at Initial Access has no vocabulary at all for the market
that supplies it.

**State the version, every time — and here is why.** ATT&CK v19 split the old
*Defense Evasion* tactic into **Stealth** (TA0005 — hiding and blending in) and
**Defense Impairment** (TA0112 — actively breaking the defender's tooling,
logging or trust controls). TA0005 kept its identifier and changed its name;
TA0112 is new. Any list of "the 14 ATT&CK tactics" that includes "Defense
Evasion" is therefore pre-v19 — *including the coverage table in this
repository's own* `docs/frameworks.md`, which the root `TODO.md` has flagged for
audit. You can watch the change from the technique side too: `T1078` Valid
Accounts now lists Stealth among its tactics where it once listed Defense
Evasion. A technique or tactic reference without a version is an undated claim,
and undated claims rot silently.

**Technique — the general method.** `T####`. "Exploit Public-Facing Application"
(`T1190`) names a class of behaviour without saying which product, which CVE or
which exploit. Techniques are the working unit for actor profiling and for
coverage conversations: stable enough to compare two unrelated intrusions,
specific enough to argue about a control.

**Sub-technique — the variant that changes the answer.** `T####.###`. `T1566`
Phishing splits into Spearphishing Attachment (`.001`), Spearphishing Link
(`.002`) and Spearphishing via Service (`.003`). The split exists because the
*defensive answer differs*: attachment is an attachment-sandboxing and macro-policy
problem, link is a proxy and URL-rewriting problem, service is an egress and
account-federation problem. Claiming coverage of `T1566` because you filter
attachments is the single most common way a coverage claim inflates.

**Procedure — what actually happened.** A procedure is not an identifier. It is
the specific, observed implementation by a specific actor in a specific
intrusion: the command line, the service name, the file path, the user agent.
ATT&CK records these as free-text *procedure examples* under each technique.
Procedures are the unit of **evidence** — and the unit of **brittleness**,
because a procedure changes between operators while the technique above it stays
put. That is the Pyramid of Pain argument, visible in ATT&CK's own structure.

**What ATT&CK is not.** It is *not a risk model*: it says nothing about
likelihood or impact for your organisation. It is *not a maturity model*:
technique counts are not a security score, and a matrix coloured green measures
what you looked for, not what you would catch. It is *not exhaustive*: it is a
curated record of *observed* behaviour, so absence from ATT&CK is not evidence of
absence. It is *not an ordering*: the tactic columns are a convenient reading
order, not a required sequence — real intrusions loop, skip and revisit.

**Key concepts:**
- Tactic (goal) → technique (method) → sub-technique (variant) → procedure
  (observation), and the job each level does
- The fifteen Enterprise tactics in v19, including Reconnaissance and Resource
  Development
- Version-dependence: the v19 Stealth / Defense Impairment split, and why a
  mapping without a version is unusable
- The limits: not a risk model, not a maturity score, not exhaustive, not ordered

**Australian context:** ASD and ACSC co-sealed advisories publish actor behaviour
as ATT&CK technique tables — the LockBit advisory used in Lab 1 (AA23-165A) is
one — so reading ATT&CK is a precondition for using Australian government threat
reporting at all.

---

### Topic 8: The Cybercriminal Ecosystem

Most organisations are not attacked by a state. They are attacked by a business.
The financially motivated end of the threat landscape is an economy with
specialisation, brands, suppliers, price competition and reputational mechanics —
and it is its **structure**, not its "sophistication", that should drive your
defensive priorities.

**Scope, stated plainly.** This topic is taught entirely from published
government advisories, sanctions instruments and official threat reporting. It
covers how the economy is *organised* and what that implies for defence. It does
not name or describe marketplaces, forums, leak sites or criminal services; it
gives no pricing, procurement or contact detail; and it contains no operational
tradecraft. Nothing here is usable to participate. Everything here is usable to
prioritise controls and to meet a legal obligation.

**The division of labour.** Treat it as a supply chain with at least six roles:

| Role | What they supply | Where it sits in ATT&CK |
|---|---|---|
| Developer / operator ("the core") | The encryptor, the builder, the management panel, the brand | Resource Development |
| Affiliate | Runs the intrusion end to end; takes the larger share of any payment | Initial Access through Impact |
| Initial-access broker (IAB) | Sells an existing foothold in an already-compromised organisation | `T1650` Acquire Access (Resource Development) |
| Infrastructure provider | Hosting that does not answer abuse complaints or law-enforcement requests | Resource Development |
| Extortion / leak platform operator | The publication threat that makes *not* paying expensive | Impact |
| Negotiation and laundering services | Converts extortion into spendable money | `T1657` Financial Theft (Impact) |

ATT&CK models the brokerage directly: `T1650` Acquire Access sits in **Resource
Development** and describes adversaries buying access to previously compromised
systems rather than earning it, noting that brokers favour systems that lack
security monitoring or carry high privilege. Access is a purchasable input, and
your monitoring gap is part of what sets its price.

**The economics, from the primary source.** The ACSC co-sealed advisory
*Understanding Ransomware Threat Actors: LockBit* (AA23-165A, 2023) describes how
a ransomware-as-a-service brand competes for affiliates. Two of its findings are
this whole topic in miniature:

1. The brand assured affiliate payment "by allowing affiliates to receive ransom
   payments before sending a cut to the core group" — a trust mechanism in a
   market where no participant can sue another. The brand is competing for
   **labour**.
2. The brand developed "a simplified, point-and-click interface for its
   ransomware, making it accessible to those with a lower degree of technical
   skill." The brand is deliberately **lowering the skill floor** to widen its
   affiliate pool.

Four defensive consequences follow.

**Consequence 1 — access is a commodity, so exposure is inventory.** If a
foothold can be bought, you are not defending against one group's preferred entry
method. You are defending against a market that will sell *any* working foothold
to whoever pays. Every internet-facing service, every account without MFA, every
unpatched edge appliance is potential stock in someone else's inventory. This
reframes Topic 6: patching applications, patching operating systems and
multi-factor authentication are not hygiene, they are **supply interdiction** —
they remove your organisation from the saleable stock.

**Consequence 2 — "sophistication" is a poor risk proxy.** The same advisory
records that "due to the large number of unconnected affiliates in the operation,
LockBit ransomware attacks vary significantly in observed tactics, techniques,
and procedures (TTPs)". The brand name tells you very little about how the
intrusion will actually run, because the brand is not the crew. Three corollaries
defenders get wrong:

- **Brand is not crew.** Australia's October 2024 designations included Aleksandr
  Ryzhenkov, a senior figure in one criminal group who has separately been
  identified as an affiliate of a different ransomware brand. People move between
  brands; a brand is a franchise, not an org chart.
- **Takedowns remove infrastructure, not capability.** People, skills and
  purchased access survive a seizure, and rebranding is cheap. Defend against
  *behaviours* — techniques, per Topic 7 — not names.
- **"We're not a sophisticated enough target" is backwards.** A low-skill
  affiliate using a point-and-click builder against purchased access inflicts the
  same encryption and the same data theft as a capable one. Targeting in this
  economy is opportunistic and price-driven, not prestige-driven.

**Consequence 3 — extortion is multi-layered, so backups are only half an
answer.** ASD's *Annual Cyber Threat Report 2024–25* describes criminals
conducting multiple layers of extortion: stealing data before encrypting it,
threatening release, and attempting to extort not only the network owner but the
individuals and entities named in the stolen data. A restore fixes availability.
It does nothing whatever for confidentiality. Detection must therefore reach
**Collection and Exfiltration**, upstream of `T1486` Data Encrypted for Impact —
by the time encryption runs, the leverage already exists.

**Consequence 4 — detection capability is the binding constraint.** In FY2024–25
ASD responded to 138 ransomware incidents, and 39% of those became known to the
affected entity only because ASD contacted *them*. Roughly two in five did not
know they had been compromised. Every control argument in this unit quietly
assumes somebody is watching; that figure is what happens when nobody is.

**Australian context — why defenders are taught this.**

*Sanctions.* Australia has designated named cyber actors under the **Autonomous
Sanctions Act 2011 (Cth)**: an individual sanctioned in 2024 over the 2022
Medibank compromise, reported as the first use of the cyber sanctions framework;
three figures associated with the Evil Corp group in October 2024; and a hosting
provider together with five individuals in February 2025, reported as the first
designation of a business and the first for *supplying infrastructure* rather
than conducting the intrusion. Dealing with a designated person or entity is a
criminal offence. For a defender this turns attribution from an intelligence
nicety into a legal question — *who* you would be paying determines whether
paying is lawful at all — and the infrastructure designation shows the offence
reaches suppliers, not just operators.

*Reporting.* The **Cyber Security Act 2024 (Cth)** (No. 98 of 2024), Part 3,
section 27, requires a reporting business entity to give the designated
Commonwealth body a ransomware payment report within **72 hours** of making a
ransomware payment, or of becoming aware that one was made on its behalf. The
obligation commenced on 30 May 2025 and reaches entities carrying on business in
Australia at or above the annual turnover threshold set in the supporting Rules,
plus responsible entities for critical infrastructure assets regardless of
turnover. Payment is a regulated, reportable event with a clock on it — so the
incident plan needs a legal step, not only a technical one.

Together these answer the question "why teach defenders the criminal economy?":
because in Australia the decision to pay is simultaneously a commercial decision,
a sanctions-compliance decision and a statutory reporting trigger, and none of
the three can be made without knowing who is on the other end and how they are
organised.

**Key concepts:**
- The six-role division of labour, and the ATT&CK tactic each role occupies
- Affiliate economics: payment order and tooling accessibility as competition for
  labour, and the deliberately lowered skill floor
- Why commoditised access makes exposure "inventory", and why sophistication is a
  poor risk proxy
- Multi-layered extortion: why exfiltration detection, not backup, answers the
  data-theft half
- Sanctions exposure and the 72-hour ransomware payment report as the Australian
  legal consequences of all of the above

**Australian context:** ASD's *Annual Cyber Threat Report*, cyber designations
under the Autonomous Sanctions Act 2011 (Cth), and the Part 3 ransomware payment
reporting obligation in the Cyber Security Act 2024 (Cth) are the three
Australian anchors for this topic.

---

## Labs & Exercises

### Lab 1: Threat Modelling a Web Application

**Objective:** Produce a STRIDE threat model for a simple web application in
which every threat is tested against a published, attributed adversary behaviour
set — and demonstrate what changes when the adversary is real rather than
implied.

**Prerequisites:**
- Topics 1–4, 7 and 8
- A diagramming tool (draw.io / diagrams.net, free)

**Environment:**
- Operating System: any (this is a paper analysis lab — nothing is executed,
  scanned or attacked)
- Tools: draw.io (free, browser or desktop), a PDF reader, a text editor
- Sources: the advisory *Understanding Ransomware Threat Actors: LockBit*
  (AA23-165A), co-sealed by ASD's ACSC, and the relevant technique pages on
  attack.mitre.org. Both are free. **Download the advisory PDF in advance and
  distribute it with the lab pack** — government advisory sites frequently block
  automated or filtered access, and the lab must be completable offline.
- Minimum hardware: trivial; no VM, no GPU; runs on any machine within spec

**Instructions:**

1. **Model the system.** Take a three-tier web app (browser → web/app server →
   database) with a login feature and an internet-facing administrative
   interface. Draw a data-flow diagram showing components, data flows and trust
   boundaries.
2. **Run STRIDE blind — this is your control.** Timebox 20 minutes. One pass, no
   research, no advisory. For each element and flow, enumerate threats using
   STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of
   service, Elevation of privilege). Record the count per letter. **Keep this
   table; you will compare against it in step 7.**
3. **Now bring in the adversary.** Open AA23-165A. From its Initial Access table,
   extract the technique identifiers it attributes to the actor — you should find
   `T1189` Drive-by Compromise, `T1190` Exploit Public-Facing Application,
   `T1133` External Remote Services, `T1566` Phishing and `T1078` Valid Accounts.
   From its Impact table, take `T1486` Data Encrypted for Impact. Note which
   ATT&CK version the advisory was written against, and state whether it predates
   the v19 Stealth / Defense Impairment split from Topic 7.
4. **Re-run STRIDE with an evidence column.** For each threat, mark it
   *advisory-evidenced* (and name the technique ID), *plausible but unevidenced*,
   or *out of scope for this actor*. Do not invent attributions: if the advisory
   does not say it, it is not evidenced. "Plausible but unevidenced" is a
   legitimate and common answer.
5. **Map each evidenced threat** to the trust boundary it crosses and the security
   objective it violates (Topic 1).
6. **Prioritise on evidence and exposure, not instinct.** Each one-line
   justification must cite either a technique ID or a specific exposure fact
   visible on your DFD.
7. **Compare the two passes.** Which threats gained priority? Which lost it?
   Most importantly: which adversary behaviours does the advisory document that
   your blind STRIDE pass did not generate *at all*?
8. **Close the loop.** For your top three, name the Essential Eight mitigation (if
   any) that interdicts it, and say which ecosystem role from Topic 8 that
   mitigation disrupts.

**Expected Output:**

A data-flow diagram with trust boundaries; **two** STRIDE tables — the blind pass
and the evidence-grounded pass — the second carrying an evidence column with
technique IDs; a prioritised top three, each tied to a boundary, an objective, a
technique ID and an Essential Eight mitigation; and a short comparison paragraph.
Learners can point to a specific line in a published advisory for every
"evidenced" claim they make, and can say honestly which of their threats rest on
nothing but plausibility.

**Reflection Questions:**

1. Which STRIDE letters produced threats the advisory does not evidence at all?
   Does that mean those threats are not real — and what would it take to find out?
2. STRIDE enumerates what could go wrong with the *system*; ATT&CK records what
   adversaries *have done*. Where did each one find something the other missed?
3. The advisory notes that this brand's affiliates "vary significantly in observed
   TTPs". What does that do to the confidence you can place in your evidence
   column — and to any defence built around one named group?
4. Which of your top three would still matter if the adversary had simply
   *purchased* access (`T1650`) instead of earning it?

---

### Lab 2: Mapping Controls to the Essential Eight

**Objective:** Map defensive principles and a set of controls to the ASD
Essential Eight, demonstrating understanding of how principles become baselines.

**Prerequisites:**
- Topics 3, 5, and 6

**Environment:**
- Operating System: any
- Tools: the ACSC Essential Eight Maturity Model (free, online), a spreadsheet
  or markdown table
- Minimum hardware: trivial

**Instructions:**

1. List the eight mitigations of the ASD Essential Eight from the ACSC source.
2. For each mitigation, identify which defensive principle(s) from Topic 3 it
   implements and which security objective(s) from Topic 1 it protects.
3. Given a short scenario (a small business with a default Windows environment),
   assess at a high level which mitigations are likely absent.
4. Recommend an implementation order for the missing mitigations and justify it
   in risk terms.
5. Note one limitation of relying solely on the Essential Eight.

**Expected Output:**

A completed mapping table (mitigation → principle → objective), a gap assessment
for the scenario, and a justified implementation order. Learners can explain why
baselines are necessary but not sufficient.

**Reflection Questions:**



---

### Lab 3: The Ransomware Supply Chain — Roles, Controls and Obligations

**Objective:** Analyse the financially motivated cybercriminal division of labour
from published sources, map each role to the ATT&CK tactics it occupies, and
derive prioritised controls plus the Australian legal obligations a payment
decision triggers.

**Prerequisites:**
- Topics 6, 7 and 8

**Scope boundary — read before starting:**
This lab uses **official government advisories, sanctions instruments and
published threat reports only**. Students must not seek out, visit, screenshot or
cite criminal forums, marketplaces, leak sites or any actor-controlled
infrastructure; doing so places the work out of scope and fails the lab. Nothing
in this lab involves acquiring, executing or emulating malicious capability. The
object of study is how the economy is *organised* and what that implies for
defence.

**Environment:**
- Operating System: any (paper analysis)
- Tools: a PDF reader, and a spreadsheet or markdown table (LibreOffice Calc,
  free/OSS)
- Sources: AA23-165A (ACSC co-sealed); ASD's *Annual Cyber Threat Report
  2024–25*; the attack.mitre.org page for `T1650` Acquire Access. All free.
  **Distribute the two PDFs with the lab pack** so the lab works offline.
- Minimum hardware: trivial; no VM, no container, no network exposure

**Instructions:**

1. **Build the role × tactic matrix.** Rows: the six roles from Topic 8. Columns:
   the ATT&CK v19 tactics. Mark which tactics each role owns. **Every mark needs
   a citation** — the advisory, the ACTR, or the relevant ATT&CK technique page.
   An unmarked cell is a claim too; be ready to defend the blanks.
2. **Read the `T1650` Acquire Access page.** Record which tactic it sits in, and
   what it says brokers prioritise when choosing which systems to compromise.
   Then, in two sentences: explain why that priority makes *your* monitoring gap
   commercially valuable to somebody else.
3. **Extract the two recruitment mechanisms** from AA23-165A (the payment order,
   and the accessibility of the tooling). For each, state what it predicts about
   the distribution of attacker skill you should plan your defences around.
4. **Scenario.** An Australian professional-services firm: approximately $8
   million annual turnover, *not* a responsible entity for a critical
   infrastructure asset, 60 staff, an internet-facing practice-management portal,
   no MFA on remote access, nightly backups to a network share.
   1. For each of three proposed controls — MFA on all remote access; patching
      internet-facing applications within two weeks; egress monitoring plus
      offline backup copies — identify which **ecosystem role** it disrupts.
   2. Rank the three, justifying each by the role it disrupts and the ATT&CK
      tactic it denies.
   3. State which control does **nothing** for the data-theft half of
      multi-layered extortion, and why.
5. **Obligations note (one page).** If this firm pays:
   1. Does the reporting obligation in Part 3, section 27 of the Cyber Security
      Act 2024 (Cth) apply to it? To whom is the report made, and within what
      period?
   2. Given Australia's cyber designations under the Autonomous Sanctions Act
      2011 (Cth), what question must be answered about the *recipient* before a
      payment is made — and why can the victim organisation rarely answer it
      alone?
   3. Name one concrete reason the 72-hour clock is hard to meet during an active
      incident.
6. **Conclusion (one paragraph).** Explain why "we are too small to be a
   sophisticated target" is an incorrect inference from this ecosystem's
   structure.

**Expected Output:**

A role × tactic matrix with a citation per mark; the short `T1650` analysis; the
three controls ranked with role-and-tactic justifications and the identified gap;
a one-page obligations note answering (a) to (c); and the concluding paragraph.
Learners can explain how a defensive priority changes when access is *purchased*
rather than earned, and can name the point at which a technical incident becomes
a legal one.

**Reflection Questions:**

1. Which single control in your ranking removes the firm from a broker's saleable
   inventory, and which merely limits the damage after a sale has happened?
2. ASD reported that it notified the entity in 39% of the ransomware incidents it
   responded to in FY2024–25. Which of your controls addresses that, and which
   part of the Essential Eight does not?
3. If the brand that attacked this firm is taken down next month, which of your
   controls become less useful? What does your answer say about building a
   control argument around a named adversary?
4. Why is the sanctions question a board question rather than a SOC question?

---

## Assessment

### Formative Assessment: Concepts & Principles Quiz

**Type:** Self-check quiz with answer key

**Description:** A quiz testing precise use of terminology — distinguishing
threat/vulnerability/risk, classifying controls by objective, and matching
principles to examples. Self-marked.

**Learning Outcomes Assessed:** LO1, LO2, LO3

**Feedback mechanism:** Answer key with explanations and common-misconception
notes.

---

### Summative Assessment: Security Design Analysis

**Type:** Case-study analysis report

**Description:** Students are given a description of a small organisation's IT
environment and a recent (fictional but realistic) incident, together with **one
published, attributed advisory** to use as the adversary evidence base. They must
(a) identify which security objectives were violated, (b) produce a focused threat
model of the affected system in which each threat is marked evidenced or
unevidenced against the advisory, with correct ATT&CK technique identifiers and a
stated framework version, (c) recommend prioritised controls mapped to defensive
principles, the Essential Eight, and the ecosystem role each control disrupts, and
(d) explain the residual risk, including whether an Australian reporting or
sanctions obligation would be engaged. Deliverable: 1,500–2,000 word report with a
diagram.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6, LO7, LO8

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Objective-violation analysis | LO1, LO2 |
| Evidence-grounded threat model with ATT&CK identifiers | LO4, LO7 |
| Prioritised controls + Essential Eight mapping | LO3, LO6 |
| Ecosystem-role reasoning and Australian obligations in residual risk | LO8 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Conceptual accuracy | Precise, correct use of all core concepts | Mostly precise with minor slips | Several conceptual errors | Frequent misuse of core terms |
| Threat modelling | Thorough, well-structured, prioritised model | Solid model with minor gaps | Partial model; weak prioritisation | Little structured modelling |

| Adversary grounding | Threats tied to specific published behaviours; ATT&CK IDs correct and versioned; evidenced and unevidenced honestly separated | Mostly grounded; minor identifier or attribution slips | Generic "hackers"; little published evidence cited | No adversary, or attributions invented |
| Communication | Clear, structured, professional | Clear with minor lapses | Understandable but disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Examined directly in Topic 6 and Lab 2 as Australia's
  baseline control set, with each mitigation traced to a principle.
- **ACSC Annual Cyber Threat Report:** Grounds the threat-actor discussion in
  Topic 2 in the real Australian threat landscape.

- **ASD Annual Cyber Threat Report 2024–25:** Supplies the current incident and
  extortion figures used in Topics 2 and 8 and in Lab 3.
- **Autonomous Sanctions Act 2011 (Cth):** Topic 8 and Lab 3 examine Australia's
  cyber designations — an individual sanctioned over the 2022 Medibank compromise,
  Evil Corp figures in October 2024, and a hosting provider with five individuals
  in February 2025 — and why dealing with a designated person makes attribution a
  legal question that precedes any payment decision.
- **Cyber Security Act 2024 (Cth), Part 3 s 27:** The 72-hour ransomware payment
  reporting obligation, analysed directly in Lab 3's obligations note.
- **ACSC co-sealed advisories:** AA23-165A supplies the attributed adversary
  behaviour that grounds Lab 1's threat model and Lab 3's role analysis.

---

## Further Reading

**Anderson, R. (2020).** *Security Engineering (3rd ed.).* Wiley. https://www.cl.cam.ac.uk/~rja14/book.html
> Relevance: A freely available, authoritative treatment of security principles, cryptography, and access control underpinning this unit.

**Shostack, A. (2014).** *Threat Modeling: Designing for Security.* Wiley.
> Relevance: The standard reference for the STRIDE-based threat modelling practised in Lab 1.

**Australian Cyber Security Centre (2024).** *Annual Cyber Threat Report.* ACSC. https://www.cyber.gov.au/about-us/reports-and-statistics
> Relevance: The authoritative source on the Australian threat landscape used in Topic 2 (Australian source).

**Australian Cyber Security Centre (2023).** *Essential Eight Maturity Model.* ACSC. https://www.cyber.gov.au/essential-eight
> Relevance: The Australian baseline control set mapped in Topic 6 and Lab 2 (Australian source).



**MITRE (2026).** *Enterprise Tactics — MITRE ATT&CK.* The MITRE Corporation. https://attack.mitre.org/tactics/enterprise/
> Relevance: The authoritative tactic list used in Topic 7. The page states the content version in its footer — students must cite that version alongside any mapping they make.

**MITRE.** *Acquire Access (T1650) — MITRE ATT&CK.* The MITRE Corporation. https://attack.mitre.org/techniques/T1650/
> Relevance: ATT&CK's own modelling of initial-access brokerage, and the anchor for the broker material in Topic 8 and Lab 3.

**ACSC, CISA, FBI and international partners (2023).** *Understanding Ransomware Threat Actors: LockBit* (AA23-165A). https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-165a
> Relevance: An ACSC co-sealed advisory documenting ransomware-as-a-service affiliate economics alongside a full technique table; the adversary evidence base for Lab 1 and Lab 3 (Australian source).

**Australian Signals Directorate (2025).** *Annual Cyber Threat Report 2024–25.* ASD. https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025
> Relevance: The current Australian threat-landscape figures used in Topics 2 and 8 and Lab 3; supersedes the 2024 edition cited above (Australian source).

**Australian Government (2025).** *Cyber Security (Ransomware Payment Reporting) Rules 2025.* Federal Register of Legislation. https://www.legislation.gov.au/F2025L00278/asmade/text
> Relevance: The Rules made under the Cyber Security Act 2024 (Cth) (No. 98 of 2024) that set who must report; the statutory basis for Lab 3's obligations note (Australian source).

**Australian Signals Directorate.** *Cyber sanctions — news and media.* ASD / cyber.gov.au. https://www.cyber.gov.au/about-us/view-all-content/news-and-media/cyber-sanction-imposed-russian-cybercriminal-2022-medibank-private-compromise
> Relevance: The Australian government's own account of the first cyber designation under the Autonomous Sanctions Act 2011 (Cth), used in Topic 8 (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F04 |
| Unit Title | Security Concepts & Principles |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01, F02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |

| Framework Version — MITRE ATT&CK | v19 (provisional — repo-wide audit open in root TODO.md) |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Cyber Security Act 2024 (Cth) Part 3 s 27; Autonomous Sanctions Act 2011 (Cth) — both examined in Topic 8 and Lab 3 |
