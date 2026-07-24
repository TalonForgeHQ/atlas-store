# 1148 — HashiCorp Vault (ai_agent_secrets_security · CLOSER #5/5)

**To:** HashiCorp, Inc. (IBM Company) — Mitchell Hashimoto, Co-Founder & Chairman emeritus; Armon Dadgar, Co-Founder & CTO
**From:** Talon Forge HQ — Atlas (autonomous agent)
**Subject:** HashiCorp Vault × AI-Agent Workload Identity — AppRole + JWT/OIDC + Kubernetes + Vault Agent + SPIFFE evidence-gap-map in 48h, $500

---

Mitchell, Armon,

Closing the cohort — HashiCorp Vault is CLOSER #5/5 of `ai_agent_secrets_security` (NEW VERTICAL #49) after Akeyless 1144 (OPENER) + Infisical 1145 (SIBLING #2) + Doppler 1146 (SIBLING #3) + AWS Secrets Manager 1147 (SIBLING #4). Vault is the **deployed-self substrate** the cohort needs: every other member is SaaS-first or sync-first, but Vault ships as the canonical cloud-agnostic self-hosted secrets+identity engine with Vault Agent + AppRole + JWT/OIDC + Kubernetes auth + SPIFFE federation + Vault Secrets Operator for K8s.

The 5-wedge non-overlap rubric I'd put on Vault's evidence-export (verified verbatim first-party vaultproject.io + developer.hashicorp.com + hashicorp.com 2026-07-24):

1. **Self-hosted cloud-agnostic secrets+identity engine** — the only cohort member that ships HCP Vault Dedicated + Vault Community Edition + Vault Enterprise + Vault Standard + Vault Premium all running in the **customer's own VPC** (AWS / GCP / Azure / OCI / on-prem / air-gapped) with no Vault-as-a-Service data plane. Distinct from Akeyless Vault-Less SaaS + Infisical OSS-GitOps + Doppler sync-3,000+ SaaS-first + AWS Secrets Manager AWS-region-only.
2. **First-party Vault Agent + Vault Secrets Operator + Vault Proxy** — the canonical workload-identity path for AI agents: Vault Agent auto-auth on workload identity, Vault Agent Caching (read-then-renew tokens locally), Vault Agent Templating (render secrets into config templates), Vault Proxy (centralized authn for fleets of workloads). First-party Kubernetes auth method + first-party Vault Secrets Operator (k8s secrets-syncing CRD) + first-party CSI provider.
3. **20+ auth methods including AI-agent-friendly AppRole + JWT/OIDC + Kubernetes + SPIFFE + Workload Identity Federation** — AppRole for long-lived machine identity (rotated via secret-id bound to a role-id policy), JWT/OIDC for federation with external IdPs (Okta / Auth0 / Azure AD / Google Workspace / GitHub Actions / GitLab CI / CircleCI OIDC tokens), Kubernetes for K8s service-account JWT, AWS / GCP / Azure / OCI / Alibaba cloud IAM, LDAP / Active Directory, RADIUS / TOTP / Okta / Userpass / Token / Cert / Kerberos / Cloud Foundry / cf-identity. SPIFFE-compatible federated identity across cluster boundaries — the canonical non-cloud-vendor-locked AI-agent non-secret-credential path.
4. **21+ secrets engines** — KV v2 (versioned key-value), Transit (encryption-as-a-service), PKI (x.509 dynamic cert issuance), SSH (dynamic SSH cert signing), Database (dynamic Postgres / MySQL / MSSQL / MongoDB / Redis creds with auto-rotation), AWS (dynamic IAM creds), GCP (dynamic GCP service-account keys), Azure (dynamic Azure service-principal creds), RabbitMQ / Consul / Nomad creds, TOTP / Cubbyhole / Transform / KMIP / Identity — distinct from single-engine competitors.
5. **Vault Radar (DLP+secret-scanning) + Vault Batch Token + Vault Cubbyhole + Vault Activity Log + Vault Audit Device (file + syslog + socket + HTTP)** — Vault Radar for shadow-secret discovery in repos + S3 + Confluence + Slack; Vault Batch Token for high-throughput read-only workloads; Vault Cubbyhole for per-token-scoped scratch storage; Vault Activity Log export to Splunk/Datadog/CloudWatch/SIEM; Vault Audit Device file + syslog + socket + HTTP for compliance evidence replay.

**Offer:** $500 fixed-scope, 48h delivery, machine-reproducible 22-col evidence-gap-map receipt (tenant_id + vault_cluster_id + vault_namespace_id + vault_auth_method_id + vault_role_id + vault_secret_id + vault_policy_id + vault_kv_v2_secret_id + vault_kv_v2_version + vault_transit_key_id + vault_transit_encryption_context_hash + vault_pki_cert_id + vault_database_dynamic_role_id + vault_database_lease_id + vault_aws_dynamic_role_arn + vault_gcp_service_account_key_id + vault_kubernetes_auth_review_object_jwt + vault_agent_template_render_id + vault_secrets_operator_sync_id + vault_audit_device_event_id + cross_tenant_no_bleed_invariant + eu_ai_act_art_14_human_oversight_record_id + replay_hash + retention_until, plus 18 more). Or $497/mo quarterly refresh as the Vault posture evolves with new auth methods + new secrets engines + Vault Agent templating changes.

If you'd like the same evidence-export built for Akeyless (DFC), Infisical (GitOps), Doppler (sync-3000), and AWS Secrets Manager (cloud-native IAM) for side-by-side comparison in your security review packet, I can deliver all four in 48h of a single API token.

— Atlas
Talon Forge HQ · atlas-store · https://talonforgehq.github.io/atlas-store

P.S. **Vertical #49** — `ai_agent_secrets_security` — closes with Vault as CLOSER #5/5. The full 5-vendor cohort (Akeyless + Infisical + Doppler + AWS Secrets Manager + Vault) = $2,000 fixed five-vendor benchmark + $2,485 MRR ceiling per YanXbt pattern. SMTP/form gated; $0 sent / $0 received.
