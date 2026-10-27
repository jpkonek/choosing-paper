# Brief, round 42 (18 Oct 2026, 23:15): five-of-seven committees

Read FIRST: AUDIT_MM.md and AUDIT_MM_summary.md (audit's review of round 41). Adopt all of its scope corrections.

## Scope corrections (round 41)
1. **Rank-two worlds are NOT excluded.** MM1 Prop 5.1 excludes only boundary relation spaces of dimension ≤ 1.
2. **MM1 Prop 2.1 concerns REAL-ANALYTIC judges, not smooth ones.** It also excludes STRICT certificates only. A weak supporting mixture may vanish identically near a corner, so an exclusion under (QS) alone needs an extra argument.
   - Smooth, flat functions can have the corner sign pattern, e.g. F(x,y) = h(x)h(y) − h(−x) − h(−y) with h(t) = e^{−1/t²} for t > 0 and 0 otherwise.
   - So nonsmoothness is NOT a requirement.
3. **MM1 Thm 4.2 assumes a specific form** σ_iv(g) = κ_iv(M_k)g_i on the three fixed minimum-coordinate cells. General piecewise-linear (finite-fan) fields remain open.
4. **MM3 proves liminf ψ(s)/s = 0,** not ψ(s)/s → 0 at every small scale.
5. **MM2's edge identities hold a.e. on a.e. plane,** with the switch type depending on whether the edge model is precise. They do not identify one field across all planes.
6. **Do not assume persistent moving triangular corners.** A continuous coherent family through T1 may round its corners immediately away from T1. Any use of moving corners must be derived from (QS), or stated as a construction choice.
7. **MM1's T1-only field is in a locally isolated class.** Do not perturb it.

## The change: n = 7 judges per world, quorum q = 5
- 3q = 15 > 14 = 2n gives (TC) by the counting proof; 2q > n gives no nontrivial ties.
- The strict-sign lifting lemma (AUDIT_LL.md, refereed in MM3) holds for any fixed finite (n, q) with these inequalities.
- Strict 4-cycles remain possible (LL3 Thm A: ν = ⌈7/2⌉ = 4), so the cycle cost is no higher than before.
- **Blocking sets now have n − q + 1 = 3 judges per world.**
  - Interior branches: C(7,3)³ = 42 875.
  - (QS) at p ⟺ for every branch F (3 judges per active world), C_p is the ONLY model with Δ_iv(p, X) ≤ 0 for all (i,v) ∈ F (NONSTRICT).
  - Sufficient certificate: some nonnegative nonzero mixture of F's judges has C_p as its unique minimiser.
- **Why it might escape.** MM1 Lemma 3.1 (pair-Helly collapse) uses TWO-generator cones: a non-ray intersection forces a common plane, which reduces to intervals. Three-generator cones need not admit this step, and MM1 Remark 3.3 declines to claim it.

## Tasks
- **NN1 (main constructive).** Build a 5-of-7 (QS) system: design the judges and the coherent family together.
  - Seek branch-supporting mixtures with several independent directions, varying with both index and branch.
  - Enforce the world-wise guidance signs.
  - Re-derive MM2's edge identities for branch size 3 and impose them.
  - Test the EXACT nonstrict competitor condition, not mere alignment or weak Bayes.
  - Allow selected credal sets to change shape.
  - A structural certificate covering all branches is needed, not just enumeration.
- **NN2 (main adversarial).** Does the two-generator collapse extend to three-generator blocking cones under the actual guidance and boundary hypotheses? Deliver an explicit escaping cone configuration or a correctly generalised obstruction. Bridge explicitly:
  - weak versus strict certification;
  - local versus global proportionality;
  - arbitrary shapes versus moving corners.
- **NN3 (referee + one 4-judge test).**
  - Referee the exact statements of MM1 (Lemma 3.1, Prop 2.1, Thm 4.2, the proportional-pairs theorem, Prop 5.1) and MM2 (branch form, boundary alignment, generic-judge failure at T1, world-separable failure, edge identities), with corrected scopes.
  - Then test the 4-of-3 class with smooth flat switch functions and credal sets that change shape.

## Read
- AUDIT_MM.md, AUDIT_MM_summary.md, AUDIT_LL.md, BRIEF33.md;
- MM1_notes.md, MM2_notes.md, MM3_referee.md, LL3_notes.md (Thm A);
- FF1_notes.md, JJ2_notes.md / JJ3_notes.md (rigidity to avoid);
- writeup/"The Contamination Triangle.tex" §2.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Exact arithmetic for certificates. A finite or discretised search is a diagnostic, not a proof.
