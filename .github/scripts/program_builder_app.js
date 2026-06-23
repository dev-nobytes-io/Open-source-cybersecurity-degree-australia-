/* Program Builder — live employability explorer.
 *
 * Vanilla JS, no dependencies. Consumes window.PROGRAM_DATA and renders, live as
 * the user ticks courses:
 *   - a searchable course picker grouped by degree -> year -> major;
 *   - NICE/DCWF work-role completion bars;
 *   - four radar ("spider web") charts on DIFFERENT category systems, framed as
 *     "what can I employ this person to do?": operational capabilities,
 *     NICE work categories, cognitive depth (Bloom's), and knowledge-vs-doing;
 *   - a learning-composition donut;
 *   - Save / Load (JSON) and a printable program report.
 *
 * KSAT IDs and the capability mapping are project-local (provisional) pending
 * Framework Custodian mapping.
 */
(function () {
  "use strict";
  var D = window.PROGRAM_DATA;
  if (!D || !document.getElementById("pb-tree")) return;

  var SVGNS = "http://www.w3.org/2000/svg";
  var COL_CAT = "#9aa7b4", COL_SEL = "#7e57c2";
  var TYPE_NAME = { K: "Knowledge", S: "Skill", A: "Ability", T: "Task" };

  var byCode = {};
  D.units.forEach(function (u) { byCode[u.code] = u; });
  var selected = new Set();

  // Work-role universes.
  var roleName = {}, roleUniverse = {};
  D.units.forEach(function (u) {
    var tot = u.k + u.s + u.a + u.t;
    u.roles.forEach(function (r) { roleName[r[0]] = r[1]; roleUniverse[r[0]] = (roleUniverse[r[0]] || 0) + tot; });
  });
  var catTotal = D.units.reduce(function (s, u) { return s + u.k + u.s + u.a + u.t; }, 0);

  // The four radar lenses (each a different category system).
  var LENSES = [
    { key: "cap", title: "Operational capabilities", desc: "Hands-on use-cases — the jobs they can do", axes: D.capabilityOrder },
    { key: "nice", title: "NICE/DCWF work categories", desc: "Breadth across the workforce taxonomy", axes: D.niceOrder },
    { key: "bloom", title: "Cognitive depth (Bloom's)", desc: "Operate → analyse → design & lead", axes: D.bloomLabels },
    { key: "mix", title: "Knowledge vs doing", desc: "Theory vs hands-on balance", axes: ["Knowledge", "Skills", "Abilities", "Tasks"] }
  ];

  function lensVectors(codes) {
    var capI = {}; D.capabilityOrder.forEach(function (c, i) { capI[c] = i; });
    var niceI = {}; D.niceOrder.forEach(function (c, i) { niceI[c] = i; });
    var v = {
      cap: D.capabilityOrder.map(function () { return 0; }),
      nice: D.niceOrder.map(function () { return 0; }),
      bloom: D.bloomLabels.map(function () { return 0; }),
      mix: [0, 0, 0, 0]
    };
    var list = codes || D.units.map(function (u) { return u.code; });
    list.forEach(function (code) {
      var u = byCode[code]; if (!u) return;
      var tot = u.k + u.s + u.a + u.t;
      if (capI[u.cap] != null) v.cap[capI[u.cap]] += tot;
      var cats = {};
      u.roles.forEach(function (r) { var c = D.niceOf[r[0].split("-")[0]]; if (c) cats[c] = 1; });
      Object.keys(cats).forEach(function (c) { if (niceI[c] != null) v.nice[niceI[c]] += tot; });
      for (var i = 0; i < 6; i++) v.bloom[i] += (u.bloom[i] || 0);
      v.mix[0] += u.k; v.mix[1] += u.s; v.mix[2] += u.a; v.mix[3] += u.t;
    });
    return v;
  }
  var catVec = lensVectors(null);

  // ---- DOM helpers ----
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
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // ---- course picker ----
  var unitCheckboxes = {}, groupNodes = [];
  function buildTree() {
    var tree = document.getElementById("pb-tree"); tree.innerHTML = "";
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
      var details = el("details", { class: "pb-deg", open: "" });
      var sm = el("summary", {});
      var dgChk = el("input", { type: "checkbox", class: "pb-grp" });
      dgChk.addEventListener("click", function (e) { e.stopPropagation(); });
      dgChk.addEventListener("change", function () { setMany(dgCodes, dgChk.checked); });
      sm.appendChild(dgChk); sm.appendChild(el("span", {}, [dname]));
      var dgCount = el("span", { class: "pb-count" }); sm.appendChild(dgCount);
      details.appendChild(sm);
      dg.order.forEach(function (yname) {
        var yr = dg.years[yname];
        details.appendChild(el("div", { class: "pb-year" }, [yname]));
        yr.order.forEach(function (aname) {
          var units = yr.areas[aname], aCodes = units.map(function (u) { return u.code; });
          dgCodes = dgCodes.concat(aCodes);
          var area = el("div", { class: "pb-area" });
          var ah = el("label", { class: "pb-area-h" });
          var aChk = el("input", { type: "checkbox", class: "pb-grp" });
          aChk.addEventListener("change", function () { setMany(aCodes, aChk.checked); });
          ah.appendChild(aChk); ah.appendChild(el("span", {}, [aname]));
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
    var grand = t.k + t.s + t.a + t.t, pct = catTotal ? Math.round(100 * grand / catTotal) : 0;
    document.getElementById("pb-summary").innerHTML =
      "<strong>" + selected.size + "</strong> of " + D.units.length + " courses · <strong>" +
      grand + "</strong> KSAT items (" + t.k + " K · " + t.s + " S · " + t.a + " A · " + t.t +
      " T) · <strong>" + pct + "%</strong> of the full catalogue (" + catTotal + " items).";
  }
  function renderBars(rows) {
    var host = document.getElementById("pb-bars"); host.innerHTML = "";
    rows.forEach(function (r) {
      var row = el("div", { class: "pb-bar-row", title: r.name + " (" + r.code + ") — " + r.cov + "/" + r.uni + " KSATs" });
      row.appendChild(el("span", { class: "pb-bar-label" }, [r.code]));
      var track = el("div", { class: "pb-bar-track" }), fill = el("div", { class: "pb-bar-fill" });
      fill.style.width = r.pct + "%"; if (r.pct === 0) fill.classList.add("pb-bar-zero");
      track.appendChild(fill); row.appendChild(track);
      row.appendChild(el("span", { class: "pb-bar-pct" }, [r.pct + "%"]));
      host.appendChild(row);
    });
  }
  function radar(axes, catVals, selVals, maxv, title) {
    var W = 300, H = 250, cx = 150, cy = 128, R = 88, rings = 4;
    var svg = sv("svg", { viewBox: "0 0 " + W + " " + H, class: "pb-radar", role: "img", "aria-label": title });
    function pt(i, frac) { var a = -Math.PI / 2 + i * 2 * Math.PI / axes.length; return [cx + R * frac * Math.cos(a), cy + R * frac * Math.sin(a)]; }
    for (var g = 1; g <= rings; g++) {
      var d = axes.map(function (_, i) { var p = pt(i, g / rings); return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + " Z";
      svg.appendChild(sv("path", { d: d, fill: "none", stroke: "#d7dce1", "stroke-width": "1" }));
    }
    axes.forEach(function (label, i) {
      var p = pt(i, 1);
      svg.appendChild(sv("line", { x1: cx, y1: cy, x2: p[0], y2: p[1], stroke: "#d7dce1", "stroke-width": "1" }));
      var lp = pt(i, 1.17), t = sv("text", { x: lp[0].toFixed(1), y: lp[1].toFixed(1), "font-size": "8.5",
        "text-anchor": lp[0] < cx - 4 ? "end" : (lp[0] > cx + 4 ? "start" : "middle"), "dominant-baseline": "middle", fill: "currentColor" });
      t.textContent = label; svg.appendChild(t);
    });
    function poly(vals, color, op) {
      var d = vals.map(function (v, i) { var p = pt(i, maxv ? v / maxv : 0); return (i ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" ") + " Z";
      svg.appendChild(sv("path", { d: d, fill: color, "fill-opacity": op, stroke: color, "stroke-width": "1.5" }));
    }
    poly(catVals, COL_CAT, "0.10"); poly(selVals, COL_SEL, "0.40");
    return svg;
  }
  function renderRadars(selVec) {
    var host = document.getElementById("pb-radars"); host.innerHTML = "";
    LENSES.forEach(function (L) {
      var maxv = Math.max.apply(null, catVec[L.key].concat([1]));
      var card = el("div", { class: "pb-radar-card" });
      card.appendChild(el("h4", {}, [L.title]));
      card.appendChild(el("p", {}, [L.desc]));
      card.appendChild(radar(L.axes, catVec[L.key], selVec[L.key], maxv, L.title));
      host.appendChild(card);
    });
  }
  function renderDonut(t) {
    var host = document.getElementById("pb-donut"); host.innerHTML = "";
    var grand = t.k + t.s + t.a + t.t;
    var parts = [["Knowledge", t.k, "#7e57c2"], ["Skills", t.s, "#26a69a"], ["Abilities", t.a, "#ef6c00"], ["Tasks", t.t, "#1e88e5"]];
    var svg = sv("svg", { viewBox: "0 0 120 120", class: "pb-donut", role: "img", "aria-label": "Learning composition" });
    var cx = 60, cy = 60, r = 45, circ = 2 * Math.PI * r, off = 0;
    if (grand === 0) { svg.appendChild(sv("circle", { cx: cx, cy: cy, r: r, fill: "none", stroke: "#e0e4e8", "stroke-width": "18" })); }
    else parts.forEach(function (p) {
      if (!p[1]) return; var len = circ * p[1] / grand;
      svg.appendChild(sv("circle", { cx: cx, cy: cy, r: r, fill: "none", stroke: p[2], "stroke-width": "18",
        "stroke-dasharray": len.toFixed(2) + " " + (circ - len).toFixed(2), "stroke-dashoffset": (-off).toFixed(2),
        transform: "rotate(-90 " + cx + " " + cy + ")" }));
      off += len;
    });
    var ctr = sv("text", { x: cx, y: cy, "text-anchor": "middle", "dominant-baseline": "central", "font-size": "16", "font-weight": "700", fill: "currentColor" });
    ctr.textContent = String(grand); svg.appendChild(ctr);
    var wrap = el("div", { class: "pb-donut-wrap" }); wrap.appendChild(svg);
    var legend = el("div", { class: "pb-legend" });
    parts.forEach(function (p) {
      var item = el("span", { class: "pb-legend-item" });
      item.appendChild(el("span", { class: "pb-swatch" })).style.background = p[2];
      item.appendChild(document.createTextNode(" " + p[0] + " " + p[1]));
      legend.appendChild(item);
    });
    wrap.appendChild(legend); host.appendChild(wrap);
  }

  // ---- save / load / print ----
  function slug(s) { return (s || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "") || "program"; }
  function nameVal() { var n = document.getElementById("pb-name"); return (n && n.value.trim()) || "Custom program"; }
  function download(fname, text, type) {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([text], { type: type || "application/json" }));
    a.download = fname; document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 0);
  }
  function doSave() {
    var payload = { format: "program-builder", version: 1, name: nameVal(), savedAt: new Date().toISOString(), selected: Array.from(selected).sort() };
    download(slug(nameVal()) + ".json", JSON.stringify(payload, null, 2));
  }
  function doLoad(file) {
    var rdr = new FileReader();
    rdr.onload = function () {
      try {
        var obj = JSON.parse(rdr.result);
        var codes = Array.isArray(obj) ? obj : (obj.selected || []);
        selected = new Set(codes.filter(function (c) { return byCode[c]; }));
        if (obj && obj.name) { var n = document.getElementById("pb-name"); if (n) n.value = obj.name; }
        update();
      } catch (e) { alert("Could not read that file: " + e.message); }
    };
    rdr.readAsText(file);
  }
  function tableHTML(head, rows) {
    return "<table><thead><tr>" + head.map(function (h) { return "<th>" + esc(h) + "</th>"; }).join("") +
      "</tr></thead><tbody>" + rows.map(function (r) {
        return "<tr>" + r.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>";
      }).join("") + "</tbody></table>";
  }
  function buildReport() {
    var t = totals(), grand = t.k + t.s + t.a + t.t;
    var pct = catTotal ? Math.round(100 * grand / catTotal) : 0;
    var selVec = lensVectors(Array.from(selected));
    var ordered = D.units.filter(function (u) { return selected.has(u.code); });

    var courses = ordered.map(function (u) {
      return [u.code, esc(u.title), esc(u.area), (u.k + u.s + u.a + u.t)];
    });
    var capRows = D.capabilityOrder.map(function (c, i) { return [esc(c), selVec.cap[i] + " / " + catVec.cap[i]]; });
    var niceRows = D.niceOrder.map(function (c, i) { return [esc(c), selVec.nice[i] + " / " + catVec.nice[i]]; });
    var bloomRows = D.bloomLabels.map(function (c, i) { return [esc(c), selVec.bloom[i] + " / " + catVec.bloom[i]]; });
    var roles = roleRows().filter(function (r) { return r.uni > 0; })
      .map(function (r) { return [esc(r.name), r.code, r.cov + " / " + r.uni, r.pct + "%"]; });

    var ksatBlocks = ordered.map(function (u) {
      var rows = u.ksats.map(function (k) { return [TYPE_NAME[k[0]] || k[0], k[1], esc(k[2]), esc(k[3])]; });
      return "<h3>" + u.code + " — " + esc(u.title) + "</h3>" + tableHTML(["Type", "ID", "Statement", "Demonstrated in"], rows);
    }).join("");

    var charts = document.getElementById("pb-radars").innerHTML;
    var bars = document.getElementById("pb-bars").innerHTML;
    var donut = document.getElementById("pb-donut").innerHTML;

    var css = "body{font-family:Arial,Helvetica,sans-serif;color:#222;margin:24px;font-size:12px;}" +
      "h1{font-size:20px;margin:0 0 2px;}h2{font-size:15px;border-bottom:2px solid #7e57c2;padding-bottom:3px;margin:22px 0 8px;}" +
      "h3{font-size:12.5px;margin:14px 0 4px;}table{border-collapse:collapse;width:100%;margin:4px 0 10px;}" +
      "th,td{border:1px solid #cfd4da;padding:3px 6px;text-align:left;vertical-align:top;}th{background:#f3eefc;}" +
      ".meta{color:#666;margin-bottom:10px;}.pb-radar-card{display:inline-block;width:32%;vertical-align:top;}" +
      ".pb-radar{width:100%;}.pb-bar-row{display:flex;gap:6px;align-items:center;margin:2px 0;}" +
      ".pb-bar-label{flex:0 0 7em;font-weight:bold;}.pb-bar-track{flex:1;height:11px;background:#eceff1;border-radius:6px;overflow:hidden;}" +
      ".pb-bar-fill{height:100%;background:#7e57c2;}.pb-bar-pct{flex:0 0 3em;text-align:right;}" +
      ".pb-donut{width:120px;}.pb-legend{display:inline-block;vertical-align:top;margin-left:12px;}.pb-swatch{display:inline-block;width:9px;height:9px;margin-right:4px;}" +
      "@media print{h2{page-break-after:avoid;}table{page-break-inside:auto;}tr{page-break-inside:avoid;}}";

    return "<!doctype html><html><head><meta charset='utf-8'><title>" + esc(nameVal()) +
      " — Program Report</title><style>" + css + "</style></head><body>" +
      "<h1>" + esc(nameVal()) + "</h1>" +
      "<div class='meta'>Program report · generated " + esc(new Date().toLocaleString()) +
      " · " + selected.size + " of " + D.units.length + " courses · " + grand + " KSAT items (" +
      t.k + " K · " + t.s + " S · " + t.a + " A · " + t.t + " T) · " + pct + "% of catalogue</div>" +
      "<h2>Work-role completion</h2>" + bars +
      "<h2>Capability lenses — what can I employ this person to do?</h2><div>" + charts + "</div>" +
      "<h2>Learning composition</h2>" + donut +
      "<h2>Operational capabilities (Selected / Catalogue)</h2>" + tableHTML(["Capability", "KSATs"], capRows) +
      "<h2>NICE/DCWF work categories (Selected / Catalogue)</h2>" + tableHTML(["Category", "KSATs"], niceRows) +
      "<h2>Cognitive depth — Bloom's (Selected / Catalogue)</h2>" + tableHTML(["Level", "Outcomes"], bloomRows) +
      "<h2>Work-role completion detail</h2>" + tableHTML(["Work role", "Code", "Covered / Catalogue", "%"], roles) +
      "<h2>Selected courses</h2>" + tableHTML(["Code", "Title", "Area", "KSATs"], courses) +
      "<h2>Full KSAT listing</h2>" + (ksatBlocks || "<p>No courses selected.</p>") +
      "<p style='margin-top:20px;color:#888;'>KSAT IDs and the capability mapping are project-local (provisional) pending Framework Custodian mapping to official NICE/DCWF identifiers.</p>" +
      "</body></html>";
  }
  function doPrint() {
    var w = window.open("", "_blank");
    if (!w) { alert("Allow pop-ups to print the program report."); return; }
    w.document.open(); w.document.write(buildReport()); w.document.close(); w.focus();
    setTimeout(function () { try { w.print(); } catch (e) {} }, 350);
  }
  function wireActions() {
    document.getElementById("pb-save").addEventListener("click", doSave);
    var file = document.getElementById("pb-file");
    document.getElementById("pb-load").addEventListener("click", function () { file.value = ""; file.click(); });
    file.addEventListener("change", function () { if (file.files && file.files[0]) doLoad(file.files[0]); });
    document.getElementById("pb-print").addEventListener("click", doPrint);
  }

  function update() {
    syncChecks();
    var t = totals();
    renderSummary(t);
    renderBars(roleRows());
    renderRadars(lensVectors(Array.from(selected)));
    renderDonut(t);
  }

  buildTree();
  buildPresets();
  wireSearch();
  wireActions();
  if (D.presets && D.presets.length) { selected = new Set(D.presets[0].units); }
  update();
})();
