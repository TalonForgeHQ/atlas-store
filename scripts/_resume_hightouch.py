from pathlib import Path
import csv
import shutil

root = Path(__file__).resolve().parents[1]

# Resume the prior Hightouch partial ship without duplicating existing ownership keys.
source = root / "chunks" / "chunk_151.html"
canonical = root / "_chunks" / "chunk_151.html"
canonical.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(source, canonical)

# leads_with_emails.csv has a different schema from leads.csv; append only its 13 fields.
with (root / "cold_email" / "leads_with_emails.csv").open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
existing_ids = {row[0].strip('"') for row in rows[1:] if row and row[0].strip('"')}
if "277" not in existing_ids:
    row = [
        "277", "Hightouch", "@hightouch", "hightouch.com", "https://www.hightouch.com",
        "Tejas Manohar (Co-Founder + CEO) + Kashish Gupta (Co-Founder + CTO)",
        "data_ops_reverse_etl", "1", "privacy@hightouch.com", "privacy@hightouch.com", "",
        "277_hightouch.md",
        "Canonical Composable Customer Data Platform (CDP) and reverse-ETL competitor to Census (276), syncing warehouse data to 200+ SaaS destinations with the AI Decisioning layer (Hightouch AI). privacy@hightouch.com verified as canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channel. Founded 2019 in San Francisco CA by Tejas Manohar (Co-Founder + CEO, ex-Wing Alphabet, ex-Facebook) + Kashish Gupta (Co-Founder + CTO, ex-Facebook data-platform). Tier-1 data_ops_reverse_etl sibling-target for per-sync-run provenance, per-AI-Decisioning-suggestion audit trail, prompt-injection isolation across reverse-ETL destinations, per-destination-API-call attribution, and the AI Decisioning cross-tenant reasoning-chain joinable per-tenant-key."
    ]
    with (root / "cold_email" / "leads_with_emails.csv").open("a", encoding="utf-8", newline="") as f:
        csv.writer(f, quoting=csv.QUOTE_ALL).writerow(row)

# Inline the public landing-page summary on the same surface as the chunk route.
index_path = root / "index.html"
index = index_path.read_text(encoding="utf-8")
if 'id="chunk-151"' not in index:
    anchor = '<section class="chunk" id="chunk-150">'
    start = index.find(anchor)
    if start < 0:
        raise SystemExit("chunk-150 anchor missing from index.html")
    body_end = index.find("</body>", start)
    if body_end < 0:
        raise SystemExit("main index body close missing")
    outer_close = index.rfind("</section>", start, body_end)
    if outer_close < 0:
        raise SystemExit("main index section close missing")
    section = '''<section class="chunk" id="chunk-151">
<h3>chunk-151 — Hightouch AI Decisioning + Reverse-ETL audit-trail review</h3>
<p><strong>Lead:</strong> Hightouch (lead 277, privacy@hightouch.com, tier-1 data_ops_reverse_etl, founders Tejas Manohar + Kashish Gupta). Long-tail: Hightouch Composable CDP + Reverse-ETL + AI Decisioning + 200+ SaaS destinations + Customer Studio + Audience Hub audit-trail review covering per-sync-run provenance, per-AI-Decisioning-suggestion reasoning-chain, per-destination-API-call attribution, per-tenant isolation, WORM retention, and cross-tenant prompt-injection defense for SOC 2 + ISO 27001 + GDPR + EU AI Act + ISO 42001.</p>
<p><a href="chunks/chunk_151.html">Read the full Hightouch AI Decisioning + Reverse-ETL audit-trail review guide →</a></p>
</section>
'''
    index = index[:outer_close] + section + index[outer_close:]
    index_path.write_text(index, encoding="utf-8")

# Move the prior fast-execution entry to the newest-first position and prepend a truthful 3-line resume status.
log_path = root / "build-log.html"
log = log_path.read_text(encoding="utf-8")
old_marker = "<!-- TICK 2026-07-16 ~06:00Z -->"
old_start = log.find(old_marker)
if old_start >= 0:
    old_end = log.find("</div>", old_start)
    if old_end < 0:
        raise SystemExit("prior Hightouch build-log block is unterminated")
    old_end += len("</div>")
    old_block = log[old_start:old_end]
    log = log[:old_start] + log[old_end:]
else:
    old_block = ""
status = '''<!-- TICK 2026-07-16 ~06:10Z -->
<div class="tick-entry" data-tick="2026-07-16-0610Z">
<h3>Tick 2026-07-16 06:10:00 UTC — Fast Execution resume</h3>
<ul>
<li><strong>Repaired Hightouch (277) partial ship:</strong> copied <code>chunks/chunk_151.html</code> into canonical source <code>_chunks/chunk_151.html</code>; source and public chunk are byte-identical.</li>
<li><strong>Completed secondary surfaces:</strong> appended the correctly shaped 13-column row to <code>cold_email/leads_with_emails.csv</code> without duplicating lead index 277, and inlined <code>id="chunk-151"</code> into <code>index.html</code>.</li>
<li><strong>Progress + pivot:</strong> moved the prior 06:00 Hightouch entry to newest-first position; next ROI pivot is outbound unblocking (Resend / SendGrid / Gmail App Password remains the hard revenue blocker).</li>
</ul>
</div>
'''
log_path.write_text(status + (old_block + "\n" if old_block else "") + log, encoding="utf-8")

print("resume_hightouch: source, leads_with_emails, index inline, and newest-first build-log status repaired")
