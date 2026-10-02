// One keeper of the TikTok login: the Mac asks here for a current access token instead of refreshing on its own.
import { json, access } from "./_lib.js";
export async function onRequestGet({ request, env }) {
  if (!env.SOCIAL_READ_KEY || request.headers.get("x-social-key") !== env.SOCIAL_READ_KEY) return new Response("Not found", { status: 404 });
  try { return json({ access_token: await access(env) }); } catch (e) { return json({ error: String(e.message) }, 500); }
}
