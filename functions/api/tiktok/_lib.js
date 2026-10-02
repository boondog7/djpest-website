export const API = "https://open.tiktokapis.com/v2";
export const ok = (env, req) => env.SOCIAL_READ_KEY && (new URL(req.url).searchParams.get("k") === env.SOCIAL_READ_KEY || req.headers.get("x-social-key") === env.SOCIAL_READ_KEY);
export const json = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { "content-type": "application/json", "cache-control": "no-store" } });
export async function access(env) {
  let t = JSON.parse((await env.SOCIAL.get("tiktok_live")) || "{}");
  if (!t.refresh_token) throw new Error("not connected");
  if (Date.now() - t.saved_at > (t.expires_in - 600) * 1000) {
    const r = await fetch(`${API}/oauth/token/`, { method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ client_key: env.TIKTOK_CLIENT_KEY, client_secret: env.TIKTOK_CLIENT_SECRET, grant_type: "refresh_token", refresh_token: t.refresh_token }) });
    const n = await r.json(); if (!n.access_token) throw new Error("refresh failed");
    t = { ...n, saved_at: Date.now() }; await env.SOCIAL.put("tiktok_live", JSON.stringify(t));
  }
  return t.access_token;
}
export async function tt(env, path, body) {
  const r = await fetch(`${API}${path}`, { method: "POST", headers: { Authorization: `Bearer ${await access(env)}`, "content-type": "application/json; charset=UTF-8" }, body: JSON.stringify(body || {}) });
  return r.json();
}
