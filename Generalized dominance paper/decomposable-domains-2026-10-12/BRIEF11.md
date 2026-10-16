# Brief, round 12 (15 Oct 2026, 07:30): does the one remaining kind of world exist?

## Read first
1. termfix/TERMFIX_RULES.md in the scratchpad (terminology: domains are classes of evaluable models).
2. writeup/"The Contamination Triangle.tex":
   - §§2–3: setting, axioms, the U-domain M_U, adding up, relevant comparisons, regular models, M0/M1/M2;
   - §7.7: case M0 closed on M_U;
   - §8.4: building ordinal rankings directly.
3. N9_notes.md: the N9.4 normal form. On M_U, (G)+(IB) at a world is exactly a strictly monotone comparative ordering ≤_i of world-i error sets satisfying de Finetti cancellation A ≤ B ⟺ A∖B ≤ B∖A.
4. N17_notes.md and N19_referee.md. These cover:
   - the relevant comparisons 𝔚^reg_i (selected, i.e. coherent undominated, B against regular X);
   - SP^reg_i: some charge ≥ 0 on 𝔚^reg_i that is strictly positive on mixed problems;
   - modes M1 (a finite cancellation obstruction) and M2 (non-Archimedean);
   - fine (NC)-violating worlds (N17.7);
   - the decorative example N17.8;
   - Conjecture N17.B′.
5. P4_notes.md Part B and P4B_referee.md. These cover:
   - the strict-escape lemma;
   - N17.B′ for lexicographic worlds with charge levels (Theorem E2);
   - N17.B′ for complete worlds (Theorem E3, CHECKED via Savage);
   - Lemma T;
   - the reduction of the general n = 2 case to a certificate statement (§5.5);
   - the open class.
6. P2_notes.md and P2P3_referee.md: Theorem LX, P2.4 (flexible worlds), P2.6 (rigid exchanges need far dominators), P2.7.
7. P3_notes.md: the exact consistency test with the limit rule R5.
8. Source papers, read-only, in /mnt/user-data/uploads/Generalized dominance paper/: "Coverage after Neutral Abstention.tex", "Incomplete Rankings and Coverage.tex", "Independent Rankings Without Additive Structure.tex", "Loss Dominance Generalized v2.tex".

## THE QUESTION (task A)
On M_U, the only remaining route to an ordinal cover of T1 is a ranking satisfying:
- strict (G), (IB), (LA);
- (S) with closed sections for every model;
- (C);
- and, at some world i, ¬SP^reg_i: no charge ≥ 0 on the relevant comparisons is strictly positive on mixed problems.

By the two-world evidence, such a world must be incomplete, not lexicographic with charge levels, without a leading charge, not CP-a, and must have spread-out cancellation certificates.

**Does such a world exist inside a full system satisfying every axiom, for ANY target, in ANY number of worlds n ≥ 2?** Either construct one, with every axiom verified (closed sections for EVERY evaluable model; use the exact consistency test with R5 where possible), or prove that none exists. A proof could be N17.B′ in full, first for n = 2 and then for n = 3.

A construction for an easy target (precise, a normalised box, n = 2) would already be decisive evidence that the route is real. A proof for n = 3 would close ordinal coverage of T1 on M_U.

## RULES
- Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- Add no assumption to the framework.
- Constructions count only when every axiom is verified.
- If an attempt fails, give an honest failure report: say exactly where it failed.
- Write only your own note, plus scripts in a subfolder named after it, in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/.
