# T1n. Configuration (V): under nested edges at e₁ the partner ratio is pinned on the whole link class, so ¬(Loc) cannot come from the partners

16 Oct 2026 (BRIEF13 rules; task: settle (V) of R21 either way). Read with R21_reduction.md, Q1_notes Part I, Q2_notes
Part I, Q3_notes Part I, N2 Part I §6, P1 Part I, H1 (H1.2), F1 (F1.2), and the two referee reports that appeared while
this note was written: **Q13_referee.md** (on Q1, Q3) and **Q24_referee.md** (on Q2, Q4). Both are used below.

Labels: **PROVED** (full proof here, from inputs whose status is named), **CHECKED** (step-by-step reading, not a
re-derivation), **CONJECTURE**, **NUMERICS** (`t1npy/t1n_band_chain.py`, run with `python3 -I -B` from inside `t1npy/`;
output `t1n_band_chain.out`; no proof rests on it). No assumption is added: every hypothesis beyond the axioms is a
hypothesis of the result that uses it.

Notation: R21 §1; Q1 §1 (H_W), (H_E), chain coordinates x_j, χ = (x₂, x₃) on Q₁, ω := w₂/w₃ on Q₁, Lemma Q1.20 (cut
moves), Lemma Q1.21 (composition); 𝒜₁ = accepted world-1 vectors (Lemma vectorform). For a measurable weight f and a set
A, f(A) := ∫_A f dμ. For z ∈ (0,1)² the open quadrants are NW(z) := {x₂ < z₁, x₃ > z₂}, SE(z) := {x₂ > z₁, x₃ < z₂},
NE(z), SW(z) likewise; "a piece in NW(z)" means a measurable subset of Q₁ ∩ χ⁻¹(NW(z)).

---

## 0. Outcome

**(V) is NOT settled. No cover was constructed, and "no cover in (V)" is not proved in full generality.** What is proved
moves the frontier as follows.

1. **The Q1/Q2 tension, resolved completely (Proposition T1n.3, PROVED).** Q24_referee's Lemma R1 settled it on the
   *transverse* part of Q₁ and named the *comonotone* part as the place where Q2.15′ still gives ¬(Loc) "for free".
   That last claim is **false**. Under (Nest_e) at both edges of e₁, (CA⁺) partners with merely measurable densities,
   and closed sections:
   - **Theorem T1n.2 (fibre constancy, no (TC), PROVED).** ω is a.e. a function of χ on **all** of Q₁. In particular ω is
     0-homogeneous on Q₁, and constant along common level sets wherever the two chains are comonotone.
   - So Q2.15's criterion (N1) never holds, and Q2.15′ (in Q2's form and in Q24_referee's corrected form) is vacuous.
     The partners can never make world 1 ¬(Loc) when its edges at e₁ are nested.
   - The new ingredient is a **window bound at the edges of e₁** (Lemma T1n.1, the edge form of P1.15(b)/P1.17, PROVED).
     On a comonotone part no cut-move *cycle* closes, which is why Lemma R1 is silent there. But alternating 12- and
     13-moves climb the common chain with ratio ((1+η)²β/α)^k in a fixed window. Closed sections at e₂ forbid that.
2. **The gluing theorem without (TC), on monotone pieces (Theorem T1n.4, PROVED).** On every comonotone piece,
   log ω is a function of the common level of locally bounded variation. So ω = ψ(x₃)/φ(x₂) there, with φ, ψ
   nondecreasing. On every anti-monotone piece the same holds, with ω nonincreasing in x₂. Q2.15's (N2) fails on such
   pieces too.
3. **Measurable-density version of Q1.22–Q1.24 (Theorem T1n.5, PROVED).** Under measurable (TC) and measurable (CA⁺)
   densities, world 1 is (Loc) and (H_U) is contradictory. This is Q13_referee's requested fix (§1.4–1.5 there):
   statements a.e., value-band pieces, jumps of φ and ψ, quantifier order. It closes the sub-branch "(V) with (CA⁺)
   partners and (Nest_e) + (TC_m) at e₁" with no continuity proviso.
4. **What is left of (V) (§7).** A (V)-cover must have one of the following:
   - **(i)** a non-nested edge at e₁, with crossings inside Λ₁ ∩ R₁ⱼ (N2.2′);
   - **(ii)** nested edges, but a χ-law on Q₁ that is not absolutely continuous, with world 1 ¬(Loc) **through its own
     comparisons, not the partners'**. CONJECTURE T1n.C: this forces an *isolated comonotone band* on which world 1 is a
     two-world-type (N) world next to an additive world, i.e. a counterexample to L2.C in band form;
   - **(iii)** a partner without (CA⁺). Then the cover is in Q13_referee's leaf (S♮)-type field configuration at e_j, or
     b♮ ≥ 2, or the all-(Loc) residual Q_W.
5. **The suggested vertex argument fails, and why (§7.4).** Closed sections at e₁ give only scalar information on
   models selected near e₁: either C_p = P₁, or ψ_k(C_p) ≤ ψ_k(P₁) with lsc at e₁. They do not make C_p = P₁ off Λ₁.
   That would need continuity of the Bayes-weight correspondence, the same missing input as Q2 §6.3.

**Single obstruction.** On a comonotone band, world 1's mobility is one-dimensional: forward along the common chain
only, as in two worlds. Every three-world mechanism used here (rook cycles, anti-diagonal 2-cycles, window climbing)
needs either transverse crossings or a partner ratio that varies along a level. Neither exists on a band, by T1n.2.

| | Statement | Label |
|---|---|---|
| T1n.1 | window bound at the edges of e₁: capacity κ_j > 0; λ_j(Q)/λ_j(P) ≥ c_j(y₀, t) for accepted 1_Q − 1_P in a window | PROVED |
| T1n.2 | fibre constancy: ω = Ω∘χ a.e. on Q₁; anti-diagonal order; ω 0-homogeneous | PROVED |
| T1n.3 | Q1/Q2 tension: Q2.15 (N1) never holds under (Nest_e) at e₁; Q2.15′ and Q24_referee §1.4 vacuous | PROVED |
| T1n.4 | monotone pieces: ω = ψ(x₃)/φ(x₂) with φ, ψ nondecreasing (log Ω locally BV on comonotone pieces) | PROVED |
| T1n.5 | Q1.22–Q1.24 for measurable densities under (TC_m): (Loc), no cover | PROVED |
| T1n.6 | near e₁: C_p = P₁, or ψ_k(C_p) ≤ ψ_k(P₁) for some k ∈ supp p ∖ {1} | PROVED |
| T1n.G | general gluing: ω = ψ(x₃)/φ(x₂), φ, ψ nondecreasing, for every χ-law | CONJECTURE |
| T1n.C | ¬(Loc) under (Nest_e) at e₁ forces an isolated comonotone band carrying an (N) world | CONJECTURE |
| Q_T1n | single open question (§8) | open |

NUMERICS (`t1npy/t1n_band_chain.out`; bookkeeping of the two mechanisms of T1n.2 on cell models):
- (A) the anti-diagonal 2-cycle returns w₂-ratio 0.501 into its source when ω_NW = 1 < ω_SE = 2;
- (B) on a comonotone band with two ω-values per level, the best composite ratio is 5.0·10⁻¹, 2.5·10⁻¹, 6.3·10⁻²,
  4.0·10⁻³, 1.6·10⁻⁵ for 2, 4, 8, 16, 32 levels, matching (β/α)^{L/2};
- (C) with ω = Ω(level) it stays at exp(−V⁻(log Ω)) ≈ 0.376;
- (D) with Ω alternating inside one window it decays to 6·10⁻²⁰.

---

## 1. Setting

n = 3 on M_U, with U = D_{K′} and μ the standard Gaussian. Fix the blind world 1 and its two edges at e₁.

- **(H_W)** World 1 is a preorder on M_U with strict (G) and (IB).
- **(H_P^m)** For j = 2, 3: w_j ∈ L¹(M), w_j > 0 a.e. on M, **merely measurable**, and (RL-2): C ⪯_j X ⇒ ψ_j(C) ≤ ψ_j(X)
  for every C ∈ C_L and regular X, with ψ_j(X) := w_j(E_jX ∩ M). This is (CA⁺) of Q3 §1. It holds in (V) origin II-a
  (Q3.24 widens it to (CA⁺)), and in origin I whenever the partners' endorsement is countably additive.
- **(H_E)** (Nest_e) on {1, 2} and on {1, 3}. Each edge selection is indexed by its own chain, as in N12_referee §1.4:
  - c^j_b ⊆ R₁ⱼ with λ_j(c^j_b) = b, where λ_j := w_jμ|_{R₁ⱼ}/w_j(R₁ⱼ);
  - C^j_b is the selected edge model with world-1 errors c^j_b on R₁ⱼ (= P₁ off R₁ⱼ, N1.0(b));
  - C^j_0 = P₁ and C^j_1 = P_j;
  - competitiveness on {1, j} holds for b ∈ (0,1) (N0(iv));
  - the world-1 b-sections {b : C^j_b ⪯₁ X} are closed in [0,1] for every X (N0(iii), from (S));
  - there are no jumps (N1.4(a), R1 after the N12_referee fix).
  - The chain coordinate x_j: R₁ⱼ → [0,1) satisfies c^j_b = {x_j < b} mod null, and pushes λ_j to Lebesgue measure. Each
    c^j_b is the world-1 error set of a coherent model, hence a cone mod null, so x_j has a 0-homogeneous version
    (Q2.13(a)'s argument, refereed CORRECT in Q24_referee §1.2). Fix it.

Write c_b := c^j_b and d_b := R₁ⱼ ∖ c_b when j is clear. No (NC), (C), (LF) or T1 ∈ C_L is used before §6.

**Inputs used throughout.**
- **Cut moves (Q1.20; CORRECT, Q13_referee §1.1).** For b ∈ (0,1), S ⊆ c_b, T ⊆ d_b with λ_j(T) > λ_j(S):
  1_T − 1_S ∈ 𝒜₁. Its proof uses only (RL-2) and competitiveness, so it holds for measurable w_j.
- **Composition (Q1.21; CORRECT).** Successive accepted moves S_i ⇒ T_i with S_i in the current set and T_i outside it
  compose. Also, 𝒜₁ is closed under ternary sums of vectors with disjoint supports, and under adding a ternary vector
  ≥ 0 (weak (G)).

---

## 2. The window bound at the edges of e₁

**Lemma T1n.1 (PROVED).** Assume (H_W), (H_P^m), (H_E). Fix j ∈ {2, 3} and write λ := λ_j.

- **(a) Capacity.** Let s ∈ (0,1) and let S ⊆ c_s be non-null. Put
  κ(S) := inf{λ(W) : W ⊆ R₁ⱼ, W ∩ S = ∅, 1_W − 1_S ∈ 𝒜₁}. Then κ(S) > 0.
- **(b) Window bound.** Let 0 < y₀ < t < 1 and c(y₀, t) := (4/9)·min(1 − t, κ(c_{y₀/2}))/y₀ > 0. Let P, Q ⊆ R₁ⱼ be
  disjoint, with P, Q ⊆ {y₀ ≤ x_j < t}, λ(P) ≤ y₀/2 and 1_Q − 1_P ∈ 𝒜₁. Then λ(Q) ≥ c(y₀, t)·λ(P).

*Proof.*
- **(a)**
  - Let X be the regular edge model with E₁X ∩ R₁ⱼ = R₁ⱼ ∖ S, equal to P₁ off R₁ⱼ. For b ∈ (s, 1) the vector of
    (C_b, X) is 1_{R₁ⱼ∖S} − 1_{c_b} = 1_{d_b} − 1_S.
  - Suppose κ(S) = 0. Fix b ∈ (s, 1) and take W as in the definition with λ(W) < (1 − b)/4.
  - If W ∩ c_b is non-null, choose Z ⊆ d_b ∖ W with λ(Z) = (3/2)λ(W ∩ c_b). There is room, since
    λ(d_b ∖ W) > (3/4)(1 − b). Z is disjoint from S ⊆ c_b. The cut move at b gives 1_Z − 1_{W∩c_b} ∈ 𝒜₁.
  - Compose: 1_W − 1_S, then 1_Z − 1_{W∩c_b}. This gives 1_{(W∩d_b)∪Z} − 1_S ∈ 𝒜₁. Adding the ternary vector
    1_{d_b ∖ ((W∩d_b)∪Z)} ≥ 0 gives 1_{d_b} − 1_S ∈ 𝒜₁, so C_b ⪯₁ X.
  - So the closed b-section of X contains (s, 1), hence 1: P_j = C_1 ⪯₁ X. Its vector is 1_{R₁ⱼ∖S} − 1_{R₁ⱼ} = −1_S,
    which is non-zero and ≤ 0. This contradicts strict (G).
- **(b)**
  - Put m := ⌈y₀/λ(P)⌉ ≥ 2. Partition c_{y₀/2} into m sets W_i with λ(W_i) = y₀/(2m) ≤ λ(P)/2.
  - W_i ⊆ c_{y₀} and P ⊆ d_{y₀}, so the cut move at y₀ gives 1_P − 1_{W_i} ∈ 𝒜₁.
  - **Room.** Suppose (3/2)mλ(Q) ≤ 1 − t. Choose disjoint R_i ⊆ d_t with λ(R_i) = (3/2)λ(Q). The cut move at t gives
    1_{R_i} − 1_Q ∈ 𝒜₁, since Q ⊆ c_t.
    - The sets W_i, P, Q, R_i are pairwise disjoint: W_i ⊆ {x_j < y₀/2}, P, Q ⊆ {y₀ ≤ x_j < t}, R_i ⊆ {x_j ≥ t}.
    - So W_i → P → Q → R_i composes to 1_{R_i} − 1_{W_i} ∈ 𝒜₁.
    - The supports are disjoint for different i, so the sum 1_{⊔R_i} − 1_{c_{y₀/2}} is accepted.
    - Hence κ(c_{y₀/2}) ≤ (3/2)mλ(Q) ≤ (3/2)(y₀/λ(P) + 1)λ(Q) ≤ (9/4)(y₀/λ(P))λ(Q).
  - **No room.** Otherwise λ(Q) > (2/3)(1 − t)/m ≥ (2/3)(1 − t)λ(P)/(y₀ + λ(P)) ≥ (4/9)(1 − t)λ(P)/y₀.
  - κ(c_{y₀/2}) > 0 by (a), with s = y₀/2. ∎

*Remarks.*
- This is P1.15(b) and P1.17 on an edge of e₁. Q2.18 had recorded them as transferring (CHECKED); here they are proved
  for measurable w_j. Only closed b-sections at the far vertex e_j are used.
- (b) is stated for **any** accepted world-1 vector with disjoint source and target in the window, not only for cut
  pairs. This is what §3 needs.
- No bound is available as y₀ → 0, at the e₁ end of the chain. Closedness at e₁ is useless here, because P₁ ⪯₁ X
  always holds. §7.3 returns to this.

---

## 3. Fibre constancy without (TC)

**Theorem T1n.2 (PROVED).** Assume (H_W), (H_P^m), (H_E). Then:
- **(a) Anti-diagonal order.** For every z ∈ (0,1)²,
  ess inf of ω on Q₁ ∩ χ⁻¹(NW(z)) ≥ ess sup of ω on Q₁ ∩ χ⁻¹(SE(z))
  whenever both sets are non-null.
- **(b) Fibre constancy.** ω = Ω∘χ a.e. on Q₁, for a measurable Ω on (0,1)².
- **(c)** ω is 0-homogeneous a.e. on Q₁.

*Proof.* Put ν := w₂μ|_{Q₁}. For rationals β < α let A := Q₁ ∩ {ω > α}, B := Q₁ ∩ {ω < β}, and π_A := χ_*(ν|_A),
π_B := χ_*(ν|_B). Fix η > 0 with (1+η)²β < α.

- **Step 1 (the anti-diagonal 2-cycle).** Let z ∈ (0,1)². Suppose N ⊆ B ∩ χ⁻¹(NW(z)) and P ⊆ A ∩ χ⁻¹(SE(z)) are
  non-null. Take S ⊆ N with w₂(S) small.
  - **12-cut at b = z₁.** S ⊆ {x₂ < z₁} and P ⊆ {x₂ > z₁}. Choose T ⊆ P with w₂(T) = (1+η)w₂(S). Q1.20 gives
    1_T − 1_S ∈ 𝒜₁.
  - **13-cut at b = z₂.** T ⊆ {x₃ < z₂} and S ⊆ {x₃ > z₂}.
    - w₃(T) = ∫_T w₂/ω < w₂(T)/α = (1+η)w₂(S)/α.
    - w₃(S) > w₂(S)/β.
    - So (1+η)w₃(T) < (1+η)²w₂(S)/α < w₃(S).
    - Choose S′ ⊊ S with w₃(S′) = (1+η)w₃(T); w₃μ is non-atomic. Q1.20 gives 1_{S′} − 1_T ∈ 𝒜₁.
  - Composing gives 1_{S′} − 1_S ∈ 𝒜₁. It is non-zero and ≤ 0, against strict (G).
  - (a) follows: if the ess inf on the NW-set were below the ess sup on the SE-set, some rational pair β < α would give
    non-null N and P as above.
- **Step 2 (typical points).** Suppose σ := π_A ∧ π_B ≠ 0. The marginals of σ are absolutely continuous, because x_j
  pushes λ_j to Lebesgue and ν ≪ w_jμ on Q₁. So every horizontal and vertical line is σ-null.
  - Let Z be the set of z for which some open half-plane through z ({x₃ < z₂}, {x₃ > z₂}, {x₂ < z₁} or {x₂ > z₁}) has
    σ-null intersection with some ball B(z, r). **Z is σ-null.**
    - Take the lower half-plane. Cover by rational balls B_k with B_k ⊆ B(z, r) ∋ z. Then z₂ ≤ m_k :=
      sup{c : σ(B_k ∩ {x₃ < c}) = 0}.
    - Hence such z lie in B_k ∩ {x₃ ≤ m_k}, which is σ-null: σ(B_k ∩ {x₃ < m_k}) = 0, and the line is null.
    - The other three half-planes are the same.
  - Fix z ∉ Z and r > 0. Write q_Q := σ(Q(z) ∩ B(z, r)) for the four open quadrants Q. All four half-planes carry mass.
    - If q_NE = 0, the upper and right half-planes force q_NW, q_SE > 0.
    - If q_SW = 0, the left and lower half-planes force the same.
    - So for each r, either **(diag)** q_NE, q_SW > 0, or **(anti)** q_NW, q_SE > 0.
- **Step 3 (anti).** If (anti) holds at some z ∉ Z and some r, then σ ≤ π_B and σ ≤ π_A make B ∩ χ⁻¹(NW(z)) and
  A ∩ χ⁻¹(SE(z)) non-null. Step 1 gives a contradiction.
- **Step 4 (diag: climbing the common chain).** So (diag) holds at every z ∉ Z and every r.
  - Fix z⁰ ∉ Z and k ∈ ℕ with ((1+η)²β/α)^k < c(y₀, t)/2, where y₀ := z⁰₁/2 and t := (1 + z⁰₁)/2 (Lemma T1n.1(b) on
    the 12-edge).
  - Choose r with 2kr < min(z⁰₁, 1 − z⁰₁)/2.
  - **Points.** Put F₀ := NE(z⁰) ∩ B(z⁰, r), which is open with σ(F₀) > 0.
    - A σ-typical y ∈ F₀ with y ∉ Z has q_SW(y, r′) > 0 for every r′, and B(y, r′) ⊆ F₀ for r′ small. So
      σ(F₀ ∩ SW(y)) > 0. Put z¹ := y.
    - Repeat inside F₁ := NE(z¹) ∩ B(z¹, r), and so on, up to z^{2k}.
    - This gives z⁰ ≺ z¹ ≺ … ≺ z^{2k} (each strictly NE of the previous), and boxes
      Bx_i := NE(z^{i−1}) ∩ SW(z^i) with σ(Bx_i) > 0, all inside B(z⁰, 2kr).
  - **Pieces.**
    - piece₀ := A ∩ χ⁻¹(SW(z⁰) ∩ B(z⁰, r)), non-null by (diag) at z⁰.
    - piece_i := A ∩ χ⁻¹(Bx_i) for even i ≥ 2, and B ∩ χ⁻¹(Bx_i) for odd i. All are non-null, because σ ≤ π_A, π_B.
    - piece_{i−1} ⊆ χ⁻¹(SW(z^{i−1})) and piece_i ⊆ χ⁻¹(NE(z^{i−1})). So consecutive pieces are separated by the 12-cut
      at z^{i−1}_1 **and** by the 13-cut at z^{i−1}_2.
  - **Moves.**
    - From an A-piece to the next B-piece, use the 13-cut, with target w₃-mass (1+η) times the source's w₃-mass.
    - From a B-piece to the next A-piece, use the 12-cut, with target w₂-mass (1+η) times the source's w₂-mass.
    - As in Step 1, each round A → B → A multiplies w₂-mass by less than (1+η)²β/α.
    - Masses only decrease (in w₂ units), so a small initial mass w₂(S₀) = m fits every piece.
  - **Conclusion.** Q1.21 gives 1_{S_{2k}} − 1_{S₀} ∈ 𝒜₁ with S₀ ⊆ piece₀ and S_{2k} ⊆ piece_{2k}. The two are disjoint,
    and both lie in R₁₂ ∩ {y₀ ≤ x₂ < t}.
    - λ₂(S_{2k})/λ₂(S₀) < ((1+η)²β/α)^k < c(y₀, t)/2.
    - With m small, λ₂(S₀) ≤ y₀/2. This contradicts Lemma T1n.1(b).
- **Step 5 (b).** So π_A ⊥ π_B for all rational β < α.
  - Disintegrate ν = ∫ν_z π(dz) along χ, where π := χ_*ν (Q₁ ⊆ ℝ³ is standard Borel). Then π_A(dz) = ν_z(A)π(dz), so
    ν_z(A)ν_z(B) = 0 for π-a.e. z, for every rational pair.
  - Hence for π-a.e. z, ω is ν_z-a.s. constant. Call the constant Ω(z).
- **Step 6 (c).** χ(λg) = χ(g) for the 0-homogeneous version, and g ↦ λg preserves μ-null sets. So
  ω(λg) = Ω(χ(g)) = ω(g) a.e., for every λ > 0. ∎

*Reading.*
- Step 1 is Q24_referee's Lemma R1, but in quadrant form with value bands. It needs no continuity of w_j and no
  openness of χ.
- Step 4 is new. At a comonotone point no cut-move cycle closes: the corners that Lemma R1 needs are null. But the two
  edge chains let error **climb** the common chain, alternating which partner pays. If ω takes two values on one level,
  each climb loses a fixed factor, and the window bound of Lemma T1n.1 (closed sections at e₂) stops it.
- So **every** non-constancy of ω along a fibre of χ is excluded:
  - transverse fibres, by cycles;
  - anti-monotone fibres, by cycles (Step 3);
  - comonotone fibres, by climbing (Step 4).
- The proof uses nothing about world 1 beyond strict (G), (IB) and closed b-sections on its two edges. So it holds at
  any world with two (CA⁺) partners and nested edges, whatever its (NC) status: R21's origin I and origin II-a alike.

---

## 4. The Q1/Q2 tension

**Proposition T1n.3 (PROVED).** Assume (H_W), (H_P^m), (H_E), as in (V) with (CA⁺) partners and (Nest_e) at e₁.
- **(i)** Q2.15's criterion (N1) ("ρ₂/ρ₃ is not 0-homogeneous on a non-null part of Q₁", with (Loc) data (w₂, ∅),
  (w₃, ∅)) never holds (T1n.2(c)).
- **(ii)** Hence Q2.15′, in its original form and in Q24_referee §1.4's corrected form, has an empty antecedent:
  - on transverse parts (Lemma R1, Q1.22);
  - on anti-monotone parts (T1n.2, Step 3);
  - on comonotone parts (T1n.2, Step 4).
  
  Q24_referee's sentence "there Q2.15 (N1) still gives ¬(Loc) for free, and no cut-move cycle reaches ω" is correct in
  its second half and false in its conclusion. Climbing reaches ω, and Lemma T1n.1 turns the climb into a contradiction.
- **(iii)** Q2.15's (N2) also fails on every monotone piece of χ (T1n.4) and under (TC_m) (T1n.5). In general it is
  open (CONJECTURE T1n.G).
- **(iv)** Logical status of the two notes:
  - Q2.15′ ("partner ratio not 0-homogeneous ⇒ world 1 ¬(Loc)") is a true implication;
  - Q1.22–Q1.24 (and T1n.5) ("(TC) ⇒ world 1 (Loc) ⇒ no cover") is a true implication;
  - by T1n.2 the antecedent of the first never holds under (Nest_e) at e₁.

  So there is no conflict. Q2's readings "costs nothing", "no proved constraint touches the partner ratio on Λ₁ ∩ Q₁"
  (Q2.14(c)) and "(I) cannot be proved by edge arguments" are false under (Nest_e) at e₁, on the whole link class and
  not only on its transverse part.
- **(v) What survives of the partner-choice lead.** Only Q2.15's (N0): a non-nested edge selection at e₁. By N2.2′
  [R1 via N12_referee] with ρ*₁ = 0 on Λ₁, its crossings lie inside Λ₁ ∩ R₁ⱼ, which is entirely the θ = 1 tie set of the
  CA edge field.

*Proof.* (i) is T1n.2(c). (ii)–(iv) are readings of (i), of Lemma R1 (Q24_referee §1.3, PROVED there) and of the cited
results. (v) is N2.2′. ∎

*Consequence for P1's Q_P1 and R21's (V6).* With additive (or (CA⁺)) partners and nested edges at e₁, the ¬(Loc) that
H1.2 demands of world 1 must be produced by **world 1's own relevant comparisons**. It cannot be produced by any choice
of partner densities. This is the opposite of Q2.15′'s reading.

---

## 5. Monotone pieces: the potential exists without (TC)

Call a non-null measurable H ⊆ Q₁ a **monotone piece** if x₃ = f(x₂) a.e. on H for a strictly monotone continuous f. It
is **comonotone** if f is increasing, and **anti-monotone** if f is decreasing. By T1n.2(b), ω = Ω_H(x₂) a.e. on H, with
Ω_H(s) := Ω(s, f(s)). Let E_H be the set of s that are Lebesgue points, with positive density, of the x₂-marginal of
ν|_H, and approximate-continuity points of log Ω_H. E_H has full measure in x₂(H).

**Theorem T1n.4 (PROVED).** Assume (H_W), (H_P^m), (H_E).
- **(a) Comonotone.** Fix 0 < y₀ < t < t′ < 1 with 0 < f(y₀) < f(t) < f(t′) < 1. Put c₂ := c(y₀, t′) from Lemma
  T1n.1(b) on the 12-edge, and c₃ := c(f(y₀), f(t′)) from Lemma T1n.1(b) on the 13-edge. Then for all
  s₀ < s₁ < … < s_n in E_H ∩ [y₀, t]:
  - Σ_i (log Ω_H(s_{i−1}) − log Ω_H(s_i))₊ ≤ log(1/c₂);
  - Σ_i (log Ω_H(s_i) − log Ω_H(s_{i−1}))₊ ≤ log(1/c₃).
  
  So log Ω_H agrees a.e. with a function of locally bounded variation. Then ω = ψ_H(x₃)/φ_H(x₂) a.e. on H, with
  φ_H := exp(V⁻) and ψ_H∘f := Ω_Hφ_H, both nondecreasing. Here V⁻ is the negative variation of log Ω_H from a base
  point.
- **(b) Anti-monotone.** Ω_H is essentially nonincreasing. Then φ_H :≡ 1 and ψ_H(f(s)) := Ω_H(s) are nondecreasing.

*Proof.*
- **(a)**
  - Fix η > 0 and small intervals J_i ∋ s_i that are pairwise separated: sup J_{i−1} < inf J_i.
  - Pieces: H_i := H ∩ x₂⁻¹(J_i) ∩ {|log ω − log Ω_H(s_i)| < log(1+η)}. They are non-null, by density and approximate
    continuity.
  - Consecutive pieces are separated by a 12-cut b ∈ (sup J_{i−1}, inf J_i). Since x₃ = f(x₂) on H, they are also
    separated by the 13-cut f(b).
  - At step i, move by the 12-cut if Ω_H(s_i) ≥ Ω_H(s_{i−1}). This multiplies w₂-mass by (1+η). Otherwise move by the
    13-cut. This multiplies w₃-mass by (1+η), hence w₂-mass by at most (1+η)³Ω_H(s_i)/Ω_H(s_{i−1}).
  - The composite (Q1.21) is an accepted 1_Q − 1_P with P ⊆ H₀, Q ⊆ H_n, disjoint, inside {y₀ ≤ x₂ < t′} (J_i small),
    with λ₂(P) ≤ y₀/2 for small initial mass, and
    λ₂(Q)/λ₂(P) ≤ (1+η)^{3n} exp(−Σ(Δ log Ω_H)⁻).
  - Lemma T1n.1(b) on the 12-edge bounds this below by c₂. Let η → 0 with n fixed.
  - The mirror choice, with bookkeeping in w₃-units and Lemma T1n.1(b) on the 13-edge, bounds the positive variation.
  - A function whose restriction to a full-measure set has bounded variation agrees a.e. with a BV function. The
    Jordan decomposition gives log Ω_H = log Ω_H(s*) + V⁺ − V⁻, so log(Ω_Hφ_H) = const + V⁺ is nondecreasing.
- **(b)** For s < s′ in E_H, the point (s, f(s)) lies NW of (s′, f(s′)). Take z with s < z₁ < s′ and
  f(s′) < z₂ < f(s). Pieces of H near s lie in χ⁻¹(NW(z)), and pieces near s′ lie in χ⁻¹(SE(z)). T1n.2(a) gives
  Ω_H(s) ≥ Ω_H(s′). ∎

*Reading.*
- On a comonotone piece the two edge structures do glue, and the endorser of the cut moves exists. Unlike the
  transverse case it is **not unique**: any nondecreasing φ̃ with Ω_Hφ̃ nondecreasing works. This residual freedom is
  where §7's open case lives.
- NUMERICS (C), (D) illustrate the two directions of (a).

**CONJECTURE T1n.G (general gluing).** Under (H_W), (H_P^m), (H_E), for **every** χ-law there are nondecreasing φ, ψ with
ω = ψ(x₃)/φ(x₂) a.e. on Q₁.
- *Reformulation.* This is feasibility of the difference system u nondecreasing, v nondecreasing,
  v(x₃) − u(x₂) = log Ω(χ) a.e.
- *Status.* Its finite cycle conditions are T1n.2(a) and the rook identities. Its path-boundedness conditions are
  T1n.1(b). What is missing is the measurable Bellman construction for a χ-law that is neither absolutely continuous nor
  carried by monotone pieces.

---

## 6. Measurable (TC): Q1.22–Q1.24 without continuity

**(TC_m).**
- **(TC1_m)** π := χ_*(μ|_{Q₁}) is equivalent to Lebesgue measure on an open set G ⊆ (0,1)², and π((0,1)² ∖ G) = 0. χ is
  only measurable.
- **(TC2)** G is rook-connected.
- **(TC3_m)** x₂ ∈ I₂ := proj₁G a.e. on Q₂, and x₃ ∈ I₃ := proj₂G a.e. on Q₃.

The linear host satisfies (TC_m) with I₂ = I₃ = (0,1) (Q1.26, upgraded to PROVED in Q13_referee §1.7).

**Theorem T1n.5 (PROVED).** Assume (H_W), (H_P^m), (H_E), (TC_m).
- **(a) Product form.** There are nondecreasing φ: I₂ → (0,∞) and ψ: I₃ → (0,∞) with ω = ψ(x₃)/φ(x₂) a.e. on Q₁. They are
  unique up to a common factor, mod null sets.
- **(b) (Loc).** Put ρ* := w₂φ(x₂) on R₁₂ and w₃ψ(x₃) on R₁₃. These agree a.e. on Q₁, and 0 < ρ* < ∞ a.e. on M. Then
  ρ*μ (E2)-endorses every D-localized comparison of world 1 between regular models, for the localizing family D of the
  proof. So world 1 is (Loc).
- **(c) No cover.** With (H_U), H1.2 [R1] gives a contradiction. Q1.24 therefore holds for measurable partner densities.

*Proof.*
- **(a)**
  - By T1n.2(b), ω = Ω∘χ, with Ω defined Lebesgue-a.e. on G.
  - **Rook identity.** Let G₀ ⊆ G be the full-measure set of approximate-continuity points of log Ω. Take an
    alternating rook cycle z⁰, …, z^N = z⁰ with every turning point in G₀.
    - Run Q1.22's cycle argument [CORRECT, Q13_referee §1.4] with
      V^i := χ⁻¹(B(z^i, r) ∩ {|log Ω − log Ω(z^i)| < log(1+η)}).
    - The corner set at z^i (target side of the incoming cut, source side of the outgoing cut, both through z^i) is a
      quadrant of B(z^i, r). The good set has density 1 at z^i, and π ~ Leb. So the corner meets χ(V^i) in positive
      π-measure, and V^i ∩ corner is non-null.
    - On V^i, w₃-to-w₂ conversions cost the factor Ω(z^i)^{±1}(1+η)^{±1}. Only ω enters, never w₂ or w₃ alone.
    - Hence Π = 1.
  - **Boxes.** Let I × J ⊆ G be an open box.
    - By Fubini, for a.e. (α₀, β₀) ∈ I × J the sections {α : (α, β₀) ∈ G₀} and {β : (α₀, β) ∈ G₀} have full measure,
      and (α₀, β₀) ∈ G₀.
    - The rectangle identity with corners (α₀, β₀), (α, β₀), (α, β), (α₀, β) then gives, for a.e. (α, β),
      log Ω(α, β) = log Ω(α, β₀) + log Ω(α₀, β) − log Ω(α₀, β₀) =: g(β) − f(α).
  - **Gluing.** Two boxes whose α-projections overlap give rectangles with two corners in each. So their f's differ by a
    constant a.e. on the overlap; likewise for β. G is covered by countably many boxes. (TC2) makes the box graph
    connected: the endpoints of each rook step lie in boxes that share the kept coordinate. Cycles of boxes are rook
    cycles through G₀, and Π = 1 closes the constants. This is Q1.22(c)'s gluing step, a.e.
  - **Local monotonicity.** On a box, take α < α′ in I and β > β′ in J, all generic, and z with α < z₁ < α′ and
    β′ < z₂ < β. T1n.2(a) gives ψ(β)/φ(α) ≥ ψ(β′)/φ(α′). Let β′ ↑ β through approximate-continuity points of ψ: then
    φ(α′) ≥ φ(α). Symmetrically for ψ. So φ is essentially nondecreasing on a neighbourhood of every point of I₂, hence
    on each component of the open set I₂.
  - **Across components.** N₂ := (0,1) ∖ I₂ is closed and Lebesgue-null: λ₂(x₂ ∈ N₂) = Leb(N₂), and by (TC1_m) and
    (TC3_m) the set {x₂ ∈ N₂} is null.
    - At s ∈ N₂, nondecreasingness across s is Q1.22(b)'s argument: a 12-cut across s, then a ρ*-neutral rook return
      through G. Its turning points can be taken in G₀, because the turning points of rook paths near a given one form a
      product family, and Fubini applies.
    - When I₂ and I₃ are intervals (the linear host), this step is void.
  - Take the nondecreasing versions.
- **(b)** This is Q1.23's routing, with three changes.
  - **The localizing family.** D_m := M ∩ (A_m ∪ B_m ∪ C_m ∪ J_m).
    - A_m, B_m, C_m are as in Q1 §4.
    - J_m is new. Let (j_k) enumerate the jump levels of φ, and (j′_k) those of ψ. Put
      J_m := (R₁₂ ∩ ⋃_k {|x₂ − j_k| < 2^{−k−m}}) ∪ (R₁₃ ∩ ⋃_k {|x₃ − j′_k| < 2^{−k−m}}).
    - λ_j(J_m ∩ R₁ⱼ) ≤ Σ_k 2·2^{−k−m} ≤ 2^{1−m}, because x_j pushes λ_j to Lebesgue measure. Since w_j > 0 a.e., the
      finite measure μ|_{R₁ⱼ} is absolutely continuous with respect to λ_j, so μ(J_m) → 0.
    - So D is decreasing with μ(D_m) → 0.
  - **Quantifier order** (Q13_referee §1.5, fix (i)).
    - First fix m′ ≥ m and the compact G′ := {z ∈ G : dist(z, ∂G) ≥ 1/m′} ∩ [1/m′, 1−1/m′]².
    - Cover G′ by finitely many open boxes inside G and fix rook routes between their centres. This gives a bound P₀ on
      route lengths, independent of the cells.
    - Then choose η with (1+η)^{3(P₀+1)} < 1 + ε.
    - Then choose cells and stops.
  - **Oscillation with jumps.**
    - On the compact level ranges met by K := M ∖ D_{m′}, φ and ψ are bounded and monotone. Only finitely many of their
      jumps have ratio > (1+η)^{1/2}, and K avoids a neighbourhood of each of those (J_{m′}).
    - Off those neighbourhoods, a monotone function whose remaining jumps all have ratio ≤ (1+η)^{1/2} oscillates by
      ≤ 1+η on every interval of some length 2h.
    - Choose the cell grid lines and the rational turning levels at continuity points, inside that region.
    - Then the first and last steps ("cut at the cell edge") and every intermediate step are ρ*-neutral up to
      (1+η)³, exactly as in Q1.23.
    - A stop just beyond a cell edge lies inside a jump strip, but strictly before the jump level. So no step crosses a
      big jump.
  - Measurability of w_j never enters: each move conserves the step's w_j-mass up to (1+η), and ρ* = w_jφ(x_j) (or
    ψ) converts it with the oscillation of φ (or ψ) only.
  - The rest of Q1.23 (shrinking Z, free room, one piece at a time, the count) is verbatim, and is CORRECT by
    Q13_referee §1.5.
- **(c)** H1.2's hypotheses, checked one by one in Q13_referee §1.6, hold verbatim. ρ* is defined a.e. on Q₂ and Q₃ by
  (TC3_m). ∎

*Scope.* This closes "(V) with (CA⁺) partners, (Nest_e) at both edges of e₁, and (TC_m)", for both of R21's origins
(Q13_referee §3), with no continuity proviso. (TC_m) is a hypothesis on the cover's own edge selection. So this closes a
sub-branch of (V), not (V).

---

## 7. What remains of (V), and where every attempt stopped

### 7.1 Inventory

Let a (V)-cover have (CA⁺) partners (the R21 case widened by Q3.24). Then one of the following holds.
1. **Non-nested edge at e₁.** By N2.2′, crossings lie in Λ₁ ∩ R₁ⱼ. Nothing here applies: Lemma T1n.1 and T1n.2 need a
   chain coordinate.
   - Crossing members give *more* moves (A ↔ B both ways at w_j-rate), never fewer. I found no mechanism by which
     crossing frees ω. But nesting is what gives levels and the window bound.
   - CONJECTURE: T1n.2 holds with a nested complete sub-chain in place of (Nest_e). I could not show that one exists.
2. **Nested edges, (TC_m) fails.** Then π has a non-null singular part, or G is not rook-connected, or (TC3_m) fails.
   - By T1n.2 and T1n.4, the partners impose a product structure piece by piece, and world 1 must be ¬(Loc) (H1.2)
     through its own comparisons.
   - CONJECTURE T1n.C below says where.
3. **Partners without (CA⁺).** Some Λ^ca_j is non-null.
   - The universal field c♮ (Q3.25, for every choice of maximal-support CA densities, Q13_referee §2.6) then has a
     degenerate partner. By Q3.26 (correct as a trichotomy, case (II) CHECKED) the cover is at field level in "b♮ = 1 at
     e_j" or in b♮ ≥ 2.
   - That is Q13_referee's leaf (S♮)-type structure, not R21's (V) at e_j.
   - Separately, with D^{ν*_j}-localized cut moves (sources off the partners' carriers), Q1.25(d) (CHECKED) makes world 1
     (Loc) under (TC). The exclusion would then need either a σ-finite H1.3 or Q_W (Q2.16).
   - I did not re-run Lemma T1n.1 with localized sources. Its capacity step moves an arbitrary W ∩ c_b, which may meet
     the carriers.

### 7.2 Where ¬(Loc) can still come from (case 2)

**Routing exits.**
- From a point of Q₁ whose 12-level (or 13-level) also carries transverse mass at nearby levels, error can leave along
  that level into the transverse region ρ*-neutrally, rook around, and come back.
- The product structure extends to such a point. This is the same 3-step cycle as in T1n.2, with one leg replaced by a
  neutral rook path.
- So the only points where Q1.23's routing cannot start or end are those whose 12- **and** 13-levels have no transverse
  mass nearby.

An **isolated band** is a non-null set of such points. By T1n.2(a) it is carried, locally, by monotone pieces. On an
anti-monotone piece mobility is two-way (Step 3 cycles), but not neutral unless Ω_H is constant. On a comonotone piece it
is one-way (forward along the common chain).

**CONJECTURE T1n.C.**
- Under (H_W), (H_P^m), (H_E), world 1 is (Loc) unless it has an isolated comonotone band H such that, for every
  admissible band potential φ̃ (T1n.4(a)), some D-localized relevant comparison supported in H is not w₂φ̃(x₂)-endorsed.
- On H, world 1 is then a two-world-type system next to the additive "world" λ₂|_H, with forward-only cut moves and
  closed sections at e₂. It is a counterexample to **L2.C in band form**.

Evidence and limits:
- **For.** Generators from a band level to the far end x₂ → 1 (the L2/P1 mechanism) can be killed if transverse levels
  exist just below the band:
  - route the target ρ*-neutrally down through the transverse region;
  - enter the band from below by 12-moves (w₂-rate ≈ 1);
  - climb to the source level.
  
  This is a contradiction whenever the generator is ρ*-unendorsed. So a surviving band must start at the e₁ end of both
  chains (levels near 0), or have no transverse levels below it.
- **Against closing it here.** Inside a band, ratios are bounded below in every window (Lemma T1n.1). L2.C's residual
  ("ratio < 1, bounded below, concentrated at the cut", P1.18(c)) is untouched. Near level 0 there is no window bound at
  all.

### 7.3 Why the e₁ end is where (V) lives now

- Lemma T1n.1 holds only for windows with y₀ > 0. Closedness at the near vertex e₁ is vacuous for world 1.
- Every three-world kill above (T1n.2 Step 4, the band entry from below) uses either a window or transverse levels below.
- So the last refuge of a non-(Loc) world 1 with (CA⁺) partners and nested edges is **a comonotone band at the start of
  both edge chains**. There, both edges at e₁ first make world 1 err on a common family of cones in Q₁.
- Geometrically this is possible. The level surfaces of a coherent edge model on Q₁ are generated by active extreme
  points of K. Both edge families can share an active point a off both edges with a·g = 0 for some g ∈ (+,−,−) ∩ U.
  - For T1's K′ = co(v′_k), hull(K′ ∪ [e₁,e₂]) ∩ hull(K′ ∪ [e₁,e₃]) contains z = (c′, c′+ε′, c′+ε′)/(1+ε′).
  - z·g < 0 for some g ∈ (+,−,−) ∩ U: one has z·g ∝ c′g₁ + (c′+ε′)(g₂+g₃) > −c′g₁ε′/(2c′+ε′), and this lower bound is
    approached.
  - So comonotone links on (+,−,−) are not excluded by geometry (CHECKED, by the computation just given).

### 7.4 The suggested vertex argument, and where it stopped

**Lemma T1n.6 (PROVED).** Assume (H_U) and (H_P^m). Let p ∈ Δ with supp p ∋ 1 and supp p ≠ {1}. Then either C_p = P₁,
or ψ_k(C_p) ≤ ψ_k(P₁) for some k ∈ supp p ∖ {1}. As p → e₁, along any sequence on which the second case occurs with a
fixed k, ψ_k(C_p) → ψ_k(P₁) (Q3.21, lsc; CORRECT, Q13_referee §2.2).

*Proof.* Competitiveness of C_p on supp p against P₁ gives k ∈ supp p with C_p ⪯_k P₁.
- If k = 1, the vector is −1_{E₁C_p} ≤ 0, so strict (G) gives E₁C_p null and C_p = P₁.
- Otherwise (RL-2) gives ψ_k(C_p) ≤ ψ_k(P₁). With lsc at e₁, ψ_k(P₁) ≤ liminf ψ_k(C_p), so the two are equal in the
  limit. ∎

*Where it stops.*
- The hint was: "near e₁ every selected model is P₁ off Λ₁, and the forced trades into V₁ generate a σ-finite
  endorser". T1n.6 gives only a scalar.
- N2.1 makes C_p c*-Bayes at some w(p) ∈ Δ_{supp p}. If w(p) ≠ e₁, then C_p = P₂ on Λ₁ ∩ Q₁. That is world-1-wrong on
  all of (+,−,−) ∩ U, however close p is to e₁.
- Nothing forces w(p) → e₁ as p → e₁. That would need upper hemicontinuity of p ↦ Γ(p), which is Q2 §6.3's missing
  continuity of the selection in measure.
- The forced trades into V₁ do exist: θ = 1 cut moves from Λ₁ ∩ R₁ⱼ into V₁ ∩ R₁ⱼ. They bound any endorser on
  Λ₁ ∩ R₁ⱼ **from above** by its values on V₁. They give no lower bound. A lower bound needs exactly the backward
  mobility that bands lack.

### 7.5 The positive side

No cover was attempted beyond identifying its required shape. By T1n.2–T1n.5 and H1.2, a (V)-cover with additive
partners and nested edges at e₁ needs all of the following:
- a non-absolutely-continuous χ-law on Q₁;
- a world 1 that is an (N) world on an isolated comonotone band. By §7.2 this most plausibly means a band at the e₁ end of
  both chains;
- T1 ∈ C_L.

The second item is a counterexample to L2.C (band form). Conjectured false in two worlds (L2.C), it is open. So a
positive answer for T1 through (V) with additive partners and nested edges at e₁ now **requires refuting L2.C** in
band form (if CONJECTURE T1n.C holds), or a non-nested edge at e₁.

---

## 8. Single open question

**Q_T1n.** Is there a full three-world system on M_U with the following properties?
- strict (G), (IB), (LA), (S) with closed sections for every model, and (C);
- worlds 2 and 3 are (CA⁺);
- world 1's edges at e₁ are nested;
- world 1 is ¬(Loc).

T1 ∈ C_L is not required.
- By T1n.2–T1n.5, such a system has ω = Ω∘χ, fails (TC_m), and its ¬(Loc) is carried by world 1's own comparisons.
- **No** closes (V) for (CA⁺) partners with nested edges at e₁, via H1.2 (both origins).
- **Yes** is the template that a (V)-cover must extend. Under CONJECTURE T1n.C it is an L2.C counterexample on a
  comonotone band at e₁.

Q_T1n refines Q1's Q_Q1. Q_Q1's "comonotone link with gluing freedom" escape is reduced from "free" (Q2.15′,
Q24_referee §1.4) to "requires an (N) world on the band".

---

## 9. Dependencies, risk points, files

**Used** (status):
- Q1.20, Q1.21 (CORRECT, Q13_referee);
- N0(iii), (iv) and N1.4(a) with the N12_referee §1.4 indexing fix (R1);
- N1.0(b), (c) (R1);
- Q2.13(a)'s cone argument (CORRECT, Q24_referee);
- Lemma R1 (Q24_referee);
- Q1.22–Q1.23's proofs (CORRECT for continuous densities, Q13_referee; extended here);
- H1.2 (R1);
- N2.1, N2.2′ (R1);
- Q3.21, Q3.25, Q3.26 (CORRECT, Q13_referee; case (II) CHECKED);
- Lyapunov is not used;
- disintegration of finite Borel measures; Denjoy's approximate-continuity theorem; Jordan decomposition.

**Not used:** (NC) at any world; (C), (LF), T1 ∈ C_L before T1n.5(c) and T1n.6; any continuity of w_j; any openness of
χ, except in T1n.5.

**Points to check, in order of risk.**
1. **T1n.2 Step 4.**
   - The choice of the typical points z^i: each must lie outside Z, and the box between consecutive points must carry
     σ-mass.
   - Consecutive pieces must be separated by **both** cuts at z^{i−1}.
   - The final pair must be disjoint and inside the window of Lemma T1n.1(b).
2. **Lemma T1n.1(a).** The composition of 1_W − 1_S with the cut move out of W ∩ c_b, and the closed b-section at
   b = 1 (P_j). (b): the per-i composites W_i → P → Q → R_i, and the disjoint sum.
3. **T1n.2 Step 2.** The σ-nullity of Z (rational-ball cover, null lines) and the quadrant dichotomy.
4. **T1n.5(a).** "Across components" uses Q1.22(b)'s return path with generic turning points. It is void when I₂ and
   I₃ are intervals.
5. **T1n.5(b).** The jump strips J_m: their measure bound, and that K avoids the finitely many big jumps.
6. **§7.2's routing exits** and the band-entry argument are readings (CONJECTURE T1n.C), not proofs.

**Files** (`t1npy/`, run with `python3 -I -B` from inside `t1npy/`):
- `t1n_band_chain.py`, `t1n_band_chain.out`: NUMERICS (A)–(D) of §0. These are cell-model bookkeeping of the 2-cycle and
  of window climbing. No statement rests on them.
