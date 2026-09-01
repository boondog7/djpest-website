# NEXT BUILD — 2026-09-01

## Progress snapshot
**Done:** 4 service pages (ant ✅, cockroach ✅, rodent ✅, spider ✅) + 3 suburb pages (joondalup v2 ✅, wanneroo ⚠️ v1, duncraig ⚠️ v1) + homepage.
**~30% of 14-day plan. DAY 92 — NO HTML CHANGE SINCE 8 AUG (24 days idle). Same 3 tasks for the 24th morning in a row.**

---

## TODAY'S TASKS (priority order)

### 1. ⬆️ Upgrade `wanneroo.html` ← **24 DAYS UNCHANGED. THIS IS A 20-MINUTE JOB.**

**Keyword:** `pest control wanneroo` — local intent, low KD, directional traffic

**Current state:** 1443w · v1 schema (3 blocks) · missing FAQPage, GeoCoordinates, OpeningHoursSpecification
**Target:** ~3000w · joondalup v2 standard (4 schema blocks)

**Exact steps:**
1. Open `joondalup.html` → copy the FAQPage `<script type="application/ld+json">` block
2. Paste before `</body>` in `wanneroo.html`
3. Rewrite the 3 Q&As Wanneroo-specific (rodents near Quinns Rocks Rd, cockroaches at Wanneroo Town Centre, spiders from Lake Joondalup greenbelt)
4. Add inside LocalBusiness block: `"geo": {"@type": "GeoCoordinates", "latitude": "-31.7527", "longitude": "115.8062"}`
5. Add `openingHoursSpecification` (copy from `joondalup.html`)
6. `git add wanneroo.html && git commit -m "feat: upgrade wanneroo schema to v2" && git push`

---

### 2. ⬆️ Upgrade `duncraig.html` ← same session, another 20 minutes

**Keyword:** `pest control duncraig` — residential intent, low KD

**Current state:** 1507w · v1 schema (3 blocks) · same gaps as wanneroo
**Target:** ~3000w · 4 schema blocks

- GeoCoordinates: `-31.8295, 115.7727`
- Local signals: Hepburn Heights bushland (roof-cavity rats), Duncraig Leisure Centre, leafy suburb pressure, ~10 min from Warwick
- Same copy-paste schema fix + Duncraig-specific FAQs

---

### 3. 💰 Build `pest-control-cost-perth.html` ← drafts already written, just waiting

**Keywords:** `how much does pest control cost` — 1300/mo, KD8 · `pest control prices` — 720/mo, KD6

**Drafts to merge (already exist in `blog/_drafts/`):**
- `01_how-much-does-pest-control-cost.md` — main article
- `12_how-much-does-it-cost-for-pest-control.md` — merge source
- `23_how-much-is-pest-control.md` — merge source

**Why now:** Three overlapping drafts → merge into one authoritative Perth pricing page with real $ tables. No competitor publishes transparent pricing. Dane's CA background = "no hidden fees" E-E-A-T angle. ~45 min: combine drafts → add HowTo + FAQPage schema → link from homepage + all 4 service pages → push. Highest-leverage MOFU move in the entire plan.

---

## COMING NEXT (after above are done)
- `sorrento.html` — 260/mo, KD8 — highest-volume unbuilt Tier-1 suburb
- `balcatta.html` — 110/mo, KD6
- `hillarys.html` — 90/mo, KD7
- `bee-removal-perth.html` — 480/mo, KD27 (easy win, fragmented competitor field)
- `commercial-pest-control-perth.html` — 390/mo, KD30

---

## BLOCKERS / FLAGS

- **Termite: HOLD.** `/termite-inspection-perth` (480/mo, KD32, $6.20 CPC) — highest-value gap in the plan — stays staged/unpublished until WA DoH pest licence + termite endorsement are confirmed. Do not publish termite expertise claims or a licence number until held.
- **GBP is still the #1 unblocked lever.** Google Business Profile + review-generation engine > any page built today. If not verified and running, that is the first call to make.
- **24 days idle on 20-minute tasks.** The steps above are copy-paste + 3 sentence rewrites. The cost-page drafts are already written in `blog/_drafts/`. Open the file. Every day this waits, a competitor is collecting the click.
