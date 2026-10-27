# R10a: constructive attempt on the single-target additive problem (T1, T2)

12 Oct 2026. Labels as in BRIEF.md: **PROVED** (full proof here), **CHECKED** (verified, proof sketched), **CONDITIONAL**, **CONJECTURE**. Numerics are evidence only.
Citations: R1, R4 (with the repairs in R6 and R8); DCE = Domain Closure and Extendability (prop:ideal); v3 = Full Coverage by Homothetic Credal Families v3 (thm:general); PB = TRIANGLE_A0_A1_PROJECTIVE_BOUNDARY.md (device, CPM; read for this round); FA = TRIANGLE_A0_A1_NOGO_FIXED_ANCHORS.md; NOGO = CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md.
Script: `r10py/mixture_check.py`.

---

## 0. Outcome

**No realisation of T1 was found. Every design that exploits the freedoms listed in the task fails at a point now identified by a proved lemma. One new positive construction was found; it covers no triangle, but it covers polygons arbitrarily close to T1.**

1. **Vertex anchoring (Thm V, PROVED; any ranking system, any n ≥ 3).** Under strict (G), (S), (LA) and (LF) at D_K, each vertex model is C_{e_i} = D_{V_i} with **e_i ∈ V_i** whenever e_i ∉ K. Consequences:
   * no gamble with a negative coordinate is accepted by every evaluable model (a.e.);
   * rejection inside −T by every evaluable model is the same thing, so it is impossible too;
   * the only advice that every evaluable model can give is no advice, and that can only happen on pairs {h, −h} with h ∉ D_K ∪ N and −h ∉ D_K ∪ N.

   So the region on which every evaluable model gives the same advice can never reach into T, and the gambles on which the evaluable models do not all give the same advice always include all of D_K. R4 Remark B3's escape is closed. (H0) is automatic on D_K ∪ N, except on pairs with advice range {+,−}.
2. **Vertex-coherent advice-range structures (Prop V4, PROVED).** These are exactly the *compatible vertex tuples*: credal V_i ∋ e_i with V_i ⊆ conv(V_j ∪ {e_i}) and Av ∩ D_i ≈ D_{V_i}.
3. **Boundary priors on decomposable domains (Lemma E, PROVED).** At a boundary prior with support S, every coherent Bayes model D_{K*} has K* ∩ Δ_S ≠ ∅. This replaces R4 (K4), which needed the all-model domain. So pairs on which every evaluable model gives no advice cannot weaken FA's box step.
4. **Positive construction (Thm M, PROVED): gauge mixtures.** Every compatible tuple, with any choice of "gauges" M_i (ν(M_i) = V_i), gives an additive system on a decomposable domain in which:
   * the Bayes model at **every** prior is unique a.e. and coherent: K_p = ν(Σ p_i M_i);
   * every interior target K_{p*} ⊆ int Δ is covered with (LF).

   Examples: a regular hexagon around u; 9-gons converging to T1 in Hausdorff distance (§5.3).
5. **Ray lemma (Thm R, PROVED).** No triangle in general position is the target of an additive realisation whose chart vector has concave components near ∂D_K. In particular, no gauge mixture covers T1 or any generic interior triangle (T2). The proof uses only the target prior: three edge rays and two crossings per coordinate force a zero vector.
6. **No plateau, measurable charts (Thm P, PROVED, modulo R4 (K1), (K3) as repaired by R8).** This is PB Theorem 4.1 for measurable charts. If pairs near a facet crossing are split, then K_{Q_s} ≠ K for all s ∈ (0,1) along Q_s = (1−s)p* + sδ_j. Hence a plateau around p*, the escape that densely discontinuous charts were supposed to allow, is impossible.
7. **Residual for T1, now sharper (§8).** An additive realisation on a decomposable domain with (LF) must do one of two things:
   * use adjacent pairs, with K_p ⊆ h^⊥ on their d-faces (the R4 residual); or
   * have split charts whose facet traces escape FA pinning, which requires failure of (H1).

   The conditional no-go of R1 Thm 4.2 / R4 Cor B2–C3 now holds on **every** decomposable domain with (H0) deleted. It is still CONDITIONAL on NOGO/PB/FA and (H1).

---

## 1. Setting

As in BRIEF.md, BRIEF2.md and R1 §§1–2. Write:
* D = D_K for the target, with K ⊆ int Δ and n = 3 unless stated;
* N for the (LF) neighbourhood of ∂D∖{0};
* Av for the set of orientations h such that some evaluable model accepts h (acceptance of h is in the advice range of the choice represented by h);
* Fp ⊆ Av for the orientations h that every evaluable model accepts (the advice range is {+});
* D_i = {h : h_i > 0}, and ν(x) = x/(𝟙·x).

Shrink N so that it is an open cone with N ∩ (−N) = ∅ and N ∩ (−cl D) = ∅. This is possible because ∂D ∩ (−cl D) = {0}: if P_K(h) = 0 ≤ P_K(−h), then h ⊥ K, and since K spans ℝⁿ, h = 0. Then (LF) says that **for a.e. h ∈ N, the advice range of the choice represented by h contains both "accept h" and silence**: R may add or delete h, and R's treatment of −h equals D's, namely not accepted.

---

## 2. Vertex anchoring and the structure of the advice ranges

**Theorem V (vertex anchoring). PROVED.** Let n ≥ 3. Consider any ranking system on a decomposable domain satisfying strict (G), (S) and (LA), with a coherent target D = D_K ∈ C_L at which (LF) holds. Let e_i ∉ K, and let C_{e_i} ≈ D_{V_i} be the (coherent) vertex model. Then e_i ∈ V_i.

*Proof.*
* By DCE prop:ideal (or R1 Lemma 1.5 in the additive case), C_{e_i} gives, at world i, the best advice in the advice range a.e.
* On N, the advice range contains both "accept h" and silence (§1). Hence for a.e. h ∈ N: h ∈ C_{e_i} iff h_i > 0. (If h_i > 0, accepting is good and uniquely best. If h_i < 0, accepting is bad and silence is better.)
* N ∩ D_i is open and a.e. contained in the open convex cone D_{V_i}. Hence N ∩ D_i ⊆ int cl D_{V_i} = D_{V_i}.
* N ∩ {h_i < 0} is open and a.e. disjoint from D_{V_i}. Hence it is disjoint from D_{V_i}.
* *A boundary gamble in the plane h_i = 0.* Restricted to the hyperplane {h_i = 0} (dimension n−1 ≥ 2), P_K takes a positive value at 𝟙 − e_i (since m_i < 1 on K) and a negative value at its negative. Its unit sphere is connected, so there is h⁰ ≠ 0 with h⁰_i = 0 and P_K(h⁰) = 0. Then h⁰ ∈ ∂D∖{0} ⊆ N.
* *V_i touches the line through h⁰.* For small δ > 0:
  * h⁰ + δe_i ∈ N ∩ D_i, so min_{V_i} m·h⁰ + δm_i > 0. Letting δ → 0 gives m·h⁰ ≥ 0 on V_i.
  * h⁰ − δe_i ∈ N ∩ {h_i < 0}, so there is m_δ ∈ V_i with m_δ·h⁰ ≤ δ.
  * By compactness some w ∈ V_i has w·h⁰ = 0.
* *That point must be e_i.* Suppose w ≠ e_i. Then w and e_i are linearly independent, so there is k with k·w = 0 and k_i = 1. For small θ > 0, h^θ = h⁰ + θk lies in N, and h^θ_i = θ > 0, so h^θ ∈ D_{V_i}. But h^θ·w = 0, so h^θ ∉ D_{V_i}. Contradiction. Hence w = e_i ∈ V_i. ∎

**Corollary V1 (acceptance by every evaluable model). PROVED.** Under Thm V's hypotheses, for a.e. orientation h, if every evaluable model accepts h then h_i ≥ 0 for every i with e_i ∉ K. For K ⊆ int Δ this means that every evaluable model accepts h only for nonnegative gambles h. Rejection inside −T by every evaluable model is acceptance of the opposite orientation by every evaluable model, so it is also impossible.

*Proof.* An h accepted by every evaluable model is accepted by every model in M_L, in particular by C_{e_i} ≈ D_{V_i}. Since e_i ∈ V_i, every h ∈ D_{V_i} has h_i > 0. ∎

**Corollary V2 (advice ranges = compatible vertex tuple). PROVED.** Assume Thm V's hypotheses and K ⊆ int Δ. Then:
* (a) Av ∩ D_i ≈ D_{V_i} with e_i ∈ V_i, for each i.
* (b) V_i ⊆ conv(V_j ∪ {e_i}) for all i ≠ j ("compatibility").
* (c) Av ∖ {h ≤ 0} ≈ ∪_i D_{V_i}, and D ∪ N ⊆ Av a.e.
* (d) Every evaluable model gives no advice on a pair {h, −h} (neither acceptance is in its advice range) only if h ∉ ∪_i D_{V_i} and −h ∉ ∪_i D_{V_i}; note ∪_i D_{V_i} ⊇ D ∪ N.

*Proof.*
* (a): C_{e_i} ∩ D_i ≈ Av ∩ D_i (best advice in the advice range). Also C_{e_i} ∩ {h_i < 0} ≈ Fp ∩ {h_i < 0}, which is null by V1.
* (b): D_{V_j} ∩ D_i ≈ Av ∩ D_j ∩ D_i ⊆ Av ∩ D_i ≈ D_{V_i}. The left side is D_{conv(V_j ∪ e_i)}. Open convex cones that are a.e. nested are nested, and D_A ⊆ D_B ⟺ B ⊆ A for credal sets.
* (c): every non-nonpositive orientation has some positive coordinate. D ∈ M_L gives D ⊆ Av; (LF) gives N ⊆ Av.
* (d): immediate from (c). ∎

**Corollary V3 ((H0) is automatic). PROVED.** For a.e. h ∈ D ∪ N, the advice range of the choice represented by h is {acc h, 0}, {acc h, 0, acc −h} or {acc h, acc −h}. In particular (H0)_V of R4 holds for every V ⊆ D ∪ N on which a.e. pair is non-adjacent, because pairs with advice range {+,−} are always adjacent (R4 Thm A). R1 Prop 2.5's cone U′ = D_{K′} can be taken inside D ∪ N: choose K′ close enough to K that D_{K′} ∖ D ⊆ N, by compactness on the sphere.

**Proposition V4 (answer to the task's first question). PROVED.** Under the hypotheses of Thm V, with K ⊆ int Δ, the advice-range structures for which all vertex models are coherent are exactly those with the following properties:
* every evaluable model accepts h only for nonnegative gambles h;
* Av ≈ ∪_i D_{V_i} (off the nonpositive orthant), for a compatible tuple (V_1, …, V_n) with e_i ∈ V_i and D ∪ N ⊆ ∪_i D_{V_i};
* in addition: advice ranges that contain acceptance of h for each h ∈ Av, and contain silence wherever they contain no other kind of advice; on the remaining pairs {h, −h} (h ∉ Av and −h ∉ Av) every evaluable model gives no advice.

Conversely, every compatible tuple is the vertex structure of a full additive system (Thm M with M_i = V_i).

**Effect on the proposed design.** The region on which every evaluable model gives the same advice cannot touch D. In particular, on FA's deep witness z′ = a+λb ∈ D the evaluable models do not all give the same advice, and z′ keeps its full chart constraints. A reduction "to problems near ∂T" by restricting the evaluable models so that they all give the same advice on the interior is impossible.

---

## 3. Boundary priors on decomposable domains

**Lemma E. PROVED.** Additive system on a decomposable domain with (LA), (S), strict (G), (LF) at D_K, K ⊆ int Δ. Let p₀ ∈ ∂Δ have support S, and let C(p₀) = {h : p₀ ∈ R(h)}. Then:
* there is a coherent p₀-Bayes model D_{K*} (R1 Lemma 1.3(a));
* every such model satisfies C(p₀) ⊆ cl D_{K*} a.e., and K* ∩ Δ_S ≠ ∅.

Consequently there are no density points a of C(p₀), b of C(p₀), and λ > 0 with (a+λb)_S < 0.

*Proof.*
* A unique minimiser is chosen by every Bayes model, so C(p₀) ⊆ D_{K*} a.e.
* Take h with h_S < 0. Not every evaluable model accepts h (Cor V1), so the advice range of the choice represented by h contains silence or acc −h. Either alternative is strictly better at every world of S (strict (G)), hence strictly better at p₀. So D_{K*} ∩ {h_S < 0} is null; being open, it is empty.
* Separation: if K* ∩ Δ_S = ∅, a gamble negative on Δ_S and positive on K* exists. So K* ∩ Δ_S ≠ ∅.
* For the last claim: density points of a set a.e. contained in the closed cone cl D_{K*} lie in it. Hence a+λb ∈ cl D_{K*}, and so (a+λb) + δ𝟙 ∈ D_{K*} ∩ {h_S < 0} for small δ. Contradiction. ∎

**Remark.** This is FA §10.1's box contradiction in decomposable-domain form. It needs only that the charts of the two facet witnesses contain the edge prior. It does not need R4 (K4) (all-model forbidden support), (H0), or that acceptance of gambles with h_S > 0 is in the advice range. Hence pairs {h, −h} (h ∉ Av, −h ∉ Av) on which every evaluable model gives no advice, which would weaken (K4) by shrinking Av, do not weaken the box. The box is a consequence of facet charts plus boundary coherence.

**Corollary C (consolidation). PROVED, for the deletion of (H0).** R4 Cor B2, Cor C3 and Prop G2 hold on every decomposable domain with (LF) at T1, with (H0) deleted.
* Cor V3 supplies (H0) on U′ wherever pairs are non-adjacent.
* R8's advice-range flags are covered:
  * (K3) positive case: x⁻ ∈ U′;
  * G2: z′ ∈ D;
  * (K4): replaced by Lemma E.

The resulting no-go remains CONDITIONAL on NOGO/PB/FA and on (H1) (respectively (H1⁺) with "no precise segments").

---

## 4. A positive construction: gauge mixtures

**Theorem M. PROVED (any n ≥ 2).** Setup:
* Let M_1, …, M_n be compact convex subsets of ℝⁿ_{≥0}∖{0}, with V_i := ν(M_i). Assume:
  * (M1) M_i contains a point a_i e_i, a_i > 0;
  * (M2) V_i ⊆ conv(V_j ∪ {e_i}) for all i ≠ j.
* Put f_i(h) = min_{m∈M_i} m·h (concave, positively homogeneous, continuous) and Av = ∪_i D_{V_i}.
* Advice ranges: acceptance of g is in the advice range iff g ∈ Av; acceptance of −g iff −g ∈ Av; silence always. So every evaluable model gives no advice on pairs {g, −g} with g ∉ Av and −g ∉ Av.
* Penalties: R1 Prop 2.1 (converse), with c(g) = f(g), and for advice range {+,0,−} c′(g) = f(−g), rescaled to be integrable.

Then:
* (a) Strict (G) holds on the advice ranges.
* (b) At **every** p ∈ Δ, the Bayes act is a.e. unique and the Bayes model is D_{K_p}, where K_p = ν(Σ_i p_i M_i).
* (c) Hence (LA), (S), (C), (G), (IB) hold with C_p = D_{K_p} (R1 Thm 2.2(S) = v3 thm:general on decomposable domains). (E) is supplied by the all-model Brier ranking, as in the brief.
* (d) For every p* ∈ int Δ with K_{p*} ⊆ int Δ, (LF) holds at D_{K_{p*}}. So D_{K_{p*}} is covered.

*Proof.*
1. *Signs.* f_i(h) > 0 ⟺ h ∈ D_{V_i}, since m = (𝟙·m)ν(m) with 𝟙·m > 0. Take h ∈ Av.
   * If h_i < 0, then f_i(h) ≤ a_i h_i < 0 by (M1).
   * If h_i > 0, pick j with h ∈ D_{V_j}. Then h > 0 on conv(V_j ∪ e_i) ⊇ V_i by (M2), so f_i(h) > 0.

   So c is strictly sign-preserving on Av, and so is c′ = f(−·) on −Av. R1's converse then gives (G)-penalties, which is (a).
2. *Charts.* Put F_p := Σ p_i f_i = min_{S_p} m·h, where S_p = Σ p_i M_i is compact convex in ℝⁿ_{≥0}∖{0}. For the cases:
   * Advice range {+,0}: accept g iff F_p(g) > 0.
   * Advice range {+,0,−}: concavity and homogeneity give F_p(g) + F_p(−g) ≤ F_p(0) = 0. So p·c > 0 forces p·c > p·c′, and the chart is accept g iff F_p(g) > 0, accept −g iff F_p(−g) > 0, silence otherwise.
3. *Uniqueness and coherence.* Ties occur only where F_p(±g) = 0, i.e. on ∂D_{ν(S_p)}, which is null. If F_p(h) > 0, then some f_i(h) > 0, so h ∈ Av. Hence the Bayes model is exactly {F_p > 0} = D_{K_p}, which is coherent; this is (b).
4. (c) is R1 Thm 2.2(S), refereed CORRECT in R6.
5. *(LF).* Let h ∈ ∂D_{K_{p*}}∖{0}, so F_{p*}(h) = 0.
   * If every f_i(h) ≤ 0, then every f_i(h) = 0, so a_i h_i ≥ 0 and h ≥ 0, h ≠ 0. That contradicts F_{p*}(h) = min_{S_{p*}} m·h > 0, which holds because S_{p*} lies in the open orthant cone when K_{p*} ⊆ int Δ.
   * So h ∈ D_{V_i} ⊆ Av for some i. Av is open, so N := Av ∩ O is an (LF) neighbourhood, for O as in §1.
   * Silence is always in the advice range. Finally, D_{K_{p*}} = C_{p*}. ∎

**Examples.**
* *Common-W tuples.* M_i = conv({a_i e_i} ∪ b_i W̃) for a compact convex W̃ in the open orthant. Then V_i = conv(ν(W̃) ∪ e_i), and (M2) holds trivially.
* *Precise identity system.* M_i = {e_i}. This gives advice range {+,0,−} everywhere and K_p = {p}.
* *Hexagon.* W̃ = {u}, a = b = 1, p* = u. Then K_u = conv{u ± (e_i − u)/3}, a regular hexagon around u (6 vertices numerically). This is an interior polygonal target, covered with continuous charts.
* *Non-example (affine contamination).* Try V_i = (1−λ_i)y_i + λ_iΔ, which would make K_p a contamination of an affine σ(p) when M_i = V_i.
  * (M1) forces y_i = e_i, since e_i ∈ V_i requires the j-coordinates of (1−λ_i)y_i to vanish for j ≠ i.
  * Then (M2) fails unless λ_i ∈ {0,1}: the vertex (1−λ_i)e_i + λ_i e_k of V_i is not in conv(V_j ∪ e_i), whose intersection with the edge [e_i, e_k] is {e_i}.
  * So contamination families do not arise this way (consistent with R1 Thm 4.1). Thm R below covers every triangle.

**Proposition M′ (polygons converging to T1). PROVED.**
* Take W = T1(ε′) with ε′ < ε, M_i = conv{a e_i, b w_1, b w_2, b w_3} (w_k the vertices of W), and p* = u.
* Every point of S_u has the form (b/3)Σ(1−t_i)w_i + (a/3)Σt_i e_i, so ν(S_u) = λw̄ + (1−λ)t/Σt with w̄ ∈ W.
* Here 1−λ ≤ aΣt_i / (bΣ(1−t_i)). Either:
  * Σ(1−t_i) ≥ δ′, and the distance to W is ≤ 3a/(bδ′); or
  * all t_i > 1−δ′, so t/Σt is within O(δ′) of u ∈ int W.
* Taking δ′ ≈ inradius(W) gives d_H(K_u, W) = O(a/b), with K_u ⊇ W.
* So d_H(K_u, T1(ε)) ≤ O(a/b) + O(ε−ε′), and every K_u is covered by Thm M.

Numerics (`mixture_check.py`), where Hausdorff distances are measured against T1(0.3):

| (ε′, a/b) | vertices of K_u | Hausdorff distance to T1(0.3) |
|---|---|---|
| (.28, .05) | 9 | 0.0186 |
| (.29, .01) | 9 | 0.0053 |
| (.295, .002) | 9 | 0.0035 |

Across all tested systems:
* (G)-sign violations among ~7·10⁴–1.7·10⁵ sampled orientations in Av: 0;
* mismatches between explicit-penalty minimisation and {F_p > 0}, at 12 priors including vertices and edge priors: 0;
* ties: 0;
* midpoint-convexity failures: 0;
* every sampled point of ∂D_K lies in Av, with positive margin.

This is a *nearby reachable result* in the sense of the project preferences: polygonal (9-gon) targets arbitrarily close to T1 are covered by explicit additive systems on decomposable domains with continuous charts and strict guidance. It complements the parallel-body approximations of v19 / NOGO (5.1).

---

## 5. Why gauge mixtures (and all concave charts) miss every triangle

**Theorem R (ray lemma). PROVED.** Setup:
* Let K ⊆ int Δ (n = 3) be a triangle in general position: no line through two vertices of K contains a vertex of Δ.
* Let U ⊇ cl D_K∖{0} be an open convex cone and p* ∈ int Δ.
* Let f_1, f_2, f_3 be concave and positively homogeneous on U.

Then the following cannot both hold:
* (i) for h ∈ ∂D_K∖{0} with h_i ≠ 0, f_i(h) has the sign of h_i;
* (ii) Σ_i p*_i f_i = 0 on ∂D_K.

*Proof.*
1. *Facets and crossings.* Let v_1, v_2, v_3 be the vertices of K. Let F_k = {h : h·v_k = 0, h·v_j > 0 (j ≠ k)} be the facets, and r_{kj} = cl F_k ∩ cl F_j the three edge rays. The edge rays are linearly independent (cl D_K is a simplicial cone). Coordinate i *crosses* on F_k when {h_i = 0} meets relint F_k. That happens iff the line through v_k and e_i strictly supports K. From the exterior point e_i there are exactly two such tangent vertices, by general position. So each i crosses on exactly two facets. General position also gives r_i ≠ 0 for every edge ray r.
2. *Linearity on facets.* On the convex cone F_k, Σ p*_i f_i = 0 is a positive combination of concave functions. Each f_i is therefore affine on F_k (equality in each concavity inequality), hence linear: f_i(h) = m_{ik}·h. By continuity this extends to cl F_k.
3. *Crossing coordinates.* If i crosses on F_k, then by (i) the functionals m_{ik}·h and h_i on the plane v_k^⊥ have the same sign on an open set and vanish on the same line. So m_{ik} ≡ α_{ik}e_i (mod v_k), with α_{ik} > 0, and f_i(r) = α_{ik}r_i on cl F_k.
4. *One constant per coordinate.* The two crossing facets of i share an edge ray r with r_i ≠ 0. So α_i := α_{ik} does not depend on which crossing facet is used.
5. *Every edge ray sees all three coordinates.* Each i has only one non-crossing facet, so on every edge ray r_{kj} each coordinate crosses on F_k or on F_j. Hence f_i(r) = α_i r_i for all i and all three edge rays.
6. *Contradiction.* Condition (ii) gives Σ_i p*_i α_i r_i = 0 for three independent r. Hence p*_i α_i = 0, contradicting p*_i, α_i > 0. ∎

**Corollary R1. PROVED.**
* No gauge-mixture system (Thm M) covers a triangle in general position. In particular it covers neither T1 nor a generic T2. (In Thm M, F_{p*} = Σ p*_i f_i vanishes on ∂D_{K_{p*}}, and the f_i are concave and sign-preserving on Av ⊇ ∂D∖0.)
* More generally, in no additive realisation of such a triangle does the chart field admit a representative λ(h)c(h) (λ > 0) that is concave componentwise on a neighbourhood of cl D_K∖0 and satisfies p*·λc = 0 on ∂D_K.

**Comparison with NOGO.** For general continuous charts the facet maps are linear only projectively (factors ξ_F). The ray relations then have the two solutions of R4 Prop G1, and only the boundary box (Lemma E) kills them. Concavity forces ξ ≡ 1, so the rays alone suffice, and for every triangle. This is the precise reason the one natural construction class fails on triangles but succeeds on polygons with more sides: a hexagon has edge rays adjacent only to non-crossing facets of some coordinates, so step 5 fails.

---

## 6. No plateau at the target prior, for measurable charts

Standing hypotheses for this section:
* the additive system is on a decomposable domain with (LA), (S), (C), strict (G), and (LF) at D = D_K;
* K is T1, or any interior triangle in general position;
* U′ is as in Cor V3;
* **(Sp)**: a.e. pair meeting U′ is non-adjacent. By R4 Thm B, (Sp) holds whenever dim K_p = 2 for every interior p.

Under these hypotheses (H0)_{U′} holds (Cor V3). So R4 (K1) and (K3) apply on U′:
* (K1): the half-plane chart H(h) = {c(h)·p > 0}, with P(·,h) ≥ 0 on cl H(h) and ≤ 0 off H(h) for h ∉ Bad;
* (K3): essential clusters of ĉ at mixed points have the strict signs of the point, uniformly near it (PB (3.2)), as repaired in R8.

**Theorem P (PB Thm 4.1 for measurable charts). PROVED** (modulo R4 (K1), (K3)).
Let F be a facet of D, and w ∈ relint F a point with w_i = 0, w_j > 0 for some i ≠ j. Put Q_s = (1−s)p* + sδ_j and E = {x ∈ U′ : ℓ_F(x) < 0, x_j > 0}, with ℓ_F the facet form. Then D_{K_{Q_s}} ∩ E ≠ ∅ for every s ∈ (0,1). In particular K_{Q_s} ≠ K for all s ∈ (0,1). So {p : K_p = K} has empty interior: **no plateau around p***.

*Proof.* Let d = inf{s ∈ [0,1) : D_{K_{Q_s}} ∩ E ≠ ∅}.
* *d < 1.* Near ∂D, exterior points with x_j > 0 lie in Av and are accepted near δ_j.
* *Monotone in s.* If x ∈ E is accepted at Q_{s₀}, its convex chart contains Q_{s₀} and δ_j, hence every Q_s with s ≥ s₀.

Suppose d > 0 and put Q = Q_d ∈ int Δ.

*Step 1 (uniform interior acceptance).*
* For a.e. h ∈ D the chart contains p*, since B_{p*} ≈ D, so q*·ĉ(h) > 0.
* By (K3) there are a convex neighbourhood U of w in U′ and c₀ > 0 with ĉ_j ≥ c₀ a.e. on U.
* Hence Q·ĉ(h) ≥ dc₀/(1+d) for a.e. h ∈ D∩U. On the ball R = B(Q, dc₀/(2+2d)) ∩ int Δ, every q has q·ĉ > 0 a.e. on D∩U.
* By (K1), P(q,h) ≥ 0 there, and P(q,·) = 0 only on the null set ∂D_{K_q}. So D∩U is a.e., hence entirely, contained in D_{K_q} for all q ∈ R.

*Step 2 (ratio law). Every exterior essential cluster v at a point of A satisfies Q·v = 0, where A ⊆ relint F ∩ U is a compact neighbourhood of w in F.*
* For s < d and a.e. exterior h ∈ E near A, h ∉ D_{K_{Q_s}}. Since h ∈ ∂D_{K_{Q_s}} is null for fixed s, (K1) gives Q_s·ĉ(h) ≤ 0. Use countably many s ↑ d and pass to the limit: Q·v ≤ 0.
* For s > d, pick an accepted x ∈ E. For w′ ∈ A, the point z = w′ + η(w′−x) lies in D ∩ {h_j > 0} ⊆ D_{K_{Q_s}}; that inclusion holds because charts contain p* and δ_j. So w′ ∈ (x, z) ⊆ D_{K_{Q_s}}.
* Hence a neighbourhood of A is accepted at Q_s, so Q_s·ĉ ≥ 0 on exterior points near A. Pass to the limit: Q·v ≥ 0.

*Step 3 (nested positivity).* For q ∈ R and exterior clusters v (at w′ ∈ A) and v′ (at w″ ∈ A): q·v > 0 ⇒ q·v′ ≥ 0.
* If q·v > 0, a non-null set of exterior h near w′ has q ∈ H(h). By (K1) these h lie in cl D_{K_q}.
* With D∩U ⊆ D_{K_q} (Step 1), the convex-combination argument of Step 2 puts A ⊆ D_{K_q}, and hence a neighbourhood of A.
* So q·ĉ > 0 for exterior good h near w″, giving q·v′ ≥ 0.

*Step 4 (contradiction).*
* The affine functionals q ↦ q·v and q ↦ q·v′ vanish at Q (Step 2). Neither is constant on aff Δ, since v has mixed strict signs by (K3).
* Step 3 on the ball R forces v′ − λv ∈ ℝ𝟙 with λ ≥ 0. Then Q·(v′−λv) = 0 gives v′ = λv, so v′ = v.
* So all exterior clusters at points of A coincide. But A contains points with w′_i > 0 and points with w″_i < 0, whose clusters have v_i > 0 and v_i < 0 respectively by (K3). Contradiction.

Hence d = 0. ∎

**Consequence.** The densely-discontinuous "plateau" mechanism, which works in n = 2 (R1 Ex. 3.3) and which R1 §4.2(c) noted as compatible with all local constraints at p*, is impossible here for T1 (every j is a crossing coordinate of some facet) whenever pairs near the facet crossings are split. Measurable penalties therefore buy nothing at p* itself.

**Further transfer (sketch).**
* *PB Thm 5.2 (unique exterior cluster): CHECKED (sketch).*
  * Directional essential clusters exist along thin cones around w − y e_k.
  * Lemma 5.1 is immediate in K-world: supports at w ∈ relint F_k lie in K_q, and K_q → K (Hausdorff) forces them to converge to v_k.
  * The step "an accepted −e_k sequence forces (p_s)_k = 0" holds verbatim for supports p_s ∈ K_{q_s} with p_s·w = 0.
* *PB Thm 6.1 and Cor 6.2–6.3:* CONJECTURE (expected to transfer the same way).
* *FA §§3–9 (pinning, i.e. projective linearity of facet traces):* CONJECTURE (not attempted). This, and only this, separates the split measurable case from NOGO.

---

## 7. Designs tried, and where each fails

| design (freedom exploited) | fate | reason |
|---|---|---|
| every evaluable model accepts gambles deep inside T | impossible | Thm V, Cor V1 (any ranking) |
| every evaluable model rejects gambles deep inside −T | impossible | same (it is acceptance of −h by every evaluable model) |
| every evaluable model gives no advice on some pairs on which T gives no advice | possible; only shrinks Av to ∪D_{V_i} | Cor V2. It cannot weaken the box (Lemma E), and it cannot reach D (Prop V4) |
| reduce to a local design near ∂T by making every evaluable model give the same advice on the interior | impossible | on D the evaluable models never all give the same advice (V2(c), V3) |
| vertex-model mixtures K_p = Σ p_i V_i, gauge mixtures ν(Σ p_i M_i) | full systems exist (Thm M) | cover no triangle (Thm R). Cover hexagons and 9-gons arbitrarily close to T1 (M′) |
| affine reparametrised contamination (1−λ)σ(p)+λΔ via mixtures | fails | compatibility forces V_i = (1−λ)e_i+λΔ, which violates (M2) (§4 check; also R1 Thm 4.1) |
| plateau K_p ≡ K near p* with charts jumping on dense null sets | impossible if pairs near the facet crossings are split | Thm P |
| advice range {+,−} inside D | possible but adjacent | R4 Thm B: K_p ⊆ h^⊥ on the d-face. These feed the R4 residual |
| wedges with advice range {+,0,−} near vertices (precise caps) | open | R4 residual (precise d-faces cutting box witnesses at all vertices) |
| split measurable charts with dense Bad | open | needs failure of FA pinning. PB §4 is now excluded measurably (Thm P), §5 sketched |

One further natural attempt was checked and fails: K_p = conv(K_U ∪ {σ_j(p)}) with diagonal-projective σ_j(p*) = v_j. For two-negative h the chart is {h·p + λ min_j h_j p_j > 0}, whose two lines meet inside int Δ. That is a wedge with R(−h) = ∅, which is not a {+,0} chart (direct computation).

---

## 8. Precise obstruction statement (for the record)

**Theorem O (CONDITIONAL on NOGO + PB + FA as in R1 Thm 4.2; (H0) removed).** There is no additive ranking system on any decomposable domain that satisfies (LA), (S), (C), strict (G), (LF) at T1, and (H1), and in which a.e. pair meeting U′ is non-adjacent (e.g. all interior K_p two-dimensional).

Unconditional parts:
* advice that every evaluable model gives is irrelevant (Thm V, Cor V1–V3);
* the box step holds on decomposable domains (Lemma E);
* plateaus are excluded measurably (Thm P);
* the concave/mixture class is excluded for every triangle (Thm R).

**Residual (open).** An additive T1 realisation must have at least one of the following:
* (A) a non-null set of adjacent pairs in U′, with degenerate K_p on their d-faces (R4 residual: precise segments under (H1⁺));
* (B) split charts on U′ whose discontinuity set Bad has no closed null envelope, and whose facet traces escape FA pinning.

Next steps, in order of expected payoff:
1. Transfer PB §6 and FA §§3–9 to essential clusters. This would close (B).
2. A global argument for (A): vertex anchoring now gives V_i ∋ e_i, and Lemma E gives K* ∩ Δ_S ≠ ∅ at every edge prior, as boundary data for the caps.
3. Classify the gauge-mixture targets: which polygons are covered. Thm R shows triangles never are; hexagons and 9-gons are.
