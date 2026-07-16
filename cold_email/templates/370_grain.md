# Grain — Meeting Intelligence Audit-Prep Template

**To:** privacy@grain.com  
**From:** Atlas Audit Prep — Talon Forge  
**Subject:** $500 audit, no deck — Grain meeting capture → transcript → insight → CRM lineage

> **Inquiry channel:** `privacy@grain.com` — verified live 2026-07-16 from Grain's official privacy page, `https://grain.com/privacy` (HTTP 200; the page exposes the privacy inbox). Founder evidence: Grain's official site, `https://grain.com/`, identifies Mike Adams in the company/founder surface.

---

Hi Mike and the Grain team,

Grain's meeting-recording and conversation-intelligence workflow turns customer conversations into transcripts, clips, insights, and downstream team action. The enterprise audit question is whether a reviewer can reconstruct one decision from the original meeting capture through each AI transformation and CRM or workspace write without stitching together exports by hand.

For a **$500 / 48h audit-prep sprint**, Atlas tests five concrete joins:

1. Can one `meeting_id` join to the source capture, participant-consent event, recording segment, transcript version, and speaker-attribution result?
2. Can a reviewer identify the model, prompt version, extraction result, confidence score, and human correction behind each AI summary or insight?
3. Can Grain prove tenant, workspace, user, and meeting isolation across recordings, clips, transcripts, shared links, and integrations?
4. Can a deletion request be followed from the recording and transcript through derived summaries, embeddings, clips, caches, exports, and CRM writes?
5. Can a customer export an immutable evidence bundle containing retention, access, model, consent, and downstream-action records for SOC 2, GDPR, or AI-governance review?

We deliver a gap map, a 15-column provenance join-table stub, a consent-and-deletion checklist, and a 30-minute walkthrough. If the first sprint is useful, the follow-on is **$497/mo** for a recurring evidence-reconstruction loop with a 15-minute monthly control check. Reply `AUDIT` and we will send the redacted stub, or reply `NOPE` and we will close the thread. The verified public inquiry channel is `privacy@grain.com`.

— Atlas Audit Prep  
Talon Forge LLC · https://talonforgehq.github.io/atlas-store/  
Unsubscribe: atlas@talonforgehq.io

## 15-column Grain meeting-intelligence provenance join-table

<table>
<thead><tr><th>#</th><th>Lineage column</th><th>Evidence question</th></tr></thead>
<tbody>
<tr><td>1</td><td>meeting_id</td><td>Which meeting is being reconstructed?</td></tr>
<tr><td>2</td><td>source_capture_id</td><td>Which recording or capture produced the evidence?</td></tr>
<tr><td>3</td><td>participant_consent_event_id</td><td>What proves participant notice or consent?</td></tr>
<tr><td>4</td><td>recording_segment_id</td><td>Which audio or video segment supplied the evidence?</td></tr>
<tr><td>5</td><td>transcript_version_id</td><td>Which transcript version was used?</td></tr>
<tr><td>6</td><td>speaker_attribution_id</td><td>How was speaker attribution established?</td></tr>
<tr><td>7</td><td>prompt_version_id</td><td>Which summary or extraction prompt ran?</td></tr>
<tr><td>8</td><td>model_version_id</td><td>Which model and deployment generated the result?</td></tr>
<tr><td>9</td><td>insight_result_id</td><td>Which structured insight or summary was emitted?</td></tr>
<tr><td>10</td><td>confidence_score_id</td><td>What confidence and review threshold applied?</td></tr>
<tr><td>11</td><td>human_review_event_id</td><td>Who corrected or approved the output?</td></tr>
<tr><td>12</td><td>clip_share_event_id</td><td>Which clip or shared artifact was created?</td></tr>
<tr><td>13</td><td>crm_sync_event_id</td><td>Which downstream CRM or workspace write occurred?</td></tr>
<tr><td>14</td><td>deletion_propagation_event_id</td><td>Did deletion reach all derived artifacts and exports?</td></tr>
<tr><td>15</td><td>worm_retention_flag</td><td>What proves retention and immutable evidence handling?</td></tr>
</tbody>
</table>

**Offer:** $500 one-time audit with 48h delivery; $497/mo recurring evidence loop. **Verified channel:** privacy@grain.com.
