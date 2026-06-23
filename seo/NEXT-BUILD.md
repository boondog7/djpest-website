# NEXT BUILD — 2026-06-23

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage.
**~30% of 14-day plan. NO CHANGE FOR 22 DAYS RUNNING.**

`wanneroo.html` and `duncraig.html` have been the stated next task since 1 June. Every day they stay at v1, the entire suburb cluster (sorrento 260/mo, hillarys 90/mo, balcatta 110/mo…) stays locked.

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← 22ND CARRY-OVER

**Keyword:** `pest control wanneroo` — local intent, low KD, easy win

**Current state:** 1443w · 3 JSON-LD blocks · missing FAQPage, GeoCoordinates, OpeningHoursSpecification  
**Target:** ~3000w · 4 JSON-LD blocks · 31 @type (joondalup v2 standard)

**If you only have 20 minutes — do this minimum:**  
Copy the `FAQPage` `<script type="application/ld+json">` block from `joondalup.html`, paste it into `wanneroo.html` before `</body>`, rewrite the three Q&As to be Wanneroo-specific. Add `GeoCoordinates` + `OpeningHoursSpecification` inside the LocalBusiness block. Push. Schema gap closed in one commit.

**Full 2–3 hr upgrade:**
- Local signals: Wanneroo Town Centre, Lake Joondalup green corridor (rodent + spider pressure), Wanneroo Raceway surrounds, urban-fringe bushland
- Drive time: ~12 min from Warwick
- Mini case study: e.g. roof rats along Quinns Rocks Rd corridor
- Every paragraph genuinely Wanneroo — not a template swap

---

### 2. ⬆️ Upgrade `duncraig.html` ← same session as task 1

**Keyword:** `pest control duncraig` — strong residential intent, low KD

**Current state:** 1507w · 3 JSON-LD blocks · same v1 schema gap  
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
