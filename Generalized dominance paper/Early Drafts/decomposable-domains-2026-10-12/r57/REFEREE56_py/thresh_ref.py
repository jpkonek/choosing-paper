"""thresh_ref (REFEREE56): the audit's geometric claims (AUDIT_round57*.md), exact where possible.

Run: python3 -I -B thresh_ref.py > thresh_ref.out
  B1 path-obstruction numbers: g = (1,1,-r); expectations at M0's endpoints; v_t.g = 1 - b_t(1+r);
     s=0, t=1/2, r=1 gives -2/30 and 14/30; C_0 silent and C_{1/2} = A there; T, N silent there;
     for s < t < 1 the r-window (1/b_s - 1, 1/b_t - 1) is non-empty (symbolic).
  B2 tau: on {g in M3 : v3.g < 0} (= common silence of N and F_0 in M3), F_t is S for t <= tau and A for
     t > tau, never B; tau in (0,1); level sets {tau = c} are planes (symbolic); recurrence
     Sil(F_s) n M3 = {tau >= s}.  Exact on 4000 random rational g.
  B3 sigma: R_alpha = D_{(1-a)M + aK_N} computed from Minkowski generators; on L = {T != N} it equals T for
     a < sigma(g) and S for a >= sigma(g), with sigma = h_M/(h_M - h_KN) in (0,1); off L it equals T = N.
  B4 J_beta = D_{(1-b)K_N + bK_L0}: equals N where N = L0; where they differ, N's S switches to L0's answer
     at a threshold; never a third value.
  B5 splice identity N[H -> T] = T[L \\ H -> N] (cell level; it is set algebra).
  B6 world-by-world: an explicit H and alpha for which R_alpha is mixed against Z_H at world 3 but
     pointwise worse at world 2 (so 'mixed at every world' fails for the retreat candidates).
  B7 NUMERICS: quartile window on a sample E (Monte Carlo; illustration only).
"""
import os, sys, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geomlib import *
import sympy as sp
ok = True
def chk(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

# ---------- B1 ----------
t, r, s_ = sp.symbols('t r s', real=True)
vts = [(1 - t) * sp.Rational(7, 30) + t / 2, (1 - t) * sp.Rational(7, 30) + t / 2, (1 - t) * sp.Rational(16, 30)]
g = [1, 1, -r]
expr = sp.simplify(sum(a * b for a, b in zip(vts, g)) - (1 - (1 - t) * sp.Rational(16, 30) * (1 + r)))
end1 = sp.simplify(sum(a * b for a, b in zip([sp.Rational(16, 23), sp.Rational(7, 23), 0], g)))
end2 = sp.simplify(sum(a * b for a, b in zip([sp.Rational(7, 23), sp.Rational(16, 23), 0], g)))
chk('B1 v_t.(1,1,-r) = 1 - b_t(1+r) with b_t = (1-t)16/30, and both endpoints of M0 give 1', expr == 0 and end1 == 1 and end2 == 1)
g0 = (1, 1, -1)
e0, e12 = dot(vt(F(0)), g0), dot(vt(F(1, 2)), g0)
chk('B1 s=0, t=1/2, r=1: v_0.g = %s, v_1/2.g = %s (audit: -2/30, 14/30)' % (e0, e12), e0 == F(-2, 30) and e12 == F(14, 30))
chk('B1 at g=(1,1,-1): C_0 = F_0 silent, C_1/2 answers + (the majority A); T and N silent (g in Q3)',
    adv(KF(F(0)), g0) == 'S' and adv(KF(F(1, 2)), g0) == '+' and adv(KT, g0) == 'S' and adv(KN, g0) == 'S')
bt = lambda x: (1 - x) * sp.Rational(16, 30)
gap = sp.simplify((1 / bt(t) - 1) - (1 / bt(s_) - 1))
chk('B1 for 0 <= s < t < 1 the window 1/b_s - 1 < r < 1/b_t - 1 is non-empty: gap = %s > 0' % gap,
    sp.simplify(gap - sp.Rational(30, 16) * (t - s_) / ((1 - t) * (1 - s_))) == 0)

# ---------- samples ----------
random.seed(57)
def rq(): return F(random.randint(-400, 400), random.randint(1, 60))
def sample_M3(n):
    out = []
    while len(out) < n:
        g = (abs(rq()) + F(1, 1000), abs(rq()) + F(1, 1000), -abs(rq()) - F(1, 1000))
        out.append(g)
    return out
G3 = sample_M3(4000)

# ---------- B2 ----------
b2 = True; cnt = 0; level = True
for g in G3:
    a3 = dot(v3, g)
    if a3 >= 0:
        b2 &= adv(KN, g) == '+' and adv(KF(F(0)), g) == '+'
        continue
    cnt += 1
    b2 &= adv(KN, g) == 'S' and adv(KF(F(0)), g) == 'S'       # common silence of N and F_0 in M3
    hg = dot(h12, g)
    tau = -a3 / (hg - a3)
    b2 &= 0 < tau < 1
    for tt in (F(0), tau / 2, tau, (tau + 1) / 2, F(999, 1000) * tau + F(1, 1000), F(1)):
        a = AB(g, adv(KF(tt), g))
        b2 &= (a == 'S') if tt <= tau else (a == 'A')
    # recurrence: g in Sil(F_s) iff tau >= s
    for ss in (F(1, 7), F(1, 3), F(2, 3), F(9, 10)):
        b2 &= (adv(KF(ss), g) == 'S') == (tau >= ss)
c = sp.symbols('c'); g1, g2, g3 = sp.symbols('g1 g2 g3')
vt_c = [(1 - c) * sp.Rational(7, 30) + c / 2] * 2 + [(1 - c) * sp.Rational(16, 30)]
lin = sp.expand(sum(a * b for a, b in zip(vt_c, (g1, g2, g3))))
level = sp.Poly(lin, g1, g2, g3).is_linear
chk('B2 on %d sampled g in M3 n {v3.g < 0}: N and F_0 both silent; tau in (0,1); F_t = S for t <= tau, '
    '= A for t > tau, never B; Sil(F_s) n M3 = {tau >= s}' % cnt, b2)
chk('B2 {tau = c} = {v_c.g = 0} is a plane for each c (so tau has an atomless law on every non-null E)', level)

# ---------- B3: R_alpha ----------
def minkowski(Ka, Kb, a):
    return [add(scal(1 - a, p), scal(a, q)) for p in Ka for q in Kb]
def hmin(K, g, sgn_):   # min over K of sgn * k.g
    return min(sgn_ * dot(k, g) for k in K)
def rand_g():
    while True:
        g = (rq(), rq(), rq())
        if 0 not in g: return g
GA = [rand_g() for _ in range(3000)]
b3 = True; nL = 0
for g in GA:
    Tg, Ng = adv(KT, g), adv(KN, g)
    if Tg == Ng:
        for a in (F(1, 5), F(1, 2), F(4, 5)):
            b3 &= adv(minkowski(KT, KN, a), g) == Tg
        continue
    nL += 1
    sg = 1 if Tg == '+' else -1
    hM, hK = hmin(KT, g, sg), hmin(KN, g, sg)
    b3 &= hM > 0 and hK <= 0 and Ng == 'S'
    sig = hM / (hM - hK)
    b3 &= 0 < sig <= 1
    for a in (sig / 3, sig * F(99, 100), sig, (sig + 1) / 2):
        if a > 1: continue
        want = Tg if a < sig else 'S'
        b3 &= adv(minkowski(KT, KN, a), g) == want
chk('B3 R_alpha (Minkowski generators): off L equals T = N; on L (%d samples) equals T for a < sigma and S for '
    'a >= sigma, sigma = h_M/(h_M - h_KN) in (0,1]; never the opposite answer' % nL, b3)

# ---------- B4: J_beta ----------
b4 = True; nd = 0
# targeted samples near the (S,S,B,B) cells: g1 > 0 > g2, g3 with 16g1 + 7g2 < 0 < 7g1 + 16g2 ... both signs
GB = list(GA)
while len(GB) < len(GA) + 3000:
    g = (abs(rq()) + F(1, 100), -abs(rq()) - F(1, 100), -abs(rq()) - F(1, 100))
    GB += [g, (g[1], g[0], g[2]), tuple(-x for x in g)]
for g in GB:
    Ng, Lg = adv(KN, g), adv(KL0, g)
    if Ng == Lg:
        for b in (F(1, 5), F(1, 2), F(4, 5)):
            b4 &= adv(minkowski(KN, KL0, b), g) == Ng
        continue
    nd += 1
    b4 &= Ng == 'S' and Lg != 'S'
    sg = 1 if Lg == '+' else -1
    hN, hL = hmin(KN, g, sg), hmin(KL0, g, sg)
    beta = -hN / (hL - hN)
    for b in (beta / 2, beta, (beta + 1) / 2, F(1)):
        b4 &= adv(minkowski(KN, KL0, b), g) == (Lg if b > beta else 'S')
chk('B4 J_beta: equals N = L0 where they agree; on {N != L0} (%d samples) switches from S to L0\'s answer at a '
    'threshold; no other value' % nd, b4)

# ---------- B5 ----------
pts, _ = cells([(1, 0, 0), (0, 1, 0), (0, 0, 1)] + KN)
Lc = [i for i, g in enumerate(pts) if adv(KT, g) != adv(KN, g)]
b5 = True
for k in range(len(Lc) + 1):
    for H in itertools.combinations(Lc, k):
        H = set(H)
        lhs = [adv(KT, g) if i in H else adv(KN, g) for i, g in enumerate(pts)]
        rhs = [adv(KN, g) if (i in Lc and i not in H) else adv(KT, g) for i, g in enumerate(pts)]
        b5 &= lhs == rhs
chk('B5 N[H -> T] = T[L \\ H -> N] for every union H of the %d cells of L' % len(Lc), b5)

# ---------- B6 ----------
# take g_H in L n M3 (T = B) and g_W in L n M1 (T = A); H := a small piece around g_H; alpha between
# sigma(g_W) and sigma(g_H) so that R_alpha restores T on the H-piece and withdraws T on the M1-piece.
gH = (-1, -1, 10)                     # R_B witness (T = B = '+', N = S)
cand = [g for g in GA if cls(g) == 1 and adv(KT, g) != adv(KN, g)]
def sigma(g):
    sg = 1 if adv(KT, g) == '+' else -1
    hM, hK = hmin(KT, g, sg), hmin(KN, g, sg); return hM / (hM - hK)
sH = sigma(gH)
gW = next((g for g in cand if sigma(g) < sH), None)
b6 = gW is not None
if b6:
    a = (sigma(gW) + sH) / 2
    RH, RW = adv(minkowski(KT, KN, a), gH), adv(minkowski(KT, KN, a), gW)
    # Z_H = T[H -> S]: S at gH, T at gW.  R_alpha: T at gH (restore), S at gW (withdraw).
    b6 &= RH == adv(KT, gH) and RW == 'S'
    r = lambda gg, x, w: rank(gg, x, w)
    d3 = (r(gH, RH, 3) < r(gH, 'S', 3), r(gW, RW, 3) > r(gW, adv(KT, gW), 3))
    d2 = (r(gH, RH, 2) > r(gH, 'S', 2), r(gW, RW, 2) > r(gW, adv(KT, gW), 2))
    d1 = (r(gH, RH, 1) > r(gH, 'S', 1), r(gW, RW, 1) < r(gW, adv(KT, gW), 1))
    print('   sigma(gH) = %s, sigma(gW) = %s, alpha = %s, gW = %s' % (sH, sigma(gW), a, gW))
    print('   world 3: gain on H-piece, loss on M1-piece: %s; world 2: loss on both: %s; world 1: loss, gain: %s'
          % (d3, d2, d1))
    b6 &= all(d3) and all(d2) and all(d1)
chk('B6 an explicit (H, alpha): R_alpha vs Z_H is mixed at worlds 3 and 1 but pointwise WORSE at world 2 '
    '(so R_alpha cannot dominate this Z_H; the guarantee is world-3 only)', b6)

# ---------- B7 NUMERICS ----------
random.seed(7)
E = []
while len(E) < 20000:
    g = (random.uniform(0.2, 1.0), random.uniform(0.2, 1.0), -random.uniform(0.5, 3.0))
    a3 = sum(float(x) * y for x, y in zip(v3, g))
    if a3 < 0: E.append((g, -a3 / (0.5 * (g[0] + g[1]) - a3)))
taus = sorted(x for _, x in E)
q1, q3 = taus[len(taus) // 4], taus[3 * len(taus) // 4]
tm = 0.5 * (q1 + q3)
ans = sum(1 for x in taus if x < tm) / len(taus)
print('   NUMERICS B7: E = a box in M3 n {v3.g<0}; quartiles of tau %.4f, %.4f; F_t at t = %.4f answers on %.3f '
      'of E and is silent on %.3f' % (q1, q3, tm, ans, 1 - ans))
print('ALL PASS' if ok else 'SOME FAIL')
