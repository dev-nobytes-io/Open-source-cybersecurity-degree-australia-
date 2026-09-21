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

- [ ] **A materiality floor is now part of the taught egress method**, after CI caught
      that ranking by modified z-score alone puts a user whose normal day is 2 kB and who
      once sent 100 kB (z = 8.5) *above* the person exfiltrating 2.5 GB (z = 3.2). The
      floor is drawn from the estate's own p99 rather than a round number. Consider
      whether the same argument applies anywhere else a scale-free statistic is taught.
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
- [x] ~~**The generator's DGA is uniform-random**, which is the case character entropy
      is optimal for.~~ **Done.** `dga_domain()` now emits two families — uniform-random
      and dictionary-word concatenations — and benign traffic carries CDN object hashes,
      DKIM selectors, UUID subdomains and base32 tokens at ~1.5% of domain draws. Entropy
      now has real false positives *and* real false negatives, and
      [SPL-09 Lab 5](../labs/guides/spl-09.md) is rebuilt around the result: per-domain
      scoring manages ~44% precision at a fixed budget, while the same weak signal
      aggregated **per host** separates 54 from 4. The transferable lesson is that the
      unit of detection matters more than the scorer.
- [ ] **Sysmon carries EventCode 1 only.** This is deliberate — it is what makes
      [SPL-03 Lab 4](../labs/guides/spl-03.md)'s telemetry-gap classification real — but
      it caps what any endpoint-detection lab can do. Decide whether to add 3, 7, 11 and
      22 behind a generator flag so the gap can be opened and closed.
- [ ] **Docker environments are untested end to end in this repository.** The compose
      files are YAML-valid and the app configuration is written, but no CI job starts
      Splunk. Everything that *can* be verified without a running instance now is, on
      every change, by [`.github/workflows/labs.yml`](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/blob/main/.github/workflows/labs.yml) —
      dataset properties, assessment integrity, every embedded Python block, the five
      objective answers by their taught method, link resolution, generator determinism
      and the quiz payload. The container startup path remains unverified; doing it
      would need a CI job that pulls the Splunk image, accepts its licence and waits
      for the instance, which is a licence question before it is a technical one.
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


### modules/security-architecture/ — EXT-SA Security Architecture Series Verification

The series is written against the source documents listed in each module's Overview and
Further Reading, read in full on **2026-09-12**. It is an extension series (0 CP) and is
delivered one module per pull request (index first, then SA-01 … SA-06, then the quiz).
Until all land, the series index links only the modules present.

**Blocking — must be resolved before any module advances beyond Draft:**

- [ ] **Assign a Domain Expert and a Practitioner Reviewer** (practising security or
      enterprise architect; for SA-06 someone with current Australian Government system
      authorisation or IRAP experience). All six modules carry `_Unassigned_`.
- [ ] **Confirm ISM chapter currency.** SA-04 and SA-06 cite the ISM *Guidelines for
      networking*, *gateways*, *system access* and *security assurance* as retrieved
      September 2026. The ISM is updated quarterly — re-verify every cited control
      identifier against the live ISM on cyber.gov.au before delivery.
- [ ] **Confirm ASD *Modern Defensible Architecture* publication status and date**
      (SA-03). The stage names and foundations are taken from the ASD document as read;
      confirm they match the current published version.
- [ ] **Confirm SABSA W100 and W117 edition/publication years** (SA-01, SA-02) and that
      the summarised content stays within fair-dealing limits — both papers are copyright
      The SABSA Institute / The Open Group.
- [ ] **Confirm SOC-CMM, CTI-CMM (v1.3) and Threat Hunting Maturity Model version and
      licence terms** before SA-06 labs reference their assessment structures.
- [ ] Framework Custodian to map the provisional project-local KSAT IDs (`SA-0n-K01` …)
      and confirm every NICE DCWF T-code and SFIA 9 code cited.

**Content reconciliation:**

- [ ] Cross-check each module's *Where this module fits* table against SC02, SE01, SE02,
      SE06, GR01, GR03, GR05, SE03, SE04, OC02 and DE02 to confirm nothing is re-taught
      rather than extended (rule in the series index, *What this series is not*).
- [ ] Add EXT-SA to [`quality/annual-review-schedule.md`](quality/annual-review-schedule.md)
      with a **6-month** staleness window (ISM quarterly updates), due 2027-03-12.
- [ ] Decide whether the series warrants a `labs/` environment as EXT-SPL has; the
      current labs are paper-based or use free tooling only.

### modules/elastic/ — EXT-ELK Elastic and OpenSearch Series Verification

Vendor-specific series (0 CP). Product behaviour is cited to Elastic's and OpenSearch's
documentation as read on **2026-09-13**; both platforms release often, so these items
are time-sensitive. Delivered one module per PR (index + ELK-01 first).

**Blocking — must be resolved before any module advances beyond Draft:**

- [ ] **Assign a Domain Expert and a Practitioner Reviewer** who run Elastic Security or
      OpenSearch Security Analytics in production.
- [ ] **Confirm the subscription tier of the Elastic Security detection engine and
      prebuilt rules.** The subscriptions comparison as read places prebuilt rules under
      Platinum; the Security docs defer to that page. ELK-04's labs use custom rules on
      Basic regardless, but the index and ELK-04 must state the tier correctly.
- [ ] **Pin the stack versions** the compose files use (`ELASTIC_VERSION`; an OpenSearch
      version for ELK-05) and record the ECS version (docs stated 9.5.0 as read).
- [ ] **Run the Elastic compose path** (`labs/docker/compose.elastic.yml`) on a machine
      with Docker: the file was syntax-validated only. In particular confirm the
      Filebeat-to-data-stream write with a custom `index` name and the `oscd-epoch`
      pipeline behave as ELK-01 Lab 2 describes.
- [ ] Confirm Elastic Cloud Australian regions and residency statements before ELK-03's
      Australian context is taught.
- [ ] Framework Custodian to map provisional KSAT IDs (`ELK-0n-K01` …) and confirm
      NICE T-codes (paraphrased) and ASD CSF sub-domain names.

**Content:**

- [ ] Add EXT-ELK to [`quality/annual-review-schedule.md`](quality/annual-review-schedule.md)
      with a **6-month** window (vendor release cadence).
- [ ] Lab guides `labs/guides/elk-*.md` following the EXT-SPL pattern, including the
      optional Fleet Server enrolment path for ELK-01 Lab 3.

### modules/constrained-operations/ — EXT-DSO Constrained and Disconnected Environments Verification

Four-module extension series (0 CP) on security operations for sites that are isolated by
link, by policy, physically, or by operational-technology zoning, delivered one module per
pull request (index and DSO-01, then DSO-02 … DSO-04, then the quiz). Sources were read
on **2026-09-13**: the ISM (September 2026) chapters on gateways, networking, media,
information technology equipment, data transfers and physical security; NIST SP 800-88
Rev. 2 (September 2025) and SP 800-84 (September 2006) from their publication PDFs; the
Sigma rules and correlation specifications v2.1.0; the OASIS STIX 2.1 and TAXII 2.1
standard pages; the pySigma pipelines documentation; and the chaos-engineering principles.

**Blocking — must be resolved before any module advances beyond Draft:**

- [ ] **Assign a Domain Expert and a Practitioner Reviewer** with current Australian
      Government assurance experience — someone who has designed or operated monitoring
      across a cross domain solution or an isolated network. All four modules carry
      `_Unassigned_`.
- [ ] **Confirm the DSO-01 Topic 4 decision rule** ("monitor at the highest classification
      the data carries; release downward only what the transfer policy allows") against
      current ASD direction. It is stated as architectural inference from ISM-0635,
      ISM-1521 and ISM-1522, not as an ISM position.
- [ ] **Read ASD's *Introduction to Cross Domain Solutions* and *Fundamentals of Cross
      Domain Solutions*** (named by the ISM; not read) and revise DSO-01 Topic 4 if they
      state a position on where monitoring sits.
- [ ] **Re-verify every cited ISM control identifier** against the live ISM before
      delivery. DSO-03 alone cites about ninety controls from the media, IT equipment,
      data-transfer and physical-security chapters; the ISM is updated quarterly.
- [ ] **Verify the OT statements taken from author knowledge** in DSO-01 Topic 6 —
      zones and conduits and security levels as concepts of IEC 62443-3-2/3-3, and the
      Purdue model levels — against the standard texts or SP 800-82 Rev. 3.
- [ ] **Confirm the ASD incident-response exercise guidance** title and URL for DSO-04
      (cyber.gov.au did not respond on the authoring date) and add it to Further reading.
- [ ] Framework Custodian to map the provisional project-local KSAT IDs (`DSO-0n-K01` …)
      and confirm every NICE DCWF T-code (T0264's wording is a paraphrase), SFIA 9 level
      and ASD CSF sub-domain cited.

**Content reconciliation:**

- [ ] Cross-check each module's *Where this module fits* table against SA-04, SA-05,
      SA-06, DE01, DE03, DE04, DE05, CE04, OC02, OC04 and EXT-ANS to confirm nothing is
      re-taught rather than extended.
- [ ] Confirm the STIX 2.1 Indicator validity and revocation field names referenced
      generically in DSO-02 Topic 5, and check for a Sigma specification release later
      than v2.1.0.
- [ ] The labs assume the SA-05 Lab 3 relay estate from `labs/` (PR #49). Once it lands,
      add `labs/guides/dso-*.md` walkthroughs and register them in the nav; DSO-03 Lab 2's
      sanitisation steps must keep their "procedural model only" wording.
- [ ] Add EXT-DSO to [`quality/annual-review-schedule.md`](quality/annual-review-schedule.md)
      with a **6-month** staleness window (ISM quarterly updates), due 2027-03-13.
### modules/playbook-engineering.md — EXT-IRP Verification

Single-module extension (0 CP) on vendor-neutral playbook engineering, grounded in the
OASIS CACAO Security Playbooks v2.0 specification and the NIST SP 800-61r3 publication
page as read on **2026-09-13**.

- [ ] **Assign a Domain Expert and a Practitioner Reviewer** who run playbooks in a live SOC.
- [ ] **Confirm the ASD incident-response guidance titles and URLs** (plan, readiness
      checklist, reporting channel) — cyber.gov.au did not respond on the authoring date,
      so Topic 8 and Further Reading cite the landing page only.
- [ ] Read SP 800-61r3 in full before Topic 3 is taught in depth; the module cites only its
      framing. Check for a CACAO release later than CS01.
- [ ] Framework Custodian to map provisional KSAT IDs (`EXT-IRP-K01` …) and confirm
      the NICE T-codes (paraphrased, incl. T0510) and ASD CSF sub-domain names.

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
