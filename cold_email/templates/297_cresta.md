# TO: Cresta (@crestaai)
# VERTICAL: customer_service_ai
# TIER: 1
# WHY: Cresta is the Sebastian-Thrun-co-founded enterprise AI contact-center — real-time agent-assist for Fortune 50 financial-services, 3 of top-5 US banks, Fortune 500 telco + insurance
# SOURCE: cresta.com/privacy-policy (cresta-privacy@cresta.ai verified live 2026-07-12 via curl, HTTP 200, mailto exposed)
# OFFER: $500 audit (24h)

---

**Subject:** Cresta's real-time agent-assist needs a per-turn AI-decision-provenance layer — 24h, $500

Hi Cresta team,

Sebastian and Liya's bet that real-time AI coaching + agent-assist belongs inside the contact-center platform — not bolted on — is the right architecture. But the audit gaps I find in real-time agent-assist platforms (Cresta, but also the 4 siblings: Decagon, Cognigy, Sierra, Tidio) all collapse into the same five SOC 2 / EU AI Act evidence failures:

- **Per-turn intent-classifier-drift provenance** — Cresta classifies every turn in real time. When the classifier starts routing billing-as-cancel-as-escalate-as-retention (the labels look right; the routing is wrong), you need a per-turn-provenance join-table reconstructible from a single conversation_id. Most real-time agent-assist platforms store the conversation, the classifier log, and the downstream CRM state-change in three systems that don't share a primary key.
- **Real-time coaching-decision evidence** — when Cresta Coach whispers "say this next" to the human agent, what proves the suggestion was grounded in the customer's prior turn + knowledge base + policy, not hallucinated? The post-call summary is not the same artifact as the pre-turn state. SOC 2 CC7.2 + EU AI Act Art. 14 (human-oversight) both demand the pre-turn state.
- **PII / PCI redaction on the wire** — Cresta ingests customer PII (orders, accounts, often SSN-last4 for identity verification) AND PCI data (card-last4 over the phone). The retention class for the conversation is different from the retention class for the LLM-trace store, which is different from the retention class for the downstream-Salesforce/Avaya/Genesys/Amazon-Connect state-change log. Three retention classes, one customer-deletion-request — and the gap between them is the gap that breaks GDPR Art. 17 + PCI-DSS 3.2 + CCPA.
- **Cross-tenant isolation-evidence on a real-time stream** — every conversation is being co-classified on shared GPU infrastructure. Per-tenant KV-cache partition + per-tenant LoRA + per-tenant prompt-injection detection-log evidence is the audit-target auditors look for and the thing most platforms can't reconstruct after the fact.
- **Downstream Avaya / Genesys / Amazon Connect state-change join** — when the agent's "say this next" suggestion is acted on and a Salesforce ticket is updated + a Zendesk macro fires + an Amazon Connect call-record is mutated, you need a single call_id that joins the AI-suggestion to the downstream state-changes. Three systems, three IDs, one conversation — and a SOC 2 auditor will ask you to reconstruct it in 30 seconds.

**$500 flat. 24h turnaround. 60-day money-back if no clear ROI.**

Worth a 15-min scope call?

— Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/