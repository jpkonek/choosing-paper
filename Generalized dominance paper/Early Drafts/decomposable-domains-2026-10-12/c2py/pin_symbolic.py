"""Symbolic-in-eps verification (vertex b=2, failing a=1, c=3, data x=x+):
 (1) w=(kappa,1,kappa) with the line direction r=d3/d1=1/x solves the common-line system for EVERY eps;
 (2) Q_a, Q_c are not identically zero at the two candidate w's;
 (3) the cap map W=(x,1,1/x) (coincident conics) violates (R1) at first order: the blow-up margin is
     u2(My) - tau_2(y) = y_c (x kappa - 1/x) > 0;  the line cap W=(kappa,1,kappa) has both margins <= 0 exactly on
     the sector y_c/y_a <= 1/x."""
import sympy as sp

e = sp.Symbol('epsilon', positive=True)
kap = (1 + 2 * e) / (1 - e)
x = sp.Symbol('x', positive=True)          # x+ : root of x^2-(kappa+1)x+1
relx = sp.expand(x ** 2 - (kap + 1) * x + 1)
c0 = (1 - e) / 3
v = [sp.Matrix([c0 + (e if i == k else 0) for i in range(3)]) for k in range(3)]


def corner(k, j):
    r = v[k].cross(v[j]); t = 3 - k - j
    val = sp.simplify((r.T * v[t])[0])
    return r if val.subs(e, sp.Rational(3, 10)) > 0 else -r


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


def reduce_x(expr):
    num, den = sp.fraction(sp.together(sp.expand(expr)))
    rem = sp.rem(sp.Poly(sp.expand(num), x), sp.Poly(relx, x))
    return sp.simplify(rem.as_expr())


t, r = sp.symbols('t r')
for name, (wa, wc) in [('line cap W=(kappa,1,kappa)', (kap, kap)), ('conic cap W=(x,1,1/x)', (x, 1 / x))]:
    wq = sp.Matrix([wa * q[0], q[1], wc * q[2]])
    Qa = (wq.T * H(0))[0]; Qc = (wq.T * H(2))[0]
    sub = {q[0]: t, q[1]: 1 - t * (1 + r), q[2]: t * r}
    PA = sp.Poly(sp.expand(Qa.subs(sub)), t); PC = sp.Poly(sp.expand(Qc.subs(sub)), t)
    coeffs = [PA.coeff_monomial(t), PA.coeff_monomial(t ** 2), PC.coeff_monomial(t), PC.coeff_monomial(t ** 2)]
    print(name)
    print("   Q_a, Q_c identically zero? ", sp.expand(Qa) == 0, sp.expand(Qc) == 0)
    if name.startswith('line'):
        vals = [reduce_x(sp.expand(cf.subs(r, 1 / x) * x ** 4)) for cf in coeffs]
        print("   common-line equations at r=1/x, reduced mod x^2-(kappa+1)x+1:", vals)
    else:
        da, dc = sp.symbols('da dc')
        sub2 = {q[0]: t * da, q[1]: 1 - t * (da + dc), q[2]: t * dc}
        PA = sp.Poly(sp.expand(Qa.subs(sub2)), t); PC = sp.Poly(sp.expand(Qc.subs(sub2)), t)
        R = sp.expand(PC.coeff_monomial(t) * PA.coeff_monomial(t ** 2) - PA.coeff_monomial(t) * PC.coeff_monomial(t ** 2))
        cfs = sp.Poly(R, da, dc).coeffs()
        print("   cubic R coefficients reduced mod relation:", [reduce_x(sp.expand(cf * x ** 4)) for cf in cfs])
# (3) first-order R1 margins in blow-up coordinates (from C2_notes section 4): u1(mu) = -mu_a + kappa mu_c,
# u2(mu) = kappa mu_a - mu_c, tau'(y) = (kappa/x)(y_c - y_a), tau_2(y) = x kappa (y_a - y_c); precise sigma = M y
ya, yc = sp.symbols('y_a y_c', nonnegative=True)
for name, M in [('line cap', (kap, kap)), ('conic cap', (x, 1 / x))]:
    mu = (M[0] * ya, M[1] * yc)
    m1 = sp.simplify(-mu[0] + kap * mu[1] - (kap / x) * (yc - ya))
    m2 = sp.simplify(kap * mu[0] - mu[1] - x * kap * (ya - yc))
    print(name, " margin u1-tau' =", sp.factor(m1), ";  margin u2-tau_2 =", sp.factor(m2))
