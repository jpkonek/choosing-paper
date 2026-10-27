# PP71. Recurrent repair among four coherent models: what the axioms allow, and what blocks it

24 October 2026. Alternative task of Brief 57 (moderate effort). One author; not refereed. Read: BRIEF57_two_direction, AUDIT_round57 (last part), AUDIT_round57_answers §6, PP68 §1 and §4 (edge lemma, Lemma 4.1, Theorem 4.3, Theorem 4.4, scripts cycle68*.py), PP67 (module T, N, D\*), AUDIT_completion (rules I–IV).

**Labels.**
- PROVED: complete argument here, or a cited result used within its hypotheses.
- CHECKED: exact SAT on a finite cell sub-universe, in `r9/PP71_py/`. Every clause is an axiom instance on the sub-universe (lib71.py, same encoding as PP68's lib68; (TC) is added lazily, but every SAT answer is re-checked against **every** ordered triple). So UNSAT is a full-domain fact; SAT is evidence only.
- **The cell instances are faithful.**
  - Cells are the faces of the exact plane arrangement (complete enumeration).
  - Each class-3 region on which some model is silent is split into a bounded piece and its rest. Fills act on unions of bounded pieces (non-conic, hence incoherent by AUDIT_completion §1) and on unions of whole regions (conic).
  - Every UNSAT reported below survives with **no** coherence labelling at all (env ALLCOH=1), so it does not depend on which non-selected models are coherent.
- NUMERICS: sampled geometry (exact rational arithmetic per sample).
- CONJECTURE / OPEN: as stated.

No axiom is added. One standing hypothesis, named where used: **(DK)** coherent models are of the form D_K with K a closed convex subset of the simplex that is not a single point (true of every model in the module).

---

## 0. Verdict

**(a) The forced verdict pattern of a 4-cycle is consistent with the axioms — on cell sub-universes.**
- PP68's edge lemma turns a cycle C₁ → C₂ → C₃ → C₄ → C₁ ("C_{i+1} dominates the class-3 fills of C_i") into the verdicts C_i ⪯₃ C_{i+1} and C_i ⋠₁ C_{i+1}, C_i ⋠₂ C_{i+1}. Triangle-(TC) does not close a 4-cycle. Either both diagonals are refused both ways at world 3 (no ties at all), or all four cycle edges tie at world 3 (Lemma 2.3; PROVED).
- CHECKED: for four explicit coherent models (segments from v₃, §3), "each C_{i+1} dominates every cell-level class-3 fill of C_i" is SAT. Every model in the sub-universe is defended and protected, and (C) holds. The forced verdicts are exactly the edge-lemma pattern and nothing else. A tie-free completion exists. On the same instance the 2-cycle is UNSAT (PP68 Lemma 4.1). The 3-cycle is SAT with forced world-3 ties, because its members are pairwise 3-mixed.
- CHECKED: T can be added (selected and registered) without conflict.
- CHECKED, **negative**: the members (and T) cannot also dominate all of the cycle's whole-region **splices**. An 11-splice core is UNSAT with no coherence labelling; it uses splices from all four edges and is SAT without the cycle (§3).

**(b) Explicit coherent models realise the pattern pointwise, but no relation on the full measurable domain is constructed.** The obstruction is structural, not a missing computation:
- **Theorem 2.4 (PROVED).** Any directed cycle of fill domination, of any length and with any rule assigning dominators, forces the world-1 and world-2 relations to be **non-transitive**. Hence every finite system closed under "each class-3 fill of a member is dominated by a member" has non-transitive worlds 1 and 2.
- **Corollary 2.5 (PROVED).** Under any certificate with transitive worlds 1 and 2, such as PP67's 𝒲 or any real-valued or lexicographic Φ_w, repair can never return. Every fill-closed system is then infinite and contains an endless chain strictly improving at worlds 1 and 2. This holds **without (GC)**. It extends PP68 Thm 4.4 (which assumed (GC)) to every certificate whose worlds 1 and 2 are transitive, and it complements PP67 Prop 7.4, which concerns additive certificates.
- **Props 2.6–2.7 (PROVED).** Two further devices are excluded:
  - "patching": a world relation that contains a fine total preorder (an integral of rank losses) cannot accept anything against it;
  - an integral of a pointwise skew-symmetric comparison (an SSB-type device) satisfying (TC) is an expected-loss difference, so it is transitive.

  So defence against every measurable rival cannot come from Bayes acts at worlds 1 and 2, which is the only whole-domain defence technology the project has.

**(c) What blocks recurrence.** Two things do, and neither is (TC) on the forced verdicts or the fill dominations.
1. **Defences.** A recurrent system needs a defence device at worlds 1 and 2 that respects (IB), (TC) and strict (G), is intransitive, and is not given by a score. No such device is known. §4 states what a closure proof would have to check.
2. **Splices.** The cycle cannot repair its own splices (CHECKED). So new models are needed, each with its own fills to repair, and the closure problem reappears one level out.

**Further structure (PROVED).**
- **Prop 2.2: common A-region.** In a uniform cycle of coherent models (any length), all members have the **same** class-3 A-region. So they differ on class 3 only by S versus B.
- Consequences:
  - T, N, every R_α, every J_β and L₀ all have bottom vertex v₃, so they are admissible partners for one another;
  - no F_t with t > 0, and not D\*, can share a uniform cycle with any of them.

**Isolated versus non-isolated (§5).** A finite set of models at isolated indices does **not** meet the milestone. In a continuum of cycles, closed sections make every refusal inherited by nearby indices (Lemma 5.1; PROVED), and some pair of cycles is pinned in both directions (Lemma 5.2; PROVED). CHECKED: two neighbouring segment cycles, with two-sided pinning and no diagonal ties, stay SAT. The joint cell instance is identical at six sampled parameter pairs across the family. A non-isolated recurrent theorem would need the defence device of (c), uniformly along the family.

| Item | Result | Label |
|---|---|---|
| Whole-family agreement exclusion | Lemma 2.1 | PROVED |
| Common class-3 A-region in coherent uniform cycles | Prop 2.2 | PROVED (under (DK)) |
| 4-cycle world-3 dichotomy (diagonals refused, or edge ties) | Lemma 2.3 | PROVED |
| Recurrence ⇒ worlds 1, 2 non-transitive | Thm 2.4 | PROVED |
| Transitive certificates ⇒ endless chain strictly improving at 1, 2, no (GC) needed | Cor 2.5 | PROVED |
| No patching of a fine total preorder | Prop 2.6 | PROVED |
| Additive skew comparisons + (TC) ⇒ expected-loss form | Prop 2.7 | PROVED |
| Explicit 4-cycle: SAT, edge pattern forced, tie-free completion | §3 | CHECKED |
| Same instance: 2-cycle UNSAT, 3-cycle SAT with forced ties | §3 | CHECKED |
| Stress tests; T present | §3 | CHECKED |
| Members and T cannot also dominate 11 whole-region splices (all four edges; needs the cycle) | §3 | CHECKED (UNSAT, no coherence labelling) |
| Two-step composition condition | Lemma 4.1 | PROVED |
| Inherited refusals and pinning in a continuum of cycles | Lemma 5.1 | PROVED |
| Two-sided pinning occurs in any uncountable family | Lemma 5.2 | PROVED |
| Two neighbouring cycles with two-sided pinning, no ties | §5 | CHECKED (SAT) |
| Exact census; sampled census misses types (an earlier UNSAT withdrawn) | §3, §5 | CHECKED |
| Full-domain recurrent relation with defences | — | OPEN |

---

## 1. Setting

As in Brief 57: three worlds, problems g mod sign, Gaussian μ, the full four-advice domain, and ranks correct 0 < silent 1 < wrong 2 < contradictory 3. The axioms are reflexivity, strict (G), (IB), (TC) (triangles only), (S), (LA) and global (C). X ⪯_w Y means "X is at least as good as Y at w".

**Notation.**
- **Classes.** On class k, A is the majority sign (correct at the two worlds other than k) and B is the other sign (correct at k). M_k is the class-k region.
- **Advice of D_K.** D_K answers A at g ∈ M₃ iff the line {m·g = 0} has K strictly on the {e₁, e₂} side. It answers B iff K is strictly on the e₃ side, and is silent iff the line meets K.
- **Fills.** A class-3 fill of C is Y = C[F ↦ A], with F ⊆ Sil(C) ∩ M₃ measurable and non-null. F may be bounded (then Y is non-conic) or conic, for example F = the whole class-3 silence, as in PP67. At worlds 1 and 2 it is a strict pointwise improvement of C; at world 3 it is strictly worse.
- **Cycles.** A **uniform m-cycle** is C₁, …, C_m (registered, selected at indices with full support) such that C_{i+1} dominates (⪯_w at every w) **every** class-3 fill of C_i, indices mod m. A **cycle of fill domination** is weaker: C_{i+1} dominates at least one class-3 fill of C_i.

**Edge lemma (PP68 Lemma 4.2; PROVED there, used within its hypotheses).** If B ⪯₁ Y and B ⪯₂ Y for a class-3 fill Y of C, then:
- C ⋠₁ B and C ⋠₂ B;
- C ⪯₃ B, provided C is selected with 3 ∈ supp.

---

## 2. Structure of recurrent repair (PROVED)

**Lemma 2.1 (whole-family agreement exclusion).** Suppose C_j dominates every class-3 fill of a registered C_i. Then C_j ≠ A a.e. on Sil(C_i) ∩ M₃.

*Proof.* This is the audit's path obstruction, applied inside the A-part.
- Suppose E ⊆ {C_j = A} ∩ Sil(C_i) ∩ M₃ is bounded and non-null, and put X = C_i[E ↦ A] and Z = C_j[E ↦ S]. Then rec(C_j, X) = rec(Z, C_i): on E both pairs agree, and off E they coincide.
- By (IB), Z ⪯_w C_i at every w. Protection of C_i gives an all-world tie, and (C) then makes Z coherent.
- But Z differs from the cone C_j exactly on a bounded non-null set. So Z is not conic (AUDIT_completion §1), and hence not coherent. ∎

With per-fill dominators, the same argument shows that the dominator of X_E is not A a.e. on E.

**Prop 2.2 (common A-region; PROVED under (DK)).** Let C_i = D_{K_i} form a uniform m-cycle, m ≥ 1 (m = 1 is excluded anyway by strict (G)). Put A_i := {g ∈ M₃ : C_i = A}. Then A₁ = A₂ = … = A_m. Equivalently (see the remark after the proof), the sets ↑K_i := (K_i + cone{e₁ − e₃, e₂ − e₃}) ∩ Δ all coincide. In particular, if one member has bottom vertex b (K ⊆ ↑{b}, b ∈ K), every member does.

*Proof.*
1. **Silence is the closure of strict silence.** Let h_i = min_{K_i} m·g and H_i = max_{K_i} m·g. Then Sil(C_i) ∩ M₃ = {h_i ≤ 0 ≤ H_i}, and the open set {h_i < 0 < H_i} is dense in it. To see this, given g in the closed set, pick k ≠ k′ in K_i (by (DK)) with k·g ≤ k′·g. Then g + δ(k′ − k) − t·1, for small δ > 0 and a suitable t, separates them strictly.
2. **A_{i+1} misses Sil(C_i).** A_{i+1} is an open convex cone. If it met Sil(C_i) it would meet the open strict-silence set in a non-null set, contradicting Lemma 2.1. So A_{i+1} ⊆ A_i ∪ B_i, and by convexity A_{i+1} lies in one of these two disjoint open sets.
3. **That set is A_i.** Let g_t = (1, 1, −t).
   - If e₃ ∉ K_{i+1}, then g_t ∈ A_{i+1} for small t > 0.
   - g_t ∉ B_i for small t, since K_i ≠ {e₃} contains some m with m₁ + m₂ > 0.

   So A_{i+1} meets A_i, and A_{i+1} ⊆ A_i. If e₃ ∈ K_{i+1}, then A_{i+1} = ∅ ⊆ A_i.
4. **Around the cycle.** A₁ ⊇ A₂ ⊇ … ⊇ A_m ⊇ A₁. ∎

The equivalent form in terms of ↑K_i is a remark only, and nothing below uses it. A(K) on M₃ depends only on ↑K, since moving up raises m·g for g ∈ M₃; the converse is support-function duality.

**Reading.**
- In a uniform cycle the members agree on where class 3 is answered A. They differ on class 3 only by S versus B, and on classes 1 and 2.
- A model with bottom vertex b has ↑K = ↑{b}. T, N, L₀, every R_α and every J_β have bottom v₃. Every F_t with t > 0 has bottom v_t ≠ v₃, and D\* has none (its set lies in the edge).
- So the audit's fill curve F_t, which adds 3-wrong A answers on class 3, **cannot** close into a uniform cycle with the T–N part of the curve. Partners must be chosen among models with a common bottom.

**Lemma 2.3 (4-cycle at world 3; PROVED).** In a uniform 4-cycle, C_i ⪯₃ C_{i+1} for all i. For each diagonal {C₁, C₃} (and likewise {C₂, C₄}), exactly one of the following holds:
- (i) C₁ ⋠₃ C₃ and C₃ ⋠₃ C₁; then C₁ and C₃ defend against each other at worlds 1 or 2;
- (ii) C₁ ≈₃ C₃, and all four cycle edges are world-3 ties.

In case (ii), no pair among C₁, …, C₄ may be pointwise strictly 3-ordered.

*Proof.*
- If C₃ ⪯₃ C₁, the triangle (C₁, C₂, C₃) is accepted. (TC) installs C₂ ⪯₃ C₁, C₃ ⪯₃ C₂ and C₁ ⪯₃ C₃.
- Then the triangle (C₃, C₄, C₁) is accepted, and installs C₄ ⪯₃ C₃, C₁ ⪯₃ C₄ and C₃ ⪯₃ C₁.
- Starting from C₁ ⪯₃ C₃ is symmetric. Strict (G) gives the last claim. ∎

So a 4-cycle **avoids** the forced world-3 ties of PP68 Thm 4.3 exactly in case (i). That makes world 3 intransitive too.

**Theorem 2.4 (recurrence forces intransitivity at worlds 1 and 2; PROVED).** Let C₁ → C₂ → … → C_m → C₁ be a cycle of fill domination, m ≥ 1. Here C_{i+1} ⪯₁ Y_i and C_{i+1} ⪯₂ Y_i for some class-3 fill Y_i of C_i. Then, for w = 1 and for w = 2, the relation ⪯_w restricted to {C_i, Y_i} is not transitive.

*Proof.*
- Y_i ⪯_w C_i by guidance. The edge lemma gives C_i ⋠_w C_{i+1}.
- If ⪯_w were transitive, then C_{i+1} ⪯_w C_i for every i. Hence C₁ ⪯_w C_m ⪯_w … ⪯_w C₂, so C₁ ⪯_w C₂, a contradiction. ∎

Only (TC) and strict (G) are used: neither registration nor the dominator rule matters. For class-k fills the same holds at the two worlds other than k.

**Corollary 2.5 (PROVED).**
- (a) Let 𝒮 be a finite set of models, each silent on a non-null part of M₃, such that every class-3 fill of every member is dominated by a member. Then 𝒮 contains a cycle of fill domination, so worlds 1 and 2 are not transitive. (Every vertex of the finite digraph has an out-edge.)
- (b) Suppose instead that worlds 1 and 2 are transitive, for example total preorders from any real-valued or lexicographic Φ_w, as in PP67's 𝒲. Then the digraph is acyclic. Starting from any member, the dominators form an infinite path of **distinct** models C₀ → C₁ → …, strictly improving at worlds 1 and 2 (C_{k+1} ≺₁ C_k and C_{k+1} ≺₂ C_k), and each step is defended at world 3.

So, under transitive certificates, the infinite chain of PP68 Thm 4.4 is forced **without (GC)**. Combined with PP67 Prop 7.4 (an additive certificate allows only finitely many uniform generations), this shows that no additive certificate supports a fill-closed system with uniform generations.

**Prop 2.6 (no patching; PROVED).** Let Φ(X) = ∫ ℓ(X(g), g) dμ, with ℓ finite, integrable and strictly increasing in the world-w rank. Suppose ⪯_w satisfies (TC) and strict (G) and contains the order {X ⪯ Y : Φ(X) ≤ Φ(Y)}. Then X ⪯_w Y implies Φ(X) ≤ Φ(Y).

*Proof.*
- Suppose X ⪯_w Y with Φ(X) > Φ(Y). Then Y is not contradictory a.e.
- Worsen Y on a small non-null set, using an atomless μ, to obtain Z with Φ(Y) < Φ(Z) < Φ(X). Then Y ⪯_w Z and Z ⪯_w X, both inside the Φ-order.
- (TC) on X ⪯ Y ⪯ Z ⪯ X installs Z ⪯_w Y, the reverse of a strict guidance comparison. ∎

So "an additive certificate plus the cycle's records" is impossible. The cycle's records C_{i+1} ⪯₁ Y_i are against every such Φ₁ (Theorem 2.4).

**Prop 2.7 (skew-additive comparisons; PROVED).** Suppose X ⪯_w Y ⇔ ∫ φ(X(g), Y(g), g) dμ ≥ 0, with φ(·, ·, g) skew-symmetric on ranks and measurable in g, and suppose this relation satisfies (TC). Then φ(x, y, g) = f(y, g) − f(x, g) a.e., so the relation is an expected-loss comparison and is transitive.

*Proof.*
- Suppose the cyclic sum φ(0,1) + φ(1,2) + φ(2,0) exceeds δ > 0 on a non-null set inside one class. On a sub-piece, all of φ's values vary by less than δ/10.
- Split the sub-piece into three disjoint parts of equal measure. Let X, Y, Z agree elsewhere, and on the three parts take the world-w ranks (0,1,2), (1,2,0) and (2,0,1).
- Then ∫φ(X,Y), ∫φ(Y,Z) and ∫φ(Z,X) are all positive. That is an accepted triangle whose reverses are refused. The same argument works for the other rank triples, including rank 3. ∎

**Reading of 2.4–2.7.** Every whole-domain defence device used so far scores models at worlds 1 and 2:
- Bayes acts of an additive Φ_w, possibly with lexicographic keys;
- "maximal-lottery" defences from skew-additive comparisons.

Any rule that defends C_i against X at w **whenever** C_i scores no worse than X at w fails on the cycle members themselves. The edge lemma's refusals C_i ⋠_{1,2} C_{i+1} would force the scores to fall strictly all the way round the cycle.

---

## 3. An explicit four-cycle (CHECKED)

**Models (cycle71.py).** C_i = D_{[v₃, a_i]}, with a_i = v₃ + λ(θ_i, 1 − θ_i, −1), λ = 1/5 and θ = 9/10, 13/20, 7/20, 1/10. These are segments from T's bottom vertex v₃ = (7, 7, 16)/30, leaning from e₁ towards e₂. Each lies in M, so each C_i tightens T. All have bottom v₃, as Prop 2.2 requires.

**Census (CHECKED, exact).** `geom71.exact_points` enumerates one exact point in every face of the arrangement of planes {g : n·g = 0}, where n runs over the coordinate vectors and every vertex of every K. This is complete: every face has a vertex on its boundary, and every face at a vertex is hit by a perturbation along a sum of two tangent rays.

Random sampling (≈ 3,400 points) **misses** one type here (class 2, SSBB) and 13 of the 56 types of the two-cycle instance of §5. All instances below therefore use the exact census (census71.out). There are 18 non-constant cells:
- class 1: BBBS, BBSS, SAAA, SSAA, SSSA;
- class 2: AAAS, AASS, ASSS, SBBB, SSBB;
- class 3: BBBS, BBSS, BSSS, SBBB, SSBB, SSSB;
- the common class-3 silence SSSS, split into two bounded atoms P₁, P₂ and a rest.

Each class-3 cell containing an S is split into a bounded piece and its rest, giving 25 cells in all.

Here a pattern lists the advice of (C₁, C₂, C₃, C₄). The silences are "intervals" in the θ-order. Every pair is 3-mixed, and every edge has the pointwise prerequisites:
- C_i silent on part of class 3;
- agreement exclusion (Lemma 2.1);
- C_{i+1} strictly better than C_i somewhere at 1 and at 2;
- C_{i+1} strictly worse than C_i somewhere at 3.

(explore71.py.)

**Sub-universe U₀.** The four models and 46 class-3 fills of each, 188 models in all. For each model these are:
- every non-empty union of its five silent bounded pieces: 31 non-conic fills;
- every non-empty union of its four silent **whole** regions: 15 conic fills, including E = its whole class-3 silence, as in PP67.

**Results (cycle71.out).**
- Each prefix H₁, H₁ + H₂, H₁ + H₂ + H₃ is SAT, and the **4-cycle H₁ … H₄ is SAT**. Here H_i says that C_{i+1} dominates every fill of C_i.
- Forced verdicts among C₁ … C₄ under the 4-cycle:
  - C_i ⪯_w C_{i+1}: refused at 1, refused at 2, accepted at 3, for each i;
  - every other ordered pair: free at all three worlds.

  This is exactly the edge-lemma pattern; nothing else is forced.
- **2-cycle** C₁ ⇄ C₂: UNSAT. C₁ and C₂ share the silence P₁ ∪ P₂, so PP68 Lemma 4.1 applies.
- **3-cycle** C₁ → C₂ → C₃ → C₁: SAT. Theorem 4.3's world-3 ties are forced, but they are harmless here, since no pair is pointwise 3-ordered.

  This corrects one reading of PP68 §4: short cycles are killed by shared silence (Lemma 4.1) or by a pointwise-3-strict pair (Thm 4.3), not by length alone.

**Stress tests (cycle71b.out).** U₀ is enlarged by:
- every single-cell change of each C_i to A, S or B;
- 100 or 200 random changes on 2–4 cells.

That gives |U| = 488 (seed 1) and 588 (seed 2). An earlier run on the coarser V1 cells gave the same results at |U| = 364, 464 and 464.
- The 4-cycle is SAT on every instance, and so is the 3-cycle.
- Diagonals and reverse edges remain free at every world.
- Both completions of Lemma 2.3 are SAT: (i), with both diagonals refused both ways at world 3 (**no world-3 ties at all**), and (ii), with all world-3 ties.
- In the 3-cycle all six world-3 verdicts are forced to be acceptances, as Theorem 4.3 predicts.
- All six cyclic orders of the four models also give SAT on U₀ (orders71.out). So U₀ alone does not discriminate between orders; the order C₁ → C₂ → C₃ → C₄ is the one tested further.

**With T, and with splices.** T = D_M is added as a fifth selected, registered model. Every K_i lies in M, so T is silent wherever the C_i differ. Splices are consecutive: C_i[H ↦ C_{i+1}].

Two instances were run.
- **V1** (cycle71c_v1_allcoh.out, cycle71f_v1.out; env PIECES=0). Cells are whole regions (23 cells), and the common silence is split into two conic halves.
  - Fills: every union of silent cells, all of them conic.
  - Splices: 138 whole-region splices. That is all of them for the pairs (1,2) and (3,4), which differ on 5 regions, and 40 sampled for (2,3), which differs on 6, and for (4,1), which differs on 16.
- **V3** (cycle71c.out, cycle71c_allcoh.out, cycle71f.out). This is the finer instance of U₀ (31 cells), with 159 sampled splices on the finer cells.

Results:
- **K1. The 4-cycle with T present: SAT** in both. T coexists with the cycle, defended and protected.
- **K2, V1. K1 plus "each of the 138 splices is dominated by one of T, C₁, …, C₄": UNSAT**, even with **no coherence labelling** (ALLCOH). This is a full-domain fact.
  - Each single edge's splices together are dominable, with or without the cycle. All 138 together are dominable **without** the cycle.
  - A greedy-minimal core has 11 splices, from **all four** edges (1 from C₁/C₂, 1 from C₂/C₃, 5 from C₃/C₄, 4 from C₄/C₁). Without H₁ … H₄ the core is SAT.
  - **Cross-check (cycle71h.out).** The same 11 whole-region splices are embedded in the finer instance, with bounded and conic fills, and with the other V1 splices present as rivals. The result is again UNSAT with no coherence labelling, and SAT without the cycle.
- **K2, V3** (159 random finer splices, which happen not to contain the core): SAT. Splices are therefore not uniformly fatal; specific whole-region splices are.

**Reading.** Recurrence is compatible with the whole fill families, but in this example it prevents the cycle's own members (and T) from also repairing all of the cycle's whole-region splices. Some splice needs a dominator outside the five models, and that new model's fills then need repair in turn. So recurrent repair here reaches the partial-success class "fills alone" (at cell level) and not "splices". Whether some other choice of four models is closed under splices is OPEN.

---

## 4. Whole measurable fill families: what is shown, and what a proof needs

**What the CHECKED results cover.** The cell instances quantify over fills that are unions of bounded pieces or of whole regions. A general measurable fill E ⊆ Sil(C_i) ∩ M₃ cuts across cells in arbitrary proportions, and its record has copies at every base, most of which lie outside any finite sub-universe. SAT on U₀ therefore shows that no **finite** combination of axiom instances among these models refutes the cycle. It does not supply the relation.

**What a full-domain relation must provide.**
- (R1) The domination records r_i^E := rec(C_{i+1}, C_i[E ↦ A]), for all measurable E ⊆ Sil(C_i) ∩ M₃, accepted at all worlds, together with all their copies (rule I).
- (R2) A defence of every C_i against **every** measurable X, at a world of its support.
- (R3) Protection of each C_i (rule III), and (C) (rule IV), with no failure F1 or F2.

By §2, (R2) cannot come from scores at worlds 1 and 2. The natural replacement is a partial commitment system, closed under rules I–IV, in which defences are committed record by record. Its triangle types are:
- (T1) cycle copy, guidance, guidance;
- (T2) cycle copy, cycle copy, guidance;
- (T3) cycle copy, defence copy, guidance;
- (T4) two or three defence copies;
- (T5) types involving world-3 ties, in case (ii) of Lemma 2.3 only.

**Lemma 4.1 (the two non-trivial composition conditions; PROVED).**
- (T1) never closes. The cycle records are mixed at worlds 1 and 2, so a guidance-guidance return would make the cycle record a strict anti-guidance record.
- (T2) at world w ∈ {1, 2} closes exactly when two cycle records compose, on a common base, to a strict pointwise w-improvement. Whether it closes depends only on the two records, not on the base.
  - For consecutive edges, take r_{i+1} = rec(C_{i+2}, C_{i+1}[F′ ↦ A]) followed by r_i^F with F′ ⊆ Sil(C_i) ∩ Sil(C_{i+1}) ∩ M₃ ∖ F.
  - These compose to C_{i+2} → C_i[F ∪ F′ ↦ A]. The triangle closes if C_i[F ∪ F′ ↦ A] is pointwise weakly w-better than C_{i+2}.
  - **Necessary condition** for a cycle whose consecutive members share class-3 silence: C_{i+2} is strictly w-better than C_i's **full** class-3 fill somewhere, for w = 1 and for w = 2.
  - CHECKED (compose71.py): this holds for the explicit cycle. The witnesses always include class-3 cells where C_i says B and C_{i+2} is silent, and for half of the (i, w) pairs they also include class-1 and class-2 cells.

*Proof.*
- The copy of rec(C_{i+1}, C_i[F ↦ A]) based at C_{i+1}[F′ ↦ A] is legitimate iff F′ avoids its support {C_{i+1} ≠ C_i} ∪ F. It ends at C_i[F ∪ F′ ↦ A].
- The return to C_{i+2} is a guidance comparison iff the stated pointwise condition holds, and then its reverse is strictly refused.
- (T1): in a triangle with one cycle copy and two guidance links, the two guidance links make the cycle record's new side pointwise weakly w-better than its old side, or the reverse. Either contradicts its being mixed at w. ∎

**What remains (OPEN).** Types (T3)–(T4) depend on how defences are committed, and no rule for committing them is known. PP67 Theorem 4.1 got (T3)–(T4) for free from a total certificate, which §2 excludes here.

**OPEN question.** Is there a record-level defence rule, committed by a criterion that is not a score (for example, by the shape of the record's support), whose closure under rules I–IV is clean together with (R1)? Sub-universe SAT cannot decide this: on U₀ every defence is satisfied by *some* assignment, but SAT returns no rule.

**(b), answered.**
- Explicit coherent models realise the forced pattern, including whole **cell-level** fill families and every pointwise prerequisite.
- They do **not** yet realise it for whole measurable families in one relation, because (R2) has no available construction.
- The blocking items are not (TC) on the forced verdicts (Lemma 2.3 shows these are consistent), nor the fill dominations (SAT). They are:
  - the absence of an intransitive, non-scored defence device;
  - in the explicit example, the cycle's whole-region splices (§3).

---

## 5. Isolated indices do not meet the milestone; what a non-isolated version needs

A finite set of cycle members at isolated indices has trivially closed sections. That is round 56's isolated-index success again, and it falls short of the milestone (Brief 57, "Partial success"). A non-isolated version needs a **continuum** of cycles: models C_i(s), s ∈ S, with S having no isolated points, at indices p_i(s) depending continuously on s.

**Lemma 5.1 (inherited refusals and pinning; PROVED).** Let X be a fixed rival, and suppose C_{p} ⋠_w X at an index p. Then C_{p′} ⋠_w X for all p′ in a neighbourhood of p, because the section {q : C_q ⪯_w X} is closed. In particular, for each s and each s′ close enough to s (how close depends on s):
- C_i(s′) ⋠₁ C_{i+1}(s) and C_i(s′) ⋠₂ C_{i+1}(s), so C_i(s′) ⪯₃ C_{i+1}(s) (**pinning**);
- in case (i) of Lemma 2.3, C_i(s′) ⋠₃ C_{i+2}(s);
- C_i(s′) refuses, at worlds 1 and 2, every fill of C_i(s) whose neighbourhood contains p_i(s′). Since these neighbourhoods depend on E and can shrink, this is a rival-dependent reservation in the sense of Brief 57.

*Proof.* Each item is the openness of refusal sets, applied to the edge lemma, to case (i), and to strict (G). ∎

**Lemma 5.2 (two-sided pinning; PROVED).** Let S be uncountable, for example an interval, and let the indices p_i be continuous. Then there are s ≠ s′ in S for which pinning holds **in both directions**: C_i(s′) ⋠_{1,2} C_{i+1}(s) and C_i(s) ⋠_{1,2} C_{i+1}(s′), for all i.

*Proof.*
- By Lemma 5.1 and continuity, each s has a radius r(s) > 0 such that the eight refusals C_i(s′) ⋠_w C_{i+1}(s) (i ≤ 4, w = 1, 2) hold whenever |s′ − s| < r(s).
- S = ∪_n {r ≥ 1/n}, so some S_n is uncountable. It therefore contains s ≠ s′ with |s − s′| < 1/n ≤ min(r(s), r(s′)). ∎

**Consequences and requirements.**
- Pinning yields a continuum of world-3 acceptances C_i(s′) ⪯₃ C_{i+1}(s). None of them forms a triangle with forced verdicts (a return path at world 3 needs four steps). So pinning alone creates no kill.
- Within one cycle, Prop 2.2 fixes the class-3 A-region. Across cycles nothing forces this, but the segment family keeps the common bottom v₃, so every member of every cycle has T's class-3 A-region.
- Each requirement of §4 (R1–R3) must hold **uniformly** along s, with closed sections for every fixed measurable rival. The defence device of §4 must in addition have closed acceptance sets in p.

**CHECKED (cycle71d.out; two cycles λ = 1/5 and λ′ = 11/50; exact joint census, 75 cells after the piece/rest split).** For each of the eight models the fills are: each bounded piece, all bounded pieces together, each whole silent region, and the whole class-3 silence. That gives 248 models.
- D (both cycles' dominations): SAT.
- D + P (two-sided pinning, Lemma 5.2): SAT.
- D + P + N (also every same-cycle and cross-cycle diagonal refused at world 3): SAT.
- Forced under D + P + N: C_i(s′) ⪯₃ C_{i+1}(s) and C_i(s) ⪯₃ C_{i+1}(s′), exactly the pinning consequences. Same-position pairs C_i(s′), C_i(s) remain free at every world.

A larger run (cycle71d_frac_seed1.out; env FRAC2=0.4, SEED=1) adds a random 40% of the two-piece fills, for 591 models. D, D + P and D + P + N are all SAT.

**Correction of an earlier run.** A first version of this test, on the *sampled* census, returned D + P UNSAT. That census missed 13 of the 56 joint types, so that instance was not faithful, and the UNSAT is **withdrawn**.

**Stability of the joint census (CHECKED exactly at the sampled parameter pairs; census71b.out).** The joint type set of two segment cycles (λ, λ′) with λ < λ′ close has the same 56 types at six pairs:
- (1/5, 11/50) and (1/5, 2001/10000);
- (21/100, 211/1000), (1/4, 2501/10000), (29/100, 2901/10000) and (3/10, 3001/10000).

So the two-cycle cell instance is literally the same instance for all of them. At those pairs, the two-cycle verdict above therefore applies to every pair of neighbouring cycles in the family λ ∈ [1/5, 3/10]; for the remaining λ this is CONJECTURE. The family excludes λ → 0, where the segments degenerate to a point, and it never reaches the edge. It would be an **interior** construction, and the endpoint is not considered.

---

## 6. Relation to the round-57 construction

- **Admissible partners.** By Prop 2.2, T, N, every R_α, every J_β and L₀ share bottom v₃ and are admissible partners in a uniform cycle; no F_t with t > 0 is. A recurrent version of the T → N → L₀ part therefore needs further models **above v₃ but not on the F_t curve**: for example segments or polygons from v₃, as here, which are tightenings of N.
- **Guidance.** Keeping T ⪯₃ N as guidance (audit correction 1) is compatible with recurrence. Lemma 2.3 and Theorem 2.4 require only that **some** edge of each cycle be a non-guidance world-3 acceptance (PP68 Thm 4.4). In the explicit cycle every edge is non-guidance, since every pair is 3-mixed.
- **The price, by Theorem 2.4.** The constructor's certificate cannot be transitive at worlds 1 and 2 if any repair ever returns. Conversely, by Cor 2.5(b), a constructor who keeps PP67-type certificates is committed to an infinite chain that strictly improves at worlds 1 and 2. That chain must then be shown to coexist at accumulation points, which is the constructor's problem in Brief 57.

---

## 7. Scripts (`r9/PP71_py/`; run `python3 -I -B <script>.py` inside the folder; outputs in `<script>.out`; env PIECES=0 gives the V1 whole-region instance, ALLCOH=1 drops all coherence labelling)

| Script | Content | Label |
|---|---|---|
| `geom71.py` | Exact D_K advice and census helpers | — |
| `lib71.py` | Axiom encoding on a sub-universe, lazy (TC) with a full final check | — |
| `explore71.py` | Pointwise prerequisites of the explicit cycle, λ = 1/5 and 3/10 (exact census) | CHECKED |
| `census71.py`, `census71b.py` | Exact face census vs sampling; stability of the joint two-cycle census | CHECKED |
| `cycle71.py` | 4-cycle SAT and forced verdicts; 2-cycle UNSAT; 3-cycle SAT | CHECKED |
| `cycle71b.py` | Stress tests on larger sub-universes; tie-free and all-tie completions | CHECKED |
| `cycle71c.py` | Cycle with T present; consecutive splices dominated by members (outputs: V3 `cycle71c.out`, `cycle71c_allcoh.out`; V1 `cycle71c_v1_allcoh.out`) | CHECKED |
| `cycle71d.py` | Two neighbouring cycles with pinning | CHECKED |
| `cycle71f.py` | Splices per edge and jointly; greedy-minimal core (V1: `cycle71f_v1.out`; V3: `cycle71f.out`) | CHECKED |
| `cycle71h.py` | The V1 splice core embedded in the finer instance, with the other V1 splices as rivals | CHECKED |
| `cycle71e.py`, `cycle71g.py` | Exploratory diagnostics (one splice at a time; pinning cores); outputs partial or superseded, not cited | — |
| `compose71.py` | (T2) composition condition of Lemma 4.1 | CHECKED |
| `orders71.py` | All six cyclic orders on U₀ | CHECKED |
