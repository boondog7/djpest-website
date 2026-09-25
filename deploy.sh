#!/usr/bin/env bash
# Build + stage + deploy DJ Pest to Cloudflare Pages (project: djpest).
#   ./deploy.sh            -> preview deploy (branch "preview")  https://preview.djpest.pages.dev
#   ./deploy.sh --prod     -> production deploy (branch "main")   https://djpest.pages.dev + custom domain
#   ./deploy.sh --branch draft-x -> named preview (blog drafts)   https://draft-x.djpest.pages.dev
set -euo pipefail
# One deploy at a time (blog desk, review sync, manual): re-exec under a shared lock, wait up to 10 min.
if [ -z "${DEPLOY_LOCKED:-}" ]; then export DEPLOY_LOCKED=1; exec /usr/bin/lockf -k -t 600 "$(dirname "$0")/.deploy.lock" "$0" "$@"; fi
cd "$(dirname "$0")"
source ~/.config/jaystack/cloudflare.env

# Pin the interpreter: launchd/cron PATH has no Homebrew, so bare python3 = macOS 3.9 and the build breaks.
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
PY=/opt/homebrew/bin/python3
"$PY" -c 'import sys; assert sys.version_info >= (3,12), sys.version' || { echo "deploy.sh: need Python 3.12+ at $PY" >&2; exit 1; }

"$PY" build/build.py   # exits non-zero on compliance hits

DIST=dist; rm -rf "$DIST"; mkdir -p "$DIST"
rsync -a --delete \
  --exclude 'build/' --exclude 'reviews/' --exclude 'seo/' --exclude 'samples/' --exclude '_archive/' --exclude 'dist/' --exclude '.git/' \
  --exclude '*.md' --exclude 'deploy.sh' --exclude 'blog/_drafts/' --exclude 'assets/img/higgsfield/' \
  --exclude 'assets/img/hero-a.png' --exclude 'assets/img/hero-b.png' --exclude 'assets/email-signature-logo.png' \
  --exclude 'node_modules/' --exclude '.DS_Store' --exclude 'wrangler.toml' \
  ./ "$DIST/"

BRANCH=preview; [[ "${1:-}" == "--prod" ]] && BRANCH=main
[[ "${1:-}" == "--branch" && -n "${2:-}" ]] && BRANCH="$2"
wrangler pages deploy "$DIST" --project-name djpest --branch "$BRANCH" --commit-dirty=true
echo "deployed branch=$BRANCH"
[[ "$BRANCH" == "main" ]] && { sleep 20; "$PY" build/indexnow.py || true; }
