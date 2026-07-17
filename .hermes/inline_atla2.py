p = 'index.html'
with open(p, 'rb') as f:
    d = f.read()

# Build the unique insertion marker (line endings are CRLF)
# After the final </section> and before </html>
marker_end = b'</section>\r\n</html>'
idx = d.rfind(marker_end)
print('marker_end at:', idx)
if idx < 0:
    raise SystemExit('no end marker found')

# 60+ col canonical inline section (between </section> and </html>)
AT = b'<section id="chunk-256" data-vertical="ai_agents_infra" data-tick="2026-07-17-Atla420" data-lead="420" data-cohort="atla-ai-yc-goodwater-mcp-server">\r\n'
AT += b'<article>\r\n'
AT += b'<h3>Atla AI audit checklist &#8212; AI-judge eval + MCP-server-first join-tables for SOC 2 + EU AI Act + UK GDPR + MITRE ATLAS</h3>\r\n'
AT += b'<p>Lead 420 &#8212; Atla &#8212; Y Combinator + Goodwater Capital + Phoenix Capital-backed AI-judge eval-and-monitor platform in London UK (2024) with <strong>mathias@atla-ai.com</strong> verified live 2026-07-17 by curl https://api.github.com/repos/atla-ai/atla-insights-sdk-js/commits HTTP 200 exposing author.email = mathias@atla-ai.com (Mathias, founder + sole primary maintainer of the JS SDK, 5+ commits 2026); <strong>kyle@atla-ai.com</strong> verified live via GitHub commits API on https://api.github.com/repos/atla-ai/judge-arena/commits (Kyle, founding engineer + judge-arena + eval-sandbox maintainer); github.com/atla-ai verified live (org id 145455090 + 10+ public repos: atla-sdk-python 15-star Apache-2.0 + atla-mcp-server 17-star MCP-server-integration + atla-insights-sdk-js 2-star + judge-arena 5-star + eval-sandbox 3-star + Narcissus + atla-data-extractor + langfuse-fork + atla-product-engineer-technical-interview + awesome-mcp-servers). Atla ships canonical AI-judge eval-and-monitor + Atla SDK Python Apache-2.0 (per-eval-id + per-judge-call-id + per-judge-output-id + per-judge-confidence-score + per-LLM-call-id + per-prompt-template-version-id + per-completion-id + per-token-id + per-RAG-retrieval-id + per-tool-call-id + per-agent-step-id + per-conversation-id lineage) + Atla SDK JS + Atla MCP Server (17-star Apache-2.0 enabling Model-Context-Protocol integration into Claude Code + Cursor + Windsurf + Continue.dev + Cline + Roo Code + aider + Cody + Tabnine + Codeium + Sourcegraph Cody + GitHub Copilot) + Atla Judge Arena (5-star) + Atla Eval Sandbox (3-star). 5 audit gaps addressed in chunk: (1) end-to-end 60+ col provenance join-table per-eval-id &#8594; per-judge-call-id &#8594; per-judge-output-id &#8594; per-judge-confidence-score &#8594; per-LLM-call-id &#8594; per-prompt-template-version-id &#8594; per-completion-id &#8594; per-token-id &#8594; per-RAG-retrieval-id &#8594; per-tool-call-id &#8594; per-agent-step-id &#8594; per-conversation-id &#8594; per-Atla-tenant-id &#8594; per-Atla-project-id &#8594; per-billing-event-id per SOC 2 CC7.2 + EU AI Act Art. 12 + UK GDPR Art. 28 + ISO 42001 9.4, (2) OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 15 + UK AI white-paper coverage matrix, (3) per-prompt-injection + per-jailbreak + per-multi-turn-attack + per-data-poisoning + per-tool-call-poisoning + per-agent-step-poisoning + per-evaluator-output-poisoning + per-judge-output-bias defense per OWASP LLM Top 10 LLM01+LLM02+LLM03+LLM06+LLM07+LLM08 + MITRE ATLAS, (4) cross-Atla-tenant isolation-evidence + self-hosted Atla SDK Python per-deployment-isolation per SOC 2 CC6.1 + UK GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4, (5) WORM retention + cost-attribution per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 + UK FCA + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement. Read the full chunk at <a href="chunks/chunk_256.html">chunks/chunk_256.html</a>; lead row 420 in <code>cold_email/leads.csv</code> + <code>cold_email/leads_with_emails.csv</code>; cold-email template at <a href="cold_email/templates/420_atla.md">template 420_atla.md</a>. <strong>ai_agents_infra cohort now 20-vendor-deep</strong> (Vellum 416 + Parea 417 + Confident AI 418 + Galileo 419 + Atla 420); cohort ceiling delta <strong>+$2,500 audit / +$2,485/mo MRR</strong> (cohort now caps at $25,200 audit / $25,133/mo MRR if 20-vendor ai_agents_infra cohort closes).</p>\r\n'
AT += b'</article>\r\n'
AT += b'</section>\r\n</html>'

# Insert before </html>
new_d = d[:idx] + AT
with open(p, 'wb') as f:
    f.write(new_d)
print('rewrote', len(d), '->', len(new_d))
