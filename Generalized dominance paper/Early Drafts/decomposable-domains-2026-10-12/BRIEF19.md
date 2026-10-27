# Brief, round 27 (16 Oct 2026, 21:15): demanding milestones in the joint two-sided method

The method of BRIEF18 continues. Audit's assessment of round 26 is in AUDIT_X123.md: read it FIRST.

## Audit's corrections (adopted)
- **X1 is a plan-based compactness criterion, not an existence argument.** Fix a selection and a reservation plan V. A cover with that plan exists iff every finite fragment of the WHOLE theory is satisfiable WITH THAT SAME selection and plan.
  - Enough: one selection and one plan that work for every finite fragment.
  - Not enough: each fragment works after choosing its own selection or shrinking its own neighbourhoods.
- **X2 does not settle the interior.** Any two distinct interior members of the posterior family differ on problems arbitrarily close to a coordinate plane (AUDIT_X123.md, interior-locality lemma). So nearby interior selections are connected by NONLOCAL records, which lie outside X2.7's scope.
  - Two different limits must not be conflated: weightings approaching ∂Δ, and problems approaching a coordinate plane.
- **X2.9 forbids keeping X2's invariant local rules.** If X2.9 holds, some local verdicts must change; patching only the nonlocal comparisons cannot work.
  - X2's local order is lexicographic over linear functionals. That is a consistency witness, not the new mechanism we are looking for.
- **Finite contradiction certificates are possible.** For a fixed selection and plan, an inconsistency has a finite certificate, which may involve continuum models and plan clauses.
  - Do not use plain finite satisfiability on grids as the success measure.

## Milestones for this round
1. **Genuine interior closed choice.** Use the posterior family on a small closed neighbourhood N of u, entirely inside Δ°. Require competitiveness against ALL measurable competitors, nonlocal differences included, and closed sections relative to N.
2. **Joint edges.** Each world appears in two edges; both appearances must belong to the same order, and compositions across edges must preserve the target. Prove an explicit compatibility lemma.
3. **An actual reservation plan.** Take one vertex and a specified family of competitors. Prove that the same reservations survive arbitrarily fine fragments.
4. **Better finite tests.** Include selected-model comparisons at different interior indices, progressively thinner regions near coordinate planes, and clauses from a fixed proposed plan.

## Read
- BRIEF18.md and AUDIT_nonlinear_programme.md.
- X1_notes.md, X2_notes.md, X3_notes.md.
- writeup §2 and §8.6.
- L3_notes.md (L3.1, L3.4).
- Full Coverage v3 (two-world two-sided additive coverage: the edge systems).
- M3_notes.md.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it.
