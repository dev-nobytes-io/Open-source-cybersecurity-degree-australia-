# Capability Maturity Model Alignment

> This document is the degree's canonical cross-walk between **capability maturity
> models**, the **capabilities/services** they assess, the **NIST CSF 2.0**
> functions those capabilities deliver, the **NIST NICE / DCWF** work roles that
> perform them, and the **KSATs** (Knowledge, Skills, Tasks, Abilities) those roles
> exercise — across **both** the Operational and Strategic degrees.
>
> It exists to prevent a **development mismatch**: operational capability maturity
> (SOC, CTI, hunting, detection, incident response) must be measured and matured
> with the same rigour as the strategic program, and the strategic program
> (governance, security program management, and risk) must be built *on top of*
> those operational maturity measures — not a separate, disconnected maturity story.

_Last updated: 2026-06-21_

---

## 1. Why maturity models, and why operational + strategic together

A capability maturity model answers "how good are we at *X*, and what does better
look like?" for a specific capability. Using maturity models only at the strategic
level (program/governance) while leaving operational capabilities unmeasured
produces a mismatch: the board is told the "program" is maturing while the SOC,
hunt, CTI, detection, and IR capabilities that the program depends on are
un-benchmarked.

This degree resolves that by:

1. Teaching the **operational** maturity model for each operational capability in
   its major (SOC-CMM, CTI-CMM, Hunting Maturity Model, DML/M3TID, SIM3).
2. Teaching the **strategic/program** maturity models in the strategic core and
   Leadership major (C2M2, O-ISM3, NIST CSF Tiers, Essential Eight Maturity Model,
   CMMI).
3. **Wiring them together**: the security program (SC05), governance (SC03), and
   risk (SC01) units consume the operational maturity scores as inputs, so program
   maturity aggregates capability maturity rather than floating free of it.

---

## 2. Maturity model register

| Model | Capability assessed | Source | Levels (summary) | Cost | Degree home |
|---|---|---|---|---|---|
| **SOC-CMM** | Security operations / SOC | Rob van Os (soc-cmm.com) | Domains: Business, People, Process, Technology + **Services**; maturity + capability scores | Free | OC02; TH/DFIR/DE majors |
| **CTI-CMM** | Cyber threat intelligence | cti-cmm.org (community) | Stakeholder-aligned CTI capability levels | Free | OC05; CTI major |
| **SIM3** | Security incident management / CSIRT (IR & DFIR) | Open CSIRT Foundation (used by FIRST/ENISA/TF-CSIRT) | Maturity across Organisation, Human, Tools, Processes parameters | Free | OC04; DFIR major |
| **Hunting Maturity Model (HMM)** | Threat hunting | David Bianco | HM0–HM4 (initial → leading) | Free | TH major (TH01) |
| **PEAK** | Threat hunting (process) | SURGe / Splunk | Hunt-type maturity & process | Free | TH major (TH01) |
| **Detection Maturity Level (DML)** | Detection (semantic maturity of what you detect) | Ryan Stillions (2014) | DML-0 … DML-8 | Free | DE major (DE01) |
| **M3TID** | Threat-informed defense | MITRE CTID | Measure / Maximize / Mature TID | Free | OC01/OC02, DE, CTE |
| **C2M2** | Cybersecurity program (enterprise) | US DOE | 10 domains; MIL 0–3 | Free | SC03/SC05 |
| **O-ISM3** | Information security management (ISMS) | The Open Group | Process maturity for the ISMS | Standard (paid) | SC03/SC05 |
| **SSE-CMM (ISO/IEC 21827)** | Systems security engineering | ISO/IEC | 5 capability levels | Standard (paid) | Security Engineering major (SE01/SE02) |
| **BSIMM** | Software security (observed) | Synopsys/community | Observation-based, 12 practices | Free | Security Engineering (SE01/SE05) |
| **OWASP SAMM** | Software assurance (prescriptive) | OWASP | 5 business functions, maturity 1–3 | Free | Security Engineering (SE01/SE05) |
| **OCEG GRC Capability Model** | Governance, risk & compliance | OCEG ("Red Book") | Learn–Align–Perform–Review components | Free (registration) | GRC major (GR01/GR06) |
| **RIMS Risk Maturity Model** | Risk management | RIMS | 7 attributes, 5 maturity levels | Free | GRC major (GR02) |
| **NIST CSF 2.0 Tiers** | Program / risk governance posture | NIST | Tiers 1–4 (Partial → Adaptive) | Free | SC01/SC05; LD02 |
| **ASD Essential Eight Maturity Model** | Baseline mitigations | ACSC | Maturity Level 0–3 | Free | F04, SC05, LD02 |
| **CMMI** | Process maturity (general) | ISACA/CMMI Institute | Levels 1–5 | Paid | SC05; LD02 (reference) |

> **Confirmation flag — "DF-C2M2":** A canonical model under that exact name is not
> established in public practice. This degree uses **SIM3** as the incident-
> management/DFIR maturity model (plus digital-forensic-readiness maturity concepts).
> If a maintainer has a specific "DF-C2M2" reference in mind, raise a *Framework
> Mapping Error* issue and it will be added here.

---

## 3. The cross-walk: capability → maturity model → CSF → role → KSATs

Each row reads: a **capability/service**, the **maturity model** that benchmarks it,
the **NIST CSF 2.0** function it primarily delivers, the **NICE/DCWF work role(s)**
that perform it, and the **KSAT focus** for that role. Degree units in the last
column.

### Operational capabilities

| Capability / SOC-CMM service | Maturity model | NIST CSF 2.0 | NICE/DCWF role (code) | KSAT focus | Degree unit(s) |
|---|---|---|---|---|---|
| Security monitoring | SOC-CMM (Services) | DE.CM, DE.AE | Cyber Defense Analyst (PR-CDA-001 / 511) | K: log sources, ATT&CK; S: correlation; T: event analysis; A: anomaly recognition | OC02, DE02 |
| Detection engineering | DML + M3TID | DE.AE, PR.PS | Cyber Defense Analyst (511) | K: detection logic, Sigma; S: rule authoring/testing; T: build/tune detections; A: evasion-resistant design | DE01–DE06 |
| Threat hunting | HMM + PEAK | DE.CM, DE.AE | Cyber Defense Analyst (511); Threat/Warning Analyst (AN-TWA-001) | K: TTPs, data; S: hypothesis/analysis; T: hunt execution; A: pattern detection | TH01–TH06 |
| Incident response | SIM3 | RS.*, RC.* | Cyber Defense Incident Responder (PR-CIR-001 / 531) | K: IR lifecycle, AU notification; S: containment; T: incident handling; A: decision under pressure | OC04, DF05 |
| Digital forensics | SIM3 + DF readiness | RS.AN, RC.* | Cyber Defense Forensics Analyst (IN-FOR-002) | K: artefacts, Evidence Act; S: imaging/analysis; T: forensic analysis; A: admissibility-aware judgement | DF01–DF06 |
| Threat intelligence | CTI-CMM | ID.RA, DE.* | Threat/Warning Analyst (AN-TWA-001 / 621); All-Source Analyst (AN-ASA-001 / 611) | K: intel cycle, PIRs; S: analysis; T: produce intelligence; A: estimative judgement | OC05, CT01–CT06 |
| Adversary emulation / purple team | M3TID + ATT&CK | ID.RA, PR.*, DE.* | Vulnerability Assessment Analyst (PR-VAM-001); Exploitation Analyst (AN-EXP-001 / 711) | K: ATT&CK, emulation; S: technique execution; T: authorised testing; A: safe, scoped operation | OC06, CTE major |

### Strategic capabilities (built on the operational maturities above)

| Capability | Maturity model | NIST CSF 2.0 | NICE/DCWF role (code) | KSAT focus | Degree unit(s) |
|---|---|---|---|---|---|
| Risk management | CSF Tiers + (consumes operational maturity) | GV.RM, ID.RA | Security Control Assessor (SP-RSK-002) | K: risk frameworks; S: quantification; T: risk assessment; A: prioritisation | SC01 |
| Governance & compliance | C2M2 + O-ISM3 + **OCEG GRC Capability Model** + CSF (Govern) | GV.* | Cyber Policy & Strategy Planner (OV-SPP-001 / 752); ISSM (OV-MGT-001 / 722) | K: governance, regimes; S: policy; T: control assessment; A: assurance judgement | SC03; GR01, GR03, GR05, GR06 |
| GRC risk management | **RIMS Risk Maturity Model** + ISO 27005 + CSF | GV.RM, ID.RA | Security Control Assessor (SP-RSK-002) | K: risk frameworks, bow-tie; S: register/appetite; T: risk assessment; A: treatment judgement | GR02 |
| Security program management | C2M2 + CMMI + **aggregates SOC-CMM/CTI-CMM/SIM3/HMM/DML** | GV.OC, GV.RM, PR.* | ISSM (OV-MGT-001 / 722) | K: program mgmt; S: roadmap/budget; T: resource allocation; A: portfolio judgement | SC05, LD02 |
| Security leadership / CISO | C2M2 + CSF Tiers + capability maturities | GV.* | Executive Cyber Leadership (OV-EXL-001 / 901) | K: governance, risk; S: strategy/communication; T: program leadership; A: executive judgement | LD01–LD06 |
| Vendor / supply-chain risk | SIG/maturity + CSF | GV.SC, ID.RA | Security Control Assessor (SP-RSK-002) | K: TPRM, SBOM; S: assurance review; T: vendor assessment; A: third-party judgement | SC04 |
| Security architecture | SABSA maturity + **SSE-CMM (ISO/IEC 21827)** + CSF | PR.*, ID.AM | Security Architect (SP-ARC-002 / 652) | K: architecture, Zero Trust; S: design; T: architecture review; A: trade-off judgement | SC02; SE02 |
| Secure systems / software engineering | **SSE-CMM + BSIMM + OWASP SAMM** | PR.PS, PR.* | Security Architect (SP-ARC-002 / 652); Secure Software Assessor (SP-DEV-002) | K: secure SDLC, threat modelling; S: secure design, IaC/pipeline security; T: design audit, AST integration; A: build-time risk judgement | SE01, SE05 |
| Identity & access engineering | (IAM maturity) + CSF | PR.AA | Security Architect (SP-ARC-002 / 652) | K: IAM/PAM, federation; S: IAM design; T: access architecture; A: least-privilege judgement | SE03 |
| Detection & response engineering | SOC-CMM + DML/M3TID | DE.*, RS.* | Security Architect (SP-ARC-002 / 652); Cyber Defense Analyst (511) | K: SIEM/SOAR/XDR; S: platform design; T: pipeline/automation engineering; A: scaling judgement | SE04 |

---

## 4. How the strategic program consumes operational maturity (the anti-mismatch wiring)

The **Security Program Management** unit (SC05) and the **Leadership** strategy unit
(LD02) treat the operational maturity scores as direct inputs:

```
SOC-CMM (OC02)   ─┐
CTI-CMM (OC05)    │
HMM/PEAK (TH)     ├─►  Capability maturity profile  ─►  Program maturity (C2M2 / CMMI)
DML/M3TID (DE)    │                                      └─►  Risk posture (CSF Tiers, SC01)
SIM3 (OC04/DFIR)  ┘                                      └─►  Governance assurance (C2M2/O-ISM3, SC03)
```

- **SC01 (Risk):** capability maturity gaps are *risk inputs* — a low SOC-CMM
  detection-services score raises detection risk in the register.
- **SC03 (Governance):** C2M2/O-ISM3 provide the program/ISMS maturity view; the
  operational models provide the evidence beneath governance assertions.
- **SC05 (Program Management):** the roadmap targets *named* operational maturity
  improvements (e.g. SOC-CMM Services L2→L3, CTI-CMM stakeholder alignment), so
  program maturity is the aggregate of capability maturities.
- **LD02 / LD06 (Leadership):** the CISO strategy and board narrative are expressed
  in these maturity terms, end-to-end.

This is the mechanism that keeps operational and strategic development aligned.

---

## 5. Using this in teaching and assessment

- Operational majors assess students *applying* the relevant operational maturity
  model to a capability (e.g. assessing a SOC with SOC-CMM, a hunt program with HMM).
- Strategic units assess students *aggregating* those into program/governance/risk
  decisions (C2M2/CSF Tiers) — explicitly referencing the operational scores.
- Students populate their competency profile (`templates/student-portfolio/`) with
  the NICE/DCWF roles + KSATs from the cross-walk above.

---

## 6. Maintenance

Maturity models evolve. Track currency in the
[framework currency table](frameworks.md#framework-currency--maintenance) and raise
a *Framework Mapping Error* issue when a model releases a new version (e.g. a new
SOC-CMM or CTI-CMM release). Confirm the **DF-C2M2** reference (see §2 flag).
