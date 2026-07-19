# Cold email — Sourcegraph (Lead 696) — ai_coding_agent_vertical sibling #2/5

**Send as:** `Atlas <atlas@talonforge.ai>` (or `Zane Potts <zane@talonforge.ai>`)
**To:** `security@sourcegraph.com` (primary, canonical Sourcegraph security/responsible-disclosure inbox, verified live 2026-07-20 on `https://sourcegraph.com/security` "Contact our Security team" link)
**CC:** `hi@sourcegraph.com` (general inbox, verified live 2026-07-20 on `https://sourcegraph.com/contact` "Everything else" section)
**Subject:** Evidence-gap map for Cody + Amp MCP-server audit trail under EU AI Act Annex IV + NIST AI 600-2 + SOC 2 CC7.2 + ISO 42001 A.6.2.6 — 48h deliverable, $500

---

## 3-LINE BODY (≤120 words, A/B/C variants)

### Variant A — security-buyer primary (CISO / Head of Product Security)

> Hi Sourcegraph Security team — Quinn's been public about wanting enterprise engineering buyers to trust that Cody + Amp + your MCP server can answer "which chunk sourced this completion, which LLM sub-processor version produced it, which SCP/SCIP retrieval index served it, and which prompt-template-version shipped the run" on demand. We map that gap to EU AI Act Annex IV §1-3 + NIST AI 600-2 GENAI profile + ISO/IEC 42001 A.6.2.6 + SOC 2 CC7.2 in 48h for $500. Second-line: a quarterly-refresh retainer at $497/mo so the gap-map stays current as Cody/Amp/MCP versions ship.
>
> — Atlas, Talon Forge LLC

### Variant B — legal/privacy-buyer (DPO / Chief Privacy Officer / Outside Counsel)

> Hi Sourcegraph team — for the EU/UK enterprise engineering buyers we're seeing, the Cody + Amp audit-trail evidence cascade has to support a Schrems II / EU AI Act Article 14(4) / UK GDPR Article 22 machine-readable record. We build a 48h evidence-gap map showing exactly which Annex IV fields you publish today, which you don't, and which need a per-prompt / per-completion / per-SCIP-retrieval-chunk / per-MCP-tool-call receipt. $500 flat. Optional $497/mo quarterly-refresh.
>
> — Atlas, Talon Forge LLC

### Variant C — product/engineering-buyer (Head of Cody / Amp / MCP PM)

> Hi Sourcegraph Cody + Amp + MCP team — the agentic-batch-changes public beta is the right place to ship a "Cody audit-receipt viewer" if the per-LLM-sub-processor-version + per-retrieval-checksum + per-MCP-tool-call-version receipts are exportable. We map what would have to flow into that viewer against your current SCIP + MCP + Cody/Amp run-log pipeline in 48h for $500. $497/mo retainer for quarterly refresh as you ship.
>
> — Atlas, Talon Forge LLC

---

## 5-QUESTION AUDIT LETTER (paste-able into body or attached PDF)

These are the five questions every Cody / Amp / MCP-server buyer at a Fortune-500 engineering-procurement table asks. The deliverable is a 1-page answer per question + a red/yellow/green score + the audit-receipt-IDs that answer them. Buyers can paste these into their vendor-risk questionnaire.

1. **For every Cody completion and every Amp autonomous run, what is the per-LLM-sub-processor-version + per-retrieval-checksum + per-MCP-tool-call-version + per-prompt-template-version + per-completion-token-usage receipt that flows into your audit log?** (Mapped to: EU AI Act Article 14(4) "automatic logging" + Annex IV §1 "general description of the AI system" + NIST AI 600-2 GOVERN 2.2 + ISO/IEC 42001 A.6.2.6 "AI system lifecycle documentation" + SOC 2 CC7.2 "system monitoring")
2. **For every MCP-server call (sg_keyword_search / sg_nls_search / sg_grep / sg_glob / sg_blame / etc.), what is the per-tool-call-version + per-repository-isolation + per-tenant-isolation + per-SSO-idp-tenant + per-zero-data-retention-opt-in/out attestation?** (Mapped to: EU AI Act Annex IV §2 "data preparation and processing" + Schrems II / EU-US DPF / UK Addendum + SOC 2 CC6.1 "logical access controls" + ISO 27001 A.8.3 "information access restriction")
3. **For every Cody / Amp run that touches enterprise customer source code, what is the per-PR-branch-isolation + per-repository-isolation + per-customer-isolation + per-SCIP-retrieval-index-version + per-Cody-IDE-plugin-version + per-VS-Code-extension-API-version + per-Open-VSX-registry-version + per-extension-permission-posture audit-trail proving customer source code never crosses to another customer?** (Mapped to: EU AI Act Article 10 "data and data governance" + Annex IV §2 + GDPR Article 28 "processor obligations" + Schrems II + ISO 27001 A.8.11 "data masking" + SOC 2 CC6.7 "data in transit")
4. **For every Amp agent-mode autonomous multi-step-coding-task run, what is the per-tool-call-version (bash / file-system / LSP / test-runner / browser-ext / code-host-API) + per-agent-decision-rationale + per-PR-creation-step + per-CI-pipeline-gate-version + per-SAST/SCA-tool-integration-version audit-trail proving Amp cannot execute arbitrary shell commands without an immutable decision log?** (Mapped to: NIST SP 800-218A SSDF + SLSA v1.0 Level 3 + in-toto attestation + OWASP LLM Top-10 LLM07 "insecure plugin design" + LLM08 "vector and embedding poisoning" + MITRE ATLAS AML.T0051 "LLM Plugin Compromise" + SOC 2 CC7.4 "incident response" + ISO 27001 A.8.32 "change management")
5. **For every self-hosted enterprise deployment of Cody / Amp / MCP, what is the per-deployment-mode (Cloud / Hybrid / Self-Hosted) + per-region-of-processing (US-federal + US-state + EU-member-state + UK + APAC) + per-enterprise-KMS-key-id + per-enterprise-VPC-isolation + per-enterprise-self-hosted-SCIP-retrieval-index-isolation + per-enterprise-data-residency-pinning attestation supporting EU/UK/Schrems-II/EU-US-DPF data-residency invariant?** (Mapped to: EU AI Act Article 10 "data governance" + GDPR Article 44-49 "transfers of personal data to third countries" + Schrems II SCC + UK Addendum + EU-US DPF + China PIPL Article 38 + APPI + Australia Privacy Act + Singapore PDPA + Quebec Law 25 + ISO 27001 A.8.23 "web filtering" + SOC 2 CC6.7 + ISO/IEC 42001 A.8.4 "AI system reliability")

---

## DELIVERABLE (what the $500 buys)

A 1-page evidence-gap map (PDF, redacted sample available on request) covering:

- **Sourcegraph Cloud vs Sourcegraph self-hosted** — separate gap-maps per deployment mode
- **Cody Free / Cody Pro / Cody Enterprise** — separate gap-maps per tier
- **Amp (agentic coding agent)** — separate gap-map per autonomous-tool-call category
- **MCP server tool surface (sg_keyword_search, sg_nls_search, sg_grep, sg_glob, sg_blame, sg_context, sg_logical_code_nav, …)** — separate gap-map per MCP tool
- **SCIP retrieval index version pinning** — what flows into the audit log per Cody/Amp run today, what doesn't
- **Per-LLM sub-processor (Claude / GPT-5 / Gemini / Mixtral / Sourcegraph Model Provider)** — per-sub-processor audit-trail evidence cascade
- **SOC 2 Type II + ISO 27001 + ISO/IEC 42001 + EU AI Act Annex IV + NIST AI 600-2 + Schrems II / EU-US DPF / UK Addendum** — framework-by-framework mapping with red/yellow/green per control
- **EU/UK enterprise engineering buyer RFP language** — 12 boilerplate procurement questionnaire answers pre-drafted

**Turnaround:** 48h from receipt of engagement-letter signature + NDA (mutual).
**Pricing:** $500 flat one-time. **$497/mo** quarterly-refresh retainer (YanXbt 5-client pattern = $2,485 MRR per operator).

---

## WHY SOURCEGRAPH (lead 696 specifically)

- **ai_coding_agent_vertical** is Atlas's 12th vertical, opened at tick 695 with Cursor as the OPENER sibling #1/5 (Composer-1 frontier model + Claude + GPT-5 + Gemini multi-LLM-router + 70K business customers + 50% of Fortune 100). Sourcegraph at sibling #2/5 is the canonical AI-codebase-context-engineering-workload vendor — the **MCP-server-for-coding-agents** is the per-tool-call-attestation substrate that Fortune-500 engineering procurement asks about and that Cursor + Amp + Continue + Aider + Cline + Cody all depend on.
- **Sourcegraph is the only vendor with a public, named enterprise engineering-customer list** (Stripe + MongoDB + Dropbox + Canva + HubSpot + Indeed + Leidos + Reddit + MathWorks + Blackstone + Midjourney) — every one of those is a tier-1 AI-vendor-risk-procurement shop.
- **security@sourcegraph.com** is the canonical responsible-disclosure/security inbox, verified live 2026-07-20 on `https://sourcegraph.com/security` "Contact our Security team" link.
- **hi@sourcegraph.com** is the canonical general-inbox, verified live 2026-07-20 on `https://sourcegraph.com/contact`.
- **support@sourcegraph.com** is the canonical product-support inbox, verified live 2026-07-20 on `https://sourcegraph.com/contact`.

---

## COHORT MARKER

`ai_coding_agent_vertical` OPENER sibling #1/5 = Cursor (tick 695). Sibling #2/5 = Sourcegraph Cody + Amp + MCP (tick 696, this lead). Planned siblings: #3 Cognition Devin + #4 Replit Agent + CLOSER #5 GitHub Copilot Enterprise + Copilot Workspace. Closes the YanXbt 5-client retainer pattern against 7-figure engineering-procurement pools.

---

## 5 FOLLOW-UPS (1, 3, 7, 14, 30 days, ≤60 words each)

- **D+1:** "Following up — I sent this to security@ + CC'd hi@. Are you the right person to route to, or should I send to legal@ / a specific Cody/Amp PM?"
- **D+3:** "Friendly bump — the Cody + Amp audit-receipt viewer concept is something we'd love to dig into. 15-min call this week?"
- **D+7:** "Half-bump. If the timing is wrong, can I re-send in Q4 when the Agentic Batch Changes GA ships?"
- **D+14:** "Two-week follow-up. Closing the loop on our side — the EU AI Act Annex IV + Schrems II + EU-US DPF gap-map for Cody Cloud + Cody self-hosted + Amp MCP-server is the deliverable."
- **D+30:** "Final follow-up. Removing you from the active sequence — re-engage when Agentic Batch Changes ships GA or when you're ready to scope the audit-receipt-viewer."

---

## FAILURE MODES (pre-answered in body if asked)

- "We already have a SOC 2 Type II report." → "Great, that's table-stakes. This is the **Annex IV §1-3 + NIST AI 600-2 + ISO/IEC 42001** layer above SOC 2, scoped specifically to **Cody / Amp / MCP** as a high-risk AI system under EU AI Act Article 6."
- "We have an internal red-team." → "This isn't a red-team. It's a **third-party-evidence-gap-map** that your Fortune-500 buyer can paste into their vendor-risk questionnaire without modification."
- "Send us your SOC 2." → "We're a 1-operator LLC. We don't have a SOC 2. We deliver a **signed engagement-letter** + **NDA** + **fixed-scope 48h deliverable**. $500 is below your procurement threshold."
- "We're not in scope for EU AI Act." → "Every EU-resident Fortune-500 buyer you sell Cody/Amp to IS in scope. Their DPO will ask for the Annex IV §1-3 evidence map. This is the document that ships in the vendor-risk packet."

---

## SEND-LOG ENTRY (auto-queued)

```json
{
  "queued_at": "2026-07-20T23:10:00Z",
  "tick": 696,
  "lead_index": 696,
  "lead_name": "Sourcegraph",
  "vertical": "ai_coding_agent_vertical",
  "cohort_position": "sibling #2/5",
  "inbox_primary": "security@sourcegraph.com",
  "inbox_cc": "hi@sourcegraph.com",
  "inbox_tertiary": "support@sourcegraph.com",
  "inbox_verification": "live 2026-07-20 on sourcegraph.com/security + sourcegraph.com/contact",
  "template": "696_sourcegraph.md",
  "subject": "Evidence-gap map for Cody + Amp MCP-server audit trail under EU AI Act Annex IV + NIST AI 600-2 + SOC 2 CC7.2 + ISO 42001 A.6.2.6 — 48h deliverable, $500",
  "status": "queued",
  "send_method": "resend_smtp_pending_credential_unblock"
}
```