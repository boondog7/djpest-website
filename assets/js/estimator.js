/* DJ Pest cost estimator: a guided journey from "what are you seeing" to an indicative range and a request for Dane's review.
   Prices come from estimator-data.js, generated at build time from the investment guide (one source of truth).
   Wording rules: indicative range, never a quote; every request is reviewed by Dane and confirmed by a site inspection;
   no treatment or medical advice; nothing limits Australian Consumer Law rights. Built 28 Sep 2026. */
(function () {
  var D = window.DJEST; if (!D) return;
  var P = D.prices, SMS = D.sms, TEL = D.tel, PHONE = D.phone, AREA = D.area;

  // ---------------------------------------------------------------- the journey
  // Each step: {q, help, opts:[{t, sub, go|result}], key}. A result names a price key (or null for "review needed").
  var STEPS = {
    start: { q: "What's going on?", help: "Pick the closest. You can go back at any point.", opts: [
      { t: "I'm seeing pests", sub: "ants, cockroaches, spiders, rodents and more", go: "pests" },
      { t: "Possible termites or timber damage", sub: "mud tubes, hollow timber, discarded wings", go: "termites" },
      { t: "I'm buying a property", sub: "pre-purchase timber pest inspection", go: "prepurchase" },
      { t: "Wasps or bees", sub: "a nest, a hive or a swarm", go: "wasps" },
      { t: "A business, rental or strata site", sub: "cafe, office, warehouse, strata", go: "commercial" },
      { t: "I'm not sure what it is", sub: "we'll work it out from a photo", result: { key: null, why: "notsure" } } ] },
    pests: { q: "What are you seeing?", opts: [
      { t: "Ants", go: "ants" }, { t: "Cockroaches", go: "roaches" }, { t: "Spiders", result: { key: "spider", scale: ["size"] } },
      { t: "Rats or mice", sub: "droppings, scratching, chewing", result: { key: "rodent", scale: ["stage"] } },
      { t: "Bed bugs, or bites in bed", go: "bedbugs" }, { t: "Mosquitoes in the yard", result: { key: "mosquito", scale: ["size"] } },
      { t: "Silverfish, or a mix of general pests", result: { key: "general", scale: ["size"] } },
      { t: "Something else", result: { key: null, why: "notsure" } } ] },
    ants: { q: "Where are the ants?", opts: [
      { t: "Outside, or inside and outside", sub: "trails along paving, sand between pavers", result: { key: "ants", scale: ["size", "stage"] } },
      { t: "Only inside", result: { key: "general", scale: ["size"], note: "Ants that only show up inside are usually handled as part of a general pest treatment. We'll confirm on site." } } ] },
    roaches: { q: "Which sounds more like them?", opts: [
      { t: "Small, light brown, in the kitchen or bathroom", sub: "often seen at night, near appliances", result: { key: "german", scale: ["stage"] } },
      { t: "Large and dark, often coming in from outside", result: { key: "general", scale: ["size"] } },
      { t: "Not sure", result: { key: "general", scale: ["size"], note: "If they turn out to be German cockroaches, the kitchen program applies instead (the range can be higher). Text us a photo and we'll tell you which." } } ] },
    bedbugs: { q: "What have you found?", opts: [
      { t: "Bed bugs, or their spots on the mattress or bed frame", result: { key: "bedbug", scale: ["size"] } },
      { t: "Bites, but no bugs seen", result: { key: null, why: "bites" } } ] },
    termites: { q: "What best describes it?", warn: "Please don't break open mud tubes or damaged timber, and don't spray them. Disturbing termites can make them harder to find.", opts: [
      { t: "I've seen signs", sub: "mud tubes, hollow-sounding timber, wings near windows", result: { key: "termite_insp", scale: ["size"], why: "termite" } },
      { t: "I'd like a regular termite inspection", result: { key: "termite_insp", scale: ["size"], why: "termite" } },
      { t: "I want a termite management system", sub: "new or replacing an old one", result: { key: "termite_insp", scale: ["size"], why: "termite_system" } } ] },
    prepurchase: { q: "When do you need it?", opts: [
      { t: "Within 48 hours", result: { key: "prepurchase", scale: ["size"], urgent: true } },
      { t: "This week or later", result: { key: "prepurchase", scale: ["size"] } } ] },
    wasps: { q: "Which is closest?", opts: [
      { t: "A grey papery nest under eaves, a pergola or a shrub", sub: "slim wasps with dangling legs", result: { key: "wasp" } },
      { t: "Yellow and black wasps, nest hidden in the ground or a wall", sub: "these could be European wasps", result: { key: null, why: "euro_wasp" } },
      { t: "A bee swarm hanging in the open", sub: "a clump of bees on a branch or fence", result: { key: null, why: "swarm" } },
      { t: "Bees going in and out of a wall, roof or tree", result: { key: "beehive" } } ] },
    commercial: { q: "What kind of site?", opts: [
      { t: "Food premises", sub: "cafe, restaurant, takeaway, kitchen", result: { key: "commercial", why: "commercial" } },
      { t: "Office, retail or warehouse", result: { key: "commercial", why: "commercial" } },
      { t: "Strata, rentals or aged care / childcare", result: { key: "commercial", why: "commercial" } } ] }
  };
  var SIZE = { q: "What's the property like?", opts: [
    { t: "Unit, villa or small home", v: 0 }, { t: "Standard 3-bedroom home", v: 0.45 }, { t: "4+ bedrooms or a big block", v: 0.75 },
    { t: "Large two-storey, outbuildings or long fence lines", v: 1 } ] };
  var STAGE = { q: "How long has it been going on?", opts: [
    { t: "Just started: a few sightings", v: 0 }, { t: "A few weeks: regular sightings", v: 0.5 }, { t: "Months, or they're everywhere", v: 1 } ] };

  // ---------------------------------------------------------------- state + rendering
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function money(x) { return "$" + x.toLocaleString("en-AU"); }
  function r10(x) { return Math.round(x / 10) * 10; }

  function App(root, opts) {
    this.root = root; this.hist = []; this.ans = []; this.res = null; this.scale = {}; this.preset = opts && opts.preset;
    this.go("start");
    if (this.preset) this.jump(this.preset);
  }
  App.prototype.jump = function (preset) {        // deep link from a service page: skip straight to the right branch
    var map = { ants: ["start", 0, "pests", 0, "ants", 0], cockroaches: ["start", 0, "pests", 1], spiders: ["start", 0, "pests", 2],
      rodents: ["start", 0, "pests", 3], bedbugs: ["start", 0, "pests", 4], mosquitoes: ["start", 0, "pests", 5], general: ["start", 0, "pests", 6],
      termites: ["start", 1], prepurchase: ["start", 2], wasps: ["start", 3], commercial: ["start", 4] }[preset];
    if (!map) return;
    for (var i = 0; i < map.length; i += 2) { var s = STEPS[map[i]], o = s.opts[map[i + 1]]; this.pick(map[i], o, true); }
    if (this.res) this.next(); else this.go(this.cur);
  };
  App.prototype.shell = function (inner, step) {
    var total = 5, pct = Math.min(100, Math.round((step / total) * 100));
    this.root.innerHTML = "";
    var top = el("div", "est-top");
    top.appendChild(el("div", "est-bar", '<span style="width:' + pct + '%"></span>'));
    var nav = el("div", "est-nav");
    if (this.hist.length) { var b = el("button", "est-back", "&larr; Back"); b.type = "button"; b.onclick = this.back.bind(this); nav.appendChild(b); }
    var h = el("a", "est-help", "Rather talk? " + esc(PHONE)); h.href = TEL; nav.appendChild(h);
    top.appendChild(nav); this.root.appendChild(top); this.root.appendChild(inner);
    var f = this.root.querySelector("h2,button.est-opt,input"); if (f && f.focus) try { f.focus({ preventScroll: true }); } catch (e) {}
  };
  App.prototype.go = function (id) { this.cur = id; this.render(STEPS[id], id); };
  App.prototype.render = function (s, id) {
    var w = el("div", "est-step"); w.appendChild(el("h2", "est-q", esc(s.q))); w.querySelector("h2").tabIndex = -1;
    if (s.help) w.appendChild(el("p", "est-sub", esc(s.help)));
    if (s.warn) w.appendChild(el("p", "est-warn", esc(s.warn)));
    var self = this, list = el("div", "est-opts");
    s.opts.forEach(function (o) {
      var b = el("button", "est-opt", "<strong>" + esc(o.t) + "</strong>" + (o.sub ? "<span>" + esc(o.sub) + "</span>" : ""));
      b.type = "button"; b.onclick = function () { self.pick(id, o); }; list.appendChild(b);
    });
    w.appendChild(list); this.shell(w, this.hist.length);
  };
  App.prototype.pick = function (id, o, silent) {
    this.hist.push({ id: this.cur, ans: this.ans.slice(), res: this.res, scale: JSON.parse(JSON.stringify(this.scale)) });
    this.ans.push([STEPS[id] ? STEPS[id].q : id, o.t]);
    if (o.go) return silent ? (this.cur = o.go) : this.go(o.go);
    this.res = o.result; this.queue = (o.result.scale || []).slice();
    if (!silent) this.next();
  };
  App.prototype.next = function () {
    var self = this;
    if (this.queue.length) {
      var k = this.queue.shift(), s = k === "size" ? SIZE : STAGE;
      var w = el("div", "est-step"); w.appendChild(el("h2", "est-q", esc(s.q))); w.querySelector("h2").tabIndex = -1;
      var list = el("div", "est-opts");
      s.opts.forEach(function (o) {
        var b = el("button", "est-opt", "<strong>" + esc(o.t) + "</strong>"); b.type = "button";
        b.onclick = function () { self.hist.push({ id: "scale", ans: self.ans.slice(), res: self.res, scale: JSON.parse(JSON.stringify(self.scale)), queue: [k].concat(self.queue) }); self.ans.push([s.q, o.t]); self.scale[k] = o.v; self.next(); };
        list.appendChild(b);
      });
      w.appendChild(list); return this.shell(w, this.hist.length);
    }
    this.suburb();
  };
  App.prototype.back = function () {
    var h = this.hist.pop(); if (!h) return;
    this.ans = h.ans; this.res = h.res; this.scale = h.scale;
    if (h.id === "scale") { this.queue = h.queue; this.next(); } else if (h.id === "suburb" || h.id === "result") { this.queue = []; if (h.id === "result") this.suburb(true); else this.next(); } else this.go(h.id);
  };
  App.prototype.suburb = function (popped) {
    var self = this;
    var w = el("div", "est-step");
    w.appendChild(el("h2", "est-q", "Which suburb is the property in?")); w.querySelector("h2").tabIndex = -1;
    w.appendChild(el("p", "est-sub", "We work across Perth's northern suburbs. The suburb is all we need for now, not the street address."));
    var dl = el("datalist"); dl.id = "est-sub-list"; AREA.forEach(function (a) { var o = el("option"); o.value = a; dl.appendChild(o); });
    var inp = el("input", "est-input"); inp.id = "est-suburb"; inp.setAttribute("list", "est-sub-list"); inp.setAttribute("autocomplete", "address-level2");
    inp.placeholder = "e.g. Duncraig"; inp.value = this.sub || "";
    var lab = el("label", "est-label", "Suburb"); lab.htmlFor = "est-suburb";
    var b = el("button", "btn btn-primary est-go", "See my range"); b.type = "button";
    b.onclick = function () { var v = inp.value.trim(); if (v.length < 2) { inp.focus(); inp.setAttribute("aria-invalid", "true"); return; }
      self.sub = v; self.hist.push({ id: "suburb", ans: self.ans.slice(), res: self.res, scale: JSON.parse(JSON.stringify(self.scale)) }); self.result(); };
    inp.onkeydown = function (e) { if (e.key === "Enter") b.onclick(); };
    w.appendChild(lab); w.appendChild(inp); w.appendChild(dl); w.appendChild(b);
    this.shell(w, 4);
  };

  // ---------------------------------------------------------------- result
  var WHY = {
    notsure: ["We'd rather look than guess", "Pest control only works when the pest is identified properly. Text us a photo (or send the request below) and Dane will tell you what it most likely is and what it would take. No range until we know what it is."],
    bites: ["Bites alone don't tell us the pest", "Bites can come from bed bugs, fleas, mites, mosquitoes or something else entirely, so we don't put a figure on it yet. Dane will help you work out what it is first, usually from a photo or a quick look. If a bite is getting worse or someone feels unwell, see a doctor."],
    euro_wasp: ["Please report it: this one's free", "Suspected European wasps are a declared pest in WA. Don't disturb the nest. Report it to DPIRD on (08) 9368 3080 or through the MyPestGuide Reporter app, and their team investigates at no charge. If it turns out to be a paper wasp, we can help."],
    swarm: ["A swarm usually needs a beekeeper, not us", "A clump of bees hanging in the open is a swarm resting on its way to a new home, and it often moves on within a day or two. Keep clear and call a local beekeeper for a live collection. We'll give you a name at no charge. If the bees move into a wall or roof, that's when we can help."],
    termite: ["Termite work always starts with an inspection", "Below is the inspection range. Whether anything else is needed, and what it would take, depends on what the inspection finds. Any treatment is designed for your house and quoted in writing after the inspection, never from a website."],
    termite_system: ["A termite system is designed around your house", "What a system involves depends on the perimeter, the construction and what's already there, so it's always quoted in writing after an inspection. Below is the inspection range. Our investment guide shows typical ranges for full systems."],
    commercial: ["Commercial sites are quoted per visit after a site survey", "The survey is free. The range below is our typical per-visit range across site types. Food premises, reporting and after-hours access can change it, and Dane confirms it after the survey."]
  };
  App.prototype.result = function () {
    var r = this.res, w = el("div", "est-step est-result"), self = this;
    var why = r.why && WHY[r.why];
    var inArea = AREA.some(function (a) { return a.toLowerCase() === (self.sub || "").toLowerCase(); });
    var html = "", summary = "";
    if (r.key && P[r.key]) {
      var p = P[r.key], sc = r.scale || [], t;
      if (!sc.length) t = 0.5; else t = sc.reduce(function (s, k) { return s + (self.scale[k] != null ? self.scale[k] : 0.5); }, 0) / sc.length;
      var span = p.hi - p.lo, lo = r10(Math.max(p.lo, p.lo + span * t - span * 0.18)), hi = r10(Math.min(p.hi, p.lo + span * t + span * 0.18));
      if (r.why === "commercial" || !sc.length) { lo = p.lo; hi = p.hi; }
      var l = ((lo - p.lo) / (span || 1)) * 100, wd = ((hi - lo) / (span || 1)) * 100;
      html += '<div class="mono eyebrow">' + esc(p.name) + "</div>";
      html += '<div class="est-range">' + money(lo) + " to " + money(hi) + "</div>";
      html += '<p class="est-sub">Indicative range for your answers, GST included' + (r.why === "commercial" ? ", per visit" : "") + ". Our full published range for this service is " + money(p.lo) + " to " + money(p.hi) + ".</p>";
      html += '<div class="est-scale" aria-hidden="true"><span style="left:' + l + "%;width:" + Math.max(wd, 4) + '%"></span></div>';
      if (p.inc) html += '<p><strong>Usually includes:</strong> ' + esc(p.inc) + "</p>";
      summary = p.name + ": indicative " + money(lo) + " to " + money(hi);
    } else {
      summary = "No range yet (" + (r.why || "review") + ")";
    }
    if (why) html = '<h2 class="est-q" tabindex="-1">' + esc(why[0]) + '</h2><p>' + esc(why[1]) + "</p>" + html; else html = '<h2 class="est-q" tabindex="-1">Your indicative range</h2>' + html;
    if (r.note) html += '<p class="est-warn">' + esc(r.note) + "</p>";
    if (r.urgent) html += '<p class="est-warn">Tight timeframe? Call ' + esc(PHONE) + " as well, so Dane sees it straight away.</p>";
    if (!inArea) html += '<p class="est-warn">' + esc(this.sub) + " may be outside our usual area. Send it through anyway and Dane will tell you straight if we can help.</p>";
    if (r.key) html += '<p><strong>What moves it:</strong> the size of the property, how established the problem is, access (roof void, sub-floor, gates, pets) and what we find on the day.</p>';
    html += '<div class="est-legal"><strong>An indicative range, not a quote.</strong> It\'s worked out from our published <a href="/pest-control-prices-perth">investment guide</a> and your answers, which we haven\'t checked yet. Every request is reviewed by Dane, and the work is confirmed by a site inspection before you get a written, itemised quote. The final investment can be lower or higher than this range, and nothing is booked until you accept the written quote. General information only, not treatment, medical or other professional advice. Nothing here limits your rights under the Australian Consumer Law.</div>';
    w.innerHTML = html;
    this.summary = summary;
    // hand-off
    var f = el("form", "est-form"); f.noValidate = true;
    f.innerHTML = '<h3>Send this to Dane for review</h3><p class="est-sub">He looks at every request himself and gets back to you to arrange a look. Text a photo as well if you can: it helps.</p>' +
      '<label class="est-label" for="est-name">Your name</label><input class="est-input" id="est-name" autocomplete="given-name" required>' +
      '<label class="est-label" for="est-phone">Mobile</label><input class="est-input" id="est-phone" type="tel" autocomplete="tel" inputmode="tel" required>' +
      '<label class="est-label" for="est-note">Anything else? (optional)</label><textarea class="est-input" id="est-note" rows="3" placeholder="Where you\'ve seen it, access, pets, best time to call"></textarea>' +
      '<input type="text" name="website" id="est-hp" tabindex="-1" autocomplete="off" class="est-hp" aria-hidden="true">' +
      '<p class="est-small">We use your details only to review this request and contact you about it. We don\'t add you to marketing and don\'t share your details. See our <a href="/privacy">privacy policy</a>.</p>' +
      '<div class="est-actions"><button class="btn btn-primary" type="submit">Send for Dane\'s review</button><a class="btn btn-ghost" id="est-sms">Text a photo instead</a></div><p class="est-msg" role="status"></p>';
    w.appendChild(f);
    this.shell(w, 5);
    var body = "Hi DJ Pest, from the website estimator. " + this.ans.map(function (a) { return a[1]; }).join("; ") + ". Suburb: " + this.sub + ". " + summary + ". (Photo attached)";
    f.querySelector("#est-sms").href = SMS + "?&body=" + encodeURIComponent(body);
    f.onsubmit = function (e) {
      e.preventDefault();
      var n = f.querySelector("#est-name"), ph = f.querySelector("#est-phone"), m = f.querySelector(".est-msg");
      if (n.value.trim().length < 2) { n.setAttribute("aria-invalid", "true"); n.focus(); return; }
      if (ph.value.replace(/\D/g, "").length < 8) { ph.setAttribute("aria-invalid", "true"); ph.focus(); return; }
      var ref = "E" + Date.now().toString(36).toUpperCase().slice(-6);
      var msg = "ESTIMATOR REQUEST " + ref + " (needs Dane's review + site inspection before any quote)\n" +
        self.ans.map(function (a) { return a[0] + " " + a[1]; }).join("\n") + "\nSuburb: " + self.sub + (inArea ? "" : " (check service area)") +
        "\nShown: " + summary + (f.querySelector("#est-note").value.trim() ? "\nNote: " + f.querySelector("#est-note").value.trim() : "");
      var btn = f.querySelector('button[type="submit"]'); btn.disabled = true; m.textContent = "Sending…";
      fetch("/api/contact", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({
        name: n.value.trim(), phone: ph.value.trim(), suburb: self.sub, pest: "Estimator: " + (r.key && P[r.key] ? P[r.key].name : (r.why || "not sure")),
        message: msg, website: f.querySelector("#est-hp").value }) })
        .then(function (x) { return x.json().catch(function () { return {}; }).then(function (j) { if (!x.ok || j.ok === false) throw 0; }); })
        .then(function () { self.done(ref); })
        .catch(function () { btn.disabled = false; m.innerHTML = "That didn't send. Please text us on <a href=\"" + SMS + "\">" + esc(PHONE) + "</a> instead."; });
    };
  };
  App.prototype.done = function (ref) {
    var w = el("div", "est-step est-result");
    w.innerHTML = '<h2 class="est-q" tabindex="-1">Sent. Thanks.</h2><p>Your reference is <strong>' + ref + "</strong>. Dane will review your answers and contact you to arrange a look.</p>" +
      "<p>What happens next: he checks what you've described, may ask for a photo, then inspects the property and gives you a written, itemised quote. Nothing is booked until you accept it.</p>" +
      '<p class="est-small">Something urgent? Call ' + esc(PHONE) + ".</p>";
    this.shell(w, 5);
  };

  // ---------------------------------------------------------------- mount: inline on the estimator page, pop-up everywhere else
  function mountInline() { var r = document.getElementById("est-app"); if (r) { r.innerHTML = ""; new App(r, { preset: new URLSearchParams(location.search).get("pest") }); } }
  var dlg;
  function open(preset) {
    if (!dlg) {
      dlg = el("dialog", "est-dialog"); dlg.setAttribute("aria-label", "Cost estimator");
      var x = el("button", "est-close", "&times;"); x.type = "button"; x.setAttribute("aria-label", "Close"); x.onclick = function () { dlg.close(); };
      dlg.appendChild(x); dlg.appendChild(el("div", "est-card")); document.body.appendChild(dlg);
      dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
    }
    var card = dlg.querySelector(".est-card"); card.innerHTML = ""; new App(card, { preset: preset });
    if (dlg.showModal) dlg.showModal(); else location.href = "/pest-control-cost-estimator" + (preset ? "?pest=" + preset : "");
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("[data-est]"); if (!a) return;
    if (document.getElementById("est-app")) { e.preventDefault(); mountInline(); document.getElementById("est-app").scrollIntoView({ behavior: "smooth" }); return; }
    e.preventDefault(); open(a.getAttribute("data-est") || null);
  });
  if (document.readyState !== "loading") mountInline(); else document.addEventListener("DOMContentLoaded", mountInline);
})();
