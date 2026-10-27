# C1 (round 15, BRIEF14). Glued credal worlds: the dichotomy, and why the design is dead

15 Oct 2026. Labels: **PROVED** (full proof here), **CHECKED** (verified; proof sketched or resting on a cited
result), **CONJECTURE**, **NUMERICS** (scripts in `c1py/`, run with `python3 -I`; no proof depends on them).
Notation as in B1_notes.md and write-up §8.5: P_i, E_i(X) = X △ P_i, M, N_+, R_ij = Q_i ∪ Q_j, the link class
Q_i = R_ij ∩ R_ik (non-null), regular models (error sets ⊆ M). Throughout, {i, j, k} = {1, 2, 3} and world i
is fixed. The round-10 note that previously occupied this file is kept unchanged at the end (Archive).

---

## 0. Outcome

**The glued credal design is dead, and the dichotomy of task (1) is settled: a glued world either collapses or
adds up. There is no third case.** No cover was constructed, because the object task (2) presupposes, a
non-collapsing glued world that is not globally CP-a in any useful sense, does not exist.

1. **Theorem C1.1 (dichotomy; PROVED).** Let Γ_ij and Γ_ik be norm-compact convex sets of densities, each
   positive a.e. on its edge region, for example finitely generated sets. Let K_1 and K_2 be the closed cones that
   their restrictions generate in L¹(Q_i).
   - **(a)** If K_1 ∩ K_2 = {0}, no preorder with strict (G) contains both strict edge-unanimity relations. The
     glued closure has an explicit strict cycle Y ≺ Y′ ⪯ Z ⪯ Y inside Q_i. It is a 2-cycle: no Lyapunov chain is
     needed.
   - **(b)** If K_1 ∩ K_2 ≠ {0}, the **glued credal set** G = {ν : ν|R_ij ∈ cone Γ_ij, ν|R_ik ∈ cone Γ_ik} is
     nonzero. Every nonzero member of G is a global density, positive a.e. on M, and every such member endorses
     every comparison of the glued closure. So the closure satisfies strict (G) and (IB), and the world **adds up**.
   - So the exact compatibility condition for non-collapse is: **the restricted cones meet in a nonzero ray.**
     The brief's premise ("no common ray ⇒ no global density, but each edge CP-a-like") describes the collapsing
     case.
2. **Theorem C1.4 (the closure is G-unanimity; PROVED for finitely generated Γ's with a non-degeneracy condition
   (UI)).** Every comparison that is strict for all of G lies in the glued closure. So
   strict-G-unanimity ⊆ closure ⊆ weak-G-unanimity. The closure is CP-a with credal set G, except possibly on
   G-boundary ties, which are irrelevant here. Interior comparisons are therefore forced to follow **every**
   potential in G, not "no potential".
   - **Proposition C1.5 (PROVED, finitely generated with (UI)).** Gluing refines the edges. The closure's own edge
     order on R_ij is unanimity over G|R_ij. This equals Γ_ij-unanimity only if K_1 ⊆ K_2. **Both edge orders
     survive gluing exactly iff K_1 = K_2.**
3. **Theorem C1.6 (the design is dead; PROVED at the status of Thm M0closed(b)).** Assume (H_U). Let every world be
   one of the following:
   - a glued credal world (C1.1 hypotheses);
   - (CP-a);
   - a world with a leading charge nonzero on M;
   - complete and AR.

   Then no cover of T1 exists. (UI) is not needed.
4. **What remains (§5).**
   - **Theorem C1.7 (PROVED; finitely generated, (UI)).** This is B1.3 with a credal set in place of a density. Let a
     world contain only the strict edge unanimities, and possibly more. Then it lies in the **G-band**: it contains
     strict-G-unanimity, and it is contained in "not strictly G-reversed".
   - **Corollary C1.8 (CHECKED, via Savage).** Complete band worlds are fine, hence AR, hence add up.
   - **Proposition C1.9 (PROVED).** A band world that does not add up must carry a **finite G-obstruction**: finitely
     many accepted comparisons δ_1, …, δ_n and weights c_s ≥ 0 with Σ c_s ν(δ_s) < 0 for every ν ∈ G ∖ 0.
   - The one surviving object is therefore an **incomplete band world with a finite G-obstruction**. This is a pure
     order-theoretic question, a finite-cancellation (Kraft–Pratt–Seidenberg-type) failure inside the G-band. No
     selection is involved; it is stated as Question C1.Q.

Scripts (`c1py/glue_dichotomy.py`, output `glue_dichotomy.out`; exact rational arithmetic for every verdict):

| Part | Instances | Result |
|---|---|---|
| A | 300 random cell instances | 176 with K_1 ∩ K_2 = {0}: an explicit strict cycle was built and verified each time. 124 others: a glued density positive on every cell was found. No other case occurred. |
| B | 92 G-strict comparisons | The round chain of Lemma C1.3 was built and verified each time (3 to 524 289 steps). There were no failures. |
| C | 14 of 14 intersecting instances with K_1 ≠ K_2 | In each, an R_ij-internal comparison lies in the closure (explicit chain) although some ρ_l strictly reverses it. This is the refinement of C1.5. |

---

## 1. Definitions

Standing for §§1–5: world i is a preorder on M_U with strict (G) and (IB), considered on regular models. No other
axiom and no other world is used until Theorem C1.6.

- **Edge credal sets.** Γ_ij is a nonempty, norm-compact, convex subset of L¹(R_ij, μ), and every member is > 0
  a.e. on R_ij. Γ_ik is the same on R_ik. **(F)** means finitely generated: Γ_ij = conv{ρ_1, …, ρ_a} and
  Γ_ik = conv{σ_1, …, σ_b}.
- **Edge unanimity.** Let Y, Z be regular with Y △ Z ⊆ R_ij. Then:
  - Y ⊑_ij Z iff γ(E_iY ∖ E_iZ) ≤ γ(E_iZ ∖ E_iY) for every γ ∈ Γ_ij;
  - **strict** unanimity, Y ⊏⊏_ij Z, holds when all these inequalities are strict. By compactness there is then
    a uniform gap.
  - ⊑_ik and ⊏⊏_ik are defined in the same way.
- **Glued closure.** ⪯^gl is the smallest relation on regular models that is reflexive, transitive and (IB)-closed
  and contains ⊑_ij ∪ ⊑_ik. Here (IB)-closed means: whether Y ⪯ Z holds depends only on the pair
  (E_iY ∖ E_iZ, E_iZ ∖ E_iY), as in the N9.4 normal form. The closure exists, as the intersection of all such
  relations.
- **Γ-leading world.** World i contains ⊏⊏_ij ∪ ⊏⊏_ik. With singletons this is B1's "leading density on both edges".
- **Link cones.**
  - K_1 := cone{γ|Q_i : γ ∈ Γ_ij} and K_2 := cone{γ′|Q_i : γ′ ∈ Γ_ik}, in L¹(Q_i).
  - Each is closed: it is the cone over a norm-compact convex base that does not contain 0, because every member is
    > 0 on the non-null set Q_i.
- **Glued credal set.**
  - G := {ν finite measure on M, ν ≪ μ : ν|R_ij ∈ cone Γ_ij, ν|R_ik ∈ cone Γ_ik}.
  - Equivalently, G consists of the pairs (λγ, λ′γ′) with γ ∈ Γ_ij, γ′ ∈ Γ_ik, λ, λ′ ≥ 0 and λγ|Q_i = λ′γ′|Q_i.
  - **Its restriction to Q_i is K_1 ∩ K_2.** This is a fibered product, not an intersection of credal sets.
  - G_1 denotes the normalised base {ν ∈ G : ν(M) = 1}.
- **G-unanimity.**
  - Y ⪯_G Z iff ν(E_iY) ≤ ν(E_iZ) for every ν ∈ G.
  - Y is **G-strictly** below Z iff the inequality is strict for every ν ∈ G ∖ 0.
  - Y and Z are **G-possible** iff some ν ∈ G ∖ 0 has ν(E_iY) ≤ ν(E_iZ).
- **(UI)** (for (F)). Let V := span{ρ_l|Q_i, σ_m|Q_i} ⊆ L¹(Q_i). (UI) requires every nonzero v ∈ V to be nonzero
  a.e. on Q_i.
  - Equivalently: for every non-null S ⊆ Q_i the map T_S : L^∞(S) → V*, h ↦ (v ↦ ∫_S h v), is onto.
  - It holds, for instance, for real-analytic generators whose restrictions to each component of Q_i are linearly
    independent.
  - It is a condition on the design, which we are free to choose, and it is generic.

Throughout, write δ := 1_{E_iX} − 1_{E_iC} for a pair of regular models C, X, and D := C △ X. Then
ν(E_iX) − ν(E_iC) = ν(δ).

---

## 2. The dichotomy

**Theorem C1.1 (PROVED).**

**(a)** If K_1 ∩ K_2 = {0}, there are regular Y, Y′, Z with Y △ Z ⊆ Y △ Y′ ∪ (Y′ △ Z) ⊆ Q_i such that:
- E_iY ⊊ E_iY′, with non-null difference;
- Y′ ⊏⊏_ij Z;
- Z ⊏⊏_ik Y.

Hence no preorder with strict (G) contains ⊏⊏_ij ∪ ⊏⊏_ik. In particular the glued closure violates strict (G):
Y ≺ Y′ ⪯^gl Z ⪯^gl Y.

**(b)** If K_1 ∩ K_2 ≠ {0}, then:
- G ≠ {0}, and every ν ∈ G ∖ 0 has a density > 0 a.e. on M;
- ⪯_G is a preorder with strict (G) and (IB) that contains ⊑_ij ∪ ⊑_ik;
- hence ⪯^gl ⊆ ⪯_G;
- ⪯^gl itself satisfies strict (G) and (IB) and has no strict cycle;
- every ν ∈ G ∖ 0 endorses every comparison of ⪯^gl.

*Proof of (a).*

1. **Separation.**
   - Put B_1 := {γ|Q_i : γ ∈ Γ_ij} and B_2 := {γ′|Q_i : γ′ ∈ Γ_ik}. Both are norm-compact and convex, and 0 ∉ B_1, B_2.
   - B_1 ∩ K_2 = ∅, since K_1 ∩ K_2 = {0} and 0 ∉ B_1.
   - Hahn–Banach (a compact convex set against a closed convex set, in the normed space L¹(Q_i)) gives
     f ∈ L^∞(Q_i) with ⟨f, b⟩ ≥ α > 0 on B_1 and ⟨f, k⟩ ≤ 0 on K_2.
   - In the same way there is g with ⟨g, b⟩ ≥ β > 0 on B_2 and ⟨g, k⟩ ≤ 0 on K_1.
   - Put h₀ := f/α − g/β. Then ⟨h₀, b⟩ ≥ 1 on B_1 (because ⟨g, ·⟩ ≤ 0 on K_1 ⊇ B_1) and ⟨h₀, b⟩ ≤ −1 on B_2.
   - Put h := h₀ / (2‖h₀‖_∞). Then |h| ≤ 1/2, ⟨h, b⟩ ≥ c on B_1 and ⟨h, b⟩ ≤ −c on B_2, with c := 1/(2‖h₀‖_∞).
2. **Realisation by sets.**
   - Take a finite (c/8)-net {w_n} of B_1 ∪ B_2 in L¹ norm, and add μ|Q_i to it.
   - Lyapunov's theorem for this finite non-atomic vector measure gives A ⊆ {h > 0} and B ⊆ {h < 0} with
     ∫_A w_n = ∫ h⁺ w_n and ∫_B w_n = ∫ h⁻ w_n for every n. So μ(A ∪ B) ≤ μ(Q_i)/2.
   - For any w ∈ B_1 ∪ B_2 with ‖w − w_n‖ ≤ c/8, we get |w(A) − ∫h⁺w| ≤ c/4, and the same for B.
   - Hence γ(A) − γ(B) ≥ c/2 for every γ ∈ Γ_ij, and σ(B) − σ(A) ≥ c/2 for every σ ∈ Γ_ik.
3. **The cycle.**
   - Let Y and Z be the regular models with E_iY = B and E_iZ = A, i.e. Y = P_i △ B and Z = P_i △ A.
   - Norm-compact sets of densities are uniformly absolutely continuous. So there is a non-null
     e ⊆ Q_i ∖ (A ∪ B) with sup_{γ∈Γ_ij} γ(e) < c/2. Put Y′ := P_i △ (B ∪ e).
   - Y ≺ Y′ by strict (G).
   - Y′ ⊏⊏_ij Z, since γ(B ∪ e) < γ(A) for every γ.
   - Z ⊏⊏_ik Y, since σ(A) < σ(B) for every σ.
   - All differences lie in Q_i ⊆ R_ij ∩ R_ik.
   - In a preorder containing these relations, Y ≺ Y′ ⪯ Z ⪯ Y gives Y ≺ Y. ∎

*Proof of (b).*

1. **G is nonzero.** Let 0 ≠ κ ∈ K_1 ∩ K_2, say κ = λγ₀|Q_i = λ′γ′₀|Q_i with λ, λ′ > 0. Then
   ν := (λγ₀ on R_ij, λ′γ′₀ on Q_k) is well defined, lies in G, and is > 0 a.e. on M.
2. **Every nonzero member is positive.** Let ν = (λγ, λ′γ′) ∈ G ∖ 0. If λ = 0, then λ′γ′|Q_i = 0, so λ′ = 0
   (because γ′ > 0 on Q_i) and ν = 0. So λ > 0, and symmetrically λ′ > 0. Hence ν > 0 a.e. on M.
3. **⪯_G contains ⊑_ij.**
   - Let Y ⊑_ij Z, so Y △ Z ⊆ R_ij. For ν ∈ G, ν(E_iZ) − ν(E_iY) = λγ(E_iZ ∖ E_iY) − λγ(E_iY ∖ E_iZ) ≥ 0.
   - ⪯_G is a preorder that depends only on δ, so it is (IB)-closed. Hence ⪯^gl ⊆ ⪯_G.
4. **Strict (G) for ⪯^gl.**
   - Let E_iY ⊆ E_iZ with non-null difference S. Split S into S ∩ R_ij and S ∩ Q_k. Each piece is an error-adding
     step inside one edge region, so it is ⊑-accepted. Transitivity gives Y ⪯^gl Z.
   - Every ν ∈ G ∖ 0 has ν(S) > 0, so Z ⪯_G Y fails, hence Z ⪯^gl Y fails.
   - The same argument shows that a strict cycle in ⪯^gl would be a strict cycle in ⪯_G, which is impossible.
5. **Endorsement** is ⪯^gl ⊆ ⪯_G. ∎

*Relation to B1.* With singletons Γ_ij = {ρ^ij} and Γ_ik = {ρ^ik}:
- (a) is the contradiction in the proof of B1.1;
- (b) is the glued density of B1.1.

C1.1 is the credal version: the gluing either fails outright or produces a whole credal set of glued global densities.

**Lemma C1.2 (what gluing does to the edges; PROVED).** Put Ĝ_ij := {ν|R_ij : ν ∈ G} ⊆ cone Γ_ij. Then
Ĝ_ij = {γ ∈ cone Γ_ij : γ|Q_i ∈ K_2}. So Ĝ_ij = cone Γ_ij iff K_1 ⊆ K_2, and both edges are unchanged iff K_1 = K_2.

*Proof.*
- (⊆) is clear.
- (⊇): if γ|Q_i = κ ∈ K_2, say κ = λ′γ′|Q_i, then (γ, λ′γ′) ∈ G.
- If K_1 ⊆ K_2, every γ ∈ cone Γ_ij qualifies. Conversely, Ĝ_ij = cone Γ_ij forces K_1 = Ĝ_ij|Q_i ⊆ K_2. ∎

---

## 3. The closure is G-unanimity (under (F) and (UI))

**Lemma C1.3 (credal transfer chain; PROVED under (F), (UI) and K_1 ∩ K_2 ≠ {0}).**
- *Hypothesis.* C, X are regular and G-strict: ν(δ) > 0 for every ν ∈ G ∖ 0.
- *Conclusion.* There is a finite chain of regular models C = Z_0, …, Z_N = X such that each step
  Z_t → Z_{t+1} lies inside R_ij or inside R_ik and is **strictly** unanimous for the generators of that region.
- In particular C ⪯^gl X, and C ⪯_i X in every Γ-leading world.

*Proof.* Coordinates: every quantity below depends on a function on M only through its integrals against the finitely
many generators.

1. **Strict decomposition (Farkas).**
   - By compactness of G_1, θ := min_{ν∈G_1} ν(δ) > 0.
   - Look for t ∈ V*, realised as a function on Q_i, and η > 0 such that:
     - φ := δ1_{Q_j} + t satisfies ∫φρ_l ≥ η for every l;
     - ψ := δ1_{Q_k} + (δ1_{Q_i} − t) satisfies ∫ψσ_m ≥ η for every m.
   - This is a finite system of linear inequalities in t. By Farkas it is infeasible iff there are (λ, μ) ≥ 0,
     not both 0, with:
     - Σλ_lρ_l|Q_i − Σμ_mσ_m|Q_i = 0 in V, which says (λ, μ) ∈ G;
     - Σλ_l(η − ∫_{Q_j}δρ_l) + Σμ_m(η − ∫_{Q_k}δσ_m − ∫_{Q_i}δσ_m) > 0, which says ν(δ) < η(Σλ + Σμ).
   - For such (λ, μ), ν(M) = Σλ_lρ_l(R_ij) + Σμ_mσ_m(Q_k) ≥ c₀(Σλ + Σμ) with
     c₀ := min(min_l ρ_l(R_ij), min_m σ_m(Q_k)) > 0, and ν(δ) ≥ θν(M). So with 0 < η < θc₀ the certificate is
     impossible, and t exists. Then δ = φ + ψ.
2. **Reserve.**
   - D⁺ := {δ = +1} is non-null, because ν(δ) > 0.
   - Say D⁺ ∩ (Q_k ∪ Q_i) is non-null. Otherwise D⁺ ⊆ Q_j, and everything below runs with the roles of j and k
     swapped.
   - Pick a non-null u ⊆ D⁺ ∩ (Q_k ∪ Q_i) with σ_m(u) ≤ η/4 for every m.
   - Put ψ′ := ψ − 1_u, which still has margin ≥ 3η/4, and δ′ := δ − 1_u.
3. **Room** (Case 1: S := Q_i ∖ D non-null).
   - S = S⁺ ⊔ S⁻, where C, and equally X, is correct (respectively wrong) at world i. Say S⁺ is non-null; the S⁻
     case is the mirror image, described below.
   - By (UI), T_{S⁺} is onto. Put τ₁ := t − T(δ′1_{Q_i}) ∈ V* and pick g₁ ∈ L^∞(S⁺) with T(g₁) = τ₁.
   - For m ∈ ℕ, Lyapunov gives disjoint x, y ⊆ S⁺ with T(1_x) = T(g₁⁺)/m and T(1_y) = T(g₁⁻)/m, once
     ‖g₁‖_∞ ≤ m.
   - Split D ∖ u by Lyapunov into m pieces D^r. Each piece carries 1/m of every generator integral over each of the
     six sets D ∩ Q_l ∩ {δ = ±1}.
4. **Rounds** ("raise first, lower later"; F = R_ij, S = R_ik).
   - The steps are, in order:
     - S_0: raise y;
     - for r = 1, …, m:
       - F_r: toggle D^r ∩ (Q_j ∪ Q_i), raise x, lower y;
       - S_r: toggle D^r ∩ Q_k, lower x, and raise y again if r < m;
     - u is toggled in S_m.
   - Contents (generator integrals of the change in the error indicator):
     - F_r has content φ/m, with margin ≥ 3η/(4m) > 0 for every ρ_l;
     - S_r has content ψ′/m for every σ_m, for r < m;
     - S_m has content ψ′/m − T(1_y) + 1_u ≥ ψ′/m, as soon as m is large enough that σ_m(y) ≤ σ_m(u);
     - S_0 has content +σ(y) ≥ 0, and is vacuous if y is null.
   - Each step toggles only sets in one edge region: x, y, u and pieces of Q_i lie in both regions.
   - Every transfer set is restored, and every piece of D is toggled once, so Z_N = X.
   - All models are regular, since every toggle lies in M.
   - **Mirror (S⁺ null, S⁻ non-null).** Lower first and raise later:
     - S_0 lowers y′ and toggles u (content σ(u) − σ(y′) > 0 for m large);
     - F_r lowers x′ and raises y′;
     - S_r raises x′ and lowers y′ again if r < m;
     - S_m carries a surplus.
5. **Case 2** (Q_i ⊆ D a.e.).
   - Split D = D′ ⊔ D″ so that every generator integral over each of the six sets is halved. Then every
     ν ∈ G has ν(δ1_{D′}) = ν(δ)/2 > 0, because ν is a combination of generators.
   - Go from C to C △ D′, then to X. Each leg has room D″ ∩ Q_i, respectively D′ ∩ Q_i, which is non-null, and
     each leg is G-strict. Apply Case 1 to each leg. ∎

NUMERICS. `glue_dichotomy.py` Part B builds exactly this chain (modes "+" and "−", both orientations of the reserve)
in exact rationals, on random cell models. Over 92 G-strict instances, every step stays in one region, every step is
accepted by every generator of its region, every step respects the available masses, and the chain ends at X. No
failures.

**Theorem C1.4 (identification; PROVED under (F), (UI)).** If K_1 ∩ K_2 ≠ {0}, then for regular C, X:

  C, X G-strict ⇒ C ⪯^gl X ⇒ C ⪯_G X.

So the glued world is CP-a with the fibered-product credal set G, up to comparisons on the boundary of G* (some
ν ∈ G gives a tie). Whether those boundary ties all lie in ⪯^gl is not settled; it is irrelevant below.

*Proof.* Lemma C1.3 and Theorem C1.1(b). ∎

**Proposition C1.5 (gluing refines the edges; PROVED under (F), (UI)).** Suppose K_1 ∩ K_2 ≠ {0} and K_1 ⊄ K_2. Then
there are regular C, X with C △ X ⊆ R_ij, C ⪯^gl X, and ρ_{l₀}(E_iX) < ρ_{l₀}(E_iC) for some generator ρ_{l₀}. So
the closure's edge order on R_ij is strictly finer than Γ_ij-unanimity. The exact compatibility condition for "the
edge orders are unanimity over Γ_ij and Γ_ik, exactly" is K_1 = K_2.

*Proof.*
- Some generator has ρ_{l₀}|Q_i ∉ K_2. By Lemma C1.2, ρ_{l₀} ∉ Ĝ_ij, which is a polyhedral cone (the linear image of
  the polyhedral cone G).
- Separate: there is f ∈ L^∞(R_ij), |f| ≤ 1/2, with ∫fν > 0 on Ĝ_ij ∖ 0 and ∫fρ_{l₀} < 0.
- Realise f by Lyapunov sets A ⊆ {f > 0} and B ⊆ {f < 0}, exactly for the finitely many generators. Put
  C := P_i △ B and X := P_i △ A.
- Then δ = 1_A − 1_B is G-strict, so C ⪯^gl X by C1.3, while ρ_{l₀}(δ) < 0. ∎

NUMERICS (Part C): in 14 of 14 random intersecting instances an R_ij-internal G-strict comparison reversed by a
generator exists, and its explicit chain through R_ik was verified exactly. Example: generator values
(−0.549, +3.42); the chain has 33 steps.

**Answer to task (1), in the brief's terms.**
- The transitive closure (with (IB)) of two edge unanimity orders glued through Q_i:
  - is never "non-CP-a and non-collapsing";
  - collapses (a 2-cycle in Q_i, against strict (G)) exactly when the restricted cones meet only in 0;
  - otherwise it is unanimity over the glued credal set G (up to G-boundary ties). G consists of global strictly
    positive densities, so the world adds up.
- G is not "strictly larger" than CP-a; it is the CP-a credal set of the closure. Its link restriction is K_1 ∩ K_2,
  and it generally refines both edge orders (C1.5).
- Cor CPaU(b) itself is not needed: any member of G endorses everything.

---

## 4. The design is dead

**Theorem C1.6 (PROVED, at the status of Theorem M0closed(b)).** Assume (H_U). Suppose that every world of a ranking
is of one of the following kinds:
- (i) a **glued credal world**: for some Γ_ij, Γ_ik as in §1 (norm-compact convex, densities > 0 a.e.; (F) and (UI)
  not required), the world contains ⊏⊏_ij ∪ ⊏⊏_ik and all its comparisons between regular models are G-weak (lie
  in ⪯_G). By C1.1(b) this includes the case where its comparisons are exactly those of ⪯^gl;
- (ii) (CP-a);
- (iii) a world with a leading charge nonzero on M;
- (iv) complete and AR on M.

Then T1 is not covered on M_U.

*Proof.*
- Take a world of kind (i). If K_1 ∩ K_2 = {0}, C1.1(a) contradicts strict (G). So K_1 ∩ K_2 ≠ {0}; take any
  ν ∈ G ∖ 0, which is > 0 a.e. on M (C1.1(b)).
- ν + μ|_{N₊} is positive on non-null sets of U and endorses every comparison between regular models, in particular
  every relevant one. So the world adds up.
- Kinds (ii)–(iv) add up by Cor CPaU(b), Theorem S21 and Corollary B3.2.
- So the ranking is (M0), which Theorem M0closed(b) excludes. ∎

*Uses:* C1.1 only (no (F), (UI), selection or third world), together with the cited exclusion. *Status:* the new
part is PROVED here. The conclusion inherits the status of Theorem M0closed(b) (imports N13 Prop B and N19
Prop R3(a), read once).

**Why the corner holonomy is not absorbed.** M0closed(b) needs one supporting additive assessment per world. A glued
world supplies a whole credal set of them, each a global positive density. Any one of them carries the potential that
the corner equation x + 1/x = κ + 1 and the box then contradict. The interior comparisons are generated by edge steps
(C1.3), each of which every member of G accepts. So they follow every potential in G, never none.

**Task (2)** was therefore not attempted. Its premise, "a non-CP-a, non-collapsing glued world exists", is false in
the only sense that matters for M0closed (C1.1 and C1.4).

---

## 5. What remains: worlds beyond the closure (the G-band)

A world may contain the strict edge unanimities and also further comparisons that are not G-weak. This is the
nearest reachable relaxation of the design. The following results fix its shape.

**Theorem C1.7 (credal B1.3; PROVED under (F), (UI)).** Let world i be Γ-leading (it contains ⊏⊏_ij ∪ ⊏⊏_ik).
Then K_1 ∩ K_2 ≠ {0}, and for all regular C, X:
- (L1_G) if C, X are G-strict, then C ⪯_i X;
- (L2_G) if C ⪯_i X, then some ν ∈ G ∖ 0 has ν(E_iX) ≥ ν(E_iC); that is, no comparison is G-strictly reversed.

*Proof.*
- K_1 ∩ K_2 ≠ {0} by C1.1(a).
- (L1_G) is Lemma C1.3, whose steps are strict unanimities.
- (L2_G):
  - Suppose C ⪯_i X but g := min_{ν∈G_1} ν(E_iC ∖ E_iX) − ν(E_iX ∖ E_iC) > 0.
  - Then M ∖ E_iX is non-null; otherwise ν(E_iX) = ν(M) is maximal.
  - Take a non-null e ⊆ M ∖ E_iX with max_{ν∈G_1} ν(e) < g/2, by Lyapunov equipartition against the finitely many
    generators. Put X′ := X △ e.
  - Then X ≺_i X′ by strict (G).
  - Also min_{G_1}(ν(E_iC) − ν(E_iX′)) ≥ g/2 > 0, so (L1_G) gives X′ ⪯_i C.
  - Hence X ≺_i X′ ⪯_i C ⪯_i X, a strict cycle. ∎

With singletons this is exactly B1.3 (one density, so the band has zero width).

**Corollary C1.8 (CHECKED; the one import is Savage's theorem, as in Theorem Q36(c)).** A complete Γ-leading world
(under (F), (UI)) is fine. Hence it has a strictly positive almost-agreeing probability, so it is AR on M and adds
up (B3.1–B3.2). Under (H_U), complete Γ-leading worlds are therefore excluded from covers.

*Proof of fineness.*
- Let S ⊆ M be non-null; then m_S := min_{G_1} ν(S) > 0.
- Equipartition M by Lyapunov into N pieces P, each carrying 1/N of every generator integral. So
  max_{G_1} ν(P) = ν(M)/N < m_S for N large.
- So every P is G-strictly below S, and P ⪯_i S by (L1_G).
- Fine together with complete and cancellative gives Savage's almost-agreeing P. P is strictly positive because
  every non-null S dominates the pieces of a finite partition. ∎

**Proposition C1.9 (PROVED; no (F) or (UI) needed beyond compactness of G_1).** Let world i be any world with G ≠ {0}.
Suppose that every finite family of its comparisons between regular models is endorsed by a common ν ∈ G ∖ 0. Then
a single ν* ∈ G ∖ 0 endorses all its comparisons, and world i adds up. Contrapositive: a world that does not add up
has a **finite G-obstruction**, i.e. comparisons C_s ⪯_i X_s (s = 1, …, n) and c ∈ Δ_n with
Σ_s c_s ν(δ_s) < 0 for every ν ∈ G_1.

*Proof.*
- For each comparison, {ν ∈ G_1 : ν(δ) ≥ 0} is compact.
- The finite intersection property gives a common point ν*. As a member of G_1 it is nonzero, so it is > 0 a.e. by
  C1.1(b). This proves the first claim.
- If the intersection over a finite family is empty, the minimax theorem applied to the finitely many linear
  functions ν ↦ ν(δ_s) on the compact convex set G_1 gives the weights c. ∎

So in a Γ-leading world each obstructing comparison is individually G-possible (C1.7), while a convex combination is
G-strictly negative. Compatible sums of accepted comparisons are accepted (transitivity and (IB)). So the
obstructing comparisons cannot be chained: their supports must cross (overlapping gains, as in N17.3).

**Question C1.Q (open; the residual of this design).** Is there a strictly monotone, cancellative, incomplete order
on the measure algebra of M (a world with strict (G) and (IB)), with ⊏⊏_ij ∪ ⊏⊏_ik ⊆ world for some finitely
generated Γ's with (UI), that carries a finite G-obstruction?
- If no, every credal-edge world adds up. The whole family "credal on the edges, free in the interior" is then dead,
  by C1.9 and M0closed(b).
- If yes, such a world is the only candidate of this kind. It would still have to satisfy (S) with closed sections
  for every model, and (C).
- This is a finite-cancellation question (Kraft–Pratt–Seidenberg; for incomplete orders compare Alon–Lehrer's
  multi-prior representation, which needs an explicit cancellation axiom beyond fineness), inside a band of fixed
  finite-dimensional width.
- It involves no selection, no target and no third world. I did not settle it.

**Updated necessary shape of a cover on M_U** (combining B1.4, C1.6–C1.9, B3.2, Q37). Some world i does not add
up, and for it:
- either (α) there is no pair of finitely generated Γ_ij, Γ_ik with (UI) for which world i is Γ-leading (for
  instance because one of its edge orders has no finite-dimensional leading credal set at all, or because only
  non-(UI) pairs are leading, a case C1.7 does not cover);
- or (β) world i is an incomplete Γ-leading band world with a finite G-obstruction.

Alternative (α) includes non-Archimedean edge orders, for example lexicographic edges with pure-charge levels,
which S21 already restricts. In particular the brief's object, "unanimity over different density sets on the two
edges, interior free", is covered only by the second alternative, and only through interior comparisons that are
not G-weak.

---

## 6. Status table

| Item | Statement | Status |
|---|---|---|
| C1.1(a) | K_1 ∩ K_2 = {0} ⇒ explicit 2-cycle in Q_i; no preorder with strict (G) contains both strict edge unanimities | PROVED (norm-compact convex positive densities); NUMERICS Part A (176/176) |
| C1.1(b) | K_1 ∩ K_2 ≠ {0} ⇒ G ∖ 0 consists of global positive densities; closure ⊆ ⪯_G, strict (G), (IB), acyclic; adds up | PROVED; NUMERICS Part A (124/124) |
| C1.2 | Ĝ_ij = {γ ∈ cone Γ_ij : γ\|Q_i ∈ K_2} | PROVED |
| C1.3 | G-strict ⇒ explicit chain of strict edge unanimities | PROVED under (F), (UI); NUMERICS Part B (92/92) |
| C1.4 | strict-G ⊆ closure ⊆ ⪯_G (closure = CP-a with set G up to boundary ties) | PROVED under (F), (UI); boundary ties open, irrelevant |
| C1.5 | gluing refines an edge unless K_1 ⊆ K_2; exact compatibility condition is K_1 = K_2 | PROVED under (F), (UI); NUMERICS Part C (14/14) |
| C1.6 | no cover of T1 on M_U with every world glued-credal, (CP-a), leading-charge, or complete-AR | PROVED at the status of Thm M0closed(b) |
| C1.7 | Γ-leading ⇒ G-band (credal B1.3) | PROVED under (F), (UI) |
| C1.8 | complete Γ-leading worlds are fine, AR, add up | CHECKED (Savage import) |
| C1.9 | not adding up ⇒ finite G-obstruction | PROVED |
| C1.Q | incomplete band world with a finite G-obstruction? | open |

## 7. Files (`c1py/`)

- `glue_dichotomy.py` (+ `glue_dichotomy.out`). Cell model with piecewise-constant densities, so that Lyapunov is
  exact. LPs propose; every verdict is checked in exact Fractions.
  - Part A: dichotomy, explicit cycle or glued positive density.
  - Part B: the round chain of C1.3.
  - Part C: edge refinement C1.5.
- `round15_note.md`: a copy of §§0–7 above.
- `.c1_round10_backup.md`: a copy of the round-10 note (also reproduced below).
- `gauge_layer.py`, `thmA_cap_geometry.py` (+ `.out`): round-10 scripts, unchanged.
