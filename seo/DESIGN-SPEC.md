# DJ Pest — World-Class Design Spec
> Source: 10-brain design committee (7 responded: Claude, GPT, Gemini, Grok, DeepSeek, Mistral, Perplexity). Run 2026-05-31.
> Governing principle (unanimous): **Anxious mobile users + "world-class" are NOT in conflict — both demand fast, calm, legible, frictionless.** Don't out-animate the competition; out-CALM and out-TRUST them. Every competitor is loud, cluttered, faceless. Win by being the quiet, premium, obviously-trustworthy professional. "Looks like Apple designed a pest control company."

## NON-NEGOTIABLES (unanimous)
- **NO video background.** Kills LCP, drains mobile battery, adds anxiety. Use one optimised hero image (WebP/AVIF, `fetchpriority="high"`, sized) + real headline text in HTML.
- **NO parallax.** Jank + motion sickness + zero conversion.
- **`prefers-reduced-motion: reduce` wrapper on ALL motion** — accessibility + right for anxious audience.
- **Content visible if JS never loads** — phone number + headline are pure HTML/CSS. Never hide content behind JS.
- **Sticky mobile call button** (tracked `tel:`) = the single most important conversion element. Always visible.

## HERO
- Dark brand canvas (black), high-contrast white headline as real text, one red accent.
- Headline speaks to the panic + the promise: e.g. *"Rats in your roof tonight? We fix it properly — first time."* Sub: *"Chartered Accountant owner. No hidden fees. Same-day response across Perth's northern suburbs."*
- Primary CTA: Call Now (tel). Secondary: Get a fixed-price quote.
- Trust strip under hero: licensed • insured • ABN • CA-owned • Warwick-based.
- **Redback SVG animation: draw the web ONCE on load** (~600–900ms via CSS `stroke-dashoffset`), then settle and stop. Inline SVG <3KB. Do NOT loop — a constantly moving spider on an anxiety site is hostile. (Minor split: Gemini/DeepSeek allow an ultra-slow hourglass glow; if used, must die under reduced-motion.)
- **Scroll reveals:** light only — IntersectionObserver, opacity + 8–20px translateY, ~200–400ms, max ~6 per page, content visible by default.
- **Number count-ups: ONLY if the number is real.** ⚠️ A brand-new business claiming "1000+ homes protected" is false + risks ACL misleading-conduct. Defensible framing: *"Second-generation — built on the 1,000+ Perth homes WDJ has protected since 2008"* (lean on Danny's heritage), or skip the count entirely.

## IMAGERY (identical ranking across all 7 brains)
1. **Dane's real face / team / branded truck** — highest E-E-A-T; a real local human destroys faceless competitors.
2. **Real before/after job photos** (termite damage, sealed roof voids) — proof of work; curate (gnarly close-ups on service/blog pages, NOT hero).
3. **Local Perth suburb / landmark shots** (truck in a recognisable northern-corridor street).
4. **Custom illustration / iconography** (matches the monochrome+red brand; softens an anxiety category — the "Frank" insurance model).
5. **Stock photography** — avoid (generic "man in white suit spraying" = screams cheap competitor).
6. **AI-generated imagery** — BANNED for people/jobs/proof/before-after (toxic for E-E-A-T, users spot it). OK only for abstract/decorative textures or pest-identifier illustrations with a disclaimer.

**Dane's shot list:** clean headshot + on-site candid; truck front + 3/4 with logo legible; hands-on-equipment detail (moisture meter on timber = "meticulous"); before/after pairs (same angle, dated, client consent); "left the home clean/tidy" shot; process/step shots; one genuine northern-corridor streetscape. Consistent cool/high-contrast grade. Serve as `<picture>` AVIF+WebP, strictly sized, lazy-load below fold.

## TRUST & CONVERSION UX
- Sticky call bar (mobile) + click-to-call everywhere (header, hero, footer).
- **WhatsApp / SMS link** (`wa.me`, lightweight) — anxious users who won't phone will text. NOT a heavy live-chat widget (JS bloat, feels cheap).
- **Short quote form AFTER trust content**, not in hero (name, phone, suburb, pest). Phone always the primary CTA over the form.
- **Real Google reviews baked as static HTML** with reviewer name + suburb ("Jane, Duncraig") + AggregateRating schema. NOT a heavy Elfsight/iframe widget (kills CWV). Curate 3–5, rest on a reviews page, refresh monthly.
- **"Redback Guarantee" badge:** *"Fixed price quoted before we start. No hidden fees. 12-month guarantee — if pests return, we come back free."* (Verify actual terms.) #1 premium-not-cheap signal.
- **Locality signal:** "Based in Warwick — fast response across Perth's northern suburbs."
- **Before/after slider:** CSS-only image-compare (no heavy lib), lazy-loaded, not the LCP element.
- **REPEL price-shoppers / attract loyal fair-price clients:** NO "from $99", no countdown timers, no "CHEAPEST IN PERTH". Say *"We're not the cheapest — we're thorough, and we stand behind it."* Button copy *"Get a Fair Price"* not *"Free Quote."*

## THE CA ANGLE (Dane's unfair advantage — lean in hard)
- Positioning line: **"The Accountant's Pest Control."** / *"Most pest companies are run by exterminators. This one's run by a Chartered Accountant who hates hidden fees more than termites."*
- Language: audit, diagnostics, compliance, documented, itemised, transparent, traceable.
- **Product feature, not just copy:** an itemised written quote + post-job report after every job (CA-grade paper trail).
- Design cues that signal honesty/premium: disciplined CSS-variable spacing system, thin 1px "ledger-line" dividers, pricing shown in clean invoice/ledger-style tables, restrained serious typography, confident whitespace, a real "from Dane" signature/note.
- ⚠️ Verify CA ANZ rules on displaying the "Chartered Accountant" designation in marketing before publishing.

## HIGHEST-ROI "WORLD-CLASS" MOVES (cheap on static HTML)
1. **Typography + whitespace** — biggest perceived-quality lift for near-zero cost. One self-hosted variable font (woff2, `font-display: swap`) — this ALSO fixes the current Google-Fonts render-block hurting Performance. Fluid type via `clamp()`. Modular type + spacing scale.
2. **Design system** — CSS custom properties for colour/spacing/radius/shadow; consistent components across all pages = looks like a real brand.
3. **Micro-interactions (pure CSS)** — button press (scale .97), card hover (translateY -2px + soft red shadow), focus rings. Zero requests, high polish.
4. **Commit to dark mode** (brand is already black/white/red — "surgical, nocturnal, lethal to pests" in an industry drowning in green/yellow).
- SKIP: personalisation, scroll-storytelling, heavy motion libs (GSAP/Three.js/Lottie), interactive maps.

## INTERACTIVE TOOLS — decisions
- **"Which pest is it?" identifier: BUILD IT** (near-unanimous). Lightweight static decision-tree / image-card grid → links to the matching service page. Matches anxious intent, drives dwell time, AI-citable, generates internal pages. Vanilla JS <10KB.
- **Public cost calculator: DON'T** (resolved against Dane's north star). 4 of 7 warn it attracts the price-shoppers Dane explicitly doesn't want. Replace with a **transparent pricing table/guide** (plain HTML text so AI search can cite it — per Gemini's correction that AI doesn't execute JS tools) + a **guided "get a fixed honest quote" form**. Keeps the CA "no surprises" promise without turning the site into a price-comparison commodity. (DeepSeek/Mistral dissent: a calculator drives leads — revisit only if lead volume is ever the bottleneck.)

## THE ONE SIGNATURE MOVE (synthesis of the committee's best ideas)
**Build "The DJ Pest Diagnostic Report" showcase** (Gemini's standout idea) inside the calm black/red "Accountant's Pest Control" identity, with the redback as an elegant recurring motif (section dividers = web threads, custom bullets, a still watermark).

Show a beautifully designed mockup of the actual report the client receives after every job — toggle between 3 static images: (1) Point-of-Entry Audit, (2) Chemical Application Ledger (exactly what was used, where, why), (3) Future Prevention Plan. No other pest controller does this. It visually PROVES the CA-level meticulousness, justifies a premium price, proves nothing's hidden, and is pure static HTML + WebP — perfect for the loyal, fair-price clients Dane wants.

## VERIFY BEFORE PUBLISH
"1000+ homes" / any stat (ACL honesty — use WDJ heritage framing); guarantee terms; CA ANZ designation-usage rules; real review count/rating before displaying; WA pest licence held before expertise claims.
