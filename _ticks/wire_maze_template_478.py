from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
leads_path = root / "cold_email" / "leads.csv"
enriched_path = root / "cold_email" / "leads_with_emails.csv"
build_log_path = root / "build-log.html"

for path, template_field in ((leads_path, "template"), (enriched_path, "source_template")):
    with path.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    header = rows[0]
    id_index = header.index("index" if path == leads_path else "lead_index")
    template_index = header.index(template_field)
    matches = [row for row in rows[1:] if len(row) > id_index and row[id_index] == "478"]
    assert len(matches) == 1, f"expected one lead 478 in {path}, got {len(matches)}"
    matches[0][template_index] = "478_maze.md"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerows(rows)

log = build_log_path.read_text(encoding="utf-8")
assert log.rstrip().endswith("</html>"), "build-log.html does not end in </html>"
assert 'data-tick="2026-07-17-fast-exec-maze-template-478"' not in log
entry = '''<div class="tick-entry" data-tick="2026-07-17-fast-exec-maze-template-478">
<h2>Tick FastExec 2026-07-17 ~13:10Z — Maze 478 audit template wired to both lead indexes</h2>
<p><strong>Artifact shipped:</strong> added <code>cold_email/templates/478_maze.md</code>, a concise Maze-specific outbound template addressed to the verified public inbox <code>privacy@maze.design</code>. The opener targets Jonathan Widawski and the product-discovery buyer lane with a $500 / 48-hour per-study provenance audit and $497/mo evidence-maintenance option.</p>
<p><strong>Revenue progress:</strong> wired <code>478_maze.md</code> into Lead 478 in both <code>cold_email/leads.csv</code> and <code>cold_email/leads_with_emails.csv</code>. The ai_research cohort now has four executable lead/template pairs — Outset, Listen Labs, Dovetail, and Maze — representing a $2,000 one-time-audit / $1,988 monthly-retainer ceiling once SMTP is unblocked.</p>
<p><strong>Pivot:</strong> Google research returned a bot challenge, so the tick stopped browser activity and used the already verified first-party Maze facts from Lead 478 instead. A Marvin lead was screened as the next sibling but deferred because first-party founder evidence was not available quickly enough; no port 9224 activity occurred.</p>
<p><strong>Next:</strong> continue ai_research sibling #5 with Marvin, Looppanel, Condens, or UserTesting, after first-party founder verification. SMTP remains the hard outbound blocker.</p>
</div>

'''
build_log_path.write_text(entry + log, encoding="utf-8")
print("updated lead 478 in both CSVs and prepended build-log entry")
