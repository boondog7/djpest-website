#!/usr/bin/env python3
"""Branded review card: card.py <review_id>  ->  assets/reviews/<slug>-feed.png (1080x1350) + -story.png (1080x1920)."""
import sys, json, pathlib, textwrap, hashlib
from PIL import Image, ImageDraw, ImageFont
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build")); import reviews_lib as RV
OUT = ROOT / "assets" / "reviews"
RAT = ROOT / "assets" / "img" / "rat-crosshair-white.png"
LOGO = ROOT / "assets" / "img" / "logo-white.png"
SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SERIF_I = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
SANS_B = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
BG, INK, INK2, INK3, RED, GOLD = (10, 10, 10), (244, 242, 239), (201, 197, 191), (142, 137, 131), (208, 2, 27), (245, 179, 1)

def slug(rid): return hashlib.sha1(rid.encode()).hexdigest()[:12]

def fit_quote(d, text, box_w, max_h, start=64, floor=34):
    for size in range(start, floor - 1, -2):
        f = ImageFont.truetype(SERIF_I, size)
        cw = d.textlength("abcdefghijklmnopqrstuvwxyz", font=f) / 26
        lines = textwrap.wrap("“" + text + "”", width=max(10, int(box_w / cw)))
        h = len(lines) * size * 1.32
        if h <= max_h: return f, lines, size
    f = ImageFont.truetype(SERIF_I, floor); cw = d.textlength("abcdefghijklmnopqrstuvwxyz", font=f) / 26
    lines = textwrap.wrap("“" + text + "”", width=int(box_w / cw))
    keep = int(max_h // (floor * 1.32)); lines = lines[:keep]; lines[-1] = lines[-1].rstrip(" ,.") + "…”"
    return f, lines, floor

def draw_card(r, W, H, path):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    rat = Image.open(RAT).convert("RGBA"); s = int(W * 0.95); rat = rat.resize((s, int(s * rat.height / rat.width)))
    a = rat.split()[3].point(lambda v: int(v * 0.07)); rat.putalpha(a)
    im.paste(rat, (int(W * 0.30), int(H * 0.30)), rat)
    M = 90
    d.rectangle([0, 0, W, 12], fill=RED)
    logo = Image.open(LOGO).convert("RGBA"); lw = 250; logo = logo.resize((lw, int(lw * logo.height / logo.width)))
    im.paste(logo, (M, 90), logo)
    d.text((W - M, 118), "GOOGLE REVIEW", font=ImageFont.truetype(SANS_B, 26), fill=INK3, anchor="ra")
    top = 90 + logo.height + (110 if H > 1500 else 80)
    sf = ImageFont.truetype(SANS_B, 64)
    for i in range(5):
        d.text((M + i * 70, top), "★", font=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", 64), fill=GOLD if i < r["rating"] else (60, 60, 60))
    qtop = top + 120
    foot = 330
    f, lines, size = fit_quote(d, r["text"], W - 2 * M, H - qtop - foot - 40)
    y = qtop
    for ln in lines:
        d.text((M, y), ln, font=f, fill=INK); y += size * 1.32
    y += 40
    d.rectangle([M, y, M + 60, y + 4], fill=RED); y += 30
    name = RV.display_name(r.get("author"))
    who = name + (f", {r['suburb']}" if r.get("suburb") else "")
    d.text((M, y), who, font=ImageFont.truetype(SANS_B, 40), fill=INK); y += 56
    svc = " · ".join(RV.SERVICE_LABEL.get(x, x) for x in r.get("services", []))
    if svc: d.text((M, y), svc, font=ImageFont.truetype(SANS, 32), fill=INK3)
    d.line([M, H - 150, W - M, H - 150], fill=(40, 40, 40), width=2)
    d.text((M, H - 118), "djpest.com.au/reviews  ·  0468 170 107", font=ImageFont.truetype(SANS_B, 32), fill=INK2)
    d.text((M, H - 70), "DJ Pest Pty Ltd · WA DoH registered pest management business PMB 3000", font=ImageFont.truetype(SANS, 24), fill=INK3)
    im.save(path, optimize=True)

def make(rid):
    d = RV.load(); r = next(x for x in d["reviews"] if x["id"] == rid)
    OUT.mkdir(parents=True, exist_ok=True); s = slug(rid)
    feed, story = OUT / f"{s}-feed.png", OUT / f"{s}-story.png"
    draw_card(r, 1080, 1350, feed); draw_card(r, 1080, 1920, story)
    return feed, story

if __name__ == "__main__":
    for p in make(sys.argv[1]): print(p)
