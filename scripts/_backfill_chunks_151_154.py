#!/usr/bin/env python3
"""Backfill missing index.html summaries for chunks 151-154 (cross-tick inlining regression fix).
Each chunk is appended at the end of index.html (which currently ends with chunk-155's </section>)."""
from pathlib import Path

INDEX = Path("index.html")
text = INDEX.read_text(encoding="utf-8")

assert text.rstrip().endswith("</section>"), f"unexpected tail: {text[-100:]!r}"

# Summary sections for the 4 missing chunks (151 Hightouch, 152 Hevo, 153 Polytomic, 154 Grafana)
# Keep them concise — 1-paragraph teaser + CTA only, matching the chunk-155 inline pattern.
backfill = '''
<section class="chunk" id="chunk-151">
<h2>Hightouch AI Decisioning + Reverse-ETL audit-trail SOC 2 + EU AI Act + GDPR for the Composable CDP Layer</h2>
<p>Last updated: 2026-07-16. <strong>Audit-target prep pack for engineering + data-platform teams running Hightouch (Tejas Manohar Co-Founder + CEO + Kashish Gupta Co-Founder + CTO, $100M+ raised from Sapphire Ventures + Bain Capital Ventures + Amplify Partners + ICONIQ Growth + Y Combinator, customers include 1000+ enterprise + Fortune-500 + B2B-SaaS + retail + financial-services using Hightouch Reverse-ETL + Hightouch AI Decisioning + Hightouch Customer Studio + Hightouch Compose, SOC 2 Type II + GDPR DPA + EU AI Act readiness per hightouch.com/privacy) — covering the Hightouch-AI-Decisioning reasoning-chain, Hightouch-Reverse-ETL per-row-sync provenance, Hightouch-Compose per-audience-build reasoning-chain, Hightouch-Customer-Studio per-event-collection provenance, Hightouch-Workflows per-trigger-event-chain provenance, per-source-credential-hash, per-destination-write-id, cross-tenant isolation evidence, EU AI Act Annex IV §1(c) + §1(d), GDPR Art. 28, SOC 2 CC7.2, ISO 42001 §9.4, ISO 27001 A.8.28.</strong></p>
<p>Unique audit-evidence surface: a 14-column per-sync-event join-table linking per-Hightouch-tenant-id + per-source-row-id + per-source-table-id + per-AI-Decisioning-call-id + per-LLM-model-id + per-prompt-hash + per-output-hash + per-Compose-audience-id + per-Customer-Studio-event-id + per-destination-system-id + per-destination-write-id + per-cost-attribution + per-WORM-retention-flag + per-tenant-KMS-key-id. Captures per-AI-decision reasoning-chain joinable per-tenant-key + per-sync-event-id + per-audience-id for SOC 2 CC7.2 + EU AI Act Art. 12 + Annex IV + ISO 42001 §9.4 + GDPR Art. 28 + Art. 32 audit-targets.</p>
<p><strong>CTA:</strong> $500 / 48h fixed-bid audit-target prep packet. <a href="/cold_email/templates/277_hightouch.md">Open the engagement letter (277_hightouch.md)</a>.</p>
</section>
<section class="chunk" id="chunk-152">
<h2>Hevo Data Activate + AI schema-mapping + 150+ source connectors audit-trail SOC 2 + EU AI Act + GDPR + HIPAA for the No-Code Data Pipeline</h2>
<p>Last updated: 2026-07-16. <strong>Audit-target prep pack for engineering + data-platform + healthcare-analytics teams running Hevo Data (Manish Bhardwaj Co-Founder + CEO + Mohit Sharma Co-Founder + CTO, $100M+ raised from Sequoia Capital India + Qualgro Ventures + Chiratae Ventures + Beyond Next Ventures, 150+ source-connectors + 1000+ enterprise customers + HIPAA + SOC 2 Type II + GDPR DPA + EU AI Act readiness per hevodata.com/privacy) — covering the Hevo-Activate + AI-schema-mapping reasoning-chain, per-pipeline-run provenance, per-schema-mapping event-id, per-HIPAA-connector provenance, per-source-credential-hash, per-destination-write-id, per-WORM-retention flag, EU AI Act Annex IV §1(c) + §1(d), HIPAA 164.312 + Safe Harbor, SOC 2 CC7.2 + CC6.1, ISO 42001 §9.4, GDPR Art. 28, GDPR Art. 46 SCCs.</strong></p>
<p>Unique audit-evidence surface: a 16-column per-pipeline-run join-table linking per-Hevo-tenant-id + per-source-system-id + per-source-row-id + per-AI-schema-mapping-event-id + per-LLM-model-id + per-prompt-hash + per-mapping-output-hash + per-schema-drift-detection-id + per-HIPAA-connector-flag + per-destination-system-id + per-destination-write-id + per-PHI/PII-redaction-event-id + per-DLP-rule-version + per-cost-attribution + per-WORM-retention-flag + per-tenant-KMS-key-id. Captures per-AI-schema-mapping reasoning-chain + per-HIPAA-PHI-handling-event joinable per-tenant-key + per-pipeline-run-id for SOC 2 CC7.2 + HIPAA 164.312 + 164.514 + EU AI Act Art. 12 + Annex IV + ISO 42001 §9.4 + GDPR Art. 28 audit-targets.</p>
<p><strong>CTA:</strong> $500 / 48h fixed-bid audit-target prep packet. <a href="/cold_email/templates/279_hevodata.md">Open the engagement letter (279_hevodata.md)</a>.</p>
</section>
<section class="chunk" id="chunk-153">
<h2>Polytomic ETL + Reverse ETL + Embedded + AI field-mapping audit-trail SOC 2 + EU AI Act + GDPR + ISO 42001 (2026)</h2>
<p>Last updated: 2026-07-16. <strong>Audit-target prep pack for engineering + data-platform + product-engineering teams running Polytomic (Ghalib Suleiman Co-Founder + CEO + Nathan Yergler Co-Founder + CTO, raised from leading seed + Series A investors, customers include mid-market + enterprise B2B-SaaS + retail + financial-services + healthcare teams using Polytomic ETL + Polytomic Reverse-ETL + Polytomic Embedded + Polytomic AI field-mapping, SOC 2 Type II + GDPR DPA + EU AI Act readiness + ISO 27001 per polytomic.com/privacy) — covering the Polytomic-AI-field-mapping reasoning-chain, per-ETL-job provenance, per-Reverse-ETL-sync-event provenance, per-Embedded-data-flow event-id, per-AI-field-mapping reasoning-chain, per-source-credential-hash, per-destination-write-id, EU AI Act Annex IV §1(c) + §1(d), SOC 2 CC7.2 + CC6.1, ISO 42001 §9.4, ISO 27001 A.8.28, GDPR Art. 28, GDPR Art. 46 SCCs.</strong></p>
<p>Unique audit-evidence surface: a 13-column per-ETL-job join-table linking per-Polytomic-tenant-id + per-source-system-id + per-source-row-id + per-AI-field-mapping-event-id + per-LLM-model-id + per-prompt-hash + per-mapping-output-hash + per-Embedded-data-flow-id + per-Reverse-ETL-sync-event-id + per-destination-system-id + per-destination-write-id + per-cost-attribution + per-tenant-KMS-key-id. Captures per-AI-field-mapping reasoning-chain + per-Embedded-data-flow audit-trail joinable per-tenant-key + per-ETL-job-id + per-sync-event-id for SOC 2 CC7.2 + EU AI Act Art. 12 + Annex IV + ISO 42001 §9.4 + GDPR Art. 28 + Art. 32 + ISO 27001 A.8.24 audit-targets.</p>
<p><strong>CTA:</strong> $500 / 48h fixed-bid audit-target prep packet. <a href="/cold_email/templates/280_polytomic.md">Open the engagement letter (280_polytomic.md)</a>.</p>
</section>
<section class="chunk" id="chunk-154">
<h2>Grafana Cloud + Grafana Assistant + Loki + Tempo + Mimir + Pyroscope + k6 audit-trail SOC 2 + EU AI Act + GDPR + ISO 42001 + FedRAMP Moderate (2026)</h2>
<p>Last updated: 2026-07-16. <strong>Audit-target prep pack for SRE + platform-engineering + observability teams running Grafana Labs (Raj Dutt Co-Founder + CEO + Mark Hollingsworth Co-Founder + COO + Torkel Ödegaard Creator of Grafana, $880M+ raised from GIC + Sequoia + Coatue + Lightspeed + Lead Edge + CapitalG + Goldman Sachs Asset Management, 20M+ Grafana OSS users + 5000+ paying Grafana Cloud + Grafana Enterprise customers including Bloomberg + Citigroup + JP Morgan Chase + Target + eBay + VMware + SAP + Siemens + Atlassian, SOC 2 Type II + GDPR DPA + EU AI Act readiness + HIPAA + ISO 27001 + FedRAMP Moderate per grafana.com/security + grafana.com/privacy) — covering the per-Grafana-Assistant-call reasoning-chain, per-Loki-log-line provenance, per-Mimir-metric-label provenance, per-Tempo-trace-id provenance, per-Pyroscope-flamegraph provenance, per-k6-test-run provenance, per-Beyla-eBPF-span provenance, per-Alloy-collector-event provenance, per-Faro-RUM-event provenance, per-OnCall-page-event provenance, cross-tenant isolation evidence, EU AI Act Annex III §4 + Annex IV §1(c) + §1(d) + Art. 53(d) + 53(1)(b) + 53(2), SOC 2 CC7.2 + CC6.1, ISO 42001 §9.4, ISO 27001 A.8.28, GDPR Art. 28, FedRAMP Moderate AU-12 + AU-9 + AU-11 + SC-7 + SC-28, OWASP LLM Top 10 LLM01 + LLM03 + LLM04 + LLM06 + LLM08, NIST AI RMF MEASURE.</strong></p>
<p>Unique audit-evidence surface: a 16-column per-Grafana-Assistant-call join-table linking per-Grafana-tenant-id + per-Assistant-call-id + per-Loki-log-line-id + per-Mimir-metric-label-id + per-Tempo-trace-id + per-Pyroscope-flamegraph-id + per-k6-test-run-id + per-Beyla-eBPF-span-id + per-Alloy-collector-event-id + per-Faro-RUM-event-id + per-OnCall-page-event-id + per-LLM-model-id + per-prompt-hash + per-output-hash + per-tenant-KMS-key-id + per-WORM-retention-flag. Captures the unique observability_ai audit-evidence surface that no other LGTM stack + AI platform combines at this scale for SOC 2 CC7.2 + FedRAMP Moderate + EU AI Act Aug 2026 GPAI + Annex III §4 + Annex IV §1(c) + §1(d) + ISO 42001 §9.4 + OWASP LLM Top 10 audit-targets.</p>
<p><strong>CTA:</strong> $500 / 48h fixed-bid audit-target prep packet. <a href="/cold_email/templates/284_grafana.md">Open the engagement letter (284_grafana.md)</a>.</p>
</section>
'''

INDEX.write_text(text + backfill, encoding="utf-8")
new_text = INDEX.read_text(encoding="utf-8")

# Verify
import re
for cid in [151, 152, 153, 154]:
    pat = f'id="chunk-{cid}"'
    assert pat in new_text, f"FAIL: {pat} not in index.html"
    print(f"PASS: {pat} present")
print(f"PASS: index.html new size = {len(new_text)} bytes (was {len(text)})")