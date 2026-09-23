# NEXT BUILD — 2026-09-23

> ## HARD RULES FOR THE CLOUD ROUTINE (added 22 Sep 2026 by Dane's Mac session)
> 1. **Never edit `site.json → "unpublished"`, the `PRICES` dict, or any dollar figure.** Prices are Dane's decision. Build the page, leave it gated, and list the proposed prices in this file for him to confirm.
> 2. **Never claim a page is "live".** The cloud commits HTML; only `./deploy.sh --prod` on the Mac deploys.
> 3. Every public claim passes the compliance scanner and the licensing wording is the fixed string ("carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence"), never bare "Licensed technicians".
> 4. Read `~/business/djpest/marketing/vibe/brand-bible.md` voice rules before writing copy.


## Progress summary
**Built 23 Sep (cloud, NOT deployed): /termite-treatment-cost-perth, /blog/how-to-get-rid-of-a-wasp-nest, internal-linking pass. ~100% of the 14-day plan's build work.**
Panel: 3 Claude advisers + 3 Claude reviewers (the real 10-brain panel needs Mac API keys). All blockers fixed.

---

## Dane: before `./deploy.sh --prod`
1. **Licence gate:** termite cost page is ungated like the other termite pages. If the termite endorsement isn't held, add `/termite-treatment-cost-perth` to `site.json → unpublished`.
2. **Wasp post hero image:** uses og-default.jpg. Add a real paper-wasp nest photo (Pexels) and set `img`/`alt` in `build/posts/how-to-get-rid-of-a-wasp-nest.html`.
3. **Sitewide wording change:** `licence_label` now reads the fixed supervision sentence (footer + JSON-LD on every page). Check you're happy.
4. Proposed (not published) itemised termite line figures, for you to price if wanted: trench $/m, drill-and-inject $/m, bait monitoring $/visit.

## Next tasks
1. Blog queue #2 `what-do-termites-look-like` (1900/KD26 + white ants 1000/KD6), termite season Sep–Nov.
2. Add FAQPage schema support to file-based blog posts (`_post` in `build/pages/30_company.py`).
3. Suburb pages still say "Licensed under the WA Pesticides Regs" / "Licensed pest control in…" (hero trust + meta). Decide whether to switch to the fixed wording.
4. Ledger tables still scroll horizontally at 390px (price table 436px in 350px box). Consider a stacked mobile layout in site.css.

## Off-site (Dane)
- GBP at Warwick 6024, NAP citations, review asks after every job. Still the biggest lever for calls.
