# Humanloop 844 — Cold-Email Template (ai_observability_eval CLOSER #5/5)

## Subject-line A/B/C

- **Subject A:** Humanloop's enterprise LLM evals — a 48-hour Art. 26 evidence-gap map
- **Subject B:** Raza — can a reviewer reproduce every prompt, eval, and release decision six months later?
- **Subject C:** Humanloop + Anthropic — pinning enterprise eval and prompt provenance before the next model release

## Five-question audit opener

1. For Humanloop's enterprise evaluation platform, can each eval run be reconstructed from dataset/version → target model/version → prompt template/version → judge model/version → metric/rubric/version → reviewer decision?
2. How do prompt-management deployments pin the exact prompt version, traffic allocation, feedback record, and rollback decision that produced a production response?
3. For LLM observability, can a customer join trace/span IDs to token usage, latency, tool calls, evaluator output, and downstream state changes without cross-tenant leakage?
4. Which controls are shipped versus customer-configured for enterprise SSO/SAML, RBAC, VPC deployment, retention, PII redaction, and exportable audit evidence?
5. Can Humanloop customers export a reproducible evidence bundle for EU AI Act Art. 26 deployer obligations, GDPR Art. 30 processing records, SOC 2 controls, and ISO/IEC 42001 release governance?

## Body

Hi Raza, Jordan, and Peter —

Humanloop is the enterprise-first member of this observability/evaluation cohort: the first-party site positions the product around evaluation, prompt management, and LLM observability, with a workflow for developing, evaluating, and shipping trustworthy LLM-powered apps. That creates a specific procurement question: can the customer prove not only that an answer was monitored, but which prompt, dataset, model, judge, rubric, reviewer, and release gate produced it?

The practical gap is a joined provenance record across three surfaces:

- **Evaluation:** dataset snapshot, eval run, target model, judge model, metric/rubric, score distribution, regression delta, and human label.
- **Prompt operations:** prompt version, deployment label, experiment assignment, feedback/correction, approval, and rollback decision.
- **Production observability:** trace/span, tool call, token/cost, latency, PII-redaction action, retention policy, and downstream state change.

That joined record is the $500/48h evidence-gap map. It gives an enterprise buyer one page showing what Humanloop supplies, what the customer configures, and where the Art. 26 deployer, GDPR Art. 30, SOC 2, and ISO/IEC 42001 responsibilities change at the deployment boundary.

I can deliver the fixed-scope map in 48 hours, or maintain the evidence table quarterly for $497/month as models, prompts, evaluators, and enterprise deployment controls change.

Would a one-page version of the five-question cascade be useful for your enterprise sales or trust review?

— Atlas @ Talon Forge

**Routing:** sanctioned first-party route is https://humanloop.com/demo. No SMTP send or form submission attempted.
