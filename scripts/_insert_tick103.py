import sys
entry_path = sys.argv[1]
log_path = sys.argv[2]
entry = open(entry_path, 'r', encoding='utf-8').read()
log = open(log_path, 'r', encoding='utf-8').read()
if '</body>' in log:
    new = log.replace('</body>', entry + '\n</body>', 1)
else:
    idx = log.rfind('</div>')
    new = log[:idx] + entry + log[idx:]
open(log_path, 'w', encoding='utf-8').write(new)
print('inserted, new size:', len(new))