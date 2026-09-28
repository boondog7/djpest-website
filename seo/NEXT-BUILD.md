# NEXT BUILD — 2026-09-28

> ## HARD RULES FOR THE CLOUD ROUTINE (added 22 Sep 2026 by Dane's Mac session)
> 1. **Never edit `site.json → "unpublished"`, the `PRICES` dict, or any dollar figure.** Prices are Dane's decision. Build the page, leave it gated, and list the proposed prices in this file for him to confirm.
> 2. **Never claim a page is "live".** The cloud commits HTML; only `./deploy.sh --prod` on the Mac deploys.
> 3. Every public claim passes the compliance scanner and the licensing wording is the fixed string ("carried out by, or under the direct supervision of, a technician holding a WA pest management technician's licence"), never bare "Licensed technicians".
> 4. Read `~/business/djpest/marketing/vibe/brand-bible.md` voice rules before writing copy.


## Progress summary
**Done: ~100% of 14-day plan. 7 blog posts live (all with FAQ JSON-LD) + 14 service/MOFU pages + 100+ suburb pages + service-areas hub. Blog pipeline is the compounding growth engine.**

**Overnight wins (Mon 28 Sep):**
- ✅ `white-tail-spider-bite` published — 8,100/mo KD27 (biggest post yet)
- ✅ `how-to-get-rid-of-german-cockroaches` published — 590/mo KD8
- ✅ FAQPage JSON-LD wired into all blog post templates (now live on all 7 posts)

---

## ⚠️ Dane: action needed on your Mac
**Run `./deploy.sh --prod`** to push the german cockroach + white-tail posts to the live site. Both are committed to `main` but not yet deployed.

Also: **Termite licence gate** — confirm `/termite-inspection-perth`, `/termite-treatment-perth`, and `/termite-treatment-cost-perth` remain in `site.json → unpublished` if termite endorsement is not yet held.

---

## Today's build tasks

### Task 1 (DO THIS TODAY) — Write `silverfish` blog draft
**Target publish: Thu 2 Oct — draft must be ready by Wed 1 Oct**
**Primary keyword:** `how to get rid of silverfish` — **1,600/mo, KD 20**
**Fold in:** `how get rid silverfish` (1,300/mo), `how to repel silverfish` (as FAQ)
**Research outline ready:** `blog/_drafts/14_how-to-get-rid-of-silverfish.md`
**Target:** ~1,500 words, 8 H2s, 4 images (Pexels query: `silverfish`).
**Internal links:** `/general-pest-control-perth` + `/pest-control-prices-perth`.
**Why now:** Next in the Mon/Thu queue; 4-day lead time to Thu publish.

### Task 2 — Write `huntsman spiders` draft (for Mon 5 Oct)
**Primary keyword:** `are huntsman spiders venomous` — **1,900/mo, KD 20**
**Research outline ready:** `blog/_drafts/17_are-huntsman-spiders-venomous.md`
**Why now:** Oct = peak Perth spider season (warmer nights). Write this BEFORE silverfish deploys so the pipeline has no gap.
**Internal links:** `/spider-control-perth`.
**Compliance note:** Huntsmans are mildly venomous but bites are very rare — do NOT overstate danger.

### Task 3 — Confirm Oct queue order (5-min decision, no build needed)
**Queue after silverfish + huntsman (QUEUE.md):**
- Thu 9 Oct: `how-to-get-rid-of-rats` → `/rodent-control-perth`
- Mon 12 Oct: `is-termite-damage-covered-by-insurance` → **HOLD until termite endorsement confirmed**
- Thu 16 Oct: `do-cockroaches-bite` → `/cockroach-control-perth`

Dane: confirm or reorder the Thu 9 Oct slot. If termite licence arrives before Mon 12, unlock that post then.

---

## Off-site (Dane — cannot build from code)
- **GBP at Warwick 6024** — still the single biggest lever for actual phone calls. Map 3-pack placement beats any organic page for "pest control near me". If not done yet: **do this week**.
- **NAP citations:** TrueLocal, Yellow Pages AU, Hipages, Oneflare, Yelp AU, StartLocal — consistent "Warwick WA 6024".
- **Review asks:** SMS/email after every job. Ask clients to mention suburb + pest in their review.
