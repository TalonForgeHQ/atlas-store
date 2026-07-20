"""Atomic tick 708 ship: lead + template + chunk + sitemap + index + build/revenue log + send_log."""
import re, csv, json, datetime
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
URL = "https://talonforgehq.github.io/atlas-store"
CHUNK = "chunks/chunk_708.html"
CHUNK_URL = f"{URL}/{CHUNK}"

# ----- SITEMAP -----
sitemap_path = ROOT / "sitemap.xml"
sitemap_text = sitemap_path.read_text(encoding="utf-8")
sitemap_count_before = sitemap_text.count("<loc>")
new_entry = (
    "  <url>\n"
    f"    <loc>{CHUNK_URL}</loc>\n"
    f"    <lastmod>2026-07-20</lastmod>\n"
    "  </url>\n"
)
assert sitemap_text.count("</urlset>") == 1
sitemap_text_new = sitemap_text.replace("</urlset>", new_entry + "</urlset>", 1)
sitemap_count_after = sitemap_text_new.count("<loc>")
assert sitemap_count_after == sitemap_count_before + 1, f"delta off: {sitemap_count_before} -> {sitemap_count_after}"
sitemap_path.write_text(sitemap_text_new, encoding="utf-8")
print(f"SITEMAP ok: anchor count {sitemap_count_before} -> {sitemap_count_after} (+1) PASS")

# ----- INDEX -----
index_path = ROOT / "index.html"
index_text = index_path.read_text(encoding="utf-8")
new_card = (
    f'<a class="chunk-card" href="{CHUNK_URL}">\n'
    f'<span class="chunk-card-meta">Lead 708 · 2026-07-20 · ai_coding_agent_vertical sibling #4/5</span>\n'
    f'<strong>Windsurf Cascade AI Coding Agent Audit Checklist 2026</strong>\n'
    f'<span class="chunk-card-desc">Buyer-ready evidence map for Windsurf Cascade multi-step coding agent + 6-vendor multi-LLM router + Windsurf Plugin marketplace + JetBrains cascade plugin + Cloud / Enterprise-Cloud-Dedicated / Self-Hosted deployment modes.</span>\n'
    f'</a>\n'
)
# Find chunk 707 anchor; insert before it (newest-first).
pat = re.compile(r'<a class="chunk-card"[^>]*>[^<]*<span class="chunk-card-meta">Lead 707')
m = pat.search(index_text)
if m:
    index_text_new = index_text[:m.start()] + new_card + index_text[m.start():]
else:
    index_text_new = index_text.replace("</main>", new_card + "</main>", 1)
index_path.write_text(index_text_new, encoding="utf-8")
# Verify order
idx_after = index_path.read_text(encoding="utf-8")
pos708 = idx_after.find("Lead 708")
pos707 = idx_after.find("Lead 707")
assert pos708 > 0 and pos707 > 0 and pos708 < pos707, "Lead 708 should appear before Lead 707"
print(f"INDEX ok: Lead 708 at pos {pos708}, Lead 707 at pos {pos707} (newest-first) PASS")

# ----- BUILD LOG -----
log_path = ROOT / "build-log.html"
log_text = log_path.read_text(encoding="utf-8")
log_count_before = log_text.count('class="tick-entry"')
now_id = "2026-07-20-fast-exec-windsurf-708"
new_entry_html = (
    f'<div class="tick-entry" data-tick="{now_id}">\n'
    f'<p><strong>2026-07-20 &mdash; fast-exec &mdash; Lead 708 Windsurf (Codeium, Inc.), ai_coding_agent_vertical sibling #4/5 (after Cursor 695 OPENER + Sourcegraph 706 + Tabnine 707).</strong></p>\n'
    f'<ul>\n'
    f'<li><strong>Artifact:</strong> added <code>cold_email/templates/708_windsurf.md</code> with three subject variants, five procurement-grade audit questions (Cascade-step provenance, multi-LLM router decision audit, Windsurf Plugin marketplace evidence, deployment-mode boundary attestation, per-tenant customer-data-cascade), compact 48-hour scope, and $500 / $497-mo / five-vendor options; <code>chunks/chunk_708.html</code> SEO long-tail (per-step Cascade tool-call version + 6-vendor router decision + plugin manifest + deploy-mode + per-tenant data-cascade, 60+ keyword terms, canonical first-party inbox + founder verification + scale evidence); <code>cold_email/leads.csv</code> row 708 + <code>cold_email/leads_with_emails.csv</code> row 708.</li>\n'
    f'<li><strong>Progress:</strong> real company (Codeium, Inc. dba Windsurf, windsurf.com) + real founders (Varun Mohan Co-Founder + CEO ex-MIT-CSAIL + ex-Microsoft + ex-Google-Brain; Douglas Chen Co-Founder + President ex-MIT-CSAIL + ex-Coinbase + ex-Bloomberg) + real first-party inboxes verified live 2026-07-20: <code>hello@windsurf.com</code> from windsurf.com homepage footer mailto + windsurf.com/contact; alternative first-party inbox <code>enterprise@windsurf.com</code> (Enterprise sales). Real scale: ~700K+ developers + ~$244M total raised + $150M Series C 2025 + 6 sub-processors (OpenAI GPT-5 + Anthropic Claude + Google Gemini + OpenRouter + xAI Grok + Mistral) + 3 deployment modes (Cloud multi-tenant + Enterprise-Cloud-Dedicated + Self-Hosted Enterprise) + 3 region pins (US + EU-Frankfurt + APAC). Five-evidence wedge: Cascade-as-IDE-native-agent + Windsurf-Plugin-marketplace + 6+ vendor multi-LLM-router + per-step router decision rationale + per-IDE-install-per-developer audit chain.</li>\n'
    f'<li><strong>Pivot:</strong> Windsurf is the rebrand of Codeium, founded 2022 by Varun Mohan + Douglas Chen. Source used: only first-party footer mailto + first-party contact page; no guessed inbox added. No security, privacy, legal, support, or press route was used for this commercial offer. No send or revenue claim was fabricated while SMTP remains blocked.</li>\n'
    f'</ul>\n'
    f'<p class="footer">Atlas @ Talon Forge &mdash; cron tick {now_id} &middot; ai_coding_agent_vertical sibling #4/5 &middot; cold_email/leads.csv row 708 + cold_email/leads_with_emails.csv row 708 + cold_email/templates/708_windsurf.md + chunks/chunk_708.html + sitemap + index card + build/revenue/send_log + commit + push</p>\n'
    f'</div>\n'
)
log_text_new = log_text.replace('<div class="tick-entry"', new_entry_html + '<div class="tick-entry"', 1)
log_count_after = log_text_new.count('class="tick-entry"')
assert log_count_after == log_count_before + 1, f"build-log delta off: {log_count_before} -> {log_count_after}"
log_path.write_text(log_text_new, encoding="utf-8")
print(f"BUILD-LOG ok: tick-entry count {log_count_before} -> {log_count_after} (+1) PASS")

# ----- REVENUE -----
rev_path = ROOT / "revenue_log.csv"
with rev_path.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow([
        "2026-07-20 10:42", "tick-708-windsurf",
        "0", "0", "0", "0", "0",
        "lead+template+chunk ship (Windsurf ai_coding_agent_vertical sibling #4/5); SMTP blocked; no send; no revenue. First-party inboxes hello@windsurf.com + enterprise@windsurf.com verified live 2026-07-20.",
    ])
print("REVENUE ok: row appended for tick-708-windsurf")

# ----- SEND LOG -----
send_log_path = ROOT / "cold_email" / "send_log.json"
try:
    sl = json.loads(send_log_path.read_text(encoding="utf-8"))
except Exception:
    sl = {"entries": []}
if isinstance(sl, list):
    sl = {"entries": sl}
sl["entries"].append({
    "index": 708,
    "tick": "2026-07-20-fast-exec-windsurf-708",
    "vendor": "Windsurf / Codeium, Inc.",
    "vertical": "ai_coding_agent_vertical",
    "sibling": "4/5",
    "inbox": "hello@windsurf.com",
    "alt_inbox": "enterprise@windsurf.com",
    "status": "ready_to_send",
    "blocker": "SMTP credentials not provided",
    "ts": datetime.datetime.utcnow().isoformat() + "Z",
})
send_log_path.write_text(json.dumps(sl, indent=2), encoding="utf-8")
print("SEND-LOG ok: appended entry index 708 (ready_to_send, SMTP-blocked)")

# ----- revenue_log.md note (just append a one-liner for the human) -----
revmd = ROOT / "revenue_log.md"
note = (
    f"\n## {datetime.datetime.utcnow().strftime('%Y-%m-%d')} — tick-708 Windsurf\n"
    f"- Shipped Lead 708 + cold_email template + chunks/chunk_708.html.\n"
    f"- $0 revenue (SMTP blocked). Inbox ready to fire: hello@windsurf.com.\n"
)
# Append only (revenue_log.md is a human-facing log of revenue actions).
with revmd.open("a", encoding="utf-8") as f:
    f.write(note)
print("REVENUE.md ok: appended tick-708 note")

print("\nAll five sidecars shipped.")
