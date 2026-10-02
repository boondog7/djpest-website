// Posts one approved DJ Pest video by FILE_UPLOAD (the file is on our own site, so no domain verification is needed).
import { ok, json, tt, access } from "./_lib.js";
export async function onRequestPost({ request, env }) {
  if (!ok(env, request)) return new Response("Not found", { status: 404 });
  const b = await request.json();
  if (!/^[\w-]+$/.test(b.job || "")) return json({ error: "bad job" }, 400);
  if (!b.privacy_level) return json({ error: "Choose who can see this post" }, 400);
  const vid = await fetch(new URL(`/assets/tt/${b.job}.mp4`, request.url));
  if (!vid.ok) return json({ error: "video not found" }, 404);
  const bytes = await vid.arrayBuffer(), size = bytes.byteLength;
  const init = await tt(env, "/post/publish/video/init/", {
    post_info: { title: (b.title || "").slice(0, 2200), privacy_level: b.privacy_level, disable_comment: !b.allow_comment, disable_duet: !b.allow_duet,
      disable_stitch: !b.allow_stitch, brand_content_toggle: !!b.branded_content, brand_organic_toggle: !!b.your_brand, is_aigc: !!b.is_aigc },
    source_info: { source: "FILE_UPLOAD", video_size: size, chunk_size: size, total_chunk_count: 1 } });
  if (!init.data?.upload_url) return json(init, 502);
  const up = await fetch(init.data.upload_url, { method: "PUT", headers: { "Content-Type": "video/mp4", "Content-Length": String(size), "Content-Range": `bytes 0-${size - 1}/${size}` }, body: bytes });
  return json({ publish_id: init.data.publish_id, upload_status: up.status });
}
