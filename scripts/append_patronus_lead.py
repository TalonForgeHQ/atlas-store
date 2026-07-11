import csv
with open(r'C:\Users\Potts\AppData\Local\Temp\patronus_tier_part1.txt','r',encoding='utf-8') as f:
    p1 = f.read().strip()
with open(r'C:\Users\Potts\AppData\Local\Temp\patronus_tier_part2.txt','r',encoding='utf-8') as f:
    p2 = f.read().strip()
tier = p1 + p2
row = {'index':'157','name':'Patronus AI','handle':'@PatronusAI','email':'security@patronus.ai','vertical':'ai_agents_infra','tier':'1','template':'237_patronus.md','tier_reason':tier}
with open(r'C:\Users\Potts\projects\atlas-store\cold_email\leads.csv','a',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['index','name','handle','email','vertical','tier','template','tier_reason'], quoting=csv.QUOTE_ALL)
    w.writerow(row)
# verify
with open(r'C:\Users\Potts\projects\atlas-store\cold_email\leads.csv','r',encoding='utf-8') as f:
    lines = f.readlines()
print(f'Total lines now: {len(lines)}')
print(f'Last row char count: {len(lines[-1])}')
# Parse last line back as CSV to verify
import csv as _csv
with open(r'C:\Users\Potts\projects\atlas-store\cold_email\leads.csv','r',encoding='utf-8') as f:
    reader = _csv.DictReader(f)
    rows = list(reader)
print(f'Parsed rows: {len(rows)}')
print(f'Last row: index={rows[-1]["index"]} name={rows[-1]["name"]} email={rows[-1]["email"]} template={rows[-1]["template"]}')
print(f'Tier reason length: {len(rows[-1]["tier_reason"])}')