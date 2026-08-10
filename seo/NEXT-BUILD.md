# NEXT BUILD — 2026-08-10

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage.
**~30% of 14-day plan. DAY 70 — NO CHANGE FROM YESTERDAY.**

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← **DAY 70. 20 MINUTES. DO IT NOW.**

**Keyword:** `pest control wanneroo` — local intent, low KD, directional traffic

**Current state:** 1443w · v1 schema (3 blocks) · missing FAQPage, GeoCoordinates, OpeningHoursSpecification
**Target:** ~3000w · joondalup v2 standard (4 schema blocks)

**Exact steps (copy-paste job):**
1. Open `joondalup.html` → copy the FAQPage `<script type="application/ld+json">` block
2. Paste before `</body>` in `wanneroo.html`
3. Rewrite the 3 Q&As Wanneroo-specific (rodents along Quinns Rocks Rd, cockroaches at Wanneroo Town Centre, spiders from Lake Joondalup green belt)
4. Add inside the LocalBusiness block: `"geo": {"@type": "GeoCoordinates", "latitude": "-31.7527", "longitude": "115.8062"}`
5. Add `openingHoursSpecification` (copy from `joondalup.html`)
6. Push: `git add wanneroo.html && git commit -m "feat: upgrade wanneroo schema to v2" && git push`

---

### 2. ⬆️ Upgrade `duncraig.html` ← same session as task 1

**Keyword:** `pest control duncraig` — strong residential intent, low KD

**Current state:** 1507w · v1 schema (3 blocks) · same gaps as wanneroo
**Target:** ~3000w · 4 schema blocks

- GeoCoordinates: `-31.8295, 115.7727`
- Local signals: Hepburn Heights bushland, Duncraig Leisure Centre, leafy suburb roof-cavity rats, ~10 min from Warwick
- Same copy-paste schema fix as wanneroo (change suburb name + GeoCoordinates + 3 local FAQs)

---

### 3. 💰 Publish `pest-control-cost-perth.html` ← EASIEST WIN IF 1+2 FEEL HEAVY

**Keywords:** `how much does pest control cost` — 1300/mo, KD8 · `pest control prices` — 720/mo, KD6

**Draft is already written and sitting here:**
- `blog/_drafts/01_how-much-does-pest-control-cost.md`
- `blog/_drafts/12_how-much-does-it-cost-for-pest-control.md` (possible merge source)

**Why today:** No competitor publishes real Perth $ tables. The MOFU pricing moat is the battle plan's highest-leverage move alongside GBP. The draft exists — this is a 45-minute conversion job: open the .md, convert to HTML, add schema, link from homepage + service pages, push.

---

## COMING NEXT (after above are done)
- `sorrento.html` — 260/mo, KD8 — highest-volume unbuilt Tier-1 suburb
- `balcatta.html` — 110/mo, KD6
- `hillarys.html` — 90/mo, KD7
- `bee-removal-perth.html` — 480/mo, KD27
- `commercial-pest-control-perth.html` — 390/mo, KD30

---

## BLOCKERS / FLAGS

- **Termite: HOLD.** `/termite-inspection-perth` (480/mo, KD32, $6.20 CPC) stays staged/unpublished until WA DoH pest licence + termite endorsement are confirmed.
- **GBP is still the #1 unblocked lever.** If the Google Business Profile isn't verified with a review-generation engine running, an hour there outperforms any page built today.
- **70 days on the same carry-over.** The schema patch on `wanneroo.html` is one copy-paste and 3 sentence rewrites. If you have 20 minutes, this is done.
