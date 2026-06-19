# TODO — degrees/operational/

This directory contains the 5 majors for the **Bachelor of Cybersecurity Operations** (AQF Level 7):

| Major | Directory | Units |
|---|---|---|
| Threat Hunting | `threat-hunting/` | TH01–TH06 |
| Digital Forensics & Incident Response | `dfir/` | DF01–DF06 |
| Cyber Threat Intelligence | `cti/` | CT01–CT06 |
| Detection Engineering | `detection-engineering/` | DE01–DE06 |
| Cyber Threat Emulation | `cte/` | CE01–CE06 |

---

## Prerequisites

All operational majors require:
- Foundation Year (F01–F06) — complete before starting any major
- Operational Core (OC01–OC06) — complete before starting any major

Ensure both sets of core units are at least **Practitioner Approved** before authoring major content that references them.

---

## Status

All 30 unit files across 5 majors are currently **Planned**.

---

## Shared Operational Considerations

### Tools Used Across Multiple Majors

Several tools appear across operational majors. Ensure consistent usage instructions:

| Tool | Used In |
|---|---|
| MITRE ATT&CK Navigator | TH, DE, CTE |
| Sigma | TH, DE, OC (core) |
| Velociraptor | TH, DFIR |
| Wireshark / Zeek | TH (network), DFIR (network forensics) |
| OpenCTI / MISP | CTI, CTE (debrief) |
| Python scripting | CTI (STIX), DE (automation), TH (notebooks) |

Where the same tool is used in multiple majors, consider creating a shared "tool reference" document in `core/` to avoid duplicating setup instructions.

### Australian Legal Context (Required in Each Major)

| Major | Required Australian Context |
|---|---|
| Threat Hunting | ASD Essential Eight, SOCI Act detection obligations |
| DFIR | Evidence Act 1995, NDB scheme, APRA notification timelines |
| CTI | ASD Annual Cyber Threat Report, ACSC partnerships, TISN |
| Detection Engineering | ASD Essential Eight logging requirements, SOCI Act |
| CTE | TIBER-AU framework, authorised testing legal scope |

---

## Content Authoring Order

Recommended sequence based on tool/concept dependencies:

1. **DFIR** — foundational to other majors; IR process feeds TH and DE
2. **Detection Engineering** — Sigma and detection logic feeds TH
3. **Threat Hunting** — builds on detection, SIEM, and DFIR concepts
4. **CTI** — builds on adversary knowledge from TH and DFIR
5. **Cyber Threat Emulation** — requires OC06 (Offensive Security Concepts) maturity and benefits from all others

---

## Capstone Coordination

All 5 operational capstones (TH06, DF06, CT06, DE06, CE06) must be:

- [ ] Practical exercises in lab or simulated environments
- [ ] Documented with a written report template suitable for professional portfolios
- [ ] Reviewed by at least one practitioner volunteer from the community
- [ ] Referenced in `templates/student-portfolio/index.html` so graduates can showcase the work

Consider whether the 5 operational capstones can use a **shared live-fire lab range** — one environment supporting TH, DFIR, DE, and CTE scenarios reduces setup overhead.

---

## Quality Checklist for Each Operational Major

Before publishing any major:

- [ ] All 6 unit files authored (using `templates/unit-template.md`)
- [ ] Each unit has correct Bloom's taxonomy level (Levels 4–5 for major units: analyse, evaluate)
- [ ] Each unit has MITRE ATT&CK mapping where applicable
- [ ] Each unit has ASD Cyber Skills Framework mapping
- [ ] All lab tools are free or open-source
- [ ] At least 8 total labs across the major
- [ ] Australian legal or regulatory context in at least 1 unit
- [ ] Capstone deliverable documented and portfolio-ready
- [ ] Domain Expert + Practitioner Reviewer sign-off on all units
- [ ] README.md unit status table updated
