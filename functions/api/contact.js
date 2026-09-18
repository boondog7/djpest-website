// Cloudflare Pages Function: POST /api/contact
// Lead capture with three layers so a lead is never lost:
//   1. Durable copy in KV (binding LEADS) keyed by timestamp.
//   2. Email to ops@djpest.com.au via FormSubmit (no account; first send needs a one-time activation click).
//   3. Optional forward to n8n when env N8N_WEBHOOK_URL is set (ServiceM8 job creation, Telegram, etc).

const ALLOWED_ORIGINS = ['https://djpest.com.au', 'https://www.djpest.com.au', 'https://djpest.pages.dev'];
const LEAD_EMAIL = 'ops@djpest.com.au';

const cors = (origin) => ({
  'Access-Control-Allow-Origin': ALLOWED_ORIGINS.includes(origin) || /\.djpest\.pages\.dev$/.test(origin) ? origin : ALLOWED_ORIGINS[0],
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Vary': 'Origin',
});
const json = (obj, status, headers) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', ...headers } });

export async function onRequestOptions({ request }) {
  return new Response(null, { status: 204, headers: cors(request.headers.get('origin') || '') });
}

export async function onRequestPost({ request, env }) {
  const origin = request.headers.get('origin') || '';
  const h = cors(origin);
  let data;
  try { data = await request.json(); } catch { return json({ ok: false, error: 'invalid_json' }, 400, h); }
  if (data.website) return json({ ok: true }, 200, h); // honeypot

  for (const f of ['name', 'phone', 'suburb']) {
    if (!data[f] || String(data[f]).trim().length < 2) return json({ ok: false, error: `missing_${f}` }, 400, h);
  }
  const s = (v, n) => String(v || '').trim().slice(0, n);
  const lead = {
    source: 'djpest.com.au', received_at: new Date().toISOString(),
    name: s(data.name, 120), phone: s(data.phone, 40), email: s(data.email, 200), suburb: s(data.suburb, 80),
    pest: s(data.pest || data.pestType || data.pest_type, 120), message: s(data.message, 2000),
    marketing_consent: data.marketing === 'yes' ? 'yes' : 'no',
    page: request.headers.get('referer') || null, ip: request.headers.get('cf-connecting-ip') || null, ua: request.headers.get('user-agent') || null,
  };

  const jobs = [];
  if (env.LEADS) {
    const key = `${lead.received_at}_${lead.phone.replace(/\D/g, '')}`;
    jobs.push(env.LEADS.put(key, JSON.stringify(lead)).catch((e) => console.error('kv', e)));
  }
  jobs.push(fetch(`https://formsubmit.co/ajax/${LEAD_EMAIL}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify({
      _subject: `New website lead: ${lead.name} (${lead.suburb}) — ${lead.pest || 'pest not specified'}`,
      _template: 'table', _captcha: 'false',
      Name: lead.name, Mobile: lead.phone, Email: lead.email, Suburb: lead.suburb, Pest: lead.pest, Message: lead.message,
      'Marketing consent': lead.marketing_consent, Page: lead.page, Received: lead.received_at,
    }),
  }).then((r) => { if (!r.ok) console.error('formsubmit', r.status); }).catch((e) => console.error('formsubmit', e)));
  if (env.N8N_WEBHOOK_URL) {
    jobs.push(fetch(env.N8N_WEBHOOK_URL, {
      method: 'POST', headers: { 'Content-Type': 'application/json', ...(env.N8N_WEBHOOK_SECRET ? { 'X-Webhook-Secret': env.N8N_WEBHOOK_SECRET } : {}) },
      body: JSON.stringify(lead),
    }).then((r) => { if (!r.ok) console.error('n8n', r.status); }).catch((e) => console.error('n8n', e)));
  }
  await Promise.allSettled(jobs);
  return json({ ok: true }, 200, h);
}

export async function onRequest() {
  return json({ ok: false, error: 'method_not_allowed' }, 405, { Allow: 'POST, OPTIONS' });
}
