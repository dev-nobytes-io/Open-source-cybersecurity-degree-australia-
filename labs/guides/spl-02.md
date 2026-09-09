# SPL-02 lab guide — SPL Mastery & Knowledge Objects

**Module:** [SPL-02](../../docs/modules/splunk/spl-02-power-user.md) · 8 labs,
7 ✅ on Free, 1 ⚠️ trial.

---

## Lab 1 ✅ — Build the Knowledge Layer for a Messy Source

`oscd:proxy` is already clean, so make a messy one. Emit a variant with an
awkward format, then normalise it:

```bash
python3 - <<'PY'
import json, random
rows=[json.loads(l) for l in open('data/events/proxy.json')][:3000]
with open('data/events/messy.json','w') as f:
    for r in rows:
        f.write(f"{r['_time']}|{r['user']}~{r['src_host']}~"
                f"GET {r['url']} {r['status']} out={r['bytes_out']}\n")
PY
```

Build extractions with `rex`, an alias, and an event type. **Justify each object
type** — solving everything with regex is marked down in the module.

## Lab 2 ✅ — Make a Source CIM-Compliant

Map `messy.json` to the CIM **Web** model: `action`, `src`, `dest`, `http_method`,
`status`, `bytes_out`, `user`.

```
index=main sourcetype=oscd:messy
| rex "^(?<epoch>\d+\.?\d*)\|(?<user>[^~]+)~(?<src_host>[^~]+)~(?<http_method>\w+) (?<url>\S+) (?<status>\d+) out=(?<bytes_out>\d+)"
| eval action=if(status<400,"allowed","blocked")
| rex field=url "https?://(?<dest>[^/]+)"
```

**Deliverable:** the gap statement — every CIM field you could **not** populate
and what telemetry would be needed. That artefact is the most valuable output.

## Lab 3 ⚠️ — Accelerate, and Pay For It

**Trial licence.** Data-model acceleration runs as a scheduled process, and the
Free licence has no scheduled searches.

Build a data model over `proxy`, time the raw search, accelerate, then:

```
| tstats summariesonly=t count from datamodel=OSCD_Web by OSCD_Web.src_host
```

**Deliverable:** before/after table covering search time, **disk consumed by the
summary**, and indexer load while it builds. "It got faster" is not sufficient.

## Lab 4 ✅ — Break a Detection with Normalisation

Write a CIM-based detection, then rename a field in `props.conf` as a vendor
upgrade would, and watch it return zero with no error.

```
index=proxy | where bytes_out > 50000000 | stats count by user
```

**Deliverable:** how you would have *detected the detection failing*. This is the
silent-failure problem and it connects to SPL-09 Topic 4's log-event argument.

## Lab 5 ✅ — Audit a Knowledge Layer

```
| rest /servicesNS/-/-/data/props/extractions | table eai:acl.app, stanza, attribute
| rest /servicesNS/-/-/admin/macros | table title, eai:acl.app, eai:acl.sharing
```

**Deliverable:** inventory plus a retirement proposal with a risk note per object.

## Lab 6 ✅ — Eliminate the `join`

Three searches to rewrite. The `join` version:

```
index=wineventlog action=success
| join user [ search index=proxy | stats sum(bytes_out) as egress by user ]
| table user egress
```

The `stats` rewrite — faster, no subsearch limit:

```
(index=wineventlog action=success) OR (index=proxy)
| stats count(eval(index="wineventlog")) as logins,
        sum(bytes_out) as egress by user
| where logins > 0
```

**Then demonstrate silent truncation.** Force a subsearch past its limit:

```
index=wineventlog [ search index=proxy | fields user | head 100000 ]
```

**Verify:** compare the result count against the `stats` version. The subsearch
returns a confidently wrong answer with **no error** — that is the finding.

## Lab 7 ✅ — Baseline Without Machine Learning

Per-user robust baseline. The dataset's per-user activity is log-normal, so a
global threshold is wrong by construction.

```
index=proxy
| bin _time span=1d
| stats sum(bytes_out) as daily by user, _time
| eventstats median(daily) as med by user
| eval dev=abs(daily-med)
| eventstats median(dev) as mad by user
| eval mod_z = 0.6745*(daily-med)/mad
| where mad > 0 AND mod_z > 3.5
| sort - mod_z
```

**Verify:** the exfiltration user should surface.

```bash
python3 harness/verify.py answer spl09.lab5.exfil_user <username>
```

Then run the same with `avg`/`stdev` instead and note how the insider's own
activity inflates their baseline — masking, and the reason for robust estimators.

## Lab 8 ✅ — Build a Real Dashboard in Simple XML

Simple XML by hand, not the UI. Required: three inputs with one **cascading**
pair, a **base search with two post-process panels**, a **dynamic drilldown**, and
an **event annotation**.

```xml
<form>
  <fieldset submitButton="false">
    <input type="dropdown" token="dept">
      <label>Department</label>
      <search><query>| inputlookup oscd_identities.csv | stats count by bunit</query></search>
      <fieldForLabel>bunit</fieldForLabel><fieldForValue>bunit</fieldForValue>
    </input>
    <input type="dropdown" token="usr">
      <label>User</label>
      <search><query>| inputlookup oscd_identities.csv | search bunit="$dept$"</query></search>
      <fieldForLabel>identity</fieldForLabel><fieldForValue>identity</fieldForValue>
    </input>
  </fieldset>
  <row>
    <panel>
      <search id="base">
        <query>index=proxy user="$usr|s$" | bin _time span=1h
               | stats sum(bytes_out) as egress, dc(dest) as sites by _time</query>
      </search>
      <chart><search base="base"><query>timechart span=1h sum(egress)</query></search></chart>
    </panel>
  </row>
</form>
```

**Note `$usr|s$`** — the quoting token filter. An unfiltered `$usr$` interpolated
into a search is an injection defect and is marked down.

**Deliverable:** the XML, a load-time comparison against a naive one-search-per-panel
version, and your justification for the token filter used.
