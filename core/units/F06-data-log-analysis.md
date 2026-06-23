# F06: Data & Log Analysis

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Almost everything a defender does eventually comes down to reading data: logs,
events, flows, alerts. This unit builds the data-handling and log-analysis skills
that make a practitioner effective in a SOC, a hunt team, or an investigation.
Learners study what logs exist and where, how to normalise and parse them, how to
search and correlate at scale, and how to apply simple statistics and
visualisation to separate signal from noise. It is the capstone of the Foundation
Year, drawing together the networking (F01), systems (F02), and scripting (F03)
skills into the single most-used operational competency.

In the Australian context, effective logging and analysis is both an Essential
Eight expectation (centralised, time-synchronised logging supports detection and
incident response) and a prerequisite for meeting incident-reporting obligations
under the NDB scheme and SOCI Act — you cannot report what you cannot see. F06 is
a direct prerequisite for OC02 (Security Monitoring & SIEM), OC04 (Incident
Response), and the Detection Engineering, Threat Hunting, and DFIR majors.

---

## Prerequisites

- F01 — Networking Fundamentals
- F02 — Operating Systems & Administration
- F03 — Scripting & Automation

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Identify** the major sources of security-relevant log and event data across
   networks, endpoints, and applications.
2. **Explain** log formats, normalisation, parsing, and the importance of
   accurate, synchronised timestamps.
3. **Demonstrate** searching, filtering, and correlating log data using
   command-line tools and a free log-analysis platform.
4. **Apply** basic statistical and visualisation techniques to detect anomalies
   and summarise large datasets.
5. **Use** structured analytic techniques to reconstruct a sequence of events
   from multiple log sources.
6. **Explain** how sound logging practices support Australian incident-reporting
   obligations and the Essential Eight.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of
security log sources, formats, and analysis methods across networks, endpoints,
and applications.

**Skills (AQF 7.2):** Students develop technical skills by parsing, searching,
and correlating data, and cognitive skills by interpreting patterns and
reconstructing event sequences.

**Application (AQF 7.3):** Students apply these skills to reconstruct a realistic
incident timeline from multiple sources, relating their work to Australian
logging expectations and reporting obligations.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0166 | Perform event correlation using information from multiple sources to gain situational awareness | Lab 2 — Multi-Source Timeline Reconstruction |
| NIST NICE DCWF | 2023 | Cyber Defense Analyst | PR-CDA-001 | T0259 | Identify and analyse anomalous activity in log and event data | Lab 1 — Log Triage with CLI & a Free SIEM |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Security operations | SCAD | Level 3 | Lab 1 |
| Data analysis | DTAN | Level 3 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Cyber Defence | Log & Event Analysis | Foundational | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F06-K01 | Knowledge of security-relevant log sources across network, endpoint, and application | Topic 1 |
| Knowledge | F06-K02 | Knowledge of log formats, normalisation, and the role of synchronised timestamps | Topic 2 |
| Knowledge | F06-K03 | Knowledge of statistical and frequency techniques for anomaly detection | Topic 4 |
| Skill | F06-S01 | Skill in searching, filtering, and correlating logs with CLI tools and a SIEM | Lab 1 |
| Skill | F06-S02 | Skill in reconstructing an event timeline across multiple sources | Lab 2 |
| Ability | F06-A01 | Ability to surface anomalies using least-frequency-of-occurrence analysis | Lab 1; Summative |
| Ability | F06-A02 | Ability to relate logging quality to Australian incident-reporting obligations | Topic 6; Summative |
| Task | T0166 | Perform event correlation using information from multiple sources | Lab 2 |
| Task | T0259 | Identify and analyse anomalous activity in log and event data | Lab 1 |

---

## Topics

### Topic 1: Log Sources and Telemetry

Defenders draw on many data sources, each with strengths and blind spots. This
topic surveys the landscape: network telemetry (firewall, DNS, proxy, Zeek/flow),
endpoint telemetry (Windows Event Log, Sysmon, Linux auditd/journald),
authentication and identity logs, and application/cloud logs. Learners learn to
reason about coverage — what each source can and cannot tell you.

**Key concepts:**
- Network vs endpoint vs identity vs application/cloud telemetry
- High-value events (process creation, authentication, DNS)
- Coverage and blind spots

---

### Topic 2: Log Formats, Parsing, and Normalisation

Raw logs come in many formats — syslog, JSON, CSV, key-value, Windows EVTX. To
analyse them together they must be parsed and normalised to common fields. This
topic covers common formats, parsing with `grep`/`awk`/`sed` and Python, field
normalisation, and the critical role of accurate, synchronised timestamps (and
time zones) in any investigation.

**Key concepts:**
- Common log formats and how to parse each
- Normalisation to a common schema
- Timestamps, time zones, and clock synchronisation (NTP)

**Australian context:** ACSC logging guidance stresses time synchronisation and
retention; a one-hour timestamp error breaks an investigation.

---

### Topic 3: Searching, Filtering, and Correlation

Finding the needle requires search. This topic moves from command-line search
(grep pipelines) to a free log-analysis platform (OpenSearch/Elastic free tier or
Splunk Free), covering query syntax, filtering, field extraction, and — the core
skill — correlation: linking events across sources by shared fields (user, host,
IP, time) to build a picture.

**Key concepts:**
- From grep pipelines to platform queries
- Field extraction and filtering
- Correlation by shared entities and time

---

### Topic 4: Statistics and Anomaly Detection

Volume hides threats; statistics surface them. This topic introduces simple but
powerful techniques: frequency analysis (rare is often interesting), aggregation
and counting, baselining "normal", and stacking/long-tail analysis. The emphasis
is on practical heuristics a foundation learner can apply immediately, not formal
statistics.

**Key concepts:**
- Frequency analysis and the value of rarity
- Aggregation, counting, and "least frequency of occurrence"
- Baselining and detecting deviation

---

### Topic 5: Visualisation and Reporting

A good chart communicates what a table cannot. This topic covers choosing the
right visualisation (time series for volume over time, bar charts for top-N,
heatmaps for activity patterns), building dashboards in a free platform, and
writing clear, evidence-backed analytic findings for both technical and
non-technical audiences.

**Key concepts:**
- Matching visualisation to question
- Dashboards as living analysis
- Writing defensible, evidence-linked findings

---

### Topic 6: Event Reconstruction and Logging for Compliance

The unit culminates in reconstructing "what happened" from multiple sources — the
core of triage and investigation — using structured analytic techniques to avoid
bias. It also connects logging practice to obligations: adequate, retained,
synchronised logs are what make NDB and SOCI incident reporting possible, and
centralised logging is an Essential Eight-aligned expectation.

**Key concepts:**
- Reconstructing an event timeline across sources
- Structured analysis and avoiding confirmation bias
- Logging for detection, response, and Australian reporting obligations

**Australian context:** Connects logging directly to NDB/SOCI reporting and the
Essential Eight expectation of centralised, retained logging.

---

## Labs & Exercises

### Lab 1: Log Triage with CLI & a Free SIEM

**Objective:** Triage a set of logs first with command-line tools, then in a free
log-analysis platform, to identify anomalous activity.

**Prerequisites:**
- Topics 1–4 and F03

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: `grep`/`awk`/`sort`/`uniq`, Python 3, and a free SIEM/log platform
  (OpenSearch or Splunk Free) — all free
- Minimum hardware: 6 GB RAM / 2 vCPU / 30 GB disk (within the 8 GB / 4-core /
  50 GB spec; no GPU). Run the platform single-node.

**Instructions:**

1. Given a sample auth log and web-access log, use a `grep`/`awk`/`sort`/`uniq`
   pipeline to count failed logins per source IP and identify the top offenders.
2. Identify a likely brute-force source from the rate and pattern of failures.
3. Ingest the same logs into the free log platform.
4. Reproduce the failed-login analysis as a platform query, then add a time-series
   visualisation of failures over time.
5. Use frequency analysis to find the *rarest* user-agent or URL in the access
   log and assess whether it is suspicious.
6. Record findings with the exact query and evidence for each.

**Expected Output:**

A CLI analysis and an equivalent platform query both identifying the brute-force
source, a time-series chart of failures, and a short note on the rarest
artefact found via frequency analysis — each finding backed by its query and
evidence.

**Reflection Questions:**

1. When is the command line better than a SIEM platform, and vice versa?
2. Why is "least frequency of occurrence" often more useful than looking for
   high-volume activity?
3. What logging gaps would have prevented you from reaching your conclusion?

---

### Lab 2: Multi-Source Timeline Reconstruction

**Objective:** Reconstruct an incident timeline by correlating events across
network, endpoint, and authentication logs.

**Prerequisites:**
- Topics 2, 3, 5, and 6 and Lab 1

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: the free log platform from Lab 1, plus a spreadsheet/markdown for the
  timeline
- Minimum hardware: as Lab 1

**Instructions:**

1. Ingest three correlated sample sources: a firewall/DNS log, an endpoint
   process-creation log (Sysmon-style), and an authentication log.
2. Normalise timestamps to a single time zone (UTC) and confirm clock alignment.
3. Starting from one indicator (e.g. a suspicious external IP), pivot across
   sources by shared fields (IP → host → user) to find related events.
4. Build a chronological timeline of the activity (initial contact → execution →
   authentication → follow-on action).
5. Use a structured technique: explicitly list alternative explanations for the
   activity and the evidence for/against each before concluding.
6. Write a one-page findings summary with the timeline and an assessed narrative.

**Expected Output:**

A normalised, chronological multi-source timeline; an explicit consideration of
alternative explanations; and a one-page findings summary with an assessed
narrative and confidence statement. Each timeline entry cites its source event.

**Reflection Questions:**

1. How did correlating across sources change your interpretation versus any
   single source alone?
2. How would a one-hour clock skew on one source have affected your timeline?
3. How does this reconstruction support an organisation's NDB/SOCI reporting
   obligations?

---

## Assessment

### Formative Assessment: Query & Parse Drills

**Type:** Hands-on drills with answer key

**Description:** A set of short tasks — write a pipeline to count X, a platform
query to find Y, a regex to extract Z — each with a known correct result.
Self-marked against the key.

**Learning Outcomes Assessed:** LO2, LO3, LO4

**Feedback mechanism:** Answer key with a model query/command and expected output
for each drill.

---

### Summative Assessment: Incident Analysis Report

**Type:** Practical analysis report

**Description:** Students are given a multi-source log dataset containing a
realistic intrusion. They must (a) triage and identify the anomalous activity,
(b) reconstruct a timeline by correlating across sources, (c) apply at least one
statistical/frequency technique, (d) present findings with appropriate
visualisations, and (e) state how the available logging supports — or fails to
support — Australian reporting obligations. Deliverable: 1,500–2,000 word report
with charts and an evidence appendix.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO5, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Triage & anomaly identification | LO1, LO3, LO4 |
| Timeline reconstruction | LO2, LO5 |
| Visualisation & reporting | LO5 |
| Logging-for-compliance discussion | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Analytical accuracy | Correctly identifies and explains all key activity | Identifies most activity with minor errors | Identifies some; notable gaps | Misreads the data |
| Correlation & timeline | Precise, well-evidenced multi-source timeline | Sound timeline with small gaps | Partial or weakly evidenced timeline | Little correlation across sources |
| Technique & visualisation | Apt statistics and clear, purposeful visuals | Adequate technique and visuals | Basic or poorly chosen visuals | Little technique; unclear visuals |
| Compliance reasoning | Insightful link to NDB/SOCI/Essential Eight | Valid compliance link | Superficial link | No meaningful link |
| Communication | Clear, structured, evidence-linked | Clear with minor lapses | Understandable but disorganised | Unclear |

---

## Australian Context

This unit incorporates the following Australian context:

- **ACSC logging guidance & Essential Eight:** Centralised, time-synchronised,
  retained logging is framed as an Australian baseline expectation (Topics 2, 6).
- **Notifiable Data Breaches scheme (OAIC):** Logging quality is connected to the
  ability to assess and report breaches (Topic 6, Lab 2).
- **Security of Critical Infrastructure Act 2018:** Incident reconstruction is
  linked to SOCI incident-reporting obligations (Lab 2, summative).

---

## Further Reading

**Australian Cyber Security Centre (2024).** *Best Practices for Event Logging and Threat Detection.* ACSC. https://www.cyber.gov.au
> Relevance: The authoritative Australian guidance on logging practice underpinning this unit (Australian source).

**Chuvakin, A., Schmidt, K. & Phillips, C. (2012).** *Logging and Log Management.* Syngress.
> Relevance: A comprehensive grounding in log sources, formats, and management for Topics 1–3.

**Bejtlich, R. (2013).** *The Practice of Network Security Monitoring.* No Starch Press.
> Relevance: Connects network telemetry and analysis to defensive operations, supporting Topics 1 and 6.

**Elastic / OpenSearch (2024).** *Documentation & query reference.* https://opensearch.org/docs/
> Relevance: The free platform documentation used directly in Labs 1 and 2.

**Office of the Australian Information Commissioner (2024).** *Data breach preparation and response.* OAIC. https://www.oaic.gov.au
> Relevance: Connects log analysis to Australian breach-assessment and notification obligations (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F06 |
| Unit Title | Data & Log Analysis |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01, F02, F03 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Privacy Act 1988 (NDB scheme); Security of Critical Infrastructure Act 2018 (contextual) |
