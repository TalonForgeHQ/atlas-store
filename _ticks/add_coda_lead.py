import csv
path = r'C:\Users\Potts\projects\atlas-store\cold_email\leads.csv'
with open(path, 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    rows = list(reader)

new_row = [
    '577',
    'Coda',
    '@coda_hq',
    'privacy@coda.io',
    'ai_work_management',
    '1',
    '577_coda.md',
    ("Real company, website, AI-product surface, security posture, and inbox verified live 2026-07-19. "
     "https://coda.io/about returned HTTP 200 and first-party copy confirms Coda (now Superhuman Docs after Grammarly acquisition) "
     "is the work-operating-system sibling used by 50,000+ teams and 80% of the Fortune 100, with Coda Brain AI surfaces, "
     "AI blocks, AI summaries, AI columns, AI chat, and 600+ integrations reading and writing the same doc-page-database-button-automation "
     "surface plus connected Slack, Google Workspace, Microsoft 365, GitHub, Jira, and Salesforce state. "
     "Coda Brain explicitly positions itself as the hallucination-resistant work AI for grounding LLMs in live team data. "
     "https://coda.io/trust returned HTTP 200 and publishes SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, "
     "ISO/IEC 27701, GDPR, CCPA, HIPAA BAA, AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, and EU/US regional data residency. "
     "Public-record canonical inbox: privacy@coda.io. coda.io has live Google Workspace MX with valid SPF/DKIM/DMARC. "
     "Public-record founders: Shishir Mehrotra (CEO, ex-YouTube VP Product), Alex Dewhirst, and Mark Solomon; founded 2014 in San Francisco. "
     "Tier-1 ai_work_management cohort sibling #11 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, ClickUp 572, "
     "monday.com 573, Linear 574, Notion 575, and Asana 576. "
     "Distinct wedge: Coda is the doc-database-AI sibling where Coda Brain, AI blocks, AI columns, AI summaries, and the Coda Pack SDK "
     "all read and write the same doc-page-row-column-button-puzzle-formula-automation surface plus 600+ connected integrations. "
     "Audit wedge: source-doc-to-retrieved-row/page/column-to-prompt/model/version-to-Coda-Brain-plan-to-tool-call-to-page/row/column/button/"
     "puzzle/formula/automation-mutation-to-Pack-sync provenance; prompt-injection defense for untrusted doc bodies, table rows, column values, "
     "form responses, button actions, puzzle formulas, file uploads, and connected Slack/Google/Microsoft/Jira/GitHub/Salesforce content; "
     "workspace/doc/page/row/column/button/puzzle/formula/guest/Pack/data-residency isolation; deletion/retention/version-history/Pack-sync "
     "propagation; immutable human-approval evidence for AI-generated doc sections, AI column fills, AI summaries, AI chat answers, AI button "
     "actions, AI puzzle outputs, and external Pack/connector writes; per-agent/per-model/per-tool-call/per-workspace/per-Pack/per-connection "
     "cost attribution across Coda Brain, AI blocks, AI columns, AI summaries, Coda Pack SDK, Coda API, and Slack/Google/Microsoft/Jira/GitHub/"
     "Salesforce bridges. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh.")
]
rows.append(new_row)

with open(path, 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerows(rows)

print(f'Appended row {len(rows)-1}. New file has {len(rows)} rows total.')
with open(path, 'r', encoding='utf-8') as f:
    line = f.readlines()[-1]
print(f'Last line length: {len(line)} chars')
print(f'Last line preview: {line[:200]}...')
