# E61 — Escaper notes: can the reversed triangle be covered? (25 Oct 2026)

Labels: PROVED (proof here, not refereed) / CHECKED (verified by hand or by exact LP/symbolic computation) / CONJECTURE / NUMERICS. Scripts in this folder: `e61_checks.py` (+ `.out`), `e61_hull.py` (+ `.out`), `e61_chart.py` (+ `.out`).

## 0. Verdict

**No cover was found.** Every escape route listed in the brief fails, and each failure is a proved lemma. The routes are: incomplete world orders, infinitely many statistics, non-integral levels, vetoes the target pays, other one-sided domains, and two-sided domains.

All the failures go through one mechanism, the **collar trade**:
- Add three small sets of gambles lying just outside the target, beyond the midpoints of its three faces.
- Their summed payoff is positive at every world, so Brier error improves at every world.
- To protect the target, some world must object to this trade at a level above Brier.

The proved results below show which objections are impossible, and what any surviving objection must look like.

Main results:

1. **Pointwise-best lemma and box lemma (PROVED, any target, any n).** These need only (G) and transitivity at one world.
   - Suppose a world has a *priority region*: a set R of wrong-at-j gambles such that accepting any non-null part of R is worse than the worst model that avoids R.
   - Then for every other world i, the model "accept exactly the i-positive gambles outside R" is undominated, so it must be coherent.
2. **No inclusion vetoes (PROVED, any target).**
   - Suppose a world refuses every change that adds a gamble of R, ordering such acceptances by set inclusion rather than by measure.
   - Then R consists of non-positive gambles, up to a null set.
   - So the most natural incomplete orders are dead for every target.
3. **Collar lemma (PROVED, reversed triangle, any one-sided domain with (LF)).** A priority region that the target does not pay never meets a fixed open collar just beyond the relative interiors of the three faces. This holds for every world, whatever its shape: non-convex, measured or not, depth-graded.
4. **Broad impossibility (PROVED).** Take any one-sided domain with (LF), and any ranking in which every world is the unanimity of *any family* of views. Allow incompleteness and infinitely many views. Each view has:
   - first, any number of integral vetoes that the target does not pay (non-convex allowed);
   - then finitely many purely finitely additive (non-integral) levels in total;
   - then a Brier level.

   No such ranking covers the reversed triangle: either some undominated model is incoherent, or the collar trade strictly dominates the target. (A short check gives the same conclusion on two-sided domains: CHECKED.)
5. **Reduction (PROVED).** Allow finitely many views per world, vetoes that the target pays, and any sign-correct second levels. A cover then *forces* a chart realisation of D_K on a one-sided domain N ⊇ D_K ∪ collar with (LF): weakly sign-correct charts all of whose a.e.-unique Bayes acts are coherent. This is the CPM realisation problem, which the brief excludes.
   - With concave charts it is impossible. That case covers every VB-type design: convex vetoes (paid by the target or not), Brier or concave secondaries, and any finite incompleteness.
   - The most natural non-concave chart (the lower-prevision chart) fails: at the prior (1,2,3) it has an explicit incoherent undominated Bayes act (CHECKED).
6. **Nearest reachable result (PROVED).**
   - Every full-dimensional K ⊆ relint Δ, the reversed triangle included, is a Hausdorff limit of polytopes K_s ⊆ K that the auditor's theorem covers exactly, each with (LF) on its own domain U_s.
   - The rate is d_H(K_s, K) ≤ (1−s)·max|k−u|.
   - On a *fixed* domain the auditor class stays a positive distance from K, linear in the (LF) margin (CHECKED).
   - Exact coverage needs a non-concave chart, which is open and is CPM-type.

Existing positive results checked (§2): normalised boxes, parallel bodies, gauge mixtures, and the auditor/VB class with any compatible one-sided domain. **None covers the reversed triangle exactly.**

---

## 1. Geometry of the target (CHECKED, `e61_checks.out` §1)

- K = {m ∈ Δ_3 : m_i ≤ 2/5}, with vertices v_1 = (1,2,2)/5, v_2 = (2,1,2)/5, v_3 = (2,2,1)/5.
- D_K = {h : v_i·h > 0 for i = 1,2,3}. This is the open simplicial cone on the rays r_j := 2·𝟙 − 5e_j, so r_1 = (−3,2,2) and so on, with v_i·r_j = δ_ij.
  - r_j is the gamble "lose 3 at j, win 2 elsewhere". It is marginally acceptable because the upper probability of {j} is 2/5.
  - Each ray has exactly one negative coordinate. T1's rays have exactly one positive coordinate, so the two cones are dual in this sense.
- Face F_{v_k} := cl D_K ∩ {v_k·h = 0} = cone(r_i, r_j) for {i,j,k} = {1,2,3}.
  - h_k > 0 on the whole face, so the face is anti-visible from k.
  - Both h_i and h_j change sign in its relative interior, so the face is crossing for i and j.
  - Hence no face can be vetoed by a single world.
- Face midpoints: m_k := r_i + r_j, so m_1 = (4,−1,−1) and so on. Each is correct at one world and wrong at two. Their sum is m_1 + m_2 + m_3 = (2,2,2).

**Collar trade.** Let P = P_1 ∪ P_2 ∪ P_3, where P_k is a small set of gambles just beyond F_{v_k} near m_k, with equal Gaussian masses. Then ∫_P h ∈ int ℝ³₊.
- NUMERICS: with U = D_{K'}, K' = u + ½(K−u), sampled pieces lie outside D_K and inside U.
- ∫_P h = (0.7, 10.8, 4.5) > 0 (`e61_checks.out` §2).

So **D_K ∪ P has strictly lower Brier error than D_K at every world.**

---

## 2. Existing project results: none covers K exactly

| Result | Covers K? | Reason |
|---|---|---|
| Normalised boxes ν(p⊙∏[α_i,β_i]) | No (PROVED) | Their edges lie on lines m_i/m_j = c, which pass through a vertex e_k of Δ. The edges m_i = 2/5 of K pass through no vertex of Δ. |
| Parallel bodies (1−t)L + tq₀ + taB (v19, CPM) | No exactly (PROVED); yes approximately | A Minkowski sum with a disc has C¹ boundary, so it never has corners. The parallel bodies of L = K converge to K, but only through CPM realisation. |
| Gauge mixtures ν(Σp_iM_i) / concave charts | No (PROVED) | R10a Thm R excludes triangles in general position. K is in general position: the lines through two of its vertices are m_i = 2/5, which contain no e_k. Re-derived here as Cor 5.2. |
| Auditor theorem / VB, U = D_{K'} | No (AUDIT §4) | No vertex is visible. |
| VB-type on any compatible one-sided domain U = ∪_i D_{V_i} | No (PROVED, §4.5) | See the zonotope lemma, §4.5. |
| Auditor class, approximately | Yes (PROVED, §6) | K_s → K, with shrinking domain margin. |

---

## 3. General tools

Notation:
- Models are measurable X ⊆ U, modulo null sets, where U is one-sided and contains D_K together with an open neighbourhood of ∂D_K∖0. This is what (LF) gives.
- The ranking orders are written ⪯_j.
- "Y is pointwise at least as good at j as X" means: at a.e. h, Y's advice has rank at world j no worse than X's.

(G) is used in two forms:
- weak: pointwise at least as good implies ⪯_j;
- strict: if in addition the two differ on a non-null set, then ≺_j. For h_j ≠ 0, distinct advices have distinct ranks.

**Lemma 3.1 (pointwise-best lemma; PROVED; any domain, any n).** Let i ≠ j. Assume strict (G) at i and transitivity at j. Let M be a model and S := {Y : Y ⪯_j M}. If X* ∈ S is pointwise at least as good at i as every member of S, then X* is undominated.

In every application below, X* is pointwise at least as good at j as M. So only the weak form (TP) of transitivity is used: if Y ⪯_j X and X is pointwise at least as good at j as M, then Y ⪯_j M.

*Proof.*
- Let Y weakly dominate X*. Then Y ⪯_j X* ⪯_j M, so Y ∈ S.
- So X* is pointwise at least as good at i as Y.
- If Y ≠ X* a.e., then X* ≺_i Y, which contradicts Y ⪯_i X*.
- So Y = X* a.e., and nothing dominates X*. ∎

(IB) and completeness are not used.

**Definition.** R ⊆ U ∩ {h_j < 0} is a **priority region at j** if no Y with μ(Y∩R) > 0 has Y ⪯_j M_R, where M_R := (U∖R) ∩ {h_j < 0} is the worst model that avoids R. Examples, all PROVED from the definitions:
- {φ > 0} for a leading non-negative integral veto φ, including in a single view of a unanimity order;
- the union of the zero-complements of any number of leading target-neutral vetoes;
- the veto region of an inclusion veto, of a Pareto-veto, or of a depth-leximax veto.

**Corollary 3.2 (box lemma; PROVED).** If R is a priority region at j, then for every i ≠ j the model X_i := (U∖R) ∩ {h_i > 0} is undominated. Under the success criterion it is therefore coherent: a.e. equal to a convex cone.

*Proof.*
- Every Y ⊆ U∖R is pointwise at least as good at j as M_R, so Y ⪯_j M_R by weak (G).
- By the priority property, S = {Y ⪯_j M_R} = {Y ⊆ U∖R a.e.}.
- X_i ∈ S and is pointwise i-best in S. Apply Lemma 3.1. ∎

**Corollary 3.3 (no inclusion vetoes; PROVED; any target, any n).** Say world j *inclusion-vetoes* R ⊆ U ∩ {h_j < 0} if Y ⪯_j X implies Y∩R ⊆ X∩R a.e. Under the success criterion, R ⊆ {h ≤ 0} a.e.

*Proof.*
- For E ⊆ R, put M_E := E ∪ M_R. Then S_E := {Y ⪯_j M_E} = {Y : Y∩R ⊆ E}:
  - "⊆" is the inclusion veto;
  - "⊇" is weak (G), since such a Y is pointwise at least as good at j as M_E.
- Its pointwise i-best member is X_E := (U∖R ∪ E) ∩ {h_i > 0}. By Lemma 3.1 it is undominated, so coherent, for every E.
- Suppose μ(R ∩ {h_i > 0}) > 0 for some i ≠ j. Pick a Lebesgue density point p of R ∩ {h_i>0} inside the open set C := U∩{h_i>0}, a small ball B ∋ p with B ⊂ C, and put E := R∖B.
- Then X_E = C∖(R∩B) a.e. Any convex cone Q equal to it a.e. contains a full-measure part of the annulus around B, hence contains B, hence contains the non-null set R∩B. This is a contradiction.
- So R ∩ {h_i > 0} is null for every i ≠ j. Since R ⊆ {h_j < 0}, this gives R ⊆ {h ≤ 0}. ∎

**Lemma 3.4 (collar lemma; PROVED; reversed triangle, any one-sided U with (LF)).** There are positive functions δ_k on relint F_{v_k}, continuous on compact subsets, such that the open collar

  C := ∪_k {p − δ v_k : p ∈ relint F_{v_k}, 0 < δ < δ_k(p)} ⊆ U ∖ cl D_K

has the following property: **every priority region R at any world j with μ(R ∩ D_K) = 0 satisfies μ(R ∩ C) = 0.**

*Proof.*
- **Face F_{v_j}.** h_j > 0 on the whole closed face minus 0, so a collar beyond it lies in {h_j > 0}, which is disjoint from R.
- **Face F_{v_i}, i ≠ j.** By Cor 3.2, X_i = (U∖R) ∩ {h_i>0} is a.e. a convex cone Q.
  - Q contains a.e. both open sets D_K∩{h_i>0} (because R misses D_K) and U∩{h_i>0, h_j>0}.
  - So Q contains their convex hull H. A convex set containing almost all of an open set contains the open set.
- **Points with p_j > 0.** Take p ∈ relint F_{v_i}. If p_j > 0, then p − δv_i ∈ U∩{h_i>0,h_j>0} for small δ.
- **Points with p_j ≤ 0.**
  - Fix b ∈ relint F_{v_i} with b_j > 0. The face crosses h_j = 0, so such b exists.
  - Put B := b − ηv_i ∈ U∩{h_i>0,h_j>0}, using (LF).
  - For t = 2δ/η, the point A := (p − δv_i − tB)/(1−t) satisfies v_i·A > 0. For small δ it also satisfies v_k·A ≈ v_k·p > 0 (k ≠ i) and A_i > 0.
  - So A ∈ D_K∩{h_i>0}, and p − δv_i = (1−t)A + tB ∈ H.
- Hence R misses the collar beyond F_{v_i} a.e. ∎

CHECKED: an exact conic-hull LP accepts all 77 of 90 sampled collar points at small depth. The 13 rejections lie at depth ≥ 0.01 near the end ray r_2, where the collar thins (`e61_hull.out`). This is consistent with δ_k(p) → 0 at the rays.

**Lemma 3.5 (minimiser converse; PROVED).** Let every world be the unanimity of finitely many lexicographic views v, each with levels (a_v, c_v, …). Fix W ⊆ views, and let N_W := models with a_v = 0 for all v ∈ W. Take weights β_v ≥ 0 on c_v (v ∈ W) and α_v ≥ 0 on a_v (v ∉ W). Every a.e.-unique minimiser over N_W of J = Σ_W β_v c_v + Σ_{∉W} α_v a_v is undominated.

*Proof.*
- A weak dominator Y has, for v ∈ W, a_v(Y) = 0 and c_v(Y) ≤ c_v(X*) by the lexicographic order. For v ∉ W it has a_v(Y) ≤ a_v(X*).
- So J(Y) ≤ J(X*), and uniqueness gives Y = X*. ∎

**Lemma 3.6 (avoiding finitely additive levels; PROVED, using Yosida–Hewitt).**
- Let ν_1, …, ν_r be bounded, purely finitely additive, μ-continuous set functions. Then for every ε > 0 there is E with μ(E) < ε and |ν_s|(U∖E) = 0 for all s. This is Yosida–Hewitt's characterisation; take the union of the r sets.
- The collar pieces P_k can be shrunk off E while keeping ∫_P h ∈ int ℝ³₊, by uniform integrability of |h|.
- So **finitely many non-integral (purely finitely additive) levels are blind to some collar trade.**

---

## 4. The escape routes

### 4.1 Incomplete world orders
- (a) **Inclusion-type incompleteness**, refusing any trade that adds a vetoed gamble: dead for every target (Cor 3.3).
- (b) **Unanimity of views**, i.e. Pareto between statistics or several "opinions" per world. Each view's leading veto is a priority region (Cor 3.2 applies view by view). Cor 5.3 then kills Brier-type views whose vetoes the target does not pay.
- (c) **Incompleteness does help in one respect (PROVED by example).**
  - Under lexicographic *complete* orders, a veto that the target pays lets a removal strictly dominate the target (S3; cf. VB note).
  - Under unanimity with a Brier view at every world, a *pure removal* A ⊆ D_K must also pass every Brier view, i.e. ∫_A h_j ≤ 0 for all j. That is impossible, since p·∫_A h > 0 for p ∈ K.
    - Example: pieces near r_j with masses x_j need 3x_j ≥ 2Σ_{k≠j}x_k for every j. Summing gives 3Σx ≥ 4Σx, so x = 0.
  - So S3's removal mechanism needs completeness, and target-paid vetoes become admissible in principle. This is the one genuine gap in S3 outside the complete class.
  - Removal combined with collar additions is still available. Thm 5.1 shows that this whole branch leads only to CPM-type charts.

### 4.2 Infinitely many statistics
Lemmas 3.1–3.5 and the collar trade use no Lyapunov argument. Cor 5.3 allows:
- infinitely many views;
- countably many veto levels per view, since the first positive level decides the lexicographic comparison;
- copies of Brier.

Only Thm 5.1(c) uses separation, which is why it is stated for finitely many views.

### 4.3 Non-integral (IB) levels
- **Depth-leximax or "worst violation first" vetoes** are priority regions, so Lemma 3.4 applies.
- **Ultrafilter, germ or Banach-limit levels** are purely finitely additive. If finitely many, they are blind to some collar trade (Lemma 3.6).
- **Complete, transitive, homogeneous (IB) orders on finitely many statistics** are lexicographic (Hausner–Wendel, brief S6), so they fall back into §5.
- Orders not generated by any family of views remain outside these results (§7).

### 4.4 Vetoes the target pays
- Complete lexicographic case: excluded by S3. Under unanimity (§4.1c) they survive, and Thm 5.1 covers them.
- Refinement (PROVED): suppose a target-paid priority veto at world j must cover the collar arbitrarily close to the point where a face F_{v_i} crosses h_j = 0. Then the convexity of X_i forces its trace on {h_i>0} to be the *full* veto U∩{h_i>0, h_j<0}.
  - Reason: the supporting halfspace of the convex set (U∖R)∩{h_i>0} ⊇ U∩{h_i>0,h_j≥0} at that point must be {h_j ≥ 0}.

### 4.5 Other one-sided domains
(LF) forces C ⊆ U, so the collar trade is always available. The world-i-best model U∩{h_i>0} is undominated by (G), hence U∩{h_i>0} = D_{V_i} is convex. For such compatible tuples, a convex veto at world i has the form max(0, sup_{a∈A}(−a·h)) with A ⊆ V_i.

**Zonotope lemma (PROVED).** The normal set {β + Σ_{j∈M} α_j a_j : M ⊆ worlds, a_j ∈ A_j ⊆ cone(V_j)} never has K as its normalised hull.
- Put f_i(x) := (2/5)Σx − x_i. Then f_i > 0 on V_j for j ≠ i.
  - Reason: D_{V_j} contains the collar beyond the faces where h_j > 0 near the rays r_i, and m·r_i > 0 means m_i < 2/5.
- So a normal with f_1 = 0, the minimum, must have M ⊆ {1}. It then has f_2 = f_2(β) + α_1 f_2(a_1) > 0.
- Hence no normal is proportional to v_3 = {f_1 = f_2 = 0}, and K's vertices are never attained.
- CHECKED for V_j = conv(K'∪e_j): min f_i = 0.033 > 0 (`e61_checks.out` §6).

### 4.6 Two-sided domains
- Lemma 3.1 holds verbatim. (LF) supplies "accept h" near ∂D_K, so the collar trade exists.
- A priority region of j-wrong advice gives a box model X_i: give the i-correct advice wherever available, except the j-wrong advice in R. Its accepted cone contains the same two open sets as in Lemma 3.4.
- So Lemma 3.4 and Cor 5.3 extend, with two-sided Brier (CHECKED, same proof).
- Nothing new protects the collar. Combined with F61's observation that convex vetoes collapse on two-sided domains, two-sided domains are harder, not easier.

---

## 5. Main impossibility and the reduction to charts

**Corollary 5.3 (broad impossibility; PROVED).** The domain is any one-sided decomposable U with (LF) at D_K, K the reversed triangle. Every world is the unanimity of any family of views. Each view has:
- first, any number (countably many) of pure integral vetoes, each vanishing on D_K, of any shape;
- then any levels drawn from a fixed finite set of purely finitely additive statistics, each weakly guiding at j as (G) requires;
- then a Brier level −κ_v∫_X h_j with κ_v > 0;
- then anything.

If every undominated model is coherent, then D_K is strictly dominated. So no such ranking covers K.

*Proof.*
- The union of a view's leading vetoes is a priority region that the target does not pay. By Lemma 3.4 it misses C.
- By Lemma 3.6, choose P ⊆ C off the finitely-additive concentration set, with ∫_P h ∈ int ℝ³₊.
- At every view of every world, D_K ∪ P ties D_K on every veto and on every finitely additive level, and is strictly better at the Brier level.
- So D_K ∪ P ≺_j D_K at every j. ∎

This contains S2, the brief's collar obstruction, and extends it to:
- incomplete orders;
- infinitely many statistics;
- non-convex vetoes;
- non-integral levels;
- every one-sided (LF) domain.

**Theorem 5.1 (reduction to a chart realisation; PROVED).** Same domain. Every world j is the unanimity of a *finite* set 𝒱_j of views. Each view has:
- a first level a_v = ∫φ_v, with φ_v ≥ 0 vanishing on {h_j > 0}; the target may pay it;
- a second level c_v = ∫σ_v, sign-correct at j: σ_v ≤ 0 where h_j > 0 and σ_v ≥ 0 where h_j < 0;
- any further levels.

Suppose D_K is undominated and every undominated model is coherent. Let W_0 := {v : a_v(D_K) = 0} and N := U ∖ ∪_{v∈W_0}{φ_v > 0}. Then there are weights β_v ≥ 0 (v ∈ W_0, not all zero) and α_v ≥ 0 (v ∉ W_0) such that the charts

  σ̂_j := Σ_{v∈𝒱_j∩W_0} β_v σ_v + Σ_{v∈𝒱_j∖W_0} α_v φ_v

satisfy:
- (a) each σ̂_j is weakly sign-correct at j;
- (b) N ⊇ D_K ∪ C, so N is a one-sided decomposable domain with (LF) along the relative interiors of the faces;
- (c) D_K is a Bayes act of Σ_jσ̂_j on N, that is N∩{Σσ̂_j < 0} ⊆ D_K ⊆ {Σσ̂_j ≤ 0} a.e.;
- (d) for every t ∈ ℝ³₊∖0 with {Σ t_jσ̂_j = 0}∩N null, the Bayes act N∩{Σ_j t_jσ̂_j < 0} is coherent.

That is, **a cover forces a CPM-type realisation of D_K on N.** It is CPM-type up to strictness of the charts.

*Proof.*
- **(b)** Each {φ_v>0} with v ∈ W_0 is a priority region that the target does not pay. Apply Lemma 3.4.
- **(c), setting up.** Use the views as pseudo-worlds.
  - World dominance and pseudo-world dominance coincide: "strict at j" means strict at some view of j.
  - The score range is convex and compact, by Lyapunov's theorem for finitely many integrals.
  - Every a_v ≥ 0, and the empty model zeroes every a_v.
- **(c), separation.** LDG Prop. lexbayes then applies; its disjointness argument uses only the first two levels. It gives β (non-zero, on W_0) and α (off W_0) such that D_K minimises J = ∫_X Σ_jσ̂_j over X ⊆ N.
- **(d)** The t-Bayes act minimises Σ_j t_j(…) uniquely. By Lemma 3.5 it is undominated, hence coherent. ∎

Conversely (CHECKED, standard), strictly sign-correct charts on such an N whose t-Bayes acts are a.e. unique and coherent for every t ∈ Δ give an additive ranking covering D_K. The two parts are Lyapunov with Zorn (Lemma zorn), and separation with uniqueness. So, **within finite-view rankings, covering the reversed triangle is equivalent, up to strictness and tie conditions, to the CPM realisation problem on a neighbourhood domain.**

**Corollary 5.2 (concave charts are impossible; PROVED).** In Thm 5.1, suppose each −σ_v is concave and strictly sign-correct, and each φ_v is convex, on an open convex set containing cl D_K∖0. This holds for VB-type designs: convex positively homogeneous vetoes paid by the target or not, Brier or concave secondaries, any finite incompleteness. Then K is not covered.

*Proof.*
- **Zero on the faces.** Put c_j := −σ̂_j. It is concave, hence continuous, on that open convex set. By (b) and (c), g := Σσ̂_j satisfies g ≥ 0 a.e. on C and g ≤ 0 a.e. on D_K, so g = 0 on the relative interiors of the faces.
- **Linear on the faces.** On each face, c_j is a concave summand of a function that is zero there, so c_j is affine there. Sign-correctness on a crossing face then forces c_j = κ_j^F h_j on F.
  - At the shared ray r_j, (r_j)_j = −3 forces the same κ_j on both crossing faces of world j.
  - On the anti-visible face F_{v_k}, c_k = −Σ_{others}.
- **The ray equations.** The six ray equations are 2κ_1 = 3κ_2 − 2κ_3 = 3κ_3 − 2κ_2, together with their cyclic versions. Their only solution is κ = 0 (CHECKED symbolically, `e61_checks.out` §5).
- **All charts vanish on D_K.**
  - So every c_j vanishes on ∂D_K. Hence c_j ≥ 0 on D_K by concavity. Each x ∈ D_K lies on a bounded chord with both ends on ∂D_K∖0: use a direction w with ±w ∉ cl D_K.
  - Sign-correctness gives c_j ≤ 0, hence c_j = 0, on the open set D_K∩{h_j<0}. A concave function vanishing on an open subset of the convex set D_K is ≤ 0 on D_K. So c_j = 0 on D_K.
- **Contradiction.** Some β_v > 0 multiplies a strictly sign-correct σ_v, and φ_v = 0 where h_j > 0. So c_j > 0 on D_K∩{h_j>0}. Contradiction. ∎

This is R10a Thm R and brief S5, re-derived and extended to incomplete orders and to vetoes paid by the target.

**A natural non-concave chart fails (CHECKED, NUMERICS, `e61_chart.out`).**
- The chart is c_j(h) := v_{k(h),j}·h_j, with k(h) := argmax_l h_l = argmin_l v_l·h. It is strictly sign-correct and discontinuous, and Σ_jc_j = min_k v_k·h, so the 𝟙-Bayes act is exactly D_K.
- But at t = (1,2,3) its Bayes act is not convex. The points x = (1.001, 1, −0.75) and y = (1, 1.3, −0.75) are accepted, while (1, 1.001, −0.75) and most of the segment [x,y] are rejected.
- The cause is that acceptance jumps across the plane h_1 = h_2 inside D_K.
- That Bayes act is a.e. unique, so it would be an incoherent undominated model. Whether *some* non-concave chart works is the open CPM question.

---

## 6. Nearest reachable results

**Proposition 6.1 (dense exact coverage; PROVED; any n, any full-dimensional compact convex K ⊆ relint Δ).** Fix u_0 ∈ relint K and s ∈ (0,1). Put K'_s := u_0 + s(K − u_0), A_i := conv(K'_s ∪ e_i) ∩ K, and K_s := conv(K'_s ∪ A_1 ∪ … ∪ A_n). Then:
- K'_s ⊆ relint K_s ⊆ K_s ⊆ K;
- d_H(K_s, K) ≤ (1−s)·max_{k∈K}|k − u_0|;
- the auditor's two-level veto–Brier ranking covers D_{K_s} exactly on U_s = D_{K'_s}, with (LF), (G), (IB), (C) and the dominance conclusion.

*Proof.*
- The inclusions in K and the bound on d_H are immediate.
- **Interior.** Suppose x ∈ K'_s lay on a supporting line ℓ(m) = c·m of K_s, with c not constant. Since x ∈ relint Δ, c·x < max_i c_i =: c_{i*}.
  - Because x ∈ relint K, points (1−t)x + te_{i*} with small t lie in A_{i*} ⊆ K_s.
  - These points have larger ℓ, which is a contradiction.
- The hypotheses of the auditor's theorem now hold. ∎

Status note: the coverage claim inherits the status of the auditor's theorem (AUDIT_VB_general §2), which has not yet been refereed. The geometric part is PROVED here.

NUMERICS for the reversed triangle with u_0 = u: d_H(K_s, K) = 0.0645, 0.0266, 0.0135, 0.0068, 0.0014 at s = 0.5, 0.8, 0.9, 0.95, 0.99. The interior condition is verified by LP at each s (`e61_checks.out` §7). The K_s are hexagons: the reversed triangle with its three corners cut.

**Proposition 6.2 (no uniform version inside the auditor class; CHECKED).**
- Fix U = D_{K'} and put M := max_{k∈K', l} k_l < 2/5.
- Every auditor target K'' with d_H(K'', K) ≤ δ has m_1 + m_2 ≤ max(2M, 2/5 + M + O(δ)) on K''. Points of conv(K'∪e_i) have coordinates l ≠ i at most M.
- So d(v_3, K'') ≥ c·(2/5 − M) − O(δ). The trade-off between (LF) margin and accuracy is therefore linear and unavoidable in this class.

**What exact coverage would need.** By Thm 5.1, exact coverage needs a sign-correct, non-concave chart family on a neighbourhood N of cl D_K∖0 whose Bayes acts are all coherent. This is CPM-type, so the brief excludes it.

---

## 7. Which axiom an escape must give up

To cover the reversed triangle, some world must object to the collar trade P above its Brier level, for every collar P. By §§3–5, that objection cannot come from:
- a target-neutral priority region (Lemma 3.4), whether measured, by inclusion, by depth, Pareto, or in a single view;
- an inclusion veto anywhere (Cor 3.3);
- finitely many finitely additive levels (Lemma 3.6);
- a Brier level (the trade improves Brier everywhere);
- a concave chart (Cor 5.2).

What remains:
- **(i)** A genuinely h-dependent, non-concave sign-correct trade-off at the collar, with all Bayes acts coherent. For finite-view integral rankings this is *exactly* the CPM realisation problem (Thm 5.1 and its converse), which the brief excludes.
- **(ii)** World orders not generated by any family of lexicographic views. Examples are non-measurable translation-invariant orders, or incomplete orders whose improving set is not an intersection of half-spaces and lexicographic boundaries. No construction of this kind is known to me, and none is excluded. CONJECTURE: none satisfies (G), (IB), transitivity and the success criterion.
- **(iii)** Weakening transitivity below (TP), the only form used (Lemma 3.1). The brief's "(TC)" is not defined in this folder. If (TC) does not imply (TP), the box lemma must be re-checked.
- **(iv)** Weakening (LF) near the face midpoints. That removes the collar, and is the cheapness the project excludes.

---

## 8. Status table

| Item | Status |
|---|---|
| Geometry: rays 2𝟙−5e_j, every face anti-visible from one world and crossing for two | CHECKED |
| Collar trade: ∫_P h ∈ int ℝ³₊ for pieces beyond face midpoints | PROVED; NUMERICS |
| Normalised boxes, parallel bodies, gauge mixtures, auditor/VB: no exact cover | PROVED (Thm R cited for gauges) |
| Lemma 3.1 pointwise-best lemma (needs only strict (G) at i, (TP) at j) | PROVED |
| Cor 3.2 box lemma | PROVED |
| Cor 3.3 inclusion vetoes impossible for every target | PROVED |
| Lemma 3.4 collar lemma (any one-sided U with (LF)) | PROVED; hull CHECKED by LP |
| Lemma 3.5 minimiser converse for finite-view rankings | PROVED |
| Lemma 3.6 finitely additive levels blind to some collar trade | PROVED (Yosida–Hewitt cited) |
| §4.1(c) unanimity blocks S3's removal argument | PROVED (example) |
| §4.4 target-paid priority vetoes near crossing points must be full | PROVED |
| §4.5 zonotope lemma for compatible one-sided domains | PROVED; CHECKED |
| §4.6 extension of Lemma 3.4 and Cor 5.3 to two-sided domains | CHECKED (same proof) |
| **Cor 5.3: no cover by view-unanimity rankings with target-neutral vetoes, finitely additive levels, Brier** | **PROVED** |
| **Thm 5.1: finite-view rankings — cover ⇒ CPM-type chart realisation on N ⊇ D_K ∪ C** | **PROVED**; converse CHECKED |
| Cor 5.2: concave charts (all VB-type, incomplete, target-paid) impossible | PROVED; κ-system CHECKED |
| Lower-prevision chart fails at t = (1,2,3) | CHECKED; NUMERICS |
| Prop 6.1 dense exact coverage by the auditor class | PROVED; NUMERICS |
| Prop 6.2 no uniform-margin version inside the auditor class | CHECKED |
| Existence of a cover by orders not generated by views | open; CONJECTURE: none |
| Non-concave CPM chart for the reversed triangle | open (excluded by brief) |
