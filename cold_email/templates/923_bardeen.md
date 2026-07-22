# 923_bardeen.md — Bardeen (bardeen.ai)

## Subject options
- Bardeen agent audit trail review
- A practical evidence map for Bardeen workflow automations
- Bardeen: per-action receipts across scraping, enrichment, CRM, and chat

## Body

Hi there —

Bardeen is the workflow-automation platform that turns repetitive scraping, enrichment, CRM-update, and chat-driven ops tasks into no-code agents running in the browser. With SOC 2 Type II, GDPR, and CASA Tier 2 / Tier 3 already in place, Bardeen's procurement posture is solid; what we usually help teams close is the *audit replay* lane that connects each Bardeen action back to the model, prompt, and human authorization that produced it.

We built a compact procurement review that maps five evidence gaps teams commonly need before scaling an automation fleet that touches Salesforce, HubSpot, LinkedIn, Notion, Google Sheets, and a long tail of internal web apps:

1. recording-consent and retention evidence per integration (Salesforce, HubSpot, LinkedIn, Notion, Google Sheets, Slack, chat-driven intent surfaces);
2. per-action provenance — which automation, which model, which prompt produced each scrape, enrichment, CRM update, or chat-driven action, with the user-override or approval step that authorized it;
3. join-tables between Bardeen actions and the underlying CRM, sheet, ticket, or document record they touched, so a reviewer can replay a single automation end-to-end;
4. role-based access and tenant isolation for cached scraping results, enrichment payloads, CRM write-back payloads, and chat-bound metadata; and
5. reproducible review receipts for automation runs and the human approval that authorized each one.

Bardeen ships the controls worth checking: SOC 2 Type 2, GDPR, CASA Tier 2 / Tier 3. The gap we usually surface is the *audit replay* lane — proving which automation produced a given write-back and what human approval authorized it, across a full week of mixed scraping + enrichment + CRM activity.

Would a one-page version of that review be useful for the person who owns automation governance or revenue operations at Bardeen?

Best,
Atlas
Talon Forge
