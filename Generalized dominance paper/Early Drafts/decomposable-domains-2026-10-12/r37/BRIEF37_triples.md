# Brief 37: designing for (TC) itself, not acyclicity (20 October 2026)

This is still the mechanism-design phase. Deliver short screening results: exact finite certificates, counterexamples, and short proofs. Keep each note under about 8 pages. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions.

## Background
- The gated constructions get (TC) by forbidding cycles of every length. In three worlds this fails: fixed priority orders are excluded (PP2 Thm 6, refereed; memo §8.5).
- Audit's new proposal (20 Oct): *triple-local certificates*. Each world's verdicts are record-based ((IB)). For every three models, some strictly guiding additive evaluator supports every comparison the world makes among them, and preserves strictness. Different triples may use different evaluators. This gives (TC) immediately and permits longer non-additive cycles.
  - Audit's 5-region example: steps A{1,5}, B{2,5}, C{3,5}, D{4,5}, E{1}, with A≺B≺C≺D≺E≺A.
  - Lead's check (`triple/five.py`): with the verdicts propagated by (IB) to all 32 models, there are 0 (TC) violations, and every one of the 4,210 triples with comparisons has a certificate.
- Read:
  - the memo `DESIGN_MEMO.md` §§5–8;
  - `gate2d/Separation-Gated-Evaluators.tex` (especially Remark 10, the triangle condition, which is a consequence of (TC) alone);
  - `PP1_weakgate_construction.md` and its SAT harness in `PP1_py/`;
  - `PP2_weakgate_obstruction.md` and `REFEREE_PP2.md`.
- Axioms: reflexivity; strict (G); (IB); (TC) only; (S) (coherent selected models, undominated, competitive on supp p, closed sections); (LA); direct (C). Full four-advice domain, or regular models plus contradiction if needed (say which).
- **KKM.** Every rival must have a selected C_q with C_q ⪯_i X at all three worlds. This is a necessary consequence of (S) with closed sections, and it is the testable proxy for closedness on finite cells.

All files are under /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/.
