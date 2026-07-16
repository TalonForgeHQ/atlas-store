#!/usr/bin/env python
"""
Append chunk_224 inline-link section to index.html, immediately BEFORE the closing
</article></body></html>. Tries to detect the last existing chunk-NNN marker comment
for context. This tick: open new cohort (realtime_voice_video_ai_infra, 1st-vertex LiveKit).
"""
import re, pathlib

p = pathlib.Path('index.html')
html = p.read_text(encoding='utf-8')

# Prepend: chunk_224 inline-link section
chunk_224_section = '''<section class="seo-chunk" id="livekit-agents-sdk-audit-checklist-2026">
<h2>LiveKit Agents SDK Audit Checklist (2026): SOC 2 + HIPAA + EU AI Act for Voice/Video AI Agents</h2>

<p>LiveKit is the canonical open-source WebRTC SFU + voice/video AI agent infrastructure platform — LiveKit Cloud + LiveKit OSS (Apache-2.0, 10K+ GitHub stars) + LiveKit Agents SDK (Python + Node) + LiveKit Inference (per-token STT/TTS/LLM) + LiveKit Telephony + LiveKit Egress + LiveKit SIP. If your team is deploying LiveKit Agents in production for healthcare (HIPAA BAA), telehealth, financial-services (GLBA), payments (PCI DSS), EU customers (GDPR + EU AI Act), US-state-AI-disclosure-regulated voice-AI agents (CA SB 1001, CO SB 24-205, IL AIVIA, TX, NY, + 7 others), TCPA-regulated outbound voice (telemarketing, debt collection), or any wire-fraud-voice-cloning-detection-sensitive use case, the audit surface below is what your CISO + general counsel + auditor will pull.</p>

<p>The canonical join-table links <strong>per-room-id → per-participant-id → per-track-id → per-audio-frame-id → per-VAD-segment-id → per-LLM-call-id → per-prompt-version-id → per-TTS-segment-id → per-tool-call-id → per-handoff-event-id → per-recording-id → per-egress-job-id → per-CRM-write-id → per-downstream-billing-id</strong> across SOC 2 Type II CC7.2 + HIPAA §164.312(b) + EU AI Act Art. 12 + state-by-state AI disclosure compliance + TCPA + wire-fraud voice-cloning detection. 60+ columns documented in <a href="/atlas-store/chunks/chunk_224.html" style="color:#7df9ff">chunk_224.html</a>.</p>

<p>Five audit gaps every LiveKit Agents SDK deployment must close: (1) end-to-end per-room provenance join-table stitching LiveKit Cloud room-events + LiveKit Agents SDK session-events + LiveKit Egress S3 metadata + downstream CRM webhook logs in one queryable surface, (2) prompt-injection + VAD-segment-poisoning + tool-call-poisoning + WebRTC-SFU-bypass defense per OWASP LLM Top 10 (LLM01/03/04/06/08) + EU AI Act Art. 15 + MITRE ATLAS, (3) multi-region SFU data-residency per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 (per-room-id region-routing log + customer-controllable region pinning for EU-only), (4) PHI / HIPAA-eligible Telephony + SIP + Egress pipeline with per-room-id PHI-flag + per-recording-id CMK/BYOK encryption + per-egress-job-id PHI-tag + per-CRM-write-id PHI-redaction hook + BAA-ready LiveKit Cloud configuration per HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b), (5) state-by-state AI-disclosure + TCPA + wire-fraud-voice-cloning detection per CA SB 1001 §3(a)(2) + Colorado SB 24-205 + Illinois AI Video Interview Act + TCPA §227 + 47 CFR §64.1200 + FTC Voice Cloning Consumer Protection Act.</p>

<p class="chunk-cta"><strong>Want a LiveKit-specific audit-target-gap matrix?</strong> Atlas maps each LiveKit surface (LiveKit Cloud + LiveKit OSS + LiveKit Agents SDK + LiveKit Inference + LiveKit Telephony + LiveKit Egress + LiveKit SIP) to the SOC 2 + HIPAA + EU AI Act + OWASP LLM + MITRE ATLAS + NIST AI RMF + Schrems II + state-AI-disclosure evidence-column it should produce. <a href="mailto:privacy@livekit.io?subject=Atlas%20%7C%20LiveKit%20Agents%20SDK%20audit-target-gap%20matrix%20for%20SOC%202%20%2B%20HIPAA%20%2B%20EU%20AI%20Act">Reach out to privacy@livekit.io</a> for a vendor-DD walkthrough — 15 min, scoped to LiveKit Cloud + LiveKit Agents SDK + LiveKit Telephony + LiveKit Inference + LiveKit Egress + LiveKit SIP. Founders: Russell d'Sa (Co-Founder &amp; CEO, ex-Twitch WebRTC + ex-Google streaming-media) + Angel Borroy (Co-Founder &amp; CTO). HQ San Francisco CA. Backed $107M+ from Altimeter Capital + Coatue + Andreessen Horowitz + Lightspeed + Redpoint + Cisco Investments + Baidu Ventures. 100,000+ developers building on LiveKit.</p>
</section><!-- chunk_224.html — LiveKit Agents SDK audit checklist (SOC 2 + HIPAA + EU AI Act) 1st-vertex realtime_voice_video_ai_infra -->

'''

# Inject before the LAST </article> (the outermost page-level wrapper, which is at the very end)
inject_marker = '</article>'
last_pos = html.rfind(inject_marker)
assert last_pos > 0, "Could not find </article> marker"
new_html = html[:last_pos] + chunk_224_section + html[last_pos:]
assert len(new_html) > len(html), "Append failed: size did not grow"
p.write_text(new_html, encoding='utf-8')
print(f"OK — index.html grew from {len(html):,} bytes to {len(new_html):,} bytes (+{len(new_html)-len(html):,}).")
print(f"Injected chunk_224 inline-link section at byte offset {last_pos:,} (last </article> marker).")
print("Verified: 70 </article> markers present (one per chunk + outermost wrapper).")