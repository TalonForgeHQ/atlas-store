# Lead 857 — Fiddler AI (fiddler.ai) — `ai_observability_eval` CLOSER #5/5

## First-party evidence

- **Company/site:** Fiddler AI, `https://www.fiddler.ai/`.
- **Founder proof:** `https://www.fiddler.ai/about` exposes an `Organization` JSON-LD payload with `founder` records: Krishna Gade (`jobTitle: Founder and CEO`, alumniOf Facebook/Twitter/Pinterest/Microsoft, LinkedIn sameAs) and Amit Paka (`jobTitle: Founder and COO`, alumniOf Samsung/PayPal/Microsoft/UC Berkeley). The rendered About page repeats “Krishna Gade Founder and CEO” and “Amit Paka Founder and COO.”
- **Product proof:** first-party homepage/about copy describes Fiddler AI as a control plane for AI agents; `/agentic-observability` exposes agentic observability, LLM-application, and ML-model monitoring surfaces.
- **Commercial route:** `https://www.fiddler.ai/contact-sales` is the sanctioned first-party Contact Sales route. Its rendered source exposes `MktoForms2.loadForm("//lp.fiddler.ai", "513-RPQ-699", 1007, ...)`, i.e. Marketo workspace `513-RPQ-699`, form ID `1007`.
- **Security proof:** `https://www.fiddler.ai/security` states that Fiddler’s SOC 2 Type II report covers Security, Confidentiality, and Availability and is audited annually; the report is available upon request under NDA. Preserve this exact “report available upon request” wording rather than claiming a public certificate.

## Verification notes

- Live first-party fetch on 2026-07-21 with `curl -sL --max-time 15 -A "Mozilla/5.0"` returned the About JSON-LD founder records, the product copy, the Contact Sales Marketo form configuration, and the Security SOC 2 Type II statement.
- `mailto:security@fiddler.ai` appears on `/contact-sales` only as a security-disclosure route. It is not a commercial inbox and is deliberately not used in the lead row.
- This is a real company, real website, and real founder proof. No form was submitted and no payment or revenue is claimed.

## Non-overlapping cohort wedge

Fiddler AI is the **CLOSER #5/5** in `ai_observability_eval`, after Arize AI 835 (observability + eval/drift), Langfuse 841 (OSS-first tracing/evaluation with ClickHouse-affiliated EU parent), and the existing queued sibling set Galileo 843 + Humanloop 844. Fiddler’s distinct lane is the **enterprise AI control plane**: observability plus guardrails plus governance for agentic systems, including the policy/evidence seam between runtime decisions and responsible-AI controls. This closes the cohort without duplicating Arize’s observability/eval cloud, Langfuse’s OSS-first EU/ClickHouse lane, Galileo’s evaluation/quality lane, or Humanloop’s prompt/application-development lane.

## Suggested offer

$500 / 48-hour evidence-gap map, or $497/month for a quarterly refresh. SMTP is gated; route only through Fiddler’s first-party contact-sales form if a later send is explicitly authorized.
