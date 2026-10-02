"""Home page (v3, 2 Oct 2026): light theme, slogan-led, roughly half the words of v2. Every H2, internal link and the
FAQ schema from v2 are kept so nothing SEO-bearing was lost; the cuts are lead paragraphs, duplicated promises and the
season strip (which lives on /whats-my-pest)."""

def pages(c):
    S = c["SITE"]; esc = c["esc"]; icon = c["icon"]
    hero_art = f"""<div class="hero-art" aria-hidden="true">
<svg class="crosshair" viewBox="0 0 400 400">
  <circle class="ring" cx="200" cy="200" r="150"/>
  <line class="tick" x1="200" y1="20" x2="200" y2="66"/><line class="tick" x1="200" y1="334" x2="200" y2="380"/>
  <line class="tick" x1="20" y1="200" x2="66" y2="200"/><line class="tick" x1="334" y1="200" x2="380" y2="200"/>
  <image class="rat" href="/assets/img/rat-crosshair-black-520.webp" x="70" y="72" width="260" height="256"/>
</svg></div>"""

    hero = f"""<section class="hero"><div class="wrap">
<div>
  {c['eyebrow']("Pest management · Perth's northern suburbs · Warwick")}
  <h1>We do things<br>right the<br><em class="red">first</em> time.</h1>
  <p class="lead">Family pest control for Perth's northern suburbs. Quoted in writing before we start, documented after, and backed by a re-treatment promise.</p>
  {c['hours_cue']()}<div class="actions">{c['btn_call']()}{c['btn_quote']()}</div>
  <ul class="trust"><li>Licensed under the WA Pesticides Regs</li><li>In Perth pest management since {S['family_since']}</li><li>Public liability insured</li><li>Same-day for active pests</li></ul>
</div>
{hero_art}
</div></section>"""

    ourown = c["section"](
        c["eyebrow"]("How we decide what to do") +
        '<div class="section-head"><h2>If this were my house, what would I do?</h2>'
        '<p class="lead">It\'s the question I stop and ask on every job, before anything comes off the ute. The answer decides the treatment.</p></div>'
        '<div class="grid grid-3">'
        + c["card"]("Where your family lives", "Inside, it\'s non-staining, low-odour products, and only where they\'re needed. The same call I\'d make for my own kids.")
        + c["card"]("The cause, not just the symptom", "If sealing a gap or cutting back a climber does more than another spray, that\'s what you\'ll hear from us first.")
        + c["card"]("Sometimes the answer is no treatment", "If you don\'t need us, we tell you and leave. I wouldn\'t pay for a treatment my own house didn\'t need, either.")
        + '</div>'
        '<blockquote class="pullquote">&ldquo;We treat your house like it\'s our own.&rdquo;<small>Dane Johns · DJ Pest</small></blockquote>', "ledger")

    services = c["section"](
        c["eyebrow"]("What we treat") +
        '<div class="section-head"><h2>Thirteen jobs, one standard of care.</h2></div>' +
        '<div class="grid grid-3">' +
        c["card"]("Termite inspection", "AS 4349.3 timber pest inspection with photos and a written report.", "/termite-inspection-perth", "01 / Termites") +
        c["card"]("Termite treatment", "Non-repellent systems to AS 3660.2, or baiting where it suits the site.", "/termite-treatment-perth", "02 / Termites") +
        c["card"]("General pest treatment", "Cockroaches, spiders, silverfish and ants, inside and out. Six-month promise.", "/general-pest-control-perth", "03 / General") +
        c["card"]("Ant management", "Coastal brown ant colonies treated with slow-acting baits, not a quick spray.", "/ant-control-perth", "04 / Ants") +
        c["card"]("Cockroach management", "Gel baits and growth regulators indoors. Non-staining products only.", "/cockroach-control-perth", "05 / Cockroaches") +
        c["card"]("Rodent management", "Entry points found, stations placed, and a sealing plan so they stay out.", "/rodent-control-perth", "06 / Rodents") +
        c["card"]("Spider management", "Redbacks, white-tails and huntsmen. Internal spray only where it's needed.", "/spider-control-perth", "07 / Spiders") +
        c["card"]("Mosquito management", "Breeding sites first, then the shaded spots where adults rest.", "/mosquito-control-perth", "08 / Mosquitoes") +
        c["card"]("Vacate flea treatment", "Quoted from the address within the hour. Certificate for your agent.", "/flea-treatment-perth", "09 / Fleas") +
        c["card"]("Wasp removal", "Nests under eaves and pergolas, usually gone the same day.", "/wasp-removal-perth", "10 / Wasps") +
        c["card"]("Bee removal", "Swarms go to a beekeeper alive. Wall hives treated, sealed and proofed.", "/bee-removal-perth", "11 / Bees") +
        c["card"]("Commercial pest management", "Cafes, strata and childcare on a documented program your auditor can read.", "/commercial-pest-control-perth", "12 / Commercial") +
        c["card"]("Bed bug treatment", "Every harbourage treated, with a second visit built in to catch the hatch.", "/bed-bug-treatment-perth", "13 / Bed bugs") +
        '</div>', "ledger")

    why = c["section"](
        '<div class="grid grid-2" style="align-items:center;gap:3rem">'
        '<div>' + c["eyebrow"]("Why DJ Pest") +
        '<h2>Run by a Chartered Accountant.<br>Raised on a farm.</h2>'
        f'<p class="lead">Two generations in Perth pest management since {S["family_since"]}, and four before that on the land at Coorow. Our grandfather\'s rule still runs the business: {esc(S["pop_rule"])}</p>'
        '<p><a class="btn btn-ghost" href="/about">Our story ' + icon("arrow", "icon") + '</a></p></div>'
        '<div class="grid" style="gap:.8rem">'
        + c["card"]("Quoted in writing before we start", "No call-out fee, no deposit, no surprises on the invoice.")
        + c["card"]("A record of every treatment", "Product, rate, areas and re-entry period, kept as WA law requires and given to you.")
        + c["card"]("A promise, not a slogan", "If the pest comes back inside the period on your invoice, so do we, at no charge. <a href=\"/warranty\">The terms</a>.")
        + '</div></div>')

    report = c["section"](
        c["eyebrow"]("The DJ Pest treatment report") +
        '<div class="report"><div>'
        '<h2>The paperwork nobody else gives you.</h2>'
        '<p class="lead">Where they got in, what was applied and where, and what to fix so they stay out. It doubles as the record WA regulations require.</p>'
        '<div class="report-tabs" role="tablist">'
        '<button role="tab" aria-selected="true" data-tab="entry">1. Entry audit</button>'
        '<button role="tab" aria-selected="false" data-tab="ledger">2. Application ledger</button>'
        '<button role="tab" aria-selected="false" data-tab="plan">3. Prevention plan</button></div>'
        '<p class="notice">Sample only. Details vary by job.</p></div>'
        '<div class="report-doc" aria-live="polite">'
        '<div class="doc-head"><img src="/assets/img/logo-black-240.webp" alt="DJ Pest" width="240" height="105" loading="lazy"><span>Treatment report · sample</span></div>'
        '<div data-pane="entry"><h3>Point-of-entry audit</h3><table><tr><th>Location</th><th>Finding</th><th>Photo</th></tr>'
        '<tr><td>Roof void, NE corner</td><td>Rat droppings, gnawed sarking, gap at eave</td><td>#04</td></tr>'
        '<tr><td>Meter box</td><td>Conduit entry unsealed (20 mm)</td><td>#07</td></tr>'
        '<tr><td>Rear patio</td><td>Coastal brown ant trail to kitchen kickboard</td><td>#11</td></tr></table></div>'
        '<div data-pane="ledger" hidden><h3>Chemical application ledger</h3><table><tr><th>Product</th><th>Active</th><th>Rate</th><th>Where</th></tr>'
        '<tr><td>Non-repellent liquid (APVMA-registered)</td><td>Fipronil</td><td>Per label</td><td>External perimeter, ant trails</td></tr>'
        '<tr><td>Rodenticide block in tamper-resistant station</td><td>Per label</td><td>2 stations</td><td>Roof void, side path</td></tr>'
        '<tr><td>Non-staining dust</td><td>Per label</td><td>Light</td><td>Wall voids, kickboards</td></tr></table>'
        '<p style="font-size:.75rem;color:#555;margin:.6rem 0 0">Re-entry: 2 hours after surfaces dry. Technician name and licence number recorded.</p></div>'
        '<div data-pane="plan" hidden><h3>Prevention plan: what we\'d do if it were our house</h3><table><tr><th>Action</th><th>Who</th><th>By</th></tr>'
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
            ("We look before we spray", "House, roof void, sub-floor and yard, with photos, and one question: what would we do if it were ours? If you don't need treatment, we say so."),
            ("You get an itemised quote", "On the spot or within the hour: what, with what, and the re-treatment period. Think it over if you like."),
            ("Treatment, then the report", "Applied to label, re-entry explained, report by email, and a reminder before the next inspection is due."),
        ]))

    heritage = c["section"](
        c["eyebrow"]("Our roots · Elders Weekly, December 1977") +
        '<div class="grid grid-2" style="align-items:center;gap:3rem"><div>'
        '<h2>Take your time and do it right.</h2>'
        '<p class="lead">That was the headline over a 1977 interview with our senior advisor, then a young farmer at Coorow. Fifty years on, it is still how we work.</p>'
        f'<blockquote class="pullquote">&ldquo;My father says do a job right first time and you will never have to do it again.&rdquo;<small>{esc(S["senior"]["name"])} · Elders Weekly, 15 December 1977</small></blockquote>'
        '<p><a class="btn btn-ghost" href="/about#1977">Read the story ' + icon("arrow", "icon") + '</a></p></div>'
        '<figure class="archive" style="margin:0"><a href="/about#1977"><img src="/assets/img/elders-weekly-1977-headline.jpg" alt="Elders Weekly headline, 15 December 1977: Take your time and do it right" width="1200" height="134" loading="lazy"></a>'
        '<figcaption>Elders Weekly, 15 December 1977. From the family archive.</figcaption></figure></div>', "ledger")

    areas = c["section"](
        c["eyebrow"]("Where we work") +
        '<div class="grid grid-2" style="align-items:center;gap:3rem"><div>'
        '<h2>Based in Warwick. Fast across the northern corridor.</h2>'
        '<p class="lead">A tight service area keeps response times short and means we know the suburbs, soils and pests personally.</p>'
        '<p><a class="btn btn-ghost" href="/service-areas">All service areas ' + icon("arrow", "icon") + '</a></p></div>'
        '<div class="card"><div class="num">Suburb pages</div><ul style="columns:2;list-style:none;padding:0;margin:0;font-size:.95rem;line-height:2">'
        + "".join(f'<li><a href="/{s.lower().replace(" ", "-")}" style="text-decoration:none;color:var(--ink-2)">{esc(s)}</a></li>' for s in ["Warwick", "Greenwood", "Duncraig", "Sorrento", "Hillarys", "Joondalup", "Wanneroo", "Balcatta", "Marangaroo", "Stirling"])
        + '</ul></div></div>')

    faqs = [
        ("Do I need to leave the house during treatment?", "For a standard general pest treatment, no. You and pets stay out of treated areas until surfaces are dry, usually two hours. We tell you the re-entry period for the specific product before we start."),
        ("What about kids and pets during treatment?", "Every product we use is registered by the APVMA and applied at the label rate. We use non-staining, low-odour formulations indoors and keep people and pets out until the re-entry period has passed. If anyone in the home is pregnant, asthmatic or chemically sensitive, tell us and we adjust the plan."),
        ("What if the pests come back?", "If the pest on your invoice is still active inside the treated area within the re-treatment period, we come back and re-treat at no charge. Periods are six months for general pest, three months for ants and rodents, 30 days for fleas and wasps. <a href=\"/warranty\">Full terms here</a>."),
        ("How much does pest control cost in Perth?", "It depends on the pest, the size of the property and how established the problem is. We publish a <a href=\"/pest-control-prices-perth\">transparent investment guide</a> so you know the range before you call, and a <a href=\"/pest-control-cost-estimator\">cost estimator</a> that narrows it to your home, and every quote is itemised."),
        ("Are you licensed?", f"Yes. Every treatment is carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence under the Health (Pesticides) Regulations 2011, and the technician's name and licence number appear on your treatment record. {S['reg_line']}"),
    ]
    faq_sec = c["section"](c["eyebrow"]("Questions") + '<div class="section-head"><h2>Straight answers.</h2></div>' + c["faq"](faqs), "ledger")

    body = hero + ourown + services + why + report + process + heritage + areas + faq_sec + c["quote_block"]()
    return [{
        "path": "/",
        "title": "DJ Pest | Pest Control Perth Northern Suburbs | Termites, Rodents, Ants",
        "desc": "Family-run pest control for Perth's northern suburbs since 2011. We do things right the first time: itemised quotes in writing, a treatment report after every job, and a re-treatment promise. Call 0468 170 107.",
        "body": body,
        "schema": [c["faq_schema"](faqs)],
    }]
