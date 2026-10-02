// TikTok redirects here after Dane approves. Exchange the code server-side and keep the token in KV (never shown in the page).
export async function onRequestGet({ request, env }) {
  const url = new URL(request.url), code = url.searchParams.get("code"), state = url.searchParams.get("state");
  const page = (msg) => new Response(`<!doctype html><meta name=viewport content="width=device-width"><body style="font:18px system-ui;padding:32px;background:#fff;color:#111"><h2>DJ Pest</h2><p>${msg}</p></body>`,
    { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" } });
  if (!code || !state || !(await env.SOCIAL.get(`tiktok_state:${state}`))) return page("This link has expired. Ask Claude for a fresh one.");
  await env.SOCIAL.delete(`tiktok_state:${state}`);
  const r = await fetch("https://open.tiktokapis.com/v2/oauth/token/", {
    method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ client_key: env.TIKTOK_CLIENT_KEY, client_secret: env.TIKTOK_CLIENT_SECRET, code,
      grant_type: "authorization_code", redirect_uri: "https://djpest.com.au/api/tiktok/callback" }),
  });
  const tok = await r.json();
  if (!tok.access_token) return page("TikTok didn't return access (" + (tok.error || r.status) + "). Tell Claude.");
  tok.saved_at = Date.now();
  await env.SOCIAL.put("tiktok_live", JSON.stringify(tok));
  return page("✅ TikTok connected. You can close this page.");
}
