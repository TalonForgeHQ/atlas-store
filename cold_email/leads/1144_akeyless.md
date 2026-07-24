# Lead 1144 — Akeyless (Secrets Security for AI Agents)

**Real company:** Akeyless Security Ltd.
**Real website:** akeyless.io
**Real CEO:** Shai Alon (co-founder, ex-VP Engineering CyberArk)
**Real co-founder:** Oded Noam (ex-VP R&D CyberArk)
**HQ:** Tel Aviv, Israel + New York, NY
**Founded:** 2018
**Stage:** Series B — $65M Series B (Apr 2021, led by Insight Partners), $14M Series A (2019). Total ~$79M raised.
**Vertical:** ai_agent_secrets_security (NEW cohort — opens AI-agent secrets/credentials/key-management wedge)
**Tier reason:** Only secrets-management vendor that ships (1) **Vault-Less SaaS** Secrets Management with **Distributed Fragments Cryptography (DFC)** — no master key, no single point of failure, sub-10ms retrieval; (2) **AI Agent Identity & Credentials** lane with per-agent short-lived dynamic secrets + per-agent workload-identity binding (spiffe-compatible) + per-invocation token rotation; (3) **MCP-aware** workload-identity binding for Claude Desktop + Cursor + Windsurf + Cline + Continue + Replit Agent + Devin + Codex local IDE integrations; (4) **BYOK + HSM-less FIPS-140-3** roll-your-own-KMS compatibility with AWS KMS + GCP KMS + Azure Key Vault + HashiCorp Vault (where Vault is the integration endpoint, not the source-of-truth); (5) **Zero-Trust just-in-time** access for human + non-human identities with per-request policy enforcement + per-session audit-log.

**Compliance posture:** SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + HIPAA + GDPR + UK GDPR + EU AI Act readiness + CCPA/CPRA + FedRAMP-In-Process + PCI DSS 4.0.

**Real differentiator for AI-agent cohorts:** the only vendor that ships a single-tenant, no-master-key, BYOK-or-HSM-less secrets plane that simultaneously binds to (a) human dev workloads, (b) non-human agent workloads (Claude/Cursor/MCP), and (c) runtime infrastructure (Lambda/Cloud Run/ECS/EKS/GKE/AKS) with the same per-request audit-log replay — without forcing customers to deploy HashiCorp Vault themselves.

**Tier-1 evidence wedge (5 surfaces, machine-reproducible):**
1. Per-secret versioned audit-trail with per-access actor + per-workload-identity + per-MCP-server + per-session attestation + per-customer retrieval of per-secret-version history without DFC re-derivation.
2. AI Agent Identity & Dynamic Secrets ledger with per-agent spiffe-id + per-invocation ephemeral token + per-secret-TTL bucket + per-rotation cadence cross-tenant-no-bleed invariant.
3. DFC fragment-distribution replay showing no single Akeyless replica can reconstruct any secret fragment alone (k-of-n threshold scheme with per-fragment per-replica per-region hash chain).
4. MCP-server + per-agent-tool-call per-secret-decision audit-log replay with per-MCP-server auth boundary + per-invocation policy enforcement + per-decision signing.
5. EU AI Act + NIST AI RMF + NIST CSF 2.0 governance mapping for AI-agent credentials — per-AI-use-case risk-tier evidence-pinning across Akeyless Secrets + Akeyless Connect + Akeyless CLI + Akeyless API + Akeyless Universal Identity.

**Offer:** $500/48h fixed-scope AI-agent secrets-evidence-gap map (machine-reproducible audit-export), or $497/mo quarterly refresh.

**Contact:** first-party demo form /contact + verified LinkedIn Shai Alon + verified LinkedIn Oded Noam.

**Cohort position:** OPENER #1/5 of NEW VERTICAL #49 ai_agent_secrets_security.
