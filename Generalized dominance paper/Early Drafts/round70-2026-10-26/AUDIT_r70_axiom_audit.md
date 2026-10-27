The collaborator should undertake an **axiom audit of both papers before further revision**. The aim is to distinguish assumptions on rankings, mathematical background assumptions, sufficient conditions used in particular proofs, and conclusions. These must not appear together as one list of “conditions.”

Send the following guidance.

---

**Prepare a complete inventory for each paper, checked against the actual theorem statements. Do not introduce new axioms.**

For every item, give:

- its exact mathematical statement;
- a plain-English explanation;
- its scope: one world, one ranking, a family of rankings, or the underlying model space;
- whether it is **assumed, constructed, or proved**;
- which theorems require it.

Use descriptive names. Symbols can accompany them, but readers should not need the old labels.

### 1. LDG: separate four groups

**A. General framework and substantive assumptions**

List explicitly:

1. **Evaluability:** every model is evaluated by at least one ranking in the family.
2. **Coherent admissibility:** every coherent model is undominated under at least one ranking in the family.
3. **Closure under all-world ties:** state the exact requirement concerning a model tied at every world with an undominated coherent model.

Explain that coherent admissibility is an assumption across the family. It does **not** require every coherent model to be undominated under every ranking.

Also distinguish definitions from assumptions: the coherent class is specified independently; “the undominated coherent models of a ranking” names a subclass and does not assert that every undominated model is coherent.

**B. Ordering properties**

State which results assume any of:

- reflexivity;
- completeness;
- transitivity;
- the three-model no-reversal condition;
- finite-chain consistency.

If a property is not assumed in the general theorem, say so. Do not import properties of numerical loss rankings into the general relational results.

**C. Alternative sufficient hypotheses for proving dominance**

State each package separately:

- **The original closed-selection condition (S):** an assigned undominated coherent model for each index, support-wise defence against every rival, and closed fixed-rival comparison sets.
- **Its genuine finite-world weakening:** closed subsets of those comparison sets suffice, provided they retain the support-wise guarantee. One assigned model must serve all rivals at a given index.
- **The local infinite-world conditions:** write out exactly how the finite-world guarantees are linked through one compact family.
- **The loss-based conditions:** the precise Bayes-choice and lower-semicontinuity assumptions, including the support relation between the indexing probability and the probability under which the assigned model is Bayes.

These are **alternative sufficient hypotheses**, not cumulative axioms governing every permissible ranking.

**D. Conclusions**

Keep these out of the axiom list:

- every model has an undominated coherent weak dominator;
- every incoherent model has an undominated coherent dominator;
- every undominated model is coherent;
- permissible models are exactly the coherent models.

Show exactly which assumptions yield each conclusion. In particular, do not use “the dominance conclusion” as a substitute for the hypotheses intended to prove it.

The construction proposition should have its own short list of premises. It supplies another method of obtaining dominance; it need not satisfy the selection hypotheses.

### 2. Desirability application: separate five groups

**A. Mathematical setting**

List the assumptions on:

- the set of worlds;
- the norm-closed, separable space of bounded gambles;
- constants or the specified order unit;
- measurable models and identification up to null sets;
- the measure’s finite first moment;
- null indifference boundaries;
- full support.

For each measure condition, state what it does. In particular, distinguish assumptions needed for repair and dominance from full support’s role in distinguishing credal sets.

Define coherence separately from all these assumptions.

**B. Requirements on a covering ranking**

Reproduce the paper’s exact definition of coverage, separating:

1. strict guidance;
2. independence;
3. the adopted finite-chain consistency requirement;
4. global coherence of undominated models;
5. closure under all-world ties;
6. undominatedness of the target;
7. domination of every incoherent model by an undominated coherent model;
8. local freedom of the evaluation domain.

**Crucially:** items in the definition of coverage are requirements the construction must **prove**, not assumptions the construction may invoke. Mark that distinction conspicuously.

Explain which requirements concern the ranking alone and which concern its domain or target.

**C. The construction’s additional commitments**

State the defining rule and its exact characterisation:

- guidance comparisons are accepted;
- accepted comparisons between distinct models strictly improve integrated payoff;
- a change available to a coherent model is accepted only through guidance;
- the relation is maximal subject to those requirements.

Explain that these characterise this construction, not all covering rankings.

Flag the third condition as stronger than coherent admissibility. Record that issue without trying to resolve it in this revision.

**D. Properties proved about the construction**

List separately:

- reflexivity;
- strict guidance;
- independence;
- finite-chain consistency and hence the three-model condition;
- disjoint additivity;
- absence of ties between distinct models;
- protection of all coherent models;
- coherent domination of every incoherent model.

State that completeness and transitivity are not generally satisfied. Absence of distinct-model ties and disjoint additivity must not silently become requirements on every covering ranking.

**E. The structured example**

Give the veto–Brier example its own assumptions. Explain which stronger ordering properties it has and which properties of the universal construction it lacks. Its additional hypotheses must not leak into the main theorem.

### 3. Required output before rewriting

Produce two short, reader-facing axiom inventories and an internal theorem-by-theorem dependency table. Then revise the manuscripts accordingly.

The decisive checks are:

- **Does any proof assume a dominance claim it is meant to establish?**
- **Does any construction-specific restriction masquerade as a general accuracy axiom?**
- **Does any sufficient proof condition masquerade as a necessary requirement?**
- **Are admissibility under some ranking and admissibility under every ranking kept distinct?**

This audit should restore the intended argument: independently stated assumptions first, dominance proved from them, and philosophical conclusions afterwards.