# Cold Email Template 981 — HashiCorp Boundary Infrastructure Identity + Agentic AI Security

**Template family:** `ai_infrastructure_identity_pam` SIBLING #3/5  
**Lead:** HashiCorp, Inc. (Boundary product) — hashicorp.com / boundaryproject.io  
**Vertical:** infrastructure identity, identity-aware proxy, credential brokering, agentic AI  
**Offer:** $500/48h evidence-gap map or $497/month quarterly refresh  
**Status:** TEMPLATE ONLY — no email or form submission claimed

---

## Verified evidence set (2026-07-23)

- HashiCorp, Inc. founded 2012 by Mitchell Hashimoto and Armon Dadgar, two University of Washington Paul G. Allen School of Computer Science classmates (en.wikipedia.org/wiki/HashiCorp).
- HashiCorp HQ 101 Second Street, San Francisco; current CEO David McJannet; 2024 revenue $583M.
- Mitchell Hashimoto resigned from the company in December 2023.
- On April 24, 2024, HashiCorp announced an agreement to be acquired by IBM for $6.4 billion.
- HashiCorp Boundary first released October 2020 — an identity-aware proxy for dynamic infrastructure.
- The first-party Boundary README on github.com/hashicorp/boundary states Boundary "integrates with your IdP of choice using OpenID Connect," "provides just-in-time network access to network resources," "manages session credentials via a native static credential store, or dynamically generate unique per-session credentials by integrating with HashiCorp Vault," "manages privileged sessions using Boundary's session controls," and runs "in clouds, on-prem, secure enclaves" without requiring an agent on every end host.
- Boundary ships an open-source Community Edition and a managed HCP Boundary plus HCP Vault credential-brokering tutorials.
- Boundary's domain model (developer.hashicorp.com/boundary/docs/concepts) treats every user, host, target, and credential as a first-class resource with role-based policy.
- First-party security contact security@hashicorp.com published in the Boundary GitHub README.
- Commercial route: https://www.hashicorp.com/contact-sales + security@hashicorp.com. Neither was used in this tick.

---

## Subject options

1. `Boundary credential-brokering replay — five evidence gaps`
2. `Can one Vault-credentialed Boundary session survive an IBM-acquisition audit?`
3. `HashiCorp Boundary + AI agents: identity-aware proxy evidence map`

## Open

Hi {{first_name}} — I mapped HashiCorp Boundary's identity-aware-proxy model against Teleport's infrastructure-identity model and Delinea's PAM control plane, focusing on the credential-brokering layer where AI-agent identity becomes a privileged network action.

Boundary ships a differentiated surface: identity-aware proxy + OpenID Connect IdP integration + just-in-time network access + native static credential store + Vault-credentialed dynamic credentials + session controls + multi-protocol support (SSH + RDP + HTTP + HTTPS + K8s) without requiring an agent on every end host. The procurement question is whether those named controls join into one replayable receipt, especially post-IBM-acquisition.

## Five-question evidence replay

1. **Agent-to-credential lineage:** Can one AI-agent action be joined to agent identity, model and prompt version, Boundary session, OIDC IdP claim, Vault-credentialed dynamic secret, target host, target port, and tenant?
2. **Identity-aware proxy decision:** Does every Boundary authorization decision preserve session-id, scope, host-set, target, time-bound, approval, and final state?
3. **Vault credential brokering:** Can a Vault-issued dynamic credential be joined to the requesting Boundary session, the target host, the rotation cadence, the lease, and the revocation, without a manual correlation step?
4. **Failure paths:** Are denied, expired, retried, cancelled, orphaned, session-recording-failed, and rolled-back sessions retained with the same fidelity as successful sessions?
5. **Regulatory export:** Can the evidence package support SOC 2, ISO 27001, PCI DSS, GDPR, ISO 42001, NIS2, and EU AI Act human-oversight review without reconstructing the story from separate consoles?

## Deliverable

Within 48 hours I return:

- one red/amber/green evidence-gap map;
- the five missing joins with highest procurement impact;
- a sample AI-agent → OIDC claim → Boundary session → Vault credential → target host → revocation receipt;
- a Teleport / Delinea / Boundary comparison focused on identity issuance vs. PAM control plane vs. credential brokering;
- an IBM-acquisition + Boundary-license continuity checklist; and
- a 30-minute handoff for Platform Security, Infrastructure Identity, Trust, or Compliance.

The single-platform map is **$500 / 48 hours**. A quarterly refresh covering policy, connector, model, OIDC, Vault, credential, and compliance changes is **$497/month**. The five-vendor cohort benchmark will be **$2,000** once the cohort closes.

## Close

Worth sending the one-page Boundary sample before we decide whether the full infrastructure-identity benchmark is useful?
