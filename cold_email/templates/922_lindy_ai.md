# 922_lindy_ai.md — Lindy AI (lindy.ai)

## Subject options
- Lindy AI agent audit trail review
- A practical evidence map for Lindy AI assistants
- Lindy AI: per-action receipts across inbox, calendar, voice

## Body

Hi there —

Lindy is the AI executive assistant that runs inbox triage, email drafting, meeting notes, scheduling, voice calls, and follow-ups across Gmail + Outlook + Google Calendar + iMessage/SMS + Zoom + Meet + Teams + a 100+ integration catalog. We built a compact procurement review that maps five evidence gaps teams commonly need before scaling an agent that touches mail, calendar, and outbound voice on their behalf:

1. recording-consent and retention evidence per integration (Gmail, Outlook, iMessage, SMS, Zoom, Meet, Teams);
2. per-action provenance — which model produced each draft / reply / scheduled event / outbound call, with the user-override or approval step that authorized it;
3. join-tables between Lindy actions and the underlying CRM, calendar, ticket, or document record they touched, so a reviewer can replay a single agent run end-to-end;
4. role-based access and tenant isolation for exported recordings, transcripts, draft mail, and calendar metadata; and
5. reproducible review receipts for agent actions and the human approval that authorized each one.

Lindy ships the controls worth checking: SOC 2 Type II audited by Johanson Group, HIPAA-eligible (signed BAA on the Enterprise tier), GDPR, PIPEDA, encryption in transit and at rest, and a no-train-on-customer-data posture. The gap we usually surface is the *audit replay* lane — proving which model produced a given draft and what human approval authorized it, across an entire week of mixed email + meeting + voice activity.

Would a one-page version of that review be useful for the person who owns AI governance or revenue operations at Lindy?

Best,
Atlas
Talon Forge
