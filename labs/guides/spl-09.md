# SPL-09 lab guide — Detection Analytics & Risk Scoring

**Module:** [SPL-09](../../docs/modules/splunk/spl-09-detection-analytics.md) ·
8 labs. **Every one of them can be completed without a Splunk instance.**

That is not a compromise here — it is the nature of the material. This module is
arithmetic, and the arithmetic does not care what stores the data. The lab dataset
is JSONL on disk and CSV lookups; Python's standard library reads both. Where a lab
has an SPL implementation, it is given, because you will need to write it in SPL
one day. Where the analysis is the point, Python is the shorter road and no
instance is required.

```bash
python3 generator/generate.py --days 14      # ~101k events, 8 labelled scenarios
ls data/events/                              # cloud dns proxy risk sysmon wineventlog
```

!!! note "No numpy, no pandas, no pip"
    Everything below is standard-library Python. That is a deliberate constraint:
    it keeps the arithmetic visible. `sum(x)/len(x)` is a mean you can argue with;
    `df.mean()` is a mean you have to trust.

---

## Lab 1 📄 — Classify Twenty Signals

Pure paper. No data, no code.

**The decision rule**, applied in order — the first question that answers "no"
settles it:

1. Is there a **specific action** a person would take on this, today?
2. Is that action **worth a human's time** at this frequency?
3. Does it need **a human decision**, or is it a threshold?
4. Does anything break if **nobody looks at it for a week**?

| Answer pattern | Classification |
|---|---|
| Action, worth it, needs judgement | **Finding** |
| Action-relevant but not alone; contributes to a picture | **Intermediate finding** |
| Action, worth it, no judgement needed | **Threshold alert** |
| No specific action; supports judgement about *other* things | **Dashboard panel** |

**Twenty candidates.** These are drawn to match the lab data, so you can check
your reasoning against real volumes later:

| # | Candidate signal | Ambiguous? |
|---|---|---|
| 1 | Successful authentication from a source that just failed against 45 accounts | |
| 2 | Any authentication failure | |
| 3 | `certutil.exe` spawning `rundll32.exe` | |
| 4 | A host's DNS NXDOMAIN rate exceeding 50% | ★ |
| 5 | Volume of egress per user per day | |
| 6 | A user's egress exceeding their own 30-day p99 | ★ |
| 7 | Legacy authentication protocol used successfully | |
| 8 | Cloud sign-in from outside Australia | ★ |
| 9 | Domain controller reboot | |
| 10 | Data source stopped sending for 30 minutes | |
| 11 | Licence volume at 90% of entitlement | |
| 12 | Privileged group membership changed | |
| 13 | Count of open findings by analyst | |
| 14 | Any access to a crown-jewel asset by a non-owner | ★ |
| 15 | Median time-to-triage per shift | |
| 16 | A detection that has not fired in 30 days | |
| 17 | Audit log cleared (Windows 1102) | |
| 18 | Failed authentication to a service account | ★ |
| 19 | Encryption on a database changed from enabled to disabled | |
| 20 | Number of assets missing from the identity lookup | |

**Worked examples of the three classes people confuse:**

- **#5 is a dashboard panel, #6 is an intermediate finding.** The distinction is
  not the data; it is that #5 has no action attached — nobody does anything about
  "here is a chart of egress" — while #6 names a specific user against their own
  baseline and contributes to a risk picture. Same telemetry, different artefact,
  because the *decision* differs.
- **#10 and #11 are threshold alerts, not findings.** Both need action, neither
  needs judgement: the action is fixed and known. Routing them through the finding
  queue puts operational work in front of security analysts and trains them to
  close things without reading.
- **#19 is the compliance promotion.** By the decision rule it might be an
  intermediate finding: one config change, weak signal, contributes to a picture.
  It is promoted to a finding anyway, because a control that a regulator or an
  auditor requires must be *demonstrably* actioned, and only a finding leaves that
  record. State the exception explicitly rather than pretending the rule produced it.

**For every dashboard-classified item, answer "what if nobody looks for a week?"**
If the honest answer is "something bad happens", it is not a dashboard — you have
built a finding and given it no way to reach anyone. If the answer is "nothing",
you have justified the classification. This single question retires more bad
dashboards than any design review.

**Deliverable:** all twenty classified, one sentence each naming the question that
settled it, and the week-of-neglect answer for every dashboard item.

---

## Lab 2 📄 — Do the Arithmetic on Your Own Detections

Paper and a calculator. The most valuable lab in the module and it needs nothing.

**The base-rate arithmetic.** For a detection with true-positive rate \(TPR\),
false-positive rate \(FPR\), over a population with base rate \(\pi\):

$$
\text{PPV} = \frac{\pi \cdot TPR}{\pi \cdot TPR + (1-\pi) \cdot FPR}
$$

Use the lab data so the numbers are yours rather than a textbook's:

```bash
python3 - <<'PY'
import csv, collections
rows = list(csv.DictReader(open('data/truth/risk_truth.csv')))
per = collections.defaultdict(lambda: [0, 0])          # [fired, true positive]
for r in rows:
    per[r['search_name']][0] += 1
    if r['scenario'] != 'benign':
        per[r['search_name']][1] += 1
print(f"{'detection':34} {'fired':>6} {'TP':>4} {'PPV':>7}")
for name, (fired, tp) in sorted(per.items(), key=lambda kv: -kv[1][0]):
    print(f"{name:34} {fired:6} {tp:4} {tp/fired:7.1%}")
PY
```

**Then invert it.** Given an observed PPV and an estimated base rate, what FPR does
the detection actually have? Rearranged:

$$
FPR = \frac{\pi \cdot TPR \cdot (1 - \text{PPV})}{(1-\pi) \cdot \text{PPV}}
$$

And the number that changes minds — the FPR required to reach a PPV of 0.25:

```bash
python3 - <<'PY'
def fpr_for_ppv(ppv, pi, tpr=0.8):
    return pi * tpr * (1 - ppv) / ((1 - pi) * ppv)

for pi in (1e-3, 1e-4, 1e-5):
    need = fpr_for_ppv(0.25, pi)
    print(f"base rate {pi:.0e}:  need FPR <= {need:.2e}  "
          f"(1 false positive per {1/need:,.0f} events)")
PY
```

At a base rate of 1 in 100,000 — optimistic for most real detections — a PPV of
0.25 needs a false-positive rate below 1 in 40,000. **Almost no detection written
by hand achieves that**, and the arithmetic says so before you deploy it.

**Estate-wide expected false alert volume.** Sum over detections:

$$
E[\text{false alerts/day}] = \sum_{d} N_d \cdot (1 - \pi) \cdot FPR_d
$$

Compare against stated SOC capacity — analysts × shifts × alerts per analyst per
shift. If expected volume exceeds capacity, the estate is already failing and
adding detections makes it worse. That is a structural finding, not a tuning one.

### The half that is actually graded

**Recommend deleting at least one detection, and make the argument to someone who
does not know Bayes' theorem.** Being right privately is not the skill.

What does not work: probability, rates, or the word "Bayesian". What does work is
counting, in their units:

The table above hands you the argument. **Four of the ten detections have a PPV of
exactly zero** — they fired between 56 and 72 times each and caught nothing.

> *"'Legacy Authentication Protocol' fired 72 times over the period. **None** were
> real. At about 20 minutes each that is roughly 24 hours of analyst time, and it
> has never once been the detection that found something.*
>
> *The two incidents where legacy authentication was actually involved were both
> found by the impossible-travel detection on the same day, so deleting this
> costs us nothing we can point at.*
>
> *If we keep it, we should be honest that we are keeping it because deleting
> detections feels risky, not because it has caught anything.*
>
> *Here is what I would do with the 24 hours instead: [specific thing]."*

Three things make that work and all three are transferable: it is **counted, not
estimated**; it names the **redundancy** (which is what makes deletion safe rather
than merely cheap); and it proposes a **use for the recovered capacity**, so the
conversation is about reallocation rather than reduction. A deletion argument
without the third part gets refused even when it is arithmetically unanswerable.

!!! warning "Zero PPV does not always mean delete"
    Check the redundancy claim before you make it. A detection with zero true
    positives that is the *only* thing watching a technique is not useless — it is
    untested, which is a different finding with a different remedy (see
    [SPL-04 Lab 6](spl-04.md) on canaries for genuinely rare detections). The
    argument above works because the redundancy was verified, not assumed.

---

## Lab 3 ✅ — Build and Calibrate a Decayed Risk Model

Runs on the lab `risk` index in Splunk, and equally in Python with no instance.
The module explicitly accepts a synthetic risk index — and says it is arguably
better pedagogy, because you control ground truth. That is what this dataset is.

**In SPL:**

```
index=risk | `oscd_decay(7)`
| stats sum(decayed_score) as R, dc(search_name) as n_detections by entity, entity_type
| sort - R
```

**In Python, so the arithmetic is visible:**

```bash
python3 - <<'PY'
import csv, collections, math, time

rows = list(csv.DictReader(open('data/truth/risk_truth.csv')))
now = max(float(r['_time']) for r in rows)

def decayed(half_life_days):
    lam = math.log(2) / half_life_days            # ln(2), NOT log10(2)
    R = collections.defaultdict(float)
    n = collections.defaultdict(set)
    bad = collections.defaultdict(bool)
    for r in rows:
        age_days = (now - float(r['_time'])) / 86400
        R[r['entity']] += float(r['risk_score']) * math.exp(-lam * age_days)
        n[r['entity']].add(r['search_name'])
        if r['scenario'] != 'benign':
            bad[r['entity']] = True
    return R, n, bad

for hl in (1, 7, 30):
    R, n, bad = decayed(hl)
    vals = sorted(R.values(), reverse=True)
    p95 = vals[int(len(vals) * 0.05)]
    fired = [e for e, v in R.items() if v > p95]
    tp = [e for e in fired if bad[e]]
    print(f"half-life {hl:2}d:  max R*={vals[0]:7.1f}  p95={p95:6.1f}  "
          f"fired={len(fired):3}  TP={len(tp):2}  PPV={len(tp)/len(fired):5.1%}")
PY
```

!!! danger "`ln(2)`, not `log(2)`"
    In SPL, `log(x)` is **base 10**. Using `log(2)` in place of `ln(2)` gives
    \(\lambda\) too small by a factor of \(\ln(10) \approx 2.303\), which makes the
    half-life about 3.3× longer than you specified. Nothing errors. Your 7-day
    half-life is silently a 23-day one, and every threshold you calibrate against it
    is wrong. In Python `math.log` is natural and `math.log10` is base 10 — the
    opposite convention to SPL, which is exactly how this defect crosses over.

**Step 1 — the empirical \(R^*\) distribution.** Do not summarise it, look at it:

```bash
python3 - <<'PY'
import csv, collections, math
rows = list(csv.DictReader(open('data/truth/risk_truth.csv')))
now = max(float(r['_time']) for r in rows)
lam = math.log(2) / 7
R = collections.defaultdict(float)
for r in rows:
    R[r['entity']] += float(r['risk_score']) * math.exp(-lam * (now - float(r['_time'])) / 86400)
vals = sorted(R.values())
for q in (0.5, 0.75, 0.9, 0.95, 0.99, 1.0):
    print(f"p{q*100:>5.1f}  {vals[min(int(q*len(vals)), len(vals)-1)]:8.1f}")
print(f"\nentities={len(vals)}  mean={sum(vals)/len(vals):.1f}")
PY
```

**Step 2 — choose the threshold from the distribution and a target volume, never a
round number.** Work backwards: if you can absorb 5 risk alerts per day and the
window is 14 days, you want a threshold at the 70th-from-top entity, whatever value
that is. A threshold of "100" chosen because it is round is a threshold chosen by
nobody.

The steady state is worth knowing analytically. For a constant arrival rate \(s\)
of risk per day and decay constant \(\lambda\):

$$
\frac{dR}{dt} = -\lambda R + s \quad\Rightarrow\quad R^{*} = \frac{s}{\lambda} = \frac{s \cdot t_{1/2}}{\ln 2}
$$

So an entity accruing a steady 10 points/day at a 7-day half-life settles at
\(R^{*} = 10 \times 7 / 0.693 \approx 101\). **Any threshold below that alerts on
every steadily-noisy entity forever** — which is how risk queues fill with service
accounts. Compute \(R^*\) for your noisiest benign entity before choosing.

**Step 3 — vary the half-life across {1, 7, 30} days** and record which entities
enter and leave the alerting set. Do not summarise; list them.

At a constant alert volume (top 5% of entities) this dataset gives a blunt result:

```
half-life  1d:  TP = 2   PPV = 12.5%
half-life  7d:  TP = 5   PPV = 31.2%
half-life 30d:  TP = 5   PPV = 31.2%
```

Entities alerting at 30 days but **not** at 1 day include the C2 host and the
exfiltration user — both real. Entities alerting at 1 day but not at 30 are
**all false positives**. On this data the short half-life is simply worse.

That is not a general law and you should not report it as one. It is a
consequence of what these scenarios look like: they accumulate over hours to days
rather than detonating in minutes. Against a smash-and-grab — ransomware
staging, a mass credential dump — the ordering would reverse, and a 30-day
half-life would bury the burst under a fortnight of accumulated background.

**The finding to report is therefore about your estate, not about half-lives:**
the decay constant encodes an assumption about the *timescale of the threat you
are funded to catch*, and this dataset's threats are slow. Running two models in
parallel at 1 and 30 days is a defensible design precisely because it stops the
assumption being implicit.

Notice also **who else** the 30-day model promotes: several service accounts. That
is the \(R^{*}\) arithmetic above arriving in practice — steady accrual plus a
long half-life equals a permanently high score. A slow half-life buys sensitivity
to slow threats and pays for it in standing false positives from anything that is
routinely noisy.

**Step 4 — add the breadth guard and measure it.**

```
... | where R > <threshold> AND n_detections >= 2
```

Measure precision before and after. **In this dataset it may well get worse** —
see [SPL-03 Lab 3](spl-03.md), where breadth-ranking underperformed score-ranking
because the malicious entities were mostly spray victims tripping one detection
repeatedly. Report what you measure, not what the guard is supposed to do.

**Deliverable:** the SPL, the \(R^*\) distribution, a justified (half-life,
threshold) pair with the target volume it was derived from, and the note on which
entities alert at 30 days but not at 1 — and whether that is desirable, which
depends entirely on which threat you are funded to catch.

---

## Lab 4 📄 — Fit Your Weights and Allocate Your Budget

No platform. Standard-library logistic regression — about 40 lines, and writing it
yourself is the point, because the regularisation path is the lesson.

```bash
python3 - <<'PY'
import csv, collections, math, random
random.seed(0)

rows = list(csv.DictReader(open('data/truth/risk_truth.csv')))
detections = sorted({r['search_name'] for r in rows})
idx = {d: i for i, d in enumerate(detections)}

# One row per entity: which detections fired, and the label.
feat = collections.defaultdict(lambda: [0.0] * len(detections))
label = collections.defaultdict(int)
for r in rows:
    feat[r['entity']][idx[r['search_name']]] += 1.0
    if r['scenario'] != 'benign':
        label[r['entity']] = 1
X = [feat[e] for e in feat]
y = [label[e] for e in feat]

def fit(X, y, l1=0.01, lr=0.3, epochs=800):
    """Logistic regression with L1 via proximal (soft-threshold) gradient steps.
    The objective is convex, so the optimum is unique — no restarts needed."""
    w = [0.0] * len(X[0]); b = 0.0
    n = len(X)
    for _ in range(epochs):
        gw = [0.0] * len(w); gb = 0.0
        for xi, yi in zip(X, y):
            z = b + sum(wj * xj for wj, xj in zip(w, xi))
            p = 1 / (1 + math.exp(-max(-30, min(30, z))))
            e = p - yi
            for j, xj in enumerate(xi):
                gw[j] += e * xj
            gb += e
        b -= lr * gb / n
        for j in range(len(w)):
            wj = w[j] - lr * gw[j] / n
            # soft-threshold: this is what drives weights to exactly zero
            w[j] = max(0.0, abs(wj) - lr * l1) * (1 if wj > 0 else -1)
    return w, b

hand = {"Excessive Failed Authentications": 20, "Authentication From New Country": 35,
        "LOLBin Download Behaviour": 60, "Anomalous Parent Child Process": 45,
        "Remote Execution Observed": 55, "High Entropy Domain Lookup": 25,
        "Regular Outbound Callback": 40, "Large Outbound Transfer": 50,
        "Access Outside Peer Group": 30, "Legacy Authentication Protocol": 15}

# The regularisation path: watch features drop out as the penalty rises.
print("l1        zeros  surviving features (strongest first)")
for l1 in (0.05, 0.01, 0.002):
    w, b = fit(X, y, l1=l1)
    alive = [d for d in sorted(detections, key=lambda d: -abs(w[idx[d]])) if w[idx[d]] != 0]
    print(f"{l1:<8} {sum(1 for x in w if x == 0):>4}   {', '.join(alive[:4])}")

w, b = fit(X, y, l1=0.002)
print(f"\n{'detection':34} {'fitted':>8}  {'hand':>5}")
for d in sorted(detections, key=lambda d: -w[idx[d]]):
    print(f"{d:34} {w[idx[d]]:8.3f}  {hand.get(d, 0):5}")
PY
```

**Report PR-AUC and Brier score, and produce a reliability diagram.** Accuracy is
useless at these base rates — a model that says "benign" to everything scores 90%
here — and ROC-AUC is nearly as misleading, because the false-positive axis is
dominated by the enormous benign population. PR-AUC and Brier are the two that
survive class imbalance.

**Read the regularisation path first.** At `l1=0.05` almost everything is zero; at
`l1=0.002` almost nothing is. The order in which features survive as the penalty
falls *is* the ranking, and it is more informative than any single fit — a feature
that survives heavy regularisation is carrying real signal, and one that appears
only at the loosest penalty is probably fitting noise. Choosing a single `l1` by
cross-validation and reporting only that fit throws the interesting part away.

**Compare fitted against hand-assigned.** The comparison is the deliverable, and
what you are looking for is not agreement but **rank inversion**. In this dataset
they are dramatic, and they are **systematic**: the fitted ordering is close to the
*reverse* of the hand ordering at the top end.

| Detection | Hand | Fitted |
|---|---:|---:|
| Excessive Failed Authentications | 20 | **+1.567** |
| Large Outbound Transfer | 50 | +0.296 |
| High Entropy Domain Lookup | 25 | +0.238 |
| Anomalous Parent Child Process | 45 | −0.296 |
| Regular Outbound Callback | 40 | −0.541 |
| Remote Execution Observed | 55 | **−0.844** |
| LOLBin Download Behaviour | 60 | **−0.833** |

The two detections analysts scored highest, 60 and 55, carry the two most
negative weights. The one they scored lowest but one, 20, dominates the fit.

Before you conclude the humans were wrong, work out what a negative weight means
here: given everything else about an entity, seeing this detection fire makes it
*less* likely to be malicious in **this labelled population**. That is a statement
about the population, not about the technique — LOLBin execution genuinely is
dangerous, and it fires overwhelmingly on benign activity in this estate. The fit
has learned the base rate, which is exactly what it was asked to do and exactly
what you must not mistake for a judgement about severity.

**This is the central tension of the lab.** Fitted weights optimise for *what is
usually true*; hand-assigned scores encode *what is occasionally catastrophic*.
A model that has never seen a real LOLBin intrusion will happily score it
negative. Any deployment of fitted weights needs a floor under the techniques you
cannot afford to miss, and choosing that floor is a judgement, not a fit.

**Capacity-constrained allocation.** With a fixed alert budget \(A\), allocate
across detections to maximise true positives. At the optimum, the marginal true
positives per alert is equal across every funded detection:

$$
\frac{dTP_j}{dA_j} = \mu \quad \text{for all funded } j
$$

The practical procedure: compute marginal TP-per-alert per detection, fund
greedily from the top until the budget is exhausted, and note the \(\mu\) at which
you stopped. Detections below \(\mu\) are not "bad" — they are **outbid**, and
saying it that way changes the conversation with their owner.

### The selection-bias statement — required, and usually wrong

Your labels come from dispositions, and dispositions come from alerts analysts
**saw**. So:

- **You have no labels for what never alerted.** The model is fitted on the
  detected population, not the true one, and it will confidently learn that
  behaviour nobody detects is not malicious.
- **Analyst dispositions are noisy and biased.** A busy shift closes more as
  benign. Fatigue is in your labels.
- **The detections generated their own training data.** Any detection that never
  fires contributes no rows and gets a weight of zero — which reads as "useless"
  and may mean "never tested".

**What follows practically:** the fitted weights are valid for *reallocating
attention among detections you already run*. They are **not** evidence that an
unfired detection is worthless, and they cannot tell you what you are missing. Say
that in the deliverable. A model presented without this paragraph will be used to
delete detections it has no information about.

---

## Lab 5 📄 — Entropy Versus a Language Model

Python, no platform. The dataset carries labelled DGA domains in **two families**
— uniform-random labels and dictionary-word concatenations — alongside benign
names that are genuinely high-entropy: CDN object hashes, DKIM selectors, UUID
subdomains and base32 tokens.

That mixture is deliberate. A DGA corpus of nothing but uniform-random labels,
scored against nothing but short pronounceable benign names, is a straw man:
character entropy is the *optimal* detector for exactly that generative process
and will score near-perfectly. The lesson would be an artefact of the test set.

```bash
python3 - <<'PY'
import json, csv, math, collections

truth = {r['event_id']: r['scenario']
         for r in csv.DictReader(open('data/truth/ground_truth.csv'))}
dga, benign = set(), set()
for line in open('data/events/dns.json'):
    e = json.loads(line)
    label = e['query'].split('.')[0]
    (dga if truth.get(e['event_id']) == 'dga_c2' else benign).add(label)
benign -= dga

def entropy(s):
    c = collections.Counter(s)
    return -sum((n/len(s)) * math.log2(n/len(s)) for n in c.values())

def train_bigram(corpus):
    counts = collections.defaultdict(collections.Counter)
    for w in corpus:
        w = "^" + w + "$"
        for a, b in zip(w, w[1:]):
            counts[a][b] += 1
    return counts

def loglik(s, counts, alpha=0.5, V=38):
    """Per-character, so long names are not penalised for being long."""
    w = "^" + s + "$"; total = 0.0
    for a, b in zip(w, w[1:]):
        c = counts[a]
        total += math.log((c[b] + alpha) / (sum(c.values()) + alpha * V))
    return total / (len(w) - 1)

bl = sorted(benign)
train, test = bl[:len(bl)//2], bl[len(bl)//2:]
model = train_bigram(train)

print(f"DGA labels {len(dga)}  benign test {len(test)}")
for name, fn, hi in (("entropy", entropy, True),
                     ("bigram LL", lambda d: loglik(d, model), False)):
    scored = [(fn(d), 1) for d in dga] + [(fn(d), 0) for d in test]
    scored.sort(reverse=hi)
    tp = sum(l for _, l in scored[:50])
    print(f"  {name:10} budget 50/day:  precision={tp/50:6.1%}  recall={tp/len(dga):6.1%}")

wordlist = [d for d in dga if entropy(d) <= 3.2]
print(f"\nDGA families: {len(dga)-len(wordlist)} uniform, {len(wordlist)} wordlist")
print(f"benign labels clearing len>=12 and entropy>3.2: "
      f"{len([d for d in test if len(d) >= 12 and entropy(d) > 3.2])}")
PY
```

```
entropy    budget 50/day:  precision  44.0%  recall  30.1%
bigram LL  budget 50/day:  precision   2.0%  recall   1.4%
```

**Both are poor.** Entropy is mediocre and the bigram model is worse than
useless. Diagnose each before reading on — the diagnosis is the deliverable.

### Why entropy is mediocre here

It has failures in both directions, and both are real:

- **False positives.** Base32 tokens over a 32-symbol alphabet, 20–28 characters
  long, have *higher* character entropy than a 12–22 character lowercase DGA
  label. They sit above the malicious domains in the ranking and cannot be
  thresholded away, because there is no cut-point with the DGA above them.
- **False negatives.** Roughly a third of the DGA labels are dictionary
  concatenations — `copperhorse`, `cottonstoneriver`. Low character entropy,
  entirely malicious, invisible to this detector at any threshold.

Note that the first failure is partly about **alphabet size and length**, not
randomness. Entropy over a longer string drawn from a larger alphabet is higher
almost mechanically. A detector that appears to work by measuring randomness may
be measuring length; control for it and watch the ranking move.

### Why the bigram model is worse

It was trained on the benign corpus, which contains those same hex and base32
tokens — so it has *learned* that improbable-looking character sequences are
normal here. And dictionary DGAs are made of English words, which are maximally
probable under a model trained on English-ish labels. It fails on both families
for opposite reasons.

The fix is not a better threshold. It is a higher-order model (trigrams with
backoff), a training corpus that excludes machine-generated names, or scoring
against a general English model rather than the local one. **Try one and report
the result** — this is where the lab wants an experiment, not an opinion.

### The move that actually works

Neither scorer is going to be rescued by tuning. Change the **unit of detection**
instead — from the domain to the host:

```bash
python3 - <<'PY'
import json, math, collections

rows = []
for line in open('data/events/dns.json'):
    e = json.loads(line)
    rows.append((e['src_host'], e['query'].split('.')[0]))

def entropy(s):
    c = collections.Counter(s)
    return -sum((n/len(s)) * math.log2(n/len(s)) for n in c.values())

per_host = collections.defaultdict(lambda: [0, 0])
for host, label in rows:
    per_host[host][1] += 1
    if len(label) >= 12 and entropy(label) > 3.2:
        per_host[host][0] += 1

print(f"{'host':18}{'high-entropy':>13}{'lookups':>9}")
for host, (hits, total) in sorted(per_host.items(), key=lambda kv: -kv[1][0])[:6]:
    print(f"{host:18}{hits:13}{total:9}")
PY
```

```
host                 high-entropy  lookups
WS-FIN-0013                    54      112     <-- the C2 host
SRV-SER-031                     4      173
WS-OPE-0161                     4       91
WS-ENG-0189                     4       59
```

**54 against 4.** The same entropy function that manages 44% precision per
domain is decisive per host, because benign high-entropy names are *spread
thinly* — a hash here, a DKIM selector there — while a beaconing host generates
them in a concentrated burst.

**This is the transferable result, and it is worth more than either scorer.**
A weak signal aggregated over the right entity beats a strong signal evaluated
on the wrong one. Before reaching for a better model, ask whether you are
scoring the right thing: the domain is what carries the property, but the host
is what you would act on, and it is also where the evidence accumulates.

It also explains why [SPL-03 Lab 7](spl-03.md) works at all. That lab ranks
hosts, not domains, which is why a mediocre per-domain scorer still lands on the
right machine.

**Deliverable:** both implementations, the PR curves, the measured precision of
each at a fixed budget of 50/day, the per-host comparison, and the diagnosis in
your own words — including at least one experiment testing one of the
explanations above (control for length, retrain the n-gram on a filtered corpus,
or raise the model order). Reporting the numbers and repeating the textbook claim
that n-grams beat entropy has not done the lab.

---

## Lab 6 📄 — Peer Groups and the Authentication Graph

Python, no platform. Standard library throughout; the linear algebra is small
enough to write by hand and clearer for it.

```bash
python3 - <<'PY'
import json, csv, collections, math

# user x resource matrix from Type 3 authentication
M = collections.defaultdict(collections.Counter)
for line in open('data/events/wineventlog.json'):
    e = json.loads(line)
    if e.get('EventCode') == 4624 and e.get('Logon_Type') == '3':
        M[e['user']][e['dest']] += 1
users = [u for u in M if len(M[u]) >= 2]
print(f"{len(users)} users with 2+ distinct resources")

def cosine(a, b):
    keys = set(a) | set(b)
    num = sum(a[k] * b[k] for k in keys)
    da = math.sqrt(sum(v*v for v in a.values()))
    db = math.sqrt(sum(v*v for v in b.values()))
    return num / (da * db) if da and db else 0.0

ids = {r['identity']: r for r in csv.DictReader(open('data/lookups/oscd_identities.csv'))}

# distance from the org-chart peer-group centroid
by_dept = collections.defaultdict(list)
for u in users:
    d = ids.get(u, {}).get('bunit', '?')
    by_dept[d].append(u)

out = []
for dept, members in by_dept.items():
    if len(members) < 3:
        continue
    centroid = collections.Counter()
    for u in members:
        for k, v in M[u].items():
            centroid[k] += v
    for u in members:
        out.append((cosine(M[u], centroid), u, dept, len(M[u])))
out.sort()
print("\nleast like their own department:")
for sim, u, dept, n in out[:8]:
    print(f"  {u:16} {dept:12} resources={n:3}  cos={sim:.3f}")
PY
```

!!! warning "Check the resource count before you believe the similarity"
    Run the block and look at the `resources=` column. The lowest cosine scores
    belong overwhelmingly to users with **two** resources. That is not a
    behavioural finding, it is arithmetic: a two-element vector compared against a
    department centroid built from dozens of resources will score low almost
    regardless of behaviour.

    Raise the floor to `len(M[u]) >= 4` and re-run. The list changes completely.
    **Report both**, and state which you would put in front of an analyst — a
    similarity score computed over a sparse vector is a measurement of sparsity
    wearing the costume of a measurement of behaviour, and shipping it produces a
    detection that alerts on people who do very little.

**Where behavioural and organisational grouping disagree, decide which is right.**
The module asks for at least one case and an assessment, and both answers occur:

- **The org chart is right, the behaviour is wrong.** A finance user whose
  behaviour clusters with IT is doing something they should not, or has been
  handed access nobody reviewed.
- **The behaviour is right, the org chart is wrong.** A "finance" analyst who has
  in practice been the reporting engineer for a year. The org chart is stale, which
  is [SPL-04 Lab 2](spl-04.md)'s identity-staleness problem showing up as a
  false positive here.

You cannot tell which from the data. That is worth stating plainly: **behavioural
peer grouping generates questions for a human, not answers**, and a system that
alerts on peer-group deviation without a human to resolve the ambiguity produces
one uninterpretable alert per stale HR record.

**The graph half.** Build the authentication graph, form the Laplacian
\(L = D - A\), and partition on the sign of the Fiedler vector (the eigenvector of
the second-smallest eigenvalue). Power iteration on a deflated matrix is enough;
the graph here is a few hundred nodes.

The expected partition is **workstations from servers** — the natural community
structure of an enterprise. Then look for **community-crossing edges without
precedent**: the lateral-movement chain in this dataset is exactly that, and the
individual edges are unremarkable. It is the crossing that is anomalous, which is
the whole argument for spectral methods over per-event rules.

**The heat kernel.** Seed \(u_0\) at a compromised host and diffuse:

$$
u(t) = e^{-Lt}u_0 \approx \left(I - \tfrac{Lt}{k}\right)^{k} u_0
$$

Rank hosts by \(u(t)\) to get an investigation order. **Justify your \(t\)**: small
\(t\) stays local (immediate neighbours, high precision, misses the chain), large
\(t\) approaches the stationary distribution and just ranks by degree — which tells
you the domain controller is important, which you knew. The useful range is where
the ranking still depends on the seed, and you find it by checking that it does.

---

## Lab 7 📄 — A Density Model That an Analyst Can Read

The module lists AITK or DSDL for `DensityFunction`. Neither is available without a
licensed instance, **and the lab survives intact without them**, because the graded
part is not the model.

**Fit the density baseline in Python.** Per-user, log-normal on egress, which is
what the data actually is:

```bash
python3 - <<'PY'
import json, collections, math, statistics

daily = collections.defaultdict(float)
for line in open('data/events/proxy.json'):
    e = json.loads(line)
    day = int(e['_time'] // 86400)
    daily[(e['user'], day)] += e['bytes_out']

by_user = collections.defaultdict(list)
for (u, d), v in daily.items():
    by_user[u].append(v)

flagged = []
for u, vals in by_user.items():
    if len(vals) < 7:
        continue
    logs = [math.log(v + 1) for v in vals]
    mu, sd = statistics.median(logs), statistics.stdev(logs)
    if sd == 0:
        continue
    for v in vals:
        z = (math.log(v + 1) - mu) / sd
        if z > 3:
            flagged.append((z, u, v))
flagged.sort(reverse=True)
for z, u, v in flagged[:5]:
    print(f"{u:18} {v/1e6:8.1f} MB  z={z:5.2f}")
PY
```

**Note the median, not the mean.** The insider is active across the whole baseline
window — `verify.py data` asserts it — so a mean-based baseline is inflated by the
very behaviour it is meant to detect. This is contamination, and robust estimators
are the response.

Note also what the z-score does here. The flagged day is roughly 117,000× the
user's median, and its z-score is **3.20** — barely over a conventional threshold.
That is the log transform doing its job on a heavy-tailed quantity, and it is why
you must not report the z-score to the analyst. Report the ratio and the bytes;
keep the z-score for ranking.

!!! danger "A scale-free statistic needs a materiality floor"
    Rank the flagged days by z-score alone and the top result is a user whose
    normal day is 2 kB and who once sent 100 kB. Their z-score is **8.5**. The
    person exfiltrating 2.5 GB scores **3.2** and ranks below them.

    The statistic is not wrong — that user really did deviate from their own
    baseline by more. It is *immaterial*, and the modified z-score has no way to
    know that, because it deliberately discarded the scale.

    Pair it with a floor drawn from the estate's own distribution rather than a
    round number:

    ```python
    everything = sorted(v for vals in by_user.values() for v in vals)
    floor = everything[int(0.99 * len(everything))]      # ~2.9 MB here
    ...
    if z > 3.5 and v > floor:
        flagged.append((z, user))
    ```

    With the floor, the taught method returns exactly one user, and it is the
    right one. Without it, it returns statistically remarkable trivia ranked
    above a genuine exfiltration. **Any anomaly detector on a scale-free
    statistic needs this**, and its absence is one of the most common reasons an
    otherwise sound model produces an unusable queue.

### The part that is actually graded

**Write the explanation an analyst would see, for five flagged events. Then have a
peer who did not build the model attempt triage using only that explanation.**

Not actionable:

> *Anomaly detected. Score: 0.97. Model: DensityFunction over bytes_out.*

Actionable:

> *`yusuf.lee` uploaded **2.49 GB** to `upload4.filetransfer-top` in a single
> day. His normal daily upload is **21 kB** (median over 12 days); his Finance
> colleagues sit at **28 kB** (median of 30 peers). This day is roughly
> **117,000× his own baseline**.*
>
> *`upload4.filetransfer-top` has been contacted by **no other user** in the
> estate, ever.*
>
> *To confirm or dismiss: check whether a sanctioned file-transfer service is in
> use by this team, and whether a data migration or release was scheduled that
> day. If neither, this is 2.5 GB leaving the business to a destination nobody
> else uses.*

The difference is not verbosity. The second gives a **comparison** (his own
baseline *and* his peers'), a **magnitude in units a person holds** (GB, not
z-scores), a **novelty signal** (a destination with no other users), and a
**disconfirming check** — the specific thing that would make this benign. An
explanation that only supports the alert cannot be triaged; it can only be
believed or ignored.

**"Any explanation your peer could not act on is a model defect, not an analyst
deficiency."** The module is right and it is the sentence to take away. If your
peer needed to ask what the score meant, the score should not have been shown. Say
what you would change.

---

## Lab 8 ✅ — Make an Analytic Search Fast

The only lab here wanting a Splunk instance, for the job inspector. **Without one**,
do it as a written optimisation exercise: the six versions, the cascade stage each
change acts on, and the predicted effect with its reasoning. That is the graded
content — the module requires attributing every speedup to a stage, and an
unattributable speedup does not count.

**Version 0 — deliberately bad.** Every mistake at once:

```
index=* | search *evil* | eval d=strftime(_time,"%Y-%m-%d")
| join user [ search index=* | stats count by user ]
| stats count by d, user | where count > 5
```

**The six versions and the stage each acts on:**

| # | Change | Cascade stage | Why it works |
|---|---|---|---|
| 1 | Tighten time range; add `index=`/`sourcetype=` | **Bucket selection** | Fewer buckets opened. The largest single win, almost always |
| 2 | `TERM(evil)`, drop the leading `*` | **Index lookup** | A leading wildcard defeats the lexicon; the term becomes a full scan |
| 3 | Move filters before the first barrier | **Event retrieval** | Filtering before `stats`/`join` means fewer events cross the barrier |
| 4 | Replace `join` with `stats` | **Distribution** | `join` runs a subsearch on the search head with a silent 50k-row cap; `stats` distributes to the peers |
| 5 | Replace centralised-streaming with distributable | **Distribution** | Work executes on peers in parallel rather than serially on one search head |
| 6 | `tstats` against an accelerated model | **Summarisation** | Reads pre-computed summaries; never touches raw events |

**The subsearch cap in version 4 is worth dwelling on**, because it is a
correctness bug and not a performance one: a subsearch silently truncates at
`maxout` (50,000 by default) and returns a **confidently wrong answer with no
error**. [SPL-02 Lab 6](spl-02.md) demonstrates it against this dataset. Anyone
optimising `join` → `stats` for speed and not noticing they also fixed a
correctness defect has missed the more important half.

**The table is the deliverable:**

| Version | Events scanned | Wall time | Stage attributed |
|---|---|---|---|
| 0 | | | — |
| 1 | | | Bucket selection |
| 2 | | | Index lookup |
| 3 | | | Event retrieval |
| 4 | | | Distribution (+ correctness) |
| 5 | | | Distribution |
| 6 | | | Summarisation |

**Without an instance**, fill in predicted orders of magnitude and defend each.
Predicting that step 1 buys 100× and step 5 buys 2× — and being able to say why —
is the understanding being assessed. The measured numbers only confirm it.
