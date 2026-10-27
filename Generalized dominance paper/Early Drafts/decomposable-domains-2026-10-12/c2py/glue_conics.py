"""Gluing obstruction at a vertex (C2_notes section 5).
On the boundary of the forced precise cap O_b, sigma(q) = w.q/(w.q) (Prop D, diagonal projective) must equal
V(q) = L^a(q) cap L^c(q), where L^k(q) = {m : m.H_k(q) = 0}, H_k(q) = (c_k(r1).q) r0 - (c_k(r0).q) r1 is the
pencil line of facet F_k selected by the chord through q.  So boundary points lie on both conics
   Q_a(q) = (w*q).H_a(q) = 0,   Q_c(q) = (w*q).H_c(q) = 0.
Infinitely many such points accumulate at e_b (arc argument), so by Bezout the conics share a component through e_b.
This script computes, exactly (sympy, rational kappa from eps), whether any w > 0 allows that."""
import sympy as sp
import sys

eps = sp.Rational(sys.argv[1]) if len(sys.argv) > 1 else sp.Rational(3, 10)
kap = (1 + 2 * eps) / (1 - eps)
s = kap + 1
xp = (s + sp.sqrt(s * s - 4)) / 2          # x_+ (failing pairs (1,2),(2,3),(3,1))
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
w = sp.Matrix([sp.Symbol('w1', positive=True), 1, sp.Symbol('w3', positive=True)])   # b = world 2, w_b = 1


def H(k, x):
    i, j = [l for l in range(3) if l != k]
    r0, r1 = corner(k, i), corner(k, j)
    return (cvec(k, r1, x).T * q)[0] * r0 - (cvec(k, r0, x).T * q)[0] * r1


x = xp
Ha, Hc = H(0, x), H(2, x)                   # facets F_1 (a=1) and F_3 (c=3); b = 2
wq = sp.Matrix([w[i] * q[i] for i in range(3)])
Qa = sp.expand((wq.T * Ha)[0]); Qc = sp.expand((wq.T * Hc)[0])
# sanity: H_a(e_b) is proportional to the crossing w' = (-1,0,kappa), and e_b lies on both conics
eb = {q[0]: 0, q[1]: 1, q[2]: 0}
print("H_a(e_b) =", sp.simplify(Ha.subs(eb)).T, " H_c(e_b) =", sp.simplify(Hc.subs(eb)).T)
print("Q_a(e_b), Q_c(e_b):", sp.simplify(Qa.subs(eb)), sp.simplify(Qc.subs(eb)))
# directions from e_b: q = e_b + t d, d = (d1, -(d1+d3), d3)
d1, d3, t = sp.symbols('d1 d3 t')
sub = {q[0]: t * d1, q[1]: 1 - t * (d1 + d3), q[2]: t * d3}
QA = sp.expand(Qa.subs(sub)); QC = sp.expand(Qc.subs(sub))
La, Qa2 = sp.Poly(QA, t).coeff_monomial(t), sp.Poly(QA, t).coeff_monomial(t ** 2)
Lc, Qc2 = sp.Poly(QC, t).coeff_monomial(t), sp.Poly(QC, t).coeff_monomial(t ** 2)
R = sp.expand(Lc * Qa2 - La * Qc2)          # cubic form in (d1, d3); must vanish identically if C_a = C_c near e_b
coeffs = sp.Poly(R, d1, d3).coeffs()
print("number of cubic coefficients:", len(coeffs))
sol = sp.solve([sp.simplify(cf) for cf in coeffs], [w[0], w[2]], dict=True)
print("w making the cubic vanish identically:", sol)
# line case: a common line through e_b in direction d0 requires La(d0)=Qa2(d0)=Lc(d0)=Qc2(d0)=0
r = sp.Symbol('r')   # direction d = (1, -(1+r), r), r = d3/d1 >= 0 inside the sector toward e_a..e_c
eqs = [sp.simplify(e.subs({d1: 1, d3: r})) for e in (La, Qa2, Lc, Qc2)]
print("line-case equations in (w1,w3,r):")
for e in eqs:
    print("   ", sp.factor(e))
sol2 = sp.solve(eqs, [w[0], w[2], r], dict=True)
print("line-case solutions:", sol2)
