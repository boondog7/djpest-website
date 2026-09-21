# NEXT BUILD — 2026-09-21

## Progress summary
**Done: 10 service pages + 8 suburb pages + pricing hub + service-areas hub + 2 blog posts + 2 gated pages; ~88% of plan.**

No changes since yesterday. Bee, commercial, bed-bug, Marangaroo and Stirling are all still outstanding. Same tasks as yesterday — pick one and ship it.

### Pages live right now
**Service (10):** ant, cockroach, flea, general, mosquito, rodent, spider, termite-inspection, termite-treatment, wasp
**Service (2 gated — price sign-off needed):** bee-removal-perth, commercial-pest-control-perth
**Suburb (8/10 Tier-1):** warwick, greenwood, duncraig, sorrento, hillarys, joondalup, wanneroo, balcatta
**Support:** service-areas, pest-control-prices-perth, whats-my-pest, property-managers, blog + 2 posts, about, contact

---

## Next tasks (priority order)

### 1. Ungate bee + commercial — 10-minute win, no writing needed

Two complete pages are sitting unpublished. All that's blocking them is your price sign-off:

- **`bee-removal-perth.html`** — target: `bee removal perth` (480/mo, KD27). Staged price: **$250–$400**. Right?
- **`commercial-pest-control-perth.html`** — target: `commercial pest control perth` (390/mo, KD30). Staged prices: **per-visit $140–$380; one-off kitchen clean-out $350–$650**. Right?

If yes: remove both slugs from `build/site.json → unpublished`, run `python3 build/build.py`, push. Done in under 10 minutes.
If the numbers are wrong: edit `build/pages/10_services.py` (the `PRICES` dict), then ungate + build + push.

---

### 2. `/bed-bug-treatment-perth.html` — last missing BOFU service page

**Keyword:** `bed bug treatment perth` — 110/mo, KD17, CPC ~$4.
**Why now:** every other service is covered. The warranty page already promises a "30-day, two-visit bed-bug plan" — that promise currently floats with no page to land on.
**How to build:** add a new function to `build/pages/10_services.py` following the flea/mosquito pattern. Angles: heat + residual two-visit protocol, mattress-edge ID tips, "no one-spray fix" honesty. Add to `SITE.nav_services` + sitemap. Run `python3 build/build.py` then push.

---

### 3. `/marangaroo.html` + `/stirling.html` — last two Tier-1 corridor suburbs

Both are KD0 with real monthly search volume. Zero competition. Dane already drives there.

**`marangaroo.html`** — 90/mo, KD0.
Local signals: Marangaroo Golf Course boundary + Lake Goollelal fringe → mosquitoes and ants from irrigation runoff; older 60s–70s brick-veneer stock → rodent harbourage in wall cavities and sub-floor.

**`stirling.html`** — 70/mo, KD0.
Local signals: Lake Gwelup reserve, Stirling Civic Gardens; mix of 60s–70s brick + newer infill → termite risk from garden beds against original timber framing; Council stormwater drains as rodent runs.

**How to build:** add both to `build/pages/20_suburbs.py` following the balcatta/greenwood pattern. Each needs a suburb-specific intro, one landmark reference, pest-pressure angle, mini case-study sentence. Run generator + push.

---

## Tier-2 suburbs (after the above are done)
Alkimos (70/KD5), Clarkson (50/KD6), Yanchep (50/KD4), Butler (50/KD0), Woodvale (30/KD0), Mindarie (40/KD0) — all still unbuilt, all in the corridor.

## Blockers
- Bee + commercial: self-blocked on your price confirmation (30 seconds).
- Bed-bug + suburbs: no blocker, ready to build.
- GBP at Warwick 6024 + review-ask after every job still outranks all of the above for phone calls. If not verified yet, do that first.
- Termite pages are live. PMB 3000 registered. No change needed there.
