# TODO — docs/

This directory contains all governance, compliance, curriculum, and reference documentation for the degree program. It is organised into subdirectories by audience and function.

---

## Directory Structure

```
docs/
├── accreditation.md          ← TEQSA/AQF alignment strategy
├── content-standards.md      ← Mandatory content standards for all units
├── frameworks.md             ← Framework-to-unit mapping tables
├── goals.md                  ← Vision, objectives, success criteria
├── governance.md             ← Governance model: roles, lifecycle, decisions
├── structure.md              ← Full degree architecture & unit design
├── compliance/               ← AQF, TEQSA, workforce framework compliance docs
├── curriculum/               ← Curriculum maps, delivery, micro-credentials, WIL
├── educator/                 ← Facilitator guide, assessment moderation, capstone supervision
├── institutional/            ← Graduate attributes, TLOs, benchmarking, equivalence, IAB
├── quality/                  ← Annual review schedule, equity & inclusion
└── student/                  ← Handbook, prospectus, academic integrity, RPL
```

---

## Root-Level Document Status

| File | Status | Action Required |
|---|---|---|
| `goals.md` | Complete (Phase 1) | Review when Phase 3 begins; update success criteria metrics |
| `structure.md` | Complete (Phase 1) | Update unit status table as units move through lifecycle |
| `frameworks.md` | Complete (Phase 1) | **Verify framework versions are current** — SFIA 9, NICE DCWF 2023, ATT&CK v14+, ASD CSF 2024 |
| `accreditation.md` | Exists — needs expansion | Expand TEQSA pathway section once Phase 3 content is complete |
| `governance.md` | Exists — needs expansion | Add escalation process for disputed content; define appeals process |
| `content-standards.md` | Exists — needs verification | Verify Bloom's verb lists are complete and accurate per AQF level |

---

## Immediate Actions

### frameworks.md — Version Check

All framework mapping tables in `frameworks.md` must reference specific versions:

- [ ] Verify NIST NICE DCWF references are against the **November 2023** publication
- [ ] Verify SFIA references are against **SFIA 9 (2023)**
- [ ] Verify MITRE ATT&CK references are against **v14 or later**
- [ ] Verify ASD Cyber Skills Framework references are against **2024 version**
- [ ] Verify NIST CSF references are against **CSF 2.0 (2024)**
- [ ] Verify ISO 27001 references are against **ISO 27001:2022** (not 2013)
- [ ] Add a "Last Verified" date to the framework version table

### governance.md — Process Gaps

- [ ] Define the escalation process for disputed framework mappings
- [ ] Define the appeals process if a unit is rejected in review
- [ ] Define what happens when a Domain Expert is no longer available (succession for unit ownership)
- [ ] Add a contributor recognition section (how contributors are credited)

### modules/splunk/ — EXT-SPL Splunk Series Verification

The series is written against official Splunk pages verified **2026-09-09**. Splunk is
now under Cisco ownership and the certification programme is actively changing, so these
items are time-sensitive.

**Blocking — must be resolved before advising any learner:**

- [ ] **Confirm `Core Consultant Labs` / `Services: Core Implementation` eligibility.**
      Practitioner reports say these are restricted to Splunk partners/employees and that
      `Core Consultant Labs` requires the Architect certification. Splunk publishes no
      eligibility criteria. If the restriction holds, [SPL-08](modules/splunk/spl-08-consultant.md)
      is content without a reachable credential and must say so plainly.
- [ ] Confirm whether the Cybersecurity Defense **Engineer** and **Architect** exams have
      unpublished prerequisites — both pages currently state none, despite sitting above
      the Analyst in the marketing sequence.

- [ ] **Confirm the successors to the Legacy certifications.** Splunk reclassified
      **ES Certified Admin** and **SOAR Certified Automation Developer** as Legacy on
      1 January 2026 and **names no replacement** for either. The series' position — that
      the Cybersecurity Defense track succeeds them for security work — is a reading, not
      a Splunk statement. [SPL-04](modules/splunk/spl-04-enterprise-security.md) and
      [SPL-05](modules/splunk/spl-05-soar.md) both flag this.
- [ ] **Confirm Splunk SOAR availability for learning use** (community edition, trial or
      developer licence) and its terms. [SPL-05](modules/splunk/spl-05-soar.md) labs are
      written so the highest-value ones run as design exercises without a platform, but
      availability must be settled before the module is scheduled.
- [ ] **Pin ES and SOAR product versions.** Neither SPL-04 nor SPL-05 is pinned, and both
      products change feature names and UI locations materially between releases.
- [ ] Record the **recertification change** (coursework-based recertification ends
      1 March 2026; three-year lifecycle from the highest-level certification) wherever the
      repo advises learners on certification pathways, including
      [`student/prospectus.md`](student/prospectus.md).

**Content reconciliation:**

- [x] ~~Reconcile SPL-01…SPL-08 topic coverage against each certification's published
      **test blueprint** PDF.~~ **Done 2026-09-09** — all eleven blueprints retrieved and
      mapped; every module carries a *Blueprint alignment* section with domain weightings.
      Corrected three material errors: SPL-08 was mis-framed (the Consultant exam is ~90%
      technical, not consulting practice), SPL-02 was missing the Advanced Power User's
      33% dashboard/Simple XML content, and lookups (Core User, 6%) and distributed search
      (Enterprise Admin, 10%) sat in the wrong modules.
- [ ] **Resolve the Consultant prerequisite-coursework discrepancy.** The blueprint names
      `Indexer Cluster Implementation Lab`, `Distributed Search Migration Lab`,
      `Implementation Fundamentals Lab`, `Architect Implementation Labs (1-3)` and
      `Services: Core Implementation`. The exam page and track flowchart name
      **`Core Consultant Labs`** as registration-mandatory; the blueprint omits it
      entirely. Both retrieved the same day.
- [ ] **Decide whether ITSI is in scope.** The Architect blueprint examines ITSI sizing and
      topology (domain 4.5) and the series does not cover it. The ITSI Certified Admin
      credential is also Legacy.
- [ ] Confirm licence terms and current availability of the **BOTS datasets**,
      **`attack_range`**, and **Splunk Security Content / ESCU** before SPL-03 Labs 4–6
      are made assessable.
- [ ] Verify the "Great 8" `props.conf` settings named in SPL-08 Topic 3 against current
      courseware. No specific settings are listed until this is done.
- [ ] Recruit reviewers holding **current** Enterprise Certified Architect (for SPL-07)
      and Core Certified Consultant (for SPL-08) certifications. Neither module may reach
      Practitioner Approved without one.

**Lab environment (`labs/`) — open items:**

- [ ] **Objective answer keys exist for five labs only** (`spl03.lab2`, `spl03.lab5`,
      `spl03.lab7`, `spl09.lab3`, `spl09.lab5`). The remaining 64 are rubric-marked.
      Decide whether more hash-checkable answers are wanted, and for which labs — the
      constraint is that a checkable answer tends to reward the answer over the method,
      which several of these labs deliberately grade the other way round.
- [ ] **The dataset's base rate is deliberately enriched** — about 0.2% of events belong
      to a scenario and roughly 10% of intermediate findings are malicious, against real
      rates orders of magnitude lower. Stated explicitly in
      [`labs/README.md`](../labs/README.md); confirm the Domain Expert accepts the
      teaching compromise, since [SPL-09](modules/splunk/spl-09-detection-analytics.md)
      Part B teaches the real arithmetic against a dataset that does not exhibit it.
- [ ] **The generator's DGA is uniform-random**, which is the case character entropy is
      optimal for. [SPL-09 Lab 5](../labs/guides/spl-09.md) now teaches this as a
      measurement artefact to diagnose rather than hiding it, but a more realistic DGA
      (dictionary-based, and hashed-but-benign CDN hostnames on the negative side) would
      make the lab better. Also absent: base32 tokens, UUID subdomains, DKIM selectors.
- [ ] **Sysmon carries EventCode 1 only.** This is deliberate — it is what makes
      [SPL-03 Lab 4](../labs/guides/spl-03.md)'s telemetry-gap classification real — but
      it caps what any endpoint-detection lab can do. Decide whether to add 3, 7, 11 and
      22 behind a generator flag so the gap can be opened and closed.
- [ ] **Docker environments are untested end to end in this repository.** The compose
      files are YAML-valid and the app configuration is written, but no CI job starts
      Splunk. Everything that could be verified without a running instance has been
      (dataset properties, answer keys, every embedded Python block); the container
      startup path has not.
- [ ] Confirm the Splunk container image licence terms are acceptable for the way the
      compose files use them (`SPLUNK_START_ARGS: --accept-license`), and that
      redistributing the compose files is within those terms.

**Cross-document consistency:**

- [ ] Update [`structure.md`](structure.md) and
      [`compliance/workforce-frameworks.md`](compliance/workforce-frameworks.md), which
      list *"Splunk Core Certified"* as a Detection Engineering certification bridge, to
      name the specific credential: **Splunk Core Certified Power User**. The same
      imprecise wording appears in [`student/prospectus.md`](student/prospectus.md).
- [ ] Add EXT-SPL re-verification to
      [`quality/annual-review-schedule.md`](quality/annual-review-schedule.md) — the
      series carries a **6-month** staleness window (due 2027-03-09), shorter than the
      annual cycle.

### accreditation.md — Expand Phase 5 Content

- [ ] Document the preliminary TEQSA pathway assessment (what is needed to apply for registration)
- [ ] Identify potential delivery partner universities for institutional recognition
- [ ] Map graduate attributes to AQF Level 7 descriptor table
- [ ] Document the gap between current "self-assessed" AQF alignment and formal TEQSA assessment

---

## Subdirectory Summary

See individual `TODO.md` files in each subdirectory for detailed action items:

| Subdirectory | Purpose | TODO |
|---|---|---|
| `compliance/` | AQF, TEQSA, workforce framework requirements | See `compliance/TODO.md` |
| `curriculum/` | Curriculum maps, delivery modes, micro-credentials, WIL | See `curriculum/TODO.md` |
| `educator/` | Facilitator guide, moderation, capstone supervision | See `educator/TODO.md` |
| `institutional/` | Graduate attributes, TLOs, benchmarking, equivalence | See `institutional/TODO.md` |
| `quality/` | Annual review, equity & inclusion | See `quality/TODO.md` |
| `student/` | Handbook, prospectus, academic integrity, RPL | See `student/TODO.md` |
