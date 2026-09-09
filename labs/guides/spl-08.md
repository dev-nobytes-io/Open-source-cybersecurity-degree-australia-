# SPL-08 lab guide — Implementation & Consulting

**Module:** [SPL-08](../../docs/modules/splunk/spl-08-consultant.md) · 7 labs,
1 ✅ on Free, 4 📄 no platform, 2 ⚠️ trial licence.

**The blueprint correction matters here.** The Core Certified Consultant exam
blueprint contains essentially no consulting-practice content — it is roughly 90%
technical, weighted towards indexer clustering, data collection, indexing, search
and search-head clustering. The module's Part A covers that. **The labs, however,
are deliberately the other half**: the technical work is exercised in
[SPL-06](spl-06.md) and [SPL-07](spl-07.md), and repeating it here would waste the
module.

So five of these seven labs have no Splunk in them at all. That is not a licensing
compromise — it is the subject. The thing that separates a consultant from a
skilled administrator is not cluster configuration.

**A note on the paper labs.** They need a second person: a peer to role-play the
client, inject a failure, or receive bad news. Done alone they degenerate into
writing down what you already believe, which is the failure mode this module
exists to correct. If you have no peer, write the client's side first, in
character, before you write your own — and write it to win.

---

## Lab 1 📄 — Find the Real Requirement

**The scenario** (use it, or write a worse one — real briefs are worse):

> *"We need Splunk to give us a single pane of glass for security. Our current SIEM
> is too slow. We want all dashboards migrated by end of quarter, and we need it to
> use AI for threat detection. Budget is approved."*

Four stated requirements, and not one of them is verifiable. Elicit until each
becomes a statement you could pass or fail.

**The elicitation questions that actually work** are the ones that convert a
preference into an observable event:

| They said | Ask | Because |
|---|---|---|
| "Single pane of glass" | *Who is looking at the pane, and what do they do next?* | Usually two audiences with incompatible needs; "one dashboard" is a compromise nobody wanted |
| "Too slow" | *Slow doing what? What did you time, and what would fast enough be?* | "Slow" is often a 40-minute analyst workflow of which the SIEM is 90 seconds |
| "All dashboards migrated" | *Which dashboards were opened in the last 90 days, and by whom?* | Typically 15% of them. Migrating the rest is pure cost |
| "Use AI" | *What decision would it make, and what happens when it is wrong?* | Often means "reduce alert volume", which is a tuning problem with a known solution |
| "Budget approved" | *Approved by whom, against what, and until when?* | The most load-bearing sentence in the brief and the least often verified |

**The requirements document.** Each requirement needs an acceptance test somebody
could run without you in the room:

| # | Requirement | Acceptance test |
|---|---|---|
| R1 | An analyst can determine whether an account is compromised without leaving one interface | Timed: 10 sampled alerts, median under 4 min, no other tool opened |
| R2 | Detections over the last 24 h return in under 10 s at p95 | Measured over 200 executions in production conditions |
| R3 | The 22 dashboards opened more than twice in 90 days are migrated | Usage report before and after |
| R4 | Tier-1 alert volume falls to under 60/shift without reducing true positives | Measured over 4 weeks against labelled outcomes |

Note what R4 did to "use AI": it turned a technology request into an outcome, which
is now satisfiable by tuning, risk-based alerting, or machine learning — whichever
works — and is testable either way. That is the job.

**The assessed artefact** is the note: what they asked for, what they need, and
**how you established the difference**. The third part is the one that gets skipped
and the only one that demonstrates skill. "I asked what they meant" is not a
method. "I pulled 90 days of dashboard-usage data and 22 of 140 dashboards had been
opened more than twice" is.

---

## Lab 2 ✅ — Build a Base Configuration

Runs on Free against the lab instance. This is the one technical lab worth
repeating here, because a base configuration is a *deliverable to a client*, not a
working system, and that changes what "done" means.

```
oscd-base/
  README.md
  base_indexes/default/indexes.conf
  base_parsing/default/props.conf
  base_parsing/default/transforms.conf
  base_forwarder_outputs/default/outputs.conf
  deployment-apps/                      # what the DS pushes
  DEVIATIONS.md
```

**Parsing standard.** Mandatory in every sourcetype stanza, no exceptions granted
without a deviation record:

```conf
[<sourcetype>]
SHOULD_LINEMERGE = false
LINE_BREAKER     = <explicit>
TRUNCATE         = <explicit>
CHARSET          = UTF-8
TIME_PREFIX      = <explicit>
TIME_FORMAT      = <explicit>
MAX_TIMESTAMP_LOOKAHEAD = <explicit>
TZ               = <explicit>
```

**The README must explain every non-obvious setting**, and "non-obvious" means
*non-obvious to the client's admin in two years*, not to you today. The test is
whether each entry answers "why is this not the default?":

> `SHOULD_LINEMERGE = false` — set on every sourcetype, including single-line ones.
> The default (`true`) makes Splunk guess at record boundaries using
> `BREAK_ONLY_BEFORE`, which is slow and is wrong the first time a message contains
> a newline. Setting it false and specifying `LINE_BREAKER` is faster and
> deterministic. Cost: a new sourcetype cannot be onboarded by copying an existing
> stanza without thinking about its record boundary. That cost is intended.

**Onboard three dissimilar sources using only the standard.** Use the lab data:
`proxy` (JSON, single line), `awkward.log` from [SPL-06 Lab 2](spl-06.md)
(multi-line, `%d/%m/%Y`), and one of your own with a header row or a fixed-width
format. Dissimilar is the requirement — three JSON sources prove nothing.

**The one documented, justified deviation is the assessed part.** A standard with
no deviations has not met reality. A good one reads:

> **DEV-001 — `oscd:awkward`: `MAX_TIMESTAMP_LOOKAHEAD = 20` (standard: 40)**
> The record body contains `code=4624`, which the timestamp parser will happily
> read as a year at lookahead 40. Restricting the lookahead to the bracketed prefix
> is the narrowest fix. Alternatives considered: `TIME_PREFIX` alone (insufficient
> — the parser still scans forward), and stripping the field (rejected, it is
> needed). Review when the source format changes. Owner: platform team.

That structure — deviation, reason, alternatives considered and rejected, review
trigger, owner — is what makes a deviation register useful rather than a list of
exceptions nobody revisits.

---

## Lab 3 ⚠️ — Staged Migration with Rollback

**Trial licence and multiple instances.** Reuse the [SPL-07](spl-07.md) cluster
inside the same trial window; the migration plan itself is
[SPL-07 Lab 5](spl-07.md)'s work, and this lab executes it under failure.

**Define stages, gates and rollbacks before starting.** Writing the rollback after
the stage has begun is not a rollback, it is improvisation with a document
attached.

**The peer injects a failure at a stage of their choosing** — and does not tell you
which. Realistic injections, in rough order of instructiveness:

| Injection | What it tests |
|---|---|
| Kill a peer during bucket fix-up | Whether your gate distinguished "replication started" from "replication complete" |
| Corrupt one peer's `server.conf` after the gate passed | Whether your gate is a point check or a continuous condition |
| Silently revert a config the deployment server pushed | Whether you verify convergence or trust the push |
| Fill a disk on one peer | Whether the plan has any resource precondition at all |

**Execute the rollback and record it**, including the wall-clock time. That number
is what a client actually buys from you: not that you have a rollback, but that
you know it takes 40 minutes and have done it.

**The honest account of what the plan did not anticipate is the deliverable.** Two
things almost always appear and are worth watching for:

1. **A rollback that is not idempotent.** Halfway back, something is in neither
   state. The plan assumed rollback was the forward path reversed, which it is not
   — replication that occurred does not un-occur.
2. **A validation gate that passed on stale information.** The check ran against a
   cached status, or against the manager's belief rather than the peers' state.
   This is why [SPL-07 Lab 2](spl-07.md) insists on three different verification
   sources: they disagree exactly when it matters.

---

## Lab 4 📄 — Health Assessment and Roadmap

Use a documented case study or an intentionally degraded deployment. The
degradations from [SPL-06 Lab 7](spl-06.md) and [SPL-07 Lab 3](spl-07.md) are a
ready-made estate if you have run those.

**Structure the assessment**, because an unstructured one becomes a list of
whatever you happened to notice:

| Domain | Evidence to gather |
|---|---|
| Ingest health | `metrics.log` thruput by sourcetype, queue fill, forwarder connection stability |
| Data quality | `_time` vs `_indextime` skew, CIM compliance, sourcetype sprawl |
| Search health | Skipped searches, concurrency headroom, long-running searches |
| Content health | Detections that never fire, detections that always fire |
| Configuration | `btool check`, config drift from any base standard |
| Access | Role sprawl, standing admin, service-account privilege |
| Capacity | Storage headroom against retention obligations, growth trend |

**Every finding needs evidence attached.** "Data quality is poor" is not a finding.
"41% of `sourcetype=vendor:app` events have `_time` more than 6 hours from
`_indextime`, indicating a missing `TZ` setting; query attached" is.

**The roadmap.** Ordered by **risk × value ÷ effort**, with effort estimated in
days, and — the part that is graded — an explicit **accept and document** category.

| Finding | Risk | Effort | Action |
|---|---|---|---|
| Retention on `sec_high` capped by `maxTotalDataSizeMB` at ~4 months against a 7-year obligation | **Critical** — compliance | 2 d | Fix now |
| 6 of 40 detections have never fired | High | 5 d | Triage: broken vs rare |
| Timezone missing on one source | Medium | 0.5 d | Fix now — cheapest item here |
| Sourcetype sprawl: 340 sourcetypes, 90 unused | Low | 20 d | **Accept and document** |
| No base configuration standard | Medium | 15 d | Schedule Q3 |

**"A roadmap where everything is priority one is a failed roadmap"** — the module
is right and it is worth understanding why, because the instinct to flag everything
feels like diligence. It is the opposite: a roadmap with no priorities transfers
the prioritisation decision back to the client, who has less information than you
do. You were hired for the ordering. The accept-and-document row is the proof you
did the work: you found it, you costed it, and you concluded it was not worth
fixing — which is a finding, not an omission.

---

## Lab 5 📄 — Deliver the Bad News, Then Hand Over

Two audiences, two failure modes, and the decision register weighted most heavily.

### Part 1 — the presentation

**To the team who built it.** They are in the room, they made these choices, and
several were reasonable under constraints you cannot see. The technique that works:

- Lead with what is working, specifically and briefly. Not as softening — as
  accuracy. A deployment with a compliance-breaking retention setting usually also
  has six things done well, and an assessment that does not mention them is a bad
  assessment.
- Attribute findings to the **system**, not the people: "the retention setting was
  never revisited after the volume grew" is both truer and more useful than "you
  configured retention wrong".
- Never present a finding they can correct in the room. Send findings in advance.
  Being wrong in public makes an enemy of the person whose cooperation you need for
  the next six months.

**To the executive who wants to know why it costs more.** Different failure mode
entirely: here the risk is hedging.

- Lead with the number and the decision. They will read three sentences.
- Convert findings into consequences in their terms: not "no continuity
  monitoring" but "we would not know a data source had stopped, and the first
  time we would find out is during an incident when the data is not there".
- Give the costed menu from [SPL-07 Lab 1](spl-07.md)'s one-pager. Never one
  option — one option reads as a demand.
- **Do not hedge the compliance finding.** If retention is short of an obligation,
  say so plainly and put a date on it. This is the one place where softening the
  message is a professional failure rather than a communication style.

### Part 2 — the handover pack

- **Runbooks** — one per recurring operation, written so someone who was not in
  the project can execute it. Test this by having a peer follow one literally.
- **Known limitations** — everything the accept-and-document category holds, plus
  every workaround with the reason it exists.
- **Decision register** — weighted most heavily, and rightly.

**The decision register** is the most valuable artefact a consultant leaves behind,
because it is the only one that answers *why*:

| ID | Decision | Alternatives considered | Rationale | Revisit when |
|---|---|---|---|---|
| D-004 | RF=3, SF=2 | 2/2 (insufficient margin), 3/3 (+35% storage for unrequired resilience) | Tolerance is one peer with no search interruption; 3/2 meets it with margin | Peer count > 20, or tolerance changes |
| D-011 | Operational retention 90 d | 180 d (+21 TB), 45 d (loses slow-burn investigation) | No stated obligation; 90 d covers observed investigation depth | If an obligation is introduced |
| D-019 | Accept 90 unused sourcetypes | Cleanup (20 d) | No operational cost; cleanup risk exceeds benefit | If sourcetype count affects search performance |

Two years later, nobody remembers why RF is 3. Without D-004 the next consultant
either changes it — reintroducing a risk somebody already reasoned about — or leaves
it alone out of caution, which is how estates ossify. The register is what makes a
system safe to change, and safe-to-change is the actual deliverable.

**The reflection on what you would say differently** is assessed. Write it the same
day, before the memory tidies itself into a version where you were right.

---

## Lab 6 ⚠️ — Implement a Cluster to a Standard

**Trial licence.** Mechanically this is [SPL-07 Lab 2](spl-07.md); what is
different is that here it is a **client deliverable**, so "it works" is not the
completion criterion.

**Three things must be evidenced**, and the second is the one that fails:

1. **Replication occurred** — `dbinspect` per peer, plus `cluster-status`.
2. **The base config from Lab 2 applied on every peer.** Not "was pushed" —
   *applied*. Verify on each peer independently, because a deployment server
   reports what it sent, not what took effect:
   ```bash
   for p in idx1 idx2 idx3; do
     echo "== $p"; docker exec $p /opt/splunk/bin/splunk btool props list oscd:proxy --debug | head
   done
   ```
3. **A peer failure behaves as specified.** Kill one and evidence the specified
   behaviour, not merely "it recovered".

**The runbook is the deliverable, not the cluster.** Write it so it is repeatable
by someone else: exact commands, expected output at each step, and what to do when
the output differs. A runbook that only describes the happy path is a description,
not a procedure.

**Completion criteria you would sign against.** Write them as pass/fail, before
building — this is the discipline the lab is really teaching:

- [ ] `cluster-status` reports all indexes searchable, RF and SF met, zero fix-up tasks pending
- [ ] `btool` output for the base config is byte-identical across all peers
- [ ] With one peer down, a control search returns the same event count as with all peers up
- [ ] Recovery to full RF/SF after peer restoration completes within N minutes, measured
- [ ] The build runbook was executed end-to-end by someone other than its author

The last one is the one clients should insist on and rarely do.

---

## Lab 7 📄 — Design the Operating Model

No platform. The uncomfortable question is the graded part.

**RACI across three distinct ownerships** — and the reason to separate them is that
they fail differently and need different skills:

| Activity | Platform | Content | Detection | Client SOC |
|---|---|---|---|---|
| Index and retention changes | **A/R** | C | C | I |
| Onboard a new data source | **R** | C | **A** | I |
| Write or tune a detection | I | C | **A/R** | C |
| Promote content to production | C | **A/R** | R | I |
| Triage a finding | I | I | C | **A/R** |
| Capacity planning | **A/R** | I | C | I |

Note that "onboard a data source" is *accountable to detection*, not to platform.
Platform can execute it; only detection knows whether the source closes a gap or
just adds licence cost. Getting that arrow backwards is how estates end up
ingesting a lot and detecting little.

**The run-book set.** Minimum viable: peer replacement, adding an index, onboarding
a source, restoring from a bad deployment push, responding to a data-source outage,
and the quarterly retention review. Each one is a thing that will happen and that
someone will otherwise improvise.

**The growth plan.** From [SPL-07 Lab 1](spl-07.md): 25%/year means a 4.8× estate
in seven years. The operating model has to say what triggers the next architecture
review — a threshold, not a date. "When ingest exceeds 1.5 TB/day or indexer count
exceeds 20, whichever first" is a plan; "annually" is a calendar entry.

### The build-versus-manage recommendation

**State the conflict of interest first, in writing, in the document itself.** Not
in a footnote:

> *Our firm's implementation revenue is higher if this client builds and operates
> in-house. This recommendation is made against that interest and the reasoning is
> set out below so it can be checked.*

**Then reason it honestly.** The question is not competence, it is *sustained
capacity*, and the tests are concrete:

| Test | Build in-house viable if... |
|---|---|
| Headcount | ≥ 2 people can operate the platform, so leave and illness are survivable |
| Depth | At least one has clustering experience, or a funded path to it |
| On-call | 24/7 coverage exists, or the business accepts business-hours recovery |
| Retention | Those people are unlikely to leave within 18 months |
| Load | Platform work is < 50% of their role, or is their whole role |

**One person who is excellent is a failure of this test, not a pass.** A
single-person platform capability is an outage waiting on a resignation, and saying
so is more valuable to the client than the work you would win by not saying it.

**Write the recommendation with its costs both ways**, including the ones that
count against your own position: managed service has an ongoing cost, creates a
dependency, and slows changes that need a ticket. Say that too. A recommendation
that only lists the advantages of the option you chose is advocacy, and clients can
tell the difference — which is, in the end, what this module is about.
