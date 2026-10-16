# Independent checks for P4 Part B (referee P4B).  Exact rational arithmetic.
# Chain c_b = [0,b) on I = [0,1], grid of M cells.  A set A is given by cell fractions f_i in [0,1]
# (cell i contributes [i/M, i/M + f_i/M)).  World 1 = lexicographic order with K levels given by
# piecewise-constant densities w_k (nonnegative); c_b <=_1 A iff (pi_k(A) - pi_k(c_b))_k >=_lex 0.
# We compute the section S_1(A) = {b in [0,1] : c_b <=_1 A} EXACTLY as an initial segment
# [0,e] or [0,e) by recursion over levels (each g_k(b) = pi_k(A) - pi_k(c_b) is continuous,
# nonincreasing, piecewise linear in b), and report whether it is closed.
from fractions import Fraction as Fr
import random

def mk(M):
    h = Fr(1, M)
    def pic(w, b):                      # pi_w(c_b)
        s = Fr(0)
        for i in range(M):
            lo = Fr(i, M)
            ov = min(max(b - lo, 0), h)
            s += w[i] * ov
        return s
    def piA(w, fr):
        return sum(w[i] * fr[i] * h for i in range(M))
    def zero_interval(w, target, lo, hi):
        # g(b) = target - pi_w(c_b), continuous nonincreasing piecewise linear on [lo,hi].
        # Returns ('pos',) if g>0 on [lo,hi]; ('neg',) if g<0 on [lo,hi]; else ('mix', l, r) with
        # {g>0} = [lo,l), {g=0} = [l,r].
        def g(b): return target - pic(w, b)
        if g(hi) > 0: return ('pos',)
        if g(lo) < 0: return ('neg',)
        if lo == hi: return ('mix', lo, lo)
        pts = sorted(set([lo, hi] + [Fr(i, M) for i in range(M + 1) if lo < Fr(i, M) < hi]))
        vals = [g(p) for p in pts]
        l = None
        for (a, ga), (c, gc) in zip(zip(pts, vals), zip(pts[1:], vals[1:])):
            if ga <= 0: l = a; break
            if gc <= 0: l = a + (c - a) * ga / (ga - gc); break
        r = None
        for (a, ga), (c, gc) in zip(zip(pts[::-1][1:], vals[::-1][1:]), zip(pts[::-1], vals[::-1])):
            if gc >= 0: r = c; break
            if ga >= 0: r = a + (c - a) * ga / (ga - gc); break
        return ('mix', l, r)
    def section(ws, fr, lo=Fr(0), hi=Fr(1), k=0):
        # S cap [lo,hi] where levels < k vanish identically. Returns None (empty) or (e, closed).
        if k == len(ws): return (hi, True)
        res = zero_interval(ws[k], piA(ws[k], fr), lo, hi)
        if res[0] == 'pos': return (hi, True)
        if res[0] == 'neg': return None
        _, l, r = res
        sub = section(ws, fr, l, r, k + 1)
        if sub is None: return (l, False) if l > lo else None
        return sub
    return pic, piA, section

if __name__ == '__main__':
    random.seed(11)
    M = 24
    pic, piA, section = mk(M)
    # (1) Theorem B3 out of order: level 1 vanishes on [0,1/3), positive after; trimmed set
    w1 = [Fr(0) if i < 8 else Fr(1 + i % 3) for i in range(M)]
    w2 = [Fr(1)] * M
    ws = [w1, w2]
    b0 = Fr(18, M)
    fr = [Fr(1) if i < 18 else Fr(0) for i in range(M)]
    fr = [Fr(0) if i < 4 else f for i, f in enumerate(fr)]   # A = c_{b0} minus Z, Z = [0,4/M)
    e, cl = section(ws, fr)
    print('(1) out-of-order trimmed set: section end =', e, 'closed =', cl, '(expect end 18/24 = 3/4, open)')
    # (2) Theorem B3 in order, 3 levels, random sets: sections closed? endorsement by random alpha?
    s1, s2 = 7, 15
    W = [[Fr(random.randint(1, 4)) if i < s1 else Fr(0) for i in range(M)],
         [Fr(random.randint(0, 3)) if i < s1 else (Fr(random.randint(1, 4)) if i < s2 else Fr(0)) for i in range(M)],
         [Fr(random.randint(0, 3)) if i < s2 else Fr(random.randint(1, 4)) for i in range(M)]]
    nclosed = nopen = viol = tested = 0
    for t in range(1500):
        fr = [Fr(random.randint(0, 6), 6) for _ in range(M)]
        if random.random() < 0.5:
            cut = random.randint(0, M)
            fr = [Fr(1) if i < cut and random.random() < 0.85 else f for i, f in enumerate(fr)]
        e, cl = section(W, fr)
        if cl: nclosed += 1
        else:
            nopen += 1
            if nopen == 1: print('    open in-order section example: end', e, 'A fractions', [str(x) for x in fr])
        if cl:
            al = [Fr(random.randint(1, 50), random.randint(1, 50)) for _ in range(3)]
            dens = [al[0] * W[0][i] if i < s1 else (al[1] * W[1][i] if i < s2 else al[2] * W[2][i]) for i in range(M)]
            tested += 1
            if piA(dens, fr) < pic(dens, e): viol += 1
    print('(2) in-order 3-level lex: sections closed', nclosed, 'open', nopen,
          '; endorsement nu(A) >= nu(c_phi) with random alphas: tested', tested, 'violations', viol)
    # (3) E2: in-order 2-level lex(lambda on [0,s), lambda) violates strict escape
    s = 12
    V = [[Fr(1) if i < s else Fr(0) for i in range(M)], [Fr(1)] * M]
    bad = 0; tot = 0
    for bi in range(1, s):
        b = Fr(bi, M)
        for t in range(10):
            D = [Fr(random.randint(0, 6), 6) if i >= s else Fr(0) for i in range(M)]
            if all(x == 0 for x in D): continue
            fr = [Fr(1) if i < bi else D[i] for i in range(M)]
            e, cl = section(V, fr)
            tot += 1
            if e == b: bad += 1
    print('(3) in-order lex(lambda|[0,1/2), lambda): phi_1(c_b u D) == b (strict escape FAILS) in', bad, 'of', tot, 'cases')
    # (K) failure with world 2 = lambda: P=[0,1/4), Q=[5/8,1): P <=_1 Q ? Q <=_2 P ?
    P = [Fr(1) if i < 6 else Fr(0) for i in range(M)]; Q = [Fr(1) if i >= 15 else Fr(0) for i in range(M)]
    vP = [piA(w, P) for w in V]; vQ = [piA(w, Q) for w in V]
    diff = [q - p for p, q in zip(vP, vQ)]
    first = next((d for d in diff if d != 0), 0)
    print('    (K) at b=5/8: P<=_1 Q:', first >= 0, '; Q<=_2 P (lambda):', piA([Fr(1)]*M, Q) <= piA([Fr(1)]*M, P))
    # (4) single strictly positive level: strict escape holds on samples
    R = [[Fr(random.randint(1, 5)) for i in range(M)], [Fr(1)] * M]
    ok = tot = 0
    for t in range(400):
        bi = random.randint(0, M - 2); b = Fr(bi, M)
        D = [Fr(random.randint(0, 6), 6) if i > bi else Fr(0) for i in range(M)]
        if all(x == 0 for x in D): continue
        fr = [Fr(1) if i < bi else D[i] for i in range(M)]
        e, cl = section(R, fr); tot += 1
        if e > b: ok += 1
    print('(4) lex(rho*lambda, lambda), rho>0: strict escape phi_1(c_b u D) > b in', ok, 'of', tot)
