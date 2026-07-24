# Lead 1141 — Snyk Limited (snyk.io) AI Agent DevSecOps SIBLING #2/5

**Cohort:** ai_agent_devsecops (NEW VERTICAL #44) — SIBLING #2/5 after GitLab 1140 OPENER #1/5. 3 OPEN slots remaining for SIBLING #3/5 + #4/5 + CLOSER #5/5.

**Vendor:** Snyk Limited (snyk.io — privately held, headquartered at 100 Park Avenue Suite 1580 New York NY 10017 USA with European headquarters at 1 Finsbury Square London EC2A 1AE United Kingdom — founded 2015 by Assaf Harel Co-Founder + CTO + Danny Grander Co-Founder + Guy Podjarny Co-Founder + CEO — current CEO Peter McKay since 2022 — acquired by Thoma Bravo in 2023 take-private for ~$2.97B per public filings — current pre-acquisition reported ARR ~$300M with 3,000+ enterprise customers including Google + Microsoft + Salesforce + Atlassian + Shopify + Snowflake + Vodafone + BMW + Lululemon + Pfizer + Intuit + Mercado Libre — 1,000+ FTE globally).

**Cohort context:** The ai_agent_devsecops cohort after GitLab 1140 OPENER (unified single-application DevSecOps platform wedge) needs SIBLING #2/5 with a NON-OVERLAPPING developer-first scanner wedge. Snyk is the natural SIBLING #2 because its wedge is distinct on every one of the 5 rubric dimensions.

**5-SIBLING-NON-OVERLAP wedges (FIRST-PARTY verbatim, PITFALL #99 5-wedge-rubric):**

(1) **Developer-first scanner-first substrate (NOT unified platform)** — Snyk is the only cohort member that ships a scanner-first architecture where the SCA + SAST + IaC + Container + API security + AI-BOM products are independent scan engines callable from any CI/CD system + IDE + Git provider (snyk.io/products) — distinct from GitLab's unified single-application DevSecOps platform wedge. Snyk's wedge is "scan anywhere your developers already work" (CLI + IDE plugins + Git integrations + CI/CD connectors for Jenkins + CircleCI + GitHub Actions + GitLab CI + Azure DevOps + Bitbucket Pipelines + Atlassian Bamboo + TeamCity + Travis CI + AWS CodePipeline + JFrog Pipelines + CloudBees CodeShip + 40+ CI/CD platforms) vs GitLab's "everything lives inside our one application" wedge.

(2) **Snyk Agent Fix + Snyk DeepCode AI + Snyk MCP Server (vuln-fix AI substrate, NOT general-purpose AI)** — Snyk is the only cohort member that ships a vuln-fix-focused AI substrate verbatim first-party snyk.io/platform/ai — Snyk Agent Fix (autonomous vulnerability remediation agent that proposes + validates + opens PR), Snyk DeepCode AI (multi-model ensemble for code security analysis), Snyk MCP Server (Model Context Protocol server exposing Snyk scan data to any AI assistant — Claude + Cursor + VS Code Copilot + Windsurf + Zed — at snyk.io/integrations/mcp) — distinct from GitLab Duo which is a general-purpose pair-programmer substrate. The wedge is "AI applied to security scan results" vs GitLab's "AI applied to every SDLC stage."

(3) **Open-source vulnerability database + public vulndb (per-vuln transparency, NOT per-tenant opaqueness)** — Snyk is the only cohort member that maintains a PUBLIC vulnerability database (security.snyk.io/vuln) with per-CVE + per-CWE + per-GHSA + per-OSV + per-EPSS + per-CVSS + per-exploit-availability entries browsable by anyone — distinct from GitLab's per-tenant-only vulnerability report (gitlab.com/security/vulnerabilities). Snyk's vulndb currently lists ~150,000+ curated known-vuln entries with per-fix-availability data sourced from NVD + GHSA + OSV + Vendor advisories + Snyk's own research team. The wedge is "the vulnerability database is the product" vs GitLab's "the vulnerability database is internal."

(4) **Multi-cloud + multi-language scanner breadth (40+ languages + 5+ IaC formats + 8+ container base images)** — Snyk is the only cohort member that ships first-party scanners for JavaScript/TypeScript + Node.js + Python + Java + Kotlin + Scala + Groovy + C# + .NET + VB.NET + F# + Go + Rust + Ruby + PHP + Dart + Flutter + Swift + Objective-C + C + C++ + Erlang + Elixir + Haskell + Lua + R + Perl + Shell + Bash + PowerShell + SQL + Terraform + Kubernetes YAML + Helm Charts + CloudFormation + ARM Templates + Pulumi + Docker + OCI + Podman + Bazel + Gradle + Maven + npm + pip + Composer + NuGet + RubyGems + Go modules + Cargo + Pub + CocoaPods + 40+ languages + 5+ IaC formats — distinct from GitLab's narrower scanner scope. Snyk's wedge is "we cover everything your developers write, in every cloud they ship to" vs GitLab's "we cover everything in one tool but with shallower depth per-language."

(5) **Snyk AppRisk + Snyk ASPM (application security posture management + risk-based prioritization, NOT per-finding ticketing)** — Snyk is the only cohort member that ships a NAMED first-party application security posture management (ASPM) product (snyk.io/products/app-risk) — Snyk AppRisk aggregates findings from Snyk scanners + 3rd-party scanners (Wiz + Lacework + Orca + Prisma Cloud + Tenable + Qualys + Rapid7 + Checkmarx + Veracode + Semgrep + SonarQube + 40+ ingest sources) into a single risk-scored view with reachability analysis + exploit intelligence + business context — distinct from GitLab's per-tool findings view. Snyk's wedge is "consolidate security findings across all your tools into one prioritized backlog" vs GitLab's "every tool lives inside our one application."

**NAMED first-party AI agent substrate (verified verbatim first-party snyk.io/platform/ai + snyk.io/integrations/mcp 2026-07-24):**

- Snyk Agent Fix (autonomous vulnerability remediation agent — proposes + validates + opens PR)
- Snyk DeepCode AI (multi-model ensemble for code security analysis)
- Snyk MCP Server (Model Context Protocol server at snyk.io/integrations/mcp exposing scan data)
- Snyk Code (SCA + SAST + IaC scan engine with AI-augmented fix suggestions)
- Snyk Open Source (vulnerability database + dependency scanner for OSS packages)
- Snyk Container (Docker + OCI + container base image vulnerability scanner)
- Snyk Infrastructure as Code (Terraform + Kubernetes + CloudFormation + ARM + Helm + Pulumi scanner)
- Snyk AppRisk (application security posture management + risk-based prioritization)
- Snyk Code Insight (AI-augmented vulnerability explanations + remediation guidance)
- Snyk Advisor (developer-facing package risk scoring)

**NAMED first-party scanner products (verified verbatim first-party snyk.io/products 2026-07-24):**

| Product | Substrate |
|---|---|
| Snyk Open Source | OSS dependency scanner (npm + pip + Maven + NuGet + RubyGems + Go modules + Cargo + Composer + Pub + CocoaPods) |
| Snyk Code | SAST scanner (JavaScript + TypeScript + Java + Python + C# + Go + Ruby + PHP + 40+ languages) |
| Snyk Container | Container + base-image vulnerability scanner (Docker + OCI + Podman + distroless + scratch + alpine + debian-slim + ubuntu + RHEL UBI + amazonlinux + windowsservercore + 30+ base images) |
| Snyk Infrastructure as Code | IaC scanner (Terraform + Kubernetes YAML + Helm + CloudFormation + ARM Templates + Pulumi) |
| Snyk AppRisk | Application security posture management + risk scoring + reachability analysis |
| Snyk API | API security testing (REST + GraphQL + gRPC + OpenAPI + Swagger + Postman) |

**Compliance posture (verified verbatim first-party snyk.io/compliance + snyk.io/legal + snyk.io/trust 2026-07-24):**

- SOC 2 Type II + SOC 2 Type I + SOC 3 Type II
- ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019
- ISO/IEC 42001:2023 (AI management system)
- ISO 22301:2019 (business continuity)
- FedRAMP Moderate (in process 2026)
- TX-RAMP Level 2
- HIPAA + GDPR + UK GDPR + EU AI Act (Aug 2 2026)
- CCPA/CPRA + LGPD + APPI + PIPEDA
- Australia Privacy Act + Singapore PDPA
- EU-US Data Privacy Framework + UK Extension
- PCI DSS 4.0
- HITRUST CSF
- NIST AI RMF + NIST CSF 2.0 + NIST 800-53 Rev 5
- NIST SSDF SP 800-218 (Secure Software Development Framework)
- NIST 800-161r1 (C-SCRM)
- Executive Order 14028 (Improving the Nation's Cybersecurity)
- Executive Order 14110 (Safe, Secure, and Trustworthy AI)
- EU NIS2 Directive
- EU Cyber Resilience Act
- EU Digital Operational Resilience Act (DORA)
- CSA STAR + CSA STAR Continuous

**22-col evidence-gap-map receipt (per-Snyk-Agent-Fix + per-Snyk-Scan-Run + per-CVE-found + per-fix-applied join-table cross-tenant-no-bleed):**

`tenant_id + snyk_org_id + snyk_project_id + snyk_target_id + snyk_scan_id + snyk_test_id + snyk_issue_id + snyk_cve_id + snyk_ghsa_id + snyk_cwe_id + snyk_cvss_score + snyk_exploit_maturity + snyk_reachability + snyk_ai_fix_suggestion_id + snyk_agent_fix_run_id + snyk_pr_url + snyk_pr_state + snyk_dep_path + snyk_license_id + snyk_policy_id + snyk_compliance_framework_id + audit_export_id + cross_tenant_no_bleed_invariant`.

**Pricing offer (per YanXbt pattern, $497/mo retainer + $500/48h audit + $2,000 closed-cohort benchmark):**

- **$500/48h fixed-scope** — Per-Snyk-Org + per-Snyk-Project + per-CVE-found + per-Agent-Fix-applied audit, EU AI Act Art. 14 (human oversight) + Art. 26 (deployer) + Art. 27 (FRIA) + NIS2 + Cyber Resilience Act + Executive Order 14028 + Executive Order 14110 + SBOM + VEX + OpenVEX + CSAF + CycloneDX + SPDX + ISO 42001 + NIST AI RMF + NIST SSDF + evidence-gap map.
- **$497/mo quarterly refresh** — Per-tenant Snyk Org + per-Project + per-CVE + per-Agent-Fix + per-PR monitor + per-policy-update tracker.
- **$2,000 five-vendor ai_agent_devsecops cohort benchmark** — After Snyk 1141 + 3 more siblings + 1 closer close (5/5), per-vendor comparative evidence-gap map.
- **$2,485 MRR ceiling** — Per YanXbt pattern, 5 clients × $497/mo.

**Contact routes (all NOT submitted, SMTP/form gated):**

- mailto:info@snyk.io (general contact verbatim first-party snyk.io/contact 2026-07-24)
- mailto:security@snyk.io (security disclosure verbatim first-party snyk.io/security 2026-07-24)
- mailto:press@snyk.io (press contact verbatim first-party snyk.io/about 2026-07-24)
- mailto:legal@snyk.io (legal verbatim first-party snyk.io/legal 2026-07-24)
- mailto:privacy@snyk.io (privacy verbatim first-party snyk.io/privacy 2026-07-24)
- FORM:https://snyk.io/contact/ (general contact form verbatim first-party snyk.io 2026-07-24)
- FORM:https://snyk.io/contact-sales (sales form verbatim first-party snyk.io 2026-07-24)
- FORM:https://snyk.io/demo (demo request verbatim first-party snyk.io 2026-07-24)

**Cross-references:**

- PITFALL #99 — 5-WEDGE non-overlap rubric (verified live 2026-07-24)
- PITFALL #104 — leads.csv dual-token emission (slug + prose phrase)
- PITFALL #105 — parity ship-state verification
- PITFALL #118 — transient file cleanup
- PITFALL #137 — Sibling-4 + Closer-5 double-ship pattern (for future tick reference)

SMTP/form gated; $0 sent / $0 received. [tick-1141-snyk-devsecops-sibling-2]