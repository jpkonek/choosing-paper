# Round 85 summary (29 Oct 2026): the countable-selection construction, refereed, and a box-score version

Sources:
- R85a_report.md: referee of the abstract theorems.
- R85b_report.md: referee of the audit's application construction.
- R85c_report.md: the version without the integral score.
- REF85_report.md: referee of R85c.

## 1. The audit's note (AUDIT_countable.md)

**Abstract theorems: CHECKED, after two repairs.**
1. In the arbitrary-world version, the tie clause must hold at every common point. Read as "at some point", it simply asserts dominance.
2. That version must be restated in the form of LDG's thm:local.

**Logical relations: CHECKED.**
- W implies the countable condition.
- The countable condition implies dominance.
- Dominance does not imply the countable condition. The obstruction is cardinality only.
- The countable condition does not imply W.

**What the condition adds: little in the application (R85a, PROVED).**
- One fixed coherent model dominates a whole neighbourhood of each incoherent model. So constant assignments suffice, which is the rival-dependent device the handoff rejected.
- On separable model spaces where dominance is robust to small changes of the rival, the condition is equivalent to plain dominance.
- Adopting it in LDG would mean rewriting (S): LDG could no longer say that (S) does not assume dominance, and the global tie assumption would give way to a local one.

**Application construction (§§5–8): CHECKED (R85b).** It is correct, with minor repairs.
- The guaranteed neighbourhoods are tiny: radius about 10⁻⁷ for the audit's pair.
- The incoherent models form an open set.

**But it conflicts with the author's ban on the integral score.**
- The ranking is a subrelation of the payoff-integral ranking.
- The targets survive only because comparisons with precise models that beat them everywhere are refused.
- δ > 0 rests on the integral score having a unique best model at each prior.

## 2. The box-score version (R85c; refereed by REF85: no errors, three fixes)

**The ranking.** Use s_ω(X) = ∫_X ψ_ω dμ with ψ_ω = l_ω g_ω⁺ − u_ω g_ω⁻, l_ω < u_ω. Accept the change X → Y at ω iff X = Y, or both of these hold:
- s_ω strictly rises;
- either the change is guided at ω, or every added gamble follows from the removed ones (A ⊆ H(B)).

**What it does not use.** No payoff integral or Brier score appears anywhere, including in the proofs.

**Results (finitely many worlds; infinite worlds for constant boxes).**
- **Structure.** Independence on arbitrary sets, world-by-world guidance, the three-model condition, transitivity through ties, and no ties between distinct models.
- **Protection.** A coherent model is undominated iff it lies inside some Bayes set of the score.
  - For boxes, D_Q is undominated iff Q contains a rescaled box.
  - The vacuous model is always undominated.
  - The audit's interval is undominated iff ρ ≤ 3.
  - **The contamination triangle {m_i ≥ a} is undominated iff ρ ≤ (1−a)/(2a).**
- **Dominance.** Every incoherent model is dominated, through the countable-selection mechanism.
  - The dominators are Bayes sets cut down to a trimmed hull, and they are coherent and undominated.
  - The audit's inconsistent case needed a repair, which is done.
- **Coverage by the class of box hull rankings.** D_Q is covered iff Q contains a vertex, or Q is full-dimensional inside some face.

**Not covered.**
- Precise non-vertex models, and thin interior sets such as interior segments. Every continuous, strictly commission-averse hull ranking dominates them.
- In two worlds a special field closes the gap. In three or more worlds, any field that protects such a target must be commission-neutral on a whole hyperplane (REF85).

**Fixes still to make.**
- The claim "a gate built from ψ alone protects at most the Bayes family" should be relabelled CONJECTURE.
- The transfer theorem is proved only for finitely many worlds.
- Three routine steps of the infinite-world proof need writing out.
- The lexicographic variant protects exactly the same models, not fewer.

**Caveat.** The hull clause can be stated without naming coherence: an added gamble must exceed a nonnegative combination of removed gambles by a margin. But it still encodes the coherence axioms D2–D4.

## 3. Status
- **The desirability question.** Is there an independent, world-by-world guided, full-domain, commission-averse ranking under which a target outside the box class is undominated and every incoherent model is dominated? Yes. The answer is a box hull ranking. It covers every full-dimensional credal set, the vacuous model and the triangle.
- **The LDG question.** Does the application verify a substantive prior-indexed selection condition? Only weakly. W itself fails, and the countable condition is close to dominance in this setting.
- **Open.**
  - Covering precise and thin targets in three or more worlds without strictly proper scores.
  - Whether a selection condition exists that is stronger than the countable one and is still satisfied by box hull rankings.
