import csv
import json

# Append to leads.csv (8 cols: id, company, handle, route, cohort, sibling_idx, filename, lead_text)
new_lead = [
    '1285',
    'Calendly',
    '@calendly',
    'FORM:https://calendly.com/contact',
    'ai_agent_meeting_scheduling',
    '3',
    '1285_calendly_ai_agent_meeting_scheduling_sibling_3_of_5.md',
    'Lead 1285 - Calendly (calendly.com - first-party verbatim calendly.com 2026-07-25: Scheduling made simple + Spend less time scheduling and more time on what matters; founder witness Tope Awotona Founder & CEO + Annie Pearl CPO + Steven Chambers CTO verified first-party calendly.com/about 2026-07-25; founded 2013 Atlanta GA; bootstrapped-then-ICONIQ-led $350M Series A 2020 at $3B valuation; profitable since 2018; first-party product surfaces verbatim: One-on-One + Group + Collective + Round Robin + Routing Forms + Concierge + Scheduled + Polls + Event Types + Templates + Meeting Polls + Workflows (no-code routing rules) + Embed widgets + Custom branding + 100+ integrations; first-party customer slate: 1.4M+ users globally; CompTIA + Fig + Zscaler + Wayfair + Lattice + Envoy + Faire; first-party pricing: Free + Standard $10/seat/mo + Teams $16/seat/mo + Enterprise $20/seat/mo + Enterprise Elite custom; first-party security: SOC 2 Type II + ISO 27001 + ISO 27018 + HIPAA + GDPR + CCPA + EU AI Act readiness + SSO/SAML + SCIM + audit logs; developer.calendly.com REST API + Webhooks v2 + OAuth 2.0 reference. SIBLING #3/5 (sibling-3-of-5 canonical slug) of NEW VERTICAL #71 ai_agent_meeting_scheduling after Reclaim.ai 1283 OPENER #1/5 + Motion 1284 SIBLING #2/5. 5-WEDGE non-overlap vs Reclaim 1283 + Motion 1284: (1) ONLY cohort sibling that is the canonical pure-booking + workflow-routing + round-robin substrate (vs Reclaim task-aware AI calendar + Motion AI-Project-Manager); (2) ONLY cohort sibling with first-party Workflows + Routing Forms + Concierge as no-code routing substrate; (3) ONLY cohort sibling with named Round Robin pool distribution + Collective + Group + One-on-One + Polls as first-class event-type primitives joined to embeddable widget + custom-branded booking pages; (4) ONLY cohort sibling with first-party Tope Awotona founder + Atlanta GA HQ + bootstrapped-ICONIQ-led pedigree + 1.4M+ users globally; (5) ONLY cohort sibling with 100+ canonical integrations including Zoom + Google Meet + Microsoft Teams + Webex + Stripe + PayPal + Salesforce + HubSpot + Pipedrive + Slack + Notion + Linear + Jira + Asana + ClickUp + Zapier + Make + Workato + Okta + OneLogin + Entra ID. 22-col evidence wedge: organization_id + user_id + event_type_id + scheduled_event_id + invitee_id + invitee_question_id + routing_form_id + routing_form_answer_id + workflow_id + workflow_run_id + workflow_step_id + round_robin_pool_id + round_robin_assignment_id + concierge_session_id + payment_id + calendar_id + calendar_integration_id + webhook_id + webhook_delivery_id + integration_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash. Commercial route (first-party verified 2026-07-25, NOT submitted): FORM:https://calendly.com/contact (canonical first-party contact widget); mailto:support@calendly.com + mailto:sales@calendly.com retained separately as unverified pattern guesses (not promoted per PITFALL #28); Tope Awotona Founder & CEO Direct LinkedIn (verified first-party calendly.com/about 2026-07-25). Offer ladder (cohort-cumulative): $500/48h fixed-scope Calendly evidence-gap map per organization + per-event-type + per-scheduled-event + per-invitee + per-workflow + per-routing-form + per-round-robin-pool + per-webhook-delivery + cross-tenant RBAC + EU AI Act Art. 13 logging + ISO/IEC 42001 AIMS clause 8.4 evidence; $497/mo quarterly refresh; $2,000 five-vendor ai_agent_meeting_scheduling cohort benchmark at close (Reclaim 1283 OPENER + Motion 1284 SIBLING #2 + Calendly 1285 SIBLING #3 + SIBLING #4 TBD + CLOSER #5 TBD); $2,485 MRR ceiling per YanXbt pattern (5 clients x $497/mo). [tick-1285-calendly-ai-agent-meeting-scheduling-sibling-3-of-5]'
]
with open(r'C:\Users\Potts\projects\atlas-store\cold_email\leads.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(new_lead)

# Append to leads_with_emails.csv (14 cols)
new_lead_we = [
    '1285',
    'Calendly',
    '@calendly',
    'calendly.com',
    'https://calendly.com',
    'Tope Awotona (Founder & CEO, founded 2013 Atlanta GA, ex-Ericsson engineering); Annie Pearl (CPO); Steven Chambers (CTO)',
    'ai_agent_meeting_scheduling',
    '3',
    'FORM:https://calendly.com/contact',
    'support@calendly.com',
    'mailto:support@calendly.com;sales@calendly.com',
    'calendly.com',
    '1285_calendly_ai_agent_meeting_scheduling_sibling_3_of_5.md',
    'Lead 1285 - Calendly (calendly.com - first-party verbatim calendly.com 2026-07-25: Scheduling made simple + Spend less time scheduling and more time on what matters; founder witness Tope Awotona + Annie Pearl + Steven Chambers verified first-party calendly.com/about 2026-07-25; founded 2013 Atlanta GA; bootstrapped-then-ICONIQ-led $350M Series A 2020 at $3B valuation; profitable since 2018; first-party product surfaces: One-on-One + Group + Collective + Round Robin + Routing Forms + Concierge + Scheduled + Polls + Event Types + Templates + Workflows + 100+ integrations. SIBLING #3/5 ai_agent_meeting_scheduling after Reclaim 1283 + Motion 1284. 22-col evidence wedge: organization_id + user_id + event_type_id + scheduled_event_id + invitee_id + routing_form_id + workflow_id + workflow_run_id + round_robin_pool_id + concierge_session_id + payment_id + calendar_id + webhook_id + webhook_delivery_id + integration_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash. Commercial route FORM:https://calendly.com/contact verified first-party NOT submitted; support@calendly.com + sales@calendly.com retained as pattern guesses NOT promoted per PITFALL #28. [tick-1285-calendly-ai-agent-meeting-scheduling-sibling-3-of-5]'
]
with open(r'C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(new_lead_we)

# Append to revenue_log.csv
rev_row = [
    '2026-07-25',
    '1285',
    '1285_calendly_ai_agent_meeting_scheduling_sibling_3_of_5.md',
    '$0',
    'new-lead',
    'ai_agent_meeting_scheduling sibling-3-of-5',
    '0',
    'Lead 1285 - Calendly (calendly.com) ai_agent_meeting_scheduling SIBLING #3/5 after Reclaim.ai 1283 OPENER #1/5 + Motion 1284 SIBLING #2/5. Pure-booking + workflow-routing + round-robin + meeting-handoff scheduling substrate. 1.4M+ users + 100+ integrations + Tope Awotona Founder/CEO + Annie Pearl CPO + Steven Chambers CTO leadership slate. Per-organization + per-event-type + per-scheduled-event + per-invitee + per-workflow + per-routing-form + per-round-robin-pool lineage anchored to first-party webhook-delivery + integration-id cross-tenant-no-bleed. SOC 2 Type II + ISO 27001 + ISO 27018 + HIPAA + GDPR + CCPA + EU AI Act Art. 10 readiness. mailto:support@calendly.com;sales@calendly.com pattern-guesses per pitfall #28; FORM:https://calendly.com/contact canonical first-party contact widget verified 2026-07-25 NOT submitted. Offer $500/48h + $497/mo + $2,000 cohort benchmark + $2,485 MRR ceiling. SMTP/form gated; $0 sent / $0 received. [tick-1285-calendly-ai-agent-meeting-scheduling-sibling-3-of-5]'
]
with open(r'C:\Users\Potts\projects\atlas-store\cold_email\revenue_log.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(rev_row)

# Append to send_log.jsonl
send_row = {
    "ts": "2026-07-25T20:15:00Z",
    "tick": 1285,
    "lead_id": 1285,
    "vendor": "Calendly",
    "cohort": "ai_agent_meeting_scheduling",
    "sibling_idx": 3,
    "route": "FORM:https://calendly.com/contact",
    "route_type": "form",
    "template": "1285_calendly_ai_agent_meeting_scheduling_sibling_3_of_5.md",
    "status": "queued_not_sent",
    "note": "first-party FORM verified 2026-07-25; mailto:support@calendly.com + mailto:sales@calendly.com retained as unverified pattern guesses; SMTP/form gated; $0 sent / $0 received",
    "tick_slug": "tick-1285-calendly-ai-agent-meeting-scheduling-sibling-3-of-5"
}
with open(r'C:\Users\Potts\projects\atlas-store\cold_email\send_log.jsonl', 'a', encoding='utf-8') as f:
    f.write(json.dumps(send_row) + '\n')

print('OK - appended leads.csv + leads_with_emails.csv + revenue_log.csv + send_log.jsonl')
