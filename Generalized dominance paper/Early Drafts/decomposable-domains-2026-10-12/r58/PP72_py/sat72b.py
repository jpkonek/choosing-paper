"""sat72b: rival-dependent dominators on a multi-scale loop instance.
Installed: loops at scales in SCALES (T shared), plus optional one-move defenders C_{m + t delta_k}.
Sources: the loop members.  For every class-k fill f = C[E -> A] of a source (E a union of <= MAXR silent bounded
pieces, all pieces, single whole regions, whole class-k silence), the candidates are the installed models that do
NOT answer A on all of E (path/agreement obstruction, PP71 Lemma 2.1 -- a candidate answering A on all of E can
never dominate f).  Fills with no candidate are DEFERRED (they need a smaller scale; reported).  Clause: some
candidate dominates f (all worlds, strict somewhere).
Env: SCALES='9/8,5/4' DEF=1 (add defenders) MAXR=1 ONLYLOOP=1 (candidates restricted to the loop's own class edge)."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inst72 import *
SC = [F(x) for x in os.environ.get('SCALES', '9/8,5/4').split(',')]
DEF = os.environ.get('DEF', '1') == '1'
MAXR = int(os.environ.get('MAXR', '1'))
CMOVES = [F(x) for x in os.environ.get('CMOVE', '9/8').split(',')]
idx = {'T': (F(1), F(1), F(1))}
src = ['T']
for i, b in enumerate(SC):
    L = loop(b)
    idx['C1_%d' % i] = L['C1']; idx['C2_%d' % i] = L['C2']
    src += ['C1_%d' % i, 'C2_%d' % i]
LOOPCLASS = {'T': 3}
for i in range(len(SC)):
    LOOPCLASS['C1_%d' % i] = 1; LOOPCLASS['C2_%d' % i] = 2
if DEF:
    for s in list(src):
        for k in (1, 2, 3):
            if k == LOOPCLASS[s] and os.environ.get('ALLDEF', '0') != '1':
                continue
            for ci, cmove in enumerate(CMOVES):
                m = shift(idx[s], k, cmove)
                if not any(all(m[0] * y[i] == y[0] * m[i] for i in range(3)) for y in idx.values()):
                    idx['%s>%d%s' % (s, k, "'" * ci)] = m
assert all(in2V(m) for m in idx.values())
t0 = time.time()
FS = os.environ.get('FSRC')
FS = FS.split(',') if FS else src
src = [x for x in src if x in FS]
B = Build(idx, maxr=MAXR, fill_sources=FS)
print('scales', SC, 'defenders', DEF, 'installed', len(idx), 'cells', len(B.cells), 'models', len(B.I.models), flush=True)
B.build(selected=list(idx), registered=list(idx))
names = [c for c, _ in B.cells]
def viable(X, f):
    a, b = B.I.idx[X], B.I.idx[f]
    for w in W:
        rX, rf = B.I.R[w - 1, a], B.I.R[w - 1, b]
        if (rf <= rX).all() and (rf < rX).any():
            return False
    return True
cl, deferred, nf = [], 0, 0
REQ = os.environ.get('REQ')
REQ = None if REQ is None else set((x.split(':')[0], int(x.split(':')[1])) for x in REQ.split(',') if x)
for s in src:
    for k in (1, 2, 3):
        if REQ is not None and (s, k) not in REQ:
            continue
        for f in B.F[(s, k)]:
            E = [j for j in range(len(names)) if f[j] != B.M[s][j]]
            cand = [B.M[x] for x in idx if B.M[x] != f and not all(B.M[x][j] == 'A' for j in E) and viable(B.M[x], f)]
            if not cand:
                deferred += 1; continue
            nf += 1
            cl += B.dominated_by_some(f, cand)
for x in cl: B.I.solver.add_clause(x)
r = B.I.solve()
print('fills required %d, deferred %d:  %s   (TC clauses %d, %.0fs)' % (nf, deferred, 'SAT' if r else 'UNSAT', B.I.ntc, time.time() - t0), flush=True)
if r:
    mdl = B.I.last
    # report which installed model dominates which class of which source
    print('dominators used (source, class) -> installed:')
    for s in src:
        for k in (1, 2, 3):
            used = {}
            for f in B.F[(s, k)]:
                for x in idx:
                    X = B.M[x]
                    if X == f: continue
                    if all(B.I.acc(X, f, w) for w in W) and not all(B.I.acc(f, X, w) for w in W):
                        used[x] = used.get(x, 0) + 1
            print('   %-6s class %d (%d fills): %s' % (s, k, len(B.F[(s, k)]), used))
    print('verdicts among loop members (A=accepted, r=refused) worlds 1,2,3:')
    for x in src:
        print('   ', x, ' '.join('%s:%s' % (y, ''.join('A' if B.I.acc(B.M[x], B.M[y], w) else 'r' for w in W)) for y in src if y != x))
