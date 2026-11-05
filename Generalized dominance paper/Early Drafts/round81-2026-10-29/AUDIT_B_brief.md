You are right on both points. I had not clearly specified the proposed condition, and **the availability of consolidation gives us a reason to revisit (S)**. The earlier failures do not settle what this machinery can now achieve.

I would give the collaborator the following brief.

## Aim

Establish a substantive connection between the desirability results and LDG, pursuing two questions:

1. Can consolidation yield a useful general LDG theorem with fewer assumptions than the current desirability proof?
2. Can consolidation help establish the existing selection condition (S), perhaps after a modest change to the desirability rankings?

The second question should remain a genuine construction task, not be dismissed because the current theorem does not already answer it.

## 1. Clarify the finite-sequence proposal

**Do not introduce an unrestricted “finite-sequence axiom.”** The proposed general result is an inference theorem about comparisons that have already been established.

> **Finite-sequence theorem.** Suppose a ranking satisfies transitivity through ties. If
> \[
> x_{j+1}\preceq_\omega x_j
> \quad\text{for every }\omega,\quad j=0,\ldots,r-1,
> \]
> and \(z\) weakly dominates \(x_r\), strictly at some world, then some member of
> \[
> x_1,\ldots,x_r,z
> \]
> dominates \(x_0\).

The collaborator should verify the short proof previously supplied, including whether only substitution through **all-world ties**, rather than the stronger worldwise condition (A3), is needed.

There are then two distinct propositions:

- **An unrestricted existence condition:** every incoherent model has some sequence of comparisons satisfying this theorem.
- **A desirability-specific geometric result:** every incoherent model admits at most two consolidations followed by a non-null change guided at every world.

The latter specifies the transformations **without reference to the ranking**. Their existence is proved using the geometry and measure assumptions. Axioms (A4) and (A1) subsequently supply the comparisons.

The unrestricted condition is **not stronger** than the prescribed-transformation condition. It allows more sequences and is therefore less restrictive. Under the tie condition, it is equivalent to the dominance conclusion, so it should not be presented as an independently motivated assumption.

**Deliverable:** a general finite-sequence theorem, a separate geometric lemma, and their application. No new dominance-equivalent axiom.

## 2. Check whether (A2) can be removed

Extract the following construction from the current proof:

- Failure to accept uniformly positive gambles or to reject uniformly negative ones permits a guided improvement.
- Failure of upward closure permits a consolidation producing the preceding failure.
- Otherwise, incoherence permits a consolidation producing a failure of upward closure.

Check carefully that these constructions use no assumption of undominatedness except in the existing contradiction argument. If they do not, they establish the geometric lemma directly.

Then apply the finite-sequence theorem using (A1), (A3), and (A4).

**Success:** the desirability dominance theorem loses (A2), and its ranking-theoretic argument becomes a direct application of LDG. This is useful progress even if (S) remains unresolved.

## 3. Reopen (S), with a precise construction target

The task is to construct, for each relevant ranking, selected models \(c_p\in\mathcal C_L\) and closed sets \(A_\omega(X)\) such that
\[
p\in A_\omega(X)\Longrightarrow c_p\preceq_\omega X,
\qquad
p\in\bigcup_{\omega\in\operatorname{supp}p}A_\omega(X).
\]

Use the actual, weaker formulation of (S): **the closed sets may be subsets of the acceptance sections**. Do not unnecessarily require every acceptance section to be closed.

Start with finitely many worlds. The arbitrary-world extension should follow only after the finite construction identifies the mechanism.

There is an important preliminary constraint:

> If every almost coherent model is undominated, and distinct models never tie at all worlds, any selection satisfying (S) must contain every almost coherent model in its image.

Indeed, (S) supplies each such model with a selected weak dominator. Undominatedness makes them tied, and absence of distinct all-world ties makes them identical.

The current ranking has precisely those two properties. Consequently, **a small selected family cannot establish (S) for that ranking**. This is not an impossibility theorem, but it tells us what a proposed construction must confront.

## 4. Test three specific possibilities, in this order

**First: use consolidation to construct the selection.**  
Investigate whether a prior \(p\) can guide consolidation toward an almost coherent model \(c_p\), while providing the support-wise defence inequality and closed witnessing sets required by (S).

Merely obtaining a coherent endpoint is insufficient: the proof must explain why that endpoint compares appropriately with the original rival. Weak comparisons do not generally compose under the current ordering assumptions.

**Second: allow coherent all-world ties.**  
The current construction’s prohibition on distinct ties is a design choice. Could almost coherent models be grouped into all-world tie classes with a manageable selection of representatives, while keeping incoherent models out of those classes?

Any proposal must verify consolidation acceptance, guidance, the necessary ordering properties, and closure under ties. Declaring the tie classes is not enough.

**Third: weaken universal coherent admissibility within each ranking.**  
LDG requires each coherent model to be admissible under *some* ranking, not every ranking. Consider rankings tailored to a target, protecting an appropriate family—potentially the rescaled family—while allowing other coherent models to be dominated.

Consolidation may now provide the missing dominance machinery. The selected family must nevertheless be proved admissible and shown to satisfy (S); it cannot simply be stipulated.

## 5. Required report

Ask for a short report separating:

- what is proved about the finite-sequence theorem and removal of (A2);
- whether (S) holds for the current ranking;
- any modified ranking for which (S) is actually verified;
- the exact additional assumptions needed;
- whether the consistency construction still works.

**My recommendation is to pursue both strands now.** The finite-sequence work is a tightly specified simplification. The selection work is the ambitious question, newly informed by consolidation. We should neither force the application through (S) at any cost nor conclude prematurely that the existing LDG machinery cannot be used.