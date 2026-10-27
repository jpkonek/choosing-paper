# Brief, round 4 (13 Oct 2026, 10:00): negligible-stakes indifference. Read BRIEF.md and BRIEF2.md first.

The author has ACCEPTED in principle a new, target-independent weakening of the guidance order, alongside the
already-accepted D_Δ exception and the Σ_T systems:

**Negligible-stakes indifference, NSI_θ (θ > 0 fixed in advance).** At world i, on a MIXED problem g (some
coordinate positive, some negative) whose world-i stake is negligible, |g_i| ≤ θ·‖g‖, good advice and silence
are tied in the guidance order at world i. Everything else is unchanged and strict: bad advice is strictly worse
than silence, contradiction worst; good is strictly better than silence when |g_i| > θ‖g‖; unanimous problems are
strict. (Norm: state your choice — sup norm or Euclidean — and whether the result depends on it.) Under NSI_θ,
(G) means: weak improvements in this coarser order are weak improvements in the ranking; strict improvements in
this coarser order (strictly better rank class on a non-null set) are strict.

Motivation (author): the evaluator may already treat silence as no worse than the right answer unconditionally
(D_Δ) or conditional on an event (Σ_T); NSI_θ extends this to a pre-specified stake threshold. Why it may help:
every triangle no-go so far (R10a Thm R ray lemma; R10b Thm PL no plateau; R15 Thm 6.2 corner calculus + box)
hinges on target-boundary gambles whose payoff at some world crosses zero (coordinate crossings), where strict
guidance forces positive reward rates; and on vertex models being forced (by the axioms) to give the best advice in the advice range,
problem by problem (R10a Thm V, R10b Prop V / Lemma FS). Under NSI_θ the vertex model at e_b may stay silent on
problems with |g_b| ≤ θ‖g‖, i.e. exactly near the crossings of coordinate b.

The author says everything turns on: (1) whether NSI_θ actually delivers coverage (start with T1 and interior
triangles in three worlds; then every coherent target in three worlds; then n ≥ 4), and (2) how close to zero the
threshold θ can be made — ideally: for EVERY θ > 0, every coherent target is covered under NSI_θ; otherwise find
the dependence of the needed θ on the target.

All other rules stand: decomposable domains (SC + closed in measure), (IB), (LA), (S), (C), (E), (LF) at the target, no
cheap realisation, nothing that makes (G) or (IB) vacuous. The CCIBU closed-choice theorem (CCIBU.tex) used strict
guidance at vertex supports/indices (R14 notes this); under NSI_θ vertex Bayes models can tie on band problems,
so its vertex step must be re-proved (e.g. by a lexicographic tie-break as in its edge case).
