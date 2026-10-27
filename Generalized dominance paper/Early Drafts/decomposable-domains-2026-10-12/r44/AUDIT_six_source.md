# After round 43: reciprocal source protection and a coherent extension

Author-checked original argument, 22 October status exchange. Not independently refereed.

**Current strongest result: sections 13–15.** A genuine enlargement of the initial operation retains its comparisons, adds three coherent defenders, and handles arbitrary measurable advice changes on all six old A/B sets. All seven coherent sources remain undominated and mutually defended. (G), (IB), (TC), (LA), and direct (C) hold. At every world, the repair comparisons themselves have no finite strictly positive weak additive endorser. No (S) selection or full coverage theorem is proved. Earlier sections record the derivation and distinguish weaker results from this final extension.

## Scope and provenance

The local memo stops at round 42. PP15, PP16 and the round-43 referee report were not present in the accessible Documents tree when this was written. Consequently this is not a line-by-line audit of those reports. It assesses the quoted conclusions and independently proves the results below.

The guard construction should not receive another filter. Its missing invariant was not merely undominatedness of its sources, but the possibility of their reciprocal defences. The construction below installs reciprocal source defences BEFORE installing repairs. It is a different extension operation, although it too is partial: no (S) selection or general iteration theorem is proved.

## 1. A necessary reservation for every coherent defender

Write A <=_i B when A is no worse than B. Strict pointwise guidance is denoted <^G_i. Suppose T is selected at an interior index, C weakly dominates a rival X at all worlds, and the comparisons satisfy (G) and (TC).

If X <^G_i T, then T <=_i C is impossible. Otherwise

    T <=_i C <=_i X <_i T

violates (TC). This does not use transitivity or an additive representation.

In particular, let T be silent on a positive-measure set E where worlds 1 and 2 favour one answer and world 3 favours the other. Let X equal T except for giving the majority answer on E. Then X <^G_1 T and X <^G_2 T. Any all-world dominator C of X must therefore be defended against by T at world 3:

    T <=_3 C.                                            (R)

This follows from the defence clause of (S) at T. If C <^G_3 T, no such repair can occur in a full system with T selected.

This gives a simple explanation of the failure of own-world-improving vertex tilts. It is a constraint on the source of the repair, not its exposure margin. It also says how to choose a different source: C must incur some worse advice than T at world 3, rather than be a pointwise improvement there.

## 2. Why the opposite edge is not a general solution

Here is a second necessary condition, using only (IB) and undominatedness.

**Exposure necessity.** If C dominates X, T is undominated, and

    {C != X} intersect {X != T}

is null, there is a contradiction.

Indeed X=T throughout D={C!=X}. Copy the comparison record (C,X) into the common context T outside D. Its new side becomes T and its old side becomes Y, where Y=C on D and Y=T elsewhere. All weak comparisons, and the strict comparison witnessing dominance, transfer by (IB). Thus Y dominates T.

For the one-class rival in section 1, any coherent C supported on the opposite edge [e_1,e_2] gives the majority answer throughout E, since both those payoffs have the same strict sign. Thus C=X on E and exposure necessity fails. Such a C cannot dominate X while preserving T's undominatedness. This does not exclude every possible use of opposite-edge models, but it excludes their proposed use as dominators of these particular majority-answer rivals.

## 3. Choose a crossing credal set, not an own-world improvement

For T1 write

    M=c*1 + epsilon*Delta, c=(1-epsilon)/3, 0<epsilon<1.

Choose

    0 < d < min(1, epsilon/c, 2*epsilon/(c+epsilon)).

At gambles

    g_A=(1,1,-(2+d)),       g_B=(1,1,-(2-d)),

T is strictly silent: its lower prevision is negative and its upper prevision is positive.

Choose 0<h<c and the credal segment

    K = conv{(h,2/3-h,1/3), (2/3-h,h,1/3)}.

Every probability in K evaluates g_A as -d/3 and g_B as d/3. Therefore C=D_K gives the minority-3 answer on an open neighbourhood A of g_A and the majority answer on an open neighbourhood B of g_B. Shrink these to disjoint measurable positive-measure sets inside the strict silence region of T, retaining the sign pattern (+,+,-).

Neither credal set contains the other: K contains points with first coordinate below c, while M has varying third coordinate. Thus neither coherent model is simply a more informative version of the other.

The segment is only a convenient formula. A sufficiently small full-dimensional thickening of K inside the simplex preserves all strict inequalities and the failure of both containments. Hence the construction permits full-dimensional imprecise defenders as well. The defender is a variable subject to two open advice conditions on A and B, not a member of a prescribed selected family.

For epsilon=3/10, take h=7/60 and d=1/5. The endpoints of K are (7,33,20)/60 and (33,7,20)/60. Exact rational checks give:

| Problem | T lower | T upper | Every m in K |
|---|---:|---:|---:|
| (1,1,-11/5) | -53/75 | 19/75 | -1/15 |
| (1,1,-9/5) | -37/75 | 26/75 | 1/15 |

No numerical approximation is needed for the general argument.

## 4. The extension operation

Let D={T!=C} and H its complement. Both A and B lie in D. The domain is ALL measurable four-advice models, modulo null sets.

For each non-null measurable E subset A, let X_E agree with T outside E and give the majority answer on E. In particular, {C!=X_E}=D: on E the three advice values of T,C,X_E are respectively silence, minority, majority; elsewhere X_E=T.

Start with guidance. More generally one may start with a relation R^0 satisfying (G), (IB), (TC), with all nonguidance records supported in H, in which T and C are undominated and there are no distinct all-world ties.

Install the following records, with ALL their common-context copies:

    worlds 1 and 2:   C <= T;
    world 3:          T <= C;
    every world:     C <= X_E, for every non-null measurable E subset A.

These are the only additional comparisons. In particular we do not take their transitive closure.

The first two lines reserve mutual defences of the two coherent sources before any domination comparison is added. They are not selected indices or a claim that a full selection already exists.

## 5. Extension theorem

**Theorem.** The operation satisfies (G), (IB), and (TC) globally on the full measurable domain. T and C remain undominated. Every X_E is strictly dominated at all worlds by C. T and C defend themselves against each other, with strict comparisons. There are no newly created ties. Starting from guidance, (LA) and direct (C) follow.

**(IB).** Whole record classes are installed. No common context is inspected.

**Strict (G).** At worlds 1 and 2, both kinds of added comparison worsen advice on B: C gives a correct answer there whereas T and X_E are silent. At world 3, T <= C worsens advice on B, while C <= X_E worsens advice on E. Thus no added comparison reverses guidance. Their reverses are neither guidance nor old nonguidance records supported in H.

**(TC), worlds 1 and 2.** Every new record has the same support D and the same old advice C throughout D. Its new advice differs from C throughout D. Consequently two new records cannot compose, even after arbitrary common-context substitutions. One new record cannot form a cycle with two old records: on B it strictly worsens advice; old nonguidance records are zero on D, and guidance can only worsen it further.

**(TC), world 3.** Denote the record T->C by a and C->X_E by b_E. All have support D.

* Neither a followed by a nor b_E followed by b_F is composable.
* b_E followed by a is not composable: on E, b_E ends with the majority answer while a starts with silence.
* a followed by b_E IS composable. Its net record is T->X_E: silence changes to the wrong answer on E, and all other changes cancel. It is a strict guidance worsening at world 3.

Thus this composable pair cannot be closed into a forbidden triangle by guidance or an old nonguidance record supported in H. A cycle with one new record is excluded by its strict worsening on B or E. A cycle of three new records is excluded by the composition list. Old triples satisfy (TC).

This is the important difference from the guard proof: useful composition is permitted, but its net effect is guaranteed to be harmless at the world where it is permitted.

**Strictness and ties.** At worlds 1 and 2 all new records start with C, so none is the reverse of another. At world 3, the reverse of a is not b_E, because E is non-null; the other reverses likewise are not installed. The guidance and support observations exclude old reverses. Hence all newly installed comparisons are strict. No new ties appear.

**T remains undominated.** The only new comparison ending at T is C <= T at worlds 1 and 2. A copied record ending at T has source exactly C, because its full disagreement is D. No repair ends at T: on E its new advice differs from T. Thus a new dominator would have to be C. But C <=_3 T is refused: it is not guidance (B witnesses worsening), not an old record supported in H, and not an installed record. All other potential dominators have unchanged incoming comparisons at T.

**C remains undominated.** The only new comparison ending at C is T <=_3 C, again with source exactly T. T <=_1 C and T <=_2 C are refused, since B witnesses their failure of guidance and their disagreement is not in H. Repair records cannot end at C. Thus no new dominator of C is created.

**(LA), direct (C).** From guidance, coherent T and C are initially undominated, so (LA) follows from their preservation. Guidance has no distinct ties, and none is added. Thus direct (C) holds. QED.

The theorem holds for the entire continuum of measurable E, not just a finite partition, and for arbitrarily small positive-measure E. It also holds for any subcollection of those repairs.

## 6. Non-additivity: distinguish two claims

The repair mechanism itself cannot be represented by finite strictly guiding additive losses preserving its strict comparisons. At world 3 it requires

    T <_3 C <_3 X_E

for EVERY non-null E subset A. For an additive representation, write delta=L_3(C)-L_3(T)>0 and let nu(E)>0 be the cost of changing silence to the wrong answer on E. Then

    0 < delta < nu(E).

Take infinitely many disjoint non-null E_n subset A. A finite positive charge, even finitely additive, cannot have nu(E_n)>delta for every n. Contradiction.

This is an essential ordinal distinction among the actual coherent sources and the repaired rivals. It is not a strict cycle located elsewhere in the domain.

HOWEVER, the weak-endorsement notion used in the T1 reductions is weaker. An endorser need only satisfy L_3(T)<=L_3(C)<=L_3(X_E), and may assign L_3(T)=L_3(C). The preceding argument forces that equality but does not exclude an endorser. It would be incorrect to claim otherwise. Non-Archimedean representations are not excluded either.

### Optional: retain non-endorsement from coherent undominated sources

There is a compatible non-priceable base on H. Accept guidance and, at world i, records supported in H whose old side is T and whose new side is strictly worse at i on a non-null set. Because C=T on H, no such record ends at either T or C.

This base has no nontrivial accepted finite cycles: once a target-reference step moves away from T to a worse rank on a witness set, guidance cannot return, and another target-reference step can act there only after the advice has already returned to T. A first-return argument gives a contradiction. Coherent T,C are undominated under the base, since any nonguidance incoming comparison to either is impossible.

The extension theorem therefore applies. In H there are open common-advice regions where T,C give good advice at i, and others where they give bad advice at i. This follows by making one positive coordinate sufficiently large, since both credal sets are contained in the simplex interior. Choose disjoint non-null A_n in the former and a fixed non-null B' in the latter. Silence T on A_n union B'. The base accepts every resulting comparison from T. Any finite strictly positive weak endorser would require the positive charge of A_n's first rank step to exceed the same positive charge of B's second rank step for all n, an impossibility.

This gives global failure of finite positive weak endorsement from an actually undominated coherent source. But it does NOT show that non-endorsement is indispensable to the repair module: that module already works from guidance alone. The distinction should remain explicit.

## 7. What this does and does not change

Proved:

* a coherent defender with flexible, nonnested credal geometry;
* reciprocal source defences installed along with the repairs;
* preservation of both coherent sources' undominatedness;
* (G), (IB), (TC), (LA), direct (C), and strict all-world domination of every X_E;
* the same result for arbitrary measurable subsets, including arbitrarily small ones;
* no finite additive representation of the strict repair comparisons;
* an optional compatible base with genuine failure of finite positive weak endorsement.

Not proved:

* any selection satisfying (S), including its fixed-rival closed sections;
* domination of arbitrary rivals, or all local-freedom variants;
* compatibility of three rotated copies of this module;
* iteration of the extension with arbitrary old records;
* full coverage.

The full domain satisfies local freedom as a domain condition, but the repaired rival class is much smaller than all local-freedom variants. The theorem must not be advertised otherwise.

There is also an intentional discontinuity: X_E can converge to T as mu(E) tends to zero, while C <=_3 X_E and C <=_3 T is refused. This is discontinuity in the RIVAL argument, not itself a violation of the fixed-rival section requirement in (S). Whether it can coexist with a full (S) selection is open.

The source/rival records in this module have the SAME full disagreement support D. That is a substantive compatibility restriction; it has not been lifted. The operation handles a continuum of rivals but is not yet a general extension lemma.

## 8. Recommendation

Retire guard filters and do not switch to a fixed continuum of intermediate selected models on the strength of an obstruction to the guard class. A continuum may be necessary for that class without being sufficient or necessary in general.

The next substantial test is to co-design two different coherent defenders, protecting all mutual source defences from the start, for TWO independently variable classes of silent-patch rivals. Allow their credal sets to vary; do not require rotated copies or membership in the posterior family. The task is to make permitted compositions end in guidance-worsening records at their assigned worlds, as above, rather than forbid composition altogether.

Success must cover every measurable subset of both classes, not selected grid cases. Failure must yield a theorem about the paired-source mechanism, not merely one set of numerical credal sets. Closed sections must then be tested with a fixed rival and moving sources; no claim of proximity to (S) is justified before that.

The unselected-clone route remains logically open on the information available. The present proof does not eliminate it. Neither an all-world clone nor a continuum of intermediates should be called a construction until its (IB) copies and actual source defences have been checked.

**Update within this investigation:** the two-class test just proposed can in fact be passed. Sections 9–12 give a stronger three-source extension, including arbitrary advice on three independently variable sets. They supersede that proposed next task, but do not settle (S).

## 9. Three coherent sources can be designed together

For each i let K_i be the rotation of the segment in section 3 having coordinate i fixed at 1/3 and the other two ranging between h and 2/3-h. Put C_i=D_{K_i}. Again each K_i can be slightly thickened to a full-dimensional credal set, and neither it nor M contains the other.

Choose d>0 sufficiently small to satisfy the bounds in section 3 AND to put both 1/(3+d) and 1/(3-d) strictly between h and 2/3-h.

For each i choose disjoint open problem sets A_i,B_i near the rotations of

    g_A=(1,1,-(2+d)), g_B=(1,1,-(2-d)),

with the negative coordinate at i. On all six sets T is strictly silent. Their advice table is:

| Set | T | C_i | Every C_j, j!=i |
|---|---|---|---|
| A_i | silence | minority-i answer | silence |
| B_i | silence | majority answer | silence |

The strict silence of C_j follows because its varying coordinate i takes values on both sides of the threshold 1/(3+d) or 1/(3-d).

We also need a protection condition for common-context copies. For each distinct i,j, let k be the remaining world and choose

    (1-c)/c < L < (1-h)/h.

Near the gamble whose coordinate k is L and whose other coordinates are -1, T accepts the minority-k answer, while C_i and C_j are both strictly silent. Let W_ij be a small positive-measure set with this property. These sets are outside all A_i,B_i because T is definite there.

These strict conditions are stable under small full-dimensional thickenings of the K_i. They are also the only geometric conditions used below: a different set of credal sets satisfying the same advice table and overlap witnesses works equally well.

## 10. Repair every measurable change on A_1 union A_2 union A_3

Let A=A_1 union A_2 union A_3. A rival X may give ANY measurable advice on A, including contradiction, and agrees with T elsewhere. Let

    J(X)={i: X gives strictly worse advice than T at world i
               on a non-null subset of A}.

For every X!=T, J(X) is nonempty: T is silent on A, and every nonsilent answer is wrong at some world on these mixed problems, while contradiction is wrong everywhere.

Start with guidance. More generally allow an old relation as before whose nonguidance supports are contained in

    H={T=C_1=C_2=C_3},

with all four coherent sources initially undominated.

At world w install these source comparisons:

    T <=_w C_w;
    C_i <=_w T             for i!=w;
    C_i <=_w C_w           for i!=w.

Thus the other two coherent defenders are above T at w, and C_w is below T. No comparison between those other two defenders at w is needed. Across worlds every pair of coherent sources has reciprocal defences.

For EVERY X!=T of the stated kind and EVERY i in J(X), install

    C_i <=_w X             at EVERY world w.

As always, install whole disagreement-record classes in all common contexts. This makes the choice of coherent defender depend on the rival: choose any world at which X worsens T, and use its C_i. More generally one can choose the credal sets themselves subject to section 9's open conditions.

## 11. Three-source extension theorem

**Theorem.** The operation in section 10 preserves (G), (IB), (TC), and the undominatedness of T,C_1,C_2,C_3. Every distinct X that agrees with T outside A is strictly dominated at every world by at least one of the coherent undominated C_i. All installed source comparisons and repairs are strict. Starting from guidance, (LA) and direct (C) hold. The four coherent sources defend themselves against each other.

**Cycle argument.** Fix a world w. Every newly installed record with old source C_i for i!=w strictly worsens advice on B_i: there C_i gives the correct majority answer while T, C_w, and every rival X are silent. Every other installed record is either zero on B_i or also worsens it. Old nonguidance records supported in H are zero there, and guidance cannot improve it. Therefore no accepted cycle containing a record with such a source C_i can occur.

The only new records left to check at w are

    a: T->C_w,        b_X: C_w->X with w in J(X).

On B_w, a changes silence to the bad answer, while every b_X makes the reverse change. Two a records cannot compose, nor can two b records. Three records of these two kinds cannot close a cycle: their changes on B_w cannot balance.

If a and b_X compose in either order, their net advice-change vector is X-T, pointwise. This statement uses advice indicators, not merely rank increments. Wherever the net change is nonzero the composite has the same old and new advice as (T,X); where it is zero the two changes cancel. Since w is in J(X), the composite strictly worsens advice at w on a non-null set. It cannot be closed into a forbidden triangle by guidance. An old nonguidance record supported in H cannot close it either, because the whole change is outside H.

A single a worsens advice on B_w. A single b_X worsens advice on a witness for w in J(X): on A_w, C_w gives the correct answer, while on A_j for j!=w it is silent like T. Thus X being worse than T at w ensures it is worse than C_w there. Such a record cannot be closed into a cycle by two guidance/old records. This completes (TC).

**(G) and strictness.** The worsening witnesses just used exclude guidance reversals. Reverses are not old nonguidance records supported in H. Reverses of records with source C_i, i!=w, improve advice on B_i, whereas every new record is nondecreasing there. For a and b_X, the reverse of a cannot equal a repair unless X=T; a reverse repair could equal a only if X=T, and cannot equal another repair because of B_w. Thus every new comparison is strict and no new ties arise.

**No repair record ends at T or any C_k.** For T, a witness for i in J(X) gives X!=T and C_i!=X, by the advice table, so the exposure is non-null. The same witness prevents the record from ending at C_i. For C_k with k!=i, use W_ik: there C_i and C_k are silent, X=T is definite, and the new side of the repair differs from C_k. These facts hold in every common context.

**Other incoming comparisons at T.** Only C_i->T can newly end at T, and its source is exactly C_i. But C_i <=_i T is refused: B_i rules out guidance, the pair does not have support in H, and no installed source comparison at i has this direction. Therefore no C_i dominates T and no other new dominator is introduced.

**Other incoming comparisons at C_k.** A source comparison ending at C_j cannot be copied into C_k for j!=k: on B_j, its new side is C_j's majority answer and C_k is silent. A C_i->T record cannot end at C_k either: for i!=k use W_ik, and for i=k use their disagreement. Thus the only new incoming comparisons at C_k are the original source comparisons at world k, from T or C_i (i!=k).

T does not dominate C_k because at any w!=k guidance refuses T <=_w C_k on B_k, and no other old or new record supplies it. C_i does not dominate C_k because at world i, B_i makes C_i worse than C_k, and no old or new comparison supplies that direction. All other potential dominators have unchanged incoming comparisons. Hence C_k remains undominated.

The remaining claims follow as in section 5. QED.

### A necessary division among defenders

There is a useful general constraint behind this assignment. If T is selected, a single coherent defender cannot dominate both a majority-fill rival harming only world i and a majority-fill rival harming only a different world j. For any world w, at least one of those rivals strictly improves T at w. Section 1 would therefore forbid T <=_w C at EVERY world, violating T's defence against C. This uses no geometry of the new construction.

The three-source construction respects this division: a majority fill on A_i is assigned only to C_i. Other changes may have more than one eligible defender. This is a derived constraint on co-design, not an arbitrary priority assignment.

## 12. Significance and remaining boundary

This supersedes the single-class result as the main positive theorem. It handles arbitrary, simultaneous, measurable changes on three independent open sets with different minority worlds. The defender may vary with the rival. The coherent sources are imprecise, may be full-dimensional, are not nested with the target, remain undominated, and have reciprocal source defences. Permitted compositions have a controlled net effect; noncomposition is no longer the sole consistency mechanism.

At EVERY world i the strict chain T <_i C_i <_i X_E for majority fills on arbitrarily small E subset A_i rules out a finite additive representation preserving the strict comparisons. This still does not, by itself, rule out a weak endorser that ties T and C_i. The optional target-reference base can be placed on common H to rule out finite positive weak endorsers as well. It remains a separate source of non-endorsement, not a proof that the repair module needs that base.

The remaining limitation is substantial: rivals must agree with T outside A. In particular the B_i and W_ij patterns remain fixed. These are doing real work in the proof, so this is not permission to repeat the construction blindly. The full domain is retained throughout; (LF) as a domain condition holds, but domination of ALL local-freedom variants is not proved.

There is still NO (S) selection, vertex/edge completion, or general iteration theorem. A finite mutually defended coherent family is not a substitute for those conditions. No claim that T1 is covered, or close to covered, follows.

The next demanding test should therefore be to let rivals vary on B_1 union B_2 union B_3 while simultaneously choosing replacement coherent defenders and retaining the already installed comparisons. That tests the actual invariant: reciprocal source protection plus harmless compositions. It should be posed as one existence-or-obstruction theorem for this co-designed source class, not as a succession of exposure filters. A result only for another finite list of rivals would not answer it.

**Update:** this enlargement can also be carried out. The following theorem retains the old comparisons and removes exactly that restriction on the B_i. It introduces new compensation sets R_i; arbitrary iteration remains unproved.

## 13. A genuine second extension: let the old B sets vary

Keep the three C_i of section 9. Choose d>0 sufficiently small, and define a=1/(1-d). Let F_i be the coherent model obtained by rescaling C_i's credal set in coordinate i by a and renormalising. Its probabilities have coordinate i equal to 1/(3-2d). In particular

    F_i is pointwise no worse than C_i at world i.

Choose three small open sets A_i,B_i,R_i around gambles with other coordinates 1 and coordinate i respectively

    -(2+d),   -(2-d),   -(2-3d).

For sufficiently small d all these sets lie strictly in T's silence region, are disjoint, and have the table:

| Set | T | C_i | F_i | C_j,F_j for j!=i |
|---|---|---|---|---|
| A_i | silence | minority-i | minority-i | silence |
| B_i | silence | majority | minority-i | silence |
| R_i | silence | majority | majority | silence |

One can require 3d<min(1,epsilon/c,2epsilon/(c+epsilon)) and then reduce d further to preserve the other sources' strict silence. The C_i/F_i disagreement on B_i makes F_i strictly better than C_i by guidance at i. At either other world their advice on B_i goes from good to bad.

The shared overlap sets W_ij from section 9 can be retained after reducing d: T is definite there, while BOTH members of group i and BOTH members of group j are silent. All geometric conditions are strict, so the old credal segments may be thickened before rescaling if desired. There is no need to identify the target or any defender with a precise model.

Call {C_i,F_i} group i. Let a rival X agree with T outside

    A_1 union A_2 union A_3 union B_1 union B_2 union B_3.

Its advice inside these six sets is arbitrary and measurable.

At world w install source comparisons:

    T <=_w S                  for S in group w;
    S <=_w T                  for S in group i, i!=w;
    S <=_w Q                  for S in group i!=w, Q in group w;
    C_i <=_w F_i              for i!=w.

Guidance already supplies F_w <_w C_w. Thus EVERY pair among T and the six coherent defenders has a defence in both directions at some worlds.

A source S in group i is eligible to dominate X when

    mu({g: r_i(X(g))>r_i(T(g)) and r_i(S(g))<=r_i(T(g))})>0.   (Q)

Install S <=_w X at ALL worlds for every eligible source, with every common-context copy. Every X!=T has an eligible source. On A_i, a wrong answer for i is handled by C_i or F_i; on B_i it is handled by F_i. An answer wrong for another world is handled by that world's silent sources. Contradiction is included in the same argument.

This operation retains every source comparison and repair of section 10. It genuinely enlarges the evaluated rival class without retracting the earlier comparisons. The optional target-reference base was not needed for this extension and is not being retained here.

## 14. Proof of the six-source extension theorem

**Theorem.** From guidance, the rule of section 13 satisfies (G), (IB), (TC), (LA), and direct (C). All seven coherent sources remain undominated, have reciprocal defences, and every distinct rival in the enlarged class is strictly dominated at every world by an undominated coherent source. No finite strictly positive additive charge weakly endorses all the relevant comparisons at any world.

Here is the consistency proof, including the new case rather than merely an appeal to the earlier theorem.

Fix world w. Every new record whose old source is in group i!=w and whose new side is T, a group-w source, or a rival X, strictly worsens advice on R_i: correct majority becomes silence. Every other record is nondecreasing there. In particular C_i->F_i is zero on R_i. Such a record cannot occur in an accepted cycle.

After excluding these records from a possible cycle, the remaining nonguidance types are:

    a_S: T->S, for S in group w;
    b_SX: S->X, for S in group w eligible by (Q);
    r_i: C_i->F_i, for i!=w.

All a_S change silence to the bad answer on R_w. All b_SX make the reverse change there. The r_i are zero there.

First consider a cycle containing r_i. On B_i this record worsens advice by TWO ranks (good to bad). Every a_S and every other r_j is zero there. A b_SX starts from silence on B_i, so it can improve by at most ONE rank. Guidance cannot improve rank. Thus a three-cycle containing r_i and at most one b_SX is impossible. A three-cycle containing r_i and TWO b_SX is also impossible: on R_w those two records both change bad advice to silence and r_i is zero. Two copies of r_i cannot compose on B_i. These observations exhaust three-cycles involving an r_i.

Now only a_S and b_SX remain. Two a records cannot compose on R_w, nor can two b records. Three such records cannot balance their +/-1 changes on R_w. A composable a_Q,b_SX pair, in either order, has a positive rank change at a witness for (Q):

* if a_Q acts before b_SX at that problem, the composite starts with T and ends with X;
* if a_Q does not act there, the composite starts with S, which is no worse than T, and ends with X;
* if b_SX acts first, a_Q cannot subsequently act there, because X differs from T there.

Therefore such a pair cannot be closed by guidance. A single a or b has a positive-rank witness as well. This proves (TC) for arbitrary common-context copies. (IB) is by construction.

All added comparisons have strict worsening witnesses, so they do not reverse guidance. None has an installed reverse: for records eliminated using R_i this follows from monotonicity on R_i; for a/b use R_w and (Q); for r_i use the support distinction (a/b change R_w or a source-group R_j, while r_i is zero on all R_j) and its good-to-bad change on B_i. Thus all new comparisons are strict and no new ties are created.

**Source protection.** No repair ends at T, by its witness for (Q). No repair with a source in group i ends at a coherent source in the same group, because on R_i its new side is silent whereas both coherent sources give the majority answer. It cannot end at a source in another group j, by W_ij: there its new side is T's definite answer and both groups are silent.

A source comparison whose new side is in group i cannot end at another group, because of R_i, nor at the other member of its own group, because of B_i. A source-to-T record cannot end at any coherent source: use its own R_i or a shared W_ij. The within-group record C_i->F_i ends, among the named coherent sources, only at F_i, with source exactly C_i.

Consequently any new dominator of a coherent source must be one of the named sources. None is a dominator:

* C_i or F_i cannot dominate T: at world i, R_i makes it worse than T and that direction is not installed.
* T cannot dominate a group-i source: at any other world, R_i makes T worse and that direction is not installed.
* A group-j source cannot dominate a group-i source, i!=j: at world j, R_j makes the proposed dominator worse, and that direction is not installed.
* C_i cannot dominate F_i: at world i strict guidance gives the reverse.
* F_i cannot dominate C_i: at either other world B_i makes F_i worse, and the installed within-group comparison gives the reverse.

Thus all coherent sources remain undominated. Guidance alone has no distinct ties; the extension creates none. This proves (LA) and direct (C).

### Non-endorsement is now intrinsic to the repairs

Fix i. Suppose a finite strictly positive additive charge weakly endorses all comparisons from the coherent undominated sources at i. Denote its induced finite error cost by L.

The source comparison T <=_i F_i requires L(T)<=L(F_i). Strict guidance and positivity give

    delta=L(C_i)-L(F_i)>0.

For infinitely many disjoint non-null E_n subset A_i, let X_n equal T except for giving the majority answer on E_n. The old source C_i is eligible for every such rival, so

    L(C_i)<=L(X_n)=L(T)+nu(E_n)<=L(F_i)+nu(E_n).

Hence nu(E_n)>=delta for every n, contradicting finiteness of the positive charge on A_i. Finite additivity is enough for the contradiction; countable additivity is unnecessary.

This argument uses comparisons among the actual coherent sources and the actual repaired rivals. It does NOT use the optional target-reference base, and it is not merely a failure of strict numerical representation. It excludes weak endorsement itself. The obstruction is on a fixed small open set A_i, not at a nearly unanimous end of a chain. The same proof works at all three worlds.

No claim about every unbounded or non-Archimedean representation follows from this argument.

## 15. Verification and the remaining research question

The measurable proofs above are the basis for the claims. Supplementary exact scripts are in `reciprocal-source-check/`:

* `check.py`: all 64 advice assignments on the three A cells, 173 distinct records per world; all common-context two-record compositions and three-record cycles, plus source undominatedness checks;
* `extension_probe.py`: enlargement at one B cell with a new defender, all 256 advice assignments on four cells; passed the finite signature checks;
* `six_source_probe.py`: all 153 nontrivial advice assignments changing at most two of six A/B cells; supplementary checks of the six-source enlargement.

Finite-cell checks are not evidence for (S). They only check the stated record algebra and representative geometric signatures. The full measurable rival claim comes from the proof, not from those checks.

The core question is no longer whether the first compensation sets can be released: this construction releases them while retaining the old comparisons and coherent sources. The next boundary is R_1 union R_2 union R_3 and the overlap witnesses W_ij. A further extension must also address the fixed-rival closed sections of (S), rather than merely add more such sets.

The construction has not supplied a full selection, ideal vertex defences by selected sources, or a general extension theorem for arbitrary old records. It does not solve T1. It does, however, give a coupled three-world, target-preserving, measurably infinite repair system with genuinely non-endorsable comparisons at every world and reciprocal protection of its coherent sources. That is a stronger positive result than the guard construction or a non-additive seed alone.
