"""Write a dataset to disk in Splunk-ingestable form.

**Assessment integrity.** Ground-truth labels are stripped from the events that
Splunk ingests and written to a separate file keyed by ``event_id``. Without
this a learner could solve every detection lab with
``index=* _truth_scenario=*``, which would defeat the entire point. Instructors
(and the verification harness) join on ``event_id``; learners are not given the
truth file unless the exercise calls for it.
"""
from __future__ import annotations

import csv
import json
import os
from collections import defaultdict

TRUTH_KEYS = ("_truth_scenario", "_truth_technique", "_truth_note")

# JSON keys that collide with Splunk metadata. With INDEXED_EXTRACTIONS = json a
# payload key named `sourcetype` is extracted as an indexed field and shadows the
# sourcetype assigned in inputs.conf, so `sourcetype=oscd:proxy` silently returns
# nothing while the events sit there in plain sight. `index`, `source` and `host`
# behave the same way. The generator uses these internally for routing; they are
# dropped on the way out, because metadata belongs in metadata.
METADATA_KEYS = ("index", "sourcetype", "source", "host")


def _strip_metadata(row):
    return {k: v for k, v in row.items() if k not in METADATA_KEYS}


def _split_truth(events, include_truth=False):
    """Assign stable ids; return (ingestable_events, truth_rows)."""
    clean, truth = [], []
    for n, e in enumerate(events):
        eid = f"e{n:08d}"
        row = dict(e)
        row["event_id"] = eid
        scenario = row.get("_truth_scenario")
        if scenario:
            truth.append({
                "event_id": eid,
                "_time": row["_time"],
                "scenario": scenario,
                "technique": row.get("_truth_technique", "-"),
                "note": row.get("_truth_note", ""),
                "index": row.get("index", "-"),
                "user": row.get("user", "-"),
                "dest": row.get("dest", row.get("src_host", "-")),
            })
        if not include_truth:
            for k in TRUTH_KEYS:
                row.pop(k, None)
        clean.append(row)
    return clean, truth


def write(dataset, findings, outdir, include_truth=False):
    events, truth = _split_truth(dataset["events"], include_truth)

    ev_dir = os.path.join(outdir, "events")
    lk_dir = os.path.join(outdir, "lookups")
    tr_dir = os.path.join(outdir, "truth")
    for d in (ev_dir, lk_dir, tr_dir):
        os.makedirs(d, exist_ok=True)

    by_index = defaultdict(list)
    for e in events:
        by_index[e.get("index", "main")].append(e)

    written = {}
    for index, rows in by_index.items():
        path = os.path.join(ev_dir, f"{index}.json")
        with open(path, "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(_strip_metadata(r), separators=(",", ":")) + "\n")
        written[index] = len(rows)

    # Risk index: findings keep their truth column only in the truth file.
    rpath = os.path.join(ev_dir, "risk.json")
    with open(rpath, "w", encoding="utf-8") as fh:
        for f in findings:
            r = _strip_metadata({k: v for k, v in f.items()
                                 if not k.startswith("_truth")})
            fh.write(json.dumps(r, separators=(",", ":")) + "\n")
    written["risk"] = len(findings)

    _csv(os.path.join(lk_dir, "oscd_assets.csv"),
         [_asset_row(a) for a in dataset["org"].assets])
    _csv(os.path.join(lk_dir, "oscd_identities.csv"),
         [_identity_row(i) for i in dataset["org"].identities])

    _csv(os.path.join(tr_dir, "ground_truth.csv"), truth)
    _csv(os.path.join(tr_dir, "risk_truth.csv"),
         [{"_time": f["_time"], "entity": f["entity"],
           "search_name": f["search_name"], "risk_score": f["risk_score"],
           "scenario": f["_truth_scenario"], "technique": f["_truth_technique"]}
          for f in findings])

    with open(os.path.join(outdir, "summary.json"), "w", encoding="utf-8") as fh:
        from .build import summarise
        s = summarise(dataset, findings)
        s["injected"] = dataset["injected"]
        s["files"] = written
        s["truth_included_in_events"] = include_truth
        json.dump(s, fh, indent=2)
    return written


def _asset_row(a):
    return {"host": a.host, "ip": a.ip, "nt_host": a.host, "role": a.role,
            "bunit": a.department, "priority": a.priority,
            "category": "crown_jewel" if a.is_crown_jewel else a.role}


def _identity_row(i):
    return {"identity": i.user, "prefix": "", "nick": i.user,
            "first": i.full_name.split()[0], "last": i.full_name.split()[-1],
            "suffix": "", "email": f"{i.user}@example.com.au",
            "phone": "", "phone2": "", "managedBy": "", "priority": i.priority,
            "bunit": i.department, "category": i.category,
            "watchlist": "true" if i.privileged else "false",
            "work_city": i.home_city, "work_lat": f"{i.home_lat}",
            "work_long": f"{i.home_long}"}


def _csv(path, rows):
    if not rows:
        open(path, "w").close()
        return
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
