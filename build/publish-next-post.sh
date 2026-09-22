#!/bin/bash
# Publishes the next queued DJ Pest blog post via headless Claude Code.
# Scheduled by launchd (com.jaystack.djpest-blog) Mon/Wed/Fri 06:00. Run by hand: bash build/publish-next-post.sh
set -u
export PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
# launchd shells don't source .zshrc; pull the keys the pipeline needs
eval "$(grep -E '^export (PEXELS_API_KEY|CLOUDFLARE_API_TOKEN|CLOUDFLARE_ACCOUNT_ID)=' "$HOME/.zshrc")" 2>/dev/null
cd "$HOME/jaystack/djpest" || exit 1
LOG="$HOME/jaystack/djpest/build/publish.log"
echo "=== $(date '+%Y-%m-%d %H:%M') start ===" >> "$LOG"
if [ -n "$(git status --porcelain | grep -v '^??')" ]; then
  echo "dirty working tree, aborting" >> "$LOG"; exit 1
fi
claude -p \
  --permission-mode acceptEdits \
  --allowedTools "Bash(python3:*),Bash(./deploy.sh:*),Bash(git:*),Bash(curl:*),Bash(cwebp:*),Bash(node:*),Bash(ls:*),Bash(grep:*),Read,Write,Edit,WebSearch,WebFetch,Skill" \
  --max-turns 80 \
  "Use the content-pipeline skill to publish exactly ONE blog post: the first row in ~/jaystack/djpest/blog/_drafts/QUEUE.md with Status queued. Follow every step in the skill: read the voice files, read the bundle(s) named in the row, research, apply the compliance overrides, fetch two Pexels images, write build/posts/<slug>.html, run python3 build/build.py until it prints 'compliance scan: clean' (fix hits in the post file only), deploy with ./deploy.sh --prod, screenshot-verify the live URL with the Playwright install in ~/jaystack/infrastructure/devicecheck, then update QUEUE.md, the bundle frontmatter and PUBLISH-LOG.md, commit with message 'Publish blog: <slug>' and push. If something fails that you cannot fix, restore a clean tree (git checkout -- . ; git clean -fd build/posts assets/img) and stop. End with exactly one line: PUBLISHED <url> or FAILED <reason>." \
  >> "$LOG" 2>&1
echo "=== $(date '+%Y-%m-%d %H:%M') end ===" >> "$LOG"
tail -1 "$LOG"
