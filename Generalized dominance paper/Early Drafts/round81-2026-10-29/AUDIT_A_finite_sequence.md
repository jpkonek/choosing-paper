**Your diagnosis is right.** The desirability paper currently proves dominance itself and then imports only LDG’s final argument from dominance to irrationality. It does not substantially use LDG’s selection theorems.

I think there is a small, mathematically useful adjustment—but it involves adding a second general dominance theorem to LDG, rather than making desirability satisfy (S). **It also appears to let us drop (A2) from the desirability dominance theorem.**

### What the desirability proof actually constructs

Reading the current proof, its geometric lemmas establish the following independently of the ranking:

> Every incoherent model can undergo at most two consolidations, followed by a non-null change guided at every world.

The cases are:

1. If the model mishandles uniformly positive or negative gambles, guidance improves it immediately.
2. If it violates upward closure, one consolidation produces a model that mishandles uniformly positive gambles.
3. Otherwise, incoherence produces a failure of closure under sums or midpoints. One consolidation produces a failure of upward closure, reducing matters to case 2.

The manuscript currently uses these constructions indirectly: it assumes the original model is undominated and repeatedly proves that consolidations preserve undominatedness. **That preservation argument uses (A2), but we can avoid it.**

### A general LDG theorem that does the work

Here is the relevant abstract result, stated using LDG’s convention that \(a\preceq_\omega b\) means \(a\) is at least as good as \(b\).

Suppose transitivity through ties holds:
\[
a\sim_\omega b,\quad c\preceq_\omega a
\quad\Longrightarrow\quad c\preceq_\omega b.
\]

Suppose there is a finite sequence
\[
x_0,x_1,\ldots,x_r,z
\]
such that each \(x_{j+1}\) weakly dominates \(x_j\), and \(z\) weakly dominates \(x_r\), strictly at some world. Then:

> **Some member of the sequence dominates \(x_0\).**

Here is the entire proof. Suppose none does. Since \(x_1\) weakly dominates \(x_0\), it must be tied with \(x_0\) at every world. Transitivity through ties then makes \(x_2\) weakly dominate \(x_0\); so it too must be tied with \(x_0\). Continuing, both \(x_r\) and \(z\) are tied with \(x_0\). But transitivity through ties then makes \(x_r\) at least as good as \(z\) at every world, contradicting the final strict comparison.

The three-model condition is not used. Nor are transitivity, compactness, scores, coherent admissibility, or the existence of undominated dominators.

Importantly, **the final model need not dominate the original model**. One of the intermediate models might do so instead. That is why this works without full transitivity.

### The resulting application

The desirability proof would then divide cleanly into two parts:

- **Desirability-specific geometry:** under (M2) and (M3), every incoherent model admits the short sequence described above.
- **General LDG result:** consolidation acceptance supplies the weak comparisons; guidance supplies the final strict comparison; transitivity through ties yields dominance of the original model.

Thus the revised dominance theorem would require **(A1), (A3), and (A4)**. The current proof suggests that **(A2) is unnecessary for this conclusion**. This should receive a focused check before changing the stated theorem, but the abstract argument above is complete.

Coherent admissibility would retain precisely its intended role: ensuring that almost coherent models are permissible under some ranking. It would not enter the proof that incoherent models are dominated.

This is not assuming the dominance conclusion under another name. The application proves the existence of particular transformations using the geometry of gambles and the measure conditions; the ranking axioms separately say how those transformations are evaluated. LDG supplies the inference from their coexistence to dominance of the original model.

### Why I would not try to recover (S) first

The present (S) requires a suitably indexed family of **undominated coherent models**, with closed comparison sets and the relevant defence properties. That supports a stronger conclusion than the desirability class theorem currently establishes: coherent, undominated dominators.

The consolidation argument supplies neither that family nor the required closedness. Adding them would therefore be a substantial extra restriction, not a small clarification. The earlier failure of veto–Brier under (S) is a particular reason not to impose them merely to make the papers fit together.

I cannot presently justify a minimal change that makes the whole desirability class satisfy the existing selection theorem.

**My recommendation is therefore:**

1. Add the short finite-sequence theorem to LDG as an alternative to selection.
2. Extract the geometric sequence lemma from the existing desirability proof.
3. Apply the LDG theorem directly, checking and then removing the unnecessary (A2) assumption.
4. Retain the selection theorems for applications where they provide the stronger conclusions.

This would make desirability a genuine application of a general LDG dominance theorem, while making its own proof shorter and its assumptions weaker. It would broaden LDG’s mathematical framework rather than force an independently successful argument back into (S).