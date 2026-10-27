# Weakening compact indexing in LDG v3.1

26 October 2026. New audit results, with proofs below; not independently refereed.

## 1. What the existing proof actually uses

In v3.1's infinite-world theorem, finite-simplex certificates give finite-world weak dominators. Condition (I) then makes the full comparison sets

    {theta : c_theta <=_omega x}

closed in one compact index space. Their finite intersection property gives a global weak dominator.

The full comparison sets are unnecessary. Closed subsets certifying enough comparisons suffice. This is the same weakening applied at the compactness stage that (B) applies at the KKM stage.

## 2. Compact-certificate condition (CC)

Let Omega be any nonempty set. Assume (LA), with C_L the nonempty class of coherent undominated evaluable models. Require a nonempty compact space Theta and sets B_omega(theta) of evaluable models such that:

1. For every omega and rival x, K_omega(x) = {theta : x in B_omega(theta)} is closed.
2. For each theta, a single c in C_L satisfies c <=_omega x for every omega and every x in B_omega(theta). The realiser may vary discontinuously. No topology on models or closedness of its other comparisons is required.
3. For each rival x and each finite nonempty F subset Omega, there is theta with x in B_omega(theta) for all omega in F.

The same realiser must realise all certificates at theta, across all worlds and rivals. Clause 3 fixes the rival while varying the finite set of worlds; it does not demand a model dominating all rivals simultaneously.

## 3. Dominance theorem

Under (LA) and (CC), every evaluable model is weakly dominated by a member of C_L. With (C), every model outside C_L is dominated by a member of C_L, and U_L=C_L.

Proof. Fix x. Clause 3 says the closed sets K_omega(x) have the finite intersection property. Compactness gives theta_x in their intersection over all worlds. A simultaneous realiser from clause 2 weakly dominates x at every world. If x is outside C_L, (C) excludes an all-world tie with this realiser, so the dominance is genuine. The remaining conclusions are those of v3.1's abstract (W)+(C) argument. No transitivity, completeness, reflexivity or numerical scores are used by this proof.

## 4. Retaining a constructive KKM route

Clause 3 can be supplied by local finite-simplex certificates rather than assumed after finding weak dominators.

For a cofinal family of finite nonempty F, suppose A_{F,omega}(p) have closed rival sections on Delta_F and support-wise coverage, as in v3.1. Replace their realisation clause by:

    For every F and p there is theta such that
    A_{F,omega}(p) subset B_omega(theta) for all omega in F.

Then KKM, applied to a fixed rival x on Delta_F, supplies p where x belongs to all A_{F,omega}(p). The displayed inclusion supplies a common global certificate index. Hence (CC3).

No continuous map from Delta_F to Theta is needed. Global certificates, not the full verdicts of selected models, must remain closed.

The old (I)+(B_infinity) implies this package: take B_omega(theta) to be the full comparison set of c_theta, and A_{F,omega} to be the old local certificates. Thus this is a weakening, not an extra assumption appended to the old theorem.

For finite Omega, ordinary (B) implies (CC) by taking Theta=Delta and the same certificates. KKM gives clause 3. Thus the new theorem extends the finite certificate theorem without reinstating a stronger compact-selection requirement.

## 5. Strict separation from the old package

The following explicit example satisfies (CC), including the local KKM formulation, but no choice of compact indexing can satisfy (I)+(B_infinity).

Let Omega={1,2} x N, so there are infinitely many worlds of two types. Models are distinct symbols c_t and x_t for t in [0,1]. Declare precisely the c_t coherent.

Begin with scores, lower better:

    loss_1(c_t)=t, loss_2(c_t)=1-t,
    loss_1(x_t)=loss_2(x_t)=2.

Duplicate each type's relation at every world of that type. Keep all score comparisons except these:

- For q>0, remove c_q <=_1 x_q.
- Remove c_0 <=_2 x_0.

The removed comparisons had strict score differences, not ties. All score ties retain both directions. This subrelation is reflexive, satisfies (TC), and has no finite accepted cycle containing a strict comparison: along an accepted cycle the original scores would all have to be equal, and all such ties remain symmetric.

Each c_t is undominated. The only model weakly dominating c_t is c_t itself. Every x_q is dominated by c_s for any s != q. No x_q is tied at all worlds with a coherent model. Thus (LA), (C) and (W) hold, with C_L={c_t}.

Take Theta=[0,1]. Define certificates by their sections:

- For rival c_s, type 1 certifies it at theta in [0,s]; type 2 at theta in [s,1].
- For rival x_q with q>0, type 1 certifies it only at theta=0; type 2 at every theta.
- For rival x_0, type 1 certifies it at every theta; type 2 only at theta=1.

All sections are closed. At theta the model c_theta simultaneously realises every certificate. Each rival is jointly certified at both types somewhere: theta=s for c_s, theta=0 for x_q with q>0, theta=1 for x_0. Hence (CC).

For the local-simplex version, set theta(p) equal to the total p-mass on type-2 worlds and pull back the above certificates. Sections are closed. Support-wise coverage holds: the ordinary interval argument handles c_s; x_q, q>0, is certified at every type-2 world, and when none is charged theta=0 certifies it at type 1; the symmetric argument handles x_0. All local certificates embed into the global ones at theta(p).

Now suppose (I)+(B_infinity) held with any compact parameter space Xi and map f:Xi -> C_L. The old theorem gives each c_t a weak dominator in the image of f. Since that dominator must equal c_t, f is onto C_L. Write E_t={xi:f(xi)=c_t}; these are nonempty disjoint sets covering Xi.

For q>0, the full comparison section against x_q at a type-1 world is Xi\\E_q. For q=0, its type-2 section is Xi\\E_0. Condition (I) makes each complement closed, so every E_t is open. The infinitely many nonempty disjoint E_t therefore form an open cover with no finite subcover, contradicting compactness.

Thus the weakening is strict, even allowing the old package to choose any compact indexing at all. The example has only two distinct world types; its purpose is to separate the abstract hypotheses, not to supply an infinite-dimensional gamble cover. It makes no claim about gamble-specific (G) or (IB).

## 6. A further rival-specific version

For each rival x one may instead have a compact Theta_x, closed K_{omega,x} with the finite intersection property, and coherent undominated realisers guaranteeing the certified comparisons against x. The same proof works. This is more flexible but risks merely repackaging an already-known dominator (choose a singleton index). It should be presented as a proof device, not automatically an independent explanation of dominance.

The shared certificate system in (CC), especially when constructed from the local KKM conditions, retains more of the original framework's reusable structure.

## 7. What this changes, and what remains

- (I) should be presented as one sufficient source of compact certificates, not as the general infinite-world requirement.
- Replace the infinite theorem's headline hypotheses by (CC), with the old theorem as a corollary. Retain the local KKM version as a practical sufficient condition.
- The original claim that no result drops (I) must be updated if the new theorem passes independent checking.
- Additional score/Bayes conclusions in the appendix still need their own hypotheses. They do not automatically follow from (CC).
- This theorem removes a topological overconstraint. It does not prove infinite-world coverage for deletion, veto–Brier or veto–box, and does not restore infinite-dimensional Lyapunov convexity.
- For deletion, investigate whether a closed family of guaranteed comparisons survives deletion and has finite-world coverage, even when the full surviving relation has nonclosed sections. Do not simply use all undeleted comparisons as the certificates.
- Compactness cannot be discarded without replacement: the finite-world feasibility clauses alone do not supply one model for all worlds.

Recommended next task: independently verify the theorem and separation example, then seek explicit infinite-world compact certificates for one existing positive construction, rather than require its entire comparison relation to satisfy (I).
