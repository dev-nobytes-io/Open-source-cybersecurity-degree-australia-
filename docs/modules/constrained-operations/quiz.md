# EXT-DSO self-assessment quiz

> **Module type:** Extension series self-assessment — part of [EXT-DSO](index.md)
> **Status:** Draft
> **Version:** v0.1
> **Last Reviewed:** 2026-09-13

!!! warning "Not a credit-bearing unit"
    This quiz belongs to the [EXT-DSO series](index.md), an optional extension outside the
    168 CP degree structure. It carries **0 CP**, is not assessed, and does not appear in
    `docs/ksat-coverage.md`, which is generated from credit-bearing units only.

**40 questions across the four modules, ten per module.** Single-answer questions
have one correct option; **multiple-selection** questions (8 of the 40) have two or
more and are marked as such. Answer a question and press **Check** to reveal the
answer and the reasoning, or use **Check all** at the bottom. The module chips filter
the set; the score counts only the questions in view.

**How to use.** Every question is drawn from the text of one module:
[DSO-01](dso-01-monitoring-isolated-and-intermittent-sites.md),
[DSO-02](dso-02-autonomous-detection-content-offline-lifecycle.md),
[DSO-03](dso-03-rapid-deployment-teardown-and-sanitisation.md) or
[DSO-04](dso-04-validation-in-degraded-conditions.md). Each explanation names the
module and the topic heading the answer comes from, so a wrong answer points you at
the passage to re-read. Questions mix recall (what a source says), application (which
decision follows from a stated constraint) and judgement (which option the module
argues against, and why). Where a module marks an item as its own design reasoning or
as unverified, the quiz says so rather than testing it as fact; where a question
mentions an ISM identifier, it is the identifier the module cites from the September
2026 edition, every one of which the modules flag for re-verification, and no answer
turns on an identifier number.

!!! note "Nothing is recorded"
    Your answers stay in the browser and are not submitted anywhere. This is
    formative self-assessment, not the modules' graded work; the assessment
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
  var Q = [
{"m":"DSO-01","t":"single","q":"Which of DSO-01's four isolation classes is defined by the property that no link exists, or none is permitted, at any time, so the boundary is a person carrying media?","o":["Class I — intermittently connected","Class II — policy-isolated","Class III — physically disconnected","Class IV — OT-zoned"],"a":[2],"e":"DSO-01, <em>Four Classes of Isolation and What Each Forbids</em>. Class III is the physically disconnected site whose release point is media transfer with inspection at both ends. Class I has a trusted link that drops; Class II is a different security domain whose only exit is a gateway or cross domain solution; Class IV is an industrial control system zoned by safety and availability."},
{"m":"DSO-01","t":"single","q":"Per the ISM as DSO-01 restates it, what does the boundary ladder require where a SECRET or TOP SECRET domain is on either side of a boundary?","o":["A VLAN with a documented rationale","A gateway with an evaluated firewall and a DMZ","A cross domain solution, with ASD consulted and its directions followed","A unidirectional diode, evaluated at any assurance level"],"a":[2],"e":"DSO-01, Topic 1 and the danger admonition. Where SECRET or TOP SECRET is on either side, a cross domain solution is required (the module cites ISM-0626) and ASD must be consulted (ISM-0597). Gateways with evaluated firewalls are the rung for different domains below that level; VLANs are never the separator between domains."},
{"m":"DSO-01","t":"multi","q":"Which of these are among the six questions DSO-01 says every release-point design must answer? Select all that apply.","o":["What leaves","What enters","At what latency","Which vendor supplies the product","Logged where","Owned by whom"],"a":[0,1,2,4,5],"e":"DSO-01, <em>Release-Point Patterns</em>. The six questions are what leaves, what enters, latency, inspection, logged where and owner. The module is vendor-neutral and names no product for any release point."},
{"m":"DSO-01","t":"single","q":"What is the asymmetry rule DSO-01 states for release points in Classes II to IV?","o":["The inward path must carry at least as much as the outward path so that content stays current","The outward path carries less than the site holds, and the inward path carries only content and direction","Both paths carry the full local store so that the centre and site are always identical","The outward path is disabled during isolation"],"a":[1],"e":"DSO-01, <em>Release-Point Patterns</em>, the asymmetry rule. An isolated site is isolated because something on one side must not reach the other; a monitoring design that makes the boundary transparent to itself has defeated the boundary. Widen the release point only with a written reason."},
{"m":"DSO-01","t":"single","q":"DSO-01's Topic 4 decision rule for Class II sites is to monitor at the highest classification the data carries and release downward only what the transfer policy allows. How does the module characterise the status of that rule?","o":["A stated ISM control, cited by identifier","ASD's published position from its cross domain solution publications","An architectural inference from the ISM's isolated-path, protocol-break and independent-function controls, flagged for Practitioner Reviewer confirmation","A requirement of NIST SP 800-92"],"a":[2],"e":"DSO-01, <em>Monitoring Across a Cross Domain Solution</em> and the Verification status table. The rule is this module's inference from ISM-0635, ISM-1521 and ISM-1522; it is not a stated ISM position, and ASD's two introductory CDS publications were not read for the draft."},
{"m":"DSO-01","t":"multi","q":"Which of these does DSO-01 list among the ISM cross domain solution requirements that bear on monitoring flow? Select all that apply.","o":["Upward and downward data travel on isolated network paths","Each direction is enforced by its own independent security-enforcing functions","A protocol break at each network layer, so no session crosses intact","Federated search across the boundary is permitted provided it is encrypted","The CDS's own security events, including configuration changes, are centrally logged"],"a":[0,1,2,4],"e":"DSO-01, Topic 4. The module cites ISM-0635 (isolated paths), ISM-1522 (independent functions), ISM-1521 (protocol breaks) and ISM-0670 (central logging). Federation needs a session that the protocol-break control forbids; correlation across the pair happens by people, not by federation."},
{"m":"DSO-01","t":"single","q":"In DSO-01's threat model for the content-import path, a bundle replayed from months ago to roll the site's detections back is defeated primarily by which step?","o":["Identity of the sender","Version discipline: a monotonic version, with the site refusing anything older than current and recording the gap","Media scanning on a dedicated host","Quarantine before activation"],"a":[1],"e":"DSO-01, <em>The Content-Import Path as an Attack Surface</em>. The version row exists for the replay threat; identity and inspection address other rows of the threat model. A design that cannot say which row defeats which threat is incomplete."},
{"m":"DSO-01","t":"single","q":"What is the first of DSO-01's six design rules for an operational-technology site?","o":["Deploy a lightweight agent on every controller so that coverage is complete","Passive first: collect by tap or span port to a sensor that parses OT protocols; no agents on controllers and no active scanning of anything that talks to a physical process","Route the control zone into the corporate SIEM over the existing IT network","Use the corporate time source for the control zone"],"a":[1],"e":"DSO-01, <em>Operational-Technology Sites</em>, rule 1, drawing on ASD's guidance (via SA-05 Topic 9) that direct logging from OT assets must be conservative and tested because of safety-critical deterministic messaging. Rules 3 and 6 contradict the third and fourth options."},
{"m":"DSO-01","t":"single","q":"DSO-01's operating model names three roles per occupied shift. Which separation does it require between the release-point custodian and the site watcher?","o":["They must never be the same person under any circumstances","They may be the same person, but not for the same transfer, so that no one both creates and carries an outward bundle unchecked","The custodian must outrank the watcher","The watcher must approve every transfer the custodian makes"],"a":[1],"e":"DSO-01, <em>The Operating Model for a Site Nobody Central Can Reach</em>. One person can hold two roles on a small site if the stated separation holds; the summative marks whether the candidate saw the conflict."},
{"m":"DSO-01","t":"single","q":"How does DSO-01 say the drift budget for an isolated site's time holdover should be set?","o":["From the manufacturer's stated oscillator accuracy alone","From the tightest correlation window in the local detection set, so that drift across sources stays well inside it","At a fixed one hour for all sites","It is not needed if the site has a satellite link"],"a":[1],"e":"DSO-01, <em>Time, Identity and Trust Anchors Without a Link</em>. The budget is derived from the tightest correlation window; the holdover source's expected drift per day then gives the isolation length after which local correlation is no longer trustworthy, recorded as residual risk, and the offset is measured at reconnection before events are released."},
{"m":"DSO-02","t":"single","q":"Under DSO-02's Topic 1 criteria, which combination makes a rule local-mandatory for a site?","o":["Its <code>level</code> is <code>critical</code>, regardless of whether the site has the log source","The log source exists at the site, a true positive requires a response the site decider may take, the level is <code>high</code> or <code>critical</code>, and no enrichment the site lacks is needed","It has <code>status: experimental</code> and the site has spare compute","It needs organisation-wide baselines"],"a":[1],"e":"DSO-02, <em>Which Detections Must Run Locally</em>. A critical rule for a source the site lacks is central-only; level is necessary, not sufficient; response authority is part of the criterion; organisation-wide baselines make a rule central-only."},
{"m":"DSO-02","t":"single","q":"By default, which Sigma <code>status</code> values does DSO-02 ship to Class II and Class III sites?","o":["<code>stable</code> only","<code>stable</code> and <code>test</code>","<code>stable</code>, <code>test</code> and <code>experimental</code>","All statuses, since the site's watcher can tune"],"a":[1],"e":"DSO-02, <em>The Rule as a Lifecycle Object</em>. An isolated site's watcher cannot ask whether an alert is trustworthy, so <code>status</code> travels with the rule; the module ships only <code>stable</code> (may be used in production) and <code>test</code> (mostly stable) by default."},
{"m":"DSO-02","t":"single","q":"According to the Sigma rules specification as DSO-02 cites it, when must a rule receive a new <code>id</code>?","o":["On every commit","On a major change to the logic, on derivation, and on merging","Only when it is renamed","Never; identifiers are permanent"],"a":[1],"e":"DSO-02, Topic 2, from specification v2.1.0. The module adds that the old rule must then ship once more as <code>deprecated</code> with the new rule's <code>related</code> entry pointing back, because a site receiving one without the other has either a duplicate or a gap."},
{"m":"DSO-02","t":"multi","q":"Which of these are valid <code>related</code> types in the Sigma rules specification as DSO-02 lists them? Select all that apply.","o":["<code>derived</code>","<code>obsolete</code>","<code>superseded</code>","<code>merged</code>","<code>renamed</code>","<code>similar</code>"],"a":[0,1,3,4,5],"e":"DSO-02, Topic 2. The five types are derived, obsolete, merged, renamed and similar. <code>superseded</code> is not one; the specification expresses that relationship with <code>obsolete</code>."},
{"m":"DSO-02","t":"single","q":"Which fields does the Sigma correlation rules specification make mandatory inside the <code>correlation</code> attribute, per DSO-02?","o":["<code>type</code>, <code>rules</code>, <code>group-by</code>, <code>timespan</code>, <code>condition</code>","<code>type</code>, <code>rules</code>, <code>aliases</code>, <code>generate</code>","<code>rules</code> and <code>timespan</code> only","<code>type</code>, <code>level</code>, <code>status</code>"],"a":[0],"e":"DSO-02, <em>Correlation Rules and Their Limits Offline</em>, from the correlation specification v2.1.0. <code>aliases</code> and <code>generate</code> are optional."},
{"m":"DSO-02","t":"single","q":"Why does DSO-02 say a correlation the site's backend cannot execute is <em>known</em> before it ships?","o":["Because the site reports it after activation","Because the correlation specification requires backends to raise an error for a mandatory feature they cannot convert, and conversion is done centrally per site","Because all backends support all correlation types","Because the site profile forbids correlations"],"a":[1],"e":"DSO-02, Topic 3. The backend obligation plus per-site central conversion (Topic 4) means a failed conversion is recorded in the site profile as Unsupported at site, the constituent rules are classified on their own merits, and the correlation runs centrally on released findings."},
{"m":"DSO-02","t":"single","q":"Where does DSO-02 say conversion of Sigma rules for an isolated site should run, and what ships as a result?","o":["On the site, so that queries match its backend; only the queries ship","Centrally, per site, in the release build; the source rule, the site's versioned pipeline(s), the converted query and the converter version all ship","At the cross domain solution","Nowhere; the site runs Sigma natively"],"a":[1],"e":"DSO-02, <em>Pipelines and Per-Site Conversion</em>. The site's stack is compute-constrained and may not carry the toolchain; the centre can fail the build when a rule does not convert; a site that receives only queries cannot audit them and one that receives only rules cannot run them."},
{"m":"DSO-02","t":"single","q":"What is the design consequence DSO-02 draws from TAXII 2.1 being an HTTPS protocol that defines no offline exchange?","o":["The site must have a TAXII client and a scheduled link","The site consumes STIX 2.1 bundles delivered through the import path; TAXII is how the centre collects, not how the site receives","Threat intelligence is not used at isolated sites","Indicators are typed in by the watcher"],"a":[1],"e":"DSO-02, <em>Threat Intelligence Without a Feed</em>. STIX's Bundle is defined for transporting content over non-TAXII mechanisms; the centre selects, bounds validity, and the site measures staleness and ages indicators out locally."},
{"m":"DSO-02","t":"multi","q":"Which statements about DSO-02's content bundle are correct? Select all that apply.","o":["The exceptions file ships so that activation does not revert the site's own tuning","Parsers and field mappings ship because a rule that arrives before its parser silently never fires","The notes are written for machines and the manifest for the watcher","A failed activation test blocks the whole bundle by default, and a per-rule override is logged and released"],"a":[0,1,3],"e":"DSO-02, <em>The Content Bundle</em>. The manifest is for machines and the notes are for the watcher, the reverse of the third option. The other three are stated in the bundle table and the activation paragraph."},
{"m":"DSO-02","t":"single","q":"Under DSO-02's merge policy, what happens to a rule authored at the site during isolation?","o":["It is discarded, because the site is not an author","It replaces the central rule immediately","It enters the central repository as <code>experimental</code> with <code>related: derived</code> where it came from an existing rule, goes through review, and returns under a new central <code>id</code> with <code>related: renamed</code> pointing at the site's","It is merged into the global rule set as <code>stable</code>"],"a":[2],"e":"DSO-02, <em>Drift, Return and the Site as an Author</em>. The site is an author with a narrower view; its exceptions merge into the site profile, its rules are proposals, and nothing site-authored is discarded silently."},
{"m":"DSO-03","t":"single","q":"DSO-03 builds the site stack from five layers. Which layer must contain nothing site-specific?","o":["Site configuration","Trust anchors","Base image","Registers"],"a":[2],"e":"DSO-03, <em>Build to Image with Pre-Staged Configuration</em>. The base image is the hardened operating system and components with no site-specific data; Lab 1 treats any site-specific content in it as a defect to move."},
{"m":"DSO-03","t":"multi","q":"Which of these does DSO-03 say are deliberately <em>not</em> in the site image? Select all that apply.","o":["Private keys other than the site's own, sealed at staging","Any data from a previous site","Any credential that would let the image reach the centre if stolen in transit","The current content bundle for the site profile"],"a":[0,1,2],"e":"DSO-03, Topic 2. The content bundle is one of the five layers and is pre-staged; keys, prior-site data and centre-reaching credentials are excluded so that a stolen image is worthless."},
{"m":"DSO-03","t":"single","q":"Which of DSO-03's six acceptance checks proves pipeline health is visible?","o":["Every source emits and lands","Every local-mandatory detection fires","Silence one source deliberately and confirm the silent-source alert appears within the configured window","The roles have logged in"],"a":[2],"e":"DSO-03, <em>Deployment Verification and Handover</em>, check 4. A failed check is a defect against the image or configuration, fixed centrally and redeployed, never patched by hand on site."},
{"m":"DSO-03","t":"single","q":"Under the ISM control DSO-03 cites, what happens to a medium connected to a system of higher sensitivity than the medium, and what design consequence does the module draw?","o":["Nothing, provided the medium is encrypted","It is reclassified to the higher sensitivity unless it is read-only or the system enforces read-only access; so the site's import host enforces read-only access for inbound media","It is destroyed immediately","It is returned to the depot for relabelling"],"a":[1],"e":"DSO-03, <em>Removable Media in Operation</em>, citing ISM-0325. Inbound content media therefore does not take the site's classification; outward media does, and is planned for."},
{"m":"DSO-03","t":"single","q":"For manual data transfers between systems in different security domains, what does the ISM expect of the media, as DSO-03 restates it?","o":["Any media, provided it is labelled","Write-once media unless the destination enforces read-only access; rewritable media sanitised after each transfer","Encrypted media only, with no other requirement","Media supplied by the destination system's owner"],"a":[1],"e":"DSO-03, Topic 4, citing ISM-0347 and ISM-0947. The write-once decision and the time cost of sanitise-after-transfer are Lab 3's step 3."},
{"m":"DSO-03","t":"single","q":"In DSO-03's teardown runbook, which step must come before running any automation against a host?","o":["Revoking the site's certificates","Reconciling the registers","Preserving evidence for open cases in a forensically defensible way, because automation changes the host","Producing the final release bundle"],"a":[2],"e":"DSO-03, <em>The Teardown Runbook</em>, step 2, drawing on EXT-ANS Topic 7. The two failure modes the order is designed against are automation before evidence and media before bundle."},
{"m":"DSO-03","t":"multi","q":"Which statements reflect NIST SP 800-88 Rev. 2 as DSO-03 reads it? Select all that apply.","o":["The sanitisation decision is based on the confidentiality of the information rather than the type of media","Purge should be used instead of clear when possible","Degaussing is not appropriate for flash media and is not currently a destroy technique even when it renders media inoperable","Rev. 2 requires three overwrite passes for the clear method"],"a":[0,1,2],"e":"DSO-03, <em>Sanitisation as an Architectural Obligation</em>. Rev. 2's change log states that multi-pass overwrite is not needed for clear, so the fourth option is the reverse of the source."},
{"m":"DSO-03","t":"single","q":"What does the ISM say about SECRET and TOP SECRET non-volatile flash memory after sanitisation, and what does DSO-03 conclude for a temporary site?","o":["It may be reclassified to OFFICIAL after two overwrites; reuse anywhere","It retains its classification; the teardown plan is therefore sanitise, keep as classified, and either redeploy within the same domain or destroy","It must be degaussed","It may be reused after a formal administrative decision alone"],"a":[1],"e":"DSO-03, Topic 6, citing ISM-0359 for the technique and ISM-0360 for retained classification. A site that stands up SECRET on cheap flash it intended to reuse elsewhere has made its teardown impossible; choose removable, registered, destroyable media and budget for destruction."},
{"m":"DSO-03","t":"single","q":"How does SP 800-88 Rev. 2 distinguish verification from validation, per DSO-03?","o":["They are synonyms","Verification inspects the outcome of the technique (tool completion status, errors, media health); validation is the decision, against the sensitivity of the data, to accept the sanitisation or repeat or escalate it","Verification is performed by the vendor; validation by the organisation","Validation is full sampling of the media contents"],"a":[1],"e":"DSO-03, Topic 6. The ISM's read back for verification is the verification step; the validation decision is the custodian's, recorded per medium. Rev. 2 states that elaborate sampling is not necessary unless policy requires it."},
{"m":"DSO-03","t":"single","q":"Per the ISM controls DSO-03 cites, what supervision does the destruction of media storing accountable material require, and may it be outsourced?","o":["One cleared person; outsourcing permitted to any certified service","At least two cleared personnel who sign a destruction certificate afterwards; it is not outsourced","No supervision if approved equipment is used","Supervision by ASD"],"a":[1],"e":"DSO-03, <em>Destruction, Supervision and Disposal</em>, citing ISM-0372, ISM-0373 and ISM-0839. Non-accountable material may go to a NAID AAA certified service with the endorsements ASIO specifies (ISM-0840)."},
{"m":"DSO-04","t":"single","q":"Which of these is <em>within</em> DSO-04's stated scope?","o":["Whether a detection's logic is correct","Where an adversary would find detection gaps","The cross domain solution's own bypass testing","Whether the site's pipeline and the operating model's decisions hold while the site is cut off, partial, late or wrong"],"a":[3],"e":"DSO-04, <em>What Validation Means for an Isolated Site</em>. Detection logic is DE04, adversary coverage is CE04, and the CDS has its own ISM testing regime; a drill plan that claims more is marked down in the summative."},
{"m":"DSO-04","t":"multi","q":"Which of these are in DSO-04's proposed steady-state set? Select all that apply.","o":["Source throughput per class per interval","Detection latency for a known-good probe detection","CPU utilisation of the site node","Silent-source count","Clock offset against the centre at reconnection"],"a":[0,1,3,4],"e":"DSO-04, <em>Steady State and the Hypothesis Form</em>. The set is built from measurable outputs rather than internal attributes, following the chaos-engineering principles; CPU utilisation is an internal attribute and is not in the set."},
{"m":"DSO-04","t":"single","q":"What is DSO-04's required form for a validation hypothesis?","o":["\"The site keeps working under failure F\"","\"Under failure F, output O stays within bound B for duration D, and the pipeline-health telemetry reports F within time T\"","\"Failure F is unlikely at this site\"","\"The watcher will notice failure F\""],"a":[1],"e":"DSO-04, Topic 2. A hypothesis without a bound is not a hypothesis, and \"the site keeps working\" is not a bound."},
{"m":"DSO-04","t":"single","q":"How does NIST SP 800-84 define a tabletop exercise, as DSO-04 quotes it?","o":["A discussion-based exercise in which a facilitator presents a scenario and participants discuss roles, responsibilities, coordination and decisions, without deploying equipment","An exercise in which personnel perform their duties in a simulated operational environment","A test with quantifiable metrics in an operational environment","A training session on the incident response plan"],"a":[0],"e":"DSO-04, Topic 1. The second option is the functional exercise; the third is a test. DSO-04 uses each type for what it alone can prove."},
{"m":"DSO-04","t":"single","q":"Which example does SP 800-84 give of a test, as DSO-04 cites it?","o":["Reviewing the plan with the executive team","Removing power from a system or system component","Presenting a scenario to a breakout group","Reading the after-action report of a previous exercise"],"a":[1],"e":"DSO-04, Topic 1, quoting the definition of tests as evaluation tools using quantifiable metrics to validate operability in an operational environment, with removing power given as an example."},
{"m":"DSO-04","t":"single","q":"Which two failures does DSO-04 rate rare but high impact, and why?","o":["Link loss and collector loss, because they are frequent","Time drift and content failure, because they corrupt what the site believes, not just what it holds","Power loss and people failure, because they are unmeasurable","Release-point failure and link loss, because the courier is unreliable"],"a":[1],"e":"DSO-04, <em>The Failure Catalogue</em>. Link and collector loss are frequent and low-impact if the design is right; time drift and content failure corrupt the site's beliefs and are prioritised accordingly."},
{"m":"DSO-04","t":"single","q":"How does DSO-04 propose measuring data loss on a site that has no centre to compare against?","o":["By asking the centre after reconnection","By a probe generator emitting synthetic events with a monotonic sequence number, generation timestamp and signature, so the local store can compute missing, reordered and duplicated sequence numbers itself","By trusting the daily digest chain","By counting alerts"],"a":[1],"e":"DSO-04, <em>Measuring Latency and Loss Without a Centre</em>. The digest chain proves integrity of what was retained, never completeness of what was generated; the probe supplies the local ground truth."},
{"m":"DSO-04","t":"single","q":"Which reporting rule does DSO-04 set for latency and loss metrics?","o":["Report the mean, because it is stable","Report distributions, not means, and count undetected and lost events in their own column rather than folding them into an average","Report only the maximum","Report a pass or fail per failure"],"a":[1],"e":"DSO-04, Topic 4. SA-05 and the Splunk detection-analytics module show why a mean over heavy-tailed, seasonal data misleads; the lab dataset is built to make the lesson unavoidable."},
{"m":"DSO-04","t":"multi","q":"Which guard rails does DSO-04 place on validation at a live site? Select all that apply.","o":["Continuous tests observe only and never inject failures","No injection during an open case without the site decider's approval","No injection in an OT zone without the engineering authority","No injection against the cross domain solution at all","Injections may run unannounced to test whether the watcher is paying attention"],"a":[0,1,2,3],"e":"DSO-04, <em>Continuous Validation on Site</em>. Failure injection is a scheduled test with an owner, a stated blast radius and a rollback; SA-05 Lab 4 already asks who must approve an unannounced active test."},
{"m":"DSO-04","t":"single","q":"Under DSO-04, where do the changes proposed by an after-action report flow?","o":["All to the site decider","Design changes to the DSO-01 package, content changes to the DSO-02 bundle, build changes to the DSO-03 image, action-list changes to the site decider, and residual-risk changes to SA-06","All to the central SOC manager","They are filed with the report and revisited annually"],"a":[1],"e":"DSO-04, <em>Drills in the SP 800-84 Form</em>. The report is the document that makes a drill worth running; a drill without one is an outage the site chose."},
  ];
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
