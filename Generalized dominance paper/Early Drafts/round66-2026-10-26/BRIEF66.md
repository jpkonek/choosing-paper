# Brief 66: referee the simple safe-improvement ranking and the infinite-world theorem; rewrite the universal note; two-sided domains; LDG route 3 (26 Oct 2026)

Labels: PROVED / CHECKED (exact computation) / CONJECTURE / NUMERICS. Write in plain English. Write only in this folder (`r66/`). Name every hypothesis where it is used. In LaTeX: no names on theorem-like environments; use \coloneqq; call the objects "models"; use the standard dominance nomenclature.

## Binding inputs
- `AUDIT_r66_message.md` and `AUDIT_r66_extension.md` are the author's decisions and the auditor's new proofs. The decisions are BINDING. The new proofs are audit results that are NOT yet refereed.
  - Do not introduce further axioms to recover a more familiar proof architecture.
  - Do not make "no reference to coherence" a mathematical objective in this round.
- Finite-world results (refereed):
  - `Universal coverage by comparison deletion (draft).tex/.pdf`, with its referee report `REF65_un_notes.md`;
  - `X65_notes.md`, with `REF65_hA_notes.md` (minimax Step 1′, contraction Lemma S) and `REF65_hB_notes.md`;
  - `ES64_notes.md` / `REF64_es_notes.md` (the binding framework, records, safety via "attack");
  - `WT65_notes.md` (hull formula, compactness);
  - `AD65_notes.md` / `REF65_ad_notes.md` ((Add), the lexicographic variant, the plain-Brier observation).
- `ROUND65_report.md`.
- Covering paper: `Covering coherent sets of desirable gambles (draft).tex` (§2: Lemma LF, Prop lowdim, Theorem 2.9 domain dichotomy). Also `FD62_notes.md` and `REF62_fd_notes.md` (FD-1 domain dichotomy, two-sided domains).
- LDG: `LDG_v3.2.tex` and `.pdf`, the generalized loss dominance paper.

## The simple ranking (AUDIT_r66_extension §2)
For a change from Y to X, write A = X∖Y and B = Y∖X, and let d_ω(A,B) = ∫_A h(ω) dμ − ∫_B h(ω) dμ.

The record (A,B) is **safe** if no coherent C contains B a.e. and misses A a.e. In the finite setting this is equivalent to μ(A ∩ hull(B)) > 0.

**Definition.** X ⪯_ω Y iff:
- (A,B) is guidance at ω (this includes the null record); or
- (A,B) is safe and d_ω(A,B) > 0.

## Roles

### SR66: referee the simple ranking (§2) and the abstract construction lemma (§3)
- Check every clause of the Proposition, in the finite setting of round 65:
  - reflexivity and a.e. identification;
  - strict (G);
  - (IB);
  - (TC) and finite-chain consistency;
  - (Add);
  - protection of every coherent model;
  - strict dominance of every incoherent model, via Theorem H;
  - (W), global coherence and direct (C);
  - (LF) and coverage of exactly the full-dimensional K with K′ ⊆ relint K on U = D_{K′}.
- Check:
  - the equivalence "safe ⟺ μ(A ∩ hull(B)) > 0", including the cases B null and Q_B = Δ;
  - that guidance records strictly improve their own world's score;
  - the (Add) argument when one record is guidance and the other safe;
  - that no nontrivial ties exist, so (C) holds trivially.
- Check the abstract lemma (§3) as stated, its hypotheses, and whether it needs anything unstated (measurability of records, the null record, closure of guidance under disjoint union).
- Check the auditor's correction: on the one-sided domain, every coherent evaluable model, including the lower-dimensional ones, is undominated; what fails for lower-dimensional targets is (LF).
- Write exact atom-free checks where useful (`sr66py/`).
- Output: `SR66_notes.md`.

### IW66a and IW66b: two independent referees of the infinite-world theorem (§4) and the contamination cover (§5)
Work independently; do not read each other's notes. Check every step:
- **Setting.**
  - S is weak-* compact and metrizable, because E is separable.
  - inf over S of q(h) equals inf over ω of h(ω).
  - Existence of μ with full support, finite first norm moment and null sets {P_Q = 0} for every compact Q. Check the construction g + t𝟙 and its independence. Is ν's full support enough? Is "summably weighted atoms on a dense sequence" acceptable when the boundary sets must be μ-null? The t-variable handles that, but check it.
  - Measurability of the sets D_Q and of the models.
- **Step A.**
  - Q_X is weak-* closed. Check continuity of q ↦ ∫_X max(−q(h), 0) dμ by dominated convergence on a metrizable S.
  - X ⊆ D_{Q_X} a.e.
- **Step B.**
  - Weak-* compactness of {f : 0 ≤ f ≤ 1_G} in L^∞(μ). This needs L^∞ = (L^1)*: is μ σ-finite? Yes, it is finite.
  - Weak-*-to-norm continuity of T via Bochner approximation.
  - Norm compactness and convexity of Z_G.
  - The minimax theorem used (which version; are its hypotheses met?).
  - Uniqueness of the maximiser for each q.
  - Is the saddle-point argument that the optimal relaxed choice is an indicator correct? In particular, check that z* is attained by f = 1_{N₀} for the optimal q*.
  - That m(N₀) − m(X) ≥ v𝟙 holds pointwise on Ω, i.e. as an element of E, evaluated at each ω.
  - v > 0.
- **Step C.**
  - The shrink keeps a uniform margin.
  - The sets N_τ are coherent with credal set ⊇ K′.
  - The gained set is non-null.
- **Step D.** The contraction lemma in infinite dimensions: weak-* convergence of the iteration; closedness of Q_X.
- **Step E.**
  - The countable norming set Ω₀.
  - That guidance at every world forces the change to be trivial, a.e.
  - The null set {P_S = 0}.
- **Section 2's ranking in this setting:** (TC), (Add), protection and dominance. Do the finite-world proofs transfer unchanged? Does "safe ⟺ hull test" still hold?
- **§5, contamination.**
  - The states of C(Ω) are the regular Borel probabilities.
  - The boundary computation P_K(h) = (1−ε)p(h) + ε min h.
  - The local-freedom analogue: the open set U is a neighbourhood of the boundary. State precisely which (LF) definition is being met in infinite dimensions, and whether it is the natural one.
  - D_K is undominated.
  - Hence a cover in the binding framework, transplanted to this setting.
- **Scope limits in §6.** Are they accurate? Anything missing?
- Try to break it: non-metrizable cases, E without constants, ε = 1, p without full support.
- Output: `IW66a_notes.md` / `IW66b_notes.md`, with verdict tables. Scripts in `iw66a_py/` / `iw66b_py/` if useful.

### TS66: two-sided domains (exploration with proofs)
Goal: universal coverage on two-sided domains, which would cover lower-dimensional targets. The FD-1 dichotomy reduces this essentially to the full domain (all gambles that are not sure losses, or all of ℝⁿ minus null sets; check which).
- Set up the analogue of the simple safe-improvement ranking on such a domain. State what "coherent model" means there: D_Q with arbitrary credal Q.
- Identify the rivals that the round-65 proof does not handle, e.g. Q_X = ∅ (X contains a sure-loss combination). Note: if Q_{X∖N} = ∅, then every record removing X∖N is automatically safe, since no coherent model contains X∖N.
- **Aim:** prove that every incoherent X on the full domain has a coherent N with strict Brier improvement at every world and a safe record. Otherwise find an obstruction (a counterexample X with proof).
- Then determine coverage. Which targets, including lower-dimensional and precise ones, satisfy (LF) on this domain? Is D_K undominated? Check against the known result that precise targets are covered on the full domain by plain Brier.
- Also check: is protection still free on a two-sided domain? That is, can pure guidance weakly dominate a coherent model there?
- Output: `TS66_notes.md`, scripts in `ts66py/`.

### UN66: rewrite the universal-coverage note (writer)
Produce `Universal coverage of coherent sets of desirable gambles (draft).tex` and its PDF, starting from the round-65 note.
- **Main construction:** the simple safe-improvement ranking.
  - Prove the Proposition in full: the main theorem's clauses, (Add) and finite-chain consistency.
  - Keep the comparison-deletion and lexicographic variants only as a short remark, or drop them.
- **Main proof:** relative minimax, then hull-preserving shrink.
  - Make the contraction lemma prominent, with the identity hull(X∖N) = hull(X).
  - Include the plain-English mechanism: the new advice is implied by the removed advice, so the change cannot apply to any coherent model.
- **Abstract construction lemma:** add it as a separate section.
- **Lower-dimensional statement:** correct it. Every coherent evaluable model, including the lower-dimensional ones, is undominated. What fails for lower-dimensional targets on one-sided domains is (LF), hence coverage as defined.
- **Do NOT include the infinite-world theorem yet.** It is under refereeing. Leave a clearly marked placeholder comment `% INFINITE-WORLD SECTION: pending refereeing` where it would go.
- **Scope section:** keep it factual: universality within a fixed U; coherence-informed definition; representation versus justification.
- **Conventions:** self-contained; no project-internal labels; author block Jason Konek; clean compile.
- **Output:** the .tex and PDF, plus `UN66_changes.md`.

### LDG66: route 3 in the generalized loss dominance paper (writer)
Produce `LDG_v3.3.tex` and its PDF from `LDG_v3.2.tex`.
- Add the abstract safe-improvement construction lemma, stated in LDG's abstract setting (models, worlds, relations ⪯_ω, the coherent class), as a third route beside compact certificates (route A) and admissibility through scores (route B). Name it in the hypothesis map (§3.2) and the hypothesis table.
- It is a construction theorem, not an axiom. State its hypotheses abstractly, so that it needs no topology. Prove it in full.
- Give at most one illustrative example, preferably finite and abstract. Cite the desirable-gambles application only in words, as a forthcoming companion; do not import its geometry.
- Same conventions as LDG v3.2:
  - self-contained;
  - no commentary comparing versions;
  - (W) as a stronger objective;
  - \coloneqq;
  - "models";
  - standard dominance nomenclature;
  - no names on theorem-like environments;
  - clean compile.
- Output: `LDG_v3.3.tex`, its PDF, and `LDG66_changes.md`.

## Output
Each role writes its notes with a status or verdict table and returns a concise summary of at most one page as its final message. If blocked from writing a file, return the full content in the final message.
