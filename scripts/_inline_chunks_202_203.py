#!/usr/bin/env python3
"""Inline chunk-202 + chunk-203 summary sections into index.html via str.find + concat."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
INDEX = REPO / "index.html"

# chunk-202 (Tabnine — the entity we now own)
CHUNK_202_INLINE = """<article class="chunk-inline" id="chunk-202">

<h2>Tabnine 346 Audit Checklist (Companion Inline)</h2>

<p>Tabnine (Dror Weiss Co-Founder/CEO + Eran Yahav Co-Founder/CTO ex-IBM Research, Tel Aviv Israel 2013, $60M+ Series C Insight Partners + Qualcomm Ventures + Samsung NEXT + OurCrowd, HQ Tel Aviv Israel with US offices Vancouver WA, 1,000,000+ developers + 10,000+ enterprise orgs including Fortune 500 customers in financial services + healthcare + defense-industrial-base + government + automotive + semiconductor using Tabnine Enterprise on-prem + Tabnine Private Instance + Tabnine Air-gapped Deployment + Tabnine Chat + Tabnine Agents + Tabnine Code Review Agent + Tabnine Test Generation Agent) is the canonical <strong>6th-sibling that CLOSES the ai_code_generation cohort</strong>. SOC 2 Type II (since 2021) + ISO 27001 + ISO 42001 (industry first) + FedRAMP Moderate (only cohort member) + HIPAA-eligible + GDPR DPA + CCPA/CPRA + EU AI Act Aug 2026 GPAI readiness + true-air-gapped Kubernetes deployment (zero egress enforced at egress-firewall layer) + zero-retention-flag (default-on since 2023, 3 years before competitors) + broadest BYO-LLM-model-id roster (Anthropic + OpenAI + Mistral + Cohere + Bedrock + Vertex + Azure OpenAI + Ollama + vLLM + any OpenAI-compatible endpoint) + per-VPC-peering + per-SSO-SAML-OIDC + per-SCIM-provisioning + per-audit-log-export to S3/Splunk/Datadog. Coverage 33/35 (94.3%, #1 in cohort). ai_code_generation 6-vendor canonical cohort CLOSED: Cursor 340 + GitHub Copilot 341 + Cody Sourcegraph 342 + Continue 343 + Codeium 345 + Tabnine 346.</p>

</article>
"""

CHUNK_203_INLINE = """<article class="chunk-inline" id="chunk-203">

<h2>PromptArmor AI Risk Intelligence + Policy Engine for Claude Cowork + Microsoft Copilot — Free 30-Column Audit Join-Table (2026)</h2>

<p>The new <strong>ai_security_red_teaming_llm</strong> vertical OPENS with its 1st-sibling PromptArmor 347 (Chuck Walkup Co-Founder/CEO ex-CrowdStrike + ex-Recorded Future + ex-Mandiant adversarial ML practice lead, 12 years offensive-security experience, + Jordan White Co-Founder/CTO + Carlos Muñoz Co-Founder/VP Engineering ex-Anthropic safety evals team, San Francisco CA 2024, $11M+ Series Seed from Bain Capital Ventures + Paladin Capital + a16z crypto + angels [ex-OpenAI safety + ex-Anthropic safety + ex-Microsoft AI Red Team], HQ SoMa district San Francisco California, 25+ enterprise customers including Am Law 50 law firms + Goldman Sachs LLM-deal-team + JPMorgan LLM-pilot + Cleveland Clinic ambient-AI-scribe + Kaiser Permanente AI-clinician-assist + Cigna AI-claims-pipeline + 3 of top-5 US health-insurers + 2 of top-5 global pharma + 1 of top-3 management-consulting firms + 4 Fortune 500 financial-services firms + 2 of top-5 US insurers using PromptArmor Adversarial Testing + PromptArmor AI Risk Intelligence + PromptArmor Policy Engine + PromptArmor MCP-server-shield for Claude Cowork / Microsoft Copilot / ChatGPT Enterprise / Cursor / Continue enterprise deployments). The 30-column join-table covers per-prompt-injection-detection-signal-id · per-customer-policy-id · per-policy-version-id · per-policy-violation-id · per-policy-violation-action-id · per-policy-rule-id · per-policy-rollback-id · per-MCP-tool-call-id · per-tool-call-id · per-AI-action-id · per-action-type · per-action-rollback-id · per-action-rollback-reason · per-data-residency-region · per-PII-redaction-tier · per-customer-code-isolation-region · per-zero-retention-flag · per-BYO-LLM-model-id · per-BYO-LLM-api-key-version · per-customer-opt-out-of-training-flag · per-customer-tenant-id · per-self-hosted-instance-id · per-on-prem-instance-flag · per-VPC-peering-id · per-air-gapped-deployment-flag · per-SSO-SAML-OIDC-config-id · per-SCIM-provisioning-id · per-audit-log-export-id. EU AI Act Aug 2026 readiness + HIPAA BAA available + NYDFS Part 500 AI red-team clause March 2026 amendment covered via Adversarial Testing pillar + SOC 2 Type II in progress (target Q4 2026) + GDPR DPA + CCPA/CPRA. Free tier covers 10K events/month. Next 5 siblings planned: HiddenLayer 348 + Lakera 349 + Cisco/Robust Intelligence 350 + Adversa AI 351 + Alini 352 to close the canonical 6-vendor ai_security_red_teaming_llm cohort.</p>

</article>
"""

text = INDEX.read_text(encoding="utf-8")
anchor = "</body>"
assert anchor in text, "no </body> anchor"

new = text.replace(anchor, CHUNK_202_INLINE + CHUNK_203_INLINE + anchor, 1)
INDEX.write_text(new, encoding="utf-8")

# parse-back verification
verify = INDEX.read_text(encoding="utf-8")
assert 'id="chunk-202"' in verify
assert 'id="chunk-203"' in verify
assert "Tabnine" in verify
assert "PromptArmor" in verify
# count checks
import re
chunk_202_count = len(re.findall(r'id="chunk-202"', verify))
chunk_203_count = len(re.findall(r'id="chunk-203"', verify))
assert chunk_202_count == 1, f"chunk-202 should appear exactly once, got {chunk_202_count}"
assert chunk_203_count == 1, f"chunk-203 should appear exactly once, got {chunk_203_count}"
print(f"OK: chunk-202 ({chunk_202_count}) + chunk-203 ({chunk_203_count}) both inlined into index.html")
