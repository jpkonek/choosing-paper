"""PP61 swap families: overlapping, balanced (zero u^1-value at all worlds at unit core masses), non-conic.

For an unordered source pair {a, b}, L = disagreement classes of (C_a, C_b).
The u^1 increment of a -> b on +K (per unit mass) is vec(K) = phi_K(C_b) - phi_K(C_a), one of
+-(2,-1,-1), +-(-1,2,-1), +-(-1,-1,2).  Families (each used in BOTH orders a->b and b->a, so the
common-context copy Y = C_b[F -> C_a] of every swap X = C_a[F -> C_b] is in the instance):
  single  {K.c1}                                  (decided by guidance at every world)
  bal2    {K.c1, K'.c1}, vec(K) = -vec(K')        (balanced at unit masses)
  ovl     {K.c1, K'.c2}, {K.c2, K'.c1}, {K.c1, K.c2, K'.c1}, {K.c1, K'.c1, K'.c2}  (overlap bal2)
  bal3    {K1.c1, K2.c1, K3.c1}, vec sum zero     (three-type balanced)
  big     {all c1 of L}
"""
import itertools
from fractions import Fraction as Fr


def vec(inst, key, a, b):
    geo = inst.geo
    c = geo.cname[key]
    p = inst.by_label[c + '.c1']
    at = inst.atoms[p]
    xa, xb = inst.src(a)[p], inst.src(b)[p]
    return tuple(at.phi[w][xb] - at.phi[w][xa] for w in range(3))


def families(inst, a, b, max_bal2=4, max_bal3=2, overlaps=True):
    geo = inst.geo
    L = [k for k in geo.dis if k[1][geo.names.index(a)] != k[1][geo.names.index(b)]]
    V = {k: vec(inst, k, a, b) for k in L}
    c1 = {k: inst.by_label[geo.cname[k] + '.c1'] for k in L}
    c2 = {k: inst.by_label[geo.cname[k] + '.c2'] for k in L}
    fam = []
    for k in L:
        fam.append(('single', (c1[k],)))
    pairs = [(k, kk) for k, kk in itertools.combinations(L, 2) if all(x + y == 0 for x, y in zip(V[k], V[kk]))]
    # prefer the kink's certificate cells (sign types Maj1 / Min1) first
    from geom61 import sig
    pairs.sort(key=lambda kp: (sig(inst.geo.cls[kp[0]]) not in ('Maj1', 'Min1'), kp))
    for (k, kk) in pairs[:max_bal2]:
        fam.append(('bal2', (c1[k], c1[kk])))
        if overlaps:
            fam.append(('ovl', (c1[k], c2[kk])))
            fam.append(('ovl', (c2[k], c1[kk])))
            fam.append(('ovl', (c1[k], c2[k], c1[kk])))
            fam.append(('ovl', (c1[k], c1[kk], c2[kk])))
    trip = [t for t in itertools.combinations(L, 3) if all(sum(V[k][w] for k in t) == 0 for w in range(3))]
    for t in trip[:max_bal3]:
        fam.append(('bal3', tuple(c1[k] for k in t)))
    if len(L) > 1:
        fam.append(('big', tuple(c1[k] for k in L)))
    # dedupe
    seen, out = set(), []
    for kind, F in fam:
        F = tuple(sorted(F))
        if F not in seen:
            seen.add(F)
            out.append((kind, F))
    return out, L, V


def swap_spec(inst_proto, pairs, **kw):
    spec, kinds = [], {}
    for (a, b) in pairs:
        fam, L, V = families(inst_proto, a, b, **kw)
        for kind, F in fam:
            spec.append((a, b, F))
            spec.append((b, a, F))
            kinds[(a, b, F)] = kind
            kinds[(b, a, F)] = kind
    return spec, kinds
