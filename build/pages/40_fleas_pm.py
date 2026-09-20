"""Vacate flea treatment page + property-manager page."""

DOMAIN = "https://djpest.com.au"
FLEA = (150, 220)

def money(lo, hi): return f"${lo:,}–${hi:,}"

def pages(c):
    S = c["SITE"]; esc = c["esc"]; icon = c["icon"]; sec = c["section"]; eb = c["eyebrow"]; card = c["card"]
    steps = c["steps"]; faq = c["faq"]; faq_schema = c["faq_schema"]; ledger = c["ledger_table"]; quote = c["quote_block"]

    def head(h2, lead=None):
        return f'<div class="section-head"><h2>{h2}</h2>{f"<p class=\"lead\">{lead}</p>" if lead else ""}</div>'

    def hero(eyebrow, h1, lead, trust, art):
        return f"""<section class="hero"><div class="wrap"><div>{eb(eyebrow)}<h1>{h1}</h1><p class="lead">{lead}</p>
<div class="actions">{c['btn_call']()}{c['btn_quote']()}</div><ul class="trust">{"".join(f"<li>{esc(t)}</li>" for t in trust)}</ul></div>{art}</div></section>"""

    def art_card(title, items):
        lis = "".join(f'<li style="display:flex;gap:.6rem;align-items:flex-start;margin:.5rem 0">{icon("check")}<span>{i}</span></li>' for i in items)
        return f'<div class="card" style="align-self:center"><div class="num">{esc(title)}</div><ul style="list-style:none;padding:0;margin:0;color:var(--ink-2)">{lis}</ul></div>'

    def svc_schema(name, lo, hi, desc):
        return {"@type": "Service", "serviceType": name, "name": name + " Perth", "description": desc,
                "provider": {"@id": DOMAIN + "/#business"}, "areaServed": {"@type": "Place", "name": "Perth northern suburbs, Western Australia"},
                "offers": {"@type": "Offer", "priceCurrency": "AUD", "price": lo, "priceSpecification": {"@type": "PriceSpecification", "minPrice": lo, "maxPrice": hi, "priceCurrency": "AUD"}}}

    price_note = ('<p class="notice">GST inclusive. Quoted from the address within the hour, itemised in writing. No call-out fee, no deposit, seven-day terms. '
                  'See the <a href="/pest-control-prices-perth">pricing guide</a>.</p>')

    # ================================================================ /flea-treatment-perth
    fl_faqs = [
        ("Do I have to get a flea treatment when I move out?", "Most WA residential leases that allowed a pet include a clause requiring a professional flea treatment at the end of the tenancy, and the property manager will ask for the certificate before releasing the bond. If the lease has the clause, the treatment is required whether or not you have seen fleas. If it doesn't, a treatment is still the fastest way to close out a pet tenancy without a dispute."),
        ("How fast can you do it?", "Quote back within the hour of receiving the address. A slot the same week, usually within two to three business days, and same-day where the schedule allows. The certificate is in your inbox and the property manager's within the hour of treatment."),
        ("What does the certificate say?", "Property address, date and time, the products applied with their APVMA registration numbers, active constituents and rates, the areas treated, the technician's name and WA licence number, and the re-entry period. It is the treatment record the Health (Pesticides) Regulations require us to keep, so it is the document a property manager can rely on."),
        ("Does the house need to be empty?", "Empty and vacuumed is ideal: fleas and their eggs live in carpet, under furniture and in pet bedding, so a bare floor means full coverage. If furniture is still in, we treat around and under what we can reach and note it on the certificate. Vacuum thoroughly beforehand and empty the vacuum outside."),
        ("What do you use, and is it OK for the next tenant?", "An APVMA-registered flea product with an insect growth regulator, applied to label to carpets, rugs, hard-floor edges, skirtings, under furniture and pet areas, plus the yard where pets spent time. Non-staining formulations indoors. The incoming tenant can move in once surfaces are dry, usually two to four hours, and the certificate states the re-entry period."),
        ("Why are there still fleas a week after the treatment?", "Flea pupae are protected in their cocoons and can hatch for up to two weeks after treatment; the growth regulator stops them breeding and the residual kills them as they emerge. Keep vacuuming daily for two weeks. If adults are still active after 30 days inside the treated areas and you followed the preparation steps, we return at no charge."),
        (f"What does an end-of-lease flea treatment cost in Perth?", f"{money(*FLEA)} depending on floor area and pet history: a unit or two-bedroom at the low end, a four-bedroom house with a dog in every room at the top. We quote from the address using the floor plan, so the price is fixed before we arrive."),
    ]
    fl_body = hero("Flea treatment · end of lease, tenants and owners",
                   "Vacate flea treatment Perth.<br>Quoted in an hour. Certificate <em class=\"red\">within the hour</em> of treatment.",
                   "Moving out with a pet, or moving in after one? We quote from the address, treat the same week, and email the treatment certificate to you and your property manager within the hour of finishing. Bond file sorted.",
                   [f"WA licence {S['licence']}", f"{money(*FLEA)} by floor area", "Same-week slot", "30-day re-treatment promise"],
                   art_card("What the certificate carries", ["Property address, date and time", "Products, APVMA numbers, actives, rates", "Areas treated, inside and out", "Technician name and WA licence 13914", "Re-entry period for the next occupant"])) + \
        sec(eb("Who this is for") + head("Three people, one document.") + '<div class="grid grid-3">'
            + card("Tenants moving out", "Your lease says a professional flea treatment at vacate. You need it done fast and you need the certificate for the bond. That is the whole job.")
            + card("Owners and landlords", "Between tenancies, after a pet, or before you move back in. Treated and documented so the next lease starts clean.")
            + card("Property managers", "One supplier who quotes from the address, turns up the same week and sends a certificate you can file without chasing. <a href=\"/property-managers\">See how we work with agencies</a>.")
            + '</div>', "ledger") + \
        sec(eb("How it works") + head("Address in, certificate out.") + steps([
            ("Send the address", "Text, email or the form. We pull the floor plan and property details, count the carpeted rooms and pet areas, and send an itemised fixed price within the hour."),
            ("Same-week treatment", "An APVMA-registered flea product with an insect growth regulator applied to label: carpets, rugs, hard-floor edges, skirtings, under and behind furniture, pet bedding areas and the yard where the pet lived. Non-staining indoors."),
            ("Certificate within the hour", "Before we reach the next job, the treatment certificate is in your inbox and the property manager's: products, rates, areas, licence number, re-entry period. Ready for the bond file."),
        ])) + \
        sec(eb("What it costs") + head("Fixed price by floor area.") +
            ledger(["Property", "Price", "Includes"], [
                ["Unit, apartment or 2-bedroom", "$150", "Internal treatment with IGR, certificate within the hour"],
                ["3-bedroom house", "$185", "Internal plus pet yard areas, certificate within the hour"],
                ["4-bedroom or larger, or heavy pet history", "$220", "Full internal and external pet areas, certificate within the hour"],
                ["Add a general pest treatment for the incoming tenant", "Itemised", "Cockroaches, spiders, silverfish, ants on the same visit at a reduced rate"],
            ], amount_cols=(1,)) + price_note, "ledger") + \
        sec(eb("Prepare the property") + head("Ten minutes of prep, full coverage.") + '<div class="prose"><ul>'
            '<li>Vacuum every carpet, rug and hard-floor edge, then empty the vacuum into an outside bin.</li>'
            '<li>Remove or wash pet bedding on a hot cycle. Take pet bowls and toys out.</li>'
            '<li>Clear floors as far as possible so we can reach under and behind furniture.</li>'
            '<li>Cover fish tanks and switch off their air pumps; take birds and reptiles out for the day.</li>'
            '<li>Leave the key arrangement with us or the agent; we do not need anyone home.</li>'
            '<li>Stay off treated floors until dry, usually two to four hours, then keep vacuuming daily for two weeks.</li></ul>'
            '<p>Related: <a href="/general-pest-control-perth">General pest treatment</a> · <a href="/property-managers">Property managers</a> · <a href="/pest-control-prices-perth">Pricing guide</a></p></div>') + \
        sec(eb("Questions") + head("Vacate flea treatment FAQ.") + faq(fl_faqs), "ledger") + \
        quote("Send the address. Price back within the hour.", "Put the property address and your move-out date in the message. Tell us if the agent needs the certificate sent to them too, and we will copy them in.")

    # ================================================================ /property-managers
    pm_faqs = [
        ("How quickly do you turn a vacate flea treatment around?", "Quote within the hour of the address, a slot the same week and usually within two to three business days, and the certificate to you and the tenant within the hour of treatment. If a settlement or new lease is tight, tell us and we will move things."),
        ("What is on the certificate and will it stand up in a bond dispute?", "It is the treatment record required by the Health (Pesticides) Regulations 2011: address, date and time, products with APVMA numbers, actives and rates, areas treated, technician name and WA licence number, re-entry period. Signed by a licensed technician of a registered pest management business. Filed with the bond, it answers the question before it is asked."),
        ("Can you handle keys and empty properties?", "Yes. Key collection from your office or a lockbox, treatment with nobody home, keys returned or left as instructed. Photos of the property on arrival and departure are attached to the report."),
        ("Do you offer account terms?", "One invoice per month with every job itemised by property, seven-day terms. Or per job if you prefer to on-charge immediately. Either way the invoice carries the trust entity and ABN your trust accountant will want."),
        ("What else do you do for managed properties?", "General pest treatments at lease start, ant and cockroach call-outs, rodent programs with entry-point sealing, spider treatments, termite inspections for owners and annual inspections for properties with a termite management system. The same certificate-style report on every job."),
        ("Which suburbs?", "The northern corridor from Balcatta and Karrinyup up to Yanchep, centred on Warwick. The full list is on the <a href=\"/service-areas\">service areas</a> page."),
    ]
    pm_body = hero("For property managers and strata",
                   "Vacate treatments that don't need <em class=\"red\">chasing</em>.",
                   "One supplier for the northern corridor who quotes from the address, turns up the same week, and puts the certificate in your inbox within the hour of treatment. Run by a Chartered Accountant, so the invoice is right the first time too.",
                   ["Quote within the hour", "Certificate within the hour of treatment", "One invoice a month", f"WA licence {S['licence']} · {S['pmb']}"],
                   art_card("What we handle", ["Vacate flea treatments with certificate", "Lease-start general pest treatments", "Ant, cockroach, spider and rodent call-outs", "Key collection and empty properties", "Termite inspections and annual re-inspections"])) + \
        sec(eb("Why agencies use us") + head("Three things a PM actually needs.") + '<div class="grid grid-3">'
            + card("Speed you can promise a tenant", "Address in, fixed price out within the hour. Same-week slot. You tell the tenant one thing and it happens.")
            + card("Paper for the bond file", "Every treatment produces a certificate with products, APVMA numbers, rates, areas and the technician's licence. It arrives within the hour of the job, to you and the tenant.")
            + card("Admin that does itself", "One monthly invoice itemised by property, or per job. Trust entity and ABN on every document. No call-out fees, no deposits, no surprises to on-charge.")
            + '</div>', "ledger") + \
        sec(eb("Vacate flea treatment") + head("The standard job, priced by floor area.") +
            ledger(["Property", "Price", "Turnaround"], [
                ["Unit, apartment, 2-bedroom", "$150", "Same week · certificate within the hour"],
                ["3-bedroom house", "$185", "Same week · certificate within the hour"],
                ["4-bedroom or larger, heavy pet history", "$220", "Same week · certificate within the hour"],
                ["Lease-start general pest treatment", "From $250", "Bundled with the flea treatment at a reduced rate"],
            ], amount_cols=(1,)) + price_note + '<p><a class="btn btn-ghost" href="/flea-treatment-perth">Flea treatment details ' + icon("arrow", "icon") + '</a></p>') + \
        sec(eb("How to send us a job") + head("Three ways, all under a minute.") + steps([
            ("Email the address", f"Send the property address, the tenant's contact and the vacate date to <a href=\"mailto:{S['email']}\">{S['email']}</a>. Quote back within the hour."),
            ("Text it", f"Same details to <a href=\"{S['phone_sms']}\">{S['phone_display']}</a> from your mobile. We reply with the price and the earliest slot."),
            ("Put us on the vacate checklist", "Add \"Flea treatment: DJ Pest, 0447 747 769, certificate within the hour\" to your vacate pack and let tenants book direct. You get the certificate either way."),
        ]), "ledger") + \
        sec(eb("Questions") + head("Property manager FAQ.") + faq(pm_faqs)) + \
        quote("Set up your agency.", "Tell us the agency, your name and roughly how many managed properties are in the northern corridor. We will send the certificate sample, the price sheet and the account form.")

    return [
        {"path": "/flea-treatment-perth", "title": "Vacate Flea Treatment Perth | Certificate Within the Hour | DJ Pest",
         "desc": f"End-of-lease flea treatment for Perth's northern suburbs. Quoted from the address within the hour, same-week slot, certificate to you and your property manager within the hour of treatment. {money(*FLEA)}.",
         "body": fl_body, "crumbs": [("Services", "/services"), ("Flea treatment", None)],
         "schema": [svc_schema("Flea treatment", *FLEA, "End-of-lease flea treatment with insect growth regulator and a treatment certificate issued within the hour."), faq_schema(fl_faqs)]},
        {"path": "/property-managers", "title": "Pest Control for Property Managers Perth | Vacate Flea Treatments | DJ Pest",
         "desc": "One pest supplier for Perth's northern corridor: vacate flea treatments quoted within the hour, same-week slots, certificates within the hour of treatment, one monthly invoice.",
         "body": pm_body, "crumbs": [("Property managers", None)],
         "schema": [svc_schema("Property management pest services", 150, 250, "Vacate flea treatments, lease-start pest treatments and call-outs for property managers, with certificates and monthly invoicing."), faq_schema(pm_faqs)]},
    ]
