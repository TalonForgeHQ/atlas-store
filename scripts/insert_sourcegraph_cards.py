#!/usr/bin/env python3
"""Insert Sourcegraph (lead 696) card after every Cursor (lead 695) card in index.html.
Mirrors the +8 Cursor card injection pattern from tick 695.
"""
from pathlib import Path

INDEX = Path("index.html")
text = INDEX.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)

# Build the Sourcegraph card (same shape as a Cursor card)
card = """<article class="card" data-tick="2026-07-20-fast-exec-sourcegraph-696">
  <h3><a href="chunks/chunk_696.html">Sourcegraph Cody + Amp + MCP-Server Audit 2026: Code Intelligence Platform + Per-LLM-Sub-Processor-Version-Pinning + Per-SCIP-Retrieval-Index-Version-Pinning + Per-MCP-Tool-Call-Version-Pinning + Agentic Batch Changes Public Beta + SOC 2 Type II + ISO/IEC 42001 + EU AI Act Article 14(4) + Annex IV §1-3 + 200+ Enterprise Engineering Customers</a></h3>
  <p><strong>Vertical:</strong> ai_coding_agent_vertical sibling #2/5 (after Cursor 695 OPENER sibling #1/5)</p>
  <p><strong>Lead:</strong> Sourcegraph (Sourcegraph, Inc. — sourcegraph.com; Quinn Slack Co-Founder + CEO ex-Google; Beyang Liu Co-Founder + CTO; 200+ enterprise engineering customers; Stripe + MongoDB + Dropbox + Canva + HubSpot + Indeed + Leidos + Reddit + MathWorks + Blackstone + Midjourney named customers; 1M+ developers; $225M Series D 2022; $2.625B valuation; Y Combinator W13; Craft Ventures + Sequoia Capital + Andreessen Horowitz + Insight Partners + Goldcrest Capital + Founders Fund + Redpoint Ventures + Section 32; Code Intelligence Platform + Code Search + Code Navigation + Deep Search + Batch Changes + Agentic Batch Changes public beta 2026 + Cody Free/Pro/Enterprise AI coding assistant + Amp autonomous coding agent + Sourcegraph MCP server sg_keyword_search/sg_nls_search/sg_grep/sg_glob/sg_blame/sg_context + Sourcegraph Model Provider + Sourcegraph Cloud + Sourcegraph self-hosted)</p>
  <p><strong>Wedge:</strong> Per-LLM-sub-processor-version-pinning audit-trail (Cody LLM-router Claude-version + GPT-5-version + Gemini-version + Mixtral-version + Sourcegraph-Model-Provider-version + Amp agent-loop-version) + per-MCP-tool-call-version + per-MCP-server-version + per-MCP-tool-input-checksum + per-MCP-tool-output-checksum + per-MCP-tool-call-latency attestation + per-SCIP-retrieval-index-version-pinning + per-retrieval-chunk-source-version (chunk-source-file-version + chunk-source-checksum + chunk-source-license + chunk-source-EMBEDDING-model-version) + per-deployment-mode (Cloud multi-tenant customer-isolated GCP vs Self-Hosted no-customer-code-egress) + per-enterprise-KMS-key-id + per-enterprise-VPC-isolation + per-region-of-processing (US-federal + US-state + EU-member-state + UK + APAC) + per-enterprise-data-residency-pinning + per-Amp-autonomous-multi-step-coding-task-version (bash-tool-call-version + file-system-tool-version + LSP-tool-version + test-runner-integration-version + code-host-API-version + CI-pipeline-gate-version + per-agent-decision-rationale + per-PR-creation-step-version) + per-Cody-IDE-extension-version-pinning (VS Code + JetBrains + Visual Studio + CLI) + per-VS-Code-extension-API-version + per-Open-VSX-registry-version + per-extension-permission-posture (network + file-system + execute + clipboard + webview) + per-extension-isolation + per-Cody-Enterprise-SSO-idp-tenant-isolation + per-SCIM-provisioning + per-OIDC-scope + per-SAML-assertion + per-just-in-time-provisioning + per-directory-sync + per-Cody-Enterprise-PR-branch-isolation + per-Cody-Enterprise-repo-isolation + per-zero-data-retention-opt-in/out + per-training-data-opt-in/out + per-customer-source-code-deletion-receipt + per-MFA-required-privilege-escalation + per-PR-branch-CI-pipeline-integration-version (GitHub Actions + GitLab CI + CircleCI + Jenkins + Buildkite + Drone) + per-Cody-test-runner-integration-version (jest + pytest + go test + cargo test + JUnit + RSpec + xUnit) + per-Cody-SAST-integration-version (Snyk + CodeQL + SonarQube + Semgrep) + per-Cody-SCA-integration-version (Snyk Open Source + Dependabot + Socket + Sonatype + JFrog Xray + FOSSA) + per-Cody-Batch-Change-version + per-Cody-Agentic-Batch-Changes-version (public beta 2026) + per-agentic-batch-change-PR-creation-step-version + per-agentic-batch-change-PR-merge-decision-version + per-agentic-batch-change-CI-pipeline-gate-version + per-agentic-batch-change-human-reviewer-required-version + per-agentic-batch-change-stale-revert-receipt audit-trail.</p>
  <p><strong>Compliance:</strong> SOC 2 Type II + ISO 27001 + ISO/IEC 42001 + ISO/IEC 23894 + GDPR Art 5+9+22+28+30+32+35+44-49 + UK GDPR + Schrems II SCC + UK Addendum + EU-US DPF + CCPA/CPRA + PIPEDA + LGPD + APPI + Australia Privacy Act + Singapore PDPA + Quebec Law 25 + China PIPL Art 38 + EU AI Act Art 10+14(4)+50+53(1)(b) + Annex IV §1-3 technical-documentation + NIST AI RMF 600-1 + NIST AI 600-2 GENAI profile + OWASP LLM Top-10 (LLM01 prompt-injection + LLM02 sensitive-info-disclosure + LLM03 training-data-poisoning + LLM06 training-data-exfiltration + LLM07 insecure-plugin + LLM08 vector-DB-poisoning + LLM09 misinformation + LLM10 model-theft) + MITRE ATLAS (AML.T0051 LLM Plugin Compromise) + EO 14028 + EO 14110 + SLSA v1.0 Level 3 + NIST SP 800-218A SSDF + SLSA Provenance + in-toto attestation + FedRAMP Moderate + ISO 29147 + ISO 30111 + Terraform-managed + Cloudflare WAF</p>
  <p><strong>Offer:</strong> $500/48h evidence-gap map or $497/mo quarterly refresh retainer; YanXbt 5-client pattern $497/mo × 5 = $2,485 MRR per operator.</p>
  <p><strong>Inbox split (verified live 2026-07-20):</strong> security@sourcegraph.com (canonical responsible-disclosure/security inbox, verified live on sourcegraph.com/security "Contact our Security team" link) + hi@sourcegraph.com (general, verified live on sourcegraph.com/contact "Everything else") + support@sourcegraph.com (product support, verified live on sourcegraph.com/contact "Product Support").</p>
  <p><strong>Cohort:</strong> ai_coding_agent_vertical sibling #2/5 after Cursor 695 (OPENER sibling #1/5); planned siblings #3 Cognition Devin + #4 Replit Agent + CLOSER #5 GitHub Copilot Enterprise + Copilot Workspace; 12th Atlas vertical; 11 prior verticals closed at 5/5 (latest = ai_legal_compliance_os 690-694 with Harvey + Spellbook + Luminance + Ironclad + DISCO).</p>
</article>
"""

# Find each <article class="card" data-tick="2026-07-20-fast-exec-cursor-695"> opening
# Walk forward to find the matching </article> close, insert Sourcegraph card after it.
new_lines = []
i = 0
inserted = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    if 'data-tick="2026-07-20-fast-exec-cursor-695"' in line:
        # Find the matching </article> close
        depth = 1
        j = i + 1
        while j < len(lines) and depth > 0:
            if '<article' in lines[j]:
                depth += 1
            if '</article>' in lines[j]:
                depth -= 1
                if depth == 0:
                    # j is the </article> close line; append it then insert Sourcegraph card
                    new_lines.append(lines[j])
                    new_lines.append(card)
                    inserted += 1
                    i = j + 1
                    break
            j += 1
        else:
            i = j + 1
    else:
        i += 1

INDEX.write_text("".join(new_lines), encoding="utf-8")
print(f"Inserted {inserted} Sourcegraph cards after Cursor cards in index.html")
print(f"New file size: {INDEX.stat().st_size:,} bytes; lines: {len(new_lines):,}")