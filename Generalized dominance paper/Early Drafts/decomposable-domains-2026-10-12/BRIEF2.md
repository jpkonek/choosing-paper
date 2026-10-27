# Brief, round 2 (12 Oct 2026, 21:45). Read BRIEF.md first, then this file.

The auditor's assessment is at "$HOME/mnt/CPMs/outputs/decomposable-domain-audit/Assessment of Decomposable Domain Results 2026-10-12.md"
(device, read-only); a copy is in this folder as AUDIT_ASSESSMENT.md. Its corrections are accepted:
1. Rigidity of the whole undominated family is stronger than coverage requires. Coverage of a target needs
   only SOME system vindicating that target; that system need not vindicate anything else in particular.
2. Bayes uniqueness ≠ selection uniqueness: for a fixed additive system each interior weighted objective has
   an a.e.-unique Bayes minimiser, but (S) allows reindexing (e.g. C_t = B_{t²}).
3. R1 Thm 4.1 excludes the prescribed family K_q=(1−ε)σ(q)+εΔ on an open set, not the target.
4. Open possibilities for T1 left by R1/R4: advice that every evaluable model gives, away from the target's boundary ((LF) does not imply
   R4's (H0)); merely measurable charts (dense discontinuities; (H1) is an extra hypothesis); R4 Prop D has
   a GAP (non-constant need not mean injective), so Prop F and the "diagonal-projective caps" picture are
   conditional.
5. R3 Theorem L needs (H1)–(H3); an error-only primary penalising bad/contradictory advice on unanimous
   problems only is compatible with (S) (auditor's example).
Referee repairs in R6_referee.md, R8_referee.md, R9_referee.md apply to the notes R1–R7.

THE SINGLE-TARGET ADDITIVE PROBLEM (precise). n = 3. T = D_K with K = (1−ε)u + εΔ (or a generic interior
triangle). Find, or prove impossible: a decomposable domain (measurable advice ranges A(g); singleton advice ranges, on
which every evaluable model gives the same advice, permitted on every pair {g,−g} with g ∉ N and −g ∉ N, for an
open N ⊇ ∂T\{0}; on pairs meeting N the advice ranges must contain every acceptance-set change, as (LF)
requires), and measurable integrable per-problem penalties ℓ_i(g,a), strictly increasing in guidance rank
at world i on A(g), such that: (i) for every interior prior the Bayes model is a.e. unique and coherent;
(ii) at each vertex the Bayes model is coherent; (iii) at boundary priors a coherent Bayes model exists and
the KKM/(S) argument of v3 thm:general goes through (state exactly what boundary condition you need);
(iv) T is the Bayes model at some interior prior p*. Nothing else is required of the family; in particular
nothing requires the Bayes models at other priors to be contamination sets or to vary in any prescribed way.
