# After round 45: the missing local defences

22 October 2026. Author-checked; not independently refereed.

Read: PP20_completion_measurable.md, PP21_closure_engine.md, and REFEREE_Z_PP19.md in r45, together with the preceding completion note.

## 1. Assessment

PP20 is a genuine measurable enlargement. Its coarsenings repair arbitrary changes on the target's silent region, and its safe-world argument defends the target against all models. These statements are stronger than the earlier finite-region modules.

But it is not yet an extension principle for constructing an (S)-system. Its new coherent defenders do not acquire the defence property that T has. This is not merely an unchecked item: the relation as described in Theorem 4.3 positively fails that property for every model other than T and the three ideal vertex models.

The theorem below identifies a general defect in the construction, independent of the particular footprints or compensation geometry.

My previous recommendation to allow triangle completion was legitimate as a removal of an unnecessary restriction, but it has not supplied a construction mechanism. PP20 and the referee are right that the established guidance-closing obstructions survive it. The least-closure operation remains useful bookkeeping; it is not an existence argument.

## 2. A general obstruction to target-only local defences

The domain is the full measurable four-advice domain, modulo Gaussian-null sets of binary problems. Write V_i for the model giving the correct answer everywhere at world i. Write X ≤_i Y for “X is no worse than Y.” A record specifies both advice values on its disagreement set, and all common-context copies have the same record.

Call a record bounded if its disagreement set is contained, modulo null sets, in a bounded annulus of gamble space. This does not impose scale invariance on rankings. It uses only bounded rivals already in the stipulated domain.

**Proposition 1 (target-only bounded records).** Suppose a relation at each world consists of:

1. weak guidance;
2. any collection of records whose old advice is T throughout their disagreement set;
3. any collection of records whose disagreement sets are not essentially bounded.

Then every model N other than T,V_1,V_2,V_3 fails competitiveness against the full domain.

In fact it fails against a rival differing from it only in a bounded annulus. If N is coherent, that rival is incoherent.

**Proof.** Since N ≠ V_i, the set on which N is not i-correct has positive measure, for each i. Since N ≠ T, the set where they differ also has positive measure.

By atomlessness, choose pairwise disjoint, positive-measure, bounded sets E_1,E_2,E_3,H such that:

* N is not i-correct on E_i;
* N differs from T on H.

They can all be chosen in a bounded annulus. For completeness, finite simultaneous splitting is possible by partitioning the four given sets into their finitely many membership regions, choosing a non-null region for each requirement, and subdividing a region when several requirements use it.

Construct Y by making its advice i-correct on E_i, changing N's advice to any different advice on H, and keeping N elsewhere. Then:

* Y strictly improves on N on E_i at world i, so N ≤_i Y is not a guidance comparison, at any world;
* rec(N,Y) has bounded support, so it cannot be a record of type 3;
* its old advice differs from T on H, so it cannot be a record of type 2.

Thus N ≤_i Y fails at every world. If N were coherent and Y coherent, their non-null disagreement set would be conic. A non-null conic set is not essentially bounded, a contradiction. ∎

This proof uses neither (TC), an additive representation, nor a prescribed selection.

## 3. Application to PP20

PP20 Theorem 4.3 says its closure adds no further records to guidance and the installed a,b,t records.

* Every a or t record has old advice T throughout its support: type 2 of Proposition 1.
* Every b record rec(C_w,X) contains the whole footprint F_w in its support, because X=T there and C_w is silent there. F_w contains the non-null open cone N_w. Hence its support is not essentially bounded: type 3.

**Corollary 2.** Under PP20's stated description of its completed relation, its full-domain competitive models are exactly

    {T,V_1,V_2,V_3}.

**Proof.** Proposition 1 excludes every other model. Theorem 4.3 supplies T's competitiveness. V_i is competitive at world i by guidance, hence competitive over all three worlds. ∎

This conclusion is conditional on PP20's claimed closure description; Proposition 1 itself is independent of its proof. I have checked the structural properties used here directly from its definitions.

**Corollary 3.** No selection for this relation satisfies (S).

**Proof.** Every selected model is competitive on its support, and therefore competitive over all worlds. So its value must be one of these four models. Each vertex index must select its ideal model, by strict guidance. The four models are undominated and pairwise not all-world tied: for V_i versus any distinct model, strict guidance at i rules out such a tie.

For any of the four models N, the set of indices selecting it would therefore equal the intersection over worlds of the closed sections {p:C_p ≤_i N}. Thus the selection would partition the connected simplex into finitely many nonempty closed fibres, including the three different vertex fibres. Impossible. ∎

This does not rule out extending or redesigning PP20. It rules out obtaining (S) merely by finding a clever indexing of its present relations. Nor does it imply every extension of its current comparisons fails.

### A very concrete rival against C_w

Take a bounded positive-measure subset Q of N_w and split it into two non-null pieces. C_w is silent there. On one piece let Y give T's answer, correct at w and wrong at the other two worlds. On the other let it give the opposite answer. Keep C_w elsewhere.

At each world Y is better than C_w somewhere and worse somewhere. Guidance supplies no defence of C_w. The disagreement is bounded, so no b record applies. Its old advice is silence, whereas T answers throughout it, so no a or t record applies. C_w has no defence at any world.

This is not a rival changing T on a footprint. It is a rival changing the *new defender* on its own silent region. Handling only the former misses the latter obligation.

## 4. The positive design requirement extracted from the proof

**Corollary 4 (local defences are necessary).** In any full-domain system, every competitive coherent N distinct from the ideal vertex models must have an accepted, bounded-support, non-guidance comparison N ≤_i Y, for some i, against an incoherent local rival Y.

More specifically, whenever bounded disjoint sets E_i exist on which N is not i-correct, the rival that corrects N at i on E_i must be defended at some world. No world can provide that defence by guidance.

If N ≠ T, the rival can also be chosen to differ on a bounded set where N ≠ T. Then its defence cannot be implemented by copying a target-old-side record.

This is not a non-additivity theorem: an additive ranking can supply such a local defence. It identifies a necessary kind of comparison missing from the present non-additive construction. Nor is this condition sufficient for (S).

The crucial missing property is therefore not simply “more repairs.” It is a mechanism for giving new selected candidates their **own** local defences, using the same independent relations that defend T.

## 5. Change the construction objective

I would not make PP20 Conjecture 6.1 the main next milestone. Even domination of every incoherent model, with T competitive, does not establish competitiveness of the coherent dominators, let alone closed sections. These are different obligations in incomplete relations.

The next operation should have the following form:

*Input:* a target T and a collection of coherent candidates already defended against their own rivals, with accepted records and still-unresolved choices of defending worlds.

*Output:* a coherent defender C for a new rival, **together with a defence rule for C's own rivals**, preserving the old candidates' defences and the axioms.

The defender's credal set and its defence rule must be chosen together. Choosing C first, proving it undominated, and postponing its defence rule is precisely the asymmetry in the current approach.

Three unnecessary restrictions should be removed:

1. Do not require every defender to be a coarsening of T. Coarsenings are useful geometric candidates, but a whole construction needs much richer geometry; in particular vertex selections are not coarsenings of T.
2. Do not freeze every currently available T-defence as a required comparison. (S) asks for at least one defending world. Installing comparisons at every available world spends freedom that a new candidate may need. Preserve the defence obligation, permitting joint reassignment, rather than preserving an arbitrary earlier allocation.
3. Do not require an inert closure, no individual-world ties, or strict repairs at every world. None follows from the axioms. Allowing them is not a solution, but prohibiting them in advance is unjustified.

## 6. A concrete next round, with a decisive success criterion

### Main constructive task: a uniform extension that transfers the defence property

Aim for the input/output operation in section 5, not for another isolated finite module. The following two-model problem is its first necessary test, to be settled inside that work rather than advertised as a sufficient construction target.

Keep T fixed. Let C vary over coherent credal sets, rather than over a fixed three-member family. Construct one relation system in which:

* T and a distinct, non-vertex C are coherent and undominated;
* **both** are competitive against every measurable rival differing from them in a bounded region, including arbitrarily small changes;
* the required comparisons are based only on their disagreement records;
* (G) and (TC) hold with every common-context copy;
* the non-additive comparisons previously obtained remain genuinely relevant, rather than being moved to unrelated models.

The case C=C_w is a useful first geometric candidate, but should not be mandatory. The two local defence rules must be solved jointly. A globally safe choice for T made before C is chosen is not an adequate construction method.

This is still a necessary subproblem, not the whole programme. Its value is that Proposition 1 proves the current construction does not even pass it. An isolated two-model example, or an additive curve with irrelevant non-additive comparisons appended, is not the desired outcome. The objective is a proof uniform in C over a nontrivial parameterised family, coupled to the actual non-additive defences. No model-valued continuity is assumed merely by asking for such a parameterised family.

### The next extension target: a family, not another finite list

If the two-model construction works, establish a uniform rule for adjoining further coherent models and maintaining these local defences. At that stage incorporate the actual fixed-rival closed-section requirements. Do not impose joint continuity, continuity in the rival, a Bayes interpretation of the index, or a predetermined posterior family.

The final objective remains a whole-simplex selection. The two-model test is a diagnostic for a reusable mechanism, not a replacement for that objective and not evidence that closed sections will follow automatically.

### Adversarial task

Use the bounded rivals in Proposition 1, the partial-source rivals from PP19, and simultaneous changes around two candidates. A failure should distinguish:

* a contradiction from (G), (IB), (TC) and the requested defence obligations;
* a contradiction caused by keeping an optional old T-defence;
* failure of a chosen geometric family of C's.

Only the first would exclude the proposed extension principle at the stated scope.

### Computation

Finite cells cannot certify this task. If used, include radial splitting and new rivals on only one radial piece, while coherent candidates retain the same advice on all pieces of a direction. Merely lifting old requests to refined cells misses the new obligation. Record success only as a finite diagnostic.

## 7. What would count as progress now

* An explicit measurable, independent local-defence rule that works for both T and new coherent candidates, with a proved compatibility principle.
* Preferably, that rule should be uniform over a family large enough to support a selection, rather than depend on private witnesses for finitely many models.
* A genuine obstruction to that joint rule would also clarify the problem, but it must not rely on freezing unnecessary earlier comparisons.

Another theorem that dominates a larger rival class while only T has its own defence rule would repeat the present asymmetry. The exact coverage problem remains open.
