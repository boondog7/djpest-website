#!/usr/bin/env python3
"""Review -> branded card + caption -> vibe-agent gate -> (Dane says yes) -> Facebook + Instagram.
  social.py drafts                 make card + caption + gate for every published 4-5 star review not yet posted
  social.py post <id-prefix>       publish that review to FB + IG (needs PASS receipts; Dane's yes first)
Cards are served from djpest.com.au/assets/reviews/ so Instagram can fetch them (deploy first).
GBP and TikTok have no API route here yet: the draft prints the text and the story card for Dane to post.
"""
import sys, json, pathlib, subprocess, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build")); sys.path.insert(0, str(ROOT / "reviews"))
import reviews_lib as RV, card as CARD
VIBE = pathlib.Path.home() / ".claude/skills/vibe-agent"
DRAFTS = ROOT / "reviews" / "drafts"; DRAFTS.mkdir(exist_ok=True)

def caption(r, channel="ig"):
    who = RV.display_name(r.get("author")) + (f" in {r['suburb']}" if r.get("suburb") else "")
    t = r["text"].strip()
    first = re.split(r"(?<=[.!?])\s+", t)[0]
    q = t if len(t) <= 300 else t[:t.rfind(" ", 0, 290)] + "\u2026"
    hook = f"\u201c{first}\u201d" if len(first) <= 140 else f"\u201c{q}\u201d"
    body = [hook, ""]
    if q != first: body += [f"\u201c{q}\u201d" if hook != f"\u201c{q}\u201d" else "", ""]
    body += [f"That's {who}, in their own words on Google. Every review we get goes on our website, unedited: djpest.com.au/reviews", "",
             "Written price first, treatment record after.",
             "Text your suburb and what you're seeing to 0468 170 107 for a written price.", "",
             "DJ Pest \u00b7 WA DoH registered pest management business PMB 3000"]
    if channel == "ig":
        tags = ["#perthpestcontrol", "#djpest"]
        if r.get("suburb"): tags.insert(1, "#" + re.sub(r"[^a-z]", "", r["suburb"].lower()) + "wa")
        body += ["", " ".join(tags)]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(body)).strip()

def _unused_gate(text, channel, media_desc, media):
    p = subprocess.run(["python3", str(VIBE / "gate.py"), "--channel", channel, "--type", "post", "--media-desc", media_desc,
                        "--media", str(media), "--consent", "google-public-review"], input=text, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()

def gate_json(text, channel, media_desc, media):
    p = subprocess.run(["python3", str(VIBE / "gate.py"), "--channel", channel, "--type", "post", "--media-desc", media_desc,
                        "--media", str(media), "--consent", "google-public-review", "--json"], input=text, capture_output=True, text=True)
    try: j = json.loads(p.stdout)
    except Exception: j = {"verdict": "ERROR", "raw": (p.stdout + p.stderr)[-400:]}
    return p.returncode, j

def drafts():
    d = RV.load(); n = 0
    for r in RV.shown(d):
        if r["rating"] < 4 or r.get("social", {}).get("posted"): continue
        n += 1; feed, story = CARD.make(r["id"]); s = CARD.slug(r["id"])
        desc = f"DJ Pest review card: {r['rating']} gold stars, the customer's Google review quote in white serif, first name and initial, rat logo, phone and PMB footer"
        print(f"\n=== {RV.display_name(r.get('author'))} {r['rating']}\u2605  feed card {feed}  story card {story}")
        for ch in ("fb", "ig"):
            text = caption(r, ch); code, j = gate_json(text, ch, desc, feed)
            if code == 2 and (j.get("brand") or {}).get("rewrite"):
                text = j["brand"]["rewrite"].strip(); code, j = gate_json(text, ch, desc, feed)
            verdict = {0: "PASS", 2: "FIX", 3: "BLOCK"}.get(code, j.get("verdict", "ERROR"))
            (DRAFTS / f"{s}-{ch}.txt").write_text(text)
            print(f"--- {ch.upper()} [{verdict}]\n{text}")
            if verdict != "PASS": print("   reasons:", "; ".join((j.get("brand") or {}).get("reasons", [])[:3]) or j)
        print(f"--- GBP / TikTok: post the story card by hand with the FB text.")
    if not n: print("no new 4-5 star published reviews to draft")

def post(prefix):
    d = RV.load(); r = next(x for x in d["reviews"] if x["id"].startswith(prefix) or prefix.lower() in (x.get("author") or "").lower())
    s = CARD.slug(r["id"]); feed = ROOT / "assets/reviews" / f"{s}-feed.png"
    fbt, igt = DRAFTS / f"{s}-fb.txt", DRAFTS / f"{s}-ig.txt"
    if not (fbt.exists() and igt.exists()): sys.exit("run social.py drafts first")
    fb = subprocess.run(["python3", str(VIBE / "publish.py"), "fb_post", "--text-file", str(fbt), "--image", str(feed)], capture_output=True, text=True)
    ig = subprocess.run(["python3", str(VIBE / "publish.py"), "ig_post", "--text-file", str(igt), "--image-url", f"https://djpest.com.au/assets/reviews/{s}-feed.png"], capture_output=True, text=True)
    print("FB:", fb.stdout.strip() or fb.stderr.strip()); print("IG:", ig.stdout.strip() or ig.stderr.strip())
    if fb.returncode == 0 and ig.returncode == 0:
        r.setdefault("social", {})["posted"] = True; RV.DATA.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    drafts() if a[0] == "drafts" else post(a[1]) if a[0] == "post" else sys.exit(__doc__)
