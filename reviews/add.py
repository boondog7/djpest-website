#!/usr/bin/env python3
"""Manage a review by hand (until the GBP API is live, and for tagging).
  add.py list                                   show every review and its status
  add.py text   <id-prefix> "<full text copied exactly from Google>"
  add.py tag    <id-prefix> --suburb Warwick --services rodents,ants
  add.py approve <id-prefix>                    Dane confirms: arm's-length customer, text checked -> publish
  add.py hold   <id-prefix> "reason"
  add.py new    --author "Name" --rating 5 --date 2026-09-23 --text "..."   (a Google review the alerts missed)
Text is stored exactly as given and hashed; the build refuses it if it is ever changed afterwards.
"""
import sys, json, argparse, pathlib, datetime, hashlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build")); import reviews_lib as RV
d = RV.load()
def find(p):
    m = [r for r in d["reviews"] if r["id"].startswith(p) or p.lower() in (r.get("author") or "").lower()]
    if len(m) != 1: sys.exit(f"{len(m)} matches for {p!r}")
    return m[0]
a = sys.argv[1:] or ["list"]
cmd = a[0]
if cmd == "list":
    for r in sorted(d["reviews"], key=lambda r: r["date"]):
        print(f'{r["id"][:10]}  {r["rating"]}★ {r["date"]} {r["status"]:8} {RV.display_name(r.get("author")):12} {r.get("suburb",""):12} {",".join(r.get("services",[])):16} {r["text"][:60]!r}')
        if r.get("hold_reason"): print("            hold:", r["hold_reason"])
    avg, n = RV.stats(d); print(f"\nrating {avg} from {n}")
    sys.exit()
if cmd == "text":
    r = find(a[1]); r.update(text=a[2].strip(), text_complete=True, text_sha=RV.text_hash(a[2].strip()))
    r["hold_reason"] = "full text added; waiting on Dane's approve (confirm arm's-length customer)"
elif cmd == "tag":
    ap = argparse.ArgumentParser(); ap.add_argument("x"); ap.add_argument("--suburb", default=None); ap.add_argument("--services", default=None)
    o = ap.parse_args(a[1:]); r = find(o.x)
    if o.suburb is not None: r["suburb"] = o.suburb
    if o.services is not None:
        bad = [s for s in o.services.split(",") if s and s not in RV.SERVICE_LABEL]
        if bad: sys.exit(f"unknown service {bad}; use {list(RV.SERVICE_LABEL)}")
        r["services"] = [s for s in o.services.split(",") if s]
elif cmd == "approve":
    r = find(a[1])
    if not r.get("text_complete"): sys.exit("cannot publish: text is still the truncated alert excerpt. Use: add.py text <id> \"...\"")
    r["status"] = "publish"; r.pop("hold_reason", None); r["approved"] = datetime.date.today().isoformat()
elif cmd == "hold":
    r = find(a[1]); r["status"] = "hold"; r["hold_reason"] = a[2]
elif cmd == "new":
    ap = argparse.ArgumentParser(); [ap.add_argument(f"--{k}") for k in ("author", "rating", "date", "text", "suburb", "services")]
    o = ap.parse_args(a[1:])
    rid = "manual-" + hashlib.sha1(f"{o.author}{o.date}{o.text}".encode()).hexdigest()[:12]
    d["reviews"].append({"id": rid, "source": "google", "author": o.author, "rating": int(o.rating), "date": o.date, "text": o.text.strip(),
        "text_complete": True, "text_sha": RV.text_hash(o.text.strip()), "suburb": o.suburb or "", "services": (o.services or "").split(",") if o.services else [],
        "reply": "", "status": "hold", "hold_reason": "manual entry; approve after checking it matches Google", "social": {}})
    print("added", rid)
else:
    sys.exit(__doc__)
RV.DATA.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
p = RV.validate(); print("ok" if not p else p)
