# Round 75 brief: application paper writer (WA75)

Write ONLY in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r75/.

**Start from** REFL75_core.tex. It is the round-74 paper with (M4), Proposition prop:advice and a symmetric existence measure already spliced in; see REFL75_report.md and REFL75_core.diff.

**Also read** AUDIT_1352.md §§1–4, and app_device.tex, the version currently on the device.

**Outputs**
- app_revised.tex and its PDF. It must compile cleanly with no undefined references.
- WA75_changes.md.

## Author's instructions (binding)

The paper stays a formal core. Do NOT add a summary of results, an introduction or a discussion; the author adds those. Add only material that defines notions explicitly and explains the axioms. Specifically:

1. **Names.** Give definitions and axioms short descriptive names, e.g. \begin{definition}[Dominance], (A4) [Consolidation]. Lemmas, theorems and propositions stay unnamed.
2. **The four advice states.** Give an explicit numbered definition. For a gamble f, a model X gives:
   - strict advice for f, when f ∈ X and −f ∉ X;
   - strict advice against f, when −f ∈ X and f ∉ X;
   - silence, when neither is in X;
   - contradictory advice, when both are in X.

   Explain briefly in plain English that f represents a binary choice (e.g. between g and h, with f = g − h). Keep REFL75's Proposition prop:advice and condition (M4), with one plain-English sentence: whether a choice opportunity is negligible should not depend on which way round it is written.
3. **What μ measures, with its assumptions.**
   - Short plain-English statement: μ measures the relative frequency or importance of advice opportunities.
   - The results hold uniformly over every μ satisfying the stated conditions. They do **not** hold for every finite Borel measure; check that no sentence says or suggests otherwise.
   - For each condition (M1), (M2), (M3), (M3′), (M4), give one plain-English sentence saying what it requires and which results use it. A table or list is fine.
4. **Plain-English explanation of consolidation (A4).** One compact paragraph or short list attached to the axiom. It must:
   - explain both forms: sums (equal masses m, m, m) and midpoints (m, m, 2m);
   - say what equal masses do and do not supply. They fix how much of each part is replaced. They do not by themselves fix how often choices from G₁ and G₂ occur together. The comparison can be made precise by grouping opportunities into matched triples whose marginals are the restricted measures; for instance, μ|G₁ ⊗ μ|G₂ ⊗ μ|G₃ / m² has total mass m and exactly those marginals. Because the payoff inequality holds for every triple, the particular grouping does not matter. The midpoint form matches two original opportunities with two replacement ones. Call this a grouping of opportunities for comparison;
   - state that consolidation applies in every context, including where adding or removing a gamble creates or resolves contradictory advice;
   - state the remaining substantive commitment plainly: payoff advantages can compensate across advice opportunities. The measure makes the quantities comparable; it does not establish that compensation.
   - Do not turn silence into a default choice.
5. **Two conclusions, clearly separated in the statements:**
   - Theorem 4.1: (A1)–(A4) give that every incoherent model is dominated;
   - Corollary 4.10: adding (A5) for 𝒦 gives that members of 𝒦 are undominated while every incoherent model is dominated.

   Check the corollary says exactly this.
6. Keep the integral ranking and the repair theorem later, unchanged except for consistency with (M4) and the symmetric existence measure.
7. **Open check from REFL75.** Does (A4) need any adjustment, or a caveat in the interpretation, when a margin-triple set G_i overlaps the reflection −G_j of another? Check mathematically. Fix the interpretation if needed; do not change the formal axiom unless necessary, and say why.

## Style
- Plain English; no jargon ("certificate", "record", "safe", "dangerous", "route", "shelter").
- Use \coloneqq; say "models"; standard dominance terms; no commentary comparing versions.

Final message: a summary under 250 words, the page count, and the answer to item 7.
