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
