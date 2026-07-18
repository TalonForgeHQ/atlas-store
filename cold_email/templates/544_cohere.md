Subject: Cohere EU AI Act Aug 2 2026 GPAI documentation — 4 audit questions your QSA + EU AI Act conformity assessor will ask

Hi Aidan / Ivan / Nick,

Congrats on Cohere North + Command R+ shipping into the regulated-enterprise lane.
I work with GPAI providers on the EU AI Act Art. 53(d) + Art. 53(1)(b) training-data
documentation + SOC 2 CC7.2 + ISO 42001 audit gap that hits the quarter before the
Aug 2 2026 GPAI enforcement deadline.

The 4 questions Cohere's QSA + a Big-4 EU AI Act conformity assessor will ask Cohere
specifically (not generic GPAI questions):

1. **End-to-end 13-col provenance join-table.** A Cohere Command R+ inference call
   crosses per-Cohere-tenant-id -> per-Cohere-workspace-id -> per-Cohere-model-id ->
   per-Command-R+-deployment-id -> per-Rerank-id -> per-Embed-id -> per-Coral-search-id
   -> per-North-workflow-id -> per-prompt-template-id -> per-prompt-input-hash ->
   per-retrieval-chunk-id -> per-LLM-output-id -> per-provenance-log-entry-id. When
   a regulated-industries customer asks "show me every prompt + retrieval + output
   that touched financial-record X in tenant Y last quarter", can Cohere answer in
   under 60 seconds? If no, you have a SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001
   9.4 + ISO 27701 + GDPR Art. 30 + Schrems II SCC + EU AI Act Aug 2 2026 GPAI
   Art. 53(d) + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation
   + 12-state AI-disclosure gap.

2. **Training-data transparency + retrieval-corpus provenance.** Cohere Command R+
   was trained on a large multimodal corpus + retrieval-augmented-generation on
   customer-documents. EU AI Act Art. 53(d) + Art. 53(1)(b) require a public
   copyright-summary + training-data-transparency disclosure before Aug 2 2026.
   Schrems II SCC + EU-US DPF + HIPAA + FedRAMP-Ready add cross-border-data-
   transfer-provenance obligations. Cohere's on-prem + VPC + private-deployment
   story helps, but the documentation gap remains.

3. **Prompt-injection + retrieval-poisoning + North-workflow-poisoning defense.**
   OWASP LLM Top 10 LLM01 (prompt injection) + LLM03 (training-data poisoning) +
   LLM06 (sensitive disclosure) + LLM08 (excessive agency) + MITRE ATLAS threats
   Cohere specifically because Command R+ + Rerank + Embed + Coral + North
   decisions reach enterprise Fortune 500 customers + regulated-industries
   (financial-services + healthcare + pharma + legal + government + defense-intel)
   across all 50 states + DC + EU + UK + APAC + AU. A poisoned Rerank call could
   mis-rank legal-discovery-documents; a poisoned Coral-search could route
   misattributed PHI to a clinical-decision-support-system.

4. **Cross-Cohere-tenant + per-tenant-KMS-key-id + CMK/BYOK + on-prem-VPC-isolation
   + cross-border-data-residency-isolation.** Cohere's enterprise posture relies on
   tenant-isolation + per-tenant-KMS-key-id + CMK/BYOK + on-prem-VPC + private-
   deployment. SOC 2 CC6.1 + GDPR Art. 28 + Schrems II SCC + EU-US DPF + FTC
   Safeguards Rule + ISO 27701 + HIPAA + FedRAMP-Ready evidence is auditable, but
   the per-tenant-isolation-evidence chain (which key, which VPC, which residency
   region) needs to be reconstructable from a single tenant-id in under 60 seconds.

**Offer:** $500 one-time audit (48-hour delivery, 5-gap report mapped to EU AI Act
Art. 53(d) + SOC 2 CC7.2 + ISO 42001 + Schrems II SCC) OR $497/mo retainer (quarterly
audit + ad-hoc QSA-question support + procurement-vendor-DD packet maintenance).

Reply with a Yes and I'll send the audit-SOW + a sample 5-gap report from a comparable
GPAI provider engagement (no competitor names, redacted).

— Atlas @ Talon Forge
Talon Forge LLC | talonforge.io
Privacy: talonforge.io/privacy