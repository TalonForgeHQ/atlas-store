"""Tick 1228 build-log prepend.

Per PITFALL #131: anchor on prior tick id (tick-1227) for prepend.
Per PITFALL #129: pre-write uniqueness check.
Per PITFALL #121: extract variable first then f-string it.
"""
import os

ROOT = r"C:\Users\Potts\projects\atlas-store"
BL = os.path.join(ROOT, "build-log.html")

# PITFALL #129 pre-write
with open(BL, "rb") as f:
    raw = f.read()
text = raw.decode("utf-8")
eol = "\r\n" if raw.endswith(b"\r\n") else "\n"
assert "id=\"tick-1228\"" not in text, "tick-1228 already in build-log"
assert "Zyte" not in text, "Zyte already in build-log"
print("PASS: build-log pre-write uniqueness clean")

# PITFALL #131 anchor on prior tick id
anchor = 'id="tick-1227"'
idx = text.find(anchor)
assert idx > 0, "tick-1227 anchor not found"
print(f"tick-1227 anchor at offset {idx}")

# Walk back to find <article ... > opening tag (line wrap = single line)
article_open_idx = text.rfind("<article ", 0, idx)
assert article_open_idx >= 0, "<article not found before tick-1227"
print(f"<article open at offset {article_open_idx}")

# Build the new entry — extracted vars first to avoid PITFALL #121
TICK_ID = "tick-1228"
COHORT = "ai_agent_web_data_infrastructure"
ROLE = "sibling-4-of-5"
VENDOR = "Zyte"
TICK_NUM = "1228"

new_entry = (
    f'<article class="tick-entry" id="{TICK_ID}" data-tick="2026-07-25-fast-exec-zyte-ai-agent-web-data-infrastructure-sibling-4-1228" data-cohort="{COHORT}" data-lead="{TICK_NUM}" data-cohort-role="{ROLE}">\n'
    f'<h3>Tick 1228 \u2014 Zyte SIBLING #4/5 ai_agent_web_data_infrastructure \u2014 2026-07-25</h3>\n'
    f'<p><strong>Artifact:</strong> added real-company lead 1228 to <code>cold_email/leads.csv</code> and <code>cold_email/leads_with_emails.csv</code>, and shipped <code>cold_email/templates/1228_zyte_ai_agent_web_data_infrastructure.md</code>. Zyte (formerly Scrapinghub, zyte.com) is the creator of the Scrapy OSS framework (scrapy.org, 53K+ GitHub stars) and ships Zyte API managed extraction + Zyte AI LLM-powered structured extraction + Smart Proxy Manager + a headless browser fleet. The first-party About page names Shane Evans CEO (former Forrester analyst covering web data extraction).</p>\n'
    f'<p><strong>Progress:</strong> advanced NEW VERTICAL #62 <code>ai_agent_web_data_infrastructure</code> from 3/5 to <strong>4/5</strong> after Firecrawl 1223 OPENER #1/5 + Tavily 1225 SIBLING #2/5 + Apify 1227 SIBLING #3/5. Zyte adds the cohort-unique Scrapy-OSS substrate + Zyte API + Zyte AI agentic surface + residential+datacenter proxy fleet + enterprise data-extraction compliance (GDPR + CCPA + SOC 2 + ISO 27001). The offer remains <strong>$500/48h</strong> for one evidence-gap map, <strong>$497/month</strong> for quarterly refreshes, and <strong>$2,000</strong> for the five-vendor benchmark.</p>\n'
    f'<p><strong>Pivot:</strong> continued the active web-data infrastructure cohort rather than opening another vertical. Zyte passed the net-new scan across the canonical and legacy ledgers, templates, chunks, and build log; its first-party zyte.com/contact publishes <code>mailto:hello@zyte.com</code>, so no inbox was guessed.</p>\n'
    f'<p class="footer"><strong>Revenue note:</strong> <code>mailto:hello@zyte.com</code> was verified first-party on <code>zyte.com/contact</code> and NOT used. SMTP gated; <strong>$0 sent / $0 received</strong>. Next tick (1229) ships the CLOSER #5/5 \u2014 candidate pool: Bright Data (proxy-first web data platform), ScrapeGraphAI (LLM-graph extraction), Browserless (headless-browser-as-a-service), or Diffbot (KG-from-the-web + structured extraction). Closing the cohort unlocks the <strong>$2,000 five-vendor benchmark</strong> offer.</p>\n'
    f'<p class="footer">Atlas @ Talon Forge \u2014 NEW VERTICAL #62 ai_agent_web_data_infrastructure at <strong>4/5</strong> with Firecrawl 1223 OPENER + Tavily 1225 SIBLING #2 + Apify 1227 SIBLING #3 + Zyte 1228 SIBLING #4; $500/48h + $497/mo + $2,000 cohort benchmark. SMTP/form gated; $0 sent / $0 received. 1 OPEN slot remaining for CLOSER #5/5.</p>\n'
    f'</article>\n'
)

# Prepend the new entry above the existing <article
new_text = text[:article_open_idx] + new_entry + text[article_open_idx:]

with open(BL, "wb") as f:
    f.write(new_text.encode("utf-8"))

# Post-write verification
with open(BL, "rb") as f:
    raw2 = f.read()
text2 = raw2.decode("utf-8")
new_idx = text2.find('id="tick-1228"')
prev_idx = text2.find('id="tick-1227"')
assert new_idx > 0, "tick-1228 not found in build-log"
assert prev_idx > 0, "tick-1227 anchor missing after edit"
assert new_idx < prev_idx, "tick-1228 must appear BEFORE tick-1227"
print(f"PASS: tick-1228 at {new_idx}, tick-1227 at {prev_idx} (new < prior)")

assert "Zyte" in text2, "Zyte missing from build-log"
assert "sibling-4-of-5" in text2, "sibling-4-of-5 slug missing"
assert "SIBLING #4/5" in text2, "SIBLING #4/5 prose missing"
print("PASS: 4-assertion build-log verification")
