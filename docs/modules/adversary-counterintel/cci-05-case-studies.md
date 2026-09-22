# CCI-05: Case Studies in the Adversary Economy

> **Module type:** Extension module (counter-intelligence deep dive) — part of [EXT-CCI](index.md)
> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-09-22
> **Domain Expert:** _Unassigned — required before Practitioner Approved (CTI, financial-crime intelligence, or law-enforcement cyber background)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must have worked adversary attribution, financial-crime intelligence, or a government cyber programme)_

!!! warning "Not a credit-bearing unit"
    CCI-05 is the fifth module of the [EXT-CCI series](index.md), an optional extension that sits outside the 66-unit / 160 CP degree structure. It carries **0 CP** and does not appear in [`docs/ksat-coverage.md`](../../ksat-coverage.md) or the [Program Builder](../../program-builder/index.md), both of which are generated from credit-bearing units only. A delivery partner wanting to recognise it should use the Tier 1 badge mechanism in [`docs/curriculum/micro-credentials-framework.md`](../../curriculum/micro-credentials-framework.md).

!!! danger "Read the series ground rules first"
    This module is bound by the [series index](index.md) danger box and by [CCI-01](cci-01-the-cybercriminal-enterprise.md), [CCI-02](cci-02-the-criminal-economy.md), [CCI-03](cci-03-the-service-economy.md) and [CCI-04](cci-04-state-sponsored-operations.md). In one line each: it is **analysis of publicly documented adversaries and operations, not a manual**; it contains **no operational tradecraft** — no exploit detail and no how-to, and **each case here is analysed for what it shows about organisation, economics, service structure, or state relationship, never for reusable technique** (if a sentence would help someone reproduce an attack, it is not in this module); **legitimate security businesses, researchers and conferences are never presented as criminals** — where a security firm appears in a case it appears as the *lawful* disruptor, investigator, or infiltrator, not as a wrongdoer (the dual-use economy itself is CCI-06, not yet written); and **named individuals appear only where a government has publicly charged, sanctioned, or formally attributed them**, described as *alleged* / *accused* / *attributed* — an indictment, an arrest, or a sanction is an allegation or an executive finding, **not a court's verdict of guilt**.

    For the **state-linked cases** (Stuxnet, Bangladesh Bank, NotPetya), this module keeps the discipline [CCI-04](cci-04-state-sponsored-operations.md) built: it applies the **same evidence standard to every state**, attributes every claim to its source **with a confidence level and caveats**, and distinguishes throughout between (a) official government attribution, (b) investigative journalism and leaks, and (c) analytic inference. **Stuxnet is US/Israel-*attributed* through investigative journalism (Sanger; Zetter) and has *not* been officially confirmed by either government — this module says so and does not upgrade it.** For the **TeamPCP** case, the two people arrested in Perth in August 2026 are **accused / alleged**, entitled to the presumption of innocence, and this module asserts no guilt; where a specific detail of the arrest could not be confirmed against reputable reporting, it is flagged provisional and described at group level.

---

## Overview

[CCI-01](cci-01-the-cybercriminal-enterprise.md) built the lens of **organisation**, [CCI-02](cci-02-the-criminal-economy.md) the lens of **money and laundering**, [CCI-03](cci-03-the-service-economy.md) the lens of the **service economy**, and [CCI-04](cci-04-state-sponsored-operations.md) the lenses of **state nexus** and **attribution confidence**. Those four modules taught the frameworks in the abstract, illustrated with fragments of cases. This module does the opposite: it takes **whole, publicly documented operations** and reads each one *through* those lenses, end to end, the way an analyst actually works — not one framework at a time, but all of them at once on a single real event.

The organising idea is that a mature case is never *only* an organisation problem, *only* a money problem, or *only* a state problem. Colonial Pipeline is simultaneously a **service-economy** story (a ransomware-as-a-service affiliate model) and a **money** story (an on-chain seizure). The Bangladesh Bank heist is simultaneously a **state** story (DPRK-attributed) and a **money** story (a laundering chain through casinos). TeamPCP is simultaneously an **organisation** story (a supply-chain extortion crew), a **service/economy** story (poisoned open-source packages as the delivery pipeline), and an **attribution / disruption** story (a lawful infiltration by a security firm and an Australian arrest). The skill this module assesses is holding several lenses on one case at once and saying which parts of the public record support which reading, and at what confidence.

This is therefore the **integrative** module of the series. It does **not** re-teach the frameworks — it applies them, cross-referencing back to the module that built each one rather than restating it. And it holds the series' hardest line without exception: every case is analysed for what it teaches about **how the adversary was built, financed, serviced, or related to a state**, and for how it was **recognised, attributed, or disrupted** — never for how the attack was carried out. The reader finishes able to *reason about* these operations as an intelligence analyst; they finish with nothing they could *reproduce*.

Everything here is built from the public record: indictments and criminal complaints, sanctions designations, court records, agency and government attribution statements, co-sealed advisories, UN reporting, blockchain-analysis publications, security-vendor threat reporting, and reputable journalism and scholarship — Kim Zetter's *Countdown to Zero Day*, David Sanger's Stuxnet reporting, and Andy Greenberg's *Sandworm* among them. Where the record is thin or recent — most of all for the 2025–26 TeamPCP case — this module under-claims and flags the gap rather than filling it.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [CCI-01 — The Cybercriminal Enterprise](cci-01-the-cybercriminal-enterprise.md) | **Lens applied (organisation).** Every case here is read partly as an organisational problem — division of labour, roles, and the enforcement paradox CCI-01 built. CCI-05 applies that lens; it does not re-teach it. |
| [CCI-02 — The Criminal Economy](cci-02-the-criminal-economy.md) | **Lens applied (money).** The Colonial Pipeline seizure and the Bangladesh Bank laundering chain are worked through CCI-02's revenue-and-cash-out analysis; CCI-05 cross-refers rather than repeating it. |
| [CCI-03 — The Service Economy](cci-03-the-service-economy.md) | **Lens applied (services).** DarkSide's affiliate model, the leaked-exploit lifecycle (EternalBlue), and TeamPCP's poisoned-package pipeline are read as service-economy and supply-chain events using CCI-03's frame. |
| [CCI-04 — State-Sponsored Operations & the State–Crime Nexus](cci-04-state-sponsored-operations.md) | **Lens applied (state + attribution).** The state-linked cases inherit CCI-04's same-standard, confidence-graded attribution discipline and its tasked/sponsored/tolerated/overlapping taxonomy. |
| [CT02 — Threat Actor Research & Profiling](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md) | **Method source.** The attribution discipline (confidence levels, source labelling) applied to every case here comes from CT02 Topic 4. |
| [CT04 — Strategic Intelligence](../../../degrees/operational/cti/CT04-strategic-intelligence.md) | **Method source.** The strategic reading of state effects operations (restraint, escalation, collateral cost) draws on CT04. |
| [F04 — Security Concepts](../../../core/units/F04-security-concepts.md) | Provides the vocabulary (ransomware, supply-chain compromise, nation-state actor) these cases make concrete. |
| CCI-06 — Counter-Intelligence Practice & the Dual-Use Economy (later in this series) | Treats the CI discipline in full and resolves the lawful/criminal boundary — including the offensive-security industry and the vulnerability market the EternalBlue and TeamPCP cases touch. Not yet present; named here without linking. |

---

## Prerequisites

- **[CCI-01](cci-01-the-cybercriminal-enterprise.md)**, **[CCI-02](cci-02-the-criminal-economy.md)**, **[CCI-03](cci-03-the-service-economy.md)** and **[CCI-04](cci-04-state-sponsored-operations.md)** (strongly recommended: this module *applies* the four lenses those modules build and assumes them rather than re-teaching them)
- **[CT02 — Threat Actor Research & Profiling](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md)** and **[CT04 — Strategic Intelligence](../../../degrees/operational/cti/CT04-strategic-intelligence.md)** (recommended: the attribution and strategic-analysis method used on every case)
- **[F04 — Security Concepts](../../../core/units/F04-security-concepts.md)** and **[OC05 — Threat Intelligence Fundamentals](../../../core/units/OC05-threat-intelligence-fundamentals.md)** (recommended: the underlying vocabulary and intelligence-cycle grounding)

No tooling is required, and none may be built. Every source used in this module and its exercises is a public web page: an indictment or criminal complaint, a sanctions designation, a court record, a government or agency attribution statement, a co-sealed advisory, a UN report, a blockchain-analysis publication, a security-vendor threat report, or reputable journalism and scholarship. **Learners are directed to no classified, criminal, or operational material, and none is needed for any task here.**

---

## Learning outcomes

On completion, a learner can:

1. **Analyse** a publicly documented operation through several of the series' lenses at once — organisation, money, service, state, and attribution — and state which parts of the public record support which reading.
2. **Distinguish**, across a set of cases, a purely criminal enterprise from a state-attributed programme and from the blurred cases in between, placing each on the [CCI-04](cci-04-state-sponsored-operations.md) tasked / sponsored / tolerated / overlapping spectrum with a confidence level and a source.
3. **Evaluate** the attribution of a case by claim-type — (a) official attribution, (b) journalism/leak, (c) analytic inference — using the confidence language the sources themselves use, and refusing to upgrade a reported or inferred claim into a fact (the Stuxnet case is the worked example).
4. **Analyse** the economics of a case — affiliate splits, laundering paths, low-friction monetisation, or the collateral cost of an uncontrolled effect — using [CCI-02](cci-02-the-criminal-economy.md) and [CCI-03](cci-03-the-service-economy.md), from public figures only, marking every unverified number as such.
5. **Evaluate** how a case was *recognised, attributed, or disrupted* — an on-chain seizure, a co-sealed advisory, a lawful infiltration by a security firm, or an arrest — and what that teaches about where an adversary economy is penetrable.
6. **Synthesise** a lens-based case teardown or a two-case comparison from public sources, with every claim traceable to a labelled source and honestly graded, and with the "no reusable technique" boundary held throughout.
7. **Apply** the correct Australian framing — the Medibank/Ermakov autonomous cyber-sanction, the TeamPCP Perth arrests, and Australian critical-infrastructure and law-enforcement roles (ASD/ACSC, AFP, AUSTRAC) — to a documented case, stating precisely what the record supports and what it does not.

> Bloom's 4–5 (Analyse / Evaluate) is the module's centre of gravity, reaching 6 (Create / Synthesise) where the exercises have the learner *construct* a case teardown and a comparison. This alignment statement is notional: CCI-05 is not credit-bearing and has not been through the AQF mapping process in [`docs/compliance/aqf-teqsa.md`](../../compliance/aqf-teqsa.md).

---

## Framework orientation

!!! note "Mappings are deferred to the Framework Custodian — no codes are asserted here"
    Consistent with the [series index](index.md), this extension module does not feed [ksat-coverage](../../ksat-coverage.md), and its framework mapping is **provisional pending Framework Custodian review**. To avoid asserting an identifier this author has not verified against a current release, the roles and skills below are named at the level this module confidently supports; the specific work-role codes, task IDs, SFIA skill codes and levels, and project-local KSAT IDs are **left to be assigned and verified**, not printed as fact. See the verification-status table.

    - **NIST Workforce Framework for Cybersecurity (NICE) — role families this module speaks to:** All-Source Analyst; Threat/Warning Analyst; Cyber Intelligence Planner; and the financial-crime and law-enforcement-analysis role sets. (Work-role and task codes: **to be assigned by the Framework Custodian.**)
    - **SFIA — skill families:** Threat intelligence; Information security; and, for the case-teardown work, the specialist-advice family as the Custodian judges appropriate. (Skill codes and proficiency levels: **to be assigned.**)
    - **ASD Cyber Skills Framework:** the Cyber Intelligence domain. (Sub-domain and proficiency: **to be assigned.**)
    - **MITRE ATT&CK:** ATT&CK describes *technical behaviours*, which this module deliberately does **not** reproduce. Where a tactic or technique **name** appears — for example the tactic name *Impact* for a destructive effects operation, or *supply-chain compromise* as a delivery pattern named only for recognition — it is in prose only, with no procedural content. Specific technique IDs and the framework version are a CT-series concern, flagged provisional in this project and not asserted here. **No framework code (NICE/DCWF/SFIA/ATT&CK) or KSAT ID is fabricated in this module.**

---

## Module structure

| Part | Topics | Exercises | Notional hours |
|---|---|---|---|
| A — Reading a whole case through the lenses (state effects; RaaS economics) | 1–2 | — | 3 |
| B — Money, state, and the leaked-exploit economy | 3–5 | Exercise 1 | 5 |
| C — Where the digital and physical meet; the current Australian case | 6–7 | Exercise 2 | 4 |
| D — Low-friction monetisation; consolidation | 8 | — | 2 |
| | | | **14 hours** |

---

## Topics

Each topic is **one case**, analysed through the series lenses — organisation, money, service, state, attribution — and read for what it teaches about the adversary economy, **never for how the attack was performed**. Each closes by naming which lens or lenses it most exercises and which module built that lens.

### Topic 1: Operation Olympic Games / Stuxnet — a State Sabotage Programme

The malware publicly known as **Stuxnet**, directed at Iran's uranium-enrichment programme and discovered in **2010**, is the archetype of a state operation that produced a **physical effect**. This module reads it not for its code — none of which appears here — but as a **programme**: how a state organises, tasks, and *restrains* a sabotage capability.

**State + attribution lens ([CCI-04](cci-04-state-sponsored-operations.md)).** Stuxnet is the series' central lesson in **claim-type (b)** attribution. David Sanger's June 2012 *New York Times* reporting (and his book that year), together with Kim Zetter's *Countdown to Zero Day* (2014), described a joint **US–Israeli** programme reportedly codenamed **"Olympic Games,"** begun under President Bush and expanded under President Obama, on the basis of interviews with current and former officials. **Neither the United States nor Israel has officially confirmed responsibility.** The disciplined register is therefore exact: Stuxnet is *reported by investigative journalists, on the basis of anonymous officials, to have been a US–Israeli operation; it has not been officially acknowledged.* An analyst who writes "the US and Israel built Stuxnet" as a bare fact has made precisely the error this module exists to prevent.

**Organisation lens ([CCI-01](cci-01-the-cybercriminal-enterprise.md)).** What the case *teaches* is what a state sabotage programme looks like from the outside: patient, narrowly targeted at one specific industrial process, evidently resourced far beyond a criminal crew, and — most tellingly — **restrained in scope** relative to what a purely destructive actor would have done. Target selection that serves no commercial purpose is the signature of tasking rather than profit ([CCI-04](cci-04-state-sponsored-operations.md) Topic 1). The strategic questions ([CT04](../../../degrees/operational/cti/CT04-strategic-intelligence.md)) are about **containment and escalation**: was the effect calibrated to stay below a threshold of response, and what precedent did a state-attributed physical-effect operation set?

**Lens exercised:** state nexus and attribution-confidence (CCI-04), with the organisation/strategic reading of a tasked programme.

---

### Topic 2: Colonial Pipeline / DarkSide (2021) — Affiliate Economics and an On-Chain Clawback

In May 2021 a ransomware incident attributed to the **DarkSide** operation disrupted a major US fuel pipeline. This module reads it for two things it teaches cleanly: the **service-economy structure** behind it and the **money trail** that let some funds be recovered — not the intrusion, which is not described here.

**Service lens ([CCI-03](cci-03-the-service-economy.md)).** DarkSide operated a **ransomware-as-a-service (RaaS)** model: a core team supplied the malware and infrastructure as a *product*, and independent **affiliates** conducted intrusions in exchange for a share of proceeds. This is the affiliate-program form [CCI-01](cci-01-the-cybercriminal-enterprise.md) and [CCI-03](cci-03-the-service-economy.md) describe, and it matters analytically because it **distributes the work and the risk**: the people who ran the intrusion are not the people who wrote the malware, which complicates both attribution and disruption.

**Money lens ([CCI-02](cci-02-the-criminal-economy.md)).** The case is a landmark because of the **clawback**. On **7 June 2021** the US Department of Justice announced it had seized **63.7 of the roughly 75 bitcoin** paid as ransom — worth about **US$2.3 million** at the time — by tracing the funds on the public blockchain and obtaining access to a wallet. Reporting noted the seized portion corresponded to the **affiliate's** share, with a separate portion having gone to the operation's developers — a direct illustration of the RaaS split, made visible *because* the ledger is public. This is [CCI-02](cci-02-the-criminal-economy.md)'s central lesson concretised: the transparency that makes cryptocurrency useful to criminals is also the lever that lets investigators follow and sometimes recover funds.

**Lens exercised:** service economy (CCI-03) and money/cash-out and seizure (CCI-02), with the affiliate-organisation reading (CCI-01).

---

### Topic 3: Bangladesh Bank Heist (2016) — A State-Attributed Digital Bank Heist

In **February 2016**, fraudulent payment instructions issued over the **SWIFT** interbank messaging network attempted to move close to **US$1 billion** out of Bangladesh Bank's account at the Federal Reserve Bank of New York. Most were blocked; about **US$81 million** went through. This module reads the case for its **money** and **state** lessons, at the level of organisation only — not the intrusion, and not the messaging abuse as a method.

**Money lens ([CCI-02](cci-02-the-criminal-economy.md)).** The stolen funds were routed to accounts in the **Philippines** and laundered onward, with reporting describing a **casino** cash-out that broke the money's traceability at a point where anti-money-laundering coverage was weak. A separate leg directed roughly **US$20 million** to a **Sri Lankan** recipient was stopped and largely recovered — famously because a **misspelling** in a beneficiary name (a charitable "foundation") triggered scrutiny. The lesson is [CCI-02](cci-02-the-criminal-economy.md)'s: moving the money is harder than taking it, cash-out points cluster where regulation is thin, and a single clerical error can collapse a laundering leg.

**State lens ([CCI-04](cci-04-state-sponsored-operations.md)).** US charging documents attribute the activity to the DPRK's **Reconnaissance General Bureau** — the **DOJ criminal complaint unsealed on 6 September 2018** named **Park Jin Hyok** in connection with the Bangladesh Bank theft (alongside the 2014 Sony attack and 2017 WannaCry), and the **17 February 2021** indictment added further defendants and alleged a conspiracy to steal and extort **more than US$1.3 billion**. This is the [CCI-04](cci-04-state-sponsored-operations.md) **"state as criminal"** pattern — theft as state revenue policy under sanctions. The complaint and indictment are **allegations**; the RGB placement is the **DOJ's finding**; the analyst keeps that wording and cites **UN/MSMT** reporting rather than the indictment for quantified totals.

**Lens exercised:** money/laundering (CCI-02) and state-as-criminal revenue nexus (CCI-04).

---

### Topic 4: NotPetya (2017) — State-Attributed Destructive Spillover

In **June 2017** the destructive malware known as **NotPetya**, delivered through a compromised Ukrainian software supply chain, spread globally and caused losses **widely reported at around US$10 billion** — striking shipping, logistics, pharmaceutical and other multinationals far from its apparent Ukrainian target. This module reads it as an **effects operation** and a **collateral-cost** lesson, with no technical detail.

**State + attribution lens ([CCI-04](cci-04-state-sponsored-operations.md)).** NotPetya is a **claim-type (a)** case: the United States, the United Kingdom, **Australia** (16 February 2018) and other governments **officially attributed** it to the Russian state, and the **US DOJ indictment unsealed on 19 October 2020** (Western District of Pennsylvania) charged **six officers of GRU Unit 74455 — "Sandworm"** — in connection with NotPetya and a series of other operations (Ukrainian power-grid attacks; the 2018 PyeongChang "Olympic Destroyer"; targeting of the 2017 French election). Andy Greenberg's *Sandworm* (2019) is the book-length account. The indictment is an **allegation**; the attributions are government **findings**; the module keeps that exact.

**Organisation / strategic lens ([CCI-01](cci-01-the-cybercriminal-enterprise.md) / [CT04](../../../degrees/operational/cti/CT04-strategic-intelligence.md)).** The teaching point is the **contrast with Stuxnet's restraint**. Where Stuxnet was narrowly contained, NotPetya was **uncontrolled** — it spread far beyond any plausible intended target and inflicted enormous collateral damage on private companies with no connection to the conflict. Read at the level of state behaviour, NotPetya is the case study in an effects operation whose spillover crossed thresholds and drew a coordinated multi-government attribution response. *Supply-chain compromise* is named here only as the recognised delivery pattern — for recognition, not reproduction.

**Lens exercised:** state nexus and attribution (CCI-04), with the strategic restraint/escalation reading (CT04).

---

### Topic 5: EternalBlue — The Lifecycle of a Leaked Exploit

**EternalBlue** is not an operation but an **exploit** — and its story is a supply-and-lifecycle lesson about the **vulnerability-and-exploit economy**, told entirely at the level of *who held it and how it moved*, with no exploit detail whatsoever.

**Service / economy lens ([CCI-03](cci-03-the-service-economy.md)).** The public record describes EternalBlue as an exploit **developed by a state agency (the NSA)** for a Windows networking vulnerability, which entered the wild when a group calling itself the **Shadow Brokers** published a cache of tools (the "Lost in Translation" dump) on **14 April 2017**. Microsoft had issued a patch (**MS17-010**) about a month earlier, on **14 March 2017**. Within weeks the exploit was **reused** by others: the **WannaCry** ransomware outbreak (12 May 2017) and, that June, **NotPetya** (Topic 4) both incorporated it. Read through [CCI-03](cci-03-the-service-economy.md), EternalBlue is the clearest documented illustration that an exploit is a **transferable asset** in an economy — it can be developed by one actor, leaked, and then picked up by criminal *and* state actors alike, and the window between a patch and mass exploitation is governed by **patching lag**, not by the leak alone.

**Attribution lens ([CCI-04](cci-04-state-sponsored-operations.md)).** The Shadow Brokers material is a **leak** (claim-type (b)): its provenance and the identity behind the persona remain matters of reporting and analysis, not official confirmation, and the module labels it as such rather than treating the leak as settled fact.

**Lens exercised:** service/economy and the exploit lifecycle (CCI-03), with an attribution caveat on the leak (CCI-04).

---

### Topic 6: Cyber-Enabled Organised & Physical Crime — Port-Logistics Compromise

Not every adversary economy is purely digital. A documented class of case fuses **digital intrusion, insider access, and physical operations**, and the clearest example is the compromise of **port-logistics systems** to facilitate drug smuggling — the Antwerp/Rotterdam container cases, as documented by European law enforcement and reporting.

**Organisation lens ([CCI-01](cci-01-the-cybercriminal-enterprise.md)).** Over roughly **2011–2013**, a Netherlands-based trafficking group is documented to have engaged people with technical skills to interfere with the container-tracking systems of terminals in the **Port of Antwerp**, so that drug-laden containers could be located and collected before legitimate handlers reached them; large seizures of cocaine and heroin and multiple arrests in the Netherlands and Belgium followed. Read through [CCI-01](cci-01-the-cybercriminal-enterprise.md), the lesson is organisational: this is a **traditional organised-crime group buying a digital capability** as one input among many (drivers, insiders, logistics), exactly the division-of-labour and outsourcing pattern the enterprise lens predicts. It also shows the **convergence** of cyber and physical crime — the digital intrusion had value only because it was wired into a physical smuggling operation.

**Service lens ([CCI-03](cci-03-the-service-economy.md)).** The case previews [CCI-03](cci-03-the-service-economy.md)'s core claim from the *demand* side: the traffickers did not need to *be* hackers; they needed to *hire* the capability, which is what a criminal service economy supplies.

**Lens exercised:** organisation and cyber–physical convergence (CCI-01), with a service-economy demand-side reading (CCI-03). *(Case details verified against reputable reporting; specific figures vary between accounts and are treated as approximate — see verification status.)*

---

### Topic 7: TeamPCP (2025–26) — A Supply-Chain Extortion Group and a Lawful Disruption

**Handle the specifics of this case with the most caution in the module.** It is recent (2025–26), the public record is still forming, and the two people arrested are **accused / alleged** and entitled to the presumption of innocence. This module describes the case at **group level**, attributes each detail to reporting, and asserts **no guilt** against any individual.

**Organisation + service lens ([CCI-01](cci-01-the-cybercriminal-enterprise.md) / [CCI-03](cci-03-the-service-economy.md)).** **TeamPCP** (tracked by Google's security researchers as **UNC6780**) is reported as a supply-chain extortion group associated with a self-propagating worm publicly named **"Shai-Hulud"** (and a later variant reported as "Mini Shai-Hulud"). The reported pattern — poisoning widely used open-source software packages so that the compromise spreads downstream — is named here **only for recognition**, as a *supply-chain* organisational model, with **no technical detail**. Read through [CCI-01](cci-01-the-cybercriminal-enterprise.md)/[CCI-03](cci-03-the-service-economy.md), the teaching point is that the **open-source dependency chain itself becomes the distribution network** — an organisational and economic insight about leverage, not a method. Reporting describes **1,000+ organisations** affected across the campaign; specific victim and volume figures vary between accounts and are treated as provisional.

**Attribution / disruption lens ([CCI-04](cci-04-state-sponsored-operations.md)) — the lawful actor.** **Google Threat Intelligence Group (GTIG) / Mandiant is the lawful disruptor and infiltrator in this case and is never implied criminal.** Public reporting, drawing on GTIG/Mandiant's own account, describes a Mandiant analyst having **infiltrated the group undercover**, gained visibility into its operations, and worked with affected platform providers to **revoke stolen credentials**. The Perth arrests followed the broader disruption of the group; this module does not assert a direct chain from the firm's disclosure to that law-enforcement action, only that the two are close in time on the public record. This is a textbook lawful-disruption story — a security firm penetrating a criminal group and its findings feeding a wider response — and it is the [CCI-04](cci-04-state-sponsored-operations.md)/CCI-06 lesson on where a criminal economy is penetrable.

**Australian law-enforcement lens (R4).** Reputable reporting (for example CyberScoop, The Register, The Hacker News) states that in **August 2026** the **Australian Federal Police** and **Western Australia Police Force**, with **FBI** involvement, arrested **two men (reported as aged 21 and 23)** in **Perth**, who were **charged** with a combined total of around **14 offences** including unauthorised data modification and dealing in criminal proceeds. **These are charges, not convictions; the accused are alleged and presumed innocent.** This module does not centre the individuals' names; where any specific arrest detail could not be pinned to reputable reporting, it is flagged provisional. The case is a live Australian counter-intelligence and law-enforcement study of exactly the kind [CCI-01](cci-01-the-cybercriminal-enterprise.md) frames — an adversary economy disrupted through infiltration and arrest.

**Lens exercised:** organisation and supply-chain service model (CCI-01/CCI-03), plus lawful disruption/attribution and the Australian arrest (CCI-04); **most-provisional case in the module.**

---

### Topic 8: Cryptojacking — Low-Friction Monetisation

A short closing case rounds out the **economics** picture. **Cryptojacking** — the unauthorised use of others' computing resources to mine cryptocurrency — is the low-friction, low-visibility end of the adversary economy, and it teaches a [CCI-02](cci-02-the-criminal-economy.md) point by contrast with the headline cases.

**Money / economy lens ([CCI-02](cci-02-the-criminal-economy.md)).** Where ransomware is high-friction (it must be noticed, negotiated, and paid) and a bank heist is high-stakes, cryptojacking is the opposite: it aims to stay **unnoticed**, monetising stolen compute quietly and continuously. The lesson is that the adversary economy spans a **spectrum of monetisation strategies** trading visibility against yield — and that the quiet, low-yield end is precisely the part a defender is least likely to detect. It is analysed here purely as an **economic model**, not as a method; no mining or intrusion technique appears.

**Lens exercised:** money/economy (CCI-02) — the low-friction monetisation contrast.

---

## Exercises

Both exercises are **intelligence-analysis tasks over public reporting**. There is no lab, no tooling, and nothing operational. Each is completable from freely available web sources — indictments, sanctions designations, court records, government and agency attributions, co-sealed advisories, UN/MSMT reports, blockchain-analysis publications, security-vendor threat reporting, and reputable journalism and scholarship — and the further-reading list is a starting point, not a limit.

!!! warning "Sourcing, neutrality and the no-technique boundary"
    Use only lawful, public sources. Do **not** attempt to access any classified, criminal, or operational material — it is unnecessary, may be unlawful, and is outside this module's authorisation. Analyse each case for **organisation, economics, service structure, and state relationship, and for how it was recognised, attributed, or disrupted — never for how the attack was done.** If a sentence you are about to write would help someone reproduce an attack, cut it. Apply the **same evidence standard to every actor**, attribute every claim to its source with a confidence level, treat every named individual as **alleged / accused / attributed** and cite the record that names them, and never present a lawful security firm, researcher, or victim as a wrongdoer. Where the record attributes only through journalism, a leak, or inference, your assessment must say so.

### Exercise 1 (Analytical): A Lens-Based Case Teardown

**Objective:** Produce a defensible, confidence-graded teardown of **one** publicly documented operation, reading it through several of the series' lenses at once and holding the no-technique boundary throughout.

**Prerequisites:** Topics 1–5.

**Task:**

1. Choose **one** case with a substantial public record — for example **Colonial Pipeline / DarkSide** (service + money), the **Bangladesh Bank heist** (money + state), **NotPetya** (state + strategic), or **Stuxnet / Olympic Games** (state + attribution). Avoid the TeamPCP case for this exercise unless your instructor confirms the record is stable enough.
2. Assemble a **labelled source inventory** of at least five items, each tagged by claim-type: (a) official attribution — indictment, complaint, designation, or co-sealed advisory; (b) journalism/leak; (c) analytic inference/research.
3. Write the **lens teardown**: for each relevant lens — organisation ([CCI-01](cci-01-the-cybercriminal-enterprise.md)), money ([CCI-02](cci-02-the-criminal-economy.md)), service ([CCI-03](cci-03-the-service-economy.md)), state/nexus and attribution ([CCI-04](cci-04-state-sponsored-operations.md)) — state what the public record shows and at what confidence, using the sources' own language ("indicted," "assessed with high confidence," "reported on the basis of anonymous officials," "not officially confirmed").
4. Write a **recognition-and-disruption note**: how was this case recognised, attributed, or disrupted (an on-chain seizure, a co-sealed advisory, a lawful infiltration, an arrest), and what does that teach about where the economy was penetrable?
5. Write a half-page **boundary-and-gaps note**: confirm you have described *what the case teaches*, not *how it was done*; identify what the record does **not** establish; and state what would raise or lower your confidence.

**Expected output:** the labelled source inventory; the multi-lens teardown; the recognition-and-disruption note; the boundary-and-gaps note. Marked on **discipline** — every claim traceable to a labelled source and honestly graded, no allegation laundered into a fact, no leak upgraded to official confirmation, and the no-technique boundary demonstrably held.

**Reflection:**

1. Which lens did the public record support *most* strongly for your case, and which did you have to leave at low confidence?
2. Where did you most have to resist upgrading a claim-type-(b) or (c) statement into a fact, and how did you word it to avoid that?
3. Was there a sentence you *wanted* to write that you cut because it crossed into technique? What did cutting it cost the analysis, and was the analysis still complete without it?

### Exercise 2 (Analytical): Compare Two Cases on a Chosen Dimension

**Objective:** Compare **two** cases on a single analytic dimension, treating criminal and state-attributed actors by the **same evidence standard**, and characterise the state–crime relationship (if any) in each.

**Prerequisites:** Topics 2–7.

**Task:**

1. Choose a **dimension** and **two** cases that contrast on it. Examples: *money movement and recovery* (Colonial Pipeline's on-chain seizure vs the Bangladesh Bank casino cash-out); *restraint and collateral cost* (Stuxnet's containment vs NotPetya's spillover); *organisational model* (a RaaS affiliate program vs a supply-chain extortion crew); or *how each was disrupted* (an on-chain clawback vs a lawful infiltration and arrest).
2. For each case, describe the chosen dimension **from public sources only**, labelling every figure and attribution by claim-type and confidence, and marking anything unverified as provisional.
3. Using the [CCI-04](cci-04-state-sponsored-operations.md) taxonomy, characterise the **state–crime relationship** in each case — *tasked / sponsored / tolerated / overlapping / none evident* — with a confidence level and a source for each characterisation.
4. Produce a **comparison table**: the dimension, the organisational/economic reading, the state relationship, and how each case was recognised or disrupted, side by side, with a confidence level in every cell and a note where the record is silent.
5. Write a half-page **evidence-asymmetry note**: state explicitly where your evidence base differed between the two cases (an older, litigated case usually has a richer record than a current one; a state-linked case is known largely through attribution) and how you stopped that asymmetry from becoming a double standard or a verdict.

**Expected output:** the two dimension descriptions; the state–crime characterisations with confidence; the comparison table; the evidence-asymmetry note. Marked on **even-handedness and honest uncertainty** — the same evidentiary standard applied to both cases, every claim sourced and graded, the asymmetry named rather than smuggled in, and no technique reproduced.

**Reflection:**

1. Did the two cases' evidence bases differ enough that a naïve reader might mistake "better documented" for "worse conduct"? How did you guard against that?
2. Which state–crime characterisation was hardest to grade, and what single public document would most change it?
3. If your two cases included the TeamPCP matter, how did you keep the accused individuals *alleged* and describe the case at group level without weakening the analysis?

---

## Australian context

This module carries the series' Australian anchor (R4) through cases with a direct Australian angle and through the Australian agencies that recognise, attribute, and disrupt this activity.

**The TeamPCP Perth arrests (2025–26).** The clearest current Australian case is **TeamPCP** (Topic 7). Reputable reporting states that in **August 2026** the **Australian Federal Police** and the **Western Australia Police Force**, with **FBI** involvement, arrested and charged **two men in Perth** in connection with the group. The case is significant for Australia because it shows an Australian law-enforcement outcome against a **globally significant supply-chain extortion group**, following a lawful disruption by a security firm (GTIG/Mandiant). Consistent with the ground rules, the accused are **alleged and presumed innocent**, this module asserts no guilt, and any specific arrest detail not confirmed against reputable reporting is flagged provisional. **This is the most provisional item in the module and must be re-verified at delivery.**

**The Medibank / Ermakov autonomous cyber-sanction.** The Australian nexus case from [CCI-04](cci-04-state-sponsored-operations.md) applies here too: on **23 January 2024**, Australia used its autonomous **cyber**-sanctions power for the **first time**, listing Russian national **Aleksandr Ermakov** — alleged to be connected to the REvil group — over the **2022 Medibank Private** breach (personal information of about **9.7 million** people), in coordination with the US and UK. The listing is an executive **finding**, the named person **alleged**, and, because sanction status changes, it is flagged for re-verification.

**Australian critical-infrastructure exposure.** The state-linked and destructive cases (NotPetya, Bangladesh Bank) and the supply-chain case (TeamPCP) all bear on Australian **critical-infrastructure** risk: an Australian operator may face a state, a state-tolerated criminal, or a supply-chain compromise reaching it through a third party. The **Security of Critical Infrastructure Act 2018 (SOCI)** regime, with its risk-management and incident-reporting obligations, is the national response to exactly that ambiguity.

**The agencies.** **ASD/ACSC** produces Australian attribution and advisory material and co-signs international advisories; the **AFP** (with state police and international partners) conducts law-enforcement action, as in the TeamPCP arrests; **AUSTRAC** is the financial-intelligence agency relevant to the money-laundering lens ([CCI-02](cci-02-the-criminal-economy.md)); and **DFAT** administers the sanctions lists. Legal authority for teaching from this material rests on it already being public; this module directs no one to any classified, criminal, or operational material.

---

## Verification status

This module has **not** had practitioner review (R2). It must not be presented to learners as verified content until a Domain Expert and Practitioner Reviewer have signed off. Because this is the case-study module, the highest-risk items are the **currency of every named individual's public-action status**, **not overstating attribution confidence** (Stuxnet above all), the **still-forming TeamPCP record**, and the **"no reusable technique" boundary** — every case must read as analysis of organisation/economics/state-relationship, never as a method. Every attribution, date, and figure below was checked against a primary or authoritative source during authoring, but each must be re-verified at delivery.

| Item | Status | Action required |
|---|---|---|
| **"No reusable technique" boundary held for every case** — each analysed for organisation/economics/service/state and for recognition/attribution/disruption, never for how the attack was done | **Blocking** | Requires the reviewer's explicit sign-off that no case contains exploit detail or a reproducible how-to |
| **TeamPCP specifics (2025–26)** — Perth arrests (August 2026; AFP + WA Police + FBI; two accused reported aged 21 and 23; ~14 combined charges); UNC6780 tracking; Shai-Hulud / "Mini Shai-Hulud" naming; 1,000+ organisations | **Most provisional in the module — verify at delivery** | Re-confirm against reputable reporting; keep accused **alleged / presumed innocent**; describe at group level; do not assert guilt; treat victim/volume figures as approximate |
| **GTIG / Mandiant as lawful disruptor** in the TeamPCP case (undercover infiltration; credential revocation; tip to law enforcement) | **Verified against GTIG/Mandiant reporting as reported** | Confirm; keep the firm framed strictly as the **lawful** infiltrator/disruptor, never implied criminal |
| **Stuxnet / Olympic Games attribution** — US/Israel per Sanger (NYT, June 2012) and Zetter (*Countdown to Zero Day*, 2014); **not officially confirmed** by either government | **Verified as reported; claim-type (b)** | Preserve the "reported by journalists, not officially confirmed" framing verbatim; do not state as official attribution |
| **Colonial Pipeline / DarkSide seizure** — 63.7 of ~75 BTC (~US$2.3m) seized; DOJ announcement 7 June 2021; RaaS affiliate/developer split | **Verified against DOJ / reputable reporting as reported** | Confirm the figures and date against the DOJ release; keep the affiliate-split reading sourced |
| **Bangladesh Bank heist (Feb 2016)** — ~US$81m moved (of ~US$951m attempted); Philippines/casino cash-out; ~US$20m Sri Lanka leg stopped on a misspelling; DPRK/RGB per DOJ (Park Jin Hyok complaint unsealed 6 Sep 2018; 17 Feb 2021 indictment, >US$1.3bn alleged) | **Verified against DOJ / reputable reporting as reported** | Confirm figures and dates; keep RGB/DPRK as the DOJ's **finding** and the defendants **alleged**; cite UN/MSMT for totals |
| **NotPetya (June 2017)** — ~US$10bn losses widely reported; official attributions by US/UK/Australia (Australia 16 Feb 2018); DOJ indictment of six GRU Unit 74455 ("Sandworm") officers unsealed 19 Oct 2020 (W.D. Pa.) | **Verified against DOJ / government statements as reported** | Confirm against the DOJ release and the Australian statement; keep indictment = allegation; the ~US$10bn is a widely reported estimate, not a court finding |
| **EternalBlue lifecycle** — NSA-developed per public reporting; Shadow Brokers "Lost in Translation" dump 14 Apr 2017; Microsoft patch MS17-010 ~14 Mar 2017; reused in WannaCry (12 May 2017) and NotPetya | **Verified as reported; leak = claim-type (b)** | Confirm dates; label the Shadow Brokers material as a leak of contested provenance; assert no exploit detail |
| **Port-logistics / Antwerp case (c. 2011–2013)** — trafficking group engaged technical help to interfere with container-tracking; cocaine/heroin seizures; arrests in NL/Belgium | **Verified against reputable reporting as reported; figures approximate** | Confirm the framing; treat quantities/values as approximate (accounts vary); analyse at organisation level only |
| **Medibank / Ermakov autonomous cyber-sanction** (23 Jan 2024; ~9.7m affected; US/UK coordinated; Australia's first use) | **Verified against ASD/DFAT/Minister releases as reported** | Confirm "first use" wording and coordination; sanction status may change |
| **Attribution confidence not overstated** — every claim labelled (a) official / (b) journalism-leak / (c) inference at no higher confidence than the source supports | **Blocking / provisional** | Do not upgrade an allegation, assessment, or leak into a fact or verdict; check each verb against the source |
| **No lawful entity implied criminal** — security firms, researchers, conferences and victims named only as such (GTIG/Mandiant especially) | **Blocking** | Requires the reviewer's sign-off; the dual-use economy is a CCI-06 subject |
| Framework mapping (NICE work-role and task codes; SFIA skill codes and levels; ASD CSF sub-domain; project-local KSAT IDs) | **Deferred — not asserted** | Assign and verify with the Framework Custodian; this module intentionally prints no codes |
| MITRE ATT&CK tactic/technique references (e.g. *Impact*; *supply-chain compromise* as a named delivery pattern) | **Names used for recognition only; IDs not asserted** | Technique IDs and framework version remain a project-wide provisional item in the CT series |

---

## Further reading

Real, citable starting points spanning the cases. All are public; treat government and court pages as primary, agency and UN pages as institutional, and reporting, vendor threat reports and scholarship as reputable secondary. Apply the same standard to every source. Australian sources are marked.

**U.S. Department of Justice (June 2021).** *Department of Justice Seizes $2.3 Million in Cryptocurrency Paid to the Ransomware Extortionists Darkside.* justice.gov.
> Relevance: The primary record for the Colonial Pipeline on-chain seizure (63.7 of ~75 BTC) in Topic 2 and the money lens ([CCI-02](cci-02-the-criminal-economy.md)).

**U.S. Department of Justice (September 2018; February 2021).** The Park Jin Hyok criminal complaint and the later DPRK indictment (Reconnaissance General Bureau; Bangladesh Bank, Sony, WannaCry; >US$1.3bn alleged). justice.gov.
> Relevance: The state-attribution record for the Bangladesh Bank heist in Topic 3 and its cross-reference to [CCI-04](cci-04-state-sponsored-operations.md).

**U.S. Department of Justice (October 2020).** *Six Russian GRU Officers Charged in Connection with Worldwide Deployment of Destructive Malware and Other Disruptive Actions in Cyberspace* (Unit 74455 / "Sandworm"; NotPetya and more). justice.gov.
> Relevance: The primary official-attribution record for NotPetya in Topic 4; a claim-type-(a) source for Exercise 1.

**Kim Zetter (2014).** *Countdown to Zero Day: Stuxnet and the Launch of the World's First Digital Weapon.* Crown; and **David E. Sanger (2012),** *"Obama Order Sped Up Wave of Cyberattacks Against Iran," The New York Times.*
> Relevance: The primary journalistic sources (claim-type (b)) for the Stuxnet / Olympic Games attribution in Topic 1 — reported, not officially confirmed.

**Andy Greenberg (2019).** *Sandworm: A New Era of Cyberwar and the Hunt for the Kremlin's Most Dangerous Hackers.* Doubleday.
> Relevance: The book-length account of Sandworm and NotPetya for Topic 4.

**Europol.** *Internet Organised Crime Threat Assessment (IOCTA)* and reporting on cyber-enabled organised crime and port compromise. europol.europa.eu.
> Relevance: Institutional context for the port-logistics / cyber–physical convergence case in Topic 6.

**Chainalysis.** *Crypto Crime Report* (annual). chainalysis.com.
> Relevance: Blockchain-analysis context for the money lens ([CCI-02](cci-02-the-criminal-economy.md)) across the ransomware and heist cases, and the tracing that enabled the Colonial Pipeline seizure.

**Google Threat Intelligence Group / Mandiant.** Public reporting on UNC6780 / TeamPCP and the Shai-Hulud supply-chain campaign. cloud.google.com/blog/topics/threat-intelligence.
> Relevance: The lawful-disruption account in Topic 7; the firm is the infiltrator/disruptor, never implied criminal. Treat as recent, still-forming reporting.

**Australian Signals Directorate / ACSC.** *Annual Cyber Threat Report* and co-sealed advisories; and **Australian Federal Police** media releases on the TeamPCP arrests. cyber.gov.au; afp.gov.au (**Australian sources**).
> Relevance: The Australian recognition/attribution and law-enforcement material for the Australian-context section; verify the TeamPCP arrest specifics here at delivery.

**Minister for Foreign Affairs / DFAT (January 2024).** Media releases on the Ermakov / Medibank cyber sanction and the consolidated sanctions list. foreignminister.gov.au; dfat.gov.au (**Australian sources**).
> Relevance: Australia's first autonomous cyber-sanction listing and the nexus case; verify status here.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | CCI-05 |
| Module Title | Case Studies in the Adversary Economy |
| Series | EXT-CCI — Adversary Counter-Intelligence |
| Module Type | Extension module (elective; **not** credit-bearing) |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 0 CP — outside the 160 CP degree structure |
| Notional Hours | 14 |
| Applies (lenses) | CCI-01 (organisation), CCI-02 (money/laundering), CCI-03 (service economy), CCI-04 (state nexus / attribution-confidence) |
| Related Units | F04, OC05, CT01, CT02, CT04 |
| Prerequisites | CCI-01/02/03/04 strongly recommended; CT02, CT04, F04, OC05 recommended |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-09-22 |
| Framework Mapping | Deferred to Framework Custodian (no codes asserted; see Framework orientation) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate), reaching 6 (Create / Synthesise) in the exercises |
| Australian Context | TeamPCP Perth arrests (Aug 2026; AFP/WA Police/FBI; accused alleged — most provisional item); Medibank/Ermakov autonomous cyber-sanction (23 Jan 2024, Australia's first); Australian critical-infrastructure exposure and SOCI; ASD/ACSC, AFP, AUSTRAC, DFAT roles |
| Tooling Licence Position | No tooling required; both exercises are analysis over public sources (R3) |
| Risk Note | Case-study module — highest risks are the currency of every named individual's public-action status, not overstating attribution confidence (Stuxnet), the still-forming TeamPCP record (accused = alleged), and the "no reusable technique" boundary; the boundary, the no-lawful-entity-implied-criminal, and the attribution-confidence rows are blocking review items |
| Licence | CC BY 4.0 |
