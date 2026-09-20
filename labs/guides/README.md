# Lab guides

One guide per module: all **69 labs** in the Splunk series, plus the **4 labs** of
[SA-05](../../docs/modules/security-architecture/sa-05-logging-and-monitoring-architecture.md)
from the security-architecture series, which run on a Splunk-free relay estate.

**The split of responsibility:** the module says *why* the lab exists and *what
to deliver*; the guide says *how to run it*. Marking criteria stay in the module.

| Guide | Module | Labs | ✅ Free | 📄 No platform | ⚠️ Trial | 🔒 Licensed |
|---|---|---|---|---|---|---|
| [spl-01](spl-01.md) | [Search Fundamentals](../../docs/modules/splunk/spl-01-core-user.md) | 7 | 7 | 0 | 0 | 0 |
| [spl-02](spl-02.md) | [SPL Mastery & Knowledge Objects](../../docs/modules/splunk/spl-02-power-user.md) | 8 | 7 | 0 | 1 | 0 |
| [spl-03](spl-03.md) | [SOC Analysis & Threat Detection](../../docs/modules/splunk/spl-03-cyber-defense-analyst.md) | 8 | 5 | 1 | 1 | 1 |
| [spl-04](spl-04.md) | [Enterprise Security Engineering](../../docs/modules/splunk/spl-04-enterprise-security.md) | 8 | 3 | 3 | 0 | 2 |
| [spl-05](spl-05.md) | [SOAR & Security Automation](../../docs/modules/splunk/spl-05-soar.md) | 8 | 0 | 6 | 0 | 2 |
| [spl-06](spl-06.md) | [Platform Administration](../../docs/modules/splunk/spl-06-enterprise-admin.md) | 8 | 4 | 0 | 4 | 0 |
| [spl-07](spl-07.md) | [Architecture & Deployment](../../docs/modules/splunk/spl-07-architect.md) | 7 | 0 | 4 | 3 | 0 |
| [spl-08](spl-08.md) | [Implementation & Consulting](../../docs/modules/splunk/spl-08-consultant.md) | 7 | 1 | 4 | 2 | 0 |
| [spl-09](spl-09.md) | [Detection Analytics & Risk Scoring](../../docs/modules/splunk/spl-09-detection-analytics.md) | 8 | 4 | 3 | 1 | 0 |
| [sa-05](sa-05.md) | [Logging, Monitoring & Detection Architecture](../../docs/modules/security-architecture/sa-05-logging-and-monitoring-architecture.md) | 4 | 2 | 2 | 0 | 0 |
| **Total** | | **73** | **33** | **23** | **12** | **5** |

**56 of 73 (77%) need no paid licence**, and **every one of the 69 has a written
deliverable that can be produced without a running Splunk instance.**

## Status legend

The icons say what the *platform* would give you. They do not say whether the lab is
worth doing without one — every guide is written so the paper path is the primary
route, because most of what these certifications assess is paperwork.

| | Meaning |
|---|---|
| ✅ | Runs on Splunk Free with the lab dataset |
| 📄 | Design, analysis or Python — no Splunk instance needed, by nature |
| ⚠️ | The *platform behaviour* needs a trial (auth, alerting, acceleration, clustering, AITK). The design, the conf files and the analysis do not. |
| 🔒 | The platform behaviour needs Enterprise Security or SOAR. The guide names the blocker plainly and gives the paper equivalent — it does not invent a workaround. |

## Working without a platform

This is the normal case, not the fallback. What you produce instead:

| Modality | Where it lives |
|---|---|
| **Configuration files**, written and defended | [Conf-file practice](../paper/conf-practice.md); SPL-06 Labs 1, 2, 6; SPL-08 Lab 2 |
| **Capacity and cost models** with traceable assumptions | SPL-07 Labs 1, 6; SPL-04 Lab 7 |
| **Risk and detection arithmetic** | SPL-09 Labs 2, 3, 4 — standard-library Python over the dataset files |
| **Architecture and operating-model design** | SPL-07 Labs 5, 7; SPL-08 Labs 1, 4, 5, 7; SA-05 Labs 1, 2 |
| **A syslog relay path you can break** | SA-05 Labs 3, 4 — `docker/compose.syslog-relay.yml`, no Splunk needed |
| **Structured analysis** — ACH, coverage maps, diagnosis logs | SPL-03 Labs 4, 7; SPL-06 Lab 7; SPL-07 Lab 3 |
| **Self-assessment** | [52-question quiz](../../docs/modules/splunk/quiz.md) |

The dataset is JSONL and CSV. Standard-library Python reads both, so the analytical labs
need no Splunk, no `pip install`, and no numpy or pandas — a deliberate constraint that
keeps the arithmetic visible.

## If you do have an instance

```bash
python3 generator/generate.py --days 14
python3 harness/verify.py data
cd docker && docker compose -f compose.single.yml up -d
```

See [environment](../docs/environment.md) · [data model](../docs/data-model.md) ·
[ground truth](../docs/ground-truth.md).
