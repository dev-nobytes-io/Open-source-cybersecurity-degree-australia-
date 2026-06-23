# Program Builder

Tick the courses you want — from a designed-degree preset, one or more majors, or any individual mix — and the **NICE/DCWF work-role completion** bars and the four **KSAT coverage** radar ("spider web") charts update live. Everything runs in your browser; nothing to install or rebuild.

> KSAT IDs are project-local (provisional) pending Framework Custodian mapping to official NICE/DCWF identifiers. The dataset embedded in this page is refreshed by `.github/scripts/program_builder.py` whenever unit content changes. Underlying coverage detail: [`../ksat-coverage.md`](../ksat-coverage.md).
<style>
.pb-app{--pb-sel:#7e57c2;}
.pb-grid{display:grid;grid-template-columns:340px 1fr;gap:1.4rem;align-items:start;}
@media(max-width:900px){.pb-grid{grid-template-columns:1fr;}}
.pb-app input[type=search]{width:100%;padding:.45rem .6rem;margin:.2rem 0 .6rem;border:1px solid #cfd4da;border-radius:6px;font-size:.85rem;}
.pb-presets{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:.6rem;}
.pb-btn{font-size:.72rem;padding:.28rem .5rem;border:1px solid var(--pb-sel);background:transparent;color:var(--pb-sel);border-radius:14px;cursor:pointer;}
.pb-btn:hover{background:var(--pb-sel);color:#fff;}
.pb-btn-clear{border-color:#b0bec5;color:#607d8b;}
.pb-tree{max-height:560px;overflow:auto;border:1px solid #e3e6ea;border-radius:8px;padding:.4rem .6rem;}
.pb-deg{margin:.2rem 0;}
.pb-deg>summary{cursor:pointer;font-weight:700;list-style:none;display:flex;align-items:center;gap:.4rem;padding:.25rem 0;}
.pb-deg>summary::-webkit-details-marker{display:none;}
.pb-deg-name{flex:0 0 auto;}
.pb-count{margin-left:auto;font-size:.7rem;color:#78909c;font-weight:600;}
.pb-year{font-size:.7rem;text-transform:uppercase;letter-spacing:.04em;color:#90a4ae;margin:.5rem 0 .1rem;}
.pb-area{margin:.1rem 0 .3rem .2rem;}
.pb-area-h{display:flex;align-items:center;gap:.4rem;font-weight:600;font-size:.8rem;cursor:pointer;}
.pb-unit{display:flex;align-items:center;gap:.4rem;font-size:.8rem;padding:.08rem 0 .08rem 1.3rem;cursor:pointer;}
.pb-unit:hover{background:rgba(126,87,194,.07);border-radius:4px;}
.pb-code{font-weight:600;flex:0 0 auto;min-width:3.2em;}
.pb-title{color:#546e7a;}
.pb-summary{font-size:.92rem;margin:.2rem 0 1rem;padding:.5rem .7rem;background:rgba(126,87,194,.08);border-radius:8px;}
.pb-bar-row{display:flex;align-items:center;gap:.5rem;margin:.18rem 0;font-size:.78rem;}
.pb-bar-label{flex:0 0 6.5em;font-weight:600;}
.pb-bar-track{flex:1 1 auto;height:14px;background:#eceff1;border-radius:7px;overflow:hidden;}
.pb-bar-fill{height:100%;background:var(--pb-sel);border-radius:7px;transition:width .25s;}
.pb-bar-fill.pb-bar-zero{background:#cfd8dc;}
.pb-bar-pct{flex:0 0 2.8em;text-align:right;font-variant-numeric:tabular-nums;color:#546e7a;}
.pb-radars{display:grid;grid-template-columns:repeat(2,1fr);gap:.4rem;}
@media(max-width:560px){.pb-radars{grid-template-columns:1fr;}}
.pb-radar{width:100%;height:auto;color:#455a64;}
.pb-donut-wrap{display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap;}
.pb-donut{width:130px;height:130px;color:#37474f;}
.pb-legend{display:flex;flex-direction:column;gap:.25rem;font-size:.8rem;}
.pb-legend-item{display:flex;align-items:center;}
.pb-swatch{display:inline-block;width:.8em;height:.8em;border-radius:2px;margin-right:.4rem;}
[data-md-color-scheme=slate] .pb-tree{border-color:#37474f;}
[data-md-color-scheme=slate] .pb-bar-track{background:#37474f;}
</style>
<div class="pb-app" markdown="0">
<div class="pb-grid">
<div class="pb-controls">
<input id="pb-search" type="search" placeholder="Search courses by code or title…" aria-label="Search courses">
<div id="pb-presets" class="pb-presets"></div>
<div id="pb-tree" class="pb-tree"></div>
</div>
<div class="pb-output">
<div id="pb-summary" class="pb-summary"></div>
<h3>NICE/DCWF work-role completion</h3>
<div id="pb-bars"></div>
<h3>KSAT coverage by domain</h3>
<div id="pb-radars" class="pb-radars"></div>
<h3>KSAT composition</h3>
<div id="pb-donut"></div>
</div>
</div>
</div>
<script>window.PROGRAM_DATA={"units":[{"code":"F01","title":"Networking Fundamentals","prefix":"F","degree":"Shared Core","year":"Year 1 · Foundation","area":"Foundation","k":3,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"F02","title":"Operating Systems & Administration","prefix":"F","degree":"Shared Core","year":"Year 1 · Foundation","area":"Foundation","k":3,"s":2,"a":2,"t":2,"roles":[["OM-ADM-001","System Administrator"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"F03","title":"Scripting & Automation","prefix":"F","degree":"Shared Core","year":"Year 1 · Foundation","area":"Foundation","k":4,"s":2,"a":2,"t":2,"roles":[["SP-DEV-001","Software Developer"],["OM-ADM-001","System Administrator"]]},{"code":"F04","title":"Security Concepts & Principles","prefix":"F","degree":"Shared Core","year":"Year 1 · Foundation","area":"Foundation","k":4,"s":2,"a":2,"t":2,"roles":[["SP-RSK-002","Security Control Assessor"],["OV-MGT-001","Information Systems Security Manager"]]},{"code":"F05","title":"Legal, Ethics & Australian Compliance","prefix":"F","degree":"Shared Core","year":"Year 1 · Foundation","area":"Foundation","k":4,"s":2,"a":2,"t":2,"roles":[["OV-LGA-001","Cyber Legal Advisor"],["OV-LGA-002","Privacy Officer/Privacy Compliance Manager"]]},{"code":"F06","title":"Data & Log Analysis","prefix":"F","degree":"Shared Core","year":"Year 1 · Foundation","area":"Foundation","k":3,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"OC01","title":"Adversary Tradecraft & TTPs","prefix":"OC","degree":"Shared Core","year":"Year 2 · Operational Core","area":"Operational Core","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"],["AN-TWA-001","Threat/Warning Analyst"]]},{"code":"OC02","title":"Security Monitoring & SIEM","prefix":"OC","degree":"Shared Core","year":"Year 2 · Operational Core","area":"Operational Core","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"OC03","title":"Malware Analysis Fundamentals","prefix":"OC","degree":"Shared Core","year":"Year 2 · Operational Core","area":"Operational Core","k":4,"s":2,"a":2,"t":2,"roles":[["IN-FOR-002","Cyber Defense Forensics Analyst"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"OC04","title":"Incident Response Lifecycle","prefix":"OC","degree":"Shared Core","year":"Year 2 · Operational Core","area":"Operational Core","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CIR-001","Cyber Defense Incident Responder"]]},{"code":"OC05","title":"Threat Intelligence Fundamentals","prefix":"OC","degree":"Shared Core","year":"Year 2 · Operational Core","area":"Operational Core","k":4,"s":2,"a":2,"t":2,"roles":[["AN-TWA-001","Threat/Warning Analyst"],["AN-ASA-001","All-Source Analyst"]]},{"code":"OC06","title":"Offensive Security Concepts","prefix":"OC","degree":"Shared Core","year":"Year 2 · Operational Core","area":"Operational Core","k":4,"s":2,"a":2,"t":2,"roles":[["PR-VAM-001","Vulnerability Assessment Analyst"],["AN-EXP-001","Exploitation Analyst"]]},{"code":"SC01","title":"Risk Management Frameworks","prefix":"SC","degree":"Shared Core","year":"Year 2 · Strategic Core","area":"Strategic Core","k":4,"s":2,"a":2,"t":2,"roles":[["SP-RSK-002","Security Control Assessor"],["OV-MGT-001","Information Systems Security Manager"]]},{"code":"SC02","title":"Security Architecture Principles","prefix":"SC","degree":"Shared Core","year":"Year 2 · Strategic Core","area":"Strategic Core","k":4,"s":2,"a":2,"t":2,"roles":[["SP-ARC-002","Security Architect"],["SP-ARC-001","Enterprise Architect"]]},{"code":"SC03","title":"Governance, Policy & Compliance","prefix":"SC","degree":"Shared Core","year":"Year 2 · Strategic Core","area":"Strategic Core","k":4,"s":2,"a":2,"t":2,"roles":[["OV-SPP-001","Cyber Policy & Strategy Planner"],["SP-RSK-002","Security Control Assessor"]]},{"code":"SC04","title":"Vendor & Supply Chain Risk","prefix":"SC","degree":"Shared Core","year":"Year 2 · Strategic Core","area":"Strategic Core","k":4,"s":2,"a":2,"t":2,"roles":[["SP-RSK-002","Security Control Assessor"],["OV-SPP-001","Cyber Policy & Strategy Planner"]]},{"code":"SC05","title":"Security Program Management","prefix":"SC","degree":"Shared Core","year":"Year 2 · Strategic Core","area":"Strategic Core","k":4,"s":2,"a":2,"t":2,"roles":[["OV-MGT-001","Information Systems Security Manager"],["OV-SPP-001","Cyber Policy & Strategy Planner"]]},{"code":"SC06","title":"Stakeholder Communication","prefix":"SC","degree":"Shared Core","year":"Year 2 · Strategic Core","area":"Strategic Core","k":4,"s":2,"a":2,"t":2,"roles":[["OV-SPP-001","Cyber Policy & Strategy Planner"],["PR-CIR-001","Cyber Defense Incident Responder"]]},{"code":"TH01","title":"Hunting Methodology & Process","prefix":"TH","degree":"Operational","year":"Year 3 · Specialisation","area":"Threat Hunting","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"],["AN-TWA-001","Threat/Warning Analyst"]]},{"code":"TH02","title":"ATT&CK for Hunters","prefix":"TH","degree":"Operational","year":"Year 3 · Specialisation","area":"Threat Hunting","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"],["AN-TWA-001","Threat/Warning Analyst"]]},{"code":"TH03","title":"Host-Based Hunting","prefix":"TH","degree":"Operational","year":"Year 3 · Specialisation","area":"Threat Hunting","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"],["IN-FOR-002","Cyber Defense Forensics Analyst"]]},{"code":"TH04","title":"Network-Based Hunting","prefix":"TH","degree":"Operational","year":"Year 3 · Specialisation","area":"Threat Hunting","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"TH05","title":"Hunt Operations & Tooling","prefix":"TH","degree":"Operational","year":"Year 3 · Specialisation","area":"Threat Hunting","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"TH06","title":"Capstone — Hunt Operation","prefix":"TH","degree":"Operational","year":"Year 3 · Specialisation","area":"Threat Hunting","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"DF01","title":"DFIR Process & Legal Foundations","prefix":"DF","degree":"Operational","year":"Year 3 · Specialisation","area":"DFIR","k":4,"s":2,"a":2,"t":2,"roles":[["IN-FOR-002","Cyber Defense Forensics Analyst"],["IN-INV-001","Cyber Crime Investigator"]]},{"code":"DF02","title":"Host Forensics","prefix":"DF","degree":"Operational","year":"Year 3 · Specialisation","area":"DFIR","k":4,"s":2,"a":2,"t":2,"roles":[["IN-FOR-002","Cyber Defense Forensics Analyst"]]},{"code":"DF03","title":"Memory Forensics","prefix":"DF","degree":"Operational","year":"Year 3 · Specialisation","area":"DFIR","k":4,"s":2,"a":2,"t":2,"roles":[["IN-FOR-002","Cyber Defense Forensics Analyst"]]},{"code":"DF04","title":"Network Forensics","prefix":"DF","degree":"Operational","year":"Year 3 · Specialisation","area":"DFIR","k":4,"s":2,"a":2,"t":2,"roles":[["IN-FOR-002","Cyber Defense Forensics Analyst"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"DF05","title":"Incident Response Operations","prefix":"DF","degree":"Operational","year":"Year 3 · Specialisation","area":"DFIR","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CIR-001","Cyber Defense Incident Responder"],["IN-INV-001","Cyber Crime Investigator"]]},{"code":"DF06","title":"Capstone — IR Simulation","prefix":"DF","degree":"Operational","year":"Year 3 · Specialisation","area":"DFIR","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CIR-001","Cyber Defense Incident Responder"],["IN-FOR-002","Cyber Defense Forensics Analyst"]]},{"code":"CT01","title":"Intelligence Tradecraft","prefix":"CT","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Intelligence","k":4,"s":2,"a":2,"t":2,"roles":[["AN-TWA-001","Threat/Warning Analyst"],["AN-ASA-001","All-Source Analyst"]]},{"code":"CT02","title":"Threat Actor Research & Profiling","prefix":"CT","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Intelligence","k":4,"s":2,"a":2,"t":2,"roles":[["AN-TWA-001","Threat/Warning Analyst"],["AN-ASA-001","All-Source Analyst"]]},{"code":"CT03","title":"Technical Intelligence","prefix":"CT","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Intelligence","k":4,"s":2,"a":2,"t":2,"roles":[["AN-ASA-001","All-Source Analyst"],["AN-TWA-001","Threat/Warning Analyst"]]},{"code":"CT04","title":"Strategic Intelligence","prefix":"CT","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Intelligence","k":4,"s":2,"a":2,"t":2,"roles":[["AN-ASA-001","All-Source Analyst"],["AN-TWA-001","Threat/Warning Analyst"]]},{"code":"CT05","title":"CTI Platforms & Sharing","prefix":"CT","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Intelligence","k":4,"s":2,"a":2,"t":2,"roles":[["AN-ASA-001","All-Source Analyst"],["AN-TWA-001","Threat/Warning Analyst"]]},{"code":"CT06","title":"Capstone — Intelligence Product","prefix":"CT","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Intelligence","k":4,"s":2,"a":2,"t":2,"roles":[["AN-ASA-001","All-Source Analyst"],["AN-TWA-001","Threat/Warning Analyst"]]},{"code":"DE01","title":"Detection Theory & Philosophy","prefix":"DE","degree":"Operational","year":"Year 3 · Specialisation","area":"Detection Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"DE02","title":"Data Sources & Log Engineering","prefix":"DE","degree":"Operational","year":"Year 3 · Specialisation","area":"Detection Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"DE03","title":"Writing Detection Logic","prefix":"DE","degree":"Operational","year":"Year 3 · Specialisation","area":"Detection Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"DE04","title":"Adversary Simulation for Detection","prefix":"DE","degree":"Operational","year":"Year 3 · Specialisation","area":"Detection Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"DE05","title":"Detection Operations & Management","prefix":"DE","degree":"Operational","year":"Year 3 · Specialisation","area":"Detection Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"DE06","title":"Capstone — Detection Library","prefix":"DE","degree":"Operational","year":"Year 3 · Specialisation","area":"Detection Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"CE01","title":"Offensive Foundations & Ethics","prefix":"CE","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Emulation","k":4,"s":2,"a":2,"t":2,"roles":[["OV-SPP-001","Cyber Policy & Strategy Planner"],["PR-VAM-001","Vulnerability Assessment Analyst"]]},{"code":"CE02","title":"Red Team Operations","prefix":"CE","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Emulation","k":4,"s":2,"a":2,"t":2,"roles":[["AN-EXP-001","Exploitation Analyst"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"CE03","title":"ATT&CK-Based Emulation","prefix":"CE","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Emulation","k":4,"s":2,"a":2,"t":2,"roles":[["AN-EXP-001","Exploitation Analyst"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"CE04","title":"Purple Team Operations","prefix":"CE","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Emulation","k":4,"s":2,"a":2,"t":2,"roles":[["PR-CDA-001","Cyber Defense Analyst"],["AN-EXP-001","Exploitation Analyst"]]},{"code":"CE05","title":"Reporting & Debrief","prefix":"CE","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Emulation","k":4,"s":2,"a":2,"t":2,"roles":[["OV-SPP-001","Cyber Policy & Strategy Planner"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"CE06","title":"Capstone — Emulation Exercise","prefix":"CE","degree":"Operational","year":"Year 3 · Specialisation","area":"Cyber Threat Emulation","k":4,"s":2,"a":2,"t":2,"roles":[["AN-EXP-001","Exploitation Analyst"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"SE01","title":"Secure System Design","prefix":"SE","degree":"Strategic","year":"Year 3 · Specialisation","area":"Security Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["SP-ARC-002","Security Architect"],["SP-DEV-002","Secure Software Assessor"]]},{"code":"SE02","title":"Security Architecture","prefix":"SE","degree":"Strategic","year":"Year 3 · Specialisation","area":"Security Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["SP-ARC-002","Security Architect"],["SP-ARC-001","Enterprise Architect"]]},{"code":"SE03","title":"Identity & Access Management","prefix":"SE","degree":"Strategic","year":"Year 3 · Specialisation","area":"Security Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["SP-ARC-002","Security Architect"],["OM-ADM-001","System Administrator"]]},{"code":"SE04","title":"Detection & Response Engineering","prefix":"SE","degree":"Strategic","year":"Year 3 · Specialisation","area":"Security Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["SP-ARC-002","Security Architect"],["PR-CDA-001","Cyber Defense Analyst"]]},{"code":"SE05","title":"Security in Cloud & DevSecOps","prefix":"SE","degree":"Strategic","year":"Year 3 · Specialisation","area":"Security Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["SP-DEV-002","Secure Software Assessor"],["SP-ARC-002","Security Architect"]]},{"code":"SE06","title":"Capstone — Architecture Design","prefix":"SE","degree":"Strategic","year":"Year 3 · Specialisation","area":"Security Engineering","k":4,"s":2,"a":2,"t":2,"roles":[["SP-ARC-002","Security Architect"],["SP-ARC-001","Enterprise Architect"]]},{"code":"LD01","title":"CISO Role & Function","prefix":"LD","degree":"Strategic","year":"Year 3 · Specialisation","area":"Leadership & CISO","k":4,"s":2,"a":2,"t":2,"roles":[["OV-EXL-001","Executive Cyber Leadership"],["OV-MGT-001","Information Systems Security Manager"]]},{"code":"LD02","title":"Security Strategy & Roadmapping","prefix":"LD","degree":"Strategic","year":"Year 3 · Specialisation","area":"Leadership & CISO","k":4,"s":2,"a":2,"t":2,"roles":[["OV-MGT-001","Information Systems Security Manager"],["OV-SPP-001","Cyber Policy & Strategy Planner"]]},{"code":"LD03","title":"Communicating Risk to Executives","prefix":"LD","degree":"Strategic","year":"Year 3 · Specialisation","area":"Leadership & CISO","k":4,"s":2,"a":2,"t":1,"roles":[["OV-MGT-001","Information Systems Security Manager"],["OV-EXL-001","Executive Cyber Leadership"]]},{"code":"LD04","title":"Building & Leading Security Teams","prefix":"LD","degree":"Strategic","year":"Year 3 · Specialisation","area":"Leadership & CISO","k":4,"s":2,"a":2,"t":2,"roles":[["OV-MGT-001","Information Systems Security Manager"],["OV-SPP-002","Cyber Workforce Developer/Manager"]]},{"code":"LD05","title":"Crisis Management & Communications","prefix":"LD","degree":"Strategic","year":"Year 3 · Specialisation","area":"Leadership & CISO","k":4,"s":2,"a":2,"t":1,"roles":[["OV-EXL-001","Executive Cyber Leadership"],["OV-MGT-001","Information Systems Security Manager"]]},{"code":"LD06","title":"Capstone — CISO Simulation","prefix":"LD","degree":"Strategic","year":"Year 3 · Specialisation","area":"Leadership & CISO","k":4,"s":2,"a":2,"t":2,"roles":[["OV-EXL-001","Executive Cyber Leadership"],["OV-MGT-001","Information Systems Security Manager"]]},{"code":"GR01","title":"Security Governance Design","prefix":"GR","degree":"Strategic","year":"Year 3 · Specialisation","area":"Governance, Risk & Compliance","k":4,"s":2,"a":2,"t":2,"roles":[["OV-SPP-001","Cyber Policy & Strategy Planner"],["OV-MGT-001","Information Systems Security Manager"]]},{"code":"GR02","title":"Risk Management in Practice","prefix":"GR","degree":"Strategic","year":"Year 3 · Specialisation","area":"Governance, Risk & Compliance","k":4,"s":2,"a":2,"t":2,"roles":[["SP-RSK-002","Security Control Assessor"],["OV-MGT-001","Information Systems Security Manager"]]},{"code":"GR03","title":"Compliance Frameworks","prefix":"GR","degree":"Strategic","year":"Year 3 · Specialisation","area":"Governance, Risk & Compliance","k":4,"s":2,"a":2,"t":2,"roles":[["SP-RSK-002","Security Control Assessor"],["OV-SPP-001","Cyber Policy & Strategy Planner"]]},{"code":"GR04","title":"Australian Regulatory Environment","prefix":"GR","degree":"Strategic","year":"Year 3 · Specialisation","area":"Governance, Risk & Compliance","k":4,"s":2,"a":2,"t":2,"roles":[["OV-LGA-002","Privacy Officer/Privacy Compliance Manager"],["OV-LGA-001","Cyber Legal Advisor"]]},{"code":"GR05","title":"Audit & Assurance","prefix":"GR","degree":"Strategic","year":"Year 3 · Specialisation","area":"Governance, Risk & Compliance","k":4,"s":2,"a":2,"t":2,"roles":[["SP-RSK-002","Security Control Assessor"]]},{"code":"GR06","title":"Capstone — GRC Program Design","prefix":"GR","degree":"Strategic","year":"Year 3 · Specialisation","area":"Governance, Risk & Compliance","k":4,"s":2,"a":2,"t":2,"roles":[["OV-MGT-001","Information Systems Security Manager"],["SP-RSK-002","Security Control Assessor"]]}],"domainOrder":["F","OC","SC","TH","DF","CT","DE","CE","SE","LD","GR"],"domainShort":{"F":"Foundation","OC":"Op Core","SC":"Str Core","TH":"Threat Hunt","DF":"DFIR","CT":"CTI","DE":"Detection","CE":"Emulation","SE":"Sec Eng","LD":"Leadership","GR":"GRC"},"domainLabel":{"F":"Foundation","OC":"Operational Core","SC":"Strategic Core","TH":"Threat Hunting","DF":"DFIR","CT":"Cyber Threat Intelligence","DE":"Detection Engineering","CE":"Cyber Threat Emulation","SE":"Security Engineering","LD":"Leadership & CISO","GR":"Governance, Risk & Compliance"},"degreeOrder":["Shared Core","Operational","Strategic"],"presets":[{"label":"Operations degree","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","TH01","TH02","TH03","TH04","TH05","TH06","DF01","DF02","DF03","DF04","DF05","DF06","CT01","CT02","CT03","CT04","CT05","CT06","DE01","DE02","DE03","DE04","DE05","DE06","CE01","CE02","CE03","CE04","CE05","CE06"]},{"label":"Strategy degree","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","SE01","SE02","SE03","SE04","SE05","SE06","LD01","LD02","LD03","LD04","LD05","LD06","GR01","GR02","GR03","GR04","GR05","GR06"]},{"label":"Shared core","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06"]},{"label":"All 66 courses","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","TH01","TH02","TH03","TH04","TH05","TH06","DF01","DF02","DF03","DF04","DF05","DF06","CT01","CT02","CT03","CT04","CT05","CT06","DE01","DE02","DE03","DE04","DE05","DE06","CE01","CE02","CE03","CE04","CE05","CE06","SE01","SE02","SE03","SE04","SE05","SE06","LD01","LD02","LD03","LD04","LD05","LD06","GR01","GR02","GR03","GR04","GR05","GR06"]},{"label":"Core + Threat Hunting","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","TH01","TH02","TH03","TH04","TH05","TH06"]},{"label":"Core + DFIR","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","DF01","DF02","DF03","DF04","DF05","DF06"]},{"label":"Core + Cyber Threat Intelligence","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","CT01","CT02","CT03","CT04","CT05","CT06"]},{"label":"Core + Detection Engineering","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","DE01","DE02","DE03","DE04","DE05","DE06"]},{"label":"Core + Cyber Threat Emulation","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","CE01","CE02","CE03","CE04","CE05","CE06"]},{"label":"Core + Security Engineering","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","SE01","SE02","SE03","SE04","SE05","SE06"]},{"label":"Core + Leadership & CISO","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","LD01","LD02","LD03","LD04","LD05","LD06"]},{"label":"Core + Governance, Risk & Compliance","units":["F01","F02","F03","F04","F05","F06","OC01","OC02","OC03","OC04","OC05","OC06","SC01","SC02","SC03","SC04","SC05","SC06","GR01","GR02","GR03","GR04","GR05","GR06"]}]};</script>
<script>
/* Program Builder — live KSAT coverage explorer.
 *
 * Vanilla JS, no dependencies. Consumes window.PROGRAM_DATA (injected into the
 * page) and renders, in real time as the user ticks courses:
 *   - a searchable course picker grouped by degree -> year -> major;
 *   - NICE/DCWF work-role completion bars;
 *   - four radar ("spider web") charts (Knowledge, Skills, Abilities, Tasks),
 *     Selected vs Catalogue across every degree domain;
 *   - a KSAT-composition donut and a summary line.
 *
 * KSAT IDs are project-local (provisional) pending Framework Custodian mapping.
 */
(function () {
  "use strict";
  var D = window.PROGRAM_DATA;
  if (!D || !document.getElementById("pb-tree")) return;

  var SVGNS = "http://www.w3.org/2000/svg";
  var COL_CAT = "#9aa7b4";   // catalogue / available
  var COL_SEL = "#7e57c2";   // selected (deep purple, matches theme)
  var TYPES = [["k", "Knowledge"], ["s", "Skills"], ["a", "Abilities"], ["t", "Tasks"]];

  var byCode = {};
  D.units.forEach(function (u) { byCode[u.code] = u; });
  var selected = new Set();

  // Catalogue aggregates.
  var roleName = {}, roleUniverse = {};
  D.units.forEach(function (u) {
    var tot = u.k + u.s + u.a + u.t;
    u.roles.forEach(function (r) {
      roleName[r[0]] = r[1];
      roleUniverse[r[0]] = (roleUniverse[r[0]] || 0) + tot;
    });
  });
  var cat = {};
  D.domainOrder.forEach(function (p) { cat[p] = { k: 0, s: 0, a: 0, t: 0 }; });
  D.units.forEach(function (u) {
    if (cat[u.prefix]) { ["k", "s", "a", "t"].forEach(function (x) { cat[u.prefix][x] += u[x]; }); }
  });
  var catTotal = D.units.reduce(function (s, u) { return s + u.k + u.s + u.a + u.t; }, 0);

  // ---- tiny DOM helpers ----
  function el(tag, attrs, kids) {
    var e = document.createElement(tag); attrs = attrs || {};
    Object.keys(attrs).forEach(function (k) {
      if (k === "class") e.className = attrs[k];
      else if (k === "html") e.innerHTML = attrs[k];
      else e.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { e.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return e;
  }
  function sv(tag, attrs, kids) {
    var e = document.createElementNS(SVGNS, tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    (kids || []).forEach(function (c) { e.appendChild(c); });
    return e;
  }

  // ---- course picker ----
  var unitCheckboxes = {};   // code -> input
  var groupNodes = [];       // {wrap, codes, header input}

  function buildTree() {
    var tree = document.getElementById("pb-tree");
    tree.innerHTML = "";
    // degree -> year -> area
    var degrees = {};
    D.degreeOrder.forEach(function (d) { degrees[d] = { order: [], years: {} }; });
    D.units.forEach(function (u) {
      var dg = degrees[u.degree]; if (!dg) return;
      if (!dg.years[u.year]) { dg.years[u.year] = { order: [], areas: {} }; dg.order.push(u.year); }
      var yr = dg.years[u.year];
      if (!yr.areas[u.area]) { yr.areas[u.area] = []; yr.order.push(u.area); }
      yr.areas[u.area].push(u);
    });

    D.degreeOrder.forEach(function (dname) {
      var dg = degrees[dname];
      var dgCodes = [];
      var details = el("details", { class: "pb-deg", open: "" });
      var sumWrap = el("summary", {});
      var dgChk = el("input", { type: "checkbox", class: "pb-grp" });
      dgChk.addEventListener("click", function (e) { e.stopPropagation(); });
      dgChk.addEventListener("change", function () { setMany(dgCodes, dgChk.checked); });
      sumWrap.appendChild(dgChk);
      sumWrap.appendChild(el("span", { class: "pb-deg-name" }, [dname]));
      var dgCount = el("span", { class: "pb-count" });
      sumWrap.appendChild(dgCount);
      details.appendChild(sumWrap);

      dg.order.forEach(function (yname) {
        var yr = dg.years[yname];
        details.appendChild(el("div", { class: "pb-year" }, [yname]));
        yr.order.forEach(function (aname) {
          var units = yr.areas[aname];
          var aCodes = units.map(function (u) { return u.code; });
          dgCodes = dgCodes.concat(aCodes);
          var area = el("div", { class: "pb-area" });
          var ah = el("label", { class: "pb-area-h" });
          var aChk = el("input", { type: "checkbox", class: "pb-grp" });
          aChk.addEventListener("change", function () { setMany(aCodes, aChk.checked); });
          ah.appendChild(aChk);
          ah.appendChild(el("span", { class: "pb-area-name" }, [aname]));
          area.appendChild(ah);
          units.forEach(function (u) {
            var row = el("label", { class: "pb-unit", "data-text": (u.code + " " + u.title).toLowerCase() });
            var chk = el("input", { type: "checkbox" });
            chk.addEventListener("change", function () { toggle(u.code, chk.checked); });
            unitCheckboxes[u.code] = chk;
            row.appendChild(chk);
            row.appendChild(el("span", { class: "pb-code" }, [u.code]));
            row.appendChild(el("span", { class: "pb-title" }, [u.title]));
            area.appendChild(row);
          });
          details.appendChild(area);
          groupNodes.push({ input: aChk, codes: aCodes });
        });
      });
      groupNodes.push({ input: dgChk, codes: dgCodes, count: dgCount });
      tree.appendChild(details);
    });
  }

  function toggle(code, on) { if (on) selected.add(code); else selected.delete(code); update(); }
  function setMany(codes, on) { codes.forEach(function (c) { if (on) selected.add(c); else selected.delete(c); }); update(); }

  function syncChecks() {
    Object.keys(unitCheckboxes).forEach(function (c) { unitCheckboxes[c].checked = selected.has(c); });
    groupNodes.forEach(function (g) {
      var n = g.codes.filter(function (c) { return selected.has(c); }).length;
      g.input.checked = n > 0 && n === g.codes.length;
      g.input.indeterminate = n > 0 && n < g.codes.length;
      if (g.count) g.count.textContent = n + "/" + g.codes.length;
    });
  }

  // ---- presets + search ----
  function buildPresets() {
    var box = document.getElementById("pb-presets");
    (D.presets || []).forEach(function (p) {
      box.appendChild(el("button", { type: "button", class: "pb-btn" }, [p.label]))
        .addEventListener("click", function () { selected = new Set(p.units); update(); });
    });
    box.appendChild(el("button", { type: "button", class: "pb-btn pb-btn-clear" }, ["Clear"]))
      .addEventListener("click", function () { selected = new Set(); update(); });
  }
  function wireSearch() {
    document.getElementById("pb-search").addEventListener("input", function (e) {
      var q = e.target.value.trim().toLowerCase();
      document.querySelectorAll("#pb-tree .pb-unit").forEach(function (row) {
        row.style.display = (!q || row.getAttribute("data-text").indexOf(q) !== -1) ? "" : "none";
      });
      document.querySelectorAll("#pb-tree .pb-area").forEach(function (area) {
        var any = Array.prototype.some.call(area.querySelectorAll(".pb-unit"), function (r) { return r.style.display !== "none"; });
        area.style.display = any ? "" : "none";
      });
    });
  }

  // ---- metrics ----
  function totals() {
    var t = { k: 0, s: 0, a: 0, t: 0 };
    selected.forEach(function (c) { var u = byCode[c]; if (u) { t.k += u.k; t.s += u.s; t.a += u.a; t.t += u.t; } });
    return t;
  }
  function selByDomain() {
    var m = {}; D.domainOrder.forEach(function (p) { m[p] = { k: 0, s: 0, a: 0, t: 0 }; });
    selected.forEach(function (c) { var u = byCode[c]; if (u && m[u.prefix]) { ["k", "s", "a", "t"].forEach(function (x) { m[u.prefix][x] += u[x]; }); } });
    return m;
  }
  function roleRows() {
    var covered = {};
    selected.forEach(function (c) {
      var u = byCode[c]; if (!u) return; var tot = u.k + u.s + u.a + u.t;
      u.roles.forEach(function (r) { covered[r[0]] = (covered[r[0]] || 0) + tot; });
    });
    return Object.keys(roleUniverse).map(function (rc) {
      var uni = roleUniverse[rc], cov = covered[rc] || 0;
      return { code: rc, name: roleName[rc], cov: cov, uni: uni, pct: uni ? Math.round(100 * cov / uni) : 0 };
    }).sort(function (a, b) { return b.pct - a.pct || (a.code < b.code ? -1 : 1); });
  }

  // ---- charts ----
  function renderSummary(t) {
    var grand = t.k + t.s + t.a + t.t;
    var pct = catTotal ? Math.round(100 * grand / catTotal) : 0;
    document.getElementById("pb-summary").innerHTML =
      "<strong>" + selected.size + "</strong> of " + D.units.length + " courses · " +
      "<strong>" + grand + "</strong> KSAT items " +
      "(" + t.k + " K · " + t.s + " S · " + t.a + " A · " + t.t + " T) · " +
      "<strong>" + pct + "%</strong> of the full catalogue (" + catTotal + " items).";
  }

  function renderBars(rows) {
    var host = document.getElementById("pb-bars");
    host.innerHTML = "";
    rows.forEach(function (r) {
      var row = el("div", { class: "pb-bar-row", title: r.name + " (" + r.code + ") — " + r.cov + "/" + r.uni + " KSATs" });
      row.appendChild(el("span", { class: "pb-bar-label" }, [r.code]));
      var track = el("div", { class: "pb-bar-track" });
      var fill = el("div", { class: "pb-bar-fill" });
      fill.style.width = r.pct + "%";
      if (r.pct === 0) fill.classList.add("pb-bar-zero");
      track.appendChild(fill);
      row.appendChild(track);
      row.appendChild(el("span", { class: "pb-bar-pct" }, [r.pct + "%"]));
      host.appendChild(row);
    });
  }

  function radar(axes, catVals, selVals, maxv, title) {
    var W = 300, H = 260, cx = 150, cy = 132, R = 92, rings = 4;
    var svg = sv("svg", { viewBox: "0 0 " + W + " " + H, class: "pb-radar", role: "img", "aria-label": title });
    function pt(i, frac) {
      var ang = -Math.PI / 2 + i * 2 * Math.PI / axes.length;
      return [cx + R * frac * Math.cos(ang), cy + R * frac * Math.sin(ang)];
    }
    for (var g = 1; g <= rings; g++) {
      var d = axes.map(function (_, i) { var p = pt(i, g / rings); return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + " Z";
      svg.appendChild(sv("path", { d: d, fill: "none", stroke: "#d7dce1", "stroke-width": "1" }));
    }
    axes.forEach(function (label, i) {
      var p = pt(i, 1);
      svg.appendChild(sv("line", { x1: cx, y1: cy, x2: p[0], y2: p[1], stroke: "#d7dce1", "stroke-width": "1" }));
      var lp = pt(i, 1.16), t = sv("text", {
        x: lp[0].toFixed(1), y: lp[1].toFixed(1), "font-size": "9",
        "text-anchor": lp[0] < cx - 4 ? "end" : (lp[0] > cx + 4 ? "start" : "middle"),
        "dominant-baseline": "middle", fill: "currentColor"
      });
      t.textContent = label; svg.appendChild(t);
    });
    function poly(vals, color, fillOp) {
      var d = vals.map(function (v, i) { var p = pt(i, maxv ? v / maxv : 0); return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + " Z";
      svg.appendChild(sv("path", { d: d, fill: color, "fill-opacity": fillOp, stroke: color, "stroke-width": "1.5" }));
    }
    poly(catVals, COL_CAT, "0.10");
    poly(selVals, COL_SEL, "0.35");
    var tt = sv("text", { x: cx, y: 14, "text-anchor": "middle", "font-size": "12", "font-weight": "600", fill: "currentColor" });
    tt.textContent = title; svg.appendChild(tt);
    return svg;
  }

  function renderRadars(sel) {
    var host = document.getElementById("pb-radars");
    host.innerHTML = "";
    var present = D.domainOrder.filter(function (p) { return cat[p].k + cat[p].s + cat[p].a + cat[p].t > 0; });
    var axes = present.map(function (p) { return D.domainShort[p]; });
    TYPES.forEach(function (ty) {
      var key = ty[0];
      var maxv = Math.max.apply(null, present.map(function (p) { return cat[p][key]; }).concat([1]));
      var catVals = present.map(function (p) { return cat[p][key]; });
      var selVals = present.map(function (p) { return sel[p][key]; });
      host.appendChild(radar(axes, catVals, selVals, maxv, ty[1]));
    });
  }

  function renderDonut(t) {
    var host = document.getElementById("pb-donut");
    host.innerHTML = "";
    var grand = t.k + t.s + t.a + t.t;
    var parts = [["Knowledge", t.k, "#7e57c2"], ["Skills", t.s, "#26a69a"], ["Abilities", t.a, "#ef6c00"], ["Tasks", t.t, "#1e88e5"]];
    var svg = sv("svg", { viewBox: "0 0 120 120", class: "pb-donut", role: "img", "aria-label": "KSAT composition" });
    var cx = 60, cy = 60, r = 45, circ = 2 * Math.PI * r, off = 0;
    if (grand === 0) {
      svg.appendChild(sv("circle", { cx: cx, cy: cy, r: r, fill: "none", stroke: "#e0e4e8", "stroke-width": "18" }));
    } else {
      parts.forEach(function (p) {
        if (!p[1]) return;
        var len = circ * p[1] / grand;
        svg.appendChild(sv("circle", {
          cx: cx, cy: cy, r: r, fill: "none", stroke: p[2], "stroke-width": "18",
          "stroke-dasharray": len.toFixed(2) + " " + (circ - len).toFixed(2),
          "stroke-dashoffset": (-off).toFixed(2), transform: "rotate(-90 " + cx + " " + cy + ")"
        }));
        off += len;
      });
    }
    var ctr = sv("text", { x: cx, y: cy, "text-anchor": "middle", "dominant-baseline": "central", "font-size": "16", "font-weight": "700", fill: "currentColor" });
    ctr.textContent = String(grand); svg.appendChild(ctr);
    var wrap = el("div", { class: "pb-donut-wrap" });
    wrap.appendChild(svg);
    var legend = el("div", { class: "pb-legend" });
    parts.forEach(function (p) {
      var item = el("span", { class: "pb-legend-item" });
      item.appendChild(el("span", { class: "pb-swatch" })).style.background = p[2];
      item.appendChild(document.createTextNode(" " + p[0] + " " + p[1]));
      legend.appendChild(item);
    });
    wrap.appendChild(legend);
    host.appendChild(wrap);
  }

  function update() {
    syncChecks();
    var t = totals();
    renderSummary(t);
    renderBars(roleRows());
    renderRadars(selByDomain());
    renderDonut(t);
  }

  buildTree();
  buildPresets();
  wireSearch();
  // Start with a meaningful default so the charts are populated on first view.
  if (D.presets && D.presets.length) { selected = new Set(D.presets[0].units); }
  update();
})();

</script>
