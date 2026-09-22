# NEXT BUILD — 2026-09-22

> ## HARD RULES FOR THE CLOUD ROUTINE (added 22 Sep 2026 by Dane's Mac session)
> 1. **Never edit `site.json → "unpublished"`, the `PRICES` dict, or any dollar figure.** Prices are Dane's decision. Build the page, leave it gated, and list the proposed prices in this file for him to confirm.
> 2. **Never claim a page is "live".** The cloud commits HTML; only `./deploy.sh --prod` on the Mac deploys.
> 3. Every public claim passes the compliance scanner and the licensing wording is the fixed string ("carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence"), never bare "Licensed technicians".
> 4. Read `~/business/djpest/marketing/vibe/brand-bible.md` voice rules before writing copy.


## Progress summary
**Done: 13 service pages + ~95 suburb pages + pricing hub + service-areas hub + 3 blog posts; ~98% of 14-day battle plan complete.**

Everything from the battle plan's Day 2–10 is shipped: all Tier-1 and Tier-2 corridor suburbs, all BOFU service pages, MOFU pricing hub + blog post. One MOFU cost page is the last gap.

---

## Next tasks (priority order)

### 1. Build `termite-treatment-cost-perth.html` ← THE THING TO DO TODAY
**Keyword:** `termite treatment cost` — 720/mo, KD8, CPC $6.20 (highest in the set)
**Why it's next:** The pricing hub (`/pest-control-prices-perth`) has a single termite FAQ. A dedicated page with a worked cost table (perimeter metres → drilling + soil treatment vs baiting system) would own this query outright — and at $6.20 CPC, competitors are spending real money here. No competitor has a transparent worked example.

**What to build:**
- Filename: `termite-treatment-cost-perth.html`
- H1: "Termite Treatment Cost Perth (2026) — What It Actually Costs"
- Core content: two cost tables (chemical barrier: perimeter metres × drilling/trenching; bait system: station count × annual monitoring); worked real-house example (e.g. 180 m² slab home in Greenwood); factors that move the price (timber floor, sub-floor, heritage stone, garden beds against the wall)
- CA angle: "no line-item surprises — here's what you get for every dollar"
- Internal links to: `/termite-inspection-perth`, `/termite-treatment-perth`, `/pest-control-prices-perth`, `/warwick` (home base)
- JSON-LD: `@graph` with LocalBusiness + Service + FAQPage + BreadcrumbList (same pattern as termite-inspection page)
- Proposed prices (Dane to confirm): chemical barrier $1,800–$4,500 depending on perimeter; Termidor HE typically 15–25% more than standard; bait station install $1,800–$3,200 + ~$600–$900/yr monitoring

**How to build:** add a new file entry in `build/pages/10_services.py` following the bee/flea pattern, or write it directly as static HTML following the termite-inspection page structure.

---

### 2. Publish next blog post from queue
**File:** `blog/_drafts/02_how-to-dispose-of-a-wasp-nest.md` — already drafted, just needs HTML rendering and publishing.
- Blog cadence is set to 2/week; 3 posts are live, 9 drafts are staged.
- Wasp content = high-conversion intent (people googling "how to get rid of a wasp nest" are 1 call away from booking).
- Run the blog publish script, push.

---

### 3. Internal linking audit (30-min skim)
With ~95 suburb pages now live, verify the hub-and-spoke wiring:
- Every suburb page → `/service-areas` (hub) and the 2–3 most relevant service pages (e.g. Yanchep → `/termite-inspection-perth` + `/ant-control-perth`)
- `/service-areas` → all suburb pages (already has a full list — confirm no new suburbs are missing)
- Every service page → 3–5 nearby suburb pages in a "We cover…" strip
This is the Day 11–14 "connect + dominate" step from the battle plan.

---

## Off-site tasks (not build work — Dane's side)
- **GBP at Warwick 6024** — still the single highest-leverage move. If not verified yet, this is the real #1 task for calls.
- **NAP citations** (TrueLocal, Yellow Pages AU, Hipages, Oneflare, Yelp AU, StartLocal) — consistent "Warwick WA 6024 / 0468 170 107"
- **Review-ask SMS/email** after every job

## Blockers
- None on the build side. Everything above is unblocked.
- GBP outranks all of the above for phone calls — prioritise it over any build task.
