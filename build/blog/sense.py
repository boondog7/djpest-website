#!/opt/homebrew/bin/python3
"""Sanity Sam (Chief of Common Sense) for the Blog Desk: look at the preview like a reader BEFORE a post is parked.

  sense.py <slug> <preview_url> [--post build/posts/<slug>.html]

1. Screenshots the preview URL (Chromium headless, desktop 1280 wide + mobile 390 wide) into blog/_drafts/screens/<slug>-preview-*.png
2. Tiles the two screenshots into ONE contact sheet (one image = one vision read, not two)
3. Extracts the text a reader sees (title, lede, every H2/H3, image alt+captions, first sentence of each section)
4. One claude-lean call (route sense_check, cheapest model, Read tool for the sheet only) returns PASS / FIX with issues
Writes blog/_drafts/screens/<slug>-sense.json and prints JSON. Exit 0 on PASS, 2 on FIX, 1 on error.
Cost: ~10 to 20K tokens (one image + ~2K of text), one call. No rewrite loop here: a FIX goes back to the writer's repair pass.
"""
from __future__ import annotations
import json, os, re, subprocess, sys, html as _html
from pathlib import Path

SITE = Path.home() / "jaystack/djpest"; SHOTS = SITE / "blog/_drafts/screens"; POSTS = SITE / "build/posts"
LEAN = str(Path.home() / "business/djpest/hq/bin/claude-lean")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PROMPT = """You are DJ Pest's Chief of Common Sense. A Perth homeowner is about to read this blog post. Look at the contact sheet
(desktop on the left, mobile on the right) with the Read tool, then read the text below, and judge it like a careful stranger.

FAIL (verdict FIX) if you see ANY of these:
- a broken layout: overlapping text, a huge blank area, a broken-image icon, text cut off, the hero or figure image missing where the article shows a caption
- a photo that does not fit what the caption or the post says it is (wrong species, wrong scene, stock photo that looks nothing like Perth), or a photo with a face, a house number, a street sign or a readable product label
- a headline, lede or H2 that promises something the post does not deliver, or that reads as clickbait
- placeholder or system text ([TODO], lorem, template words, file names, "Sources: S1")
- a sentence a reader would find confusing, contradictory, cringe, American, or unprofessional for a Perth pest business
- a claim of a job, customer, number, year or result that the text cannot stand behind ("we've had", "our clients", "25 years")
- a chemical rate, a mixing instruction, "guarantee", "100%", "safe for kids/pets", "non-toxic"
- a price that is not phrased as a typical range for a standard three-bedroom home
Do NOT fail it for a text-only first screen (posts have a text hero; photos sit lower), for calm, plain copy, or for being long.

TEXT THE READER SEES:
{text}

Reply with ONLY JSON: {{"verdict": "PASS" or "FIX", "issues": ["short, specific, quote the words"], "fixes": ["what to change, one per issue"]}}"""

def strip(h): return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()

def reader_text(post: Path) -> str:
    txt = post.read_text(); hdr = json.loads(txt.splitlines()[0]); parts = txt.split("\n---\n", 2)
    lede = parts[1] if len(parts) > 2 else ""; body = parts[-1]
    out = [f"TITLE: {hdr.get('title')}", f"DESCRIPTION: {hdr.get('desc')}", f"HERO IMAGE ALT: {hdr.get('alt')}", f"LEDE: {lede.strip()}"]
    for m in re.finditer(r"<(h2|h3)[^>]*>(.*?)</\1>\s*(<p[^>]*>.*?</p>)?", body, re.S | re.I):
        out.append(f"{m.group(1).upper()}: {strip(m.group(2))}" + (f" | {strip(m.group(3))[:220]}" if m.group(3) else ""))
    for m in re.finditer(r'<img[^>]+alt="([^"]*)"[^>]*>(?:\s*<figcaption[^>]*>(.*?)</figcaption>)?', body, re.S):
        out.append(f"FIGURE: alt='{m.group(1)}' caption='{strip(m.group(2) or '')[:200]}'")
    prices = re.findall(r"[^.]*\$[\d,]+[^.]*\.", strip(body))
    if prices: out.append("PRICE SENTENCES: " + " / ".join(p.strip()[:160] for p in prices[:4]))
    return "\n".join(out)[:6000]

def shoot(slug, url):
    from PIL import Image
    SHOTS.mkdir(parents=True, exist_ok=True); shots = []
    for tag, size in (("desktop", "1280,2200"), ("mobile", "390,2000")):
        out = SHOTS / f"{slug}-preview-{tag}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={size}", "--virtual-time-budget=12000",
                        f"--screenshot={out}", url], capture_output=True, timeout=120)
        if out.exists(): shots.append(out)
    if not shots: return None, []
    ims = [Image.open(s).convert("RGB") for s in shots]
    for i, im in enumerate(ims):
        if im.width > 900: ims[i] = im.resize((900, round(im.height * 900 / im.width)))
    h = max(im.height for im in ims); w = sum(im.width for im in ims) + 20 * (len(ims) - 1)
    sheet = Image.new("RGB", (w, min(h, 2600)), "white"); x = 0
    for im in ims: sheet.paste(im.crop((0, 0, im.width, min(im.height, 2600))), (x, 0)); x += im.width + 20
    cs = SHOTS / f"{slug}-preview-sheet.jpg"; sheet.save(cs, quality=78)
    return cs, shots

def run(slug, url, post=None):
    post = Path(post) if post else POSTS / f"{slug}.html"
    sheet, shots = shoot(slug, url)
    if not sheet: return {"verdict": "FIX", "issues": ["could not screenshot the preview"], "fixes": []}
    prompt = f"Contact sheet to Read: {sheet}\n\n" + PROMPT.format(text=reader_text(post))
    env = dict(os.environ); env["HQ_ROLE"] = "chief-of-common-sense"
    r = subprocess.run([LEAN, "-p", "--output-format", "text", "--model", "haiku", "--max-turns", "4", "--allowedTools", "Read", "--add-dir", str(SHOTS)],
                       input=prompt, capture_output=True, text=True, timeout=400, env=env)
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", r.stdout, re.S) or re.search(r"(\{.*\})", r.stdout, re.S)
    try: v = json.loads(m.group(1))
    except Exception: v = {"verdict": "FIX", "issues": ["common-sense check returned no verdict: " + (r.stdout or r.stderr)[-200:]], "fixes": []}
    v.update({"slug": slug, "url": url, "sheet": str(sheet), "shots": [str(s) for s in shots]})
    (SHOTS / f"{slug}-sense.json").write_text(json.dumps(v, indent=1))
    return v

if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2: print(__doc__); sys.exit(1)
    post = a[a.index("--post") + 1] if "--post" in a else None
    v = run(a[0], a[1], post); print(json.dumps(v, indent=1))
    sys.exit(0 if v.get("verdict") == "PASS" else 2)
