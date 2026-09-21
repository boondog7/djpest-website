#!/usr/bin/env python3
"""DJ Pest static site generator (v2, rat-in-crosshair brand).

Shared chrome + page modules -> plain static HTML for Cloudflare Pages.
    python3 build/build.py            # build everything into repo root
    python3 build/build.py --check    # build + compliance scan only

Page modules live in build/pages/*.py and expose `pages(ctx) -> list[dict]` where each dict has:
    path      "/termite-inspection-perth"   (no .html; "/" for home; "/blog/x" allowed)
    title     <title>
    desc      meta description (<=160 chars)
    body      inner HTML between header and footer (use ctx helpers)
    schema    list of JSON-LD dicts (optional; site graph is added automatically)
    crumbs    [("Services","/services"),("Termites",None)]  (optional)
    og_image  path (optional)
    noindex   True to add robots noindex (optional)
"""
import json, os, pathlib, re, sys, importlib.util, datetime, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = json.loads((ROOT / "build" / "site.json").read_text())
DOMAIN = SITE["domain"]
TODAY = datetime.date.today().isoformat()
import hashlib
CSS_VER = hashlib.md5((ROOT / "assets" / "css" / "site.css").read_bytes()).hexdigest()[:8]

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(str(s), quote=True)

def icon(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<g id="i-phone"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></g>
<g id="i-message"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></g>
<g id="i-shield"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></g>
<g id="i-pin"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></g>
<g id="i-check"><path d="M20 6 9 17l-5-5"/></g>
<g id="i-arrow"><path d="M5 12h14M13 6l6 6-6 6"/></g>
<g id="i-doc"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h8"/></g>
<g id="i-clock"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></g>
<g id="i-mail"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7L22 6"/></g>
<g id="i-menu"><path d="M4 7h16M4 12h16M4 17h16"/></g>
<g id="i-target"><circle cx="12" cy="12" r="8"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/><circle cx="12" cy="12" r="2"/></g>
</defs></svg>"""

def btn_call(label=None, cls="btn btn-primary"):
    label = label or f"Call {SITE['phone_display']}"
    return f'<a class="{cls}" href="tel:{SITE["phone_tel"]}">{icon("phone")}{esc(label)}</a>'

def btn_quote(label="Get an honest quote", cls="btn btn-ghost", href="#quote"):
    return f'<a class="{cls}" href="{href}">{esc(label)}{icon("arrow")}</a>'

def hours_cue():
    return (f'<p class="hours-cue">Mon–Sat 7am–6pm. After hours, text a photo to '
            f'<a href="{SITE["phone_sms"]}">{SITE["phone_display"]}</a> and we reply first thing.</p>')

def eyebrow(text): return f'<div class="eyebrow mono">{esc(text)}</div>'

def section(inner, cls="", id_=""):
    idattr = f' id="{id_}"' if id_ else ""
    return f'<section class="{cls}"{idattr}><div class="wrap">{inner}</div></section>'

def card(title, text, href=None, num=None, img=None, alt="", more="Learn more"):
    n = f'<div class="num">{esc(num)}</div>' if num else ""
    im = f'<img src="{img}" alt="{esc(alt)}" width="600" height="400" loading="lazy">' if img else ""
    body = f'{im}{n}<h3>{esc(title)}</h3><p>{text}</p>'
    if href:
        return f'<a class="card" href="{href}">{body}<span class="more">{esc(more)} {icon("arrow","icon")}</span></a>'
    return f'<div class="card">{body}</div>'

def steps(items):
    return '<div class="steps">' + "".join(f'<div class="step"><h3>{esc(t)}</h3><p>{d}</p></div>' for t, d in items) + "</div>"

def faq(items):
    return '<div class="faq">' + "".join(f'<details><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in items) + "</div>"

def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in items]}

def ledger_table(headers, rows, amount_cols=()):
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = ""
    for r in rows:
        tds = "".join(f'<td class="{"amount" if i in amount_cols else ""}">{c}</td>' for i, c in enumerate(r))
        trs += f"<tr>{tds}</tr>"
    return f'<div class="table-wrap"><table class="ledger-table"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'

def season_strip():
    return """<div class="season">
<div><span class="m">Sep – Nov</span><strong>Spring: ants and spiders wake up</strong><p>Warmer soil brings coastal brown ants and redbacks out. Good time for a perimeter treatment before summer.</p></div>
<div><span class="m">Nov – Apr</span><strong>Summer: termite swarm season</strong><p>Subterranean termites swarm on warm, humid evenings. Sandy northern-suburb soils and garden timber raise the risk.</p></div>
<div><span class="m">Mar – May</span><strong>Autumn: cockroaches move indoors</strong><p>German and Australian cockroaches follow warmth and food into kitchens as nights cool.</p></div>
<div><span class="m">May – Aug</span><strong>Winter: rodents in the roof</strong><p>Rats and mice look for warm voids. Sealing entry points now beats baiting later.</p></div>
</div>"""

def quote_block(heading="Get an honest, itemised quote.", intro=None):
    intro = intro or ("Tell us what you're seeing and where. We'll call you back with a written, itemised quote before anything is booked. "
                      "No obligation, no pressure.")
    suburbs = "".join(f'<option>{esc(s)}</option>' for s in SITE["service_area"])
    return f"""<section class="quote" id="quote"><div class="wrap">
  <div>
    {eyebrow("Quote request")}
    <h2>{esc(heading)}</h2>
    <p class="lead">{intro}</p>
    <p>Prefer to talk? {btn_call(cls="btn btn-light")}</p>
    <p class="notice">Or text photos of the pest or droppings to <a href="{SITE['phone_sms']}">{SITE['phone_display']}</a> and we'll identify it.</p>
  </div>
  <form class="lead-form" id="leadForm" method="POST" action="/api/contact" novalidate>
    <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" aria-label="Leave this field empty">
    <div class="row">
      <label>Name<input name="name" required autocomplete="name"></label>
      <label>Mobile<input name="phone" type="tel" required autocomplete="tel" inputmode="tel"></label>
    </div>
    <div class="row">
      <label>Email (optional)<input name="email" type="email" autocomplete="email"></label>
      <label>Suburb<select name="suburb" required><option value="">Select…</option>{suburbs}<option>Other</option></select></label>
    </div>
    <label>What's the problem?<select name="pest"><option>Not sure — please identify</option><option>Termites / timber pest</option><option>General pest (cockroaches, spiders, silverfish)</option><option>Ants</option><option>Rodents</option><option>Mosquitoes</option><option>Wasps or bees</option><option>Fleas or bed bugs</option><option>Pre-purchase inspection</option><option>Commercial / strata</option></select></label>
    <label>Anything else we should know?<textarea name="message" rows="3"></textarea></label>
    <label class="consent"><input type="checkbox" name="marketing" value="yes"> Send me seasonal pest reminders (a few emails a year, unsubscribe any time).</label>
    <button class="btn btn-primary" type="submit">Request my quote {icon("arrow","icon")}</button>
    <div class="form-msg" role="status" aria-live="polite"></div>
    <p class="notice">By sending this form you agree to our <a href="/privacy">privacy policy</a>. We only use your details to respond to this enquiry.</p>
  </form>
</div></section>"""

# ---------------------------------------------------------------- chrome
NAV = [("Services", "/services"), ("Termites", "/termite-inspection-perth"), ("Investment", "/pest-control-prices-perth"),
       ("Areas", "/service-areas"), ("About", "/about"), ("Blog", "/blog")]

def header():
    links = "".join(f'<a href="{h}">{esc(t)}</a>' for t, h in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/"><img src="/assets/img/logo-white.png" alt="DJ Pest" width="120" height="43" style="filter:none"><span class="brand-sub">Perth's northern<br>suburbs</span></a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">{icon("menu")}</button>
  <nav class="nav" id="nav">{links}{btn_call(cls="btn btn-primary")}</nav>
</div></header>"""

def footer():
    areas = ", ".join(SITE["service_area"][:16]) + " and surrounding suburbs"
    return f"""<footer class="site-footer"><div class="wrap">
  <div class="cols">
    <div>
      <a class="brand" href="/"><img src="/assets/img/logo-white.png" alt="DJ Pest" width="96" height="34" style="filter:none"></a>
      <p style="margin-top:1rem;max-width:36ch">Second-generation pest management for {SITE['base_region']}. Licensed, documented, quoted in writing before we start.</p>
      <p><a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a><br><a href="mailto:{SITE['email']}">{SITE['email']}</a><br>{SITE['hours']}</p>
    </div>
    <div><div class="fh">Services</div><ul>
      <li><a href="/termite-inspection-perth">Termite inspections</a></li>
      <li><a href="/termite-treatment-perth">Termite treatment</a></li>
      <li><a href="/general-pest-control-perth">General pest treatment</a></li>
      <li><a href="/ant-control-perth">Ant management</a></li>
      <li><a href="/cockroach-control-perth">Cockroach management</a></li>
      <li><a href="/spider-control-perth">Spider management</a></li>
      <li><a href="/mosquito-control-perth">Mosquito management</a></li>
      <li><a href="/flea-treatment-perth">Vacate flea treatment</a></li>
      <li><a href="/rodent-control-perth">Rodent management</a></li>
      <li><a href="/wasp-removal-perth">Wasp removal</a></li>
      <li><a href="/bee-removal-perth">Bee removal</a></li>
      <li><a href="/commercial-pest-control-perth">Commercial pest management</a></li>
    </ul></div>
    <div><div class="fh">Company</div><ul>
      <li><a href="/about">About</a></li>
      <li><a href="/pest-control-prices-perth">Investment guide</a></li>
      <li><a href="/whats-my-pest">What's my pest?</a></li>
      <li><a href="/property-managers">Property managers</a></li>
      <li><a href="/service-areas">Service areas</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul></div>
    <div><div class="fh">Legal</div><ul>
      <li><a href="/terms">Terms &amp; conditions</a></li>
      <li><a href="/warranty">Re-treatment promise</a></li>
      <li><a href="/privacy">Privacy policy</a></li>
    </ul></div>
  </div>
  <div class="legal">
    {esc(SITE['legal_name'])} · ABN {SITE['abn']} · ACN {SITE['acn']}<br>
    WA Department of Health pest management business registration pending ({SITE['pmb']} assigned) · {esc(SITE['licence_label'])}<br>
    Based in {SITE['base_suburb']} WA {SITE['base_postcode']}. Servicing {esc(areas)}.<br>
    All pesticides are APVMA-registered and applied to label. Re-entry periods are advised before every treatment. © {TODAY[:4]} DJ Pest.
  </div>
</div></footer>
<div class="callbar">{btn_call("Call now")}<a class="btn btn-ghost" href="{SITE['phone_sms']}">{icon("message")}Text us</a></div>"""

SCRIPT = ("""<script>
(function(){
  var t=document.querySelector('.nav-toggle'),n=document.getElementById('nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});}
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});document.querySelectorAll('.reveal').forEach(function(el){io.observe(el)});}
  var f=document.getElementById('leadForm');
  if(f){f.addEventListener('submit',async function(ev){ev.preventDefault();var m=f.querySelector('.form-msg'),b=f.querySelector('button[type=submit]');
    var d={};new FormData(f).forEach(function(v,k){d[k]=v});
    if(!d.name||!d.phone||!d.suburb){m.textContent='Please add your name, mobile and suburb.';return;}
    b.disabled=true;m.textContent='Sending…';
    try{
      var fs=fetch('https://formsubmit.co/ajax/d50bd5ca094e7fb250eb75f3921a0b42',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify({_subject:'New website lead: '+d.name+' ('+d.suburb+') — '+(d.pest||'pest not specified'),_template:'table',_captcha:'false',Name:d.name,Mobile:d.phone,Email:d.email||'',Suburb:d.suburb,Pest:d.pest||'',Message:d.message||'','Marketing consent':d.marketing||'no',Page:location.href})}).then(function(r){return r.ok}).catch(function(){return false});
      var api=fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)}).then(function(r){return r.json()}).then(function(j){return !!j.ok}).catch(function(){return false});
      var ok=await Promise.all([fs,api]);
      if(ok[0]||ok[1]){m.textContent='Thanks '+d.name.split(' ')[0]+' — we\\'ll call you back shortly.';f.reset();}else{m.textContent='Something went wrong. Please call __PHONE__.';}
    }catch(e){m.textContent='Could not send. Please call __PHONE__.';}
    b.disabled=false;});}
  document.querySelectorAll('.report-tabs button').forEach(function(bt){bt.addEventListener('click',function(){
    var p=bt.closest('.report');p.querySelectorAll('.report-tabs button').forEach(function(x){x.setAttribute('aria-selected','false')});bt.setAttribute('aria-selected','true');
    p.querySelectorAll('.report-doc [data-pane]').forEach(function(x){x.hidden=x.dataset.pane!==bt.dataset.tab});});});
})();
</script>""").replace("__PHONE__", SITE["phone_display"])

def site_graph():
    return [{
        "@type": ["LocalBusiness", "PestControl"], "@id": DOMAIN + "/#business",
        "name": SITE["name"], "legalName": SITE["legal_name"], "url": DOMAIN, "telephone": SITE["phone_tel"], "email": SITE["email"],
        "image": DOMAIN + "/assets/img/og-default.jpg", "logo": DOMAIN + "/assets/img/logo-black.png",
        "address": {"@type": "PostalAddress", "addressLocality": SITE["base_suburb"], "addressRegion": "WA", "postalCode": SITE["base_postcode"], "addressCountry": "AU"},
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["geo"]["lat"], "longitude": SITE["geo"]["lng"]},
        "areaServed": [{"@type": "City", "name": s} for s in SITE["service_area"]],
        "openingHours": "Mo-Sa 07:00-18:00", "priceRange": "$$",
        "foundingDate": "2026", "slogan": "Perth family pest management since 2011",
        "identifier": [{"@type": "PropertyValue", "propertyID": "ABN", "value": SITE["abn"].replace(" ", "")},
                        {"@type": "PropertyValue", "propertyID": "WA Pest Management Business Registration (pending)", "value": SITE["pmb"] + " (assigned, certificate pending)"}],
        "hasCredential": {"@type": "EducationalOccupationalCredential", "name": SITE["licence_label"], "recognizedBy": {"@type": "GovernmentOrganization", "name": "WA Department of Health"}},
    }]

def crumbs_html(crumbs):
    if not crumbs: return ""
    parts = ['<a href="/">Home</a>']
    for t, h in crumbs:
        parts.append(f'<a href="{h}">{esc(t)}</a>' if h else esc(t))
    return '<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb">' + "<span>/</span>".join(parts) + "</nav></div>"

def crumbs_schema(crumbs, path):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    for i, (t, h) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": t, "item": DOMAIN + (h or path)})
    return {"@type": "BreadcrumbList", "itemListElement": items}


import re as _re
_WEBP_DONE = set()
def _webp_for(src):
    """Ensure a .webp sibling exists for /assets/img/x.(jpg|png); return its URL or None."""
    if not src.startswith("/assets/img/"): return None
    p = ROOT / src.lstrip("/")
    if not p.exists() or p.suffix.lower() not in (".jpg", ".jpeg", ".png"): return None
    w = p.with_suffix(".webp")
    if str(w) not in _WEBP_DONE and (not w.exists() or w.stat().st_mtime < p.stat().st_mtime):
        try:
            from PIL import Image
            im = Image.open(p); im = im.convert("RGBA") if p.suffix.lower() == ".png" else im.convert("RGB")
            if im.width > 1600:  # nothing on the site renders wider than this
                im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
            im.save(w, "WEBP", quality=80, method=6)
            if w.stat().st_size >= p.stat().st_size:  # WebP not a win: drop it, serve the original
                w.unlink(); _WEBP_DONE.add(str(w)); return None
        except Exception as e:
            print("webp skip", p.name, e); return None
    _WEBP_DONE.add(str(w))
    return "/" + str(w.relative_to(ROOT))

def _picturize(html_text):
    """Wrap <img src=/assets/img/*.jpg|png> in <picture> with a WebP <source>."""
    def rep(m):
        tag = m.group(0); src = m.group(1)
        if "data-nopicture" in tag: return tag
        w = _webp_for(src)
        if not w: return tag
        return f'<picture style="display:contents"><source type="image/webp" srcset="{w}">{tag}</picture>'
    return _re.sub(r'<img\b[^>]*\bsrc="(/assets/img/[^"]+\.(?:jpe?g|png))"[^>]*>', rep, html_text)


import os as _os
def _gated_paths():
    if _os.environ.get("DJPEST_GATE", "1") == "0": return []
    return list(SITE.get("unpublished", []))
def _strip_gated(html_text):
    for g in _gated_paths():
        html_text = re.sub(r'<a class="card" href="%s">.*?</a>' % re.escape(g), '', html_text, flags=re.S)
        html_text = re.sub(r'<li><a href="%s">[^<]*</a></li>\s*' % re.escape(g), '', html_text)
        html_text = re.sub(r'<tr>(?:(?!</tr>).)*href="%s"(?:(?!</tr>).)*</tr>' % re.escape(g), '', html_text, flags=re.S)
        html_text = re.sub(r'<a href="%s"><strong>.*?</a>' % re.escape(g), '', html_text, flags=re.S)
        html_text = re.sub(r' · <a href="%s">[^<]*</a>' % re.escape(g), '', html_text)   # 'Related:' separators
        html_text = re.sub(r'<a href="%s">([^<]*)</a>' % re.escape(g), r'\1', html_text)  # inline prose links -> plain text
    return html_text

def render(page):
    path = page["path"]
    canonical = DOMAIN + ("" if path == "/" else path)
    schema = {"@context": "https://schema.org", "@graph": site_graph() + list(page.get("schema", []))}
    if page.get("crumbs"): schema["@graph"].append(crumbs_schema(page["crumbs"], path))
    og = DOMAIN + page.get("og_image", "/assets/img/og-default.jpg")
    robots = '<meta name="robots" content="noindex,nofollow">' if page.get("noindex") else ""
    ver = SITE.get("verification", {})
    vtags = "".join(f'<meta name="{esc(k)}" content="{esc(v)}">' for k, v in ver.items() if v)
    return _strip_gated(_picturize(f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<script>document.documentElement.className+=' js';</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page['title'])}</title>
<meta name="description" content="{esc(page['desc'])}">
<meta name="theme-color" content="#0a0a0a">
<link rel="canonical" href="{canonical}">
{robots}{vtags}
<meta property="og:type" content="website"><meta property="og:site_name" content="DJ Pest"><meta property="og:title" content="{esc(page['title'])}"><meta property="og:description" content="{esc(page['desc'])}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{og}"><meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.ico" sizes="32x32"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/inter-tight.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/fraunces-roman.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<link rel="stylesheet" href="/assets/css/site.css?v={CSS_VER}">
<script type="application/ld+json">{json.dumps(schema, separators=(',', ':'), ensure_ascii=False)}</script>
</head>
<body>
{SPRITE}
{header()}
{crumbs_html(page.get('crumbs'))}
<main id="main">
{page['body']}
</main>
{footer()}
{SCRIPT}
</body>
</html>
"""))

# ---------------------------------------------------------------- compliance
FORBIDDEN = [r"\bguarantee[ds]?\b", r"100\s?%", r"\bpest[- ]proof\b", r"\btermite[- ]proof\b", r"\brodent[- ]proof\b", r"\bnon[- ]toxic\b",
             r"\bpermanent(ly)?\b", r"\blifetime\b", r"\bcheapest\b", r"\bbest in perth\b", r"\bwe beat any quote\b", r"\binstant(ly)?\b",
             r"\bsince 19\d\d\b", r"\b25\+? years\b", r"\b30 years\b", r"1,000\+", r"\$20M", r"\bWDJ\b", r"\bsafe for (kids|children|pets)\b"]
def compliance_scan(path, html_text):
    text = re.sub(r"<script.*?</script>", "", html_text, flags=re.S)
    text = re.sub("<[^>]+>", " ", text)
    hits = []
    for pat in FORBIDDEN:
        for m in re.finditer(pat, text, flags=re.I):
            ctx = text[max(0, m.start() - 40): m.end() + 40].replace("\n", " ")
            # allow "re-treatment promise" language that explicitly defines terms: skip 'guarantee' if followed by 'cannot be excluded' (ACL text)
            if pat.startswith(r"\bguarantee") and re.search(r"consumer guarantee|cannot be excluded|Australian Consumer Law", ctx, re.I):
                continue
            hits.append((path, pat, ctx.strip()))
    return hits

# ---------------------------------------------------------------- build
def load_pages():
    ctx = {k: v for k, v in globals().items() if not k.startswith("_")}
    pages = []
    pdir = ROOT / "build" / "pages"
    for f in sorted(pdir.glob("*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        pages.extend(mod.pages(ctx))
    return pages

def out_path(path):
    if path == "/": return ROOT / "index.html"
    return ROOT / (path.strip("/") + ".html")

def main():
    check_only = "--check" in sys.argv
    pages = load_pages()
    seen = set(); hits = []; urls = []
    for g in _gated_paths():  # remove stale output of gated pages so they cannot ship
        gp = out_path(g)
        if gp.exists(): gp.unlink()
    pages = [p for p in pages if p["path"] not in _gated_paths()]
    for p in pages:
        assert p["path"] not in seen, f"duplicate path {p['path']}"; seen.add(p["path"])
        html_text = render(p)
        hits += compliance_scan(p["path"], html_text)
        if not check_only:
            op = out_path(p["path"]); op.parent.mkdir(parents=True, exist_ok=True); op.write_text(html_text)
        if not p.get("noindex"): urls.append(p["path"])
    if not check_only:
        sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
            f"  <url><loc>{DOMAIN}{'' if u == '/' else u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
        (ROOT / "sitemap.xml").write_text(sm)
        (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /samples/\nDisallow: /api/\nSitemap: {DOMAIN}/sitemap.xml\n")
        idx = {p["path"]: p for p in pages if not p.get("noindex")}
        def _sec(title, paths):
            rows = [f"- [{idx[u]['title'].split('|')[0].strip()}]({DOMAIN}{'' if u == '/' else u}): {idx[u]['desc']}" for u in paths if u in idx]
            return f"\n## {title}\n" + "\n".join(rows) + "\n" if rows else ""
        svc = [u for u in urls if u.endswith("-perth") and u not in ("/pest-control-prices-perth",)]
        sub = [u for u in urls if u.count("/") == 1 and u not in svc and u not in ("/", "/services", "/service-areas", "/pest-control-prices-perth", "/whats-my-pest", "/about", "/contact", "/terms", "/warranty", "/privacy", "/blog", "/property-managers") and not u.startswith("/blog/")]
        blog = [u for u in urls if u.startswith("/blog/")]
        llms = (f"# {SITE['name']}\n\n> {SITE['name']} is a family-run pest management business based in {SITE['base_suburb']}, Western Australia, "
                f"servicing {SITE['base_region']}. In Perth pest management since {SITE.get('family_since','2011')}. Run by a Chartered Accountant: "
                f"itemised written quotes, a treatment record for every job, and a written re-treatment promise. "
                f"Technicians are licensed under the WA Health (Pesticides) Regulations 2011. {SITE.get('reg_line','')}\n\n"
                f"Phone {SITE['phone_display']} · {SITE['email']} · Hours {SITE['hours']}. Legal entity: {SITE['legal_name']}, ABN {SITE['abn']}.\n"
                f"Service area: {', '.join(SITE['service_area'])}.\n"
                + _sec("Services", ["/services"] + svc)
                + _sec("Investment and guidance", ["/pest-control-prices-perth", "/whats-my-pest", "/property-managers", "/warranty"])
                + _sec("Suburb pages", ["/service-areas"] + sub)
                + _sec("Guides", ["/blog"] + blog)
                + _sec("Company", ["/about", "/contact", "/terms", "/privacy"])
                + "\n## Facts an assistant may cite\n"
                "- Every product used is APVMA-registered and applied at its label rate; products and rates are named on the treatment record.\n"
                "- Re-treatment periods: " + "; ".join(f"{k} {v}" for k, v in SITE["retreat_periods"].items()) + ".\n"
                "- No call-out fee, no deposit; itemised quote in writing before work starts.\n"
                "- Termite inspections to AS 4349.3:2010; termite management to AS 3660.2:2017.\n")
        (ROOT / "llms.txt").write_text(llms)
    print(f"built {len(pages)} pages" if not check_only else f"checked {len(pages)} pages")
    if hits:
        print("\nCOMPLIANCE HITS (fix before deploy):")
        for path, pat, ctx in hits: print(f"  {path}  [{pat}]  …{ctx}…")
        sys.exit(2)
    print("compliance scan: clean")

if __name__ == "__main__":
    main()
