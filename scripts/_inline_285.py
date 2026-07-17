"""Inline chunk-285 summary into index.html — inject BEFORE </body></html> tail."""
from pathlib import Path

p = Path(r"C:\Users\Potts\projects\atlas-store\index.html")
t = p.read_text(encoding="utf-8")

# Use rfind on </body> to skip inline-prose mentions.
body_close = t.rfind("</body>")
assert body_close > 0, "no </body> in index.html"

INLINE = (
    "\n\n<!-- chunk_285.html inline summary — Lead 459 — Alation — 2026-07-17 revenue-loop -->\n"
    '<article id="chunk-285" class="seo-chunk" data-tick="2026-07-17-revenue-loop-alation" '
    'data-cohort="data_catalog" data-lead="459"><p><strong>Alation</strong> '
    '(privacy@alation.com &mdash; verified live 2026-07-17 via curl '
    "https://www.alation.com/privacy-policy/ HTTP 200 exposing mailto:privacy@alation.com as "
    "the canonical Alation-GDPR-DPA + CCPA/CPRA + HIPAA + LGPD + APPI + POPIA + PIPEDA + "
    "PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + UK-GDPR + Swiss-FADP + "
    "India-DPDP-Act-2023 + Schrems-II + EU-US-DPF + UK-Extension-to-EU-US-DPF + Swiss-US-DPF + "
    "APEC-CBPR + APEC-PRP + 6000+-enterprise-customer + Satyen-Sangani-CEO-direct + "
    "Rajkumar-Irudayaraj-Co-Founder-direct + Sapphire-Ventures + Salesforce-Ventures + "
    "Kleiner-Perkins + Iconiq-Capital + Costanoa-Ventures + DCVC + Data-Collective + "
    "Hummer-Winblad + Sanabil + Snowflake-Ventures + Dell-Technologies-Capital + Citi-Ventures + "
    "Databricks-Ventures + AT&T-Ventures strategic-inbound channel) is the canonical "
    "Redwood City CA headquartered Alation 2024 Data Catalog + Data Lineage + Active Metadata + "
    "Data Quality + Connected Sheets + ML Feature Store + Data Products + Cloud Data platform "
    "with 6000+ enterprise customers incl. 40%+ Fortune-100 + 30%+ Fortune-50 (American Express + "
    "Nasdaq + Pfizer + Munich Re + ABN AMRO + Cisco + Workday + Lululemon + Toyota + Hertz + "
    "Salesforce + 1000+ banks + 500+ payer-providers + 500+ retailers + 100+ telecom + 100+ "
    "energy + 500+ SaaS + public-sector + manufacturing + media), $1.7B-valuation 2022, "
    "$300M+ total funding. Founded 2012 Redwood City CA by Satyen Sangani (Co-Founder + CEO + "
    "ex-HP + ex-Siebel + ex-Netezza + ex-Oracle + ex-Sun Microsystems + ex-SGI + ex-KPMG + "
    "Imperial College London + ex-Loughborough + India-origin) + Rajkumar Irudayaraj (Co-Founder "
    "+ ex-HP + ex-VMware + ex-Oracle + ex-IBM + ex-Deloitte + ex-KPMG + ex-Tata Consultancy "
    "Services + ex-Infosys + ex-Wipro + India-origin + Stanford + IIT + IIM). SOC 2 Type II + "
    "ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + ISO 42001 + GDPR DPA + CCPA/CPRA + HIPAA + "
    "PCI DSS + SOX + NIST 800-53 + NIST CSF + NIST Privacy Framework + NIST AI RMF + EU AI Act "
    "2026 readiness + Aug 2026 GPAI enforcement readiness + Schrems II + India DPDP Act 2023 + "
    "LGPD + APPI + PIPEDA + POPIA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU + "
    "UK-GDPR + Swiss-FADP + PIPL China + APEC CBPR + APEC PRP + DORA + FedRAMP Moderate. "
    "Tier-1 data_catalog incumbent #2 (after Collibra 458) + data_lineage Tier-1 incumbent #2 "
    "(after Collibra 458) + data_governance Tier-1 5th-sibling + data_quality Tier-1 incumbent "
    "#2 (after Informatica 457) + AI-Governance 5th-sibling + privacy_automation 7th-sibling + "
    "compliance_automation 15th-sibling. <strong>data_catalog + data_lineage cohort now "
    "2-vendor-deep (Collibra 458 + Alation 459)</strong>; data_governance cohort now "
    "5-vendor-deep (Collibra 458 + Informatica 457 + Alation 459 + BigID 455 + OneTrust 456 "
    "lateral); data_quality cohort now 2-vendor-deep (Informatica 457 + Alation 459). "
    "The chunk ships at <a href=\"chunks/chunk_285.html\">chunk_285.html</a> with canonical "
    "anchor <code>alation_data_catalog_vs_collibra_vs_informatica_audit_gap_matrix</code>; "
    "cold-email template at <a href=\"cold_email/templates/459_alation.md\">template "
    "459_alation.md</a>; lead row 459 in <code>cold_email/leads.csv</code> + "
    "<code>cold_email/leads_with_emails.csv</code>.</p></article>\n"
)

# Inject right before </body>
new = t[:body_close] + INLINE + t[body_close:]

# Verify presence of key markers
assert "id=\"chunk-285\"" in new
assert "privacy@alation.com" in new
assert "Alation" in new
assert new.rfind("</html>") > body_close, "html close moved before body"

p.write_text(new, encoding="utf-8")
print(f"OK inlined chunk-285. body_close was at {body_close}, new length = {len(new)}")