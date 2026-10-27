# After round 46: selected realizability, rather than universal coverage in one ranking

22 October 2026. Author-checked; not independently refereed.

Read: REFEREE_round46.md and PP23_local_rule.md, including the room theorem and the padding argument. Earlier context: PP20, PP21 and the local-defence audit.

## 1. Assessment

Round 46 makes a useful distinction. Supplying local defences by itself is easy; supplying them in a way compatible with coherent domination and a whole-simplex selection is hard. My previous local-defence test exposed a real defect of PP20, but it was a necessary diagnostic, not a discriminating sufficient target. I would not spend another round merely passing a more elaborate version of that test.

The referee's R46.1 is a clean improvement: the particular balanced rules are excluded under actual fixed-rival closed sections, without model-valued continuity. However, its interpretation and the proposed edge-first strategy need correction.

The most promising construction ingredient is PP23's use of partial advice that no coherent model can realise, to prevent a repair from composing into a guidance reversal. The restriction I would remove is the demand that the covering layer defend **every coherent model**, including arbitrary auxiliary models introduced in impossibility proofs.

## 2. R46.1 does not force non-additivity on every edge

The exact conclusion is:

> On each edge, some accepted bounded comparison from an edge-selected model, at an edge world, has negative value under the specified balanced field Ω^(0).

That is disagreement with one particular additive field. It is not failure of endorsement by every additive field. The referee's proof correctly distinguishes these in its paragraph about general strictly guiding fields, but its later description of “where non-additivity must live” overstates the conclusion.

### Explicit additive sanity check

On the full four-advice domain define

    L_i(X) = integral |g_i| r_i(X,g) dμ(g),

where r_i is 0,1,2,3 for correct, silent, wrong, contradictory advice. Gaussian integrability makes the losses finite. Select C_p = D_{ {p} }.

For a fixed problem represented by g, put

    a = sum_{g_i>0} p_i |g_i|,
    b = sum_{g_i<0} p_i |g_i|.

The weighted costs of accepting g, accepting -g, silence and contradiction are respectively

    2b, 2a, a+b, 3(a+b).

Except on the null hyperplane p·g=0, the unique minimum is the answer given by C_p. This holds for boundary priors too.

It follows that:

* the rankings satisfy strict (G), (IB), and transitivity, hence (TC);
* C_p is competitive on supp(p), and undominated, by unique weighted minimisation;
* p ↦ L_i(C_p) is continuous by dominated convergence, so all required sections against fixed rivals are closed;
* (LA) holds;
* (C) holds: KKM puts any undominated model in an all-world tie with some C_p, and unique weighted minimisation makes that model equal to C_p. The same uniqueness excludes distinct all-world tie partners.

This is an additive (S)-system. It does not cover the imprecise target T1, which is not the claim here.

One can see its negative-Ω edge comparison explicitly. Let p=(1/2,1/2,0). On a small patch near (2,-1,-1), C_p gives the world-1-correct answer; on another near (1,-2,-1), it gives the world-1-wrong answer. Both patches are in minority class M_1. Replace both answers by silence, using patch masses m and 3m/2 respectively.

Choose the patches so g_1 is between 1.9 and 2.1 on the first and between 0.9 and 1.1 on the second. Then the world-1 loss change is at least

    1.9m - 1.1(3m/2) > 0,

so C_p is accepted as no worse than the rival. But the balanced score is

    Ω_1^(0) = 2m - 2(3m/2) = -m < 0.

Thus even a bounded comparison of the exact kind required by R46.1 can be entirely additive.

**Strategic consequence.** R46.1 does not establish that the essential non-additive construction must start at the edges. It excludes keeping Ω as the universal local judge there. Edge-first assembly is a possible tactic, not a deduction from this theorem.

Nor should “a geometrically two-dimensional selected family” be silently added as an axiom. The index domain must be the full simplex. A lower bound on the geometric dimension of its image would require a separate proof under the actual section axiom.

## 3. The unnecessary universal obligation in PP23

Theorem 4.5 defines a covering layer that accepts each bounded record with a coherent-realizable old side at some world. That means: if **any** coherent model could give the old advice, the record must be defended.

For one ranking in the coverage programme, that is too much. We need the support-defence clauses for its selected models. We do not need every coherent model to be competitive under that same ranking. The coverage axiom asks for each target to be vindicated by **some** suitable ranking, not for universal vindication under one ranking.

This difference matters in the proof of Proposition 4.7, even after the referee's repairs. The proof constructs padding records x and y with old sides realised by auxiliary coherent sets. Because the covering layer must defend every such record, and Ω leaves only the owner world available, both records are forced onto that world. Together they exclude the proposed domination.

For a co-designed selected family, the missing premise would be:

    The old side of x, respectively y, is realised by a selected model.

Realisation by some coherent model does not establish that. Consequently, Proposition 4.7 is a genuine obstruction to its universal covering class, but not automatically to a selected-family version. This does not refute the proposition or show its conclusion false in that version; it identifies the proof obligation that would have to be restored.

By contrast, Lemma 4.4's safety argument remains available when the covering layer is restricted to selected-realizable old sides. Selected models are coherent, so the contradiction to coherent realisability used in that lemma still applies.

This is a substantive asymmetry: we can retain the geometric protection lemma without accepting the universal covering obligation that makes the padding records compulsory.

There is a concrete check that this distinction is not empty. Put an inverted departure inside T's silent region and use Proposition 4.7's particular splitting record x. Its old side is A on the positive-measure A-part of the departure and S on the positive-measure padding set F. T does not realise that old side, since it is silent on the A-part. No precise model realises it either, since a precise model is silent only on a null hyperplane. Thus x is not realised even by the candidate collection consisting of T together with **all precise models**. This is not an (S)-construction, and it does not exclude alternative forced splits. It does show directly why coherent realisability alone cannot make this particular padding comparison compulsory in a selected-family argument.

## 4. An exact way to formulate the co-design

Let p ↦ C_p be a candidate coherent selection, whose values are still variables. For a record r=(D,a,b), define

    P(r) = {p : C_p = a almost everywhere on D}.

This is the set of indices whose selected models can be the old side of a common-context copy of r. Let A(r) be the set of worlds accepting r.

**Lemma (support-sensitive record obligations).** The support-defence part of (S) is equivalent to

    A(r) intersects supp(p), for every record r and every p in P(r).

**Proof.** If p is in P(r), splice b into C_p on D. The resulting rival has exactly record r from C_p, so (S) gives the intersection. Conversely every rival of C_p defines such a record. ∎

This condition is simultaneously:

* weaker than covering every coherent-realizable old side, because only selected realisations matter;
* more precise than an undifferentiated three-world covering rule, because boundary indices require particular supports.

It also makes the co-design lever explicit. If a record cannot be accepted at the worlds available on a face, one must either change the verdict or avoid selecting models on that face that realise its old advice. Merely labelling two copies “edge” and “interior” cannot change their verdict: (IB) still identifies the records.

This is not permission to arbitrarily declare the undominated class. Keep the protection and tie-propagation rules from the completion note. Once full (S) is obtained, those rules and KKM identify the actual undominated class. Candidate exclusions must be compatible with those rules too.

## 5. The construction problem I would put first

Develop a **selected-family version of the incoherence-certificate construction**, rather than first solving universal Conjecture 4.9 and then trying to glue three fixed-key systems onto it.

Use three coupled choices:

1. **Coherent candidates.** Choose credal sets containing T among the selected values, with the required vertex values. Interior and edge values remain variables; neither coarsenings nor posterior families are prescribed.
2. **Defence allocations.** Cover precisely the record obligations in section 4, including their face supports. Do not require coverage for records merely because arbitrary unselected coherent models realise them.
3. **Coherent repairs.** Choose both the coherent defender and the accepted repair record. Prefer records whose new advice carries a concrete incoherence certificate, beginning with inverted departures, because Lemma 4.4 gives genuine composition control without a permanent protected region.

The bounded inverted departures are a seed class, not a claim to cover every incoherent rival. A full construction must later handle other kinds of incoherence, unbounded records and the whole selection. The point is to test whether the geometric certificate can survive the *right* defence obligations first.

### A concrete first test of this mechanism

Take one of the referee's repaired padding configurations, including its steep lines and sufficient measurable mass. Use an inverted departure out of T on a bounded portion of T's silent region. Try to admit this as an all-world domination while jointly choosing:

* the selected coherent models that supply the surrounding defence obligations;
* which of the padding records are actually compulsory;
* the worlds that accept those compulsory records.

In particular, test the B-heavy configuration that universal Proposition 4.7 excludes. The aim is not to circumvent a theorem by ignoring its hypotheses, but to determine whether the extra universal-realisation hypothesis is doing essential work.

Successful construction must show that omitted padding records are not forced back by other selected realisations, (IB), (TC), protection of the selected models, or the section obligations. A numerical colouring that simply omits them is insufficient.

If both padding records inevitably become compulsory in every permissible selected family, prove that implication. It would make the obstruction genuinely relevant to co-design, rather than merely to universal coverage.

## 6. How to prevent another round of weak milestones

Keep fixed-rival closed sections in the design constraints from the beginning. Do not replace them by joint continuity, continuity in measure, or a blanket measurability condition on the verdict as a function of all records. Measurable models are stipulated; such additional regularity of the ranking requires justification and is not the same thing as (S).

Do not demand that all earlier optional comparisons survive. If a previously chosen defence causes a conflict, permit reassignment as long as the actual support-defence obligation remains met. Do preserve strict guidance and genuinely required strictness.

Do not treat avoiding every shared-source configuration as a new axiom. PP25's no-shadow hypotheses are sufficient conditions for its reduction, not established necessities for all constructions. A proposed construction may instead handle the corresponding compositions directly.

Do not interpret an additive edge comparison that violates Ω as evidence of non-additivity. Check endorsement by arbitrary relevant fields separately.

An isolated new local domination would still not be a breakthrough. The intended output is a repeatable construction in which selecting coherent models and assigning their defence records constrain each other constructively, with an explicit route to the whole-simplex section condition.

## 7. Recommended allocation of effort

**Main effort:** selected-family, support-sensitive incoherence-certificate co-design. The repaired padding configuration is its first adversarial test, not the final objective.

**Secondary tool:** ordinary additive precise-probability systems provide a known-working edge benchmark. Use their existence as a check against blanket edge claims. Do not freeze all their comparisons as an irrevocable base; previous barriers explain why that is restrictive.

**Optional secondary problem:** Conjecture 4.9 under its original universal covering requirement. It is mathematically interesting, but neither a necessary gateway to the main construction nor sufficient for full (S).

**Do not prioritise:** another general exclusion of fixed or regionally nested priorities, unless it directly distinguishes a proposed construction. Those exclusions have already explained the failure of the particular one-dimensional mechanisms.

## 8. Status

No cover of T1 is supplied here. The new contributions are the explicit additive check on the edge interpretation, the exact support-sensitive formulation of record obligations, and the identification of universal coherent-realisation coverage as a removable restriction in PP23's construction problem. The mathematical results quoted from round 46 retain their stated scopes; the proposed wider construction remains open.
