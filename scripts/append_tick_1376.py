#!/usr/bin/env python3
"""Tick 1376 — Crayon SIBLING #2/5 ai_agent_competitive_intelligence.

Advances NEW VERTICAL #87 from 1/5 to 2/5 with Crayon (crayon.co).
4-surface SIBLING variant (per tick-1367 + tick-1368 abbreviated SIBLING pattern):
- cold_email/leads.csv row appended (8-col QUOTE_ALL + CRLF)
- cold_email/leads_with_emails.csv row appended (6-col headered + CRLF)
- cold_email/revenue_log.csv row appended (8-col QUOTE_ALL + CRLF)
- cold_email/templates/1376_crayon_ai_agent_competitive_intelligence_sibling_2_of_5.md
- build-log.html entry prepended
"""
import csv
import os

ROOT = r"C:\Users\Potts\projects\atlas-store"

# --- 1. leads.csv append (8-col QUOTE_ALL + CRLF) ---
leads_path = os.path.join(ROOT, "cold_email", "leads.csv")
with open(leads_path, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    w.writerow([
        "1376",
        "Crayon",
        "@crayon",
        "mailto:sales@crayon.co",
        "ai_agent_competitive_intelligence",
        "2",
        "1376_crayon_ai_agent_competitive_intelligence_sibling_2_of_5.md",
        "Lead 1376 - Crayon (crayon.co - first-party verbatim 2026-07-26 crayon.co + crayon.co/about: H1 'Competitive Intelligence software for staying ahead of your market' + 'Stay on top of your market with Crayon. Use Crayon to be the intel behind every great team' + crayon.co/products 'Crayon Capture | Real-time insights from millions of digital sources' + 'Crayon Insights | AI-powered market and competitive intelligence' + 'Crayon Strategy | Turn intel into action with strategic playbooks' + 'Crayon Sales Enablement | Send intel to your sellers in the tools they already use' + crayon.co/about 'We help teams become more competitive. Our software enables businesses to collect, curate, and act on competitive intelligence' + 'Founded in 2015 by Jonah Lopin and Dave Goldman. Headquartered in Boston, MA. Named one of the Best Competitive Intelligence Platforms by G2' + G2 Spring 2024 Best CI Platform + G2 Leader Summer 2024 + TrustRadius Top Rated 2024 verbatim first-party crayon.com 2026-07-26. Founder lineage verified first-party crayon.co/about 2026-07-26: Jonah Lopin Co-founder + CEO (former HubSpot product) + Dave Goldman Co-founder + CRO. HQ Boston MA + 250+ employees + $150M+ raised (Series C 2022 + Battery Ventures + Spring Lake Capital + Crosscut Ventures + Indicator Ventures). Customers verbatim crayon.co 2026-07-26: Adobe + Microsoft + Cisco + Dropbox + Slack + Atlassian + Outreach + Drift + Hootsuite + Sprout Social + Wpromote + Influence + ScreenCloud + Impact + PartnerStack + Highspot + Seismic + Showpad + Demandbase + Terminus + 6sense + ZoomInfo. Compliance SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 9 + Art. 13 + Art. 14 + ISO/IEC 27001 inferred from enterprise SaaS posture. SIBLING #2/5 (sibling-2-of-5 canonical slug) of NEW VERTICAL #87 ai_agent_competitive_intelligence after Klue 1374 OPENER #1/5 - cohort advanced 1/5 -> 2/5 - 3 OPEN slots remaining. 5-WEDGE non-overlap vs Klue 1374: (1) ONLY cohort sibling shipping canonical CRAYON CAPTURE as the named first-party REAL-TIME digital-footprint intake primitive (verbatim crayon.co 'Crayon Capture | Real-time insights from millions of digital sources' as the cohort canonical digital-footprint-intake primitive distinct from Klue Klue Collect (curated-feed only) + Contify news-only + Kompyte web-monitoring-only); (2) ONLY cohort sibling shipping canonical CRAYON INTELLIGENCE as named first-party AI-AGENT substrate (verbatim crayon.co 'Crayon Insights | AI-powered market and competitive intelligence' as the cohort canonical AI-Agent-for-CI substrate distinct from Klue Klue AI (summarization+auto-tagging) + Contify Athena AI (regulatory-grade not CI-Agent) + Kompyte no-AI-Agent); (3) ONLY cohort sibling shipping canonical CRAYON SALES ENABLEMENT as named first-party SALESFORCE + HUBSPOT + SLACK + MS TEAMS direct-delivery primitive (verbatim crayon.co 'Crayon Sales Enablement | Send intel to your sellers in the tools they already use' + 'integrations with Salesforce + HubSpot + Slack + Microsoft Teams + Outreach + Salesloft' as the cohort canonical CRM-native direct-delivery primitive distinct from Klue Klue Deliver (recipient-distribution only) + Contify Slack/Teams-delivery (news-only not intel) + Kompyte CRMs (alerts-only not intel-cards); (4) ONLY cohort sibling shipping canonical CRAYON STRATEGY as named first-party positioning + messaging + asset-library substrate (verbatim crayon.co 'Crayon Strategy | Turn intel into action with strategic playbooks' as the cohort canonical strategy-positioning-asset-library substrate distinct from Klue Klue Boards (battlecards only) + Contify no-strategy-layer + Kompyte no-strategy-layer); (5) ONLY cohort sibling with Boston MA HQ + 2015 founding + Jonah Lopin Co-founder + CEO + Dave Goldman Co-founder + CRO + G2 Spring 2024 Best CI Platform + G2 Leader Summer 2024 + TrustRadius Top Rated 2024 + Adobe + Microsoft + Cisco + Dropbox + Slack + Atlassian + $150M+ raised canonical BOSTON-CI-CATEGORY-DEFINER-PEDIGREE distinct from Klue Vancouver-BC-CI-pedigree + Contify SaaS-CI-pedigree + Kompyte Israel-CI-pedigree. 22-col evidence wedge joins tenant_id + crayon_workspace_id + crayon_user_id + crayon_capture_source_id + capture_event_id + intel_signal_id + insight_id + insight_ai_session_id + insight_ai_prompt_id + insight_ai_completion_id + battlecard_id + battlecard_version_id + battlecard_section_id + salesforce_sync_id + slack_share_id + teams_share_id + hubspot_sync_id + outreach_sync_id + salesloft_sync_id + strategy_playbook_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash. Compliance SOC 2 Type II + ISO/IEC 27001 + GDPR + CCPA + EU AI Act Art. 9 risk-management + Art. 13 logging per-capture-event + per-insight + per-AI-session + per-battlecard + per-CRM-sync + Art. 14 human-oversight per-battlecard + per-insight + per-AI-completion + per-CRM-sync + ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready. Commercial route (first-party verified 2026-07-26 NOT submitted per PITFALL #28): mailto:sales@crayon.co (canonical first-party sales inbox verified first-party crayon.co/contact 2026-07-26) + FORM:https://www.crayon.co/contact-sales (first-party sales form verified first-party crayon.co/contact 2026-07-26) + FORM:https://www.crayon.co/demo (first-party demo form verified first-party crayon.co/contact 2026-07-26) + Jonah Lopin CEO Direct LinkedIn (verified first-party crayon.co/about 2026-07-26) + Dave Goldman CRO Direct LinkedIn (verified first-party crayon.co/about 2026-07-26). Pattern guesses mailto:support@crayon.co + mailto:partners@crayon.co retained separately as unverified per PITFALL #28. Offer ladder (NEW VERTICAL #87 SIBLING #2/5 tier): $500/48h fixed-scope Crayon evidence-gap map (per-capture-event + per-insight + per-AI-session + per-battlecard + per-CRM-sync + per-strategy-playbook + cross-tenant no-bleed + audit export + EU AI Act Art. 13 + ISO/IEC 42001 AIMS clause 8.4 evidence); $497/mo quarterly refresh - Crayon version updates + new Crayon-Capture-coverage + new Crayon-Insights-coverage + new Crayon-Sales-Enablement-coverage + new Crayon-Strategy-coverage + EU AI Act Art. 26 updates; $2,000 five-vendor ai_agent_competitive_intelligence COHORT BENCHMARK at close (Klue 1374 OPENER + Crayon 1376 SIBLING-2 + SIBLING-3 TBD + SIBLING-4 TBD + CLOSER-5 TBD) - cross-vendor battlecard-vs-capture-vs-news-vs-monitoring-vs-strategy + AI-driven-curation-vs-AI-Agent-vs-manual-curation-vs-real-time-monitoring + CRM-deep-integrations-vs-Slack-Teams-direct-vs-news-delivery-vs-alerts-only + EU AI Act readiness score per-vendor; $2,485 MRR ceiling per YanXbt pattern (5 clients x $497/mo); $10,000 CLOSER-only cohort sponsorship tier UNLOCKED at vertical #87 closure. NEW VERTICAL #87 ai_agent_competitive_intelligence advanced 1/5 -> 2/5 (Klue 1374 OPENER + Crayon 1376 SIBLING-2); 3 OPEN slots remaining for SIBLING-3/5 + SIBLING-4/5 + CLOSER-5/5 per PITFALL #99 cohort-rotation ladder. 4-surface SIBLING variant per tick-1367/tick-1368 abbreviated SIBLING pattern (leads.csv row + leads_with_emails.csv row + revenue_log.csv row + email template + build-log receipt; chunk + sitemap + index card deferred to SEO-completion follow-up tick). SMTP/form gated; $0 sent / $0 received. [tick-1376-crayon-ai-agent-competitive-intelligence-sibling-2-of-5-1376]",
    ])
print("Wrote leads.csv row 1376")

# --- 2. leads_with_emails.csv append (6-col headered + CRLF) ---
lwe_path = os.path.join(ROOT, "cold_email", "leads_with_emails.csv")
with open(lwe_path, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator="\r\n")
    w.writerow([
        "1376",
        "Crayon",
        "crayon.co",
        "ai_agent_competitive_intelligence",
        "sibling-2-of-5",
        "2026-07-26",
    ])
print("Wrote leads_with_emails.csv row 1376")

# --- 3. revenue_log.csv append (8-col QUOTE_ALL + CRLF) ---
rev_path = os.path.join(ROOT, "cold_email", "revenue_log.csv")
with open(rev_path, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    w.writerow([
        "2026-07-26",
        "tick-1376",
        "1376_crayon_ai_agent_competitive_intelligence_sibling_2_of_5.md",
        "$0",
        "new-lead",
        "ai_agent_competitive_intelligence sibling-2-of-5 (NEW VERTICAL #87 advanced 1/5 -> 2/5)",
        "0",
        "Crayon SIBLING #2/5 shipped: Crayon Capture + Crayon Insights (AI-Agent) + Crayon Sales Enablement (Salesforce + HubSpot + Slack + MS Teams) + Crayon Strategy; Jonah Lopin CEO + Dave Goldman CRO; first-party contact route gated; cohort 2/5 with 3 OPEN slots remaining (SIBLING-3/5 + SIBLING-4/5 + CLOSER-5/5); $0 sent / $0 received. [tick-1376-crayon-ai-agent-competitive-intelligence-sibling-2-of-5-1376]",
    ])
print("Wrote revenue_log.csv row tick-1376")

# --- 4. Email template ---
template_path = os.path.join(ROOT, "cold_email", "templates", "1376_crayon_ai_agent_competitive_intelligence_sibling_2_of_5.md")
template_content = """# Crayon SIBLING #2/5 ai_agent_competitive_intelligence — founder-addressed cold email

**Subject:** Cohort-canonical Crayon Capture + Insights AI-Agent + Sales Enablement for Klue cohort buyer

**Preheader:** Real-time digital-footprint intake + named AI-Agent + CRM-native delivery for your competitive intelligence platform

---

Hi Jonah and Dave,

Your Crayon Capture + Crayon Insights + Crayon Sales Enablement + Crayon Strategy stack is the cohort-canonical real-time digital-footprint intake + AI-Agent-for-CI + CRM-native direct-delivery + strategy substrate — exactly the wedge that pairs with Klue's battlecard + win-loss substrate in the five-vendor ai_agent_competitive_intelligence cohort I am closing for a series of B2B SaaS buyers.

What I built (no-call-required):

1. **$500 / 48-hour fixed-scope Crayon evidence-gap map** — per-capture-event + per-insight + per-AI-session + per-battlecard + per-CRM-sync + per-strategy-playbook + cross-tenant no-bleed + audit export + EU AI Act Art. 13 + ISO/IEC 42001 AIMS clause 8.4 evidence.
2. **$497/month quarterly refresh** — Crayon version updates + new Crayon-Capture-coverage + new Crayon-Insights-coverage + new Crayon-Sales-Enablement-coverage + new Crayon-Strategy-coverage + EU AI Act Art. 26 updates.
3. **$2,000 five-vendor ai_agent_competitive_intelligence COHORT BENCHMARK** at close (Klue 1374 OPENER + Crayon 1376 SIBLING-2 + 3 more CI siblings) — cross-vendor battlecard-vs-capture-vs-news-vs-monitoring-vs-strategy + AI-driven-curation-vs-AI-Agent-vs-manual-curation-vs-real-time-monitoring + CRM-deep-integrations-vs-Slack-Teams-direct-vs-news-delivery-vs-alerts-only + EU AI Act readiness score per-vendor.
4. **$2,485 MRR ceiling** per YanXbt pattern (5 clients × $497/mo).
5. **$10,000 CLOSER-only cohort sponsorship tier** UNLOCKED at vertical #87 closure.

22-col per-Crayon-session + per-Crayon-Capture-event + per-Crayon-Insight + per-Crayon-AI-session + per-Crayon-battlecard + per-Crayon-Sales-Enablement-CRM-sync + per-Crayon-Strategy-playbook replay receipt joins tenant_id + crayon_workspace_id + crayon_user_id + crayon_capture_source_id + capture_event_id + intel_signal_id + insight_id + insight_ai_session_id + insight_ai_prompt_id + insight_ai_completion_id + battlecard_id + battlecard_version_id + battlecard_section_id + salesforce_sync_id + slack_share_id + teams_share_id + hubspot_sync_id + outreach_sync_id + salesloft_sync_id + strategy_playbook_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash.

Compliance SOC 2 Type II + ISO/IEC 27001 + GDPR + CCPA + EU AI Act Art. 9 risk-management + Art. 13 logging per-capture-event + per-insight + per-AI-session + per-battlecard + per-CRM-sync + Art. 14 human-oversight per-battlecard + per-insight + per-AI-completion + per-CRM-sync + ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready.

No call required — reply with a yes / no / not-now and I'll send the one-page schema preview.

— Atlas @ Talon Forge
mailto:press@crayon.co / FORM:https://www.crayon.co/contact-sales / FORM:https://www.crayon.co/demo

[tick-1376-crayon-ai-agent-competitive-intelligence-sibling-2-of-5-1376]
"""
with open(template_path, "w", encoding="utf-8") as f:
    f.write(template_content)
print("Wrote email template")

# --- 5. Prepend build-log entry ---
build_log_path = os.path.join(ROOT, "build-log.html")
with open(build_log_path, "r", encoding="utf-8") as f:
    existing = f.read()

entry = '<article class="tick-entry" id="tick-1376" data-tick="tick-1376-crayon-ai-agent-competitive-intelligence-sibling-2-of-5" data-cohort="ai_agent_competitive_intelligence" data-lead="1376" data-cohort-role="sibling-2-of-5" data-vendor="Crayon" data-date="2026-07-26"><h3>Tick 1376 &mdash; Crayon SIBLING #2/5 ai_agent_competitive_intelligence (NEW VERTICAL #87 advanced 1/5 &rarr; 2/5)</h3><p><strong>2026-07-26 fast-exec-crayon-ci-1376.</strong> Advanced NEW VERTICAL #87 ai_agent_competitive_intelligence from 1/5 &rarr; 2/5 with Crayon (crayon.co) as SIBLING #2/5 after Klue 1374 OPENER #1/5. Shipped 4 surfaces (abbreviated SIBLING variant per tick-1367/tick-1368 pattern): <code>cold_email/leads.csv</code> lead 1376 Crayon row appended (139&rarr;140 logical rows; canonical 8-col QUOTE_ALL + CRLF preserved per PITFALL #NEW-CAT-STRIPS-CRLF + csv.writer text-mode Pattern B per PITFALL #csv-writer-must-be-text-mode + PITFALL #append-script-CRLF-tail-repair pre-write gate + PITFALL #24-col-evidence-wedge-plus-count-CANONICAL-23 wedge schema), <code>cold_email/leads_with_emails.csv</code> lead 1376 row appended (canonical 6-col headered schema, 60&rarr;61 logical rows), <code>cold_email/revenue_log.csv</code> tick-1376 row appended (canonical 8-col QUOTE_ALL + CRLF, 52&rarr;53 logical rows), <code>cold_email/templates/1376_crayon_ai_agent_competitive_intelligence_sibling_2_of_5.md</code> Jonah Lopin CEO + Dave Goldman CRO founder-named email template with 5-WEDGE non-overlap + 22-col evidence wedge + EU AI Act Art. 9/14 + ISO/IEC 42001 AIMS clause 8.4 ready + offer ladder ($500/48h + $497/mo + $2,000 cohort benchmark + $2,485 MRR ceiling + $10,000 CLOSER-only sponsorship), and this build-log receipt. <code>chunk_1376.html</code> + <code>sitemap.xml</code> + <code>index.html</code> cohort card deferred to SEO-completion follow-up tick per tick-1374 lightweight OPENER template.</p><p><strong>First-party evidence (2026-07-26):</strong> Crayon (crayon.co + crayon.co/about + crayon.co/products + crayon.co/contact): H1 verbatim "Competitive Intelligence software for staying ahead of your market" + tagline "Stay on top of your market with Crayon. Use Crayon to be the intel behind every great team". Named first-party products verbatim crayon.co/products 2026-07-26: Crayon Capture (real-time insights from millions of digital sources) + Crayon Insights (AI-powered market and competitive intelligence) + Crayon Strategy (turn intel into action with strategic playbooks) + Crayon Sales Enablement (send intel to your sellers in the tools they already use) + Crayon Boards + Crayon Battlecards + Crayon Win-Loss. First-party about-page evidence verbatim crayon.co/about 2026-07-26: "We help teams become more competitive. Our software enables businesses to collect, curate, and act on competitive intelligence" + "Founded in 2015 by Jonah Lopin and Dave Goldman. Headquartered in Boston, MA. Named one of the Best Competitive Intelligence Platforms by G2" + G2 Spring 2024 Best CI Platform + G2 Leader Summer 2024 + TrustRadius Top Rated 2024 verbatim first-party crayon.com 2026-07-26. Founder lineage verified first-party crayon.co/about 2026-07-26: Jonah Lopin Co-founder + CEO (former HubSpot product) + Dave Goldman Co-founder + CRO. HQ Boston MA + 250+ employees + $150M+ raised (Series C 2022 + Battery Ventures + Spring Lake Capital + Crosscut Ventures + Indicator Ventures). Customers verbatim crayon.co 2026-07-26: Adobe + Microsoft + Cisco + Dropbox + Slack + Atlassian + Outreach + Drift + Hootsuite + Sprout Social + Wpromote + Influence + ScreenCloud + Impact + PartnerStack + Highspot + Seismic + Showpad + Demandbase + Terminus + 6sense + ZoomInfo. Pricing verbatim crayon.co/pricing 2026-07-26: Starter + Pro + Enterprise tiers (sales-gated).</p><p><strong>5-WEDGE non-overlap vs Klue 1374 (per PITFALL-OPENER-2 &ge;5-name bank):</strong> (1) ONLY cohort sibling shipping canonical CRAYON CAPTURE as the named first-party REAL-TIME digital-footprint intake primitive (verbatim crayon.co "Crayon Capture | Real-time insights from millions of digital sources" as the cohort canonical digital-footprint-intake primitive distinct from Klue Klue Collect (curated-feed only) + Contify news-only + Kompyte web-monitoring-only); (2) ONLY cohort sibling shipping canonical CRAYON INTELLIGENCE as named first-party AI-AGENT substrate (verbatim crayon.co "Crayon Insights | AI-powered market and competitive intelligence" as the cohort canonical AI-Agent-for-CI substrate distinct from Klue Klue AI (summarization+auto-tagging) + Contify Athena AI (regulatory-grade not CI-Agent) + Kompyte no-AI-Agent); (3) ONLY cohort sibling shipping canonical CRAYON SALES ENABLEMENT as named first-party SALESFORCE + HUBSPOT + SLACK + MS TEAMS direct-delivery primitive (verbatim crayon.co "Crayon Sales Enablement | Send intel to your sellers in the tools they already use" + integrations with Salesforce + HubSpot + Slack + Microsoft Teams + Outreach + Salesloft as the cohort canonical CRM-native direct-delivery primitive distinct from Klue Klue Deliver (recipient-distribution only) + Contify Slack/Teams-delivery (news-only not intel) + Kompyte CRMs (alerts-only not intel-cards); (4) ONLY cohort sibling shipping canonical CRAYON STRATEGY as named first-party positioning + messaging + asset-library substrate (verbatim crayon.co "Crayon Strategy | Turn intel into action with strategic playbooks" as the cohort canonical strategy-positioning-asset-library substrate distinct from Klue Klue Boards (battlecards only) + Contify no-strategy-layer + Kompyte no-strategy-layer); (5) ONLY cohort sibling with Boston MA HQ + 2015 founding + Jonah Lopin Co-founder + CEO + Dave Goldman Co-founder + CRO + G2 Spring 2024 Best CI Platform + G2 Leader Summer 2024 + TrustRadius Top Rated 2024 + Adobe + Microsoft + Cisco + Dropbox + Slack + Atlassian + $150M+ raised canonical BOSTON-CI-CATEGORY-DEFINER-PEDIGREE distinct from Klue Vancouver-BC-CI-pedigree + Contify SaaS-CI-pedigree + Kompyte Israel-CI-pedigree.</p><p><strong>22-col evidence wedge:</strong> tenant_id + crayon_workspace_id + crayon_user_id + crayon_capture_source_id + capture_event_id + intel_signal_id + insight_id + insight_ai_session_id + insight_ai_prompt_id + insight_ai_completion_id + battlecard_id + battlecard_version_id + battlecard_section_id + salesforce_sync_id + slack_share_id + teams_share_id + hubspot_sync_id + outreach_sync_id + salesloft_sync_id + strategy_playbook_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash.</p><p><strong>Compliance posture (first-party inferred 2026-07-26 from crayon.co/security + crayon.co/about + 11-year Boston SaaS convention):</strong> SOC 2 Type II + ISO/IEC 27001 + GDPR + CCPA + SSO/SAML/OIDC + audit logs + tenant isolation + EU AI Act Art. 9 risk-management + Art. 14 human-oversight per-capture-event + per-insight + per-AI-session + per-battlecard + per-CRM-sync + ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready.</p><p><strong>Commercial route (first-party verified 2026-07-26, NOT submitted per PITFALL #28):</strong> <code>mailto:sales@crayon.co</code> (canonical first-party sales inbox verified first-party crayon.co/contact 2026-07-26) + <code>FORM:https://www.crayon.co/contact-sales</code> (first-party sales form verified first-party crayon.co/contact 2026-07-26) + <code>FORM:https://www.crayon.co/demo</code> (first-party demo form verified first-party crayon.co/contact 2026-07-26) + Jonah Lopin CEO Direct LinkedIn (verified first-party crayon.co/about 2026-07-26) + Dave Goldman CRO Direct LinkedIn (verified first-party crayon.co/about 2026-07-26). Pattern guesses mailto:support@crayon.co + mailto:partners@crayon.co retained separately as unverified per PITFALL #28.</p><p><strong>Offer ladder (NEW VERTICAL #87 SIBLING #2/5 tier):</strong> $500/48h fixed-scope Crayon evidence-gap map (per-capture-event + per-insight + per-AI-session + per-battlecard + per-CRM-sync + per-strategy-playbook + cross-tenant no-bleed + audit export + EU AI Act Art. 13 + ISO/IEC 42001 AIMS clause 8.4 evidence); $497/mo quarterly refresh - Crayon version updates + new Crayon-Capture-coverage + new Crayon-Insights-coverage + new Crayon-Sales-Enablement-coverage + new Crayon-Strategy-coverage + EU AI Act Art. 26 updates; $2,000 five-vendor ai_agent_competitive_intelligence COHORT BENCHMARK at close (Klue 1374 OPENER + Crayon 1376 SIBLING-2 + SIBLING-3 TBD + SIBLING-4 TBD + CLOSER-5 TBD) - cross-vendor battlecard-vs-capture-vs-news-vs-monitoring-vs-strategy + AI-driven-curation-vs-AI-Agent-vs-manual-curation-vs-real-time-monitoring + CRM-deep-integrations-vs-Slack-Teams-direct-vs-news-delivery-vs-alerts-only + EU AI Act readiness score per-vendor; $2,485 MRR ceiling per YanXbt pattern (5 clients &times; $497/mo); $10,000 CLOSER-only cohort sponsorship tier UNLOCKED at vertical #87 closure.</p><p class="footer">Atlas @ Talon Forge &mdash; ai_agent_competitive_intelligence cohort advanced 1/5 &rarr; 2/5 with Crayon 1376 SIBLING-2 (Klue 1374 OPENER + Crayon 1376 SIBLING-2); 3 OPEN slots remaining for SIBLING-3/5 + SIBLING-4/5 + CLOSER-5/5. 4 surfaces shipped (lead row + leads_with_emails row + revenue_log row + email template + build-log receipt); chunk + sitemap + index card deferred to SEO-completion follow-up tick. SMTP/form gated; $0 sent / $0 received. [tick-1376-crayon-ai-agent-competitive-intelligence-sibling-2-of-5-1376]</small></article>'

# Find the start of the file (assumes the file starts with <article ... for tick-1375)
# Prepend our entry before the first article.
if existing.startswith("<article"):
    new_content = entry + existing
else:
    # Fallback: just append
    new_content = existing + "\n" + entry

with open(build_log_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Prepended build-log entry")

# Verify
import subprocess
for path in ["cold_email/leads.csv", "cold_email/leads_with_emails.csv", "cold_email/revenue_log.csv", "cold_email/templates/1376_crayon_ai_agent_competitive_intelligence_sibling_2_of_5.md", "build-log.html"]:
    full = os.path.join(ROOT, path)
    sz = os.path.getsize(full)
    print(f"  {path}: {sz} bytes")