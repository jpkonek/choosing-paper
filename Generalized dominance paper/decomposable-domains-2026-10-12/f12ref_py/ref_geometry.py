"""F12 referee: independent checks of F1 claim (A), Lemma F1.1, the F1.2 coupling, and F1.4 constants.
Run: python3 -I ref_geometry.py
n = 2, weight t of world 2, m_t = (1-t, t). U = D_{K'} = {h : min_{t in K'} m_t.h > 0}.
World-1 error of a model X at mixed h: h1>0 and h not accepted, or h1<0 and h accepted.
"""
import math, random
random.seed(12345)
al, be = 0.3, 0.6

def acc(h, l, r):  # h in D_[l,r] : (1-t)h1 + t h2 > 0 for t in {l, r}
    return min((1-l)*h[0] + l*h[1], (1-r)*h[0] + r*h[1]) > 0

def inU(h): return acc(h, al, be)

def err1(h, l, r):
    a = acc(h, l, r)
    return (h[0] > 0 and not a) or (h[0] < 0 and a)

def T(h): return h[0]/(h[0]-h[1])

# host A raw coordinate (from C2.1 parametrisation K_s=[al s, be+(1-be)s])
def xA(h):
    t = T(h)
    return (t-be)/(1-be) if h[0] > 0 else t/al

# (1) brute-force: E1(D_{K_s}) on M equals {x_A <= s} (mod the level set)
bad = 0; nM = 0
for _ in range(200000):
    th = random.uniform(-math.pi, math.pi); h = (math.cos(th), math.sin(th))
    if not inU(h) or h[0]*h[1] >= 0: continue
    nM += 1
    s = random.random()
    l, r = al*s, be+(1-be)*s
    if err1(h, l, r) != (xA(h) <= s) and abs(xA(h)-s) > 1e-12: bad += 1
print("(1) host A: E1(C_s) cap M == {x_A <= s}: mixed samples %d, mismatches %d" % (nM, bad))

# (2) ends: where does x_A -> 1 ?  and is the limit ray in U or on dU ?
thb = math.atan2(be-1, be); tha = math.atan2(1-al, -al)
P = lambda h: min((1-al)*h[0]+al*h[1], (1-be)*h[0]+be*h[1])
print("(2) P_K'(1,0) = %.3f (>0: interior of U);  P_K'(-al,1-al) = %.2e (on dU)" % (P((1, 0)), P((-al, 1-al))))
for eps in (1e-2, 1e-4, 1e-6):
    hp = (math.cos(-eps), math.sin(-eps)); hm = (math.cos(tha-eps), math.sin(tha-eps))
    print("    theta=-%.0e: x_A=%.8f inU=%s | theta=th_a-%.0e: x_A=%.8f inU=%s" % (eps, xA(hp), inU(hp), eps, xA(hm), inU(hm)))

# (3) analytic slope of uniform x at the interior ray: (1-x)/|theta| -> G'(1)/(1-be)
Tp = lambda th: 1/(math.cos(th)-math.sin(th))**2
Mang = (0-thb) + (tha-math.pi/2)
Gp1 = ((1-be)/Tp(0.0) + al/Tp(tha))/Mang
print("(3) analytic G'(1)/(1-be) = %.4f  (F1 numerics: 2.309)" % (Gp1/(1-be)))
share = ((1-be)/Tp(0.0))/((1-be)/Tp(0.0) + al/Tp(tha))
print("    near-unanimous share of the levels x->1: %.4f (F2 numerics: 0.437)" % share)

# (4) F1.2 coupling in D2'_A: a density heavy only on M- near th_a but bounded on M+ fails a (K) cut move.
# uniform coordinate on host A via numeric G
N = 200000
grid = [thb + (0-thb)*(i+0.5)/N for i in range(N)] + [math.pi/2 + (tha-math.pi/2)*(i+0.5)/N for i in range(N)]
w = [(0-thb)/N]*N + [(tha-math.pi/2)/N]*N
raws = [xA((math.cos(t), math.sin(t))) for t in grid]
order = sorted(range(2*N), key=lambda i: raws[i])
cum = 0.0; xu = [0.0]*(2*N)
for i in order:
    xu[i] = (cum + w[i]/2)/Mang; cum += w[i]
def rho_bad(i):  # heavy (1/(1-x)) only on M-, bounded (=1) on M+
    return 1/(1-xu[i]) if grid[i] > 0 else 1.0
b = 0.99
Pm = [i for i in range(2*N) if grid[i] > 0 and b-0.004 <= xu[i] < b]      # P in c_b, on M-
Qp = [i for i in range(2*N) if grid[i] < 0 and xu[i] >= b]                 # Q in d_b, on M+
lP = sum(w[i] for i in Pm)/Mang; lQ = sum(w[i] for i in Qp)/Mang
nuP = sum(w[i]*rho_bad(i) for i in Pm)/Mang; nuQ = sum(w[i]*rho_bad(i) for i in Qp)/Mang
print("(4) cut b=%.2f: lambda(P)=%.5f < lambda(Q)=%.5f, so (K) forces C_b <=_1 X; nu(P)=%.4f > nu(Q)=%.4f: %s"
      % (b, lP, lQ, nuP, nuQ, "UNENDORSED (as F1.2 predicts)" if (lQ > lP and nuP > nuQ) else "no violation"))

# (5) F1.4 rounding constants
c = 1-math.exp(-1)
print("(5) P(cover >= c/2) >= c/2 = %.4f; P(cost <= 4G) >= 0.75; sum - 1 = %.4f > 0" % (c/2, c/2+0.75-1))

# (6) host B: x_B < lambda(M+) on M+, so compact K in U has K cap M in some c_b0, b0<1
xB = lambda h: (T(h)-be)/(2*(1-be)) if h[0] > 0 else 0.5 + T(h)/(2*al)
print("(6) host B: x_B at theta=-1e-6 is %.6f (<1/2); at th_a-1e-6 is %.6f" %
      (xB((math.cos(-1e-6), math.sin(-1e-6))), xB((math.cos(tha-1e-6), math.sin(tha-1e-6)))))
