# Data model

Six indexes, CIM-aligned field names, JSON with `INDEXED_EXTRACTIONS`.

## Indexes and sourcetypes

| Index | Sourcetype | CIM model | Key fields |
|---|---|---|---|
| `wineventlog` | `oscd:winauth` | Authentication | `EventCode` (4624/4625), `action`, `user`, `src`, `dest`, `Logon_Type`, `Failure_Reason` |
| `sysmon` | `oscd:sysmon` | Endpoint / Processes | `EventCode` (1), `process_name`, `parent_process_name`, `process`, `user`, `dest` |
| `proxy` | `oscd:proxy` | Web | `user`, `src`, `dest`, `url`, `http_method`, `status`, `category`, `bytes_out`, `bytes_in` |
| `dns` | `oscd:dns` | Network Resolution | `src`, `query`, `query_type`, `answer`, `reply_code` |
| `cloud` | `oscd:cloud` | Authentication | `user`, `action`, `src_country`, `src_city`, `src_lat`, `src_long`, `authentication_method`, `mfa_result` |
| `risk` | `oscd:risk` | — (ES risk index) | `entity`, `entity_type`, `risk_score`, `risk_message`, `search_name` |

The `risk` index uses **ES 8 field names** (`entity`, `entity_type`). Pre-ES 8
deployments use `risk_object` / `risk_object_type` — see the terminology table in
[SPL-09](../../docs/modules/splunk/spl-09-detection-analytics.md).

## Lookups

`oscd_assets.csv` and `oscd_identities.csv` are written in ES Asset & Identity
framework shape (`priority`, `bunit`, `category`, `watchlist`), so the enrichment
labs mirror the real framework rather than a toy.

```
| inputlookup oscd_assets.csv | head 5
| inputlookup oscd_identities.csv | search watchlist=true
```

## Deliberate statistical properties

Each is asserted by `harness/verify.py data`. They exist because specific labs
would be hollow without them.

| Property | Observed (seed 1337, 14 days) | Which lab needs it |
|---|---|---|
| Egress heavy-tailed | mean/median ≈ 19× | SPL-09 Lab 3, SPL-02 Lab 7 — a 3-sigma rule fails here |
| Daily seasonality | peak/trough ≈ 11× | SPL-09 Topic 7 deseasonalisation |
| Weekly seasonality | weekday/weekend ≈ 3.6× | as above |
| Counts overdispersed | var > mean (negative binomial) | SPL-09 Topic 9 — Poisson thresholds over-alert |
| Beacon regularity | CV ≈ 0.05 **on the isolated channel** | SPL-03 Lab 7, SPL-09 Topic 9 |
| DGA separability | entropy 3.4 vs 2.4 **in the mean only** | SPL-09 Lab 5 |
| Contaminated baseline | insider active across the full window | SPL-09 Topic 8 — why robust estimators win |
| Per-user activity | log-normal multiplier | SPL-02 Lab 7 — global thresholds are wrong |

!!! important "The DGA corpus has two families, and the benign corpus fights back"
    `dga_domain()` emits **uniform-random** labels (~70%) and **dictionary-word
    concatenations** (~30%). The second family has *low* character entropy and is
    invisible to an entropy threshold at any cut-point.

    Benign traffic carries genuinely high-entropy names too — CDN object hashes,
    DKIM selectors, UUID subdomains, base32 tokens — at about 1.5% of benign
    domain draws. Some have *higher* entropy than the DGA, because they are
    longer and drawn from a larger alphabet.

    Both are deliberate. Without them, entropy scores near-perfectly and SPL-09
    Lab 5 teaches an artefact of the test set rather than anything about
    detection. With them, per-domain entropy manages about 44% precision at a
    fixed budget, and the lab's real lesson — that aggregating the same weak
    signal **per host** is decisive where per-domain scoring is not — becomes
    visible.

!!! important "Beaconing is only regular once you isolate the channel"
    The beacon host also browses normally. Measured across all its DNS traffic
    the inter-arrival CV is ~3.0; filtered to the DGA channel it is ~0.05.

    That is not a defect, it is the lesson: **isolate the candidate channel,
    then measure regularity**. A learner who computes CV over a host's entire
    traffic will find nothing and conclude the technique does not work.

!!! note "Why the events carry no `index` or `sourcetype` field"
    The generator routes internally on those names but strips them before writing.
    With `INDEXED_EXTRACTIONS = json`, a payload key called `sourcetype` is
    extracted as an indexed field and **shadows the sourcetype assigned in
    `inputs.conf`** — so `sourcetype=oscd:proxy` returns nothing while the events
    sit in the index in plain sight, with no error anywhere. `index`, `source` and
    `host` collide the same way.

    Metadata belongs in metadata. This is a real defect people ship, and it is
    worth recognising the symptom: a search that returns zero on a sourcetype the
    UI's sourcetype picker is happy to offer you.

## Attack scenarios

| Scenario | ATT&CK | Signal |
|---|---|---|
| `password_spray` | T1110.003 | One source IP, ~45 accounts, 1–3 attempts each, one success |
| `impossible_travel` | T1078.004 | AU sign-in then RU/NG within ~40 min, legacy auth |
| `lolbin_download` | T1105 | `certutil` as downloader; `certutil` → `rundll32` parentage |
| `lateral_movement` | T1021.002 | Workstation → jump host → server → DC, with remote exec |
| `dga_c2` | T1568.002 | High-entropy domains, mostly NXDomain |
| `beacon_c2` | T1071.001 | ~300s callbacks, 8% jitter, small symmetric payloads |
| `exfil_volume` | T1041 | ~2.4 GB in 9–18 chunks to an uncategorised destination |
| `insider_collection` | T1005 | Low-and-slow out-of-peer-group access + large uploads, full window |

ATT&CK IDs are stated against **v19** for consistency with the repository and
are provisional pending Framework Custodian verification.

Benign LOLBin use is injected at ~1.2% of process events **on purpose**, so
"any `certutil` is malicious" scores badly. The signal is context — parentage,
command line, what followed — not the binary.
