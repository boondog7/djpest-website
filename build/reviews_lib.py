"""Reviews for djpest.com.au: data, stats and HTML blocks.

Rules baked in (ACL / ACCC online reviews guidance, Google terms):
- The rating and count shown are ALWAYS computed from every review we hold (or Google's own totals),
  never from the ones we choose to display. Negative reviews go on the wall like any other.
- Review text is never edited. Truncated text is never published.
- Reviewers are shown as first name + surname initial.
- Every block links to the full list on Google.
"""
import json, pathlib, html, datetime, re, os

DATA = pathlib.Path(os.environ.get("REVIEWS_JSON") or pathlib.Path(__file__).with_name("reviews.json"))
MIN_BADGE = 3          # hero star badge appears from this many reviews
MIN_BLOCK = 1          # review blocks appear from this many publishable reviews

SERVICE_BY_PATH = {
    "/termite-inspection-perth": "termites", "/termite-treatment-perth": "termites",
    "/general-pest-control-perth": "general", "/ant-control-perth": "ants", "/cockroach-control-perth": "cockroaches",
    "/spider-control-perth": "spiders", "/rodent-control-perth": "rodents", "/mosquito-control-perth": "mosquitoes",
    "/flea-treatment-perth": "fleas", "/wasp-removal-perth": "wasps", "/bee-removal-perth": "bees",
    "/commercial-pest-control-perth": "commercial", "/bed-bug-treatment-perth": "bed-bugs",
}
SERVICE_LABEL = {"termites": "Termites", "general": "General pest", "ants": "Ants", "cockroaches": "Cockroaches", "spiders": "Spiders",
                 "rodents": "Rodents", "mosquitoes": "Mosquitoes", "fleas": "Fleas", "wasps": "Wasps", "bees": "Bees",
                 "commercial": "Commercial", "bed-bugs": "Bed bugs"}

esc = lambda s: html.escape(str(s), quote=True)

def load():
    d = json.loads(DATA.read_text())
    d.setdefault("reviews", []); d.setdefault("profile", {})
    return d

def counted(d):   return [r for r in d["reviews"] if r.get("status") != "removed"]
def shown(d):     return sorted([r for r in d["reviews"] if r.get("status") == "publish" and r.get("text_complete")],
                                key=lambda r: r["date"], reverse=True)

def stats(d):
    t = d["profile"].get("google_totals")
    if t and t.get("count"):
        return round(float(t["rating"]), 1), int(t["count"])
    c = counted(d)
    if not c: return None, 0
    return round(sum(r["rating"] for r in c) / len(c), 1), len(c)

def display_name(full):
    parts = [p for p in re.split(r"\s+", (full or "").strip()) if p]
    if not parts: return "Google reviewer"
    return parts[0] if len(parts) == 1 else f"{parts[0]} {parts[-1][0]}."

def stars(n, cls="stars"):
    n = int(round(n))
    return f'<span class="{cls}" role="img" aria-label="{n} out of 5 stars">' + "".join(
        f'<span class="{"on" if i < n else "off"}" aria-hidden="true">★</span>' for i in range(5)) + "</span>"

def _date(s):
    try: return datetime.date.fromisoformat(s).strftime("%-d %b %Y")
    except Exception: return s

G_MARK = ('<svg class="g-mark" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.4h6.5a5.6 5.6 0 0 1-2.4 3.6v3h3.9c2.3-2.1 3.5-5.2 3.5-8.7z"/>'
          '<path fill="#34A853" d="M12 24c3.2 0 6-1.1 8-2.9l-3.9-3c-1.1.7-2.5 1.2-4.1 1.2-3.1 0-5.8-2.1-6.7-5H1.3v3.1A12 12 0 0 0 12 24z"/>'
          '<path fill="#FBBC05" d="M5.3 14.3a7.2 7.2 0 0 1 0-4.6V6.6h-4a12 12 0 0 0 0 10.8z"/>'
          '<path fill="#EA4335" d="M12 4.8c1.8 0 3.3.6 4.6 1.8l3.4-3.4A12 12 0 0 0 1.3 6.6l4 3.1c.9-2.8 3.6-4.9 6.7-4.9z"/></svg>')

def review_card(r, big=False):
    svc = " · ".join(SERVICE_LABEL.get(s, s) for s in r.get("services", []))
    meta = " · ".join(x for x in [r.get("suburb", ""), svc] if x)
    reply = (f'<div class="rv-reply"><span class="mono">Reply from DJ Pest</span><p>{esc(r["reply"])}</p></div>') if r.get("reply") else ""
    return (f'<figure class="rv{" rv-big" if big else ""}">'
            f'<div class="rv-top">{stars(r["rating"])}<span class="rv-src">{G_MARK}Google</span></div>'
            f'<blockquote><p>{esc(r["text"])}</p></blockquote>'
            f'<figcaption><strong>{esc(display_name(r.get("author")))}</strong>'
            f'{f"<span>{esc(meta)}</span>" if meta else ""}<time datetime="{esc(r["date"])}">{_date(r["date"])}</time></figcaption>'
            f'{reply}</figure>')

def badge(d, compact=False):
    avg, n = stats(d)
    if n < MIN_BADGE: return ""
    url = esc(d["profile"].get("public_url", "/reviews"))
    return (f'<a class="rv-badge{" rv-badge-sm" if compact else ""}" href="/reviews">{G_MARK}'
            f'<span class="rv-badge-score">{avg:.1f}</span>{stars(avg)}'
            f'<span class="rv-badge-n">from {n} Google review{"s" if n != 1 else ""}</span></a>')

def _pick(d, service=None, suburb=None, k=3):
    s = shown(d)
    def score(r):
        v = 0
        if service and service in r.get("services", []): v += 4
        if suburb and suburb.lower() == (r.get("suburb") or "").lower(): v += 5
        v += min(len(r["text"]), 400) / 400      # fuller stories first
        return v
    ranked = sorted(s, key=lambda r: (score(r), r["date"]), reverse=True)
    return ranked[:k]

def block(d, heading, service=None, suburb=None, k=3, eyebrow="What customers say"):
    picks = _pick(d, service, suburb, k)
    if len(picks) < MIN_BLOCK: return ""
    avg, n = stats(d)
    url = esc(d["profile"].get("public_url", ""))
    summary = (f'<p class="rv-summary">{stars(avg)} <strong>{avg:.1f}</strong> average from <strong>{n}</strong> Google review{"s" if n != 1 else ""}. '
               f'Showing {len(picks)}. <a href="/reviews">Read every review</a>'
               + (f' or <a href="{url}" rel="noopener" target="_blank">see them on Google</a>.' if url else ".") + "</p>")
    return (f'<section class="rv-section ledger"><div class="wrap">'
            f'<div class="eyebrow mono">{esc(eyebrow)}</div><div class="section-head"><h2>{esc(heading)}</h2>{summary}</div>'
            f'<div class="rv-grid">{"".join(review_card(r) for r in picks)}</div></div></section>')

def quote_strip(d):
    s = shown(d)
    if not s: return ""
    r = max(s, key=lambda r: (r["rating"], r["date"]))
    t = r["text"] if len(r["text"]) <= 220 else r["text"][:r["text"].rfind(" ", 0, 210)] + "…"
    return (f'<figure class="rv-mini">{stars(r["rating"])}<blockquote><p>{esc(t)}</p></blockquote>'
            f'<figcaption>{esc(display_name(r.get("author")))}{", " + esc(r["suburb"]) if r.get("suburb") else ""} · Google review · '
            f'<a href="/reviews">all reviews</a></figcaption></figure>')

def schema(d):
    """Review markup is self-serving for rich results since 2019, so only add aggregateRating as a plain fact
    when it exactly matches the full count. It will not produce stars in Google; it keeps AI/LLM readers accurate."""
    avg, n = stats(d)
    if n < MIN_BADGE: return {}
    return {"aggregateRating": {"@type": "AggregateRating", "ratingValue": f"{avg:.1f}", "reviewCount": n, "bestRating": 5, "worstRating": 1}}

def inject(path, body, suburb=None):
    """Called by build.render for every page. Adds the right review blocks by page type."""
    d = load()
    out = body
    if path == "/":
        b = badge(d)
        if b: out = out.replace('<h1>', b + '<h1>', 1)
        blk = block(d, "Northern-suburbs homes, in their own words.", k=6)
    elif path in SERVICE_BY_PATH:
        svc = SERVICE_BY_PATH[path]
        blk = block(d, f"What customers said after {SERVICE_LABEL[svc].lower()} jobs." if any(svc in r.get("services", []) for r in shown(d))
                    else "What our customers say.", service=svc)
    elif suburb:
        sub = suburb
        blk = block(d, f"Reviews from {sub} and nearby." if any((r.get("suburb") or "").lower() == sub.lower() for r in shown(d))
                    else "What our customers say.", suburb=sub)
    else:
        blk = ""
    if blk:
        i = out.find('<section class="quote"')
        out = out[:i] + blk + out[i:] if i >= 0 else out + blk
    qs = quote_strip(d)
    if qs and '<form class="lead-form"' in out:
        out = out.replace('<p class="notice">', qs + '<p class="notice">', 1)
    return out

import hashlib
def text_hash(t): return hashlib.sha256((t or "").encode()).hexdigest()[:16]

def validate():
    """Hard gate run by build.py. Returns a list of problems; any problem blocks the build."""
    d = load(); p = []
    ids = set()
    for r in d["reviews"]:
        rid = r.get("id", "?")
        if rid in ids: p.append(f"duplicate review id {rid}")
        ids.add(rid)
        if r.get("status") == "publish":
            if not r.get("text_complete"): p.append(f"{rid}: truncated text marked publish")
            if r.get("text_sha") and r["text_sha"] != text_hash(r["text"]): p.append(f"{rid}: review text was edited after capture (ACCC: never edit reviews)")
            if not (1 <= int(r.get("rating", 0)) <= 5): p.append(f"{rid}: bad rating")
    t = d["profile"].get("google_totals")
    if t and t.get("count") and t["count"] < len(counted(d)):
        p.append("google_totals.count is lower than reviews held; refresh totals")
    return p
