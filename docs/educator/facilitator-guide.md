# Facilitator Guide

This guide is for educators, trainers, mentors, and institutions delivering the
Open-Source Cybersecurity Degree in a structured setting — including university
semesters, employer training programs, bootcamps, and mentored cohorts.

For governance and content standards, see `docs/governance.md` and
`docs/content-standards.md`. For assessment moderation, see
`docs/educator/assessment-moderation-guide.md`.

---

## 1. Who This Guide Is For

**University lecturers** adopting this curriculum for a unit or full degree program.

**Employer L&D teams** running a structured cohort of staff through the degree or
selected units as part of a development program.

**Bootcamp facilitators** running intensive delivery of Foundation or Core units.

**Community mentors** supporting a small group of self-directed learners with
regular check-ins, feedback, and guidance.

---

## 2. Delivery Modes

The degree supports four delivery modes. Choose the mode that fits your context.

| Mode | Description | Typical Context |
|---|---|---|
| **Self-paced (async)** | Students work independently with no structured sessions | Default open-source mode |
| **Mentored self-paced** | Students work independently with regular mentor check-ins (fortnightly or monthly) | Community mentorship programs |
| **Structured cohort** | Students progress together on a shared timetable with facilitated sessions | Employer programs, bootcamps |
| **Blended university** | Structured cohort with formal assessment and institutional recognition | University adoption |

See `docs/curriculum/delivery-modes.md` for detailed guidance on each mode.

---

## 3. Scheduling Guidance

### Per-Unit Time Budget

Each unit is designed for approximately 120–140 hours of student effort:

| Activity | Hours |
|---|---|
| Reading and directed study (topics) | 60–70 |
| Lab exercises (minimum 2 per unit) | 30–40 |
| Assessment (formative + summative) | 20–30 |
| **Total** | **~120–140 hours** |

### Recommended Timetabling

**University semester (13 weeks):**
- One 8 CP unit per semester fits comfortably at ~10 hours/week student effort
- Two units per semester is feasible for full-time students (~20 hours/week)

**Employer cohort (intensive, 5 days/unit):**
- Day 1–2: Topics and concepts (facilitator-led sessions, ~4 hrs/day)
- Day 3–4: Lab exercises (supervised lab time, ~6 hrs/day)
- Day 5: Assessment briefing and formative task, debrief

**Bootcamp (Foundation Year in 12 weeks):**
- 2 weeks per unit
- Week 1: Topics + Lab 1
- Week 2: Lab 2 + Assessment

**Part-time cohort (one unit per 10 weeks):**
- Week 1–5: Topics (2 hrs/week directed study + 1 hr group session)
- Week 6–8: Labs (3 hrs/week lab time + 1 hr group debrief)
- Week 9–10: Assessment + peer review

---

## 4. Facilitated Session Design

### Recommended Session Types

**Concept sessions (1–2 hrs)**
Present or discuss one or two topics per unit. Do not read the content aloud —
students should read topics before the session. Use session time for:
- Discussion questions ("How does this apply in an Australian enterprise context?")
- Worked examples using real Australian incidents or ASD advisories
- Guest practitioner Q&A

**Lab sessions (2–4 hrs)**
Students work through lab exercises with facilitator support available. Facilitator
role is to troubleshoot, not demonstrate. Students should attempt each step before
asking for help.

**Assessment workshops (1 hr)**
Brief the summative assessment, answer questions about scope and rubric expectations.
Do not pre-answer the assessment — the purpose is clarification, not scaffolding.

**Debrief/review sessions (1 hr)**
Review formative assessment responses as a group. Use exemplary and developing
examples (anonymised) to calibrate student understanding of the rubric.

### Practitioner Guest Sessions

Every major unit should include at least one guest session with a practitioner
currently working in the domain. This reinforces the practitioner-led design
principle and gives students access to real-world context.

Practitioner guests should be briefed to:
- Describe their actual role and a day in their working life
- Connect their work to the frameworks covered in the unit (NICE, ATT&CK, etc.)
- Discuss the Australian regulatory and threat landscape context
- Answer student questions honestly — including about salary, career paths, and
  the realities of the role

---

## 5. Lab Supervision

### Before the Lab

- Test every lab environment before delivery — tool versions change and instructions
  may need adjustment
- Ensure students have completed prerequisites (prior units and environment setup)
- Brief expected outcomes and what "done" looks like

### During the Lab

- Circulate and observe — do not hover
- Encourage students to attempt steps before asking for help
- Where a student is stuck, ask guiding questions rather than providing the answer:
  "What does that error message tell you?", "What did you expect to happen?"
- Flag any lab steps that consistently cause difficulty — these should be reported
  as GitHub Issues for content improvement

### Lab Safety (CTE and Offensive Units)

For Cyber Threat Emulation units involving offensive techniques:
- All lab work must occur in isolated, authorised environments only
- Brief the legal and ethical framework at the start of every CTE lab session
- Review `degrees/operational/cte/README.md` for the ethical and legal framework
- Never allow students to practice offensive techniques outside of controlled lab VMs

---

## 6. Assessment in Facilitated Delivery

### Formative Assessment

Formative assessments are feedback tools, not grades. Use them to:
- Identify students who are not tracking with the content
- Provide written or verbal feedback before the summative assessment
- Calibrate group understanding before moving on

### Summative Assessment Marking

Use the rubric provided in each unit. For consistency across multiple markers,
follow the moderation process in `docs/educator/assessment-moderation-guide.md`.

Key principles:
- Apply the rubric as written — do not add undocumented criteria
- If a student response is borderline between two levels, select the lower level
  and provide specific feedback on what would achieve the higher level
- Keep marked copies for a minimum of 12 months for moderation and audit purposes

### Returning Feedback

Return formative feedback within 5 working days of submission.
Return summative feedback within 10 working days of submission.
Feedback must reference specific rubric criteria — "good work" is not sufficient feedback.

---

## 7. Student Support

### At-Risk Indicators

Watch for students who:
- Miss two or more consecutive lab sessions
- Submit formative assessments with "Beginning" performance on majority of criteria
- Do not engage in group sessions or discussions
- Report significant time pressure or life difficulties

### Intervention

If a student appears at risk:
1. Have a private, non-judgmental check-in conversation
2. Discuss whether the pace is sustainable and whether adjustments are needed
3. Consider a flexible timeline extension (facilitated delivery partners set their
   own policies on extensions)
4. Connect the student with community mentorship resources if available

### Equity Considerations

See `docs/quality/equity-and-inclusion.md` for guidance on supporting diverse learners,
including those with disabilities, ESL students, and those facing access barriers.

---

## 8. Using the Portfolio System

Ensure all students set up their competency profile from the first session:
1. Fork the repository
2. Copy `templates/competency-profile-template.md`
3. Open `templates/student-portfolio/index.html` locally

By the end of each unit, students should update their T-code evidence table with
links to their completed lab reports and assessment responses. This is not optional
in a facilitated delivery context — portfolio maintenance is part of the program.

---

## 9. Reporting Framework Issues

Facilitators are in the best position to identify content quality issues:
- Incorrect or outdated technical information
- Lab steps that do not work as documented
- Australian context references that are out of date
- Framework mappings that appear incorrect

Report these via GitHub Issues with the appropriate label (`content-review`,
`dead-link`, `framework-update`). You can also open a pull request with a fix —
see `CONTRIBUTING.md`. Facilitators who contribute content fixes are acknowledged
as contributors.

---

## 10. Becoming a Delivery Partner

Organisations wishing to formally deliver this degree (including issuing institutional
certificates of completion or credit) should refer to
`docs/institutional/equivalence-mapping.md` for the formal pathway, and contact
the project Maintainers via GitHub to discuss a partnership arrangement.

Delivery partners are expected to:
- Deliver content as documented without removing framework mappings or Australian context
- Apply the assessment standards in `docs/content-standards.md`
- Follow the academic integrity policy in `docs/student/academic-integrity.md`
- Contribute back content improvements and corrections identified during delivery
