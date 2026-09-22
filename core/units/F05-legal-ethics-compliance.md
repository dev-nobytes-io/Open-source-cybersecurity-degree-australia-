# F05: Legal, Ethics & Australian Compliance

> **Status:** Draft
> **Version:** v0.2
> **Last Reviewed:** 2026-09-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Cybersecurity is practised within a legal and ethical framework, and a
practitioner who ignores it can cause serious harm — to others and to their own
career. This unit gives learners working knowledge of the Australian legislation
that governs computer access, interception and monitoring, privacy, data
breaches, ransomware payments, and critical infrastructure, alongside the
professional ethics and authorisation boundaries that separate legitimate
security work from criminal conduct. It is the unit that makes the rest of the
degree safe to practise: the same `nmap` command is professional in one context
and an offence in another, and the difference is entitlement, law, and a written
record of both.

The unit is explicitly Australian. It covers the **computer offences in Part
10.7 of the Criminal Code** (Schedule 1 to the *Criminal Code Act 1995* (Cth)),
the concurrent State and Territory computer offences, the *Telecommunications
(Interception and Access) Act 1979* (Cth) and surveillance-devices law, the
*Privacy Act 1988* and Australian Privacy Principles, the Notifiable Data
Breaches scheme, the ransomware-payment reporting duty in the *Cyber Security
Act 2024* (Cth), and the *Security of Critical Infrastructure Act 2018* (SOCI),
together with the roles of regulators such as the OAIC, ACSC/ASD, and the AFP.
F05 is a prerequisite for every offensive or investigative unit in the degree,
including OC06 (Offensive Security Concepts), the CTE major, and the DFIR major,
and it supplies the lawful basis that F06, DF04 and TH04 rely on whenever a
learner captures packets.

---

## Prerequisites

- F01 — Networking Fundamentals (for technical context)

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Describe** the key Australian laws governing computer access, interception,
   privacy, data breaches, and critical infrastructure, and explain what conduct
   each governs.
2. **Explain** the Australian Privacy Principles and the obligations of the
   Notifiable Data Breaches scheme.
3. **Identify** when an activity requires explicit authorisation and describe the
   legal consequences of acting without it.
4. **Demonstrate** the construction of a basic rules-of-engagement /
   authorisation document for a security activity.
5. **Explain** professional ethics codes and how they guide conduct where the law
   is silent or ambiguous.
6. **Describe** the roles and powers of the relevant Australian regulators and
   how to interact with them.
7. **Explain** what makes the possession, production and supply of security
   tooling, exploit code and sample data lawful or unlawful under the
   intent-based computer offences.
8. **Identify** the specific lawful basis, if any, for a proposed packet-capture
   or monitoring activity, and state which provision supplies it.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of the
Australian legal, regulatory, and ethical environment for cybersecurity,
including the difference between an amending Act and the operative instrument it
amends — a distinction that determines whether a citation is current law.

**Skills (AQF 7.2):** Students develop cognitive and communication skills by
analysing scenarios for legal and ethical issues, identifying the precise
provision that authorises or prohibits an activity, and drafting authorisation
documentation.

**Application (AQF 7.3):** Students apply this knowledge to realistic
professional scenarios, producing the authorisation, monitoring-basis and
breach-response artefacts an Australian practitioner is expected to handle.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Legal Advisor | OV-LGA-001 | T0098 | Develop and review policies/agreements ensuring legal and regulatory compliance | Lab 1 — Drafting Rules of Engagement; Lab 3 — Lawful Basis for Capture |
| NIST NICE DCWF | 2023 | Privacy Officer/Privacy Compliance Manager | OV-LGA-002 | T0863 | Ensure organisational compliance with privacy and data-breach obligations | Lab 2 — Notifiable Data Breach Tabletop |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Information governance | IRMG | Level 3 | Throughout |
| Personal data protection | PEDP | Level 3 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Governance | Legal & Regulatory | Foundational | Lab 1, Lab 2, Lab 3 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F05-K01 | Knowledge of the Criminal Code (Cth) Part 10.7 computer offences and the entitlement-based concept of "unauthorised" | Topic 1; Lab 1 |
| Knowledge | F05-K02 | Knowledge of the Privacy Act 1988 and the Australian Privacy Principles | Topic 5 |
| Knowledge | F05-K03 | Knowledge of the Notifiable Data Breaches scheme, SOCI Act obligations, and the Cyber Security Act 2024 ransomware-payment report | Topic 6; Topic 7 |
| Knowledge | F05-K04 | Knowledge of Australian regulators (OAIC, ACSC/ASD, AFP, APRA) and their roles | Topic 9 |
| Knowledge | F05-K05 | Knowledge of the intent-based tooling offences (ss 478.3 and 478.4) and what makes holding and publishing tooling lawful | Topic 2; Summative |
| Knowledge | F05-K06 | Knowledge of the TIA Act prohibition on interception and of surveillance-devices and workplace-surveillance law | Topic 4; Lab 3 |
| Skill | F05-S01 | Skill in constructing a rules-of-engagement / authorisation document | Lab 1 |
| Skill | F05-S02 | Skill in performing an NDB eligible-breach assessment and notification | Lab 2 |
| Skill | F05-S03 | Skill in stating the specific lawful basis for a capture or monitoring activity | Lab 3 |
| Ability | F05-A01 | Ability to determine when an activity requires explicit authorisation | Lab 1; Formative |
| Ability | F05-A02 | Ability to apply professional ethics where the law is silent or ambiguous | Topic 8; Summative |
| Ability | F05-A03 | Ability to reason about concurrent Commonwealth and State/Territory liability for the same conduct | Topic 3; Formative |
| Task | T0098 | Develop and review policies/agreements ensuring legal and regulatory compliance | Lab 1; Lab 3 |
| Task | T0863 | Ensure organisational compliance with privacy and data-breach obligations | Lab 2 |

---

## Topics

### Topic 1: Computer Crime Law — Criminal Code (Cth) Part 10.7

**Start with the citation, because most secondary material gets it wrong.** The
*Cybercrime Act 2001* (Cth) is an **amending Act** — Act No 161 of 2001, assented
1 October 2001, long title "An Act to amend the law relating to computer
offences, and for other purposes". Schedule 1 repealed the old computer
offences in Part VIA of the *Crimes Act 1914* (Cth), and Schedule 1
**inserted Part 10.7 "Computer offences" into the Criminal Code**, which is
Schedule 1 to the *Criminal Code Act 1995* (Cth). Those provisions commenced on
21 December 2001. The Cybercrime Act also inserted the assistance-order power
now in s 3LA of the *Crimes Act 1914* (Cth).

Having done its work, the Cybercrime Act 2001 is **spent as a source of operative
law**. A practitioner, a contract, or a rules-of-engagement document must cite
the Criminal Code — for example "*Criminal Code Act 1995* (Cth) sch 1 s 477.2",
or "*Criminal Code* (Cth) s 477.2" — and may cite the Cybercrime Act only
historically ("Part 10.7 was inserted by the *Cybercrime Act 2001* (Cth) sch 1
item 4"). Citing the amending Act as the operative offence is the legal-writing
equivalent of citing a changelog instead of the code.

**Division 476 — the machinery.** Section 476.1 defines *access to data*
(display or output, copying or moving, executing a program), *modification*
(alteration, removal or addition), *impairment of electronic communication*
(including impairment on a link or network used by the computer, but expressly
**not** mere interception), and *electronic communication*; s 476.1(2) limits all
three to results caused, directly or indirectly, by the execution of a function
of a computer. Merely reading a page is "access"; running a program is "access".
The carve-out of interception from "impairment" is the seam between Part 10.7
and the TIA Act (Topic 4).

**Section 476.2 is the real home of "authorisation".** Conduct is unauthorised
where the person **"is not entitled to cause that access, modification or
impairment"** (s 476.2(1)). Three consequences matter for this degree:

- *Entitlement, not belief.* The test is objective entitlement. Being told
  verbally that "it's fine" is evidence about entitlement, not a substitute for
  it, and the person giving permission must actually have the right to give it —
  which is why cloud tenancies, shared hosting, managed SaaS and
  landlord/ISP-supplied equipment need their own authorisation.
- *Ulterior purpose does not destroy entitlement* (s 476.2(2)). A penetration
  tester with a signed scope does not become "unauthorised" merely because they
  intend to find flaws. Equally, a tester who steps outside scope is simply not
  entitled for that step.
- *Substantial contribution is enough* (s 476.2(3)). You need not be the only
  cause.

Section 476.2(4) lists the situations where a person **is** entitled: acting
under a warrant, under an emergency authorisation under Part 3 of the
*Surveillance Devices Act 2004* (Cth), under a tracking-device authorisation
under s 39 of that Act, or under or in compliance with a technical assistance
request, notice or capability notice.

**Division 477 — the serious offences.**

| Provision | Offence | Fault element | Maximum |
|---|---|---|---|
| s 477.1 | Unauthorised access, modification or impairment **with intent to commit a serious offence** | Knowledge of lack of authorisation + intent to commit/facilitate a serious offence | The penalty applicable to the intended serious offence (s 477.1(6)) — a "serious offence" is one punishable by life or 5+ years (s 477.1(9)) |
| s 477.2 | Unauthorised modification of data **causing, or risking, impairment** | Knowledge of lack of authorisation + **recklessness** as to impairment | 10 years |
| s 477.3 | Unauthorised **impairment of electronic communication** to or from a computer | Knowledge of lack of authorisation | 10 years |

Three teaching points. First, the s 477.1 ceiling is **borrowed** from the
intended offence, so "just hacking" is not the worst case: intent to defraud,
extort or steal can carry life. Impossibility is no defence (s 477.1(7)) and
there is no offence of attempting s 477.1 (s 477.1(8)). Second, s 477.2 runs on
**recklessness**, and there need be no actual impairment (s 477.2(3)) — a student
who modifies data on a system they were not entitled to touch is exposed even if
nothing broke. Third, s 477.3 is the denial-of-service and network-disruption
section, and it has only two elements: cause unauthorised impairment, know it is
unauthorised. An unauthorised stress test, or an ARP-spoofing or jamming lab that
escapes onto a shared network, sits squarely inside it.

**Division 478 — the everyday offences.** Section 478.1 (2 years) covers
unauthorised access to, or modification of, **restricted data** — data to which
access is restricted by an access control system associated with a function of
the computer. Defeating *any* access control (a password, an API key, an
authorisation check) is enough; there is no damage requirement. Credential
re-use, poking at an insecure direct object reference on a live site, and logging
into a friend's account are all here. Section 478.2 (2 years) covers unauthorised
impairment of data held on a disk, credit card or other storage device — the
offline and physical-media case. Sections 478.3 and 478.4 are the tooling
offences and have their own topic.

Sections 476.6 and 476.7 create narrow immunities for ASIS/ASD/AGO and defence
officials; they are named here only so students do not mistake them for a general
"security professional" defence.

**Key concepts:**
- The Cybercrime Act 2001 as amending Act; the Criminal Code as operative law
- Unauthorised = "not entitled" (s 476.2), and who can validly authorise
- The Division 477/478 offence set, fault elements and maximum penalties

**Australian context:** This entire topic is Australian law; it is the legal
spine of the degree's ethics requirements.

---

### Topic 2: Tooling, Exploits and Intent — ss 478.3 and 478.4

This degree asks students to hold and run offensive tooling, keep malware
samples, and publish write-ups. Two sections govern that, and both turn on
**intention**, not on the nature of the tool.

**Section 478.3 — possession or control of data with intent** (maximum 3 years).
The elements are: the person has possession or control of data, **and** has it
with the intention that the data be used, by them or another, in committing or
facilitating an offence **against Division 477**. It is not a possession-per-se
offence and not a dual-use-tool offence. There is no reverse onus and no
presumption arising from the nature of the tool — the prosecution must prove the
intention beyond reasonable doubt. Holding Metasploit, exploit proofs of concept,
malware samples, wordlists, cracked hashes or a leaked credential dump is lawful
under this section where the purpose is study, research, defence or authorised
testing. Note the scope: an intention to use data to commit a *s 478.1* offence
is **not** within s 478.3, because s 478.3 refers only to Division 477.
"Possession or control" is defined broadly (s 478.3(4)) and reaches data held on
a device in someone else's possession, inside or outside Australia — so an
overseas VPS you control is your possession.

**Section 478.4 — producing, supplying or obtaining data with intent** (maximum
3 years). Same structure: produce, supply or obtain data, with the intention that
it be used in committing or facilitating a Division 477 offence. Publishing an
exploit, a working payload, a custom command-and-control tool or a phishing kit
to a public repository is "producing" and "supplying" data. It is an offence only
if done with that intention. **Intention, not foreseeability**, is the test, and
recklessness as to third-party misuse is not sufficient — genuine defensive or
educational publication (coordinated disclosure after a fix, CTF write-ups,
detection rules, defensive tooling) falls outside the section even if someone
later misuses it.

Because intention can be **inferred from surrounding conduct**, the practical
discipline is to make purpose evident and contemporaneous:

- keep signed authorisation and scope documents for every engagement;
- maintain a lab charter and a dated research log;
- frame published work defensively, with a disclosure timeline;
- redact live targets, real credentials and customer data;
- avoid ready-to-run weaponisation against identifiable third-party systems;
- state the intended use in the repository's README and licence.

Exposure is not limited to s 478.4: supplying a tool to someone who then offends
can also raise complicity, incitement and conspiracy principles in Part 2.4 of
the Criminal Code. Those provisions were **not read** for this draft and are
flagged in the Verification status table.

**Key concepts:**
- Possession and supply offences are intent offences, not tool bans
- Evidence of purpose is the control that keeps a security portfolio lawful
- Division 477 is the reference point; s 478.1 intentions fall outside s 478.3

**Australian context:** Directly governs what an Australian student may hold in a
home lab and publish in a portfolio.

---

### Topic 3: Jurisdiction — Concurrent Commonwealth and State/Territory Offences

**The obsolete rule.** As enacted in 2001, the Division 477 and 478 offences each
carried an express jurisdictional element requiring a Commonwealth connection —
conduct by means of a carriage service, or involving a "Commonwealth computer",
or data held on behalf of the Commonwealth. That is the source of the widely
taught (and now wrong) rule that Commonwealth computer offences only bite if you
"used the internet", and that a purely local attack is a State matter.

**The current rule.** Schedule 3 of the *Cybercrime Legislation Amendment Act
2012* (Cth) (Act No 120, 2012) **repealed every one of those elements** — the
definition of "Commonwealth computer" in s 476.1(1), and the jurisdictional
paragraphs and subsections in ss 477.1, 477.2, 477.3, 478.1 and 478.2. Schedule 3
commenced on **1 March 2013**, when the Council of Europe Convention on
Cybercrime came into force for Australia, and applies to acts and omissions from
that commencement. Since then:

1. The Division 477 and 478 offences are **general computer offences**. There is
   no carriage-service, Commonwealth-computer or Commonwealth-data element.
2. The only geographic limit is **s 476.3**, which applies s 15.1 of the Criminal
   Code — *extended geographical jurisdiction, category A*: conduct wholly or
   partly in Australia (or on an Australian aircraft or ship); or conduct wholly
   outside Australia with a result wholly or partly in Australia; or conduct
   wholly outside Australia by an Australian citizen or an
   Australian-incorporated body corporate; plus an ancillary-offence limb.
   Section 15.1(2) provides a narrow defence for a primary offence committed
   wholly in a foreign country by a non-citizen where the conduct is not an
   offence in that country.
3. State and Territory computer offences apply **concurrently, not residually**.
   Section 476.4(1) expressly preserves them. One act can breach both Part 10.7
   and a State offence.

**So the modern distinction is prosecutorial, not jurisdictional.** Both bodies
of law reach the same conduct; what varies is who investigates and who
prosecutes. In practice the AFP and CDPP take matters with a Commonwealth
interest — Commonwealth systems, critical infrastructure, transnational or
organised offending, large-scale fraud — and State police and State DPPs take
local matters under State law. Teach students "both apply; who charges you is a
policy and resourcing question", never "Commonwealth law only applies if you used
the internet".

**Applied to the degree's own scenarios.** Attacking a neighbour's machine over
their Wi-Fi, or breaking out of your home lab onto a housemate's device, is now
within Part 10.7 — no carriage service is needed, and a State offence is likely
to be available as well. Attacking **your own** home lab is normally not an
offence at all, but the reason is **entitlement under s 476.2(1)**, not
jurisdiction. The caveat is any device you do not solely control: a landlord's
router, ISP-supplied customer premises equipment, a shared or family machine, a
cloud tenancy, or a licensed appliance whose terms restrict testing.

**Jurisdiction table — where the computer offences live.**

| Jurisdiction | Instrument and location | Notes |
|---|---|---|
| Commonwealth | *Criminal Code Act 1995* (Cth) sch 1, Part 10.7 (Divs 476, 477, 478) | General offences since 1 March 2013; s 476.3 applies s 15.1 category A; s 476.4 preserves State/Territory law |
| Victoria | *Crimes Act 1958* (Vic) Part I Div 3 subdiv (6), ss 247A–247I | Model Criminal Code shape; 247B carries the serious offence's own maximum; 247C and 247D level 5 (10 years); 247E and 247F 3 years; 247G and 247H level 7 (2 years, summary); 247I extra-territorial operation |
| Queensland | *Criminal Code* (Qld) ch 37 s 408E | Heading is now **"Misuse of restricted computer"** (renamed; amending Act number unverified); tiers: 3 years; 5 years where detriment/benefit intended or caused; 10 years where value exceeds $5,000 or an indictable offence is intended; s 408E(4) defence of lawful authority, justification or excuse |
| Western Australia | *The Criminal Code* (WA) s 440A "Unlawful use of computer" | Tiers: 10 years (benefit/detriment over $5,000), 5 years (benefit/detriment intended or caused), 2 years otherwise. Note s 440A(2)(b): WA expressly criminalises an **authorised** user who acts outside their authorisation |
| New South Wales | *Crimes Act 1900* (NSW) Part 6 — “Computer offences” (ss 308–308I) | Model-Criminal-Code style regime inserted by the *Crimes Amendment (Computer Offences) Act 2001* (NSW). **Section numbers and penalties are unverified for this draft** — see Verification status; check legislation.nsw.gov.au before teaching them |
| South Australia | A summary computer-misuse offence exists in SA statute | **Instrument, section number and penalty unverified** — see Verification status; check legislation.sa.gov.au before teaching them |
| Tasmania | *Criminal Code* (Tas) ss 257A–257F | Older, pre-Model-Criminal-Code regime (inserted 1990): computer-related fraud, damaging computer data, unauthorized access, insertion of false information, and an extra-territorial provision requiring a real and substantial link. **Maximum penalties unverified** |
| Australian Capital Territory | *Criminal Code 2002* (ACT) ch 4 Part 4.2, ss 412–421 | Mirrors the Part 10.7 structure (definitions, meaning of unauthorised, intent-to-commit, impairment, possession, production/supply, restricted data, storage-device impairment). **Individual maximum penalties unverified** |
| Northern Territory | *Criminal Code* (NT) Part VIIA Div 1, ss 276–276F | Structurally different: 276B unlawful access with intent (10 years) **and 276B(2) unlawful *use* of unlawfully accessed data (10 years), whether or not the user obtained it** — important for students handling leaked datasets; 276C and 276D 10 years; 276E unlawful use of access time 3 years. **Section range and all maximum penalties unverified** |

Victoria, the ACT and the NSW Part 6 regime were modelled on the same Model
Criminal Code chapter that Part 10.7 implements, so their elements mirror the
Commonwealth closely. Queensland, Western Australia, Tasmania and the Northern
Territory use older or structurally different offences, and the differences are
not cosmetic — WA's exceeding-authorisation limb and the NT's use-of-data offence
have no Commonwealth equivalent.

**Key concepts:**
- The 2012 repeal of the Commonwealth nexus and what replaced it (s 476.3)
- Concurrent liability under s 476.4, and the prosecutorial (not jurisdictional) split
- Reading a State offence alongside the Commonwealth one for the same conduct

**Australian context:** The whole topic is the Australian federal division of
criminal jurisdiction over computer conduct.

---

### Topic 4: Interception, Surveillance and Monitoring

Every unit in this degree that captures packets — F06, DF04, TH04 — depends on
this topic. The **Telecommunications (Interception and Access) Act 1979** (Cth)
is often described in course material as the Act that "allows" monitoring. It is
the opposite: **it is a prohibition with narrow, closed exceptions.**

**The prohibition.** Section 7(1): a person shall not intercept, authorise,
suffer or permit another person to intercept, **or do any act or thing that will
enable** interception of a communication passing over a telecommunications
system. Limb (c) matters for engineers — building or deploying capture capability
is itself caught. Contravening s 7(1) (or s 63, on dealing with intercepted
information) is an indictable offence punishable by up to **2 years**
imprisonment (s 105), reducible to 6 months in a court of summary jurisdiction on
strict conditions; s 105(5) applies category A extended geographical
jurisdiction, and s 107A provides a civil remedy.

**Two definitions decide most lab questions.**

- *"Interception"* (s 6(1)) is listening to or recording a communication **in its
  passage** over a telecommunications system **without the knowledge of the
  person making the communication**. Two escape hatches live here: a saved
  `.pcap`, or data at rest, is not in passage; and capture done *with the
  knowledge* of the person making the communication is not interception at all.
  The statutory word is **knowledge**, not consent.
- *"Telecommunications system"* (s 5(1)) is a telecommunications network within
  Australia, **and includes equipment, a line or other facility connected to such
  a network and within Australia**. A genuinely air-gapped or isolated lab
  segment is arguably outside the Act entirely — but the moment a lab VM has a
  bridged uplink or an internet route, the connected-equipment limb probably
  brings it back in. **Isolation is a legal control, not just a safety control.**

**What actually permits capture.** A practitioner should always be able to name
which of these applies:

1. **Not a communication in passage** — offline pcap analysis, data at rest, or
   a genuinely isolated lab.
2. **Knowledge of the maker** — your own generated traffic, or traffic made with
   notice.
3. **s 7(2)(aaa) network protection duties** — the key workplace basis. It
   requires that the person be **authorised in writing** by a responsible person
   for the computer network to engage in network protection duties, and that
   interception be **reasonably necessary** to perform those duties effectively
   (s 7(2A) directs a court to matters specified in the regulations). **Critical
   limit: s 7(3) excludes voice communications in the form of speech**, including
   recorded or synthetic voice — so a full-packet-capture programme cannot be
   used to capture VoIP speech under this paragraph.
4. **Carrier and installation/maintenance duties** — s 7(2)(a) and s 7(2)(aa),
   where reasonably necessary to perform those duties.
5. **A warrant** — s 7(2)(b) and the related Part 2-2 and Part 2-5 regimes, plus
   narrow emergency and consent provisions available only to the AFP and State
   police forces.

None of these is available to a student acting on their own initiative against
someone else's network, and **"my employer told me to" is not an answer** — it
must be a written s 7(2)(aaa) authorisation from a responsible person for that
network.

**Stored communications.** Chapter 3 separately prohibits accessing a stored
communication without the knowledge of either the intended recipient or the
sender, with a penalty of 2 years imprisonment or 120 penalty units, or both.
Section 108(1A) deems knowledge where written notice of the intention to access
is given. The Act does not prohibit accessing communications that are no longer
passing over a telecommunications system from the intended recipient, or from a
device in the intended recipient's possession — which is why mailbox and
message-store forensics is workable at all (DF04).

**Surveillance devices.** The **Surveillance Devices Act 2004 (Cth)** is an
**authorising** statute, not a source of permission for private parties. Its long
title speaks of the *powers* of Commonwealth law enforcement agencies, and s 3
lists warrant types (surveillance device, computer access, data disruption,
network activity), emergency authorisations and tracking-device authorisations,
together with use, storage, destruction and reporting restrictions. Section 4(1)
says that, absent express provision, the Act is not intended to affect other laws
prohibiting or regulating surveillance devices, access to data, or disruption of
data. **It confers nothing on a student, a consultant or a corporate security
team.** The link back to Part 10.7 is s 476.2(4): access under a Part 3 emergency
authorisation or a s 39 tracking-device authorisation is "entitled".

**The prohibitions on private surveillance are State and Territory law.** Using
Victoria as the verified example, the *Surveillance Devices Act 1999* (Vic)
prohibits knowingly installing, using or maintaining a **listening device** to
record a private conversation you are not party to without the express or implied
consent of each party (s 6; natural person level 7 imprisonment, 2 years maximum,
or a level 7 fine of 240 penalty units, or both; 1200 penalty units for a body
corporate), with parallel prohibitions for **optical surveillance devices** (s 7)
and **tracking devices** (s 8). Counterintuitively, **s 9 — data surveillance
devices — is directed at law enforcement officers, not private persons**, so in
Victoria a private keylogger or endpoint monitor is constrained by the computer
offences and the TIA Act rather than by s 9. Part 2A (ss 9A–9B) separately bans
employer optical and listening devices in prescribed private areas of a workplace
(toilets, washrooms, change rooms, lactation rooms).

Other jurisdictions differ, and **workplace surveillance** is separately
regulated in some of them — New South Wales, in particular, has both a
surveillance devices Act and a dedicated workplace surveillance Act with notice
and policy requirements. Neither was verified for this draft; see Verification
status, and confirm the local regime before designing any monitoring programme.

Finally, satisfying the TIA Act is not the end of the analysis: State
surveillance-devices law and the *Privacy Act 1988* (APP 3 collection, APP 5
notification) may independently bite on the same capture.

**Key concepts:**
- The TIA Act as a prohibition with closed exceptions; s 7(1) limb (c)
- "In passage" and "knowledge of the maker" as the two definitional hinges
- The written s 7(2)(aaa) network-protection authorisation, and the voice carve-out
- The Surveillance Devices Act 2004 as a law-enforcement power, not a permission

**Australian context:** Australian interception and surveillance law, applied
directly to the degree's own capture labs.

---

### Topic 5: Privacy — The Privacy Act and the APPs

The *Privacy Act 1988* (Cth) and the 13 Australian Privacy Principles (APPs)
govern how organisations collect, use, store, and disclose personal information.
This topic covers what counts as personal and sensitive information, the key
APPs most relevant to security (APP 3 collection, APP 5 notification, APP 11
security of personal information, APP 12 access and APP 13 correction, APP 8
cross-border disclosure), and who the Act applies to.

Reform is live. The *Privacy and Other Legislation Amendment Act 2024* (Cth)
(Act No 128, 2024) is reported to have introduced a statutory tort of serious
invasion of privacy alongside its amendments to the Criminal Code; the tort was
**not verified against the primary text** for this draft and is flagged in the
Verification status table. Students should check the current consolidated
Privacy Act before relying on it.

**Key concepts:**
- Personal vs sensitive information
- The 13 Australian Privacy Principles (with a security focus on APP 11, and on
  APP 3 and APP 5 for monitoring and capture)
- Who is covered, and current reform directions

**Australian context:** The Privacy Act and APPs are the core Australian data
protection regime.

---

### Topic 6: Data Breaches — The NDB Scheme

The Notifiable Data Breaches (NDB) scheme requires organisations covered by the
Privacy Act to notify affected individuals and the OAIC of eligible data breaches
likely to result in serious harm. This topic covers what triggers notification,
the assessment timeline, the content of a notification, and the practitioner's
role in breach response. It links directly to OC04 (Incident Response).

Students should hold the NDB clock apart from the two other clocks taught in
Topic 7: NDB assessment is measured in **30 days**, a critical SOCI incident in
**12 hours**, and a ransomware payment report in **72 hours** from the payment.

**Key concepts:**
- What makes a breach "eligible" and "likely to result in serious harm"
- The 30-day assessment obligation and notification content
- The security practitioner's role in supporting NDB compliance

**Australian context:** The NDB scheme is administered by the OAIC and is central
to Australian incident response.

---

### Topic 7: Critical Infrastructure and Ransomware Payment Reporting

**SOCI.** The *Security of Critical Infrastructure Act 2018* (Cth), as amended,
imposes obligations on responsible entities for critical infrastructure assets —
including risk management programs and mandatory cyber incident reporting. The
Part 2B timeframes are the ones to memorise: a **critical** cyber security
incident having a significant impact on the availability of the asset must be
reported as soon as practicable and **within 12 hours** (s 30BC; civil penalty 50
penalty units; an oral report must be reduced to an approved-form written record
given within 84 hours), and **any other** cyber security incident having or
likely to have a relevant impact must be reported **within 72 hours** (and,
where that report is given orally, a written record must be given within
48 hours) (s 30BD;
civil penalty 50 penalty units).

The *Security of Critical Infrastructure and Other Legislation Amendment
(Enhanced Response and Prevention) Act 2024* (Cth) (Act No 100, 2024) reshaped
several things students will meet in practice:

- **Data storage systems are in scope.** Section 9(7) treats a data storage
  system as part of the critical infrastructure asset where the responsible
  entity owns or operates it, it is used in connection with the asset,
  **business critical data** is stored or processed in or by it, and a hazard
  affecting it could materially risk a relevant impact on the asset. Part 2
  obligations, the Part 2A risk management program and Part 2B notification all
  have to account for it.
- **Telecommunications security moved into SOCI.** New Part 2D (enhanced
  security regulation for critical telecommunications assets) replaces the former
  *Telecommunications Act 1997* Part 14 framework.
- **Consequence management broadened.** Part 3A is now headed "Responding to
  serious incidents" — all-hazards, not cyber-only.
- Section 5A reformulates "protected information" on a harm basis, and Part 2AA
  adds reporting obligations for certain assets not covered by a risk management
  program.

**Ransomware payment reporting — Cyber Security Act 2024 (Cth).** Act No 98 of
2024 creates a duty that attaches to **the payment, not the incident**. An entity
is a *reporting business entity* (s 26(2)) if, when the payment is made, it
carries on business in Australia with previous-financial-year turnover above the
threshold (and is not a Commonwealth or State body, and is not a responsible
entity for a critical infrastructure asset), **or** it is a responsible entity
for a critical infrastructure asset to which Part 2B of the SOCI Act applies. The
threshold is **$3 million**, set by s 6(1) of the *Cyber Security (Ransomware
Payment Reporting) Rules 2025*, with a pro-rata formula for part-year businesses.

The trigger (s 26(1)) is a cyber security incident with a direct or indirect
impact on the entity, a demand by an extorting entity made in order to benefit
from the incident, and the provision of a payment or benefit directly related to
that demand — by the entity, or by another on its behalf where the entity is
aware of it. The report must be given to the designated Commonwealth body
**within 72 hours** of making the payment or becoming aware it was made (s
27(1)), covering the payer's details, the incident and its impact, the demand,
the payment, and communications with the extorting entity (s 27(2)). The sanction
is a **civil penalty of 60 penalty units** (s 27(5)) — not a criminal offence.

The architecture worth teaching is the **limited-use** protection: s 28
(good-faith immunity from damages), s 29 and s 30 (restrictions on use and
secondary disclosure by the receiving body), s 31 (legal professional privilege
preserved) and s 32 (restricted admissibility against the reporting entity). The
design intent is that an incident response team can report without
self-incriminating. Note also that none of this legalises or prohibits the
payment itself — sanctions law, proceeds-of-crime law and directors' duties are
separate questions this unit does not cover.

The commencement date commonly cited for the reporting duty, and the regulator's
education-first posture through 2025, are **secondary-source only**; see
Verification status.

**Key concepts:**
- Covered sectors, responsible entities, and data storage systems in scope
- The 12-hour and 72-hour SOCI reporting clocks and the 84-hour and 48-hour
  written records
- The ransomware-payment report: who, what trigger, 72 hours, civil penalty,
  and the limited-use protections

**Australian context:** SOCI and the Cyber Security Act 2024 are distinctively
Australian regimes reshaping critical-infrastructure and incident obligations.

---

### Topic 8: Professional Ethics, Disclosure and the Doxxing Offences

Where the law is silent, ethics guides conduct. This topic covers professional
codes (e.g. AISA's code of conduct, (ISC)² and broader practitioner ethics),
responsible disclosure of vulnerabilities, conflicts of interest, and the
handling of sensitive data discovered during work. It develops the judgement to
act well in grey areas that legislation does not fully address.

It also covers a place where the law is **not** silent and students routinely
assume it is. The *Privacy and Other Legislation Amendment Act 2024* (Cth)
inserted two **doxxing offences** into the Criminal Code:

- **s 474.17C** — using a carriage service to make available, publish or
  otherwise distribute **personal data** of one or more individuals in a way that
  reasonable persons would regard as, in all the circumstances, menacing or
  harassing towards those individuals. Maximum **6 years**. Section 474.17C(2)
  defines personal data as information enabling an individual to be identified,
  contacted or located, expressly including name, photograph or other image,
  telephone number, email address, online account, residential address, work or
  business address, place of education and place of worship.
- **s 474.17D** — the aggravated group form, where the person acts in whole or in
  part because of a belief that the group is distinguished by race, religion,
  sex, sexual orientation, gender identity, intersex status, disability,
  nationality or national or ethnic origin. Maximum **7 years**. It is immaterial
  whether the group is actually so distinguished (s 474.17D(3)).

These sections sit in Part 10.6, not Part 10.7, so — unlike the Division 477 and
478 offences — they **do** retain a carriage-service element. Their direct effect
on this degree is on OSINT exercises, reconnaissance reports and threat-actor
attribution write-ups: aggregating a real individual's name, employer, photograph
and address into a published artefact can be the conduct element, with the
objective "menacing or harassing" test as the qualifier. Teach OSINT deliverables
to use synthetic targets, consenting subjects, or redaction, and to stay
organisation-level rather than individual-level wherever the learning objective
allows.

**Key concepts:**
- Professional codes of conduct and their common themes
- Responsible/coordinated vulnerability disclosure, read together with s 478.4
- Handling incidental discovery of sensitive or illegal material
- The doxxing offences as a hard limit on OSINT and attribution deliverables

**Australian context:** AISA (Australian Information Security Association) is
referenced as the leading Australian professional body; ss 474.17C and 474.17D
are Commonwealth criminal law.

---

### Topic 9: Regulators and Authorisation in Practice

This topic brings law and ethics into daily practice. It covers the roles of the
OAIC, ACSC/ASD, AFP, and sector regulators (e.g. APRA), how and when to engage
them, and — crucially — how authorisation works in real engagements: scope, rules
of engagement, written permission, and the consequences of scope creep. It is the
practical bridge to the offensive and investigative units.

It also covers the powers that run the other way. Section 3LA of the *Crimes Act
1914* (Cth) — inserted by Schedule 2 of the Cybercrime Act 2001 — lets an
executing officer apply to a magistrate for an **assistance order** requiring a
specified person to provide information or assistance reasonable and necessary to
access, copy or convert data held in or accessible from a computer on warrant
premises. The answer to "can they compel my password?" is therefore **yes, by
order of a magistrate**. The penalty for non-compliance has risen from 6 months
in 2001 to **5 years or 300 penalty units** (s 3LA(5)), and **10 years or 600
penalty units** where the warrant relates to a serious offence or a serious
terrorism offence (s 3LA(6)). That escalation is itself the lesson in currency:
a practitioner who quotes the 2001 figure is out by an order of magnitude.

**Key concepts:**
- Roles and powers of key Australian regulators
- Building a defensible authorisation: scope, RoE, written approval
- Scope creep and its legal consequences
- Assistance orders under s 3LA and the practitioner's obligations

**Australian context:** Directly covers the Australian regulator landscape.

---

## Labs & Exercises

### Lab 1: Drafting Rules of Engagement

**Objective:** Draft a rules-of-engagement / authorisation document for a
hypothetical internal security assessment, demonstrating how authorisation is
established lawfully and cited correctly.

**Prerequisites:**
- Topics 1, 2, 8, and 9

**Environment:**
- Operating System: any (this is a documentation lab)
- Tools: a word processor or markdown editor (free/open-source, e.g. LibreOffice
  or any text editor)
- Minimum hardware: trivial (well under the 8 GB RAM / 4 vCPU / 50 GB ceiling)

**Instructions:**

1. Take a scenario: an organisation asks you to assess the security of its
   internal web portal.
2. Draft an authorisation/RoE document that includes: parties and signatories,
   in-scope and explicitly out-of-scope systems, permitted techniques, testing
   window, data-handling rules, and an emergency-stop contact.
3. Add a clause making clear that activity outside scope is unauthorised access,
   citing the operative instrument — the computer offences in **Part 10.7 of the
   Criminal Code (Schedule 1 to the *Criminal Code Act 1995* (Cth))**, and in
   particular the meaning of "unauthorised" in s 476.2 (conduct the person is
   *not entitled* to cause). Do **not** cite the *Cybercrime Act 2001* (Cth) as
   the operative offence: it is the amending Act that inserted Part 10.7, and
   citing it as operative law is a defect a reviewing lawyer will mark. If you
   mention it at all, mention it historically.
4. Add a clause confirming that the signatory has the authority to grant
   entitlement over every in-scope system, and identify any system where a third
   party (cloud provider, managed service provider, landlord, upstream ISP) must
   also authorise.
5. Add a data-handling clause referencing Privacy Act / APP 11 obligations for
   any personal information encountered.
6. Add a monitoring clause stating whether any traffic capture will occur and,
   if so, the basis relied on under the TIA Act (cross-reference Lab 3).
7. Identify three ways scope creep could occur and how the document prevents
   each.

**Expected Output:**

A complete, signable RoE document with clear scope boundaries, correct statutory
citations, an entitlement/authority clause, and data-handling rules. Learners can
explain why each clause exists and which law or principle it protects against
breaching, and can explain why the Criminal Code — not the Cybercrime Act 2001 —
is the instrument named.

**Reflection Questions:**

1. Why is written, scoped authorisation the single most important protection for
   a security professional under Part 10.7 of the Criminal Code — and what does
   s 476.2(2) tell you about a tester's *purpose*?
2. Your client's portal runs in a cloud tenancy and behind a third-party WAF. Who
   is "entitled" to authorise testing of each layer, and what happens to your
   position if one of them has not signed?
3. How would the RoE change if the assessment involved a critical-infrastructure
   asset under SOCI, including the reporting clocks in Topic 7?
4. What ethical obligations apply if you discover evidence of a real, unrelated
   crime during the assessment?

---

### Lab 2: Notifiable Data Breach Tabletop

**Objective:** Work through a simulated data breach and produce the assessment
and notification artefacts required under the NDB scheme, alongside the other
statutory clocks that may run at the same time.

**Prerequisites:**
- Topics 5, 6, 7, and 9

**Environment:**
- Operating System: any
- Tools: the OAIC NDB guidance (free, online), a document editor (free/open-source)
- Minimum hardware: trivial (well under the 8 GB RAM / 4 vCPU / 50 GB ceiling)

**Instructions:**

1. Read the provided breach scenario (e.g. a misconfigured database exposing
   customer records).
2. Assess whether the breach is "eligible" and "likely to result in serious
   harm", documenting your reasoning against OAIC criteria.
3. Draft the statement that would be provided to the OAIC and to affected
   individuals, including the required content elements.
4. Build a short timeline showing the 30-day assessment obligation and key
   decision points.
5. Overlay the other clocks that could run on the same incident: SOCI s 30BC (12
   hours, critical incident) and s 30BD (72 hours), and — if the scenario is
   extended so that the entity pays an extortion demand — the 72-hour
   ransomware-payment report under s 27(1) of the *Cyber Security Act 2024* (Cth).
   State, for each, whether the entity is actually caught by it and why.
6. Note which of the limited-use protections in ss 28–32 of the Cyber Security
   Act 2024 would apply to the ransomware report, and explain to a hypothetical
   general counsel why they reduce the risk of reporting.

**Expected Output:**

A documented eligibility assessment with reasoning, a draft OAIC/individual
notification meeting the required content, and a multi-clock compliance timeline.
Learners can justify the notify/not-notify decision against OAIC criteria and can
say which obligations attach to the **incident** and which attach to the
**payment**.

**Reflection Questions:**

1. What factors most influence whether a breach is "likely to result in serious
   harm"?
2. How do the NDB scheme, SOCI reporting and the ransomware-payment report
   interact for a critical infrastructure entity — and which one is triggered by
   something other than the incident itself?
3. How does early, well-documented incident response (OC04) make NDB compliance
   easier?

---

### Lab 3: Establishing a Lawful Basis for Capture and Monitoring

**Objective:** Produce a short "lawful basis" determination for each of several
packet-capture and monitoring scenarios, and draft the written network-protection
authorisation that the workplace scenario requires. This is the document F06,
DF04 and TH04 assume exists before a learner runs a capture.

**Prerequisites:**
- Topics 1, 3, 4, and 5
- F01 (for the network concepts)

**Environment:**
- Operating System: any (this is a documentation lab)
- Tools: a document editor (free/open-source); optionally an existing capture
  file from F01 for the offline-analysis scenario. No live capture is performed
  in this lab.
- Minimum hardware: trivial (well under the 8 GB RAM / 4 vCPU / 50 GB ceiling)

**Instructions:**

1. For each scenario below, write a short determination: (a) is there a
   communication **passing over** a telecommunications system? (b) is the capture
   **without the knowledge of the person making** the communication? (c) if the
   TIA Act is engaged, which exception applies — and name the paragraph. If no
   exception applies, say so and stop.
   - Analysing a `.pcap` file supplied by your instructor.
   - Capturing traffic you generate yourself between two VMs on a
     host-only/NAT-isolated virtual network.
   - The same lab, but the VMs are bridged to your home network with an internet
     route.
   - Capturing on a corporate network as a SOC analyst, for intrusion detection.
   - Capturing VoIP call audio on that same corporate network.
   - Capturing on a café or campus Wi-Fi network to "see what's there".
2. Draft a written authorisation under **s 7(2)(aaa)** of the TIA Act for the SOC
   scenario: identify the responsible person for the network, name the authorised
   person, define the network, state the network protection duties, and state why
   interception is reasonably necessary to perform them effectively.
3. Add an express exclusion to that authorisation reflecting **s 7(3)** (voice
   communications in the form of speech), and explain in one sentence why it must
   be there.
4. Identify, for the corporate scenario, what *else* must be satisfied beyond the
   TIA Act: the applicable State or Territory surveillance-devices law, any
   workplace-surveillance notice or policy requirement in that jurisdiction, and
   the Privacy Act APP 3 and APP 5 obligations for the personal information the
   capture will collect.
5. Write one paragraph explaining why the *Surveillance Devices Act 2004* (Cth)
   does **not** supply your authority, referring to s 4(1) of that Act.
6. Record which jurisdiction you assumed, and flag any point where you could not
   confirm the local rule — matching the honesty requirement in the Verification
   status table below.

**Expected Output:**

Six short determinations, each naming a specific provision or expressly
concluding that no basis exists; a signable s 7(2)(aaa) authorisation with a
voice-communication exclusion; and a paragraph correctly distinguishing an
authorising statute from a permission. Learners can articulate the rule in one
line: *isolation, knowledge, written authorisation, duty, or warrant — name which
one, or do not capture.*

**Reflection Questions:**

1. Bridging a lab VM to your home network changes nothing technically. Why can it
   change the legal position, and which definition does the work?
2. Your manager tells you verbally to turn on full packet capture. What exactly
   is missing, and what would you ask for in writing?
3. Why does the TIA Act carve mere interception out of "impairment of electronic
   communication" in s 476.1 of the Criminal Code, and what would go wrong if it
   did not?

---

## Assessment

### Formative Assessment: Legal Scenario Spotting

**Type:** Short-answer scenario exercise with answer key

**Description:** Students are given short vignettes (e.g. "a colleague scans a
partner's network without asking"; "a student runs an exploit against a VM that
is bridged to the household router"; "a graduate publishes a working exploit for
an unpatched product"; "an analyst mirrors a switch port to a laptop on a
verbal instruction") and must identify the law/principle at issue, name the
provision, state whether Commonwealth and State law both reach the conduct, and
say whether the conduct is lawful/ethical. Self-marked.

**Learning Outcomes Assessed:** LO1, LO3, LO5, LO7, LO8

**Feedback mechanism:** Answer key identifying the relevant law/principle, the
specific provision, and the reasoning for each vignette — including, for each
vignette, whether the answer depends on entitlement (s 476.2), on a TIA Act
exception, or on intention (ss 478.3–478.4).

---

### Summative Assessment: Compliance & Ethics Case Study

**Type:** Case-study analysis report

**Description:** Students analyse a realistic scenario in which an organisation
suffers an incident with legal, privacy, and ethical dimensions. They must (a)
identify all applicable Australian legislation and obligations, citing operative
instruments rather than amending Acts, (b) determine notification requirements
under the NDB scheme (and SOCI and the Cyber Security Act 2024 ransomware report
if applicable), (c) state the lawful basis for any monitoring or capture the
response relies on, (d) assess any ethical issues in the organisation's response,
including any publication or disclosure decisions, and (e) recommend a compliant,
ethical course of action. Deliverable: 1,500–2,000 word report.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6, LO7, LO8

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Identification of applicable law (correct operative instrument) | LO1, LO3 |
| NDB / SOCI / ransomware-payment notification analysis | LO2, LO6 |
| Lawful basis for monitoring or capture | LO8 |
| Tooling, disclosure and publication analysis | LO7 |
| Ethical analysis & recommendation | LO5 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Legal accuracy | Identifies all relevant laws/obligations correctly and cites operative instruments and provisions | Identifies most with minor gaps; citations mostly operative | Identifies some; notable omissions or cites an amending Act as operative | Misidentifies or omits key law |
| Regulatory/notification analysis | Correct, well-reasoned notification decisions across all applicable clocks | Mostly correct with small gaps | Partial or weakly reasoned | Incorrect notification analysis |
| Lawful basis for capture | Names the specific provision relied on and its limits | Names a basis with minor imprecision | Asserts a basis without provision | No basis identified, or asserts a non-existent one |
| Ethical reasoning | Nuanced, principled, well-justified | Sound ethical analysis | Basic, surface-level analysis | Little or no ethical reasoning |
| Communication | Clear, structured, professional | Clear with minor lapses | Disorganised but understandable | Unclear |

---

## Australian Context

This unit is Australian context throughout. Key elements:

- **Criminal Code Act 1995 (Cth) sch 1, Part 10.7 (Divisions 476–478):** The
  operative computer offences and the basis for the authorisation requirement
  that governs all offensive/investigative work in the degree (Topics 1–3,
  Lab 1). Part 10.7 was inserted by the *Cybercrime Act 2001* (Cth) sch 1
  and commenced 21 December 2001; the *Cybercrime Act 2001* is an amending Act
  and is cited in this unit only historically.
- **Cybercrime Legislation Amendment Act 2012 (Cth) sch 3:** Repealed the
  Commonwealth-nexus elements of the Division 477 and 478 offences, commencing
  1 March 2013 (Topic 3).
- **State and Territory computer offences:** Concurrent with Part 10.7 by force
  of s 476.4 — *Crimes Act 1958* (Vic) ss 247A–247I; *Criminal Code* (Qld)
  s 408E; *The Criminal Code* (WA) s 440A; *Crimes Act 1900* (NSW) Part 6 (ss 308–308I, individual sections and
  penalties unverified — see Verification status);
  *Criminal Code* (Tas) ss 257A–257F; *Criminal Code 2002* (ACT) Part 4.2;
  *Criminal Code* (NT) Part VIIA Div 1; and the South Australian summary
  computer-misuse offence (Topic 3).
- **Telecommunications (Interception and Access) Act 1979 (Cth):** The
  prohibition on interception, and the s 7(2)(aaa) written network-protection
  authorisation that makes workplace capture lawful (Topic 4, Lab 3).
- **Surveillance Devices Act 2004 (Cth) and State surveillance-devices law
  (e.g. *Surveillance Devices Act 1999* (Vic)):** Law-enforcement powers versus
  the prohibitions that actually bind private parties (Topic 4).
- **Crimes Act 1914 (Cth) s 3LA:** Magistrate-ordered assistance with access to
  data, and the modern penalties for refusing (Topic 9).
- **Privacy Act 1988 (Cth) & Australian Privacy Principles:** The data protection
  regime, with APP 11 (security) emphasised and APP 3/APP 5 relevant to capture
  (Topic 5).
- **Notifiable Data Breaches scheme (OAIC):** Breach assessment and notification
  obligations practised in Lab 2.
- **Security of Critical Infrastructure Act 2018 (Cth):** Critical-infrastructure
  obligations, data storage systems, and the 12-hour/72-hour reporting clocks
  (Topic 7).
- **Cyber Security Act 2024 (Cth) and the Cyber Security (Ransomware Payment
  Reporting) Rules 2025:** The 72-hour ransomware-payment report, the $3 million
  turnover threshold, and the limited-use protections (Topic 7, Lab 2).
- **Criminal Code (Cth) ss 474.17C–474.17D:** The doxxing offences constraining
  OSINT and attribution deliverables (Topic 8).
- **Regulators:** OAIC, ACSC/ASD, AFP, APRA roles and powers (Topic 9).
- **AISA:** The Australian professional body referenced for ethics (Topic 8).

---

## Verification status

Per **R5 (accuracy over speed)**, everything below was *not* confirmed against a
primary source for this revision. Nothing in this table may be taught as settled
law, and no unverified section number appears as a bare assertion in the topics
above. Items are for Domain Expert and Practitioner Reviewer resolution before
this unit moves past Draft.

| Item | Status | Action required |
|---|---|---|
| NSW computer offences: the section range, headings and **all penalties** in *Crimes Act 1900* (NSW) Part 6 (ss 308–308I) | **Could not verify** — legislation.nsw.gov.au and AustLII both returned HTTP 403 to every attempt | Read the current consolidation at legislation.nsw.gov.au and insert verified section numbers and penalties in the Topic 3 table |
| NT computer offences: the section range *Criminal Code* (NT) Part VIIA Div 1 ss 276–276F and **all four maximum penalties** | **Not verified** — no NT primary source was read | Read the current consolidation at legislation.nt.gov.au; the structural point about s 276B(2) (unlawful *use* of unlawfully accessed data) is the teaching content, not the year figures |
| Qld: the amending Act that renamed s 408E to “Misuse of restricted computer” | **Not verified** — heading confirmed on the current consolidation, amending Act number not confirmed | Confirm on legislation.qld.gov.au, or drop the attribution |
| *Cybercrime Act 2001* (Cth) Schedule 1 **item numbers** for the Part VIA repeal and the Part 10.7 insertion | **Could not verify** — the Federal Register and AustLII returned HTTP 403; cited at Schedule level only, which is sufficient for the teaching point | Confirm item numbers against the as-made text if a pinpoint is wanted |
| South Australia: the instrument, section number and penalty for the SA computer-misuse offence (commonly cited as s 44 of the *Summary Offences Act 1953* (SA)) | **Could not verify** — legislation.sa.gov.au returned HTTP 403 | Confirm the instrument and section at legislation.sa.gov.au before any SA citation is published |
| ACT: individual maximum penalties for *Criminal Code 2002* (ACT) ss 415–421 | **Unverified** — only Part 4.2 section numbers and headings were read (republication R58, effective 23 February 2026) | Read the penalties from the authorised ACT republication and add them to the Topic 3 table |
| Tasmania: maximum penalties for *Criminal Code* (Tas) ss 257B–257E, and the general proposition that Tasmanian Code crimes take their penalty from s 389 | **Unverified** | Confirm against the consolidated Tasmanian Code |
| Constitutional basis for the nexus-free Part 10.7 offences after 2013 (external affairs power) | **Inferred, not verified** — drawn from Schedule 3's commencement being tied to the Convention on Cybercrime entering into force for Australia | Read the Explanatory Memorandum and the constitutional-power statement before teaching the attribution |
| *Cyber Security Act 2024* (Cth) Part 3 commencement date (30 May 2025) and the "education-first to 31 December 2025, enforcement from January 2026" posture | **Secondary-source only** — the statutory rule is Proclamation, or a default six months after the 29 November 2024 assent; the Proclamation was not located on the Federal Register. The posture is administrative policy, not law | Confirm the proclaimed date on the Federal Register; treat the posture as regulator policy that can change |
| Whether rules specify a "designated Commonwealth body" under s 8 of the *Cyber Security Act 2024* (Cth), or the default (the Department and ASD) applies | **Not checked** | Check the Federal Register for rules made under s 8 |
| Complicity, incitement and conspiracy exposure (Criminal Code Part 2.4) for publishing exploit code, asserted in Topic 2 | **Not read** | Read ss 11.2, 11.2A, 11.4 and 11.5 before teaching the extension beyond s 478.4 |
| The statutory tort of serious invasion of privacy said to be inserted into the *Privacy Act 1988* by the *Privacy and Other Legislation Amendment Act 2024* (Cth) | **Not verified** against the primary text | Confirm in the current Privacy Act consolidation before Topic 5 relies on it |
| *Surveillance Devices Act 2004* (Cth): only the long title, s 3 (purposes) and s 4 (relationship to other laws) were read; s 45 and the protected-information offences were not | **Partially verified** | Read the remaining provisions if the unit's treatment is expanded |
| TIA Act: the regulations specifying matters for the s 7(2A) "reasonably necessary" assessment | **Not read** | Read the Telecommunications (Interception and Access) Regulations before Lab 3 is delivered |
| NSW *Surveillance Devices Act 2007* and *Workplace Surveillance Act 2005* — including the commonly taught 14-day written notice and surveillance-policy requirements for computer surveillance of employees, and covert surveillance requiring a court authority | **Not verified** — NSW legislation site inaccessible | Verify before Lab 3 step 4 is taught in a NSW context |
| Surveillance-devices and workplace-surveillance statutes for Qld, WA, SA, Tas, NT and the ACT | **Not read** — only the *Surveillance Devices Act 1999* (Vic) was verified | Verify the learner's own jurisdiction before delivery |
| SOCI: the Critical Infrastructure Risk Management Program Rules, the asset-class definition rules, and civil penalty amounts outside ss 30BC/30BD | **Not read** | Re-verify each teaching period; SOCI is amended frequently and much detail sits in subordinate rules |
| Currency of the State sources read: *Crimes Act 1958* (Vic) Authorised Version No 307 (published February 2025); *The Criminal Code* (WA) official version as at 30 May 2025; the Qld consolidation, whose currency date was not captured | **Currency unconfirmed** as at the date of this revision | Re-check each jurisdiction's current authorised version before delivery |
| Criminal Code (Cth) ss 476.6 and 476.7 (ASIS/ASD/AGO and defence-official immunities) — named in Topic 1 but not analysed | **Read, not analysed** | Decide whether s 476.7 has student-facing relevance |
| Project-local KSAT IDs (`F05-K01`…), the Program Builder capability mapping | **Provisional** | Framework Custodian mapping to official NICE/DCWF identifiers (Phase 4) |

Primary sources relied on for the verified material in this unit: *Criminal Code
Act 1995* (Cth) compilation No 174 (registerId C2026C00243, compilation date 30
June 2026); *Crimes Act 1914* (Cth) compilation No 167 (compilation date 27
August 2026); *Telecommunications (Interception and Access) Act 1979* (Cth)
compilation No 134 (C2026C00372, 27 August 2026); *Surveillance Devices Act 2004*
(Cth) compilation No 62 (C2026C00371, 27 August 2026); *Security of Critical
Infrastructure Act 2018* (Cth) compilation No 9 (C2026C00213, 4 June 2026);
*Cyber Security Act 2024* (Cth) as made (No 98 of 2024); *Cyber Security
(Ransomware Payment Reporting) Rules 2025* (F2025L00278); *Cybercrime Act 2001*
(Cth) as made (No 161 of 2001); *Cybercrime Legislation Amendment Act 2012* (Cth)
as made (No 120 of 2012); *Surveillance Devices Act 1999* (Vic) Authorised
Version No 048. **Compilations change — re-verify before each teaching period.**

---

## Further Reading

**Office of the Australian Information Commissioner (2024).** *Australian Privacy Principles & Data Breach Preparation and Response guides.* OAIC. https://www.oaic.gov.au
> Relevance: The authoritative source for the Privacy Act, APPs, and NDB scheme central to Topics 5 and 6 and Lab 2 (**Australian source**).

**Australian Government.** *Criminal Code Act 1995 (Cth) — Schedule 1, Part 10.7 (Computer offences) and ss 474.17C–474.17D.* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The operative computer offences and the doxxing offences. Read the **current compilation** (compilation No 174, registerId C2026C00243, was the version verified for this revision), not a point-in-time version, and note that the endnotes record Part 10.7 as added by Act No 161 of 2001 (**Australian source**).

**Australian Government (2001).** *Cybercrime Act 2001 (Cth), Act No 161 of 2001 (titleId C2004A00937).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The **amending** Act. Read Schedule 1 to see the repeal of the *Crimes Act 1914* Part VIA offences and the insertion of Part 10.7, and Schedule 2 for the original s 3LA. Useful as a worked example of why an amending Act is not operative law (**Australian source**).

**Australian Government (2012).** *Cybercrime Legislation Amendment Act 2012 (Cth).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: Schedule 3 is the repeal of the Commonwealth-nexus elements discussed in Topic 3; read it item by item against the pre-2013 offence text (**Australian source**).

**Australian Government (1979).** *Telecommunications (Interception and Access) Act 1979 (Cth).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: Sections 5, 6, 7, 63 and 105, plus Chapter 3, are the prohibition and exceptions that govern every capture lab in the degree (**Australian source**).

**Australian Government (2018/2024).** *Security of Critical Infrastructure Act 2018 (Cth)* and the *Cyber Security Act 2024 (Cth).* Federal Register of Legislation. https://www.legislation.gov.au
> Relevance: The primary legislation behind Topic 7, including SOCI Part 2B reporting and the ransomware-payment report; students should read the current consolidated versions (**Australian source**).

**Australian Signals Directorate / ACSC.** *Report a cybercrime, incident or vulnerability, and ransomware payment reporting guidance.* https://www.cyber.gov.au
> Relevance: The practical reporting channel behind SOCI and the Cyber Security Act 2024 obligations, and the regulator's stated administrative posture (**Australian source**; administrative guidance, not law).

**Australian Information Security Association (2024).** *AISA Code of Conduct.* AISA. https://www.aisa.org.au
> Relevance: The leading Australian professional body's ethics code, used in Topic 8 (**Australian source**).

**Cyber Security Cooperative Research Centre / academic commentary (2023).** *Australian cyber law and policy analyses.* (Freely available CSCRC publications.) https://cybersecuritycrc.org.au
> Relevance: Accessible Australian analysis connecting legislation to practice for the case-study assessment (**Australian source**).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F05 |
| Unit Title | Legal, Ethics & Australian Compliance |
| Version | v0.2 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-09-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Criminal Code Act 1995 (Cth) sch 1 Pt 10.7 (Divs 476–478) and ss 474.17C–474.17D; Cybercrime Act 2001 (Cth) (amending Act, historical citation only); Cybercrime Legislation Amendment Act 2012 (Cth) sch 3; Crimes Act 1914 (Cth) s 3LA; State/Territory computer offences (Vic, Qld, WA, NSW, SA, Tas, ACT, NT); Telecommunications (Interception and Access) Act 1979 (Cth); Surveillance Devices Act 2004 (Cth); Surveillance Devices Act 1999 (Vic); Privacy Act 1988 (APPs, NDB scheme); Security of Critical Infrastructure Act 2018 (Cth); Cyber Security Act 2024 (Cth) and Cyber Security (Ransomware Payment Reporting) Rules 2025 |
