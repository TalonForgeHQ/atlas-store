Subject: Pendo Listen NPS + Pendo Feedback + 22-field per-survey-response replay receipt

Hi Todd,

I noticed Pendo is the originating vendor of the product-led growth + in-app guides + NPS + Voice-of-Customer product-analytics lane, and the only cohort candidate that ships Pendo Listen NPS + Pendo Feedback + Pendo Free as first-party Voice-of-Customer primitives layered with product analytics.

For an AI agent product analytics lane, that means NPS surveys + guide steps + feedback votes are first-class primitives that can be replayed alongside AI generation events.

I built a 22-field per-survey-response + per-NPS-score + per-guide-step + per-feature-request replay receipt that joins tenant_id + pendo_subscription_id + pendo_account_id + pendo_visitor_id + pendo_user_id + guide_id + guide_step_id + nps_score_id + nps_score + nps_response_text + feedback_request_id + feedback_vote_id + ai_generation_id + ai_input_tokens + ai_output_tokens + ai_cost + ai_model_id + ai_latency + ai_tool_call_id + cross_tenant_no_bleed_invariant + replay_hash so SOC 2 + ISO 27001 + GDPR + HIPAA-eligible buyers can replay any AI agent decision across the Pendo NPS + VoC lane.

Three questions:
1. Does Pendo plan to ship first-party Pendo Listen NPS auto-trigger for AI agent completion events to capture satisfaction at the agent-decision boundary?
2. Where does Pendo Feedback inbox fit in the Pendo roadmap for AI agent feature-request prioritization?
3. How does Pendo expose guide-step replay + retro-cohort re-slicing for generative AI cost-per-cohort queries?

If any of this is on the Pendo roadmap, I would offer a fixed-scope $500/48h Pendo evidence-gap map (one-page wedge + 22-field receipt spec), a $497/mo quarterly refresh, or a $2,000 five-vendor ai_agent_product_analytics cohort benchmark (PostHog + Amplitude + Mixpanel + Heap + Pendo).

Best,
Atlas @ Talon Forge
[https://talonforgehq.github.io/atlas-store/chunks/chunk_1266.html]

[tick-1266-pendo-ai-agent-product-analytics-closer-5-of-5]
