# Cold email opener: Tabnine — Lead 346

**Subject:** Tabnine Enterprise + Private AI Code Assistant — agentic audit-trail joins for your Fortune-500 customers?

Hi {{founder_name}},

Congrats on closing Tabnine's enterprise-AI-code-assistant lane — Tabnine was the first production AI-code-autocomplete vendor (founded 2013, pre-dating every modern cohort member), pivoted to private-deployment + on-prem Kubernetes Helm chart for regulated industries, and the security@tabnine.com contact page is now where procurement teams land when they ask "who handles our per-air-gapped-deployment-flag + per-VPC-peering + per-private-instance-id + per-BYO-LLM-model-id requirements for AI coding at scale?"

I'm Atlas at Talon Forge — we run vendor-DDQ audits for AI-code-assistant buyers (Cursor, GitHub Copilot, Cody Sourcegraph, Continue, Codeium/Windsurf, and now Tabnine). Each vendor gets the same 11-column join-table: per-prompt-id, per-completion-id, per-LLM-model-id, per-LLM-prompt-hash, per-LLM-prompt-template-version, per-system-prompt-id, per-context-window-tokens, per-context-window-strategy, per-repository-file-id, per-code-chunk-id, per-codebase-index-id, per-similarity-score, per-retrieved-chunk-id, per-tool-call-id, per-AI-action-id, per-action-type, per-action-rollback-id, per-action-rollback-reason, per-prompt-injection-detection-signal-id, per-data-residency-region, per-PII-redaction-tier, per-customer-code-isolation-region, per-zero-retention-flag, per-BYO-LLM-model-id, per-BYO-LLM-api-key-version, per-customer-opt-out-of-training-flag, per-customer-tenant-id, per-self-hosted-instance-id, per-on-prem-instance-flag, per-VPC-peering-id, per-air-gapped-deployment-flag, per-SSO-SAML-OIDC-config-id, per-SCIM-provisioning-id, per-audit-log-export-id.

**5 quick questions** so the 1-page brief I send back actually maps to Tabnine's reality:

1. **Private instance + air-gap support** — `per-private-instance-id` + `per-air-gapped-deployment-flag` + `per-self-hosted-instance-id`. Tabnine is the only AI-code-assistant vendor that ships a true air-gapped Kubernetes deployment with no outbound network at all (no model telemetry egress, no completion logging egress, no anonymized analytics egress). Is the per-air-gapped-deployment-flag enforced at the egress-firewall layer, or only at the application layer? (FedRAMP High + financial-services-banking + defense-industrial-base buyers want the egress-firewall-layer answer.)

2. **Codebase index isolation** — `per-codebase-index-id` + `per-customer-code-isolation-region` + `per-data-residency-region`. Are Tabnine Enterprise on-prem indices stored in the customer's VPC, and is the per-customer-tenant-id namespace the boundary for retrieval? (Fortune-500 buyers want proof that their private repos can't bleed into another tenant's index — and Tabnine on-prem is the strongest answer in the cohort because the index never leaves the customer's environment.)

3. **BYO-LLM keys + per-BYO-LLM-api-key-version** — can a customer bring their own Anthropic / OpenAI / Mistral / Cohere / Bedrock / Vertex / Azure OpenAI / Ollama key and pin per-BYO-LLM-api-key-version, so revoking + rotating that version doesn't affect other customers? (Tabnine's BYO-LLM roster is the broadest in the cohort — but the version-pinning behavior is the regulated-industries gate.)

4. **Zero-retention-flag + opt-out-of-training-flag** — Tabnine has been zero-retention by default since 2023 (industry first). When `per-zero-retention-flag = true` is set per-customer-tenant-id, does Tabnine's product-analytics ingestion skip the tenant entirely, and is that skip verifiable in the `per-audit-log-export-id`? (Procurement needs the receipt, and Tabnine's zero-retention posture is the strongest in the cohort — but the audit-log-receipt is still the buyer's question.)

5. **Prompt-injection detection + `per-prompt-injection-detection-signal-id`** — does Tabnine surface a signal when a fetched code chunk tries to override the system prompt, and does that signal flow into the `per-action-rollback-reason` field? (OWASP LLM01 is now a CISO-conversation line item, and Tabnine's older autocomplete surface has a different injection model than Cascade / Copilot / Cody agentic surfaces — buyers ask because the agentic Tabnine Chat + Tabnine Agents surfaces behave differently.)

The deliverable for security@tabnine.com would be a 1-page brief that places Tabnine inside the canonical ai_code_generation 6-vendor cohort (Cursor 340, GitHub Copilot 341, Cody Sourcegraph 342, Continue 343, Codeium 345, Tabnine 346) — closing the canonical 6-vendor chain — with a per-vendor 35-column coverage score and the EU AI Act Art. 14 (Human Oversight) / SOC 2 CC7.2 (System Operations Monitoring) / ISO 42001 §9.4 (AI System Lifecycle) / NIST AI RMF MEASURE cross-walk your buyers can hand to legal.

**Audit price:** $500 flat, 48h delivery. **Retainer:** $497/mo for monthly coverage updates as Tabnine ships new private-deployment features + Tabnine Agents agentic surfaces + the EU AI Act implementing acts land through 2026-2027.

Want the sample brief? I can send the Tabnine section as a standalone PDF if you forward this to the right person on the Tabnine side.

— Atlas
Talon Forge LLC
atlas@talonforge.com

P.S. If the right contact is support@tabnine.com (the secondary inbox I verified), feel free to forward — both mailboxes route to the same vendor-DD queue.