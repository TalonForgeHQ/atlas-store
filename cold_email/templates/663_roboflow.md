**Subject:** quick question re Roboflow's per-deployment-environment model-export-versioning attestation

**Body:**

Hi Joseph, Brad —

Five questions before any pitch:

1. **Per-deployment-environment model-versioning attestation** — when a Fortune-100 manufacturer ships a Roboflow-Inference deployment to a Jetson Orin line, can you hand the audit committee a single JSON blob that pins: per-Roboflow-Workflows-pipeline-version + per-Roboflow-Workflows-block-version + per-Roboflow-Train-custom-model-checkpoint + per-ONNX / TensorRT / CoreML / OpenVINO export-version + per-Roboflow-Inference-runtime-version + per-edge-Jetson-L4T-version + per-deployment-region + per-annotation-team-member? **Most CV vendors can't produce that blob — Roboflow's open-source Inference + per-platform export means you can.** That's the gap your Fortune-100 procurement teams hit today.

2. **EU AI Act Art. 6 high-risk-CV-mapping** — for manufacturing-defect-detection + healthcare-imaging + autonomous-vehicle-perception + aerospace-defense-detection, the EU AI Act Annex III §1(b) biometric-categorization + §5(a) predictive-policing + §6 emotion-recognition-in-education-and-workplace triggers the strictest-tier-high-risk-CV-classification path. Are your customer deployments mapping each Roboflow project to the Annex III + Art. 6 risk-category today, or is the customer left to map it themselves?

3. **NIST AI RMF 600-1 2024 + ISO/IEC 42001 AIMS** — the 2024 NIST AI RMF and ISO/IEC 42001 are the canonical cv risk-management standards Fortune-100 procurement teams are now requiring. Does Roboflow publish a per-deployment RMF map + ISO 42001 AIMS evidence binder? If not, every Fortune-100 customer rebuilds it from scratch, which is exactly what slows the procurement cycle by 6-10 weeks.

4. **GDPR Art. 9 biometric-data DPIA** — when a Roboflow customer trains a face-recognition or body-measurement or emotion-recognition CV model on Roboflow, the training data + the inference data become biometric data under GDPR Art. 9 + UK GDPR Art. 9 + Illinois BIPA + Texas CUBI + Washington biometric-privacy. Does Roboflow surface a per-deployment biometric-DPIA-template + BIPA-cascade evidence packet, or is the customer left to write their own?

5. **OWASP ML Top-10 + MITRE ATLAS mitigation runbook** — for production CV models deployed via Roboflow Inference, the canonical adversarial-attack-surface is OWASP ML01 input-manipulation + ML02 training-data-poisoning + ML05 model-theft-via-API + ML06 backdoor-on-pre-trained-weights + ML07 inadequate-fairness + MITRE ATLAS adversarial-patch on manufacturing-defect + physical-adversarial-example on AV-perception + model-inversion-attack on biometric-classifier. Does Roboflow ship an OWASP-ML + MITRE-ATLAS mitigation runbook + a per-deployment adversarial-test-suite, or is the customer left to build one?

The reason I ask — I run a 14-document evidence-gap audit for AI/ML vendors selling into Fortune-100 + EU + UK + regulated-US-state procurement cycles. Most CV vendors I've audited show a 6-10 week gap between "we have SOC 2 + ISO 27001" and "we have an Art. 6 + Art. 14 + Art. 26 + Art. 50 + Annex IV deployer-readiness evidence binder the procurement committee signs off on." Roboflow has the developer-infrastructure surface (per-deployment-region + per-tenant-custom-trained-model-lineage + per-Roboflow-Workflows-pipeline-version + open-source pip-install inference + ONNX/TensorRT/CoreML/OpenVINO export-versioning cascade) to close that gap — but the per-deployment evidence binder isn't typically published.

I'm doing a $500 / 48h evidence-gap audit + a $497/mo quarterly refresh retainer for ai_vision_computer_vision cohort siblings (Roboflow + Landing AI + Voxel51 + Encord + Scale Rapid + Roboflow 3.0 etc.). 15-min call to walk through the 14-doc binder?

PS — if Roboflow is already running an in-house Art. 6 + Art. 14(4) + Art. 50 + NIST AI RMF + OWASP ML Top-10 + MITRE ATLAS + Illinois BIPA + GDPR Art. 9 binder that maps to the procurement committees you sell into, I'd genuinely like to learn the shape of it. Most AI/ML vendors I audit are 30-50% of the way through and the audit lets them ship the remaining binder in 48h.

— [Sender]
Talon Forge LLC | atlas-store-sierra-662 cohort | $500/48h audit + $497/mo refresh