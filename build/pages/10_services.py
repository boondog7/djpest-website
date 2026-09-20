"""Services hub + seven service pages."""

DOMAIN = "https://djpest.com.au"

PRICES = {
    "general": (250, 350), "ant": (250, 400), "cockroach": (250, 450), "rodent": (220, 380), "rodent_follow": (90, 140),
    "spider": (220, 300), "inspection": (250, 350), "prepurchase": (300, 400), "chem": (2500, 5500), "bait": (1500, 3000), "wasp": (180, 280), "mosquito": (220, 320), "bee": (250, 400), "comm_visit": (140, 380), "comm_cleanout": (350, 650),
}

def money(lo, hi): return f"${lo:,}–${hi:,}"

def service_schema(name, lo, hi, desc):
    return {"@type": "Service", "serviceType": name, "name": name + " Perth", "description": desc,
            "provider": {"@id": DOMAIN + "/#business"},
            "areaServed": {"@type": "Place", "name": "Perth northern suburbs, Western Australia"},
            "offers": {"@type": "Offer", "priceCurrency": "AUD", "price": lo,
                       "priceSpecification": {"@type": "PriceSpecification", "minPrice": lo, "maxPrice": hi, "priceCurrency": "AUD"}}}

PRICE_NOTE = ('<p class="notice">Typical range, GST inclusive. Every job is quoted itemised in writing before we start. '
              'No call-out fee, no deposit, seven-day payment terms. See the full <a href="/pest-control-prices-perth">pricing guide</a>.</p>')


def pages(c):
    S = c["SITE"]; esc = c["esc"]; icon = c["icon"]; sec = c["section"]; eb = c["eyebrow"]; card = c["card"]
    steps = c["steps"]; faq = c["faq"]; faq_schema = c["faq_schema"]; ledger = c["ledger_table"]; quote = c["quote_block"]

    def hero(eyebrow, h1, lead, trust, art=None):
        art_html = art or ""
        return f"""<section class="hero"><div class="wrap">
<div>
  {eb(eyebrow)}
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  {c['hours_cue']()}<div class="actions">{c['btn_call']()}{c['btn_quote']()}</div>
  <ul class="trust">{"".join(f"<li>{esc(t)}</li>" for t in trust)}</ul>
</div>
{art_html}
</div></section>"""

    def art_img(src, alt):
        return f'<div class="hero-art"><img src="{src}" alt="{esc(alt)}" width="440" height="440" fetchpriority="high" style="width:100%;height:100%;object-fit:cover;border-radius:var(--r);border:1px solid var(--line)"></div>'

    def art_card(title, items):
        lis = "".join(f'<li style="display:flex;gap:.6rem;align-items:flex-start;margin:.5rem 0">{icon("check")}<span>{i}</span></li>' for i in items)
        return f'<div class="card" style="align-self:center"><div class="num">{esc(title)}</div><ul style="list-style:none;padding:0;margin:0;color:var(--ink-2)">{lis}</ul></div>'

    def head(h2, lead=None):
        lead_html = f'<p class="lead">{lead}</p>' if lead else ""
        return f'<div class="section-head"><h2>{h2}</h2>{lead_html}</div>'

    def included(items):
        return '<div class="grid grid-3">' + "".join(card(t, d) for t, d in items) + "</div>"

    def prep(items):
        return '<div class="prose"><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"

    def related(links):
        return '<p class="prose" style="margin-top:2rem">Related: ' + " · ".join(f'<a href="{h}">{esc(t)}</a>' for t, h in links) + "</p>"

    def crumbs(name): return [("Services", "/services"), (name, None)]

    out = []

    # ================================================================ /services hub
    hub_cards = '<div class="grid grid-3">' + "".join([
        card("Termite inspection", "A full AS 4349.3 timber pest inspection: roof void, sub-floor, interior, exterior and the yard. Photos, moisture readings and a written report you can act on.", "/termite-inspection-perth", "01 / Termites"),
        card("Termite treatment", "Non-repellent chemical management systems installed to AS 3660.2, or baiting and monitoring where the construction suits it. Certificate issued, annual inspection scheduled.", "/termite-treatment-perth", "02 / Termites"),
        card("General pest treatment", "Cockroaches, spiders, silverfish and ants in one internal and external treatment. Non-staining products indoors. Six-month re-treatment promise.", "/general-pest-control-perth", "03 / General"),
        card("Ant control", "Coastal brown ant super-colonies need slow-acting non-repellents and baits, not a repellent spray that splits the colony. We treat the colony, not the trail.", "/ant-control-perth", "04 / Ants"),
        card("Cockroach control", "German cockroaches in the kitchen or Australian cockroaches from the garden. Gel bait, insect growth regulator and drain treatment where the species calls for it.", "/cockroach-control-perth", "05 / Cockroaches"),
        card("Rodent control", "Species identified, entry points mapped, tamper-resistant stations placed, and a sealing plan so the roof void stays quiet.", "/rodent-control-perth", "06 / Rodents"),
        card("Spider control", "Redbacks, white-tails and black house spiders. Web removal, retic-box check and a residual treatment of eaves, weep holes and fence lines.", "/spider-control-perth", "07 / Spiders"),
        card("Mosquito control", "Breeding-site audit of the yard, then a residual treatment of the shaded harbourages where adults rest. Timed for Perth's warm-season peak.", "/mosquito-control-perth", "08 / Mosquitoes"),
        card("Vacate flea treatment", "End-of-lease flea treatment quoted from the address within the hour, same-week slot, certificate to you and the agent within the hour of treatment.", "/flea-treatment-perth", "09 / Fleas"),
        card("Wasp removal", "Paper wasp nests under eaves, pergolas and in hedges: found, treated, removed and the site treated so the next queen moves on. Suspected European wasps are reported to DPIRD, not treated.", "/wasp-removal-perth", "10 / Wasps"),
        card("Bee removal", "Swarm on a branch? A beekeeper collects it alive and we give you the number. Hive in a wall or roof void? Evening treatment, entry sealed, comb-removal and proofing plan.", "/bee-removal-perth", "11 / Bees"),
        card("Commercial pest control", "Cafes, strata, childcare, aged care, warehouses and offices. Numbered stations on a site map, same-day service reports and a site folder your auditor can read.", "/commercial-pest-control-perth", "12 / Commercial"),
    ]) + "</div>"

    pricing = sec(eb("How we price") + head("One method for every job.",
        "DJ Pest is run by a Chartered Accountant, and the quoting habits come with that: a written, itemised price before anything is booked, no call-out fee, no deposit, and a seven-day invoice that matches the quote.") +
        steps([
            ("Look, then price", "We inspect first. Where the pest is, how established it is, and what construction we are working with. If you do not need a treatment, we say so."),
            ("Itemised in writing", "Product, areas treated, number of stations or metres of perimeter, follow-up visits and the re-treatment period that applies. Prices include GST."),
            ("Invoice matches quote", "No surprises on the invoice. If we find something on the day that changes the scope, we stop and talk to you before doing it."),
        ]), "ledger")

    rt_rows = [[esc(k), esc(v)] for k, v in S["retreat_periods"].items()]
    retreat = sec(eb("Re-treatment promise") + head("What happens if they come back.",
        "If the pest named on your invoice is still active in the treated area inside the period below, we return and re-treat at no charge. It is written into our <a href=\"/terms\">terms</a>, not a slogan.") +
        ledger(["Service", "Re-treatment period"], rt_rows) +
        '<p class="notice">Periods apply to the pest and areas named on your invoice. Conditions are set out in full on the <a href="/warranty">re-treatment promise</a> page.</p>')

    hub_faqs = [
        ("Which service do I need if I am not sure what the pest is?", "Text a photo of the pest, the droppings or the damage to 0447 747 769 and we will identify it and tell you which treatment applies. Our <a href=\"/whats-my-pest\">What's my pest?</a> page covers the common Perth suspects."),
        ("Can I combine services on one visit?", "Yes. A general pest treatment already covers cockroaches, spiders, silverfish and nuisance ants. Rodent stations, a termite inspection or an external ant program can be added to the same visit and itemised on one quote."),
        ("Do you charge a call-out fee?", "No. Inspections that lead to a quote are free within our northern-suburbs service area. A stand-alone timber pest inspection with a written AS 4349.3 report is a priced service because the report itself is the product."),
        ("Are the prices on this site fixed?", "They are typical ranges for a standard three-bedroom home in Perth's northern suburbs. Every job is quoted itemised in writing after we have seen it, and the invoice matches the quote."),
        ("What do I receive after the job?", "A treatment report by email: where the pests were getting in, exactly what was applied and where, the re-entry period, and a prevention plan. It doubles as the record WA regulations require us to keep for three years."),
        ("Which suburbs do you cover?", f"We are based in Warwick and cover {', '.join(S['service_area'][:10])} and the rest of the northern corridor. See the <a href=\"/service-areas\">service areas</a> page."),
    ]

    hub_body = hero("Services · Perth's northern suburbs",
                    "Twelve pest problems.<br>One <em class=\"red\">documented</em> way of fixing them.",
                    "Diagnosed first, treated with the right chemistry for the pest and the site, then written up. Every product is APVMA-registered and applied to its label, and every job carries a re-treatment period you can read before you book.",
                    ["Licensed technicians", f"In Perth pest control since {S['family_since']}", "Itemised quotes", "Treatment report after every job"],
                    art_card("Every job includes", ["Inspection before any product is opened", "Written, itemised price. No call-out fee, no deposit", "Re-entry period explained before treatment", "Treatment report and prevention plan by email", "Re-treatment promise on the invoice"])) + \
        sec(eb("What we treat") + head("Choose the pest. We handle the rest.") + hub_cards, "ledger") + pricing + retreat + \
        sec(eb("Perth pest calendar") + head("When each pest is active in the northern suburbs.") + c["season_strip"]()) + \
        sec(eb("Questions") + head("Straight answers.") + faq(hub_faqs), "ledger") + \
        quote("Not sure which service? Start here.", "Tell us what you are seeing and where. We will identify it, tell you which treatment applies, and send an itemised price. No obligation.")

    out.append({"path": "/services", "title": "Pest Control Services Perth Northern Suburbs | DJ Pest",
                "desc": "Termite inspections and treatment, general pest, ants, cockroaches, rodents and spiders across Perth's northern suburbs. Licensed, itemised, documented.",
                "body": hub_body, "schema": [faq_schema(hub_faqs)], "crumbs": [("Services", None)]})

    # ================================================================ /termite-inspection-perth
    ti_faqs = [
        ("How often should a Perth home be inspected for termites?", "AS 3660.2 recommends inspections at intervals not exceeding 12 months, and more often where the risk is higher. In the northern suburbs, a house with a garden bed against the wall, timber retaining, a paved-over inspection zone or a nearby bush reserve sits in the higher-risk bracket. Annual is the sensible default."),
        ("What is the difference between a termite inspection and a pre-purchase timber pest inspection?", "The inspection method is the same and both follow AS 4349.3. A pre-purchase inspection is written for someone who does not yet own the property, so the report gives more weight to the limitations, the areas we could not access and the conducive conditions a buyer would want to negotiate on. It is priced slightly higher because the report is longer and usually needed within a short settlement window."),
        ("Can you tell me if there are termites inside the walls?", "Not with certainty, and no inspector can. AS 4349.3 is a visual inspection of accessible areas, backed by moisture readings and sounding of timbers. We report evidence of activity, evidence of past damage and the conditions that make an attack more likely. Where readings suggest something behind a surface, we tell you and recommend an invasive inspection with the owner's consent."),
        ("Do I need to be home?", "It helps. We need access to the roof void manhole, the sub-floor where there is one, every room, the garage and the yard, and we like to walk you through the findings before we leave. If you cannot be there, arrange access and we will call you afterwards."),
        ("How long does the inspection take?", "Sixty to ninety minutes for a typical single-storey home on a standard block, longer for two-storey homes, large sheds, heavy landscaping or a sub-floor. We do not rush an inspection to fit more into a day."),
        ("What if you find live termites?", "We show you, photograph them and identify the species. We do not disturb the workings, because that makes them harder to treat. You receive the report with a treatment recommendation and an itemised price for a <a href=\"/termite-treatment-perth\">management system</a>. There is no obligation to have us do the treatment."),
        ("Is the inspection priced in writing?", f"Yes. A standard timber pest inspection with report is typically {money(*PRICES['inspection'])} and a pre-purchase inspection {money(*PRICES['prepurchase'])}, GST inclusive. We confirm the price before booking based on the size of the property and construction."),
    ]
    ti_body = hero("Termite inspection · AS 4349.3:2010",
                   "Termite inspection Perth.<br>Every accessible timber, <em class=\"red\">documented</em>.",
                   "A full timber pest inspection to AS 4349.3, from roof void to fence line, with photos, moisture readings and a written report that tells you what we found, what we could not see, and what to do next.",
                   ["Licensed technicians", "AS 4349.3 report", f"Typical {money(*PRICES['inspection'])}", "60–90 minutes on site"],
                   art_card("Inspected on every visit", ["Roof void and ceiling timbers", "Sub-floor where one exists", "Every internal room, skirting, architraves and frames", "External walls, weep holes, slab edge and paving", "Fences, retaining walls, sheds, trees and stumps to 50 m", "Moisture readings and sounding of timbers"])) + \
        sec('<div class="prose">'
            '<h2>Why an inspection comes first</h2>'
            '<p>Subterranean termites do not announce themselves. By the time a skirting board sounds hollow or a door frame gives under a thumb, the colony has usually been feeding for months. Perth\'s northern suburbs give them everything they need: warm sandy soil that is easy to tunnel, garden beds built against brick, timber retaining walls, and a swarm season that runs from November to April.</p>'
            '<p>An inspection is the only way to know where you stand. It is also the first step of every treatment. AS 3660.2 requires a thorough inspection before a management system is designed, and any quote you receive without one is a guess. We inspect, report, and only then price a treatment if one is needed.</p>'
            '<h2>What is inspected</h2>'
            '<p>The inspection follows AS 4349.3:2010, the Australian Standard for timber pest inspections of buildings. It is a visual inspection of accessible areas, supported by instruments. On a typical northern-suburbs home we cover:</p>'
            '<ul><li><strong>Roof void.</strong> Entered where the manhole and clearance allow. We check rafters, battens, ceiling joists, wall plates and the tops of internal walls for mud leads, damage and moisture.</li>'
            '<li><strong>Sub-floor.</strong> Timber-floored homes in older parts of Duncraig, Sorrento and Carine have crawl spaces. We inspect bearers, joists, stumps, piers and ant caps, and note ventilation and drainage.</li>'
            '<li><strong>Interior.</strong> Every room. Skirtings, architraves, door and window frames, built-in cupboards, wet-area timbers and any exposed structural timber. Timbers are sounded with a tapping tool and read with a moisture meter where the surface allows.</li>'
            '<li><strong>Exterior.</strong> Slab edge and weep holes, wall-to-ground contact, paving and garden beds against walls, timber decks, pergolas, garages and carports, sheds, external stairs.</li>'
            '<li><strong>Grounds.</strong> Fences, retaining walls, sleepers, tree stumps, timber stored on the ground and trees within 50 metres of the building, where they are on the property.</li></ul>'
            '<p>We photograph evidence and points of interest as we go. The photos go into the report, not a filing cabinet.</p>'
            '<h2>The limitations, stated plainly</h2>'
            '<p>AS 4349.3 is a visual inspection. It cannot see inside a wall cavity, under a fixed floor covering, behind stored goods, under a concrete slab or inside a timber. We do not move furniture or stored items, lift carpet or open walls. Where clearance in a roof void or sub-floor is too low, or an area is unsafe, we say so in the report rather than pretend we saw it.</p>'
            '<div class="callout"><p>The report lists every area that was not accessible and why. If an inaccessible area worries you, we can arrange an invasive inspection with the owner\'s written consent, priced separately.</p></div>'
            '<p>Moisture readings and sounding raise the odds of finding concealed activity but do not remove the possibility. A clear report means no evidence was found in the accessible areas on the day. It is not a statement about the future, which is why the Standard recommends inspections at intervals not exceeding 12 months.</p>'
            '<h2>What the report contains</h2>'
            '<ul><li>Property description, construction type, date and weather, and who was present.</li>'
            '<li>Areas inspected and areas not accessible, with the reason for each.</li>'
            '<li>Evidence of live subterranean termites, with species where identifiable and photographs.</li>'
            '<li>Evidence of previous termite activity or damage, and whether it appears to have been treated.</li>'
            '<li>Evidence of borers, timber decay (fungal rot) and, where relevant, other timber pests.</li>'
            '<li>Conducive conditions: moisture, drainage, timber-to-ground contact, garden beds bridging the slab edge, stored timber, leaking taps and air-conditioner drains.</li>'
            '<li>Any existing termite management system, its condition and whether it is being maintained.</li>'
            '<li>Recommendations, in order of priority, with an indicative cost where treatment or repairs are advised.</li></ul>'
            '<p>The report is emailed as a PDF, usually the same day. We keep a copy for three years as the Health (Pesticides) Regulations 2011 require of treatment records, and longer for our own files.</p>'
            '<h2>Risk factors in Perth\'s northern suburbs</h2>'
            '<p>The northern corridor is not one environment. The coastal strip from Sorrento to Yanchep sits on deep Spearwood and Quindalup sands: free-draining, warm and easy for termites to tunnel through. Further inland, the limestone ridge suburbs such as Greenwood, Warwick and Kingsley carry pockets of shallow limestone that push moisture and termite activity toward the slab edge. Both are active termite country.</p>'
            '<p>Housing stock matters as much as soil. Brick-and-tile homes from the 1970s and 1980s in Duncraig, Padbury and Warwick often have decades of garden build-up against the walls, timber pergolas added later and no maintained chemical barrier. Newer estates in Alkimos, Butler and Clarkson generally have a physical or chemical system installed at construction, but it only remains effective if it is inspected and not bridged by paving, a new deck or a raised garden bed.</p>'
            '<p>Then there is the bush. Yellagonga Regional Park, Warwick Bushland, Star Swamp, the Neerabup reserves and dozens of smaller pockets keep a standing population of <em>Coptotermes acinaciformis</em>, the species behind most structural damage in Perth. If your property backs onto or sits within a few streets of reserve bush, we treat it as elevated risk and say so.</p>'
            '<h2>Pre-purchase timber pest inspections</h2>'
            '<p>Buying in the northern suburbs? A pre-purchase timber pest inspection follows the same AS 4349.3 method but is written for a buyer. It leans harder on limitations, on what could not be accessed with the current owner\'s furniture and stored goods in place, and on the conducive conditions you would want to fix or negotiate on. We can usually inspect within two to three business days and report the same day, which suits a standard WA settlement timeline.</p>'
            '<p>We do not do the building inspection. If your building inspector also offers a timber pest report, ask whether it is a separate AS 4349.3 report by a licensed pest management technician. Ours is.</p>'
            '</div>') + \
        sec(eb("What it costs") + head("Priced before booking.") +
            ledger(["Inspection", "Typical range", "Includes"], [
                ["Timber pest inspection (AS 4349.3)", money(*PRICES['inspection']), "Full inspection, moisture readings, photos, PDF report, same-day"],
                ["Pre-purchase timber pest inspection", money(*PRICES['prepurchase']), "As above, buyer-focused report, priority booking for settlement"],
                ["Annual inspection for a DJ Pest management system", "Quoted with the system", "Keeps the AS 3660.2 certificate current"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("The report is the product.") + included([
            ("A written AS 4349.3 report", "Findings, photos, moisture readings, areas not accessed, conducive conditions and prioritised recommendations. Emailed as a PDF, usually same day."),
            ("A straight recommendation", "If we find nothing, we say so. If we find activity, we explain the options and price a management system separately. No pressure either way."),
            ("A reminder before it lapses", "Inspections have no re-treatment period. We diarise your next 12-month inspection and remind you before it is due."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Ten minutes of prep gets a better inspection.") + prep([
            "Clear access to the roof manhole. Move anything stored in a cupboard below it.",
            "Open the sub-floor access door or hatch if the home has one.",
            "Pull stored items back from the garage walls and shed walls where you can.",
            "Unlock side gates and sheds. Note where the retic control boxes are.",
            "Tell us about any past termite treatment, damage or repairs you know of, and where.",
            "Keep pets inside or secured. Nothing is sprayed during an inspection, but we open a lot of doors.",
        ]) + related([("Termite treatment", "/termite-treatment-perth"), ("Pricing guide", "/pest-control-prices-perth"), ("Termite blog posts", "/blog")]), "ledger") + \
        sec(eb("Questions") + head("Termite inspection FAQ.") + faq(ti_faqs)) + \
        quote("Book a termite inspection.", "Tell us the suburb, the age of the house and whether it is for peace of mind, a suspected problem or a purchase. We will confirm a price and a time.")
    out.append({"path": "/termite-inspection-perth", "title": "Termite Inspection Perth | AS 4349.3 Timber Pest Reports | DJ Pest",
                "desc": f"AS 4349.3 termite inspections across Perth's northern suburbs. Roof void, sub-floor, interior and grounds. Same-day report. Typical {money(*PRICES['inspection'])}.",
                "body": ti_body, "crumbs": crumbs("Termite inspection"),
                "schema": [service_schema("Termite inspection", PRICES['inspection'][0], PRICES['prepurchase'][1], "Timber pest inspection to AS 4349.3:2010 with written report."), faq_schema(ti_faqs)]})

    # ================================================================ /termite-treatment-perth
    tt_faqs = [
        ("Do you need to inspect before quoting a termite treatment?", "Yes. AS 3660.2 requires an inspection before a management system is designed, and we cannot price a perimeter we have not measured or a construction type we have not seen. If you already have a current AS 4349.3 report from another licensed technician we can work from it, but we still walk the site before quoting."),
        ("Chemical system or baiting: which is better?", "Neither, in general. A non-repellent chemical treated zone gives faster, continuous protection and suits most northern-suburbs brick homes on a slab. Baiting suits sites where trenching or drilling is impractical, where the owner wants to avoid soil treatment, or where live activity needs to be eliminated first. Often we recommend a chemical system with a small number of monitoring stations as a check. We explain the reasoning on your quote."),
        ("Will a treatment kill the nest?", "A non-repellent treated zone is designed so that foraging termites pass through it, pick up the active and transfer it through the colony. Field results are strong, but the colony may be a hundred metres away under a neighbour's yard and cannot be located or confirmed. The system protects the building; the annual inspection confirms it is still doing so."),
        ("Why is the annual inspection a condition of the certificate?", "Because a treated zone can be breached: a new garden bed, paving laid over the slab edge, a deck footing, a plumber's trench. Chemicals also degrade over time. AS 3660.2 sets an inspection interval not exceeding 12 months for this reason, and our re-treatment promise on the system is conditional on those inspections being carried out."),
        ("How long does the treatment take, and do we need to leave?", "A full perimeter chemical system on a single-storey home takes most of a day. You can stay home. Kids and pets stay away from the treated zone until it is complete and any re-entry period we advise has passed. Baiting installations take two to three hours."),
        ("What does a termite treatment cost in Perth?", f"A non-repellent chemical management system typically runs {money(*PRICES['chem'])} depending on perimeter length, construction and how much drilling is needed. A baiting and monitoring system typically runs {money(*PRICES['bait'])} to install, plus scheduled monitoring visits. Every system is quoted itemised in writing after inspection."),
        ("Do you use physical barriers?", "Physical systems such as stainless mesh or graded stone are installed at construction and are not something we retrofit. For existing homes, the options are a chemical treated zone, a baiting and monitoring system, or a combination."),
    ]
    tt_body = hero("Termite treatment · AS 3660.2:2017",
                   "Termite treatment Perth.<br>Designed for your house, <em class=\"red\">certified</em> in writing.",
                   "Non-repellent chemical management systems and baiting programs installed to AS 3660.2 by a licensed technician. Inspected first, quoted itemised, certificate issued, annual inspection scheduled.",
                   ["Licensed technicians", "AS 3660.2 certificate", "Non-repellent chemistry", "Annual inspection scheduled"],
                   art_card("How a treatment runs", ["AS 4349.3 inspection first, always", "System designed to the construction and soil", "Itemised quote: metres, drill points, product, follow-ups", "Installed to label and to the Standard", "Certificate and site plan issued", "12-month inspection diarised"])) + \
        sec('<div class="prose">'
            '<h2>What a termite management system is</h2>'
            '<p>The Australian Standard for termite management in existing buildings, AS 3660.2:2017, does not talk about "barriers". It talks about management systems: a designed set of measures that reduce the risk of concealed termite entry to the building and make any entry detectable at the next inspection. The distinction matters. Nothing stops termites. A well-designed system makes them either die trying or show themselves where an inspector will see them.</p>'
            '<p>For existing homes in Perth\'s northern suburbs there are two families of system, and a good treatment is often one with a little of the other.</p>'
            '<h2>Non-repellent chemical treated zones</h2>'
            '<p>A continuous treated zone of soil is created around and, where needed, beneath the building. Where soil is exposed, a trench is dug against the footing to the required depth, flooded with the product at label rate and backfilled with treated soil. Where the perimeter is covered by paving, a concrete path, a patio slab or a garage floor, holes are drilled at close spacing and the product is injected beneath, then the holes are plugged. Slab penetrations, piers and pipe entries are treated individually.</p>'
            '<p>We use non-repellent actives such as fipronil. Termites cannot detect a non-repellent zone, so they tunnel through it, pick up the active on their bodies and transfer it through the colony by contact and grooming. Repellent products work differently: termites sense them and go around, which sounds helpful until they find the one gap the repellent did not reach. That is why we do not use repellent chemistry for termite work and never mix a repellent and a non-repellent in the same zone.</p>'
            '<div class="callout"><p>Every drill hole, trench section and litre applied is recorded on the site plan that comes with your certificate. It is the same ledger discipline we apply to every job, and it is what the next inspector will want to see.</p></div>'
            '<h2>Baiting and monitoring systems</h2>'
            '<p>In-ground stations are installed at intervals around the building and checked on a schedule. When termites are found feeding in a station, a bait containing a slow-acting insect growth regulator replaces the timber. Workers carry it back to the colony, where it disrupts moulting. Over weeks the colony declines and, in the better outcomes, is eliminated.</p>'
            '<p>Baiting is slower than a chemical zone and depends on termites finding the stations, but it has real advantages: no soil treatment, minimal disturbance to paving, and a direct path to the colony when there is live activity. On homes with a treated zone that cannot be made continuous, a small set of monitoring stations across the gap is often the honest answer.</p>'
            '<h2>How we choose between them</h2>'
            '<ul><li><strong>Live activity in the house.</strong> We usually bait the active workings first, or apply a non-repellent directly to them, then install the perimeter system once the colony pressure drops. Disturbing active termites with a repellent sends them elsewhere in the building.</li>'
            '<li><strong>Construction.</strong> A slab-on-ground brick veneer home with an accessible perimeter suits a chemical zone. A timber-floored home with a sub-floor gets a sub-floor treatment as well. Extensions, split slabs and pavers laid to the wall increase drilling and can tip the balance toward baiting.</li>'
            '<li><strong>Soil and water.</strong> Coastal sands drain fast and take product well. Limestone pockets in Greenwood, Warwick and Kingsley need more drilling. Sites near bores, wells or a soakwell that discharges to a waterway need label setbacks respected, which sometimes rules out soil treatment along one side.</li>'
            '<li><strong>Your preferences.</strong> Some owners want no soil chemical near a vegetable garden or a bore. We design around it and say plainly what that does to the level of protection.</li></ul>'
            '<p>The decision and the reasons are written on the quote, not delivered as a verdict.</p>'
            '<h2>The annual inspection condition</h2>'
            '<p>AS 3660.2 sets an inspection interval not exceeding 12 months for every management system, and more frequent inspections where the risk is high. This is not a sales device. A treated zone is only as good as its weakest point, and the weakest point is usually created after installation: a raised garden bed bridging the slab edge, a new deck footing punched through the zone, a trench for a retic line. The annual inspection finds those breaches and finds any termite entry while it is still a small repair.</p>'
            '<p>Our re-treatment promise on a termite management system is set out on your AS 3660.2 certificate and is conditional on the annual inspections being carried out. Miss one and the promise lapses. We remind you before each is due and price it with the system so there is no surprise.</p>'
            '<h2>What the certificate covers</h2>'
            '<ul><li>The type of system installed and the product used, with its APVMA registration and the rate applied.</li>'
            '<li>A site plan showing treated zones, drill lines, bait or monitoring station positions and any areas that could not be treated, with the reason.</li>'
            '<li>The date of installation, the licensed technician who installed it and our WA business registration.</li>'
            '<li>The inspection interval and the conditions of the re-treatment promise.</li>'
            '<li>Durable notice details for the meter box as the Standard requires, so the next owner or tradesperson knows a system is in place.</li></ul>'
            '<p>The treatment record is kept for three years as the Health (Pesticides) Regulations 2011 (WA) require. If you sell the house, the certificate and site plan go to the buyer and save everyone an argument.</p>'
            '</div>') + \
        sec(eb("What it costs") + head("Two systems, both itemised.") +
            ledger(["System", "Typical range", "What drives the price"], [
                ["Non-repellent chemical management system", money(*PRICES['chem']), "Perimeter length, drilling through paving or concrete, sub-floor, extensions"],
                ["Baiting and monitoring system (install)", money(*PRICES['bait']), "Number of stations, plus scheduled monitoring visits priced separately"],
                ["Treatment of live activity (spot)", "Quoted on inspection", "Extent of workings, access, product"],
                ["Annual AS 3660.2 inspection", "Quoted with the system", "Keeps the certificate and re-treatment promise current"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("Paperwork that follows the house.") + included([
            ("AS 3660.2 certificate and site plan", "System type, product, rate, treated zones, drill lines, station positions and exclusions. The document a buyer's inspector will ask for."),
            ("Treatment record", "Product, active constituent, rate, litres, areas treated, re-entry period and technician. Kept three years under WA regulations and emailed to you."),
            ("Re-treatment promise, conditional", "If termites breach the system during the period on your certificate and the annual inspections have been kept, we re-treat the breach at no charge."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Before installation day.") + prep([
            "Clear at least a metre of access along every external wall: pots, furniture, firewood, bins.",
            "Locate and mark retic lines and control boxes near the walls. We trench carefully, but a plan helps.",
            "Tell us about bores, soakwells, rainwater tanks and vegetable beds. Label setbacks apply.",
            "Unlock side gates, sheds and garages. Move cars out of the garage if the floor is to be drilled.",
            "Keep pets inside for the day. Kids and pets stay out of the treated zone until the re-entry period we advise has passed.",
            "Have a plan for the meter box notice. We fit it on the day.",
        ]) + related([("Termite inspection", "/termite-inspection-perth"), ("Pricing guide", "/pest-control-prices-perth"), ("Service areas", "/service-areas")]), "ledger") + \
        sec(eb("Questions") + head("Termite treatment FAQ.") + faq(tt_faqs)) + \
        quote("Get a termite treatment priced properly.", "Tell us what has been found and where. We will inspect, design the system to the house and send an itemised price with the reasoning written down.")
    out.append({"path": "/termite-treatment-perth", "title": "Termite Treatment Perth | AS 3660.2 Management Systems | DJ Pest",
                "desc": f"Termite treatment for Perth's northern suburbs: non-repellent chemical systems and baiting to AS 3660.2, certificate issued. Typical {money(*PRICES['chem'])}.",
                "body": tt_body, "crumbs": crumbs("Termite treatment"),
                "schema": [service_schema("Termite treatment", PRICES['bait'][0], PRICES['chem'][1], "Termite management systems installed to AS 3660.2:2017."), faq_schema(tt_faqs)]})

    # ================================================================ /general-pest-control-perth
    gp_faqs = [
        ("What pests does a general pest treatment cover?", "Cockroaches (German, American and Australian), spiders including redbacks and black house spiders, silverfish and nuisance ants around the home. It does not cover termites, rodents, fleas, bed bugs or wasps, which are separate treatments with their own re-treatment periods. Ant super-colonies get an <a href=\"/ant-control-perth\">external ant program</a> on top."),
        ("How long do we need to stay out of the house?", "Until treated surfaces are dry, usually around two hours for the products we use indoors. We confirm the exact re-entry period for the product before we start. Kids and pets stay out until it has passed."),
        ("Do you spray inside every room?", "Only where it is needed. Indoors we use non-staining, low-odour products and gel baits, targeted at skirting lines, wet areas, kitchen voids and entry points. We do not fog whole rooms or spray food-preparation surfaces, bedding or toys."),
        ("How often should a Perth home be treated?", "Once a year suits most northern-suburbs homes, timed for spring before ants and spiders wake up or autumn before cockroaches move indoors. Homes backing onto bush, with heavy garden cover, or with a history of German cockroaches may benefit from six-monthly visits. We tell you which applies, not the other way round."),
        ("What is the six-month promise?", "If cockroaches, spiders, silverfish or ants named on your invoice are still active inside the treated areas within six months of the treatment, we return and re-treat at no charge. Full conditions on the <a href=\"/warranty\">re-treatment promise</a> page."),
        ("What does general pest control cost in Perth?", f"A typical three-bedroom home, internal and external, runs {money(*PRICES['general'])} GST inclusive. Larger homes, two storeys, heavy infestations or add-ons such as rodent stations are itemised on the quote."),
        ("Will one treatment fix a German cockroach problem?", "Not always. German cockroaches breed fast and live inside voids. A general treatment includes gel and an insect growth regulator in the kitchen, and that is often enough for a light problem. For an established infestation we recommend the <a href=\"/cockroach-control-perth\">dedicated kitchen program</a> with a follow-up visit."),
    ]
    gp_body = hero("General pest treatment · internal + external",
                   "General pest control Perth.<br>One visit, inside and out, <em class=\"red\">six-month promise</em>.",
                   "Cockroaches, spiders, silverfish and ants treated in one itemised visit. Non-staining products indoors, a residual treatment outside, and a written record of what went where.",
                   ["Licensed technicians", "6-month re-treatment promise", f"Typical {money(*PRICES['general'])}", "Around 90 minutes on site"],
                   art_card("Covered in one visit", ["German, American and Australian cockroaches", "Redbacks, black house and other spiders", "Silverfish", "Nuisance ants around the home", "Internal skirtings, wet areas, kitchen voids", "External perimeter, eaves, weep holes, fences"])) + \
        sec(eb("Signs you need it") + head("What a northern-suburbs home looks like before we visit.") + '<div class="prose"><ul>'
            '<li>Cockroaches in the kitchen at night, or small brown ones inside cupboards and behind the fridge.</li>'
            '<li>Webs re-forming at window frames and eaves within days of brushing them down.</li>'
            '<li>A redback under the outdoor furniture, the pool coping or in the retic box.</li>'
            '<li>Silverfish in the linen cupboard, bookshelves or bathroom.</li>'
            '<li>Ant trails along the kitchen bench or the bathroom skirting after rain.</li>'
            '<li>It has been more than a year since the last treatment, or you have just moved in.</li></ul></div>', "ledger") + \
        sec(eb("How we treat it") + head("Three parts to every general treatment.") + steps([
            ("Walk-through and identification", "We look before we spray. Which species, where they are harbouring, where they are getting in. We photograph findings and confirm the scope and price with you before opening a product."),
            ("Inside: targeted, non-staining", "Skirting lines, wet areas, behind appliances, wardrobes and the roof void entry are treated with a non-staining, low-odour residual. Kitchens get gel bait and an insect growth regulator in the voids rather than spray on benches."),
            ("Outside: the residual perimeter", "Eaves, weep holes, window and door frames, fence lines, garage, patio and sub-floor vents are treated with a residual product. Webs are brushed down first so spiders re-establish on treated surfaces. Retic boxes are checked for redbacks."),
        ])) + \
        sec(eb("What it costs") + head("Typical range for a three-bedroom home.") +
            ledger(["Treatment", "Typical range", "Includes"], [
                ["General pest, internal + external", money(*PRICES['general']), "All areas above, gel and IGR in kitchen, treatment report, 6-month promise"],
                ["External only", "Quoted", "Perimeter, eaves, fences, retic check. Suits rentals and pre-summer top-ups"],
                ["Add rodent stations", f"From ${PRICES['rodent'][0]} as a stand-alone", "See the rodent page; itemised on the same quote"],
                ["Add external ant program", money(*PRICES['ant']), "For coastal brown super-colonies; 3-month promise"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("The paperwork nobody else gives you.") + included([
            ("Treatment report", "Where pests were harbouring and entering, what was applied and where, re-entry period, and a prevention plan for you. Emailed after the job."),
            ("Treatment record", "Product, active constituent, rate and areas, kept for three years as WA regulations require. Yours on request at any time."),
            ("Six-month re-treatment promise", "If the pests on your invoice are back inside the treated areas within six months, we return at no charge."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Prep checklist.") + prep([
            "Clear benches and put away food, pet bowls, chopping boards and dish racks.",
            "Pull items back from wet-area skirtings and the kitchen kickboards where you can. We do not move furniture.",
            "Cover or remove fish tanks and bird cages. Tell us about reptiles and other sensitive pets.",
            "Strip beds if you have asked for a bedroom treatment. Otherwise bedrooms are skirting-only.",
            "Unlock side gates, sheds and the garage. Point out retic boxes and any redback sightings.",
            "Plan to be out of treated rooms until surfaces are dry, around two hours. We confirm the re-entry period before we start.",
        ]) + related([("Cockroach control", "/cockroach-control-perth"), ("Spider control", "/spider-control-perth"), ("Ant control", "/ant-control-perth"), ("Pricing guide", "/pest-control-prices-perth")]), "ledger") + \
        sec(eb("Questions") + head("General pest FAQ.") + faq(gp_faqs)) + \
        quote("Book a general pest treatment.", "Tell us the suburb, the size of the home and what you have been seeing. We will send an itemised price and a time.")
    out.append({"path": "/general-pest-control-perth", "title": "General Pest Control Perth | Internal + External Treatment | DJ Pest",
                "desc": f"General pest treatment for Perth's northern suburbs: cockroaches, spiders, silverfish and ants, inside and out. Six-month promise. Typical {money(*PRICES['general'])}.",
                "body": gp_body, "crumbs": crumbs("General pest treatment"),
                "schema": [service_schema("General pest treatment", *PRICES['general'], "Internal and external general pest treatment with six-month re-treatment promise."), faq_schema(gp_faqs)]})

    # ================================================================ /ant-control-perth
    ant_faqs = [
        ("Why has spraying made my ant problem worse?", "Because you are probably dealing with a coastal brown ant super-colony. Repellent sprays, including the supermarket ant killers and bifenthrin perimeter sprays, trigger budding: the colony splits into satellite nests to escape the threat. One nest under the patio becomes several across the yard within weeks. The fix is a slow-acting non-repellent such as fipronil, or a bait, that workers do not detect and carry back to the queens."),
        ("How long does ant baiting take to work?", "Expect more ants for the first three to seven days as workers recruit nest-mates to the bait. That is the bait working. Activity drops sharply by the second week. Full collapse of a super-colony typically takes four to six weeks. Small, localised colonies clear in one to two weeks."),
        ("What is a coastal brown ant super-colony?", "Coastal brown ants (<em>Pheidole megacephala</em>) form linked networks of nests that share queens, workers and food across hundreds of metres, with no aggression between nests. In the northern suburbs they thrive in sandy soil, paving joints, garden-bed edges and lawn margins, and they are heaviest along the coast from Hillarys to Mindarie. You cannot find the nest because there are dozens."),
        ("Can you treat ants in the kitchen?", "Yes. Indoors we use gel bait placed inside cabinetry, behind appliances and along the hinge side of kickboards, away from food-contact surfaces. We do not spray kitchen interiors with a residual for ants; gel is more effective and keeps product off benches."),
        ("What about kids and pets during an ant treatment?", "Gel placements go where fingers and paws do not reach. External non-repellent treatment is applied to soil, paving joints and nest zones at label rate. Kids and pets stay off treated areas until the re-entry period we advise has passed, usually once surfaces are dry."),
        ("Will the ants come back?", "Coastal brown ants re-invade from neighbouring properties, so pressure never drops to zero on the coast. Our external ant program carries a three-month re-treatment promise on the treated zones. For properties with chronic pressure, an annual spring top-up is realistic and we say so rather than sell a quarterly plan."),
        ("Which ant species are common in Perth's northern suburbs?", "Coastal brown ant (super-colonies, the most common call), white-footed house ant (kitchens and bathrooms, moisture-seeking), sugar ant (large, slow, sweet feeders, mostly outdoors), Argentine ant (an invasive super-colony species restricted to some Perth zones), and bull ants near bushland. The species decides the chemistry, which is why we identify first."),
    ]
    ant_body = hero("Ant control · coastal brown super-colonies",
                    "Ant control Perth.<br>We treat the <em class=\"red\">colony</em>, not the trail.",
                    "Months of spraying and more ants than when you started? That is a coastal brown super-colony, and repellent spray makes it split. We use slow-acting non-repellents and baits that workers carry home.",
                    ["Licensed technicians", "3-month re-treatment promise", f"Typical {money(*PRICES['ant'])}", "Species identified first"],
                    art_img("/assets/img/ant-closeup.jpg", "Close-up of a brown ant on a pale surface, illustrative image")) + \
        sec(eb("Signs you have a super-colony") + head("Why most Perth ant treatments fail.") + '<div class="prose">'
            '<p>Perth\'s biggest ant problem is the coastal brown ant, <em>Pheidole megacephala</em>. It forms super-colonies: networks of linked nests that share queens, workers and food across hundreds of metres. Hit them with a repellent spray and the colony detects the threat and buds, splitting into satellite nests to escape. What was one nest under the patio becomes several across the property in weeks.</p>'
            '<ul><li>Fine sandy mounds along paving joints, lawn edges and garden beds that reappear after rain or watering.</li>'
            '<li>Trails that shift to a new spot every time you spray.</li>'
            '<li>Ants in the kitchen or bathroom after wet weather, following moisture and food.</li>'
            '<li>Two sizes of worker on the same trail, small workers and larger big-headed soldiers.</li>'
            '<li>Heaviest along the coastal strip: Hillarys, Sorrento, Mullaloo, Ocean Reef, Mindarie, Quinns Rocks.</li></ul>'
            '<p>Not every ant is a coastal brown. White-footed house ants live in kitchens and bathrooms and need gel, not soil treatment. Sugar ants are large, slow and mostly outdoors. Bull ants near bush reserves have single nests that can be treated directly. We identify before we open a product, because the wrong chemistry on the wrong species is the reason the last treatment did not hold.</p></div>', "ledger") + \
        sec(eb("How we treat it") + head("Slow-acting, non-repellent, carried home.") + steps([
            ("Identify and map", "Species, trail direction, nest zones, entry points into the house and the moisture sources drawing them in. We photograph the map for your report."),
            ("Non-repellent external treatment", "A slow-acting non-repellent such as fipronil is applied at label rate to nest zones, paving joints, lawn margins and the perimeter. Workers walk through it undetected, groom it and transfer it through the colony. Never mixed with a repellent in the same zone."),
            ("Gel inside, then prevention", "Indoors, gel bait goes inside cabinetry and behind appliances, away from food-contact surfaces. We note the leaking tap, the pet bowl and the mulch against the wall that keep them coming, and put it in writing."),
        ])) + \
        sec(eb("What it costs") + head("Typical ranges.") +
            ledger(["Treatment", "Typical range", "Includes"], [
                ["External ant program (whole property)", money(*PRICES['ant']), "Identification, non-repellent treatment of nest zones and perimeter, gel indoors, report, 3-month promise"],
                ["Ants within a general pest treatment", money(*PRICES['general']), "Nuisance ants around the home; super-colonies need the program above"],
                ["Bull ant nest (single nest)", "Quoted", "Direct nest treatment, usually near bushland"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("Treatment report", "Species, nest map, products and rates applied, re-entry period and a prevention plan for the moisture and food sources drawing them in."),
            ("Treatment record", "Kept three years under the Health (Pesticides) Regulations 2011 and yours on request."),
            ("Three-month re-treatment promise", "If active trails return to the treated zones within three months, we come back at no charge."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Before we arrive.") + prep([
            "Stop spraying. Repellent spray in the week before treatment scatters the colony and hides the trails we need to see.",
            "Leave the trails alone. We want to see where they run.",
            "Put away food, pet bowls and bins, and wipe benches.",
            "Turn retic off the night before so soil treatments are not flushed.",
            "Unlock side gates and note where the worst mounds are.",
            "Kids and pets stay off treated soil and paving until the re-entry period we advise has passed.",
        ]) + related([("General pest treatment", "/general-pest-control-perth"), ("Pricing guide", "/pest-control-prices-perth"), ("Ant blog posts", "/blog")]), "ledger") + \
        sec(eb("Questions") + head("Ant control FAQ.") + faq(ant_faqs)) + \
        quote("Get the ants treated properly.", "Tell us the suburb and where the trails run. Text a photo if you can. We will identify the species and send an itemised price.")
    out.append({"path": "/ant-control-perth", "title": "Ant Control Perth | Coastal Brown Ant Super-Colony Treatment | DJ Pest",
                "desc": f"Ant control for Perth's northern suburbs. Coastal brown super-colonies treated with non-repellents and baits, not repellent spray. Typical {money(*PRICES['ant'])}.",
                "body": ant_body, "crumbs": crumbs("Ant control"),
                "schema": [service_schema("Ant control", *PRICES['ant'], "External ant treatment for coastal brown super-colonies using non-repellent products and baits."), faq_schema(ant_faqs)]})

    # ================================================================ /cockroach-control-perth
    ck_faqs = [
        ("What kind of cockroach do I have?", "German cockroaches are small, 12 to 15 mm, tan with two dark stripes behind the head, and live indoors in kitchens, bathrooms and warm appliances. American cockroaches are large, 35 to 40 mm, reddish-brown and fast, and come up from drains, sewers and sub-floors. Australian cockroaches are a similar size with yellow edges on the wings and breed outdoors in mulch, wood piles and garden beds. Text us a photo and we will tell you."),
        ("Why does spraying on its own not work?", "Spray kills the cockroaches that are out walking. The rest are inside wall voids, behind appliances and inside egg cases, and they breed back faster than the survivors die. Gel bait reaches the ones in the voids, and an insect growth regulator stops juveniles maturing into breeding adults. The spray is the smallest part of a proper treatment."),
        ("How long until they are gone?", "German cockroach activity usually falls away over two to three weeks as the gel and growth regulator work through the population. Drain-based American and Australian jobs clear faster because we can treat the breeding site directly. Established German infestations get a scheduled follow-up visit, which is included in the kitchen program."),
        ("Are the baits placed near food?", "Gel is placed inside cabinetry voids, behind and under appliances, on the hinge side of doors and in kickboard gaps, away from food-contact surfaces. We do not spray inside kitchen cupboards or on benches. You get a list of placements with your report."),
        ("Do you treat cockroaches in apartments and units?", "Yes, with a caveat. German cockroaches move between units through shared walls and plumbing. If only your unit is treated, re-infestation from next door is likely. Strata-coordinated treatment is the best outcome; failing that we treat your unit thoroughly, seal the penetrations we can reach and set expectations honestly."),
        ("What does cockroach treatment cost in Perth?", f"A German cockroach kitchen program, including gel, growth regulator, a targeted residual and a follow-up visit, typically runs {money(*PRICES['cockroach'])}. Light cockroach activity is covered within a <a href=\"/general-pest-control-perth\">general pest treatment</a> at {money(*PRICES['general'])}."),
        ("Are cockroaches actually a health issue?", "They do not bite, but they walk through drains and refuse, then across food-preparation surfaces, carrying bacteria with them, and their droppings and shed skins are a recognised asthma trigger. That is why food businesses run continuous cockroach programs and why we treat the breeding sites, not just the visible adults."),
    ]
    ck_body = hero("Cockroach control · German, American, Australian",
                   "Cockroach control Perth.<br>Break the <em class=\"red\">breeding cycle</em>, not just the ones you see.",
                   "Saw one cockroach? There are more. We identify the species, place gel bait and an insect growth regulator where they breed, treat the drains if that is the source, and follow up. No spray on your benches.",
                   ["Licensed technicians", "Gel + IGR method", f"Typical {money(*PRICES['cockroach'])}", "Follow-up included on kitchen programs"],
                   art_img("/assets/img/cockroach-closeup.jpg", "Close-up of a cockroach on a dark surface, illustrative image")) + \
        sec(eb("Signs you have cockroaches") + head("Three species, three different treatments.") + '<div class="prose">'
            '<p>Almost every cockroach call in Perth\'s northern suburbs is one of three species, and they do not respond to the same treatment.</p>'
            '<ul><li><strong>German cockroach</strong> (<em>Blattella germanica</em>): small, tan, two dark stripes. Lives in warm, humid voids near food and water: behind the fridge, under the dishwasher, in the pantry kickboards. One female produces dozens of offspring per egg case and carries several cases over her life. This is the indoor infestation species.</li>'
            '<li><strong>American cockroach</strong> (<em>Periplaneta americana</em>): large, reddish-brown, flies clumsily into the kitchen late at night. Lives in drains, sewers, sub-floors and the gap behind the dishwasher where the drain pipe enters the wall.</li>'
            '<li><strong>Australian cockroach</strong> (<em>Periplaneta australasiae</em>): similar size to the American with yellow wing edges. Breeds outdoors in mulch, compost, wood piles and under pavers, and wanders in through gaps under doors and weep holes.</li></ul>'
            '<p>Signs: droppings like coarse ground pepper inside cupboards, brown smear marks along the top of cupboard doors, a musty smell in the pantry, egg cases behind appliances, and adults seen in daylight, which means the harbourages are full. Perth\'s mild winters mean there is no seasonal die-off. Autumn is when they move indoors.</p></div>', "ledger") + \
        sec(eb("How we treat it") + head("Gel, growth regulator, drains, then a follow-up.") + steps([
            ("Identify the species and the harbourages", "German jobs are cabinetry gel and growth regulator. American jobs are drain treatment and penetrations. Australian jobs are external harbourage clean-up and a perimeter. We inspect with a torch and a flushing agent to find where they are living, then confirm the plan and price."),
            ("Gel bait and insect growth regulator", "Gel placements go inside cabinetry voids, behind and under appliances and on hinge sides, away from food-contact surfaces. An insect growth regulator is applied to the voids so juveniles cannot mature into breeding adults. Indoors we use non-staining products only. Actives are rotated to avoid resistance."),
            ("Drains, perimeter and follow-up", "Floor wastes, sub-floor cavities and external drain pits are treated for drain-breeding species and pipe penetrations sealed where we can. A residual goes on the external perimeter, not inside the kitchen. Kitchen programs include a scheduled follow-up to check placements and re-apply."),
        ])) + \
        sec(eb("What it costs") + head("Typical ranges.") +
            ledger(["Treatment", "Typical range", "Includes"], [
                ["German cockroach kitchen program", money(*PRICES['cockroach']), "Inspection, gel, growth regulator, targeted residual, follow-up visit, report, 6-month promise"],
                ["Cockroaches within a general pest treatment", money(*PRICES['general']), "Light activity; gel and growth regulator in the kitchen plus external perimeter"],
                ["Drain treatment (American cockroach)", "Quoted", "Floor wastes, sub-floor, external pits, penetrations"],
                ["Food premises program", "Quoted", "Scheduled visits with records suitable for a food safety audit"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("Treatment report", "Species, harbourages found, every gel placement listed, products and rates, re-entry period, and the sanitation and sealing plan that keeps them out."),
            ("Treatment record", "Kept three years under WA regulations. For food businesses, formatted for your audit file."),
            ("Six-month re-treatment promise", "Cockroaches named on your invoice still active inside the treated areas within six months? We return at no charge."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Before we arrive.") + prep([
            "Do not spray or bomb the kitchen beforehand. Repellent aerosols scatter cockroaches away from the gel and hide the harbourages.",
            "Empty the cupboards under the sink and next to the stove. Pull the fridge and dishwasher out if you can do so safely; otherwise we will.",
            "Clear benches, put away food and pet bowls, and empty the bin.",
            "Fix or report dripping taps and leaking dishwasher hoses. Water is the reason they chose your kitchen.",
            "Tell us about anyone in the home with asthma or chemical sensitivity so we can adjust the plan.",
            "Kids and pets stay out of treated rooms until surfaces are dry and the re-entry period we advise has passed.",
        ]) + related([("General pest treatment", "/general-pest-control-perth"), ("Pricing guide", "/pest-control-prices-perth"), ("Cockroach blog posts", "/blog")]), "ledger") + \
        sec(eb("Questions") + head("Cockroach control FAQ.") + faq(ck_faqs)) + \
        quote("Get the cockroaches treated at the source.", "Tell us where you are seeing them and when. A photo helps us identify the species before we arrive. Itemised price, no obligation.")
    out.append({"path": "/cockroach-control-perth", "title": "Cockroach Control Perth | German Cockroach Gel + IGR Program | DJ Pest",
                "desc": f"Cockroach control for Perth's northern suburbs. German, American and Australian species treated with gel bait and growth regulator. Typical {money(*PRICES['cockroach'])}.",
                "body": ck_body, "crumbs": crumbs("Cockroach control"),
                "schema": [service_schema("Cockroach control", *PRICES['cockroach'], "Cockroach treatment using gel bait, insect growth regulator and targeted residual, with follow-up."), faq_schema(ck_faqs)]})

    # ================================================================ /spider-control-perth
    sp_faqs = [
        ("Are redbacks dangerous in Perth?", "A redback bite is a medical matter: severe local pain, sweating, nausea and sometimes muscle pain, with children and older people most at risk. Deaths have been extremely rare since antivenom became available. If bitten, apply ice, do not apply a pressure bandage, and get to an emergency department. Reducing the chance of a bite is the point of treating the places they hide."),
        ("Where do redbacks hide around a Perth home?", "Under coping on pavers, retaining walls and pool edges, inside reticulation valve boxes, under stored items in the shed, behind outdoor furniture, in roller-door rails and under the rims of unused pots. They like dry, sheltered, undisturbed spots and rarely come inside on their own. The retic box is the single most common bite scenario in the northern suburbs: someone reaches in blind."),
        ("What about white-tail spiders?", "White-tails are wandering indoor hunters, most active on summer evenings. They do not build webs; they hunt other spiders. A bite can cause local pain and minor irritation. The long-running claim that they cause necrotic ulcers has not been supported by Australian clinical research. Unpleasant, not destructive."),
        ("Are huntsman spiders dangerous?", "No. They are large and alarming but not medically significant, and they eat cockroaches. We do not target huntsmen specifically. A general spider treatment affects them incidentally, but if a huntsman in the shed is your only complaint, we will tell you to save your money."),
        ("Will treatment stop spiders for good?", "No, and be wary of anyone who says it will. Spiders walk in from neighbouring properties and balloon in on the wind. A residual treatment affects spiders that cross treated surfaces while it remains active. Spider treatment inside a general pest visit carries a six-month re-treatment promise on the treated areas. Annual pre-summer treatment suits most homes."),
        ("When is the best time to treat spiders in Perth?", "October to December is peak activity: the most webs, the most wandering males and the most new redback nests. A treatment in spring sets the property up for summer. Properties backing onto bush or with a lot of retic boxes and hard landscaping benefit most."),
        ("What about kids and pets during a spider treatment?", "Residual products are applied to external surfaces, eaves, weep holes, fence lines and sub-floor vents at label rate. Kids and pets stay off treated surfaces until they are dry and the re-entry period we advise has passed, usually around two hours. Pets should not lick treated surfaces in that window."),
    ]
    sp_body = hero("Spider control · redbacks, white-tails, black house spiders",
                   "Spider control Perth.<br>The retic box gets checked <em class=\"red\">every time</em>.",
                   "Two kinds of northern-suburbs household: those who have found a redback in the retic box, and those who are about to. Webs removed, harbourages treated, redback hotspots opened and photographed.",
                   ["Licensed technicians", "Included in general pest", f"Stand-alone {money(*PRICES['spider'])}", "Retic-box check on every job"],
                   art_img("/assets/img/spider-redback.jpg", "Redback spider showing the red hourglass marking, illustrative image")) + \
        sec(eb("Signs and species") + head("The spiders that actually matter in Perth.") + '<div class="prose">'
            '<p>Of the dozens of species in a northern-suburbs garden, only the redback (<em>Latrodectus hasselti</em>) is a genuine medical concern, with the white-tail a distant and overstated second. The rest are alarming, harmless or actively useful.</p>'
            '<ul><li><strong>Redback.</strong> Outdoors, in dry sheltered spots: under coping, inside retic valve boxes, under shed clutter, behind outdoor furniture, in roller-door rails. Peak summer. Rarely enters the house unaided.</li>'
            '<li><strong>White-tail</strong> (<em>Lampona</em> spp.). Indoor wanderer on summer evenings, hunts other spiders, found in bedding and towels left on the floor. Mild bite.</li>'
            '<li><strong>Black house spider</strong> (<em>Badumna insignis</em>). The messy funnel webs in window frames, eaves and fence corners. Mild bite, very common.</li>'
            '<li><strong>Huntsman</strong> and <strong>wolf spiders</strong>. Large, fast, harmless. Huntsmen eat cockroaches. Wolf spiders live in lawns and bush edges.</li>'
            '<li><strong>Daddy-long-legs.</strong> Eats other spiders. Leave them.</li></ul>'
            '<p>Signs: webs re-forming at eaves and window frames within days, a tangled web with a small hanging retreat under outdoor furniture or pool coping, and egg sacs, round and papery, in the retic box lid.</p></div>', "ledger") + \
        sec(eb("How we treat it") + head("Webs down, harbourages treated, hotspots opened.") + steps([
            ("Web removal first", "A treated surface only matters if the spider walks across it. Existing webs come down with a brush before anything is applied, so spiders re-establish on fresh treated surfaces, not on old silk."),
            ("Residual treatment of harbourage zones", "Eaves and gutter lines, weep holes, window and door frames, fence lines, sub-floor vents, garage corners, under coping on patios and pool surrounds, and the outside of sheds. Spiders pick the residual up on their legs and groom it in."),
            ("Retic boxes and inside", "Every visible retic valve box is opened, any redback photographed, and the lid and surrounds treated. Indoors, white-tail treatment is a targeted skirting and wardrobe-margin application with a non-staining product, only where it is warranted."),
        ])) + \
        sec(eb("What it costs") + head("Typical ranges.") +
            ledger(["Treatment", "Typical range", "Includes"], [
                ["Spiders within a general pest treatment", money(*PRICES['general']), "All external zones above plus internal treatment; 6-month promise"],
                ["Stand-alone spider treatment", money(*PRICES['spider']), "External harbourage treatment, web removal, retic-box check, report"],
                ["Annual pre-summer spider treatment", money(*PRICES['spider']), "Same scope, timed October to December"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("Treatment report", "Species found, every retic box and hotspot checked with photos, products and rates, re-entry period and a list of the clutter and coping that needs attention."),
            ("Treatment record", "Kept three years under WA regulations, yours on request."),
            ("Re-treatment promise", "Six months when spiders are treated as part of a general pest visit. Conditions on the <a href=\"/warranty\">promise</a> page."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Before we arrive.") + prep([
            "Leave webs in place. They show us where the spiders are.",
            "Move outdoor furniture, pots and stored items a little away from walls and coping so we can treat behind them.",
            "Tell us where the retic boxes are, and about any redback sightings.",
            "Bring washing in and close windows on the treated sides for the visit.",
            "Cover fish ponds and outdoor tanks. Tell us about reptiles, birds and chickens.",
            "Kids and pets stay off treated surfaces until dry and the re-entry period we advise has passed.",
        ]) + related([("General pest treatment", "/general-pest-control-perth"), ("Pricing guide", "/pest-control-prices-perth"), ("Spider blog posts", "/blog")]), "ledger") + \
        sec(eb("Questions") + head("Spider control FAQ.") + faq(sp_faqs)) + \
        quote("Get the redback hotspots dealt with.", "Tell us the suburb, what you have seen and where. We will send an itemised price and a time, and we will check every retic box.")
    out.append({"path": "/spider-control-perth", "title": "Spider Control Perth | Redback and White-Tail Treatment | DJ Pest",
                "desc": f"Spider control for Perth's northern suburbs. Redbacks and white-tails: webs removed, eaves treated, every retic box checked. Stand-alone {money(*PRICES['spider'])}.",
                "body": sp_body, "crumbs": crumbs("Spider control"),
                "schema": [service_schema("Spider control", *PRICES['spider'], "External spider treatment with web removal and retic-box redback check."), faq_schema(sp_faqs)]})

    # ================================================================ /rodent-control-perth
    ro_faqs = [
        ("How do I tell if I have rats or mice?", "Rats leave droppings 8 to 12 mm long, gnaw holes the size of a 50-cent coin and thump across the roof void at night. Mice leave rice-grain droppings of 3 to 6 mm, gnaw smaller holes and scurry. Black rats, the usual northern-suburbs roof invader, are climbers; Norway rats are ground and sub-floor animals. Treatment differs, so we identify first."),
        ("How long until the rats are gone?", "Most domestic jobs settle within two to three weeks. Rats are neophobic: they avoid new objects in their territory for several days, so a station that looks untouched at day five is normal, not a failure. Mice usually feed within a day or two. The follow-up visit checks consumption and repositions stations along the runs."),
        ("Is baiting a risk to pets and kids?", "Baits go only in locked, tamper-resistant stations anchored in place and positioned where children and pets cannot reach the block. Inside the house, where pets or kids are present, we prefer snap traps in covered boxes to avoid a pet catching a poisoned rodent. Every placement is listed on your report and we brief you on what to watch for."),
        ("Will they come back?", "Almost every re-infestation is an unsealed entry point. A rat needs a gap about the size of a 20-cent coin; a mouse gets through a gap the width of a pen. We map every gap we find and give you a sealing plan, do the simple seals on the day, and quote anything larger. Rodent baiting carries a three-month re-treatment promise."),
        ("Do you go into the roof void?", "Yes, where the manhole and clearance make it safe. Most northern-suburbs rat activity is black rats in the roof, entering at gutter joints, eave gaps and unsealed roof penetrations. We inspect the void, place stations or traps there, then seal externally."),
        ("What does rodent control cost in Perth?", f"A rodent program with the initial visit, two tamper-resistant stations and a written proofing plan typically runs {money(*PRICES['rodent'])}. Follow-up checks are {money(*PRICES['rodent_follow'])}. Additional stations, roof or sub-floor access and sealing work are itemised on the quote."),
        ("Why do rodents come inside in winter?", "Warmth and food. Perth's May to August rains push rats and mice out of bush margins and garden beds toward roof voids and garages, and a dripping tap or a pet bowl left out overnight keeps them there. Sealing entry points before winter beats baiting in July."),
    ]
    ro_body = hero("Rodent control · rats and mice",
                   "Rodent control Perth.<br>Bait the runs, then <em class=\"red\">seal the gaps</em>.",
                   "Noises in the roof at night? We identify the species, map every entry point, place locked tamper-resistant stations, and give you a sealing plan so the roof stays quiet after the bait is gone.",
                   ["Licensed technicians", "3-month re-treatment promise", f"Typical {money(*PRICES['rodent'])}", "Follow-up visit scheduled"],
                   art_img("/assets/img/rodent-rat.jpg", "Brown rat on a ledge, illustrative image")) + \
        sec(eb("Signs you have rodents") + head("Rats, mice, and why winter is the season.") + '<div class="prose">'
            '<p>Three species cover almost every rodent call in Perth\'s northern suburbs. <strong>Black rats</strong> (<em>Rattus rattus</em>) are climbers: they enter roof voids along gutter lines, eaves and unsealed roof penetrations, and they are the usual reason for the scratching above the bedroom at 2 am. <strong>Norway rats</strong> (<em>Rattus norvegicus</em>) are larger, ground-based and prefer sub-floors, drains and burrows under sheds. <strong>House mice</strong> (<em>Mus musculus</em>) need a gap the width of a pen and a little dropped food.</p>'
            '<ul><li>Scratching, scurrying or gnawing in the ceiling, usually from dusk.</li>'
            '<li>Droppings in the roof void, garage, pantry, under the sink or along the fence line.</li>'
            '<li>Gnaw marks on cables, sarking, pet-food bags and fruit on the tree.</li>'
            '<li>Grease rubs along a wall or beam where a rat runs the same route each night.</li>'
            '<li>A pet suddenly fixated on one corner of the kitchen or the ceiling.</li></ul>'
            '<p>Rodents do not come inside for shelter alone. They come for food and water. A dripping tap, an open compost bin, fallen citrus or a bird feeder does more to keep them than any gap in the eaves. We look at why before we treat what.</p></div>', "ledger") + \
        sec(eb("How we treat it") + head("Identify, map, station, seal, follow up.") + steps([
            ("Identify the species and map the entry points", "Black rat, Norway rat or mouse changes the station, the bait and the placement. We inspect the roof void where safe, the sub-floor, garage and perimeter, and map every gap: gutter joints, eave gaps, roof penetrations, sub-floor vents, garage door seals, conduit entries."),
            ("Tamper-resistant stations and traps", "Locked, anchored stations with an APVMA-registered rodenticide block go on the external runs and in the roof void. Inside the living space, where pets or kids are present, we use covered snap traps to avoid secondary poisoning. Every placement is numbered and listed."),
            ("Proofing and the follow-up", "Simple seals such as mesh over an eave gap or a conduit escutcheon are done on the day. Larger sealing work is quoted. A follow-up visit checks consumption, repositions stations along the runs and confirms the house has gone quiet."),
        ])) + \
        sec(eb("What it costs") + head("Typical ranges.") +
            ledger(["Service", "Typical range", "Includes"], [
                ["Rodent program (initial visit)", money(*PRICES['rodent']), "Inspection, species ID, two tamper-resistant stations, entry-point map and proofing advice, report, 3-month promise"],
                ["Follow-up check", money(*PRICES['rodent_follow']), "Consumption check, re-bait, reposition, confirm clearance"],
                ["Additional stations", "Itemised", "Per station, placed and recorded"],
                ["Entry-point sealing", "Quoted", "Mesh, sealant, escutcheons; simple seals included on the day"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("Treatment report", "Species, an entry-point audit with photos, every station and trap numbered on a plan, product and rate, and a prevention plan split into what we did and what is yours to fix."),
            ("Treatment record", "Kept three years under the Health (Pesticides) Regulations 2011 and yours on request."),
            ("Three-month re-treatment promise", "If rodent activity returns inside the baited areas within three months, we return at no charge. Stations remain ours and are collected when the program ends unless you keep them on a check schedule."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Before we arrive.") + prep([
            "Clear access to the roof manhole and, if there is one, the sub-floor hatch.",
            "Remove any supermarket baits you have put down so we can read the runs and avoid doubling up.",
            "Put pet food away overnight, pick up fallen fruit, and lid the compost.",
            "Note where you hear the noise and at what time. It tells us the species and the run.",
            "Unlock side gates, the garage and the shed.",
            "Keep pets secured while we work in the roof and along the perimeter, and away from station positions we point out.",
        ]) + related([("General pest treatment", "/general-pest-control-perth"), ("Pricing guide", "/pest-control-prices-perth"), ("Rodent blog posts", "/blog")]), "ledger") + \
        sec(eb("Questions") + head("Rodent control FAQ.") + faq(ro_faqs)) + \
        quote("Get the roof quiet again.", "Tell us the suburb, where the noise is and whether you have pets. We will send an itemised price and a time, usually within a day or two for active rodents.")
    out.append({"path": "/rodent-control-perth", "title": "Rodent Control Perth | Rats and Mice in the Roof | DJ Pest",
                "desc": f"Rodent control for Perth's northern suburbs. Species identified, entry points mapped, tamper-resistant stations and a sealing plan. Typical {money(*PRICES['rodent'])}.",
                "body": ro_body, "crumbs": crumbs("Rodent control"),
                "schema": [service_schema("Rodent control", *PRICES['rodent'], "Rodent baiting with tamper-resistant stations, entry-point mapping and proofing advice."), faq_schema(ro_faqs)]})

        # ================================================================ /mosquito-control-perth
    mo_faqs = [
        ("Why are mosquitoes so bad in Perth's northern suburbs?", "Two reasons. The wetland chain from Lake Joondalup through Yellagonga to Lake Gwelup and the coastal swales breed mosquitoes on a large scale after rain and in the warm months, and the backyard container breeders, mainly <em>Aedes notoscriptus</em>, breed in anything that holds water for a week: pot-plant saucers, blocked gutters, bird baths, tarps, retic boxes. The wetland species fly in; the container species are made at home."),
        ("Can you get rid of mosquitoes completely?", "No, and be wary of anyone who says they can. Mosquitoes fly in from wetlands and neighbouring yards. What a treatment does is cut the number resting and biting in your yard by removing where they breed and treating the shaded surfaces where adults rest during the day. Most clients notice the difference within a day or two of treatment and it holds for several weeks in peak season."),
        ("What do you actually spray?", "An APVMA-registered residual insecticide whose label covers mosquitoes, applied to the surfaces where adults rest: under eaves, shaded walls and fences, dense shrubs and hedges, the underside of patio furniture, sheds and damp shady corners. It is not fogged into the air and it is not applied to flowering plants where bees are working. The product, rate and areas are on your treatment record."),
        ("Is it OK for kids, pets and the veggie patch?", "Kids and pets stay off treated surfaces until they are dry, usually within an hour or two, and we tell you the re-entry period before we start. We keep the treatment off vegetable beds, fruit that is about to be picked, fish ponds and bee-attracting flowers. Tell us about ponds, chooks and edible gardens when you book."),
        ("How often does it need doing?", "In the warm months a yard treatment typically holds four to six weeks, less after heavy rain or if the breeding sites are not fixed. Most clients on the wetland fringe book a treatment before a party or at the start of the season and one follow-up in late summer. Fixing the breeding sites is what stretches the interval."),
        ("What does mosquito control cost?", f"A residential yard treatment with the breeding-site audit typically runs {money(*PRICES['mosquito'])}. Larger blocks, dense vegetation and additional structures are itemised on the quote. Because mosquitoes fly in from outside the property, this service carries a recommended re-treatment interval rather than a re-treatment promise."),
        ("Do you treat for Ross River virus?", "We treat mosquitoes, not the virus. WA Health advises that mosquito-borne viruses including Ross River virus occur in Western Australia and that the best protection is avoiding bites: reducing breeding sites, screening, repellent and covering up at dusk. A yard treatment reduces the number of biting mosquitoes at home; it is not a substitute for personal protection."),
    ]
    mo_body = hero("Mosquito control · yards, patios and pool areas",
                   "Mosquito control Perth.<br>Fix the <em class=\"red\">breeding</em>, treat the resting sites.",
                   "Can't sit outside after five? We audit the yard for every place water sits, fix or flag it, then treat the shaded surfaces where adult mosquitoes rest during the day. Timed for Perth's warm-season peak.",
                   ["Licensed technicians", f"Typical {money(*PRICES['mosquito'])}", "Breeding-site audit included", "Bee-aware application"],
                   art_card("The audit covers", ["Gutters, downpipe sumps and drains", "Pot saucers, bird baths, buckets, tarps", "Retic and meter boxes, pool covers", "Ponds, water features, rain tanks", "Shaded harbourage: eaves, hedges, sheds"])) + \
        sec(eb("Why mosquitoes get bad") + head("Two populations, two fixes.") + '<div class="prose">'
            '<p>Perth\'s northern suburbs get mosquitoes from two directions. The <strong>wetland breeders</strong> come off the lakes and swales after rain and through the warm months, fly in at dusk and rest in your shaded vegetation by day. The <strong>container breeders</strong>, mostly the striped <em>Aedes notoscriptus</em>, are raised at home in anything that holds water for about a week: a pot saucer, a blocked gutter, a bird bath, a tarp on the trailer, a retic box with a slow leak.</p>'
            '<ul><li>Biting in the yard from late afternoon, worst in still, humid weather.</li>'
            '<li>Mosquitoes resting on shaded walls, under eaves and in dense shrubs during the day.</li>'
            '<li>Wrigglers (larvae) in standing water: flick a saucer or a bucket and watch for movement.</li>'
            '<li>Worse after rain and around the wetland fringe suburbs: Joondalup, Wanneroo, Kingsley, Woodvale, Balcatta near Lake Gwelup.</li></ul>'
            '<p>You can only treat what is on your side of the fence. That is why the audit comes first: emptying, tipping and screening the breeding sites does more over a season than any spray, and the residual treatment handles the adults that fly in.</p></div>', "ledger") + \
        sec(eb("How we treat it") + head("Audit, fix, treat, time it.") + steps([
            ("Breeding-site audit", "A walk of the whole yard, roof line and side paths for standing water. Saucers tipped, bird baths flagged for weekly changing, gutters and sumps noted, retic boxes drained. Anything you need to fix goes on the prevention plan."),
            ("Residual harbourage treatment", "An APVMA-registered residual insecticide labelled for mosquitoes is applied to the surfaces where adults rest: eaves, shaded walls and fences, hedges and dense shrubs, the underside of outdoor furniture, sheds and gazebos. Applied to label, not fogged, kept off flowering plants and food crops."),
            ("Timing and follow-up", "Treatments are timed for the warm season and ahead of events. A follow-up in late summer keeps the interval covered. Every visit is recorded with product, rate and areas."),
        ])) + \
        sec(eb("What it costs") + head("Typical ranges.") +
            ledger(["Service", "Typical range", "Includes"], [
                ["Residential yard mosquito treatment", money(*PRICES['mosquito']), "Breeding-site audit, residual harbourage treatment of yard, patio and structures, report and prevention plan"],
                ["Follow-up treatment (same season)", "Itemised", "Repeat harbourage treatment, audit re-check"],
                ["Large block or dense vegetation", "Quoted", "Additional product and time itemised"],
                ["Add to a general pest treatment", "Itemised", "Done on the same visit at a reduced rate"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("Breeding-site map", "Every place water was found, what we fixed on the day and what is yours to fix, with photos."),
            ("Treatment record", "Product, active constituent, rate, areas treated and re-entry period, kept three years under the Health (Pesticides) Regulations 2011."),
            ("Recommended interval", "Mosquitoes fly in from outside the property, so this service carries a recommended four-to-six-week interval in peak season rather than a re-treatment promise. We tell you that up front."),
        ])) + \
        sec(eb("Prepare for the visit") + head("Before we arrive.") + prep([
            "Tip out and turn over anything holding water: saucers, buckets, toys, tarps, wheelbarrows.",
            "Tell us about fish ponds, chooks, bee hives, vegetable beds and fruit about to be picked so we keep the treatment away from them.",
            "Bring washing in and cover outdoor food-prep areas and pet bowls.",
            "Unlock side gates and clear the path around the house.",
            "Keep kids and pets inside during treatment and off treated surfaces until dry.",
        ]) + related([("General pest treatment", "/general-pest-control-perth"), ("Spider control", "/spider-control-perth"), ("Pricing guide", "/pest-control-prices-perth")]), "ledger") + \
        sec(eb("Questions") + head("Mosquito control FAQ.") + faq(mo_faqs)) + \
        quote("Get the yard back after five.", "Tell us the suburb, whether you back onto bush or wetland, and if you have a pond or veggie patch. We will send an itemised price and a time.")
    out.append({"path": "/mosquito-control-perth", "title": "Mosquito Control Perth | Yard Treatment and Breeding-Site Audit | DJ Pest",
                "desc": f"Mosquito control for Perth's northern suburbs. Breeding-site audit, residual treatment of the shaded harbourages where adults rest, timed for the warm season. Typical {money(*PRICES['mosquito'])}.",
                "body": mo_body, "crumbs": crumbs("Mosquito control"),
                "schema": [service_schema("Mosquito control", *PRICES['mosquito'], "Residential mosquito control: breeding-site audit and residual harbourage treatment."), faq_schema(mo_faqs)]})

    

    # ================================================================ /wasp-removal-perth
    wa_faqs = [
        ("Can I remove a wasp nest myself?", "A brand-new paper wasp nest in early spring, the size of a golf ball with one or two wasps on it, can be knocked down at dusk with a long-handled broom and stepped on, if nobody in the house is allergic and you can retreat indoors quickly. Anything larger, anything above head height, anything in a wall vent or retic box, or anything where you cannot see the whole nest, is a job for someone with the gear. Multiple stings from a defended nest are a genuine medical risk, not an inconvenience."),
        ("Why do wasps keep building in the same spot?", "Paper wasps choose sheltered, warm, dry overhangs with a clear flight path, and your eaves offer the same thing every year. Mated queens also overwinter in roof voids and wall cavities nearby, and they start next season's nests within metres of where they were raised. Removing the comb and treating the surface with a residual product breaks that cycle for the season; screening the vent or gap they used breaks it for good."),
        ("Do wasps die off in winter?", "The colony does. Workers and the old queen die as the weather cools, and the nest is abandoned. The mated new queens do not; they tuck into a roof void, a wall cavity, a wood pile or under bark and start again in spring. An empty nest in June is not a problem, but a house with a lot of old nests under the eaves is a house that will have a lot of new ones in October."),
        ("Is it a wasp or a bee?", "Paper wasps are slim, with a narrow waist, long legs that dangle in flight and smooth, mostly hairless bodies in orange-brown or yellow and black. They build open grey combs where you can see the cells. Honey bees are stockier, hairy, golden brown, fly with their legs tucked, and nest inside cavities where you see traffic but no comb. If it is bees, see our <a href=\"/bee-removal-perth\">bee removal</a> page: the approach is different and a beekeeper may be the right call."),
        ("Are there European wasps in Perth?", "Not as an established population. European wasps are a declared pest in Western Australia and the Department of Primary Industries and Regional Development runs a surveillance and eradication program to keep it that way. They are stocky, bright yellow and black with black antennae, nest in the ground, compost or wall cavities, and a mature nest holds thousands of wasps. If we suspect one on a job we photograph it and report it to DPIRD, and they investigate and destroy confirmed nests. We do not treat suspected European wasp nests ourselves, and we do not charge you for the report."),
        ("What if I have been stung several times?", "For most people, stings from paper wasps cause local pain and swelling that settles in a day or two. Multiple stings, a sting inside the mouth or throat, or any swelling of the face, difficulty breathing or dizziness is an emergency: call 000. Anyone with a known wasp or bee venom allergy should stay well away from the nest and let someone else deal with it."),
        ("How quickly can you get to a wasp nest?", "Usually the same day or the next for a nest near a door, a path, a play area or a business entrance, because it is a safety issue rather than a nuisance. We are based in Warwick, so most of the northern corridor from Balcatta to Joondalup is under twenty minutes away."),
        ("Does a general pest treatment cover wasps?", "No. A general pest treatment covers cockroaches, spiders, silverfish and nuisance ants; wasps are a separate, nest-by-nest treatment with its own 30-day re-treatment period. If you book both on the same visit the wasp work is itemised on the same quote at a reduced rate."),
        ("What does wasp nest removal cost?", f"Treatment and removal of an accessible paper wasp nest typically runs {money(*PRICES['wasp'])}, including the walk of the roofline for others, the residual treatment of the site and the record. Additional nests found on the same visit are itemised at a reduced rate. Nests high on two-storey eaves or needing access equipment are quoted."),
    ]
    wa_body = hero("Wasp removal · eaves, pergolas, hedges and vents",
                   "Wasp removal Perth.<br>Nest treated and <em class=\"red\">gone</em>, usually same day.",
                   "Paper wasps build the grey, open-celled combs under your eaves and pergola beams, in the hedge and behind the shutters, and they defend them. We treat the nest, remove it, treat the surface so the next queen moves on, and walk the rest of the house for the ones you have not found yet.",
                   ["Licensed technicians", f"Typical {money(*PRICES['wasp'])}", "Same-day where possible", "30-day re-treatment promise"],
                   art_card("Where we find them", ["Under eaves, gutters and fascia returns", "Pergola, patio and carport beams", "Retic boxes, meter boxes and letterboxes", "Hedges, dense shrubs and citrus", "Behind shutters, roller-door housings and play equipment"])) + \
        sec(eb("Which wasp?") + head("Three wasps, three different answers.") + '<div class="prose">'
            "<p>Almost every wasp call in Perth's northern suburbs is a paper wasp. Two species share the eaves: the native common paper wasp and the introduced Asian paper wasp, which has been established in Perth for decades. Both are slim, orange-brown or yellow and black, with long legs that dangle in flight, and both build the familiar grey comb with open cells, anywhere from a fifty-cent piece to a dinner plate in size. A nest holds a few dozen to a couple of hundred wasps. They are not aggressive away from the nest, but they will sting repeatedly to defend it, and a nest over a door, a path or a swing set gets defended a lot.</p>"
            "<p>Mud daubers are the other regular. They are solitary, build mud tubes or blobs on walls and under eaves, and almost never sting. Their nests can be scraped off with a paint scraper when the wasp is out. If you send us a photo of a mud dauber we will tell you that, and not charge you.</p>"
            "<p>European wasps are the one to take seriously, because they are not meant to be here. They are a declared pest in Western Australia, not established in the state, and DPIRD runs an active surveillance and eradication program with public trapping each summer. They are stockier than paper wasps, bright yellow and black with black antennae, fly with their legs tucked up, and nest in the ground, in compost or inside wall cavities in colonies of thousands. If we see one we photograph it and report it to DPIRD's Pest and Disease Information Service, and they handle the nest. So can anyone: the MyPestGuide Reporter app takes photos straight to DPIRD.</p>"
            "<ul><li>Repeated wasp traffic to one point under the roofline, in a vent or a retic box.</li>"
            "<li>A grey comb with visible cells and wasps sitting on it, usually facing down.</li>"
            "<li>Wasps hunting caterpillars over the lawn and veggie patch: that is what paper wasps eat, and a nest nearby is likely.</li>"
            "<li>Stocky yellow-and-black wasps around meat, pet food or soft drink in numbers: photograph and report, do not disturb.</li></ul></div>", "ledger") + \
        sec(eb("How we treat it") + head("Find them all, treat, remove, make it unattractive.") + steps([
            ("Find every nest", "The nest you called about usually has relatives. We walk the whole roofline, pergola, fence line, hedge and outbuildings and count them before we start, because a treated nest by the front door does nothing about the three under the back eaves."),
            ("Treat the nest", "An APVMA-registered insecticide labelled for wasps, dust or spray depending on the position, applied directly to the comb, ideally early or late in the day when the colony is on the nest. We wear the gear so you do not have to. Activity stops within minutes to an hour."),
            ("Remove and treat the site", "Once the nest is quiet the comb comes off and goes with us. The surface is treated with a residual product so returning foragers and next season's queens are discouraged from rebuilding on the same beam. Vents and gaps that were being used are flagged for screening."),
            ("Record and promise", "Product, rate, every nest position and the re-entry period go on your treatment record. Treated nests carry a 30-day re-treatment promise: if a treated nest is active again inside that period, we come back at no charge."),
        ])) + \
        sec(eb("What it costs") + head("Typical ranges.") +
            ledger(["Service", "Typical range", "Includes"], [
                ["Paper wasp nest, accessible, treatment and removal", money(*PRICES['wasp']), "Roofline check for other nests, direct treatment, comb removal, residual treatment of the site, record and 30-day re-treatment promise"],
                ["Additional nests on the same visit", "Itemised", "Each extra nest at a reduced rate on the same quote"],
                ["High nest: two-storey eaves, tall trees, access equipment", "Quoted", "Ladder or platform work and time itemised after we have seen it"],
                ["Mud dauber nest", "Advice only", "Identification from your photo and how to remove it yourself"],
                ["Suspected European wasp", "No charge", "Photographed and reported to DPIRD, who investigate and destroy confirmed nests"],
                ["Add to a general pest treatment", "Itemised", "Done on the same visit at a reduced rate"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("Nest count and map", "Every nest we found, where it was and what we did with it, with photos. Most houses have more than the one you saw."),
            ("Treatment record", "Product, active constituent, rate, positions treated and re-entry period, kept three years under the Health (Pesticides) Regulations 2011 and emailed to you."),
            ("30-day re-treatment promise", "If a treated nest is active again inside 30 days we return at no charge. It is written into our terms, not a slogan."),
        ])) + \
        sec(eb("Wasp calendar") + head("The paper wasp year in the northern suburbs.") + steps([
            ("Sep – Oct · Spring: queens start small nests", "Overwintered queens begin golf-ball-sized combs under eaves. The easiest and lowest-cost time to deal with them, and the time nobody notices."),
            ("Nov – Jan · Early summer: colonies grow", "Workers emerge, nests reach palm size, traffic becomes obvious. Most first calls come now, often after someone is stung near a door or the pool."),
            ("Feb – Apr · Late summer and autumn: peak defence", "Nests at full size with the most wasps and the most to defend. New queens and males are reared. The busiest wasp months, and the ones with the most multiple-sting incidents."),
            ("May – Aug · Winter: colonies die, queens hide", "Workers die off and nests are abandoned. Mated queens shelter in roof voids and wall cavities nearby. Old nests can be scraped off; screen the vents they used before spring."),
        ]), "ledger") + \
        sec(eb("Prepare for the visit") + head("Before we arrive.") + prep([
            "Keep everyone, including pets, away from the nest and its flight path, and close windows and doors near it.",
            "Do not knock the nest down, hose it or hit it with a broom. A disturbed colony defends itself, and it will still be there tomorrow.",
            "Do not spray it at night by torchlight. Paper wasps fly to light, and the light is in your hand.",
            "Tell us about anyone in the household with a wasp or bee sting allergy.",
            "If you can do it safely from a distance, text a photo of the nest and note any other spots you have seen traffic.",
            "Unlock side gates and clear the path along the walls so we can walk the full roofline.",
        ]) + related([("Bee removal", "/bee-removal-perth"), ("General pest treatment", "/general-pest-control-perth"), ("Pricing guide", "/pest-control-prices-perth")])) + \
        sec(eb("Questions") + head("Wasp removal FAQ.") + faq(wa_faqs), "ledger") + \
        quote("A nest by the door gets fast-tracked.", "Text a photo of the nest and your suburb. We will tell you what it is, send an itemised price and, for a nest over a door or a path, usually get there the same day.")
    out.append({"path": "/wasp-removal-perth", "title": "Wasp Removal Perth | Paper Wasp Nest Treatment, Same Day | DJ Pest",
                "desc": f"Wasp nest removal across Perth's northern suburbs. Paper wasp nests found, treated and removed, site treated, 30-day re-treatment promise. Suspected European wasps reported to DPIRD. Typical {money(*PRICES['wasp'])}.",
                "body": wa_body, "crumbs": crumbs("Wasp removal"),
                "schema": [service_schema("Wasp nest removal", *PRICES['wasp'], "Paper wasp nest treatment and removal with residual site treatment and 30-day re-treatment promise."), faq_schema(wa_faqs)]})

    # ================================================================ /bee-removal-perth
    be_faqs = [
        ("Do you kill bees?", "Not when there is a reasonable alternative. A swarm hanging on a branch, a fence or a letterbox can usually be collected alive by a beekeeper, and that is what we recommend first. An established hive that has been building comb inside a double-brick wall or a roof void for months is a different problem: it cannot be coaxed out, a cut-out is a building job, and if nobody can reach the comb the only responsible option is a treatment done properly, with the entry sealed and the comb removed afterwards."),
        ("Why can't the bees in my wall just be removed alive?", "Because the colony is not the bees you see at the vent. It is the comb, the brood and the honey behind the bricks. Removing it alive means opening the wall, cutting out every piece of comb and boxing the queen, which is beekeeper and builder work, not pest control. Where the cavity can be opened and a beekeeper is willing, we will put you in touch and step back. Where it cannot, we treat."),
        ("Can I just leave the hive in the wall?", "You can, but the problems compound. The colony grows through spring and summer, throws off new swarms, and becomes more defensive as the honey stores build. Honey and wax stored inside a wall soften in Perth summer heat and can stain plaster, attract ants, cockroaches and wax moth, and draw robbing bees from other hives. Anyone in the household with a sting allergy is living next to an ongoing risk. Most people who wait end up calling in autumn with a bigger, angrier colony."),
        ("What actually happens on a bee treatment?", "We come in the evening when the foragers are home so the whole colony is inside. An APVMA-registered insecticide whose label covers bees is applied directly into the entry and the cavity, then the entry is sealed straight away so bees from other hives cannot rob the treated honey and carry it back to their own colony. We come back to confirm the traffic has stopped, and we give you a written plan for getting the comb out and proofing the weep holes."),
        ("Do I have to remove the comb afterwards?", "We strongly advise it, and we say so on the treatment record. Dead bees, brood and honey left inside a wall break down, smell, and pull in secondary pests. Unattended comb also smells like home to next spring's swarms, which is the most common reason people get bees in the same wall two years running. Comb removal is usually a handyman or builder opening a small section of plaster or a few bricks; we can recommend people who do it and tell them exactly where the comb is."),
        ("Are the bees in Perth dangerous?", "The bees that swarm and nest in Perth homes are European honey bees. A single sting is painful and, for most people, nothing more. For the small number of people with a bee venom allergy a sting can cause anaphylaxis, which is a 000 call. Swarms in transit are usually placid because they have no home to defend; a hive with stores is not. Keep children, pets and mowers away from the flight line and call before you poke anything."),
        ("What about native bees?", "Perth's native bees, including blue-banded bees, resin bees and leafcutter bees, are mostly solitary, nest in small burrows or borer holes, and rarely sting. They do not form the large colonies that cause problems in walls, and we do not treat them. If you send us a photo and it is a native bee, we will tell you so and suggest you enjoy it."),
        ("When is bee swarm season in Perth?", "Spring. Colonies that have built up over winter split as the weather warms and the flowering starts, so most swarm calls come between September and December, with October and November the peak. A swarm that lands in your garden will usually move on within a day or two once the scouts find a cavity, which is exactly when it becomes someone's wall problem. Late summer and autumn calls are usually established hives that were swarms in spring."),
        ("What does bee removal cost?", f"A swarm referral costs nothing: we identify it from your photo and give you the beekeeper's number. A treatment of an established hive with an accessible entry typically runs {money(*PRICES['bee'])}, including the evening visit, sealing the entry and the follow-up check. Hives high on a two-storey wall, in a roof void or behind cladding are quoted after we have seen them. Comb removal is a building task and is itemised or referred separately."),
    ]
    be_body = hero("Bee removal · swarms, wall cavities and roof voids",
                   "Bee removal Perth.<br>Relocate the <em class=\"red\">swarm</em>, resolve the hive.",
                   "A ball of bees hanging off a branch is a swarm looking for a home, and a beekeeper can often collect it alive. Bees that have been coming and going from a weep hole or the roofline for weeks are a hive with comb and honey behind your bricks, and that is a different job. We tell you which one you have before anything is booked.",
                   ["Licensed technicians", "Beekeeper referral first", f"Typical {money(*PRICES['bee'])} for a hive", "Comb removal and proofing plan"],
                   art_card("First we work out", ["Swarm in transit or an established hive", "How long the traffic has been going to that spot", "Whether the comb can be reached and cut out alive", "Who in the house has a sting allergy", "Whether a neighbour keeps hives nearby"])) + \
        sec(eb("Swarm or hive?") + head("Two situations, two answers.") + '<div class="prose">'
            "<p>Every spring, honey bee colonies across Perth's northern suburbs split. Half the bees leave with the old queen, settle in a tight cluster on a branch, a fence post, a letterbox or the side of a car, and send out scouts to find a cavity. That cluster is a swarm. It has no comb, no honey and nothing to defend, which is why swarms are usually placid, and why a beekeeper can shake it into a box and take it away. Most swarms move on within a day or two whether anyone helps them or not.</p>"
            "<p>The trouble starts where the scouts send them. Double-brick homes with open weep holes, roof voids with a lifted tile, meter and retic boxes, compost bins, wheelie bins, possum boxes and the hollow limbs of old tuarts and marris all make good cavities. Once the swarm moves in and starts drawing comb, it is an established hive. Within weeks there is brood, within a couple of months there can be several kilograms of honey inside your wall, and the colony now has something worth defending.</p>"
            "<ul><li><strong>Swarm:</strong> a dense cluster the size of a football, appeared in the last day or so, hanging in the open. Bees mostly still.</li>"
            "<li><strong>Hive:</strong> steady traffic in and out of one point, a hum in the wall, dark stains or a warm patch on plaster, bees appearing inside near windows, going on for weeks or months.</li>"
            "<li><strong>Neither:</strong> a few bees working the flowers or drinking from the pool are foragers from a hive somewhere else. Nothing to treat.</li></ul>"
            "<p>Text us a photo and tell us how long it has been going on. We will tell you which you have, and if it is a swarm we will give you a beekeeper's number rather than a quote.</p></div>", "ledger") + \
        sec(eb("How we handle it") + head("Identify, relocate where we can, treat where we must.") + steps([
            ("Identify and advise", "From your photo and a few questions we work out swarm or hive, how long it has been established and where the comb probably is. If it is a swarm that a beekeeper can reach, we give you the number of a registered WA beekeeper who collects swarms and we do not charge for the call. The WA Apiarists' Society also keeps a swarm collector list."),
            ("Relocate where the comb can be reached", "Where an established hive is somewhere a beekeeper can open, a compost bin, a possum box, a meter box, a wall a builder is willing to open, a live cut-out is the better outcome for you and the bees. We coordinate it and step back. It is beekeeper and builder work, and we say so rather than sell you a treatment."),
            ("Treat where it cannot", "Where the hive is deep in a double-brick cavity or a roof void and nobody can reach the comb, we treat. An APVMA-registered insecticide whose label covers bees is applied into the entry in the evening when the foragers are home. The entry is sealed immediately so bees from other colonies cannot rob the treated honey. A follow-up visit confirms the traffic has stopped."),
            ("Remove the comb, proof the wall", "The treatment record tells you exactly where the comb is and why it should come out: honey softens in summer heat, stains plaster, feeds ants and cockroaches, and draws next spring's swarms to the same wall. We recommend people who can open and close the wall, and we fit or specify weep-hole guards and vent screens that keep the ventilation and keep the bees out."),
        ])) + \
        sec(eb("What it costs") + head("Typical ranges.") +
            ledger(["Service", "Typical range", "Includes"], [
                ["Swarm on a branch, fence or post", "No charge", "Identification from your photo and a referral to a registered beekeeper who collects swarms"],
                ["Established hive, accessible entry", money(*PRICES['bee']), "Evening treatment with an APVMA-registered product, entry sealed, follow-up check, treatment record and comb-removal plan"],
                ["Hive in a roof void, two-storey wall or behind cladding", "Quoted", "Access equipment and additional time itemised after inspection"],
                ["Comb removal and making good", "Referred or itemised", "Opening the cavity, removing comb and honey, closing the wall; a building task we coordinate"],
                ["Weep-hole guards and vent screens", "Itemised", "Proofing the entry points so the next swarm's scouts move on"],
            ], amount_cols=(1,)) + PRICE_NOTE, "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("A straight answer first", "Swarm, hive or foragers, and whether it needs us, a beekeeper or nobody. Plenty of bee calls end with advice and no invoice."),
            ("Treatment record", "Product, active constituent, rate, where it went and the re-entry period, kept three years under the Health (Pesticides) Regulations 2011 and emailed to you."),
            ("Proofing and comb plan", "Where the comb sits, who can remove it, and the weep-hole and vent proofing that stops the same wall being colonised next spring. Treated nests carry our 30-day re-treatment promise."),
        ])) + \
        sec(eb("Bee calendar") + head("When bees turn up in the northern suburbs.") + steps([
            ("Sep – Dec · Spring: swarm season", "Colonies split as flowering starts. Clusters on branches and fences, scouts checking weep holes and roof tiles. October and November are the peak."),
            ("Dec – Feb · Summer: hives build stores", "Swarms that moved into walls in spring are now drawing comb and storing honey. Traffic at the entry gets heavier and the colony more defensive."),
            ("Mar – May · Autumn: the wall calls", "Honey stores peak and warm walls start to stain. Most established-hive treatments happen now, and comb removal before winter avoids a slow leak."),
            ("Jun – Aug · Winter: quiet, not gone", "Colonies cluster and traffic drops, so people assume the bees have left. They have not. Proof the weep holes now, before spring's scouts arrive."),
        ]), "ledger") + \
        sec(eb("Prepare for the visit") + head("Before we arrive.") + prep([
            "Keep children, pets and the mower away from the flight line. Bees defend the approach to the entry, not the garden in general.",
            "Do not block the entrance. Bees shut out of their entry look for another way, and that is usually into the house through a downlight or a vent.",
            "Do not spray the entry with a hardware-store aerosol. It rarely reaches the comb, it agitates the colony, and it pushes bees indoors.",
            "Tell us about anyone in the household with a bee-sting allergy, and where the EpiPen is kept.",
            "Text a photo of the cluster or the entry point and tell us how long the traffic has been going on.",
            "Let us know if a neighbour keeps hives. Sealing the treated entry promptly matters more when there are managed colonies nearby.",
        ]) + related([("Wasp removal", "/wasp-removal-perth"), ("General pest treatment", "/general-pest-control-perth"), ("Pricing guide", "/pest-control-prices-perth")])) + \
        sec(eb("Questions") + head("Bee removal FAQ.") + faq(be_faqs), "ledger") + \
        quote("Swarm or hive, start with a photo.", "Text a photo and how long it has been going on. If it is a swarm you get a beekeeper's number; if it is a hive you get an itemised price and an evening slot.")
    out.append({"path": "/bee-removal-perth", "title": "Bee Removal Perth | Swarm Relocation and Hive Treatment | DJ Pest",
                "desc": f"Bee removal in Perth's northern suburbs. Swarms referred to a beekeeper at no charge; hives in walls and roof voids treated and sealed. Typical {money(*PRICES['bee'])}.",
                "body": be_body, "crumbs": crumbs("Bee removal"),
                "schema": [service_schema("Bee removal", *PRICES['bee'], "Swarm identification and beekeeper referral; established hive treatment with entry sealing and comb-removal plan."), faq_schema(be_faqs)]})

    # ================================================================ /commercial-pest-control-perth
    co_faqs = [
        ("How often does a cafe or restaurant need pest control?", "Monthly is the norm for a working commercial kitchen, and it is what environmental health officers and HACCP auditors expect to see in the folder. The frequency is driven by food, warmth and water being present every day, and by German cockroaches breeding in six weeks. Small, dry, low-risk premises such as an office kitchenette can sit on quarterly. We recommend a frequency after the site survey and put the reasoning in writing."),
        ("Do you provide the reports an EHO or HACCP auditor wants?", "Yes, and that is most of the point. Your site folder holds the site map with numbered stations, the station register, a service report for every visit showing activity per station and actions taken, the pesticide ledger with product, active, rate and location, the safety data sheets, our licence and registration details and our insurance certificate. Auditors ask for exactly those documents, in roughly that order."),
        ("Can you service outside trading hours?", "Yes. Kitchens are treated before open or after close so nothing is applied around food preparation, and re-entry periods are met before staff return. Childcare and aged care sites are serviced when the rooms are empty. Early-morning and evening slots are part of the price for food premises, not an extra."),
        ("What does the Food Standards Code actually require?", "Standard 3.2.2 of the Australia New Zealand Food Standards Code, which applies in WA through the Food Act 2008, requires a food business to take all practicable measures to prevent pests entering the premises and to eradicate and prevent the harbourage of pests on the premises and in vehicles. The local government's environmental health officers inspect against that, and evidence of pests or no documented control is one of the fastest ways to a poor inspection result."),
        ("Do you do strata common property?", "Yes. Bin rooms, basements, car parks, plant rooms, lift wells, gardens and common walkways, on a quarterly or monthly cycle depending on the building. Cockroaches and rodents move between lots through service ducts and bin chutes, so a program that treats only the lot that complained does not work; we report to the strata manager or council of owners with what we found where, and quote individual lots separately when residents ask."),
        ("Is there a lock-in contract?", "There is a written agreement so the price, the frequency and what is included are not in dispute, and it is written in plain English. We do not rely on long lock-ins to keep clients; we rely on the folder being in order when the inspector walks in."),
        ("How is commercial work priced?", "Per site, after a walk-through, as a fixed price per visit, invoiced monthly on seven-day terms with a proper tax invoice. The indicative ranges on this page cover most northern-suburbs premises. What moves the price is floor area, the number of rodent stations and insect monitors the site needs, whether kitchens need a cockroach clean-out before the routine program can start, and access outside hours."),
        ("Which areas do you cover for commercial work?", "The northern corridor from Balcatta and Stirling up through Warwick, Greenwood, Duncraig, Hillarys, Joondalup and Wanneroo to Clarkson and Alkimos. Keeping the run tight is how we hold monthly prices down and turn up on time."),
    ]
    co_body = hero("Commercial pest control · food, strata, care, warehouse, office",
                   "Commercial pest control Perth.<br>A program your <em class=\"red\">auditor</em> can read.",
                   "Cafes and restaurants, strata common property, childcare and aged care, medical suites, warehouses and offices across the northern corridor. A documented program: numbered stations on a site map, a service report after every visit and a pesticide ledger in your site folder, so the environmental health officer or HACCP auditor finds what they need on the first look.",
                   ["Licensed technicians", "Site folder and same-day service reports", "Fixed per-visit price in writing", "Food Standards Code 3.2.2 aware"],
                   art_card("Built for", ["Food premises under Food Standards Code 3.2.2", "Strata common property, bin rooms and basements", "Childcare, aged care, medical and dental", "Offices, retail and showrooms", "Warehouses, workshops and depots"])) + \
        sec(eb("What the rules ask of you") + head("Documented, or it did not happen.") + '<div class="prose">'
            "<p><strong>Food businesses.</strong> Standard 3.2.2 of the Food Standards Code, applied in WA through the Food Act 2008, requires you to take all practicable measures to prevent pests entering and to eradicate and prevent their harbourage. Your local government's environmental health officers inspect against it. Droppings behind the fryer, a German cockroach in the coffee machine or no evidence of a program are the fastest routes to a poor result, a follow-up inspection and, in the worst case, a public notice. HACCP-based food safety programs and third-party audits go further: they want to see the station map, the service history, safety data sheets and licences in a folder, and a trend they can read.</p>"
            "<p><strong>Strata.</strong> The council of owners is responsible for common property. Cockroaches travel between lots through service risers and bin chutes, rodents run the basement and the bin room, and a program that only treats the lot that complained is a program that keeps complaining. Strata managers need a report they can table.</p>"
            "<p><strong>Childcare, aged care and health.</strong> Sensitive people, strict re-entry periods, product choices that suit the site and servicing when rooms are empty. Regulators and parents both ask what was used and when; the record answers.</p>"
            "<p><strong>Warehouses and workshops.</strong> Rodents are the usual issue: pallets, cardboard, roller doors that do not seal and food in the lunchroom. Numbered external and internal bait stations, proofing that actually gets done, and stock protected.</p>"
            "<p><strong>Offices and retail.</strong> Lower risk, quarterly is usually enough, but the kitchenette and the loading dock still need looking at, and a tenant's lease often requires a program in place.</p></div>", "ledger") + \
        sec(eb("How a program runs") + head("Survey, install, service, report.") + steps([
            ("Site survey and risk map", "A walk-through with whoever runs the site: kitchens, stores, bin areas, plant rooms, roof void and perimeter. We mark harbourages, entry points and conducive conditions, list the proofing that needs doing and by whom, recommend a frequency, and price it per visit in writing. If the site needs a cockroach clean-out or a rodent knock-down before a routine program makes sense, that is quoted separately and first."),
            ("Install and baseline", "Numbered, tamper-resistant rodent stations inside and out, insect monitors in kitchens and stores, gel and insect growth regulator in food areas, drain treatment where the species calls for it. The site folder is set up: site map, station register, safety data sheets, our licence and registration details and insurance certificate."),
            ("Scheduled service", "Each visit checks every station and monitor, records activity, re-baits or replaces, treats as needed and notes proofing items still outstanding on your side. Food premises are serviced outside food preparation, with re-entry met before staff return. Out-of-cycle callouts for a sighting are part of the agreement."),
            ("Report and trend", "A service report is emailed the same day: activity by station, product ledger, actions, photos, and what we need from you. Quarterly you get a trend summary you can hand to an auditor or table at a strata meeting. Records are kept three years under the Health (Pesticides) Regulations 2011."),
        ])) + \
        sec(eb("What it costs") + head("Indicative per-visit pricing.", "Every site is priced after the survey, as a fixed price per visit. These are the ranges most northern-suburbs premises land in.") +
            ledger(["Site type", "Typical range per visit", "Usual frequency and scope"], [
                ["Cafe, takeaway or small restaurant kitchen", "$140–$220", "Monthly. Cockroach gel and IGR, insect monitors, rodent stations, drain treatment, service report"],
                ["Larger restaurant, pub or commercial kitchen", "$220–$380", "Monthly. As above across multiple prep areas, cool rooms, stores and bin area"],
                ["Strata common property", "$180–$350", "Quarterly or monthly. Bin rooms, basement, car park, plant rooms, walkways; report to the strata manager"],
                ["Childcare, aged care, medical or dental", "$160–$300", "Monthly or bi-monthly. Serviced when rooms are empty, product and timing chosen for the site"],
                ["Office, retail or showroom", "$150–$260", "Quarterly. Kitchenette, stores, loading dock, perimeter stations"],
                ["Warehouse or workshop rodent program", "$180–$320", "Monthly. Numbered internal and external stations, proofing list, stock protection"],
                ["One-off kitchen clean-out before a program starts", money(*PRICES['comm_cleanout']), "German cockroach gel and IGR program with follow-up visit, or initial rodent knock-down"],
            ], amount_cols=(1,)) + '<p class="notice">Indicative ranges, GST inclusive, invoiced monthly on seven-day terms. Every program is quoted itemised in writing after the site survey; the invoice matches the quote. No call-out fee for the survey. See the <a href="/pest-control-prices-perth">residential pricing guide</a> for one-off treatments.</p>', "ledger") + \
        sec(eb("What you get") + head("What you get.") + included([
            ("The site folder", "Site map with numbered stations, station register, safety data sheets, our licence and registration details and insurance certificate. Everything an inspector or auditor asks for, in one place, kept current."),
            ("Same-day service reports", "Activity by station, what was applied where, photos, actions and the proofing we need from you, emailed the day of the visit. Quarterly trend summaries for audits and strata meetings."),
            ("Clean paperwork", "DJ Pest is run by a Chartered Accountant. One agreement in plain English, a fixed price per visit, one tax invoice a month with your purchase order on it, and a supplier who understands what your bookkeeper needs."),
        ])) + \
        sec(eb("Why this suits a business") + head("Run by a Chartered Accountant.") + '<div class="prose">'
            "<p>Most commercial pest programs fail on paperwork, not chemistry: the station map is out of date, two service reports are missing, the SDS folder has the wrong products in it, and the auditor is standing in the kitchen. DJ Pest is run by a Chartered Accountant, in a family that has been in Perth pest control since 2011. The technical work is done to label and to the Australian standards that apply; the record-keeping is done the way an auditor would do it. That is the whole pitch.</p>"
            "<ul><li>The same technician on your site each visit, who knows where the problems were last time.</li>"
            "<li>Proofing recommendations in writing, with who is responsible, so the same finding is not on every report.</li>"
            "<li>Out-of-cycle callouts for a sighting are part of the program, not a surprise invoice.</li>"
            "<li>Property managers with residential portfolios: see the <a href=\"/property-managers\">property managers</a> page for vacate flea treatments and lease-start programs.</li></ul></div>"
            + related([("Cockroach control", "/cockroach-control-perth"), ("Rodent control", "/rodent-control-perth"), ("General pest treatment", "/general-pest-control-perth"), ("Service areas", "/service-areas")])) + \
        sec(eb("Commercial pest calendar") + head("What turns up at work, and when.") + steps([
            ("Sep – Nov · Spring: ants and paper wasps", "Ant trails across loading docks and outdoor dining, wasp nests over entrances and in bin enclosures. Perimeter work and nest checks on the spring visits."),
            ("Dec – Feb · Summer: flies, cockroaches and drains", "German cockroaches at peak breeding in warm kitchens, drain flies and mosquitoes around bin rooms and grease traps. Gel, IGR and drain treatment carry the load."),
            ("Mar – May · Autumn: cockroaches move in", "Australian and American cockroaches follow warmth indoors from gardens, drains and mulch. Harbourage treatment of the perimeter and stores."),
            ("Jun – Aug · Winter: rodents", "Rats and mice into warehouses, roof voids, bin rooms and ceiling spaces above kitchens. Station activity peaks; proofing roller doors and pipe penetrations is the fix that lasts."),
        ]), "ledger") + \
        sec(eb("Questions") + head("Commercial pest control FAQ.") + faq(co_faqs)) + \
        quote("Book a site survey.", "Tell us the premises type, the suburb and what you have seen. We walk the site, recommend a frequency and send a fixed per-visit price in writing. No call-out fee for the survey.")
    out.append({"path": "/commercial-pest-control-perth", "title": "Commercial Pest Control Perth | Cafes, Strata, Childcare, Warehouses | DJ Pest",
                "desc": "Commercial pest control, Perth northern suburbs: documented programs for cafes, strata, childcare, aged care, offices and warehouses. Numbered stations, same-day reports, audit-ready folder.",
                "body": co_body, "crumbs": crumbs("Commercial pest control"),
                "schema": [service_schema("Commercial pest control", PRICES['comm_visit'][0], PRICES['comm_cleanout'][1], "Documented commercial pest management programs: site survey, numbered stations, scheduled service, same-day reports."), faq_schema(co_faqs)]})

    return out
