#!/opt/homebrew/bin/python3
"""Masthead Mack's brief pack (Blog Desk stage 2 to 5): everything the writer needs, so the writer needs no web tools.

  brief.py <slug> [--no-photos] [--json]

Builds blog/_drafts/wip/<slug>/brief.json from:
  - the QUEUE.md row (primary keyword, fold-in keywords, hub service page, bundles)
  - the research bundle frontmatter (volume, KD, targets) with the stale voice rules stripped
  - the hub page (title + H2s from the built HTML) and every sibling post on the same pest
  - links_available: every live root page and post, so the writer can only link to what exists
  - prices: the pest's ranges from build/pages/10_services.py PRICES (the only figures the writer may use)
  - fixed strings + claims policy from build/site.json
  - primary sources: an allowlisted candidate list per pest, each curl-checked (200) with a text excerpt
  - Dane's experience note (blog/_drafts/experience/<slug>.md) if he gave one
  - photos: Shutter Shaz (photos.py) sources 2 stock photos BEFORE writing (or reuses ones already registered for the slug)
  - STYLE.md + the brand bible's voice section
Exit 1 with {"error": ...} if fewer than 3 primary sources are live or the photo desk finds nothing.
0 tokens except the photo desk's one Haiku vision call.
"""
from __future__ import annotations
import json, re, subprocess, sys, datetime as dt, html as _html
from pathlib import Path

SITE = Path.home() / "jaystack/djpest"; DRAFTS = SITE / "blog/_drafts"; QUEUE = DRAFTS / "QUEUE.md"
POSTS = SITE / "build/posts"; WIP = DRAFTS / "wip"; STYLE = SITE / "blog/STYLE.md"
BIBLE = Path.home() / "business/djpest/marketing/vibe/brand-bible.md"
SITEJSON = SITE / "build/site.json"; SERVICES_PY = SITE / "build/pages/10_services.py"
STOP = {"how", "to", "get", "rid", "of", "a", "the", "do", "what", "is", "are", "can", "i", "in", "my", "and", "or", "you", "does", "will", "bite", "perth"}

PEST_KEYS = {  # slug/keyword token -> (pest label, PRICES keys, photo queries, species note)
    "silverfish": ("silverfish", ["general"], ["silverfish insect", "silverfish close up"], "Lepisma saccharina / Ctenolepisma; wingless, silver, carrot-shaped, three tail filaments"),
    "termite": ("termites", ["inspection", "chem", "bait"], ["termites wood", "termite damage timber"], "Coptotermes acinaciformis is the main Perth pest species; workers are pale and soft-bodied"),
    "white-ant": ("termites", ["inspection", "chem", "bait"], ["termites wood"], "termites (called white ants), not ants"),
    "cockroach": ("cockroaches", ["cockroach", "general"], ["german cockroach", "cockroach kitchen"], "German cockroach 13 to 16 mm tan with two dark stripes; Australian/American cockroaches larger, reddish-brown"),
    "ant": ("ants", ["ant", "general"], ["ants trail", "ants close up"], "coastal brown ant, black house ant, Argentine ant are the common Perth species"),
    "spider": ("spiders", ["spider", "general"], ["spider web house", "huntsman spider"], "redback, white-tail, huntsman, black house spider in Perth"),
    "huntsman": ("spiders", ["spider", "general"], ["huntsman spider", "huntsman spider wall"], "Sparassidae; large, flat, fast, not dangerous to people"),
    "white-tail": ("spiders", ["spider", "general"], ["white tailed spider"], "Lampona cylindrata / Lampona murina; dark cigar body, pale tip"),
    "rat": ("rodents", ["rodent", "rodent_follow"], ["rat roof", "brown rat"], "black rat (roof rat) and Norway rat; roof rat is the common Perth roof-void species"),
    "rodent": ("rodents", ["rodent", "rodent_follow"], ["rat", "mouse house"], "black rat, Norway rat, house mouse"),
    "mice": ("rodents", ["rodent", "rodent_follow"], ["house mouse", "mouse"], "house mouse (Mus musculus)"),
    "mouse": ("rodents", ["rodent", "rodent_follow"], ["house mouse", "mouse"], "house mouse (Mus musculus)"),
    "flea": ("fleas", ["flea"], ["flea close up", "dog scratching fleas"], "cat flea (Ctenocephalides felis) on dogs and cats; pupae survive in carpet"),
    "wasp": ("wasps", ["wasp"], ["paper wasp nest", "wasp nest"], "paper wasp is the common Perth nest; European wasp is a DPIRD-reportable pest"),
    "bee": ("bees", ["bee"], ["honey bee swarm", "bees"], "European honey bee swarms; refer to a beekeeper where possible"),
    "mosquito": ("mosquitoes", ["mosquito"], ["mosquito close up", "mosquito water"], "Aedes and Culex; breed in standing water"),
    "bed-bug": ("bed bugs", ["bedbug", "bedbug_room", "bedbug_home"], ["bed bug mattress", "bed bug"], "Cimex lectularius; 4 to 5 mm, flat, reddish-brown"),
    "cost": ("pest control pricing", ["general", "ant", "cockroach", "rodent", "spider", "inspection"], ["pest control technician spraying", "pest control van"], ""),
    "insurance": ("termites", ["inspection", "chem", "bait"], ["termite damage timber", "termite damage house"], "insurance and termite damage"),
}

# Primary-source candidates per pest. brief.py checks each one live (HTTP 200) and keeps an excerpt; dead ones are dropped.
GENERAL_SOURCES = [
    ("WA Department of Health: pest management technician licensing", "https://www.health.wa.gov.au/Articles/A_E/Becoming-a-licensed-pest-management-technician"),
    ("HealthyWA: choosing a pest management business", "https://www.healthywa.wa.gov.au/Articles/N_R/Pest-control"),
    ("HealthyWA: pesticides and pest control in the home", "https://www.healthywa.wa.gov.au/Articles/N_R/Pesticides"),
    ("APVMA PubCRIS (registered products and labels)", "https://portal.apvma.gov.au/pubcris"),
    ("Health (Pesticides) Regulations 2011 (WA)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_s44226.html"),
    ("AEPMA (Australian Environmental Pest Managers Association)", "https://www.aepma.com.au/"),
]
PEST_SOURCES = {
    "silverfish": [("Australian Museum: silverfish", "https://australian.museum/learn/animals/insects/silverfish/"),
                   ("HealthyWA: silverfish", "https://www.healthywa.wa.gov.au/Articles/S_T/Silverfish"),
                   ("CSIRO: silverfish (Zygentoma)", "https://www.csiro.au/en/research/animals/insects/silverfish")],
    "termites": [("WA DoH TG013 termite management", "https://www.wa.gov.au/system/files/2025-11/tg013-termite-management.pdf"),
                 ("HealthyWA: termites", "https://www.healthywa.wa.gov.au/Articles/S_T/Termites"),
                 ("CSIRO: termites", "https://www.csiro.au/en/research/animals/insects/termites"),
                 ("Australian Museum: termites", "https://australian.museum/learn/animals/insects/termites/")],
    "cockroaches": [("HealthyWA: cockroaches", "https://www.healthywa.wa.gov.au/Articles/A_E/Cockroaches"),
                    ("Australian Museum: German cockroach", "https://australian.museum/learn/animals/insects/german-cockroach/"),
                    ("Australian Museum: cockroaches", "https://australian.museum/learn/animals/insects/cockroaches/")],
    "ants": [("HealthyWA: ants", "https://www.healthywa.wa.gov.au/Articles/A_E/Ants"),
             ("DPIRD: ants in the home and garden", "https://www.agric.wa.gov.au/pest-insects/ants-home-and-garden"),
             ("Australian Museum: ants", "https://australian.museum/learn/animals/insects/ants/")],
    "spiders": [("HealthyWA: spider bites", "https://www.healthywa.wa.gov.au/Articles/S_T/Spider-bites"),
                ("Australian Museum: white-tailed spider", "https://australian.museum/learn/animals/spiders/white-tailed-spider/"),
                ("Australian Museum: huntsman spiders", "https://australian.museum/learn/animals/spiders/huntsman-spiders/"),
                ("Australian Museum: redback spider", "https://australian.museum/learn/animals/spiders/redback-spider/"),
                ("HealthyWA: spiders", "https://www.healthywa.wa.gov.au/Articles/S_T/Spiders")],
    "rodents": [("HealthyWA: rodents", "https://www.healthywa.wa.gov.au/Articles/N_R/Rodents"),
                ("HealthyWA: rats and mice", "https://www.healthywa.wa.gov.au/Articles/N_R/Rats-and-mice"),
                ("Australian Museum: black rat", "https://australian.museum/learn/animals/mammals/black-rat/"),
                ("DPIRD: rats and mice", "https://www.agric.wa.gov.au/pest-mammals/rats-and-mice")],
    "fleas": [("HealthyWA: fleas", "https://www.healthywa.wa.gov.au/Articles/F_I/Fleas"),
              ("Australian Museum: fleas", "https://australian.museum/learn/animals/insects/fleas/"),
              ("WA DoH: end of tenancy pest treatments", "https://www.commerce.wa.gov.au/consumer-protection/pest-control")],
    "wasps": [("DPIRD: European wasp", "https://www.agric.wa.gov.au/european-wasp"),
              ("HealthyWA: bee and wasp stings", "https://www.healthywa.wa.gov.au/Articles/A_E/Bee-and-wasp-stings"),
              ("Australian Museum: paper wasps", "https://australian.museum/learn/animals/insects/paper-wasps/")],
    "bees": [("HealthyWA: bee and wasp stings", "https://www.healthywa.wa.gov.au/Articles/A_E/Bee-and-wasp-stings"),
             ("DPIRD: bees", "https://www.agric.wa.gov.au/bees")],
    "mosquitoes": [("HealthyWA: mosquitoes", "https://www.healthywa.wa.gov.au/Articles/J_M/Mosquitoes"),
                   ("WA DoH: Fight the Bite", "https://www.health.wa.gov.au/Articles/F_I/Fight-the-bite"),
                   ("HealthyWA: Ross River virus", "https://www.healthywa.wa.gov.au/Articles/N_R/Ross-River-virus")],
    "bed bugs": [("HealthyWA: bed bugs", "https://www.healthywa.wa.gov.au/Articles/A_E/Bed-bugs"),
                 ("Australian Museum: bed bugs", "https://australian.museum/learn/animals/insects/bed-bugs/")],
    "pest control pricing": [],
}
ALLOW = ("gov.au", "australian.museum", "csiro.au", "aepma.com.au", "apvma.gov.au", "standards.org.au", "nih.gov", "edu.au")

def parse_queue(slug):
    for ln in QUEUE.read_text().splitlines():
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) >= 7 and c[0].isdigit() and c[1] == slug:
            return {"n": c[0], "slug": c[1], "primary": c[2], "fold": c[3], "bundles": c[4], "service": c[5], "status": c[6]}
    return None

def bundle_meta(bundles):
    out = []
    for n in re.findall(r"\d+", bundles or ""):
        for f in sorted(DRAFTS.glob(f"{int(n):02d}_*.md")):
            t = f.read_text(); m = re.match(r"---\n(.*?)\n---", t, re.S); fm = {}
            if m:
                for l in m.group(1).splitlines():
                    if ":" in l: k, v = l.split(":", 1); fm[k.strip()] = v.strip()
            ext = re.findall(r"`(https?://[^`]+)`", t)
            out.append({"file": f.name, "primary_keyword": fm.get("primary_keyword"), "volume": fm.get("volume"), "kd": fm.get("keyword_difficulty"),
                        "target_words": fm.get("target_word_count"), "external_links": ext})
    return out

def strip_html(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I); h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", _html.unescape(h)).strip()

def page_outline(path):
    t = path.read_text(errors="ignore")
    title = re.search(r"<title>(.*?)</title>", t, re.S); h2 = re.findall(r"<h2[^>]*>(.*?)</h2>", t, re.S)
    return {"title": strip_html(title.group(1)) if title else path.stem, "h2": [strip_html(x)[:90] for x in h2][:12]}

def pest_of(slug, primary):
    toks = (slug + " " + primary).lower().replace("_", "-")
    for k in ("white-tail", "white-ant", "bed-bug", "huntsman", "silverfish", "termite", "cockroach", "mosquito", "rodent", "mice", "mouse", "rat", "flea", "wasp", "bee", "spider", "ant", "insurance", "cost"):
        if k in toks or k.replace("-", " ") in toks: return k, PEST_KEYS[k]
    return None, ("pests", ["general"], [primary], "")

def prices():
    src = SERVICES_PY.read_text(); m = re.search(r"PRICES = \{(.*?)\n\}", src, re.S); d = {}
    for k, lo, hi in re.findall(r'"(\w+)":\s*\((\d+),\s*(\d+)\)', m.group(1) if m else ""): d[k] = [int(lo), int(hi)]
    return d

def check_source(name, url):
    r = subprocess.run(["curl", "-sL", "-A", "Mozilla/5.0 (DJPest brief.py)", "--max-time", "15", "-w", "\n%{http_code}", url], capture_output=True)
    body, _, code = (r.stdout or b"").decode("utf-8", "replace").rpartition("\n")
    if code.strip() != "200": return None
    text = strip_html(body) if not url.endswith(".pdf") else ""
    if url.endswith(".pdf"): text = f"(PDF, {len(body)//1024} KB)"
    if re.search(r"\b404\b|page (?:you(?:'re| are) looking for )?(?:no longer exists|not found|cannot be found|could not be found)|page has moved", text[:600], re.I): return None
    if not url.endswith(".pdf") and len(text) < 300: return None
    excerpt = text[:900]
    return {"name": name, "url": url, "http": 200, "excerpt": excerpt}

def sources_for(pest, bundle_links):
    cands = list(PEST_SOURCES.get(pest, [])) + [(f"bundle link {i+1}", u) for i, u in enumerate(dict.fromkeys(bundle_links))] + GENERAL_SOURCES
    seen, out = set(), []
    for name, url in cands:
        if url in seen or not any(a in url for a in ALLOW): continue
        seen.add(url); s = check_source(name, url)
        if s: s["id"] = f"S{len(out)+1}"; out.append(s)
        if len(out) >= 8: break
    return out

def photos_for(slug, queries, subject, skip):
    reg = DRAFTS / "images.csv"; have = []
    if reg.exists():
        import csv
        for r in csv.DictReader(open(reg)):
            if r.get("slug") == slug: have.append("/assets/img/" + Path(r["file"]).name)
    have = [h for h in have if (SITE / h.lstrip("/")).exists()]
    if len(have) >= 2: return {"files": have[:3], "alts": [], "credits": [], "note": "already registered for this slug"}
    if skip: return {"files": have, "alts": [], "credits": [], "note": "photos skipped"}
    r = subprocess.run([sys.executable, str(SITE / "build/blog/photos.py"), slug, *queries, "--n", "2", "--subject", subject], capture_output=True, text=True, timeout=600)
    try: return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception: return {"error": (r.stdout + r.stderr)[-300:]}

def build(slug, no_photos=False):
    row = parse_queue(slug)
    if not row: return {"error": f"{slug} is not in QUEUE.md"}
    key, (pest, price_keys, queries, species) = pest_of(slug, row["primary"])
    site = json.loads(SITEJSON.read_text()); pr = prices()
    hub = SITE / (row["service"].strip("/") + ".html")
    hub_outline = page_outline(hub) if hub.exists() else {"title": row["service"], "h2": [], "missing": True}
    my_toks = set(slug.split("-")) - STOP
    posts = {f.stem: f for f in list(POSTS.glob("*.html"))}
    for f in (SITE / "blog").glob("*.html"):
        posts.setdefault(f.stem, f)
    siblings = []
    for st, f in sorted(posts.items()):
        if st == slug or st == "README": continue
        their_key, (their_pest, *_r) = pest_of(st, "")
        if their_pest == pest or {t.rstrip("s") for t in st.split("-")} & {t.rstrip("s") for t in my_toks}:
            t = f.read_text(errors="ignore"); title = None
            try: title = json.loads(t.splitlines()[0]).get("title")
            except Exception:
                m = re.search(r"<title>(.*?)</title>", t, re.S); title = strip_html(m.group(1)) if m else st
            siblings.append({"url": f"/blog/{st}", "title": title})
    links = sorted({"/" + p.stem for p in SITE.glob("*.html") if p.stem not in ("404", "index")} | {"/blog/" + s for s in posts if s != "README" and s != slug} | {"/"})
    bundles = bundle_meta(row["bundles"]); bundle_links = [u for b in bundles for u in b["external_links"]]
    srcs = sources_for(pest, bundle_links)
    exp = DRAFTS / "experience" / f"{slug}.md"
    experience = {"text": exp.read_text().strip(), "ref": f"blog/_drafts/experience/{slug}.md"} if exp.exists() else {"text": "", "ref": ""}
    photos = photos_for(slug, queries, f"{pest}: {species or row['primary']}", no_photos)
    month = dt.date.today().month
    season = {12: "summer", 1: "summer", 2: "summer", 3: "autumn", 4: "autumn", 5: "autumn", 6: "winter", 7: "winter", 8: "winter"}.get(month, "spring")
    bible = BIBLE.read_text() if BIBLE.exists() else ""
    voice = bible.split("## 3.")[0][:7000]
    brief = {
        "slug": slug, "built": dt.datetime.now().isoformat(timespec="seconds"), "today": dt.date.today().isoformat(), "season": season,
        "row": row, "pest": pest, "species_note": species, "bundles": bundles,
        "hub": {"url": row["service"], **hub_outline}, "siblings": siblings, "links_available": links,
        "prices": {k: pr[k] for k in price_keys if k in pr}, "price_rule": "Typical ranges, GST inclusive, for a standard three-bedroom home in Perth's northern suburbs; every job is itemised in writing after we have seen it. Use ONLY these figures.",
        "fixed_strings": {"registration": "WA Department of Health registered pest management business PMB 3000", "licensing": site.get("licence_label"),
                          "reg_line": site.get("reg_line"), "cta": "Text your suburb and what you're seeing to 0468 170 107 for a written price.",
                          "phone": "0468 170 107", "email": site.get("email"), "hours": site.get("hours"), "base": "Warwick WA 6024",
                          "retreat_periods": site.get("retreat_periods"), "retreat_rule": "any period mentioned must carry 'terms at djpest.com.au/warranty'"},
        "claims_policy": site.get("claims_policy"), "service_area": site.get("service_area", [])[:20],
        "sources": srcs, "experience": experience, "photos": photos,
        "style": STYLE.read_text(), "brand_voice": voice,
        "format_example": {"header": {"slug": slug, "title": "<45 to 65 chars, keyword near the front>", "desc": "<120 to 155 chars>", "img": (photos.get("files") or ["/assets/img/..."])[0],
                                      "alt": "<factual alt under 125 chars>", "date": dt.date.today().isoformat(), "read": "7 minutes", "service": row["service"], "service_label": hub_outline["title"].split("|")[0].strip()[:40]}},
    }
    problems = []
    if len(srcs) < 3: problems.append(f"only {len(srcs)} live primary sources")
    if hub_outline.get("missing"): problems.append(f"hub page {row['service']} does not exist")
    if photos.get("error") or len(photos.get("files", [])) < 2: problems.append("photo desk: " + str(photos.get("error") or "fewer than 2 photos"))
    brief["problems"] = problems
    d = WIP / slug; d.mkdir(parents=True, exist_ok=True)
    (d / "brief.json").write_text(json.dumps(brief, indent=1, ensure_ascii=False))
    return brief

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if not a: print(__doc__); sys.exit(2)
    b = build(a[0], no_photos="--no-photos" in sys.argv)
    if "--json" in sys.argv: print(json.dumps(b, indent=1)[:4000])
    else:
        print(json.dumps({"slug": b.get("slug"), "sources": len(b.get("sources", [])), "siblings": [s["url"] for s in b.get("siblings", [])], "photos": b.get("photos"), "problems": b.get("problems", b.get("error"))}, indent=1))
    sys.exit(1 if b.get("error") or b.get("problems") else 0)
