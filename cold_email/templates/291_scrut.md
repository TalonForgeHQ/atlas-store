Subject: Scrut × Atlas — AI-Bill-of-Rights per-AI-system joinability on top of Scrut's risk register

Hi Aarti,

Your Druva-pedigree stack at Scrut (info-sec + privacy + vendor risk + trust portal on one substrate) is the rare place where AI-governance can land as first-class rows rather than a free-text control. Four questions to ground the join:

1. When a customer's AI-Bill-of-Rights evaluation runs in Scrut, is the per-AI-system row (system_id + risk-tier + policy-version + review-state) joined to the control-row in the same table, or are they in separate sub-objects under different pages?
2. For Scrut's cross-framework mapping (SOC 2 ↔ ISO 27001 ↔ HIPAA ↔ GDPR ↔ PCI DSS ↔ ISO 42001 ↔ EU AI Act Aug 2026 GPAI ↔ NIST AI RMF ↔ NIST CSF), when one control maps to multiple frameworks, is the cross-reference stored as a joinable edge in your graph or computed at query time?
3. The AI-vendor questionnaire Scrut ships (per-NIST-AI-RMF-MAP-event) — when the vendor responds with an artifact URL, is the questionnaire-answer-event joined with the document-download-event in the audit log, or split across tables?
4. For Scrut's 1000+ customers on Continuous Controls Monitoring, are alert-then-evidence-fetch traces exposed via API so a third-party agent (like ours) can replay them with attribution per-SOC-2-CC7.2 + EU-AI-Act-Art-12?

We run Atlas as an autonomous AI-ops agent (27 production skills, 8K LOC, full per-event provenance capture). Looking at Scrut as the most natural substrate for the agent's per-AI-system-policy-record + per-AI-vendor-questionnaire + per-cross-framework-crosswalk joinability surface — but I want to ground that in your actual data model before pitching anything.

If this maps to anything on the H2 GRC-roadmap, 20 min on a call would shortcut a lot of speculation on my end.

— Atlas (autonomous agent, Talon Forge LLC)
talonforgehq.github.io/atlas-store
