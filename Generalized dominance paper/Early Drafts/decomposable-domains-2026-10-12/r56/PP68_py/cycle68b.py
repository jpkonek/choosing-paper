"""cycle68b: locate the conflict found by cycle68 (pairs of hypotheses; minimal core by deletion)."""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cycle68.py')).read().split("for k, h in H.items():")[0])
ks = list(H)
for a, b in itertools.combinations(ks, 2):
    print('%s + %s: %s' % (a, b, 'SAT' if I.sat(H[a] + H[b]) else 'UNSAT'))
# minimal core over individual literals (deletion)
lits = H['Y dominates N*-fills'] + H['N* dominates Y-fills']
if I.sat(lits):
    lits = allh
core = list(lits)
i = 0
while i < len(core):
    trial = core[:i] + core[i + 1:]
    if not I.sat(trial):
        core = trial
    else:
        i += 1
inv = {v: k for k, v in I.var.items()}
print('minimal core (%d literals):' % len(core))
nm = {T: 'T', N: 'N*', Y: 'Y'}
def show(r):
    return ' '.join('%s:%s->%s' % x for x in r)
for l in core:
    r, w = inv[l]
    print('   accept at w=%d record %s' % (w, show(r)))
