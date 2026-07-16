import os

# 1. Prepend build-log tick entry
TICK = '''<div class="tick-entry" data-tick="2026-07-17-1855Z">
<h2>Tick 2026-07-17-1855Z — Lead 377 Vapi (ai_voice_agents_orchestration 3rd-sibling) + Template 377 + Chunk 225 Vapi audit checklist</h2>
<p><strong>Action:</strong> Shipped lead 377 Vapi (Jordan Dearsley, Founder &amp; CEO) — canonical developer-platform voice-AI orchestration surface for production phone agents + Composer + Monitoring + Simulations + fleet mode + 1M+ developers + 1B+ calls handled + Series B May 2026. Inbox <code>support@vapi.ai</code> verified live 2026-07-17 by curl scrape of https://vapi.ai/privacy (HTTP 200, 28,248 bytes) exposing mailto:support@vapi.ai as canonical support channel. Security channel <code>infosec@vapi.ai</code> verified live 2026-07-17 by curl scrape of https://security.vapi.ai/ (HTTP 200, 370,502 bytes). Founder evidence: official Vapi blog post https://vapi.ai/blog/series-b ("AGI is here. Why am I still on hold?" — published 2026-05-12, JSON-LD article:author = "Jordan Dearsley") identifies Jordan Dearsley as Founder &amp; CEO, signed — Jordan at post end. HQ San Francisco CA. Founded 2020. Backed across Series A + Series B (May 2026 announcement).</p>
<p><strong>Audit surface:</strong> 60-col per-call provenance join-table per-call-id → per-agent-id → per-prompt-version-id → per-script-version-id → per-model-id → per-TTS-provider-id → per-STT-provider-id → per-VAD-segment-id → per-tool-call-id → per-handoff-event-id → per-recording-id → per-transcript-id → per-call-summary-id → per-CRM-write-id → per-downstream-billing-id → per-VPC-peering-id → per-SSO-SAML-OIDC-id → per-SCIM-provisioning-id → per-deployment-region → per-telephony-provider-id → per-phone-number-id → per-TCPA-prior-express-consent-link-id → per-AI-disclosure-script-version-id → per-jurisdiction-detection-id → per-human-handoff-evidence-id → per-prompt-injection-detection-signal-id → per-voice-cloning-detection-signal-id → per-wire-fraud-detection-signal-id → per-PHI-flag → per-recording-encryption-key-id → per-GLBA-flag → per-PCI-DSS-flag → per-FDCPA-flag → per-cross-border-transfer-sccs-version-US-EU → per-tenant-KMS-key-id → per-monitoring-snapshot-id → per-simulation-run-id → per-improvement-run-id → per-training-data-PHI-redaction-flag → per-fleet-id → per-locale-id → per-deletion-event-id → per-WORM-retention-flag → per-audit-log-export-id → per-breach-detection-event-id → per-API-key-id → per-llm-call-message-id → per-completion-token-id → per-downstream-tool-call-id → per-account-MFA-challenge-id → per-role-id + per-role-permission-id → per-session-id → per-deployment-id.</p>
<p><strong>Vertical position:</strong> Tier-1 <code>ai_voice_agents_orchestration</code> 3rd-sibling, extending canonical cohort after Bland AI 189 + Retell AI 374. SOC 2 Type II + HIPAA + GDPR DPA + CCPA/CPRA + EU AI Act readiness surfaced via security.vapi.ai trust portal + vapi.ai/privacy.</p>
<p><strong>Template 377_vapi.md:</strong> send-ready opener with 5-question audit cold-ask + $500 / 48h fixed-fee audit + $497/mo recurring evidence loop + 15-row canonical per-call provenance join-table mapped to SOC 2 CC + HIPAA § + EU AI Act Art. + state-AI-disclosure + OWASP LLM + voice-cloning-detection. Subject line: "SOC 2 / HIPAA / EU AI Act audit for Vapi's 1B+ call surface — 48h".</p>
<p><strong>Chunk 225 — "Vapi Audit Checklist: SOC 2 + HIPAA + EU AI Act for the 1B+ Call Surface (2026)":</strong> new SEO chunk targeting long-tail keyword <code>Vapi audit checklist SOC 2 HIPAA EU AI Act 1B calls</code>. Covers the canonical 60-col per-call provenance join-table for production Vapi voice-agent deployments at 1B+ calls/year scale. 5 audit gaps documented: (1) end-to-end per-call provenance joining Vapi call-records + Composer prompt-versions + Monitoring snapshots + Simulations runs + telephony legs + downstream CRM/billing, (2) Composer self-improvement loop lineage per EU AI Act Art. 10 data governance + Art. 53(d) model-card lineage + HIPAA §164.514(b) min-necessary on training-set guard, (3) multi-region residency for EU + India + Brazil + UAE + Australia + Pakistan customer cohort per Schrems II + GDPR Art. 28 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL, (4) state-by-state US AI-disclosure for 12 states (CA SB 1001 §3(a)(2) + CO SB 24-205 + IL AIVIA + TX + NY + 7 others), (5) voice-cloning + telephony-input fraud detection at 1B+ calls/year scale per FTC Voice Cloning Consumer Protection + FBI voice-cloning-fraud guidance. Internal links to voice-AI-agent-audit-checklist (chunk_223) + LiveKit audit (chunk_224) + Fathom meeting audit (chunk_221) + Otter.ai meeting audit (chunk_222).</p>
<p><strong>Sitemap updated:</strong> added chunks/chunk_225.html with lastmod 2026-07-17.</p>
<p><strong>Revenue impact:</strong> $0 / $0. Send-ready inventory now 260 primary rows (leads.csv: 259 data rows) + 273 enriched rows (leads_with_emails.csv: 272 data rows) + 394 templates + 109 SEO chunks live (108 + new chunk_225). <code>ai_voice_agents_orchestration</code> vertical now 3 leads (Bland AI 189 + Retell AI 374 + Vapi 377). SMTP unblock unchanged (Gmail App Password / SendGrid / Resend — 5 min user task).</p>
<p><strong>Committed:</strong> pending — will commit + push to origin/main this tick.</p>
</div>'''

with open('build-log.html', 'r') as f:
    build_log = f.read()
# Insert at top after any doctype/head (after first newline after </header> or right after the first <div class="tick-entry")
# Simpler: find first occurrence of <div class="tick-entry" and prepend before it
marker = '<div class="tick-entry" data-tick="2026-07-17-1812Z">'
idx = build_log.find(marker)
if idx == -1:
    raise SystemExit("tick-entry marker not found")
new_build_log = build_log[:idx] + TICK + build_log[idx:]
with open('build-log.html', 'w') as f:
    f.write(new_build_log)
print("Build-log prepended. New first entry is the 2026-07-17-1855Z tick.")

# 2. Inline chunk_225 into index.html — inject before LAST </article>
CHUNK_INLINE = '''<section class="audit-chunk">
<h2>Vapi Audit Checklist — SOC 2 + HIPAA + EU AI Act for the 1B+ Call Surface</h2>
<p><strong>Vapi (vapi.ai)</strong> · Founder &amp; CEO: Jordan Dearsley · Series B May 2026 · 1M+ developers · 1B+ calls handled. Verified inboxes: <code>support@vapi.ai</code> + <code>infosec@vapi.ai</code>. Full audit surface in <a href="/atlas-store/chunks/chunk_225.html" style="color:#7df9ff">chunk_225.html</a>.</p>
<p>The canonical join-table links <strong>per-call-id → per-agent-id → per-prompt-version-id → per-script-version-id → per-model-id → per-TTS-provider-id → per-STT-segment-id → per-tool-call-id → per-handoff-event-id → per-recording-id → per-transcript-id → per-call-summary-id → per-monitoring-snapshot-id → per-simulation-run-id → per-improvement-run-id → per-fleet-id → per-deployment-region → per-TCPA-prior-express-consent-link-id → per-AI-disclosure-script-version-id → per-jurisdiction-detection-id → per-prompt-injection-detection-signal-id → per-voice-cloning-detection-signal-id → per-wire-fraud-detection-signal-id → per-tenant-KMS-key-id → per-WORM-retention-flag</strong> across SOC 2 Type II CC7.2 + HIPAA §164.312(b) + §164.514(b) + EU AI Act Art. 10 + Art. 12 + Art. 14 + Art. 15 + Art. 53(d) + Schrems II + GDPR Art. 28 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + 12-state US AI-disclosure + OWASP LLM Top 10 + MITRE ATLAS. 60+ columns documented in <a href="/atlas-store/chunks/chunk_225.html" style="color:#7df9ff">chunk_225.html</a>.</p>
<p><strong>5 audit gaps specific to Vapi at 1B+ calls scale:</strong> (1) end-to-end per-call provenance joining Vapi call-records + Composer prompt-versions + Monitoring snapshots + Simulations runs + telephony legs + downstream CRM/billing, (2) Composer self-improvement loop lineage per EU AI Act Art. 10 + Art. 53(d) + HIPAA §164.514(b) min-necessary on training-set guard, (3) multi-region residency for EU + India + Brazil + UAE + Australia + Pakistan customer cohort, (4) state-by-state US AI-disclosure for 12 states (CA SB 1001 §3(a)(2) + CO SB 24-205 + IL AIVIA + TX + NY + 7 others), (5) voice-cloning + telephony-input fraud detection at 1B+ calls/year scale per FTC Voice Cloning Consumer Protection Act.</p>
<p><strong>Send-ready:</strong> <code>cold_email/templates/377_vapi.md</code> with $500 / 48h fixed-fee audit offer + $497/mo recurring evidence loop.</p>
</section><!-- chunk_225.html — Vapi voice-agent audit checklist (SOC 2 + HIPAA + EU AI Act) 3rd-sibling ai_voice_agents_orchestration -->'''

with open('index.html', 'r') as f:
    idx_html = f.read()
last_article = idx_html.rfind('</article>')
if last_article == -1:
    raise SystemExit("</article> not found in index.html")
new_idx = idx_html[:last_article] + CHUNK_INLINE + idx_html[last_article:]
with open('index.html', 'w') as f:
    f.write(new_idx)
print("chunk_225 inlined into index.html. New </article> marker count:", new_idx.count('</article>'))