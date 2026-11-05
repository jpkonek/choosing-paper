# WA86 change log: app_ldg.tex

Output: app_ldg.tex and app_ldg.pdf. The PDF is 13 pages, built with pdflatex. The build has no errors, no warnings, no undefined references and no overfull or underfull boxes. The lead renames the file on copying to `Coherence and accuracy for sets of desirable gambles - LDG application.tex` (GUIDANCE86 §2). The title and the author line ("Jason Konek") are unchanged. The bibliography uses only entries already in the sources: LDG manuscript, Rudin, Diestel–Uhl.

## Structure (follows GUIDANCE86 §§4–9)

1. **Setting.**
   - Def 1.1: gambles, with the two-sentence limit for infinite worlds. ℓ^∞ is excluded for infinite Ω; C(Ω) is allowed for compact metrizable Ω.
   - Defs 1.2–1.3: D1–D4; states, P_Q and D_Q.
   - Lemmas 1.4–1.5: states and D_Q.
   - Def 1.6: (M1) and (M2) only. It explains full support and points to Lemma 6.1.
   - Def 1.7: models and almost coherence. One fixed μ; C is the class of almost coherent models.
   - Lemma 1.8: identification (D = D_{K_D} a.e.; D_Q = {P_Q>0} a.e.; D_P ∩ {q>0} = D_conv a.e.). The note that {P_Q>0} represents D_Q is stated once.
   - Def 1.9: Bochner payoff vector.
   - Def 1.10 and Lemma 1.11: hull, including monotonicity.
   - Lemma 1.12: contraction. Lemma 1.13: trimming.
2. **Ranking.**
   - Def 2.1: rankings and dominance, with the LDG orientation correspondence. LDG's a ⪯_ω x is our a ⪰_ω x.
   - Def 2.2: changes and guidance at a world.
   - Def 2.3: the payoff ranking L_μ, with a note that it is incomplete.
   - Def 2.4: reflexivity, world-by-world guidance, independence in arbitrary contexts, finite-chain consistency, the three-model condition and tie substitution.
   - Lemma 2.5: guidance at every world, for arbitrary Ω via a countable Ω_0.
   - Prop 2.6: elementary properties. Transitivity is not claimed.
3. **Prop 3.1: every almost coherent model is undominated.** This is proved before selection, with a hull branch and a guided branch.
4. **Fixed assignments.**
   - Def 4.1: finite lists of inequalities.
   - Lemma 4.2: approximation, with strict margins, (1−λ)Q+λS ⊆ P, and ∫_{D_Q∖D_P}‖g‖ → 0.
   - Def 4.3: the assignments b^j_q, with F(G)=G and F(∅)={ω_0}, and t_F.
   - Lemma 4.4: the assigned models are almost coherent and undominated; continuity.
5. **Selection and dominance.**
   - Def 5.1: countable selection, restated from LDG with the evaluability of assigned models noted.
   - Thm 5.2: cites LDG Thm 2.5.
   - Def 5.3: (E), (A), (S_σ), (T_σ). (S_σ) and (T_σ) are per ranking.
   - Thm 5.4: cites LDG Thm 3.4(a), (d), (e) and Cor 3.5.
   - Lemma 5.5: gap (Step 1).
   - Lemma 5.6: listed set and hull chain (Step 2).
   - Lemma 5.7: witnesses, closedness, coverage and ties (Step 3).
   - Thm 5.8: main theorem (Step 4, applying LDG).
   - Cor 5.9: family-level conclusion.
6. **Lemma 6.1.** (a) Existence of an atomless, full-support measure with (M1) and (M2) on every permitted E. (b) Under full support, distinct credal sets give distinct models.
7. **Scope.** Two sentences on limitations.

## Citations to ldg_countable.tex

These are checked against ldg_countable.aux after its revision.

| Cited result | Content |
|---|---|
| Defs 2.2–2.4 | Countable selection |
| Thm 2.5 | The general theorem; nonempty ⋂K_ω, with weak dominance and dominance |
| Defs 3.1, 3.3 | Dominance principle; (E), (A), (S_σ), (T_σ) |
| Thm 3.4(a) | Dominance under one ranking, and U_L = C_L |
| Thm 3.4(d) | The partition, without (E) |
| Thm 3.4(e) | Non-vacuity, using (E) |
| Cor 3.5 | Dominators in C_L |

No TODO remains.

## VER86 / coordinator points applied

1. The manuscript does not say that Q ⊆ int_S P is insufficient. After Lemma 4.2(c), one sentence presents the margin proof as one way to obtain the neighbourhood and notes that compactness also gives it.
2. b^j_q is called almost coherent throughout (Lemma 1.8(c), Lemma 4.4(a), Thm 5.8(d)). Nothing is called a "coherent dominator".
3. The citations follow WL86_changes.md, including the new part letters of Thm 3.4. The orientation correspondence is stated in §2 and again in Def 5.1.
4. F(∅) := {ω_0} is fixed in Def 4.3, and Def 5.1 includes G = ∅. The assigned models lie in M, which is the full domain of every ranking.

## Cut, per GUIDANCE86 §9 and BRIEF86

The following are omitted: consolidation and the (A1)–(A4) proof; (M3); maximality; boxes and veto–Brier; numerical work; the general Ψ-field; neighbourhood robustness (ρ, violation-mass minima, radii); the countable-subcover argument; the repair theorem and minimax; advice/(M4) material. The trimming lemma is kept as a geometric lemma, and the repair theorem is not invoked.

## Proofs

Every lemma used is proved in the paper. The exceptions are standard cited facts: Banach–Alaoglu, Hahn–Banach separation (Rudin Thms 3.4, 3.10), and the Bochner integral (Diestel–Uhl). Two arguments are tightened relative to app_long:
- The identification lemma now uses only Hahn–Banach for the open cone D + D°_S, not the bipolar theorem.
- The approximation union ⋃D_{P_n} = D_Q is shown to be exact.

Labels: all lemmas, propositions, Thm 5.8 and Cor 5.9 are PROVED. Thms 5.2 and 5.4 are cited from LDG and CHECKED against its statements. No GAP or ERROR. **There is nothing I could not prove.**

## Notes for the lead

- 13 pages, within the 15-page ceiling. Proof completeness was prioritised over the 10–12 target.
- The infinite-world sentences and the scope sentences are deliberately short; the author may wish to revise their prose.

## After REF86

Before these changes, the file was backed up as app_ldg_v1.tex. Every MINOR point that REF86 raised for the application is applied, using its replacement text.

**A1.** In Def 5.1, (W2) and (W3) now state their own quantifier over finite G.

**A2 (notation).** Each symbol now has one meaning:

| Where | Old | New |
|---|---|---|
| Lemma 1.4(a) | dense sequence (h_n) | (e_n) |
| Lemma 1.4(e) | dense sequence (h_j) | (u_j) |
| Lemma 1.8 | element d ∈ D | u ∈ D |
| Lemmas 1.12–1.13 | P_{Q_Z} written P | \underline P_Z |
| Lemma 2.5 and Prop 3.1 | almost coherent model C | K |
| Lemma 5.5 | set L | X⁻ |
| Lemma 5.5 | d | β (γ ≔ β) |
| Lemma 5.7 and Thm 5.8(d) | margin d | κ ≔ γ/2 |

After these changes, L denotes only rankings, d only the metric on S, 𝒞 only the class of almost coherent models, and P only credal or listed sets.

**A3.** The last sentence of Cor 5.9 is replaced by REF86's text. It now says that {L_μ} witnesses non-vacuity for families also required to satisfy guidance and independence, and that (A) may be assumed directly.

**A10.** (T_σ) in Def 5.3 now reads: "the family in (S_σ) for L can be chosen so that the witnesses for every incoherent model exclude ties."

**A12.** The second Scope sentence now states that the results hold for each finite Borel measure satisfying (M1) and (M2) on a separable gamble space. The section is still two sentences.

**S1.** Thms 5.2 and 5.4 are now unnamed. Their citations open the theorem text: "The following is [LDG, Theorem 2.5]" and "The following are [LDG, Theorem 3.4(a), (d), (e) and Corollary 3.5]".

**S2.** The commentary sentence after Lemma 4.2(c) is cut.

**Rudin.** Banach–Alaoglu is now cited as [Rudin, Theorem 3.15].

**Unchanged.** No result numbers changed, and the LDG citations still match ldg_countable.aux.

**Build.** pdflatex builds cleanly, with no errors, warnings, undefined references or overfull/underfull boxes. The paper is still 13 pages.
