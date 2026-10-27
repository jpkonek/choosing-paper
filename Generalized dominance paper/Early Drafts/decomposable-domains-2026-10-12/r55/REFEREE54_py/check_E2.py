"""REFEREE54: independent re-check of PP61's allocation E2 on the G3 instance.

What is reused from PP61: the instance itself (atoms with exact rays, model value vectors, the selected /
coherent flags, the sigma/minus refinement of each shift sub-instance) and the saved verdict vector E2_G3.pkl,
read through PP61's pair -> record-id matrices.  What is NOT reused: record canonicalisation, ranks,
guidance, every clause, (IB), (TC).  All of those are recomputed here from the model vectors.

Checks (per block = base instance and each of the 9 shift sub-instances):
  IB    verdicts depend only on the (own) canonical record, across ALL blocks;
  REFL  empty records accepted;
  G     strict guidance (own ranks) on every ordered pair, both the acceptance and the reverse refusal;
  DEF   every selected model accepts every other model of its block at some world;
  PROT  for every selected S and X != S: X incoherent -> some world refuses X <= S;
        X coherent -> (X <= S at all worlds) implies (S <= X at all worlds)  [undominatedness];
  SEC   [C_{a_t} <=_i X] -> [C_a <=_i X] for every fixed base rival X;
  TC    every ordered triple of the block, every world (matrix test);
  PAT   E2's pattern: each balanced swap has a world refusing both r and r^-;
  GERM  refusal sets of the shifted records vs the base record.
"""
import sys, os, pickle, time
from collections import defaultdict, Counter
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
P61 = os.path.join(HERE, '..', 'PP61_py')
sys.path.insert(0, P61)
sys.path.insert(0, os.path.join(HERE, '..', 'PP56_py'))
import inst61  # noqa: F401  (needed only to unpickle the instance objects)

VALS = ('P', 'M', 'S', 'C')


def my_rank(v, g, w):
    """0 correct < 1 silent < 2 wrong < 3 contradictory; 'P' answers +g, 'M' answers -g."""
    if v == 'S':
        return 1
    if v == 'C':
        return 3
    sgn = g[w] if v == 'P' else -g[w]
    assert sgn != 0
    return 0 if sgn > 0 else 2


def main():
    t0 = time.time()
    with open(os.path.join(P61, 'enc61_G3.pkl'), 'rb') as f:
        inst, kinds, enc = pickle.load(f)
    with open(os.path.join(P61, 'E2_G3.pkl'), 'rb') as f:
        val = pickle.load(f)
    print('loaded (%.0fs): atoms %d, base models %d, subs %d' % (time.time() - t0, len(inst.atoms), len(inst.base_models), len(inst.subs)))
    atoms = inst.atoms
    nb = inst.nbase

    def acc(rid, i):
        return bool(val[3 * rid + i + 1])

    # ---- own canonical records ----
    def canon(x, y, sub):
        if sub is None:
            return tuple((p, x[p], y[p]) for p in range(nb) if x[p] != y[p])
        S = inst.subs[sub]
        pos = {aid: nb + j for j, aid in enumerate(S['sig'])}
        ch = S['children']
        out = []
        for p in range(nb):
            if p in ch:
                pieces = [(S['minus'][p], x[p], y[p])] + [(c, x[pos[c]], y[pos[c]]) for c in ch[p]]
                pairs = set((a, b) for (_, a, b) in pieces)
                if len(pairs) == 1:
                    a, b = pairs.pop()
                    if a != b:
                        out.append((p, a, b))
                else:
                    out.extend(t for t in pieces if t[1] != t[2])
            elif x[p] != y[p]:
                out.append((p, x[p], y[p]))
        for c in S['sig']:
            if atoms[c].parent is None and x[pos[c]] != y[pos[c]]:
                out.append((c, x[pos[c]], y[pos[c]]))
        return tuple(sorted(out))

    rk = {}

    def rk_of(p, v, w):
        k = (p, v, w)
        if k not in rk:
            rk[k] = my_rank(VALS[v], atoms[p].ray, w)
        return rk[k]

    def guid(rec, w):
        if not rec:
            return 1
        b = [rk_of(p, x, w) < rk_of(p, y, w) for (p, x, y) in rec]
        return 1 if all(b) else (-1 if not any(b) else 0)

    blocks = [('base', None, list(inst.base_models), [inst.models[n] for n in inst.base_models], inst.coherent, inst.selected)]
    for s, S in inst.subs.items():
        nm = list(inst.base_models) + S['new']
        blocks.append((s, s, nm, [S['models'][n] for n in nm], S['coherent'], S['selected']))
    ib = defaultdict(set)
    bad = Counter({k: 0 for k in ('REFL', 'G', 'DEF', 'PROT/C', 'UND', 'SEC', 'TC', 'PAT', 'GERM')})
    for (label, sub, names, vecs, coh, sel) in blocks:
        names_e, M = enc.mat[label]
        assert names_e == names
        n = len(names)
        A = np.zeros((3, n, n), dtype=bool)
        for a in range(n):
            for b in range(n):
                r = int(M[a, b])
                for i in range(3):
                    A[i, a, b] = acc(r, i)
                rec = canon(vecs[a], vecs[b], sub)
                ib[rec].add(tuple(A[:, a, b]))
                if a == b:
                    if not A[:, a, b].all():
                        bad['REFL'] += 1
                    continue
                if not rec:            # distinct names, equal models: (IB) + reflexivity
                    if not A[:, a, b].all():
                        bad['REFL'] += 1
                    continue
                if a < b:
                    for i in range(3):
                        g = guid(rec, i)
                        if g == 1 and not (A[i, a, b] and not acc(int(M[b, a]), i)):
                            bad['G'] += 1
                        if g == -1 and not (not A[i, a, b] and acc(int(M[b, a]), i)):
                            bad['G'] += 1
        # selected-model obligations
        for a in range(n):
            if not sel[names[a]]:
                continue
            for b in range(n):
                if a == b:
                    continue
                if not A[:, a, b].any():
                    bad['DEF'] += 1
                if not coh[names[b]]:
                    if A[:, b, a].all():
                        bad['PROT/C'] += 1
                else:
                    if A[:, b, a].all() and not A[:, a, b].all():
                        bad['UND'] += 1
        # sections along the shift subsequence (fixed base rivals only)
        if sub is not None:
            S = inst.subs[sub]
            ia, it = names.index('S:' + sub[0]), names.index(S['tname'])
            for b, Xn in enumerate(names):
                if Xn not in inst.models or b in (ia, it):
                    continue
                for i in range(3):
                    if A[i, it, b] and not A[i, ia, b]:
                        bad['SEC'] += 1
        # TC on every ordered triple: violation iff A[x,y] & !A[y,x] & exists z: A[y,z] & A[z,x]
        for i in range(3):
            Ai = A[i].astype(np.int32)
            strict = A[i] & ~A[i].T
            two = (Ai @ Ai)          # two[y,x] = #z with A[y,z] & A[z,x]
            nv = int((strict & (two.T > 0)).sum())
            bad['TC'] += nv
        print('  block %-12s models %4d  cumulative violations %s  (%.0fs)' % (str(label), n, dict(bad), time.time() - t0), flush=True)
    nib = sum(1 for r, s in ib.items() if len(s) > 1)
    print('IB: own canonical records %d (PP61 record ids %d); records with inconsistent verdicts: %d' % (len(ib), len(enc.recs), nib))
    bad['IB'] = nib
    # ---- E2 pattern and germs, recomputed ----
    names0, M0 = enc.mat['base']
    swaps = [(n, a, b, F) for (n, a, b, F) in inst.swaps if kinds.get((a, b, F)) == 'bal2']
    pat = Counter()
    Rf = lambda r: ''.join(str(i + 1) for i in range(3) if not acc(int(r), i)) or '-'
    for (n, a, b, F) in swaps:
        ia, ix = names0.index('S:' + a), names0.index(n)
        r, rb = M0[ia, ix], M0[ix, ia]
        both = [i + 1 for i in range(3) if not acc(int(r), i) and not acc(int(rb), i)]
        if not both:
            bad['PAT'] += 1
        g1 = []
        for w in range(3):
            nm, Ms = enc.mat[(a, w)]
            g1.append(Rf(Ms[nm.index(inst.subs[(a, w)]['tname']), nm.index(n)]))
        yn = [m for (m, x, y, FF) in inst.swaps if x == b and y == a and FF == F][0]
        g2 = []
        for w in range(3):
            nm, Ms = enc.mat[(b, w)]
            g2.append(Rf(Ms[nm.index(inst.subs[(b, w)]['tname']), nm.index(yn)]))
        germ_ok = all(x == Rf(r) for x in g1) and all(x == Rf(rb) for x in g2)
        if not germ_ok:
            bad['GERM'] += 1
        # u^1 increments of r per unit mass on its atoms (sign information only)
        pat[(Rf(r), Rf(rb), 'both-refused@' + ''.join(map(str, both)))] += 1
    print('E2 pattern on the %d balanced swaps (R(r), R(r-), worlds refusing both):' % len(swaps))
    for k, c in sorted(pat.items()):
        print('   ', k, 'x', c)
    print('VIOLATIONS:', dict(bad))
    print('E2 RE-CHECK:', 'PASS' if not any(bad.values()) else 'FAIL', '(%.0fs)' % (time.time() - t0))


if __name__ == '__main__':
    main()
