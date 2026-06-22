# TODO — degrees/operational/cti/

**Major:** Cyber Threat Intelligence (CTI)
**Degree:** Bachelor of Cybersecurity Operations
**Year:** 3
**Units:** CT01–CT06

All units are currently **Planned**. No unit files have been authored yet.

**Update (2026-06-21):** All six units (CT01–CT06) have been authored to **Draft**
and pass the unit linter. They await practitioner review (Domain Expert +
Practitioner Reviewer with active CTI experience; Diamond Model and STIX 2.1
schema compliance verified; attribution guidance reviewed to ensure method is
taught, not specific actor attributions).

---

## Files to Create

| File | Unit | Description |
|---|---|---|
| `CT01-intelligence-tradecraft.md` | CT01 | Intelligence cycle, PIRs, OPSEC, intelligence disciplines |
| `CT02-threat-actor-research-profiling.md` | CT02 | Diamond Model, group tracking, actor attribution methodology |
| `CT03-technical-intelligence.md` | CT03 | Malware IOCs, infrastructure analysis, pivoting, OSINT |
| `CT04-strategic-intelligence.md` | CT04 | Geopolitical context, sector threats, strategic briefings |
| `CT05-cti-platforms-sharing.md` | CT05 | MISP, OpenCTI, STIX 2.1 / TAXII 2.1, MITRE CTID |
| `CT06-capstone-intelligence-product.md` | CT06 | Full CTI report from collection to dissemination (capstone) |

---

## Bloom's Taxonomy Requirements

Units CT01–CT05: **Levels 4–5** (analyse, evaluate, synthesise)
Capstone CT06: **Levels 5–6** (evaluate, create, produce, recommend)

Example verbs: analyse, synthesise, evaluate, assess, attribute, prioritise, produce, recommend

---

## Framework Mapping Requirements

| Framework | Required |
|---|---|
| MITRE CTID | Yes — Center for Threat-Informed Defense methodology |
| MITRE ATT&CK | Yes — actor-technique mapping, group profiles |
| Diamond Model of Intrusion Analysis | Yes — core analytical model (CT02) |
| STIX 2.1 / TAXII 2.1 | Yes — CT05 structured sharing |
| NIST NICE (AN-TWA-001, AN-ASA-001) | Yes — T-codes traceable to labs |
| DCWF (621, 611) | Yes — Threat/Warning and All-Source Analyst roles |
| SFIA 9 (INAS L4–L5) | Yes — at least 2 units |
| CIISec | Recommended |

---

## Lab Requirements

At least 8 labs total. Tools must be free or free-tier.

### Required Labs Across the Major

| Unit | Lab Ideas |
|---|---|
| CT01 | Lab: Write 3 Priority Intelligence Requirements (PIRs) for a fictional Australian utility company facing ransomware groups |
| CT01 | Lab: Map a given scenario through the intelligence cycle (direction → collection → processing → analysis → dissemination) |
| CT02 | Lab: Profile an APAC-relevant threat actor using ATT&CK Navigator and publicly available reports |
| CT02 | Lab: Apply the Diamond Model to a known intrusion case — populate all 4 vertexes |
| CT03 | Lab: Enrich a set of IOCs using VirusTotal free, Shodan free, and passive DNS data |
| CT03 | Lab: Infrastructure pivot exercise — trace C2 infrastructure from a known IP to related domains and certificates |
| CT04 | Lab: Produce a 1-page strategic intelligence briefing on a sector-relevant threat for a non-technical CISO audience |
| CT05 | Lab: Create STIX 2.1 objects (threat actor, malware, relationship) using the Python `stix2` library |
| CT05 | Lab: Ingest a MISP feed into OpenCTI and produce a dashboard for a specific threat actor |
| CT06 | Capstone: Full intelligence product — collection through finished report — for a defined PIR |

**Tools for this major (all free or free-tier):**
- OpenCTI (open-source CTI platform)
- MISP (Malware Information Sharing Platform)
- MITRE ATT&CK Navigator
- Maltego Community Edition
- VirusTotal (free tier)
- Shodan (free tier)
- Python 3 + `stix2` library

---

## Intelligence Levels Coverage

Each of the three intelligence levels must be explicitly covered:

- [ ] **Technical Intelligence** (CT03) — IOCs, TTPs, malware signatures; audience: SOC, Detection Engineering
- [ ] **Operational Intelligence** (CT02, CT03) — campaign analysis, actor intent; audience: DFIR, Threat Hunters
- [ ] **Strategic Intelligence** (CT04) — geopolitical context, sector risk; audience: CISO, Board, GRC

---

## Australian Context

- [ ] **CT01** — ASD Annual Cyber Threat Report as a primary source for Australian PIR development
- [ ] **CT02** — ACSC-identified threat actors targeting Australian sectors; focus on APT groups active in APAC
- [ ] **CT04** — Australia's geopolitical context, QUAD security partnership, critical infrastructure sector risks
- [ ] **CT05** — TISN (Trusted Information Sharing Network for critical infrastructure) context
- [ ] All units — Use real (publicly attributed) Australian incident examples where possible (e.g., ACSC advisories)

---

## Capstone Unit (CT06) Requirements

The capstone must produce a **finished intelligence product**:

- [ ] PIR defined for a named fictional (or anonymised real) Australian organisation
- [ ] Collection plan documented
- [ ] Sources collected and processed (minimum 3 distinct source types)
- [ ] Analysis completed using Diamond Model or another structured methodology
- [ ] Finished intelligence product written at the appropriate level (technical or strategic)
- [ ] STIX 2.1 representation of the threat actor produced
- [ ] Dissemination plan documented
- [ ] Community practitioner review of the finished product
- [ ] Deliverable suitable for professional portfolio (reference `templates/student-portfolio/index.html`)

---

## Sign-off Requirements

Before any unit can be merged:

- [ ] Domain Expert with active CTI experience named in metadata
- [ ] Practitioner Reviewer (different from Domain Expert) named in metadata
- [ ] Diamond Model usage verified for accuracy in CT02
- [ ] STIX 2.1 objects in CT05 labs verified for schema compliance
- [ ] Attribution guidance reviewed — must teach methodology, not make specific actor attributions

See `templates/review-checklist.md` for the full pre-merge checklist.
