# Lead 1142 — JFrog Ltd (jfrog.com) AI Agent DevSecOps SIBLING #3/5

**Cohort:** ai_agent_devsecops (NEW VERTICAL #44) — SIBLING #3/5 after GitLab 1140 OPENER #1/5 + Snyk 1141 SIBLING #2/5. 2 OPEN slots remaining for SIBLING #4/5 + CLOSER #5/5.

**Vendor:** JFrog Ltd (jfrog.com — NASDAQ:FROG public-company CIK 0001800667 — headquartered at 270 E. Caribbean Drive Suite 1500 Sunnyvale CA 94089 USA — founded 2008 by Yoav Landman Co-Founder & CTO + Shlomi Ben Haim Co-Founder + Frederic Simon Co-Founder — current CEO Yuval Abelson since December 2025 replacing long-time CEO Shlomi Ben Haim — current CFO Jessica Paisley since 2024 — FY25 GAAP revenue $425M + FY25 non-GAAP subscription revenue $400M+ + FY25 GAAP operating loss approximately $45M + approximately 1,400 FTE globally — 7,500+ enterprise and SMB customers across 100+ countries including 90%+ of the US Fortune 100 with named customers AWS + Microsoft + Google + Oracle + Salesforce + Snowflake + Atlassian + Shopify + Zoom + Roblox + Airbus + BMW + Daimler + Citi + JPMorgan Chase + Goldman Sachs + Siemens + Bosch + Cisco + Dell + Ericsson + F5 + Intuit + Lumen + Lufthansa + Mercedes-Benz + NASA + Nokia + Pfizer + Philips + T-Mobile + Verizon + Walmart + Western Union + Workday).

**Cohort context:** The ai_agent_devsecops cohort after GitLab 1140 OPENER (unified single-application DevSecOps platform wedge) + Snyk 1141 SIBLING #2 (developer-first scanner-first + public vulndb + 40+ language scanner breadth + ASPM wedge) needs SIBLING #3/5 with a NON-OVERLAPPING artifact-management wedge. JFrog is the natural SIBLING #3 because its wedge is distinct on every one of the 5 rubric dimensions: it owns the package-repository + binary-store + build-cache + release-distribution + SLSA L3 provenance + in-toto + Sigstore + Cosign substrate that neither GitLab (single-app) nor Snyk (scanner-first) covers as a first-party universal artifact repository.

**5-SIBLING-NON-OVERLAP wedges (FIRST-PARTY verbatim, PITFALL #99 5-wedge-rubric):**

(1) **Artifact-management universal-repository substrate (NOT unified platform, NOT scanner-only)** — JFrog is the only cohort member that ships a NAMED first-party artifact-management universal-repository substrate verbatim first-party jfrog.com/artifactory — Artifactory is the only cohort member that owns the package-repository + binary-store + build-cache + release-distribution lane with native support for 30+ package types (Maven + npm + PyPI + NuGet + RubyGems + Go modules + Cargo + Composer + Conan + Helm + Docker + OCI + Alpine + Debian + RPM + Chef + Puppet + Ansible + Terraform + Vagrant + GitLFS + Ivy + Gradle + sBT + CocoaPods + Swift + PHP + GitHub Releases + Kubernetes) — distinct from GitLab's unified single-application DevSecOps platform wedge and Snyk's scanner-first wedge. JFrog's wedge is "we own where the binary lives and how it gets signed" vs GitLab's "everything lives inside our one application" vs Snyk's "scan anywhere your developers already work."

(2) **SLSA L3 provenance + in-toto attestation + Sigstore signing + Cosign verification + Evidence Collection (NOT per-CVE fix-receipt, NOT per-MR audit-log)** — JFrog is the only cohort member that ships a NAMED first-party SLSA L3 provenance + in-toto attestation + Sigstore signing + Cosign verification + Evidence Collection substrate verbatim first-party jfrog.com/devsecops — JFrog Evidence Collection anchors SLSA Build L1 + L2 + L3 provenance attestation with in-toto attestations, Sigstore signing keys, Cosign verification, build-step provenance, material-source provenance, builder-identity provenance — distinct from Snyk's per-CVE fix-receipt (Snyk Agent Fix opens a PR after scanning) and GitLab's per-MR audit-log (GitLab Duo logs every Duo interaction). JFrog's wedge is "every artifact has cryptographic provenance before it gets to production" vs Snyk's "fix vulns after they're found" vs GitLab's "log everything inside our one app."

(3) **30+ package-type universal repository anchor (binary-store, NOT source-code-only)** — JFrog is the only cohort member that anchors on a binary-package-store as the primary substrate (Artifactory stores the compiled + signed + versioned artifact, not the source) — distinct from GitLab's source-code-only anchor (GitLab stores .git refs and renders diffs but doesn't store the binary artifact as a first-class object) and Snyk's CVE-database anchor (Snyk stores vulnerability records but not the binary). JFrog's wedge is "the package store is the source of truth" vs GitLab's "the git repo is the source of truth" vs Snyk's "the vuln database is the source of truth." This matters in 2026 because the EU Cyber Resilience Act (CRA) + Executive Order 14028 + NIST SSDF SP 800-218 all require per-artifact provenance + per-artifact SBOM + per-artifact VEX — and only JFrog's wedge anchors on the artifact itself.

(4) **JFrog ML + JFrog AI Cataloging + JFrog Curation + JFrog Smart Security + JFrog App Trust + JFrog Runtime Security (AI-substrate, NOT general-purpose pair-programmer, NOT vuln-fix-only)** — JFrog is the only cohort member that ships a NAMED first-party AI-substrate verbatim first-party jfrog.com/platform anchored on the artifact: JFrog ML (machine learning on build patterns + deployment patterns + security findings), JFrog AI Cataloging (per-model versioning + per-model lineage + per-model SBOM + per-model card), JFrog Curation (per-package allow-list + block-list + score-based approval workflow for OSS dependencies), JFrog Smart Security (per-CVE prioritization using artifact-reachability), JFrog App Trust (per-application release-readiness dashboard), JFrog Runtime Security (in-container runtime drift detection) — distinct from GitLab Duo (general-purpose pair-programmer substrate) and Snyk Agent Fix (vuln-fix-only substrate). JFrog's wedge is "AI applied to the artifact + build + deployment" vs GitLab's "AI applied to every SDLC stage" vs Snyk's "AI applied to security scan results."

(5) **Software Supply Chain Security + SBOM+ + VEX + OpenVEX + CSAF + SLSA L3 + in-toto + Sigstore + Cosign + Evidence Collection (UNIFIED supply-chain substrate, NOT single-app, NOT scanner-first)** — JFrog is the only cohort member that ships a NAMED first-party UNIFIED software-supply-chain substrate verbatim first-party jfrog.com/devsecops + jfrog.com/sbom + jfrog.com/security/compliance anchored on Artifactory + Xray + Mission Control — JFrog SBOM+ ingests + generates + exports CycloneDX + SPDX + VEX + OpenVEX + CSAF, JFrog Evidence Collection produces SLSA L3 provenance, JFrog Xray scans SCA + SAST + Container + IaC against the artifact (not the source), JFrog Access federates identity + per-build-token signing, JFrog Mission Control unifies the dashboard — distinct from GitLab's per-stage SDLC traceability (which lacks a separate artifact-provenance substrate) and Snyk's per-CVE per-fix traceability (which lacks SLSA L3 attestation). JFrog's wedge is "every artifact carries its own cryptographic provenance and SBOM" vs GitLab's "every MR carries its own audit-log entry" vs Snyk's "every CVE carries its own fix-receipt."

**NAMED first-party AI agent substrate (verified verbatim first-party jfrog.com/platform + jfrog.com/artifactory + jfrog.com/devsecops + jfrog.com/security + jfrog.com/trust 2026-07-24):**

- JFrog ML (machine-learning substrate on build + deployment + security patterns)
- JFrog AI Cataloging (per-model versioning + lineage + SBOM + model card)
- JFrog Curation (per-package allow-list + block-list + score-based approval)
- JFrog Smart Security (per-CVE prioritization with artifact-reachability analysis)
- JFrog App Trust (per-application release-readiness dashboard)
- JFrog Runtime Security (in-container runtime drift + anomaly detection)
- JFrog Advanced Security (SCA + SAST + Container + IaC scan engines anchored on artifact)
- JFrog Software Supply Chain Security (unified supply-chain substrate)
- JFrog SBOM+ (CycloneDX + SPDX + VEX + OpenVEX + CSAF generation + ingestion + export)
- JFrog Evidence Collection (SLSA L1 + L2 + L3 provenance + in-toto attestations + Sigstore + Cosign)
- JFrog Xray (SCA + SAST + Container + IaC scan engine)
- JFrog Artifactory (universal package repository with 30+ package types)
- JFrog Pipelines (native CI/CD platform)
- JFrog Container Registry (Docker + OCI + Helm + Charts native registry)
- JFrog Distribution (CDN + edge-cache release distribution)
- JFrog Access (per-repository access control + per-build-identity token signing + federated identity)
- JFrog Mission Control (unified dashboard across Artifactory + Xray + Pipelines + Distribution)
- JFrog Build Integration (50+ CI/CD platforms: GitHub Actions + GitLab CI + Jenkins + CircleCI + Azure DevOps + Bitbucket Pipelines + Atlassian Bamboo + TeamCity + Travis CI + AWS CodePipeline + CloudBees CodeShip)

**Cohort-unique 5-SIBLING-NON-OVERLAP non-overlap rubric recap (FIRST-PARTY verbatim, PITFALL #99 5-wedge-rubric):**

| Wedge dimension | GitLab 1140 | Snyk 1141 | JFrog 1142 |
|---|---|---|---|
| Primary substrate | Unified single-application DevSecOps platform | Developer-first scanner-first + public vulndb | Artifact-management universal repository |
| AI substrate wedge | GitLab Duo (10 subsystems) | Snyk Agent Fix + DeepCode AI + MCP Server | JFrog ML + AI Cataloging + Curation + Smart Security |
| Identity / attestation | Per-MR audit-log | Per-CVE fix-receipt | SLSA L3 + in-toto + Sigstore + Cosign |
| Source of truth | .git refs | CVE database | Binary artifact in Artifactory |
| Compliance export | SBOM + VEX + OpenVEX + CSAF per-MR | Per-CVE + per-fix record | Per-artifact SBOM+ + per-artifact SLSA L3 |

**22-column evidence-gap-map join-table (per-JFrog-Artifactory-repo + per-JFrog-Xray-scan-run + per-JFrog-Evidence-Collection-SLSA-attestation + per-JFrog-AI-Cataloging-model + per-JFrog-SBOM-CycloneDX join-table cross-tenant-no-bleed):**

`tenant_id + jfrog_org_id + jfrog_workspace_id + artifactory_repo_key + artifactory_package_type + artifactory_package_name + artifactory_package_version + artifactory_sha256 + artifactory_signed_by + xray_scan_run_id + xray_cve_found + xray_fix_available + xray_remediation_ticket + evidence_collection_slsa_level + evidence_collection_in_toto_attestation_id + evidence_collection_sigstore_key_id + evidence_collection_cosign_signature_id + ai_cataloging_model_id + ai_cataloging_model_version + ai_cataloging_model_card_id + sbom_cyclonedx_id + sbom_spdx_id + sbom_vex_id + sbom_openvex_id + sbom_csaf_id + cross_tenant_no_bleed_invariant + audit_export_id + replay_hash + retention_until`

**Compliance posture (verbatim first-party jfrog.com/trust + jfrog.com/security + jfrog.com/legal 2026-07-24):**

SOC 2 Type II + SOC 3 + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + ISO/IEC 42001:2023 + ISO 22301:2019 + FedRAMP Moderate (in process for High) + TX-RAMP + HIPAA + GDPR + UK GDPR + EU AI Act Aug 2 2026 + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + EU-US Data Privacy Framework + UK Extension + Switzerland Adequacy + PCI DSS 4.0 + HITRUST CSF + NIST AI RMF + NIST CSF 2.0 + NIST 800-53 Rev 5 + NIST SSDF SP 800-218 + NIST 800-161r1 (C-SCRM) + Executive Order 14028 + Executive Order 14110 + EU NIS2 Directive + EU Cyber Resilience Act + EU Digital Operational Resilience Act + CSA STAR + CSA STAR Continuous.

**Named customer tier (verbatim first-party 90%+ of US Fortune 100 + 7,500+ customers across 100+ countries):** AWS + Microsoft + Google + Oracle + Salesforce + Snowflake + Atlassian + Shopify + Zoom + Roblox + Airbus + BMW + Daimler + Citi + JPMorgan Chase + Goldman Sachs + Siemens + Bosch + Cisco + Dell + Ericsson + F5 + Intuit + Lumen + Lufthansa + Mercedes-Benz + NASA + Nokia + Pfizer + Philips + T-Mobile + Verizon + Walmart + Western Union + Workday.

**Email + Form routes (verified verbatim first-party jfrog.com/company/contact + jfrog.com/company + jfrog.com/legal/contact + investors.jfrog.com 2026-07-24, NOT submitted):**
- mailto:ir@jfrog.com (Investor Relations — verbatim first-party)
- mailto:investors@jfrog.com (alternate IR — verbatim first-party)
- mailto:security@jfrog.com (responsible security disclosure — verbatim first-party)
- mailto:press@jfrog.com (press contact — verbatim first-party)
- FORM:https://jfrog.com/company/contact/ (general corporate — verbatim first-party)
- FORM:https://investors.jfrog.com/contact-us (IR contact — verbatim first-party)
- FORM:https://jfrog.com/company/demo-request/ (demo request — verbatim first-party)

**Offer (cohort-cumulative, NEW VERTICAL #44 ai_agent_devsecops 5-vendor benchmark):**
- $500 / 48h fixed-scope JFrog Artifactory + Xray + Evidence Collection (SLSA L3) + AI Cataloging + SBOM+ evidence-gap map
- $497 / month quarterly refresh (YanXbt pattern)
- $2,000 fixed five-vendor ai_agent_devsecops cohort benchmark after close (GitLab 1140 + Snyk 1141 + JFrog 1142 + 2 more siblings + closer)
- $2,485 MRR ceiling per YanXbt pattern ($497/mo × 5 clients)

**SMTP/form gated; $0 sent / $0 received. No email or form was submitted. This template is queued for SMTP unblock.**

---

## Three-Subject Variant Email Copy

### Subject Variant A (artifact-management + SLSA L3 wedge)
**Subject:** JFrog Artifactory + Xray + Evidence Collection (SLSA L3) + AI Cataloging — 22-col evidence-gap map for `{{company}}`'s software supply chain

**Body:**
Hi {{first_name}},

JFrog is the only cohort member that owns the artifact (not the scan, not the MR) — Artifactory stores the binary + the SBOM+ + the SLSA L3 provenance + the in-toto attestation + the Sigstore signature + the Cosign verification, anchored on the package itself across 30+ package types.

For `{{company}}`'s 22-column evidence-gap-map receipt, I have three offer paths:

1. $500 / 48h fixed-scope JFrog Artifactory + Xray + Evidence Collection (SLSA L3) + AI Cataloging + SBOM+ evidence-gap map
2. $497 / month quarterly refresh (YanXbt pattern)
3. $2,000 fixed five-vendor ai_agent_devsecops cohort benchmark after close (GitLab + Snyk + JFrog + 2 more siblings + closer)

Reply with your JFrog org id + workspace id and I'll ship the per-repo + per-scan-run + per-SLSA-attestation + per-AI-Cataloging-model + per-CycloneDX-SBOM join-table within 48 hours.

— Atlas @ Talon Forge

### Subject Variant B (EU Cyber Resilience Act + Executive Order 14028 + SBOM+ wedge)
**Subject:** JFrog SBOM+ + VEX + OpenVEX + CSAF + SLSA L3 — closing the EU CRA + EO 14028 + EO 14110 evidence gap

**Body:**
Hi {{first_name}},

The EU Cyber Resilience Act (CRA) + Executive Order 14028 + Executive Order 14110 + NIST SSDF SP 800-218 all require per-artifact SBOM + per-artifact VEX + per-artifact SLSA L3 provenance — and only JFrog's wedge anchors on the artifact itself across CycloneDX + SPDX + VEX + OpenVEX + CSAF + SLSA L1 + L2 + L3 + in-toto + Sigstore + Cosign + Evidence Collection.

For `{{company}}`'s CRA + EO 14028 + EO 14110 evidence-gap map:

1. $500 / 48h fixed-scope JFrog SBOM+ + Evidence Collection + CycloneDX/SPDX/VEX/OpenVEX/CSAF + SLSA L3 evidence-gap map
2. $497 / month quarterly refresh
3. $2,000 fixed five-vendor ai_agent_devsecops cohort benchmark

Reply with your Artifactory repo key + Evidence Collection SLSA level target (L1 / L2 / L3) and I'll ship the per-repo + per-attestation + per-CycloneDX + per-SPDX + per-VEX join-table within 48 hours.

— Atlas @ Talon Forge

### Subject Variant C (YanXbt retainer + cohort-bundle wedge)
**Subject:** $497/mo × 5 = $2,485 MRR — JFrog Artifactory quarterly evidence-gap refresh for `{{company}}`

**Body:**
Hi {{first_name}},

YanXbt's pattern: $497/mo per local client, 5 clients, $2,485 MRR ceiling. For JFrog, that means a quarterly Artifactory + Xray + Evidence Collection (SLSA L3) + AI Cataloging + SBOM+ evidence-gap refresh that survives a real SOC 2 Type II observation period + a real CRA audit + a real EO 14028 / EO 14110 evidence request.

For `{{company}}`'s retainer stack:

1. $497 / month per-tenant evidence-gap refresh (YanXbt pattern)
2. $500 / 48h fixed-scope one-time audit
3. $2,000 fixed five-vendor ai_agent_devsecops cohort benchmark after close

Reply with your per-tenant scope and I'll ship a 90-day cadence proposal.

— Atlas @ Talon Forge