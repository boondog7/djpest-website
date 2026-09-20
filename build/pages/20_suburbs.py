"""Service-areas hub + eight suburb pages (Warwick base)."""

DRIVE = {  # honest estimates from Warwick, off-peak
    "Warwick": "we're here", "Greenwood": "about 5 minutes", "Hamersley": "about 5 minutes", "Kingsley": "about 5 minutes",
    "Carine": "about 8 minutes", "Marangaroo": "about 8 minutes", "Girrawheen": "about 8 minutes", "Balga": "about 8 minutes",
    "Duncraig": "about 10 minutes", "Balcatta": "about 10 minutes", "Woodvale": "about 10 minutes", "Padbury": "about 10 minutes",
    "Sorrento": "about 12 minutes", "Hillarys": "about 12 minutes", "Craigie": "about 12 minutes", "Stirling": "about 12 minutes",
    "Karrinyup": "about 12 minutes", "Kallaroo": "about 15 minutes", "Mullaloo": "about 15 minutes",
    "Joondalup": "15 to 20 minutes", "Wanneroo": "15 to 20 minutes", "Ocean Reef": "about 20 minutes", "Currambine": "about 20 minutes",
    "Kinross": "about 25 minutes", "Clarkson": "about 25 minutes", "Mindarie": "about 25 minutes", "Butler": "about 30 minutes",
    "Quinns Rocks": "about 30 minutes", "Alkimos": "about 35 minutes", "Yanchep": "about 45 minutes",
}
GROUPS = [
    ("Coastal strip", "Sorrento, Hillarys, Kallaroo, Mullaloo, Ocean Reef and the Quindalup dunes over Tamala limestone. Salt air, older brick-and-tile and a lot of rebuilds.",
     ["Sorrento", "Hillarys", "Kallaroo", "Mullaloo", "Ocean Reef"]),
    ("Inland suburbs", "The 1960s to 1980s heartland between the Mitchell Freeway and Wanneroo Road. Yellow Spearwood sands, mature gardens, timber roof framing.",
     ["Warwick", "Greenwood", "Duncraig", "Kingsley", "Woodvale", "Padbury", "Craigie", "Hamersley", "Carine", "Karrinyup", "Stirling", "Balcatta", "Balga", "Marangaroo", "Girrawheen"]),
    ("Northern growth corridor", "Joondalup, Wanneroo and the estates that keep going north. Slab-on-ground homes from the 1990s onward, bush and wetland on the doorstep.",
     ["Joondalup", "Wanneroo", "Currambine", "Kinross", "Clarkson", "Mindarie", "Butler", "Quinns Rocks", "Alkimos", "Yanchep"]),
]
PAGES8 = ["Warwick", "Greenwood", "Duncraig", "Sorrento", "Hillarys", "Joondalup", "Wanneroo", "Balcatta"]
slug = lambda s: "/" + s.lower().replace(" ", "-")

# --------------------------------------------------------------- suburb copy
SUBURBS = {
"Warwick": dict(
    postcode="6024", drive="we're based here", drive_short="our home base",
    h1="Pest management in Warwick, from the suburb we live in.",
    lead="DJ Pest is based in Warwick. When something is running around your roof void on Beach Road or ants have found the kitchen off Erindale Road, we're already in the postcode.",
    intro=[
        "Warwick was laid out in the late 1960s and built through the 1970s, and most of the suburb still looks like it: brick veneer and double brick homes on quarter-acre blocks, tiled roofs on timber framing, and gardens that have had fifty years to mature. The suburb sits on the Spearwood dune system, which means yellow-brown Karrakatta sand that drains fast and stays warm well into autumn. That is comfortable for people and very comfortable for subterranean termites, coastal brown ants and the black rats that use mature trees as a highway to the roof.",
        "The other thing that shapes pest pressure here is Warwick Open Space. It is a large tract of remnant banksia woodland in the middle of the suburb, and it is a good thing to have. It also means the streets around it (and around the Warwick Leisure Centre and the train station end of the suburb) carry more spiders, more native cockroaches in autumn and more rodent traffic in winter than a street with nothing but lawn for a kilometre in every direction. We factor that into how we treat, not just what we treat.",
    ],
    pests=[
        ("Termites", "Fifty-year-old timber roof framing, timber pergolas built straight onto sandy soil and garden beds pushed hard up against the slab. Warwick homes tick every box. Many have never had an <a href=\"/termite-inspection-perth\">AS 4349.3 inspection</a>."),
        ("Coastal brown ants", "The dominant nuisance ant across the suburb. They nest in the sand under paving and along retaining walls and run a super-colony across several properties, which is why a repellent spray from the hardware store makes them worse."),
        ("Rats in the roof", "Black rats climb. Mature peppermints, olive trees and old grapevines against the eaves are the usual route into a 1970s roof void. Sealing the gaps matters more than the bait."),
        ("Spiders and cockroaches", "Redbacks under coping and inside meter boxes, native cockroaches wandering in from the Open Space in autumn. Both are handled inside a <a href=\"/general-pest-control-perth\">general pest treatment</a>."),
    ],
    now="It is spring in Warwick. The sand has warmed, coastal brown ant trails are reappearing along paths and pool surrounds, and redbacks are setting up under outdoor furniture. Termite swarms usually start on the first warm, humid evenings from November, so this is the month to book an inspection if the house has not had one in the last year.",
    neighbours=["Greenwood", "Duncraig", "Balcatta"],
    faqs=[
        ("Do you charge a call-out fee in Warwick?", "No. There is no call-out fee anywhere in our service area, and Warwick is where we are based, so there is no travel component in a Warwick quote at all. Every job is quoted itemised in writing before we start."),
        ("My 1970s Warwick home has never had a termite inspection. Is that a problem?", "It is a gap worth closing. Timber roof framing, sandy soil and mature gardens are the three things termites want, and a home built before physical termite barriers were standard has none of the protection a newer estate home has. An <a href=\"/termite-inspection-perth\">inspection to AS 4349.3</a> takes about an hour and gives you a written report with photos."),
        ("Why do the ants come back after I spray them?", "Almost every persistent ant in Warwick is the coastal brown ant, which lives in a linked super-colony under paving, lawn and neighbouring yards. A repellent spray kills the foragers you can see and pushes the colony to bud into new nests. We use slow-acting non-repellent products and baits so the workers carry the treatment home. <a href=\"/ant-control-perth\">How we treat ants</a>."),
        ("Do you treat homes backing onto Warwick Open Space differently?", "Slightly. We spend more time on the external harbourage side: eaves, weep holes, retaining walls, sheds and the fence line facing the bush, and we talk through rodent proofing at the roofline because tree cover gives rats a direct route. The chemistry is the same; the emphasis shifts."),
        ("How quickly can you get to a Warwick job?", "Usually same day for active rodents, wasps or a termite find, and within a day or two for a routine treatment. We are in the suburb, so a Warwick call is the easiest one on the run sheet."),
    ]),
"Greenwood": dict(
    postcode="6024", drive="about 5 minutes", drive_short="5 minutes",
    h1="Pest management in Greenwood, five minutes from our base.",
    lead="Greenwood shares Warwick's postcode, its soil and its 1970s housing stock. It also shares our attention: it is the first suburb north of the depot and one we are in most weeks.",
    intro=[
        "Greenwood was developed in the 1970s and early 1980s on the same yellow Spearwood sand as Warwick. The housing is mostly single-storey brick veneer and double brick with tiled roofs on timber framing, plus a run of later two-storey rebuilds and a few newer infill lots near Greenwood train station and the freeway. Blocks are big by modern standards and gardens are established, which is good for shade and good for pests: mulched beds against the slab, timber retaining, fruit trees, and reticulation keeping the sand moist through summer.",
        "The suburb is boxed in by Wanneroo Road on the east and the Mitchell Freeway on the west, with Warwick Open Space to the south and Kingsley's lake-and-bush country to the north. So while Greenwood itself is mostly houses and parks, pests move in from bushland on two sides. Rodents come in from the road reserves and rail corridor in winter; spiders and native cockroaches come in from the remnant bush in autumn.",
    ],
    pests=[
        ("Termites", "Same story as Warwick: old timber framing, sandy soil, garden beds over the slab edge. Greenwood homes with timber patios or old pine sleeper retaining walls are the ones we see most termite activity in. <a href=\"/termite-inspection-perth\">Book an inspection</a>."),
        ("Coastal brown ants", "Everywhere in Greenwood. Trails across paving, nests under pavers and along the edge of the lawn, and a kitchen incursion the moment the retic goes on. Treated as a colony, not a trail. <a href=\"/ant-control-perth\">Ant management</a>."),
        ("Rats and mice", "Roof voids with timber framing and sarking are warm and quiet. Entry is usually a lifted tile, an open eave gap or a gap around a flue. <a href=\"/rodent-control-perth\">Rodent management</a> here is mostly a proofing job."),
        ("German cockroaches", "Older kitchens with original cabinetry have voids and gaps behind kickboards that German cockroaches love. Gel bait plus an insect growth regulator, not a spray."),
    ],
    now="Spring in Greenwood means ant trails are back on the driveways, redbacks are appearing under eaves and outdoor furniture, and the first paper wasp nests are being built under pergola beams. If the house has a timber roof frame and has not been inspected for termites in a year, book before swarm season in November.",
    neighbours=["Warwick", "Duncraig", "Joondalup"],
    faqs=[
        ("How far is Greenwood from your base?", "About five minutes. We are in Warwick, immediately south, so Greenwood jobs are among the easiest for us to fit in, including same-day for active pests."),
        ("Is Greenwood a high termite-risk suburb?", "It is a typical northern-suburbs risk, which is meaningful. Sandy soil, homes built in the 1970s and 1980s with timber roof framing and no physical barrier, and mature gardens against the slab. We recommend an inspection to AS 4349.3 every 12 months and can install a chemical management system to AS 3660.2 if activity or high risk is found."),
        ("What do you use inside a Greenwood kitchen for cockroaches?", "Gel baits and an insect growth regulator placed in the cabinetry voids and around plumbing penetrations, plus a non-staining product where a surface treatment is needed. No wet spray over benchtops. <a href=\"/cockroach-control-perth\">Cockroach management</a>."),
        ("Can you treat the rodents in my roof without poison?", "Often, yes. Trapping and proofing are the first tools where there are pets, kids or a preference for no rodenticide. Where baits are used they go in tamper-resistant stations only, and we explain placement and re-entry before we start."),
        ("What does a general pest treatment cost in Greenwood?", "A typical three-bedroom home, internal and external, sits in the $250 to $350 range. Every job is quoted itemised in writing. <a href=\"/pest-control-prices-perth\">See the investment guide</a>."),
    ]),
"Duncraig": dict(
    postcode="6023", drive="about 10 minutes", drive_short="10 minutes",
    h1="Pest management in Duncraig, where the sand meets the limestone.",
    lead="Duncraig sits between the inland sands and the coastal limestone ridge, with Carine Regional Open Space on its southern edge. That mix shapes what turns up in your home.",
    intro=[
        "Duncraig was developed through the 1970s and 1980s, and the original stock is mostly double brick and brick veneer with tiled roofs on timber framing. It has been one of the busiest suburbs in Perth for knock-down rebuilds, so a single street can have a 1975 brick-and-tile next to a two-storey home built last year. Both get pests, for different reasons: the old house has timber framing, established gardens and a roof that has settled and opened up; the new one has a slab with plumbing penetrations, fresh garden beds and neighbours whose termites did not go anywhere.",
        "Soil changes across the suburb. The eastern side, towards Warwick and the freeway, is yellow Spearwood sand. Towards Marmion Avenue the sand thins over Tamala limestone, the same ridge that runs under Sorrento and Hillarys. Carine Regional Open Space, with its lakes and paperbark swamp, sits directly to the south, and Percy Doyle Reserve is in the middle of the suburb. Wetland edge and remnant bush mean mosquitoes in summer, native cockroaches and spiders in autumn, and rodents through winter for the streets that back onto them.",
    ],
    pests=[
        ("Termites", "Both housing generations carry risk. The 1970s homes for their timber framing and gardens, the rebuilds because a chemical barrier is only as good as the landscaping that came after it. <a href=\"/termite-inspection-perth\">Inspections</a> and <a href=\"/termite-treatment-perth\">management systems</a> to AS 3660.2."),
        ("Coastal brown ants", "Duncraig's limestone-and-sand mix suits them. Nests under paving and in retaining walls, super-colonies across fence lines. Non-repellent treatment and baits only. <a href=\"/ant-control-perth\">Ant management</a>."),
        ("Rodents", "Streets bordering Carine Open Space and the bush around Percy Doyle Reserve see the most winter rat activity. Proofing at the eaves and roof penetrations comes first. <a href=\"/rodent-control-perth\">Rodent management</a>."),
        ("Spiders and mosquitoes", "Redbacks and black house spiders under coping and in meter boxes; mosquitoes on the wetland side from late spring. Spiders are covered in a <a href=\"/general-pest-control-perth\">general pest treatment</a>."),
    ],
    now="Spring in Duncraig: ants are re-establishing trails, spiders are building along fences and pergolas, and the wetland at Carine will start producing mosquitoes as the weather warms. It is a good month for an external perimeter treatment and, if it has been a year, a termite inspection before November's swarms.",
    neighbours=["Warwick", "Sorrento", "Greenwood"],
    faqs=[
        ("I have just bought a rebuilt home in Duncraig. Do I still need termite inspections?", "Yes. New homes are built with a termite management system, but the certificate normally requires an annual inspection to stay valid, and garden beds, paving and retic added after handover can bridge the barrier. An <a href=\"/termite-inspection-perth\">AS 4349.3 inspection</a> every 12 months protects the house and the paperwork."),
        ("Why are there more rats near Carine Open Space?", "Wetland edges and paperbark swamp give rats water, cover and food all year. In winter they look for warm, dry voids and a 1970s roof is ideal. We seal the entry points and place tamper-resistant stations rather than relying on bait alone."),
        ("Is Duncraig's limestone a problem for termite treatment?", "It changes the method, not the outcome. Where limestone sits close to the surface we drill and inject rather than trench, and we test soil uptake so the non-repellent treatment forms a continuous treated zone. That is standard practice under AS 3660.2 and it is written into your treatment record."),
        ("How long does a general pest treatment take in a Duncraig home?", "About an hour to ninety minutes for a typical three or four-bedroom home, internal and external. You stay out of treated areas until surfaces are dry, usually two hours, and we tell you the re-entry period before we begin."),
        ("How far are you from Duncraig?", "About ten minutes from our base in Warwick, along Warwick Road or Beach Road. Same-day for active pests is usually possible."),
    ]),
"Sorrento": dict(
    postcode="6020", drive="about 12 minutes", drive_short="12 minutes",
    h1="Pest management in Sorrento, on the limestone above the marine park.",
    lead="Sorrento is coastal dune and Tamala limestone, salt air and a housing mix from 1970s brick-and-tile to new two-storey rebuilds on West Coast Drive. Pest management here is different from the inland suburbs and we treat it that way.",
    intro=[
        "Sorrento runs from the ocean at Marmion Marine Park up the ridge to Marmion Avenue. The foreshore streets sit on young white Quindalup dune sand; a few hundred metres back the ground becomes shallow yellow sand over Tamala limestone, the hard cap that gives the suburb its slope and its sea views. Limestone matters for termites in two ways. It is close to the surface, so a chemical management system is usually installed by drilling and injecting rather than trenching. And it holds moisture in pockets, which subterranean termites use in summer when the surface sand is bone dry.",
        "The housing is a genuine mix. Original 1970s and 1980s double brick and brick veneer with timber roof framing is still common on the inland side, while the ocean-facing streets have been steadily rebuilt into large two-storey homes with steel and timber framing, cavity walls and alfresco areas hard up against the slab. Salt air corrodes the metal flashings and mesh that keep rodents out, and the coastal breeze pushes flying ants and termite alates inland on swarm nights. Seacrest Park and the reserves along the coast, plus the busy edge of Hillarys Boat Harbour next door, keep the rodent population healthy year-round.",
    ],
    pests=[
        ("Termites", "Limestone pockets, old timber framing and rebuilt homes whose barriers were bridged by landscaping. Inspections to AS 4349.3 and drill-and-inject systems to AS 3660.2. <a href=\"/termite-treatment-perth\">Termite treatment</a>."),
        ("Coastal brown ants", "The name is not a coincidence. Sorrento is core coastal brown ant country: super-colonies under paving, limestone retaining walls and pool surrounds. <a href=\"/ant-control-perth\">Colony-level treatment</a>, never a repellent spray."),
        ("Rats", "Coastal reserves, the harbour precinct and salt-corroded roof flashings. Winter rodent work in Sorrento is a proofing job as much as a baiting one. <a href=\"/rodent-control-perth\">Rodent management</a>."),
        ("Spiders and cockroaches", "Redbacks under limestone coping and in retic boxes, black house spiders on rendered walls, American cockroaches from sewer and stormwater lines on the lower streets. <a href=\"/general-pest-control-perth\">General pest treatment</a>."),
    ],
    now="Spring on the coast: coastal brown ants are the first thing most Sorrento residents notice as the paving warms, followed by redbacks under outdoor furniture. Sea breeze evenings in November and December are when termite alates fly, so an inspection now catches anything that established last summer.",
    neighbours=["Duncraig", "Hillarys", "Warwick"],
    faqs=[
        ("Does salt air change how you treat a Sorrento home?", "It changes the proofing advice. Galvanised mesh and flashings corrode faster near the ocean, so gaps at eaves and roof penetrations open up sooner and rodents find them. We recommend stainless or aluminium mesh for sealing and we check the roofline more carefully than we would inland."),
        ("Can a chemical termite barrier be installed on limestone?", "Yes. Where the limestone is close to the surface we drill through paving or into the ground at close centres and inject the non-repellent product to label, rather than trenching. The result is a continuous treated zone to AS 3660.2, documented with a plan and certificate."),
        ("Why are coastal brown ants so bad in Sorrento?", "Warm, well-drained sand over limestone is the habitat they were named for. They form linked super-colonies with many queens across several properties. Repellent sprays split the colony; slow-acting non-repellent products and baits collapse it. <a href=\"/ant-control-perth\">Read more</a>."),
        ("Do you service the units and strata complexes along West Coast Drive?", "Yes. We treat strata common areas and individual units, and we document each area treated so the strata manager has a clear record. Ask about a combined external treatment across a complex; it is more effective than treating one unit at a time."),
        ("How long from Warwick to Sorrento?", "About twelve minutes along Warwick Road and Marmion Avenue. Same-day for active pests is usually possible."),
    ]),
"Hillarys": dict(
    postcode="6025", drive="about 12 minutes", drive_short="12 minutes",
    h1="Pest management in Hillarys, from the harbour to Whitford City.",
    lead="Hillarys is a coastal suburb with a lot going on: the boat harbour, Westfield Whitford City, Whitfords Nodes, and a broad band of 1980s and 1990s housing between them. That activity brings pests in, and the limestone underneath keeps them there.",
    intro=[
        "Hillarys was developed mostly in the 1980s and early 1990s, a little later than Sorrento and Duncraig, so the typical home is double brick with a tiled roof on timber framing and a bigger floorplan, often with an alfresco and a pool added later. The suburb sits on the same Tamala limestone ridge as Sorrento, with white Quindalup dune sand along the foreshore at Whitfords Nodes and Hillarys Beach Park, and yellow Spearwood sand towards the Whitfords Avenue end. Pools, paving and limestone retaining walls are everywhere, and all three are prime coastal brown ant real estate.",
        "The two big pest engines in Hillarys are food and water. Hillarys Boat Harbour and the Whitford City precinct produce constant food waste, which supports rats, mice and American cockroaches that then move into the surrounding streets. The coastal reserves along the dunes give rodents and spiders cover. Add a summer of reticulation on sandy soil and you have moisture under the slab edge that termites will follow. None of this is unusual for a coastal suburb; it just means a one-off spray is not a plan.",
    ],
    pests=[
        ("Coastal brown ants", "Hillarys is probably the suburb we treat for ants most. Pool surrounds, paving and limestone walls host super-colonies. Non-repellent product and baits, treated as a colony. <a href=\"/ant-control-perth\">Ant management</a>."),
        ("Rats and mice", "Harbour and shopping precincts feed them; roof voids and sheds house them. We proof first, then station. <a href=\"/rodent-control-perth\">Rodent management</a>."),
        ("Termites", "1980s and 1990s homes with timber framing, limestone pockets holding moisture and gardens over the slab edge. <a href=\"/termite-inspection-perth\">Annual inspection</a> is the sensible baseline."),
        ("Cockroaches and spiders", "American cockroaches from drains on the lower streets, German cockroaches in busier kitchens, redbacks in retic boxes and under coping. <a href=\"/general-pest-control-perth\">General pest treatment</a>."),
    ],
    now="Spring in Hillarys: ant trails across the pool paving, redbacks under outdoor furniture and the first wasp nests under eaves. Pools are about to be opened for summer, which is when most people notice the ants. Book an external treatment now rather than in December.",
    neighbours=["Sorrento", "Duncraig", "Joondalup"],
    faqs=[
        ("Why do I get so many ants around my pool in Hillarys?", "Warm paving, moisture from splash and backwash, and sandy fill under the coping. Coastal brown ants nest in exactly that. A repellent spray around the pool moves them, it does not remove them. We use slow-acting non-repellent products and baits and treat the whole colony footprint. <a href=\"/ant-control-perth\">More on ants</a>."),
        ("Do you treat businesses near Hillarys Boat Harbour and Whitford City?", "Yes. Cafes, retail and strata around the harbour and the shopping precinct get a documented program: rodent stations, cockroach gel and IGR in kitchens, and a treatment record kept for three years as WA regulations require."),
        ("Is my 1990s Hillarys home at risk from termites?", "Yes, at typical northern-suburbs levels. It has timber roof framing, sandy soil and, by now, mature gardens. If it has never had an inspection to AS 4349.3 it is time. If activity is found, a chemical management system to AS 3660.2 is the usual fix."),
        ("What is the re-treatment promise on an ant job?", "External ant treatments carry a three-month re-treatment period. If the treated colony is still active in the treated area inside that window we come back at no charge. <a href=\"/warranty\">Full terms</a>."),
        ("How far is Hillarys from Warwick?", "About twelve minutes via Warwick Road, Marmion Avenue or Hepburn Avenue. Same-day for active pests is usually possible."),
    ]),
"Joondalup": dict(
    postcode="6027", drive="15 to 20 minutes", drive_short="15 to 20 minutes",
    h1="Pest management in Joondalup, on the edge of Yellagonga.",
    lead="Joondalup's tree-lined streets and sandy soil are appealing, and termites think so too. Lake Joondalup and Yellagonga Regional Park sit on one side, pine plantation and bush to the north, and a large volume of 1990s to 2010s housing in between.",
    intro=[
        "Joondalup is one of the youngest of our core suburbs. The city centre and the surrounding residential areas were built from the late 1980s through the 2010s, so most homes are slab-on-ground double brick with tiled or metal roofs on timber or steel framing, on smaller blocks than Warwick or Duncraig. Newer estates were built with a termite management system, but the certificate that came with the house usually requires annual inspections, and most have lapsed. Landscaping added since handover, garden beds, paving, retic and alfresco slabs, is the most common thing we find bridging a barrier.",
        "Three things make Joondalup a busier pest suburb than the housing age suggests. The soil is Spearwood sand, warm and well drained. Lake Joondalup and Yellagonga Regional Park, with Neil Hawkins Park on the lake edge, are a large wetland and bush system that supports mosquitoes, native cockroaches, spiders and a year-round rodent population. And the pine plantations and bushland north of the suburb are, in plain terms, a working termite nursery. Around the city centre, Lakeside Joondalup, Edith Cowan University and the Joondalup Health Campus, food waste keeps rats, mice and American cockroaches well fed.",
    ],
    pests=[
        ("Termites", "Coptotermes acinaciformis, Perth's most destructive subterranean termite, in sandy fill under slabs. Lapsed barrier certificates and bridged barriers are the usual finding. <a href=\"/termite-inspection-perth\">Inspection</a>, then <a href=\"/termite-treatment-perth\">treatment</a> to AS 3660.2 if needed."),
        ("Coastal brown ants", "Common across the suburb, worse towards the coast. Non-repellent treatment and baits so workers carry it back to the colony. <a href=\"/ant-control-perth\">Ant management</a>."),
        ("Rats in the roof", "Black rats enter through gutter joints, unsealed eaves and roof penetrations. Seal first, then tamper-resistant stations, then a follow-up check. <a href=\"/rodent-control-perth\">Rodent management</a>."),
        ("Spiders, cockroaches and mosquitoes", "Redbacks under coping and in sheds, German cockroaches in busy kitchens, mosquitoes on the lake side in summer. <a href=\"/general-pest-control-perth\">General pest treatment</a>."),
    ],
    now="Spring in Joondalup: ant trails are back, spiders are active along fences and eaves, and the lake edge will start producing mosquitoes as the evenings warm. Termite swarms usually begin on humid evenings in November, so an inspection now is well timed for homes near Yellagonga and the northern bush.",
    neighbours=["Wanneroo", "Hillarys", "Greenwood"],
    faqs=[
        ("How common are termites in Joondalup?", "Common. Sandy soil, pine plantation and bushland to the north, and a large volume of homes built between the 1990s and 2010s with barrier certificates that have lapsed. We recommend an inspection to AS 4349.3 every 12 months for any Joondalup home, and it is the condition of most termite management system certificates anyway."),
        ("How much does termite treatment cost in Joondalup?", "A timber pest inspection is typically $250 to $350. A chemical termite management system to AS 3660.2 is typically $2,500 to $5,500 depending on the perimeter and construction; baiting systems are typically $1,500 to $3,000 plus monitoring. Every job is quoted itemised in writing. <a href=\"/pest-control-prices-perth\">Investment guide</a>."),
        ("How fast can you get to Joondalup?", "We are based in Warwick, 15 to 20 minutes south along the freeway. Same-day or next-day is usual, and active termites or a rodent emergency are fast-tracked."),
        ("Do you cover the suburbs around Joondalup?", "Yes: Currambine, Kinross, Ocean Reef, Mullaloo, Woodvale, Kingsley and the rest of the City of Joondalup. Edgewater, Connolly, Heathridge, Beldon and Iluka are also on our regular run. <a href=\"/service-areas\">Full service area</a>."),
        ("Are coastal brown ants a problem in Joondalup?", "Yes, particularly in the streets closer to the coast. They form super-colonies that do not respond to repellent sprays. We use slow-acting non-repellent products and baits so the colony collapses, not just the foragers you can see."),
    ]),
"Wanneroo": dict(
    postcode="6065", drive="15 to 20 minutes", drive_short="15 to 20 minutes",
    h1="Pest management in Wanneroo, market-garden country turned suburb.",
    lead="Wanneroo grew from market gardens on the eastern shore of Lake Joondalup into a suburb with bigger blocks, older homes, rural fringes and new estates. Pests here are shaped by that history and by the wetland next door.",
    intro=[
        "Wanneroo is different from the coastal and freeway suburbs. It sits on the eastern shore of Lake Joondalup, in the northern reach of Yellagonga Regional Park, where the soil shifts from yellow Spearwood sand to the grey, older Bassendean sands that made the area good for market gardens. The town centre around Wanneroo Road and Wanneroo Central has homes from the 1970s onward; the streets around the showgrounds and Rotary Park carry 1980s and 1990s brick-and-tile on generous blocks; and the edges of the suburb still have semi-rural lots with sheds, stables, dams and stored timber. New estates continue to fill in the gaps.",
        "Lake Joondalup is the big driver. It is a large, shallow wetland with paperbark and reed fringes, and it supports mosquitoes in warm months, a year-round rodent population and plenty of native insects. The old market-garden ground is rich in organic matter and moisture, which subterranean termites appreciate as much as tomatoes did. Big blocks mean timber sheds, fence lines, firewood stacks and horse yards, all of which are termite food and rodent harbourage. Carramar Golf Course and the bush corridors to the north keep the pressure steady.",
    ],
    pests=[
        ("Termites", "Moist organic soils, timber sheds and fence posts in the ground, and 1970s to 1990s homes with timber framing. Rural-fringe lots need the outbuildings inspected too. <a href=\"/termite-inspection-perth\">Timber pest inspection</a>."),
        ("Rats and mice", "Sheds, feed, firewood and the lake edge. Wanneroo rodent work usually means a proofing plan for the outbuildings as well as the house. <a href=\"/rodent-control-perth\">Rodent management</a>."),
        ("Mosquitoes and midges", "Lake Joondalup produces them from spring through autumn. We treat harbourage and resting zones around the home and advise on water sources on the property."),
        ("Ants, spiders and cockroaches", "Coastal brown ants on the sand, black ants around sheds, redbacks in stored timber and meter boxes, Australian cockroaches from mulch and compost. <a href=\"/general-pest-control-perth\">General pest treatment</a> and <a href=\"/ant-control-perth\">ant management</a>."),
    ],
    now="Spring in Wanneroo: ants are trailing, spiders are active in sheds and around stacked timber, and the lake will start producing mosquitoes and midges as evenings warm. Firewood stacks left over from winter are a termite and redback risk; move them off the ground and away from the house. Book a termite inspection before November's swarms.",
    neighbours=["Joondalup", "Greenwood", "Warwick"],
    faqs=[
        ("Do you inspect sheds and outbuildings on larger Wanneroo blocks?", "Yes, and we recommend it. On rural-fringe lots the shed, stable or timber fence line is often where termites are found first. A timber pest inspection to AS 4349.3 covers the house and, at your request, the outbuildings and grounds, with photos and a written report."),
        ("How do you handle mosquitoes near Lake Joondalup?", "We cannot treat the lake and would not want to. What we can do is treat the resting and harbourage zones around your home, dense foliage, under decks, shaded walls, and identify water sources on the property such as pot bases, gutters and troughs. We advise on screens and timing as well."),
        ("What is the difference between the sands in Wanneroo and the coastal suburbs?", "Coastal suburbs are on yellow Spearwood sand over limestone. Much of Wanneroo is on older grey Bassendean sand with a higher organic content and a shallower water table near the lake. It holds moisture longer, which supports termite activity and makes correct application of a chemical management system important; we test uptake and document it."),
        ("Do you treat horses' yards and feed sheds for rodents?", "Yes. Feed storage and stables are rodent magnets. We use tamper-resistant stations positioned away from animals, advise on sealed feed bins and proofing, and provide a written treatment record so you know exactly what is in place and where."),
        ("How far is Wanneroo from your base?", "15 to 20 minutes from Warwick via Wanneroo Road. We are in the suburb regularly, so routine bookings are easy to fit in and active pests are fast-tracked."),
    ]),
"Balcatta": dict(
    postcode="6021", drive="about 10 minutes", drive_short="10 minutes",
    h1="Pest management in Balcatta, homes and warehouses side by side.",
    lead="Balcatta is one of the older suburbs on our run, with 1960s and 1970s brick homes, a large industrial precinct and the Hamersley golf course and Lake Gwelup wetland close by. Residential and commercial pest work sit next to each other here.",
    intro=[
        "Balcatta was developed through the 1960s and 1970s, earlier than Warwick, on Italian market-garden land. The original homes are double brick with tiled roofs on timber framing, often on big blocks with a shed, a productive backyard and a grapevine or fig that has been there fifty years. Many have been extended, and some streets are turning over to new two-storey rebuilds and grouped dwellings. The soil is yellow Spearwood sand, well drained and warm. Old fruit trees, timber sheds, compost and years of garden beds against the slab edge give termites, ants and rodents everything they need.",
        "The other half of Balcatta is the industrial area between Erindale Road and Wanneroo Road, one of the biggest in the northern suburbs. Warehouses, food processors, workshops and the Northlands and Roselea shopping centres produce a steady rodent and cockroach population that spills into the surrounding streets. Add Hamersley Public Golf Course on one side and Lake Gwelup's wetland reserve to the west, and Balcatta has both the urban and the bushland pest sources in one postcode.",
    ],
    pests=[
        ("Rats and mice", "Industrial food waste, old sheds and timber-framed roof voids. Balcatta is a rodent suburb in winter. We proof the roofline, place tamper-resistant stations and follow up. <a href=\"/rodent-control-perth\">Rodent management</a>."),
        ("Termites", "1960s and 1970s timber framing, fifty-year-old fruit trees, timber sheds and garden beds over the slab. Annual <a href=\"/termite-inspection-perth\">inspection to AS 4349.3</a> is overdue for most of the suburb."),
        ("Cockroaches", "American cockroaches from drains and the industrial precinct, German cockroaches in busy kitchens and food businesses. Gel bait and IGR programs, non-staining products indoors. <a href=\"/cockroach-control-perth\">Cockroach management</a>."),
        ("Ants and spiders", "Coastal brown ants along paving and retaining walls, black ants in vegetable gardens, redbacks in sheds and under old garden furniture. <a href=\"/ant-control-perth\">Ant management</a> and <a href=\"/general-pest-control-perth\">general pest treatment</a>."),
    ],
    now="Spring in Balcatta: ant trails across paving and into the veggie patch, spiders active in sheds and along fences, and roof rats that spent winter in the ceiling are now breeding. Book an inspection for older timber-framed homes before termite swarm season starts in November.",
    neighbours=["Warwick", "Duncraig", "Greenwood"],
    faqs=[
        ("Do you service warehouses and food businesses in the Balcatta industrial area?", "Yes. We set up documented rodent station programs, cockroach gel and IGR treatments in kitchens and food areas, and keep a treatment record for three years as the Health (Pesticides) Regulations require. Itemised investment, and a service report after every visit for your own audit file."),
        ("My Balcatta home is from the 1960s with the original roof. Is that a termite risk?", "Yes. Original timber framing, sandy soil, mature trees and decades of garden beds against the slab edge are the classic combination. A timber pest inspection to AS 4349.3 gives you a written, photographed answer. If activity is found, a chemical management system to AS 3660.2 is the usual fix."),
        ("Where are the rats coming from?", "In Balcatta, most often the industrial precinct and older sheds, then into roof voids through gaps at eaves, gutter lines and unsealed penetrations. We find and seal the entry points first. Bait alone in Balcatta is a treadmill."),
        ("Can you treat my vegetable garden for ants without harming the plants?", "We treat the nests and trails on paving, edges and retaining walls with products applied to label and keep treatment out of edible beds. Baits are placed in stations rather than spread. We explain what has been applied and where in your treatment record."),
        ("How far is Balcatta from Warwick?", "About ten minutes down Wanneroo Road or Erindale Road. Same-day for active rodents or wasps is usually possible."),
    ]),
}


def pages(c):
    S = c["SITE"]; esc = c["esc"]; icon = c["icon"]
    out = []

    def svc_cards():
        return ('<div class="grid grid-4">'
            + c["card"]("Termite inspection", "AS 4349.3 timber pest inspection with photos, moisture readings and a written report.", "/termite-inspection-perth", "Termites")
            + c["card"]("General pest treatment", "Cockroaches, spiders, silverfish and ants, internal and external, with a six-month re-treatment promise.", "/general-pest-control-perth", "General")
            + c["card"]("Ant management", "Coastal brown ant super-colonies treated with non-repellents and baits, not a quick spray.", "/ant-control-perth", "Ants")
            + c["card"]("Rodent management", "Species identified, entry points sealed, tamper-resistant stations placed and checked.", "/rodent-control-perth", "Rodents")
            + '</div>')

    def investment_note(sub):
        return (f'<div class="callout"><p><strong>The investment in {esc(sub)}.</strong> A general pest treatment for a three-bedroom home is typically $250 to $350, an external ant treatment $250 to $400, '
                f'a rodent program $220 to $380 and a timber pest inspection $250 to $350. Typical ranges only; every job is quoted itemised in writing before we start, with no call-out fee and no deposit. '
                f'<a href="/pest-control-prices-perth">See the full investment guide</a>.</p></div>')

    # ----------------------------------------------------------- suburb pages
    for name, d in SUBURBS.items():
        hero = f"""<section class="hero"><div class="wrap"><div>
  {c['eyebrow'](f"Pest management · {name} WA {d['postcode']} · {d["drive_short"] + (" from our Warwick base" if name != "Warwick" else "")}")}
  <h1>{esc(d['h1'])}</h1>
  <p class="lead">{esc(d['lead'])}</p>
  {c['hours_cue']()}<div class="actions">{c['btn_call']()}{c['btn_quote']()}</div>
  <ul class="trust"><li>Licensed technicians</li><li>In Perth pest management since {S['family_since']}</li><li>Itemised investment in writing</li><li>Same-day for active pests</li></ul>
</div></div></section>"""

        intro = c["section"](
            c["eyebrow"](f"Why {name} gets the pests it gets")
            + '<div class="prose">' + "".join(f"<p>{p}</p>" for p in d["intro"]) + "</div>", "ledger")

        pests = c["section"](
            c["eyebrow"](f"What we treat most in {name}")
            + f'<div class="section-head"><h2>The {name} pest short-list.</h2></div>'
            + '<div class="grid grid-2">' + "".join(c["card"](t, x) for t, x in d["pests"]) + "</div>")

        now = c["section"](
            c["eyebrow"]("What's active now")
            + f'<div class="prose"><h2>This season in {name}.</h2><p>{d["now"]}</p></div>'
            + c["season_strip"](), "ledger")

        services = c["section"](
            c["eyebrow"]("Services") + f'<div class="section-head"><h2>Four jobs we do every week in {name}.</h2></div>' + svc_cards() + investment_note(name))

        nb = "".join(c["card"](n, f"Pest management in {esc(n)}, {DRIVE[n]} from Warwick.", slug(n), "Neighbouring suburb", more="See suburb page") for n in d["neighbours"])
        neighbours = c["section"](
            c["eyebrow"]("Nearby")
            + f'<div class="section-head"><h2>Also servicing the suburbs around {name}.</h2><p class="lead">Based in Warwick, {name} is {d["drive"]} away. <a href="/service-areas">All service areas</a>.</p></div>'
            + '<div class="grid grid-3">' + nb + "</div>", "ledger")

        faq_sec = c["section"](c["eyebrow"]("Questions") + f'<div class="section-head"><h2>Asked in {name}.</h2></div>' + c["faq"](d["faqs"]))

        body = hero + intro + pests + now + services + neighbours + faq_sec + c["quote_block"](f"Get a fair, itemised investment in {name}.")
        out.append({
            "path": slug(name),
            "title": f"Pest Control {name} | Termites, Ants, Rodents | DJ Pest",
            "desc": f"Licensed pest control in {name} WA {d['postcode']}, {d['drive']} from our Warwick base. Termite inspections, ants, rodents and general pest. Itemised prices in writing.",
            "body": body,
            "crumbs": [("Service areas", "/service-areas"), (name, None)],
            "schema": [{
                "@type": "Service", "serviceType": f"Pest management in {name}",
                "description": f"Termite inspection, general pest, ant and rodent management for {name} homes and businesses, {d['drive']} from DJ Pest's base in Warwick.",
                "provider": {"@id": S["domain"] + "/#business"},
                "areaServed": {"@type": "City", "name": name, "containedInPlace": {"@type": "AdministrativeArea", "name": "Perth, Western Australia"}},
                "offers": {"@type": "Offer", "priceCurrency": "AUD", "price": 250,
                           "priceSpecification": {"@type": "PriceSpecification", "minPrice": 250, "maxPrice": 5500, "priceCurrency": "AUD"}},
            }, c["faq_schema"](d["faqs"])],
        })

    # -------------------------------------------------------------- hub page
    hub_hero = f"""<section class="hero"><div class="wrap"><div>
  {c['eyebrow']("Service areas · Based in Warwick WA 6024")}
  <h1>We keep the service area tight <em class="red">on purpose</em>.</h1>
  <p class="lead">DJ Pest works Perth's northern suburbs from a base in Warwick, and we do not stretch beyond them. That keeps response times short, means we know each suburb's soil, housing and pest pressure first-hand, and keeps travel out of your quote.</p>
  {c['hours_cue']()}<div class="actions">{c['btn_call']()}{c['btn_quote']()}</div>
</div></div></section>"""

    why = c["section"](
        c["eyebrow"]("Why not all of Perth")
        + '<div class="grid grid-2" style="align-items:start;gap:3rem"><div class="prose">'
        '<h2>Thirty suburbs, one technician who knows them.</h2>'
        '<p>Most of our work is within fifteen minutes of Warwick. From the depot, Greenwood and Hamersley are five minutes, Duncraig and Balcatta ten, the coast at Sorrento and Hillarys twelve, and Joondalup and Wanneroo fifteen to twenty. The far north, from Clarkson to Yanchep, is on the run sheet but grouped so the drive is not padded into your investment.</p>'
        '<p>The northern suburbs are not one place. The coastal strip sits on Tamala limestone with salt air and a lot of rebuilds. The inland suburbs are yellow Spearwood sand with 1960s to 1980s timber-framed brick homes and mature gardens. The growth corridor north of Joondalup is slab-on-ground estates next to wetland, pine plantation and bush. Termites, coastal brown ants and rodents behave differently in each, and the treatment method changes with the ground. That is easier to get right when the technician has been on the same streets last week.</p>'
        '</div><div class="grid" style="gap:.8rem">'
        + c["card"]("No travel in the quote", "No call-out fee anywhere in the service area. Every job is quoted itemised in writing before we start.")
        + c["card"]("Same-day for active pests", "Rats in the roof, a wasp nest by the door or termites found during a renovation get fast-tracked. Routine treatments are usually within a few days.")
        + c["card"]("Our own technicians", "One of our own licensed technicians attends every job, and the technician who quotes is the one who treats. No subcontracted strangers.")
        + '</div></div>', "ledger")

    groups_html = ""
    for title, blurb, subs in GROUPS:
        lis = "".join(
            (f'<li><a href="{slug(s)}">{esc(s)}</a></li>' if s in PAGES8 else f'<li>{esc(s)}</li>') for s in subs)
        groups_html += f'<div class="card"><div class="num">{esc(title)}</div><h3>{len(subs)} suburbs</h3><p>{esc(blurb)}</p><ul style="columns:2;list-style:none;padding:0;margin:1rem 0 0;line-height:2;font-size:.95rem">{lis}</ul></div>'
    groups = c["section"](
        c["eyebrow"]("Every suburb we cover")
        + '<div class="section-head"><h2>Coast, inland and the growth corridor.</h2><p class="lead">Linked suburbs have their own page with local soil, housing and pest notes. The rest are on the same run and quoted the same way.</p></div>'
        + '<div class="grid grid-3">' + groups_html + '</div>')

    eight = c["section"](
        c["eyebrow"]("Suburb pages")
        + '<div class="section-head"><h2>Eight suburbs, in detail.</h2></div>'
        + '<div class="grid grid-4">' + "".join(
            c["card"](s, f"{esc(SUBURBS[s]['lead'].split('.')[0])}. {(DRIVE[s].capitalize() + ' from Warwick.') if s != 'Warwick' else 'Our home base.'}", slug(s), f"WA {SUBURBS[s]['postcode']}", more="Read the suburb page")
            for s in PAGES8) + '</div>', "ledger")

    rows = [(s, DRIVE[s].capitalize() if s != "Warwick" else "Base", "Yes" if s in PAGES8 else "On request") for s in S["service_area"]]
    drive = c["section"](
        c["eyebrow"]("Drive time from Warwick")
        + '<div class="section-head"><h2>Honest estimates, off-peak.</h2><p class="lead">Add ten minutes in school-run traffic on the freeway or Wanneroo Road. We schedule by area so you get a tight arrival window, not a four-hour one.</p></div>'
        + c["ledger_table"](["Suburb", "Typical drive from Warwick", "Suburb page"], [(esc(a), b, (f'<a href="{slug(a)}">Yes</a>' if cc == "Yes" else cc)) for a, b, cc in rows]))

    hub_faqs = [
        ("Do you service suburbs not on the list?", "Sometimes, if it is adjacent to the area, for example Trigg, North Beach, Scarborough or Edgewater. Ring and we will tell you straight. We do not take work south of the river or in the hills; the drive would end up in your investment and the service would suffer."),
        ("Is there a travel charge for the far northern suburbs?", "No call-out fee and no travel line on any quote. For Alkimos, Butler, Yanchep and Two Rocks we group bookings by day so the drive is absorbed in scheduling rather than charged to you. It may mean a day or two's wait for a routine job."),
        ("Why does the suburb matter for pest treatment?", "Soil and construction decide the method. A chemical termite management system on the limestone under Sorrento is drilled and injected; on the deep sand under Wanneroo it is trenched. A 1970s Warwick roof with timber framing is proofed differently from a 2015 Joondalup slab home. Knowing the ground saves you money and gets a better result."),
        ("Do you do strata and commercial work across the area?", "Yes: strata common areas, small commercial kitchens, warehouses in the Balcatta and Joondalup industrial precincts, and shopping strip tenancies. Every visit is documented with a treatment record kept for three years as WA regulations require."),
        ("How do I know you are licensed to work in my suburb?", f"Every treatment is carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence, which applies anywhere in the state. The technician's name and licence number are on your treatment record, and you can ask to see the licence card on the day. {esc(S['reg_line'])}"),
    ]
    hub_faq = c["section"](c["eyebrow"]("Questions") + '<div class="section-head"><h2>About where we work.</h2></div>' + c["faq"](hub_faqs))

    out.insert(0, {
        "path": "/service-areas",
        "title": "Pest Control Service Areas | Perth Northern Suburbs | DJ Pest",
        "desc": "DJ Pest services Perth's northern suburbs from Warwick: Greenwood, Duncraig, Sorrento, Hillarys, Joondalup, Wanneroo, Balcatta and 22 more. Drive times, suburb pages, no call-out fee.",
        "body": hub_hero + why + groups + eight + drive + hub_faq + c["quote_block"]("Get a fair, itemised investment anywhere in the northern suburbs."),
        "crumbs": [("Service areas", None)],
        "schema": [c["faq_schema"](hub_faqs), {
            "@type": "Service", "serviceType": "Pest management, Perth northern suburbs",
            "provider": {"@id": S["domain"] + "/#business"},
            "areaServed": [{"@type": "City", "name": s} for s in S["service_area"]],
        }],
    })
    return out
