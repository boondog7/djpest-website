#!/usr/bin/env python3
"""
Round-2 SEMrush extraction — go deeper on questions + competitors to set up
5+ years of content. Uses ~25k units, leaving budget for ad-hoc queries.

Strategy:
  Phase A — phrase_questions on 25 deeper pest roots (5000 units)
  Phase B — phrase_related on 20 deeper roots, 25 rows each (20000 units) — actually too much
            → reduced to 15 roots × 20 rows × 40 units = 12000
  Phase C — domain_organic on 5 more major AU pest competitors (10000 units)

Total target: ~27k units. Saves remainder for follow-up.
"""
import csv, json, os, sys, time, urllib.request, urllib.parse
from pathlib import Path

KEY = os.environ.get("SEMRUSH_API_KEY")
if not KEY:
    sys.exit("SEMRUSH_API_KEY not in env")

DB = "au"
BASE = "https://api.semrush.com/"
OUT = Path("/Users/danejohns/jaystack/djpest/seo/semrush")
RAW = OUT / "raw"
RAW.mkdir(parents=True, exist_ok=True)


def units():
    url = f"https://www.semrush.com/users/countapiunits.html?key={KEY}"
    return int(urllib.request.urlopen(url, timeout=30).read().decode().strip())


def call(params):
    p = {**params, "key": KEY, "database": DB}
    qs = urllib.parse.urlencode(p)
    try:
        with urllib.request.urlopen(f"{BASE}?{qs}", timeout=60) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return f"ERROR :: {e}"


def parse(text):
    if not text or text.startswith("ERROR"):
        return []
    lines = [ln for ln in text.strip().split("\n") if ln]
    if not lines:
        return []
    return list(csv.DictReader(lines, delimiter=";"))


def save_csv(rows, path, fields=None):
    if not rows:
        Path(path).write_text("(no data)")
        return
    if fields is None:
        fields = list(rows[0].keys())
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


# Deeper pest niche roots — informational seeds (TOFU)
QUESTION_SEEDS = [
    "termite damage", "termite swarm", "termite mud tubes",
    "carpenter ant", "pavement ant", "fire ant",
    "german cockroach", "american cockroach", "cockroach eggs",
    "mouse droppings", "rat poison", "rat trap",
    "huntsman spider", "wolf spider", "black house spider",
    "mosquito control", "mosquito bite", "mosquito repellent",
    "flea treatment dog", "bed bug bite", "bed bug eggs",
    "silverfish", "millipede", "earwig",
    "wasp nest", "bee removal", "european wasp",
    "termite inspection cost", "pest control cost"
]

# Related-keyword roots
RELATED_ROOTS = [
    "termite", "ant", "cockroach", "rat", "mouse", "spider",
    "redback spider", "white tail spider", "huntsman",
    "mosquito", "flea", "bed bug", "silverfish", "wasp", "bee",
]

# Round 2 competitor analysis — bigger Aussie players
COMPETITORS_2 = [
    "tomspestcontrolperth.com.au",
    "envirapest.com.au",
    "termicopestmanagement.com.au",
    "perthpest.com.au",
    "swatapest.com.au",
    "homestars.com.au",
]


def phase_a_questions():
    print(f"[A] phrase_questions × {len(QUESTION_SEEDS)} roots × 25 rows")
    rows = []
    for i, q in enumerate(QUESTION_SEEDS, 1):
        text = call({
            "type": "phrase_questions",
            "phrase": q,
            "export_columns": "Ph,Nq,Cp,Co,Nr,Td,In,Kd",
            "display_limit": "25",
            "display_sort": "nq_desc",
        })
        (RAW / f"r2_questions_{i:02d}_{q.replace(' ','_')}.txt").write_text(text)
        out = parse(text)
        for r in out:
            r["_root"] = q
        rows.extend(out)
        print(f"  {q}: {len(out)} rows")
        time.sleep(0.1)
    save_csv(rows, OUT / "r2_questions.csv")
    print(f"  → r2_questions.csv ({len(rows)} rows)")
    return rows


def phase_b_related():
    print(f"[B] phrase_related × {len(RELATED_ROOTS)} roots × 20 rows")
    rows = []
    for i, q in enumerate(RELATED_ROOTS, 1):
        text = call({
            "type": "phrase_related",
            "phrase": q,
            "export_columns": "Ph,Nq,Cp,Co,Nr,Td,In,Kd",
            "display_limit": "20",
            "display_sort": "nq_desc",
        })
        (RAW / f"r2_related_{i:02d}_{q.replace(' ','_')}.txt").write_text(text)
        out = parse(text)
        for r in out:
            r["_root"] = q
        rows.extend(out)
        print(f"  {q}: {len(out)} rows")
        time.sleep(0.1)
    save_csv(rows, OUT / "r2_related.csv")
    print(f"  → r2_related.csv ({len(rows)} rows)")
    return rows


def phase_c_competitors():
    print(f"[C] domain_organic × {len(COMPETITORS_2)} competitors × 60 rows")
    rows = []
    for i, d in enumerate(COMPETITORS_2, 1):
        text = call({
            "type": "domain_organic",
            "domain": d,
            "export_columns": "Ph,Po,Nq,Cp,Co,Tr,Tc,Ur,Td,In,Kd",
            "display_limit": "60",
            "display_sort": "tr_desc",
        })
        (RAW / f"r2_domain_{i:02d}_{d.replace('.', '_')}.txt").write_text(text)
        out = parse(text)
        for r in out:
            r["_competitor"] = d
        rows.extend(out)
        print(f"  {d}: {len(out)} rows")
        time.sleep(0.2)
    save_csv(rows, OUT / "r2_competitor_keywords.csv")
    print(f"  → r2_competitor_keywords.csv ({len(rows)} rows)")
    return rows


def main():
    start = units()
    print(f"Starting unit balance: {start:,}")
    print()
    questions = phase_a_questions()
    related = phase_b_related()
    competitors = phase_c_competitors()
    end = units()
    print()
    print(f"Final unit balance: {end:,}")
    print(f"Used this run: {start - end:,}")
    json.dump({
        "questions": questions,
        "related": related,
        "competitors": competitors,
    }, open(OUT / "r2_responses.json", "w"), indent=2)


if __name__ == "__main__":
    main()
