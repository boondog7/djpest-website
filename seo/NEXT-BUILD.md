# NEXT BUILD — 2026-09-25

> ## HARD RULES FOR THE CLOUD ROUTINE (added 22 Sep 2026 by Dane's Mac session)
> 1. **Never edit `site.json → "unpublished"`, the `PRICES` dict, or any dollar figure.** Prices are Dane's decision. Build the page, leave it gated, and list the proposed prices in this file for him to confirm.
> 2. **Never claim a page is "live".** The cloud commits HTML; only `./deploy.sh --prod` on the Mac deploys.
> 3. Every public claim passes the compliance scanner and the licensing wording is the fixed string ("carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence"), never bare "Licensed technicians".
> 4. Read `~/business/djpest/marketing/vibe/brand-bible.md` voice rules before writing copy.


## Progress summary
**Done: ~100% of the 14-day plan. 14 service/MOFU pages + 98 suburb pages + service-areas hub + 5 blog posts, all with connected @graph JSON-LD. Blog pipeline is now the main growth lever.**

---

## Dane: pending actions on your Mac
1. **Deploy German cockroach post (TODAY — Thu 25 Sep):** `./deploy.sh --prod` for `build/posts/how-to-get-rid-of-german-cockroaches.html` — draft is ready in `blog/_drafts/ready/how-to-get-rid-of-german-cockroaches/`, matches the Mon/Thu publish cadence.
2. **Deploy wasp post:** `./deploy.sh --prod` for `build/posts/how-to-get-rid-of-a-wasp-nest.html` (has real Pexels hero image; ready to go).
3. **Deploy termite ID post:** `./deploy.sh --prod` for `build/posts/what-do-termites-look-like.html`.
4. **Licence gate check:** If termite endorsement is NOT yet held, add `/termite-inspection-perth`, `/termite-treatment-perth`, `/termite-treatment-cost-perth` to `site.json → unpublished` before next deploy.

---

## Today's build tasks

### Task 1 (highest priority) — `blog/white-tail-spider-bite.html`
**Keyword:** `white tail spider bite` — **8,100/mo, KD 27**
**Fold in:** `are white tail spiders dangerous` (480), `what does a white tail spider bite look like` (320), `can a white tail spider kill you` (320), `how to get rid of white tail spiders` (90). ~9,310/mo total coverage.
**Why now:** Highest-volume blog post in the queue by 13×. Spider bites are evergreen (no seasonal cliff), KD27 is achievable, and `/spider-control-perth` needs organic support. Next scheduled publish date: **Mon 29 Sep** — build today, publish Monday.
**How:** Follow the established blog post format. No claims re: venom lethality that can't be sourced — white-tails are "necrotic wound" myth territory; cite the Australian Medical Association position. Internal link to `/spider-control-perth` + `/general-pest-control-perth`.

### Task 2 — FAQPage JSON-LD on blog posts
**File:** `build/pages/30_company.py` — the `_post` template (the `faq_schema` component already exists on service pages, just not wired into `_post`).
**Why:** All 5 existing blog posts have zero `@type: FAQPage` structured data. Blog posts are prime AI Overview / Perplexity citation targets; FAQ schema is the difference between a blue link and a featured answer block.
**How:** Wire `c["faq_schema"]` into `_post` and regenerate. Do NOT rebuild/overwrite the published post HTML manually — let `build.py` regenerate on the Mac.

### Task 3 — `blog/how-to-get-rid-of-silverfish.html`
**Keyword:** `how to get rid of silverfish` — **1,600/mo, KD moderate**
**Fold in:** `how get rid silverfish` (bundle 20).
**Why:** Queue #4; schedules for Mon 29 Sep if white-tail spider bite ships first, or Thu 2 Oct. No seasonal cliff. Links to `/general-pest-control-perth`.
**Draft source:** `blog/_drafts/14_how-to-get-rid-of-silverfish.md`

---

## Off-site (Dane — cannot build from code)
- **GBP at Warwick 6024** — still the single biggest lever for actual phone calls (7/8 consensus brains). Map 3-pack placement outweighs any page for "pest control near me" queries.
- **NAP citations:** TrueLocal, Yellow Pages AU, Hipages, Oneflare, Yelp AU, StartLocal — consistent "Warwick WA 6024".
- **Review asks:** SMS/email after every job. Ask the client to mention suburb + pest in their review.
