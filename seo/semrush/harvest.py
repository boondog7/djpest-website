#!/usr/bin/env python3
"""
SEMrush comprehensive harvester for DJ Pest.
Pulls everything we'd ever want from the Australian database, saves it locally
forever so we never need a paid SEMrush subscription. Built to maximise the
14-day trial budget (~50,000 units).

Phases:
  1. phrase_this — volume, CPC, KD, intent for every keyword in our universe
  2. phrase_related — keyword expansion from each root
  3. phrase_questions — TOFU blog candidates ("how X", "what Y", etc.)
  4. phrase_organic — top 10 SERP results for BOFU keywords (competitor URLs)
  5. domain_organic — what Australian pest competitors actually rank for

Outputs CSVs to the same folder, plus a master analysis report.
"""
import csv
import json
import os
import sys
import time
from pathlib import Path

import urllib.request
import urllib.parse

# ---------------------------------------------------------------------------
KEY = os.environ.get("SEMRUSH_API_KEY")
if not KEY:
    sys.exit("SEMRUSH_API_KEY not in env")

DB = "au"
BASE = "https://api.semrush.com/"
OUT = Path("/Users/danejohns/jaystack/djpest/seo/semrush")
OUT.mkdir(parents=True, exist_ok=True)
RAW = OUT / "raw"
RAW.mkdir(exist_ok=True)

# Standard column shorthands per SEMrush docs
COLS = {
    "phrase": "Ph,Nq,Cp,Co,Nr,Td,In,Kd",          # keyword overview
    "related": "Ph,Nq,Cp,Co,Nr,Td,In,Kd",         # related keyword
    "organic": "Po,Pp,Pd,Ur,Tt,Ds,Tg",            # SERP position, URL, title, desc
    "domain":  "Ph,Po,Nq,Cp,Co,Tr,Tc,Ur,Td,In,Kd", # ranked keywords for a domain
}

UNITS_USED = 0


def units_balance():
    url = f"https://www.semrush.com/users/countapiunits.html?key={KEY}"
    return int(urllib.request.urlopen(url, timeout=30).read().decode().strip())


def call(params):
    """Hit SEMrush API. Returns raw text. Tracks unit usage roughly."""
    global UNITS_USED
    params = {**params, "key": KEY, "database": DB}
    qs = urllib.parse.urlencode(params)
    url = f"{BASE}?{qs}"
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            text = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return f"ERROR :: request failed: {e}"
    return text


def parse_csv(text):
    """Parse SEMrush ;-delimited CSV response."""
    if not text or text.startswith("ERROR"):
        return []
    lines = [ln for ln in text.strip().split("\n") if ln]
    if not lines:
        return []
    reader = csv.DictReader(lines, delimiter=";")
    return list(reader)


def save_raw(name, text):
    (RAW / f"{name}.txt").write_text(text)


def save_csv(rows, path, fieldnames=None):
    if not rows:
        Path(path).write_text("(no data)")
        return
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


# ---------------------------------------------------------------------------
# Keyword universe — roots × suburbs × services
# ---------------------------------------------------------------------------

PERTH_NORTHERN_SUBURBS = [
    "warwick", "joondalup", "duncraig", "wanneroo", "hillarys", "kingsley",
    "woodvale", "padbury", "sorrento", "marmion", "north beach", "scarborough",
    "trigg", "mullaloo", "ocean reef", "currambine", "kinross", "iluka",
    "burns beach", "mindarie", "quinns rocks", "clarkson", "butler",
    "alkimos", "yanchep", "greenwood", "craigie", "beldon", "edgewater",
    "heathridge", "connolly", "kallaroo", "carine", "hamersley", "balcatta",
    "girrawheen", "marangaroo", "westminster", "tuart hill", "mirrabooka",
    "stirling", "innaloo", "doubleview", "karrinyup", "watermans bay",
    "north fremantle", "fremantle",  # broader Perth metro
]

ROOT_TERMS = [
    "pest control",
    "termite inspection",
    "termite treatment",
    "termite control",
    "ant control",
    "cockroach control",
    "spider control",
    "rodent control",
    "rat control",
    "mouse control",
    "mosquito control",
    "bee removal",
    "wasp removal",
    "flea treatment",
    "bed bug treatment",
    "silverfish treatment",
    "millipede control",
    "redback spider control",
    "white-tail spider treatment",
    "coastal brown ant",
]

# Adjacent-topic / TOFU seeds — informational intent
INFO_SEEDS = [
    "are termites dangerous",
    "signs of termites in house",
    "what does termite damage look like",
    "are redbacks dangerous",
    "white tail spider bite",
    "how to get rid of cockroaches",
    "how to get rid of ants in kitchen",
    "are coastal brown ants dangerous",
    "how often should you spray for pests",
    "how much does pest control cost",
    "how much does termite treatment cost",
    "best termite treatment australia",
    "diy termite treatment",
    "termite vs ant",
    "termite chemical barrier vs bait",
    "pre-construction termite barrier",
    "as 3660.2",
    "as 4349.3",
    "pest management technician licence wa",
    "how long does pest control last",
]


def build_keyword_universe():
    """Return list[str] of every keyword we want metrics on."""
    kws = set()
    # Root terms alone
    for r in ROOT_TERMS:
        kws.add(r)
        kws.add(f"{r} perth")
        kws.add(f"{r} wa")
        kws.add(f"{r} near me")
    # Service × suburb (BOFU money keywords)
    for r in ["pest control", "termite inspection", "termite treatment",
              "termite control", "ant control", "cockroach control",
              "spider control", "rat control"]:
        for s in PERTH_NORTHERN_SUBURBS:
            kws.add(f"{r} {s}")
    # Suburb-only "pest control X" variants
    for s in PERTH_NORTHERN_SUBURBS:
        kws.add(f"pest control {s}")
        kws.add(f"pest control {s} perth")
    # Informational
    for q in INFO_SEEDS:
        kws.add(q)
    return sorted(kws)


# Australian pest control competitors to mine for ranking keywords
COMPETITORS = [
    "rentokil.com.au",
    "jimspestcontrol.com.au",
    "vipperthpestcontrol.com.au",
    "amalgamatedpestcontrol.com.au",
    "wapestcontrol.com.au",
]

# Top BOFU keywords to pull SERP organic results for (compete-set)
SERP_PULL = [
    "pest control perth",
    "pest control joondalup",
    "termite inspection perth",
    "termite treatment perth",
    "termite control perth",
    "pest control duncraig",
    "pest control wanneroo",
    "pest control warwick",
    "pest control hillarys",
    "pest control kingsley",
    "pest control woodvale",
    "ant control perth",
    "cockroach control perth",
    "rodent control perth",
    "spider control perth",
    "bee removal perth",
    "wasp removal perth",
    "coastal brown ant perth",
    "termite inspection joondalup",
    "termite treatment joondalup",
]


# ---------------------------------------------------------------------------
# Phases
# ---------------------------------------------------------------------------

def phase1_keyword_metrics(keywords):
    """phrase_this on every keyword. ~10 units per call."""
    print(f"[Phase 1] phrase_this on {len(keywords)} keywords (~{len(keywords) * 10:,} units)")
    results = []
    for i, kw in enumerate(keywords, 1):
        text = call({
            "type": "phrase_this",
            "phrase": kw,
            "export_columns": COLS["phrase"],
        })
        save_raw(f"phrase_this_{i:04d}", text)
        rows = parse_csv(text)
        for r in rows:
            r["_query"] = kw
        results.extend(rows)
        if i % 25 == 0:
            print(f"  {i}/{len(keywords)} done")
        time.sleep(0.05)
    save_csv(results, OUT / "01_keyword_metrics.csv")
    print(f"  → 01_keyword_metrics.csv ({len(results)} rows)")
    return results


def phase2_related(roots, n_per_root=30):
    """phrase_related on each root. ~40 units per row."""
    print(f"[Phase 2] phrase_related on {len(roots)} roots × {n_per_root} rows")
    all_rows = []
    for i, root in enumerate(roots, 1):
        text = call({
            "type": "phrase_related",
            "phrase": root,
            "export_columns": COLS["related"],
            "display_limit": str(n_per_root),
            "display_sort": "nq_desc",  # by volume
        })
        save_raw(f"phrase_related_{i:02d}", text)
        rows = parse_csv(text)
        for r in rows:
            r["_root"] = root
        all_rows.extend(rows)
        print(f"  {root}: {len(rows)} rows")
        time.sleep(0.1)
    save_csv(all_rows, OUT / "02_related_keywords.csv")
    print(f"  → 02_related_keywords.csv ({len(all_rows)} rows)")
    return all_rows


def phase3_questions(roots, n_per_root=30):
    """phrase_questions on each root. ~40 units per row."""
    print(f"[Phase 3] phrase_questions on {len(roots)} roots × {n_per_root} rows")
    all_rows = []
    for i, root in enumerate(roots, 1):
        text = call({
            "type": "phrase_questions",
            "phrase": root,
            "export_columns": COLS["related"],
            "display_limit": str(n_per_root),
            "display_sort": "nq_desc",
        })
        save_raw(f"phrase_questions_{i:02d}", text)
        rows = parse_csv(text)
        for r in rows:
            r["_root"] = root
        all_rows.extend(rows)
        print(f"  {root}: {len(rows)} rows")
        time.sleep(0.1)
    save_csv(all_rows, OUT / "03_question_keywords.csv")
    print(f"  → 03_question_keywords.csv ({len(all_rows)} rows)")
    return all_rows


def phase4_serp_organic(keywords):
    """phrase_organic on each BOFU keyword. ~10 units per row × 10 rows."""
    print(f"[Phase 4] phrase_organic on {len(keywords)} keywords × 10 rows")
    all_rows = []
    for i, kw in enumerate(keywords, 1):
        text = call({
            "type": "phrase_organic",
            "phrase": kw,
            "export_columns": COLS["organic"],
            "display_limit": "10",
        })
        save_raw(f"phrase_organic_{i:02d}", text)
        rows = parse_csv(text)
        for r in rows:
            r["_keyword"] = kw
        all_rows.extend(rows)
        print(f"  {kw}: {len(rows)} top-ranking URLs")
        time.sleep(0.1)
    save_csv(all_rows, OUT / "04_serp_top10.csv")
    print(f"  → 04_serp_top10.csv ({len(all_rows)} rows)")
    return all_rows


def phase5_competitor_keywords(domains, n_per_domain=80):
    """domain_organic for each competitor. ~50 units per row."""
    print(f"[Phase 5] domain_organic on {len(domains)} competitors × {n_per_domain} rows")
    all_rows = []
    for i, d in enumerate(domains, 1):
        text = call({
            "type": "domain_organic",
            "domain": d,
            "export_columns": COLS["domain"],
            "display_limit": str(n_per_domain),
            "display_sort": "tr_desc",  # by traffic
        })
        save_raw(f"domain_organic_{i:02d}_{d.replace('.', '_')}", text)
        rows = parse_csv(text)
        for r in rows:
            r["_competitor"] = d
        all_rows.extend(rows)
        print(f"  {d}: {len(rows)} ranked keywords")
        time.sleep(0.2)
    save_csv(all_rows, OUT / "05_competitor_keywords.csv")
    print(f"  → 05_competitor_keywords.csv ({len(all_rows)} rows)")
    return all_rows


# ---------------------------------------------------------------------------
# Aggregation / analysis
# ---------------------------------------------------------------------------

def to_int(v, default=0):
    try:
        return int(float(v or 0))
    except Exception:
        return default


def to_float(v, default=0.0):
    try:
        return float(v or 0)
    except Exception:
        return default


def aggregate_master(metrics):
    """Build the master keyword CSV with priority scoring."""
    print("[Aggregate] building master keyword list with funnel classification")
    out = []
    for r in metrics:
        kw = (r.get("Keyword") or r.get("_query") or "").lower().strip()
        if not kw:
            continue
        vol = to_int(r.get("Search Volume"))
        kd = to_int(r.get("Keyword Difficulty Index"))
        cpc = to_float(r.get("CPC"))
        comp = to_float(r.get("Competition"))
        intent_raw = r.get("Intent", "0")

        # Classify funnel stage
        kw_low = kw.lower()
        is_question = any(w in kw_low for w in [
            "how", "what", "why", "when", "are ", "is ", "do ", "does ",
            "best ", "diy", "vs", "cost"
        ])
        is_geo = any(s in kw_low for s in PERTH_NORTHERN_SUBURBS) or "perth" in kw_low or "wa" in kw_low.split()
        has_service = any(t in kw_low for t in [
            "control", "treatment", "inspection", "removal", "exterminator"
        ])

        if is_question and not has_service:
            stage = "TOFU"
        elif "cost" in kw_low or "vs " in kw_low or "best " in kw_low:
            stage = "MOFU"
        elif is_geo and has_service:
            stage = "BOFU"
        elif has_service:
            stage = "MOFU"
        else:
            stage = "TOFU"

        # Priority score (higher = better target):
        # reward volume, penalize KD, reward CPC (=> commercial value)
        priority = 0
        if vol > 0 and kd > 0:
            priority = (vol * (1 + cpc)) / (kd + 10)

        out.append({
            "keyword": kw,
            "volume": vol,
            "keyword_difficulty": kd,
            "cpc_aud": cpc,
            "competition": comp,
            "intent_code": intent_raw,
            "funnel_stage": stage,
            "is_geo": "yes" if is_geo else "no",
            "priority_score": round(priority, 1),
            "rank_target": "yes" if (vol >= 50 and kd <= 35) else "no",
        })
    out.sort(key=lambda x: x["priority_score"], reverse=True)
    save_csv(out, OUT / "00_MASTER_keywords.csv",
             fieldnames=["keyword", "volume", "keyword_difficulty", "cpc_aud",
                         "competition", "intent_code", "funnel_stage", "is_geo",
                         "priority_score", "rank_target"])
    print(f"  → 00_MASTER_keywords.csv ({len(out)} rows)")
    return out


def split_by_funnel(master):
    """Split master into TOFU/MOFU/BOFU candidate CSVs (rank_target=yes only)."""
    targets = [r for r in master if r["rank_target"] == "yes"]
    for stage in ("TOFU", "MOFU", "BOFU"):
        rows = [r for r in targets if r["funnel_stage"] == stage]
        rows.sort(key=lambda x: x["priority_score"], reverse=True)
        save_csv(rows, OUT / f"06_targets_{stage.lower()}.csv")
        print(f"  → 06_targets_{stage.lower()}.csv ({len(rows)} rows)")


def competitor_url_map(serp):
    """From phrase_organic, build a map: domain → list of (keyword, url, position)."""
    by_domain = {}
    for r in serp:
        url = r.get("Url") or r.get("URL") or ""
        if not url:
            continue
        # Extract domain
        m = url.replace("https://", "").replace("http://", "").split("/")[0]
        m = m.removeprefix("www.")
        rec = by_domain.setdefault(m, [])
        rec.append({
            "keyword": r.get("_keyword", ""),
            "position": r.get("Position", ""),
            "url": url,
            "title": r.get("Title", ""),
        })
    # Save sorted by who appears most
    summary = sorted(
        ({"domain": d, "rankings": len(rs), "keywords": ";".join(set(x["keyword"] for x in rs))}
         for d, rs in by_domain.items()),
        key=lambda x: x["rankings"], reverse=True
    )
    save_csv(summary, OUT / "07_competing_domains.csv",
             fieldnames=["domain", "rankings", "keywords"])
    print(f"  → 07_competing_domains.csv ({len(summary)} domains found in BOFU SERPs)")
    return by_domain


def main():
    start_balance = units_balance()
    print(f"Starting unit balance: {start_balance:,}")
    print()

    keywords = build_keyword_universe()
    print(f"Keyword universe: {len(keywords)} terms")
    print()

    # Phase 1 — every keyword's metrics
    metrics = phase1_keyword_metrics(keywords)

    # Phase 2 — related keyword expansion (top roots only)
    top_roots = ["pest control perth", "termite perth",
                 "termite treatment perth", "termite inspection perth",
                 "ant control perth", "cockroach perth",
                 "rat control perth", "spider control perth"]
    related = phase2_related(top_roots, n_per_root=30)

    # Phase 3 — question keywords (TOFU mining)
    q_seeds = ["pest control", "termite", "cockroach", "ant", "rat",
               "spider", "redback", "white tail spider", "coastal brown ant"]
    questions = phase3_questions(q_seeds, n_per_root=25)

    # Phase 4 — SERP top 10 for our priority BOFU keywords (URLs to study)
    serp = phase4_serp_organic(SERP_PULL)

    # Phase 5 — what competitors actually rank for
    comp_kws = phase5_competitor_keywords(COMPETITORS, n_per_domain=80)

    # Aggregate
    print()
    print("=" * 60)
    all_metrics = metrics + related + questions
    master = aggregate_master(all_metrics)
    split_by_funnel(master)
    competitor_url_map(serp)

    # Save everything also as JSON for future programmatic use
    json.dump({
        "metrics": metrics,
        "related": related,
        "questions": questions,
        "serp": serp,
        "competitors": comp_kws,
    }, open(OUT / "all_responses.json", "w"), indent=2)

    end_balance = units_balance()
    print()
    print(f"Final unit balance: {end_balance:,}")
    print(f"Units consumed this run: {start_balance - end_balance:,}")
    print(f"All outputs in: {OUT}")


if __name__ == "__main__":
    main()
