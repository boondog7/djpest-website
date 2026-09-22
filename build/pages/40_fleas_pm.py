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
{c['hours_cue']()}<div class="actions">{c['btn_call']()}{c['btn_quote']()}</div><ul class="trust">{"".join(f"<li>{esc(t)}</li>" for t in trust)}</ul></div>{art}</div></section>"""

    def art_card(title, items):
        lis = "".join(f'<li style="display:flex;gap:.6rem;align-items:flex-start;margin:.5rem 0">{icon("check")}<span>{i}</span></li>' for i in items)
        return f'<div class="card" style="align-self:center"><div class="num">{esc(title)}</div><ul style="list-style:none;padding:0;margin:0;color:var(--ink-2)">{lis}</ul></div>'

    def svc_schema(name, lo, hi, desc):
        return {"@type": "Service", "serviceType": name, "name": name + " Perth", "description": desc,
                "provider": {"@id": DOMAIN + "/#business"}, "areaServed": {"@type": "Place", "name": "Perth northern suburbs, Western Australia"},
                "offers": {"@type": "Offer", "priceCurrency": "AUD", "price": lo, "priceSpecification": {"@type": "PriceSpecification", "minPrice": lo, "maxPrice": hi, "priceCurrency": "AUD"}}}

    investment_note = ('<p class="notice">GST inclusive. Quoted from the address within the hour, itemised in writing. No call-out fee, no deposit, seven-day terms. '
                  'See the <a href="/pest-control-prices-perth">investment guide</a>.</p>')

    # ================================================================ /flea-treatment-perth
    fl_faqs = [
        ("Do I have to get a flea treatment when I move out?", "Most WA residential leases that allowed a pet include a clause requiring a professional flea treatment at the end of the tenancy, and the property manager will ask for the certificate before releasing the bond. If the lease has the clause, the treatment is required whether or not you have seen fleas. If it doesn't, a treatment is still the fastest way to close out a pet tenancy without a dispute."),
        ("How fast can you do it?", "Quote back within the hour of receiving the address. A slot the same week, usually within two to three business days, and same-day where the schedule allows. The certificate is in your inbox and the property manager's within the hour of treatment."),
        ("What does the certificate say?", "Property address, date and time, the products applied with their APVMA registration numbers, active constituents and rates, the areas treated, the technician's name and WA licence number, and the re-entry period. It is the treatment record the Health (Pesticides) Regulations require us to keep, so it is the document a property manager can rely on."),
        ("Does the house need to be empty?", "Empty and vacuumed is ideal: fleas and their eggs live in carpet, under furniture and in pet bedding, so a bare floor means full coverage. If furniture is still in, we treat around and under what we can reach and note it on the certificate. Vacuum thoroughly beforehand and empty the vacuum outside."),
        ("What do you use, and is it OK for the next tenant?", "An APVMA-registered flea product with an insect growth regulator, applied to label to carpets, rugs, hard-floor edges, skirtings, under furniture and pet areas, plus the yard where pets spent time. Non-staining formulations indoors. The incoming tenant can move in once surfaces are dry, usually two to four hours, and the certificate states the re-entry period."),
        ("Why are there still fleas a week after the treatment?", "Flea pupae are protected in their cocoons and can hatch for up to two weeks after treatment; the growth regulator stops them breeding and the residual kills them as they emerge. Keep vacuuming daily for two weeks. If adults are still active after 30 days inside the treated areas and you followed the preparation steps, we return at no charge."),
        ("I didn't have a pet. Do I still need a flea treatment?", "Check the special conditions of your lease. If the pet clause and its flea-treatment condition are not there, you generally do not need one under WA tenancy arrangements, and a property manager asking anyway should point to the clause. If a previous tenant's fleas are the problem, that is normally the owner's issue to fix, not yours. If your lease does have the clause, the treatment is required whether or not you ever saw a flea."),
        ("When should I book it?", "After the bond clean and the carpet clean, as close to handing back the keys as possible. Treating a cleaned, empty house gives the residual and growth regulator full contact with the carpet, and nothing walks fleas back in afterwards. Same-week slots mean booking two or three days before key handover usually lands perfectly. Doing a <a href=\"/end-of-lease-pest-control-perth\">full end-of-lease pest treatment</a>? Same visit, one certificate."),
        (f"What does an end-of-lease flea treatment cost in Perth?", f"{money(*FLEA)} depending on floor area and pet history: a unit or two-bedroom at the low end, a four-bedroom house with a dog in every room at the top. We quote from the address using the floor plan, so the investment is fixed before we arrive."),
    ]
    fl_body = hero("Flea treatment · end of lease, tenants and owners",
                   "Vacate flea treatment Perth.<br>Quoted in an hour. Certificate <em class=\"red\">within the hour</em> of treatment.",
                   "Moving out with a pet, or moving in after one? We quote from the address, treat the same week, and email the treatment certificate to you and your property manager within the hour of finishing. Bond file sorted.",
                   ["Licensed under the WA Pesticides Regs", f"{money(*FLEA)} by floor area", "Same-week slot", "30-day re-treatment promise"],
                   art_card("What the certificate carries", ["Property address, date and time", "Products, APVMA numbers, actives, rates", "Areas treated, inside and out", "Technician name and licence number", "Re-entry period for the next occupant"])) + \
        sec(eb("Who this is for") + head("Three people, one document.") + '<div class="grid grid-3">'
            + card("Tenants moving out", "Your lease says a professional flea treatment at vacate. You need it done fast and you need the certificate for the bond. That is the whole job.")
            + card("Owners and landlords", "Between tenancies, after a pet, or before you move back in. Treated and documented so the next lease starts clean.")
            + card("Property managers", "One supplier who quotes from the address, turns up the same week and sends a certificate you can file without chasing. <a href=\"/property-managers\">See how we work with agencies</a>.")
            + '</div>', "ledger") + \
        sec(eb("How it works") + head("Address in, certificate out.") + steps([
            ("Send the address", "Text, email or the form. We pull the floor plan and property details, count the carpeted rooms and pet areas, and send an itemised fixed investment within the hour."),
            ("Same-week treatment", "An APVMA-registered flea product with an insect growth regulator applied to label: carpets, rugs, hard-floor edges, skirtings, under and behind furniture, pet bedding areas and the yard where the pet lived. Non-staining indoors."),
            ("Certificate within the hour", "Before we reach the next job, the treatment certificate is in your inbox and the property manager's: products, rates, areas, licence number, re-entry period. Ready for the bond file."),
        ])) + \
        sec(eb("The investment") + head("Fixed investment by floor area.") +
            ledger(["Property", "Investment", "Includes"], [
                ["Unit, apartment or 2-bedroom", "$150", "Internal treatment with IGR, certificate within the hour"],
                ["3-bedroom house", "$185", "Internal plus pet yard areas, certificate within the hour"],
                ["4-bedroom or larger, or heavy pet history", "$220", "Full internal and external pet areas, certificate within the hour"],
                ["Add a general pest treatment for the incoming tenant", "Itemised", "Cockroaches, spiders, silverfish, ants on the same visit at a reduced rate"],
            ], amount_cols=(1,)) + investment_note, "ledger") + \
        sec(eb("Prepare the property") + head("Ten minutes of prep, full coverage.") + '<div class="prose"><ul>'
            '<li><strong>Order matters:</strong> bond clean and carpet clean first, flea treatment last, just before the keys go back. A steam clean after our treatment strips the residual and the growth regulator out of the carpet.</li>'
            '<li>Vacuum every carpet, rug and hard-floor edge, then empty the vacuum into an outside bin.</li>'
            '<li>Remove or wash pet bedding on a hot cycle. Take pet bowls and toys out.</li>'
            '<li>Clear floors as far as possible so we can reach under and behind furniture.</li>'
            '<li>Cover fish tanks and switch off their air pumps; take birds and reptiles out for the day.</li>'
            '<li>Leave the key arrangement with us or the agent; we do not need anyone home.</li>'
            '<li>Stay off treated floors until dry, usually two to four hours, then keep vacuuming daily for two weeks.</li></ul>'
            '<p>Related: <a href="/general-pest-control-perth">General pest treatment</a> · <a href="/property-managers">Property managers</a> · <a href="/pest-control-prices-perth">Investment guide</a></p></div>') + \
        sec(eb("Questions") + head("Vacate flea treatment FAQ.") + faq(fl_faqs), "ledger") + \
        quote("Send the address. Investment back within the hour.", "Put the property address and your move-out date in the message. Tell us if the agent needs the certificate sent to them too, and we will copy them in.")

    # ================================================================ /property-managers
    pm_faqs = [
        ("How quickly do you turn a vacate flea treatment around?", "Quote within the hour of the address, a slot the same week and usually within two to three business days, and the certificate to you and the tenant within the hour of treatment. If a settlement or new lease is tight, tell us and we will move things."),
        ("What is on the certificate and will it stand up in a bond dispute?", "It is the treatment record required by the Health (Pesticides) Regulations 2011: address, date and time, products with APVMA numbers, actives and rates, areas treated, technician name and WA licence number, re-entry period. Signed by a licensed technician of a registered pest management business. Filed with the bond, it answers the question before it is asked."),
        ("Can you handle keys and empty properties?", "Yes. Key collection from your office or a lockbox, treatment with nobody home, keys returned or left as instructed. Photos of the property on arrival and departure are attached to the report."),
        ("Do you offer account terms?", "One invoice per month with every job itemised by property, seven-day terms. Or per job if you prefer to on-charge immediately. Either way the invoice carries the trust entity and ABN your trust accountant will want."),
        ("What else do you do for managed properties?", "General pest treatments at lease start, ant and cockroach call-outs, rodent programs with entry-point sealing, spider treatments, termite inspections for owners and annual inspections for properties with a termite management system. The same certificate-style report on every job."),
        ("Which suburbs?", "Perth's northern and inner-northern suburbs, from Subiaco and Bayswater up to Yanchep, centred on Warwick. The full list is on the <a href=\"/service-areas\">service areas</a> page."),
    ]
    pm_body = hero("For property managers and strata",
                   "Vacate treatments that don't need <em class=\"red\">chasing</em>.",
                   "One supplier for the northern corridor who quotes from the address, turns up the same week, and puts the certificate in your inbox within the hour of treatment. Run by a Chartered Accountant, so the invoice is right the first time too.",
                   ["Quote within the hour", "Certificate within the hour of treatment", "One invoice a month", "Licence details on every certificate"],
                   art_card("What we handle", ["Vacate flea treatments with certificate", "Lease-start general pest treatments", "Ant, cockroach, spider and rodent call-outs", "Key collection and empty properties", "Termite inspections and annual re-inspections"])) + \
        sec(eb("Why agencies use us") + head("Three things a PM actually needs.") + '<div class="grid grid-3">'
            + card("Speed you can promise a tenant", "Address in, fixed investment out within the hour. Same-week slot. You tell the tenant one thing and it happens.")
            + card("Paper for the bond file", "Every treatment produces a certificate with products, APVMA numbers, rates, areas and the technician's licence. It arrives within the hour of the job, to you and the tenant.")
            + card("Admin that does itself", "One monthly invoice itemised by property, or per job. Trust entity and ABN on every document. No call-out fees, no deposits, no surprises to on-charge.")
            + '</div>', "ledger") + \
        sec(eb("Vacate flea treatment") + head("The standard job, quoted by floor area.") +
            ledger(["Property", "Investment", "Turnaround"], [
                ["Unit, apartment, 2-bedroom", "$150", "Same week · certificate within the hour"],
                ["3-bedroom house", "$185", "Same week · certificate within the hour"],
                ["4-bedroom or larger, heavy pet history", "$220", "Same week · certificate within the hour"],
                ["Lease-start general pest treatment", "From $250", "Bundled with the flea treatment at a reduced rate"],
            ], amount_cols=(1,)) + investment_note + '<p><a class="btn btn-ghost" href="/flea-treatment-perth">Flea treatment details ' + icon("arrow", "icon") + '</a></p>') + \
        sec(eb("How to send us a job") + head("Three ways, all under a minute.") + steps([
            ("Email the address", f"Send the property address, the tenant's contact and the vacate date to <a href=\"mailto:{S['email']}\">{S['email']}</a>. Quote back within the hour."),
            ("Text it", f"Same details to <a href=\"{S['phone_sms']}\">{S['phone_display']}</a> from your mobile. We reply with the investment and the earliest slot."),
            ("Put us on the vacate checklist", "Add \"Flea treatment: DJ Pest, 0468 170 107, certificate within the hour\" to your vacate pack and let tenants book direct. You get the certificate either way."),
        ]), "ledger") + \
        sec(eb("Questions") + head("Property manager FAQ.") + faq(pm_faqs)) + \
        quote("Set up your agency.", "Tell us the agency, your name and roughly how many managed properties are in the northern corridor. We will send the certificate sample, the investment sheet and the account form.")


    # ================================================================ /end-of-lease-pest-control-perth
    eol_faqs = [
        ("Is an end-of-lease pest treatment legally required in WA?", "Not by any statute directly. The requirement comes from your lease: WA tenancy agreements made under the Residential Tenancies Act 1987 (WA) commonly carry special conditions requiring a professional flea treatment where a pet was kept, and sometimes a broader pest treatment. Read the special conditions of your own lease; that clause, not a law, is what the property manager holds you to at bond time."),
        ("Who pays: tenant or owner?", "The working rule in WA: pests that arrived because of your tenancy (fleas from your pet is the classic) are the tenant's to fix at vacate; infestations that pre-date the tenancy or come with the building (termites, an established cockroach problem in the walls) are the owner's. Where it is arguable, the lease's special conditions and the condition report decide it. We put what we found on the certificate either way, which usually settles the conversation."),
        ("What order do I do everything in?", "Bond clean first, carpet steam clean second, pest treatment last, keys back to the agent after that. If the carpets are cleaned after the pest treatment, the residual product and insect growth regulator are stripped out and the treatment may have to be repeated. We schedule for the gap between the carpet clean and key handover, and same-week slots make that easy to hit."),
        ("Will your certificate satisfy my property manager?", "It is the treatment record the Health (Pesticides) Regulations 2011 (WA) require a registered pest management business to keep: property address, date and time, every product with its APVMA number, active constituent and rate, the areas treated, the technician's name and WA licence number, and the re-entry period. It is emailed to you and your agent within the hour of treatment. A supermarket bomb receipt is not a treatment record, which is why agents reject them."),
        ("Do I need the full pest treatment or just the flea treatment?", "Read the clause. Most pet clauses require a flea treatment only, which is the smaller job. Some leases require an end-of-tenancy pest treatment covering general pests as well; owners often add one between tenancies anyway so the next lease starts clean. If you book both, they happen on the same visit, on one certificate, at a bundled rate."),
        ("How fast can you turn it around?", "Quote within the hour of receiving the address, a slot the same week and usually within two to three business days, same-day where the run allows. The certificate is in your inbox and the property manager's within the hour of treatment finishing."),
        ("What does end-of-lease pest control cost in Perth?", f"A vacate flea treatment is {money(*FLEA)} by floor area. A full general pest treatment (cockroaches, spiders, silverfish, ants, internal and external) is typically $250 to $350 for a three-bedroom home, and booking it with the flea treatment on the same visit brings the combined figure down. Every job is quoted itemised in writing from the address before you commit."),
    ]
    eol_body = hero("End of lease · tenants, owners and agents",
                    "End of lease pest control Perth.<br>One visit, one certificate, <em class=\"red\">bond file closed</em>.",
                    "Vacate flea treatment, a full end-of-tenancy pest treatment, or both on the same visit. Quoted from the address within the hour, treated the same week, certificate to you and your property manager within the hour of finishing.",
                    ["Licensed under the WA Pesticides Regs", "Certificate within the hour of treatment", "Same-week slot", "30-day re-treatment promise on fleas"],
                    art_card("The bond-file order of operations", ["1. Bond clean", "2. Carpet steam clean", "3. Pest treatment (this is us)", "4. Certificate emailed within the hour", "5. Keys back to the agent"])) + \
        sec(eb("What your lease actually requires") + head("Read the special conditions, then book only what they ask for.") + '<div class="grid grid-3">'
            + card("Pet clause: flea treatment", "The most common condition. A professional flea treatment at vacate, certificate to the agent, whether or not you ever saw a flea. <a href=\"/flea-treatment-perth\">The vacate flea treatment</a> is the whole job.")
            + card("Pest clause: full treatment", "Some leases require an end-of-tenancy pest treatment covering general pests. Internal and external, cockroaches, spiders, silverfish and ants, documented on the same certificate.")
            + card("No clause: your call", "No pet, no clause, no obligation. WA tenancy agreements under the Residential Tenancies Act 1987 only bind you to what is written in them. If an agent asks anyway, ask them to point to the clause.")
            + '</div>', "ledger") + \
        sec(eb("How it works") + head("Address in, certificate out, keys back.") + steps([
            ("Send the address and vacate date", "Text, email or the form. We pull the floor plan, count carpeted rooms and pet areas, and send an itemised fixed investment for the flea treatment, the full treatment or the bundle within the hour."),
            ("We treat after your carpet clean", "Scheduled for the gap between the carpet clean and key handover. APVMA-registered products applied to label: carpets, hard-floor edges, skirtings, pet areas and the yard where pets lived, plus the general pest scope if booked. Non-staining indoors."),
            ("Certificate within the hour", "Products, APVMA numbers, actives, rates, areas, technician licence number and re-entry period, emailed to you and the agent before we reach the next job. The bond conversation is over before it starts."),
        ])) + \
        sec(eb("The investment") + head("Itemised, fixed from the address.") +
            ledger(["Job", "Investment", "Notes"], [
                ["Vacate flea treatment", money(*FLEA), "By floor area and pet history · certificate within the hour"],
                ["End-of-lease general pest treatment", "$250–$350", "Three-bedroom home, internal and external"],
                ["Flea + general pest on one visit", "Itemised bundle", "One visit, one certificate, reduced combined rate"],
            ], amount_cols=(1,)) + investment_note, "ledger") + \
        sec(eb("Questions") + head("End-of-lease FAQ.") + faq(eol_faqs)) + \
        quote("Send the address and your vacate date.", "Tell us which clause is in your lease, or forward the page of the lease and we will read it. Investment back within the hour, certificate copied to your agent on the day.")

    return [
        {"path": "/flea-treatment-perth", "title": "Vacate Flea Treatment Perth | Certificate Within the Hour | DJ Pest",
         "desc": f"End-of-lease flea treatment for Perth's northern suburbs. Quoted from the address within the hour, same-week slot, certificate to you and your property manager within the hour of treatment. {money(*FLEA)}.",
         "body": fl_body, "crumbs": [("Services", "/services"), ("Flea treatment", None)],
         "schema": [svc_schema("Flea treatment", *FLEA, "End-of-lease flea treatment with insect growth regulator and a treatment certificate issued within the hour."), faq_schema(fl_faqs)]},
        {"path": "/end-of-lease-pest-control-perth", "title": "End of Lease Pest Control Perth | Flea & Full Treatments, Certificate | DJ Pest",
         "desc": "End-of-lease pest control for Perth's northern suburbs: vacate flea treatments and full end-of-tenancy treatments, quoted within the hour, certificate to you and your agent within the hour of treatment.",
         "body": eol_body, "crumbs": [("Services", "/services"), ("End of lease", None)],
         "schema": [svc_schema("End of lease pest control", 150, 350, "Vacate flea treatments and end-of-tenancy pest treatments with a treatment certificate emailed within the hour."), faq_schema(eol_faqs)]},
        {"path": "/property-managers", "title": "Pest Control for Property Managers Perth | Vacate Flea Treatments | DJ Pest",
         "desc": "One pest supplier for Perth's northern corridor: vacate flea treatments quoted within the hour, same-week slots, certificates within the hour of treatment, one monthly invoice.",
         "body": pm_body, "crumbs": [("Property managers", None)],
         "schema": [svc_schema("Property management pest services", 150, 250, "Vacate flea treatments, lease-start pest treatments and call-outs for property managers, with certificates and monthly invoicing."), faq_schema(pm_faqs)]},
    ]
