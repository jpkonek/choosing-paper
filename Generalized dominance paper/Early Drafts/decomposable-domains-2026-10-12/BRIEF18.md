# Brief, round 26 (16 Oct 2026, 16:20): CHANGE OF METHOD — joint two-sided comparison systems

## Why the method is changing (audit's assessment, adopted by the author)
- The positive search so far used one narrow method: start from an additive or chain-based order, then add special comparisons (protected generators, projective-plane targets, ends). Failure of that method is not evidence that every independent ordinal construction fails.
- "Blind" (in R21, L4, M1, …) describes the WEIGHTS endorsing a world's comparisons. It does not mean the ranking ignores improvements: strict guidance still rewards every non-null pointwise improvement.
- U1 and V1 constrain specified classes ((Loc), and V1's hypotheses (Z), (UB), (H_Q)). They are not universal restrictions.
- **Requirements we are dropping.** Do NOT require, as a design constraint:
  - an additive base;
  - a leading density;
  - a one-dimensional chain of selected models;
  - (Loc);
  - closure under positive linear combinations of comparisons.

  Any of these may emerge in a construction, but none is to be imposed.

## Read first
1. Audit's note, copied locally: `AUDIT_nonlinear_programme.md` in this folder. It contains the transition-record language, the transition lemma, the joint construction with disjunctive competitiveness (K), the extension lemma to pursue, and its warnings.
2. Literature (fetch with WebFetch):
   - **Miranda & Zaffalon, Nonlinear desirability theory** (IJAR 2023): https://people.idsia.ch/~zaffalon/papers/2023ijar-ndt.pdf (Defs 2–5, Prop 2, §5: general closure operators, natural extension).
   - **De Cooman, Van Camp & De Bock, The logic behind desirable sets of things, and its filter representation** (IJAR 2024): https://users.ugent.be/~jdbock/documents/GdC-2024-IJAR-paper.pdf (disjunctive assessments; finite vs full consistency; Thm 31, Cor 32 and the §2.4 counterexample — finitary closure needed).
   - **Conder & Slinko** on discrete cones for comparative probability: https://www.math.auckland.ac.nz/Research/Reports/Series/509.pdf (§§2, 5).
   - **De Bock & de Cooman 2019** (choice functions): https://proceedings.mlr.press/v103/de-bock19b/de-bock19b.pdf.
3. writeup/"The Contamination Triangle.tex":
   - §2: axioms, domains, the four kinds of advice and their background order, (LF), the full domain;
   - §7 (M0closed) and §8.6 (fixed-point reduction; M3: on two-sided domains a cover forces a degenerate "ladder" field — blind on a silence step or a wrong step). Treat this as a necessary condition to meet, not an obstacle to the method.
4. Source papers in /mnt/user-data/uploads/Generalized dominance paper/:
   - "Coverage after Neutral Abstention.tex" §3: the exact consistency test, which this programme extends;
   - "Vacuous Targets and Transfinite Construction.tex" §5: the union lemma; closedness not preserved by unions; permanent open forbidden neighbourhoods;
   - "Loss Dominance Generalized v2.tex": the axioms and KKM;
   - "Full Coverage by Homothetic Credal Families v3.tex": the two-world additive coverage and the (IB) discussion.
5. Notes:
   - P3_notes.md: the limit rule R5 and the false extension lemma — know exactly why the earlier extension lemma failed;
   - L3_notes.md: Prop L3.1 (on two-sided domains, vertex models are precise; Theorem L3.4, vetoes cannot be paid);
   - M3_notes.md: two rank steps per {+,0,−} problem;
   - B1_notes.md: transfer chains through link classes. Know when sum-closure is legitimate: it is only for ternary results.

## RULES
- As in BRIEF13. Every construction must verify every axiom: strict (G), (IB), (LA), (S) with closed sections for EVERY evaluable model and competitiveness on supp p, (C), (LF) at T1, T1 undominated.
- Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- Add no assumptions.
- Write only your own note, plus scripts in a subfolder named after it, in this folder.
- Deliver one of:
  - an invariant or extension theorem;
  - a construction;
  - a precise single obstruction, proved.
