# djpest.com.au is returning HTTP 522 — fix steps

> **Status (as of audit):** site is returning Cloudflare 522 "origin timeout". DNS resolves correctly to Cloudflare IPs (104.21.96.52, 172.67.173.71), which means **DNS is not the problem** — Cloudflare's edge can't reach the origin (Pages project).
>
> Most likely causes, in order: (1) the Pages project was unpublished/deleted, (2) the custom domain `djpest.com.au` got detached from the Pages project, (3) the apex/www was accidentally pointed at the n8n A record (143.198.195.54) which doesn't serve HTTP.

## Fix procedure

### Step 1 — Open Cloudflare Pages
1. Go to https://dash.cloudflare.com
2. Workers & Pages → **Pages** → check if `djpest-website` (or whatever the project is named) still exists
3. If the project is missing: see *Recreate the project* below
4. If the project exists: open it, click **Deployments** — confirm the latest deployment is "Production" and shows the recent commit (`124b043 — Rewrite licensing copy + vary Joondalup CTA text`)

### Step 2 — Check custom domain binding
1. Inside the Pages project → **Custom domains** tab
2. You should see **two entries**:
   - `djpest.com.au` — status "Active"
   - `www.djpest.com.au` — status "Active"
3. If either is missing or shows "Verification failed" or "Pending":
   - Click **Set up a custom domain** → enter `djpest.com.au`
   - Cloudflare auto-creates the right DNS record (CNAME to `<project>.pages.dev`)
   - Repeat for `www.djpest.com.au`

### Step 3 — Verify DNS in the Cloudflare DNS dashboard
Open the `djpest.com.au` zone → DNS → Records. You should see:

| Type | Name | Content | Proxy |
|---|---|---|---|
| CNAME | `djpest.com.au` (or `@`) | `<project>.pages.dev` | Proxied (orange) |
| CNAME | `www` | `<project>.pages.dev` | Proxied (orange) |
| A | `n8n` | `143.198.195.54` | **DNS only (grey)** |

**Critical:** the `n8n` record MUST stay grey-clouded (DNS only). The apex/www MUST stay orange-clouded (Proxied).

### Step 4 — If neither apex nor www points to Pages
Cloudflare won't let you put an A record on the apex with a CNAME alongside, so they use CNAME flattening. If you see an A record at the apex pointing to the wrong IP (like 143.198.195.54), **delete it** and re-add via Pages custom-domain wizard which sets up flattening correctly.

### Step 5 — Verify with curl
```bash
curl -I https://djpest.com.au
curl -I https://www.djpest.com.au
```

You should see `HTTP/2 200` (or 301 from apex → www if redirect is set up). NOT 522.

## Recreate the project (only if Pages project was deleted)

```bash
cd ~/jaystack/djpest
git status   # confirm clean
git push origin main   # ensures GitHub has latest
```

Then in Cloudflare dashboard:
1. Workers & Pages → Pages → **Create a project** → Connect to Git
2. Pick the GitHub account `boondog7` → repo `djpest-website`
3. Production branch: `main`
4. Build command: *(blank)*
5. Build output directory: *(blank)* (static site)
6. Save and Deploy

After first deploy, attach custom domains as in Step 2.

## Quick health-check command to run after fix

```bash
bash ~/.claude/skills/seo-site-audit/audit.sh ~/jaystack/djpest djpest.com.au
```

Reports a 200 on every sitemap URL with security headers present = green light.

## Why this matters

Until 522 is fixed:
- No leads come in through the contact form (Pages Function isn't reachable)
- Google ranks the site as down — repeat outages = ranking damage
- The Cloudflare Web Analytics token in the new pages won't collect data (beacon can't fire)
- AI crawlers (GPTBot, PerplexityBot, ClaudeBot) see 522 and may downrank the source

This is **task #0** before any other audit item matters.
