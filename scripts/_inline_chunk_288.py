# Append chunk-288 inline summary to index.html (after chunk-287)
import re
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
INDEX = REPO / "index.html"
CHUNK = REPO / "chunks" / "chunk_288.html"

text = INDEX.read_text(encoding="utf-8")

# Verify chunk-287 is the last seo-chunk in index.html
last_chunk_pos = text.rfind('id="chunk-287"')
if last_chunk_pos == -1:
    raise SystemExit("ERROR: chunk-287 anchor missing from index.html")
# After chunk-287's closing </article>, there's a blank line then </body>
chunk_287_end = text.find("</article>", last_chunk_pos)
if chunk_287_end == -1:
    raise SystemExit("ERROR: chunk-287 closing </article> not found")
insert_pos = chunk_287_end + len("</article>")

# Build the inline summary as a compact <article> (matches existing shape)
summary = (
    '\n<article id="chunk-288" class="seo-chunk" data-tick="2026-07-17-fast-exec-databricks" data-cohort="ml_ops" data-lead="462">'
    '<p><strong>Databricks</strong> (privacy@databricks.com &mdash; Lead 462, ml_ops Tier-1 incumbent #2 &mdash; verified live 2026-07-17 via curl '
    'https://www.databricks.com/legal/privacy-policy HTTP 200 exposing mailto:privacy@databricks.com as the canonical Databricks-GDPR-DPA + CCPA/CPRA + HIPAA + '
    'LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + India-DPDP-Act-2023 + Schrems-II + EU-US-DPF + '
    'UK-Extension-to-EU-US-DPF + Swiss-US-DPF + APEC-CBPR + APEC-PRP + 9000+-enterprise-customer + Ali-Ghodsi-CEO-direct + Matei-Zaharia-CTO-creator-Apache-Spark + '
    'Reynold-Xin-Co-Founder-Apache-Spark-PMC + Patrick-Wendell-Co-Founder + Andy-Konwinski-Co-Founder + Arsalan-Tavakoli-Shirazi-Co-Founder + $43B-valuation-2021 + '
    'IPO-2025-confidential-S-1 + Snowflake-competitor + Apache-Spark + Apache-Iceberg + Delta-Lake + MLflow + Linux-Foundation + '
    'Databricks-DBRX-open-source-132B-MoE-LLM + Counterpoint-Ventures-led-Series-H-2021 + T-Rowe-Price-led-Series-I-2022 strategic-inbound channel) is the canonical '
    'San Francisco CA headquartered Databricks Lakehouse + Unity Catalog + MLflow + Mosaic AI + Model Serving + Model Registry + Feature Store + Vector Search + '
    'Agent Framework + DBRX 132B-MoE + Delta Lake + Apache Spark + Apache Iceberg platform with 9000+ enterprise customers incl. 60%+ Fortune-100 '
    '(Comcast + AT&amp;T + Disney + Walmart + Delta + Starbucks + HSBC + Rivian + Toyota + Shell + Pfizer + Regeneron + Block + Adobe + Mastercard + 400+ Global 2000), '
    '$43B valuation 2021 + IPO 2025 confidential S-1 + $3B+ revenue 2024. Founded 2013 by Ali Ghodsi (Co-Founder + CEO + UC Berkeley AMPLab PhD + Swedish) + '
    'Matei Zaharia (Co-Founder + CTO + creator Apache Spark + UC Berkeley Asst Professor + ACM Doctoral Dissertation Award 2014) + Reynold Xin + Patrick Wendell + '
    'Andy Konwinski + Arsalan Tavakoli-Shirazi. SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + ISO 42001 + GDPR DPA + CCPA/CPRA + HIPAA + '
    'PCI DSS + SOX + NIST 800-53 + NIST CSF + NIST Privacy Framework + NIST AI RMF + EU AI Act 2026 readiness + Aug 2026 GPAI enforcement readiness + Schrems II + '
    'India DPDP Act 2023 + LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + PIPL China + APEC CBPR + '
    'APEC PRP + DORA + FedRAMP Moderate + HITRUST. Tier-1 ml_ops Tier-1 incumbent #2 (after Domino 461) + model_risk_management Tier-1 incumbent #2 + '
    'AI_governance Tier-1 incumbent #2 + ml_feature_store Tier-1 incumbent #2 + model_monitoring Tier-1 incumbent #2 + audit_trail Tier-1 incumbent #2 + '
    'data_lakehouse Tier-1 incumbent #1 NEW VERTICAL + data_warehouse Tier-1 incumbent #2 (after Snowflake) + data_catalog Tier-1 5th-sibling (after '
    'Informatica 457 + Collibra 458 + Alation 459 + Atlan 460) + data_lineage Tier-1 5th-sibling + data_governance Tier-1 7th-sibling + data_mesh Tier-1 2nd-sibling '
    '(after Atlan 460) + data_products Tier-1 2nd-sibling (after Atlan 460) + AI-Governance 7th-sibling + privacy_automation 9th-sibling + compliance_automation 17th-sibling. '
    '<strong>ml_ops + model_risk_management + AI_governance + ml_feature_store + model_monitoring + audit_trail cohort now 2-vendor-deep (Domino 461 + Databricks 462)</strong>; '
    'data_lakehouse NEW VERTICAL opens with Databricks 462 as Tier-1 incumbent #1. The chunk ships at '
    '<a href="chunks/chunk_288.html">chunk_288.html</a> with canonical 6-vendor ml_ops Tier-1 cohort comparison table '
    '(Domino 461 + Databricks 462 + Snowflake + SageMaker + Vertex AI + W&amp;B) + 5-question audit-gap opener + EU AI Act Art. 9/10/12/13/14/15/Annex III 4 + '
    'Aug 2026 GPAI enforcement + ISO 42001 + India-DPDP-Act-2023 + Schrems II + NIST AI RMF + MITRE ATLAS + OWASP LLM Top 10 coverage matrix; '
    'cold-email template at <a href="cold_email/templates/462_databricks.md">template 462_databricks.md</a>; lead row 462 in '
    '<code>cold_email/leads.csv</code> + <code>cold_email/leads_with_emails.csv</code>.</p></article>'
)

new_text = text[:insert_pos] + summary + text[insert_pos:]
INDEX.write_text(new_text, encoding="utf-8")

# Verify
final = INDEX.read_text(encoding="utf-8")
assert 'id="chunk-288"' in final
n_288 = final.count('id="chunk-288"')
n_287 = final.count('id="chunk-287"')
n_286 = final.count('id="chunk-286"')
print(f"INDEX OK: chunk-286 count={n_286}, chunk-287 count={n_287}, chunk-288 count={n_288}")
assert n_288 == 1, f"chunk-288 expected 1, got {n_288}"
assert n_287 == 1, f"chunk-287 expected 1, got {n_287}"
assert n_286 == 1, f"chunk-286 expected 1, got {n_286}"

# Verify chunk-287 still in index.html (verify no clobber)
assert "data-lead=\"461\"" in final, "chunk-287 lost data-lead"
assert "data-lead=\"460\"" in final, "chunk-286 lost data-lead"
assert "data-lead=\"462\"" in final, "chunk-288 lost data-lead"
# Verify chunk-288 ordering (should appear after chunk-287)
pos_286 = final.find('id="chunk-286"')
pos_287 = final.find('id="chunk-287"')
pos_288 = final.find('id="chunk-288"')
assert pos_286 < pos_287 < pos_288, f"WRONG ORDER: 286={pos_286} 287={pos_287} 288={pos_288}"
print(f"ORDER OK: 286({pos_286}) < 287({pos_287}) < 288({pos_288})")
print("INDEX VERIFY: PASS")
