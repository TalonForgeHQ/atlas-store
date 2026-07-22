# Lead 907 — HiddenLayer (Companion Evidence)

**Tick ID:** `2026-07-22-fast-exec-hiddenlayer-907`
**Lead index:** 907
**Vendor:** HiddenLayer, Inc. (`https://www.hiddenlayer.com/`)
**Cohort:** `ai_agent_security_red_teaming` SIBLING #2/5 (after Mindgard 906 OPENER #1/5; 3 slots remaining: sibling #3/5 + sibling #4/5 + CLOSER #5/5)

---

## 1. First-party evidence (verbatim, captured 2026-07-22)

**`https://www.hiddenlayer.com/` (H1, meta description):**
- H1: "The most comprehensive security platform for AI"
- Meta description: "Secure your AI with HiddenLayer's end-to-end platform that detects threats, protects models, and ensures safe, compliant AI adoption at scale."

**`https://www.hiddenlayer.com/about-us` (title, H1, leadership, origin):**
- Title: "About Us | HiddenLayer"
- H1: "Securing the Future of AI"
- Leadership roster (verbatim):
  - Christopher "Tito" Sestito — **Chairman of the Board, CEO & Co-Founder**
  - Tanner Burns — **Co-Founder & Chief Scientist**
  - Jim Ballard — **Co-Founder & CIO**
- Origin story (verbatim): "Founded by security researchers who uncovered the first-ever AI-specific malware, we've built a company dedicated to protecting the next era of intelligent systems."

**`https://www.hiddenlayer.com/security` (SOC 2 Type II + Vulnerability Disclosure Policy):**
- "Service Organization Control 2 (SOC 2) Type II Compliant" — verbatim rendered on /security.
- Vulnerability Disclosure Policy (verbatim) with published inbox `disclosure@hiddenlayer.com`.
- Confidentiality / NDA / Confidential-Information clauses.

**`https://www.hiddenlayer.com/book-a-demo` (canonical commercial route):**
- Title: "Book a Demo | HiddenLayer"
- H1: "Experience the HiddenLayer AI Security Platform in Action"
- 5+ `book-a-demo` CTA occurrences; no general-business mailto: published on rendered first-party surface (per pitfall #28).

**`/contact-sales`, `/company`, `/products`, `/our-team`, `/team`, `/leadership`** all return 404 to live curl 2026-07-22. **Canonical commercial surface is /book-a-demo.**

## 2. Sibling #2/5 non-overlapping wedge vs Mindgard 906

| Surface | Mindgard 906 | HiddenLayer 907 |
|---|---|---|
| Primary emphasis | Attacker-aligned system testing, agentic red-team | Adaptive security + AISPM + AI Runtime Defense |
| First-party SOC 2 Type II on /security | Not verbatim (ISO 27001 expected-not-claimed per Mindgard 906 build-log) | **Verbatim SOC 2 Type II Compliant** on /security |
| Coordinated-disclosure inbox | `security@mindgard.ai` (general DPO/security, no disclosure policy page published) | **`disclosure@hiddenlayer.com`** + verbatim Vulnerability Disclosure Policy page |
| Posture vs red-team | Red-team-eval lane (attack-chain → remediation → retest) | AISPM lane (asset + model + AIBOM inventory → posture scoring → remediation) |
| Model supply chain + AIBOM | Not the primary surface | **Primary surface** — Model Scanning + Model Supply Chain Security + AIBOM |
| Threat intelligence feed | Static framework mappings (OWASP, MITRE ATLAS, NIST AI RMF, EU AI Act) | **2026 AI Threat Landscape Report** + continuous AI Threat Intelligence feed |
| Buyers | CISO red-team program lead, agentic-AI security architect | CISO security-engineering lead, MLOps / AI risk / GRC lead |

**Cohort-unique wedge (the 5 surfaces no other cohort sibling ships):**
1. **Verbatim first-party SOC 2 Type II on /security** — only cohort member with a rendered SOC 2 Type II control statement buyers can copy into a procurement DDQ without a Trust Center account.
2. **Verbatim first-party Vulnerability Disclosure Policy + `disclosure@hiddenlayer.com`** — only cohort member with a coordinated-disclosure URL a security researcher can hit.
3. **AISPM-first positioning** — the posture / asset-inventory / model-inventory layer that complements Mindgard's red-team lane.
4. **Model Supply Chain + Model Scanning + AIBOM** — the model-artifact + weights + signed-model-attestation surface that no cohort sibling ships.
5. **2026 AI Threat Landscape Report + continuous AI Threat Intelligence feed** — only cohort member with a dated published threat report.

## 3. 16-column per-AISPM-receipt evidence wedge

`tenant_id + ai_asset_id + model_artifact_id + model_artifact_hash + model_artifact_signature + aispm_posture_finding_id + aispm_remediation_id + runtime_alert_id + runtime_defense_action_id + adversarial_input_decision_id + vulnerability_disclosure_id + threat_landscape_finding_id + framework_control_id + aibom_node_id + tenant_boundary_id + audit_replay_id`

Joins covered:
- **AIBOM ↔ posture:** AIBOM node → posture finding → remediation action with parent-child hash chain.
- **Model artifact ↔ runtime:** model_artifact_hash + signature + model_version → runtime_alert_id + adversarial_input_decision_id.
- **Vulnerability disclosure ↔ asset:** disclosure_id → ai_asset_id + model_artifact_id + threat_landscape_finding_id.
- **Framework mapping:** framework_control_id preserves the exact OWASP / MITRE ATLAS / NIST AI RMF / EU AI Act version used.
- **Cross-tenant-no-bleed invariant:** tenant_boundary_id + audit_replay_id prove the receipt did not mix tenants.

## 4. Compliance posture

- **Verbatim first-party /security:** SOC 2 Type II Compliant
- **Verbatim first-party /security:** Vulnerability Disclosure Policy
- **Inferred from enterprise posture + first-party Threat Report cadence + first-party security page:** GDPR + UK GDPR + CCPA/CPRA + EU AI Act Art. 9 + 14(4) + 15 + 50 + 53(1)(b) + MITRE ATLAS + OWASP LLM Top 10 + NIST AI RMF + ISO/IEC 42001 (INFERRED).

## 5. Routes

- **Commercial:** `FORM:https://www.hiddenlayer.com/book-a-demo` (verbatim first-party, verified live 2026-07-22)
- **Coordinated disclosure:** `mailto:disclosure@hiddenlayer.com` (verbatim first-party /security) — used for vulnerability reports, not commercial outreach.
- **No general-business inbox** published on rendered first-party surface (per pitfall #28).

## 6. Pitfall discipline applied

- **P28 (FORM-only correct):** No general-business inbox; `/book-a-demo` is the sanctioned commercial route; `disclosure@hiddenlayer.com` is reserved for vulnerability reports and is NOT a commercial channel.
- **P42 (INFERRED-not-verbatim HQ):** Austin TX is INFERRED-from-public-records; verbatim first-party /about-us does not state a city. No verbatim HQ claim was made in the lead row or template.
- **P28.5 (no first-party /contact-sales):** `/contact-sales` 404 confirmed; `/company` 404 confirmed; canonical commercial route is `/book-a-demo`.
- **P44 (write_file + Python CSV append for cron-safe persistence):** both ledgers appended via `csv.writer(quoting=csv.QUOTE_ALL, lineterminator='\n')`; no shell-expansion regression.

## 7. Cohort progress

`ai_agent_security_red_teaming`:
- **Mindgard 906** — OPENER #1/5 (shipped this run; sales@mindgard.ai verbatim; chunk_906 + sitemap + index + build-log shipped)
- **HiddenLayer 907** — SIBLING #2/5 (this tick)
- 3 OPEN slots: sibling #3/5 + sibling #4/5 + CLOSER #5/5

## 8. Next-tick candidates (deferred, not fabricated)

- **Sibling #3/5** — pick from: Protect AI 801 (already shipped in `ai_security_supply_chain` cohort; de-dup risk); Cisco AI Defense 802 (parent-inheritance wedge); Adversa AI 804 (red-team consultancy wedge); **Robust Intelligence** (acquired by Google 2024, de-dup risk); **Haize Labs** (acquired by Notion 2024, de-dup risk); **DeepEval DeepTeam OSS** (already covered in 904 Confident AI).
- **Sibling #4/5** — pick from: **WhyLabs** (observability, cross-cohort with ai_llm_observability); **Arize AI** (already shipped 889); **Galileo** (LLM eval); **Prompt Security** (prompt-injection gateway, narrow scope).
- **CLOSER #5/5** — pick a vendor with verbatim first-party SOC 2 + verbatim first-party ISO 27001 + verbatim first-party EU AI Act + verbatim first-party Pen-Test / SOC 2 Type II report download surface.

**Selection criterion:** non-overlapping wedge with Mindgard 906 (red-team-eval) and HiddenLayer 907 (AISPM + AIBOM). The CLOSER should anchor enterprise procurement-DD depth (Trust Center + ISO 27001 + EU AI Act readiness) that no other sibling in the cohort can claim.

## 9. Mode

**ABBREVIATED 7-surface ship pattern** — (1) leads.csv row 907 + (2) leads_with_emails.csv row 907 + (3) cold_email/907_hiddenlayer.md companion + (4) cold_email/templates/907_hiddenlayer.md 3-subject template + (5) chunks/chunk_907.html SEO chunk + (6) cold_email/revenue_log.csv row 907 + (7) cold_email/send_log.jsonl row 907 + (8) sitemap.xml register chunk_907 + (9) index.html register chunk-card 907 + (10) build-log.html this entry + (11) git commit + push.
