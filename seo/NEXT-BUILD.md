# NEXT BUILD — updated 2026-09-18 (site rebuilt, read this before doing anything)

## What changed on 18 Sep 2026
The site was rebuilt from scratch on the rat-in-crosshair brand and is LIVE at https://djpest.com.au (Cloudflare Pages project `djpest`).
**All HTML in the repo root is now GENERATED. Do not hand-edit any .html file.** Edits go in `build/pages/*.py`; run `python3 build/build.py`; it refuses to build if the compliance scanner finds forbidden claims (see `build/build.py` FORBIDDEN and the brief in git history). Deploy with `./deploy.sh` (preview) or `./deploy.sh --prod`.

Pages that exist (29): home, /services + 7 service pages, /service-areas + 8 suburbs (warwick, greenwood, duncraig, sorrento, hillarys, joondalup, wanneroo, balcatta), /pest-control-prices-perth, /whats-my-pest, /about, /contact, /terms, /warranty, /privacy, /blog + 2 posts, /404.

## Facts policy (hard)
Only facts in `build/site.json` and the T&Cs. No founding year, no "25 years", no "1,000+ homes", no insurance dollar figures, no reviews or ratings until real ones exist, never name the father's business. Prices are indicative ranges labelled as such.

## Next tasks (priority order)
1. **Tier-1 suburb pages not yet built** (add to `build/pages/20_suburbs.py`, same structure as existing entries, 700–1,000 unique words each): Marangaroo, Stirling, Kingsley, Woodvale, Padbury, Carine, Karrinyup, Hamersley.
2. **BOFU service gaps** (add to `build/pages/10_services.py`): /wasp-removal-perth, /bee-removal-perth (relocation, licensed beekeeper referral), /flea-treatment-perth, /bed-bug-treatment-perth, /commercial-pest-control-perth (strata, food businesses, property managers).
3. **MOFU cost articles** as blog posts in `build/pages/30_company.py` (BlogPosting schema): "termite treatment cost perth", "exterminator cost", "how much does a termite inspection cost".
4. **Blog backlog**: convert one bundle per day from `blog/_drafts/` via the content-pipeline skill into a generator page (never publish more than one per day).
5. Add each new page to the footer/nav only if it is a top-level service.

Always: build clean, screenshot at 1280 and 390 with Playwright, commit, push, `./deploy.sh --prod`.
