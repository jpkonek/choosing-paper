# P61 — PROVER: a general covering theorem for coherent sets of desirable gambles via veto–Brier rankings

25 October 2026. Labels: PROVED (proved here, not yet refereed) / CHECKED / CONJECTURE / NUMERICS.
Scripts: `r61/p61py/` (`vis_check.py`, `vb_general_sim.py`, `smooth_depth.py`, `tangent_example.py`, each with a `.out` file).

## 0. Outcome

1. **The auditor's theorem is correct (Thm A, PROVED).** I re-proved every step. Two steps came out shorter than in the audit:
   - Null boundaries: both kinds of null set follow from one fact. The relevant functions are strictly monotone along the direction **1** = (1,…,1), so Fubini makes their zero sets null. No polyhedrality is needed and no "full-dimensional cone" argument.
   - (C): a model tied with an undominated model has the same score vector, so it is itself undominated, and therefore coherent by part (b).
2. **A sharper theorem in the same paradigm (Thm B, PROVED).** For a veto–Brier ranking VB(K′,A), the undominated models are *exactly* the a.e.-unique minimisers X\*(W0,β,α). Every one of them with (LF) is a covered target. With W0 = all worlds this gives **one free extreme point**: K = conv(K′ ∪ ⋃A_i ∪ {p}) is covered for *any* p ∈ Δ, including p on ∂Δ. (The VB selections C_p = D_{conv(T1∪{p})} of L3 are the special case.) Rem. B′: replacing the vetoes by arbitrary sublinear vetoes adds no targets.
3. **Geometry (Thm V, PROVED).** The auditor's condition is equivalent to *uniform visibility* of the extreme points. Pointwise visibility has an exact normal-cone form: v ≠ e_j is visible from j iff **every nonzero h ∈ F_v has h_j < 0**.
   - Lead's S1 needs the strict inequality. With "F_v ⊆ {h_j ≤ 0}" it is false (a tangent ray: `tangent_example.out`).
   - The auditor's class equals pointwise visibility of cl(ext K) away from vertices of Δ, plus one condition: no vertex e_i ∈ K is a limit of other extreme points.
   - For polytopes the class is exactly "every vertex is visible or is a vertex of Δ".
   - For K ⊆ relint Δ, the targets of VB-type rankings are exactly the K in which **all but at most one** extreme point is uniformly visible (Cor V6).
4. **Inside the class (PROVED):**
   - interior ε-contaminations (any n);
   - total-variation balls in relint Δ (any n);
   - belief functions with m(Ω) > 0 and positive singleton masses (any n);
   - strictly 2-monotone lower probabilities with positive singletons (any n), which includes constant-odds-ratio and all strictly convex distortion models;
   - smooth K ⊆ relint Δ (discs, ellipsoids, KL balls, outer parallel bodies);
   - all full-dimensional K when n = 2;
   - probability intervals whose vertices have at most one coordinate at its upper bound (all generic hexagons when n = 3).
5. **Outside the class (PROVED):**
   - pari-mutuel models (n ≥ 3), every vertex. **The reversed triangle is the pari-mutuel model with p uniform and δ = 1/5.**
   - normalised boxes, i.e. density-ratio classes (n ≥ 3, at least 3 bad vertices);
   - ε-contaminations whose p has a zero coordinate (n ≥ 3);
   - every lower-dimensional K, including precise models: these cannot be targets on *any* one-sided domain with (LF), for any ranking (Prop D1).
6. **Nearby results for the reversed triangle (PROVED).** Each of the following is covered:
   - the hexagons {1/5+η ≤ m_i ≤ 2/5}, at Hausdorff distance ≈ 1.22η;
   - the outer parallel bodies;
   - conv(hexagon_η ∪ {v_1}), which restores one exact vertex.

   The reversed triangle itself is excluded from **every** two-level veto–Brier ranking on every convex one-sided domain (Cor V7). Whether some other ranking covers it is O61's and E61's question.

---

## 1. Setting and hypotheses (all named)

- (H1) There are finitely many worlds Ω = {1,…,n}, with n ≥ 2. Δ is the simplex, e_i its vertices, **1** = (1,…,1), and aff Δ = {m : **1**·m = 1}.
- (H2) μ is a finite measure on ℝⁿ, absolutely continuous with respect to Lebesgue measure, with ∫|h| dμ < ∞. Gaussian μ satisfies this. Models are taken modulo μ-null sets.
- (H3) K ⊆ Δ is compact and convex. In §§2–4, K is also *full-dimensional*: aff K = aff Δ.
  - D_S := {h : m·h > 0 for every m ∈ S}.
  - cl D_K = {h : m·h ≥ 0 on K}.
  - F_x := {h ∈ cl D_K : x·h = 0} for x ∈ K. This is the face of cl D_K exposed by x, equivalently the normal cone of K at x written as gambles.
- (H4) The domain is M_U: all measurable X ⊆ U, where U = D_{K′} and K′ is nonempty, compact and convex.
  - At a problem {h,−h} with h ∈ U, a model either accepts h (h ∈ X) or is silent.
  - At world i, accepting h is correct if h_i > 0 and wrong if h_i < 0. The case h_i = 0 is μ-null.
  - U ∩ (−U) = ∅, so the domain is one-sided.
  - M_U is decomposable: it is closed under splicing (X∩S) ∪ (Y∖S), and under limits in measure, since μ(X∖U) ≤ μ(XΔX_k) → 0.
- Axioms checked:
  - **Strict (G).** If X is at least as good as Y at world i pointwise, and strictly better on a non-null set, then X ≺_i Y. On M_U this means X ⊇ Y on {h_i > 0}, X ⊆ Y on {h_i < 0}, and XΔY non-null.
  - **(IB).** If X,Y agree off S, and X′,Y′ agree with X,Y respectively on S and with each other off S, then X ⪯_i Y ⇔ X′ ⪯_i Y′.
  - **Transitivity.**
  - **(LA), (C)** and the dominance conclusion (W), as in LDG v3.1 §2.
  - **(LF) at D_K.** There is an open N ⊇ ∂D_K∖{0} such that every measurable X with XΔD_K ⊆ N lies in the domain.

**The ranking VB(K′,A).** Let A = (A_1,…,A_n), with each A_i ⊆ conv(K′ ∪ {e_i}) compact; empty sets are allowed. Put

  φ_i(h) := max(0, sup_{v∈A_i} −v·h),  a_i(X) := ∫_X φ_i dμ,  b_i(X) := −∫_X h_i dμ.

Then X ⪯_i Y iff (a_i(X), b_i(X)) ≤_lex (a_i(Y), b_i(Y)). The Brier error at world i is c_i + b_i(X), with c_i a constant.

---

## 2. Theorem A (auditor's theorem; PROVED, every step re-done)

**Theorem A.** Assume (H1)–(H4) and that K is full-dimensional. Assume K′ ⊆ relint K, A_i ⊆ conv(K′ ∪ {e_i}) compact, and K = conv(K′ ∪ A_1 ∪ … ∪ A_n). Then VB(K′,A) on M_U satisfies:
- strict (G), (IB) and transitivity;
- (W), i.e. every model is weakly dominated by a coherent undominated model;
- U_L = C_L, and every incoherent model is dominated by a member of C_L;
- (C), and D_K ∈ C_L;
- (LF) at D_K, with N = U.

**A1. Guidance.**
- Let h ∈ U with h_i ≥ 0, and v ∈ conv(K′ ∪ {e_i}). Write v = (1−t)k + te_i with k ∈ K′ and t ∈ [0,1]; this form exists because K′ is convex. Then v·h = (1−t)k·h + t h_i ≥ 0. So φ_i(h) = 0.
- Hence φ_i > 0 only at i-wrong acceptances.
- Let X improve Y at i. Then X∖Y ⊆ {h_i > 0} a.e., where φ_i = 0, so a_i(X) − a_i(Y) = −∫_{Y∖X} φ_i ≤ 0.
- Also b_i(X) − b_i(Y) = −∫_{X∖Y} h_i + ∫_{Y∖X} h_i < 0. Both integrands are negative a.e. on their sets, and XΔY is non-null.
- So X ≺_i Y lexicographically.

**A2. (IB) and transitivity.**
- a_i(X) − a_i(Y) = ∫_S (1_X − 1_Y) φ_i, and the same holds for b_i. So the differences, and hence the lexicographic comparisons, depend only on the advice on S.
- ≤_lex is a total order on ℝ², so each ⪯_i is a total preorder.

**A3. Integrability.** v ∈ Δ gives |v·h| ≤ max_j |h_j| ≤ |h|. So 0 ≤ φ_i ≤ |h| and |h_i| ≤ |h|, and both are μ-integrable by (H2).

**A4. Lyapunov, with 2n coordinates.**
- z(X) := (a_1,…,a_n, b_1,…,b_n)(X) = ∫_X f dμ, where f : U → ℝ^{2n} is integrable.
- Each coordinate is a finite signed measure absolutely continuous with respect to the non-atomic μ, hence non-atomic.
- Lyapunov's theorem in finite dimension makes Z := z(M_U) convex and compact.
- Only finitely many coordinates are used, as the audit asked.

**A5. Zorn (LDG Lemma 3.11, re-checked).**
- A lexicographic tie at every world is equality of z. So "weakly dominates", restricted to score vectors, is a *partial order* on Z.
- Fix X and put D := {y ∈ Z : y ⪯ z(X)}. Let 𝒞 ⊆ D be a chain, viewed as a net decreasing in ⪯, and let y^∞ ∈ Z be a cluster point; Z is compact.
- Fix ω and γ ∈ 𝒞. Along the chain a_ω is non-increasing, so a_ω(y^∞) = inf_𝒞 a_ω ≤ a_ω(y^γ).
  - If the inequality is strict, then y^∞_ω <_lex y^γ_ω.
  - If it is an equality, every element below y^γ has a_ω = a_ω(y^γ). Along that tail b_ω is non-increasing, and y^∞ lies in the closure of the tail, so b_ω(y^∞) ≤ b_ω(y^γ).
- So y^∞ is a lower bound of 𝒞 in D. Zorn gives a minimal y\* ∈ D.
- A dominator of y\* would lie in D, contradicting minimality. So any model with score y\* is undominated and weakly dominates X.

**A6. Separation (LDG Prop 3.12, re-checked).**
- Every a_ω is ≥ 0. D_K makes every a_ω zero: for h ∈ D_K and v ∈ A_ω ⊆ K we have v·h > 0. So Prop 3.12 applies.
- Let X\* be undominated and W0 := {ω : a_ω(X\*) = 0}. Then W0 ≠ ∅: otherwise D_K strictly dominates X\*.
- There are β ≥ 0, supported on W0 and β ≠ 0, and α_ω ≥ 0 for ω ∉ W0, such that z(X\*) minimises J := Σ_{W0} β_ω b_ω + Σ_{ω∉W0} α_ω a_ω over Z′ := {z ∈ Z : a_ω = 0 for ω ∈ W0}.
- The separating functional of the open cone P° is forced to be ≤ 0 on cl P°. That fixes the signs, and the free b-coordinates off W0 get weight 0.
- β = 0 is impossible. It would give J = Σα a ≥ 0 with J(D_K) = 0, so J(X\*) = 0 and a_ω(X\*) = 0 for some ω ∉ W0 with α_ω > 0, contradicting the definition of W0.
- Z′ is the score range of the models with X ⊆ N(W0) := U ∩ ⋂_{ω∈W0} {φ_ω = 0} a.e., because φ_ω ≥ 0. On those models J(X) = ∫_X g dμ, with

  g(h) := Σ_{ω∉W0} α_ω φ_ω(h) − β·h.

**A7. Uniqueness without polyhedrality.**
- v ≥ 0 and v·**1** = 1 give φ_ω(h + t**1**) = max(0, sup_{A_ω}(−v·h) − t) ≤ φ_ω(h) for t ≥ 0.
- Hence g(h + t**1**) ≤ g(h) − t Σβ, with Σβ > 0.
- g is continuous (a finite combination of convex functions), so {g = 0} is closed. Each line h + ℝ**1** meets it at most once.
- Fubini over **1**^⊥ × ℝ**1** makes it Lebesgue-null, hence μ-null by (H2).
- The minimisers of ∫_X g over X ⊆ N(W0) are exactly the X with N(W0) ∩ {g < 0} ⊆ X ⊆ N(W0) ∩ {g ≤ 0}. So the minimiser is unique a.e.:

  X\* = N(W0) ∩ {g < 0}.

**A8. Coherence.**
- Put B_ω := conv({0} ∪ A_ω). A linear function has the same supremum on a set and on its convex hull, so φ_ω(h) = sup_{v∈B_ω}(−v·h).
- Summing independent suprema gives g(h) = max_{w∈W}(−w·h), where W := {β + Σ_{ω∉W0} α_ω v_ω : v_ω ∈ B_ω}. W is compact, as a continuous image of a product of compacta, so the maximum is attained.
- Hence {g < 0} = D_W.
- Every w ∈ W is ≥ 0 with **1**·w ≥ Σβ > 0. So Ŵ := {w / **1**·w} ⊆ Δ is compact, and D_W = D_Ŵ.
- For ω ∈ W0, {φ_ω = 0} = {h : ψ_ω(h) ≥ 0}, where ψ_ω(h) := min_{A_ω} v·h. Since ψ_ω(h + t**1**) = ψ_ω(h) + t, the set {ψ_ω = 0} is null by the A7 argument. So {φ_ω = 0} = D_{A_ω} a.e.
- Using D_{S1} ∩ D_{S2} = D_{S1∪S2} and D_S = D_{conv S} for compact S:

  **X\* = D_{K\*} a.e., with K\* := conv(K′ ∪ ⋃_{ω∈W0} A_ω ∪ Ŵ).**

  K\* is compact, convex and nonempty, and K\* ⊇ K′, so X\* ∈ M_U is coherent. This also holds when the A_ω are infinite and not polyhedral.

**A9. (W), U_L = C_L, (C).**
- By A5 and A8, every model is weakly dominated by an undominated coherent model, i.e. by a member of C_L. That is (W).
- (C): if m ≈ c ∈ C_L, then z(m) = z(c). Domination depends only on z, so m is undominated, hence coherent by A8, hence m ∈ C ∩ U_L = C_L.
- LDG Prop 2.1(a) then gives U_L = C_L, and every incoherent model is dominated by a member of C_L.

**A10. Target protection.**
- Let Y ⪯ D_K at every world. Then a_i(Y) ≤ 0, so a_i(Y) = 0 for every i. So Y ⊆ N(Ω) = U ∩ ⋂_i D_{A_i} = D_{K′ ∪ ⋃A_i} = D_K a.e., by A8.
- With the a's tied, b_i(Y) ≤ b_i(D_K) for every i. Fix p ∈ K. Then Σ p_i (b_i(Y) − b_i(D_K)) = ∫_{D_K∖Y} p·h dμ, which is > 0 unless D_K∖Y is null.
- So Y = D_K a.e. Every weak dominator of D_K equals it, so D_K ∈ C_L.

**A11. (LF).**
- Let 0 ≠ h ∈ ∂D_K. Then min_K m·h = 0.
- The affine map m ↦ m·h on aff Δ is non-constant. If it were constant, the constant would be 0, and since aff Δ spans ℝⁿ that would force h = 0.
- K is full-dimensional, so a non-constant affine function exceeds its minimum over K at every relative-interior point. So k′·h > 0 for every k′ ∈ K′ ⊆ relint K, i.e. h ∈ U.
- U is open, since K′ is compact. Every measurable change of D_K inside U is a model, so N = U works. ∎

*Converse to A11 (PROVED).* U = D_{K′} ⊇ ∂D_K∖{0} iff K′ ⊆ relint K. If k′ ∈ K′ ∩ rel∂K, a supporting functional at k′, shifted by a multiple of **1**, gives 0 ≠ h ∈ ∂D_K with k′·h = 0.

*Remark (convex U is no restriction; PROVED).* Every open convex cone U ⊇ D_K equals D_{K″} with K″ := C\* ∩ Δ compact, where C = cl U. The reason: int C = {h : y·h > 0 for all y ∈ C\*∖0}, and C\* ⊆ (int ℝⁿ₊)\* = ℝⁿ₊. So convex one-sided domains are exactly the auditor's U = D_{K′}, and (LF) forces K′ ⊆ relint K.

---

## 3. Theorem B: the exact undominated family, and one free extreme point (PROVED)

**Theorem B.** Assume (H1), (H2) and (H4). Let A_i ⊆ conv(K′ ∪ {e_i}) be compact, and put K_0 := conv(K′ ∪ ⋃A_i).
- (a) The undominated models of VB(K′,A) are *exactly* the models X\*(W0,β,α) := N(W0) ∩ {g < 0} = D_{K(W0,β,α)}, with K(W0,β,α) := conv(K′ ∪ ⋃_{ω∈W0} A_ω ∪ Ŵ). Here:
  - W0 ≠ ∅;
  - β ≥ 0, β ≠ 0, supported on W0;
  - α ≥ 0 on Ω∖W0;
  - Ŵ = normalise(β + Σ_{ω∉W0} α_ω B_ω).
- (b) Every conclusion of Thm A except target protection holds for this ranking whatever the target: strict (G), (IB), transitivity, (W), U_L = C_L and (C).
- (c) Let K := K(W0,β,α) be full-dimensional with K′ ⊆ relint K. Then D_K is undominated with (LF), so **K is covered**.
- (d) **One free point.** Let p ∈ Δ be arbitrary, let K := conv(K_0 ∪ {p}) be full-dimensional, and let K′ ⊆ relint K. Then K is covered. Note that K′ need not lie in relint K_0, K_0 need not be full-dimensional, and p may lie on ∂Δ.

*Proof.*
- **(a), "only these".** A6–A8 use only the existence of *some* model with all a_ω = 0. D_{K_0} is one, by the A6 computation with K_0 in place of K.
- **(a), "all these".** Let Y ⪯ X\* at every world.
  - For ω ∈ W0: a_ω(Y) ≤ a_ω(X\*) = 0, so a_ω(Y) = 0. The a's are then tied, so b_ω(Y) ≤ b_ω(X\*).
  - For ω ∉ W0: a_ω(Y) ≤ a_ω(X\*).
  - So Y ⊆ N(W0) a.e., and J(Y) ≤ J(X\*) since the weights are ≥ 0.
  - By A7, X\* is the unique minimiser, so Y = X\* a.e. Hence X\* is undominated.
- **(b)** A1–A9 never use the target.
- **(c)** follows from (a), with (LF) as in A11.
- **(d)** Take W0 = Ω and β = p. Then Ŵ = {p}, and X\* = U ∩ ⋂_i D_{A_i} ∩ {p·h > 0} = D_{conv(K_0∪{p})}. ∎

*Examples.*
- L3's VB is the case A_i = {v_i}. Its selections C_p = D_{conv(T1 ∪ {p})} are all covered targets, including at p = e_j.
- `vb_general_sim.out`: free-point targets conv(hexagon ∪ {(.15,.45,.40)}) and conv(contamination ∪ {(0,.55,.45)}). In both, the added point is not visible from any world.

**Remark B′ (sublinear vetoes give no new targets; PROVED).**
- Let φ_i ≥ 0 be any sublinear (convex, positively homogeneous) veto that vanishes on U ∩ {h_i ≥ 0}.
- Write φ_i(h) = sup_{v∈B_i}(−v·h) with B_i compact convex ∋ 0. This is the support-function form, using φ ≥ 0.
- Vanishing on U ∩ {h_i ≥ 0} means B_i ⊆ (U ∩ {h_i ≥ 0})\* = cone(K′ ∪ {e_i}). The last equality uses the bipolar theorem; the cone is closed because K′ is compact and 0 ∉ K′.
- A7 and A8 go through verbatim with this B_i. The zero set {φ_i = 0} = D_{Â_i} a.e., where Â_i := cl normalise(B_i∖0) ⊆ conv(K′ ∪ {e_i}).
- So the targets are those of VB(K′,Â). The auditor's form is without loss of generality among sublinear vetoes.

---

## 4. Geometry: visibility

**Definition.** x ∈ K is *visible from j* if x = e_j, or if the open ray {x + s(x − e_j) : s > 0} meets relint K. For δ > 0 put K_δ := {k : B(k,δ) ∩ aff Δ ⊆ K}.
- K_δ is compact and convex. For convexity: if k, k′ ∈ K_δ, then λk + (1−λ)k′ + u = λ(k+u) + (1−λ)(k′+u).
- K_δ ⊆ relint K.
- Every compact subset of relint K lies in some K_δ, because the depth function is continuous and positive on relint K.

**Lemma V1 (normal-cone form; PROVED).** Let K be full-dimensional, x ∈ K and x ≠ e_j. Then x is visible from j iff **h_j < 0 for every nonzero h ∈ F_x**.

*Proof.*
- (⇒) Let k = x + s(x − e_j) ∈ relint K with s > 0, and let 0 ≠ h ∈ F_x. Then k·h = (1+s)x·h − s h_j = −s h_j.
  - m ↦ m·h is non-constant on aff Δ (as in A11), has minimum 0 over K, attained at x, and k ∈ relint K. So k·h > 0, i.e. h_j < 0.
- (⇐) Suppose the open ray R misses relint K. Both are convex subsets of aff Δ, and relint K is open there.
  - Separation in aff Δ gives a non-constant affine ℓ with ℓ ≥ c on K and ℓ ≤ c on R. Letting s → 0 on R and using x ∈ K gives ℓ(x) = c.
  - Represent ℓ − c on aff Δ by h ∈ ℝⁿ: an affine a·m + b equals (a + b**1**)·m there. Then h ≠ 0 and h ∈ F_x.
  - On R, (x + s(x−e_j))·h = −s h_j ≤ 0. So h_j ≥ 0. ∎

*Correction to S1.* "F_v ⊆ {h_j ≤ 0}" is strictly weaker than visibility. The extra cases are those where the ray from e_j runs along an edge of K. Example (`tangent_example.out`): K = conv{(.4,.3,.3), (.2,.4,.4), (.45,.45,.1)} at v = (.4,.3,.3). The normals at v are (0,1,−1) and (−1,.90,.43). The weak test holds, but v is not visible from any world, and not in conv(K′ ∪ e_j) for any K′ ⊆ relint K. The strict test is the right one.

**Lemma V2 (stability; PROVED).** Let x = (1−t)k + te_j with k ∈ K_δ and t ∈ [0,1), i.e. x ≠ e_j. Then every y ∈ K with |y − x| < (1−t)δ/2 lies in conv(K_{δ/2} ∪ {e_j}).

*Proof.* Put k_y := (y − te_j)/(1−t). Then |k_y − k| = |y − x|/(1−t) < δ/2, so B(k_y, δ/2) ⊆ B(k, δ) and k_y ∈ K_{δ/2}. Also y = (1−t)k_y + te_j. ∎

**Theorem V (characterisation of the auditor's class; PROVED).** Let K be full-dimensional. The following are equivalent.
- (i) There are K′ and A_i as in Thm A.
- (ii) (UV) There is δ > 0 such that ext K ⊆ ⋃_j conv(K_δ ∪ {e_j}).
- (iii) Both of the following hold:
  - (iii-a) every x ∈ cl(ext K) that is not a vertex of Δ is visible from some j, i.e. by V1 there is j with h_j < 0 on F_x∖0;
  - (iii-b) no vertex e_i ∈ K is an accumulation point of ext K.

*Proof.*
- **(i)⇒(ii).** ext K ⊆ K′ ∪ ⋃A_i (extreme points of the convex hull of a compact set lie in the set), and K′ ∩ ext K = ∅. Also K′ ⊆ K_δ for some δ.
- **(ii)⇒(i).** Put K′ := K_δ and A_j := K ∩ conv(K_δ ∪ {e_j}). By Minkowski, K = conv ext K ⊆ conv(K′ ∪ ⋃A_j) ⊆ K.
- **(ii)⇒(iii).**
  - Take x ∈ cl ext K ⊆ rel∂K with x = lim v_m, v_m ∈ ext K, v_m = (1−t_m)k_m + t_m e_{j_m} and k_m ∈ K_δ.
  - Pass to a subsequence with j_m = j, t_m → t and k_m → k ∈ K_δ.
  - If t = 1 then x = e_j. If t = 0 then x = k ∈ relint K, which is impossible. Otherwise x is visible from j: this is (iii-a).
  - For (iii-b), let v_m → e_i with v_m ≠ e_i. Then the limit is e_i = (1−t)k + te_j. Since k has full support, t = 1 and j = i.
  - So v_m lies in the open segment (k_m, e_i), whose endpoints are both in K. Then v_m is not extreme, a contradiction.
- **(iii)⇒(ii).**
  - Each x ∈ cl ext K that is not a vertex of Δ has, by V2, a relatively open neighbourhood visible from j(x) at depth δ(x)/2.
  - Each vertex e_i ∈ cl ext K is isolated in cl ext K by (iii-b), and lies in conv(K_δ ∪ e_i) for every δ.
  - cl ext K is compact. Take a finite subcover and let δ be the minimum of the depths. ∎

**Corollaries (all PROVED).**
- **V3. Polytopes.** ext K is finite, so (Aud) holds iff every vertex of K is a vertex of Δ or visible. Visibility is checked by the active facet normals h^{(f)} (with m·h^{(f)} ≥ 0 on K, including facets m_k ≥ 0 of Δ): some j has h^{(f)}_j < 0 for every active f. F_v is the cone of these normals, and it is pointed because K is full-dimensional.
- **V4. Smooth K ⊆ relint Δ.** Assume K is full-dimensional with a unique supporting hyperplane at every relative-boundary point.
  - Then F_x = ℝ₊h_x for each x ∈ rel∂K, because affine functionals on aff Δ correspond one-to-one to vectors in ℝⁿ.
  - x has full support and x·h_x = 0, so h_x has a negative coordinate j. By V1, x is visible from j.
  - V2 and compactness of rel∂K give (UV). So K is covered.
  - Examples: Euclidean and elliptical discs, KL balls inside relint Δ, and every outer parallel body (K_0 + rB) ∩ aff Δ ⊆ relint Δ.
- **V5. n = 2.** Every full-dimensional K = [x, y] is covered. The endpoint nearer e_1 is visible from 1 (the ray points into K), or it is e_1 itself.
- **V6. Exact VB-class for K ⊆ relint Δ.** Let K ⊆ relint Δ be full-dimensional. K is a covered target of some VB(K′,A) (equivalently, by B′, of some two-level sublinear-veto–Brier ranking on a convex one-sided domain) **iff there is p ∈ K with ext K∖{p} ⊆ ⋃_j conv(K_δ ∪ {e_j}) for some δ > 0.** In words: all but at most one extreme point is uniformly visible. For polytopes: at most one vertex is not visible.
  - (⇐) By Thm B(d), with K′ = K_δ and A_j = K ∩ conv(K_δ ∪ e_j).
  - (⇒) Let D_K = X\*(W0,β,α). β̂ ∈ Ŵ ⊆ K (take every v_ω = 0) has support supp β ⊆ W0. K ⊆ relint Δ forces W0 = Ω, so Ŵ = {β̂}.
  - So ext K ⊆ K′ ∪ ⋃A_ω ∪ {β̂}, with K′ ∩ ext K = ∅ and K′ ⊆ K_δ.
- **V7. Excluded.**
  - The reversed triangle {m_i ≤ 2/5}. At v_1 = (1/5,2/5,2/5) the normals are (2/5,−3/5,2/5) and (2/5,2/5,−3/5), with no common negative coordinate, and likewise at each vertex. Three bad vertices, and V6 allows at most one, so no VB-type ranking covers it.
  - Pari-mutuel models and normalised boxes are excluded too (§6).

**Remark (CONJECTURE, consistent with S2).** With more veto levels before Brier, the same accounting seems to hold. Every veto level's sets must lie in conv(K′ ∪ e_ω) by guidance (B′). The final Brier weights β must have full support for K ⊆ relint Δ. So V6 should persist for lexicographic sublinear-veto rankings with any number of levels. I have not written the nested-separation proof; that is O61's remit.

---

## 5. Boundary and lower-dimensional targets

**Prop D1 (lower-dimensional K, including precise K = {p}; PROVED, any ranking).** If dim K < n−1, no one-sided domain (all models inside some U with U ∩ −U = ∅) has (LF) at D_K.

*Proof.*
- span K has dimension dim K + 1 < n, so some h ≠ 0 has m·h = 0 for every m ∈ K. Then h and −h both lie in ∂D_K.
- (LF) gives an open N ∋ h, −h. The model D_K ∪ (N ∩ B(h,r)) ∪ (N ∩ B(−h,r)) lies in the domain, so these sets lie in U a.e.
- O := N ∩ B(h,r) ∩ −(N ∩ B(−h,r)) is open, contains h, and has positive Lebesgue measure. For a.e. g ∈ O, both g and −g lie in U, which is impossible. ∎

Precise and other lower-dimensional models therefore need two-sided domains (F61's remit). On one-sided domains, the reachable statement is: every full-dimensional neighbour in the classes of §4 and §6.

**Lemma D2 (convex vetoes cannot cut at boundary points of K; PROVED).**
- Let U be any open cone with ∂D_K∖{0} ⊆ U. Let v ∈ K ∩ ∂Δ, v ≠ e_j. Then some h ∈ U has h_j ≥ 0 and v·h < 0.
- Hence v ∉ (U ∩ {h_j ≥ 0})\*: no sublinear veto at j that vanishes on U ∩ {h_j ≥ 0} has v·h ≥ 0 among its zero-set constraints.

*Proof.* Pick k with v_k = 0. Then e_k ∈ cl D_K∖D_K = ∂D_K, so e_k ∈ U.
- If k = j, pick l ∈ supp v and put h = e_j − η e_l.
- If k ≠ j, pick l ∈ supp v with l ≠ j (possible since v ≠ e_j); then l ≠ k. Put h = e_k − η e_l.

In both cases h_j ≥ 0, v·h = −η v_l < 0, and h ∈ U for small η. ∎

So in Thm A, extreme points of K on ∂Δ must be vertices of Δ. In Thm B such points can also come from Ŵ. Here is what that allows in a concrete class.

**Prop D3 (ε-contaminations with a zero coordinate; PROVED).** Let n ≥ 3, 0 < ε < 1, and let p have exactly one zero coordinate k. Then K = (1−ε)p + εΔ is not the target of any VB(K′,A).

*Proof.*
- The vertices v_i (i ≠ k) are n−1 ≥ 2 distinct points with support exactly Ω∖{k}.
- Generators in the face {m_k = 0}:
  - K′ ⊆ relint Δ contributes none.
  - A_ω ⊆ conv(K′ ∪ e_ω) contributes only e_ω, and e_ω ∉ K.
  - A point of Ŵ in the face needs β_k = 0, and each v_ω equal to 0 or to λe_ω with ω ≠ k. That is because a = (1−t)k′ + te_ω has a_k = 0 iff t = 1, and for ω = k, a_k > 0.
- So the face generators are ν(β + Σ_{ω∈M} α_ω e_ω) with M ⊆ Ω∖(W0 ∪ {k}). Exactly one of them, M = Ω∖(W0 ∪ {k}), has support Ω∖{k}.
- So at most one v_i is generated, a contradiction. ∎

---

## 6. Standard IP classes

**Lemma I0 (lower probabilities; PROVED).** Let P̲ be coherent and K = {m ∈ Δ : m(A) ≥ P̲(A)} full-dimensional. Put h_A := 1_A − P̲(A)**1**.
- Farkas: the normal cone at a vertex v is cone{h_A : A active} + ℝ**1**. Intersecting with {v·h = 0} gives F_v = cone{h_A : A active, ∅ ≠ A ≠ Ω}, where the active A include the facets m_k ≥ 0 when P̲({k}) = 0.
- (h_A)_j < 0 iff j ∉ A and P̲(A) > 0.
- **So a vertex v ≠ e_j is visible from j iff every active proper event A has P̲(A) > 0 and j ∉ A. The vertex is visible iff the active proper events do not cover Ω and all have positive lower probability.**

| Class | In Thm A class? | Proof / check |
|---|---|---|
| ε-contamination, p full support, 0<ε<1 | yes, any n | I0: active events at v_i are the A ∌ i. Also a belief function with m(Ω) = ε. |
| ε-contamination, p with a zero, n ≥ 3 | **no**, not even in the Thm B class | D3 |
| ε = 1 (vacuous) | yes | K′ = {u}, A_i = {e_i} |
| ε = 0 (precise) | **impossible on one-sided domains** | D1 |
| Belief function, m(Ω) > 0, m({k}) > 0 ∀k | yes, any n | I1 |
| Strictly 2-monotone P̲, P̲({k}) > 0 | yes, any n | I2 |
| Constant odds ratio, p full support; any strictly convex distortion f∘p with f > 0 on (0,1] | yes, any n | I2 |
| TV ball {‖m−p‖_TV ≤ δ}, δ < min p_j | yes, any n | I3 |
| Probability intervals [l_i,u_i] ⊆ relint Δ | iff every vertex has ≤ 1 coordinate at its upper bound (Thm B: all vertices but one) | I4 |
| n = 3 generic hexagon PRI | yes | I4 |
| Pari-mutuel u_i = (1+δ)p_i, K ⊆ relint Δ, n ≥ 3 | **no**: every vertex is bad | I5 |
| Normalised boxes / density-ratio classes, n ≥ 3 | **no**: ≥ 3 bad vertices | I6 |
| Smooth K ⊆ relint Δ (discs, KL balls, parallel bodies) | yes | V4 |

**I1 (belief functions).**
- Bel is ∞-monotone, so ext K = {v^σ} (Shapley–Ichiishi).
- v^σ(σ(k)) = Bel(A_k) − Bel(A_{k−1}), where A_k := {σ(1),…,σ(k)}. This assigns each focal mass m(F) to the σ-last element of F.
- So v^σ(A) = Σ_{F : last(F) ∈ A} m(F) ≥ Bel(A).
- If σ(n) ∈ A ≠ Ω, the focal set Ω has last element in A but Ω ⊄ A. With m(Ω) > 0 the inequality is strict.
- So every active proper A omits σ(n), and Bel(A) ≥ Σ_{k∈A} m({k}) > 0. Hence v^σ is visible from σ(n).
- Full-dimensionality: Bel(A) + Bel(A^c) ≤ 1 − m(Ω) < 1.

**I2 (strictly supermodular P̲).** Assume P̲(A∪B) + P̲(A∩B) > P̲(A) + P̲(B) for every non-nested pair A, B, and P̲({k}) > 0.
- For σ(k) ∈ A, the marginal comparison P̲(A_k) − P̲(A_{k−1}) ≥ P̲((A∩A_{k−1}) ∪ σ(k)) − P̲(A∩A_{k−1}) is strict unless A_{k−1} ⊆ A.
- Summing gives v^σ(A) ≥ P̲(A), with equality only if A_{k−1} ⊆ A for every σ(k) ∈ A, i.e. only if A is an initial segment A_k.
- So the active proper events form the chain A_1 ⊂ … ⊂ A_{n−1}, which omits σ(n). Each has positive lower probability by monotonicity. Visible from σ(n).
- Full-dimensionality: take A, A^c, which are non-nested.
- f∘p with f strictly convex, f(0) = 0, f(1) = 1, and p full support is strictly supermodular. For non-nested A, B, put x = p(A∩B), a = p(A∖B) > 0 and b = p(B∖A) > 0; then f(x+a+b) + f(x) > f(x+a) + f(x+b).
- COR: f(x) = (1−δ)x/(1−δx) with 0 < δ < 1.

**I3 (TV).**
- K = p + δ·conv{e_i − e_j}: the slice {Σd = 0, Σ|d| ≤ 2} has extreme points e_i − e_j, since d = Σ_{i,j} d⁺_i d⁻_j (e_i − e_j).
- At v = p + δ(e_i − e_j), the active events are exactly the A ∋ j with A ∌ i. Their union is Ω∖{i}, and P̲(A) ≥ p_j − δ > 0.
- So v is visible from i. This covers every n ≥ 2, not just n = 3.

**I4 (PRI).**
- At a vertex v, let L be the set of coordinates at their lower bounds and H the set at their upper bounds.
- The lower-bound normal for i is e_i − l_i**1**: negative off i, if l_i > 0. The upper-bound normal for i is u_i**1** − e_i: negative only at i.
- So v is visible iff |H| ≤ 1 and all active l_i > 0. (When H = ∅, the free coordinate does the job.)
- n = 3: a generic hexagon has each vertex at one lower bound and one upper bound.

**I5 (PMM).**
- K = {m_i ≤ (1+δ)p_i}. Inside relint Δ, every vertex has n−1 ≥ 2 coordinates at their upper bounds, so by I4 no vertex is visible.
- For n = 3 and p uniform, (1+δ)/3 = 2/5 gives δ = 1/5. **The reversed triangle is this PMM**: 2-monotone, but modular wherever its values are positive.

**I6 (normalised boxes).**
- K = {α_i m_j ≤ β_j m_i}. The normal of constraint (i,j) is β_j e_i − α_i e_j, negative only at j.
- The vertices are ν(w) for box corners w with L, H ≠ ∅. Rank count: |L| + |H| − 1 = n − 1.
- A vertex is visible iff |H| = 1. For n = 3 that gives 3 good and 3 bad vertices.
- Normalised boxes are covered on two-sided domains by L3's box systems, but they are not in this one-sided class.

NUMERICS (`vis_check.out`). Every vertex of every example was tested by the normal-cone test and, independently, by an LP ray test. The two agree everywhere.
- Named classes for n = 3, 4, 5: the bad-vertex counts are reversed triangle 3; PMM 3, 6, 11; boxes 3, 10, 25. Contamination, TV and COR have 0.
- 150 random PRIs per n: the rule "|H| ≤ 1" matches both tests with 0 mismatches. n = 4 PRIs are mostly *outside* (136/150 have ≥ 2 bad vertices).
- Random belief functions with m(Ω) > 0 for n = 3, 4, 5, and random strictly convex distortions for n = 4: 0 bad vertices.
- 1260 vertices of random polygons: 0 disagreements between the tests.
- One early run showed mismatches. They came from P̲({k}) ≈ 1e−11, i.e. tolerance with p ~ Dirichlet(1), and disappear with well-conditioned p.

---

## 7. Nearby covered targets for the reversed triangle (PROVED)

- **N1. Truncations.** K_η := {1/5+η ≤ m_i ≤ 2/5}.
  - For 0 < η ≤ 1/10 it is a hexagon. Each vertex has one coordinate at its upper bound and one at its lower bound, so it is visible by I4.
  - For 1/10 < η < 2/15 it is an interior lower-bound triangle, i.e. an ε-contamination, also covered.
  - Covered, with d_H(K_η, K) = η√(3/2).
  - NUMERICS (`smooth_depth.out`): the uniform depth δ\* ≈ 0.41η, which tends to 0 as η → 0.
- **N2. Outer parallel bodies.** Covered for every r > 0 with K_r ⊆ relint Δ, by V4. NUMERICS: δ\* ≈ 0.05r.
- **N3. One exact vertex.** conv(K_η ∪ {v_1}) is covered by Thm B(d). It agrees with K exactly near v_1, and the other two corners are cut at depth η.

  No VB-type ranking gives two exact vertices (V6).

---

## 8. NUMERICS: simulation of VB(K′,A) (`vb_general_sim.out`)

Setup: n = 3, an empirical Gaussian sample restricted to U, with K′ = c + s(K−c). The A_j were assigned by an LP ray test. Since the measure is atomic, this checks algebra only.

Targets:
- the hexagon PRI {1/4 ≤ m_i ≤ 2/5};
- an interior ε-contamination;
- two free-point targets.

Results:
- guidance violations (φ_j > 0 with h_j ≥ 0): 0;
- target = N(Ω) (∩ {p·h > 0} for free points): 0 mismatches;
- X\*(W0,β,α) = D_{K\*}, the A8 formula including Ŵ, over 40 random (W0,β,α) per target: 0 mismatches;
- dominations of the target among 2000 random perturbations per target, half of them concentrated near ∂D_K: 0.

---

## 9. Status table

| Item | Status |
|---|---|
| Thm A (auditor): G, IB, transitivity, Lyapunov (2n coords), Zorn, separation, uniqueness via **1**-monotonicity, coherence (non-polyhedral), target protection, (C) via score equality, (LF) | PROVED |
| (LF) on M_U ⇔ K′ ⊆ relint K; convex one-sided U ⇔ U = D_{K′} | PROVED |
| Thm B: U_L(VB(K′,A)) = {X\*(W0,β,α)} exactly; every such member with (LF) is a covered target | PROVED |
| Thm B(d): one free extreme point p ∈ Δ (including ∂Δ) | PROVED; NUMERICS |
| Rem B′: sublinear vetoes add no targets | PROVED |
| Lemma V1: visibility ⇔ h_j < 0 on F_x∖0 (strict); S1's weak form is false | PROVED; NUMERICS (counterexample) |
| Thm V: auditor class ⇔ uniform visibility ⇔ (cl ext K visible off Δ-vertices, and no Δ-vertex in K is an accumulation point of ext K) | PROVED |
| V3 polytopes; V4 smooth K ⊆ relint Δ; V5 n = 2 | PROVED |
| V6: K ⊆ relint Δ is a VB-type target ⇔ all but ≤ 1 extreme point uniformly visible | PROVED |
| V7: reversed triangle, PMMs and normalised boxes (n ≥ 3) not covered by any two-level sublinear-veto–Brier ranking on a convex one-sided domain | PROVED |
| Same for multi-level veto rankings | CONJECTURE (O61) |
| D1: lower-dimensional / precise K impossible on any one-sided domain with (LF) | PROVED |
| D2: convex vetoes cannot cut at points of K ∩ ∂Δ; D3: contaminations with p_k = 0 excluded | PROVED |
| IP classes (table §6): contamination, TV, belief (m(Ω) > 0), strictly 2-monotone, COR / strictly convex distortions, PRI rule, smooth: in; PMM, boxes: out | PROVED; NUMERICS |
| Nearby: truncations, parallel bodies, one exact vertex | PROVED; NUMERICS (depths) |

**Hypotheses used:** (H1)–(H4) and full-dimensionality of K. For coherence only H2 is needed: absolute continuity plus a finite first moment. Nothing from (S), (B), selections, Bayes-index matching or closed sections is used.
