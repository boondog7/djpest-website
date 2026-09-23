#!/usr/bin/env python3
"""Hourly Google review watcher for DJ Pest, via the Places API (New). Alerts + keeps the site count in sync.

Why this exists: Google Business Profile emails are unreliable (1 alert email for the first 10
reviews, verified 24/9/2026), and the Business Profile API is still awaiting access approval.

What it does each run:
  - fetches rating, total review count and the up-to-5 reviews Places returns (by relevance)
  - if the count rose or a review it hasn't seen appears -> Telegram alert to Dane
  - if the count rose but the new review isn't among the 5 returned -> still alerts, "text not shown yet"
  - if the count FELL -> alerts too (Google's filter removed a review; worth knowing)

Google Maps Platform terms: review content must not be cached/stored. State keeps only the review
resource names (identifiers), the count and the rating. Text is shown in the alert and discarded.
It also writes Google's own rating + count into build/reviews.json (profile.google_totals) and redeploys
whenever they change, so the website number always matches Google. Review TEXT is never written:
publishing individual reviews stays with sync.py / add.py and Dane.

key + place id: ~/.config/jaystack/google-places.env (GOOGLE_PLACES_API_KEY, DJPEST_PLACE_ID)
launchd: au.com.djpest.places-watch (hourly).     --dry = print, no Telegram, no state write.
"""
import json, pathlib, sys, datetime, urllib.request, urllib.parse

CFG = pathlib.Path.home() / ".config/jaystack"
HERE = pathlib.Path(__file__).resolve().parent
STATE = HERE / "places_watch_state.json"
LOG = HERE / "places_watch.log"
DRY = "--dry" in sys.argv

def env(name):
    f = CFG / name
    out = {}
    if f.exists():
        for l in f.read_text().splitlines():
            l = l.strip()
            if not l or l.startswith("#") or "=" not in l: continue
            k, v = l.removeprefix("export ").split("=", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out

def log(msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M} {msg}"
    print(line)
    if not DRY:
        with LOG.open("a") as fh: fh.write(line + "\n")

def telegram(text):
    e = env("telegram-djpest.env")
    if DRY or not e.get("TELEGRAM_BOT_TOKEN"):
        print("[telegram]", text); return
    data = urllib.parse.urlencode({"chat_id": e["TELEGRAM_CHAT_ID"].strip(), "text": text,
                                   "disable_web_page_preview": "true"}).encode()
    urllib.request.urlopen(f"https://api.telegram.org/bot{e['TELEGRAM_BOT_TOKEN'].strip()}/sendMessage", data, timeout=20)

g = env("google-places.env")
key, pid = g["GOOGLE_PLACES_API_KEY"].strip(), g["DJPEST_PLACE_ID"].strip()
req = urllib.request.Request(f"https://places.googleapis.com/v1/places/{pid}",
      headers={"X-Goog-Api-Key": key, "X-Goog-FieldMask": "rating,userRatingCount,reviews"})
d = json.load(urllib.request.urlopen(req, timeout=30))

count, rating = d.get("userRatingCount", 0), d.get("rating")
reviews = d.get("reviews", [])
prev = json.loads(STATE.read_text()) if STATE.exists() else None

if prev is None:
    log(f"baseline: {count} reviews, {rating}★, {len(reviews)} visible")
else:
    seen = set(prev.get("seen", []))
    new = [r for r in reviews if r["name"] not in seen]
    delta = count - prev.get("count", count)
    if delta > 0 or new:
        lines = [f"⭐ New Google review for DJ Pest — now {count} reviews, {rating}★"]
        for r in new:
            who = r.get("authorAttribution", {}).get("displayName", "someone")
            txt = (r.get("originalText") or r.get("text") or {}).get("text", "").strip()
            lines.append(f"\n{r.get('rating')}★ {who}: {txt[:300] or '(no text)'}")
        if delta > len(new):
            lines.append(f"\n{delta - len(new)} more new review(s) not shown by Google yet. Open GBP to read and reply.")
        lines.append("\nReply within 48h: name the service + suburb, sign — Dane.")
        telegram("\n".join(lines))
        log(f"ALERT +{delta} count, {len(new)} new visible → {count} reviews {rating}★")
    elif delta < 0:
        telegram(f"⚠️ DJ Pest Google reviews dropped {prev['count']} → {count}. Google's filter likely removed {-delta}. Rating now {rating}★.")
        log(f"DROP {prev['count']} → {count}")
    else:
        log(f"no change: {count} reviews, {rating}★")

def push_totals_to_site():
    """Keep the website's review count/rating identical to Google's. reviews_lib uses profile.google_totals."""
    import subprocess
    site = HERE.parent
    rj = site / "build" / "reviews.json"
    data = json.loads(rj.read_text())
    cur = data["profile"].get("google_totals") or {}
    if cur.get("count") == count and float(cur.get("rating") or 0) == float(rating or 0):
        return
    data["profile"]["google_totals"] = {"rating": float(rating), "count": int(count),
        "as_of": datetime.date.today().isoformat(), "source": "Google Business Profile, via Places API (New) watcher"}
    rj.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    r = subprocess.run(["./deploy.sh", "--prod"], cwd=site, capture_output=True, text=True)
    ok = r.returncode == 0
    log(f"site totals -> {count} reviews {rating}★, deploy {'OK' if ok else 'FAILED: ' + r.stderr[-300:]}")
    if not ok:
        telegram(f"⚠️ Review count changed to {count} but the website deploy failed. Check reviews/places_watch.log.")

if not DRY and count:
    push_totals_to_site()

if not DRY:
    seen = set((prev or {}).get("seen", [])) | {r["name"] for r in reviews}
    STATE.write_text(json.dumps({"count": count, "rating": rating, "seen": sorted(seen),
                                 "checked": datetime.datetime.now().isoformat(timespec="seconds")}))
