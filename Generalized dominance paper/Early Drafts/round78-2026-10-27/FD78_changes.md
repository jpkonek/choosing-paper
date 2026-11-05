# FD78: final fixes (RD78 required fixes 1–6, AUDIT_1547 items 1 and 3)

Outputs (r77/): short_final78.tex, full_final78.tex, handout_final78.tex.
Build: r77/FD78_build/, pdflatex x3 each. 0 errors, 0 LaTeX warnings, 0 undefined references, 0 overfull/underfull boxes.
Pages: Short 6, Full 31 (was 30), handout 5 (was 7; the drop comes from the author's 15:50 comment-outs, not from these fixes).

## RD78 required fixes (exact replacement texts)
1. "Three things are not assumed", Second point: Short and Full. Not applicable to the handout (its "Not assumed" line has no such clause and is now commented out by the author).
2. (P2) "exactly when … so no model is both (Lemma 3.2)": all three. Handout uses hard-coded (Definition 3.1), (Lemma 3.2).
3. Full §6 intro: dominance proved from selection and closure under ties; (A) used only for permissibility.
4. Full §6.1: (S) example stated in full (singleton family; (E), (A), (T) hold; no e_n weakly dominates x).
5. Full §6.1: applications verify (S) in Sections 8.1–8.4 (sec:proper–sec:conditional) and Prop. prop:countable; fails for the loss of Prop. prop:joyce.
6. Handout Figure 5: step marker 4 moved to (5.75,0.25). The figure is inside the author's comment block (lines 416–449), so the fix sits in the comment. Tested by compiling a copy with that block uncommented: no errors or overfull boxes, and the marker sits beside "C = C_L1 ∪ C_L2 ∪ C_L3".

R1–R4 (recommendations) not applied.

## AUDIT item 1: compactness remark (Full only)
- Remark rem:collapse now fixes an arbitrary set 𝒜 of models (Θ := 𝒜, cofinite topology, c_θ = θ, K_ω(m) = {d(m)}). It states: for assigned models drawn from 𝒜, the abstract compactness condition is equivalent to weak domination of every model by a member of 𝒜. In particular, the dominance property holds iff the condition holds for some family of undominated coherent assigned models (𝒜 = C_L). The audit's counterexample is added to show the condition does not give the dominance property for arbitrary assigned models. The counterexample has one world, coherent c, incoherent x, only identity comparisons, discrete Θ = {c, x} and K_ω(m) = {m}. I checked it: item 1 holds because m ⪯ m, and the finite-set condition holds with θ = m. x is undominated and has no coherent weak dominator. The Hausdorff sentence is generalized from C_L to 𝒜.
- Intro ("The general theorems weaken…"): "equivalent to it" → equivalent to weak domination by a member of the assigned family (for undominated coherent assigned models, to the dominance property).
- Scope, "Sufficient conditions": "collapse into it" → collapse into their own conclusion, weak domination by a member of the assigned family. That conclusion gives the dominance property when the assigned models are undominated coherent models, but not in general.
- Short and handout: no analogous claim (neither has the collapse remark). No change.

## AUDIT item 3: infinite worlds (Full only)
- "For infinitely many worlds there is no simplex of priors on all worlds. We work on finite sets of worlds and join them by compactness." → "For infinitely many worlds, we cannot directly apply the finite-dimensional simplex argument to all worlds at once. We instead work on finite sets of worlds and join their conclusions by compactness."
- Short and handout: no analogous sentence. No change.

## Handout integrity
`diff handout_user1550.tex handout_final78.tex` shows exactly two changed lines: 438 (figure marker, inside the comment) and 465 ((P2)). Every author comment block and % line is unchanged.

## Numbering check
The Short .aux gives Def 1.1–1.6, Lem 1.7, Lem 2.1, Thm 2.2, Cor 2.3, Thm 2.4, Cor 2.5, Def 3.1, Lem 3.2, Def 3.3, Thm 3.4 and Props 3.5–3.7. Every hard-coded number in the handout matches. "Proposition 3.3" appears only in the author's comment block and in the % notes.
