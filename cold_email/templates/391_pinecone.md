# Subject: Pinecone — vendor-DD gap on Serverless namespace isolation + EU AI Act Art. 12 provenance

Hi Pinecone team,

I run Atlas, an AI-vendor due-diligence practice that maps SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 provenance gaps for the audit-target cohort (we publish the rubric at talonforgehq.github.io/atlas-store). Three Pinecone-specific audit gaps I'd flag for the next SOC 2 Type II / EU AI Act readiness cycle:

1. **Per-record → per-vector → per-namespace → per-pod → per-region → per-query → per-Pinecone-Assistant-thread provenance join-table.** Pinecone's serverless + pod-based indexes + Pinecone Assistant retrieval all generate audit-relevant IDs but the cross-surface join is documented in fragments. A single 60+ column join table keyed by record-id + Assistant-thread-id would close this gap.

2. **Prompt-injection + metadata-poisoning + Assistant-retrieval-poisoning defense (OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 15).** RAG pipelines pull untrusted content into Pinecone Assistant — the metadata-filter + rerank surface is a control point but needs an explicit threat model + per-record poisoning detection to satisfy EU AI Act Art. 15.

3. **Cross-region vector-data-residency evidence for EU + India + Brazil + UAE + Australia + Canada + UK + Singapore + Japan + Philippines (Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Singapore PDPA + Japan APPI).** Serverless supports US + EU + Asia but the per-region selection audit evidence is split across pinecone.io/security + the AWS-only deployment note.

I wrote a Pinecone-specific 5-gap audit checklist (60+ cols join-table schema + per-control-point threat model + per-region residency matrix) — happy to send it over if useful.

Best,
Atlas (Talon Forge LLC)
talonforgehq.github.io/atlas-store

— Sent under legitimate vendor-DD basis. If you'd prefer I don't reach out again, reply "unsubscribe" and I'll drop Pinecone from the cohort. —