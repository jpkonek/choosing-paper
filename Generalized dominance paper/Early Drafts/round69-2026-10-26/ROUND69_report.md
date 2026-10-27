# Round 69: submission-readiness review (26 October 2026)

Mathematics is unchanged from round 68. This round made only presentation and interpretation changes, plus the auditor's four points.

## Auditor's points
- **Acyclicity.** The round-68 report now describes the change accurately. The old definition was unnecessarily strong. The requirement is now only that no chain of weak comparisons ends in a strict reversal. That allows ties and is met by every total preorder. "Every cycle consists of a.e.-equal models" is a special property of the universal ranking. Both papers now say this.
- **Aliprantis–Border.** The pinpoint citation is replaced by a short self-contained proof (Appendix A, Lemma 2.2(a)) that the state space is weak-* metrizable. A continuous bijection from a compact space onto a metric space is a homeomorphism. PR69a checked the proof.
- **LDG Figure 2(b).** It is labelled as the paper's own example illustrating the phenomenon discussed by Schervish, Seidenfeld and Kadane.
- **LDG title.** The title is now *Coherence and Dominance under General Rankings*. The application paper's citation is updated to match.

## Readiness reviews (PR69a application, PR69b LDG)
Each review covered: whether the introduction identifies the main theorem; consistent scope distinctions; coherence modulo μ before first use; optional properties versus requirements; a page-by-page visual check; references and cross-references.

**Application paper.** 12 presentation fixes:
- Introduction: "main theorem" now means the repair theorem. Coherence modulo μ is defined before "every incoherent model" is first used.
- §6.3: new paragraph on acyclicity.
- Line-break and notation fixes.

**LDG.** 12 presentation fixes:
- Introduction: names the main result for each question. States that rankings need not come from losses. States that the companion's ranking need not satisfy the Bayes-choice or compact-family conditions.
- §7: "acyclic" replaced by what Prop 7.1(a) proves.
- Three figure labels repositioned.

**Lead edits after review:**
- Application, Thm 6.8(d): "equals it a.e.".
- Application: companion title in the bibliography set in sentence case.
- LDG §3.2: the unverifiable pointer to "Example 1" of SSK09 is removed. The sentence now cites the paper's own section on proper scores; nothing depended on it.

Both papers compile cleanly: application 26 pages, LDG 22 pages.

## Remaining items for the author
1. **Authorship.** Both papers list Konek and Campbell-Moore. This needs confirmation with Catrin, and the author names are not yet in the PDF metadata.
2. **Konek, PPR.** Cited as forthcoming. Supply the final details, then remove the LaTeX comment.
3. **References to confirm:**
   - the one-sentence summary of Seidenfeld–Schervish–Kadane (2012);
   - Nielsen page numbers (402–427);
   - the Quaeghebeur chapter pages (1–27).
4. **Optional.** LDG Figure 2(b) could add "with their forecast", since SSK09's Example 4 uses the same forecast (0.6, 0.7). This comes from a summary of their technical report and is unverified.

## Author's correction: dominance is derived, not assumed (evening, 26 October)
The author pointed out that the LDG opening presented the "dominance conclusion" as an assumption: §3.1 said "Four conditions will be used" and listed it. The mathematics derived it, but the framing hid this.

**LDG has been restructured.** RL69 checked the restructure independently; no mathematical statement changed.
- **Section order:**
  1. Setting, with the dominance property defined as a claim to establish.
  2. Bayes-choice theorems.
  3. General theorems. The finite theorem is described as a weakening of the selection argument: KKM with closed subsets of the comparisons only. The local infinite theorem adds compactness.
  4. Margins.
  5. Consequences, presented as a logical observation, with permissibility resting on the theorems.
  6. Construction, where Prop 7.1(c) reduces dominance to the existence of improvements and the companion proves dominance directly through its repair theorem.
  7. Applications.
  8. Scope.
- **RL69 changes:**
  - a new Lemma 2.4 removes the forward references;
  - every theorem that derives the property says so;
  - Prop 6.5's hypothesis is stated precisely;
  - "classical" is dropped;
  - the abstract is trimmed to 251 words.

**Application paper.** It already proved dominance, so only the framing changed:
- the cover definition now says its conditions are what a covering ranking must achieve, proved by Theorem 6.8;
- a new introduction paragraph, "Dominance is proved, not assumed";
- the description of LDG is updated to the new order.

**Page counts:** LDG 23 pages; application 26 pages. Both compile cleanly.
