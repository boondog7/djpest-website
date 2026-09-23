#!/usr/bin/env python3
"""Daily review sync for djpest.com.au.

Sources, best first:
  1. Google Business Profile API (all reviews, full text, replies, true totals) once
     ~/.config/jaystack/gbp-oauth.json exists (run gbp_auth.py once after Google approves API access).
  2. Fallback: Google's "left a review" alert emails in ops@ (read-only IMAP, never marks read).
     These carry only an excerpt, so new reviews land as HOLD until full text arrives.

Then: validate -> rebuild -> deploy (only if what the public sees changed) -> cards for new 4-5 star
reviews -> gated social drafts -> Telegram summary. Nothing is posted to social without Dane's yes.

  sync.py            normal run (launchd daily)
  sync.py --dry      fetch + report, write nothing
"""
import sys, json, re, os, pathlib, imaplib, email, email.header, subprocess, datetime, urllib.request, urllib.parse
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build")); import reviews_lib as RV
CFG = pathlib.Path.home() / ".config/jaystack"
LOG = ROOT / "reviews" / "sync.log"
DRY = "--dry" in sys.argv
# People who must never appear as independent reviews without Dane confirming (ACCC: family/staff reviews).
WATCH = ["johns", "shaw-johnston", "brooke", "danny", "amber", "elliott", "sims"]
FORBIDDEN = [r"\bguarantee", r"100\s?%", r"pest[- ]proof", r"non[- ]toxic", r"\bsafe for (kids|children|pets)\b", r"\bcheapest\b", r"\bpermanent"]
STAR = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5}

def env(name):
    f = CFG / name
    return dict((k.replace("export ", "").strip(), v.strip().strip('"')) for k, v in
                (l.split("=", 1) for l in f.read_text().splitlines() if "=" in l and not l.lstrip().startswith("#"))) if f.exists() else {}

def log(msg):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M} {msg}"; print(line)
    if not DRY:
        with LOG.open("a") as fh: fh.write(line + "\n")

def telegram(text):
    e = env("telegram-djpest.env")
    if DRY or not e.get("TELEGRAM_BOT_TOKEN"): print("[telegram]", text); return
    data = urllib.parse.urlencode({"chat_id": e["TELEGRAM_CHAT_ID"], "text": text, "disable_web_page_preview": "true"}).encode()
    try: urllib.request.urlopen(f"https://api.telegram.org/bot{e['TELEGRAM_BOT_TOKEN']}/sendMessage", data, timeout=20)
    except Exception as ex: log(f"telegram failed: {ex}")

def screen(r):
    """Decide publish vs hold for a review with full text."""
    reasons = []
    if not r.get("text", "").strip(): reasons.append("star-only review, no text to show (still counted in the rating)")
    low = (r.get("author") or "").lower()
    if any(w in low for w in WATCH): reasons.append("reviewer name matches family/staff watchlist: confirm arm's-length customer (ACCC)")
    for p in FORBIDDEN:
        if re.search(p, r.get("text", ""), re.I): reasons.append(f"text contains a claim we can't republish as our own ({p}); publish only after checking it's accurate")
    return reasons

# ---------------------------------------------------------------- source 1: GBP API
def gbp_fetch():
    f = CFG / "gbp-oauth.json"
    if not f.exists(): return None
    c = json.loads(f.read_text())
    tok = json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", urllib.parse.urlencode({
        "client_id": c["client_id"], "client_secret": c["client_secret"], "refresh_token": c["refresh_token"], "grant_type": "refresh_token"}).encode()))["access_token"]
    def get(u):
        return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"Authorization": f"Bearer {tok}"})))
    acct = c.get("account") or get("https://mybusinessaccountmanagement.googleapis.com/v1/accounts")["accounts"][0]["name"]
    loc = c.get("location_id") or RV.load()["profile"]["location_id"]
    base = f"https://mybusiness.googleapis.com/v4/{acct}/locations/{loc}/reviews?pageSize=50"
    out, page, totals = [], "", None
    while True:
        j = get(base + (f"&pageToken={page}" if page else ""))
        totals = {"rating": j.get("averageRating"), "count": j.get("totalReviewCount"), "as_of": datetime.date.today().isoformat()}
        for g in j.get("reviews", []):
            text = re.sub(r"\s*\(Translated by Google\).*", "", g.get("comment", ""), flags=re.S).strip()
            out.append({"id": g["reviewId"], "source": "google", "author": g.get("reviewer", {}).get("displayName", ""),
                        "rating": STAR.get(g.get("starRating"), 0), "date": g.get("createTime", "")[:10], "text": text,
                        "text_complete": True, "reply": (g.get("reviewReply") or {}).get("comment", "")})
        page = j.get("nextPageToken")
        if not page: break
    return out, totals

# ---------------------------------------------------------------- source 2: Gmail alerts
def imap_fetch():
    e = env("gmail-ops-imap.env")
    if not e.get("GMAIL_USER"): return []
    M = imaplib.IMAP4_SSL("imap.gmail.com"); M.login(e["GMAIL_USER"], e["GMAIL_APP_PASSWORD"].replace(" ", ""))
    M.select('"[Gmail]/All Mail"', readonly=True)
    _, ids = M.search(None, '(FROM "businessprofile-noreply@google.com" SUBJECT "review")')
    out = []
    for i in ids[0].split()[-200:]:
        _, data = M.fetch(i, "(BODY.PEEK[])")
        msg = email.message_from_bytes(data[0][1])
        body = ""
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(errors="replace"); break
        m_id = re.search(r"/reviews/([A-Za-z0-9_-]{20,})", body)
        m_star = re.search(r"new (\d)-star review", body)
        if not (m_id and m_star): continue
        # layout: "Read review\n<url>\n\n<Name>\n\n<excerpt>\n\nReply to review"
        m_blk = re.search(r"Read review\s*<[^>]+>\s*\n\s*\n(.+?)\n\s*\n(.*?)\n\s*\nReply to review", body, re.S)
        name = m_blk.group(1).strip() if m_blk else ""
        excerpt = re.sub(r"\s+", " ", m_blk.group(2)).strip() if m_blk else ""
        date = email.utils.parsedate_to_datetime(msg["Date"]).date().isoformat()
        out.append({"id": m_id.group(1), "source": "google", "author": name, "rating": int(m_star.group(1)), "date": date,
                    "text": excerpt, "text_complete": bool(excerpt) and not excerpt.endswith("..."), "reply": ""})
    M.logout()
    return out

# ---------------------------------------------------------------- merge
def merge(d, fetched, authoritative):
    byid = {r["id"]: r for r in d["reviews"]}
    new, changed = [], []
    for f in fetched:
        cur = byid.get(f["id"])
        if cur is None:
            r = {**f, "suburb": "", "services": [], "social": {}}
            if r["text_complete"]:
                reasons = screen(r)
                r["status"] = "hold" if reasons else "publish"
                if reasons: r["hold_reason"] = "; ".join(reasons)
            else:
                r["status"] = "hold"; r["hold_reason"] = "alert email excerpt only; waiting on full text"
            r["text_sha"] = RV.text_hash(r["text"])
            d["reviews"].append(r); new.append(r)
            continue
        # upgrade an excerpt to full text from the API; never touch text we already hold in full
        if authoritative and not cur.get("text_complete") and f["text_complete"]:
            cur.update(text=f["text"], text_complete=True, text_sha=RV.text_hash(f["text"]))
            reasons = screen(cur)
            if cur.get("status") == "hold" and cur.get("hold_reason", "").startswith("alert email") and not reasons:
                cur["status"] = "publish"; cur.pop("hold_reason", None)
            elif reasons: cur["hold_reason"] = "; ".join(reasons)
            changed.append(cur)
        elif authoritative and cur.get("text_complete") and f["text"] != cur["text"]:
            # reviewer edited their review on Google: take their new words (it's their text, not ours)
            cur.update(text=f["text"], text_sha=RV.text_hash(f["text"]), rating=f["rating"]); changed.append(cur)
        if authoritative and f.get("reply") != cur.get("reply"):
            cur["reply"] = f["reply"]; changed.append(cur)
        if authoritative and f["rating"] != cur["rating"]:
            cur["rating"] = f["rating"]; changed.append(cur)
    if authoritative:
        live = {f["id"] for f in fetched}
        for r in d["reviews"]:
            if r["id"] not in live and r.get("status") != "removed":
                r["status"] = "removed"; changed.append(r)
    return new, changed

def public_fingerprint(d):
    return json.dumps([RV.stats(d), [(r["id"], r["text"], r.get("reply"), r.get("suburb"), r.get("services")) for r in RV.shown(d)]])

def main():
    d = RV.load(); before = public_fingerprint(d)
    try:
        res = gbp_fetch()
    except Exception as ex:
        log(f"GBP API failed, falling back to email alerts: {ex}"); res = None
    if res:
        fetched, totals = res; authoritative = True; d["profile"]["google_totals"] = totals; src = "GBP API"
    else:
        fetched = imap_fetch(); authoritative = False; src = "email alerts"
    new, changed = merge(d, fetched, authoritative)
    log(f"{src}: fetched {len(fetched)}, new {len(new)}, changed {len(changed)}")
    if DRY:
        for r in new: print("NEW", r["rating"], r["author"], r["status"], r.get("hold_reason", ""), r["text"][:80])
        return
    RV.DATA.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")

    problems = RV.validate()
    if problems:
        telegram("DJ Pest reviews: build blocked.\n" + "\n".join(problems)); log(f"validate failed {problems}"); sys.exit(3)

    deployed = False
    if public_fingerprint(d) != before:
        r = subprocess.run(["./deploy.sh", "--prod"], cwd=ROOT, capture_output=True, text=True)
        deployed = r.returncode == 0
        log("deploy ok" if deployed else f"deploy FAILED: {r.stdout[-400:]} {r.stderr[-400:]}")

    msgs = []
    for r in new:
        star = "★" * r["rating"]
        line = f"{star} {RV.display_name(r['author'])}: {r['text'][:140]}"
        if r["status"] == "hold": line += f"\n  HOLD: {r.get('hold_reason')}"
        msgs.append(line)
    if new or deployed:
        avg, n = RV.stats(d)
        head = f"DJ Pest reviews: {len(new)} new. Rating {avg} from {n}." + (" Site updated." if deployed else "")
        tail = ("\n\nNext: reply to every review on Google. Tell Claude 'review social drafts' to make the "
                "cards + captions for the new 4-5 star ones; nothing posts without your yes.")
        if any(r["status"] == "hold" for r in new):
            tail += "\nHeld reviews need you: paste the full text / confirm the reviewer isn't family, via reviews/add.py or Claude."
        telegram(head + "\n\n" + "\n".join(msgs) + tail)

if __name__ == "__main__":
    main()
