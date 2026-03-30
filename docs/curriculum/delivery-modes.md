# Delivery Modes

This document defines how the degree can be delivered across four modes,
with guidance on scheduling, support structures, and quality standards for each.

---

## Mode 1 — Self-Paced (Default)

### Description
The student studies independently, at their own pace, with no structured cohort,
deadlines, or facilitator. This is the default mode for open-source learners.

### Who it's for
- Career changers studying alongside full-time employment
- Experienced practitioners seeking structured self-development
- Learners in regional or remote areas without access to structured delivery
- Anyone who cannot commit to a fixed schedule

### How it works
1. Fork the repository and copy the competency profile template
2. Begin with F01 and progress through the prerequisite chain
3. Complete all labs and assessments independently, using the rubrics for self-assessment
4. Maintain the portfolio as you go
5. Seek community support through GitHub Discussions as needed

### Support available
- GitHub Discussions (community Q&A)
- Community mentorship (voluntary — see `docs/curriculum/work-integrated-learning.md`)
- GitHub Issues for content errors or questions

### No deadlines, no cohort, no certificate
Self-paced learners receive no certificate of completion. The portfolio is the
evidence of completion. There is no external body validating self-assessed progress.

---

## Mode 2 — Mentored Self-Paced

### Description
The student works at their own pace but with structured check-ins from a mentor
(a practitioner who has volunteered through the community mentorship program or
who the student has independently engaged).

### Who it's for
- Self-paced learners who want accountability and expert feedback
- Learners transitioning from a different technical background who need guidance
- Learners preparing for a role change and wanting practitioner input

### Scheduling guidance
- **Check-in frequency:** Fortnightly (30–60 minutes per session)
- **Duration:** Ongoing for the duration of a layer or major
- **Format:** Video call, chat, or asynchronous (Discord, Slack, email)

### Mentor responsibilities
- Review the student's lab work and provide constructive feedback
- Provide real-world context for unit content
- Help the student connect unit content to their career goals
- Not complete work for the student

### Does not change the assessment model
Mentored self-paced students still self-assess against rubrics. The mentor may
provide feedback on assessment responses but does not formally grade them.

---

## Mode 3 — Structured Cohort

### Description
A group of students progresses through the degree (or a layer/major) on a shared
timetable, with facilitated sessions, formal assessment marking, and structured support.

### Who it's for
- Employer-sponsored groups (staff development programs)
- Bootcamps running intensive delivery
- Community groups wanting accountability and peer learning
- Learners who perform better with structure and deadlines

### Scheduling templates

**Foundation Year in 12 weeks (intensive):**
```
Week 1–2:   F01 — Networking Fundamentals
Week 3–4:   F02 — OS & Administration
Week 5–6:   F03 — Scripting & Automation
Week 7–8:   F04 — Security Concepts & Principles
Week 9–10:  F05 — Legal, Ethics & Australian Compliance
Week 11–12: F06 — Data & Log Analysis
```

**Foundation Year in 24 weeks (standard pace, ~10 hrs/week):**
- 4 weeks per unit

**One unit per university semester (13 weeks, ~10 hrs/week):**
- Suitable for a single unit delivered as part of a broader university program

### Facilitation requirements
Refer to `docs/educator/facilitator-guide.md` for full guidance on running
structured cohort delivery, including session design, lab supervision, and
assessment marking.

### Minimum facilitation per unit
- 4 hours of facilitated concept sessions
- 4 hours of supervised lab time
- 1 hour assessment briefing and debrief

---

## Mode 4 — Blended University Delivery

### Description
A registered higher education provider adopts the curriculum and delivers it
as a formal accredited unit or program, with institutional assessment, formal
transcripts, and HECS-HELP eligibility (if applicable).

### Who it's for
- Universities seeking to adopt a free, framework-mapped cybersecurity curriculum
- TAFEs or private providers integrating specific units into existing programs
- Delivery partners pursuing formal TEQSA-compliant delivery

### Requirements for Mode 4 delivery
The delivering institution must:
1. Follow this degree's content standards (`docs/content-standards.md`) without
   removing framework mappings or Australian context requirements
2. Apply the assessment standards and moderation process (`docs/educator/assessment-moderation-guide.md`)
3. Acknowledge the open-source origin of the curriculum in their course documentation
4. Notify the project Maintainers of their use (via GitHub Issue) — not for approval,
   but for awareness and so the community can benefit from their improvements
5. Contribute back improvements and corrections identified during delivery (encouraged,
   not mandatory — but consistent with the CC BY 4.0 spirit)

### Institutional customisation
Delivering institutions may:
- Add institution-specific context, examples, or guest practitioners
- Adjust scheduling and delivery format
- Apply their own institutional assessment policies (late submission, resubmission, etc.)
- Issue their own institutional certificates of completion

Delivering institutions may not:
- Remove or substantially alter the framework mapping requirements
- Remove the Australian context requirement
- Replace the practitioner review requirement with purely academic review
- Assert ownership of the curriculum or restrict its continued open availability

### Credit transfer and articulation
For information on credit transfer between this degree and formal university programs,
see `docs/institutional/equivalence-mapping.md`.

---

## Choosing the Right Mode

| Factor | Recommended Mode |
|---|---|
| No fixed schedule available | Mode 1 (Self-paced) |
| Want accountability + expert feedback | Mode 2 (Mentored) |
| Employer is sponsoring | Mode 3 (Structured cohort) |
| Want a formal institutional qualification | Mode 4 (University) |
| Studying alongside full-time work, need flexibility | Mode 1 or 2 |
| Prefer structured learning with peers | Mode 3 |
| In a region without university access | Mode 1, 2, or 3 |
