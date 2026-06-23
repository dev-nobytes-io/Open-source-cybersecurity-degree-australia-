# F03: Scripting & Automation

> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-06-21
> **Domain Expert:** _Unassigned — required before Practitioner Approved_
> **Practitioner Reviewer:** _Unassigned — required before Practitioner Approved_

---

## Overview

Modern security work is automation work. Whether a practitioner is parsing logs,
enriching indicators, deploying a lab, or pushing a configuration to a hundred
hosts, the leverage comes from code. This unit builds practical fluency across
the languages a cybersecurity professional actually meets on the job: **Python**
as the general orchestration spine, **Bash** for Linux automation, **PowerShell**
for Windows and Active Directory automation, **Ansible** and **Terraform** for
infrastructure as code, **Docker** Compose/YAML for reproducible environments,
**Cisco IOS** syntax for network device configuration, and **Lua** for extending
security tools such as Nmap NSE and Metasploit modules. The goal is not mastery
of every language but the ability to read, adapt, and write automation in the
right tool for the task.

In the Australian context, automation is how the ASD *Essential Eight* moves from
a document to an enforced reality — patch automation, configuration as code, and
automated logging are how organisations sustain maturity at scale. F03 underpins
every later operational unit: detection engineering, SIEM content, malware
triage, and threat-intel enrichment are all code-driven.

---

## Prerequisites

- F01 — Networking Fundamentals
- F02 — Operating Systems & Administration

---

## Learning Outcomes

By the end of this unit, students will be able to:

1. **Explain** the role of scripting and automation in security operations and
   select an appropriate language for a given task.
2. **Demonstrate** core programming constructs (variables, control flow,
   functions, data structures, error handling) in Python.
3. **Use** Bash and PowerShell to automate common Linux and Windows/Active
   Directory administrative tasks.
4. **Implement** infrastructure as code using Ansible, Terraform, and Docker
   Compose to build a reproducible lab environment.
5. **Describe** how domain-specific syntaxes (Cisco IOS configuration, Lua tool
   extensions) are used to configure devices and extend security tooling.
6. **Apply** safe coding practices — input validation, secrets handling, and
   version control — when writing automation that touches real systems.

---

## AQF Level 7 Alignment

**Knowledge (AQF 7.1):** This unit develops broad and coherent knowledge of
programming and automation across general-purpose, administrative, and
infrastructure-as-code languages used in cybersecurity.

**Skills (AQF 7.2):** Students develop technical skills by writing working
scripts and infrastructure definitions, and cognitive skills by selecting tools
and structuring solutions to automation problems.

**Application (AQF 7.3):** Students apply these skills to build a reproducible
lab and automate security-relevant tasks, following safe coding and
version-control practices appropriate to a professional Australian workplace.

---

## Framework Mappings

### NIST NICE DCWF

| Framework | Version | Work Role | Code | T-Code | Task Description | Demonstrated In |
|---|---|---|---|---|---|---|
| NIST NICE DCWF | 2023 | Software Developer | SP-DEV-001 | T0077 | Develop secure code and scripts to automate and support cyber tasks | Lab 1 — Python Log-Parsing & Enrichment Tool |
| NIST NICE DCWF | 2023 | System Administrator | OM-ADM-001 | T0431 | Automate system administration tasks across platforms | Lab 2 — Infrastructure as Code Lab Build |

### SFIA 9

| Skill | Code | Level | Demonstrated In |
|---|---|---|---|
| Programming/software development | PROG | Level 3 | Lab 1 |
| Configuration management | CFMG | Level 3 | Lab 2 |

### ASD Cyber Skills Framework

| Domain | Sub-domain | Proficiency | Demonstrated In |
|---|---|---|---|
| Technical Foundations | Automation & Scripting | Foundational | Lab 1, Lab 2 |

### NICE/DCWF KSATs

> Knowledge, Skills, Abilities, and Tasks developed in this unit, each tied to
> evidence. IDs are project-local (provisional) pending Framework Custodian mapping
> to official NICE/DCWF identifiers. Coverage metrics: `docs/ksat-coverage.md`.

| Type | ID | Statement | Demonstrated In |
|---|---|---|---|
| Knowledge | F03-K01 | Knowledge of core programming constructs in Python | Topic 2; Lab 1 |
| Knowledge | F03-K02 | Knowledge of administrative automation with Bash and PowerShell | Topic 3 |
| Knowledge | F03-K03 | Knowledge of infrastructure as code (Ansible, Terraform, Docker) | Topic 4; Lab 2 |
| Knowledge | F03-K04 | Knowledge of safe-coding and secrets-handling practices | Topic 6; Lab 1 |
| Skill | F03-S01 | Skill in writing Python to parse and enrich security-relevant data | Lab 1 |
| Skill | F03-S02 | Skill in building a reproducible lab with infrastructure as code | Lab 2 |
| Ability | F03-A01 | Ability to select an appropriate language/tool for an automation task | Topic 1; Formative |
| Ability | F03-A02 | Ability to apply safe-coding practices to automation that touches real systems | Topic 6; Summative |
| Task | T0077 | Develop secure code and scripts to automate and support cyber tasks | Lab 1 |
| Task | T0431 | Automate system administration tasks across platforms | Lab 2 |

---

## Topics

### Topic 1: Why Automate — Choosing the Right Tool

Automation reduces toil, removes human error from repetitive tasks, and makes
work reproducible and auditable. But each language has a niche. This topic frames
the landscape: Python for general orchestration and data work; Bash for Linux
glue; PowerShell for Windows/AD; Ansible/Terraform for infrastructure; Docker for
packaging; domain syntaxes (Cisco IOS, Lua) for devices and tools. Learners
develop the judgement to pick the right tool rather than forcing one everywhere.

**Key concepts:**
- Idempotency, reproducibility, and auditability as automation goals
- Matching language to task domain
- The cost of automation: maintenance, testing, and brittleness

---

### Topic 2: Python — The Orchestration Spine

Python is the lingua franca of security tooling. This topic covers the core
constructs — variables and types, control flow, functions, lists/dicts, file
I/O, exceptions — and the patterns that recur in security scripts: parsing
structured and semi-structured data, calling APIs, and using the standard
library (`re`, `json`, `csv`, `subprocess`, `pathlib`). It establishes the
foundation that OC02/OC05 and the detection-engineering major build on.

**Key concepts:**
- Core constructs and idiomatic Python
- Parsing logs and JSON; calling HTTP APIs with `requests`
- Structuring a small, reusable script (functions, `__main__`, arguments)

---

### Topic 3: Bash and PowerShell — Administrative Automation

Bash automates the Linux estate; PowerShell automates the Windows and Active
Directory estate. This topic contrasts the two: Bash's text-stream/pipe model
versus PowerShell's object pipeline. Learners write Bash for log rotation and
service checks, and PowerShell for querying AD users, examining event logs, and
bulk endpoint tasks. PowerShell's centrality to both Windows administration and
to adversary tradecraft makes it a defender's must-know.

**Key concepts:**
- Bash: pipes, redirection, loops, `grep`/`awk`/`sed`, exit codes
- PowerShell: cmdlets, the object pipeline, `Get-`/`Set-` verbs, AD modules
- Why PowerShell logging matters to defenders (links to F06/OC02)

**Australian context:** ACSC guidance specifically calls for PowerShell logging
and constrained language mode; learners see both the offensive and defensive
sides.

---

### Topic 4: Infrastructure as Code — Ansible, Terraform, Docker

Infrastructure as code (IaC) makes environments reproducible and reviewable.
This topic introduces three complementary tools: **Terraform** to *provision*
infrastructure declaratively, **Ansible** to *configure* hosts idempotently, and
**Docker Compose** (YAML) to *package* services. Learners see how IaC is both an
operational efficiency and a security control — configuration drift is an attack
surface, and code review of infrastructure is a defensive practice.

**Key concepts:**
- Declarative vs imperative; provisioning vs configuration
- Terraform resources/state; Ansible playbooks/idempotency; Docker Compose files
- Configuration drift and why IaC reduces it

---

### Topic 5: Domain-Specific Syntaxes — Cisco IOS and Lua

Not all automation is general-purpose. Network devices are configured in vendor
syntaxes such as **Cisco IOS**, and security tools are extended in embedded
languages such as **Lua** (used by Nmap's NSE and within tools like Metasploit's
broader ecosystem and many others). This topic gives learners reading-level
fluency: interpreting an IOS configuration to assess a device's security posture,
and reading a simple Lua/NSE script to understand what a tool extension does.

**Key concepts:**
- Cisco IOS configuration structure (modes, ACLs, interface config)
- Reading device configuration for security review
- Lua basics and how tools embed it for extensibility

---

### Topic 6: Safe and Maintainable Automation

Automation that touches real systems can do real damage. This topic covers the
professional practices that make automation safe: input validation, never
hard-coding secrets (environment variables and secret stores), least-privilege
service accounts, dry-run/idempotent design, testing, and version control with
Git. It also covers the ethics and authorisation boundaries of writing tooling
that interacts with systems.

**Key concepts:**
- Secrets handling and avoiding credential leakage in code/repos
- Idempotency, dry-run modes, and testing before production
- Git basics: commits, branches, and code review as a control

**Australian context:** Secrets leakage in public repositories is a recurring
cause of breaches reported under the Notifiable Data Breaches scheme; safe
secrets handling is framed as a breach-prevention skill.

---

## Labs & Exercises

### Lab 1: Python Log-Parsing & Enrichment Tool

**Objective:** Write a Python script that parses a log file, extracts indicators,
and enriches them — demonstrating core Python and security-relevant data work.

**Prerequisites:**
- Topics 2 and 6
- Python 3 installed in a local VM

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Python 3 (standard library; `requests` optional), Git
- Minimum hardware: 2 GB RAM / 2 vCPU / 10 GB disk (well within spec; no GPU)

**Instructions:**

1. Initialise a Git repository and create a virtual environment.
2. Given a sample web-server access log, write a function that reads the file and
   returns a list of (timestamp, source IP, request path, status code) records.
3. Use the `re` module to extract all source IP addresses; count requests per IP
   and print the top 10.
4. Add a function that flags IPs exceeding a configurable request threshold
   (a crude rate-limit/scan heuristic).
5. Handle errors gracefully (missing file, malformed line) with exceptions.
6. Read any configurable value (e.g. threshold) from an environment variable or
   argument — **do not** hard-code secrets or paths.
7. Commit your work with a clear message and confirm no secrets are tracked.

**Expected Output:**

A runnable script that prints a ranked list of source IPs and flags those over
threshold, with graceful handling of bad input, committed to Git with no
hard-coded secrets. Learners can explain each function's purpose.

**Reflection Questions:**

1. How would you extend this script to enrich each IP against a threat-intel
   source, and what API-handling concerns arise? (Links to OC05.)
2. Why is reading configuration from the environment safer than hard-coding it?
3. What would you add to make this script safe to run automatically on a
   schedule in production?

---

### Lab 2: Infrastructure as Code Lab Build

**Objective:** Use Docker Compose and Ansible to build a reproducible two-service
lab environment, demonstrating infrastructure as code.

**Prerequisites:**
- Topics 3 and 4
- Docker Engine and Ansible installed in a local VM

**Environment:**
- Operating System: Ubuntu 22.04 LTS VM
- Tools: Docker + Docker Compose, Ansible (all free/OSS), Git
- Minimum hardware: 4 GB RAM / 2 vCPU / 20 GB disk (within spec; no GPU)
- *Note:* No cloud account required — everything runs locally. Terraform is
  introduced via reading/walkthrough only, so no paid cloud provider is needed.

**Instructions:**

1. Write a `docker-compose.yml` that defines two services — for example a web app
   container and a log-collector/`rsyslog` container on a shared network.
2. Bring the stack up with `docker compose up -d` and confirm both containers run.
3. Write an Ansible playbook that configures the host: installs a package,
   ensures a service is enabled, and writes a config file from a template.
4. Run the playbook twice and confirm the second run reports no changes
   (demonstrating idempotency).
5. Read the provided sample Terraform file and annotate, in comments, what each
   resource block would provision and where Terraform state would live.
6. Commit `docker-compose.yml`, the playbook, and your annotated Terraform to Git.

**Expected Output:**

A running two-container stack defined entirely in code, an idempotent Ansible
playbook (second run = "ok", no "changed"), and an annotated Terraform file,
all committed to Git. Learners can explain the difference between provisioning,
configuring, and packaging.

**Reflection Questions:**

1. How does defining infrastructure as code reduce configuration drift, and why
   is drift a security concern?
2. Why is idempotency important when automation runs repeatedly against live
   systems?
3. How could a reviewer use these files to assess the security posture of the
   environment before it is ever deployed?

---

## Assessment

### Formative Assessment: Language-Selection Scenarios

**Type:** Short-answer exercise with answer key

**Description:** Students are given six automation scenarios (e.g. "bulk-disable
500 stale AD accounts", "stand up a disposable malware-analysis VM", "configure
ACLs on 30 switches") and must choose and justify the most appropriate
language/tool for each. Self-marked against a key.

**Learning Outcomes Assessed:** LO1, LO5

**Feedback mechanism:** Answer key with the rationale for each recommended tool.

---

### Summative Assessment: Automation Project

**Type:** Practical coding project with report

**Description:** Students build a small but complete automation that solves a
security-relevant problem of their choosing (subject to approval) — for example
a log-triage tool, an account-audit PowerShell script, or an IaC lab build. The
deliverable is a Git repository plus a 1,200–1,500 word report covering the
problem, the tool choice, safe-coding measures taken, and limitations.

**Learning Outcomes Assessed:** LO1, LO2, LO3, LO4, LO6

**Assessment-Learning Outcome Mapping:**

| Assessment Task | Learning Outcomes |
|---|---|
| Working automation code in Git | LO2, LO3, LO4 |
| Tool-selection justification | LO1 |
| Safe-coding & version-control practices | LO6 |

**Rubric:**

| Criterion | Exemplary | Proficient | Developing | Beginning |
|---|---|---|---|---|
| Code correctness & quality | Correct, readable, idiomatic, with error handling | Correct with minor quality issues | Works partially; notable issues | Does not work or is unreadable |
| Tool selection & justification | Insightful, well-justified choice for the task | Sound choice with adequate justification | Defensible choice, weak justification | Inappropriate or unjustified choice |
| Safe-coding practice | No secrets in code; validated input; clean Git history | Mostly safe with minor gaps | Some unsafe patterns present | Hard-coded secrets / unsafe code |
| Communication | Clear report, accurate terminology | Clear with minor lapses | Understandable but thin | Unclear or inaccurate |

---

## Australian Context

This unit incorporates the following Australian context:

- **ASD Essential Eight:** Patch and configuration automation are framed as the
  mechanism for sustaining Essential Eight maturity at scale.
- **ACSC PowerShell guidance:** PowerShell logging and constrained language mode
  are referenced in Topic 3 as both administrative and defensive controls.
- **Notifiable Data Breaches scheme (OAIC):** Secrets leakage in code/repos is
  presented as a notifiable-breach risk, motivating safe secrets handling.

---

## Further Reading

**Matthes, E. (2023).** *Python Crash Course (3rd ed.).* No Starch Press.
> Relevance: A practical, beginner-friendly grounding in the Python used throughout this unit and the degree.

**Australian Cyber Security Centre (2024).** *Securing PowerShell in the Enterprise.* ACSC. https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration
> Relevance: Australian guidance on PowerShell logging and hardening, directly supporting Topic 3 (Australian source).

**Geerling, J. (2023).** *Ansible for DevOps.* Midwestern Mac.
> Relevance: A hands-on guide to the Ansible playbooks and idempotency demonstrated in Lab 2.

**HashiCorp (2024).** *Terraform Documentation.* https://developer.hashicorp.com/terraform
> Relevance: The authoritative, free reference for the Terraform concepts read and annotated in Lab 2.

**Office of the Australian Information Commissioner (2024).** *Notifiable Data Breaches Report.* OAIC. https://www.oaic.gov.au
> Relevance: Australian breach statistics that motivate the safe secrets-handling practices in Topic 6 (Australian source).

---

## Unit Metadata

| Field | Value |
|---|---|
| Unit Code | F03 |
| Unit Title | Scripting & Automation |
| Version | v0.1 |
| Status | Draft |
| Credit Points | 8 CP |
| Degree Layer | Foundation |
| Major / Pathway | All |
| Prerequisites | F01, F02 |
| Domain Expert | _Unassigned — required before Practitioner Approved_ |
| Practitioner Reviewer | _Unassigned — required before Practitioner Approved_ |
| Last Reviewed | 2026-06-21 |
| Framework Version — NICE DCWF | 2023 |
| Framework Version — SFIA | SFIA 9 (2023) |
| Framework Version — ASD CSF | 2024 |
| Bloom's Level (range) | 1–3 (Remember, Understand, Apply) |
| Australian Legislation Referenced | Privacy Act 1988 (Cth) — NDB scheme (contextual) |
