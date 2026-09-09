# EXT-SPL self-assessment quiz

**52 questions across the nine Splunk modules.** Single-answer questions have one
correct option; **multiple-selection** questions have two or more and are marked
as such. Answer a question and press **Check** to reveal the answer and the
reasoning, or use **Check all** at the bottom.

Every question is drawn from material in the [module series](index.md) and the
[lab guides](https://github.com/dev-nobytes-io/Open-source-cybersecurity-degree-australia-/tree/main/labs/guides).
Where a question quotes a number, that number was measured against the lab
dataset rather than estimated.

!!! note "Nothing is recorded"
    Your answers stay in the browser and are not submitted anywhere. This is
    formative self-assessment, not the module's graded work — the assessment
    criteria live in each module page.

!!! warning "Viewing this on GitHub"
    The quiz runs in your browser. On GitHub's raw markdown view the JavaScript
    does not execute, so use the published documentation site.

<style>
.qz{--qz-a:#2e7d32;--qz-b:#c62828;--qz-p:#1565c0;--qz-bd:#d7dce1;--qz-mut:#6b7783;
    --qz-card:rgba(127,127,127,.045);}
.qz-bar{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center;margin:.8rem 0 1rem;}
.qz-chip{font-size:.74rem;padding:.3rem .62rem;border:1px solid var(--qz-p);color:var(--qz-p);
    background:transparent;border-radius:14px;cursor:pointer;font-family:inherit;}
.qz-chip[aria-pressed=true]{background:var(--qz-p);color:#fff;}
.qz-act{font-size:.78rem;padding:.42rem .8rem;border:1px solid var(--qz-p);background:var(--qz-p);
    color:#fff;border-radius:6px;cursor:pointer;font-family:inherit;}
.qz-act.ghost{background:transparent;color:var(--qz-p);}
.qz-score{margin-left:auto;font-size:.82rem;font-weight:700;}
.qz-q{border:1px solid var(--qz-bd);border-radius:9px;padding:.85rem 1rem;margin:.85rem 0;
    background:var(--qz-card);}
.qz-q[hidden]{display:none;}
.qz-meta{display:flex;gap:.5rem;align-items:center;font-size:.7rem;color:var(--qz-mut);
    text-transform:uppercase;letter-spacing:.05em;margin-bottom:.35rem;}
.qz-tag{border:1px solid var(--qz-bd);border-radius:10px;padding:.05rem .45rem;}
.qz-tag.multi{color:var(--qz-p);border-color:var(--qz-p);font-weight:700;}
.qz-stem{font-weight:600;margin:0 0 .6rem;line-height:1.45;}
.qz-opt{display:flex;gap:.55rem;align-items:flex-start;padding:.34rem .5rem;border-radius:6px;
    cursor:pointer;line-height:1.4;border:1px solid transparent;}
.qz-opt:hover{background:rgba(127,127,127,.09);}
.qz-opt input{margin-top:.22rem;flex:none;}
.qz-q.done .qz-opt{cursor:default;}
.qz-q.done .qz-opt.right{border-color:var(--qz-a);background:rgba(46,125,50,.11);}
.qz-q.done .qz-opt.wrong{border-color:var(--qz-b);background:rgba(198,40,40,.11);}
.qz-mark{font-weight:700;flex:none;width:1.1em;}
.qz-foot{display:flex;gap:.55rem;align-items:center;margin-top:.55rem;}
.qz-btn{font-size:.74rem;padding:.3rem .7rem;border:1px solid var(--qz-p);background:transparent;
    color:var(--qz-p);border-radius:5px;cursor:pointer;font-family:inherit;}
.qz-btn:disabled{opacity:.4;cursor:default;}
.qz-verdict{font-size:.78rem;font-weight:700;}
.qz-verdict.ok{color:var(--qz-a);} .qz-verdict.no{color:var(--qz-b);}
.qz-why{margin-top:.55rem;padding:.6rem .75rem;border-left:3px solid var(--qz-p);
    background:rgba(21,101,192,.07);font-size:.88rem;line-height:1.5;border-radius:0 5px 5px 0;}
.qz-why[hidden]{display:none;}
.qz code{font-size:.9em;}
</style>

<div class="qz" id="qz">
  <div class="qz-bar" id="qz-filters"></div>
  <div class="qz-bar">
    <button class="qz-act" id="qz-all">Check all</button>
    <button class="qz-act ghost" id="qz-reset">Reset</button>
    <span class="qz-score" id="qz-score">Not started</span>
  </div>
  <div id="qz-list"></div>
  <div class="qz-bar">
    <button class="qz-act" id="qz-all2">Check all</button>
    <button class="qz-act ghost" id="qz-reset2">Reset</button>
  </div>
</div>

<script>
(function () {
  var Q = [{"m":"SPL-01","t":"single","q":"A search returns zero results for <code>sourcetype=oscd:proxy</code>, but the sourcetype appears in the sourcetype picker and <code>index=proxy</code> returns thousands of events. What is the most likely cause?","o":["The events carry a JSON field named <code>sourcetype</code> which, under <code>INDEXED_EXTRACTIONS = json</code>, shadows the sourcetype assigned in inputs.conf","The index has not finished replicating","The sourcetype was renamed but the picker is cached","Search-time field extraction is disabled for that sourcetype"],"a":[0],"e":"Payload keys named <code>index</code>, <code>sourcetype</code>, <code>source</code> or <code>host</code> collide with Splunk metadata. Under <code>INDEXED_EXTRACTIONS = json</code> the payload value wins and the metadata value becomes unsearchable — with no error anywhere. Metadata belongs in metadata."},{"m":"SPL-01","t":"single","q":"Which of these is the <em>most</em> selective filter, and therefore belongs earliest in a search?","o":["The time range","<code>| where status=404</code>","<code>| search user=alice</code>","<code>| stats count by user</code>"],"a":[0],"e":"Time range determines which buckets are opened at all. Every other filter operates on events already retrieved. It is almost always the largest single performance lever."},{"m":"SPL-01","t":"multi","q":"Select every statement that is true of the Splunk <strong>Free</strong> licence.","o":["There is no authentication — every user is admin","Scheduled searches and alerting are unavailable","Distributed search is unavailable","Data cannot be forwarded to it from a universal forwarder"],"a":[0,1,2],"e":"Free accepts forwarded data perfectly well (up to the daily volume limit) and runs a deployment server — which is why the forwarder labs run on it. What it lacks is auth, alerting/scheduling and distributed search."},{"m":"SPL-01","t":"single","q":"You want to compare internal and external source addresses in the lab dataset. Why is <code>index=proxy</code> the wrong index for a <code>cidrmatch(\"10.0.0.0/8\", src)</code> exercise?","o":["Every <code>proxy.src</code> is an internal 10.x address, so the comparison is degenerate","<code>cidrmatch</code> does not work on the <code>src</code> field","The proxy index has no <code>src</code> field","CIDR matching requires an accelerated data model"],"a":[0],"e":"All proxy traffic originates from internal workstations. Use <code>index=cloud</code>, where <code>src</code> is genuinely public and varied, or the comparison teaches nothing."},{"m":"SPL-02","t":"single","q":"A subsearch exceeds its <code>maxout</code> limit (50,000 rows by default). What happens?","o":["It silently truncates and the outer search returns a confidently wrong answer","The search fails with an error","The subsearch is automatically converted to a <code>stats</code> operation","The outer search runs but is flagged in the job inspector as incomplete"],"a":[0],"e":"This is a correctness defect, not a performance one. Rewriting <code>join</code> as <code>stats</code> is usually presented as an optimisation; it also removes a silent truncation bug."},{"m":"SPL-02","t":"single","q":"In a Simple XML form, what does the token filter in <code>$user|s$</code> do, and why does it matter?","o":["Quotes the value for safe interpolation into a search — an unfiltered token is a search-injection defect","Converts the value to a string type","Sorts multi-value token contents","Strips whitespace from the token"],"a":[0],"e":"An unfiltered <code>$user$</code> interpolated straight into SPL lets a crafted input alter the search. The <code>|s</code> filter quotes it. This is marked down in the module when omitted."},{"m":"SPL-02","t":"multi","q":"A CIM-based detection silently starts returning zero results after a vendor upgrade renames a field. Which of these would have <em>detected the detection failing</em>?","o":["Monitoring the fraction of events that successfully enrich or normalise","A canary event that should always trigger the detection","Alerting when a detection's fire count drops to zero over a period it normally fires","Increasing the detection's schedule frequency"],"a":[0,1,2],"e":"Running it more often does not help — it returns zero more often. Silent failure needs a positive signal: match rate, canaries, or absence-of-firing monitoring."},{"m":"SPL-02","t":"single","q":"Why is a per-user robust baseline (median and MAD) preferable to a global mean-and-standard-deviation threshold for daily egress?","o":["Per-user activity is log-normal, so a global threshold is wrong by construction, and the mean is inflated by the very outliers being sought","MAD is faster to compute in SPL","Standard deviation cannot be computed by <code>eventstats</code>","Log-normal data has no mean"],"a":[0],"e":"Two separate problems: heterogeneity across users (global thresholds are wrong per-user) and contamination (an insider active throughout the baseline window inflates their own mean)."},{"m":"SPL-03","t":"single","q":"A per-account rule <code>stats count by user | where failures &gt; 5</code> misses a password spray entirely. What is the defect?","o":["The aggregation key. A spray is designed to stay under per-account thresholds; counting distinct accounts per <em>source</em> finds it","The threshold of 5 is too high","The time span is too short","Failed logons are not being indexed"],"a":[0],"e":"Tuning the number 5 cannot fix this. The search counts the wrong thing: pivot the aggregation from user to source and the sprayer separates from the noisiest benign source by an order of magnitude."},{"m":"SPL-03","t":"single","q":"A naive geo-velocity impossible-travel rule returns ~140 candidate pairs across 72 users in a 14-day window with one real attacker. What is the correct diagnosis?","o":["Base rate — the rule is logically sound and the data is fine; legitimate travellers vastly outnumber the attacker","A logic error in the distance calculation","A normalisation failure in the cloud sign-in sourcetype","Missing telemetry — the sign-in logs are incomplete"],"a":[0],"e":"None of logic, normalisation or telemetry is at fault. This is the base-rate problem, and the fix is a filter that targets something the adversary needs — such as legacy authentication, which bypasses MFA."},{"m":"SPL-03","t":"multi","q":"When narrowing an impossible-travel detection, which filters target something the <em>adversary needs</em> rather than something incidental?","o":["Require a legacy authentication protocol or an unsatisfied MFA result","Exclude service accounts","Require a sign-in from a country on a high-risk list","Require the destination to be a crown-jewel asset"],"a":[0],"e":"Legacy protocols bypass MFA, which is <em>why</em> adversaries use them — instrumental to the attack. Excluding service accounts is a noise reduction with a real cost. A country list encodes today's org chart and is the least transferable filter you can build."},{"m":"SPL-03","t":"single","q":"Measuring beaconing regularity on a compromised host gives a coefficient of variation near 3.0 — apparently random. Filtering to the suspected C2 domains gives 0.05. What does this tell you?","o":["Isolate the candidate channel before measuring regularity; mixed with normal browsing the signal vanishes into the variance","The CV metric is unreliable for beacon detection","The host is not actually beaconing","The proxy logs have incorrect timestamps"],"a":[0],"e":"The compromised host also browses normally. A learner who computes CV over all of a host's traffic concludes the technique does not work. This is method, not a defect."},{"m":"SPL-03","t":"single","q":"Sysmon in the lab estate carries EventCode 1 only. Kerberoasting (T1558.003) cannot be detected. How should this be classified and routed?","o":["Telemetry gap — route to data engineering; no detection content can close it","Detection gap — route to detection engineering","Covered, but with low confidence","Out of scope for ATT&CK coverage assessment"],"a":[0],"e":"The distinction is the whole point of a coverage assessment. A remediation plan that sends telemetry gaps to the detection team is wrong regardless of how good the detections it proposes are."},{"m":"SPL-03","t":"multi","q":"In an ACH table, which pieces of evidence have genuine <strong>diagnostic value</strong> for separating a C2 beacon from a broken DNS client?","o":["Algorithmically generated domain labels combined with regular inter-arrival timing","A 38% NXDOMAIN rate","The host is in the Sales department","Small transfer volumes"],"a":[0],"e":"A high NXDOMAIN rate is equally consistent with a broken client, so on its own it has no diagnostic value however compelling it looks. Only the conjunction of random labels and regular timing separates the hypotheses."},{"m":"SPL-04","t":"single","q":"<code>| tstats count from datamodel=Web</code> returns rows. What has this proved?","o":["That the data model maps. It has <em>not</em> proved acceleration ran — that needs <code>summariesonly=true</code>","That acceleration completed successfully","That the underlying index is correctly parsed","Both mapping and acceleration"],"a":[0],"e":"Reporting the first as though it were the second is the exact failure a post-install validation report is meant to catch."},{"m":"SPL-04","t":"single","q":"A stalled data-model acceleration produces which symptom?","o":["<code>tstats summariesonly=t</code> returns fewer rows — no error, silent loss of recall in every detection built on it","A clear error in the scheduler log and a red banner","Searches fail with a bundle replication error","The data model disappears from the picker"],"a":[0],"e":"Silence is the danger. Nothing tells you; you have to ask, via <code>/services/admin/summarization</code> and a completion/age check."},{"m":"SPL-04","t":"multi","q":"An Asset &amp; Identity lookup goes stale (half the rows vanish). Which monitors would catch it?","o":["Match rate — the fraction of events that successfully enrich","Row-count drift against an expected value","Freshness — when the lookup file last changed","Alerting when the lookup file is deleted"],"a":[0,1,2],"e":"Match rate is the strongest of the three because it measures the thing you actually care about: a lookup can be fresh, full-sized and still match nothing if the join key format changed. File deletion is not the failure mode — silent partial staleness is."},{"m":"SPL-04","t":"single","q":"In ES 8 terminology, what was previously called a <em>risk notable</em>?","o":["An intermediate finding","A finding","A detection","A risk factor"],"a":[0],"e":"ES 8 renamed correlation search → detection, notable → finding, risk notable → intermediate finding, and <code>risk_object</code>/<code>risk_object_type</code> → <code>entity</code>/<code>entity_type</code>. Risk factors became multipliers."},{"m":"SPL-04","t":"single","q":"You apply two risk factors: 1.5× for high asset priority and 1.4× for privileged accounts. What must you check before defending the model?","o":["Whether the two factors are correlated — privileged users are usually also high-priority, so you may have applied one adjustment twice","That the product does not exceed the maximum risk score","That both factors are integers","That the factors are applied before the risk score is normalised"],"a":[0],"e":"Multiplicative factors compound. Correlated factors are not two independent adjustments; check the joint distribution in the identity lookup before claiming they are."},{"m":"SPL-05","t":"single","q":"An enrichment source becomes unreachable. What is the correct behaviour for a playbook that must 'fail without producing a wrong answer'?","o":["Mark the artefact <strong>unenriched</strong>, as a state distinct from enriched-and-clean","Treat it as clean and continue","Retry immediately until it responds","Abort the entire playbook run"],"a":[0],"e":"A two-state field (malicious / not malicious) silently converts every outage into an all-clear — and does so exactly when the estate is stressed and providers are overloaded. Unknown and clean must be different values all the way to the analyst's screen."},{"m":"SPL-05","t":"single","q":"An approval prompt in a containment playbook times out at 3 a.m. with no response. Which timeout behaviours are defensible?","o":["No action, or escalate to a second approver and then no action","Proceed with the action, since the detection was high confidence","Proceed, but log the absence of approval","Retry the prompt indefinitely"],"a":[0],"e":"'Timeout → proceed' is never defensible. Which of the two acceptable options you choose depends on whether the action is reversible and whether you have 24-hour coverage."},{"m":"SPL-05","t":"multi","q":"An attacker gains playbook-edit access to your SOAR platform. Which suppressions could they achieve <em>without</em> touching any credential?","o":["Add an early exit for artefacts matching their own infrastructure, leaving logging intact","Change a containment action to a no-op","Edit an enrichment step to return <code>clean</code> instead of <code>unknown</code> on failure","Widen a bounded target set so a future containment causes an outage"],"a":[0,1,2,3],"e":"All four. The automation is a security control and therefore a target. The detection that works is not 'alert on edit' — edits are normal — but reconciling the deployed playbook hash against version control and alerting on <strong>divergence</strong>."},{"m":"SPL-05","t":"multi","q":"A vendor reports 'hours saved' as successful runs × manual minutes. Which criticisms are valid?","o":["It counts work nobody would have done — automation makes a task cheap, so you do far more of it","It ignores maintenance engineering time","It ignores failed runs, which an analyst still had to handle","Automation raises average handling time on what remains, because it absorbs the easy cases"],"a":[0,1,2,3],"e":"All four, plus a fifth: saved time is not saved money unless a queue actually shortened. A defensible metric is time-to-containment for incidents that mattered, and decisions made per analyst per shift."},{"m":"SPL-05","t":"single","q":"In an audit trail for an automated containment that fired wrongly, which field is most often missing and most needed?","o":["The playbook <strong>version hash</strong> at time of execution","The timestamp of the action","The name of the playbook","The artefact type"],"a":[0],"e":"Six weeks later, 'playbook contain_host v?' is not an answer, and the repository history will not tell you which version was deployed at 03:14 unless something recorded it."},{"m":"SPL-06","t":"single","q":"An index has <code>frozenTimePeriodInSecs</code> set to 7 years and <code>maxTotalDataSizeMB</code> left at a low default. What happens?","o":["Buckets roll to frozen when either limit is hit, so the 7-year obligation silently becomes a few months","The age setting takes precedence and 7 years is honoured","Splunk warns at index creation","Indexing stops when the size cap is reached"],"a":[0],"e":"Whichever limit binds first wins, silently, in the direction that matters for compliance. This is the single most common index-design defect."},{"m":"SPL-06","t":"single","q":"For <code>props.conf</code> in the global context, which layer wins?","o":["<code>system/local</code> → <code>apps/*/local</code> → <code>apps/*/default</code> → <code>system/default</code>","<code>apps/*/local</code> → <code>system/local</code> → <code>apps/*/default</code> → <code>system/default</code>","Alphabetical order of app name, always","The most recently modified file"],"a":[0],"e":"But this ordering is not universal. In app/user scope (savedsearches, macros, views) it is user → app in <strong>ASCII order of app name</strong> → system, which is why apps ship with numeric prefixes. Use <code>btool --debug</code> rather than memory."},{"m":"SPL-06","t":"single","q":"An Australian log source emits <code>12/03/2026</code>. Splunk's default parsing resolves this as 12 March. What is the practical consequence?","o":["Days 1–12 of each month land in the wrong month while days 13+ parse correctly — a mixture that passes spot checks","All timestamps are wrong by a consistent offset, which is easy to spot","Events are rejected at parse time","Only the year is affected"],"a":[0],"e":"A uniform failure would be found immediately. A mixture is far worse: any spot check on a date after the 12th looks fine. Set <code>TIME_FORMAT = %d/%m/%Y</code> explicitly, and <code>TZ</code> too."},{"m":"SPL-06","t":"multi","q":"You push a bad monitor input via the deployment server to every host in a server class. What would have limited the blast radius?","o":["A staged server class: a canary host, promoted after a soak period","<code>restartSplunkd = false</code> where the change does not require a restart","A positive <code>whitelist</code> on the monitor input rather than <code>.*</code>","Running <code>btool check</code> on the deployment server before reloading"],"a":[0,1,2],"e":"<code>btool check</code> catches invalid configuration; the dangerous push is <em>valid</em> and wrong. The deployment server has no <code>--check</code>, no <code>--limit</code> and no dry run, which makes the staged server class the only real lever."},{"m":"SPL-06","t":"single","q":"You mask a secret with <code>SEDCMD</code>. Which check actually proves the secret is absent from the index?","o":["Grepping the bucket files on disk","A search for the secret returning zero results","The absence of the field in the field picker","<code>| tstats</code> returning no matching events"],"a":[0],"e":"A search returning zero is not proof — a search-time alias or a <code>fields</code> command could be hiding it. Also note <code>SEDCMD</code> runs on the indexer or heavy forwarder, never on a universal forwarder, so it cannot stop a secret leaving a host."},{"m":"SPL-06","t":"single","q":"Queue metrics show <code>indexqueue</code> full and <code>parsingqueue</code> not full. Where is the blockage?","o":["Downstream of parsing — queues fill backwards from the blockage","In the parsing pipeline","At the forwarder","In the search head's knowledge bundle"],"a":[0],"e":"Read queue fill right to left. The first-full queue is the symptom; the last one still draining is nearest the cause."},{"m":"SPL-06","t":"single","q":"A search head loses contact with one of its peers mid-search. What does the user see?","o":["The search completes with results missing that peer's data, and a warning in the messages rather than in the results","An error and no results","The search hangs until the peer returns","Results are automatically re-run against the remaining peers"],"a":[0],"e":"Distributed search fails <em>partially</em>, and partial failures do not look like failures. A scheduled threshold detection running at that moment simply does not fire."},{"m":"SPL-07","t":"single","q":"With RF=3 and SF=2, rawdata ≈ 0.15× and tsidx ≈ 0.35× of raw ingest, what is the storage multiple against raw ingest?","o":["1.15× — (3 × 0.15) + (2 × 0.35)","3.0× — the replication factor","1.50× — (3 × 0.15) + (3 × 0.35)","0.50× — one bucket copy"],"a":[0],"e":"State it in these terms to a finance approver: 'we store 1.15 bytes on disk per byte ingested, and 1.50× if we go to RF=3/SF=3'. 'RF=3/SF=2' is a configuration; the multiple is an architecture decision someone can price."},{"m":"SPL-07","t":"single","q":"Sizing gives 8 indexers on ingest, 7 on search concurrency and 14 on storage. What follows?","o":["The deployment is storage-bound: six indexers' worth of CPU is being bought to carry disk, which is the case SmartStore addresses","Provision 8 indexers and add storage later","Take the average, 10","Provision 14 and treat the CPU headroom as growth capacity"],"a":[0],"e":"Which constraint binds tells you what kind of deployment you have, and therefore which architectural lever is worth pulling."},{"m":"SPL-07","t":"multi","q":"Which workloads are <strong>worse</strong> under SmartStore?","o":["Long-range rare-term searches across 12 months","Wide scheduled searches over old data, where the download is paid on every run","The first search after a cache eviction","Dashboard searches over the last 24 hours"],"a":[0,1,2],"e":"Recent-data workloads hit a warm cache and are unaffected. The worst case is the rare-term search across a year — which is exactly the 'did this indicator ever appear?' threat-hunting query, one of the most valuable searches a SOC runs."},{"m":"SPL-07","t":"single","q":"You kill the cluster manager while searches are running. What happens?","o":["Searches keep working; what you lose is the ability to recover — no bucket fix-up, no rebalancing, no new peers","All searches fail immediately","The search head elects a new manager automatically","Indexing stops on all peers"],"a":[0],"e":"It is a latent failure, and the danger is that nobody notices for a week — during which a second failure has no safety net."},{"m":"SPL-07","t":"single","q":"A stated tolerance is 'survive one indexer with no search interruption'. Why is RF=3/SF=3 marked down as an architecture failure?","o":["It spends ~35% more storage to buy a resilience property nobody asked for; someone else's project does not get funded so that yours can be over-engineered","It does not actually provide more resilience than RF=3/SF=2","It is incompatible with SmartStore","Search factor cannot equal replication factor"],"a":[0],"e":"Designing for maximum resilience regardless of requirement is an architecture failure, not caution. Write the recommendation with the cost multiple attached."},{"m":"SPL-07","t":"single","q":"In a single-site to multi-site migration, where is the point of no return?","o":["When site-specific replication factors are set and buckets have been fixed to satisfy them","When the second site's peers are first stood up","When the cluster manager is upgraded","When search heads are made site-aware"],"a":[0],"e":"Reverting does not un-copy data, and from that stage the cluster's correctness depends on cross-site links: a WAN failure means the manager cannot satisfy site RF and begins remediation it cannot complete."},{"m":"SPL-08","t":"single","q":"A client says 'our SIEM is too slow'. What is the most useful elicitation question?","o":["Slow doing what? What did you time, and what would fast enough be?","How many indexers do you have?","What is your daily ingest volume?","Which version are you running?"],"a":[0],"e":"'Slow' is often a 40-minute analyst workflow of which the SIEM is 90 seconds. The question converts a preference into an observable event you can write an acceptance test against."},{"m":"SPL-08","t":"multi","q":"What makes a deviation record in a base-configuration standard genuinely useful?","o":["The alternatives considered and why they were rejected","A review trigger — the condition under which it should be revisited","A named owner","The date it was written"],"a":[0,1,2],"e":"A date alone produces a list of exceptions nobody revisits. Deviation, reason, alternatives rejected, review trigger and owner is the structure that survives handover."},{"m":"SPL-08","t":"single","q":"Why is 'a roadmap where everything is priority one' a failed roadmap?","o":["It transfers the prioritisation decision back to the client, who has less information than you do — the ordering is what you were hired for","It is too long to read","It implies the deployment is beyond repair","It cannot be costed"],"a":[0],"e":"The 'accept and document' category is the proof you did the work: you found it, costed it, and concluded it was not worth fixing. That is a finding, not an omission."},{"m":"SPL-08","t":"single","q":"Which handover artefact is weighted most heavily, and why?","o":["The decision register — it is the only artefact that answers <em>why</em>, and it is what makes a system safe to change","The runbooks, because they are executable","The architecture diagram, because it is the overview","The known-limitations list, because it manages expectations"],"a":[0],"e":"Two years on, nobody remembers why RF is 3. Without the register the next consultant either changes it — reintroducing a risk somebody already reasoned about — or leaves it alone out of caution, which is how estates ossify."},{"m":"SPL-08","t":"single","q":"A client has one excellent engineer who can operate the platform. Under the build-versus-manage test, what does this indicate?","o":["A failure of the test — a single-person platform capability is an outage waiting on a resignation","A pass, since competence is demonstrated","Neither; headcount is not a relevant criterion","A pass, provided the engineer is well documented"],"a":[0],"e":"The question is sustained capacity, not competence. Saying so is worth more to the client than the implementation revenue you would win by not saying it — and the conflict of interest belongs in the document, not a footnote."},{"m":"SPL-09","t":"single","q":"In SPL, <code>log(x)</code> defaults to base 10. What happens if you write <code>log(2)</code> instead of <code>ln(2)</code> in a risk-decay half-life calculation?","o":["λ is too small by a factor of ln(10) ≈ 2.303, so the half-life is about 3.3× longer than specified — silently, with no error","The search fails with a domain error","The decay becomes linear rather than exponential","Nothing; the two are equivalent"],"a":[0],"e":"Your 7-day half-life is silently a 23-day one, and every threshold calibrated against it is wrong. Note that Python's <code>math.log</code> is natural and <code>math.log10</code> is base 10 — the opposite convention, which is exactly how this defect crosses over."},{"m":"SPL-09","t":"single","q":"An entity accrues a steady 10 risk points per day under a 7-day half-life. What is its steady state R*?","o":["≈ 101, from R* = s·t½/ln2","70, from s × t½","10, since decay balances accrual at the arrival rate","Unbounded — risk accumulates indefinitely"],"a":[0],"e":"dR/dt = −λR + s gives R* = s/λ = s·t½/ln2 = 10 × 7 / 0.693 ≈ 101. Any threshold below that alerts on every steadily-noisy entity forever, which is how risk queues fill with service accounts."},{"m":"SPL-09","t":"single","q":"At a base rate of 1 in 100,000 and TPR 0.8, roughly what false-positive rate does a detection need to reach PPV = 0.25?","o":["About 2.4 × 10⁻⁵ — one false positive per ~42,000 events","About 1 in 100","About 1 in 1,000","About 0.25, matching the target PPV"],"a":[0],"e":"Almost no hand-written detection achieves that, and the arithmetic says so before you deploy it. This is why base rate, not cleverness, dominates alert quality."},{"m":"SPL-09","t":"multi","q":"Which classifications are correct under the finding / intermediate finding / threshold alert / dashboard decision rule?","o":["'Data source stopped sending for 30 minutes' → threshold alert","'Volume of egress per user per day' → dashboard panel","'A user's egress exceeding their own 30-day p99' → intermediate finding","'Encryption disabled on a database' → intermediate finding"],"a":[0,1,2],"e":"The last is a compliance-driven <strong>promotion</strong> to a finding: by the decision rule it might be an intermediate finding, but a control a regulator requires must be demonstrably actioned, and only a finding leaves that record. State the exception rather than pretending the rule produced it."},{"m":"SPL-09","t":"single","q":"For every dashboard-classified signal, what is the single most useful test?","o":["What happens if nobody looks at this for a week? If the answer is 'something bad', it is a finding with no way to reach anyone","Does it render in under two seconds?","Can it be built from an accelerated data model?","Does it have a drilldown?"],"a":[0],"e":"This one question retires more bad dashboards than any design review."},{"m":"SPL-09","t":"single","q":"L1-regularised logistic regression fits a <strong>negative</strong> weight to 'LOLBin Download Behaviour', which analysts hand-scored 60 — the highest in the set. What does this mean?","o":["In this labelled population, that detection fires overwhelmingly on benign activity; the fit has learned the base rate, not a judgement about severity","The technique is not actually dangerous","There is a sign error in the implementation","The feature should be removed from the model"],"a":[0],"e":"Fitted weights optimise for what is <em>usually</em> true; hand scores encode what is <em>occasionally catastrophic</em>. Any deployment of fitted weights needs a floor under techniques you cannot afford to miss — and choosing that floor is a judgement, not a fit."},{"m":"SPL-09","t":"multi","q":"Your risk weights are fitted on analyst dispositions. Which selection-bias statements must appear in the deliverable?","o":["There are no labels for behaviour that never alerted, so the model cannot say what you are missing","Analyst dispositions are noisy and biased — a busy shift closes more as benign","A detection that never fires contributes no rows and gets weight zero, which reads as 'useless' but may mean 'never tested'","The model is valid for reallocating attention among detections you already run"],"a":[0,1,2,3],"e":"All four. Without this paragraph the model will be used to delete detections it has no information about."},{"m":"SPL-09","t":"single","q":"A character-entropy DGA scorer achieves 100% precision on the lab's synthetic DGA. Why is this <em>not</em> evidence that entropy works well?","o":["The synthetic DGA draws characters uniformly, which is exactly the distribution entropy assumes — the test set was drawn from the detector's own model","Precision is the wrong metric at a fixed budget","The benign corpus is too small","Entropy was measured on the wrong label"],"a":[0],"e":"Real DGAs are not uniform. Worse, entropy here is partly measuring <strong>length</strong> — benign filler is 6–10 characters and the DGA is 12–18. Control for length and the gap narrows sharply; that is the transferable lesson."},{"m":"SPL-09","t":"single","q":"A flagged egress day is 67,000× the user's median but has a z-score of 3.18. What should the analyst-facing explanation report?","o":["The ratio and the bytes; keep the z-score for ranking only","The z-score, since it is the model's native output","Both, with the z-score first","The percentile rank"],"a":[0],"e":"The log transform compresses a heavy-tailed quantity, so a dramatic event yields an unremarkable z-score. An explanation an analyst cannot act on is a model defect, not an analyst deficiency."},{"m":"SPL-09","t":"multi","q":"Match each optimisation to the cascade stage it acts on. Which pairings are correct?","o":["Tightening the time range → bucket selection","Removing a leading wildcard and using <code>TERM()</code> → index lookup","Replacing <code>join</code> with <code>stats</code> → distribution (and it also fixes a silent correctness bug)","Rewriting against an accelerated data model with <code>tstats</code> → summarisation"],"a":[0,1,2,3],"e":"All four. A speedup you cannot attribute to a stage does not count — and anyone optimising <code>join</code> → <code>stats</code> for speed without noticing they also removed a silent subsearch truncation has missed the more important half."}];
  var list = document.getElementById('qz-list');
  var filter = 'all';

  function esc(s) { return s; }

  Q.forEach(function (q, i) {
    var d = document.createElement('div');
    d.className = 'qz-q';
    d.dataset.module = q.m;
    var opts = q.o.map(function (o, j) {
      var type = q.t === 'multi' ? 'checkbox' : 'radio';
      return '<label class="qz-opt" data-i="' + j + '">' +
             '<input type="' + type + '" name="q' + i + '" value="' + j + '">' +
             '<span class="qz-mark"></span><span>' + esc(o) + '</span></label>';
    }).join('');
    d.innerHTML =
      '<div class="qz-meta"><span class="qz-tag">' + q.m + '</span>' +
      (q.t === 'multi' ? '<span class="qz-tag multi">select all that apply</span>' : '') +
      '<span>Q' + (i + 1) + '</span></div>' +
      '<p class="qz-stem">' + esc(q.q) + '</p>' +
      '<div class="qz-opts">' + opts + '</div>' +
      '<div class="qz-foot"><button class="qz-btn" type="button" data-check="' + i + '">Check</button>' +
      '<span class="qz-verdict"></span></div>' +
      '<div class="qz-why" hidden><strong>Why:</strong> ' + esc(q.e) + '</div>';
    list.appendChild(d);
  });

  var cards = Array.prototype.slice.call(list.children);

  function chosen(i) {
    return Array.prototype.slice
      .call(cards[i].querySelectorAll('input:checked'))
      .map(function (el) { return parseInt(el.value, 10); })
      .sort(function (a, b) { return a - b; });
  }

  function check(i) {
    var q = Q[i], card = cards[i], picked = chosen(i);
    if (!picked.length) return false;
    var want = q.a.slice().sort(function (a, b) { return a - b; });
    var right = picked.length === want.length &&
                picked.every(function (v, k) { return v === want[k]; });
    card.classList.add('done');
    card.querySelectorAll('input').forEach(function (el) { el.disabled = true; });
    card.querySelectorAll('.qz-opt').forEach(function (lab) {
      var j = parseInt(lab.dataset.i, 10);
      var isAns = want.indexOf(j) !== -1, isPicked = picked.indexOf(j) !== -1;
      var mark = lab.querySelector('.qz-mark');
      if (isAns) { lab.classList.add('right'); mark.textContent = '✓'; mark.style.color = 'var(--qz-a)'; }
      else if (isPicked) { lab.classList.add('wrong'); mark.textContent = '✗'; mark.style.color = 'var(--qz-b)'; }
    });
    var v = card.querySelector('.qz-verdict');
    v.textContent = right ? 'Correct' : (picked.length && want.length > 1 ? 'Not quite' : 'Incorrect');
    v.className = 'qz-verdict ' + (right ? 'ok' : 'no');
    card.querySelector('.qz-why').hidden = false;
    card.querySelector('[data-check]').disabled = true;
    card.dataset.result = right ? 'right' : 'wrong';
    return true;
  }

  function score() {
    var done = cards.filter(function (c) { return c.dataset.result && !c.hidden; });
    var ok = done.filter(function (c) { return c.dataset.result === 'right'; }).length;
    var visible = cards.filter(function (c) { return !c.hidden; }).length;
    var el = document.getElementById('qz-score');
    el.textContent = done.length
      ? ok + ' / ' + done.length + ' correct  (' + done.length + ' of ' + visible + ' answered)'
      : 'Not started';
  }

  list.addEventListener('click', function (e) {
    var b = e.target.closest('[data-check]');
    if (!b) return;
    check(parseInt(b.dataset.check, 10));
    score();
  });

  function checkAll() {
    cards.forEach(function (c, i) { if (!c.hidden && !c.dataset.result) check(i); });
    score();
  }

  function reset() {
    cards.forEach(function (c) {
      c.classList.remove('done');
      delete c.dataset.result;
      c.querySelectorAll('input').forEach(function (el) { el.disabled = false; el.checked = false; });
      c.querySelectorAll('.qz-opt').forEach(function (lab) {
        lab.classList.remove('right', 'wrong');
        lab.querySelector('.qz-mark').textContent = '';
      });
      c.querySelector('.qz-verdict').textContent = '';
      c.querySelector('.qz-why').hidden = true;
      c.querySelector('[data-check]').disabled = false;
    });
    score();
    window.scrollTo({ top: document.getElementById('qz').offsetTop - 20, behavior: 'smooth' });
  }

  ['qz-all', 'qz-all2'].forEach(function (id) {
    document.getElementById(id).addEventListener('click', checkAll);
  });
  ['qz-reset', 'qz-reset2'].forEach(function (id) {
    document.getElementById(id).addEventListener('click', reset);
  });

  var mods = ['all'].concat(Q.map(function (q) { return q.m; })
    .filter(function (m, i, a) { return a.indexOf(m) === i; }).sort());
  var bar = document.getElementById('qz-filters');
  mods.forEach(function (m) {
    var b = document.createElement('button');
    b.className = 'qz-chip';
    b.type = 'button';
    b.textContent = m === 'all' ? 'All modules (' + Q.length + ')' : m;
    b.setAttribute('aria-pressed', m === 'all' ? 'true' : 'false');
    b.addEventListener('click', function () {
      filter = m;
      bar.querySelectorAll('.qz-chip').forEach(function (o) {
        o.setAttribute('aria-pressed', o === b ? 'true' : 'false');
      });
      cards.forEach(function (c) { c.hidden = (filter !== 'all' && c.dataset.module !== filter); });
      score();
    });
    bar.appendChild(b);
  });

  score();
})();
</script>
