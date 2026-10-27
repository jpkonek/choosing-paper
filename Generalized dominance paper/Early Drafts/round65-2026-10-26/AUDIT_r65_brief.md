# Round 64 assessment and round 65 brief

26 October 2026. Based on ES64, its referee report, PC64 and the round report. This is an audit and proposed research programme, not an independent referee certification of every result.

## Decision

Keep comparison-deleted Brier admissible under the agreed axioms. Make (H) the main mathematical task. Do not add (Add) merely to exclude this construction. Examine (Add) separately as a proposed additional normative assumption, with an argument independent of the desired coverage answer.

Protecting a coherent target is now easy in this architecture; covering it is not. The theorem is conditional on (H), which is precisely the missing dominance statement. A coherence-informed definition is not a circular proof when its dominance claim still requires a substantial independent theorem. It may, however, supply a representation of coherence rather than an independent accuracy-based justification for it. The paper must distinguish those ambitions.

The veto–box theorem is a substantial positive result: it refutes the latest proposed three-world characterisation. That is additional reason not to infer general impossibility from the accumulated exclusions.

## Scope corrections

1. ES64 Lemma 5.1 proves strict Brier improvement over every non-Bayes model. It does not prove (H) for every non-Bayes model. Every incoherent model is non-Bayes here, so the latter claim would already settle (H).
2. The universal construction is universal within a fixed evaluable domain U. Local freedom and target coverage still require the relevant domain hypotheses. Do not say that one fixed U covers every conceivable coherent target.
3. Failure of (H) defeats deletion protecting *all* coherent models. It does not defeat deletion protecting a smaller family, or coverage under the axioms in general.
4. “Weakest identified candidate” for (Add) is a comparison among tested proposals, not a minimality theorem.
5. The success of all existing constructions under (Add) does not show that (Add) follows from accuracy or from the agreed axioms. Its exclusion of deliberate incomparability is a substantive modelling choice.

## A finite geometric witness for the missing condition

This observation strengthens ES64 Lemma 5.3 by removing its interior-point assumption and giving a converse. It needs independent checking, particularly against the project's a.e. conventions.

Let A=N\\X and B=X\\N. Let B_d denote the Lebesgue density-one points of B. Under ES64's positive-density measure assumptions and hull definition,

    mu(A intersect hull(B)) > 0

if and only if there are a density-one point a of A, density-one points b_1,...,b_r of B, nonnegative coefficients lambda_j, with 0 <= r <= n, such that

    a - sum_j lambda_j b_j is strictly positive in every coordinate.

The case r=0 includes missing strictly positive gambles. In three worlds at most three removed density points suffice.

Proof of sufficiency: every q in Q_B is nonnegative on each b_j. Otherwise its negative half-space would contain a positive-measure part of B around the density point. Since q is a probability vector, the strictly positive residual gives q.a >= eta > 0 uniformly in q. A ball around a therefore lies in hull(B); density of A at a gives the required positive-measure intersection.

Proof of necessity: write C=cl cone(B_d union R_+^n). Bipolarity gives hull(B)=int C, as in ES64 Lemma 5.2. Choose a density-one point of A inside this open set. For sufficiently small eta>0, a-2 eta 1 belongs to C. Approximate it within eta in sup norm by a point c of cone(B_d union R_+^n). Conic Caratheodory represents c with at most n generators from that union. Absorb its nonnegative generators into the residual. Then a minus the remaining nonnegative combination of B_d generators is strictly positive, as required.

This is not a finite-cell reduction of the ranking problem. Density, the moment inequalities and the quantification over arbitrary measurable X remain essential. It is a finite geometric certificate for the hull part of (H).

## Main task: obtain a dominator and its witness jointly

For arbitrary incoherent measurable X, seek a coherent N and the density-point certificate above, subject to

    integral_N h >= integral_X h coordinatewise,
    with at least one strict inequality.

The hard requirement is that the same N satisfies both conditions. Do not separately prove moment domination and an unrelated coherence violation and call that progress on (H).

Start with Lemma 5.1's strict Bayes dominator N_0. It gives an explicit positive margin in every coordinate. Explore coherent changes to N_0 that create the density-point certificate while using that margin. A useful sufficient bound is

    integral_{N triangle N_0} |h_i| dmu
       < integral_{N_0} h_i dmu - integral_X h_i dmu

for every i. Such an N remains a strict dominator. This bound is a search aid, not a requirement on a general proof: a successful repair may redistribute improvements and violate this bound while retaining the actual moment inequalities. Nor should the proof assume that an arbitrarily small modification of a particular N_0 always suffices.

Use general coherent defenders D_Q, not only Bayes half-spaces, rescalings, a fixed facet count, or one chosen deformation. Those are computational subfamilies only. If a proposed procedure fails, identify which of those optional restrictions caused it.

Two complementary outputs count:

- A theorem producing N and its finite witness for every measurable X, with the existing hypotheses or an explicitly substantial new class.
- An explicit incoherent X and a proof ruling out the witness for *every* coherent N satisfying the moment inequalities. Failure of a search over sampled priors or polytopes is not a counterexample to (H).

The adversary should concentrate on rivals for which added regions surround the hull of removed regions but do not meet it. The referee's centroid calculation explains why this can frustrate one defender. A counterexample must make it happen for every eligible defender.

## Compactness tool, with its limitation

For fixed compact nonempty K', the family of compact convex Q with K' subset Q subset Delta is compact in Hausdorff distance. The map Q -> integral_{D_Q} h dmu is continuous: lower expectations converge uniformly on bounded gamble sets, their zero sets are Lebesgue-null because P_Q(h+t1)=P_Q(h)+t, and dominated convergence uses the finite first moment.

Consequently the coherent defenders with moment improvement at least delta in each coordinate form a compact set whenever nonempty. Lemma 5.1 supplies such a delta for every incoherent X.

This can support a global search or variation proof. It does NOT justify maximising the hull-overlap functional without further analysis. A tiny removed set can change its coherent hull dramatically. Do not assume hull continuity, or that a proof restricted to a fixed positive delta settles cases needing smaller margins.

## Secondary tasks

- Audit (Add) independently: give its decision-theoretic justification, and distinguish it from IB and TC. Report results under (Add) as a strengthened-framework branch, not corrections to the original question.
- Preserve the veto–box theorem in the covering paper. Its scalarisation proof supplies a robust positive construction without depending on (H).
- Finish the six omitted exclusion proofs and four citation checks, or remove/downgrade those claims before presenting a completed paper.

## Success criterion

The next round should advance the geometric existence problem (H), not spend its main effort finding an axiom that makes the new construction illegal. Do not reopen (S), demand complete world orders, or impose transitivity. If (H) succeeds, report both the formal universal-admissibility theorem and the separate philosophical limitation of coherence-informed rankings.
