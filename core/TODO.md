# TODO — core/

This directory contains all shared unit content: Foundation Year (F01–F06), Operational Core (OC01–OC06), and Strategic Core (SC01–SC06). These are the prerequisite units all students complete before entering a major.

---

## Status

All 18 units in this directory are currently **Planned** — no unit files have been authored yet.

---

## What Needs to Be Done

### Step 1 — Create the unit file structure

Create a subdirectory structure inside `core/units/` to organise units by layer:

```
core/units/
├── foundation/        ← F01–F06
├── operational-core/  ← OC01–OC06
└── strategic-core/    ← SC01–SC06
```

Alternatively, keep units flat in `core/units/` with the unit code prefix. Either approach is acceptable — decide and document in `core/units/README.md` before authoring begins.

### Step 2 — Author Foundation Year Units (Priority: Highest)

Foundation units must be completed first because all students require them before proceeding to either the Operational or Strategic degree core. Author in this recommended order:

1. [ ] `F01-networking-fundamentals.md` — TCP/IP, protocols, Wireshark, nmap, tcpdump
2. [ ] `F02-operating-systems.md` — Windows + Linux admin, CLI, OS internals, Sysinternals
3. [ ] `F04-security-concepts.md` — CIA triad, threat modelling, STRIDE, control categories
4. [ ] `F03-scripting-automation.md` — Python 3, Bash, PowerShell, structured data parsing
5. [ ] `F06-data-log-analysis.md` — SIEM fundamentals, Splunk/OpenSearch/Elastic, Sigma basics
6. [ ] `F05-legal-ethics-compliance.md` — Privacy Act 1988, SOCI Act, NDB scheme, ASD/ACSC/APRA/OAIC

### Step 3 — Author Operational Core Units

Complete after all F01–F06 units are in Practitioner Approved status:

1. [ ] `OC01-adversary-tradecraft.md` — MITRE ATT&CK, kill chain, actor profiling
2. [ ] `OC02-security-monitoring-siem.md` — Detection at scale, SIEM use case development
3. [ ] `OC03-malware-analysis.md` — Static + dynamic analysis, sandbox tools, IOC extraction
4. [ ] `OC04-incident-response-lifecycle.md` — PICERL, containment, eradication, recovery
5. [ ] `OC05-threat-intelligence-fundamentals.md` — CTI lifecycle, STIX/TAXII, feeds
6. [ ] `OC06-offensive-security-concepts.md` — Recon, exploitation concepts, C2 frameworks

### Step 4 — Author Strategic Core Units

Complete in parallel with or after Operational Core. Strategic students can start these once foundation is done:

1. [ ] `SC01-risk-management-frameworks.md` — NIST RMF, ISO 27005, bow-tie analysis
2. [ ] `SC02-security-architecture.md` — SABSA, Zero Trust, defence-in-depth
3. [ ] `SC03-governance-policy-compliance.md` — Policy design, control frameworks
4. [ ] `SC04-vendor-supply-chain-risk.md` — Third-party risk, SCRM methodologies
5. [ ] `SC05-security-program-management.md` — Roadmaps, metrics, stakeholder management
6. [ ] `SC06-stakeholder-communication.md` — Board reporting, risk communication, executive briefings

---

## Per-Unit Requirements Checklist

Each unit file must include (per `templates/unit-template.md`):

- [ ] Status block (Draft → Under Review → Practitioner Approved → Framework Verified → Published)
- [ ] Overview (1–2 paragraphs with Australian context)
- [ ] Prerequisites (unit codes)
- [ ] 5–8 Learning Outcomes with correct Bloom's taxonomy verbs
  - Foundation units: Levels 1–3 (define, explain, demonstrate)
  - Core units: Levels 3–4 (apply, analyse)
- [ ] AQF Level 7 Alignment (Knowledge, Skills, Application)
- [ ] Framework Mappings (NIST NICE DCWF T-codes, SFIA 9, ASD CSF — minimum 2 frameworks, 1 Australian)
- [ ] Minimum 6 substantive topics (no placeholder headings — actual content required)
- [ ] Minimum 2 complete labs (objective, prerequisites, environment spec, steps, expected output, reflection questions)
  - All tools must be free/open-source for Foundation and Core units
  - Minimum hardware spec: 8 GB RAM, 4-core CPU, 50 GB disk
- [ ] Formative assessment + Summative assessment with 4-level rubric
- [ ] Australian Context section (AU legislation, regulator, case study, or framework)
- [ ] Minimum 5 annotated references (at least 1 Australian source)
- [ ] Unit metadata table (all fields completed)
- [ ] Domain Expert sign-off
- [ ] Practitioner Reviewer sign-off

---

## Contributor Notes

- Assign yourself to a unit by opening a GitHub issue before starting to avoid duplication
- All tools referenced in Foundation and Core labs MUST be free or open-source (no commercial licences required)
- Do not merge a unit until both Domain Expert and Practitioner Reviewer are named in the metadata
- Reference `docs/content-standards.md` for the complete authoring guide
- Reference `docs/compliance/aqf-teqsa.md` for AQF Level 7 descriptor definitions
- Reference `docs/compliance/workforce-frameworks.md` for valid NICE DCWF T-codes and SFIA format
