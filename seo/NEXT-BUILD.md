# NEXT BUILD — 2026-07-24

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage.
**~30% of 14-day plan. NO NEW PAGES BUILT IN 53 DAYS.**

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← **53RD CARRY-OVER — MINIMUM 20-MINUTE FIX**

**Keyword:** `pest control wanneroo` — local intent, low KD, easy win

**Current state:** 1443w · v1 schema (3 blocks) · missing FAQPage, GeoCoordinates, OpeningHoursSpecification
**Target:** ~3000w · joondalup v2 standard (4 schema blocks)

**Minimum viable fix (20 mins):**
1. Copy the `<script type="application/ld+json">` FAQPage block from `joondalup.html`
2. Paste before `</body>` in `wanneroo.html`
3. Rewrite the 3 Q&As Wanneroo-specific (rodents along Quinns Rocks Rd corridor, cockroaches at Wanneroo Town Centre, spiders from Lake Joondalup green belt)
4. Add `"geo": {"@type": "GeoCoordinates", "latitude": "-31.7527", "longitude": "115.8062"}` inside the LocalBusiness block
5. Add `openingHoursSpecification` array (copy from joondalup.html)
6. `git add wanneroo.html && git commit -m "feat: upgrade wanneroo schema to v2" && git push`

**Full upgrade (2–3 hrs) adds:**
- Local signals: Wanneroo Town Centre, Lake Joondalup green corridor, Wanneroo Raceway surrounds, urban-fringe bushland, ~12 min from Warwick
- Mini case study: roof rats along Quinns Rocks Rd

---

### 2. ⬆️ Upgrade `duncraig.html` ← same schema fix, same session

**Keyword:** `pest control duncraig` — strong residential intent, low KD

**Current state:** 1507w · v1 schema (3 blocks) · missing FAQPage, GeoCoordinates, OpeningHoursSpecification
**Target:** ~3000w · 4 schema blocks

- GeoCoordinates: `-31.8295, 115.7727`
- Local signals: Hepburn Heights bushland (ant + spider pressure), Duncraig Leisure Centre, leafy suburb roof-cavity rats, Carine Glades proximity, ~10 min from Warwick
- Keep voice distinct from wanneroo.html

---

### 3. 🆕 Build `sorrento.html` ← only after tasks 1 + 2 are pushed

**Keyword:** `pest control sorrento` — **260 searches/mo, KD8** — highest-volume unbuilt Tier-1 suburb

- Build to joondalup v2 standard from day one: ~3000w · 4 schema blocks
- GeoCoordinates: `-31.8295, 115.7601`
- Local signals: Sorrento Quay precinct, Marmion Marine Park, sandy-soil ant colonies, coastal cockroach + silverfish pressure, ~10 min from Warwick

---

## BLOCKERS / FLAGS

- **53 days on the same carry-over.** The schema patch on wanneroo.html is genuinely 20 minutes. Do the minimum viable fix first, full rewrite later.
- **Termite: HOLD.** `/termite-inspection-perth` (480/mo, KD32, $6.20 CPC — highest CPC on the board) stays staged/unpublished until WA DoH pest licence + termite endorsement are confirmed.
- **GBP is still the #1 unblocked lever.** If the Google Business Profile isn't verified with a review-generation engine running, an hour there outperforms any page built today.
- **Tier-1 queue after wanneroo + duncraig:** Sorrento (260/mo, KD8), Balcatta (110/mo, KD6), Hillarys (90/mo, KD7), Marangaroo (90/mo, KD0), Greenwood (70/mo, KD0), Stirling (70/mo, KD0), Warwick home-base (KD0)
- **Service gaps queued:** bee-removal (480/mo, KD27), wasp-removal (170/mo, KD8), mosquito-control (260/mo, KD11), bed-bug-treatment (110/mo, KD17), flea-treatment (140/mo, KD11), commercial-pest-control (390/mo, KD30)
- **MOFU cost pages:** `pest-control-cost-perth` (1300/mo, KD8) + `pest-control-prices` (720/mo, KD6) — transparent-pricing moat, no competitor has built this
