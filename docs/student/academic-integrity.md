# Academic Integrity Policy

This policy defines the standards for academic honesty in the Open-Source
Cybersecurity Degree. All students — whether self-directed or studying through
a delivery partner — are expected to uphold these standards.

Academic integrity is not just a rule. In cybersecurity, your professional
reputation is built on trust. An employer who discovers that your portfolio
was fabricated or AI-generated will not give you a second chance. The habits
you form here are the habits you carry into your career.

---

## 1. Core Principles

### Your Work Must Be Your Own

All assessment responses, lab reports, and project deliverables you submit or
include in your portfolio must represent your own thinking, analysis, and effort.

This does not mean you cannot:
- Use reference materials, documentation, or textbooks
- Discuss concepts with peers or a mentor
- Use tools (including AI) to assist your learning

It means the final output — the analysis, the conclusions, the written response —
must be yours.

### Attribution Is Mandatory

Any time you use someone else's words, ideas, data, or code, you must attribute
the source. This applies to:
- Direct quotations
- Paraphrased ideas
- Code you adapted from another source
- Framework content (e.g., MITRE ATT&CK descriptions)
- AI-generated text (see Section 3)

---

## 2. Prohibited Conduct

The following are violations of academic integrity:

### Plagiarism
Presenting someone else's work as your own — including copying text from websites,
reports, other students' work, or AI tools without attribution.

### Contract Cheating
Having another person (human or AI service) complete your assessment on your behalf.
This includes paying for assignment help services.

### Fabricating Evidence
Claiming to have completed a lab exercise without doing so, or fabricating expected
outputs (screenshots, terminal outputs, analysis results).

### Collusion
Working with another student to produce a joint submission where individual work is
required, without the assessment explicitly permitting collaboration.

### Misrepresentation of AI Use
Using AI tools to generate assessment responses and submitting them as your own
original analysis. See Section 3 for the detailed AI use policy.

---

## 3. Artificial Intelligence (AI) Use Policy

### The Principle

AI tools are permitted as **learning aids**. They are not permitted as
**assessment substitutes**.

The distinction: using AI to understand a concept better is encouraged. Using AI
to generate the analysis or written response you then submit as your own work is
a violation of academic integrity.

### Permitted AI Use

You **may** use AI tools to:
- Explain a concept you don't understand (e.g., "explain how STIX bundles work")
- Debug code or lab configurations ("why is this Python script throwing a TypeError")
- Review the clarity of writing you have already drafted ("is this sentence clear?")
- Brainstorm an approach before you do your own analysis
- Summarise a long reference document to help you decide if it's worth reading in full

### Prohibited AI Use

You **must not** use AI tools to:
- Generate the substantive analysis in an assessment response
- Write a lab report describing steps you did not actually perform
- Draft your threat intelligence report, risk assessment, or forensic findings
- Produce code for an assessment that requires you to write code
- Substitute for doing the lab exercise yourself

### Disclosure Requirement

If you used AI tools in the preparation of an assessment, you must disclose this in
your submission. State which tools you used and for what purpose. Example:

> *"I used Claude to check the clarity of Section 2 after I had drafted it. The analysis
> and findings are my own."*

Failure to disclose AI use when it occurred is itself an integrity violation.

### Why This Matters in Cybersecurity

Cybersecurity roles require genuine technical judgement that AI cannot provide
on your behalf in a live environment. An incident responder who cannot actually
perform triage, or a threat hunter who cannot run a real query, will be exposed
immediately. Your portfolio needs to reflect real capability.

Additionally, AI tools can generate plausible-sounding but technically incorrect
cybersecurity analysis. If you submit AI-generated content without understanding
it, you may be submitting factual errors — which directly undermines the accuracy
requirements of this degree (Rule R5 in `CONTRIBUTING.md`).

---

## 4. Collaboration Policy

### When Collaboration Is Permitted

Some assessments explicitly permit or require peer collaboration. Where an assessment
says "complete individually", it means individually.

Discussing concepts, sharing resources, and helping each other understand material
is always permitted and encouraged — the community is built on this.

What is not permitted is sharing assessment responses, co-writing submissions, or
dividing up and sharing sections of an individual assessment.

### Pair Lab Work

For lab exercises, two students may work together in the same environment if they
both complete all steps themselves and both write their own independent lab reports.
Sharing a single lab report between two students is collusion.

---

## 5. Consequences

### Self-Directed Learners

This degree operates on an honour system. There is no external enforcement body.
The consequences of academic dishonesty are professional, not academic:

- A portfolio built on dishonest work is a liability in a technical interview
- Experienced practitioners can identify AI-generated cybersecurity analysis
- Fabricated lab evidence will be exposed when you cannot demonstrate the skill live

### Facilitated Delivery

If you are studying through a university, employer, or bootcamp delivery partner,
that institution's academic integrity policy and consequences apply. This policy
is the minimum standard; delivery partners may apply stricter rules.

Typical consequences in facilitated delivery include:
- Requirement to resubmit the assessment
- Grade penalty (Developing or Beginning on affected rubric criteria)
- Exclusion from the unit or program at the facilitator's discretion

### Community Contributions

Contributors who plagiarise content submitted as pull requests will have their
contributions rejected and, for repeated violations, may be blocked from contributing.
See `docs/governance.md` and Rule R6 in `CONTRIBUTING.md`.

---

## 6. Referencing Standard

Use the **APA 7th edition** referencing style for all written assessments.

For MITRE ATT&CK references:
> MITRE. (Year). *Technique name* [Tactic]. MITRE ATT&CK. https://attack.mitre.org/techniques/TXXXX/

For ASD/ACSC publications:
> Australian Signals Directorate. (Year). *Publication title*. Australian Government. https://www.asd.gov.au/...

For legislation:
> *Privacy Act 1988* (Cth).
> *Security of Critical Infrastructure Act 2018* (Cth).

---

## 7. Raising Integrity Concerns

If you observe academic integrity violations by other students in a facilitated
delivery context, raise the concern with your facilitator.

For concerns about the integrity of published unit content (e.g., suspected
plagiarism in course materials), raise a GitHub Issue with the label `integrity-concern`.
