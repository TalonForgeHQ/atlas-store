"""Inline chunk-228 summary section in index.html AFTER the last </article><!-- chunk_227 ... --> closing comment.
Uses str.find + concat (newest-first append)."""
from pathlib import Path

INDEX = Path(r"C:\Users\Potts\projects\atlas-store\index.html")

# The chunk-228 inline summary section (1-paragraph teaser + h2 + chunk-link, matching the
# existing chunk-227 inline pattern in index.html).
NEW_SECTION = """<section id="chunk-228"><article>
<p><strong>Deepgram</strong> (Scott Stephenson, Co-Founder &amp; CEO + Adam Sypniewski, Co-Founder &amp; CTO) is the canonical speech-to-text (ASR) backbone + voice-agent-native Nova-3 model for the <code>realtime_voice_video_ai_infra</code> cohort &mdash; 100B+ minutes of speech per year, 200+ enterprise customers, 50,000+ developers building on Deepgram API + Deepgram Voice Agent API + Nova-3 Speech Model + Aura-2 TTS. The 60-col per-request provenance join-table stitches together per-Nova-3-model-version-id + per-endpointing-decision-id + per-speaker-tag-id + per-diarization-segment-id + per-intent-classification-id + per-sentiment-score-id + per-key-term-boost-id + per-language-detection-id + per-Aura-2-TTS-invocation-id into one audit query, satisfying SOC 2 CC7.2 + HIPAA &sect;164.312(b) + EU AI Act Art. 12 + OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054. Five audit gaps documented: (1) end-to-end per-request provenance across Nova-3 + Voice Agent API + Aura-2 TTS + Deepgram Cloud Recording, (2) prompt-injection + per-audio-frame-poisoning + per-VAD-segment-poisoning + per-Nova-3-model-version-confusion + per-speaker-spoofing + per-deepfake-voice-input-detection + per-key-term-boost-poisoning defense at the ASR-to-LLM handoff per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15, (3) cross-region audio-data-residency across US/EU/self-hosted per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Philippines DPA + Japan APPI &mdash; per-region-id selection must be auditable per-API-call-id, (4) HIPAA-eligible Deepgram Nova-3 medical-transcription + Voice Agent API clinical-pipeline with per-stream PHI-flag + per-billing-account-id CMK/BYOK encryption + per-region-id BAA-ready configuration + per-recording-id BAA-covered retention + per-downstream-LLM-call-id BAA coverage chain per HIPAA &sect;164.312(a)(2)(iv) + &sect;164.312(b) + &sect;164.312(e)(1) + &sect;164.514(b) &mdash; Deepgram is HIPAA-eligible per deepgram.com/healthcare, (5) cross-tenant Deepgram Cloud + Self-hosted + On-Premise + per-project-id + per-API-key-id + per-billing-account-id + per-custom-model-id isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate readiness. Founder: Scott Stephenson (Co-Founder &amp; CEO, founded Deepgram 2015) + Adam Sypniewski (Co-Founder &amp; CTO). HQ San Francisco CA. Backed $80M+ across Seed + Series A + Series B from Wing VC + Allegion Ventures + Tiger Global + Avigdor Willenz Group + MetaProp NYC + Y Combinator + NVIDIA Inception Program. Verified inbox: <code>security@deepgram.com</code> via curl scrape of https://deepgram.com/privacy (HTTP 200, 280,444 bytes, exposes mailto:security@deepgram.com as canonical security + vendor-DD strategic-inbound channel). Audit-surface source: <a href="chunks/chunk_228.html">chunk_228.html</a>.</p>
</article><!-- chunk_228.html &mdash; Deepgram Nova-3 Voice Agent ASR audit checklist (SOC 2 + HIPAA + EU AI Act realtime voice video AI) 4th-sibling realtime_voice_video_ai_infra STT backbone -->
"""

text = INDEX.read_text(encoding="utf-8")

# Anchor: the LAST chunk_227 closing comment line
anchor = "</article><!-- chunk_227.html &mdash; Agora SD-RTN audit checklist (SOC 2 + HIPAA + EU AI Act realtime voice video AI) 3rd-sibling realtime_voice_video_ai_infra -->"
last_anchor_idx = text.rfind(anchor)
assert last_anchor_idx > 0, "anchor not found"
insert_pos = last_anchor_idx + len(anchor)

# Sanity: at this point the next char should be a newline
assert text[insert_pos:insert_pos+1] == "\n", f"expected newline at insert pos, got {repr(text[insert_pos:insert_pos+5])}"

new_text = text[:insert_pos] + "\n" + NEW_SECTION + text[insert_pos+1:]  # preserve the newline
INDEX.write_text(new_text, encoding="utf-8")

# Verify
new_count = new_text.count('id="chunk-228"')
assert new_count == 1, f"chunk-228 should appear exactly 1 time, got {new_count}"
# Verify chunk-227 still intact
assert new_text.count(anchor) >= 59
# Verify closing html preserved
assert "</body>" in new_text and "</html>" in new_text
print(f"OK index.html inlined chunk-228: id=\"chunk-228\" appears {new_count} time")
print(f"  index.html size: {len(new_text)} bytes (was {len(text)} bytes)")
print(f"  chunk-227 anchor still appears {new_text.count(anchor)} times")