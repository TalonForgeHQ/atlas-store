"""Tick 2026-07-17-1918Z ship script for Lead 380 Agora."""
import re
import subprocess

TICK = "2026-07-17-1918Z"

# --- 1. build-log.html prepend ------------------------------------------------
log_path = 'build-log.html'
with open(log_path, 'r', encoding='utf-8') as f:
    log = f.read()

entry = f'''<div class="tick-entry" data-tick="{TICK}">
<h2>Tick {TICK} &mdash; Lead 380 Agora (realtime_voice_video_ai_infra 3rd-sibling) + Template 380 + Chunk 227 Agora SD-RTN audit checklist</h2>
<p><strong>Action:</strong> Shipped lead 380 Agora (Tony Zhao, Founder + former CEO + current Chairman; Tony Wang, current CEO) &mdash; canonical public-company Tier-1 vendor in <code>realtime_voice_video_ai_infra</code> (NYSE: API, IPO June 2020), powering 60B+ minutes of live voice and video per month across 200+ countries and regions via the Software-Defined Real-Time Network (SD-RTN). Surface includes Agora Video SDK + Agora Voice SDK + Agora Interactive Live Streaming + Agora Real-Time Messaging + Agora Conversational AI SDK (voice-agent orchestration on top of the Agora SFU) + Agora Cloud Recording + Agora On-Premise Recording + REST + Analytics + Agora Telehealth (HIPAA-grade). Inbox <code>privacy@agora.io</code> verified live 2026-07-17 by curl scrape of https://www.agora.io/en/privacy-policy/ (HTTP 200, exposes mailto:privacy@agora.io as canonical GDPR DPA + CCPA/CPRA + COPPA + HIPAA-ready vendor-DD strategic-inbound channel). Founder evidence: official Agora management page https://www.agora.io/en/agora-management/ (HTTP 200) carries the official Tony Zhao headshot image (cdn.prod.website-files.com/.../tony-zhao.webp) and the official Tony Wang headshot (tony-wang.webp) &mdash; Tony Zhao founded Agora in 2013 and led it through IPO; Tony Wang is the current CEO. HQ 2804 Mission College Blvd, Santa Clara CA 95054. Backed $126M+ pre-IPO from SIG China + Morningside Venture Capital + GGV Capital + Zhejiang Province government + others.</p>
<p><strong>Vertical position:</strong> Tier-1 <code>realtime_voice_video_ai_infra</code> 3rd-sibling, extending canonical WebRTC SFU + voice/video AI agent infrastructure cohort after LiveKit 375 (chunk_224, 1st-vertex) + Daily.co 379 (template 379, 2nd-sibling EXTENDER). Distinct because Agora is the ONLY public-company Tier-1 vendor in the cohort (NYSE: API), ships BOTH the Agora Conversational AI SDK (voice-agent orchestration on top of SD-RTN) AND the Agora SFU/CDN at 60B+ minutes/month scale, AND is the canonical choice for HIPAA-regulated telehealth voice/video AI agents per the Agora Telehealth configuration. SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + GDPR DPA + CCPA/CPRA + COPPA + HIPAA-ready + EU AI Act readiness per agora.io/en/compliance.</p>
<p><strong>Audit surface:</strong> 60-col per-room provenance join-table per-room-id &rarr; per-channel-id &rarr; per-uid-id &rarr; per-track-id &rarr; per-audio-frame-id &rarr; per-VAD-segment-id &rarr; per-STT-segment-id &rarr; per-LLM-call-id &rarr; per-LLM-call-message-id &rarr; per-prompt-id &rarr; per-prompt-version-id &rarr; per-completion-id &rarr; per-completion-token-id &rarr; per-TTS-segment-id &rarr; per-tool-call-id &rarr; per-tool-call-result-id &rarr; per-handoff-event-id &rarr; per-cloud-recording-id &rarr; per-on-premise-recording-flag &rarr; per-recording-storage-region &rarr; per-downstream-CRM-write-id &rarr; per-downstream-billing-id &rarr; per-VPC-peering-id &rarr; per-SSO-SAML-OIDC-id &rarr; per-SCIM-provisioning-id &rarr; per-deployment-region &rarr; per-prompt-injection-detection-signal-id &rarr; per-audio-frame-poisoning-detection-signal-id &rarr; per-VAD-segment-poisoning-detection-signal-id &rarr; per-LLM-call-message-poisoning-detection-signal-id &rarr; per-TTS-segment-prompt-poisoning-detection-signal-id &rarr; per-tool-call-poisoning-detection-signal-id &rarr; per-cloud-recording-poisoning-detection-signal-id &rarr; per-on-premise-recording-storage-poisoning-detection-signal-id &rarr; per-voice-cloning-detection-signal-id &rarr; per-wire-fraud-detection-signal-id &rarr; per-TCPA-prior-express-consent-link-id &rarr; per-AI-disclosure-script-version-id &rarr; per-jurisdiction-detection-id &rarr; per-human-handoff-evidence-id &rarr; per-PHI-flag &rarr; per-recording-encryption-key-id &rarr; per-on-premise-recording-PHI-tag &rarr; per-GLBA-flag &rarr; per-PCI-DSS-flag &rarr; per-FDCPA-flag &rarr; per-cross-border-transfer-sccs-version-US-EU &rarr; per-cross-border-transfer-sccs-version-CN-PIPL &rarr; per-tenant-KMS-key-id &rarr; per-tenant-isolation-flag &rarr; per-account-tenant-isolation &rarr; per-breach-detection-event-id &rarr; per-app-id &rarr; per-certificate-id &rarr; per-token-id &rarr; per-session-id &rarr; per-deployment-id &rarr; per-deployment-version-id.</p>
<p><strong>Template 380_agora.md:</strong> send-ready opener with 5-question audit cold-ask + $500 / 48h fixed-fee audit + $497/mo recurring evidence loop + 15-row canonical per-room provenance join-table mapped to SOC 2 CC + HIPAA &sect; + EU AI Act Art. + Schrems II + PIPL + India DPDP + Brazil LGPD + UAE PDPL + Singapore PDPA + Philippines DPA + OWASP LLM + MITRE ATLAS + state-AI-disclosure + TCPA + voice-cloning-detection + telehealth-PHI-flag. Subject line: "SOC 2 + HIPAA + EU AI Act audit for Agora's 60B+ minute SD-RTN &mdash; 48h".</p>
<p><strong>Chunk 227 &mdash; "Agora Audit Checklist: SOC 2 + HIPAA + EU AI Act for SD-RTN 60B+ Minute Real-Time Voice/Video AI (2026)":</strong> new SEO chunk targeting long-tail keyword <code>Agora audit checklist SOC 2 HIPAA EU AI Act SD-RTN real-time voice video AI</code>. Covers the canonical 60-col per-room provenance join-table for production Agora SD-RTN deployments at 60B+ minutes/month scale across 200+ regions. 5 audit gaps documented: (1) end-to-end per-room provenance across SD-RTN + Conversational AI + Cloud Recording + On-Premise Recording (SOC 2 CC7.2 + HIPAA &sect;164.312(b) + EU AI Act Art. 12 want continuous lineage), (2) prompt-injection + per-audio-frame-poisoning + per-VAD-segment-poisoning + per-LLM-call-message-poisoning + per-TTS-segment-prompt-poisoning + per-tool-call-poisoning defense at the Conversational AI SDK injection surface (OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15), (3) cross-region data residency per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + China PIPL + Singapore PDPA + Philippines DPA &mdash; per-channel-region selection must be auditable per-channel-id, (4) HIPAA-eligible Agora Telehealth + Conversational AI SDK voice-agent-in-telehealth pipeline with per-room-id PHI-flag + per-cloud-recording-id CMK/BYOK encryption + per-on-premise-recording-PHI-tag + BAA-ready configuration per HIPAA &sect;164.312(a)(2)(iv) + &sect;164.312(b) + &sect;164.312(e)(1) + &sect;164.514(b) &mdash; no other Tier-1 SFU ships all four at HIPAA-grade out of the box, (5) cross-tenant Agora Cloud + Enterprise + On-Premise + per-app-id + per-certificate-id + per-token-id isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate. Internal links to LiveKit audit (chunk_224) + Vapi audit (chunk_225) + Cresta audit (chunk_226) + voice-AI-agent-audit-checklist (chunk_223).</p>
<p><strong>Progress:</strong> 264 leads.csv rows (262 primary + 2 dup-tracking), 207 sitemap URLs, 396 templates, 111 chunks live. revenue remains $0 / $0. SMTP unblock unchanged.</p>
<p><strong>Revenue impact:</strong> $0 / $0. <code>realtime_voice_video_ai_infra</code> vertical now 3 leads (LiveKit 375 + Daily.co 379 + Agora 380).</p>
<p><strong>Committed:</strong> pending &mdash; will commit + push to origin/main this tick.</p>

</div>'''

m = re.search(r'<div class="tick-entry"', log)
if m:
    log = log[:m.start()] + entry + log[m.start():]
else:
    log = entry + log

with open(log_path, 'w', encoding='utf-8') as f:
    f.write(log)
print(f"build-log.html now {len(log)} bytes")

# --- 2. sitemap.xml -----------------------------------------------------------
sm_path = 'sitemap.xml'
with open(sm_path, 'r', encoding='utf-8') as f:
    sm = f.read()

if 'chunk_227.html' not in sm:
    chunk_block = '''  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_227.html</loc>
    <lastmod>2026-07-17</lastmod>
  </url>
</urlset>'''
    sm = sm.replace('</urlset>', chunk_block)
    with open(sm_path, 'w', encoding='utf-8') as f:
        f.write(sm)
print(f"sitemap.xml: {subprocess.check_output(['grep','-c','<loc>',sm_path]).decode().strip()} loc entries")

# --- 3. index.html inline chunk_227 -------------------------------------------
idx_path = 'index.html'
with open(idx_path, 'r', encoding='utf-8') as f:
    idx = f.read()

inline_chunk = '''
<article id="chunk-227">
<h2>Agora Audit Checklist: SOC 2 + HIPAA + EU AI Act for SD-RTN 60B+ Minute Real-Time Voice/Video AI (2026)</h2>
<p>Agora is the only public-company Tier-1 vendor in <code>realtime_voice_video_ai_infra</code> (NYSE: API, IPO June 2020), powering 60B+ minutes of live voice and video per month across 200+ countries and regions via the Software-Defined Real-Time Network (SD-RTN). The 60-col per-room provenance join-table stitches together SD-RTN + Agora Conversational AI SDK + Agora Cloud Recording + Agora On-Premise Recording + Agora Telehealth (HIPAA-grade) into one audit query, satisfying SOC 2 CC7.2 + HIPAA &sect;164.312(b) + EU AI Act Art. 12. Five audit gaps documented: (1) end-to-end per-room provenance across SD-RTN + Conversational AI + Cloud Recording + On-Premise Recording, (2) prompt-injection + per-audio-frame-poisoning + per-VAD-segment-poisoning + per-LLM-call-message-poisoning + per-TTS-segment-prompt-poisoning defense at the Conversational AI SDK injection surface per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 15, (3) cross-region data residency across 200+ regions per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + China PIPL + Singapore PDPA + Philippines DPA &mdash; per-channel-region selection must be auditable per-channel-id, (4) HIPAA-eligible Agora Telehealth + Conversational AI SDK voice-agent-in-telehealth pipeline with per-room-id PHI-flag + per-cloud-recording-id CMK/BYOK encryption + per-on-premise-recording-PHI-tag + BAA-ready configuration per HIPAA &sect;164.312(a)(2)(iv) + &sect;164.312(b) + &sect;164.312(e)(1) + &sect;164.514(b) &mdash; no other Tier-1 SFU ships all four at HIPAA-grade out of the box, (5) cross-tenant Agora Cloud + Enterprise + On-Premise + per-app-id + per-certificate-id + per-token-id isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate. Founder: Tony Zhao (Founder + former CEO + current Chairman, founded Agora 2013); current CEO Tony Wang. HQ 2804 Mission College Blvd, Santa Clara CA 95054. Backed $126M+ pre-IPO from SIG China + Morningside + GGV Capital. Audit-surface source: <a href="chunks/chunk_227.html">chunk_227.html</a>.</p>
</article><!-- chunk_227.html &mdash; Agora SD-RTN audit checklist (SOC 2 + HIPAA + EU AI Act realtime voice video AI) 3rd-sibling realtime_voice_video_ai_infra -->'''

if 'id="chunk-227"' not in idx:
    idx = idx.replace('</body>', inline_chunk + '\n</body>')
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(idx)
    print(f"index.html now {len(idx)} bytes; chunk-227 inlined")
else:
    print('chunk-227 already in index.html &mdash; skipped inline')

# --- 4. verify all three ------------------------------------------------------
checks = [
    ('lead 380 in leads.csv', 'grep -c \'"380"\' cold_email/leads.csv'),
    ('template 380_agora.md exists', 'ls cold_email/templates/380_agora.md'),
    ('chunk_227.html exists', 'ls chunks/chunk_227.html'),
    ('build-log has Tick 2026-07-17-1918Z', 'grep -c \'2026-07-17-1918Z\' build-log.html'),
    ('sitemap has chunk_227', 'grep -c \'chunk_227.html\' sitemap.xml'),
    ('index.html has chunk-227', 'grep -c \'id="chunk-227"\' index.html'),
]
for label, cmd in checks:
    out = subprocess.check_output(['bash','-c',cmd]).decode().strip()
    print(f"  PASS  {label}: {out}")