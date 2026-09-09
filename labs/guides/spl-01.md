# SPL-01 lab guide — Search Fundamentals

**Module:** [SPL-01 — Search Fundamentals](../../docs/modules/splunk/spl-01-core-user.md)
· 7 labs, all ✅ **run on Splunk Free**.

Setup: `python3 generator/generate.py --days 14` then
`docker compose -f docker/compose.single.yml up -d`.

---

## Lab 1 ✅ — Stand Up Splunk and Onboard Data

The compose file does the install; the *learning* is in inspecting what Splunk
assigned and in breaking it deliberately.

```
index=proxy | head 5 | table _time host source sourcetype index
| tstats count where index=* by index, sourcetype
```

**Break it on purpose.** Copy one events file, strip the `props.conf` stanza for
its sourcetype, and re-ingest as `oscd:broken`:

```bash
cp data/events/proxy.json data/events/broken.json
```

Add a monitor input with **no** `TIMESTAMP_FIELDS`, restart, and observe every
event landing at index time rather than event time.

```
index=proxy sourcetype=oscd:broken | eval delta=_indextime-_time | stats avg(delta)
```

**Verify:** `_time` for the broken sourcetype clusters at ingest; the correct one
spans 14 days. Explain why fixing it needs a re-index while a field extraction
would not.

## Lab 2 ✅ — The Cost of Pipeline Order

Three variants of one question, timed with the job inspector.

```
index=proxy | stats count by user | search user="alice.*"        (filter late)
index=proxy user="alice.*" | stats count by user                 (filter early)
index=proxy user="alice.*" | fields user | stats count by user    (+ trim payload)
```

**Verify:** record `eventCount`, `scanCount` and `command.search.rawdata` from the
job inspector for each. Expect a decisive gap between variant 1 and variants 2–3.

## Lab 3 ✅ — Answer an Investigative Question

*Which accounts failed to authenticate most, from which hosts, and did any then
succeed?*

```
index=wineventlog action=failure
| stats count as failures, values(src) as sources, dc(src) as src_count by user
| sort - failures | head 20
```

Then the "subsequently" half — the deliberately under-specified part:

```
index=wineventlog
| stats count(eval(action="failure")) as fails,
        count(eval(action="success")) as wins,
        earliest(_time) as first, latest(_time) as last by user, src
| where fails > 5 AND wins > 0
```

**Verify:** the password-spray source should surface. Self-check the victim:

```bash
python3 harness/verify.py answer spl03.lab2.spray_victim <username>
```

## Lab 4 ✅ — A Dashboard That Answers a Question

Three panels, each answering a stated question. Suggested:

```
index=proxy | timechart span=1h sum(bytes_out) as egress
index=wineventlog action=failure | timechart span=1h count by Logon_Type
index=cloud | stats count by src_country | sort - count
```

**Verify:** every panel has a written question. A panel that exists because it
looked good is marked down in the module.

## Lab 5 ✅ — Drill the Command Set

Fifteen questions where the obvious command is sometimes wrong. Four that
matter, with the trap named:

```
index=proxy | stats dc(dest) as sites by user | sort - sites
```
`dc` not `count` — counting rows counts visits, not distinct sites.

```
index=wineventlog | where isnull(Failure_Reason) | stats count by user
```
`isnull` not `="")` — an absent field is not an empty one.

```
index=cloud | eval rfc1918=if(cidrmatch("10.0.0.0/8", src), 1, 0) | stats count by rfc1918, src_country
```
`cidrmatch` not a string prefix — `10.2*` also matches `10.20.x` and `102.x`.
Use `cloud`, not `proxy`: every `proxy` src is internal, so the comparison there
is degenerate and would teach nothing.

```
index=sysmon | where process_name=parent_process_name
```
`where` not `search` — comparing two fields needs `where`.

**Verify:** write down the three you got wrong first. That list is the deliverable.

## Lab 6 ✅ — Read the Job Inspector

Run one search four ways: fast mode, verbose mode, 14-day range, 1-hour range.

```
index=proxy dest="*.top" | stats count by src_host
```

**Verify:** tabulate `scanCount`, `eventCount`, `command.search.index` and total
runtime for each. The time-range effect should dwarf the mode effect — that is the
Topic 27 cascade in miniature.

## Lab 7 ✅ — Enrich With a Lookup

The lookups ship with the app.

```
| inputlookup oscd_assets.csv | head 5

index=wineventlog
| lookup oscd_assets host as dest OUTPUT priority as dest_priority, bunit
| stats count by dest, dest_priority, bunit
| sort - count
```

Now the question only the enrichment answers:

```
index=wineventlog action=failure
| lookup oscd_assets host as dest OUTPUT priority as dest_priority, category
| where category="crown_jewel"
| stats count by user, dest
```

**Verify:** the raw search gives a technically correct, useless ranking; the
enriched one ranks by business criticality. Write one sentence on what happens to
every search using this sourcetype if the lookup file is deleted.
