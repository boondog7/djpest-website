# DJ Pest blog STYLE.md (v1, 29 Sep 2026)

Replaces `~/jaystack/internal/templates/seo-voice/*.md` for every blog post. Those files predate DJ Pest and describe a different business (WDJ, Danny, 25+ years, 1,000+ clients, pub humour). Nothing in them may be used. Brand truth lives in `~/business/djpest/marketing/vibe/brand-bible.md`; this file applies it to long-form.

## 1. Who is writing
DJ Pest: a new, second-generation Perth pest business in the northern suburbs, run by a Chartered Accountant, WA DoH registered (PMB 3000). Provisional technician working under direct supervision. We claim no history, no client counts, no years in business, no jobs we have not done, no numbers we cannot source.

## 2. Voice (the six dials, long-form settings)
- Short declaratives. A plain sentence around one technical noun. The payoff sentence is the shortest one.
- Formal/casual 2.5: contractions fine, no slang, no "mate", no "g'day".
- Humour 2/5, dry: at most ONE dry observational line per post, about the pest or Perth conditions. Never about the reader, never a pun on a pest word, never in the first 50 words as a rule (the old "wink in the first 50 words" rule is retired).
- Technical/plain 3: name the biology, the standard or the active class, then say why in plain words. Never a rate, never a mix, never spray steps.
- Bold about our process ("You get the price in writing before we book, and the treatment record after"). Never comparative ("unlike other companies", "nobody else"). Humble about outcomes (pests can re-enter from next door).
- Calm. Real urgency only (season, active infestation). No caps, no "!!!", no countdowns.
- "We" for DJ Pest. No personal names on the website, not even "Dane". Never "Danny", never "WDJ".
- Australian English: colour, organise, mould, metres, "management" not "control" in body copy (the keyword may appear in the title, H1 and FAQ questions). "Investment" is fine, "cost" and "price" are fine when the query uses them.
- Words we use: itemised written price, treatment record, re-treatment promise, re-entry period, applied to label, APVMA-registered, look before we spray, harbourage, entry point, colony, foragers, non-repellent, bait, roof void, sub-floor, northern suburbs.
- Punctuation: NO em dashes or en dashes anywhere (use commas, full stops or brackets). Numbers with a unit use "to" not a dash ("13 to 16 mm"). Oxford comma optional. No exclamation marks.

## 3. Words that fail the gate (never)
guarantee(d) · 100% · pest-proof/termite-proof · non-toxic · chemical-free · safe for kids/pets/babies · permanent/lifetime/gone for good · cheapest/best in Perth/#1 · instant · exterminate/eradicate/annihilate · "solution(s)" · since 19xx / years of experience / 1,000+ clients · WDJ · Danny · a licence number · client names or street addresses · competitor names · any mL/L, g/L or "per litre" rate · "we've had", "our customers", "one of our clients", "last week we" (no invented experience) · AI-slop openers ("In today's fast-paced world", "this comprehensive guide", "everything you need to know", "look no further") · American spellings (color, favorite, neighbor, cilantro, faucet).

## 4. What a post is (the template)
Every H2 is a real question a Perth homeowner types, answered in its first sentence. 1,100 to 2,400 words. 5 to 9 H2s. Reading grade 9 or under.
1. **Lede** (one paragraph, 50 to 90 words): the direct answer to the query with Perth context. No throat-clearing.
2. **What it is / how to tell** (ID features: size, colour, where seen, what it is confused with).
3. **Signs, by Perth house type** where it fits: slab-on-ground, brick veneer, limestone footings, raised timber floor with sub-floor, roof void.
4. **Why it happens here / Perth timing**: season, weather, suburbs by construction era, when the pest peaks.
5. **What you can do yourself (non-chemical)**: hygiene, exclusion, harbourage removal, moisture, monitoring. Product questions get "the label is the law" and a PubCRIS link. No rates, no mixing, no application steps.
6. **What not to do**: including "Already sprayed? Get it checked" and the supermarket-bomb line.
7. **When to call a professional**: link the hub service page with a descriptive anchor (the page's own title words, not "click here"). Say what a treatment involves in outline and that it is applied to label by a licensed technician (use the fixed licensing line if licensing is mentioned).
8. **What it costs**: ONLY the ranges in the brief's `prices` (from site.json/PRICES). Say "typical range for a standard three-bedroom home in Perth's northern suburbs, itemised in writing after we have seen it". Never a figure that is not in the brief.
9. **Frequently asked** (`<h2>Frequently asked</h2>`): 6 to 8 `<h3>` questions, each answered in 2 to 4 sentences. Use the fold-in keywords from the brief as questions where they fit.
10. **Sources**: a short `<h2>Sources</h2>` list of the primary sources actually cited (from the brief only). Link with `rel="noopener"`.

Information gain: every post carries at least one thing the top results do not, from the brief: a WA primary-source data point, a Perth construction detail, a first-hand experience note (verbatim from Dane, if the brief has one), or a paperwork explainer (written price, treatment record, re-entry note).

Internal links: at least 3 distinct, relative (`href="/..."`): the hub service page, at least one sibling `/blog/` post on the same pest (from the brief's `siblings`), and the investment guide `/pest-control-prices-perth` or `/what-my-pest`-style helper where it fits. Only link URLs listed in the brief's `links_available`.

Images: place ONLY the images the brief supplies, with the alt text and captions given. The hero goes in the JSON header (`img`, `alt`); the second image goes in a `<figure>` after the first H2, with `width`, `height`, `loading="lazy"` and the credit line in the `<figcaption class="notice">`.

## 5. Fixed strings (copy exactly when the topic needs them)
- Registration: "WA Department of Health registered pest management business PMB 3000".
- Licensing: "carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence".
- Re-treatment periods must carry "terms at djpest.com.au/warranty" whenever a period is mentioned.
- CTA (closing line before the FAQ or at the end): "Text your suburb and what you're seeing to 0468 170 107 for a written price."
- Phone: 0468 170 107 (exactly). Email: ops@djpest.com.au. Base: Warwick WA 6024.

## 6. Experience notes
If the brief has `experience.text`, quote or paraphrase it truthfully, marked as our own observation ("On a recent Warwick job we found..."). It must fit a provisional technician working under supervision. If the brief has none, do not invent a job, a sighting, a number or a testimonial. Use the WA data point instead.

## 7. File format (write exactly this, nothing else)
Line 1: one-line JSON header `{"slug","title","desc","img","alt","date","read","service","service_label"}`.
Line 2: `---`
Then the lede paragraph as plain text (one paragraph).
Then `---`
Then the article HTML (`<h2>`, `<h3>`, `<p>`, `<ul>`, `<ol>`, `<table>`, `<figure>`, `<blockquote>`). No `<h1>`, no `<html>`, no scripts, no inline styles, no markdown.
`title` 45 to 65 characters with the primary keyword near the front and "Perth" where natural. `desc` 120 to 155 characters. `read` like "7 minutes".

## 8. Sidecar (sidecar.json, alongside post.html)
```
{"slug": "...",
 "claims": [{"sentence": "...", "type": "pesticide|health|regulation|price|stat", "source_id": "S1"}],
 "sources_used": ["S1", "S3"],
 "images": ["/assets/img/..."],
 "hub": "/service-page", "siblings": ["/blog/..."],
 "experience": {"used": true|false, "ref": "..."},
 "derivatives": {"gbp": "<= 1,500 chars, no phone number, one link", "fb_ig": "2 to 5 short lines + the CTA line", "email": "one paragraph"}}
```
Every sentence in the post that states a health effect, a regulation, a pesticide fact, a price or a statistic goes in `claims` with the source id from the brief it rests on. A claim with no source does not go in the post.
