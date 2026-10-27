# Brief, round 43 (19 Oct 2026, 08:00): one bounded test of the quorum class, with explicit success criteria

Read FIRST: AUDIT_NN.md and AUDIT_NN_summary.md (audit's strategic assessment of round 42).

## Corrections and discipline adopted
1. **The general blocking-cone collapse theorem (NN1 Lemma 2.1 / NN2 Thm 2.3) is retained. Committee-size escalation is retired.**
2. **The interior sum relation u₁ + u₂ + u₃ = 0 is the general three-world case, not a "narrow gap".** Converting it to the intersection form needed by the collapse is a substantial unproved step.
3. **NN1 Example 5.1 is weak data.** Boundary alignment at two points is far weaker than (QS) against every measurable rival at one model. The construction hierarchy is:
   - (a) compatible boundary data;
   - (b) ONE coherent model with exact (QS) (T1 alone: achieved);
   - (c) a NONCONSTANT family through T1 with exact (QS) on a parameter neighbourhood;
   - (d) a full family on the simplex.

   We are at level (b).
4. **Plane-wise edge proportionality is not a global field.** Ratios and participating judges can vary between planes (NN2 Obs 5.1). No open-and-closed propagation principle is established outside the min-cell case.
5. **NN3's analytic repair does not exclude smooth flat judges in general.**
6. **Even excluding all finite quorum systems would leave the general (TC) ordinal question open.**

## Success criteria for this round
- **OO1 (negative) succeeds only if it either:**
  - (i) PROVES a complete impossibility theorem for finite quorum systems with 3q > 2n through T1 (any judges, any coherent selection continuous in measure, any decomposable (LF) domain); or
  - (ii) states the EXACT missing global rigidity lemma and PROVES that it, together with already-proved results (collapse theorem, edge identities, FF2/MM1 imports), implies that impossibility theorem. This must be a fixed-field or equivalent global conclusion actually usable downstream. "More local proportionality" or "collapse spreads inward" does not count.
- **OO2 (positive) succeeds only by constructing** FIXED judges (some finite (n, q) with 3q > 2n; four of three is fine) and an actual NONCONSTANT coherent family p ↦ C_p, continuous in measure, defined on a parameter neighbourhood of T1's index, passing through T1. It must satisfy EXACT (QS) against EVERY measurable rival at every index of that neighbourhood. The proof must not rest on boundary samples or weak certificates.
  - Allow nearby credal sets to change shape.
  - Neither the posterior family nor persistent triangular corners may be imposed without a construction-specific reason.
- **Decision rule (author's).** If neither criterion is met, the quorum results will be consolidated and the representation class reconsidered. Another minor variation will NOT be announced as the final route.

## Also this round
- **OO3 (consolidation, in parallel).** Write a consolidated, LaTeX-ready note of the quorum results of rounds 40–42, with exact statements, hypotheses, statuses and dependencies. It covers:
  - the foundations (LL3 Thm A);
  - the fixed-margin exclusion;
  - the strict-sign lifting lemma;
  - the escape certificate;
  - the branch form and boundary alignment;
  - the general collapse theorem;
  - edge identities;
  - the exclusions for analytic, min-cell, cellwise-linear, world-separable and proportional judges;
  - the T1-only certificate;
  - the open sum-form question.

## Read
- AUDIT_NN.md, AUDIT_NN_summary.md, AUDIT_MM.md, AUDIT_LL.md, BRIEF34.md;
- NN1_notes.md, NN2_notes.md, NN3_notes.md, MM1_notes.md, MM2_notes.md, MM3_referee.md, LL1–LL3 notes, AUDIT_quorum.md;
- writeup/"The Contamination Triangle.tex" §2.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Exact arithmetic for certificates.
