# Lead 61 — Clay

**Vertical:** data_enrichment
**Tier:** 1
**Website:** https://www.clay.com/
**Founder contact:** Kareem Amin
**Verified public inbox:** team@clay.com

---

**Subject:** 5 audit questions for Clay's enrichment-to-outbound evidence trail

Hi Kareem,

Clay turns many provider lookups, formulas, AI prompts, enrichment signals, and CRM writes into a single GTM workflow. For an enterprise buyer, the diligence question is concrete: can they reconstruct why each enriched field or personalized line was produced, what source supported it, which policy allowed it, and what changed downstream?

I run a focused **$500 / 48-hour audit** for production AI workflows. These are the five questions I would test on one Clay prospect-to-CRM route:

1. **Row-level provenance:** Can one export join tenant, workspace, table and row, source provider, source response, normalization, formula or prompt version, model output, confidence, human override, CRM mutation, timestamp, and attributed cost?
2. **Provider and license governance:** Can customers prove which provider supplied every company or person field, what use and retention rights applied at that moment, and how consent, suppression, correction, and deletion propagate through cached and derived data?
3. **Hostile data and prompt injection:** What stops attacker-controlled websites, scraped text, imported CSV cells, provider payloads, and webhook results from steering AI formulas or leaking adjacent row, tenant, connector, or secret context?
4. **Tenant, credential, and destination isolation:** Can Clay demonstrate that tables, enrichment credits, API keys, OAuth tokens, model context, caches, exports, and CRM destinations stay isolated across workspaces, tenants, roles, and regions?
5. **Change, rollback, and incident evidence:** When a provider changes schema, a prompt drifts, a formula is edited, or a bad enrichment fans out to thousands of emails or CRM records, can the team identify every affected row, stop the run, roll back downstream state, and preserve WORM-capable evidence?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 9, 12, 14, and 15; GDPR Articles 5, 6, 17, 22, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; CAN-SPAM; and CCPA/CPRA**. I test one live prospect-to-CRM route end to end rather than sending a generic checklist.

**Why Clay specifically:** enrichment and AI personalization compress research and execution into one surface. That speed is valuable, but one unsupported field can silently become segmentation, copy, scoring, and a downstream CRM write. A defensible evidence spine turns that compounding-risk surface into a stronger procurement and incident-response story.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Clay prospect-to-CRM route tested end to end
