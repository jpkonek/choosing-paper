# L2. A non-localizable blind set in a full system: Conjecture K3.C is false

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up or
refereed notes mark proved, each named), **CHECKED**, **CONJECTURE**, **NUMERICS** (scripts in `l2py/`, run with
`python3 -I` from inside `l2py/`; no proof depends on them). No assumption is added. Setting and notation: D2 §§1–3
(two worlds, chain coordinate x, path C_b, c_b, d_b, λ, N₊, D(δ), τ_f), K3 §1 (𝔚, 𝒩, 𝒩(𝔊), localizing families,
Λ, Λ_D, Λ_∞, (S), (S_int), ratio certificates). As the K3 referee asked, K3's class "(S)" is written **(Loc)** below
(and (S_int) is **(Loc_int)**), so that "(S)" always means the axiom "closed competitive choice".

---

## 0. Outcome

**Q_K3 has answer YES, and Conjecture K3.C is FALSE (PROVED).** There is a two-world full system on M_U, next to an
additive world, in which world 1 has a non-null **non-localizable** blind set:

- **Theorem L2.1.** For every K′ = [α′, β′] ⊆ (0,1) and every a ∈ (0,1) there is a ranking (⪯₁, ⪯₂) on M_U with
  strict (G), (IB), (LA), (S) (the C2.1 path as selection, competitiveness on supp p, closed sections for **every**
  evaluable model at both worlds), (C), C_L = {C_b : b ∈ [0,1]}, and (LF) at every interior C_b. World 2 is additive
  with density 1 (w.r.t. λ).
- **Theorem L2.4 (blindness).** For **every** localizing family D, every ν ∈ 𝒩(𝔚_D) (every bounded endorser of the
  D-localized relevant world-1 comparisons, purely finitely additive part included) has ν(c_a) = 0. The bounded
  countably additive charge λ|_{d_a} endorses **all** relevant comparisons. Hence
  Λ = Λ_D = Λ_∞ = c_a = E₁(C_a) for every D, so a_∞ = a > 0 (K3.8), and world 1 is not (Loc_int).
- So the strong classification "every world that does not add up is (M1) or (Loc_int)" is **false** in a full system
  (K3.1(e), K3 referee §5.3), already in two worlds next to an additive world. The blind set has the rigid shape of
  K3.7(β′) on the edge: it is the world-1 error set of a selected coherent model between P₁ and P₂.

**The mechanism (§6).** D2's generators, with two changes.
1. Each level of the design is **finite** and lives on finitely many **blocks** B_k of the chain that accumulate at
   x = 1 geometrically, so every certificate of a given quality avoids a whole neighbourhood of the end. End
   localization therefore cannot kill it, and targets defined by "most of each block" can be moved off any small
   set; so no localization can kill it.
2. Sums of two generators of the same level are blocked by **geometry**, not by D2's near-one clause: their targets
   share a block (lines of a projective plane meet), each fills 4/5 of it, and everything to the right of that
   block has measure less than twice the shared part, so no rightward transport can separate them. The base cone is
   plain tail dominance.

Closed sections then follow from compactness of the space of "one generator per level" selectors (Lemma L2.3); no
finiteness condition like D2's (D3) is needed.

**What it does not give (§5, PROVED).** World 1 is (Loc) with a σ-finite endorser and **no** localization at all
(Prop. L2.5): ρ = φ∘x, φ nondecreasing, finite on [0,1), ∫^1 φ = ∞. So the example lies in (Loc) ∖ (Loc_int). This
realizes the K3 referee's §1.4 observation that (N) ⊊ {Λ_∞ non-null}, but it is **not** in (N). For T1 this
matters: by H1.2 (as used in K3.7's first sentence), a world of class (Loc) can never be the exceptional world of a
cover of T1 next to two integrable worlds. So the aimed version of Q_K3 is **"Yes, but without (Loc)"**, which
remains open (§7).

**Three worlds (§7): not constructed.** I give the exact list of what a lift must verify, the one place where the
two-world blocking argument does not transfer (forced world-1 trades out of the end into the "tie wedges" of R₂₃),
and the scaling under which those leaks are smaller than the blocks. No three-world full system is claimed.

| | Statement | Label |
|---|---|---|
| L2.2 | the world-1 acceptance set gives a preorder with strict (G), (IB); same-level generator sums are blocked | PROVED; NUMERICS |
| L2.3 | closed world-1 sections for every model (compactness of selectors) | PROVED; NUMERICS |
| L2.1 | full two-world system: (G), (IB), (LA), (S), (C), C_L = path, (LF) | PROVED; NUMERICS |
| L2.4 | ν(c_a) = 0 for every bounded D-localized endorser and every D; Λ = Λ_∞ = c_a; K3.C false; Q_K3 "Yes" | PROVED; NUMERICS |
| L2.5 | world 1 is (Loc) with a σ-finite endorser, D = ∅; not in (N) | PROVED; NUMERICS |
| L2.6 | consequences: the strong classification fails; for T1 the mechanism is excluded next to integrable partners | PROVED (from H1.2, K3.7) |
| L2.C | next to an additive world, (N) = ∅ (every non-(M1) world is (Loc)) | CONJECTURE |
| §7 | three-world lift: requirements, the wedge leak, scaling | analysis (no label claimed beyond CHECKED where marked) |

---

## 1. Setting (D2 §1)

- n = 2, K′ = [α′, β′] ⊆ (0,1), U = D_{K′}, M_U, M the mixed part of U, N₊ its nonnegative part, λ := μ/μ(M),
  n₊ := λ(N₊).
- The C2.1 path C_b, b ∈ [0,1], reindexed so that c_b := E₁C_b ∩ M = {x < b} (mod null) for the chain coordinate x,
  which pushes λ|_M to Lebesgue measure on [0,1). C₀ = P₁, C₁ = P₂, E₂C_b = d_b := M ∖ c_b. Selection p ↦ C_{p₂}.
- A model X is determined by E₁X = A ∪ N_X, with A := E₁X ∩ M and N_X := N₊ ∖ X. X is regular iff N_X is null.
- For f ∈ L¹(M) and t ∈ [0,1]: τ_f(t) := ∫_{M∩{x≥t}} f dλ. For a ternary δ on U: D(δ) := ∫_{N₊} δ dλ.
- For a cut b and a model X put P := c_b ∖ A, Q := A ∖ c_b. Then C_b ⪯₂ X iff λ(Q) ≤ λ(P) + λ(N_X), and the world-1
  vector of C_b ⪯₁ X is δ_b := 1_{A∪N_X} − 1_{c_b}, whose restriction to M is 1_A − 1_{c_b} = 1_Q − 1_P.

## 2. The design and world 1

**Blocks.** Fix a ∈ (0,1) and u₀ ∈ (a, 1). Put r_k := (1 − u₀)5^{−k} and u_k := 1 − r_k (k ≥ 0), and
- B_k := M ∩ {u_k ≤ x < u_{k+1}}, so λ(B_k) = (4/5)r_k;
- ref_k := M ∩ {u_k ≤ x < u_k + (4/5)λ(B_k)}, the left 4/5 of B_k, λ(ref_k) = (16/25)r_k;
- F_k := B_k ∖ ref_k (the free right part), λ(F_k) = (4/25)r_k.

The one quantitative fact used about blocks is the **blocking inequality**

  λ(M ∩ {x ≥ u_k}) − 2λ(ref_k) = r_k − (32/25)r_k < 0.                                   (B)

**Levels.** For n ≥ 1 let K_n := 2^n, q_n a prime ≥ 4^n, Π_n := q_n² + q_n + 1, L_n := ⌊Π_n/K_n⌋. Choose disjoint
finite sets I_n of consecutive block indices, I_n to the right of I_{n−1}, |I_n| = Π_n, identified with the points of
PG(2, q_n); unused "gap" blocks between consecutive I_n are allowed (they are used only in Prop. L2.5). Fix an
injective assignment (i, l) ↦ line ℓ_{n,i,l} of PG(2,q_n) (i < K_n, l < L_n); it exists since K_nL_n ≤ Π_n.

**Generators.** P_{n,i} := M ∩ {ia/K_n ≤ x < (i+1)a/K_n}; Q_{n,i,l} := ⋃_{k∈ℓ_{n,i,l}} ref_k;
g_{n,i,l} := 1_{Q_{n,i,l}} − 1_{P_{n,i}}. 𝒢_n is the finite set of level-n generators. Facts used:
- (G1) P ⊆ c_a, Q ⊆ M ∩ {x ≥ u₀} ⊆ d_a; ‖g‖₁ ≤ a2^{−n} + r_{min I_n} for g ∈ 𝒢_n, summable in n.
- (G2) any two level-n targets (equal or not) contain a common ref_k, k ∈ I_n (two lines of a projective plane meet).
- (G3) every k ∈ I_n lies on exactly q_n + 1 lines, so at most q_n + 1 level-n targets contain ref_k.

**Selectors.** A selector is F = (F(n))_{n≥1} with F(n) ∈ 𝒢_n ∪ {⊥}; 𝔉 := ∏_n(𝒢_n ∪ {⊥}), compact metrizable in the
product of discrete topologies. g_F := Σ_{n : F(n) ≠ ⊥} g_{F(n)} converges in L¹(M) by (G1). On d_a, g_F ∈ {0, 1}
(targets of different levels are disjoint) and g_F = 1 on every ref_k with k on the line of some F(n).

**Base cone.** T := {f ∈ L¹(M) : τ_f(t) ≥ 0 for all t ∈ [0,1]}: a convex cone, closed in L¹ (each τ_f(t) is a
continuous linear functional), containing every f ≥ 0.

**World 1.** For a ternary δ on U:
- **R⁻:** D(δ) < 0 ⇒ reject;
- **R⁺:** D(δ) > 0 ⇒ accept;
- **R⁰:** D(δ) = 0 ⇒ accept iff δ = 0 a.e. on N₊ and δ|_M ∈ 𝒜 := ⋃_{F∈𝔉} (g_F + T).

X ⪯₁ Y :⟺ 1_{E₁Y} − 1_{E₁X} is accepted. **World 2:** X ⪯₂ Y :⟺ λ(E₂X) ≤ λ(E₂Y).

In words: world 1 ranks first by unanimous-problem errors; among models with equal such errors it accepts
rightward transport of errors along the chain (tail dominance), plus at most one generator trade per level, each
trading a thin strip of c_a for "most of" a projective-plane line of blocks. (R⁺ is the simplest closure of the
kind D2 §3 calls R⁺; it touches no relevant comparison.)

## 3. Every axiom

**Lemma L2.2 (PROVED).** The acceptance set contains every δ ≥ 0, no nonzero δ ≤ 0, and δ₁ + δ₂ whenever δ₁, δ₂ are
accepted and δ₁ + δ₂ is ternary. Hence (Lemma vectorform) ⪯₁ is a preorder on M_U with strict (G) and (IB). World 2
is additive with density, so it has strict (G) and (IB).

*Proof.*
- *δ ≥ 0.* D(δ) ≥ 0. If D(δ) > 0, R⁺. If D(δ) = 0 then δ = 0 on N₊, and δ|_M ∈ T = g_∅ + T (F ≡ ⊥).
- *δ ≤ 0, δ ≠ 0.* D(δ) ≤ 0; R⁻ rejects if D(δ) < 0. Let D(δ) = 0, so δ = 0 on N₊ and δ|_M ≤ 0 is nonzero. Suppose
  δ|_M = g_F + f with f ∈ T.
  - If F ≡ ⊥: τ_f(0) = ∫δ dλ < 0, a contradiction.
  - Otherwise pick n with F(n) ≠ ⊥ and k on its line. On M ∩ {x ≥ u_k} ⊆ d_a: δ ≤ 0 and g_F ≥ 0, so f ≤ 0 there, and
    f ≤ −1 on ref_k. Hence τ_f(u_k) ≤ −λ(ref_k) < 0, a contradiction.
- *Sums.* Let σ := δ₁ + δ₂ be ternary, δ₁, δ₂ accepted. D(σ) = D(δ₁) + D(δ₂) with both ≥ 0.
  - If D(σ) > 0: accepted by R⁺.
  - If D(σ) = 0: D(δ₁) = D(δ₂) = 0, both vanish on N₊, so σ does. Write δ_j|_M = g_{F_j} + f_j.
    - If no n has F₁(n) ≠ ⊥ ≠ F₂(n): F := F₁ ∪ F₂ is a selector, g_{F₁} + g_{F₂} = g_F, and
      σ|_M = g_F + (f₁ + f₂) ∈ 𝒜.
    - Otherwise some n has F₁(n), F₂(n) ∈ 𝒢_n (possibly equal). By (G2) both targets contain ref_k for some
      k ∈ I_n. Put f := f₁ + f₂ = σ − g_{F₁} − g_{F₂} ∈ T. On ref_k, g_{F₁} = g_{F₂} = 1, so f ≤ 1 − 2 = −1. On
      M ∩ {x ≥ u_k} ∖ ref_k, g_{F₁}, g_{F₂} ≥ 0, so f ≤ 1. Hence
      τ_f(u_k) ≤ λ(M ∩ {x ≥ u_k}) − 2λ(ref_k) < 0 by (B), a contradiction. So this case does not occur. ∎

**Lemma L2.3 (closed world-1 sections, every model; PROVED).** For every model X, S₁(X) := {b ∈ [0,1] : C_b ⪯₁ X} is
closed.

*Proof.*
- If N_X is non-null, D(δ_b) = λ(N_X) > 0 for every b, so S₁(X) = [0,1].
- Let X be regular, A := E₁X ∩ M. Then D(δ_b) = 0, δ_b = 0 on N₊, and δ_b|_M = 1_A − 1_{c_b}. So
  b ∈ S₁(X) iff 1_A − 1_{c_b} − g_F ∈ T for some F ∈ 𝔉.
- Let b_j ∈ S₁(X), b_j → β, with selectors F_j. By compactness of 𝔉 pass to a subsequence with F_j → F pointwise
  (each coordinate eventually constant). Then ‖g_{F_j} − g_F‖₁ ≤ Σ_{n : F_j(n) ≠ F(n)} 2(a2^{−n} + r_{min I_n}) → 0 by
  dominated convergence, and ‖1_{c_{b_j}} − 1_{c_β}‖₁ = |b_j − β| → 0. T is closed in L¹, so
  1_A − 1_{c_β} − g_F ∈ T and β ∈ S₁(X). ∎

*Remark (shape of the sections, PROVED as in D2.4).* For each F, S_F := {b : 1_A − 1_{c_b} − g_F ∈ T} is an initial
segment: if b ∈ S_F and b′ < b, the tail condition at t ∈ [b′, b) follows from the one at t for b, as in D2.4(ii)
step 3. So S₁(X) = [0, max_F β_F] with the max attained; it contains [0, λ(A)] (F ≡ ⊥, D2.4(ii) step 2).

**Theorem L2.1 (PROVED).** The ranking of §2 with selection p ↦ C_{p₂} satisfies strict (G), (IB), (LA), (S)
(competitiveness on supp p and closed sections for every model at both worlds), (C), C_L = {C_b : b ∈ [0,1]}, and
(LF) at every interior C_b.

*Proof.* Fix a model X (A, N_X) and a cut b; P, Q as in §1.
1. **(G), (IB):** Lemma L2.2.
2. **Competitiveness ((K) for every model).** Vertices: C₀ = P₁ ⪯₁ X and C₁ = P₂ ⪯₂ X by (G). Interior b: suppose
   C_b ⋠₂ X, i.e. λ(Q) > λ(P) + λ(N_X). If N_X is non-null, R⁺ accepts δ_b. If N_X is null, f := 1_Q − 1_P has
   τ_f(t) = λ(Q ∩ {x ≥ t}) ≥ 0 for t ≥ b and τ_f(t) ≥ λ(Q) − λ(P) > 0 for t < b, so f ∈ T and C_b ⪯₁ X.
3. **Closed sections.** World 2: S₂(X) = {b : λ(A ∩ d_b) ≤ λ(c_b ∖ A) + λ(N_X)}, closed by continuity in b. World 1:
   Lemma L2.3. p ↦ p₂ is continuous, so the sections in p are closed. With 2 this is (S).
4. **No weak domination of C_b.** Suppose X ⪯₁ C_b and X ⪯₂ C_b, i.e. δ′ := 1_P − 1_{Q∪N_X} is accepted and
   λ(P) + λ(N_X) ≤ λ(Q).
   - D(δ′) = −λ(N_X), so R⁻ forces N_X null. Then δ′|_M = 1_P − 1_Q = g_F + f, f ∈ T.
   - If b ≥ a: on M ∩ {x ≥ b} ⊆ d_a, g_F ≥ 0 and δ′ = −1_Q, so τ_f(b) ≤ −λ(Q); hence Q is null, and then λ(P) ≤ 0.
   - If b < a and F ≢ ⊥: on M ∩ {x ≥ u_k} (k on the line of some F(n)) δ′ ≤ 0 and g_F ≥ 0, with g_F = 1 on ref_k,
     so τ_f(u_k) ≤ −λ(ref_k) < 0: impossible. If b < a and F ≡ ⊥: τ_f(b) = −λ(Q), so Q and then P are null.
   - So X = C_b.
5. **C_L, (C), (LA).** By 4 every C_b is undominated and is the only model tied with C_b at both worlds. C_b is
   coherent, so C_b ∈ C_L, (LA) holds, and with 2–3, (S) holds. Theorem kkm (which needs (LA) and (S)) ties every
   undominated model at every world with some C_b, which by 4 equals it. So U_L = C_L = {C_b}, and (C) holds.
6. **(LF)** at interior C_b: C2.1(4) (as in D2.1 step 6). ∎

NUMERICS (`l2py/l2_check.py`, `.out`; exact rationals; levels n = 1, 2 with PG(2,2), PG(2,3); 20 blocks, 93 cells,
91 selectors): blocking inequality 20/20; all 180 same-level generator pairs share a block and their sum is
infeasible; 300/300 nonzero δ ≤ 0 rejected; 100/100 δ ≥ 0 accepted; (K) 25/25 and (U) 25/25 on random cut pairs;
566/566 ternary sums of accepted vectors accepted; grid sections are initial segments containing [0, λ(A)] (60/60).

---

## 4. Blindness: Λ_∞ = c_a

**Theorem L2.4 (PROVED).** In the system of Theorem L2.1:
- **(a)** for every localizing family D and every ν ∈ 𝒩(𝔚_D) (ν ∈ ba(M), ν ≥ 0, ν(M) = 1, vanishing on null sets,
  ν(δ) ≥ 0 for every D-localized relevant world-1 comparison δ), ν(c_a) = 0;
- **(b)** ν₀ := λ|_{d_a}/(1 − a) is a countably additive member of 𝒩 (it endorses every relevant comparison);
- **(c)** consequently (NC_𝔚) holds, Λ = Λ_D = Λ_∞ = c_a for every D (mod null), a_∞ = a, world 1 is in mode (M2),
  and world 1 is not (Loc_int). Conjecture K3.C is false, and Q_K3 has answer "Yes".

*Proof.*
- **(a) Flexible generators.** Fix D, n, and m so large that λ(D_m ∩ B_k) ≤ λ(F_k)/2 for the finitely many k ∈ I_n
  (possible since λ(D_m) → 0). For k ∈ I_n put Z_k := ref_k ∩ D_m and choose R_k ⊆ F_k ∖ D_m with λ(R_k) = λ(Z_k)
  (λ(F_k ∖ D_m) ≥ λ(F_k)/2 ≥ λ(D_m ∩ B_k) ≥ λ(Z_k)). Then f_k := 1_{R_k} − 1_{Z_k} ∈ T: R_k lies entirely to the
  right of Z_k, so τ_{f_k}(t) is λ(R_k) − λ(Z_k ∩ {x ≥ t}) ≥ 0 or λ(R_k ∩ {x ≥ t}) ≥ 0.
- For g = g_{n,i,l} with line ℓ put Q′ := (Q ∖ D_m) ∪ ⋃_{k∈ℓ} R_k and δ′ := 1_{Q′} − 1_{P_{n,i}} = g + Σ_{k∈ℓ} f_k.
  - δ′ ∈ g + T, with the selector F(n) = g and F ≡ ⊥ elsewhere; so it is accepted.
  - It is the relevant comparison C_a ⪯₁ X′ with X′ regular, E₁X′ ∩ M = (c_a ∖ P_{n,i}) ∪ Q′ (a cut pair at a).
  - It is D-localized: δ′⁺ = Q′ misses D_m.
- **Certificate.** h_n := Σ_{i<K_n} Σ_{l<L_n} L_n^{−1} δ′_{n,i,l} = Σ L_n^{−1} 1_{Q′_{n,i,l}} − 1_{c_a}. On B_k, every
  Q′ whose line contains k equals (ref_k ∖ D_m) ∪ R_k, and by (G3) at most q_n + 1 lines contain k. So
  h_n ≤ ε_n − 1_{c_a} with ε_n := (q_n + 1)/L_n.
- ε_n → 0: L_n ≥ Π_n/2^n − 1 ≥ q_n²/2^{n+1} (for n ≥ 1), so ε_n ≤ 2^{n+1}(q_n+1)/q_n² ≤ 2^{n+2}/q_n ≤ 4·2^{−n}.
- For ν ∈ 𝒩(𝔚_D): 0 ≤ ν(h_n) ≤ ε_n − ν(c_a), so ν(c_a) ≤ ε_n for every n, and ν(c_a) = 0.
- In K3.1(f) form: for non-null B′ ⊆ c_a, h_n/λ(B′) ≤ ε_n/λ(B′) − 1_{B′}/λ(B′), a c-ratio certificate on B′ with
  uniform density g = 1_{B′}/λ(B′) and c = ε_n/λ(B′) → 0. (So the concentration of g that the K3 referee's §8
  identifies as the gap in the F1.4 argument is not even needed.)
- **(b)** Let δ be an accepted relevant comparison. It is regular, so D(δ) = 0 and δ|_M = g_F + f, f ∈ T. Then
  ∫_{d_a} δ dλ = τ_δ(a) = τ_f(a) + τ_{g_F}(a) = τ_f(a) + Σ_n λ(Q_{F(n)}) ≥ 0 (sources lie in c_a; the series converges
  in L¹). So ν₀(δ) ≥ 0.
- **(c)** ν₀ ∈ 𝒩 gives (NC_𝔚) (K3.1(a)), so K3.1(c)–(d) apply (K3 referee §1.3). ρ_{ν₀} > 0 on d_a gives Λ ⊆ c_a;
  (a) gives c_a ⊆ Λ_D for every D. With Λ_D ⊆ Λ (K3.1(d)): Λ_D = Λ = c_a for every D, hence Λ_∞ = c_a. K3.8 then
  reads a_∞ = a, and K3.1(e) says world 1 is not (Loc_int). Mode (M2): the selection is nested, so (NC⁺) holds on 𝔚
  (N17 Lemma 3.1, as in K3.3(b)), and there is no finite certificate; world 1 does not add up since Λ is
  non-null (K3.1(c)). ∎

*Reading.*
- Λ_∞ = c_a = E₁(C_a), the world-1 error set of a selected coherent model C_a = D_{[α′a′, β′+(1−β′)a′]} on the path
  from P₁ to P₂ (a′ the C2.1 parameter of C_a). This is exactly the shape K3.7(β′) requires on an edge region (a
  coherent model between P₁ and P_j).
- Strict (G) holds everywhere, in particular on Λ: every enlargement of a world-1 error set inside c_a is strictly
  worse. Yet no bounded endorser, of any localized family of comparisons, charges c_a; the purely finitely additive
  parts vanish there too.
- **Consistency with F1.4.** F1.4 bounds the target cost of a certificate with sources and targets in c_{b₀} below by
  θ(S, b₀), and θ(S, b₀) ≤ λ(d_{b₀})/8 → 0 as b₀ → 1. The level-n certificate has b₀ = u_{max I_n + 1} → 1 and target
  cost Γ_n ≥ K_n·λ(ref_{max I_n}) ≥ λ(d_{b₀}); no contradiction. Exporting its targets into d_{b₀} is exactly what (B)
  forbids.
- **Consistency with Q15 and (QC₁).** These hold automatically, since every axiom holds. Directly: same-level targets
  meet, so there is no star certificate; and if c_a ≤₁ A with A ⊆ d_a, then τ_f(0) ≥ 0 for f = 1_A − 1_{c_a} − g_F gives
  λ(A) ≥ a(1 − Σ_{n : F(n)≠⊥} 2^{−n}) + Σ_n λ(Q_{F(n)}) ≥ min(a/2, min_{g∈𝒢₁} λ(Q_g)) > 0.

NUMERICS (`l2py/l2_check.py`): every generator comparison accepted (18/18); for 40 random sets D inside the blocks,
the modified generators are accepted and the certificate multiplicity is ≤ (q+1)/L (40/40); λ|_{d_a} endorses
1200/1200 sampled accepted relevant vectors.

---

## 5. The example is (Loc), with a σ-finite endorser

**Proposition L2.5 (PROVED).** Choose the gap blocks (§2) so that, with C_n := a2^{−n}/(q_n + 1) and
G_n := number of gap blocks between I_n and I_{n+1} (and G₀ before I₁),
5^{G_n+1}(q_n + 1) ≥ 2(q_{n+1} + 1) and C₁/λ(ref_{min I₁}) ≥ 1. Define φ: [0,1) → (0,∞) by φ := 1 on [0, u_{min I₁}),
φ := C_n/λ(ref_k) on the x-range of B_k for k ∈ I_n, and φ constant on each run of gap blocks, equal to its value on
the preceding block. Then φ is nondecreasing and finite, ∫^1 φ = ∞, and ρ := φ∘x on M (ρ := 1 on N₊) endorses every
relevant world-1 comparison in the cancellation reading (E2): ρ(δ⁻) ≤ ρ(δ⁺) in [0, ∞]. So world 1 is (Loc) with the
trivial localizing family D_m = ∅ and a σ-finite density; it is not in (N).

*Proof.*
- *Monotone.* Within I_n, λ(ref_k) decreases with k. From the last block of I_n to the first of I_{n+1} the ratio of
  λ(ref) is 5^{−(G_n+1)}, so φ jumps by the factor 5^{G_n+1}C_{n+1}/C_n = 5^{G_n+1}(q_n+1)/(2(q_{n+1}+1)) ≥ 1. The
  first step is ≥ 1 by the choice of C₁.
- *Non-integrable.* ∫ over level-n blocks = Σ_{k∈I_n} C_n λ(B_k)/λ(ref_k) = (5/4)Π_nC_n ≥ a2^{−n}q_n/2 ≥ a2^{n−1}.
- *Generators are ρ-neutral.* ρ(Q_{n,i,l}) = Σ_{k∈ℓ} C_n = (q_n+1)C_n = a2^{−n} = ρ(P_{n,i}).
- *Endorsement.* Let δ be an accepted relevant comparison, δ|_M = g_F + f, f ∈ T, δ = 0 on N₊. If ρ(δ⁺) = ∞ there
  is nothing to prove; assume ρ(δ⁺) < ∞.
  - For φ_N := min(φ, N) (N ≥ 1; bounded, nondecreasing) and any h ∈ L¹(M), Stieltjes integration by parts gives
    ∫φ_N h dλ = φ_N(0)τ_h(0) + ∫_{(0,1)} τ_h dφ_N.
  - For t ≥ a, τ_δ(t) = τ_f(t) + τ_{g_F}(t) ≥ 0, since g_F ≥ 0 on d_a. Applying the identity on d_a (φ_N 1_{d_a})
    gives ∫_{d_a} φ_N δ ≥ 0, so ∫_{d_a} φ_N δ⁻ ≤ ρ(δ⁺); letting N → ∞, ρ(δ⁻ ∩ d_a) ≤ ρ(δ⁺) < ∞. On c_a, ρ = 1. So
    ∫ρ|δ| < ∞.
  - On all of M: ∫φ_N δ = φ_N(0)τ_δ(0) + ∫τ_δ dφ_N ≥ φ_N(0)τ_{g_F}(0) + ∫τ_{g_F} dφ_N = ∫φ_N g_F = Σ_n ∫φ_N g_{F(n)}
    (τ_f ≥ 0, dφ_N ≥ 0; the last step by L¹ convergence and boundedness of φ_N).
  - Each term satisfies ∫φ_N g_{F(n)} ≥ −a2^{−n} and → ρ(Q_{F(n)}) − ρ(P_{F(n)}) = 0 as N → ∞. By dominated
    convergence over n, Σ_n ∫φ_N g_{F(n)} → 0; and ∫φ_N δ → ∫ρδ by dominated convergence (ρ|δ| integrable). So
    ∫ρδ ≥ 0, i.e. ρ(δ⁻) ≤ ρ(δ⁺).
- ρ > 0 and finite everywhere on M, so this is (Loc) with D ≡ ∅. ∎

NUMERICS (`l2py/l2_check.py`, the cell model with the same recipe): ρ(Q_g) ≥ ρ(P_g) for 18/18 generators; ρ endorses
1200/1200 sampled accepted relevant vectors.

**Corollary L2.6 (PROVED).**
- **(a)** The strong classification of K3 (every world that does not add up is (M1) or (Loc_int); equivalently
  Q_K3 "No") is false in a full system, already with n = 2 and an additive neighbour.
- **(b)** The weak classification ((N) = ∅) is not touched: the example is (Loc).
- **(c) For T1.** Under (H_U), next to two worlds with integrable densities endorsing all their relevant comparisons,
  a world of class (Loc) is impossible (H1.2; this is the "(S) is excluded by H1.2" step of K3.7's first sentence,
  for a.e.-finite ρ₁). So the mechanism of L2.1, which produces (Loc) worlds, cannot supply the exceptional world of
  K3.7. More generally, with every world (Loc) and compatible localizations it is excluded by K3.5′(c) unless there is
  sheltering or infinite minority mass. To be aimed at T1 next to integrable partners, a non-localizable blind set
  must come with ¬(Loc), i.e. world 1 must be in (N).

**CONJECTURE L2.C.** In the setting of F1.2/K3.8 (two worlds, world 2 additive with integrable density, every axiom),
every world that is not (M1) is (Loc) with a σ-finite endorser; i.e. (N) = ∅ there.
- *Evidence (heuristic, no label beyond this).* By F1.2-type monotonicity, a localized σ-finite endorser must be φ∘x
  with φ nondecreasing. Defeating every such φ needs accepted localized cut pairs (P, Q) with Q in a **fixed** c_t
  and λ(Q)/λ(P) → 0 at fixed positions. Their targets are inside c_t, where d_t has room 1 − t, so (B)-type blocking
  is impossible. Disjoint such pairs then sum, and by (K)-transport they export into d_t; summing enough of them gives
  a fixed fat set ≤₁ sets of vanishing measure, against Prop. Q15(a). What is missing is a proof that the sums can
  always be arranged to be fat (the pieces may shrink summably).

---

## 6. Why it works, and what D2/F1/K3 missed

- **Where localization bites.** K3.1(f): Λ_∞ ⊇ B needs, for **every** D, certificates from D-localized comparisons.
  A certificate is finite, so it is D-localized as soon as each of its finitely many comparisons is ≤ 0 on one
  D_m. D2's generators reach x = 1 (all scale blocks), so the end family kills them all at once. Here each level is a
  finite union of blocks inside some c_{t_n}, t_n < 1, so for every D the level-n certificate survives at a depth
  m(n, D). Flexibility ("4/5 of each block, any shape after rightward moves inside the block") handles every D, not
  just end families.
- **Why sums stay blocked without a near-one clause.** In two worlds next to an additive world, (K) forces the base to
  contain every strict rightward transport. D2 kept generator sums out by forbidding the base to move mass near
  x = 1. Here the base is all of T, and a sum is impossible for measure reasons alone: two same-level targets share
  ref_k, and the entire region to its right, ref_k included, has measure r_k < 2λ(ref_k) (inequality (B)).
  Transporting either copy out of ref_k needs more room than exists.
- **Why closedness is free.** D2 needed (D3) (finitely many generators with source ≥ η) to close a union of
  sections. Here a section is a union over the compact space 𝔉, and acceptance is an L¹-closed condition jointly in
  (b, F). Allowing countably many generators (one per level) is what makes 𝔉 compact and the union closed.
- **Relation to K3.4.** K3.4 localizes a pairwise-meeting family whose members have positive parts of measure
  tending to 0. It does not apply here: within a level the targets meet but have measure bounded below, and targets
  of different levels are disjoint. A localizing family can remove any finite set of levels, but only at depths that
  grow with the level, and the certificates of the remaining levels survive.

---

## 7. Three worlds

**Not constructed.** What follows is the exact state.

**7.1 What a lift must verify.** Take n = 3, ε, K′, U, M_U as in K3 §5, worlds 2, 3 additive with densities ρ₂, ρ₃,
a coherent selection p ↦ C_p, and world 1 = (base cone 𝓑) ∪ ⋃_F (g_F + 𝓑) with L2-type generators out of one
selected model C_{p₀} (sources in E₁(C_{p₀})) and targets in blocks. Then:
- (i) 𝓑 must contain every **forced** comparison: δ_{p,X} := 1_{E₁X} − 1_{E₁C_p} whenever X strictly beats C_p at
  every world of supp p ∖ {1} (competitiveness);
- (ii) blocking: no f ∈ 𝓑 with f ≤ −1 on a shared ref_k and f ≤ 1 elsewhere on the target side;
- (iii) strictness and (U) for g_F + 𝓑 (no forced chain may carry target mass back into the sources);
- (iv) closed world-1 sections at every C_p for every model, now in the 2-simplex;
- (v) (C), and C_L = the selection.

E1.3 places any blocks at a near-unanimous end: here the e₁ ray inside (+,−,−), where C_p errs only when p₁ is small.

**7.2 Where the two-world argument fails: wedge leaks (order-of-magnitude computation; no label claimed).** Take the
linear selection C_p = U ∩ {p·g > 0}, i.e. the Bayes models of any surrogate (h|g₁|, h|g₂|, h|g₃|) with a common
factor h > 0, and worlds 2, 3 additive with densities ρ_j = h|g_j|. For a block O at angular depth δ about the e₁ ray
(|g₂|, |g₃| ≤ δg₁), the models erring on O have p₁ ≲ δ.
- Besides moves deeper into the end (controlled by (B)-type geometry in the measure ρ₂, as in two worlds), such a C_p
  is world-1-sensitive on thin **tie wedges** {|p₂ρ₂σ₂ + p₃ρ₃σ₃| < p₁ρ₁} in R₂₃. Flipping a (+,−,+) piece and a
  (+,+,−) piece of these wedges gains at worlds 2 **and** 3, by at most p₁ρ₁ per unit.
- So (i) forces moves Z → R₁ ∪ R₂ from O into the wedges as soon as the joint gain exceeds the (2,3)-cost of Z. Over
  all directions p₂ : p₃ the wedges sweep all of R₂₃. The ρ₂-cost that can leave O this way is of order
  ρ₁(R₂₃)/r, where r := ρ₁/ρ₂ on O ≈ 1/δ.
- With h ≡ 1 this is ≈ δ, while ρ₂(O) ≈ δ³ (λ(O) ≈ δ²): the leak empties every deep block, and (ii) fails.
- With h large near the ray (for instance h ≈ (g₁/|(g₂, g₃)|)^{5/2} there, so that ρ₂(O_k) ≈ δ_k^{1/2} decreases
  geometrically and ρ₂ stays integrable), the leak capacity ≈ δ_k is ≪ ρ₂(O_k), and the deeper-room inequality
  ρ₂(deeper than O_k) < ρ₂(O_k)/2 can hold. This scaling is consistent with (ii); proving (ii) needs a separating
  endorser of the whole forced cone, i.e. an additive "shadow" for which every C_p is weakly Pareto. That is a
  realisation problem I did not solve.
- (iii)–(v) were not examined.

**7.3 Single open question (Q_L2).** On M_U with n = 3 and worlds 2, 3 additive, is there a coherent selection and a
non-null O near the e₁ ray in (+,−,−) such that the forced cone of world 1 contains no f with f ≤ −1 on O and
f ≤ 1 elsewhere? "Yes", with (iii)–(v), lifts L2.1/L2.4 to three worlds, with Λ ∩ R₁₂ = E₁(C₁₂) ∩ R₁₂ for a selected
edge model C₁₂. By L2.6(c), such a lift would still be (Loc). Aiming at T1 additionally needs ¬(Loc) (Conjecture L2.C
says this is impossible in two worlds next to an additive world).

---

## 8. Dependencies and files

**Used.**
- D2 §§1–3: setting, C2.1 path, D2.4(ii) steps 2–3 for the shape of sections, D2.1 steps 5–6.
- Lemma vectorform; Theorem kkm; C2.1(4).
- K3.1 (with the K3 referee's (NC) presupposition), K3.8, N17 Lemma 3.1.
- H1.2 and K3.5′(c), K3.7 (for L2.6(c) only); F1.4, Prop. Q15 (consistency remarks only); E1.3 (§7 only).

**Not yet refereed.**

`l2py/` (run with `python3 -I` from inside `l2py/`):
- `l2_common.py`: finite cell model (two levels, PG(2,2) and PG(2,3), 20 geometric blocks, 91 selectors), exact
  rationals, acceptance test via selectors and tails at breakpoints.
- `l2_check.py` (+ `l2_check.out`): blocking inequality and blocked same-level sums, strictness, monotonicity, (K),
  (U), generator acceptance, sum closure on sampled accepted vectors, sections on the breakpoint grid, flexible
  certificates for random D, endorsement by λ|_{d_a}, the σ-finite ρ of L2.5.
