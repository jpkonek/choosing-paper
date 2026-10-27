import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'c2py'))
import ld_two_world as L
F = {'Fa': L.F_MEMBERS['Fa'], 'Fc': lambda x: 2.0 - x}
sysm = L.System(F, L.G_MEMBERS_ADD)
tested = fails = 0
for s in L.S_GRID[1:-1:40]:
    c = L.chain(s); A = c[:]
    lo = sorted([i for i in range(L.NCELL) if L.XM[i] < s], key=lambda i: L.XM[i])[:3]
    hi = sorted([i for i in range(L.NCELL) if L.XM[i] > s], key=lambda i: -L.XM[i])[:3]
    if not lo or not hi: continue
    tested += 1
    for i in lo: A[i] = 0.0
    need = 1.02 * sum(L.MASS[i] for i in lo)
    for i in hi:
        t = min(1.0, need / L.MASS[i]); A[i] = t; need -= t * L.MASS[i]
        if need <= 0: break
    ok = sysm.le1(c, 0.0, A, 0.0) or sysm.le2(c, 0.0, A, 0.0)
    fails += not ok
    if ok: print("not failing at s =", s)
print("tested", tested, "fails", fails)
