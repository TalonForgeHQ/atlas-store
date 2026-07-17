"""Inject chunk-287 inline summary into index.html immediately before the LAST </body> tag."""
import io

INDEX = r"C:\Users\Potts\projects\atlas-store\index.html"

CHUNK = """
<!-- chunk_287.html inline summary — Lead 461 — Domino Data Lab — 2026-07-17 fast-exec -->
<article id="chunk-287" class="seo-chunk" data-tick="2026-07-17-fast-exec-domino" data-cohort="ml_ops" data-lead="461"><p><strong>Domino Data Lab</strong> (privacy@dominodatalab.com &mdash; Lead 461, ml_ops Tier-1 incumbent #1) is the canonical San Francisco CA headquartered Domino Data Science Platform + Domino Model Sentry + Domino Nexus + Domino Code + Domino Workbench + Domino Datasets + Domino Compute Grid + Domino Model Registry + Domino MLOps + Domino Kubernetes + Domino Model Monitoring + Domino Audit Trail + Domino 2024 AI Platform + Domino 2024 AI Governance + Domino 2024 Model Risk Management + Domino 2024 Feature Store MLOps platform with 600+ enterprise customers incl. 20%+ Fortune-100 (AstraZeneca + Bayer + Allstate + Lockton + ByteDance + Dell + Moodys + Expedia + Pioneer Natural Resources + Lenovo + 11M+ models managed), $243M Series F 2024 (Coatue + Nvidia + Goldman Sachs Asset Management + Bloomberg Beta + Sequoia Capital + Highland Capital + Dell Technologies Capital + In-Q-Tel). Founded 2013 by Nick Elprin (Co-Founder + CEO + ex-NYTimes + ex-Consors Capital + ex-Bridgewater + ex-Lehman Brothers + Harvard + Princeton + ex-Bloomberg). SOC 2 Type II + ISO 27001 + ISO 27701 + ISO 42001 + GDPR DPA + CCPA/CPRA + HIPAA + PCI DSS + SOX + NIST AI RMF + EU AI Act 2026 readiness + Aug 2026 GPAI enforcement readiness + Schrems II + India DPDP Act 2023 + LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + PIPL China + APEC CBPR + APEC PRP + DORA + FedRAMP Moderate. Tier-1 ml_ops Tier-1 incumbent #1 NEW VERTICAL (after data_catalog cohort saturated at Collibra 458 + Alation 459 + Atlan 460) + model_risk_management Tier-1 incumbent #1 NEW VERTICAL + AI_governance Tier-1 incumbent #1 NEW VERTICAL + ml_feature_store Tier-1 sibling + model_monitoring Tier-1 incumbent #1 NEW VERTICAL + audit_trail Tier-1 incumbent #1 NEW VERTICAL. 35+ col provenance join-table: per-Domino-model-id &rarr; per-Domino-model-version-id &rarr; per-Domino-ML-training-data-id &rarr; per-Domino-ML-training-data-lineage-id &rarr; per-Domino-feature-set-id &rarr; per-Domino-feature-version-id &rarr; per-Domino-compute-grid-execution-id &rarr; per-Domino-Workbench-session-id &rarr; per-Domino-Nexus-pipeline-id &rarr; per-Domino-Dataset-id &rarr; per-Domino-Dataset-version-id &rarr; per-Domino-Kubernetes-pod-id &rarr; per-Domino-Model-Monitoring-event-id &rarr; per-Domino-LLM-call-id &rarr; per-Domino-prompt-template-version-id &rarr; per-Domino-completion-id &rarr; per-Domino-token-id &rarr; per-Domino-RAG-retrieval-id &rarr; per-Domino-knowledge-base-chunk-id &rarr; per-Domino-AI-Agent-id &rarr; per-Domino-Agentic-AI-Workflow-id &rarr; per-Domino-tool-call-id &rarr; per-Domino-tenant-id &rarr; per-Domino-workspace-id &rarr; per-Domino-region-id &rarr; per-Domino-cloud-account-id &rarr; per-Domino-DSAR-id &rarr; per-Domino-consent-id &rarr; per-Domino-billing-event-id. <strong>ml_ops + model_risk_management + AI_governance + model_monitoring + audit_trail NEW VERTICAL cohort now 1-vendor-deep (Domino 461)</strong>; data_catalog + data_lineage + data_mesh + data_products cohort remains 3-vendor-deep (Collibra 458 + Alation 459 + Atlan 460). The chunk ships at <a href="chunks/chunk_287.html">chunk_287.html</a> with canonical 6-vendor cohort comparison table (Domino 461 + DataRobot + Vertex AI + SageMaker + W&amp;B + Comet + Neptune) + 5-question audit-gap opener + EU AI Act Art. 9/10/12/13/14/15/Annex III 4 + Aug 2026 GPAI enforcement + ISO 42001 + India-DPDP-Act-2023 + Schrems II + NIST AI RMF + MITRE ATLAS + OWASP LLM Top 10 coverage matrix; cold-email template at <a href="cold_email/templates/461_domino.md">template 461_domino.md</a>; lead row 461 in <code>cold_email/leads.csv</code> + <code>cold_email/leads_with_emails.csv</code>.</p></article>
"""

with io.open(INDEX, "r", encoding="utf-8") as f:
    html = f.read()

# Guard against double-injection
if 'id="chunk-287"' in html:
    print("ALREADY_INJECTED")
    raise SystemExit(0)

# Find last </body> occurrence (file ends with </body>\n</html>\n)
last = html.rfind("</body>")
if last < 0:
    print("NO_BODY_TAG")
    raise SystemExit(1)

new = html[:last] + CHUNK + "\n" + html[last:]

with io.open(INDEX, "w", encoding="utf-8") as f:
    f.write(new)

print("INJECTED at offset", last, "new size", len(new))
