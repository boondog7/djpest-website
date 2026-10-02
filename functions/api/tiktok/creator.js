import { ok, json, tt } from "./_lib.js";
export async function onRequestGet({ request, env }) {
  if (!ok(env, request)) return new Response("Not found", { status: 404 });
  try { return json(await tt(env, "/post/publish/creator_info/query/")); } catch (e) { return json({ error: { code: String(e.message) } }, 500); }
}
