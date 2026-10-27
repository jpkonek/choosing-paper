# Independent corner cuts and gate compatibility

23 October 2026. Author-checked mathematical proposal; no independent referee. This constructs a coherent family and simplifies a sufficient ranking construction. It does not construct rankings satisfying the full milestone.

## Assessment of PP42

The fixed-rival section proof uses a potentially valuable general mechanism: compactness of the gate family, convergence in measure of its models, convergence of its fields under a common integrable envelope, and acceptance of zero-valued gate records. This deserves to be preserved separately from the particular cap fields.

Repairs needed in the statements:

* The witness hypothesis in Theorem 2.1 gives necessity of Bayes optimality for competitiveness, not sufficiency for an arbitrary subrelation of the witness preorder. A nonnegative witness value need not be accepted.
* Theorem 3.1(c)'s necessity of CG2 includes a common-agreement region on which the models are not world-perfect. Do not state unrestricted equivalence with TC. Strong CG3 is sufficient; its weak necessary version is not the same condition.
* Theorem 4.3(c) establishes absence of a globally consistent collection of rescaling constants. By itself that is not absence of every possible additive endorser.
* Theorem 4.3(a) uses an integral ratio bound R as a pointwise bound. Supply the pointwise bound or a different proof of pointwise Bayes optimality.
* Proposition 5.1 excludes the stated eventual-domination configuration under (U). It does not establish general local finiteness of dominator indices.

## 1. A three-parameter coherent family

Let M = c 1 + epsilon Delta, where c=(1-epsilon)/3. Choose 0<delta<epsilon/3. For s=(s1,s2,s3) in [0,delta]^3 define

    K_s = M intersect {m_i <= c+epsilon-s_i for i=1,2,3},
    C_s = D_{K_s}.

The centre u lies in every K_s. The family is compact in the Hausdorff metric, C_0=T, and its advice varies continuously in measure. The latter follows from convergence of the support functions and the fact that, for a fixed s, the finitely many polytope boundary planes are Gaussian-null.

Write K_i(t) for the single-corner cut and H_i(t) for the problems where D_{K_i(t)} differs from T.

**Union lemma.** Up to null sets, C_s differs from T on precisely the union of H_i(s_i). On this union it gives the corresponding single-cap answer. These three sets are pairwise disjoint, and the added answers agree with the sign of u dot g.

**Proof.** In M the removed corners O_i={m_i>c+epsilon-s_i} are pairwise disjoint: s_i+s_j<epsilon makes simultaneous membership impossible. Suppose g is accepted by K_s and not by M. Outside the null boundary cases, the nonempty set {m in M:m dot g<=0} is convex and hence connected. It misses K_s, so it lies in the disjoint union of the O_i. Connectedness puts it wholly inside one O_i. Therefore the corresponding single-cut K_i(s_i) already accepts g. The converse follows from K_s subset K_i(s_i). Apply the same reasoning to -g. A nonempty excluded half-space cannot lie in two disjoint corners, so two single cuts cannot supply the new answer simultaneously. All K_s contain u, so conflicting definite answers are impossible. QED.

Consequences:

* We can vary all three cuts independently without solving coherence again.
* At any fixed problem, every family member gives either silence or the same definite answer. No triple of members has three distinct advice values.
* The family contains the eight models of every small coordinate box, not just three unrelated one-dimensional paths.
* This is a family of candidate models. It is not a declaration that they are all undominated or selected. Those conclusions require a ranking.

Exact rational diagnostic: 100 independently sampled cut triples, 100 integer gambles per triple, and all eight sub-cut models gave 80,000 successful checks of the union identity. This supports bookkeeping, not the proof's continuum quantifiers.

## 2. CG3 becomes a triangle condition on intervals

Fix a world and two distinct gated members N,M. Use PP42's f^N and f^M for the move N to M. Define the interval for x_N-x_M by

    L_NM = log ess sup_{f^N<0} (f^M/f^N),
    U_NM = log ess inf_{f^N>0} (f^M/f^N).

An absent negative region gives lower bound -infinity; an absent positive region gives upper bound +infinity. Under the stated positive-ratio bounds, these have their usual meaning. CG2 is exactly the feasibility of

    L_NM <= x_N-x_M <= U_NM,

where c_N=exp(x_N). Reversing the pair reverses the interval: I_MN=-I_NM.

For three members A,B,C, common pair constants exist exactly when each interval is nonempty and

    0 belongs to I_AB + I_BC + I_CA.

For finite closed bounds this says sum L <= 0 <= sum U. For the strict sufficient version use open feasible intervals and strict cycle inequalities; this is stronger than merely demanding pointwise strictness at an unattained essential extremum.

**Proof.** The three differences must sum to zero. Conversely, choose one number from each interval with zero sum, set x_A=0, and reconstruct x_B,x_C. QED.

By the union lemma, PP42's extra pointwise CG3 condition on three different advice values is vacuous for this family. Thus, conditional on PP42's sufficient local-witness theorem, these interval triangle conditions are a concrete sufficient TC test. They are not asserted to be necessary for every permissible ranking.

Do not demand one choice of x_N for the entire family. The sufficient TC argument needs constants for each triple. Global consistency would be an additional restriction.

## 3. Proposed construction task

Assign strictly guiding fields to all C_s. Permit each field to change on all three corner bands, including bands on which its own model is still silent. Keeping the target field off each model's own band is optional and causes PP42's cross-cap conflict.

Seek simultaneously:

1. Each C_s is uniquely Bayes for its own field at a weighting in its assigned index support. The weighting need not be uniform or identical across members.
2. Every pair and triple passes the interval test, at each world.
3. The fields vary continuously in measure with s and have a common integrable envelope on this compact local family. With a zero-accepting gate rule and strict sufficient compatibility, PP42's section argument then extends to the whole parameter cube.
4. The fields endorse the first recursive fills and retreats, including those missed by the single-cap path. No universal choice of dominator is imposed.

The first nontrivial test is T, two individual caps, and their combined cut. Then include the full eight-model box and shrink the cut sizes towards zero. A finite successful test alone is not the required result: find a formula or uniform construction valid for an open box of cut sizes and all measurable rivals.

The parameter cube is geometric, not the probability-index simplex. To obtain a selection, choose a suitable two-dimensional parameter surface and an explicit map from a patch of the probability simplex, then verify support conditions. No continuity of the ranking beyond the stated sufficient construction is imposed as an axiom.

This attacks simultaneous repair in three directions before adding an edge. If all such fields fail, distinguish failure of this gated sufficient class from failure of G, IB, TC and S themselves. In particular, do not promote CG3 to a necessary axiom.
