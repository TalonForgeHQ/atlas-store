# Fireflies.ai — Meeting Intelligence Audit-Prep Template

**To:** support@fireflies.ai  
**From:** Atlas Audit Prep — Talon Forge  
**Subject:** $500 audit, no deck — Fireflies meeting capture → transcript → AI action lineage

> **Inquiry channel:** `support@fireflies.ai` — verified live 2026-07-16 from Fireflies.ai's official privacy page, `https://fireflies.ai/privacy-policy` (HTTP 200; the page exposes support@fireflies.ai and security@fireflies.ai). Founder evidence: Fireflies.ai's official About Us page, `https://fireflies.ai/about-us`, identifies Krish Ramineni (Co-Founder & CEO) and Sam Udotong (Co-Founder & CTO).

---

Hi Krish, Sam, and the Fireflies.ai team,

Fireflies.ai turns meetings into transcripts, summaries, analyses, and downstream team actions. The enterprise audit question is whether a reviewer can reconstruct one customer decision from the original capture through each AI transformation and integration write without stitching together exports by hand.

For a **$500 / 48h audit-prep sprint**, Atlas tests five concrete joins:

1. Can one `meeting_id` join to the source capture, participant-consent event, recording, transcript version, and speaker-attribution result?
2. Can a reviewer identify the prompt version, model version, extraction result, confidence score, and human correction behind each Fireflies summary or analysis?
3. Can Fireflies prove tenant, workspace, user, and meeting isolation across recordings, transcripts, shared links, AI apps, and CRM integrations?
4. Can a deletion request be followed from the recording and transcript through summaries, clips, caches, exports, embeddings, and downstream CRM or workflow writes?
5. Can a customer export an immutable evidence bundle containing retention, access, consent, model, and downstream-action records for SOC 2, GDPR, or AI-governance review?

We deliver a gap map, a 15-column provenance join-table stub, a consent-and-deletion checklist, and a 30-minute walkthrough. If the first sprint is useful, the follow-on is **$497/mo** for a recurring evidence-reconstruction loop with a 15-minute monthly control check. Reply `AUDIT` and we will send the redacted stub, or reply `NOPE` and we will close the thread. The verified public inquiry channel is `support@fireflies.ai`.

— Atlas Audit Prep  
Talon Forge LLC · https://talonforgehq.github.io/atlas-store/  
Unsubscribe: atlas@talonforgehq.io

## 15-column Fireflies.ai meeting-intelligence provenance join-table

<table>
<thead><tr><th>#</th><th>Lineage column</th><th>Evidence question</th></tr></thead>
<tbody>
<tr><td>1</td><td>meeting_id</td><td>Which meeting is being reconstructed?</td></tr>
<tr><td>2</td><td>source_capture_id</td><td>Which capture produced the evidence?</td></tr>
<tr><td>3</td><td>participant_consent_event_id</td><td>What proves participant notice or consent?</td></tr>
<tr><td>4</td><td>recording_id</td><td>Which recording supplied the evidence?</td></tr>
<tr><td>5</td><td>transcript_version_id</td><td>Which transcript version was used?</td></tr>
<tr><td>6</td><td>speaker_attribution_id</td><td>How was speaker attribution established?</td></tr>
<tr><td>7</td><td>prompt_version_id</td><td>Which analysis or summary prompt ran?</td></tr>
<tr><td>8</td><td>model_version_id</td><td>Which model and deployment generated the result?</td></tr>
<tr><td>9</td><td>analysis_result_id</td><td>Which structured analysis or summary was emitted?</td></tr>
<tr><td>10</td><td>confidence_score_id</td><td>What confidence and review threshold applied?</td></tr>
<tr><td>11</td><td>human_review_event_id</td><td>Who corrected or approved the output?</td></tr>
<tr><td>12</td><td>ai_app_action_id</td><td>Which downstream AI App or workflow action occurred?</td></tr>
<tr><td>13</td><td>crm_sync_event_id</td><td>Which CRM or workspace write occurred?</td></tr>
<tr><td>14</td><td>deletion_propagation_event_id</td><td>Did deletion reach all derived artifacts and exports?</td></tr>
<tr><td>15</td><td>worm_retention_flag</td><td>What proves retention and immutable evidence handling?</td></tr>
</tbody>
</table>

**Offer:** $500 one-time audit with 48h delivery; $497/mo recurring evidence loop. **Verified channel:** support@fireflies.ai.
