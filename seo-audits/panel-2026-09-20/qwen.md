1. FIRST-GLANCE VERDICT
A stressed homeowner at 9pm with rats in the roof lands on a dark, high-contrast mobile site that immediately validates their panic ("Rats in the roof tonight?") and offers a frictionless, sticky click-to-call button. They will call because the copy projects extreme competence, transparent pricing, and a documented "accountant-run" methodology that eliminates the typical tradesman anxiety. The immediate visibility of the "pending" registration status might cause a micro-hesitation, but the overwhelming E-E-A-T signals and itemised pricing will win the conversion.

2. TOP 10 CHANGES
**1. Rodent Page Hero: Scrub the licence number**
*What is wrong:* The hero section lists "- WA licence 13914". This directly violates the hard constraint "never a licence number" and WA DoH advertising rules for provisional/supervised setups.
*Precise fix:* Replace with "- Licensed technicians (WA DoH supervised)". [confidence: high]

**2. Home Page Sample Report & Terms: Scrub technician names/numbers**
*What is wrong:* The sample report table says "Technician name and licence number recorded." The Terms say "Licence numbers appear on every treatment record." This violates the "NO personal names" and "never a licence number" constraints.
*Precise fix:* Change to "Technician ID and provisional licence status recorded." Update Terms 1.2 to match. [confidence: high]

**3. About Page & Meta: Fix the "Since 2011" ACL trap**
*What is wrong:* Meta and H1 claim "A Perth family pest control business since 2011", but the About page admits "DJ Pest was formed in 2026". Under the Australian Consumer Law, a new entity cannot claim the trading history of a previous entity without explicit clarification, risking a misleading conduct complaint from competitors.
*Precise fix:* Change H1/Meta to "Family-run Perth pest control | Second generation since 2011". Change About H1 to "Our family has worked in Perth pest control since 2011. DJ Pest is the second-generation evolution, established in 2026." [confidence: high, verify ACCC guidance on business history claims]

**4. Pricing Guide: Inject `PriceSpecification` JSON-LD for AI**
*What is wrong:* The page uses an `OfferCatalog` schema array but lacks the explicit `PriceSpecification` markup needed for AI engines to parse and cite "how much does pest control cost Perth".
*Precise fix:* Wrap every table row in JSON-LD `Offer` with `priceSpecification`: `{"@type": "PriceSpecification", "minPrice": "250", "maxPrice": "350", "priceCurrency": "AUD"}`. [confidence: high]

**5. Services Hub: Move the Treatment Report visual above the fold**
*What is wrong:* The "DJ Pest treatment report" mockup is buried halfway down the Home page and missing from the Services Hub. This is your strongest conversion asset against competitors who hand over one-line receipts.
*Precise fix:* Move the 3-part report visual (Entry audit, Chemical ledger, Prevention plan) to the Services Hub hero section, immediately below the primary CTA. [confidence: high]

**6. What's My Pest: Optimise H3s for exact-match AI queries**
*What is wrong:* "Bitten in the yard after five" is great copy, but AI answer engines look for exact semantic matches like "what is biting me at dusk in Perth".
*Precise fix:* Change the H3 to "What is biting me at dusk in Perth? (Mosquitoes & Midges)". Add an `FAQPage` schema block specifically targeting this long-tail query. [confidence: high]

**7. Global Schema: Add explicit `areaServed` postcodes**
*What is wrong:* The `LocalBusiness` schema lacks the granular postal code arrays required to dominate the local map pack for "northern suburbs" vs general Perth.
*Precise fix:* In the `LocalBusiness` JSON-LD, add `"areaServed": [{"@type": "GeoCircle", ...}, {"@type": "PostalCode", "postalCode": "6024"}, ...]` listing all 30+ target postcodes. [confidence: high]

**8. Suburb Pages (e.g., Duncraig): Add hyper-local landmark schema**
*What is wrong:* The copy brilliantly mentions Carine Regional Open Space and Percy Doyle Reserve, but the schema ignores them, missing a chance to build a local relevance graph for Google.
*Precise fix:* Add `LandmarksOrHistoricalBuildings` or `CivicStructure` schema referencing these specific locations in the suburb page JSON-LD. [confidence: medium]

**9. About Page / FAQ: Clarify provisional supervision**
*What is wrong:* "Every treatment is carried out by a technician licensed under the WA Health (Pesticides) Regulations 2011" implies full licensing. If the tech is provisional, r.13 requires direct supervision by a fully licensed PMT.
*Precise fix:* Change to "Treatments are carried out by a provisional technician under the direct supervision of a fully licensed Pest Management Technician, in accordance with r.13 of the Health (Pesticides) Regulations 2011 (WA)." [confidence: medium, verify WA DoH r.13 supervisory definitions]

**10. Commercial Page: Add an EHO/HACCP lead magnet**
*What is wrong:* B2B strata and cafe managers need compliance proof before calling. The page lists what you do, but doesn't capture leads who aren't ready to buy today.
*Precise fix:* Add a "Download our Free EHO/HACCP Pest Compliance Checklist" email capture form to build a B2B nurture list. [confidence: medium]

3. WHAT IS ALREADY WORLD-CLASS
* **The "Accountant" Positioning:** Framing the business as run by a CA who hates hidden fees is a masterstroke. It turns a lack of flashy marketing into a massive trust signal (itemised quotes, ledgers, no deposits).
* **Treatment Report Mockup:** Showing the exact 3-part report (Entry audit, Chemical ledger, Prevention plan) completely demystifies the service and sets a barrier to entry for competitors.
* **Suburb-Specific Geography:** The Duncraig page mentions Spearwood sand, Tamala limestone, and specific reserves. This is elite local SEO and proves actual E-E-A-T to both humans and LLMs.
* **llms.txt Implementation:** Having a dedicated, well-structured `llms.txt` file is cutting-edge for AI answer-engine optimisation.
* **Pest Calendar:** Tying pests to Perth's specific seasons (e.g., coastal brown ants in spring, rodents in winter) is highly actionable and locally relevant.

4. LOCAL SEO GAPS
* **Google Business Profile (GBP):** The site has no GBP yet. Competitors (Flick, Rentokil, Jim's) have hundreds of reviews. *Achievable fix:* The moment the DoH certificate issues, verify the GBP, seed it with the 8 suburb pages as "service areas", and use the "treatment report" as a "product" or "update" post to build initial signals.
* **Local Backlinks / Citations:** Missing mentions in local northern suburbs community groups or business directories (e.g., Joondalup Chamber of Commerce). *Achievable fix:* Join the local chamber and get a citation.
* **Visual Proof:** Zero photos of real jobs. *Achievable fix:* Start taking macro photos of pest harbourages, entry points, and station placements (no client faces/houses) to build a proprietary image library that Google Vision can index.

5. AI/ANSWER-ENGINE CITATION
* **Structure:** AI engines heavily weight `FAQPage` schema. Ensure every H2/H3 on the "What's my pest" and "Pricing" pages is wrapped in `FAQPage` JSON-LD, not just plain text.
* **Wording:** AI looks for direct, concise answers. Add a "TL;DR" paragraph at the very top of the Pricing Guide: *"In Perth, general pest control typically costs $250–$350, while termite inspections range from $250–$350 and treatments from $2,500–$5,500."*
* **Data:** AI loves tables. Ensure the pricing tables use strict semantic HTML (`<table>`, `<th>`, `<td>`) rather than CSS grid divs, so parsers can easily extract the min/max ranges.
* **Schema:** Add `HowTo` schema for "How to prepare for a pest control treatment" on the service pages to capture preparatory queries.

6. TRUST WITHOUT A NAME
Since the owner is anonymous and there are no reviews yet, deploy these lawful trust signals:
1. **The "Accountant" Persona:** Implies financial probity, record-keeping, and no cash-in-hand dodginess.
2. **The Treatment Report Sample:** Proves competence and transparency before the sale.
3. **APVMA & AS Standards:** Repeatedly citing AS 4349.3, AS 3660.2, and APVMA labels shows regulatory mastery.
4. **Transparent Pricing:** Publishing prices upfront eliminates the "tradesman rip-off" fear.
5. **Public Liability Insurance:** Mentioning it and offering to provide a certificate on request builds B2B/B2C trust.
6. **Provisional Licence Transparency:** Explaining *exactly* how the provisional licence works under supervision shows radical honesty.
7. **Itemised Invoicing:** "No call-out fee, no deposit, seven-day terms" is a massive trust signal for a new business.

7. CONTENT ACCURACY
* **Drywood Termites (What's My Pest page):** The text says "Borers or drywood termites leave pellets... Either way it needs a timber pest inspection". *Correction:* The West Indian drywood termite (*Cryptotermes cynocephalus*) is a declared/notifiable quarantine pest in WA. If suspected, the technician *must* notify DPIRD/DoH immediately; they cannot just "inspect and treat" it under a standard contract. [confidence: high, verify with DPIRD WA declared pest list]
* **Record Keeping:** "kept for three years as WA law requires". Health (Pesticides) Regulations 2011 (WA) r.59 requires records to be kept for 3 years. Correct. [confidence: high]
* **Cooling-off period:** Terms say "10 business days" for unsolicited consumer agreements. Under ACL s.82, the cooling-off period is indeed 10 business days. Correct. [confidence: high]
* **European Wasps:** Correctly identified as a DPIRD reportable pest, not to be treated by the operator. [confidence: high]

8. MISSING PAGES OR FEATURES
* **"How to Prepare" Page:** A dedicated, printable page for customers on what to do before the tech arrives (move furniture, cover fish tanks, vacate pets).
* **Visual Pest Gallery:** High-res, macro photos of the specific pests (coastal brown ant vs black ant, rat vs mouse droppings) to aid the "What's my pest" tool.
* **Case Studies / "Job Logs":** Since there are no reviews, publish anonymised "Job Logs" (e.g., "How we solved a coastal brown ant super-colony in Sorrento") showing the problem, the ledger, and the result.
* **Strata/Property Manager Portal:** A dedicated page or login for property managers to access treatment records and compliance certificates for their portfolios.

9. THREE THINGS TO DELETE
1. **"WA licence 13914" (Rodent Page Hero):** Hard constraint violation. Delete immediately.
2. **"Technician name and licence number recorded" (Home Sample Report & Terms):** Hard constraint violation (no personal names, no licence numbers). Delete/replace with "Technician ID".
3. **The phrase "A Perth family pest control business since 2011" (Home Meta/H1):** Risks ACL misleading conduct claims since DJ Pest was formed in 2026. Delete or rephrase to focus on the *family's* history, not the *business entity's* history.

10. ONE-PARAGRAPH SUMMARY
DJ Pest’s website is an exceptional piece of conversion-focused, E-E-A-T-driven design that brilliantly leverages the "Chartered Accountant" positioning to solve the trust deficit in the trades industry. To make it truly world-class and legally bulletproof, you must immediately scrub the hard-constraint violations (the specific licence number and technician name references), clarify the "since 2011" vs "formed in 2026" timeline to satisfy the ACL, and inject explicit `PriceSpecification` and `FAQPage` JSON-LD schema to dominate AI answer engines. Once the DoH certificate issues and the Google Business Profile goes live, the site’s hyper-local suburb geography, transparent pricing, and "treatment report" mockups will effortlessly outconvert the generic, review-reliant pages of national competitors like Flick and Rentokil.