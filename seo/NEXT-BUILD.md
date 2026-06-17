# NEXT BUILD — 2026-06-17

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage.
**~30% of 14-day plan. NO CHANGE FOR 16 DAYS RUNNING.**

`wanneroo.html` (1443w / 12 @type) and `duncraig.html` (1507w / 12 @type) are both still at v1 — thin schema, below word-count target. Every day these sit at v1 delays the rest of the suburb cluster (sorrento, hillarys, balcatta, etc.) which all depend on this standard being set. These two pages are the gate.

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← 16TH CARRY-OVER — START HERE

**Keyword:** `pest control wanneroo` — low KD, high local intent

**Fastest path in (20 min — just the schema, unblocks indexing immediately):**
Open `joondalup.html`. Copy the `<script type="application/ld+json">` block with `"@type": "FAQPage"` and paste it into `wanneroo.html` just before `</body>`. Rewrite the three questions Wanneroo-specific:
- "Do you cover the Wanneroo Town Centre area?"
- "What pests come from the Lake Joondalup bushland?"
- "How quickly can you reach Wanneroo from Warwick?"
Then copy `GeoCoordinates` + `OpeningHoursSpecification` from `joondalup.html`. 20 min, push, done. Full word-count upgrade can come after.

**Full upgrade (2–3 hrs):**
- **Current:** 1443w · 12 @type · missing FAQPage, GeoCoordinates, OpeningHoursSpecification
- **Target:** ~3000w · 31 @type (joondalup v2 standard)
- **Required local signals:** Wanneroo Town Centre, Lake Joondalup green corridor (rodent + spider pressure), Wanneroo Raceway surrounds, urban-fringe bushland, drive time ~12 min from Warwick, 1 mini case study (roof rats near Quinns Rocks Rd)
- **Not a template swap** — every paragraph must be genuinely Wanneroo-specific

---

### 2. ⬆️ Upgrade `duncraig.html` ← same session

**Keyword:** `pest control duncraig` — low KD, strong residential intent

- **Current:** 1507w · 12 @type · same v1 schema gap as wanneroo
- **Target:** ~3000w · 31 @type
- **Required local signals:** Duncraig Leisure Centre, Hepburn Heights bushland (ant + spider pressure), leafy-suburb roof-cavity rats, Carine Glades proximity, drive time ~10 min from Warwick
- **Must read distinctly from wanneroo** — different pest profile, different voice

---

### 3. 🆕 Build `sorrento.html` ← only once tasks 1 + 2 are pushed

**Keyword:** `pest control sorrento` — **260 searches/mo, KD8** — highest unbuilt volume in Tier-1 cluster

- Build to joondalup v2 standard from day one: ~3000w · 31 @type
- **Local signals:** Sorrento Quay, Marmion Marine Park, sandy-soil ant colonies, coastal cockroach + silverfish pressure, older-unit mice near marine park, ~10 min drive from Warwick

---

## BLOCKERS / FLAGS

- **Termite: HOLD.** `/termite-inspection-perth` (480/mo, KD32, $6.20 CPC — highest CPC on board) stays staged/unpublished until WA DoH pest licence + termite endorsement are confirmed. Unlocking this is the single most valuable thing the licence enables.
- **GBP is still the #1 unblocked lever.** If the Google Business Profile isn't verified with a review-generation engine running, an hour there outperforms any page built today. Map 3-pack = where the phone calls come from.
- **Tier-1 suburbs queued after wanneroo + duncraig:** Balcatta (110/mo, KD6), Hillarys (90/KD7), Marangaroo (90/KD0), Greenwood (70/KD0), Stirling (70/KD0), Warwick home-base (KD0)
- **MOFU cost pages (after suburb cluster):** `pest-control-cost-perth` (1300/mo, KD8) + `pest-control-prices` (720/mo, KD6) — transparent-pricing moat, no competitor has built this
- **Service gaps still queued:** bee-removal (480/mo, KD27), wasp-removal (170/mo, KD8), mosquito-control (260/mo, KD11), bed-bug-treatment (110/mo, KD17), flea-treatment (140/mo, KD11), commercial-pest-control (390/mo, KD30)
