"""Pinning of the forced precise caps (C2_notes section 5), at every vertex b and for both facet data x+-.

At vertex b with failing pair (a,b) and third index c, the precise map on the cap is sigma(q)=nu(Wq), W=diag(w),
w_b=1, and its boundary points q near e_b satisfy Q_a(q)=(Wq).H_a(q)=0 and Q_c(q)=(Wq).H_c(q)=0, H_k(q) the pencil
normal of facet F_k selected by the chord through q.  Infinitely many common zeros accumulating at e_b in the sector
between the failing edge and lambda_b force a common component through e_b:
  (I)  the conics coincide near e_b: R(d) = Lc(d)Qa2(d) - La(d)Qc2(d) vanishes identically in the direction d;
  (II) a common line through e_b, direction d0:  La(d0)=Qa2(d0)=Lc(d0)=Qc2(d0)=0.
We solve both exactly (sympy) and confirm completeness with a multistart numerical search, then test the precise
constraint (R1) for sigma=nu(Wq) at points of the cap near the failing edge.
usage: pin_caps.py eps"""
import sympy as sp, numpy as np, sys, itertools
from scipy.optimize import least_squares

eps = sp.Rational(sys.argv[1]) if len(sys.argv) > 1 else sp.Rational(3, 10)
kap = (1 + 2 * eps) / (1 - eps); s_ = kap + 1
xp = (s_ + sp.sqrt(s_ * s_ - 4)) / 2
c0 = (1 - eps) / 3
v = [sp.Matrix([c0 + (eps if i == k else 0) for i in range(3)]) for k in range(3)]


def corner(k, j):
    r = v[k].cross(v[j]); t = 3 - k - j
    return r if (r.T * v[t])[0] > 0 else -r


def cvec(k, h, x):
    h1, h2, h3 = h
    if k == 0:
        return sp.Matrix([-(x * h2 + h3), x * h2, h3])
    if k == 1:
        return sp.Matrix([h1, -(h1 + x * h3), x * h3])
    return sp.Matrix([x * h1, h2, -(x * h1 + h2)])


q = sp.Matrix(sp.symbols('q1 q2 q3'))


def H(k, x):
    i, j = [l for l in range(3) if l != k]
    r0, r1 = corner(k, i), corner(k, j)
    return (cvec(k, r1, x).T * q)[0] * r0 - (cvec(k, r0, x).T * q)[0] * r1


def failing_a(b, xname):
    # writeup / N28_referee: x+ fails at (a,b) = (1,2),(2,3),(3,1); x- at (2,1),(3,2),(1,3)  (1-based)
    tab = {'x+': {1: 0, 2: 1, 0: 2}, 'x-': {0: 1, 1: 2, 2: 0}}
    return tab[xname][b]


for xname, x in [('x+', xp), ('x-', 1 / xp)]:
    for b in range(3):
        a = failing_a(b, xname); c = 3 - a - b
        W = sp.symbols('wa wc', positive=True)
        wv = [None] * 3; wv[a], wv[b], wv[c] = W[0], sp.Integer(1), W[1]
        wq = sp.Matrix([wv[i] * q[i] for i in range(3)])
        # the facet whose crossing coordinate b lies on the chord lambda_b: F_a and F_c both cross b
        Qa = sp.expand((wq.T * H(a, x))[0]); Qc = sp.expand((wq.T * H(c, x))[0])
        da, dc, t = sp.symbols('da dc t')
        d = [None] * 3; d[a], d[c], d[b] = da, dc, -(da + dc)
        sub = {q[i]: (1 if i == b else 0) + t * d[i] for i in range(3)}
        PA = sp.Poly(sp.expand(Qa.subs(sub)), t); PC = sp.Poly(sp.expand(Qc.subs(sub)), t)
        assert PA.coeff_monomial(1) == 0 and PC.coeff_monomial(1) == 0
        La, Qa2 = PA.coeff_monomial(t), PA.coeff_monomial(t ** 2)
        Lc, Qc2 = PC.coeff_monomial(t), PC.coeff_monomial(t ** 2)
        R = sp.expand(Lc * Qa2 - La * Qc2)
        cI = [sp.simplify(cf) for cf in sp.Poly(R, da, dc).coeffs()]
        solI = sp.solve(cI, list(W), dict=True)
        r = sp.Symbol('r')
        eqII = [sp.simplify(e.subs({da: 1, dc: r})) for e in (La, Qa2, Lc, Qc2)]
        solII = sp.solve(eqII, list(W) + [r], dict=True)
        # numerical completeness check (multistart)
        fI = sp.lambdify(list(W), cI, 'numpy'); fII = sp.lambdify(list(W) + [r], eqII, 'numpy')
        numI, numII = set(), set()
        for s0 in itertools.product(np.geomspace(0.05, 20, 9), repeat=2):
            res = least_squares(lambda z: np.array(fI(*np.exp(z)), float) * 1e3, np.log(s0))
            if res.cost < 1e-16:
                numI.add(tuple(np.round(np.exp(res.x), 6)))
            for r0 in (0.05, 0.3, 1.0, 3.0):
                res = least_squares(lambda z: np.array(fII(np.exp(z[0]), np.exp(z[1]), np.exp(z[2])), float) * 1e3,
                                    np.r_[np.log(s0), np.log(r0)])
                if res.cost < 1e-16:
                    numII.add(tuple(np.round(np.exp(res.x), 6)))
        print(f"eps={eps} {xname}={float(x):.6f} kappa={float(kap):.6f} vertex b={b+1} failing a={a+1} third c={c+1}")
        print("   (I)  exact:", [{str(k_): float(v_) for k_, v_ in s.items()} for s in solI], " numeric:", sorted(numI))
        print("   (II) exact:", [{str(k_): float(v_) for k_, v_ in s.items()} for s in solII], " numeric:", sorted(numII))
        print("        1/x =", float(1 / x), " x =", float(x), " kappa =", float(kap))
