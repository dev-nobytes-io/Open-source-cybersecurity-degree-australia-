# CCI-04: State-Sponsored Operations & the State–Crime Nexus

> **Module type:** Extension module (counter-intelligence deep dive) — part of [EXT-CCI](index.md)
> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-09-22
> **Domain Expert:** _Unassigned — required before Practitioner Approved (strategic-CTI, national-security-cyber, or law-enforcement cyber background)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must have worked adversary attribution, strategic intelligence, or a government cyber programme)_

!!! warning "Not a credit-bearing unit"
    CCI-04 is the fourth module of the [EXT-CCI series](index.md), an optional extension that sits outside the 66-unit / 160 CP degree structure. It carries **0 CP** and does not appear in [`docs/ksat-coverage.md`](../../ksat-coverage.md) or the [Program Builder](../../program-builder/index.md), both of which are generated from credit-bearing units only. A delivery partner wanting to recognise it should use the Tier 1 badge mechanism in [`docs/curriculum/micro-credentials-framework.md`](../../curriculum/micro-credentials-framework.md).

!!! danger "Read the series ground rules first — and note that this is the politically sensitive module"
    This module is bound by the [series index](index.md) danger box and by [CCI-01](cci-01-the-cybercriminal-enterprise.md), [CCI-02](cci-02-the-criminal-economy.md) and [CCI-03](cci-03-the-service-economy.md). In one line each: it is **analysis of publicly documented adversaries and programmes, not a manual**; it contains **no operational tradecraft** — no exploit detail and no how-to, only organisation, tasking, economics and attribution at the level an analyst needs to *recognise and reason about* a programme; **legitimate security businesses, researchers and conferences are never presented as criminals** (they belong to the lawful dual-use economy studied in CCI-06, not here); and **named individuals appear only where a government has publicly charged, sanctioned, or formally attributed them**, described as *alleged* / *attributed* — an indictment or a sanction is an allegation or an executive finding, not a court's verdict of guilt.

    **This module treats every state — adversary and allied alike — by the same evidence standard.** It covers publicly attributed adversary programmes (for example Russia, the DPRK, Iran and China as officially attributed) *and* allied and Western programmes (for example the US and Israel in the public reporting on Stuxnet; the Five Eyes SIGINT agencies). For each, it states **only what is publicly documented or officially attributed**, attributes every claim to its source **with a confidence level and caveats**, and does **not editorialise, moralise, or take a side.** It distinguishes throughout between (a) official government attribution, (b) investigative journalism and leaks (e.g. the Snowden and Shadow Brokers material), and (c) analytic inference — and it never asserts that an intelligence agency committed an act that the public record attributes only with low or medium confidence, or only through a leak. "Attributed to" and "has not been officially confirmed" are the register of the whole module.

---

## Overview

[CCI-01](cci-01-the-cybercriminal-enterprise.md) taught the adversary as an **organisation**, [CCI-02](cci-02-the-criminal-economy.md) taught the **money**, and [CCI-03](cci-03-the-service-economy.md) taught the **service industry** those two run on. All three stayed on the criminal side of the spectrum. This module crosses to the other end — the **state** — and to the increasingly blurred border between the two, studied not as geopolitics or advocacy but as an **intelligence and attribution subject**.

The organising idea is that a state cyber programme is a fundamentally different kind of adversary from a criminal enterprise, and that the difference is legible in the public record if you know how to read it. A criminal group is coordinated by money and constrained by the enforcement paradox of [CCI-01](cci-01-the-cybercriminal-enterprise.md); a state programme is coordinated by **tasking** and constrained by **policy, deniability, and the risk of escalation.** Those different constraints produce different behaviour — different target selection, different restraint, different tolerance for being caught — and therefore call for a different analytic frame. This module builds that frame, and then applies it evenly to whichever state the public record documents.

The second idea is that the neat line between "state" and "criminal" is, in several documented cases, not there at all. A state may **run** an operation directly, **sponsor or task** a proxy, **tolerate** a criminal crew that stays within unwritten limits, or simply **share people** with the criminal economy through moonlighting. The DPRK's revenue-generating theft, Russia's tolerance of ransomware crews, and "patriotic hacker" proxies are the documented illustrations of that nexus, and reasoning about which of those relationships a given case represents — on the available evidence, with an honest confidence level — is exactly the skill this module assesses.

Everything here is built from the public record: government attributions and indictments, sanctions designations, co-sealed intelligence advisories, UN reporting, declassified material, leaked documents (labelled as such), and reputable scholarship — Thomas Rid's *Active Measures*, Kim Zetter's *Countdown to Zero Day*, and David Sanger's reporting on Stuxnet among them. It deliberately does **not** re-teach attribution method from scratch (that is [CT02](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md) Topic 4) or the intelligence cycle ([CT01](../../../degrees/operational/cti/CT01-intelligence-tradecraft.md)); it extends them into the hardest and highest-stakes attribution problem there is — attributing an act to a **state** — where getting the confidence level wrong is not merely an analytic error but, potentially, a diplomatic one.

---

## Where this module fits

| Unit / module | Relationship |
|---|---|
| [CCI-01 — The Cybercriminal Enterprise](cci-01-the-cybercriminal-enterprise.md) | **Predecessor (organisation).** CCI-01 established the criminal enterprise as a firm coordinated by money under the enforcement paradox; CCI-04 contrasts it with the state programme coordinated by tasking under policy and deniability, and shows where the two overlap. |
| [CCI-02 — The Criminal Economy](cci-02-the-criminal-economy.md) | **Predecessor (money).** CCI-02's laundering-and-cash-out analysis is the direct antecedent of this module's DPRK "state-as-criminal" revenue theft; CCI-04 cross-refers rather than re-teaching the money movement. |
| [CCI-03 — The Service Economy](cci-03-the-service-economy.md) | **Predecessor (services).** CCI-03's contractor-and-market view is what a state buys into or tasks; CCI-04 adds the state as customer, sponsor, and tolerator of that market. |
| [CT02 — Threat Actor Research & Profiling](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md) | **Method source.** Topic 4's attribution discipline (confidence levels, source labelling) is the backbone this module extends to state-level attribution — the hardest case. |
| [CT04 — Strategic Intelligence](../../../degrees/operational/cti/CT04-strategic-intelligence.md) | **Direct predecessor (strategic lens).** Strategic-level analysis of state intent and capability; CCI-04 adds the counter-intelligence framing and the state–crime nexus. |
| [F04 — Security Concepts](../../../core/units/F04-security-concepts.md) | Introduces state-sponsored actors and the threat landscape as vocabulary; CCI-04 takes "nation-state actor" from a term to a programme read off the public record. |
| [CT01 — Intelligence Tradecraft](../../../degrees/operational/cti/CT01-intelligence-tradecraft.md) | Provides the collection-and-analysis discipline (sourcing, confidence, bias) this module applies to the state programme. |
| [OC05 — Threat Intelligence Fundamentals](../../../core/units/OC05-threat-intelligence-fundamentals.md) | Operational-core grounding this module assumes. |
| CCI-05 — Case Studies in the Adversary Economy (later in this series) | Works several of this module's cases at length as organisational and economic events. Not yet present; named here without linking. |
| CCI-06 — Counter-Intelligence Practice & the Dual-Use Economy (later in this series) | Treats the CI discipline in full and resolves the lawful/criminal boundary (the offensive-security industry, conferences, and the vulnerability market). Not yet present; named here without linking. |

---

## Prerequisites

- **[CT02 — Threat Actor Research & Profiling](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md)** and **[CT04 — Strategic Intelligence](../../../degrees/operational/cti/CT04-strategic-intelligence.md)** (strongly recommended; this module extends CT02 Topic 4 attribution and CT04's strategic lens to the state actor)
- **[CCI-01](cci-01-the-cybercriminal-enterprise.md)**, **[CCI-02](cci-02-the-criminal-economy.md)** and **[CCI-03](cci-03-the-service-economy.md)** (recommended: the criminal-side baseline this module contrasts and connects to)
- **[F04 — Security Concepts](../../../core/units/F04-security-concepts.md)**, **[OC05 — Threat Intelligence Fundamentals](../../../core/units/OC05-threat-intelligence-fundamentals.md)** and **[CT01 — Intelligence Tradecraft](../../../degrees/operational/cti/CT01-intelligence-tradecraft.md)** (recommended: the vocabulary, the intelligence cycle, and source-and-confidence discipline used in both exercises)

No tooling is required, and none may be built. Every source used in this module and its exercises is a public web page: a government attribution statement, an indictment, a sanctions designation, a co-sealed advisory, a UN report, a declassified document, a leaked-document archive already published by reputable outlets, or scholarship. **Learners are directed to no classified, criminal, or operational material, and none is needed for any task here.**

---

## Learning outcomes

On completion, a learner can:

1. **Distinguish** a state cyber programme from a criminal enterprise on the dimensions that matter analytically — tasking versus profit motive, restraint and deniability, resourcing, and target selection — and place a publicly documented operation on that spectrum with justification from sources.
2. **Explain**, structurally and neutrally, how state programmes are organised across the SIGINT / military / intelligence-service models, and describe the contractor-and-proxy market and the oversight arrangements around them — applying the **same** descriptive standard to adversary and to allied programmes, and naming only publicly acknowledged facts.
3. **Analyse** the attribution of a state operation as a method with explicit confidence levels, correctly separating (a) official government attribution, (b) journalism and leaks, and (c) analytic inference, and identifying where false-flag and deniability techniques complicate the picture.
4. **Evaluate** a documented effects or sabotage operation (e.g. the Stuxnet or NotPetya public records) as an organisational and strategic event — its tasking, its restraint or lack of it, and its escalation implications — without reference to any technical exploit detail.
5. **Analyse** the state–crime nexus in a named case — sponsorship, tasking, tolerance, or moonlighting — and state, with a confidence level, which relationship the public record actually supports, distinguishing an attributed state programme from a merely tolerated criminal one.
6. **Evaluate** influence and information operations as a documented state capability, at the level of organisation and attribution (drawing on the IRA/GRU indictments and Rid's *Active Measures*), without reproducing any technique.
7. **Apply** the correct Australian and allied framing — ASD/ACSC public attributions and co-sealed advisories, the *Autonomous Sanctions Act 2011* cyber listings, Australia's declared offensive-cyber capability and its oversight, and the SOCI critical-infrastructure implications — to a documented case, stating precisely what the record supports and what it does not.

> Bloom's 4–5 (Analyse / Evaluate) is the module's centre of gravity, reaching 6 (Create) where Exercise 1 has the learner *construct* a confidence-graded attribution assessment. This alignment statement is notional: CCI-04 is not credit-bearing and has not been through the AQF mapping process in [`docs/compliance/aqf-teqsa.md`](../../compliance/aqf-teqsa.md).

---

## Framework orientation

!!! note "Mappings are deferred to the Framework Custodian — no codes are asserted here"
    Consistent with the [series index](index.md), this extension module does not feed [ksat-coverage](../../ksat-coverage.md), and its framework mapping is **provisional pending Framework Custodian review**. To avoid asserting an identifier this author has not verified against a current release, the roles and skills below are named at the level this module confidently supports; the specific work-role codes, task IDs, SFIA skill codes and levels, and project-local KSAT IDs are **left to be assigned and verified**, not printed as fact. See the verification-status table.

    - **NIST Workforce Framework for Cybersecurity (NICE) — role families this module speaks to:** All-Source Analyst; Threat/Warning Analyst; Cyber Intelligence Planner; and the strategic-intelligence and mission-assessment role sets. (Work-role and task codes: **to be assigned by the Framework Custodian.**)
    - **SFIA — skill families:** Threat intelligence; Information security; and (for the strategic and national-security content) the specialist-advice and governance families as the Custodian judges appropriate. (Skill codes and proficiency levels: **to be assigned.**)
    - **ASD Cyber Skills Framework:** the Cyber Intelligence domain. (Sub-domain and proficiency: **to be assigned.**)
    - **MITRE ATT&CK:** ATT&CK describes *technical behaviours*, not the organisation, tasking, or attribution of a state programme, so it is only lightly relevant here. Where a tactic or technique **name** is used — for example the tactic name *Impact* for a destructive effects operation, or *supply-chain compromise* as the delivery pattern the NotPetya public reporting describes — it is in prose only, for recognition, with no procedural content. Specific technique IDs and the framework version are a CT-series concern, flagged provisional in this project and not asserted here.

---

## Module structure

| Part | Topics | Exercises | Notional hours |
|---|---|---|---|
| A — The strategic and CI lens on state cyber power | 1 | — | 2 |
| B — Organisation, attribution and effects | 2–4 | Exercise 1 | 6 |
| C — The state–crime nexus and influence operations | 5–6 | Exercise 2 | 4 |
| D — The Australian and allied position; consolidation | 7 | — | 2 |
| | | | **14 hours** |

---

## Topics

### Topic 1: The Strategic and Counter-Intelligence Lens on State Cyber Power

Why does a state run a cyber programme at all? The public record and the strategic-studies literature converge on four broad purposes, and naming them is the first analytic move because they predict behaviour: **espionage** (collecting foreign intelligence — political, military, economic, and increasingly commercial); **sabotage or effects** (degrading, disrupting, or destroying an adversary's systems or physical processes); **influence** (shaping foreign perceptions and politics — Topic 6); and, in at least one documented case, **revenue** (generating hard currency, the DPRK pattern in Topic 5). A single programme may pursue several; the analyst's job is to infer which one a given operation served, and with what confidence.

State operations differ from criminal ones along dimensions that are analytically load-bearing, and this module returns to them throughout:

- **Tasking, not profit.** A criminal crew chooses targets that pay; a state programme attacks what it is *tasked* to attack. Target selection that makes no commercial sense — a foreign ministry, a grid, an election commission — is itself a signal of a state hand.
- **Restraint and deniability.** A state usually has reasons *not* to be caught, or not to be provably caught: escalation risk, diplomatic cost, and the value of keeping a capability in reserve. This produces restraint and deception that a profit-driven criminal rarely bothers with — false flags, plausible-deniability proxies, and operations calibrated to stay below a threshold of response.
- **Resourcing.** States can sustain long, patient, well-funded operations, develop or buy capabilities a criminal could not, and absorb failures. Persistence and patience are, again, signals.
- **The stakes of getting attribution wrong.** Misattributing a criminal act is an analytic error; misattributing an act to a *state* can be a diplomatic incident. This is why the confidence discipline in Topic 3 matters more here than anywhere else in the series.

The counter-intelligence lens asks the CCI-series question — *how is this thing built, who tasks it, and where is it legible?* — of the state programme, while holding the neutrality rule fixed: the same descriptive frame is applied to every state, and the module states only what is on the public record for each.

**Key concepts:** the four purposes (espionage, sabotage, influence, revenue); tasking vs profit; restraint, deniability and escalation as state-specific constraints; the elevated stakes of state attribution; the same lens applied to every state.

---

### Topic 2: How State Programmes Are Organised

State cyber programmes are housed in a small number of recurring institutional models. The point of this topic is structural literacy — to recognise the *type* of organisation behind an operation — and it is applied **evenly to adversary and allied programmes alike**, naming only publicly acknowledged facts and never asserting a covert detail.

**The recurring models.**

- **The SIGINT-agency model.** A signals-intelligence agency, historically built for interception, extends into computer-network operations. This is the publicly acknowledged shape of the **Five Eyes** SIGINT partnership — the United States' NSA, Australia's **ASD**, the United Kingdom's GCHQ, Canada's CSE, and New Zealand's GCSB — a arrangement whose existence the member governments have themselves acknowledged. The specific collection activities of these agencies are, in the main, not officially detailed; where the public knows more, it is largely through the 2013 Snowden disclosures (a leak — Topic 3), which must be labelled as such and not treated as official confirmation.
- **The military-command model.** A uniformed command conducts cyber operations as a military function. **US Cyber Command** is the publicly documented example: established in 2010 as a sub-unified command and elevated to a full unified combatant command in May 2018, and led under a "dual-hat" arrangement jointly with the Director of the NSA. Australia's own capability (Topic 7) is a declared **joint civil–military** arrangement between ASD and the ADF.
- **The intelligence-/security-service model.** A foreign-intelligence or internal-security service runs cyber operations alongside its human-intelligence work. Several publicly attributed adversary programmes have been placed by attributing governments in this or the military model — for example, US and allied attributions have located "Sandworm" in **GRU Unit 74455** (Russian military intelligence), and the DPRK's cyber activity in the **Reconnaissance General Bureau** (Topic 5). These placements are the attributing governments' findings; this module reports them as such.

**The contractor and proxy market.** No modern programme is entirely in-house. States buy tooling, access, and services from a contractor market and, in some cases, task or tolerate proxies. Consistent with the series rules, a **company is named here only where a government has taken a public action against it or officially named it**; otherwise the contractor market is described structurally — a supply of capabilities, exploits, and services that states procure, which raises the same recognition-and-disruption questions [CCI-03](cci-03-the-service-economy.md) raised for the criminal market.

**Tasking and oversight.** What separates a lawful state programme from a criminal one, in the democracies that describe their arrangements, is **authorisation and oversight**: legal authority to act, ministerial or executive tasking, and independent review. Australia's arrangements (Topic 7) are the worked example. This module describes oversight where it is publicly documented and does not speculate where it is not.

**Key concepts:** the SIGINT / military-command / intelligence-service models; the Five Eyes SIGINT partnership as publicly acknowledged; US Cyber Command and the dual-hat arrangement; the contractor-and-proxy market described structurally; authorisation and oversight as the lawful-programme distinction; naming a company only on a public action.

---

### Topic 3: Attribution of State Operations as a Method

This topic is the analytic heart of the module, and it extends [CT02](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md) Topic 4 to the hardest case. Attribution of a state operation is a **claim with a confidence level and a caveat**, never a verdict, and the first discipline is to label the *kind* of claim you are dealing with:

- **(a) Official government attribution.** A government publicly names a state or its unit as responsible — in an indictment (an *allegation*, framed to meet legal elements), a sanctions designation (an executive *finding*), or a formal attribution statement or co-sealed advisory. This is the highest-status public claim, but it is still a claim, and governments themselves grade their confidence ("we assess, with high confidence…").
- **(b) Journalism and leaks.** Investigative reporting (for example David Sanger's Stuxnet reporting) and leaked-document archives (the 2013 **Snowden** documents; the 2016–2017 **Shadow Brokers** releases) can be detailed and credible, but they are **not** official confirmation. A programme "reported by journalists on the basis of anonymous officials" or "described in leaked documents" is exactly that, and the module says so rather than upgrading it to fact.
- **(c) Analytic inference.** A researcher or analyst infers a state hand from tradecraft, infrastructure, targeting, timing, or code overlap. This is legitimate and often correct, but it carries the lowest ceiling of the three and must be flagged as inference.

**False flags and deniability** are the reason this is hard. States have a documented interest in *not* being provably attributed, and in some cases in making an operation look like someone else's. The analyst therefore treats a clean, convenient attribution signal with suspicion, holds alternative hypotheses open (an ACH discipline from [CT01](../../../degrees/operational/cti/CT01-intelligence-tradecraft.md)), and states residual uncertainty rather than resolving it prematurely.

**The co-sealed advisory as public attribution.** A distinctive modern mechanism is the **co-sealed (jointly authored) advisory**, in which several governments' agencies — for example CISA, Australia's ASD/ACSC, the UK's NCSC, and Five Eyes partners — publish a single technical-and-attribution advisory under all their seals. Analytically, co-sealing is a **confidence signal**: multiple independent services have put their names to the same assessment. It is still an assessment, graded by its authors, and the analyst reads the confidence language the advisory itself uses rather than inflating it.

**Key concepts:** the three claim-types (a/b/c) and their confidence ceilings; governments grade their own confidence; false flags and deniability as reasons to hold alternatives open; the co-sealed advisory as a multi-service confidence signal but still an assessment.

---

### Topic 4: Sabotage and Effects Operations

Most state cyber activity is espionage. A smaller, more consequential class produces **effects** — disruption, destruction, or physical consequence — and two documented cases anchor the analysis, treated purely at the level of organisation, tasking, restraint, and attribution, **with no exploit or technical detail.**

**Stuxnet / Operation Olympic Games — the archetype, attributed through journalism, not officially confirmed.** The malware publicly known as Stuxnet, directed at Iran's uranium-enrichment programme and discovered in 2010, is the archetypal state sabotage operation with a physical effect. Its attribution status is a **teaching case in claim-type (b)**: David Sanger's June 2012 *New York Times* reporting (and his book of that year), together with Kim Zetter's *Countdown to Zero Day* (2014), described a joint US–Israeli programme reportedly codenamed "Olympic Games," begun under President Bush and expanded under President Obama, on the basis of interviews with current and former officials. **Neither the United States nor Israel has officially confirmed responsibility.** The correct register is therefore precise: Stuxnet is *reported by investigative journalists, on the basis of anonymous officials, to have been a US–Israeli operation; it has not been officially acknowledged.* The analytic value is in what the case shows about a state sabotage *programme* — the patience, the specificity of the target, the evident restraint in scope — not in the code.

**NotPetya — destructive spillover, officially attributed.** In June 2017 the destructive malware known as NotPetya, delivered through a compromised Ukrainian software supply chain, spread globally and caused losses widely reported in the billions. This case sits in claim-type (a): the United States, the United Kingdom, **Australia** (16 February 2018, in a statement by the then Minister for Law Enforcement and Cyber Security), and other governments **officially attributed** NotPetya to the Russian state, and the US **DOJ indictment unsealed on 19 October 2020** charged six officers of **GRU Unit 74455** ("Sandworm") in connection with NotPetya and a series of other operations (Ukrainian power-grid attacks, the 2018 PyeongChang "Olympic Destroyer," and more). The indictment is an *allegation*; the attribution statements are *findings*; the module keeps that wording exact.

**The restraint and escalation questions.** These two cases frame the strategic questions an analyst must reason about without moralising: Was the effect **contained** (Stuxnet, narrowly targeted) or **uncontrolled** (NotPetya, global spillover)? Was it **calibrated** to stay below a threshold of response, or did it cross one? What **escalation** did it invite or deter? These are analytic questions about state behaviour, asked identically of whichever state the record documents.

**Key concepts:** effects operations as the consequential minority; Stuxnet as the archetype and a claim-type-(b) case not officially confirmed; NotPetya as officially attributed destructive spillover with a DOJ indictment; the restraint/containment/escalation questions asked neutrally.

---

### Topic 5: The State–Crime Nexus

The line between state and criminal is, in several documented cases, not a line. This topic sets out the relationship types and the evidence for each, and the analytic skill is to say **which** relationship a case supports, and with what confidence.

- **The state as criminal — the DPRK revenue model.** The clearest documented case of a state programme run **for revenue** is the DPRK. US charging documents place the activity in the **Reconnaissance General Bureau**: the **DOJ criminal complaint unsealed on 6 September 2018** charged Park Jin Hyok in connection with the 2014 Sony attack, the 2017 WannaCry outbreak, and the 2016 Bangladesh Bank theft; the **indictment unsealed on 17 February 2021** added Jon Chang Hyok and Kim Il and alleged a conspiracy to steal and extort **more than US$1.3 billion**. This is the [CCI-02](cci-02-the-criminal-economy.md) money problem run *as state policy* — theft to generate hard currency under sanctions. For quantified totals beyond the indictment, the analyst should cite **UN reporting** and its successor: the UN Panel of Experts monitoring DPRK sanctions **lapsed on 30 April 2024** after a Russian veto on 28 March 2024, and the **Multilateral Sanctions Monitoring Team (MSMT)**, established in October 2024 by eleven states including Australia, is the successor mechanism for later figures.
- **The state as tolerator — the safe-harbour dynamic.** A different relationship is **tolerance**: a state does not task a criminal crew but declines to prosecute or extradite it, provided it does not attack domestic targets. Western agency and government reporting has **characterised** Russia as tolerating ransomware crews under such a safe-harbour, non-extradition dynamic. The analyst records this as an **agency assessment / analytic inference** (claim-types a/c), not as a proven tasking relationship, and is careful not to upgrade "tolerated" into "directed" without evidence.
- **Proxies and "patriotic hackers."** States may task or encourage proxies — nominally independent "patriotic" hackers or hacktivist fronts — precisely because the arrangement provides deniability (Topic 3). The relationship is often deliberately ambiguous, which is the point; the analyst treats the degree of state control as an open question graded by evidence.
- **Moonlighting and the blurred individual.** Finally, the same *people* may work both sides — a state operator moonlighting for profit, or a criminal occasionally tasked by a service. Public reporting on individuals who appear in both state-attribution and criminal contexts illustrates that the "state vs criminal" question is sometimes wrongly framed as either/or.

The disciplined output is a **labelled relationship claim**: *tasked* (state directs), *sponsored* (state resources or enables), *tolerated* (state declines to act), or *overlapping* (shared people) — each with a confidence level and the source behind it.

**Key concepts:** tasked / sponsored / tolerated / overlapping as the relationship taxonomy; the DPRK as the state-as-criminal revenue case (RGB; 2018 and 2021 DOJ actions; UN/MSMT for totals); the safe-harbour dynamic as an agency assessment, not proven tasking; proxies and deniability; moonlighting and the blurred individual.

---

### Topic 6: Influence and Information Operations as a State Programme

Not all state cyber power is technical. **Influence operations** — the use of information, including deception and manipulation, to shape a foreign audience — are a documented state capability, and this topic treats them at the level of **organisation and attribution**, never technique, and never as a partisan claim.

The scholarly anchor is Thomas Rid's *Active Measures: The Secret History of Disinformation and Political Warfare* (2020), which places contemporary operations in a long lineage of state "active measures" and supplies the vocabulary for analysing them as *programmes* rather than as isolated posts. The documented, officially attributed cases are the two US special-counsel indictments of 2018:

- The **Internet Research Agency (IRA) indictment**, unsealed **16 February 2018**, charged the St Petersburg "troll farm," its financier, and associated individuals and entities with a scheme to interfere in the 2016 US election through coordinated inauthentic social-media activity. It is an *allegation*, and it describes an **organisation** — staffing, budgeting, and tasking of an influence operation — which is exactly the analytic level this topic works at.
- The **GRU indictment**, unsealed **13 July 2018**, charged twelve GRU officers in connection with the hack-and-leak operations against US political organisations during the same election.

The analytic points are organisational and neutral. Influence operations are run like *programmes*, with budgets, staff, and tasking, which is what makes an indictment such a rich organisational source. Attribution follows the same three claim-types as Topic 3 — an indictment is an allegation, a platform's or researcher's takedown report is inference or corporate finding, and the analyst does not blur them. And the module takes **no view** on the politics of any operation's content; its subject is the *existence, organisation, and attribution* of the capability, applied to whichever state the record documents.

**Key concepts:** influence operations as a documented, programme-level state capability; Rid's *Active Measures* as the analytic frame; the 2018 IRA and GRU indictments as officially attributed cases read for organisation; the same three claim-types; strict neutrality on content and politics.

---

### Topic 7: The Australian and Allied Position

This topic anchors the module in Australia's declared arrangements and public actions (R4), and treats allied capability by the same standard applied to every other state — stating only what is publicly acknowledged.

**Australia's public attributions and co-sealed advisories.** Australia, through **ASD/ACSC**, is a regular participant in public attribution and in **co-sealed (jointly authored) advisories** with Five Eyes and other partners (Topic 3). Australia's February 2018 attribution of NotPetya to Russia (Topic 4) is one documented example; ASD/ACSC also co-authors joint advisories on state-attributed activity. These are the mechanism by which Australia converts an intelligence assessment into a public, graded attribution, and they are the primary Australian-source material for the exercises.

**The Autonomous Sanctions Act 2011 cyber listings.** On **23 January 2024**, Australia used its autonomous **cyber**-sanctions power for the **first time**, listing Russian national **Aleksandr Ermakov** — alleged to be connected to the criminal group REvil — over the 2022 Medibank Private breach (personal information of about **9.7 million** people), in coordination with the US and UK. This is the same instrument [CCI-01](cci-01-the-cybercriminal-enterprise.md) and [CCI-02](cci-02-the-criminal-economy.md) treat on the criminal side; its relevance here is the **nexus** — the sanction targets a criminal actor whose activity is a national-security concern, exactly the blurred border this module studies. The listing is an executive **finding** and the named person **alleged**; sanction status changes, so it is flagged for re-verification.

**Australia's declared offensive-cyber capability and its oversight.** In **April 2016**, then Prime Minister Turnbull publicly **acknowledged that Australia has an offensive cyber capability** — reportedly the first time a state had so declared — with the technical capability residing in **ASD** and military operations conducted as a **joint civil–military** arrangement governed by ADF rules of engagement. The analytic point for this module is **oversight**: Australia's arrangements sit within a framework of legal authority, ministerial authorisation, and independent review (for example the Inspector-General of Intelligence and Security and parliamentary oversight), which is what publicly distinguishes a lawful state programme from a criminal one (Topic 2). The module describes this at the level of the public declaration and does not detail operations.

**The state–crime nexus and Australian critical infrastructure (SOCI).** The reason this all matters for Australia is critical-infrastructure risk. The state–crime nexus means an Australian critical-infrastructure operator may face an adversary that is a state, a state-tolerated criminal, or something in between — and the **Security of Critical Infrastructure Act 2018 (SOCI)** regime, with its risk-management and incident obligations for responsible entities, is the national response to exactly that ambiguity. For the analyst, the nexus is why "is this criminal or state?" is not an academic question for an Australian CI defender: it changes the threat model, the likely persistence, and the appropriate national response.

**Key concepts:** ASD/ACSC public attribution and co-sealed advisories; the *Autonomous Sanctions Act 2011* cyber listings and the Ermakov "first use" as a nexus case; Australia's 2016-declared offensive-cyber capability (ASD/ADF joint) and its oversight; SOCI and the CI relevance of the state–crime nexus.

---

## Exercises

Both exercises are **intelligence-analysis tasks over public reporting**. There is no lab, no tooling, and nothing operational. Each is completable from freely available web sources — government attributions, indictments, sanctions designations, co-sealed advisories, UN/MSMT reports, and reputable scholarship and journalism — and the further-reading list is a starting point, not a limit.

!!! warning "Sourcing, neutrality and conduct"
    Use only lawful, public sources. Do **not** attempt to access any classified, criminal, or operational material — it is unnecessary, may be unlawful, and is outside the authorisation of this module. Apply the **same evidence standard to every state**, adversary and allied alike; attribute every claim to its source with a confidence level; treat every named individual as **alleged / attributed** and cite the record that names them; and do not editorialise or take a political side. Where the public record attributes only with low or medium confidence, or only through a leak, your assessment must say so.

### Exercise 1 (Analytical): Build a Confidence-Graded Attribution Assessment of a Named Operation

**Objective:** Produce a defensible, confidence-graded attribution assessment of one publicly documented state operation, using only public sources, correctly labelling every claim by type and never overstating.

**Prerequisites:** Topics 1, 3, 4.

**Task:**

1. Choose **one** documented operation with a substantial public record — for example **Stuxnet / Olympic Games** (a claim-type-(b) case, attributed through journalism and *not* officially confirmed), **NotPetya** (a claim-type-(a) case with official attributions and the 2020 DOJ Sandworm indictment), or another operation with an equally rich public record.
2. Assemble a **source inventory** of at least five items and label each by claim-type: (a) official attribution — indictment, designation, or co-sealed advisory; (b) journalism/leak; (c) analytic inference/research.
3. Write the **attribution assessment**: state who the operation is attributed to, by whom, and — crucially — **at what confidence and on what basis**, using the language the sources themselves use ("indicted," "assessed with high confidence," "reported on the basis of anonymous officials," "not officially confirmed"). Grade your own overall confidence and justify it.
4. Address **deniability and alternatives**: identify any false-flag or deniability considerations and at least one alternative hypothesis you cannot fully exclude (an ACH discipline from [CT01](../../../degrees/operational/cti/CT01-intelligence-tradecraft.md)).
5. Write a half-page **caveats-and-gaps note**: what the record does *not* establish, and what would raise or lower your confidence.

**Expected output:** the labelled source inventory; the confidence-graded attribution assessment; the deniability-and-alternatives analysis; the caveats-and-gaps note. Marked on **discipline** — every claim traceable to a labelled source and honestly graded, with no allegation laundered into a fact and no leak upgraded to official confirmation — not on the strength of the conclusion.

**Reflection:**

1. Where did you most have to resist upgrading a claim-type-(b) or (c) statement into a claim-type-(a) fact, and how did you word it to avoid that?
2. If your operation is officially attributed, what confidence language did the attributing government itself use — and did any secondary reporting overstate it?
3. What single additional public document would most change your confidence, and why can you not simply assume its contents?

### Exercise 2 (Analytical): Compare Two States' Programme Structures from Official Reporting

**Objective:** Compare the *organisation and tasking* of two states' cyber programmes — treating adversary and allied programmes by the **same standard** — using only publicly acknowledged facts, and characterise any state–crime relationship each involves.

**Prerequisites:** Topics 2, 5, 7.

**Task:**

1. Choose **two** states whose programmes have a public record — and, to exercise the neutrality rule, choose them so that **at least one is an allied/Western programme** (for example Australia's declared ASD/ADF capability or US Cyber Command) and at least one is a publicly attributed adversary programme (for example the DPRK RGB or GRU-attributed activity).
2. For each, describe the **organisational model** (SIGINT / military-command / intelligence-service — Topic 2) and the **oversight and tasking** arrangements, using only publicly acknowledged facts and labelling anything known only through a leak as such.
3. Characterise any **state–crime relationship** each programme involves, using the Topic 5 taxonomy (*tasked / sponsored / tolerated / overlapping / none evident*), with a confidence level and a source for each characterisation.
4. Produce a **comparison table**: purpose(s), organisational model, oversight (where public), and state–crime relationship, side by side, with a confidence level in every cell and a note where the public record is silent.
5. Write a half-page **neutrality-and-evidence note**: state explicitly where your evidence base differs between the two states (allied programmes often disclose more; adversary programmes are known largely through attribution and leaks), and how you avoided letting that asymmetry become a double standard.

**Expected output:** the two structural descriptions; the state–crime characterisations with confidence; the comparison table; the neutrality-and-evidence note. Marked on **even-handedness and honest uncertainty** — the same evidentiary standard applied to both states, every claim sourced and graded, and the evidence asymmetry named rather than smuggled in as a judgement.

**Reflection:**

1. Where was more publicly known about the allied programme than the adversary one (or vice versa), and how did you stop that asymmetry from reading as a verdict about either state's conduct?
2. Which state–crime relationship was hardest to grade, and what would you need to move it from "tolerated" to "tasked," or from inference to official finding?
3. If a reader accused your assessment of taking a side, which sentence would you point to as evidence that you did not — and is it actually neutral, or does it only sound neutral?

---

## Australian context

Australia is both a **participant** in allied cyber power and a **target** of the state and state-adjacent activity this module studies, and its public instruments are specific.

**Public attribution and co-sealed advisories.** Australia, through **ASD/ACSC**, contributes to and co-signs public attributions and jointly authored advisories with Five Eyes and other partners. Australia's **16 February 2018** attribution of NotPetya to Russia is a documented example of converting an intelligence assessment into a public, graded attribution; ASD/ACSC also co-authors advisories on state-attributed activity. Read as intelligence products, these are the mechanism through which Australia states, publicly and with a confidence level, that a particular state was responsible — the claim-type-(a) source the exercises lean on.

**Autonomous cyber sanctions (Autonomous Sanctions Act 2011).** On **23 January 2024**, Australia exercised its autonomous **cyber**-sanctions power for the **first time**, listing Russian national **Aleksandr Ermakov** — alleged to be linked to the REvil criminal group — over the 2022 Medibank Private breach (about **9.7 million** people's personal information), in a coordinated action with the United States and United Kingdom. The listing makes it a criminal offence to deal with the person's assets. Its significance for this module is the **nexus**: the instrument sits on the criminal side of the ledger ([CCI-01](cci-01-the-cybercriminal-enterprise.md)/[CCI-02](cci-02-the-criminal-economy.md)) but is used against activity that Australia treats as a national-security concern — the blurred border made concrete. It is an executive **finding**, the named person is **alleged**, and, because sanction status changes, it is flagged for re-verification at delivery.

**Australia's declared offensive-cyber capability and its oversight.** In **April 2016**, then Prime Minister Turnbull publicly **acknowledged that Australia has an offensive cyber capability** — reportedly the first such public declaration by a state — with the capability residing in **ASD** and military operations conducted as a **joint civil–military** ASD/ADF arrangement under ADF rules of engagement. Treated by the module's neutral standard, the analytically important feature is **oversight**: legal authority, ministerial authorisation, and independent review (including the Inspector-General of Intelligence and Security and parliamentary oversight) are what publicly distinguish this lawful state programme from a criminal enterprise. The module describes this at the level of the public declaration only.

**The state–crime nexus and critical infrastructure (SOCI).** The reason the state end of the spectrum matters for Australia is critical-infrastructure risk. An Australian operator may face a state, a state-tolerated criminal, or something in between — and the **Security of Critical Infrastructure Act 2018** regime, with its risk-management and incident-reporting obligations for responsible entities, is the national instrument built for that ambiguity. For the analyst supporting a CI defender, "state or criminal?" changes the threat model, the expected persistence, and the appropriate national response — which is why the nexus is a practical Australian concern, not an abstraction.

**The agencies.** ASD/ACSC produces the attribution and advisory material and holds the declared offensive capability; the ADF conducts military cyber operations jointly with ASD; DFAT administers the sanctions lists; and the oversight bodies provide the review that legitimises the whole arrangement. Legal authority for teaching from this material rests on it already being public; this module directs no one to any classified, criminal, or operational material.

---

## Verification status

This module has **not** had practitioner review (R2). It must not be presented to learners as verified content until a Domain Expert and Practitioner Reviewer have signed off. Because this is the politically sensitive module, the highest-risk review items are **political neutrality and the even application of the evidence standard across all states**, the **currency and correctness of every named individual's public-action status**, and **not overstating attribution confidence**. Every attribution, date, and figure below was checked against a primary or authoritative source during authoring, but each must be re-verified at delivery.

| Item | Status | Action required |
|---|---|---|
| **Neutral / same-standard framing across all states** — adversary and allied programmes described by the identical evidence standard; claims attributed to source with confidence and caveats; no editorialising, moralising, or taking a side | **Blocking** | Requires the reviewer's explicit sign-off that the module is politically neutral and applies one standard to every state |
| **Every named individual currently and correctly subject to a public action** (Ermakov; the six GRU/Unit 74455 defendants; Park Jin Hyok, Jon Chang Hyok, Kim Il; the 2018 IRA and GRU indictees) | **Must be re-verified at delivery** | Legal and sanction status changes (charges dropped, convictions entered, sanctions lifted). Re-confirm each against the primary record; keep *alleged/attributed* wording exact; name no serving intelligence officer not subject to such a public action |
| **Attribution confidence not overstated** — every claim labelled (a) official attribution, (b) journalism/leak, or (c) inference, at no higher confidence than the source supports | **Blocking / provisional** | Do not upgrade an allegation, an assessment, or a leak into a fact or a verdict; check each verb against the source, especially for Stuxnet (see below) |
| **Stuxnet / Olympic Games attribution** — US/Israel per Sanger (NYT, June 2012) and Zetter (*Countdown to Zero Day*, 2014); **not officially confirmed** by either government | **Verified as reported; claim-type (b)** | Confirm the "reported by journalists, not officially confirmed" framing is preserved verbatim; do not state as official attribution |
| **NotPetya attribution** — official attributions by US/UK/Australia (Australia 16 Feb 2018) and the DOJ indictment of six GRU Unit 74455 officers unsealed 19 Oct 2020 | **Verified against DOJ / government statements as reported** | Confirm against the DOJ press release and the Australian government statement; keep indictment = allegation |
| **DPRK: DOJ Park Jin Hyok complaint (unsealed 6 Sep 2018) and three-defendant indictment (unsealed 17 Feb 2021, >US$1.3bn alleged); RGB attribution** | **Verified against DOJ as reported** | Confirm names, dates, and the >$1.3bn figure against the DOJ records; keep RGB attribution as the DOJ's finding |
| **UN Panel of Experts (DPRK) mandate lapsed 30 Apr 2024** (Russian veto 28 Mar 2024); **MSMT successor established Oct 2024** (eleven states incl. Australia) | **Verified against UN / MSMT / reputable reporting as reported** | Cite MSMT (not the lapsed PoE) for post-April-2024 figures; confirm the dates and membership |
| **Russian tolerance of ransomware / safe-harbour dynamic** | **Agency assessment / inference (claim-types a/c) — not proven tasking** | Present as characterised in Western agency/government reporting; do **not** upgrade "tolerated" to "tasked/directed"; cite the specific reporting used |
| **IRA indictment (unsealed 16 Feb 2018) and GRU indictment (unsealed 13 Jul 2018, twelve officers)** | **Verified against DOJ as reported** | Confirm dates and counts against the DOJ records; keep as allegations; maintain neutrality on political content |
| **Ermakov / Medibank as Australia's first autonomous cyber-sanction listing (23 Jan 2024; ~9.7m affected; US/UK coordinated)** | **Verified against ASD/DFAT/Minister releases as reported** | Confirm "first use" wording and the coordination against the official releases; sanction status may change |
| **Australia's declared offensive-cyber capability (April 2016 PM acknowledgement; ASD capability; ASD/ADF joint) and oversight** | **Verified against government statements / ASPI as reported** | Confirm the 2016 acknowledgement and the ASD/ADF framing; describe oversight only at the publicly documented level |
| **US Cyber Command (established 2010; elevated to unified combatant command May 2018; NSA dual-hat) and the Five Eyes SIGINT partnership as publicly acknowledged** | **Verified as reported** | Confirm against DoD/authoritative sources; name no covert activity; label Snowden/Shadow Brokers material as leaks |
| **Security of Critical Infrastructure Act 2018 (Cth) relevance** | **Verified as to the principle; scope provisional** | Verify current asset classes, obligations and rules against the Act at delivery |
| **No lawful private entity implied criminal; contractor market described structurally; company named only on a public government action** | **Blocking** | Requires the reviewer's sign-off that no lawful firm, researcher or conference is implied criminal (a CCI-06 subject) |
| Framework mapping (NICE work-role and task codes; SFIA skill codes and levels; ASD CSF sub-domain; project-local KSAT IDs) | **Deferred — not asserted** | Assign and verify with the Framework Custodian; this module intentionally prints no codes |
| MITRE ATT&CK tactic/technique references (e.g. *Impact*; supply-chain compromise as the NotPetya delivery pattern) | **Names used for recognition only; IDs not asserted** | Technique IDs and framework version remain a project-wide provisional item in the CT series |

---

## Further reading

Real, citable starting points. All are public; treat government and court pages as primary, agency and UN pages as institutional, and reporting and scholarship as reputable secondary. Apply the same standard to every source regardless of the state it concerns. Australian sources are marked.

**U.S. Department of Justice (October 2020).** *Six Russian GRU Officers Charged in Connection with Worldwide Deployment of Destructive Malware and Other Disruptive Actions in Cyberspace* (Unit 74455 / "Sandworm"; NotPetya and more). justice.gov.
> Relevance: The primary official-attribution record for NotPetya and Topic 4; a claim-type-(a) source for Exercise 1.

**U.S. Department of Justice (September 2018; February 2021).** The Park Jin Hyok criminal complaint and the three-defendant DPRK indictment (Reconnaissance General Bureau; >US$1.3bn alleged). justice.gov.
> Relevance: The state-as-criminal revenue case in Topic 5 and its cross-reference to [CCI-02](cci-02-the-criminal-economy.md).

**U.S. Department of Justice (February 2018; July 2018).** The Internet Research Agency indictment and the GRU (twelve-officer) indictment. justice.gov.
> Relevance: The officially attributed influence and hack-and-leak cases read for organisation in Topic 6.

**Multilateral Sanctions Monitoring Team (MSMT) reports; and archived UN Panel of Experts (1718 Committee) reports.** msmt.info; un.org.
> Relevance: The successor mechanism (established October 2024) and the archived PoE material (mandate lapsed 30 April 2024) for quantified DPRK figures in Topic 5.

**Australian Signals Directorate / ACSC.** *Annual Cyber Threat Report*, public attribution statements, and co-sealed advisories. cyber.gov.au (**Australian source**).
> Relevance: The Australian attribution and co-sealed-advisory mechanism in Topics 3 and 7 and the primary Australian material for the exercises.

**Minister for Foreign Affairs / DFAT (January 2024).** Media releases on the Ermakov / Medibank cyber sanction and the consolidated sanctions list. foreignminister.gov.au; dfat.gov.au (**Australian source**).
> Relevance: Australia's first autonomous cyber-sanction listing and the nexus case in Topic 7; verify status here.

**Australian Government — Federal Register of Legislation.** *Autonomous Sanctions Act 2011* (Cth); *Security of Critical Infrastructure Act 2018* (Cth). legislation.gov.au (**Australian source**).
> Relevance: The primary Australian legal instruments for the Australian-context section; verify current provisions.

**Australian Strategic Policy Institute (ASPI).** *Australia's Offensive Cyber Capability* (policy brief). aspi.org.au (**Australian source**).
> Relevance: The public account of Australia's 2016-declared offensive capability and its oversight in Topic 7; treat as reputable secondary analysis of publicly acknowledged facts.

**David E. Sanger (2012).** *"Obama Order Sped Up Wave of Cyberattacks Against Iran," The New York Times* (June 2012), and *Confront and Conceal*. nytimes.com.
> Relevance: The primary journalistic source (claim-type (b)) for the Stuxnet / Olympic Games attribution in Topic 4 — reported, not officially confirmed.

**Kim Zetter (2014).** *Countdown to Zero Day: Stuxnet and the Launch of the World's First Digital Weapon.* Crown.
> Relevance: The book-length investigative account of Stuxnet for Topic 4 and Exercise 1; a claim-type-(b) source.

**Thomas Rid (2020).** *Active Measures: The Secret History of Disinformation and Political Warfare.* Farrar, Straus and Giroux.
> Relevance: The analytic frame for influence operations as state programmes in Topic 6.

---

## Module metadata

| Field | Value |
|---|---|
| Module Code | CCI-04 |
| Module Title | State-Sponsored Operations & the State–Crime Nexus |
| Series | EXT-CCI — Adversary Counter-Intelligence |
| Module Type | Extension module (elective; **not** credit-bearing) |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 0 CP — outside the 160 CP degree structure |
| Notional Hours | 14 |
| Extends | CT02 (Threat Actor Research & Profiling) Topic 4; CT04 (Strategic Intelligence) |
| Related Units | F04, OC05, CT01, CT02, CT04 |
| Prerequisites | CT02 and CT04 strongly recommended; CCI-01/02/03, F04, OC05, CT01 recommended |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-09-22 |
| Framework Mapping | Deferred to Framework Custodian (no codes asserted; see Framework orientation) |
| Bloom's Level (range) | 4–5 (Analyse, Evaluate), reaching 6 (Create) in Exercise 1 |
| Australian Context | ASD/ACSC public attributions and co-sealed advisories; Autonomous Sanctions Act 2011 (Cth) cyber listings (Ermakov/Medibank, Jan 2024, Australia's first); Australia's declared offensive-cyber capability (ASD/ADF, 2016) and its oversight; Security of Critical Infrastructure Act 2018 (Cth) |
| Tooling Licence Position | No tooling required; both exercises are analysis over public sources (R3) |
| Risk Note | Politically sensitive module — highest risks are political neutrality / same-standard framing across all states, the currency and correctness of every named individual's public-action status, and not overstating attribution confidence; the neutrality row is a blocking review item |
| Licence | CC BY 4.0 |
