"""core72: UNSAT core over fill requirements (selector literal per fill), lazy (TC) as in lib72b.
Every clause other than the fill requirements is an axiom instance on the sub-universe, so the extracted core
is a set of fill-domination requirements that NO relation satisfying the axioms (with these installed models
defended and protected) can meet simultaneously.  Env as sat72b."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inst72 import *
src_txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sat72b.py')).read()
exec(src_txt.split('REQ = os.environ')[0])
sels, info = [], {}
for s in src:
    for k in (1, 2, 3):
        for f in B.F[(s, k)]:
            E = [j for j in range(len(names)) if f[j] != B.M[s][j]]
            cand = [x for x in idx if B.M[x] != f and not all(B.M[x][j] == 'A' for j in E) and viable(B.M[x], f)]
            if not cand: continue
            sv = B.newvar(); sels.append(sv); info[sv] = (s, k, [names[j] for j in E], cand)
            for c in B.dominated_by_some(f, [B.M[x] for x in cand]):
                B.I.add([-sv] + c)
I = B.I
def solve(assum):
    while True:
        if not I.solver.solve(assumptions=assum):
            return False
        mdl = set(x for x in I.solver.get_model() if x > 0)
        viol = I.violations(mdl)
        if not viol:
            return True
        for (a, b, c, w) in viol:
            X = [(a, b), (b, c), (c, a)]
            base = [-int(I.Vw[w - 1, x, y]) for (x, y) in X]
            for (x, y) in X:
                I.add(base + [int(I.Vw[w - 1, y, x])]); I.ntc += 1
r = solve(sels)
print('all %d fill requirements: %s (TC %d, %.0fs)' % (len(sels), 'SAT' if r else 'UNSAT', I.ntc, time.time() - t0), flush=True)
if not r:
    core = list(I.solver.get_core())
    # deletion-based minimisation
    i = 0
    while i < len(core):
        trial = core[:i] + core[i + 1:]
        if not solve(trial):
            core = [x for x in I.solver.get_core()] if I.solver.get_core() else trial
            core = [x for x in core if x in info]
        else:
            i += 1
    print('minimal core: %d fill requirements' % len(core))
    for x in core:
        s, k, E, cand = info[x]
        print('   source %s class %d fill on %s ; candidates %s' % (s, k, E, cand))
