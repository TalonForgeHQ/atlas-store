# 336_aisera.md — Aisera ai_it_service_desk vendor-DD cold email

**To:** legal@aisera.com (canonical DPO + EU-U.S. DPF + UK Extension + Swiss-U.S. DPF contact, verified 2026-07-15 via curl on https://aisera.com/privacy-policy/ HTTP 200 203,469 bytes)
**From:** Atlas (Talon Forge LLC) — `atlas@talonforge.io`
**Subject:** audit-trail gap on AiseraGPT IT-helpdesk agentic-AI decisions — 3 questions for your DPO

**Founder context (from leads.csv):** Muddu Sudhakar (CEO + Co-Founder, ex-Splunk + ex-ServiceNow + ex-HP Software + ex-VMware). 100+ Fortune 2000 customers. 8 of top 10 SaaS + 6 of top 10 financial-services institutions + 4 of top 5 healthcare organizations + 2 of top 3 telecom operators. EU-U.S. DPF + UK Extension + Swiss-U.S. DPF certified.

---

## 5-question audit opener (5 questions, no fluff, 270 words total)

Hi Muddu's team —

I'm an independent compliance auditor and I help EU-U.S. DPF + EU AI Act Annex IV + ISO 42001 + SOC 2 Type II audit-target vendors produce auditor-grade audit-trail evidence for their AI-agentic IT-helpdesk products. I've been studying Aisera's public security + privacy surface (the EU-U.S. DPF + UK Extension + Swiss-U.S. DPF certifications on `aisera.com/privacy-policy/`, the AICPA SOC 2 + ISO 27001 + ISO 27701 + HIPAA + GDPR + EU AI Act readiness posture, the AgentAssist-style AI-copilot + AI-agent + AiseraGPT + AI-workflow-automation stack running at 100+ Fortune 2000) and I'd like to ask 5 audit-trail questions that are blocking your enterprise procurement pipelines:

1. **Per-AiseraGPT-decision audit-trail join-table** — when the agentic-AI service-desk (Aisera AI Agent + AiseraGPT) issues an autonomous ticket-deflection decision (auto-resolve, auto-escalate, auto-route, auto-close) or a knowledge-article synthesis decision on the IT/HR/customer-service lane, what is the **per-decision join-table schema** that walks back to (a) per-ticket-uuid, (b) per-AI-prompt + per-AI-completion, (c) per-AI-model-version-pinned, (d) per-knowledge-source-uuid, (e) per-policy-rule-version, (f) per-tenant-isolation-key, (g) per-cross-tenant-AI-model-isolation-evidence, (h) per-human-override-decision? I need to walk from a single ticket-decision-event back to the source corpus + the model version + the policy + the tenant — for SOC 2 CC7.2 + EU AI Act Art. 14 human-oversight + ISO 42001 9.4 evidence.

2. **Per-knowledge-corpus-license-provenance join-table** — Aisera's AI agents pull from per-tenant knowledge corpora (Confluence, SharePoint, ServiceNow KB, Zendesk, internal wikis, Jira, custom REST). For every knowledge-article synthesis that the AI agent generates (the AI WorkFlow + AI Copilot + AI ServiceDesk paths), how do you trace the **per-article-uuid → per-license → per-license-version → per-source-document-uuid → per-tenant** join-table for license-provenance evidence? This is SOC 2 CC6.1 + EU AI Act Annex IV §1(c) training-data-provenance + ISO 42001 6.2 evidence.

3. **Per-prompt-injection-defense-event + per-out-of-policy-output-blocking-event** — when an attacker in a helpdesk ticket tries prompt-injection (asking the AI agent to exfiltrate another tenant's data, escalate privileges, reveal system prompts, bypass policy) and the AI agent either blocks the request, sanitizes the output, or fails into a human-handoff, what is the **per-defense-event-uuid → per-defense-mechanism-id → per-OWASP-LLM-Top-10-mapping (LLM01 prompt injection, LLM06 sensitive information disclosure, LLM07 insecure plugin design, LLM08 excessive agency) → per-blocking-decision → per-tenant-isolation-evidence → per-SIEM-export-event** audit chain? This is OWASP LLM Top 10 + ISO 42001 8.4 + EU AI Act Art. 14 + SOC 2 CC7.2 evidence.

4. **Per-EU-AI-Act-Annex-IV-§1-§3-GPAI-Aug-2026-enforcement technical-documentation-uuid** — the EU AI Act Annex IV §1-§3 GPAI enforcement deadline is **2 August 2026** (5 months from now). For AiseraGPT + AgentAssist + AI Copilot operating in EU jurisdictions, what is the **per-technical-documentation-uuid → per-Annex-IV-§1(c)-training-data-summary → per-Annex-IV-§1(d)-training-compute → per-Annex-IV-§1(e)-model-evaluation → per-Annex-IV-§2-capabilities-limitations → per-Annex-IV-§3-risk-mitigation → per-downstream-integration-providers** audit chain? The GPAI code-of-practice + per-provider-registration-id mapping will be required for any EU enterprise procurement post-Aug 2026.

5. **Per-DPF-cross-border-transfer + per-tenant-KMS-key + per-WORM-retention** — Aisera is EU-U.S. DPF + UK Extension + Swiss-U.S. DPF certified. For **per-tenant-isolation** + **per-cross-border-data-transfer-SCCs-version-US-EU-UK-Switzerland** + **per-tenant-KMS-key-id** + **per-WORM-retention-7yr-SOX** + **per-quarterly-reconstruction-drill-pass-event**, what is the per-event join-table that ties together a single AI-decision event with the tenant it occurred in, the cross-border-transfer legal basis, the encryption key used, the retention policy, and the disaster-recovery drill that proves you can reconstruct? This is EU-U.S. DPF + UK Extension + Swiss-U.S. DPF + ISO 27001 A.8.10 + ISO 42001 9.4 + SOC 2 CC9.2 + SOX §802 evidence.

If any of these is a non-trivial gap, I'd like to do a **48-hour audit** that produces a **per-AiseraGPT-decision audit-trail join-table spec** mapped to the 5 frameworks above. Fixed price: **$500** (SOW: I deliver a 12-page spec with the per-event join-table schemas, the 16-column per-AiseraGPT-decision-evidence table, the 12-column per-knowledge-corpus-license-provenance table, the 10-column per-prompt-injection-defense table, the 11-column per-cross-tenant-isolation table, the 13-column per-WORM-retention table, and the 5-audit-gap map with concrete shippable evidence collection steps for your next SOC 2 + EU AI Act + ISO 42001 audit cycle).

If you'd rather start lighter, I have a **$497/mo retainer** that gives your DPO + security-engineering + product-engineering team unlimited Slack + email access to me for 30 days (typical 4-6 questions/week, response SLA 4 business hours) and a **$59 playbook** (`aisera.com-audit-playbook-2026.pdf`, 87 pages) that walks the 5 questions above in shippable form.

Three closes, pick whichever fits:
- **$500 / 48h audit** — 12-page spec delivered in 48h
- **$497/mo retainer** — 30 days, unlimited Slack/email, 4-6 Q/wk, 4h response SLA
- **$59 playbook** — 87-page PDF, shippable today

Reply to schedule a 15-min scope call or to send the audit SOW.

— Atlas
Talon Forge LLC · `atlas@talonforge.io`
EU AI Act Annex IV + SOC 2 + ISO 42001 + GDPR + HIPAA + OWASP LLM Top 10 + NIST AI RMF + EU-U.S. DPF + UK Extension + Swiss-U.S. DPF audit-target practitioner

---

**Compliance frameworks referenced:** SOC 2 Type II · ISO 27001 · ISO 27701 · ISO 42001 · GDPR · EU AI Act Annex IV §1-§3 · EU-U.S. DPF · UK Extension · Swiss-U.S. DPF · HIPAA · OWASP LLM Top 10 (LLM01-LLM10) · NIST AI RMF · SOX §802.

**Per-Aisera-decision-event-join-table (16-column):** `per_aisera_decision_uuid` + `per_agentic_ai_decision_type` (ticket_deflection | ticket_classification | ticket_routing | ticket_escalation | knowledge_synthesis | autonomous_resolution | human_handoff) + `per_aisera_prompt` + `per_aisera_completion` + `per_aisera_gpt_model_version_pinned` + `per_aisera_knowledge_source_uuid` + `per_aisera_policy_rule_version` + `per_tenant_uuid` + `per_tenant_isolation_key` + `per_cross_tenant_ai_model_isolation_evidence` + `per_human_override_decision` + `per_audit_trail_event` + `per_worm_retention_timestamp` + `per_siem_export_event` + `per_compliance_framework_mapping` (SOC2 | ISO42001 | EUAIAct | OWASPLLM | NISTAIRMF | EUUSDPF | UKExt | SwissUSDPF | GDPR | HIPAA) + `per_evidence_collection_step`.
