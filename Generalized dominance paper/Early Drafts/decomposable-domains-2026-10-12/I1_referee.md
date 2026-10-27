# I1 referee report: edge pinning, forced supporting lines, and the (Diag) contradiction

14 Oct 2026. An independent, adversarial reading of `I1_notes.md` (all of it), checked against the write-up §§2–5 and
against the sources the note cites: N21 (N21.2, N21.4 item 5, N21.7), N23 §§4, 6, N28 Prop 5.1, N28_referee §5.1,
R4 Thm B and (K4), R8 §8.

I reran every script in `i1py/` that has a `.out` file, and every output was reproduced identically (`i1ref_py/reruns/`).
My own checks, written without importing anything from `i1py/`, are in `i1ref_py/`:
- `ref_symbolic.py` (sympy);
- `ref_t1_window.py` (T1: the full piecewise edge maps, Prop E at m₁₂, the non-failing sets, window admissibility and
  the γ certificate, over 12 values of ε including ε = 1/7);
- `ref_box.py` (the normalised-box system, a genuine CF solution).

Labels: CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.

---

## 0. Verdict

**Theorem I1 is CONFIRMED, at the status of its cited inputs.**

I did not find a gap or an error in any of the new steps. All the repairs below are expository; none changes a
statement.

| step | verdict |
|---|---|
| Normalisations (p\* = u by reweighting worlds; x = x₊ by σ = (1 2)) | CONFIRMED |
| (C1) chart cells, every-q form | CONFIRMED (cosmetic repair R1) |
| (C2) (TS), (PC), (NS), crossing rows, x ∈ {x±} | CONFIRMED as imported (statuses in §8) |
| (C3) unique clusters as **vectors in ℝ³** | CONFIRMED |
| (C4) edge confinement | CONFIRMED as imported |
| Lemma 1 (strict vertex signs) | CONFIRMED (recomputed symbolically) |
| Lemma 2 (edge maps) (a), (b), (c) | CONFIRMED WITH REPAIR (R2: expository, the no-fold step) |
| Explicit facet maps and piece boundaries on [e₁,e₂] | CONFIRMED (sympy and numerics) |
| Prop E (edge limits) | CONFIRMED (repair R3: one omitted parameter) |
| Thm R (c-lines pinned) | CONFIRMED (remark R4 on {+,−} pairs) |
| Lemma S (forced supporting lines) | CONFIRMED |
| Lemma W (window, every ε) | CONFIRMED WITH REPAIR (R5: order of quantifiers) |
| Lemma P | CONFIRMED (repair R6: projective reading at ε = 1/7) |
| Lemma D | CONFIRMED (sympy, exact) |
| Theorem I1, final contradiction | CONFIRMED |
| Corollary (a), (b) | CONFIRMED; (b) at CCIBU status, as stated |
| Corollary (c) (charges) | CHECKED only, as labelled; not refereed here |
| §6 interpretation, "other targets" | interpretation / CONJECTURE, as labelled |
| "the box is not used" | CONFIRMED WITH REPAIR (R7: precision) |

---

## 1. Priority (1): unique-cluster convergence as vectors, at edge priors far from p\*

**What is claimed.** Take good g → ĥ ∈ relint F_k ∩ Σ inside N₀. Then c(g)/|c(g)| → c_k(ĥ)/|c_k(ĥ)| in ℝ³.

**Why it holds.**
- By Lemma B1 (N21.2), for a.e. g ∈ N₀ the chart on B₁ is {c(g)·q > 0} ∩ B₁, where c(g) is the penalty vector.
- That penalty vector is the CF vector c, because (LF) together with Cor TSalways(b) makes the advice range {+,0,−} on N.
- N21.4 item 5 shows that every cluster ĉ of c(g_m)/|c(g_m)| satisfies ĉ·q = κ n_τ·(q − p\*) on all of aff Δ, with κ > 0.
- The reason: q ↦ ĉ·q is an affine function on aff Δ, and aff Δ spans ℝ³ linearly. So a vector in ℝ³ is fixed by its
  restriction to any open subset of aff Δ, here B₁. That restriction is fixed, up to a positive factor, by its zero line
  λ_τ (the cluster line meets B₁ by (TS)) and its positive side.
- The limit vector cannot be ∝ 𝟙, since it has the weak sign pattern of a mixed ĥ.

**The uniform form used in Prop E.** Suppose c_k(ĥ)·q₀ ≠ 0. Then there are δ, ρ > 0 such that sign c(g)·q = sign c_k(ĥ)·q₀
for every good g with |g − ĥ| < δ and every q with |q − q₀| < ρ.

Proof: if not, take sequences g_m → ĥ and q_m → q₀ with the wrong sign. Extract a subsequence on which the normalised
c(g_m) converge. The limit is c_k(ĥ)/|c_k(ĥ)|, so c(g_m)·q_m/|c(g_m)| → c_k(ĥ)·q₀/|c_k(ĥ)| ≠ 0. This is a contradiction.

**Precedent.** The same vector convergence, used at edge priors, already appears in N21.6 Step 1 ("α is affine, so
convergence on B₁ is convergence at q₀"), which N23 §6 confirmed. **CONFIRMED.**

---

## 2. Priority (2): the every-q chart form

**The source.** N28 Prop 5.1(⇒) and N28_referee §5.1 (re-derived there) give the following. For good g:
- R(±g) is open and convex (R1 cells);
- {P(·,±g) > 0} is open and convex (N21.1);
- the two sets are a.e. equal (Fubini plus the Bayes property at every q), hence equal.

The exceptional null set of g does not depend on q. I re-derived "a.e. equal open convex sets are equal": A ⊆ cl B, so
A ⊆ int cl B = B.

**What the note needs.** Thm R, Lemma S and Prop E only need the a.e.-q form together with the continuity of K_q:
- closures of sets of positive measure suffice in Thm R;
- in Prop E, the sequence q_n can be perturbed off a null set using Hausdorff continuity.

So the every-q form is stronger than necessary, and it is available. **CONFIRMED.**

**Cell bookkeeping (checked).** The complement of S = {c ≤ 0, c′ ≤ 0} in the plane is exactly W⁺ ∪ W⁻ ∪ {d = 0, c = c′ > 0}.
The last set meets Ω in the d-face, where K_q ⊆ ℓ_g for a.e. g (R4 Thm B, refereed in R8). This is what Prop E step 3
and Thm R step 2 use.

**R1 (cosmetic).** (C1) should say that on N₀ the advice range is {+,0,−}, by (LF), so the c in (C3) is the CF c. For
{+,−} pairs see R4 below.

---

## 3. Priority (3): Prop E and Lemma 2(a)

### Lemma 1
Symbolic check (`ref_symbolic.out` (a)). Along the F₁ segment from r₃₁ to r₁₂, the quantity xh₂ + h₃ is affine. Its
endpoint values are:
- (x(2+ε) + ε − 1)/(1−ε), which is > 0 iff x > 1/(κ+1);
- ((2+ε) − x(1−ε))/(1−ε) = κ + 1 − x, which is > 0 iff x < κ + 1.

Both conditions hold for x± because x + 1/x = κ + 1. This is a cleaner proof than the case split in the note; the note's
case split is also correct. **CONFIRMED.**

### Lemma 2

**(a), well-defined and endpoints.** CONFIRMED (Lemma 1; crossing rows).

**(a), injectivity: CONFIRMED WITH REPAIR R2.** The note's degree-one sentence is right but compressed. The point to
make explicit is that the chord normal cannot fold back at a corner. The full argument:
- The signs of n·(e_l − u) partition S¹ into six sectors, met in the cyclic order
  (+,−,−) → (+,+,−) → (−,+,−) → (−,+,+) → (−,−,+) → (+,−,+).
- By Lemma 1, F₁ sends n through (−,+,−) → (−,+,+) → (−,−,+). It crosses the whole middle sector, so the direction of
  its strictly monotone rotation is forced.
- F₂ continues from the shared corner through (−,−,+) → (+,−,+) → (+,−,−), in the same direction. F₃ does the same.
- So n is continuous (by (NS)) and strictly monotone in one direction all the way round. This is the degree-one claim.
- On the arc that μ_j uses, h_j > 0 > h_i, so n·(e_j − u) > 0 > n·(e_i − u). This confines n to an open arc shorter
  than π. So distinct t give distinct unoriented chords through u, which meet E in distinct points.

**(b), (c).** CONFIRMED.

**Explicit maps** (`ref_symbolic.out` (b); `ref_t1_window.out` pieces):
- facet 3 on [e₁,e₂]: s = tx/(tx − t + 1);
- facet 1 on E₁: s(0) = (x−1)/(2x−1), s(1) = 1;
- facet 1 on E₂: s(1) = −1/(x−2).

The pieces are F₃ then F₁ on E₁ ("toward e₂"), with the break at t = c₀. On E₂ ("toward e₃", measured from e₃) the
pieces are F₁ then F₂, with the break at 1 − c₀. This holds at all 12 values of ε.

Monotonicity and the endpoints hold on all edges and both orientations. (At ε = 0.995 my script flagged an endpoint only
because the slope at 0 is x ≈ 600. There is no non-monotone step; see the end of the output.)

### Prop E: CONFIRMED (repair R3)

I re-derived every step.
- **Step 2.** c_k(ĥ)_j > 0 > c_k(ĥ)_i by Lemma 1, so c_k(ĥ)·q₀ = (1−s)c_i + s c_j has the sign of s − μ_j(t). The
  uniform form of §1 applies.
- **Steps 3–4.** Correct with the cell bookkeeping of §2: no strict straddle for t < Z_j(s), and min K\* ≤ t for
  t > Z_j(s).
- **Steps 6–7.** Correct, including the case Z_j = Z_i, where K\* = {Z_j}.

**R3 (omitted parameter).** Two parameters t, where h_o(z(t)) is a corner ray (t = c₀ or t = 1 − c₀), are not covered
by (C3), which is stated for relint F_k. They are harmless: both conclusions involve open sets or infima of t.

**Independent tests.**
- At m₁₂: Z₂ = (1−ε)/(2+ε) and Z₁ = (1+2ε)/(2+ε) to 6 digits, non-failing, at all 12 values of ε.
- Non-failing set of each edge: one crossover, at 0.53, 0.597, 0.665, 0.744, 0.862, 0.966 for
  ε = .005, .05, 1/7, .3, .6, .9. It is measured from the vertex where the box holds.
- At the failing ends, the identity value s lies in [Z_i, Z_j], since ω = 1 ∈ [κ/x₊, x₊]. This is consistent with the
  sector cap C1.

---

## 4. Priority (4): Thm R and Lemma S

### Thm R: CONFIRMED

**Quantifiers.**
- Thm R needs a.e. g, satisfying (C1) together with R4 Thm B. Neither null set depends on q.
- It needs y ∈ N_E (an open set), so that Prop E holds at every q₀ ∈ E near y.
- y ∈ S follows because S is a closed planar set and Ω ∩ S accumulates at y. Then c·y ≥ 0 (from cl W⁺) and c·y ≤ 0
  give c·y = 0 and c′·y ≤ 0.
- It applies to every crossing gamble g, not only to near-facet gambles. It needs no regularity.

**R4 (remark).** For a pair with advice range {+,−}, the CF data have S = ∅. Thm R's hypotheses would then put a strictly
straddling prior in W⁺ ∪ W⁻ ∪ F, which is impossible. So a.e. gamble to which Thm R applies has 0 in its advice range.
This is a true by-product; it is not an inconsistency.

**Independent test on the box system** (`ref_box.out` (R)). Over 4484 (gamble, edge) cases with y ∈ N, the c-line of g
passes through μ_o(t) to |c·y|/|c| ≤ 3.6e−16, and c′·y ≤ −3.3e−4.

### Lemma S: CONFIRMED

**Steps 1–4 re-derived.**
- The two μ-images lie on the convex c-ray. The c-line meets Δ exactly in the segment between them, so the whole chord
  ∩ Ω lies in cl(W⁺) ∩ S.
- So P(·,g) = 0 on the chord. The apex is handled by continuity.
- The chords converge to Λ (μ is continuous; y₁ ≠ y₂). Joint continuity of P gives P(q,g_L) = 0.

**Independent test** (`ref_box.out` (S)). Over 400 random (q, Λ) on the box system, |min_{K_q} g_L| ≤ 1.1e−15.

---

## 5. Priority (5): Lemmas W, P, D and the final contradiction

### Lemma W: CONFIRMED WITH REPAIR R5

**R5 (order of quantifiers).** The proof says "check in the limit y → m₁₂, q = u". At that limit y₂ = e₃, which is not
in relint E₂, so the limit itself is degenerate. The correct order is:
1. Fix y⁽ⁱ⁾ on the **e₂-side** of m₁₂ (t > ½), close enough to m₁₂ that:
   - y₂(u) ∈ (0, δ₀), using N_{E₂} ⊇ (e₃, e₃ + δ₀), which holds since κx₊² > 1;
   - Z₃^{E₂}(y₂(u)) < 1 − c₀ (Z₃^{E₂} is continuous with Z(0) = 0);
   - the E₁ conditions hold (all open at m₁₂).
2. Since y⁽ⁱ⁾ ≠ m₁₂, u ∉ line(y⁽ⁱ⁾, e₃). So for q in a small U, y₂(q) stays in (0, δ₀).

The window exists for every ε ∈ (0,1). The required closeness to m₁₂ depends on ε, because the slope of Z₃^{E₂} at e₃
is about κx₊.

**Numerics.** All conditions (y₁, y₂ non-failing; facet 1 at z₁ and z₂; y₂ ∈ relint E₂; orientations) hold at the actual
q = u ± r n, for windows at offsets 0.01 and 0.003, at all 12 values of ε, including ε = 0.995 and ε = 1/7.

**Every interior target weighting p\*.** The reduction to p\* = u multiplies world i's penalties by p\*_i. This leaves
every world preorder unchanged, so the ranking, its domain, (LA), (S), (C) and (LF) are literally the same. Only the
Bayes family is re-indexed, by q ↦ ν(p\* ⊙ q). The reduction is correct. Normalising x = x₊ via σ = (1 2) is
Contamination Triangle §4.6.

### Lemma P: CONFIRMED (repair R6)

Checked symbolically (`ref_symbolic.out` (b), (c)):
- c₁(h\*) = (1−x, x, −1);
- μ₁(e₁) = a₁ = (x−1)/(2x−1), which lies in relint E₁ for x > 1;
- μ₂(e₁) = a₂ = −1/(x−2), measured from e₃;
- h\* = (0,1,−1) satisfies h\*·v₂ = ε > 0 > h\*·v₃ = −ε, so h\* is **not** a facet gamble. Only the Möbius extension is
  used, and π_q is a projectivity determined by the window.

The perspectivity criterion (the common point is self-corresponding) is classical.

**R6.** At ε = 1/7 (x₊ = 2), a₂ is at infinity. Transversality must then be read in a projective chart of line E₂.
Möbius maps are diffeomorphisms of P¹, so the argument goes through. Numerics at ε = 1/7: γ/r = ±2.31e−3, with opposite
signs on the two sides.

### Lemma D: CONFIRMED

Exact in sympy:
- D|_{b=0} = 0;
- ∂_b D|_{b=0} − (d/a²)(w₁−w₂)(w₂−w₃)(w₃−w₁) = 0.

Since D vanishes identically on {b = 0}, D = b(∂_b D|_{b=0} + O(b)) uniformly. At q = u, in the coordinates (X,Y) centred
at e₁, π_u(X) = Y_v X/(X − X_v), so ad = −X_v Y_v ≠ 0 (v₁ lies on neither edge line).

### Theorem I1: CONFIRMED

- γ = g₂(L₁ ∩ L₃). The identity l₂·(l₁ × l₃) = −det(l₁,l₂,l₃) was verified symbolically, so γ ∝ D with a locally
  constant nonzero factor (L₁ and L₃ meet at v₁ at q = u).
- b(q) ∝ π_q(e₁) changes sign transversally across C₁.
- On the side where γ > 0: K_q ⊆ {g₁ ≥ 0} ∩ {g₃ ≥ 0} ⊆ {g₂ ≥ γ}, which contradicts min_{K_q} g₂ = 0.

My independent certificate (`ref_t1_window.out`) uses the full piecewise maps, with no Möbius fitting. At r = 1e−4 and
r = 1e−6, γ/r has opposite signs on the two sides of C₁ and is stable in r, at every ε. For example, ε = 0.3:
γ/r = +6.452e−3 / −6.452e−3.

**The contradiction itself is recomputed:**
- (Diag) holds iff c₁(h\*)₁ = 0 iff x = 1.
- The corner equation x + 1/x = κ + 1 > 2 gives x ≠ 1.
- Equivalently: c₁ restricted to v₁^⊥ is the restriction of a diagonal map iff x = 1, since h₁ = −c₀(h₂+h₃)/(c₀+ε) on
  v₁^⊥.

---

## 6. Priority (6): hidden assumptions

I found no regularity or additional hypothesis. What the argument actually uses:
- Hausdorff continuity of K_q and joint continuity of P (Prop reduction (b));
- the every-q (or a.e.-q) chart form;
- R4 Thm B;
- (C2)–(C4);
- continuity of μ, which is proved;
- openness of N_E, which follows from the continuity of Z.

Nothing is assumed about the chart data beyond measurability. The window is fixed, and only finitely many lines are used
at each q.

**R7 (precision).** "The box is not used" is true of I1's own steps: the inequality 1/κ ≤ x² ≤ κ never appears. However,
box witnesses enter **through the inputs**. Cor TSalways(b)/(c) and Cor availability come from Thm cuts, which uses the
chart-form box witnesses of Prop boxbridge(c). The sentence should say so.

---

## 7. Priority (7): known genuine solutions are not excluded

On the normalised-box system K_q = ν(q ⊙ a), a ∈ ∏[λ_i, η_i] (a genuine CF solution), my own implementation gives:
- **Prop E:** exact, with max error 4.4e−16 over 75 edge priors;
- **Thm R:** exact;
- **Lemma S:** exact;
- **the certificate:** it **does not fire**. γ is between 1e−19 and 2e−16 for windows at y ≈ .55, .68, .93 and for q on
  both sides of three directions through p\*.

**Why the certificate is silent there.** The box facet maps are diagonal on each sign piece: c(h)_k = 0 whenever h_k = 0.
So every C_k passes through e_k, and π_q(e_k) = e_k for every q. The forced lines from one piece all pass through
ν(D_σ q), so they are concurrent.

**The step that distinguishes T1** is Lemma P(4), fed by (C2). The crossing rows together with the corner equation make
the T1 facet maps non-diagonal (x ≠ 1).

The control runs in the note show the same:
- x = 1: middle-window gap 0 on both sides;
- x = 1.2: gaps on one side.

---

## 8. Statement established, and dependencies

**Established (PROVED, modulo the inputs listed below).** For every ε ∈ (0,1) and every interior target weighting p\*,
no strictly guiding additive ranking with integral penalties on a decomposable domain with (LF) at D_{T1}, satisfying
(LA), (S), (C), covers T1.

Consequently CF(T1) has no solution. This consequence has the status of Prop CF(⇐), i.e. of Thm CCIBU.

The bounded-charge version (Cor (c)) remains CHECKED.

**Dependencies and their statuses.**

| input | used for | status |
|---|---|---|
| Prop necessary (a), Prop reduction (b) | K_q, Hausdorff continuity, joint continuity of P | proved; refereed (R6, N14) |
| Cor TSalways (a)–(c), Thm TSalways (N28 Thm 3.5) | (TS); both acceptances a.e.; K_q → {e_b} | one referee (N28_referee §3); rests on N21.9, N21.4 (N23), R10b (R12), Lemma R23.1 / Cor R23.2 (N23 + second reading) |
| Thm TS = N21.4 (item 5: c-clusters as vectors) | (C3) and (PC), (NS) | one referee (N23 §4) |
| Lemma B1 = N21.2 | chart {c·q > 0} on B₁ | one referee (N23 §3) |
| N12 Thm 3.1 items 3–5 + N21 remark; R15 algebra | crossing rows; x₁ = x₂ = x₃ = x ∈ {x±} | refereed (N14, N23; R18) |
| N21.7(d) ← R4 (K4) | (C4) edge confinement | one referee each (N23; R8) |
| N28 Prop 5.1(⇒) | every-q CF chart form | one referee, confirmed with repair (N28_referee §5.1) |
| R4 Thm B | K_q ⊆ ℓ_g on the d-face | refereed (R8) |
| §4.6 transposition; prior reweighting | normalisations | elementary (re-checked here) |
| **I1's new steps:** Lemma 1, Lemma 2, Prop E, Thm R, Lemma S, Lemma W, Lemma P, Lemma D, Thm I1 | the proof | **this report: CONFIRMED** (repairs R1–R7, all expository) |
| Prop CF(⇐), Thm CCIBU | only for "CF(T1) has no solution" | CHECKED / author-checked |

**Single points of failure.** The once-refereed inputs are Cor TSalways, N21.4 item 5, N21.7(d) and N28 Prop 5.1(⇒).
Before the result is promoted from one reader to two, a second reading of these, together with this note, is the right
test.
