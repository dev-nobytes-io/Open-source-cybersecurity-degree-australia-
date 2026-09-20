# Ground truth and assessment integrity

## How labels are stored

Every generated event gets a stable `event_id`. Events belonging to an attack
scenario are additionally labelled with the scenario, ATT&CK technique and a
short note. Derived firewall and IDS events inherit the label of the traffic
they were derived from, so a scenario is labelled consistently across all of
its views.

**By default those labels are stripped before the events are written for
ingestion**, and go to `data/truth/` instead:

```
data/events/*.json          <- ingested by Splunk. NO labels.
data/truth/ground_truth.csv <- event_id, scenario, technique, note, user, dest
data/truth/risk_truth.csv   <- per intermediate finding
data/summary.json           <- counts, base rates, and the injected entities
```

Without this split, every detection lab is solvable with
`index=* _truth_scenario=*`. `harness/verify.py integrity` asserts the split held.

## For instructors

```bash
python3 generator/generate.py --with-truth --out ./data-instructor
```

Leaves labels inline for building worked solutions. **Never point a learner's
Splunk at that directory**, and note that `summary.json` names the compromised
accounts and hosts outright — it is an answer key.

## Scoring a lab

Join a learner's findings back to truth on `event_id`, or use the self-check:

```bash
python3 harness/verify.py answer spl03.lab7.beacon_host WS-ENG-0042
python3 harness/verify.py answer spl09.lab3.insider_user alice.nguyen
```

Known keys: `spl03.lab2.spray_victim`, `spl03.lab5.travel_user`,
`spl03.lab7.beacon_host`, `spl09.lab3.insider_user`, `spl09.lab5.exfil_user`.

## Computing a real PPV

This is what ground truth buys you, and it is the exercise the whole of
[SPL-09](../../docs/modules/splunk/spl-09-detection-analytics.md) Part B rests on.
Write your detection, export its results, then:

```python
import csv, json
truth = {r["event_id"]: r["scenario"]
         for r in csv.DictReader(open("data/truth/ground_truth.csv"))}
hits = [json.loads(l)["event_id"] for l in open("my_detection_results.json")]

tp = sum(1 for h in hits if h in truth)
fp = len(hits) - tp
total_malicious = len(truth)

print("alerts   ", len(hits))
print("PPV      ", tp / len(hits) if hits else 0)      # precision
print("recall   ", tp / total_malicious)
```

Report **PPV and recall**, never accuracy — at these base rates a detector that
never fires is 99.8% accurate.

## Honest limits

- The base rate is **enriched** so labs are tractable. Real rates are far lower.
- Scenarios are **single-variant**: one spray, one beacon interval, one exfil
  pattern. A detector tuned to this dataset is tuned to *this* dataset, and
  generalisation is not demonstrated by passing here.
- Benign traffic is generated from a model, so it lacks the messy long tail of
  real estates — real false positives come from places a generator does not
  think of. Treat measured false-positive rates as a floor, not an estimate.
