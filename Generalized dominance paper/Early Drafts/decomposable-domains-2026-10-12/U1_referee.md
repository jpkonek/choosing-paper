# Referee report on U1_notes.md (round 23)

16 Oct 2026. This is an adversarial reading. Verdicts are **CORRECT**, **GAP** (fixable; the fix is given) or **WRONG**.

I re-derived every PROVED item against:
- Q2_notes Part I (Q2.10–Q2.13, Q2.16) and Q24_referee §§1.1–1.2 (Q2.11(c) and Q2.12(a) are R1 there);
- Q1_notes Part I (Q1.20–Q1.26) and Q13_referee §§1.1–1.7;
- T1n_notes (T1n.1, T1n.2, T1n.5) and T12n_referee §§1.1–1.5, 2.8;
- T2n_notes §§1, 4 (T2n.1, T2n.2, the blueprint (E∗), T2n.7, T2n.8) and T12n_referee;
- R21_reduction §1;
- write-up §2 (D_K, C_L, axioms, Theorem kkm, §2.3 target, §2.5 U-domain, §2.7 relevant comparisons).

Scratch work is in `u1ref_py/`.

**Numerics.**
- `u1py/u1_checks.py` was rerun with `python3 -I -B` from inside `u1py/` (24 s), with output sent to a separate file.
  It is byte-identical to `u1py/u1_checks.out` (copy kept in `u1ref_py/u1_checks_rerun.out`). Every number quoted in U1 §§3 and 6 is reproduced.
- My own checks are `u1ref_py/ref_checks.py` (+ `.out`, 28 s) and three diagnostics `diag_R2*.py` (+ `.out`).
  - (R1) sympy: the identities of h, the Π₁₂ ∩ R⁽¹⁾ computation, and the slacks of m₀.
  - (R2) the U1.2(c) criterion (an LP for "K meets the segment") against sampling, on 1200 random K.
  - (R3) segment models are edge models and have the error sets of §6.1.
  - (R4) U1.5(c) in exact rational arithmetic, corners included.
  - (R5) U1.1(i) for the template on all three edges.
  - (R6) the x-ranges of (3.1).
- No verdict rests on numerics.

---

## 0. Verdicts

**Nothing is WRONG.** The main theorem chain U1.1 ⇒ U1.3 ⇒ U1.4 is correct. It is a genuine new obstruction: the
interior σ-finite admissibility of T1 (Q2.11(c)) is pushed onto the edges, where the third world's positive density
makes it strict. The facet geometry of T1 (the overlap (1/κ, κ)) then forbids one-sided edge ratios. The template
U1.5 is correct, exactly, and not only numerically.

All the GAPs are small: status bookkeeping, one citation in the measurable case of U1.4, and wording.

| Item | Verdict |
|---|---|
| **U1.1(i)** strict edge inequalities r_ij < θ_ij on W_i, > on W_j | **CORRECT** |
| **U1.1(ii)** E^{θ,−} = C_q with q in the open edge; it agrees with T1 on W_i ∪ W_j | **CORRECT** |
| (3.1) charts and x-ranges | **CORRECT**. GAP (minor): state the Fubini form (§2.1). §5 item 2 needs it |
| **U1.2(a)** Π₁₂ | **CORRECT** |
| **U1.2(b)** R⁽¹⁾, R⁽²⁾, minimax | **CORRECT** |
| **U1.2(c)** Π₁₂ ∩ R⁽¹⁾ = [m₀, v₁]; characterisation | **CORRECT** (exact check (R1); LP vs sampling (R2)) |
| **U1.2(d)** no L_m separates; neither does P₁ or P₂ | **CORRECT** |
| **U1.2(e)** K_a, K_b separate and are edge models | **CORRECT**. Cosmetic: the slack list for m₀ is garbled; the last sentence (K ⊆ co(e₁, e₂, v′₃)) is not needed |
| **U1.3** | **CORRECT** |
| **U1.4**, continuous ρ₁ and dλ/dμ | **CORRECT** at PROVED level. The transfer of Q1.22–Q1.23 to designed 23-cut moves is legitimate (re-derived in §4.2; T12n_referee §2.8 says the same) |
| U1.4, measurable densities ("CHECKED via T1n.5") | **GAP (citation; fixable, then PROVED).** T1n.5 is R1, not "unrefereed". But T1n.5(a) rests on T1n.2(b), and through it on the window bound T1n.1. Step 4 does not mention this. Fix in §4.3 |
| Status bookkeeping (§0 table, §1, §7, U1.6) | **GAP (stale).** T1n.5 and T2n.2 are R1 (T12n_referee, 13:49). T2n.8 is "CHECKED stands, conditional on a realisation" |
| U1.4 Remarks | **CORRECT** |
| §5 item 1 (closes (E∗)) | **CORRECT** |
| §5 item 2 (one-sided ratio closes) | **CORRECT in substance. GAP (route):** "the separating model is a linear-host model" needs a monotone R. The direct argument from U1.1(i) needs no monotonicity (§5.1) |
| §5 "Why T2n missed it", "Not closed" | CORRECT as a reading |
| **U1.5(a)–(d)** | **CORRECT** (all four parts re-derived; exact check (R4)) |
| U1.5 "passes Q2.11–Q2.14 and U1.1–U1.3" | **GAP (wording).** Correct for the field-level items (Q2.11(c) at p̂ = u, Q2.12–Q2.13, Q2.14(a), U1.1). Q2.11(a), (b) and Q2.14(b) concern the selection or the bounded endorsers, which the template does not specify. Say which items |
| Linear host = R₊(x)R₊(1/x) ≡ 1, forbidden; segment host = "≥ 1" | **CORRECT** (within the single-rule family; in general, R₊ ≥ R₋) |
| U1.6 edge blocks | Fine at the status of T2n.2 [R1] plus a one-line transfer to nested segment chains. Better labelled CHECKED than "PROVED at the status of T2n.2" |
| U1.6 (Loc) of worlds 2, 3 | Properly labelled CONJECTURE. It is likely a short lemma (§6.3) |
| **Q_U1** | **Well posed.** GAP (citation): "U1.3 shows it cannot be answered No at edge-plus-admissibility level" should cite **U1.5**. "By K1.6 [R1]" is a reading in the σ-finite setting (T2n §5 says so) |
| NUMERICS (A)–(F) | Reproduced exactly. In `check_D`, the variable `accQ` (edge-model property on Q_k) is computed and never used; (R3) supplies that check |

**Nearby sharpening (§3.4), available now:** in any all-(Loc) cover whose {i, j}-edge selection consists of segment
models, the selected model at level θ_ij is **exactly** S[m₀, m₀′] = K_a, whatever p̂ is. Segment hosts are therefore
rigid at the separating level, which is useful input for Q_U1.

---

## 1. Inputs and their status

- **Q2.11(c)**: D_{T1} = B_{p̂} ∪ S′ with S′ ⊆ Z_{p̂} and p̂ ∈ Δ°. This is R1 (Q24_referee §1.1). Its hypotheses are (H_U)
  and (Loc) at every world. Enlarging the data changes the families but not ρ_k. So U1.1 may use the original
  densities.
- **Q2.12(a)**: E^{θ,±} ∈ C_L. This is R1 (Q24_referee §1.2), including (LA), which (H_U) has.
  - The proof shows X = C_p for the p ∈ [e_i, e_j] given by M1.3. In the interior case "X = C ∈ C_L". In the vertex
    case X = P_i = C_{e_i}.
  - So U1.1(ii)'s "E^{θ,−} = C_q, q ∈ [e_i, e_j]" is literally in the proof. This answers the author's risk point 2.
- **Q1.20–Q1.23, Q1.26**: R1 (Q13_referee). Q1.23 has a quantifier GAP, and the fix is routine.
- **T1n.5**: R1 (T12n_referee §1.5: "CORRECT. This is the write-up of Q13_referee §1.4–1.5, done right"). U1's
  "unrefereed" (§1 table, §7) is stale.
- **T2n.2**: R1 (T12n_referee: "CORRECT"). **T2n.8**: "CHECKED stands, as a reading conditional on a realisation of
  (E∗)" (T12n_referee §2.8). U1's "T2n unrefereed" is stale on both counts.

---

## 2. Theorem U1.1: CORRECT

### 2.1 Geometry used by U1.1 and U1.2

I re-derived the charts. min_{m∈co V} m·g = c₀Σg + ε·min_k g_k, and the same holds for K′ with (c₀′, ε′).
- **O_l⁺**, chart |g_l|(e_l − a e_k − b e_{k′}). With a ≥ b, T1 is c₀(1 − a − b) − εa > 0 ⟺ κa + b < 1. So T1 there is
  the quad, with vertices (0,0), (1/κ, 0), (0, 1/κ) and (c, c), c = 1/(κ+1).
- **O_l⁻**, chart |g_l|(−e_l + a e_k + b e_{k′}). T1 is a + b > 1 + ε/c₀ = κ, and U is a + b > κ_U, with
  κ_U = (1+2ε′)/(1−ε′) < κ.
- **W_l.** On O_l⁺ world l says "accept", and on O_l⁻ it says "reject". So W_l = (O_l⁺ ∩ D_{T1}) ∪ (O_l⁻ ∖ D_{T1}) is
  right. W_l ⊆ Q_l ⊆ R_ij for each i ≠ j containing l.
- **(3.1).**
  - For O₁⁻ ∖ D_{T1} in the chart (−1, s, t): x = s, and for every s ∈ (0, κ) the t-section
    (max(0, κ_U − s), κ − s) is non-empty.
  - For O₂⁻ ∖ D_{T1} in the chart (s′, −1, t′): x = 1/s′ ∈ (1/κ, ∞).
  - (R6) confirms the ranges numerically.
  - *Minor GAP.* The note states only "non-null for every **open** J". By Fubini, the stronger statement holds: the
    law of x under μ restricted to O₁⁻ ∖ D_{T1} is equivalent to Lebesgue measure on (0, κ), and likewise on (1/κ, ∞)
    for O₂⁻ ∖ D_{T1}. The chart is a smooth bijection of rays, and every section has positive length. U1.2(d) needs
    only the open-J form. §5 item 2 needs the Fubini form (§5.1 below). State it.

### 2.2 U1.1(i)

This is the author's risk point 1. I checked it on both orthants of W_i.
- On Q_i world i is odd, and σ_j = σ_l = −σ_i.
- On O_i⁺ ∩ D_{T1}, T1 accepts, so p̂·c ≥ 0 a.e. (D_{T1} ⊆ B ∪ Z). That is p̂_iρ_i − p̂_jρ_j − p̂_lρ_l ≥ 0.
- On O_i⁻ ∖ D_{T1}, T1 rejects, so p̂·c ≤ 0 a.e. (B ⊆ D_{T1}). That is −p̂_iρ_i + p̂_jρ_j + p̂_lρ_l ≤ 0. This is the same
  inequality.
- Strictness uses **both** p̂_l > 0 (p̂ ∈ Δ°) **and** ρ_l > 0 a.e. The note says only the latter. Add "p̂_l > 0".
- Dividing by ρ_i ∈ (0, ∞) gives r_ij < θ_ij. On W_j ⊆ Q_j, exchange i and j.

**CORRECT.** It is a pure field-level consequence of Q2.11(c). No ranking-level input enters (i).

### 2.3 U1.1(ii)

- θ := θ_ij/(1+θ_ij) gives θ/(1−θ) = θ_ij. The world-i errors of E^{θ,−} on R_ij are {e_θ < 0} = {r_ij > θ_ij} (Q2 §1).
- Selected, hence coherent and equal to C_q (§1 above).
- Agreement with T1:
  - on W_i both are right at i;
  - on W_j, X errs at i, so it is right at j (the two worlds of R_ij disagree), as T1 is;
  - "on U the advice is determined by the error status at one world" holds (accept or silence).
- q is interior. X errs at i on W_j (non-null), so X ≠ P_i. X is right at i on W_i (non-null), while P_j errs at i on
  all of R_ij, so X ≠ P_j. And C_{e_i} = P_i by strict (G).

**CORRECT.** *Remark (wording):* the list of inputs in the Remarks should include (S) as well as strict (G), (IB) and
(LA).

---

## 3. Lemma U1.2: CORRECT

### 3.1 (a) Π₁₂

- m·g = m₁ − m₂a − m₃b is affine in the chart. Non-negativity at the four quad vertices gives exactly the six
  inequalities (plus m₁ ≥ 0).
- The interior argument is right. An affine function ≥ 0 on a polygon that vanishes at an interior point vanishes
  identically, and that forces m = 0. Compactness of K gives min_K > 0 pointwise.
- Converse: a negative vertex value gives a non-empty open set of the quad that D_K rejects.
- The mod-null remark is fine.

### 3.2 (b) R⁽¹⁾, R⁽²⁾ (risk point 5)

- *If.* For m ∈ R⁽¹⁾ and s + t ≤ κ: m₂s + m₃t ≤ κ max(m₂, m₃) ≤ m₁. So D_K rejects.
- *Only if.* F is bilinear on compact convex K × Tr, so von Neumann/Sion applies. A maximiser may lie on s + t = κ or on
  an axis. Continuity uniform on K gives a non-empty open set with s, t > 0 and s + t < κ inside D_K. D_K ⊆ U gives
  s + t > κ_U automatically, so these gambles lie in O₁⁻ ∖ D_{T1}.
- *Closure case* e₁ ∈ K: e₁ ∈ R⁽¹⁾ and D_K ∩ O₁⁻ = ∅. Consistent.

### 3.3 (c), (d), (e)

- **(c).** On R⁽¹⁾ ∩ Π₁₂ we get m₁ = κm₂ and m₃ ≤ m₂. (R1) gives the slacks of the remaining inequalities at
  (κ, 1, μ): (κ−1)(κ+1), κ² − μ, κ² + κ − μ − 1, κ − μ, 1 − μ, κ(1 − μ). All are ≥ 0 for μ ∈ [0,1] and κ > 1.
  - The normalised point (κ, 1, μ)/(κ+1+μ) has m₂ ≥ c₀ ⟺ μ ≥ 1 and m₃ ≥ c₀ ⟺ μ ≥ 1. So only v₁ = c₀(κ, 1, 1) is in T1.
  - (The note's "m₂ < c₀ for μ > 1" concerns values of μ outside [0,1]. It is harmless, but should read "m₃ < c₀ for
    μ < 1".)
- **(d).** In the chart of O₁⁻, L_m accepts {s > m₁/m₂}. This meets O₁⁻ ∖ D_{T1} in a non-null set iff m₁/m₂ < κ, by
  (3.1). In the chart of O₂⁻, L_m accepts {s′ > m₂/m₁}, non-null iff m₂/m₁ < κ. Separation needs both ratios ≥ κ, so
  κ² ≤ 1, which is impossible. The endpoints m = e₁, e₂ are P₁, P₂ and are included.
  - **CORRECT**, and this answers risk point 3: the overlap (1/κ, κ) of the two x-ranges is non-empty exactly because
    κ > 1.
- **(e).**
  - K′ ⊆ T1 ⊆ Π₁₂: apply (a) to D_{T1} itself.
  - m₀'s slacks are (κ−1)(κ+1), κ², κ² + κ − 1, 0, κ, 1 ((R1)). The note's list "κ²/(κ+1) ≥ 1/(κ+1), κ ≥ 1/(κ+1), …"
    does not match the six inequalities. This is cosmetic.
  - Edge model on Q₃: re-derived. In (+,+,−), U forces c < c₀′(a+b)/(c₀′+ε′), so v₁·g ≥ c₀(a+b)ε′/(c₀′+ε′) > 0.
    Edge points are positive, and so is K′.
  - The inclusion K ⊆ co(e₁, e₂, v′₃) is true (γ = c₀/(c₀′+ε′) ≤ 1, non-negative remainder), but nothing uses it.
- **Numerics.**
  - (R2): on 1200 random K, the criterion "K ⊆ Π₁₂ and K meets [m₀, v₁] and [m₀′, v₂]" (an LP) never says "separates"
    when sampling finds a violation (0/53).
  - Conversely, 8 of 1147 "does not separate" cases showed no sampled violation.
    - Targeted chart sampling (`diag_R2.out`) finds the violation in all but one of them.
    - The ε = 0.1 cases are all marginal (`diag_R2b.py`). Either a Π₁₂ slack is ≈ −10⁻³ (a thin sliver at a quad
      vertex), or an edge point misses m₀′ by a ratio 1.325 vs κ = 1.333.
    - Sampling inside the predicted sliver for the latter gives 200 000/200 000 witnesses (`diag_R2c.out`).

### 3.4 Nearby sharpening (available now; PROVED here)

T1 lies on the side m₁ ≤ κm₂ of the line e₃v₁ = {m₁ = κm₂}, and touches it only at v₁ (v₂ and v₃ satisfy the inequality
strictly). K′ ⊆ relint T1. So a segment model co(K′ ∪ [a, b]) with a, b ∈ [e₁, e₂] can meet [m₀, v₁] only on [a, b],
i.e. only if a₁/a₂ ≥ κ (a is at least as far toward e₁ as m₀). Membership in Π₁₂ forces a₁/a₂ ≤ κ. So a = m₀, and
symmetrically b = m₀′.

**Corollary.** If the {i, j}-edge selection of an all-(Loc) cover consists of segment models, then the U1.1 model at
level θ_ij is exactly S[m₀, m₀′], whatever p̂ is. In ratio form: α(θ_ij) = κ and β(θ_ij) = 1/κ. Equivalently, R₋ < θ on
(0, κ), R₋ > θ on (κ, ∞), R₊ < θ on (0, 1/κ) and R₊ > θ on (1/κ, ∞). The last two conditions come from the quad parts of
W₁ and W₂, which §6.1 does not list.

This is the rigidity that Q_U1 must live with, and U1.5(d) is its instance at p̂ = u.

---

## 4. U1.3 and Corollary U1.4

### 4.1 U1.3: CORRECT

The selected X_ij of U1.1(ii) is not any L_m a.e., by U1.2(d) transported by the coordinate permutation (which
preserves T1, K′, U). So the selection on {i, j} contains a non-linear-host model. A "linear-host edge selection" means
every C_p, p ∈ [e_i, e_j], is some L_m mod null. The statement and proof are right as worded.

### 4.2 U1.4, continuous case: CORRECT

I checked each step against Q1 and T2n.
1. *World 1.* (CA⁺) = (RL-2) with an integrable positive density. The datum (ρ₁, ∅) is (Loc).
2. *12-cut moves at world 2.* Q1.20 with world 2 in the role of world 1 and world 1 as the (RL-2) partner. Its
   hypotheses hold:
   - C ∈ C_L competitive on {1, 2} at interior chain levels;
   - a nested linear chain without jumps (N1.4(a));
   - a coordinate pushing ρ₁μ|_{R₁₂} (normalised) to Lebesgue, continuous because the level cones are null.
3. *23-cut moves at world 2.* The computation that 1_T − 1_S ∈ T′ for S ⊆ {x′ < b′}, T ⊆ {x′ ≥ b′} and λ(T) ≥ λ(S) is
   right:
   - for t ≤ b′: λ(T) − λ(S ∩ {x′ ≥ t}) ≥ λ(T) − λ(S) ≥ 0;
   - for t > b′: λ(T ∩ {x′ ≥ t}) ≥ 0.

   The orientation matches T2n.1 step 3 ("1_Q − 1_P ∈ T ⇒ C_b ⪯ X"), since world 2's errors are initial in x′. The
   comparison lies in 𝓔₂₃, and the hypothesis "comparisons supported in R₂₃ are those of T2n.1" together with Lemma
   vectorform carries it to the three-world ranking.
4. *(TC) at Q₂.* Apply Q1.26 under the transposition (1 2). The chain coordinates are continuous strictly increasing
   functions of |g₂|/|g₁| and |g₂|/|g₃| (base measures ρ₁μ and λ have positive densities), and I₂ = I₃ = (0,1).
5. *Transfer of Q1.22–Q1.23.* This is the author's risk point 4, re-derived.
   - Q1.22(a)–(b) (cycles, monotonicity) use the partners only through accepted cut moves with mass ratio > 1 in the
     step's base density, plus non-atomicity and continuity of the two base densities on neighbourhoods V^i. Q1.22(c)
     is not needed for (Loc).
   - Q1.23 uses only cut moves, Q1.21, strict (G), (IB), Lyapunov and the localizing family.
   - (RL-2) enters only inside Q1.20. Designed moves accept with "≥", which is stronger than Q1.20's ">".
   - The bases are ρ₁ on R₁₂ and dλ/dμ on R₂₃. Both are integrable and positive. Continuity is assumed in the PROVED
     case. In T2n.2's literal (E∗), λ is normalised μ, so dλ/dμ is constant.
   - (TC3) makes ρ*₂ finite and positive on Q₁ (via x₂₁) and on Q₃ (via x₂₃).
6. *World 3* by (2 3). *Contradiction* by U1.3 on any one edge.

**CORRECT at PROVED level for continuous ρ₁ and dλ/dμ**, at the status of Q1.22–Q1.23 [R1] with Q13_referee's
quantifier fix. T12n_referee §2.8 independently found the transfer legitimate.

One clarification: only one linear edge is needed, but U1.1 still needs **all three** worlds (Loc), because Q2.11(c)
does. So world 3's step (5) is not optional, even when only the 12-edge is used. The Remark states this correctly.

### 4.3 U1.4, measurable case: GAP (citation), fixable to PROVED

Step 4 justifies the measurable case by "T1n.5(a),(b), whose proof also uses only cut moves (T1n §6: 'only ω enters')".
That is incomplete.
- T1n.5(a) begins "By T1n.2(b), ω = Ω∘χ". T1n.2's Step 4 (climbing on comonotone points) uses the **window bound,
  Lemma T1n.1(b)**, and T1n.1 uses closed b-sections at the far vertex and the capacity argument.
- **Fix.** In T1n.2 Step 4 the window bound is applied on one edge only, and it may be taken on world 2's **12-edge**,
  whose partner, world 1, is a genuine (RL-2) world. So T1n.1 applies verbatim there:
  - closed sections along [e₁, e₂] from (S);
  - no jumps from N1.4(a);
  - λ = ρ₁μ.
- The 23-chain enters T1n.2 and T1n.5 only through accepted cut moves (Step 1, the climbing moves, the rook
  identities, the routing of (b)). Designed moves supply these.
- (TC_m) for the linear host is in T1n §1 (with π ~ Leb: the chain reparametrisations are absolutely continuous with
  a.e.-positive derivative because the bases are a.e. positive).
- With this paragraph added, the measurable case is **PROVED at the status of T1n.5 [R1]**. Without it, CHECKED is the
  fair label. T12n_referee §2.8 flagged exactly this point ("would also need Lemma T1n.1 for designed moves"). The
  observation above removes even that need.

---

## 5. §5 (what is closed)

### 5.1 One-sided ratios: CORRECT, GAP in the route

§5 item 2 argues: "if r_ij is a function of |g_j|/|g_i| alone, the same on both sides, then the separating model
{r_ij > θ_ij} is a linear-host model". That needs {R > θ} to be a half-line, i.e. R monotone. Q2.12–Q2.13 do give
monotonicity up to ties, but the note does not say so.

The direct argument is cleaner and needs nothing beyond U1.1(i) and the Fubini form of (3.1):
- R < θ for Lebesgue-a.e. x ∈ (0, κ) (from O₁⁻ ∖ D_{T1} ⊆ W₁);
- R > θ for Lebesgue-a.e. x ∈ (1/κ, ∞) (from O₂⁻ ∖ D_{T1} ⊆ W₂);
- these contradict each other on (1/κ, κ), which has positive length since κ > 1.

Replace the sentence with this.

### 5.2 The rest of §5

- Item 1, item 3 and "Not closed" are accurate.
- "Why T2n missed it" is a fair reading: the bounded field c♮ = (ρσ₁, 0, 0) of T2n.5(a) has no third density, and U1.1's
  strictness lives exactly there.

---

## 6. Proposition U1.5 and §6

### 6.1 U1.5: CORRECT (re-derived, and exact in (R4))

- **h.**
  - The two pieces agree at c (value 1/2), and h(1/κ) = 1.
  - The corner identity h(t) + h(1 − κt) = 1 on [c, 1/κ] is an exact identity in sympy, because 1 − κt ∈ [0, c] lands
    on the first piece.
  - h ≥ t/κ holds at 0, c and 1/κ, and both sides are piecewise linear with the same breakpoints.
- **(a).** Only pairs of opposite sign get a ratio. On O_l⁺ these are (l, k) and (l, k′); on O_l⁻ they are (k, l) and
  (k′, l). So the rule is consistent, and r_ij = R₊(x) on {g_i > 0 > g_j} and 1/R₊(1/x) = R₋(x) on the other side.
- **(b).** R₊ ≥ R₋ ⟺ R₊(x)R₊(1/x) ≥ 1. The three ranges check: κh(x)/x ≥ 1, κ², and the mirror.
  - B_t on R_ij: world-i errors {R₊(x) > s} = {x > R₊⁻¹(s)} on the + side and {x > R₋⁻¹(s)} on the − side. This is
    S[a, b] with α = R₋⁻¹(s) ≥ β = R₊⁻¹(s).
  - On Q_l, B_t = P_i. At a vertex, B_{e_i} = P_i = S[e_i, e_i].
  - (R3) confirms the error sets of §6.1 and the edge-model property for 40 random segments per (ε, s), on all three
    edges.
- **(c)** (risk point 6).
  - *One-positive chart.* If a or b > 1/κ, the bracket is < 0 and the point is outside the quad. On (0, 1/κ]² with
    a ≥ b, the binding facet is κa + b < 1 (since (κ−1)(a−b) ≥ 0). The two cases a ≤ c and a ∈ (c, 1/κ] are right; the
    second uses h(b) < h(1 − κa) ⟺ b < 1 − κa.
  - *Two-positive chart.* ρ_k/ρ_l = 1/R₊(|g_l|/|g_k|) = R₋(a). The bracket is (a+b)/κ − 1 for a, b ≤ κ. For a > κ,
    R₋(a) = 1/h(1/a) > 1, so the bracket is > 0 and a + b > κ.
  - (R4): exact rational arithmetic for ε ∈ {1/10, 3/10, 3/5, 9/10} on 30 260 grid points per ε (corner (c,c), c ± 10⁻⁶
    and 1/κ included). Zero mismatches, and the bracket is exactly 0 on every boundary grid point. So **B_u = D_{T1}
    up to the null set ∂D_{T1}**.
- **(d).** r₁₂ = R₊(a) < 1 − R₊(b) < 1 on the quad, and R₋(a) < 1 on the rejected part of O₁⁻. The level 1 has
  α = R₋⁻¹(1) = κ and β = R₊⁻¹(1) = 1/κ, so the model is S[m₀, m₀′] = K_a. (R5) confirms U1.1(i) on all three edges.
- **Reading paragraph.** "B_q incoherent for a non-null set of interior q, by M0closed(a)" is right as a consistency
  remark (strictly signed field, T1 admissible at u).

### 6.2 Scope of "passes Q2.11–Q2.14 and U1.1–U1.3": GAP (wording)

What the template verifies is field-level only:
- Q2.11(c), at p̂ = u, strictly;
- Q2.12–Q2.13: edge ratios are 0-homogeneous, strictly increasing, and their chains are coherent segment hosts;
  c = hĉ; (γ) holds on ∂Δ;
- Q2.14(a) (automatic for any field);
- U1.1(i), (ii);
- U1.3 (not linear).

Q2.11(a), (b) concern selected models C_p, which the template does not specify. Q2.14(b) concerns bounded endorsers.
Write "passes the field-level conditions Q2.11(c), Q2.12, Q2.13, Q2.14(a), U1.1".

Also, §6.1's "a separating level needs R₋ < 1 on (0, κ) and R₊ > 1 on (1/κ, ∞)" lists only the rejected-region
conditions. The quad parts of W₁, W₂ add R₊ < 1 on (0, 1/κ) and R₋ > 1 on (κ, ∞). With monotonicity this pins the
level-1 thresholds exactly (§3.4).

### 6.3 U1.6 and the (Loc) conjecture

- **Edge blocks.** T2n.2 [R1] uses a nested chain of coherent edge models with an atomless chain coordinate. Segment
  hosts have this: level cones {R±(x) = s} are null, and α, β are continuous. So "PROVED by T2n.2's proof" is
  acceptable once that sentence is added. As written, "PROVED at the status of T2n.2, which is unrefereed" is stale and
  slightly overstated. **CHECKED** is the accurate label until the sentence is added.
- **(Loc) of worlds 2, 3.** Labelled CONJECTURE, which is correct. It looks close to a short lemma: a segment-host
  analogue of Q1.26.
  - On each of the two orthants of Q₂, χ is a product of strictly monotone functions of |g₁|/|g₂| and |g₃|/|g₂|, so it
    is a homeomorphism onto an open set.
  - (TC2) follows if the first-coordinate projections of the two images overlap.
  - (TC3) holds with full intervals.

  This is the natural next step before Q_U1.

### 6.4 Q_U1: well posed

- **Mis-citation.** "U1.3 shows it cannot be answered No at edge-plus-admissibility level" should read **U1.5**. U1.3
  is the obstruction; U1.5 shows that segment hosts survive it.
- "By K1.6 [R1] it needs anti-safe indices": K1.6(b)3 is proved for integrable base endorsers, and its σ-finite use is
  a reading (T2n §5 says so). Label it accordingly.
- By §3.4, any positive answer must select **exactly** S[m₀, m₀′] at level θ_ij on each segment edge. That is a concrete
  constraint for a construction.

---

## 7. Requested edits, in order of importance

1. U1.4 Step 4, measurable case: add the T1n.2/T1n.1 paragraph of §4.3 (window bound on the 12-edge, genuine (RL-2)
   partner). Then relabel the measurable case PROVED at the status of T1n.5 [R1].
2. Update statuses:
   - T1n.5 [R1];
   - T2n.2 [R1];
   - T2n.8 CHECKED stands (conditional);
   - U1.6 edge blocks CHECKED (or PROVED with the one-line transfer).
3. §5 item 2: replace the linear-host route by the direct U1.1(i) argument, and state the Fubini form of (3.1).
4. U1.1(i): name p̂_l > 0 alongside ρ_l > 0. Add (S) to the Remarks' input list.
5. U1.5: restrict "passes …" to the field-level items. Complete the level-1 conditions in §6.1.
6. Q_U1: cite U1.5 instead of U1.3; mark the K1.6 use as a reading. Optionally add the rigidity corollary of §3.4.
7. Cosmetic:
   - m₀'s slack list in U1.2(e);
   - the μ-direction remark in U1.2(c);
   - the unused K ⊆ co(e₁, e₂, v′₃);
   - the dead `accQ` variable in `check_D`.

---

## 8. Files

- `u1ref_py/ref_checks.py`, `ref_checks.out`: (R1)–(R6) as listed at the top.
- `u1ref_py/diag_R2.py`, `diag_R2b.py`, `diag_R2c.py` (+ `.out` where written): diagnosis of the marginal (R2) cases.
  - They use targeted chart sampling.
  - They import `ref_checks` from their own directory, with an explicit `sys.path` insert, because `-I` drops the
    script directory.
- `u1ref_py/u1_checks_rerun.out`: the rerun of `u1py/u1_checks.py`. It was written outside `u1py/` and is identical to
  `u1py/u1_checks.out` (`diff`).
