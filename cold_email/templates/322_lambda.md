# Lead 232 — Lambda

**Vertical:** ai_infra
**Tier:** 1
**Website:** https://lambda.ai/
**Founders:** Stephen Balaban and Michael Balaban
**Verified public inbox:** privacy@lambda.ai

---

**Subject:** 5 audit questions for Lambda's AI-factory evidence chain

Hi Stephen + Michael,

Lambda spans AI factories, GPU clusters, model training, fine-tuning, and inference. For an enterprise buyer, that creates one high-value diligence question: can every production result be reconstructed from tenant and request through model artifact, cluster and hardware route, deployment, policy decision, cost, and downstream action?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test on one Lambda training-to-inference route:

1. **End-to-end provenance:** Can one export join tenant, API key, request or training-step ID, model and weights hash, prompt and output hashes, cluster and node IDs, GPU type, region, scheduler route, policy decision, downstream action, latency, token usage, GPU time, and attributed cost?
2. **Model and training-data supply chain:** Are base models, fine-tune corpora, checkpoints, containers, drivers, CUDA libraries, orchestration manifests, and deployment promotions tied to signed versions, license evidence, approvals, and reproducible rollback points?
3. **Hostile input and workload isolation:** What prevents prompt injection, poisoned training data, malicious model files, unsafe containers, cache poisoning, compromised notebooks, or tool output from crossing the serving boundary or influencing another tenant's workload?
4. **Tenant, secret, and hardware isolation:** Can customers retrieve tests proving separation across clusters, GPU memory, KV caches, storage, networks, service accounts, API tokens, encryption keys, regions, support access, and dedicated versus shared inference paths?
5. **Incident, retention, and deletion reconstruction:** After a bad output, vulnerable model, poisoned corpus, cross-tenant exposure, scheduler fault, or deletion request, can Lambda identify every affected training run and inference call, preserve WORM-capable evidence, and prove rollback or deletion across checkpoints, caches, replicas, logs, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 9, 12, 14, and 15; GDPR Articles 17, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; NIST SSDF; and SLSA**. I test one live request-to-cluster-to-result path end to end rather than sending a generic checklist.

**Why Lambda specifically:** combining AI-factory infrastructure with training and inference removes handoffs, but it also concentrates model, workload, hardware, tenant, and cost evidence in one operational plane. Buyers will want proof that the consolidation improves auditability as well as performance.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Lambda training-to-inference route tested end to end
