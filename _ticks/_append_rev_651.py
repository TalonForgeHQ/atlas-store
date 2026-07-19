import csv, os
path = r'C:\Users\Potts\projects\atlas-store\revenue_log.csv'
header = ['date','lead','template','chunk','cohort','revenue_usd','note']
row = ['2026-07-19','651','651_vanta.md','chunk_647','ai_compliance_automation','0',
       "Vanta ai_compliance_automation CLOSES the cohort at 5/5 after Drata 647 + Scrut 648 + Secureframe 649 + Sprinto 650 - Vanta the leading Agentic Trust Platform + AI-native evidence mapping + 12K+ customers + Sequoia Capital-backed + Christina Cacioppo CEO and co-founder + privacy@vanta.com verified live 2026-07-19 on official Vanta privacy page canonical privacy/DPA inbox. Differentiated wedge: AGENTIC-TRUST + AI-NATIVE-EVIDENCE-MAPPING + SEQUOIA-BACKED + TRUST-CENTER-PUBLISHING + QUESTIONNAIRE-AUTOMATION (the agentic-first customer base + Sequoia-led rounds + 300+ integrations + Trust Center publishing surface that converts continuous-compliance paperwork into a customer-facing trust asset at agentic-AI scale). Tier-1 evidence wedge: per-control + per-evidence-collection-timestamp + per-reviewer + per-auditor-access + per-framework-version + per-mapping-rule + per-exception + per-remediation evidence schema + Vanta-AI-output provenance + per-prompt + per-model + per-tool-version + per-incident + per-human-override logging + ISO 42001 AIMS-mapping ready + OWASP LLM Top-10 mitigation runbook + multi-tenant evidence-isolation in LLM retrieval layer + deletion-cascade SLA + provable-purge-log. Compliance map: SOC 2 Type II + ISO 27001 + ISO 27701 + ISO 42001 + GDPR + UK GDPR + HIPAA + PCI DSS + NIST CSF + CCPA/CPRA + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD + EU AI Act Aug 2 2026 ready for high-risk-system obligations. Offer 500/48h audit + 497/mo MRR quarterly refresh. SMTP still blocked. COHORT-FULL marker: ai_compliance_automation closed at canonical N=5."]

if not os.path.exists(path):
    with open(path,'w',newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        w.writerow(header)

with open(path,'a',newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    w.writerow(row)

with open(path,'r') as f:
    rows = list(csv.reader(f))
print('revenue_log.csv rows now:', len(rows))
print('last row:', rows[-1])
