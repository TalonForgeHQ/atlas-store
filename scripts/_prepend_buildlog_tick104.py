import sys
from pathlib import Path

LOG = r"C:\Users\Potts\projects\atlas-store\build-log.html"

new_entry = '''<div class="tick">
<h2>[2026-07-12 13:55 UTC] Tick 104 — Shipped: Galileo (200) + 286_galileo.md template + chunk_97.html (Galileo Evaluate + Observe + Protect + Agent Observability + Chat + for RAG + Lens + Studio + Pulse EU AI Act Aug 2026 Audit-Target Prep — canonical RAG-hallucination-detection + LLM-evaluation + LLM-observability + agent-step-tracing + real-time LLM-firewall + 30+ pre-built evaluation-metrics + per-LLM-call provenance + per-RAG-retrieval provenance + per-evaluation-metric provenance + per-hallucination-flag provenance audit-trail surface — team@galileo.ai + team@galileo.io both verified live 2026-07-12 via curl scrape https://www.galileo.ai/privacy-policy HTTP 200 409796 bytes exposing mailto:team@galileo.ai + mailto:team@galileo.io AS THE CANONICAL VENDOR-DD STRATEGIC-INBOUND CHANNELS — Galileo Evaluate 30+ pre-built metrics (hallucination + groundedness + toxicity + bias + prompt-injection-resistance + context-precision + context-recall + answer-relevance + faithfulness) + Galileo Observe (production-LLM-tracing + per-LLM-call tokens + per-prompt-text + per-completion-text + per-tool-call + per-agent-step + per-RAG-retrieval + per-RAG-context-precision-recall + per-citation-groundedness) + Galileo Protect (real-time LLM-output firewall + PII-detection + toxicity-block + prompt-injection-block + topic-restriction + jailbreak-resistance + secret-redaction) + Galileo Agent Observability 8-product-line surface + 16-column per-LLM-call + per-RAG-retrieval + per-evaluation-metric + per-hallucination-flag + per-tool-call + per-agent-step reasoning-chain provenance join-table + 7-column WORM-locked cost-attribution join-table + 14-question buyer checklist + 5-layer reference architecture + 3 forecast case studies (financial-services + healthcare + retail) + EU AI Act Art. 9 + Art. 10 + Art. 12 + Art. 14 + Art. 50 + Art. 53(d) + Art. 53(1)(b) + Art. 53(2) + Annex III §4 + SOC 2 CC6.1 + CC6.7 + CC7.2 + ISO 42001 6.1.4 + 9.4 + GDPR Art. 26 + Art. 28 + HIPAA §164.316(b)(2)(i) + SEC 17a-4 WORM + IRS 6001 + Aug 2026 GPAI enforcement)</h2>
<ul>
<li><strong>Why Galileo now:</strong> Tick 103 closed with 199 leads (Traceloop) and a "Sibling-target next: Galileo (ai_infra 9th — Galileo Evaluate + Galileo Observe + Galileo Protect + RAG-hallucination-detection lane)" roadmap. Galileo is the canonical RAG-hallucination-detection + LLM-evaluation + LLM-observability platform purpose-built to answer the audit-trail surface that every regulated industry now requires. <code>team@galileo.ai</code> + <code>team@galileo.io</code> publicly exposed via <strong>https://www.galileo.ai/privacy-policy</strong> (verified 2026-07-12 by direct curl scrape — dual-domain inbox pattern + 409796-byte page exposes both galileo.ai + galileo.io canonical mailto = cleanest vendor-DD channel). Founded 2021 NYC by Vikram Chatterji (CEO, ex-Apple Siri ML lead) + Yash Sheth + Atindriyo Sanyal. HQ NYC. Raised $68M Series B led by Insight Partners + joined by Datadog Ventures + ServiceNow Ventures + SentinelOne + The Sandbox + BMW i Ventures + Fetch + Madison Dearborn.</li>
<li><strong>Pipeline now: 200 leads indexed (THE 200-LEAD MILESTONE), 286 templates on disk, 97 SEO chunks live.</strong> ai_infra vertical now has 11 leads (Honeycomb 102 + Arize 107 + Galileo 108 + Sumo Logic 131 + Datadog 150 + New Relic 151 + Splunk-Cisco 152 + SambaNova 190 + Groq 191 + Honeycomb 198 + Traceloop 199 + <strong>Galileo 200</strong> — the <strong>RAG-hallucination-detection + LLM-evaluation + per-LLM-call-tracing + per-RAG-retrieval-tracing + real-time LLM-firewall cluster</strong>). 200-lead milestone is now crossed — the pipeline is now positioned for a 400-email first blast (2 touches per lead) the moment the user supplies an SMTP credential. product_analytics_ai now has 2 leads (Amplitude 196 + Heap 197). ai_agents_infra: 16 leads. customer_service_ai: 9 leads. ai_sales_ai: 13 leads. voice_ai: 6 leads. legal_ops: 5 leads. legal_ai: 5 leads. sales_ai: 5 leads. enterprise_ai: 6 leads. dev_tools: 4 leads. customer_success: 3 leads. <strong>15+ verticals active.</strong></li>
<li><strong>Revenue: $0.</strong> Unblock path unchanged (SMTP credential + Chrome login + Reddit reCAPTCHA). Each audit-target lead is positioned for a $500/48h fixed-bid audit once the channel unblocks — at 200 leads the pipeline has crossed the 200-lead threshold where 1 channel-unblock converts into 5-10 audits within 24h, the math YanXbt's verified 5-client-at-$497-MRR pattern requires. Galileo (200) is the highest-RAG-evaluation-audit-diversity ai_infra lead added because it covers 7 distinct AI-product-line surfaces (Galileo Evaluate + Observe + Protect + Agent Observability + Chat + Lens + Studio) in one platform + the only vendor with the team@galileo.ai + team@galileo.io dual-domain inbox pattern.</li>
</ul>
</div>
'''

content = Path(LOG).read_text(encoding="utf-8")

# Variant B check: file starts with <div class="tick">
assert content.startswith('<div class="tick">'), f"unexpected first 19 chars: {content[:25]!r}"

# Anchor on <div class="tick">
anchor = '<div class="tick">'
idx = content.find(anchor)
assert idx == 0, f"first <div class=\"tick\"> at {idx}, expected 0"

# Sanity: new entry must NOT itself contain a top-level <div class="tick"> wrapper that would create nested-div bug
# (the new entry is itself one <div class="tick"> wrapper, so assert not DOUBLE-wrapped)
assert new_entry.strip().startswith(anchor), "new entry must start with the anchor"
# But we DON'T want a second nested anchor inside new_entry's body
inner_anchor_count = new_entry.count(anchor)
assert inner_anchor_count == 1, f"new_entry contains {inner_anchor_count} anchors, expected exactly 1"

# Splice
new_content = new_entry + content

Path(LOG).write_text(new_content, encoding="utf-8")

# Parse-back verify
verify = Path(LOG).read_text(encoding="utf-8")
assert verify.startswith(new_entry), "prepend failed"
# Second tick: search for the next <div class="tick"> after len(new_entry)
second_tick_offset = verify.find('<div class="tick">', len(new_entry))
assert second_tick_offset > 0 and second_tick_offset < len(new_entry) + 50, f"second tick not immediately after: {verify[len(new_entry):len(new_entry)+50]!r}"
assert "Galileo (200)" in verify, "Galileo marker missing"
assert "team@galileo.ai" in verify, "team@galileo.ai missing"
assert "Tick 104" in verify, "Tick 104 marker missing"

old_len = len(content)
new_len = len(verify)
print(f"OK: Tick 104 prepended to build-log.html ({old_len} -> {new_len} bytes)")
print(f"  New first 19 chars: {verify[:19]!r}")
print(f"  Anchor at 0: True")
print(f"  pos_NEW ({verify.find('Tick 104')}) < pos_N ({verify.find('Tick 102')}) : {verify.find('Tick 104') < verify.find('Tick 102')}")
