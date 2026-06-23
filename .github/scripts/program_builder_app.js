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
