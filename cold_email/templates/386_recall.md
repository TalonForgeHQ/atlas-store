# Recall.ai — Meeting-Agent Audit-Prep Template

**To:** support@recall.ai  
**From:** Atlas Audit Prep — Talon Forge  
**Subject:** $500 audit, no deck — Recall meeting capture → transcript → agent-action lineage

> **Inquiry channel:** `support@recall.ai` — verified live 2026-07-16 by running the repository's `lead_finder.py` against Recall.ai's official homepage, `https://www.recall.ai/` (HTTP 200; public page exposed the support inbox).

---

Hi David, Amanda, and the Recall.ai team,

Recall.ai's public site describes meeting capture across Google Meet, Webex, in-person meetings, and phone calls. That creates a useful audit question for teams building meeting agents: can one customer decision be reconstructed from the original meeting artifact through transcription, extraction, agent reasoning, and the downstream system write without hand-joining exports from several services?

For a $500 / 48h audit-prep sprint, we test five concrete joins:

1. Can one `meeting_id` be joined to the source capture, participant-consent event, recording segment, transcript version, and extracted action item?
2. Can a reviewer identify the model, prompt version, confidence score, and human correction behind each summary or extracted field?
3. Can Recall separate customer, workspace, bot, and meeting data across Google Meet, Webex, phone, and in-person capture paths?
4. Can a deletion request be followed from recording and transcript stores through derived summaries, embeddings, caches, exports, and downstream CRM writes?
5. Can a customer export an immutable evidence bundle containing retention, access, model, and downstream-action records for SOC 2, GDPR, or AI-governance review?

If one of those joins breaks, the issue usually appears during enterprise security review—after a buyer has already asked how meeting data becomes an operational decision. We deliver the gap map, a 15-column provenance join-table stub, a consent-and-deletion checklist, and a 30-minute walkthrough. If the first sprint is useful, the follow-on is $497/mo for a recurring evidence-reconstruction loop with a 15-minute monthly control check.

Reply `AUDIT` and we will send the redacted join-table stub, or reply `NOPE` and we will close the thread. The verified public inquiry channel is `support@recall.ai`.

— Atlas Audit Prep  
Talon Forge LLC · https://talonforgehq.github.io/atlas-store/  
Unsubscribe: atlas@talonforgehq.io

## 15-column meeting-agent provenance join-table

<table>
<thead><tr><th>#</th><th>Lineage column</th><th>Evidence question</th></tr></thead>
<tbody>
<tr><td>1</td><td>meeting_id</td><td>Which meeting is being reconstructed?</td></tr>
<tr><td>2</td><td>source_capture_id</td><td>Which Google Meet, Webex, phone, or in-person capture produced it?</td></tr>
<tr><td>3</td><td>participant_consent_event_id</td><td>What proves participant notice or consent?</td></tr>
<tr><td>4</td><td>recording_segment_id</td><td>Which audio or video segment supplied the evidence?</td></tr>
<tr><td>5</td><td>transcript_version_id</td><td>Which transcript version was used?</td></tr>
<tr><td>6</td><td>speaker_attribution_id</td><td>How was each speaker attribution established?</td></tr>
<tr><td>7</td><td>prompt_version_id</td><td>Which extraction or summary prompt ran?</td></tr>
<tr><td>8</td><td>model_version_id</td><td>Which model and deployment generated the result?</td></tr>
<tr><td>9</td><td>extraction_result_id</td><td>Which structured field or summary was emitted?</td></tr>
<tr><td>10</td><td>confidence_score_id</td><td>What confidence and review threshold applied?</td></tr>
<tr><td>11</td><td>human_review_event_id</td><td>Who corrected or approved the generated result?</td></tr>
<tr><td>12</td><td>tool_call_id</td><td>Which agent or integration action followed?</td></tr>
<tr><td>13</td><td>downstream_write_id</td><td>Which CRM, ticket, or task record changed?</td></tr>
<tr><td>14</td><td>deletion_propagation_event_id</td><td>Did deletion reach recordings, transcripts, derivatives, and exports?</td></tr>
<tr><td>15</td><td>retention_audit_record_id</td><td>Where is the immutable retention and access evidence?</td></tr>
</tbody>
</table>
