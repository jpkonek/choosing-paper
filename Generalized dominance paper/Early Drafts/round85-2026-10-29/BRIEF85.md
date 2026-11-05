# Round 85 brief: refereeing the audit's countable-selection construction

Folder (write ONLY here): /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r85/

## Inputs (same folder)
- **AUDIT_countable.md**: the note being refereed, "Countable selections – theorem and full-domain construction". It supersedes §§6–8 of AUDIT_newranking.md.
- **AUDIT_newranking.md**: the earlier version.
- **AUDIT_obstruction83.md**: the copy lemma, and the two-world pair (T, X).
- **AUDIT_handoff.md**: the binding constraints (world-by-world guidance, independence on arbitrary sets, the full domain), and Theorem W.
- **appshort.tex**: the application's definitions, the measure conditions, and the hull and trimming lemmas.
- **app_long.tex**: the long version. It contains the repair theorem and its hull, trimming and minimax lemmas, which AUDIT_countable.md calls "the existing hull and trimming lemmas".
- **ldgshort.tex**: LDG's definitions and its theorems thm:finite, cor:closed-choice and thm:local.
- **Background:** ../r84/ROUND84_summary.md, ../r84/C1_report.md and ../r84/C2_report.md.

## The author's standing instruction (binding, 29 Oct)
"Stop using the integral score. That is essentially a strictly proper scoring rule, unsuitable for the sort of rankings we're looking for, which are meant explicitly to render imprecise models non-dominated."

The audit's ranking (AUDIT_countable.md §5) accepts only comparisons that strictly raise the payoff integral m(·)(ω). It is therefore a subrelation of the integral-score ranking. Referees R85a and R85b must check the mathematics as written, and **flag this conflict plainly**. Agent R85c tests whether the construction survives without that score.

## Tasks

### R85a: the abstract theorems and the logical comparisons
1. Check the finite countable-selection theorem (§2) and the compact arbitrary-world version (§3), including every quantifier. In particular, the maps θ^j_F and the parameter spaces must be fixed independently of the rival.
2. Check the logical relations:
   - W implies the countable condition.
   - The countable condition implies dominance.
   - Dominance does not imply the countable condition (the uncountable-pairs example).
   - The countable condition does not imply W (§9's argument, which relies on the round-83 obstruction and a separation argument).
3. **Assess the substance (important).**
   - In the application the model space is separable. The collection is countable because each incoherent model has a neighbourhood on which one assignment works. Is the countable condition then equivalent to *local uniformity*: one assignment per open neighbourhood, plus second countability?
   - If so, how much weaker is it than "every incoherent model has a dominator that works uniformly on a neighbourhood of it"? Is that closer to the rival-dependent assignment the audit rejected than the note suggests?
   - Give a precise statement of what the condition adds beyond dominance in topological settings, with an example or a theorem.
   - State exactly what would change in LDG's (S), its dominance argument and its tie assumptions if the condition were adopted.

Output: **R85a_report.md**.

### R85b: the application construction
Check, line by line:
1. **The ranking (§5).** Check:
   - independence (the verdict depends only on the change);
   - world-by-world guidance;
   - the three-model condition, finite-chain consistency, and the absence of ties between distinct models;
   - protection of every almost coherent model, including the pure-removal case and the infinite-world state space.
2. **§6, the consistent incoherent case.** Check:
   - δ > 0;
   - the buffer Q_ε;
   - that the trimming lemma applies, giving Q_{X∖G_ε} = Q;
   - the robust hull inclusion H(Y∖G_ε) ⊇ G_ε for ρ(X,Y) < a/2;
   - the uniform score gap q(m(b_q) − m(Y)) > δ/2;
   - acceptance of every comparison from b_q to Y that strictly raises the score;
   - closedness of K_ω(Y);
   - support coverage on Δ_F;
   - the use of KKM and compactness.

   Pay particular attention to whether "Y∖G_ε ⊆ Y∖b_q, so hull monotonicity gives b_q∖Y ⊆ G_ε ⊆ H(Y∖b_q)" is right: what H is monotone in, and in which direction.
3. **§7, the inconsistent case.** Check the directional derivative at q₀, the bound m_L(ω) ≤ q₀(m_L), and the neighbourhood bound.
4. **§8, countability.** Check that the model space under ρ is separable, given the completion and the identification of models modulo null sets, and that a countable subcover exists.
5. **Infinite worlds.** Check:
   - weak-* metrizability of S;
   - dominated convergence for continuity in q;
   - that the compact theorem's hypotheses hold with Θ = S and θ_F(p) = Σ p_ω δ_ω.

Run numerical spot checks in two and three worlds with Gaussian μ where possible, for example on the audit's pair (T, X) and on a perturbed contamination target. These are for exploration only.

Output: **R85b_report.md**.

### R85c: can the construction be done without the integral score?
Replace m(·)(ω) by a commission-averse sign-respecting score s_ω(X) = ∫_X ψ_ω dμ that is not strictly proper. Start with the box integrand ψ_ω = l g_ω⁺ − u g_ω⁻, u > l, whose Bayes sets are rescaled boxes. Then try other non-additive or lexicographic variants.

Determine:
- **(a) Protection.** Which coherent models does the analogue of §5's ranking protect?
  - Note that removing mixed gambles from a coherent model can raise a commission-averse score at every world, so one ranking may no longer protect all of them.
  - If not all are protected, consider one ranking per target.
- **(b) Selection.** Does the analogue of the §6–§7 neighbourhood selection go through?
  - The b_q would now be ψ-Bayes or ψ-hull models.
  - What plays the role of the expected-choice gap δ?
- **(c) Coverage.** Which targets are covered: boxes only, or more?
  - Can the hull clause A ⊆ H(B), which is a non-additive and coherence-sensitive ingredient, reach beyond the Bayes sets of ψ?
  - Test the contamination triangle.
- **(d) The hull clause.** It refers to the coherent hull. Is the ranking then "built from coherence"? State whether the hull clause can be expressed without mentioning coherence, e.g. as a conic-hull or positive-combination condition on gambles, and whether that changes anything.

Output: **R85c_report.md**, with proofs or explicit counterexamples.

## All agents
- Labels: PROVED / CHECKED / CONJECTURE / UNCLEAR / FAILS.
- Plain English. No jargon such as "certificate" or "route".
- Journal-level rigour.
- Write only in r85.
- Final message: under 250 words.
