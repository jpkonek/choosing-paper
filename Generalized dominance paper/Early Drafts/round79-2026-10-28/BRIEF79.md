# Round 79 brief: do the rankings of the cited papers satisfy LDG's current conditions?

Folder: /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r79/. Write ONLY there.

**Our paper.** ldg_full.tex is the current full LDG, "Coherence and Dominance under General Rankings". Read these parts:
- §2: definitions (def:rankings, def:dominance, def:loss, def:bayes, def:coherence-property, def:tie-closure, def:family-assumptions);
- §3: Bayes choices with lower semicontinuous losses (thm:bayes-finite, thm:bayes-infinite, cor:bayes-coherent);
- §4: the general theorems (thm:finite, cor:closed-choice, thm:local, cor:coherent-assigned);
- §5: margins and strict dominance (thm:margin, prop:strict);
- §6.1: the dominance argument. This contains the assumption list def:argument-assumptions, which is (E), (A), (S), (T), and thm:argument;
- §8: applications (prop:proper, thm:nielsen, prop:blocks, prop:joyce).

**"Our conditions"** means the hypotheses of the dominance argument, thm:argument. They are:
- **(E)** evaluability;
- **(A)** coherent admissibility;
- **(S)** selection: for each ranking, there are assigned models that are undominated coherent models and satisfy the hypotheses of thm:finite, cor:closed-choice or thm:local. For loss rankings, the Bayes-choice and lower-semicontinuity conditions of thm:bayes-finite and thm:bayes-infinite are sufficient routes; say which you use;
- **(T)** closure under ties.

Use the exact statements in ldg_full.tex.

**Context.** The author wants to verify, for each cited paper, that the rankings that paper uses satisfy our conditions. Some papers prove more than we do, for example uniform or strict dominance; note that, but the question is whether our conditions hold. If a condition fails, say so plainly, with a counterexample or the precise reason, and say whether a nearby variant holds. Examples: (T) may fail for merely proper scores, and one may then use transitivity (prop:profiles) instead. Being too general does not count as satisfaction: if the paper allows a class of losses, check the whole class it allows, and identify any subclass for which our conditions fail.

**For your paper, produce:**
1. **The paper's setting, precisely.** Models (credence functions, forecasts, and so on), worlds, the coherent class, the family of losses or rankings it allows with their exact assumptions, and its main theorem(s) with exact numbers and statements. Quote briefly; at most one short quote per item.
2. **The translation into LDG.** Give M, Ω, C, the family 𝔏 and each M_L.
3. **Each condition (E), (A), (S), (T): HOLDS / FAILS / HOLDS UNDER EXTRA ASSUMPTION.** Give a proof, or a precise counterexample. For (S), name the route and verify every hypothesis: Bayes choice, competitiveness on supp p, closed comparison sets or lower semicontinuity, and compact family and linked finite sets for infinite Ω.
4. **What the paper proves beyond our conclusion**, such as uniform or strict dominance, or dominance by coherent models. Say whether LDG's §5 recovers it.
5. **Whether LDG §8's current treatment of this paper is still accurate** under the current axioms. That section was written under much stronger axioms. List the exact sentences that need changing, with replacement text.

**Rules.** Labels: PROVED / CHECKED / CONJECTURE / UNCLEAR / FAILS. Plain English; be rigorous; no flattery.

**Output.** <TAG>_report.md, results first.

**Final message.** Under 250 words: the verdict per condition, plus anything the author must know.
