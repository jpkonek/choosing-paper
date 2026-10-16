# N7: referee report on N5_notes.md and N6_notes.md (permitted negligible-stakes ties, BRIEF4)

13 Oct 2026. Independent referee. I wrote neither note and assumed nothing in them correct until checked.

**Read.** BRIEF–BRIEF4; Consolidated Statements; N4_referee; R18_referee; R15_notes §§1–6, 9; N2 §§1–3, 7; N3 §§1–2, 4; N1 §2.3; R10b §§1–3; R1 §§1–3; R10a Thm V (statement).

**Verdicts.** CORRECT / CORRECT WITH REPAIR (the statement stands after the local fix given) / GAP / FALSE.

**Scripts.**
- Reran `n5py/thetax.py`, `tie_system.py`, `geom_check.py`, `n6py/theta1.py` and `dl_certificate.py`. All outputs match the notes: θ_x, Θ_NT, x±, Λ ∈ [0.0504, 3.7978], 0 hull failures, and 136/400 and 373/400 DL certificates.
- New: `n7py/referee_checks.py` (output in `referee_checks.out`). It runs five checks:
  - (1) the Euclidean window Θ_NT < θ_x, and the band status of x₀ = r − s𝟙 inside it;
  - (2) Lemma 4.2's sign–rank claim, on 300 random (triangle, p\*) cases;
  - (3) N6's NT(a) path on 250 inner points, including N5's example (0.1, 2, −0.3);
  - (4) the algebra of Thm V′;
  - (5) the hull construction of N5 Prop 3.2 at a crossing, on 20000 collar points.
- All of these are evidence only.

---

## 0. Summary table

| Item | Verdict | Note |
|---|---|---|
| **N5** Lemma 2.1 (weak signs) | CORRECT | |
| N5 Lemma 2.2 (vertex-uniform acceptance; "centre" construction) | CORRECT WITH REPAIR | A_i° is open and upward closed but **not conic** in general: ties at tg are unrelated to ties at g. Drop "conic". Nothing uses it. |
| N5 Lemma 3.1 (VT) | CORRECT | Same mechanism as N6 Lemma DL |
| N5 Lemma 3.1 applied at a crossing (inner side strict if outer quarter-ball strict) | CORRECT WITH REPAIR | Replace B(w, δ/3) by B(w, δ/C), with C depending on v_k. Otherwise exact |
| N5 Prop 3.2 (outer collar) | CORRECT | Hull estimate re-derived; 20000/20000 numerical checks |
| N5 Thm 3.3 (NT) | CORRECT WITH REPAIR | Corner-ray outer clause needs θ < φ_i(r) = Θ_NT (Euclidean), which is **strictly below** θ_x. For θ ∈ [Θ_NT, θ_x) the point x₀ = r − s𝟙 is a band point and may be tied. The clause is then a GAP. The facet and crossing parts hold for θ < θ_x |
| N5 Cor 3.4 (inner ties "deep") | CORRECT, not sharp | N6 NT(a) is right: inner ties are null on all of D. N5's "residual inner freedom" reading is wrong (§3(iv)) |
| N5 Prop 3.5 (anchoring of every coherent world-i-optimal model) | CORRECT | Both routes, (X_ik) and (DF)+(ND). The directional-limit version needs no (S) and no boundary-prior coherence |
| N5 verdict on the coordinator's sketch | CORRECT | The collar alone admits the contact ν(v_k + c′e_i) |
| N5 Prop 3.7 (closed choice) | CORRECT at CHECKED level | Shape-free reading of N3 CC_θ / N1 Thm 3.1. Not used by any no-go |
| N5 Thm 4.1(a), (b), (d) | CORRECT | Verbatim from R15 |
| N5 Thm 4.1(c) with Lemma 4.2 (λ_{ik} > 0 by sign–rank) | CORRECT | Re-derived. Holds for **every θ**, with no UVN. 0 of 600 zero patterns survive the weak signs |
| N5 Prop 4.3 (ties cannot touch facets under (DF)+(ND)) | CORRECT | Holds pointwise: no tie accumulation at any facet point with h_i > 0 |
| N5 Prop 4.4 (no kinked solution with inner-tied, outer-strict) | CORRECT (as scoped) | Excludes that configuration only. Outer horn ties beyond the collar remain |
| N5 Lemma 4.5 (box under ties) | CORRECT | R18's line(p\*, e_b) route, used for both signs |
| N5 Thm 5.1 (R15 Thm 6.2 for permitted ties, every θ > 0) | CORRECT | My own step-by-step re-check is in §4. No (S) needed |
| N5 θ_x formulas | CORRECT as formulas | θ_x is the threshold for (X_ik). It is **not** the threshold for Thm 3.3's corner clause, nor for the table row "ties … impossible" (see Thm 3.3) |
| **N6** Lemma DL | CORRECT | Any n, any target, any good~silence tie rule; IBU near δ_i only |
| N6 Lemma OT | CORRECT WITH REPAIR | (a) The hull also needs z ∈ N. Make W_A thin enough that the Cσ-neighbourhood of W_A ∩ {σ small} lies in N. (b) Only θ < θ_x is needed, not θ < Θ_NT |
| N6 Theorem NT (a) | CORRECT | Also holds for θ < θ_x via N5 Prop 3.2 |
| N6 Theorem NT (b), (c) | CORRECT for θ < Θ_NT | The corner neighbourhoods C_r need (T-i) |
| N6 Theorem V′ | CORRECT | Algebra re-derived and checked numerically. Uses a coherent e_i-Bayes model from (LA)+(S) via R1 Lemma 1.3(a), which survives ties |
| N6.5 / Cor TR (i): R15 Thm 6.2 for θ < Θ_NT | CORRECT, not sharp | N5 gives every θ. One wording slip: c_k(w)_a = λ_{ak}w_a holds on one of the two b-crossing facets only; on the other, the sign comes from the third-coordinate row with μ > 0 |
| N6.5 / Cor TR (ii): N3 PL_θ | CORRECT WITH REPAIR (justification) | "Permitted ties are a subset of the forced ties" is not a valid reason. The valid reason is that PL_θ's proof uses no exact tie (c_i = 0) anywhere, only off-band strictness and strict badness (N4 §4) |
| N6 Θ_NT formulas (N6.7) | CORRECT | t\* = (κ²+1)/κ and the corner value re-derived by hand |
| N6 §8 horns, §9 scope | Labelled CHECKED/CONJECTURE; not load-bearing | "R10a Thm V holds with N replaced by its inner part" was not verified |
| Discrepancy (iv): N5 Cor 3.4 vs N6 NT(a) | N6 is right | Immaterial to the conclusion; it only removes a freedom N5 thought might remain |
| "R15 Thm 6.2 transfers verbatim" (v) | CONFIRMED, every θ > 0 | Via N5's route. N6's route covers θ < Θ_NT |
| Overall conclusion (vi) | JUSTIFIED WITH CAVEATS | §5 |

No item is FALSE.

---

## 1. Standing conventions (checked once)

- **Permitted-tie signs.** For an orientation h with + and 0 in its advice range, put c = ℓ(0) − ℓ(+). Then:
  - c_l ≥ 0 if h is band-l⁺;
  - c_l > 0 if h_l > θ‖h‖, or if h is unanimous;
  - c_l < 0 if h_l < 0.

  If − is also in the advice range, c′_l < 0 where h_l > 0, so d_l = c_l − c′_l > 0 there. Good vs bad is never tied. This is BRIEF4 in additive form.
- **IBU and its consequences.** IBU gives joint continuity of P(q, h) (R1 Prop 3.1) and R10b (1.1), using IBU only. It also gives R1 Lemma 3.5 for pairs in N. That lemma needs only K_q ∩ K′ ≠ ∅ near p\* and the advice range {+, 0, (−)} from (LF), not R1 Prop 2.4(ii), which uses vertex uniqueness. N5 §2 says this correctly.
- **Interior p\*.** N1 Prop 2.3 holds under permitted ties, since it uses only strict badness.
- **IBU itself.** (C) forces IBU only for θ < 1 (sup) and θ < 1/√3 (Euclidean). For larger θ, IBU is requirement (i) of BRIEF2. Both notes say so.
- **Inherited convention: N taken to be an open cone.** This comes from R10a §1, as repaired in R12. It is not literally implied by (LF), since N may thin out at large or small |h|. Every argument here is local in h, and D_{K_q} is conic, so all proofs localise to balls around the relevant points. Harmless.

## 2. N5, item by item

### Lemma 2.2. CORRECT WITH REPAIR
- **Argument.** Accepting g is the strict world-i optimum on B₀: it beats 0 because c_i > 0, beats −g because −g is bad at i, and beats ×. So the radius r(g) > 0 is measurable, and μ(B₀ ∖ B_q) ≤ μ{g ∈ B₀ : r(g) ≤ |q − e_i|} → 0 *uniformly in |q − e_i|*. This yields a full neighbourhood V and needs no sequences.
- **Half-ball step.** It needs a lower bound on the measure of half-balls of sub-balls. That bound is uniform for sub-balls of radius ≥ ρ/2, which is what "centre-ball point" means.
- **Upward step.** P(q, h) ≥ P(q, x) + min_l (h − x)_l holds because K_q ⊆ Δ.
- **Repair.** A_i° is open and upward closed. It is *not* conic: the tie set at tg is the designer's free choice, so tB₀ need not be strict. It is conic when B₀ is off-band. I checked every use of A_i° (Lemma 3.1, application at a crossing, Cor 3.4, Prop 3.5). All are pointwise, and none uses conicity.

### Lemma 3.1 (VT). CORRECT
- **Fubini.** Fubini is legitimate. {(h, q) : q ∈ R(h)} is measurable, because R(h) is defined by affine inequalities with measurable coefficients. {(h, q) : h ∈ D_{K_q}} is measurable, because P is jointly continuous. And B_q ≈ D_{K_q} for every interior q.
- **The tied prior set.** For a tied h, {q = (1−s−t)e_i + s e_l + t e_m : 0 < t < s|c_l|/max(c_m, 1)} is a non-null subset of V ∩ int Δ with c·q < 0. So h is in the exceptional null set.
- **Advice ranges.** "+ and 0 in the advice range" is a hypothesis on h, and the centre balls lie in N. No use of the advice range outside N.
- **Relation to N6 DL.** This is the same lemma as N6 Lemma DL. DL uses a single prior q(s, α₀) instead of Fubini.

### Application at a crossing. CORRECT WITH REPAIR
- x⁻ = h − (τh_i, s, s) lies outside cl D, with x⁻_i > 0 and h − x⁻ ≫ 0.
- |x⁻ − w| ≤ |h − w| + O(v_k·h + τh_i). So "B(w, δ/3)" must be B(w, δ/C), with C depending on v_k, for x⁻ to land in O⁻.
- This is cosmetic. The configuration "inner tied, outer strict near w_{ik}" is impossible for every θ.

### Prop 3.2 (outer collar). CORRECT
Re-derived step by step.
- **Step 1, vertex pull.** This is N2 Lemma 2 with "c_i(x) > 0" in place of "off-band". The proof needs only δ_i ∈ R(x).
- **Step 3.** The inner set U⁺_i is open and convex. Its tied points are transported by N2 Lemma 1(a) (tie-free at p\* a.e.). Its strict points contain [δ_i, p\*] in their convex chart.
- **Step 4, the hull estimate.** With c′ = |v_k·x₀|/(4x₀_i) and λ = 2σ/|v_k·x₀|:
  - λx₀_i < y_i/2, so z_i > y_i/2 > 0;
  - v_k·z = σ/(1−λ) > 0;
  - |z − w| ≤ ρ(1 + |y − x₀|/(2x₀_i)), small once ρ is chosen after x₀;
  - v_l·z > 0 near w.
- **Step 5.** This uses N ∩ (−cl D) = ∅ and N2 Lemma 1(b) for a fixed q. That is a.e. legitimate.
- **Numerics.** `referee_checks.py` (5): 20000 collar points, 0 failures.

### Theorem 3.3. CORRECT WITH REPAIR
- **Facet points with h_i > 0.** The slab comes from Prop 3.2. The inner side follows from Lemma 3.1, since inner h dominates slab centres h − σ𝟙 with σ ∈ (v_k·h, v_k·h + c′). CORRECT for θ < θ_x.
- **Corner rays, inner side.** Positivity: a tied h would have c ≤ 0 with negative entries, so it would be rejected at p\*. CORRECT for every θ.
- **Corner rays, outer side.**
  - The hull uses x₀ = r − s𝟙 as a *strict, vertex-pulled* point. That needs φ_i(x₀) > θ, i.e. θ < φ_i(r) = (κ+1)/√((κ+1)²+2) = Θ_NT (Euclidean).
  - Θ_NT < θ_x strictly, because r ∈ cl F_k and the facet maximum of φ_i is attained in relint F_k (N4). Values: 0.9185 vs 0.9282 at ε = .3, and 0.8364 vs 0.8371 at ε = .05.
  - For θ in this window, x₀ is a band point (`referee_checks.py` (1)), and the designer may tie it.
  - No other strict point with acceptance in the advice range is known to help. One would need x with x_i > 0, v_k·x < 0 and v_j·x < 0 that is strict. Inside N, such points exist only near r, where φ_i ≈ φ_i(r) ≤ θ. Outside N, acceptance need not be in the advice range: the advice range may be a singleton (every evaluable model gives the same advice).
  - So the outer corner clause is a **GAP for Euclidean θ ∈ [Θ_NT, θ_x)**. Sup norm: no change.
- **Downstream.** Cor 3.4 is unaffected, because a.e. b avoids corner rays and the facet slab is pointwise. Prop 3.5 and Thm 5.1 are unaffected.
- **Wording.** The §5 table row "ties next to crossings, unconditionally impossible" must say "except in the outer horns". N5 §3.2 says so; the table does not.

### Cor 3.4. CORRECT, but not sharp; see §3(iv).

### Prop 3.5 (anchoring). CORRECT
- **C_{e_i}.** Competitiveness on {i} against M_L gives pointwise world-i optimality a.e. Otherwise one could splice in better advice on a non-null set, giving a strict improvement at world i, since this happens off the tie set. So (α) and (β) hold. Because of the ties, good and silence are both world-i optimal on τ_i.
- **Directional limits W = lim K_{q_n}** (Blaschke subsequence).
  - D_{K_{q_n}} → D_W in measure, because ∂D_W is null.
  - (α) in the form D_W ⊇ A_i° follows from Lemma 2.2.
  - (β) holds because silence (in the advice range in N) beats acceptance at e_i with a gap.
  - This route needs no (S), no vertex uniqueness and no boundary-prior coherence. It is the cleanest source of V1.
- **Step 2 under (X).** y = w + αf − βv_k/|v_k|² with y_i = h_i/2 and β < c′h_i/2. Then h − y ≫ 0 for ρ ≪ t, since α = O(h_i) = O(ρ), and y lies in the collar W.
  - The admissible ball around y shrinks as h_i → 0. This is harmless, because Lemma 3.1 and Lemma 2.2 are applied pointwise.
- **Step 2 under (DF)+(ND).** The unique cluster at y ∈ relint F_k has ĉ_i ∝ λ_{ik}y_i > 0 (Lemma 4.2). Hence c_i > 0 at a.e. point of a small ball around y: otherwise a sequence of good points would produce a cluster with ĉ_i ≤ 0. There is no circularity: Lemma 4.2 does not use anchoring.
- **Step 4.** h₀ ∈ ∂D_W. A minimiser m ∈ W of m·h₀ = 0 satisfies m·d ≥ 0 for all d with d_i > 0, so m = e_i.
- **Consequences.** V1 follows for every i: a set E accepted by every evaluable model satisfies E ⊆ every B_{q_n}, so E ⊆ cl D_W ⊆ {h_i ≥ 0}. R10b Lemma FS follows from V1 and strict badness alone, and good~silence ties never enter it.
- **Wording.** "R10b Cor V2 fails" should read "is not available (and fails in general under ties)". R15 does not use V2.

### Prop 3.7 (closed choice). CORRECT at the CHECKED level
- Under permitted ties, F_i = argmin_R y_i is a compact convex face of any dimension ≤ 2.
- N3's blow-up uses only:
  - strict convexity of G_r on F_i (y_i is constant there);
  - the inequality G_{r_m}(x_m) ≤ G_{r_m}(y\*);
  - R14 Thm A;
  - CCIBU's interior and edge lsc lemmas.
- Edge priors where both edge worlds are tied are handled by CCIBU's secondary minimisation of the omitted coordinate: the advice is bad there, so the choice is unique.
- No no-go uses this proposition.

### Thm 4.1(a), (b), (d). CORRECT
- (a): concavity in h plus two-sided (DF).
- (b): Lemma C. Its non-constancy needs only weak mixed signs: ĉ ∝ 𝟙 is incompatible with ĉ_l ≥ 0 on P(h) and ĉ_l ≤ 0 on N(h) unless ĉ = 0.
- (d): no signs at all.

### Lemma 4.2 and Thm 4.1(c). CORRECT; this is the key new step
- **Setup.** c_k(h) := (Γ_k h·(e_l − p\*))_l satisfies c_k(h)·p\* = 0 and c_k(h)|_{𝟙^⊥} = Γ_k h. So ĉ_k(h) ∝₊ c_k(h), and the cluster's i-entry has the sign of λ_{ik}h_i.
- **Weak signs give μ ≥ 0.** Under (ND), {h_i > 0} ∩ relint F_k minus ker Γ_k (at most a ray) is nonempty, so μ_{ik} ≥ 0.
- **μ_{ik} = 0 forces μ_{jk} = 0.** If μ_{ik} = 0 < μ_{jk}, then at h ∈ relint F_k with h_j < 0 the cluster has k-entry −μ_{jk}h_j/p\*_k > 0 while h_k < 0. That contradicts strict badness at k. So μ_{jk} = 0, Γ_k = 0, and (ND) fails.
- **Scope.** Needs all-facing (h_k < 0 on relint F_k) and C_k = {i, j}. Uses no strictness at any positive coordinate, so it holds **for every θ > 0**.
- **Lemma 3.2 (nonsingularity).** It then follows verbatim.
- **Numerics.** `referee_checks.py` (2): 600 zero patterns, on T1 and on random strictly all-facing triangles, all violate the weak signs. An earlier apparent exception came from coarse sampling of the all-facing test in my own sampler and disappeared with fine sampling.

### Prop 4.3, Prop 4.4. CORRECT
- **Prop 4.3.** It is even pointwise. A sequence of good tied points converging to h ∈ relint F_k with h_i > 0 gives a cluster with ĉ_i = 0, while the unique cluster has ĉ_i ∝ λ_{ik}h_i > 0.
- **Prop 4.4.** It excludes exactly "inner tied, outer strict" (by Lemma 3.1, with no derivative needed) and two-sided ties (N2 Thm B, tie version, at a facet point with w_i > 0 near the crossing). The outer horn beyond the collar is not excluded. N5 states this.

### Lemma 4.5 (box). CORRECT
- **Strict signs of Λ.** Γ_k w ≠ 0 at both b-crossings (nonsingularity). The zero line of the cluster is line(p\*, e_b) ∌ e_a, so each weak sign is strict. This uses no strictness at world a.
- **Steps 1–4.** These use first-order charts with λ_{bk′} > 0, plus (NA_w). Ties are irrelevant there: unique clusters already forbid tie accumulation at the witnesses A and B, which have A_b > 0 and B_a > 0 and lie in relint facets.
- **Step 5.** Lemma FS via Prop 3.5.

### Thm 5.1. CORRECT. See §4 for my step-by-step re-check.

### θ_x formulas. CORRECT as the (X_ik) threshold
- Sup: θ_x = 1. On F_k, φ_i = 1 on an open arc near r_{kj}, so (X) holds for every θ < 1.
- Euclidean: θ_x = √((κ²+1)/(κ²+2)), attained at t\* = (κ²+1)/κ < κ+1. Re-derived; inf over ε is √(2/3).

## 3. N6, item by item

### Lemma DL. CORRECT
- **Step 1.** Uniform V comes from dominated convergence plus the half-ball argument. Use Lebesgue density, which has the same null sets as Gaussian measure.
- **Step 3.** c(h)·q(s, α) = s[(1−α)c_k + α u·c] < 0 for α < α(h). The single prior q(s, α₀) ∈ V gives E₂ ⊆ D_{K_q} ∖ B_q, which is null.
- **Hypotheses used.** Only IBU at that q, and strict badness at k. The advice ranges enter through the definition of Θ_i and S_i: + and 0 are in the advice range, or (for S_i) every evaluable model accepts.

### Lemma OT. CORRECT WITH REPAIR
- **Steps 1–4 and 6.** CORRECT. N need not be convex: (F1) needs convexity of D_{K_q} only.
- **Step 5.** z = (h − λx)/(1−λ) satisfies z_i > 0 (since λx_i ≤ 2σ/τ < h_i), v_k·z > 0, and v_l·z > 0.
  - z must also lie in G ⊆ N. Repair: |z − h| ≤ Cσ, so choose W_A so thin, relative to N's thickness along the compact A ∩ S², that this neighbourhood lies in N.
- **Threshold.** Only (T-ii) is used, i.e. θ < θ_x. The statement's θ < Θ_NT is unnecessarily strong.

### Theorem NT. CORRECT
- **(b), (c).** CORRECT for θ < Θ_NT, which (T-i) needs for the corner neighbourhoods. The horn description Hor_{ik} is right.
- **(a).** CORRECT.
  - Generic d ≥ 0 with d_i = 0 avoids the finitely many corner directions in the 2-plane.
  - The exit point w″ has w″_i = a − η ≥ 3a/4 > 0 and lies in relint F_k with k ≠ i.
  - The shallow exterior x⁰ is strict a.e. by OT (or by N5 Prop 3.2), and h ≥ x⁰ on B(h⁰, η/2).
  - `referee_checks.py` (3): 250 random inner tied candidates, including N5's (0.1, 2, −0.3), all reach a facet exit with w″_i ≥ 3a/4. For instance, (0.1, 2, −0.3) exits at (0.075, 1.875, −0.853) on F_3.
- No circularity: OT does not use (a).
- (a) holds for θ < θ_x, not only θ < Θ_NT, because N5 Prop 3.2 provides the shallow strict slab at any facet point with w″_i > 0.

### Theorem V′. CORRECT
- **Step 1.** Uses NT(a) only near w, and (F1). Silence is in the advice range in N.
- **Step 2.** h_δ = w + cδn − δe_i is inner, since P_T(h_δ) = δ(c − v_{k,i}) and P_T = v_k·h near w. Also (h_δ)_i = −δ.
- **Steps 3–5.** V ⊆ {m·w ≥ 0}, because w ∈ cl D_V. w^⊥ ∩ aff Δ = line(e_i, v_k). The bound a ≤ 1/(c + 1 − v_{k,i}) is confirmed numerically to 6 digits (`referee_checks.py` (4)).
- **The model D_V.** It is a coherent e_i-Bayes model from (LA)+(S) via R1 Lemma 1.3(a). That KKM argument uses only (S) and completeness of additive rankings, not strictness. It is C_{e_i}, not a "boundary-prior Bayes model is coherent" assumption.

### N6.5 Cor TR. CORRECT (i); CORRECT WITH REPAIR (ii)
- **(i)** is correct for θ < Θ_NT, by UVN(a) at an off-band facet point and V′. It is superseded by N5 Thm 5.1, which holds for every θ.
  - Wording: in the Λ-signs, only one b-crossing facet has a ∈ C_k. On the other (F_a), c_a(w′)_a = −μ_{ca}w′_c/p\*_a < 0, again by μ > 0.
- **(ii)** The reason given ("subset of the forced ties") is wrong as logic. Permitted ties are not forced ties, and N3's forced-tie arguments that use c_i = 0 (cevian charts, Prop A) do not transfer. PL_θ transfers because its proof (R10b Thm PL plus N3's off-band modifications, as checked in N4 §4) uses only off-band strictness and strict badness, never c_i = 0.

### Θ_NT formulas. CORRECT
Sup: Θ_NT = 1. Euclidean: (κ+1)/√((κ+1)²+2), which is 0.9185 at ε = .3. Θ_NT < θ_x for every ε ∈ (0, 1).

### N6 numerics (§7). Reproduced (DL certificates). These are evidence only. The horn design S3 fails at 12 of 166 priors, which says nothing general.

## 4. Cross-cutting checks (i)–(vi)

### (i) Advice ranges
I checked every use of an advice range in both notes. The centre balls (Lemma 2.2, OT's B\*), the cutting points x (Prop 3.2, OT), the inner regions G and U⁺_i, the collar W, the disc B(h₀, ρ), the witnesses of Lemma 6.1 and the near-vertex points of V′ all lie in N. There (LF) gives + and 0, and N ∩ (−cl D) = ∅.
- Points outside N enter only as tied orientations, where "+ and 0 in the advice range" is part of the definition of τ_i or Θ_i. They also enter as "dominating" points h in Lemma 3.1 / DL, where only the advice range of h matters.
- Advice that every evaluable model gives enters only through V1 / Lemma FS, and are handled there.
- The one place a needed strict point with acceptance in the advice range may not exist is the corner clause of N5 Thm 3.3 in the Euclidean window (§2).
- No argument needs a kind of advice that the domain need not put in the advice range.

### (ii) a.e. / Fubini
These are sound: Lemma 3.1 (joint measurability as above), Lemma 2.2 and DL step 1 (uniform dominated convergence), Prop 3.2 and OT (single fixed q; tie-free at p\* a.e.), the "good h" of (1.1), and the directional-limit (α)/(β).

### (iii) Silent imports
- **Strictness in the band.** Used only at N5 Thm 3.3's corner (repair above) and at N6 TR(i)'s λ > 0 (legitimate for θ < θ_x, which is N6's stated range).
- **Hausdorff continuity of K_q at vertices.** Not used: N5 and N6 both use directional limits or C_{e_i}.
- **Coherence of boundary-prior Bayes models.** Not used. N6 V′ uses the existence of a coherent e_i-Bayes model from (LA)+(S), which is legitimate. N5 needs not even that.
- **Bayes-at-index selection.** None.
- **(S).** Used only in N6 V′ (as an axiom) and in N5 Prop 3.5's C_{e_i} branch. N5 Thm 5.1 needs no (S).

### (iv) N5 Cor 3.4 vs N6 NT(a)
- **N6 is right** for θ < θ_x (Euclidean) and θ < 1 (sup): inner ties are null on all of D_{T1}.
- N5's Cor 3.4 is a true but weak sufficient condition. It lowered along 𝟙, which also lowers h_i. N6 lowers only the other coordinates, so the exit point keeps w″_i ≥ 3a/4.
- N5's own Lemma 3.1 plus Prop 3.2 prove the stronger statement along N6's path.
- So N5's "inner points with h_i ≤ min_k v_k·h are a usable freedom" (§3.3, §5 "Net") should be deleted.
- It does not matter for the conclusion. It only shrinks the residual tie freedom near and inside D to the outer horns (plus ties far outside, and reversed orientations).

### (v) R15 Thm 6.2, step by step, in the permitted-tie class (my own check)

| R15 ingredient | Strictness used in R15/R18 | Status under permitted ties |
|---|---|---|
| (SH): Q (R1 L3.5), (1.1), P jointly continuous, K_{p\*} = T | none beyond IBU, (LF) | unchanged |
| (SH): CCIBU ⇒ (LA), (S), (C); R10b Prop V | vertex uniqueness | not needed. Anchoring comes from N5 Prop 3.5 (directional limits) or N6 V′ |
| Lemma C | strict mixed signs for non-constancy | weak signs suffice |
| Thm 1(a), (b), (d) | none | verbatim |
| Thm 1(c): vanishing at w_{ik} | two-sided signs | weak suffices |
| Thm 1(c): λ > 0 | UVN(a), i.e. strict at an h_i > 0 facet point | N5 Lemma 4.2 (every θ), or UVN(a) off-band (θ < θ_x) |
| Lemma 3.2 | λ > 0 | verbatim given λ > 0 |
| §4 forms, Lemma 4.1 | none | verbatim |
| Λ strict signs (R18 repair) | weak signs plus line(p\*, e_b) | verbatim; Γ_k w ≠ 0 by nonsingularity |
| Lemma 6.1, Steps 1–4 | first-order charts, (NA_w) | verbatim; ties cannot accumulate at the witnesses (Prop 4.3) |
| Lemma 6.1, Step 5 (Lemma FS) | V1, strict badness | V1 from anchoring; badness still strict |
| Thm 6.2, Steps 1–6 | algebra | verbatim |

So R15 Thm 6.2 holds in the permitted-tie class for **every θ > 0**, in both norms, for every all-facing general-position triangle and every interior p\*, under (DF), (ND), (NA_w). IBU is assumed where (C) does not force it. The first-order system and the box are literally the strict ones; `tie_system.py` is reproduced.

### (vi) The overall conclusion

**Justified, in this precise form.** In the additive, decomposable-domain, permitted-tie class:
- **(A) Conditional no-go.** No realisation of T1 satisfies (DF), (ND), (NA_w), for any θ > 0, either norm, any ε, any measurable (target-dependent) placement of ties. PROVED (N5 Thm 5.1, checked here).
- **(B) Unconditional tie localisation.** For θ < Θ_NT (Euclidean) or θ < 1 (sup):
  - ties are null on D_{T1};
  - near ∂D_{T1}, ties lie a.e. in the six outer horns at the crossing rays;
  - inner and two-sided ties next to a crossing are impossible;
  - every vertex model and every directional vertex limit is anchored, so V1 and Lemma FS hold.

  For θ < θ_x the inner statement and anchoring hold as well.

  So none of the specific inputs BRIEF4 hoped to relax is relaxed. Those inputs were the crossing-row positivity, the box witnesses, and vertex anchoring/FS. Small θ is not a loophole.

**Caveats that must accompany it.**
1. **The strict residual is inherited, not resolved.** A realisation must violate (DF), (ND) or (NA_w): escapes (E1)–(E4). The permitted class contains the strict class, so T1 is at least as open here as there.
2. **Horn ties.** Outer ties in Hor_{ik} (tangential to {h_i = 0} at the crossing rays) are not excluded. Nor are outer ties away from N′, or ties on reversed orientations. They do not feed R15's first-order data. It is **not proved** that they cannot help a non-(DF) realisation (N5 §6 CONJECTURE; CONJECTURE N6).

   So "no new route beyond the strict residual" is a theorem only in the (DF)/(ND)/(NA_w) class. Outside it, it is the claim that the permitted residual is the strict residual *plus horn freedom*.
3. **Thresholds.**
   - Unconditional localisation needs θ < Θ_NT. Euclidean: (κ+1)/√((κ+1)²+2), which is 0.9185 at ε = .3 and always > √(2/3). Sup: θ < 1.
   - In the Euclidean window [Θ_NT, θ_x), outer ties near the corner rays are open; inner ties and anchoring still hold.
   - Above θ_x (and sup θ ≥ 1) only (A) is available.
   - None of this is "negligible stakes".
4. **Ranking class.** Additive rankings only. Nothing is claimed for countably sandwiched or general (IB) rankings under permitted ties.
5. **IBU.** For Euclidean θ ≥ 1/√3 and sup θ ≥ 1, IBU is an assumption (BRIEF2 (i)), not a consequence of (C).
6. **Approximation.** Coverage of polygons converging to T1 (R10a Prop M′) is unaffected, since the permitted class contains the strict class. It does not count as exact coverage.

## 5. Requested edits

**N5.**
1. Thm 3.3: restrict the corner-ray outer clause to θ < Θ_NT (Euclidean), or mark it open on [Θ_NT, θ_x). Correct the §5 table rows accordingly, adding "except outer horns".
2. Delete "conic" from A_i° (or restrict it to off-band balls).
3. Delete the "inner points with h_i ≤ min v_k·h remain usable" reading, citing N6 NT(a) or the N6 path with Prop 3.2.
4. Change B(w, δ/3) to B(w, δ/C).
5. Change "Cor V2 fails" to "is not available".
6. State that Thm 5.1 needs no (S) (directional limits), which slightly strengthens R15.

**N6.**
1. Lemma OT: add z ∈ N, and replace θ < Θ_NT by θ < θ_x in OT and NT(a).
2. Cor TR(ii): replace the "subset of forced ties" justification.
3. Cor TR(i): fix the Λ-sign wording.
4. Note that N5 Lemma 4.2 removes the θ-restriction in (i).

## 6. Files
- `n7py/referee_checks.py`, `n7py/referee_checks.out`: checks (1)–(5) above.
- This report: `n7py/N7_referee.md`.
