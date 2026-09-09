# Conf-file practice

**Nine exercises with marking keys.** No Splunk instance, no dataset — a text
editor and the reasoning. Each gives you a stanza that is *plausible and wrong*,
which is the only kind that ships: a stanza that fails to parse gets caught.

Work each one before opening its key. The keys are collapsed; the value is in
being wrong first.

**How these are marked.** Finding the defect is worth little on its own — the
graded content is *what the symptom would look like in production*, because that
is what you will actually be handed. A correct fix with no symptom stated scores
about half.

Related labs: [SPL-06](../guides/spl-06.md) Labs 1, 2, 6 and 7 ·
[SPL-08](../guides/spl-08.md) Lab 2 · [SPL-04](../guides/spl-04.md) Lab 2.

---

## 1. Retention that isn't

```conf
[sec_high]
homePath   = $SPLUNK_DB/sec_high/db
coldPath   = $SPLUNK_DB/sec_high/colddb
thawedPath = $SPLUNK_DB/sec_high/thaweddb
frozenTimePeriodInSecs = 220752000
maxTotalDataSizeMB = 500000
```

The obligation is **seven years** of searchable security telemetry. Ingest into
this index is 280 GB/day. State the defect, the symptom, and the fix.

??? success "Marking key"
    **Defect.** Buckets roll to frozen when **either** limit is reached, whichever
    comes first. `maxTotalDataSizeMB = 500000` is 500 GB on disk.

    **The arithmetic that matters.** At a 0.5× on-disk ratio (rawdata ≈ 0.15,
    tsidx ≈ 0.35), 280 GB/day of ingest is 140 GB/day on disk. The cap therefore
    holds **3.6 days**. Seven years needs roughly **358 TB** per copy. The setting
    is short by a factor of about 700.

    **Symptom.** Nothing errors. Search returns results, the dashboards look
    healthy, and data silently ages out after three or four days. You discover it
    during an investigation that needs last month, or during an audit.

    **Fix.** Set `maxTotalDataSizeMB` from the retention arithmetic, not from a
    default, and add `maxVolumeDataSizeMB` on the volume so the cap is enforced
    where the disk actually is. Then **monitor it**, because a correct number
    today is wrong after 25% annual growth:

    ```
    | dbinspect index=sec_high
    | stats min(startEpoch) as oldest by index
    | eval retained_days = round((now()-oldest)/86400, 1)
    | where retained_days < 2555
    ```

    **Full marks** require noticing that the *direction* of this failure is the
    dangerous one: it fails towards non-compliance, quietly.

---

## 2. Australian dates

```conf
[vendor:app]
SHOULD_LINEMERGE = true
TIME_FORMAT = %m/%d/%Y %H:%M:%S
```

The source emits `12/03/2026 09:14:22`, generated in Melbourne. Two defects.

??? success "Marking key"
    **Defect 1 — date order.** `%m/%d/%Y` reads `12/03/2026` as **12 March**. The
    source means **3 December**.

    **Why this is worse than a uniform failure.** Days 13–31 have no valid month
    interpretation, so they parse correctly. Days 1–12 silently land in the wrong
    month. Any spot check on a date after the 12th passes. You get a dataset that
    is right about two-thirds of the time, which is much harder to notice than one
    that is wrong all the time.

    **Defect 2 — no timezone.** With no `TZ`, Splunk applies the forwarder's or
    the indexer's timezone. A Melbourne source forwarded through a Sydney indexer
    is fine in winter and an hour out whenever the two differ; a source in
    Brisbane against a Sydney indexer is an hour out for half the year. Every
    cross-source correlation silently misses.

    **Also wrong.** `SHOULD_LINEMERGE = true` makes Splunk guess record
    boundaries. It is slow, and it is wrong the first time a message contains a
    newline.

    **Fix.**
    ```conf
    [vendor:app]
    SHOULD_LINEMERGE = false
    LINE_BREAKER = ([\r\n]+)
    TIME_FORMAT = %d/%m/%Y %H:%M:%S
    TZ = Australia/Melbourne
    MAX_TIMESTAMP_LOOKAHEAD = 20
    ```

    **Detection.** Skew between parse time and index time finds both:
    ```
    index=* sourcetype=vendor:app
    | eval skew_h = round((_indextime - _time)/3600, 1)
    | stats count by skew_h | sort - count
    ```
    A healthy source has one skew bucket.

---

## 3. Metadata in the payload

```conf
[oscd:proxy]
INDEXED_EXTRACTIONS = json
KV_MODE = none
TIMESTAMP_FIELDS = _time
```

```json
{"_time":1755475221.7,"sourcetype":"proxy:squid","index":"proxy","user":"olive.brown"}
```

`sourcetype=oscd:proxy` returns nothing. `index=proxy` returns thousands. Explain.

??? success "Marking key"
    **Defect.** The JSON payload contains keys named `sourcetype` and `index`.
    Under `INDEXED_EXTRACTIONS = json` these are extracted as indexed fields and
    **shadow the metadata assigned in `inputs.conf`**. `host` and `source` collide
    the same way.

    **Symptom.** Uniquely nasty: the sourcetype picker in Splunk Web offers you
    `oscd:proxy`, because the input assigned it — and searching for it returns
    nothing, with no error, while the events sit in the index in plain sight.
    Every macro, eventtype, tag and CIM mapping keyed on that sourcetype is dead.

    **Fix, in order of preference.**
    1. **Stop emitting the collision.** Metadata belongs in metadata; the payload
       does not need to restate what the input already assigns. This is what the
       lab generator does.
    2. If you cannot change the source, rename on ingest:
       ```conf
       [rename_payload_sourcetype]
       SOURCE_KEY = field:sourcetype
       REGEX = (.+)
       FORMAT = payload_sourcetype::$1
       WRITE_META = true
       ```
    3. Do **not** "fix" it by changing every search to use the payload value.
       That works until someone writes a search the normal way.

---

## 4. Masking that does not mask

```conf
# On the universal forwarder, in etc/system/local/props.conf
[app:logs]
SEDCMD-strip = s/(AKIA[A-Z0-9]{16})/REDACTED/g
```

The intent is to stop AWS keys leaving the host. Assess.

??? success "Marking key"
    **Defect.** A universal forwarder does **not parse**. `SEDCMD` is applied at
    the parsing stage, which happens on an indexer or a heavy forwarder. On a UF
    this stanza does nothing at all.

    **Symptom.** No error, no warning, and — worst of all — the setting is present
    in the config, so a reviewer reading `btool` output concludes masking is in
    place. The keys are indexed in full.

    **Fix.** Put the `SEDCMD` where parsing occurs: on the indexers, or on a heavy
    forwarder between the UF and the indexers.

    **The harder point, and the one worth full marks.** Even placed correctly,
    `SEDCMD` is the wrong control for the stated intent. The intent was *stop the
    key leaving the host*; by the time an indexer masks it, the key has crossed
    the network and is in the indexer's memory. `SEDCMD` protects the index, not
    the host. If the requirement is really the host, the control belongs at the
    source — stop the application logging the key.

    **Verification.** A search returning zero is **not** proof of masking; a
    field alias or a `fields` command could be hiding it. Grep the buckets:
    ```bash
    grep -r "AKIA" /opt/splunk/var/lib/splunk/ | head
    ```
    Anything on disk means the secret is in your index, your backups, and your
    seven-year retention — and `SEDCMD` cannot retroactively remove it.

---

## 5. A whitelist that is not one

```conf
# deployment-apps/web_inputs/local/inputs.conf
[monitor:///var/log]
index = sec_high
recursive = true
whitelist = .*
disabled = false
```

Pushed to a server class matching `uf-web-*`. What happens?

??? success "Marking key"
    **Defect.** `whitelist = .*` matches everything. This monitors the entire
    `/var/log` tree, recursively, into a seven-year-retention index — including
    Splunk's own logs, creating a feedback loop.

    **Symptom.** It parses cleanly and pushes successfully. Ingest volume on
    `sec_high` climbs, the licence warning appears the following day, and the
    seven-year index now contains operating-system noise you are obliged to keep.

    **Fix.** A positive whitelist naming what you want:
    ```conf
    [monitor:///var/log/nginx/access.log]
    index = web
    sourcetype = nginx:access
    disabled = false
    ```

    **The blast-radius half, which is the graded part.** The deployment server has
    no `--check`, no `--limit` and no dry run. So:

    - **What limits it:** a staged server class — one canary host, promoted to the
      full class after a soak period. `restartSplunkd = false` where the change
      does not require a restart, so a bad push does not also take the forwarder
      down.
    - **How you detect it:** ingest volume per index, watched. If your honest
      answer is "the licence warning next week", say so — that is the finding.
    - **Recovery order:** remove the app from the *server class* (do not delete
      the app — clients need something to converge onto), reload the deploy
      server, confirm each client's app list shrank, then deal with the polluted
      index. Note that `| delete` only hides data from search; the disk cost and
      the retention obligation both remain.

---

## 6. Precedence

```conf
# etc/apps/my_ta/local/props.conf
[vendor:app]
TRUNCATE = 50000

# etc/system/local/props.conf
[vendor:app]
TRUNCATE = 1000
```

Which wins? What is the symptom? And what would change your answer?

??? success "Marking key"
    **Winner.** `system/local` — so `TRUNCATE = 1000`. For global-context files
    the order is `system/local` → `apps/*/local` → `apps/*/default` →
    `system/default`.

    **Symptom.** Events over 1000 bytes are truncated at index time. The event is
    present, so counts are right; the tail is gone, so any field extracted from
    the end of a long line silently returns null. Detections keyed on those fields
    return zero without erroring.

    **What would change the answer.** The ordering is **not universal**. In
    app/user scope — `savedsearches.conf`, `macros.conf`, views — it is
    user → app **in ASCII order of app name** → system. That is why apps ship with
    numeric prefixes like `000_overrides`, and why guessing from memory costs an
    afternoon.

    **The method.** Never reason about precedence from memory:
    ```bash
    splunk btool props list vendor:app --debug
    ```
    `--debug` prefixes each line with the file it came from. Without it you see
    the answer and not the reason, which is useless for a conflict.

---

## 7. Least privilege, or the appearance of it

```conf
[role_soc_analyst]
importRoles = admin
srchIndexesAllowed = sec_high;sec_std
srchIndexesDefault = sec_std
```

Assess against a requirement of least privilege.

??? success "Marking key"
    **Defect.** `importRoles = admin` inherits every admin capability, including
    `admin_all_objects`, `edit_roles` and `delete_by_keyword`. The
    `srchIndexesAllowed` line looks like a restriction and is not one: an admin
    can edit their own role.

    **Symptom.** An access review reads the stanza, sees a restricted index list,
    and signs it off. The restriction is decorative.

    **Fix.**
    ```conf
    [role_soc_analyst]
    importRoles = user
    srchIndexesAllowed = sec_high;sec_std
    srchIndexesDefault = sec_std
    srchJobsQuota = 5
    ```

    **Two design points for full marks.**

    - **"Security team gets everything" must be defended or abandoned.** An
      analyst does not get `hr_adjacent`, because it holds personal information
      whose access must be justifiable per APP 6, and a standing grant to a whole
      team cannot be justified per instance. Route it to a lead, audited.
    - **The platform administrator should not be able to read security data.**
      Someone who can both alter audit logging and read everything is a single
      point of total compromise. This is the separation people resist hardest.

    **Test it negatively.** A design with no negative test is untested. As
    `soc_analyst`, `index=hr_adjacent | head 1` must return zero — and note that
    Splunk renders an access denial identically to an empty index. Document how an
    analyst is meant to tell the difference, because during an incident they will
    need to.

---

## 8. nullQueue

```conf
# transforms.conf
[drop_noise]
REGEX = .
DEST_KEY = queue
FORMAT = nullQueue

# props.conf
[vendor:app]
TRANSFORMS-drop = drop_noise
```

Two defects, one of them catastrophic.

??? success "Marking key"
    **Defect 1, catastrophic.** `REGEX = .` matches any event containing at least
    one character — that is, all of them. The entire sourcetype is discarded.

    **Symptom.** Silent and total. `index=x sourcetype=vendor:app` returns
    nothing; there is no error, no queue backup, and no dropped-event counter that
    anyone watches. It looks exactly like the source not sending.

    **Defect 2.** Nothing records what was dropped. Six months later a gap in the
    data looks like an outage and someone spends a day on it.

    **Fix.** Anchor the pattern to what you actually mean, and keep a count:
    ```conf
    [drop_health_checks]
    REGEX = (?i)\burl="[^"]*/(healthz|ping|status)"
    DEST_KEY = queue
    FORMAT = nullQueue
    ```

    **State the cost before enabling it**, which is the graded part. `nullQueue`
    data is **gone** — not archived, not summarised, not recoverable. If an
    incident later turns on those health checks (proving a service was up,
    establishing a baseline, showing an attacker probed the endpoint), the answer
    is that you cannot know.

    **Mitigation.** Route a per-minute count to a metrics or summary index before
    the drop, so the volume survives even though the content does not.

---

## 9. Two settings that contradict each other

```conf
[app:multiline]
SHOULD_LINEMERGE = false
BREAK_ONLY_BEFORE = ^\[\d{4}-
LINE_BREAKER = ([\r\n]+)
TIME_PREFIX = ^\[
MAX_TIMESTAMP_LOOKAHEAD = 150
```

The source emits multi-line records beginning `[2026-03-12T09:14:22]`. Explain
what actually happens.

??? success "Marking key"
    **Defect 1 — a setting that does nothing.** `BREAK_ONLY_BEFORE` is only
    consulted when `SHOULD_LINEMERGE = true`. With line merging off it is ignored
    entirely. The stanza *reads* as though multi-line handling is configured; it
    is not.

    **Defect 2 — the wrong breaker.** `LINE_BREAKER = ([\r\n]+)` breaks on every
    newline, so each multi-line record becomes several events. Only the first
    carries a timestamp; the rest inherit the previous event's `_time`, which is
    close enough to look right and wrong enough to ruin any ordering.

    **Defect 3 — a lookahead that is too generous.** At 150 characters the
    timestamp parser scans well past the bracketed prefix and into the record
    body, where it will happily interpret any digit run as a date. `TIME_PREFIX`
    anchors the *start* of the scan; it does not bound its length.

    **Fix.**
    ```conf
    [app:multiline]
    SHOULD_LINEMERGE = false
    LINE_BREAKER = ([\r\n]+)(?=\[\d{4}-)
    TIME_PREFIX = ^\[
    TIME_FORMAT = %Y-%m-%dT%H:%M:%S
    MAX_TIMESTAMP_LOOKAHEAD = 20
    TRUNCATE = 100000
    CHARSET = UTF-8
    ```

    The lookahead assertion in `LINE_BREAKER` is the important move: it breaks
    *before* each timestamp without consuming it, which is the modern replacement
    for `BREAK_ONLY_BEFORE` and is faster because it does not merge.

    **Full marks** require noticing defect 1 — a setting that is present,
    plausible, and inert. Those are harder to find than settings that are wrong,
    because a reviewer reads them and moves on satisfied.

---

## What these have in common

Every defect above is **silent**. None of them fails to parse, none logs an
error, and several leave configuration in place that reads correctly to a
reviewer. That is not a coincidence in how the exercises were chosen — it is the
characteristic failure mode of Splunk configuration, and the reason the
[SPL-06 diagnostic method](../guides/spl-06.md) starts from `_internal` and
`btool` rather than from a hypothesis.

The generalisable habit: **for each setting you write, ask what the symptom would
be if it were wrong, and whether anything would tell you.** Where the answer is
"nothing would tell me", that setting needs a monitor, not just a review.
