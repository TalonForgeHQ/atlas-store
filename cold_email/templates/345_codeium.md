# Cold email opener: Codeium (Cognition AI / Windsurf) — Lead 345

**Subject:** Codeium Enterprise + Windsurf Cascade — agentic audit-trail joins for your Fortune-500 customers?

Hi {{founder_name}},

Congrats on the Cognition AI rebrand and the Windsurf Editor launch — Codeium went from autocomplete plugin to Fortune-500 enterprise AI-code-assistant + agentic IDE in 18 months, and the security@cognition.ai contact page is now where procurement teams land when they ask "who handles our zero-retention-flag + per-VPC-peering + per-air-gapped-deployment requirements for AI coding?"

I'm Atlas at Talon Forge — we run vendor-DDQ audits for AI-code-assistant buyers (Cursor, GitHub Copilot, Cody Sourcegraph, Continue, and now Codeium/Windsurf). Each vendor gets the same 11-column join-table: per-prompt-id, per-completion-id, per-LLM-model-id, per-LLM-prompt-hash, per-LLM-prompt-template-version, per-system-prompt-id, per-context-window-tokens, per-context-window-strategy, per-repository-file-id, per-code-chunk-id, per-codebase-index-id, per-similarity-score, per-retrieved-chunk-id, per-tool-call-id, per-AI-action-id, per-action-type, per-action-rollback-id, per-action-rollback-reason, per-prompt-injection-detection-signal-id, per-data-residency-region, per-PII-redaction-tier, per-customer-code-isolation-region, per-zero-retention-flag, per-BYO-LLM-model-id, per-BYO-LLM-api-key-version, per-customer-opt-out-of-training-flag, per-customer-tenant-id, per-self-hosted-instance-id, per-on-prem-instance-flag, per-VPC-peering-id, per-air-gapped-deployment-flag, per-SSO-SAML-OIDC-config-id, per-SCIM-provisioning-id, per-audit-log-export-id.

**5 quick questions** so the 1-page brief I send back actually maps to Codeium's reality:

1. **Cascade agent actions** — every Cascade `ai_action` writes `per-AI-action-id` + `per-action-type` + `per-action-rollback-id` + `per-action-rollback-reason`. Where does the rollback ledger live, and how long does it persist per-customer-tenant-id? (Buyers ask because EU AI Act Art. 14 + Art. 53(d) require human-oversight-evidence for ≥6 months.)

2. **Codebase index isolation** — `per-codebase-index-id` + `per-customer-code-isolation-region` + `per-data-residency-region`. Are Codeium Enterprise on-prem indices stored in the customer's VPC, and is the per-customer-tenant-id namespace the boundary for retrieval? (Fortune-500 buyers want proof that their private repos can't bleed into another tenant's index.)

3. **BYO-LLM keys** — `per-BYO-LLM-model-id` + `per-BYO-LLM-api-key-version`. Can a customer bring their own Anthropic/OpenAI/Mistral key and pin per-BYO-LLM-api-key-version, so revoking + rotating that version doesn't affect other customers? (This is the table-stakes ask for regulated industries.)

4. **Zero-retention-flag + opt-out-of-training-flag** — when both are set per-customer-tenant-id, does the Windsurf Cascade plugin skip Codeium's product-analytics ingestion entirely, and is that skip verifiable in the per-audit-log-export-id? (Procurement needs the receipt.)

5. **Prompt-injection detection** — `per-prompt-injection-detection-signal-id`. Does Codeium surface a signal when a fetched code chunk tries to override the system prompt, and does that signal flow into the per-action-rollback-reason field? (OWASP LLM01 is now a CISO-conversation line item.)

The deliverable for security@cognition.ai would be a 1-page brief that places Codeium/Windsurf inside the canonical ai_code_generation 5-vendor cohort (Cursor 340, GitHub Copilot 341, Cody Sourcegraph 342, Continue 343, Codeium 345) with a per-vendor 35-column coverage score and the EU AI Act / SOC 2 CC7.2 / ISO 42001 cross-walk your buyers can hand to legal.

**Audit price:** $500 flat, 48h delivery. **Retainer:** $497/mo for monthly coverage updates as Codeium ships new Cascade features and the EU AI Act implementing acts land.

Want the sample brief? I can send the Codeium section as a standalone PDF if you forward this to the right person on the Codeium/Windsurf side.

— Atlas
Talon Forge LLC
atlas@talonforge.com

P.S. If the right contact is support@cognition.ai (the secondary inbox I verified), feel free to forward — both mailboxes route to the same vendor-DD queue.