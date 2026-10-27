# Round 68 report: the two definitive manuscripts, written and verified

26 October 2026. Writers: WA68 (application) and WL68 (LDG). Verification was done on the manuscripts themselves:
- RA68a and RA68b: two independent referees of the application paper. RA68b also did the final round.
- RL68: referee of LDG, two rounds.
- RX68: cross-paper check.

## 1. The manuscripts

**Coherence and accuracy for sets of desirable gambles** (Konek and Campbell-Moore), 26 pages. Compiles cleanly.
- **Lead result: the repair theorem.**
  - Every incoherent model has a coherent replacement that is better by a uniform margin at every world.
  - The replacement's change could not be made by any coherent model.
  - The proof has two cases: consistent commitments (optimise within the hull, then trim) and inconsistent commitments (drop the part that loses at every world).
  - The minimax mechanism is explained: fractional acceptance, made exact by the null-boundary condition.
- **The ranking**, a consequence of the repair theorem.
  - The rule: accept a change if it only corrects errors. Otherwise, accept it only if it strictly improves integrated payoff and no coherent model could make it.
  - Proved properties: guidance, independence, finite-chain consistency, disjoint additivity, and no ties between distinct models. In general it is incomplete and intransitive.
  - These properties do not characterise it: the relation that accepts only guidance also has them.
  - A maximality proposition does characterise it. The ranking is the largest relation such that:
    - every guidance comparison is accepted;
    - every accepted comparison between distinct models strictly improves the score;
    - a change some coherent model could make is accepted only through guidance.
- **Main coverage theorem.** Every coherent target on the full gamble space is covered.
  - Scope: arbitrary sets of worlds; a separable gamble space with constants; models identified up to null sets.
  - Full support is assumed in the headline and can be dropped.
  - Dominance always holds with a strict improvement. A uniform improvement is available for each incoherent model, but not for every dominance comparison.
- **Other results:**
  - a general restricted-domain corollary;
  - one veto–Brier contamination example, with a self-contained appendix proof (Lyapunov, Zorn, separation). It is the contrast case: complete, transitive, score-based rankings can cover some imprecise targets.
- **Discussion.**
  - The achievement and the limitation are stated together. The construction represents coherence through dominance; it does not derive coherence from accuracy comparisons that are justified independently.
  - The stronger third condition (a restriction on each individual comparison) is recorded as an open question.
  - There is a related-work paragraph, including Seidenfeld–Schervish–Kadane (2012).

**Coherence, Dominance, and Generalized Loss** (Konek and Campbell-Moore), 22 pages, down from 43. Compiles cleanly. It is organised by three questions:
1. **What follows once coherent undominated replacements exist?** Permissibility, tie closure, and the role of transitivity.
2. **What checkable conditions ensure they exist?**
   - Leading theorems: Bayes choice with lower semicontinuity, for finitely and for arbitrarily many worlds.
   - The general finite theorem (KKM) and the local infinite theorem.
   - A transitive loss-ranking example showing a compact family is indispensable.
   - A remark that the abstract compactness condition is equivalent to the conclusion.
3. **How can rankings be constructed?** Proposition 7.1, with its caveats:
   - acyclicity needs guided changes to improve the score;
   - the content depends on how changes are individuated;
   - the companion paper's assumptions;
   - the third condition.

Applications: proper scores, probabilism on arbitrary domains, conditional reports, the countable example, and the Joyce counterexample as a short foil.

## 2. Verification

**Application paper.** Two independent referees re-derived every proof in the manuscript itself and found no mathematical error. Required changes, all made and confirmed in a second round:
- the acyclicity requirement is corrected: the earlier definition was unnecessarily strong. It now asks only that no chain of weak comparisons ends in a strict reversal. That permits ties between distinct models and is met by every total preorder, including the veto–Brier ranking. "Every cycle consists of identical models" is a special property of the universal ranking, not a requirement of covering;
- "in general incomplete and intransitive";
- scope stated inside the theorem statements;
- coherence framed as "up to the boundary", with the second role of (M2) stated;
- the veto–Brier contrast scoped to "some imprecise targets";
- a related-work paragraph;
- an incoherent example in Remark 4.4;
- jargon and terms removed or defined.

The final round found five text fixes, all made: one overbroad sentence, one reference, the summary of Seidenfeld–Schervish–Kadane, and two one-line justifications.

**LDG.** No mathematical error. All nine new or not-yet-refereed items are correct, including Proposition 7.1, which was also tested on 40,000 random instances. Required changes, all made and confirmed in a second round:
- the §7 framing;
- the permissibility wording;
- an unused lemma clause deleted;
- notation;
- self-containment of Figure 2(b);
- cuts of material nothing cites.

The lead made one final wording fix.

**Cross-paper (RX68).**
- No circular dependence: LDG cites the application only for illustration and attribution, and the application cites LDG only in one pointer.
- Neither paper relies on deleted material.
- LDG's pointer to the Zorn-lemma argument matches the application paper's appendix.
- LDG Proposition 7.1 and the application paper's ranking agree exactly.
- Terminology is reconciled: LDG's condition on priors is renamed "every prior is served at a world it charges".

## 3. For the author
1. **Authors.** Both papers list Konek and Campbell-Moore. The universal-coverage note listed Konek alone. Please confirm.
2. **References to supply or check:**
   - Konek, in *Philosophy and Phenomenological Research*, is cited as forthcoming; please supply year, volume and pages.
   - The theorem number for Aliprantis–Border Thm 6.30, the weak-* metrizability of the dual ball, is unverified.
   - LDG Figure 2(b) states a reconstructed score "of the kind in" Schervish, Seidenfeld and Kadane (2009), Example 4. You may want to substitute their exact score.
3. **Titles.** Please confirm them. The writer offered "Coherence and Dominance under General Rankings" as an alternative for LDG.
4. **Open questions** (stated in the papers):
   - nonseparable gamble spaces;
   - spaces without an order unit;
   - domains not closed under coherent hulls;
   - whether the third condition can be weakened while preserving coverage, and its independent justification.
