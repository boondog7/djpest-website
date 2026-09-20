# djpest.com.au — 10-brain panel review, 20 Sep 2026 (synthesis)
Panel: Claude, GPT, Gemini, Grok, Perplexity, Kimi, DeepSeek, Qwen, GLM (healed at 60k tokens), Mistral. 10/10 answered. Transcripts in this folder; question in QUESTION.md (9.5k-word packet of the built site + constraints). Competitor benchmark and Lighthouse run the same day. Manus async result not awaited.

## Verdict tally
- 9/10: the home headline "Rats in the roof tonight? We fix it properly, and put it in writing." is best-in-class — keep.
- 8/10: the documentation positioning (itemised quote → application ledger → treatment report → prevention plan) is the real differentiator and is ACL-safe — keep, make it visible.
- 10/10: technical/performance/security is elite (Lighthouse 97/100/100/100 vs Flick 27, Jim's 28, Allpest 51 on mobile).
- 7/10: hero buried locality + speed under the accountant line — FIXED 20 Sep.
- 6/10: "tonight" hook contradicted by Mon–Sat 7–6 hours with no after-hours cue — FIXED (hours cue under every hero).
- 5/10: "WA licence 13914" leaking on ten pages — FIXED (0 pages).
- 4/10 (Gemini, Grok, Mistral, GPT-partial): dark theme reads "law firm / tactical", brighter would convert better. 4/10 (Claude, Qwen, Perplexity, Kimi) explicitly did not ask for a reversal. **Split — Dane's call.**
- 3/10: the pending-registration sentence was opaque about whose registration — FIXED (reworded; business not named per brand rule).
- 2/10: "licensed technicians" is a defined term for FULL licence holders (Regs r.3) — FIXED ("carried out by, or under the direct supervision of, a technician holding a WA PMT licence").
- 2/10: phantom "Bed bugs 30 days" re-treatment row with no service page — FIXED (removed).
- 1/10 (GLM): rodent dropping size contradiction 8–12 vs 12–18 mm — FIXED (10–20 mm by species).

## Rejected / not adopted
- Gemini's "purge licence number invites regulatory scrutiny" — the number was an owner-rule breach, not unlawful; fixed on the owner rule.
- Qwen's r.13 citation for supervision — supervision is r.35(2); r.13 is sales. Wording fixed on the r.3 definition instead.
- Mistral's answers were generic ("site has a blog post that is outdated") — weighted zero.
- Adding Review/AggregateRating schema now — no reviews exist; would be fabrication.

## Backlog, ranked by expected calls (panel-weighted)
1. **Google Business Profile + first 10 reviews** — every brain; gated on the PMB certificate. Plan: marketing/gbp-and-directories.md.
2. **Downloadable sample treatment report PDF** (Claude, Gemini, GPT, Perplexity) — the USP is currently unviewable. Redacted real report once one exists; until then the on-page sample.
3. **"Choose your pest" symptom strip under the hero** (GPT, Kimi, GLM) — 6 cards: rats in roof / termites / ants / cockroaches / spiders / wasps & bees, with typical price. Cuts the 14-screen mobile scroll.
4. **Price anchor strip under hero** (GLM, Claude, Grok) — "Typical: rodents $220–$380 · general $250–$350 · termite inspection $250–$350 · full list".
5. **Real job photos, anonymised** (Claude, DeepSeek, Perplexity) — replace stock; nothing AI-generated as evidence.
6. **Suburb pages for the 22 named-but-unbuilt suburbs** (GPT, Grok) — Kingsley, Woodvale, Padbury, Craigie, Kallaroo, Mullaloo, Ocean Reef, Currambine, Kinross, Marangaroo, Girrawheen, Carine, Karrinyup, Hamersley, Balga, Alkimos, Clarkson, Butler, Mindarie, Quinns Rocks, Yanchep, Stirling — one per day via the generator.
7. **Emergency / after-hours advice page** (Perplexity, Claude, GLM) — what to do at 9pm, what to photograph, morning slots.
8. **Pre-purchase timber pest inspection page** (Gemini) and **bed bug page** (Claude, GPT) — or keep bed bugs out entirely.
9. **FAQ answers as one-line answer + link** (Perplexity, Grok) and **llms.txt Q&A block** with the exact voice queries (Grok, Kimi).
10. **Suburb dropdown → autocomplete** (Gemini) and reconcile the form's suburb list with llms.txt (Claude).
11. Titles >60 chars on 10 pages; metas >160 on ~12 pages — trim.
12. `areaServed` postcodes in LocalBusiness schema (Qwen) — cheap, do with #6.

## Decisions for Dane
- Dark theme: keep (distinctive, panel split) or brighten hero only. Recommend: keep the brand, test a white "emergency card" hero variant on one suburb page first.
- Confirm bee ($250–400) and commercial ($140–380 / clean-out $350–650) prices → un-gate those two pages.
- Beekeeper swarm-collector number before the bee page goes live.
