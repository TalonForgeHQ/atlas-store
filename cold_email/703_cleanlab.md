# Lead 703 — Cleanlab evidence package

## Verified company facts

- **Company:** Cleanlab, Inc.
- **Website:** https://cleanlab.ai
- **Commercial route:** `sales@cleanlab.ai`
- **Route evidence:** the exact address is published on Cleanlab's first-party Contact page: https://cleanlab.ai/contact
- **Public handle:** `@cleanlabai`, linked from Cleanlab's first-party site.
- **Founder evidence:** https://www.cleanlab.ai/about/ labels the team section **Our Founders** and names:
  - Curtis Northcutt — CEO
  - Jonas Mueller — Chief Scientist
  - Anish Athalye — CTO
- **Current company context:** the first-party About page displays the notice “Cleanlab has been acquired by Handshake AI.”
- **Verification date:** 2026-07-20.

## Cohort fit

Cleanlab is sibling #4/5 in `ai_evidence_pack_automation`, after Mistral AI 700, WRITER 701, and Cohere 702. It adds a non-overlapping quality-and-reliability wedge: evidence generated while an AI agent's unsafe, inaccurate, or low-quality output is detected, diagnosed, remediated, and re-evaluated.

## Evidence-pack wedge

A procurement-ready Cleanlab evidence export should join:

1. `cleanlab_project_id`
2. `agent_application_id`
3. `agent_release_id`
4. `model_provider_and_version`
5. `prompt_or_policy_version`
6. `evaluation_dataset_snapshot`
7. `input_record_hash`
8. `output_record_hash`
9. `quality_issue_type`
10. `quality_score_and_threshold`
11. `root_cause_finding_id`
12. `guardrail_or_remediation_version`
13. `human_review_and_approval_id`
14. `post_remediation_evaluation_result`
15. `deployment_environment_and_tenant_id`
16. `source_url_owner_timestamp_and_exception_status`

That release-pinned chain is the commercial audit wedge: turn Cleanlab's AI reliability controls into one buyer-facing packet that proves which output failed, why it failed, which control changed, who approved the change, and whether the repaired release passed the same evaluation set.

## Five audit questions

1. Can a customer export the exact model, agent release, prompt/policy, dataset snapshot, and Cleanlab detector versions used for a material evaluation?
2. Does each flagged response preserve immutable input/output hashes, issue type, score, threshold, and root-cause finding?
3. Can the export join each remediation or guardrail change to its owner, approval, deployment, and post-change evaluation result?
4. When a threshold, detector, model, dataset, or policy changes, can buyers retrieve the prior state and affected runs?
5. Can procurement receive all of those joins as one machine-readable bundle with first-party source URLs, control owners, timestamps, exceptions, and remediation status?

## Offer

- **$500 / 48 hours:** evidence-gap map for one Cleanlab-backed agent workflow.
- **$497/month:** material-change evidence refresh.
- **$2,485/month:** five-vendor portfolio using the YanXbt operator pattern.

## Route-safety note

`sales@cleanlab.ai` is a first-party commercial Sales route. Do not substitute Cleanlab's published legal/privacy channel for this commercial offer.
