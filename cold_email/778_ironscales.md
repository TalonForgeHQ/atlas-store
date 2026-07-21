# IRONSCALES — procurement evidence package (Lead 778)

**Verification date:** 2026-07-21  
**Canonical website:** https://ironscales.com/  
**Commercial route:** FORM:https://secure.ironscales.com/demo  
**Cohort:** `ai_email_security_agents` — sibling #2/5 after Abnormal Security 776 OPENER  
**Route status:** form route verified by first-party redirect from `https://ironscales.com/demo`; no form submission performed.

## First-party facts recovered

- IRONSCALES describes itself as an AI-driven, self-learning email-security platform for advanced phishing, business-email-compromise, and account-takeover threats.
- The platform page names a mailbox-level, API-driven email-security approach with Adaptive AI, human insights, automated incident response/remediation, and integrations for Microsoft 365, Microsoft Teams, and Google Workspace.
- The first-party About page says the platform installs in minutes, works alongside existing tools/processes, and had reached **17,000 customers** in its 2025 milestone.
- The first-party About page describes a 2026 product release with three agentic capabilities: **Red-Teaming Agent**, **Phishing SOC Agent**, and **Phishing Simulation Agent**.
- The first-party About page describes the 2014 origin as an incubation from a cybersecurity venture program and alumni of an Israeli Defense Forces intelligence-technology unit. No unsupported founder list is inferred from that language.
- The first-party Leadership page identifies **Eyal Benishti, CEO**, and states: “Eyal Benishti is the CEO and Founder of IRONSCALES.”
- The first-party demo route resolves to `https://secure.ironscales.com/demo` and presents “Preemptive Security for M365 & GWS,” Adaptive AI, advanced phishing/BEC protection, Agentic SOC Automation, deepfake threat protection, and a personalized-demo request.
- The first-party contact route is `https://ironscales.com/contact-us`; it is preserved as a company contact surface, not substituted for the commercial demo route.

## Why this is a useful sibling

Abnormal 776 opened the cohort with a behavioral-AI foundation-model and Trust-Center attestation wedge. IRONSCALES adds a different procurement story: mailbox-level API deployment without MX changes, Adaptive AI combined with a human-insights feedback loop, and a current three-agent surface spanning red-team research, Phishing-SOC investigation, and phishing simulation. The evidence question is therefore not “does another vendor block phishing?” but whether the customer can prove the full chain from mailbox signal → Adaptive-AI decision → human/agent investigation → remediation → simulation/training feedback → export, retention, and deletion.

Planned comparison siblings remain Proofpoint (mature incumbent / SEG and compliance packet), Mimecast (gateway + archiving / EMEA incumbent), Microsoft Defender for Office 365 (native-tenant control plane), and Avanan/Check Point or another challenger (cloud-native behavioral-AI comparison). IRONSCALES should not be positioned as identical to those products.

## Five evidence joins for the audit

1. **Mailbox-level Adaptive AI provenance:** message or identity signal → mailbox-level feature set → model/version → decision reason → confidence → tenant boundary → analyst or admin-visible explanation.
2. **Agentic SOC human oversight:** Red-Teaming Agent or Phishing SOC Agent run → evidence gathered → verdict → recommended action → approver identity/role/timestamp → remediation result → rollback target and retention.
3. **Human-insights feedback loop:** analyst-confirmed phishing → shared intelligence or self-learning update → propagation scope → customer opt-out/tenant isolation → model-change or rule-change receipt.
4. **Simulation and deepfake coverage:** Phishing Simulation Agent or deepfake-protection decision → target/segment → generated or detected artifact → consent/approval → employee outcome → follow-up training evidence.
5. **Enterprise export and lifecycle:** Detection/incident record → CSV/JSONL/API export → retention window → legal hold (if any) → tenant deletion request → deletion-cascade receipt; pair with sub-processor DPA and responsible-disclosure evidence.

## Verification boundary

This file records facts found on current first-party pages plus buyer questions that remain to be answered. A named capability is not treated as proof that IRONSCALES already publishes every requested export, model card, retention receipt, or EU AI Act control. No email, form submission, delivery, payment, or revenue is claimed. SMTP remains gated.
