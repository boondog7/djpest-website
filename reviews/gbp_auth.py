#!/usr/bin/env python3
"""One-time: connect the review sync to the Google Business Profile API.
Prereqs (Dane, once):
  1. Request GBP API access for the GCP project in ~/.config/jaystack/google-cloud.env:
     https://support.google.com/business/contact/api_default  (approval: days to weeks)
  2. In that project enable: My Business Account Management API + Google My Business API (v4 reviews).
  3. Create an OAuth client (type: Desktop app). Download nothing; copy the client ID + secret.
Then:  python3 gbp_auth.py <client_id> <client_secret>
A browser opens; sign in as ops@djpest.com.au (the profile owner) and allow. The refresh token is saved to
~/.config/jaystack/gbp-oauth.json (chmod 600) and sync.py switches to the API automatically.
"""
import sys, json, pathlib, urllib.parse, urllib.request, http.server, webbrowser, threading, os
if len(sys.argv) != 3: sys.exit(__doc__)
cid, sec = sys.argv[1], sys.argv[2]; PORT = 8765; RED = f"http://127.0.0.1:{PORT}/"
code = {}
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query); code.update(q)
        self.send_response(200); self.end_headers(); self.wfile.write(b"DJ Pest review sync connected. You can close this tab.")
    def log_message(self, *a): pass
srv = http.server.HTTPServer(("127.0.0.1", PORT), H); threading.Thread(target=srv.handle_request).start()
webbrowser.open("https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
    "client_id": cid, "redirect_uri": RED, "response_type": "code", "access_type": "offline", "prompt": "consent",
    "scope": "https://www.googleapis.com/auth/business.manage", "login_hint": "ops@djpest.com.au"}))
print("waiting for Google sign-in in the browser…")
while "code" not in code and "error" not in code: pass
if "error" in code: sys.exit(f"denied: {code['error']}")
tok = json.load(urllib.request.urlopen("https://oauth2.googleapis.com/token", urllib.parse.urlencode({
    "code": code["code"][0], "client_id": cid, "client_secret": sec, "redirect_uri": RED, "grant_type": "authorization_code"}).encode()))
out = pathlib.Path.home() / ".config/jaystack/gbp-oauth.json"
out.write_text(json.dumps({"client_id": cid, "client_secret": sec, "refresh_token": tok["refresh_token"]}, indent=2)); os.chmod(out, 0o600)
print("saved", out, "- run: python3 sync.py --dry")
