# Blog post source files

`content-pipeline` writes one file per post here: `posts/<slug>.html`

Format:
```
{"slug": "...", "title": "...", "desc": "...", "img": "/assets/img/blog-....jpg", "alt": "...", "date": "2026-09-29", "read": "9 minutes", "service": "/ant-control-perth", "service_label": "Ant management Perth"}
---
Lede paragraph (plain text, one paragraph).
---
<h2>Article HTML…</h2>
```
Then `python3 build/build.py` and `./deploy.sh --prod`. Images go in `assets/img/`. Never hand-edit root HTML.
