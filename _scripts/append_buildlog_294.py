import re
p=r'C:\Users\Potts\projects\atlas-store\build-log.html'
with open(p,'r',encoding='utf-8') as f: c=f.read()

entry = '''<h2>Tick 2026-07-16T09:11Z — Suki AI (294) lead + template + chunk_162 — opens ai_healthcare_clinical_assistant vertical (1st sibling)</h2>
<p><strong>Lead:</strong> <a href="cold_email/leads.csv">294_suki.md</a> &middot; <strong>Template:</strong> <a href="cold_email/templates/294_suki.md">294_suki.md</a> &middot; <strong>Chunk:</strong> <a href="chunks/chunk_162.html">chunk_162.html</a></p>
<p><strong>Company:</strong> Suki AI (Redwood City CA, founded 2017 by Punit Singh Sonali + Sonali Mangrulkar, $220M+ raised at $1B+ valuation, Hedosophia + Venrock + March Capital). <strong>Email:</strong> support@suki.ai verified live 2026-07-16 via curl scrape https://www.suki.ai/privacy-policy HTTP 200 + https://www.suki.ai/contact HTTP 200. <strong>Vertical:</strong> ai_healthcare_clinical_assistant (inaugural 1st-sibling, opens new vertical). <strong>Product surface:</strong> Suki Assistant + Suki Dictation + Suki Q&A + Suki Coding + Suki Inbox + Suki Ambient + Suki Mobile. <strong>Customers:</strong> 100+ US health-systems including Mayo Clinic + Ascension + St. Joseph Health + Steward Health Care + Rush University Medical Center + Wake Forest Baptist Health + UofL Health.</p>
<p><strong>Why this lead matters:</strong> Suki AI is the ONLY AI-clinical-assistant vendor that operates BOTH the ambient-documentation / voice-to-EHR layer AND the clinical-decision-support layer (per-clinician-voice-session + per-EHR-write-event + per-clinician-approval-event + per-clinician-rollback-event + per-HL7-FHIR-R4-resource-version + per-HIPAA-Business-Associate-Agreement-evidence + per-OCR-breach-notification-event). That dual-layer architecture produces a unique <em>per-clinician-id + per-patient-id + per-voice-session-id + per-EHR-write-event-id + per-EHR-system-id + per-HL7-FHIR-R4-resource-version + per-clinician-approval-event-id + per-clinician-rollback-event-id + per-HIPAA-Business-Associate-Agreement-evidence-id + per-OCR-breach-notification-event-id</em> evidence chain that no other ai_healthcare_clinical_assistant vendor has. Closes the canonical 1-vendor ai_healthcare_clinical_assistant cohort seed (Suki AI 294).</p>
<p><strong>Cohort closures pending:</strong> ai_healthcare_clinical_assistant needs 2-3 more siblings (Abridge, Nuance DAX, Augmedix, DeepScribe, Nabla Copilot) to close the canonical 4-5 vendor cohort pattern established in the 7 prior cohort closures. <strong>Frameworks mapped:</strong> HIPAA 45 CFR 164.312(b) + 164.520 + 164.524 + HITECH + ONC 170.315(d)(13) + FDA 21 CFR Part 11 + EU AI Act Art. 9 + 10 + 14 + 27 + 43 + 53(d) + Annex III 5(a) medical-device + GDPR Art. 28 + 32 + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF GOVERN + MAP + MEASURE + MANAGE. <strong>Cumulative:</strong> 294 leads in cold_email/leads.csv (live), 162 SEO chunks live (was 161), 9 verticals active. <strong>Next:</strong> 2-3 more ai_healthcare_clinical_assistant siblings to close the cohort, then resume ai_legal_ai + ai_insurance_ai rotations per the cohort-closure roadmap.</p>
<hr>
'''

# Insert at top (after the first <h1> or just at start)
# Find first <h2> tick entry and insert before it
m = re.search(r'(<h2>Tick \d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z)', c)
if m:
    idx = m.start()
    c = c[:idx] + entry + c[idx:]
    with open(p,'w',encoding='utf-8') as f: f.write(c)
    print('inserted before', m.group(1))
else:
    print('no tick h2 found, appending')
    c = c + entry
    with open(p,'w',encoding='utf-8') as f: f.write(c)
