import { ok, json, tt } from "./_lib.js";
export async function onRequestGet({ request, env }) {
  if (!ok(env, request)) return new Response("Not found", { status: 404 });
  return json(await tt(env, "/post/publish/status/fetch/", { publish_id: new URL(request.url).searchParams.get("id") }));
}
