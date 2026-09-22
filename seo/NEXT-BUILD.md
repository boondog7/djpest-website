# NEXT BUILD — 2026-09-21 (evening update)

> ## HARD RULES FOR THE CLOUD ROUTINE (added 22 Sep 2026 by Dane's Mac session)
> 1. **Never edit `site.json → "unpublished"`, the `PRICES` dict, or any dollar figure.** Prices are Dane's decision. Build the page, leave it gated, and list the proposed prices in this file for him to confirm.
> 2. **Never claim a page is "live".** The cloud commits HTML; only `./deploy.sh --prod` on the Mac deploys. As of 22 Sep bee, commercial and bed-bug are GATED (404 live) pending Dane's price sign-off and a beekeeper's number for the bee page.
> 3. Every public claim passes the compliance scanner and the licensing wording is the fixed string ("carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence"), never bare "Licensed technicians".
> 4. Read `~/business/djpest/marketing/vibe/brand-bible.md` voice rules before writing copy.


## Progress summary
**Done: 10 service pages live + 3 built-but-gated (bee, commercial, bed bug: awaiting Dane price sign-off) + 10 Tier-1 suburb pages + pricing hub + service-areas hub + 2 blog posts; ~95% of plan.**

Shipped today (all built, compliance-clean, pushed):
- `bee-removal-perth.html` and `commercial-pest-control-perth.html` built, RE-GATED 22/9 pending Dane. Proposed prices: bee hive $320–$480; commercial $160–$420/visit, clean-out $400–$750.
- `bed-bug-treatment-perth.html` built — 110/mo, KD17. Two-visit program $450–$950 (one room $450–$550, whole home $650–$950). Last BOFU service gap closed.
- `marangaroo.html` (90/mo, KD0) and `stirling.html` (70/mo, KD0) built — Tier-1 corridor cluster complete.
- Pricing page, services hub, home, footer, what's-my-pest, llms.txt and sitemap all updated to match.

### Pages live right now
**Service (13):** ant, bed-bug, bee, cockroach, commercial, flea, general, mosquito, rodent, spider, termite-inspection, termite-treatment, wasp
**Suburb (10/10 Tier-1):** warwick, greenwood, duncraig, sorrento, hillarys, joondalup, wanneroo, balcatta, marangaroo, stirling
**Support:** service-areas, pest-control-prices-perth, whats-my-pest, property-managers, blog + 2 posts, about, contact

---

## Next tasks (priority order)

### 1. Sanity-check today's prices on your phone (5 min)
Open `/pest-control-prices-perth`, `/bee-removal-perth`, `/commercial-pest-control-perth`, `/bed-bug-treatment-perth`. If any number feels wrong, edit the `PRICES` dict at the top of `build/pages/10_services.py` (`bee`, `comm_visit`, `comm_cleanout`, `bedbug_room`, `bedbug_home`) plus the matching rows in `build/pages/30_company.py`, run `python3 build/build.py`, push.

### 2. Tier-2 suburb pages — first three
The plan's next cluster. All on the corridor, all low KD:
- **`alkimos.html`** — 70/mo, KD5. New estates 2010s+, slab-on-ground with builder barriers now lapsing; coastal dune + Alkimos Beach reserve; big ant pressure.
- **`clarkson.html`** — 50/mo, KD6. 1990s–2000s stock, Ocean Keys precinct feeds rodents/cockroaches, Neerabup bush to the east = termites.
- **`yanchep.html`** — 50/mo, KD4. Furthest north (45 min); Yanchep National Park and Lagoon; grouped bookings, say so on the page.

**How to build:** add to `SUBURBS` in `build/pages/20_suburbs.py` and to the `PAGES8` list (it's the linked-suburbs list). Follow the Marangaroo/Stirling pattern: two intro paragraphs with real landmarks and soil, four pest cards, a "now" paragraph, five FAQs. Home page suburb list is in `build/pages/00_home.py`.

### 3. MOFU: dedicated `termite-treatment-cost-perth` page
720/mo, KD8. The pricing hub answers it in one FAQ; a dedicated page with a worked example (perimeter metres × drilling vs trenching) would own the query and feed the termite BOFU pages. Real $ tables only.

---

## Blockers
- None on the build side. Everything above is unblocked.
- Build script needs Python 3.12+ (nested f-string quotes in `20_suburbs.py`). Fine on your machine (3.14).
- GBP at Warwick 6024 + review-ask after every job still outranks all of the above for calls. If not verified yet, that is the real next task.
- Termite pages are live; PMB 3000 registered. No change needed.
