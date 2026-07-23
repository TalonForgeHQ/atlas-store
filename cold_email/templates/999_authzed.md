# AuthZed — AI agent authorization evidence-gap map

**Lead 999 · CLOSER #5/5 · ai_agent_authorization**

## Verified first-party evidence (2026-07-23)

- Company: AuthZed — `https://authzed.com/`
- Positioning: “The Authorization Platform for AI and Modern Applications”
- Canonical About route: `https://authzed.com/about` → `https://authzed.com/why-authzed`
- Founding team: Jake Moshenko (CEO), Joey Schorr (CTO), Jimmy Zelinskie (CPO)
- Founder history: the About page says Jake and Joey met on Google's APIs team in 2010, founded Quay, and Jimmy joined as their first hire.
- Named surfaces: AI Authorization, MCP, OpenAI + AuthZed, Retrieval-Augmented Generation, permission-aware lists and search, AuthZed Cloud, AuthZed Dedicated, SpiceDB Enterprise, and open-source SpiceDB.
- Scale principle: the About page states solutions should support 1,000,000 requests per second as well as 1,000.
- Commercial route: `FORM:https://authzed.com/schedule-demo` (first-party footer “Schedule a demo”; not submitted).

## Cohort-specific wedge

AuthZed closes the cohort with the Google-Zanzibar-derived relationship-based authorization lane: SpiceDB schema and relationship tuples drive permission checks across agents, MCP tools, RAG retrieval, and application actions. This differs from Permit.io's full-stack permissions, Cerbos's contextual policy decisions, Oso's Polar policy-as-code, and SGNL's continuous identity/CAEP/ZSP substrate.

## Proposed audit receipt

```text
tenant_id
authzed_deployment_mode
spicedb_schema_version
relationship_tuple_id
subject_identity_id
agent_identity_id
resource_type
resource_id
permission_name
caveat_name
context_hash
mcp_server_id
mcp_tool_name
rag_source_id
check_request_id
check_result
zed_token
policy_change_id
revocation_event_id
cross_tenant_no_bleed_result
audit_export_id
```

## Subject A

Can AuthZed replay each AI-agent permission decision?

## Subject B

Five authorization evidence gaps across SpiceDB, MCP, and RAG

## Subject C

$500 / 48h AuthZed AI-authorization evidence-gap map

## Body

Hi AuthZed team,

Your first-party surfaces connect SpiceDB-based authorization with AI Authorization, MCP, OpenAI, permission-aware search, and retrieval-augmented generation.

I run a fixed-scope evidence-gap map that tests whether an enterprise deployment can replay:

1. the subject, agent, resource, permission, schema version, and relationship tuple behind each decision;
2. contextual caveats and the exact inputs used at decision time;
3. MCP server and tool authorization before an agent action;
4. permission-aware RAG filtering back to the governed source;
5. policy change, revocation, cross-tenant isolation, and audit export.

The deliverable is a 21-column receipt design plus a concise audit letter. It is $500 fixed for a 48-hour single-platform map, $497/month for quarterly refreshes, or $2,000 for the five-vendor benchmark covering Permit.io, Cerbos, Oso, SGNL, and AuthZed.

If useful, I can send the one-page scope through your first-party demo route.

Atlas @ Talon Forge

---

**Status:** staged only; no form or email submitted; $0 sent / $0 received.
