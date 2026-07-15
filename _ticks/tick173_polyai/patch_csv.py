from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
INDEX = '265'
reason = ('Canonical enterprise conversational-AI-agent platform: PolyAI Agentic Dialog Platform lets enterprise teams build, run, adapt, and iterate dialog agents across millions of customer conversations. '
          'compliance@poly.ai verified live 2026-07-16 via curl on https://poly.ai/privacy-policy (HTTP 200, 189,959 bytes) exposing mailto:compliance@poly.ai; legal@poly.ai also exposed on the same official privacy notice. '
          'Founder Nikola Mrkšić verified live on https://poly.ai/about as Co-founder & CEO, PolyAI; Shawn Wen and Eddy Su are also listed as co-founders. '
          'Tier-1 ai_agents_infra target for per-conversation turn + dialog-state + policy-version provenance, retrieval-context lineage, tool-call and handoff side effects, cross-tenant knowledge isolation, and GDPR Article 17 deletion propagation.')

lead = [INDEX, 'PolyAI', '@PolyAI', 'compliance@poly.ai', 'ai_agents_infra', '1', '354_polyai.md', reason]
enriched = [INDEX, 'PolyAI', '@PolyAI', 'poly.ai', 'https://poly.ai', 'Nikola Mrkšić (Co-founder + CEO)', 'ai_agents_infra', '1', 'compliance@poly.ai', 'compliance@poly.ai; legal@poly.ai', '', '354_polyai.md', reason]

for filename, row in [('cold_email/leads.csv', lead), ('cold_email/leads_with_emails.csv', enriched)]:
    path = ROOT / filename
    with path.open('r', encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f))
    ids = {r[0] for r in rows[1:] if r}
    if INDEX not in ids:
        with path.open('a', encoding='utf-8', newline='') as f:
            csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerow(row)
        print('appended', filename, INDEX)
    else:
        print('already present', filename, INDEX)

for filename in ['cold_email/leads.csv', 'cold_email/leads_with_emails.csv']:
    with (ROOT / filename).open('r', encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f))
    ids = [r[0] for r in rows[1:] if r]
    print(filename, 'rows=', len(ids), 'index_265=', ids.count(INDEX), 'max_index=', max(map(int, ids)))
