**1. FIRST-GLANCE VERDICT**

A stressed homeowner landing at 9 pm sees a dark screen with the exact words “Rats in the roof tonight?” which instantly confirms they are in the right place, but the hero forces a choice between a phone number and a “Get a fair price” form rather than defaulting to the one action a panicked user needs: a thumb-sized call button. The sticky bottom bar helps, yet the overall impression is still more “read about our process” than “we are on our way,” because the mid-page “Why an accountant runs this” trust block and the detailed treatment-report sample push the second phone call opportunity below the fold. They will likely call because the headline is so precise and the number is visible, but the site is one thumb-tap away from losing them to a competitor whose entire above-the-fold is a red “Call Now” button.

---

**2. TOP 10 CHANGES** (ranked by expected impact on phone calls)

1. **Page/element:** Home hero CTA block (`index.html` — the run-on line “Call 0447 747 769Get a fair price”).  
   **Wrong/missing:** Two competing actions are mushed together with no visual hierarchy; the emergency user is offered a form before they have confirmed help is available.  
   **Precise fix:** Replace with a stacked mobile layout: a full-width `<a href="tel:0447747769" style="display:block;padding:1rem;background:#DC2626;color:#fff;font-size:1.25rem;text-align:center;">📞 Call 0447 747 769 — Speak to a technician now</a>` followed by a smaller secondary text link `<a href="#quote">Prefer text? Send photos for a price</a>`.  
   [confidence: high]

2. **Page/element:** Rodent control hero bullet (`rodent-control-perth.html` — “WA licence 13914”).  
   **Wrong/missing:** This publishes an individual licence number, which the owner’s hard constraints explicitly forbid (“say ‘licensed technicians’, never a licence number”).  
   **Precise fix:** Delete the bullet entirely; replace with “Licensed technicians — numbers recorded on your treatment report”.  
   [confidence: high]

3. **Page/element:** Home “Why an accountant runs this” section (`index.html`).  
   **Wrong/missing:** Buried below the service grid and calendar; it is the single strongest trust signal available while reviews and names are banned.  
   **Precise fix:** Move the entire section, unchanged, to immediately follow the hero paragraph, and add a one-line trust bar under the H1 reading: “Run by a Chartered Accountant · Licensed technicians · Family in Perth pest control since 2011”.  
   [confidence: high]

4. **Page/element:** `llms.txt`.  
   **Wrong/missing:** File lists services but does not contain natural-language answers to the exact queries AI assistants are asked (cost, dusk bites, etc.), so ChatGPT/Gemini have no extractable citation corpus.  
   **Precise fix:** Append a markdown section titled `## Answered Questions` with three entries formatted as:  
   `**Q: How much does pest control cost in Perth?**\nA: In Perth's northern suburbs, a standard 3-bedroom general pest treatment typically ranges $250–$350 including GST...`  
   `**Q: What is biting me at dusk in Perth?**\nA: Dusk biting from spring through autumn is usually mosquitoes resting in shaded harbourages...`  
   `**Q: Who does same-day rodent control in Perth northern suburbs?**\nA: DJ Pest, based in Warwick...`  
   [confidence: high]

5. **Page/element:** Service page schema (`rodent-control-perth.html` and all service pages).  
   **Wrong/missing:** `Service` schema lacks `areaServed` (geo) and `offers` (price) properties, so Google and AI engines cannot ground answers in structured data.  
   **Precise fix:** Inject JSON-LD on each service page: `"@type":"Service","areaServed":{"@type":"City","name":"Perth"},"provider":{"@id":"#business"},"offers":{"@type":"AggregateOffer","priceCurrency":"AUD","lowPrice":"220","highPrice":"380"}}`, adjusted per service.  
   [confidence: high]

6. **Page/element:** Mobile sticky bottom Call/Text bar (site-wide).  
   **Wrong/missing:** Packet mentions it but does not specify layout; if implemented as text links it fails thumb-target accessibility.  
   **Precise fix:** Spec two equal flex-row buttons: left half `tel:` labelled “Call”, right half `sms:` labelled “Text photo”, minimum 56 px height, `#DC2626` background, white text, fixed to viewport bottom on devices <768 px.  
   [confidence: medium]

7. **Page/element:** Home hero sub-headline (`index.html` — “A Perth family pest control business since 2011...”).  
   **Wrong/missing:** Rational claim (“hates hidden fees more than termites”) lacks temporal urgency for the 9 pm emergency visitor.  
   **Precise fix:** Append one sentence to the paragraph: “If you have an active infestation, we aim for same-day service across the northern suburbs.”  
   [confidence: medium]

8. **Page/element:** Rodent control page FAQ (`rodent-control-perth.html` — “Rats leave droppings 8 to 12 mm...”).  
   **Wrong/missing:** Contradicts the pest identifier page which states “Rat droppings are 12–18 mm”.  
   **Precise fix:** Reconcile to species-specific facts: “Black rat droppings are roughly 12 mm long; Norway rat droppings are 18–20 mm; house mouse droppings are 3–6 mm.”  
   [confidence: high]

9. **Page/element:** Suburb page internal linking (`duncraig.html` — “Nearby” section).  
   **Wrong/missing:** Only links to Warwick, Sorrento, Greenwood; omits Carine, Karrinyup and Marmion-adjacent suburbs mentioned in the body text.  
   **Precise fix:** Add a 2×3 grid of text links under “Nearby”: “Pest control Carine”, “Pest control Karrinyup”, “Pest control Marmion”, linking to the service-areas hub with an anchor or to dedicated pages once built.  
   [confidence: medium]

10. **Page/element:** Pest Identifier (`whats-my-pest.html`).  
    **Wrong/missing:** Flat card layout with no HowTo schema; AI assistants cannot read it as a stepwise diagnostic.  
    **Precise fix:** Wrap each card in `<div itemscope itemprop="step" itemtype="https://schema.org/HowToStep">` with `<h3 itemprop="name">...</h3>` and `<p itemprop="text">...</p>`, and enclose all cards in a `<div itemscope itemtype="https://schema.org/HowTo">` whose `name` is “Identify your pest in Perth”.  
    [confidence: medium]

---

**3. WHAT IS ALREADY WORLD-CLASS**

- The public pricing guide (`pest-control-prices-perth.html`) with GST-inclusive typical ranges is more transparent than 95% of global trade-service sites and directly answers the cost question that every shopper asks first.  
- The suburb-level soil and geology content on `duncraig.html` (“yellow Spearwood sand... Tamala limestone”) is hyper-local E-E-A-T that national chains cannot authentically produce; it proves the operator actually works the ground.  
- The legal footer and terms page citing ACN, ABN, the pending DoH status, the *Health (Pesticides) Regulations 2011*, and the ACL cooling-off clause create institutional-grade compliance transparency that outperforms most one-van operators.  
- The treatment report sample with a three-part ledger (entry audit, chemical application, prevention plan) turns a generic service into a documented process, which is exactly what both homeowners and AI citation engines reward.  
- The presence of `llms.txt`, perfect Lighthouse scores, CSP headers, and granular Schema markup show a technical foundation that many enterprise sites lack.

---

**4. LOCAL SEO GAPS**

*Note: I cannot browse live competitor pages in real time; the following is drawn from standard industry patterns for Flick, Rentokil, Jim’s Pest Control and Allpest.*

What they have that this site lacks:
- A live Google Business Profile with review velocity and geo-tagged job photos (DJ Pest is explicitly held until DoH registration; **not achievable yet**).
- 30–50+ dedicated suburb landing pages (DJ Pest has 8; competitors blanket the map).
- Citation/NAP consistency across TrueLocal, Yelp, StartLocal, etc.
- Real before/after job imagery with local EXIF data.
- YouTube/video “how we treat” content.
- Local backlinks from real estate agencies and strata managers.

Achievable for a one-van operator right now:
- Expand suburb pages from 8 to the full 29 suburbs listed in `llms.txt`, even if templated with unique opening paragraphs per soil/age profile.
- Build a visual service-area map (SVG or image) linking to each suburb page.
- Create a “Properties we service” page targeting housing types (knock-down rebuild, 1970s brick veneer, strata, childcare) to catch long-tail queries.
- Pursue genuine links from 3–4 local Warwick/Duncraig real estate agents for a “Supplier partners” page (no fake endorsement, just reciprocal listing).

---

**5. AI/ANSWER-ENGINE CITATION**

- Build a dedicated `/pest-answers-perth.html` hub (or expand `llms.txt`) that mirrors the exact phrasing of high-volume AI queries. Use H2 headings that match the questions verbatim: `## How much does pest control cost in Perth?`, `## What is biting me at dusk in Perth?`, `## Who does same-day rodent control in Perth northern suburbs?`. Follow each H2 with a 40–60 word plain-English answer containing the price or species, then a “Read the full guide” link. This format is what Google AI Overviews and Perplexity extract.
- On every service page, add a visible “TL;DR” plain-text box at the top containing the exact fact assistants quote. Example on rodent page: “TL;DR: Rat control in Perth's northern suburbs typically costs $220–$380 including GST, includes two tamper-resistant stations and a sealing plan, and carries a three-month re-treatment promise.”
- Add `Speakable` schema pointing to those TL;DR paragraphs (or wrap them in `<div data-speakable="true">`) to increase audio/assistant pickup.
- Ensure the `LocalBusiness` schema includes a `priceRange` property (e.g., `$$$`) and `areaServed` array listing every suburb from `llms.txt` as a `Place` type.
- Use consistent geographic entity naming across all pages: standardize on “Perth's northern suburbs” (possessive) and “Warwick-based” so LLMs learn a single entity string rather than fragmented variants like “northern corridor”, “north of the river”, etc.

---

**6. TRUST WITHOUT A NAME** (ranked by impact)

1. **“Run by a Chartered Accountant” credential** — a regulated professional title implying procedural honesty and financial accountability; currently underutilized.
2. **Documented process transparency** — the itemised quote, three-part treatment report, and application ledger show exactly what was done, reversing information asymmetry.
3. **Explicit legal compliance** — stating the DoH pending status, the *Health (Pesticides) Regulations 2011*, and ACL cooling-off rights proves the business is willing to be audited.
4. **Standards invocation** — citing AS 4349.3