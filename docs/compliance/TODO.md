# TODO — docs/compliance/

This directory contains the compliance documentation that governs how units must be designed to meet Australian education standards and industry workforce frameworks.

**Files in this directory:**
- `aqf-teqsa.md` — AQF Level 7 + TEQSA HESF compliance requirements
- `program-delivery.md` — Delivery standards: accessibility, licensing, QA cycles
- `workforce-frameworks.md` — NICE/DCWF, SFIA 9, ASD framework mapping requirements

---

## aqf-teqsa.md

### What it needs to contain (verify completeness)

- [ ] AQF Level 7 descriptor — full knowledge, skills, and application of knowledge and skills descriptors (verbatim from AQF)
- [ ] Mapping of each descriptor to how the degree structure satisfies it
- [ ] TEQSA Higher Education Standards Framework (HESF) 2021 — which standards apply to this program
- [ ] Guidance for unit authors on how to write learning outcomes that satisfy AQF Level 7
- [ ] Bloom's taxonomy verb reference table for each degree layer:
  - Foundation (Levels 1–3): define, identify, describe, explain, demonstrate, classify
  - Core (Levels 3–4): apply, analyse, differentiate, examine, investigate
  - Major (Levels 4–5): analyse, evaluate, critique, recommend, compare, justify
  - Capstone (Levels 5–6): evaluate, create, design, construct, synthesise, develop, defend
- [ ] Assessment type guidance per AQF level (what types of assessment satisfy AQF Level 7 application requirement)

### Actions

- [ ] Verify the Bloom's verb table is complete and covers all levels
- [ ] Add cross-reference to how each foundation unit satisfies AQF 7.1 knowledge descriptors
- [ ] Add cross-reference to how each major unit satisfies AQF 7.2 skills descriptors
- [ ] Add cross-reference to how each capstone satisfies AQF 7.3 application descriptors
- [ ] Add a "self-assessment vs. TEQSA assessment" comparison table for transparency

---

## workforce-frameworks.md

### What it needs to contain (verify completeness)

- [ ] **NIST NICE DCWF** — Full list of valid Work Role codes and T-codes used in this degree; guidance on how to look up T-codes; current version reference (November 2023)
- [ ] **DoD 8140** — Mapping of relevant work roles to DoD 8140 cyberspace workforce categories
- [ ] **SFIA 9** — Guidance on which SFIA skills and levels apply at each degree layer; format for citing SFIA in unit files
- [ ] **ASD Cyber Skills Framework** — Current version; mapping of framework domains to degree majors; how to cite in unit files
- [ ] **CIISec Skills Framework** — Overview of relevant skill categories
- [ ] **Format specification** — Exact format for framework citation in unit files (table headers, column names) — must match `templates/unit-template.md`

### Actions

- [ ] Verify NIST NICE DCWF T-code list is from November 2023 publication
- [ ] Verify SFIA 9 skill codes are accurate (check against sfia.org)
- [ ] Verify ASD Cyber Skills Framework version — confirm 2024 version is referenced
- [ ] Add a "framework mapping worked example" section — show a complete, correct mapping for one unit
- [ ] Add guidance on what to do when a new framework version is released (versioning policy)
- [ ] Add a table showing which frameworks are mandatory vs. recommended for each degree layer

---

## program-delivery.md

### What it needs to contain (verify completeness)

- [ ] Licensing — CC BY 4.0 requirements; what attribution looks like; what derivative works must include
- [ ] Accessibility — WCAG 2.1 AA compliance requirements for any web-based content; alt text requirements for images; minimum contrast for diagrams
- [ ] QA cycles — Annual review schedule; trigger events for off-cycle review (major framework version change, significant AU legislation change)
- [ ] Versioning — How unit versions are numbered; what triggers a version increment; how learners know which version they studied
- [ ] Lab environment standards — Minimum hardware spec (8 GB RAM, 4-core CPU, 50 GB); OS requirements; how to document tool versions
- [ ] Tooling policy — Which tools are approved for Foundation/Core labs (free/OSS only); which tools are permitted in major labs; how to handle tool deprecation

### Actions

- [ ] Verify the minimum hardware spec is documented clearly with rationale
- [ ] Add guidance on how to update a unit when a tool version changes (e.g., Volatility 2 vs. 3)
- [ ] Add a versioning worked example — show how a unit file header changes from v0.1 Draft to v1.0 Published
- [ ] Add a trigger list for off-cycle review (major NIST publication, ASD Essential Eight revision, Privacy Act amendment, etc.)
- [ ] Clarify the accessibility standard for Mermaid diagrams (are they readable by screen readers?)
