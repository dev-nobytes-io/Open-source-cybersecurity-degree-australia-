# TODO — degrees/operational/cte/

**Major:** Cyber Threat Emulation (CTE)
**Degree:** Bachelor of Cybersecurity Operations
**Year:** 3
**Units:** CE01–CE06

All units are currently **Planned**. No unit files have been authored yet.

**Update (2026-06-21):** All six units (CE01–CE06) have been authored to **Draft**
(authorisation-first, isolated-lab-only, detection-outcome-focused) and pass the
unit linter. Per the major's content-safety rules they await review by a Domain
Expert with red team/emulation experience, a Practitioner Reviewer who has checked
**dual-use risk**, an AU computer-crime-law check of CE01, and TIBER-AU
verification.

**Important:** This major must not be started until OC06 (Offensive Security Concepts) is at least **Practitioner Approved**, as CTE builds directly on offensive tradecraft concepts.

---

## Files to Create

| File | Unit | Description |
|---|---|---|
| `CE01-offensive-foundations-ethics.md` | CE01 | Authorised testing, scope, rules of engagement, AU legal context |
| `CE02-red-team-operations.md` | CE02 | C2 frameworks, tradecraft, OPSEC, operational security |
| `CE03-attack-based-emulation.md` | CE03 | Emulation plans, MITRE CTID methodology, ATT&CK-based operations |
| `CE04-purple-team-operations.md` | CE04 | Collaborative testing, detection gap analysis, joint exercises |
| `CE05-reporting-debrief.md` | CE05 | Technical and executive reporting, TIBER-AU framework |
| `CE06-capstone-emulation-exercise.md` | CE06 | Full threat emulation operation with detection team (capstone) |

---

## Bloom's Taxonomy Requirements

Units CE01–CE05: **Levels 4–5** (analyse, evaluate, apply, design)
Capstone CE06: **Levels 5–6** (create, design, evaluate, execute)

Example verbs: design, execute, evaluate, construct, plan, assess, report, recommend

---

## Framework Mapping Requirements

| Framework | Required |
|---|---|
| MITRE ATT&CK (v14+) | Yes — emulation plans must be ATT&CK technique-based |
| MITRE CTID Emulation Plans | Yes — CE03 must use CTID methodology |
| TIBER-EU / TIBER-AU | Yes — CE05 reporting must reference TIBER-AU format |
| NIST NICE (PR-CDA-001, OV-SPP) | Yes — T-codes traceable to labs |
| SFIA 9 (PENT) | Yes — at least 2 units |

---

## Lab Requirements

At least 8 labs total. **Note:** CTE labs by nature involve offensive techniques. Every lab must include explicit authorisation scope, legal disclaimer, and be conducted in isolated lab environments only.

### Required Labs Across the Major

| Unit | Lab Ideas |
|---|---|
| CE01 | Lab: Draft a Rules of Engagement (ROE) document for a fictional engagement |
| CE01 | Lab: Review an authorisation scope — identify what is and is not permitted; identify AU legal implications (Computer Crimes Act) |
| CE02 | Lab: Set up a basic C2 framework (e.g., Havoc or Sliver) in an isolated lab; execute basic post-exploitation tasks |
| CE02 | Lab: Practice operational OPSEC — identify how attacker infrastructure can be fingerprinted |
| CE03 | Lab: Select a CTID emulation plan; adapt it to a fictional Australian organisation's threat model |
| CE03 | Lab: Execute the first 3 steps of a CTID emulation plan against a lab target |
| CE04 | Lab: Purple team exercise — red team executes a technique; blue team validates detection; document coverage result |
| CE04 | Lab: Produce a detection gap analysis report from a purple team exercise |
| CE05 | Lab: Write a technical findings report and a 1-page executive summary for a fictional engagement |
| CE05 | Lab: Produce a TIBER-AU-style threat intelligence-led red team report |
| CE06 | Capstone: Full threat emulation op against a simulated target with active detection team |

**Tools for this major (all free/OSS):**
- Havoc C2 or Sliver C2 (open-source C2 frameworks)
- MITRE ATT&CK Navigator
- MITRE CTID Emulation Plans (public library)
- Atomic Red Team (technique execution)
- Metasploit Framework
- Cobalt Strike is NOT permitted in labs (commercial; use open-source equivalents)

**Lab Environment Requirement:** All offensive labs must be run in **fully isolated environments** — no external network access during offensive exercises.

---

## Australian Legal Context (Critical for CE01)

CE01 must cover Australian computer crime law in detail:

- [ ] **Criminal Code Act 1995 (Cth)** — Part 10.7 (Computer offences); what constitutes unauthorised access
- [ ] **Authorisation requirements** — what constitutes written authorisation in Australia
- [ ] **State-level laws** — brief overview of state computer crime provisions
- [ ] **TIBER-AU** — the Australian adaptation of the TIBER-EU threat intelligence-led red team framework
- [ ] **Privacy Act 1988** — obligations when personal data is encountered during testing

---

## Capstone Unit (CE06) Requirements

The capstone is a **full threat emulation operation** conducted jointly with a detection team:

- [ ] Threat scenario defined and threat intelligence used to create an emulation plan
- [ ] Emulation plan developed using CTID methodology
- [ ] Rules of engagement and authorisation documented
- [ ] Operation executed against isolated lab environment
- [ ] Blue team participation documented (detection attempts, gaps identified)
- [ ] Purple team debrief conducted and documented
- [ ] Technical findings report written
- [ ] Executive summary written (TIBER-AU format)
- [ ] Detection gaps fed back into a detection improvement plan
- [ ] Community practitioner review of the capstone
- [ ] Deliverable suitable for professional portfolio (reference `templates/student-portfolio/index.html`)

---

## Content Safety Requirements

CTE is the highest-risk major for content misuse. All content must:

- [ ] Emphasise **authorised testing only** — every offensive technique must be framed in the context of a scoped engagement
- [ ] Include explicit legal context in CE01 that is revisited throughout the major
- [ ] Never provide step-by-step instructions for attacking production systems without authorisation
- [ ] Frame all tools in the context of their legitimate use in authorised red team or purple team engagements
- [ ] Be reviewed for dual-use risk by the Practitioner Reviewer

---

## Sign-off Requirements

Before any unit can be merged:

- [ ] Domain Expert with active red team / adversary emulation experience named in metadata
- [ ] Practitioner Reviewer (different from Domain Expert) named in metadata
- [ ] CE01 legal content reviewed by someone with knowledge of Australian computer crime law
- [ ] All offensive lab content reviewed for scope safety and dual-use risk
- [ ] TIBER-AU framework references verified against current Australian version

See `templates/review-checklist.md` for the full pre-merge checklist.
