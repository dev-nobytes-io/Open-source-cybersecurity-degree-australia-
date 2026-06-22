# TODO — degrees/operational/detection-engineering/

**Major:** Detection Engineering
**Degree:** Bachelor of Cybersecurity Operations
**Year:** 3
**Units:** DE01–DE06

All units are currently **Planned**. No unit files have been authored yet.

**Update (2026-06-21):** All six units (DE01–DE06) have been authored to **Draft**
and pass the unit linter. They await practitioner review (Domain Expert +
Practitioner Reviewer with active detection-engineering experience; Sigma rules and
ATT&CK references verified; Atomic Red Team test IDs verified as current).

---

## Files to Create

| File | Unit | Description |
|---|---|---|
| `DE01-detection-theory-philosophy.md` | DE01 | Pyramid of Pain, detection-as-code, alert quality philosophy |
| `DE02-data-sources-log-engineering.md` | DE02 | Data modelling, log normalisation, source coverage gaps |
| `DE03-writing-detection-logic.md` | DE03 | Sigma, SPL, KQL, YARA — writing and testing detection rules |
| `DE04-adversary-simulation-detection.md` | DE04 | Atomic Red Team, detection testing pipelines, purple teaming basics |
| `DE05-detection-operations-management.md` | DE05 | Alert quality metrics, tuning workflows, detection lifecycle management |
| `DE06-capstone-detection-library.md` | DE06 | Build and test a detection rule library for a given environment (capstone) |

---

## Bloom's Taxonomy Requirements

Units DE01–DE05: **Levels 4–5** (analyse, evaluate, design, build)
Capstone DE06: **Levels 5–6** (create, design, evaluate, construct)

Example verbs: design, construct, build, test, evaluate, optimise, prioritise, analyse

---

## Framework Mapping Requirements

| Framework | Required |
|---|---|
| MITRE ATT&CK (v14+) | Yes — technique-to-detection mapping throughout |
| NIST CSF 2.0 DE.* | Yes — Detect function mapping in DE01, DE02, DE05 |
| NIST NICE DCWF | Yes — T-codes traceable to labs |
| SFIA 9 (SCAD) | Yes — at least 2 units |
| Sigma (open standard) | Yes — core skill in DE03 |
| ASD Essential Eight (logging requirements) | Yes — DE02 must reference AU logging standards |

---

## Lab Requirements

At least 8 labs total. All tools must be free or open-source.

### Required Labs Across the Major

| Unit | Lab Ideas |
|---|---|
| DE01 | Lab: Map a set of existing alerts against the Pyramid of Pain; identify which level each detection operates at |
| DE01 | Lab: Evaluate a set of detection rules for quality — identify false positive risk, coverage gaps, and evasion potential |
| DE02 | Lab: Audit Windows event log sources against an ATT&CK technique list; identify logging gaps |
| DE02 | Lab: Normalise log data from 3 different sources into a common schema using Python |
| DE03 | Lab: Write 5 Sigma rules for ATT&CK techniques in the Execution tactic |
| DE03 | Lab: Convert a Sigma rule to SPL and KQL; test against sample data |
| DE03 | Lab: Write a YARA rule for a given malware family based on static indicators |
| DE04 | Lab: Execute Atomic Red Team tests and verify Sigma rules fire correctly |
| DE04 | Lab: Build a simple detection testing pipeline using Atomic Red Team + Sigma converter + SIEM |
| DE05 | Lab: Analyse a set of alerts for tuning opportunities; produce a tuning recommendation report |
| DE06 | Capstone: Build a detection library of 10+ tested Sigma rules covering a defined threat scenario |

**Tools for this major (all free/OSS):**
- Sigma (detection rule language + converter)
- Splunk Free / OpenSearch / Elastic Stack
- YARA
- Atomic Red Team (Invoke-AtomicRedTeam)
- MITRE ATT&CK Navigator
- Python 3 (rule conversion and automation)
- KQL (Azure Sentinel / Defender)

---

## Australian Context

- [ ] **DE02** — ASD Essential Eight Maturity Model logging requirements (application control, patch management logging)
- [ ] **DE02** — SOCI Act 2018 detection and monitoring obligations for critical infrastructure
- [ ] **DE04** — Reference ASD ACSC advisories for detection validation scenarios
- [ ] **DE05** — Australian threat landscape context for detection prioritisation decisions
- [ ] **DE06** — Capstone scenario should reference an ACSC-identified threat group or advisory

---

## Capstone Unit (DE06) Requirements

The capstone must produce a **tested detection rule library**:

- [ ] Scope defined: a specific threat scenario (e.g., ransomware pre-deployment activity, APT lateral movement)
- [ ] Data source mapping documented (which logs are required)
- [ ] Minimum 10 Sigma rules written and documented
- [ ] All rules tested using Atomic Red Team or equivalent (evidence of testing required)
- [ ] False positive analysis conducted and documented
- [ ] Coverage map produced in ATT&CK Navigator
- [ ] Detection library exported in Sigma format (ready for deployment)
- [ ] Community practitioner review of the rule library
- [ ] Deliverable suitable for professional portfolio (reference `templates/student-portfolio/index.html`)

---

## Sign-off Requirements

Before any unit can be merged:

- [ ] Domain Expert with active detection engineering experience named in metadata
- [ ] Practitioner Reviewer (different from Domain Expert) named in metadata
- [ ] Sigma rules in labs validated for correctness against current Sigma specification
- [ ] ATT&CK technique references verified against latest ATT&CK version
- [ ] Atomic Red Team test IDs verified as current

See `templates/review-checklist.md` for the full pre-merge checklist.
