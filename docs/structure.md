# Degree Structure

> 🧭 **Assemble your own pathway interactively:** the
> [Program Builder](program-builder/index.md) lets you tick courses (grouped by
> degree → year → major) and instantly see the NICE/DCWF work-role and KSAT
> coverage your selection delivers — no scripts required.

---

## Architecture Overview

The degree system is built in three layers:

```mermaid
graph TB
    subgraph L1["Layer 1 — Foundation (Shared, Year 1)"]
        direction LR
        L1A["Networking &<br/>Infrastructure"]
        L1B["Operating Systems"]
        L1C["Scripting &<br/>Automation"]
        L1D["Security Concepts<br/>& Principles"]
        L1E["Legal, Ethics &<br/>Australian Compliance"]
        L1F["Data & Log<br/>Analysis"]
    end

    subgraph L2["Layer 2 — Degree Core (Year 2)"]
        direction LR
        L2_OP["Operational Core<br/>(6 units)"]
        L2_ST["Strategic Core<br/>(6 units)"]
    end

    subgraph L3["Layer 3 — Major (Year 3)"]
        direction LR
        L3A["Threat Hunting"]
        L3B["DFIR"]
        L3C["CTI"]
        L3D["Detection Eng."]
        L3E["CTE"]
        L3F["Sec. Engineering"]
        L3G["Leadership/CISO"]
        L3H["GRC"]
    end

    L1 --> L2_OP
    L1 --> L2_ST
    L2_OP --> L3A & L3B & L3C & L3D & L3E
    L2_ST --> L3F & L3G & L3H
```

---

## Credit Structure

| Layer | Units | Credit Points | Year |
|---|---|---|---|
| Foundation (shared) | 6 | 48 CP | Year 1 |
| Degree Core (operational or strategic) | 6 | 48 CP | Year 2 |
| Major | 6 | 48 CP | Year 3 |
| Capstone | 1 | 24 CP | Year 3 |
| **Total** | **19** | **168 CP** | **3 years** |

> Credit point structure follows AQF Level 7 Bachelor Degree conventions (typically 144–192 CP for a 3-year degree at Australian universities).

---

## Foundation Year — Units (Shared)

These units are completed by all students regardless of which degree or major they pursue.

```mermaid
graph LR
    subgraph FY["Foundation Year"]
        F1["F01<br/>Networking Fundamentals<br/><i>TCP/IP, protocols, packet analysis</i>"]
        F2["F02<br/>Operating Systems & Administration<br/><i>Windows, Linux, file systems, processes</i>"]
        F3["F03<br/>Scripting & Automation<br/><i>Python, Bash, PowerShell</i>"]
        F4["F04<br/>Security Concepts & Principles<br/><i>CIA triad, threat models, controls</i>"]
        F5["F05<br/>Legal, Ethics & Australian Compliance<br/><i>Privacy Act, SOCI Act, NDB, ASD</i>"]
        F6["F06<br/>Data & Log Analysis<br/><i>SIEM fundamentals, log parsing, queries</i>"]
    end
```

### Foundation Unit Descriptions

#### F01 — Networking Fundamentals
**AQF Learning Outcomes:**
- Explain the OSI and TCP/IP models and their role in network communication
- Analyse packet captures to identify protocols, anomalies, and communication flows
- Configure and troubleshoot basic network services (DNS, DHCP, HTTP/S)

**Tools:** Wireshark, tcpdump, nmap
**Framework Mapping:** NIST NICE K0001, K0010, K0011, K0034; SFIA NTAS; DCWF 511

---

#### F02 — Operating Systems & Administration
**AQF Learning Outcomes:**
- Administer Windows and Linux systems at a command-line level
- Describe OS internals including processes, memory, file systems, and authentication
- Identify OS artefacts relevant to security investigations

**Tools:** Windows CLI, PowerShell, Bash, Sysinternals
**Framework Mapping:** NIST NICE K0117, K0167, K0187; SFIA ITOP; DCWF 511, 521

---

#### F03 — Scripting & Automation
**AQF Learning Outcomes:**
- Write Python, Bash, and PowerShell scripts to automate security tasks
- Parse and manipulate structured data (JSON, CSV, XML) programmatically
- Build basic tooling for log analysis, file processing, and API interaction

**Tools:** Python 3, Bash, PowerShell, VS Code
**Framework Mapping:** NIST NICE K0068, S0266; SFIA PROG; DCWF 531

---

#### F04 — Security Concepts & Principles
**AQF Learning Outcomes:**
- Apply the CIA triad and fundamental security principles to system design
- Construct threat models using STRIDE or similar methodologies
- Explain the categories of security controls (preventive, detective, corrective)

**Tools:** Microsoft Threat Modelling Tool, draw.io
**Framework Mapping:** NIST CSF 2.0 (all functions); NIST NICE K0004, K0007; SFIA SCAD

---

#### F05 — Legal, Ethics & Australian Compliance
**AQF Learning Outcomes:**
- Identify obligations under the Privacy Act 1988 and Notifiable Data Breaches scheme
- Explain the scope and intent of the Security of Critical Infrastructure Act 2018
- Describe the role of Australian regulators: ASD/ACSC, APRA, OAIC, AFP
- Apply ethical frameworks to cybersecurity decision-making

**Framework Mapping:** NIST NICE K0003; ASD Essential Eight context; APRA CPS 234 overview; SFIA CNSL

---

#### F06 — Data & Log Analysis
**AQF Learning Outcomes:**
- Ingest, parse, and query log data from multiple source types
- Identify patterns and anomalies in event data
- Write basic detection logic and alert rules

**Tools:** Splunk Free / OpenSearch / Elastic Stack, Sigma
**Framework Mapping:** NIST NICE K0058, S0173; DCWF 511; NIST CSF 2.0 DE.AE

---

## Operational Degree — Year 2 Core

```mermaid
graph LR
    subgraph OC["Operational Core"]
        O1["OC01<br/>Adversary Tradecraft & TTPs<br/><i>ATT&CK, kill chain, actor profiling</i>"]
        O2["OC02<br/>Security Monitoring & SIEM<br/><i>Detection at scale, use case dev</i>"]
        O3["OC03<br/>Malware Analysis Fundamentals<br/><i>Static & dynamic analysis</i>"]
        O4["OC04<br/>Incident Response Lifecycle<br/><i>PICERL, containment, recovery</i>"]
        O5["OC05<br/>Threat Intelligence Fundamentals<br/><i>CTI lifecycle, STIX/TAXII, feeds</i>"]
        O6["OC06<br/>Offensive Security Concepts<br/><i>Recon, exploitation concepts, C2</i>"]
    end
```

---

## Strategic Degree — Year 2 Core

```mermaid
graph LR
    subgraph SC["Strategic Core"]
        S1["SC01<br/>Risk Management Frameworks<br/><i>NIST RMF, ISO 27005, bow-tie</i>"]
        S2["SC02<br/>Security Architecture Principles<br/><i>SABSA, Zero Trust, defence-in-depth</i>"]
        S3["SC03<br/>Governance, Policy & Compliance<br/><i>Policy design, control frameworks</i>"]
        S4["SC04<br/>Vendor & Supply Chain Risk<br/><i>Third-party risk, SCRM</i>"]
        S5["SC05<br/>Security Program Management<br/><i>Roadmaps, metrics, stakeholder mgmt</i>"]
        S6["SC06<br/>Stakeholder Communication<br/><i>Board reporting, risk communication</i>"]
    end
```

---

## Operational Majors — Year 3

### Major 1: Threat Hunting

> Proactive, hypothesis-driven search for threats that have evaded automated detection.

```mermaid
graph TD
    TH["Threat Hunting Major"]
    TH --> TH1["TH01<br/>Hunting Methodology & Process<br/><i>TaHiTI, hypothesis design, hunt loops</i>"]
    TH --> TH2["TH02<br/>ATT&CK for Hunters<br/><i>Technique-based hunting, navigator</i>"]
    TH --> TH3["TH03<br/>Host-Based Hunting<br/><i>Memory, process, persistence artefacts</i>"]
    TH --> TH4["TH04<br/>Network-Based Hunting<br/><i>Traffic analysis, beaconing detection</i>"]
    TH --> TH5["TH05<br/>Hunt Operations & Tooling<br/><i>Jupyter, Velociraptor, EDR hunting</i>"]
    TH --> TH6["TH06<br/>Capstone — Hunt Operation<br/><i>Full hunt lifecycle on live-fire range</i>"]
```

**Role Alignment:** Threat Hunter, Detection Analyst, SOC Tier 3
**Framework Mapping:** NIST NICE TH-INV; ASD CSF; MITRE ATT&CK; SFIA INAS
**Certification Bridges:** GIAC GCIH, eCTHP, BTL2

---

### Major 2: Digital Forensics & Incident Response (DFIR)

> Responding to and investigating security incidents through systematic evidence collection and analysis.

```mermaid
graph TD
    DFIR["DFIR Major"]
    DFIR --> D1["DF01<br/>DFIR Process & Legal Foundations<br/><i>Chain of custody, Evidence Act AU</i>"]
    DFIR --> D2["DF02<br/>Host Forensics<br/><i>Disk imaging, artefact analysis, timelines</i>"]
    DFIR --> D3["DF03<br/>Memory Forensics<br/><i>Volatility, process injection, memory IOCs</i>"]
    DFIR --> D4["DF04<br/>Network Forensics<br/><i>PCAP analysis, C2 identification</i>"]
    DFIR --> D5["DF05<br/>Incident Response Operations<br/><i>PICERL execution, comms, reporting</i>"]
    DFIR --> D6["DF06<br/>Capstone — IR Simulation<br/><i>End-to-end incident on simulated network</i>"]
```

**Role Alignment:** DFIR Analyst, Incident Responder, Forensic Investigator
**Framework Mapping:** PICERL, NIST SP 800-61, DCWF 212/221, DoD 8140, SFIA SURE
**Certification Bridges:** GIAC GCFE, GCFA, GCIH, eCIR, eCDFP

---

### Major 3: Cyber Threat Intelligence (CTI)

> Collecting, processing, analysing, and disseminating intelligence about adversaries to support decision-making.

```mermaid
graph TD
    CTI["CTI Major"]
    CTI --> C1["CT01<br/>Intelligence Tradecraft<br/><i>Intelligence cycle, PIRs, OPSEC</i>"]
    CTI --> C2["CT02<br/>Threat Actor Research & Profiling<br/><i>Diamond Model, group tracking</i>"]
    CTI --> C3["CT03<br/>Technical Intelligence<br/><i>Malware IOCs, infra analysis, pivoting</i>"]
    CTI --> C4["CT04<br/>Strategic Intelligence<br/><i>Geopolitical context, sector threats, briefings</i>"]
    CTI --> C5["CT05<br/>CTI Platforms & Sharing<br/><i>MISP, OpenCTI, STIX/TAXII, CTID</i>"]
    CTI --> C6["CT06<br/>Capstone — Intelligence Product<br/><i>Full CTI report from collection to dissemination</i>"]
```

**Role Alignment:** CTI Analyst, Threat Intelligence Manager
**Framework Mapping:** MITRE CTID, STIX 2.1, Diamond Model, NIST NICE IN-001; SFIA INAS
**Certification Bridges:** GIAC GCTI, CREST CCTIM, eCTHP

---

### Major 4: Detection Engineering

> Designing, building, and maintaining detection logic that converts threat knowledge into reliable alerts.

```mermaid
graph TD
    DE["Detection Engineering Major"]
    DE --> E1["DE01<br/>Detection Theory & Philosophy<br/><i>Pyramid of Pain, detection-as-code</i>"]
    DE --> E2["DE02<br/>Data Sources & Log Engineering<br/><i>Data modelling, normalisation, gaps</i>"]
    DE --> E3["DE03<br/>Writing Detection Logic<br/><i>Sigma, SPL, KQL, YARA</i>"]
    DE --> E4["DE04<br/>Adversary Simulation for Detection<br/><i>Atomic Red Team, testing pipelines</i>"]
    DE --> E5["DE05<br/>Detection Operations & Management<br/><i>Alert quality, tuning, lifecycle mgmt</i>"]
    DE --> E6["DE06<br/>Capstone — Detection Library<br/><i>Build and test a detection rule library</i>"]
```

**Role Alignment:** Detection Engineer, Security Content Engineer, SOC Content Developer
**Framework Mapping:** MITRE ATT&CK, NIST CSF 2.0 DE.*, Sigma, NIST NICE; SFIA SCAD
**Certification Bridges:** GIAC GDAT, Splunk Core Certified, Elastic Engineer

---

### Major 5: Cyber Threat Emulation (CTE)

> Simulating adversary behaviour to test and improve defensive controls and team readiness.

```mermaid
graph TD
    CTE["Cyber Threat Emulation Major"]
    CTE --> E1["CE01<br/>Offensive Foundations & Ethics<br/><i>Authorised testing, scope, rules of engagement</i>"]
    CTE --> E2["CE02<br/>Red Team Operations<br/><i>C2 frameworks, tradecraft, OPSEC</i>"]
    CTE --> E3["CE03<br/>ATT&CK-Based Emulation<br/><i>Emulation plans, CTID methodology</i>"]
    CTE --> E4["CE04<br/>Purple Team Operations<br/><i>Collaborative testing, detection gap analysis</i>"]
    CTE --> E5["CE05<br/>Reporting & Debrief<br/><i>Technical & executive reporting, TIBER-AU</i>"]
    CTE --> E6["CE06<br/>Capstone — Emulation Exercise<br/><i>Full threat emulation op with detection team</i>"]
```

**Role Alignment:** Red Team Operator, Purple Team Lead, Adversary Emulation Engineer
**Framework Mapping:** MITRE ATT&CK, MITRE CTID, TIBER-EU/AU, NIST NICE PR-CDA; SFIA PENT
**Certification Bridges:** GIAC GPEN, GRTOP, eCPTX, OSCP

---

## Strategic Majors — Year 3

### Major 6: Security Engineering

> Designing and implementing secure systems, architectures, and tooling at a technical level.

```mermaid
graph TD
    SE["Security Engineering Major"]
    SE --> S1["SE01<br/>Secure System Design<br/><i>Secure SDLC, threat modelling, secure defaults</i>"]
    SE --> S2["SE02<br/>Security Architecture<br/><i>SABSA, Zero Trust, cloud security architecture</i>"]
    SE --> S3["SE03<br/>Identity & Access Management<br/><i>IAM design, PAM, federation, MFA</i>"]
    SE --> S4["SE04<br/>Detection & Response Engineering<br/><i>SIEM/SOAR design, automation pipelines</i>"]
    SE --> S5["SE05<br/>Security in Cloud & DevSecOps<br/><i>IaC security, container security, CI/CD</i>"]
    SE --> S6["SE06<br/>Capstone — Architecture Design<br/><i>Secure architecture for a defined environment</i>"]
```

**Role Alignment:** Security Architect, Security Engineer, Principal Security Consultant
**Framework Mapping:** NIST SP 800-160, NIST CSF 2.0, SABSA, SFIA ARCH; Zero Trust (NIST SP 800-207)
**Certification Bridges:** SABSA SCF, AWS Security Specialty, CISSP ISSAP

---

### Major 7: Leadership & CISO

> Building the knowledge and skills required for executive cybersecurity leadership.

```mermaid
graph TD
    LD["Leadership & CISO Major"]
    LD --> L1["LD01<br/>The CISO Role & Function<br/><i>Mandate, reporting lines, board engagement</i>"]
    LD --> L2["LD02<br/>Security Strategy & Roadmapping<br/><i>3-year planning, maturity models, investment cases</i>"]
    LD --> L3["LD03<br/>Communicating Risk to Executives<br/><i>Risk language, dashboards, board reporting</i>"]
    LD --> L4["LD04<br/>Building & Leading Security Teams<br/><i>Hiring, culture, career pathways, talent retention</i>"]
    LD --> L5["LD05<br/>Crisis Management & Comms<br/><i>Incident comms, media, regulator notification AU</i>"]
    LD --> L6["LD06<br/>Capstone — CISO Simulation<br/><i>Present a security strategy and budget to a board</i>"]
```

**Role Alignment:** CISO, Security Director, VP Security
**Framework Mapping:** NIST CSF 2.0 GV.*, NIST NICE OV-MGT; SFIA MANA; CISM domains
**Certification Bridges:** CISM, CISSP, GIAC GSLC

---

### Major 8: GRC (Governance, Risk & Compliance)

> Designing and managing the governance structures, risk processes, and compliance programs that underpin organisational security.

```mermaid
graph TD
    GRC["GRC Major"]
    GRC --> G1["GR01<br/>Security Governance Design<br/><i>Policy hierarchy, roles, accountability structures</i>"]
    GRC --> G2["GR02<br/>Risk Management in Practice<br/><i>Risk registers, bow-tie analysis, treatment options</i>"]
    GRC --> G3["GR03<br/>Compliance Frameworks<br/><i>ISO 27001, NIST CSF 2.0, Essential Eight</i>"]
    GRC --> G4["GR04<br/>Australian Regulatory Environment<br/><i>APRA CPS 234, Privacy Act, SOCI Act, NDB</i>"]
    GRC --> G5["GR05<br/>Audit & Assurance<br/><i>Control testing, internal audit, IRAP</i>"]
    GRC --> G6["GR06<br/>Capstone — GRC Program Design<br/><i>Design a GRC program for a defined organisation</i>"]
```

**Role Alignment:** GRC Analyst, Risk Manager, Compliance Manager, Security Auditor
**Framework Mapping:** NIST CSF 2.0 GV.* & ID.*, ISO 27001/27002, APRA CPS 234, ASD Essential Eight, NIST SP 800-37 (RMF); SFIA IRMG
**Certification Bridges:** CISM, ISO 27001 Lead Implementer, CRISC, IRAP Assessor pathway

---

## Capstone Structure

Each major culminates in a capstone unit (the 6th unit in each major). Capstone projects are:

- **Practical** — completed in a lab or simulated environment
- **Integrated** — requires knowledge from all units in the major
- **Documented** — includes a written report suitable for a professional portfolio
- **Community-reviewed** — submissions are reviewed by at least one practitioner volunteer

```mermaid
flowchart LR
    M1["Major Units 1–5<br/>(Knowledge & Skills)"]
    M2["Capstone Unit 6<br/>(Applied Project)"]
    M3["Portfolio Artefact<br/>(Professional Use)"]
    M1 --> M2 --> M3
```

---

## Prerequisite Pathways

```mermaid
graph TD
    ANY["Any learner"] --> F["Foundation Year<br/>F01–F06"]
    F --> OC["Operational Core<br/>OC01–OC06"]
    F --> SC["Strategic Core<br/>SC01–SC06"]
    OC --> TH["Threat Hunting Major"]
    OC --> DFIR["DFIR Major"]
    OC --> CTI["CTI Major"]
    OC --> DE["Detection Engineering Major"]
    OC --> CTE["Cyber Threat Emulation Major"]
    SC --> SENG["Security Engineering Major"]
    SC --> LD["Leadership Major"]
    SC --> GRC["GRC Major"]
    TH & DFIR & CTI & DE & CTE --> CAP_OP["Operational Capstone"]
    SENG & LD & GRC --> CAP_ST["Strategic Capstone"]
```

> **Cross-pathway note:** Security Engineering benefits from Operational Core exposure. Learners pursuing the Strategic degree are encouraged to complete at least two Operational Core units as electives.
