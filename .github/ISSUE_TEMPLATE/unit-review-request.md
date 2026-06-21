---
name: "Unit Review Request"
about: Request Domain Expert / Practitioner / Framework Custodian sign-off on a unit
title: "[Review] <UNIT CODE> — <Unit Title>"
labels: ["unit: review", "status: under-review"]
assignees: []
---

<!--
Use this issue to request practitioner review of a Draft unit. See
docs/governance.md for the content lifecycle and required sign-offs.
Lifecycle: Draft -> Under Review -> Practitioner Approved -> Framework Verified -> Published
-->

## Unit under review

- **Unit code & title:**
- **File path:**
- **Pull request:** <!-- link the PR containing the unit -->
- **Current status:** Draft

## Pre-review checklist (author confirms)

- [ ] `python3 .github/scripts/lint_units.py <file>` passes
- [ ] All template sections present; no leftover `[placeholders]`
- [ ] Learning outcomes use the correct Bloom's level for the layer
- [ ] Framework mapping T-codes each trace to a specific lab/assessment

## Reviewers requested

- [ ] **Domain Expert** (technical accuracy): @
- [ ] **Practitioner Reviewer** (workforce relevance): @
- [ ] **Framework Custodian** (mapping accuracy): @

## Areas needing particular attention

<!-- e.g. "Please confirm the NICE DCWF T-codes in the mapping table" or
"the Australian legislation references in Topic 4". -->

## Sign-off (reviewers tick when complete)

- [ ] Domain Expert approved
- [ ] Practitioner Reviewer approved
- [ ] Framework Custodian verified mappings
