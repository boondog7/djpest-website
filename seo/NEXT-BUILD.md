# NEXT BUILD — 2026-06-15

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage.
**~30% of 14-day plan. NO CHANGE FOR 14 DAYS RUNNING.**

`wanneroo.html` (1443w / 3 JSON-LD) and `duncraig.html` (1507w / 3 JSON-LD) have been sitting at v1 since Day 1.
The 14-day plan has elapsed. These two files are the only thing standing between 30% and 55% plan completion.

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← 14TH CARRY-OVER — DO THIS FIRST

**Keyword:** `pest control wanneroo` — low KD, high local intent

**Micro-entry (20 min — just the schema):**
Open `joondalup.html`. Copy the `<script type="application/ld+json">` block containing `"@type": "FAQPage"`. Paste it into `wanneroo.html` just before `</body>`. Rewrite the three questions as Wanneroo-specific:
- "Do you cover the Wanneroo Town Centre area?"
- "What pests come from the Lake Joondalup bushland?"
- "How quickly can you reach Wanneroo from Warwick?"
Then add GeoCoordinates + OpeningHoursSpecification from `joondalup.html`. 20 minutes. Push it.

**Full upgrade (2–3 hrs):**
- **Current:** 1443w · 3 JSON-LD blocks · missing FAQPage, GeoCoordinates, OpeningHoursSpecification
- **Target:** ~3000w · 4 JSON-LD blocks matching `joondalup.html` v2 standard
- **Required local signals:** Wanneroo Town Centre, Lake Joondalup green corridor (rodent + spider pressure), Wanneroo Raceway surrounds, urban-fringe bushland, drive time ~12 min from Warwick, 1 mini case study (roof rats near Quinns Rocks Rd)
- **Not a template swap** — every paragraph must be genuinely Wanneroo-specific

### 2. ⬆️ Upgrade `duncraig.html` ← same session if time allows

- **Keyword:** `pest control duncraig` — low KD, strong residential intent
- **Current:** 1507w · 3 JSON-LD blocks · same v1 schema gap
- **Target:** ~3000w · 4 JSON-LD blocks (add FAQPage, GeoCoordinates, OpeningHoursSpecification)
- **Required local signals:** Duncraig Leisure Centre, Hepburn Heights bushland (ant + spider pressure), leafy-suburb roof-cavity rats, proximity to Carine Glades, drive time ~10 min from Warwick
- **Must read distinctly from wanneroo** — different pest angle, different voice

### 3. 🆕 Build `sorrento.html` ← only after tasks 1 + 2

- **Keyword:** `pest control sorrento` — **260 searches/mo, KD8** — highest unbuilt volume in the Tier-1 cluster
- **Why:** Coastal profile is genuinely distinct (cockroaches near beach, sandy-soil ants, silverfish pressure, older-unit mice near Marmion Marine Park)
- **Build to joondalup v2 standard from day one:** ~3000w · 4 JSON-LD blocks · local signals = Sorrento Quay, Marmion Marine Park, ~10 min drive from Warwick

---

## BLOCKERS / FLAGS

- **Termite: HOLD.** `/termite-inspection-perth` (480/mo, KD32, $6.20 CPC — highest CPC on the board) cannot go live until WA DoH pest licence + termite endorsement are confirmed. Sorting the licence unlocks the most lucrative keyword on the plan.
- **GBP remains the #1 unblocked lever.** If the Google Business Profile isn't verified with a review-generation engine running, one hour there outperforms any page built today. Map 3-pack = where the phone calls come from.
- **Tier-1 suburbs queued after wanneroo + duncraig:** Balcatta (110/KD6), Hillarys (90/KD7), Marangaroo (90/KD0), Greenwood (70/KD0), Stirling (70/KD0), Warwick home-base (KD0)
- **MOFU cost pages (after suburbs):** `pest-control-cost-perth` (1300/mo, KD8) + `pest-control-prices` (720/mo, KD6) — transparent-pricing moat; Dane's CA background = E-E-A-T angle no competitor has built
- **Service gaps still queued:** bee-removal (480/KD27), wasp-removal (170/KD8), mosquito-control (260/KD11), bed-bug-treatment (110/KD17), flea-treatment (140/KD11), commercial-pest-control (390/KD30)
