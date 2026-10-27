# REF65_hB — Referee report on H65 Theorem H and X65 Theorem H.1 (26 Oct 2026)

Referee: REF65_hB (independent). Labels: PROVED / CHECKED (exact computation) / NUMERICS. I checked every step of both proofs by hand. I also wrote exact scripts, independent of `es64py/`, `h65py/` and `x65py/`, to probe edge cases (`ref65hB_py/`; run each with `python3 -I <script>` from that folder; each has an `.out` file).

## Headline

1. **(H) is PROVED. Both proofs are correct. I recommend X65's proof for publication.**
   - Hypotheses:
     - n ≥ 1 worlds;
     - (M): μ is a finite Borel measure with the null sets of Lebesgue measure and ∫|h| dμ < ∞. A positive density with a finite first moment is a special case;
     - K′ is nonempty, compact and convex, with K′ ⊆ relint Δ, and U = D_{K′};
     - X ⊆ U is an arbitrary measurable incoherent model.
   - Conclusion: there is a coherent N = D_Q, with K′ ⊆ Q, such that m(N) − m(X) ∈ int ℝⁿ₊ and μ((N∖X) ∩ hull(X∖N)) > 0.
   - Nothing else is assumed. No regularity of X, no pointedness of hull(X), and no condition on n or dim K′.
   - **X65's proof does not use K′ ⊆ relint Δ.** It needs only ∅ ≠ K′ ⊆ Δ. H65's proof uses relint in its lineality step (Lemma 2.5). This extension is not needed for the brief.
2. **The universal-cover corollary holds** (PROVED, given ES64 Thm 3.2 / Cor 3.5 and REF64_es §2.5, all refereed CORRECT).
   - On a fixed U = D_{K′}, the relation Δ(all coherent models) satisfies reflexivity, a.e.-ties, strict (G), (IB) and (TC), and also finite-chain consistency.
   - Its undominated models are exactly the coherent models on U.
   - Every incoherent model is dominated by a coherent one, by Brier-strict margins at every world.
   - Direct (C) and (W) hold.
   - **On that U it covers exactly the full-dimensional K with K′ ⊆ relint K** (§4).
3. **No counterexample was found, and none can exist.** I tried the adversarial classes in the brief:
   - spikes and needles running to ∂U;
   - notches and combs at ∂hull(X), so that X is dense near ∂hull(X);
   - non-pointed hulls, including Example NP and hull(X) = U;
   - X ⊇ int ℝⁿ₊ throughout.

   No step failed. Every search failure was traced to the search: the needed π or τ was below its resolution.
4. **Scope (the auditor's corrections stand).**
   - "Universal" means universal on one fixed U.
   - Δ(𝒩) is coherence-informed. It represents coherence through dominance; it is not an independent accuracy-based justification of coherence.
   - Δ(𝒩) violates (Add) (REF64_es §5.3(3)), so nothing here bears on the (Add)-strengthened framework.

---

## 1. Verdict table

### 1.1 H65 (`H65_notes.md`)

| # | Item | Verdict | Notes / repairs |
|---|---|---|---|
| H1 | Lemma 2.1 (support-point witness ⇒ μ(A ∩ hull B) > 0) | **CORRECT** | Brief point (b), second half: the e_j are *conic support* points Σ(B). These are conic limit points: every open cone around e_j has positive B-mass. They need not be density points, or points of B or supp(B); X need not be a cone. **This is harmless.** The proof uses only the open cone {q·h < 0} around e_j, so it is a strict strengthening of the sufficiency half of WT65 W1′. |
| H2 | Lemma 2.2(a)–(c) (Q_X via Σ(X); hull(X) = int C; X ⊆ hull(X) a.e.) | **CORRECT** | Lindelöf covers, the polar description of int C, and the null boundary of a convex set are all fine. |
| H3 | **Lemma 2.2(d)** (relative ES64 Lemma 5.1) | **CORRECT** (minor presentational GAP) | Brief point (a). The checks: X ⊆ G a.e. by (c), so m(X) ∈ ℳ_G. ℳ_G is compact and convex by Lyapunov (atomless, finite first moment), and full-dimensional by (M), since G is open and nonempty. Maximisers G ∩ {ν·h > 0} are unique a.e. Every G-Bayes act G ∩ {π·h > 0} = D_{conv(Q_X∪{π})} is coherent, including π ∈ ∂Δ. ES64's interior and boundary cases then go through: the normal cone is pointed because ℳ_G is full-dimensional, and int T_ℳ(x) = ∪_t t(int ℳ − x). *Repair:* write the boundary case out ("verbatim" hides the full-dimensionality and uniqueness inputs). X65's Step 1 does this. |
| H4 | **Lemma 2.3, Generation Lemma** | **CORRECT** (pointed and non-pointed) | Brief point (b). Checked line by line (§2.1). Steps 0–1: P = cl N₁ is pointed and P ∩ (−C_out) = {0}, and g separates. Step 2: C = P′ + C_out, with closedness from the recession argument. Step 3, the key step: the minimiser t* lies in N₁; perturb to w = t* − εx₀; then 0 ≤ g(y) < 1 and q·y < −β contradict q·y ≥ −β g(y). Step 4: x − ε𝟙 ∈ C_out, then approximate. *Pointed case:* the Minkowski remark is right, since extreme rays of C lie in Σ ∪ ℝⁿ₊ and on ∂C. *Non-pointed case:* the lineality hypothesis is **necessary**. In X65's NP with N₁ = U, the conclusion fails (CHECKED, `np_lineality.out` (1)). It is also **sufficient**, by the proof. |
| H5 | Lemma 2.4 (thin cuts: coherent, cost → 0) | **CORRECT** | R(s) ⊆ {h ∈ N′ : h_k < 0, q·h ≤ s|h_k|/(1−s)} decreases to ∅. Dominated convergence applies. |
| H6 | Lemma 2.5 (lineality directions have a negative coordinate) | **CORRECT** | This is the only use of K′ ⊆ relint Δ. It fails without relint: with K′ = {e₁}, L ∋ e₂ ≥ 0 cannot be cut by any q″_k. That is why H65 needs relint and X65 does not. |
| H7 | **Theorem H, Step 2 (lineality cut)** vs X65 Example NP | **CORRECT** | Brief point (e). q_X·l = 0 on L, and q″_k·l = s₁l_k < 0 for some k, so cl N₁ ∩ L = {0}. On NP, after the cut, the tangential X-points w ± βw′ + γ𝟙 lie outside cl N₁ and generate a = w′ + 𝟙 with residual (9/10)𝟙 (CHECKED, `np_lineality.out` (2)). Without the cut they lie inside, and only ±w remain on ∂U. **So Step 2 is exactly the extra argument X65 §5.2 asks for.** On polyhedral non-pointed rivals the cut was not needed (`e2e.out`: R3, R4, R6 all report "same a from points outside cl N₀: yes"). The NP obstruction is a limit (non-polyhedral) phenomenon. |
| H8 | Theorem H, Steps 1, 3–6 (margins, cut defenders, witness) | **CORRECT** | Brief point (d). Margin: d₁ ≥ ½d₀ after Step 2; after Step 5, m(N) − m(X) ≥ d₁ − ∫_{N₁∖N}\|h\| ≫ 0. Coherence: Q = conv(Q_X ∪ {π} ∪ {q″_k} ∪ {q′_j}) ⊇ Q_X ⊇ K′, so the credal set of every cut defender contains K′. a ∈ N because q′_j·a > 0 for small s₂. e_j ∈ Σ(X∖N) via the open cone W_j disjoint from N. Absorbing e_j ≥ 0 into p keeps p ≫ 0, and every remaining e_j has a negative coordinate, so the cut direction exists. Step 3's non-null gain is the K′-positivity argument, which needs only k ∈ Δ. |
| H9 | Count of cuts (≤ 2n; ≤ n if no line) | CORRECT (cosmetic) | With WT65 W2, the cuts at the e_j number ≤ n−1, so the totals are ≤ 2n−1, and ≤ n−1 in the pointed case. |
| H10 | **Cor H.1** (W^≫(X) non-empty and open; polytopes suffice) | **CORRECT** | Brief point (f). Non-empty by Theorem H. Open by WT65 C2 (continuity of m) and C4 (lsc of Φ_X); I re-checked C4's proof: density points of B with P_Q < 0 persist under perturbation, then Fatou. Polytopes: by density of polytopes in 𝒦(K′) plus openness, or directly, since Q is a polytope when Q_X is. |
| H11 | Cor H.2 (universal cover) | **CORRECT** given refereed inputs | See §4 for exactly which targets are covered. |
| H12 | §3 exact checks | CHECKED (re-run) | `examples.py` re-run is byte-identical (`rerun_h65_examples.out`). I reviewed `construct.py`'s certificate logic. a ∈ N and a ∉ cl(each piece) make a a density point of N∖X. Each e_j is an extreme ray of a non-null piece with e_j ∉ cl N, so e_j ∈ Σ(X∖N). The margin is exact. The defender's inequalities are Q_X facet normals in Δ, U's K′-vertices, π and the cuts, so it is coherent. The verification is sound. `hunt3_final.py` re-run stopped at the lead's instruction after 2/30 rivals; both lines identical (§6). |
| H13 | §0 / §2.7 diagnosis ("U-Bayes base defender caused earlier failures") | CORRECT as interpretation | Consistent with X65 §5.1: 90/104 U-Bayes dominators fail on the spike. That output was re-run and is identical. |
| H14 | §4 (WT65's open question: strict witnesses always exist) | CORRECT | — |

### 1.2 X65 (`X65_notes.md`)

| # | Item | Verdict | Notes / repairs |
|---|---|---|---|
| X1 | Theorem H.1, Step 1 (relative Lemma 5.1) | **CORRECT** | As H3, written out in full. |
| X2 | Step 2 (non-null gain) | **CORRECT** | — |
| X3 | Step 3 (uniform shrink N_τ = N₀ ∩ D_{(1−τ)Q_X + τΔ}) | **CORRECT** | P_{Q_τ} = (1−τ)P + τ min_i h_i. Since min_i h_i ≤ P(h), N_τ increases as τ ↓ 0 and exhausts N₀. The defender is coherent, with credal set conv(Q_X ∪ {π} ∪ Q_τ) ⊇ K′. a stays a density point of N_τ∖X because N_τ is open. |
| X4 | **Step 4** (representation of b = a − (P(a)−δ)𝟙) | **CORRECT** | P(b) = δ > 0, so b ∈ G. WT65 W1 (⊆) gives b = Σλ_jx_j + p′ with x_j ∈ X_d. Moving the x_j off the null set ∂N_τ is legitimate: points of X_d∖∂N_τ are dense near each x_j, and p′ ≫ 0 is an open condition. Removed points are density points of B; kept points lie in N_τ. *Minor:* say explicitly that X_d ⊆ cl G (X ⊆ G a.e.), which gives P(x_j) ≥ 0. |
| X5 | **Step 5: lower bound for retained (kept) points** | **CORRECT** | x_j ∈ D_{Q_τ} gives min_i x_{j,i} > −((1−τ)/τ)P(x_j), so q·x_j > −((1−τ)/τ)P(x_j) for *every* q ∈ Δ. Removed points satisfy the same bound for q ∈ Q_B, by Claim 0 and P ≥ 0. |
| X6 | **Step 5: superadditivity and uniformity over q ∈ Q_B** | **CORRECT** | Σλ_jP(x_j) ≤ P(b − p′) ≤ P(b) − min p′ < δ. So q·a > P(a) − δ/τ > P(a)/2, with a constant independent of q. min over the compact Q_B is ≥ P(a)/2, so the sup-ball of radius P(a)/2 around a lies in hull(B). B null is handled (Q_B = Δ). **Adversarial test (CHECKED, `shrink_algebra.out`):** 3801 exact instances. Kept points sat at the edge of D_{Q_τ}, removed points had huge negative coordinates, Σλ_jP(x_j) was pushed to δ, Q_X touched ∂Δ, and τ went down to 10⁻⁶. There were **0 failures**. The worst ratio was min_{Q′} q·a / P(a) = 0.5016, so **the bound P(a)/2 is essentially sharp**. *Control, τ = 0 (no shrink):* 1554/3288 instances give min ≤ 0. **The shrink is essential.** |
| X7 | Cor H.2 | **CORRECT** given refereed inputs | Same as H11. |
| X8 | Theorem 2D and Lemma 2D.1 (two worlds) | CORRECT (spot-checked; script re-run identical, 384/384) | I checked case (c) by hand: v₁ − β\|v₂\| = a₁(1−βt̄) + a₂(β−s̄) > 0, using βt̄ < T_LT_R ≤ 1. *Wording:* "fails to witness iff it contains X" uses the normalisation X ⊇ int ℝ²₊. |
| X9 | **Example NP** | **CORRECT** | Q_X = {u} (analytic argument checked). Σ(X) ∩ ∂U = {±w}. cone(±w) + int ℝ³₊ ∌ w′ + 𝟙 (exact). It defeats any generation from boundary support points, and Lemma 2.3 without its lineality hypothesis. It does **not** defeat H65 (H7). |
| X10 | Lemmas 4.1 and 4.3, Prop 4.2 | 4.1 CORRECT; 4.3 CORRECT as a sketch (not used); 4.2 subsumed | — |
| X11 | §5.1 surround rival | CHECKED (re-run identical, `rerun_x65_surround3d.out`) | — |

---

## 2. Notes on the delicate steps

### 2.1 H65 Lemma 2.3, Steps 2–3 (brief point (b))

- **Step 2.** C = P′ + C_out with P′ = cl cone(Σ ∩ P).
  - The inclusion cone(Σ∪ℝⁿ₊) ⊆ cone(Σ∩N₁) + cone(T∪ℝⁿ₊) is a split of generators.
  - Closedness: if |y_k| → ∞, the normalised limit ȳ ∈ P′ ⊆ P has −ȳ ∈ C_out ⊆ C. That contradicts P ∩ (−C) = {0}, which is where cl N₁ ∩ L = {0} enters.
- **Step 3.** Fix q ∈ ℝⁿ₊∖0 separating x ∈ P∖C_out from C_out.
  - The minimiser t* of q over the compact base Σ ∩ P ∩ {g = 1} has q·t* = −β < 0. So t* ∉ T, hence t* ∈ N₁, which is open.
  - The linear inequality q·s + βg(s) ≥ 0 holds on the generators, hence on P′.
  - For w = t* − εx₀ ∈ N₁ ⊆ C = P′ + C_out, any decomposition w = y + z has q·y ≤ q·w < −β and 0 ≤ g(y) ≤ g(w) < 1. That contradicts q·y ≥ −βg(y) ≥ −β.
  - Every inequality used is justified: g ≥ 0 and q ≥ 0 on C_out, g > 0 on P∖0, and x₀ ≫ 0.
- **"Support points of X outside N₁" in the non-pointed case.** They are *not* only boundary points of hull(X). Σ∖N₁ contains interior X-directions that the lineality cut has excluded from N₁; in NP these are the tangential points. H65's §0 phrase "in the pointed case these are the extreme rays" is accurate. The proof itself never assumes boundary location.

### 2.2 X65 Steps 4–5 (secondary item)

- The proof never needs to know where the x_j are relative to ∂G.
- The shrink forces every kept point to have its most negative coordinate controlled by its own P-value.
- Superadditivity bounds the total P-budget by δ.
- The choice δ < τP(a)/2 converts this into a margin P(a)/2 at a that is uniform in q ∈ Q_B.
- `shrink_algebra.out` shows the constant is attained up to 0.3%, so there is no slack to hide an error.

---

## 3. Attempts to break both proofs (brief: spikes, dense near ∂hull, non-pointed, hull = U, X ⊇ int ℝⁿ₊)

All scripts are in `ref65hB_py/`. Moments use density e^{−|h|₁} via my own implementation `geo3.py`; it agrees 200/200 with `es64py/cones.py` (`momcheck.out`). Every certificate is verified in exact rationals, as follows:
- N = D_Q is coherent;
- m(N) − m(X) ≫ 0;
- a lies in the open N and outside the closure of every piece of X;
- the removed points lie strictly inside pieces and outside cl N;
- min{q·a : q ∈ Δ, q·x_j ≥ 0 ∀ removed j} > 0, computed as an exact polygon in Δ.

By Claim 0 this certifies (H). Searches (for π and a) use floats; failures of a search refute nothing.

| Script | Rivals | Result |
|---|---|---|
| `np_lineality.py` | X65 Example NP (hull = U, non-pointed, X ⊇ int ℝ³₊) | (1) Generation fails without H65's Step 2. (2) It succeeds after the cut. (3) X65's shrink certifies the same a, with min_{Q′} q·a = 149/150 ≥ 3/4. CHECKED. |
| `shrink_algebra.py` | 3801 adversarial configurations of X65 Steps 4–5; control τ = 0 | 0 failures; bound sharp (0.5016). Control: 1554 failures. CHECKED. |
| `e2e.py` | R1 spike to ∂U (width 1/40) and R1′ needle (width 1/400); R2 notch at ∂D; R5 comb of 9 shallow notches; R3 half-space U minus an interior hole; R4 half-space minus 2 holes touching ∂U; R6 wedge U (K′ a segment, 1-dim lineality) minus a hole | **7/7 certified by X65's shrink** (margins down to 1.0·10⁻⁴; τ down to 10⁻⁵). **3/3 non-pointed cases also certified by H65's Step-2 path.** |
| `e2e_random.py` | 36 random rivals: spikes (widths to 1/1000), 1–4 notches touching ∂D, holes in the half-space, holes touching ∂U | 32/36 certified directly. The 4 misses were π-search failures on single shallow notches. |
| `notch_pi_scan.py`, `notch_pi_refine.py` | the 4 misses | Strict hull-relative Bayes acts exist, with exact margins 1.9·10⁻⁶ (×3) and 7.0·10⁻⁸. X65 certificate exact for all 4, with τ down to 10⁻⁸. **36/36.** |

Observations:
- The windows for the hull-relative Bayes act can be very small, as H65 §3.3 also reports. A coarse polar scan missed three of them. This is a search difficulty only; Lemma 2.2(d) guarantees existence.
- In every polyhedral run the final certificate used removed points only (kept = 0). The kept-point branch of X65 Step 5 is exercised by `shrink_algebra.py`, not by `e2e`.
- I found **no configuration in which any step of either proof fails.**

---

## 4. From (H) to the universal cover; which targets are covered on fixed U

**Chain (checked).**
- Theorem H / H.1 gives, for every incoherent X, a coherent N with m(N) − m(X) ≫ 0 and μ((N∖X) ∩ hull(X∖N)) > 0.
- A coherent D_{Q°} containing X∖N a.e. contains hull(X∖N) (REF64_es §2.5, using E23). So it meets N∖X in positive measure, and r(N,X) attacks no coherent model.
- Hence (★) holds for 𝒩 = all coherent models.
- ES64 Thm 3.2 (refereed CORRECT, E11–E14) gives:
  - (i) no coherent model has a weak dominator other than itself;
  - (ii)–(iii) every incoherent model is dominated by a coherent one; undominated = coherent; direct (C) in the strong form; (W).
- Also: (TC) by Lemma 1.3, and finite-chain consistency (REF64_es E3).
- ES64 Cor 3.5 is therefore unconditional within the setting. The converse direction (REF64_es §2.5) shows (H) was also necessary for this particular construction.

**Targets on a fixed U = D_{K′}** (K′ ⊆ relint Δ nonempty, compact and convex):
- **Protected:** every coherent model on U, that is, every D_Q with K′ ⊆ Q (Q may touch ∂Δ or be lower-dimensional). Each is undominated, and global coherence and (ID) hold.
- **Covered in the paper's sense** (Definition cover, which includes (LF)): exactly the full-dimensional K with K′ ⊆ relint K.
  - Sufficiency: paper Lemma LF(a).
  - Necessity: Lemma LF(b), together with the remark below for lower-dimensional K.
  - For K ⊇ K′ with K′ ∩ rbd K ≠ ∅, or K lower-dimensional, D_K is undominated, but (LF) fails. **No ranking on this U can repair that**, since (LF) is a property of the domain.
  - (Lower-dimensional K: some h ≠ 0 has k·h = 0 on K ⊇ K′. This h lies in ∂D_K but not in the open U.)
- **Across domains:** every full-dimensional credal K is covered by Δ(all coherent) on U = D_{K′} for any K′ ⊆ relint K, e.g. a point of relint K. This includes the reversed triangle.
  - Per the auditor's correction, this is "for each target, a ranking", and the ranking also covers every other K with K′ ⊆ relint K.
  - It is not "one U covers everything".
- **Measure:** (H) holds for every μ satisfying (M), which is more than the cover needs (REF64_es E14).

**Limitation to report alongside.** Δ(𝒩) decides whether to keep a comparison by asking whether its record attacks a coherent model. The theorem therefore shows coherence is *representable* through dominance under the agreed axioms. It does not give an independent accuracy-based vindication of coherence. Δ(𝒩) also fails (Add). Whether (G) + (IB) + (TC) + (Add) admits covers remains open and is untouched here.

---

## 5. Comparison and recommendation for publication

| Criterion | H65 (Theorem H) | X65 (Theorem H.1) |
|---|---|---|
| Length / machinery | Six lemmas, including a new cone lemma (Generation Lemma, with a separation and compact-base argument) and a lineality case split | Five short steps; uses only WT65 W1 (one inclusion, re-proved inline) and Claim 0 |
| Delicate points | Lemma 2.3 Steps 2–3; Step 2 lineality cut (necessary: NP) | none beyond Lemma 5.1 relativised; one inequality chain with an explicit, sharp constant |
| Hypotheses | needs K′ ⊆ relint Δ (Lemma 2.5) | needs only ∅ ≠ K′ ⊆ Δ |
| Output | explicit finite certificate (a; ≤ n−1 removed support points); defender = hull ∩ Bayes half-space ∩ ≤ 2n thin cuts; polyhedral when Q_X is | explicit quantitative witness (sup-ball of radius P(a)/2 in hull(X∖N)); defender = hull ∩ Bayes half-space ∩ D_{(1−τ)Q_X+τΔ}; polyhedral when Q_X is |
| Robustness to non-pointed hulls | handled, but only via the extra Step 2 | automatic |
| Computation | certificate easy to verify, harder to construct (support points on ∂hull) | construction is a one-parameter shrink; certificate verified by one LP/polygon |

**Recommendation.**
- Publish **X65's uniform-shrink proof as the proof of (H)**. Give Step 1 (relative Lemma 5.1) in full, as X65 does. Credit the relativisation idea to H65, as X65 already does.
- H65's Generation Lemma is a correct and independently interesting structural fact: support points outside an open coherent sub-cone generate it, once the lineality is cut off.
- It can appear as a remark or appendix, giving the finite certificate with ≤ n−1 removed support points and the explicit "≤ 2n cuts" defender. It is not needed for the theorem.
- If both are kept, the paper should state that the lineality hypothesis in Lemma 2.3 is necessary, citing Example NP.

**Required minor edits before publication.**
1. H65 Lemma 2.2(d): write out the boundary case rather than "verbatim" (H3).
2. X65 Step 4: state X_d ⊆ cl G, hence P(x_j) ≥ 0 (X4).
3. X65 statement: note that K′ ⊆ relint Δ is not used. If the authors do not want to claim this, simply leave the hypothesis.
4. H65 cut count: ≤ 2n−1, or ≤ n−1 in the pointed case, with W2. Cosmetic.
5. X65 §0 item 3 / Lemma 2D.1: "fails to witness iff it contains X" holds under the normalisation X ⊇ int ℝ²₊.
6. Both: Cor H.2 must carry the auditor's scope corrections (§4 above), in particular "exactly the full-dimensional K with K′ ⊆ relint K on a fixed U".

---

## 6. Files (`ref65hB_py/`)

| File | Content |
|---|---|
| `geo3.py` | independent exact cone moments (e^{−\|h\|₁}), polygon clipping, Q-polygons |
| `momcheck.out` | 200/200 agreement with `es64py/cones.py` |
| `np_lineality.py` / `.out` | Example NP: failure of generation without Step 2; success with it; X65's shrink on NP |
| `shrink_algebra.py` / `.out` | adversarial exact test of X65 Steps 4–5 (3801 cases, sharpness 0.5016); τ = 0 control |
| `e2e.py` / `.out` | 7 named adversarial rivals: X65 end to end (7/7); H65 Step-2 path on non-pointed hulls (3/3) |
| `e2e_random.py` / `.out` | 36 random adversarial rivals (32 direct) |
| `notch_pi_scan.py` / `.out`, `notch_pi_refine.py` / `.out` | the 4 search misses resolved (36/36) |
| `rerun_h65_examples.out` | H65 `examples.py` re-run: identical |
| `rerun_h65_hunt3_final.out` | H65 `hunt3_final.py` re-run, partial: 2/30 rivals, identical (see note below) |
| `rerun_x65_two_world.out`, `rerun_x65_surround3d.out` | X65 scripts re-run: identical |

**Note on the hunt3 re-run.** At the lead's instruction, I stopped the re-run of H65's `hunt3_final.py` early.
- Each rival takes several minutes.
- These runs illustrate H65's construction; they are not part of its proof.
- Before I stopped it, the re-run covered **2 of the 30 rivals** (deephole #1 and #2). Both were CERTIFIED, and their output lines are byte-identical to `h65py/hunt3_final.out`.
- I did not re-run the other 28. Their status rests on H65's own outputs and on my review of `construct.py`'s exact verification logic (H12), which is sound.
- **None of the verdicts above depends on these runs.**
