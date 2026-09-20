"""Company pages: pricing guide, pest identifier, about, contact, terms, warranty, privacy, blog index + posts."""

DOMAIN = "https://djpest.com.au"


def _hero(c, eyebrow, h1, lead, actions=True):
    act = f'<div class="actions">{c["btn_call"]()}{c["btn_quote"]()}</div>' if actions else ""
    return f'<section class="hero"><div class="wrap"><div>{c["eyebrow"](eyebrow)}<h1>{h1}</h1><p class="lead">{lead}</p>{act}</div></div></section>'


def _prose(c, inner, cls="ledger"):
    return c["section"](f'<div class="prose">{inner}</div>', cls)


# ------------------------------------------------------------------ pricing
def pricing(c):
    S = c["SITE"]; T = c["ledger_table"]
    note = '<p class="notice">Typical range, GST inclusive. Every job is quoted itemised in writing before it is booked.</p>'

    general = T(["Service", "What it covers", "Typical range"], [
        ["General pest treatment (3-bedroom home)", "Internal and external treatment for cockroaches, spiders, silverfish and internal ants. Non-staining products indoors with an insect growth regulator where it helps. Six-month re-treatment period.", "$250 – $350"],
        ["Spider treatment (stand-alone)", "External web-and-harbourage treatment for redbacks, white-tails and huntsmen, with the internal spray only where it is needed. Included in a general pest treatment.", "$220 – $300"],
        ["External ant treatment", "Colony-level treatment for coastal brown and other super-colony ants using slow-acting non-repellents and baits, not a quick knockdown spray. Three-month re-treatment period.", "$250 – $400"],
        ["German cockroach kitchen program", "Gel bait plus insect growth regulator through the kitchen, appliances and voids, with a follow-up visit built into the price. Six-month re-treatment period.", "$250 – $450"],
    ], amount_cols=(2,))

    rodents = T(["Service", "What it covers", "Typical range"], [
        ["Rodent program, initial visit", "Species identification, entry-point audit, two tamper-resistant bait stations placed and a written proofing (sealing) plan. Three-month re-treatment period.", "$220 – $380"],
        ["Rodent follow-up check", "Station check and re-bait, activity review, proofing progress.", "$90 – $140"],
        ["Wasp nest removal", "Treatment and removal of an accessible European or paper wasp nest. 30-day re-treatment period.", "$180 – $280"],
        ["Mosquito yard treatment", "Breeding-site audit plus residual treatment of shaded harbourages. Recommended 4–6 week interval in peak season.", "$220 – $320"],
    ], amount_cols=(2,))

    termites = T(["Service", "What it covers", "Typical range"], [
        ["Timber pest / termite inspection", "Visual inspection to AS 4349.3:2010 of the interior, roof void and sub-floor where accessible, exterior and grounds, with moisture readings, photos and a written report.", "$250 – $350"],
        ["Pre-purchase timber pest inspection", "Same inspection scope, with a full AS 4349.3 report formatted for a property purchase and available to your settlement agent.", "$300 – $400"],
        ["Termite chemical management system", "Non-repellent treated zone installed to AS 3660.2:2017 around the perimeter, by trenching in garden beds and drilling and injecting through paving and concrete. Certificate issued. Price depends on perimeter length and construction.", "$2,500 – $5,500"],
        ["Termite baiting system install", "In-ground monitoring and baiting stations placed around the building to AS 3660.2, with a monitoring program priced separately.", "$1,500 – $3,000 plus monitoring"],
    ], amount_cols=(2,))

    movers = T(["Factor", "Moves the price down", "Moves the price up"], [
        ["Property size", "Unit, villa or standard 3-bedroom home on a small block", "Large two-storey home, multiple outbuildings, long fence lines"],
        ["Construction", "Slab-on-ground with open garden beds around the perimeter", "Paving or concrete against every wall (drilling and injecting), suspended timber floors, limestone footings, extensions with hidden joins"],
        ["Infestation stage", "Early: a few sightings, one trail, one entry point", "Established: breeding population in voids, multiple nests, structural timber already damaged"],
        ["Access", "Clear roof void and sub-floor, gates open, yard tidy", "No manhole, packed storage in the garage, dense garden against walls, dogs that need securing"],
        ["Preparation done", "Kitchen cleared, pet bowls up, lawn mowed before we arrive", "We do the preparation on the day (time is billed honestly, but it is still time)"],
    ])

    included = c["card"]("An itemised written quote", "Every line is priced separately, so you can see what the treatment is, what the report is and what the follow-up is. Accept all of it or part of it.") + \
        c["card"]("A treatment record", "Product, active constituent, rate, areas treated and re-entry period. We keep it three years as the Health (Pesticides) Regulations 2011 require, and you get a copy.") + \
        c["card"]("A re-treatment period", "Printed on your invoice. If the pest we treated is still active inside the treated area within that period, we come back at no charge. <a href=\"/warranty\">Read the promise</a>.")

    never = c["card"]("No call-out fee", "Coming to look costs nothing. If we find you do not need treatment, we tell you and leave.") + \
        c["card"]("No deposit", "You pay after the work, on seven-day terms. Bank transfer, PayTo or card, no surcharge.") + \
        c["card"]("No surprise variations", "If we find something concealed on the day, we stop, explain it and price it before continuing. Never on the invoice.")

    compare = [
        ("Is the price itemised, or one number?", "One number hides what you are paying for. Ask for the treatment, the report and any follow-up as separate lines."),
        ("What product will you use, and is it on the APVMA register?", "A licensed operator can name the product and its active constituent before they arrive. If they cannot, keep looking."),
        ("What is the re-treatment period, and is it in writing?", "A verbal promise is not a promise. It should be on the quote and the invoice with its conditions."),
        ("Will I get a treatment record?", "WA law requires the operator to make one. You should receive a copy, not have to ask for it."),
        ("What is your licence and business registration number?", f"Ours are Technician Licence {S['licence']} and business registration {S['pmb']}, both with the WA Department of Health. Every operator should be able to give you theirs."),
        ("Is there a call-out fee, a deposit or a variation clause?", "Read the fine print for the phrase \"additional charges may apply\". Ask what would trigger one."),
    ]

    faqs = [
        ("How much does pest control cost?", "In Perth a general pest treatment for a standard three-bedroom home is typically $250 to $350 including GST. Targeted treatments for ants, German cockroaches or rodents sit between $220 and $450 depending on the extent of the problem. Termite work is priced by the perimeter and construction and ranges from $250 for an inspection to $2,500 to $5,500 for a full chemical management system. Every DJ Pest job is quoted itemised in writing before it is booked."),
        ("What are typical pest control prices in Perth?", "The tables on this page are our typical ranges for Perth's northern suburbs: general pest $250–$350, external ants $250–$400, German cockroach program $250–$450, rodent program $220–$380, spider treatment $220–$300, termite inspection $250–$350, pre-purchase timber pest inspection $300–$400, termite chemical system $2,500–$5,500, termite baiting $1,500–$3,000 plus monitoring, wasp nest $180–$280, mosquito yard treatment $220–$320."),
        ("How much does termite treatment cost?", "A termite chemical management system installed to AS 3660.2:2017 typically costs $2,500 to $5,500 in Perth, depending on the length of the perimeter and how much of it is paved or concreted (which has to be drilled and injected rather than trenched). A baiting system is $1,500 to $3,000 to install plus an ongoing monitoring program. An inspection first ($250–$350) tells you which one the house actually needs."),
        ("What does an exterminator cost per visit?", "We do not use the word exterminator, because no treatment removes every pest for good. A single general pest visit is $250 to $350. Follow-up visits, where a program needs them, are $90 to $140. There is no call-out fee for a look and a quote."),
        ("Why is one quote so much cheaper than another?", "Usually one of four things: a smaller scope (external only, no roof void), a repellent spray instead of a colony treatment, no report or follow-up, or a variation clause that lifts the price on the day. Ask the six questions above and the difference usually explains itself."),
        ("Do you charge more for same-day or weekend work?", "No. We work Monday to Saturday, 7am to 6pm, at the same rates. If we can fit an active infestation in today, we do."),
        ("Are prices GST inclusive?", "Yes. Every figure on this page and every quote we send includes GST. There is no deposit and payment terms are seven days from the invoice."),
    ]

    body = _hero(c, "Pricing guide · Perth northern suburbs",
                 "How much does pest control cost in Perth?",
                 "Here is what we charge, before you call. These are typical ranges for a standard home in Perth's northern suburbs. Every job is quoted itemised in writing, and the quote is the price. We're not the lowest price in Perth, we're thorough.")

    body += c["section"](c["eyebrow"]("General pest, ants, cockroaches, spiders") + '<div class="section-head"><h2>Everyday pests</h2><p class="lead">The jobs most northern-suburbs homes need once a year. Internal treatments use non-staining, low-odour products; external treatments use the chemistry that suits the pest, not the one that suits the truck.</p></div>' + general + note, "ledger")
    body += c["section"](c["eyebrow"]("Rodents and wasps") + '<div class="section-head"><h2>Rodents and wasps</h2><p class="lead">Rodent work is a program, not a visit. The first price includes proofing advice because sealing the entry is what stops them coming back.</p></div>' + rodents + note, "ledger")
    body += c["section"](c["eyebrow"]("Termites and timber pests") + '<div class="section-head"><h2>Termite inspections and treatment</h2><p class="lead">Termite prices vary more than any other pest because they follow the building, not the pest. We inspect first and quote the system the house needs, with a drawing of where it goes.</p></div>' + termites + note + '<p><a href="/termite-inspection-perth">About termite inspections</a> · <a href="/termite-treatment-perth">About termite treatment</a></p>', "ledger")

    body += c["section"](c["eyebrow"]("What moves the price") + '<div class="section-head"><h2>Why your quote lands where it does</h2><p class="lead">Four things account for almost every difference between the low and high end of a range. We tell you which apply to your property on the quote itself.</p></div>' + movers, "ledger")

    body += c["section"](c["eyebrow"]("Always included") + '<div class="section-head"><h2>What every price includes</h2></div><div class="grid grid-3">' + included + '</div>', "ledger")
    body += c["section"](c["eyebrow"]("Never charged") + '<div class="section-head"><h2>What we never charge for</h2></div><div class="grid grid-3">' + never + '</div>', "ledger")

    body += c["section"](c["eyebrow"]("How to compare quotes") + '<div class="section-head"><h2>Six questions to ask any pest controller</h2><p class="lead">Ask these of us too. A fair operator answers all six without hesitating.</p></div>' + c["steps"](compare), "ledger")

    body += _prose(c, """<h2>A note on the accountant's approach</h2>
<p>DJ Pest is run by a Chartered Accountant. That shapes the pricing in three ways. First, every quote is a ledger: line items, quantities, a total, nothing folded into a single "from" price. Second, every job leaves a paper trail, the treatment record and the report, so you can see what the money bought. Third, there are no incentives to upsell on the day. The technician who quotes is the technician who treats, and the price does not change once you have accepted it unless we find something concealed, in which case we stop and explain before we continue.</p>
<p>If you are comparing this page with a "from $99" advertisement, look for what the $99 covers. Usually it is an external spray with no roof void, no report and no re-treatment period. That is not a pest treatment; it is a lower price for a different job.</p>
<p>Ranges on this page are updated as our costs change. The quote you accept is the price you pay. <a href="/services">See all services</a> or <a href="/service-areas">check we cover your suburb</a>.</p>""")

    body += c["section"](c["eyebrow"]("Pricing questions") + '<div class="section-head"><h2>Straight answers about cost</h2></div>' + c["faq"](faqs), "ledger")
    body += c["quote_block"]("Get your itemised price.", "Tell us the pest, the suburb and roughly what you are seeing. We'll send a written, itemised price, usually the same day, before anything is booked.")

    offers = [("General pest treatment", 250, 350), ("External ant treatment", 250, 400), ("German cockroach program", 250, 450),
              ("Rodent control program", 220, 380), ("Spider treatment", 220, 300), ("Termite inspection", 250, 350),
              ("Pre-purchase timber pest inspection", 300, 400), ("Termite chemical management system", 2500, 5500),
              ("Termite baiting system", 1500, 3000), ("Wasp nest removal", 180, 280), ("Mosquito yard treatment", 220, 320)]
    offer_schema = {"@type": "OfferCatalog", "name": "DJ Pest price guide", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "provider": {"@id": DOMAIN + "/#business"}},
         "priceCurrency": "AUD", "price": lo,
         "priceSpecification": {"@type": "PriceSpecification", "minPrice": lo, "maxPrice": hi, "priceCurrency": "AUD", "valueAddedTaxIncluded": True}}
        for n, lo, hi in offers]}
    return {
        "path": "/pest-control-prices-perth",
        "title": "Pest Control Prices Perth 2026 | Transparent Cost Guide | DJ Pest",
        "desc": "How much does pest control cost in Perth? Typical ranges for general pest, ants, cockroaches, rodents, spiders, termite inspections and treatment. Itemised quotes, no call-out fee.",
        "body": body,
        "schema": [c["faq_schema"](faqs), offer_schema],
        "crumbs": [("Pricing guide", None)],
    }


# ------------------------------------------------------------------ what's my pest
def whats_my_pest(c):
    S = c["SITE"]
    cards = [
        ("/rodent-control-perth", "Droppings in the roof or pantry", "Dark, spindle-shaped pellets, scratching at night, gnawed packets.", "Rats or mice. Rat droppings are 12–18 mm, mouse droppings 3–6 mm. We identify the species, find the entry and place tamper-resistant stations."),
        ("/ant-control-perth", "Trail of small brown ants", "A steady line along skirting, paving edges or into the pantry.", "Most likely coastal brown ants, a super-colony species. Sprays split the colony; we use slow-acting non-repellents and baits that reach the queens."),
        ("/cockroach-control-perth", "Cockroach in the kitchen at night", "Small, tan, two dark stripes, near the fridge or dishwasher.", "German cockroaches breed in warm appliance voids. Gel bait plus an insect growth regulator, not aerosol, is the treatment that holds."),
        ("/termite-inspection-perth", "Mud tubes on brick or piers", "Pencil-width earthen tunnels running up a wall, pier or slab edge.", "Subterranean termites. Do not break the tubes open. Book an AS 4349.3 inspection; we map the activity before recommending a system."),
        ("/spider-control-perth", "Messy tangled web in a corner", "Untidy, strong web low down, under outdoor furniture, in the meter box.", "Redback territory. Their webs are irregular, not the neat orb of a garden spider. External harbourage treatment with a check of play equipment."),
        ("/termite-inspection-perth", "Sawdust-like piles near timber", "Fine granular frass below a skirting, window frame or beam.", "Borers or drywood termites leave pellets; subterranean termites usually do not. Either way it needs a timber pest inspection to tell which."),
        ("/general-pest-control-perth", "Bites overnight", "Small itchy welts in lines or clusters, worse on arms and legs.", "Fleas if you have pets or carpet; bed bugs if the bites are along the mattress edge. Different treatments, both with a 30-day re-treatment period."),
        ("/mosquito-control-perth", "Bitten in the yard after five", "Mosquitoes biting on the patio from late afternoon, resting on shaded walls by day, wrigglers in saucers or the bird bath.", "Container breeders at home plus wetland species flying in. A breeding-site audit and a residual treatment of the shaded harbourages cuts the numbers for weeks."),
        ("/general-pest-control-perth", "Wasps around the eaves", "Repeated wasp traffic to one point under the roofline or in a wall vent.", "A paper wasp or European wasp nest. We treat and remove accessible nests; 30-day re-treatment period. Keep children away from the flight line."),
        ("/cockroach-control-perth", "Large dark cockroach on the patio", "35–40 mm, reddish or with yellow wing markings, mostly outdoors.", "American or Australian cockroaches from mulch, drains and wood piles. External harbourage treatment, not a kitchen program."),
        ("/rodent-control-perth", "Scratching in the ceiling at dusk", "Running or scratching above the bedroom as the light goes.", "Roof rats are active at dusk and dawn. Possums are heavier and slower. We check the roof void, then bait or refer accordingly."),
        ("/ant-control-perth", "Large black ants at night", "5–15 mm, slow, single ants rather than a trail, drawn to sweet spills.", "Sugar ants. Mostly outdoor, occasionally wandering in. A sweet bait along the entry point usually settles it."),
        ("/spider-control-perth", "Grey-brown spider with banded legs", "Cigar-shaped body, found in bedding, towels or shoes.", "White-tailed spider. They hunt other spiders, so reducing their food (daddy-long-legs and black house spiders) is part of the treatment."),
    ]
    grid = '<div class="ident">' + "".join(
        f'<a href="{h}"><strong>{c["esc"](t)}</strong><small>{c["esc"](s)}</small><span style="font-size:.9rem;color:var(--ink-2)">{c["esc"](x)}</span></a>' for h, t, s, x in cards) + '</div>'

    body = _hero(c, "Pest identifier",
                 "What's my pest?",
                 "Pick the thing you saw. Each card tells you what it usually is in Perth's northern suburbs and takes you to the right treatment page. If none of them fit, text us a photo.",
                 actions=False)
    body += c["section"](c["eyebrow"]("What did you see?") + grid, "ledger")
    body += _prose(c, f"""<h2>Still not sure? Text a photo.</h2>
<p>A phone photo is enough for most identifications. Send it to <a href="{S['phone_sms']}">{S['phone_display']}</a> with your suburb and where you found it (kitchen, roof void, garden bed). We reply during business hours, Monday to Saturday, with what it is, whether it needs treatment and roughly what that would cost. No charge for the identification.</p>
<div class="callout"><p><strong>Helpful photos:</strong> the pest next to a coin for scale, droppings where you found them, mud tubes with a wider shot of the wall, and any damage to timber or packaging. A blurry photo of a fast ant is still useful if the trail is in the frame.</p></div>
<h2>Why identification comes first</h2>
<p>Every pest on this page is treated differently, and getting the species wrong wastes the treatment. A repellent spray on a coastal brown ant trail splits the colony into several. Aerosol on German cockroaches scatters them deeper into the voids. Breaking a termite mud tube sends the workers elsewhere and hides the evidence an inspector needs. Rat bait placed for mice, or mouse bait for rats, gets ignored.</p>
<p>That is why the first thing we do on any visit is look, not spray. Species, entry point, harbourage and conditions first, then the chemistry that fits, applied to its APVMA label. The <a href="/pest-control-prices-perth">pricing guide</a> shows what each treatment typically costs once we know what we are dealing with.</p>
<h2>Perth's northern suburbs pest calendar</h2>
<p>Timing narrows the answer too. Ants and spiders build in spring as the sand warms. Termite swarmers appear on warm, humid evenings from November to April. Cockroaches move indoors as the nights cool in autumn. Rodents look for roof voids in winter. If you saw the pest this week, the season is a strong clue.</p>""")
    body += c["section"](c["eyebrow"]("Right now") + c["season_strip"]())
    body += c["quote_block"]("Send us what you saw.", "Describe it or attach nothing at all, we'll call and ask the right questions. Identification is free.")
    return {
        "path": "/whats-my-pest",
        "title": "What's My Pest? Identify Ants, Cockroaches, Termites, Rodents | DJ Pest Perth",
        "desc": "Droppings in the roof, a trail of brown ants, mud tubes on brick or a messy web? Pick what you saw and find the right treatment. Or text a photo to 0447 747 769.",
        "body": body,
        "crumbs": [("What's my pest?", None)],
    }


# ------------------------------------------------------------------ about
def about(c):
    S = c["SITE"]
    mark = ('<div class="card" style="text-align:center;padding:2.5rem 1.6rem">'
            '<img src="/assets/img/rat-crosshair-white.png" alt="DJ Pest rat-in-crosshair mark" width="160" height="158" style="margin:0 auto 1rem;width:160px;aspect-ratio:1/1;object-fit:contain;filter:invert(1)" loading="lazy">'
            f'<div class="num">{c["esc"](S["owner"])}</div><p>{c["esc"](S["owner_title"])}<br>{c["esc"](S["licence_label"])}<br>{c["esc"](S["reg_short"])}<br>Based in {S["base_suburb"]} WA {S["base_postcode"]}</p></div>')

    body = _hero(c, "About DJ Pest · Warwick, WA",
                 f"A Perth family pest control business since {S['family_since']}. Second generation, run by a Chartered Accountant.",
                 "DJ Pest is a small, family-run pest management business in Warwick, servicing Perth's northern suburbs. The technician who quotes is the technician who treats and writes the report.")
    body += c["section"]('<div class="grid grid-2" style="align-items:start;gap:3rem"><div class="prose">'
        "<h2>Fifteen years in Perth pest control.</h2>"
        "<p>Our family started in Perth pest control in 2011, working the northern suburbs out of a ute: roof voids in January, sub-floors in July, learning which suburbs have the sand that coastal brown ants love and which have the limestone that termites track along. That is where we learned how a good technician reads a house before opening a drum of anything.</p>"
        "<p>The second generation kept the books for that business from the start and went on to qualify as a Chartered Accountant. Fifteen years of watching how service businesses price by feel, promise by mouth and keep no records teaches you that the fix is not marketing, it is bookkeeping.</p>"
        f"<p>DJ Pest was formed in 2026 as the second generation of that family business, run its own way. Our technicians are licensed under the WA Health (Pesticides) Regulations 2011. {S['reg_line']}</p>"
        "<h2>Why the accountant's approach matters</h2>"
        "<p>Pest control is a trust purchase. You cannot see what was applied in the roof void, you cannot verify the rate, and you find out whether it worked six weeks later. Most of the industry's bad reputation comes from that gap: a one-line invoice, a verbal promise and no way to check either.</p>"
        "<p>An accountant closes gaps like that with documents. So every DJ Pest job produces three: an itemised quote before the work, a chemical application ledger during it (product, active constituent, rate, areas, re-entry period) and a treatment report after it, with photos of what was found and a prevention plan. The ledger doubles as the treatment record WA law requires us to keep for three years. You get a copy of all of it without asking.</p>"
        "<p>It also means the numbers are honest. There is no call-out fee, no deposit and no variation on the day without stopping to explain it. The <a href=\"/pest-control-prices-perth\">pricing guide</a> is published so you can check a quote against it. The <a href=\"/warranty\">re-treatment promise</a> is written down with its conditions rather than implied.</p>"
        "</div><div>" + mark +
        '<div class="card" style="margin-top:.8rem"><div class="num">Credentials</div><ul style="list-style:none;padding:0;margin:0;line-height:1.9;font-size:.95rem">'
        f"<li>Licensed technicians (WA Health (Pesticides) Regulations 2011)</li><li>{S['reg_short']}</li><li>Run by a Chartered Accountant</li><li>Public liability insured</li><li>ABN {S['abn']}</li></ul></div>"
        "</div></div>")

    body += c["section"](c["eyebrow"]("The first visit") + '<div class="section-head"><h2>What a first visit is like</h2><p class="lead">About an hour for a general pest job, longer for termites. No sales script.</p></div>' + c["steps"]([
        ("A conversation at the door", "What you have seen, where, for how long, and anything we need to know: pregnancy, asthma, pets, fish tanks, edible gardens. That changes the product and the timing."),
        ("A walk-through with a torch", "Inside, roof void and sub-floor where it is safe, then the perimeter and yard. Photos of droppings, trails, tubes, moisture and entry points. If there is nothing to treat, we say so."),
        ("An itemised price, on paper", "What is being treated, with what, the re-entry period and the re-treatment period. Written on the spot or sent within the hour. Accept it then or later; nothing is booked until you do."),
        ("Treatment, then the report", "Products applied to label, warning signs where required, re-entry explained. The treatment report follows by email with the ledger and a prevention plan for the things only you can fix."),
    ]), "ledger")

    body += _prose(c, f"""<h2>How we work</h2>
<ul>
<li><strong>Diagnose before treating.</strong> Species, entry point and harbourage first. The chemistry follows the pest, not the truck.</li>
<li><strong>Label is law.</strong> Every product is APVMA-registered and applied at its label rate. We will not apply a product outside its label, even if asked.</li>
<li><strong>Standards, not opinions.</strong> Termite inspections to AS 4349.3:2010, termite management to AS 3660.2:2017, records to the Health (Pesticides) Regulations 2011 (WA).</li>
<li><strong>Indoors, non-staining.</strong> Low-odour, non-staining formulations and growth regulators inside; the heavier chemistry stays outside where it belongs.</li>
<li><strong>Small on purpose.</strong> A tight service area from {S['base_suburb']} means short drive times and a technician who knows your house. <a href="/service-areas">See the suburbs we cover</a>.</li>
</ul>
<h2>Where we are</h2>
<p>Based in Warwick, WA 6024, in the middle of the northern corridor. Most of the service area is within twenty minutes. Hours are {S['hours']}. Call <a href="tel:{S['phone_tel']}">{S['phone_display']}</a>, text a photo to the same number, or email <a href="mailto:{S['email']}">{S['email']}</a>.</p>""")
    body += c["quote_block"]("Talk to us directly.", "The person who answers the phone is one of the technicians who comes out. Tell us what you are seeing and we'll give you a straight answer and a written price.")
    schema = [{
        "@type": "AboutPage", "name": "About DJ Pest", "url": DOMAIN + "/about",
        "mainEntity": {"@id": DOMAIN + "/#business"}}]
    return {
        "path": "/about",
        "title": "About DJ Pest | Family-Run Perth Pest Control Since 2011",
        "desc": "A Perth family pest control business since 2011, now run by a Chartered Accountant. Licensed technicians, itemised quotes, written treatment records. Based in Warwick.",
        "body": body, "schema": schema, "crumbs": [("About", None)],
    }


# ------------------------------------------------------------------ contact
def contact(c):
    S = c["SITE"]
    areas = ", ".join(S["service_area"][:12])
    cards = (c["card"]("Call", f'<a href="tel:{S["phone_tel"]}" style="font-size:1.3rem;text-decoration:none">{S["phone_display"]}</a><br>Answered by one of our technicians. If we are in a roof void, leave a message and we call back within the hour.') +
             c["card"]("Text a photo", f'<a href="{S["phone_sms"]}" style="font-size:1.3rem;text-decoration:none">{S["phone_display"]}</a><br>Send a photo of the pest, droppings or damage with your suburb. Free identification.') +
             c["card"]("Email", f'<a href="mailto:{S["email"]}" style="font-size:1.1rem;text-decoration:none">{S["email"]}</a><br>For quotes, reports, invoices and strata or commercial enquiries.') +
             c["card"]("Hours", f'{S["hours"]}<br>Closed Sundays and public holidays. Same-day for active infestations where the run allows.'))
    body = _hero(c, "Contact", "Get in touch.", "Phone, text or the form. Whichever you choose, you get a written, itemised price before anything is booked.", actions=False)
    body += c["section"]('<div class="grid grid-4">' + cards + '</div>', "ledger")
    body += c["section"]('<div class="grid grid-2" style="gap:3rem;align-items:start"><div class="prose">'
        f"<h2>Where we work</h2><p>DJ Pest is based in {S['base_suburb']} WA {S['base_postcode']} and services Perth's northern suburbs: {c['esc'](areas)} and the coastal strip north to Yanchep. Most jobs are within twenty minutes of the depot. <a href=\"/service-areas\">Full list of service areas</a>.</p>"
        f"<h2>Business details</h2><p>{c['esc'](S['legal_name'])}<br>ABN {S['abn']} · ACN {S['acn']}<br>{c['esc'](S['reg_line'])}<br>{c['esc'](S['licence_label'])}</p>"
        "<p>We do not have a shopfront. Visits are by appointment at your property; there is nothing to collect from ours.</p>"
        '</div><div class="card" style="min-height:280px;display:grid;place-items:center;text-align:center"><div><div class="num">Map</div><p>Warwick, WA 6024. Servicing the northern corridor from Balcatta and Karrinyup up the coast to Yanchep, and inland to Wanneroo.</p><p><a href="/service-areas">See the suburb list</a></p></div></div></div>', "")
    body += c["quote_block"]("Or use the form.", "Name, mobile and suburb are enough. We'll call back with the right questions and a written price.")
    return {
        "path": "/contact",
        "title": "Contact DJ Pest | Pest Control Warwick & Perth Northern Suburbs",
        "desc": "Call or text 0447 747 769, email ops@djpest.com.au, or send the form. Mon–Sat 7am–6pm. Based in Warwick, servicing Perth's northern suburbs.",
        "body": body, "schema": [{"@type": "ContactPage", "name": "Contact DJ Pest", "url": DOMAIN + "/contact", "mainEntity": {"@id": DOMAIN + "/#business"}}],
        "crumbs": [("Contact", None)],
    }


# ------------------------------------------------------------------ terms
def _retreat_table(c):
    return c["ledger_table"](["Service", "Free re-treatment period"], [
        ["General pest treatment (cockroaches, spiders, silverfish, internal ants)", "6 months"],
        ["External ant treatment", "3 months"],
        ["Rodent baiting", "3 months, or the agreed program period"],
        ["Fleas", "30 days, subject to your completing the preparation and vacuuming plan"],
        ["Bed bugs", "30 days, subject to your completing the treatment plan (usually two visits)"],
        ["Wasps, bees (relocation), bird control, one-off nests", "30 days"],
        ["Termite chemical management system", "The period stated on your AS 3660.2 certificate (typically up to 8 years), conditional on annual inspections (clause 5.4)"],
        ["Termite baiting / monitoring", "Duration of the agreed monitoring agreement"],
        ["Timber pest and termite inspections", "No re-treatment period; see clause 5.5"],
    ])


def terms(c):
    body = _hero(c, "Legal", "Terms and conditions of service.", "Version 1.0, 18 September 2026. The version on your quote applies to that job.", actions=False)
    body += _prose(c, f"""<h2>1. Who we are</h2>
<p>1.1 Services are provided by <strong>DJ Pest Pty Ltd (ACN 697 588 579) as trustee for the Johns Family Trust, ABN 86 797 740 716</strong> ("DJ Pest", "we", "us"). Contact: ops@djpest.com.au, 0447 747 769, djpest.com.au.</p>
<p>1.2 Pest management treatments are carried out by technicians licensed under the <em>Health (Pesticides) Regulations 2011</em> (WA). Licence numbers appear on every treatment record.</p>
<p>1.3 DJ Pest Pty Ltd has applied for registration as a pest management business with the Western Australian Department of Health under the <em>Health (Pesticides) Regulations 2011</em> (registration number PMB 3000 assigned, certificate pending). Until the certificate issues, treatments are carried out and recorded under a registered pest management business, and invoiced accordingly.</p>
<h2>2. Quotes and acceptance</h2>
<p>2.1 Quotes are valid for <strong>30 days</strong> and are based on the information you gave us and what we could see at the time. Concealed conditions (for example inaccessible roof voids or sub-floors, undisclosed infestation extent, structural issues) may require a variation, which we will explain and price before proceeding.</p>
<p>2.2 A quote is accepted when you accept it online, in writing, by SMS, or by allowing us to start work.</p>
<p>2.3 All prices are in Australian dollars and <strong>include GST</strong> unless stated.</p>
<p>2.4 <strong>Cooling-off.</strong> If we quoted in your home without you inviting us (an unsolicited consumer agreement), you may cancel within 10 business days under section 82 of the Australian Consumer Law. This does not apply to work you requested.</p>
<h2>3. Scheduling, access and preparation</h2>
<p>3.1 Bookings are confirmed by SMS or email. We give an arrival window rather than a fixed time and send an "on the way" text where possible.</p>
<p>3.2 You must give us safe, unobstructed access to all areas to be treated, secure pets, and complete any preparation steps we send you (for example covering fish tanks, removing food from benches, vacating during and after treatment for the re-entry period).</p>
<p>3.3 If we cannot start or complete the work because of access, preparation, weather (wind, rain) or safety, we will reschedule at no charge.</p>
<p>3.4 Please give at least 24 hours' notice to cancel or move a booking so the time can be offered to someone else.</p>
<h2>4. Our work</h2>
<p>4.1 We use only pesticides registered by the APVMA, applied strictly in accordance with the approved label and the <em>Health (Pesticides) Regulations 2011</em>. We will not apply a product outside its label directions, even at your request.</p>
<p>4.2 Before treatment we will tell you the product, the re-entry period and any precautions. During treatment we may erect warning signs as required by regulation 60. Do not remove them.</p>
<p>4.3 Within 2 business days of each treatment we make a treatment record containing the details required by regulation 77 (address, areas treated, date and time, technician, product brand, active constituent, application rate, equipment). You receive a copy with your service report.</p>
<p>4.4 Termite work is carried out to <strong>AS 3660.2:2017</strong> (management of existing buildings) and timber pest inspections to <strong>AS 4349.3:2010</strong>. These standards define the limitations of what can be inspected and treated; those limitations form part of our report and these terms.</p>
<p>4.5 We may take photographs of the areas treated for your report and our records.</p>
<h2>5. Results and our service promise</h2>
<p>5.1 Pest management reduces pest activity; no treatment can eliminate every pest for good, and pests can re-enter from neighbouring properties or with goods. We do not promise a pest-free property.</p>
<p>5.2 <strong>Free re-treatment period.</strong> If the target pest listed on your invoice is still active inside the treated areas within the period below, we will return and re-treat the affected area at no charge, provided you have followed our preparation and after-care instructions:</p>
{_retreat_table(c)}
<p>5.3 The re-treatment period does not cover: pests not listed on the invoice; new infestations introduced after treatment; areas you asked us not to treat or that were inaccessible; damage caused by pests; treatments where you did not follow preparation or after-care instructions; or where building works, landscaping, plumbing leaks or soil disturbance have breached a termite management system.</p>
<p>5.4 <strong>Termite management systems</strong> must be inspected at least annually as required by AS 3660.2:2017 (interval not exceeding 12 months) for the system to remain effective and for clause 5.2 to apply. We will remind you when an inspection is due. Missed inspections void the re-treatment period from the date the inspection fell due.</p>
<p>5.5 Timber pest and termite <strong>inspections</strong> are visual and non-invasive within the limits of AS 4349.3. An inspection is a snapshot on the day; it is not a warranty that timber pests are absent or will not appear later, and it does not cover concealed areas listed as inaccessible in the report.</p>
<h2>6. Australian Consumer Law</h2>
<p>6.1 Our services come with guarantees that cannot be excluded under the Australian Consumer Law: they will be provided with due care and skill, be fit for any purpose you told us about, and be delivered within a reasonable time. Nothing in these terms limits those rights.</p>
<p>6.2 Where the law allows, our liability for a failure to comply with a consumer guarantee is limited to supplying the service again or paying the cost of having it supplied again (ACL s 64A).</p>
<p>6.3 Clause 5 is in addition to, and does not replace, your rights under the Australian Consumer Law.</p>
<h2>7. Payment</h2>
<p>7.1 Invoices are due 7 days from the invoice date unless a different term is shown on the invoice.</p>
<p>7.2 Pay by bank transfer, PayTo, or card (online or on site). Card and PayTo payments are processed by ServiceM8 Pay (Stripe); no surcharge is added.</p>
<p>7.3 Overdue accounts may be referred for collection and you agree to pay our reasonable recovery costs. We may suspend re-treatment obligations while an account is overdue.</p>
<h2>8. Health, safety and your responsibilities</h2>
<p>8.1 Tell us before we start about pregnancy, asthma, chemical sensitivity, infants, elderly or immunocompromised occupants, pets, fish, birds, reptiles, bees, or edible gardens. We will adjust the product, method or timing.</p>
<p>8.2 Keep people and pets out of treated areas until the re-entry period we advise has passed and surfaces are dry. Do not wash treated surfaces for the period we advise, as this reduces the treatment's effect.</p>
<p>8.3 You are responsible for structural, plumbing and landscaping conditions that attract pests (moisture, timber-to-ground contact, stored goods). We will point these out; fixing them is up to you and the re-treatment period assumes you do.</p>
<h2>9. Privacy and communication</h2>
<p>9.1 We collect your name, address, contact details, property details, photos and treatment history to provide the service, keep the records the Regulations require, and remind you of due inspections. Our <a href="/privacy">Privacy Policy</a> at djpest.com.au/privacy explains access, correction and complaints.</p>
<p>9.2 We will send booking confirmations, reminders, reports, invoices and annual service reminders by SMS and email. Marketing messages are only sent with your consent and every message has an unsubscribe option (Spam Act 2003).</p>
<h2>10. Insurance and limits</h2>
<p>10.1 We hold public liability insurance and, where applicable, professional indemnity insurance for timber pest inspections. Certificates are available on request.</p>
<p>10.2 To the extent permitted by law, we are not liable for indirect or consequential loss, or for loss caused by your failure to follow our instructions, by third parties, or by conditions outside our control.</p>
<h2>11. Disputes</h2>
<p>11.1 Tell us within 7 days if you are unhappy with our work and we will come back to look. If we cannot resolve it, you may contact Consumer Protection WA (1300 30 40 54) or, for licensing matters, the WA Department of Health Pesticide Safety Section (9222 2000). These terms are governed by the laws of Western Australia.</p>
<h2>12. General</h2>
<p>12.1 These terms, your quote and our service report make up the whole agreement. If any clause is unenforceable the rest still applies. We may update these terms; the version on your quote applies to that job.</p>
<hr>
<p class="notice"><em>Version 1.0, 18 September 2026. DJ Pest Pty Ltd ATF Johns Family Trust, ABN 86 797 740 716. ops@djpest.com.au | 0447 747 769 | djpest.com.au</em></p>
<p>See also: <a href="/warranty">Our re-treatment promise</a> · <a href="/privacy">Privacy policy</a></p>""")
    body += c["quote_block"]()
    return {
        "path": "/terms",
        "title": "Terms and Conditions of Service | DJ Pest",
        "desc": "DJ Pest terms of service: quotes, scheduling, our work to APVMA labels and Australian Standards, re-treatment periods, Australian Consumer Law, payment and privacy.",
        "body": body, "crumbs": [("Terms & conditions", None)],
    }


# ------------------------------------------------------------------ warranty
def warranty(c):
    S = c["SITE"]
    body = _hero(c, "Our re-treatment promise",
                 "If it comes back, so do we.",
                 "Every invoice carries a re-treatment period. If the pest we treated is still active inside the treated area within that period, we return and re-treat at no charge. Here is the promise in full, with its conditions, so there is nothing to argue about later.", actions=False)
    body += c["section"](c["eyebrow"]("The periods") + '<div class="section-head"><h2>Re-treatment periods by service</h2><p class="lead">Taken from clause 5.2 of our <a href="/terms">terms and conditions</a>. The period that applies to your job is printed on your quote and invoice.</p></div>' + _retreat_table(c), "ledger")
    body += _prose(c, f"""<h2>The conditions</h2>
<p>The promise applies when the target pest listed on your invoice is still active inside the areas we treated, within the period shown, and you have followed the preparation and after-care instructions we gave you. That is the whole test. We do not ask whether you have been "unlucky", and we do not charge a reduced call-out to come back.</p>
<p>Two services carry an extra condition. A <strong>termite chemical management system</strong> stays covered only while it is inspected at least annually, as AS 3660.2:2017 requires (an interval not exceeding 12 months). We remind you when the inspection is due; if it is missed, the promise lapses from the date it fell due. <strong>Flea and bed bug</strong> treatments depend on you completing the vacuuming or two-visit plan, because the chemistry cannot do that part for you.</p>
<h2>What it does not cover</h2>
<ul>
<li>Pests that are not listed on your invoice. A general pest treatment does not cover termites or rodents, and an ant treatment does not cover cockroaches.</li>
<li>New infestations introduced after the treatment, for example bed bugs brought home in luggage or fleas arriving with a new pet.</li>
<li>Areas you asked us not to treat, or that were inaccessible on the day and noted as such on the report.</li>
<li>Damage caused by pests. The promise is to re-treat, not to repair timber or replace goods.</li>
<li>Jobs where the preparation or after-care instructions were not followed, including washing treated surfaces inside the period we advised.</li>
<li>Termite systems that have been breached by building works, landscaping, plumbing leaks or soil disturbance after installation.</li>
<li>Inspections. A timber pest inspection is a snapshot on the day within the limits of AS 4349.3:2010, not a promise about the future.</li>
</ul>
<h2>How to claim</h2>
<p>Call or text <a href="tel:{S['phone_tel']}">{S['phone_display']}</a>, or email <a href="mailto:{S['email']}">{S['email']}</a>, within the re-treatment period on your invoice. Tell us what you are seeing and where; a photo helps. We book the return visit at the next available run, usually within a few days, and re-treat the affected area. There is no form and no fee. Your original treatment record tells us exactly what was applied, so the re-treatment is planned from the ledger, not from memory.</p>
<p>The promise is suspended while an invoice is overdue and resumes once it is paid.</p>
<h2>Why we write it down</h2>
<p>Most operators promise something similar verbally. We put ours in the terms, on the quote and on the invoice because a promise you cannot read is not one you can hold anyone to. It also keeps us honest about what a treatment can do: pest management reduces activity, and pests can re-enter from next door. A written period with clear conditions is the fair way to share that risk.</p>
<div class="callout"><p><strong>Australian Consumer Law.</strong> Our services come with guarantees that cannot be excluded under the Australian Consumer Law, including that they will be provided with due care and skill and be fit for the purpose you told us about. This re-treatment promise is in addition to those rights and does not replace or limit them.</p></div>
<p>Full wording: <a href="/terms">terms and conditions</a>, clauses 5 and 6. Pricing for each service: <a href="/pest-control-prices-perth">pricing guide</a>.</p>""")
    body += c["quote_block"]("Book a treatment that comes with a promise.", "Every quote shows the re-treatment period that applies. Tell us what you are seeing and we'll put it in writing.")
    return {
        "path": "/warranty",
        "title": "Our Re-treatment Promise | DJ Pest Perth",
        "desc": "If the pest we treated is still active inside the treated area within the period on your invoice, we come back at no charge. Periods, conditions and how to claim.",
        "body": body, "crumbs": [("Re-treatment promise", None)],
    }


# ------------------------------------------------------------------ privacy
def privacy(c):
    S = c["SITE"]
    body = _hero(c, "Legal", "Privacy policy.", "How DJ Pest collects, uses, stores and shares your personal information, and how to access it, correct it or complain. Written for the Privacy Act 1988 (Cth) and the Australian Privacy Principles.", actions=False)
    body += _prose(c, f"""<p class="notice">Version 1.0, 18 September 2026. {c['esc'](S['legal_name'])}, ABN {S['abn']}.</p>
<h2>1. Who this policy covers</h2>
<p>This policy applies to personal information collected by DJ Pest Pty Ltd as trustee for the Johns Family Trust ("DJ Pest", "we", "us") through our website, phone, SMS, email, quote and booking forms, and during pest management services at your property. We follow the Australian Privacy Principles (APPs) in the <em>Privacy Act 1988</em> (Cth) as a matter of policy, whether or not we are legally required to in a given year.</p>
<h2>2. What we collect</h2>
<ul>
<li><strong>Identity and contact details:</strong> your name, mobile number, email address and postal or service address.</li>
<li><strong>Property details:</strong> the address, construction type, access notes, the presence of pets, tanks, edible gardens, and any health information you tell us so we can adjust the treatment (for example pregnancy, asthma or chemical sensitivity). Health information is sensitive information and is collected only with your consent, only for that purpose.</li>
<li><strong>Photographs:</strong> of pest activity, damage, entry points and treated areas, taken by you or by us for the report and our records.</li>
<li><strong>Treatment history:</strong> the treatment records required by regulation 77 of the <em>Health (Pesticides) Regulations 2011</em> (WA), quotes, invoices, reports, inspection due dates and correspondence.</li>
<li><strong>Payment details:</strong> handled by our payment processor. We do not store full card numbers.</li>
<li><strong>Website data:</strong> the information you type into a form, and standard server logs (IP address, browser, pages viewed). We do not run advertising trackers.</li>
</ul>
<h2>3. Why we collect it</h2>
<ul>
<li>To identify the pest, quote, book, carry out and document the treatment, and to invoice you.</li>
<li>To meet our legal obligations, in particular to make and keep treatment records for three years as regulation 77 requires, and to respond to the WA Department of Health if asked.</li>
<li>To remind you of a due inspection or follow-up visit, and to honour the re-treatment promise on your invoice.</li>
<li>To send marketing, such as seasonal pest reminders, only if you have opted in (see section 6).</li>
<li>To improve our services and website.</li>
</ul>
<p>If you do not give us the information we ask for, we may not be able to quote or treat safely.</p>
<h2>4. How we collect it</h2>
<p>Directly from you, by phone, SMS, email, our website forms and in person. From a third party only where you have arranged that, for example a property manager, strata company, builder or settlement agent who engages us on your behalf.</p>
<h2>5. Who we share it with</h2>
<p>We do not sell personal information. We share it only as needed to deliver the service:</p>
<ul>
<li><strong>ServiceM8</strong>, our job management and invoicing platform, which stores client, job, photo and treatment record data and sends our booking confirmations and reports. ServiceM8 Pay (Stripe) processes card and PayTo payments.</li>
<li><strong>Google Workspace</strong>, for email, calendars and document storage.</li>
<li>Our website form service, which passes your enquiry to us by email.</li>
<li>Our accountant, insurer or legal adviser where required, and government agencies where the law requires it (for example the WA Department of Health or a court order).</li>
<li>Another licensed pest management technician working under DJ Pest's supervision or subcontract on your job, bound by the same confidentiality.</li>
</ul>
<p><strong>Overseas disclosure.</strong> Our processors are cloud services and may store data on servers outside Australia (Google Workspace, Stripe and ServiceM8 use infrastructure in Australia and other countries). We choose providers that publish their own privacy commitments and security certifications, and we do not otherwise send your information overseas.</p>
<h2>6. Marketing, SMS and email</h2>
<p>We send service messages (booking confirmations, "on the way" texts, reports, invoices, inspection reminders) as part of the job. We send marketing messages, such as seasonal pest reminders, only if you have ticked the consent box on our form or otherwise told us you want them. Every marketing email and SMS includes a working unsubscribe option, and we act on it within five business days, as the <em>Spam Act 2003</em> (Cth) requires. You can also opt out at any time by emailing <a href="mailto:{S['email']}">{S['email']}</a> or replying STOP to a text.</p>
<h2>7. Storage, security and retention</h2>
<p>Information is held in ServiceM8 and Google Workspace behind access limited to DJ Pest staff. Paper is not kept beyond the day of the job. Devices are encrypted and locked.</p>
<p>Treatment records are kept for at least <strong>three years</strong> after the treatment because the <em>Health (Pesticides) Regulations 2011</em> (WA) require it. Financial records are kept for seven years under tax law. Termite management certificates and inspection reports are kept for the life of the system so future inspections can be planned. Other personal information is deleted or de-identified when it is no longer needed for the purpose it was collected for.</p>
<h2>8. Access and correction</h2>
<p>You can ask for a copy of the personal information we hold about you, or ask us to correct it, by emailing <a href="mailto:{S['email']}">{S['email']}</a> or calling <a href="tel:{S['phone_tel']}">{S['phone_display']}</a>. We respond within 30 days and do not charge for access to your own treatment records. If we refuse a request, we tell you why in writing.</p>
<h2>9. Website and cookies</h2>
<p>Our website is static and does not set tracking cookies. Our hosting provider records standard server logs. Website forms send your enquiry to us by email; the form includes a hidden field to filter automated spam and nothing else.</p>
<h2>10. Data breaches</h2>
<p>If personal information we hold is lost or accessed without authority in a way likely to cause serious harm, we will notify you and the Office of the Australian Information Commissioner (OAIC) as the Notifiable Data Breaches scheme requires.</p>
<h2>11. Complaints</h2>
<p>If you think we have mishandled your information, contact us first at <a href="mailto:{S['email']}">{S['email']}</a> or {S['phone_display']}. We acknowledge complaints within five business days and aim to resolve them within 30 days. If you are not satisfied, you can complain to the Office of the Australian Information Commissioner at <a href="https://www.oaic.gov.au" rel="noopener">oaic.gov.au</a> or 1300 363 992.</p>
<h2>12. Contact and changes</h2>
<p>Privacy questions: {c['esc'](S['legal_name'])}, {S['base_suburb']} WA {S['base_postcode']}, <a href="mailto:{S['email']}">{S['email']}</a>, {S['phone_display']}. We may update this policy; the current version is always at djpest.com.au/privacy with its date at the top.</p>
<p>See also: <a href="/terms">terms and conditions</a>.</p>""")
    body += c["quote_block"]()
    return {
        "path": "/privacy",
        "title": "Privacy Policy | DJ Pest",
        "desc": "How DJ Pest collects, uses and stores your personal information under the Privacy Act 1988 and the Australian Privacy Principles, including marketing consent, retention and complaints.",
        "body": body, "crumbs": [("Privacy policy", None)],
    }


# ------------------------------------------------------------------ blog
POSTS = [
    {"slug": "how-to-get-rid-of-ants", "title": "How to get rid of ants (Australian guide, 2026)",
     "desc": "Why spraying makes coastal brown super-colonies worse, how to identify the species, which non-repellent baits work and when to call a licensed Perth pest controller.",
     "img": "/assets/img/blog-ant-food.jpg", "alt": "Ant trail across a kitchen counter, typical foraging behaviour",
     "date": "2026-05-01", "read": "10 minutes", "service": "/ant-control-perth", "service_label": "Ant control Perth"},
    {"slug": "how-to-get-rid-of-cockroaches", "title": "How to get rid of cockroaches (2026 Australian guide)",
     "desc": "Species identification, why spray-and-forget fails on German cockroaches, the gel bait and IGR protocol that works, and when DIY is enough versus when to call a pro.",
     "img": "/assets/img/blog-cockroach-german.jpg", "alt": "German cockroach, small and tan with two dark stripes",
     "date": "2026-05-01", "read": "9 minutes", "service": "/cockroach-control-perth", "service_label": "Cockroach control Perth"},
]


def _post(c, p, lede, content):
    S = c["SITE"]
    body = f'<section class="hero"><div class="wrap"><div>{c["eyebrow"]("Blog · Pest guides")}<h1>{c["esc"](p["title"])}</h1><p class="lead">{lede}</p><p class="notice">Published 1 May 2026 · Reading time {p["read"]} · By DJ Pest</p></div></div></section>'
    body += _prose(c, content + f"""<hr>
<h2>Related</h2>
<ul><li><a href="{p['service']}">{p['service_label']}</a>, the full service and what it costs</li><li><a href="/pest-control-prices-perth">Pest control prices in Perth</a>, every service with a typical range</li><li><a href="/whats-my-pest">What's my pest?</a>, pick what you saw</li><li><a href="/blog">All guides</a></li></ul>""")
    body += c["quote_block"]("Rather have it done properly?", "Tell us what you are seeing and where. Itemised price in writing, no call-out fee.")
    path = f"/blog/{p['slug']}"
    schema = [{
        "@type": "BlogPosting", "@id": DOMAIN + path + "#post", "headline": p["title"], "description": p["desc"],
        "image": [DOMAIN + p["img"]], "datePublished": p["date"], "dateModified": "2026-09-18", "inLanguage": "en-AU",
        "author": {"@id": DOMAIN + "/#business"}, "publisher": {"@id": DOMAIN + "/#business"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": DOMAIN + path}, "about": {"@type": "Service", "name": p["service_label"], "url": DOMAIN + p["service"]}}]
    return {"path": path, "title": p["title"] + " | DJ Pest", "desc": p["desc"], "body": body, "schema": schema,
            "og_image": p["img"], "crumbs": [("Blog", "/blog"), (p["title"].split(" (")[0], None)]}


def blog_index(c):
    cards = "".join(c["card"](p["title"], p["desc"], f"/blog/{p['slug']}", f"Guide · {p['read']}", p["img"], p["alt"], more="Read the guide") for p in POSTS)
    body = _hero(c, "Blog", "Pest guides from a licensed Perth operator.", "What actually works, what doesn't, when DIY is enough and when to call someone. Written by our technicians, second-generation Perth pest controller. No upsells.", actions=False)
    body += c["section"]('<div class="grid grid-2">' + cards + '</div>', "ledger")
    body += _prose(c, """<h2>What these guides are for</h2>
<p>Most pest problems in Perth's northern suburbs start with a wrong identification and a can of spray. These guides are written to fix that: identify the species first, understand why the obvious product fails, then either do it properly yourself or know exactly what to ask a licensed operator for. Every guide names the chemistry class that works, not a brand, and says plainly when a professional is the faster and cheaper route.</p>
<p>New guides are added as the seasons turn. Spring for ants and spiders, summer for termite swarmers, autumn for cockroaches, winter for rodents. If there is a pest you would like covered, <a href="/contact">tell us</a>. For prices, see the <a href="/pest-control-prices-perth">pricing guide</a>; to identify what you saw, try <a href="/whats-my-pest">What's my pest?</a>.</p>""")
    body += c["quote_block"]()
    return {"path": "/blog", "title": "Pest Control Guides | DJ Pest Blog Perth",
            "desc": "Plain-English pest guides from a licensed Perth pest controller: how to get rid of ants and cockroaches, what works, what doesn't, and when to call a pro.",
            "body": body, "crumbs": [("Blog", None)],
            "schema": [{"@type": "Blog", "@id": DOMAIN + "/blog#blog", "name": "DJ Pest guides", "publisher": {"@id": DOMAIN + "/#business"},
                        "blogPost": [{"@id": DOMAIN + "/blog/" + p["slug"] + "#post"} for p in POSTS]}]}


def post_ants(c):
    p = POSTS[0]
    lede = "If you've been spraying for months and there are now more ants than when you started, you're probably making a coastal brown super-colony angry. Here's how to actually get rid of ants: the science, the species ID, the non-obvious \"stop spraying\" rule, and when DIY is enough versus when you need a pro."
    content = f"""<figure><img src="{p['img']}" alt="{p['alt']}" width="1200" height="800" loading="lazy"><figcaption class="notice">An ant trail tells you a lot: species, food preference, entry point, and most importantly, where to place the bait.</figcaption></figure>
<h2>The thing nobody tells you: spraying often makes ants worse.</h2>
<p>Australian homes, particularly anywhere in Perth's beachside suburbs, deal with a species called the coastal brown ant (<em>Pheidole megacephala</em>). It is not your average ant. It forms super-colonies: networks of linked nests that share queens, workers and resources across hundreds of metres. Multiple queens. Multiple nest sites. No inter-nest aggression.</p>
<p>When you hit a super-colony with a repellent spray (almost everything on the hardware shelf is bifenthrin- or permethrin-based), the colony detects the threat and does something called budding. It splits. What was one nest under your patio becomes seven satellite nests scattered across your property within weeks. You then spray those, and they split again. This is why your ant problem keeps getting bigger no matter how much you spray.</p>
<blockquote>If you've sprayed and there are more ants now than there were before, you've probably got a coastal brown super-colony, and the spray is the cause.</blockquote>
<p>The fix isn't more chemistry. It's different chemistry: a class of insecticides called non-repellent transfer baits. The active ingredient (typically fipronil for outdoor liquids and granular baits, hydramethylnon or indoxacarb for indoor gels) is undetectable to ants. They walk through it, carry it back to the colony and feed it to nest-mates and queens. The whole network collapses, not just the workers you can see. This is exactly how our <a href="/ant-control-perth">ant treatment</a> is built.</p>
<h2>Step one: identify the ant species.</h2>
<h3>Coastal brown ant (<em>Pheidole megacephala</em>)</h3>
<p>Small (1.5–2.5 mm), light brown, fast-moving, in trails of dozens to hundreds. Beachside Perth heavy: Hillarys, Sorrento, Mullaloo, Ocean Reef, Kallaroo. Comes inside via paving cracks, lawn margins, garden bed edges. Super-colony forming. Don't spray. Use non-repellent baits along trails.</p>
<h3>White-footed house ant (<em>Technomyrmex</em> spp.)</h3>
<p>Small (2.5–3 mm), dark brown to black, with pale tarsi (feet). Indoor pest: bathrooms and kitchens, attracted to moisture. Sweet liquid baits or gel placed near plumbing entries.</p>
<h3>Sugar ant (<em>Camponotus consobrinus</em>)</h3>
<p>Large (5–15 mm), slow-moving, two-toned (black thorax, lighter gaster), nocturnal. Mostly outdoor, sometimes wanders inside. Sweet-tooth, so sweet liquid baits work well.</p>
<h3>Argentine ant (<em>Linepithema humile</em>)</h3>
<p>Small (2–3 mm), uniformly light brown, super-colony forming like coastal brown but more aggressive towards other ant species. Restricted Perth distribution but expanding. Treatment same as coastal brown.</p>
<h3>Bull ant (<em>Myrmecia</em> spp.)</h3>
<p>Large (10–25 mm), aggressive, painful sting, isolated nests in bushland-adjacent properties. Single nest treatment with a directed liquid product. Not really a "trail" species; they're solitary hunters.</p>
<h2>Step two: the right bait for the species.</h2>
<p>Stop ringing pest controllers and asking "do you have anything stronger than what I bought at the hardware store?". The issue isn't strength, it's chemistry class. There are three things you want from an ant bait:</p>
<ol>
<li><strong>Non-repellent active ingredient</strong>: fipronil, hydramethylnon or indoxacarb. Workers shouldn't be able to detect they're walking on it.</li>
<li><strong>Slow-acting</strong>: a worker that drops dead 30 seconds after picking up bait can't carry it back to the colony. Modern transfer baits take hours to kill, giving the worker time to share with nest-mates.</li>
<li><strong>Right food matrix for the species</strong>: sweet-tooth species (sugar ant) ignore protein baits and vice versa. Coastal brown will take both depending on colony stage.</li>
</ol>
<p>Retail gel baits based on indoxacarb or hydramethylnon work for coastal brown ants indoors. The fipronil liquids that collapse a super-colony outdoors are professional products applied to a label by a licensed technician. Avoid anything labelled "kill-on-contact" or "fast knockdown"; that's repellent chemistry that splits colonies.</p>
<figure><img src="/assets/img/blog-ant-queen.jpg" alt="Ant nest cross-section: the worker carries bait back to feed the queen and the brood" width="1200" height="800" loading="lazy"><figcaption class="notice">The worker you see is doing reconnaissance. The queen and brood are 30 cm to 3 m underground. Bait is the only way to reach them.</figcaption></figure>
<h2>Step three: place the bait correctly.</h2>
<p>Bait placement is at least as important as bait choice. Common mistakes:</p>
<ul>
<li><strong>Don't break the trail.</strong> Place gel next to active trails, not across them. Ants will walk around any disturbance.</li>
<li><strong>Don't combine with spray.</strong> Spraying repellent product over or near non-repellent bait makes the bait detectable. Pick one approach, stick to it for at least four weeks.</li>
<li><strong>Place at the entry point and deep inside.</strong> Inside: under the dishwasher, behind the fridge, in cabinet kickboards. Outside: along paving lines, garden bed edges, lawn margins, wherever you see continuous trails.</li>
<li><strong>Replenish weekly until activity drops.</strong> Ants consume gel quickly when active; a 5 g tube might last four days at peak. Don't ration the bait.</li>
</ul>
<h2>Step four: expect activity to spike for a week.</h2>
<p>This is the bit that sends people back to the spray can. After bait placement, you'll see more ants for 3–7 days, not fewer. They're recruiting nest-mates to the food source. They're carrying it back to the colony. This is the bait working. Trail counts then drop sharply by week two. Full super-colony collapse takes 4–6 weeks.</p>
<p>If you spray at the activity spike, you've reset the whole thing. You've killed the workers carrying bait back to the queens, you've contaminated the bait sites with repellent residue, and the colony splits to escape. Resist.</p>
<h2>What doesn't work (don't bother).</h2>
<ul>
<li><strong>Boiling water on the nest.</strong> For coastal brown super-colonies there is no "the nest"; there are dozens, linked. Boiling water kills a few workers and a tiny fraction of brood at one spot. Adjacent nests carry on.</li>
<li><strong>Vinegar or lemon juice.</strong> Disrupts the pheromone trail temporarily. Doesn't affect colony health. Activity returns within hours.</li>
<li><strong>Baby powder, chalk, cinnamon, peppermint oil.</strong> Same: temporary trail disruption, no colony effect.</li>
<li><strong>"Kill on contact" sprays.</strong> Splits super-colonies. Documented as actively counterproductive for <em>Pheidole</em> species.</li>
<li><strong>Diatomaceous earth.</strong> Works on some species (it's a desiccant that damages the exoskeleton), but coastal brown ants will route around it. Useful supplementary tool, not a primary solution.</li>
</ul>
<h2>When DIY is fine vs when you need a pro.</h2>
<h3>DIY is fine when:</h3>
<ul>
<li>You've correctly ID'd a single small colony (sugar ants, white-footed house ants, a single bull ant nest).</li>
<li>You're using non-repellent bait, you've placed it correctly, and you can wait 2–4 weeks.</li>
<li>The ants are confined to one room or one external area.</li>
</ul>
<h3>Call a licensed pest controller when:</h3>
<ul>
<li>You suspect a coastal brown super-colony covering large parts of your property. These need a coordinated fipronil treatment along every trail and nest entry to collapse properly.</li>
<li>You've baited correctly for four weeks and activity hasn't dropped (that means re-invasion from a neighbouring property, and an annual professional treatment is the realistic answer).</li>
<li>Bull ants near a play area or outdoor entertaining zone. Directed treatment is faster than DIY.</li>
<li>You're in a commercial premises and ant activity is a food-safety risk.</li>
</ul>
<div class="callout"><p>A typical Perth <a href="/ant-control-perth">external ant treatment</a> with a licensed technician runs $250–$400 for a standard property, uses fipronil outdoors and gel indoors where needed, and carries a three-month <a href="/warranty">re-treatment period</a>. Every figure is on the <a href="/pest-control-prices-perth">pricing guide</a>.</p></div>
<h2>Common Perth-specific questions.</h2>
<h3>Why are coastal brown ants so common in Perth?</h3>
<p>Sandy soil (great for nest-building), mild climate (year-round breeding), and <em>Pheidole megacephala</em>'s general invasive success. Beachside suburbs are particularly heavy because the species thrives in the lawn-paving-garden interface that Perth landscapes favour. It's basically the perfect environment for them.</p>
<h3>Will I ever fully be rid of them?</h3>
<p>Honest answer: probably not for good. A good treatment plus sealing entry points plus good hygiene gets you 6–12 months clear. Re-invasion from neighbouring properties is realistic in chronic-pressure beachside zones. An annual treatment is the maintenance approach most Perth homes settle into.</p>
<h3>Are baits a risk to my dog?</h3>
<p>Every product is applied at its label rate and the label sets the placement. Bait stations are tamper-resistant. Indoor gels go inside cabinetry where dogs can't reach, and pets stay out of treated areas until the re-entry period has passed. We brief on placements as part of any professional job.</p>
<h3>What about ants in my plants and lawn?</h3>
<p>Ants in lawns are usually doing more good than harm: they aerate soil and predate other pests. Treat them only if they're a nuisance or actively coming inside. Garden bed edges along paving lines are common coastal brown nest entries; treat those with granular outdoor bait.</p>"""
    return _post(c, p, lede, content)


def post_cockroaches(c):
    p = POSTS[1]
    lede = "Species ID first, then the chemistry that fits. Why spray-and-forget fails on German cockroaches, the seven-step protocol that works, what doesn't, and when a licensed operator is the faster route."
    content = f"""<figure><img src="{p['img']}" alt="{p['alt']}" width="1200" height="800" loading="lazy"><figcaption class="notice">German cockroach: the small one with two dark stripes that lives in your kitchen.</figcaption></figure>
<h2>Step one: which cockroach do you actually have?</h2>
<h3>German cockroach (<em>Blattella germanica</em>)</h3>
<p>Small (12–15 mm), tan to light brown with two dark stripes running down the back. Lives indoors in warm, humid voids: kitchens, bathrooms, behind fridges, inside microwaves, under dishwashers. This is the one you have to take seriously. They breed fast (one female produces 30–40 nymphs per egg case, 4–8 cases over a 200-day life), they hide in voids you can't reach, and they develop chemical resistance quickly. If you've sprayed and they keep coming back, this is probably your species.</p>
<h3>American cockroach (<em>Periplaneta americana</em>)</h3>
<p>Large (35–40 mm), reddish-brown, fast-moving, sometimes flies. Lives in drains, sub-floors, sewer systems and outside in mulch beds. They come up through the floor wastes at night looking for water and food. Less of a breeding-population problem than Germans; usually individual incursions from a sewer or sub-floor source. Treatment focus is the source, not the kitchen.</p>
<h3>Australian cockroach (<em>Periplaneta australasiae</em>)</h3>
<p>Similar size to American but with distinctive yellow markings on the wings and pronotum. Outdoor preferring: wood piles, garden mulch, garage corners. Less commonly an indoor breeding problem; usually they wander in and you spot one on the way to the kitchen. External harbourage clean-up plus a perimeter treatment solves this one.</p>
<blockquote>If you don't ID the species first, you're throwing money at the wrong product.</blockquote>
<h2>Why "spray and forget" doesn't work.</h2>
<p>Here's the problem with reaching for an aerosol: it kills a small fraction of your cockroach population, the adults that are out walking around when you spray. The rest are inside wall voids, behind appliances, inside hatching egg cases (oothecae), and in places aerosols don't reach. They breed back faster than the survivors die.</p>
<p>German cockroaches in particular have what entomologists call insecticide resistance. Sites that have been hit with the same active ingredient (typically pyrethroids: bifenthrin, permethrin) repeatedly often have populations that no longer respond to it. Modern professional treatment rotates active ingredients and combines them with insect growth regulators (IGRs), which prevent juveniles from maturing into reproductive adults. That breaks the cycle even if some adults survive. It is the basis of our <a href="/cockroach-control-perth">German cockroach kitchen program</a>.</p>
<h2>What actually works (the 7-step protocol).</h2>
<ol>
<li><strong>ID the species.</strong> See above. Don't skip this.</li>
<li><strong>Place 3–5 sticky monitor traps</strong> in corners of the kitchen, behind the fridge, under the sink, in the pantry and bathroom. Leave them three days. The catch tells you where the harbourage zones are and roughly how many you're dealing with.</li>
<li><strong>Apply gel bait inside cabinetry voids and behind appliances.</strong> Gel bait (active ingredients such as hydramethylnon, fipronil, indoxacarb or imidacloprid) placed as 3–5 mm dots. Never on food-preparation surfaces. Replace every 2–4 weeks until traps are catching nothing.</li>
<li><strong>Add an IGR (insect growth regulator).</strong> Pyriproxyfen or hydroprene in liquid or aerosol, applied along wall-floor junctions of the kitchen and bathroom per the label. Keeps working 90-plus days.</li>
<li><strong>Fix the why.</strong> Repair leaking taps, store food in sealed containers, take out rubbish daily, vacuum behind appliances weekly. Cockroaches need food and water. Remove either and you cripple them.</li>
<li><strong>Seal entry points.</strong> Caulk gaps around plumbing, pipe penetrations, weep holes wider than 6 mm, gaps between cabinetry and wall. Pay particular attention to where the dishwasher hose enters cabinetry, sink waste pipes, and around the back of the fridge.</li>
<li><strong>Re-monitor at 14 days.</strong> Re-deploy the sticky traps. Catch should be down 80 per cent or more from baseline. If not, you've missed a harbourage zone; reset and find it (usually inside an appliance you didn't pull out).</li>
</ol>
<figure><img src="/assets/img/blog-cockroach-trap.jpg" alt="Sticky monitor trap used to identify cockroach activity zones" width="1200" height="800" loading="lazy"><figcaption class="notice">Sticky monitor traps cost a few dollars and are the single best DIY tool for understanding where your cockroach activity actually is.</figcaption></figure>
<h2>What doesn't work (don't waste your money).</h2>
<ul>
<li><strong>Boric acid alone.</strong> It works on cockroaches that walk through it, but they groom obsessively and avoid heavy dustings. Useful as part of a multi-tool approach, useless on its own.</li>
<li><strong>Aerosol "kill on contact" sprays.</strong> See above: kills the few in the open, scatters the rest deeper into voids.</li>
<li><strong>Bay leaves, cucumber peel, peppermint oil.</strong> All popular on social media. None of them have any meaningful effect on a real infestation.</li>
<li><strong>Bug bombs and foggers.</strong> Push cockroaches into wall voids where they breed back. Considered actively counterproductive by most professional pest controllers.</li>
<li><strong>Ultrasonic repellers.</strong> No scientific evidence they work. Consumer tests have shown no effect on cockroach populations.</li>
</ul>
<h2>When DIY is fine, and when you need a pro.</h2>
<h3>DIY is fine when:</h3>
<ul>
<li>You've spotted 1–3 cockroaches over a few weeks and sticky traps are catching fewer than five over three days.</li>
<li>It's an American or Australian (large outdoor type); you mostly need to fix the entry point and treat the source.</li>
<li>You're in a stand-alone house with no shared walls.</li>
<li>You're catching them, but it's manageable and you're seeing decline.</li>
</ul>
<h3>Call a licensed pest controller when:</h3>
<ul>
<li>You're seeing cockroaches during the day. Cockroaches are nocturnal; daytime sightings mean the population is large enough to spill out of harbourage.</li>
<li>You're in an apartment or townhouse. German cockroaches travel between units through wall cavities, and uncoordinated treatment usually fails.</li>
<li>You've treated multiple times yourself and they keep returning.</li>
<li>You run a commercial kitchen, café or food premises; there are regulatory implications for an active infestation.</li>
<li>You have very young children or immunocompromised family members. Cockroach allergens are documented asthma triggers.</li>
</ul>
<div class="callout"><p>A typical Perth <a href="/cockroach-control-perth">German cockroach kitchen program</a> with a licensed technician runs $250–$450 depending on severity, includes an IGR (which DIY products often don't) and a follow-up visit, and carries a six-month <a href="/warranty">re-treatment period</a>. See the <a href="/pest-control-prices-perth">pricing guide</a>. That's not always cheaper than a determined DIY effort, but it's almost always faster and more reliable.</p></div>
<h2>Common questions Perth homeowners ask.</h2>
<h3>Are cockroaches dangerous?</h3>
<p>They don't bite. They are, however, mechanical vectors of <em>Salmonella</em>, <em>E. coli</em> and <em>Staphylococcus</em>. They walk through drains and refuse, then across food preparation surfaces. Their droppings and shed skins are documented asthma and allergy triggers, particularly in kids. The food safety implications are why commercial kitchens are under regulatory pressure to maintain ongoing pest programs.</p>
<h3>Why do I see them in a "clean" house?</h3>
<p>Cleanliness reduces opportunity, but a single dripping tap and a neighbour with an active population is enough. Don't beat yourself up; German cockroaches are a coordination problem more than a cleanliness problem.</p>
<h3>Will one treatment fix it forever?</h3>
<p>For most small-to-medium infestations, one professional treatment plus IGR plus your follow-up hygiene is enough to clear the active population for 6–12 months. For apartments or chronic-pressure properties (food premises, old plumbing), an ongoing quarterly program is realistic. Anyone promising "completely gone forever" from a single visit is selling, not treating.</p>
<h3>What about gel baits around pets and kids?</h3>
<p>Gels are applied at the label rate and placed inside cabinetry voids and behind appliances where pets and kids can't reach. People and pets stay out of treated areas until the re-entry period has passed. We brief on placements as part of any professional job.</p>"""
    return _post(c, p, lede, content)


def pages(c):
    return [pricing(c), whats_my_pest(c), about(c), contact(c), terms(c), warranty(c), privacy(c), blog_index(c), post_ants(c), post_cockroaches(c)]
