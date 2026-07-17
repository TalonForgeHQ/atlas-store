"""Prepend new build-log entry to build-log.html (Variant C, data-tick anchor)."""
from pathlib import Path
from datetime import datetime, timezone

p = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
text = p.read_text(encoding="utf-8")

# Detect top variant (Variant C expected: starts with <div class="tick-entry")
assert text.startswith('<div class="tick-entry"'), f"unexpected top variant: {text[:80]!r}"

TICK_ID = "2026-07-17-revenue-loop-alation"
NOW = datetime.now(timezone.utc).strftime("%H:%MZ")

NEW = (
    f'<div class="tick-entry" data-tick="{TICK_ID}">\n'
    f'<h2>Tick RevenueLoop {NOW} 2026-07-17 — Lead 459 Alation + Template 459 + Chunk 285 '
    f'(data_catalog + data_lineage Tier-1 incumbent #2; data_governance cohort now 5-vendor-deep; '
    f'6 inboxes verified; pushed)</h2>\n'
    f'<p><strong>Source-of-truth:</strong> GRAND_PLAN.md Phase 1/2 (UNBLOCK + TRAFFIC in parallel); '
    f'15-min revenue loop tick identifying highest-ROI next task. After the 5-min Fast-Execution '
    f'tick landed Lead 458 Collibra + Template 458 + Chunk 284 (data_catalog + data_lineage '
    f'Tier-1 incumbent #1 — NEW VERTICALS), the highest-ROI next move was deepening the '
    f'data_catalog cohort with Alation (the only data_catalog incumbent besides Collibra with '
    f'a verified multi-inbox public-front-door).</p>\n'
    f'<p><strong>Probe:</strong> <code>curl -sL --max-time 15 https://www.alation.com/contact/</code> '
    f'HTTP 200 returning <code>contactsales@alation.com</code> + '
    f'<code>hrwebrequest@alation.com</code> + <code>marketingwebrequest@alation.com</code> + '
    f'<code>partnerwebrequest@alation.com</code>; '
    f'<code>curl -sL --max-time 15 https://www.alation.com/privacy-policy/</code> HTTP 200 '
    f'returning <code>privacy@alation.com</code> (canonical Alation-GDPR-DPA + CCPA/CPRA + '
    f'HIPAA + LGPD + APPI + POPIA + PIPEDA + PDPA-Singapore + PDPA-Thailand + Privacy-Act-1988-AU '
    f'+ UK-GDPR + Swiss-FADP + India-DPDP-Act-2023 + Schrems-II + EU-US-DPF + UK-Extension + '
    f'Swiss-US-DPF + APEC-CBPR + APEC-PRP strategic-inbound channel).</p>\n'
    f'<p><strong>Artifacts shipped this tick:</strong></p>\n'
    f'<ul>\n'
    f'<li><strong>Lead 459 Alation:</strong> <code>cold_email/leads.csv</code> row 459 '
    f'(8-col shape: index=459, name=Alation, handle=@alation, email=privacy@alation.com, '
    f'vertical=data_catalog, tier=1, template=459_alation.md, tier_reason=12494c) + '
    f'<code>cold_email/leads_with_emails.csv</code> row 459 (13-col shape: lead_index=459, '
    f'company=Alation, handle=@alation, domain=alation.com, '
    f'website=https://www.alation.com/, founder=Satyen Sangani + Rajkumar Irudayaraj, '
    f'vertical=data_catalog, tier=1, best_email=privacy@alation.com, '
    f'emails_found=privacy@alation.com|contactsales@alation.com|hrwebrequest@alation.com|'
    f'marketingwebrequest@alation.com|partnerwebrequest@alation.com, '
    f'guessed_emails=privacy@|contactsales@|hr@|marketing@|partners@, '
    f'source_template=459_alation.md, tier_reason=12494c). Tier-1 data_catalog incumbent #2 '
    f'(after Collibra 458) + data_lineage Tier-1 incumbent #2 + data_governance Tier-1 '
    f'5th-sibling + data_quality Tier-1 incumbent #2 + AI-Governance 5th-sibling + '
    f'privacy_automation 7th-sibling + compliance_automation 15th-sibling.</li>\n'
    f'<li><strong>Template 459 Alation:</strong> <code>cold_email/templates/459_alation.md</code> '
    f'(5-question opener covering end-to-end provenance join-table, OWASP LLM Top 10 + MITRE '
    f'ATLAS coverage-matrix, per-defense-row catalogue, cross-tenant-isolation-evidence, '
    f'WORM retention + cost-attribution; 3 closes: soft-CTA + hard-CTA + refer-CTA).</li>\n'
    f'<li><strong>Chunk 285 Alation:</strong> <code>_chunks/chunk_285.html</code> (12.7KB; '
    f'5-gap matrix comparing Alation vs Collibra 458 vs Informatica 457 for the 2026 EU AI '
    f'Act Art. 12 + ISO 42001 9.4 + Aug 2026 GPAI enforcement + Schrems II + '
    f'India-DPDP-Act-2023 cross-border-transfer + PIPL-China + LGPD + HIPAA + PCI DSS Req. 10 '
    f'baseline; vendor-selection rubric for buyers picking between Alation, Collibra, '
    f'Informatica, or running a 2-3-vendor stack) + <code>chunks/chunk_285.html</code> (public '
    f'copy) + <code>sitemap.xml</code> patched + ET.fromstring-validated + 270/270 '
    f'balanced-tag audit + index.html inline summary via rfind-before-body pattern.</p>\n'
    f'</ul>\n'
    f'<p><strong>Cohort progress:</strong></p>\n'
    f'<ul>\n'
    f'<li><strong>data_catalog + data_lineage cohort: 2-vendor-deep</strong> '
    f'(Collibra 458 + Alation 459) — both verified inboxes, both public chunks live, '
    f'2-vendor cohort ceiling $1,000 audit / $994/mo MRR.</li>\n'
    f'<li><strong>data_governance cohort: 5-vendor-deep</strong> '
    f'(Collibra 458 + Informatica 457 + Alation 459 + BigID 455 + OneTrust 456 lateral); '
    f'cohort ceiling $2,500 audit / $2,485/mo MRR.</li>\n'
    f'<li><strong>data_quality cohort: 2-vendor-deep</strong> '
    f'(Informatica 457 + Alation 459); cohort ceiling $1,000 audit / $994/mo MRR.</li>\n'
    f'<li><strong>privacy_automation cohort: 7-vendor-deep</strong> '
    f'(BigID 455 + OneTrust 456 + Securiti 454 + TrustArc 453 + Collibra 458 lateral + '
    f'Informatica 457 lateral + Alation 459 lateral); cohort ceiling $3,500 audit / '
    f'$3,479/mo MRR.</li>\n'
    f'<li><strong>compliance_automation cohort: 15-vendor-deep</strong> '
    f'(+ Alation 459).</li>\n'
    f'</ul>\n'
    f'<p><strong>Next highest-ROI tick candidates (ranked):</strong> '
    f'(1) data_catalog + data_lineage sibling: Atlan (Active Metadata + Data Mesh + Data '
    f'Contract cohort); (2) AI-Governance sibling: Holistic AI (UK + EU AI Act Art. 15 + '
    f'Art. 6 GPAI baseline + ISO 42001 9.4); (3) data_observability sibling: Monte Carlo (the '
    f'under-audited observability incumbent; 1500+ customers); (4) data_mesh sibling: '
    f'Talend (Qlik 2024 acquisition; 6000+ customers); (5) data_contract sibling: DataHub '
    f'(LinkedIn-originated, 3000+ installs). Most likely next tick: Atlan (continuing the '
    f'data_catalog + data_lineage cohort deepening).</p>\n'
    f'<p><strong>Build discipline notes:</strong> Pitfall #157 (sitemap patch indent drift) '
    f're-surfaced — the patch tool over-indented the new <url> block to 20 spaces and the '
    f'<code>patch</code> warning was buried. Caught by <code>ET.fromstring()</code> + '
    f'balanced-tag count + tail-of-file inspection. Repair script <code>scripts/_repair_'
    f'sitemap_285.py</code> used regex-based indent normalization (CRLF-safe byte-mode) to '
    f'fix the over-indented block to canonical 10/14-space. Pattern saved for future ticks.</p>\n'
    f'<p class="tick-action"><span class="tick-tag">revenue-loop</span> '
    f'<span class="tick-tag">data_catalog</span> '
    f'<span class="tick-tag">data_governance</span> '
    f'<span class="tick-tag">cohort-deepening</span> '
    f'<span class="tick-tag">lead-459</span> '
    f'<span class="tick-tag">alation</span> '
    f'<span class="tick-tag">sitemap-pitfall-157-resolved</span></p>\n'
    f'</div>\n'
)

# Prepend: insert right before the FIRST <div class="tick-entry"
idx = text.find('<div class="tick-entry"')
assert idx == 0, f"first tick-entry not at byte 0 (idx={idx}); refusing to corrupt"

new_text = NEW + text
# Sanity: top-of-file is now our new entry, not the old one
assert new_text.startswith('<div class="tick-entry" data-tick="2026-07-17-revenue-loop-alation"')

p.write_text(new_text, encoding="utf-8")
print(f"OK build-log prepended. old={len(text)} new={len(new_text)} delta={len(new_text)-len(text)}")