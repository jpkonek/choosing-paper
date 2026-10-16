# I2 referee: solve the three relations det DG_b = 0 (b=1,2,3) exactly for w>0 (w1=1), x=x_+,
# and check kernels lie in the open sectors. Also: is each single relation solvable?
import sympy as sp, itertools
exec(open('blowup_exact.py').read().split("# compare with I2's v")[0].replace('print(','(lambda *a,**kw: None)('))
W2, W3 = sp.symbols('W2 W3', positive=True)
for eps in [sp.Rational(1,20), sp.Rational(3,10), sp.Rational(6,10), sp.Rational(9,10)]:
    kv = (1+2*eps)/(1-eps); xv = ((kv+1)+sp.sqrt((kv+1)**2-4))/2
    sub = {k: kv, x: xv, w[0]: 1, w[1]: W2, w[2]: W3}
    nums = [sp.numer(sp.together(rel[b][1].subs(sub))) for b in (1,2,3)]
    # solve pairs then test third
    sols = sp.solve([nums[1], nums[2]], [W2, W3], dict=True)
    real_pos = []
    for s in sols:
        a2, a3 = complex(sp.N(s[W2])), complex(sp.N(s[W3]))
        if abs(a2.imag) < 1e-12 and abs(a3.imag) < 1e-12 and a2.real > 0 and a3.real > 0:
            r1 = float(sp.N(nums[0].subs({W2: s[W2], W3: s[W3]})))
            real_pos.append((a2.real, a3.real, r1))
    print(f"eps={eps}: positive solutions of (R_2),(R_3): {[(round(a,5),round(b,5)) for a,b,_ in real_pos]}; residual of (R_1) there: {[f'{r:.3e}' for *_,r in real_pos]}")
    # each single relation solvable with kernel in open sector?  b=2: kernel y3/y1 in (0,1)
    J = rel[2][0].subs(sub)
    for w2v in [0.5, 1.0, 2.0]:
        s3 = sp.solve(nums[1].subs(W2, w2v), W3)
        for s in s3:
            sv = float(sp.N(s))
            if sv > 0:
                Jn = sp.N(J.subs({W2: w2v, W3: sv}))
                ker = sp.Matrix(Jn).nullspace(simplify=True)
                # numeric kernel
                import numpy as np
                M = np.array(Jn.tolist(), dtype=float); u_, s_, vt = np.linalg.svd(M); kv_ = vt[-1]; kv_ = kv_/kv_[0]
                print(f"   (R_2) alone: w=(1,{w2v},{sv:.4f}) sing.val {s_[-1]:.1e}, kernel (y1,y3)=(1,{kv_[1]:.4f}) in open sector: {0<kv_[1]<1}")
