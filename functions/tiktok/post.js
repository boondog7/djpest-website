// DJ Pest → TikTok posting page. Follows TikTok's Content Sharing Guidelines: preview, creator identity, privacy with no default,
// interaction toggles respecting creator settings, commercial content disclosure, AI label, consent text, post status.
export async function onRequestGet({ request, env }) {
  const u = new URL(request.url), k = u.searchParams.get("k"), job = u.searchParams.get("job") || "";
  if (!env.SOCIAL_READ_KEY || k !== env.SOCIAL_READ_KEY || !/^[\w-]+$/.test(job)) return new Response("Not found", { status: 404 });
  const meta = await fetch(new URL(`/assets/tt/${job}.json`, request.url)).then(r => r.ok ? r.json() : {}).catch(() => ({}));
  const esc = s => String(s || "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Post to TikTok · DJ Pest</title><meta name="robots" content="noindex">
<style>
:root{--bg:#fff;--fg:#111;--mut:#666;--line:#e3e3e3;--acc:#fe2c55;--card:#f7f7f7}
@media (prefers-color-scheme:dark){:root{--bg:#111;--fg:#f2f2f2;--mut:#aaa;--line:#333;--card:#1b1b1b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,-apple-system,sans-serif}
main{max-width:480px;margin:0 auto;padding:16px}h1{font-size:20px;margin:4px 0 14px}
.who{display:flex;gap:10px;align-items:center;margin-bottom:12px}.who img{width:40px;height:40px;border-radius:50%;background:var(--card)}
video{width:100%;max-height:60vh;border-radius:12px;background:#000}label{display:block;font-weight:600;margin:16px 0 6px}
textarea,select{width:100%;font:inherit;padding:10px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--fg)}
.row{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.row small{display:block;color:var(--mut);font-weight:400}.sub{padding-left:14px}.hint{color:var(--mut);font-size:14px}
#vids div{display:flex;gap:10px;align-items:center;padding:6px 0;border-bottom:1px solid var(--line);font-size:14px}#vids img{width:44px;height:58px;object-fit:cover;border-radius:6px}summary{cursor:pointer;margin:8px 0}
.warn{background:var(--card);border-radius:10px;padding:10px;font-size:14px;margin-top:10px}
button{width:100%;margin:18px 0 8px;padding:14px;border:0;border-radius:10px;background:var(--acc);color:#fff;font:600 17px system-ui}
button:disabled{opacity:.45}a{color:var(--acc)}#msg{min-height:1.5em}
</style></head><body><main>
<h1>Post to TikTok</h1>
<div class="who"><img id="av" alt=""><div><b id="nick">Loading account…</b><div class="hint">Posting to this TikTok account</div></div></div>
<details id="stats" open><summary><b>Your account</b></summary><p class="hint" id="acct">Loading stats…</p><div id="vids"></div></details>
<h2 style="font-size:17px;margin:18px 0 8px">New post</h2>
<video src="/assets/tt/${job}.mp4" poster="/assets/tt/${job}.jpg" controls playsinline preload="metadata"></video>
<label for="cap">Caption</label><textarea id="cap" rows="5" maxlength="2200">${esc(meta.caption)}</textarea>
<label for="priv">Who can view this video</label>
<select id="priv"><option value="" selected disabled>Choose who can see this post</option></select>
<div class="hint" id="privhint"></div>
<label>Allow users to</label>
<div class="row"><span>Comment</span><input type="checkbox" id="c_comment"></div>
<div class="row"><span>Duet</span><input type="checkbox" id="c_duet"></div>
<div class="row"><span>Stitch</span><input type="checkbox" id="c_stitch"></div>
<div class="row"><span>AI-generated content<small>Label this video as AI-generated</small></span><input type="checkbox" id="aigc" ${meta.is_aigc ? "checked" : ""}></div>
<div class="row"><span>Disclose video content<small>Turn on to show this post promotes a brand, product or service</small></span><input type="checkbox" id="cc"></div>
<div id="ccopts" hidden>
<div class="row sub"><span>Your brand<small>You are promoting yourself or your own business. Labelled "Promotional content".</small></span><input type="checkbox" id="yb"></div>
<div class="row sub"><span>Branded content<small>You are promoting another brand or a third party. Labelled "Paid partnership".</small></span><input type="checkbox" id="bc"></div>
<div class="warn" id="ccwarn" hidden>You need to indicate if your content promotes yourself, a third party, or both.</div>
</div>
<p class="hint" id="consent"></p>
<button id="go" disabled>Post</button><p id="msg" role="status"></p>
<p class="hint">After you post, it can take a few minutes for the video to process and appear on your profile.</p>
</main><script>
const K=${JSON.stringify(k)},JOB=${JSON.stringify(job)},$=id=>document.getElementById(id);let ci=null;
const M='<a href="https://www.tiktok.com/legal/page/global/music-usage-confirmation/en" target="_blank" rel="noopener">Music Usage Confirmation</a>';
const B='<a href="https://www.tiktok.com/legal/page/global/bc-policy/en" target="_blank" rel="noopener">Branded Content Policy</a>';
function upd(){const cc=$("cc").checked,yb=$("yb").checked,bc=$("bc").checked;$("ccopts").hidden=!cc;$("ccwarn").hidden=!(cc&&!yb&&!bc);
 const so=[...$("priv").options].find(o=>o.value==="SELF_ONLY");if(so){so.disabled=bc;if(bc&&$("priv").value==="SELF_ONLY")$("priv").value="";}
 $("privhint").textContent=bc?"Branded content visibility can't be set to private.":"";
 $("consent").innerHTML="By posting, you agree to TikTok's "+(cc&&bc?B+" and ":"")+M+".";
 $("go").disabled=!ci||!$("priv").value||(cc&&!yb&&!bc);}
fetch("/api/tiktok/creator?k="+encodeURIComponent(K)).then(r=>r.json()).then(r=>{const d=r.data;
 if(!d||r.error&&r.error.code!=="ok"){$("nick").textContent="Can't reach TikTok right now";$("msg").textContent="Try again in a few minutes.";return;}
 ci=d;$("nick").textContent=d.creator_nickname+" (@"+d.creator_username+")";$("av").src=d.creator_avatar_url;
 const L={PUBLIC_TO_EVERYONE:"Everyone",MUTUAL_FOLLOW_FRIENDS:"Friends",FOLLOWER_OF_CREATOR:"Followers",SELF_ONLY:"Only me"};
 d.privacy_level_options.forEach(v=>{const o=document.createElement("option");o.value=v;o.textContent=L[v]||v;$("priv").appendChild(o);});
 [["comment","comment_disabled"],["duet","duet_disabled"],["stitch","stitch_disabled"]].forEach(([a,b])=>{if(d[b]){$("c_"+a).disabled=true;$("c_"+a).checked=false;}});
 const dur=document.querySelector("video");dur.addEventListener("loadedmetadata",()=>{if(dur.duration>d.max_video_post_duration_sec){$("msg").textContent="This video is longer than your account allows.";ci=null;upd();}});
 upd();});
fetch("/api/tiktok/stats?k="+encodeURIComponent(K)).then(r=>r.json()).then(r=>{const u=r.user;if(!u){$("acct").textContent="Stats unavailable right now.";return;}
 $("acct").textContent=u.follower_count+" followers · "+u.likes_count+" likes · "+u.video_count+" videos";
 $("vids").innerHTML=r.videos.map(v=>'<div><img alt="" src="'+v.cover_image_url+'"><span>'+String(v.title||"").replace(/[<>&]/g,"").slice(0,48)+'<br><span class="hint">'+v.view_count+' views · '+v.like_count+' likes · '+v.comment_count+' comments · '+v.share_count+' shares</span></span></div>').join("");});
["priv","cc","yb","bc"].forEach(i=>$(i).addEventListener("change",upd));
$("go").onclick=async()=>{$("go").disabled=true;$("msg").textContent="Uploading to TikTok…";
 const r=await fetch("/api/tiktok/publish?k="+encodeURIComponent(K),{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({job:JOB,title:$("cap").value,
  privacy_level:$("priv").value,allow_comment:$("c_comment").checked,allow_duet:$("c_duet").checked,allow_stitch:$("c_stitch").checked,
  is_aigc:$("aigc").checked,your_brand:$("cc").checked&&$("yb").checked,branded_content:$("cc").checked&&$("bc").checked})}).then(r=>r.json());
 if(!r.publish_id){$("msg").textContent="TikTok didn't accept it: "+JSON.stringify(r.error||r).slice(0,160);$("go").disabled=false;return;}
 $("msg").textContent="Sent. TikTok is processing it…";
 for(let i=0;i<30;i++){await new Promise(s=>setTimeout(s,6000));const s=await fetch("/api/tiktok/status?k="+encodeURIComponent(K)+"&id="+encodeURIComponent(r.publish_id)).then(r=>r.json());
  const st=s.data&&s.data.status;if(st==="PUBLISH_COMPLETE"){$("msg").textContent="✅ Posted to TikTok.";return;}
  if(st==="FAILED"){$("msg").textContent="TikTok couldn't post it: "+(s.data.fail_reason||"unknown");return;}
  $("msg").textContent="TikTok is processing it… ("+(st||"waiting")+")";}
 $("msg").textContent="Still processing. It should appear on your profile shortly.";};
</script></body></html>`;
  return new Response(html, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store", "x-robots-tag": "noindex" } });
}
