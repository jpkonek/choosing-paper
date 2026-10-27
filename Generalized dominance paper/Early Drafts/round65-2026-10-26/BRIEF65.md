# Brief 65: the geometric condition (H), (Add) as a separate question, and completing the covering paper (26 Oct 2026)

Labels: PROVED / CHECKED (exact computation) / CONJECTURE / NUMERICS. Plain English. Write only in this folder (`r65/`). Name every hypothesis where it is used. No names on theorem-like environments in LaTeX; use \coloneqq.

## Binding inputs
- `AUDIT_r65_brief.md` and `AUDIT_r65_message.md`. These are the author's decisions via the auditor, and they are BINDING. Read both in full.
  - Comparison-deleted Brier Δ(𝒩) is admissible under the agreed axioms.
  - (H) is the main mathematical task.
  - Do not add (Add) to exclude the construction.
  - Do not reopen (S), demand complete world orders, or impose transitivity.
- `AUDIT_r64_decisions.md`: the binding framework (reflexive relations with (TC); strict (G); (IB); global coherence; direct (C); target undominated; incoherent-model dominance; (LF)).
- Core sources:
  - `ES64_notes.md`: §3 has the setting, Definition 3.1 and Theorem 3.2; §5 has (H), Lemmas 5.1–5.3 and Props 5.4–5.6.
  - `REF64_es_notes.md`: the referee's report. It proves (★) ⟺ (H) in both directions. It proves the new cases R1 (small holes inside a Bayes act) and R2 (small bumps outside one), kept away from the act's boundary. It gives the exact reformulation of Brier dominance (§3.2) and the centroid calculation. It repairs Prop 5.6 for collar pieces near face midpoints (§3.4). It defines (Add) (§5).
  - `OR64_notes.md` and `REF64_or_notes.md`: Lemma T, Lemma OC, the diagnostic 𝒯, and M1.
  - `ROUND64_report.md`.
- Paper: `Covering coherent sets of desirable gambles (draft).tex` and `.pdf`; `W64_changes.md`; `REF64_paper_notes.md`; `REF64_bx_notes.md`. Exclusion sources: `O61_notes.md`, `E61_notes.md`, `R15_notes.md`, `A62_notes.md`, `C62_notes.md`, `REF62_corner_notes.md`, `DC63_notes.md`, `IN63_notes.md`, `REF63_neg_notes.md`, `REF62_fd_notes.md`, `P61_notes.md`, `PC64_notes.md`, `REF64_pc_notes.md`.
- Scripts from round 64: `es64py/`, `ref64es_py/`.

## The setting of (H) (as in ES64 §3, §5)
- n worlds; the main case is n = 3, and statements for general n are welcome.
- μ is a finite measure with a positive density and a finite first moment. The density e^{−|h|₁} gives exact rational cone moments.
- U = D_{K'}, with K' compact convex and contained in relint Δ. U is one-sided, U ⊇ int ℝⁿ₊, and U ∩ (−ℝⁿ₊) = ∅.
- Models: measurable X ⊆ U, mod null sets. Coherent models: D_Q a.e., with K' ⊆ Q.
- m(X) := ∫_X h dμ. Bayes acts: N_π = U ∩ {π·h > 0}.
- hull(B) := D_{Q_B}, with Q_B := {q ∈ Δ : q·h ≥ 0 for a.e. h ∈ B}.
- **(H):** every incoherent X has a coherent N with:
  - m(N) ≥ m(X) coordinatewise;
  - m(N) ≠ m(X);
  - μ((N∖X) ∩ hull(X∖N)) > 0.

## Roles

### WT65 — check the auditor's two tools first (short, foundational)
1. **The density-point witness.** Let A = N∖X and B = X∖N. Then μ(A ∩ hull(B)) > 0 iff there are:
   - a density-one point a of A;
   - density-one points b_1, …, b_r of B, with 0 ≤ r ≤ n;
   - coefficients λ_j ≥ 0;

   such that a − Σλ_j b_j ∈ int ℝⁿ₊.

   The auditor's proof sketch is in `AUDIT_r65_brief.md`. Check both directions against the a.e. conventions. Check especially:
   - "every q ∈ Q_B is non-negative on each density point b_j";
   - the uniformity of the margin η over q;
   - hull(B) = int C with C = cl cone(B_d ∪ ℝⁿ₊) when B_d is not closed;
   - the Carathéodory step, including that "absorbing the nonnegative generators" keeps the strict positivity;
   - the case r = 0;
   - whether n generators suffice, or n + 1 are needed.
2. **The compactness tool.** Fix K'. The family {compact convex Q : K' ⊆ Q ⊆ Δ} is compact in the Hausdorff distance. The map Q ↦ m(D_Q) is continuous. So the coherent defenders whose moment improvement is at least δ in every coordinate form a compact set.

   Check:
   - the null-zero-set argument P_Q(h + t𝟙) = P_Q(h) + t;
   - dominated convergence;
   - whether the defenders must range over Q ⊇ K' or over all Q;
   - that D_Q is identified a.e. with the model.

   Also state precisely the failure of continuity of Q ↦ hull-overlap that the auditor warns about, with an explicit example.

Write `WT65_notes.md`. Its verdicts are used by H65 and X65, so be quick and precise. Two hours is a sensible budget.

### H65 — prove (H): a dominator and its hull witness jointly (main task)
Aim: for an arbitrary incoherent measurable X, produce a coherent N (any D_Q with K' ⊆ Q) and a density-point witness, such that the moment inequalities hold for the same N.
- Start from Lemma 5.1's strict Bayes dominator N₀. It has a positive margin in every coordinate.
- Explore coherent modifications of N₀ that spend this margin to create the witness. The auditor's L¹ bound is a search aid only.
- Use general D_Q, not only Bayes half-spaces, rescalings, a fixed facet count, or one chosen deformation. If a procedure fails, identify which optional restriction caused the failure.
- Reductions you may prove and use:
  - If μ(int ℝⁿ₊ ∖ X) > 0, then (H) holds (ES64 Prop 5.4). So you may assume X ⊇ int ℝⁿ₊ a.e.
  - R1 and R2 from REF64_es.
  - Use structure such as: X ⊆ hull(X); the cases X ⊆ some Bayes act or X ⊇ some Bayes act; Pareto-maximal moments.
- Success criteria, in order:
  - (A) a theorem proving (H) in full;
  - (B) a proof for an explicitly substantial new class, with the obstruction to the remaining class stated exactly;
  - (C) an exact reduction of (H) to a sharper geometric statement, proved equivalent.

  Do not present a sequence of sufficient conditions as progress on the general statement.
- The WT65 tools are available as "auditor lemma, under check" until WT65 reports. Note any place where your proof depends on them.

Write `H65_notes.md`.

### X65 — attack (H) globally (adversary)
Aim: an explicit incoherent X and a proof that NO coherent N satisfying the moment inequalities has μ((N∖X) ∩ hull(X∖N)) > 0.
- Concentrate on rivals in which the added regions surround the hull of the removed regions without meeting it. See the centroid calculation in REF64_es.
- A counterexample must defeat every eligible defender D_Q. The compactness tool (WT65) may help: the eligible defenders with a fixed margin form a compact set, but the margin may need to go to zero.
- Failure of a sampled search is not a counterexample.
- **If you find a counterexample:**
  - Determine the fallback: which coherent models must be left unprotected for deletion to dominate X? Is there a smaller family 𝒩 containing a given target, e.g. the reversed triangle's D_K, for which (★) can still hold?
  - Do not conclude that the original coverage objective fails.
- **If you find no counterexample:** state the strongest necessary structure any counterexample must have, and any proved obstruction to building one (e.g. "every X with property P satisfies (H)").

Write `X65_notes.md`.

### AD65 — (Add) as a separate normative question (secondary)
- Give the best decision-theoretic case for and against disjoint additivity (Add): if X ⪯_i Y and Y ⪯_i Z, with (X△Y) ∩ (Y△Z) = ∅, then X ⪯_i Z.
- Distinguish (Add) precisely from:
  - (IB);
  - (TC);
  - finite-chain consistency;
  - transitivity;
  - (TP).

  Give exact implications and non-implications with small explicit relational examples.
- State what accuracy-based considerations do and do not support it. Cover the case of deliberate incomparability: a world that is undecided about a combined change but decided about each part.
- Optionally, in a clearly labelled "strengthened-framework branch": does (G) + (IB) + (TC) + (Add) still allow free protection of every coherent model? A short answer with proof, or an exact statement of what is open.
- This is not the main effort. Do not present (Add) results as corrections to the agreed question.

Write `AD65_notes.md`.

### W65 — complete the covering paper
Produce a revised `Covering coherent sets of desirable gambles (draft).tex` and PDF in this folder, starting from the copy here.
- **§8.3, six exclusions recorded without proof.** For each, either give a complete proof in the paper (an appendix is fine) taken from its refereed source, or downgrade or remove the claim. A proof may be included only if its source is refereed CORRECT, possibly after repair, and has the same hypotheses. List each decision in `W65_changes.md`.
  - The items: convex error levels; concave charts; regular single charts; continuous piecewise-linear charts; direction-continuous piecewise-linear charts (with (C2) at u); finite unanimity.
- **Citations.** Resolve the four unverified ones: Rockafellar 6.3, 11.3 and 13.2; Schrijver §8.5. Use web search. If a number cannot be verified, replace the citation with a self-contained argument or a verified reference.
- Keep the veto–box section intact.
- Do not add the deletion construction or (H) to this paper: (H) is open.
- Conventions as before:
  - self-contained, with no commentary comparing drafts;
  - no names on theorem-like environments;
  - \coloneqq;
  - "models";
  - standard dominance nomenclature;
  - clean compile.

## Output
Each role writes `<ROLE>_notes.md` (W65: the .tex + PDF + `W65_changes.md`) with a status table, and returns a concise summary (≤ 1 page) as its final message. Put scripts in `<role>py/`. If blocked from writing a file, return the full content in the final message.
