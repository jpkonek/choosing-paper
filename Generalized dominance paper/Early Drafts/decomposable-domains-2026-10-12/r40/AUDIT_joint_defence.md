# Candidate: joint defence and weakest-pair deletion

21 October 2026. A specific candidate rule, not a covering theorem. The proofs of (G), (IB), and (TC) below are author-checked. Neither survival of all defence obligations nor closed sections is proved. No numerical implementation of this candidate has been run.

## Purpose

Replace additive-first and successive local repair by two operations:

1. Choose both directions of each disagreement together, preferring strict defences and retaining redundant defenders.
2. In every forbidden three-model configuration, remove its weakest removable comparison-pair, everywhere that disagreement occurs.

The second operation is simultaneous and performed once. Symmetric deletion cannot create a new (TC) violation. This is not an extension lemma, a transfinite construction, or a request to solve for arbitrary relations satisfying all the axioms. The initial relation and the deletion criterion are specified below without (S) or (TC) as optimisation constraints.

Use the existing coherent family K_p = p + 3 epsilon min_j p_j (Delta-u), C_p=D_{K_p}. The rule is a candidate for this family. Its applicability to other families would need the corresponding defence-pool facts.

## 1. Data obtained from one disagreement

For d=rec(X,Y), let bar(d)=rec(Y,X). At world i, let P_i be the errors added on going from X to Y and Q_i the errors removed. Put

    b_i(d) = nu(P_i)-nu(Q_i),
    Phi_i(d) = 4 nu(P_i)-nu(Q_i),
    c_i(d) = nu(Q_i)/(nu(P_i)+nu(Q_i)).

Only use c_i for a nontrivial record. Let A(d) be the set of indices whose selected model agrees with the old advice of d on its changed problems. Write H for A(d) nonempty.

The eligible directions at i are:

- Every guidance direction, compulsorily, with its strict guidance reverse forbidden.
- A non-guidance d only if A(d) is nonempty and Phi_i(d)>=0.

Thus non-guidance comparisons with no coherent selected-source explanation are initially absent. This is a design choice, not a necessary condition on rankings. It is intended to avoid introducing unsupported return comparisons.

For each nonempty face I, if A(d) meets Delta_I, at least one i in I must accept d. Apply the same requirement separately to bar(d).

## 2. Joint initial choice: at most 64 alternatives

For the unordered pair {d,bar(d)}, consider the four states at each world: forward only, reverse only, both, neither. There are 4^3 possibilities.

Keep those obeying guidance, eligibility and all the face requirements in §1. The feasible list is nonempty: accepting every eligible direction works, by the established interior and edge pool theorems and vertex guidance.

Select an alternative by these objectives, in order:

1. Minimise the number of worlds accepting both directions.
2. Maximise the number of accepted non-guidance directions.
3. Minimise the sum of c_i(d) over the accepted non-guidance directions (including reverse directions with their own c_i).
4. Break any remaining tie by a fixed deterministic coding of records and states.

The last convention can be made explicit without referring to models' common advice: order rational boxes in gamble space; use the first nonzero integral of the world-1 advice-rank difference over those boxes to canonically orient {d,bar(d)}; order its 64 states lexicographically. A nontrivial signed rank-difference function is detected by this countable determining family. This tie-break is provisional: no closed-section claim is made for it.

Call the resulting record relations R_i^0.

### Concrete consequence for the troublesome rivals

If A(d) is nonempty, A(bar(d)) is empty, and every b_i(d)<0, all eligible forward directions are accepted and their reverses are refused. There is no reason in the optimisation to leave an eligible forward direction out. At least two worlds are eligible by the kappa=4 theorem.

So these rivals receive at least two **strict** defences at the outset, rather than one arbitrarily chosen defence or several ties. This applies to the explicit three-cone rivals in the preceding audit note. Their reverse records have no coherent completion.

The 4:1 field is just a specified initial pool. It is not preserved as a global pricing rule, and its favourable verdicts outside the selected joint allocation have no standing. A later enlargement of the pool is possible, but is not part of this candidate.

## 3. Assign priorities to removable comparison-pairs

A pair that contains a compulsory guidance comparison cannot be removed.

For every other pair present at world i define its priority as the lexicographic pair (s,m):

- s=1 if it contains an accepted direction d for which A(d) is nonempty, A(bar(d)) is empty, and b_j(d)<0 at all three worlds; otherwise s=0.
- m is the minimum of Phi_i(e)/(nu(P_i(e))+nu(Q_i(e))) over the directions e of this pair accepted at i.

Thus necessary departures from all three ordinary additive balances receive priority over ordinary comparisons. Within a priority class, comparisons with less eligibility margin are sacrificed first. The use of a minimum matters when both directions are accepted.

This is an order of **disagreement records**, not a fixed priority ordering of individual gamble problems. The fixed-problem-priority exclusion therefore does not apply merely by inspection; other exclusions still need checking.

## 4. One simultaneous deletion

Inspect every actual triple of measurable models and every world. Whenever R_i^0 violates (TC), select the removable unordered comparison-pair(s) of lowest priority in that triple. Mark their disagreement records and reverses for deletion. Equal lowest priorities are all marked.

Delete every marked record and its reverse from R_i^0, in every context where they occur. Call the result R_i.

Equivalently, a record-pair is deleted if there exists any realisation of it in a violating triple in which it has minimal removable priority. This is an exact mathematical rule on the continuum of models. It is not asserted to be a finite or cheap computational procedure.

There is always a removable pair in a violating triple: if every participating pair were a guidance pair, all three accepted links would be pointwise guidance comparisons, which cannot form such a violation.

## 5. What follows immediately

**(G).** Guidance pairs are retained, and their strictly forbidden reverses are never introduced.

**(IB).** Initial decisions use only records. Deletion is also a decision about a record, applied in all common contexts. The existence of a witnessing triple is quantified over all realisations, not tested only at a convenient chosen source model.

**(TC).** Every initial violating triple loses at least one of its participating pairs. Symmetric deletion creates no new violation: surviving strict comparisons were already strict, and all surviving weak links were already present. Hence the final relation satisfies (TC).

**Reflexivity.** The identity record remains accepted; it cannot be a member whose deletion is needed to break a strict three-cycle.

The rule does not impose full transitivity or exclude longer strict cycles.

## 6. What remains genuinely open

The initial relation satisfies all face defence requirements. It is **not proved** that the final one does. In particular, different triangles could mark both initial strict defenders of the same rival. The priority rule protects them against lower-priority returns, but not against triangles involving several equally protected defences.

Neither the initial tie-break nor the deletion operation has been proved to preserve the sections required by (S). Check only the actual sets {p:C_p R_i X}, not global closedness of R_i on all record pairs. Removing an unanchored record leaves these sections unchanged, but marking an anchored defence does not.

(LA), selected-model undominatedness, and direct (C) are also unproved. The rule's non-additivity in the programme's strong sense (absence of an endorsing positive field on the relevant comparisons) is not established simply by its nonlinear definition.

## 7. What to ask the collaborator to do

Implement this exact candidate, before substituting another additive base or imposing a closed graph. First use the already certified PP5/PP7 configurations, including all contexts identified by record equality.

The first decisive test is whether a record loses every required defender. If it does, report the full collection of triangles causing the losses, not merely an unsuccessful sequential repair. If it does not, prove survival on the entire three-cone rival family and its transferred return comparisons.

Next test closed sections along selected-model paths with the rival held fixed. A varying-rival discontinuity is not by itself a failure of (S).

The point of the construction is that (TC) is enforced by an explicit deletion rule while strict defences are present from the start. The difficult theorem is that this enforcement leaves enough defences, together with the required closed sections. No claim is made that the priority formula already accomplishes that.
