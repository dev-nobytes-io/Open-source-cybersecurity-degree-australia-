/* Program Builder — TEAM overlay.
 *
 * Vanilla JS, no dependencies. Reuses window.PROGRAM_DATA. Build a team from
 * several members (each a course selection, added manually or loaded from a saved
 * program/team JSON) and overlay their capability radars to check coverage.
 *
 * The extra dimension is overlap: each member's polygon is drawn translucent and
 * the same colour, so where many members coincide (the shared core) the fill
 * composites to a deep, opaque purple, and where only a specialist reaches out the
 * fill stays faint — unless the team is genuinely diverse. A union outline shows
 * the team's total reach and each axis is annotated with how many members cover it.
 *
 * Save / Load / Print extend to the whole team.
 */
(function () {
  "use strict";
  var D = window.PROGRAM_DATA;
  if (!D || !document.getElementById("pb-team")) return;

  var SVGNS = "http://www.w3.org/2000/svg";
  var COL_SEL = "#7e57c2", COL_GAP = "#e53935";
  var byCode = {};
  D.units.forEach(function (u) { byCode[u.code] = u; });

  var LENSES = [
    { key: "profile", title: "Capability profile", axes: ["Knows", "Can do", "Unique", "Has done"] },
    { key: "cap", title: "Operational capabilities", axes: D.capabilityOrder },
    { key: "nice", title: "NICE/DCWF work categories", axes: D.niceOrder },
    { key: "bloom", title: "Cognitive depth (Bloom's)", axes: D.bloomLabels }
  ];

  function lensVectors(codes) {
    var capI = {}; D.capabilityOrder.forEach(function (c, i) { capI[c] = i; });
    var niceI = {}; D.niceOrder.forEach(function (c, i) { niceI[c] = i; });
    var v = { profile: [0, 0, 0, 0], cap: D.capabilityOrder.map(z), nice: D.niceOrder.map(z), bloom: D.bloomLabels.map(z) };
    function z() { return 0; }
    (codes || []).forEach(function (code) {
      var u = byCode[code]; if (!u) return;
      var tot = u.k + u.s + u.a + u.t;
      v.profile[0] += u.k + (u.bloom[0] || 0) + (u.bloom[1] || 0);
      v.profile[1] += u.s + (u.bloom[2] || 0);
      v.profile[3] += u.t + (u.bloom[3] || 0);
      v.profile[2] += u.a + (u.bloom[4] || 0) + (u.bloom[5] || 0);
      if (capI[u.cap] != null) v.cap[capI[u.cap]] += tot;
      var cats = {};
      u.roles.forEach(function (r) { var c = D.niceOf[r[0].split("-")[0]]; if (c) cats[c] = 1; });
      Object.keys(cats).forEach(function (c) { if (niceI[c] != null) v.nice[niceI[c]] += tot; });
      for (var i = 0; i < 6; i++) v.bloom[i] += (u.bloom[i] || 0);
    });
    return v;
  }
  var catVec = lensVectors(D.units.map(function (u) { return u.code; }));

  // ---- DOM helpers ----
  function el(tag, attrs, kids) {
    var e = document.createElement(tag); attrs = attrs || {};
    Object.keys(attrs).forEach(function (k) {
      if (k === "class") e.className = attrs[k]; else if (k === "html") e.innerHTML = attrs[k]; else e.setAttribute(k, attrs[k]);
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
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // ---- team state ----
  var members = [];   // {name, sel:Set}
  var active = -1;
  var unitCheckboxes = {}, groupNodes = [];

  function addMember(name, codes) {
    members.push({ name: name || ("Member " + (members.length + 1)), sel: new Set((codes || []).filter(function (c) { return byCode[c]; })) });
    active = members.length - 1;
  }
  function removeMember(i) {
    members.splice(i, 1);
    if (active >= members.length) active = members.length - 1;
    renderMembers(); syncPicker(); update();
  }
  function selectMember(i) { active = i; renderMembers(); syncPicker(); }

  function renderMembers() {
    var host = document.getElementById("pb-members"); host.innerHTML = "";
    members.forEach(function (m, i) {
      var row = el("div", { class: "pb-member" + (i === active ? " pb-active" : "") });
      var dot = el("span", { class: "pb-mdot" }); dot.style.opacity = "1";
      row.appendChild(dot);
      var nm = el("button", { type: "button", class: "pb-mname-btn" }, [m.name + " (" + m.sel.size + ")"]);
      nm.addEventListener("click", function () { selectMember(i); });
      row.appendChild(nm);
      var del = el("button", { type: "button", class: "pb-mdel", title: "Remove" }, ["✕"]);
      del.addEventListener("click", function () { removeMember(i); });
      row.appendChild(del);
      host.appendChild(row);
    });
    var nameInput = document.getElementById("pb-mname");
    if (active >= 0) { nameInput.value = members[active].name; nameInput.disabled = false; }
    else { nameInput.value = ""; nameInput.disabled = true; }
  }

  // ---- picker (edits the active member) ----
  function buildTree() {
    var tree = document.getElementById("pb-tree"); tree.innerHTML = ""; unitCheckboxes = {}; groupNodes = [];
    var degrees = {}; D.degreeOrder.forEach(function (d) { degrees[d] = { order: [], years: {} }; });
    D.units.forEach(function (u) {
      var dg = degrees[u.degree]; if (!dg) return;
      if (!dg.years[u.year]) { dg.years[u.year] = { order: [], areas: {} }; dg.order.push(u.year); }
      var yr = dg.years[u.year];
      if (!yr.areas[u.area]) { yr.areas[u.area] = []; yr.order.push(u.area); }
      yr.areas[u.area].push(u);
    });
    D.degreeOrder.forEach(function (dname) {
      var dg = degrees[dname], dgCodes = [];
      var details = el("details", { class: "pb-deg" });
      var sm = el("summary", {});
      var dgChk = el("input", { type: "checkbox", class: "pb-grp" });
      dgChk.addEventListener("click", function (e) { e.stopPropagation(); });
      dgChk.addEventListener("change", function () { setMany(dgCodes, dgChk.checked); });
      sm.appendChild(dgChk); sm.appendChild(el("span", {}, [dname]));
      var dgCount = el("span", { class: "pb-count" }); sm.appendChild(dgCount);
      details.appendChild(sm);
      dg.order.forEach(function (yname) {
        details.appendChild(el("div", { class: "pb-year" }, [yname]));
        dg.years[yname].order.forEach(function (aname) {
          var units = dg.years[yname].areas[aname], aCodes = units.map(function (u) { return u.code; });
          dgCodes = dgCodes.concat(aCodes);
          var area = el("div", { class: "pb-area" });
          var ah = el("label", { class: "pb-area-h" });
          var aChk = el("input", { type: "checkbox", class: "pb-grp" });
          aChk.addEventListener("change", function () { setMany(aCodes, aChk.checked); });
          ah.appendChild(aChk); ah.appendChild(el("span", {}, [aname]));
          area.appendChild(ah);
          units.forEach(function (u) {
            var r = el("label", { class: "pb-unit", "data-text": (u.code + " " + u.title).toLowerCase() });
            var chk = el("input", { type: "checkbox" });
            chk.addEventListener("change", function () { toggle(u.code, chk.checked); });
            unitCheckboxes[u.code] = chk;
            r.appendChild(chk); r.appendChild(el("span", { class: "pb-code" }, [u.code])); r.appendChild(el("span", { class: "pb-title" }, [u.title]));
            area.appendChild(r);
          });
          details.appendChild(area);
          groupNodes.push({ input: aChk, codes: aCodes });
        });
      });
      groupNodes.push({ input: dgChk, codes: dgCodes, count: dgCount });
      tree.appendChild(details);
    });
  }
  function curSel() { return active >= 0 ? members[active].sel : null; }
  function toggle(code, on) { var s = curSel(); if (!s) return; if (on) s.add(code); else s.delete(code); afterEdit(); }
  function setMany(codes, on) { var s = curSel(); if (!s) return; codes.forEach(function (c) { if (on) s.add(c); else s.delete(c); }); afterEdit(); }
  function afterEdit() { renderMembers(); syncPicker(); update(); }
  function syncPicker() {
    var s = curSel();
    Object.keys(unitCheckboxes).forEach(function (c) { unitCheckboxes[c].checked = s ? s.has(c) : false; unitCheckboxes[c].disabled = !s; });
    groupNodes.forEach(function (g) {
      var n = s ? g.codes.filter(function (c) { return s.has(c); }).length : 0;
      g.input.checked = n > 0 && n === g.codes.length;
      g.input.indeterminate = n > 0 && n < g.codes.length;
      g.input.disabled = !s;
      if (g.count) g.count.textContent = n + "/" + g.codes.length;
    });
  }

  function buildPresets() {
    var box = document.getElementById("pb-presets");
    (D.presets || []).forEach(function (p) {
      box.appendChild(el("button", { type: "button", class: "pb-btn" }, [p.label]))
        .addEventListener("click", function () { if (active < 0) return; members[active].sel = new Set(p.units); afterEdit(); });
    });
    box.appendChild(el("button", { type: "button", class: "pb-btn pb-btn-clear" }, ["Clear member"]))
      .addEventListener("click", function () { if (active < 0) return; members[active].sel = new Set(); afterEdit(); });
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

  // ---- overlay radar ----
  function memberFrac(key) {
    return members.map(function (m) {
      var v = lensVectors(Array.from(m.sel))[key];
      return v.map(function (x, i) { return catVec[key][i] ? x / catVec[key][i] : 0; });
    });
  }
  function radar(axes, fracs, title) {
    var W = 300, H = 252, cx = 150, cy = 130, R = 88, rings = 4;
    var svg = sv("svg", { viewBox: "0 0 " + W + " " + H, class: "pb-radar", role: "img", "aria-label": title });
    function pt(i, f) { var a = -Math.PI / 2 + i * 2 * Math.PI / axes.length; return [cx + R * f * Math.cos(a), cy + R * f * Math.sin(a)]; }
    for (var g = 1; g <= rings; g++) {
      var d = axes.map(function (_, i) { var p = pt(i, g / rings); return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + " Z";
      svg.appendChild(sv("path", { d: d, fill: "none", stroke: "#d7dce1", "stroke-width": "1" }));
    }
    // overlap count per axis (members with >0 on that axis)
    var counts = axes.map(function (_, i) { return fracs.reduce(function (n, f) { return n + (f[i] > 0 ? 1 : 0); }, 0); });
    axes.forEach(function (label, i) {
      var p = pt(i, 1);
      svg.appendChild(sv("line", { x1: cx, y1: cy, x2: p[0], y2: p[1], stroke: "#d7dce1", "stroke-width": "1" }));
      var lp = pt(i, 1.17), t = sv("text", { x: lp[0].toFixed(1), y: lp[1].toFixed(1), "font-size": "8.5",
        "text-anchor": lp[0] < cx - 4 ? "end" : (lp[0] > cx + 4 ? "start" : "middle"), "dominant-baseline": "middle",
        fill: counts[i] === 0 ? COL_GAP : "currentColor" });
      t.textContent = label + (counts[i] ? " ·" + counts[i] : " ·0");
      svg.appendChild(t);
    });
    // each member as a translucent polygon — overlap composites to opacity
    var alpha = members.length ? Math.max(0.12, Math.min(0.28, 0.9 / members.length)) : 0.2;
    fracs.forEach(function (f) {
      var d = f.map(function (v, i) { var p = pt(i, v); return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + " Z";
      svg.appendChild(sv("path", { d: d, fill: COL_SEL, "fill-opacity": alpha.toFixed(3), stroke: "none" }));
    });
    // union outline (team's total reach)
    if (fracs.length) {
      var uni = axes.map(function (_, i) { return Math.max.apply(null, fracs.map(function (f) { return f[i]; })); });
      var du = uni.map(function (v, i) { var p = pt(i, v); return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + " Z";
      svg.appendChild(sv("path", { d: du, fill: "none", stroke: COL_SEL, "stroke-width": "1.4", "stroke-dasharray": "3 2" }));
    }
    return svg;
  }
  function renderRadars() {
    var host = document.getElementById("pb-radars"); host.innerHTML = "";
    LENSES.forEach(function (L) {
      var card = el("div", { class: "pb-radar-card" });
      card.appendChild(el("h4", {}, [L.title]));
      card.appendChild(radar(L.axes, memberFrac(L.key), L.title));
      host.appendChild(card);
    });
  }

  // ---- coverage table (operational capabilities) ----
  function renderCoverage() {
    var host = document.getElementById("pb-coverage"); host.innerHTML = "";
    var fr = memberFrac("cap");
    var head = el("tr", {}, [el("th", {}, ["Capability"]), el("th", {}, ["Members"]), el("th", {}, ["Who / status"])]);
    var rows = [el("thead", {}, [head])], body = el("tbody", {});
    D.capabilityOrder.forEach(function (capName, i) {
      var who = [];
      members.forEach(function (m, mi) { if (fr[mi][i] > 0) who.push(m.name); });
      var status = who.length === 0 ? "⚠ gap" : (who.length === 1 ? "solo" : (who.length >= 3 ? "redundant" : "covered"));
      var tr = el("tr", who.length === 0 ? { class: "pb-gap" } : {}, [
        el("td", {}, [capName]),
        el("td", {}, [String(who.length)]),
        el("td", {}, [who.length ? who.join(", ") + " — " + status : "no one — " + status])
      ]);
      body.appendChild(tr);
    });
    rows.push(body);
    host.appendChild(el("table", { class: "pb-cov" }, rows));
  }

  function renderSummary() {
    var union = new Set();
    members.forEach(function (m) { m.sel.forEach(function (c) { union.add(c); }); });
    var grand = 0; union.forEach(function (c) { var u = byCode[c]; if (u) grand += u.k + u.s + u.a + u.t; });
    var catTotal = D.units.reduce(function (s, u) { return s + u.k + u.s + u.a + u.t; }, 0);
    var fr = memberFrac("cap");
    var gaps = D.capabilityOrder.filter(function (_, i) { return fr.every(function (f) { return f[i] === 0; }); });
    document.getElementById("pb-summary").innerHTML =
      "<strong>" + members.length + "</strong> member" + (members.length === 1 ? "" : "s") +
      " · team covers <strong>" + union.size + "</strong> of " + D.units.length + " courses (" +
      Math.round(100 * grand / catTotal) + "% of the catalogue) · " +
      (gaps.length ? "<span style='color:" + COL_GAP + "'><strong>" + gaps.length + "</strong> capability gap" + (gaps.length === 1 ? "" : "s") + ": " + esc(gaps.join(", ")) + "</span>" : "<strong>no capability gaps</strong> 🎯");
  }

  // ---- save / load / print ----
  function slug(s) { return (s || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "") || "team"; }
  function teamName() { var n = document.getElementById("pb-team-name"); return (n && n.value.trim()) || "Team"; }
  function download(fname, text) {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([text], { type: "application/json" }));
    a.download = fname; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 0);
  }
  function doSaveTeam() {
    var payload = { format: "program-builder-team", version: 1, name: teamName(), savedAt: new Date().toISOString(),
      members: members.map(function (m) { return { name: m.name, selected: Array.from(m.sel).sort() }; }) };
    download(slug(teamName()) + "-team.json", JSON.stringify(payload, null, 2));
  }
  function ingest(obj, fallbackName) {
    if (obj && Array.isArray(obj.members)) {
      if (obj.name) { var tn = document.getElementById("pb-team-name"); if (tn && !tn.value.trim()) tn.value = obj.name; }
      obj.members.forEach(function (m) { addMember(m.name, m.selected || []); });
    } else {
      var codes = Array.isArray(obj) ? obj : (obj.selected || []);
      addMember((obj && obj.name) || fallbackName, codes);
    }
  }
  function readFiles(files, cb) {
    var arr = Array.prototype.slice.call(files), done = 0;
    arr.forEach(function (file) {
      var r = new FileReader();
      r.onload = function () { try { ingest(JSON.parse(r.result), file.name.replace(/\.json$/i, "")); } catch (e) { alert("Could not read " + file.name + ": " + e.message); } if (++done === arr.length) cb(); };
      r.readAsText(file);
    });
  }
  function tableHTML(head, rows) {
    return "<table><thead><tr>" + head.map(function (h) { return "<th>" + esc(h) + "</th>"; }).join("") + "</tr></thead><tbody>" +
      rows.map(function (r) { return "<tr>" + r.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }).join("") + "</tbody></table>";
  }
  function buildReport() {
    var fr = memberFrac("cap");
    var covRows = D.capabilityOrder.map(function (capName, i) {
      var who = []; members.forEach(function (m, mi) { if (fr[mi][i] > 0) who.push(esc(m.name)); });
      var st = who.length === 0 ? "GAP" : (who.length === 1 ? "solo" : (who.length >= 3 ? "redundant" : "covered"));
      return [esc(capName), String(who.length), who.join(", ") || "—", st];
    });
    var memRows = members.map(function (m) {
      var t = { k: 0, s: 0, a: 0, ta: 0 };
      m.sel.forEach(function (c) { var u = byCode[c]; if (u) { t.k += u.k; t.s += u.s; t.a += u.a; t.ta += u.t; } });
      var codes = Array.from(m.sel).sort().join(", ");
      return [esc(m.name), String(m.sel.size), (t.k + t.s + t.a + t.ta) + " KSATs", esc(codes) || "—"];
    });
    var charts = document.getElementById("pb-radars").innerHTML;
    var css = "body{font-family:Arial,Helvetica,sans-serif;color:#222;margin:24px;font-size:12px;}" +
      "h1{font-size:20px;margin:0 0 2px;}h2{font-size:15px;border-bottom:2px solid #7e57c2;padding-bottom:3px;margin:22px 0 8px;}" +
      "table{border-collapse:collapse;width:100%;margin:4px 0 10px;}th,td{border:1px solid #cfd4da;padding:3px 6px;text-align:left;vertical-align:top;}th{background:#f3eefc;}" +
      ".meta{color:#666;margin-bottom:10px;}.pb-radar-card{display:inline-block;width:32%;vertical-align:top;}.pb-radar{width:100%;}" +
      "tr.pb-gap td{background:#fdecea;}h4{margin:6px 0 0;font-size:11px;}";
    return "<!doctype html><html><head><meta charset='utf-8'><title>" + esc(teamName()) + " — Team Report</title><style>" + css +
      "</style></head><body><h1>" + esc(teamName()) + "</h1><div class='meta'>Team coverage report · generated " +
      esc(new Date().toLocaleString()) + " · " + members.length + " members</div>" +
      "<h2>Capability coverage overlay</h2><div>" + charts + "</div>" +
      "<h2>Operational capability coverage</h2>" + tableHTML(["Capability", "Members", "Who", "Status"], covRows) +
      "<h2>Members</h2>" + tableHTML(["Member", "Courses", "KSATs", "Selected courses"], memRows) +
      "<p style='margin-top:18px;color:#888;'>Opacity in the overlays shows how many members coincide on each area; dashed line is the team's total reach. KSAT IDs and the capability mapping are project-local (provisional).</p></body></html>";
  }
  function doPrint() {
    var w = window.open("", "_blank");
    if (!w) { alert("Allow pop-ups to print the team report."); return; }
    w.document.open(); w.document.write(buildReport()); w.document.close(); w.focus();
    setTimeout(function () { try { w.print(); } catch (e) {} }, 350);
  }

  function wireActions() {
    document.getElementById("pb-add").addEventListener("click", function () { addMember(null, []); renderMembers(); syncPicker(); update(); });
    var mfile = document.getElementById("pb-memberfile");
    document.getElementById("pb-loadmember").addEventListener("click", function () { mfile.value = ""; mfile.click(); });
    mfile.addEventListener("change", function () { if (mfile.files && mfile.files.length) readFiles(mfile.files, function () { renderMembers(); syncPicker(); update(); }); });
    var tfile = document.getElementById("pb-team-file");
    document.getElementById("pb-team-load").addEventListener("click", function () { tfile.value = ""; tfile.click(); });
    tfile.addEventListener("change", function () { if (tfile.files && tfile.files.length) { members = []; readFiles(tfile.files, function () { renderMembers(); syncPicker(); update(); }); } });
    document.getElementById("pb-team-save").addEventListener("click", doSaveTeam);
    document.getElementById("pb-team-print").addEventListener("click", doPrint);
    document.getElementById("pb-mname").addEventListener("input", function (e) { if (active >= 0) { members[active].name = e.target.value || members[active].name; renderMembers(); } });
  }

  function update() { renderMembers(); renderRadars(); renderCoverage(); renderSummary(); }

  buildTree();
  buildPresets();
  wireSearch();
  wireActions();
  // Seed an illustrative, diverse team so the overlay is meaningful on first view.
  function preset(label) { var p = (D.presets || []).filter(function (x) { return x.label.indexOf(label) !== -1; })[0]; return p ? p.units : []; }
  addMember("Analyst — Threat Hunting", preset("Threat Hunting"));
  addMember("Engineer — Security Engineering", preset("Security Engineering"));
  addMember("Lead — Leadership & CISO", preset("Leadership"));
  active = 0;
  renderMembers(); syncPicker(); update();
})();
