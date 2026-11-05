# Round 83: an overview of the attempts so far, and lessons for moving forward (29 Oct 2026)

**Basis.** Five readers each reviewed one period of the project: 25 Sep–8 Oct, 9–12 Oct, 12–19 Oct, 19–26 Oct and 26–29 Oct. Their reports are LESSONS_H1 to LESSONS_H5. Between them they covered every project note, the auditor's assessments, the current application Short paper and the auditor's latest handoff.

The readers could not use the Projects tool. They read the device originals or local copies instead.

Most cited results were refereed at the time. Claims a reader proved for the first time in this round are marked *(new, unrefereed)*.

---

## 1. What is settled

**Abstract results (LDG).**
- **The KKM selection theorem and the dominance argument.** Under (E), (A), (S) and (T), the permissible models are exactly the coherent ones.
- **The weaker selection package W1–W3 (Theorem W).** It uses one common assignment, closed witnessing sets for incoherent rivals only, and excludes ties only at the intersection point.
- **The finite-sequence theorem.** If a chain of weak improvements ends in a strict one, some member of the chain dominates the start. The only hypothesis needed is that models tied at every world have the same dominators.
- **The literature check.** The published dominance results were sorted under these conditions. The failures sit exactly at (S) and (T).

**Dominance in the application.** These hold for any set of worlds, on the full domain, without (S).
- **The consolidation theorem.** (A1), (A4) and tie-substitution give: every incoherent model is dominated, under every ranking that satisfies them. The proof uses no score.
- **The integral ranking R0** satisfies:
  - world-by-world guidance;
  - independence: its verdict depends only on what is added and what is removed;
  - the full domain;
  - (A1)–(A4);
  - and it leaves every almost coherent model undominated, within a single ranking.

  So R0 meets every constraint the auditor now insists on, **except LDG's selection mechanism**: neither (S) nor W holds.
- **The repair theorem.** Under R0, every incoherent model is uniformly dominated by an undominated coherent model.

So the open problem is narrow. It is not "is every incoherent model dominated?"; that is proved. It is: **can the application be made to verify LDG's prior-indexed selection mechanism** while keeping full domain, independence and world-by-world guidance, with every coherent model admissible under some ranking?

---

## 2. Why that problem has been so hard

The obstructions recur across all five periods.

1. **Rules that test the whole model break independence.**
   - 9 Oct (v3, Prop. 1): the 8 Oct cover and benchmark recipe fails independence.
   - Round 82 repeated this failure with a different family.
   - Any verdict that depends on a global property of the two models can be switched by adding shared advice. Examples are "is there a benchmark covering X?" and "which regime applies?".
2. **Complete rankings reduce to additive ones, and additive rankings reach very little.**
   - Under the auditor's independence, each world's ranking compares error sets as a comparative probability. With completeness and enough continuity it becomes (almost) additive.
   - The models an additive score leaves undominated are exactly its Bayes sets {p·ψ > 0}.
   - **Concave scores** reach only rescaled normalised boxes (proved 5 Oct, and again in the Hurwicz note and round 61). The auditor's box baseline is this case.
   - **Triangles** such as ε-contamination are excluded by the corner equation (Theorem gm, three independent proofs). The cause is "half-plane charts": for each gamble, the set of priors whose Bayes set accepts it must be a half-plane.
   - **The vacuous model.** Complete rankings with strict guidance, independence and closed-section (S) leave it dominated for every n ≥ 3 (11 Oct). That proof used independence on whole binary problems. The auditor's version is stronger, so the result should carry over; this still needs an explicit check.
   - So any construction that covers the vacuous model or a triangle must be **incomplete**.
3. **Assigned models are pushed onto the Bayes family.**
   - Prop C (round 81): if a ranking agrees with a score against incoherent rivals and satisfies (S), every undominated coherent model is tied with a precise one.
   - H5 extends this to W *(new, unrefereed)*: under such a ranking, every incoherent model needs a precise dominator.
   - Assigning an imprecise target, or its rescaled family, is therefore exactly what the obstructions attack.
4. **Selection, not independence, was the binding constraint in rounds 37–60.** Every non-selection axiom could be met locally. Every failure came at the closed witnessing sets:
   - vetoes cannot be paid;
   - the jump;
   - the kink;
   - the two-envelope squeeze;
   - all-or-nothing sections under rescaling invariance (Theorem E).
5. **Additive collapse.** Committees, intersections, majorities, convex cones and anchored scores of additive judges all reduce to a single additive score, so they inherit item 2.
6. **Protection costs little; defence is the content.** Keeping one target undominated is easy (rounds 43–46 and 64). The hard part is that the same assigned models must defend against every rival.
7. **Independence ties protection to defence.**
   - For a given change, independence makes one verdict apply in every context.
   - Protecting the target needs that verdict refused at some world. Defending needs it accepted at some world in supp p.
   - R0 refuses too much: it refuses every non-guided change that a coherent model could make, and that kills W (two-world counterexample).
8. **Easy successes that were later ruled out.** Each of these met the abstract tests but was later excluded:
   - restricted domains;
   - distance to the target;
   - all-world guidance in place of world-by-world guidance;
   - stipulated coherent ties (R\*);
   - write-in losses;
   - an imposed loss profile 1 − p_i.

   Many weeks went into constructions that these exclusions later rejected.

---

## 3. Lessons

1. **Keep the two questions apart.** The dominance of incoherent models in the application is proved robustly by the consolidation route. LDG's selection mechanism is a *sufficient* condition, and verifying it in the application is a separate, much harder goal.
   - Round 81 found that the natural bridge between the two papers is the finite-sequence theorem, not (S).
   - Whether the application must also verify the prior-indexed mechanism is a decision for you. Everything below assumes it must.
2. **Do not assign the target.** The evidence is now consistent across 80 rounds.
   - Assigned models that work come from unique Bayes optima: precise models, or boxes.
   - Assigning imprecise targets or their rescaled families is what fails, whether through half-plane charts, Theorem E, Prop C, or whole-model covers.
   - Theorem W does not require the target to be assigned, and that is its main value here.
   - The rescaled family may still describe *which* coherent models a ranking protects. It should not be the assignment.
3. **Build the ranking one change at a time.**
   - Under independence, a ranking is exactly a rule saying, for each change (gambles added, gambles removed), at which worlds the change is accepted.
   - Writing the rule in that form makes independence automatic and world-by-world guidance easy to check.
   - Every construction that started from whole models had to be repaired afterwards, and the repairs failed.
4. **Incompleteness is necessary, so place it as sparsely as possible.**
   - Complete rankings are essentially additive and reach only boxes (§2.2). Incompleteness is required.
   - It should be used only to protect the target.
   - Round 71's maximal rankings show the shape: take the strictly guided integral ranking, and refuse each change that would let a coherent model be dominated, at **one** non-guided world only.
5. **The crux is a single lemma about where to refuse.** With precise Bayes models D_p as the assignment, competitiveness holds point by point:
   - D_p is p-Bayes, so the change from an incoherent x to D_p improves the expected score under p;
   - if the change is refused, it is refused at only one world;
   - at a vertex the change is guided, hence accepted.

   What remains is to choose the refusal world, as a function of the change alone, so that the strict-defence sets are open, or at least contain closed witnessing sets that cover supports. Then the auditor's open-strict-defence lemma gives W.

   Rounds 38–60 show this is where constructions die. But those rounds assigned imprecise models. This version assigns precise ones, and refuses only the changes that threaten the target.
6. **Check consistency with deletion lemmas, not by hand.** Two earlier lemmas preserve the required consistency conditions when acceptances are removed:
   - deleting a comparison together with its reverse (round 39);
   - deleting comparisons from a complete score order, symmetrically at ties (round 64).
7. **Use a fixed acceptance checklist before any construction.** It should cover:
   - world-by-world guidance;
   - independence for arbitrary contexts, including contradictions;
   - the full domain;
   - a coherent undominated class that is derived, not assumed;
   - one assignment common to all rivals;
   - no target written into the domain or the loss profile.

   Add one cheap first test: does every incoherent model near the target have a precise dominator?
8. **The box construction.** It is useful only as a consistency proof that all the constraints can be met together. It is also the limit of the complete additive class.
   - It should not be extended by tuning weights.
   - One reader shows that in two worlds, scores whose weights depend on the other world's payoff cover every interval, including the vacuous one *(new, unrefereed)*. The same reader's three-world test suggests this does not extend.
   - Agreed with you: it is of little use for the main problem.

---

## 4. Recommended next round

**Main task.** Give one target-relative ranking L_M per credal set M:
- **Base:** the strictly guided integral ranking, or Brier: accept a change at i iff it weakly raises the world-i score.
- **Protection:** refuse each change that D_M could make (its removed gambles lie in D_M, its added ones outside) and that would weakly improve every world, at one non-guided world j(change). The refusal world is chosen by a rule that depends only on the change, e.g. the world with the smallest normalised improvement, with a tie-break to be designed.
- **Assignment:** b_p ≔ D_p, the precise Bayes models of the base score. They are not the target.
- **Goal:** prove W1–W3 for every incoherent rival through open strict defences. Then prove:
  - world-by-world guidance;
  - independence;
  - the three-model condition and tie-substitution;
  - that D_M is undominated.

  Also derive C_L.

**Variant.** Protect every coherent model at once, which is round 71's maximal ranking. If it works, no target-relative choice is needed.

**Side checks (one agent each, bounded):**
- **(a)** whether the 11 Oct theorem "complete rankings cannot cover the vacuous model" carries over to the auditor's independence;
- **(b)** whether the target-relative ranking also satisfies consolidation (A4), so that both routes apply to the same rankings.

**What would count as success:** for one imprecise target outside the box class, e.g. the symmetric contamination triangle, a full-domain ranking with world-by-world guidance, independence and W.

**What would count as informative failure:** a proof that no choice of refusal world gives closed witnessing sets. That would show the prior-indexed mechanism needs a different assignment (finitely or countably many index sets, or a compact parameter space as in LDG's local theorem), not more incompleteness.

---

## 5. Corrections to the readers' reports

- H3 links round 82's independence failure to additivity. That is wrong. Round 82's loss is not additive. It fails independence because it tests whole-model covers, as v3 Prop. 1 had already shown on 9 Oct.
- Reader claims marked *(new, unrefereed)* need checking before use:
  - the extension of Prop C to W;
  - two-world full coverage by scores with weights depending on the other world's payoff;
  - the conjecture that complete additive rankings reach only near-box targets for n ≥ 3.
