# Cold Email — Snyk (cybersecurity)

**Subject:** Snyk DeepCode AI + SOC 2 scope on code-write path

Hi Peter,

DeepCode AI now writes code fixes — that's an autonomous AI agent pushing to PRs in production repos. Question for your SOC 2: is the AI's commit-authorization + secret-redaction path in audit scope?

The pattern I'm seeing in 2026: AI security tools get SOC 2'd at the cloud layer but the actual AI-write loop (LLM decides to fix → commits code → opens PR) is not. The risk surface is huge — secret leaks in training data, prompt injection via package.json names, mass-PR-spam from an exploited model.

I run a 48-hour **AI Agent Compliance Audit** ($500, Stripe). Maps Snyk DeepCode AI's write-loop to SOC 2 + the new OWASP Top 10 for LLMs (2026). 12-page report + specific controls to add to your next Type II.

— Atlas (Talon Forge)