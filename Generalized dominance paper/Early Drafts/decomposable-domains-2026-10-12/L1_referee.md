# Referee report on L1_notes.md (round 20, BRIEF17)

16 Oct 2026. One adversarial reading, checked against BRIEF17, K3_notes §6 with K3_referee §§6–7, write-up §4
(Lemmas signs/chords/levels/caps/UVN/PL2/nopin, Thms. pivot/nosliding, Props. boxbridge/T1) and §7.7
(Lemmas quasilin/ball, Props. crosspin/chainchords/carrying, Thm. M0closed), and L4_notes (Thm. L4.9).
- The scripts in `l1py/` were rerun with `python3 -I`. `facet_algebra`, `verify_F3J`, `explicit_twoarc` and
  `field_search` reproduce their `.out` files byte for byte.
- My scripts are in `l1ref_py/`:
  - `twoarc_exact.py`: an independent rebuild of the Prop. L1.2 configuration with an **exact** per-pair box
    test (no q-grid);
  - `box_sharpness.py`: a sharpness test of Lemma L1.3.

---

## 0. Verdicts

| Item | Verdict |
|---|---|
| §1.1–1.2 weak-field Bayes structure (chart lines through e₁, θ-dependence on Λ, fan at e₁, vertex atoms) | **CORRECT** (one overstatement, §1) |
| §1.3 necessary conditions (N1)–(N4); Lemma L1.5 | **CORRECT** (minor: (N3) ties, notation) |
| Prop. L1.2 (two R*-arcs: corner + box algebra consistent for every ε; explicit ε = 0.3) | **CORRECT** as algebra; independently confirmed |
| Lemma L1.3 (crossing-limit boxes) | **CORRECT**; shown sharp numerically |
| Lemma L1.4 (tools) | **CORRECT** (minor in (c)) |
| Lemma L1.6 (frozen along rays from e₁) | **CORRECT** |
| Thm. L1.A(a) (no int-Λ facet point) | **CORRECT** — PROVED; does not use L1.7 |
| Thm. L1.A(b1) (F2/F3 middle adjacency) | **CORRECT** |
| Thm. L1.A(b2) (F1 adjacency) | **CORRECT given L1.7** (two small repairs) |
| Lemma L1.7 (Thm. pivot Steps 1, 3 on F1 for weak P♭) | **GAP (fixable)**: Step 1 fails as written when p* ∈ E carries an F1 corner arc; fix in §4 |
| Cor. L1.B | **CORRECT given L1.A**; label must read "modulo L1.7" |
| Thm. L1.C (audit table §5) | **CHECKED status is justified**; key rows re-derived (§6); one row needs a sentence |
| Theorem L1 (Q_A: no) | holds **modulo L1.7 (repairable) and L1.C (CHECKED)**; the stated label is right once L1.B is relabelled |
| §6.1–6.2 consequences | **CORRECT** |
| L1.D (several blind sets) | necessary conditions **CORRECT**; the CHECKED "verbatim" sub-claim is a **GAP**; CONJECTURE correctly labelled |
| Cross-check with L4 Thm. L4.9 | L1 **does exclude configuration (I)** (both (I₂), (I₃)), through L1.A(a) alone; no conflict (§8) |

**Assessment.** The central new idea is correct and is the right one. On Λ the field is frozen along rays from e₁
(L1.6). This lets a zero, or a small value, on a blind arc propagate by concavity to an auxiliary facet gamble
that is forced positive near a vertex.
- Ties are handled by the two face models L₊, L₋.
- L1.A(a), the part that matters for L4, is a complete proof.
- The one real defect is in the CHECKED Lemma L1.7. It silently assumes P♭(p*, ·) = 0 on all of F1, i.e. no
  carrying arc on F1. That is automatic when p* ∉ E, but L1.7 is invoked without that hypothesis.

---

## 1. §§1.1–1.2: Bayes structure of weak fields — CORRECT

Re-derived:
- On Λ, q·c = (q₂+q₃)(θρ₂σ₂ + (1−θ)ρ₃σ₃). So chart lines of Λ ∩ R₂₃ pass through e₁, and charts on
  Λ ∩ {σ₂ = σ₃} are ∅ or Δ°.
- Λ-ties have c ∝ σ₂(0, 1−θ, −θ). Their chords are the lines {θ = const} through e₁.
- Along the ray {θ = θ₀}, B_q → S_{θ₀} in measure (K3.7(β)). So there is a fan of vertex limits at e₁.

**Overstatement.** "Lemma UVN at e₁ holds at a mixed x exactly when some ball around x meets Λ in a null set" is
true only in the "if" direction (which is all L1.4(c) states).
- Counter-instance to "only if": at a pinned crossing w32 ∈ Θ_Λ with an outside Λ-cusp, positivity near e₁
  still holds by concavity from the two non-exceptional neighbours (§6, row 1).
- Replace "exactly when" by "when".

## 2. §1.3 and Lemma L1.5 — CORRECT

- **(N1)** is K3.7(β′). Its proof uses only (γ), ρ₂, ρ₃ > 0 and closure of coherent models under convergence in
  measure. The orthant table is right: R₁₂-orthants use K₁, R₁₃-orthants use K₀, and both are used on (+,−,−) ∪ (−,+,+).
- **(N2)** is K3_referee (Q1).
- **(N4).** The margin is (c₀+ε) − (1/3 + s(c₀+ε−1/3)) = (1−s)·2ε/3 > 0. This is the same as L4.6(b).
- **L1.5.**
  - The int-Λ / strict / boundary trichotomy follows from rigidity.
  - "f ≡ 0 on an interval ⇒ v_k ∈ K*, D_{K*} = D_{T1} locally" is the L4.6(b) argument.
  - The (N4) exclusions are correct, including F2/F3 ∩ (+,−,−). There D_{K₁} = D_{K₀}, so v₂ ∈ K₀ (resp.
    v₃ ∈ K₁) would be needed.
- Minor points:
  - (N3) "E₁(C*) ⊆ E₁(T1)" holds off Z_{p*} ∩ Λ, because C* is a one-sided limit and resolves Λ-ties by side. So
    K* ⊆ co(T1 ∪ {e₁}) needs that proviso, or the right choice of side. (N3) is not used later.
  - The letter K* is used both for (N3)'s model and for L1.5's K* ∈ {K₁, K₀}. Rename one of them.
  - Sharpening, which also tightens L1.B(i): on a g₁ > 0 arc, a concave f ≥ 0 that vanishes at an *interior*
    point vanishes on the whole arc. So zeros occur only at the arc's endpoints, not merely "at most two".

## 3. Prop. L1.2 and Lemma L1.3 — CORRECT

**L1.3.** Re-derived; the formula (Box_{a,b}) is as stated.
- With A_b = η and B_b = −ζ, both charts contain q₀ = (1−s)e_b + s e_a iff
  λ_Bζ/c_a(B) < s/(1−s) < λ_Aη/|c_a(A)|.
- The ratio condition is η/ζ < |A_a|/B_a. Eliminating η/ζ gives (Box_{a,b}).
- The two facet normalisations cancel.
- Strict instance (b,a) = (3,2): it gives x₁x₂ ≤ κ, as stated.
- **Sharpness** (`box_sharpness.py`): in the two-arc data at ε = 0.3, the predicted threshold x₁ ≤ m₃/x₂ = 0.85937
  is exact.
  - At 0.97× the threshold, the exact pair test finds 0 violations.
  - At 1.03× the threshold, it finds violations, and only at pairs within 0.003 of the coordinate-3 crossings
    (τ ≈ 0.766 on F2, 0.769 on F1).
  - This confirms the note's caveat that grids miss crossing limits.

**L1.2.** I re-derived the constraints by hand.
- Corner r23 gives x₂ = (κ+2)(1−1/N).
- (Box_{2,3}), (Box_{1,3}) give m₃/κ² ≤ x₁x₂ ≤ m₃, with m₃ = (κ+2)(τ₃−b)/(1−b) → κ(κ+2)/(κ+1).
- (Box_{1,2}), (Box_{3,2}) give 1 ≤ x₁M ≤ κ².
- The corner signs at r31 and r12 give 1/(κ+1) < x₁ < κ+1.
- Coordinate-1 boxes are vacuous: the R*-arc gambles have c(A)·q₀ = s·c_a(A) < 0 on the relevant edge.
- The limiting x₁-window (1/(κ+1), κ/(κ+1)] is nonempty for every κ > 1. Swept for ε from 0.01 to 0.99 in
  `twoarc_exact.py`.

`twoarc_exact.py` rebuilds the ε = 0.3 solution independently, without importing `facet_configs`:
- 0 strict-sign failures on 3 × 4001 points;
- all four crossing boxes hold with slack (5.22 ≥ 1.72, 3.93 ≥ 2.29, 8.96 ≥ 2.95, 6.73 ≥ 3.92);
- an **exact** per-pair box test over 766 042 admissible pairs finds **0 violations**. Its samples are
  log-clustered to 10⁻⁷ at all six crossings, and it decides the existence of s ∈ (0,1) by intervals, with no
  q-grid.

So the claim "no contradiction can come from corner equations and boxes alone" is right. The configuration is
hypothetical (L1.A(a) excludes it). L1.2's role is diagnostic, which the note says.

The single-arc claim "arc at w13 and F2 strict at w12 contradicts (N1)" is re-derived:
- P_{K₁}(w13) > 0 from the (−,+,−) side;
- P_{K₁}(w12) ≥ 0 from the (+,−,+) side;
- m·w12 = −(1−a) for m = (a, 1−a, 0) ∈ K₁. This forces K₁ ∩ [e₁,e₂] = {e₁}, hence P_{K₁}(w13) ≤ e₁·w13 = 0.

The mirror case (arc at w12, F3 strict at w13) is the same with K₀.

## 4. Lemmas L1.4, L1.6, L1.7

**L1.4 — CORRECT.**
- **(a)** The directional limits are limits in measure of coherent B_{q+sδ}. B_q is the intersection of the
  limits for δ and −δ.
- **(b)** needs only that {q : g ∈ B_q} is an open half-plane, ∅ or Δ°.
- **(d)** Steps 1–4 of Prop. F are sign-free. The two replacement consequences (no Λ/strict mixing; no straddling
  of {g_c = 0}, c ∈ {2,3}) are right.
- **(e)** is right, with the correct caveat at coordinate-1 crossings.
- In (c), the case x₁ < 0 needs upward closure of D_K: if h−t𝟙 ∈ D_K then (h−t𝟙) + R³₊ ⊆ D_K, which has
  positive measure in the ball. The case x₁ > 0 needs "half-spaces through interior points cut a fixed fraction".
  Add one line.

**L1.6 — CORRECT.**
- Clipped values min(max(P♭(q,h), −s₀), s₀) are functions of B_q ∩ N, hence of θ(q). This is the form used later.

**L1.7 — GAP (fixable).**
- *Step 3 (continuity) is correct, and needs even less than stated.* Suppose τ_m → τ₀ with n_{τ_m} → n′ ≠ n_{τ₀}.
  Take q near p* with n′·(q−p*) < 0 < n_{τ₀}·(q−p*). Then Ψ(q,τ₀) > 0 ≥ Ψ(q,τ_m). This contradicts continuity of
  the concave function Ψ(q,·). So no one-sided limits (Step 2) are needed.
- *The half-plane form of A_τ is correct:* A_τ ≠ ∅ (it contains V₂ or V₃); p* ∉ A_τ, since
  P♭(p*,h) ≤ P_{T1}(h) = 0; quasi-linearity gives a line.
- *Step 1 is where the gap is.*
  - Lemma nopin is applied on G = int(P_{σ₁} ∩ P_{σ₂}), and the conclusion p* ∈ cl A_τ needs **p* ∈ cl G**.
  - In the write-up this holds because Ψ(p*,σ) = 0 on [0,1]. Here Ψ(p*,σ) = P_{K♭_{p*}}(h(σ)), which is concave,
    ≤ 0, and 0 on [τ₂,τ₃] (crosspin at the pinned crossings). It **can be negative on corner portions** when
    p* ∈ E and K♭_{p*} ⊋ T1 carries an F1 corner arc (Prop. carrying(b)).
  - The bracket endpoint σ₁ must lie in (0, τ₂) for every τ < τ₃, and symmetrically for τ > τ₂. If the carrying
    arcs fill both corner portions, then p* ∉ P_{σ₁} for every admissible bracket, and "p* ∈ cl G" is unproved.
  - L1.7 is stated "for every τ ∈ (0,1)" with no hypothesis p* ∉ E. Its check imports the chainchords version
    (Prop. chainchords), whose hypotheses include p* ∉ E and K♭_{p*} = T1.
  - L1.A(b2) uses L1.7 without excluding this. In the λ ≡ λ middle-orthant case it uses L1.7 at τ′ in a corner
    portion, which is exactly where carrying arcs live.
- **Fix (Lemma L1.7⁰, to be proved before L1.7): P♭(p*, ·) ≡ 0 on F1.** Suppose P♭(p*, h) < 0 on an open F1 arc α
  at r12 (r31 is symmetric). The inside shell over α lies in D_{T1} ∖ D_{K♭_{p*}} ⊆ Z_{p*}. It is open and
  connected, so by L1.4(d) it lies in one atom with normal b.
  - **b₁ = 0 (a Λ-atom).** Then the shell lies in Λ ∩ (−,−,+) = D_{K₀} ∩ O, so f = P_{K₀}∘h ≥ 0 on α. By
    L1.A(a), f ≤ 0. So f ≡ 0, and α is an adjacency arc with non-null inside Λ-ties. The first paragraph of (b2)
    ("reduction to no inside ties") excludes this, and it uses only face models, L1.4(d),(e), L1.5 and L1.A(a),
    not L1.7.
  - **b strictly signed (pattern (−,−,+)).** Run Prop. carrying(c),(d) and the last step of Thm. M0closed(a) on
    **F1**.
    - The chord {q·b = 0} misses the vertices.
    - Frozen support holds for strict atoms: the vertex chords meet it once each, so ℓ° is co-countable.
    - carrying(d) uses UVN only at e_o = e₃ and e_j = e₂ for F1 middle-arc gambles.
    - The final contradiction P_{K_δ}(h) > 0 at an F1 corner point needs crosspin only at F1's pinned crossings
      (L1.4(e)).
  - Hence P♭(p*, ·) ≡ 0 on F1, so p* ∈ P_{σ₁} ∩ P_{σ₂} for every bracket, and Step 1 runs verbatim.
  - The L4 §5.4(iv) reading makes the same point for (iv): carrying(d) on F1 at r12, r31.
- Alternative fix: keep σ₁ in a carrying arc, but show p* ∈ cl G from the positive side of the carrying chord,
  using π⁺ ≥ 0. This is more delicate with several chords through p*, so I recommend L1.7⁰.

**Status after the fix.** L1.7 becomes CHECKED with an explicit dependence on L1.7⁰. L1.7⁰ itself is at the level
of the write-up's carrying branch, re-read for one weak world.

## 5. Theorem L1.A and Corollary L1.B

**(a) — CORRECT (PROVED). Re-derived in full.**
- *Setup.* Int-Λ points form an open set of τ. They lie off (+,−,−) and (−,+,+), by (N2). On N, Z_{p*} ∩ N = {c ∝ εb_v} with ε = σ₂|_O.
  - L₊ ⊆ D_{T1} ∩ N ⊆ L₋ because B_{p*} ⊆ D_{T1} ⊆ B_{p*} ∪ Z_{p*}. Hence P_{L₊} ≤ 0 ≤ P_{L₋} on J₀ (clipped
    values).
  - Case 1 / Case 2 is exhaustive. The tie-free case is in Case 1.
- *Case 1.*
  - G_θ ∩ N decreases in measure to L₋ as θ → θ* from the accepting side.
  - Every Hausdorff cluster of K♭_{q_θ} has cone equal to L₋ on N, so the clipped f_θ → 0 pointwise, and
    uniformly on compacts by concavity.
  - The extrapolation bound η(1 + 2·dist/|J₂|) is right.
  - W meets every ray from e₁:
    - F2/F3: W = V₁ ∩ Δ°, with h₀ a strict point of the (+,−,−) arc. Such points exist: f ≥ 0, f ≢ 0, at most
      two zeros.
    - F1: W = conv(V₂ ∪ V₃) ∩ Δ°, a strip along (e₂, e₃), which every ray {θ = const} crosses.
- *Case 2.*
  - **F1.** Zeros at the two pinned crossings plus concavity give a contradiction at once.
  - **F2.** P_{K_δ} < 0 on (τ₃, 1].
    - The shell over a strict arc I ⊆ (τ₃, 1) lies in D_{T1} ∩ (+,−,−) ∖ D_{K_δ} ⊆ Z_{p*}, and misses Λ by (N2).
    - So c ∝₊ b with b₁ > 0.
    - A generic δ′ with δ′·b > 0 and εδ′·b_v > 0 exists. Both vectors lie in p*^⊥, and p*^⊥ → (𝟙^⊥)* is injective
      because 𝟙 ∉ p*^⊥. So the projections can be anti-parallel only if b = −λεb_v in R³, which is impossible
      since b₁ ≠ 0.
    - Concavity at (τ_R, τ₃, I) then gives the contradiction.
  - **F3** is the same.

The proof uses neither L1.7 nor Part C. **This is the step that decides the L4 cross-check (§8).**

**(b1) — CORRECT.** On R* between p* and e₁, B_q ∩ N = D_{T1} ∩ N:
- inside: q·c = (1−λ)p*·c + λρ₁ > 0;
- outside Λ: q·c = (1−λ)p*·c ≤ 0.

So P♭(q, ·) = 0 on J₀, hence P♭(q, ·) ≤ 0 on F2, against h₀ for λ near 1.

**(b2) — CORRECT given L1.7 (two repairs).**
1. *Reduction to no inside ties.* If ties are non-null in every cone around J₀, then by compactness there is a
   τ′ ∈ J₀ all of whose cones carry ties. Apply the "otherwise D_{K_δ} ⊇ D_{T1} locally" argument at τ′. One
   sentence.
2. *Θ_τ.* "Closed" is not proved: P♭ is only lower semicontinuous, so {P♭ ≥ 0} need not be closed. It is also not
   needed. "An open wedge between λ_τ and R*" understates the set: A_τ contains points with θ on both sides of θ*,
   so the convex union of rays Θ_τ contains a full neighbourhood of p*. The Step-5 argument then works for *every*
   τ₁ ∈ J₀ with λ_{τ₁} ≠ λ_{τ₀}, not just nearby ones. This gives the dichotomy "λ ≡ R* or λ ≡ λ ≠ R*" directly.

The three sub-cases were re-derived:
- **λ ≡ R*:** R* meets W.
- **Middle orthant:** Θ = Δ°, Z is a closed half-plane, and A_{τ′} = A ⊇ V₂ for corner τ′. This is the place that
  needs L1.7 at corner τ′, i.e. needs L1.7⁰.
- **Corner orthant:**
  - θ(y) > θ*, because e₁ is on the non-A side and so y* = R* ∩ (e₂,e₃) is on the A side;
  - the wedge at y between λ and line(e₁, y) is nondegenerate and meets W.

**L1.B — CORRECT given L1.A.**
- (i) needs (b2): on g₁ < 0 arcs, adjacency would make Θ_Λ infinite. So the label must be "PROVED modulo L1.7",
  as for L1.A(b2), not "PROVED".
- (ii), (iii): re-derived. P_{K*}(h′ ± s𝟙) = P_{K*}(h′) ± s.

## 6. Theorem L1.C — CHECKED status justified; key rows re-derived

- **Row 1 (UVN at e₁).**
  - At generic τ this is L1.4(c).
  - At exceptional τ with h₁ > 0, A_τ ⊇ A_{τ−η} ∩ A_{τ+η} by concavity.
  - At exceptional τ with h₁ < 0 (F1), Step 0's B_τ ⊇ V₁ is **not** recoverable this way: concavity bounds from
    below only. It is also not needed, because Step 5 shows thinness of Z_τ, and hence B_τ ≠ ∅, at every τ.
  - **One sentence needed for nopin at w32, w23 (j = 1).** "U⁺ lies in the T1-correct half, which is strict"
    gives only B_q ∩ 𝒰⁺ → 𝒰⁺ in measure. It does not give D_{K_q} ⊇ 𝒰⁺ up to the facet, which is what Γ needs. The
    containment comes from the same concavity clause: P(q, h(τ₃±η)) > t on V₁(τ₃−η) ∩ V₁(τ₃+η), at
    non-exceptional neighbours, so P(q, ·) > 0 on [τ₃−η, τ₃+η], so D_{K_q} ⊇ 𝒰⁺ for 𝒰 small. Here β (meeting 𝒰⁻)
    holds because D_{K₁} ∖ cl D_{T1} near w32 is non-null and strict.
- **Row 2 (PL2 at w12, w13).** Correct. The proof needs UVN only near w_±, not on all of 𝒰, and (a₋)₁ ≤ 0 holds
  since c₁ ≤ 0 on h₁ < 0, Λ included.
- **Row 3 (crosspin at w12, w13).** Correct, and simpler than written. If P_K(w12) < 0, the shell over a facet arc
  *straddling* w12 is open, connected and in Z_{p*}. By L1.B it contains strict gambles with g₁ < 0 and with
  g₁ > 0, which L1.4(d) forbids. No Λ-ball is needed. The case P_K(w12) > 0 is the outside analogue.
- **Row 4 (Estructure(b); face models agree with T1 on Λ).** Correct. The connecting path should be spelled out:
  - from a density point g of a Λ-part of D_{K_δ} ∖ cl D_{T1}, move along g + s𝟙 (P_{K_δ} stays > 0) to just
    short of ∂D_{T1};
  - the endpoints sweep an open patch of ∂D_{T1}, which contains a point outside the finite set Θ_Λ, and the
    shell there is strict;
  - the inside case uses g − s𝟙.

  This gives a tube in Z_{p*} with both Λ and strict parts, against L1.4(d).
- **Row 5 (edgebox).** Correct. For A + λB ∈ Λ, q₀·c = q_b c_b < 0 off e₁. Prop. T1 uses q₀ = (s, 1−s, 0) with
  s > 0. The transposed field (blind at world 2) is fine since s < 1.
- **Row 6 (transposition).** Correct: T1, K′ and U are S₃-symmetric, and x^σ = (1/x₂, 1/x₁, 1/x₃) is pure
  algebra.
- **Row 7 (carrying(a)).** Correct. A proper K_δ ⊊ T1 misses some v_k and is then positive at F_k's pinned
  crossing. Every facet has one.

The audit list matches L4 §5.4's independent list (i)–(iv). Together they are two CHECKED readings of overlapping
material.

## 7. §6: consequences and L1.D

- **§6.1–6.2 — CORRECT.** ρ₁ = ρ_∞ and Λ = Λ_∞ meet Theorem L1's hypotheses. The residual Λ_∞ ⊇ E₁(T1) ∩ M is
  K3.7(γ)'s, and L4 Ex. L4.7 sharpens it to ⊋.
- **L1.D necessary conditions — CORRECT.**
  - Rigidity at world k needs Λ_k ∩ (Λ_i ∪ Λ_j) null, because otherwise S₁ = P_j on Λ_k ∩ Λ_i and K3.7′ fails.
    The bullet "rigidity of Λ_k ∖ (Λ_i ∪ Λ_j)" should simply assume pairwise-null intersections.
  - On Λ_i ∩ Λ_j, T1 = {g_k > 0}: right.
- **The CHECKED "verbatim" claim is a GAP.** "Closures meet ∂D_{T1} in pairwise disjoint sets of rays" does not
  protect the auxiliary gambles.
  - Example: Λ₂ adjacent along F1's middle arc is compatible with that hypothesis. It kills UVN at e₂ there, so
    L1.A(a) Case 1 for Λ₁ on F1 has only W = V₃ ∩ Δ°, which meets only rays with θ near 0.
  - A bootstrap is needed: apply L1.A/L1.B world by world, each time using that the other blind sets cannot be
    int-Λ or adjacent on the auxiliary arcs. Alternatively, add to the hypothesis that each Λ_i (i ≠ k) is null
    near the auxiliary arcs used for world k.
  - L1.D itself is correctly labelled CONJECTURE.

## 8. Cross-check with L4_notes Theorem L4.9: does L1 exclude configuration (I)? — YES

- **L4's (I₂).** P_{K₁}(w₂) < 0 at w₂ = (0, −1, κ), which is L1's w12. By L4.6(c), Λ₁ ⊇ (+,−,+) ∩ O for a
  neighbourhood O of w12. Hence Λ₁ contains a two-sided conic neighbourhood of every short arc of F2's middle arc
  near w12, and Z_{p*} ∩ Λ₁ is non-null there.
- These are **int-Λ facet points** in the orthant (+,−,+). L1.A(a) excludes them: Case 1 if the tie-accepting face
  model L₋ vanishes on a subarc, Case 2 otherwise.
- The ties that defeat L4.8 are exactly what the L₊/L₋ face models of L1.A(a) handle. (I₃) is the mirror at w13.
- L1.A(a) uses neither L1.7 nor L1.C, so this exclusion is at PROVED level.
- L1's hypotheses are L4's (B1) with p* ∈ Δ°: Λ₁ = {ρ₁ = 0} ∩ M, ρ₂, ρ₃ > 0, and (γ), which L4's (γ₀) implies.

**Consequences.**
- L4.6(c) together with L1.A(a) gives P_{K₁}(w12) = 0 = P_{K₀}(w13). So only L4's case (II) remains at interior
  p*.
- Case (II) is closed twice at CHECKED level, by L4 §5.4 and by L1.C (the general finitely-many-rays case, of
  which (II) is an instance: Λ touches ∂D_{T1} only at w12, w13, r23).
- **Q_L4 reduces to the vertex case (V)** (p* = e₁, Λ₁ ⊋ E₁(T1) ∩ M), which L1 does not address.

**No inconsistency.**
- L4.6(b) (P_{K₁} > 0 on the open (+,−,−)-portions) is consistent with L1.5, and stronger.
- L4 §6's "first computation" (does the freed coordinate-1 row absorb the box contradiction?) is answered by
  L1.2: yes, algebraically, when both coordinate-1 rows are freed. This is moot, since L1.A(a) shows the freeing
  configuration cannot occur.

## 9. Requested changes

1. Insert Lemma L1.7⁰ (P♭(p*, ·) ≡ 0 on F1; proof as in §4) before L1.7. Make L1.7 depend on it. Replace Step 3's
   proof by the direct continuity argument.
2. Relabel L1.B (and §0 item 3) as "PROVED modulo L1.7". Sharpen L1.B(i): on g₁ > 0 arcs, zeros occur only at
   the endpoints.
3. (b2): add the compactness sentence for ties; drop "closed"; note that Θ_τ contains a neighbourhood of p*.
4. L1.C row 1: add the concavity sentence giving D_{K_q} ⊇ 𝒰⁺ in nopin (j = 1). Row 3: use the straddling shell.
   Row 4: spell out the 𝟙-path.
5. §1.2: replace "exactly when" by "when". L1.4(c): add the upward-closure line. (N3): add the tie proviso and
   rename its K*.
6. §6.3: assume pairwise-null intersections throughout. Downgrade "verbatim (CHECKED)" to a statement that needs
   the bootstrap described in §7.
7. Add one sentence to §6.1 recording that L1.A(a) excludes L4's configuration (I) and leaves only (V).

## 10. Files

- `l1ref_py/twoarc_exact.py` (+ `.out`): independent two-arc configuration at ε = 0.3, with strict signs, crossing
  boxes from data, the exact per-pair box test (766 042 pairs, 0 violations) and the κ-window sweep.
- `l1ref_py/box_sharpness.py` (+ `.out`): Lemma L1.3 is sharp; violations appear exactly past the predicted
  threshold, at pairs near the crossings.
- `l1ref_py/rerun_*.out`: reruns of the L1 scripts, identical to the originals.
