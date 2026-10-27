"""chain68: the G-closed second-generation chain (PP68 Prop 4.5).

L(t) := D_{conv(v3(t), M0)}, v3(t) = v3 + t*(h12 - v3), v3 = c*1 + eps*e3, M0 = [(16,7,0),(7,16,0)]/23.
N = D_{conv(M u M0)} (PP67).  Checks, exact on samples (geom68.samples):
  C1  L(0) is weakly 3-worse than N; it differs from N only by new B answers on classes 1 and 2
      (3-wrong), and L(0) = N on class 3 (so it is silent wherever N is silent on class 3);
  C2  for t in a grid 0 < t1 < t2 < ... < 1: L(t_{k+1}) is weakly 3-worse than L(t_k), and every new
      answer is 3-wrong (A on class 3, B on classes 1 and 2);
  C3  L(t) keeps a non-null class-3 silence for every grid t < 1 (so its fills exist), and the
      class-3 silence shrinks to nothing on the samples as t -> 1 (L(1) = D* = A on class 3).
Run: python3 -I -B chain68.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geom68 import *

G = [g for g in samples() if g[0] + g[1] != 0]
v3 = M[2]
KP = M + KD
rk = lambda g, a, w: 1 if a == 'S' else (0 if correct(g, a, w) else 2)


def L(t):
    return [tuple(v3[i] + t * (h12[i] - v3[i]) for i in range(3))] + KD


def newtypes(Kold, Knew):
    s = set()
    for g in G:
        a, b = ans(Kold, g), ans(Knew, g)
        if a != b:
            s.add((cls(g), AB(g, a), AB(g, b)))
    return s


def worse3(Kold, Knew):
    return all(rk(g, ans(Knew, g), 3) >= rk(g, ans(Kold, g), 3) for g in G)


ok = True
t0 = newtypes(KP, L(F(0)))
c1 = worse3(KP, L(F(0))) and t0 <= {(1, 'S', 'B'), (2, 'S', 'B')} and len(t0) == 2
print('C1 L(0) weakly 3-worse than N; new answers', sorted(t0), c1)
ok &= c1
grid = [F(k, 10) for k in range(0, 10)] + [F(99, 100), F(999, 1000)]
allowed = {(3, 'S', 'A'), (1, 'S', 'B'), (2, 'S', 'B')}
c2 = True
for a, b in zip(grid, grid[1:]):
    nt = newtypes(L(a), L(b))
    w = worse3(L(a), L(b))
    c2 &= w and nt <= allowed and len(nt) > 0
    sil = sum(1 for g in G if cls(g) == 3 and ans(L(b), g) == 'S')
    print('   t=%-6s -> %-7s weakly 3-worse: %s; new answer types %s; class-3 silent samples left %d'
          % (a, b, w, sorted(nt), sil))
print('C2 chain is strictly descending at world 3 with only 3-wrong new answers:', c2)
ok &= c2
sil1 = sum(1 for g in G if cls(g) == 3 and ans(KD, g) == 'S')
print('C3 class-3 silence of D* = L(1) on samples:', sil1, '(0 expected)')
ok &= sil1 == 0
print('ALL PASS' if ok else 'SOME FAIL')
