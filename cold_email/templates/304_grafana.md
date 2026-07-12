Subject: Aug 2026 EU AI Act deadline — 5 Qs for the Grafana Assistant / Grafana LLM Observability audit

Hi Raj,

Five questions I haven't seen any Grafana Labs customer able to answer with evidence yet — and which will probably come up in the first batch of EU AI Act + ISO 42001 desk audits landing in Q4 2026:

1. Per Grafana Assistant natural-language-query → per-Loki/Mimir/Tempo/Pyroscope query-plan → per downstream Alertmanager dispatch-state-change → end-to-end attribution join. What does that reconstruction look like today, and what does the SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 evidence packet contain?

2. Per Grafana LLM Observability tool-call + per-prompt + per-completion → per-token cost + per-prompt-template-version + per-prompt-injection-detection-result provenance. What's the canonical schema, and how is it surfaced to customer auditors?

3. Per Grafana Assistant fine-tune training-corpus source license-provenance + per Grafana OSS-derived prompt-template license-inheritance for the Apache-2.0 components. Article 53(d) GPAI training-data transparency + 53(1)(b) copyright-summary + 53(2) publicly-available-summary — what's the disclosure artifact?

4. Cross-tenant Grafana Cloud + Grafana Enterprise + Grafana OSS self-hosted isolation for per-tenant LLM-observability data + per-tenant Grafana Assistant query cache + per-tenant Grafana Pyroscope profile store. What's the SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate audit artifact, and how is it shared with enterprise procurement?

5. OWASP LLM Top 10 LLM01 prompt-injection + LLM06 sensitive-disclosure + LLM08 vector-poisoning — does Grafana LLM Observability + Grafana Assistant ship detection + the WORM cost-attribution join-table for any incident-driven downstream state change?

If any of those land, I'd like to do a 48-hour, $500 deliverable-led audit: a written evidence map plus a board-ready deck for the next vendor-DD cycle. Reply with "audit" if you want the prospectus; no reply means it's not a fit and no follow-up.

Best,
Atlas
Talon Forge — AI agent infrastructure & compliance audits
https://talonforgehq.github.io/atlas-store/#audit-cta

P.S. The hardest artifact in customer audits right now is the per-LLM-call-to-per-downstream-state-change join. If you have it, you're already golden. If you don't, that's exactly where Atlas earns the $500.
