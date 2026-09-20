# SPL-03 lab guide — SOC Analysis & Threat Detection

**Module:** [SPL-03](../../docs/modules/splunk/spl-03-cyber-defense-analyst.md) ·
8 labs, 5 ✅ on Free, 1 📄 no platform, 1 ⚠️ trial, 1 🔒 Enterprise Security.

This is the first guide where the dataset's *ground truth* matters. Three labs
have an objectively checkable answer:

```bash
python3 harness/verify.py answer spl03.lab2.spray_victim <username>
python3 harness/verify.py answer spl03.lab5.travel_user  <username>
python3 harness/verify.py answer spl03.lab7.beacon_host  <hostname>
```

The harness compares a hash, so it tells you *whether* you are right, not *who*
the answer is. Getting the right name from the wrong search still fails the
module's marking criteria — the deliverable is the reasoning.

---

## Lab 1 🔒 — Triage a Notable Queue

**Blocker, stated plainly:** Incident Review is an Enterprise Security view.
There is no Free-licence substitute, no community app that reproduces it, and
nothing in this repository fakes one. If you do not have ES, you cannot run this
lab as specified.

What you *can* do without ES is the analytical half, which is where the marks
are anyway. `index=risk` is a queue of intermediate findings with the same shape
ES would give you:

```
index=risk
| stats sum(risk_score) as total, dc(search_name) as detections,
        values(search_name) as fired, min(_time) as first, max(_time) as last
        by entity, entity_type
| where total > 100
| sort - total
```

Triage the top 20 entities as if they were notables: for each, record an
assignment, a disposition, and the reasoning. Then enrich with business context,
because a score without context is not a priority:

```
... | lookup oscd_identities.csv identity as entity OUTPUT priority, bunit, category, watchlist
```

**The reflection the module asks for.** Work out which of your dispositions were
false positives, then say what change to the detection would have prevented each.
You can check yourself — the truth file is keyed by entity:

```bash
python3 - <<'PY'
import csv, collections
rows = list(csv.DictReader(open('data/truth/risk_truth.csv')))
mal = collections.Counter(r['entity'] for r in rows if r['scenario'] != 'benign')
print(f"{len(mal)} of {len({r['entity'] for r in rows})} entities have a malicious contribution")
for entity, n in mal.most_common(20):
    print(f"  {entity:22} {n:3} malicious findings")
PY
```

!!! warning "Instructor-only"
    Do not read `data/truth/` before you have written your dispositions. Once you
    have, comparing them is the most useful thing in this lab.

**With an ES trial:** the same exercise on the real Incident Review, which adds
what the substitute cannot — ownership, status transitions, adaptive response
actions and the audit trail of who decided what. Note in your write-up which
parts of triage were *process* rather than *analysis*; that distinction is what
SPL-04 builds on.

---

## Lab 2 ✅ — Author and Tune a Correlation Search

The dataset contains one password spray: a single external source attempting a
small number of passwords against many accounts, then one success.

**Version 1 — the obvious search.** Per-account failure counting, which is what
most estates ship with:

```
index=wineventlog EventCode=4625
| bin _time span=1h
| stats count as failures by user, _time
| where failures > 5
```

Run it. It returns **nothing at all** — not one row, against a dataset that
contains a live password spray with 45 victims and a successful compromise.

That is the point, and it is worth sitting with: the search is not broken, it is
counting the wrong thing. A spray is *designed* to stay under a per-account
threshold, so one to three attempts per account is invisible to a rule that
aggregates by account. The detection's failure is in its **aggregation key**, not
its threshold, and no amount of tuning the number 5 will fix it.

**Version 2 — pivot the aggregation.** Count distinct accounts per source:

```
index=wineventlog EventCode=4625
| bin _time span=1h
| stats dc(user) as accounts, count as attempts, values(user) as targets by src, _time
| eval attempts_per_account = round(attempts/accounts, 2)
| where accounts >= 15 AND attempts_per_account < 4
| sort - accounts
```

One source separates cleanly: the noisiest benign source touches **4** accounts,
the sprayer touches **45**. An order of magnitude of separation on the right key,
where the wrong key gave nothing whatsoever. Now find what it got:

```
index=wineventlog EventCode=4624 src=<the sprayer IP>
| table _time, user, dest, Logon_Type
```

```bash
python3 harness/verify.py answer spl03.lab2.spray_victim <username>
```

**Measuring the rates the module asks for.** Both versions need numbers, not
adjectives:

| | Version 1 | Version 2 |
|---|---|---|
| Findings | | |
| True positives | | |
| PPV | | |
| Spray detected? | | |

**The trade you must state.** Version 2's `accounts >= 15` is a real sensitivity
loss: a spray against ten accounts now passes cleanly. Say so explicitly, and say
what you would need — a baseline of normal distinct-accounts-per-source, so the
threshold is relative rather than absolute — to avoid the trade. Naming the
detection you gave up is worth more marks than the one you built.

---

## Lab 3 ✅ — Design a Risk-Based Alerting Scheme

`index=risk` is a **deliberately uncalibrated** risk index. Somebody picked the
ten scores by feel, exactly as happens in a real deployment:

```
index=risk | stats count, avg(risk_score) as avg_score by search_name | sort - count
```

**Step 1 — pick your threshold.** Aggregate to entity-days and look at the
distribution before choosing a number:

```
index=risk
| bin _time span=1d
| stats sum(risk_score) as risk, dc(search_name) as breadth,
        values(search_name) as contributors by entity, entity_type, _time
| eventstats perc90(risk) as p90, perc99(risk) as p99
| where risk > p99
```

**Step 2 — apply decay, because risk is not cumulative forever.** The lab app
ships the macro:

```
index=risk | `oscd_decay(7)` | stats sum(decayed_score) as risk by entity
```

Compare against the undecayed total. Entities whose ranking changes are the
interesting ones: they are the ones whose risk is old.

!!! danger "`ln()` is not `log()`"
    The macro uses `ln(2)`. In SPL, `log(x)` defaults to **base 10**. Using
    `log(2)` gives a half-life about 3.3× longer than you intended, silently, with
    no error. This is the single most common arithmetic defect in hand-rolled RBA
    and it is worth confirming in your own copy.

**Step 3 — measure.** How many risk incidents fired, and how many were worth
investigating? The truth labels give you a real PPV:

```bash
python3 - <<'PY'
import csv, collections
rows = list(csv.DictReader(open('data/truth/risk_truth.csv')))
total, malicious = collections.defaultdict(float), collections.defaultdict(bool)
for r in rows:
    total[r['entity']] += float(r['risk_score'])
    if r['scenario'] != 'benign':
        malicious[r['entity']] = True
for threshold in (100, 150, 200, 300):          # substitute your own
    fired = [e for e, v in total.items() if v > threshold]
    tp = [e for e in fired if malicious[e]]
    print(f"threshold={threshold:4}  fired={len(fired):4}  "
          f"true positive={len(tp):3}  PPV={len(tp)/max(1, len(fired)):.1%}")
PY
```

Run it across several thresholds before you commit to one, and look at the shape:

```
threshold= 100  fired=  92  true positive=  9  PPV= 9.8%
threshold= 150  fired=  35  true positive=  4  PPV=11.4%
threshold= 200  fired=  22  true positive=  4  PPV=18.2%
threshold= 300  fired=   6  true positive=  2  PPV=33.3%
```

Precision rises with the threshold, as you would hope. **Now read the other two
columns, which is where the decision actually lives.** Going from 100 to 300
improves precision by a factor of 3.4 and discards **7 of 9** true positives. You
are not choosing a precision; you are choosing how many real incidents to miss in
exchange for a queue somebody can work.

There is no correct answer to that, and this is the honest reason risk thresholds
are hard: the arithmetic gives you the trade curve, and someone accountable has to
pick a point on it. What the arithmetic *can* tell you is that the curve here is
poor — 33% precision at the cost of two-thirds of your recall is not a good place
to be operating, and no cut-point on this ranking is. When the whole curve is bad,
the fix is the scores, not the threshold. That is what
[SPL-09](../../docs/modules/splunk/spl-09-detection-analytics.md) Lab 4 fits
properly, and why the calibration note below matters more than the number you pick.

**Step 4 — test the received wisdom instead of repeating it.** Every RBA talk you
will ever see asserts that **breadth beats depth**: three different detections on
one entity is a stronger signal than one detection firing three times. It is a
reasonable prior. Test it, because you have labels:

```bash
python3 - <<'PY'
import csv, collections
rows = list(csv.DictReader(open('data/truth/risk_truth.csv')))
total = collections.defaultdict(float)
breadth = collections.defaultdict(set)
malicious = collections.defaultdict(bool)
for r in rows:
    total[r['entity']] += float(r['risk_score'])
    breadth[r['entity']].add(r['search_name'])
    if r['scenario'] != 'benign':
        malicious[r['entity']] = True

by_score = [e for e, _ in sorted(total.items(), key=lambda kv: -kv[1])]
by_breadth = [e for e, _ in sorted(breadth.items(),
                                   key=lambda kv: (-len(kv[1]), -total[kv[0]]))]
for k in (10, 20, 50):
    p_s = sum(malicious[e] for e in by_score[:k]) / k
    p_b = sum(malicious[e] for e in by_breadth[:k]) / k
    print(f"P@{k:<3} by total score {p_s:5.0%}   by breadth {p_b:5.0%}")
PY
```

**In this dataset the prior is wrong where it matters.** Total score wins at the
top of the queue — 20% against 10% at the top ten, 15% against 10% at twenty — and
only draws level deeper down, where nobody is looking. Work out why before reading
on.

The reason is that the malicious entities here are mostly spray victims, and a
spray trips *one* detection many times. Ranking by breadth actively demotes them.
Breadth wins when an intrusion chain trips structurally different detections on
the same entity — which happens for the C2 host and the insider, and for almost
nobody else. Two or three such entities cannot outweigh twenty-four spray victims
at the top of a precision-at-k measurement.

The transferable lesson is not "breadth is bad". It is that **a scoring heuristic
is a claim about your population, not a law**, and you have the labels to check
which claim holds in yours. A SOC that adopted breadth-ranking here on the
strength of a conference talk would have made its own queue worse.

**The calibration note.** Full marks require defending a score you got wrong. The
easiest one to get wrong here is *Excessive Failed Authentications* at 20. The
spray generates **25 findings across 21 distinct victims**, all of them accounts
that merely *received* attempts and were never compromised. A purely additive
scheme therefore floods the top of the queue with victims and buries the one
account that actually fell over.

State what you would do about it, and be specific: cap each detection's
contribution per entity per window, attribute the risk to the **source** rather
than to each victim, or treat repeat firings of one detection as evidence of a
single event rather than many. Do not quietly fix it and present the scheme as
though it was right the first time — the module marks the reasoning, and a
defended mistake scores above an undisclosed correction.

---

## Lab 4 📄 — Coverage Assessment

No Splunk instance needed; this is analysis. Your detection estate is the ten
detections in `index=risk`, and your telemetry is the eight indexes.

Pick one ATT&CK tactic — **Lateral Movement (TA0008)** and **Credential Access
(TA0006)** both have real substance in this dataset. For each technique, classify:

| Class | Meaning | Route to |
|---|---|---|
| **Covered** | Telemetry exists and a detection consumes it | — |
| **Detection gap** | Telemetry exists, nothing looks at it | Detection engineering |
| **Telemetry gap** | The data is not being collected at all | Data engineering |

The distinction is the whole lab. The dataset is built so you cannot fudge it:

- `sysmon` carries **EventCode 1 only**. Every technique that needs image loads
  (7), registry (12–14), pipes (17–18) or WMI subscriptions (19–21) is a
  **telemetry gap**, not a detection gap, and no amount of detection-engineering
  effort will close it.
- Kerberos service-ticket events (4769) are absent entirely, so Kerberoasting
  (T1558.003) is a telemetry gap — even though `wineventlog` exists and looks like
  it ought to cover credential access.
- Remote execution via WMI **is** present in `sysmon`, and *is* consumed by a
  detection. Covered.
- Lateral authentication (Logon Type 3 to servers) is present and only partly
  consumed. Detection gap.

Confirm each claim rather than trusting the list:

```
index=sysmon | stats count by EventCode
index=wineventlog | stats count by EventCode
```

**Deliverable:** the map plus a prioritised remediation plan. The plan is marked
on routing, not on volume — a plan that sends telemetry gaps to the detection
team is wrong regardless of how good the detections it proposes are.

---

## Lab 5 ✅ — Adopt and Adapt Detection Content

Take a public detection and get it working here. Two honest routes:

**Route A — convert a Sigma rule by hand.** Impossible travel, since the dataset
has exactly one. Start naive:

```
index=cloud action=success
| sort 0 user, _time
| streamstats current=f last(src_lat) as plat, last(src_long) as plong,
              last(_time) as ptime, last(src_city) as pcity,
              last(src_country) as pcountry by user
| where isnotnull(plat)
| eval dlat=(src_lat-plat)*111.32,
       dlong=(src_long-plong)*111.32*cos(src_lat*pi()/180),
       km=sqrt(pow(dlat,2)+pow(dlong,2)),
       hours=(_time-ptime)/3600,
       kmh=km/hours
| where km > 500 AND kmh > 900
| table _time, user, pcity, src_city, pcountry, src_country, km, hours, kmh
```

The `dlong` term scales longitude by `cos(latitude)` — an equirectangular
approximation, which is accurate to well under a percent over Australia and far
cheaper than haversine. At continental scale that error is irrelevant next to the
threshold you are about to pick arbitrarily; do not let precision here distract
you from the fact that `900 km/h` is a guess.

That returns roughly **120 pairs across 74 users**. **This is correct behaviour,
not a bug.** People genuinely travel interstate, and the detection has no way to
know that. Your job is the diagnosis the module asks for: is the failure *logic*,
*normalisation*, or *missing telemetry*?

It is none of the three — it is **base rate**. The rule is logically sound and the
data is fine; the population of legitimate travellers simply dwarfs the one
attacker. That is the honest answer and it is the one that connects to
[SPL-09](../../docs/modules/splunk/spl-09-detection-analytics.md) Part B.

Now narrow it, one condition at a time, and **write down the count after each**.
The shape of that funnel is the deliverable, not the final row.

**Filter 1 — drop service accounts.**

```
... | where km > 500 AND kmh > 900
| lookup oscd_identities.csv identity as user OUTPUT category, priority, work_city
| search category!="service_account"
```

122 pairs → 102; 74 users → 68. Service accounts sign in constantly, so even a
small genuine-travel rate produces many pairs from very few accounts. Cheap win,
real cost: **a compromised service account is now invisible to this detection**.
Say so, and say where you would cover it instead.

**Filter 2 — require an offshore leg.**

```
| where src_country!="AU" OR pcountry!="AU"
```

Note that **both** legs matter — an adversary signing in from offshore and then
the victim signing in normally from Sydney is the same pair seen from the other
end. Filtering only on `src_country` silently drops half of them.

Down to **34 users**, and this is where the naive analyst declares victory and is
wrong. Thirty-four is still an unworkable queue, the organisation has legitimate
NZ and Singapore activity, and in a company with offshore staff this filter buys
nothing at all. It is also the least transferable thing you could build: a
country list encodes today's org chart, not adversary behaviour.

**Filter 3 — pivot on authentication strength, not geography.**

```
| join type=left user
    [ search index=cloud (authentication_method=legacy OR mfa_result!=satisfied)
      | stats count as weak_auth, values(app) as weak_apps by user ]
| where weak_auth > 0
```

**One user.**

```bash
python3 harness/verify.py answer spl03.lab5.travel_user <username>
```

The reason this filter is the good one is not that it is more selective. It is
that it targets something the adversary *needs*: legacy protocols such as IMAP4
bypass modern authentication and therefore bypass MFA, which is exactly why they
get used. Geography is incidental to the attack; MFA bypass is instrumental to it.

Rank your three filters by how much of the adversary's freedom each removes, and
you will find the ordering is the reverse of how selective they look at first
glance. That ordering is the point of the lab.

**Route B — adopt from Splunk Security Content.** Pull a detection from the
[security_content](https://github.com/splunk/security_content) repository and try
to run it. Most will fail immediately because they are written against accelerated
CIM data models this lab does not build. Diagnose that correctly: it is neither a
logic error nor missing telemetry, it is a **normalisation** dependency, and the
fix is either accelerating the model (SPL-02 Lab 3, trial licence) or rewriting
`tstats` against raw indexes and accepting the performance cost.

**Deliverable:** the working detection, or a documented reason it cannot work
here. A documented failure with the right diagnosis scores full marks.

---

## Lab 6 ✅ — A PEAK Hunt, Productised

Prepare, Execute, Act with Knowledge. The dataset supports several hypotheses;
pick one you have *not* already been handed a detection for.

**Suggested hypothesis (genuinely un-detected in this dataset):** *An adversary is
using a compromised account to authenticate across hosts it has no business
relationship with.* Lateral movement is present in the data, and the risk index
consumes it only through generic remote-execution firing.

Prepare — define the abstraction. "No business relationship" needs an operational
definition. Use the department fields in both lookups:

```
index=wineventlog EventCode=4624 Logon_Type=3
| lookup oscd_identities.csv identity as user OUTPUT bunit as user_dept, category
| lookup oscd_assets.csv host as dest OUTPUT bunit as host_dept, role, category as asset_class
| where user_dept != host_dept AND category != "service_account"
| stats dc(dest) as hosts, values(role) as roles, values(dest) as targets by user
| where hosts >= 3
| sort - hosts
```

Execute — refine until the output is small enough to read. Add the time dimension,
because a chain in one hour is different from the same hosts over two weeks:

```
... | transaction user maxpause=30m | where eventcount >= 3
```

!!! important "Your threshold decides what you find — check it deliberately"
    `hosts >= 3` returns **two users**, and they are not the same kind of thing:
    one reached 11 cross-department hosts steadily over the whole window, the
    other reached 3 inside an hour. Raise it to `hosts >= 5` and you keep only the
    first and lose the intrusion entirely.

    That is the lab. A count threshold cannot distinguish *breadth* from *speed*,
    and the two behaviours it conflates are a data-collecting insider and an
    adversary moving laterally. Add the time dimension and they separate
    immediately — which is what the `transaction` above is for, and why running it
    is not optional.

    Then say in your hunt record what the abstraction could not see, and what you
    would measure instead: host *role* transitions (workstation → jump host →
    server → domain controller) rather than department count. Role crossing is
    what actually characterises lateral movement, and unlike department it does
    not depend on how the org chart happens to be drawn this quarter.

Act — whatever the outcome, produce a durable artefact. **A hunt with no artefact
fails this lab.** Acceptable outputs:

1. A saved search (⚠️ scheduling needs a trial licence; the search definition
   alone is acceptable on Free).
2. A risk contribution — write your own findings into `index=risk` shape and show
   they rank the right entity.
3. A documented negative result **with the search that would find it next time**,
   plus what telemetry you would need. This is a full-marks outcome; a negative
   result is only a failure if it is undocumented.

**Knowledge** is the part everyone skips. Write down the abstraction you built
("cross-department Type 3 authentication") separately from the search, because the
abstraction survives a SIEM migration and the SPL does not.

---

## Lab 7 ✅ — Investigate End to End, and Write It Up

There are **two independent things** to investigate in this dataset, and finding
out that they are independent is part of the lab. Work both.

- **Thread A — a C2 channel**, visible in DNS and proxy, with no user attached.
- **Thread B — a compromised account**, visible in authentication and endpoint
  telemetry, running from initial access through to lateral movement.

Do Thread A first: it is where the answer key is, and it is the harder analysis.
Then do Thread B, which is where the timeline and the Diamond Model actually earn
their keep.

---

### Thread A — the C2 channel

**Start with the cheap signal, and watch it fail to finish the job.** Failed
lookups are one command:

```
index=dns reply_code=NXDomain
| stats count as failures by src_host
| sort - failures
```

That narrows 260 hosts to about 250 with at least one failure — which is to say,
it narrows nothing. Real estates fail DNS lookups constantly: typos, decommissioned
internal names, search-domain suffixing. Roughly 11% of lookups here fail and that
is normal.

Rate, not count, is the improvement:

```
index=dns
| stats count as lookups, count(eval(reply_code=="NXDomain")) as failures by src_host
| where lookups >= 20
| eval failure_rate = round(failures/lookups*100, 1)
| sort - failure_rate
```

One host sits near **53%** against a field where the next-worst is around 23%.
That is a strong lead, and still only a lead —
and nothing yet says the failures are hostile rather than a broken agent. Note how
much weaker this signal is than the neat story usually told about NXDOMAIN and C2.

**Now characterise the domains.** SPL has no entropy function, so compute it:

```
index=dns
| eval label=mvindex(split(query,"."),0), n=len(label)
| where n >= 12
| eval c=split(label,"")
| mvexpand c
| stats count as k by label, src_host, c
| eventstats sum(k) as total by label, src_host
| eval p=k/total, term=-p*log(p,2)
| stats sum(term) as entropy, first(total) as len by label, src_host
| where entropy > 3.2
| stats count as high_entropy_lookups, dc(label) as distinct_domains by src_host
| sort - high_entropy_lookups
```

The same host returns, now for a different reason: its failing lookups are
*algorithmically generated*, and the benign failures elsewhere in the estate are
not. Two independent lines of evidence converging on one host is worth more than
either alone, and saying so is part of the write-up.

```bash
python3 harness/verify.py answer spl03.lab7.beacon_host <hostname>
```

**Confirm regularity — and isolate the channel first.**

```
index=proxy src_host=<host>
| search dest IN (<the high-entropy domains>)
| sort 0 _time
| delta _time as gap
| where gap > 0
| stats count, avg(gap) as mean_gap, stdev(gap) as sd by src_host
| eval cv = sd/mean_gap
```

You should get a CV around **0.05** — very regular. Now run the same without the
`search dest IN (...)` line and you will get a CV near **3.0**, which looks like
nothing at all.

!!! important "This is the lesson, not a defect"
    The compromised host also browses normally. Beaconing is regular *within its
    own channel*; mixed with human traffic the regularity vanishes into the
    variance. Isolate the candidate channel, **then** measure. A learner who
    computes CV over all of a host's traffic will conclude the technique does not
    work.

**Pivot to everything else that host did:**

```
(index=dns src_host=<host>) OR (index=proxy src_host=<host>)
  OR (index=sysmon dest=<host>) OR (index=wineventlog dest=<host>)
| eval detail=coalesce(query, url, process, user)
| table _time, index, sourcetype, user, detail
| sort _time
```

This is where Thread A stops. There is no user, no process ancestry and no
authentication activity tying the beacon to anything else — you have a machine
talking to infrastructure it should not, and that is the whole finding. Say so at
the confidence it deserves rather than inflating it.

**Apply ACH properly.** The module fails an investigation that never considered a
benign explanation, and it is right to. Enumerate at least two:

| Hypothesis | Evidence for | Evidence against | Discriminator |
|---|---|---|---|
| H1: C2 beacon | High-entropy domains, CV ≈ 0.05 on the isolated channel, 54% NXDOMAIN | Small transfer volumes; no second-stage payload observed | Random labels *and* regular timing together |
| H2: Software telemetry / CDN | Regular timing is normal for update checks | Domains are algorithmically generated, not vendor-owned | Domain *structure*, not failure rate — a broken updater also fails lookups |
| H3: Misconfigured or broken client | Explains the 54% failure rate completely | Does not explain regular timing on the lookups that *do* resolve, nor the random labels | Regularity **and** label structure together — neither alone rules this out |

The discriminator column is what ACH is *for*, and H3 is why it is in the table.
A high NXDOMAIN rate feels like damning evidence, but it is equally consistent with
a broken client — so on its own it has **no diagnostic value**, however compelling
it looks. Only the conjunction of random labels and regular timing separates H1
from H3. Listing non-diagnostic evidence as support for your preferred hypothesis
is the classic ACH failure and the module marks it down.

---

### Thread B — the compromised account

This is the multi-stage intrusion, and it runs across three telemetry types in
under three hours. Start from the successful spray authentication you found in
Lab 2 and follow the account, not the host:

```
(index=wineventlog user=<spray victim>) OR (index=sysmon user=<spray victim>)
  OR (index=proxy user=<spray victim>)
| eval detail=coalesce(process, url, dest)
| table _time, index, sourcetype, EventCode, Logon_Type, dest, parent_process_name, detail
| sort _time
```

Narrow to the window around the compromise and the shape appears:

| Time (UTC) | Source | What |
|---|---|---|
| 02:11 | `wineventlog` | Failed authentications from an external address, one of 45 accounts targeted |
| 02:30 | `wineventlog` | **Successful** authentication from that same address |
| 03:00 | `sysmon` | `certutil.exe` spawned by `powershell.exe`, fetching a remote file |
| 03:00 | `sysmon` | `rundll32.exe` spawned by **`certutil.exe`** |
| 04:11 → 04:49 | `wineventlog` + `sysmon` | Type 3 authentications to four servers in 38 minutes, each followed by `wmic.exe` under `services.exe` |

**Read the timing.** Initial access to four servers in about two and a half
hours, from a password guessed over the internet. Nothing in that sequence
required a novel technique, and no single event in it is remarkable enough to
alert on by itself — which is the entire argument for correlating across
telemetry types rather than tuning any one detection harder.

**Two things here are worth more than the timeline itself.**

First, the `certutil.exe` → `rundll32.exe` parent-child edge. Neither binary is
malicious, both are signed by Microsoft, and both appear in benign traffic in this
dataset. The *edge* is what is anomalous. Confirm that yourself rather than taking
it on trust:

```
index=sysmon
| stats count by parent_process_name, process_name
| sort count
```

The numbers make the argument for you: `certutil.exe` runs **45 times** in this
dataset and `rundll32.exe` **44 times**, both almost always under `cmd.exe`. The
pair `certutil.exe → rundll32.exe` occurs **once**. Frequency-based detection on
either binary alone gives you 100-odd events and no signal; frequency on the
*edge* gives you one event and the answer.

The same holds for the lateral movement: `wmic.exe` under `cmd.exe` occurs 39
times and is unremarkable, while `wmic.exe` under **`services.exe`** occurs 4
times and is the entire intrusion.

Rare-pair analysis over that table is the durable technique; the specific pairs
are disposable, because tomorrow it will be a different LOLBin. What survives is
the shape of the query — score the edge, not the node.

Second, the lateral movement crosses from a **workstation** into four servers —
a boundary that ordinarily is not crossed by this user's account at all. Verify with the asset lookup:

```
index=wineventlog EventCode=4624 Logon_Type=3 user=<spray victim>
| lookup oscd_assets.csv host as dest OUTPUT role, bunit, priority, category as asset_class
| stats values(role) as roles, values(dest) as hosts, dc(dest) as n by user
```

**Diamond Model.** You now have all four vertices — adversary (unattributed, one
external source address), capability (spray, then certutil staging, then WMI
remote execution), infrastructure (the spraying address and the staging URL), and
victim (the account, its workstation, then four servers). Pivot on infrastructure:
does the spraying address appear anywhere else? Does the staging host?

**ACH for Thread B**, and it needs a benign hypothesis just as much as Thread A:

| Hypothesis | Evidence for | Evidence against | Discriminator |
|---|---|---|---|
| H1: Account compromise via spray | Success from the spraying address; unusual process ancestry follows within 30 min | — | Temporal ordering: the anomalous behaviour *begins* after the external success and not before |
| H2: Legitimate admin work by the account owner | Type 3 auth to servers is normal for some staff | The account is a finance user; the authentication came from an external address; `certutil` fetching a remote file is not administration | Source address of the successful logon — an admin does not administer from a public IP that just failed 45 other accounts |

**Now the part most write-ups get wrong.** Thread A and Thread B are **not the
same incident**. Different hosts, different users, no shared infrastructure, no
temporal relationship. Check that rather than assuming it in either direction:

```
(index=dns OR index=proxy OR index=wineventlog OR index=sysmon)
  (src_host=<beacon host> OR dest=<beacon host> OR user=<spray victim>)
| stats dc(user) as users, values(user) as who by src_host
```

Binding unrelated anomalies into a single narrative is the most common failure in
real incident write-ups, and it is much easier to do than to undo: once a report
says "the intrusion", every subsequent reader inherits the assumption. Two
findings at appropriate confidence beat one confident and wrong story.

---

**Deliverable:** for each thread — a timeline with sources, the searches, the
competing hypotheses with their discriminators, and a finding at an explicit
confidence level. Plus one handover note a colleague could act on cold, which
states that there are two separate findings and says which one to work first.

Write the handover before you stop. It is the part that will be marked hardest
and the part you will be worst at.

---

## Lab 8 ⚠️ — Assess Your Data Sources with Security Essentials

**Splunk Security Essentials is free**, but it leans on scheduled searches and
accelerated data models, which the Free licence does not have. Install it inside
a trial window.

```bash
docker compose -f compose.single.yml down
# add SPLUNK_LICENSE_URI / start a trial, then:
docker compose -f compose.single.yml up -d
```

Install SSE from Splunkbase into `splunk-apps/`, restart, and run its Data
Inventory against the six lab indexes.

**Do the inventory manually first**, before SSE tells you the answer. It takes one
search and it is the only way to know whether you agree with the tool:

```
| tstats count where index=* by index, sourcetype
| sort - count
```

**The two-gap answer.** Keep these separate — SSE will happily blur them:

1. **Detectable today, not detected.** Content SSE unlocks that you are not
   running. Cheap to close: it is engineering effort, no ingest cost.
2. **Not detectable at any effort.** The telemetry is absent. No amount of
   detection work closes this; someone has to onboard a data source.

**The three-source prioritisation, costed.** Estimate each against the licence
model from [SPL-06](../../docs/modules/splunk/spl-06-enterprise-admin.md) Topic 10.
Order by *content unlocked per GB/day*, not by content unlocked:

| Source | Content unlocked | Est. GB/day | Ratio | Why |
|---|---|---|---|---|
| Sysmon 3, 7, 11, 12–14, 22 | | | | Extends an agent you already run |
| 4769 / Kerberos service tickets | | | | Closes the credential-access gap from Lab 4 |
| TLS/JA3 or full HTTP metadata | | | | Expensive per GB; be honest about it |

**Deliverable:** the assessment, the two-gap statement, and the costed
prioritisation. A list ordered by content unlocked with no cost column does not
meet the brief — the module's point is that detection coverage is bought, and
someone signs for it.
