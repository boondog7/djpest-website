#!/usr/bin/env python3
"""Submit every URL in the just-deployed sitemap to IndexNow (Bing + partner engines). Runs after each prod deploy.
usage: indexnow.py [url ...]   (no args = all URLs in ./sitemap.xml)"""
import json, os, re, sys, urllib.request, urllib.error
key = open(os.path.expanduser("~/.config/jaystack/indexnow-djpest.env")).read().split("=", 1)[1].strip()
host = "djpest.com.au"
local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sitemap.xml")
urls = sys.argv[1:] or re.findall(r"<loc>(.*?)</loc>", open(local).read())
body = json.dumps({"host": host, "key": key, "keyLocation": f"https://{host}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/IndexNow", data=body,
      headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "djpest-indexnow/1.0"})
try:
    r = urllib.request.urlopen(req, timeout=30); print(f"IndexNow {r.status}: {len(urls)} URLs")
except urllib.error.HTTPError as e:
    print(f"IndexNow {e.code}: {e.read().decode()[:200]}"); sys.exit(1)
