# Cold Email Template — Lead 415 DeepKeep

**Vertical:** ai_safety_red_teaming_llm (Tier-1, 8th-sibling after Giskard 407 / PyRIT 409 / Anthropic Safety 410 / HiddenLayer 411 / NVIDIA Garak 412 / Lakera 413 / Protect AI 414)
**Best verified inbox:** privacy@deepkeep.ai (live HTTP 200 from curl deepkeep.ai/privacy-policy 2026-07-17)
**Engineer-direct inboxes (verified via GitHub commits API 2026-07-17):** gil@deepkeep.ai (Gil Harel, n8n-nodes-deepkeep maintainer), kobi@deepkeep.ai (Kobi Moraz, public-docs maintainer), tziona@deepkeep.ai (public-docs maintainer)

---

## Subject Line Options (A/B)

A: `SOC 2 CC7.2 evidence trail across DeepKeep's 7-product AI attack-surface`
B: `Per-DeepKeep-Firewall-API-call-id → per-LLM-call-id → per-token-id audit gap map`
C: `Yossi + Ofir — quick question on Israel-Privacy-Protection-Law + EU AI Act dual-stack`

---

## Body (240 words, audit-gapped)

Hi Yossi + Ofir,

I'm writing because DeepKeep's 7-product AI attack-surface coverage (DeepKeep for LLM + Vision + AI Firewall + AI Red Teaming + AI Lens + AI Agent Scanner + Model Scanning) is exactly what Tier-1 enterprise security teams are now asking for in their SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 15 evidence binder. The Vibe AI Red Teaming launch is the right move — adaptive human-steered testing across models + applications + agents is the gap that's still open in most incumbent red-team libraries.

I work with AI safety + red-teaming vendors (Giskard + PyRIT + Anthropic Safety + HiddenLayer + NVIDIA Garak + Lakera + Protect AI + now DeepKeep) on a focused 5-evidence-table SOC 2 audit binder:

1. End-to-end provenance join-table — per-LLM-call-id → per-VLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-prompt-injection-score-id → per-jailbreak-score-id → per-multi-turn-attack-id → per-conversation-id → per-agent-step-id → per-tool-call-id → per-RAG-retrieval-id → per-DeepKeep-Firewall-API-call-id → per-DeepKeep-tenant-id → per-DeepKeep-project-id → per-billing-event-id
2. Per-OWASP-LLM-Top-10 → per-MITRE-ATLAS → per-prompt-injection-id → per-visual-prompt-injection-id → per-VLM-call-id coverage-matrix
3. 16-defense deep-coverage matrix — per-prompt-injection + per-jailbreak + per-multi-turn + per-data-poisoning + per-tool-call-poisoning + per-RAG-retrieval-poisoning + per-agent-step-poisoning + per-prompt-leak + per-system-prompt-extraction + per-visual-prompt-injection + per-adversarial-perturbation + per-deepfake + per-ML-trojan + per-ML-backdoor + per-ML-evasion + per-ML-poisoning
4. Cross-DeepKeep-tenant isolation-evidence + self-hosted DeepKeep OSS per-deployment-isolation
5. WORM retention + cost-attribution join-table linking per-detection-cost + per-eval-cost + per-scan-cost

If this maps to what Samsung Ventures + DELL Technologies Capital + StageOne Ventures' enterprise customers are asking for, would a 30-min working session in the next two weeks make sense?

— [Atlas / Talon Forge LLC]

---

## Audit Gap Anchors (for the 5-evidence-table binder)

- **per-DeepKeep-tenant-id** — every detection event needs to be traceable to a specific tenant + project + API-call-id
- **per-DeepKeep-Firewall-API-call-id** — runtime firewall detection events need their own audit-row
- **per-VLM-call-id** — DeepKeep's vision coverage is the unique differentiator vs Lakera + Protect AI; needs its own lineage row
- **per-Agent-step-id** — AI Agent Scanner's runtime scan needs an audit-row per agent step
- **per-DeepKeep-project-id** — projects within tenants need their own isolation evidence (CMK/BYOK + no-cross-leak)

## Compliance Frameworks Targeted

- SOC 2 Type II CC7.2 (system operations — evidence trail)
- EU AI Act Art. 12 (logging) + Art. 15 (robustness, accuracy, cybersecurity)
- Israel Privacy Protection Law (Protection of Privacy Law 5741-1981 + Amendment 13 + Amendment 14 + Privacy Protection Regulations Data Security 2017)
- GDPR Art. 28 (processor obligations) + Art. 32 (security of processing)
- ISO 27001 + ISO 9001 (already certified — verified via deepkeep.ai footer badges)
- ISO 42001 (AI management — WIP per DeepKeep documentation)
- NIST AI RMF MEASURE function
- OWASP LLM Top 10 + OWASP ML Top 10 + MITRE ATLAS + MITRE ATT&CK
