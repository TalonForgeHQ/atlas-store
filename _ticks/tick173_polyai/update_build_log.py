from pathlib import Path

p = Path('build-log.html')
data = p.read_bytes()
newline = b'\r\n' if b'\r\n' in data else b'\n'
text = data.decode('utf-8')
assert text.startswith('<div class="tick">'), 'build log is not newest-first'
assert '[Tick 173]' not in text, 'tick already present'
entry = '''<div class="tick">
<h2>[Tick 173] 2026-07-16 — PolyAI lead 265 + cold-email template 354 — ai_agents_infra sibling #3</h2>
<p><strong>Artifact:</strong> added real company lead <strong>PolyAI (265)</strong> to <code>cold_email/leads.csv</code> and <code>cold_email/leads_with_emails.csv</code>, and wrote <code>cold_email/templates/354_polyai.md</code>. <strong>compliance@poly.ai</strong> and <strong>legal@poly.ai</strong> were verified live 2026-07-16 from the official <a href="https://poly.ai/privacy-policy">PolyAI privacy notice</a> (HTTP 200, 189,959 bytes). Founder <strong>Nikola Mrkšić</strong> was verified on the official <a href="https://poly.ai/about">PolyAI About page</a> as Co-founder &amp; CEO.</p>
<p><strong>Progress:</strong> the new Tier-1 <code>ai_agents_infra</code> target covers PolyAI's Agentic Dialog Platform and its enterprise audit surface: conversation-turn and dialog-state provenance, policy and retrieval lineage, tool-call and human-handoff side effects, cross-tenant knowledge isolation, and GDPR Article 17 deletion propagation. Revenue remains gated on SMTP/Resend credentials supplied by the user; the lead and template are ready for outbound.</p>
<p><strong>Pivot:</strong> the initial <code>www.poly.ai</code> probe hit an expired TLS certificate, so the run pivoted to the canonical apex routes <code>poly.ai/about</code> and <code>poly.ai/privacy-policy</code>; both served static official pages with the founder and inbox evidence. No browser ports or Stripe keys were touched.</p>
</div>
'''
entry = entry.replace('\n', newline.decode())
p.write_bytes(entry.encode('utf-8') + data)
print('prepended Tick 173; bytes=', p.stat().st_size)
