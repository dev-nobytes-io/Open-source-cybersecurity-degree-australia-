# Annual Curriculum Review Schedule

This document defines the formal schedule for reviewing all published units
and program documents. Annual review ensures currency of content, accuracy of
framework mappings, and ongoing compliance with AQF and TEQSA standards.

---

## 1. Review Principles

Every published unit must be reviewed at least once per calendar year.
The review cycle runs from January to December.

Reviews are triggered by:
1. **Scheduled annual review** (this document)
2. **Framework version update** — new release of NICE DCWF, SFIA, ATT&CK, ASD CSF, etc.
3. **Legislative change** — amendment to Privacy Act, SOCI Act, APRA CPS 234, etc.
4. **Significant threat landscape shift** — new major Australian incident, new
   ATT&CK technique category, ASD advisory
5. **Community-raised issue** — `content-review` GitHub Issue
6. **Post-delivery feedback** — issues identified during facilitated delivery

---

## 2. Annual Review Calendar

### Q1 (January–March) — Foundation Year Review

| Unit | Review Owner | Reviewers Required |
|---|---|---|
| F01 — Networking Fundamentals | Maintainer | Domain Expert (Networking), Practitioner Reviewer |
| F02 — OS & Administration | Maintainer | Domain Expert (Systems), Practitioner Reviewer |
| F03 — Scripting & Automation | Maintainer | Domain Expert (Development/Scripting), Practitioner Reviewer |
| F04 — Security Concepts | Maintainer | Domain Expert (Security), Practitioner Reviewer |
| F05 — Legal, Ethics & Australian Compliance | Maintainer | Domain Expert (Legal/Compliance), Practitioner Reviewer |
| F06 — Data & Log Analysis | Maintainer | Domain Expert (SIEM/Analytics), Practitioner Reviewer |

**Q1 also includes:** Framework Custodian review of all Foundation framework
mappings; Australian legislative currency check (Privacy Act, SOCI Act amendments).

---

### Q2 (April–June) — Operational Core Review

| Unit | Review Owner | Reviewers Required |
|---|---|---|
| OC01 — Adversary Tradecraft & TTPs | Maintainer | Domain Expert (Threat Intel/Red Team), Practitioner Reviewer |
| OC02 — Security Monitoring & SIEM | Maintainer | Domain Expert (SOC/Detection), Practitioner Reviewer |
| OC03 — Malware Analysis | Maintainer | Domain Expert (Malware Analyst), Practitioner Reviewer |
| OC04 — Incident Response | Maintainer | Domain Expert (DFIR/IR), Practitioner Reviewer |
| OC05 — Threat Intelligence | Maintainer | Domain Expert (CTI), Practitioner Reviewer |
| OC06 — Offensive Security Concepts | Maintainer | Domain Expert (Pen Testing), Practitioner Reviewer |

**Q2 also includes:** MITRE ATT&CK version check and update of all ATT&CK
technique references; NICE DCWF T-code currency check.

---

### Q2 (April–June) — Strategic Core Review (concurrent)

| Unit | Review Owner | Reviewers Required |
|---|---|---|
| SC01 — Risk Management Frameworks | Maintainer | Domain Expert (Risk), Practitioner Reviewer |
| SC02 — Security Architecture | Maintainer | Domain Expert (Architecture), Practitioner Reviewer |
| SC03 — Governance, Policy & Compliance | Maintainer | Domain Expert (GRC), Practitioner Reviewer |
| SC04 — Vendor & Supply Chain Risk | Maintainer | Domain Expert (Vendor Risk), Practitioner Reviewer |
| SC05 — Security Program Management | Maintainer | Domain Expert (CISO/Security Manager), Practitioner Reviewer |
| SC06 — Stakeholder Communication | Maintainer | Domain Expert (CISO/Communications), Practitioner Reviewer |

---

### Q3 (July–September) — Operational Majors Review

| Major | Units | Review Owner | Reviewers Required |
|---|---|---|---|
| Threat Hunting | TH01–TH06 | Maintainer | Domain Expert (TH practitioner), Practitioner Reviewer |
| DFIR | DF01–DF06 | Maintainer | Domain Expert (DFIR practitioner), Practitioner Reviewer |
| CTI | CT01–CT06 | Maintainer | Domain Expert (CTI analyst), Practitioner Reviewer |
| Detection Engineering | DE01–DE06 | Maintainer | Domain Expert (Detection Eng.), Practitioner Reviewer |
| CTE | CE01–CE06 | Maintainer | Domain Expert (Red/Purple Team), Practitioner Reviewer |

**Q3 also includes:** TIBER-AU update check; ASD CSF version check;
ATT&CK Navigator heatmap updates for all operational majors.

---

### Q4 (October–December) — Strategic Majors + Program Review

| Scope | Review Owner | Reviewers Required |
|---|---|---|
| Security Engineering (SE01–SE06) | Maintainer | Domain Expert (Architect), Practitioner Reviewer |
| Leadership & CISO (LD01–LD06) | Maintainer | Domain Expert (CISO), Practitioner Reviewer |
| GRC (GR01–GR06) | Maintainer | Domain Expert (GRC/Audit), Practitioner Reviewer |
| Program governance docs | Maintainer | All Maintainers |
| External benchmarking update | Maintainer | Framework Custodian |
| IAB annual meeting | IAB Chair | All IAB members |

**Q4 also includes:** ISO 27001/27002 currency check; APRA CPS 234 update check;
ISM (Information Security Manual) version check; annual curriculum benchmarking update.

---

## 3. Review Checklist

For each unit reviewed, the reviewer must confirm:

**Content currency:**
- [ ] All technical content is current as of the review date
- [ ] No deprecated tools or techniques are presented as current
- [ ] All lab tools are still available and free/OSS (for Foundation/Core)
- [ ] All hyperlinks are working

**Framework currency:**
- [ ] NICE DCWF work role codes and T-codes are current (check against latest DCWF)
- [ ] SFIA skill codes are current (check against SFIA 9 or latest version)
- [ ] ASD Cyber Skills Framework domain references are current
- [ ] MITRE ATT&CK technique references match the current version
- [ ] All framework version numbers in the unit are up to date

**Australian context currency:**
- [ ] Legislation references are accurate (check for amendments)
- [ ] Regulatory body references are current (ASD, OAIC, APRA, AFP, etc.)
- [ ] Case studies and examples are still appropriate

**Outcome:**
- Unit confirmed current → Status remains "Published"
- Minor updates required → Contributor opens PR; expedited review
- Significant update required → Unit status changed to "Under Review"
- Framework mapping outdated → Status changed to "Framework Review Required"

---

## 4. Trigger-Based Review Timelines

| Trigger | Review Required Within |
|---|---|
| New NICE DCWF version | 90 days |
| New SFIA version | 90 days |
| New MITRE ATT&CK version | 60 days |
| New ASD Cyber Skills Framework version | 60 days |
| Privacy Act amendment | 45 days |
| SOCI Act amendment | 45 days |
| APRA CPS 234 update | 45 days |
| ASD Essential Eight maturity model update | 45 days |
| ASD advisory impacting unit content | 30 days |
| Lab tool discontinued or paywalled | 14 days |
| Critical content error reported | 7 days |

---

## 5. Review Records

All review outcomes are recorded as GitHub Issues or PR comments.
The Framework Custodian maintains a review log updated quarterly showing:
- Which units have been reviewed in the current year
- The outcome of each review
- Any pending trigger-based reviews

The review log is stored at `docs/quality/review-log.md` (created when first
annual review cycle is completed).
