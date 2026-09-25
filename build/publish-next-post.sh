#!/bin/bash
# DJ Pest Blog desk (Head of Blog). launchd:
#   com.jaystack.djpest-blog          Mon/Thu 06:00  -> publish (a ready draft first; otherwise write + gate + publish)
#   com.jaystack.djpest-blog-prepare  Sun/Wed 18:00  -> prepare (write + gate + preview; publishes next morning)
# All model calls go through ~/business/djpest/hq/bin/claude-lean (API key, metered, never the Max plan).
# The previous 80-turn agentic version is kept as publish-next-post.sh.old-agentic for reference.
set -u
export PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin
cd "$HOME/jaystack/djpest" || exit 1
exec /opt/homebrew/bin/python3 build/blog/publish.py "$@"
