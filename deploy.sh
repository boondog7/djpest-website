#!/usr/bin/env bash
# Build + stage + deploy DJ Pest to Cloudflare Pages (project: djpest).
#   ./deploy.sh            -> preview deploy (branch "preview")  https://preview.djpest.pages.dev
#   ./deploy.sh --prod     -> production deploy (branch "main")   https://djpest.pages.dev + custom domain
set -euo pipefail
cd "$(dirname "$0")"
source ~/.config/jaystack/cloudflare.env

python3 build/build.py   # exits non-zero on compliance hits

DIST=dist; rm -rf "$DIST"; mkdir -p "$DIST"
rsync -a --delete \
  --exclude 'build/' --exclude 'seo/' --exclude 'samples/' --exclude '_archive/' --exclude 'dist/' --exclude '.git/' \
  --exclude '*.md' --exclude 'deploy.sh' --exclude 'blog/_drafts/' --exclude 'assets/img/higgsfield/' \
  --exclude 'assets/img/hero-a.png' --exclude 'assets/img/hero-b.png' --exclude 'assets/email-signature-logo.png' \
  --exclude 'node_modules/' --exclude '.DS_Store' --exclude 'wrangler.toml' \
  ./ "$DIST/"

BRANCH=preview; [[ "${1:-}" == "--prod" ]] && BRANCH=main
wrangler pages deploy "$DIST" --project-name djpest --branch "$BRANCH" --commit-dirty=true
echo "deployed branch=$BRANCH"
[[ "$BRANCH" == "main" ]] && { sleep 20; python3 build/indexnow.py || true; }
