#!/usr/bin/env python3
"""Dedupe master keyword list, write actionable analysis report."""
import csv
from collections import defaultdict
from pathlib import Path

OUT = Path("/Users/danejohns/jaystack/djpest/seo/semrush")


def load(name):
    with open(OUT / name) as f:
        return list(csv.DictReader(f))


def dedupe_master():
    rows = load("00_MASTER_keywords.csv")
    by_kw = {}
    for r in rows:
        kw = r["keyword"].strip().lower()
        if not kw:
            continue
        # Keep the row with the most data (highest volume)
        existing = by_kw.get(kw)
        if existing is None or int(r["volume"] or 0) > int(existing["volume"] or 0):
            by_kw[kw] = r
    deduped = sorted(by_kw.values(),
                     key=lambda x: float(x["priority_score"] or 0),
                     reverse=True)
    with open(OUT / "00_MASTER_keywords.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(deduped[0].keys()))
        w.writeheader()
        w.writerows(deduped)
    print(f"Deduped: {len(rows)} → {len(deduped)} unique keywords")

    # Re-split by funnel
    for stage in ("TOFU", "MOFU", "BOFU"):
        rows = [r for r in deduped
                if r["funnel_stage"] == stage and r["rank_target"] == "yes"]
        with open(OUT / f"06_targets_{stage.lower()}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"  {stage}: {len(rows)} unique rank-target keywords")
    return deduped


def write_report(master):
    """Write a human-readable strategic report."""
    targets = [r for r in master if r["rank_target"] == "yes"]
    bofu = sorted(
        [r for r in targets if r["funnel_stage"] == "BOFU"],
        key=lambda x: float(x["priority_score"]), reverse=True
    )
    mofu = sorted(
        [r for r in targets if r["funnel_stage"] == "MOFU"],
        key=lambda x: float(x["priority_score"]), reverse=True
    )
    tofu = sorted(
        [r for r in targets if r["funnel_stage"] == "TOFU"],
        key=lambda x: float(x["priority_score"]), reverse=True
    )

    out = []
    out.append("# DJ Pest — SEMrush Deep Research Report")
    out.append(f"Generated: 2026-05-01 · Australian database · 21,090 units used\n")

    out.append("## Executive Summary\n")
    out.append("**Best money keywords (BOFU) we should target with service pages:**")
    out.append("These are commercial-intent + Perth/WA keywords with low keyword difficulty.")
    out.append("")
    out.append("| Rank | Keyword | Volume/mo | KD | CPC | Priority |")
    out.append("|---|---|---:|---:|---:|---:|")
    for r in bofu[:20]:
        out.append(f"| {r['keyword']} | {r['volume']} | {r['keyword_difficulty']} | ${r['cpc_aud']} | {r['priority_score']} |")
    out.append("")

    out.append("## TOFU Blog Priorities (informational, build topical authority)\n")
    out.append("These have huge volume and low difficulty. Each = one comprehensive blog post.")
    out.append("")
    out.append("| Keyword | Volume/mo | KD | Priority |")
    out.append("|---|---:|---:|---:|")
    for r in tofu[:25]:
        out.append(f"| {r['keyword']} | {r['volume']} | {r['keyword_difficulty']} | {r['priority_score']} |")
    out.append("")

    out.append("## MOFU Conversion Content (cost guides, comparisons)\n")
    out.append("People close to buying. Each one = one conversion-optimised long-form guide.")
    out.append("")
    out.append("| Keyword | Volume/mo | KD | CPC | Priority |")
    out.append("|---|---:|---:|---:|---:|")
    for r in mofu[:15]:
        out.append(f"| {r['keyword']} | {r['volume']} | {r['keyword_difficulty']} | ${r['cpc_aud']} | {r['priority_score']} |")
    out.append("")

    out.append("## Service-Suburb Money Keywords (specific suburbs to build pages for)\n")
    geo_bofu = [r for r in bofu if r["is_geo"] == "yes"
                and any(s in r["keyword"] for s in [
                    "joondalup", "wanneroo", "hillarys", "sorrento", "duncraig",
                    "warwick", "kingsley", "padbury", "edgewater", "marmion",
                    "currambine", "mindarie", "ocean reef", "mullaloo"
                ])]
    out.append("")
    out.append("| Suburb keyword | Volume/mo | KD | CPC |")
    out.append("|---|---:|---:|---:|")
    for r in geo_bofu[:15]:
        out.append(f"| {r['keyword']} | {r['volume']} | {r['keyword_difficulty']} | ${r['cpc_aud']} |")
    out.append("")

    out.append("## Strategic Recommendations\n")
    out.append("""
### 1. **Service page priority order** (build in this sequence)
1. **rodent control perth** — KD 26, 1300/mo. Biggest BOFU opportunity. NO existing page.
2. **ant control perth** — KD 14, 480/mo. Easy win. NO existing page.
3. **cockroach control perth** — KD 12, 390/mo. Easy. NO existing page.
4. **spider control perth** — KD 13, 320/mo. Easy. NO existing page.
5. **termite inspection perth** — KD 32, 480/mo. Harder but $6.20 CPC = high-value.
6. **pest control joondalup** — KD 15, 390/mo. Already have a page (needs SERP-steal redo).
7. **pest control hillarys** — beatable SERP, no page yet.
8. **pest control sorrento** — KD 8, 260/mo, no real competition.
9. **commercial pest control perth** — KD 30, 390/mo. B2B angle, opens new client base.

### 2. **TOFU blog priority order** (write in this sequence)
1. "How to get rid of cockroaches" — 2,900/mo, KD 12 (huge win)
2. "How to get rid of ants" — 4,400/mo, KD 18
3. "White-tail spider bite" — 8,100/mo, KD 27 (health/identification angle)
4. "What do termites look like" — 1,900/mo, KD 26
5. "Pre-construction termite barrier" — 90/mo, KD **1** (no competition, B2B/builder audience)
6. "What do white ants look like" — 1,000/mo, KD 6 (very easy)
7. "Termite cost to treat" — 720/mo, KD 11

### 3. **MOFU conversion guides**
1. "How much does pest control cost (Perth, 2026 prices)" — 1,300/mo, KD 8 — **easiest money**
2. "Pest exterminator cost Australia" — 1,000/mo, KD 9
3. "Termite chemical barrier vs bait stations" (no direct keyword data, but adjacent to high-volume "termite cost")

### 4. **Critical SERP intel**
- `pest control joondalup` #1 ranker is **joondaluppestcontrol.com.au** (exact match domain — gets 312 traffic). #2 onwards average <10 traffic each → easy to take #4-#6.
- `pest control wanneroo` #1 is bugbusters.com.au with only 7 traffic → wide open.
- `pest control warwick` is dominated by **Warwick QLD** results, not Warwick WA → pure whitespace for us. Must clarify "Warwick Perth" or "Warwick WA" in our content + targeting.
- `pest control hillarys` top 5 combined traffic: 11. Anyone with a decent page can rank.
- For `termite treatment perth`, Reddit ranks #3 → opportunity to write a deeper, better cost guide.

### 5. **Competitor gap — Jim's Pest Control structure**
Jim's ranks for `pest control [suburb]` pages all over Australia (Burwood KD 8, Hornsby KD 14, North Manly KD 5, Flagstaff Hill KD 7). They DON'T have Perth-specific suburb pages — that's our gap to exploit. Suburb pages with KD <15 are extremely rankable.

### 6. **The "low CPC = informational" trap**
Some high-volume keywords have low CPC because they're informational (no one bids on them). These are still valuable for **topical authority** even if they don't directly convert. Examples: `white tail spider bite` ($0.03 CPC) — high traffic, low conversion, but Google trusts you on spider topics → lifts your `spider control perth` ranking.

### 7. **Watch out for**
- `flick.com.au` and `rentokil.com` rank in TOP 5 of every Perth keyword — they're spending real SEO budget. Don't try to displace them on `pest control perth` (KD 50). Take suburbs they ignore.
- `joondaluppestcontrol.com.au` owns the EMD — we can't displace #1 there without 12+ months of authority. Aim for #4-#6.
""")

    out.append("## Files in this folder\n")
    out.append("```")
    out.append("00_MASTER_keywords.csv      — every keyword ranked by priority")
    out.append("01_keyword_metrics.csv      — raw phrase_this output (volume/CPC/KD)")
    out.append("02_related_keywords.csv     — expansion from each root term")
    out.append("03_question_keywords.csv    — TOFU blog topic mining")
    out.append("04_serp_top10.csv           — actual ranking URLs for our priority keywords")
    out.append("05_competitor_keywords.csv  — what Jim's Pest Control ranks for")
    out.append("06_targets_bofu.csv         — service page candidates")
    out.append("06_targets_mofu.csv         — comparison/cost guide candidates")
    out.append("06_targets_tofu.csv         — blog post candidates")
    out.append("07_competing_domains.csv    — who appears in Perth pest SERPs")
    out.append("REPORT.md                   — this file (strategic summary)")
    out.append("all_responses.json          — raw JSON dump (for re-processing without re-querying)")
    out.append("```")

    Path(OUT / "REPORT.md").write_text("\n".join(out))
    print(f"  → REPORT.md ({len(out)} lines)")


if __name__ == "__main__":
    master = dedupe_master()
    write_report(master)
