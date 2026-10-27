# Optional defenders, a sharp slack theorem, and symmetric repairs

21 October 2026. Author-checked, not independently refereed. Read PP5_diagnostic_and_repair.md. These results do not construct a full cover of T1.

## 1. What is actually forced by guidance and the defence clause?

Let C=D_K be coherent, with K supported on a nonempty set I of worlds. Let X be any measurable four-advice rival. Write

    P_i = U_i(X) minus U_i(C),
    Q_i = U_i(C) minus U_i(X).

Thus P_i records ways the rival is worse, and Q_i ways it is better. Ignore coordinate hyperplanes, which are null. If the record is nontrivial, its advice changes rank at every world.

**Lemma 1 (pointwise efficiency).** On almost every problem, changing C's advice makes it worse at at least one world in I.

Proof. On a problem unanimous over I, coherence requires C to give the correct advice. On a mixed problem, each of the three regular advice options is pointwise undominated across I: switching between regular options helps some worlds and hurts others. Contradiction is worse everywhere. C never advises contradiction. These exhaust the cases.

**Theorem 2 (no uniquely compulsory mixed defence).** Suppose i is the only world in I with nu(P_i)>0. Then nu(Q_i)=0: C is pointwise no worse than X at world i, and strictly better on a non-null set. Its defence there is already required by (G).

Proof. If X improved C at i on a non-null set, Lemma 1 would give a worsening at some other world in I on a non-null subset (there are finitely many worlds), contradicting nu(P_j)=0 for all j != i.

Therefore, if no world in I supplies a guidance defence, at least two worlds in I are legally available to defend the comparison. This statement has no additive, mass-ratio, or priority-order hypothesis. It applies to each face obligation in the anchor construction, because every compatible C_q is supported on supp q.

This does NOT say a global allocation can choose freely: (TC), closed sections, and protection of selected models couple the choices. It says that the unique non-additive defences in PP5 Proposition 4.3 are forced by the OPTIONAL eligibility pool, not by (G) and the defence clause alone.

## 2. A sharp replacement for the optional 2:1 pool

For kappa >= 1 define

    b_i = nu(P_i)-nu(Q_i),
    Phi_i^kappa = kappa nu(P_i)-nu(Q_i),
    D = {problems where C and X differ}.

Work in three worlds, with C coherent and X arbitrary, including contradictory advice.

**Theorem 3 (two alternatives with quantitative slack).** For kappa >= 3, and distinct i,j,k,

    Phi_j^kappa + Phi_k^kappa + ((kappa+1)/2) b_i
        >= ((kappa-3)/2) mu(D).

Consequently, if b_1,b_2,b_3 <= 0, at least two worlds satisfy Phi_i^3 >= 0. For kappa>3 the second-largest Phi_i^kappa is at least

    ((kappa-3)/4) mu(D).

In particular, kappa=4 gives two strictly eligible worlds with margin at least mu(D)/4 whenever D is non-null.

**Proof.** Prove the displayed inequality pointwise and integrate. Let delta_l be the change in advice rank at world l. The integrand of Phi_l^kappa is

    ((kappa-1)/2)|delta_l| + ((kappa+1)/2)delta_l.

For a change between distinct regular advice options on a mixed problem, |delta_l|=a in {1,2} at all worlds, and at least one delta_l is positive. Hence sum_l delta_l >= -a. The left-hand integrand is

    (kappa-1)a + ((kappa+1)/2) sum_l delta_l
        >= ((kappa-3)/2)a >= (kappa-3)/2.

If the new advice is contradictory, all delta_l are positive. The inequality then holds directly. On unanimous problems C gives good advice, and all delta_l are again positive for a nontrivial change. On unchanged problems both sides are zero.

For the second-largest bound choose i with largest Phi_i^kappa. Since b_i<=0, the sum of the other two Phi values is at least ((kappa-3)/2)mu(D), and hence the larger of those two has at least half that value.

The pointwise cases were additionally checked in exact rational arithmetic for kappa=3, 7/2, 4: 540 checks. The proof, not the enumeration, establishes the theorem for every kappa>=3.

**Sharpness of 3.** Use PP5's silence-to-majority changes in the three minority classes, with masses m_1=m and m_2=m_3=sm. Then

    b_1=(1-2s)m, b_2=b_3=-m,
    Phi_1^kappa=(kappa-2s)m,
    Phi_2^kappa=Phi_3^kappa=((kappa-1)s-1)m.

For any 2<=kappa<3 choose

    1/2 < s < min(kappa/2, 1/(kappa-1)).

All additive balances are negative and only world 1 is eligible. Such sets of sufficiently small prescribed masses exist in the silent regions of every interior member of the contamination family. Thus no coefficient below 3 (among those giving the original three-world counting guarantee) ensures two eligible defenders.

For PP5's s=3/4, changing kappa=2 to kappa=4 changes its first-link verdict vector from

    (1/2,-1/4,-1/4)m

to

    (5/2,5/4,5/4)m.

The comparison is then eligible everywhere. In particular its acceptance at world 1 is no longer compulsory, so the stated return refusal is no longer forced by that first link.

### Neighbourhood control

For the record metric rho used in PP5, Phi_i^4 has Lipschitz constant at most 15: its pointwise integrand lies in [-3,12]. Thus each of the two margin-bearing worlds remains strictly eligible throughout a ball of radius less than mu(D)/60. Choosing mu(D)/120 leaves half the guaranteed margin. This scales with the actual size of the disagreement; it is not a fixed lower size cutoff.

This does not prove that an arbitrary local reallocation preserves every face obligation. For the PP5 sticky records all changed old advice is silence, so a sufficiently small ball continues to have positive silent-old mass and hence no boundary anchor. On that ball the sole obligation is a defence at some world, and either positive alternative supplies it.

## 3. A repair that cannot create new (TC) failures at the world being thinned

**Theorem 4 (symmetric thinning).** Let R be any reflexive relation, whether or not it satisfies (TC). Delete a collection of unordered pairs: whenever a pair is deleted, remove both directed comparisons if present. Then every (TC) violation of the resulting relation was already a violation of R.

Proof. A surviving forward comparison has exactly the same status of its reverse as before: if the pair survived, both original directions survive. Therefore a surviving strict comparison was already strict. All three premises of a new forbidden triangle were present before, and its strict edge was strict before. So it was an old forbidden triangle.

For record-based relations, remove a set O of records with O=rev(O). This preserves (IB). If O is open, closed accepted-record sets remain closed. If O avoids guidance in both directions, (G) is preserved. The lemma was also checked on all 64 directed relations on three distinct objects and all eight unordered-pair deletion masks (512 cases).

**Application to PP5.** The reported new world-1 violations after the proposed repair arose because it removed d_ab while retaining rev(d_ab), and similarly for d_bc. Remove both directions instead. At world 1 this cannot create ANY new (TC) violation, not merely those tested on a grid. Use reversal-symmetric open neighbourhoods to retain closedness.

The opposite directions also have alternative defenders. From PP5's certified masses, already with kappa=2, rev(d_ab) is eligible at world 2 and rev(d_bc) is eligible at world 3. The forward directions are eligible at worlds 3 and 2 respectively. All these inequalities are strict and persist on small neighbourhoods.

This is not a complete repair: adding comparisons at the receiving worlds can introduce their own forbidden triangles. It does invalidate the inference that the one-sided repair's new world-1 triangles rule out the symmetric repair strategy.

## 4. What should change in the construction search

1. Stop treating a 2:1 error ratio as part of the problem. It was a convenient sufficient pool and creates artificial unique-defender constraints. The sharp theorem above gives a specific reason to start with 4:1 if a closed finite-ratio pool is useful, rather than adjusting constants blindly.
2. Do not infer that selected comparisons must follow a scalar potential. PP5 supplies that as one sufficient design, not a necessity, and (TC) allows longer cycles.
3. Handle a record and its reverse together when removing comparisons. Symmetric thinning gives a global no-new-violations guarantee at the thinned world.
4. For a candidate reallocation, check the receiving worlds, selected-model protection, and direct (C) explicitly. These remain the hard part. No result here establishes that repeated reallocations terminate or preserve the required covers globally.

The useful positive content is that non-additive defences need not be uniquely allocated, and the quantitative freedom is available at arbitrarily small scales. The full construction is still open. This note must not be cited as a cover or as an impossibility theorem for any unrestricted priority design.
