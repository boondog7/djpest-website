#!/usr/bin/env python3
"""Submit every URL in the live sitemap to IndexNow (Bing, plus partner engines). Runs after each prod deploy."""
import json, os, re, sys, urllib.request
key = open(os.path.expanduser("~/.config/jaystack/indexnow-djpest.env")).read().split("=",1)[1].strip()
host = "djpest.com.au"
sm = urllib.request.urlopen(f"https://{host}/sitemap.xml").read().decode()
urls = re.findall(r"<loc>(.*?)</loc>", sm)
if len(sys.argv) > 1: urls = sys.argv[1:]
body = json.dumps({"host": host, "key": key, "keyLocation": f"https://{host}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/IndexNow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req); print(f"IndexNow {r.status}: {len(urls)} URLs")
except urllib.error.HTTPError as e: print(f"IndexNow {e.code}: {e.read().decode()[:200]}"); sys.exit(1)
