# PP67: per-type feasibility of a common witness field for the 7-model module
# {T, N_1, N_2, N_3, D*_1, D*_2, D*_3} (all three classes at once). Exact sample census + LP with unit margins,
# then an exact rational re-check of every LP solution.  Run: python3 -I -B types7.py > types7.out
from fractions import Fraction as Fr
import itertools, random
from scipy.optimize import linprog
random.seed(7)
c, e = Fr(7,30), Fr(3,10)
MV = [tuple(c + (e if i==v else 0) for i in range(3)) for v in range(3)]
def proj(v, k):                     # radial projection from e_k onto the opposite edge
    s = sum(v[i] for i in range(3) if i != k)
    return tuple(Fr(0) if i == k else v[i]/s for i in range(3))
M0 = {k: [proj(v, k) for v in MV] for k in range(3)}
MODELS = [('T', MV, (1,1,1))]
for k in range(3):
    lam = [1,1,1]; lam[k] = Fr(1,2); MODELS.append(('N%d' % (k+1), MV + M0[k], tuple(lam)))
for k in range(3):
    lam = [1,1,1]; lam[k] = 0; MODELS.append(('D%d' % (k+1), M0[k], tuple(lam)))
def adv(K, g):
    s = [sum(q[i]*g[i] for i in range(3)) for q in K]
    if all(x > 0 for x in s): return 1
    if all(x < 0 for x in s): return -1
    return 0
def cls(g):
    s = [1 if x > 0 else -1 for x in g]
    if s[0] == s[1] == s[2]: return None
    for o in range(3):
        if s[(o+1)%3] == s[(o+2)%3]: return o
def lab(x, g, o): return 'S' if x == 0 else ('B' if x*g[o] > 0 else 'A')
G = [g for g in itertools.product(range(-8,9), repeat=3) if all(x != 0 for x in g)]
G += [tuple(Fr(random.randint(-600,600), random.randint(1,80)) for _ in range(3)) for _ in range(30000)]
G = [g for g in G if all(x != 0 for x in g)]
types = set(); unanim_ok = True
for g in G:
    o = cls(g)
    if o is None:
        unanim_ok &= all(adv(K,g) != 0 and adv(K,g) == adv(MV,g) for _, K, _ in MODELS); continue
    types.add((o, tuple(lab(adv(K,g),g,o) for _, K, _ in MODELS)))
print("unanimous points: every model answers the unanimous answer:", unanim_ok)
print("distinct mixed types:", len(types))
ok = unanim_ok
for o, ty in sorted(types):
    # variables x = (a1,a2,a3,b1,b2,b3); a = f(A)-f(S), b = f(B)-f(S)
    A_ub, b_ub = [], []
    for w in range(3):                      # rank monotonicity with margin 1
        rowa = [0]*6; rowb = [0]*6
        if w != o: rowa[w] = 1;  rowb[3+w] = -1     # a_w <= -1, b_w >= 1
        else:      rowa[w] = -1; rowb[3+w] = 1      # a_o >= 1, b_o <= -1
        A_ub += [rowa, rowb]; b_ub += [-1, -1]
    for (nm, K, lam), want in zip(MODELS, ty):
        la = [float(l) for l in lam]
        va = la + [0,0,0]; vb = [0,0,0] + la     # lam.a, lam.b
        neg = lambda v: [-x for x in v]
        diff = [x - y for x, y in zip(va, vb)]
        if want == 'S':   A_ub += [neg(va), neg(vb)]; b_ub += [-1, -1]          # lam.a >= 1, lam.b >= 1
        if want == 'A':   A_ub += [va, diff]; b_ub += [-1, -1]                   # lam.a <= -1, lam.a - lam.b <= -1
        if want == 'B':   A_ub += [vb, neg(diff)]; b_ub += [-1, -1]
    r = linprog([0]*6, A_ub=A_ub, b_ub=b_ub, bounds=[(-100,100)]*6, method='highs')
    feas = r.status == 0
    if feas:   # exact re-check with rounded rationals
        x = [Fr(round(v*8), 8) for v in r.x]
        a, b = x[:3], x[3:]
        good = all((a[w] < 0 < b[w]) if w != o else (b[w] < 0 < a[w]) for w in range(3))
        for (nm, K, lam), want in zip(MODELS, ty):
            vals = {'S': Fr(0), 'A': sum(Fr(l)*q for l, q in zip(lam, a)), 'B': sum(Fr(l)*q for l, q in zip(lam, b))}
            m = min(vals.values()); good &= [k for k, v in vals.items() if v == m] == [want]
        feas = good
    ok &= feas
    print("class o=%d  (T,N1,N2,N3,D1,D2,D3) = %s : %s" % (o+1, ''.join(ty), "feasible, exact" if feas else "INFEASIBLE"))
print("ALL PASS" if ok else "SOME FAIL")

# ---- exact completeness of the census: enumerate every open cell of the plane arrangement ----
# Types depend only on the signs of g against: the coordinate planes and every vertex of M, M0^1, M0^2, M0^3.
import math
normals = [(1,0,0),(0,1,0),(0,0,1)] + MV + [v for k in range(3) for v in M0[k]]
normals = list({tuple(Fr(x) for x in n) for n in normals})
def cross(p, q): return (p[1]*q[2]-p[2]*q[1], p[2]*q[0]-p[0]*q[2], p[0]*q[1]-p[1]*q[0])
def dot(p, q): return sum(x*y for x, y in zip(p, q))
cells = set(); mingap = 10.0
for n1, n2 in itertools.combinations(normals, 2):
    d0 = cross(n1, n2)
    if all(x == 0 for x in d0): continue
    for sgn in (1, -1):
        d = tuple(sgn*x for x in d0)
        u = n1; v = cross(d, n1)
        through = [n for n in normals if dot(n, d) == 0]
        angs = sorted({(math.atan2(-float(dot(n,u)), float(dot(n,v))) % math.pi) for n in through})
        angs = sorted(set([a % (2*math.pi) for a in angs] + [(a + math.pi) % (2*math.pi) for a in angs]))
        gaps = [(angs[(i+1) % len(angs)] - angs[i]) % (2*math.pi) for i in range(len(angs))]
        mingap = min(mingap, min(gaps))
        for i in range(len(angs)):
            th = angs[i] + gaps[i]/2
            al, be = Fr(round(math.cos(th)*10**6), 10**6), Fr(round(math.sin(th)*10**6), 10**6)
            nd = math.sqrt(float(dot(d,d))); scale = max(abs(float(x)) for x in u + v)
            dl = Fr(1, 10**9)
            g = tuple(d[j] + dl*(al*u[j] + be*v[j]) for j in range(3))
            # exact sanity: off every plane; same side as d for planes not through d
            if any(dot(n, g) == 0 for n in normals): continue
            if any(dot(n, d) != 0 and (dot(n, g) > 0) != (dot(n, d) > 0) for n in normals):
                print("WARNING: perturbation too large"); ok = False
            cells.add(tuple(1 if dot(n, g) > 0 else -1 for n in normals) + (g,))
reps = {}
for cell in cells: reps.setdefault(cell[:-1], cell[-1])
print("arrangement: %d planes, %d distinct open cells found (min angular gap %.4f rad)" % (len(normals), len(reps), mingap))
newtypes = set()
for g in reps.values():
    o = cls(g)
    if o is None: continue
    newtypes.add((o, tuple(lab(adv(K,g),g,o) for _, K, _ in MODELS)))
print("types from exact cell enumeration: %d; all already in the sample census and solved: %s" % (len(newtypes), newtypes <= types))
ok &= newtypes <= types
print("ALL PASS" if ok else "SOME FAIL")
# Euler check on the sphere: F = 2 - V + E, with V = vertices (lines x 2), E = sum over vertices of (planes through it)
lines = {}
for n1, n2 in itertools.combinations(normals, 2):
    d = cross(n1, n2)
    if all(x == 0 for x in d): continue
    # normalise direction up to positive scale
    s = next(x for x in d if x != 0); key = tuple(x / s for x in d)   # a line, not a ray
    lines[key] = sum(1 for n in normals if dot(n, d) == 0)
V = 2*len(lines); E = 2*sum(lines.values())
print("Euler: V=%d E=%d -> F=%d faces; enumerated %d" % (V, E, 2 - V + E, len(reps)))
ok &= (2 - V + E) == len(reps)
print("ALL PASS" if ok else "SOME FAIL")
