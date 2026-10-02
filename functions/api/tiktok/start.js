// Starts TikTok Login Kit for DJ Pest's own account. Guarded so nobody else can overwrite the stored token.
export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  if (!env.SOCIAL_READ_KEY || url.searchParams.get("k") !== env.SOCIAL_READ_KEY) return new Response("Not found", { status: 404 });
  const state = crypto.randomUUID();
  await env.SOCIAL.put(`tiktok_state:${state}`, "1", { expirationTtl: 600 });
  const q = new URLSearchParams({
    client_key: env.TIKTOK_CLIENT_KEY, response_type: "code", state,
    scope: (url.searchParams.get("s") || "user.info.basic,user.info.profile,user.info.stats,video.list,video.upload,video.publish").replace(/[^a-z.,_]/g, ""),
    redirect_uri: "https://djpest.com.au/api/tiktok/callback",
  });
  return Response.redirect(`https://www.tiktok.com/v2/auth/authorize/?${q}`, 302);
}
