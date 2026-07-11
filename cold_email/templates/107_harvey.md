**Subject:** Harvey + ABA Model Rule 1.6 — 5 audit gaps your QSA will ask about in 2026

Hi Winston,

Your Series C at ~$3B led by Sequoia + Kleiner Perkins + the OpenAI Startup Fund is the strongest signal yet that legal-domain AI agents have crossed from "experimental" to "table stakes" at the AmLaw 200. The Allen & Overy + PwC + A&O Shearman + Citi + GS + JPM + Bridgepoint + HSF + DLA Piper logo stack means Harvey is now embedded in the privilege-handling path of every major cross-border deal and litigation in 2026. The forensic question every AmLaw 200 CISO + GRC lead + Conflicts Counsel is asking their QSA right now is: **does the LLM layer preserve or waive attorney-client privilege + work-product?**

Here are 5 audit gaps that the public material doesn't address but that every AmLaw 200 SOC 2 Type II + ABA Standing Committee on Ethics + EU privileged-communications auditor will ask Harvey to evidence in 2026:

1. **Privilege preservation across the LLM boundary** — ABA Model Rule 1.6 + FRCP 502(d) + EU privileged communications under national-bar rules require that the join-table between the firm's privileged corpus + the Harvey retrieval decision + the produced draft + the LLM-provider's ephemeral-decryption log be reconstructible so that the firm can prove *on a per-matter, per-query basis* that no inadvertent disclosure to OpenAI's infrastructure waived privilege. The audit artifact: a per-query privilege-decision log with cryptographic binding between (a) the matter ID, (b) the retrieved-doc IDs + their privilege stamps, (c) the prompt sent to the LLM, (d) the LLM response, (e) the produced draft, (f) the firm's privilege-log entry. Without (a)-(f) cryptographically bound, the firm cannot defend a clawback under FRCP 502(b).

2. **Conflict-of-interest screening surface** — ABA Model Rule 1.7 + 1.9 + IRPC 1.10 imputation require that any agent operating on behalf of a firm across matters maintain a real-time conflict-screening surface for adverse-position detection + prior-representation screening. When Harvey is shared across the firm's matters, the agent's retrieval-decision must be screened against the firm's conflicts database per query. Audit artifact: per-query conflict-check log with the screening-decision + the conflict-DB lookup + the screening-decision-timestamp.

3. **Work-product doctrine preservation** — FRCP 26(b)(3) + Hickman v. Taylor require that mental impressions + legal theories + strategies prepared in anticipation of litigation be protected. When Harvey is used for active litigation matters, the prompt + retrieval-decision log + the agent's intermediate reasoning trace must be sequestered from opposing-counsel discovery. Audit artifact: per-matter work-product-sequestration policy + technical control that prevents the prompt log from being discoverable in the firm's normal e-discovery export (it must live in a separate, access-controlled store under attorney-work-product privilege).

4. **Cross-jurisdiction unauthorized practice of law (UPL) boundary** — Harvey is deployed at firms in 50+ jurisdictions, but the agent must not cross the UPL line by giving jurisdiction-specific legal advice without a licensed-attorney-in-that-jurisdiction loop. When Harvey advises on a California matter from a New York attorney's prompt, the agent's response must trigger a jurisdiction-routing layer that escalates to a CA-bar-licensed attorney. Audit artifact: jurisdiction-detection log per query + escalation-routing log + per-jurisdiction licensed-attorney-loop proof.

5. **Multi-region + multi-tenant privilege-log residency** — AmLaw 200 firms have matters in the US, UK, EU, APAC. The Harvey audit log + privilege-decision log + retrieval-decision log must be partitionable by jurisdiction so that a UK SRA + EU GDPR + US state-bar regulator audit can each pull their jurisdiction's evidence without cross-jurisdictional data transfer. Audit artifact: per-jurisdiction audit-log partition with cryptographic binding to the per-query privilege-decision.

I'm running a 48-hour, fixed-price **$500 audit** that delivers all five artifacts as a working reference implementation + the per-jurisdiction audit-log partition design + the work-product-sequestration policy + the cross-jurisdiction UPL escalation layer + a one-page memo for your QSA. References: chunks 34 (SOC 2 AI agent), 35 (CX-AI), 36, 39 (permission inheritance), 40 (IT-helpdesk), 42 (voice-AI) — all live at talonforgehq.github.io/atlas-store.

Worth a 30-min call this week?

— Atlas
