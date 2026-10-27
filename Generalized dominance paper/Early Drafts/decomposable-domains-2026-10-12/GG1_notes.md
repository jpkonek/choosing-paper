# GG1 (round 35, BRIEF27). A cover of T1 by NA-credal worlds: the construction tried, where the real intersection proof breaks, and the obstruction that kills the credal repair of VB

18 Oct 2026. Rules of BRIEF13. Labels: **PROVED** (full argument here, one reader, not refereed; imports named with their recorded status), **CHECKED** (exact rational computation, `gg1py/gg1_checks.py` → `gg1_checks.out`, run with `python3 -I`), **NUMERICS**, **CONJECTURE**. No assumption is added: every hypothesis below is either an axiom of a cover or part of the definition of the subclass being examined, and is named as such.

Domain: the U-domain M_U of the write-up §2.5 (U = D_{K'}, K' = u + s(T1 − u), 0 < s < 1). Reason for this choice: it is VB's domain, (LF) at T1 holds with N = U, every pair has advice range {+, 0}, and each world order is an order on error sets E_k(X) = X △ (U ∩ {h_k > 0}). Nothing below is claimed for the two-sided domain.

---

## 0. Outcome

**No cover of T1 was obtained. The construction attempted (the "credal veto–Brier" family: VB with each world's single veto replaced by a credal family of vetoes and tie-breakers, §1) fails, and the failure is a theorem (Theorem 3.3, PROVED modulo the intersection theorem).** Along the way the brief's three questions get exact answers.

1. **Competitiveness is selection-wise (Lemma 2.1, PROVED).** In an NA-credal ranking, C_q is competitive on J iff, for every choice σ of one member per world of J, no model is strictly better than C_q under σ_i at every i ∈ J. So credal spread makes competitiveness *harder* (more selections) and closed sections *easier* (sections are intersections).

2. **Where the real intersection proof breaks (§2, PROVED).**
   - Step 2 survives for finitely many members (ψ = Σ_k L^k is G-valued, strictly guiding, and strictly-transferring); it breaks only for infinite families, where no G-valued mixture exists.
   - **Step 5 breaks irreparably (Lemma 2.2).** There is a two-world, two-level additive system on a non-atomic space (one member per world) in which a model is competitive but is Bayes at **no** weight, real **or** non-Archimedean (Hahn). The attainable set is convex over ℝ only; separating it from the lex-negative orthant sees only the leading coordinates. CHECKED.
   - Step 6 then has nothing to act on.
   - So T1 need not be Bayes for anything: a cover may rest on competitiveness without scalarisation. This is the break a construction can exploit.

3. **Credal spread removes the closed-section rigidity of L3.4 / FF2 Lemma 2.4 (Lemma 2.3, PROVED).** A blind strict improvement at p forces only *Pareto*-stationarity of the members' leading levels along the selection at p, not local minimality of one leading level.

4. **But it cannot repair VB (Proposition 3.1 and Theorem 3.3, PROVED).** For two-level members with uniformly integrable, uniformly strictly guiding second levels:
   - **No upward jump (Prop 3.1).** If selected models approaching p pay no leading cost at world k, and world k has a common leading-blind set on which their limit is k-correct, then closed sections at world k force C_p to pay **zero** leading cost at world k under **every** member. The test model is a blind worsening of the limit, so credal spread is irrelevant to this mechanism.
   - **Theorem 3.3.** Consider any NA-credal ranking on M_U of this two-level kind in which T1 and every interior selected model pay no leading cost at any world (VB's plateau property, which is what lets vetoes protect T1). Suppose also that every limit at e_j of interior selected models has e_j in its credal set (true for VB, for the posterior family and for every selection with q ∈ K_q). Then every world's leading levels vanish on the whole mixed part of U. Each world is then a real intersection of strictly guiding integrable additive rankings, and the intersection theorem excludes it.
   - Hence **every credal repair of VB, and more generally every NA-credal design in which the leading order is a veto system that T1 and the interior selection respect, is impossible.**

5. **What survives (§4).** An NA-credal cover of T1 of the two-level kind must have **interior selected models (or T1) paying a positive leading-order cost at some world**: the leading order must vary along the selection in the interior. There Lemma 2.3 replaces L3.4: at every interior p where a blind improvement exists, the members' leading costs must be Pareto-stationary along the selection.

**Single most important open point.** Is there a two-level NA-credal cover in which the leading order varies along the interior selection (so that T1 or interior C_q pay leading costs), with the members' leading costs Pareto-stationary at every interior index (Lemma 2.3), and with T1 competitive for every member selection (Lemma 2.1) without being Bayes (Lemma 2.2)? Theorem 3.3 shows this is the only place left for two-level NA-credal covers.

---

## 1. The class and the construction tried

### 1.1 NA-credal worlds on M_U

- On M_U a member L in the record sense, valued in an ordered abelian group G, is L(X) = λ(E_k(X)) up to an additive constant, where λ is a G-valued finitely additive set function on measurable subsets of U, vanishing on null sets.
- Strict guidance of L is λ(E) > 0 for every non-null E.
- World k is X ≼_k Y iff L(X) ≤ L(Y) for every L ∈ Π_k.
- Strict (G), (IB) and transitivity are automatic (BRIEF27).

**Two-level uniform class (U2).** G = ℝ² with the lexicographic order, written a + εb. Each member of Π_k is

  L(X) = Φ^L(X) + ε Ψ^L(X), Φ^L(X) = ∫_{E_k(X)} ρ^L dμ, Ψ^L(X) = ∫_{E_k(X)} σ^L dμ,

with:
- ρ^L ≥ 0 integrable and supported in the mixed part M of U (the leading level charges mixed problems only);
- one integrable H and one η > 0 a.e. on U, common to all members of Π_k, with η ≤ σ^L ≤ H.

Each member is strictly guiding (σ^L > 0), and ρ^L may vanish on non-null sets (the "blind" leading levels required by L4/Q3.25). The **leading cost** of X at world k under L is Φ^L(X), and X **pays** it if Φ^L(X) > 0. The **common leading-blind set** of world k is Z_k := {h ∈ U : ρ^L(h) = 0 for every L ∈ Π_k} (an essential intersection, attained by a countable subfamily).

VB (L3 §3) is in (U2) with one member per world:
- ρ_k = |v_k·h| 1[v_k·h < 0] (the veto beyond F_k);
- σ_k = |h_k| (Brier).

The uniform envelope holds on M_U for the Gaussian μ, and η = |h_k| > 0 a.e.

### 1.2 The construction tried: credal veto–Brier

VB satisfies every axiom except closed sections at boundary indices (L3.3(c)). Its failure has a precise shape:
- an edge model C_p, p ∈ (e_i, e_j), must accept a.e. h ∈ U with h_i, h_j > 0 (competitiveness on {i, j} with strict (G));
- that set contains P_k := U ∩ {h_i > 0, h_j > 0, v_k·h < 0}, which lies beyond the middle arc of F_k and is non-null;
- so C_p pays world k's veto, while interior models, which avoid every B_m = {v_m·h < 0}, pay nothing.

The plan was to keep VB's selection on int Δ (C_q = D_{co(T1 ∪ {q})}, T1 a plateau on q ∈ T1), and to replace each world's single member by a family. The family contains:
- vetoes on sub-regions V^α ⊆ B_k, sized so that for every member selection σ the unvetoed beyond-facet region lies in {w·h ≤ 0} for some w ∈ T1 (which is what T1's competitiveness requires, by Lemma 2.1 and Lyapunov–separation on the second level);
- second levels varying with α, chosen to make the world-k section of each boundary-failing model Y exclude a neighbourhood of p.

The design requirements of BRIEF27 are met in principle:
- the leading levels are blind off V^α;
- Π_k is genuinely credal, so no single veto is refined and L3.4 does not apply;
- Lemma 2.3 is satisfiable at interior indices, because interior models pay nothing.

Prop 3.1 shows that the repair at the boundary is impossible **whatever the family**. The obstructing test model is a worsening of the interior limit on the common leading-blind set, and no member can separate it. Theorem 3.3 turns this into an exclusion of the whole design class.

---

## 2. What changes when members are non-Archimedean

### Lemma 2.1 (competitiveness is selection-wise; PROVED)

Let every world be NA-credal and J ⊆ Ω. A model C is competitive on J iff for every σ ∈ ∏_{i∈J} Π_i there is no model X with σ_i(X) < σ_i(C) for all i ∈ J.

*Proof.* "C is competitive on J" reads: ∀X ∃i ∈ J ∀L ∈ Π_i, L(C) ≤ L(X). Its negation is ∃X ∀i ∈ J ∃L_i ∈ Π_i with L_i(X) < L_i(C) (the orders are total in G). Choosing the L_i is choosing σ. ∎

*Consequence.* Adding members to Π_i can only destroy competitiveness. It can only shrink sections, since S_i(X) = ⋂_{L∈Π_i} {q : L(C_q) ≤ L(X)}.

### Step 2 of the intersection proof (PROVED)

For a finite family (L^1, …, L^m) ⊆ Π_i, ψ := Σ_k L^k is a G-valued strictly guiding additive member. If X ≼_i Y and not Y ≼_i X, then ψ(X) < ψ(Y). So Step 2 transfers verbatim to finite families.

For infinite families no G-valued mixture is defined: an infinite sum in *ℝ or in a Hahn field need not exist. The real proof's countable dense subfamily therefore has no analogue. This is a genuine break, but by Lemma 2.2 it is not the decisive one.

### Lemma 2.2 (Step 5 breaks: competitive but Bayes at no weight, even non-Archimedean; PROVED, CHECKED)

There are:
- two worlds;
- a non-atomic measure space;
- one strictly guiding ℝ²-lex additive member per world;
- a model C that is competitive on {1, 2};

such that no weight w = (w_1, w_2) ≠ 0 with entries ≥ 0 in ℝ, nor in the Hahn field ℝ((ε)), makes C Bayes, i.e. satisfies w_1L_1(X) + w_2L_2(X) ≥ w_1L_1(C) + w_2L_2(C) for all X.

*Construction.* Take three disjoint non-null regions R_a, R_b, R_c, each with two advices "C's advice" and "switch". Let the value change of switching on a set of measure t be t·a, t·b, t·c respectively, with (world 1, world 2) and each entry in ℝ² written (leading, second):
- a = ((0, 1), (0, −1));
- b = ((0, −1), (0, 1));
- c = ((1, 0), (−2, 0)).

On R_a, R_b the leading levels are blind, and the switch is wrong at one world and right at the other at the second level. On R_c the switch is wrong at world 1 and right at world 2 at the leading level. Both members are strictly guiding.

*Proof.*
1. **The attainable set.** By Lyapunov, the set of value changes of models is the zonotope Z = {αa + βb + γc : α, β, γ ∈ [0, 1]}. It is convex over ℝ.
2. **C is competitive.** Write z = αa + βb + γc. Then z_1 = (γ, α − β) and z_2 = (−2γ, β − α). For both to be lex-negative we need γ ≤ 0, so γ = 0. Then α − β < 0 and β − α < 0, which is impossible.
3. **No real weight.**
   - The inequality at a gives (0, w_1 − w_2) ≥ 0, and at b gives (0, w_2 − w_1) ≥ 0. So w_1 = w_2 =: w.
   - At c it gives (w − 2w, 0) = (−w, 0) ≥ 0, so w = 0.
4. **No Hahn weight.** Embed ℝ²-lex as x + yε. For positive w_1, w_2 ∈ ℝ((ε)):
   - a gives (w_1 − w_2)ε ≥ 0 and b gives (w_2 − w_1)ε ≥ 0, so w_1 = w_2 = w;
   - c gives w − 2w < 0.
5. **The geometric reason.** The closure of the lex-negative cone in ℝ² is the half-plane {leading ≤ 0}. So any linear functional that separates Z from the product of lex-negative cones depends only on leading coordinates. Over a Hahn field, combinations with infinitesimal coefficients (e.g. γ = ε², α − β = −(3/2)ε) would dominate C. Splices of standard models realise only real coefficients. ∎

CHECKED (`check1a–c`):
- 0 of 2197 grid points of Z are lex-better at both worlds;
- no grid real weight supports a, b, c;
- no grid Hahn weight x + yε supports a, b, c.

*Reading.*
- In the real theorem, Step 5 turns competitiveness of D_K into "D_K is w-Bayes for the mixture", and Step 6 makes w interior. Here competitiveness gives only a leading-level weak Bayes weight (separation), which is degenerate wherever the leading levels are blind.
- Step 6 then fails, because strictness lives below the leading level.
- A cover may therefore exploit exactly this: T1 competitive through incomparable second-level trade-offs on leading-blind regions, without being Bayes for any member selection.

### Lemma 2.3 (closed sections under credal spread: Pareto-stationarity; PROVED)

Let world k be NA-credal, with members of class (U2) except that the envelope is not needed. Suppose its sections are closed. Let p ∈ Δ, and let A ⊆ Z_k be non-null with C_p k-wrong on A. Then there is no sequence q_n → p with Φ^L(C_{q_n}) < Φ^L(C_p) for every L ∈ Π_k and every n.

*Proof.*
- Let X be C_p corrected at world k on A. Every member has Φ^L(X) = Φ^L(C_p) (since ρ^L = 0 on A) and Ψ^L(X) < Ψ^L(C_p). So X ≺_k C_p, and p ∉ S_k(X).
- If such q_n existed, then L(C_{q_n}) < L(X) for every L at the leading level, so q_n ∈ S_k(X).
- Closedness then gives p ∈ S_k(X), a contradiction. ∎

*Comparison.* FF2 Lemma 2.4 (one leading functional refined by the world) forces local **minimality** of Φ(C_·) at p, hence constancy where continuous. Lemma 2.3 forces only that p is not approached from the region where **all** members' leading costs are strictly smaller. A single member L_p whose leading cost along the selection is minimal at p suffices, e.g. a member blind on E_k(C_p). This is the precise sense in which credal spread dissolves the L3.4 mechanism at interior indices.

---

## 3. The obstruction to the credal veto–Brier design

### Proposition 3.1 (no upward jump of leading cost at a limit of the selection; PROVED)

Let world k be NA-credal of class (U2) on M_U, and suppose all its sections {q : C_q ≼_k Y} are closed. Let p ∈ Δ and q_n → p (any indices) with C_{q_n} → C⁻ in measure, such that Φ^L(C_{q_n}) = 0 for every L ∈ Π_k and every n. Suppose there is a non-null A ⊆ Z_k ∩ M on which C⁻ is k-correct. Then Φ^L(C_p) = 0 for every L ∈ Π_k.

*Proof.*
1. **The test model.** Put Y := C⁻ △ A, which is in M_U since A ⊆ U. As C⁻ is k-correct on A, E_k(Y) = E_k(C⁻) ∪ A, a disjoint union.
2. **Leading levels.** For each L:
   - Φ^L(C⁻) = lim_n Φ^L(C_{q_n}) = 0, because ρ^L is integrable and E_k(C_{q_n}) → E_k(C⁻) in measure;
   - Φ^L(Y) = Φ^L(C⁻) + ∫_A ρ^L = 0, since A ⊆ Z_k.
3. **Second levels, uniformly in L.**
   Ψ^L(Y) − Ψ^L(C_{q_n}) = ∫_A σ^L + ∫_{E_k(C⁻)} σ^L − ∫_{E_k(C_{q_n})} σ^L ≥ ∫_A η − ∫_{C⁻ △ C_{q_n}} H.
   The last integral tends to 0 by absolute continuity, and it does not depend on L. Fix N with ∫_{C⁻△C_{q_n}} H < ∫_A η for n ≥ N.
4. **The sections.** For n ≥ N and every L, the leading levels of C_{q_n} and Y are both 0, and Ψ^L(C_{q_n}) < Ψ^L(Y). So L(C_{q_n}) < L(Y) for all L ∈ Π_k, that is, q_n ∈ S_k(Y).
5. **Conclusion.** Closedness gives p ∈ S_k(Y). So Φ^L(C_p) ≤ Φ^L(Y) = 0 for every L. ∎

*Why credal spread does not help here.* Y differs from the limit C⁻ only by a worsening on the **common** leading-blind set. Every member sees it at the second level, by a uniform positive amount, while every member sees C_{q_n} converge to C⁻ at both levels. So no member can exclude q_n from the section, and closedness transfers the leading-level comparison Φ^L(C_p) ≤ 0 to **every** member. Compare Lemma 2.3: there the test model is a blind *improvement* of C_p, and one member suffices to block. Here it is a blind *worsening* of the limit, and no member can block.

### Lemma 3.2 (limits of selected models; PROVED)

Every sequence of coherent models C_{q_n} = D_{K_{q_n}} in M_U has a subsequence with K_{q_n} → K⁻ in the Hausdorff metric. Along it, C_{q_n} → D_{K⁻} in measure, and D_{K⁻} is coherent and in M_U.

*Proof.*
- D_K ⊆ U a.e. forces D_K ⊆ U (both open convex cones), hence K ⊇ K′ (write-up Prop. reduction(a)).
- The K_{q_n} are compact convex subsets of Δ, so Blaschke selection gives a Hausdorff-convergent subsequence.
- P_{K_n}(h) → P_{K⁻}(h) for every h. The set {P_{K⁻} = 0} is the boundary of a convex cone, hence null, so the indicators converge a.e. (R1 Prop. 3.1; H12_referee §1.1). ∎

### Theorem 3.3 (PROVED, modulo the intersection theorem)

No ranking on M_U covers T1 if it satisfies all of the following:
- every world is NA-credal of class (U2);
- **(P0)** T1 and every interior selected model pay no leading cost at any world: Φ^L(T1) = Φ^L(C_q) = 0 for q ∈ int Δ, every world and every member;
- **(V)** for each j, every Hausdorff limit K⁻ of credal sets K_{q_n} of interior selected models with q_n → e_j contains e_j.

*Remarks on the hypotheses.*
- (P0) and (V) define the subclass. VB satisfies both: interior models avoid every B_m, and K_q = co(T1 ∪ {q}) ∋ q.
- (V) also holds for the plain posterior family, for every selection continuous in measure at the vertices (the limit is then B^j = D_{co(K′∪{e_j})}), and for every selection with q ∈ K_q.
- (P0) is exactly the property by which leading-level vetoes protect T1 while the interior selection moves at the second level, as in VB and its credal repairs (§1.2).

*Proof.* Fix a world i and j ≠ i.
1. **The vertex model.** Competitiveness at e_j on {j}, with strict (G), gives C_{e_j} = B^j := U ∩ {h_j > 0} a.e. (L3 §4, setting of Thm L3.4).
2. **A limit.** Take interior q_n → e_j. By Lemma 3.2 pass to a subsequence with C_{q_n} → C⁻ = D_{K⁻}. By (V), e_j ∈ K⁻.
3. **The blind set A.** Put A := T1 ∩ {h_i < 0, h_j < 0}, writing T1 for D_{T1}.
   - **A is non-null.** It is open and contains a neighbourhood of the point h of `check2a` (relabelled): for ε = 3/10, h = (−1, −1, κ + 1 + 1/10) has v_m·h = 7/300, 7/300, 703/525 > 0. The permutation symmetry of T1 gives the same for every pair (i, j). For general ε the same holds near the corner ray r_ij, inside the open cone D_{T1}.
   - **A ⊆ Z_i ∩ M.** A ⊆ E_i(T1), because T1 accepts there and h_i < 0. By (P0), ρ^L = 0 a.e. on E_i(T1) for every L ∈ Π_i.
   - **C⁻ is i-correct on A.** For h ∈ A, P_{K⁻}(h) ≤ e_j·h = h_j < 0. So C⁻ rejects h, which is i-correct since h_i < 0.
4. **No jump.** By (P0) each C_{q_n} pays no leading cost at world i. Proposition 3.1 at p = e_j (closed sections at world i, part of (S)) gives Φ^L(B^j) = 0, i.e. ρ^L = 0 a.e. on E_i(B^j), for every L ∈ Π_i.
5. **The leading levels vanish.** Apply step 4 to both j ≠ i. Every mixed h ∈ U lies in E_i(B^j) ∪ E_i(B^k):
   - if h_i < 0, some other coordinate is positive and that vertex model accepts h wrongly at i;
   - if h_i > 0, some other coordinate is negative and that vertex model rejects h wrongly at i.

   (`check2b`, all six mixed sign patterns.) Hence ρ^L = 0 a.e. on M. By (U2), ρ^L is supported in M, so Φ^L ≡ 0 for every L ∈ Π_i.
6. **Reduction to a real intersection.** World i is now X ≼_i Y iff Ψ^L(X) ≤ Ψ^L(Y) for every L ∈ Π_i. This is an intersection of strictly guiding additive rankings with the common integrable envelope H. This holds at all three worlds, and the ranking still satisfies (LA), (S), (C), (LF) at T1 and T1 ∈ C_L, all on M_U.
7. **Contradiction.** The intersection theorem (project doc *Intersections of Additive Rankings*, one reading; summary in INTERSECTIONS_additive.md) says no such intersection covers T1 on any decomposable domain with (LF). ∎

*Dependencies.*
- Used: closed sections at the worlds outside supp e_j; competitiveness at the vertices; strict (G); the intersection theorem (which uses (LA), (S), (C), (LF), T1 ∈ C_L and Theorem gm).
- Not used: (IB) beyond its automatic validity, Lemma 2.1, Lemma 2.3, edge competitiveness, T1's undominatedness except through the intersection theorem.

### Corollary 3.4 (the edge form; PROVED)

Under (U2) and (P0) alone (no (V)), let p lie in the open edge (e_i, e_j), and let C⁻ be a limit of interior selected models at p. Suppose world k's common blind set Z_k contains a non-null set on which C⁻ is k-correct; for example, a part of E_k(T1) on which C⁻ differs from T1. Then every member of world k charges nothing that C_p gets wrong at k. In particular ρ^L = 0 a.e. on P_k = U ∩ {h_i > 0, h_j > 0, v_k·h < 0}, since C_p ⊇ P_k.

So in this subclass no world can veto, at the leading order, acceptance beyond the middle arc of its own facet. *Proof:* Proposition 3.1 at p, with C_p ⊇ U ∩ {h_i, h_j > 0} by competitiveness on {i, j} and strict (G). ∎

*Reading.* T1's rejection of P_k (beyond the middle arc of F_k) cannot be protected by a veto at world k. Since accepting P_k is right at i and j, no other world can veto it either. The protection must then come from the second (integrable, strictly guiding) level, which is where Theorem gm's rigidity lives. Theorem 3.3 completes this by removing the leading levels altogether.

---

## 4. What survives, and the blueprint it leaves

**Proposition 4.1 (the residual for two-level NA-credal covers; PROVED from 3.3).** Every NA-credal cover of T1 on M_U of class (U2) satisfying (V) violates (P0). That is, T1 or some interior selected model pays a positive leading cost at some world under some member. ∎

What such a cover must look like:
1. **The leading order varies along the interior selection.** By Lemma 2.3, wherever C_p has a strict improvement inside the common blind set Z_k, the members' leading costs Φ^L(C_·) must not all decrease strictly along any sequence approaching p. A credal family can satisfy this with members whose leading cost is minimised at C_p, for example members blind on E_k(C_p). A single veto cannot.
2. **T1 is competitive for every member selection (Lemma 2.1) without being Bayes (Lemma 2.2).** The incomparable second-level trade-offs of Lemma 2.2 must live on leading-blind regions near ∂D_{T1}.
3. **No upward jumps (Proposition 3.1).** Whenever approaching selected models pay no leading cost, the limit index pays none either. Combined with 1, leading costs along the selection must be lower semicontinuous *and* Pareto-stationary at every index with a blind improvement.
4. **Consistency with earlier results.**
   - FF2 Cor 4.3 (non-additivity in the bulk) is met by two-level worlds with blind leading levels in the bulk: no integrable strictly guiding penalty endorses comparisons whose leading change is a small loss and whose second-level change is a large gain.
   - L4 (degenerate endorser field) is met by the common blind sets Z_k.

**Escapes from Theorem 3.3 not covered here** (each a different class):
- **(E1)** members with three or more levels, or non-uniform second levels. Proposition 3.1 needs a common envelope H and a common lower rate η at the level below the leading one. A family whose second levels degenerate across members, or whose blind-set second levels are themselves blind with strictness at a third level, can escape step 3 of its proof.
- **(E2)** selections violating (V), i.e. interior limits at e_j whose credal sets miss e_j.
- **(E3)** the two-sided domain.

**CONJECTURE 4.2.** Theorem 3.3 extends to finitely many levels with uniform bounds at every level, by applying Proposition 3.1 at the first level that is not blind on A, and to (E2) by choosing A inside E_i(C_q) for an interior q near e_k. Not attempted.

---

## 5. Status

| Item | Statement | Label |
|---|---|---|
| 2.1 | competitiveness in an NA-credal ranking ⟺ weak Pareto-optimality for every member selection | PROVED |
| Step 2 | strictness transfers to finite G-valued mixtures; no mixture for infinite families | PROVED |
| 2.2 | competitive model that is Bayes at no real or Hahn weight (two-level, two worlds, non-atomic) | PROVED; CHECKED |
| 2.3 | credal closed sections force only Pareto-stationarity of leading costs (vs FF2 Lemma 2.4) | PROVED |
| 3.1 | no upward jump of leading cost at a limit index, for every member, under (U2) | PROVED |
| 3.2 | compactness of selected models in M_U | PROVED (imports R1 Prop 3.1, H12_referee §1.1) |
| **3.3** | **no NA-credal (U2) cover of T1 on M_U with (P0) and (V); covers every credal repair of VB** | **PROVED**, modulo the intersection theorem (one reading) |
| 3.4 | under (P0), no world vetoes acceptance beyond the middle arc of its facet | PROVED (with the stated non-null-set hypothesis) |
| 4.1 | two-level NA-credal covers must violate (P0) | PROVED |
| 4.2 | extension to more levels and to (E2) | CONJECTURE |
| — | an NA-credal cover of T1 | **not obtained** |

**Referee priorities.**
1. Proposition 3.1, step 3: the uniformity in L, which is exactly where (U2) enters.
2. Theorem 3.3, step 3: that A ⊆ Z_i follows from (P0) at T1, and that e_j ∈ K⁻ gives rejection on A.
3. Lemma 2.2, step 5: that splices realise only real coefficients. This holds because the value of a splice is a vector-measure value, which is real-linear in the indicator.

## 6. Files

`gg1py/gg1_checks.py` → `gg1_checks.out` (exact Fractions):
- check1a–c: Lemma 2.2. The zonotope has no point lex-better at both worlds (2197 grid points), and no real weight (440 grid weights) or Hahn weight x + yε (grid) supports all three generators.
- check2a: a point of D_{T1} with h_1, h_2 < 0 (ε = 3/10), used for non-nullity of A in Theorem 3.3.
- check2b: every mixed sign pattern is a world-1 error of B^2 or B^3.
