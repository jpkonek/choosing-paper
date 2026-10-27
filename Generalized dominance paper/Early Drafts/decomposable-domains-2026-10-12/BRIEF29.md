# Brief, round 37 (18 Oct 2026, 16:30): the exchange-rate design, decided by the exact (RB) test; plus a distinct non-transitive route

Read FIRST: AUDIT_HH_rate.md (audit's assessment of round 36 and the exact rate criterion) and AUDIT_HH_summary.md. Adopt all its corrections.

## Corrections adopted
1. **Divergence of k does NOT make small-record verdicts lexicographic** (HH2 Prop 6.1(e) is false as stated).
   - Counterexample: let the leading increment be a = μ(E) > 0 and the lower increment 2a − m, where m = μ(E) + μ(F) and 0 < a < m/(k(m)+2).
   - The lexicographic order accepts this record; the rate rule rejects it.
   - So neither the claimed escape from HH2 Thm 5.1 nor the failure of (Loc) follows from k → ∞.
2. **Failure of (Loc) is not a representation theorem.** "Non-Archimedean" must not be claimed from it. HH2 Cor 5.3 excludes only the specified integrable local descriptions, under the full domain and a selection continuous in measure through T1.
3. **HH2 Cor 6.2 needs an admissibility repair.** (S) requires EVERY selected C_p to be undominated, and competitiveness alone does not give this.
   - Sufficient repair: every C_p is undominated in the lexicographic base. The deletion rule keeps strict comparisons strict, so it preserves this.
   - Alternatively, prove protection directly for the reduced relation.
4. **HH3 proved nothing about all finite fragments.** The claim "an (FC) obstruction must involve infinitely many models" is unsupported: an (FC) violation is itself a finite chain.
5. **This design is one class, not "the one live design".** Its failure would close only this ansatz: additive two-level lexicographic bases, with a selection continuous in measure, under the rate rule. It would not close the non-transitive programme.

## The design (HH2 Prop 6.1, items (a)–(d) stand)
- **Base.** World i has a two-level lexicographic base (Φ_i, Ψ_i), additive with integrable densities; Φ_i weakly guiding, Ψ_i strictly guiding.
- **Rate rule.** k : (0, M] → (0, ∞) continuous, and K(t) = k(μ(supp t)). Accept the identity record ι, and every record t with Φ_i(t) ≥ 0 and Ψ_i(t) + K(t)Φ_i(t) ≥ 0.
- **What it gives (PROVED in HH2):** reflexivity, (IB), strict (G), (FC) with ordering extension L_i, ties exactly the lexicographic ties, and closed sections when the selection is continuous in measure.

## The exact test (audit's criterion (RB), PROVED in AUDIT_HH_rate.md)
- For a selected p and an evaluable X, write t = rec(C_p, X) and m = μ(supp t) > 0. For i ∈ supp p:
  - r_i = 0 if Φ_i(t) = 0 and Ψ_i(t) ≥ 0;
  - r_i = max(0, −Ψ_i(t)/Φ_i(t)) if Φ_i(t) > 0;
  - r_i = ∞ otherwise.
- Put r(p, X) = min_{i ∈ supp p} r_i. Only ONE active world needs to defend.
- A continuous rate giving competitiveness against every competitor exists **iff**
  (RB)  for every a > 0, sup{ r(p, X) : μ(supp rec(C_p, X)) ≥ a } < ∞.
- **Positive route:** prove (RB) for a candidate base, jointly over all worlds and all measurable competitors. The rate then follows automatically.
- **Negative route:** find competitors with μ(supp) ≥ a > 0 and r → ∞ at EVERY active world jointly. Natural adversary: leading gains and losses nearly cancel while the adverse lower-level change stays substantial.

## Constraints a base must still meet (from HH2 §6, GG1)
- Φ_i must charge the bulk near T1; otherwise FF2 Cor 4.2 binds.
- GG1 Prop 3.1 transfers: on M_U, (U2)-type bases with (P0), (V) force T1 or interior selected models to pay leading costs (GG1 Prop 4.1).
- HH2 vertex lemma 3.1: interior models near e_j must accept the vetoed one-positive sets, for veto-type leading levels.
- Admissibility: every C_p undominated in the base (or proved directly). T1 undominated. (C) direct, e.g. via trivial three-world base ties with selected models (VB's L3.3(b) argument).
- VB itself cannot be the base with VB's selection: HH2 Lemma 3.1 / vb_vertex shows that selection's vertex jump defeats every relation.

## Deliverables
A full cover of T1 (every axiom verified for arbitrary measurable competitors), or a precise PROVED obstruction to this class. Separately, a genuinely different non-transitive route (see the agent briefs).

## Read
- AUDIT_HH_rate.md, AUDIT_HH_summary.md, BRIEF28.md, AUDIT_nontransitive.md;
- HH2_notes.md (whole; especially §§1, 3, 5, 6), HH1_notes.md (foundation; Example B; the "T1 tied but not selected" escape), HH3_notes.md (Radon obstruction to additivity; fragments);
- GG1_notes.md (two-level members, Prop 3.1, Thm 3.3, Prop 4.1), L3_notes.md (VB, L3.3–L3.4);
- FF1_notes.md (plain posterior family, level lines, bets lemma), FF2_notes.md;
- writeup/"The Contamination Triangle.tex" §2.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Exact arithmetic for checks.
