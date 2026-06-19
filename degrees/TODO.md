# TODO — degrees/

This directory contains all major-specific unit content for both the Operational and Strategic degree pathways. It is organised into two subdirectories:

- `degrees/operational/` — 5 operational majors
- `degrees/strategic/` — 3 strategic majors

---

## Overall Status

All 8 majors and all 48 unit files within them are currently **Planned**. No major unit content has been authored yet.

---

## Dependency: Complete Core Units First

Major units should only be authored after the relevant prerequisite units in `core/units/` are at least in **Draft** status. Do not author major units in isolation — they build directly on core unit content.

| Major Track | Prerequisite Core |
|---|---|
| All operational majors (TH, DFIR, CTI, DE, CTE) | F01–F06 + OC01–OC06 |
| All strategic majors (SE, Leadership, GRC) | F01–F06 + SC01–SC06 |
| Security Engineering (SE) | Benefits from OC01–OC06 as well |

---

## Authoring Order (Recommended)

Start with the majors that have the most community interest or the most volunteer practitioner authors. The suggested order below prioritises majors with clearly defined roles in the Australian market:

1. **DFIR** — well-defined toolset, strong practitioner community, clear AU legal context
2. **Detection Engineering** — high demand, Sigma-based content is well documented
3. **GRC** — directly tied to APRA CPS 234, Essential Eight, and ISO 27001 AU context
4. **Threat Hunting** — good practitioner volunteer pool, MITRE ATT&CK-led content
5. **CTI** — strong framework base (Diamond Model, STIX 2.1, MITRE CTID)
6. **Security Engineering** — broader scope, benefits from core units being mature
7. **Leadership & CISO** — content depends on real-world practitioner input
8. **Cyber Threat Emulation** — requires Offensive Security Concepts (OC06) to be mature first

---

## What Each Major Directory Needs

Each major directory currently has only a `README.md`. The following files need to be created in each:

```
degrees/operational/<major>/
├── README.md              ← Exists — review and update when units are authored
├── TODO.md                ← This file (exists in each major subdirectory)
├── <unit-code>-<title>.md ← 6 unit files per major — NOT YET CREATED
└── labs/                  ← Optional: separate lab environment files or scripts
```

---

## Cross-Major Considerations

- [ ] Identify content that overlaps between majors and consider whether it should live in `core/units/` instead (e.g., MITRE ATT&CK Navigator usage appears in TH, DE, and CTE)
- [ ] Ensure capstone units (unit 6 in each major) reference the portfolio template at `templates/student-portfolio/index.html`
- [ ] All capstone outputs must be documented deliverables suitable for a professional portfolio
- [ ] Each major must have at least 8 lab-based exercises total across 6 units (success criterion from `docs/goals.md`)
- [ ] Every major must cover Australian legislation or regulators in at least one unit

---

## Quality Gates Before Publishing Any Major

- [ ] All 6 unit files drafted and reviewed
- [ ] Each unit has Domain Expert + Practitioner Reviewer sign-off
- [ ] Framework mappings verified (T-codes traceable to lab steps)
- [ ] At least 8 labs across the major
- [ ] Capstone unit includes practitioner community review process
- [ ] README.md unit status table updated to reflect final statuses
