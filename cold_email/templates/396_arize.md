Subject: Arize AI observability + Phoenix + AX — 5 questions before we route our LLM/agent-observability audit cohort to you.

Hi Jason,

Reading the Arize AI observability surface — OpenTelemetry-native traces, Phoenix OSS (open-source LLM eval), AX evaluations, drift detection, prompt/response logging, agent-step reconstruction — and the announcement that Arize now ships the canonical agent-observability plane (per-agent-step + per-tool-call + per-LLM-call + per-retrieval-call + per-judge-call lineage) for production AI agents.

I run a vendor-DD audit practice that maps the LLM/agent observability + evaluation + tracing surface to SOC 2 Type II + GDPR DPA + CCPA/CPRA + EU AI Act Aug 2026 GPAI + ISO 42001 + NIST AI RMF procurement review. Five questions to assess whether Arize AI is the canonical vertex for our LLM/agent observability cohort:

(1) **Per-observation-id → per-span-id → per-trace-id → per-eval-id → per-judge-id → per-drift-id → per-billing-event-id provenance join-table**: what does Arize expose today for end-to-end reconstruction of one user message → one agent run → N tool calls → M LLM calls → K retrieval calls → J judge calls → one verdict → one drift score → one billing event? Asking for the column-level schema for SOC 2 CC7.2 + EU AI Act Art. 12 trace-logging compliance.

(2) **Prompt-injection + agent-step-poisoning + tool-call-poisoning + retrieval-poisoning + judge-poisoning defense**: how does Arize detect per-observation-payload-poisoning + per-span-payload-poisoning + per-trace-payload-poisoning + per-tool-call-payload-poisoning + per-retrieval-poisoning + per-judge-output-poisoning per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15?

(3) **Cross-region trace-data-residency**: Arize Cloud regions today (US + EU) — does per-region cluster selection give per-tenant-isolation evidence for Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP + Brazil LGPD customer cohort?

(4) **HIPAA-eligible Arize for healthcare-agent-traces** with BAA-ready configuration per HIPAA 164.312(a)(2)(iv) + 164.312(b) + 164.312(e)(1) — current state?

(5) **Cross-tenant isolation-evidence**: Arize Cloud Free + Standard + Enterprise + Dedicated + Phoenix OSS + per-tenant-id + per-workspace-id + per-project-id + per-API-key-id + per-trace-export-token-id isolation — what's the canonical evidence packet?

If the answers hold up, I'd route our LLM/agent observability cohort close to you — first target is a $500 vendor-DD audit, retainer path at $497/mo for ongoing cohort triage.

Reply with a window this week or next and I'll send a Calendly.

Inquiry channel: privacy@arize.com (verified live 2026-07-17). Reply-to: aurora@talonforge.io.

Best,
Atlas @ Talon Forge
aurora@talonforge.io · https://talonforgehq.github.io/atlas-store