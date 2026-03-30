# Teaching and Learning Philosophy

This document articulates the pedagogical principles underpinning the
Open-Source Cybersecurity Degree. It is intended for accreditation reviewers,
institutional partners, and educators seeking to understand the educational
design rationale.

---

## 1. Core Pedagogical Stance

This degree is built on the conviction that **cybersecurity is learned by doing**.
Theoretical knowledge is necessary but insufficient — a practitioner who can define
a threat hunting methodology but cannot execute a hunt in a real environment is not
prepared for professional practice.

The degree therefore adopts a **practice-first, framework-grounded** pedagogy:
- Practical application precedes or accompanies theoretical exposition
- Every concept is demonstrated in a lab environment before being assessed
- Theoretical content exists to explain and extend practical experience, not to precede it

This aligns with established constructivist learning theory (Vygotsky, 1978; Bruner, 1977)
and is directly informed by the design of exemplary practitioner education programs
including CS50 (Harvard/edX), SANS training, and apprenticeship models in the trades.

---

## 2. Instructional Design Principles

### 2.1 Lab-First Sequencing

Within each unit, lab exercises are positioned as the primary learning vehicle.
Topics provide the conceptual scaffolding to make sense of lab experiences.
Assessments require students to reflect on and extend what they did in labs.

The sequence is:
```
Read topic → Perform lab → Reflect in assessment → Synthesise in portfolio
```

Not:
```
Read content → Answer questions about content
```

### 2.2 Framework-Native Learning

Students do not learn frameworks as an add-on. Frameworks — MITRE ATT&CK, NICE DCWF,
SFIA, ASD CSF, NIST CSF — are the vocabulary used throughout the degree. Students
learn cybersecurity *in* the language of professional practice, not in an academic
vocabulary that then has to be translated.

This approach ensures graduates can immediately communicate in terms their employers
use, and that their competency profiles (NICE T-codes, SFIA levels) are credible and
accurate because they reflect genuine demonstrated practice.

### 2.3 Authentic Assessment

Assessments are designed to be as close as possible to real professional tasks.
A threat intelligence assessment asks students to produce a finished intelligence
product, not to answer questions about intelligence concepts. A GRC assessment asks
students to conduct a compliance gap analysis, not to define what a gap analysis is.

Rubrics are written to evaluate professional-quality outputs (clarity, accuracy,
reasoning, appropriate use of evidence) not to evaluate memorisation of content.

### 2.4 Australian Context as Core Content

The Australian regulatory, legislative, and threat environment is not a bolt-on
addition to generic international cybersecurity content. It is core content.

Every unit requires Australian context because the graduates of this degree will
practise cybersecurity in Australia, under Australian law, working for Australian
organisations facing Australian-specific threats. Generic international content
without this context produces practitioners who are less effective in Australian roles.

### 2.5 Practitioner Authorship and Review

Content is authored and reviewed by practitioners currently active in the domain.
Academic content review without practitioner validation is insufficient for a
practice-based degree. The governance model (see `docs/governance.md`) requires
practitioner sign-off before any unit can be published.

This reflects the apprenticeship tradition — learning should be modelled on the
practice of expert practitioners, not solely on academic descriptions of that practice.

---

## 3. Bloom's Taxonomy Application

The degree applies Bloom's Revised Taxonomy (Anderson & Krathwohl, 2001) to ensure
cognitive demand increases progressively across the three degree layers:

| Layer | Bloom's Levels | Learning Focus |
|---|---|---|
| Foundation | 1–3 (Remember, Understand, Apply) | Build foundational literacy; demonstrate core skills in controlled scenarios |
| Core | 3–4 (Apply, Analyse) | Apply knowledge to professional scenarios; analyse situations to identify issues and solutions |
| Major | 4–5 (Analyse, Evaluate) | Evaluate complex situations; make and justify professional judgements |
| Capstone | 5–6 (Evaluate, Create) | Synthesise knowledge across units; create original professional artefacts |

This progression ensures students are not simply recalling content — they are
developing the higher-order thinking required for professional practice.

---

## 4. Assessment Philosophy

### Formative Assessment as Feedback

Formative assessments are explicitly not high-stakes grade events. Their purpose
is to provide timely feedback that helps students improve before the summative
assessment. Facilitators should treat formative tasks as diagnostic tools, not
performance evaluations.

### Summative Assessment as Professional Evidence

Summative assessments produce artefacts that are meaningful beyond the degree —
a lab report, a threat analysis, an architecture design, a compliance framework.
These become the student's professional portfolio. The assessment design
incentivises producing genuinely high-quality work because that work has
real-world professional value.

### Rubric Transparency

All summative rubrics are published with the assessment. Students know exactly
what distinguishes Exemplary from Proficient from Developing. This is not "teaching
to the test" — it is transparency about professional quality standards. In industry,
practitioners are expected to know what good work looks like in their domain.

---

## 5. Learner-Centred Principles

### Student Ownership

Students own their learning artefacts. Lab reports, assessment responses, and
portfolio materials belong to the student. This is not a feature of the licence —
it is a pedagogical choice. Professional ownership of one's work is a habit
that should be cultivated from the beginning of a practitioner's career.

### Pacing Flexibility

The degree accommodates diverse learners through flexible pacing. There is no
universal cohort timetable for self-directed learners. Delivery partners may
apply structured timetables but should accommodate learners who need flexibility
where institutional policy permits.

### Failure as Learning

Lab exercises are designed to be attempted before answers are provided. Getting
something wrong in a lab environment is a learning event, not a failure. Facilitators
and the pedagogical design actively avoid pre-answering lab challenges.

---

## 6. Technology and Open-Source Tools

The choice to use exclusively free and open-source tools in Foundation and Core
units is both ethical and pedagogical.

**Ethical:** Learning should not require financial resources beyond access to a
standard consumer laptop.

**Pedagogical:** Open-source tools require students to engage with configuration,
documentation, and troubleshooting in ways that commercial GUI tools do not.
The problem-solving involved in getting Elastic running correctly teaches more
than clicking through a polished commercial interface.

Major units may introduce commercial tools alongside free equivalents because
commercial tools are often encountered in professional practice, and graduates
need to be able to work with them.

---

## 7. References

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning,
teaching, and assessing: A revision of Bloom's educational objectives.* Longman.

Bruner, J. S. (1977). *The process of education.* Harvard University Press.

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological
processes.* Harvard University Press.

Malan, D. J., & Hardison, T. (2010). CS50: Democratizing computing education.
*ACM Inroads, 1*(4), 31–32.
