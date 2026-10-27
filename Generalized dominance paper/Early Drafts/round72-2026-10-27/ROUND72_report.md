# Round 72 report: score-free maximality does not give dominance

27 October 2026. Agents: REF72 (referee of the counterexample), INC72 (inclusion branch), AX72 (score-free principles), REF72b (referee of INC72 and AX72). The manuscripts are unchanged.

Labels: PROVED means proved and refereed unless marked otherwise.

## 1. Assumptions statement (one page)

**Setting.**
- Worlds Ω.
- Gamble space E ⊆ ℓ∞(Ω), separable, with an order unit.
- Finite measure μ on E with null indifference boundaries (μ{P_S = 0} = 0 suffices for protection).
- Models: measurable sets of gambles modulo μ-null sets.
- Coherent model: equal a.e. to D_Q for a credal set Q.
- Change from Y to X: adds A = X∖Y and removes B = Y∖X. It is available to C iff B ⊆ C and A ∩ C is null.
- Guided at ω: A ⊆ {h(ω) > 0} and B ⊆ {h(ω) < 0}.
- Dominance (manuscript definitions): Y dominates X iff Y ⪰_ω X at every world, and the reverse fails at some world.

**Ranking class 𝓡** (one relation per world; no score, no integral):
- (R) Reflexivity. A.e.-equal models are tied.
- (G) Strict guidance. If X ≠ Y a.e. and the change Y→X is guided at ω, then X ≻_ω Y.
- (I) Independence. The verdict depends only on the change (A, B).
- (SC) Chain condition (Suzumura consistency). No chain X₁ ⪰ … ⪰ X_k with X_k ≻ X₁. It implies the three-model condition (TC).
- (P) Admissibility. Every model in a protected family 𝓟 is undominated.
  - The counterexamples use 𝓟 = all coherent models under one ranking, the strongest premise.
  - Any positive theorem must name 𝓟, which must contain the target.
- Closure under ties is not assumed. Where it is mentioned, it is stated in words.

**Extension notions.**
- Strict-preserving extension (Suzumura extension): keeps every weak and every strict comparison.
- Inclusion: keeps weak comparisons only, so strict comparisons may become ties.

**Objective tested.** Every incoherent model is dominated under every maximal member of 𝓡. The dominator need not be coherent or undominated.

## 2. Results

### 2.1 Counterexample under strict-preserving maximality (PROVED; REF72)

Setting:
- Ω = {1, 2}, E = R², μ Gaussian.
- s′₁(X) = ∫_X h₁ dμ.
- s′₂(X) = ∫_X f(h₂) dμ, where f(t) = 2t for t ≥ 0 and f(t) = t/2 for t < 0.

The ranking:
- At ω, accept a change that strictly raises s′_ω.
- Exception: a change that some coherent model could make, and that raises s′ at both worlds, is refused at one world where it is not guided.

Then:
- The ranking is in 𝓡.
- X* = {h₁ + f(h₂) > 0} = D_{(1/3, 2/3)} ∪ D_{(2/3, 1/3)}. This is a non-convex cone of about 217°, so X* is incoherent.
- X* is strictly preferred to every rival at some world.
- So every strict-preserving extension leaves X* undominated.
- For finitely many worlds, chain unions preserve every axiom, so maximal members exist above this ranking (Zorn).

**General form.** Take any n ≥ 2 worlds and any sign-respecting scores ∫_X f_ω dμ. Suppose some weighting π ≥ 0 has a Bayes set {Σ π_ω f_ω > 0} with a null zero set that is not a.e. a convex cone. Then the same conclusion holds.

The counterexample also defeats:
- (TC);
- the addition of closure under ties;
- every property shared by all maximal members, so any weaker substitute implied by this maximality fails too.

**Infinite Ω.** Existence of maximal members is open: a chain union can assemble a dominance relation across stages that no single stage contains. This does not rescue the objective, because the counterexample has two worlds.

### 2.2 Inclusion does not help either (PROVED; REF72b)

Let R₀′ be the manuscript's rule (Definition 6.1) with s′ in place of the integrated payoff. Then:
- R₀′ is in 𝓡.
- In **every** ranking in 𝓡 that extends R₀′, X* has no weak dominator.

So no extension principle that R₀′ can meet yields the objective, whether strict-preserving maximality, inclusion maximality or anything else. The obstruction sits in R₀′ itself.

**Entrenchment lemma.**
- Statement: above any ranking of the manuscript's form built from a sign-respecting integral score, every strict comparison stays strict in every extension satisfying (G) and (TC).
- Consequence: there, inclusion and strict-preserving extension coincide.
- Status: PROVED for μ with no atoms, any Ω. UNCLEAR if μ has atoms; (M1)–(M3) allow atoms.

**Philosophy.** Turning an established strict comparison into a tie retracts a verdict; it is not more decisive. We recommend closing the inclusion branch.

### 2.3 Positive counterpart: coverage is robust (PROVED for atomless μ; REF72b)

Let R be any ranking in 𝓡 that extends the paper's ranking. Every incoherent model is then strictly dominated at every world, by the same coherent model as before. That model remains undominated, by (P).

So requirements (1), (2), (4b) and (5) of "covers" survive every such extension. Closure under ties (3) is not shown.

This is a robustness theorem for the construction, not a score-free axiomatisation. The class is defined by containing a ranking built with the integral.

### 2.4 Score-free principles (bounded search; AX72, REF72b)

**C1. Cross-world monotonicity.** If ω′ is at least as kind as ω to everything added and at least as harsh to everything removed, then ω′ accepts what ω accepts.
- It excludes the counterexample.
- R0 and veto–Brier satisfy it.
- **Insufficient** (PROVED). The same kink at both worlds gives an incoherent model, {f(h₁) + f(h₂) > 0}, that is strictly defended against every rival. C1 forces a common distortion, not a linear one.

**C2. Gain–loss symmetry.**
- **Self-defeating** (PROVED). If any imprecise coherent model is admissible, its mirror image is incoherent and admissible.
- R0 violates it. Rejected.

**C3. Consolidation.** No improving chain leads from holding a gamble-sum, or two units of a midpoint, to holding matched pieces whose payoffs add up to the same thing.
- It excludes the counterexample.
- R0, R∩, every round-71 maximal ranking and veto–Brier satisfy it.
- Within the integral-score family, it forces every Bayes set to be a convex cone.
- Score-free, it gives a nearby result: no incoherent model is strictly defended against every rival. This is PROVED in outline; it has not been refereed in full.
- **Dominance is OPEN.** C3 only forbids strict comparisons, so ties or incomparabilities could still shelter an incoherent model.
- **Costs.**
  - μ enters beyond its null sets, through exact μ-preserving pairings.
  - Such pairings are proved to exist only for rotation-invariant μ.
  - The direct (one-step) form, and each clause alone, are defeated by counterexamples (PROVED).

## 3. What this settles

1. Maximal decisiveness alone cannot turn assumed coherent admissibility into incoherent inadmissibility, whether "maximal" means strict-preserving extension or inclusion. A sign-respecting scoring rule that distorts payoff magnitudes differently at different worlds satisfies every score-free axiom and defends an incoherent model.
2. The failure does not come from unresolved comparisons. It comes from comparisons the ranking already makes.
3. The defect a principle must address is that the ranking rewards splitting a commitment into pieces whose payoffs add up to the same thing. Same aggregation across worlds (C1) does not address it. Consolidation (C3) does, but at the cost of using μ beyond null sets, and dominance is still open.
4. What can be said positively, with exact scope:
   - the coverage theorems of the paper and of round 71;
   - robustness of coverage under every extension within 𝓡 (§2.3);
   - the counterexample as a theorem explaining why the integral, or some substitute that forbids splitting, is doing real work.

## 4. Options for the next step (decision for the author)

- (a) **Close the search.** Retain the construction-based results. Add the counterexample and the robustness theorem to the papers as the explanation of what the integral contributes.
- (b) **One bounded round on C3.** Try either to prove dominance under C3 plus a named closure principle, or to find a ranking satisfying C3 with an undominated incoherent model. Also settle C3's dependence on μ.
- (c) Both: (a) now, and (b) as a separate, time-limited investigation.

## 5. Corrections recorded

- The axiom (G) must exclude a.e.-equal models; otherwise the class is empty.
- In INC72 §2, the mirror case is valid because the score enters only through c > 0 and the smallness of g. Coordinate symmetry is not the reason.
- INC72's remark on incomparability in R₀′ holds only for consistent B meeting both S₁ and S₂.
- In §2.3, the dominator stays undominated, by (P).
- The entrenchment lemma needs μ to have no atoms.
