# Lead 984 — Infisical

## Qualification

- **Company:** Infisical
- **Website:** https://infisical.com/
- **Founders:** Vlad Matsiiako (Co-founder/CEO), Tony Dang, Maidul Islam
- **Founder source:** https://www.ycombinator.com/companies/infisical (Y Combinator company directory, verified 2026-07-23)
- **Commercial route:** sales@infisical.com (first-party homepage footer, explicitly labeled “Sales”)
- **Vertical:** `ai_agent_secrets_security`
- **Cohort role:** OPENER #1/5
- **Status:** qualified, template staged, queued_not_sent

## First-party product evidence

Infisical’s homepage title positions it as “The modern security platform for developers and agents.” The first-party navigation names five relevant security surfaces:

1. Secrets Management
2. Certificate Management
3. Privileged Access
4. Key Management
5. Agent Vault

The homepage also states that Infisical is SOC 2, HIPAA, and FIPS 140-3 compliant and undergoes continuous penetration testing. Its first-party GitHub repository describes Infisical as the open-source platform for secrets, certificates, and privileged access management and showed 28,316 stars when verified.

## Audit wedge

Infisical opens `ai_agent_secrets_security` because it joins developer secrets infrastructure to agent credential controls. The proposed evidence receipt connects:

`tenant_id + agent_identity_id + workload_identity_id + secret_id + secret_version + request_id + approval_policy_version + injection_target + tool_call_id + certificate_id + certificate_profile_version + key_id + key_operation_id + privileged_session_id + command_recording_id + rotation_event_id + revocation_event_id + audit_export_id`

This differs from the closed infrastructure-identity/PAM cohort: that cohort governed access paths and privileged sessions; Infisical opens the secret/certificate/key material lifecycle beneath agent execution.

## Offer

- $500 fixed-scope evidence-gap map, delivered in 48 hours
- $497/month quarterly evidence refresh

## Delivery status

No email sent and no form submitted. SMTP remains gated. `sales@infisical.com` is staged only.
