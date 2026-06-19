# TODO — core/units/

This directory will hold all 18 shared unit content files: 6 Foundation Year units, 6 Operational Core units, and 6 Strategic Core units.

**Current status: No unit files exist yet. All are Planned.**

---

## Files to Create

Use `templates/unit-template.md` as the base for every file. Copy the template, rename it, and fill in all required sections. Do not remove any template section.

### Foundation Year (F01–F06)

| File to Create | Unit | Layer | Bloom's Level |
|---|---|---|---|
| `F01-networking-fundamentals.md` | Networking Fundamentals | Foundation | 1–3 (define, explain, demonstrate) |
| `F02-operating-systems.md` | Operating Systems & Administration | Foundation | 1–3 |
| `F03-scripting-automation.md` | Scripting & Automation | Foundation | 1–3 |
| `F04-security-concepts.md` | Security Concepts & Principles | Foundation | 1–3 |
| `F05-legal-ethics-compliance.md` | Legal, Ethics & Australian Compliance | Foundation | 1–3 |
| `F06-data-log-analysis.md` | Data & Log Analysis | Foundation | 1–3 |

### Operational Core (OC01–OC06)

| File to Create | Unit | Layer | Bloom's Level |
|---|---|---|---|
| `OC01-adversary-tradecraft.md` | Adversary Tradecraft & TTPs | Operational Core | 3–4 (apply, analyse) |
| `OC02-security-monitoring-siem.md` | Security Monitoring & SIEM | Operational Core | 3–4 |
| `OC03-malware-analysis.md` | Malware Analysis Fundamentals | Operational Core | 3–4 |
| `OC04-incident-response-lifecycle.md` | Incident Response Lifecycle | Operational Core | 3–4 |
| `OC05-threat-intelligence-fundamentals.md` | Threat Intelligence Fundamentals | Operational Core | 3–4 |
| `OC06-offensive-security-concepts.md` | Offensive Security Concepts | Operational Core | 3–4 |

### Strategic Core (SC01–SC06)

| File to Create | Unit | Layer | Bloom's Level |
|---|---|---|---|
| `SC01-risk-management-frameworks.md` | Risk Management Frameworks | Strategic Core | 3–4 (apply, analyse) |
| `SC02-security-architecture.md` | Security Architecture Principles | Strategic Core | 3–4 |
| `SC03-governance-policy-compliance.md` | Governance, Policy & Compliance | Strategic Core | 3–4 |
| `SC04-vendor-supply-chain-risk.md` | Vendor & Supply Chain Risk | Strategic Core | 3–4 |
| `SC05-security-program-management.md` | Security Program Management | Strategic Core | 3–4 |
| `SC06-stakeholder-communication.md` | Stakeholder Communication | Strategic Core | 3–4 |

---

## How to Author a Unit

1. Copy `templates/unit-template.md` to this directory with the correct filename
2. Replace all placeholder text — do not leave `[brackets]` in the final file
3. Write minimum 6 substantive topic sections (paragraphs, not just bullet lists)
4. Write minimum 2 complete labs — each must specify:
   - OS and tool versions
   - Step-by-step instructions (numbered, actionable)
   - Expected output (what success looks like)
   - 3 reflection questions
5. Write 1 formative + 1 summative assessment; summative must have a 4-level rubric (Exemplary / Proficient / Developing / Beginning)
6. Complete all framework mapping rows with valid T-codes traceable to a specific lab or assessment
7. Complete the unit metadata table — all fields
8. Open a PR; request Domain Expert and Practitioner Reviewer sign-off before merging

---

## Tool Requirements for This Layer

Foundation and Core units must use **free or open-source tools only**:

| Tool Category | Approved Tools |
|---|---|
| Network analysis | Wireshark, tcpdump, Zeek, nmap |
| SIEM / Log analysis | Splunk Free, OpenSearch, Elastic Stack (free tier) |
| Endpoint analysis | Volatility 3, Autopsy, Velociraptor |
| Scripting | Python 3, Bash, PowerShell |
| Threat modelling | Microsoft Threat Modelling Tool, draw.io |
| Detection | Sigma, YARA |
| CTI platforms | OpenCTI, MISP |

Do not reference paid commercial tools in Foundation or Core labs.

---

## Minimum Hardware Spec

All labs must be completable on:
- 8 GB RAM
- 4-core CPU
- 50 GB free disk space

Document the environment requirement in every lab section.

---

## Update README.md When Units Change Status

When a unit file is merged and its status changes, update the status table in `core/units/README.md`:

```
Planned → Draft → Under Review → Practitioner Approved → Framework Verified → Published
```
