#!/opt/homebrew/bin/python3
"""DJ Pest Blog desk: publish the next queued post, end to end, with no silent failures.

Stages (only stage 2 uses a model):
  1 preflight   STOP file, lock, git pull --rebase, auto-commit generated-only diffs (review sync), pick the next queued row
  2 brief+write  brief.py builds blog/_drafts/wip/<slug>/brief.json (hub, siblings, allowed links, prices, fixed strings,
                live primary sources, photos sourced by photos.py, STYLE.md + brand voice). Then ONE claude-lean call
                (route blog_write, cheapest model, tools Read/Write/lint.py only, no web, no build, no git) writes
                wip/<slug>/post.html + sidecar.json, which is copied to build/posts/<slug>.html. (v2, 29 Sep 2026)
  3 gates       script checks: header, compliance scan clean, images real + sized, FAQ >= 6, internal links incl. the
                queue row's service page, word count, no em dashes, no DIY application rates, no quality-bar phrases,
                not already published. One repair pass by the writer, then re-gate.
  4 deploy      ./deploy.sh --prod (plain bash, so no permission prompt can block it)
  4b sense      (--prepare only) Sanity Sam reads the PREVIEW like a reader: screenshots + the text, PASS/FIX; a FIX gets one
                repair pass and a re-check; a second FIX blocks the park (blog/_drafts/failed/<slug>/) and signals
  5 verify      live URL 200 + title, hero image 200, desktop + mobile screenshots, a cheap Haiku visual check
  6 books       QUEUE.md row -> published, PUBLISH-LOG.md, git commit + push
  7 report      HQ signal (digest) on success; on failure: rollback, HQ signal, urgent after 2 failures in a row

Usage: publish.py [--prepare] [--dry] [--slug <slug>]
  --prepare  write + gate the next queued post, park it in blog/_drafts/ready/<slug>/, deploy a PREVIEW, mark the row
             "ready <date>". The next normal run publishes a ready draft (re-gated, no rewrite) before writing anything new.
  --dry      stop after gates and roll back
Owner: Head of Blog (HQ). Model routing: Meter Maddie (hq/models.json route "draft").
"""
from __future__ import annotations
import fcntl, json, os, re, subprocess, sys, time, datetime as dt
from pathlib import Path

SITE = Path.home() / "jaystack/djpest"
POSTS = SITE / "build/posts"; IMG = SITE / "assets/img"; DRAFTS = SITE / "blog/_drafts"
QUEUE = DRAFTS / "QUEUE.md"; PLOG = DRAFTS / "PUBLISH-LOG.md"; SHOTS = DRAFTS / "screens"
HQ = Path.home() / "business/djpest/hq"; HQPY = HQ / ".venv/bin/python"
LEAN = str(HQ / "bin/claude-lean"); SKILL = Path.home() / ".claude/skills/content-pipeline/SKILL.md"
STATE = SITE / "build/blog/state.json"; LOG = SITE / "build/publish.log"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROLE = "head-of-blog"
DRY = "--dry" in sys.argv; PREPARE = "--prepare" in sys.argv; READY = DRAFTS / "ready"
WIP = DRAFTS / "wip"; FAILED = DRAFTS / "failed"; HOLD = DRAFTS / "HOLD"; STYLEMD = SITE / "blog/STYLE.md"
sys.path.insert(0, str(SITE / "build/blog"))
def route(name, key, default):
    try: return json.loads((HQ / "models.json").read_text())["routes"][name][key]
    except Exception: return default
WRITE_BUDGET_USD = str(route("blog_write", "max_usd_per_run", 1.5)); REPAIR_BUDGET_USD = str(route("blog_repair", "max_usd_per_run", 0.8))
WRITER_MODEL = "haiku"   # Dane 28 Sep 2026: every automation on the cheapest model (models.json policy)
GENERATED_OK = re.compile(r"^(build/reviews\.json|[^/]+\.html|blog/[^/]+\.html|blog\.html|sitemap\.xml|llms\.txt|reviews/.*\.(log|out|json))$")

def log(m):
    line = f"{dt.datetime.now():%Y-%m-%d %H:%M:%S} {m}"; print(line)
    with open(LOG, "a") as f: f.write(line + "\n")

def sh(cmd, cwd=SITE, timeout=900, env=None, inp=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, env=env, input=inp)

def signal(sev, title, detail="", url=""):
    if DRY: log(f"[dry] signal {sev}: {title} | {detail[:200]}"); return
    sh([str(HQPY), str(HQ / "hq.py"), "signal", ROLE, sev, title, detail[:600], url], cwd=HQ)
    if sev == "urgent": sh([str(HQPY), str(HQ / "hq.py"), "flush-urgent"], cwd=HQ)

def zsh_env(*names):
    env = dict(os.environ); rc = (Path.home() / ".zshrc").read_text()
    for n in names:
        m = re.search(rf'^\s*export\s+{n}=["\']?([^"\'\n]+)', rc, re.M)
        if m and n not in env: env[n] = m.group(1)
    env["PATH"] = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:" + env.get("PATH", "")
    return env

def state(): return json.loads(STATE.read_text()) if STATE.exists() else {}
def put_state(s): STATE.write_text(json.dumps(s, indent=1))

# ------------------------------------------------------------------ 1 preflight
def preflight():
    if (HQ / "STOP").exists(): raise Fail("preflight", "HQ STOP file present")
    r = sh(["git", "pull", "-q", "--rebase", "--autostash"])
    if r.returncode: raise Fail("preflight", "git pull failed: " + (r.stderr or r.stdout)[-300:])
    dirty = [l[3:] for l in sh(["git", "status", "--porcelain"]).stdout.splitlines() if l.strip()]
    if dirty:
        bad = [p for p in dirty if not GENERATED_OK.match(p)]
        gen = [p for p in dirty if GENERATED_OK.match(p)]
        # Other sessions' work in progress no longer blocks a slot: deploys are built from a clean export of HEAD plus this
        # run's own files (see clean_src), so a half-written file elsewhere in the tree can never ship. Just record it.
        if bad: log("note: uncommitted non-blog changes left alone: " + ", ".join(bad[:6]))
        if gen and not DRY:
            sh(["git", "add", "--"] + gen); sh(["git", "commit", "-q", "-m", "Sync generated pages (reviews/build) before blog run"])
            log(f"committed {len(gen)} generated files")

def next_row(force_slug=None):
    rows = []
    for ln in QUEUE.read_text().splitlines():
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) >= 7 and cells[0].isdigit():
            rows.append({"n": cells[0], "slug": cells[1], "primary": cells[2], "fold": cells[3], "bundles": cells[4], "service": cells[5], "status": cells[6], "line": ln})
    if force_slug: return next((r for r in rows if r["slug"] == force_slug), None)
    if not PREPARE:
        ready = next((r for r in rows if r["status"].lower().startswith("ready")), None)
        if ready: return ready
    return next((r for r in rows if r["status"].lower() == "queued"), None)

def park(row):
    """Move the written post + its images into blog/_drafts/ready/<slug>/ so the tree is clean until publish day."""
    import shutil
    d = READY / row["slug"]; d.mkdir(parents=True, exist_ok=True)
    post = POSTS / f"{row['slug']}.html"; hdr = json.loads(post.read_text().splitlines()[0]); body = post.read_text()
    files = [post] + [SITE / i.lstrip("/") for i in set([hdr["img"]] + re.findall(r'src="(/assets/img/[^"]+)"', body))]
    files += [f.with_suffix(".webp") for f in files if f.suffix == ".jpg" and f.with_suffix(".webp").exists()]
    manifest = []
    for f in files:
        if f.exists():
            rel = f.relative_to(SITE); dst = d / rel; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(f, dst); manifest.append(str(rel))
    for extra in ("sidecar.json", "brief.json"):
        if (WIP / row["slug"] / extra).exists(): shutil.copy2(WIP / row["slug"] / extra, d / extra)
    (d / "manifest.json").write_text(json.dumps(manifest, indent=1)); return manifest

def unpark(row):
    import shutil
    d = READY / row["slug"]; manifest = json.loads((d / "manifest.json").read_text())
    for rel in manifest: dst = SITE / rel; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(d / rel, dst)
    return manifest

def set_status(row, status):
    QUEUE.write_text(QUEUE.read_text().replace(row["line"], row["line"].replace(f"| {row['status']} |", f"| {status} |")))

# ------------------------------------------------------------------ 2 write (v2: brief pack, no web tools)
WRITER_TASK = """You are Inky Quill, DJ Pest's blog writer. Write exactly ONE post from the brief pack and stop.
Brief pack (Read it first, it is the ONLY source of facts, links, images, prices and sources you may use): {brief}
Style guide (already in your system prompt): blog/STYLE.md. Follow its template, voice, fixed strings and file format exactly.

Write these two files and nothing else:
  1. {wip}/post.html   (line 1 one-line JSON header, then ---, then the lede paragraph, then ---, then the article HTML; see STYLE.md section 7)
  2. {wip}/sidecar.json (STYLE.md section 8)
Then run:  python3 build/blog/lint.py {wip}/post.html --brief {brief}
and fix your post until it prints "lint: clean". Do not edit any other file. No web, no build.py, no git.

Non-negotiables the script enforces: only links from brief.links_available (the hub {service} plus at least one sibling /blog/ post and one more);
only the images in brief.photos.files with their alt text; only the price figures in brief.prices; only external links from brief.sources;
6 to 8 FAQ <h3> under <h2>Frequently asked</h2>; a <h2>Sources</h2> list; 1,100 to 2,400 words; NO em or en dashes; no application
rates; no invented jobs, customers, numbers or years; Australian English; "management" not "control" in body copy.
Primary keyword: {primary}. Fold these in as H2s or FAQ questions: {fold}. Today: {today}. Season in Perth: {season}.
End your reply with exactly one line: WROTE {slug}  or  FAILED <reason>."""

REPAIR_TASK = """The post {wip}/post.html failed these checks. Fix ONLY that file (and sidecar.json if a claim changed), using only facts,
links, images and prices from the brief {brief}. Re-run  python3 build/blog/lint.py {wip}/post.html --brief {brief}  until clean.
End with exactly one line: WROTE {slug}  or  FAILED <reason>.
Problems:
- {errs}"""

def run_writer(prompt, budget, turns, slug):
    env = dict(os.environ); env["HQ_ROLE"] = "blog-writer" if turns > 12 else "blog-repair"; env["PATH"] = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:" + env.get("PATH", "")
    wip = WIP / slug
    cmd = [LEAN, "-p", "--output-format", "text", "--model", WRITER_MODEL, "--max-turns", str(turns), "--max-budget-usd", budget,
           "--permission-mode", "acceptEdits", "--append-system-prompt-file", str(STYLEMD),
           "--allowedTools", f"Read,Write,Edit,Bash(python3 build/blog/lint.py:*),Bash(python3 {SITE}/build/blog/lint.py:*)",
           "--disallowedTools", "WebSearch,WebFetch,Glob,Grep,Task,Bash(curl:*),Bash(git:*),Bash(python3 build/build.py:*)",
           "--add-dir", str(wip)]
    before = untracked()
    r = sh(cmd, env=env, timeout=1800, inp=prompt)
    out = (r.stdout or "").strip(); stop = "?"
    try:
        last = [json.loads(l) for l in (HQ / "ledger.jsonl").read_text().splitlines() if f'"{env["HQ_ROLE"]}"' in l][-1]
        stop = f"{last.get('stop')} US${(last.get('usd') or 0):.2f}"
    except Exception: pass
    strays = [p for p in untracked() - before if not p.startswith(("build/posts/", "assets/img/", "blog/_drafts/"))]
    if strays: log(f"note: new untracked files appeared during the writer run (left alone; other sessions share this tree): {strays[:6]}")
    log("writer: " + (out.splitlines()[-1] if out else f"(no output) rc={r.returncode}") + f" [{stop}]")
    return out if out else f"FAILED writer stopped: {stop}"

def resume_failed(slug):
    """--resume: reuse the newest failed/<slug>-*/ draft (post, sidecar, brief, images) instead of paying the writer again."""
    import shutil
    cands = sorted(FAILED.glob(f"{slug}-*"), reverse=True)
    for d in cands:
        if (d / "post.html").exists() and (d / "brief.json").exists():
            wip = WIP / slug; shutil.rmtree(wip, ignore_errors=True); shutil.copytree(d, wip)
            for f in (wip / "img").glob("*"): shutil.copy2(f, IMG / f.name)
            b = json.loads((wip / "brief.json").read_text())
            missing = [i for i in b.get("photos", {}).get("files", []) if not (SITE / i.lstrip("/")).exists()]
            if missing: log(f"resume: images missing {missing}; falling back to a fresh brief"); return None
            (POSTS / f"{slug}.html").write_text((wip / "post.html").read_text()); log(f"resume: reused {d.relative_to(SITE)} (no writer call)"); return b
    return None

def write_post(row):
    """brief -> writer -> copy wip/post.html into build/posts/. Raises Fail on a brief problem or a writer FAILED."""
    import brief as briefmod
    slug = row["slug"]
    if "--resume" in sys.argv:
        b = resume_failed(slug)
        if b: return b
    b = briefmod.build(slug)
    if b.get("error"): raise Fail("brief", b["error"])
    if b.get("problems"): raise Fail("brief", "; ".join(b["problems"]))
    log(f"brief: {len(b['sources'])} sources, {len(b['siblings'])} siblings, photos {b['photos'].get('files')}")
    wip = WIP / slug; bp = wip / "brief.json"
    prompt = WRITER_TASK.format(brief=bp, wip=wip, service=row["service"], primary=row["primary"], fold=row["fold"], today=b["today"], season=b["season"], slug=slug)
    out = run_writer(prompt, WRITE_BUDGET_USD, 35, slug)
    last = out.splitlines()[-1] if out else "FAILED no output"
    if not (wip / "post.html").exists(): raise Fail("write", last if "FAILED" in last else "writer ended without writing post.html")
    if "WROTE" not in last:
        # 29 Sep: Haiku wrote a clean post but ran out of turns before saying WROTE; the file is the deliverable, so lint decides
        import lint as lintmod
        le = lintmod.check(wip / "post.html", json.loads(bp.read_text()))
        if le and "FAILED" in last: raise Fail("write", last)
        log(f"writer ended without WROTE ({last[:60]}); post.html present, lint {'clean' if not le else str(len(le)) + ' problems'}: continuing to gates")
    (POSTS / f"{slug}.html").write_text((wip / "post.html").read_text())
    return b

def repair_post(row, errs, budget=None, turns=20):
    slug = row["slug"]; wip = WIP / slug; bp = wip / "brief.json"
    if not (wip / "post.html").exists() and (POSTS / f"{slug}.html").exists(): wip.mkdir(parents=True, exist_ok=True); (wip / "post.html").write_text((POSTS / f"{slug}.html").read_text())
    run_writer(REPAIR_TASK.format(wip=wip, brief=bp, slug=slug, errs="\n- ".join(errs)), budget or REPAIR_BUDGET_USD, turns, slug)
    if (wip / "post.html").exists(): (POSTS / f"{slug}.html").write_text((wip / "post.html").read_text())

def fail_wip(slug):
    import shutil
    if (WIP / slug).exists():
        # keep the Photo Desk's images with the failed draft so a retry does not pay for them again (brief.py restores them)
        try:
            b = json.loads((WIP / slug / "brief.json").read_text())
            for i in b.get("photos", {}).get("files", []):
                for f in (SITE / i.lstrip("/"), (SITE / i.lstrip("/")).with_suffix(".webp")):
                    if f.exists(): (WIP / slug / "img").mkdir(exist_ok=True); shutil.copy2(f, WIP / slug / "img" / f.name)
        except Exception: pass
        FAILED.mkdir(parents=True, exist_ok=True); dst = FAILED / f"{slug}-{dt.datetime.now():%Y%m%d-%H%M}"
        shutil.move(str(WIP / slug), str(dst)); log(f"wip moved to {dst.relative_to(SITE)}")

def untracked():
    return set(l for l in sh(["git", "ls-files", "--others", "--exclude-standard"]).stdout.splitlines() if l)

# ------------------------------------------------------------------ 3 gates
BANNED = ["in today's fast-paced world", "this comprehensive guide", "everything you need to know", "look no further",
          "faucet", "cilantro", "neighbor", "favorite", " color ", "exterminat", "guarantee", "100%", "non-toxic", "pest-proof"]
RATE = re.compile(r"\b\d+(?:\.\d+)?\s?(?:mL|ml|g|grams?)\s?(?:/|per)\s?(?:L|litre|liter|\d+\s?L|m2|m²|square metre)", re.I)

def image_content_errors(hdr, body, skip=()):
    """Ask Haiku (vision) whether each image actually shows what its alt text / caption says. Any MISMATCH fails the gate."""
    pairs = [(hdr.get("img", ""), hdr.get("alt", ""))]
    for fig in re.findall(r"<img[^>]+>(?:\s*<figcaption[^>]*>(.*?)</figcaption>)?", body, re.S):
        pass
    for m in re.finditer(r'<img[^>]+src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>(?:\s*<figcaption[^>]*>(.*?)</figcaption>)?', body, re.S):
        pairs.append((m.group(1), (m.group(2) + ". Caption: " + re.sub("<[^>]+>", "", m.group(3) or "")).strip(". ")))
    errs = []
    for src, claim in pairs:
        f = SITE / src.lstrip("/")
        if not src.startswith("/assets/img/") or not f.exists(): continue
        if src in skip: log(f"image check {src}: verified by the Photo Desk before writing (skipped)"); continue
        env = zsh_env(); env["HQ_ROLE"] = "blog-image-check"
        q = (f"Read the image {f}. A pest control blog says this picture shows: \"{claim}\". Does the picture really show that (right subject, "
             "right kind of animal/insect or body part, nothing unrelated)? Reply with one line: MATCH or MISMATCH <what it actually shows>.")
        v = sh([LEAN, "-p", "--output-format", "text", "--model", "haiku", "--max-turns", "3", "--allowedTools", "Read", "--add-dir", str(f.parent)], env=env, inp=q, timeout=240)
        line = (v.stdout.strip().splitlines() or ["(no verdict)"])[-1]
        log(f"image check {src}: {line}")
        if not line.upper().startswith("MATCH"):
            errs.append(f"image {src} does not show what the post says ({claim[:80]}): {line[:120]}. Replace it with a correct photo.")
    return errs

def gates(row):
    slug = row["slug"]; p = POSTS / f"{slug}.html"; errs = []
    if not p.exists(): return [f"post file build/posts/{slug}.html was not written"]
    txt = p.read_text(); parts = txt.split("\n---\n", 2)
    try: hdr = json.loads(txt.splitlines()[0])
    except Exception: return ["line 1 is not a valid JSON header"]
    for k in ("slug", "title", "desc", "img", "alt", "date", "read", "service", "service_label"):
        if not hdr.get(k): errs.append(f"header missing '{k}'")
    if hdr.get("slug") != slug: errs.append(f"header slug is '{hdr.get('slug')}', expected '{slug}'")
    if hdr.get("service") != row["service"]: errs.append(f"header service is '{hdr.get('service')}', queue says '{row['service']}'")
    if len(parts) < 3: errs.append("file must be: JSON header, ---, lede, ---, article HTML")
    body = parts[-1] if parts else txt
    # images
    imgs = [hdr.get("img", "")] + re.findall(r'<img[^>]+src="([^"]+)"', body)
    if "og-default" in hdr.get("img", ""): errs.append("hero image is the default site image; use a real photo")
    if len(set(i for i in imgs if i)) < 2: errs.append("needs 2 distinct real images (hero + one in the article)")
    for i in set(i for i in imgs if i.startswith("/assets/img/")):
        f = SITE / i.lstrip("/")
        if not f.exists(): errs.append(f"image {i} does not exist"); continue
        try:
            w = int(sh(["sips", "-g", "pixelWidth", str(f)]).stdout.split()[-1])
            if w < 1200: errs.append(f"image {i} is only {w}px wide (need 1200+)")
        except Exception: pass
        if not f.with_suffix(".webp").exists(): errs.append(f"missing .webp for {i}")
        if sh(["git", "ls-files", "--error-unmatch", i.lstrip("/")]).returncode == 0:
            errs.append(f"image {i} is an existing site photo; download a NEW one for this post")
    # structure
    faq = re.split(r"<h2>[^<]*(?:Frequently asked|Quick answers|FAQ|Common questions)[^<]*</h2>", body, flags=re.I)
    nq = len(re.findall(r"<h3", faq[1])) if len(faq) > 1 else 0
    if nq < 6: errs.append(f"FAQ has {nq} questions (need 6+ <h3> under a 'Frequently asked' or 'Quick answers' <h2>)")
    # images must be this post's own (world-class: no recycled photos from other pages)
    for i in set(i for i in imgs if i.startswith("/assets/img/")):
        base = i.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        def reuses(f):
            t = f.read_text(errors="ignore")
            hits = [m.start() for m in re.finditer(re.escape(base), t)]
            # a listing card for THIS post (blog index, related-posts blocks) sits next to a link to /blog/<slug>: not reuse
            return any(f"/blog/{slug}" not in t[max(0, h - 600): h + 600] for h in hits)
        users = [str(f.relative_to(SITE)) for f in list(SITE.glob("*.html")) + list((SITE / "blog").glob("*.html")) + list(POSTS.glob("*.html"))
                 if f.stem != slug and reuses(f)]
        if users: errs.append(f"image {i} is already used on {users[0]}; source a new photo for this post")
    links = set(re.findall(r'href="(/[^"#?]*)"', body))
    if row["service"] not in links: errs.append(f"no link to the service page {row['service']}")
    if not any(l.startswith("/blog/") for l in links): errs.append("link at least one related blog post (/blog/...) to build the topic cluster")
    sib = [f.stem for f in (SITE / "blog").glob("*.html") if f.stem != slug and set(slug.split("-")) & set(f.stem.split("-")) - {"how", "to", "get", "rid", "of", "a", "the", "do", "what", "is"}]
    if sib and not any(f"/blog/{x}" in links for x in sib): errs.append(f"link the sibling post(s) on the same pest: {', '.join('/blog/' + x for x in sib[:3])}")
    for m in re.findall(r"\b(we've had|we have had|our customers|one of our (?:clients|customers)|last (?:week|month) we|we recently|a customer (?:told|called|rang))\b[^.]{0,60}", re.sub(r"<[^>]+>", " ", txt), re.I):
        errs.append(f"unsourced first-hand claim '{m}' (only use experience from Dane's field notes, or rephrase generally)")
    missing = [l for l in links if l not in ("/",) and not ((SITE / (l.strip("/") + ".html")).exists() or (SITE / l.strip("/") / "index.html").exists() or (POSTS / (l.rsplit("/", 1)[-1] + ".html")).exists())]
    if missing: errs.append("internal links to pages that don't exist: " + ", ".join(sorted(missing)[:6]))
    if len(links) < 3: errs.append(f"needs at least 3 distinct internal links (has {len(links)})")
    words = len(re.sub(r"<[^>]+>", " ", parts[1] + " " + body if len(parts) > 2 else body).split())
    if not 1100 <= words <= 2400: errs.append(f"{words} words (need 1,100 to 2,400)")
    if "—" in txt: errs.append(f"{txt.count('—')} em dashes (Dane's style: none)")
    for m in RATE.findall(re.sub(r"<[^>]+>", " ", txt)): errs.append(f"application rate in copy: '{m}' (say 'at the label rate')")
    for m in re.findall(r"\b(WDJ|Danny|\d+\+?\s*years?(?: of)? (?:experience|in business|in pest)|1,000\+?|thousands of (?:customers|clients|homes)|since 19\d\d|family[- ]owned for)\b", re.sub(r"<[^>]+>", " ", txt), re.I):
        errs.append(f"legacy/unverifiable business claim '{m}' (DJ Pest is a new business: remove it)")
    low = txt.lower()
    for b in BANNED:
        if b in low: errs.append(f"banned phrase: '{b.strip()}'")
    # compliance scanner (the site's own)
    b = sh([sys.executable, "build/build.py"])
    if "compliance scan: clean" not in b.stdout: errs.append("compliance scan not clean: " + (b.stdout + b.stderr)[-400:])
    # images must SHOW what they claim (28 Sep: a "white tail bite" photo was a football game; the card was a man with binoculars)
    if not errs:
        verified = set()
        try:
            b = json.loads((WIP / slug / "brief.json").read_text())
            verified = {f for f in b.get("photos", {}).get("files", []) if any(c.startswith(f + ": MATCH") for c in b.get("photos", {}).get("checks", []))}
        except Exception: pass
        errs += image_content_errors(hdr, body, skip=verified)   # 29 Sep: Haiku flipped MATCH/MISMATCH on the same file between runs; one full-res check per photo is the rule
    return errs

def clean_src(slug):
    """A deploy tree = git HEAD exported + this run's post, its images and the regenerated pages. Nothing else in the working copy."""
    import shutil
    src = Path("/tmp/djpest-deploy"); shutil.rmtree(src, ignore_errors=True); src.mkdir(parents=True)
    subprocess.run(f"git archive HEAD | tar -x -C {src}", shell=True, cwd=SITE, check=True)
    own = [f"build/posts/{slug}.html", "build/reviews.json"]
    post = POSTS / f"{slug}.html"
    if post.exists():
        hdr = json.loads(post.read_text().splitlines()[0])
        for i in set([hdr.get("img", "")] + re.findall(r'src="(/assets/img/[^"]+)"', post.read_text())):
            if i: own += [i.lstrip("/"), i.lstrip("/").rsplit(".", 1)[0] + ".webp"]
    for rel in own:
        f = SITE / rel
        if f.exists(): (src / rel).parent.mkdir(parents=True, exist_ok=True); shutil.copy2(f, src / rel)
    for d in ("functions", "reviews"):   # runtime dirs that must ship as HEAD has them (already in the archive)
        pass
    return src

def deploy(slug, *args):
    env = dict(os.environ); env["DEPLOY_SRC"] = str(clean_src(slug)); env["PATH"] = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:" + env.get("PATH", "")
    r = sh(["./deploy.sh", *args], timeout=900, env=env)
    if r.returncode: log(f"deploy {' '.join(args)} failed rc={r.returncode}: {(r.stdout + r.stderr)[-500:]}")
    return r

def rollback(slug):
    """Undo only what a blog run creates: the new post source, new images, and pages regenerated by build.py.
    Never a blanket checkout: other uncommitted work in the repo is left alone."""
    changed = [l[3:] for l in sh(["git", "status", "--porcelain"]).stdout.splitlines() if l.startswith(" M") or l.startswith("M ")]
    gen = [p for p in changed if GENERATED_OK.match(p) and p != "build/reviews.json"]
    if gen: sh(["git", "checkout", "--"] + gen)
    sh(["git", "clean", "-fq", f"build/posts/{slug}.html"])
    new_imgs = [l[3:] for l in sh(["git", "status", "--porcelain", "assets/img", "blog"]).stdout.splitlines() if l.startswith("??")]
    new_imgs = [p for p in new_imgs if not p.startswith("blog/_drafts/")]
    if new_imgs: sh(["git", "clean", "-fq", "--"] + new_imgs)
    log(f"rolled back {len(gen)} generated pages + {len(new_imgs)} new files for {slug}")

# ------------------------------------------------------------------ 5 verify
def verify(slug, title, hero):
    url = f"https://djpest.com.au/blog/{slug}"; ok = False
    for _ in range(12):
        r = sh(["curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}", url + f"?v={int(time.time())}"])
        if r.stdout == "200":
            html = sh(["curl", "-s", "-L", url + f"?v={int(time.time())}"]).stdout
            if title.split(":")[0][:40] in html or slug in html: ok = True; break
        time.sleep(10)
    if not ok: raise Fail("verify", f"{url} not serving the new post after 2 minutes")
    if sh(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "https://djpest.com.au" + hero]).stdout != "200":
        raise Fail("verify", f"hero image {hero} not serving")
    SHOTS.mkdir(parents=True, exist_ok=True)
    shots = []
    for tag, size in (("desktop", "1280,2000"), ("mobile", "390,1800")):
        out = SHOTS / f"{slug}-{tag}.png"
        sh([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={size}", "--virtual-time-budget=12000", f"--screenshot={out}", url], timeout=120)
        if out.exists(): shots.append(out)
    verdict = "no screenshot"
    if shots:
        env = zsh_env(); env["HQ_ROLE"] = "blog-visual-check"
        q = (f"Read these two screenshots of a newly published blog page ({', '.join(str(s) for s in shots)}). Judge as a stranger in 2 seconds: "
             "is there a readable headline, body text, and no broken layout (overlaps, huge blank areas, broken image icons)? Posts have a text-only "
             "hero; photos sit in the article further down and may be below the fold, so a text-only first screen is fine. FAIL only for a real "
             "problem a reader would notice, or a visible photo that clearly does not fit a pest-control article. Reply with one line: PASS <reason> or FAIL <reason>.")
        v = sh([LEAN, "-p", "--output-format", "text", "--model", "haiku", "--max-turns", "4", "--allowedTools", "Read", "--add-dir", str(SHOTS)], env=env, inp=q, timeout=300)
        verdict = (v.stdout.strip().splitlines() or ["(no verdict)"])[-1]
    log(f"visual check: {verdict}")
    return url, verdict

# ------------------------------------------------------------------ 6 books
def books(row, title):
    today = dt.date.today().isoformat()
    set_status(row, f"published {today}")
    import shutil; shutil.rmtree(READY / row["slug"], ignore_errors=True)
    m = re.match(r"(.*?)\s*(\d[\d/]*)?\s*$", row["primary"]); kw, vol = (m.group(1) or row["primary"]).strip(), (m.group(2) or "-")
    with open(PLOG, "a") as f: f.write(f"{today} | {row['slug']} | {kw} | {vol}\n")
    sh(["git", "add", "-A"])
    sh(["git", "commit", "-q", "-m", f"Publish blog: {row['slug']}\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"])
    r = sh(["git", "pull", "-q", "--rebase"]); p = sh(["git", "push", "-q", "origin", "main"])
    if p.returncode: log("git push failed (post is live; books committed locally): " + p.stderr[-200:])

EXIT = [0]

class Fail(Exception):
    def __init__(self, stage, why): super().__init__(f"{stage}: {why}"); self.stage = stage; self.why = why

def main():
    force = sys.argv[sys.argv.index("--slug") + 1] if "--slug" in sys.argv else None
    lock = open(SITE / "build/blog/.lock", "w")
    try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError: log("another blog run is active"); return
    st = state(); row = None
    log(f"=== blog run start{' (dry)' if DRY else ''} ===")
    try:
        preflight()
        row = next_row(force)
        if not row: signal("notable", "Blog queue is empty", "Refill: seo/semrush/build_blog_pipeline.py or add rows to QUEUE.md."); return
        log(f"row {row['n']}: {row['slug']} ({row['status']})")
        if f"| {row['slug']} |" in PLOG.read_text():
            raise Fail("preflight", f"{row['slug']} is already published; mark its QUEUE.md row")
        if row["status"].lower().startswith("ready"):
            unpark(row); log("restored ready draft")
            if not PREPARE:   # the post goes live today: its date is today
                pf = POSTS / f"{row['slug']}.html"; ls = pf.read_text().split("\n"); h = json.loads(ls[0]); h["date"] = dt.date.today().isoformat()
                ls[0] = json.dumps(h, ensure_ascii=False); pf.write_text("\n".join(ls))
        else:
            if (POSTS / f"{row['slug']}.html").exists(): raise Fail("preflight", f"build/posts/{row['slug']}.html already exists")
            write_post(row)
        errs = gates(row)
        if errs:
            log("gates failed: " + " | ".join(errs))
            short = "-".join(w for w in row["slug"].split("-") if w not in ("how", "to", "get", "rid", "of", "a", "the", "do", "what", "is", "are"))[:30]
            img_help = (f"\nIMAGES: download two NEW photos from Pexels (curl -H \"Authorization: $PEXELS_API_KEY\" \"https://api.pexels.com/v1/search?query=...&per_page=8\"), "
                        f"look at them, pick ones that truly show the subject, save as assets/img/blog-{short}-1.jpg and assets/img/blog-{short}-2.jpg (?w=1600), "
                        f"run cwebp -q 80 on each, then point the header \"img\" and the in-article <img src> at them. Existing files in assets/img are not allowed."
                        ) if any("image" in e for e in errs) else ""
            repair_post(row, errs + ([img_help] if img_help else []))
            errs = gates(row)
            if errs: raise Fail("gates", " | ".join(errs[:6]))
        hdr = json.loads((POSTS / f"{row['slug']}.html").read_text().splitlines()[0])
        if DRY:
            log(f"[dry] gates passed for {row['slug']}; rolling back"); rollback(row["slug"]); return
        if PREPARE:
            br = ("draft-" + "-".join(w for w in row["slug"].split("-") if w not in ("how", "to", "get", "rid", "of", "a", "the", "do", "what", "is", "are")))[:28].rstrip("-")
            pv = deploy(row["slug"], "--branch", br)   # a preview alias per draft, never production; built from a clean export
            preview = f"https://{br}.djpest.pages.dev/blog/{row['slug']}"
            # Sanity Sam reads the preview like a reader BEFORE anything is parked (Dane 29 Sep: previews checked before publish, not only after)
            import sense as sensemod
            v = sensemod.run(row["slug"], preview) if pv.returncode == 0 else {"verdict": "FIX", "issues": ["preview deploy failed"], "fixes": []}
            log(f"sense: {v.get('verdict')} {' | '.join(v.get('issues', [])[:4])}")
            if v.get("verdict") != "PASS":
                repair_post(row, [f"{i} -> {f}" for i, f in zip(v.get("issues", []), v.get("fixes", []) + [""] * 9)] or v.get("issues", []))
                errs = gates(row)
                if errs: raise Fail("sense", "after the common-sense repair the gates failed: " + " | ".join(errs[:4]))
                hdr = json.loads((POSTS / f"{row['slug']}.html").read_text().splitlines()[0])
                pv = deploy(row["slug"], "--branch", br)
                v = sensemod.run(row["slug"], preview) if pv.returncode == 0 else v
                log(f"sense (2nd): {v.get('verdict')} {' | '.join(v.get('issues', [])[:4])}")
                if v.get("verdict") != "PASS": raise Fail("sense", "held by the common-sense check: " + " | ".join(v.get("issues", [])[:4]) + f" (sheet: {v.get('sheet')})")
            manifest = park(row); rollback(row["slug"])
            lost = [m for m in manifest if not (READY / row["slug"] / m).exists()]
            if lost or not (READY / row["slug"] / "manifest.json").exists():
                raise Fail("prepare", f"parked draft missing after rollback: {lost[:4]}")
            set_status(row, f"ready {dt.date.today().isoformat()}")
            sh(["git", "add", "blog/_drafts"]); sh(["git", "commit", "-q", "-m", f"Blog draft ready: {row['slug']}\n\nCo-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"])
            sh(["git", "pull", "-q", "--rebase"]); sh(["git", "push", "-q", "origin", "main"])
            signal("notable", f"Blog draft ready: {hdr['title']}", f"Passed every gate. Preview: {preview} ({'ok' if pv.returncode == 0 else 'preview deploy failed'}). Publishes at the next Mon/Thu 06:00 run unless you say hold.", preview)
            st["fails"] = 0; st["last_ok"] = f"ready:{row['slug']}"; put_state(st)
            log(f"READY {row['slug']} ({len(manifest)} files parked) preview {preview}"); return
        if HOLD.exists():
            rollback(row["slug"]); signal("notable", f"Blog publish HELD: {row['slug']}", f"blog/_drafts/HOLD is present ({HOLD.read_text().strip()[:120] or 'no reason given'}). Remove the file to publish at the next slot.")
            log("HELD: blog/_drafts/HOLD present"); return
        d = deploy(row["slug"], "--prod")
        if d.returncode: raise Fail("deploy", (d.stdout + d.stderr)[-400:])
        url, verdict = verify(row["slug"], hdr["title"], hdr["img"])
        if not verdict.upper().startswith("PASS"):
            # Dane 28 Sep: a bad publish is blocked and fixed, never left live. One repair pass, then take it down.
            log(f"visual check failed on the live post; repairing: {verdict}")
            repair_post(row, [f"the published page failed a visual check: {verdict}"])
            errs = gates(row)
            if not errs:
                hdr = json.loads((POSTS / f"{row['slug']}.html").read_text().splitlines()[0])
                d = deploy(row["slug"], "--prod")
                if d.returncode == 0: url, verdict = verify(row["slug"], hdr["title"], hdr["img"])
            if errs or not verdict.upper().startswith("PASS"):
                rollback(row["slug"]); deploy(row["slug"], "--prod")        # take the post down again
                st["fails"] = st.get("fails", 0) + 1                                 # a pulled post always pages Dane
                raise Fail("verify", f"published post failed the visual check twice and was taken down: {verdict} {' | '.join(errs[:3])}")
        books(row, hdr["title"])
        import shutil
        if (WIP / row["slug"]).exists():
            pub = DRAFTS / "published" / row["slug"]; shutil.rmtree(pub, ignore_errors=True); pub.parent.mkdir(exist_ok=True); shutil.move(str(WIP / row["slug"]), str(pub))
        st["fails"] = 0; st["last_ok"] = row["slug"]; put_state(st)
        signal("notable", f"Blog published: {hdr['title']}", f"Visual check: {verdict}. Screens: blog/_drafts/screens/{row['slug']}-*.png", url)
        log(f"PUBLISHED {url}")
    except Fail as e:
        if row and e.stage in ("write", "gates", "sense", "brief", "prepare"): fail_wip(row["slug"]); rollback(row["slug"])
        st["fails"] = st.get("fails", 0) + 1; st["last_fail"] = str(e); put_state(st)
        sev = "urgent" if st["fails"] >= 2 else "notable"
        signal(sev, f"Blog run FAILED at {e.stage}" + (f" ({row['slug']})" if row else ""), e.why)
        log(f"FAILED {e}"); EXIT[0] = 1
    except Exception as e:
        if row: rollback(row["slug"])
        st["fails"] = st.get("fails", 0) + 1; put_state(st)
        signal("urgent" if st["fails"] >= 2 else "notable", "Blog run crashed", f"{type(e).__name__}: {e}")
        log(f"CRASH {type(e).__name__}: {e}"); EXIT[0] = 1
    finally:
        log("=== blog run end ===")

if __name__ == "__main__":
    main(); sys.exit(EXIT[0])
