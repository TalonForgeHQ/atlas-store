"""Stage all atlas-store artifacts and commit + push for tick 1340Z."""
import subprocess, sys

REPO = r"C:\Users\Potts\projects\atlas-store"

def run(args, **kw):
    r = subprocess.run(["git", "-C", REPO] + args, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print(f"ERR git {' '.join(args)}: {r.stderr}", file=sys.stderr)
    return r

# 1) status (what's going to be committed)
r = run(["status", "--porcelain"])
print("STATUS:")
for line in r.stdout.splitlines()[:30]:
    print("  ", line)
print(f"... {len(r.stdout.splitlines())} lines total")
