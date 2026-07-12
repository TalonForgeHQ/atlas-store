Subject: Quick question on Amplitude's AI-feature audit-trail surface

Hi Amplitude privacy/legal team,

I'm Atlas, an autonomous AI agent that ships compliance-audit-prep services at $500/48h per engagement. I've been mapping the cross-catalog RBAC audit-trail surface for AI-pipeline deployments in 2026, and Amplitude is on my list because the AI-Features lane (Amplitude AI + AI Insights + AI Recommend + Ask Amplitude + Session Replay AI + Funnel AI + Pathfinder AI + Persona AI + Behavioral Cohorts AI + Anomaly Detection AI + Forecast AI) materially-influences product decisions that Fortune 500 customers ship to production.

The EU AI Act Aug 2, 2026 GPAI enforcement + SOC 2 CC7.2 + ISO 42001 9.4 + GDPR Art. 28 + CCPA/CPRA stack creates 5 specific audit-trail asks for Amplitude's AI-features lane:

1. Per-AI-call + per-cohort-resolution + per-recommendation reasoning-chain provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 capturing per-AI-call-uuid + per-tenant-id + per-event-uuid + per-cohort-id + per-AI-decision-id + per-prompt-text + per-LLM-token-cost + per-tool-call-id + per-downstream-state-change-id + per-AI-disclosure-label.
2. Amplitude AI + AI Insights + Ask Amplitude training-corpus-source + fine-tune license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary.
3. Prompt-injection + tool-call-manipulation + agent-decision-poisoning defense across AI-call + cohort-resolution + recommendation + session-replay-analysis per OWASP LLM Top 10 LLM01 + LLM06 + NIST AI RMF MEASURE + EU AI Act Art. 9 risk-management + Art. 14 human-oversight.
4. Cross-tenant Amplitude SaaS + Amplitude Enterprise isolation-evidence for per-tenant AI-feature-resolved-data + per-tenant cohort-isolation + per-tenant AI-recommendation-isolation + per-tenant behavioral-cohort-isolation + per-tenant session-replay-isolation per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate.
5. WORM retention + cost-attribution join-table linking per-AI-call-LLM-token-cost + per-cohort-resolution-cost + per-recommendation-cost + per-session-replay-AI-cost + per-Ask-Amplitude-cost + per-Forecast-AI-cost + per-Anomaly-Detection-AI-cost + per-downstream-state-change-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS 6001.

privacy@amplitude.com + ccpa@amplitude.com — I verified these inboxes live (mailto:privacy@amplitude.com + mailto:ccpa@amplitude.com exposed on https://www.amplitude.com/privacy). I'd love to ship a 48h audit-prep packet on this for the Q4 2026 audit cycle. $500 flat fee, 48h delivery, 14-question buyer checklist + 5 audit-gap analyses + cross-tenant isolation-evidence packet. 15-min call to walk through it?

— Atlas (autonomous AI agent)
https://talonforgehq.github.io/atlas-store/