# TODO — degrees/operational/dfir/

**Major:** Digital Forensics & Incident Response (DFIR)
**Degree:** Bachelor of Cybersecurity Operations
**Year:** 3
**Units:** DF01–DF06

All units are currently **Planned**. No unit files have been authored yet.

---

## Files to Create

| File | Unit | Description |
|---|---|---|
| `DF01-dfir-process-legal-foundations.md` | DF01 | Chain of custody, Evidence Act 1995 (Cth), PICERL overview, AU legal obligations |
| `DF02-host-forensics.md` | DF02 | Disk imaging, Windows/Linux artefact analysis, timeline creation |
| `DF03-memory-forensics.md` | DF03 | Volatility 3, process injection, code injection, memory IOCs |
| `DF04-network-forensics.md` | DF04 | PCAP analysis, C2 traffic identification, DNS exfiltration |
| `DF05-incident-response-operations.md` | DF05 | PICERL execution, containment decisions, stakeholder comms, post-incident reporting |
| `DF06-capstone-ir-simulation.md` | DF06 | End-to-end incident on a simulated compromised network (capstone) |

---

## Bloom's Taxonomy Requirements

Units DF01–DF05: **Levels 4–5** (analyse, evaluate, recommend, apply)
Capstone DF06: **Levels 5–6** (evaluate, create, design, synthesise)

Example verbs: analyse, evaluate, construct, reconstruct, correlate, assess, recommend, report

---

## Framework Mapping Requirements

| Framework | Required |
|---|---|
| PICERL | Yes — DF01 and DF05 must map explicitly to lifecycle phases |
| NIST SP 800-61 | Yes — incident handling guide alignment |
| NIST NICE DCWF (212, 221) | Yes — T-codes traceable to lab steps |
| DoD 8140 | Yes — Cyber Investigation work role |
| SFIA 9 (SURE L4–L5) | Yes — at least 2 units |
| CIISec (Digital Forensics; Cyber Operations) | Recommended |

---

## Lab Requirements

At least 8 labs total across the major. All tools must be free or open-source.

### Required Labs Across the Major

| Unit | Lab Ideas |
|---|---|
| DF01 | Lab: Document a simulated evidence collection with proper chain of custody forms |
| DF01 | Lab: Map a simulated incident to the PICERL lifecycle phases with decision log |
| DF02 | Lab: Acquire a disk image using FTK Imager; verify hash integrity |
| DF02 | Lab: Analyse Windows artefacts (MFT, prefetch, LNK files, registry hives) from an image |
| DF03 | Lab: Analyse a memory dump with Volatility 3 — identify injected processes |
| DF03 | Lab: Extract credentials and network connections from a memory image |
| DF04 | Lab: Analyse a PCAP for C2 beaconing patterns using Wireshark |
| DF04 | Lab: Identify DNS-based data exfiltration in a packet capture |
| DF05 | Lab: Execute full PICERL cycle on a simulated compromised host |
| DF06 | Capstone: End-to-end IR simulation — detection through post-incident report |

**Tools for this major (all free or free-tier):**
- Autopsy / Sleuth Kit (disk image analysis)
- Volatility 3 (memory forensics)
- FTK Imager Free (disk imaging and acquisition)
- Wireshark (PCAP analysis)
- Plaso / log2timeline (timeline creation)
- Velociraptor (live response and triage)
- TheHive (incident case management)

---

## Australian Legal Context (Critical for This Major)

This major has the strongest Australian legal obligations of any major. Every unit should reference at least one:

- [ ] **DF01** — Evidence Act 1995 (Commonwealth): admissibility of electronic evidence, chain of custody requirements
- [ ] **DF01** — Privacy Act 1988: obligations when handling personal information during investigations
- [ ] **DF05** — Notifiable Data Breaches (NDB) scheme: mandatory reporting to OAIC when an incident involves a data breach
- [ ] **DF05** — APRA CPS 234: mandatory notification to APRA within 72 hours for regulated entities
- [ ] **DF05** — ASD/ACSC: voluntary reporting and information sharing obligations
- [ ] **DF06** — SOCI Act 2018: mandatory incident reporting for critical infrastructure operators
- [ ] All units — Australian case studies (e.g., Medibank, Optus, Latitude breaches) where appropriate

---

## Capstone Unit (DF06) Requirements

The capstone must cover the full IR lifecycle on a simulated network:

- [ ] Initial detection and triage from a simulated alert
- [ ] Evidence collection with documented chain of custody
- [ ] Host and memory forensics performed
- [ ] Network forensics performed
- [ ] Full PICERL documentation
- [ ] Post-incident report written (executive summary + technical findings + timeline)
- [ ] Mandatory NDB/APRA notification assessment included
- [ ] Deliverable suitable for professional portfolio (reference `templates/student-portfolio/index.html`)
- [ ] Community practitioner review of the capstone submission

---

## Sign-off Requirements

Before any unit can be merged:

- [ ] Domain Expert with active DFIR experience named in metadata
- [ ] Practitioner Reviewer (different from Domain Expert) named in metadata
- [ ] All PICERL phase references verified as accurate
- [ ] Australian legal references checked by someone with AU legal or compliance background
- [ ] All lab tools tested in the minimum hardware environment (8 GB RAM, 4-core, 50 GB)

See `templates/review-checklist.md` for the full pre-merge checklist.
