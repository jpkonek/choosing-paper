**Round 51 makes a useful advance: it identifies a restriction imposed by the gate architecture, rather than by our axioms. But I would not make the sampled fan the main next step.** I have worked out a stronger alternative: your original rescaled family passes the new pairwise geometric obstruction throughout its interior, not merely for sampled pairs.

This is not yet a construction of the rankings. It does, however, give us a full-simplex family through T with a proved compatibility property. That is a better foundation than another local family whose extension remains unspecified.

### What round 51 establishes—and what it does not

The combined-cut obstruction looks sound under the stated gate and Bayes hypotheses. My multicap proposal therefore fails **within that architecture**. The union lemma remains correct, but combining the advice geometrically does not ensure that the corresponding gates can coexist.

Two qualifications matter:

- Passing the pair’s ordering test is not the same as constructing compatible fields. The fan’s 1,640 successful tests establish a necessary geometric condition, not joint gate compatibility.
- PP47’s wording that a combined cut cannot dominate *any* rival is too broad. For example, a coherent model improves pointwise on the always-contradictory model. The restriction to the relevant fills and non-guidance comparisons must remain in the statement.

Also, PP47’s exact zero-accepting test retains a strict pairwise compatibility hypothesis. It should not become an assertion about all rankings satisfying (TC), or about all gate designs.

**The star’s global witness is acceptable as an intermediate result.** Our axioms do not prohibit it. The reason to avoid spending another round strengthening it is strategic: it does not supply the missing non-additive mechanism or handle the decisive rivals. We should not turn that strategic concern into an extra axiom.

### My positive result: the rescaled family escapes the combined-cut obstruction

Let \(M\) be any compact convex credal set strictly inside the simplex. For a likelihood vector \(a\in\Delta\), put
\[
M_a=\left\{\frac{a*p}{a\cdot p}:p\in M\right\},
\qquad C_a=D_{M_a}.
\]

This is your original family. What is new here is its relationship to round 51’s obstruction.

Take two interior indices \(a,b\). On any problem where their advice differs, let:

- \(W\) be the worlds where \(C_b\)’s advice is worse than \(C_a\)’s;
- \(R\) be the worlds where it is better.

Then
\[
\boxed{\quad
\min_{i\in W}\frac{b_i}{a_i}
<
\max_{j\in R}\frac{b_j}{a_j}.
\quad}
\]

Crucially, **the same ordering of the ratios works for every disagreement between these two models.** Equivalently, the vector
\[
D_i=\log(a_i/b_i)
\]
satisfies round 51’s necessary condition
\[
\max_{i\in W}D_i>\min_{j\in R}D_j
\]
on every disagreement.

The reason is simple. Suppose the new model starts accepting \(g\). If likelihoods had increased at least as much at every negative-payoff world as at every positive-payoff world, this could not turn an unaccepted gamble into an accepted one. The corresponding argument works when advice is withdrawn or reversed.

I proved this directly and checked 9,855 disagreements using exact rational arithmetic. The proof, not the computation, establishes the result.

This family also has the global geometry we need:

- It contains T at the uniform likelihood.
- It reaches the appropriate precise model at each vertex and stays on the appropriate face at boundary indices.
- Its credal sets vary continuously over the whole simplex.
- For T1, the advice varies continuously in measure.
- Its interior is genuinely two-dimensional, unlike a two-dimensional index map whose image is only a tripod.

I have written the proof and its limitations in [Posterior family passes the pair-type obstruction](</Users/jk13942/Documents/CPMs/outputs/decomposable-domain-audit/posterior-gates/Posterior family passes the pair-type obstruction.md>). It is author-checked, not independently refereed.

**What this does not establish:** compatible gate fields, (TC), closed sections for the rankings, or domination of the necessary rivals. Boundary pairs also need their own gate analysis. This is a substantial improvement to the candidate geometry, not a claimed cover.

### The conceptual change I recommend

The multicap construction makes several repairs independently and then tries to accommodate their combination. That combination creates the incompatible advice patterns.

The posterior family instead **changes the whole credal set through one coordinated change in relative likelihoods**. Its changes of advice therefore come with a common pairwise ordering certificate. We should exploit that coordination, rather than continue adding independent repairs and protecting them afterwards.

This is not a recommendation simply to revisit round 42. That round established that:

- rescaling-*invariant rankings* fail;
- accepting every proposed repair at every world fails (TC).

Neither result excludes using this family with model-dependent fields that are **not invariant under rescaling**. Round 51 now gives a precise compatibility question that was not available in round 42.

Nor should we freeze the compatibility constants to \(a_i/b_i\). Those ratios certify the **advice geometry**; they are not yet the correct constants for the fields. Imposing that identification could manufacture another global-witness restriction.

### Instructions for the next round

I would replace the fan-first brief with this one.

**1. Construct joint fields on the posterior family, starting with a genuinely two-dimensional test.**

Use T and two nearby posterior models whose likelihood directions are independent. Require:

- each model’s own supporting Bayes inequalities;
- the pairwise field inequalities;
- the zero-accepting triangle conditions, including attained equalities;
- competitiveness against all measurable rivals, not just selected models.

The first deliverable must be **actual fields or an exact obstruction**, not another successful type test. If fields exist, seek one formula valid on a two-dimensional neighbourhood. Supporting weights may vary independently of the selection indices.

**2. Make repair capacity part of that construction from the start.**

For those same models, require dominators for both:

- fills combining advice from the two different nearby models;
- retreats that remove advice from a registered model.

These are the interactions that the star avoids and that caused previous extensions to fail. Do not postpone them until after building a beautifully compatible but unusable family. The defender’s posterior index should be an unknown chosen jointly with the fields.

**3. Run the non-additive branch now—but change exactly one architectural commitment.**

Retain model-dependent evaluators as sources of proposed comparisons. **Drop the rule that every positive evaluation must automatically become an accepted comparison.**

That universal acceptance rule is what turns pairwise field compatibility into such a strong restriction. A selective rule could retain the comparisons needed for defence while leaving other positively scored comparisons incomparable.

This branch must produce an explicit disagreement-based acceptance rule. “Choose a consistent subset” is an existence problem, not a construction. It must also check all coherent models that realise the same disagreement; assigning a comparison to its originally intended source is insufficient under (IB).

There is no theorem yet showing that this selective architecture works. But it changes the commitment responsible for the current obstruction, rather than changing the shape of the cuts while retaining that commitment.

**My recommendation is therefore: keep the star as a benchmark, stop the multicap gate construction, and make the posterior family’s jointly designed fields and repairs the principal constructive task. Start selective, genuinely non-additive verdicts alongside it.** The useful next success would be a two-dimensional neighbourhood with actual fields and cross-model repairs—not another family that merely passes a necessary test.