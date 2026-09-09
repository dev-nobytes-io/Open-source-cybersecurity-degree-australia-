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
      eligibility criteria. If the restriction holds, [SPL-06](modules/splunk/spl-06-consultant.md)
      is content without a reachable credential and must say so plainly.
- [ ] Confirm whether the Cybersecurity Defense **Engineer** and **Architect** exams have
      unpublished prerequisites — both pages currently state none, despite sitting above
      the Analyst in the marketing sequence.

**Content reconciliation:**

- [ ] Reconcile SPL-01…SPL-06 topic coverage against each certification's published
      **test blueprint** PDF. Current topic lists are the module author's reading of the
      platform, not a blueprint transcription.
- [ ] Confirm licence terms and current availability of the **BOTS datasets**,
      **`attack_range`**, and **Splunk Security Content / ESCU** before SPL-03 Labs 4–6
      are made assessable.
- [ ] Verify the "Great 8" `props.conf` settings named in SPL-06 Topic 2 against current
      courseware. No specific settings are listed until this is done.
- [ ] Recruit reviewers holding **current** Enterprise Certified Architect (for SPL-05)
      and Core Certified Consultant (for SPL-06) certifications. Neither module may reach
      Practitioner Approved without one.

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
