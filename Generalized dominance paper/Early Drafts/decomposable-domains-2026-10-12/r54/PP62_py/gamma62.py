"""PP62 (NUMERICS): the source map Gamma(a, a') = Phi(C_a) - Phi(C_a') for the balanced field u1.

Phi(Y) = int u1(g, Y(g)) dmu over the disagreement region (h/S part only); for two members
Phi(C_a') - Phi(C_a) = int phi(g) (1[C_a' answers] - 1[C_a answers]) dmu,
phi(g) = |g| * (-|Wr| on Cor(h), +|Cor| on Wr(h)), h = the common answer (sign of g1+g2+g3 under (2V)).
Gamma(a,a') = V(rec(C_a', C_a)) = u1-loss of C_a minus u1-loss of C_a' (per world).
Gamma_w > 0 : C_a' is u1-better than C_a at w.
O_w = {x in Pi : x_v < 0 for both v != w}.

Prints, for a in {u, B, D}: the six pure shifts a o (1 + t e_w)^{+-1}, finite-difference Gamma / t,
the odd-world composition of the moved layer, and whether Gamma lies in O_1, O_2, O_3.
Also the 2x2 Jacobian rank of a -> Phi(C_a) (in coordinates of Pi).
Standard Gaussian mu; common random numbers; Monte Carlo (NUMERICS only).
"""
import numpy as np

rng = np.random.default_rng(54062)
EPS = 0.3
C0 = (1 - EPS) / 3
VERT = np.array([[C0 + (EPS if i == v else 0) for i in range(3)] for v in range(3)])
N = 4_000_000
G = rng.standard_normal((N, 3))
NORM = np.linalg.norm(G, axis=1)
H = np.sign(G.sum(axis=1))[:, None] * G          # oriented so the (2V) answer is +H
COR = H > 0                                        # worlds where answer is correct
ncor = COR.sum(axis=1)
mixed = (ncor == 1) | (ncor == 2)
PHI = np.where(COR, -(3 - ncor)[:, None], ncor[:, None]) * NORM[:, None]
PHI[~mixed] = 0.0
odd = np.where(ncor == 1, np.argmax(COR, axis=1), np.argmin(COR, axis=1))


def answers(a):
    s = H @ (VERT * np.asarray(a)).T             # s_v = sum_i a_i m_{v,i} H_i
    return (s > 0).all(axis=1)


def Phi(a):
    A = answers(a) & mixed
    return (PHI * A[:, None]).sum(axis=0) / N, A


def report(name, a, t=0.01):
    a = np.asarray(a, float)
    P0, A0 = Phi(a)
    print(f'--- a = {name} = {np.round(a, 5)}  (t = {t})')
    J = []
    for w in range(3):
        for sgn in (+1, -1):
            b = a * (1 + sgn * t * np.eye(3)[w])
            b = b / b.sum()
            P1, A1 = Phi(b)
            gam = (P0 - P1) / t                  # Gamma(a, b)/t
            lay = A0 ^ A1
            comp = [float((NORM * (lay & (odd == k) & mixed)).sum() / N / t) for k in range(3)]
            inO = [all(gam[v] < 0 for v in range(3) if v != k) for k in range(3)]
            print(f'  shift {"+" if sgn > 0 else "-"}e{w+1}: Gamma/t = {np.round(gam, 4)}  sum={gam.sum():+.1e}'
                  f'  layer mass by odd world = {np.round(comp, 4)}  in O_1,O_2,O_3: {inO}')
            if sgn > 0:
                J.append(-gam)
    J = np.array(J)                               # rows: dPhi along +e_w (3 vectors in Pi)
    basis = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[2 ** .5], [6 ** .5]])
    Jc = J @ basis.T
    sv = np.linalg.svd(Jc[:2], compute_uv=False)
    print('  dPhi(+e_w) in Pi-coordinates:', np.round(Jc, 4), ' singular values (e1,e2 block):', np.round(sv, 4))


if __name__ == '__main__':
    report('u', [1 / 3] * 3)
    report('B', [406 / 1200, 421 / 1200, 373 / 1200])
    report('D', [406 / 1200, 373 / 1200, 421 / 1200])
    report('a1', [0.34, 0.335, 0.325])
