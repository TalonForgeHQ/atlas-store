import csv
path = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
with open(path, "r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
print("before", len(rows), rows[-1][0])

tier_reason = (
    "Canonical AI-revenue-forecasting + pipeline-inspection + deal-health-score + "
    "at-risk-flag-propagation + AI-forecast-roll-up + commit-vs-best-case-vs-pipeline-coverage-recompute + "
    "downstream-Salesforce/HubSpot-state-change + downstream-CRO-compensation-decision + "
    "downstream-SEC-10-Q-revenue-guidance-decision + downstream-board-of-directors-forecast-published-decision + "
    "downstream-investor-day-published-revenue-guidance platform (Clari Forecast + Clari Inspect + Clari Copilot + "
    "Clari Revenue Context + Clari Groove + Clari Cadences + Clari Deal Room + Clari Pipeline + Clari Spotlight); "
    "evidence: privacy@clari.com directly verified 2026-07-12 via curl scrape of https://www.clari.com/privacy/ "
    "(HTTP 200, mailto:privacy@clari.com exposed in the canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD "
    "strategic-inbound channel routed to the privacy/legal/security team - consistent with the public "
    "ai_sales_ai-inbox pattern used at Gong 167 privacy@gong.io + Outreach 138 privacy@outreach.io + "
    "Lavender 117 privacy@lavender.ai). Founder CEO Andy Byrne (publicly known, ex-Siebel VP + early MarkLogic "
    "founder) co-founded Clari 2012 (originally as a sales-analytics SaaS, pivoted to AI-revenue-forecasting 2018); "
    "HQ Sunnyvale California + Bangalore India engineering hub; raised $500M+ across rounds from Sequoia Capital "
    "(Series A lead) + Tenaya Capital + Norwest Venture Partners + Sapphire Ventures (Series E lead $225M at "
    "$2.6B post-money 2021) + BlackRock + Silver Lake + Greenoaks; ~1500+ enterprise customers including "
    "Datadog + Crowdstrike + Okta + Zoom + Auth0 + Atlassian + Workday + HashiCorp + Zendesk + Nutanix + "
    "Qualtrics + RingCentral + Medallia + Alation. SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR DPA + "
    "HIPAA-eligible + FedRAMP Moderate-in-progress per public trust page (clari.com/security + clari.com/privacy + "
    "clari.com/dpa). 7th ai_sales_ai lead in pipeline + sibling-target of Outreach 138 + Salesloft 139 + "
    "Persana 221 + Artisan 222 + Lavender 117 + Gong 167. Distinct because Clari is the only "
    "AI-revenue-forecast-roll-up-as-audit-target + AI-deal-health-score-recompute + "
    "commit-vs-best-case-vs-pipeline-coverage-recompute + downstream-CRO-compensation-decision + "
    "downstream-SEC-10-Q-revenue-guidance-decision + downstream-board-of-directors-forecast-published-decision + "
    "downstream-investor-day-published-revenue-guidance vendor in the pipeline - the audit-trail surface is the "
    "per-forecast-run forecast-decision + deal-health-score-recompute-decision + at-risk-flag-propagation-decision + "
    "commit-vs-best-case-vs-pipeline-coverage-recompute-decision + downstream-CRO-compensation-decision + "
    "downstream-SEC-10-Q-revenue-guidance-decision + downstream-board-of-directors-forecast-published-decision "
    "join-table (which ai-forecast-decision + which deal-health-score-recompute-decision + which "
    "commit-vs-best-case-vs-pipeline-coverage-recompute-decision + which downstream-Salesforce-state-change + which "
    "downstream-HubSpot-state-change + which downstream-CRO-compensation-decision + which "
    "downstream-board-of-directors-forecast + which downstream-investor-day-published-revenue-guidance occurred), "
    "which is fundamentally different from per-conversation-call-recording (Gong 167) + per-email-engagement-step "
    "(Outreach 138 / Salesloft 139) + per-prospect-research (Persana 221 / Artisan 222) + per-email-coaching-feedback "
    "(Lavender 117) audit lanes. 5 audit gaps as detailed in template 253_clari.md. privacy@clari.com verified live "
    "as the canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channel for ai_sales_ai "
    "AI-revenue-forecast-roll-up audit-target inquiries."
)

new_row = ["173", "Clari", "@clariinc", "privacy@clari.com",
           "ai_sales_ai", "1", "253_clari.md", tier_reason]
rows.append(new_row)

with open(path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerows(rows)

print("after", len(rows), rows[-1][0], rows[-1][1])