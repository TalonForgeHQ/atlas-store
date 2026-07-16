From: james@talonforge.io
To: security@bardeen.ai
Subject: Bardeen AI Browser Agent + Magic Box + Autobook — 5 questions before we route our workflow-automation audit cohort to you

Hi Bardeen security team,

I'm James Potts, founder of Talon Forge. We run a 50-customer AI-agent audit practice (SOC 2 Type II + HIPAA + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS coverage) and we're now sending our clients to Bardeen as the canonical workflow_automation_ai_agents surface — browser-automation + no-code workflows + AI-agent-CRM-sync + data-enrichment + outreach-sequencer. Three of our recent audit subjects — Clay, Persana, and an in-house RevOps pipeline — all evaluate Bardeen AI Browser Agent + Magic Box + Autobook against competitive browser-automation offerings (Zapier + Make + n8n + Workato + Tonkean), and we want to make sure our enterprise audit-template lines up with your actual control surface before we send our first joint customer your way.

I have five vendor-DD questions I'd like to walk through with your security/GRC team (30-min Zoom, your time):

1. Per-workflow provenance — can you share the canonical join-table for per-workflow-id → per-trigger-id → per-action-id → per-browser-step-id → per-scraper-id → per-form-fill-id → per-CRM-write-id → per-Slack-message-id → per-webhook-delivery-id → per-billing-event-id → per-credential-access-id lineage? Our audit-template uses 60+ columns and we want to make sure we're not missing Bardeen-specific events like Magic Box AI-decision steps or Autobook scheduled-job runs.

2. Prompt-injection + adversarial-page defense — Bardeen reads arbitrary third-party web pages and executes browser actions on behalf of users. How do you defend against prompt injection in scraped content, per-browser-page-poisoning, per-scraper-payload-poisoning, per-form-fill-value-poisoning, per-CRM-record-poisoning (writing attacker-controlled data to Salesforce / HubSpot / Pipedrive), and per-Slack-message-poisoning (writing attacker-controlled messages to internal Slack)? We benchmark against OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15 + NIST AI RMF MEASURE.

3. Cross-region browser-execution-data-residency — for EU + India + Brazil + UAE + Australia + Canada + UK + Singapore + Japan + Philippines customers, what's the per-customer-region selection mechanism for browser-execution + scraped-data-storage + workflow-state-storage, and is it auditable in your customer-facing logs? We're auditing against Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Philippines DPA + Japan APPI.

4. HIPAA-eligible Bardeen for healthcare-RevOps — if your healthcare customers want to use Bardeen for HIPAA-covered workflows (e.g. patient-intake-form-fills, provider-CRM-sync, payer-portal-scraping), can you walk us through the BAA-ready configuration, per-credential-id PHI-flag handling, per-scraper-id CMK/BYOK encryption, and per-browser-session-id BAA-isolation? HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b) is the floor.

5. Cross-tenant isolation — for Bardeen Cloud + Bardeen Enterprise + Bardeen Self-hosted + per-workspace-id + per-team-id + per-user-id + per-API-key-id + per-credential-id + per-browser-session-id isolation evidence, can you share the most recent SOC 2 Type II report (CC6.1) + GDPR DPA (Art. 28) + EU AI Act readiness statement? Especially interested in how user-stored credentials (Salesforce OAuth tokens, HubSpot API keys, LinkedIn session cookies, Gmail App Passwords) are isolated across tenants.

If a 30-min Zoom is too much friction, I'm also happy to do a written Q&A over email. Our standard vendor-DD SLA is 5 business days, and we won't share your answers outside our audit subject's GRC team.

If Bardeen isn't the right contact for any of these, I'd appreciate a redirect to your security/GRC lead. Either way, thanks for your time — looking forward to working together.

Best,
James Potts
Founder, Talon Forge LLC
james@talonforge.io
https://talonforge.io