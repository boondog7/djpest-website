"""/reviews: every Google review, unedited, with the true overall rating."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import reviews_lib as RV

def pages(c):
    esc = c["esc"]; d = RV.load()
    avg, n = RV.stats(d); allr = RV.counted(d); wall = RV.shown(d)
    url = d["profile"].get("public_url", ""); write = d["profile"].get("write_review_url", "")

    if n:
        dist = "".join(
            f'<div class="rv-bar"><span>{s}★</span><i style="--w:{(sum(1 for r in allr if r["rating"] == s) / len(allr) * 100) if allr else 0:.0f}%"></i>'
            f'<span>{sum(1 for r in allr if r["rating"] == s)}</span></div>' for s in (5, 4, 3, 2, 1))
        score = (f'<div class="rv-score"><div class="rv-score-big">{avg:.1f}</div>{RV.stars(avg)}'
                 f'<p>{n} Google review{"s" if n != 1 else ""}</p></div><div class="rv-dist" aria-label="Rating breakdown">{dist}</div>')
    else:
        score = '<div class="rv-score"><p>Our first reviews are coming in now.</p></div>'

    svcs = sorted({s for r in wall for s in r.get("services", [])})
    chips = ""
    if len(svcs) > 1:
        chips = ('<div class="rv-chips" role="group" aria-label="Filter reviews"><button type="button" aria-pressed="true" data-f="">All</button>'
                 + "".join(f'<button type="button" aria-pressed="false" data-f="{s}">{esc(RV.SERVICE_LABEL.get(s, s))}</button>' for s in svcs) + "</div>")
    cards = "".join(f'<div class="rv-cell" data-s="{" ".join(r.get("services", []))}">{RV.review_card(r)}</div>' for r in wall)
    wall_html = (f'{chips}<div class="rv-wall">{cards}</div>' if wall else
                 '<div class="card rv-empty"><h3>Reviews appear here as customers leave them.</h3>'
                 '<p>Every review we receive on Google is shown on this page, unedited, good or bad.</p></div>')

    ctas = ""
    if url: ctas += f'<a class="btn btn-ghost" href="{esc(url)}" rel="noopener" target="_blank">See us on Google {c["icon"]("arrow")}</a>'
    if write: ctas += f'<a class="btn btn-ghost" href="{esc(write)}" rel="noopener" target="_blank">Had a job done? Leave a review</a>'

    body = f"""<section class="hero rv-hero"><div class="wrap">
<div>{c['eyebrow']("Customer reviews · Google")}
<h1>Judge us on what our customers <em class="red">say</em>.</h1>
<p class="lead">Every review we receive on Google is on this page. We don't edit them, we don't pick the good ones, and we reply to all of them, including the ones that tell us where we can do better.</p>
<div class="actions">{c['btn_call']()}{ctas}</div></div>
<div class="rv-scorecard">{score}</div>
</div></section>
<section class="ledger"><div class="wrap">{wall_html}
<p class="rv-note mono">Reviews are pulled from our Google Business Profile. Names are shortened to first name and initial for privacy. We never pay or reward anyone for a review, and every customer is asked the same way.</p>
</div></section>
<script>(function(){{var b=document.querySelectorAll('.rv-chips button');b.forEach(function(x){{x.addEventListener('click',function(){{var f=x.dataset.f;b.forEach(function(y){{y.setAttribute('aria-pressed',y===x)}});document.querySelectorAll('.rv-cell').forEach(function(c){{c.hidden=f&&(' '+c.dataset.s+' ').indexOf(' '+f+' ')<0}})}})}})}})();</script>
{c['quote_block']("Want the same result at your place?")}"""
    return [{"path": "/reviews", "title": "DJ Pest Reviews | Google Reviews from Perth's Northern Suburbs",
             "desc": (f"{avg:.1f} stars from {n} Google reviews. " if n >= RV.MIN_BADGE else "") + "Every DJ Pest Google review, unedited, with our replies. Pest management in Perth's northern suburbs.",
             "body": body, "crumbs": [("Reviews", None)], "noindex": not wall}]
