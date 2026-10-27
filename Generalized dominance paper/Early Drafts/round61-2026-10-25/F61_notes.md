# F61 — Full-domain role: two-sided domains and the admissibility route (25 Oct 2026)

Labels: PROVED (in this note, not refereed) / CHECKED / CONJECTURE / NUMERICS. Scripts and outputs: `f61py/` in this folder
(`common.py`, `full_domain_veto.py`, `domains_vb.py`, `domains_vb_big.py`, `contamination_Aeps.py`, `exempt_facet.py`, with `.out` files).

## 0. Answer in brief

1. **On the full four-advice domain the veto mechanism dies, and nothing non-CPM replaces it** (within the classes below).
   - *Convex leading levels* (any shape of world order that refines them): the only undominated targets D_K with K ⊆ relint Δ are **normalised boxes** (Thm A). T1 and every ε-contamination with n ≥ 3 are not boxes.
   - *Veto-led lexicographic rankings, any shape of veto (convex or not)*: on the full domain every veto must vanish except on sure losses (Thm B, Cor B1). With Brier as second level, the only undominated targets are precise.
   - *Strictly guiding leading levels*: undominatedness of generic Bayes acts is exactly the CPM realisation problem (Prop E). So the full domain gives nothing the CPM programme does not.
2. **The obstruction is local and has an exact geometric form.** A veto at world k survives only if no available gamble that is correct at k *and at some other world* lies beyond the facet F_k (Thm B, Cor B3). The full domain and the symmetric domain U ∪ −U both violate this.
3. **Nearest reachable domain (PROVED positive result, Thm D).** Let K = conv{v_1,…,v_n}, v_i = (1−ε_i)p + ε_i e_i with p interior and 0 < ε_i < 1 (this includes T1 and every interior ε-contamination, in any number of worlds). Let
   A_K := {h : h has at most one positive coordinate, or v_k·h ≥ 0 at every k with h_k > 0}.
   On the domain of all measurable models X ⊆ A_K, the ranking "level 1: veto of *wrong* acceptances beyond the facet, φ_k(h) = 1[h_k<0]·[−v_k·h]_+; level 2: Brier" satisfies compact range, every undominated model coherent (explicitly polyhedral), target undominated, strict (G), (IB), direct (C), (LF) at the target.
   - A_K is **genuinely two-sided**: for n = 3 it contains both h and −h for 89–98% of gambles (NUMERICS), including a full neighbourhood of the single-negative part ("middle arc") of every facet of ∂D_K.
   - It is **maximal** for veto-led rankings with a Brier second level, up to one possible exempt facet (Cor B3). The obvious one-exempt-facet design fails (NUMERICS).
4. **What replaces vetoes on two-sided domains:** vetoes indexed by the advice, not by the accepted gamble (charge only *wrong* acceptances), together with a domain that removes exactly the gambles where that indicator would make minimisers non-convex. The indicator then never bites on an undominated model (Lemma D1).

## 1. Setting and named hypotheses

- n finite worlds; μ absolutely continuous, full support, finite first moment. A *domain* is given by a measurable cone A ⊆ ℝⁿ of **available gambles**. Models are measurable X ⊆ A, modulo null sets. At the pair {h, −h} the options are those of h, −h that lie in A (accept h, accept −h, silence, both = contradiction). The full domain is A = ℝⁿ. The U-domain is A = U = D_{K'}. Every such domain is closed under splicing and convergence in measure.
- *Coherent model on A*: X = D_{K*} ∩ A a.e. for some nonempty closed convex K* ⊆ Δ.
- (Int) Each level is integral: z_{j,ℓ}(X) = ∫ f_{j,ℓ}(s, a_X(s)) dμ, with f(s, silent) = 0 and integrable f. Write c^ℓ_j(h) for the integrand of *accepting h* (h determines its pair), and treat contradictions separately.
- (Lex) World j's order is lexicographic in its levels. Weaker, used in Thm A: (Ref) world j *refines* its first level: a_j(Y) < a_j(X) ⇒ Y ≺_j X.
- (G) strict guidance: correct < silent < wrong < contradictory, strictly on non-null sets.
- *Sign-correct* c: c(h) ≤ 0 if h_j > 0 and c(h) ≥ 0 if h_j < 0. Strictly sign-correct: strict inequalities a.e. (Ref)+(G) force the first level to be sign-correct (removing a correct acceptance would lower a_j and so be strictly better, against (G)).
- (VL) *veto-led class*: each world's first level is a veto c_j ≥ 0 (possibly ≡ 0); (L2) each world's second level is strictly sign-correct. Later levels arbitrary. (Br) the second level is Brier, c²_j(h) = −h_j.
- Throughout, K is closed convex with K ⊆ relint Δ, unless stated.

Tools used repeatedly (from LDG v3.1 §3.5 and the VB note): Lyapunov (finitely many integrable coordinates and finitely many actions per pair give a convex compact range), Lemma zorn, Prop lexbayes (its proof works for any number of levels: only levels 1 and 2 enter the separation), and the **converse**: an a.e.-unique minimiser of a lex-Bayes functional over its face is undominated.

Two easy facts. (F1) Undominated models never contradict: replacing a contradiction by silence improves every world with s_j ≠ 0. (F2) If D_K is undominated and some model zeroes every first level, Prop lexbayes applies to D_K.

## 2. Theorem A: convex leading levels allow only boxes on the full domain (PROVED)

**Theorem A.** Full domain, (Int), and each world j refines (Ref) a first level whose acceptance integrand c_j is convex on ℝⁿ and not identically zero. (Lexicographic structure, transitivity and completeness are not needed.) If D_K is undominated and e_j ∉ K for all j, then K = ν(Q) for a box Q = ∏_j [l_j, u_j] with 0 ≤ l_j ≤ u_j, Q ≠ {0}, where ν is normalisation. If K ⊆ relint Δ, all l_j > 0.

*Proof.*
1. **Weak Pareto at level 1.** If some Y had a_j(Y) < a_j(D_K) at every j, it would strictly dominate D_K by (Ref). The range of (a_j)_j is convex (Lyapunov). Separation gives α ≥ 0, α ≠ 0, with D_K minimising Σ_j α_j a_j over all models.
2. **Pointwise.** Put ψ := Σ α_j c_j (convex). Minimisation forces ψ ≤ 0 a.e. on D_K (accepting beats silence), and ψ ≥ 0 a.e. on the silent region S of D_K (complement of cl D_K ∪ −cl D_K). Contradictions do not enter, by (F1) and since D_K never contradicts. Convex functions are continuous, so both hold everywhere on those open sets.
3. **Homogenise.** ψ(0) = 0 (each c_j vanishes on {h_j = 0}: sign-correctness plus continuity). Let ψ̂(h) := lim_{t↓0} ψ(th)/t. ψ(th)/t is non-decreasing in t, so ψ̂ ≤ ψ ≤ 0 on D_K. On S, which is a cone, ψ(th) ≥ 0, so ψ̂ ≥ 0. Also ψ̂ = Σ α_j ĉ_j with ĉ_j(h) = c_j'(0; h).
4. **Classification of ĉ_j.** ĉ_j is convex, positively homogeneous and sign-correct, so it vanishes on H_j = {h_j = 0}. Its subgradients ℓ at 0 satisfy max_ℓ ℓ·h = 0 and max_ℓ ℓ·(−h) = 0 for h ∈ H_j, so every ℓ ∝ e_j. Hence ĉ_j(h) = max(−κ_j h_j, −λ_j h_j) with κ_j ≥ λ_j ≥ 0. Therefore ψ̂(h) = max_{q∈Q} (−q·h) with Q = ∏ [α_jλ_j, α_jκ_j].
5. **Degenerate case Q ∋ 0.** Then ψ̂ ≥ 0, so ψ̂ = 0 on D_K. D_K contains gambles with h_j < 0 for each j (since e_j ∉ K), so α_jκ_j = 0 for all j and ψ̂ ≡ 0. Then for j ∈ supp α, ĉ_j ≡ 0, so 0 is a subgradient of c_j at 0 and c_j ≥ 0. With ψ ≤ 0 on D_K, each such c_j vanishes on D_K ∪ {h_j ≥ 0}. The convex hull of that set is ℝⁿ, because D_K has points with h_j < 0. So c_j ≡ 0, which is excluded.
6. **Box case.** ψ̂ ≤ 0 on D_K means min_Q q·h ≥ 0 there, so Q ⊆ cone K by duality. Then D_Q := {ψ̂ < 0} ⊇ D_K. D_Q is an open convex cone disjoint from S (ψ̂ ≥ 0 there), and it is pointed and contains D_K, so it is disjoint from −D_K. An open set inside cl D_K ∪ (−∂D_K) lies in D_K. So D_Q = D_K and K = ν(Q). ∎

**Corollary A1 (PROVED).** For n ≥ 3 no interior ε-contamination (0 < ε < 1, p interior) is a normalised box. The facets of ν(Q) are {m : u_j m_i ≥ l_i m_j}, with normals having n−2 zero coordinates modulo 𝟙. The contamination's facet m_i ≥ (1−ε)p_i·Σm has normal e_i − (1−ε)p_i𝟙, all coordinates nonzero. T1 is not a box (L3.1(c)). So no ranking whose worlds refine convex first levels covers these targets on the full domain. (n = 2: every interval is a box, and boxes are covered.)

The lead's observation (a convex veto vanishing on D_K ∪ {h_j ≥ 0} vanishes everywhere) is step 5. Theorem A adds that convex *signed* first levels are asymmetric-linear in h_j at the origin, and so produce boxes.

## 3. The target pays no veto (Lemma T0, PROVED; this makes S3 rigorous in general)

**Lemma T0.** Any domain A ⊇ D_K that contains the vacuous model; (Int), (Lex), (VL); K ⊆ relint Δ. If D_K is undominated, then every veto vanishes a.e. on D_K.

*Proof.* Let W0 = {i : a_i(D_K) = 0} and suppose M := W0ᶜ ≠ ∅. The vacuous model zeroes all vetoes, so Prop lexbayes gives β ≥ 0 on W0 (β ≠ 0) and α ≥ 0 on M with D_K minimising J = Σ_{W0} β_i b_i + Σ_M α_m a_m over the face {a_i = 0, i ∈ W0}. Let S = supp β. Consider the open set O of h with h_i < 0 for i ∈ S, h_m > 0 large for m ∈ M, and the remaining coordinates small positive. For h ∈ O we have K·h > 0, since every k ∈ K has k_M bounded below, so O ⊆ D_K.
- On O, vetoes at W0 vanish a.e., because D_K pays none.
- Vetoes at M vanish on O by guidance, because h_m > 0.
- So accepting h ∈ O costs Σ_{i∈S} β_i c²_i(h) > 0 (wrong at every i ∈ S), more than silence.

Removing a non-null piece of O from D_K stays in the face and lowers J, a contradiction. ∎

## 4. Theorem B: vetoes collapse on two-sided domains (PROVED)

**Theorem B.** Domain A (open cone, up to null sets) with D_K ⊆ A; (Int), (Lex), (VL), (L2). Suppose every undominated model is coherent. Fix worlds j ≠ m and let Z_m = {c_m = 0}. Then

  Z_m ∩ {h_j > 0} ∩ A  =  C_{jm} ∩ A  (a.e.)  for a convex cone C_{jm}.

If moreover D_K is undominated and K ⊆ relint Δ, then c_m = 0 a.e. on

  A ∩ {h_j > 0} ∩ conv[ (A ∩ {h_m > 0, h_j > 0}) ∪ (D_K ∩ {h_j > 0}) ].

*Proof.*
1. **A one-parameter family.** For t > 0 let X_t minimise J_t = b_j + t·a_m over the face {a_j = 0}. Pointwise, at h with h_j > 0, acceptance costs c²_j(h) + t c_m(h), with c²_j(h) < 0. At −h the cost is ≥ c²_j(−h) > 0. Contradictions are excluded from the face or cost more (lexicographic (G)). So X_t = {h ∈ A : h_j > 0, t·c_m(h) < −c²_j(h)}.
2. **Uniqueness for all but countably many t.** Ties {t c_m = −c²_j} are disjoint for distinct t on {c_m > 0}, and impossible on {c_m = 0}. So only countably many t give a non-null tie.
3. **Undominated.** Suppose Y weakly dominates X_t. At world j, lex gives a_j(Y) = 0 and b_j(Y) ≤ b_j(X_t). At world m, a_m(Y) ≤ a_m(X_t). So J_t(Y) ≤ J_t(X_t), and uniqueness gives Y = X_t a.e. Hence X_t is coherent: X_t = D_{K_t} ∩ A.
4. **Intersection.** X_t decreases in t. Along good t_n → ∞, ⋂ X_{t_n} = Z_m ∩ {h_j > 0} ∩ A, because −c²_j is finite and positive. This equals (⋂ D_{K_{t_n}}) ∩ A, which has the form C ∩ A with C convex.
5. **Generators.** Z_m ⊇ {h_m ≥ 0} by guidance, and Z_m ⊇ D_K a.e. by Lemma T0. So C contains almost every point of the open sets A ∩ {h_m > 0, h_j > 0} and D_K ∩ {h_j > 0}. A convex set containing a dense subset of an open set contains the convex hull of that open set (perturbed-simplex argument). ∎

**Corollary B1 (full domain, n ≥ 3; PROVED).**
- conv[{h_m ≥ 0, h_j > 0} ∪ (D_K ∩ {h_j > 0})] ⊇ {h_j > 0}. The reason is that D_K ∩ {h_j > 0} contains q with q_m < 0 and q_j/(−q_m) arbitrarily small (make a third coordinate large).
- So every veto c_m vanishes off the sure-loss cone {h_m < 0, h_i ≤ 0 ∀i}. Undominated models never accept sure losses.
- So on the models that matter, a VL ranking *is* its level-2 ranking. With (Br), Prop lexbayes plus T0 make the target the Brier minimiser {β·h > 0}: **only precise targets are covered**.
- (With non-Brier level 2 one is in Prop E.)

**Corollary B2 (two-sided U-domain A = U ∪ −U, U = D_{K'}, n ≥ 3; PROVED).**
- conv(A ∩ {h_m > 0, h_j > 0}) = {h_m > 0, h_j > 0}: any gap point z is the midpoint of z ± t·e_k with k ∉ {j, m}, which lie in U and −U.
- So the same collapse holds. Symmetrising the U-domain kills VB.
- NUMERICS (`domains_vb.out`): VB-type minimisers are incoherent in 24/42 random lex-Bayes trials on U ∪ −U, and in 29/42 on the full domain. With the full-domain veto 1[h_m<0][−v_m·h]_+, the family X_t of Thm B is visibly non-convex for every t tested, and its hull fills {h_j > 0} as t grows (`full_domain_veto.out`).

**Corollary B3 (where two-sidedness is fatal; PROVED).** Take K a radial simplex (§6) such as T1, n ≥ 3, and (VL)+(Br). Take A with (LF) at D_K (A ⊇ a neighbourhood of ∂D_K ∖ 0), D_K undominated, and every undominated model coherent. Let β be the target's lex weight (by T0, W0 = all worlds). Then for every k with β ∉ ℝ₊v_k and every j ≠ k:

  A ∩ {h_k > 0, h_j > 0} ⊆ {v_k·h ≥ 0}  (a.e.).

*Proof.*
- Suppose g ∈ int A has g_k, g_j > 0 and v_k·g < 0.
- Let r lie on the single-negative part of F_k (r_k < 0 < r_i for i ≠ k). For q ∈ D_K near r and small λ > 0, z = q + λg lies just beyond F_k, near r, inside A (by (LF)), in Z_i for every i ≠ k, and in the hull of Theorem B. So c_k(z) = 0 on an open set accumulating at r.
- The target minimises Σβ_i b_i over ⋂Z_i ∩ A, so it must accept such z wherever β·z > 0.
- β ∈ cone K, and r exposes only v_k, so β·r > 0 unless β ∝ v_k. Then D_K is not a minimiser, a contradiction. ∎

Since β is proportional to at most one v_k, the condition binds at all facets but one. **This is the exact sense in which "visible from the domain" replaces "visible from a world"**: an available gamble that is correct at k and at another world must not lie beyond F_k.

## 5. Prop E: what is left on the full domain is the CPM realisation problem (PROVED)

**Prop E.** Full domain, (Int), and every world's first level strictly sign-correct. Write c_j(h) = −ρ_j(h)·h_j with ρ_j > 0. For a.e. α ∈ Δ the Bayes set
 X_α = {h : (α⊙ρ(h))·h > 0, and accepting h beats accepting −h}
is the a.e.-unique minimiser of Σα_j a_j, hence undominated. So U_L ⊆ C requires **X_α to be coherent for a.e. prior α**. The target must be a (possibly tied) minimiser for some α.

*Proof.* Uniqueness holds for a.e. α by Fubini on {(α, h) : α·c(h) = 0 or α·(c(h) − c(−h)) = 0}. Every h-slice is a null hyperplane in α, because c(h) ≠ 0 and c(h) − c(−h) ≠ 0 a.e. Contradictions cost strictly more than both single acceptances. The converse argument gives undominatedness. ∎

This is precisely "h-dependent local priors α⊙ρ(h) whose Bayes acts are coherent for every prior", the CPM realisation problem the brief excludes. By Theorem A, its convex instances give boxes only.

**Classes on the full domain, summarised.**
- Convex first levels (signed or not): boxes only.
- Any-shape vetoes with (L2): vetoes collapse; with Brier, precise only.
- Strictly guiding first levels: CPM.

Not covered (§8): mixed classes (some worlds' first levels are vetoes, others are signed), signed first levels with flat regions, non-lexicographic or incomplete world orders, and non-integral (IB) rankings.

## 6. Theorem D: radial simplices, including T1 and all interior ε-contaminations, are covered on a maximal two-sided domain (PROVED)

**Class.** p ∈ int Δ, ε_i ∈ (0,1), v_i = (1−ε_i)p + ε_i e_i, K = conv{v_1,…,v_n}. T1 is the case p = u with all ε_i equal. Equal ε_i give every interior ε-contamination, in any number of worlds. D_K = {h : v_i·h > 0 ∀i}.

**Domain.** A_K = {h : #{k : h_k > 0} ≤ 1, or v_k·h ≥ 0 for every k with h_k > 0}. Models are all measurable X ⊆ A_K. A_K ⊇ U = D_{K'} for every K' ⊆ K. The ranking does not use K'.

**Ranking (advice-indexed veto–Brier, AVB).** At world m, on a pair s:
- level 1: φ_m(h) = 1[h_m < 0]·[−v_m·h]_+ for an accepted h, so it charges only *wrong* acceptances; a contradiction is charged its wrong half;
- level 2: correct −|s_m|, silent 0, wrong +|s_m|, contradiction 2|s_m|.

**Theorem D.** AVB on M_{A_K} has the following properties:
- (i) strict (G) and (IB);
- (ii) a convex compact score range, so every model is weakly dominated by an undominated model;
- (iii) every undominated model is coherent, namely X* = A_K ∩ D_{K*} a.e., where K* = ν-conv({β + Σ_{m∈M'} α_m v_m : M' ⊆ M} ∪ {v_i : i ∈ W0, if |W0| ≥ 2});
- (iv) D_K is undominated;
- (v) direct (C);
- (vi) (LF) at D_K;
- (vii) A_K is two-sided on an open neighbourhood of the single-negative part of every facet of ∂D_K.

Hence (W) and U_L = C_L. **The target is covered on a decomposable two-sided domain.**

*Proof.*
- **(i)** Lexicographically: correct (0, −) < silent (0, 0) < wrong (φ ≥ 0, +) < contradiction (φ, 2|s_m|). Both levels are integrals.
- **(ii)** There are 2n integrable coordinates (φ_m ≤ |h|). Lyapunov and Lemma zorn apply.
- **(iii)** The vacuous model zeroes level 1, so Prop lexbayes applies: X* minimises J = Σ_{W0} β_i b_i + Σ_M α_m a_m over the face ⋂_{W0} Z_i, with Z_i = {φ_i = 0}. Pointwise, accept h iff h ∈ A_K ∩ ⋂_{W0} Z_i and G(h) := β·h − Σ_M α_m φ_m(h) > 0. The −h option and contradiction lose, because G(h) > 0 ⇒ β·h > 0 ⇒ G(−h) < 0. The minimiser is unique, since {G = 0} is null: G is piecewise linear with nonzero non-negative gradients. Now split A_K.
  - *(a) ≥ 2 positive coordinates.* If h_m > 0 then v_m·h ≥ 0 by definition of A_K, so φ_m(h) = [−v_m·h]_+ for every m, and Z_i = {v_i·h ≥ 0}. So X* = {β·h + Σ_M α_m min(v_m·h, 0) > 0, v_i·h ≥ 0 (i ∈ W0)} = D_{K*} here. When W0 = {k} the v_k constraint is redundant: G > 0 forces h_k > 0, and then v_k·h ≥ 0 in A_K.
  - *(b) Exactly one positive coordinate k* (P1_k). If G(h) > 0 then β·h > 0, so k ∈ supp β ⊆ W0. Hence k ∉ M, and the indicator in φ_k never enters G. The only difference from D_{K*} is the constraint v_k·h ≥ 0, which X* omits.
    - **Lemma D1.** If |W0| ≥ 2, some i ∈ W0∖{k} has h_i < 0 and v_i·h ≥ 0. Then (1−ε_i)p·h ≥ −ε_i h_i > 0, so p·h > 0, so v_k·h = (1−ε_k)p·h + ε_k h_k > 0. The omitted constraint is implied.
    - If W0 = {k}, K* omits v_k as well.
  - *(c) No positive coordinate.* Neither set accepts (β·h ≤ 0, and every point of K* is ≥ 0).
- **(iv)** If Y weakly dominates D_K then a_i(Y) = 0 at every i, so Y ⊆ ⋂ Z_i a.e. If h ∈ ⋂ Z_i has some h_i < 0, Lemma D1's computation gives p·h > 0 and all v·h ≥ 0, so ⋂ Z_i ⊆ cl D_K. Then Σ p_i b_i(Y) > Σ p_i b_i(D_K) for any non-null omission, so some world strictly prefers D_K.
- **(v)** A tie at every world with an undominated model gives the same score vector, the same face and the same J, so equality a.e. follows from uniqueness.
- **(vi)** Let r ∈ ∂D_K ∖ 0 and let v_i·r = 0. If r_i ≥ 0 the constraints force r = 0. So r_i < 0 and p·r > 0, hence v_k·r > 0 at every k with r_k ≥ 0. So a neighbourhood of r satisfies A_K's condition at every coordinate that can be positive nearby.
- **(vii)** If h is near the single-negative part of F_i (h_i < 0 < h_k for k ≠ i, v_k·h > 0), then h ∈ A_K and −h has exactly one positive coordinate. ∎

**CHECKED / NUMERICS.**
- `contamination_Aeps.out`: the identity X* = A_K ∩ D_{K*} gave 0 mismatches over 60 random (W0, β, α) × 2·10⁵ Gaussian gambles, for n = 3, 4, 5, 6 with random p and ε, and the target-protection inclusion gave 0 violations. The two-sided fraction of gambles is 0.44–0.98.
- `domains_vb_big.out`: an independent convex-hull coherence test (no formula assumed) gave 0/280 incoherent minimisers on A_max = A_{T1}, and 0/280 on U ∪ P1, at s = 0.5 and 0.9.

**Maximality.**
- By Cor B3, any domain on which a (VL)+(Br) ranking covers K must satisfy A ∩ {h_k > 0, h_j > 0} ⊆ {v_k·h ≥ 0} at all facets but one. Off sure losses, this is exactly A_K's defining condition. So **A_K is the largest such domain, up to one exempt facet**.
- The natural one-exempt-facet design (world 3 pure Brier, domain relaxed at facet 3) has incoherent minimisers in 27/280 trials, and its target-protection inclusion fails (`exempt_facet.out`).
- CONJECTURE: no exempt-facet design works, so A_K is exactly maximal.

**Two-sidedness that is impossible.** For n = 3, on the outer arcs of F_i (one positive coordinate k, h_i < h_j < 0) the reflected gamble −h has positive coordinates i and j with v_j·(−h) < 0. Cor B3 forbids making it available at two facets. So for veto-led rankings, *two-sidedness on the outer arcs is excluded*, and on the middle arcs it is achieved.

## 7. What replaces vetoes on two-sided domains

- **Gamble-indexed vetoes** (VB: φ(h) = [−v·h]_+) charge acceptances that are correct at the vetoing world as soon as the domain contains h with h_m > 0 and v_m·h < 0. That violates (G).
- **Advice-indexed vetoes** (1[h_m < 0]·[−v_m·h]_+) respect (G) on every domain. But their zero sets are unions of half-spaces, so lex-Bayes minimisers are non-convex, hence incoherent, whenever the domain contains two-positive gambles beyond a facet (Thm B).
- The cure is to **remove exactly those gambles** and nothing else. On what remains, the indicator acts only on one-positive gambles. There Lemma D1 shows it is invisible: a minimiser that accepts a one-positive gamble must avoid some *other* world's veto, and that already places the gamble inside the facet.
- So the replacement is "advice-indexed vetoes plus a domain cut by facet visibility". On the full domain there is no replacement of veto type (Cor B1). Signed leading levels lead to boxes (convex case) or to CPM (Prop E).

## 8. Open points and conjectures

1. **General auditor class on A-type domains (CONJECTURE).** For K = conv(K' ∪ ⋃A_i), the argument needs Lemma D1 in the form: h ∈ P1_k and φ_i(h) = 0 with h_i < 0 ⇒ φ_k-constraint holds. This holds when the A_i lie on rays from a common point p, which is §6. For general K', a domain smaller than A_K may be needed.
2. **Mixed classes.** If some worlds have signed (strictly guiding) first levels and others vetoes, the X_t family of Thm B still gives convex zero-set slices Z_m ∩ {h_j > 0} ∩ A. But Lemma T0 (which uses the vacuous model) is unavailable. So the D_K generator is missing, and the full-domain collapse is not proved. CONJECTURE: the collapse still holds for targets in relint Δ.
3. **Non-lexicographic, incomplete or infinitely-many-statistics rankings on the full domain:** untouched here. Theorem A needs only (Ref), so it already covers incomplete world orders that refine a convex additive charge.
4. **Exempt facet:** see §6.

## 9. Status

| Result | Status |
|---|---|
| Thm A: worlds refining convex first levels on the full domain ⇒ undominated D_K (e_j ∉ K) is a normalised box | PROVED |
| Cor A1: T1 and ε-contaminations (n ≥ 3) are not boxes ⇒ not covered by that class | PROVED |
| Lemma T0: under (VL), a target in relint Δ pays no veto (S3 made rigorous) | PROVED |
| Thm B: under (VL)+(L2) with undominated ⇒ coherent, veto zero-set slices are convex and contain the hull of guidance zone ∪ target | PROVED |
| Cor B1: full domain (n ≥ 3), vetoes vanish off sure losses; with Brier, only precise targets | PROVED; NUMERICS illustrate |
| Cor B2: U ∪ −U collapses likewise | PROVED; NUMERICS (24/42 incoherent) |
| Cor B3: exact domain condition A ∩ {h_k>0, h_j>0} ⊆ {v_k·h ≥ 0} at all facets but one | PROVED |
| Prop E: strictly guiding first levels on the full domain ⇒ CPM realisation condition | PROVED |
| **Thm D: radial simplices (T1, all interior ε-contaminations, any n) covered on the two-sided domain A_K by AVB, with every criterion** | **PROVED**; identity and hull tests CHECKED numerically (0 failures) |
| A_K maximal for (VL)+(Br) up to one exempt facet | PROVED; exact maximality CONJECTURE (exempt design fails, NUMERICS) |
| Outer arcs cannot be made two-sided for veto-led rankings (at ≥ 2 facets) | PROVED (Cor B3) |
| Extension of Thm D to the auditor's general class | CONJECTURE |
| Mixed and non-lexicographic classes on the full domain | open |

**Referee priorities.**
1. Thm D(iii): the case split, and Lemma D1 when W0 = {k}.
2. Thm B steps 3–5: undominatedness of X_t with more than two levels, and the dense-subset hull step.
3. Thm A step 3: the directional-derivative reduction for non-homogeneous convex levels.
4. Cor B3: the exposure argument (β·r > 0 unless β ∝ v_k).
