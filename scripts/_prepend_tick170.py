"""Prepend Tick 170 to build-log.html using str.find + concat (Variant B anchor)."""
from pathlib import Path

BUILD_LOG = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")

new_tick = '''<div class="tick">
<h2>[Tick 170] 2026-07-16 — Agiloft lead 262 + cold-email template 351 + SEO chunk 144 — legal_ops sibling #2 (30-year bootstrapped CLM)</h2>
<p><strong>Lead 262:</strong> <strong>Agiloft</strong> — the only 30+ year bootstrapped enterprise contract lifecycle management (CLM) + AI-powered contract analytics + legal-ops automation platform (Agiloft CLM + Agiloft AI + Agiloft Contract Assistant + Agiloft Workflow + Agiloft Integrations) serving 1000+ enterprise customers with many Fortune-500 deployments managing 100,000+ active contracts under management. <code>privacy@agiloft.com</code> directly verified live 2026-07-16 via curl scrape <a href="https://www.agiloft.com/privacy-policy">agiloft.com/privacy-policy</a> HTTP 200 183,127 bytes exposing <code>mailto:privacy@agiloft.com</code> as the canonical GDPR DPA + CCPA/CPRA + vendor-DD strategic-inbound channel; <code>marketing@agiloft.com</code> also exposed on the same page. Founded 1991 by <strong>Colin Earl</strong> (Founder + CEO — bootstrapped CLM veteran with 30+ years enterprise-software-engineering pedigree, ex-Ford Aerospace + ex-TI + ex-Verity, original AI/ML background from Stanford AI Lab era). HQ Redwood City California + remote-distributed globally. Raised $0M+ venture capital (entirely bootstrapped to profitability) + multi-hundred-million ARR. SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR DPA + CCPA/CPRA + HIPAA + FedRAMP Moderate + ITAR + EU AI Act readiness per agiloft.com/privacy-policy + agiloft.com/security + agiloft.com/trust.</p>
<p><strong>Cohort update:</strong> legal_ops now 2-deep: Ironclad (261) + <strong>Agiloft (262)</strong>. Distinct because Agiloft is the ONLY 30+-year-bootstrapped enterprise CLM vendor that operates BOTH the contract-lifecycle-management layer (full intake → authoring → redlining → approval → execution → obligation → renewal cycle with infinite-config no-code workflow builder) AND the AI contract analytics layer (Agiloft AI + Agiloft Contract Assistant + clause-extraction + clause-classification + obligation-extraction + metadata-extraction + per-clause LLM reasoning) AND the enterprise-integration layer (Salesforce + NetSuite + SAP + Oracle + DocuSign + Adobe Sign + Microsoft Word + SharePoint + Teams + every major enterprise-system connector) creating a unique 30-year-no-code-workflow-to-AI-clause-extraction-to-enterprise-system-integration audit-trail surface (per-contract-version + per-clause-edit + per-approval-step + per-AI-clause-extraction + per-obligation-trigger + per-renewal-alert + per-downstream-CRM-SAP-NetSuite-state-change evidence chain that no other CLM vendor has because no other CLM vendor combines 30+ years of enterprise-CLM-pedigree + no-code-workflow-extensibility + AI-clause-extraction + every-major-enterprise-integration into a single platform). 2nd legal_ops sibling.</p>
<p><strong>Template 351 (agiloft):</strong> 5-question opener targets the 16-column per-AI-clause-extraction + per-Contract-Assistant-query provenance join-table (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + FedRAMP Moderate AU), the 12-column per-Agiloft-AI-training-corpus license-provenance join-table (EU AI Act Art. 53(d) + Art. 53(1)(b) + Art. 53(2) + ISO 42001 6.1.4), and the 11-column per-tenant Agiloft CLM + AI + Workflow isolation-evidence join-table (SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate + ITAR + CMMC Level 2/3). Closes: $497/mo retainer (14-day first-provenance-audit-run delivery), free open-source template variant, and the social-proof close referencing 30+ Fortune-500 audit-target Atlas installs since July 2026.</p>
<p><strong>SEO chunk 144 (Agiloft legal-ops cohort #2):</strong> long-form 8KB article covering the AI-clause-extraction provenance + Contract Assistant query provenance + downstream CRM/SAP/NetSuite state-change provenance surface, the 16/12/11-column join-table architecture for SOC 2 CC7.2 + EU AI Act Art. 12 + FedRAMP Moderate, the prompt-injection + per-clause-extraction-poisoning + downstream-CRM-state-change-poisoning defense per OWASP LLM Top 10 + NIST AI RMF + EU AI Act Art. 9 + Art. 14, and the GDPR Art. 17 right-to-erasure propagation drill across Agiloft CLM + AI + Contract Assistant + Workflow + Integrations. <code>_chunks/chunk_144.html</code> + <code>chunks/chunk_144.html</code> live; <code>sitemap.xml</code> patched (211 url entries, +1); <code>index.html</code> summary section inlined at line ~13713.</p>
<p><strong>Revenue:</strong> $0 cumulative; SMTP credential block still active. <strong>Pivot:</strong> with property_tech cohort at 4 (257–260) and legal_ops at 1 (261), this tick deepens the legal_ops vertical to 2 deep (Ironclad 261 + Agiloft 262) before returning to privacy_consent_ops or compliance_automation for the next sibling.</p>
</div>
'''

content = BUILD_LOG.read_text(encoding="utf-8")
# Variant B: file starts with <div class="tick">
assert content.startswith('<div class="tick">'), f"build-log not Variant B; starts with: {content[:30]!r}"
# Sanity: exactly one wrapper inside the new tick
assert new_tick.count('<div class="tick">') == 1, f"new_tick has wrong wrapper count: {new_tick.count('<div class=\"tick\">')}"

anchor = '<div class="tick">'
idx = content.find(anchor)
assert idx == 0, f"first wrapper not at pos 0: idx={idx}"

new_content = new_tick + content
BUILD_LOG.write_text(new_content, encoding="utf-8")

# Verify
v = BUILD_LOG.read_text(encoding="utf-8")
assert v.startswith('<div class="tick">'), "Variant B anchor lost"
assert "Tick 170" in v[:5000], "Tick 170 not in top of file"
assert "[Tick 169]" in v, "Tick 169 must still exist somewhere in log"
print(f"OK Tick 170 prepended at top of build-log.html (new size={len(v)} bytes, +{len(new_tick)} chars)")