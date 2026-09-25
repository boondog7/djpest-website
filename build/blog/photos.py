#!/opt/homebrew/bin/python3
"""Shutter Shaz, Photo Desk (Blog Desk): source a post's OWN photos before (or instead of) the writer touching images.

  photos.py <slug> "<query 1>" ["<query 2>" ...] [--n 2] [--subject "German cockroach in a kitchen"]

1. Pexels search (full gallery: 15 per query, landscape) -> skip any photo id already in images.csv (no reuse across posts)
2. numbered contact sheet -> ONE Haiku vision call (claude-lean, visual_check route) ranks candidates for species/scene match
3. downloads the picks at 1800 px, strips EXIF, saves assets/img/blog-<short>-<n>.jpg + .webp (cwebp -q 80)
4. registers each in blog/_drafts/images.csv (slug, file, source, pexels id, photographer, url, licence, date)
Prints JSON: {"files": [...], "alts": [...], "credits": [...]}. Exit 1 if fewer than --n good matches.
"""
import csv, io, json, os, re, subprocess, sys, datetime as dt, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw

SITE = Path.home() / "jaystack/djpest"; IMG = SITE / "assets/img"; REG = SITE / "blog/_drafts/images.csv"
LEAN = str(Path.home() / "business/djpest/hq/bin/claude-lean")
WORK = SITE / "blog/_drafts/.photos"

def key():
    k = os.environ.get("PEXELS_API_KEY")
    if k: return k
    m = re.search(r'^\s*export\s+PEXELS_API_KEY=["\']?([^"\'\n]+)', (Path.home() / ".zshrc").read_text(), re.M)
    return m.group(1) if m else None

def curl_json(url, k):
    r = subprocess.run(["curl", "-s", "-H", f"Authorization: {k}", url], capture_output=True, text=True, timeout=60)
    return json.loads(r.stdout or "{}")

def fetch(url, dest, tries=3):
    import time
    for t in range(tries):
        subprocess.run(["curl", "-s", "-L", "-A", "Mozilla/5.0", "-o", str(dest), url], timeout=120)
        try:
            Image.open(dest).verify(); return True
        except Exception: time.sleep(3 * (t + 1))
    return False

def used_ids():
    if not REG.exists(): return set()
    return {row["pexels_id"] for row in csv.DictReader(open(REG)) if row.get("pexels_id")}

def dhash(im, size=8):
    g = im.convert("L").resize((size + 1, size), Image.LANCZOS)
    px = list(g.get_flattened_data()) if hasattr(g, "get_flattened_data") else list(g.getdata())
    return sum(1 << i for i in range(size * size) if px[(i // size) * (size + 1) + i % size] > px[(i // size) * (size + 1) + i % size + 1])

def site_hashes():
    cache = WORK / "site-dhash.json"; data = json.loads(cache.read_text()) if cache.exists() else {}
    for f in IMG.glob("*.jpg"):
        k = f"{f.name}:{int(f.stat().st_mtime)}"
        if k not in data:
            try: data[k] = dhash(Image.open(f))
            except Exception: pass
    cache.write_text(json.dumps(data)); return list(data.values())

def main():
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(2)
    slug = a[0]; n = 2; subject = ""; queries = []
    i = 1
    while i < len(a):
        if a[i] == "--n": n = int(a[i + 1]); i += 2
        elif a[i] == "--subject": subject = a[i + 1]; i += 2
        else: queries.append(a[i]); i += 1
    subject = subject or queries[0]
    k = key(); assert k, "PEXELS_API_KEY missing"
    stop = {"how", "to", "get", "rid", "of", "a", "the", "do", "what", "is", "are", "can", "i"}
    short = "-".join(w for w in slug.split("-") if w not in stop)[:30]
    WORK.mkdir(parents=True, exist_ok=True); seen = used_ids(); cands = []
    for q in queries:
        d = curl_json(f"https://api.pexels.com/v1/search?query={urllib.parse.quote(q)}&per_page=15&orientation=landscape", k)
        for p in d.get("photos", []):
            if str(p["id"]) in seen or any(c["id"] == p["id"] for c in cands): continue
            if p["width"] < 1600: continue
            cands.append({"id": p["id"], "alt": p.get("alt") or "", "by": p.get("photographer", ""), "url": p.get("url", ""),
                          "orig": p["src"]["original"], "large": p["src"].get("large2x", ""), "thumb": p["src"]["medium"]})
    if len(cands) < n: print(json.dumps({"error": f"only {len(cands)} unused candidates"})); sys.exit(1)
    cands = cands[:24]
    existing = site_hashes()
    # contact sheet
    W, H, cols = 300, 200, 6; rows = (len(cands) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * W, rows * H), "white"); dr = ImageDraw.Draw(sheet)
    for j, c in enumerate(cands):
        t = WORK / f"{c['id']}.jpg"
        try:
            fetch(c["thumb"], t); im = Image.open(t).convert("RGB")
            h = dhash(im)
            if any(bin(h ^ e).count("1") <= 6 for e in existing):
                c["dupe"] = True; continue
            im.thumbnail((W, H))
            x, y = (j % cols) * W, (j // cols) * H; sheet.paste(im, (x, y)); dr.rectangle([x, y, x + 34, y + 20], fill="black"); dr.text((x + 5, y + 4), str(j + 1), fill="yellow")
        except Exception: pass
    cs = WORK / f"{slug}-contact.jpg"; sheet.save(cs, quality=80)
    prompt = (f"Read the contact sheet image at {cs}. It shows {len(cands)} numbered stock photos. A Perth pest control blog post needs {n} photos of: {subject}.\n"
              f"Photographer captions (may be wrong): " + "; ".join(f"{j+1}: {c['alt'][:80]}" for j, c in enumerate(cands)) + "\n"
              "Photos marked DUPLICATE are already used on the site: never pick them. " + ("DUPLICATE: " + ", ".join(str(j + 1) for j, c in enumerate(cands) if c.get("dupe")) + ". " if any(c.get("dupe") for c in cands) else "") + "Pick the photos that clearly and accurately show that subject (correct species, realistic scene, not blurry, no people's faces, no text/watermarks). "
              "Never pick the wrong species. Reply with ONLY JSON: {\"picks\": [numbers in best-first order], \"alts\": [one factual alt text per pick, under 120 chars], \"why\": \"short\"}. "
              f"If fewer than {n} are good, return only the good ones.")
    env = dict(os.environ); env["HQ_ROLE"] = "photo-desk"
    r = subprocess.run([LEAN, "-p", "--output-format", "text", "--model", "haiku", "--max-turns", "4", "--allowedTools", "Read", "--add-dir", str(WORK)],
                       input=prompt, capture_output=True, text=True, timeout=300, env=env)
    m = re.search(r"\{.*\}", r.stdout, re.S)
    pick = json.loads(m.group(0)) if m else {"picks": []}
    picks = [p for p in pick.get("picks", []) if isinstance(p, int) and 1 <= p <= len(cands) and not cands[p - 1].get("dupe")][:n]
    if len(picks) < n: print(json.dumps({"error": f"photo desk found {len(picks)} good matches", "why": pick.get("why", ""), "sheet": str(cs)})); sys.exit(1)
    files, credits, rows, made = [], [], [], []
    for idx, p in enumerate(picks, 1):
        c = cands[p - 1]; raw = WORK / f"{c['id']}-full.jpg"
        ok = fetch(c["orig"] + "?auto=compress&cs=tinysrgb&w=1800", raw) or (c.get("large") and fetch(c["large"], raw))
        if not ok:
            for f in made: f.unlink(missing_ok=True)
            print(json.dumps({"error": f"download failed for Pexels {c['id']}"})); sys.exit(1)
        im = Image.open(raw).convert("RGB")
        if im.width > 1800: im = im.resize((1800, round(im.height * 1800 / im.width)), Image.LANCZOS)
        out = IMG / f"blog-{short}-{idx}.jpg"
        im.save(out, quality=84, optimize=True, progressive=True)  # re-encode = EXIF/GPS stripped
        subprocess.run(["cwebp", "-quiet", "-q", "80", str(out), "-o", str(out.with_suffix(".webp"))], check=False)
        made += [out, out.with_suffix(".webp")]
        files.append("/assets/img/" + out.name); credits.append(f"{c['by']} (Pexels {c['id']})")
        rows.append([dt.date.today().isoformat(), slug, out.name, "pexels", c["id"], c["by"], c["url"], "Pexels License"])
    new_reg = not REG.exists()
    with open(REG, "a", newline="") as fh:   # register only after every pick succeeded
        w = csv.writer(fh)
        if new_reg: w.writerow(["date", "slug", "file", "source", "pexels_id", "photographer", "url", "licence"])
        w.writerows(rows)
    print(json.dumps({"files": files, "alts": pick.get("alts", [])[:n], "credits": credits, "why": pick.get("why", "")}))

if __name__ == "__main__":
    import urllib.parse
    main()
