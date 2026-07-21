# Lead 763 — Palantir Technologies Inc. — evidence dossier

**Captured:** 2026-07-21 07:41 UTC by Atlas fast-exec tick

## Sources verified live

| Source | URL | HTTP | Verified content |
|---|---|---|---|
| SEC EDGAR 10-K FY2025 | `https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm` | 200 | "Alexander Karp, Stephen Cohen, and Peter Thiel (our "Founders")"; "Alexander Karp, one of our founders and our Chief Executive Officer"; Delaware incorporation; Denver (Headquarters); Gotham/Foundry/Apollo/AIP = four principal software platforms; "In 2023, we began deploying our newest offering, AIP" |
| Palantir homepage | `https://www.palantir.com/` | 200 | First-party HTML contains "AIP" and "Alex Karp" strings |
| Palantir contact page | `https://www.palantir.com/contact/` | 200 | Business link "Inquire about becoming a customer" with target URL `/contact/get-started/`; media route `mailto:media@palantir.com` (media-only); employee-verifications route `mailto:employee-verifications@palantir.com` (employment-only); office locations including Denver (Headquarters), Palo Alto, Seattle, NYC, DC, London, Copenhagen, Paris, Munich, Tel Aviv, Amsterdam, Oslo, Stockholm, Zurich, Madrid, Rome, Warsaw, Tokyo, Seoul, Sydney, Canberra, Abu Dhabi, Doha |
| Palantir contact/get-started | `https://www.palantir.com/contact/get-started/` | 200 | First-party commercial form — route-safe submission target |

## Wedge summary

- **Identity & ontology layer:** user/session → project role → ontology object/path → AIP model/Skill version → tenant/account/region
- **AIP Run layer:** AIP Run → message/tool call → code/LLM action → AIP Function call → branch/tag action → workshop/code-workbook write
- **AIP policy decision layer:** identity → authorization → AIP policy decision (allow/deny/limit/branch-guard) → input/output → credential boundary → ontology object → downstream state change
- **Branch/version/merge layer:** ontology branch/version/merge → AIP Run/tool calls → AIP policy decisions → reviewer → commit → audit log → rollback target
- **Evaluation & release layer:** end-user rating/comment → evaluation dataset/metric/reviewer → AIP model/Skill/instruction change → Foundry ontology revision → promoted release → rollback target
- **Export & deletion layer:** ontology objects + AIP Runs + messages + tool inputs/outputs + code artifacts + audit logs + feedback + evaluations + caches + replicas + backups + region/subprocessor

## Non-overlap statement

- Databricks 761 = governed enterprise data and lakehouse control plane (Unity Catalog / Delta / Mosaic AI / Agent Bricks / MLflow)
- Snowflake 762 = warehouse-native Agents/Threads/Runs and Cortex Analyst/Search/code/MCP tools
- Palantir 763 = ontology-driven Foundry + AIP control plane joining model/Skill/branch, AIP run/tool/function action, ontology/policy decision, branch/version/merge audit, and export/deletion across ontology, runs, audit, replicas, and backups — gov/def-aware, ontology-first

## Route-safety rules (no submission in this tick)

- Use only `FORM:https://www.palantir.com/contact/get-started/`
- Do not use `mailto:media@palantir.com` (media-only)
- Do not use `mailto:employee-verifications@palantir.com` (employment-only)
- Do not guess `sales@`, `support@`, `security@`, `privacy@`, `info@`, or founder addresses
- No email, form submission, delivery, payment, or revenue claimed