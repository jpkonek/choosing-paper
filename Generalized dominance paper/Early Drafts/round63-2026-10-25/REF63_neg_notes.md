# REF63-neg: referee report on DC63 (direction-continuous charts) and IN63 (incomplete finite-view branch)

25 Oct 2026. Adversarial referee; I wrote neither note.

Labels: PROVED (proof given or repaired here) / CHECKED (exact computation) / CONJECTURE / NUMERICS.
Verdicts: CORRECT / CORRECT WITH REPAIR / GAP / ERROR.

Scripts are in `ref63neg/`; run with `python3 -I`.
- `dc_checks.py` → `dc_checks.out`: the corner system derived independently; positive controls tested against DC63's necessary conditions; the junction witness recomputed; a local example for the (C2) gap.
- `in_checks.py` → `in_checks.out`: W1–W3 recomputed independently with my own implementation of Σ_cap; the cut-point discriminant and the exact p = 1/4 point; the circulant; Prop 5.1 geometry.
- I re-ran all the authors' scripts. `corner_dir`, `junction_witness`, `sigma_cap` and `capcut_sym` reproduce their `.out` files exactly. `freesign_witness` differs only because it re-prints `sigma_cap`'s output when it imports that module.

---

## 0. Bottom line

1. **Theorem DC holds as a theorem about the four-condition certificate.**
   - The junction lemma, the local-rescaling reduction to REF62's repaired Lemma 4.3, the crossing rows and the projective corner system 2z² − 3z + 2 = 0 are all CORRECT.
   - **GAP: DC63's claim that (C2) is not used is false.** Lemma 4.2-D(c), and everything downstream that needs u·c < 0 outside cl D_K (the outer slopes β > 0, the rank-1 cases of 4.2-D(d) and (e), the outer kink tests inside REF62's Lemma 4.3), needs the tie set {u·c = 0} to be null. (C4) alone gives only u·c ≤ 0 a.e. off D_K.
   - The step is not local. I give an exact local DC-PL field that satisfies (C1), (C4) and (C3) for every q near u, yet has u·c ≡ 0 on an open outer cell (§1.2).
   - **Repair:** add (C2) at the single prior u, which the certificate contains anyway. Then Theorem DC is PROVED. A partial repair without (C2) is in §1.2.
   - REF62's own local dichotomy also assumed (C2) at u, so DC63's import of it already carries this assumption.
2. **IN63's general lemmas are CORRECT:** E1 (including the admissible-chain efficiency), E2 (slab), E3 (free-sign), E4 (rank-deficiency; the alternative used is Stiemke's, not Gordan's) and E6 (limit).
3. **Theorem C is CORRECT.** I checked every step, including the new reduction from weak to strict signs through the priority regions R_v = {φ_v > 0} ∪ {c_v < 0}. It depends on E61 Lemma 3.4 (collar) and Cor 3.2 (box lemma), which are cited as refereed.
4. **Theorem S is CORRECT given C62 Thm 4.1 as repaired by REF62.** Every prior it uses is interior, the efficiency comes from E1(b) with full support on Z_{r−1}, and C62's proof is local to ∂D_K.
5. **The cap analysis (§7).**
   - The algebra of the cut-point system is CHECKED: real positive solutions exist, with the exact point p = 1/4, x = 1, κ = (1,1,−2).
   - Its derivation assumes multi-view face linearity, which IN63 itself lists as unrefereed.
   - §7.3(a)–(b) are CORRECT.
   - §7.3(c) is CORRECT WITH REPAIR: κ_Z is undefined as written, and I supply the missing step.
   - The rotation lemma is CORRECT (local, rank-one case). Cor 7.1 is CORRECT.
6. **Σ_cap witnesses W1, W2 and W3 are CHECKED independently** (exact and robust), and each one's efficiency is properly established.
   - The face claim, that the omitted views eliminate every incoherent minimiser on the face λ¹, was supported only for positive-weight selections. It is true for all efficient points of that face by a bathtub argument (§2.6). CORRECT WITH REPAIR.
7. **Overstatement in IN63's §8 diagnosis: GAP.** It says the off-face failures are "forced" within continuous PL designs, W2-type by Theorem S.
   - Theorem S does not apply to cap (two-level-resolution) designs.
   - Σ_cap is itself discontinuous across the cuts, so it violates §7's (K2) and (K4).
   - For continuous PL cap designs the exclusion is only CONJECTURE 7.2.
8. **Positive controls.** No stated necessary condition in either note is violated by normalised boxes or orthant-planar targets (CHECKED on a box and the cyclic triangle; §3).

---

## 1. DC63

### 1.1 Verdicts by item

**Setting (DC-PL), direction invariance, unit normalisation (§§1–2): CORRECT.**
- Implicit: the chart neighbourhood N must lie inside U. Add this.
- The wall dichotomy is CORRECT: on a rank-2 wall, B M⁻¹ fixes an open set of directions in a plane, so it is a scalar.
- The vertex holonomy is trivial when M w ≠ 0: CORRECT.
- The junction example's facet ratio (2ρ + s)/ρ is not constant: CHECKED.

**Lemma 4.2-D.**
- **(a): CORRECT.** It needs only u·c ≥ 0 a.e. on D_K and u·c ≤ 0 a.e. off it.
- **(b): CORRECT.** The midpoint construction: the open convex C contains balls around x and 2h₀ − x, so it contains a ball around h₀. The radius depends on t, which is harmless.
- **(c): GAP.** It needs a.e. strict negativity off cl D_K ("pick x … with u·δ(x) < 0"). That is (C2) at u, not (C4). See §1.2.
- **(d), rank ≥ 2 case: CORRECT.** The image of a 3-dimensional tangent cone under a rank-2 map spans an arc of directions.
- **(d), rank-1 case, and (e): CORRECT given (c).** For an outer cell or wall they reduce to (c).
- **Consequence "u·M_σ = α_σ v_k, α_σ > 0":** for inner cells it needs only (b). For outer cells it needs β > 0, hence (c).

**Lemma 4.3-D(a), local rescaling: CORRECT, given (c).**
- The κ_i are well defined because every wall at w has rank 2 on its span; rank 0 is excluded by (d).
- The product of the κ_i is 1 because M_{σ₁} w ≠ 0.
- The rescaled field c′ is continuous PL on a conic neighbourhood of the ray w and has the same B_q.
- I re-checked REF62's repaired Lemma 4.3 in this setting:
  - Step 1: the kink test at q = u + tδ′ gives q·d_j ≤ 0, so u·d_j ≤ 0.
  - Step 2: evaluate u(M_{σ₁} − M_{σ_m}) on side 1 of the facet. u·M vanishes on v_k^⊥ for both facet sectors by the Consequence. Every n_j is positive at −e, because each inner half-wall at angle θ_j ∈ (0,π) has σ_j's side containing angle π. So u·d_j = 0.
  - Then δ·d_j ≤ 0 whenever δ·c′(w) < 0 gives d_j = κ_j c′(w), and the two-sided comparison gives κ = κ′ = 0.
  - The outer kink tests need u·c′ < 0 strictly on the outer sectors, again through (c).

**Lemma 4.3-D(b), the junction lemma: CORRECT. Witness CHECKED independently: t/30, t/5, −t/20.**
- ω exists with ω·p = 0 and ω·L_R e > 0, because L_R e ∉ ℝp (rank 2, and L_R w ∥ p).
- On the left, ω·p = u·p = 0 makes the boundary exactly r = 0.
- On the right, the boundary is r = −c_t s with c_t > 0.
- The graph f = min(0, −c_t s) is concave, so its epigraph is not convex.
- The triple P1, P2, midpoint (r-values c_t S/4, −(3/2)c_t S, −(5/8)c_t S against f = −(1/2)c_t S) is right.
- Remark: the lemma survives β_L = 0 as well. Either the left outer cell is rejected (choose the sign of ω·M_{τ_L}n), or it is accepted, and then the accepted set is the complement of a convex wedge of angle < π, which is not convex.

**Lemma 4.3-D(c): CORRECT.**
- Adjacent rank-1 runs share p.
- If every run were rank 1, p would have zeros at both crossings and u·p = 0, so p = 0.
- Corner closure follows from M_σ r_j ≠ 0.

**Lemma 4.4-D: CORRECT.** Weak signs give δ_i(w_ik) = 0. Row i vanishes on ℝw_ik = v_k^⊥ ∩ e_i^⊥. Strictness follows from 4.2-D(d) at w_jk.

**Corner proportionality and the system: CHECKED independently** (`dc_checks.out` §1).
- The cross products are multiples of (1,1,1), so there is one scalar equation per corner:
  - r₁: 3λ₁₂λ₁₃ = 2λ₁₂λ₂₃ + 2λ₁₃λ₃₂, and cyclically.
- In the ratios X = λ₂₃/λ₁₃, Y = λ₃₁/λ₂₁, Z = λ₁₂/λ₃₂, the lex Gröbner basis is {X − Z, Y − Z, 2Z² − 3Z + 2}. The discriminant is −7, so there are no real roots.
- Positive parallelism is automatic, because the first coordinates are −3λ₁₂ and −3λ₁₃.

**Theorem DC: CORRECT with (C2) at u added.** As a statement that DC-PL charts cannot carry the full four-condition certificate it is CORRECT. As stated with only (C1), (C3) near u and (C4), it is GAP.

**§7 scope and the stopping point (corner-ray jumps; the N5 step lemma): correctly labelled GAP.**

### 1.2 The (C2) gap: an exact local example (`dc_checks.out` §4)

**The field.**
- Take w = (−1, −1/2, 3) ∈ relint F₃, e = (1,−1,0), n = (1,1,1), and coordinates h = ρw + se + rn.
- Inner cell (r > 0): c = ρp + rm, with p = (−1,−1,2) and m = (0,0,1).
- Outer cell (r < 0): c = (ρ − r)p.

**What holds.**
- The directions agree on the facet, so the field is DC-PL.
- (C1) holds: 0/400 failures.
- (C4) holds a.e.: u·c = r > 0 inside and u·c ≡ 0 outside.
- For q = u + tω, B_q near w is either the half-plane {r > tρ|ω·p|/(1 + tω₃)} or everything. CHECKED: 0 convexity violations over 60 priors × 40 pairs.

**What it shows.** u·δ = 0 on an open set off cl D_K. The proof of 4.2-D(c) breaks exactly here: every segment from h₀ into D_K stays in the tied cell. So that step cannot be derived from the local hypotheses.

This is not a counterexample to Theorem DC without (C2). A global argument may still exclude such cells. One part of that argument is below.

**Partial repair without (C2) (PROVED here, rank-2 runs only).**
- Suppose a rank-2 facet run has an outer cell τ with u·M_τ = 0 (β = 0).
- Take w₀ in the run, and ω ⊥ L w₀ with a := ω·L e ≠ 0. Put g := ω·M_τ n.
- Inside, the boundary is r = −tas/α′. Outside, acceptance is the t-independent condition κas + rg > 0.
- For a > 0 and each sign of g, B_q is non-convex near w₀ with strict witnesses:
  - g = 0: the union of {s > 0} and a thin wedge;
  - g > 0: the boundary graph is concave at s = 0 for small t;
  - g < 0: the accepted set misses a near-facet outer wedge but contains deeper outer points.
- So β > 0 on rank-2 runs.
- The remaining cases are rank-1 outer cells with u·p = 0 next to rank-1 runs, and outer middle sectors with u·M = 0. They need a global argument, which is not supplied.
- **Recommendation:** state Theorem DC with (C2) at u.

---

## 2. IN63

### 2.1 General toolkit
- **§2, existence.**
  - Single-level: CORRECT (Lyapunov, then maximise Σz over D).
  - Lexicographic: CORRECT. Chains have upper bounds by compactness, using nets. If a view's veto is eventually constant along the chain, its gain is eventually monotone. If not, the limiting veto is strictly smaller than every veto in the chain. Zorn's lemma on the preorder then gives an undominated weak dominator.
- **E1(a), (b): CORRECT.**
  - The representative μ′ ≫ 0 exists, using s₁ ≫ s₂ ≫ ….
  - Each λ^i is constant on F_{r−1}.
  - The climbing step needs λ^ℓ + sλ^{<ℓ} ≥ 0. No uniqueness is needed.
- **E2, slab: CORRECT.** Some reflected pair (y, 2x − y) falls in C × C, so the core of Q₀ is in C, which contradicts the density estimate.
- **E3, free-sign: CORRECT.** It is E1(b) with r = 2, and E2 run inside T.
- **E4: CORRECT.** The alternative used is Stiemke's lemma (L ∩ ℝ^V_+ = {0} ⇔ L^⊥ ∩ ℝ^V_{++} ≠ ∅), not Gordan's. A naming fix only.
- **E5: CORRECT as stated, with its caveat.** The Martínez-Legaz–Singer paper exists (Linear Algebra Appl. 90, 1987), but its use is not needed.
- **E6, limit: CORRECT.** Add: liminf C_n contains int ℝ³₊ and lies in U, so its interior is a coherent cone (C62 Lemma 2.1(c)).

### 2.2 Theorem C: CORRECT

**Step 1.**
- For v ∈ S₀: c_v concave on U and zero on the open D_K gives c_v ≤ 0 on U. The proof is the chord y = (z + εx)/(1+ε).
- R_v is a priority region at j(v): every Y that meets R_v non-null is strictly worse in view v than any model avoiding R_v, so Y is not ⪰ M_{R_v} under unanimity.
- I checked that the unanimity of (WS) views satisfies weak (G), and that (SG) gives strict (G). These are what E61 Cor 3.2 and Lemma 3.4 need.

**Step 2.**
- A Y ⊆ D_K ∪ C that improves every W₀′ gain and every paid veto dominates D_K, because S₀ views tie and unpaid vetoes are 0.
- Lyapunov and separation give (β, α) ≥ 0, not both zero.
- β ≠ 0, because the empty model scores 0 on the vetoes.

**Steps 3–4.** g is concave, hence continuous, and vanishes on ∂D_K∖0. A sum of concave summands that vanishes makes each summand affine on the face.

**Step 5.**
- Crossing rows κ_v h_j hold for the β_v > 0 views.
- Vetoes vanish on every face, because each face has an open part with h_j > 0.
- Values at the ray coincide by continuity.

**Step 6.** The circulant (−3,2,2) has eigenvalues 1, −5, −5 and det 25 (CHECKED).

**Steps 7–8.** Correct: the chord argument and the open set D_K ∩ {h_j < 0}.

**Scope remarks.**
- The theorem needs concavity of each gain on all of U, used in Step 1.
- The Corollaries (i)–(iii) follow.
- It is not in tension with VB, box or orthant-planar positive results: Steps 5–6 use the reversed triangle's two crossings per face and the circulant.

### 2.3 Prop 5.1 and Cor 5.2
- **Prop 5.1: CORRECT.**
  - r₃ = (2,2,−3) lies in the open orthant (+,+,−) with v₁·r₃ = v₂·r₃ = 0, so D_K ∩ σ₃ is not a half-space (CHECKED).
  - Every boundary point of the strictly convex moment zonoid is a unique maximiser.
  - It concerns single-level views only. Say so where the note refers to "the composition-theorem charts".
- **The remark "So the corners r_j must lie on cell walls": CORRECT WITH REPAIR.** It needs either the hypothesis M_σd ∈ ℝ^V_+∖0, or, by Stiemke, λ ≫ 0 with λ·c ≡ 0 on σ, which E2 then kills. With this alternative the remark holds unconditionally under (WS) and (SG).
- **Cor 5.2(a), (b): CORRECT.** Entries of both signs follow from (WS) and (SG) in a mixed orthant.

### 2.4 Theorem S: CORRECT given C62 Thm 4.1 / REF62
- ν ≫ 0 from E1(b), and C is strictly sign-correct a.e.
- For every π ≫ 0, μ_π is admissible at depth r. Its maximiser is efficient (no uniqueness needed) and so coherent. Its ties on T_{r−1} are null by E3(b). It agrees with {π·C > 0} on O.
- Lemma 4.2's blow-up, Lemma 4.3 (repaired) and the corner continuity are local to ∂D_K, so convexity on O suffices.
- Every prior used is interior, including the segments (e_k, u].
- Hypothesis (i) is a strong structural assumption; it is correctly stated as such.

### 2.5 §7, caps
- **§7.2 algebra: CHECKED.**
  - The discriminant is −(4p − 1)(8p − 7), so x is real iff p ∈ [1/4, 7/8].
  - Cut validity requires p < 2/3, since h₂ = 2 − 3p on F₁.
  - At p = 1/4 the face maps h − (Σh)e_k give (1,1,−2) at both (2,1,−2) and (1,2,−2).
  - The dot product is positive on the sampled real branch.
  - NUMERICS for non-symmetric cuts: not re-run.
- **§7.2 as a necessary condition: conditional.** It presupposes the face-linear crossing rows on the face middles for the aggregated used views (the multi-view C62 Lemma 4.3). IN63 lists that step as unrefereed.
- **The exact solution is killed by the rotation lemma.** Along F₁ into the middle, the derivative of the face map is (0,−1,1), which is not in ℝκ. So the claim "the C62 corner obstruction is specific to one-level resolution" holds only at first order. It is not an escape.
- **§7.3(a): CORRECT.**
  - A transverse sign change of δ·c at x gives the union of the H half-plane and a wedge in the cap, an angle > π that does not shrink as s → 0.
  - "Every pair of views of opposite sign" is best read as: c_z/τ is constant on the cut for each omitted z (combine δ_R of either sign with δ_Z = b e_z, b ≥ 0).
- **§7.3(b): CORRECT** (Farkas: c_R ∈ ℝ₊κ_R).
- **§7.3(c): CORRECT WITH REPAIR.**
  - Define κ_Z by c_Z = τκ_Z on the cut, using the previous remark.
  - Then δ_R·κ_R + δ_Z·κ_Z < 0 (with δ_Z ≥ 0) forces rejection of the whole cap, so τ(δ·κ) − δ_Z·ζ ≤ 0. Taking δ_Z = e_z gives ζ_z ≥ 0.
- **§7.3(d):** sketch only.
- **§7.4, rotation lemma: CORRECT** (local; rank-one case; (K1)–(K4), (H1), (H3′)).
  - λ_η ≫ 0, so efficiency holds.
  - The accepted layer outside the cap's face portion is O(η²).
  - The reach beyond the middle is ηtδ·τ_R/β_M.
  - At the midpoint the value is −βΘ(ηt₁) + O(η²) < 0 for fixed t₁.
- **Cor 7.1: CORRECT. CONJECTURE 7.2:** as labelled.

### 2.6 Σ_cap (§8)

**Structure (CHECKED).**
- u·A = (5/2)min_k v_k·h off the caps, and 0 on the caps.
- Sign-structure mismatches in 3 000 random exact points: only 2, both exactly on ∂D_K, which is null.
- D_K is the unique lexicographic maximiser of (λ¹, (0|1,1,1)), since 3Σh + h_k > 0 on the open caps.

**Face claim: CORRECT WITH REPAIR.** The note verifies strips only for selections at μ_B ≫ 0 (E3). The stronger claim, that every efficient model in F₁ is coherent, holds by a bathtub argument (PROVED here):
- On F₁, the score is z = const + Σ_k a_k(𝟙 − 3e_k | 𝟙) + b_k(0 | e_k), with a_k = ∫_{S_k}Σh and b_k = ∫_{S_k}h_k.
- Each b_k enters only B_k.
- For fixed a_k, the unique a.e. maximiser of b_k is a strip {h_k > tΣh} ∩ C_k.
- So a non-strip selection is dominated. Every efficient point of F₁ is T ∩ {h_k > t_kΣh}, which is coherent.

**Witnesses (CHECKED independently, `in_checks.out`).**
- **W2.**
  - Values at ε = 0: 501/2000, 1/20, −199/2000.
  - ε = 10⁻⁶ and 10⁻³ keep the signs. All three points lie in U.
  - It is the E61 lower-prevision defect, and is efficient because the weights are full support.
- **W3.**
  - Values: 1921/20000000, 21/10000, −7/10000. Stable on a 10⁻⁶ box.
  - In the cap the A-part is exactly 0, so acceptance comes only from the omitted (B) weights.
  - It instantiates the rotation lemma with δ = (1/10, −1/10, 0): δ·κ = 0 and δ·τ = 1/10.
  - Efficient because the weights are full support.
- **W1.**
  - Values: μ·c = 2/5 at p, λ¹·c = 1/40 at q (in H′), μ·c = −3/10 at the midpoint in C₃.
  - Efficient by E1(b), since μ_Z = (3,1,1) ≫ 0. No uniqueness is needed.

**Regularity.** A is discontinuous across each cut except at its endpoints. CHECKED: just inside the cap A = (1,1,−2); just on the H′ side A ≈ (3/4, 3/2, −2). So Σ_cap is outside §7's hypotheses (K2)/(K4), and W3 is a rotation-type failure of a discontinuous design.

**Diagnosis paragraph: GAP (overstated).**
- "W2-type failures forced by Theorem S" is wrong scope: Theorem S excludes only one-level resolution.
- "W3-type forced by the rotation lemma" reaches only the pinned branch, which is CONJECTURE 7.2.

---

## 3. Positive controls against the stated necessary conditions (CHECKED, `dc_checks.out` §2)

For the cyclic triangle conv{(1,4,2),(4,2,1),(2,1,4)}/7, and the normalised box with l = (1,1,1), u = (2,3,5), I used the orthant chart c = d_σ⊙h, where d_σ is the facet normal in that orthant.
- **Linear facet maps.** One d per facet, including across the crossing in the cyclic case.
- **Crossing rows.** Positive coefficients (2 in the cyclic case; 3/10 and 5/7 in the box case).
- **Corner seams.**
  - Every corner seam is positively parallel. All corner rays have a zero coordinate.
  - Cyclic: (0,−28,28) ∥ (0,−14,14), and so on.
  - Box: all six corners.
- **Junctions.** No rank-1 runs.

So DC63 Lemmas 4.2-D to 4.4-D and corner proportionality hold for the positive controls, and the obstruction is the reversed triangle's two crossings per face.

IN63's general lemmas (E2, E4, Cor 5.2) are also consistent with these controls:
- ties are null for λ ≫ 0;
- the direction is never constant;
- D_K ∩ σ is a half-space in every mixed orthant, so Prop 5.1 says nothing there.

Theorem C's crossing and circulant steps are specific to the reversed triangle.

---

## 4. Verdict table

| Item | Verdict |
|---|---|
| DC63 unit normalisation, wall dichotomy, holonomy | CORRECT |
| DC63 L4.2-D(a), (b) | CORRECT |
| DC63 L4.2-D(c) (and the outer parts of (d), (e), Consequence β > 0) | GAP: needs (C2) at u; exact local example; partial repair for rank-2 runs |
| DC63 claim "(C2) not used" | GAP (false as a claim about the proof) |
| DC63 L4.3-D(a) (local rescaling + REF62 repaired L4.3) | CORRECT (given (c)) |
| DC63 L4.3-D(b) junction lemma; exact witness | CORRECT; CHECKED independently (t/30, t/5, −t/20) |
| DC63 L4.3-D(c), L4.4-D, corner proportionality | CORRECT |
| DC63 corner system 2z² − 3z + 2 = 0, no real roots | CHECKED independently |
| **Theorem DC** | **CORRECT with (C2) at u** (PROVED); as stated without (C2): GAP |
| DC63 §7 stopping point (corner-ray jumps) | GAP, correctly labelled |
| IN63 §2 existence; E1; E2; E3; E6 | CORRECT |
| IN63 E4 | CORRECT (it is Stiemke's lemma) |
| IN63 E5 | CORRECT as stated |
| **IN63 Theorem C** | **CORRECT** (relies on E61 L3.4, Cor 3.2) |
| IN63 Prop 5.1 | CORRECT (single-level views) |
| IN63 "corners must lie on walls" | CORRECT WITH REPAIR (Stiemke + E2) |
| IN63 Cor 5.2 | CORRECT |
| **IN63 Theorem S** | **CORRECT given C62 Thm 4.1 / REF62** |
| IN63 §7.2 cut-point solvability (p = 1/4, x = 1) | CHECKED (algebra); its status as a necessary condition is conditional on unrefereed multi-view face linearity; the solution is killed by the rotation lemma |
| IN63 §7.3(a), (b) | CORRECT |
| IN63 §7.3(c) | CORRECT WITH REPAIR (define κ_Z) |
| IN63 §7.3(d) | sketch |
| IN63 rotation lemma; Cor 7.1 | CORRECT (local, rank-one case) |
| IN63 Conj 7.2 | CONJECTURE |
| Σ_cap structure; D_K unique lexicographic maximiser | CHECKED |
| Σ_cap face claim (all efficient points of face λ¹ coherent) | CORRECT WITH REPAIR (bathtub) |
| W1, W2, W3 | CHECKED independently; efficiency properly established |
| IN63 §8 diagnosis "failures forced within continuous PL designs" | GAP (overstated; Σ_cap is discontinuous; Theorem S does not cover caps) |
| Positive controls vs stated necessary conditions | no violation (CHECKED) |
