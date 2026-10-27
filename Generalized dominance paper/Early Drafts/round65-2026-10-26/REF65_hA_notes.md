# REF65_hA — referee report on X65 Theorem H.1 and Corollary H.2 (26 Oct 2026)

Referee: REF65_hA. I checked every step of X65 §2 by hand, re-derived Steps 1–5, and replayed the construction with exact rational computation on 25 adversarial incoherent rivals in three worlds. Labels: PROVED / CHECKED (exact computation) / NUMERICS. Scripts are in `ref65hA_py/`; run each with `python3 -I <script>` from that folder. Each has an `.out` file.

## Verdict at the top

**Theorem H.1 holds as stated.** Every step of X65's proof is correct. I found two small expository gaps and one scope error in the corollary. None of them affects the theorem.

**Hypotheses that are actually used:**
- n ≥ 1 worlds. The case n = 1 is trivial.
- μ is a finite measure with the null sets of Lebesgue measure, and ∫|h| dμ < ∞. The streamlined proof in §1 needs only μ ≪ Lebesgue and a finite first moment.
- K′ ⊆ Δ is nonempty, compact and convex, and U = D_{K′}. The condition K′ ⊆ relint Δ is never used in H.1.
- X ⊆ U is measurable and incoherent.

**Not needed:** pointedness of cl hull(X) or of U; any condition on dim K′; X ⊇ int ℝⁿ₊; any continuity of the density.

**What the conclusion gives.** The defender N has m(N) − m(X) ∈ int ℝⁿ₊. In fact it gives more than (H) asks: **hull(X∖N) = hull(X) ⊇ N**, so μ((N∖X) ∩ hull(X∖N)) = μ(N∖X) > 0. This is Lemma S in §1.

**Corollary H.2 is correct after one scope repair.** On a fixed U = D_{K′}, comparison-deleted Brier Δ(all coherent models on U) satisfies every requirement of the binding framework. Its undominated models are exactly the coherent models on U. It covers **exactly the full-dimensional K with K′ ⊆ relint K**. X65 writes "every K with K′ ⊆ relint K". That is false for lower-dimensional K, where (LF) fails on any one-sided domain (paper, Prop lowdim). Lower-dimensional targets are not covered by this result.

## 0. Verdict table

| # | Item (X65) | Verdict | Note / repair |
|---|---|---|---|
| a1 | Step 1: Lemma 5.1 relativised to G = hull(X) | **CORRECT** | §2(a). Lyapunov holds (μ atomless; the vector measure h dμ is finite). ℳ_G is full-dimensional (G open, μ charges open sets). Maximisers of λ·m within G are unique a.e. (hyperplanes are null). Boundary case: the normal cone is pointed, misses ℝⁿ₊∖0, and a direction d ≫ 0 lies in int T_{ℳ_G}. A shorter proof by minimax needs no case split (§1, Step 1′). |
| a2 | X ⊆ hull(X) a.e.; G open, convex, coherent; P > 0 on G, P ≥ 0 on cl G | CORRECT | Q_X is closed (countable dense subset), ∂G = {P = 0} is null, and K′ ⊆ Q_X because X ⊆ U. CHECKED: every piece of every rival lies in G with exact equality of mass. |
| a3 | "X is a G-Bayes act ⟺ X is coherent"; K′ ⊆ conv(Q_X ∪ {π}) | CORRECT | ⇐: X = G = G ∩ {π·h > 0} for any π ∈ Q_X. ⇒: G ∩ {π·h > 0} = D_{conv(Q_X∪{π})}, and its credal set contains K′. So no incoherent X can be a G-Bayes act, and no coherent X fails to be one. |
| b | Step 2: N₀∖X is non-null | CORRECT | If it were null, k·(m(N₀) − m(X)) = −k·m(X∖N₀) ≤ 0 for k ∈ K′, while the left side is > 0 because m(N₀) − m(X) ≫ 0 and k ∈ Δ. Only K′ ≠ ∅ and k·h ≥ 0 on U are used. |
| c | Step 3: the uniform shrink | CORRECT | P_{Q_τ} = (1−τ)P + τ min_i h_i. N_τ = D_{conv(Q_X ∪ {π} ∪ Q_τ)} is coherent, with credal set ⊇ K′. N_τ ↑ N₀ as τ ↓ 0, so m(N_τ) → m(N₀) by dominated convergence (dominating function \|h\|). a ∈ N_τ for small τ, and a is a density point of N_τ∖X because N_τ is open. |
| d1 | Step 4: the representation b = Σλ_j x_j + p′ | CORRECT | P(b) = δ > 0 gives b ∈ G = cone(X_d) + int ℝⁿ₊ (W1, "⊆", proved in X65 §1). Moving each x_j off the null set ∂N_τ to nearby points of X ∩ X_d keeps p′ ≫ 0. A "removed" x_j lies in the exterior of N_τ, so it is a density point of B. |
| d2 | Step 5: q·x ≥ −((1−τ)/τ)P(x) for kept points | CORRECT | Kept points lie in the open set N_τ, so no boundary or density issue arises. The bound q·x_j ≥ min_i x_{j,i} > −((1−τ)/τ)P(x_j) uses only q ∈ Δ. |
| d3 | Removed points: q·x_j ≥ 0 ≥ −((1−τ)/τ)P(x_j) | **GAP (expository)** | This needs P(x_j) ≥ 0, which holds because X_d ⊆ cl G (every ball around a density point meets X ∩ G). X65 states it only for the case of a nonnegative minimum. Repair: one sentence. |
| d4 | Superadditivity: Σλ_j P(x_j) ≤ P(b − p′) ≤ δ − min p′ < δ | CORRECT | P is a minimum of linear forms, hence superadditive and positively homogeneous, and P(h+p) ≥ P(h) + min_i p_i. |
| d5 | Uniformity in q; Q_{X∖N_τ} may be large | CORRECT; the worry is vacuous | The bound q·a ≥ P(a) − δ/τ > P(a)/2 is uniform in q, since δ is fixed before q. The referee's Lemma S shows more: Q_{X∖N_τ} = Q_X for **every** τ ∈ (0,1). It is never large. |
| d6 | X∖N_τ null | CORRECT | Then Q_B = Δ, and the bound gives a ≫ 0. By Lemma S this case occurs only when Q_X = Δ, i.e. X ⊆ int ℝⁿ₊ a.e. (rival E8). |
| d7 | P(a) > 0; a is a density point with positive measure nearby | CORRECT | a ∈ N₀ ⊆ G. Density is inherited because N_τ is open. |
| e | Hidden assumptions: pointedness, dim K′, n ≥ 2, μ, X ⊇ int ℝⁿ₊, Example NP | **None hidden** | §2(e). Pointedness and dim K′ are never used. n ≥ 1 suffices. X ⊇ int ℝⁿ₊ is not used. μ needs only absolute continuity, finite first moment and finiteness. Example NP is CORRECT and is handled by the shrink (CHECKED, `np_and_highdim.out` A1–A3). |
| f1 | Cor H.2: the binding framework holds for Δ(all coherent on U) | CORRECT | §3. (G), (IB) and (TC) come from ES64 Thm 3.2. (GC), (C), (ID) and target undominated come from Thm 3.2(i)–(iii) together with (★). (★) is equivalent to (H) by REF64_es §2.5 and is now proved. |
| f2 | Cor H.2: "every K with K′ ⊆ relint K is covered" | **ERROR (scope)** | Correct set, for fixed U: the **full-dimensional** K with K′ ⊆ relint K. This is exact: Lemma LF(a) gives sufficiency, Lemma LF(b) gives K′ ⊆ relint K, and Prop lowdim excludes lower-dimensional K on one-sided U. Repair: insert "full-dimensional". ES64 Cor 3.5 carries the same omission. |
| f3 | "Universal" | CORRECT with the auditor's scope | One ranking per U. Every full-dimensional K is covered by *some* such ranking: choose K′ ⊆ relint K (e.g. K′ = {k₀} for a k₀ ∈ relint K), which fixes U and the ranking. Different targets need different U unless their relative interiors share K′. |
| f4 | Lower-dimensional targets | Not covered (correct that X65 does not claim them) | They need domains that are not essentially one-sided (Prop lowdim). H.1 is stated for one-sided U only. See §4 for the nearby open question. |
| g | Adversarial rivals | **No failure** | 25 incoherent rivals, all certified exactly (§4): spikes; three spikes; deep hole with hull = U; the boundary case of Step 1; Q_X meeting ∂Δ; Q_X = Δ; two non-pointed hulls; a comb of teeth; a union of Bayes acts; a full-width shallow collar; 14 random rivals. Controls: without the shrink (τ = 0) the witness mass is **0** in two of them. So the shrink is genuinely needed. |
| h1 | Lemma 2D.1 | CORRECT under X ⊇ int ℝ²₊ (assumed in X65 §3) | The summary phrase "a dominator fails to witness iff it contains X" (§0.3, status table) needs this qualifier. Without it, "if" fails: a dominator containing X then gains int ℝ²₊∖X, which lies in every hull. |
| h2 | Theorem 2D | CORRECT | Every case checked by hand, including βt̄ < T_R T_L ≤ 1 and the no-room cases. Re-run byte-identical: 384/384 (`rerun_two_world.out`). |
| h3 | Lemma 4.1 (cut lemma) | CORRECT | Notational clash: e_i is used both for a coordinate of e and for a unit vector. |
| h4 | Prop 4.2 | CORRECT (subsumed) | The finite set of cut rays must be chosen depending on the target point a, which is fine. It is superseded by Lemma S, which needs no pointedness. |
| h5 | Lemma 4.3 (localisation) | CORRECT | The degenerate case S = ∅ forces Q_X = Δ, and the statement still holds. |
| h6 | §5.1 surround rival, Parts 1–3 | CHECKED (re-run byte-identical, `rerun_surround3d.out`) | My minimax solver independently finds the optimal G-Bayes margin 4.115·10⁻⁴ at π ≈ (0.20328, 0.39836, 0.39836), consistent with X65's line search. |
| h7 | §0.2 wording: "Bayes acts of hull(X) remove it" | GAP (wording) | G-Bayes acts alone do **not** suffice. In rivals E1b and E9, μ((N₀∖X) ∩ hull(X∖N₀)) = 0 exactly. The cure is G-Bayes act **plus** shrink, which X65's own Part 2b also notes. |
| h8 | §5.2 Example NP | CORRECT | CHECKED in 50-digit arithmetic: A1 (non-generation), A2 (an explicit two-point witness after the shrink), A3 (Q_X = {u}). |
| h9 | §5.3 | Vacuous; not refereed in detail | — |

---

## 1. A streamlined proof (referee; PROVED)

This proof is offered for the paper. It removes W1, density points and the case split in Lemma 5.1.

Setting: n ≥ 1; μ finite, μ ≪ Lebesgue, ∫|h| dμ < ∞; K′ ⊆ Δ nonempty, compact and convex; U = D_{K′}. Let X ⊆ U be incoherent. Put G := hull(X) = D_{Q_X} and P := P_{Q_X}. As in X65:
- G is open and coherent;
- X ⊆ G a.e., so P ≥ 0 a.e. on X;
- Q_X is closed.

**Step 1′ (minimax).** Let ℳ_G := {m(Y) : Y ⊆ G}. It is convex and compact by Lyapunov. Put x := m(X) ∈ ℳ_G and σ(λ) := max_{z∈ℳ_G} λ·z. By the minimax theorem for the bilinear function λ·(z − x) on Δ × ℳ_G,

  v := max_{z∈ℳ_G} min_i (z_i − x_i) = min_{λ∈Δ} (σ(λ) − λ·x),

and both optima are attained, at z* and λ*.
- If v ≤ 0, then λ*·x ≥ σ(λ*). So X maximises λ*·m(Y) over Y ⊆ G. By a.e.-uniqueness of the maximiser, X = G ∩ {λ*·h > 0} a.e. That set is coherent: a contradiction. Hence v > 0.
- (z*, λ*) is a saddle point, so z* maximises λ*·z, and z* = m(G ∩ {λ*·h > 0}).

So N₀ := G ∩ {λ*·h > 0} is coherent, with m(N₀) − m(X) ≥ v𝟙 ≫ 0. Full-dimensionality of ℳ_G is not needed.

Computationally, λ* is the minimiser of a convex function on Δ. This is how `core.find_pi_minimax` found π on all 25 rivals, including the 6 on which grid search failed.

**Step 2 and Step 3** are exactly as in X65. The only change: choose τ so small that m(N_τ) − m(X) ≫ 0 and μ(N₀∖N_τ) < μ(N₀∖X). Then μ(N_τ∖X) > 0.

**Lemma S (shrink invariance; PROVED).** Let c ≥ 0. If q ∈ Δ and q·x ≥ −c P(x) for μ-a.e. x ∈ X, then q ∈ Q_X.

*Proof.*
- For q′ ∈ Q_X we have (q + cq′)·x ≥ q·x + cP(x) ≥ 0 a.e. on X. So T(q′) := (q + cq′)/(1+c) ∈ Q_X.
- T is a contraction with ratio c/(1+c) and fixed point q.
- Hence Tᵏ(q′) → q, and Q_X is closed, so q ∈ Q_X. ∎

**Corollary S.** Let τ ∈ (0,1) and let N be any measurable set with N ⊆ D_{(1−τ)Q_X+τΔ}. Then **hull(X∖N) = hull(X)**.

*Proof.*
- Let q ∈ Q_{X∖N}.
- On X ∩ N: q·x ≥ min_i x_i > −((1−τ)/τ)P(x), pointwise.
- On X∖N: q·x ≥ 0 ≥ −((1−τ)/τ)P(x) a.e.
- Lemma S gives Q_{X∖N} ⊆ Q_X. The reverse inclusion is trivial. ∎

**Conclusion.** N := N_τ ⊆ G = hull(X∖N_τ). So μ((N∖X) ∩ hull(X∖N)) = μ(N∖X) > 0, and m(N) − m(X) ≫ 0. ∎

*Relation to X65 Steps 4–5.* X65's estimate q·a ≥ P(a) − δ/τ holds for every δ ∈ (0, τP(a)/2). Letting δ → 0 gives q·a ≥ P(a) for all a ∈ G and all q ∈ Q_B. Shifting by 𝟙, this means q ∈ Q_X. So X65's argument proves Corollary S too; Lemma S is its 3-line form.

*Checks of Lemma S.*
- Exact: Q_{X∖N} = Q_X on all 25 rivals, at the certified τ and at 6 random τ ∈ (0,1) with random coherent N ⊆ D_{Q_τ}. That is 175 exact checks, with no exception.
- NUMERICS (LP): 300 random instances, n = 3…7, no violation.

---

## 2. Notes on the checks (a)–(e)

**(a) Step 1.**
- *Lyapunov.* The ℝⁿ-valued measure Y ↦ ∫_{Y∩G} h dμ is finite (first moment) and non-atomic (μ ≪ Lebesgue). So its range ℳ_G is convex and compact.
- *Full-dimensional ℳ_G.* If λ·m(Y) = 0 for all Y ⊆ G, then G ⊆ {λ·h = 0}, which is impossible for an open nonempty G when μ charges open sets. X65's Step 1 needs this; Step 1′ does not.
- *Uniqueness.* λ·m(Y) ≤ ∫_{G∩{λ·h>0}} λ·h, with equality iff Y △ (G∩{λ·h>0}) ⊆ {λ·h = 0} a.e. This holds for every λ ≠ 0, including λ on ∂Δ, and G ∩ {λ·h > 0} is coherent for every λ ∈ Δ.
- *Boundary case.* An outer normal ν at x makes X a.e. equal to G ∩ {ν·h > 0}.
  - If ν ≥ 0, X is coherent: a contradiction.
  - Otherwise the normal cone is pointed (ℳ_G is full-dimensional) and meets ℝⁿ₊ only in 0.
  - Separating K₁ = conv(N ∩ {|ν|₁ = 1}) from ℝⁿ₊ gives d ≥ 0 with d·ν < 0 on K₁, and then d + ζ𝟙 ≫ 0 does too.
  - int T(x) = {d : d·ν < 0 on N∖0} = ∪ t(int ℳ_G − x).
  - Rival E3 (X = U ∩ {ν·h > 0}, ν = (1, 1, −1/5)) is exactly this boundary case. Strict margin 0.0183 is CHECKED.
- *Margin.* Step 1 delivers m(N₀) − m(X) ≫ 0, so WT65's open question about zero-margin witnesses is moot.

**(b) Step 2.** It needs only one k ∈ K′. The argument fails on two-sided domains (K′ = ∅), where the conclusion can genuinely fail for N₀. Take X = N₀ ∪ E with E ⊆ −int ℝⁿ₊. This is irrelevant here.

**(c) Step 3.** P_{Q_τ}(h) = P(h) − τ(P(h) − min_i h_i) is non-increasing in τ, because P ≥ min_i h_i on Δ-mixtures. So N_τ increases as τ ↓ 0, with union N₀. The credal set of N_τ is conv(Q_X ∪ {π} ∪ Q_τ), which contains K′.

**(d) Steps 4–5.** See table rows d1–d7. The only omission is P(x_j) ≥ 0 for removed points (row d3).

**(e) Hidden assumptions.**
- *Pointedness and dim K′.* Never used. CHECKED on a non-pointed hull with a pointed U (E5, K′ = {u}) and on a non-pointed U (E5b, K′ a segment). Example NP is CHECKED as well.
- *n.* n = 1 is trivial: U = (0,∞), G = U, and N = U witnesses.
- *μ.* As stated at the top. A positive continuous density is not needed.
- *X ⊇ int ℝⁿ₊.* Not used. Rivals E3 and E8 violate it.
- *K′ ⊆ relint Δ.* Not used in H.1. It matters only for W2 and (LF).

---

## 3. The corollary chain (f)

1. **(H) holds** (Theorem H.1).
2. **REF64_es §2.5** (refereed CORRECT): (★) for 𝒩 = all coherent models on U ⟺ (H).
   - A coherent D_Q contains X∖N a.e. iff Q ⊆ Q_{X∖N}, iff D_Q ⊇ hull(X∖N).
   - So r(N,X) attacks no coherent model iff μ((N∖X) ∩ hull(X∖N)) > 0.
   - I re-checked this.
3. **ES64 Thm 3.2** (refereed CORRECT) applied to Δ(𝒩):
   - reflexivity, a.e.-ties, strict (G), (IB) and (TC) (Lemma 1.3);
   - (i) no member of 𝒩 has a weak dominator;
   - (ii)–(iii) under (★): undominated = 𝒩 (GC); direct (C) in the strong form "tied ⇒ equal"; (W); every incoherent X is dominated by a coherent, undominated N (ID).
   - With H.1's strict margin, N is strictly Brier-better at every world, and the record is never deleted.
4. **Target K.**
   - "Target undominated" needs D_K ∈ 𝒩, i.e. K′ ⊆ K.
   - (LF) holds iff K′ ⊆ relint K, given full-dimensional K (Lemma LF(a),(b)).
   - (LF) fails for every lower-dimensional K on a one-sided domain (Prop lowdim).

   Hence, **for fixed U = D_{K′}: Δ(all coherent on U) covers K ⟺ K is full-dimensional and K′ ⊆ relint K.** This includes the reversed triangle with K′ = (u+K)/2.
5. **Every full-dimensional K** is covered by the ranking built on any U = D_{K′} with K′ ⊆ relint K. This is a different ranking for each choice of U. "Universal" means universal over targets compatible with one U, not one ranking for all targets.
6. The auditor's interpretive caveat stands and X65 records it. The ranking is coherence-informed: it represents coherence by dominance, but it does not justify coherence independently on accuracy grounds.

---

## 4. Adversarial testing (g): `ref65hA_py/h1_check.py` → `h1_check.out` (CHECKED)

**Method.** Density e^{−|h|₁}. Each rival is a finite disjoint union of open polyhedral cones. The pipeline works on the credal side, so it also handles non-pointed hulls:
- Q_X is computed exactly from the generators (with lineality) of the piece closures;
- G = D_{Q_X};
- π is found by the minimax of Step 1′ (float), then verified exactly;
- N_τ = G ∩ {π·h > 0} ∩ D_{Q_τ}.

**Checked exactly for each rival:**
- incoherence (μ(G∖X) > 0);
- X ⊆ G;
- m(N₀) − m(X) ≫ 0;
- μ(N₀∖X) > 0;
- m(N_τ) − m(X) ≫ 0;
- Q_{X∖N_τ} = Q_X;
- μ(N_τ∖X) > 0;
- the witness mass μ((N_τ∖X) ∩ D_{Q_{X∖N_τ}}), computed directly. It equals μ(N_τ∖X) in every case.

| Rival | Feature | Certified τ | Smallest margin |
|---|---|---|---|
| E1 | spike beyond F₁ to ∂U (X65 §5.1) | 10⁻⁴ | 2.9·10⁻⁴ |
| E1b | three spikes; **N₀ alone has witness mass 0** | 10⁻² | 0.060 |
| E2 | deep hole; hull(X) = U | 10⁻³ | 1.1·10⁻⁴ |
| E3 | Step 1 boundary case, X misses part of int ℝ³₊ | 10⁻² | 6.7·10⁻³ |
| E4 | Q_X has a vertex (½,½,0) ∈ ∂Δ; e₃ ∈ ∂G | 10⁻³ | 2.4·10⁻⁴ |
| E5 | non-pointed hull (line ℝw), K′ = {u} | 10⁻¹ | 1.23 |
| E5b | K′ a segment: U and hull(X) non-pointed | 10⁻⁴ | 2.8·10⁻⁴ |
| E6 | comb of 9 teeth along a face of U | 10⁻⁵ | 5.0·10⁻⁵ |
| E7 | N_{p₁} ∪ N_{p₂} (ES64 T1) | 10⁻⁴ | 2.4·10⁻⁴ |
| E8 | X ⊆ int ℝ³₊ with a hole: Q_X = Δ, X∖N null | 10⁻¹ | 0.012 |
| E9 | full-width shallow collar beyond F₁; **N₀ alone has witness mass 0** | 10⁻⁵ | 1.6·10⁻⁷ |
| R0–R29 | 14 incoherent random rivals (Bayes act ± random bumps and holes; 16 of the 30 draws were coherent and skipped) | 10⁻²…10⁻⁷ | down to 6.6·10⁻⁷ |

**Result.** 25/25 certified. For τ = 0, Q_{X∖N₀} ≠ Q_X in 24/25. ES64 hunt3-type failures were search failures; Step 1′'s convex minimisation removes them.

**Re-runs.** X65's `two_world.py` and `surround3d.py` re-run byte-identical.

**Example NP** (`np_and_highdim.out`, 50 digits):
- A1: w′ + ε𝟙 ∉ cone(±w) + int ℝ³₊.
- A2: with τ = 1/10, two explicit interior points x± of X outside cl N_τ give (w′ + ε𝟙) − (x₊ + x₋)/(2β) = 0.0096·𝟙 ≫ 0.
- A3: Q_X = {u}, tested against 20 random perturbations.

---

## 5. Repairs requested

1. **Cor H.2, §0.5, §6:** replace "every K with K′ ⊆ relint K" with "every full-dimensional K with K′ ⊆ relint K". Add: "lower-dimensional K are not covered: they require domains that are not essentially one-sided." Carry the same fix into ES64 Cor 3.5 wherever it is quoted.
2. **Step 5:** add "X_d ⊆ cl G, so P(x_j) ≥ 0 for every x_j". Optionally replace Steps 4–5 by Lemma S and Corollary S (§1).
3. **§0.2:** "Bayes acts of hull(X) remove it" → "Bayes acts of hull(X), followed by the uniform shrink, remove it". G-Bayes acts alone can fail (E1b, E9).
4. **§0.3 and the status table:** "fails to witness iff it contains X" → add "for X ⊇ int ℝ²₊ (after Prop 5.4)".
5. **Hypotheses** (optional sharpening): H.1 needs only μ ≪ Lebesgue with a finite first moment, and K′ ⊆ Δ nonempty, compact and convex.
6. **Lemma 4.1:** rename the unit vector to avoid clashing with the coordinate e_i.
7. **Credit:** Step 1 is H65's relativisation, as X65's independence statement says. The paper should credit the construction accordingly.

## 6. Nearby open question (not claimed)

Lower-dimensional targets need domains that are not essentially one-sided. On such domains:
- Q_B can be empty, and then "hull" must be read as "no coherent model contains B";
- X65's Step 2 fails.

Step 1′ and Lemma S still apply verbatim wherever Q_X ≠ ∅. A version of H.1 for two-sided U = {h : h_l > 0 for some l} is therefore the natural next target for lower-dimensional K. I have not checked it.

## 7. Files (`ref65hA_py/`)

| File | Content |
|---|---|
| `core.py` | independent exact cone moments; generators with lineality; exact credal polygons Q; set differences; float search; minimax Step-1′ solver |
| `h1_check.py` / `.out` | exact replay of H.1 on 25 adversarial rivals; τ = 0 controls; random-τ invariance checks |
| `np_and_highdim.py` / `.out` | Example NP (A1–A3, 50 digits); Lemma S in n = 3…7 (LP, NUMERICS) |
| `rerun_two_world.out`, `rerun_surround3d.out` | byte-identical re-runs of X65's scripts |
