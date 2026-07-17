"""Prepend build-log entry for Tick 1355Z (Lead 436 ElevenLabs)."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
BUILD_LOG = REPO / "build-log.html"

ENTRY = '''<div class="tick-entry" data-tick="2026-07-17-1355Z">
<h2>Tick 2026-07-17-1355Z &mdash; Lead 436 ElevenLabs Conversational AI Voice-Agent (10th voice_agents sibling)</h2>
<p><strong>+ chunk_265.html</strong> (ElevenLabs Conversational AI Voice-AI Audit Binder 2026: Voice Cloning + Voice Library + Dubbing Studio + Sound Effects + Voice Isolator + Conversational AI + 1M+ Developers + 30+ Languages + EU AI Act Art. 15 Coverage &mdash; 5 audit gaps for voice-AI orchestration cohort: per-conversation-id provenance join-table, OWASP LLM Top 10 + MITRE ATLAS voice-AI attack coverage matrix, per-prompt-injection + per-Voice-Clone-consent-verification + per-Voice-Library-content-moderation + per-deepfake-watermark + per-provenance-attestation defense, cross-ElevenLabs-tenant + per-voice-clone-id + per-Voice-Library-creator-id isolation-evidence, WORM retention + per-Voice-Library-monetization-payout-id cost-attribution join-table).</p>
<p><strong>+ leads.csv 314 / leads_with_emails.csv 297</strong> (Lead 436 ElevenLabs &mdash; thor@elevenlabs.io verified live via GitHub commits API on github.com/elevenlabs/captions.events + developers@elevenlabs.io via GitHub org metadata API + legal@elevenlabs.io via curl https://elevenlabs.io/privacy HTTP 200 &mdash; DevRel + open-source-maintainer inbox).</p>
<p><strong>+ template 436_elevenlabs.md</strong> (5-question voice-agent audit opener: per-conversation-id provenance join-table SOC 2 CC7.2 + EU AI Act Art. 12, per-Voice-Clone-consent-verification + per-Voice-Library-creator-id + per-Voice-Design-attribute-validation vendor-DD, per-Voice-Clone-training-data-provenance + per-Voice-Library-content-moderation + per-deepfake-watermark defense, cross-ElevenLabs-tenant + per-Voice-Clone-id isolation evidence, per-Voice-Isolator-input-id + per-Sound-Effects-output-id + per-Dubbing-Studio-tampering-id voice-AI-specific attack coverage matrix per MITRE ATLAS + EU AI Act Art. 15).</p>
<p><strong>+ index.html inlined chunk-264 (SoundHound 435) + chunk-265 (ElevenLabs 436)</strong> (cross-tick inlining regression fix: tick 1330Z shipped SoundHound chunk_264 source + public + sitemap but missed index.html inline summary &mdash; this tick catches it + adds ElevenLabs 436 inline).</p>
<p><strong>+ sitemap.xml chunk_264 + chunk_265 entries</strong> (sitemap previously had chunk_263 as last entry &mdash; this tick backfills chunk_264 + adds chunk_265 with lastmod 2026-07-17).</p>
<p><strong>voice_agents cohort now 10-vendor-deep</strong>: Voiceflow 427 + Lindy AI 428 + Retell AI 429 + Vapi 430 + Bland AI 431 + Synthflow 432 + PolyAI 433 + Deepgram 434 + SoundHound 435 + ElevenLabs 436. Cohort ceiling delta <strong>+$500 audit / +$497/mo MRR</strong>; cohort now caps at $5,000 audit / $4,970/mo MRR if 10-vendor voice_agents cohort closes.</p>
<p><strong>Tick 1355Z shipped:</strong> 3 files modified (leads.csv + leads_with_emails.csv + template 436_elevenlabs.md + _chunks/chunk_265.html + chunks/chunk_265.html + sitemap.xml + index.html + build-log.html).</p>
</div>
'''

text = BUILD_LOG.read_text(encoding="utf-8")

# Variant detection
assert text.startswith('<div class="tick-entry"'), f"Unexpected build-log head: {text[:80]!r}"

# Find the FIRST <div class="tick-entry" (the newest entry) — we want to insert before it
first_idx = text.find('<div class="tick-entry"')
assert first_idx == 0, f"First tick-entry not at offset 0 (was {first_idx})"

# Verify no duplicate tick
assert 'data-tick="2026-07-17-1355Z"' not in text, "duplicate tick"

new_text = ENTRY + text
BUILD_LOG.write_text(new_text, encoding="utf-8")
print(f"Prepended tick 1355Z (entry len={len(ENTRY)}), new file size={len(new_text)}")

# Verify
v = BUILD_LOG.read_text(encoding="utf-8")
assert v.startswith('<div class="tick-entry" data-tick="2026-07-17-1355Z"'), "tick not at top"
assert v.count('data-tick="2026-07-17-1355Z"') == 1
print("OK build-log prepended, single tick 1355Z at top")
