# Brief 42: the rescaled family, equivariance, repairs, and the cut skeleton (21 October 2026)

Mechanism-design phase, but this round aims at a construction or an exact obstruction, not at more screens. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated. Keep each note under about 10 pages.

## Read first (all paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `Rescaling.pdf` (the author's note): Q_p(g) = min_{m∈M} (p∘m)·g/(p·m) is coherent, and Q_p(g) > 0 iff P(p∘g) > 0.
- `AUDIT_rescaling_construction.md` (audit's explicit closed non-additive ranking; why it fails (S)).
- `AUDIT_round42_brief.md` (audit's proposed round: certificate inside the family; the repair lemma; (TC) for repair records; both clauses of (S)).
- `DESIGN_MEMO.md` §8 (especially §8.10: Theorem J and J1), `PP11_coupled_obstruction.md`, `REFEREE_PP11.md`, `PP2_weakgate_obstruction.md`, `REFEREE_PP2.md`, `gate2d/Separation-Gated-Evaluators.tex`.

## Setting
- Three worlds, problems g ∈ R³ modulo sign, Gaussian μ (only its null sets matter to the axioms), full four-advice domain.
- T1 = D_M, with M = c·1 + εΔ and c = (1−ε)/3.
- Rescaled family:
  - interior p: C_p := D_{M_p}, where M_p = {p∘m/(p·m) : m ∈ M};
  - boundary p: the corresponding limits.
- Axioms: reflexivity; (G), both halves; (IB); (TC) only; (S), i.e. coherent selected models, each undominated, competitive on supp p, with closed sections {p : C_p ⪯_i X} for each fixed X; (LA); direct (C).

## Lead's observations to build on (check them)
1. **The family is one orbit.** For interior p, C_p accepts g iff T1 accepts p∘g. So C_p = T1∘S_p, with S_p(g) = p∘g a positive diagonal map. Diagonal maps preserve the sign of every coordinate and preserve μ-null sets.
2. **Equivariance reduction.** If each world's ranking is invariant under positive diagonal maps (X ⪯_i Y iff X∘S ⪯_i Y∘S), then for interior p:
   - C_p ⪯_i X iff T1 ⪯_i X∘S_p⁻¹;
   - the interior defence clause is exactly "T1 is competitive on {1,2,3} against every model";
   - undominatedness of every interior C_p is exactly undominatedness of T1.
   Closed sections and the edge and vertex clauses become statements about continuity along the orbit and about limits as S_p degenerates. The two-world gated construction, applied to the rescaled two-world family, already has this form: its keys are translations in log-odds.
3. **Price of invariance.** There is no finite measure invariant under the diagonal group. So invariant verdicts cannot be additive over a finite measure; this is consistent with FF2, which excludes integrable fields.
4. **J1** (refereed) says that for imprecise interior targets, accepted-record sets cannot be closed in the rival argument. Audit's closed construction is closed, and fails exactly as J1 predicts. Any successful construction must jump across rivals at forced cuts, while staying closed along fixed-rival sections.
5. **Where the failures have come from.** No (TC) engine found so far has failed on (TC): additive scores, lexicographic gates, and audit's coarsest-cell counting. The failures are all in (S), meaning defence and KKM dominators: for every rival X, some selected C_q with C_q ⪯_i X at all three worlds.
