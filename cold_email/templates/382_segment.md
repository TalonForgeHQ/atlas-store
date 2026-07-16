From: james@talonforge.io
To: privacy@twilio.com
Subject: Twilio Segment + Twilio Voice/SMS/Flex — 5 questions before we route our CDP audit cohort to you

Hi Twilio Segment privacy/security team,

I'm James Potts, founder of Talon Forge. We run a 50-customer voice-AI-agent + customer-data-platform audit practice (SOC 2 Type II + HIPAA + EU AI Act + GDPR DPA + CCPA/CPRA + ISO 27001/27017/27018 + OWASP LLM Top 10 + MITRE ATLAS coverage) and we're now sending our clients to Twilio Segment as the canonical CDP backbone + Twilio Voice/SMS/WhatsApp/Verify/Flex as the canonical customer-engagement-channel surface for the customer_data_platform_cdp cohort. Three of our recent audit subjects — mParticle 257 (CDP sibling), Heap Illuminate 284 (auto-capture analytics + Connect), Amplitude 283 (product analytics + Amplitude AI) — all evaluate Twilio Segment's Connections + Protocols + Personas + Functions + Journeys + Twilio Engage against competitive CDP offerings, and we want to make sure our enterprise audit-template lines up with your actual control surface before we send our first joint customer your way.

I have five vendor-DD questions I'd like to walk through with your security/GRC team (30-min Zoom, your time):

1. Per-event provenance — can you share the canonical join-table for per-event-id → per-track-id → per-page-id → per-screen-id → per-user-id → per-anonymous-id → per-identity-merge-id → per-source-of-truth-id → per-destination-sync-id → per-Twilio-channel-delivery-id → per-Voice-call-id → per-SMS-message-id → per-email-message-id → per-WhatsApp-message-id → per-Verify-verification-id → per-Flex-task-id → per-Segment-AI-Assist-decision-id → per-Segment-Functions-execution-id → per-downstream-CDP-state-change-id lineage? Our audit-template uses 60+ columns and we want to make sure we're not missing Segment-specific events like identity-merge decisions or per-Functions invocation rows.

2. Prompt-injection + per-event-poisoning + per-identity-merge-poisoning defense — Twilio Segment Functions + Segment AI Assist + Twilio Voice/Voicebot + Twilio Flex Insights ingest user events that get fed into downstream AI agents + LLM pipelines. How do you defend against adversarial payloads (per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06 + MITRE ATLAS + EU AI Act Art. 15)? Specifically — per-event-poisoning, per-identity-merge-poisoning, per-Personas-computation-poisoning, per-Journeys-trigger-poisoning, per-AI-Assist-prompt-poisoning, per-Functions-payload-poisoning, per-Voice-call-prompt-poisoning, per-SMS-content-poisoning, per-email-content-poisoning.

3. Cross-region customer-data-residency — Twilio Segment supports EU + US + Sydney regions. For EU + India + Brazil + UAE + Australia + Canada + UK + Singapore + Japan + Philippines customers, what's the per-customer-region selection mechanism for the Segment CDP bucket + Twilio Voice recording bucket + Twilio SMS message store + Twilio Conversations log, and is per-region selection auditable in customer-facing logs? We're auditing against Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Philippines DPA + Japan APPI.

4. HIPAA-eligible Twilio Segment + Twilio Voice + Twilio SMS + Twilio Conversations + Twilio Verify + Twilio Flex — Twilio is HIPAA-eligible since 2018 per twilio.com/en-us/legal/hipaa-eligible-products-and-services. For BAA-covered healthcare customers using Segment CDP + Twilio Voice/SMS/Conversations in PHI pipelines, can you walk us through the per-event-id PHI-flag + per-Voice-call-id CMK/BYOK encryption + per-Flex-task-id BAA-ready configuration? HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b) is the floor.

5. Cross-tenant isolation — for Twilio Segment + Twilio Voice + Twilio SMS + Twilio Conversations + Twilio Verify + Twilio Flex + Twilio Frontline + Twilio Studio + Twilio SendGrid + per-workspace-id + per-account-id + per-project-id + per-API-key-id + per-Segment-source-id + per-Segment-destination-id isolation evidence, can you share the most recent SOC 2 Type II report (CC6.1) + ISO 27001/27017/27018 statements + GDPR DPA (Art. 28) + EU AI Act readiness statement + HIPAA BAA template?

If a 30-min Zoom is too much friction, I'm also happy to do a written Q&A over email. Our standard vendor-DD SLA is 5 business days, and we won't share your answers outside our audit subject's GRC team.

If Twilio Segment isn't the right contact for any of these, I'd appreciate a redirect to your security/GRC lead (or to Segment's separate GRC team if one exists post-acquisition). Either way, thanks for your time — looking forward to working together.

Best,
James Potts
Founder, Talon Forge LLC
james@talonforge.io
https://talonforge.io