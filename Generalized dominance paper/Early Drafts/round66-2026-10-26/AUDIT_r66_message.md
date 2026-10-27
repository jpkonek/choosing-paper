**This is the breakthrough the programme needed.** The new result settles finite-world coverage for the stated full-dimensional targets, and the proof reveals a much simpler mechanism than the preceding constructions.

I reviewed the universal-coverage proof, both referees’ geometric arguments and the (Add) construction. I also worked through a simplification and a substantial infinite-world extension. **Those new audit arguments still need independent refereeing.**

**The core mechanism is “improve within the rival’s own commitments.”**

The crucial change is to begin with the coherent hull of the rival \(X\), rather than with the entire evaluable domain.

The proof then does two things:

1. **Find a coherent improvement inside that hull.** Minimax supplies a coherent model that improves Brier performance at every world.
2. **Trim it slightly without losing the improvement.** After trimming, the advice removed from \(X\) still generates its entire coherent hull.

Consequently, the new advice is already implied by the advice being removed. This makes the change impossible to apply to a coherent model: a coherent model accepting the removed advice would already accept the added advice.

That is why the improvement can be admitted without endangering any coherent model.

The referee’s identity
\[
\operatorname{hull}(X\setminus N)=\operatorname{hull}(X)
\]
is therefore more revealing than the original intersection condition (H). **The removed advice preserves the rival’s coherent commitments; the defender reorganises its actual acceptances into a better-performing coherent model.**

This is a general mechanism, not another special construction for triangles.

**The ranking can now be much simpler**

The strengthened theorem gives **strict** Brier improvement at every world. That makes the designated deletion world and the lexicographic tie-break unnecessary.

For a change from \(Y\) to \(X\), use this rule at world \(\omega\):

> Accept the comparison if it is guidance; otherwise accept it only if it strictly improves Brier performance at \(\omega\) and the change cannot be applied to any coherent model.

Include equality as usual.

“Cannot be applied” has the explicit hull test
\[
\mu\bigl((X\setminus Y)\cap
\operatorname{hull}(Y\setminus X)\bigr)>0.
\]

This is closely related to AD65’s plain-Brier variant, but we can omit its zero-score comparisons too.

The proofs become short:

- **(G):** guidance is included.
- **(IB):** the rule depends only on the disagreement.
- **(TC), and finite-chain consistency:** every accepted nontrivial comparison strictly improves one scalar score at that world, so an accepted cycle is impossible.
- **Protection:** a change out of a coherent model fails the hull test, so it can be accepted only through guidance. Guidance alone cannot dominate that coherent model.
- **Dominance:** the strengthened theorem supplies exactly the strict, safe improvement the rule accepts.
- **(Add):** adjoining a disjoint change cannot make a previously inapplicable change applicable to a coherent model; strict score improvements also add.

Thus **no lexicographic machinery is needed even to retain (Add)**. I would make this simpler rule the main construction.

**The infinite-world prospects are better than my previous assessment suggested**

The contraction argument behind the trimming step is essentially dimension-independent. Its content is that repeatedly mixing a probability with members of a closed credal set forces the limiting probability into that set. It does not depend on vertices, finitely many facets or finite-dimensional convex geometry.

The apparent obstacle is the initial minimax step. The published proof uses finite-dimensional Lyapunov to make the attainable moment vectors compact and convex.

There is a way around that.

Temporarily allow a gamble to be accepted with a value between 0 and 1. These *relaxed choices* give a compact convex moment range under suitable integrability assumptions. Apply minimax there. Then the uniqueness of the optimal choice forces the solution back to an ordinary acceptance set: accept where the relevant expectation is positive, refuse where it is negative.

**The final model is not randomised. Relaxation is only a proof device.**

I have written a proof using this argument for:

- **any set of worlds \(\Omega\);**
- a **separable, sup-norm closed space of bounded gambles**, containing constants;
- an explicitly constructible measure on that gamble space with full support, finite first moment and null indifference boundaries;
- coherent models represented by compact sets of positive normalised linear functionals.

The proof obtains a coherent defender with a **uniformly positive improvement across all worlds**, followed by the same hull-preserving trimming operation.

A particularly natural special case is:

> \(\Omega\) is a compact metric space, and gambles are continuous real-valued functions on \(\Omega\).

Here the states are ordinary regular probability measures. This includes genuinely infinite and uncountable world spaces.

There is also a concrete coverage application. For a full-support probability \(p\), the contamination model
\[
K=(1-\varepsilon)\{p\}+\varepsilon\mathcal P(\Omega),
\qquad 0<\varepsilon\leq1,
\]
has the required local freedom on
\[
U=\{h:p(h)>0\}.
\]
So the argument appears to give **exact infinite-world contamination coverage**, not merely an abstract conditional extension.

Again, this is a new audit result requiring verification.

**What remains outside that extension**

It does **not** yet cover all bounded gambles on an arbitrary infinite world set. That space is generally nonseparable—even for countably many worlds.

This matters because the present integration architecture needs an appropriate measure on gamble space. One cannot simply replace finite-dimensional Lebesgue measure by a full-support finite measure on every nonseparable normed space.

We must also distinguish:

- arbitrary positive linear functionals from countably additive probabilities;
- the open desirability sets \(D_K\) used here from more general coherent sets with additional boundary choices;
- infinite-dimensional local freedom from the finite-dimensional phrase “full-dimensional.”

These are genuine scope questions. But they now sit alongside a concrete infinite-world theorem to check, rather than an entirely speculative extension.

**What should change in generalized loss dominance**

I would organise the package around three alternative methods, none elevated into a necessary axiom:

1. **Compact certificates:** the weakening of the old infinite-world indexing requirement.
2. **Admissibility through scores:** establish existence of undominated models and identify them as coherent.
3. **Explicit safe improvements:** construct improvements that cannot be applied to coherent models.

The new result principally uses the third route. It does not need closed sections or compact certificates once the explicit improvement theorem is proved.

A short abstract construction lemma can capture this: if guidance protects coherent models, and every incoherent model has a coherent strict score improvement whose record cannot be applied to a coherent model, the simple ranking above yields the dominance conclusions.

That lemma belongs in generalized loss dominance. The geometric proof supplying those improvements belongs in the desirable-gambles application. **Do not introduce further axioms to recover a more familiar proof architecture.**

**Priorities for the next round**

1. **Referee the simplified ranking and the infinite-world extension.** This is now the highest-value mathematical task.
2. **Make relative minimax plus hull-preserving trimming the main proof.** The longer generation arguments can become supplementary results.
3. **Keep the two-sided problem active, but identify its real difficulty:** some rivals may have no nonempty coherent hull of the present kind. The current proof cannot simply be repeated for them.
4. **Clarify the lower-dimensional limitation.** The universal ranking already makes every *evaluable coherent model* undominated, including lower-dimensional ones. What fails on the one-sided domain is local freedom, hence coverage as defined.
5. **Reframe the application paper around universal coverage.** The earlier score constructions remain valuable as more structured ways of obtaining coverage. Keep the general dominance paper distinct.

I would **not** make finding a new criterion for “independent accuracy” the next main mathematical objective. That philosophical question remains important, but this round has opened a substantial positive extension programme.

The proofs and proposed revisions are here:

[Round 65: simplification and infinite-world extension](/Users/jk13942/Documents/CPMs/outputs/decomposable-domain-audit/Round65-simplification-and-infinite-extension-2026-10-26.md).