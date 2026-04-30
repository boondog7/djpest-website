# DJ Pest Website — Deployment Guide

## Current Status

✅ **Built & ready for Cloudflare Pages**

- Single HTML file: `index.html`
- Video: Cloudflare Stream (already embedded)
- Responsive design (mobile-first)
- No build step required

## Before Going Live

1. **Replace placeholder contact details:**
   - Phone: `0861 234 567` → real number
   - Email: `hello@djpest.com.au` → confirmed address
   - Social links: Facebook & Instagram URLs (or remove if not ready)

2. **Update the video URL if needed:**
   - Current: `https://customer-vse5dkzg7f3e81ww.cloudflarestream.com/c881126506c22b338101b9ca6db297d3/downloads/default.mp4`
   - Get public URLs from your Cloudflare Stream dashboard (Videos → Copy public link)

## Deploy to Cloudflare Pages

### Option A: Git + Auto-Deploy (Recommended)

Already wired up. The git remote is set to `git@github.com:boondog7/djpest-website.git` (Dane's GitHub). To push:
```bash
git push origin main
```

In Cloudflare Dashboard (one-time setup, only if not already connected):
- Pages → Create project → Connect to Git
- Select repo: `djpest-website`
- Build command: *(leave blank)*
- Build output directory: *(leave blank)*
- Deploy!

### Option B: Direct Upload (Fastest)

```bash
npm install -g wrangler
wrangler pages deploy .
```

## DNS Setup

Once deployed to Cloudflare Pages:

1. Get your Pages URL (e.g., `djpest-website.pages.dev`)
2. Point DNS record to Cloudflare:
   - `djpest.com.au` A record → `192.0.2.1` (Cloudflare IP, they'll provide)
   - Or CNAME → `djpest-website.pages.dev`

## Next Steps

- [ ] Replace contact details with real numbers
- [ ] Confirm `hello@djpest.com.au` domain is live
- [ ] Get Facebook & Instagram URLs
- [ ] Set up DNS
- [ ] Deploy to live domain
- [ ] Test on mobile
- [ ] Add Google Business Profile link
- [ ] Set up basic analytics (optional)

## Files in Repo

```
djpest/
├── index.html          # Single-page site
├── .gitignore
└── DEPLOY.md           # This file
```

---

**Questions?** Ask DJ or Simsy about Cloudflare setup.
