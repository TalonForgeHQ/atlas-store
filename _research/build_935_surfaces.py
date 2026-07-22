#!/usr/bin/env python3
"""Append chunk_935 to sitemap.xml + index.html + revenue_log.csv + send_log.jsonl + build-log.html"""
import csv
import json
import os
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
os.chdir(REPO)

# ===== 3. APPEND chunk_935 TO sitemap.xml =====
sitemap_path = REPO / "sitemap.xml"
sitemap_text = sitemap_path.read_text(encoding="utf-8")

# Find the closing </urlset> tag and insert before it
new_url_block = """  <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_935.html</loc>
      <lastmod>2026-07-22</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.85</priority>
    </url>
"""
# Insert before closing </urlset>
sitemap_text = sitemap_text.replace("</urlset>", new_url_block + "</urlset>", 1)
sitemap_path.write_text(sitemap_text, encoding="utf-8")
print(f"OK sitemap.xml updated. New size: {len(sitemap_text)} bytes")

# ===== 4. APPEND chunk-935 card TO index.html =====
index_path = REPO / "index.html"
index_text = index_path.read_text(encoding="utf-8")

# Find the closing of the chunk-934 card
new_card = '''<div class="card" id="chunk-935" data-cohort="ai_agent_operations" data-lead="935" data-cohort-role="sibling-4-of-5">
<a href="chunks/chunk_935.html">Lead 935 — StackAI (SIBLING #4/5 ai_agent_operations) — Agentic Workflows + Agentic Development Life Cycle (SDLC for AI era) + LLM-Agnostic + 4-tier Deployment (Multi-Tenant / Single-Tenant / VPC / Air-Gapped On-Premise) + SOC 2 Type II / HIPAA / GDPR / ISO 27001 (San Francisco + Founded 2023 + YC + Google backed + 24,322 LinkedIn followers, customer logos Nubank + Dine Development Corp + SmartAsset + Granite, Asana-acquired 2026)</a>
</div>
'''
# Insert before the closing tag of the previous card or at end of cards section
# Find last closing </div> after chunk-934 card
marker = '<div class="card" id="chunk-934"'
if marker in index_text:
    # Find the end of chunk-934 card
    pos = index_text.find(marker)
    # Find the closing </div> of this card
    end_pos = index_text.find("</div>", pos) + len("</div>")
    index_text = index_text[:end_pos] + "\n" + new_card + index_text[end_pos:]
else:
    # fallback: append to end
    index_text = index_text + "\n" + new_card

index_path.write_text(index_text, encoding="utf-8")
print(f"OK index.html updated. New size: {len(index_text)} bytes")

# ===== 5. APPEND send_log.jsonl row =====
send_log_path = REPO / "cold_email" / "send_log.json"
# Read existing JSON array
try:
    send_log_data = json.loads(send_log_path.read_text(encoding="utf-8"))
except json.JSONDecodeError:
    send_log_data = []

new_entry = {
    "timestamp": "2026-07-22T19:30:00Z",
    "lead": "935",
    "company": "StackAI",
    "vertical": "ai_agent_operations",
    "sent_amount": 0,
    "received_amount": 0,
    "status": "queued_not_sent",
    "route": "FORM:https://www.stackai.com/demo (Framer Typeform embed)",
    "template": "templates/935_stackai.md",
    "note": "FORM only per pitfall #28 — /about + /contact 404 on rendered Framer SPA; mailto:NONE first-party"
}
send_log_data.append(new_entry)
send_log_path.write_text(json.dumps(send_log_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"OK send_log.json updated. New entries: {len(send_log_data)}")

# ===== 6. APPEND revenue_log.csv row =====
revenue_log_path = REPO / "cold_email" / "revenue_log.csv"
with open(revenue_log_path, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow([
        "2026-07-22", "935", "935_stackai.md", "chunk_935.html",
        "ai_agent_operations SIBLING #4/5 (after Glean 902 OPENER + Lindy AI 922 SIBLING #2/5 + Bardeen 923 SIBLING #3/5) — StackAI Inc. (stackai.com — San Francisco CA HQ + Founded 2023 + 51-200 employees + 24,322 LinkedIn followers + YC + Google backed verbatim LinkedIn 2026-07-22 — Asana acquisition just-announced verbatim home — Agentic Workflows + Agentic Development Life Cycle + LLM-Agnostic + 4-tier deployment model + SOC 2 Type II + GDPR + HIPAA + ISO 27001 verbatim /security 2026-07-22 — customer logos Dine Development Corp + Nubank + SmartAsset + Granite verbatim home — FORM:https://www.stackai.com/demo is the canonical commercial route per pitfall #28 (Framer Typeform embed — /about + /contact 404 on rendered Framer SPA) — 16-col per-agent-action + per-deployment-model + per-LLM-call + per-MCP-tool-call + per-human-in-loop-acknowledgment + per-audit-log-row + per-SSO-SAML-attribute-bundle + per-tenant-credential-scope evidence-join-table cross-tenant-no-bleed — $500/48h + $497/mo + YanXbt 5-client $2,485 MRR ceiling — SMTP/form gated; no send, submission, payment, or revenue claim was fabricated.",
        "0",
        "Lead 935 — StackAI Inc. (stackai.com — San Francisco CA HQ + Founded 2023 + 51-200 employees + YC + Google backed verbatim LinkedIn 2026-07-22 — 24,322 LinkedIn followers verbatim — Asana acquisition just-announced verbatim home 2026-07-22 — 4 NAMED first-party AI surfaces verbatim home: Agentic Workflows + Deploy Anywhere + Security and Governance + Human in the Loop + LLM Agnostic + Agentic Development Life Cycle + White-Glove Experience — verbatim first-party compliance /security 2026-07-22: SOC 2 Type II + HIPAA + GDPR + ISO 27001 4-stack verbatim + AES-256 at rest + TLS 1.3 in transit verbatim + Data Retention Policies verbatim + No Training on Your Data via DPAs verbatim + Custom SSO SAML verbatim + 4 deployment models Multi-Tenant Cloud / Single Tenant Cloud / VPC / Air-Gapped On-Premise verbatim — verbatim customer logos home image alts 2026-07-22: Dine Development Corporation (DDC) + Nubank + SmartAsset + Granite — SIBLING #4/5 of ai_agent_operations cohort after Glean 902 OPENER + Lindy AI 922 SIBLING #2/5 + Bardeen 923 SIBLING #3/5 — 5 non-overlap wedges: only cohort member with NAMED first-party Agentic Workflows + Agentic SDLC substrate + only cohort member with NAMED first-party 4-tier deployment model + only cohort member with verbatim first-party 4-stack AICPA SOC 2 + GDPR + HIPAA + ISO 27001 compliance + only cohort member with NAMED first-party no-train-on-customer-data via DPAs + Data Retention Policies verbatim + only cohort member with NAMED first-party LLM-Agnostic stance + White-Glove Experience — 16-col per-StackAI-agent-action + per-deployment-model + per-LLM-call + per-MCP-tool-call + per-human-in-loop-acknowledgment + per-audit-log-row + per-SSO-SAML-attribute-bundle + per-tenant-credential-scope evidence-join-table cross-tenant-no-bleed — Offer $500/48h fixed-scope StackAI + Agentic Workflows + Agentic SDLC + LLM-Agnostic + 4-tier deployment evidence-gap-map or $497/mo quarterly refresh — FORM:https://www.stackai.com/demo NOT submitted — mailto:NONE first-party per pitfall #28 (/about + /contact 404 on rendered Framer SPA) — SMTP/form gated; no send, submission, payment, or revenue claim was fabricated."
    ])
print(f"OK revenue_log.csv updated. Total lines: {sum(1 for _ in open(revenue_log_path, encoding='utf-8'))}")