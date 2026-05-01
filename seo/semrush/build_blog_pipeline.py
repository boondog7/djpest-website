#!/usr/bin/env python3
"""
Build the 5-year DJ Pest blog content pipeline from SEMrush data.

Inputs:
  - 03_question_keywords.csv (round 1 — 214 questions)
  - r2_questions.csv (round 2 — 721 questions)
  - 06_targets_tofu.csv / 06_targets_mofu.csv

Outputs:
  - _drafts/00_blog_pipeline.csv — master pipeline with ALL eligible blog topics
  - _drafts/<NN>_<slug>.md — research bundles for the top 24 priority topics

Each research bundle contains everything needed for a writer (or Claude) to
produce the final HTML in one pass: keyword data, SERP intel, image suggestion,
schema scaffold, voice notes, internal link recommendations.
"""
import csv, os, re, sys, json, urllib.request, urllib.parse
from pathlib import Path
from collections import OrderedDict

OUT = Path("/Users/danejohns/jaystack/djpest/seo/semrush")
DRAFTS = Path("/Users/danejohns/jaystack/djpest/blog/_drafts")
DRAFTS.mkdir(parents=True, exist_ok=True)

PEXELS_KEY = os.environ.get("PEXELS_API_KEY", "")


def slugify(s):
    s = re.sub(r"[^a-z0-9\s-]", "", s.lower())
    s = re.sub(r"\s+", "-", s.strip())
    return s[:80]


def load_csv(name):
    try:
        with open(OUT / name) as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def to_int(v):
    try:
        return int(float(v or 0))
    except Exception:
        return 0


def to_float(v):
    try:
        return float(v or 0)
    except Exception:
        return 0.0


def fetch_pexels_image(query):
    if not PEXELS_KEY:
        return None
    try:
        url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query)}&per_page=1&orientation=landscape"
        req = urllib.request.Request(url, headers={"Authorization": PEXELS_KEY})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.load(r)
        if d.get("photos"):
            return d["photos"][0]["src"]["large2x"]
    except Exception:
        pass
    return None


# Load all candidate keywords across rounds
all_questions = []

for src, label in [("03_question_keywords.csv", "r1"), ("r2_questions.csv", "r2")]:
    rows = load_csv(src)
    for r in rows:
        kw = (r.get("Keyword") or "").lower().strip()
        if not kw:
            continue
        all_questions.append({
            "keyword": kw,
            "volume": to_int(r.get("Search Volume")),
            "kd": to_int(r.get("Keyword Difficulty Index")),
            "cpc": to_float(r.get("CPC")),
            "competition": to_float(r.get("Competition")),
            "intent": r.get("Intent", ""),
            "root": r.get("_root", ""),
            "source": label,
        })


# Dedupe by keyword (keep highest-volume version)
by_kw = {}
for q in all_questions:
    kw = q["keyword"]
    if kw not in by_kw or q["volume"] > by_kw[kw]["volume"]:
        by_kw[kw] = q

deduped = list(by_kw.values())
print(f"Loaded {len(all_questions)} question rows, {len(deduped)} unique keywords")


# Filter eligible blog topics
def is_eligible(q):
    if q["volume"] < 50:
        return False
    if q["kd"] > 35:
        return False
    if q["kd"] == 0:
        return False  # KD=0 usually means SEMrush has no data
    kw = q["keyword"]
    # Drop anything that's clearly a brand/business name
    if any(w in kw for w in ["service", "company", "near me", "perth", "sydney", "melbourne", "brisbane", "adelaide"]):
        # Allow some — these can still be informational
        if not any(p in kw for p in ["how", "what", "why", "when", "are", "do", "does", "is", "can"]):
            return False
    # Must look like a question or informational phrase
    if not any(p in kw for p in ["how ", "what ", "why ", "when ", "are ", "do ", "does ", "is ", "can ", "best ", "vs ", "cost", "diy", "kill", "get rid"]):
        # Could still be a how-to even without explicit question word
        return q["volume"] >= 200  # higher bar
    return True


eligible = [q for q in deduped if is_eligible(q)]
# Score: volume × (1 + cpc) / (kd + 10)
for q in eligible:
    q["score"] = (q["volume"] * (1 + q["cpc"])) / (q["kd"] + 10)
eligible.sort(key=lambda x: x["score"], reverse=True)
print(f"Eligible blog topics: {len(eligible)}")


# Save the full pipeline as CSV
with open(DRAFTS / "00_blog_pipeline.csv", "w", newline="") as f:
    fields = ["rank", "keyword", "volume", "kd", "cpc", "score", "root", "source"]
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for i, q in enumerate(eligible, 1):
        q["rank"] = i
        w.writerow({k: q.get(k, "") for k in fields})
print(f"  → 00_blog_pipeline.csv ({len(eligible)} rows)")


# Generate research bundles for the TOP 24 (already covered: cockroach + ant — skip)
ALREADY_PUBLISHED = {
    "how to get rid of cockroaches",
    "how to get rid of ants",
}

PEST_TO_QUERY = {
    "termite": "termite damage timber",
    "ant": "ants kitchen counter",
    "cockroach": "cockroach kitchen",
    "rat": "rat in house",
    "mouse": "mouse in house",
    "spider": "spider web outdoor",
    "redback": "redback spider",
    "white tail": "white tail spider",
    "huntsman": "huntsman spider",
    "mosquito": "mosquito bite",
    "flea": "flea on pet",
    "bed bug": "bed bug close up",
    "silverfish": "silverfish",
    "wasp": "wasp nest",
    "bee": "bee colony",
    "millipede": "millipede",
    "earwig": "earwig",
}


def voice_notes(kw):
    """Suggest which voice files / framings to lean on."""
    notes = []
    if "cost" in kw:
        notes.append("Lean into pricing transparency. Cite specific Perth $ ranges from stats.md.")
    if "are " in kw or "is " in kw or "dangerous" in kw:
        notes.append("Health/safety angle. Be honest, cite WA DoH or AEPMA. Don't catastrophise.")
    if "diy" in kw or "kill" in kw or "get rid" in kw:
        notes.append("DIY-vs-pro framing. Tell readers when DIY is fine, when not. Don't oversell.")
    if "vs" in kw or "best" in kw:
        notes.append("Comparison structure. Use a table.")
    if "signs of" in kw or "look like" in kw:
        notes.append("Visual ID guide — pull 4-6 species photos. Use a quick-facts identification box.")
    if not notes:
        notes.append("Standard TOFU treatment — voice + humor + species ID + how-to.")
    return notes


def link_suggestions(kw):
    """Suggest internal links."""
    links = ["/joondalup"]
    if "termite" in kw:
        links.append("/joondalup")  # termite-heavy suburb page
    if "ant" in kw:
        links.append("/ant-control-perth")
        links.append("/blog/how-to-get-rid-of-ants")
    if "cockroach" in kw or "roach" in kw:
        links.append("/cockroach-control-perth")
        links.append("/blog/how-to-get-rid-of-cockroaches")
    if "rat" in kw or "rodent" in kw or "mouse" in kw or "mice" in kw:
        links.append("/rodent-control-perth")
    if "spider" in kw or "redback" in kw or "huntsman" in kw or "white tail" in kw:
        links.append("/spider-control-perth")
    return list(OrderedDict.fromkeys(links))


def image_query(kw):
    for p, q in PEST_TO_QUERY.items():
        if p in kw:
            return q
    return "pest control technician australia"


# Pick top 24 (skipping already-published)
draft_count = 0
for q in eligible:
    if draft_count >= 24:
        break
    if q["keyword"] in ALREADY_PUBLISHED:
        continue
    draft_count += 1
    rank = draft_count
    slug = slugify(q["keyword"])
    img_url = fetch_pexels_image(image_query(q["keyword"]))

    md = []
    md.append(f"---")
    md.append(f"primary_keyword: {q['keyword']}")
    md.append(f"slug: {slug}")
    md.append(f"volume: {q['volume']}")
    md.append(f"keyword_difficulty: {q['kd']}")
    md.append(f"cpc_aud: {q['cpc']}")
    md.append(f"priority_score: {round(q['score'], 1)}")
    md.append(f"target_word_count: {1200 if q['volume'] < 1000 else 1500}")
    md.append(f"target_h2_count: {6 if q['volume'] < 1000 else 8}")
    md.append(f"target_image_count: {3 if q['volume'] < 1000 else 4}")
    md.append(f"hero_image_url: {img_url or '(fetch with Pexels API at write time)'}")
    md.append(f"image_query: {image_query(q['keyword'])}")
    md.append(f"status: draft-research")
    md.append(f"published_url: ~")
    md.append(f"---\n")

    md.append(f"# Research bundle: \"{q['keyword']}\"\n")
    md.append(f"**Priority rank:** #{rank} of {len(eligible)} eligible blog topics")
    md.append(f"**Volume:** {q['volume']} searches/month (Australian SEMrush)")
    md.append(f"**KD:** {q['kd']} (rank-target: ≤35)")
    md.append(f"**Source:** {q['source']} round, root keyword `{q['root'] or '(none)'}`\n")

    md.append(f"## Suggested article structure\n")
    md.append("- **H1**: matches primary keyword, hook-y opening")
    md.append("- **Lede paragraph**: 50-80 words, must contain dad joke / parenthetical wink in first 50 words (humor.md rule)")
    md.append(f"- **{6 if q['volume'] < 1000 else 8} H2 sections** covering:")
    md.append("  - The species or context (ID, biology, why this matters in Perth)")
    md.append("  - The science of treatment (chemistry / mechanism)")
    md.append("  - Step-by-step DIY protocol (HowTo schema)")
    md.append("  - What doesn't work (myth-busting list)")
    md.append("  - DIY-vs-pro decision tree")
    md.append("  - Pricing reference table")
    md.append("  - 6-8 question FAQ (FAQPage schema)")
    md.append("  - CTA to relevant service page\n")

    md.append(f"## Voice notes\n")
    for n in voice_notes(q["keyword"]):
        md.append(f"- {n}")
    md.append("")

    md.append(f"## Internal link suggestions (3-5 links)\n")
    for l in link_suggestions(q["keyword"])[:5]:
        md.append(f"- `{l}`")
    md.append("")

    md.append(f"## External authority links (2-3)\n")
    md.append("- WA Department of Health PMT scheme: `https://www.health.wa.gov.au/Articles/A_E/Becoming-a-licensed-pest-management-technician`")
    md.append("- AEPMA: `https://www.aepma.com.au/`")
    md.append("- WA DoH TG013 termite guideline (where relevant): `https://www.wa.gov.au/system/files/2025-11/tg013-termite-management.pdf`")
    md.append("- AS standards (where relevant): `https://www.standards.org.au/`\n")

    md.append(f"## Schema scaffold\n")
    md.append(f"- `Article` with author=DJ Pest, publisher=DJ Pest, dateModified=auto")
    md.append(f"- `BreadcrumbList` (Home → Blog → this article)")
    if "how" in q["keyword"] or "get rid" in q["keyword"] or "diy" in q["keyword"]:
        md.append(f"- `HowTo` with 5-7 steps + supplies array (high-value rich-result eligibility)")
    md.append(f"- `FAQPage` with 6-8 Q&A from suggested FAQ block\n")

    md.append(f"## Suggested file path\n")
    md.append(f"- HTML: `~/jaystack/djpest/blog/{slug}.html`")
    md.append(f"- Canonical URL: `https://djpest.com.au/blog/{slug}`")
    md.append(f"- Sitemap entry priority: 0.7-0.8\n")

    md.append(f"## Pre-write checklist\n")
    md.append(f"- [ ] Voice files read (humor.md, voice.md, opinions.md, stats.md, stories.md)")
    md.append(f"- [ ] SERP-stealing: fetch top 3 Google results for `{q['keyword']}`, average word count")
    md.append(f"- [ ] Hero image fetched + descriptive alt text")
    md.append(f"- [ ] Schema validated against schema.org")
    md.append(f"- [ ] Australian English check (colour, organise, optimise, etc.)")
    md.append(f"- [ ] No fake testimonials, no \"comprehensive guide\" / \"in today's fast-paced world\" cliches")
    md.append(f"- [ ] FAQ block 6-8 questions, all answered honestly\n")

    out = DRAFTS / f"{rank:02d}_{slug}.md"
    out.write_text("\n".join(md))
    print(f"  → {out.name} (vol={q['volume']}, KD={q['kd']})")

print(f"\n{draft_count} research bundles saved to {DRAFTS}")
