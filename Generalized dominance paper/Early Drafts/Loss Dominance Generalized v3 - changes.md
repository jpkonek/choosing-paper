# Loss Dominance Generalized v3: changes from v2

25 October 2026. v2 is unchanged. v3 reorganises results already present in v2; it adds no new main theorem.

## What moved to the centre
- **Finite (B) is now the main technical condition** (Section 2.1). Its three requirements are stated separately: (B1) closed certificate sections, (B2) support-wise coverage, (B3) one coherent undominated realiser meeting all certificates at each index. No compact indexing (I) is assumed for finitely many worlds.
- **Main theorem (Thm 3.2)** is proved directly from (LA) and (B): (a) weak dominance of every model by a member of C_L; (b) every undominated model is tied at every world with a member of C_L; (c) with (C), U_L = C_L and every model outside C_L is dominated by a member of C_L. Weak dominance and dominance are kept apart; strict improvement at every world is not claimed.
- **(S) is kept as a stronger sufficient condition**: Prop 2.1 proves (S) ⇒ (B); Cor 3.3 states the (S) version.
- **Infinite worlds**: (I) and (B∞) (v2's bounds condition, now with realisers from the compact family of (I)). Thm 3.4 gives the full compactness proof; Cor 3.5 is v2's (I)+(S∞) corollary. The paper says explicitly that it does not show (I) can be dropped for infinitely many worlds.

## Relational assumptions separated
- Section 1 now allows arbitrary world-wise relations (not assumed reflexive, transitive or complete). Weak dominance, all-world ties, dominance and competitiveness are defined model by model.
- Thm 3.2 and Thm 3.4 use no order properties. Results needing transitivity are collected in Section 3.3 (Prop 3.6, Cor 3.8). Profiles (K, U_R) are used only for preorder rankings.
- New Example 3.7 (one world, reflexive but not transitive): (B) and (S) hold, a model tied with the undominated coherent model is dominated. This shows why Prop 3.6 needs transitivity. It comes from the independent check.
- Prop 5.1 (permissibility) is split into (a) ties, (b) with (C), (c) preorder rankings. The "if and only if" now requires (C) or a preorder ranking.

## Certificates versus selections (new Section 4, built from v2 material)
- 4.1 explains the two separations: (i) the certifying prior need not equal the index (the conditional-probability construction, which still satisfies (S)); (ii) under (B), regularly varying certificates may have coherent realisers that jump.
- 4.2 moves v2's three-world example forward (Prop 4.1), adding an incoherent model with profile (2,2,2) so that the dominance conclusion is not empty. Remark 4.2 gives the explicit edge certificates, now with an explicit parametrisation, and shows the realiser **must** jump (both points from the independent check). The Bayes-form impossibility is kept.
- 4.3 states the limits: (B) is not called the weakest condition; certificates built from a known dominance conclusion (Prop B.6, Remark B.8) repackage it; rival-specific certificates are circular; applications must supply certificates independently.

## Other edits
- Example B.7 (the "hole") is restated for finite (B). It shows that without compactness of K, (B) can be strictly stronger than the conclusion, and it does not use (I).
- Example B.1 now also notes that (B1) cannot be dropped.
- Cor A.3 (coherent Bayes models exist) is stated under (I) with lsc losses and (B∞). It is **not** established under finite (B) alone; the paper says so.
- New subsection A.9 restates Lemma A.11 (Bayes-form certificates) for finite (B) and for (B∞), with the margin-theorem extension.
- Prop A.1 (change of scale) now lists (B) and (B∞).
- Scope section rewritten: the results concern one ranking; they do not establish coverage of any coherent class; (S)-based impossibility results do not carry over automatically to (B).
- New Appendix E: theorem-by-theorem hypothesis table.
- Removed: red markup, names on examples and remarks, the stray page break, the "See § X" placeholder, the label clash between axiom (C) and a recipe item.

## Checks
- An independent check confirmed: the KKM lemma; that the finite (B) proof uses no order properties (brute force over all relations on 3 models and 2 worlds: no failures); (S) ⇒ (B); the three-world example including (2,2,2) (exact checks at 11,476 simplex points and 5,001 edge points); Example B.7 uses only finite (B). Its four repairs are all in v3.
- Compiled: 33 pages, no undefined references, no overfull boxes.

## Results to re-audit under (B) (project work, not in the paper)
v3 does **not** show coverage of coherent gamble models, does not vindicate T1, and does not invalidate any earlier impossibility result. Results that rely on **closed full comparison sections of a selected family**, i.e. on (S) itself, need new proofs before they can be read as excluding (B). Candidates (to check one by one whether (S) is used essentially):
1. Contamination Triangle: Theorem gm, the M0-closedness result, L4 / R21.
2. Quorum rankings: Q4.1–Q4.2.
3. "Three complete rankings cannot cover" and "Complete rankings for any number of worlds".
4. The selection-count lemmas (A, B, E).
5. Rounds 44–60: Theorems Q, E, K, K′, PP52 Thm 4.1, and the PP64 partial-system framework.

Results that show directly that some model is weakly dominated by no coherent model still exclude (B) as well.
