# Lead 753 — Modal evidence note

**Company:** Modal Labs, Inc.
**Website:** https://modal.com/
**Route:** `mailto:security@modal.com` (first-party Enterprise / HIPAA BAA / SOC 2 / PCI / GDPR contact published on modal.com/docs/guide/security); alt `mailto:support@modal.com` (first-party support line on modal.com/company)
**Lead 753 row file:** `cold_email/leads.csv`
**Lead 753 template file:** `cold_email/templates/753_modal_agent_sandbox_followup.md`
**Lead 753 SEO file:** `chunks/chunk_753.html`

## Live evidence (curl-verified 2026-07-21, Mozilla/5.0 Chrome/130.0 UA)

- modal.com/ (HTTP 200, title "Modal: High-performance AI infrastructure", og:description "Bring your own code, and run CPU, GPU, and data-intensive compute at scale. The serverless platform for AI and data teams.", $30/month free compute, Sign Up form at /signup, Contact Us button on the nav)
- modal.com/company (HTTP 200, founders identified by image alt "Our founders Erik Bernhardsson and Akshat Bubna, pictured with Mugi (Akshat's dog)", "We've raised over $466M from some of the best investors and product leaders in the industry. Our investors include General Catalyst, Redpoint Ventures, Lux Capital, Amplify Partners, Creandum, and more." Modal's team is based out of New York, Stockholm, and San Francisco; explicit NYC address "233 Spring St, Floor 11", Stockholm "Sveavägen 17, Floor 16", SF "375 Alabama St, Suite 490"; explicit contact section "Email: support@modal.com" first-party footer of /company)
- modal.com/docs/guide/security (HTTP 200, "SOC 2: We have successfully completed a System and Organization Controls (SOC) 2 Type 2 audit. Go to our Security Portal https://trust.modal.com to request access to the report."; "HIPAA: Modal's services can be used in a HIPAA compliant manner... To use Modal services for HIPAA-compliant workloads, a Business Associate Agreement (BAA) should be established with us prior to submission of any PHI. This is available on our Enterprise plan. Contact us at security@modal.com"; "PCI: Payment Card Industry Data Security Standard... please send an email to security@modal.com"; "Questions? Email us!" — security@modal.com)
- modal.com/legal/privacy-policy (HTTP 200, "Privacy Policy of Modal Labs", "Last updated May 17th, 2023")
- modal.com/legal/terms (HTTP 200, "Modal Labs, Inc. ... Services provided by Modal Labs, Inc.", "GDPR ... UK GDPR ... Standard Contractual Clauses ... Article 46 of GDPR or UK GDPR equivalent")
- modal.com/products/sandboxes (HTTP 200, Modal Sandbox dashboard screenshot, automated health checks, readiness probes TCP port/file/shell condition, detailed logging and metrics, Observability and controls for end-to-end health section, Modal Sandbox Pricing section with usage-based burst-up)
- modal.com/slack (200, Modal Slack community link)
- modal.com/blog/soc2type2 (referenced from /docs/guide/security; the SOC 2 Type 2 audit announcement blog post)
- trust.modal.com (Modal Security Portal — request-access gate for the SOC 2 Type 2 report)
- github.com/modal-labs (Modal Labs GitHub org, footer of /docs/guide/security)
- x.com/modal (@modal X handle, linked from /company and /docs/guide/security footers)
- linkedin.com/company/modal-labs (Modal Labs LinkedIn page, linked from /company and /docs/guide/security footers)

## Key facts (canonical)

- **Legal entity:** Modal Labs, Inc.
- **Founders:** Erik Bernhardsson, Akshat Bubna (verified live on modal.com/company founder image + alt text)
- **CEO:** Erik Bernhardsson (per live /company page where he is identified as co-founder and is the public CEO face)
- **Funding:** $466M+ raised; investors include General Catalyst, Redpoint Ventures, Lux Capital, Amplify Partners, Creandum
- **HQ:** 233 Spring St, Floor 11, New York City (multi-office: NYC + Stockholm + SF)
- **Products:** Inference, Sandboxes (highlighted product in /products), Training, Notebooks, Batch, Core Platform
- **Compliance:** SOC 2 Type 2 (audit completed, report behind trust.modal.com); HIPAA Business Associate Agreement on Enterprise plan; GDPR + UK GDPR DPA with SCCs; PCI section; Bug Bounty program; Vulnerability remediation with Critical 24h / High 1 week / Medium 1 month / Low 3 month SLAs; Shared-responsibility model
- **Modal Sandboxes specific:** automated health checks, readiness probes (TCP port / file / shell condition), Memory Snapshots, Filesystem and Directory Snapshots, Images, Volumes v1 (out-of-HIPAA scope), HIPAA-Compliant Volumes v2, Sandbox dashboard observability
- **Publicly published contact channels:** support@modal.com (general), security@modal.com (Enterprise / HIPAA BAA / SOC 2 / PCI / questions)

## Non-overlap vs E2B 751 + Daytona 752

- E2B 751 owns the **full-computer Enterprise AI Agent Cloud lane** (sandbox image, credential/egress, replay, teardown, AWS/GCP/Azure/VPC, hello@e2b.dev, FOUNDRYLABS INC Delaware, Vasek Mlejnsky CEO, 166 Geary St SF, $11.5M seed)
- Daytona 752 owns the **stateful execution + persistent volumes + customer-managed compute + multi-OS computer-use lane** (sub-90ms sandbox creation, process/file/Git/LSP APIs, snapshots, volumes, Linux/Windows/macOS computer use, SSH/VS Code Browser/Web Terminal access, FORM:https://www.daytona.io/contact, Ivan Burazin CEO, Vedran Jukić CTO, Goran Draganić Chief Architect)
- **Modal 753 owns the serverless, scale-to-zero, Python-decorator + modal run CLI, CPU/GPU, Inference endpoints + Training jobs, HIPAA-compliant Volumes v2, Memory Snapshots + Filesystem Snapshots, automated health checks + readiness probes, $466M-raised / SOC 2 Type 2 / HIPAA BAA / GDPR DPA / UK GDPR / PCI enterprise posture wedge**

## Status

No email sent, no form submitted, no delivery, no reply, no payment, no revenue claimed.