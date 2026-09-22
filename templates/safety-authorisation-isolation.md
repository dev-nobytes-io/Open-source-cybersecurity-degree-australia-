# Template — `## Safety, Authorisation & Isolation`

Copy this section into any unit whose **Unit Metadata** declares
`| Offensive Content | Yes |`. `lint_units.py` treats the section as a required
section for such units and fails the build without it.

## Why this section exists in the file

This repository is **public** and published to MkDocs. There is no enrolment, no
identity check and no access control, so "prerequisite", "gated" and "supervised"
describe controls that do not exist here. Merging is worldwide publication.

The safety contract therefore has to **travel with the content**: whoever reads
the unit reads the boundary in the same file, whatever route brought them to it.

Model the wording on the established example in
[`docs/modules/ansible-security-automation.md`](../docs/modules/ansible-security-automation.md)
§ *Safety, Authorisation & Blast Radius*, which is the house posture — direct,
specific about the legal instrument, and written as rules rather than warnings.

---

## Template

```markdown
## Safety, Authorisation & Isolation

Read this before any lab in this unit.

<!-- One paragraph: what makes THIS unit's technique dangerous, concretely.
     Not a generic warning -- name the actual failure mode. -->

**Rules for this unit:**

1. **Labs run only against infrastructure you own or have written authorisation
   to test.** The authorisation boundary is the one taught in
   [F05](../../core/units/F05-legal-ethics-compliance.md) and
   [CE01](../../degrees/operational/cte/CE01-offensive-foundations-ethics.md):
   the *Criminal Code Act 1995* (Cth) sch 1 Part 10.7 offences turn on access,
   modification or impairment that you are **not entitled** to cause (s 476.2).
   A purely local act against a machine you do not own is more likely to engage
   the State or Territory computer offences. "It was coursework" is not a defence.
2. **Your home, employer, university or ISP network is not your lab.** Use
   self-hosted targets on host-only or internal networking.
3. **Verify egress is blocked and record that you did.** A lab target that can
   reach the internet is not isolated, whatever the intent.
4. **Snapshot before, revert after.** Every destructive step needs a documented
   reversal written before it is run.
5. **Never commit credentials, keys, live payloads or captured data.** Portfolio
   artefacts are sanitised: publish the analysis, never a working chain against
   an identifiable target. Criminal Code ss 478.3 and 478.4 turn on **intent**,
   and what you publish is evidence of intent.

<!-- Add unit-specific rules here. Keep them enforceable and specific. -->
```

---

## What this section is not

It is **not** containment. It is a contract with a reader who has already reached
the content. The controls that actually bound exposure are editorial:
pre-merge practitioner review, and the decision about what is written down at all.

A safety section that reads as though it were a technical control is worse than
none, because it invites reliance it cannot support.
