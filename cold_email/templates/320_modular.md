# Lead 230 — Modular

**Vertical:** ai_infra
**Tier:** 1
**Website:** https://www.modular.com/
**Co-founders:** Chris Lattner (CEO) and Tim Davis (President)
**Verified public inbox:** hello@modular.com

---

**Subject:** 5 audit questions on Modular’s MAX inference evidence chain

Hi Chris + Tim,

Modular’s advantage is unusually broad: MAX spans model execution, GPU kernels, serving, and deployment while Mojo reaches down into the code that builds the inference path. For an enterprise buyer, that creates one critical diligence question: can every production result be reconstructed from request and model version through compiled graph, hardware route, serving decision, and downstream action?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test against Modular:

1. **Request-to-result provenance:** Can one export join tenant, API key, request and trace IDs, model and weights hash, prompt and completion hashes, MAX graph version, Mojo module and compile artifact, serving route, GPU type, latency, token and compute cost, output policy decision, and downstream action?
2. **Compiler and graph supply chain:** Are Mojo packages, custom ops, MAX graph transforms, model artifacts, containers, and deployment manifests signed and reproducible, with SBOMs, dependency provenance, promotion approvals, and rollback evidence?
3. **Hostile model and request input:** What prevents poisoned model files, prompt injection, malformed tensors, unsafe custom kernels, graph manipulation, cache poisoning, or tool output from crossing the inference boundary or altering a downstream agent decision?
4. **Tenant and hardware isolation:** Can customers retrieve tests proving isolation across dedicated endpoints, shared serving pools, GPU memory, KV caches, notebooks, logs, model stores, secrets, encryption keys, regions, and support access?
5. **Incident and deletion reconstruction:** After a bad output, routing fault, cross-tenant exposure, vulnerable kernel, or model withdrawal, can Modular identify every affected request and derivative, preserve WORM-capable incident evidence, and prove deletion or rollback across caches, replicas, logs, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 9, 12, 14, and 15; GDPR Articles 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; SLSA; and NIST SSDF**. I test one live request-to-MAX-to-hardware route end to end rather than sending a generic checklist.

**Why Modular specifically:** a unified stack can remove the fragmented handoffs that make inference operations slow, but it also concentrates compiler, graph, model, serving, hardware, and tenant evidence in one control plane. Buyers will want proof that this consolidation improves auditability as well as performance.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live inference route tested end to end
