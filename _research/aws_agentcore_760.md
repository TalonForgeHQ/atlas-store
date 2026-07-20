# Lead 760 evidence — Amazon Web Services / Amazon Bedrock AgentCore

**Verified:** 2026-07-21 UTC
**Cohort:** `ai_agent_sandbox_infrastructure` cycle-2 CLOSER sibling #5/5
**Company:** Amazon Web Services (AWS), a segment of Amazon.com, Inc.
**Website:** https://aws.amazon.com/bedrock/agentcore/
**Commercial route:** `FORM:https://aws.amazon.com/contact-us/sales-support/`

## First-party product proof

Source: https://aws.amazon.com/bedrock/agentcore/ — HTTP 200 on 2026-07-21.

Exact current positioning captured from the live page:

- “Amazon Bedrock AgentCore”
- “The platform for production AI agents. Any framework. Any model. Secure at scale.”
- “One platform to build, connect and optimize agents.”
- AgentCore handles connecting agents to systems, securing tool calls, debugging unexpected behaviors, and scaling without rebuilding everything.
- “Confidence and control” copy says AgentCore helps authorize agent tool calls, trace decisions, and enforce security boundaries when agents behave unexpectedly.
- “Breadth and depth” copy says teams can build, connect, observe, evaluate, experiment, and scale in one place.
- The page publishes a Get started with the AgentCore CLI route and an AgentCore console route.

## Company, founder, and current AWS leadership proof

Source: Amazon.com, Inc. 2025 Form 10-K, filed 2026-02-06:
https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm

The filing states:

- Amazon.com, Inc. organizes operations into North America, International, and Amazon Web Services (“AWS”) segments.
- “Mr. Bezos founded Amazon.com in 1994.”
- Jeffrey P. Bezos is Executive Chair.
- Andrew R. Jassy is President and Chief Executive Officer of Amazon.com, Inc.
- Matthew S. Garman has served as CEO Amazon Web Services since June 2024.

Founder encoding is therefore precise: **Jeffrey P. Bezos — founder of Amazon.com, Inc., the parent company whose AWS segment ships Amazon Bedrock AgentCore.** This evidence does not mislabel him as an AgentCore product founder.

## Route proof and safety

Source: https://aws.amazon.com/contact-us/sales-support/ — HTTP 200 on 2026-07-21.

The page is titled “Contact AWS Sales support” and states: “Please complete the form to reach an Amazon Web Services sales representative.” It requests contact and employment information, including job role.

No general-business inbox was guessed. Privacy, legal, security-disclosure, abuse, support, press, careers, and investor routes are excluded. `FORM:` is a transport sentinel; no SMTP event or form-submission event is created by this tick.

## Distinct closer wedge

Fireworks 756 owns specialized serverless/dedicated inference; Replicate 757 owns Cog container/model-catalog inference; Together AI 758 owns dedicated inference/GPU-cluster AI cloud; Anyscale 759 owns Ray/KubeRay distributed workloads. Amazon Bedrock AgentCore closes cycle-2 with the hyperscaler production-agent control-plane lane: framework/model portability, system connection, tool-call authorization, decision tracing, security-boundary enforcement, observe/evaluate/experiment lifecycle, and scaling without rearchitecture.

Five procurement joins staged for the $500/48h evidence-gap map:

1. Framework/model/agent build → deployed runtime/version receipt.
2. Agent → connected system → tool call → authorization/policy-decision receipt.
3. Unexpected behavior → decision trace → enforced security boundary → operator action receipt.
4. Build/connect/observe/evaluate/experiment → release decision → scale event receipt.
5. Export/deletion proof across agent configuration, traces, evaluation artifacts, connection metadata, and operational logs.

**No outreach or revenue claim:** SMTP and authenticated form submission remain gated. No email, sales-form submission, delivery, payment, or revenue is claimed.
