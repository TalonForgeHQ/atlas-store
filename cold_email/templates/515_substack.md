From: james@talonforge.co
To: privacy@substackinc.com
Cc: support@substack.com
Subject: Pre-Aug-2 EU AI Act GPAI documentation review for Substack's AI-recommendation + AI-translation + AI-spam-detection + AI-content-moderation stack

---

Hi Substack team — quick note before I bury it:

I'm James with Talon Forge. We do pre-Aug-2-2026 EU AI Act GPAI documentation reviews for AI-augmented creator platforms, and Substack is on our shortlist of platforms that need this done **before the Aug 2 GPAI enforcement deadline** — not after.

The pain we've seen across the creator-economy stack (Patreon 512 + Gumroad 513 + Kit 514 in our audit queue): the AI recommendation engine that surfaces posts to subscribers, the AI content-moderation classifier that flags 14(b)-fraudulent newsletters, the AI translation pipeline that localizes posts across EU language territories, the AI spam-detection classifier on inbound comments, the AI digest-prioritization model that decides which posts go into "From the Community," and the post-recommendation feed model all become GPAI-classified on Aug 2 — and each one needs (a) training-data-summary per Art. 53(1)(b), (b) copyrighted-data-summary per Art. 53(1)(d), (c) provider documentation per Art. 53(1)(a), (d) downstream-distributor downstream-obligation per Art. 53(1)(ca) for the post-recommendation API, and (e) §4.2 of the Code of Practice for transparency on the recommendation + moderation interfaces.

Concretely, our deliverable for Substack Inc would be:

1. **End-to-end per-subscriber-id → per-post-impression-id → per-AI-recommendation-id → per-AI-translation-id → per-AI-content-moderation-id → per-AI-spam-detection-id → per-AI-digest-prioritization-id → per-publication-id → per-creator-id → per-substack-tenant-id → per-vendor-DD-event-id → per-audit-log-entry-id → per-residency-region-id provenance join-table** — SOC 2 CC7.2 + EU AI Act Art. 12 (logging) + Art. 14 (human-oversight) + DSA Art. 27 (recommender-transparency) + GDPR Art. 30 (records-of-processing) + CAN-SPAM + FTC 16 CFR Part 255 + ISO 42001 §9.4.
2. **Per-publication + per-creator training-corpus + fine-tune-license provenance** for the post-recommendation model, comment-moderation classifier, AI-digest-prioritization model, AI-spam-detection classifier, and post-translation pipeline — Art. 53(1)(b) + Art. 53(1)(d) + ISO 42001 6.1.4. Substack's corpus spans per-post-content + per-engagement-event + per-subscriber-impression + per-commenter-history + per-creator-network-graph + per-publication-network-graph — all of which is GPAI training-data on Aug 2.
3. **Prompt-injection + AI-recommendation-poisoning + AI-content-moderation-bypass + AI-spam-detection-bypass + AI-translation-poisoning + per-publication-prompt-injection + per-creator-self-promotion-bypass + spam-bypass defense review** per OWASP LLM Top 10 (LLM01 prompt-injection + LLM03 training-data-poisoning + LLM06 excessive-agency + LLM08 vector-and-embedding-poisoning) + MITRE ATLAS + EU AI Act Art. 14 (human-oversight) + Art. 50 (transparency-obligation). Substack's recommendation + comment-moderation stack reaches every reader + every commenter + every publication's subscriber base across the entire post-discovery surface.
4. **Cross-Substack-publication + cross-creator + per-subscriber + per-publication + per-substack-tenant + per-procurement-vendor-DD isolation evidence review** per SOC 2 CC6.1 + GDPR Art. 28 (processor-obligation) + Schrems II (cross-border transfer) + ISO 27701 + ISO 42001 §7.5 — including cross-border-data-residency-isolation-evidence for the AI-translation pipeline (US + EU + UK + APAC language territories).
5. **WORM retention + cost-attribution join-table** linking per-AI-recommendation-cost + per-AI-translation-cost + per-AI-content-moderation-cost + per-AI-spam-detection-cost + per-substack-tenant-cost + per-publication-cost + per-vendor-DD-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 (if any paid-subscriber-tier features count as financial records) + CAN-SPAM retention + DSA Art. 27 + Aug 2 2026 GPAI enforcement + EU AI Act Annex III 4.

We'll deliver a 60-100 page audit packet + a SOC 2 / EU AI Act / DSA cross-walk memo. $497 for the review, normally $1,200 if you wait until after Aug 2 (when the EU enforcement posture hardens). Available Mon-Fri 9-5 PT for a 30-min scoping call; we can sign a mutual NDA first if procurement requires it.

Relevant background: Substack's post-recommendation API is the most surfaced AI in the creator-economy stack I've reviewed since the FTC 16 CFR Part 255 endorsement-disclosure amendment (and the DSA Art. 27 recommender-transparency requirement is its European twin). Substack is one of four platforms we've lined up for the August GPAI-rush cohort.

Best,
James Potter
Talon Forge — AI Act Readiness Audits
james@talonforge.co | https://talonforge.co
EU AI Act Art. 53 GPAI documentation • SOC 2 CC7.2 evidence • DSA Art. 27 recommender-transparency
