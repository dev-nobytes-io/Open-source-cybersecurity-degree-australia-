# EXT-CCI: Adversary Counter-Intelligence — The Cybercrime & State-Cyber Ecosystem

> **Module type:** Extension module series (counter-intelligence / strategic-CTI elective)
> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-09-22
> **Domain Expert:** _Unassigned — required before Practitioner Approved (CTI or law-enforcement cyber background)_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved (must have worked adversary attribution, financial-crime intelligence, or a government cyber programme)_

!!! warning "This is an extension series, not credit-bearing units"
    EXT-CCI sits **outside** the fixed degree structure (see
    [`docs/structure.md`](../../structure.md); structural changes require the process in
    [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)). It carries **0 CP**, is not assessed for
    the award, and does not appear in [`docs/ksat-coverage.md`](../../ksat-coverage.md) or
    the [Program Builder](../../program-builder/index.md), both generated from
    credit-bearing units only. A delivery partner wanting to recognise it uses the Tier 1
    badge mechanism in
    [`docs/curriculum/micro-credentials-framework.md`](../../curriculum/micro-credentials-framework.md).

!!! danger "Read this first — what this series is, and is not"
    Most cyber teaching focuses on **what adversaries do** (the techniques). This series is
    deliberately about the adversary **as an organisation and an economy** — how criminal
    enterprises and state programmes recruit, finance, launder, resource, partner, and
    coordinate — studied the way a counter-intelligence analyst studies a target.

    **It is analysis of publicly documented adversaries, not a manual.** Everything here is
    built from published, attributable sources: government indictments and sanctions,
    court records, regulator and agency reporting, blockchain-analysis publications, and
    peer-reviewed and industry research. The series contains **no operational tradecraft** —
    nothing that would help anyone recruit for, finance, launder for, resource, or join a
    criminal enterprise. Where it explains a mechanism (e.g. how mixing services obscure a
    flow of funds), it does so at the level a defender or investigator needs to *recognise
    and disrupt* it, citing the public reporting that already describes it.

    **Legitimate security businesses, researchers and conferences are not criminal
    organisations and are never presented as such.** Firms such as SpecterOps and Black
    Hills Information Security, and conferences such as Black Hat and DEF CON, are lawful
    participants in a **dual-use** research economy. Where the series discusses them
    ([CCI-06](#planned-modules)), it is precisely to draw the line between lawful offensive
    research and criminal enterprise — the grey market between them is itself the
    counter-intelligence lesson. Nothing in this series alleges wrongdoing by any lawful
    person or company.

    **Named individuals appear only where a government has publicly charged, sanctioned, or
    formally attributed them**, and are described as *alleged* / *attributed* per due
    process — an indictment or sanction is an allegation or an executive finding, not a
    court's verdict of guilt. The series teaches attribution as a **method with confidence
    and caveats** (extending [CT02](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md)
    Topic 4), not as the pronouncement of verdicts.

!!! note "Delivered in stages"
    This series is added over several pull requests, in module order, on top of this index.
    **The series index is present.** CCI-01 to CCI-06 and the self-assessment quiz are
    listed below as planned; each is linked from this page only once its file is in the
    repository, so the site build stays free of dangling links.

---

## Why this series exists

The degree already teaches threat intelligence — [CT01–CT06](../../../degrees/operational/cti/README.md)
cover tradecraft, actor profiling, technical and strategic intelligence, platforms, and a
capstone — and the credit-bearing units now reach the adversary economy at two points:
[`F04`](../../../core/units/F04-security-concepts.md) introduces the cybercriminal ecosystem
as vocabulary, and [`CT02`](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md)
Topic 7 profiles the financially motivated organisation as an intelligence target.

What none of them does — because it is a specialisation, not a core competency — is treat
the **organisational and economic structure of the adversary** as a subject in its own
right: the enterprise design of a ransomware cartel, the plumbing of criminal finance and
laundering, the service economy (RaaS, initial-access broking, exploitation-development and
information brokering as products), the state–crime nexus and safe-harbour politics, and the
counter-intelligence discipline used to penetrate, attribute, and disrupt all of it. That is
what a financial-crime intelligence analyst, a national-security cyber analyst, or a
threat-intelligence lead specialising in actor tracking actually spends their time on, and
it is the gap this series fills.

## What this series is *not*

- **Not a replacement for CT01–CT06.** It is a specialisation that builds on them. Where it
  needs actor-profiling or attribution method, it references CT02 rather than re-teaching it.
- **Not a how-to for any criminal activity.** No recruitment channels, market access,
  laundering procedures, or infrastructure are provided; the series describes these
  mechanisms only as an investigator recognises them, from public reporting.
- **Not an allegation against any lawful person or organisation.** See the danger box above.
- **Not vendor-specific (R3).** Analysis relies on open reporting and free/open tooling
  (e.g. public blockchain explorers, court-record databases); no paid platform is required.

## Planned modules

| Module | Title | Focus |
|---|---|---|
| **CCI-01** | The Cybercriminal Enterprise | Organisation and roles; recruitment and vetting; resourcing and internal OPSEC; how a crime group is *run*, from forum crews to cartel-scale RaaS operations |
| **CCI-02** | The Criminal Economy: Financing, Laundering & Cash-Out | Revenue models; cryptocurrency laundering (mixers, chain-hopping, cash-out networks) as blockchain analysts describe it; sanctions and asset-seizure as counter-levers |
| **CCI-03** | The Service Economy | Cybercrime-as-a-service as an *industry*: RaaS, initial-access brokering, exploitation-development and access-as-a-service, information/intelligence brokering, bulletproof hosting, partnering and criminal supply chains |
| **CCI-04** | State-Sponsored Operations & the State–Crime Nexus | Documented state cyber programmes; sponsorship, tasking, and tolerance; safe-harbour and non-extradition dynamics; the blurred line between state operation and criminal moonlighting |
| **CCI-05** | Case Studies in the Adversary Economy | Publicly documented operations analysed as organisational and economic events (see the case list below) |
| **CCI-06** | Counter-Intelligence Practice & the Dual-Use Economy | The CI discipline applied to cyber adversaries — penetration, informants, attribution, disruption, takedowns — and the **lawful** dual-use research economy (the offensive-security industry, conferences, and the exploit market) as its necessary contrast |
| — | Self-assessment quiz | Series-level formative check |

## Case studies (CCI-05, and threaded through the series)

Each is chosen because it is **publicly and officially documented** — through indictments,
sanctions, agency reporting, or court records — and each is analysed for what it shows about
adversary *organisation, economics, or state relationship*, not for reusable technique.

- **Operation Olympic Games / Stuxnet** — state-sponsored sabotage as a documented programme;
  the archetype of a national cyber operation with physical effect.
- **Colonial Pipeline (DarkSide, 2021)** — RaaS affiliate economics, the ransom-and-clawback,
  and critical-infrastructure impact; a case where funds were partially recovered.
- **Bangladesh Bank heist (2016)** — a state-attributed (DPRK / "Lazarus") digital bank heist;
  the SWIFT abuse, the cash-out network, and the money-laundering trail.
- **NotPetya (2017)** — state-attributed destructive operation using a leaked exploit; supply-chain
  delivery and global collateral damage.
- **EternalBlue** — the life-cycle of a leaked state-developed exploit and its reuse by
  criminal and state actors (WannaCry, NotPetya); the vulnerability-and-exploit economy.
- **Cryptojacking campaigns** — low-friction monetisation and its economics.
- **Cyber-enabled organised and physical crime** — where digital intrusion, insider access,
  and physical operations combine (e.g. port-logistics compromise for smuggling), as
  documented by law enforcement.
- **TeamPCP (2025–26)** — a current supply-chain extortion group (the Shai-Hulud worm),
  **with two alleged members arrested in Perth in August 2026** — an Australian
  counter-intelligence and law-enforcement case study (R4).

> Several further items the maintainer proposed — the "Spectre"/Meltdown hardware
> vulnerabilities, and the histories of specific offensive-security firms and conference
> talks — are folded into **CCI-06** under the lawful **dual-use research economy**, not the
> criminal-organisation modules, because that is what they are. See the danger box.

## Australian context (R4)

The series is anchored to Australian material wherever the topic is legal or regulatory:
the *Autonomous Sanctions Act 2011* cyber-sanctions framework (used against named ransomware
actors), the *Cyber Security Act 2024* ransomware-payment reporting duty, ASD/ACSC threat
reporting and co-sealed international advisories, AUSTRAC's role in criminal-finance
intelligence, and Australian law-enforcement actions including the TeamPCP arrests. Legal
authority for consuming and teaching from public reporting rests on that material being
already public; the series directs no one to criminal infrastructure.

## Mapping onto the degree

| Related unit | Relationship |
|---|---|
| [`F04` Security Concepts](../../../core/units/F04-security-concepts.md) | Introduces the cybercriminal ecosystem as vocabulary; CCI goes to organisational and economic depth |
| [`CT01` Intelligence Tradecraft](../../../degrees/operational/cti/CT01-intelligence-tradecraft.md) | Provides the tradecraft (collection, analysis, bias) this series applies to the adversary economy |
| [`CT02` Threat Actor Research & Profiling](../../../degrees/operational/cti/CT02-threat-actor-research-profiling.md) | Topic 7 profiles the criminal organisation; CCI extends into financing, service economy, and the state nexus |
| [`CT04` Strategic Intelligence](../../../degrees/operational/cti/CT04-strategic-intelligence.md) | Strategic-level analysis; CCI adds the counter-intelligence and financial-crime lenses |
| [`OC05` Threat Intelligence Fundamentals](../../../core/units/OC05-threat-intelligence-fundamentals.md) | Operational-core grounding CCI assumes |

## Verification status

Provisional pending Domain Expert and Practitioner Reviewer sign-off. Specific items to
verify before delivery:

| Item | Status |
|---|---|
| Every named individual is currently and correctly the subject of a public charge, sanction, or government attribution | **Must be re-verified at delivery** — legal status changes (charges dropped, convictions entered, sanctions lifted) |
| Attribution statements match the confidence expressed by the attributing government/source | Provisional — must not overstate a "suspected" as "confirmed" |
| Australian legislative and sanction references (Autonomous Sanctions Act 2011, Cyber Security Act 2024, AUSTRAC role) current as at delivery | Provisional — verify against the current instruments |
| The lawful/criminal boundary in CCI-06 has been checked so no lawful person or company is implied to be criminal | **Blocking** — requires the reviewer's explicit sign-off |
| Blockchain-laundering and finance mechanisms are described at recognition level only, not as procedure | Provisional |

## Further reading (anchors — expanded per module)

- Australian Signals Directorate / ACSC — *Annual Cyber Threat Report* and co-sealed advisories.
- U.S. Department of Justice — cybercrime indictments and press releases (primary attribution records).
- OFAC / DFAT — cyber sanctions designations.
- Chainalysis and comparable blockchain-analysis firms — annual crypto-crime reporting.
- Academic and institutional work on the cybercrime economy and state cyber operations
  (e.g. Rid, *Active Measures*; ransomware task-force reports).

## Series metadata

| Field | Value |
|---|---|
| Series Code | EXT-CCI |
| Series Title | Adversary Counter-Intelligence — The Cybercrime & State-Cyber Ecosystem |
| Module Type | Extension series (elective; **not** credit-bearing) |
| Credit Points | 0 CP — outside the degree structure |
| Status | Draft (index only; modules to follow) |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Australian Context | Autonomous Sanctions Act 2011; Cyber Security Act 2024; ASD/ACSC reporting; AUSTRAC; Australian law-enforcement actions |
| Licence | CC BY 4.0 |
