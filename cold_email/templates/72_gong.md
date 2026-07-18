# Lead 72 — Gong

**Vertical:** sales_intel
**Tier:** 1
**Website:** https://www.gong.io/
**Co-founders:** Amit Bendov (CEO) and Eilon Reshef (Chief Product Officer)
**Verified public inboxes:** privacy@gong.io and dpo@gong.io

---

**Subject:** 5 audit questions for Gong's AI revenue workflows

Hi Amit + Eilon,

Gong turns conversations, CRM context, and buyer signals into recommendations that can change forecast calls, account priorities, coaching, and seller behavior. That makes its evidence chain commercially important: when an AI insight affects a deal, can an enterprise reconstruct the source conversation, consent state, model and prompt version, retrieved context, recommendation, user approval, CRM mutation, and downstream outcome?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test on one Gong request-to-revenue-action route:

1. **End-to-end provenance:** Can one export join tenant, workspace, account, opportunity, call or meeting, transcript segment, speaker, consent and recording policy, CRM object, retrieved context, prompt and model version, AI recommendation, human reviewer, downstream mutation, and token or compute cost?
2. **Hostile input and grounding:** What prevents prompt injection, misleading call content, poisoned CRM notes, malicious attachments, or manipulated buyer signals from steering summaries, next steps, coaching, deal-risk scores, or automated actions—and can every claim be traced to its evidence?
3. **Tenant, identity, and secret isolation:** Can customers prove that recordings, transcripts, CRM credentials, model-provider keys, exports, webhooks, and regional data boundaries prevent cross-tenant, cross-workspace, or cross-account leakage?
4. **Change control and human approval:** Are prompt, model, scoring, retrieval, redaction, and automation-policy changes versioned and approval-bound, with a tested path to pause a bad rollout, identify affected insights, and reverse an unsafe CRM side effect?
5. **Incident, retention, and deletion reconstruction:** After a false recommendation, unauthorized recording, leaked transcript, compromised integration, or failed deletion request, can Gong preserve WORM-capable evidence while proving retention and deletion across recordings, transcripts, embeddings, caches, analytics stores, exports, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Articles 5, 6, 22, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; and MITRE ATLAS**. I test one live conversation-to-insight-to-revenue-action route end to end rather than sending a generic checklist.

**Why Gong specifically:** revenue teams increasingly act on AI summaries, recommendations, and forecasts as operational truth. Gong already owns the conversation and CRM context needed to make those actions useful; a defensible evidence spine turns that advantage into a stronger enterprise procurement story.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Gong conversation-to-revenue-action route tested end to end
