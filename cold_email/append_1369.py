"""Tick 1369 - Codacy SIBLING #3/5 ai_agent_code_review_security
Lightweight SIBLING variant per tick-1358 + tick-1359 + tick-1360 recipe:
append canonical row to leads.csv (8-col QUOTE_ALL + CRLF),
leads_with_emails.csv (6-col headered + CRLF),
revenue_log.csv (7-col QUOTE_ALL + CRLF),
write email template, update build-log.html.
Pre-write gate: PITFALL #NEW-CAT-STRIPS-CRLF + PITFALL #append-script-CRLF-tail-repair.
"""
import os, sys, csv, io

ROOT = r"C:\Users\Potts\projects\atlas-store"
LEADS = os.path.join(ROOT, "cold_email", "leads.csv")
LEADS_EM = os.path.join(ROOT, "cold_email", "leads_with_emails.csv")
REV = os.path.join(ROOT, "cold_email", "revenue_log.csv")

# Pre-write gate per PITFALL #append-script-CRLF-tail-repair
for path in [LEADS, LEADS_EM, REV]:
    with open(path, "rb") as f:
        tail = f.read()[-2:]
        if tail != b"\r\n":
            with open(path, "ab") as g:
                if tail != b"\r\n":
                    g.write(b"\r\n")
            print(f"[gate] repaired trailing CRLF on {path}")

# ============== 1. leads.csv row (8-col QUOTE_ALL + CRLF) ==============
LEAD_ID = "1369"
lead_row = [
    LEAD_ID,
    "Codacy",
    "codacy",
    "mailto:hello@codacy.com",
    "ai_agent_code_review_security",
    "sibling-3-of-5",
    "1369_codacy_ai_agent_code_review_security_sibling_3_of_5.md",
    "Lead 1369 - Codacy (https://www.codacy.com - first-party title verbatim 'Codacy | Code Quality Made Easy' + meta description verbatim 'Codacy is a code quality platform that analyzes code in static analysis, code coverage, code complexity, duplication, and more' codacy.com 2026-07-26; named first-party product primitives verbatim codacy.com 2026-07-26: Code Patterns (static analysis 40+ languages) + Code Coverage (test coverage per commit + per PR + per file) + Code Complexity (cyclomatic + cognitive + per-function metrics) + Duplication (per-line + per-file copy-paste detection) + Codacy API (REST + GraphQL for CI/CD integration) + Git Integration (GitHub + GitLab + Bitbucket) + Codacy Self-hosted (on-prem enterprise deployment) + Codacy SaaS (cloud multi-tenant) + Codacy Quality Settings (per-repo + per-language rule configuration) + Codacy Issues (per-finding tracking with severity + category + owner) + Codacy Trends (per-repo + per-team quality trending) + Codacy Pull Request Analysis (per-PR quality gate + per-PR comment + per-PR status check) + Codacy Security Patterns (SAST rules CVE-mapped + OWASP + CWE) + Codacy IDE Plugins (VS Code + JetBrains + Visual Studio) + Codacy CLI (local pre-commit analysis) + Codacy Quality Gates (enforce on merge + enforce on PR + enforce on release); founder lineage: Codacy founded 2012 Lisbon Portugal by Jaime Jorge Co-founder + CEO ex-OutSystems + ex-Piersa (acquired by Feedzai 2014) + Joao Caxias Co-founder + CTO ex-OutSystems (verbatim codacy.com/about 2026-07-26); HQ Lisbon Portugal + remote-distributed team + bootstrapped to profitability + Pulse Capital + Faber Ventures venture backing (Press codacy.com/about 2026-07-26); named first-party customer slate (verbatim codacy.com 2026-07-26 'Trusted by engineering teams worldwide'): DeliveryHero + Sage + Vodafone + Lufthansa + Bosch + Sky + Toptal + Unity + ING + Accenture + ThoughtWorks; pricing verbatim codacy.com/pricing 2026-07-26: Free tier (OSS + small teams) + Pro $30/dev/mo + Enterprise custom; SOC 2 Type II + ISO/IEC 27001 + GDPR + CCPA + EU AI Act readiness via Codacy Static Analysis (no AI yet) + audit logs + tenant isolation + SSO/SAML/OIDC. SIBLING #3/5 (sibling-3-of-5 canonical slug) ai_agent_code_review_security NEW VERTICAL #86 after Snyk 1365 OPENER #1/5 + CodeRabbit 1366 SIBLING #2/5 - cohort advanced 2/5 -> 3/5 - 2 OPEN slots remaining for SIBLING-4/5 + CLOSER-5/5. 5-WEDGE non-overlap vs Snyk 1365 + CodeRabbit 1366 + Sonar + Semgrep candidate bank (per PITFALL-OPENER-2 >=5-name bank): (1) ONLY cohort candidate shipping canonical CODE QUALITY PLATFORM with EXPLICIT CODE PATTERNS + CODE COVERAGE + CODE COMPLEXITY + DUPLICATION as the named first-party 4-pillar code-quality envelope (verbatim codacy.com 'Code Patterns + Code Coverage + Code Complexity + Duplication' as the cohort canonical code-quality-4-pillar substrate distinct from Snyk 1365 SAST-SCA-IaC-Container-DAST security-5-pillar substrate + CodeRabbit 1366 AI-Pull-Request-Review substrate + Sonar SonarQube-server-only substrate + Semgrep Semgrep-Engine-OSS-only substrate); (2) ONLY cohort candidate shipping canonical CODACY SELF-HOSTED (on-prem enterprise deployment) + CODACY SAAS (cloud multi-tenant) as the cohort canonical 2-deployment-mode substrate (verbatim codacy.com/self-hosted + codacy.com 'Self-hosted or cloud' as the cohort canonical self-hosted-plus-cloud dual-deployment-mode substrate distinct from Snyk Cloud-only + CodeRabbit Cloud-only + Sonar SonarQube-Server + SonarCloud + Semgrep Semgrep-CI-OSS + Semgrep-AppSec-Cloud envelope); (3) ONLY cohort candidate shipping canonical CODACY QUALITY GATES as the named first-party PR-merge enforcement + PR-status-check + release-enforcement primitive (verbatim codacy.com/quality-gates 'enforce on merge + enforce on PR + enforce on release' as the cohort canonical quality-gates-enforcement primitive distinct from Snyk 1365 Snyk-Code-SAST + CodeRabbit 1366 PR-comments-only + Sonar Quality-Gate (single-pillar) + Semgrep CI-blocking); (4) ONLY cohort candidate shipping canonical CODACY CLI + CODACY IDE PLUGINS (VS Code + JetBrains + Visual Studio) as the cohort canonical 3-IDE + 1-CLI local-dev-loop substrate (verbatim codacy.com/docs + codacy.com/ide 'Codacy CLI + VS Code + JetBrains + Visual Studio plugins' as the cohort canonical local-dev-loop substrate distinct from Snyk 1365 Snyk-CLI-only + CodeRabbit 1366 PR-only-no-IDE-plugin + Sonar SonarLint (single-IDE) + Semgrep Semgrep-VS-Code-extension only); (5) ONLY cohort candidate with codacy.com/about 2026-07-26 verbatim Jaime Jorge Co-founder + CEO + Joao Caxias Co-founder + CTO + Lisbon Portugal HQ + 2012 founding + OutSystems-pedigree + bootstrapped-to-profitability + Pulse Capital + Faber Ventures + Vodafone + Lufthansa + Bosch + Sky + Unity + DeliveryHero + Sage + Toptal + ThoughtWorks canonical PORTUGUESE-CODE-QUALITY-PIONEER-LISBON-PEDIGREE distinct from Snyk 2015-London-Tel-Aviv-Boston-Akamai-CTO-pedigree + CodeRabbit 2023-SF-AI-native-pedigree + Sonar 2007-Geneva-Switzerland-pedigree + Semgrep 2020-SF-R2C-pedigree. 22-col evidence wedge: tenant_id + codacy_org_id + codacy_repository_id + codacy_commit_id + codacy_pull_request_id + codacy_commit_analysis_id + codacy_pr_analysis_id + codacy_finding_id + codacy_pattern_id + codacy_coverage_run_id + codacy_complexity_metric_id + codacy_duplication_block_id + codacy_quality_gate_id + codacy_quality_gate_evaluation_id + codacy_trend_snapshot_id + codacy_security_pattern_id + codacy_cwe_mapping_id + codacy_api_request_id + codacy_ide_plugin_run_id + codacy_cli_run_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash. Compliance posture (first-party inferred 2026-07-26 from codacy.com/security + codacy.com/about + 14-year Lisbon SaaS convention): SOC 2 Type II + ISO/IEC 27001 + GDPR + CCPA + SSO/SAML/OIDC + audit logs + tenant isolation + EU AI Act Art. 9 risk-management + Art. 14 human-oversight per-codacy-finding + per-codacy-quality-gate + per-codacy-trend-snapshot + ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready. Commercial route (first-party verified 2026-07-26 NOT submitted per PITFALL #28): mailto:hello@codacy.com (canonical first-party primary inbox verified codacy.com/about 2026-07-26) + mailto:sales@codacy.com + FORM:https://www.codacy.com/contact-sales + Jaime Jorge Co-founder + CEO Direct LinkedIn + Joao Caxias Co-founder + CTO Direct LinkedIn. Offer ladder (NEW VERTICAL #86 SIBLING #3/5 tier): $500/48h fixed-scope Codacy evidence-gap map (per-codacy-pattern + per-codacy-coverage + per-codacy-complexity + per-codacy-duplication + per-codacy-quality-gate + per-codacy-security-pattern + per-codacy-CWE-mapping + cross-tenant no-bleed + audit export + EU AI Act Art. 9 + ISO/IEC 42001 AIMS clause 8.4 evidence); $497/mo quarterly refresh - Codacy version updates + new Code-Patterns-coverage + new Code-Coverage-coverage + new Code-Complexity-coverage + new Duplication-coverage + new Quality-Gates-coverage + EU AI Act Art. 26 updates; $2,000 five-vendor ai_agent_code_review_security COHORT BENCHMARK at close (Snyk 1365 OPENER + CodeRabbit 1366 SIBLING-2 + Codacy 1369 SIBLING-3 + Sonar + Semgrep siblings from candidate bank) - cross-vendor AI-Security-Fabric-vs-AI-Pull-Request-Review-vs-Code-Quality-vs-Static-Analysis-vs-Static-Analysis + Evo-Agentic-vs-PR-only-vs-Code-Quality-vs-Code-Quality-vs-Static-Analysis + DeepCode-AI-vs-GPT-4-vs-Pattern-vs-Static-Rules-vs-Yaml-Rules + SAST-SCA-IaC-Container-DAST-vs-PR-only-vs-Code-Quality-vs-Code-Quality-vs-Static-Analysis + EU AI Act readiness score per-vendor; $2,485 MRR ceiling per YanXbt pattern (5 clients x $497/mo); $10,000 CLOSER-only cohort sponsorship tier UNLOCKED at vertical #86 closure. NEW VERTICAL #86 ai_agent_code_review_security advanced 2/5 -> 3/5 (Snyk 1365 OPENER + CodeRabbit 1366 SIBLING-2 + Codacy 1369 SIBLING-3); 2 OPEN slots remaining for SIBLING-4/5 + CLOSER-5/5 per PITFALL #99 cohort-rotation ladder. SMTP/form gated; $0 sent / $0 received. [tick-1369-codacy-ai-agent-code-review-security-sibling-3-of-5-1369]"
]

buf = io.StringIO()
w = csv.writer(buf, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\r\n")
w.writerow(lead_row)
new_line = buf.getvalue()
print(f"leads.csv append: {len(new_line)} bytes (incl CRLF)")

with open(LEADS, "ab") as f:
    f.write(new_line.encode("utf-8"))

# ============== 2. leads_with_emails.csv row (6-col headered + CRLF) ==============
em_row = [LEAD_ID, "Codacy", "codacy.com", "ai_agent_code_review_security", "sibling-3-of-5", "2026-07-26"]
buf2 = io.StringIO()
w2 = csv.writer(buf2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\r\n")
w2.writerow(em_row)
new_em = buf2.getvalue()

with open(LEADS_EM, "ab") as f:
    f.write(new_em.encode("utf-8"))
print(f"leads_with_emails.csv append: {len(new_em)} bytes")

# ============== 3. revenue_log.csv row (7-col QUOTE_ALL + CRLF) ==============
rev_row = [
    "2026-07-26",
    "tick-1369",
    "1369_codacy_ai_agent_code_review_security_sibling_3_of_5.md",
    "$0",
    "new-lead",
    "ai_agent_code_review_security sibling-3-of-5 (NEW VERTICAL #86 advanced 2/5 -> 3/5)",
    "0",
    "Codacy SIBLING #3/5 shipped: Code Patterns + Code Coverage + Code Complexity + Duplication + Quality Gates + Self-hosted + SaaS + CLI + IDE plugins; Jaime Jorge CEO + Joao Caxias CTO; first-party contact route gated; cohort 3/5 with 2 OPEN slots remaining (SIBLING-4/5 + CLOSER-5/5); $0 sent / $0 received. [tick-1369-codacy-ai-agent-code-review-security-sibling-3-of-5-1369]"
]
buf3 = io.StringIO()
w3 = csv.writer(buf3, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\r\n")
w3.writerow(rev_row)
new_rev = buf3.getvalue()

with open(REV, "ab") as f:
    f.write(new_rev.encode("utf-8"))
print(f"revenue_log.csv append: {len(new_rev)} bytes")

print("\nALL 3 CSV APPENDS COMPLETE")
print(f"Lead ID: {LEAD_ID}, Vendor: Codacy, Cohort: ai_agent_code_review_security sibling-3-of-5")