# OSCD Labs — runnable environment for the Splunk series

This directory turns the **69 labs** specified across
[EXT-SPL](../docs/modules/splunk/index.md) into something a learner can actually
run: a Splunk instance, a labelled synthetic dataset, and a verification harness.

Before this existed, every lab in the series said "provision Splunk Free" and
stopped. That gap is what this closes.

---

## Quickstart

```bash
# 1. Generate the dataset (pure stdlib, no pip install, ~15s)
python3 generator/generate.py --days 14

# 2. Confirm it is well-formed and has the properties the labs rely on
python3 harness/verify.py integrity
python3 harness/verify.py data

# 3. Start Splunk (Free licence, binds to localhost only)
cd docker && docker compose -f compose.single.yml up -d

# 4. http://localhost:8000  — then:  | tstats count where index=* by index
```

The `oscd_lab` app is mounted into the container and defines the indexes, inputs,
parsing and macros. Data is monitored from `../data` read-only.

---

## What you get

| Component | What it is |
|---|---|
| `generator/` | Pure-stdlib Python that builds a labelled 14-day estate: ~130k events across eight indexes (including derived firewall sessions and IDS alerts), 227 identities, 260 assets, 8 attack scenarios |
| `harness/verify.py` | Checks the dataset is sound, that no answers leaked, and self-checks objective lab answers |
| `docker/` | `compose.single.yml` (Free licence), `compose.distributed.yml` (search head + 2 indexers, **trial licence required**), and `compose.syslog-relay.yml` (three-node rsyslog/TLS relay path for the SA-05 labs — no Splunk needed) |
| `splunk-apps/oscd_lab/` | Indexes, inputs, explicit parsing, macros, lookup definitions |
| `guides/` | One guide per module, covering all 69 Splunk-series labs plus the 4 SA-05 labs, with setup, commands and verification |
| `docs/` | [Environment](docs/environment.md), [data model](docs/data-model.md), [ground truth](docs/ground-truth.md) |

---

## Runnability, stated honestly

The series documents a hard constraint: **Splunk Free has no authentication, no
alerting, no distributed search and no clustering**, and Enterprise Security and
SOAR are separately licensed products. That constraint is real and this lab does
not pretend otherwise.

| Status | Meaning | Labs |
|---|---|---|
| ✅ **Runs on Free** | Works with this dataset on the single-instance compose | 31 |
| 📄 **No platform needed** | Design, analysis or Python exercise | 21 |
| ⚠️ **Trial licence** | Needs auth, alerting, acceleration, clustering or AITK | 12 |
| 🔒 **Licensed product** | Needs Enterprise Security or SOAR; guide gives the spec and the blocker | 5 |

**52 of 69 labs (75%) run with no paid licence.** The per-lab status is in each
guide and summarised in [`guides/README.md`](guides/README.md).

!!! note
    The 🔒 labs are not padding. They are specified because the capability is real
    and the exam blueprints test it — but the guide says plainly what you cannot
    do without a licence rather than pretending a workaround exists.

---

## Why generate data rather than use BOTS

Splunk publishes the *Boss of the SOC* datasets, and they are good. This
generator exists anyway, for three reasons that matter to this curriculum:

1. **Ground truth.** You know exactly which events are malicious, so you can
   compute a real positive predictive value. [SPL-09](../docs/modules/splunk/spl-09-detection-analytics.md)
   Part B is arithmetic about base rates — it needs labels, not vibes.
2. **The statistics are deliberate.** The data is built to be log-normal in
   egress, seasonal by hour and weekday, overdispersed in counts, and
   contaminated by an insider who is active across the whole baseline window.
   Those are precisely the properties that make robust estimators and
   deseasonalisation *necessary* rather than merely recommended. `verify.py data`
   asserts each one.
3. **Reproducibility.** Same seed, same dataset, on any machine, forever. A
   grader can regenerate exactly what the learner saw.

```bash
python3 generator/generate.py --seed 1337 --days 14      # the default dataset
python3 generator/generate.py --seed 42 --days 30 --users 500 --out /tmp/big
python3 generator/generate.py --with-truth --out ./data-instructor   # labels inline
```

!!! warning "Assessment integrity"
    By default the `_truth_*` labels are **stripped from the events Splunk
    ingests** and written to `data/truth/` instead, keyed by `event_id`. Without
    that, every detection lab is solvable with `index=* _truth_scenario=*`.

    Do not hand learners the `truth/` directory, and do not generate their
    dataset with `--with-truth`. `verify.py integrity` checks this.

---

## A caveat on realism

The dataset is **deliberately enriched**: about 0.2% of events belong to an
attack scenario, and roughly 13% of intermediate findings are malicious. Real
enterprise base rates are orders of magnitude lower.

This is a teaching compromise, and the series is explicit about it rather than
quiet: a dataset with a realistic base rate would need hundreds of millions of
events before a single scenario appeared, which no learner can run on a laptop.
[SPL-09 Topic 5](../docs/modules/splunk/spl-09-detection-analytics.md) teaches
the real arithmetic; this dataset lets you practise the technique.

One genuine property survives the compression and is worth noticing: **lengthen
the window and the base rate falls**, because benign volume grows while the
scenarios do not.

```
--days  7    400 findings   16.8% malicious
--days 14    771 findings   12.8% malicious
--days 30  1,609 findings    6.1% malicious
```

That is Topic 5's lesson in miniature — the same detector gets worse as the
population grows.

---

## How this is kept honest

The guides make quantitative claims — a beacon channel's coefficient of
variation, a detection's positive predictive value, the funnel from 142
candidate pairs down to one user. Every one came from running the code. A change
to the generator can invalidate them without breaking anything that looks like a
test, so CI ([`.github/workflows/labs.yml`](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/blob/main/.github/workflows/labs.yml))
guards them:

```bash
python3 harness/verify.py integrity      # no ground truth leaked into the events
python3 harness/verify.py data           # the 8 statistical properties the labs need
python3 harness/check_guides.py blocks   # every embedded python block still runs
python3 harness/check_guides.py answers  # each answer still reachable by the taught method
python3 harness/check_guides.py links    # relative links resolve
```

**The `answers` check is the one with teeth.** `verify.py answer` confirms a
value against a hash. `check_guides.py answers` re-implements the *search the
guide actually teaches* and asserts it still produces that value. A generator
change that broke the taught method while leaving the labelled scenario intact
would pass the first and fail the second — which is exactly the failure that
would waste a learner's afternoon.

CI also re-runs the generator twice and diffs the output, because "same seed,
same dataset, on any machine" is a promise a grader relies on.

## Requirements

- **Python 3.8+** — standard library only, no `pip install`
- **Docker** with Compose v2, for the Splunk labs
- **~4 GB RAM** for single-instance; **~6 GB** for distributed
- No internet access needed after the Splunk image is pulled

---

## Licence

Lab **code** (`generator/`, `harness/`, `docker/`, `splunk-apps/`) is offered
under the MIT licence so it can be freely reused in other teaching contexts.
Lab **prose** (`guides/`, `docs/`) is CC BY 4.0, consistent with the rest of the
repository. See [`LICENCE-NOTE.md`](LICENCE-NOTE.md).

Splunk is a trademark of its owner. This lab is not affiliated with or endorsed
by Splunk, and using the Splunk container image is subject to Splunk's own
licence terms, which you accept via `SPLUNK_START_ARGS: --accept-license`.
