# Student Handbook

Welcome to the Open-Source Cybersecurity Degree (Australia). This handbook is your
primary reference for everything you need to navigate and complete the degree.

---

## 1. About This Degree

This is a free, open-source cybersecurity degree designed for the Australian workforce.
It is aligned to the Australian Qualifications Framework (AQF) Level 7 and maps directly
to the workforce frameworks your future employer uses to hire and assess cybersecurity
professionals — including NIST NICE DCWF, SFIA 9, and the ASD Cyber Skills Framework.

The degree is not issued by a registered tertiary provider. It is community-built,
practitioner-reviewed, and freely available. Think of it as the CS50 of Australian
cybersecurity education — rigorous, practical, and respected by the industry.

**What you get:**
- 168 credit points of structured cybersecurity education across 3 years
- A practitioner-verified competency profile mapped to NIST NICE DCWF work roles
- A portfolio of labs and assessments you own and can show employers
- A clear bridge to industry certifications (GIAC, CISSP, CISM, OSCP, and more)

**What you do not get:**
- A parchment or formal academic transcript from a registered provider
- HECS-HELP eligibility (this is a free, open-source program)
- Automatic credit at other universities without a formal articulation agreement

For formal academic recognition, see `docs/student/recognition-of-prior-learning.md`
and `docs/institutional/equivalence-mapping.md`.

---

## 2. Degree Structure

The degree has three layers completed in sequence:

```
Year 1 — Foundation (6 units, 48 CP)
         ↓
Year 2 — Degree Core (6 units, 48 CP)
  Choose: Operational Core  OR  Strategic Core
         ↓
Year 3 — Major + Capstone (6 units + capstone, 72 CP)
  Choose one of 8 majors
```

**Total: 19 units × 8 CP + 1 capstone × 24 CP = 168 CP**

### Foundation Year (All Students)

All students complete the same 6 foundation units regardless of pathway:

| Code | Title |
|---|---|
| F01 | Networking Fundamentals |
| F02 | Operating Systems & Administration |
| F03 | Scripting & Automation |
| F04 | Security Concepts & Principles |
| F05 | Legal, Ethics & Australian Compliance |
| F06 | Data & Log Analysis |

### Year 2 — Choose Your Core

After Foundation, choose the core that matches your intended major:

**Operational Core** → leads to operational majors (Threat Hunting, DFIR, CTI,
Detection Engineering, Cyber Threat Emulation)

**Strategic Core** → leads to strategic majors (Security Engineering, Leadership
& CISO, GRC)

### Year 3 — Choose Your Major

| Pathway | Majors |
|---|---|
| Operational | Threat Hunting · DFIR · CTI · Detection Engineering · CTE |
| Strategic | Security Engineering · Leadership & CISO · GRC |

Not sure which major to choose? See `docs/student/pathway-guide.md`.

---

## 3. Prerequisites

Units must be completed in order. The prerequisite chain is:

- **Foundation units** (F01–F06): No prerequisites — start here
- **Core units** (OC/SC): Requires completion of all 6 Foundation units
- **Major units**: Requires completion of all 6 Core units in your chosen pathway
- **Capstone**: Requires completion of all 6 Major units

You may not start Core units until all Foundation units are complete. This is enforced
in the honour system for self-directed learners; institutional delivery partners may
enforce formal prerequisites.

---

## 4. How to Study

### Self-Directed (Default)

The degree is designed for self-directed learners. There are no fixed enrolment dates,
no cohorts, and no deadlines unless you are studying through a delivery partner.

**Recommended pace:**
- Full-time (40 hrs/week): 1 unit per 3–4 weeks; complete degree in approximately 18 months
- Part-time (15 hrs/week): 1 unit per 8–10 weeks; complete degree in approximately 3 years
- Each unit is designed for 120–140 hours of total student effort

**Suggested weekly rhythm:**
1. Read all topics for the week (2–3 hrs)
2. Complete the lab exercises (3–5 hrs)
3. Draft assessment responses or build portfolio artefacts (2–4 hrs)
4. Update your competency profile (`templates/competency-profile-template.md`)

### Structured Delivery

If you are studying through a university, employer, or bootcamp delivery partner,
your facilitator will provide a timetable. See `docs/educator/facilitator-guide.md`
for how structured delivery works.

---

## 5. Labs & Technical Environment

### What You Need

All Foundation and Core labs require only a standard consumer laptop:
- **Minimum:** 8 GB RAM, quad-core CPU, 50 GB free disk
- **Recommended:** 16 GB RAM for comfortable VM use

Major-level labs may require more resources; each lab states its requirements.

### Lab Environment

Labs use free and open-source tools only (Foundation and Core). You will be working with:
- Linux VMs (Kali Linux, Ubuntu — free downloads)
- Wireshark, Zeek, Elastic/OpenSearch, Sigma, Volatility, Autopsy, and others
- Python and Bash scripting environments

No paid tool licences are required for Foundation or Core units. Some Major units
reference commercial tools alongside free alternatives.

### Lab Safety and Ethics

Some labs involve offensive security techniques (especially in the CTE major).
All offensive techniques in this degree are performed only in isolated, authorised
lab environments. Applying these techniques outside of authorised environments is
illegal under the Australian Criminal Code Act 1995 and may constitute a serious
criminal offence.

You are responsible for ensuring all lab work is conducted ethically and lawfully.

---

## 6. Assessment

Each unit has at minimum:
- One **formative assessment** — low-stakes, feedback-focused
- One **summative assessment** — evaluated against a 4-level rubric (Exemplary,
  Proficient, Developing, Beginning)

### Self-Assessed vs. Peer/Facilitated Assessment

**Self-directed learners:** Most assessments are self-assessed using the provided
rubrics. You are expected to apply the rubric honestly to your own work.

**Facilitated delivery:** Your facilitator or a peer reviewer will assess your
summative work. See `docs/educator/assessment-moderation-guide.md` for how
assessment consistency is maintained.

### Portfolio Approach

Every assessment you complete becomes part of your professional portfolio. Store your
lab reports, assessment responses, and project files in your own GitHub repository
and link them from your competency profile.

Employers increasingly ask candidates to provide evidence of hands-on skills.
A well-maintained portfolio is one of the most valuable outcomes of this degree.

---

## 7. Academic Integrity

This is a self-directed program. Your integrity is your own responsibility.

The key rules:
- **All submitted work must be your own** unless the assessment explicitly requires
  collaboration
- **AI tools may be used** as learning aids (to explain concepts, debug code, review
  drafts) but may not be used to generate assessment responses you submit as your own
  work. See `docs/student/academic-integrity.md` for the full AI use policy.
- **Do not copy** lab reports, assessment responses, or written work from other
  students or online sources
- **Attribution is required** for any third-party content used in assessments

Violations in a self-directed context primarily harm you — a portfolio full of
AI-generated work will be transparent to any experienced cybersecurity employer.

---

## 8. Your Competency Profile

From your first unit, maintain your competency profile:
- `templates/competency-profile-template.md` — fill this in as you complete each unit
- `templates/student-portfolio/index.html` — your visual, employer-facing portfolio

After completing the degree, your profile will show every NICE DCWF work role and
task code you have demonstrated, backed by specific lab and assessment evidence.
This is what you show employers.

---

## 9. Getting Help

### Community Support

This is an open-source project with a contributor community. For questions:
- Raise a GitHub Issue with the label `question` or `student-support`
- Engage with other students and practitioners in the community discussion forums
  (see the repository's Discussions tab on GitHub)

### Finding a Mentor

Practitioners who have contributed to the degree may be available as mentors.
The community maintains a list of practitioners willing to support learners (see
`docs/institutional/industry-advisory-board-charter.md` for the advisory structure).

### Content Errors

If you find an error in unit content, lab instructions, or framework mappings:
1. Raise a GitHub Issue with the label `content-review` and describe the error
2. If you can fix it, open a pull request — see `CONTRIBUTING.md`

---

## 10. Completing the Degree

The degree is considered complete when:
1. All 6 Foundation units are marked complete in your competency profile
2. All 6 Core units (Operational or Strategic) are marked complete
3. All 6 Major units in your chosen major are marked complete
4. The Capstone project is complete and documented in your portfolio

There is no formal graduation ceremony or certificate for self-directed completion.
Your evidence of completion is your competency profile and portfolio — a practical
demonstration of capability that carries more weight with technical employers than
a certificate.

For formal recognition pathways (credit transfer, institutional recognition), see
`docs/student/recognition-of-prior-learning.md`.
