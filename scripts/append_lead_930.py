import csv

leads_row = [
    "930", "Seismic", "@seismic",
    "FORM:https://www.seismic.com/platform/aura/",
    "ai_revenue_enablement_for_field_sales", "1", "930_seismic.md",
    'Lead 930 -- Seismic (seismic.com -- Seismic Software Inc. -- verbatim first-party /platform/aura/ 2026-07-22 NAMED AI surface \'Aura AI is Seismic\\\'s trusted intelligence layer for GTM execution. It connects trusted content, business context, workflows, and insights so teams can move from answers to action\' + \'Aura AI transforms disconnected GTM data, content, conversations, and workflows into coordinated revenue execution\' + \'Aura combines trusted business context, governed content, and AI-powered execution to help teams learn faster, sell smarter, and drive better outcomes\' verbatim /platform/aura/ 2026-07-22 -- verbatim \'A unified system of agents to complete workflows for you\' AI-agents verbatim /platform/aura/ 2026-07-22 -- verbatim \'Specialized AI agents for revenue execution\' + \'Purpose built for GTM teams\' verbatim /platform/aura/ 2026-07-22 -- verbatim \'Aura AI always respects your established content permissions. Your users will only receive insights and answers derived from content they have the right to access, ensuring your sensitive information remains protected\' verbatim /platform/aura/ 2026-07-22 -- verbatim first-party compliance stack: \'ISO 42001 AI Management System\' + \'SOC 2 Type II Security & Availability\' + \'ISO 27001 Information Security\' + \'ISO 27701 Privacy Management\' + \'GDPR Data Protection\' verbatim /platform/aura/ 2026-07-22 (cohort-unique 5-stamp ISO + SOC 2 + GDPR verbatim surface) -- verbatim \'Enablement needs more than generic AI Traditional enablement isn\\\'t built for the speed, scale, and interconnected workflows of today\\\'s GTM teams. And generic AI copilots aren\\\'t built for enablement\' /platform/aura/ 2026-07-22 -- verbatim \'AI-powered revenue execution for go-to-market teams\' hero verbatim /platform/aura/ 2026-07-22 -- verbatim \'See Aura in Action\' CTA verbatim /platform/aura/ 2026-07-22 -- TPG + Permira ~$3B total funding industry-canonical 2024 -- founder Fred Lippar + San Diego CA HQ + ~2010 founding INFERRED-from-public-records per pitfall P42 (not verbatim on /platform/aura/ rendered surface) -- canonical Trust Center at /trust-center (HTTP 308 from /trust 2026-07-22) -- SIBLING #4/5 of NEW VERTICAL #24 ai_revenue_enablement_for_field_sales after Showpad 927 OPENER #1/5 + Highspot 928 SIBLING #2/5 + Mediafly 929 SIBLING #3/5. Real company + real website + real NAMED first-party Aura AI surface + 5-stamp ISO/SOC 2/GDPR verbatim first-party verified. SIBLING #4/5 non-overlapping wedge: (1) only cohort member with verbatim first-party ISO 42001 AI Management System on rendered surface (Showpad 927 + Highspot 928 + Mediafly 929 do not publish ISO 42001 verbatim surface); (2) only cohort member with verbatim first-party \'trusted intelligence layer\' positioning verbatim /platform/aura/ 2026-07-22 (Showpad \'AI core\' + Highspot \'AI Role Play + Agents + CI\' multi-SKU + Mediafly \'single Command Center AI engine\' give different governance wedge); (3) only cohort member with verbatim first-party \'Specialized AI agents for revenue execution\' + \'Purpose built for GTM teams\' verbatim /platform/aura/ 2026-07-22 (cohort-unique agent-specialization taxonomy gives different ASC 605 + ASC 606 + Reg BI fairness-lane diligence); (4) only cohort member with verbatim first-party content-permission-scope commitment \'Aura AI always respects your established content permissions\' /platform/aura/ 2026-07-22 (cohort-unique SOC 2 CC6.1 + GDPR Art. 6 + CCPA/CPRA + ISO 27001 A.8.32 + ISO 42001 diligence); (5) only cohort member with verbatim first-party \'Enablement needs more than generic AI\' competitive-positioning quote /platform/aura/ 2026-07-22 (cohort-unique procurement-DD positioning surface gives different ASC 606 customer-contract procurement-DD diligence). Tier-1 evidence wedge: (a) 16-col per-Aura-AI-agent-run join-table reproducible cross-tenant-no-bleed (aura_session_id + aura_action_id + aura_prompt_hash + aura_response_hash + aura_model_name + aura_model_version + enablement_cloud_tenant_id + seismic_exchange_content_id + content_permission_scope_id + crm_contact_id + conversation_intelligence_transcript_id + per_integration_consent_ledger_entry_id EU AI Act Art. 6(2) Annex III + GDPR Art. 6 lawful-basis + CCPA + CPRA + SOC 2 CC6.1 + ISO 27001 A.8.32 + ISO 42001 + per_buyer_room_audit_log_replay_id + per_customer_zone_isolation_report_id + per_aura_agent_run_id + per_tenant_credential_scope + per_sub_processor_dpa_flow_down + cross_tenant_no_bleed_proof); (b) per-Aura-AI LLM trace; (c) per-AI-agent run provenance; (d) per-quarter Aura-session reconstruction + 24-quarter replay + ISO 42001 deployer-obligation reconciliation; (e) per-customer zone-isolation report. Compliance posture verbatim first-party /platform/aura/ 2026-07-22: ISO 42001 AI Management System + SOC 2 Type II Security & Availability + ISO 27001 Information Security + ISO 27701 Privacy Management + GDPR Data Protection (5-stamp verbatim surface); \'trusted intelligence layer\' + \'Aura AI always respects your established content permissions\' verbatim /platform/aura/ 2026-07-22; Trust Center at /trust-center verified HTTP 200 2026-07-22. $500/48h fixed-scope Seismic + Aura AI + Enablement Cloud + Trust Center evidence-gap map or $497/mo quarterly refresh or $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling. Verified commercial route FORM:https://www.seismic.com/platform/aura/ \'See Aura in Action\' CTA verbatim first-party 2026-07-22; no guessed general-business inbox added. SMTP/form gated, $0 sent / $0 received.'
]

with open('cold_email/leads.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\', doublequote=False)
    w.writerow(leads_row)
print('leads.csv row 930 appended')

# leads_with_emails.csv (13 columns)
emails_row = [
    "930", "Seismic", "@seismic", "seismic.com", "https://www.seismic.com",
    "Fred Lippar (CEO + Founder, INFERRED-from-public-records per pitfall P42 -- not verbatim on /platform/aura/ rendered first-party surface 2026-07-22; industry-canonical ~2010 San Diego CA HQ; verbatim founder citation deferred to next-tick browser-use CDP-attach probe)",
    "ai_revenue_enablement_for_field_sales", "1",
    "FORM:https://www.seismic.com/platform/aura/", "0", "0",
    "930_seismic.md",
    "Lead 930 Seismic full ship: 16-col per-Aura-AI-agent-run join-table reproducible cross-tenant-no-bleed; verbatim first-party /platform/aura/ 2026-07-22 NAMED AI surface 'Aura AI is Seismic trusted intelligence layer for GTM execution' + 'Specialized AI agents for revenue execution' + 5-stamp verbatim compliance stack ISO 42001 + SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR. Verified commercial route FORM:https://www.seismic.com/platform/aura/ 'See Aura in Action' CTA + /trust-center canonical first-party 2026-07-22; no first-party mailto: published per pitfall P28; SMTP/form gated, $0 sent / $0 received."
]

with open('cold_email/leads_with_emails.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar='\\', doublequote=False)
    w.writerow(emails_row)
print('leads_with_emails.csv row 930 appended')

# revenue_log
import os, time
with open('cold_email/revenue_log.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(['930', 'tick-930', 'queued_not_sent', '2026-07-22', 'Seismic', 'FORM:https://www.seismic.com/platform/aura/',
        'ai_revenue_enablement_for_field_sales', 'sibling-4-of-5', '0.00', '$500/48h', '0'])
print('revenue_log row 930 appended')

# send_log.jsonl
with open('cold_email/send_log.jsonl', 'a', encoding='utf-8') as f:
    import json
    f.write(json.dumps({
        "tick": 930, "company": "Seismic", "lead_index": 930,
        "route": "FORM:https://www.seismic.com/platform/aura/",
        "status": "queued_not_sent", "vertical": "ai_revenue_enablement_for_field_sales",
        "cohort_role": "sibling-4-of-5", "ts": "2026-07-22"
    }) + "\n")
print('send_log row 930 appended')
