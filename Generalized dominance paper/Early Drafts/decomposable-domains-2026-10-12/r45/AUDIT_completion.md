# After round 44: complete comparisons, rather than protect regions

22 October 2026. Author-checked mathematical note; not independently refereed.

Read: PP18_source_field.md, PP19_sections_near_T.md, REFEREE_six_source.md, and LEAD_selection_count.md in r44. This note does **not** construct a full cover of T1. It gives a more permissive, exact extension operation and identifies what remains to be proved about it.

## 1. Assessment and two important qualifications

Theorem Z's main argument is sound: a permanent prohibition on making advice correct on a non-null mixed region conflicts with (S), strict guidance, independence and direct (C). It does not use (TC). Changing the positions, number or ownership of the protection regions cannot fix that problem.

This does **not** establish that the comparisons in the six-source module have no extension satisfying (S). It establishes that such an extension cannot preserve the invariant used in their present proof. Adding comparisons that violate that invariant is still allowed, provided the enlarged relations satisfy (TC).

Two qualifications matter for the next construction:

* PP19 forces compensation **for the particular defender and fill being considered**. It does not force a permanently designated compensation region, a finite partition into source types with fixed advice, or a prohibition on subsequent comparisons reversing advice there.
* Its separation from the target's tie fibre is **rival-dependent**. For each fixed rival X, its dominator indices are separated from that fibre. The union of dominators over different rivals need not have a uniform positive separation. PP19 explicitly leaves the relevant uniformity question open.

Thus compensation should be a consequence of choosing a defender, not a piece of territory reserved in advance.

### A shorter verification of the rigidity ingredient in Theorem Z

In the present Gaussian/Lebesgue measure class, Lemma R can be proved using homogeneity alone. Let N be coherent, and let Q' have positive measure where N is not correct at w. Choose a non-null subset Q of Q' inside a bounded annulus a < ||g|| < b. Change N to the w-correct answer on Q and nowhere else, obtaining X.

If a coherent C equalled X almost everywhere, then C and N would agree almost everywhere outside that annulus. Their disagreement is conic. Any non-null conic disagreement has a non-null portion outside the annulus, by dilation. Hence C and N agree almost everywhere everywhere. This contradicts X differing from N on Q.

This verifies the ingredient needed by Z without the convex-cap argument. It uses the stipulated equivalence to Lebesgue null sets; it is not a claim for arbitrary measures supported on an annulus.

## 2. The restriction to remove next

The six-source proof gives much more than (TC): no accepted three-cycle passes through any new record, and no two distinct models tie at any world.

Neither condition is an axiom.

For a reflexive relation, (TC) is equivalent to:

> Every accepted directed triangle has all three reverse comparisons accepted as well.

Indeed, if A ≤ B ≤ C ≤ A, (TC) applied to A,B,C requires A ≤ C. Applying it to the two other rotations requires the other two reverses. Conversely, a violation of (TC) is precisely an accepted triangle with a missing reverse.

Consequently, a new triangle has three possible resolutions: refuse one of its edges, change a proposed coherent defender, or accept its missing reverses. We have concentrated on the first two and largely excluded the third by construction.

There is a hard limit: a triangle containing a strict guidance comparison cannot be repaired this way, because reversing that guidance comparison is forbidden. But an entirely non-guidance triangle need not be rejected merely because it is a triangle.

Allowing this does not assume that ties are harmless. Their further consequences must be generated and checked. In particular, ties at all worlds with an incoherent model are unacceptable when one endpoint is protected and coherent.

## 3. A precise extension operation

Work on the full measurable model domain, modulo null sets. Write X ≤_i Y for “X is no worse than Y.” Store comparisons as full advice-change records and install all their common-context copies. No location-changing or rescaling invariance is imposed.

Maintain:

* world relations R_i;
* a collection P of models required to remain undominated, initially containing the target T;
* any already assigned selection values C_p, which must belong to P.

P is a bookkeeping collection during construction. It is not declared to be the final class of coherent undominated models.

Include reflexivity and weak guidance at the outset. Repeatedly apply the following rules, including all newly enabled instances.

**I. Independence.** Install every common-context copy of an accepted record.

**II. Triangle completion.** If A R_i B, B R_i C and C R_i A, install A R_i C. The rotated instances install the other reverses.

**III. Protection of registered models.** If N belongs to P and X R_i N for every world i, install N R_i X for every i.

This is exactly what N's undominatedness requires: a weak all-world dominator of N must tie with it everywhere.

**IV. Propagation of protection through all-world ties.** If N belongs to P and N and X tie at every world, put X in P.

This is what direct (C) requires for a protected coherent model: its all-world tie partners must also be coherent and undominated.

There are two basic failures:

**F1.** A reverse of a strict guidance comparison is installed.

**F2.** An incoherent model enters P.

Explicitly stipulated strict comparisons, if any, add corresponding forbidden reverses. They should be stipulated only when needed, not automatically for every new comparison.

This distinction matters when using the previous module. Reusing its weak comparisons while permitting some of its strict verdicts to become ties is a **redesign**, not an exact extension preserving that ranking's strict part. An exact extension must mark every old strict reverse as forbidden. No claimed extension theorem silently changes that requirement.

Take the least collection closed under I–IV. It exists by monotone closure on the set of models and comparison pairs. For these finitary rules, iteration through finite stages and their union suffices; each premise uses finitely many atoms because the number of worlds is finite. This is an existence definition, not a claim that the operation is computable on the full measurable domain.

### Extension theorem

If this closure has neither F1 nor F2, then:

1. the resulting relations satisfy strict (G), (IB) and (TC);
2. every model in P is coherent and undominated;
3. every all-world tie partner of a model in P belongs to P, so direct (C) holds for all models registered in P;
4. in particular, T remains coherent and undominated, giving (LA).

**Proof.** Independence is rule I. Rule II gives the triangle characterization of (TC). Weak guidance was inserted initially and F1 preserves its strict part. If X weakly dominates N in P, rule III inserts every reverse, so X cannot strictly dominate N. F2 excludes incoherent members. Rule IV gives the tie claim. ∎

This statement deliberately does not claim direct (C) for unregistered undominated models. Section 5 explains how full (S) removes that gap.

### Necessity of the closure

Every full solution extending the initial comparisons and keeping the registered models coherent and undominated must include everything forced by I–IV. Rule II follows from (TC), rule III from undominatedness, and rule IV from direct (C).

Thus F1 or F2 is a genuine obstruction to that particular extension request. Neither is an artefact of a margin, a priority order, a fixed family of sources, or an additive endorser.

Clean closure is not a guarantee of a later (S)-extension. It is an exact test of the consequences of these rules at the present stage.

## 4. The new coherent defender is a variable

For an incoherent rival X, propose any coherent C, register C in P, and insert

    C R_i X   for every world i.

Then apply the closure above. The candidate C is chosen after seeing the existing comparisons and X; it need not belong to a preassigned family.

**Corollary.** If the closure is clean, C remains undominated, T remains undominated, and C dominates X: it is no worse at every world and strictly better at at least one.

**Proof.** Protection gives the first two claims. If all reverses X R_i C were accepted, rule IV would register the incoherent X, giving F2. Thus at least one reverse is absent. ∎

This removes an important unnecessary demand: we need not choose in advance the world at which a repair is strict, and we need not make it strict at every world. Some reverse comparisons can be admitted to resolve triangles. The collective requirement is only that they cannot all be admitted for an incoherent rival.

For a coherent rival, a tie is not automatically a failure: it may enlarge P. This is an actual form of co-design of the undominated class.

The operation does not assert that an admissible C always exists. Proving that is the substantive extension problem, now with fewer imposed restrictions.

## 5. How the actual undominated class is recovered

Suppose the construction eventually supplies an (S)-selection p ↦ C_p with image in P, satisfying the support-defence and fixed-rival closed-section clauses. Suppose the resulting relations remain closed under I–IV and have neither failure.

Then P is **exactly** the class of undominated models, and all of them are coherent.

**Proof.** Members of P are already coherent and undominated. For any undominated N, the KKM argument from (S) gives a selected C_p that is no worse than N at every world. Since N is undominated, every reverse holds. Thus N is tied at all worlds with C_p ∈ P, and rule IV places N in P. ∎

Consequently full direct (C) follows too: an all-world tie partner of any coherent undominated model is registered and is coherent and undominated.

This addresses the concern about freely choosing C_R. The construction may register candidate defenders, but closure constrains those choices. Under completed (S), it identifies the actual undominated class rather than simply naming one.

## 6. What happens to closed sections

Nothing above imposes closure as the rival varies, joint continuity, or continuity of p ↦ C_p.

For an assigned selection, the required additional implication is only:

    p lies in the closure of {q : C_q R_i X}
        implies C_p R_i X,

for fixed X and i. This is precisely the closed-section clause. Adding these implications to the closure is sound, but they are no longer finitary. One must take the least fixed point of the enlarged monotone operator, not assume that the union of finite stages is closed. No compactness claim about that enlarged construction is made here.

The defence obligations still involve choices:

    for every p and X, choose at least one i in supp(p)
    at which C_p R_i X holds.

Neither these choices nor the values C_p should be fixed by a margin rule. Their compatibility is the remaining construction problem.

## 7. What the next round should actually do

The main task should be a target-preserving extension with **reversible** non-guidance comparisons, not a new permanent protection zone.

1. Start with T and the guidance relations. Use the six-source module as a source of geometric candidates, not an irrevocable list of strict comparisons. In particular, do not automatically install all its between-source comparisons.
2. Treat the majority-fill rivals and the cross-source rival X* together. For each repair, let the coherent C vary. Insert only the requested weak comparisons, then complete triangles and propagate protection as above.
3. Allow individual-world ties and incomparabilities. Reject only an actual forced reversal of guidance, an incoherent protected model, or a separately required negative comparison. A triangle made solely of new comparisons is not by itself failure.
4. Include rivals changing the former R_i regions from the beginning. A theorem restricted to rivals avoiding those regions would repeat the old limitation.
5. Prove the result for measurable fills, not just whole-cell advice. Any finite calculation must report which continuum implications it omits.
6. Next add fixed-rival section obligations. Their propagation must be checked; the algebraic extension theorem does not supply them.

There are two worthwhile outcomes: a clean extension handling this joint class without any permanent correctness zone, or a finite derivation of F1/F2 that applies to every coherent candidate in a precisely stated geometric class. Another construction protected by moving the forbidden region elsewhere would not meet the objective.

This is not an existence proof in disguise. The closure part is elementary, and related least-closure tests were already considered earlier in the project. Its practical change is to let (TC), undominatedness and direct (C) **force additional comparisons and additional protected coherent models**, rather than treating every new cycle or weak dominator as immediately fatal. Whether this enlarged freedom is sufficient for T1 remains open.
