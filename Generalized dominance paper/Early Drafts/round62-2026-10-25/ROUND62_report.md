# Round 62 report: signed scoring fields, the reversed triangle, and orthant-planar targets

25 October 2026. Six agents: constructor C62, adversary A62, foundations FD62, writer W62, and three referees (corner, foundations, R1/R2). Labels: PROVED (refereed once, unless stated) / CHECKED / CONJECTURE / NUMERICS. Notes are in `round62-2026-10-25/`.

## 1. Headlines
1. **A new covered class: orthant-planar targets** (REF62_fd Prop R2; refereed in REF62_R2).
   - *Condition:* K ⊆ relint Δ, and on every mixed orthant σ, D_K ∩ σ = {d_σ·h > 0} ∩ σ.
   - *Ranking:* the chart c(h) = d_{σ(h)} ⊙ h, which is discontinuous across the coordinate planes.
   - *Bayes sets:* exactly D_{ν(π⊙K)} for every π ≥ 0, including boundary priors.
   - *Domains:* the full domain, and every one-sided U = D_{K′} with K′ ⊆ relint K.
   - *n = 3 geometry:* K qualifies iff every edge line passes through a vertex of the simplex. These are R10b §7's "cevian polygons", whose coverage R10b left open.
   - *Examples:* every normalised box, including the constant-odds-ratio set (holonomy 1); a non-box hexagon; and the cyclic triangle {m₃ ≤ 2m₁, m₁ ≤ 2m₂, m₂ ≤ 2m₃}. The cyclic triangle has no strictly visible vertex, and no earlier construction reaches it.
   - *So:* sharp corners as such are not the obstruction.
2. **Boxes are covered** (FD62 Prop FD-B; refereed). The ranking is the concave chart c_j = min(l_j h_j, u_j h_j), on the full domain and on every one-sided U. It meets all four certificate conditions for every prior.
3. **Two-sided domains under global coherence** (FD62 Thm FD-1; refereed). Assume n ≥ 3, a target meeting no edge of the simplex, and strict guidance.
   - Every domain is then one-sided or the full domain (up to sure losses).
   - The auditor's counterexample to F61's domain A_K holds exactly. F61 Thm D proves only relative coherence.
   - On the full domain, regular strictly sign-correct certificate charts reach exactly the orthant-planar targets (R1 (a)–(b), refereed). R1(c) as first stated was false: continuous does not imply box. The corrected statements: continuous charts with constant scale on each orthant, including every continuous piecewise-linear chart, reach exactly the boxes.
   - So T1 and the reversed triangle are not covered by regular certificate charts on any two-sided domain.
4. **The reversed triangle on one-sided domains** (C62 Thm 4.1; refereed, with a local repair to Lemma 4.3).
   - No continuous piecewise-linear signed field, with values matching on seams, meets the certificate, for any finite conic partition and any K′.
   - *Why:* priors near u force linear crossing-row faces, and the corner system has rank 6. Fields vanishing on the faces fail at generic priors between u and each vertex (repaired form of A62-1).
   - *Independent confirmation:* within R15's regular class ((DF) + (ND)), A62 Cor 2.3 shows the corner equations have no real solution. The map x ↦ 3/2 − 1/x has no real periodic point. R15 does not use (S) (CHECKED).
   - *Limit:* a chart's Bayes sets depend only on its direction field (PROVED). So matching *values* on seams is stronger than needed, and this exclusion does not reach direction-continuous piecewise-linear fields with free positive scalars. The corner algebra with directions only has complex solutions 3/4 ± i√7/4 (CHECKED), which suggests those fail too, but the supporting lemmas are not yet redone for directions (GAP).
5. **The certificate reformulation** (lead's pairwise condition; refereed with repairs). Under sign correctness, coherence is the same as convexity up to null sets. The pairwise Farkas form c(h+k) ∈ ℝ³₊ + ℝ₊c(h) + ℝ₊c(k) is needed only for pairs some prior accepts together; the non-strict form is the correct one.
6. **Pari-mutuel triangles:** convex error levels are excluded for every interior pari-mutuel triangle with n = 3 (O61 Thm B upgraded; refereed).
7. **Draft paper** (W62): a self-contained 20-page LaTeX note on the one-sided veto–Brier theorem, with the visibility characterisation, examples and dense approximation, and with scope narrowed to refereed results. It is not yet refereed. Citations to Rockafellar and Schrijver need checking.

## 2. Corrections adopted (auditor and referees)
- **Non-visible corners** limit the veto–Brier construction, not coverage. Boxes and orthant-planar targets have such corners and are covered.
- **The constant-odds-ratio set** is a box and is covered.
- **"The remaining problem is exactly CPM"** is withdrawn; within finite-view architectures it holds only as a sandwich.
- **The zero-support contamination repair** extends an exclusion within the VB class; it constructs nothing.
- **A62 Thm A62-1** as stated is false (the pinned-field counterexample); repaired.
- **C62's remark "(ND) automatic for piecewise-linear fields"** is false in general.
- **FD62:** the "|W0| = 1 family" wording, the "U ∪ −U" scope (needs K′ not a singleton), and "(LF)" in FD-1c are all fixed.
- **"For triangles the live distinction is general position"** is relabelled CONJECTURE. Triangles with one or two edge lines through a simplex vertex are open.

## 3. Coverage map now
- **Covered:**
  - *One-sided domains:* the visibility class (VB-type, plus one exempt point).
  - *Full domain and one-sided domains:* boxes; orthant-planar polygons.
  - *Full domain:* precise targets.
  - *Approximately:* every full-dimensional K, each approximant on its own domain.
- **Not covered by any construction yet:**
  - the reversed triangle (uniform pari-mutuel) and other pari-mutuel models;
  - T1 on two-sided domains;
  - triangles in general position whose corners are not visible;
  - triangles with one or two edges through simplex vertices.
- **Open routes for the reversed triangle:**
  - direction-continuous piecewise-linear fields on one-sided U;
  - irregular fields (A62's S1–S4, plus pinned faces);
  - incomplete orders with vetoes the target pays;
  - hybrids of vetoes with orthant-diagonal charts.

## 4. Suggested next round
1. Finish the direction-only analysis on one-sided U: redo C62 Lemmas 4.2–4.3 for direction fields, or find an escape.
2. Hybrids: lexicographic rankings with vetoes, then an orthant-diagonal chart. Characterise the union of the visibility class and the orthant-planar class, including triangles with edges through simplex vertices.
3. Extend W62 with the orthant-planar and box constructions as a second covering theorem, then referee the note.
4. Reversed triangle: incomplete orders with vetoes the target pays (C62 §6.4(iii)).
