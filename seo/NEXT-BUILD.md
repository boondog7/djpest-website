# NEXT BUILD — 2026-08-13

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage + 2 blog pages.
**~30% of 14-day plan. DAY 73 — SAME CARRY-OVER AS YESTERDAY (and the 72 days before).**

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← **DAY 73. STILL 20 MINUTES. DO IT NOW.**

**Keyword:** `pest control wanneroo` — local intent, low KD, directional traffic

**Current state:** 1443w · v1 schema (3 blocks) · missing FAQPage, GeoCoordinates, OpeningHoursSpecification
**Target:** ~3000w · joondalup v2 standard (4 schema blocks, 21+ @type refs)

**Exact steps (copy-paste job):**
1. Open `joondalup.html` → copy the FAQPage `<script type="application/ld+json">` block
2. Paste before `</body>` in `wanneroo.html`
3. Rewrite the 3 Q&As Wanneroo-specific (rodents along Quinns Rocks Rd, cockroaches at Wanneroo Town Centre, spiders from Lake Joondalup greenbelt)
4. Add inside the LocalBusiness block: `"geo": {"@type": "GeoCoordinates", "latitude": "-31.7527", "longitude": "115.8062"}`
5. Add `openingHoursSpecification` (copy from `joondalup.html`)
6. Push: `git add wanneroo.html && git commit -m "feat: upgrade wanneroo schema to v2" && git push`

---

### 2. ⬆️ Upgrade `duncraig.html` ← same session, 20 more minutes

**Keyword:** `pest control duncraig` — strong residential intent, low KD

**Current state:** 1507w · v1 schema (3 blocks) · same gaps as wanneroo
**Target:** ~3000w · 4 schema blocks

- GeoCoordinates: `-31.8295, 115.7727`
- Local signals: Hepburn Heights bushland, Duncraig Leisure Centre, leafy suburb roof-cavity rats, ~10 min from Warwick
- Same copy-paste schema fix + Duncraig-specific FAQs

---

### 3. 💰 Build `pest-control-cost-perth.html` ← drafts already written, zero prep needed

**Keywords:** `how much does pest control cost` — 1300/mo, KD8 · `pest control prices` — 720/mo, KD6

**Drafts sitting ready:**
- `blog/_drafts/01_how-much-does-pest-control-cost.md` (main)
- `blog/_drafts/12_how-much-does-it-cost-for-pest-control.md` (merge source)
- `blog/_drafts/23_how-much-is-pest-control.md` (merge source)

**Why now:** Three drafts on the same topic = merge into one authoritative Perth pricing page with real $ tables. No competitor does this. Dane's CA background = the "transparent, no-hidden-fees" E-E-A-T angle every AI flagged. ~45 min: combine drafts → add HowTo + FAQPage schema → link from homepage + all 4 service pages → push. This is the MOFU moat the battle plan calls the highest-leverage move.

---

## COMING NEXT (after above are done)
- `sorrento.html` — 260/mo, KD8 — highest-volume unbuilt Tier-1 suburb
- `balcatta.html` — 110/mo, KD6
- `hillarys.html` — 90/mo, KD7
- `bee-removal-perth.html` — 480/mo, KD27 (easy, fragmented field)
- `commercial-pest-control-perth.html` — 390/mo, KD30

---

## BLOCKERS / FLAGS

- **Termite: HOLD.** `/termite-inspection-perth` (480/mo, KD32, $6.20 CPC) — highest-value gap in the plan — stays staged/unpublished until WA DoH pest licence + termite endorsement are confirmed. Do not publish any termite expertise claims or licence number until held.
- **GBP is still the #1 unblocked lever.** Google Business Profile + review-generation engine > any page built today. If it isn't verified and running, that is still the first phone call to make.
- **73 days on the same carry-over.** Task 1 (wanneroo schema upgrade) is one copy-paste and 3 sentence rewrites. The drafts for Task 3 are already written. There is nothing to prepare. The only move left is to open the file and do it.
