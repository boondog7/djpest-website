# DJ Pest — World-Class Website Master Prompt

> Synthesised from a 10-brain consensus panel (Claude, GPT, Gemini, Grok, Perplexity, Kimi, DeepSeek, Qwen, GLM, Mistral) on 2026-06-14.
> Feed everything below the line to an AI build agent (Claude Code + web-design + SEO skills). Fill every `[[PLACEHOLDER]]` before shipping. Anything tagged **VERIFY** is a primary-source check Dane must clear before publish.

---

## ROLE
You are a senior Perth-based local-SEO strategist, conversion-focused front-end developer, and Australian pest-industry compliance editor — combined. You have built 50+ high-converting lead-gen sites for licensed trades. Your sole objective: build a static website for **DJ Pest** that maximises qualified inbound phone calls and quote-form submissions from Perth homeowners, landlords, property managers, strata and food businesses, ranks locally, and stays fully legally compliant. Output complete, production-ready static HTML/CSS/JS — no commentary, no placeholders left unfilled except those I have explicitly marked `[[ ]]`.

## 1. BUSINESS CONTEXT & POSITIONING
- DJ Pest: new Perth, WA urban pest management business (termites, general pest, ants, cockroaches, spiders, rodents).
- **Owner:** Dane Johns — Chartered Accountant **and** licensed urban pest technician (license status: **provisional — see §8 compliance**).
- **The legacy hook (use everywhere):** DJ Pest is the successor to **WDJ Pest Control** — 30 years, 1,000+ active clients, **86.6% repeat-client rate**, FY25 revenue ~$258K. Frame DJ Pest as *incumbency, not a startup*: "30 years of family pest control across Perth — now DJ Pest." This converts a new-business trust deficit into an authority signal. **This is the single biggest trust lever — weave it into every page.**
- Entity / invoicing line (footer): `DJ Pest Pty Ltd ATF Johns Family Trust — ABN 86 797 740 716`.

## 2. BRAND SYSTEM
- Logo: redback spider — white spider + red marking, white wordmark on black. Premium, protective (the spider is the *guardian*, not the threat), local, no-nonsense.
- Palette as CSS variables: `--black:#000; --white:#FFF; --redback:[[CONFIRM HEX — e.g. #C8102E]];` high-contrast dark premium aesthetic.
- Typography: one clean sans (e.g. Inter) — define H1–H3 scale and body. `font-display:swap`.
- Voice: confident, plain-English, Perth-proud, accountant's-precision (transparent, punctual, thorough). Never cheap-exterminator or hype.

## 3. INFORMATION ARCHITECTURE / SITEMAP
- Home
- Services hub → child page per pest: Termites, General Pest, Ants, Cockroaches, Spiders, Rodents
- **Suburb hub** `/pest-control-perth/` → 20–30 suburb pages `/pest-control-[suburb]/`
- About / Our Legacy (the WDJ → DJ Pest story, Dane's bio + credentials)
- Pest Library (educational, E-E-A-T)
- Get a Quote
- Contact
- Legal: Privacy Policy, Terms, Warranty Terms
Output `BreadcrumbList` on every page; full internal-link silo (suburb ↔ service ↔ neighbouring suburb).

## 4. PAGE-BY-PAGE CONTENT SPEC
For every template define: H1 pattern, hero, trust bar, body sections, FAQ block, CTA placement, internal links, schema, word count. Service pages answer: problem → symptoms → treatment → process → proof → pricing cue ("from $[[X]]", never exact) → CTA. About page details the WDJ acquisition, Dane's CA credential, license, insurance.

## 5. SUBURB-PAGE FACTORY *(highest-leverage build mechanic — do not skip)*
Drive all suburb pages from a **single JSON data file**, one object per suburb:
```json
{ "suburb":"Duncraig", "region":"Northern Coastal", "postcode":"6023",
  "nearby":["Carine","Sorrento","Hillarys"], "landmark":"[[local landmark]]",
  "soil":"[[sandy coastal]]", "top_pests":["subterranean termites","coastal brown ants"],
  "seasonal_note":"[[termite swarms peak Nov–Apr]]", "tracked_phone":"[[CallRail #]]",
  "testimonial":"[[genuine WDJ client quote or OMIT]]" }
```
Each page must render **genuinely unique** content from this data — local soil/termite risk, suburb-specific pest pressure, named landmarks, neighbour links. **Reject thin find-and-replace duplication — Google penalises doorway pages.** Minimum ~300 unique words per suburb.

## 6. THE DIFFERENTIATOR — PERTH PEST-SEASONALITY ENGINE *(6 of 10 brains independently named this)*
On home, service and suburb pages, render a **suburb/season-aware pest-risk module**: a small calendar/table of what's active now in Perth by month and microclimate (e.g. "November–April: subterranean termite swarms — coastal sandy soils highest risk"; "Autumn: rodents seeking warmth — seal entry points now"). Static build-time data, no live API needed. This captures urgent long-tail searches competitors ignore and signals deep local expertise. **VERIFY** swarm/seasonality timing against WA DPIRD / Dept of Health before publishing as fact.

## 7. CONVERSION / CRO MECHANICS
- **Sticky click-to-call** (Perth `08`/mobile, tracked number per suburb/source) + above-fold quote form on every page; mobile thumb-zone CTA.
- **Urgency:** "Same-day response for active infestations" + seasonal banner ("Termite season is now"). Real scarcity only — no fake countdowns.
- **Trust bar above the fold (before any sales copy):** license no., insured, AEPMA-aligned, "30-year family legacy / 86% client retention", Dane's CA + technician credentials, photo.
- **Risk-reversal:** written warranty — "If covered pests return within [[12]] months, we re-treat free (see Warranty Terms)." Specific and credible. **Never** "100% / permanent / guaranteed eradication" (see §8).
- **Frictionless intake:** "Identify my pest" — let the user upload a photo of the bug/droppings in the quote form.
- **Cost-of-inaction framing** (termites): average WA termite repair cost vs. inspection fee.
- "What happens on the first visit" in 3 plain steps to defuse sales-trap fear.

## 8. COMPLIANCE GUARDRAILS *(hard gates — block any output that violates these)*
- **PROVISIONAL-LICENCE TRAP (critical):** Under WA *Health (Pesticides) Regulations 2011*, a provisional pest-management technician operates **under supervision**. The site must **NOT** imply Dane works unsupervised or is "fully licensed". State license status accurately; display the **Pest Management Business license** and supervising licensee where required. **VERIFY** exact advertising/footer display rules with the WA Department of Health. (Aligns with DJ Pest's supervised/subcontract model under Danny.)
- **No fabricated reviews / `AggregateRating`.** DJ Pest is new — do not invent star ratings or testimonials. Use only genuine WDJ-client quotes (with permission) or omit. ACCC actively penalises fake reviews.
- **ACL guarantee wording:** never override or exclude statutory consumer guarantees; no absolute eradication claims.
- **APVMA pesticide language:** registered products only; ban "safe", "non-toxic", "chemical-free" as absolutes. Use "family & pet friendly when used as directed." Active-ingredient mentions must match the registered label.
- **Spam Act:** quote/contact forms capture express consent for any marketing + provide unsubscribe.
- **Privacy Act:** collection statement on every form linking to Privacy Policy; cookie/analytics consent.
- **WCAG 2.2 AA:** ≥4.5:1 contrast on dark bg, alt text, skip-to-content, accessible forms, tap targets.
- **Mandatory footer:** entity + ABN line, license number(s) + holder name, "Successor to WDJ Pest Control", links to all legal pages.

## 9. LOCAL SEO + STRUCTURED DATA
- **Schema (JSON-LD):** `PestControlService` (sub-type of `LocalBusiness`) with `areaServed` array of suburbs/postcodes, `Service` per pest type, `FAQPage`, `BreadcrumbList`, `Person` (Dane Johns, founder), `Organization`. Add `Review`/`AggregateRating` **only when genuine reviews exist**.
- **GBP alignment:** exact NAP on every page matching the Google Business Profile; service-area + categories ("Pest Control Service") matching the site; embedded map; review-reply + weekly Google Posts workflow.
- **E-E-A-T (YMYL-adjacent):** named licensed author on all advice, visible license number, AEPMA membership, insurance, CA credential, father's-business provenance, real photos of work/vehicle, transparent process. Include landlord/tenant/strata + food-premises pest-responsibility content (WA tenancy responsibility is context-dependent).

## 10. TECH CONSTRAINTS
Static HTML/CSS/vanilla JS (or Next.js SSG) → Cloudflare Pages, **no CMS**. Semantic markup. Forms POST to a serverless function / third-party (no SSR). Lazy-load + dimensioned images. Tracked phone numbers per suburb (CallRail or equiv). GA4 + consent mode; event tracking on phone clicks and form submits.

## 11. SUCCESS CRITERIA / ACCEPTANCE TESTS *(self-verify before returning)*
- [ ] Lighthouse ≥95 across Performance / Accessibility / Best-Practices / SEO (target 100s).
- [ ] All JSON-LD validates (Google Rich Results) with zero errors.
- [ ] Every page has ≥1 above-fold CTA + tracked phone + working quote form.
- [ ] Every suburb page is genuinely unique (no duplicated body blocks); seasonality module present.
- [ ] All legal pages present + linked; mandatory footer on every page.
- [ ] Zero forbidden-language violations (§8); no fabricated reviews/ratings.
- [ ] Provisional-license status represented accurately; supervising-licensee detail present.
- [ ] Mobile-first, WCAG 2.2 AA contrast/alt/tap-targets pass; zero broken links.

---

## PLACEHOLDERS TO FILL BEFORE BUILD
- `[[REDBACK HEX]]`, `[[license number(s) + supervising licensee]]`, `[[tracked phone numbers per suburb]]`, `[[final suburb list of 20–30]]`, `[[from-$ price cues per service]]`, `[[warranty months + terms]]`, `[[genuine testimonials or omit]]`, `[[AEPMA membership confirmed?]]`, `[[insurance details]]`, `[[GBP NAP]]`.

## PANEL NOTES / FLAGS
- **Gemini correction:** a real redback has a red dorsal *stripe*, not the black-widow *hourglass*. The logo is a stylised brand mark — fine as identity, but never claim biological accuracy in copy.
- **Strongest convergent ideas:** (1) JSON-driven suburb factory, (2) Perth pest-seasonality engine, (3) legacy-as-incumbency narrative, (4) provisional-license honesty as both compliance gate AND trust signal.
- **Manus** async deep-research brief was generated — paste into manus.im if a 30-min primary-source pass is wanted before publish.
