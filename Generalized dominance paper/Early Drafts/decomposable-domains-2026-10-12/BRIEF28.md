# Brief, round 36 (18 Oct 2026, 10:30): coverage WITHOUT full transitivity

Read FIRST: AUDIT_nontransitive.md (audit's instruction for this round). It takes priority over the NA-credal classification, whose representations are transitive by construction.

## The change
- Rankings are no longer assumed to be preorders. Each world ≼_i is REFLEXIVE, and satisfies one of:
  - **(FC) finite-chain consistency:** A_0 ≼_i A_1 ≼_i … ≼_i A_k ⇒ ¬(A_k ≺_i A_0);
  - **(TC) three-model consistency:** A ≼_i B ≼_i C ⇒ ¬(C ≺_i A).
- X ≺_i Y means X ≼_i Y and not Y ≼_i X.
- Endpoint comparisons are NOT installed. A chain from A to B forbids B ≺ A; it does not require A ≼ B.
- Keep the two conditions separate. A (TC)-only construction must report its longer strict cycles explicitly.

## Unchanged
- Strict (G).
- (IB): replacement of common advice in a single comparison.
- The domain and (LF) at T1, (LA), and (S): closed sections F_i(X) = {p : C_p ≼_i X} for every evaluable X, plus competitiveness on supp p.
- Coverage of T1.
- **(C), stated directly:** if X is mutually ranked no worse than a coherent undominated model at every world, then X is in the coherent undominated class.
- Do NOT use equal-profile equivalence classes. Do NOT assume tied models have identical comparisons with third models.

## Facts to use (author's observations; verify before relying on them)
1. **(FC) is Suzumura consistency** (Suzumura 1976; Bossert–Suzumura, Consistency, Choice and Rationality, 2010).
   - A reflexive relation is Suzumura consistent iff it has an ordering extension: a complete preorder containing it that keeps its strict comparisons strict.
   - Equivalently, its transitive closure keeps every strict comparison strict.
   - So under (FC) each world's verdicts are those of SOME complete preorder, which need not satisfy (IB).
   - **The new freedom is exactly this:** comparisons obtained by composition need not obey independence, and need not be installed.
2. **Record formulation.** (IB) says that the verdict on a pair depends only on its transition record rec(X, Y) (AUDIT_nonlinear_programme.md).
   - So a world is a set 𝒜_i of accepted records, NOT required to be closed under composition (contrast the transition lemma for preorders).
   - Strict (G): every improving record is accepted, and no worsening record is accepted (for non-null changes).
   - (FC): no realisable cycle A_0, …, A_k = A_0 with every rec(A_j, A_{j+1}) ∈ 𝒜_i and at least one step strict (rec(A_{j+1}, A_j) ∉ 𝒜_i).
3. **What survives.** FF2 Theorem 4.1 (refereed in GG3, with the repair to Cor 4.3) states that it uses no (IB), no transitivity, no closed sections and no (C). It therefore survives: with a selection continuous in measure and T1 competitive, no single integrable strictly guiding field endorses all bounded-region comparisons out of selected models near T1.
   - Theorem gm, the intersection theorem and the NA-credal results concern transitive classes. They constrain only those classes.
   - Q4.2, M0closed, L4 (Hahn–Banach endorser field), L3.4, CC2 and GG2 Theorem B must be checked for hidden uses of transitivity.
4. **The author's splicing construction** (project doc "Splicing at a Pair-Indexed Weighting") satisfies (G) and (IB) for any base with (G).
   - With the homothetic ordinal base it has a STRICT 3-cycle Y ≺ X ≺ Z ≺ Y in two worlds, so it violates both (TC) and (FC).
   - Other bases are untested.
   - Splicing with an additive base reproduces the base.

## Primary objective
A full cover of T1 under (FC) (or, failing that, (TC)). Next best: an extension theorem preserving (IB), closed competitive defences and the chosen no-reversal condition WITHOUT transitive closure. An obstruction must show that the weakened requirements themselves force a violation; failure of the threshold scheme is not enough.

## Read
- AUDIT_nontransitive.md, AUDIT_nonlinear_programme.md, SPLICING_summary.md.
- writeup/"The Contamination Triangle.tex" §2 (axioms; search for where transitivity is used).
- "/mnt/user-data/uploads/Generalized dominance paper/Loss Dominance Generalized v2.tex" (the dominance theorem and KKM).
- FF1_notes.md (§§3–5: cell arrangements, bets, level lines of the plain family; scripts ff1py/arr.py, lin.py, closure.py).
- FF2_notes.md (Thm 4.1), GG3_notes.md (representation theorem, Part B referee), GG2_notes.md (Thm A, Thm B).
- EE2_notes.md (splices, Lemma 2.2–2.3, cell decision procedure).
- L4_notes.md, BB2_notes.md, CC3_referee.md (Q4.2), L3_notes.md (VB).

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Finite searches are diagnostics: a positive result must cover arbitrary measurable competitors and prove closed sections.
