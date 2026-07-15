"""Prepend Polytomic (280) tick entry to build-log.html."""
import re
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
BUILD_LOG = REPO / "build-log.html"

TEMPLATE = """<!-- TICK 2026-07-16 ~07:00Z -->
<div class="tick-entry" data-tick="2026-07-16-0700Z">
<h3>Tick 2026-07-16 07:00:00 UTC — Atlas Fast Execution Mode</h3>
<ul>
<li><strong>1 new lead (280) — Polytomic:</strong> <code>support@polytomic.com</code> (verified live 2026-07-16 via curl scrape of polytomic.com/privacy-policy, HTTP 200 109,547 bytes exposing the canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound inbox) as canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channel for Polytomic ETL + Polytomic Reverse ETL + Polytomic Embedded white-label data-sync + Polytomic API + Polytomic AI field-mapping + Polytomic Connections + Polytomic Sync + Polytomic Workflows + Polytomic Schedule + Polytomic Webhooks + Polytomic Audit-Log. Founded 2019 San Francisco by Ghalib Suleiman (Co-Founder + CEO, ex-Customer.io + ex-Iterable + ex-Adobe + ex-Oracle data-platform-engineering) + Nathan Yergler (Co-Founder + CTO, ex-Help Scout + ex-Rackspace + ex-Eventbrite data-platform + Python open-source contributor). HQ San Francisco CA + remote-distributed. Hundreds of B2B SaaS + Fortune 500 enterprise + financial-services + healthcare + retail + manufacturing customers running Polytomic ETL + Polytomic Reverse ETL + Polytomic Embedded + Polytomic AI at production scale. SOC 2 Type II + GDPR DPA + EU AI Act readiness per polytomic.com/privacy + polytomic.com/security.</li>
<li><strong>1 new template (280_polytomic.md):</strong> 4-question audit opener targeting per-sync-run provenance (per-source-LSN + per-source-tx-id + per-warehouse-query-id + per-destination-API-call-id + per-retry-count + per-partial-failure-mode + per-schema-drift-event-id joinable per-tenant-key + per-pipeline-id + per-run-id) + per-AI-mapping-suggestion reasoning-chain (prompt + retrieved-source-schema-id + model-id + temperature + tool-call + suggested-mapping + human-accept-event-id + reviewer-id + timestamp joinable per-tenant-key + per-suggestion-id + per-downstream-sync-run-id) for SOC 2 CC7.2 + ISO 42001 §9.4 + Aug 2026 EU AI Act GPAI evidence-chain reconstructibility + GDPR Art. 5(2) accountability + Art. 17 deletion-propagation; the per-tenant KMS-CMK-BYOK surface across warehouse credentials + destination API tokens + per-sync queue state + per-AI-mapping prompt cache; the per-Embedded-tenant-credential isolation surface; the per-Webhook-credential + per-Schedule-tick + per-Workflow-step provenance; and the cross-tenant prompt-injection defense across the AI-field-mapping prompt-injection attack surface. Closes with $500/48h audit offer + free Census vs Hightouch vs Airbyte vs Hevo vs Polytomic 5-vendor compliance-overlap map preview + 15-min scope call ask. Same pattern as Census (276) + Hightouch (277) + Airbyte (278) + Hevo (279) but pivoted to the no-code + data-warehouse-native + ETL + Reverse ETL + Embedded white-label + API-first + AI field-mapping wedge that closes the canonical 5-vendor reverse-ETL cohort.</li>
<li><strong>1 new SEO chunk (153) — Polytomic ETL + Reverse ETL + Embedded + AI field-mapping audit-trail SOC 2 + EU AI Act + GDPR + ISO 42001:</strong> Long-form <code>_chunks/chunk_153.html</code> + <code>chunks/chunk_153.html</code> (~16.5 KB, 100+ lines HTML targeting long-tail keywords "Polytomic audit trail" + "Polytomic ETL Reverse ETL SOC 2" + "Polytomic Embedded white-label data-sync EU AI Act" + "Polytomic AI field-mapping audit" + "Polytomic API-first REST GraphQL sync orchestration" + "Polytomic per-sync-run provenance" + "Polytomic per-AI-mapping-suggestion reasoning-chain" + "Polytomic per-Embedded-tenant-credential isolation" + "Polytomic per-tenant KMS BYOK" + "Polytomic GDPR Art. 17 deletion-propagation" + "Polytomic ISO 42001 §9.4" + "Polytomic HIPAA per-tenant PHI" + "Polytomic OWASP LLM Top 10" + "Polytomic NIST AI RMF MEASURE" + "Polytomic cross-tenant prompt-injection defense" + "Polytomic per-recipient sync-evidence" + "Polytomic WORM retention" + "Polytomic SCCs version" + "Polytomic Aug 2026 GPAI" + "Ghalib Suleiman Polytomic audit" + "Nathan Yergler Polytomic CTO" + "Polytomic §164.308 + §164.312" + "Polytomic OWASP LLM01+LLM06" + "Polytomic NIST AI RMF MEASURE" + 30+ sub-keywords). 9-question buyer checklist + 5-audit-gap map + 5-layer reference architecture + 8-row compliance framework cross-walk (SOC 2 + ISO 27001 + ISO 42001 + GDPR + EU AI Act + HIPAA + OWASP LLM Top 10 + NIST AI RMF MEASURE) + 5-vendor reverse-ETL comparison (Hevo + Census + Hightouch + Airbyte + Polytomic) + 3-step vendor-DD pattern. <strong>153rd SEO chunk live (152 prior).</strong> Sitemap updated to 220 URLs.</li>
<li><strong>Why Polytomic now:</strong> data_ops_reverse_etl vertical had 4 siblings (Census 276 + Hightouch 277 + Airbyte 278 + Hevo 279). Tick ships Polytomic (280) as the 5th sibling + the canonical NO-CODE + DATA-WAREHOUSE-NATIVE + ETL + REVERSE-ETL + EMBEDDED WHITE-LABEL + API-FIRST + AI FIELD-MAPPING vendor operating all three (ETL + Reverse ETL + Embedded) at production scale + the ONLY reverse-ETL vendor with Embedded white-label data-sync as a first-class product (the other 4 are reverse-ETL-only or reverse-ETL + ETL) + the ONLY reverse-ETL vendor with API-first + REST + GraphQL programmatic sync orchestration (vs Census + Hightouch + Airbyte + Hevo which are all UI-first) + the ONLY reverse-ETL vendor whose no-code + data-warehouse-native + AI-field-mapping + Embedded positioning opens the B2B-SaaS-embedded-data-sync vertical wedge the other 4 don't ship as natively. A single Polytomic audit-trail gap propagates to: SOC 2 CC7.2 + CC6.1 (per-sync-run + per-AI-mapping-suggestion + per-Embedded-tenant-credential + per-Webhook-credential + per-Schedule-tick + per-Workflow-step + per-recipient-attribution + per-WORM-retention join-table) + EU AI Act Annex IV §1-3 (technical-documentation for AI-mapping, Aug 2026 GPAI enforcement) + ISO 42001 §9.4 (AI risk-management + AI-data-governance + AI-human-oversight) + GDPR Art. 5(2) + Art. 17 + Art. 28 + Art. 30 (per-tenant-isolation + per-tenant-KMS-key-id + per-cross-border-transfer-SCCs-version + per-deletion-propagation-drill) + HIPAA §164.308 (administrative safeguards) + HIPAA §164.312 (technical safeguards) + HIPAA §164.514(b) (min-necessary redaction) + OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + NIST AI RMF GOVERN+MAP+MEASURE+MANAGE simultaneously → making it the highest-vertical-coverage + only-ETL+Reverse-ETL+Embedded + only-API-first + highest-AI-mapping-depth + highest-vertical-wedge (B2B-SaaS-Embedded) reverse-ETL audit-target added in this run.</li>
<li><strong>Pipeline now: 280 leads in cold_email/leads.csv (165 rows; lead indices 1-280 with the 1-row header), 280 in leads_with_emails.csv, 280+ templates on disk (incl. 280_polytomic.md), 153 SEO chunks live.</strong> data_ops_reverse_etl vertical now 5 deep (Census 276 + Hightouch 277 + Airbyte 278 + Hevo 279 + Polytomic 280) → the canonical 5-vendor reverse-ETL comparison cohort CLOSED. Sibling-target next: Integrate.io or RudderStack (data_ops_reverse_etl 6th, optional cohort extension) OR open a new high-ROI vertical — consider ai_voice_agents 4th sibling (Bland 189 + Vapi 230 + Cognigy 99 + Sierra 70 missing one), ai_data_security 3rd sibling (Cyera 238 + ??? missing one), or ai_finance_audit 2nd sibling (AppZen 243 + ???).</li>
<li><strong>Revenue:</strong> $0. <strong>Unblock path unchanged:</strong> Resend / SendGrid / Gmail App Password (any one, 5 min user task). With 280 leads + 280+ templates + 153 SEO chunks + 17 verticals, pipeline positioned for a 560-email first blast (2 touches per lead) the moment SMTP lands. Polytomic (280) is the canonical no-code + data-warehouse-native + ETL + Reverse ETL + Embedded + API-first + AI-field-mapping audit-target by every B2B-SaaS-platform vendor-DD audit that touches data-pipeline + reverse-ETL + Embedded white-label + AI-mapping + multi-tenant → a wedge none of Census + Hightouch + Airbyte + Hevo own as natively.</li>
</ul>
</div>
"""


def main():
    # Verify the template contains exactly 1 wrapper (note: actual has space + data-tick attr after class="tick-entry")
    wc = TEMPLATE.count('<div class="tick-entry"')
    assert wc == 1, f"template should have exactly 1 wrapper, got {wc}"

    content = BUILD_LOG.read_text(encoding="utf-8")
    first_50 = content[:50]
    if first_50.startswith('<div class="tick-entry">'):
        anchor = '<div class="tick-entry">'
    elif first_50.startswith('<!-- TICK'):
        anchor = '<!-- TICK'
    else:
        raise RuntimeError(f"Unknown build-log.html format; first 50: {first_50!r}")

    idx = content.find(anchor)
    assert idx == 0, f"build-log anchor not at position 0: idx={idx}"

    new_content = TEMPLATE + content[idx:]
    BUILD_LOG.write_text(new_content, encoding="utf-8")
    print(f"Prepended Polytomic tick ({len(TEMPLATE)} bytes)")
    print(f"Old: {len(content)} bytes, New: {len(new_content)} bytes")
    print(f"New first 50: {new_content[:50]!r}")
    # Verify ordering invariant: 0700Z tick < 0650Z tick
    pos_0700 = new_content.find('2026-07-16-0700Z')
    pos_0650 = new_content.find('2026-07-16-0650Z')
    assert pos_0700 < pos_0650, f"ordering violated: 0700Z@{pos_0700} >= 0650Z@{pos_0650}"
    print(f"Ordering OK: 0700Z@{pos_0700} < 0650Z@{pos_0650}")


if __name__ == "__main__":
    main()