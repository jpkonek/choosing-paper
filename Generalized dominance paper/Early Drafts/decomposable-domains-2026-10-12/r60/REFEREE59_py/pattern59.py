"""pattern59: independent exact-cell check of PP75 Theorem 3.1 (Pattern Lemma) and Cor 3.2.
For posterior a, b in the (2V) region and r = b/a, the patterns (worlds where C_b is strictly better) occurring
non-null on {C_a != C_b} should be exactly:
   {k} iff r_k > min_{i != k} r_i ;   {!= k} iff r_k < max_{i != k} r_i,
with twin sources: {k} = lose A_k (inside A(C_a)) and gain B_k (inside Sil(C_a)); {!=k} = gain A_k and lose B_k.
All 13 order types of r are generated, several random pairs each; (2V) is checked on every cell.
"""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib59 import *
random.seed(75)


def orders():
    out = []
    for blocks in [((0, 1, 2),), ((0,), (1, 2)), ((1,), (0, 2)), ((2,), (0, 1)), ((0, 1), (2,)), ((0, 2), (1,)),
                   ((1, 2), (0,))] + [tuple((i,) for i in p) for p in itertools.permutations(range(3))]:
        out.append(blocks)
    return out


def mk(blocks):
    vals = sorted(F(random.randint(85, 115), 100) for _ in range(len(blocks)))
    while len(set(vals)) < len(vals):
        vals = sorted(F(random.randint(85, 115), 100) for _ in range(len(blocks)))
    r = [None] * 3
    for b, v in zip(blocks, vals):
        for i in b: r[i] = v
    return tuple(r)


def in2V(a):
    inv = [1 / F(x) for x in a]
    s = sum(inv)
    return all(x / s > F(7, 30) for x in inv)


def main():
    n_pairs = mism = twin_bad = v2 = comp_bad = 0
    types = orders()
    assert len(types) == 13
    for blocks in types:
        for _ in range(6):
            while True:
                a = tuple(F(random.randint(90, 110), 100) for _ in range(3))
                r = mk(blocks)
                b = tuple(a[i] * r[i] for i in range(3))
                if in2V(a) and in2V(b): break
            cs = cells({'A': post(a), 'B': post(b)})
            found = {}
            for c in cs:
                t = htype(c['pt'])
                va, vb = c['vals']['A'], c['vals']['B']
                if va == -1 or vb == -1: v2 += 1
                if t[0] == 'U' or va == vb: continue
                kind, o = t
                pat = frozenset([w for w in range(3) if rank(vb, c['pt'], w) < rank(va, c['pt'], w)])
                src = ('gain' if vb == 1 else 'lose') + kind
                found.setdefault(pat, set()).add(src)
            pred = set()
            for k in range(3):
                others = [r[i] for i in range(3) if i != k]
                if r[k] > min(others): pred.add(frozenset([k]))
                if r[k] < max(others): pred.add(frozenset([w for w in range(3) if w != k]))
            n_pairs += 1
            if set(found) != pred: mism += 1
            for pat, srcs in found.items():
                if len(pat) == 1 and srcs != {'loseA', 'gainB'}: twin_bad += 1
                if len(pat) == 2 and srcs != {'gainA', 'loseB'}: twin_bad += 1
            # Cor 3.2: C_b weakly better than C_a at w pointwise iff r is a single raise of w
            for w in range(3):
                pointwise = all(w in p for p in found) and bool(found)
                single_raise = all(r[i] == r[(w + 1) % 3] for i in range(3) if i != w) and r[w] > r[(w + 1) % 3]
                if pointwise != single_raise: comp_bad += 1
    print('pairs: %d over 13 order types ; pattern-set mismatches: %d ; twin-source failures: %d ; '
          '-h cells (2V violations): %d ; Cor 3.2 mismatches: %d' % (n_pairs, mism, twin_bad, v2, comp_bad))


if __name__ == '__main__':
    main()
