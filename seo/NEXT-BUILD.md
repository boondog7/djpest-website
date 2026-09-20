# NEXT BUILD — 2026-09-20

## Progress summary
**Done: 10 service pages published + 2 gated (price check needed) + 8 suburb pages + pricing hub + service-areas hub + 2 blog posts; ~88% of plan.**

Big news today: PMB 3000 registration issued 20/9/2026. Site copy updated to "registered". Country-heritage voice applied sitewide. The website is now your most credible asset — the remaining gaps are small.

### Pages live right now
**Service (10 published):** ant, cockroach, flea, general, mosquito, rodent, spider, termite-inspection, termite-treatment, wasp
**Service (2 gated — prices unconfirmed):** bee-removal-perth, commercial-pest-control-perth
**Suburb (8/10 Tier-1):** warwick, greenwood, duncraig, sorrento, hillarys, joondalup, wanneroo, balcatta
**Support:** service-areas, pest-control-prices-perth, whats-my-pest, blog + 2 posts, about, contact, property-managers

---

## Next tasks (priority order)

### 1. Confirm bee and commercial prices — then ungate in 5 minutes

Two fully-built pages are sitting gated in `build/site.json → "unpublished"`. They just need your price sign-off:

- **Bee hive treatment: $250–$400** — is this right?
- **Commercial per-visit: $140–$380; one-off kitchen clean-out: $350–$650** — is this right?

If yes: remove both slugs from `build/site.json → unpublished`, run `python3 build/build.py` and push. Two pages live in under 10 minutes. No writing required.

If the numbers are wrong: edit `build/pages/10_services.py` line 7 (the `PRICES` dict: `"bee": (250, 400)`, `"comm_visit": (140, 380)`, `"comm_cleanout": (350, 650)`), then ungate + build + push.

---

### 2. `/bed-bug-treatment-perth.html` — 110 searches/mo, KD17, CPC ~$4

**Last missing BOFU service page.** Every other service is covered; bed bugs are a growing Perth problem and the warranty page already promises "Bed bugs: 30-day, two-visit plan" — without a page to land on, that promise floats.

**Target keyword:** `bed bug treatment perth` (110/mo, KD17)
**Why next:** closes the last service gap; ties into existing warranty + pricing pages.
**How to build:** add a new function in `build/pages/10_services.py` following the same pattern as flea/mosquito. Heat + residual two-visit angle. Flag mattress-edge ID, no "one spray fixes it" claim. Add to `SITE.nav_services` and the sitemap. Run `python3 build/build.py` then push.

---

### 3. `/marangaroo.html` and `/stirling.html` — last two Tier-1 corridor suburbs

**Marangaroo:** 90/mo, KD0 — zero competition, Dane already drives here.
- Local signals: Marangaroo Golf Course boundary, Lake Goollelal fringe → mosquitoes and ants from golf-course irrigation runoff; older brick-veneer housing stock (60s–70s) → rodent harbourage.

**Stirling:** 70/mo, KD0 — zero competition.
- Local signals: Lake Gwelup reserve, Stirling Civic Gardens, mix of older 60s–70s brick + newer infill → both termites (timber framing, garden beds against brick) and rodents. Council stormwater drains as rodent runs.

**How to build:** add both to `build/pages/20_suburbs.py` following the balcatta/greenwood pattern. Each needs a suburb-specific intro paragraph, one local landmark reference, the pest-pressure angle, and a mini case-study sentence. Run generator + push.

---

## Ungate bee/commercial first — it's a 10-minute win

The two gated pages are complete. The only blocker is a price number. Do that before spending 2 hours on bed bugs or suburbs — it's the highest ROI action in the list.

## The bit no page can fix
GBP at Warwick 6024 + a review-ask after every job still beats all of the above. If GBP isn't verified and live yet, prioritise that today. PMB 3000 now gives you the "registered business" trust signal for citations too — add it to TrueLocal, Yellow Pages AU, Hipages, Oneflare, Yelp AU, StartLocal (consistent: DJ Pest Pty Ltd, Warwick WA 6024, PMB 3000).

## Blockers
None for bed bugs or suburbs. Bee/commercial are self-blocked on price confirmation (30 seconds of your time). Termite licence (endorsement) remains separate from PMB 3000 — termite pages are already live, so no change needed there.
