# Round 40 audit and next-round brief

21 October 2026. Read PP8_joint_defence_test.md and PP9_joint_defence_analysis.md. The analytic arguments below are author-checked; archived numerical certificates have not been rerun. The pointwise inequality in §2 was exhaustively checked on 240 sign/advice/world cases, including unchanged advice.

## 1. Assessment

The proposed joint-choice/deletion rule should be withdrawn as a covering construction. Its failures are structural, not a tie-breaking bug:

- the cost objective gives a doubly anchored, additively dominated record only one defender;
- the margin priority then deletes precisely that non-additive defence;
- both reverse-anchor eligibility and strict protection thresholds create genuine closed-section difficulties.

PP9's protected-defence theorem is sound. However, its mechanism is considerably more familiar than the report suggests: all those defences belong to one fixed lexicographic additive ranking. This is proved below. It explains their mutual compatibility, and limits how much positive evidence they provide for the programme.

The reports establish failures of particular allocations. They do not establish an impossibility for the anchored-reverse rival under unrestricted rankings. In particular, they do not force the supposedly cheaper return comparison: the tested rule chooses it.

Coverage-constrained deletion is an exact constraint problem, but is not a new construction. Retaining the current initial relation also retains its section holes. Another round of priorities V4, V5, etc. is not recommended.

## 2. A stronger explanation of the protected-defence theorem

Let M_i be the mixed problems on which world i disagrees with both other worlds. For advice-rank r_i define

    J_i(X) = integral over M_i of r_i(X) dmu,
    E_i(X) = integral over all problems of r_i(X) dmu.

Consider the fixed lexicographic loss (J_i,E_i): first minimise errors on M_i; use total errors only to break a tie.

**Theorem.** Every guidance comparison and every PP9 protected defence is respected by this ranking, including the extended protected class in PP9 §7. Every nontrivial protected defence is strict at the first level.

**Proof.** Write delta_l=r_l(Y)-r_l(X), b_l=integral delta_l, and let {i,j,k}={1,2,3}. If X is regular on the changed problems, then pointwise

    delta_j + delta_k + 2 1_{M_i} delta_i >= 0.

For regular-to-regular changes on mixed problems this is equality: the other two worlds' changes sum to -2 delta_i on M_i and to zero elsewhere. Changes to contradiction, and changes away from correct unanimous advice, contribute a nonnegative remainder. These are all cases because the old advice is regular.

Hence

    2 [J_i(Y)-J_i(X)] >= -(b_j+b_k).

Every protected record has a regular old side (it has a coherent anchor) and b_l<0 at all three worlds. Therefore J_i(Y)-J_i(X)>0, so the protected defence X<Y is strict under the lexicographic ranking. Guidance makes J_i weakly increase and E_i strictly increase whenever the advice changes nontrivially, so guidance is respected strictly as well. QED.

Consequences:

1. Protected defences and guidance have **no strict cycles of any length**, not merely no forbidden triples.
2. Every finite collection of protected comparisons is endorsed by one ordinary strictly guiding additive loss alpha J_i+E_i for sufficiently large alpha. The required alpha can depend on the collection.
3. These comparisons do not themselves supply a finite cancellation violation. The entire collection is endorsed by the same two-level additive lexicographic loss.
4. This does NOT say that every extension containing them is additive, nor that the lexicographic loss satisfies (S). It usually does not.

## 3. The mirror rival that this lexicographic protection cannot handle

Choose equal-mass patches, of mass a>0, in the selected model's silent regions of M_1,M_2,M_3.

- Y_plus gives the majority advice on all three patches.
- Y_minus gives the minority advice on all three patches.

At every world i:

                     change in J_i       change in E_i
    C -> Y_plus             +a                  -a
    C -> Y_minus            -a                  +a

Thus ordinary total-error scoring prefers Y_plus to C everywhere, whereas the fixed minority-first lexicographic scoring prefers Y_minus to C everywhere.

Both rival families are legitimate, arbitrarily small changes of the same coherent model. A defence mechanism must handle both, and all their independent splices. Handling Y_plus alone can conceal a fixed priority for minority-world errors. Handling these two rivals alone is NOT an impossibility test: different worlds could defend them by different rankings. The constraints emerge when the whole splice family, other coherent anchors, (IB), and closed sections are included.

## 4. The next round: solve the coupled problem without a priced initial order

### The question

Can a single record-based allocation handle the two-sided splice family around nearby coherent selected models, including the PP8 doubly anchored rivals, while satisfying (G), (TC), the required face defences, and actual closed sections?

This is a test of the previously untreated interaction, not a demand to make the latest priority formula work. A positive solution of this local module would still need extension to the whole simplex and all rivals before it is a T1 cover. A negative result applies to the specified selected family unless its dependence on that family is removed.

### What must remain free

- No fixed additive comparisons, including comparisons between selected models.
- No 4:1 eligibility ceiling.
- No requirement to use the PP9 protected verdicts at every eligible world.
- No restriction to deletion from a previously chosen relation.
- No fixed or minimum-cost choice of defender.
- No global closed-graph condition in place of (S).
- Do not infer that the index of a selected model is a Bayes weight.

The 4:1 lemma remains available as a sufficient supply of candidates; it is not an axiom or a bound on admissible defenders.

### Concrete test module

Start with the exact PP8 pump and edge certificates, not new random grids. Include:

1. the selected models and the entire selected-index paths used in the section arguments;
2. the majority-advice rivals and their minority-advice counterparts;
3. independent measurable splices on the three mixed regions and the extra return region;
4. every transfer of the same disagreement into a different common context;
5. both directions' anchor-face obligations, especially the edge obligation in PP8 F-B;
6. closed sections with the rival genuinely fixed.

Also check that the asserted selected models are undominated within the module and that no incoherent rival ties with one at every world. These are necessary local checks for (LA) and direct (C); passing them does not establish the global axioms on a larger domain.

The key change is that the defences and the returns are chosen together, with neither set given precedence. Comparisons between selected models are variables too.

### Required outputs

**Constructive output:** an explicit formula or algorithm for a ranking on this atomless module, with a proof against all its rivals and the indicated selected paths. A list of assignments on finitely many models is not this output. Then attempt the full family with the same rule, rather than introducing a new protection priority.

**Adversarial output:** an implication chain using only the adopted axioms and the specified coherent family, ending in a contradiction. Every indispensable comparison must be justified by an axiom, a face obligation, or a fixed-rival limit. A return selected by an additive or margin rule is not compulsory.

A finite search may find exact records or suggest a formula. Fractional refinements and the continuum sections must be addressed before claiming a positive construction. Numerical sequences alone do not force a comparison unless their acceptance has been established independently of the failed rule.

### Stop conditions

- If unrestricted assignments work but the current priorities fail, stop patching those priorities.
- If a proof uses fixed minority-first evaluation, it has not supplied a new non-additive mechanism; §2 gives the diagnostic.
- If the only new theorem concerns another shrinking subclass, report that it does not settle the coupled problem.
- If a negative certificate uses the homothetic selection specifically, state that scope. It does not establish that T1 itself is uncoverable.

## 5. Why this is the recommended change

The last rounds repeatedly gave one side's verdicts priority and repaired the other side afterwards. The protected side is now seen to be a fixed lexicographic additive subsystem. The unresolved task is its coexistence with the opposite defences that (S) demands, especially when records have two coherent explanations.

The next round should therefore settle that coexistence directly, with the ordinary and lexicographic starting orders removed. It should not spend its main effort on finding a better numerical priority for the same starting comparisons.
