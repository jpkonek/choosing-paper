# Referee report on P1_notes.md Part I (P1.10–P1.19, round 21)

16 Oct 2026. Adversarial referee. I checked every PROVED item line by line against L2_notes + L23_referee, F1_notes
(F1.2, F1.4), K3_notes §§1, 4.3 + K3_referee, N2_notes Part I + N12_referee, H1.2, S1.6/S1.9, and the write-up
§§2–3 (axioms, Def. addup, relevant comparisons, regular models, Theorem kkm). Part II (the archived round-11 note)
was not refereed.

**Numerics.**
- `p1py/q_n2_check.py`, rerun with `python3 -I -B` from inside `p1py/`, reproduces `q_n2_check.out` byte for byte
  (rerun in `p1ref_py/q_n2_rerun.out`; about 3 minutes).
- My own checks are `p1ref_py/ref_checks.py` (+ `.out`), run with `python3 -I -B` from inside `p1ref_py/`:
  - (A) Lemma P1.10a exactly, for k < 400 with s_k at its largest allowed value. The worst ratio Θ-bound/r_k is
    0.0189 ≤ 1/25. The three margins −3/5 (strictness), −1/5 (sums) and +3/5 (case (i)) are confirmed.
  - (B) LP relaxations of the cell model. Fractional cell densities are realizable by sets: place −1 left and +1
    right inside each cell, which only raises interior tails. Results:
    - (B1) strictness: no fractional δ ≤ 0, δ ≠ 0, is accepted, for all 91 selectors;
    - (B2) no weak domination: P = Q = 0 for all 9464 selector/cut pairs;
    - (B3) same-level sums: σ ∈ [−1,1] is infeasible for all 7956 selector pairs that share a level.

    This is exhaustive, which is stronger than the note's random sampling.
  - *Caution.* Cell sizes span 5^{−24}. Unscaled floating LPs give spurious "counterexamples", because the deep
    cells fall below solver tolerance. The tail rows must be scaled by 1 − x_i, as the script does.
  - (C) κ(c_{y₀/2}) > 0 in the cell model, and the P1.17 bound holds for all 30 shrunk generator pairs.
- **Two remarks on `q_n2_check.py`.**
  - Its test 6 ("non-S cells have S to their right", 72/72) records True unconditionally, so it tests nothing. §0
    does not cite it.
  - Its φ (test 8) is not the P1.14 recipe: it takes C_n from the largest strip, and clamps with max(cur, ·),
    instead of using equal-φ-mass strips and the min I_n condition.

  No verdict rests on numerics.

---

## Verdicts

| Item | Verdict |
|---|---|
| **P1.10a** deep sources negligible, Θ(F,k) ≤ r_k/25 | **CORRECT** |
| **P1.11** preorder, strict (G), (IB); same-level sums blocked with deep sources | **CORRECT** |
| **P1.12** closed world-1 sections for every model | **CORRECT** |
| **P1.10** full two-world system (incl. new two-case no-weak-domination) | **CORRECT** |
| **P1.13** total blindness: ν(c_b) = 0 for every D, every ν ∈ 𝒩(𝔚_D), every b < 1; Λ = Λ_D = Λ_∞ = M; (NC); (M2) | **CORRECT** |
| **P1.14** σ-finite endorser φ∘x, D ≡ ∅; (Loc) ∖ (Loc_int) | **CORRECT** |
| **P1.15** (a) cut moves; (b) κ(S) > 0, monotone | **CORRECT** (cite N1.4(a) with the N12_referee fix) |
| **P1.16** transport of ratios | **CORRECT** |
| **P1.17** window ratio bound | **CORRECT** |
| **P1.18(a)** no vanishing ratios in a fixed window | **GAP (fixable, trivial)**: the hypothesis λ(P_j) ≤ y₀/2 of P1.17 is dropped; fix by shrinking |
| **P1.18(b)** interior ends | **GAP (fixable, statement)**: what is proved is "no full system accepts these trades", not "the design violates (S)"; the P1.10 variant needs a choice of strips |
| P1.18(c) | CORRECT as a reading; L2.C stays CONJECTURE, as stated |
| **P1.19** (V1)–(V6) at (V0) | **CORRECT** |
| P1.19 "two-world test" / §0 "not excluded by any two-world obstruction" | **GAP (wording/label)**: unproved reading, overstated (S1.9) |
| §7.2, Q_P1 | properly unlabelled / open. Two wording points (§D) |

Nothing is WRONG. Q_N2 has answer YES as claimed: P1.10 + P1.13 give a full two-world system next to an additive
world with Λ = Λ_∞ = M.

---

## A. Theorem P1.10 and its lemmas

### A.1 Lemma P1.10a — CORRECT
- *Levels ≤ n.* P_{F(n′)} ⊆ Σ_{n′} ⊆ c_{v_{n′}}. This holds because S_k ⊆ B_k ⊆ {x < u_{k+1}} ≤ u_{min I_{n′}} for
  k < min I_{n′}. Also v_{n′} ≤ v_n ≤ u_k for k ∈ I_n. So these levels contribute nothing on {x ≥ u_k}.
- *Levels > n.* λ(P_{F(n′)}) = λ(Σ_{n′})/K_{n′} ≤ 2^{−n′}, using λ(Σ_{n′}) ≤ u₀ + Σs_k < 1. Also
  P ∩ {x ≥ u_k} ⊆ S ∩ {x ≥ u_k} = ⋃_{k′≥k} S_{k′}, since u_k ≥ u₀. So the bound min(2^{−n′}, s_{≥k}) is right.
- *(2.1).* s_{≥k} ≤ Σ_{k′≥k} r_{k′}/(100N_{k′}) ≤ (1/(100N_k))·(5/4)r_k. This uses N_{k′} ≥ N_k, and N_k is
  nondecreasing because r_k decreases. Here (5/4)/100 = 1/80 exactly.
- *The sum.* Σ_{n′≥1} min(2^{−n′}, s) ≤ N_k s + Σ_{n′>N_k} 2^{−n′} = N_k s + 2^{−N_k} ≤ r_k/80 + r_k/50 = 0.0325 r_k.
  The exact supremum is below 0.019 r_k (`ref_checks` (A)).
- *Overlaps are harmless.* Sources of different levels overlap, since the Σ_n are nested. So g_F can take the values
  −2, −3, … on S. The lemma bounds g_F⁻ by Σ_n 1_{P_{F(n)}}. This is the exact value of g_F⁻ on S, because no target
  meets S (G4).

### A.2 Lemma P1.11 — CORRECT
- *δ ≥ 0, R±.* As in L2.2, including the unconditional R⁺ (L23_referee §A.1).
- *δ ≤ 0, δ ≠ 0.* On {x ≥ u_k}, f ≤ −g_F = −g_F⁺ + g_F⁻. So f ≤ −1 on ref_k and f ≤ g_F⁻ elsewhere. Then
  τ_f(u_k) ≤ −(16/25)r_k + r_k/25 < 0. The very negative values of g_F on c_{u₀} play no role, because only the tail
  at u_k is used.
- *Sums.* On ref_k, f ≤ 1 − 2. On {x ≥ u_k} ∖ ref_k, which has measure (9/25)r_k, f ≤ 1 + g_{F₁}⁻ + g_{F₂}⁻. So
  τ_f(u_k) ≤ (−16 + 9 + 2)r_k/25 < 0. The case F₁ = F₂ on level n is included. The disjoint-level case is
  g_{F₁} + g_{F₂} = g_{F₁∪F₂}.
- (B1) and (B3) confirm both blocking statements exhaustively on the cell model.

### A.3 Lemma P1.12 — CORRECT
- The only input beyond L2.3 is Σ_n max_{g∈𝒢_n} 2‖g‖₁ < ∞. (G1) gives ‖g‖₁ ≤ 2^{−n} + (q_n+1)(16/25)r_{min I_n}
  ≤ 2^{1−n}.
- (The sharper bound λ(Q) ≤ (4/5)r_{min I_n} also holds, because the blocks are disjoint and geometric.)
- Initial segments: L23_referee §A.2's one-line argument applies verbatim.
- Non-regular models have section [0,1].

### A.4 Theorem P1.10 — CORRECT
- **Steps 1–3, 5, 6** are L2.1 verbatim, with P1.11/P1.12 substituted. Step 2 ((K) for every model) uses only
  F ≡ ⊥, so it is untouched by the new sources. Vertex competitiveness follows from (G), and world-2 sections are
  closed by continuity.
- **Step 4, new two-case argument (priority 1).** Setup: R⁻ forces N_X null. X ⪯₂ C_b reads λ(P) ≤ λ(Q). Then
  1_P − 1_Q = g_F + f with f ∈ T, where P ⊆ c_b and Q ⊆ d_b.
  - *F ≡ ⊥:* τ_f(b) = −λ(Q).
  - *Case (i):* τ_{δ′}(u_k) = −λ(Q ∩ {x ≥ u_k}) ≤ 0, since P ⊆ c_b ⊆ c_{u_k}. Also
    τ_{g_F}(u_k) ≥ λ(ref_k) − Θ(F,k) ≥ (15/25)r_k, by P1.10a; this needs k ∈ I_n with F(n) ≠ ⊥, which holds. So
    τ_f(u_k) < 0.
  - *Case (ii):* every block on every selected line has u_k < b. Each line has q_n + 1 ≥ 3 points, so
    v_n = u_{min I_n} ≤ u_k < b. Hence Σ_n ⊆ c_{v_n} ⊆ c_b. Then g_F ≥ 0 on d_b, and τ_f(b) ≤ −λ(Q).
  - The two cases are exhaustive. In case (ii) only finitely many levels can be selected, since v_n ↑ 1, but the
    argument does not need this.
  - Both cases give X = C_b. This is what step 5 needs: the only model tied with C_b at both worlds is C_b.
- (B2) finds no fractional counterexample at any of the 9464 selector/cut pairs. This includes cuts inside deep
  blocks, where later-level sources sit to the right of b.

## B. Theorem P1.13 — CORRECT (priority 2)

Definitions are as in K3 §1:
- 𝔚 = {1_{E₁X} − 1_{E₁B} : B ∈ C_L, X regular, B ⪯₁ X}, which lives on M;
- D-localized means ≤ 0 a.e. on some D_m;
- localizing families have μ(D_m) → 0.

**Step A.**
- Room: λ((F_k∖S_k)∖D_m) ≥ λ(F_k∖S_k) − λ(D_m∩B_k) ≥ λ(F_k∖S_k)/2 ≥ λ(D_m∩B_k) ≥ λ(Z_k). Also
  λ(F_k∖S_k) ≥ (4/25 − 1/100)r_k ≥ (3/25)r_k.
- f_k ∈ T, because R_k lies to the right of Z_k in B_k.
- δ′ is ternary and relevant. It is the cut pair (P_{n,i}, Q′) at v_n, with X′ regular, and C_{v_n} ∈ C_L. It is
  D-localized, because Q′ ∩ D_m = ∅.
- The R_k are chosen once per block, so the multiplicity bound (q_n+1)/L_n holds pointwise.
- Σ_n is increasing, so ν(Σ_n) ≤ ν(Σ_{n′}) ≤ ε_{n′} → 0. Also S ∩ c_b ⊆ Σ_n once v_n ≥ b: an S_k meeting c_b has
  u_k < b ≤ v_n, so k < min I_n.
- (Excluding S_k from R_k is not needed for ternarity, since S_k ⊄ Σ_n for k ∈ I_n. It is harmless.)

**Step B ("move rightward into blind thin sources").**
- G is non-null for large m. This holds because S ∩ {b ≤ x < b″} is non-null for every b < b″ ≤ 1: either
  c_{u₀} ∖ c_b or some S_k lies there.
- Each (W_j, G_j) is an equal-measure cut pair at b with G_j to the right of W_j. So 1_{G_j} − 1_{W_j} ∈ T, and it is
  accepted (F ≡ ⊥), relevant and D-localized (G ∩ D_m = ∅).
- Re-using G for every j is legitimate: the comparisons are separate members of 𝔚_D. Only finite additivity of ν
  over the W_j is used.
- Hence ν(c_b) = 0.

**Consequences.**
- ρ_νλ = ν_c ≤ ν, so ρ_ν = 0 a.e. 𝒩(𝔚_D) ⊇ 𝒩 ≠ ∅, so Λ_D = M by K3.1(c),(d).
- *(NC).* Relevant vectors are regular, so b_j = 1 forces δ_j ≤ 0 and hence δ_j = 0. Every δ_j is ≥ 0 on the
  non-null d_{b*}. This is the presupposition of K3.1(a), so 𝒩 ≠ ∅.
- *¬(M1).* The induction is correct: each step deletes the δ with the largest cut.
- *¬(M0).* Λ is non-null.
- Q_N2 (N2 §6) asks for Λ = M with a_∞ = 1. That is exactly what is proved.

## C. Proposition P1.14 — CORRECT (priority 3)

- *No circularity.*
  - φ_prev is the value on the last block of I_{n−1}, independent of min I_n.
  - The s_k of the gap blocks before I_n use φ_prev, so Σ_n is fixed before the strips are chosen.
  - S_k for k ∈ I_n enters only Σ_{n+1}.
- *Lyapunov.* (λ, φλ) is a non-atomic finite vector measure on Σ_n, and φ is bounded there. Iterated halving gives
  2^n = K_n strips with equal λ-mass and equal φλ-mass.
- *Monotone.*
  - Within I_n, λ(ref_k) decreases.
  - At v_n, φ_new ≥ φ_prev, using π_n ≥ u₀/K_n (from φ ≥ 1 and λ(Σ_n) ≥ u₀) and the min I_n condition.
  - Gaps are constant.
- *Neutrality.* ∫_Q φ = (q_n+1)C_n = π_n = ∫_P φ, because φ is constant on each B_k ⊇ ref_k.
- *Endorsement.*
  - Base step: layer cake with Fubini; ψ is bounded and f ∈ L¹, and level sets {x = y} are null.
  - ρ(δ⁻) ≤ φ(b)b < ∞.
  - ∫φ_N g_F = Σ_n ∫φ_N g_{F(n)} by L¹ convergence. The terms lie in [−π_n, π_n] and vanish for large N, since φ is
    bounded on P ∪ Q.
  - Σπ_n ≤ Σ 3·2^{−n} < ∞, from ∫_S φ ≤ u₀ + Σ2^{−k}. Dominated convergence is used twice.
- *(Loc), D ≡ ∅.*
  - φ ≥ 1 and φ is finite on [0,1).
  - ∫^1 φ = ∞ by P1.13. Directly, the level-n integral is (5/4)Π_nC_n ≥ (5/4)q_nπ_n ≥ (5/4)u₀2^n.
  - ¬(Loc_int) by K3.1(e), since Λ_∞ = M.
- The remark "total blindness does not imply ¬(Loc)" is correct.

## D. §6–§7

### D.1 Lemma P1.15 — CORRECT
- **(a)**
  - The strict case is (K) at b (F1.2, first paragraph).
  - The equal case: λ(E₂X) = λ(d_b) < λ(d_{b′}) for b′ < b. So C_{b′} ⋠₂ X, and competitiveness at the interior
    prior gives C_{b′} ⪯₁ X.
  - Closedness in p transfers to b: by continuity, the first prior with λ(c_p) = b is a limit of priors with
    λ(c_p) < b. Priors with λ(c_p) = 0 are covered by (G).
  - **Citation:** "no jumps" is N1.4(a), which N12_referee §1.4 marks GAP (fixable: index by the chain via Lemma
    N0). Cite it with that fix.
- **(b)**
  - The room computation λ(d_b ∖ W) ≥ λ(W ∩ c_b) is correct.
  - The partial chaining 1_W − 1_S + 1_Z − 1_{W∩c_b} is ternary: the sets S, W, Z are pairwise disjoint. So it is
    accepted by sum closure (Lemma vectorform, F1.4's proof preamble). It is not literally F1.4(iii), which moves
    all of W; say "sum closure".
  - Adding 1_{d_b∖W′} ≥ 0 gives 1_{d_b} − 1_S, which is the vector of C_b ⪯₁ X.
  - With κ = 0: [0,1) ⊆ S₁(X), then closedness at b = 1 gives P₂ ⪯₁ X. Its vector −1_S contradicts strict (G).
  - Monotonicity is F1.4(i).
  - *Cosmetic:* §0 states κ without the condition W ∩ S = ∅. Use §6's definition throughout.

### D.2 Lemma P1.16 — CORRECT
- Disjointness of W, P, Q, R: W ⊆ c_y with P ⊆ d_y; Q ⊆ d_b ⊆ d_y; R ⊆ d_t ∖ (P∪Q) with W ⊆ c_t. The two partial sums
  are ternary.
- Degenerate cases: y = 0 forces W null, and t = 1 forces R and then Q null. Both are trivial.
- Disjoint sums: F1.4(iv).

### D.3 Proposition P1.17 — CORRECT (priority 5)
- y₀ < b < t: P non-null forces b > y₀. Q is non-null, since otherwise −1_P would be accepted.
- m ≤ y₀/λ(P) uses λ(P) ≤ y₀/2.
- The R_i ⊆ d_t automatically avoid P ∪ Q ⊆ c_t.
- P1.16 applies with y = y₀, since W_i ⊆ c_{y₀/2} ⊆ c_{y₀}.
- κ₀ ≤ mλ(Q), using ⊔R_i ∩ c_{y₀/2} = ∅. In the no-room case λ(Q) > (1−t)/m.
- Sanity check against P1.10: its generator trades have vanishing ratio, but their targets leave every c_t. For
  targets just past I_n, 1 − t ≤ r_{min I_n}5^{−Π_n}, so the bound is far below the actual ratio. This is consistent,
  and it is confirmed in the cell model (C).

### D.4 Corollary P1.18
- **(a) GAP (trivial).** P1.17 needs λ(P_j) ≤ y₀/2, but (a) states no such restriction.
  - *Fix:* if λ(P_j) > y₀/2, shrink P_j to P′_j ⊆ P_j with λ(P′_j) = y₀/2. This uses F1.4(i), and (P′_j, Q_j) is still
    a cut pair at the same b.
  - Then λ(Q_j)/λ(P′_j) ≤ (2/y₀)λ(Q_j) ≤ (2/y₀)·λ(Q_j)/λ(P_j) → 0, against P1.17.
- **(b) GAP (statement).** The argument shows that **no system in the setting of §6 accepts these generator trades**.
  It does not show that the literal design "violates (S)".
  - With an interior end t*, the blocking inequality (B) fails: there is room 1 − t* to the right. So L2.2's sum
    closure is no longer proved for the literal 𝒜, and which axiom fails first is not determined.
  - *Fix:* restate (b) as "no full system next to an additive world contains these trades", or "any completion
    satisfying (G), (IB), (K) fails (S)".
  - The ratio formula is an upper bound, not the exact ratio. It suffices, since λ(Q) ≤ (4/5)r_{min I_n}.
  - For "P1.10's" variant, choose the strips in x-order. Then a fixed fraction of strips lies in d_{y₀}; for an
    arbitrary partition no strip need lie in d_{y₀}.
- **(c)** CORRECT as a reading.
  - "Excludes exactly that" should say: with sources bounded away from x = 0 as well. P1.17 needs P ⊆ d_{y₀}.
  - L2.C remains a CONJECTURE, and the note says so.

### D.5 Proposition P1.19 — (V1)–(V6) CORRECT; "two-world test" overstated
- **(V1).** c* = (0, ρ₂σ₂, ρ₃σ₃). A(c*) ⊆ {e₁} can be checked directly: T1 accepts (+,−,−) gambles near the e₁ ray,
  where q·c* < 0 whenever q₂ + q₃ > 0. The other clauses are trivial. The B_q computation (P₂, P₃, P₂ ∩ P₃ within U)
  is correct.
- **(V2).** X₁₂ = P₂ = D_{co(K′∪{e₂})} and X₁₃ = P₃.
- **(V3).** Every edge model is 1-Bayes because e₁ ≡ 0. A model is θ-Bayes with θ < 1 only if c = R₁₂, since
  e_θ = −(1−θ)ρ₂ < 0. So N2.2 is vacuous.
- **(V4).** Trivially internal.
- **(V5).** N2.5′ is untouched.
- **(V6).** H1.2's hypotheses are exactly "integrable ρ₂, ρ₃ > 0 endorsing all relevant comparisons". ¬(M0) is
  immediate from Λ₁ = M, so the citation of M0closed(b) is not needed. K3.7's first sentence gives (M1) or (N).
- **GAP (wording/label).** "So no edge-by-edge argument of N1/N2/L3.4 type can exclude (V0)" (§7.1), and §0's "(V0) is
  not excluded by any two-world obstruction", are unproved readings.
  - An edge system inside a three-world cover need not be a full two-world system, and conversely (S1.9;
    N12_referee §2.8 made the same point about "reduces").
  - P1.10 is not shown to embed as an edge of a (V0) system.
  - Rephrase: "the two-world form of (V0) (Q_N2) is consistent with every axiom, so no argument that uses only the
    two-world axioms on an edge can exclude (V0)". Label it as a reading.

### D.6 §7.2–§7.3 (wording only)
- "'No' closes (V0) for additive (more generally, integrably endorsed) partners." Q_P1 is posed for additive
  partners. Either pose it for integrably endorsed partners, or drop "more generally".
- "P1.17/P1.18 prove the fixed-window half of L2.C" (§7.3) should read "of the L2 heuristic for L2.C", as §0 says.
- "P1.10's world 1, installed unchanged as an exceptional world" (§5 remark) is a reading. The proved statement is
  H1.2: no world-1 of class (Loc) in a three-world (H_U) system with integrable partners.

---

## E. Requested changes (all local)
1. **P1.18(a):** add the shrinking step (§D.4).
2. **P1.18(b):** restate as "no full system next to an additive world accepts these trades". Remark that with an
   interior end the literal 𝒜 loses the blocking inequality. Fix the strip choice for the P1.10 variant.
3. **§0 item 1, §7.1 "two-world test":** relabel as a reading and weaken it, as in §D.5. Cite S1.9.
4. **P1.15:** cite N1.4(a) with the N12_referee fix. Say "sum closure" for the partial chaining. Unify the κ
   definition between §0 and §6.
5. **§7.3:** fix "more generally" and "half of L2.C" (§D.6).
6. **NUMERICS:** remove or implement test 6 of `q_n2_check.py`. State that test 8's φ is a proxy, not the P1.14
   recipe.

None of these touches P1.10, P1.13, P1.14 or P1.15–P1.17. **Q_N2 = YES stands**: there is a full two-world system,
next to an additive world, that is totally blind (Λ = Λ_∞ = M) with closed sections for every model. Its world 1 is
(Loc) (P1.14), so for T1 next to integrable partners it is excluded by H1.2, as the note says.
