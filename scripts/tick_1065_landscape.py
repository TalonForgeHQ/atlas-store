"""Tick 1065 ship helper: update sitemap.xml + index.html + revenue_log.csv + build-log.html + send_log.jsonl"""
import re
import json
import csv
from pathlib import Path

ROOT = Path("C:/Users/Potts/projects/atlas-store")

# Constants
LEAD_ID = "1065"
CHUNK = "1065"
VENDOR = "Portkey"
VENDOR_URL = "portkey.ai"
URL = "https://talonforgehq.github.io/atlas-store/chunks/chunk_1065.html"
COHORT_SLUG = "opener-1-of-5"
COHORT = "ai_agent_llm_gateway"

# =========================
# 1. Append to sitemap.xml
# =========================
sm = ROOT / "sitemap.xml"
sm_text = sm.read_text(encoding="utf-8")

# Match prior canvas chunk_1064 entry for canonical indent (2-space <url>, 4-space <loc>)
new_block = (
    "  <url>\n"
    "    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_1065.html</loc>\n"
    "    <lastmod>2026-07-23</lastmod>\n"
    "    <changefreq>monthly</changefreq>\n"
    "    <priority>0.7</priority>\n"
    "  </url>"
)

# Insert before </urlset>
if "</urlset>" in sm_text:
    new_sm = sm_text.replace("</urlset>", f"{new_block}\n</urlset>")
    if new_sm.count("<loc>") <= sm_text.count("<loc>"):
        # already present
        print("[!] chunk_1065 already in sitemap.xml -- skipping insertion")
    else:
        sm.write_text(new_sm, encoding="utf-8")
        print(f"[OK] sitemap.xml updated; url count: {new_sm.count('<loc>')}")
else:
    print("[!] </urlset> not found -- sitemap not updated")

# =========================
# 2. Append chunk card to index.html (PITFALL #115/120: rfind chunk id of most-recently-shipped)
# =========================
idx = ROOT / "index.html"
idx_text = idx.read_text(encoding="utf-8")

# Find most-recently-shipped chunk id (chunk_1057 was the prior ship)
prior_chunk_id = 'id="chunk-1057"'
insert_after = idx_text.find(prior_chunk_id)
if insert_after == -1:
    print(f"[!] anchor {prior_chunk_id} not found -- falling back to last </section>")
    insert_after = idx_text.rfind("</section>")

# Find the end of the chunk-1057 wrapper section
section_end = idx_text.find("</section>", insert_after)
if section_end == -1:
    print("[!] closing </section> not found after chunk-1057")
else:
    insert_pos = section_end + len("</section>")
    chunk_card_text = idx_text[insert_after:insert_pos]
    print(f"[i] prior chunk card length: {len(chunk_card_text)} chars")

# Read the new chunk from chunks/chunk_1065.html and inline
new_chunk_html = (ROOT / f"chunks/chunk_{CHUNK}.html").read_text(encoding="utf-8")
# Strip the <section ...> wrapper opening tag of the new chunk since index already provides context
# Actually keep it -- other chunks keep the full <section>...</section>
# Ensure newline separation
new_index_text = (
    idx_text[:insert_pos] + "\n" + new_chunk_html + idx_text[insert_pos:]
)
if new_index_text.count('id="chunk-1065"') > idx_text.count('id="chunk-1065"'):
    idx.write_text(new_index_text, encoding="utf-8")
    chunk_marker = 'id="chunk-'
    total_chunks = new_index_text.count(chunk_marker)
    print(f"[OK] index.html updated; total chunks: {total_chunks}")
else:
    print("[!] index.html already has chunk-1065 -- skipping")

# =========================
# 3. Append row to revenue_log.csv
# =========================
rev = ROOT / "revenue_log.csv"
rev_rows = []
rev_header = ["tick", "ts", "lead", "vendor", "cohort", "cohort_role", "offer", "amount_usd", "status", "evidence_path"]
if rev.exists():
    with rev.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            rev_header = next(reader)
        except StopIteration:
            pass
        for row in reader:
            rev_rows.append(row)

rev_rows.append([
    "1065", "2026-07-23T18:55:00Z", "1065", "Portkey", "ai_agent_llm_gateway", "opener-1-of-5",
    "$500/48h fixed-scope Portkey AI-Gateway evidence-gap map", "0", "shipped-template-only",
    "chunks/chunk_1065.html",
])

with rev.open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(rev_header)
    for r in rev_rows:
        w.writerow(r)
print(f"[OK] revenue_log.csv updated; total rows: {len(rev_rows)}")

# =========================
# 4. Append send_log entry -- gap-filler per PITFALL #108
# =========================
sl = ROOT / "cold_email/send_log.jsonl"
# Per PITFALL #97a + #97: bare raw_decode loop
with sl.open("rb") as f:
    raw = f.read()
text = raw.decode("utf-8", errors="replace").strip()
records = []
while text:
    obj, idx_off = json.JSONDecoder().raw_decode(text)
    records.append(obj)
    text = text[idx_off:].strip()

new_send_record = {
    "ts": "2026-07-23T18:55:00Z",
    "lead_id": "1065",
    "vendor": "Portkey",
    "cohort": "ai_agent_llm_gateway",
    "cohort_role": "opener-1-of-5",
    "action": "template_shipped_only",
    "channel": "cold_email/template",
    "evidence": "cold_email/templates/1065_portkey.md",
    "outcome": "no_send_authorized",
    "revenue_usd": 0,
    "comment": "tick 1065: NEW VERTICAL #36 ai_agent_llm_gateway OPENER ship",
}

records.append(new_send_record)
# Rewrite -- use JSON concatenation with one record per line
with sl.open("wb") as f:
    for rec in records:
        line = json.dumps(rec, separators=(",", ":"))
        f.write(line.encode("utf-8"))

print(f"[OK] send_log.jsonl updated; total records: {len(records)}")

# =========================
# 5. Prepend tick-1065 article to build-log.html
# =========================
bl = ROOT / "build-log.html"
bl_text = bl.read_text(encoding="utf-8")

new_article = (
    '<article class="tick-entry" id="tick-1065" data-tick="2026-07-23-fast-exec-portkey-opener-1065" '
    'data-cohort="ai_agent_llm_gateway" data-lead="1065" data-cohort-role="opener-1-of-5">'
    '<h3>tick 1065: 2026-07-23 — Portkey OPENER #1/5 NEW VERTICAL #36 ai_agent_llm_gateway</h3>'
    '<p><strong>Artifact:</strong> shipped Lead 1065 (Portkey) OPENER #1/5 NEW VERTICAL #36 '
    'ai_agent_llm_gateway with companion <code>cold_email/1065_portkey.md</code>, three-subject '
    'template <code>cold_email/templates/1065_portkey.md</code>, and SEO chunk '
    '<code>chunks/chunk_1065.html</code> wired into <code>index.html</code> and '
    '<code>sitemap.xml</code>.</p>'
    '<p><strong>Progress:</strong> opened <code>ai_agent_llm_gateway</code> cohort '
    'with Portkey AI as the canonical AI-Gateway OPENER. The cohort wedge is the dedicated '
    'LLM-call gateway between an agent and 200+ upstream model providers — routing + '
    'fallbacks + semantic cache + provider-credential vault + per-virtual-key audit trail. '
    '5-WEDGE non-overlap: (1) AI-Gateway-only substrate vs all 14 closed cohorts; (2) '
    'provider-credential vault + BYOC + per-virtual-key rate-limit SOC 2 + GDPR lane; '
    '(3) fallback + conditional routing + semantic cache canonical cost-optimization '
    'surface; (4) per-virtual-key + per-provider cost/usage reconciliation audit ledger; '
    '(5) SOC 2 Type II + GDPR + HIPAA BAA + EU AI Act readiness + Free + Pro + Enterprise '
    'tier ladder. First-party pages not LIVE-crawled this tick (sandbox Cron) — public-knowledge '
    'fingerprint re-verification deferred to a future execution tick per PITFALL #98 recovery '
    'pattern. Founder Rohit Agarwal (CEO) + Vishnu Kiran (co-founder). HQ San Francisco CA. '
    'Y Combinator W22 graduate. Sibling plan: Helicone (SIBLING #2/5) + LiteLLM '
    '(SIBLING #3/5) + Unify (SIBLING #4/5) + Bifrost (CLOSER #5/5).</p>'
    '<p><strong>Pivot:</strong> cohort 5-WEDGE plan set; no email/form submitted; '
    'SMTP/form gated; <code>$0 sent / $0 received</code>. Future ticks will close '
    'Helicone + LiteLLM + Unify + Bifrost to advance to CLOSER #5/5.</p></article>'
)

# Prepend after the opening of <body> or after the </header>. Use insertion: find first <article
# (the first tick entry) and insert before
first_article_pos = bl_text.find('<article class="tick-entry"')
if first_article_pos == -1:
    print("[!] no <article> anchor found in build-log")
else:
    new_bl = bl_text[:first_article_pos] + new_article + bl_text[first_article_pos:]
    bl.write_text(new_bl, encoding="utf-8")
    print(f"[OK] build-log.html prepended with tick-1065 article")
print("[i] all artifacts shipped")
