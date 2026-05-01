# DJ Pest — SERP-Stealing Analysis

> Real top-3 ranking page analysis for our priority BOFU keywords.
> Run 2026-05-01. Data lives forever. Re-run if SERP shifts (≥6 months).

---

## `pest control joondalup` — KD 15, 390/mo, $4.17 CPC

### Top 3 ranking pages (October 2026)

| # | URL | Traffic | Word count | H2s | Images | Notes |
|---|---|---:|---:|---:|---:|---|
| 1 | joondaluppestcontrol.com.au | 312 | **249** | 2 | 9 | Exact-match domain dominance. Thin content. 53 external links (social/citations). |
| 2 | allpest.com.au/joondalup/ | 10 | **718** | 3 | 21 | Standard suburb landing page. Termites is primary H2. |
| 3 | rentokil.com/au/.../pest-control-joondalup | 7 | 9* | 0 | 0 | JS-rendered (server returns shell HTML). Effectively a placeholder ranking on Rentokil domain authority alone. |

*Average across top 3 (excluding JS-rendered Rentokil): **~480 words, 2-3 H2s, 15 images**.*

### Strategic implication

**The SERP is weak on content depth.** DJ Pest's `joondalup.html` at 1,241 words with 4 H2s + 5 H3s + 2 images already exceeds the top 3. We don't need more content — we need:

- ✅ Better structured data (FAQPage schema, openingHours)
- ✅ Better internal linking (currently 3 internal nearby-suburb links; the body mentions 17)
- ✅ Trust signals (license number, ABN, years operating in trade prominent)
- ❌ Possibly a bit more pricing depth (allpest does termite extensively)

### What #1 (joondaluppestcontrol.com.au) gets that we don't

- **Exact match domain (EMD)** — they own `joondaluppestcontrol.com.au`. We can't replicate this for every suburb. But we can take #2-#5 with better content + schema + GBP integration.
- **53 external citation links** — they're getting authority from social profiles, directory listings, partner mentions. We need a similar citation footprint.

### What #2 (allpest.com.au) gets that we don't

- **21 images** vs our 2. Their gallery includes pest photos, technician photos, equipment shots. Ours is termite-damage + house. Add 4-5 more.
- **More H3s on individual pest categories** — they cover termites in depth as a sub-section. We treat termite as the big topic, then 4 numbered H3s for our services. Theirs is more "pest catalog" style.

### Realistic ranking target
With our 1,241-word page + technical fixes + GBP listing + 5-10 quality citations, we should hit **#3-#5 within 4-6 months**. Displacing #1 EMD requires 12+ months of authority building.

---

## `pest control wanneroo` — KD ~14, 110/mo (low volume but easy)

### Top 3 ranking pages

| # | URL | Traffic |
|---|---|---:|
| 1 | bugbusters.com.au/wanneroo-pest-control/ | 7 |
| 2 | rentokil.com/au/.../pest-control-wanneroo | 4 |
| 3 | stewartspestcontrol.com.au/pest-control-wanneroo | 3 |

**Combined top 3 traffic: 14 visits/month.** Almost wide open. Any well-structured page can take #1-#2.

---

## `pest control warwick` — DOMINATED BY WARWICK QLD

### Top 5 ranking pages

| # | URL | Notes |
|---|---|---|
| 1 | flick.com.au/warwick-pest-control/ | **Warwick QLD** |
| 2 | facebook.com/paynespestmanagement/ | **Warwick QLD** |
| 3 | yellowpages.com.au/warwick-qld-4370/pest-control | **Warwick QLD** |
| 4 | jimspestwarwick.com.au | **Warwick QLD** |
| 5 | hentschelpestmanagement.com | **Warwick QLD** |

**Strategic implication:** the SERP for `pest control warwick` is 100% Warwick, Queensland (postcode 4370). **There is no one ranking for "pest control Warwick WA"** — pure whitespace. We must:

1. **Target the longer-tail variant**: `pest control warwick wa` or `pest control warwick perth`
2. **Heavy geo-disambiguation in our Warwick page** — every paragraph must mention Perth/WA/6024 to keep us out of the QLD SERP
3. **Internal link from Joondalup, Greenwood, Hamersley pages** to reinforce "Warwick WA" cluster

---

## `pest control hillarys` — wide open

Top 5 combined traffic: 11 visits/month. Top ranker is tomspestcontrolperth.com.au (5 visits). Very rankable.

---

## `pest control perth` (the dream keyword) — KD 50, very competitive

### Top 8 dominant players (avoid for now — too expensive to displace)

1. allpest.com.au — 188 traffic
2. termicopestmanagement.com.au — 127 traffic
3. rentokil.com/au/.../pest-control-perth — 101 traffic
4. a1pestcontrolperth.com.au/pricing/ — 69 traffic
5. perthpest.com.au — 69 traffic
6. tomspestcontrolperth.com.au — 63 traffic
7. envirapest.com.au — 55 traffic
8. flick.com.au/perth-pest-control/ — 37 traffic

**Strategic implication:** don't try to take this for at least 12 months. Stack rankings on every Perth suburb page first, then climb to "pest control perth" via accumulated topical authority. Ranking #6-#8 here is realistic in year 2.

---

## `termite treatment perth` — Reddit ranks #3, opportunity for cost guide

Top 5:

1. termicopestmanagement.com.au — 30 traffic
2. tomspestcontrolperth.com.au/termite-treatment-perth/ — 24 traffic
3. **reddit.com/r/perth/comments/.../termite_treatment_cost** — 24 traffic
4. rentokil.com/au/.../termite-treatment-perth — 19 traffic
5. allpest.com.au/pests/termite-pest-control-perth/ — 5 traffic

**Reddit at #3 is a huge signal.** The query has commercial intent but searchers also want honest pricing — Reddit threads provide that. **Opportunity:** write a brutally transparent pest-cost guide with real Perth pricing breakdowns. Write it as honest TOFU/MOFU content (not a sales page), and we can outrank the Reddit thread because:
- Reddit threads age (this one is from `1bn8qkh` which is ~3 years old)
- We can offer up-to-date 2026 pricing
- We can structure with proper schema (Reddit's HowTo schema is generic)

This is the highest-leverage MOFU blog target for us.

---

## Insights for ALL future suburb pages

Based on the SERP analysis, every DJ Pest suburb page needs:

1. **Word count: 800-1,500 minimum** (top SERP averages ~480 — so 800+ wins on depth)
2. **6-12 images minimum** (allpest at #2 has 21 images. Pexels has plenty.)
3. **Multiple JSON-LD schema types**: LocalBusiness + Service + FAQPage + BreadcrumbList (none of the top 3 are doing this comprehensively — easy edge)
4. **Real local content** (street names, council, real distances from Warwick) — the top rankers are generic
5. **Internal link to other suburb pages** in same LGA + back to homepage
6. **External authority links** (DoH WA, AS standards, AEPMA) — top 3 don't do this
7. **Pricing transparency in a table** — Reddit's success at #3 for "termite treatment perth" shows people want this
8. **Question-format FAQ block** with 6-8 questions and FAQPage schema attached

The top 3 rankers are getting traffic on domain authority + EMD, NOT content quality. That's our edge.
