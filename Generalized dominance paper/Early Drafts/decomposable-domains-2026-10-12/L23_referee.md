# Referee report on L2_notes.md and L3_notes.md (round 20)

16 Oct 2026. Adversarial referee. I checked every proof line by line against the write-up §2 (definitions of
(G), (IB), (LA), (S), (C), C_L, covering), D2 §§1–3 (now Lemma D23 / Thm D21 in the write-up), K3 §1–2 and §4.3,
K3_referee, F1.4, H1.2, and R10a (Thm V, Cor V2, Thm M, Thm R). I reran all scripts with `python3 -I`.
Referee scripts and outputs are in `l23ref_py/`: `l3_checks.py` (+ `.out`), `cube_scan.py` (+ `.out`), and the
rerun outputs `l2_rerun.out`, `vb_rerun.out`, `boxes_rerun.out`, `gauge_rerun.out`.

**Reruns.** `l2py/l2_check.py`, `l3py/vb_system.py`, `l3py/two_sided_boxes.py` and `l3py/gauge_fixed_U.py`
reproduce their stored `.out` files byte for byte. I did not rerun `gauge_structure.py`, because it writes into `l3py/`.

---

## Summary of verdicts

| Item | Verdict |
|---|---|
| **L2.2** preorder, strict (G), (IB); same-level sums blocked | **CORRECT** |
| **L2.3** closed world-1 sections for every model (compact selectors) | **CORRECT** |
| **L2.1** full two-world system: (G), (IB), (LA), (S), (C), C_L = path, (LF) | **CORRECT** |
| **L2.4** every bounded endorser of every localization vanishes on c_a; Λ = Λ_D = Λ_∞ = c_a; K3.C false | **CORRECT** |
| **L2.5** σ-finite endorser φ∘x with D = ∅; world 1 ∈ (Loc) ∖ (Loc_int), not in (N) | **CORRECT** |
| **L2.6** (a)–(c) | **CORRECT** |
| L2.C, §7 | properly labelled (CONJECTURE / analysis); no claim to referee |
| **L3.1(a)** precise vertex models on two-sided domains | **CORRECT** |
| **L3.1(b),(c)** gauges are boxes; c(ε) > 0 | **CORRECT**. The NUMERICS values of c(ε) are **wrong** (too large; §B.1) |
| **L3.2** fixed-margin gauge covers on M_U with d_H = O(a/b) | **CORRECT** |
| **L3.3(a)** "VB is the ordinal (lexicographic/ultrafilter) limit" | **GAP (fixable)**: the limit's second level is Brier error *off the veto set*, not Ψ_i (§B.3) |
| **L3.3(b)** strict (G), (IB), (LA), (C), (LF) at T1; T1 ∈ C_L; plateau; competitive and undominated at every p ∈ Δ | **CORRECT** |
| **L3.3(c)** closed relative to int Δ; fails at e_j | **CORRECT**. The extra clause "closed relative to each open edge" is **WRONG** for the world off the edge (§B.4). This does not affect the headline |
| **L3.3(d)** no world adds up | **CORRECT** |
| **L3.4** vetoes cannot be paid | **CORRECT** |
| L3.4 applied to VB | **CORRECT** |
| **L3.5** (under (N)) | **CORRECT**, with two hypotheses to state (§B.7) |
| L3.5 "what a repair must do" (R5, CHECKED) | not independently verified; the general sentence follows from L3.4 (§B.7) |
| **L3.6(a)** | **CORRECT**. The half-plane step should be written out (§B.8) |
| **L3.6(b),(b′)** | **GAP (fixable)**: silence on every mixed pair is not given by L3.1(a), so the model R may not be evaluable. The conclusion survives with a different comparison model (§B.8). (Imp) and the precise-edge residual are CORRECT |
| **L3.6(c)** | a pointer to the D1 residual. The claim "the routes break at exactly one input" is a survey assertion and should not carry PROVED |

---

## A. L2

### A.1 Lemma L2.2 — CORRECT
- *δ ≥ 0 accepted; nonzero δ ≤ 0 rejected.*
  - In the case F ≢ ⊥, the step "f ≤ −1 on ref_k" uses two facts: g_F = 1 on ref_k, and u_k > u₀ > a, so
    {x ≥ u_k} ⊆ d_a, where g_F ∈ {0,1}.
  - Both facts hold: targets of different levels are disjoint, and a selector takes one generator per level.
- *Sums.* D ≥ 0 on accepted vectors, so D(σ) = 0 forces D(δ₁) = D(δ₂) = 0.
  - Same-level overlap: f := f₁ + f₂ ∈ T. Then f ≤ 1 − 2 on ref_k and f ≤ 1 on the rest of {x ≥ u_k}.
  - So τ_f(u_k) ≤ r_k − 2·(16/25)r_k = −(7/25)r_k < 0.
  - I checked the block arithmetic: λ(B_k) = r_k − r_{k+1} = (4/5)r_k, and λ(ref_k) = (16/25)r_k.
  - The argument rules out *every* pair of representations whose levels overlap, so sum closure follows.
- *Unconditional R⁺.* This is a real change from D2, where R⁺ was "accept iff τ_δ ≥ 0 on [a,1]". I checked that it is
  harmless.
  - Accepted vectors still have D ≥ 0, so no nonzero δ ≤ 0 is accepted.
  - Sum closure is unaffected.
  - R⁺ only makes every non-regular model strictly world-1-worse than every regular one. Such models are dominated
    (world 2 is matched by some C_b), so they cannot enter U_L.
  - No relevant comparison involves R⁺.

### A.2 Lemma L2.3 — CORRECT
- 𝔉 is a countable product of finite sets, so it is compact metrizable.
- ‖g_{F_j} − g_F‖₁ → 0 by dominated convergence: the level-n term is at most 2(a2^{−n} + r_{min I_n}), which is
  summable.
- T is an intersection of closed half-spaces of L¹.
- Non-regular models have D(δ_b) = λ(N_X) > 0, so their section is all of [0,1].
- *Remark.* The initial-segment claim needs no reference to D2. The functions satisfy
  1_A − 1_{c_{b′}} − g_F = (1_A − 1_{c_b} − g_F) + 1_{[b′,b)}, and adding a nonnegative function preserves T.

### A.3 Theorem L2.1 — CORRECT
- (K) for every model: for t < b, τ_f(t) ≥ λ(Q) − λ(P) > 0.
- Vertices follow from (G).
- No weak domination: there are three cases (b ≥ a; b < a with F ≢ ⊥; b < a with F ≡ ⊥). Each is correct.
  - For b ≥ a, {x ≥ b} ⊆ d_a.
  - For b < a, u_k > a > b, so δ′ = −1_Q ≤ 0 on {x ≥ u_k}.
- Step 5 is the D2 argument verbatim, and it is valid here: Theorem kkm needs only (LA) and (S), and both hold.
- World-2 sections are closed by continuity.
- (LF) is imported from C2.1(4).

### A.4 Theorem L2.4 — CORRECT
- **(a)** I checked the arithmetic.
  - λ(F_k ∖ D_m) ≥ λ(F_k)/2 ≥ λ(D_m ∩ B_k) ≥ λ(Z_k).
  - f_k ∈ T, since R_k lies to the right of Z_k inside B_k.
  - δ′ = g + Σf_k is ternary.
  - Q′ ∩ D_m = ∅, so δ′ is D-localized in the sense of K3 §1 (δ ≤ 0 a.e. on D_m).
  - The comparison is relevant: C_a ∈ C_L and X′ is regular.
  - The certificate uses one R_k per block, shared by all lines through k. So the multiplicity bound (q_n+1)/L_n is
    pointwise.
  - The ε_n bound is correct. L_n ≥ q_n²/2^{n+1} because q_n²/2^{n+1} + (q_n+1)/2^n ≥ 1.
- **(b)** τ_{g_F}(a) = Σλ(Q_{F(n)}) ≥ 0. The argument uses only D(δ) = 0 and δ = 0 on N₊, so ν₀ endorses every
  accepted regular–regular comparison, not only the relevant ones.
- **(c)** The chain Λ_D ⊆ Λ ⊆ c_a ⊆ Λ_D (K3.1(c),(d)) is correct, as are K3.1(e) and K3.8.
  - *Suggestion.* ¬(M1) also follows directly from L2.5: ∫ρδ ≥ 0 with ∫ρ|δ| < ∞, applied to a finite combination.
  - ¬(M0) follows directly from (a), because 𝒩 ⊆ 𝒩(𝔚_D).
  - Neither needs N17 Lemma 3.1.
- **Consistency with F1.4** is correctly argued. F1.4's constant is θ = min(ν₂(d_{b₀})/8, κ_m/4). The level-n
  certificate has Γ_n ≥ K_n(16/25)r_{max I_n} > r_{max I_n}/5 ≥ λ(d_{b₀}), so F1.4's export step never triggers.
- This also confirms the K3 referee's §8 remark: F1.4 does not reach chain-free certificates whose b₀ → 1.
- *Typo.* "K3.7(β′)" should be K3.7(β).

### A.5 Proposition L2.5 — CORRECT
- *Monotonicity.* The jump factor is 5^{G_n+1}(q_n+1)/(2(q_{n+1}+1)), as stated. φ = 1 on c_a ⊆ [0, u₀).
- *Non-integrability.* The level-n integral is ≥ a2^n.
- *Endorsement.*
  - Stieltjes integration by parts with bounded φ_N is valid.
  - ∫ρ|δ| < ∞ is shown on d_a first; on c_a, ρ = 1.
  - Each ∫φ_N g_{F(n)} lies in [−a2^{−n}, 0] and tends to 0, so dominated convergence over n is legitimate.
- So world 1 is (Loc) with D_m = ∅. It is not in (N), and it lies in (Loc) ∖ (Loc_int).

### A.6 Corollary L2.6 — CORRECT
- (a) World 1 does not add up (Λ non-null), is not (M1), and is not (Loc_int).
- (b) The example is (Loc), so (N) = ∅ is not touched.
- (c) This is H1.2 exactly as stated in H1_notes (σ-finite ρ₁, any localizing family, cancellation reading).

**Bottom line for L2.** Conjecture K3.C is refuted, and Q_K3 has answer "Yes" in a two-world full system. The
example lies in (Loc), so for T1 it is excluded next to integrable partners. The note says this itself.

---

## B. L3

### B.1 Proposition L3.1 — (a), (b) CORRECT; (c) CORRECT; NUMERICS wrong
- **(a)** Every step checks.
  - −g′ ∈ Av ∩ D_k ≈ D_{V_k} gives V_k ⊆ {m·g′ < 0}.
  - The middle arc of F_k is nonempty. On F_k, h_k < 0 and h_i + h_j = 3u·h − h_k > 0, so the two crossing points are
    ordered symmetrically.
  - W_k is the wedge at v_k bounded by lin(v_k,e_i) and lin(v_k,e_j). So W_j ⊆ H_j, and conv(W_j ∪ e_i) ⊆ H_j.
  - Compatibility V_i ⊆ conv(V_j ∪ e_i) comes from Cor V2(b).
  - The parameters are x_j = c₀/(2c₀+ε) < x_k = (c₀+ε)/(2c₀+ε), as projections of v_j and v_k from e_i.
  - Thm V and Cor V2 hold for any ranking, not only additive ones, so the scope is right.
- **(b)** For gauges, (M1) and (M2) give the same three inputs. Two-sidedness alone suffices here; T1 ∈ C_L is not
  needed.
- **(c)** The proof that no box image equals T1 is correct. It uses uniqueness of the maximiser corner, and the fact
  that x_k at v_i must equal min_{T1} x_k = c₀, which forces α_j = β_j. The compactness step is correct.
- **NUMERICS are wrong.** The reported minima 0.0080, 0.0375, 0.0314, 0.0168 (ε = .05, .3, .6, .9) are not minima;
  the script used 12 Nelder–Mead starts.
  - `l23ref_py/l3_checks.py` (60 starts, exact polygon Hausdorff distance, cross-checked by support functions) and
    `cube_scan.py` (symmetric cubes [1,r]³) give the following upper bounds for c(ε):

    | ε | 0.05 | 0.3 | 0.6 | 0.9 |
    |---|---|---|---|---|
    | upper bound for c(ε) | 0.0068 | **0.0289** | 0.0308 | 0.0107 |
    | at r = | 1.12 | 2.00 | 4.62 | 23.3 |

  - The optimal boxes are numerically symmetric.
  - Replace "c(0.3) ≈ 0.037" by "c(0.3) ≤ 0.029". Positivity is proved and is unaffected.

### B.2 Proposition L3.2 — CORRECT
- V_i = conv(e_i ∪ K′) (since v_i ∈ [u, e_i]), (M2) holds, and Av = D_{K′} = U, so the system is M_U.
- In the two-case bound (σ ≥ 1, or σ < 1 with α_i ≥ 1 − σ), the constant is uniform.
- (LF) at each covered K_u comes from Thm M(d). Every h ∈ ∂D_{K_u}∖0 lies in some D_{V_i} ⊆ U.
- `gauge_fixed_U.out` reproduces.

### B.3 Theorem L3.3(a) — GAP: VB is not the lexicographic limit
- **The problem.** At stage (a,b), f_i(h) = min(a h_i, b·min_{K′}k·h, b v_i·h).
  - On the deep veto set {v_i·h < (a/b)h_i}, f_i = b v_i·h *exactly*. There is no a·h_i term.
  - So the stage loss is L_i = bΦ_i + aΨ̃_i + R, with Ψ̃_i(X) := ∫_{E_i(X) ∖ V_i}|h_i| (V_i := {v_i·h < 0}) and
    R = o(a). It is not bΦ_i + aΨ_i + R.
- **A counterexample to the stated limit.** Let X and Y agree except on the deep veto set, and accept A₁ and A₂ there
  respectively, with Φ_i(A₁) = Φ_i(A₂) and ∫_{A₁}|h_i| ≠ ∫_{A₂}|h_i|.
  - Then L_{i,n}(X) = L_{i,n}(Y) at every small a/b.
  - (Φ,Ψ)-lex nevertheless orders X and Y strictly.
- **Checks.**
  - NUMERICS (`l3_checks.out` (1)): max|f_i − b v_i·h| = 0 on the deep veto sample at a/b = 10⁻², 10⁻³, 10⁻⁴.
  - The note's own script prints "f/a → h_i off veto" (`gauge_fixed_U.out`, last lines).
  - The ultrafilter clause fails in the same way: those limits refine (Φ,Ψ̃)-lex, not (Φ,Ψ)-lex.
- **Fix.** Either of two works.
  - Redefine VB's second level as Ψ̃_i. Then (a) holds as stated.
  - Or keep VB, and say only that it *refines the leading scale*. That is the sense of "ordinal limit" in L3.5, so VB
    is an ordinal limit in that sense, but not the lexicographic limit.
- **Effect of the fix.** I re-ran every proof in (b)–(d) for VB′ = (Φ,Ψ̃)-lex.
  - Lex-Bayes, competitiveness and undominatedness are unchanged. Models with Φ_m = 0 accept nothing in V_m ⊆ {h_m < 0},
    so Ψ̃_m = Ψ_m on them.
  - Vector uniqueness: M_A h becomes ((−v_m·h)1[m∈A], −h_m 1[m∉A]). It still spans M_A(ℝ³), and
    M_A𝟙 = (−1[m∈A], −1[m∉A]) is still lex-negative at every world.
  - Sections, (d) and the L3.4 application are unchanged.
- So the substance of L3.3 survives for both VB and VB′.

### B.4 Theorem L3.3(b),(c),(d)
- **(b) CORRECT.**
  - Strict (G): E_i(X) ⊆ E_i(Y) shrinks vetoed wrong acceptances weakly, and Ψ_i strictly.
  - (IB) holds because both levels are integrals.
  - The lex-Bayes model is C_p, and it is a.e. unique. Competitiveness and undominatedness hold at every p ∈ Δ,
    including the edges and the vertices.
  - (C), through the vector-uniqueness lemma, was the priority item. It is correct.
    - The splice range is convex and compact (Lyapunov).
    - It is symmetric, because σ(D∖S) = −σ(S) when σ(D) = 0.
    - A symmetric convex set contains a ball of its span.
    - A non-null set of orientations spans ℝ³.
    - (C) in the write-up's sense ("tied at every world with a member of C_L ⇒ in C_L") follows.
  - T1 = C_p for p ∈ T1, so T1 ∈ C_L. (LF) at T1 holds with N = U.
- **(c), first clause.** Sections are closed relative to int Δ: CORRECT, since Φ_m(C_p) = 0 at interior p.
  - **"Relative to each open edge" is WRONG** for the world k off the edge.
  - On the open edge (e_i,e_j), Φ_k(C_{q_t}) > 0 varies with t. It equals ∫ over U ∩ {v_i·h ≥ 0, v_j·h ≥ 0,
    v_k·h < 0, (1−t)h_i + t h_j > 0}.
  - At t = 1/2 the last constraint is void, since h_i + h_j = 3u·h − h_k > 0 there. As t → 0 it removes a non-null set
    near the corner ray r_{ki}. So the map is non-constant.
  - Take t₀ where it strictly increases, and let X := C_{q_{t₀}} minus a Φ_k-neutral world-k-wrong piece. Then
    S_k(X) contains q_t for t ↑ t₀ but does not contain q_{t₀}.
  - NUMERICS (`l3_checks.out` (2)): f(t) = 0.00448, 0.00459, 0.00470 at t = .001, .05, .1. The section contains
    t = .08, .09, .095, but not t = .1.
  - On the open edge the sections at worlds i and j *are* closed.
  - The headline ("fail exactly at boundary priors") stands: these failures are at edge priors. Note also that every
    boundary p with Φ_k(C_p) > 0 for some k ∉ supp p has a non-closed section through it (int Δ ⊆ S_k(X)).
- **(c), second clause (failure at e_j): CORRECT.**
- **(d) CORRECT.** Disjoint small vetoed P's give ν(∪P_n) ≥ Nν(A), which contradicts boundedness. The same argument
  also excludes σ-finite endorsers.

### B.5 Theorem L3.4 — CORRECT
This was priority item 1, so I checked each step.
- **C_{e_m} = B^m.** Best advice is unique in the background order, and (G) is strict.
- **Step 1.** Splices B^j|_A ∪ B^i|_{A^c} realise every value in [0,Λ], since ω(·,b^i) = 0 a.e. Closed sublevel sets
  {f ≤ c}, c < Λ, follow.
- **Step 2 (usc off T).**
  - Y is a splice, so Y ∈ M. Y ≺_j C_{q_t} holds because b^j is the unique best world-j advice.
  - The open complement of S_j(Y) excludes t′ = 1, because B^j ⪯_j Y.
  - Competitiveness on {i,j} at interior edge priors gives C ⪯_i Y. At t′ = 0 the bound is trivial, since f(0) = 0.
  - The neighbourhood depends on δ, which is exactly usc.
- **Step 3.**
  - T ⊆ {f ≥ Λ}, since ω ≥ 0.
  - Q is relatively open by Step 2 alone.
  - 0 ∈ Q, since b^i ≠ b^j a.e. on G_j: otherwise Φ(B^i) > 0.
  - t* ∉ Q, f(t*) ≥ Λ, and liminf_{t↑t*} f ≥ Λ by Step 1. f is continuous on [0,t*).
- **Step 4.** t_c exists by the intermediate value theorem, and the contradiction is valid.
- **Scope.**
  - The theorem uses strict (G), splice closure, non-atomicity, Φ(B^j) < ∞, competitiveness at both vertices and at
    the interior edge priors, and closedness at worlds i and j only.
  - "No (IB), (C), totality, third world" is accurate.
- **Application to VB: CORRECT.**
  - (V): B^j accepts the non-null set {h_j > 0, v_i·h < 0} ∩ U.
  - (Imp): e_i is an extreme point of Δ, so e_i ∉ K and e_i ∉ T1 give e_i ∉ conv(K ∪ T1). Strict separation gives an
    open set of accepted, i-wrong, unvetoed h. Removing a piece of it is Φ-neutral and strictly better.
  - The argument uses only coherence of the selected models, which (S) requires. So "no selection whatever" is right.

### B.6 Remark on (Imp)
On M_U (silence always available), (Imp) holds under strict (G) for *every* ranking whose veto vanishes on cl D_{T1}.
So the escape route "keep the veto but break (Imp)" is closed there. This supports L3.5's "must give up refining".

### B.7 Theorem L3.5 — CORRECT under (N), with two hypotheses to state
- **Checks.**
  - The weak-sign Thm R argument is correct: linearity on facets, then α_i ≥ 0 equal on both crossing facets, then
    α = 0 at the corner rays.
  - Concavity gives f^∞ ≥ 0 on cl D_{T1}. Then f^∞_i = 0 on an open set near F_i (where h_i < 0), so f^∞_i ≤ 0
    everywhere, and 0 ∈ M^∞_i.
  - Dominated convergence for the leading scale is correct, since |f_{i,n}| ≤ s_n|h| and μ is Gaussian.
  - Both orientations on two-sided pairs are handled: the cost −f^∞_i(±g) is positive only on i-wrong advice.
  - (V): the veto set lies in Av ∩ {h_i < 0} ⊆ ∪_{j≠i}D_{V_j}.
  - (Imp): if silence is missing, use the opposite acceptance; it is i-good and Φ-neutral, because f^∞_i = 0 on
    Av ∩ {h_i ≥ 0}.
- **Hypotheses to state.**
  - (i) M^∞_i is a Blaschke-subsequence limit. "→" needs a subsequence.
  - (ii) The ordinal limit must have **strict (G)** at worlds i and j, because L3.4 uses it.
    - This holds for ultrafilter limits: each stage is strictly guiding, so a pointwise improvement is strict at
      every n.
    - It holds for a lexicographic limit with a strictly guiding tail.
    - It does not follow from "any order that refines the leading scale".
  - Also replace u by the target prior p* when p* ≠ u.
- **"What a repair must do", R5 part (CHECKED).** Not independently verified. The sentence "a repair must give up
  refining the leading level" is supported by L3.4 and §B.6. "Near the boundary of Δ" is interpretive.

### B.8 Proposition L3.6
- **(a) CORRECT, but the half-plane step should be written out.**
  - The argument: let P := {d : 0 ⪯ d}. It is closed under addition (translation invariance from (IB)), and
    P ∪ −P = ℝ² (totality).
  - Rational scaling follows from strictness, so P is ℚ-convex.
  - (G) forces (+,0), (0,+) and every (W(A), −S(A)) into P. P ⊇ ℝ²₊ together with the down-set property along rays
    (1,−t) makes P a half-plane, possibly containing part of its boundary line.
  - Then a ∝ (0,1) contradicts (G); a ∝ (1,0) is wrong-first; a > 0 adds up.
- **(b), (b′) GAP (fixable).**
  - "By L3.1(a), every mixed pair has all three advices available" is not what L3.1(a) gives. L3.1(a) gives both
    *acceptances*. Silence is guaranteed only on the (LF) neighbourhood N.
  - So the regular vacuous model R need not be evaluable.
  - **Fix.** Use R″ := T1 with silence on N ∩ D_{T1} ∩ {mixed}, which is evaluable by (LF).
    - T1 is m-wrong on a non-null part of N ∩ D_{T1} near F_m, for every m.
    - So W_m(R″) < W_m(T1) at every world, and the same conclusions follow: at most two wrong-first worlds, and
      (1,0) ∈ A_i blocks T1.
    - The (0,1) case of (b′) is correct as written: D_{p*} is evaluable and never silent, by L3.1(a).
  - **(Imp) for non-precise selected models: CORRECT.** It uses silence → right advice, which is available.
  - **Precise-edge residual: CORRECT as a reduction.** Each c ∈ (0,Λ) gives a distinct first-hitting t_c at which
    (Imp) must fail, so uncountably many precise edge models are needed. It is correctly labelled CONJECTURE.
  - L3.6 should state that it assumes the hypotheses of L3.1(a): a cover with (S) and T1 ∈ C_L.
- **(c).** Correct as a pointer: D1 gives p* ∉ E(ψ), and Prop M0 gives E ≠ ∅. The claim that the routes I1, I2, C2
  and the short route break at exactly one input ((BU) on the atom chords) was not proved in the note. It should be
  CHECKED at most.
- **§0 remark "dropping boundary priors trivialises coverage".**
  - The full-veto example (constant vacuous selection) is correct.
  - "Trivialises" is not shown. For example, wrong-first worlds do not cover T1, since R″ dominates it.
  - Suggested wording: "interior-only (S) admits lexicographic systems such as VB and constant selections".

---

## C. Requested changes (all local)
1. **L3.3(a):** replace Ψ_i by Ψ̃_i (Brier error off the veto set), or reword (a) as "VB refines the leading scale".
   State that (b)–(d) hold for both VB and VB′ (§B.3).
2. **L3.3(c):** delete "and relative to each open edge", or restrict it to the two worlds of the edge. Add the
   world-k example (§B.4).
3. **L3.1 NUMERICS:** correct c(ε) to ≤ 0.0068, 0.029, 0.031, 0.011 (§B.1).
4. **L3.5:** add the subsequence and strict (G) of the ordinal limit to the hypotheses (§B.7).
5. **L3.6(b),(b′):** replace R by R″, or assume silence on mixed pairs. Write out the half-plane step of (a). Relabel
   the route-survey part of (c) (§B.8).
6. **L2 (cosmetic):** "K3.7(β′)" → K3.7(β). Optionally give the direct proofs of ¬(M0) and ¬(M1) (§A.4) and the
   one-line initial-segment argument (§A.2).

None of these changes touches L2.1/L2.4 (K3.C is refuted) or L3.4.
