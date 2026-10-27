# Round 66: assessment and remaining mathematical work

26 October 2026. Research brief, not a definitive manuscript. The new proof below needs independent refereeing.

## 1. Priorities met and missed

Met: the simpler ranking, its (Add) property, finite-chain consistency, the infinite-world extension on separable order-unit gamble spaces, and the finite full-domain theorem have been independently checked. The relative minimax and hull-preserving shrink are now the central mechanisms.

Still missing:

- The full-domain infinite-world theorem is only a sketch in TS66. It should be the main completion task, not optional.
- LDG v3.3 still uses (I)+(B_infinity) in its main infinite theorem. The compact closed-subset weakening from `Infinite-world-compact-certificates-2026-10-26.md`, including the strict-separation example, has not been incorporated or reported as independently refereed. Calling route A “compact certificates” does not implement that weakening.
- The final statement must make the measure-relative identification of models explicit. It is not literal coherence of every raw measurable set.

Two corrections to summary wording:

- Weak dominance coincides with strict dominance only for distinct models in the quotient. Every model weakly dominates itself.
- The infinite theorem gives every incoherent model a defender with a uniform positive score margin. It is merely false that *every* strict dominance comparison has a uniform margin. Both referees explicitly retain the stronger existence result.

## 2. Complete the full-domain infinite theorem now

Use the already-refereed setting: E is a separable sup-norm-closed real linear space of bounded functions on arbitrary Omega, contains 1 (or normalise an order unit), and S is its compact state space. The finite measure mu has finite first norm moment and mu({P_Q=0})=0 for nonempty compact Q. Full support is included when identifying distinct coherent sets and stating coverage. Models are all measurable subsets of E modulo mu. Coherent models are D_Q for nonempty compact convex Q subset S, modulo mu.

The simple ranking is unchanged. Safety means that no coherent model contains the removed set and misses the added set, a.e. In particular, removing a set B for which Q_B is empty is safe even if nothing is added.

### Proposition: uniformly losing part

If Q_X is empty, there exist q* in S and eta>0 such that

    L = X intersect {h:q*(h)<0}
    m(L)(omega) <= -eta for every omega.

Proof. Let F_X={f in L-infinity(mu):0<=f<=1_X}. The already-proved compact integral-operator lemma makes

    Z = {-integral f(h)h dmu : f in F_X}

norm compact and convex in E. Minimax gives

    eta = max_{z in Z} min_{q in S}q(z)
        = min_{q in S} integral_X (-q(h))_+ dmu.

The right-hand function is continuous on compact S. It is strictly positive at every q, since Q_X is empty; hence eta>0. At a saddle point q*, the relaxed choice is uniquely f=1_L a.e. because {q*(h)=0} is null. Thus -m(L)>=eta 1, as claimed.

### Theorem: full-domain coverage on E

Every incoherent measurable X subset E has a coherent N with a safe record and uniform positive score improvement. The simple ranking consequently has exactly the coherent models as its undominated models and covers every coherent target on E under literal (LF).

Proof. If Q_X is nonempty, the existing one-sided theorem applies on G=hull(X), which contains X a.e. Equivalently, apply it on D_{q_0} for q_0 in Q_X and use its conclusion that the resulting defender lies inside G. Its proof gives the safe change and a uniform margin.

If Q_X is empty, take L,q*,eta from the proposition and put X_+=X intersect {q*(h)>0}. Since {q*(h)=0} is null,

    m(X_+)-m(X)=-m(L)>=eta 1.

Now q* belongs to Q_{X_+}. If X_+ is coherent, take N=X_+. Otherwise use the existing theorem inside hull(X_+) to obtain coherent N subset hull(X_+) with a uniform score improvement over X_+.

In both cases N subset {q*(h)>0}, so L subset X\\N a.e. Since m(L)<=-eta 1, no state can be nonnegative a.e. on L: applying such a state to its Bochner integral would give both a nonnegative number and a number at most -eta. Thus Q_L is empty, and Q_{X\\N} is empty. The record from X to N is safe. The total score improvement is at least eta at every world.

Protection on the full domain requires only the existing countable-norming argument. A record guided at every world adds nonnegative gambles and removes nonpositive gambles a.e. The null-boundary assumptions make these uniformly positive and uniformly negative a.e., respectively. Every coherent model contains the former and excludes the latter. Thus guidance cannot weakly dominate a coherent model nontrivially. The other ranking arguments are unchanged.

On U=E, local freedom is automatic: take the open neighbourhood to be E itself. No restriction K_perp={0}, full dimensionality or strictly positive member of K is needed. All coherent targets in the adopted quotient are covered by this one ranking.

This proof extends TS66's sketch using exactly the referee-confirmed relaxed moment machinery; it is not yet an independently refereed theorem.

## 3. One minimax lemma, two natural cases

Do not retain separate long finite and infinite proofs. The common lemma is:

    Optimising relaxed acceptance choices against all states has an attained
    maximin solution; the null-indifference condition makes the optimal
    relaxed choice an ordinary acceptance set.

It gives a coherent improvement when optimising within a coherent hull, and a uniformly losing subset when applied with a minus sign to a rival with no supporting state. The contraction lemma then handles the nonempty-hull case. There are two natural cases because a set of commitments may be consistent or inconsistent; forcing these into one opaque formula would not improve the exposition.

Finite-dimensional Lyapunov can be a historical remark or alternative proof. It is not needed in the main proof once the relaxed-choice argument is available.

The common repair mechanism is simple:

- either discard commitments that already form a uniform loss;
- or replace part of a consistent but incoherent set of commitments by consequences of that part, after optimising within its coherent hull.

The permitted change cannot be applied to a coherent model, and its score strictly improves at every world. The ranking therefore protects coherence while improving every incoherent model.

## 4. What should become general in LDG

Separate results about a given ranking from results constructing a ranking. Do not force them into one giant theorem with a list of alternative hypotheses.

For a given ranking, the topological result can be stated directly, without the term “certificate”:

    There are a compact space Theta, models c_theta in C_L, and closed sets
    F_omega(x) contained in {theta:c_theta <=_omega x}, such that every finite
    collection F_omega(x), for fixed x, has nonempty intersection.

Then some c_theta weakly dominates x at every world. The closed sets need not contain every true comparison. The finite-simplex/KKM theorem is one sufficient way to obtain the finite intersection property. The earlier (I) is another sufficient implementation, not a binding requirement.

Keep the separate score-compactness lemma where it gives additional information, and the construction lemma where it builds a new ranking. Main text should state their mathematical content in words before introducing notation. The exact-hypothesis equivalences, auxiliary closure labels and full dependency tables can be technical appendices where genuinely needed.

The condition “every model has an undominated coherent weak dominator” is a useful conclusion to connect the arguments. It is not an explanation by itself. Do not make a shorter paper by replacing all the constructive results with that conclusion as a hypothesis.

## 5. Scope to settle before definitive writing

1. World sets are arbitrary, but the present theorem assumes a separable bounded-gamble space with an order unit. It is not a theorem for all bounded gambles on an arbitrary infinite world set.
2. Models are identified modulo a specified measure. Full support does not mean every nonempty measurable defect has positive measure. An actually incoherent set can coincide a.e. with a coherent one. State this convention prominently.
3. The full-domain infinite theorem, if confirmed, removes the one-sided local-freedom restrictions. The one-sided characterisation remains a domain corollary, not the headline general result.
4. Nonseparable spaces, spaces without an order unit and classification of arbitrary restricted domains are further extensions. They need not hold up definitive versions of the established theorem, provided the stated objective and title match its scope.
5. Keep the accuracy interpretation separate. No new axiom should be added merely to exclude the universal construction.

## 6. Recommended next round

Do mathematical completion, not definitive prose rewriting:

1. Referee the full-domain infinite theorem above; check empty X_+, boundary states, Bochner integration of states, and protection under uncountably many worlds.
2. Referee and implement the weakened compactness theorem and strict-separation example. Record explicitly what parts of LDG's appendix do not follow from the weakening without extra hypotheses.
3. Assemble one theorem-and-proof outline for the application: ranking lemma; relaxed minimax; contraction; universal full-domain theorem; restricted-domain and local-freedom corollaries. Check whether the finite proofs become special cases.
4. Produce a short scope statement covering measure-relative coherence, the gamble space, order unit and the meanings of strict and uniform improvement.

After those checks, the mathematical package is sufficiently settled to begin the two definitive versions. Updating working notes is fine now; wholesale reframing of the old covering manuscript should wait.
