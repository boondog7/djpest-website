# NEXT BUILD — 2026-09-19

## Progress summary
**Done: 12 service pages (incl. 2 termite) + 8 suburb pages + pricing hub + service-areas; ~85% of plan.**
Built today (Claude, this session): `/wasp-removal-perth`, `/bee-removal-perth`, `/commercial-pest-control-perth` — each ~2,200–2,400 words, full @graph schema (LocalBusiness → Service/Offer → FAQPage → BreadcrumbList), season module, pricing table, 8–9 FAQs. Wired into footer nav (all 35 pages), services hub, homepage grid, pricing guide, What's-my-pest, sitemap. Zero broken links. Rendered clean at 390px and 1280px.

### Pages built so far
**Service (12):** ant, cockroach, flea, general, mosquito, rodent, spider, termite-inspection, termite-treatment, **wasp, bee, commercial**  
**Suburb (8):** warwick, greenwood, duncraig, sorrento, hillarys, joondalup, wanneroo, balcatta  
**Support:** service-areas, pest-control-prices-perth, whats-my-pest, blog + 2 posts, about, contact, property-managers

---

## ⚠️ Dane — three things before you deploy today's pages

### 1. Confirm the prices I set (I had no data for these — they are my estimates)
- **Bee hive treatment: $250–$400** (on bee page, pricing guide row, Service schema)
- **Commercial per-visit ranges: $140–$380**, one-off kitchen clean-out **$350–$650** (commercial page table + schema)
- Wasp $180–$280 was already in your pricing guide — unchanged.
Change the numbers in the HTML if wrong; they appear in the table, the FAQ answer and the JSON-LD `priceSpecification` on each page.

### 2. Port the three pages into the generator or they will be orphaned
`build/` is gitignored, so the three pages were hand-built to match the generator's output byte-for-byte. Your next `python3 build/build.py` will regenerate `services.html`, `index.html`, footers and `sitemap.xml` **without** the new links unless the pages exist in `build/pages/10_services.py`. The page HTML files themselves will survive.

**Strongly recommended:** remove `build/` from `.gitignore` and commit the generator. Right now the source of truth for a 35-page site lives only on your laptop, and the daily build coach can't use it.

### 3. Beekeeper referral contact
The bee page says we refer swarms to a registered WA beekeeper and mentions the WA Apiarists' Society swarm list. Have a name/number ready before the first call.

---

## Facts I built in — worth a 2-minute check
- **European wasps are not established in WA**; DPIRD runs surveillance/eradication and destroys confirmed nests. Report via MyPestGuide Reporter or PaDIS. The wasp page and pricing guide now say we *report* rather than treat suspected European wasps. (The old pricing-guide row said "European or paper wasp" — corrected.)
- Commercial page cites **Food Act 2008 (WA)** and **Food Standards Code 3.2.2** (pest clause). Re-entry, HACCP folder, strata council-of-owners responsibility. Nothing about licence status beyond what is already in the footer.

---

## Next tasks (priority order)

### 1. `/bed-bug-treatment-perth.html` — 110 searches/mo, KD17
Last BOFU service gap. Warranty page already lists "Bed bugs: 30 days, two-visit plan" — page must match. Angle: heat + residual, two visits, mattress-edge ID, no "one spray fixes it" claims. Add to `build/pages/10_services.py`.

### 2. Suburb pages: `/marangaroo` (90/mo, KD0) and `/stirling` (70/mo, KD0)
Last two Tier-1 suburbs with no page. Both already in schema `areaServed` and the form dropdown. Marangaroo: Marangaroo Golf Course/Lake Goollelal fringe → mosquitoes, ants. Stirling: Lake Gwelup/Stirling Civic Gardens, older 60s–70s brick → termites, rodents.

### 3. MOFU cost posts (the moat)
- "termite treatment cost perth" (720/mo, KD8) — pull ranges from `/termite-treatment-perth` table
- "exterminator cost perth" (1000/mo, KD11) — pull from `/pest-control-prices-perth`
Drafts in `blog/_drafts/` for 01/12/23 (cost) can be merged.

---

## The bit no page can fix
Battle plan consensus: the website is already ahead of every competitor. **Google Business Profile at Warwick 6024 + a review-ask after every job + NAP citations (TrueLocal, Yellow Pages, Hipages, Oneflare, Yelp AU, StartLocal)** is what puts you in the map pack and gets the phone ringing. If GBP isn't verified and live yet, that beats building page 13.

## Blockers
None. Termite licence confirmed (PMB 3000 + Licence 13914 in schema). Deploy: `./deploy.sh --prod` (after porting pages into the generator, see above).
