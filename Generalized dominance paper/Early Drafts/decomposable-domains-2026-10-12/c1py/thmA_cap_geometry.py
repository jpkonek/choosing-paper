"""C1 notes, Theorem A illustration (CHECKED-level geometry, exact rational arithmetic where it matters).

Setting: writeup conventions, eps=0.3, p*=u, facet data x = x_+ ; vertex b=2, failing edge [e1,e2]
(N28_referee failing_edge.out).  The referee's sector cap (counterexample C1) is K_q={q} on
S_2 = {phi <= phi_max ~ 0.129} near e2, phi measured from the failing edge.

We check:
 (1) the chosen cap point q0 passes the C1 facet constraints (A),(B) (re-using the referee's test);
 (2) q0 lies in the open chamber C = conv{u, e2, f}, f=(1/2,1/2,0) (foot of lambda_3 on [e1,e2]);
 (3) the set of directions of lines through q0 that leave C through BOTH chord sides (u,e2) and (u,f)
     has positive angular measure (exact, from the two angles subtended);
 (4) for two explicit such lines through a common chord point y in (u,e2), both meeting the cap, the
     corresponding gambles g, g' (identity sigma: l_g = L_g) satisfy l_g cap l_g' = {y}: Theorem A's
     fibration step would force K_y = {y}, a precise prior on the crossing chord lambda_2 -- excluded
     by Prop vertexfree (iv).
"""
from fractions import Fraction as Fr
import numpy as np, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'n28ref_py'))
from sector_caps2 import setup, viol

eps = 0.3
kap, v, xp = setup(eps)
E = np.eye(3)
u = np.ones(3) / 3
b, a, c = 1, 0, 2          # 0-based: b=e2, failing edge to e1, third e3
rho, phi = 0.05, 0.06
q0 = E[b] + rho * ((1 - phi) * (E[a] - E[b]) + phi * (E[c] - E[b]))
print("(1) q0 =", q0, " passes C1 constraints (A),(B):", not viol(q0, q0, v, xp))

f = np.array([0.5, 0.5, 0.0])
# barycentric coordinates of q0 w.r.t. (u, e2, f) in aff Delta (use coords 1,2)
M = np.array([[u[0], E[b][0], f[0]], [u[1], E[b][1], f[1]], [1, 1, 1]])
lam = np.linalg.solve(M, np.array([q0[0], q0[1], 1.0]))
print("(2) barycentrics of q0 in conv{u,e2,f}:", lam, " all >0:", bool((lam > 0).all()))

# (3) 2D coordinates in aff Delta: (q1,q2)
P2 = lambda q: np.array([q[0], q[1]])
Q, U, B, F = P2(q0), P2(u), P2(E[b]), P2(f)
ang = lambda w: np.arctan2(w[1], w[0])
# a line through Q (direction theta mod pi) exits C through the boundary sides hit by the two rays.
# Both exits on chord sides <=> neither ray hits the boundary side [B,F].
aB, aF = ang(B - Q), ang(F - Q)
span = abs((aB - aF + np.pi) % (2 * np.pi) - np.pi)      # angle subtended by [B,F] from Q (< pi)
print("(3) angle subtended by boundary side [e2,f] from q0: %.4f rad; bad-line directions (both exits on chords):"
      " measure pi - span = %.4f rad > 0" % (span, np.pi - span))

# (4) explicit: choose y on (u,e2), two lines through y and through cap points near q0
def line_gamble(p, r):
    """gamble g with l_g = line through probabilities p, r (g = p x r, adjusted so that g.1 arbitrary)."""
    return np.cross(p, r)
y = 0.93 * E[b] + 0.07 * u          # on lambda_2, between u and e2
qa = E[b] + rho * ((1 - 0.03) * (E[a] - E[b]) + 0.03 * (E[c] - E[b]))
qb = E[b] + rho * ((1 - 0.10) * (E[a] - E[b]) + 0.10 * (E[c] - E[b]))
for nm, qq in [("qa", qa), ("qb", qb)]:
    print("    cap point", nm, qq, " passes (A),(B):", not viol(qq, qq, v, xp))
g1, g2 = line_gamble(y, qa), line_gamble(y, qb)
for nm, g, qq in [("g1", g1, qa), ("g2", g2, qb)]:
    # does this line leave C through both chord sides?  intersect with segment (u,f) and (u,e2)
    s = np.sign(g @ np.array([u, E[b], f]).T)
    print("    %s = %s ; signs of g at (u,e2,f): %s ; mixed: %s" % (nm, np.round(g, 5), s, bool((g > 0).any() and (g < 0).any())))
# exact intersection of l_g1 and l_g2
G = np.vstack([g1, g2, np.ones(3)])
m = np.linalg.solve(G, np.array([0, 0, 1.0]))
print("(4) l_g1 cap l_g2 =", m, " equals y:", np.allclose(m, y), "  y on lambda_2 (det(u,e2,y)=0):",
      abs(np.linalg.det(np.vstack([u, E[b], y]))) < 1e-14)
# does line(y,qa) cross (u,f)?  parametrise and check
def crosses(gm, P0, P1):
    s0, s1 = gm @ P0, gm @ P1
    return s0 * s1 < 0
for nm, g in [("g1", g1), ("g2", g2)]:
    print("    %s line crosses open side (u,f): %s, crosses open side (u,e2) at y (interior): True;"
          " crosses boundary side (e2,f): %s" % (nm, crosses(g, u, f), crosses(g, E[b], f)))

print("\n(4') search: lines through a fixed y on (u,e2) and a C1-cap point that leave C through BOTH chord sides")
y = (1 - 0.006) * E[b] + 0.006 * u
print("    y =", y, "(on lambda_2, interior)")
found = []
for rr in np.linspace(0.02, 0.3, 57):
    for ph in np.linspace(0.005, 0.125, 49):
        qq = E[b] + rr * ((1 - ph) * (E[a] - E[b]) + ph * (E[c] - E[b]))
        if viol(qq, qq, v, xp):
            continue
        g = line_gamble(y, qq)
        if crosses(g, u, f) and not crosses(g, E[b], f):
            found.append((rr, ph, qq, g))
print("    admissible cap points giving such lines:", len(found))
if len(found) >= 2:
    (r1, p1, qa, g1), (r2, p2, qb, g2) = found[0], found[-1]
    m = np.linalg.solve(np.vstack([g1, g2, np.ones(3)]), np.array([0, 0, 1.0]))
    print("    e.g. cap points (rho,phi)=(%.3f,%.3f) and (%.3f,%.3f); l_g1 cap l_g2 = %s = y: %s" %
          (r1, p1, r2, p2, np.round(m, 6), np.allclose(m, y)))
    print("    g1 =", np.round(g1 / abs(g1).max(), 5), " g2 =", np.round(g2 / abs(g2).max(), 5))
