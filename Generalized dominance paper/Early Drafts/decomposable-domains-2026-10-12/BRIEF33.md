# Brief, round 41 (18 Oct 2026, 21:20): strict quorum competitiveness (QS)

Read FIRST: AUDIT_LL.md (audit's review of round 40, with the strict-sign lifting lemma and the exact test) and AUDIT_LL_summary.md.

## Corrections adopted
1. **The fixed relative margin is retired** (LL1, LL2). LL2's closed-section version uses the absence of nontrivial ties; keep that qualification.
2. **LL3's certificate uses coherent CANDIDATE models,** not models proved competitive and undominated in a full system. Coherence of the bases does not ensure an endorser, but non-endorsement in a completed cover is not yet exhibited.
3. **LL2 Prop 8.3 (weak Bayes in every branch) is NECESSARY only.** LL1 Prop 6.3 is an exact criterion for a different rule, with virtual fields ℓ − ησℓ′, not plain mixtures. The two do NOT give "the same exact test".
4. **LL1's relative-net-margin class loses automatic admissibility and (C).** Its positive-mixture condition is sufficient for (C), not necessary. This class is secondary.

## The target: (QS)
- **Setting.** At each world i there are n strictly guiding integrable additive judges, with quorum q and 3q > 2n (e.g. n = 4, q = 3). Take a coherent selection p ↦ C_p, continuous in measure on the whole simplex, through T1.
- **Notation.** Δ_iv(p, X) = L_iv(X) − L_iv(C_p).
- **(QS).** For every p and every X ≠ C_p (mod null sets), some i ∈ supp p has at least q judges with Δ_iv(p, X) > 0 (STRICT preference for C_p; no margin).
- **Lifting lemma (audit; to be refereed).** (QS) holds iff there is a continuous nondecreasing ψ with ψ(0) = 0 and 0 < ψ(s) ≤ s (it may be chosen with ψ(s)/s → 0) such that the shrinking-margin quorum rule makes every C_p competitive.
  - The rule: judge iv supports C R_i X iff Δ_iv ≥ ψ(d_iv).
  - The proof is by compactness/purification: a uniform separation δ(a) > 0 at gross size ≥ a.
  - Then the quorum lemmas give (IB), strict (G), (TC), closed sections, no nontrivial ties, direct (C) and selected admissibility. So **(QS) for a family through T1 gives a cover of T1 under (TC).** No (FC) claim is made.
- **Exact branch test (n = 4, q = 3).** (QS) fails at p iff some X ≠ C_p and some pairs F_i (one per active world) have Δ_iv(p, X) ≤ 0 for all v ∈ F_i. The inequalities are NONSTRICT.
  - There are 216 branches at full support.
  - Branch F passes iff A_p ∩ {Δ_iv ≤ 0, (i,v) ∈ F} = {0}, where A_p is the compact convex attainable set of full (Δ, d) vectors.
  - Equivalently: maximising Σ d_iv over that intersection gives 0.
- **Sufficient certificate.** For every branch F and every p, some nonnegative nonzero mixture of the judges in F has C_p as its UNIQUE minimiser.
  - Do NOT require a single mixture across branches or indices.
  - Do NOT require strictly positive weights unless proved necessary.
  - Do NOT require that every Bayes model of every judge mixture be coherent: (QS) has not been shown to need that.

## Read
- AUDIT_LL.md, AUDIT_LL_summary.md, BRIEF32.md, AUDIT_quorum.md;
- LL1_notes.md (mirror swap Lemma 2.1, Thm 3.1, Lemma 4.1), LL2_notes.md (Lemma 2.1 distorted Bayes, gap lemma, Prop 6.1, §8), LL3_notes.md (foundations; the certificate out of coherent bases);
- FF1_notes.md (plain posterior family, acceptance geometry, bets lemma), JJ2_notes.md / JJ3_notes.md (how unique interior Bayes plus coherence forces rigidity, which (QS) must avoid), JJ1_referee.md and II2_notes.md (compactness/purification);
- writeup/"The Contamination Triangle.tex" §2.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Exact arithmetic for certificates. A finite or discretised search is a diagnostic, not a proof.
