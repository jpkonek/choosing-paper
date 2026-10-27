# Referee report on T1n_notes.md and T2n_notes.md (round 22)

16 Oct 2026. Adversarial referee. Verdicts are **CORRECT**, **GAP** (fixable; the fix is given) or **WRONG**.

I re-derived every PROVED item against:
- R21_reduction;
- Q1 Part I and Q13_referee;
- Q2 Part I (Q2.10–Q2.16) and Q24_referee (Lemma R1, §1.4);
- Q3 Part I (Q3.20–Q3.26) and M2 §1 (forced and limit pairs);
- P1 Part I and P1_referee;
- N1 §7 (Q_N1), N2 Part I and N12_referee §1.9;
- K3 §5 (K3.5, K3.5′) and K3_referee;
- H1 (H1.2);
- write-up §2 (axioms (G), (IB), (LA), (S), (C); Theorem kkm) and §2.5 (U-domain).

Scratch work is in `t12nref_py/`.

**Numerics.** Every script was rerun with `python3 -I -B`, from a copy placed in `t12nref_py/`.
- `t1npy/t1n_band_chain.py`: the rerun in `t12nref_py/t1n_rerun/` is byte-identical to `t1npy/t1n_band_chain.out`.
  - *Disclosure.* My first rerun was made from inside `t1npy/`. The script writes its `.out` into its working
    directory, so that run rewrote `t1npy/t1n_band_chain.out` in place (the file time is now 13:38).
  - The script is deterministic. The rewritten content reproduces every number in T1n §0, and the second run from the
    copy is identical to it. No content changed.
- `t2npy/t2n_checks.py`: the rerun from a copy (`t12nref_py/t2n_rerun/`, 51 s) is byte-identical to
  `t2npy/t2n_checks.out`.
  - `p1_cell_copy.py` equals `p1py/q_n2_common.py` from the second line on. The first line carries the "verbatim copy"
    marker.
- My own checks are `t12nref_py/ref_checks.py` (+ `.out`, 3 s). Items (R1)–(R7) are cited below.

No verdict rests on numerics.

---

## 0. Verdicts

**Nothing in either note is WRONG at PROVED level.**
- The four main new results are correct: T1n.1, T1n.2 (including Step 4), T2n.0 and T2n.1/T2n.2.
- Two inventory and consequence statements claim more than the proved results give: T1n §0 item 4(ii) with §7.5, and
  T2n.4's "only ranking-level arguments".
- Several statements need small fixes.

### T1n

| Item | Verdict |
|---|---|
| **T1n.1(a)** capacity κ_j > 0 | **CORRECT** |
| **T1n.1(b)** window bound, constant (4/9)min(1−t, κ)/y₀ | **CORRECT** (constant re-derived; (R1)) |
| **T1n.2(a)** anti-diagonal order | **CORRECT** |
| **T1n.2 Steps 2–5** (typical points, dichotomy, climbing, disintegration): ω = Ω∘χ on all of Q₁ | **CORRECT** (Step 4 checked item by item, §1.2) |
| T1n.2(c) 0-homogeneity | **CORRECT** |
| **T1n.3** (i), (ii), (iv) | **CORRECT**. This refutes Q24_referee §1.4's surviving lead |
| T1n.3 (iii), (v) | **GAP (wording)**. (v) "only (N0) survives" contradicts (iii). "(N2) fails on monotone pieces" is local, but (N2) is global (§1.3) |
| **T1n.4** (a), (b) | **CORRECT**. One trivial GAP: one-sided interval at s₀ = y₀ |
| **T1n.5** (a)–(c), measurable (TC_m) | **CORRECT**. This is the write-up of Q13_referee §1.4–1.5, done right. Minor: "generic turning points" in "across components" is a sketch-level sentence; it is sufficient (§1.5) |
| **T1n.6** | **CORRECT** |
| §0 item 4(ii), §7.1 item 2, §7.5: "a (V)-cover needs a non-absolutely-continuous χ-law" | **GAP (claim does not follow; fix by restating)**. The complement of (TC_m) contains a.c. laws (§1.6) |
| §7.2 "by T1n.2(a) it is carried by monotone pieces" | **GAP (citation)**. T1n.2(a) concerns ω, not the χ-law. Labelled reading; fine once re-cited |
| §7.3 geometric check | **CORRECT** ((R5)) |
| §7.4 | CORRECT as a reading |
| T1n.G, T1n.C, Q_T1n | properly labelled CONJECTURE / open |
| NUMERICS | reproduced. (B) and (D) are the same computation in two codings (identical numbers at L = 8, 32). Illustrative only |

### T2n

| Item | Verdict |
|---|---|
| **T2n.0** self-protection | **CORRECT** (both cases re-derived) |
| **T2n.1** P1 ⊕ mirror: full two-world system, both worlds totally blind | **CORRECT**. Every axiom was verified independently (§2.2). **GAP (statement)**: "(Loc) ∖ (Loc_int) at both" needs P1.14's parameter choice at each world |
| **T2n.2** edge form on 𝓔_ij | **CORRECT** |
| T2n §1 "what this does to the negative route" | The consistency conclusion is **CORRECT**. **GAP (label)**: "N2.1, N2.2, N1.1, N1.2, N1.4–N1.6 are consequences of (a)–(c) and K3.1" is an unverified reading inside a PROVED paragraph |
| **T2n.3** | **CORRECT** (K3.5's (P1)–(P3) checked) |
| **T2n.4** (a), (b), (c) | **CORRECT**. All clauses were checked, including N12_referee's extra clause ((R2), (R3)) |
| T2n.4 "Consequence": "(PD), (E), (X) can be closed only by ranking-level arguments" | **GAP (overclaim)**. What is proved: no argument using only the properties listed in Q_N1, N1.2 and N2.3′(d) can close them |
| **T2n.5** (a)–(c) | **CORRECT** (forced and limit pairs checked against M2 §1; witness (R4)) |
| **T2n.6** | **CORRECT** |
| **T2n.7** | **CORRECT** for η < c′/(c′+ε′). **GAP (trivial)**: "for every η ∈ (0,1)" is false; H_η leaves U for larger η (§2.7) |
| T2n.8 | CHECKED stands, as a reading conditional on a realisation of (E∗) |
| **T2n.9** | **CORRECT**. Its first Reading bullet is in fact a complete proof and can be upgraded (§2.9) |
| Q_W (pair form) | well posed |
| NUMERICS (A)–(D) | reproduced. (C) is analytically trivial. (D) samples W_η with c ∈ (κ+0.1, κ+1), not (κ, κ+1); (R6) covers the full range |

---

## 1. T1n

### 1.1 Lemma T1n.1: CORRECT

**(a) Capacity.**
- *The test model.* X is regular, equals P₁ off R₁ⱼ, and has E₁X ∩ R₁ⱼ = R₁ⱼ ∖ S.
  - C^j_b = P₁ off R₁ⱼ (N1.0(b)).
  - For b > s, S ⊆ c_s ⊆ c_b. So the vector of (C_b, X) is 1_{R₁ⱼ∖S} − 1_{c_b} = 1_{d_b} − 1_S.
- *The case W ∩ c_b non-null.*
  - Z exists: (3/2)λ(W ∩ c_b) < (3/8)(1−b) < λ(d_b ∖ W).
  - Z ∩ S = ∅, because S ⊆ c_b and Z ⊆ d_b.
  - The cut move (Q1.20) needs strict mass inequality, and the factor 3/2 supplies it.
  - The sum (1_W − 1_S) + (1_Z − 1_{W∩c_b}) is ternary, with value −1 on S, +1 on (W∩d_b) ∪ Z and 0 elsewhere. So
    sum closure (Lemma vectorform) applies.
  - Adding 1_{d_b∖((W∩d_b)∪Z)} ≥ 0 gives 1_{d_b} − 1_S. The case W ∩ c_b null is the same without the cut move.
- *Closing at b = 1.*
  - The b-section is the continuous image of the closed t-section, since there are no jumps (N1.4(a), with the
    N12_referee fix). So it is closed.
  - It contains (s, 1), hence 1.
  - Any t with b(t) = 1 has C^j_t = P_j mod null, so the vector is −1_S, against strict (G).
- This is P1.15(b) on an edge, with the partner entering only through (RL-2). Measurable w_j suffice.

**(b) Window bound.** Re-derived.
- y₀/(2m) ≤ λ(P)/2 < λ(P), which gives the strict cut move W_i → P at y₀.
- λ(Q) > 0, since otherwise −1_P is accepted.
- The chain W_i → P → Q → R_i has pairwise-disjoint sets, so its partial sums are ternary. The disjoint sum over i is
  accepted.
- The two cases:
  - room: κ ≤ (3/2)mλ(Q) ≤ (9/4)(y₀/λ(P))λ(Q), using m ≤ y₀/λ(P) + 1 ≤ (3/2)y₀/λ(P);
  - no room: λ(Q) > (2/3)(1−t)λ(P)/(y₀+λ(P)) ≥ (4/9)(1−t)λ(P)/y₀.
- The lemma is stated for **any** accepted 1_Q − 1_P with disjoint P, Q in the window, which is what T1n.2 and T1n.4
  need. The proof uses only cut moves at y₀ and at t, so this generality is legitimate.
- (R1): no violation in 2·10⁵ random valid instances.

### 1.2 Theorem T1n.2: CORRECT, including Step 4

**Step 1** is Lemma R1 in band form.
- The inequality chain (1+η)w₃(T) < (1+η)²w₂(S)/α < w₂(S)/β < w₃(S) is right.
- S′ ⊊ S exists because w₃μ is non-atomic.
- No continuity is used. (a) follows by choosing rationals β < α strictly between the ess inf and the ess sup.

**Step 2.**
- *Absolutely continuous marginals.*
  - The x₂-marginal of ν = w₂μ|_{Q₁} is ≤ w₂(R₁₂)·Leb.
  - The x₃-marginal is ≪ x₃_*(w₃μ|_{R₁₃}) ∝ Leb, because w₃ > 0 a.e. gives w₂μ ≪ w₃μ.
  - Hence lines are σ-null, and quadrants partition half-planes mod σ.
- *Z is σ-null.* For the lower half-plane: if σ(B(z,r) ∩ {x₃ < z₂}) = 0, take a rational ball B_k with
  z ∈ B_k ⊆ B(z, r). Then z₂ ≤ m_k, and σ(B_k ∩ {x₃ ≤ m_k}) = 0, by continuity from below plus a null line. Countably
  many k. Correct.
- *Dichotomy.* If q_NE = 0, then upper ⇒ q_NW > 0 and right ⇒ q_SE > 0. If q_SW = 0, then left ⇒ q_NW > 0 and lower ⇒
  q_SE > 0. Exhaustive.

**Step 3.** σ ≤ π_A, π_B transfers σ-mass to non-null B∩NW and A∩SE preimages. Step 1 does not need z ∉ Z.

**Step 4 (the author's riskiest step).** I checked each point the author lists in §9.
1. *Typical points.*
   - (diag) holds at **every** z ∉ Z and **every** r, because (anti) is excluded wherever it would hold.
   - σ(F₀) > 0 by (diag) at (z⁰, r), and Z is σ-null, so y ∈ F₀ ∖ Z exists.
   - F₀ is open, so B(y, r′) ⊆ F₀ for small r′. (diag) at (y, r′) gives σ(F₀ ∩ SW(y)) > 0, so σ(Bx₁) > 0. The same
     holds inductively.
2. *Location.*
   - Each z^i lies in B(z^{i−1}, r). The box between consecutive points lies in the ball of radius |z^i − z^{i−1}|
     about z^{i−1}.
   - So everything is inside B(z⁰, 2kr), whose x₂-range lies in (z⁰₁/2, (1+z⁰₁)/2) = (y₀, t).
3. *Double separation.*
   - piece_{i−1} ⊆ χ⁻¹(SW(z^{i−1})), using Bx_{i−1} ⊆ SW(z^{i−1}) for i−1 ≥ 1 and the definition for piece₀.
   - piece_i ⊆ χ⁻¹(NE(z^{i−1})).
   - So both forward cuts at z^{i−1} separate consecutive pieces, with the source below and the target above in both
     coordinates.
4. *Disjointness.* For i < j, Bx_i ⊆ SW(z^i) ⊆ SW(z^{j−1}) and Bx_j ⊆ NE(z^{j−1}). piece₀ ⊆ SW(z⁰). All pieces are
   pairwise disjoint, so Q1.21's conditions hold and the final pair (S₀, S_{2k}) is disjoint.
5. *Bookkeeping.*
   - A→B by the 13-cut: w₂(T) < (1+η)(β/α)w₂(S).
   - B→A by the 12-cut: ×(1+η).
   - Per round < (1+η)²β/α < 1. The w₃-mass needed at an A→B step is < w₂(S)/α, so a small m fits every piece.
   - (R7) confirms the bound on 2·10⁴ random multi-round instances: maximal ratio/bound 0.996.
6. *Window.* S₀, S_{2k} ⊆ R₁₂ ∩ {y₀ ≤ x₂ < t}, λ₂(S₀) ≤ y₀/2, and the ratio is < c/2. This contradicts T1n.1(b).

**Step 5.**
- π_A ∧ π_B = min(ν_z(A), ν_z(B))π, so singularity is equivalent to ν_z(A)ν_z(B) = 0 π-a.e.
- Countably many rational pairs force ω to be ν_z-a.s. constant.
- Measurability of Ω: take for instance Ω(z) := tan ∫ arctan ω dν_z / ν_z(Q₁).

**Step 6.** Correct.

**Assessment.** This is a genuine strengthening of Lemma R1 and Q1.22(a). It needs only strict (G), (IB), (CA⁺) partners
and nested, closed edges at e₁. The new ingredient, alternating climbs stopped by closedness at the far vertex, is
sound.

### 1.3 Proposition T1n.3: (i), (ii), (iv) CORRECT; (iii), (v) GAP (wording)

- **(i), (ii): CORRECT.**
  - Q2.15 (N1) with data (w₂, ∅), (w₃, ∅) asks for ω not 0-homogeneous on Q₁. T1n.2(c) excludes this.
  - Q24_referee §1.4's corrected Q2.15′ has two alternatives: a non-open χ, which is now also excluded, and non-nested
    crossings, which (Nest_e) removes.
  - So **Q24_referee's sentence "there Q2.15 (N1) still gives ¬(Loc) for free" is refuted** under (Nest_e) at e₁. I
    concur.
  - *Scope.* (N1) for **other** (Loc) data of the partners is not addressed. The note specifies the data, so this is
    fine.
- **(iii): GAP (wording).**
  - Q2.15 (N2) is a **global** statement on Q₁: "not of the form A(r₁₂)/B(r₁₃)".
  - T1n.4 gives the form **piece by piece**, with piece-dependent φ_H, ψ_H. That does not make (N2) fail unless the
    χ-law is carried by one piece, or the pieces glue.
  - *Fix:* "on each monotone piece, the restriction of ω has the product form".
- **(v): GAP (wording).** "Only (N0) survives" contradicts (iii)'s "(N2) open in general".
  - *Fix:* "(N0), and (N2) for χ-laws neither satisfying (TC_m) nor carried by a single monotone piece".

### 1.4 Theorem T1n.4: CORRECT

**(a)**
- On H, Ω_H(s) = Ω(s, f(s)) is defined ν|_H-a.e., because χ_*(ν|_H) ≤ π.
- H_i is non-null by positive density and approximate continuity (Denjoy).
- The cuts b and f(b) both separate consecutive pieces forward, since f is increasing.
- The per-step factors are right:
  - a 12-step multiplies w₂ by (1+η);
  - a 13-step multiplies w₂ by ≤ (1+η)³Ω_i/Ω_{i−1}.
- So the composite ratio is ≤ (1+η)^{3n}e^{−Σ⁻}. T1n.1(b) gives Σ⁻ ≤ log(1/c₂) as η → 0.
- The mirror, in w₃-units on the 13-window [f(y₀), f(t′)), gives Σ⁺ ≤ log(1/c₃). So the variation is uniformly
  bounded on E_H ∩ [y₀, t].
- The Jordan decomposition and the nondecreasing φ_H = e^{V⁻}, ψ_H∘f = Ω_Hφ_H are right.

*GAP (trivial).* If s₀ = y₀, J₀ must be one-sided [y₀, y₀+δ) to stay in the window. Lebesgue points have positive
one-sided density, or take y₀′ < y₀. Cosmetic.

**(b)** (s, f(s)) is NW of (s′, f(s′)). T1n.2(a) then gives Ω_H(s) ≥ Ω_H(s′), and ψ_H(x₃) = Ω_H(f⁻¹(x₃)) is
nondecreasing. Correct.

### 1.5 Theorem T1n.5: CORRECT

This is exactly the write-up requested by Q13_referee §1.4–1.5, and it is right.

**(a)**
- *Rook identity through G₀.* The corner at each turning point is a quadrant. The good set has density 1, and π ~ Leb,
  so V^i ∩ corner is non-null. Conversions use only ω.
- *Rectangle identity.* Fubini gives (α₀, β₀) generic, then all four corners in G₀ for a.e. (α, β). With the orientation
  convention of Q1.22, Π = Ω(α,β₀)Ω(α₀,β)/(Ω(α,β)Ω(α₀,β₀)) = 1.
- *Gluing.* The box graph is connected under (TC2): both endpoints of a rook step lie in boxes whose projections contain
  the kept coordinate.
- *Local monotonicity* via T1n.2(a), plus approximate continuity of ψ from the left. Correct.
- *Across components.*
  - N₂ is Lebesgue-null: λ₂(x₂ ∈ N₂) = Leb(N₂), and {x₂ ∈ N₂} is null on Q₁ (π(G^c) = 0) and on Q₂ (TC3_m).
  - The Q1.22(b) argument actually works for **any** α < α′ in I₂ with any cut b between them, so global monotonicity
    does not even need the component structure.
  - The return path needs turning levels at continuity points of φ, ψ. Monotone functions have countably many jumps,
    so generic turning points (a product family, Fubini) avoid them.
  - The sentence in the note is terse but sufficient.

**(b)**
- The jump strips have λ_j(J_m ∩ R₁ⱼ) ≤ 2^{1−m}, and μ(J_m) → 0 by w_j > 0.
- The quantifier order is now P₀ first, then η, then cells. This fixes Q13_referee's circularity.
- *Oscillation.* After removing neighbourhoods of the finitely many big jumps, a bounded monotone function whose
  remaining jumps have ratio ≤ (1+η)^{1/2} oscillates by ≤ 1+η on all short intervals. (By compactness: a sequence of
  shrinking bad intervals would produce a jump > the threshold at the limit point.)
- Steps along a level see only the oscillation of φ (12-steps) or ψ (13-steps) near that level. So no step crosses a big
  jump.

**(c)** H1.2's hypotheses are verbatim as in Q13_referee §1.6. ρ* is defined a.e. on Q₂, Q₃ by (TC3_m).

So **(V) with (CA⁺) partners, (Nest_e) and (TC_m) at e₁ is closed with no continuity proviso.** This is a sub-branch,
as the note says.

### 1.6 The inventory (§0 item 4(ii), §7.1 item 2, §7.5): GAP (the claim does not follow)

§0 item 4(ii) and §7.5 say a (V)-cover with (CA⁺) partners and nested edges needs "a χ-law on Q₁ that is not absolutely
continuous". What T1n.2–T1n.5 + H1.2 prove is weaker: the cover must **fail (TC_m)**. The complement of (TC_m) contains
absolutely continuous laws:
- π ≪ Leb, but π is not equivalent to Lebesgue on any open set. For instance, π ~ Leb restricted to a closed nowhere-dense
  set of positive measure.
- π ~ Leb on an open G that is not rook-connected: two components with disjoint projections.
- (TC3_m) fails.

§7.1 item 2 lists the last two but omits the first. §7.5's first bullet and §0 item 4(ii) omit all three. None of them
is excluded: T1n.4 handles only singular, monotone pieces.

*Fix.*
- Restate §0 item 4(ii) and §7.5 as "a χ-law failing (TC_m)".
- Add the non-open a.c. case to §7.1 item 2.
- In §7.5, the second bullet ("an (N) world on an isolated comonotone band") rests on CONJECTURE T1n.C. Write it as
  conditional. Note too that ¬(Loc) together with ¬(M0) gives "(M1) with (NC), or (N)", not (N) alone (K3.7).

*Nearby result (available).* T1n.5's proof uses π only through Lebesgue density points and Fubini on rectangles. It
should go through with (TC1_m) replaced by "π ≪ Leb, and the set of density points of π is rook-connected in measure"
(every two density points are joined by an alternating chain of density points). (TC3_m) is kept with I_j := projections
of the density set. That would shrink (ii) to singular laws plus disconnected supports, which is the inventory the note
wants.

### 1.7 T1n.6 and §7.3–7.4

- **T1n.6: CORRECT.**
  - Competitiveness against P₁ gives k with C_p ⪯_k P₁.
  - k = 1 gives −1_{E₁C_p} accepted, hence C_p = P₁.
  - Otherwise (RL-2) at k applies: C_p ∈ C_L and P₁ is regular.
  - The limit: Q3.21's lower semicontinuity at C_{e₁} = P₁ (competitive on {1}).
- **§7.3:** z = (v′₃ + ε′e₂)/(1+ε′) = (v′₂ + ε′e₃)/(1+ε′), and some g ∈ (+,−,−) ∩ U has z·g < 0 (R5: 788/8115 samples
  at ε = 0.1). CHECKED is fair.
- **§7.2:** the citation "by T1n.2(a) it is carried, locally, by monotone pieces" should be replaced. An isolated band
  has no NW/SE mass near its points, so its χ-law is locally carried by a chain of the product order, which is the graph
  of a monotone relation. This is a property of π, not of ω. It is still a reading.

---

## 2. T2n

### 2.1 Lemma T2n.0: CORRECT (priority 1)

- δ′|_M = 1_P − 1_Q, with D(δ′) = 0 because X and C_b are regular. So R⁰ gives 1_P − 1_Q = g_F + f.
- *F ≡ ⊥:* τ_f(b) = −λ(Q).
- *Case (i):*
  - τ_{δ′}(u_k) = −λ(Q ∩ {x ≥ u_k}) ≤ 0, since P ⊆ c_b ⊆ c_{u_k}.
  - τ_{g_F}(u_k) ≥ (16/25 − 1/25)r_k, by P1.10a [R1].
  - So τ_f(u_k) < 0.
- *Case (ii):*
  - Every line has q_n + 1 ≥ 3 points, so v_n ≤ u_k < b. Sources are in Σ_n ⊆ c_{v_n} ⊆ c_b.
  - On d_b, g_F is a sum of target indicators, ≥ 0. A ref block straddling b is harmless, because only g_F ≥ 0 on d_b
    is used.
  - So τ_f(b) ≤ −λ(Q).
- The cases are exhaustive. NUMERICS (A) reproduced (max 0, control 1).

### 2.2 Theorem T2n.1: CORRECT; every axiom checked independently (priority 2)

Write-up §2 lists the axioms: preorders, strict (G), (IB), (LA), (S) (selection in C_L, competitive on supp p, closed
sections for every model at every world), and (C).

1. **Preorder, strict (G), (IB).** World 1 is P1.11 [R1].
   - World 2 is P1's acceptance set built on (M, λ, x′ = 1 − x) and applied to world-2 vectors. x′ pushes λ to
     Lebesgue.
   - P1.11's proof uses only (λ, chain coordinate, blocks, N₊ rules), so it holds verbatim. Lemma vectorform then applies.
   - On N₊ the two worlds' error sets coincide, so D(·) is the same functional.
2. **Closed sections.**
   - World 2's error set at C_b is d_b = {x′ ≤ 1−b}, which is c′_{1−b} mod null.
   - So its section is {b : 1−b ∈ S′(X)}, where S′(X) is P1.12's closed initial segment, or [0,1] for non-regular X.
   - Hence it is a closed final segment. In p it is the preimage under the continuous map p ↦ p₂.
3. **Competitiveness.** I re-derived all cases.
   - *Vertices.* (G) gives C₀ = P₁ competitive on {1}, and likewise C₁ = P₂ on {2}.
   - *N_X non-null.* D(δ) = λ(N_X) > 0, so R⁺ accepts at world 1.
   - *X regular, λ(Q) ≥ λ(P).* For t ≤ b, τ(t) = λ(Q) − λ(P ∩ {x ≥ t}) ≥ 0. For t > b, τ(t) = λ(Q ∩ {x ≥ t}) ≥ 0. So the
     vector is in T ⊆ 𝒜.
   - *X regular, λ(P) > λ(Q).* The head integrals of 1_P − 1_Q are ≥ λ(P) − λ(Q) > 0 for s ≥ b, and ≥ 0 for s < b. So
     the vector is in T′.
4. **No weak domination ⇒ C_L = U_L = {C_b}, and (C).**
   - R⁻ makes N_X null. T2n.0 makes Q null. The world-2 vector is then −1_P, and mirrored strictness makes P null.
   - Theorem kkm: an undominated Y has a selected C ⪯_k Y at both worlds, hence (being undominated) Y ⪯_k C at both,
     hence Y = C.
   - C_b is undominated by the same argument, and C_b is coherent.
   - (C): a model tied with C_b at both worlds is C_b. (LA) holds.
5. **(LF):** C2.1(4), a domain/path property, imported from P1 [R1].
6. **Blindness, (NC), (M2).**
   - P1.13 uses only world-1 acceptances of relevant comparisons, i.e. cut pairs at v_n and T-moves out of C_b ∈ C_L.
   - It uses world 2 nowhere: its only use of C_L is C_L = {C_b}, which holds here. Mirror at world 2.
   - Λ^ca = M via Q3 §4 item 2.
7. **(Loc) ∖ (Loc_int). GAP (statement).**
   - ¬(Loc_int) holds for every parameter choice (Λ_∞ = M, K3.1(e)).
   - (Loc) is P1.14, proved **for a suitable choice of the free parameters**: the min I_n condition, strips of equal
     λ- and φλ-mass, and s_k ≤ 2^{−k}/φ_k.
   - *Fix:* state T2n.1 with "with P1.14's parameter choice at each world (made independently)". The designs do not
     interact.

NUMERICS (B) and (C) reproduced. (C) is the computation in item 3, so it is not independent evidence.

**Corollary T2n.2: CORRECT.**
- 𝓔_ij is closed under splicing and under convergence in measure. Its advice range is single-valued on Q_k ∩ U, so it
  is decomposable.
- Sign analysis: E_i(C_s) ∩ R_ij = {σ < s} in both orientations of R_ij, and C_s = P_i on Q_k. So C_s ∈ 𝓔_ij, and
  C_s = D_{co(K′∪{(1−s)e_i+se_j})} is coherent.
- F is continuous, because level sets of σ are null cones. Flat parts of F only repeat models.
- Q_k carries no error differences.
- **The consistency conclusion is CORRECT.** The axioms (a)–(c) on one edge are consistent with "neither world's edge
  comparisons have a nonzero CA endorser".
- **GAP (label).** The sentence "N2.1, N2.2, N1.1, N1.2, N1.4–N1.6 are consequences of (a)–(c) and K3.1" is not
  proved in the note. N2.1 as proved uses the three-world maximal endorsers. Label it as a reading, or drop it: the
  consistency statement does not need it.

### 2.3 Theorem T2n.3: CORRECT (priority 5)

- *Y° is consistent:* on Q_i and Q_j (both ⊆ R_ij) the overlap is null, and on Q_k worlds i and j agree. Y° is regular.
- *(P1) at k:* D^k = ∅ is a localizing family, and (CA⁺) endorses all relevant comparisons.
- *(P1) at l:* for every m, "≤ 0 on D̃^l_m ∖ E_l(Y°)" implies "≤ 0 on D̃^l_{max(m,m₀)}", since E_l(Y°) misses D̃^l_{m₀}.
  So the comparison is D̃^l-localized, and the enlarged data endorse it (Q2.10(a)).
- *(P2):* E_l(Y°) ⊆ M ∖ D̃^l_{m₀}, where ρ_l ≤ m₀.
- *(P3)* and positivity hold, because (Loc) densities are > 0 a.e.
- K3.5 [R1] closes it.
- The Reading ("≥ 2 non-(CA⁺) worlds" via H1.2) is correct.

### 2.4 Proposition T2n.4: CORRECT; the "Consequence" overclaims (priority 4)

- **(a) c ≡ 0.**
  - (γ₀) holds trivially. B_t = N₊ (with ρ := 1 there), T1 ∩ M ⊆ Z, A = Δ, and every pair is in the joint-blind
    alternative. Correct, and indeed trivial.
  - The second field (blind exactly on E₁(T1) ∩ M) is also correct: E₁(T1) ∩ R₁ⱼ ⊇ J_k is non-null, so pairs (1, j) are
    jointly blind.
- **(b) (ρσ₁, 0, 0).**
  - B_t = P₁ for t₁ > 0, coherent.
  - A(c) = [e₂, e₃], since T1 ≠ P₁ on a non-null set ((R3)).
  - Pairs (2,1), (1,2): the between model P₁ = D_{co(K′∪{e₁})}, which meets [e₁, e₂] at e₁.
  - Extra clause for (1, j): e_θ = θ ≥ 0, so the extreme models are P₁, and P_j at θ = 0. Correct.
- **(c) (0, σ₂1_{M∖Λ⁰}, σ₃).** I re-derived the four regimes and the q₂ = q₃ line.
  - On R₂₃ ∖ Λ⁰, sign(t·c) = sign((t₂−t₃)σ₂). On Λ⁰ it is σ₃. On Q₁ it is σ₂ = σ₃.
  - So B_t = P₃ (t₃ > t₂), C^{23}_{s₀} (t₂ > t₃), and C^{23}_{s₀} ∩ P₃ (t₂ = t₃).
  - D_K ∩ D_{K″} = D_{co(K∪K″)}.
  - (R2): 0 mismatches over 300 random t, three geometries.
  - A(c) = {e₁}: J₁ is non-null, and T1 is non-Bayes at 200/200 random p ≠ e₁.
  - Λ⁰ ∩ Q₂ ∩ U is non-null (≈ 18 000 of ≈ 10⁵ samples).
  - Extra clause for pair (2,3): extreme models P₃, C^{23}_{s₀}, P₂, all coherent.
- **"Consequence": GAP (overclaim).**
  - "So (PD), (E), (X) can be closed only by ranking-level arguments" (and §0 item 2's "cannot be closed by any
    field-level argument") goes beyond what is shown.
  - Proved: the field questions **as posed** (Q_N1 with N1.2 and N2.3′(d)) are Yes, so no argument using only those
    field properties closes these configurations.
  - Other field-level necessary conditions of a maximal tuple were not checked against these fields. Examples: N2.5's
    tie structure, L4.3's location facts beyond J_l, or properties specific to c* being **maximal**.
  - *Fix:* restrict the sentence accordingly. The comparison with M1.1′(c) is apt and can stay.

### 2.5 Proposition T2n.5: CORRECT (priority 6)

- **(a)** Forced pairs (M2 §1) need ψ_j(X) < ψ_j(C) for j ∈ S ∖ {1}. With ρ^ca_2 = ρ^ca_3 = 0 (Q3.20), only S = {1}
  survives.
  - Then C is competitive on {1}, so C = P₁.
  - Limit pairs with constant support {1} are the constant sequence at e₁.
  - So every vector of 𝔉𝔏 is ≥ 0, normalised μ is in 𝒩(𝔉𝔏), and the maximal-support φ* has ρ♮₁ > 0 a.e.
  - The rest is T2n.4(b)'s computation.
- **(b)** The witness: (1, 1, −c) ∈ U ∖ cl D_{T1} iff 2c₀/(c₀+ε) < c < 2c′/(c′+ε′), a non-empty interval since
  ε′/c′ < ε/c₀ ((R4): for example (0.875, 0.948) at ε = 0.3, s = 0.9). There p·c♮ ≥ p₁ρ^ca_1 > 0, while T1 rejects.
  e₃ ∈ A. Correct.
- **(c)** Mirror. Correct.

### 2.6 Lemma T2n.6: CORRECT

- h = 1_{P∖R} − 1_Q has ν(h) ≥ 0, and g + h = −1_R is ternary, nonzero and ≤ 0.
- Non-atomicity of ν ~ μ supplies R.
- The Reading after it (interior indices) is unlabelled heuristics. Fine as such.

### 2.7 Proposition T2n.7: CORRECT for small η; GAP (trivial) in the statement

- (a) and (b) were re-derived.
  - For g = (a, −b, 1), min_k v_k·g = c₀(1+a−b) − εb.
  - For W_η, v₂·g > 0 iff c > κ − a, with κ = 1 + ε/c₀ = (1+2ε)/(1−ε), the same κ as the script.
  - (R6) samples the note's full range c ∈ (κ, κ+1): all in U ∩ D_{T1}.
- **GAP.** "(a) For every η ∈ (0,1): 𝔈^{12}_2(η) ∩ 𝔈^{23}_3(η) ⊇ H_η" is false for large η. The 𝔈's are subsets of U,
  and H_η ⊄ U once η > c′/(c′+ε′).
  - Example: ε = 0.6, s = 0.5, g = (5·10⁻⁴, −0.5, 1) ∉ U; the threshold is 0.4375.
  - *Fix:* state (a) for η < c′/(c′+ε′), or for H_η ∩ U.
  - Nothing downstream uses large η.

### 2.8 T2n.8: CHECKED stands (priority 8)

- The transfer of Q1.22 from (RL-2)-forced to designed cut moves is legitimate. Q1.22's continuous-case proof (cycles,
  (b), (c)) uses only acceptance of the two families of cut moves, strict (G) and (IB) [Q13_referee §1.4].
- In (E∗), world 2 accepts:
  - 12-cut moves at rate ρ₁, from Q1.20 with the additive world 1;
  - 23-cut moves at rate λ, because T contains every forward cut pair of equal or larger λ-mass.
- On Q₂ the linear-host coordinates are functions of |g₁|/|g₂| and |g₂|/|g₃|, which is (TC) as in Q1.26.
- (b) and (c) are correct consequences: ψ is finite on [0,1), and ψ′ is the mirror in x₃₂ = 1 − x₂₃.
- The whole item is conditional on a realisation of (E∗), which the note does not construct. It should say so in its
  first line.
- *Remark.* T1n.5 now gives a measurable-density version of Q1.22–Q1.23. Using it here would also need Lemma T1n.1 for
  designed moves (capacity and window at the far vertex). That holds if world 2's sections are closed, as (S) requires.

### 2.9 Proposition T2n.9: CORRECT (priority 7)

- (a): F_l is closed, e_l ∈ F_l, so by connectedness some p is in F_i ∩ F_j.
  - Both comparisons are relevant and localized, so ρ_l(E_lC) < ∞.
  - On R_ij a model errs at exactly one of i, j.
  - The vertex case p = e_i is covered by the same count: then ρ_j(R_ij) < ∞ from p ∈ F_j.
- (b) and (c) follow by competitiveness and transitivity.
- **Upgrade available.** The first Reading bullet is a complete proof.
  - If D̃^i_a ∩ D̃^j_a ∩ R_ij were null, let Y be i-correct on D̃^i_a and j-correct on D̃^j_a, err at the lower-density
    world on the rest of R_ij, and be correct at both off R_ij.
  - Y is regular, with ρ_l(E_lY) ≤ aμ(M), contradicting (c).
  - Also ∫_{R_ij ∖ (D̃^i_a ∩ D̃^j_a)} min(ρ_i, ρ_j) ≤ 2aμ(M).
  - So "under infinite minority mass every depth is sheltered, and all but finite minority mass sits in the overlap" can
    be labelled PROVED.

---

## 3. Requested changes

**T1n.**
1. T1n.3(iii), (v): make the (N2) statements local, and drop "only (N0) survives" (§1.3).
2. §0 item 4(ii), §7.1 item 2, §7.5: replace "χ-law not absolutely continuous" by "χ-law failing (TC_m)". Add the
   non-open a.c. case. Mark §7.5's (N)-band item as conditional on T1n.C, and write "(M1) or (N)" (§1.6). Optionally
   prove the density-point form of T1n.5 suggested there.
3. §7.2: replace the citation of T1n.2(a) (§1.7).
4. T1n.4(a): one-sided J₀ when s₀ = y₀.

**T2n.**
5. T2n.1: add "with P1.14's parameter choice at each world" to the (Loc) clause.
6. T2n §1: label the "N2.1 … N1.6 are consequences of (a)–(c)" sentence as a reading, or delete it.
7. T2n.4 Consequence and §0 item 2: restrict to "field properties of Q_N1 / N1.2 / N2.3′(d)".
8. T2n.7(a): η < c′/(c′+ε′).
9. T2n.8: state its conditional status in the first line.
10. T2n.9: upgrade the first Reading bullet to PROVED.
11. NUMERICS: in (D), sample c ∈ (κ, κ+1) as stated. Note that (C) restates the item 3 computation.

**For R21 / the integrator.**
- T1n.2 + T1n.5 [R1 after this report] close "(V) with (CA⁺) partners, (Nest_e) and (TC_m) at e₁" with measurable
  densities. Under (Nest_e), the comonotone escape of Q24_referee §1.4 is gone.
- T2n.1/T2n.2 [R1] show that edge-only axioms never force a nonzero CA endorser at either world of a blind pair.
- T2n.4 [R1] shows that the field questions of (PD), (E), (X) as posed are Yes.

## 4. Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/t12nref_py/ref_checks.py`, `.out`:
  checks (R1)–(R7).
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/t12nref_py/t1n_rerun/`: copy and
  rerun of `t1n_band_chain.py` (identical).
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/t12nref_py/t2n_rerun/`: copy and
  rerun of `t2n_checks.py` (identical).
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/t12nref_py/t1n_rerun.out`: stdout of
  the first, in-place rerun (see the disclosure under Numerics).
