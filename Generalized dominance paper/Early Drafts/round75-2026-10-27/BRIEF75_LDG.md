# Round 75 brief: LDG writer (WL75)

Write ONLY in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r75/.

**Inputs**
- ldg_full_device.tex: the full LDG, current device version.
- ldg_short_device.tex: the author's Short manuscript, the version the auditor read.
- AUDIT_1352.md: the auditor's note, §§5–6. Follow it.
- app_device.tex: the companion application paper (Theorem \ref{thm:dominance}, Corollary \ref{cor:admissible}). Use it for cross-reference accuracy.

**Outputs**
- ldg_full_revised.tex and ldg_short_revised.tex, with their PDFs. Both must compile cleanly with no undefined references.
- WL75_changes.md: every change, with locations, for each file.

## Required changes (both files, kept consistent)

1. **Irrationality.** A model is *irrational* if, under every ranking in the family that evaluates it, some model dominates it.
   - Rational permissibility is unchanged: the model is undominated under some ranking that evaluates it.
   - With evaluability, irrational and permissible are complementary. Prove this in one line; it needs no transitivity, compactness or undominated dominators.
2. **New final family-level proposition** (elementary). Assume evaluability. If every incoherent model is dominated under every ranking that evaluates it, and every coherent model is undominated under some ranking that evaluates it, then the rationally permissible models are exactly the coherent ones.
   - State that this does not prove its dominance premise.
   - Add a one-line pointer: the companion paper's Theorem (consolidation) proves that premise for sets of desirable gambles. The KKM and compactness theorems here give other sufficient conditions.
3. **Lead the dominance-argument section with ordinary dominance** and the proposition in item 2.
   - Recast the existing stronger results (closure under ties, transitivity, undominated coherent dominators, the old Prop. permissible parts) as *additional* conclusions under their existing extra hypotheses. Do not delete them.
   - Make sure nothing suggests that every dominance argument must find an undominated coherent replacement.
4. **The KKM and compactness theorems: state the existence step for an arbitrary assigned family.**
   - Hypotheses: assigned models c_p, or c_θ, need NOT be coherent or undominated.
   - Conclusion: every evaluable model is weakly dominated by some assigned model.
   - Then derive the existing conclusions (dominance property with undominated coherent dominators, exact identification, etc.) as corollaries, adding back coherence and undominatedness of the assigned models.
   - **Keep the strictness / tie-exclusion step explicit.** Weak domination alone does not give irrationality, because the weak dominator might tie with the original. Say exactly what extra condition gives strict or ordinary dominance: e.g. the dominator is distinct and not tied, closure under ties, or the assigned models are undominated and the model is not among them.
   - Check each proof genuinely never uses coherence or undominatedness in the existence step. If it does somewhere, say so and keep the hypothesis there.
   - Do not replace C_L by an arbitrary family throughout while retaining the old conclusions.
5. **Cross-references to the companion paper** must match app_device.tex exactly: the theorem's axioms, the measure conditions (M2) and (M3′), and that it gives ordinary dominance, not undominated coherent dominators, for the general class.

## Style (author's standing rules)
- Plain English; no jargon such as "certificate", "record", "safe", "route" or "dangerous".
- Definitions may carry short descriptive names, e.g. \begin{definition}[Dominance]. Lemmas, theorems and propositions stay unnamed.
- Use \coloneqq.
- No commentary comparing versions.
- Keep each file's existing scope and length discipline. The Short version stays short.

Final message: a summary under 250 words, plus any mathematical issue found in item 4.
