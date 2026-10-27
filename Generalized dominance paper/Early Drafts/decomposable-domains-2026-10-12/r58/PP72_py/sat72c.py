"""sat72c: rich installed set (loop at scale b, plus moves C_{m + t delta_k} for every source m, class k and every move
factor in CMOVE), fills of all three classes of the loop members, optional splices between installed models, every
requirement 'dominated by SOME installed model' (disjunctive; candidates pre-screened by the agreement obstruction
and strict-(G) viability, both axiom-level).  Lazy (TC) with full final check (lib72b).  Reports SAT/UNSAT, a minimal
core on UNSAT, and on SAT the dominator classes used and the verdicts among loop members.
Env: SCALE=5/4 CMOVE=5/4,17/16 FSRC=T,C1,C2 SPL='T:C1,C1:C2,C2:T' SPLR=1 MAXR=1"""
import sys, os, time, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inst72 import *
t0 = time.time()
b = F(os.environ.get('SCALE', '5/4'))
CM = [F(x) for x in os.environ.get('CMOVE', '5/4,17/16').split(',')]
FSRC = os.environ.get('FSRC', 'T,C1,C2').split(',')
SPL = [tuple(x.split(':')) for x in os.environ.get('SPL', '').split(',') if x]
SPLR = int(os.environ.get('SPLR', '1')); MAXR = int(os.environ.get('MAXR', '1'))
L = loop(b)
idx = dict(L)
def same(m, y): return all(m[0] * y[i] == y[0] * m[i] for i in range(3))
for s in ['T', 'C1', 'C2']:
    for k in (1, 2, 3):
        for ci, c in enumerate(CM):
            m = shift(L[s], k, c)
            if not any(same(m, y) for y in idx.values()):
                idx['%s>%d%s' % (s, k, "'" * ci)] = m
assert all(in2V(m) for m in idx.values())
B = Build(idx, maxr=MAXR, fill_sources=FSRC, splice_pairs=SPL, splice_r=SPLR)
I = B.I
print('scale', b, 'moves', CM, 'installed', len(idx), 'cells', len(B.cells), 'models', len(I.models), flush=True)
B.build(selected=list(idx), registered=list(idx))
names = [c for c, _ in B.cells]
def viable(X, f):
    a, c = I.idx[X], I.idx[f]
    for w in W:
        rX, rf = I.R[w - 1, a], I.R[w - 1, c]
        if (rf <= rX).all() and (rf < rX).any():
            return False
    return True
info, sels, deferred = {}, [], []
def require(tag, f, cand):
    if not cand:
        deferred.append(tag); return
    sv = B.newvar(); sels.append(sv); info[sv] = (tag, cand)
    for cl in B.dominated_by_some(f, [B.M[x] for x in cand]):
        I.add([-sv] + cl)
for s in FSRC:
    for k in (1, 2, 3):
        for f in B.F[(s, k)]:
            E = [j for j in range(len(names)) if f[j] != B.M[s][j]]
            cand = [x for x in idx if B.M[x] != f and not all(B.M[x][j] == 'A' for j in E) and viable(B.M[x], f)]
            succ = {('T', 3): 'C1', ('C1', 1): 'C2', ('C2', 2): 'T'}.get((s, k))
            if os.environ.get('LOOPEDGE') == '1' and succ in cand:
                cand = [succ]          # the loop successor itself must dominate every fill it can admissibly dominate
            require(('fill', s, k, tuple(names[j] for j in E)), f, cand)
import random
SPLMAX = int(os.environ.get('SPLMAX', '0'))
for (x, y) in SPL:
    zs = B.S[(x, y)]
    if SPLMAX and len(zs) > SPLMAX:
        zs = random.Random(72).sample(zs, SPLMAX)
    for z in zs:
        H = [j for j in range(len(names)) if z[j] != B.M[x][j]]
        cand = [u for u in idx if u not in (x, y) and B.M[u] != z and viable(B.M[u], z)]
        require(('splice', x, y, tuple(names[j] for j in H)), z, cand)
def solve(assum):
    while True:
        if not I.solver.solve(assumptions=assum):
            return False
        mdl = set(v for v in I.solver.get_model() if v > 0)
        viol = I.violations(mdl)
        if not viol:
            I.last = mdl; return True
        for (a, c, d, w) in viol:
            X = [(a, c), (c, d), (d, a)]
            base = [-int(I.Vw[w - 1, p, q]) for (p, q) in X]
            for (p, q) in X:
                I.add(base + [int(I.Vw[w - 1, q, p])]); I.ntc += 1
r = solve(sels)
print('requirements %d (fills %d, splices %d), deferred %d: %s  (TC %d, %.0fs)' % (len(sels),
      sum(1 for v in sels if info[v][0][0] == 'fill'), sum(1 for v in sels if info[v][0][0] == 'splice'),
      len(deferred), 'SAT' if r else 'UNSAT', I.ntc, time.time() - t0), flush=True)
for d in deferred: print('   deferred (no admissible installed candidate):', d)
if not r:
    core = [v for v in I.solver.get_core() if v in info]
    i = 0
    while i < len(core):
        trial = core[:i] + core[i + 1:]
        if not solve(trial):
            core = [v for v in I.solver.get_core() if v in info] or trial
        else:
            i += 1
    print('minimal core (%d):' % len(core))
    for v in core: print('   ', info[v])
else:
    mdl = I.last
    use = {}
    for v in sels:
        tag, cand = info[v]
        f = None
        # recover the model for this tag
    for s in FSRC:
        for k in (1, 2, 3):
            cnt = {}
            for f in B.F[(s, k)]:
                for x in idx:
                    X = B.M[x]
                    if X != f and all(I.acc(X, f, w) for w in W) and not all(I.acc(f, X, w) for w in W):
                        cnt[x] = cnt.get(x, 0) + 1
            print('   %s class %d: dominators used %s' % (s, k, cnt))
    print('   verdicts among loop members (worlds 1,2,3; A accepted, r refused):')
    for x in ['T', 'C1', 'C2']:
        print('     ', x, ' '.join('%s:%s' % (y, ''.join('A' if I.acc(B.M[x], B.M[y], w) else 'r' for w in W)) for y in ['T', 'C1', 'C2'] if y != x))
    print('   verdicts of loop members against their class-k repairers (move 1):')
    for x in ['T', 'C1', 'C2']:
        print('     ', x, ' '.join('%s:%s' % (y, ''.join('A' if I.acc(B.M[x], B.M[y], w) else 'r' for w in W)) for y in idx if y.startswith(x + '>')))
