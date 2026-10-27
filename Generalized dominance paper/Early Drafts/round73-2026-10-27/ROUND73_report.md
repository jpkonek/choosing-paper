# Round 73 report: consolidation gives a score-free dominance theorem

27 October 2026. The manuscripts are unchanged.

Agents:
- PRO73: prove dominance under consolidation.
- CEX73: refute it.
- MU73: dependence on μ, and whether consolidation is the integral in disguise.
- REF73: referee of PRO73 and MU73.
- DPR73: the margin version.
- REF73b: referee of the margin version.

Labels: PROVED means proved and refereed.

## 1. Main result: Theorem D′ (PROVED)

DPR73 and REF73 proved it independently, and REF73b refereed it line by line.

**Setting**
- Ω is any nonempty set.
- E ⊆ ℓ∞(Ω) is separable, norm-closed and contains 𝟙.
- μ is a finite measure on E with null indifference boundaries (M2), whose atomless part has full support. Atomless μ with (M3) is enough.
- (M1) is not used.
- Models are measurable sets of gambles modulo null sets.

**Consolidation with a margin.** Take three disjoint sets of gambles G₁, G₂, G₃ of equal measure, with a margin κ > 0: every gamble in G₃ pays at least κ more, at every world, than the sum of any gamble in G₁ and any gamble in G₂. (In the midpoint version, G₃ has twice the measure and beats the average.)

For a model W that contains G₁ and G₂ and misses G₃, its consolidation W′ is W with G₁ ∪ G₂ replaced by G₃.

**Axioms**

None of these refers to a score or an integral. μ enters only through null sets and the equality of three masses.
- **(G_E)** A non-null change guided at every world is strictly better at every world. This is implied by strict guidance.
- **(TC)** The three-model chain condition: there are no A ⪰ B ⪰ C with C ≻ A. This is implied by the full chain condition.
- **(TT)** Transitivity through ties: if Z is tied with X at ω and Y ⪰_ω Z, then Y ⪰_ω X.
- **(CAm)** Consolidation acceptance: W′ ⪰_ω W at every world.

**Theorem D′.** Under these four axioms, every incoherent model is dominated.

The dominator is obtained from the model by at most two consolidations, followed by at most one change guided at every world. It need not be coherent. The same holds on any open convex cone of gambles containing D_S.

**What the proof does not use:**
- maximality;
- independence;
- the admissibility premise;
- any score.

**Where the coherent class enters.** It enters only at the last step, through the paper's identification lemma and (M2). There, a model that cannot be consolidated, contains every uniformly positive gamble, and misses every uniformly negative one, is shown to be coherent.

**Sharpness**
- (M3) cannot be dropped. With μ on three small balls, every axiom holds and an incoherent model is undominated (CHECKED; exact LP check).
- (G_E) cannot be dropped (trivial).
- Whether (TT), the chain condition or midpoints can be dropped: UNCLEAR.

## 2. The class is nonempty for every set of worlds (PROVED)

The paper's ranking R0 (Definition 6.1) satisfies all of the following:
- reflexivity;
- strict guidance;
- independence;
- the chain condition;
- admissibility of every coherent model;
- (TT), trivially, since R0 has no ties between distinct models;
- (CAm), strictly at every world.

Why R0 satisfies (CAm): a margin consolidation adds only gambles in the coherent hull of what it removes, so no coherent model could make it, and it raises the integrated payoff at every world.

So, for every Ω, the class {reflexivity, strict guidance, independence, chain condition, admissibility of coherent models, (TT), (CAm)} is nonempty. In every member:
- the undominated models are exactly the coherent ones;
- every incoherent model is dominated.

Coverage requirements (1)–(4b) hold. Requirement (5), domination by an *undominated coherent* model, is OPEN for the class. It holds for R0, by the repair theorem.

Veto–Brier also satisfies (CAm) and (TT) on its domain.

The exact form of consolidation acceptance (CA) is violated by R0 whenever μ has an exact matched triple. That is why the margin form is the right one.

## 3. Status of the other questions

- **Maximality plus consolidation (OPEN).** No counterexample was found.
  - Ties with consolidations do not shelter an incoherent model, except possibly for one "staircase" shape (CEX73, Theorem G, PROVED).
  - Any ranking whose comparisons never lower the payoff can be extended to dominate (CEX73, Lemma A, PROVED).
  - A counterexample, if one exists, must be non-additive.
  - Theorem D′ makes this question unnecessary for the main result.
- **No strict defence (PROVED, MU73 and REF73).** Under the chain condition, guidance and margin consolidation, any model strictly defended against every rival is coherent.
- **Exact triples (CHECKED or PROVED, Gaussian).** They exist for Gaussian μ in every dimension. For general densities they exist in outline only. They are no longer needed.
- **Two-world score-free ranking (PROVED, with the corrected formula F).** R_GC, built only from guided and consolidation changes, is in the class with exact consolidation and protects every coherent model. With three or more worlds it is UNCLEAR. A margin variant works for two worlds.

## 4. Is consolidation the integral in disguise? (MU73, PROVED)

**No.** It mentions only:
- the linear structure of gambles;
- the pointwise payoff order;
- the equality of three masses.

**But it is the integral's motivation in qualitative form.** Among additive integral scores satisfying strict guidance, those passing exact consolidation are exactly a_ω∫h(ω)⁺ − b_ω∫h(ω)⁻ with b_ω ≥ a_ω > 0. These are loss-weighted payoffs, and they still give coherent optimal models. Whether the margin form admits exactly the same class was not checked separately.

**Plain-English motivation.** Accepting an amount of x together with the same amount of y pays, at every world, what accepting that amount of x + y pays. Pooling them into gambles that pay more than that, at every world, should never count as less accurate.

## 5. Corrections recorded

- Theorem S needed a fix for y = −x.
- In PRO73's Theorem D, step 5 had a wrong justification; it is repaired in REF73.
- In Proposition GC, use the single formula F = a·h₁⁺ − b·h₁⁻ + (1−b)·h₂⁺ − (1−a)·h₂⁻ for every Q ≠ S.
- In DPR73, the guided rival is X^D ∪ ((G₁∪G₂) ∩ D_S). The dominator uses at most two consolidations and then one guided change.
- REF73's Lemma U needs G₁ and G₂ chosen disjoint.
- Atoms must be kept out of triples.
- Drop the aside "C3p strict contains C3m".

## 6. Proposed next steps (for the author)

1. **Decide whether Theorem D′ becomes the central dominance result of the application paper.**
   - It would state the axioms and prove dominance for every ranking satisfying them.
   - The repair theorem would then serve two roles: it shows R0 is in the class, and it gives requirement (5) for R0.
   - This would replace Proposition 6.3, the maximality characterisation, as the justification of the ranking.
2. Settle requirement (5) for the class: is every incoherent model dominated by an undominated coherent one?
3. Check whether (TT) can be dropped, and whether three or more worlds admit a score-free member.
4. LDG: Theorem D′ is specific to sets of desirable gambles. LDG's abstract Proposition 7.1 is unaffected. An abstract analogue would need a notion of consolidation for general models, which is not proposed here.
