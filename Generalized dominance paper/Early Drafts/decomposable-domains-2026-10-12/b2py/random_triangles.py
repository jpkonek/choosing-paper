"""Run the geometric checks G1, G2, G4-G7 of geom_checks.py on random all-facing triangles in general
position (the facts used in Theorem B2.1 for general all-facing targets). NUMERICS."""
import numpy as np
import geom_checks as gc

rng = np.random.default_rng(1)
E = np.eye(3)


def random_allfacing():
    while True:
        V = [rng.dirichlet(np.ones(3) * 3) for _ in range(3)]
        ok = True
        for k in range(3):
            i, j = [x for x in range(3) if x != k]
            M = np.vstack([E[k], V[i], V[j]]).T
            try:
                lam = np.linalg.solve(M, V[k])
            except np.linalg.LinAlgError:
                ok = False
                break
            ok &= bool(np.all(lam > 1e-3))
        # general position: no line through two v's contains a vertex of Delta
        for a in range(3):
            for b in range(a + 1, 3):
                n = np.cross(V[a], V[b])
                ok &= all(abs(np.dot(n, E[l])) > 1e-6 for l in range(3))
        if ok:
            return V


cnt = 0
fails = {}
for trial in range(300):
    V = random_allfacing()
    gc.T1_vertices = lambda eps, V=V: V  # monkeypatch
    res = gc.report(0.0)
    for name, v in res:
        if name.startswith(("G3", "G8")):
            continue  # cap/hexagon labels are T1-specific in the script
        if not v:
            fails[name] = fails.get(name, 0) + 1
    cnt += 1
print(f"{cnt} random all-facing triangles; failures: {fails if fails else 'none'}")
