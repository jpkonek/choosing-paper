# Round 65: simpler ranking and an infinite-world extension

26 October 2026. Audit of the universal-coverage note, REF65_hA, REF65_hB and AD65. The new propositions below are audit proofs, not independently refereed.

## 1. Assessment

The decisive mechanism is now explicit: optimise inside the rival's own coherent hull, then shrink the resulting coherent acceptance set so that the removed advice still generates the original hull. Every new acceptance is therefore a consequence of the removed advice. Such a change cannot be applied to a coherent model. This supplies strict score improvement without threatening any coherent model.

REF65_hA's contraction proof is the right main proof. The generation lemma, density-point certificates, finite facet bounds and designated-world deletion bookkeeping are unnecessary for the universal theorem.

## 2. The ranking can be simpler than either published variant

For a disagreement from Y to X write A=X\\Y, B=Y\\X, and

    d_omega(A,B)=integral_A h(omega) dmu - integral_B h(omega) dmu.

Call the record safe if it cannot be applied to any coherent model: there is no coherent C containing B a.e. and missing A a.e. In the current hull setting this is equivalent to

    mu(A intersect hull(B)) > 0.

Define X <=_omega Y exactly when:

- the record is guidance at omega (including the null record); OR
- the record is safe and d_omega(A,B)>0.

No zero-score comparisons, lexicographic levels, sum across worlds, or designated deletion world are needed.

### Proposition

In the finite-world setting of round 65 this ranking satisfies reflexivity, a.e. identification, strict (G), (IB), (TC), finite-chain consistency and (Add). Every coherent model has no weak dominator except itself. Every incoherent model is strictly dominated at every world by a coherent model. Thus (W), global coherence and direct (C) hold.

Proof:

1. Every accepted non-null record has strictly positive score increment at its world, including guidance. Thus every nontrivial accepted comparison strictly increases that world's scalar moment. An accepted cycle must consist only of null records. This proves (TC) and finite-chain consistency, and excludes nontrivial single-world ties.
2. The rule depends only on (A,B), giving (IB); guidance is included and its reverse has negative increment.
3. If two disjoint accepted records are both guidance, their union is guidance. Otherwise one is safe. A coherent model carrying the union would carry that safe subrecord, a contradiction. The union is safe and its score increment is positive. This gives (Add).
4. Any non-null record applied to a coherent C is unsafe. If it were accepted at every world it would therefore be guidance at every world. Such a record is null: its additions are universally positive and already in C, while its removals are universally negative and cannot belong to U.
5. The strengthened H theorem supplies a coherent N with strictly positive increments at every world and a safe record from X to N. That record is accepted strictly everywhere.

This uses AD65's plain-Brier observation but removes even the symmetric zero-score clause. The extra clause is unnecessary now that H provides strict improvement at every world.

## 3. Abstract construction lemma for LDG

The preceding proof separates into an abstract representation lemma and the application-specific repair theorem.

Let a measurable record domain have a distinguished coherent class C and scalar world scores. Assume:

- guidance is record-based, closed under composition of disjoint guidance changes, and every non-null guided change strictly improves its world's score;
- guidance alone cannot weakly dominate any coherent model nontrivially;
- every incoherent X has a coherent N strictly improving its score at every world, with a record that cannot be applied to any coherent model.

Then guidance plus safe strict score improvement gives the conclusions of the proposition. The definition of safety makes it upward closed under adjoining disjoint records, which proves (Add).

This lemma is a construction theorem, not a proposed new axiom of reasonable rankings. Its repair hypothesis must be proved separately. It complements the compact-certificate and score-admissibility routes in LDG; it does not require either route's topological hypotheses.

## 4. Infinite-world theorem on separable bounded-gamble spaces

### Setting

Let Omega be any nonempty set. Let E be a separable closed real linear subspace of bounded functions on Omega, with the sup norm, containing the constant gamble 1. It need not be finite-dimensional. Let S be its state space: all positive continuous linear functionals q on E with q(1)=1. S is weak-* compact and metrizable. Evaluations at worlds belong to S, and

    inf_{q in S} q(h) = inf_{omega in Omega} h(omega).

For a nonempty weak-* compact convex Q subset S define

    P_Q(h)=min_{q in Q}q(h),   D_Q={h:P_Q(h)>0}.

Fix nonempty compact convex K' subset S and U=D_{K'}. Models are measurable subsets X of U modulo mu-null sets. Coherent models are D_Q modulo null sets, with K' subset Q subset S compact convex.

Choose a finite full-support Borel measure mu on E such that:

- integral ||h||_infinity dmu < infinity;
- mu({h:P_Q(h)=0})=0 for every nonempty compact Q subset S.

These measure assumptions are simultaneously satisfiable. Choose a world omega_0, let E_0={g:g(omega_0)=0}, let nu be a full-support probability on E_0 with finite first norm moment, and independently choose a real variable t with an everywhere-positive continuous density and finite first moment. The law of h=g+t1 has the required properties. Indeed P_Q(g+t1)=P_Q(g)+t. Separability supplies nu, for example by summably weighted atoms on a dense sequence. This measure is a tool on gamble space, not a prior over worlds.

### Theorem (new audit result)

For every incoherent X subset U there is a coherent N such that

    inf_omega [integral_N h(omega) dmu - integral_X h(omega) dmu] > 0,
    hull(X\\N)=hull(X),
    N subset hull(X), and mu(N\\X)>0.

Consequently the simple safe-improvement ranking of section 2 makes precisely the coherent evaluable models undominated and strictly dominates every incoherent model, on this arbitrary-world domain.

### Proof, step A: the hull

Set Q_X={q in S:q(h)>=0 for mu-a.e. h in X}. It contains K'. It is weak-* closed: q -> integral_X max(-q(h),0) dmu is continuous by dominated convergence (S is metrizable), and Q_X is its zero set.

Choose a countable dense subset of Q_X. Its inequalities hold simultaneously a.e. on X, and continuity in q gives all Q_X inequalities there. Thus P_{Q_X}>=0 a.e. on X. The boundary-null assumption gives X subset G=D_{Q_X} a.e.

### Proof, step B: relaxed moments replace Lyapunov

Consider f in L-infinity(mu) with 0<=f<=1_G. This is weak-* compact and convex. The map

    T(f)=integral f(h) h dmu(h) in E

is weak-*-to-norm continuous on this set. To see this, approximate the identity h by E-valued simple functions in L1(mu;E). Their integral operators are finite-rank and weak-*-to-norm continuous; the operator errors are bounded uniformly on ||f||_infinity<=1 by the L1 approximation errors. Bochner integrability holds because E is separable and integral ||h|| is finite.

Hence the relaxed moment range Z_G is norm compact and convex. This does not assert that the range of ordinary indicator choices is convex.

Let x=T(1_X). Minimax on S times Z_G gives

    v=max_{z in Z_G} min_{q in S} q(z-x)
     =min_{q in S} max_{z in Z_G} q(z-x).

The pairing is jointly continuous on this product, since Z_G is norm compact and states have norm 1. Both extrema are attained.

For each q, the maximising relaxed choice is uniquely f=1_{G intersect {q(h)>0}} a.e., because mu({q(h)=0})=0. This is an ordinary coherent model D_{conv(Q_X union {q})}.

If v=0, an optimal q makes X a maximiser, so uniqueness makes X coherent, a contradiction. Also v>=0 since x belongs to Z_G. Therefore v>0.

An optimal pair (q*,z*) is a saddle point. Its optimal relaxed choice is therefore the unique indicator 1_{N_0}, with N_0=G intersect {q*(h)>0}. Consequently

    m(N_0)-m(X) >= v1 pointwise on Omega.

Relaxation is only a proof device: the actual defender is not randomised.

### Proof, step C: shrink while preserving the uniform margin

Put Q_tau=(1-tau)Q_X+tau S and N_tau=N_0 intersect D_{Q_tau}. These sets are coherent. Since

    P_{Q_tau}(h)=(1-tau)P_{Q_X}(h)+tau inf_omega h(omega),

N_tau increases to N_0 as tau decreases to zero. Dominated convergence gives

    ||m(N_tau)-m(N_0)|| <= integral_{N_0\\N_tau} ||h|| dmu -> 0.

Choose tau small enough to preserve, for example, half the uniform score margin. The gained set is non-null: otherwise applying any k in K' to the improvement contradicts k(h)>0 on U. Shrinking can also preserve its positive measure.

### Proof, step D: the contraction lemma is dimension-independent

If q(h)>=-c P_{Q_X}(h) a.e. on X, then for every q' in Q_X, (q+cq')/(1+c) belongs to Q_X. Iteration converges weak-* to q, so q belongs to Q_X.

If q is nonnegative a.e. on X\\N_tau, the same bound holds on X intersect N_tau because q(h)>=inf_omega h(omega)>-((1-tau)/tau)P_{Q_X}(h). It also holds on the removed part. Thus Q_{X\\N_tau}=Q_X, proving hull invariance and the theorem's geometric conclusions.

### Proof, step E: protecting coherent models at arbitrary worlds

The finite-world pure-guidance argument needs an a.e. qualification here. Separability of E supplies a countable set Omega_0 subset Omega that computes suprema and infima of every h in E (choose approximate norming evaluations for a countable dense subset of E, with both signs).

If a record is guidance at every world, intersecting the null-set complements for Omega_0 shows that its added gambles are nonnegative everywhere and its removed gambles nonpositive everywhere, a.e. The removed part cannot lie in U. The added part is uniformly positive a.e.: the remaining nonnegative gambles with inf h=0 form the null set {P_S=0}. Every coherent model already accepts uniformly positive gambles. Thus no coherent model can be nontrivially weakly dominated by pure guidance. Section 2's ranking proof now applies unchanged.

## 5. A genuine infinite-world contamination cover

Take Omega compact metric and E=C(Omega). States are the regular Borel probability measures. Let p be a full-support probability and 0<epsilon<=1. Put

    K=(1-epsilon){p}+epsilon S,   K'={p},   U={h:p(h)>0}.

The theorem makes D_K undominated and dominates every incoherent model on U. It also supplies the natural norm-topological analogue of (LF).

Indeed P_K(h)=(1-epsilon)p(h)+epsilon min h. If h is a nonzero boundary gamble, P_K(h)=0. Since min h<=p(h), p(h)>=0. If p(h)=0, then min h=0, hence h>=0; full support and continuity force h=0, a contradiction. Therefore p(h)>0 at every nonzero boundary gamble. The open domain U itself is a neighbourhood of that boundary, so all measurable local modifications inside it are evaluable.

This gives exact infinite-world coverage for contamination targets in this specified continuous-gamble setting, contingent on independent verification of the audit theorem. It does not claim coverage for every compact credal set under every possible infinite-dimensional local-freedom condition.

## 6. Scope limits

- Arbitrary Omega is allowed above, but the bounded-gamble space E is separable. All of ell-infinity(Omega) is nonseparable even for countably infinite Omega. The theorem does not cover that full space.
- In the general E setting, states are positive functionals, naturally compatible with finitely additive representations. Countable additivity cannot be silently required. In C(Omega) for compact metric Omega, the usual state representation uses countably additive regular probabilities.
- Coherence here means the open/strict desirability sets D_Q used in the finite paper. Arbitrary coherent desirable sets with non-Archimedean boundary choices are not automatically included.
- Infinite-dimensional “full dimensionality” should not be imported as a substitute for local freedom. State and prove the actual local-freedom property, as in the contamination example.
- The measure, null-set quotient and regularity of gambles remain substantive choices. On a nonseparable normed gamble space there is no finite full-support Borel measure in the norm topology: uncountably many disjoint open balls would each need positive mass. A full bounded-gamble theorem needs another treatment.

## 7. Recommended revision and next round

1. Independently referee the simple strict safe-improvement ranking and the infinite-world theorem, including the countable norming argument and norm-compact relaxed range.
2. Replace the universal note's main ranking by the simpler rule; retain the designated-world and lexicographic variants only if independently useful.
3. Present the proof as relative minimax plus hull-preserving shrink. The contraction lemma should be prominent.
4. Add the abstract safe-improvement construction lemma to LDG as a route alongside compact certificates and admissibility. Do not turn its sufficient conditions into necessary axioms.
5. Correct the claim that lower-dimensional targets are not admissible under the universal ranking: all coherent evaluable models already are. What fails on a one-sided domain is (LF), hence coverage as defined. A two-sided extension must confront inconsistent rivals with Q_X empty, not merely repeat the nonempty-hull proof.
6. Reframe the covering paper around the universal finite result, then distinguish the independently structured score constructions. Keep the general LDG paper separate from the gamble application unless editorial constraints favour merging.
7. Do not make a new “no reference to coherence” requirement the next mathematical objective. That is a separate philosophical programme, and syntactic non-reference is not an invariant property of a ranking.
