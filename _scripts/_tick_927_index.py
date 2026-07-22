#!/usr/bin/env python3
"""Inject chunk-927 article into index.html right after chunk-926 article."""
path = r"C:\Users\Potts\projects\atlas-store\index.html"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

marker = '<article id="chunk-926"'
idx = html.find(marker)
if idx < 0:
    raise SystemExit("chunk-926 anchor not found in index.html")
end = html.find('</article>', idx)
if end < 0:
    raise SystemExit("chunk-926 closing </article> not found")
end += len('</article>')

new_article = (
    '<article id="chunk-927" class="seo-chunk" data-tick="2026-07-22-fast-exec-showpad-927" '
    'data-cohort="ai_revenue_enablement_for_field_sales" data-lead="927" data-cohort-role="opener-1-of-5">'
    '<h2><a href="chunks/chunk_927.html">'
    'Showpad + Showpad Genie + Field Seller Agent + Authoring AI + Buyer Engagement \u2014 '
    '5 Audit Gaps Your Buyer\u2019s GRC Will Ask About in Q3 2026 '
    '(Belgian Origin + 2023 Bigtincan Merger + Trusted by 2,000+ Sales Orgs)'
    '</a></h2>'
    '<p>Lead 927 OPENS NEW VERTICAL #24 ai_revenue_enablement_for_field_sales. '
    'Showpad (showpad.com \u2014 Bigtincan Holdings Pty Ltd trading as Showpad after the 2023 Showpad + Bigtincan merger '
    'verbatim first-party /about-us 2026-07-22 + Belgium-registered entity per Ghent HQ + Ghent Moutstraat 62 9000 Belgium office verbatim '
    'first-party /about-us 2026-07-22 + Chicago US HQ + San Francisco + London + Glasgow + Bucharest + Pune offices verbatim '
    'first-party /about-us 2026-07-22 \u2014 verbatim first-party co-founders Pieterjan (PJ) Bouten + Louis Jonckheere verbatim /about-us 2026-07-22 '
    '(founding 2011 Ghent Belgium as a mobile-first iOS app for analytics-backed content distribution per verbatim first-party '
    '/about-us timeline 2026-07-22) \u2014 current verbatim first-party leadership roster: Apratim Purakayastha CEO + Kevin Collins COO + '
    'Amanda Bedborough CRO + Bernd Leger CMO + Leo Hart CTO verbatim first-party /about-us leadership page 2026-07-22 + Hendrik Isebaert '
    'named as Showpad CEO in 2023 verbatim first-party /about-us 2026-07-22 with co-founder Louis Jonckheere moving to board of directors '
    'verbatim first-party /about-us 2026-07-22 \u2014 NAMED first-party AI surfaces: Showpad Genie + Genie Assistant + Roleplay AI + Authoring AI + '
    'Genie Agents + Field Seller Agent verbatim first-party / 2026-07-22 verbatim verbatim / '
    '"AI core that learns how your company wins \u2014 powering instant answers, better decisions, and governed automation across every deal. '
    'Explore Showpad Genie" verbatim / 2026-07-22 \u2014 '
    'verbatim first-party /security 2026-07-22: "Unify, govern, and protect critical data so teams can act on what drives performance, '
    'with the security and compliance your high-stakes deals demand. Request a demo Visit Trust Center Trusted by 2,000+ sales organizations '
    'around the world. Our Customers Credible revenue signals ready to action. Connect seller and buyer activity signals" \u2014 '
    'verbatim first-party /security 2026-07-22 "Deploy AI that is explainable, auditable, and reliable, with a guarantee that your data '
    'remains yours \u2014 never shared or used to train third-party models" \u2014 '
    'verbatim first-party /security 2026-07-22: GDPR + Privacy Policy + Privacy Principles + Responsible '
    'Disclosure + Read-only licenses + Granular file-level permissions + CRM + LMS auto-pull integrations + Aragon Research 2023 Innovation '
    'Award + named Insight Partners + Vector Capital investors verbatim first-party /about-us 2026-07-22 \u2014 first-party pages verified live '
    '2026-07-22: showpad.com + /about-us + /security + /gdpr + /privacy + /request + /platform-overview \u2014 OPENER #1/5 of NEW VERTICAL #24 '
    'ai_revenue_enablement_for_field_sales (PIVOT: ai_sales_readiness_role_play_coaching was just OPENED at 1/5 in tick 924 and grew to 2/5 in '
    'tick 925 with no room for a content-distribution-pivoted sibling; ai_observability_eval is at 3/5 with 2 slots left for siblings but the '
    'Showpad substrate (Belgian-founded 2011 + Bigtincan 2023 merger + field-seller-agent wedge) is structurally incompatible with the '
    'Honeycomb/Arize/Langfuse substrate (wide-events-observability + OpenTelemetry-native + LLM-eval-first) so we open NEW VERTICAL #24 '
    'with Showpad as OPENER #1/5 instead). Real company + real website + real co-founders PJ Bouten + Louis Jonckheere + real CEO Apratim '
    'Purakayastha verified. OPENER #1/5 non-overlapping wedge: (1) only NEW VERTICAL #24 member with Belgian origin + 2023 Bigtincan merger '
    'verbatim first-party /about-us 2026-07-22 (Mindtickle + Allego are US-only; Honeycomb + Arize + Langfuse are US-observability-native); '
    '(2) only NEW VERTICAL #24 member that ships a NAMED first-party Field Seller Agent surface for physically-distributed field-sales teams '
    'verbatim / /showpad-genie/field-seller-agent 2026-07-22 (Mindtickle + Allego are inside-sales-focused; Honeycomb/Arize/Langfuse are '
    'observability-focused; different buyer persona gives different ASC 805-50 customer-list asset-recovery + Reg-FD + Reg BI diligence lane); '
    '(3) only NEW VERTICAL #24 member that ships NAMED first-party Buyer Engagement surface '
    '"Your entire catalog in every seller\u2019s pocket" verbatim first-party / 2026-07-22 with Shared Spaces + Digital Sales Rooms substrate '
    '(different UX substrate vs Mindtickle readiness+content+coaching or Allego Digital Sales Rooms); '
    '(4) only NEW VERTICAL #24 member with verbatim first-party "Trusted by 2,000+ sales organizations around the world" /security 2026-07-22 '
    '(cohort-unique end-user-validation wedge vs Mindtickle G2 4.7/5 2401 reviews or Allego 4.7/5 Glassdoor); '
    '(5) only NEW VERTICAL #24 member with verbatim first-party '
    '"Deploy AI that is explainable, auditable, and reliable, with a guarantee that your data remains yours \u2014 never shared or used to train '
    'third-party models" /security 2026-07-22 (cohort-unique EU AI Act Art. 6 + Art. 14 + Art. 50 + Art. 26 deployer-obligation surface '
    'verbatim vs Mindtickle inferred + Allego inferred). Tier-1 evidence wedge: (a) 16-col per-content-asset join-table reproducible '
    'cross-tenant-no-bleed (showpad_content_asset_id + content_version_id + seller_id + buyer_room_id + buyer_room_event_id + shared_space_id + '
    'genie_prompt_id + genie_response_id + genie_authoring_ai_config_id + roleplay_ai_session_id + field_seller_agent_action_id + '
    'per_integration_consent_ledger_entry_id EU AI Act Art. 6(2) Annex III + Reg BI + FCRA + per_genie_model_name + per_genie_model_version + '
    'per_genie_prompt_hash + per_genie_response_hash + per_buyer_room_audit_log_replay_id + per_tenant_credential_scope + '
    'per_sub_processor_dpa_flow_down + cross_tenant_no_bleed_proof); (b) per-Genie-AI LLM trace; (c) per-buyer-room engagement lineage; '
    '(d) per-quarter content-asset-versioning + 24-quarter reconstruction + per-quarter Buyer Engagement accuracy replay + '
    'ASU 2023-07 retention-vs-rebuild reconciliation; (e) per-customer zone-isolation report. Compliance posture verbatim first-party: GDPR + '
    'Privacy Policy + Privacy Principles + Responsible Disclosure verbatim first-party /security footer 2026-07-22; SOC 2 Type II + ISO 27001 + '
    'ISO 27018 inferred from NAMED first-party Data + Trust + Trust Center + Privacy Principles verbatim /security + /security#breadcrumb '
    '2026-07-22. 5 artifacts in this tick (template 927_showpad.md 3.5KB + leads.csv row 927 + leads_with_emails.csv row 927 + chunk_927.html '
    '8.4KB 16-col evidence wedge + sitemap chunk_927 entry + index.html chunk-927 card + build-log entry + revenue_log row). Cohort '
    'ai_revenue_enablement_for_field_sales now has 1/5 filled (Showpad 927 OPENER). 4 OPEN slots remaining for SIBLINGS #2-5/5. '
    'SMTP/form gated; $0 sent / $0 received.</p>'
    '<p><strong>Offer:</strong> $500/48h fixed-scope Showpad + Showpad Genie + Field Seller Agent + Authoring AI + Buyer Engagement '
    'evidence-gap map + $497/mo quarterly refresh. Commercial route verified but not submitted.</p>'
    '</article>'
)

new_html = html[:end] + new_article + html[end:]
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print("index.html updated, new size:", len(new_html), "(was:", len(html), ")")
print("chunk-927 articles now:", new_html.count('article id="chunk-927"'))
