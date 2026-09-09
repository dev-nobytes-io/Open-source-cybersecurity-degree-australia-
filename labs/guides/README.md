# Lab guides

One guide per module, covering all **69 labs** in the series.

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
| **Total** | | **69** | **31** | **21** | **12** | **5** |

**52 of 69 (75%) need no paid licence.**

## Status legend

| | Meaning |
|---|---|
| ✅ | Runs on Splunk Free with the lab dataset |
| 📄 | Design, analysis or Python — no Splunk instance needed |
| ⚠️ | Needs a trial licence (auth, alerting, acceleration, clustering, AITK) |
| 🔒 | Needs Enterprise Security or SOAR. Guide gives the spec and states the blocker plainly. |

## Before any lab

```bash
python3 generator/generate.py --days 14
python3 harness/verify.py data
cd docker && docker compose -f compose.single.yml up -d
```

See [environment](../docs/environment.md) · [data model](../docs/data-model.md) ·
[ground truth](../docs/ground-truth.md).
