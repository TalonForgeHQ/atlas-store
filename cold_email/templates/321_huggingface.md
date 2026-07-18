# Lead 231 — Hugging Face

**Vertical:** ai_infra
**Tier:** 1
**Website:** https://huggingface.co/
**Founders:** Clément Delangue (CEO), Julien Chaumond, and Thomas Wolf
**Verified public inbox:** privacy@huggingface.co
**Evidence re-checked:** 2026-07-18 — Hugging Face's live Privacy Policy exposes the public route above; the live homepage and Hub security documentation cover Models, Datasets, Spaces, Inference Endpoints, access controls, and audit logs. TechCrunch's 2023 funding profile identifies Delangue as co-founder and CEO and says he launched Hugging Face with Chaumond and Wolf.

---

**Subject:** 5 audit questions for Hugging Face's Hub-to-inference evidence chain

Hi Clément + Julien + Thomas,

Hugging Face connects community Models, Datasets, Spaces, and managed Inference Endpoints in one platform. For an enterprise buyer, that creates a narrow diligence question: can one production result be reconstructed from the exact Hub artifacts and permissions through deployment, routing, policy decisions, and downstream action?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test on one Hub-to-inference route:

1. **Artifact-to-result provenance:** Can one export join organization and user IDs, access token or service account, model and dataset repositories, commit hashes, model and dataset cards, Space or Endpoint deployment, prompt and output hashes, provider and hardware route, safety decision, downstream action, latency, token usage, and attributed cost?
2. **Model, dataset, and application supply chain:** Are community uploads, gated assets, licenses, dependencies, containers, safetensors, adapters, quantizations, Space code, and deployment promotions tied to signed versions, review decisions, scanners, approvals, and reproducible rollback points?
3. **Hostile community content:** What prevents a poisoned model, dataset, model card, Space repository, pull request, prompt, or tool response from escalating authority, exfiltrating secrets, crossing a trust boundary, or changing an agent's downstream decision?
4. **Tenant, token, and runtime isolation:** Can enterprise customers retrieve evidence proving separation across organizations, private repositories, resource groups, Spaces, Inference Endpoints, caches, GPU memory, secrets, encryption keys, regions, support access, and third-party inference providers?
5. **Incident, retention, and deletion reconstruction:** After a malicious upload, vulnerable dependency, leaked token, unsafe output, provider fault, or deletion request, can Hugging Face identify every affected clone, deployment, cache, derivative, inference call, and downstream action, preserve WORM-capable evidence, and prove quarantine, rollback, or deletion?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 9, 12, 14, 15, and 53; GDPR Articles 17, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; NIST SSDF; and SLSA**. I test one live artifact-to-deployment-to-result path end to end rather than sending a generic checklist.

**Why Hugging Face specifically:** the Hub collapses software supply chain, model and dataset governance, interactive applications, and production inference into one ecosystem. That removes handoffs for builders, but enterprise buyers will want proof that permissions, provenance, isolation, and deletion stay continuous across every layer.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Hugging Face Hub-to-inference route tested end to end
