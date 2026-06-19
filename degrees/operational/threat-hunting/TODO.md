# TODO — degrees/operational/threat-hunting/

**Major:** Threat Hunting
**Degree:** Bachelor of Cybersecurity Operations
**Year:** 3
**Units:** TH01–TH06

All units are currently **Planned**. No unit files have been authored yet.

---

## Files to Create

| File | Unit | Description |
|---|---|---|
| `TH01-hunting-methodology-process.md` | TH01 | TaHiTI methodology, hypothesis design, hunt loops, documentation |
| `TH02-attack-for-hunters.md` | TH02 | ATT&CK technique-based hunting, Navigator usage, hunt planning |
| `TH03-host-based-hunting.md` | TH03 | Memory, process, persistence artefacts; EDR-based hunting |
| `TH04-network-based-hunting.md` | TH04 | Traffic analysis, beaconing detection, DNS anomalies |
| `TH05-hunt-operations-tooling.md` | TH05 | Jupyter notebooks, Velociraptor VQL, EDR platforms |
| `TH06-capstone-hunt-operation.md` | TH06 | Full hunt lifecycle on live-fire range (capstone) |

---

## Bloom's Taxonomy Requirements

Units TH01–TH05: **Levels 4–5** (analyse, evaluate, recommend)
Capstone TH06: **Levels 5–6** (evaluate, create, design)

Example verbs: analyse, evaluate, recommend, design, construct, prioritise, defend

---

## Framework Mapping Requirements

Each unit must include mappings for:

| Framework | Required |
|---|---|
| MITRE ATT&CK (v14+) | Yes — technique-level references required |
| NIST NICE DCWF | Yes — T-codes must be traceable to a lab or assessment |
| ASD Cyber Skills Framework | Yes — at least 1 unit |
| SFIA 9 (INAS L4–L5) | Yes — at least 2 units |
| CIISec | Recommended |

---

## Lab Requirements

Each lab must use **free or open-source tools** and must be completable with 8 GB RAM / 4-core CPU / 50 GB disk.

### Required Labs Across the Major

The major must include at least 8 labs total. Suggested distribution:

| Unit | Lab Ideas |
|---|---|
| TH01 | Lab: Develop a hunt hypothesis using TaHiTI for a given threat scenario |
| TH02 | Lab: Use ATT&CK Navigator to map a hunt plan for a specific adversary group |
| TH03 | Lab: Analyse host artefacts (prefetch, registry, event logs) using Velociraptor queries |
| TH03 | Lab: Memory analysis using Volatility 3 to identify process injection |
| TH04 | Lab: Detect C2 beaconing patterns in Zeek/Wireshark PCAP data |
| TH04 | Lab: Hunt for DNS-based exfiltration in log data |
| TH05 | Lab: Build a hunt notebook in Jupyter using Pandas + Elastic queries |
| TH05 | Lab: Execute a VQL hunt query across a simulated endpoint fleet in Velociraptor |
| TH06 | Capstone: End-to-end hunt operation on a simulated compromised environment |

**Tools for this major (all free/OSS):**
- Velociraptor (VQL endpoint hunting)
- MITRE ATT&CK Navigator
- Jupyter Notebooks + Pandas
- Elastic Stack / OpenSearch (log-based hunting)
- Zeek + Wireshark (network hunting)
- Sigma (converting hunt findings to detection rules)
- Volatility 3 (memory analysis in TH03 host hunting)

---

## Australian Context

This major must incorporate:

- [ ] **ASD Essential Eight** — hunting for gaps in Essential Eight controls (e.g., patching, application control bypass)
- [ ] **SOCI Act 2018** — detection obligations for critical infrastructure operators
- [ ] **ASD Annual Cyber Threat Report** — use real Australian threat actor TTPs as hunt scenarios
- [ ] **ACSC Alert / Advisory** — at least one hunt scenario based on a real ACSC advisory

---

## Capstone Unit (TH06) Requirements

The capstone must be a **full end-to-end hunt operation**:

- [ ] Hypothesis developed and documented using TaHiTI
- [ ] Hunt plan mapped to ATT&CK techniques
- [ ] Host-based and network-based hunt queries executed
- [ ] Findings documented in a structured hunt report
- [ ] Findings converted into at least 2 Sigma detection rules
- [ ] Final deliverable suitable for professional portfolio (reference `templates/student-portfolio/index.html`)
- [ ] Community practitioner review of the capstone submission

---

## Sign-off Requirements

Before any unit can be merged:

- [ ] Domain Expert with active threat hunting experience named in metadata
- [ ] Practitioner Reviewer (different from Domain Expert) named in metadata
- [ ] All framework T-codes verified and traceable to lab steps
- [ ] Labs tested in the minimum hardware environment

See `templates/review-checklist.md` for the full pre-merge checklist.
