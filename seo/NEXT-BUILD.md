# NEXT BUILD — 2026-09-23

> ## HARD RULES FOR THE CLOUD ROUTINE (added 22 Sep 2026 by Dane's Mac session)
> 1. **Never edit `site.json → "unpublished"`, the `PRICES` dict, or any dollar figure.** Prices are Dane's decision. Build the page, leave it gated, and list the proposed prices in this file for him to confirm.
> 2. **Never claim a page is "live".** The cloud commits HTML; only `./deploy.sh --prod` on the Mac deploys.
> 3. Every public claim passes the compliance scanner and the licensing wording is the fixed string ("carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence"), never bare "Licensed technicians".
> 4. Read `~/business/djpest/marketing/vibe/brand-bible.md` voice rules before writing copy.


## Progress summary
**Done: 13 service pages + ~95 suburb pages + pricing hub + service-areas hub + 3 blog posts; ~98% of 14-day battle plan complete.**

Same status as yesterday — the one remaining build gap is still open.

---

## Next tasks (priority order)

### 1. ⚠️ CARRY-OVER (day 2) — Build `termite-treatment-cost-perth.html`
**Keyword:** `termite treatment cost` — 720/mo, KD8, CPC $6.20 (highest CPC in the set)
**Why it's still #1:** This was yesterday's priority and still hasn't been built. It's the only MOFU cost page in the battle plan that's missing. `/pest-control-prices-perth` covers termite in one FAQ line — not enough to own the `termite treatment cost` query, which at $6.20 CPC means competitors pay real money for every click. A standalone page with worked cost tables would rank uncontested.

**What to build:**
- Filename: `termite-treatment-cost-perth.html`
- H1: "Termite Treatment Cost Perth (2026) — What It Actually Costs"
- Core content:
  - Table 1 — Chemical barrier: perimeter metres × drilling/trenching cost (e.g. 120m = ~$1,800, 200m = ~$3,200, 280m = ~$4,500; Termidor HE adds ~20%)
  - Table 2 — Bait system: station count × install; annual monitoring fee
  - Worked example: 180m² slab home in Greenwood — step-by-step quote breakdown
  - Factors that move the price (sub-floor access, heritage stone, garden beds against the wall, timber floors)
  - CA angle: "No line-item surprises — here's what every dollar pays for"
- Internal links: `/termite-inspection-perth`, `/termite-treatment-perth`, `/pest-control-prices-perth`, `/warwick`
- JSON-LD: `@graph` — LocalBusiness + Service + FAQPage + BreadcrumbList (copy pattern from termite-inspection-perth.html)
- **⚠️ Proposed prices below — Dane to confirm before deploying:**
  - Chemical barrier (Termidor): $1,800–$4,500 depending on perimeter
  - Termidor HE upgrade: +15–25% on the above
  - Bait system install: $1,800–$3,200; annual monitoring ~$600–$900/yr

**How to build:** Copy `termite-inspection-perth.html` as scaffold; adapt H1/meta/content/tables/schema. Or add an entry in `build/pages/10_services.py` following the bee/flea pattern.

---

### 2. Publish next blog post from the draft queue
**File:** `blog/_drafts/02_how-to-dispose-of-a-wasp-nest.md`
**Keyword:** `how to dispose of a wasp nest` — 1,600/mo, KD10, CPC $0.79 (rank 4 in pipeline)
**Why:** Blog cadence is 2/week, 3 posts are live, 26 drafts are staged. The wasp disposal post captures people who already have a nest — they're one step from booking a removal. Script exists: `build/publish-next-post.sh`.

---

### 3. Internal linking audit (30-min skim)
With ~95 suburb pages live, verify hub-and-spoke wiring:
- `/service-areas` → all suburb pages (check none are missing)
- Every suburb page → `/service-areas` + 2–3 relevant service pages (e.g. Yanchep → `/termite-inspection-perth` + `/ant-control-perth`)
- Every service page → 3–5 nearby suburb pages in a "We cover…" strip
This is the Day 11–14 "connect + dominate" step from the battle plan — still unverified.

---

## Off-site tasks (not build work — Dane's side)
- **GBP at Warwick 6024** — still the single highest-leverage move for phone calls. Map pack > organic rankings.
- **NAP citations** (TrueLocal, Yellow Pages AU, Hipages, Oneflare, Yelp AU, StartLocal) — consistent "Warwick WA 6024 / 0468 170 107"
- **Review-ask SMS/email** after every job; ask clients to mention suburb + pest in the review text

## Blockers
- None on the build side.
- GBP outranks all build tasks for phone calls — if not yet verified, it is the real #1.
