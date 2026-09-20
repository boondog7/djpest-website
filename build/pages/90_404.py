"""404 page (Cloudflare Pages serves /404.html for unknown routes)."""

def pages(c):
    body = c["section"](
        c["eyebrow"]("Page not found") +
        '<h1>That page has gone to ground.</h1>'
        '<p class="lead">The link may be old or mistyped. Try one of these, or call us and we\'ll sort it on the phone.</p>'
        '<div class="grid grid-3" style="margin-top:2rem">'
        + c["card"]("Services", "Termites, general pest, ants, cockroaches, rodents, spiders.", "/services")
        + c["card"]("Pricing guide", "Typical Perth ranges, and what moves the price.", "/pest-control-prices-perth")
        + c["card"]("What's my pest?", "Match what you saw to the right treatment.", "/whats-my-pest")
        + '</div><p style="margin-top:2rem">' + c["btn_call"]() + '</p>')
    return [{"path": "/404", "title": "Page not found | DJ Pest", "desc": "The page you were after is not here. Find DJ Pest services, pricing and contact details.", "body": body, "noindex": True}]
