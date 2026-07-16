"""Prepend Tick 2026-07-17-1926Z entry to build-log.html.
Variant C file: anchor = first occurrence of <div class="tick-entry" data-tick= (newest-first)."""
from pathlib import Path

BUILDLOG = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")

NEW_ENTRY = '''<div class="tick-entry" data-tick="2026-07-17-1926Z">
<h2>Tick 2026-07-17-1926Z &mdash; Lead 381 Deepgram (realtime_voice_video_ai_infra 4th-sibling STT backbone) + Template 381 + Chunk 228 Deepgram Nova-3 audit checklist</h2>
<p><strong>Action:</strong> Shipped lead 381 Deepgram (Scott Stephenson, Co-Founder &amp; CEO + Adam Sypniewski, Co-Founder &amp; CTO) &mdash; canonical speech-to-text (ASR) backbone + voice-agent-native Nova-3 model for the <code>realtime_voice_video_ai_infra</code> cohort, extending canonical WebRTC SFU + voice/video AI agent infrastructure after LiveKit 375 1st-vertex + Daily.co 379 2nd-sibling + Agora 380 3rd-sibling. Deepgram serves 100B+ minutes of speech per year, 200+ enterprise customers, 50,000+ developers building on Deepgram API + Deepgram Voice Agent API + Nova-3 Speech Model + Aura-2 TTS. Inbox <code>security@deepgram.com</code> verified live 2026-07-17 by curl scrape of https://deepgram.com/privacy (HTTP 200, 280,444 bytes, exposes mailto:security@deepgram.com as canonical security + vendor-DD strategic-inbound channel). Founder evidence: official Deepgram about page https://deepgram.com/about (HTTP 200, 583,324 bytes) names Scott Stephenson (Co-Founder &amp; CEO) + Adam Sypniewski (Co-Founder &amp; CTO). Founded 2015 San Francisco CA. HQ San Francisco CA. Backed $80M+ across Seed + Series A + Series B from Wing VC + Allegion Ventures + Tiger Global + Avigdor Willenz Group + MetaProp NYC + Y Combinator + NVIDIA Inception Program.</p>
<p><strong>Artifacts:</strong> leads.csv row index=381 (Deepgram, vertical=realtime_voice_video_ai_infra, tier=1, email=security@deepgram.com, tier_reason 4238 chars). Template 381_deepgram.md (5-vendor-DD-question opener for the security team: per-request provenance join-table + prompt-injection + cross-region audio-data-residency + HIPAA-eligible medical-transcription + cross-tenant isolation). Chunk 228 (Deepgram audit checklist SOC 2 + HIPAA + EU AI Act for Nova-3 Voice Agent ASR Backbone) &mdash; 145 lines, 16 headings, 60-col per-request provenance join-table, OWASP LLM Top 10 + MITRE ATLAS coverage, HIPAA §164.312(b) + EU AI Act Art. 12 + 8-jurisdiction residency.</p>
<p><strong>Surface verification:</strong> leads.csv (263 rows, well-formed index 381 with Scott Stephenson evidence + privacy/security mailbox pattern); template 381_deepgram.md (5 vendor-DD questions in opener + closes); chunk_228.html (145 lines, 16 headings, canonical 60-col per-request provenance join-table + 5-audit-gap analysis + 30-day adoption plan + companion links to chunks 223/224/225/226/227); sitemap.xml (208 balanced &lt;url&gt; open/close tags + chunk_228 entry with 2026-07-17 lastmod); index.html (id=&quot;chunk-228&quot; appears 1 time, inlined after the last chunk_227 closing comment; chunk-227 anchor still appears 59 times preserved).</p>
<p><strong>Pivot:</strong> Twilio (rt_v_v_ai vertical 5th candidate) was probed first but the entire twilio.com domain is SPA-rendered JS-shell (every route returns identical 597020-byte skeleton), no static mailto exposed. Pivoted within-vertical to Deepgram (canonical STT backbone, not just another SFU) &mdash; clean inbox verification in 2 tool calls.</p>
</div>
'''

text = BUILDLOG.read_text(encoding="utf-8")

# Variant C: anchor on the first <div class="tick-entry" data-tick=  (newest-first invariant)
anchor = '<div class="tick-entry" data-tick="'
first_anchor_idx = text.find(anchor)
assert first_anchor_idx >= 0, "anchor not found"
assert first_anchor_idx < 200, f"anchor at unexpected offset {first_anchor_idx}"

new_text = text[:first_anchor_idx] + NEW_ENTRY + text[first_anchor_idx:]

# Verify exactly one new entry prepended (NEW_ENTRY contains exactly one wrapper)
assert NEW_ENTRY.count('<div class="tick-entry"') == 1, "NEW_ENTRY wrapper count wrong"
# Verify the new entry is at the top (data-tick starts at position 0)
assert new_text[:len('<div class="tick-entry" data-tick="')] == '<div class="tick-entry" data-tick="', "new entry not at top"

# Sanity: the new tick should be the first data-tick, before 2026-07-17-1918Z (the prior top)
new_top = new_text.find('data-tick="2026-07-17-1926Z"')
prior_top = new_text.find('data-tick="2026-07-17-1918Z"')
assert new_top == len('<div class="tick-entry" '), f"new tick should start at char ~25, got {new_top}"
assert prior_top > new_top, f"prior tick 1918Z should come AFTER new tick 1926Z, got new_top={new_top} prior_top={prior_top}"

BUILDLOG.write_text(new_text, encoding="utf-8")
print(f"OK build-log prepended: new tick at char {new_top}, prior tick at char {prior_top}")
print(f"  build-log.html size: {len(new_text)} bytes (was {len(text)} bytes)")