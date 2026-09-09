# SPL-07 lab guide — Architecture & Deployment

**Module:** [SPL-07](../../docs/modules/splunk/spl-07-architect.md) · 7 labs,
4 📄 no licence required, 3 ⚠️ trial licence + multiple instances.

**Do Lab 1 first, before you start any trial clock.** The module says so and it is
the single most useful piece of scheduling advice in the series: Labs 2, 3 and 4
consume a trial window continuously, and Labs 1, 5, 6 and 7 are paper exercises
that feed them. Arriving at the cluster with no capacity model means building the
wrong cluster and finding out on day 12 of a 14-day trial.

Suggested order: **1 → 6 → 5 → 7** (paper), then **2 → 3 → 4** inside one trial
window.

---

## Lab 1 📄 — Size a Deployment

No licence. Arithmetic and defensibility.

**The scenario** (substitute your own; keep the shape):

| Input | Value |
|---|---|
| Daily ingest | 800 GB/day |
| Growth | 25%/year |
| Retention — security | 7 years (searchable 12 months, then archive) |
| Retention — operational | 90 days |
| Split | 35% security, 65% operational |
| Concurrent searches | 40 peak |
| Premium apps | ES, 8 accelerated data models |
| Availability | Survive one indexer loss with no data loss and no search interruption |

### Step 1 — Storage, and the multiplier nobody quotes

Raw ingest is not what you store. Work it through in stages, because the total is
meaningless without them:

Fix the two ratios first and use them everywhere, so the model is one calculation
rather than several that quietly disagree:

```
rawdata on disk  ≈ 0.15 × raw ingest     (the compressed source)
tsidx on disk    ≈ 0.35 × raw ingest     (the index)
                 → one bucket copy ≈ 0.50 × raw ingest
```

With RF=3 and SF=2 you keep three rawdata copies and two tsidx copies, so the
**storage multiple against raw ingest** is:

```
3 × 0.15  +  2 × 0.35  =  0.45 + 0.70  =  1.15 × raw ingest
```

Now apply it to the searchable window:

```
security     280 GB/day × 365 d  =  102 TB raw ingest
operational  520 GB/day ×  90 d  =   47 TB
                                 =  149 TB raw ingest, searchable

× 1.15 storage multiple          =  171 TB on disk
÷ 0.80 (never fill a volume)     ≈  214 TB provisioned
```

Frozen security data (years 2–7) goes to archive: not searchable, not in this
number, and it needs its own budget line rather than being quietly omitted.

**State every ratio as an assumption with a source.** The 0.15 compression figure
is data-dependent — JSON compresses far better than binary, and Windows event logs
better than either. If you have the source data, measure it:

```
| dbinspect index=*
| stats sum(rawSize) as raw, sum(sizeOnDiskMB) as disk by index
| eval ratio = round(disk*1024*1024/raw, 3)
```

A model that says "compression is 0.15 (industry rule of thumb)" is weaker than
one that says "compression is 0.11 (measured on 30 days of our own proxy data,
query above)", and the second is what survives a finance conversation.

### Step 2 — Indexers, from the binding constraint

Three constraints; the largest wins, and which one wins tells you what kind of
deployment you have:

```
Ingest:   800 GB/day ÷ 100 GB/day/indexer (conservative, with ES)  =  8
Search:   40 concurrent ÷ ~6 per indexer                           =  7
Storage:  214 TB ÷ 16 TB usable per indexer                        = 14   ← binds
```

The 16 TB is an assumption and needs stating like any other: direct-attached NVMe
on a 2U server, after RAID and filesystem overhead. Quote 24 TB instead and
storage stops binding at 9 indexers, which changes the recommendation entirely.
This is exactly the kind of number that must be visible rather than buried.

Storage binds — 14 indexers to hold the data, 8 to process it — so you are
building a **storage-bound cluster**, and the implication is immediate: six
indexers' worth of CPU is being bought to carry disk. That is precisely the case
SmartStore exists for. Carry the finding into Lab 6 rather than deciding storage
architecture separately.

### Step 3 — Growth

25%/year compounding against a 7-year obligation is the number that reframes the
project:

```
year 0   800 GB/day
year 1  1000
year 3  1563
year 5  2441
year 7  3815      ← 4.8× the original
```

You are not sizing for 800 GB/day. You are sizing for a system that must reach
3.8 TB/day without a redesign. That means the architecture question is *how does
this grow* — and the honest answer is that a 13-indexer cluster becomes a
60-indexer cluster, which is a different operational proposition, not a bigger
version of the same one.

### Step 4 — The one-pager for the finance approver

Different document, different audience, same numbers. Structure it as an answer to
the question they will actually ask:

> **"Why can't it be half the size?"**
>
> It can, and here is exactly what you get for it.
>
> - **Halving storage** (214 TB → 107 TB) means 6 months of searchable
>   security data instead of 12.
>   Investigations routinely reach back further than six months; the 2024 median
>   dwell time for the incidents in our own history was N days. Below that number,
>   we cannot investigate our own typical incident.
> - **Halving indexers** means searches queue at peak. The visible symptom is
>   analysts waiting; the invisible symptom is scheduled detections being
>   **skipped**, which looks identical to nothing having happened.
> - **What we could cut instead, and what it costs:** drop operational retention
>   from 90 to 45 days (saves 21 TB, ~12%, and costs us the ability to
>   investigate slow-burn operational issues); stop accelerating three data models
>   nobody queries (saves 8 TB and 2 indexers, costs nothing we can identify);
>   move warm and cold data to SmartStore (drops local storage from 171 TB to
>   around 21 TB plus 74 TB of object storage, and costs first-search latency on
>   old data — see Lab 6).

The third bullet is what makes the document credible. Arriving with one number and
no alternatives reads as a request; arriving with a costed menu reads as advice,
and gets a better outcome even when the answer is still no.

**Deliverable:** the model with every assumption traceable, the topology, the
one-pager. The module marks defensibility, not the number — a model whose
assumptions are visible and wrong beats one whose assumptions are hidden and right,
because only the first can be corrected.

---

## Lab 2 ⚠️ — Build an Index Cluster and a Search Head Cluster

**Trial licence and multiple instances.** [`compose.distributed.yml`](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/blob/main/labs/docker/compose.distributed.yml)
gives you a search head and two peers; extend it to a cluster manager, three peers,
a deployer and three search heads. Budget ~10 GB RAM.

**Set RF and SF deliberately**, and write down what you chose *before* you check
what happened:

```conf
# cluster manager — server.conf
[clustering]
mode = manager
replication_factor = 3
search_factor = 2
pass4SymmKey = <shared>
```

**Verify replication actually occurred** — the module is specific, because a
cluster in a valid-looking state can be one bucket away from unhappy:

```
| rest /services/cluster/manager/indexes
| table title, is_searchable, num_buckets, replicated_copies_tracker.*, searchable_copies_tracker.*
```

```
| dbinspect index=sec_high
| stats count by splunk_server, state
```

```bash
splunk show cluster-status --verbose
```

The three checks answer different questions and you need all three: the REST
endpoint says what the manager *believes*, `dbinspect` says what is *on the peers*,
and `cluster-status` says whether the manager thinks it is done fixing things.

**The storage multiple is the deliverable**, and it is the number that connects
this lab to Lab 1:

```
RF=3, SF=2
  rawdata copies:  3 × 0.15 = 0.45 × raw
  tsidx copies:    2 × 0.35 = 0.70 × raw
                 = 1.15 × raw ingest on disk
```

Against 800 GB/day that is 920 GB/day of disk for 800 GB of data. Say it in those
terms in your write-up. "RF=3/SF=2" is a configuration; "we store 1.15 bytes on
disk per byte ingested, and 2.3× that if we go to RF=3/SF=3" is an architecture
decision someone can price.

---

## Lab 3 ⚠️ — Structured Diagnosis of a Broken Deployment

**Marked on method. A lucky guess with no evidence trail scores zero.** The module
means it, and this is the lab closest to what the Architect exam assesses.

Run at least three faults across different tiers, **including one where the results
are wrong rather than slow**. Self-inject from this list:

| # | Fault | Tier | Symptom | Class |
|---|---|---|---|---|
| 1 | One peer's disk at 100% | Storage | Indexing stalls, queues back up | Slow |
| 2 | Bundle replication failing to one peer | Search | Searches return **fewer results**, no error | **Wrong** |
| 3 | A peer with a skewed clock | Ingest | Events land outside search windows | **Wrong** |
| 4 | `maxKBps` throttle left at default on a forwarder | Ingest | Growing ingest lag, no error | Slow |
| 5 | Search head captain flapping | Search | Intermittent scheduled-search skips | Slow + wrong |

**Faults 2 and 3 are the important ones.** A slow system announces itself; a wrong
system does not, and an architect who has only ever diagnosed slowness has not
practised the harder half.

### The method, in fixed order

Write the log as you go — a numbered list of what you looked at, what it said, and
what you concluded. Reconstructed afterwards it is fiction.

1. **Scope it.** One peer or all peers? One index or all? One user or all? Three
   cheap searches:
   ```
   | tstats count where index=* by splunk_server
   | rest /services/server/status/resource-usage/hostwide | table splunk_server, mem_used, cpu_system_pct
   | rest /services/cluster/manager/peers | table label, status, is_searchable, last_heartbeat
   ```
2. **Establish "wrong or slow".** They are different investigations and conflating
   them costs hours.
   ```
   | tstats count where index=* by splunk_server, index
   ```
   Unequal counts across peers on evenly distributed data is *wrong*, not slow.
3. **Walk the pipeline in data-flow order** — forwarder → queues → parsing →
   indexing → replication → bundle → search. Do not jump to the tier you suspect;
   the whole value of the method is that it finds the fault you did not suspect.
   ```
   index=_internal source=*metrics.log group=queue | timechart max(current_size_kb) by name
   index=_internal component=DistributedBundleReplicationManager log_level!=INFO
   ```
4. **Confirm by removing the cause**, not by observing that things improved.
   Systems improve on their own. Restore the fault and confirm the symptom
   returns — that is the difference between a diagnosis and a coincidence.

**For fault 3 specifically**, the diagnostic is worth knowing by heart because the
symptom is so misleading:

```
| tstats count where index=* by splunk_server, _time span=1h
| timechart span=1h sum(count) by splunk_server
```

A peer whose clock is skewed forward has all its events in the future. They index
fine, replicate fine, and are absent from every search over "last 24 hours". The
count is wrong, everything is green, and nothing logs an error.

---

## Lab 4 ⚠️ — Fail It

Cluster from Lab 2, searches running, then break things on purpose. Record four
columns for each: **what the user experienced, what the cluster did, how long
remediation took, what was lost.**

| Failure | User experience | Cluster behaviour | Remediation | Lost |
|---|---|---|---|---|
| Kill an indexer peer mid-search | | Manager marks peer down, fixes buckets to restore RF/SF | | |
| Kill the SH captain | | Election, ~30–60 s; in-flight ad-hoc searches die | | |
| Kill the cluster manager | | **Searches keep working.** No bucket fixing, no new peers | | |

**The cluster-manager result is the one people get wrong**, and it is worth
predicting before you run it. Losing the manager is not an outage: existing peers
keep indexing and searching. What you lose is the ability to *recover* — no bucket
fix-up, no rebalancing, no new peer joining. It is a latent failure, and the danger
is that nobody notices for a week, during which a second failure has no safety net.

**Then repeat with a different RF/SF** and compare. The comparison is the lab:

| RF/SF | Storage multiple | Survives | Search after 1 loss | Cost vs RF=2/SF=2 |
|---|---|---|---|---|
| 2/2 | 1.00× | 1 peer | Complete | baseline |
| 3/2 | 1.15× | 2 peers | Complete | +15% |
| 3/3 | 1.50× | 2 peers | Complete, faster | +50% |

**The recommendation must be tied to a stated tolerance, and the module marks down
maximum resilience regardless of requirement.** That is the right call and worth
defending explicitly: RF=3/SF=3 against a stated tolerance of "survive one peer"
spends 50% more storage — on a 310 TB deployment, roughly 100 TB — to buy a
resilience property nobody asked for. Someone else's project does not get funded
so that yours can be over-engineered. That is an architecture failure, not caution.

Write your recommendation as: *"RF=3/SF=2, costing 1.15× raw, because the stated
tolerance is one peer with no search interruption and this meets it with one
peer of margin. RF=3/SF=3 would add 35% storage (~100 TB, ~$X) for faster search
after a failure, which is not in the requirement."*

---

## Lab 5 📄 — Plan a Migration

No licence. Single-site to multi-site, with a data-residency constraint.

**The residency constraint is the interesting part** and in Australia it is
concrete: personal information may be subject to APP 8 cross-border disclosure
obligations, and some government and health data carries explicit onshore
requirements. So "multi-site" cannot mean "one site in Singapore" without a
specific analysis, and the analysis belongs in the plan rather than in an
assumption.

**Sequencing.** Each stage needs a validation gate and a rollback path, and the
rollback is what makes it a plan rather than a hope:

| Stage | Action | Validation gate | Rollback |
|---|---|---|---|
| 0 | Upgrade all instances to a common version | Version parity confirmed | Standard downgrade path |
| 1 | Stand up site 2 peers, **not** in the cluster | Peers healthy standalone | Delete them; nothing changed |
| 2 | Enable multi-site on the manager, site 1 only | `cluster-status` clean, RF/SF met | Revert `server.conf`, restart manager |
| 3 | Join site-2 peers | Buckets replicating cross-site; measure the link | Remove peers, manager re-fixes to site 1 |
| 4 | Set `site_replication_factor` / `site_search_factor` | Per-site counts met | Revert factors; excess copies age out |
| 5 | Move search heads to site awareness | Searches distribute per `site_affinity` | Revert `server.conf` per SH |
| 6 | Decommission any site-1 excess | — | **None** |

**The point of no return is stage 4**, and it is worth being precise about why.
Once site-specific replication factors are set and buckets have been fixed to
satisfy them, reverting does not un-copy data — it leaves excess copies that age
out over the retention period. More importantly, from stage 4 the cluster's
*correctness* depends on cross-site links: a WAN failure now means the manager
cannot satisfy site RF and begins remediation it cannot complete.

**What mitigates it:**

- Measure the inter-site link **before** stage 3, not after. Bucket replication is
  bulk transfer and a link adequate for search is not necessarily adequate for it.
- Enter stage 4 with a full, verified, restorable backup of the manager's
  configuration — the cluster state is reconstructible, the manager's config is
  the part that is not.
- Do stages 3 and 4 in a maintenance window with `maintenance-mode` enabled, so
  the manager does not start bucket fix-up on transient peer flaps and turn a
  five-minute blip into an hour of replication traffic.

**Deliverable:** the plan, the point of no return, the mitigations. A plan whose
rollback column says "restore from backup" at every stage has not been thought
about — restoring from backup is what you do when the plan failed, not the plan.

---

## Lab 6 📄 — Storage Architecture and the SmartStore Trade-off

No licence. Take the Lab 1 model — 149 TB of searchable raw ingest, 171 TB on
disk, storage-bound at 14 indexers — and re-cost it three ways.

### The three models

**A. All local, conventional tiering.** Hot/warm on NVMe, cold on cheaper spinning
or network storage, frozen to archive.

```
hot/warm (30 d)    24 TB raw × 1.15 =  28 TB   NVMe       × $A/TB
cold (remainder)  125 TB raw × 1.15 = 144 TB   HDD / NAS  × $B/TB
                                    = 171 TB
frozen                                         archive, cheap, not searchable
```

Note where the volume sits: **84% of your expensive storage is cold data**, which
is by definition the data nobody searches often. That one ratio is the argument
for the next two models.

**B. SmartStore + object storage.** Warm and cold live in object storage; each
indexer keeps a local cache.

```
hot, local, RF/SF    7 d × 800 GB = 5.6 TB raw × 1.15 =   6 TB NVMe
cache (~20% of searchable, at 0.50 × raw)            =  15 TB NVMe
                                         local total ≈  21 TB
object storage, one copy (0.50 × 149 TB)             =  74 TB
```

The material change is that **replication factor no longer multiplies your bulk
storage** — the object store provides durability its own way. Local storage falls
from 171 TB to about 21 TB, and 144 TB of replicated cold data becomes 74 TB of
object storage at a fraction of the per-terabyte price.

It also unbinds the indexer count. At 21 TB local you are no longer
storage-bound, so the cluster sizes on ingest and search instead: **8 indexers,
not 14**. The saving is six servers as well as the disk, and that is the number
to put in front of a finance approver.

**C. Hybrid.** SmartStore for operational data (90-day retention, rarely searched
after a fortnight), local for security data (searched constantly across a year).

### Search-latency assessment

| | Cache hit | Cache miss |
|---|---|---|
| Local | n/a | n/a — all local, uniform latency |
| SmartStore | Comparable to local | **Bucket must download first** |

**State which workloads are worse under SmartStore**, since the module requires it
and it is the honest part of the analysis:

- **Long-range rare-term searches.** A search for one string across 12 months
  touches nearly every bucket and hits cache misses on almost all of them. This is
  exactly the "did this indicator ever appear?" threat-hunting query — one of the
  most valuable searches a SOC runs, and the worst case for SmartStore.
- **Wide scheduled searches on old data**, where the download is paid on every run.
- **The first search after a cache eviction**, which is unpredictable and
  therefore hard to explain to the person waiting.

And which are unaffected or better:

- Dashboard and detection searches over recent data — the cache is warm.
- Anything accelerated: `tstats` against a summary reads the summary, not the
  buckets.
- Rebuilds and peer replacement, which become dramatically faster because a new
  peer fetches from object storage rather than from its neighbours.

**Recommendation tied to a workload profile.** For the Lab 1 scenario — storage
bound, 65% operational data that is rarely searched after two weeks, 35% security
data searched constantly across a year — **C, the hybrid**, and the reasoning is
that it puts SmartStore exactly where its weakness does not apply. Say that; a
recommendation that does not name the weakness it is avoiding has not made an
argument.

---

## Lab 7 📄 — Design the Detection Capability, Not Just the Platform

No licence. This is the Cybersecurity Defense Architect deliverable and the
capstone of the paper labs.

**Work backwards from detection requirements**, never forwards from data sources.
Forwards gives you a platform that ingests what was easy to ingest.

| Requirement | Technique | Telemetry needed | Have it? | Where detection runs |
|---|---|---|---|---|
| Detect credential access via Kerberoasting | T1558.003 | Windows 4769 with ticket encryption type | **No** | ES detection over Authentication DM |
| Detect C2 over DNS | T1071.004 | Full DNS query logs, all resolvers | Partial | ES, accelerated Network_Resolution |
| Detect lateral movement via remote services | T1021.002 | 4624 Type 3 **and** process creation on target | Yes | ES over Authentication + Endpoint |
| Detect exfiltration to cloud storage | T1567.002 | Proxy with full URL and byte counts | Yes | ES over Web |
| Detect defence evasion via log clearing | T1070.001 | Windows 1102, forwarded before clearing | **No** | ES, but see gap |

**The architecture-level gap statement is the deliverable**, and it is
architectural precisely because no amount of detection content closes any of it:

| Gap | Why no content can fix it | Cost to close |
|---|---|---|
| 4769 not collected | The event is not being forwarded | Audit-policy change on all DCs + ~40 GB/day + storage |
| DNS only from corporate resolvers | Endpoints using DoH bypass them entirely | Endpoint DNS telemetry (Sysmon 22) or DoH blocking at egress — **a policy decision, not a Splunk one** |
| 1102 arrives after clearing | Local forwarding is inherently racy | Real-time forwarding with `_TCP_ROUTING`, or accept the gap and detect the *absence* of logs instead |

**The third row is the most instructive** and worth working through in the design:
you cannot reliably detect log clearing from the logs that were cleared. The
architectural answer is not a better detection — it is
[SPL-06 Lab 5](spl-06.md)'s continuity monitoring. Detecting the *silence* is a
different capability, sits in a different part of the architecture, and has to be
designed in rather than added later.

**Also design the content pipeline**, because "where detection executes" is only
half of it. How does content reach production? That is
[SPL-04 Lab 6](spl-04.md)'s version control and promotion path, drawn on the
architecture diagram as a real path with real gates — dev search head, test
fixtures, promotion, production — rather than left as an implied manual step.

An architecture that shows where detections *run* but not how they *arrive* has
designed a system nobody can safely change, which is a system that stops being
changed.
