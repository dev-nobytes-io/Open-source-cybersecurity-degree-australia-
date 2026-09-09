# SPL-06 lab guide — Platform Administration

**Module:** [SPL-06](../../docs/modules/splunk/spl-06-enterprise-admin.md) ·
8 labs, 5 ✅ on Free, 3 ⚠️ trial licence.

The module's own warning lists Lab 3 as needing more than a single instance.
This guide ships [`docker/compose.forwarders.yml`](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/blob/main/labs/docker/compose.forwarders.yml),
which adds a deployment server and three universal forwarders **on the Free
licence** — Free has no distributed *search*, but it accepts forwarded data and
runs a deployment server perfectly well. So Lab 3 runs here.

Labs 4, 5 and 8 genuinely need a trial: authentication, scheduled alerting and
distributed search do not exist on Free, and no configuration makes them exist.

```bash
# Labs 1, 2, 6, 7
docker compose -f docker/compose.single.yml up -d

# Lab 3 as well
docker compose -f docker/compose.single.yml -f docker/compose.forwarders.yml up -d

# Lab 8 (trial licence)
docker compose -f docker/compose.distributed.yml up -d
```

---

## Lab 1 ✅ — Index Design and a Precedence Conflict

**The design half.** Three sensitivities, two retention obligations. Use a real
Australian framing, since [R4](../../CONTRIBUTING.md) requires it and the
constraints are genuinely different from the US defaults most Splunk material
assumes:

| Index | Contents | Retention | Driving obligation |
|---|---|---|---|
| `sec_high` | Authentication, endpoint, privileged access | 7 years | APRA CPS 234 for regulated entities; ASD Essential Eight event-log guidance |
| `sec_std` | Proxy, DNS, network | 12 months | Investigative utility; volume makes longer prohibitive |
| `hr_adjacent` | Anything containing employee behavioural data | 12 months, restricted | Privacy Act 1988 APP 11 — minimise retention of personal information |

**Justify each setting, not the set.** The marks are in the reasoning, and the
reasoning has to survive an obvious challenge: *why not keep everything for seven
years?* Because APP 11.2 requires you to destroy or de-identify personal
information no longer needed, so over-retention is a compliance failure in the
opposite direction. Cost is the second reason, not the first.

```conf
# indexes.conf
[sec_high]
homePath   = $SPLUNK_DB/sec_high/db
coldPath   = $SPLUNK_DB/sec_high/colddb
thawedPath = $SPLUNK_DB/sec_high/thaweddb
frozenTimePeriodInSecs = 220752000    # 7 years
maxTotalDataSizeMB     = 2000000

[hr_adjacent]
frozenTimePeriodInSecs = 31536000     # 12 months — APP 11.2, not budget
```

!!! warning "`frozenTimePeriodInSecs` is not a retention guarantee"
    Buckets roll to frozen when **either** the age limit or `maxTotalDataSizeMB`
    is hit, whichever comes first. Set the size cap too low on `sec_high` and your
    seven-year obligation quietly becomes four months. This is the single most
    common index-design defect and it fails silently, in the direction that
    matters.

**The precedence conflict.** Create it deliberately across two layers:

```bash
docker exec -it oscd-splunk bash
# App layer
echo -e '[oscd:proxy]\nTRUNCATE = 5000' \
  > /opt/splunk/etc/apps/oscd_lab/local/props.conf
# System layer
echo -e '[oscd:proxy]\nTRUNCATE = 100' \
  > /opt/splunk/etc/system/local/props.conf
```

**Diagnose with `btool`, and read it properly:**

```bash
/opt/splunk/bin/splunk btool props list oscd:proxy --debug
```

The `--debug` flag prefixes every line with the file it came from. Without it you
see the answer and not the reason, which is useless for a conflict.

**Which layer won, and why.** For `props.conf`, `system/local` beats `apps/*/local`
beats `apps/*/default` beats `system/default`. So the truncation is **100**, and
your app's carefully considered 5000 is invisible.

But — and this is the part worth internalising — that ordering is **not universal**.
Configuration precedence in Splunk depends on context:

| Context | Ordering |
|---|---|
| Global (indexes, inputs, most parsing) | System local → app local → app default → system default |
| App/user scope (savedsearches, macros, views) | User → app (in **ASCII order** of app name) → system |

The ASCII-order rule is why an app called `000_overrides` beats one called
`zz_local`, and why people ship apps with numeric prefixes. Guessing the ordering
from memory is how you spend an afternoon on a setting that was never applied.

**Deliverable:** the design with per-setting justification, plus the `btool --debug`
output showing which layer won and the sentence explaining why that layer wins in
*this* context.

---

## Lab 2 ✅ — Onboard a Source Correctly, and Incorrectly

Build a source with a genuinely awkward timestamp. Australian date order plus a
multi-line record does it — and `%d/%m/%Y` versus `%m/%d/%Y` is a real,
recurring, silent failure in this country:

```bash
python3 - <<'PY'
import json, random
random.seed(11)
rows = [json.loads(l) for l in open('data/events/wineventlog.json')][:800]
import datetime as dt
with open('data/events/awkward.log', 'w') as f:
    for r in rows:
        t = dt.datetime.utcfromtimestamp(r['_time'])
        f.write(f"[{t.strftime('%d/%m/%Y %H:%M:%S')}] EVENT START\n")
        f.write(f"  user={r['user']} host={r['dest']} code={r['EventCode']}\n")
        f.write(f"  result={r['action']}\n")
        f.write("EVENT END\n")
print("wrote data/events/awkward.log")
PY
```

**First, carelessly.** Add a monitor input with no settings at all and let Splunk
infer. Record three specific failures:

1. **Line breaking.** Splunk breaks per line, so one four-line record becomes four
   events, three of which have no timestamp and inherit the previous one.
2. **`_time`.** `12/03/2026` is ambiguous. Splunk's default resolves it as
   **March 12**, not 3 December. Every event from the 1st to the 12th of a month
   lands in the wrong month; every event from the 13th onward parses correctly.
   That mixture is far worse than a uniform failure, because spot checks pass.
3. **Sourcetype.** Auto-assigned to something like `awkward-2`, which no
   downstream knowledge object references.

**Prove the timestamp failure rather than asserting it:**

```
index=main source=*awkward.log
| eval indexed=_indextime, parsed=_time, skew_days=round((_indextime-_time)/86400,1)
| stats count by skew_days | sort - count
```

A healthy source has one skew bucket. This one will have several.

**Then properly:**

```conf
[oscd:awkward]
SHOULD_LINEMERGE = false
LINE_BREAKER = ([\r\n]+)EVENT END[\r\n]+
TIME_PREFIX = ^\[
TIME_FORMAT = %d/%m/%Y %H:%M:%S
MAX_TIMESTAMP_LOOKAHEAD = 20
TRUNCATE = 10000
CHARSET = UTF-8
TZ = Australia/Sydney
```

**The checklist is the deliverable**, because it is the thing a colleague can use.
Sample first, always, and in this order:

1. Get 20 raw events **before** touching a config. Not a description of them.
2. Identify the record boundary. Is one event one line?
3. Identify the timestamp: its position, its format, and **its timezone** —
   which is usually undocumented and is the source's local time, not UTC.
4. Set `LINE_BREAKER`, `TIME_PREFIX`, `TIME_FORMAT`, `MAX_TIMESTAMP_LOOKAHEAD`,
   `TRUNCATE`, `CHARSET`, `TZ` **explicitly**. Inference works until the data
   changes shape, and then it fails without telling you.
5. Index into a scratch index. Verify `_time` against `_indextime` and eyeball
   `_raw`.
6. Only then assign the real index and sourcetype.

Step 3's timezone item is the one that bites hardest: a source with no timezone in
its timestamps, forwarded from a host in another state, will be wrong by two or
three hours forever, and every correlation across sources will silently miss.

---

## Lab 3 ✅ — Manage Forwarders at Scale

```bash
docker compose -f docker/compose.single.yml -f docker/compose.forwarders.yml up -d
docker compose -f docker/compose.single.yml -f docker/compose.forwarders.yml ps
```

Three forwarders phone home to the deployment server. Confirm from the DS side:

```
| rest /services/deployment/server/clients
| table hostname, ip, utsname, lastPhoneHomeTime, applications
```

**Build the server classes.** Two classes, deliberately overlapping in one host,
so the blast-radius question has an interesting answer:

```conf
# etc/system/local/serverclass.conf
[serverClass:web_tier]
whitelist.0 = uf-web-*
[serverClass:web_tier:app:oscd_inputs_web]
restartSplunkd = true

[serverClass:all_forwarders]
whitelist.0 = uf-*
[serverClass:all_forwarders:app:oscd_outputs]
restartSplunkd = true
```

```bash
docker exec oscd-splunk /opt/splunk/bin/splunk reload deploy-server
```

**Now push something bad.** The instructive failure is a config that is *valid* and
wrong, not one that fails to parse — a parse error gets caught, a valid mistake
ships:

```conf
# oscd_inputs_web/local/inputs.conf — plausible and wrong
[monitor:///var/log]
index = sec_high
recursive = true
whitelist = .*
```

That monitors everything under `/var/log`, recursively, into your seven-year
index. It will parse fine. It will be pushed to every host matching `uf-web-*`.

**Measure the blast radius before you fix it:**

```
| rest /services/deployment/server/clients
| search applications.oscd_inputs_web.*=*
| stats count as hosts_reached, values(hostname) as which
```

```
index=_internal source=*metrics.log group=per_index_thruput series=sec_high
| timechart span=1m sum(kb) as kb
```

**The recovery, in order:**

1. Remove the app from the server class (do **not** delete the app — the clients
   need something to converge onto).
2. `splunk reload deploy-server`.
3. Confirm each client picked up the change: `lastPhoneHomeTime` moves and the
   app list shrinks.
4. Clean the polluted index. `| delete` only hides data from search — the disk
   cost and the retention obligation both remain. If it went into a
   seven-year-retention index, you now have a data-handling problem as well as a
   configuration one.

**The blast-radius note is the deliverable.** Two answers are required:

- **How you detected it.** Ingest volume on `sec_high` is the fast signal, and
  it is only fast if someone is watching it. If your honest answer is "I would
  have noticed the licence warning next week", say so.
- **What would have limited it.** Phased server classes: a `canary` class of one
  host, promoted to the full class after a soak period. `restartSplunkd = false`
  where possible, so a bad push does not also take the forwarder down. And a
  positive `whitelist` on the monitor input, never `.*`.

Compare against the blast-radius discipline in
[EXT-ANS](../../docs/modules/ansible-security-automation.md) — the deployment
server has no `--check` mode, no `--limit`, and no dry run, which makes the
staged server class the only lever you have.

---

## Lab 4 ⚠️ — Least-Privilege Access Model

**Trial licence required.** The Free licence has no authentication at all — you
are dropped straight in as `admin`. This is not a limitation you can work around;
it is why [`compose.single.yml`](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/blob/main/labs/docker/compose.single.yml) binds to
`127.0.0.1` only.

**Design it now, implement it in the trial window.** Four job functions against
three sensitivities:

| Role | `sec_high` | `sec_std` | `hr_adjacent` | Capabilities |
|---|---|---|---|---|
| `soc_analyst` | read | read | **no** | `search`, `schedule_search` |
| `soc_lead` | read | read | read, **audited** | + `edit_own_objects`, `list_all_objects` |
| `platform_admin` | **no** | **no** | **no** | `admin_all_objects` minus `srchIndexesAllowed` |
| `auditor` | read | read | read | `search` only, no export |

**Two deliberate provocations in that table**, and the module demands you defend
or abandon both:

**"Security team gets everything" — abandoned.** `soc_analyst` cannot read
`hr_adjacent`. The defence is not that analysts are untrustworthy; it is that
`hr_adjacent` contains personal information whose access must be justified per
APP 6, and a standing grant to a whole team cannot be justified per-instance.
Access goes to `soc_lead`, is audited, and the audit is reviewed.

**`platform_admin` cannot read security data.** The person who administers the
platform does not need to read what is in it. This separation is the one people
resist hardest and it is the one that matters most: an administrator who can both
alter audit logging and read everything is a single point of total compromise.

```conf
# authorize.conf
[role_soc_analyst]
srchIndexesAllowed = sec_high;sec_std
srchIndexesDefault = sec_std
importRoles = user
srchJobsQuota = 5

[role_platform_admin]
importRoles = admin
srchIndexesAllowed =
```

**Test by attempting access you should not have** — the evidence is the deliverable
and a design with no negative test is not tested:

```
index=hr_adjacent | head 1
```

as `soc_analyst` must return **zero results with no error**, which is Splunk's
behaviour and is itself worth noting: an access denial that looks identical to an
empty index is a usability problem and an incident-response problem. Document how
an analyst is supposed to tell the difference.

---

## Lab 5 ⚠️ — Detect the Absence of Data

**Trial licence** for the alerting half; the detection logic runs on Free.

**The search is easy. The inventory is the lab.**

```
| tstats latest(_time) as last_seen where index=* by index, sourcetype
| eval age_min = round((now() - last_seen)/60, 1)
| where age_min > 30
```

That finds sources that *have* stopped. It cannot find a source that never
started, or one removed six months ago that everyone forgot was load-bearing. For
that you need to compare against what you **expect**:

```
| inputlookup expected_sources.csv
| join type=left index, sourcetype
    [ | tstats latest(_time) as last_seen where index=* by index, sourcetype ]
| eval age_min = round((now() - last_seen)/60, 1),
       state = case(isnull(last_seen), "NEVER SEEN",
                    age_min > max_gap_min, "STALE",
                    true(), "ok")
| where state != "ok"
| table index, sourcetype, owner, state, age_min, max_gap_min
```

```bash
python3 - <<'PY'
import csv
rows = [
    ("wineventlog", "oscd:winauth", 30,  "windows-team"),
    ("sysmon",      "oscd:sysmon",  30,  "endpoint-team"),
    ("proxy",       "oscd:proxy",   15,  "network-team"),
    ("dns",         "oscd:dns",     15,  "network-team"),
    ("cloud",       "oscd:cloud",   60,  "identity-team"),
    ("risk",        "oscd:risk",    120, "detection-eng"),
]
with open('data/lookups/expected_sources.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(["index", "sourcetype", "max_gap_min", "owner"])
    w.writerows(rows)
print(f"{len(rows)} expected sources")
PY
```

**Note the per-source `max_gap_min`.** A single global threshold is wrong: cloud
sign-ins are bursty and quiet overnight, while proxy traffic is continuous. A
30-minute rule alerts on `cloud` every night and misses `proxy` being down for
25 minutes, which is the worse outage.

**Now stop a forwarder and confirm you are told:**

```bash
docker compose -f docker/compose.single.yml -f docker/compose.forwarders.yml stop uf-web-01
```

**The inventory-maintenance question is the graded part**, and the module is right
that an inventory nobody updates is the actual failure mode. Three approaches,
with honest costs:

| Approach | How it stays current | Failure mode |
|---|---|---|
| Manual CSV, reviewed quarterly | Someone remembers | Rots within two quarters; new sources missing, dead sources alerting |
| Generated from observed data, human-approved | New sources appear as proposals | Cannot catch a source that never started |
| Generated from the CMDB / onboarding ticket queue | Onboarding creates the row | Only works if onboarding is actually ticketed |

The second is the one that survives, but only with the addition that makes it
work: **new-source proposals must expire**. A source seen for the first time
becomes a proposal; if nobody claims an owner within a fortnight, it alerts. That
converts inventory rot from a silent decay into a noisy one, which is the only
kind anybody fixes.

---

## Lab 6 ✅ — Parse It Properly, Then Route and Mask It

**HEC on Free:**

```bash
docker exec oscd-splunk /opt/splunk/bin/splunk http-event-collector create oscd-hec \
  -uri https://localhost:8089 -auth admin:oscd-lab-changeme \
  -index main -sourcetype oscd:hec
```

```bash
curl -k https://localhost:8088/services/collector/event \
  -H "Authorization: Splunk <token>" \
  -d '{"event":{"user":"test","secret":"AKIAIOSFODNN7EXAMPLE"},"sourcetype":"oscd:hec"}'
```

**Routing and masking**, all three in one `transforms.conf`:

```conf
# transforms.conf
[route_to_sec_high]
REGEX = .
DEST_KEY = _MetaData:Index
FORMAT = sec_high

[drop_health_checks]
REGEX = (?i)url="[^"]*/(healthz|ping|status)"
DEST_KEY = queue
FORMAT = nullQueue
```

```conf
# props.conf
[oscd:winauth]
TRANSFORMS-route = route_to_sec_high

[oscd:proxy]
TRANSFORMS-drop = drop_health_checks
SEDCMD-mask_keys = s/(AKIA[A-Z0-9]{16})/AWS_KEY_REDACTED/g
SEDCMD-mask_pw   = s/(password|passwd|pwd)=[^\s,]+/\1=REDACTED/g
```

**Prove the mask worked at index time, not search time.** This is the deliverable
and the distinction is the entire point:

```
index=main sourcetype=oscd:hec "AKIA*"
```

returning zero is **not** proof — a search-time field alias or a `fields` command
could be hiding it. Go to the data:

```bash
docker exec oscd-splunk grep -r "AKIAIOSFODNN7EXAMPLE" /opt/splunk/var/lib/splunk/ 2>/dev/null | head
```

Nothing on disk is proof. Anything on disk means the secret is in your index, in
your backups, and in your seven-year retention, and `SEDCMD` cannot retroactively
remove it — you would have to delete and re-index the buckets.

!!! danger "`SEDCMD` runs on the indexer or heavy forwarder, never on a UF"
    A universal forwarder does not parse, so it cannot mask. If your masking is
    meant to stop a secret leaving a host, `SEDCMD` is the wrong control entirely
    — the secret is already off the box by the time it runs.

**What `nullQueue` costs you.** Write it down before you enable it:

- The data is **gone**. Not archived, not summarised, not recoverable. If an
  incident later hinges on those health checks — proving a service was up,
  establishing a baseline, showing an attacker probed the health endpoint —
  the answer is that you cannot know.
- You will not remember it was dropped. Six months on, a gap in the data looks
  like an outage, and someone will spend a day on it.
- **Mitigation:** keep a count. Route dropped events to a metrics or summary index
  as a per-minute count before the drop, so the volume survives even though the
  content does not.

---

## Lab 7 ✅ — Diagnose Five Faults

Marked on method. The method is: **`_internal` first, in a fixed order, before any
hypothesis.** Guessing is fast and wrong; the order below is slow and right.

Inject each fault yourself, then diagnose it as though you had not.

### Fault 1 — Data not arriving

```
index=_internal source=*splunkd.log* component=TailReader OR component=WatchedFile
| stats count by log_level, component | sort - count

index=_internal source=*metrics.log group=per_sourcetype_thruput
| timechart span=5m sum(kb) by series
```

The ordering that matters: **is it not arriving, or arriving and not searchable?**
`| tstats count where index=* by index` versus the thruput metric separates the
two in one step, and they have completely different causes.

### Fault 2 — Wrong timestamps

```
index=* | eval skew = _indextime - _time
| stats count, min(skew) as min, max(skew) as max, avg(skew) as avg by sourcetype
| where abs(avg) > 3600
```

A large positive skew means events are old on arrival (backfill, or a wrong
timezone). Negative skew means **future-dated events**, which is worse — they sit
outside your default search window and are effectively invisible.

### Fault 3 — A blocked queue

```
index=_internal source=*metrics.log group=queue
| eval fill = current_size_kb / max_size_kb
| timechart span=1m max(fill) by name
```

Read this **right to left**. Queues fill backwards from the blockage: if `indexqueue`
is full and `parsingqueue` is not, the problem is downstream of parsing. The
first-full queue is the symptom; the *last* one still draining is next to the cause.

### Fault 4 — A skipped scheduled search

```
index=_internal sourcetype=scheduler status=skipped
| stats count by savedsearch_name, reason | sort - count
```

`reason` is usually concurrency limits. This is the same failure as
[SPL-04 Lab 7](spl-04.md): a skipped search and a detection that legitimately did
not fire are indistinguishable in the output. Only this log tells them apart, and
if nobody reads it, you have detections you believe in that are not running.

### Fault 5 — An instance that will not start

`_internal` is unavailable, so the method changes:

```bash
docker logs oscd-splunk 2>&1 | tail -50
docker exec oscd-splunk cat /opt/splunk/var/log/splunk/splunkd.log | tail -50
docker exec oscd-splunk /opt/splunk/bin/splunk btool check
docker exec oscd-splunk /opt/splunk/bin/splunk btool inputs list --debug 2>&1 | grep -i error
```

`btool check` is the highest-yield command here and the one people reach for last.
It validates every configuration file without starting the service, so it finds
the bad stanza in seconds.

**Deliverable: the evidence and the order you gathered it in.** Write the order
down as you go, not afterwards — reconstructing it later produces the tidy
narrative you wish you had followed rather than the one you did.

---

## Lab 8 ⚠️ — Stand Up Distributed Search

**Trial licence required.** Free has no distributed search.

```bash
docker compose -f docker/compose.distributed.yml up -d
```

**Verify the peers:**

```
| rest /services/search/distributed/peers
| table title, status, version, replicationStatus
```

**Prove distribution from the job inspector, not from the absence of errors.**
The module is specific about this because a search head with unreachable peers
runs the search *locally* and returns a smaller, entirely plausible answer.

Run a search, open **Job → Inspect Job**, and read:

- `remoteSearch` — non-empty means work was actually shipped to peers.
- `command.search.index` under **remote** timing, with a per-peer breakdown.
- Event count **per peer** in `search.remote_*`.

The cheaper check, worth building into a habit:

```
| tstats count where index=* by splunk_server
```

Every peer should appear. One missing peer is a silently wrong answer with a green
tick next to it.

### Break it two ways

**1. Stop a peer mid-search.**

```bash
docker compose -f docker/compose.distributed.yml stop idx2
```

Re-run a long search. Record precisely what happens, because the answer is worse
than "it errors":

- The search **completes**.
- Results are missing that peer's data.
- The job carries a warning — in the messages, not in the results.
- Any downstream alert or dashboard sees only the numbers.

A detection running at that moment produces a smaller count and no error. If the
detection is a threshold, it does not fire. **This is the most important
observation in the lab**: distributed search fails *partially*, and partial
failures do not look like failures.

**2. Inflate the knowledge bundle.**

```bash
python3 - <<'PY'
import csv, random, string
random.seed(3)
with open('data/lookups/bloat.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(["key", "value"])
    for i in range(400_000):
        w.writerow([f"k{i:08d}", "".join(random.choices(string.ascii_letters, k=60))])
import os
print(f"{os.path.getsize('data/lookups/bloat.csv')/1e6:.0f} MB")
PY
```

Make it an **automatic** lookup (`props.conf` `LOOKUP-bloat = ...`) so it enters
the bundle whether or not any search uses it, then re-run your searches.

```
index=_internal component=DistributedBundleReplicationManager
| table _time, log_level, event_message
```

**Record the cost**, and note that it is paid by every search:

| Measure | Before | After |
|---|---|---|
| Bundle size | | |
| Replication time | | |
| Time-to-first-result on a trivial search | | |
| `| tstats count` wall time | | |

The bundle replicates to every peer on change. A 400,000-row automatic lookup that
one search uses once a day is paid for by **every search on the system**, forever.
That is why `replicationBlacklist` exists, and why large reference data belongs in
a KV store collection or an indexed summary rather than a CSV lookup.

**Deliverable:** the configuration, the job-inspector evidence, and the two failure
observations. For the first, state explicitly what a scheduled detection would have
done during the outage — that sentence is the one worth having.
