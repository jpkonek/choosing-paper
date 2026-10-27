# P1 (round 21). Q_N2 has answer YES: a totally blind world with closed sections, and why it does not yet close (V0)

16 Oct 2026, round 21 (BRIEF13 rules; task: settle Q_N2 of N2 §6). This file has two parts. **Part I** is the new
note. **Part II** (after the double rule at the end) is the earlier note "P1" of 14 Oct 2026 (round 11), kept
verbatim, because the write-up cites its Lemmas P1.1–P1.4 as \src{P1}; a copy is also in
`p1py/archive_P1_notes_2026-10-14.md`. To avoid clashes, the new results are numbered **P1.10–P1.19**.

Labels: **PROVED** (full proof here, from results the write-up or the notes mark proved, each named),
**CHECKED**, **CONJECTURE**, **NUMERICS** (`p1py/q_n2_*.py`, run with `python3 -I -B q_n2_check.py` from inside
`p1py/`; no proof rests on them). No assumption is added. The old scripts in `p1py/` are untouched.

Notation: L2 §1 (n = 2, K′ = [α′, β′] ⊆ (0,1), U = D_{K′}, M_U, M, N₊, λ = μ/μ(M), the C2.1 path C_b with
c_b = E₁C_b ∩ M = {x < b}, d_b = M ∖ c_b, chain coordinate x pushing λ|_M to Lebesgue measure on [0,1), selection
p ↦ C_{p₂}, τ_f(t) = ∫_{M∩{x≥t}} f dλ, D(δ) = ∫_{N₊} δ dλ, T = {f ∈ L¹(M) : τ_f ≥ 0 on [0,1]}); K3 §1 (𝔚, 𝒩,
𝒩(𝔚_D), localizing families, Λ, Λ_D, Λ_∞, ratio certificates); L2's names **(Loc)**/(Loc_int) for K3's class
(S)/(S_int). "P ≤₁ Q" means that 1_Q − 1_P is an accepted world-1 vector (F1.4's notation). A **cut pair at b** is
P ⊆ c_b, Q ⊆ d_b, with the relevant comparison C_b ⪯₁ X, E₁X ∩ M = (c_b ∖ P) ∪ Q, X regular.

---

## 0. Outcome

**Q_N2 has answer YES (PROVED).** There is a full two-world system on M_U, world 2 additive with density 1, in
which world 1 is totally blind: every bounded endorser of world 1's relevant comparisons, for every localization,
is purely finitely additive on M. So **(V0) is not excluded by any two-world obstruction**, and it is not closed for
T1. But the example has a σ-finite endorser, and that is exactly what H1.2 forbids next to integrable partners. So
the strong reading of the brief's gloss ("even σ-finite endorsers fail") is **not** obtained, and it is **not**
implied by total blindness.

1. **Theorem P1.10 (the totally blind full system; PROVED).** For every K′ there is a ranking on M_U with strict (G),
   (IB), (LA), (S) (the C2.1 path, competitiveness on supp p, closed sections for **every** model at both worlds),
   (C), C_L = {C_b}, and (LF) at every interior C_b; world 2 is additive with density 1.
   - *Design.* L2's world 1, with L2's single source strip c_a replaced by a **thin source region S that reaches
     every point of the chain**: S = c_{u₀} ∪ ⋃_k S_k, where S_k is a sliver of block B_k of measure
     s_k ≤ r_k/(100N_k), N_k := ⌈log₂(50/r_k)⌉.
   - Level n trades strips of S ∩ c_{v_n} (v_n the left end of the level-n blocks) against projective-plane lines of
     reference blocks, one generator per level, exactly as in L2.
   - Thinness keeps every source of a later level negligible next to every reference block: ∫_{x≥u_k} g_F⁻ ≤ r_k/25
     for every selector F. So L2's blocking, strictness and no-weak-domination arguments survive. The last needs a
     new two-case argument (§3).
2. **Theorem P1.13 (total blindness; PROVED).** For every localizing D and every ν ∈ 𝒩(𝔚_D), ν(c_b) = 0 for every
   b < 1. Hence Λ = Λ_D = Λ_∞ = M (a_∞ = 1 in K3.8's notation), (NC) holds, and world 1 is in mode (M2).
   - The proof has two steps. Thin sources are blind by L2's certificates, now at every depth.
   - Everything else is blind because it can be moved rightward, piece by piece, into blind thin sources (a T-move
     into a set of positive but arbitrarily small measure, used once per piece).
3. **Proposition P1.14 (PROVED).** For a suitable choice of the free parameters, world 1 of P1.10 is (Loc) with
   D ≡ ∅: some ρ = φ∘x, φ finite and nondecreasing with ∫^1 φ = ∞, endorses every relevant comparison. So the
   example lies in (Loc) ∖ (Loc_int), like L2.
   - **Total blindness does not imply ¬(Loc).**
   - Next to two worlds with integrable endorsing densities, (Loc) worlds are excluded (H1.2). So the example cannot
     be the exceptional world of a T1 cover with additive partners.
4. **What closedness does forbid (general, two worlds next to an additive world; PROVED).**
   - **Lemma P1.15.** Equal-measure cut moves are accepted. Every non-null S ⊆ c_s, s < 1, has a capacity
     κ(S) := inf{λ(W) : S ≤₁ W} > 0.
   - **Lemma P1.16 (transport of ratios).** A trade P ≤₁ Q can be replayed by any W to the left of P (λ(W) ≤ λ(P))
     into any R to the right of Q (λ(R) ≥ λ(Q)).
   - **Proposition P1.17 (window ratio bound).** Every cut pair with source in d_{y₀} and target in c_t (t < 1)
     satisfies λ(Q)/λ(P) ≥ min(1 − t, κ(c_{y₀/2}))/y₀ > 0, provided λ(P) ≤ y₀/2.
   - **Corollary P1.18 (ends only at x = 1).** No full system has trades with vanishing ratio inside a fixed window.
     In particular the brief's "dense family of ends" (L2 blocks accumulating at interior points) violates (S). Ends
     must sit at the end of the chain, which is why P1.10 uses one end and sources everywhere.
   - P1.17 proves the "fixed position" half of the heuristic for CONJECTURE L2.C.
5. **What (V0) needs at three worlds, and the lift (§7).**
   - (V1)–(V5) of N2 §6 degenerate: p* = e₁, X₁₂ = P₂, X₁₃ = P₃, every edge model is a θ = 1 model, and the M1.7
     exchanges are internal.
   - With worlds 2, 3 additive (or with integrable CA endorsers), H1.2 adds one requirement: world 1 must be **¬(Loc)
     in the three-world system**. With partners that merely add up, nothing beyond (V1)–(V6) is known.
   - The natural lift of P1.10 (its world 1 on R₁₂ ∪ R₁₃, additive partners) has to destroy (Loc) through the interior
     forced cone, or H1.2 excludes it. I did not construct a lift.
   - The single open question is Q_P1 (§7.3).

| | Statement | Label |
|---|---|---|
| P1.10 | full two-world system with thin sources at every depth: every axiom, closed sections for every model | PROVED; NUMERICS |
| P1.11 | preorder, strict (G), (IB); same-level sums blocked with deep sources present | PROVED; NUMERICS |
| P1.12 | closed world-1 sections (compact selectors) | PROVED (L2.3 verbatim) |
| P1.13 | ν(c_b) = 0 for every bounded D-localized endorser, every D, every b < 1; Λ = Λ_∞ = M; (NC); (M2) | PROVED |
| P1.14 | σ-finite endorser φ∘x, D ≡ ∅: (Loc) ∖ (Loc_int) | PROVED; NUMERICS |
| P1.15 | equal-measure cut moves accepted; κ(S) > 0 | PROVED |
| P1.16 | transport of ratios | PROVED |
| P1.17 | window ratio bound | PROVED |
| P1.18 | no vanishing ratios in a fixed window; no interior ends | PROVED |
| P1.19 | (V0) at three worlds: what is forced, and H1.2's extra requirement | PROVED (from cited results) |
| Q_P1 | three-world (V0) with additive partners: world 1 totally blind and ¬(Loc)? | open |

NUMERICS (`p1py/q_n2_check.out`; exact rationals; 24 blocks with PG(2,2), PG(2,3), two gap pairs, 105 cells, 91
selectors). Every test passes:
- thinness bound 24/24 and model Θ_k ≤ r_k/25 7/7;
- 180/180 same-level pairs blocked (worst case over other-level sources);
- 300/300 nonzero δ ≤ 0 rejected; 100/100 δ ≥ 0 accepted;
- (K) 23/23; (U) 23/23, plus 117/117 at deep cuts;
- 18/18 generators accepted; 840/840 ternary sums of accepted vectors accepted;
- certificate identities 2/2 + 2/2; sections are initial segments containing [0, λ(A)] 60/60 + 60/60;
- φ monotone, φ(Q_g) ≥ φ(P_g) 18/18, and φ endorses 215/215 sampled accepted relevant vectors.

The blindness rate ε_n → 0 needs q_n ≥ 4^n and is not modelled.

---

## 1. Setting

As in L2 §1. World 2 is additive with density 1: X ⪯₂ Y iff λ(E₂X) ≤ λ(E₂Y). For a cut b and a model X put
A := E₁X ∩ M, N_X := N₊ ∖ X, P := c_b ∖ A, Q := A ∖ c_b. Then:
- C_b ⪯₂ X iff λ(Q) ≤ λ(P) + λ(N_X);
- the world-1 vector of C_b ⪯₁ X restricts on M to 1_Q − 1_P.

## 2. The design

**Blocks** (L2). Fix u₀ ∈ (0,1). Put r_k := (1 − u₀)5^{−k}, u_k := 1 − r_k, B_k := M ∩ {u_k ≤ x < u_{k+1}}
(λ(B_k) = (4/5)r_k). Let ref_k be the left (16/25)r_k of B_k and F_k := B_k ∖ ref_k (λ(F_k) = (4/25)r_k). The blocks
partition M ∩ {x ≥ u₀}, and λ(M ∩ {x ≥ u_k}) = r_k.

**Thin sources.** Put N_k := min{N ∈ ℕ : 2^N ≥ 50/r_k} (nondecreasing in k). Choose s_k with
0 < s_k ≤ r_k/(100N_k); P1.14 makes one further choice. Let S_k ⊆ F_k be the rightmost piece of F_k of measure s_k, and

  S := c_{u₀} ∪ ⋃_{k≥0} S_k,   s_{≥k} := λ(S ∩ {x ≥ u_k}) = Σ_{k′≥k} s_{k′} ≤ (5/4)r_k/(100N_k) ≤ r_k/(80N_k).   (2.1)

S is disjoint from every ref_k, and S ∩ {x ≥ y} is non-null for every y < 1.

**Levels** (L2). For n ≥ 1: K_n := 2^n, q_n a prime ≥ 4^n, Π_n := q_n² + q_n + 1, L_n := ⌊Π_n/K_n⌋.
- I_n is a set of Π_n consecutive block indices, identified with the points of PG(2, q_n). It lies to the right of
  I_{n−1}, with gap blocks allowed. Its first index is so large that (q_n + 1)r_{min I_n} ≤ 2^{−n}.
- v_n := u_{min I_n}, so v_n ↑ 1.
- Fix an injective assignment (i, l) ↦ line ℓ_{n,i,l} (i < K_n, l < L_n).

**Generators.**
- Σ_n := S ∩ c_{v_n} = c_{u₀} ∪ ⋃_{k<min I_n} S_k.
- {P_{n,i}}_{i<K_n} is any measurable partition of Σ_n into K_n sets of λ-measure λ(Σ_n)/K_n ≤ 2^{−n}.
- Q_{n,i,l} := ⋃_{k∈ℓ_{n,i,l}} ref_k, and g_{n,i,l} := 1_{Q_{n,i,l}} − 1_{P_{n,i}}. 𝒢_n is the finite set of level-n
  generators.

Facts:
- **(G1)** P_{n,i} ⊆ S ∩ c_{v_n}, Q_{n,i,l} ⊆ ⋃_{k∈I_n} ref_k ⊆ d_{v_n}, and
  max_{g∈𝒢_n}‖g‖₁ ≤ 2^{−n} + (q_n+1)(16/25)r_{min I_n} ≤ 2^{1−n}.
- **(G2), (G3)** as in L2: two level-n targets share a ref_k, and each k ∈ I_n lies on q_n + 1 lines.
- **(G4)** Targets are reference blocks, sources lie in S, and S ∩ ⋃_k ref_k = ∅. Targets of different levels are
  disjoint.

**Selectors, base cone, world 1, world 2**: verbatim L2 §2.
- 𝔉 := ∏_n(𝒢_n ∪ {⊥}), and g_F := Σ_{n : F(n)≠⊥} g_{F(n)} (L¹-convergent by (G1)).
- World 1 has rules R⁻ (D(δ) < 0: reject), R⁺ (D(δ) > 0: accept) and R⁰ (D(δ) = 0: accept iff δ = 0 a.e. on N₊ and
  δ|_M ∈ 𝒜 := ⋃_{F∈𝔉}(g_F + T)).
- X ⪯₁ Y iff 1_{E₁Y} − 1_{E₁X} is accepted. World 2 = λ.

By (G4), for every selector F:
- g_F ∈ {0, 1} on ⋃_k ref_k, with g_F = 1 on ref_k iff k lies on the line of some F(n);
- g_F ≥ 0 off S;
- g_F⁻ ≤ Σ_n 1_{P_{F(n)}} on S.

**Lemma P1.10a (deep sources are negligible; PROVED).** Let F be a selector and k ∈ I_n. Then

  Θ(F, k) := ∫_{M∩{x≥u_k}} g_F⁻ dλ ≤ r_k/25.

*Proof.*
- For n′ ≤ n, P_{F(n′)} ⊆ c_{v_{n′}} ⊆ c_{v_n} ⊆ c_{u_k}, so these sources contribute nothing.
- For n′ > n, λ(P_{F(n′)} ∩ {x ≥ u_k}) ≤ min(2^{−n′}, s_{≥k}), since c_{u₀} ∩ {x ≥ u_k} = ∅.
- So Θ ≤ Σ_{n′≥1} min(2^{−n′}, s_{≥k}) ≤ N_k s_{≥k} + 2^{−N_k} ≤ r_k/80 + r_k/50 < r_k/25, by (2.1) and
  2^{N_k} ≥ 50/r_k. ∎

## 3. Every axiom

**Lemma P1.11 (PROVED).** The world-1 acceptance set contains every δ ≥ 0, no nonzero δ ≤ 0, and δ₁ + δ₂ whenever δ₁,
δ₂ are accepted and δ₁ + δ₂ is ternary. Hence (Lemma vectorform) ⪯₁ is a preorder on M_U with strict (G) and (IB).

*Proof.*
- *δ ≥ 0, and the rules R±.* Verbatim L2.2.
- *δ ≤ 0, δ ≠ 0, D(δ) = 0, δ|_M = g_F + f with f ∈ T.*
  - If F ≡ ⊥: τ_f(0) = ∫δ < 0, a contradiction.
  - Otherwise pick n with F(n) ≠ ⊥ and k on its line. On {x ≥ u_k}: f = δ − g_F ≤ −g_F, so f ≤ −1 on ref_k and
    f ≤ g_F⁻ elsewhere.
  - By P1.10a, τ_f(u_k) ≤ −(16/25)r_k + r_k/25 < 0, a contradiction.
- *Sums.* As in L2.2, everything reduces to σ := δ₁ + δ₂ ternary with D(σ) = 0 and δ_j|_M = g_{F_j} + f_j.
  - If F₁, F₂ use no common level, g_{F₁} + g_{F₂} = g_{F₁∪F₂}, and σ is accepted.
  - Otherwise both use level n. By (G2) both targets contain ref_k for some k ∈ I_n. Put f := σ − g_{F₁} − g_{F₂} ∈ T.
  - On ref_k, f ≤ 1 − 2 = −1. On {x ≥ u_k} ∖ ref_k, f ≤ 1 + g_{F₁}⁻ + g_{F₂}⁻.
  - So τ_f(u_k) ≤ −(16/25)r_k + (9/25)r_k + 2r_k/25 = −(5/25)r_k < 0, by P1.10a. So this case does not occur. ∎

**Lemma P1.12 (closed world-1 sections, every model; PROVED).** For every model X, S₁(X) := {b : C_b ⪯₁ X} is closed.
It is an initial segment containing [0, λ(A)] when X is regular, and it is [0,1] otherwise.

*Proof.* Verbatim L2.3 and its Remark (L23_referee §A.2). The only input is
Σ_n max_{g∈𝒢_n} 2‖g‖₁ < ∞, which is (G1). ∎

**Theorem P1.10 (PROVED).** The ranking of §2 with selection p ↦ C_{p₂} satisfies strict (G), (IB), (LA), (S)
(competitiveness on supp p and closed sections for every model at both worlds), (C), C_L = {C_b : b ∈ [0,1]}, and
(LF) at every interior C_b.

*Proof.* Steps 1–3, 5, 6 are verbatim L2.1, with P1.11 and P1.12 in place of L2.2 and L2.3. Step 2 ((K) for every
model) uses only T ⊆ 𝒜 (F ≡ ⊥). The world-2 sections are closed by continuity. Step 4 (no weak domination) is new,
because L2's case split used that every source lies in c_a.

- *Setup.* Suppose X ⪯₁ C_b and X ⪯₂ C_b. R⁻ forces N_X null. Then λ(P) ≤ λ(Q) and
  δ′ := 1_P − 1_Q = g_F + f with f ∈ T; here P ⊆ c_b and Q ⊆ d_b.
- *F ≡ ⊥.* τ_f(b) = −λ(Q) ≥ 0, so Q is null and then λ(P) ≤ 0.
- *Case (i): some selected level n has a block k on its line with u_k ≥ b.*
  - τ_{δ′}(u_k) = −λ(Q ∩ {x ≥ u_k}) ≤ 0, since P ⊆ c_b ⊆ c_{u_k}.
  - τ_{g_F}(u_k) ≥ λ(ref_k) − Θ(F, k) ≥ (15/25)r_k > 0.
  - So τ_f(u_k) < 0, which is impossible.
- *Case (ii): every block k on every selected line has u_k < b.*
  - Then v_n < b for every selected n, so every selected source lies in c_b and g_F ≥ 0 on d_b.
  - So τ_f(b) = −λ(Q) − τ_{g_F}(b) ≤ −λ(Q). Hence Q is null, and then P is null.
- *Conclusion.* So X = C_b. With L2.1 step 5 (Theorem kkm needs only (LA) and (S)), C_L = U_L = {C_b} and (C)
  holds. ∎

## 4. Total blindness

**Theorem P1.13 (PROVED).** In the system of P1.10, let D be any localizing family and ν ∈ 𝒩(𝔚_D). Then ν(c_b) = 0
for every b < 1. Consequently:
- ρ_ν = 0 a.e. on M for every such ν, so Λ_D = M for every D and Λ = Λ_∞ = M;
- (NC_𝔚) holds, so 𝒩 ≠ ∅ and the statement is not vacuous;
- world 1 is in mode (M2): it neither adds up nor has a finite (M1) certificate.

*Proof.*
- **Step A: thin sources are blind.** This is L2.4(a) at every level, with cut v_n in place of a.
  - Fix n. Choose m with λ(D_m ∩ B_k) ≤ λ(F_k ∖ S_k)/2 for the finitely many k ∈ I_n. This is possible since
    λ(F_k ∖ S_k) ≥ (3/25)r_k.
  - For k ∈ I_n put Z_k := ref_k ∩ D_m, and choose R_k ⊆ (F_k ∖ S_k) ∖ D_m with λ(R_k) = λ(Z_k). Then
    f_k := 1_{R_k} − 1_{Z_k} ∈ T.
  - For g = g_{n,i,l}, δ′ := g + Σ_{k∈ℓ} f_k = 1_{Q′} − 1_{P_{n,i}}, with Q′ := (Q ∖ D_m) ∪ ⋃_{k∈ℓ} R_k. It is ternary
    (R_k ∩ P_{n,i} = ∅, since R_k ⊆ d_{v_n}) and lies in g + T.
  - It is the vector of the cut pair (P_{n,i}, Q′) at v_n, so it is relevant. It is D-localized (Q′ ∩ D_m = ∅).
  - Put h_n := Σ_{i,l} L_n^{−1} δ′_{n,i,l} = Σ_{i,l} L_n^{−1} 1_{Q′_{n,i,l}} − 1_{Σ_n}. Each strip occurs L_n times
    with weight 1/L_n, and the strips partition Σ_n.
  - By (G3), h_n ≤ ε_n − 1_{Σ_n}, with ε_n := (q_n+1)/L_n ≤ 4·2^{−n} (L2.4).
  - So 0 ≤ ν(h_n) ≤ ε_n − ν(Σ_n). Since Σ_n increases and v_n ↑ 1, ν(S ∩ c_b) ≤ ν(Σ_n) ≤ ε_n for all large n. So
    **ν(S ∩ c_b) = 0 for every b < 1.**
- **Step B: everything else empties into S.**
  - Fix b < 1. Pick b″ ∈ (b, 1) and m with G := (S ∩ {b ≤ x < b″}) ∖ D_m non-null (S reaches every point, and
    λ(D_m) → 0). Put γ := λ(G) > 0.
  - Partition c_b into finitely many W_1, …, W_J with λ(W_j) ≤ γ, and choose G_j ⊆ G with λ(G_j) = λ(W_j).
  - The cut pair (W_j, G_j) at b has vector 1_{G_j} − 1_{W_j} ∈ T, since G_j lies to the right of W_j with equal
    measure. So it is accepted, relevant and D-localized.
  - Hence ν(W_j) ≤ ν(G_j) ≤ ν(S ∩ c_{b″}) = 0 by Step A. So ν(c_b) = Σ_j ν(W_j) = 0. (Each W_j uses its own
    comparison, so the room γ is never exhausted.)
- **Consequences.**
  - ρ_νλ ≤ ν gives ∫_{c_b} ρ_ν = 0 for every b < 1, so ρ_ν = 0 a.e. on M. With K3.1(c),(d), Λ_D = M for every D.
  - (NC): let Σ_j w_jδ_j be a finite nonnegative combination of accepted relevant vectors δ_j = 1_{A_j} − 1_{c_{b_j}}.
    If b_j = 1 then δ_j ≤ 0, so δ_j = 0 by strictness. With b* := max b_j < 1, every δ_j ≥ 0 on the non-null d_{b*},
    so the sum is not ≤ −1.
  - ¬(M1): suppose the sum is ≤ 0. On d_{b*} it is Σ w_j1_{A_j∩d_{b*}} ≥ 0, so each A_j ∩ d_{b*} is null. Then
    δ_{j*} ≤ 0 for b_{j*} = b*, so δ_{j*} = 0. Delete it and induct: every δ_j = 0.
  - ¬(M0): Λ is non-null (K3.1(c)). ∎

*Reading.*
- Strict (G) holds everywhere, yet no bounded charge with a countably additive part, localized or not, endorses
  world 1.
- Every endorser lives "at x → 1": ν(c_b) = 0 for b < 1 and ν(M) = 1. This is the totally blind (V0) pattern of
  K3.3's tilted world, now with closed sections.
- The two steps use different mechanisms: projective certificates on the thin sources, and repeated T-moves into
  arbitrarily thin blind sets for the rest. Step B is the new ingredient: blindness spreads leftward from any blind
  set that reaches every depth.

## 5. The example is (Loc)

**Proposition P1.14 (PROVED).** Choose the free parameters of §2 inductively as follows.
- φ := 1 on M ∩ {x < v₁}.
- At stage n, the value φ_prev on the gap before I_n is known. Choose min I_n so that, in addition to (G1),
  (16/25)r_{min I_n} φ_prev ≤ u₀/(K_n(q_n + 1)).
- Choose the strips P_{n,i} with equal λ-mass **and** equal φλ-mass π_n := ∫_{Σ_n}φ dλ/K_n. This is possible by
  Lyapunov halving applied to the non-atomic finite vector measure (λ, φλ) on Σ_n; φ is bounded there.
- Put C_n := π_n/(q_n + 1). Set φ := C_n/λ(ref_k) on the x-range of B_k for k ∈ I_n, and φ constant (equal to the
  last value) on the following gap blocks.
- Take s_k := min(r_k/(100N_k), 2^{−k}/φ_k), where φ_k is the value of φ on B_k.

Then φ is finite and nondecreasing, ∫^1 φ = ∞, and ρ := φ∘x on M (ρ := 1 on N₊) endorses every relevant world-1
comparison in the cancellation reading. So world 1 is (Loc) with D ≡ ∅ and lies in (Loc) ∖ (Loc_int).

*Proof.*
- *Well-defined (no circularity).*
  - φ_k for k ∈ I_n depends only on s_{k′} for k′ < min I_n, so s_k can be chosen after φ_k.
  - φ ≥ 1 gives π_n ≥ u₀/K_n.
  - s_kφ_k ≤ 2^{−k} gives ∫_Sφ ≤ u₀ + 2 ≤ 3, so π_n ≤ 3·2^{−n}.
- *Monotone.* Within I_n, λ(ref_k) decreases. At v_n the new value is
  C_n/λ(ref_{min I_n}) ≥ u₀/(K_n(q_n+1)λ(ref_{min I_n})) ≥ φ_prev.
- *Generators are φ-neutral.* ∫_{Q_{n,i,l}}φ = (q_n+1)C_n = π_n = ∫_{P_{n,i}}φ.
- *Base.* For bounded nondecreasing ψ ≥ 0 and f ∈ T, ∫ψf dλ ≥ 0. Write ψ = ∫_0^∞ 1[ψ > s] ds. Each {ψ > s} ∩ M is
  {x > y_s} or {x ≥ y_s}, which agree mod null. So ∫ψf = ∫_0^{sup ψ} τ_f(y_s) ds ≥ 0, by Fubini.
- *Endorsement.* Let δ be an accepted relevant vector: δ = 1_A − 1_{c_b}, b < 1 (b = 1 forces δ = 0),
  δ|_M = g_F + f, δ = 0 on N₊.
  - ρ(δ⁻) ≤ ∫_{c_b}φ < ∞. If ρ(δ⁺) = ∞ there is nothing to prove, so let ∫ρ|δ| < ∞.
  - For φ_N := min(φ, N): ∫φ_Nδ = ∫φ_N g_F + ∫φ_N f ≥ Σ_n ∫φ_N g_{F(n)}, by L¹ convergence and the base step.
  - Each term lies in [−π_n, π_n] and tends to ∫φ g_{F(n)} = 0 as N → ∞ (φ is bounded on P ∪ Q).
  - Σπ_n < ∞, so by dominated convergence the sum tends to 0. Also ∫φ_Nδ → ∫ρδ (dominated by ρ|δ|).
  - Hence ∫ρδ ≥ 0, i.e. ρ(δ⁻) ≤ ρ(δ⁺).
- *∫^1 φ = ∞.* Otherwise ρλ would be a bounded endorser with ρ > 0 on M, against P1.13. ∎

*Remarks.*
- **Total blindness does not imply ¬(Loc).** The brief's gloss "total blindness means even σ-finite endorsers fail"
  is false in general: P1.13 and P1.14 hold in one system. This is consistent with F1.2: its σ-finite endorsers are
  φ(x)λ, and here φ is non-integrable at the end.
- **For T1 (from H1.2, PROVED there).** Next to two worlds with integrable densities endorsing all their relevant
  comparisons, a world of class (Loc) (any a.e.-finite ρ₁, any localization) is impossible under (H_U). So P1.10's
  world 1, installed unchanged as an exceptional world next to additive partners, is excluded.

## 6. What closedness does forbid: ratios in a window

**Setting for §6.** The setting of F1.2: a two-world system on M_U with strict (G), (IB), (LA), (S) with closed
sections for every model, and (C). World 2 is additive with an integrable density w > 0. Put
λ := wμ|_M/(wμ)(M). The selection is nested (S1.6), with no jumps (N1.4(a)). Reindex the chain so that λ(c_b) = b.
Nothing is assumed about world 1 beyond the axioms. Write ≤₁ for acceptance of 1_Q − 1_P.

**Lemma P1.15 (PROVED).**
- **(a) Cut moves.** If P ⊆ c_b, Q ⊆ d_b (b ∈ (0,1)) and λ(Q) ≥ λ(P), then P ≤₁ Q, as a relevant comparison at b.
- **(b) Capacity.** For s < 1 and non-null S ⊆ c_s, κ(S) := inf{λ(W) : W ∩ S = ∅, S ≤₁ W} > 0. Also κ is
  monotone: S ⊆ S′ ⇒ κ(S) ≤ κ(S′).

*Proof.*
- **(a)**
  - If λ(Q) > λ(P), this is (K) (F1.2's first paragraph).
  - If λ(Q) = λ(P), let X be the regular model with E₁X ∩ M = (c_b ∖ P) ∪ Q. For interior b′ < b,
    λ(E₂X) = λ(d_b) < λ(d_{b′}), so C_{b′} ⋠₂ X, and competitiveness gives C_{b′} ⪯₁ X. The chain points b′ ∈ (0,1)
    are selected only at interior priors.
  - The closed section S₁(X) then contains b.
- **(b)**
  - Monotonicity: S′ ≤₁ W gives S ≤₁ W (F1.4(i)).
  - Let X be regular with E₁X ∩ M = (c_s ∖ S) ∪ d_s. For b ∈ (s, 1) the vector of C_b ⪯₁ X is 1_{d_b} − 1_S.
  - Suppose S ≤₁ W with λ(W) ≤ 1 − b. Choose Z ⊆ d_b ∖ W with λ(Z) = λ(W ∩ c_b); there is room, since λ(W) ≤ λ(d_b).
    By (a), W ∩ c_b ≤₁ Z.
  - Chaining (F1.4(iii); Z ∩ S = ∅) gives S ≤₁ W′ := (W ∩ d_b) ∪ Z ⊆ d_b. Adding 1_{d_b} − 1_{W′} ≥ 0 gives
    1_{d_b} − 1_S accepted, i.e. b ∈ S₁(X).
  - So if κ(S) = 0, then [0,1) ⊆ S₁(X) (S₁ is an initial segment by (G) and transitivity). Closedness, with
    p ↦ λ(c_p) continuous and onto, gives C₁ = P₂ ⪯₁ X. Its vector is 1_A − 1_M = −1_S ≤ 0 and nonzero, against
    strict (G). ∎

(b) is the closedness-at-the-end mechanism behind Prop. Q15(a). It is stated here because §6 needs it for arbitrary S,
with this proof.

**Lemma P1.16 (transport of ratios; PROVED).** Let P ≤₁ Q be a cut pair at b. Let y ≤ b with P ⊆ d_y, and t ≥ b
with Q ⊆ c_t. Let W ⊆ c_y with λ(W) ≤ λ(P), and R ⊆ d_t ∖ (P ∪ Q) with λ(R) ≥ λ(Q). Then W ≤₁ R, as a relevant
comparison at t. For pairwise disjoint W_1, …, W_m and R_1, …, R_m of this kind, ⊔W_i ≤₁ ⊔R_i.

*Proof.*
- W ≤₁ P is a cut move at y, and Q ≤₁ R is a cut move at t (P1.15(a)).
- The sets W, P, Q, R are pairwise disjoint: W ⊆ c_y ⊆ c_b, Q ⊆ d_b, R ⊆ d_t ∖ (P ∪ Q).
- So (1_P − 1_W) + (1_Q − 1_P) = 1_Q − 1_W and then + (1_R − 1_Q) = 1_R − 1_W are ternary partial sums of accepted
  vectors, hence accepted (F1.4(iii)).
- W ⊆ c_t and R ⊆ d_t, so this is the cut pair (W, R) at t.
- Disjoint sums: F1.4(iv). ∎

**Proposition P1.17 (window ratio bound; PROVED).** Let 0 < y₀ < t < 1 and κ₀ := κ(c_{y₀/2}) > 0. Every cut pair
P ≤₁ Q with P ⊆ d_{y₀}, Q ⊆ c_t and λ(P) ≤ y₀/2 satisfies

  λ(Q)/λ(P) ≥ min(1 − t, κ₀)/y₀.

*Proof.*
- Let the cut be b. Then y₀ < b ≤ t: P ⊆ d_{y₀} ∩ c_b is non-null, and Q ⊆ d_b ∩ c_t. So P ∪ Q ⊆ c_t.
- Partition c_{y₀/2} into m := ⌈(y₀/2)/λ(P)⌉ sets W_i with λ(W_i) ≤ λ(P). Since λ(P) ≤ y₀/2, m ≤ y₀/λ(P).
- *Room.* If mλ(Q) ≤ 1 − t, choose disjoint R_i ⊆ d_t with λ(R_i) = λ(Q). By P1.16 (with y = y₀),
  c_{y₀/2} ≤₁ ⊔R_i, so κ₀ ≤ mλ(Q) ≤ y₀λ(Q)/λ(P).
- *No room.* Otherwise λ(Q) > (1 − t)/m ≥ (1 − t)λ(P)/y₀. ∎

**Corollary P1.18 (no vanishing ratios in a window; ends only at x = 1; PROVED).**
- **(a)** In the setting of §6, for fixed 0 < y₀ < t < 1 there is no sequence of cut pairs P_j ≤₁ Q_j with
  P_j ⊆ d_{y₀}, Q_j ⊆ c_t and λ(Q_j)/λ(P_j) → 0.
- **(b) Interior ends are impossible.** Take L2's design (or P1.10's) with its blocks accumulating at an interior
  point t* < 1 instead of at x = 1 (a "dense family of ends" of the brief is a special case). Then it violates (S).
  - The level-n generators with sources P_{n,i} ⊆ {a/2 ≤ x < a} and targets in c_{t*} have ratio
    (q_n + 1)(16/25)r_{min I_n}/(a2^{−n}) → 0. This contradicts (a).
  - Concretely, transitivity forces the replicated trades of P1.16, and their sum c_{a/2} ≤₁ (sets of vanishing
    measure) contradicts P1.15(b) at b = 1. This is what L2's blocking inequality (B) prevents when the end is x = 1:
    there is no room to the right.
  - For full certificates (sources covering a fixed S, targets in c_{b₀}) this already follows from F1.4. (a) is
    stronger: it concerns single trades, with no covering, and its bound is linear in λ(P), where F1.4's θ(S, b₀)
    degenerates as λ(S) → 0.
- **(c) For CONJECTURE L2.C.** The L2 referee and L2 §5 identified, as the way to defeat every finite φ, "accepted
  localized cut pairs with Q in a fixed c_t and λ(Q)/λ(P) → 0 at fixed positions". (a) excludes exactly that.
  - What remains for an (N) world next to an additive world: pairs whose ratio is bounded below in every window but
    is < 1, concentrated at the cut, at a set of cuts that φ cannot absorb by countably many jumps.
  - Chaining (P1.16) multiplies such ratios and must then leave every window, by (a).
  - I did not close this. L2.C stays a CONJECTURE.

*Reading.* P1.10 lives exactly on the right side of P1.18. Its trades with vanishing ratio have targets in blocks
that approach x = 1 as the ratio vanishes, and with no room beyond them. Its sources reach every depth only as a
**thin** set, which is why blindness spreads (Step B) without creating room for replication.

## 7. (V0) at three worlds, and the lift

**7.1 What (V0) forces (Proposition P1.19; PROVED from the cited results).** Setting: n = 3, (H_U), worlds 2 and 3
add up (L4.9's setting) and world 1 satisfies (NC). (V0) means V₁ null, i.e. Λ₁ = M. Then:
- **(V1)** The CA field of the maximal tuple is c* = (0, ρ₂σ₂, ρ₃σ₃), and p* = e₁ with A(c*) = {e₁} (N2 §6 (V1),
  from L4, L4_referee and M1.2). The other clauses of (V1) (Λ₁ ⊋ E₁(T1) ∩ M, Λ₁ ⊇ M ∩ {g₁ > 0}, V₁ ⊆ {g₁ < 0}) hold
  trivially. With ρ₂ = ρ₃ = 1 this is M1.1(c)'s field: every B_q (q ∈ Δ°) is P₂, P₃ or P₂ ∩ P₃.
- **(V2)** X₁₂ = E^{1,+} has world-1 errors Λ₁ ∩ R₁₂ = R₁₂, so X₁₂ = P₂. Likewise X₁₃ = P₃. N2.3′ is trivially true;
  M1.2's e₂ ∈ K₁ and e₃ ∈ K₀ hold with D_{K₁} = P₂ and D_{K₀} = P₃.
- **(V3)** For the pair (ρ₁, ρ₂) = (0, ρ₂), e_θ = −(1−θ)ρ₂ on R₁₂, so N2.1(c) holds with θ = 1 for every edge model,
  and N2.2 is vacuous. Nothing constrains the edge selections beyond the axioms.
- **(V4)** The M1.7 exchange on [e₁, e_j] is internal (int₁) (N2.4 with Λ₁ = M).
- **(V5)** T1 is (2,3)-Bayes on J₂ ∪ J₃ (N2.5′).
- **(V6) and H1.2.** If worlds 2 and 3 have integrable densities ρ₂, ρ₃ > 0 endorsing all their relevant comparisons
  (for instance, additive worlds with integral penalties), world 1 must moreover be ¬(Loc) in the three-world system
  (H1.2). Since it is not (M0) (M0closed(b)) and not (Loc), it is (M1) with (NC), or (N) (K3.7's first sentence).
  The (M1) branch makes its certificate's negative set blind (L4.4), which Λ₁ = M allows.
- **Two-world test.** P1.10 shows that the two-world part of this (closed sections, strict (G), a nested chain from P₁
  to P_j, total blindness) is consistent. So no edge-by-edge argument of N1/N2/L3.4 type can exclude (V0).
  - N1.1, N1.2 and N2.2 need a visible set.
  - L3.4 needs a CA veto. Here Φ₁ ≡ 0 (V₁ null), so N2.7(d) does not apply.

**7.2 The lift attempt.**
- *Natural lift.* Worlds 2, 3 additive with densities ρ₂, ρ₃. On each edge region R₁ⱼ take an edge path of coherent
  models D_{K^j_s} from P₁ to P_j, with K^j_s ∩ [e₁, e_j] ≠ ∅ (K3.7′). Give world 1 the P1.10 design along each edge
  chain: thin sources at every depth of the chain, blocks at the far end, which is the e₁-ray end inside (+,−,−)
  (E1.3, L2 §7.1).
- *Where it breaks.* In two worlds this design carries a σ-finite endorser φ∘x (P1.14). The three-world analogue
  is CONJECTURE, not proved. Whenever world 1's three-world relevant comparisons are endorsed by some a.e.-finite ρ₁,
  H1.2 gives a contradiction outright, before closedness, (C) or (LF) at T1 are reached.
  - So the forced cone of world 1 must defeat every a.e.-finite ρ₁. The forced cone consists of the comparisons
    C_p ⪯₁ X forced because X strictly beats C_p at worlds 2 and 3, for p ∈ Δ°.
  - L2 §7.2's wedge leaks are the only known source of such additional forced trades. They move world-1 mass into the
    tie wedges of R₂₃. Whether they can defeat every ρ₁ without also violating blocking (L2 §7.1(ii)) is the open
    point.
  - In two worlds the forced cone is only (K), and P1.17 constrains it. In three worlds P1.17 has no proved analogue
    on edges: (Nest_e) does not follow from the axioms (S1, "Edges").
- *With partners that merely add up.* If the endorsing weights of worlds 2, 3 have essential purely finitely additive
  parts, H1.2 does not apply. Then no known result excludes a (Loc) totally blind world 1. P1.10 is the two-world
  template, and L2 §7.1 (i)–(v) is the list a lift must verify, with the M1.7 exchanges internal (V4).
  - I did not attempt this lift beyond identifying it.

**7.3 Single open question (Q_P1).** On M_U (n = 3, T1, K′ = u + s(T1 − u)), is there a ranking with (H_U), worlds 2
and 3 additive with integrable densities, and world 1 totally blind (Λ₁ = M)? By H1.2 world 1 would have to be
¬(Loc).
- "No" closes (V0) for additive (more generally, integrably endorsed) partners.
- Its two-world shadow is "a totally blind (N) world with closed sections next to an additive world". This is the
  negation of L2.C restricted to Λ = M. P1.17/P1.18 prove the fixed-window half of L2.C, and P1.10/P1.14 show that
  total blindness alone is not the obstruction.

So (V0) is **not** closed. The precise status: two-world total blindness with closed sections is possible (P1.10,
P1.13). What remains is the three-world requirement ¬(Loc) of H1.2, which in two worlds is L2.C, open.

## 8. Dependencies and files

**Used.**
- L2 §§1–4 (design, L2.1–L2.4; refereed CORRECT in L23_referee §A). Lemma vectorform; Theorem kkm; C2.1(4) for (LF).
- K3.1 (localization, blind sets, (NC)), K3.8.
- F1.2 (first paragraph: (K) at cuts), F1.4(i)–(iv) (shrinking, chaining, disjoint sums).
- S1.6 (nested selection next to an additive world), N1.4(a) (no jumps).
- H1.2 (§§5, 7). M1.1(c), M1.2, N2.1–N2.5′, N2.7(d), K3.7, K3.7′, L3.4, E1.3 (§7 only).

**Not used.** (LF) except as imported; any three-world result in §§2–6; Lyapunov except in P1.14.

**Not refereed.** Points to check, in order of risk:
1. P1.10 step 4, case (ii): every selected source lies in c_b.
2. P1.10a: the bound Σ_{n′} min(2^{−n′}, s_{≥k}) ≤ N_ks_{≥k} + 2^{−N_k}, and that sources of levels ≤ n lie left of
   u_k.
3. P1.13 Step B: the finitely many pieces W_j, each with its own D-localized comparison into the same G.
4. P1.15(b): the export into d_b and the closedness at b = 1.
5. P1.17: the disjointness of the W_i, P, Q, R_i.

`p1py/` (new files only; run with `python3 -I -B` from inside `p1py/`):
- `q_n2_common.py`: finite cell model (24 geometric blocks, thin S-slivers in every block, two levels with PG(2,2)
  and PG(2,3), gap blocks, 91 selectors), exact rationals.
- `q_n2_check.py` (+ `q_n2_check.out`): the tests listed in §0.
- `archive_P1_notes_2026-10-14.md`: verbatim copy of Part II.

---
---

# Part II — the earlier note P1 (14 Oct 2026, round 11), verbatim

# P1. Case M0 on the U-domain: can atom chords of ψ rescue a cover of T1?

14 Oct 2026, BRIEF10 (round 11), construction side. Scripts: `p1py/`. Labels: **PROVED** (full proof here), **CHECKED**
(sketch, or proof imported from the write-up), **CONJECTURE**, **NUMERICS**. Nothing is assumed beyond the write-up's
framework. Notation as in "The Contamination Triangle" (§§2, 4, 7): U = D_{K′}, c(g) = ρ(g)⊙sign(g), B_q = {q·c > 0},
K♭_q (B_q = D_{K♭_q} a.e., for EVERY q, Thm Estructure(d)), E(ψ) = union of atom chords, p* the ψ-Bayes weighting of
T1, normalised p* = u, facet data x_k as in Prop T1.

---

## 0. Outcome

**No cover was constructed. No proof that M0 is impossible was found.** What was obtained:

1. **Reduction (CHECKED).** On M_U the three new routes (I1, I2, C2/short) are not the relevant obstruction. They are
   proofs for general decomposable domains, and their common input Cor TSalways(b) ("both acceptances in the advice range
   of a.e. mixed pair") is already contradictory on M_U. For a supporting assessment ψ on M_U, all of them reduce to the
   chain of §4 (Thm pivot → (PC), (NS) → corner equations + box). Every route enters through the facet data at p*.
   So a chord configuration defeats all three routes as soon as it defeats the facet-data algebra at p*.
2. **Straight levels survive every atom chord (PROVED, Lemma P1.2).** For every gamble h and level t, the sets
   {q : P_{K♭_q}(h) > t} and {q : P_{K♭_q}(h) < t} are half-planes ∩ int Δ, at every interior q. No continuity of K is
   needed. This removes one of the two "global" caveats in the write-up's localisation remark. Only PL2/nopin and
   evaluation at p* remain.
3. **One-sided holonomy (PROVED, Lemma P1.1).** The box bounds 1/κ ≤ x_k x_{k+1} ≤ κ and the corner relations weakened
   to *inequalities* x_k + 1/x_{k+1} ≥ κ+1 (k cyclic) have no positive solution. Here κ > 1.
4. **Atoms at corners cannot help (PROVED under hypothesis (HC), Thm P1.4).** An atom chord through p* whose atom sits
   at a corner of ∂D_{T1} turns (NS) at that corner into the *strict inequality* x_k + 1/x_{k+1} > κ+1, never the reverse
   (Lemma P1.3). By P1.1, any set of corner atoms through p* leaves the box contradiction intact. This covers R-a′(i)
   entirely (by Prop 4.3, a single atom at p* is a corner atom), and also the corner part of R-a′(ii), (iii).
5. **The escape that survives (NUMERICS, §4).** Atoms through p* whose arcs lie in the *middle* (+,+)-region of each
   facet ("split facets") give each facet two linear chart maps, of ratios a_k near one corner and b_k > a_k near the
   other. With (NS) at all three corners, b_k = κ+1 − 1/a_{k+1}, and the box admits solutions, for example
   a_k ≡ a ∈ (1/κ, 1). The semi-exact box search finds no certificate (log-margins −0.13 … −1.5 at ε = 0.1, 0.3, 0.6,
   0.9); the controls x_± give the known certificates. So the facet-data algebra at p* does **not** exclude M0.
   The configuration needs:
   - p* at a crossing of at least three atom chords, with a 2-dimensional face;
   - T1 intermediate in that face;
   - the mid-facet atoms *outside* cl D_{T1};
   - directional limits that drop vertices of T1.

   §4.3 gives proved constraints on it.
6. **Construction status.** Step (2) of the plan requires a global ψ (field c on U), and it is not achieved. Neither
   the split facet data nor any other configuration is known to extend from p* to the whole simplex with coherent B_q
   off E. Without ψ, the ordinal tie-breaking and the exact consistency test could not be run. §5 states the precise
   construction problem (CFJ) and what an obstruction would have to show.

---

## 1. What the additive proofs need from the Bayes family, and where atoms enter

**1.1 On M_U, I1/I2/C2 reduce to the §4 chain (CHECKED).**
- Thm gm's three routes start from §5.2 (Cor TSalways):
  - (b) a.e. mixed pair has both acceptances in its advice range;
  - (c) K_q → {e_b}, and edge confinement.

  On M_U no advice range contains both acceptances, so (b) already contradicts a cover. Edge confinement (K* ⊆ edge)
  is false on M_U in any case, because every K_q ⊇ K′.
- Cor TSalways rests on N21.4 items 1–5 and the localised N15 chain. So for ψ on M_U, the operative obstruction is
  Thm main, i.e. §4: Thm pivot, nosliding, PCNS, boxbridge, Prop T1.
- I1 then needs (PC) and the corner equation (x ≠ 1); I2 and C2 need the collar certificate, which uses x_+² > κ; the
  short route needs the collar. All of these come from the facet data at p*.

**1.2 Uses of the Bayes family in the §4 chain, and the effect of atom chords.**

| Step | Use of K | Atom chord through p* | Chord away from p* |
|---|---|---|---|
| Lemma chords/levels | joint continuity | harmless: Lemma P1.2 (K♭, every q) | harmless (P1.2) |
| Lemma UVN | q → e_l off E | harmless | harmless |
| Lemma PL2 in nopin (Step 1 of pivot) | clopen argument on int co(G ∪ V_l) | broken | broken if the chord separates G from V_l |
| Ψ(p*, τ) = 0 on [0,1] | K_{p*} = T1 | broken: P(p*, h) = P_{K♭}(h) may be < 0 (Thm pstarE) | harmless |
| Steps 3–5, nosliding, blow-up | continuity at p* | broken in the sectors cut by the chords | harmless if chords stay away from p* |
| Lemma edgebox | half-planes, E null | harmless (N26 §4.3) | harmless |
| boxbridge(c) | unique cluster lines of the witnesses | only through the facet data | harmless |

So the configurations that can defeat the chain are:
- (A) chords through p* (R-a′);
- (B) chords whose tie sets accumulate near a crossing ray of ∂D_{T1}, so that PL2 fails and a vertex may be pinned
  near p* (the write-up's Conj N26.R′; R-b′).

A **dense** family of chords enters only through (A) or (B).

---

## 2. Straight levels for K♭ at every weighting

**Lemma P1.2 (PROVED).** Let c be strictly signed on U, with B_q = D_{K♭_q} a.e. for every q ∈ int Δ. (This holds
for every supporting assessment: Thm Estructure(d).) For h ∈ ℝ³ put f(q) := P_{K♭_q}(h) and fix t. Then {f > t} is
int Δ ∩ (an open half-plane, ∅, or int Δ), and {f < t} is int Δ ∩ (a half-plane, possibly with part of its boundary,
∅, or int Δ).

*Proof.*
- *{f > t} is convex.* Let f(q₁), f(q₂) > t′ > t. On a ball O around h′ := h − t′𝟙, P_{K♭_{q_m}}(g) > 0 (continuity in
  g). For a.e. g ∈ O this gives g ∈ B_{q_m}, i.e. q_m·c(g) > 0, for m = 1, 2. By linearity, q·c(g) > 0 on [q₁, q₂].
  So for q ∈ [q₁, q₂], D_{K♭_q} contains a.e. point of O, hence all of O, since an open convex set containing a dense
  subset of a ball contains the ball. Thus P_{K♭_q}(h′) ≥ 0, i.e. f(q) ≥ t′ > t.
- *{f < t} is convex.* The same argument with P < 0 on O gives q_m·c(g) ≤ 0 on [q₁, q₂]. Then g ∉ B_q for a.e. g ∈ O,
  so O ∩ D_{K♭_q} is null and open, hence empty. So f(q) ≤ t′ < t.
- *Closing.* K♭ is upper semicontinuous (Estructure(d)), so f is lower semicontinuous and {f > t} is open. Also
  {f ≤ t} = ⋂_{t′>t} {f < t′} and {f ≥ t} = ⋂_{t′<t} {f > t′} are convex. Two complementary convex subsets of int Δ
  are separated by a line. ∎

*Consequence.* The write-up's localisation remark lists Lemma levels as surviving only off a null E (§7.2; N26_referee
§4.2). It holds verbatim at every interior weighting, for every field with (γ). Lemma sandwich holds wherever its
hypotheses at p* hold.

---

## 3. Corner atoms through p* do not help

**3.1 The algebra.**

**Lemma P1.1 (PROVED).** Let κ > 1, and let x₁, x₂, x₃ > 0 satisfy, for each k (indices mod 3),

 (C≥_k) x_k + 1/x_{k+1} ≥ κ+1,  (B_k) 1/κ ≤ x_k x_{k+1} ≤ κ.

This is impossible.

*Proof.* Fix k and put a = x_k, b = x_{k+1}.
- From ab ≤ κ: κ/b + 1/b ≥ a + 1/b ≥ κ+1, so b ≤ 1.
- From ab ≥ 1/κ: 1/b ≤ κa, so (1+κ)a ≥ κ+1, so a ≥ 1.

Applying this for k = 1, 2, 3 gives x_k ≥ 1 ≥ x_{k+1} for every k. Hence x₁ = x₂ = x₃ = 1, and then (C≥) reads
2 ≥ κ+1, a contradiction. ∎

(Sanity: `p1py/overlap_sympy.py`, 2·10⁵ random samples, none feasible.)

*Relation to Prop T1.* The six box bounds are those of Prop T1:
- x₁x₃ ≤ κ is the (1,2) certificate written with general facet data; the other two upper bounds are its cyclic images.
- The three lower bounds are the mirror certificates. For these, NUMERICS: the semi-exact search `p1py/box_exact.py`
  reproduces log(x₊²/κ) = 1.334 at ε = 0.3, and its binding certificates match log(1/(κ x_i x_j)) to 10⁻⁴. CHECKED
  through the transposition argument of Prop T1.

**Lemma P1.1 strengthens Prop T1.** The equality case is the corner equation. The box contradiction survives the
corners being only one-sided, in the "≥" direction.

**3.2 The sign of a corner atom.**

**Hypothesis (HC): the facet-data form of the chain with breaks.** For each facet F_k there are finitely many closed
arcs ("atom arcs"), each inside one sign-pattern region of F_k, such that:
- off the arcs, every facet gamble h has a unique oriented cluster line through p*;
- that line is given by a map Γ which is linear on each complementary piece of F_k;
- crossing rows hold on the pieces that contain crossings;
- on an atom arc the cluster line is the arc's atom chord (constant);
- the pivot normal is continuous along ∂D_{T1}, except at a corner without an atom, where (NS) holds;
- boxbridge(c) holds for witnesses off the arcs.

(HC) is what the §4 chain gives when no chord passes through p*, with no arcs. With chords through p*, (HC) is the
CONJECTURE that the chain runs sector by sector. It is not proved here, because PL2/nopin and Steps 3–5 of Thm pivot
would have to be redone in sectors with jumps.

**Lemma P1.3 (PROVED from (HC)).** Suppose an atom arc contains the corner r₃₁. Its pattern is that of r₃₁, (−,+,−),
and its chord cuts off e₂. Then x₃ + 1/x₁ > κ+1.

Here x₁ is the ratio of F₁'s piece next to r₃₁ and x₃ the ratio of F₃'s piece next to r₃₁. The same holds at every
corner, cyclically.

*Proof.*
- Parametrise the normals of pattern (−,+,−) by t := −b₁/(−b₁ − b₃) ∈ (0,1). Here t = 0 is the normal of lin(p*, e₁),
  i.e. (0,1,−1), the pivot of F₃'s 1-crossing; t = 1 is the normal of lin(p*, e₃), i.e. (−1,1,0), the pivot of F₁'s
  3-crossing.
- Γ₃ is linear, so t is strictly increasing along F₃ from its 1-crossing toward r₃₁. Γ₃ extended to r₃₁ gives
  t₃ = x₃/(κ+1).
- Likewise t increases along F₁ from r₃₁, where Γ₁ gives t₁ = 1 − 1/(x₁(κ+1)), to 1 at the 3-crossing.
- The arc has a single constant normal t_b, attained at its end h_b ∈ F₃ and its end h_a ∈ F₁, by continuity. So
  t₁ < t_b < t₃, strictly, since a non-null atom gives a non-degenerate arc.
- Finally t₃ − t₁ = (x₃ + 1/x₁ − (κ+1))/(κ+1) (sympy, `overlap_sympy.py`). ∎

*Reading.* In a realisation the pivot normal runs once round the circle with no overlap, and (NS) is the equality. An
atom can only produce an *overlap*: two facet pieces whose normal ranges overlap, joined by a constant arc. A *gap* is
what nosliding forbids, and an atom cannot fill it, because the arc's normal must be attained on both sides.

**Theorem P1.4 (PROVED from (HC)).** Assume (H_M0) and (HC), with all atom arcs at corners, and atoms through p* at any
subset of the three corners (R-a′(i), and the corner configurations of R-a′(ii), (iii)). Then no cover of T1 exists.

*Proof.*
- Without mid-facet arcs, each facet has one linear map. Its ratio x_k is shared by its two corners and by its boxes.
- Corners without atoms give equality by (NS), and corners with atoms give the strict inequality by Lemma P1.3. All
  satisfy (C≥).
- The box witnesses of Prop T1 lie arbitrarily near the crossings, which no atom arc contains (an arc lies in one
  pattern region), so (B_k) holds by boxbridge(c).
- Lemma P1.1 gives the contradiction. ∎

*NUMERICS cross-check.* With an atom only at r₃₁ and (NS) at r₁₂, r₂₃, the overlap condition holds on exactly two
branches: x₂ ∈ (1/(κ+1), x₋) and x₂ ∈ (x₊, κ+1). On the first all x_k < x₋; on the second all x_k > x₊. The
semi-exact search finds certificates on both branches at ε ∈ {0.02, 0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99}, with log
margins between 0.66 and 5.7, even after excluding the maximal possible r₃₁ arcs (`lower_branch.py`). The
general-subset run is `multi_atoms.py`. The point (κ, 1, 1/κ), with diagonal facet maps of weight (1, κ, 1), is
box-feasible with zero margin. There the r₃₁ defect is negative (a gap), so no atom can occur.

---

## 4. The surviving configuration: split facets

**4.1 Facet data with mid-facet arcs (PROVED from (HC)).** Let F₁ carry an atom arc inside its middle region
(h₂, h₃ > 0, pattern (−,+,+); the chord cuts off e₁). Write a₁ for the ratio of the piece next to r₃₁ (the piece
containing the 3-crossing) and b₁ for the piece next to r₁₂ (containing the 2-crossing). The normal parameter on the
middle region is u = ρ/(x + ρ), with ρ = h₃/h₂ increasing along F₁. Continuity across the arc gives
ρ_b/ρ_a = b₁/a₁, so **b₁ > a₁** (sympy). Cyclically on F₂ and F₃.

The pairings are then:
- corner r₁₂ ↔ (b₁, a₂), r₂₃ ↔ (b₂, a₃), r₃₁ ↔ (b₃, a₁);
- box (1,2) ↔ (b₁, a₃); the other boxes cyclically.

They are no longer the same pairs, which is why Lemma P1.1's argument does not close.

**4.2 Consistency (NUMERICS).** Take (NS) at all corners, b_k = κ+1 − 1/a_{k+1}, and a_k ≡ a ∈ (1/κ, 1). Then
b = κ+1 − 1/a > a, since 1/κ ∈ (x₋, x₊). Arcs were placed at the log-centre of each middle region, with ρ_b/ρ_a = b/a.
`split_facets.py` runs the semi-exact box search over all ordered pairs, all facet pairs and 600 edge priors, with the
arc gambles excluded or given the chord normal:

| ε | a | b | best log-margin |
|---|---|---|---|
| 0.1 | 0.81, 0.88, 0.94 | 1.10, 1.19, 1.27 | −0.42, −0.26, −0.13 |
| 0.3 | 0.58, 0.72, 0.86 | 1.56, 1.89, 2.12 | −0.76, −0.55, −0.25 |
| 0.6 | 0.39, 0.59, 0.80 | 3.91, 4.81, 5.24 | −1.34, −0.71, −0.32 |
| 0.9 | 0.28, 0.52, 0.76 | 25.4, 27.1, 27.7 | −1.47, −0.79, −0.37 |

The unsplit control x_± gives +0.83 … +1.95. **So corner equations plus box admit split solutions.** The algebra at p*
does not exclude atom chords through p* in the middle regions. (Only s is gridded, and the binding certificates sit at
the vertices; the margins are far from 0.)

**4.3 Necessary structure of a split configuration (PROVED, unconditional).** Let p* ∈ E(ψ), T1 a face model at p*,
and K any coherent face model, for example a directional limit B_{p*} ∪ (Z_{p*} ∩ {δ·c > 0}).

(a) On each facet, τ ↦ P_K(h(τ)) is concave. So O⁺_k(K) := {h ∈ relint F_k : P_K(h) > 0} is an interval, and
O⁻_k(K) := {P_K < 0} is a union of at most two end-intervals, each containing a corner.
- Gambles just outside D_{T1} near O⁺ lie in Z_{p*}, and so do gambles just inside near O⁻, since
  D_K △ D_{T1} ⊆ Z_{p*}.
- Hence tie gambles *inside* D_{T1} near a point h of a facet's middle region occur only together with tie gambles
  inside along a whole end-interval from h to a corner. That end-interval passes through a crossing, so two patterns
  and at least two atoms through p* are involved.
- So an isolated mid-facet arc consists of tie gambles **outside** cl D_{T1}. It needs a face model K with
  O⁺_k(K) ⊇ arc, hence v_k ∉ K.

(b) If K ⊊ T1 (D_K ⊋ D_{T1}), then K misses some v_k. Every h ∈ relint F_k then has P_K(h) > 0 (h·m > 0 on
T1 ∖ {v_k}). So Z_{p*} accumulates at every point of relint F_k from outside, with all three patterns of F_k (Prop 4.3's
argument).

(c) *Corollary.* Suppose the split configuration of 4.2 is realised with tie gambles only near the three mid-arcs. Then
T1 ≠ B_{p*}.
- If T1 = B_{p*}, every directional limit satisfies K_θ ⊆ T1.
- K_θ ≠ T1 for every θ: the three chord normals are the pivot normals of the three middle regions, which positively
  span the plane, so no direction rejects all three atoms.
- So each K_θ misses a vertex, and by (b) there are tie gambles along a whole facet, contradicting "only near the
  mid-arcs".

  Hence T1 is intermediate in a 2-dimensional face, its profile interior to the zonoid Σ_k[0, −∫_{G_k}c], with S ≠ ∅.
  By (a), its inside tie gambles run from the middle to corners, so the configuration must combine split facets with
  corner-to-crossing tie regions. The facet-data algebra for that combination is again feasible: the split solution
  satisfies the corner inequalities as equalities. So nothing local closes it.

---

## 5. What a construction must supply, and what an obstruction must show

**5.1 The construction problem (CFJ), precisely.** Find a measurable c : U → ℝ³ with:
- strict signs;
- B_q coherent for q ∉ E, where E is a countable union of atom chords and the atoms are as in Estructure(b);
- T1 = B_u ∪ S for some S ⊆ Z_u.

By §4, u must be a crossing of at least three chords, with split facet data. Then find preorders ⪯_i (strictly
monotone, cancellative qualitative probabilities on error sets: N9.4) such that each ψ_i endorses the relevant
comparisons, together with a selection C_p ∋ T1 with closed sections for every model. The ordinal part must:
- (i) dominate every incoherent model of the 2-dim face at u by a selected coherent model of equal ψ-profile, under
  (E_ψ) (Prop Epsi(a),(d)). This requires coherent face models B_u ∪ S realising a.e. profile of the 2-dim zonoid.
  Prop Epsi(d) (ideal tie-breaking) then forbids j-improvable selected realisers at area-a.e. profile;
- (ii) do the same along every other chord, with undominated splits independent of the point of the chord
  (Prop Epsi(e));
- (iii) avoid the N26 mechanisms: N26.5 (no 2-dim faces) and N26.7 use, per the N26 referee, (1) undominated ⇒ weakly
  ψ-Pareto, (2) R2 Thm 7, (3) the multiplier of an additive secondary, (4) the splice being a pointwise Lagrangian
  minimiser. A non-lexicographic ⪯_i must break (3)–(4). Within each ψ-fibre of the face, the comparison of a selected
  set with a competitor must not be a fixed-multiplier threshold rule shared by all three worlds. Otherwise the N26.4
  splice reappears.

None of (i)–(iii) can be checked before c exists. The exact consistency test (Thm closure) needs the family C_p and its
sections A_i(X), which depend on c.

**5.2 What remains open, and what an obstruction would have to show.**
- (O1) **(HC) in sectors.** Prove that the §4 chain runs in each sector at p* cut by atom chords: pivot lines through
  p*, linear pieces, crossing rows. Then Thm P1.4 becomes unconditional for corner atoms. The missing steps are PL2/nopin
  and continuity of pivot normals across sector boundaries, now with Lemma P1.2 available.
- (O2) **Split facets.** Exclude, or realise globally, the configuration of §4. An obstruction must use something
  beyond the facet data at p*, e.g.:
  - the global continuation of the mid-facet chords to the edges. Each chord's atom must be a shell D_{K⁺_t} ∖ D_{K⁻_t}
    at every point t of the chord (Estructure(e)), and K_t ⊇ K′ throughout;
  - a three-world multiplier argument for general (IB) preorders on the 2-dim face, generalising N26.5.
- (O3) **R-b′ (p* ∉ E).** Chords that cut PL2's set can let a vertex be pinned on a region accumulating at p*, bounded
  by chords. Lemma P1.2 shows that this, and evaluation at p*, are the only two places where chords enter the chain.

---

## 6. Status

| Claim | Status | Where |
|---|---|---|
| On M_U, I1/I2/C2 reduce to the §4 chain through facet data at p* | CHECKED | §1.1 |
| Straight levels for K♭ at every interior weighting, any field with (γ) | PROVED | Lemma P1.2 |
| Corner inequalities + box products infeasible | PROVED | Lemma P1.1 |
| Box bounds 1/κ ≤ x_k x_{k+1} ≤ κ (lower ones via the mirror certificate) | CHECKED / NUMERICS | §3.1 |
| Corner atom ⇒ strict inequality x_k + 1/x_{k+1} > κ+1 | PROVED from (HC) | Lemma P1.3 |
| No cover with only corner atoms through p* (incl. all of R-a′(i)) | PROVED from (HC) | Thm P1.4 |
| (HC) itself with chords through p* | CONJECTURE | §3.2, (O1) |
| Single corner atom: both overlap branches box-certified, ε ∈ [0.02, 0.99] | NUMERICS | §3.2 |
| Split facet data with (NS) at all corners is box-consistent | NUMERICS | §4.2 |
| Concavity/pattern constraints; split ⇒ T1 intermediate in a 2-dim face | PROVED | §4.3 |
| Global ψ, ordinal tie-breaking, closed sections | not achieved | §5 |

Scripts (NUMERICS only; no proof depends on them):
- `box_relax.py`: grid box search;
- `box_exact.py`: semi-exact box search;
- `relax_scan*.py`, `lower_branch.py`: corner-relaxed families;
- `relax_point.py`: the point (κ, 1, 1/κ);
- `multi_atoms.py`: atoms at several corners;
- `box_formula.py`: identification of the binding box bounds;
- `split_facets.py`: split facets;
- `overlap_sympy.py`: symbolic checks.
