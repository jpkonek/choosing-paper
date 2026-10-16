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


---

# Archive: round-10 C1 note (14 Oct 2026), unchanged

# C1: construction side on CF(T1) — every gluing fails at the carrier of the cuts

14 Oct 2026. Construction side of the round-10 attack (BRIEF9). Labels: **PROVED** (proof written here), **CHECKED** (verified, proof sketched or resting on a cited classical theorem), **CONJECTURE**, **NUMERICS** (evidence only). Scripts in `c1py/`. Notation as in the write-up *The Contamination Triangle.tex* (cited as WU), §§2–5: Ω = int Δ, p\* the target prior, K_q the family, P(q,g) = min_{K_q} m·g, R(g) = {q ∈ Ω : P(q,g) > 0}, λ_b = line(p\*, e_b) the crossing chords, ℓ_g = g^⊥ ∩ aff Δ (a line of *probabilities*), d = c − c′ and the d-line {d·q = 0} (a line of *priors*).

---

## 0. Outcome

**No solution of CF(T1) was found, and none of the requested kinds can exist.** Two theorems show where every global gluing breaks.

1. **Theorem A (PROVED, given one CHECKED classical input).** In no solution of CF(T1) is there an open set O ⊆ Ω on which K_q = {σ(q)} is precise with σ injective. In particular **the referee's sector caps (counterexample C1) cannot occur in any solution**, and neither can any diagonal-projective precise region anywhere in Ω (not only those meeting a chord, as in WU Prop vertexfree(iv)).
   - *Mechanism.* Inside a precise region every gamble whose line passes through it is adjacent: R(g) and R(−g) touch along the line. The d-face is a half-line, so it must run from the region to ∂Δ.
   - A positive-measure set of lines through the cap (those nearly parallel to the failing edge) cannot reach ∂Δ without crossing a crossing chord λ_b.
   - Along a d-face, K_q ⊆ ℓ_g (WU's R4 Thm B, in CF form). At a chord point crossed by two such faces, K_q would lie in two distinct lines, so it would be precise. That contradicts WU Prop vertexfree(iv).
   - C1 tested only facet gambles. The gambles that kill it are generic ones (§5, `c1py/thmA_cap_geometry.out`).
2. **Corollary A′ (PROVED).** Precise regions with interior can only be *walls* (K ≡ {m₀}), at least wherever σ is locally injective or C¹ of rank 1. A wall carries the d-face of no generic gamble. So **no precise region with interior can carry the cuts** that WU Thm cuts/Thm apex require at each vertex.
3. **Theorem B (PROVED, for the stated class).** CF(T1) has **no locally definable solution**, i.e. none that is semialgebraic, or more generally definable in an o-minimal structure on every compact subset of Ω.
   - This class contains every ansatz suggested in the brief:
     - piecewise-projective families;
     - families built from finitely many generator gambles;
     - families whose dimension changes across finitely many pieces (cores, segment layers on the chords, point caps, triangles near p\*);
     - hulls of gauge mixtures and projective points;
     - cyclically equivariant families;
     - vertex-self-similar families whose pieces accumulate only at ∂Δ.
   - *Mechanism.* A cover cannot be split almost everywhere (WU main theorem), so a non-null set of pairs is adjacent.
   - A dimension count on their d-faces leaves two possibilities, and both fail:
     - the faces sweep an open set, which is then precise, hence a wall by A′, and a wall carries no generic face;
     - the faces share lines, in which case nested faces force the corresponding ℓ_g to be concurrent and σ to be constant along the faces; the faces then sweep an open set again.
4. **What the gauge-mixture approximants teach (§2).**
   - Their pairs are all split (PROVED).
   - Their vertex models are conv(W ∪ {e_i}), not {e_i}.
   - As the polygons tend to T1 they converge to the plateau family K_q = conv(W ∪ {q}) (CHECKED, NUMERICS). It is not a solution, and it violates every structural property that WU §5 proves for covers of T1.
   - So nothing in them points toward a solution. They succeed for polygons precisely because polygon targets do not force competition.
5. **Exact failure point.** It is the *carrier of the cuts*. At each vertex the box forces a non-null family of adjacent pairs, whose d-faces run to ∂Δ with K_q ⊆ ℓ_g along them. Precise caps cannot carry them (Theorem A). Walls cannot (A′). Nothing tame can (Theorem B).
   - A solution, if one exists, must be **wild**: not locally definable, with adjacency carried by a fractal (Cantor- or Kakeya-type) family of faces (§7).
   - To close CF(T1) completely, the dimension counts of Theorem B need measure-theoretic replacements. The two missing lemmas are stated precisely in §7.2. CONJECTURE: CF(T1) has no solution.

---

## 1. Setting and inputs

CF(T1) is the problem stated in BRIEF9 / WU Def CF. A *solution* is a Hausdorff-continuous q ↦ K_q on Ω with K_{p\*} = T1. For a.e. mixed g ("good" g) there must be c, c′ with the sign patterns of g and −g such that, for every q ∈ Ω,
- R(g) = {c·q > 0, d·q > 0};
- R(−g) = {c′·q > 0, d·q < 0};
- d = c − c′.

The **d-face** is F(g) = {q ∈ Δ : c·q = c′·q > 0}, a relatively open subset of the d-line. The pair is **adjacent** if F(g) ∩ Ω ≠ ∅, and **split** otherwise.

Inputs used, with their status:
- **(I1)** WU Prop vertexfree(iv): no prior on a crossing chord λ_b is precise. It is proved for every cover (N28 Prop 4.3, one referee), hence for every solution of CF(T1) at the status of CCIBU (WU Prop CF, ⇐).
- **(I2)** WU Thm main and Cor coverage, refereed twice, together with the exact reduction N14 §3(iv): a solution whose pairs are a.e. split gives a realisation on M_{D_{K′}}.
  - Proof of the reduction: Ĉ_q := co(K_q ∪ K′). For split pairs, R(g) ∩ Ω = {c > 0} ∩ Ω (R4 Thm A, PROVED) with vertex-respecting signs, and Prop reduction (converse) applies.
  - Hence **no solution has a.e. split pairs**. This needs no appeal to CCIBU.
- **(I3)** R4 Lemma S (PROVED): pairwise disjoint non-degenerate segments lie on a Lebesgue-null set of lines.
- **(I4)** The local fundamental theorem of projective geometry: a continuous injective map of a planar domain that sends segments into lines is projective (classical; used in R4 Prop D). For the injective case we use R4 Prop D as repaired in R8 (R8: the injective case is "essentially right"; its missing step, invariance of domain, is supplied in Lemma 5.0 below). We do **not** use the non-injective part of Prop D, which R8 marks GAP.
- **(I5)** o-minimal dimension theory (van den Dries, *Tame topology*, Ch. 4, 7), used only in Theorem B.

---

## 2. What the gauge mixtures teach

R10a Thm M: M_i compact convex in ℝ³_{≥0}∖0 with a_i e_i ∈ M_i and (M2); f_i(g) = min_{M_i} m·g; K_q = ν(Σ q_i M_i); c(g) = f(g) and c′(g) = f(−g).

**Lemma 2.1 (gauge mixtures are split everywhere; PROVED).** For every mixed g and every q ∈ Δ, c·q > 0 implies c′·q < 0. So no pair of a gauge-mixture system is adjacent.

*Proof.* f_i is concave and homogeneous, so f_i(g) + f_i(−g) ≤ f_i(0) = 0. Hence (c + c′)·q ≤ 0 on Δ. ∎ (NUMERICS: 0 violations in 2·10⁴ random gambles, `c1py/gauge_layer.out`.)

So gauge mixtures live entirely in the non-adjacent world. There WU Thm main forbids T1, and R10a Thm R forbids every triangle. They cover polygons because a polygon target, unlike T1, does not force competition.

**Lemma 2.2 (the limit of the approximants; CHECKED, NUMERICS).** Take M′ of R10a: M_i = conv{a e_i, bW} with W = T1(ε′). Then
- K_q ⊇ conv(W ∪ {q}), because choosing a e_i in every M_i gives ν(a q) = q;
- d_H(K_q, conv(W ∪ {q})) → 0 as a/b → 0, uniformly in q ∈ Ω.

*Sketch.* A point of Σ q_i M_i is a·(q⊙t) + b·Σ q_i(1−t_i)w_i with t ∈ [0,1]³. After normalisation it is a mixture of ν(q⊙t) and a point of W, the weights being proportional to a·(q·t) and b·Σ q_i(1−t_i).
- If the W-weight is not ≫ the other, then Σ q_i(1 − t_i) = O(a/b), so q⊙t is within O(a/b) of q in ℓ¹.
- Otherwise the point is within o(1) of W.

Numerics (`gauge_layer.out`, ε′ = 0.29, along q = (1−2s, s, s)): d_H(K_q, conv(W ∪ q)) ≤ 0.039, 0.0090, 0.0019, 0.0004 for a/b = 0.05, 0.01, 0.002, 0.0004. Meanwhile d_H(K_q, W) at s = 0.2 stays at 0.0898 for every a/b. ∎

**What changes in the limit.** The approximants converge to the *plateau family* K_q^∞ = conv(T1 ∪ {q}). It has K ≡ T1 on all priors in T1, so it violates:
- the absence of plateaus (R10a Thm P);
- thin zero sets (WU Thm pivot): P(·,h) ≡ 0 on a half-plane for every facet gamble h;
- vertex anchoring (K_{e_b} = conv(T1 ∪ e_b) ≠ {e_b}, against WU Cor TSalways(c));
- the requirement that both acceptances lie in the advice range (Cor TSalways(b)): for g ∉ D_W the gauge systems have no acceptance in their advice range;
- competition, which they never have (Lemma 2.1).

The (LF) margin O(a) recorded in R10a is the visible symptom. **Conclusion:** the approximants are close to T1 only at p\*. None of the structure that covers of T1 must have (PC/NS with x ∈ {x₊, x₋}, cuts, vertex limits {e_b}) is present in them or in their limit. So they cannot seed a construction.

---

## 3. Self-consistent chart fields: the ansätze tried

The self-consistent form (BRIEF9) has two steps:
- choose (c, c′) for a.e. g;
- put K_q := ∩{m : m·g ≥ 0 for g with q ∈ R(g)}, and demand that the induced K_q reproduce every chart.

Every ansatz below was set up in this form. Each was abandoned at the point stated. Each is locally definable, so Theorem B (§6) excludes all of them at once.

**3.1 Hulls of gauge mixtures and projective points.** K_q = conv(⋃_j ν(S_j(q))) with S_j(q) = Σ_i q_i M_{j,i}. This is the minimal way to leave the split world of Lemma 2.1.
- *Charts.* sign P(q,g) = sign min_j q·f_j(g), so R(g) = ⋂_j {q·f_j(g) > 0} is a polygon cut by several lines through no common point.
- *Concurrency condition.* CF requires that, on Ω, only two of these lines are active for R(g), two for R(−g), and that one line (the d-line) is shared and concurrent with the other two. For one gauge piece plus one precise piece σ(q) = ν(Nq), this reads det(f(g), f(−g), Ng) = 0 wherever all three lines meet Ω. That is an identity in g on an open set. I found no solution of it other than the degenerate one below.
- *Symmetric gauges.* The gauges M_i = n_i + w_i B, with B centrally symmetric, achieve exactly f(g) − f(−g) = 2Ng. But then σ(q) = ν(Nq) lies inside the hull, and the system is again a gauge mixture: split everywhere.
- *Precise extreme points.* Making the precise points extreme on the d-faces forces dim K_q ≤ 1 there (Lemma 4.1). The hull then degenerates to a precise region exactly where adjacency is needed. That precise region is diagonal-projective, which Theorem A excludes.

**3.2 Three-zone gluing (the brief's plan).** The plan has three parts:
- a core near p\* with full-dimensional K_q (PC/NS facet data x₊);
- a non-precise segment layer along each λ_b;
- precise identity sector caps S_b at e_b adjacent to the failing edge, carrying the cuts (C1).

Zone 3 is impossible (Theorem A). The two natural replacements also fail:
- a wall (constant precise region) cannot carry a generic d-face (Cor 5.3);
- a one-dimensional layer carries the faces of only a null set of lines (Lemma 4.3), and Theorem B shows that no tame family of faces can do it.

So the gluing fails before the core and the chord layer even come into play: **there is nothing at the vertex to glue them to.**

**3.3 Families that change dimension, with apexes anywhere.** The admissible apex positions were scanned: on the edge, outside Δ, and on the boundary of a precise or segment region. In every case the face is a half-line reaching ∂Δ (Lemma 4.2) and K_q ⊆ ℓ_g along it (Lemma 4.1). The only freedom left is where the faces run, and §§4–6 settle that.

---

## 4. Faces in CF form

Throughout, g is good. Write P := {q ∈ Ω : K_q is a singleton}, which is relatively closed because diam K_q is continuous. Write σ(q) for the point of K_q when q ∈ P, and N₁ := {q : K_q is a non-degenerate segment}.

**Lemma 4.0 (adjacency is not negligible; PROVED).** In every solution of CF(T1), the set G_adj of good g with F(g) ∩ Ω ≠ ∅ is non-null.

*Proof.* Otherwise a.e. pair is split, and (I2) gives a realisation of T1 on a U-domain, which contradicts WU Thm main. ∎

**Lemma 4.1 (K_q ⊆ ℓ_g on closed faces; PROVED).** Let g be good. Then:
- cl R(g) ∩ cl R(−g) ∩ Ω = cl F(g) ∩ Ω =: J_g;
- K_q ⊆ ℓ_g for every q ∈ J_g.

*Proof.*
- *(⊆).* cl R(g) ⊆ {c ≥ 0, d ≥ 0} and cl R(−g) ⊆ {c′ ≥ 0, d ≤ 0}. So the intersection lies in {d = 0, c = c′ ≥ 0}, which is cl F(g) on the d-line.
- *(⊇).* At q with d·q = 0 < c·q = c′·q, nearby points with d > 0 lie in R(g) and those with d < 0 lie in R(−g). Apexes (c = c′ = 0) are limits of such points.
- On J_g, continuity of P(·, ±g) gives P(q,g) ≥ 0 and P(q,−g) ≥ 0, i.e. min_{K_q} m·g ≥ 0 ≥ max_{K_q} m·g. ∎

This is R4 Thm B in CF form. It holds for **every** good g, not just a.e., because CF charts are exact at every q.

**Lemma 4.2 (faces are half-lines; PROVED).** If g is adjacent, then J_g is the intersection of Ω with a closed half-line of the d-line (or with the whole d-line). So J_g is a non-degenerate segment, at least one of whose ends lies on ∂Δ.

*Proof.* q ↦ c·q is affine on the d-line, so {c ≥ 0} is a closed half-line, the whole line, or empty. ∎

**Lemma 4.3 (single-face points; PROVED).** If q ∈ J_g ∩ J_{g′} with ℓ_g ≠ ℓ_{g′}, then K_q = ℓ_g ∩ ℓ_{g′} ∩ Δ, a singleton, so q ∈ P. Hence the sets J_g ∖ P are pairwise disjoint for projectively distinct g, and by Lemma S (I3) the d-lines of the g with J_g ⊄ P form a null set of lines. ∎

**Lemma 4.4 (nested faces force concurrency; PROVED).** Let L be a line and E an end of L ∩ Δ. Let G_{L,E} be a set of good adjacent g with d-line L and E ∈ cl J_g, containing at least two projectively distinct g. Then:
- all ℓ_g, g ∈ G_{L,E}, pass through one point m_L, i.e. G_{L,E} ⊆ m_L^⊥;
- K_q = {m_L} at every q of L that lies in two of the faces;
- in particular this holds on every J_g that is not the largest face.

*Proof.* By Lemma 4.2 the faces in G_{L,E} are segments of L with common end E, so they are nested. Given g₁, g₂, g₃, the smallest of their faces lies in all three. At a point of it, Lemma 4.1 gives K_q ⊆ ℓ_{g₁} ∩ ℓ_{g₂} ∩ ℓ_{g₃}, which is nonempty, so the three lines are concurrent. With two distinct lines fixed, every third line passes through their common point m_L. ∎

**Lemma 4.5 (one sign class per d-line; PROVED).** If good g, g′ have the same d-line, then sign(g′) = ±sign(g). For m ∈ Ω the pencil m^⊥ meets all three mixed pair classes, and for m ∈ Δ not a vertex it meets at least two.

*Proof.*
- An affine function on aff Δ determines its coefficient vector in ℝ³, because q ↦ d·q restricted to {𝟙·q = 1} is injective on vectors. So equal d-lines give d(g′) = λ d(g) with λ ≠ 0, and d has the strict sign pattern of its gamble.
- The pencil m^⊥ is a projective line with the three coordinate zeros {g_i = 0} on it. Crossing each zero flips one sign. For m interior the three zeros are distinct and give three arcs. ∎

The sign argument is the repair that R8 suggested for the fold case of Prop D. It is used three times below.

---

## 5. Theorem A: no injective precise region

**Lemma 5.0 (injective precise regions are diagonal-projective; CHECKED: R4 Prop D, injective case, with R8's repair written out).** Let O ⊆ Ω be open and connected, with K_q = {σ(q)} on O and σ injective. Then σ(q) = ν(w⊙q) on O for some w ∈ (0,∞)³.

*Proof.*
1. By invariance of domain, σ(O) is open and σ: O → σ(O) is a homeomorphism.
2. Take a good g with ℓ_g ∩ σ(O) ≠ ∅, and q ∈ σ^{-1}(ℓ_g). Since σ is open, σ-values on both open sides of ℓ_g occur arbitrarily near q. So q ∈ cl R(g) ∩ cl R(−g) = J_g (Lemma 4.1), and σ^{-1}(ℓ_g) lies in the d-line of g.
3. For an arbitrary line ℓ meeting σ(O), approximate it by lines ℓ_{g_n} of good g. Points of σ^{-1}(ℓ) are limits of points of σ^{-1}(ℓ_{g_n}), because σ is open; so σ^{-1}(ℓ) also lies in a line.
4. So σ^{-1} is a continuous injective map sending segments into lines. By (I4) it is projective, hence σ(q) = ν(Aq) with A invertible and 𝟙·Aq > 0 on O. The d-line of g is then {q·(Aᵀg) = 0}, and R(g) ∩ O = {q·Aᵀg > 0} ∩ O ⊆ {d > 0}. So d(g) is a positive multiple of Aᵀg, and Aᵀg has the strict sign pattern of g for a.e. g with ℓ_g ∩ σ(O) ≠ ∅.
5. By continuity, (Aᵀg)_i = 0 whenever g_i = 0 there. Taking g = e_i × x with x ∈ σ(O) gives det(e_i, x, Ae_i) = 0 on an open set of x. Hence Ae_i ∥ e_i: A is diagonal, and positivity of Aq on O gives w > 0. ∎

The only input beyond CF is the classical theorem (I4). R8 found the injective case essentially right and asked for exactly step 1.

**Theorem A (PROVED, given (I1) and Lemma 5.0).** In no solution of CF(T1) is there a nonempty open O ⊆ Ω on which K_q = {σ(q)} with σ injective.

*Proof.*
1. *O lies in one chamber.* By (I1), O avoids the three chords. The chords are three distinct lines through p\*, each through one vertex, and they cut Ω into six open triangles ("chambers"). Taking O connected, it lies in one chamber C = int conv{p\*, e_b, f}. Here f is the foot on ∂Δ of another chord, and C has one side [e_b, f] on ∂Δ and two *chord sides* s₁ = (p\*, e_b), s₂ = (p\*, f) inside Ω.
2. *A non-null set of lines crossing both chord sides.* Let 𝓛 be the set of lines that meet O and cross both open chord sides. It is open. It is nonempty: through q₀ ∈ O, the line parallel to [e_b, f] meets the other two sides of the triangle C in their relative interiors.
3. *These lines are d-lines.* By Lemma 5.0, σ(q) = ν(w⊙q), and for each g the zero set of q ↦ σ(q)·g in O is O ∩ L_g, where L_g := {q : q·(w⊙g) = 0}. Then:
   - g ↦ L_g is a diffeomorphism from projective classes of mixed g onto lines;
   - L_g = L_{g′} iff g ∝ g′ iff ℓ_g = ℓ_{g′};
   - so a.e. L ∈ 𝓛 is L_g for a good g.
   Fix such a g. Inside O we have R(g) ∩ O = {σ·g > 0} and R(−g) ∩ O = {σ·g < 0}. Both sides of L_g meet the open set O, so L_g ∩ O ⊆ cl R(g) ∩ cl R(−g) = J_g. Since L_g ∩ O is a non-degenerate segment, the d-line of g is L_g.
4. *Each such face reaches a chord.* By Lemma 4.2, J_g is a segment of L_g that contains L_g ∩ O and reaches ∂Δ. Now L_g ∩ cl C = [y₁, y₂] with y₁ ∈ s₁ and y₂ ∈ s₂, both in Ω. The ends of L_g ∩ Δ lie outside [y₁, y₂]. So the convex set J_g contains y₁ or y₂, and K_{y_i} ⊆ ℓ_g by Lemma 4.1.
5. *Fibration.* Let G_i := {good g with L_g ∈ 𝓛 and y_i(g) ∈ J_g}. Then G₁ ∪ G₂ is co-null in the non-null set {g : L_g ∈ 𝓛}, so some G_i, say G₁, is non-null. In the coordinates (y, θ) ∈ s₁ × (0, π) (crossing point, direction), the map g ↦ L_g ↦ (y₁(g), θ) is a diffeomorphism onto its image. By Fubini there is y ∈ s₁ whose θ-section of the image of G₁ has positive measure, so it contains two directions. This gives good g ≠ g′ with y ∈ J_g ∩ J_{g′} and ℓ_g ≠ ℓ_{g′}.
6. Lemma 4.3 now makes y ∈ λ_b ∩ Ω precise, which contradicts (I1). ∎

**Corollary 5.1 (counterexample C1 is not part of any solution; PROVED).** The identity cap K_q = {q} on any open sector at e_b, the identity on any open set, and every diagonal-projective precise region (anywhere in Ω) are incompatible with CF(T1). WU Prop vertexfree(iv) excluded only regions meeting a chord.

*Illustration* (`c1py/thmA_cap_geometry.out`, ε = 0.3, x₊, b = 2, failing edge [e₁, e₂]):
- The C1 cap point q₀ = (0.047, 0.95, 0.003) passes the referee's exact facet tests (A), (B). It lies in the chamber conv{u, e₂, f}, f = (½, ½, 0).
- The lines through q₀ that leave that chamber through both chords form an angle of 0.034 rad.
- At y = (0.002, 0.996, 0.002) ∈ λ₂, 1283 lines through y and through admissible C1 cap points leave the chamber through both chords. Two of them give gambles g₁, g₂ with ℓ_{g₁} ∩ ℓ_{g₂} = {y}. Theorem A's fibration step would then force K_y = {y}, a precise point on λ₂.
- The facet gambles tested by C1 are all on the facets, where this phenomenon does not appear.

**Proposition 5.2 (no C¹ rank-1 precise region; PROVED).** In no solution is there an open O ⊆ Ω with K = {σ} on O and σ of class C¹ with rank 1 on O.

*Proof.*
1. Shrinking O, write σ = γ∘φ with φ: O → ℝ a submersion with connected level arcs, and γ an embedded C¹ arc in Δ. The arc meets the three vertices of Δ in at most three parameters s, and these are ignored below.
2. A.e. line ℓ meeting γ(φ(O)) crosses γ transversally at some m = γ(s). For good g with ℓ_g such a line, points of the level arc φ^{-1}(s) see σ-values on both sides of ℓ_g. So φ^{-1}(s) ⊆ J_g, and the d-line of g is the line L_s that contains the level arc (which must therefore be straight).
3. In the coordinates (s, direction) of transversal lines (a local diffeomorphism), Fubini gives an s for which a.e. g in the pencil γ(s)^⊥ is good.
4. For such s with γ(s) not a vertex, that pencil meets at least two sign classes, each in an arc of positive length (Lemma 4.5). So it contains good g, g′ of different classes with the same d-line L_s. This contradicts Lemma 4.5. ∎

**Corollary 5.3 (walls carry no generic face; PROVED).** Let V be a component of int P on which σ ≡ m₀. Then the good g with J_g ∩ V ≠ ∅ satisfy m₀·g = 0 (Lemma 4.1), so they form a null set. There are only countably many such V. So for a.e. g, J_g avoids every open constant precise region.

**Corollary 5.4 (where the cuts can live; PROVED).** In every solution, for a.e. adjacent g, J_g ⊆ (P ∖ int P) ∪ N₁ ∪ P_wild. Here P_wild is the union of the components of int P on which σ is non-constant, injective on no open subset, and C¹ of rank 1 on no open subset. In particular the cut pairs of WU Thm cuts / Thm apex can be carried only by:
- precise sets with empty interior;
- one-dimensional layers, whose faces lie on a null set of lines by Lemma 4.3;
- wild precise regions.

P_wild = ∅ if σ is locally definable (Prop 6.1), or if the non-injective case of R4 Prop D is ever proved.

---

## 6. Theorem B: no tame solution

**Definition (LD).** A solution is **locally definable** if, for every compact Q ⊆ Ω, the set {(q, m) : q ∈ Q, m ∈ K_q} is definable in some o-minimal expansion of the real field (which may depend on Q). Examples:
- semialgebraic families: piecewise-projective, piecewise-polynomial, polytopes with algebraic vertex maps, hulls of gauge mixtures and projective points, families generated by finitely many gambles;
- globally subanalytic families;
- families with finitely many pieces on each compact subset of Ω. This includes families whose pieces accumulate only at ∂Δ, such as log-periodic constructions that are self-similar under the diagonal projective maps fixing e_b.

(LD) restricts **the construction class only**. It is not added to CF(T1). The statement below is a theorem about that class.

**Proposition 6.1 (tame precise regions are walls; PROVED).** Under (LD), σ is constant on every connected open O ⊆ int P.

*Proof.* Fix a ball B with cl B ⊆ O. By C¹ cell decomposition, a dense open subset B′ ⊆ B has finitely many components, on each of which σ is C¹ of constant rank.
- Rank 2 somewhere would give, by the inverse function theorem, an open set on which σ is injective, against Theorem A.
- Rank 1 on a component is excluded by Proposition 5.2.

So σ is constant on each of the finitely many components of B′. Then σ(B) lies in the closure of a finite set and is connected, so it is a point. Since O is connected, σ is constant on O. ∎

**Theorem B (PROVED, at the status of (I1) and (I2)).** CF(T1) has no locally definable solution.

*Proof.*
- *Step 0 (an open set of adjacent pairs inside one tame window).*
  - Lemma 4.0 makes G_adj non-null.
  - Exhaust Ω by compact triangles Q_n. Let G_n be the set of good g with J_g ∩ int Q_n containing a non-degenerate segment. Then G_adj = ⋃_n G_n, so some G_n is non-null.
  - Definability: J_g ∩ int Q = cl R(g) ∩ cl R(−g) ∩ int Q, where the closures may be taken inside int Q, and "good" is first-order (∃ c, c′ ∀ q). So G_n is definable. Being non-null, it has interior.
  - Fix Q = Q_n and a definable open G ⊆ G_n of good gambles. Put J′_g := J_g ∩ int Q and I := {(g, q) : g ∈ G, q ∈ J′_g}. Then dim I = 3.
  - Let δ: G → {lines} be the d-line map, and k := dim δ(G).
- *Case k = 2.*
  - Let U := π(I) ⊆ int Q, where π(g, q) = q. If dim U ≤ 1, all faces would lie on finitely many lines, so k = 0. Hence dim U = 2.
  - By Lemma 4.1, the fibre π^{-1}(q) consists of g with K_q ⊆ ℓ_g. It has dimension 0 if K_q is not a singleton, and lies in a pencil (dimension ≤ 1) if it is.
  - Since dim I = 3, the set U₁ := {q : dim π^{-1}(q) = 1} has dimension 2, so it contains an open V. By Lemma 4.3, V ⊆ P.
  - By Prop 6.1, σ ≡ m₀ on a component V₀ of V. Then π^{-1}(V₀) has dimension 3. Its projection to G has dimension ≥ 2, because its fibres are segments. But that projection lies in m₀^⊥, which has dimension 1. Contradiction.
- *Case k = 1.*
  - Shrinking G, δ has 1-dimensional fibres over a 1-dimensional family Λ of lines. Shrinking again, all faces in each fibre contain the same end E(L) of L ∩ Δ.
  - By Lemma 4.4, each fibre lies in a pencil m_L^⊥, and K ≡ {m_L} on the set O_L of points of L lying on two faces of the fibre. O_L contains J′_g for every non-maximal g, so O_L ∩ int Q is a non-degenerate segment.
  - Distinct lines of a 1-dimensional definable family share a point only finitely often, outside finitely many exceptional points. So W := ⋃_{L ∈ Λ} O_L ∩ int Q has dimension 2 and contains an open set inside P.
  - By Prop 6.1, σ ≡ m₀ on a component V₀ of int W. Every L whose O_L meets V₀ has m_L = m₀, and these L form a 1-dimensional set. Their fibres are pairwise disjoint and 1-dimensional, so together they form a 2-dimensional subset of G inside m₀^⊥. Contradiction.
- *Case k = 0.* Some line L has a 2-dimensional fibre, and a 2-dimensional part of it shares an end. By Lemma 4.4 that part lies in a 1-dimensional pencil. Contradiction.

So G_adj is null, against Lemma 4.0. ∎

*Remarks.*
1. *Inputs.* Theorem B uses the hypothesis T = T1 only through (I1) (no precise point on a crossing chord, inside Theorem A) and (I2) (the main theorem, inside Lemma 4.0). It needs none of PC, NS, the box or the cuts explicitly; they enter only through (I1). So, for any all-facing T in general position, where (I2) holds, it shows: **a locally definable solution of CF(T) must have precise points on the crossing chords.**
2. *What it excludes in the brief's list.* It excludes every option in BRIEF9's strategy (2)–(3):
   - piecewise-projective families;
   - generator families;
   - dimension-changing families with finitely many pieces;
   - equivariant and diagonally normalised families;
   - apexes anywhere.

   The "measurable chart data" freedom is not restricted: for a locally definable K the charts are determined by K.

---

## 7. The exact failure point, and what a solution would have to be

### 7.1 Where every attempted gluing broke

Every attempt broke at the same place: **the vertex structure that carries the cuts.** The core near p\* (PC/NS with x₊ or x₋) and the non-precise chord layers were never the problem; nothing is known against them. What fails is the following.

1. The box fails at one edge per vertex (WU Prop T1). On general domains the failure has to be absorbed by adjacent pairs whose d-faces cut the box witnesses near e_b (WU Thm cuts, Thm apex). And by Lemma 4.0, adjacency cannot be negligible in any solution.
2. Each d-face is a half-line reaching ∂Δ, with K_q ⊆ ℓ_g along it (Lemmas 4.1, 4.2).
3. The candidate carriers fail as follows:
   - *precise regions with interior:* injective σ is impossible (Theorem A: the faces through the region are forced along every line, and lines nearly parallel to the failing edge must cross a chord); C¹ rank-1 σ is impossible (Prop 5.2, by the sign class); constant σ carries no generic face (Cor 5.3);
   - *one-dimensional layers:* each prior carries the face of at most one gamble, so the faces lie on a null set of lines (Lemma 4.3);
   - *faces sharing lines:* nesting forces concurrency and constant σ along the faces (Lemma 4.4), within one sign class (Lemma 4.5);
   - *any tame combination of these:* excluded by the dimension count of Theorem B.

### 7.2 What a solution would have to look like (necessary shape; PROVED unless marked)

A solution of CF(T1) must be **wild**, i.e. fail (LD), near the cut faces. More precisely, for a.e. adjacent g:
- (W1) J_g ⊆ (P ∖ int P) ∪ N₁ ∪ P_wild (Cor 5.4);
- the non-precise parts of faces lie on a null set of lines (Lemma 4.3).

One of the following must also hold:
- **(W2-a)** the d-lines of a non-null set of adjacent pairs form a non-null set of lines. Then, by Fubini, the union of their faces has positive area, and at a.e. point of it two faces cross. So P has positive area and empty interior, or contains P_wild.
- **(W2-b)** the d-line map sends a non-null set of adjacent pairs onto a null set Λ of lines. Then:
  - each fibre lies in a pencil m_L^⊥, within one sign class (Lemmas 4.4, 4.5);
  - σ ≡ m_L along leaves O_L ⊆ P;
  - the pencils over Λ cover a non-null set of gambles.

  Since the set of lines meeting a set M of zero length is null, M := {m_L} must have positive one-dimensional measure. Yet the leaves are carried by a null set of lines, so σ restricted to a transversal maps a null set onto a set of positive length. In particular σ is **not Lipschitz** on P there.

A concrete candidate shape left open: a **Cantor fan**.
- *Leaves.* Precise leaves O_x run from near e_b to the failing edge, for x in a Cantor set X, with σ ≡ m(x) on O_x and m of Cantor-function type.
- *Gaps.* The gaps between leaves carry non-precise K_q.
- *Pencils.* Every leaf that P accumulates on from both sides, with m having a tangent there, forces the whole pencil m(x)^⊥ onto one d-line. Lemma 4.5 then excludes it, provided a.e. gamble of that pencil is good, which Fubini guarantees only when the parametrisation is regular. So the surviving shapes need leaves accumulated one-sidedly, cusps in m, or a non-regular parametrisation.

I have not been able to exclude or construct such a fan.

### 7.3 What would close CF(T1)

Two measure-theoretic statements would turn Theorem B into a full impossibility proof. Both are CONJECTURE.
- **(M1) Prop D on positive-measure precise sets.** If P has positive area, then at a.e. density point σ is locally constant, or diagonal-projective, on P. With (M1), (W2-a) dies: the Theorem A argument runs on density points, because a.e. line through a positive-measure set meets it in positive length.
- **(M2) No Peano carriers.** In every solution, σ is locally Lipschitz on P near the faces of adjacent pairs (or some weaker Hölder/Hausdorff condition holds). Then the dimension counts of Theorem B go through with Hausdorff measure and the coarea formula, and (W2-b) dies.

**CONJECTURE C1.** CF(T1) has no solution. (This is WU Conj N21. The evidence now includes Theorems A and B: every tame solution is excluded, and every precise cap.)

**Suggested next step for the impossibility side.** Prove (M2). A natural route is a quantitative version of Lemma 4.1: along a face, K_q ⊆ ℓ_g, and WU's Lipschitz bound near p\* (Prop regularity (a)) transported to the vertices by the diagonal projective maps fixing e_b. Alternatively, show directly that a Cantor fan violates the chart condition of the generic gambles whose lines cross the gaps between leaves.

---

## 8. Status table

| Result | Status | Depends on |
|---|---|---|
| Lemma 2.1: gauge mixtures split everywhere | PROVED | — |
| Lemma 2.2: approximants → conv(W ∪ {q}), a plateau family | CHECKED + NUMERICS | — |
| Lemma 4.0: adjacency non-null in every solution | PROVED | (I2): WU Thm main (2 referees), N14 §3(iv) (1 referee) |
| Lemmas 4.1–4.5: faces (exact K_q ⊆ ℓ_g, half-lines, single-face points, nested concurrency, sign class) | PROVED | Lemma S (R4) for 4.3 |
| Lemma 5.0: injective precise regions are diagonal-projective | CHECKED | classical theorem (I4); R4 Prop D injective case as repaired in R8 |
| **Theorem A**: no injective precise open region; C1 excluded | PROVED given (I1) and 5.0 | (I1) = WU Prop vertexfree(iv) (N28 Prop 4.3, 1 referee; for CF solutions at CCIBU status) |
| Prop 5.2: no C¹ rank-1 precise region | PROVED | CF only (no further input) |
| Cor 5.3, 5.4: walls carry no generic face; where cuts can live | PROVED | — |
| Prop 6.1: tame precise regions are walls | PROVED | Theorem A, Prop 5.2, o-minimal C¹ cell decomposition |
| **Theorem B**: no locally definable solution of CF(T1) | PROVED at the status of (I1), (I2) | as above |
| §7.2 necessary shape of a wild solution | PROVED (W1, W2) / CONJECTURE (Cantor fan open) | — |
| (M1), (M2); CF(T1) has no solution | CONJECTURE | — |
| C1 cap counter-illustration | NUMERICS / CHECKED (exact intersections) | `c1py/thmA_cap_geometry.out` |

Things a second reader should check first:
1. Theorem A step 5. The fibration needs g ↦ (y₁(g), θ) to be a diffeomorphism. It is, because L_g = {q·(w⊙g) = 0}.
2. Theorem A uses (I1) on the **whole** chord, both sides of p\*.
3. Theorem B case k = 1: the finite-intersection claim for 1-dimensional families of lines.
4. The definability of "good" and of J_g ∩ int Q in Step 0.

---

## 9. Files (`c1py/`)

| File | Content | Result |
|---|---|---|
| `gauge_layer.py/.out` | R10a M′ gauge mixtures: d_H(K_q, W), d_H(K_q, conv(W ∪ q)) along a ray, and the split check | the limit is conv(W ∪ {q}), not W; the boundary-layer guess was wrong and is corrected in Lemma 2.2; 0 adjacent pairs |
| `thmA_cap_geometry.py/.out` | C1 cap at e₂ (ε = .3, x₊): chamber, exits through both chords, two cap lines meeting at a chord point | a 0.034 rad cone of bad directions at q₀; 1283 admissible lines through y ∈ λ₂; ℓ_{g₁} ∩ ℓ_{g₂} = {y} |
