# SPL-04 lab guide — Enterprise Security Engineering

**Module:** [SPL-04](../../docs/modules/splunk/spl-04-enterprise-security.md) ·
8 labs, 3 ✅ on Free, 3 📄 no platform, 2 🔒 Enterprise Security.

**Read this before starting.** The module's own warning says a trial licence is
required throughout, and for Labs 1 and 5 that is simply true. For the other six
it is not, and the difference matters: most of what ES *is* — a risk model, a
correlation search, an asset and identity fabric, a capacity model — is
architecture you can build and reason about on core Splunk. What ES adds is the
framework that makes it someone else's job to maintain.

Work the six runnable labs first. If you then buy a trial window, spend it on
Labs 1 and 5 rather than on re-doing work you have already done.

---

## Lab 1 🔒 — Deploy and Validate ES

**Blocker:** Enterprise Security is a licensed premium app. There is no free tier,
no community equivalent, and nothing here substitutes for it.

**Inside a trial window**, the lab as specified. Two things are worth planning
before you start the clock, because a trial is short:

1. ES install plus data-model acceleration over a fortnight of data takes
   longer than you expect. Start acceleration and go and do something else.
2. The `oscd_lab` app's indexes must exist *before* ES's data models will
   populate from them. Install `oscd_lab`, confirm data is in, then install ES.

**The validation report is the deliverable, and you can write most of it now.**
The module fails an install that "looks fine on the dashboards" with three empty
models, so decide in advance what proof you will accept per model. This is the
form; fill the evidence column during the trial:

| Data model | Populated by | Proving search | Acceleration state | Evidence |
|---|---|---|---|---|
| Authentication | `wineventlog`, `cloud` | `\| tstats count from datamodel=Authentication by Authentication.action` | | |
| Endpoint.Processes | `sysmon` | `\| tstats count from datamodel=Endpoint.Processes by Processes.process_name` | | |
| Web | `proxy` | `\| tstats count from datamodel=Web by Web.action` | | |
| Network_Resolution | `dns` | `\| tstats count from datamodel=Network_Resolution by DNS.query` | | |
| Risk | `risk` | `\| tstats sum(All_Risk.calculated_risk_score) from datamodel=Risk by All_Risk.normalized_risk_object` | | |

Note that `| tstats ... summariesonly=false` returning rows proves the **model
maps**; only `summariesonly=true` proves the **acceleration ran**. Reporting the
first as though it were the second is the exact failure the module is testing for,
and it is easy to do by accident.

**Without a trial**, do the CIM-mapping half against raw data. Take one index and
write the field-by-field mapping to its data model, then state every required
field you cannot populate. That gap statement is the same artefact and it is
worth more than the install.

---

## Lab 2 ✅ — Diagnose the Dependency Stack

Three injected faults at three layers. You can inject all three yourself on core
Splunk, and self-injection is better practice than being handed a broken system —
you learn what the symptom looks like from the inside.

### Fault A — a broken TA (parsing layer)

Break the parsing and watch the search layer lie to you:

```bash
# In splunk-apps/oscd_lab/local/props.conf
printf '[oscd:proxy]\nINDEXED_EXTRACTIONS = none\nKV_MODE = none\n' \
  > ../splunk-apps/oscd_lab/local/props.conf
docker compose -f docker/compose.single.yml restart
```

Then re-index. **Symptom:** events are present, `index=proxy` returns rows, and
every field-based search returns zero. The count is right; the content is gone.

**Proving search** — the discipline is to test the layer, not the symptom:

```
index=proxy | head 5 | table _raw
index=proxy | fieldsummary | table field, count, distinct_count
```

`fieldsummary` on a healthy source lists a dozen fields; on the broken one it
lists almost none while `_raw` is intact. That distinguishes *parsing* from
*ingest* in one search.

### Fault B — a stalled acceleration (summarisation layer)

⚠️ Genuinely needs a trial licence to reproduce, since Free has no scheduled
searches. **What you can do on Free** is build the detection for it, which is the
part that transfers:

```
| rest /services/admin/summarization
| eval age_hours = (now() - strptime(summary.latest_time, "%Y-%m-%dT%H:%M:%S%z"))/3600
| table title, summary.complete, summary.size, summary.latest_time, age_hours
| where 'summary.complete' < 0.9 OR age_hours > 6
```

The point is that a stalled acceleration is **silent**: `tstats summariesonly=t`
returns fewer rows, not an error, so every detection built on it quietly loses
recall. Nothing tells you. You have to ask.

### Fault C — a stale Asset & Identity lookup (enrichment layer)

Easiest to inject and the most instructive:

```bash
python3 - <<'PY'
import csv
rows = list(csv.DictReader(open('data/lookups/oscd_identities.csv')))
kept = rows[:len(rows)//2]              # half the org "leaves the company"
with open('data/lookups/oscd_identities.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(kept)
print(f"{len(rows)} -> {len(kept)} identities")
PY
```

**Symptom:** nothing breaks. Searches run, detections fire, dashboards render.
Half your findings simply have no business context attached and are therefore
silently deprioritised.

**Proving search:**

```
index=risk entity_type=user
| lookup oscd_identities.csv identity as entity OUTPUT priority, bunit
| eval enriched = if(isnull(priority), "unmatched", "matched")
| stats count by enriched
```

### The staleness process — this is the real deliverable

The module asks you to build the refresh and staleness detection that would have
caught Fault C. Three properties, all of which need monitoring, and the third is
the one people miss:

```
| inputlookup oscd_identities.csv
| stats count as identities, dc(bunit) as departments
| appendcols [ | inputlookup oscd_assets.csv | stats count as assets ]
| eval expected_identities = 227, expected_assets = 260
| eval drift = round(abs(identities - expected_identities)/expected_identities*100, 1)
| where drift > 10
```

1. **Freshness** — when did the lookup last change? A file that has not changed in
   a fortnight is either stable or dead, and you cannot tell which from the file.
2. **Volume drift** — a 50% row-count change is a failed export, not a
   restructure. Alert on the delta, not the value.
3. **Match rate** — the only one that measures the thing you actually care about.
   A lookup can be fresh, full-sized and still match nothing, because the join key
   changed format. Monitor the *fraction of events that enrich*, and you catch all
   three failure modes with one number.

**Deliverable:** per fault, the layer and the search that proved it, plus the
staleness process. Say explicitly which of your three monitors would have caught
Fault C and which would have missed it.

---

## Lab 3 ✅ — Build, Tune and Respond

`tstats` without acceleration still works — it reads indexed fields — so you can
do the authoring and tuning halves on Free. Only the adaptive response needs ES.

**Version 1.** Authentication from an unusual source, written the fast way:

```
| tstats count where index=wineventlog EventCode=4624 by _time, user, src, dest span=1h
| stats dc(src) as sources, values(src) as source_list by user
| where sources > 3
```

Measure it. Then tune with a baseline rather than a constant — the difference
between a detection that survives contact with a real estate and one that does
not:

```
| tstats count where index=wineventlog EventCode=4624 by _time, user, src span=1d
| stats dc(src) as sources by user, _time
| eventstats median(sources) as usual, p90(sources) as busy by user
| where sources > usual * 2 AND sources > 3
```

**Throttling, and why it needs justifying.** ES throttles by field and window:

```conf
# In savedsearches.conf, on the correlation search
alert.suppress = 1
alert.suppress.fields = user
alert.suppress.period = 24h
```

The justification the module wants is not "to reduce noise". It is a statement of
**what you are willing to miss**. Suppressing by `user` for 24 hours means a
second, different compromise of the same account on the same day produces no
alert. Whether that is acceptable depends on whether your response to the first
alert would have caught it anyway — and if your answer is "probably", say so and
say what makes it only probable.

**Measure both versions against ground truth**, the same way as SPL-03 Lab 2. Two
numbers per version and a sentence about what you gave up. No adjectives.

---

## Lab 4 ✅ — A Calibrated Risk Model

SPL-03 Lab 3 built a scheme. This one builds a **model**, and the difference is
risk factors — multipliers applied by context rather than by detection.

!!! note "ES 8 terminology"
    In ES 8 a correlation search is a **detection**, a notable is a **finding**,
    and a risk notable is an **intermediate finding**. `risk_object` and
    `risk_object_type` became `entity` and `entity_type` — which is why this
    dataset uses those names. Risk factors are **multipliers**, not additive
    modifiers; getting that wrong changes the arithmetic substantially.

**Ten behaviours.** Use the ten in `index=risk` or write your own. Either way,
record why each score is what it is — an undefended number is not a model.

**At least two risk factors, applied multiplicatively:**

```
index=risk
| lookup oscd_identities.csv identity as entity
    OUTPUT priority as user_priority, category as user_category, watchlist
| lookup oscd_assets.csv host as entity
    OUTPUT priority as asset_priority, category as asset_class
| eval priority = coalesce(user_priority, asset_priority, "low")
| eval factor_priority = case(priority=="critical", 2.0, priority=="high", 1.5,
                              priority=="medium", 1.0, true(), 0.8)
| eval factor_privileged = if(watchlist=="true" OR user_category=="service_account", 1.4, 1.0)
| eval adjusted = risk_score * factor_priority * factor_privileged
| stats sum(adjusted) as risk, dc(search_name) as breadth by entity, entity_type
| sort - risk
```

**Then look at what your factors did to the distribution**, which is the step
everyone skips:

```
... | eventstats avg(risk) as mean, stdev(risk) as sd
| eval z = (risk-mean)/sd
| stats count by entity_type
```

Multiplicative factors compound. Two 2.0 factors on one entity is a 4× multiplier,
and if your factors correlate — privileged users are usually also high-priority —
you have not applied two independent adjustments, you have applied one twice.
Check the correlation before you defend the model:

```
| inputlookup oscd_identities.csv
| stats count by priority, watchlist
```

**The risk incident rule.** Threshold on the adjusted score, and state the window:

```
... | where risk > 150
| eval risk_message = "Risk threshold exceeded: " . entity
| table _time, entity, entity_type, risk, breadth, risk_message
```

**Score distribution.** Plot it, do not summarise it. A heavy right tail means
your threshold is doing the work; a flat distribution means it is arbitrary.

```
index=risk | `oscd_decay(7)`
| stats sum(decayed_score) as risk by entity
| eval bucket = round(risk/50)*50
| stats count by bucket | sort bucket
```

**Calibration note.** As in SPL-03: defend a score or factor you got wrong. The
factor most likely to be wrong here is the service-account multiplier — service
accounts are privileged *and* high-volume, so a 1.4× on top of their natural
finding count puts them at the top of every queue permanently. That is a model
that has learned "service accounts exist", which is not a security finding.

---

## Lab 5 🔒 — Threat Intelligence, Including Its Failure

**Blocker:** the ES Threat Intelligence framework — `threatlist` inputs, the
threat collections, `| tstats` against the threat data models — is ES-only.

**What runs on Free** is a lookup-based approximation, and it is enough to build
and test the staleness detection, which is the transferable half:

```bash
python3 - <<'PY'
import csv, json, collections
# Build an "intel feed" from domains in the data plus plausible filler.
seen = collections.Counter()
for line in open('data/events/dns.json'):
    seen[json.loads(line)['query']] += 1
rare = [d for d, n in seen.items() if n <= 2][:150]
with open('data/lookups/threat_domains.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['domain', 'source', 'first_seen', 'confidence'])
    for d in rare:
        w.writerow([d, 'oscd-demo-feed', '2026-08-20', 'medium'])
print(f"{len(rare)} indicators written")
PY
```

```
index=dns
| lookup threat_domains.csv domain as query OUTPUT source, confidence
| where isnotnull(source)
| stats count, dc(src_host) as hosts by query, confidence
```

**Now break it.** Freeze the file, then detect the freeze:

```
| rest /services/data/lookup-table-files
| search title="threat_domains.csv"
| eval age_hours = (now() - updated)/3600
| where age_hours > 24
```

**Feed quality is the deliverable most people skip.** Ask the awkward question:
what fraction of the indicators produced an actionable match?

```
| inputlookup threat_domains.csv
| stats count as indicators
| appendcols [ search index=dns
               | lookup threat_domains.csv domain as query OUTPUT source
               | where isnotnull(source) | stats dc(query) as matched ]
| eval hit_rate = round(matched/indicators*100, 2)
```

Then the harder question the number does not answer: of the indicators that
matched, how many led to any action? A feed with a 40% hit rate and a 0% action
rate is worse than no feed, because it consumes analyst attention and produces a
sense of coverage. State that assessment even if — especially if — you are the
one who chose the feed.

---

## Lab 6 📄 — ES Content Under Version Control

No platform needed. Build the repository and the promotion path.

**Minimum viable structure:**

```
es-content/
  detections/            # savedsearches.conf stanzas, one file per detection
  lookups/
  macros/
  tests/                 # a fixture and an expected result per detection
  promote.sh
  README.md
```

**The test is the part that distinguishes this from a backup.** For each
detection, a small fixture and an assertion about what it should produce:

```bash
# tests/spray_detection.test
# Given: 45 distinct users failing from one source in one hour
# Expect: exactly 1 result, with src = 203.0.113.x
```

You can run these against the lab dataset without ES: generate a fixture, run the
search via the REST API or `splunk search`, compare the row count and key fields.
A detection that passes its test in dev and fails in production has told you
something specific — the environments differ in a way you can now name.

**The dead-content report.** Run over your own risk index or, with ES, over the
correlation-search audit log:

```
index=risk
| stats count as fired, max(_time) as last by search_name
| append [ | inputlookup detection_inventory.csv | eval fired=0 ]
| stats max(fired) as fired, max(last) as last by search_name
| eval days_since = round((now()-last)/86400, 1)
| eval verdict = case(fired==0, "never fired — broken or untestable",
                      days_since > 30, "dormant — verify or retire",
                      true(), "active")
| sort fired
```

**The classification is the whole point.** "Never fired" has two very different
causes and they need opposite responses:

- **Broken** — the search has a defect, references a field that no longer exists,
  or depends on a data model that is not populating. Fix it or delete it.
- **Genuinely rare** — the behaviour it detects has not occurred. Keep it, and
  add a **canary**: a periodic synthetic event that proves the detection still
  fires. Without a canary you cannot distinguish the two, ever.

The deliverable is marked on that distinction. A report that lists dormant
detections without classifying them has done the easy 20%.

---

## Lab 7 📄 — Size ES

Arithmetic, no platform. State every assumption; the module marks the assumptions
harder than the numbers, because the numbers are wrong the moment the estate
changes and the assumptions are what let someone re-derive them.

**Given** (or substitute your own): 500 GB/day ingest, 8 accelerated data models,
120 correlation searches, most on a 5-minute schedule.

**The three quantities:**

| Quantity | Rough model | Assumption to state |
|---|---|---|
| Acceleration disk | ~3–10% of source volume per model, per retention period | Summary size scales with *cardinality*, not raw bytes — a high-cardinality model costs far more |
| Indexer load | Acceleration searches run continuously; budget them as a standing fraction of search capacity | You are estimating concurrent searches, not CPU directly |
| Search concurrency | `searches = Σ(1 / schedule_interval) × avg_runtime` | Skew matters more than the mean — 120 searches all on `*/5` collide every five minutes |

**The concurrency arithmetic**, since it is the one that actually breaks
deployments:

```
120 searches ÷ 5-minute schedule = 24 searches/minute
× 45 s average runtime           = 18 concurrent
+ acceleration                   ≈ 8 concurrent
+ ad-hoc analyst searches        ≈ 6 concurrent
                                 = 32 concurrent
```

Against a default `max_searches_per_cpu = 1` plus base, a 16-core search head
gives you roughly 27. **You are over.** The symptom is not an error — it is
searches being *skipped*, which looks exactly like a detection that did not fire.

That is the through-line to Lab 6: skipped searches and dead content are
indistinguishable in the output. Only the scheduler log tells them apart.

```
index=_internal sourcetype=scheduler status=skipped
| stats count by savedsearch_name, reason
```

**The 30%-under-provisioned tuning recommendation.** Order your cuts and cost
each one honestly:

1. **Stop accelerating the models nothing queries.** Free, if you check first —
   audit which models your detections actually reference.
2. **Widen schedules on detections whose data is not real-time anyway.** A
   detection over a source with a 15-minute ingest latency gains nothing from a
   5-minute schedule. Free.
3. **Reduce acceleration retention** before reducing acceleration coverage. A
   30-day summary instead of 90 costs you long-baseline searches only.
4. **Only then drop a model.** Name the detections that die with it. This is the
   step where you are trading detection capability for hardware, and the trade
   should be made by someone who can sign for it, in writing.

---

## Lab 8 📄 — Build an Add-on for an Unsupported Source

Add-on Builder is free from Splunkbase, but the marks here are in the mapping and
the gap statement, not the packaging.

**Use the messy source from [SPL-02 Lab 1](spl-02.md)** — you already generated a
pipe-and-tilde delimited proxy variant with no TA. Build a real add-on for it:

1. Sourcetype definition with explicit `LINE_BREAKER`, `TRUNCATE`, `TIME_FORMAT`
   and `CHARSET` — the discipline `oscd_lab/default/props.conf` demonstrates.
2. Field extractions.
3. CIM mapping to **Web**, with an eventtype and the `web` tag.
4. Packaging: `app.conf`, `default.meta`, correct permissions.

**Validate the model, not the install.** The module is explicit about this and it
is the same trap as Lab 1:

```
| datamodel Web Web search | stats count by sourcetype
| tstats count from datamodel=Web where sourcetype=your:sourcetype by Web.action
```

An app that installs cleanly and populates nothing is the normal outcome of a
first attempt, and the search above is how you find out in a minute rather than
in a month.

**The gap statement.** Every CIM Web field you could not populate, and what the
vendor would have to emit for you to populate it:

| CIM field | Populated? | If not, what is needed |
|---|---|---|
| `action` | derived from `status` | — |
| `src`, `dest` | yes | — |
| `http_user_agent` | **no** | Source does not log it; needs a proxy config change |
| `http_referrer` | **no** | Not emitted |
| `duration` | **no** | Not emitted |

That table is the actual deliverable. It converts "our proxy TA is a bit limited"
into a specific, costed request to a specific team — which is the thing that
gets fixed, and the reason [SPL-03 Lab 4](spl-03.md)'s telemetry-gap routing
exists.
