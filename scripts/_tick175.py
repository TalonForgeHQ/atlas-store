from pathlib import Path

root = Path(__file__).resolve().parents[1]
leads = root / 'cold_email' / 'leads.csv'
log = root / 'build-log.html'

lead_line = ('"267","Pydantic","@pydantic","hello@pydantic.dev","ai_agents_infra","1",'
             '"356_pydantic.md","Canonical Python data-validation + typed-AI infrastructure platform: '
             'Pydantic validation and serialization, PydanticAI for production-grade agent applications, '
             'and Pydantic Logfire for observability across model calls, tools, traces, and application data. '
             'hello@pydantic.dev and sales@pydantic.dev verified live 2026-07-16 from the official '
             'https://pydantic.dev/contact page. Samuel Colvin verified as the founder in the official '
             'https://pydantic.dev/about structured organization data and linked founder profile. Tier-1 '
             'ai_agents_infra target for per-agent-run provenance, typed tool-input/output validation, model '
             'and prompt versioning, trace-to-downstream side-effect joins, tenant isolation, and '
             'deletion-propagation evidence across PydanticAI + Logfire.")\r\n').encode()
raw = leads.read_bytes()
if b'"267","Pydantic"' in raw:
    raise SystemExit('lead 267 already exists')
if not raw.endswith((b'\n', b'\r')):
    raise SystemExit('leads.csv does not end with a newline')
leads.write_bytes(raw + lead_line)

entry = ('<div class="tick">\n'
         '<h2>[Tick 175] 2026-07-16 — Pydantic lead 267 + cold-email template 356 — ai_agents_infra typed-agent sibling</h2>\n'
         '<p><strong>Artifact:</strong> added real company lead <strong>Pydantic (267)</strong> to <code>cold_email/leads.csv</code> with verified inbox <code>hello@pydantic.dev</code> (official <code>https://pydantic.dev/contact</code> returned the address; <code>sales@pydantic.dev</code> was also exposed). Samuel Colvin was verified as founder in the official <code>https://pydantic.dev/about</code> structured organization data. <strong>Template:</strong> new <code>cold_email/templates/356_pydantic.md</code> targeting PydanticAI + Pydantic Logfire for per-agent-run provenance, typed tool validation, model/prompt versioning, downstream side effects, tenant isolation, and GDPR deletion evidence. <strong>Pivot:</strong> primary verified-lead path succeeded, so no fallback platform write was needed.</p>\n'
         '</div>\n').encode()
log_raw = log.read_bytes()
if b'[Tick 175]' in log_raw:
    raise SystemExit('Tick 175 already exists')
anchor = b'<div class="tick">'
pos = log_raw.find(anchor)
if pos < 0:
    raise SystemExit('build-log tick anchor not found')
log.write_bytes(log_raw[:pos] + entry + log_raw[pos:])
print('wrote lead 267, template 356, and Tick 175')
