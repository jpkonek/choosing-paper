# REF62 — Referee report on FD62_notes.md (25 Oct 2026)

Labels: PROVED (proved here by the referee; not yet independently refereed) / CHECKED (exact rational computation) / CONJECTURE / NUMERICS.
Scripts (all in `ref62py/`, run with `python3 -I`): `ref62_a.py` (+`.out`), `ref62_a2.py` (+`.out`), `ref62_b.py` (+`.out`), `ref62_c.py` (+`.out`).

## 0. Summary

FD62 is sound in its main claims:
- the auditor's counterexample;
- the reading of F61 Thm D as relative coherence;
- the domain dichotomy FD-1;
- Lemma FD-3;
- the box chart FD-B;
- the corner-type reconciliation.

I found:
- one scope **ERROR**: "open only for strictly sign-correct charts" (FD-1b, §0, row 17);
- one wording **ERROR**: "exactly the |W0| = 1 family";
- several **GAPs**:
  - FD-1a fails for a singleton K′;
  - FD-1c leaves (LF) unnamed;
  - the LP in `thmD_global.py` tests a sufficient condition only;
  - the n = 3 restriction in §2.2 is essential;
  - E61 Cor 5.2 is understated.

I also add two referee results that change the status table:
- **Thm R1 (rigidity).** On the full domain, regular certificate charts force "orthant-diagonal" structure. Continuous ones give exactly the normalised boxes. So T1 and the reversed triangle cannot be covered on any two-sided domain through the certificate. This settles FD's OPEN item for that route.
- **Prop R2 (orthant-planar targets).** Every target whose D_K is planar on each mixed orthant is covered, both on the full domain and on every one-sided U. Examples are a non-box hexagon and a sharp *triangle* with a crossing world at every vertex.

## 1. Verdict table

| # | FD62 item | Verdict | Notes |
|---|---|---|---|
| 1 | Auditor counterexample on A_K (x = (1,−1,−20), y = (1,4,−1)) | **CORRECT** (CHECKED) | Reproduced independently. Margins are 1, 1 and 5/3, so sup-radius < 5/6 works. 0/20 000 failures under random interior perturbations of radius 0.8 (`ref62_a.out`). |
| 2 | Lemma W1: A ∩ {h_i>0} is undominated under strict (G) alone | **CORRECT** | Hidden hypotheses that should be named: (i) every measurable subset of A is a model (decomposability); (ii) silence is on every pair's menu; (iii) (G) compares the four advice types pointwise. |
| 3 | What F61 Thm D proves: (RC), not (GC); D_K is undominated and (GC) | **CORRECT** | |
| 3a | "X* is (GC) if K ⊆ K*" | CORRECT | D_K ⊆ A_K. |
| 3b | "n = 3, \|W0\| ≥ 2 ⇒ X* = D_{K*}" | **CORRECT, but n = 3 is essential** | Proof checked. For n = 4, 5 and \|W0\| = 2, 3, D_{K*} ⊄ A_K often (n = 4, \|W0\| = 2: 71/100; NUMERICS `ref62_a.out` §3). FD's "NUMERICS otherwise" refers to n = 3 only. |
| 3c | "global coherence is false … exactly the \|W0\| = 1 family" | **ERROR (wording)** | Inside \|W0\| = 1 both outcomes occur (`ref62_a2.out`: 83 fail, 29 pass). Correct reading: at n = 3, failures occur only when \|W0\| = 1, and not for every such model. |
| 3d | LP "GLOBAL-FAIL" in `thmD_global.py` | **GAP (closed numerically)** | The LP tests D_{K*} ⊄ A_K. That shows X* ≠ D_{K*}, not that X* fails to be D_Q for some other Q. An exact-decision LP (x, y ∈ X*, x+y ∉ A_K, polyhedral pieces) finds X* non-convex in 83/83 such cases and convex in all others (NUMERICS). Exact test for n = 3, W0 = {k} (PROVED via Lemma 0): D_{K*} ⊆ A_K iff v_k, v_l ∈ cone(K* ∪ {e_l}) for both l ≠ k. It agrees with the LP in 600/600 draws. |
| 4 | Thm FD-1 (domain dichotomy) | **CORRECT** (PROVED; every step re-derived) | Steps 1–6 hold. The edge argument with f = 1 − m_i − m_j is right, and the dichotomy is exhaustive and exclusive. **Strengthening:** only the n world-best models B_i need to be (GC); "every undominated model" is more than needed. Hidden hypotheses: decomposability, μ with a positive density (Lemma 0(ii)), D_K ⊆ A a.e. |
| 5 | FD-1a: "U ∪ (−U) … inadmissible" | **GAP (minor ERROR)** | If K′ = {p} then U ∪ −U = {p·h ≠ 0}, which is the full domain a.e. FD-1 then gives no exclusion. Add "K′ not a singleton". Exact witness for K′ = conv{(.4,.3,.3), (.3,.4,.3)}: x = (13/5, −3/2, 19/4) ∈ U and y = (1/2, −7/5, −9/2) ∈ −U both have h_1 > 0, but x+y = (31/10, −29/10, 1/4) ∉ U ∪ −U (`ref62_b.out`). A_K itself is fine. |
| 6 | FD-1b: two-sided coverage of T1 under (GC) = the full-domain problem | **CORRECT** | "Exactly" needs a one-line extension argument (lexicographically penalise accepted sure losses), which is routine. |
| 6′ | "There … strictly sign-correct charts are OPEN"; row 17 "open only for strictly sign-correct charts" | **ERROR (scope)** | The analysed classes are not exhaustive. F61 §5 itself lists mixed veto/signed classes, signed levels with flat regions, non-lexicographic or incomplete orders, and non-integral rankings as untouched. Also, the certificate route for strictly sign-correct charts is now closed for T1 and the reversed triangle (Thm R1 below). |
| 7 | FD-1c (lower-dimensional targets need the full domain) | **CORRECT with GAP** | It inherits (LF) from P61 D1 and O61 Rem 1.1, so (LF) must be named. "Degenerate boxes (some l_j = u_j)": ν(Q) is lower-dimensional only if at least two coordinates are degenerate. |
| 8 | FD-1d (n = 2), FD-1e (one-sided branch) | CORRECT (remarks) | |
| 9 | Lemma FD-3 (full-domain Bayes acts at prior π are cylinders over supp π) | **CORRECT** | The proof should say that a contradiction loses to accepting h at every world in S, by (G). It is necessary wherever X_π must be coherent: under the certificate, at unique Bayes acts, or by limits from a.e. priors. It is much stronger than FD indicates (Thm R1). |
| 10 | Prop FD-B: box chart c_j = min(l_j h_j, u_j h_j) meets all four certificate conditions, on ℝⁿ and on every U = D_{K′} | **CORRECT** | Re-verified. π·c = min_Q(π⊙q)·h; concavity gives superadditivity; zero sets are null; π·c(h) + π·c(−h) ≤ 0; contradiction scored −2u_j\|h_j\|; B_𝟙 = D_K. The certificate itself needs only K′ ⊆ K; relint is used for (LF). |
| 11 | COR set = ν(p⊙[1,k]ⁿ); chart = Walley's E_p h⁺ > k·E_p h⁻; covered | **CORRECT** | |
| 12 | Corner types: boxes S/T/A only; reversed triangle and interior PMMs A/C only; interval vertices with \|H\| ≥ 2 all A/C | **CORRECT** | Generators u_i e_j − l_j e_i verified by hand. ν(l) and ν(u) are never vertices: l ∈ cone{l + d_i e_i}, and similarly for u. So enumerating H, L ≠ ∅ is right. |
| 13 | Reconciliation §4.3, items 1–18 | **CORRECT except as noted** | (i) Item 7 / row 9: concave charts are excluded for **every interior triangle in general position** (R10a Thm R = E61 Cor 5.2), not only the reversed triangle. The correction is understated. (ii) Item 6: O61 Thm B extends to every interior n = 3 PMM triangle; see §3. (iii) Row 21 says "Cor A(d): one-world tangency sketched", while ROUND61 §4.5 says "repaired for n = 3 polytopes". Reconcile the two. |
| 14 | Corrected status table §6 | **Mostly CORRECT** | Fix row 17 (ERROR above), FD-1a, and the §2.2 wording. Add rows for Thm R1 and Prop R2, and the O61 Thm B upgrade. |

## 2. Referee additions (PROVED, not independently refereed)

### Lemma R0 (edge-ratio lemma; strengthens FD-3)
- *Hypotheses.* Full domain. c is strictly sign-correct and positively homogeneous. For π = a e_i + b e_j (a, b > 0), {π·c = 0} is null and B_π := {π·c > 0} is (GC).
- *Conclusion.* On {h_i > 0 > h_j},
  c_i(h)/(−c_j(h)) = g_ij(h_i/(−h_j))  a.e.
  for a nondecreasing g_ij. This holds whatever the other coordinates are.
- *Proof.*
  - By FD-3, B_π = D_Q with Q ⊆ [e_i, e_j]. On the quadrant, D_Q is {ρ > τ}, where ρ = h_i/(−h_j).
  - Also B_π ∩ quadrant = {c_i/(−c_j) > b/a}.
  - Run b/a over the rationals. ∎

### Theorem R1 (full-domain rigidity)
- *Hypotheses.*
  - n ≥ 3, full domain.
  - c is positively homogeneous and strictly sign-correct.
  - **Regularity (R):**
    - on each closed orthant, c is locally Lipschitz;
    - c_j/h_j is bounded above and below by positive constants on compact subsets away from 0. (The round-62 continuous piecewise-linear ansatz satisfies this.)
  - For every nonzero π ≥ 0, {π·c = 0} is null and B_π = {π·c > 0} is (GC). This is the auditor's certificate with U = ℝⁿ. Interior priors a.e. plus limits suffice.
  - B_{π*} = D_K for some π* ≫ 0.
- *Conclusion.*
  - Every g_ij is linear: g_ij(ρ) = κ_ij ρ.
  - So on each mixed orthant σ, c(h) = λ(h)·d_σ⊙h, with λ > 0 and d_σ ≫ 0 constant.
  - Hence ∂D_K is planar inside every mixed orthant ("orthant-planar").
  - If c is continuous, then d_σ,j depends only on sign(h_j) (trivial holonomy), so **K is a normalised box**.
- *Proof sketch.*
  1. **Concavity of g_ij.** Take the orthant h_i > 0 > h_j, h_k > 0 and slice at h_j = −1. B_π is {π_i g_ij(a) + π_k g_kj(b) > π_j}, using Lemma R0 for the pairs (i,j) and (k,j). Convexity for all weights means that, for every λ > 0, the superlevel sets of λ g_ij + g_kj are convex. Let λ → 0 and differentiate F = g_kj⁻¹ at a point where F′ > 0 (by (R)). The pointwise limit −F′ g_ij is convex, so g_ij is concave.
  2. **Convexity of φ.** Take the orthant h_i > 0 > h_j, h_k and slice at h_i = 1. The same argument gives φ_j(S) := 1/g_ij(1/S) convex, with φ_j(0⁺) = 0 by (R).
  3. **Linearity.** g concave with g > 0 makes g(ρ)/ρ nonincreasing. φ convex with φ(0⁺) = 0 makes φ(S)/S = ρ/g(ρ) nondecreasing in S, that is, nonincreasing in ρ. Hence g(ρ)/ρ is constant.
  4. **Continuity.** It forces λ_σ d_σ = λ_σ′ d_σ′ off the flipped coordinate. Around the cycle of mixed orthants the product of jump factors must be 1. Rescale along a spanning tree.
  5. **Box.** d_σ,j depends only on σ_j. Convexity of B_𝟙 forces l ≤ u. ∎
- *Consequences.*
  - T1 and the reversed triangle are not orthant-planar. Their rays (−1,−1,5)/12 and (−3,2,2)/25 have no zero coordinate, and some mixed orthants meet two facets (CHECKED, `ref62_c.out`).
  - So **no regular chart satisfies the full-domain certificate for them**. With FD-1, no regular certificate chart covers them on any two-sided domain under (GC).
  - On the full domain, continuous certificate charts reach **exactly the normalised boxes**. This matches F61 Thm A (convex first levels) and extends it to non-convex charts.
- *What stays OPEN on two-sided domains:* irregular charts, non-null ties at the target, rankings whose Bayes acts are not {π·c > 0} (double-positive pairs), and the non-chart classes in row 6′.

### Proposition R2 (orthant-planar targets are covered)
- *Hypotheses.* K ⊆ relint Δ. For every mixed orthant σ, D_K ∩ σ = {d_σ·h > 0} ∩ σ.
- *Chart.* c(h) := d_{σ(h)} ⊙ h, with any positive weights on the two pure orthants.
- *Conclusion.* The four certificate conditions hold on ℝⁿ and on every U = D_{K′}, for any nonempty compact convex K′ ⊆ K. Namely:
  - B_π = D_{ν(π⊙K)} for every nonzero π ≥ 0;
  - zero sets are null;
  - at most one orientation is positive;
  - B_𝟙 = D_K.
- *Proof.*
  - For π ≫ 0, π·c(h) = d_σ·(π⊙h) and π⊙h ∈ σ. So B_π = diag(π)⁻¹D_K = D_{ν(π⊙K)}.
  - For π with zeros: D_K ∩ cl σ = {d_σ·x > 0} ∩ cl σ, because a boundary point x with d_σ·x > 0 could be pushed into σ ∖ cl D_K. ∎
- *n = 3 geometry.* K is orthant-planar iff every edge line of the polygon K passes through a vertex of Δ, so K has at most 6 edges. The boxes are the hexagons of this kind with trivial holonomy, a Ceva-type product condition.
- *Examples (CHECKED, exact random tests, 0 failures; `ref62_b.out`, `ref62_c.out`).*
  - **Non-box hexagon:** vertices (1,2,2), (1,1,2), (2,1,2), (2,1,1), (2,11/5,1), (11/10,11/5,1). Its holonomy is 11/10, and sympy finds no box representation.
  - **Cyclic triangle** conv{(1,4,2), (2,1,4), (4,2,1)}/7. It is not a box (l_1 = 8l_1 would be forced). Its vertex types are ATC, CAT and TCA: each vertex has a *crossing* world and none is strictly visible.
  - Both are therefore **not VB-type**. The triangle is also outside 𝒱_B by O61 Thm A with Cor A(d) (one-world tangency, repaired for n = 3).
  - The triangle is not in general position, so R10a Thm R does not apply. The chart is discontinuous, so it is neither convex nor concave, and E61 Cor 5.2 and O61 Thm B do not apply either.
  - So **a sharp-cornered triangle is exactly covered**. "Sharp corners" is no obstruction even for triangles. The live distinction for triangles is general position.

## 3. O61 Thm B for interior n = 3 PMM triangles (upgrade from CONJECTURE)

- *Setting.* K = {m ∈ Δ : m_i ≤ u_i} with u = (1+δ)p, every vertex having two coordinates at their upper bounds.
- *Vertex pattern.* Each vertex is ACC (anti-visible from the free world, crossing for the others). Each ray u_i𝟙 − e_i lies on two faces, and every world crosses on at least one of them.
- *Rays.* The ray matrix has det = u_1 + u_2 + u_3 − 1 = δ ≠ 0 (CHECKED, sympy).
- *Conclusion.* Steps 1–6 of O61 Thm B go through verbatim: x = π⊙κ̂ = 0 forces π = 0. **PROVED (referee sketch).**

## 4. Corrected entries for FD62 §6

- **Row 7.** Add: orthant-planar targets are covered by orthant-diagonal charts, on ℝⁿ and on every U (Prop R2). Examples: the non-box hexagon and the cyclic triangle.
- **Row 9.** Concave charts: excluded for all interior triangles in general position (R10a Thm R). Convex error levels: excluded for all interior n = 3 PMM triangles (§3).
- **Row 13.** Add: full domain with the certificate and regular charts — continuous charts give exactly the boxes, and charts discontinuous across coordinate planes give exactly the orthant-planar targets (Thm R1 + Prop R2).
- **Row 17.** Replace with: *"T1 / reversed triangle on two-sided domains under (GC) = the full-domain problem (FD-1). The certificate route with regular charts is impossible (Thm R1). OPEN only outside it: irregular charts, tied target, double-positive Bayes acts, mixed / flat / non-lexicographic / non-integral rankings."*
- **§2.2.** Replace "exactly the |W0| = 1 family" with: *"(n = 3) |W0| ≥ 2 ⇒ globally coherent (PROVED); |W0| = 1: globally coherent iff v_k, v_l ∈ cone(K* ∪ e_l) for l ≠ k (sufficiency PROVED, necessity NUMERICS 83/83); for n ≥ 4, |W0| ≥ 2 does not suffice (NUMERICS)."*
- **FD-1a.** Add "K′ not a singleton".
- **FD-1c.** Name (LF).

## 5. Implication for round 62

- Thm R1 shows that the two-sided route is closed for the reversed triangle under the certificate.
- The edge-prior cylinder constraint (FD-3) is exactly what one-sided U avoids, since there Q_π ⊆ conv(K′ ∪ Δ_S) only. So the constructive search belongs on one-sided U, as BRIEF62 already directs.
- Orthant-planar charts give a new positive control besides boxes, including a sharp triangle. They are the natural starting family for piecewise charts on U: refine the cones beyond the orthants and let K′ absorb the non-planar part.
