# PANEL REVIEWER CRITIQUE — DJ PEST WEBSITE

## 1. FIRST-GLANCE VERDICT

A stressed homeowner at 9pm sees "Rats in the roof tonight? We fix it properly, and put it in writing" — a headline that names their exact problem and situation, with a sticky Call/Text bar always in thumb reach; that is close to best-in-class and they are primed to call. The one thing that could stall them in those five seconds is a dark, serif, editorial aesthetic that reads more "law firm" than "emergency help right now," plus zero visible faces, real photos, star ratings or a "we answer now" cue to confirm a human will pick up at 9pm. Net: yes, most call — but the site earns the click on copy, not on the visual proof-of-trust that converts the last hesitant 20%.

## 2. TOP 10 CHANGES (ranked by expected impact on phone calls)

**1. Add an "answered now / after-hours" cue next to the phone number in the hero and sticky bar** [high]
- Element: hero CTA + sticky bottom bar.
- Wrong/missing: "Rats in the roof tonight?" promises urgency but nothing tells the 9pm caller anyone will answer. Hours are Mon–Sat 7am–6pm (About), which *contradicts the "tonight" hook* — a caller at 9pm hits voicemail and feels tricked.
- Fix: Under the number add: "Call or text now — the technician answers, or you get a callback first thing. Mon–Sat 7am–6pm." If after-hours texts are triaged, say: "After hours? Text a photo to 0447 747 769 — we reply first thing." Resolve the contradiction between "tonight" and the stated hours honestly.
- Confidence: high.

**2. Fix the licensing FAQ sentence that is confusing and legally risky** [high]
- Element: Home + About + llms.txt: *"Until the certificate issues, every treatment is carried out and recorded under a registered pest management business."*
- Wrong/missing: This sentence is opaque and arguably implies DJ Pest *is* operating as/through a registered business while simultaneously saying its own registration is pending — it invites the exact r.9 "holding out" risk the constraint warns against. A reader cannot tell *whose* registration. If it means work is performed under a *third party's* registration, that must be stated plainly; if it does not, the sentence should be deleted.
- Fix (if under a third party): "While our own registration is pending, all work is performed and recorded under [an existing WA-registered pest management business / our supervising registered business], as WA law requires." If you cannot name or substantiate that arrangement, DELETE the sentence and keep only: "DJ Pest Pty Ltd's WA Department of Health pest management business registration is pending (PMB 3000 assigned)." **VERIFY with a WA pesticide-law solicitor before publishing either version** — this is the highest legal-exposure item on the site.
- Confidence: high (that it's a problem); the exact fix needs legal verification.

**3. Remove the leftover licence number "WA licence 13914" from the rodent page** [high]
- Element: rodent-control-perth.html trust chips: "WA licence 13914".
- Wrong/missing: This directly violates owner rule #3 ("say 'licensed technicians', never a licence number") AND the technician holds a *provisional* licence under supervision. A specific number invites verification that may not check out cleanly for a provisional holder, and it contradicts the rest of the site which says "Licensed technicians." Likely a build/template leak.
- Fix: Replace with "Licensed technicians." Grep the whole build for stray licence numbers before republishing.
- Confidence: high.

**4. Add real proof of a real business: photos of actual work, van, gear, reports** [high]
- Element: home hero + service pages (currently stock/illustrative only).
- Wrong/missing: "No photos of real jobs yet; stock/illustrative photos only." In a trust purchase, generic stock imagery *lowers* trust and is the single biggest gap vs. Flick/Rentokil/Jim's. The excellent sample treatment report is described in a table but never *shown* as an image.
- Fix: Add (a) a photo of the actual van/branding, (b) real (blurred-address) roof-void/mud-tube/station photos, (c) a screenshot image of a real (redacted) treatment report. No people needed, so anonymity is preserved. Even 6–8 authentic images beats 35 pages of stock.
- Confidence: high.

**5. Make the sample treatment report downloadable as a real PDF** [high]
- Element: Home "The DJ Pest treatment report" section.
- Wrong/missing: The differentiator of the whole business is "the paperwork nobody else gives you," but a visitor cannot actually *see or hold* one. A table on a page isn't proof.
- Fix: Add "See a sample report (PDF)" button linking a redacted example. This converts skeptics and is highly citable/shareable.
- Confidence: high.

**6. Add a lead-time / response expectation to reduce call anxiety** [medium]
- Element: hero + quote form ("Same-day for active pests").
- Wrong/missing: "Same-day for active pests" is a claim with no supporting detail; a stressed user wonders "same-day *today*, at 9pm?" Vague urgency claims can also read as puffery under the ACL if unsubstantiated.
- Fix: "Active pests (rats, wasps, fleas) — we aim to get to you same or next day. Text a photo now for a time." Keeps it honest and actionable.
- Confidence: medium.

**7. Quote form: reduce friction and set a callback-time expectation** [medium]
- Element: home quote form.
- Wrong/missing: Form requires Name + Mobile + Suburb dropdown; no expectation of *when* they'll hear back, and the dropdown omits some llms.txt suburbs (e.g. Quinns Rocks, Yanchep) — inconsistency. For a 9pm rat panic, the form is the *slow* path.
- Fix: Put "Call or text now for tonight; use the form for a next-day callback" above the form. Add "We reply within [X] business hours." Reconcile the suburb list with llms.txt (either match it or add "Other").
- Confidence: medium.

**8. Add a visible "what happens when you call" micro-reassurance** [medium]
- Element: near primary CTA.
- Fix: One line: "No call centre. You talk to the technician who'd do the job." (You already say this in About — surface it at the decision point.)
- Confidence: medium.

**9. Strengthen the pricing-page hero for the highest-intent query** [medium]
- Element: pest-control-prices-perth.html H1 "How much does pest control cost in Perth?"
- Wrong/missing: Great H1, but the answer a person (and an AI) wants — a *single headline number* — is buried in tables. "We're not the lowest price in Perth, we're thorough" is a nice differentiator but pushes price-sensitive callers away before they see the reasonable ranges.
- Fix: Add an immediate answer line: "Most northern-suburbs homes pay $250–$350 for a general pest treatment and $220–$380 for a rodent program. Full ranges below." Keep the "thorough" line but move it below the numbers.
- Confidence: medium.

**10. Suburb pages: add a genuine local "call now" anchor and internal proof** [low-medium]
- Element: Duncraig (and 7 others).
- Wrong/missing: The Duncraig geology/soil content is genuinely excellent (Spearwood sand vs Tamala limestone) but there's no local-specific CTA and no per-suburb proof. For map-pack intent these pages must convert, not just inform.
- Fix: Add "Rats or ants in Duncraig? Call 0447 747 769 — we're ~10 min away in Warwick." Keep the soil narrative; it's a competitive weapon.
- Confidence: low-medium (impact depends on traffic these pages actually get).

## 3. WHAT IS ALREADY WORLD-CLASS (do not break)

- **The problem-first headline** "Rats in the roof tonight? We fix it properly, and put it in writing." — situation + benefit + differentiator in nine words. Best I've seen in this vertical.
- **The "paperwork" positioning** (itemised quote → application ledger → treatment report → prevention plan). It is a *real*, legally-grounded differentiator that also happens to be ACL-safe and AI-quotable.
- **Technical accuracy of the pest content** — non-repellent vs repellent for coastal brown ant super-colonies, neophobia explaining day-5 untouched stations, black rat vs Norway rat behaviour, "don't break the mud tubes." This is expert-level and E-E-A-T gold.
- **Standards cited correctly and specifically**: AS 4349.3 (inspection), AS 3660.2 (management). Most competitors are vaguer.
- **Lighthouse 97/100/100/100, LCP 2.4–2.6s, CLS≈0, WebP, CSP/HSTS** — technically ahead of most national competitors' bloated sites.
- **The ACL discipline** — no "safe," "guarantee," "eco-friendly," "pet-friendly"; re-treatment framed as a *re-treat not a results guarantee*; cooling-off clause (ACL s.82) present in Terms. Genuinely compliant where most rivals over-claim.
- **The Perth pest calendar** and **What's-my-pest identifier** — both are strong AEO and engagement assets. Keep and expand.

## 4. LOCAL SEO GAPS

What competitors have that this lacks (and one-van feasibility):

| Gap | Competitors | One-van achievable? |
|---|---|---|
| **Google Business Profile** | Flick, Rentokil, Jim's, Allpest all rank via GBP with reviews & photos | **Blocked until DoH cert issues** — biggest single ranking lever, correctly deferred. The moment the certificate issues, this is priority #1. [high] |
| **Reviews / ratings** | All four have Google reviews | Not yet (none exist) — but *set up the request flow now* so day-1 reviews flow after cert. [high] |
| **Real job photos in GBP + on-page** | Jim's & Flick use franchisee/job photos | Yes, immediately. [high] |
| **Backlinks / local citations** | National brands have domain authority; Allpest is long-established WA | Achievable slowly: local directories (True Local, Yellow), Warwick/Joondalup community pages, supplier links. [medium] |
| **Suburb coverage depth** | Jim's has many franchise-suburb pages | Already strong — 8 built suburb pages with *better* local content than competitors' thin templates. [high] |
| **Named/credentialed technicians on-page** | Rentokil/Allpest show accreditation logos | Constrained by anonymity rule — substitute with association/insurance logos (see §6). [medium] |

**Verdict:** The only decisive gaps (GBP + reviews) are the two deliberately deferred. Everything else this site already matches or beats. **All competitor comparisons here are from general knowledge of these brands' Perth pages — VERIFY current competitor pages directly; I cannot browse.**

## 5. AI / ANSWER-ENGINE CITATION

You already have llms.txt, FAQPage schema, and clean H2/Q&A structure — ahead of the field. To get *cited*:

**"pest control Perth northern suburbs"**
- Add a single, liftable definitional sentence high on the services hub: "DJ Pest provides licensed pest control across Perth's northern suburbs — Warwick, Greenwood, Duncraig, Sorrento, Hillarys, Joondalup and Wanneroo — for termites, rodents, ants, cockroaches and spiders." Assistants quote self-contained sentences. [high]

**"how much does pest control cost Perth"**
- Add a lead answer paragraph on the pricing page written as a standalone fact: "In Perth's northern suburbs (2026), a general pest treatment for a 3-bedroom home typically costs $250–$350, a rodent program $220–$380, and a termite inspection $250–$350. Termite chemical management systems run $2,500–$5,500 depending on perimeter and construction." Keep OfferCatalog schema; add a `dateModified`. This is *exactly* the format AI Overviews lifts. [high]

**"what is biting me at dusk in Perth"**
- Your identifier already nails "Bitten in the yard after five" (mosquitoes) and "Bites overnight" (fleas vs bed bugs). Add an explicit H2 phrased as the question: "What's biting me at dusk in Perth?" with a two-sentence answer naming mosquitoes (container + wetland species) and, for indoor line-bites, fleas/bed bugs. Match the query wording verbatim. [high]

**Structural moves:**
- Add `speakable` schema to the FAQ answers. [medium]
- Add `areaServed` (all llms.txt suburbs) and `priceRange` to the LocalBusiness node. [high]
- Keep every FAQ answer self-contained (don't rely on preceding context) — several already do this well; audit the rest. [medium]
- Add a "Last updated" date visible on pricing and calendar pages — recency signals help both Google and AI. [medium]
- **VERIFY:** FAQPage rich-result eligibility has been curtailed by Google; the schema still aids AEO/parsing even if it no longer shows stars in SERPs. [medium]

## 6. TRUST WITHOUT A NAME (ranked, all lawful under the constraints)

1. **Real job photos + real (redacted) treatment report PDF** — proof of actual work, no name needed. [high]
2. **Van / branding / equipment photo** — proof of a real operating business. [high]
3. **Industry association membership logo** (e.g. AEPMA — Australian Environmental Pest Managers Association) *if genuinely a member* — VERIFY membership before displaying. [high]
4. **Public liability insurance statement** — already present; add insurer name/certificate on request (no figure, per constraint). [high]
5. **Standards badges**: "Inspections to AS 4349.3 · Management to AS 3660.2" as a visible trust strip. [high]
6. **ABN/ACN + registered-entity footer** — already present; good. [medium]
7. **"Pending PMB 3000" stated honestly** — transparency itself is a trust signal *if* the confusing sentence (§2.2) is fixed. [medium]
8. **The Chartered Accountant positioning** — a real, verifiable-in-principle credential and a memorable differentiator. Keep. [medium]
9. **Money-handling clarity**: "no call-out fee, no deposit, seven-day terms, quote = invoice." Financial transparency is a trust proxy. [medium]
10. **Response/communication promises**: SMS confirmations, "on the way" text, callback windows. [medium]
11. **Guarantee-adjacent, ACL-safe re-treatment promise with published conditions.** [medium]
12. **A future "reviews will appear here" honest placeholder** — optional; some find it authentic, others find it empty. [low]

## 7. CONTENT ACCURACY (WA-specific)

- **Rodent dropping size inconsistency.** Rodent page says rat droppings "8 to 12 mm"; the pest identifier says "Rat droppings are 12–18 mm." Both cannot be your standard. Roof rat (black rat) droppings are typically ~6–12 mm. Pick one range and make it consistent. [medium — VERIFY against a standard pest reference]
- **"Fifteen years in Perth pest control" vs "since 2011."** About H2 says "Fifteen years"; 2011→2026 is 15 years, so arithmetically fine — but the *entity* "DJ Pest was formed in 2026," so "fifteen years" refers to the *family's* experience, not this business. This is defensible under the approved positioning but borders on the kind of experience claim the ACL scrutinises. Ensure every "since 2011 / fifteen years" is clearly the family's, never DJ Pest Pty Ltd's. [medium]
- **European wasp reporting to DPIRD** — correct in principle for WA (European wasp is a declared/notifiable target of DPIRD surveillance). [medium — VERIFY current DPIRD reporting channel/name; agency naming changes]
- **Food Standards Code 3.2.2 applied in WA via Food Act 2008** — broadly correct. [medium — VERIFY exact adoption mechanism wording]
- **AS 4349.3:2010 and AS 3660.2:2017** — check these are the *current* editions cited on your quotes; standards get revised. [medium — VERIFY current version numbers]
- **"White-tails and huntsmen"/"black house spiders"** — service pages vary (one lists "huntsmen," another "black house spiders"). Not an error, but tidy for consistency. [low]
- **Re-treatment period inconsistency**: Home FAQ says ants/rodents "three months," fleas/wasps "30 days"; services hub table says rodent baiting 3 months, external ant 3 months, wasps 30 days — consistent. But Home FAQ groups "ants and rodents" at three months while omitting bed bugs (30 days) listed elsewhere. Reconcile all three locations to one source table. [medium]
- **"Technician name and licence number recorded"** appears in the sample report caption — fine as a *record* statement, but ensure it's never rendered as a *displayed* number on the public site (see §2.3). [high]
- **CANNOT VERIFY**: ABN 86 797 740 716, ACN 697 588 579, PMB 3000 assignment — check these against ABR / DoH records before publishing.

## 8. MISSING PAGES / FEATURES

- **Downloadable sample treatment report (PDF)** — your whole USP, currently unviewable. [high]
- **Real photo gallery / recent-jobs page** (anonymised). [high]
- **Bed bug service page** — bed bugs appear in the re-treatment table and identifier but have *no service page*; a high-intent, high-value query is unserved. [high]
- **Emergency / after-hours page or clear policy** — given the "tonight" hook. [medium]
- **Termite service pages** are referenced (llms.txt) but not in packet — ensure they carry the same depth. [n/a — not provided]
- **"How to prepare for your visit" as a standalone linkable page** (currently only on rodent page). [medium]
- **A "why we're not the cheapest" / how to compare quotes** guide — strong AEO + trust play. [medium]
- **Google/third-party review widget** (post-certificate). [high, deferred]
- **Blog depth** — only 2 posts; the pest calendar and identifier are seeds for 15–20 genuinely useful local posts (e.g. "coastal brown ants in [suburb]"). [medium]

## 9. THREE THINGS TO DELETE

1. **"WA licence 13914" on the rodent page** — breaks owner rule #3 and the provisional-licence constraint. Delete/replace immediately. [high]
2. **The confusing "carried out and recorded under a registered pest management business" sentence** (as currently worded) — delete or rewrite per §2.2; it creates r.9 "holding out" ambiguity that undermines the very compliance it's meant to demonstrate. [high]
3. **Stock/illustrative photos that depict generic pest-control scenes** — they actively lower trust in a trust purchase. Delete rather than keep placeholders until real photos exist; whitespace beats fake. [medium]

## 10. ONE-PARAGRAPH SUMMARY (act this week)

This is already, on copy and technical build, one of the best small pest-control sites in its market — the "rats in the roof tonight… put it in writing" hook, the accountant-led paperwork USP, and the genuinely expert pest content are world-class and must not be touched. Do five things this week: (1) grep the whole build and delete "WA licence 13914" and any other licence numbers, replacing with "Licensed technicians"; (2) get a WA pesticide-law solicitor to rewrite or remove the "under a registered pest management business" sentence before it becomes an r.9 problem; (3) resolve the 9pm contradiction — either add an honest after-hours/callback line beside every phone number, or soften "tonight," so nobody hits silent voicemail; (4) replace stock imagery with even a handful of real (anonymised) van, roof-void and treatment-report photos plus a downloadable sample report PDF — your single biggest trust upgrade under the no-name constraint; and (5) reconcile the rat-dropping sizes and re-treatment periods across pages, and add one liftable "typical cost" answer sentence at the top of the pricing page for the AI engines. The GBP-and-reviews gap is real but correctly deferred until the DoH certificate issues — the day it does, that becomes priority number one. *(All legal/compliance items flagged should be verified against WA DoH guidance and a solicitor; competitor and standards-version claims should be checked against primary sources as I could not browse.)*