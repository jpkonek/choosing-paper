# I2 referee: independent exact recomputation of the transition-point blow-up at ALL three vertices
# (no use of cyclic symmetry), the relations (R_b), and the cyclic contradiction.
# Conventions: writeup Prop T1 facet data c_k with x1=x2=x3=x, p*=u, kappa=(1+2eps)/(1-eps).
import sympy as sp

t, k, x = sp.symbols('t kappa x', positive=True)
y = sp.symbols('y1:4')           # blow-up direction (coordinates of q-e_b, sum 0)
w = sp.symbols('w1:4', positive=True)

def c_k(kf, h):
    h1, h2, h3 = h
    if kf == 1: return sp.Matrix([-(x*h2+h3), x*h2, h3])
    if kf == 2: return sp.Matrix([h1, -(h1+x*h3), x*h3])
    if kf == 3: return sp.Matrix([x*h1, h2, -(x*h1+h2)])

def facet_gamble(kf, b, z):
    # gamble on F_kf with h_kf=-1, h_b=z, third coordinate kappa-z  (h.v_kf = c0(kappa-1)-eps = 0)
    h = [None]*3; h[kf-1] = -1; h[b-1] = z; j = 6-kf-b; h[j-1] = k - z
    return sp.Matrix(h)

def Phi(q, b, a, c):
    # facet gambles on F_a and F_c (both b-crossing) whose chord passes through q; intersect zero lines
    gs = []
    for kf in (a, c):
        z = sp.symbols('z')
        expr = (c_k(kf, facet_gamble(kf, b, z)).T * q)[0]
        zs = sp.solve(sp.Eq(expr, 0), z)
        assert len(zs) == 1
        gs.append(facet_gamble(kf, b, zs[0]))
    m = gs[0].cross(gs[1])
    return m / (m[0]+m[1]+m[2])

def sigma(q):
    m = sp.Matrix([w[i]*q[i] for i in range(3)])
    return m / sum(m)

pairs = {2: (1, 3), 3: (2, 1), 1: (3, 2)}   # b: (a, c) for x = x_+  (failing edges [e_a,e_b])
corner = {x: sp.Symbol('X')}
rel = {}
for b, (a, c) in pairs.items():
    eb = sp.Matrix([1 if i == b-1 else 0 for i in range(3)])
    ya, yc = sp.symbols('ya yc')
    dirv = [0, 0, 0]; dirv[a-1] = ya; dirv[c-1] = yc; dirv[b-1] = -(ya+yc)
    q = eb + t*sp.Matrix(dirv)
    G = sigma(q) - Phi(q, b, a, c)
    # first-order coefficient in t of the (a,c) coordinates
    Ga = sp.simplify(sp.diff(G[a-1], t).subs(t, 0))
    Gc = sp.simplify(sp.diff(G[c-1], t).subs(t, 0))
    J = sp.Matrix([[sp.diff(Ga, ya), sp.diff(Ga, yc)], [sp.diff(Gc, ya), sp.diff(Gc, yc)]])
    J = sp.simplify(J)
    det = sp.factor(sp.simplify(J.det()))
    print(f"b={b} (a,c)=({a},{c}):  DG =", J.applyfunc(sp.factor))
    print("    det DG =", det)
    rel[b] = (J, det)

# compare with I2's v
v1 = k/(1-k**2)*(1/x - k*x); v3 = k/(1-k**2)*(k/x - x)
print("I2 v1-v3 simplified:", sp.simplify((v1-v3)))
print("   with corner equation x+1/x=kappa+1:", sp.simplify((v1-v3).subs(k, x+1/x-1)))
J2, det2 = rel[2]
pred = sp.Matrix([[w[0]/w[1]-v1, v1], [-v3, w[2]/w[1]+v3]])
print("b=2: DG - I2 prediction =", sp.simplify(J2-pred))
