# Program: Operations + Threat Hunting major

> **Generated** by `.github/scripts/program_builder.py`. Do not edit by hand.
> KSAT IDs are project-local (provisional) pending Framework Custodian
> mapping to official NICE/DCWF identifiers. Charts use Mermaid radar
> (v11.6+) and xychart (v10.3+); each is backed by a table below it.

A realistic single-major program: the 18-unit shared core plus the six Threat Hunting units.

**Selection:** 24 of 66 units · **237** KSAT items (93 K · 48 S · 48 A · 48 T) · **36%** of the full catalogue (655 items).

## Selected courses

| Domain | Units |
|---|---|
| Foundation | F01, F02, F03, F04, F05, F06 |
| Operational Core | OC01, OC02, OC03, OC04, OC05, OC06 |
| Strategic Core | SC01, SC02, SC03, SC04, SC05, SC06 |
| Threat Hunting | TH01, TH02, TH03, TH04, TH05, TH06 |

## NICE/DCWF work-role completion

Percentage of each work role's catalogue KSATs delivered by this selection (a role's KSAT universe is the sum of KSATs across every unit that develops it).

```mermaid
xychart-beta horizontal
  title "Work-role KSAT completion (%)"
  x-axis ["SP-DEV-001", "OM-ADM-001", "OV-LGA-001", "OV-LGA-002", "PR-CIR-001", "PR-VAM-001", "SP-RSK-002", "PR-CDA-001", "OV-SPP-001", "AN-TWA-001", "SP-ARC-001", "IN-FOR-002", "OV-MGT-001", "AN-EXP-001", "AN-ASA-001", "SP-ARC-002", "IN-INV-001", "OV-EXL-001", "OV-SPP-002", "SP-DEV-002"]
  y-axis "Percent complete" 0 --> 100
  bar [100, 66, 50, 50, 50, 50, 50, 47, 44, 40, 33, 29, 25, 20, 14, 14, 0, 0, 0, 0]
```

| Work role | Code | Covered | Catalogue | % |
|---|---|---|---|---|
| Software Developer | SP-DEV-001 | 10 | 10 | 100% |
| System Administrator | OM-ADM-001 | 19 | 29 | 66% |
| Cyber Legal Advisor | OV-LGA-001 | 10 | 20 | 50% |
| Privacy Officer/Privacy Compliance Manager | OV-LGA-002 | 10 | 20 | 50% |
| Cyber Defense Incident Responder | PR-CIR-001 | 20 | 40 | 50% |
| Vulnerability Assessment Analyst | PR-VAM-001 | 10 | 20 | 50% |
| Security Control Assessor | SP-RSK-002 | 40 | 80 | 50% |
| Cyber Defense Analyst | PR-CDA-001 | 117 | 247 | 47% |
| Cyber Policy & Strategy Planner | OV-SPP-001 | 40 | 90 | 44% |
| Threat/Warning Analyst | AN-TWA-001 | 40 | 100 | 40% |
| Enterprise Architect | SP-ARC-001 | 10 | 30 | 33% |
| Cyber Defense Forensics Analyst | IN-FOR-002 | 20 | 70 | 29% |
| Information Systems Security Manager | OV-MGT-001 | 30 | 118 | 25% |
| Exploitation Analyst | AN-EXP-001 | 10 | 50 | 20% |
| All-Source Analyst | AN-ASA-001 | 10 | 70 | 14% |
| Security Architect | SP-ARC-002 | 10 | 70 | 14% |
| Cyber Crime Investigator | IN-INV-001 | 0 | 20 | 0% |
| Executive Cyber Leadership | OV-EXL-001 | 0 | 38 | 0% |
| Cyber Workforce Developer/Manager | OV-SPP-002 | 0 | 10 | 0% |
| Secure Software Assessor | SP-DEV-002 | 0 | 20 | 0% |

## KSAT coverage by domain (spider charts)

Each axis is a degree domain. The **Catalogue** curve is everything on offer; the **Selected** curve is what this program delivers. The gap between them is the breadth not taken.

### Knowledge

```mermaid
radar-beta
  title Knowledge coverage by domain
  axis f["Foundation"], oc["Op Core"], sc["Str Core"], th["Threat Hunt"], df["DFIR"], ct["CTI"], de["Detection"], ce["Emulation"], se["Sec Eng"], ld["Leadership"], gr["GRC"]
  curve cat["Catalogue"]{21, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24}
  curve sel["Selected"]{21, 24, 24, 24, 0, 0, 0, 0, 0, 0, 0}
  max 24
  min 0
```

### Skill

```mermaid
radar-beta
  title Skill coverage by domain
  axis f["Foundation"], oc["Op Core"], sc["Str Core"], th["Threat Hunt"], df["DFIR"], ct["CTI"], de["Detection"], ce["Emulation"], se["Sec Eng"], ld["Leadership"], gr["GRC"]
  curve cat["Catalogue"]{12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12}
  curve sel["Selected"]{12, 12, 12, 12, 0, 0, 0, 0, 0, 0, 0}
  max 12
  min 0
```

### Ability

```mermaid
radar-beta
  title Ability coverage by domain
  axis f["Foundation"], oc["Op Core"], sc["Str Core"], th["Threat Hunt"], df["DFIR"], ct["CTI"], de["Detection"], ce["Emulation"], se["Sec Eng"], ld["Leadership"], gr["GRC"]
  curve cat["Catalogue"]{12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12}
  curve sel["Selected"]{12, 12, 12, 12, 0, 0, 0, 0, 0, 0, 0}
  max 12
  min 0
```

### Task

```mermaid
radar-beta
  title Task coverage by domain
  axis f["Foundation"], oc["Op Core"], sc["Str Core"], th["Threat Hunt"], df["DFIR"], ct["CTI"], de["Detection"], ce["Emulation"], se["Sec Eng"], ld["Leadership"], gr["GRC"]
  curve cat["Catalogue"]{12, 12, 12, 12, 12, 12, 12, 12, 12, 10, 12}
  curve sel["Selected"]{12, 12, 12, 12, 0, 0, 0, 0, 0, 0, 0}
  max 12
  min 0
```

**Domain × type — Selected / Catalogue**

| Domain | Knowledge | Skills | Abilities | Tasks |
|---|---|---|---|---|
| Foundation | 21 / 21 | 12 / 12 | 12 / 12 | 12 / 12 |
| Operational Core | 24 / 24 | 12 / 12 | 12 / 12 | 12 / 12 |
| Strategic Core | 24 / 24 | 12 / 12 | 12 / 12 | 12 / 12 |
| Threat Hunting | 24 / 24 | 12 / 12 | 12 / 12 | 12 / 12 |
| DFIR | 0 / 24 | 0 / 12 | 0 / 12 | 0 / 12 |
| Cyber Threat Intelligence | 0 / 24 | 0 / 12 | 0 / 12 | 0 / 12 |
| Detection Engineering | 0 / 24 | 0 / 12 | 0 / 12 | 0 / 12 |
| Cyber Threat Emulation | 0 / 24 | 0 / 12 | 0 / 12 | 0 / 12 |
| Security Engineering | 0 / 24 | 0 / 12 | 0 / 12 | 0 / 12 |
| Leadership & CISO | 0 / 24 | 0 / 12 | 0 / 12 | 0 / 10 |
| Governance, Risk & Compliance | 0 / 24 | 0 / 12 | 0 / 12 | 0 / 12 |

## KSAT composition of this program

```mermaid
pie showData
  title KSAT composition
  "Knowledge" : 93
  "Skills" : 48
  "Abilities" : 48
  "Tasks" : 48
```

## Program structure

```mermaid
flowchart LR
  P([Operations + Threat Hunting major])
  P --> D0["Foundation<br/>6 units"]
  P --> D1["Operational Core<br/>6 units"]
  P --> D2["Strategic Core<br/>6 units"]
  P --> D3["Threat Hunting<br/>6 units"]
```

---

_Build your own: `python3 .github/scripts/program_builder.py --help`._
