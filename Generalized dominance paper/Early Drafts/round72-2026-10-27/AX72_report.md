# AX72 report: three score-free principles tested against the distorted score

Round 72, 27 Oct 2026. Scope: the bounded search (Guidance §8, Auditor §4). I examine three principles, one for each of the auditor's gamble-structure headings:

- C1 uses the same aggregation at every world, combined with payoff order.
- C2 is gain–loss symmetry. This is the negation part of the linear structure.
- C3 is consolidation under addition and mixtures of gambles.

Scripts are in `r72/ax72_py/`: `checks.py` and `config.py`.

## Verdicts

| | Principle | Excludes R_{s'}? | R0 / round-71 maximal / veto–Brier (VB) | Plus the class: does every incoherent model get dominated in every maximal member? | Use of μ |
|---|---|---|---|---|---|
| C1 | Cross-world monotonicity | yes (PROVED) | yes / some but not all / yes (PROVED) | **NO** (counterexample E1, PROVED) | null sets only, any Ω |
| C2 | Gain–loss duality X ↦ −(E∖X) | yes (PROVED) | **violated** / violated / not applicable (PROVED) | **NO, and self-defeating**: with any imprecise coherent model admissible, an incoherent model is admissible in *every* such ranking (PROVED). For precise-only protected families: counterexample E2 (PROVED) | the statement needs reflection-invariant null sets; score examples need μ symmetric |
| C3 | Consolidation, chain form (sums C3a, midpoints C3b) | yes (PROVED, NUMERICS) | yes / yes (all) / yes (PROVED) | **OPEN**. The direct (non-chain) form fails (E3, PROVED). Either clause alone fails (E4, E5, PROVED). The joint chain form removes every *strict* defence of an incoherent model (PROVED in outline), but it supplies no strict preferences | **beyond null sets**: exact μ-preserving pairings. Pairings are proved to exist for rotation-invariant μ on R²; for general μ this is unproved |

Bottom line:

1. **Same aggregation across worlds does not help.** Distort every world in the same way and the counterexample survives intact (E1).
2. **Gain–loss symmetry is the wrong fix.** It is exactly what the auditor's f violates, but it contradicts imprecise admissibility outright. R0 itself violates it.
3. **C3 is the only candidate that addresses the actual defect.** That defect is that the distorted score rewards splitting a commitment into pieces whose payoffs add up to the same thing.
   - In the test family, C3 is equivalent to the per-world densities being superlinear: superadditive and positively homogeneous. That forces every Bayes set to be a convex cone.
   - Score-free, it kills the counterexample *mechanism*: an incoherent model can no longer be strictly preferred to every rival somewhere, either directly or through chains.
   - It is **not** a dominance theorem. C3 only forbids strict preferences, so maximal members can still leave an incoherent model undominated through ties or incomparabilities. I found neither a proof nor a counterexample.
4. **A nearby result is available now (C3.7).** Under the class axioms plus C3, every model with a strict defence against every rival is coherent. The open step is from "no incoherent model is strictly defended" to "every incoherent model is dominated in every maximal member".

---

## 0. Common tools

**Test family and construction R_g (from the brief).** Two worlds, E = R², μ the standard Gaussian. For truth-directed densities g_ω (sign g_ω(h) = sign h_ω, continuous, |g_ω(h)| ≤ c‖h‖), put s_ω(X) = ∫_X g_ω dμ.

At world ω, R_g accepts a non-null change iff it strictly raises s_ω. The one exception: a *dangerous* change (some coherent model could make it, and it raises s at both worlds) is refused at exactly one world, where it is not guided. Such a world exists because, with two worlds, a dangerous change is non-guided at both (round-71 R3). Null changes are accepted.

R_g satisfies (R), (G), (I) and (P) for all coherent models. It satisfies (SC) because every accepted non-null change strictly raises s_ω. This is the brief's argument; it does not depend on g. For each candidate below I fix the refusal world so that the candidate holds.

**Bayes fact.** Let X* be the a.e.-unique maximiser of Σ p_ω s_ω, so X* = {Σ p_ω g_ω > 0} with a null zero set.
- For every rival Y, the change Y→X* raises s at some world.
- Each change is refused at at most one world, and it is refused only if it raises s at both.
- So X* is strictly preferred to Y at some world.

**Defence lemma (PROVED).** Let R satisfy (SC). Say X has a *strict defence at ω against Y* if R contains a chain X ⪰_ω X₂ ⪰_ω … ⪰_ω Y with at least one strict link. (One step means X ≻_ω Y.)

If X has a strict defence against every rival at some world, then X is undominated in every E-strict extension of R that satisfies (SC). Proof: adding Y ⪰_ω X closes the chain into a cycle. The strict link survives, because E-strict extensions keep strict preferences. Rotating the cycle to start just after that link gives a forbidden chain.

If the candidate C is preserved under unions of chains of rankings, then for finite Ω Zorn's lemma gives a maximal member of 𝓡∩C above R. (P) is preserved under such unions because the strictness of a domination is already visible at the stage where its weak comparisons appear.

So **a counterexample to "C + class ⇒ dominance in every maximal member" is a ranking in 𝓡∩C in which an incoherent model is strictly defended against every rival.** All three candidates are preserved under chain unions:
- C1 is a closure condition on single comparisons;
- C2 is a biconditional on single comparisons;
- C3 forbids certain finite chains with a strict link, and any such chain lies in some stage.

---

## C1. Cross-world monotonicity (same aggregation plus payoff order)

**1. Motivation.** Suppose world ω′ is at least as kind as ω to everything a change adds, and at least as harsh as ω to everything it removes. Then if ω judges the change an improvement, so should ω′. Worlds may differ in which gambles pay; they should not differ in how they weigh what they see.

**2. Statement.** For worlds ω, ω′ and models X, Y with A = X∖Y and B = Y∖X:
if X ⪰_ω Y, h(ω′) ≥ h(ω) for a.e. h ∈ A, and h(ω′) ≤ h(ω) for a.e. h ∈ B, then X ⪰_{ω′} Y.

This needs only null sets, any Ω, and no symmetry.

**3. R_{s'} violates it (PROVED).** Let B = B₁ ∪ B₂, where B₁ is a small ball about (−1, −1.2) of mass 1.1m and B₂ a small ball about (1, 0.9) of mass m. Both lie in {h₂ < h₁}. Take X = Y∖B.
- World 1: the increment is ≈ 1.1m − m = 0.1m > 0. The change does not raise world 2, so it is not dangerous, and it is accepted at world 1.
- World 2: the increment is ≈ 1.1m·0.6 − 1.8m = −1.14m < 0, so it is refused.

The hypotheses of C1 for ω = 1 and ω′ = 2 hold, so C1 is violated.

In the local test family g_ω(h) = f_ω(h_ω), C1 forces f₂ = c·f₁ (PROVED). The proof uses diagonal point-pairs to get f₂ = c_± f₁ on each sign. Mixed-sign removals or additions, as above, then force c₊ = c₋. **C1 forces a common shape, not linearity.**

**4. Covering constructions.**
- **R0 satisfies C1 (PROVED).** If acceptance is by guidance at ω, the hypotheses make the change guided at ω′. If it is by clause (ii), then m_{ω′} ≥ m_ω > 0, and availability does not depend on the world.
- **VB satisfies C1 (PROVED).** v_j·h − v_i·h = ε(h_j − h_i). So the veto increment at j is no worse than at i, and the Brier increment at j is no worse either. Lexicographic acceptance carries over.
- **Round-71 maximal rankings: some satisfy C1, some do not (PROVED, finite Ω).** Fix a change. The hypothesis relation "ω → ω′" is a preorder on worlds. The guided worlds are upward-closed in it, so a dangerous change has a minimal non-guided world. Refusing there satisfies C1; refusing at a non-minimal world violates it. R∩ satisfies C1.

**5. Not enough: counterexample E1 (PROVED; NUMERICS for the arithmetic).**
- Set g_ω(h) = f(h_ω) with the auditor's kinked f at *both* worlds, and p = (½, ½). Then X*₁ = {f(h₁) + f(h₂) > 0}.
- a = (−7/2, 1) and b = (1, −7/2) give F(a) = F(b) = 1/4 and F(a+b) = −5/2. These are strict, so X*₁ is incoherent on neighbourhoods.
- Refusal rule for a dangerous r: if all of A lies in {h₂ ≥ h₁} and all of B in {h₂ ≤ h₁}, refuse at world 1. If the reverse holds, refuse at world 2. Otherwise refuse at world 1. Both conditions cannot hold for a non-null r.
- C1 then holds. If r is accepted at ω and satisfies the hypotheses toward ω′, then r is not refused at ω. So r is not dangerous, or it would have been refused at ω. And d_{ω′} ≥ d_ω > 0, because f is common and increasing.
- By the Bayes fact and the defence lemma, X*₁ is undominated in a maximal member of 𝓡∩C1.

**Verdict: insufficient.** The defect is not that worlds aggregate differently. It is that each world weighs gains and losses non-linearly.

---

## C2. Gain–loss duality

**1. Motivation.** A model makes two kinds of error: accepting a loser and failing to accept a winner. Write X^♯ = −(E∖X), the model that accepts h exactly when X does not accept −h. Gain–loss symmetry says the ranking should weigh the two kinds of error alike. Under it, "accept h" and "do not accept −h" carry the same accuracy content. Linear scores with a symmetric μ satisfy s_ω(X^♯) = s_ω(X). The auditor's f is exactly a violation of this: gains count four times as much as losses.

**2. Statement.** X ⪰_ω Y ⟺ X^♯ ⪰_ω Y^♯. The change Y^♯ → X^♯ adds −B and removes −A. The statement needs μ and its reflection to have the same null sets, which holds for Lebesgue-equivalent μ.

**3. R_{s'} violates it (PROVED).** Take A = balls of equal mass m about (−1, 1) and (−1, −1), and the change that adds A.
- World 2 increment: 2m − m/2 > 0. World 1 increment: −2m. So the change is not dangerous and is accepted at world 2.
- The dual change removes −A. Its world-2 increment is −(f(1) + f(−1))m = −1.5m, so it is refused.

In the test family with symmetric μ, C2 forces each g_ω to be odd.

**4. Covering constructions.**
- **R0 violates C2 (PROVED, NUMERICS).** Let Q = conv{(.8,.2), (.2,.8)} and let A be small balls about (2, −1) and (−1, 2) with equal mass.
  - P_Q = −0.4 at both centres, so D_Q could make the change that adds A.
  - The change is not guided at either world, so R0 refuses it at both.
  - The dual removes −A. −A is inconsistent: it would need p ≤ 1/3 and p ≥ 2/3 at once. So no coherent model could make the dual. Its score is m·(1, 1) > 0 for symmetric μ, so R0 accepts it at both worlds.
- **Round-71 maximal rankings violate C2.** Same change: they refuse it at one world and accept the dual at both.
- **VB: not applicable.** ♯ does not preserve the domain U.

**5a. Self-defeat (PROVED; uses (M3)).** If the ranking satisfies C2 and an imprecise coherent D_Q is undominated, then D_Q^♯ is undominated, because ♯ preserves every world's relation and hence dominance. And D_Q^♯ = {h : max_{q∈Q} q(h) ≥ 0} a.e. is incoherent:
- pick q₁ ≠ q₂ in Q and k with q₁(k) = 1 and q₂(k) = −1;
- then k − c𝟙 and −k − c𝟙 lie in its interior for small c > 0, and their sum −2c𝟙 lies in the interior of the complement;
- Lemma 2.3(a) turns this into a.e. incoherence.

So C2 together with the admissibility of even one imprecise coherent model contradicts the objective, under every ranking and not only maximal ones. This holds for the target-relative premise too, whenever the protected family contains an imprecise model.

**5b. Precise-only protected families: counterexample E2 (PROVED, NUMERICS).**
- Let f(t) = t for |t| ≤ 1 and 2t − sgn t otherwise. It is odd, increasing, and its weights lie in [1, 2].
- Use f at both worlds with p = (2/3, 1/3), so X*₂ = {2f(h₁) + f(h₂) > 0}.
- h = (−2, 3.6) gives F = 0.2 > 0, while h/4 gives −0.1. So X*₂ is not a cone and is incoherent.
- Refuse a change at one world when it or its dual is dangerous. Use the C1 rule for which world, which is ♯-invariant because the hypothesis relation is the same for r and r^♯.
- This ranking satisfies C1 and C2 together, protects all coherent models, and leaves X*₂ strictly defended against every rival.

**Verdict: reject.**

---

## C3. Consolidation: sums and mixtures (chain form)

**Definitions.** A *matched triple* consists of three pairwise disjoint non-null models G₁, G₂, G₃ and bijections T: G₁ → G₂ and S: G₁ → G₃, with T_*(μ|G₁) = μ|G₂ and one of:
- (sum) S(h) = h + T(h) and S_*(μ|G₁) = μ|G₃;
- (midpoint) S(h) = (h + T(h))/2 and S_*(μ|G₁) = ½ μ|G₃.

For a model Z containing G₁ ∪ G₂ and missing G₃, its *consolidation* is Z′ = (Z∖(G₁∪G₂)) ∪ G₃.

**1. Motivation.** Read μ as "how much each gamble counts". Then holding the matched pieces h and T(h) pays exactly what holding h + T(h) pays, at every world and gamble by gamble. In the midpoint case it pays what two units of their average pay. A ranking should not reward fragmenting a commitment into pieces that add up to the same payoff. (SC) already treats chains of comparisons as binding, so fragmentation should not be reachable by an improving chain either.

**2. Statement (C3).** At no world is there a chain Z ⪰_ω Z₂ ⪰_ω … ⪰_ω Z′ with a strict link. C3a and C3b are the sum-only and midpoint-only versions. The *direct form* C3⁻ only says that Z ≻_ω Z′ never holds.

μ enters beyond null sets, through exact μ-preserving pairings. Justification: μ already fixes what counts as the same amount of gambles. A pairing is a like-for-like substitution, not a score.

**C3.1 Triples exist (PROVED for the standard Gaussian on R²; NUMERICS).** Work in polar coordinates.
- Let T map (r, φ) to (τ(r), φ + θ(r)) and S map (r, φ) to (σ(r), φ + β(r)).
- τ and σ preserve the radial law (by the inverse-CDF construction), and each circle is only rotated. Both maps therefore preserve μ.
- θ(r) solves |r + τ(r)e^{iθ}| = σ(r) (respectively 2σ(r)). This can be solved near r₀ whenever |x|, |y|, |x+y| form a non-degenerate triangle, that is, whenever x and y are not collinear.
- Numerics (`config.py`): near a = (−1.5, 1), b = (1, −1.5), the Jacobian identities hold to 2·10⁻⁹ for both the sum and the midpoint versions.
- For general μ, existence near prescribed points is plausible (a PDE problem) but unproved. **Flag: C3 has force only where μ has enough of these triples.**

**3. R_{s'} violates C3a and C3b, even in the direct form (PROVED, NUMERICS).** Take the triple near (a, b, a+b), or near (a, b, (a+b)/2) for midpoints. The splitting change Z′ → Z has:
- world-1 increment exactly 0, because payoffs at world 1 are linear and the pairing is exact;
- world-2 increment ≈ +1.49 μ(G₁), which is μ(G₁)·[f(1) + f(−3/2) − f(−1/2)] for sums.

So the change is not dangerous and is accepted at world 2. Its reverse is refused there, so Z ≻₂ Z′.

**4. Covering constructions (PROVED).**
- **R0, R∩ and every round-71 maximal ranking satisfy C3.** Every accepted non-null change strictly raises m_ω. Splitting has m-increment exactly 0. So no chain with a strict link runs from Z′ up to Z. (The splitting change is also never guided.)
- **VB satisfies C3.** The veto [−v·h]⁺ is sublinear, so consolidation never raises the veto, and the Brier part is linear. So split ⪯_i consolidated in a total preorder, and transitivity rules out a strict chain.

**C3.5 The direct form is insufficient: counterexample E3 (PROVED).** Let R̃ be R_{s'} with every splitting change (sum or midpoint) refused at both worlds.
- R̃ satisfies C3⁻ and stays in 𝓡: refusing more keeps (P), (SC) and (I), and splitting changes are never guided.
- X* keeps a strict *chain* defence against each consolidation rival. Every splitting change (A, B) has μ(A) = 2μ(B) (sum) or μ(A) = μ(B) (midpoint).
- So route through W = Y ∪ K or W = X*∖K, where K is a tiny ball of positive gambles and μ(K) ≠ μ(B). The step involving K alone is guided at every world, and the other step is no longer a splitting change.
- Both steps strictly raise s′ at some common world. If the second step is dangerous, use the world where it is not refused.
- The defence lemma applies. **So the principle must be stated for chains.**

**C3.6 Each clause alone is insufficient (PROVED, NUMERICS).**
- **E4 (C3a only).** Use f(t) = 2t − |sin t| at both worlds.
  - It is superadditive (gap ≥ 0 on 2·10⁵ random pairs; analytically, |sin(x+y)| ≤ |sin x| + |sin y|), strictly increasing, and its weights lie in [1, 3].
  - X* = {f(h₁) + f(h₂) > 0} contains h = (π + 0.3, −π) but not h/2. So it is not a cone and is incoherent.
  - R_g has no strict chain from a consolidated model to its split, because every chain raises s and splitting does not. With the C1 refusal rule it also satisfies C1.
- **E5 (C3b only).** Use g(t) = min(t, (1+t)/2) at both worlds. It is concave, so it respects midpoints, and its weights lie in [½, 1]. X* contains (−1, 1.01) but not 10× that point.

**C3.7 What the joint chain form does (PROVED in outline).**
- **(i) Test family.** For continuous truth-directed densities and Gaussian μ, R_g satisfies C3 iff every g_ω is superlinear.
  - (⇒) Use C3.1 near every non-collinear pair. A positive splitting increment at some world gives a direct strict splitting preference: the change is refused at most at one world, and only when it raises both. So each g_ω is superadditive and midpoint-concave, hence concave by measurability. Concave plus superadditive with g(0) = 0 gives positive homogeneity.
  - (⇐) is the chain argument of item 4.
  - Then every Bayes set {Σ p_ω g_ω > 0} is an open convex cone that contains D_S and misses the non-positive gambles, so it is coherent. **The distorted-score technique is closed off entirely.**
- **(ii) Score-free.** Let R ∈ 𝓡 satisfy C3, and let X have a strict defence (at some world) against every rival. Then X is coherent.
  1. X must contain D_S and miss the non-positive gambles a.e. Otherwise the guided rival is strictly better at every world, and (SC) forbids a defence against it.
  2. Suppose X has density points x, y (not collinear) with x + y, or (x + y)/2, a density point of the complement. Intersecting small polar sectors with X, T⁻¹X and S⁻¹(E∖X) gives a matched triple inside X with its sum outside X. The consolidation rival is then exactly a model against which C3 forbids a defence.
     - Consolidation changes are never available to coherent models, which are a.e. closed under matched sums. So no protection-based shield is involved.
  3. Otherwise X is a.e. closed under sums and midpoints, contains D_S and misses the non-positive gambles. So it is a.e. an open convex cone, hence coherent.

  Steps 1 and 2 are PROVED. Step 3 is checked for models a.e. equal to open sets with null boundary; the general measurable case is a routine density-point argument but not written out (CONJECTURE-level care).

**C3.8 Dominance in every maximal member: OPEN.** C3 removes strict defences, but it never makes a consolidation strictly better. An incoherent X can still survive a maximal member in two ways:
- (a) through ties with its consolidations, which C3 allows; closure under ties is not assumed;
- (b) through incomparabilities that cannot be resolved because of other contexts. By independence, accepting a change at ω means accepting it in every context. One context may block the consolidation (a chain of ties from split to consolidated, with the consolidation not accepted directly), while another blocks the splitting (a strict chain from consolidated to split).

This is the extension-lemma gap of Guidance §6 again, now isolated. No counterexample was found. Every test-family counterexample is excluded by C3.7(i). Non-additive (lexicographic or finitely additive) rankings were not searched.

---

## 4. The four ingredients, kept separate

- **Pointwise payoff order.** R_{s'} satisfies it (f is increasing). On its own it does nothing. In its cross-world form (C1) it forces a common shape only.
- **Same aggregation across worlds.** Insufficient (E1). The world-permutation-symmetry version needs a symmetric μ and E. The symmetric distortion with p = (0.9, 0.1) defeats it (CHECKED, not written in full):
  - Equivariance forces a change that the swap maps to itself to be refused at both worlds, which breaks the strict defence.
  - But X*_p ∩ σX*_p is a coherent cone (rays (2.25, −1) and (−1, 2.25), an angle of 138°). So the reverse of every such change into X*_p is available to the hull of what the change adds, and protection forbids accepting it at both worlds.
- **Positive scaling.** It cannot be stated at the level of sets for a finite μ with positive continuous density. For the Gaussian, an exact μ-preserving dilation h ↦ λh with λ ≠ 1 exists only on a circle, which is null. It is also not needed: in the test family, C3a and C3b together imply homogeneity.
- **Addition and mixtures (C3).** The only ingredient that touches the defect. Both clauses are needed, and the chain form is needed.

## 5. Recommendation

Do not adopt C1 or C2.

Adopt C3 (chain form) only as a candidate, with its μ-dependence stated: it uses μ-preserving pairings and has force only where pairings exist.

The nearby result that is reachable now is C3.7(ii): **under the class axioms plus C3, no incoherent model is strictly defended against every rival.** This exactly defeats the auditor's mechanism and every distorted-score variant of it.

To reach the stated objective, one more ingredient is needed: a score-free reason why maximal members cannot shelter an incoherent model behind ties or context-blocked incomparabilities. Two options:
1. Assume tie-closure, in the paper's sense (3), as an explicit, separately labelled axiom. Then test whether, together with C3 and maximality, it yields the extension lemma.
2. Settle for "no strict defence" as the score-free theorem, and keep maximality-based dominance as a conjecture.

I have not checked whether option 1 suffices.

## Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r72/ax72_py/checks.py`: the incoherence witnesses for E1, E2, E4 and E5; the superadditivity, concavity and weight bounds; and R0's violation of C2.
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r72/ax72_py/config.py`: exact matched triples for the Gaussian (Jacobian check) and the splitting increments of R_{s'}.
