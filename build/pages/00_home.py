"""Home page."""

def pages(c):
    S = c["SITE"]; esc = c["esc"]; icon = c["icon"]
    hero_art = f"""<div class="hero-art" aria-hidden="true">
<svg class="crosshair" viewBox="0 0 400 400">
  <circle class="ring" cx="200" cy="200" r="150"/>
  <line class="tick" x1="200" y1="20" x2="200" y2="66"/><line class="tick" x1="200" y1="334" x2="200" y2="380"/>
  <line class="tick" x1="20" y1="200" x2="66" y2="200"/><line class="tick" x1="334" y1="200" x2="380" y2="200"/>
  <image class="rat" href="/assets/img/rat-crosshair-white.png" x="70" y="72" width="260" height="256"/>
</svg></div>"""

    hero = f"""<section class="hero"><div class="wrap">
<div>
  {c['eyebrow']("Perth's northern suburbs · Warwick-based · Family-run since 2011")}
  <h1>Rats in the roof tonight?<br>We fix it <em class="red">properly</em>, and put it in writing.</h1>
  <p class="lead">Local pest control for Perth's northern suburbs, based in Warwick. Same-day for active rats, mice, ants and spiders where the run allows, with the price in writing before we start and a treatment record after.</p>
  <div class="actions">{c['btn_call']()}{c['btn_quote']()}</div>{c['hours_cue']()}
  <ul class="trust"><li>Licensed technicians</li><li>In Perth pest control since {S['family_since']}</li><li>Public liability insured</li><li>Same-day for active pests</li></ul>
</div>
{hero_art}
</div></section>"""

    services = c["section"](
        c["eyebrow"]("What we treat") +
        '<div class="section-head"><h2>Twelve jobs, one standard of care.</h2><p class="lead">Diagnosed first, treated with the right chemistry for the pest and the site, then documented. Every product is APVMA-registered and applied to its label.</p></div>' +
        '<div class="grid grid-3">' +
        c["card"]("Termite inspection", "A full AS 4349.3 timber pest inspection with photos, moisture readings and a written report you can act on.", "/termite-inspection-perth", "01 / Termites") +
        c["card"]("Termite treatment", "Non-repellent chemical management systems installed to AS 3660.2, or baiting where that suits the site better.", "/termite-treatment-perth", "02 / Termites") +
        c["card"]("General pest treatment", "Cockroaches, spiders, silverfish and ants in one internal and external treatment. Six-month re-treatment promise.", "/general-pest-control-perth", "03 / General") +
        c["card"]("Ant control", "Coastal brown ant super-colonies need slow-acting non-repellents and baits, not a quick spray. We treat the colony.", "/ant-control-perth", "04 / Ants") +
        c["card"]("Cockroach control", "German cockroaches in the kitchen or Australian cockroaches from the garden. Gel baits, IGRs and non-staining products indoors.", "/cockroach-control-perth", "05 / Cockroaches") +
        c["card"]("Rodent control", "Species identified, entry points found, tamper-resistant stations placed and a sealing plan so they don't come back.", "/rodent-control-perth", "06 / Rodents") +
        c["card"]("Spider control", "Redbacks, white-tails and huntsmen. External web-and-harbourage treatment with the internal spray only where it's needed.", "/spider-control-perth", "07 / Spiders") +
        c["card"]("Mosquito control", "Breeding-site audit first, then a residual treatment of the shaded harbourages where adults rest. Timed for Perth's warm-season peak.", "/mosquito-control-perth", "08 / Mosquitoes") +
        c["card"]("Vacate flea treatment", "Moving out with a pet? Quoted from the address within the hour, certificate to you and your agent within the hour of treatment.", "/flea-treatment-perth", "09 / Fleas") +
        c["card"]("Wasp removal", "Paper wasp nests under eaves and pergolas found, treated and removed, usually same day. Suspected European wasps are reported to DPIRD.", "/wasp-removal-perth", "10 / Wasps") +
        c["card"]("Bee removal", "Swarms go to a beekeeper alive. Hives in walls and roof voids are treated in the evening, sealed, and you get a comb-removal and proofing plan.", "/bee-removal-perth", "11 / Bees") +
        c["card"]("Commercial pest control", "Cafes, strata, childcare and warehouses on a documented program: numbered stations, same-day reports, a folder your auditor can read.", "/commercial-pest-control-perth", "12 / Commercial") +
        '</div>', "ledger")

    ca = c["section"](
        '<div class="grid grid-2" style="align-items:center;gap:3rem">'
        '<div>' + c["eyebrow"]("Why an accountant runs this") +
        '<h2>Most pest companies are run by exterminators. This one is run by a Chartered Accountant.</h2>'
        '<p class="lead">Our family has been in Perth pest control since 2011. DJ Pest is the second generation, run by a Chartered Accountant, and that shapes how it works: itemised quotes, a chemical application ledger for every job, and a re-treatment promise you can read in full before you book.</p>'
        '<p><a class="btn btn-ghost" href="/about">About DJ Pest ' + icon("arrow", "icon") + '</a></p></div>'
        '<div class="grid" style="gap:.8rem">'
        + c["card"]("Priced in writing before we start", "No call-out fee, no deposit, no surprises on the invoice. Seven-day terms.")
        + c["card"]("A record of every treatment", "Product, active constituent, rate, areas treated and re-entry period, kept for three years as WA law requires and given to you.")
        + c["card"]("A promise, not a slogan", "If the pest we treated comes back inside the period on your invoice, we come back at no charge. <a href=\"/warranty\">Read the terms</a>.")
        + '</div></div>')

    report = c["section"](
        c["eyebrow"]("The DJ Pest treatment report") +
        '<div class="report"><div>'
        '<h2>You get the paperwork nobody else gives you.</h2>'
        '<p class="lead">After every job you receive a report with three parts: where the pests were getting in, exactly what was applied and where, and what to fix so they stay out. It doubles as the treatment record WA regulations require us to keep.</p>'
        '<div class="report-tabs" role="tablist">'
        '<button role="tab" aria-selected="true" data-tab="entry">1. Entry audit</button>'
        '<button role="tab" aria-selected="false" data-tab="ledger">2. Application ledger</button>'
        '<button role="tab" aria-selected="false" data-tab="plan">3. Prevention plan</button></div>'
        '<p class="notice">Sample only. Details vary by job.</p></div>'
        '<div class="report-doc" aria-live="polite">'
        '<div class="doc-head"><img src="/assets/img/logo-black.png" alt="DJ Pest" width="900" height="392" loading="lazy"><span>Treatment report · sample</span></div>'
        '<div data-pane="entry"><h3>Point-of-entry audit</h3><table><tr><th>Location</th><th>Finding</th><th>Photo</th></tr>'
        '<tr><td>Roof void, NE corner</td><td>Rat droppings, gnawed sarking, gap at eave</td><td>#04</td></tr>'
        '<tr><td>Meter box</td><td>Conduit entry unsealed (20 mm)</td><td>#07</td></tr>'
        '<tr><td>Rear patio</td><td>Coastal brown ant trail to kitchen kickboard</td><td>#11</td></tr></table></div>'
        '<div data-pane="ledger" hidden><h3>Chemical application ledger</h3><table><tr><th>Product</th><th>Active</th><th>Rate</th><th>Where</th></tr>'
        '<tr><td>Non-repellent liquid (APVMA-registered)</td><td>Fipronil</td><td>Per label</td><td>External perimeter, ant trails</td></tr>'
        '<tr><td>Rodenticide block in tamper-resistant station</td><td>Per label</td><td>2 stations</td><td>Roof void, side path</td></tr>'
        '<tr><td>Non-staining dust</td><td>Per label</td><td>Light</td><td>Wall voids, kickboards</td></tr></table>'
        '<p style="font-size:.75rem;color:#555;margin:.6rem 0 0">Re-entry: 2 hours after surfaces dry. Technician name and licence number recorded.</p></div>'
        '<div data-pane="plan" hidden><h3>Prevention plan</h3><table><tr><th>Action</th><th>Who</th><th>By</th></tr>'
        '<tr><td>Seal eave gap with mesh</td><td>DJ Pest (included)</td><td>Done</td></tr>'
        '<tr><td>Fit escutcheon to meter-box conduit</td><td>Owner</td><td>2 weeks</td></tr>'
        '<tr><td>Cut back climber from roofline</td><td>Owner</td><td>Before winter</td></tr>'
        '<tr><td>Station check</td><td>DJ Pest</td><td>4 weeks</td></tr></table></div>'
        '<div class="stamp">Itemised · Documented</div>'
        '</div></div>', "ledger")

    process = c["section"](
        c["eyebrow"]("What happens on the first visit") +
        '<div class="section-head"><h2>Three steps. No sales pitch.</h2></div>' +
        c["steps"]([
            ("We look before we spray", "A walk-through of the house, roof void or sub-floor where it's safe, and the yard. Photos of what we find, and a straight answer about whether you need treatment at all."),
            ("You get an itemised price", "Written on the spot or sent within the hour. What's being treated, with what, and the re-treatment period that applies. If you'd rather think about it, that's fine."),
            ("Treatment, then the report", "Products applied to label with re-entry times explained. Your treatment report follows by email, and a reminder before your next inspection is due."),
        ]))

    season = c["section"](
        c["eyebrow"]("Perth pest calendar") +
        '<div class="section-head"><h2>What\'s active right now in the northern suburbs.</h2><p class="lead">Sandy coastal soils, warm summers and mild winters give Perth a predictable pest rhythm. Knowing it means treating at the right time, not after the damage.</p></div>' +
        c["season_strip"]())

    areas = c["section"](
        c["eyebrow"]("Where we work") +
        '<div class="grid grid-2" style="align-items:center;gap:3rem"><div>'
        '<h2>Based in Warwick. Fast across the northern corridor.</h2>'
        '<p class="lead">We deliberately keep the service area tight so response times stay short and we know the suburbs, soils and pests personally. Greenwood, Duncraig, Sorrento, Hillarys, Joondalup, Wanneroo and everything between.</p>'
        '<p><a class="btn btn-ghost" href="/service-areas">All service areas ' + icon("arrow", "icon") + '</a></p></div>'
        '<div class="card"><div class="num">Suburb pages</div><ul style="columns:2;list-style:none;padding:0;margin:0;font-size:.95rem;line-height:2">'
        + "".join(f'<li><a href="/{s.lower().replace(" ", "-")}" style="text-decoration:none;color:var(--ink-2)">{esc(s)}</a></li>' for s in ["Warwick", "Greenwood", "Duncraig", "Sorrento", "Hillarys", "Joondalup", "Wanneroo", "Balcatta"])
        + '</ul></div></div>')

    faqs = [
        ("Do I need to leave the house during treatment?", "For a standard general pest treatment, no. You and pets stay out of treated areas until surfaces are dry, usually two hours. We tell you the re-entry period for the specific product before we start."),
        ("What about kids and pets during treatment?", "Every product we use is registered by the APVMA and applied at the label rate. We use non-staining, low-odour formulations indoors and keep people and pets out until the re-entry period has passed. If anyone in the home is pregnant, asthmatic or chemically sensitive, tell us and we adjust the plan."),
        ("What if the pests come back?", "If the pest on your invoice is still active inside the treated area within the re-treatment period, we come back and re-treat at no charge. Periods are six months for general pest, three months for ants and rodents, 30 days for fleas and wasps. <a href=\"/warranty\">Full terms here</a>."),
        ("How much does pest control cost in Perth?", "It depends on the pest, the size of the property and how established the problem is. We publish a <a href=\"/pest-control-prices-perth\">transparent pricing guide</a> so you know the range before you call, and every quote is itemised."),
        ("Are you licensed?", f"Yes. Every treatment is carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence under the Health (Pesticides) Regulations 2011, and the technician's name and licence number appear on your treatment record. {S['reg_line']}"),
    ]
    faq_sec = c["section"](c["eyebrow"]("Questions") + '<div class="section-head"><h2>Straight answers.</h2></div>' + c["faq"](faqs), "ledger")

    body = hero + services + ca + report + process + season + areas + faq_sec + c["quote_block"]()
    return [{
        "path": "/",
        "title": "DJ Pest | Pest Control Perth Northern Suburbs | Termites, Rodents, Ants",
        "desc": "Family-run pest control for Perth's northern suburbs since 2011. Itemised prices in writing, a treatment report after every job, and a re-treatment promise. Call 0447 747 769.",
        "body": body,
        "schema": [c["faq_schema"](faqs)],
    }]
