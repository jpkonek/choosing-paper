"""PP62 (CHECKED, exact integers): rule R0 on PP56's exact kink-cell instances.

R0(r) = {}                        if r is null
      = {w : V_w(r) < 0}          if V(r) != 0
      = {W0}                      if r non-null and V(r) = 0   (W0 = world 2, index 1)
X <=_w Y  iff  w not in R0(rec(X,Y)),  V_w(rec(X,Y)) = sum_p m_p (phi_p(Y_p)_w - phi_p(X_p)_w)  (PP56 level-0 field u1).

Instances (PP56 instance56 conventions; local proxies A^B, A^D carry B's and D's clauses by exact (IB)):
  pieces in actual kink cells; masses are integers with m(above) = m(below), so balanced (null) records occur.
Checked exhaustively: reflexivity; strict (G) on every pair at every world; (IB) (verdict constant per record);
(TC) on every ordered triple at every world; defence and protection (some world refuses the reverse) of
A, A^B, A^D against every instance model.  Also counted: null records, single-world incomparabilities (all on
null records at W0), ties, and the alpha = (1,1) certificate for the inverse pair of the balanced swap.
"""
import sys, os, itertools, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
from instance56 import Instance, DIS, ABOVE, BELOW   # noqa: E402
from cells56 import rank                            # noqa: E402

W0 = 1
random.seed(62)


def make(inst):
    def V(X, Y):
        return tuple(sum(inst.m[p] * (inst.phi[p][Y[p]][w] - inst.phi[p][X[p]][w]) for p in range(len(X)))
                     for w in range(3))

    def R(X, Y):
        if X == Y:
            return frozenset()
        v = V(X, Y)
        if any(v):
            return frozenset(w for w in range(3) if v[w] < 0)
        return frozenset([W0])
    return V, R


def proxies(inst):
    A = inst.base['A']
    out = {'A': A}
    for N in 'BD':
        out['A^' + N] = inst.base[N]     # on the pieces, the proxy carries N's values (A elsewhere)
    return out


def check(inst, models, full=True):
    V, R = make(inst)
    ok = True
    stats = dict(null=0, incomp=0, ties=0)
    W = range(3)
    if full:
        Rm = {(X, Y): R(X, Y) for X in models for Y in models}
        recs = {}
        for (X, Y), rr in Rm.items():
            key = tuple((p, X[p], Y[p]) for p in range(len(X)) if X[p] != Y[p])
            if recs.setdefault(key, rr) != rr:
                ok = False
            if X != Y and not any(V(X, Y)):
                stats['null'] += 1
            for w in W:
                acc_xy, acc_yx = w not in rr, w not in Rm[(Y, X)]
                if X < Y and acc_xy and acc_yx:
                    stats['ties'] += 1
                if X < Y and not acc_xy and not acc_yx:
                    stats['incomp'] += 1
                    ok &= (w == W0 and not any(V(X, Y)))     # incomparability only on null records at W0
        ok &= all(Rm[(X, X)] == frozenset() for X in models)
        for X, Y in itertools.permutations(models, 2):
            for w in W:
                rx = [rank(X[p], inst.g[p], w) for p in range(len(X))]
                ry = [rank(Y[p], inst.g[p], w) for p in range(len(Y))]
                if all(a <= b for a, b in zip(rx, ry)) and rx != ry:      # Y weakly worse, strictly somewhere
                    ok &= (w not in Rm[(X, Y)]) and (w in Rm[(Y, X)])
        for X in models:
            for Y in models:
                rxy = Rm[(X, Y)]
                for Z in models:
                    ryz, rzx = Rm[(Y, Z)], Rm[(Z, X)]
                    for w in W:
                        if w not in rxy and w not in ryz and w not in rzx:
                            if w in Rm[(Y, X)] or w in Rm[(Z, Y)] or w in Rm[(X, Z)]:
                                ok = False
        stats['records'] = len(recs)
    for name, N in proxies(inst).items():
        for X in models:
            if X == N:
                continue
            defence = len(R(N, X)) < 3
            protect = len(R(X, N)) > 0
            if not (defence and protect):
                ok = False
                print('  selected obligation fails', name, X)
    return ok, stats


if __name__ == '__main__':
    ALL = True
    others = [i for i in range(len(DIS)) if i not in (ABOVE, BELOW)]
    # I1: 18 cells, values {h,S}: selected obligations only (2^18 rivals)
    for trial in range(2):
        ms = [random.randint(1, 40) for _ in DIS]
        ms[BELOW] = ms[ABOVE]
        inst = Instance(list(range(len(DIS))), ('P', 'S'), ms)
        ok, st = check(inst, inst.models(), full=False)
        print(f'[I1.{trial}] 18 cells, {{h,S}}, 2^18 rivals, m(above)=m(below): defence+protection of A, A^B, A^D:', ok)
        ALL &= ok
    # I2: exhaustive axioms, six pieces {h,S} incl. above/below with equal mass
    for trial in range(3):
        ids = [ABOVE, BELOW] + random.sample(others, 4)
        ms = [random.randint(1, 12) for _ in ids]
        ms[1] = ms[0]
        inst = Instance(ids, ('P', 'S'), ms)
        ok, st = check(inst, inst.models())
        print(f'[I2.{trial}] cells {ids} masses {ms}: all axioms + selected obligations:', ok, st)
        ALL &= ok
    # I3: three pieces with all four values (64 models), above/below equal mass
    for trial in range(3):
        ids = [ABOVE, BELOW, random.choice(others)]
        ms = [random.randint(1, 12) for _ in ids]
        ms[1] = ms[0]
        inst = Instance(ids, ('P', 'M', 'S', 'C'), ms)
        ok, st = check(inst, inst.models())
        print(f'[I3.{trial}] cells {ids} masses {ms}, four values: all axioms + selected obligations:', ok, st)
        ALL &= ok
    # I4: equal masses everywhere (many null records), six pieces
    ids = [ABOVE, BELOW] + others[:4]
    inst = Instance(ids, ('P', 'S'), [5] * 6)
    ok, st = check(inst, inst.models())
    print(f'[I4] cells {ids}, all masses equal: all axioms + selected obligations:', ok, st)
    ALL &= ok
    # alpha certificate on the balanced swap: forward record A -> A[{above,below} -> S], reverse record
    inst = Instance([ABOVE, BELOW], ('P', 'S'), [7, 7])
    V, R = make(inst)
    A = inst.base['A']; X = ('S', 'S')
    d_fwd = [inst.m[p] * (inst.phi[p][X[p]][W0] - inst.phi[p][A[p]][W0]) for p in range(2)]
    d_rev = [inst.m[p] * (inst.phi[p][A[p]][W0] - inst.phi[p][X[p]][W0]) for p in range(2)]
    cert = all(a + b >= 0 for a, b in zip(d_fwd, d_rev))
    print('[alpha] V(A->X) =', V(A, X), ' R0(A->X) =', set(R(A, X)), ' R0(X->A) =', set(R(X, A)),
          ' pointwise d_fwd + d_rev >= 0 (alpha=(1,1)):', cert)
    ALL &= cert and R(A, X) == R(X, A) == frozenset([W0])
    print('ALL PASS' if ALL else 'SOME FAIL')
