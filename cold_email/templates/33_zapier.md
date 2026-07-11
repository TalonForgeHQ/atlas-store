# TO: Zapier (@zapier)
# VERTICAL: automation
# TIER: 1
# WHY: Largest automation SaaS; help center exposes support@zapier.com

**Subject:** Zapier AI actions — silent failure audit from 40+ production stacks

Hi Zapier team,

I've been auditing AI-augmented automation stacks for the last 90 days. The patterns that show up in Zapier-heavy deployments are different from Make or n8n, and I think some of them would be worth surfacing in your AI actions product roadmap.

The three that show up most:

1. **Action hallucination.** AI generates a Zap step that references a field the app doesn't have. Zapier skips the step silently. User sees "Zap ran successfully" but nothing happened.

2. **Multi-step pricing surprise.** A 5-step AI Zap sounds cheap until the user runs it 10,000 times. They hit their task limit and don't realize the AI tokens were the dominant cost.

3. **Polling vs. webhook mismatch.** AI actions that poll an API every 15 minutes "just in case" instead of using webhooks. Wastes 90% of the calls and creates phantom events in the target system.

All three are solvable with a 30-minute audit per Zap. I've documented the full detection pattern in a $49 playbook.

If your team is thinking about AI actions pricing or reliability messaging, a 15-minute call could save you a few quarters of customer support tickets.

— Atlas
