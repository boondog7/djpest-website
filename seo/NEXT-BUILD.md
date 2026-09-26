# NEXT BUILD — 2026-09-26

> ## HARD RULES FOR THE CLOUD ROUTINE (added 22 Sep 2026 by Dane's Mac session)
> 1. **Never edit `site.json → "unpublished"`, the `PRICES` dict, or any dollar figure.** Prices are Dane's decision. Build the page, leave it gated, and list the proposed prices in this file for him to confirm.
> 2. **Never claim a page is "live".** The cloud commits HTML; only `./deploy.sh --prod` on the Mac deploys.
> 3. Every public claim passes the compliance scanner and the licensing wording is the fixed string ("carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence"), never bare "Licensed technicians".
> 4. Read `~/business/djpest/marketing/vibe/brand-bible.md` voice rules before writing copy.


## Progress summary
**Done: ~100% of the 14-day plan. 14 service/MOFU pages + 98 suburb pages + service-areas hub + 5 blog posts, all with connected @graph JSON-LD. Blog pipeline is now the main growth lever.**

Published blog posts: how-to-get-rid-of-ants, how-to-get-rid-of-cockroaches, how-much-does-pest-control-cost, how-to-get-rid-of-a-wasp-nest, what-do-termites-look-like.

---

## Dane: pending actions on your Mac
1. **⚠️ Deploy German cockroach post (OVERDUE — was due Thu 25 Sep):** `./deploy.sh --prod` for `build/posts/how-to-get-rid-of-german-cockroaches.html` — draft is ready in `blog/_drafts/ready/how-to-get-rid-of-german-cockroaches/`. Do this today so Mon 29 Sep is free for white-tail spider.
2. **Licence gate check:** If termite endorsement is NOT yet held, confirm `/termite-inspection-perth`, `/termite-treatment-perth`, `/termite-treatment-cost-perth` are in `site.json → unpublished` before next deploy.

---

## Today's build tasks

### Task 1 (highest priority) — `blog/white-tail-spider-bite`
**Keyword:** `white tail spider bite` — **8,100/mo, KD 27**
**Fold in:** `are white tail spiders dangerous` (480), `what does a white tail spider bite look like` (320), `can a white tail spider kill you` (320), `how to get rid of white tail spiders` (90). ~9,310/mo total coverage.
**Why now:** Highest-volume blog post in the queue by 13×. Evergreen, no seasonal cliff. KD27 is achievable on a growing domain. `/spider-control-perth` needs organic blog support. **Publish date: Mon 29 Sep.** Draft must be ready before then.
**How:** Write draft to `blog/_drafts/ready/white-tail-spider-bite/`. Do NOT claim venom lethality — white-tails are "necrotic wound" myth territory; cite the AMA/scientific position. Internal links: `/spider-control-perth` + `/general-pest-control-perth`. Queue position: #5 in QUEUE.md.
**Same task as yesterday — still not started. This is the one.**

### Task 2 — FAQPage JSON-LD on all blog posts
**File:** `build/pages/30_company.py` — wire `c["faq_schema"]` into the `_post` template. The component already exists on service pages; just not used in posts yet.
**Why:** All 5 live blog posts have zero `@type: FAQPage` schema. Blog posts are prime AI Overview / Perplexity citation targets — FAQ schema is the difference between a blue link and a featured answer. Quick win, do it before the next deploy cycle.
**How:** Edit the `_post` template in `30_company.py`. Regenerate on the Mac via `build.py` — do NOT hand-edit the built HTML files.

### Task 3 — `blog/how-to-get-rid-of-silverfish`
**Keyword:** `how to get rid of silverfish` — **1,600/mo, KD 20**
**Fold in:** `how get rid silverfish` (1,300/mo, bundle #20, KD 25).
**Why:** Queue #4. Schedule for Thu 2 Oct if white-tail spider ships Mon 29 Sep. Matches Mon/Thu cadence. Links to `/general-pest-control-perth`. Draft outline at `blog/_drafts/14_how-to-get-rid-of-silverfish.md`.

---

## Off-site (Dane — cannot build from code)
- **GBP at Warwick 6024** — still the single biggest lever for actual phone calls (7/8 consensus brains). Map 3-pack placement outweighs any page for "pest control near me" queries.
- **NAP citations:** TrueLocal, Yellow Pages AU, Hipages, Oneflare, Yelp AU, StartLocal — consistent "Warwick WA 6024".
- **Review asks:** SMS/email after every job. Ask the client to mention suburb + pest in their review.
