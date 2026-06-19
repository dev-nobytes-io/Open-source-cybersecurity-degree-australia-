# TODO — templates/

This directory contains the mandatory templates that all contributors must use when authoring unit content, reviewing units, and building learner portfolios.

**Files in this directory:**
- `unit-template.md` — Mandatory template for all unit content files
- `review-checklist.md` — Pre-merge sign-off checklist for Domain Expert and Practitioner Reviewer
- `competency-profile-template.md` — Template for learners to build a framework-mapped competency profile
- `student-portfolio/` — HTML portfolio template for learners

---

## unit-template.md

### Current State

The unit template exists and is well-structured. The following improvements should be made as the project matures:

- [ ] **Add version history to the template itself** — when the template changes, existing units must be updated to match
- [ ] **Add worked examples as comments** — expand the inline comments in each section with concrete examples from a completed unit (not just instructions)
- [ ] **Clarify the DCWF T-code requirement** — add a worked example showing a complete, correct T-code mapping row with a lab reference
- [ ] **Add the "lab environment setup" sub-section** — every lab should have a "Setup" step before Instructions (install tools, configure environment)
- [ ] **Add a "common mistakes" appendix** — list the most common reasons units fail review (placeholder headings left in, T-codes not traceable to labs, etc.)
- [ ] **Add a changelog section** to the template — unit authors must record what changed between versions
- [ ] **Consider adding a "difficulty progression" field** to the unit metadata — to help learners self-assess readiness

---

## review-checklist.md

### Current State

The review checklist exists. Improvements needed:

- [ ] **Add section-by-section review instructions** — for each template section, tell the reviewer what to check (not just "is it complete" but "does it meet the standard")
- [ ] **Add specific checks for the Australian context section** — reviewers must verify AU legislation references are accurate and current
- [ ] **Add specific checks for framework T-codes** — reviewers must verify that each T-code:
  1. Exists in the current DCWF version
  2. Is linked to a specific lab step or assessment task
  3. The task description matches the actual DCWF task description
- [ ] **Add a lab testing checklist** — reviewer must confirm labs were executed successfully in the minimum hardware environment
- [ ] **Add an AI content check** — flag if content appears AI-generated without human expert review
- [ ] **Add explicit sign-off fields** for Domain Expert and Practitioner Reviewer (name, date, GitHub handle)
- [ ] **Define what "Practitioner Approved" means** — the reviewer must be an active practitioner in the domain, not just someone who has read about it

---

## competency-profile-template.md

### Current State

This template allows learners to build a framework-mapped competency profile to use in job applications. Needs significant expansion:

- [ ] **Expand the profile structure** — it should map to DCWF T-codes, SFIA skills, and ASD CSF domains
- [ ] **Add a per-unit evidence block** — for each unit completed, the learner records:
  - Unit code and title
  - Lab or assessment that generated evidence
  - Framework T-code or SFIA skill demonstrated
  - Link to portfolio artefact (from `student-portfolio/`)
- [ ] **Add employer guidance** — a brief note at the top of the template explaining to employers how to read the profile
- [ ] **Add a "how to use this in a resume"** section — practical guidance for learners
- [ ] **Create a PDF export version** — or add instructions for converting the Markdown to a professional PDF
- [ ] **Add a "certifications held" section** — so learners can cross-reference their degree competencies with any certifications they hold

---

## student-portfolio/

See `templates/student-portfolio/TODO.md` for detailed actions.

---

## New Templates Needed

The following templates do not exist yet but should be created:

- [ ] **`lab-environment-setup-template.md`** — A reusable template for documenting lab environment setup instructions (to avoid duplication across unit files). Should cover: OS selection, tool installation steps, verification steps, teardown instructions.

- [ ] **`capstone-brief-template.md`** — A template that supervisors use to define the capstone scope for each learner. Should include: learner name, major, capstone objective, scenario description, deliverables, timeline milestones, supervisor details.

- [ ] **`practitioner-review-template.md`** — A template for community practitioners who are reviewing a learner's capstone submission. Should include: submission summary, review criteria from the rubric, strengths, areas for improvement, overall assessment (Pass/Revise/Fail).

- [ ] **`wil-agreement-template.md`** — A work-integrated learning placement agreement template. Should include: learner details, workplace supervisor details, placement duration, learning objectives mapped to the degree, evidence requirements, confidentiality provisions.
