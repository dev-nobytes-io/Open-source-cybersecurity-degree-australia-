# EXT-ELK self-assessment quiz

> **Module type:** Extension series self-assessment — part of [EXT-ELK](index.md)
> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-09-13

!!! warning "Not a credit-bearing unit"
    See the [series index](index.md). This quiz carries no credit points and is not part
    of any module's graded assessment; the assessment criteria live in each module page.

**50 questions across the five Elastic and OpenSearch modules** — ten each for
[ELK-01](elk-01-collection-agent-fleet.md), [ELK-02](elk-02-ingest-pipelines-ecs-data-streams.md),
[ELK-03](elk-03-lifecycle-sizing-cluster-architecture.md), [ELK-04](elk-04-detection-rules-eql-security-app.md)
and [ELK-05](elk-05-opensearch-alternative-and-migration.md). Single-answer questions have one
correct option; **multiple-selection** questions (13 of them) have two or more and are
marked as such. Answer a question and press **Check** to reveal the answer and the
reasoning, or use **Check all** at the bottom. Every explanation names the module and topic
it comes from. Where a module marks something provisional or unverified — a subscription
tier, a version number — the quiz does not test it as settled fact.

!!! note "Nothing is recorded"
    Your answers stay in the browser and are not submitted anywhere.

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
  var Q = [{"m": "ELK-01", "t": "single", "q": "Fleet Server is down for an hour. According to the module, what happens to collection on enrolled agents during that hour?", "o": ["Collection continues; agents keep their last policy and still write data to Elasticsearch, but management (policy updates, upgrades, actions) stops", "Collection stops because agents cannot check in", "Agents fall back to standalone mode permanently", "Data is buffered on Fleet Server until it returns"], "a": [0], "e": "ELK-01 Topic 2: Fleet Server carries <em>control</em>, not data. Agents write to Elasticsearch directly; what breaks when Fleet Server is down is management, not collection."}, {"m": "ELK-01", "t": "single", "q": "In the data-stream name <code>logs-nginx.access-production</code>, which segment is the one the module calls a governance lever, and why?", "o": ["<code>production</code> — the namespace, because templates, ILM policies and role privileges all match on the stream name", "<code>logs</code> — the type, because it decides the ILM policy", "<code>nginx.access</code> — the dataset, because it sets the retention", "None — the name is only a label"], "a": [0], "e": "ELK-01 Topic 4: the namespace is yours, and because lifecycle and access control match on stream names, it is how retention and RBAC follow the data's obligation."}, {"m": "ELK-01", "t": "multi", "q": "Select every statement the module makes about standalone versus Fleet-managed agents.", "o": ["Elastic's documentation recommends standalone mode for advanced users only", "A managed agent that cannot reach Fleet Server keeps its last policy and keeps collecting", "Standalone mode removes the agent's inbound control channel, trading operability for a smaller attack surface", "Standalone agents receive policy revisions automatically"], "a": [0, 1, 2], "e": "ELK-01 Topic 3. Standalone agents are configured locally and get no automatic revisions — that is the trade."}, {"m": "ELK-01", "t": "single", "q": "Why does the module insist that an agent policy is a security concern and not just configuration?", "o": ["Because whoever can change a policy can run a new input on every enrolled host — it is a remote-execution channel", "Because policies are stored unencrypted", "Because policies cannot be version-controlled", "Because agents ignore invalid policies"], "a": [0], "e": "ELK-01 Topic 5, the same argument EXT-ANS Topic 1 makes about Ansible's control plane."}, {"m": "ELK-01", "t": "single", "q": "The lab dataset carries an epoch <code>_time</code> field rather than <code>@timestamp</code>. What happens if you send it to a data stream without the <code>oscd-epoch</code> pipeline?", "o": ["The documents are rejected — a data stream requires <code>@timestamp</code>", "They are indexed with the ingestion time as <code>@timestamp</code>", "They land in the <code>default</code> namespace", "Filebeat converts the field automatically"], "a": [0], "e": "ELK-01 Topic 6 and Lab 2: without <code>@timestamp</code> a document is not a valid data-stream document, which is why the one <code>date</code> processor is the first thing the lab creates."}, {"m": "ELK-01", "t": "multi", "q": "Which of these are in the free Basic tier, per the subscriptions page as the module read it?", "o": ["Fleet and Elastic Agent", "Ingest pipelines", "Index lifecycle management", "Elastic Defend endpoint protection"], "a": [0, 1, 2], "e": "ELK-01 Topic 7 and the series index: Defend, audit logging, SSO and most alerting connectors are paid; Fleet, pipelines, ILM, RBAC and TLS are free."}, {"m": "ELK-01", "t": "single", "q": "An agent reports healthy but its stream has had no documents for three hours. What does the module say this most likely is?", "o": ["A data problem — the source stopped generating, a file rotated, credentials expired, or documents are being rejected — because health is an agent statement and completeness is a data statement", "A Fleet Server outage", "Normal behaviour during policy revision", "A Kibana display bug"], "a": [0], "e": "ELK-01 Topic 8: silent sources are detected by querying <code>@timestamp</code> per stream per host, not by reading agent status."}, {"m": "ELK-01", "t": "single", "q": "What does an integration package contribute when it is added to a policy, according to the module?", "o": ["Index templates, ingest pipelines and dashboards for its data streams, plus the inputs", "Only the input configuration", "A new namespace", "A licence entitlement"], "a": [0], "e": "ELK-01 Topic 6: integrations \"ship with dashboards, visualizations, and data extraction pipelines\" — onboarding a source with a package is a policy edit; one without a package is engineering."}, {"m": "ELK-01", "t": "single", "q": "For a site whose link to the centre drops for days, what does the module say Elastic Agent alone does <em>not</em> solve?", "o": ["Reaching an Elasticsearch it cannot see — the SA-05 Topic 6 answer (a local tier or store-and-forward) applies to the output, not the agent", "Enrolment", "Timestamp parsing", "Namespace assignment"], "a": [0], "e": "ELK-01 Topic 3: a managed agent keeps its last policy and keeps collecting, but it cannot write to a cluster it cannot reach."}, {"m": "ELK-01", "t": "multi", "q": "Which controls does the module list for the Fleet control plane? Select all that apply.", "o": ["Short-lived or per-policy enrolment tokens, revoked on suspicion", "TLS to Fleet Server with a CA the agents trust, placed per SA-04 as a collector-tier service", "Least privilege on Kibana's Fleet and Integrations privileges, with change control on policy revisions", "Running Fleet Server on every workstation"], "a": [0, 1, 2], "e": "ELK-01 Topic 5's surface/threat/control table. Fleet Server is a designated host or hosts, not every endpoint."}, {"m": "ELK-02", "t": "single", "q": "Which of these can an ingest pipeline <em>not</em> do, according to Elastic's documentation as the module cites it?", "o": ["Split one incoming document into multiple documents", "Rename a field", "Set <code>@timestamp</code> from another field", "Enrich a document from an enrich index"], "a": [0], "e": "ELK-02 Topic 1: pipelines run one document at a time; they cannot split or aggregate (the <code>enrich</code> lookup is the one exception)."}, {"m": "ELK-02", "t": "single", "q": "Where does the module say an organisation-wide rule such as a tenant tag or a redaction belongs, and why?", "o": ["In <code>index.final_pipeline</code>, because it always runs and cannot be bypassed by a request parameter", "In the request parameter, because it is explicit", "In a Beats processor, because it runs earliest", "In a Painless script in each per-source pipeline"], "a": [0], "e": "ELK-02 Topic 2: <code>final_pipeline</code> runs after the default or request pipeline, always."}, {"m": "ELK-02", "t": "multi", "q": "Select every ECS rule the module quotes from the guidelines.", "o": ["Documents MUST have the <code>@timestamp</code> field", "Field names must be lower case, with underscores between words", "Use prefixes for all fields except the base fields, ordered from general to specific", "Custom fields are forbidden"], "a": [0, 1, 2], "e": "ELK-02 Topic 4: custom fields are permitted — \"add them to your events, using custom field names\" — subject to the naming rules."}, {"m": "ELK-02", "t": "single", "q": "The lab's <code>ids</code> source is given <code>event.kind: alert</code>, not <code>signal</code>. Why?", "o": ["<code>alert</code> is for detections made by a system external to the stack (an IDS); <code>signal</code> is reserved for alerts created by rules running inside Kibana", "<code>signal</code> is deprecated", "<code>alert</code> has higher severity", "They are interchangeable"], "a": [0], "e": "ELK-02 Topic 4, from the ECS <code>event.kind</code> allowed values; ELK-04's rule output is what gets <code>signal</code>."}, {"m": "ELK-02", "t": "single", "q": "Per the ECS reference as read, which <code>event.type</code> values does the <code>authentication</code> category expect?", "o": ["<code>start</code>, <code>end</code>, <code>info</code>", "<code>allowed</code>, <code>denied</code>", "<code>access</code>, <code>change</code>, <code>creation</code>, <code>deletion</code>", "<code>connection</code>, <code>protocol</code>"], "a": [0], "e": "ELK-02 Topic 4's table, from the ECS <code>event.category</code> allowed-values page."}, {"m": "ELK-02", "t": "single", "q": "Elasticsearch's built-in <code>logs-*-*</code> template has priority 100 and Fleet integrations use up to 200. Where does the module say the lab's <code>logs-oscd.*-lab</code> template must sit?", "o": ["Above 100 to own its streams, and below 200 if it must not shadow an integration — the lab uses 150", "Below 100 so the built-in wins", "Exactly 200", "Priority does not matter for data streams"], "a": [0], "e": "ELK-02 Topic 6: highest priority wins among matching templates."}, {"m": "ELK-02", "t": "single", "q": "You change a component template's mapping. What happens to the running backing index?", "o": ["Nothing until rollover — templates apply only at index or data-stream creation", "It is remapped in place", "It is reindexed automatically", "It becomes read-only"], "a": [0], "e": "ELK-02 Topic 6 and Lab 2 step 5: change the template, and existing backing indices keep their old mappings until the next rollover creates a new one."}, {"m": "ELK-02", "t": "multi", "q": "Which measurements does the module use for data quality on a running stream?", "o": ["Completeness — documents per stream against the source count", "Categorisation coverage — share of documents with <code>event.category</code> set", "Mapping growth — field count per backing index over time", "Average query latency"], "a": [0, 1, 2], "e": "ELK-02 Topic 8's three measurements. Query latency is a capacity concern (ELK-03), not a data-quality one."}, {"m": "ELK-02", "t": "single", "q": "In Lab 3 a rule-breaking regression (renaming <code>source.ip</code> to <code>src_ip</code>) passes both reconciliation and the coverage query. What test would have caught it?", "o": ["A golden simulate output per source, diffed on every change", "A larger sample", "A second reconciliation", "Disabling <code>on_failure</code>"], "a": [0], "e": "ELK-02 Lab 3 step 3 and Topic 7: pipelines are detection code; the test is a stored expected output, not a count."}, {"m": "ELK-02", "t": "single", "q": "Which processor does the module identify as where an APP 11 minimisation decision is implemented, and where should it run?", "o": ["<code>remove</code>, in the <code>final_pipeline</code> so no request can bypass it", "<code>set</code>, in the request pipeline", "<code>grok</code>, on the agent", "<code>enrich</code>, in the common pipeline"], "a": [0], "e": "ELK-02 Australian context: dropping fields the security use case does not need, with the pipeline definition as the evidence."}, {"m": "ELK-03", "t": "single", "q": "What shard size band does Elastic's guidance recommend, as the module cites it?", "o": ["10 GB to 50 GB, with fewer than 200 million documents per shard", "1 GB to 5 GB", "100 GB to 500 GB", "Any size below the node's heap"], "a": [0], "e": "ELK-03 Topic 4, from <em>Size your shards</em> as read on 2026-09-13."}, {"m": "ELK-03", "t": "single", "q": "Which tier depends on <em>partially</em> mounted searchable snapshots, and what licence does the searchable-snapshots page state it needs?", "o": ["Frozen; an Enterprise licence", "Warm; Basic", "Hot; Platinum", "Content; Gold"], "a": [0], "e": "ELK-03 Topic 2 and Topic 5: frozen uses partially mounted indices from the repository; the docs page says \"requires an Enterprise license\"."}, {"m": "ELK-03", "t": "multi", "q": "Select every ILM action the module lists.", "o": ["<code>rollover</code>", "<code>shrink</code>", "<code>forcemerge</code>", "<code>searchable_snapshot</code>"], "a": [0, 1, 2, 3], "e": "ELK-03 Topic 3 lists rollover, shrink, forcemerge, searchable_snapshot, migrate, allocate, readonly and delete."}, {"m": "ELK-03", "t": "single", "q": "On the free Basic tier, what does the module say the realistic tiers are, and what holds retention beyond them?", "o": ["Hot and warm; a snapshot repository, not a tier", "Hot, warm, cold and frozen", "Hot only", "Content only"], "a": [0], "e": "ELK-03 Topic 2: cold and frozen savings need searchable snapshots, so on Basic long retention goes to the repository."}, {"m": "ELK-03", "t": "single", "q": "In the capacity model, why does the module say the per-node shard limit often binds before disk on long-retention warm tiers?", "o": ["Because 1000 non-frozen shards per node is reached by shard count long before disk fills, unless <code>shrink</code> and <code>forcemerge</code> reduce the count", "Because warm nodes have small disks", "Because replicas are not allowed in warm", "Because ILM cannot run in warm"], "a": [0], "e": "ELK-03 Topic 4's warning and the worked example: 2,000 warm shards means at least three warm nodes on the limit alone."}, {"m": "ELK-03", "t": "single", "q": "What does the CCR documentation say is <em>not</em> replicated to the follower cluster?", "o": ["Security configuration — roles and users are a separate build", "Index mappings", "Documents", "ILM policies only"], "a": [0], "e": "ELK-03 Topic 5: \"security configuration is not replicated\"."}, {"m": "ELK-03", "t": "single", "q": "For requirement (b) in Lab 3 — survive a cluster loss with one hour of data loss and four hours of downtime — which mechanism does the module's reasoning support on Basic?", "o": ["Snapshot and restore with a 15–60 minute snapshot schedule", "Replica shards alone", "Cross-cluster replication", "Searchable snapshots"], "a": [0], "e": "ELK-03 Topic 5 and Lab 3: replicas do not survive cluster loss; CCR and searchable snapshots are paid. Snapshot-and-restore meets an RPO of one hour on Basic."}, {"m": "ELK-03", "t": "single", "q": "The module says residency on this platform is three questions. Which is the one people miss?", "o": ["Where the snapshot repository is — every restore and searchable snapshot reads from it", "Where Kibana runs", "Where the hot nodes are", "Where the licence is registered"], "a": [0], "e": "ELK-03 Australian context: nodes, repository, and (with CCR) the follower cluster."}, {"m": "ELK-03", "t": "multi", "q": "Select every control the module lists as free on the Basic tier for the cluster's own security.", "o": ["Transport (node-to-node) and HTTP encryption", "Role-based access control and API keys", "Audit logging", "SAML/OIDC single sign-on"], "a": [0, 1], "e": "ELK-03 Topic 8: audit logging and SSO are paid; the evidence pack states the gap."}, {"m": "ELK-03", "t": "single", "q": "What is the point of the \"decided / left to your architecture\" table in Topic 6?", "o": ["To separate what Elastic's production guidance settles (shard bands, tiers, roles) from what only the architecture can settle (sources, retention per obligation, residency, RTO/RPO) — the SA-05 Topic 12 reading method", "To list every Elastic default", "To justify buying a licence", "To compare Elastic with Splunk"], "a": [0], "e": "ELK-03 Topic 6."}, {"m": "ELK-04", "t": "single", "q": "Which rule type does the module say fits a password spray — many failed authentications from one source in a window?", "o": ["Threshold — the count is the detection, not the event", "Custom query", "Indicator match", "New terms"], "a": [0], "e": "ELK-04 Topic 1's table; Lab 2 step 2 builds it on <code>source.ip</code>."}, {"m": "ELK-04", "t": "multi", "q": "Select every EQL keyword the module describes for sequences.", "o": ["<code>by</code> — shared field values across events", "<code>with maxspan</code> — the time bound", "<code>until</code> — an expiration event", "<code>!</code> — a missing event"], "a": [0, 1, 2, 3], "e": "ELK-04 Topic 2, from the EQL reference."}, {"m": "ELK-04", "t": "single", "q": "Why does an EQL sequence require <code>event.category</code> on every document?", "o": ["Because the basic form is <code>[event_category] where [condition]</code>; without the field (or the <code>any</code> keyword) the query cannot address the event", "Because Kibana indexes on it", "Because it sets severity", "It does not; only <code>@timestamp</code> is required"], "a": [0], "e": "ELK-04 Topic 2 — and the reason ELK-02's categorisation was not optional."}, {"m": "ELK-04", "t": "single", "q": "What does the prebuilt-rules documentation say about installing, enabling and adding exceptions to prebuilt rules?", "o": ["They are \"available across all subscription levels\"; direct editing and update-conflict resolution are Enterprise", "They require Platinum", "They require Enterprise", "They are free only on Elastic Cloud"], "a": [0], "e": "ELK-04 Topic 4 — and the module records that the subscriptions comparison read differently, as an item to verify."}, {"m": "ELK-04", "t": "single", "q": "Under what licence are Elastic's prebuilt rules published in the <code>elastic/detection-rules</code> repository?", "o": ["Elastic License v2", "Apache 2.0", "MIT", "CC BY 4.0"], "a": [0], "e": "ELK-04 Topic 4: \"Everything in this repository — rules, code, etc. — is licensed under the Elastic License v2.\""}, {"m": "ELK-04", "t": "single", "q": "How does the module say tuning should be done, and why?", "o": ["With exceptions — \"source event conditions that determine when alerts shouldn't be generated\" — so the rule stays as shipped and the known-good is expressed once, surviving updates", "By editing the rule's query", "By lowering severity", "By disabling the rule during business hours"], "a": [0], "e": "ELK-04 Topic 5: tuning becomes data; prebuilt-rule updates \"preserve exceptions and tuning\"."}, {"m": "ELK-04", "t": "multi", "q": "Which <code>kibana.alert.*</code> fields does the module name on the alert document?", "o": ["<code>kibana.alert.rule.name</code>", "<code>kibana.alert.severity</code>", "<code>kibana.alert.risk_score</code>", "<code>kibana.alert.workflow_status</code>"], "a": [0, 1, 2, 3], "e": "ELK-04 Topic 7, from <em>View alert details</em>."}, {"m": "ELK-04", "t": "single", "q": "The module warns that severity and risk score are rule <em>attributes</em>. What follows?", "o": ["A triage queue sorted by them is sorted by the author's judgement, not by evidence — precision against ground truth is what tells you whether high severity means high precision", "They cannot be changed", "They are computed from the data", "They are ignored by cases"], "a": [0], "e": "ELK-04 Topic 7, echoing SPL-09's calibration argument."}, {"m": "ELK-04", "t": "single", "q": "In Lab 3, which exception does the module tell you to refuse to write?", "o": ["One that removes false positives by excluding the true positives' neighbours rather than by the actual benign cause", "One with an owner and a review date", "One in a shared list", "One for a scanner host"], "a": [0], "e": "ELK-04 Lab 3 step 2 and reflection 1: exceptions target causes (a service account, a scanner, a benign path), never the attack's surroundings."}, {"m": "ELK-04", "t": "multi", "q": "Which of these are among the seven detection rule types the module lists? Select all that apply.", "o": ["Threshold", "New terms", "ES|QL", "Machine learning (paid tier)"], "a": [0, 1, 2, 3], "e": "ELK-04 Topic 1's table; every lab uses custom rules on Basic."}, {"m": "ELK-05", "t": "single", "q": "From which Elasticsearch and Kibana version was OpenSearch forked, and under what licence is it released?", "o": ["7.10.2; Apache License 2.0", "8.0; Elastic License 2.0", "6.8; SSPL", "7.17; MIT"], "a": [0], "e": "ELK-05 Topic 1, from the OpenSearch FAQ."}, {"m": "ELK-05", "t": "multi", "q": "Select every compatibility statement the module quotes from the FAQ.", "o": ["Backward compatibility with Elasticsearch 7.10's REST APIs", "Can read indices from Elasticsearch versions 6.0–7.10", "Elastic-licensed features are not included", "Full compatibility with Elasticsearch 9.x indices"], "a": [0, 1, 2], "e": "ELK-05 Topic 2: 8.x and later indices are not directly readable; that is a reindex or Migration Assistant path."}, {"m": "ELK-05", "t": "single", "q": "What does the module call \"the portable layer\" between the two platforms?", "o": ["ECS — a stream shaped to ECS means the same query works on both and Security Analytics' field mapping is short", "Kibana saved objects", "Elastic Agent policies", "EQL rules"], "a": [0], "e": "ELK-05 Topic 2's design rule."}, {"m": "ELK-05", "t": "single", "q": "In Security Analytics, what is the difference between a finding and an alert?", "o": ["A finding is generated when a rule matches; an alert is a notification triggered by findings, by severity, to channels", "They are synonyms", "An alert is the raw event; a finding is its enrichment", "A finding is a correlation; an alert is a single rule match"], "a": [0], "e": "ELK-05 Topic 3, from the detector-configuration documentation."}, {"m": "ELK-05", "t": "single", "q": "Where does the module say migrations to Security Analytics \"fail quietly\"?", "o": ["Field mapping — a detector whose expected field is unmapped produces no findings and no error", "Index template priority", "The snapshot repository", "Dashboards import"], "a": [0], "e": "ELK-05 Topic 3 and Lab 2 reflection 1 — the ELK-04 source-applicability matrix enforced per detector."}, {"m": "ELK-05", "t": "multi", "q": "Which ISM actions does the module list? Select all that apply.", "o": ["<code>rollover</code>", "<code>replica_count</code>", "<code>force_merge</code>", "<code>snapshot</code>"], "a": [0, 1, 2, 3], "e": "ELK-05 Topic 4: rollover, replica_count, force_merge, read_only, delete, snapshot, allocation."}, {"m": "ELK-05", "t": "single", "q": "What structural difference between ISM and ILM does the module draw?", "o": ["ISM has arbitrary named states and transitions; ILM has fixed phases — and ISM has no licence line between tiers", "ISM cannot roll over", "ILM cannot delete", "ISM applies only to data streams"], "a": [0], "e": "ELK-05 Topic 4's comparison table."}, {"m": "ELK-05", "t": "single", "q": "For an Elasticsearch 8.x source, which migration paths does the module say apply?", "o": ["Reindex from remote, or the Migration Assistant — 8.x indices are not directly readable", "Snapshot and restore directly", "Rolling upgrade", "Copying the data directory"], "a": [0], "e": "ELK-05 Topic 6's table; snapshot and restore works for 6.x–7.10 sources."}, {"m": "ELK-05", "t": "multi", "q": "In the three-inventory migration method, which are the inventories? Select all that apply.", "o": ["Data — what must be readable on day one, and how much history", "Collection — every agent and beat, and its replacement", "Content — pipelines, templates, dashboards, rules", "Users, roles and spaces"], "a": [0, 1, 2], "e": "ELK-05 Topic 6 and Lab 3."}, {"m": "ELK-05", "t": "single", "q": "What is the module's \"honest summary\" of the three-platform comparison?", "o": ["The architecture — sources, placement, retention, boundaries — is the same on all three; the platform decides only how much is paid for, how much is engineered, and how hard it is to leave", "Splunk is best for security", "OpenSearch is always cheapest", "Elastic has no free tier"], "a": [0], "e": "ELK-05 Topic 8."}];
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
