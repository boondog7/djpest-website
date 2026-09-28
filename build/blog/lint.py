#!/opt/homebrew/bin/python3
"""Read-only self-check for the blog writer (and the first half of the publish gates).

  lint.py <post.html> [--brief <brief.json>]

Checks the same structural and language rules publish.py enforces, without touching git, build.py or any model:
header keys, slug/service match, lede + article parts, 6+ FAQ h3s, 3+ internal links (hub + a /blog/ sibling), links
that exist, word count, em dashes, application rates, first-hand claims, legacy claims, banned phrases, image placement,
and (with --brief) that every image and every link is one the brief allows and every price figure is in the brief.
Prints one problem per line and exits 1 if any; prints "lint: clean" and exits 0 otherwise.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

SITE = Path.home() / "jaystack/djpest"; POSTS = SITE / "build/posts"
BANNED = ["in today's fast-paced world", "this comprehensive guide", "everything you need to know", "look no further",
          "faucet", "cilantro", "neighbor", "favorite", " color ", "exterminat", "guarantee", "100%", "non-toxic", "pest-proof",
          "termite-proof", "chemical-free", "safe for kids", "safe for pets", "safe for children", "gone for good", "cheapest", "best in perth",
          "unlike other companies", "nobody else", "no one else"]
RATE = re.compile(r"\b\d+(?:\.\d+)?\s?(?:mL|ml|g|grams?)\s?(?:/|per)\s?(?:L|litre|liter|\d+\s?L|m2|m²|square metre)", re.I)

def link_exists(l):
    if l == "/": return True
    s = l.strip("/")
    return (SITE / (s + ".html")).exists() or (SITE / s / "index.html").exists() or (POSTS / (s.rsplit("/", 1)[-1] + ".html")).exists()

def check(path: Path, brief: dict | None = None) -> list[str]:
    errs = []
    if not path.exists(): return [f"{path} does not exist"]
    txt = path.read_text(); lines = txt.splitlines()
    try: hdr = json.loads(lines[0])
    except Exception: return ["line 1 is not a valid one-line JSON header"]
    for k in ("slug", "title", "desc", "img", "alt", "date", "read", "service", "service_label"):
        if not hdr.get(k): errs.append(f"header missing '{k}'")
    parts = txt.split("\n---\n", 2)
    if len(parts) < 3: errs.append("file must be: JSON header, ---, lede paragraph, ---, article HTML")
    body = parts[-1] if parts else txt; lede = parts[1] if len(parts) > 2 else ""
    plain = re.sub(r"<[^>]+>", " ", lede + " " + body)
    if brief:
        row = brief["row"]
        if hdr.get("slug") != row["slug"]: errs.append(f"header slug '{hdr.get('slug')}' should be '{row['slug']}'")
        if hdr.get("service") != row["service"]: errs.append(f"header service '{hdr.get('service')}' should be '{row['service']}'")
    t = hdr.get("title", "")
    if not 40 <= len(t) <= 70: errs.append(f"title is {len(t)} chars (aim 45 to 65)")
    d = hdr.get("desc", "")
    if not 110 <= len(d) <= 160: errs.append(f"desc is {len(d)} chars (aim 120 to 155)")
    if "<h1" in body.lower(): errs.append("no <h1> in the article (the template renders it)")
    if re.search(r"<(html|head|body|script|style)\b", body, re.I): errs.append("no html/head/body/script/style tags")
    h2s = re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S | re.I)
    if not 5 <= len(h2s) <= 10: errs.append(f"{len(h2s)} H2s (aim 5 to 9 plus the FAQ and Sources)")
    faq = re.split(r"<h2>[^<]*(?:Frequently asked|Quick answers|FAQ|Common questions)[^<]*</h2>", body, flags=re.I)
    nq = len(re.findall(r"<h3", faq[1].split("<h2")[0])) if len(faq) > 1 else 0
    if nq < 6: errs.append(f"FAQ has {nq} questions (need 6 to 8 <h3> under <h2>Frequently asked</h2>)")
    if nq > 8: errs.append(f"FAQ has {nq} questions (max 8)")
    imgs = [hdr.get("img", "")] + re.findall(r'<img[^>]+src="([^"]+)"', body)
    if len(set(i for i in imgs if i)) < 2: errs.append("needs 2 distinct images (header img + one <figure> in the article)")
    if "og-default" in hdr.get("img", ""): errs.append("hero image is the default site image")
    for i in set(i for i in imgs if i):
        if not (SITE / i.lstrip("/")).exists(): errs.append(f"image {i} does not exist")
        if brief and brief.get("photos", {}).get("files") and i not in brief["photos"]["files"]: errs.append(f"image {i} is not one the brief supplied ({brief['photos']['files']})")
    for m in re.finditer(r"<img(?![^>]*\bwidth=)[^>]*>", body): errs.append("an <img> is missing width/height attributes")
    links = set(re.findall(r'href="(/[^"#?]*)"', body))
    if brief:
        if brief["row"]["service"] not in links: errs.append(f"no link to the hub service page {brief['row']['service']}")
        sib = [s["url"] for s in brief.get("siblings", [])]
        if sib and not any(s in links for s in sib): errs.append("link at least one sibling post: " + ", ".join(sib[:3]))
        allowed = set(brief.get("links_available", []))
        for l in links:
            if allowed and l not in allowed: errs.append(f"link {l} is not in the brief's links_available")
    if not any(l.startswith("/blog/") for l in links): errs.append("link at least one related /blog/ post")
    for l in links:
        if not link_exists(l): errs.append(f"internal link to a page that doesn't exist: {l}")
    if len(links) < 3: errs.append(f"needs at least 3 distinct internal links (has {len(links)})")
    for m in re.findall(r'href="(https?://[^"]+)"', body):
        if brief and m not in {s["url"] for s in brief.get("sources", [])} and not any(m.startswith(s["url"].split("#")[0]) for s in brief.get("sources", [])):
            errs.append(f"external link not in the brief's sources: {m}")
    words = len(plain.split())
    if not 1100 <= words <= 2400: errs.append(f"{words} words (need 1,100 to 2,400)")
    if "—" in txt or "–" in txt: errs.append(f"{txt.count('—') + txt.count('–')} em/en dashes (use commas, full stops, brackets or 'to')")
    if "!" in plain: errs.append("no exclamation marks")
    for m in RATE.findall(plain): errs.append(f"application rate in copy: '{m}' (say 'at the label rate')")
    for m in re.findall(r"\b(we've had|we have had|our customers|one of our (?:clients|customers)|last (?:week|month) we|we recently|a customer (?:told|called|rang)|we see (?:this|it) (?:a lot|every|all the time))\b", plain, re.I):
        errs.append(f"unsourced first-hand claim '{m}'")
    for m in re.findall(r"\b(WDJ|Danny|Dane|\d+\+?\s*years?(?: of)? (?:experience|in business|in pest)|1,000\+?|thousands of (?:customers|clients|homes)|since 19\d\d|family[- ]owned for)\b", plain, re.I):
        errs.append(f"legacy/personal/unverifiable claim '{m}'")
    low = txt.lower()
    for b in BANNED:
        if b in low: errs.append(f"banned phrase: '{b.strip()}'")
    if re.search(r"\b(control)\b", " ".join(h2s), re.I) and not re.search(r"control", hdr.get("title", ""), re.I):
        pass
    if brief:
        allowed_prices = {str(v) for pr in brief.get("prices", {}).values() for v in pr}
        for m in re.findall(r"\$\s?([\d,]{2,6})", plain):
            if m.replace(",", "") not in allowed_prices: errs.append(f"price ${m} is not in the brief's prices {brief.get('prices')}")
        if "terms at djpest.com.au/warranty" not in plain and re.search(r"re-treat\w*\s+(?:period|promise)|\b(?:30 days|3 months|6 months)\b", plain, re.I):
            errs.append("a re-treatment period is mentioned without 'terms at djpest.com.au/warranty'")
    if re.search(r"\b0?4\d{2}\s?\d{3}\s?\d{3}\b", plain) and "0468 170 107" not in plain: errs.append("phone number is not 0468 170 107")
    if not re.search(r"<h2[^>]*>\s*Sources\s*</h2>", body, re.I): errs.append("missing <h2>Sources</h2> list")
    return errs

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(2)
    brief = None
    if "--brief" in a: brief = json.loads(Path(a[a.index("--brief") + 1]).read_text())
    errs = check(Path(a[0]), brief)
    for e in errs: print("- " + e)
    print("lint: clean" if not errs else f"lint: {len(errs)} problem(s)")
    sys.exit(1 if errs else 0)
