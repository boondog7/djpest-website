# NEXT BUILD — 2026-09-18

## Progress summary
**Done: 9 service pages + 2 termite + 8 suburb pages + pricing hub + service-areas; ~75% of plan.**
Huge session today — full site rebuild on the new generator, all core suburb cluster built, termite pages LIVE (licence 13914 confirmed in schema ✅), mosquito + flea + property-managers added.

### Pages built so far
**Service (9):** ant, cockroach, flea, general, mosquito, rodent, spider, termite-inspection, termite-treatment
**Suburb (8):** warwick, greenwood, duncraig, sorrento, hillarys, joondalup, wanneroo, balcatta
**Support:** service-areas, pest-control-prices-perth, whats-my-pest, blog + 2 posts, about, contact, property-managers

---

## Today's tasks (priority order)

### 1. `/bee-removal-perth.html` — 480 searches/mo, KD27
**Why now:** Highest-volume missing service page. Battle plan calls it "fragmented field, easy" (Day 5–10 BOFU). No competitor owns this with a quality page.
**Target keyword:** `bee removal perth` (480/mo, KD27, CPC est. ~$4)
**How:** Add to `build/pages/10_services.py` → `python3 build/build.py` → `./deploy.sh --prod`
**Angle:** Cover live bee removal + relocating to local beekeeper (responsible framing). 900–1200 words, PestControl schema + FAQPage. Mention seasonal spring swarms (Perth Aug–Nov peak).

### 2. `/wasp-removal-perth.html` — 170 searches/mo, KD8
**Why now:** Lowest KD of all remaining service pages (KD8 = almost zero competition). Quick win, pairs naturally with bee page. Build both in same session.
**Target keyword:** `wasp removal perth` (170/mo, KD8)
**How:** Add alongside bee entry in `build/pages/10_services.py`
**Angle:** European wasp vs paper wasp (Perth has both), nest removal safety, why DIY spraying is risky. 700–900 words.

### 3. `/commercial-pest-control-perth.html` — 390 searches/mo, KD30
**Why now:** `/property-managers.html` exists but targets property managers specifically, NOT the broader `commercial pest control perth` search term. Recurring-revenue clients (restaurants, strata, warehouses). Dane-the-CA angle = transparent contracts, no hidden fees. Battle plan BOFU Day 5–10.
**Target keyword:** `commercial pest control perth` (390/mo, KD30)
**How:** Add to `build/pages/10_services.py` as a separate page from property-managers
**Angle:** Food-safe methods (HACCP awareness), strata body corporates, ILM programs, monthly service contracts. 900–1100 words.

---

## Up next after these three
- `/bed-bug-treatment-perth` (110/mo, KD17) — completes BOFU service gaps
- Suburb pages: Marangaroo (90/KD0), Stirling (70/KD0), Kingsley, Hamersley, Carine, Karrinyup, Woodvale, Padbury — 8 more in schema areaServed but no dedicated pages
- MOFU blog posts: "termite treatment cost perth" (720/mo, KD8), "exterminator cost perth" (1000/mo, KD11)

## Blockers
None. Termite licence confirmed (PMB 3000 + Licence 13914 in schema). Build pipeline working.
`build/` is gitignored — rebuild locally with `python3 build/build.py` then commit generated HTML + `./deploy.sh --prod`.
