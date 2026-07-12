"""Prepend Tick 120 build-log entry (Variant B: anchored on <div class=\"tick\"> at position 0)."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
build_log = REPO / "build-log.html"
content = build_log.read_text(encoding="utf-8")

# Sanity: Variant B file
assert content.startswith('<div class="tick">'), f"Variant mismatch, starts with: {content[:50]!r}"

NEW_ENTRY = '''<div class="tick">
<h2>[2026-07-12 17:36 +0700 / 10:36 UTC] Tick 120 &mdash; Shipped: Reclaim.ai (Lead 215 + Template 303, b2b_saas 20th sibling)</h2>
<p>Lead 215 = Reclaim.ai (@reclaimai, <a href="https://reclaim.ai/privacy">reclaim.ai/privacy</a>) &mdash; canonical AI-calendar + AI-scheduling + AI-task-automation SaaS (Reclaim Calendar + Reclaim Planner + Reclaim Habits + Reclaim Chat + 50+ integrations for Google Calendar + Outlook + iCloud + Zoom + Slack + Notion + Linear + Jira + Todoist + HubSpot + Salesforce). privacy@reclaim.ai directly verified live 2026-07-12 via curl scrape <a href="https://reclaim.ai/privacy">reclaim.ai/privacy</a> exposing mailto:privacy@reclaim.ai as canonical GDPR DPA + SOC 2 + EU AI Act vendor-DD channel. Founded 2019 by Henry Shapiro (CEO) + Patrick Lightbody (Co-Founder, ex-BrowserStack). HQ San Francisco CA. 50000+ paying teams + solo-pros. SOC 2 Type II + GDPR DPA + EU AI Act readiness per reclaim.ai/security + reclaim.ai/dpa. 20th b2b_saas vertical sibling + 1st canonical AI-calendar-automation + 1st Reclaim Chat AI-scheduling-agent + 1st with EU AI Act Annex III high-risk-scheduling-decision framing for vendor-DD. Pipeline now 215 leads / 303 templates / 108 SEO chunks. Pivot note: Height.app SPA-blocked (0 mailto on /privacy) &mdash; pivoted within b2b_saas vertical to Reclaim.ai (canonical calendar-AI-ops) which verified on first probe.</p>
<span class="tick-action">+ 1 lead (215 Reclaim.ai)</span>
<span class="tick-action">+ 1 template (303_reclaim.md)</span>
<span class="tick-action">+ 1 build-log entry (Tick 120)</span>
</div>
'''

# Double-wrap sanity: exactly one wrapper in new_entry
_wc = NEW_ENTRY.count('<div class="tick">')
assert _wc == 1, f"new_entry has wrong wrapper count: {_wc}"

idx = content.find('<div class="tick">')
assert idx == 0, f"Variant B file should start with <div class=\"tick\">, but idx={idx}"
new_content = NEW_ENTRY + content

build_log.write_text(new_content, encoding="utf-8")

# Verify: newest tick now before second-newest
content2 = build_log.read_text(encoding="utf-8")
tick_120_pos = content2.find("Tick 120")
tick_119_pos = content2.find("Tick 119")
tick_118_pos = content2.find("Tick 118")
assert tick_120_pos == -1 or tick_119_pos == -1 or tick_118_pos == -1 or (tick_120_pos < tick_119_pos < tick_118_pos), f"reverse-chronological broken: 120@{tick_120_pos} 119@{tick_119_pos} 118@{tick_118_pos}"
assert content2.startswith('<div class="tick">'), "file no longer starts with wrapper"

print(f"OK: prepended Tick 120 (pos {tick_120_pos}) above Tick 119 (pos {tick_119_pos})")
print(f"OK: file starts: {content2[:50]!r}")
print(f"OK: file size: {len(content2)} bytes")