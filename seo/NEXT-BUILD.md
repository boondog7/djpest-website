# NEXT BUILD — 2026-06-28

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage.
**~30% of 14-day plan. NO CHANGE FOR 27 DAYS RUNNING.**

The tasks below are identical to yesterday and every day back to 2 June. One of them takes 20 minutes. Pick it today.

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← 27TH CARRY-OVER

**Keyword:** `pest control wanneroo` — local intent, low KD, easy win

**Current state:** 1443w · v1 schema · missing FAQPage, GeoCoordinates, OpeningHoursSpecification  
**Target:** ~3000w · joondalup v2 standard (full @type set incl. FAQPage + GeoCoords)

**20-minute minimum patch (do this NOW if time is short):**
1. Copy the `<script type="application/ld+json">` FAQPage block from `joondalup.html`
2. Paste before `</body>` in `wanneroo.html`
3. Rewrite the 3 Q&As to be Wanneroo-specific (rodents along Quinns Rocks Rd corridor, cockroaches at Wanneroo Town Centre, spiders from Lake Joondalup green belt)
4. Add `GeoCoordinates` + `OpeningHoursSpecification` inside the existing LocalBusiness block
5. `git add wanneroo.html && git commit -m "feat: upgrade wanneroo schema to v2" && git push`

**Full 2–3 hr upgrade:**
- Local signals: Wanneroo Town Centre, Lake Joondalup green corridor (rodent + spider pressure), Wanneroo Raceway surrounds, urban-fringe bushland
- Drive time: ~12 min from Warwick
- Mini case study: roof rats along Quinns Rocks Rd corridor
- Every paragraph genuinely Wanneroo — not a template swap

---

### 2. ⬆️ Upgrade `duncraig.html` ← same session as task 1

**Keyword:** `pest control duncraig` — strong residential intent, low KD

**Current state:** 1507w · v1 schema · same gaps as wanneroo  
**Target:** ~3000w · 31 @type

- Local signals: Hepburn Heights bushland reserve (ant + spider pressure), Duncraig Leisure Centre, leafy suburb roof-cavity rats, Carine Glades proximity
- Drive time: ~10 min from Warwick
- Must read distinctly from wanneroo.html — different pest profile, different voice

---

### 3. 🆕 Build `sorrento.html` ← only after tasks 1 + 2 are pushed

**Keyword:** `pest control sorrento` — **260 searches/mo, KD8** — highest-volume unbuilt Tier-1 suburb

- Build to joondalup v2 standard from day one: ~3000w · 31 @type
- Local signals: Sorrento Quay, Marmion Marine Park, sandy-soil ant colonies, coastal cockroach + silverfish pressure, ~10 min from Warwick

---

## BLOCKERS / FLAGS

- **Termite: HOLD.** `/termite-inspection-perth` (480/mo, KD32, $6.20 CPC — highest CPC on the board) stays staged/unpublished until WA DoH pest licence + termite endorsement are confirmed. The single most valuable page the licence unlocks — worth staging now and flipping live the day paperwork clears.
- **GBP is still the #1 unblocked lever.** If the Google Business Profile isn't verified with a review-generation engine running, an hour there outperforms any page built today. Map 3-pack is where phone calls come from.
- **Tier-1 queue after wanneroo + duncraig:** Balcatta (110/mo, KD6), Hillarys (90/mo, KD7), Marangaroo (90/mo, KD0), Greenwood (70/mo, KD0), Stirling (70/mo, KD0), Warwick home-base (KD0)
- **Service gaps queued:** bee-removal (480/mo, KD27), wasp-removal (170/mo, KD8), mosquito-control (260/mo, KD11), bed-bug-treatment (110/mo, KD17), flea-treatment (140/mo, KD11), commercial-pest-control (390/mo, KD30)
- **MOFU cost pages:** `pest-control-cost-perth` (1300/mo, KD8) + `pest-control-prices` (720/mo, KD6) — transparent-pricing moat, no competitor has built this
