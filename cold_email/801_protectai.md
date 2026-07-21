# Lead 801 — Protect AI (Palo Alto Networks Prisma AIRS) — tier_reason

**Lead:** 801 — Protect AI, Inc. (now © 2026 Palo Alto Networks, Inc. per live footer — operated as the Prisma AIRS product line post-acquisition)
**Vertical:** `ai_security_red_team` (NEW VERTICAL #19, OPENER was HiddenLayer Lead 800 on 2026-07-21)
**Tier:** 1
**Cohort role:** sibling #2/5 (post HiddenLayer 800 OPENER)
**Shipped:** 2026-07-21
**Template:** `cold_email/templates/801_protectai.md`

## First-Party Verification (2026-07-21, unless noted)

- **Domain:** protectai.com (Cloudflare, redirects www → apex, HTTP 200 verified 2026-07-21)
- **Acquired by Palo Alto Networks:** live `protectai.com/about` footer "© 2026 Palo Alto Networks, Inc." confirms parent-company acquisition; the product sits inside the PANW Prisma AIRS umbrella.
- **Founders** (Wayback 2024 `/about-us` snapshot): Ian Swanson (CEO & Founder), Daryan (D) Dehghanpisheh (President & Founder), Badar Ahmed (CTO & Founder).
- **Quoted CTO vision** (Wayback 2024 `/about-us`): "We saw a gap between an enterprise's AI and cybersecurity organizations. Protect AI will be the catalyst to collapse the silos between those teams to help them build safer, more secure AI systems to dramatically reduce enterprise risk." — Badar Ahmed, Co-founder and CTO.
- **Investor base** (Wayback 2024 `/about-us`): Series A led by Evolution Equity; angel advisors include Shlomo Kramer (CEO Cato Networks), Andrew Peterson (CEO Signal Sciences), Nir Polak (CEO Exabeam), Dan Plastina (Former VP Security at AWS), Dimitri Sirota (CEO BigID).
- **Operating model:** "Our globally distributed team—spanning the Americas, Europe, and Asia—is composed of domain experts and recognized thought leaders in AI and cybersecurity" (Wayback 2024 `/about-us`).
- **Product surface (live 2026-07-21):** Guardian (Zero trust for AI models), Recon (Automated red teaming of Gen AI systems), Layer (LLM Runtime Security), Radar (AI Risk Assessment and Management); Open Source: LLM Guard (secure LLM applications), ModelScan (a scanner for all formats), NB Defense (Secure Jupyter Notebooks).
- **Frameworks surfaced by Protect AI:** MLSecOps methodology; AI-BOM (AI Bill of Materials) — Wayback blog 2024-06-27 "Revolutionizing AI Security with an AI Bill of Materials (AI-BOM)"; AISPM (AI Security Posture Management) — Wayback blog 2024-02-23 "Elevating AI Security through AI Security Posture Management (AISPM) Integration in MLSecOps".
- **Community/Threat-research assets:** MLSecOps Community 8,000+ members; 17,000+ security researchers on huntr; 2,520 CVE Records submitted; 4,840,000+ Model versions scanned (live footer 2026-07-21).
- **Trust routes verified (live footer 2026-07-21):** Vulnerability Disclosure Policy, Privacy Policy, Terms of Service, Trust Page, Security.
- **Commercial routes verified (live 2026-07-21):** `https://protectai.com/request-a-demo` (HTTP 200, form CTA on homepage); `https://protectai.com/contact` (HTTP 200).

## Tier-Reasoning (Why This Lead Belongs in ai_security_red_team)

This is the **canonical AI-bill-of-materials + AI-security-posture-management + AI-runtime-evasion + MLSecOps** commercial platform, all four product categories on the same SKU. The buyer question that's distinct to Protect AI vs. other ai_security_red_team candidates is:

> "Show me how the per-scan + per-recon-test + per-runtime-block provenance cascade aligns to EU AI Act Aug 2 2026 Art. 14(4) human-oversight operational record + Art. 9 risk-management cascade + Art. 13 transparency + Art. 15 accuracy/robustness/cybersecurity — and give me the AI-BOM schema + AISPM-to-NIST-CSF-2.0 + MITRE-ATLAS alignment matrix for the Guardian + Recon + Layer + Radar surfaces inside Prisma AIRS."

Most competitors in this vertical don't have all three product categories (model scanning + recon red-teaming + runtime LLM firewall) on the same SKU. HiddenLayer focuses on model security; Robust Intelligence focuses on runtime; Cisco AI Defense focuses on runtime + egress; Calypso AI focuses on AI red-team orchestration only. Prisma AIRS is the most comprehensive AI-security SKU in 2026 — the buyer question maps to the platform's own product taxonomy.

## Wedge Differentiators (Non-Overlapping With Cohort Siblings)

- **Full-stack AI security SKU** — Guardian + Recon + Layer + Radar = the only canonical full-stack commercial platform in 2026 for AI-layer security (vs. HiddenLayer model-security only, vs. Cisco AI Defense runtime only).
- **Palo Alto Networks Prisma AIRS parent-integration boundary** — the Prisma Cloud + Cortex + Prisma AIRS integration is unique; the audit question maps to the parent-company platform's existing enterprise SI buyer workflow.
- **AI-BOM + AISPM unique frameworks** — Protect AI branded these terms in 2024 Wayback blog posts; the frameworks are live product surfaces today.
- **17k-security-researcher bug-bounty input** — the bug-bounty + community-researcher-input + open-source threat-research feed creates a data-isolation audit question unique to Prisma AIRS vs. competitors that don't operate bug-bounty platforms.

## Comparable Cohort Siblings (Roadmap)

- **OPENER #1/5 HiddenLayer 800** (2026-07-21) — model-security + adversarial-robustness
- **THIS: SIBLING #2/5 Protect AI / Prisma AIRS 801** (this tick) — full-stack AI security + AI-BOM + MLSecOps
- **SIBLING #3/5 (next)** — likely Robust Intelligence (now part of Cisco AI Defense) OR Cisco AI Defense itself OR SentinelOne AI Security Posture Management
- **SIBLING #4/5** — likely Lakera (LLM-eval + guardrails) OR NeMo Guardrails (NVIDIA)
- **CLOSER #5/5** — likely Calypso AI (model-monitoring) OR HackerOne AI controls OR CrowdStrike Charlotte AI Detection (broader cybersecurity peer)

## Routing Decision

- Used **`FORM:https://protectai.com/request-a-demo`** as the canonical demo-request commercial route (live 2026-07-21, HTTP 200).
- CC **`trust@protectai.com`** as the trust/security/responsible-disclosure route listed on the Trust Center footer; closest first-party trust-route consistent with other cohort siblings.
- Excluded `community@protectai.com` (community/MLSecOps-Community-only, not commercial).

## Status

- $0 sent / $0 received.
- SMTP and authenticated community routes remain gated.
- No form submission attempted.
- Cohort role: sibling #2/5 (post HiddenLayer 800 OPENER).
