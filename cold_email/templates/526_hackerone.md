# Subject: HackerOne agentic-AI security audit — 5 evidence gaps before procurement asks

Hi Jobert,

HackerOne's H1 AI Red Teaming, Hai agentic orchestrator, H1 Agentic Pentest, and H1 Code create a rare audit surface: human security findings and autonomous security actions now share the same customer evidence chain.

I can map five gaps for HackerOne in a fixed-fee, 48-hour audit:

1. **End-to-end action provenance.** Can each target, model/prompt version, tool call, finding, human validation, severity change, remediation, and retest be reconstructed under SOC 2 CC7.2 and EU AI Act Article 12?

2. **Agent authority and human oversight.** Are Hai and H1 Agentic Pentest permissions, stop conditions, approvals, and emergency revocation bound to each action under EU AI Act Article 14 and NIST AI RMF?

3. **Hostile-input defenses.** Are prompt injection, repository poisoning, forged vulnerability evidence, secret exfiltration, and tool-result poisoning tested against OWASP LLM Top 10 and MITRE ATLAS?

4. **Tenant and target isolation.** Can HackerOne prove that prompts, code, findings, credentials, payloads, and model context cannot cross customer programs, assets, or data-residency boundaries under SOC 2 CC6.1, GDPR Article 28, and ISO 27001?

5. **Immutable incident evidence.** Are model changes, agent costs, exploit attempts, human decisions, disclosure events, and deletion propagation retained in WORM-capable records with a repeatable reconstruction drill?

Deliverable: one Markdown report, one CSV remediation backlog, and one 30-minute walkthrough. Fixed price: **$500**, delivered within **48 hours**. No prep is needed beyond one architecture diagram and a redacted sample action trace.

If useful, reply with a target delivery date and I'll send the one-page scope within four hours.

Best,
Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/
