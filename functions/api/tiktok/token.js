// Hands the stored token to the Mac (shared-secret header). The Mac refreshes it from then on.
export async function onRequestGet({ request, env }) {
  if (!env.SOCIAL_READ_KEY || request.headers.get("x-social-key") !== env.SOCIAL_READ_KEY) return new Response("Not found", { status: 404 });
  return new Response((await env.SOCIAL.get("tiktok_token")) || "{}", { headers: { "content-type": "application/json", "cache-control": "no-store" } });
}
