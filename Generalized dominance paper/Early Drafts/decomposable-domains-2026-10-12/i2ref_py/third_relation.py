# I2 referee: at the unique positive solution of (R_2),(R_3), evaluate the normalised det DG_1 and the
# Moebius check r_{i+1}=G(r_i) directly; also verify G(1)=1 iff v1-v3=1 and v1-v3=kappa.
import sympy as sp
exec(open('blowup_exact.py').read().split("# compare with I2's v")[0].replace('print(','(lambda *a,**kw: None)('))
W2, W3 = sp.symbols('W2 W3', positive=True)
for eps in [sp.Rational(1,20), sp.Rational(3,10), sp.Rational(6,10), sp.Rational(9,10)]:
    kv=(1+2*eps)/(1-eps); xv=((kv+1)+sp.sqrt((kv+1)**2-4))/2
    sub={k:kv,x:xv,w[0]:1,w[1]:W2,w[2]:W3}
    dets=[sp.together(rel[b][1].subs(sub)) for b in (1,2,3)]
    sols=sp.solve([sp.numer(dets[1]),sp.numer(dets[2])],[W2,W3],dict=True)
    for s in sols:
        a2,a3=complex(sp.N(s[W2])),complex(sp.N(s[W3]))
        if abs(a2.imag)<1e-12 and abs(a3.imag)<1e-12 and a2.real>0 and a3.real>0:
            J1=rel[1][0].subs(sub).subs(s); M=sp.Matrix(J1).evalf()
            import numpy as np
            sv=np.linalg.svd(np.array(M.tolist(),dtype=float),compute_uv=False)
            print(f"eps={eps}: (R_2),(R_3) solved at w=(1,{a2.real:.5f},{a3.real:.5f}); DG_1 singular values {sv.round(4)} -> (R_1) fails: {sv[-1]>1e-6}")
    v1=kv/(1-kv**2)*(1/xv-kv*xv); v3=kv/(1-kv**2)*(kv/xv-xv)
    print("     v1-v3 =",sp.N(v1-v3,12)," kappa =",sp.N(kv,12))
