# Sprint Plan — Open Source Cybersecurity Degree (Australia)

This plan converts the scattered `TODO.md` backlog across the repository into
time-boxed, deliverable-focused sprints. It is derived from the root `TODO.md`
phase status and the per-directory TODO files in `core/`, `degrees/`, `docs/`,
and `templates/`.

> **Convention:** Each sprint has a goal, a definition of done, and a checklist.
> Units are authored against `templates/unit-template.md` and must satisfy the
> 10-point completion bar in the root `TODO.md` and `docs/content-standards.md`.

---

## Sprint 1 — Foundation Year Content (Phase 2 Priority)

**Goal:** Author all six Foundation Year units (F01–F06) to template-complete
Draft status so the shared first year of both degrees has real content.

**Source TODOs:** root `TODO.md` §1, `core/units/TODO.md`.

**Deliverables**
- [x] `core/units/F01-networking-fundamentals.md`
- [x] `core/units/F02-operating-systems.md`
- [x] `core/units/F03-scripting-automation.md`
- [x] `core/units/F04-security-concepts.md`
- [x] `core/units/F05-legal-ethics-compliance.md`
- [x] `core/units/F06-data-log-analysis.md`
- [x] `core/units/README.md` status table updated `Planned → Draft`

**Status:** ✅ Complete — all six Foundation units authored to Draft (2026-06-21).

**Definition of done:** Each unit has ≥6 substantive topics, ≥2 complete labs
(free/OSS tools only), formative + summative assessment with a 4-level rubric,
≥2 framework mappings (incl. ASD CSF), an Australian context section, and ≥5
annotated references with ≥1 Australian source.

---

## Sprint 2 — Operational Core Content

**Goal:** Author the six Operational Core units (OC01–OC06) — the operational
half of Year 2.

**Source TODOs:** root `TODO.md` §2, `core/units/TODO.md`.

**Deliverables**
- [x] `core/units/OC01-adversary-tradecraft.md`
- [x] `core/units/OC02-security-monitoring-siem.md`
- [x] `core/units/OC03-malware-analysis.md`
- [x] `core/units/OC04-incident-response-lifecycle.md`
- [x] `core/units/OC05-threat-intelligence-fundamentals.md` *(Priority Intelligence Requirements — Red Hat PIR process per SANS CTI material)*
- [x] `core/units/OC06-offensive-security-concepts.md`
- [x] `core/units/README.md` status table updated

**Definition of done:** As Sprint 1, but Bloom's levels 3–4 (Apply/Analyse) and
framework coverage incl. NICE DCWF Protect & Defend / Investigate + SFIA 9.

**Status:** ✅ Complete — all six Operational Core units authored to Draft
(2026-06-21). Threat-informed defense (MITRE ATT&CK + CTID) is the connective
thread across all six units per practitioner direction.

---

## Sprint 3 — Strategic Core Content

**Goal:** Author the six Strategic Core units (SC01–SC06) — the strategic half
of Year 2.

**Source TODOs:** root `TODO.md` §3, `core/units/TODO.md`.

**Deliverables**
- [x] `core/units/SC01-risk-management-frameworks.md`
- [x] `core/units/SC02-security-architecture.md`
- [x] `core/units/SC03-governance-policy-compliance.md`
- [x] `core/units/SC04-vendor-supply-chain-risk.md`
- [x] `core/units/SC05-security-program-management.md`
- [x] `core/units/SC06-stakeholder-communication.md`
- [x] `core/units/README.md` status table updated

**Status:** ✅ Complete — all six Strategic Core units authored to Draft
(2026-06-21). Frameworks per practitioner direction: NIST CSF 2.0 + ISO 27001
backbones, SABSA/Zero Trust/SP 800-160 for SC02, APRA CPS 234/CPS 230 + SOCI +
ISM/IRAP, and a **compliance-as-revenue** thread (IRAP→gov, SOC 2/APRA→finance,
ISO 27001 broad) woven through SC01, SC03, SC05, and SC06.

> **Milestone:** All 18 shared core units (Foundation + Operational + Strategic)
> are now authored to Draft. The shared curriculum spine of both degrees is
> complete. Remaining: Sprint 4 (infrastructure), Sprint 5 (docs), Sprint 6+
> (48 major units).

---

## Sprint 4 — Contribution Infrastructure

**Goal:** Make the project safe for multiple contributors so unit-authoring can
scale beyond the maintainers.

**Source TODOs:** root `TODO.md` "Contributing Infrastructure".

**Deliverables**
- [x] Issue templates: "New Unit Draft", "Unit Review Request", "Framework Mapping Error" (+ `config.yml`)
- [x] `STATUS.md` dashboard showing every unit's lifecycle status (linked from README)
- [x] Contributor onboarding checklist (`docs/contributor-onboarding.md`)
- [x] Unit-assignment register (`docs/unit-assignments.md`)
- [x] GitHub Actions CI to lint unit files against required template sections (`.github/scripts/lint_units.py` + `.github/workflows/lint-units.yml`)

**Status:** ✅ Complete (2026-06-21). The unit linter validates all 18 existing
units (required sections, ≥6 topics, ≥2 labs, 4-level rubric, ≥5 annotated refs
incl. an Australian source, ASD mapping, metadata fields, no leftover
placeholders) and runs on every PR touching unit files.

---

## Sprint 5 — Documentation Gaps

**Goal:** Close the documentation gaps that block accreditation work.

**Source TODOs:** root `TODO.md` "Documentation Gaps", `docs/*/TODO.md`.

**Deliverables**
- [x] Verify `docs/frameworks.md` tables against latest versions — currency table + review log; ATT&CK flagged as likely superseded
- [x] Expand `docs/accreditation.md` TEQSA pathway section — routes, HESF evidence mapping, provider-readiness checklist
- [x] Define disputed-content escalation process in `docs/governance.md` (§5.1)
- [x] Live unit status dashboard in root `README.md` (summary table → `STATUS.md`)

**Status:** ✅ Complete (2026-06-21).

---

## Sprint 6+ — Major Units (Phase 3)

**Goal:** Author the 8 majors × 6 units = 48 major-unit files.

**Source TODOs:** `degrees/**/TODO.md`.

Sequenced one major per sprint after the shared core is complete. Bloom's levels
4–5 (Analyse/Evaluate), capstones 5–6 (Evaluate/Create); major units may reference
paid tools provided a free alternative is documented.

### Sprint 6 — Threat Hunting major ✅ Complete (2026-06-21)

- [x] `TH01-hunting-methodology-process.md` (TaHiTI, hypothesis design, maturity)
- [x] `TH02-attack-for-hunters.md` (ATT&CK v19, Navigator, CTID prioritisation)
- [x] `TH03-host-based-hunting.md` (Velociraptor VQL, Volatility 3)
- [x] `TH04-network-based-hunting.md` (Zeek/Wireshark, beaconing, DNS exfil)
- [x] `TH05-hunt-operations-tooling.md` (Jupyter/Pandas, fleet VQL, Sigma)
- [x] `TH06-capstone-hunt-operation.md` (end-to-end capstone, Bloom's 5–6, 24 CP)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Free/OSS tooling throughout; threat-informed-defense spine continued; ATT&CK
**v19** used (technique IDs provisional pending the repo-wide v19 audit).

### Sprint 7 — DFIR major ✅ Complete (2026-06-21)

- [x] `DF01-dfir-process-legal-foundations.md` (PICERL/800-61, Evidence Act 1995)
- [x] `DF02-host-forensics.md` (Autopsy/Sleuth Kit, MFT/registry, Plaso timelines)
- [x] `DF03-memory-forensics.md` (Volatility 3, injection, credentials)
- [x] `DF04-network-forensics.md` (Wireshark/Zeek, C2, DNS exfil)
- [x] `DF05-incident-response-operations.md` (PICERL ops, NDB/APRA/SOCI, TheHive)
- [x] `DF06-capstone-ir-simulation.md` (end-to-end IR, Bloom's 5–6, 24 CP)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Strongest AU-legal major: Evidence Act 1995 admissibility throughout, full
NDB/APRA CPS 234/SOCI notification coverage, and Optus/Medibank/Latitude case
studies. Free/OSS tooling; ATT&CK v19 (technique IDs provisional pending audit).

### Sprint 8 — CTI major ✅ Complete (2026-06-21)

- [x] `CT01-intelligence-tradecraft.md` (intelligence cycle, PIRs, OPSEC)
- [x] `CT02-threat-actor-research-profiling.md` (Diamond Model, ATT&CK, attribution method)
- [x] `CT03-technical-intelligence.md` (IOC enrichment, infrastructure pivoting)
- [x] `CT04-strategic-intelligence.md` (geopolitics, sector risk, exec briefings)
- [x] `CT05-cti-platforms-sharing.md` (STIX 2.1/TAXII, MISP/OpenCTI, CTID)
- [x] `CT06-capstone-intelligence-product.md` (full cycle, Bloom's 5–6, 24 CP)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Builds on OC05 PIR work; teaches attribution **methodology, not verdicts**; AU
context via ASD reports, QUAD, TISN. Free/OSS tooling; ATT&CK v19 (provisional).

### Sprint 9 — Detection Engineering major ✅ Complete (2026-06-21)

- [x] `DE01-detection-theory-philosophy.md` (Pyramid of Pain, detection-as-code)
- [x] `DE02-data-sources-log-engineering.md` (data modelling, coverage audit)
- [x] `DE03-writing-detection-logic.md` (Sigma, SPL, KQL, YARA)
- [x] `DE04-adversary-simulation-detection.md` (Atomic Red Team, testing pipeline)
- [x] `DE05-detection-operations-management.md` (metrics, tuning, lifecycle)
- [x] `DE06-capstone-detection-library.md` (tested 10+ rule library, Bloom's 5–6)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Completes the operational "detect" triad with TH and CTI; builds on OC02 Sigma/
ATT&CK work. NIST CSF 2.0 Detect mapping; Essential Eight logging; ATT&CK v19
(provisional). Free/OSS tooling throughout.

### Sprint 10 — Leadership & CISO major ✅ Complete (2026-06-21)

Authored ahead of CTE/SOC-CMM at maintainer direction, with a deliberate **full
emphasis on security program management and risk**.

- [x] `LD01-ciso-role-function.md` (mandate, reporting, risk ownership, APRA CPS 234)
- [x] `LD02-security-strategy-roadmapping.md` (maturity, roadmap, investment case)
- [x] `LD03-communicating-risk-to-executives.md` (board risk narrative, dashboards)
- [x] `LD04-building-leading-security-teams.md` (team design, AU talent, retention)
- [x] `LD05-crisis-management-comms.md` (NDB/APRA/SOCI/ASX notification, media)
- [x] `LD06-capstone-ciso-simulation.md` (board strategy + budget, Bloom's 5–6)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Bloom's 4–6 (activity-based, not lab-heavy); NICE DCWF 901/722/752 + SFIA MANA
L6–7 + ASD CSF; extensive AU regulatory context (APRA, ASX CGP, OAIC, SOCI).
Flagged for review by current/former CISOs per the major's high practitioner
dependency.

### Sprint 11 — Capability Maturity Integration ✅ Complete (2026-06-21)

Broadened from SOC-CMM alone to **all the operational capability maturity models**,
integrated across operations **and** strategy so operational and strategic
development stay aligned (no mismatch). Per maintainer direction, includes SOC-CMM,
CTI-CMM, SIM3 (IR/DFIR), Hunting Maturity Model/PEAK, DML/M3TID, and program models
C2M2/O-ISM3/CMMI — tied **service/capability → maturity model → NIST CSF 2.0 →
NICE/DCWF role → KSATs**.

- [x] `docs/maturity-models.md` — NEW canonical cross-walk (operational + strategic
  capabilities → model → CSF → role → KSATs; §4 wires operational maturity into
  SC01 risk, SC03 governance, SC05 program management, LD02 strategy)
- [x] `docs/frameworks.md` — maturity models added to index, a Capability Maturity
  Models section, and the currency table
- [x] Operational anchors cite their model: OC02 (SOC-CMM), OC04 (SIM3), OC05
  (CTI-CMM), DE01 (DML/M3TID)
- [x] Strategic anti-mismatch wiring: SC01 (maturity gaps as risk inputs), SC03
  (C2M2/O-ISM3 governance), SC05 (program maturity aggregates capability maturity),
  LD02 (roadmap targets named operational maturity)
- [x] README governance table links the new doc; all 48 units still pass the linter

> **Confirmation flag:** no canonical **"DF-C2M2"** found; SIM3 used as the IR/DFIR
> maturity model. Maintainer to confirm the intended "DF-C2M2" source.

### (superseded) original SOC-CMM-only scope

**Goal:** Integrate the **SOC-CMM** (SOC Capability Maturity Model) across the
**whole project — every relevant section**, not just the framework docs. Per
maintainer direction, explicitly tie:

- SOC-CMM **service offerings** → **capabilities** →
- **NIST CSF 2.0** functions →
- **NIST NICE / DCWF** work roles and **KSATs** (Knowledge, Skills, Tasks,
  Abilities).

Planned deliverables:
- Add SOC-CMM to `docs/frameworks.md` (index, mapping section, currency table).
- New `docs/soc-cmm-alignment.md`: degree-wide map of SOC-CMM domains
  (Business/People/Process/Technology) and **Services** → degree units/majors →
  NIST CSF functions → NICE/DCWF roles + KSATs.
- Weave SOC-CMM service→capability→role/KSAT references into the relevant units
  (OC02, OC04, OC05, DE05, SC05, and the operational majors' service-aligned units).
- Update README framework section and link the alignment doc.

### Sprint 12 — Cyber Threat Emulation major ✅ Complete (2026-06-21)

Completes the **Operational degree** (5/5 majors). Authored authorisation-first,
isolated-lab-only, and detection-outcome-focused per the major's content-safety
rules (highest dual-use sensitivity):

- [x] `CE01-offensive-foundations-ethics.md` (authorised testing, Criminal Code Act
  1995 Part 10.7, RoE, TIBER-AU)
- [x] `CE02-red-team-operations.md` (C2 concepts via OSS Sliver/Havoc, OPSEC,
  detection-aware tradecraft)
- [x] `CE03-attack-based-emulation.md` (CTID emulation plans, ATT&CK v19, M3TID)
- [x] `CE04-purple-team-operations.md` (collaborative testing, detection-gap analysis)
- [x] `CE05-reporting-debrief.md` (technical + executive reporting, TIBER-AU)
- [x] `CE06-capstone-emulation-exercise.md` (full emulation op w/ detection team, Bloom's 5–6)
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

Free/OSS tooling; NICE DCWF 711/511 + SFIA PENT L4–5 + ASD CSF; ties into M3TID/
SOC-CMM maturity (`docs/maturity-models.md`). Flagged for dual-use review.

### Sprint 13 — Security Engineering major ✅ Complete (2026-06-21)

- [x] `SE01-secure-system-design.md` (secure SDLC, threat modelling, SP 800-160)
- [x] `SE02-security-architecture.md` (applied SABSA, Zero Trust, cloud, ISM/IRAP)
- [x] `SE03-identity-access-management.md` (IAM/PAM, federation, MFA, Keycloak)
- [x] `SE04-detection-response-engineering.md` (SIEM/SOAR/XDR platform engineering)
- [x] `SE05-security-cloud-devsecops.md` (IaC/Checkov, containers, CI/CD, Semgrep)
- [x] `SE06-capstone-architecture-design.md` (secure architecture, Bloom's 5–6)
- [x] **Closed the Security-Engineering maturity gap:** added **SSE-CMM (ISO/IEC
  21827) + BSIMM + OWASP SAMM** to the units and `docs/maturity-models.md` +
  `docs/frameworks.md`
- [x] README/STATUS/assignments/TODO updated; all six pass the CI linter

### Sprint 14 — GRC major ✅ Complete (2026-06-21)

- [x] `GR01-security-governance-design.md` (policy hierarchy, RACI, CSF Govern, APRA)
- [x] `GR02-risk-management-in-practice.md` (register, bow-tie, appetite, ISO 27005)
- [x] `GR03-compliance-frameworks.md` (ISO 27001:2022, NIST CSF 2.0, Essential Eight)
- [x] `GR04-australian-regulatory-environment.md` (Privacy/NDB, APRA, SOCI, regulators)
- [x] `GR05-audit-assurance.md` (control testing, internal audit, IRAP, ASAE 3402)
- [x] `GR06-capstone-grc-program-design.md` (full GRC program, Bloom's 5–6)
- [x] Added GRC maturity (OCEG GRC Capability Model, RIMS RMM) to the cross-walk
- [x] README/STATUS/assignments/TODO updated; all 66 units pass the CI linter

> 🎓 **MILESTONE: All 66 units across both degrees authored to Draft.** Phase 3
> complete. The project now moves to **Phase 4**: practitioner review (Domain Expert
> + Practitioner Reviewer + Framework Custodian sign-off), independent framework
> verification, and the AQF Level 7 gap analysis — work that needs real practitioners
> rather than authoring.

### Phase 4 (next — not authoring)

- Practitioner review of each major (root `TODO.md` Phase 4)
- Framework mappings independently verified — including the **ATT&CK v19 audit** and
  NICE/DCWF T-code confirmation already tracked in `TODO.md`
- AQF Level 7 gap analysis
- Confirm flagged items: exact SANS PIR-guide citation (OC05) and the "DF-C2M2"
  reference (`docs/maturity-models.md`)

---

## Phase 4 — Infrastructure & Review Scaffolding

These post-authoring sprints harden the project for practitioner review and
future metrics. They do not author new units.

### Sprint 15 — MkDocs publishing ✅ Complete (2026-06-22)

- [x] All 66 units + new docs added to `mkdocs.yml` explicit nav
- [x] `.github/prepare_wiki.py` staging into `wiki_src/`; deploy workflow to Pages
- [x] Verified with `mkdocs build --strict` (exit 0); fixed a broken anchor

### Sprint 16 — Deepen quality automation ✅ Complete (2026-06-22)

- [x] Rewrote `.github/scripts/lint_units.py` with ERROR/WARNING severity split
- [x] NICE T-code traceability errors; cross-file prerequisite existence + acyclic graph
- [x] Advisory warnings: Bloom's verb level (one-level tolerance), framework-version
      consistency, internal-link resolution
- [x] `contributor-onboarding.md` updated to describe the checks

### Sprint 17 — NICE/DCWF KSAT mapping ✅ Complete (2026-06-23)

Goal: enumerate the **Knowledge, Skills, Abilities, and Tasks** developed in
*every* unit, each tied to evidence, so coverage maps can be generated for future
metrics on the education delivered.

- [x] `### NICE/DCWF KSATs` subsection spec added to `docs/content-standards.md`
- [x] `.github/scripts/ksat_coverage.py` — generates `docs/ksat-coverage.md`
      (totals, by-layer, by-unit, work-role, full KSAT index)
- [x] Linter advisory WARNING for a missing/empty KSAT subsection
- [x] `docs/ksat-coverage.md` added to the MkDocs nav
- [x] **Foundation tranche** — KSATs authored for F01–F06
- [x] **Operational Core tranche** — OC01–OC06
- [x] **Strategic Core tranche** — SC01–SC06
- [x] **Major tranches** — TH, DF, CT, DE, CE, SE, LD, GR (48 units)

> **655 KSAT items across 66/66 units** (261 Knowledge · 132 Skills ·
> 132 Abilities · 130 Tasks). Task rows reuse each unit's existing NICE/DCWF
> T-codes. Knowledge/Skill/Ability IDs are project-local and provisional pending
> Framework Custodian mapping to official NICE/DCWF identifiers (tracked for
> Phase 4 verification). Coverage map: `docs/ksat-coverage.md`.

### Sprint 18 — Program Builder ✅ Complete (2026-06-23)

Goal: let a student or designer compose a program — from a designed-degree
preset, one or more majors, or arbitrary individual courses — and see the
education it delivers as Mermaid visualisations, building on the Sprint 17 KSAT
data.

- [x] `.github/scripts/program_builder.py` — selection engine (presets,
      `--degree`, `--major`, `--units`, `--core/--no-core`) over the live KSAT data
- [x] Horizontal bar chart of **NICE/DCWF work-role completion %** per selection
- [x] **Four radar ("spider web") charts** — Knowledge, Skills, Abilities, Tasks —
      Selected vs Catalogue across every degree domain
- [x] Extra diagrams: KSAT-composition pie + program-structure flowchart
- [x] Every chart backed by a plain table (survives non-rendering viewers)
- [x] All four Mermaid types validated (`xychart-beta horizontal`, `radar-beta`,
      `pie`, `flowchart`)
- [x] Six example programs generated under `docs/program-builder/` + an index;
      wired into the MkDocs nav; `mkdocs build --strict` passes

> Mermaid radar requires v11.6+ and xychart v10.3+; the backing tables make the
> data legible regardless. Regenerate examples with
> `python3 .github/scripts/program_builder.py --build-docs`.

### Sprint 19 — Program Builder goes live (interactive) ✅ Complete (2026-06-23)

Goal: replace the per-preset **static generated pages** with a single
**interactive page** — tick courses and watch the KSAT coverage diagrams update
in real time, with no per-selection tooling or rebuild.

- [x] `.github/scripts/program_builder_app.js` — dependency-free vanilla-JS app:
      searchable course picker grouped **degree → year → major** (select-all per
      group, presets, search), live SVG charts
- [x] Live **NICE/DCWF work-role completion** bars + **four radar/"spider web"
      charts** (K/S/A/T, Selected vs Catalogue) + composition donut + summary
- [x] `program_builder.py` reduced to a one-shot **dataset embedder**: parses the
      units and writes a self-contained `docs/program-builder/index.md` (data +
      app inlined) — refreshed only when unit content changes
- [x] Removed the six static preset pages; nav collapsed to one page
- [x] Confirmed raw `<script>`/`<div>` survive the MkDocs build; verified the
      embedded JSON parses and the render path runs without error (DOM-shim smoke
      test); `mkdocs build --strict` passes

> Self-contained and offline-friendly: no CDN, no external JS, no asset-staging
> changes (charts are hand-drawn SVG). Loads showing the Operations degree by
> default. Refresh the embedded dataset with
> `python3 .github/scripts/program_builder.py`.

### Sprint 20 — Employability lenses + save / load / print ✅ Complete (2026-06-23)

Goal: the four radars were near-identical (K/S/A/T over the same academic
domains). Re-base them on *different* category systems that answer **"what can I
employ this person to do?"**, and add save / load / print.

- [x] Four radars now use four **different** category systems, each a Selected-vs-
      Catalogue lens:
      1. **Operational capabilities / use-cases** (Detect, Respond, Hunt,
         Forensics, Intelligence, Emulate, Architect, Govern/Risk, Lead…) —
         a curated, project-local capability mapping;
      2. **NICE/DCWF work categories** (Protect & Defend, Analyze, Investigate,
         Operate & Maintain, Securely Provision, Oversee & Govern);
      3. **Cognitive depth (Bloom's)** parsed from each unit's learning-outcome
         verbs (Remember → Create);
      4. **Knowledge vs doing** (K/S/A/T mix).
      Verified the four vectors produce distinct shapes (e.g. Ops degree is
      Protect-&-Defend/Analyze-heavy; Strategy is Securely-Provision/Oversee-heavy).
- [x] **Save / Load** the selection as JSON (`{format,version,name,savedAt,selected}`)
- [x] **Print report** — a standalone, print-formatted report (program name, date,
      summary, all four lens tables, work-role detail, selected courses, and the
      **full KSAT listing** for the program)
- [x] Embedded dataset extended with per-unit Bloom levels, capability tag, and
      the full KSAT items; `program_builder.py` updated accordingly
- [x] JS syntax-checked, render path + lens vectors verified under a DOM shim;
      `mkdocs build --strict` passes

> The capability mapping is curated and project-local (provisional), alongside the
> KSAT IDs, pending Framework Custodian review.

### Sprint 21 — Meaningful capability profile ✅ Complete (2026-06-23)

Goal: the K/S/A/T comparison was still uninformative (every radar a near-regular
shape, because each unit carries an almost constant K/S/A/T mix). Re-express the
four KSAT dimensions as an **employability profile** that actually varies.

- [x] New headline radar — **Capability profile**: *Knows · Can do · Unique · Has
      done* — each dimension binds its KSAT type to the matching Bloom band so the
      axes carry independent signal:
      Knows = Knowledge + Remember/Understand; Can do = Skills + Apply;
      Has done = Tasks + Analyse; **Unique = Abilities + Evaluate/Create**
      (distinctive higher-order judgement, which tracks program depth).
- [x] All radars now plot **this program as a fraction of the full catalogue**
      (catalogue = outer reference ring), so the shape shows relative emphasis and
      skew rather than just "the catalogue is bigger". E.g. a Foundation-only
      selection is visibly knowledge-leaning with a thin *Unique* corner; full
      degrees fill out.
- [x] Donut and report relabelled with the plain-language meanings
      (knows / can do / unique / has done); profile added to the print report.
- [x] Verified the profile differentiates programs; `mkdocs build --strict` passes.

> Note: the published Pages deploy of Sprint 20 succeeded; a stale screenshot of
> the pre-Sprint-20 "KSAT coverage by domain" radars prompted this further
> sharpening of the K/S/A/T story.

### Sprint 22 — Team coverage overlay ✅ Complete (2026-06-23)

Goal: extend the builder from one person to a whole **team**, overlaying members'
radars to check coverage — with overlap shown as opacity.

- [x] New page `docs/program-builder/team.md` + `program_builder_team_app.js`:
      add members and build each one's program, or **Load member(s)** from the
      individual Program Builder's saved JSON.
- [x] **Overlay radars** (all four lenses): each member is a translucent same-colour
      layer, so **overlap composites to opacity** — the shared core goes deep/opaque
      (everyone has it) and lone specialist areas stay faint; a dashed union outline
      shows the team's total reach, and each axis is annotated with how many members
      cover it (red `·0` = gap).
- [x] **Operational capability coverage table** flagging gaps / solo / redundant,
      plus a team summary (members, union catalogue %, capability gaps).
- [x] **Save / Load / Print** the whole team (`format: program-builder-team`); the
      member format is the same JSON the Program Builder saves.
- [x] Seeds an illustrative 3-member team on first view; JS syntax-checked, render
      path verified under a DOM shim; `mkdocs build --strict` passes.

### Sprint 23 — Phase 4 review scaffolding ✅ Complete (2026-06-23)

Goal: stand up the infrastructure to hand the curriculum to practitioners for
sign-off (the main remaining non-practitioner task).

- [x] **Review hub** `docs/review/index.md` — the lifecycle, roles, how to review
      a unit/major, and the repo-wide Phase 4 audits in one place.
- [x] **Generated review dashboard** `.github/scripts/review_dashboard.py` →
      `docs/review/dashboard.md` — live per-unit status + reviewer assignment from
      unit metadata, grouped by section/major (currently 66/66 Draft, 0 assigned).
- [x] **Framework verification tracker** `docs/review/framework-verification.md` —
      the Framework Custodian's per-unit checks, repo-wide audits (ATT&CK v19, KSAT
      ID mapping, capability mapping, DF-C2M2), and a per-major progress grid.
- [x] Wired into the nav; cross-linked from STATUS, TODO (Phase 4 items), and the
      existing issue templates / `templates/review-checklist.md`.
- [x] `mkdocs build --strict` passes; all links resolve.

> Built on the existing scaffolding (governance roles, content lifecycle, the
> `unit-review-request` / `framework-mapping-error` issue templates, and the
> review checklist) rather than duplicating it.

---

## Resource Inputs from Practitioners

This project is practitioner-led. Where a maintainer has a preferred real-world
process or reference, it is captured here and woven into the relevant unit
rather than reinvented.

| Topic / Unit | Practitioner-supplied resource | Status |
|---|---|---|
| Threat-informed defense (all OC units) | MITRE ATT&CK + MITRE CTID body of work as the organising philosophy; defence as a living system that adapts to changing adversary behaviour | ✅ Incorporated across OC01–OC06 |
| Priority Intelligence Requirements (OC05) | Red Hat **Priority Intelligence Requirements** (PIR) process, as referenced in the SANS CTI body of knowledge (FOR578) | ✅ Incorporated in OC05 — exact SANS guide citation to confirm at review |
| Blameless post-incident review (OC04) | Covered within OC04's lessons-learned topic (per maintainer scope) | ✅ Incorporated in OC04 |
| Strategic Core control backbones (SC01, SC03) | NIST CSF 2.0 (Govern/Identify) + ISO 27001:2022 | ✅ Incorporated in SC01–SC06 |
| Security architecture (SC02) | SABSA + Zero Trust (NIST SP 800-207) + NIST SP 800-160 | ✅ Incorporated in SC01–SC06 |
| Australian regulatory regimes (SC03, SC04, SC05) | APRA CPS 234 + SOCI risk-management program + Australian Government ISM / IRAP | ✅ Incorporated in SC01–SC06 |
| Compliance-as-revenue framing (SC03, SC05) | Position compliance as a commercial/market-access enabler ("frameworks that make money"); map framework choice to industry — **IRAP** for government, **SOC 2** and **APRA CPS 234** for finance/other industries, ISO 27001 broadly | ✅ Incorporated in SC01–SC06 — distinctive angle to weave through governance/program units |

| Capability maturity (all units) | Integrate **all** operational + program maturity models (SOC-CMM, CTI-CMM, SIM3, HMM/PEAK, DML/M3TID, C2M2, O-ISM3) across operations **and** strategy; tie service→capability→NIST CSF→NICE/DCWF role→KSATs; wire operational maturity into governance/program/risk to avoid development mismatch | ✅ Sprint 11 — `docs/maturity-models.md` ("DF-C2M2" name pending confirmation) |

*(Add rows as resources are supplied.)*
