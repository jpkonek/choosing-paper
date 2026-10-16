# I2 referee report (14 Oct 2026, round 10)

Referee for convex analysis and projective geometry. Object: `I2_notes.md`, read in full, with `i2py/`.
Sources checked against: writeup §§2–5 (*The Contamination Triangle.tex*), N15, N18, N12, N14 (Thm C2), N21, N23,
N28, N28_referee (§4.3, C1, N1), R4 (Thms A, B, Prop D, Prop F), R8 (Prop D verdict), R10a (Thm M, as a test
family). Independent scripts: `i2ref_py/`. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.

## 0. Verdict

| Step | Item | Verdict |
|---|---|---|
| 1 | Lemma 1 (no straddling on the positive side) | **CONFIRMED WITH REPAIR** (a trivial missing case in step 4) |
| 2 | Theorem 2 (positive state; exact facet behaviour at non-precise priors near e_b) | **CONFIRMED** |
| 3 | Theorem 3 (failing box ⇒ precise collar) | **CONFIRMED** |
| 4a | Prop 4(a) (collar map is diagonal-projective) | **GAP as written, CONFIRMED WITH REPAIR.** I2 cites R4 Prop D as CHECKED, but R8 recorded a GAP in Prop D's dichotomy ("non-constant ⇒ injective"), and the Consolidated Statements list it as GAP. Repair: Prop D* below (proved here; one reader) |
| 4b,c | Prop 4(b),(c) (global transport, one w at all three vertices) | **CONFIRMED**. They need σ_w only on some nonempty open subset of one collar |
| 5 | Lemma 5 and existence of transition points at every small radius | **CONFIRMED** |
| 6 | Theorem 6 (blow-up, relations (R_b), Möbius cycle, corner equation) | **CONFIRMED**, recomputed exactly at all three vertices without using the cyclic symmetry |
| 7 | Over-exclusion of genuine covers | **None found**. The distinguishing input is the box certificate in Theorem 3, which exists for T1 because the corner equation forces x₊² > κ. It cannot exist for any cover with half-plane charts near the target (gauge mixtures, U-domain covers), and two-world targets have no such facets |
| — | Status line of I2 §0 and §7 | **WRONG as stated.** Prop D is not "CHECKED, the only non-PROVED input". Several inputs are one-referee results, Prop CF (⇒) is CHECKED, and the charge clause rests on N14 Thm C2. Corrected list in §9 |

**Bottom line.** With the repair D*, the chain is correct. What is established (§8) is the following. No strictly guiding additive cover of T1 exists on any decomposable domain with (LF), for any ε ∈ (0,1) and any interior target prior. This holds for integral penalties, and for bounded charges given interior Bayes minimisers. The status is PROVED from the cited inputs plus Prop D* (referee-proved here, one reader) and the classical local fundamental theorem of projective geometry. Hence CF(T1) has no solution, at the status of CCIBU. Second readings of Lemma 1, Theorem 3 and Prop D* are the priority.

I tried hard to break steps 1, 3 and 4 and could not. The only real hole was the inherited Prop D gap, and it closes. The closing route is the one R8 suggested, a sign-class count, combined with a convexity argument for plateau boundaries.

---

## 1. Lemma 1: no straddling on the positive side. CONFIRMED WITH REPAIR

**Quantifiers (brief priority 1).** The worry was that the lemma speaks of the specific facet gamble h, while charts exist only for a.e. g, with no continuity of g ↦ c(g). The proof does not use continuity. It runs as follows.
- *Step 1 is a sequence argument.* Suppose good g_m → h with c(g_m)·q ≤ 0. Then a cluster c* of c(g_m)/|c(g_m)| has c*·q ≤ 0.
- *What "good" must mean.* Here "good" means: the CF chart holds at every q, and Lemma B1 holds (half-plane chart {c(g)·q > 0} on B₁). Both sets are co-null, so their intersection is co-null too.
- *Every cluster equals ĉ_k(h).* The cluster-line clause of Thm TS concerns every sequence in the Lemma B1 set. Its proof also applies to every sequence in the smaller set. I re-derived it locally:
  - the cluster line of c* must meet B₁, since otherwise P(·,h) would be one-signed on B₁, against A_τ ∩ B₁ ≠ ∅ ≠ B_τ ∩ B₁;
  - its trace on B₁ lies in Z_τ ∩ B₁ = λ_τ ∩ B₁;
  - an affine function on aff Δ determines its vector in ℝ³, and c* ∝ ±𝟙 is impossible, so c* = ĉ_k(h).
  
  Hence c*·q = ĉ_k(h)·q > 0, which is a contradiction. So r(q) > 0 exists. No continuity of c is used.
- *The step is global in q.* The convergence is a convergence of vectors, so it holds at every q ∈ Ω with c_k(h)·q > 0, not only on B₁. This is the genuinely new observation of I2:
  - in CF, silence is the cell {c ≤ 0, c′ ≤ 0};
  - so c(g)·q > 0 excludes silence at q.
- *Step 2: the case split.* c(g)·q > 0 gives q ∈ R(g), q ∈ R(−g) (when c′·q > c·q > 0) or q ∈ F(g). These are the only cells of max(0, c·q, c′·q) with c·q > 0. On F(g), the exact charts give P(q,±g) ≥ 0 by closure, since F(g) ⊆ cl R(g) ∩ cl R(−g). So K_q ⊆ g^⊥ there (R4 Thm B, re-derived).
- *Step 3.* Strict straddling, max_{K_q} m·g > 0 > min_{K_q} m·g, is open in g for fixed q, and good g are dense. Correct.
- *Step 4: incomplete case split.* It treats m₁·h > 0 and m₁·h = 0, but not m₁·h < 0, and the second case does not give strict straddling. With g = h + δ((m₁−m₀) − ((m₁−m₀)·m₀)𝟙) one gets m₀·g = 0 and m₁·g = δ|m₁−m₀|² > 0.
  - **Repair R1.** If m₁·h < 0, use g = h + δ𝟙. If m₁·h = 0, use g′ = g − δ′𝟙 with the g above and 0 < δ′ < δ|m₁−m₀|². Then m₀·g′ < 0 < m₁·g′, and g′ ∈ B(h,r) for small δ, δ′.

## 2. Theorem 2: positive state near e_b. CONFIRMED

- **(a)** For each τ ∈ J, Lemma 1 gives K_q ∩ h(τ)^⊥ = ∅, because K_q is non-singleton. K_q is connected, so it lies strictly on one side. The two sets of τ are open and disjoint, and they cover the interval J. Correct.
- **(b)** τ\* with h^a(τ\*)_b > 0 exists, since b crosses on F_a. The vertex sign c_a(h(τ\*))·e_b > 0 also follows directly:
  - P(·,h(τ\*)) > 0 near e_b, since K_q → {e_b};
  - N21.1′ gives A_τ ⊆ H⁺_τ;
  - a line through p\* and e_b would cut that vertex neighbourhood.
  
  V is the intersection of the two vertex neighbourhoods (one for F_a, one for F_c). It is shrunk so that the chords of both facets through every q ∈ V have parameters in (0,1). This is possible because the chords λ_τ with τ near τ_b sweep a neighbourhood of e_b, by strict monotone rotation (Thm pivot via Thm TS). It is uniform, as I2 §7.2 asks.
- *Equivalence and endpoint zero.* N21.1′ gives P ≤ 0 off J. P(q,h_∂) ≥ 0 by continuity in τ from inside J, which is nonempty since τ\* ∈ J. Both claims are correct.
- *Homogeneity.* "For every h ∈ relint F_a" follows from homogeneity of P(q,·) and linearity of c_k.

## 3. Theorem 3: the box returns as a precise collar. CONFIRMED

- *The certificate.* It is that of Prop T1 at (a,b) = (1,2) for x₊. A = (−β(1+η), η, 1) ∈ relint F_1 and B = (1, −ζ, −β(1−ζ)) ∈ relint F_3 both tend to the Σ-limits as s → 0, so (PC) applies to them.
  - Re-run in `i2ref_py/box_certificate.out`: both chart values are positive, the λ-interval is nonempty, and A and B lie in the relative interiors at s ≤ 10⁻³ for ε ∈ {.05, .3, .6, .9}.
  - At ε = .9 and s = 10⁻², B is not yet in relint F_3. This only confirms "for small s".
- *The superadditivity step.* At non-singleton q_n ∈ W ∩ V, Theorem 2(b) gives P(q_n,A), P(q_n,B) > 0, hence P(q_n, A+λB) > 0.
- *The edge-confinement step.* By Hausdorff compactness, every subsequence of K_{q_n} has a further subsequence converging to some K\* ⊆ Δ_{ab}. Then min_{K\*} m·(A+λB) ≤ max((A+λB)_a, (A+λB)_b) < 0. Correct.
- *Singletons are not touched.* At a singleton, P is linear, and the box only says m·A ≤ 0 or m·B ≤ 0. The new content is that Theorem 2 forces both positive at non-singletons.
- *Shape of the collar.* The radii r(q₀) may shrink as q₀ → e_b, so U_b may be a horn along the edge. U_b is connected (an increasing union of chains of overlapping half-discs). It is open in Ω and accumulates at e_b and along the edge segment.
- *Consistency.* C1's sector cap is precise next to the failing edge, as Theorem 3 requires.

## 4. Prop 4 and the repair of Prop D (brief priority 4)

### 4.1 What I2 uses, and the inherited gap

Prop 4(a) applies R4 Prop D to O = U_b. R8 (§"Proposition D (CHECKED): GAP") found that "(G)-signs exclude non-injective degenerate maps" is supported only by one example. Folds, plateaus and one-dimensional images are not excluded. Only the injective case is right, and it needs invariance of domain, which is written out in C1 Lemma 5.0. I2 does not mention this. As written, Prop 4(a) has a GAP.

### 4.2 Prop D* (PROVED here, one reader; replaces R4 Prop D)

**Prop D\*.** Let K solve CF (any target), and let O ⊆ Ω be open and connected with K_q = {σ(q)} on O. Then σ is constant on O, or σ is injective on every convex subset of O. Hence (R4 Prop D, injective case, as repaired in R8 / C1 Lemma 5.0, with the classical local FTPG) σ is constant or σ = ν(w⊙·) on O, w > 0.

*Proof.*

**(F1) Sign identity.** For a.e. g and **every** q ∈ O: sign(σ(q)·g) = sign(d_g·q), where d_g = c − c′ has the strict sign pattern of g.
- *Null zero set.* By Fubini on {(q,g) ∈ O×ℝ³ : σ(q)·g = 0}, whose q-sections are planes, Z_g = σ^{-1}(g^⊥) ∩ O is null for a.e. g.
- *Silence misses O, except on the d-line.* Silence {c ≤ 0, c′ ≤ 0} is closed and convex, and on O it lies in Z_g. If it has interior, O cannot meet it, since a closed convex body is the closure of its interior. If it has none and is nonempty, then c′ = −λc with λ > 0, and it equals the d-line.
- *Off silence, the cells give the identity.*
  - d·q > 0 forces c > max(0, c′), i.e. R(g), i.e. σ·g > 0;
  - d·q < 0 forces R(−g), i.e. σ·g < 0;
  - d·q = 0 forces c = c′ > 0, i.e. F(g), where neither strict acceptance holds, so σ·g = 0.

**(F2) Segments go to monotone line paths.** If s₁ < s₂ < s₃ lie on a segment in O, then σ(s₂) ∈ [σ(s₁), σ(s₃)].
- Otherwise an open set of g strictly separates σ(s₂) from that closed segment. A good such g makes the affine function d_g·s change sign twice along the segment, against (F1).
- Consequences:
  - σ maps segments into lines;
  - σ^{-1}(m) ∩ C is convex for convex C ⊆ O;
  - if σ(p₁) = σ(p₂) with [p₁,p₂] ⊆ O, then σ is constant on [p₁,p₂].

**(F3) No local one-dimensional image.** If D ⊆ O is an open disc and σ(D) ⊆ a line M, then σ is constant on D.
- *Setup.* Otherwise I = σ(D) is a nondegenerate interval. For y ∈ relint I and any mixed g with y ∈ g^⊥ ≠ M: g^⊥ ∩ σ(D) = {y}. So by (F1), L_g ∩ D = σ^{-1}(y) ∩ D, a nonempty chord.
- *All good g through y share one d-line.* That chord determines L_g.
- *Fubini.* The coordinates (y, direction) are a local diffeomorphism onto lines. So for a.e. y ∈ relint I, a.e. direction gives a good g.
- *The pencil at y meets at least two sign classes on arcs of positive length.*
  - y ∈ int Δ gives three classes;
  - y ∈ relint of an edge gives two classes;
  - y cannot be a vertex, since a vertex is an extreme point of Δ.
- *Contradiction.* The same d-line gives d_{g₁} ∝ d_{g₂}, hence the same class, because d has the strict sign of g. This is R8's suggested repair; it is C1 Prop 5.2 without C¹.

**(F4) Plateaus have no boundary in O.** Let P be a component of int σ^{-1}(m) and suppose p ∈ ∂P ∩ O. Take a ball B ⊆ O around p.
- *Setup.* By (F2), σ^{-1}(m) ∩ B is convex. Its interior Q is convex, open, nonempty, has p ∈ ∂Q, and contains σ^{-1}(m) ∩ B in its closure. Points of B outside cl Q therefore have σ ≠ m.
- *Rays from a ∈ Q.* Fix a ∈ Q. For directions θ near the direction of p − a, the exit point e(θ) of the ray from cl Q is continuous, with e(θ_p) = p. By (F2), the whole ray segment inside B maps into one line M_θ ∋ m.
- *θ ↦ M_θ is locally constant.* Take z beyond e(θ) on the ray. By (F2), conv(Q ∪ {z}) maps into M_θ, since every point lies on some [a′,z] with a′ ∈ Q. That set contains a disc around any w ∈ (e(θ), z), and the disc consists of points outside cl Q on rays θ′ near θ. So M_{θ′} = M_θ.
- *Contradiction.* For small r″, σ(B(p,r″)) ⊆ M. By (F3), σ is constant there, so p ∈ int σ^{-1}(m), contradicting p ∈ ∂P.
- *Conclusion.* A nonempty plateau is relatively clopen in the connected O, so σ is constant on O.

**(F5) Folds.** Suppose σ ≡ m on a segment S ⊆ O, with midpoint p₀, and σ is not constant on O.
- *No points of value m off S.* By (F4) there is no plateau. So no point near p₀ off S has σ = m: otherwise conv(S ∪ {z}) would lie in the fibre.
- *One line on each side.* For z₁, z₂ on the same side within δ ≪ |S| of p₀, the triangles conv(S ∪ {z_i}) overlap in an open set. If the lines line(m, σ(z_i)) differed, σ ≡ m there, which is a plateau. So each side has one line, M₊ and M₋.
- *The two lines agree.* A segment [z, z′] crossing S at s has σ(s) = m. By (F2), σ(z), m and σ(z′) are collinear, so M₊ = M₋.
- *Contradiction.* Then σ(B(p₀,δ)) ⊆ M₊, and (F3) and (F4) give a contradiction.
- *Conclusion.* Hence σ(p₁) ≠ σ(p₂) whenever [p₁,p₂] ⊆ O, i.e. σ is injective on convex subsets of O.

**Conclusion.** On each ball, the injective case gives σ = ν(w_B⊙·). Diagonal-projective maps that agree on an open set have proportional w, so one w works on the connected O. ∎

With D\*, Prop 4(a) holds:
- σ on U_b is constant or diagonal-projective;
- a constant value would be e_b, since K_q → {e_b} along U_b, and that is excluded by Prop vertexfree(i).

D\* also closes the R4/R8 gap in general. R4 Prop F and the "caps" picture regain their projective form, and C1's residual P_wild is empty.

### 4.3 Prop 4(b),(c): the global claim. CONFIRMED

- **(b)** By (F1) on U_b, d_g·q and (w⊙g)·q have the same sign on U_b. If their zero line meets U_b, then d_g ∝₊ w⊙g. Then R(g) = {c > 0, d > 0} ⊆ {σ_w(q)·g > 0} on all of Ω.
- **(c)** Let q′ be precise with K_{q′} = {σ′}, and let G_U be the open set of g with g^⊥ ∩ σ_w(U_b) ≠ ∅.
  - For good g ∈ G_U, σ′·g > 0 implies q′ ∈ R(g), hence σ_w(q′)·g > 0. By density this gives "σ′·g > 0 ⇒ σ_w(q′)·g ≥ 0" for every g ∈ G_U.
  - Fix m₀ ∈ σ_w(U_b) with m₀ ≠ σ′. Every g ⊥ m₀ lies in G_U. The restriction map m₀^⊥ → (𝟙^⊥)\* is an isomorphism, since m₀·𝟙 = 1, so the condition holds for every functional on 𝟙^⊥.
  - Hence σ_w(q′) − m₀ ∈ ℝ₊(σ′ − m₀), including 0.
  - Two m₀ not collinear with σ′ give σ_w(q′) = σ′; the value m₀ itself is excluded by non-collinearity.
  - Comparing collars at two vertices on an open set gives proportional weights.

This is the strong global claim of brief priority 4, and it is correct. It needs σ_w only on some open subset of one collar. I2 §7's remark that "the rest needs only σ C¹ with diagonal derivative at e_b" is inaccurate: (b) and (c) use the projective form on an open set.

## 5. Lemma 5 and transition points. CONFIRMED

- *Lemma 5.*
  - Joint continuity |P(q,g) − P(q′,g′)| ≤ ‖g−g′‖ + ‖g‖ d_H passes P(q_n, h_∂(q_n)) = 0 to the limit.
  - h_∂ is rational in q near e_b, because τ ↦ c_k(h(τ)) is affine by (PC).
  - The lines ℓ_{h^a_∂} and ℓ_{h^c_∂} pass through v_a and v_c near the crossings, so they are distinct.
  - Both chords through q pass through p\*, so Φ_b is constant along lines through p\*.
- *Existence of transition points (brief priority 5).* Take the arc of radius r < min(ρ_V, collar scale) from λ_b to the failing edge.
  - Its λ_b end is non-precise (Prop vertexfree(iii); the non-strict form suffices).
  - Points near its edge end lie in the half-discs of U_b.
  - The non-precise set is open, so the first precise point exists and is a limit of non-precise points.
  - This works at every small r, inside the closed sector.
  - At such points σ_w(q_r) = Φ_b(q_r), by Prop 4(c) and Lemma 5.

## 6. Theorem 6. CONFIRMED (recomputed)

- *Exact blow-ups at all three vertices.* `i2ref_py/blowup_exact.py` computes DG_b symbolically for b = 2, 3, 1, from the exact Φ_b (sympy) and σ_w, with x₁ = x₂ = x₃ = x. It does not use the cyclic symmetry.
  - At b = 2 it equals I2's diag(ω_a, ω_c) − v(1,−1), with v = κ/(1−κ²)(1/x − κx, κ/x − x) (difference 0).
  - At b = 3, 1 the formulas are the cyclic images.
- *Kernel and sector.* det DG = ω_aω_c + ω_a v₃ − ω_c v₁. The λ_b direction (1,1) and the edge direction (1,0) are not kernel vectors, since v₃ > 0 and ω > 0.
  - Kernel in the open sector ⟺ 0 < ω_a < v₁ and 1/ω_c = (v₁ − ω_a)/(v₃ω_a). I re-derived both kernel equations.
  - Uniformity of the O(r²) remainder holds because G_b is smooth on a full neighbourhood of e_b in aff Δ.
- *The Möbius cycle.* G has matrix [[−1, v₁],[v₃, 0]], with det −v₁v₃ < 0 and trace −1.
  - Its eigenvalues are real, of opposite sign and unequal modulus. So G³ ≠ id, and G³ fixes only G's fixed points.
  - With r₁r₂r₃ = 1, this forces r = 1 and v₁ − v₃ = 1.
  - Symbolically, v₁ − v₃ = κ(x²+1)/(x(κ+1)), which equals κ under x + 1/x = κ+1. So v₁ − v₃ = κ > 1.
- *The global step is load-bearing* (`solve_system.out`, `third_relation.out`, NUMERICS).
  - Each single relation (R_b) is solvable, with kernel in the open sector.
  - Any two are solvable, at a unique positive w.
  - The third then fails, with smallest singular value of DG_1 equal to 0.076, 0.50, 0.67, 0.71 at ε = .05, .3, .6, .9.
  
  So Prop 4(c)'s "same w at all three vertices" is essential. The contradiction weakens as ε → 0, as it should.
- *Reruns.* `i2py/transition.py` and `three_vertices.py` reproduce I2's output; the diff is identical (`three_vertices_rerun.out`). Those grids are NUMERICS only; the proof is algebraic.

## 7. Does the argument exclude genuine covers? (brief priority 7)

- **Steps 1–2** hold for every all-facing triangle in general position: they use (TS)/(PC) from Thm TSalways.
  - For half-plane covers they are tautologies. On R10a gauge mixtures, c(g) = f(g) and P(q,h) > 0 ⟺ F_q(h) > 0 ⟺ c(h)·q > 0, which is consistent with Lemma 1.
- **Step 3** needs a box certificate: PC data with c_a(A)·q₀ > 0 and c_c(B)·q₀ > 0, plus the ratio condition. That is exactly what Lemma edgebox forbids for half-plane charts.
  - So for gauge-mixture polygons, U-domain covers and every non-adjacent cover the certificate cannot exist, and Theorem 3 is vacuous.
  - Two-world targets have no such facets.
  - For T1 the certificate exists because the corner equation forces x = x₊ with x₊² > κ (Prop T1).
  - **This is the step that distinguishes T1.**
- **Step 6** is T1-specific algebra (v₁ − v₃ = κ ≠ 1). For a general all-facing triangle, Theorem 3 still yields a collar at every vertex with a failing box. The closing would then need either the analogue of Theorem 6 or C1's Theorem A, which is independent of Theorem 6.
- **Cross-check.** With D\*, Theorem 3 + Prop 4(a) + C1 Theorem A ("no injective precise open region in any CF(T1) solution") gives a second, independent closing from step 3 onward. I read it and found no error, but I did not referee it formally.

## 8. Exact statement established

**Theorem (I2, with repairs R1 and D\*).** Let ε ∈ (0,1) and p\* ∈ Ω. There is no strictly guiding additive ranking on a decomposable domain with (LF) at D_{T1} that satisfies (LA), (S), (C) and covers T1 with T1 as the p\*-Bayes model. Here the penalties are either:
- integral penalties with integrable envelopes; or
- bounded charges vanishing on null sets, given interior Bayes minimisers (via N14 Thm C2, which reduces them to the integral case).

Consequently, CF(T1) has no solution, at the status of CCIBU (Prop CF ⇐).

**Status.** PROVED from the inputs in §9. Two links are new and have one reader each:
- Prop D\* (this report);
- Lemmas 1–5 and Theorems 2, 3, 6 of I2 (first reading here).

**Intermediate result, independent of D\*** (PROVED from the inputs plus the injective case of Prop D, CHECKED). In every cover there is a precise open collar U_b at each vertex along its failing edge, and on no open subset of any collar is σ injective.

## 9. Dependencies and statuses

| Input | Used in | Status |
|---|---|---|
| Thm TSalways and Cor TSalways(a),(c): (TS), (PC), (NS), K_q → {e_b}, edge confinement | 1, 2, 3 | proved; one referee (N28_referee) |
| Thm TS, with the cluster-line clause for every good sequence near Σ | 1 | proved; one referee (N23 §4) |
| Lemma B1 (half-plane charts on B₁) | 1 | proved; one referee (N23 §3) |
| Lemma quasiconcave / N21.1′ | 2 | proved; one referee (N23 §2) |
| Prop vertexfree (i), (iii) (non-strict forms suffice) | 4a, 5 | proved; one referee |
| Prop T1 (corner equation, box certificate), Prop boxbridge (a),(b) on general domains | 3, 6 | proved; refereed (N14, R15/R18; assembly N23 §6) |
| Prop necessary, Prop reduction(b): Hausdorff continuity, joint continuity of P | all | proved; refereed |
| Prop CF (⇒): exact cell-decomposition charts at every q for a.e. g | 1, D\* | CHECKED; confirmed with repair, one referee |
| R4 Thm B (K_q ⊆ g^⊥ on cl F(g)) | 1 (re-derived) | proved; R8 CORRECT |
| **Prop D\*** (replaces R4 Prop D) | 4a | PROVED here; one reader |
| R4 Prop D, injective case (invariance of domain; local FTPG; diagonal step) | 4a | CHECKED (R8 repair; C1 Lemma 5.0) |
| Local fundamental theorem of projective geometry | 4a | classical |
| Reduction to p\* = u (world-wise rescaling of penalties; Prop diag(a)) | 6 | proved; one referee |
| N14 Thm C2 | charge clause | proved in a referee report; one reader; existence proviso |
| Thm CCIBU (Prop CF ⇐) | CF(T1) form only | author-checked |

## 10. Requested edits to I2

1. Lemma 1 step 4: add the case m₁·h < 0, and replace the m₁·h = 0 gamble by g − δ′𝟙 (R1).
2. Prop 4(a): replace "R4 Prop D, CHECKED" with Prop D\* (or a citation of this report). Record R8's GAP.
3. §0 and §7: correct the status line and the dependency list (§9). Remove "the rest needs only σ C¹ with diagonal derivative at e_b".
4. Theorem 2(b): state explicitly that V is shrunk so that both chord parameters through each q ∈ V lie in (0,1).
5. Theorem 3: note that U_b may be a horn (radii → 0 at e_b). Nothing downstream needs a sector.
6. §6, NUMERICS: add that any two of the three relations (R_b) are solvable, so the global w of Prop 4(c) is essential.

## 11. Scripts (`i2ref_py/`)

| File | Content | Result |
|---|---|---|
| `three_vertices_rerun.out` | rerun of `i2py/three_vertices.py` | identical to I2 |
| `blowup_exact.py/.out` | exact symbolic DG_b at b = 1, 2, 3 from the exact Φ_b, without cyclic symmetry | matches I2 at b = 2 (difference 0); v₁ − v₃ = κ(x²+1)/(x(κ+1)), equal to κ under the corner equation |
| `solve_system.py/.out` | each (R_b) alone; pairs of relations | single relations are solvable with kernel in the open sector; (R_2) and (R_3) have a unique positive solution |
| `third_relation.py/.out` | (R_1) at that solution | fails at every ε tested; v₁ − v₃ = κ exactly |
| `box_certificate.py/.out` | Prop T1 certificate as the input of Theorem 3 | valid for s ≤ 10⁻³ at ε ∈ {.05, .3, .6, .9} |

All numerics are sanity checks. The verdicts rest on the hand derivations above.
