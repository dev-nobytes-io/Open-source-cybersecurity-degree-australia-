# SPL-05 lab guide — SOAR & Security Automation

**Module:** [SPL-05](../../docs/modules/splunk/spl-05-soar.md) · 8 labs,
6 📄 no platform, 2 🔒 SOAR platform required.

**No lab in this module runs on the Splunk Free licence**, because none of them
are about Splunk. Splunk SOAR is a separately licensed product and its community
availability is unverified — the module says so and this guide will not pretend
otherwise.

That sounds worse than it is. Six of the eight labs are design and analysis, and
they are the six that matter most. The module's own gating lab is one of them:
**automating an undocumented process is the failure this module exists to
prevent**, and you do not need a platform to avoid it.

Lab 4 needs no SOAR either — it is Python against an HTTP API, and everything
transferable about writing a connector transfers from any language to any
platform.

---

## Lab 1 📄 — Map a Process Before Automating It

The gate. Do not skip it, and do not do it from memory.

**Use a process you can actually observe:** the suspicious-authentication triage
from [SPL-03 Lab 2](spl-03.md), which you have now performed. Write down what you
did — not what you would recommend, what you *did*, including the parts that were
guesses.

Record for each step: the input, the source consulted, the decision made, the
possible outcomes, and how long it took.

| # | Step | Input | Source | Decision | Outcomes | Time |
|---|---|---|---|---|---|---|
| 1 | Confirm the source is external | `src` | RFC1918 check | mechanical | internal / external | 5 s |
| 2 | Count distinct accounts targeted | `src` | `wineventlog` | mechanical | number | 20 s |
| 3 | Check whether any attempt succeeded | `src` | `wineventlog` | mechanical | yes / no | 20 s |
| 4 | Look up the victim's role and privilege | `user` | identity lookup | mechanical | context | 10 s |
| 5 | **Decide whether this is worth waking someone** | all of the above | judgement | **judgement** | escalate / queue / close | 2 min |
| 6 | Write the disposition | — | — | judgement | text | 3 min |

**Classify against the decision boundary.** The useful test is not "is this hard?"
but **"is this step reversible, and is its input trustworthy?"**

| Class | Test | Automate? |
|---|---|---|
| Mechanical, reversible | Deterministic given the input; wrong answer costs a re-run | Yes |
| Mechanical, irreversible | Deterministic, but the action cannot be undone | Only behind an approval |
| Judgement | Requires weighing incommensurable things | No — automate the *inputs* to it |

**The deliverable is the "do not automate" list**, and steps 5 and 6 above belong
on it for different reasons. Step 5 is judgement. Step 6 looks automatable — a
template could write it — and must not be, because a disposition written by a
template stops recording that a human considered the case, and the record is the
whole point of a disposition.

Note how much of the *elapsed* time is in steps 5 and 6, and how little is in the
four mechanical steps. That ratio is the honest answer to "how much would
automation save here", and it is much less than the sales figure. Keep it: Lab 7
comes back to it.

---

## Lab 2 🔒 — An Enrichment Playbook That Fails Well

**Blocker:** requires a SOAR platform. There is no substitute — the failure modes
the lab is about (asset unreachable, rate limit, malformed response, missing
artefact) are platform behaviours, and simulating them in a script tests your
script, not the platform.

**Design it in full anyway**, because the design is what you would take to a
platform on day one. The specification the lab demands:

For each of three enrichment sources, define behaviour under four failures. The
constraint that makes this hard is the module's: **fail without producing a wrong
answer**.

| Failure | Wrong-answer trap | Correct behaviour |
|---|---|---|
| Asset unreachable | Treating "no response" as "no reputation data" and therefore as benign | Mark the artefact **unenriched**, distinctly from *enriched-and-clean* |
| Rate limit (HTTP 429) | Retrying immediately, compounding the limit | Back off exponentially with jitter; after N attempts, unenriched |
| Malformed response | Parsing partially and using whatever fields survived | Fail closed on a schema violation; log the raw response |
| Missing artefact | Running the action on a null and recording its result | Skip with a reason, never a default |

**The single most important design decision in this lab** is that
*unknown* and *clean* must be different values all the way through to the
analyst's screen. Almost every enrichment playbook that goes wrong goes wrong here:
a two-state field (`malicious` / `not malicious`) silently converts every outage
into an all-clear, and it does so at exactly the moment the estate is under stress
and the enrichment provider is overloaded.

**Deliverable without a platform:** the playbook design, the failure table with
your logging output for each case written as the analyst would see it, and an
explicit statement of the three-state model and where it is enforced.

---

## Lab 3 📄 — A Guarded Response Playbook

Design achievable without a platform, and the module says so.

**Four components, all required:**

1. **A bounded target set.** Define what the playbook may act on, positively —
   never by exclusion. "Any host except domain controllers" fails the moment a
   new DC is built and not tagged. Use the asset lookup:

   ```
   | inputlookup oscd_assets.csv
   | where role=="workstation" AND category!="crown_jewel"
   | stats count, values(bunit) as departments
   ```

   That set is the playbook's entire universe. Anything outside it escalates to a
   human, including anything the lookup does not know about — an unknown asset is
   out of scope, not in it.

2. **An approval prompt**, with defined timeout behaviour. The design question
   the module is testing is what happens when nobody answers at 3 a.m. There are
   only two defensible answers and you must pick one and justify it:

   - **Timeout → no action.** Correct when the action is irreversible or the
     false-positive cost is high. Accepts that a real incident may run unchecked.
   - **Timeout → escalate to a second approver, then no action.** Correct when
     you have 24-hour coverage. Never "timeout → proceed".

3. **A reversal procedure**, written before the action is ever taken. If you
   cannot write down how to undo it, the action is not automatable — that is the
   test, not a formality. For a host containment: which control did what, what the
   pre-state was, who can restore it, and how long restoration takes.

4. **The false-positive test.** Have a peer hand you an input that looks
   actionable and is not. The obvious candidate from this dataset is a **service
   account** — high volume, privileged, trips several detections, and containing
   it takes down a backup or a monitoring pipeline at 3 a.m.

   ```
   index=risk entity_type=user
   | lookup oscd_identities.csv identity as entity OUTPUT category, priority
   | where category=="service_account"
   | stats sum(risk_score) as risk by entity | sort - risk
   ```

**Deliverable:** all four, plus the false-positive result. If your bounded target
set already excluded the service account, say so — that is the design working, and
it is worth more than a guard that catches it later in the chain.

---

## Lab 4 📄 — Build a Custom App

No SOAR needed. Write the connector as a plain Python module with the same shape
a platform connector has, and the port later is mechanical.

**Pick a genuinely free API with no key**, so the lab does not stall on
registration. Two that work: `https://dns.google/resolve?name=<domain>&type=A`,
and `http://ip-api.com/json/<ip>` for geolocation.

**Four required behaviours**, and the last two are where the marks are:

```python
"""Connector skeleton: two actions, real validation, real error handling."""
import json
import re
import urllib.error
import urllib.request

_DOMAIN = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$")
_TIMEOUT = 5


class ActionResult:
    """Three states, never two. `unknown` is not `clean`."""
    def __init__(self, status, data=None, message=""):
        assert status in ("success", "failed", "unknown")
        self.status, self.data, self.message = status, data or {}, message

    def __repr__(self):
        return f"<{self.status}: {self.message or self.data}>"


def _get(url):
    try:
        with urllib.request.urlopen(url, timeout=_TIMEOUT) as r:
            if r.status != 200:
                return ActionResult("unknown", message=f"HTTP {r.status}")
            return ActionResult("success", json.loads(r.read().decode()))
    except urllib.error.HTTPError as e:
        # 429 is retryable; 4xx is not. Conflating them is the classic defect.
        kind = "unknown" if e.code in (429, 500, 502, 503, 504) else "failed"
        return ActionResult(kind, message=f"HTTP {e.code}")
    except (urllib.error.URLError, TimeoutError) as e:
        return ActionResult("unknown", message=f"unreachable: {e}")
    except json.JSONDecodeError as e:
        return ActionResult("failed", message=f"malformed response: {e}")


def test_connectivity():
    r = _get("https://dns.google/resolve?name=example.com&type=A")
    return ActionResult("success" if r.status == "success" else r.status,
                        message="connector reachable" if r.status == "success"
                                else r.message)


def resolve_domain(domain):
    """Action 1. Output schema: {domain, resolved: bool, answers: [str]}"""
    if not _DOMAIN.match(domain or ""):
        return ActionResult("failed", message=f"invalid domain: {domain!r}")
    r = _get(f"https://dns.google/resolve?name={domain}&type=A")
    if r.status != "success":
        return r
    answers = [a["data"] for a in r.data.get("Answer", []) if a.get("type") == 1]
    return ActionResult("success", {"domain": domain,
                                    "resolved": bool(answers),
                                    "answers": answers})


def geolocate_ip(ip):
    """Action 2. Output schema: {ip, country, city, lat, lon, asn}"""
    parts = (ip or "").split(".")
    if len(parts) != 4 or not all(p.isdigit() and 0 <= int(p) < 256 for p in parts):
        return ActionResult("failed", message=f"invalid IPv4: {ip!r}")
    r = _get(f"http://ip-api.com/json/{ip}")
    if r.status != "success":
        return r
    d = r.data
    if d.get("status") != "success":
        return ActionResult("unknown", message=d.get("message", "no data"))
    return ActionResult("success", {"ip": ip, "country": d.get("countryCode"),
                                    "city": d.get("city"), "lat": d.get("lat"),
                                    "lon": d.get("lon"), "asn": d.get("as")})
```

**Prove the failure paths, not just the happy path.** The module requires evidence
of correct behaviour on authentication failure and malformed response, and those
are the ones nobody tests:

```python
print(resolve_domain("example.com"))          # success
print(resolve_domain("not a domain"))         # failed — validation, no network call
print(resolve_domain(None))                   # failed — no exception
print(geolocate_ip("8.8.8.8"))                # success
print(geolocate_ip("999.1.1.1"))              # failed — validation
print(_get("https://dns.google/resolve?name=example.com&type=A&x=%00"))  # malformed/HTTP
```

**Document the output schema explicitly** — field name, type, nullability, and
what a missing value means. A connector whose schema is "whatever the API
returned" is a connector that breaks silently when the vendor adds a field, and
every playbook downstream of it inherits the breakage.

**Deliverable:** the code, evidence of both actions working, and evidence of the
two failure paths. The three-state `ActionResult` from Lab 2 is not decoration —
if your connector collapses `unknown` into `failed`, a rate limit becomes an
error, and if it collapses into `success`, an outage becomes an all-clear.

---

## Lab 5 📄 — Case Management and the Audit Trail

Design, no platform. The worked reconstruction is the deliverable; the case model
is scaffolding for it.

**Case model — the parts that need defining:**

- **Severity**, defined by *impact and response time*, never by a detection's own
  score. A detection cannot know your business.
- **SLA per severity**, with the clock start defined precisely: detection time,
  not triage time. Starting at triage means a backlog makes your SLA look better.
- **Ownership and handoff**, with an explicit rule for what happens at shift end
  to a case in progress.
- **Evidence requirements** per severity — what must be attached before a case can
  close.

**The audit fields, which are the actual subject.** Design them by working
backwards from the reconstruction, which is what the module asks for:

> An automated containment fired wrongly. Reconstruct it.

Four questions, and each needs a field that exists *before* the incident:

| Question | Field(s) | Failure if absent |
|---|---|---|
| What fired? | playbook id **and version hash** | You can see it ran, not what it was — the playbook has been edited since |
| On what input? | the artefact **as received**, serialised | You have the container's current state, which the playbook then modified |
| Who approved? | approver identity, timestamp, prompt text shown | You know it was approved, not what they were told they were approving |
| What changed? | per-action target, pre-state, post-state, reversal token | You know it ran; you cannot undo it |

**The version hash is the one people miss** and it is the one that matters. Six
weeks later, "playbook `contain_host` v?" is not an answer, and the repository
history will not tell you which version was deployed at 03:14 on the night in
question unless something recorded it.

**Do the reconstruction as a written exercise.** Take a false containment of a
service account (Lab 3's false positive), and walk the four questions with your
field list in hand. Where you cannot answer, add the field. That iteration is the
lab.

---

## Lab 6 📄 — Attack Your Own Automation

Threat modelling. A platform helps but is not required — the analysis is about
privilege, and privilege is documented.

**Enumerate what the automation can do**, which is almost always more than its
owners think. For each asset the platform holds credentials for:

| Asset | Credential | Effective privilege | Needed privilege | Gap |
|---|---|---|---|---|
| Active Directory | service account | Domain Admin (typical) | Disable user; read group membership | Enormous |
| EDR | API token | Full console, incl. policy edit | Isolate host; query telemetry | Large |
| Firewall | admin | Full config | Add block rule to one object group | Large |
| Splunk | search head user | `admin` (typical) | Run saved searches; write to one summary index | Large |
| Email gateway | admin | Read all mail, purge any message | Purge by message id | Large |

**Then the question the lab is actually asking:** what could an attacker with
**playbook-edit access** suppress? This is the interesting half, because it is not
about stealing the credentials — it is about the automation being a *control* and
therefore a target.

An attacker who can edit playbooks can:

- Add an early exit for artefacts matching their own infrastructure. The playbook
  still runs, still reports success, and does nothing.
- Change a containment action to a no-op while leaving its logging intact.
- Widen a bounded target set so a future containment causes an outage, as cover.
- Edit the enrichment step to return `clean` instead of `unknown` on failure —
  invisible, and it degrades every downstream decision.

**Least-privilege re-scoping for three assets.** Be specific: the AD account needs
`Enable/disable user` on one OU, not Domain Admin. Write the delegation.

**Detection for unauthorised playbook modification.** The design that works is not
"alert on edit" — edits are normal. It is:

1. Playbooks in version control; the platform's copy reconciled against the
   repository head on a schedule.
2. Alert on **divergence**, not on change: a playbook whose deployed hash does
   not match any committed hash.
3. Alert on edits by an identity that has never edited before, and on edits
   outside business hours, as weaker secondary signals.

Point 2 is the one that catches the attacker, and it costs nothing but the
discipline of Lab 6 in [SPL-04](spl-04.md) — content under version control.

---

## Lab 7 📄 — Measure and Retire

Given a portfolio with run statistics. Generate a plausible one so the arithmetic
is real:

```bash
python3 - <<'PY'
import csv, random
random.seed(7)
rows = [
    # name, runs, success, avg_sec, manual_min, last_edit_days, last_run_days
    ("enrich_ip_reputation",     4820, 4611, 12, 4,   38,   0),
    ("enrich_url_sandbox",        910,  402, 240, 15, 210,   1),
    ("contain_host_edr",           31,   29, 45, 25,  95,   6),
    ("disable_user_ad",            18,   17, 20, 15, 140,  11),
    ("notify_oncall",            5210, 5198,  3,  2,  60,   0),
    ("phishing_triage_full",      680,  310, 180, 35, 250,   2),
    ("block_domain_firewall",      12,    5, 60, 20, 320,  74),
    ("legacy_ticket_sync",        140,   12, 30, 10, 480, 190),
]
with open('playbook_portfolio.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(["playbook","runs","successes","avg_sec","manual_min",
                "days_since_edit","days_since_run"])
    w.writerows(rows)
print("wrote playbook_portfolio.csv")
PY
```

**Assess on three axes**, not one:

```bash
python3 - <<'PY'
import csv
for r in csv.DictReader(open('playbook_portfolio.csv')):
    runs, succ = int(r['runs']), int(r['successes'])
    rate = succ / runs
    saved_h = succ * int(r['manual_min']) / 60
    print(f"{r['playbook']:26} runs={runs:5} success={rate:5.0%} "
          f"saved={saved_h:7.0f}h  edited={r['days_since_edit']:>3}d ago  "
          f"last run={r['days_since_run']:>3}d ago")
PY
```

| Axis | Question | Red flag |
|---|---|---|
| **Value** | Is it doing useful work? | Low run count, or high runs × trivial time saved |
| **Maintenance** | Is anyone looking after it? | Success rate well under 100% and no edit in months |
| **Relevance** | Does the thing it handles still happen? | No run in weeks |

**The retirement candidates fall out immediately**, and they fail on different
axes — say which:

- `legacy_ticket_sync` — 9% success, not run in six months, not edited in 16.
  Failing on all three. Retire.
- `block_domain_firewall` — 42% success, 74 days idle, untouched for nearly a
  year. Either the action is broken or the process moved elsewhere. **Find out
  which before retiring**, because a broken containment playbook is a control
  everyone believes exists.
- `enrich_url_sandbox` — 44% success but runs constantly and is recent. Not a
  retirement candidate, a *repair* candidate, and the most urgent item here: it is
  silently failing on more than half of a high-volume path.

**The critique of "hours saved" is the graded part.** The number above is
`successes × manual_minutes`, which is how every vendor computes it, and it is
wrong in at least five ways:

1. **It counts work nobody would have done.** `enrich_ip_reputation` ran 4,611
   times. No human was ever going to hand-enrich 4,611 IPs; they would have
   enriched the twenty that mattered. Automating something makes it cheap, so you
   do vastly more of it — most of the "saved" hours were never going to be spent.
2. **It ignores maintenance.** A playbook against six APIs breaks when any of the
   six changes. That engineering time is real and is never in the numerator.
3. **It ignores the failures.** 56% of `enrich_url_sandbox` runs failed. An
   analyst still had to do those *and* work out why the automation did not.
4. **It ignores the tail.** Automation handles the common case and hands you the
   hard ones, so average handling time on what remains goes **up**. Comparing
   pre- and post-automation averages without noting that is a category error.
5. **It counts saved time as saved money**, which it is not unless someone was
   let go or a queue actually shortened. Usually the freed capacity went into more
   alerts — which may be good, and is not what the metric claims.

**A defensible metric instead:** time-to-containment for the incidents that
mattered, and the number of decisions an analyst made per shift. Both are harder
to game and both go in the direction you actually care about.

---

## Lab 8 🔒 — Wire ES to SOAR

**Blocker:** requires both Enterprise Security and a SOAR instance. Two licensed
products; no substitute exists and none is offered here.

**The design question is answerable without either**, and it is the one the module
puts most weight on: *what happens to the SOAR container when the ES finding is
later closed by an analyst?*

Nothing, by default. That is the answer, and it is the problem.

The two systems each hold state, each believes it is authoritative, and the export
app is one-directional. Analysts close findings in ES; automation closes
containers in SOAR; neither tells the other. Within a month the container queue
and the finding queue disagree about what is open, and the metrics from both are
wrong in opposite directions.

**Design the reconciliation.** Four options, and you should pick one and defend it:

| Design | Mechanism | Cost |
|---|---|---|
| **One-way, ES authoritative** | SOAR container closure writes back to the ES finding; ES closure closes the container | Needs a bidirectional integration; simplest mental model |
| **One-way, SOAR authoritative** | ES findings become read-only once exported | Analysts lose the ES workflow they know |
| **Periodic reconciliation** | Scheduled job compares both queues, reports divergence | Simple, tolerant of outages, but divergence is detected rather than prevented |
| **Correlation id only** | Both stay independent; a shared id lets you join them for reporting | Cheapest, honest, no synchronisation illusion — and often the right answer |

The fourth deserves more credit than it usually gets. Two systems that are
*honestly independent* and joinable for reporting cause fewer incidents than two
systems that are *supposedly synchronised* and occasionally are not.

**Deliverable without platforms:** the integration design, the state-synchronisation
analysis above with your chosen option defended, and the specific field you would
add to both sides to make the join possible. Note when you would find out your
synchronisation had failed, and how — because "we would notice" is not a mechanism.
