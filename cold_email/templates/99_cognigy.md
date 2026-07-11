Subject: NiCE Cognigy acquisition — 4 audit questions your QSA will ask in Q4

Hi Philipp / Sascha,

Congrats on the NiCE close. I work with CX-AI vendors on the post-acquisition
SOC 2 + EU AI Act + ISO 42001 audit gap that shows up the quarter after a
parent company gets assigned a new audit cycle.

The 4 questions NiCE's QSA + a Big-4 EU AI Act conformity assessor will
ask Cognigy specifically (not generic CX-AI questions):

1. **Cross-stack action join-table.** A Cognigy agent calls NiCE CXone +
   a CRM + a billing system + an LLM. When a customer disputes
   "the agent said X but did Y," can you reconstruct the full call graph
   from a single conversation_id across all 4 systems in under 60
   seconds? If no, you have a SOC 2 CC7.2 + EU AI Act Art. 12 (logging)
   gap that the parent company's integrated audit will surface.

2. **Multilingual PII deletion propagation.** Cognigy ships 100+ languages.
   When a German customer invokes GDPR Art. 17, you need to delete their
   transcript + prompt log + completion log + tool payloads + NiCE CXone
   recording + eval set + any fine-tune data in 30 days. We see most
   vendors fail this at language #4 because translation pipelines
   duplicate PII into side tables nobody tracks.

3. **EU AI Act high-risk classification memo.** A customer-service agent
   that "materially influences" decisions (refunds, escalations,
   cancellations) is Annex III high-risk under the EU AI Act. You need a
   written conformity assessment + post-market monitoring plan +
   fundamental-rights impact assessment. Most CX vendors don't have this
   memo at all.

4. **Acquisition-locked prompt-version history.** When NiCE ships a
   Cognigy v8 update that changes escalation behavior, can you A/B against
   the v6 prompt that was live for the customer who just escalated to
   legal? If your prompt-template store isn't SHA-pinned per
   conversation, you can't defend the prompt-as-code drift claim.

I do a 24h audit ($500, flat) that produces a 1-page memo answering each
of these with the specific evidence your QSA will request. Happy to send
the memo outline + a sample from a Sierra / Decagon / in-house
LangChain stack engagement.

Want me to send it?

— Atlas
Talon Forge

P.S. If the EU AI Act deadline (Aug 2026 for high-risk) is your
trigger, I can have the conformity memo skeleton to you in 48h.