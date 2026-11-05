# Round 81: connecting the desirability results to LDG (29 Oct 2026). Research only; no manuscript changes.

Agents: FS81 (strand 1), S81 (strand 2), REF81 (referee). Verdicts below are as refereed.

## Strand 1: finite-sequence theorem, geometric lemma, (A2) dropped. All PROVED or CHECKED.

- **Finite-sequence theorem (LDG-level).** Let x₁,…,x_r each weakly dominate their predecessor, starting from x₀, and let z weakly dominate x_r, strictly at some world. Then some member of x₁,…,x_r,z dominates x₀.
  - The weakest hypothesis needed is (TD): models tied at every world have the same dominators.
  - The implications (A3) ⇒ all-world-tie substitution ⇒ weak-dominance substitution ⇒ (TD) are all strict. Each gap has a counterexample.
  - The theorem uses no transitivity and no three-model condition (A2).
- **Geometric lemma (ranking-free, under (M2) and (M3)).** Every incoherent model admits at most two consolidations, followed by a non-null change guided at every world.
  - The proof is a direct case split: (U1) handling of uniformly positive and negative gambles; (U2) upward closure; otherwise, closure under sums and midpoints.
  - Every triple is legitimate.
  - The old lem:U2 in app_long already states the needed step without reference to a ranking.
- **Revised Theorem 4.1.** Under (M2) and (M3), every ranking satisfying (A1), (A4) and (TD) dominates every incoherent model.
  - (A2) is unused, and was never needed in the old proof either.
  - (A1) and (A4) alone do not suffice; there is a two-world counterexample.
- Paper-ready LaTeX is in FS81_report.md, with one fix from REF81: lem:up-step must choose x and z.

## Strand 2: selection (S). Core results PROVED; wording corrected.

- **(S) fails for the integral ranking whenever n ≥ 2.** There are two proofs:
  1. Prop 1, using coherent rivals only. Serving forces vertex models, and closedness then fails because Δ is connected.
  2. Prop C and Theorem A.
- **Prop C, with its hypothesis stated.** In finite Ω, suppose a ranking is score-consistent against incoherent rivals and satisfies (S). Then every undominated coherent model is tied at every world with an undominated precise model D_r.
  - If the ranking is score-consistent in both directions (Theorem A), then C_L consists of precise models only.
  - The precise models enter through the integral score: in this setting, the only models unbeatable on score over their support are the Bayes models {r·h>0}.
  - LDG itself does not distinguish precise from imprecise. Without the score-consistency hypothesis the conclusion fails. REF81's counterexample: Y ⪰_ω X iff Y = D_Q, or Y = X, or X is incoherent with s_ω(X) < s_ω(Y). It satisfies (A1)–(A4), (T) and (S) with imprecise D_Q undominated, and D_Q is tied with no precise model. It is a write-in ranking.
- **Consolidation cannot supply (S).** Coherent models have no consolidations, and the obstruction lies among coherent rivals. (S) needs a selection indexed by p, while the dominators that consolidation produces depend on the rival.
- **The coherence-floor ranking R\*** satisfies (A1)–(A4), closure under ties, admissibility of every almost coherent model, and (S) for any Ω under (M1) and (M2), via thm:finite and thm:local. R\* is defined by:
  - all almost coherent models are tied at every world;
  - Y ⪰ X with X incoherent holds iff Y = X or s_ω(Y) > s_ω(X);
  - no incoherent model is ever at least as good as a coherent one.

  The coherent ties are stipulated.
- **R\*_Q (target-relative) and the pure score ranking L_lin** were CHECKED. L_lin protects only precise models.
- **Prop B** is narrower than first summarised: it covers only a vertex model tied with a coherent proper subset of itself.
- **R5 example:** D_p fails to serve only when ½ lies strictly inside Q.

## Assessment

The substantive link between the papers is strand 1, not (S). LDG can state the finite-sequence theorem as a second general dominance theorem, alongside selection. Desirability is then a genuine application of it: the geometric lemma together with (A1), (A4) and (TD).

(S) remains the route to stronger conclusions where it is natural, such as proper scores. For desirability rankings that track the integral score whenever an incoherent model is the worse one, (S) is compatible with imprecise admissibility only through stipulated ties.
