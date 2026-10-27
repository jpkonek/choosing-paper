# Dominance in the veto–Brier ranking without closed choice (25 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. **Refereed once (25 Oct): Steps 0–3 CORRECT; Remark 1 CHECKED numerically; Remark 3 doubtful as stated (see below).** Referee scripts: scratch `vbref/vb_check*.py`. Notation as in L3 (`decomposable-domains-2026-10-12/L3_notes.md`, §3).

## Setting (L3 §3, unchanged)
- Three worlds. U = D_{K'} with u ∈ K' ⊆ relint T1. Models: measurable X ⊆ U, modulo μ-null sets (μ Gaussian, so non-atomic). M_U is decomposable, and (LF) holds at T1 with N = U.
- Vetoed region: V_m := U ∩ {v_m·h < 0} ⊆ {h_m < 0}. Put φ_m(h) := −v_m·h on V_m and 0 elsewhere, so φ_m ≥ 0.
- Level 0: a_m(X) := Φ_m(X) = ∫_X φ_m dμ.
- Level 1: Ψ_m(X) = ∫_{E_m(X)} |h_m| dμ = c_m + b_m(X), where c_m := ∫_{U∩{h_m>0}} h_m dμ and b_m(X) := −∫_X h_m dμ.
- VB: X ⪯_m Y iff (a_m(X), b_m(X)) ≤_lex (a_m(Y), b_m(Y)). Each ⪯_m is a total preorder (in particular transitive).
- L3 Thm 3.3 (refereed per the T1 status map; the L3 note itself predates the referee): VB satisfies strict (G), (IB), (LA), (LF) at T1 and direct (C), and T1 ∈ C_L. It fails (S), and by L3 Thm 3.4 no selection whatever has closed sections.

## Theorem VB (PROVED; refereed once)
Here C_L means the coherent undominated models, C ∩ U_L, as in Loss Dominance Generalized v3 (LA). It does not mean that every coherent model in M_U is undominated: that is false for VB (U itself, and D_K for K a small disc about u, are dominated).

In VB on M_U:
- (a) every model is weakly dominated by an undominated model;
- (b) every undominated model is coherent; explicitly, it is U ∩ ⋂_{w∈W} {w·h > 0} a.e., for a finite set W of nonzero vectors with non-negative coordinates;
- (c) hence, with (LA) and (C): U_L = C_L, and every model outside C_L is dominated by a member of C_L.

So VB satisfies the full dominance conclusion. With L3 Thm 3.3, **T1 is covered on M_U under strict (G), (IB), (LA), (LF), (C) and the dominance conclusion. (S) fails, but (S) was only a sufficient condition for that conclusion.**

## Proof

**Step 0: the range is convex and compact.** Let z(X) := (a_1, a_2, a_3, b_1, b_2, b_3)(X) ∈ ℝ⁶, and Z := {z(X) : X ∈ M_U}.
- Each a_m and b_m is X ↦ ∫_X f dμ for an integrable f: |φ_m| ≤ |h| and |h_m| ≤ |h|, and |h| is μ-integrable.
- μ restricted to U is non-atomic. By Lyapunov's theorem, Z is convex and compact.
- VB's orders depend on X only through z(X). Write z ⪯ z' when z ⪯_m z' at every m.

**Step 1 (a): existence by Zorn.** Fix X and z := z(X). Let D := {z' ∈ Z : z' ⪯ z}.
- Let 𝒞 ⊆ D be a chain. Along 𝒞, each a_m is monotone (z' ⪯ z'' ⇒ a_m(z') ≤ a_m(z'')).
- Let z^∞ be a cluster point of 𝒞, viewed as a decreasing net, in the compact set Z.
- Fix m and γ ∈ 𝒞.
  - If inf_𝒞 a_m is not attained, then a_m(z^∞) = inf < a_m(z^γ).
  - If it is attained, then on the tail where a_m equals the infimum, b_m is non-increasing. So b_m(z^∞) ≤ b_m(z^γ) for every γ in that tail, and a_m(z^γ) is larger than the infimum for every γ outside it.
  - Either way z^∞ ⪯_m z^γ.
- So z^∞ ∈ D is a lower bound for 𝒞. By Zorn's lemma (for preorders), D has a minimal element z*.
- If z' dominated z*, then z' ⪯ z* ⪯ z would put z' in D, contradicting minimality. So z* is undominated in Z. Any model realising z* is an undominated model weakly dominating X.

**Step 2 (b): undominated implies coherent.** Let X* be undominated, z* = z(X*), and W0 := {m : a_m(z*) = 0}.
- Let Z' := {z ∈ Z : a_m(z) = 0 for m ∈ W0}. This is convex and compact, and it is the range over the models X ⊆ N(W0) := ⋂_{m∈W0}{v_m·h ≥ 0} (a.e.).
- **Coordinates.** On Z' use y := ((b_m)_{m∈W0}, (a_m, b_m)_{m∉W0}). Let P° := {d : d_{b_m} < 0 for m ∈ W0, and d_{a_m} < 0 for m ∉ W0}. This is a non-empty open convex cone.
- **Disjointness.** If z ∈ Z' had y(z) − y(z*) ∈ P°, then z would be strictly better than z* at every world:
  - for m ∈ W0, a_m is equal (0) and b_m is strictly smaller;
  - for m ∉ W0, a_m is strictly smaller.
  
  That contradicts undominatedness. So y(Z') − y(z*) and P° are disjoint convex sets, one of them open.
- **Separation.** There is λ ≠ 0 with:
  - λ·d ≤ 0 on P°, hence on its closure;
  - λ·(y(z) − y(z*)) ≥ 0 on Z'.
- **Signs of λ.** The closure of P° is {d_{b_m} ≤ 0 (m ∈ W0), d_{a_m} ≤ 0 (m ∉ W0), d_{b_m} free (m ∉ W0)}. So:
  - β_m := λ_{b_m} ≥ 0 for m ∈ W0;
  - α_m := λ_{a_m} ≥ 0 for m ∉ W0;
  - λ_{b_m} = 0 for m ∉ W0.
  
  Hence z* minimises J := Σ_{m∈W0} β_m b_m + Σ_{m∉W0} α_m a_m over Z'.
- **β ≠ 0.** Suppose β = 0. Then α ≠ 0. T1 ∈ M_U avoids every V_m, so z(T1) ∈ Z' and J(z(T1)) = 0. Since J ≥ 0 on Z', J(z*) = 0, so a_m(z*) = 0 for m ∈ supp α ⊆ complement of W0. That contradicts the definition of W0. (This also shows W0 ≠ ∅.)
- **The integrand.** For X ⊆ N(W0) we have J(X) = ∫_X g dμ, with
  g := Σ_{m∉W0} α_m φ_m − Σ_{m∈W0} β_m h_m.
  Extend β by 0 outside W0. On each region where the set A := {m ∉ W0 : v_m·h < 0} is fixed, g = −(β + Σ_{m∈A} α_m v_m)·h. That vector has non-negative coordinates and is non-zero because β ≠ 0. So {g = 0} is μ-null.
- **The minimiser.** The minimisers of X ↦ ∫_X g over X ⊆ N(W0) ∩ U are therefore unique a.e.:
  X* = N(W0) ∩ U ∩ {g < 0}.
- **It is coherent.**
  - g(h) < 0 ⟺ β·h + Σ_{m∉W0} α_m min(v_m·h, 0) > 0 ⟺ (β + Σ_{m∈M} α_m v_m)·h > 0 for every M ⊆ complement of W0.
  - Each N(W0)-constraint v_m·h ≥ 0 agrees a.e. with v_m·h > 0.
  - So X* = U ∩ ⋂_{w∈W}{w·h > 0} a.e., with W := {β + Σ_{m∈M} α_m v_m : M} ∪ {v_m : m ∈ W0}, all non-negative and non-zero.
  - This is D_K ∩ U = D_{conv(K ∪ K′)} for K the normalised convex hull of W, a coherent model in M_U.

**Step 3 (c).** By (a) and (b), every model is weakly dominated by an undominated coherent model, that is, by a member of C_L ((LA)). For m ∉ C_L with weak dominator c ∈ C_L, direct (C) (L3 Thm 3.3(b)) rules out m ≈ c, so c dominates m. Every undominated model is coherent, so U_L ⊆ C ∩ U_L = C_L ⊆ U_L. ∎

## Remarks
1. **Why closed choice failed but dominance holds.** The weak dominators of the rivals that break VB's sections are coherent models that are not in VB's selection. Example: the rival X = C_{e_j} ∖ A of L3 Thm 3.3(c) is weakly dominated by D_K ∩ U with K = conv(K′ ∪ {e_j, w}), where w ∝ v_i + τ e_j (a Neyman–Pearson cut of the veto region). CHECKED by hand for A inside V_i ∩ {h_k > 0}, after adding a small cut of V_k to secure world k.
2. **The route is the classical one, without randomisation.** Admissible (undominated) implies lexicographic Bayes implies coherent. Convexity comes from non-atomic splicing (Lyapunov), not from mixing models. Nothing is assumed beyond VB's own definition, the domain M_U, and L3 Thm 3.3.
3. **Generalisation (CONJECTURE; the referee judges the stated form doubtful).** The two-level argument needs a model zeroing every leading level at once. Without it, separation may put all its weight on leading levels, ties become non-null, and a nested separation is needed whose later weights attach to worlds optimal only within a face. The version in LDG v3.1 (Prop. lexbayes) keeps that hypothesis and two levels. Original wording: The same proof should give: on a non-atomic decomposable domain, for any ranking whose world orders are lexicographic in finitely many integral scores, (a) every model is weakly dominated by an undominated model, and (b) undominated models minimise lexicographic weightings of the scores in which later levels appear only at worlds whose earlier levels are already optimal. Coherence of those minimisers is then a check on the integrands.
4. **Wrong-first worlds.** L3.6(b) lives on two-sided domains; Step 2 uses one-sided structure, so this proof does not cover them (referee).
5. **Domain.** This is the one-sided U-domain M_U, which has (LF) at T1. The full four-advice domain is not addressed.

## Additions from the referee (PROVED)
- **Exact characterisation.** Conversely, every a.e.-unique minimiser of J over models inside N(W0), for any non-empty W0, β ≥ 0 non-zero and α ≥ 0, is undominated. So U_L is exactly this polyhedral lexicographic-Bayes family. VB's selected models C_p are the members with W0 = supp p and β = p.
- **(C) without the vector-uniqueness lemma.** A weak dominator that does not dominate is tied at every world, so has the same six numbers; Step 2's uniqueness then makes the models equal a.e.
- W0 ≠ ∅ directly: if every a_m(X) > 0, D_{T1} strictly dominates X.

## Points for the author
- Whether the U-domain M_U suffices, or the full four-advice domain is required.
- VB is lexicographic in its rankings (not in priors), with three worlds.
- C_L contains models tangent to ∂U (e.g. C_{e_j}); under the 12 Oct decision, non-cheapness is required only at the target ((LF) at T1), which holds.
