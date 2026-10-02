// GET: Mac collects a fresh login. PUT: Mac shares its refreshed token so the posting page can use it (both secret-key only).
import { json } from "./_lib.js";
export async function onRequest({ request, env }) {
  if (!env.SOCIAL_READ_KEY || request.headers.get("x-social-key") !== env.SOCIAL_READ_KEY) return new Response("Not found", { status: 404 });
  if (request.method === "PUT") { await env.SOCIAL.put("tiktok_live", await request.text()); return json({ ok: true }); }
  return new Response((await env.SOCIAL.get("tiktok_token")) || "{}", { headers: { "content-type": "application/json", "cache-control": "no-store" } });
}
