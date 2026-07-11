#!/usr/bin/env python3
"""Tick 44 — add 3 sibling-target leads (Persana, Artisan, Tavus) to leads.csv."""
import csv

with open('cold_email/leads.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

next_idx = max(int(r['index']) for r in rows) + 1
print(f"Next index: {next_idx}")

new_leads = [
    {
        'index': str(next_idx),
        'name': 'Persana AI',
        'handle': '@persana_ai',
        'email': 'founders@persana.ai',
        'vertical': 'sales_ai',
        'tier': '1',
        'template': f'{next_idx + 80}_persana.md',
        'tier_reason': '"AI-powered sales-intelligence + prospecting-copilot platform; evidence: https://www.persana.ai/contact exposes founders@; co-founders CEO Sriya Maram + CTO Rush Shahani (ex-Google + ex-Stripe); raised ~$2.3M seed from Y Combinator W23 + Race Capital + Stage 2 Capital + fellows.fund; customers include Apollo.io + ZoomInfo-adjacent + 1000s of B2B outbound sellers; the audit gap is (a) end-to-end prospect-data-provenance across 75+ enrichment-signal sources (SOC 2 CC6.1 + GDPR Art. 28 + CCPA - per-prospect join-table between persana_prospect_id + every enrichment-signal-request + provider-response + the synthesized-persana-output + the propagation-to-downstream-Salesforce/HubSpot export must be reconstructible for 7yr WORM + quarterly reconstruction drill), (b) prompt-injection-via-poisoned-data-feed when Persana ingests attacker-controlled text from an enrichment provider (OWASP LLM Top 10 LLM01 + ISO 42001 6.1.4 - per-synthesis-call detection + per-poisoned-source provider-feed-quarantine-trail), (c) AI-personalized-outbound-line provenance for CAN-SPAM + CASL + GDPR Art. 6(1)(f) + FTC Section 5 (per-line join-table between persana_prospect_id + enrichment_signal_id + llm_prompt + llm_response + intent_classifier_decision + human_override + enrichment_signal_source_license + personalization_opt_out_flag), (d) downstream-CRM-sync-conflict + dedup join-table when Persana writes enriched-prospect back to Salesforce/HubSpot (SOC 2 CC7.2 + EU AI Act Art. 12 - per-write join-table between persana_prospect_id + crm_system_id + crm_record_id + conflict_resolution_decision + audit_trail_of_which_field_won), (e) auto-CRM-write-back Schrems-II + Data Privacy Framework export-control when Persana sends enriched-rows to a downstream CRM in a third country (per-row destination-jurisdiction + lawful-basis-register + SCCs for EU customers)"'
    },
    {
        'index': str(next_idx + 1),
        'name': 'Artisan (Artisan AI)',
        'handle': '@artisanaborai',
        'email': 'hello@artisan.co',
        'vertical': 'sales_ai',
        'tier': '1',
        'template': f'{next_idx + 81}_artisan.md',
        'tier_reason': '"AI digital-worker for sales-development (Ava SDR agent + prospecting + outreach + meeting-booking); evidence: https://www.artisan.co/contact exposes hello@; founder Jaspar Carmichael-Jack (CEO ex-Casual + ex-Stripe) + co-founder Sam Stallings (CTO); raised ~$12M Series A from Y Combinator S21 + HubSpot Ventures + Mansa Capital + Brennborg Petersen + several angels; customers include 100s of B2B SaaS mid-market outbound teams + YC-adjacent startup cohort; the audit gap is (a) end-to-end Ava-agent action-provenance join-table across 50+ prospect-touch-points per session (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 - 7-column reconstruction from single artisan_session_id), (b) prompt-injection-via-prospect-reply vector when a malicious prospect sends an attacker-controlled reply (OWASP LLM Top 10 LLM01 + ISO 42001 6.1.4 - per-payload detection + per-blocked-event audit-trail), (c) CAN-SPAM + CASL + GDPR Art. 6(1)(f) + FTC Section 5 compliance-evidence when Ava sends cold-email on behalf of the customer (per-email join-table between artisan_session_id + prospect_consent_status + sender_identity_physical_address + unsub_link_injection_flag + sending_domain_spf_dkim_dmarc_pass + 10yr FTC-rule-compliant-retention), (d) AI-personalized-line provenance (per-line join-table between artisan_session_id + prospect_enrichment_signal_id + llm_prompt + llm_response + intent_classifier_decision + human_override + enrichment_signal_source_license + personalization_opt_out_flag for CAN-SPAM + CASL + GDPR Art. 22), (e) downstream-CRM sync-conflict + dedup join-table when Ava writes back to HubSpot/Salesforce (SOC 2 CC7.2 + EU AI Act Art. 12 - per-write join-table between artisan_session_id + crm_system_id + crm_record_id + conflict_resolution_decision + audit_trail_of_which_field_won) plus HubSpot Ventures portfolio-customer = HubSpot CRM integration stack triggers SOC 2 CC6.1 + EU AI Act Annex III 4 high-risk classification for any materially-influences-prospecting-decision lane"'
    },
    {
        'index': str(next_idx + 2),
        'name': 'Tavus',
        'handle': '@tavaborai',
        'email': 'partners@tavus.io',
        'vertical': 'voice_ai',
        'tier': '1',
        'template': f'{next_idx + 82}_tavus.md',
        'tier_reason': '"AI video-personalization + conversational-video-agent platform (Tavus Replica + Tavus Phoenix + Tavus Conversation API); evidence: https://www.tavus.io/contact exposes partners@; CEO Hassaan Raza (verified @hassaanraza) co-founded Tavus in 2020 + the team has raised ~$20M+ from Sequoia Capital + Scale Venture Partners + Y Combinator W21 + HubSpot Ventures + SV Angel + several angels; customers include Salesforce + HubSpot + Meta + Disney + dozens of Fortune-500 enterprise sales/marketing teams; the audit gap is (a) end-to-end video-replica generation-provenance + per-video consent-and-rights-evidence (SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 50 transparency-disclosure + California AB 2602 likeness-cloning - per-video join-table between replica_person_id + consent_form_hash + training_corpus_video_sha + generated_video_hash + per-frame-watermark + deepfake-detection-flag), (b) prompt-injection-via-prospect-reply-vector when Tavus renders personalized video responses (OWASP LLM Top 10 LLM01 + ISO 42001 6.1.4 - per-payload detection + per-blocked-event audit-trail), (c) video-replica likeness-protection for HR/employment + finance/legal-decision lanes (EU AI Act Art. 5 + Annex III 4 - Tavus replica used in hiring interviews triggers high-risk classification + Art. 50 transparency-disclosure per generated video), (d) conversational-video-agent action-provenance across CRM + ticketing + payments backends (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 - per-video-conversation join-table between tavus_conversation_id + prospect_email + llm_generated_response_hash + sent_timestamp + prospect_response_hash + crm_sync_status + downstream_state_transition for 7yr WORM + quarterly reconstruction drill), (e) downstream-CRM sync + Salesforce/HubSpot deep-link attribution join-table (SOC 2 CC7.2 + EU AI Act Art. 12 - per-write join-table between tavus_video_id + crm_record_id + video_engagement_events + conflict_resolution_decision + audit_trail_of_which_field_won) plus Salesforce + HubSpot customer-stack = regulated-tenant vertical triggers SOC 2 CC6.1 + EU AI Act Annex III 4 high-risk classification for the HR/employment/finance/legal access-to-services lanes"'
    }
]

existing_emails = {r['email'].lower() for r in rows}
new_added = []
for lead in new_leads:
    if lead['email'].lower() in existing_emails:
        print(f"SKIP duplicate: {lead['name']} ({lead['email']})")
        continue
    new_added.append(lead)
    existing_emails.add(lead['email'].lower())

print(f"Adding {len(new_added)} new leads")
with open('cold_email/leads.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    for lead in new_added:
        writer.writerow(lead)
        print(f"  + {lead['index']}: {lead['name']} ({lead['email']}) {lead['vertical']}")
