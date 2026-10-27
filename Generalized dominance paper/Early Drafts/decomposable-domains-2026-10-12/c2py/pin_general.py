"""Uniqueness of the cap pinning for general eps (vertex b=2, a=1, c=3, x=x+), parametrised by x>1
(kappa = x + 1/x - 1; every kappa>1 i.e. every eps in (0,1) arises from exactly one x>1).
Solves the coincident-conic system (I) and the common-line system (II) with x symbolic, via Groebner bases."""
import sympy as sp

x = sp.Symbol('x', positive=True)
kap = x + 1 / x - 1
e = (kap - 1) / (kap + 2)          # inverse of kappa=(1+2e)/(1-e)
c0 = (1 - e) / 3
v = [sp.Matrix([sp.simplify(c0 + (e if i == k else 0)) for i in range(3)]) for k in range(3)]


def corner(k, j):
    r = v[k].cross(v[j]); t = 3 - k - j
    val = sp.simplify((r.T * v[t])[0])
    return r if val.subs(x, 3) > 0 else -r


def cvec(k, h):
    h1, h2, h3 = h
    if k == 0:
        return sp.Matrix([-(x * h2 + h3), x * h2, h3])
    if k == 1:
        return sp.Matrix([h1, -(h1 + x * h3), x * h3])
    return sp.Matrix([x * h1, h2, -(x * h1 + h2)])


q = sp.Matrix(sp.symbols('q1 q2 q3'))


def H(k):
    i, j = [l for l in range(3) if l != k]
    r0, r1 = corner(k, i), corner(k, j)
    return (cvec(k, r1).T * q)[0] * r0 - (cvec(k, r0).T * q)[0] * r1


wa, wc, r, t, da, dc = sp.symbols('wa wc r t da dc')
wq = sp.Matrix([wa * q[0], q[1], wc * q[2]])
Qa = (wq.T * H(0))[0]; Qc = (wq.T * H(2))[0]
sub = {q[0]: t * da, q[1]: 1 - t * (da + dc), q[2]: t * dc}
PA = sp.Poly(sp.expand(Qa.subs(sub)), t); PC = sp.Poly(sp.expand(Qc.subs(sub)), t)
La, Qa2, Lc, Qc2 = PA.coeff_monomial(t), PA.coeff_monomial(t ** 2), PC.coeff_monomial(t), PC.coeff_monomial(t ** 2)


def numer(ex):
    return sp.factor(sp.numer(sp.together(sp.expand(ex))))


# (I)
R = sp.expand(Lc * Qa2 - La * Qc2)
eqI = [numer(cf) for cf in sp.Poly(R, da, dc).coeffs()]
GI = sp.groebner(eqI, wa, wc, domain=sp.QQ.frac_field(x), order='lex')
print("(I) Groebner basis:")
for g_ in GI.exprs:
    print("   ", sp.factor(g_))
# (II)
eqII = [numer(ex.subs({da: 1, dc: r})) for ex in (La, Qa2, Lc, Qc2)]
GII = sp.groebner(eqII, wa, wc, r, domain=sp.QQ.frac_field(x), order='lex')
print("(II) Groebner basis:")
for g_ in GII.exprs:
    print("   ", sp.factor(g_))
