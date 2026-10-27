# REF62: referee report on C62 and A62 (the reversed triangle has no continuous piecewise-linear signed field)

25 Oct 2026. Adversarial referee. I wrote neither note. Labels: PROVED (proof given or repaired here) / CHECKED (exact computation) / CONJECTURE / NUMERICS. Verdicts: CORRECT / CORRECT WITH REPAIR / GAP / ERROR.
Scripts: `ref62py/` (exact `Fraction`/sympy). Each has a `.out` file.

Setting as in BRIEF62:
- K = {m_i ≤ 2/5}, with rays r_j = 2·𝟙 − 5e_j and faces F_k = cone(r_i, r_j).
- Normalise π* = u and write g = u·c. In the cross-section Σh = 1, F_k is the line h_k = 2.

---

## 0. Bottom line

1. **The negative result holds in C62's form.**
   - Statement: no continuous PL field satisfies (1)–(4) with (2), (3) used near u **and on the three segments (e_k, u]** (C62 Thm 4.1).
   - The corner algebra is right.
   - One step in the proof of Lemma 4.3 is mis-justified but repairable (§2).
2. **A62's Theorem A62-1 is false as stated.** Its hypotheses are (1), (2) at u only, (3) on a neighbourhood of u only, and (4).
   - Exact counterexample (§3): a continuous PL field that vanishes on ∂D_K and is **pinned**, meaning B_π = D_K for every π in an explicit neighbourhood of u.
   - That field fails (3) only farther out, at π = (1/60, 1/60, 29/30) on [e_3, u].
3. **The reachable nearby result (PROVED here, §4).**
   - (a) Local dichotomy: A62's local hypotheses force c ≡ 0 on ∂D_K∖0. This is sharp by §3.
   - (b) The vanishing case is then excluded by (3) at generic priors near the segments (u, e_k). This uses A62's own N6/N7 with piecewise-constant data, and needs neither (2) on the segments nor C62's tie step.
   - (a) and (b) together give a repaired A62-1. They also repair C62 §6.3.
4. **The box control passes every necessary condition stated in either note.** I re-ran this independently and exactly: N0, N1 (winding exactly 1, monotone), θ = 1, linear facet maps, no crossings, and C62's checker.

---

## 1. Corner algebra (CHECKED, `ref_corner.out`)

**Facet maps after Lemma 4.4.** On F_k:
- c_i = λ_{ik}h_i for i ≠ k;
- c_k = −Σ_{i≠k} λ_{ik}h_i.

**Continuity at r_1, r_2, r_3.** This gives 9 equations in the 6 λ's.
- The system has rank 6, so only λ = 0 solves it.
- By hand:
  - λ_{31} = λ_{32} = μ_3 (cyclically);
  - 3μ_3 = 2(μ_1 + μ_2) (cyclically);
  - the circulant (3, −2, −2) has eigenvalues −1, 5, 5, so it is nonsingular.

**Direction-only matching** (c_{F_a}(r_j) = κ_j c_{F_b}(r_j), κ_j > 0).
- The corner equations are x + y = 3/2, 1/y + z = 3/2 and 1/z + 1/x = 3/2.
- The only solutions are 3/4 ± i√7/4. They are non-real, and I confirmed the same at p\* = (1/6,1/3,1/2), (1/10,1/10,4/5) and (7/10,1/5,1/10) in μ-form.
- Degenerate normalisations (one λ = 0) also have no real solution.

**Möbius form.** y ↦ 3/2 − 1/y has matrix [[3/2, −1], [1, 0]], with trace 3/2 and det 1.
- T³ = [[3/8, −5/4], [5/4, −3/2]], and cos 3θ = −9/16 ≠ ±1. So no power of T fixes a point of ℝP¹, including 0 and ∞.
- Wording: arccos(3/4) ≈ 41.4° is the angle of the conjugate SO(2) matrix. As a map of the circle ℝP¹ the rotation is 2·arccos(3/4) ≈ 82.8°. This does not matter, because only T³ ≠ ±I is used.

---

## 2. C62

**Lemma 2.1 (reformulation).**
- (a) and (b): CORRECT.
- (c), direction "⇒": CORRECT WITH REPAIR.
  - The given proof ("a coherent cone is closed under addition") treats (C3) as exact equality, but (C3) is an a.e. statement.
  - Repair (PROVED): this uses continuity and strict signs everywhere, which is C62's hypothesis. Suppose π₀ ∈ A, h, k ∈ B_{π₀}, and π₀·c(z) = 0 with z = h + k. Then z ∈ int conv B_{π₀}, so π₀·c ≥ 0 near z.
  - Let T be the cone of admissible perturbations at π₀. If c(z) ∉ T\*, pick an admissible δ with δ·c(z) < 0. For small η, B_{π₀+ηδ} must contain a neighbourhood of z, because it contains small simplices around z. Yet it rejects a ball at z. Contradiction.
  - If c(z) ∈ T\*, strict signs force z_i = 0 on supp π₀ and z ≥ 0, so z − εe_i (i ∈ supp π₀) gives π₀·c < 0. Contradiction.
  - So the strictness clause is automatic in C62's setting.
- Under merely a.e. signs the clause is **not** necessary, as A62 says. Example: c = ψ(h)h, with ψ ≥ 0 continuous and vanishing only on one interior ray z. It satisfies (1)–(3), but π·c(2z) = 0.

**Lemmas 2.2 and 2.3, checker.**
- CORRECT: Tietze–Nakajima applies, and the necessity of (K) is right.
- I re-ran `box_control.py` and `seam_system.py`; both reproduce.
- I did not audit the code line by line.

**Lemma 4.2 (c ≠ 0 on ∂D_K∖0).** CORRECT.
- The blow-up cone P_π is either a.e. full or lies in a half-plane, so a non-null Z(s) contains an arc ≥ π.
- Uniform convergence passes this to s₀.
- Affineness in s gives a non-null tie at π(s₀), which (C2) forbids.
- It genuinely needs (C2) and (C3) on the segments (§3 shows the theorem is false without them).

**Lemma 4.3 (facet linearity). CORRECT WITH REPAIR.**
- The step "continuity of f_u = α v_k·h across an inner half-wall gives α_σ = α_τ, hence d·u = 0" is valid only when both sectors touch the facet.
- At a facet vertex w there can be **middle sectors**, bounded by two inner half-walls, on which g is linear and positive but not a multiple of v_k·h. So the normal slope can jump at w.
  - CHECKED (`alpha_jump.out`): in the §3 field, the inner slopes along F_3 are 19/2, 12, 19/2 on h_1 ∈ [−3,−1], [−1,0], [0,2].
- Repair (PROVED), using c(w) ≠ 0 from Lemma 4.2:
  1. The kink test at q = u + tδ (δ·c(w) < 0), with t → 0, gives u·d_j ≤ 0 for every inner half-wall.
  2. Apply u to M_{σ₁} − M_{σ₂} = Σ_j d_j n_jᵀ and evaluate at a facet point on side 1, where g vanishes for both facet sectors. This gives Σ_j (u·d_j)(n_j·h) = 0 with n_j·h > 0, so u·d_j = 0 for every j.
  3. The outer walls are handled the same way.
- From there C62's argument runs unchanged: d = κc(w), d′ = −κ′c(w), and the facet comparison gives κ = κ′ = 0. The lemma does not need (DF), and it uses (C3) only on a neighbourhood of u.

**Lemma 4.4 (crossing rows).** CORRECT.
- Given facet linearity, c_i(w_{ik}) = 0 follows from continuity and weak signs.
- v_k^⊥ ∩ e_i^⊥ = ℝw_{ik}, so c_i|_{v_k^⊥} = λ_{ik}h_i.
- Lemma 4.2 at the crossing points also forces both λ's on a face to be positive.

**Theorem 4.1.** CORRECT (with the Lemma 4.3 repair). The segment hypotheses are essential (§3).

**Corollary 4.5.**
- The algebra is CHECKED.
- As a theorem about fields that are only direction-continuous: GAP.
  - Lemmas 4.2 and 4.3 use matching values.
  - Corner proportionality for fields that jump at the corners is not derived (A62's N5 step lemma is only a sketch).
  - If the field is just c̃ times a positive scalar, with c̃ continuous, the corollary is already contained in Thm 4.1.

**§6.1 and §6.2.** CONJECTURE, correctly labelled.

**§6.3 (complete veto-then-PL designs).** GAP, repairable.
- The step through Lemma 4.2 ends with "a non-null tie contradicts (C2)". E61 Thm 5.1(d) gives coherence only at null-tie priors and never forbids ties.
- Repair: replace that step by §4(b), which uses only generic priors.

**§7 "(ND) is automatic for PL fields".** ERROR as stated.
- The pinned field has P(u + tδ, y) = 0 for small t, so (ND) fails there.
- It is true once Lemma 4.2's hypotheses hold.
- The other §7 claims are CORRECT: (NA_w) is automatic, (DF) ⟺ no kink across faces, and Λ is undefined.

---

## 3. Counterexample to Thm A62-1 as stated (CHECKED, `ref_pinned.out`, `tjunction.out`)

**Construction.**
- K′ = (u + K)/2, so in the cross-section U₂ = {h_k < 11/3}.
- Subdivide by the six lines h_i = 0 and h_k = 2. This gives 19 cells. Cone each cell from its centroid, giving 75 triangles. There are no T-junctions, so the field is a continuous PL field on a finite simplicial fan.
- Vertex values, with ε = 1/10:
  - c(ρ) = 0 if P_K(ρ) = 0;
  - otherwise c_i(ρ) = sign(ρ_i)·(1 if sign ρ_i = sign P_K(ρ), else ε).

**What holds, all checked exactly.**
- (1) strict signs a.e.: each triangle contains a cell centroid, whose c has the strict sign pattern.
- On N = {|π_i − 1/3| ≤ 1/10}, checked at its 7 vertices since the conditions are linear in π: sign(π·c) = sign P_K on every open triangle.
- So B_π = D_K a.e. for every π ∈ N. This gives (4), (2) at u, and (3) on N.

**Where it fails.** At π = (1/60, 1/60, 29/30), on [e_3, u]:
- h = (−14/5, 7/2, 3/10) has π·c = 11/1200;
- k = (7/5, 1/10, −1/2) has π·c = 1/500;
- h + k has π·c = −137/3000.

All three points are interior to cells and lie in U. This is the mechanism of C62 Lemma 4.2 and of A62 N6/N7.

**What breaks in the proof of A62-1.**
- Step 1: "constant normal slopes by continuity" is false here.
- Step 4: "d_σ is the same on the whole inner layer" is false at crossing points. The h_i = 0 half-line must be bridged by middle cells on which c_i ∝ h_i.
- A62-3 cannot rescue it either. Its hypothesis that d^in is continuous is incompatible with strict signs at crossing worlds for any PL field: d_i^in has opposite strict signs on the two sides of the crossing. So A62's remark "for PL c this is automatic once c ≡ 0 on F_k" is an ERROR.

---

## 4. Repaired statements (PROVED here, modulo routine write-up)

**(a) Local dichotomy.** Let c be continuous PL and satisfy (1), (2) at u, (3) on a neighbourhood of u, and (4). Then c ≡ 0 on ∂D_K∖0.

*Proof.*
- At relint points with c(w) ≠ 0, the repaired Lemma 4.3 makes c linear nearby on the face.
- At zeros, use A62's N2 limit φ_w = −ρ_y(w·c). It is convex: f_ε is the lower boundary function of the convex set B_π, |f_ε| = O(ε), and the limit is taken away from vertices. Here the slopes ρ may depend on the side. Then N4 steps 2–3 run with side-dependent slopes and exclude zero arcs next to nonzero arcs, and isolated zeros.
- So each face is either ≡ 0 or nowhere zero and linear with crossing rows (both λ > 0).
- At the corners, a nonzero face has c(r) ≠ 0. So mixed faces contradict continuity, and all-nonzero faces contradict §1. ∎
- Sharp: the §3 field satisfies every hypothesis.

**(b) Vanishing faces fail at generic priors near (u, e_k).**
- Near relint F_k, c = (v_k·h)d^in_σ on inner face cells and (v_k·h)d^out_σ on outer face cells. The data are piecewise constant.
- Along π_t from u to π′ near e_k:
  - inner acceptance persists, since u·d^in > 0 and d^in_k > 0;
  - each outer cell switches on at t\*_σ, where π_t·d^out_σ = 0, since u·d^out > 0 > d^out_k.
- If t\*_σ ≠ t\*_τ for two cells on the same face, choose t between them with π_t free of non-null ties. That is all but finitely many t on a generic segment. Then N6 (exclusivity) is violated: genuine non-convexity, not a tie.
- If t\*_σ = t\*_τ for every π′ in an open set, all d^out are positively proportional to one n.
- The crossing worlds then force n_i = 0 for both of them, so n ∝ e_k, which contradicts u·d^out > 0 > d^out_k. ∎

**Consequence.** No continuous PL field satisfies (1), (2) at u, (3) on a neighbourhood of u together with (3) at generic priors in neighbourhoods of the segments (u, e_k), and (4). This is A62-1 repaired. It also repairs C62 §6.3, because E61 Thm 5.1(d) supplies coherence at null-tie priors, which is all (b) uses.

---

## 5. A62, other items

**Correct.**
- Lemma 1.1: CORRECT.
- Thm A (the repaired reformulation): CORRECT WITH REPAIR. Add (1) as a hypothesis: (ii) ⇒ (i) yields only convexity, and coherence then comes from Lemma 1.1. The other corrections to the brief are CORRECT (joint-acceptance restriction, strictness, null sets).
- Cor 2.3: CORRECT, conditional on R15 Thm 1, Lemma 3.2 and R18's refereeing. Scope: the (DF)+(ND) class only.
- R15 audit (no use of (S)): CHECKED as far as the files allow.
  - R15's (SH) assumes interior unique coherent Bayes acts directly.
  - (S) appears only as a CCIBU consequence, which R18 confirms.
  - UVN(a) uses strict guidance and interior coherence.
  - I could not read CCIBU or the underlying proof of R1 Prop 3.1.
- N0, N1, N3, N4 (θ typo: φ_{−w} = θ·w·ĉ, not θ⁻¹), N6, N7: CORRECT.
- N2: CORRECT under its hypotheses. Its "λ continuous" hypothesis fails for some PL fields (§2), so its application in A62-1 Step 1 needs the §4(a) argument.
- N5 for continuous fields: CORRECT.
- A62-1′: CORRECT. Its conclusion is c ≡ 0, not a contradiction.
- A62-2: CORRECT. Quantifier: it needs (3) along an open family of segments from u to points near e_k, not along [u, e_k] alone.
- §5 witnesses: CHECKED independently with my own implementations (`ref_witness.out`, `ref_witness_e61.out`).
- §5.5 (box mixtures are boxes): CORRECT.

**Needs repair or relabelling.**
- Dual view: minor imprecision. Redundancy of a generator only over Δ suffices, so "binds coordinatewise" is sufficient but not "iff".
- N5 for discontinuous fields: a sketch, correctly labelled.
- Mixed and one-sided jumps: these should be labelled CONJECTURE (sketch), not CHECKED.
- PMA criterion: minor ERROR. At min π̂ = 1/6, B_π is an open convex cone containing int ℝ³₊ inside U, hence coherent. CHECKED at (1/6, 5/12, 5/12). The criterion for incoherence is "< 1/6".
- §6 (surviving design space): GAP. Its local analysis omits **pinned faces** (c ≡ 0 on ∂D_K with B_π = D_K near u). For PL fields these are excluded only by §4(b) or C62 Lemma 4.2. Cheap filter 3 is not itself necessary, because S2–S4 are alternatives.

---

## 6. Box positive control (CHECKED, `ref_box_nc.out`)

Boxes tested: l = (1,1,1), u = (2,2,2); l = (1,1,1), u = (2,3,5); l = (2,1,3), u = (5,4,4).

Results:
- every extreme ray of D_K has a zero coordinate;
- no face has a crossing;
- g = 0 on ∂D_K;
- c is linear on every face;
- θ = 1;
- the winding number of c in 𝟙^⊥ is exactly 1, and the direction is monotone.

So no stated necessary condition is violated by a known cover. Lemmas 4.3 and 4.4 and N1–N7 are vacuous or satisfied for boxes, and C62's checker certifies all three.

---

## 7. Verdict table

| Claim | Verdict |
|---|---|
| C62 box control (checker) | CORRECT (reproduced; also passes A62's N-conditions) |
| C62 L2.1(a,b) | CORRECT |
| C62 L2.1(c) | CORRECT WITH REPAIR (a.e. issue; strictness automatic under strict signs) |
| C62 L2.2, L2.3 | CORRECT |
| C62 L4.2 | CORRECT (needs segments; essential) |
| C62 L4.3 | CORRECT WITH REPAIR (middle-sector slope step) |
| C62 L4.4 | CORRECT |
| **C62 Thm 4.1** | **CORRECT (after repair)** |
| C62 rank-6 corner system; Möbius | CHECKED |
| C62 Cor 4.5 as a theorem on direction-continuous fields | GAP |
| C62 §6.1, §6.2 | CONJECTURE (as labelled) |
| C62 §6.3 | GAP → repaired by §4(b) |
| C62 "(ND) automatic for PL" | ERROR (pinned field); true under L4.2's hypotheses |
| A62 Lemma 1.1 | CORRECT |
| A62 Thm A | CORRECT WITH REPAIR (assume (1)) |
| A62 strictness / joint-acceptance remarks | CORRECT (a.e. setting) |
| A62 Cor 2.3 (R15: no real corner solution, any interior p\*) | CORRECT (conditional on R15 Thm 1); algebra CHECKED |
| A62 R15 audit (no (S)) | CHECKED as far as files allow |
| A62 N0, N1, N3, N4, N6, N7 | CORRECT; N2 CORRECT under its own hypotheses |
| **A62 Thm A62-1** | **ERROR (false as stated; exact counterexample §3)**. Repaired: §4 |
| A62-1′ | CORRECT |
| A62-2 | CORRECT (quantifier: open family of segments) |
| A62 mixed jumps | relabel CONJECTURE |
| A62-3 | statement CORRECT; "automatic for PL" ERROR |
| A62 §5 witnesses | CHECKED (independent) |
| A62 PMA "≤ 1/6" | minor ERROR (should be "< 1/6") |
| A62 box mixtures | CORRECT |
| A62 §6 surviving space | GAP (pinned faces missing locally) |
| Local dichotomy §4(a) and generic-segment exclusion §4(b) | PROVED here (new; sharp by §3) |

## 8. What is established for the reversed triangle

Within the auditor's continuous PL signed-field ansatz, any finite fan and any K′ fail. The obstruction has two parts.

- **(i) First order at u, the corner seams.** Priors near u force either linear crossing-row faces, which are inconsistent at the corners, or c ≡ 0 on ∂D_K.
- **(ii) Away from u, the vertex segments.** Pinned (vanishing) faces fail by genuine non-convexity at generic priors between u and each e_k. This is not a tie, so relaxing tie conditions does not reopen this branch for PL fields.

Nothing here excludes non-PL, irregular or incomplete designs. The remaining open branches are A62's S1–S4 and C62's §6.4(iii) (incomplete orders with target-paid vetoes). For S1–S4 the pinned branch must now be added explicitly.
