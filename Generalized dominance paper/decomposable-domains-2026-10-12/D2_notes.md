# D2. A full system in which a world does not add up (n = 2): N17.B′ is false

15 Oct 2026, BRIEF13/14 rules. Labels: **PROVED** (full proof here), **CHECKED**, **CONJECTURE**, **NUMERICS**
(scripts in `d2py/`, run with `python3 -I`; no proof depends on them). No assumption is added. Notation as in the
write-up §§2–3 and §8.4–8.5, and C2_notes §1: n = 2, K′ = [α′, β′] ⊆ (0,1), U = D_{K′}, M_U, P_i, E_i(X) = X △ P_i,
M = mixed part of U, N₊ = nonnegative part of U. Models are regular when they accept a.e. h ∈ N₊.

---

## 0. Outcome

**Theorem D2.1 (PROVED).** For every K′ there is a two-world ranking on M_U with strict (G), (IB), (LA), (S) (an
explicit coherent nested selection, competitiveness on supp p, closed sections for **every** evaluable model),
(C) and (LF) at every interior selected model, in which **world 1 does not add up**: every finitely additive
ν ≥ 0 on U that vanishes on null sets and endorses world 1's relevant comparisons vanishes on the non-null set
c_a = E₁(C_a). World 2 is additive (density 1 w.r.t. μ). The selection is the C2.1 path; C_L is that path.

Consequences (all PROVED, by Theorem D2.1):
- **Conjecture N17.B′ is false**, already for n = 2 with a nested selection (N17.B′(2), P4 §5.5, P4B §8.5).
- **Conjecture Q1.C1 is false** (world 2 additive does not force world 1 to add up), and question **(R2)** of
  write-up §8.5(f) has a **negative** answer: world 1 has no simple, star or vanishing-target certificate
  (Prop. Q15, since world 2 is additive), yet fails SP^reg through ratio certificates with thin sources.
- The sentence "No world failing to add up has been found in a full system, for any target" (write-up
  Introduction) is superseded. The failure is of mode (M2) (no finite obstruction, N17.3, the selection is nested).
- For T1 on M_U: the exclusion route "prove N17.B′, then apply Theorem M0closed" cannot work as stated. A world
  that does not add up is no longer a hypothetical object; the positive route for T1 is open again in the sense
  that nothing known excludes covers whose non-additive worlds are of the D2 type. Lifting to n = 3 is **not done**
  (§6).

NUMERICS (`d2py/d2_check.py`, output `d2_check.out`; exact integer arithmetic on a finite cell model with two
levels of the design and three scale blocks at the far end of the chain): 0 failures in 1000 competitiveness
tests, 1000 no-domination tests, 800 strict-(G) tests, 1915 transitivity triples on a pool of 53 structured models,
200 incompatibility tests of generator pairs, 60 section tests (initial segments) and 28 section-formula tests;
all 40 generator comparisons accepted; target multiplicity equals the bound (q+1)/L.

**What made it work** (the answer to the brief's "which certificate shapes survive"). Next to an additive world,
(K) forces world 1 to contain the strict first-order band on cut pairs, and the band transports mass to the right.
Any ¬SP certificate whose targets can be made disjoint by such transports sums, by the chaining lemma N17.1(b),
to "a set of measure ≥ m is ≤₁ a set of small measure", which (SR₁) + (QC₁) forbid. So the surviving shape is a
**ratio certificate with thin sources whose targets cannot be separated by rightward transport**: here, targets
that meet pairwise in **every** neighbourhood of the far end x = 1 of the chain, where the base cone is not allowed
to move mass. Thin sources keep the sections closed (each section is a union of closed segments, and only finitely
many generators can raise it by more than any η > 0). The one remaining leak, sections of non-regular models,
is closed by letting unanimous-problem errors make c_a free (rule R⁺ below); this touches no relevant comparison.

---

## 1. Coordinates

Take the C2.1 path C_s = D_{[α′s, β′+(1−β′)s]}, s ∈ [0,1], with chain coordinate x_{C2}: M → (0,1). Put
λ := μ/μ(M) on U, so λ(M) = 1 and n₊ := λ(N₊) ∈ (0, ∞). Since s ↦ λ{x_{C2} < s} is continuous and strictly
increasing (C2.1 setting), the map x := λ{x_{C2} < x_{C2}(·)} sends λ|_M to Lebesgue measure on [0,1). Reindex
the path by b = λ(E₁C_s ∩ M):

- C_b (b ∈ [0,1]) is coherent, regular, C_0 = P₁, C_1 = P₂, and c_b := E₁C_b = {x < b} (mod null), λ(c_b) = b,
  E₂C_b = M ∖ c_b =: d_b (C2.1, §1).
- Selection: p ↦ C_{p₂}. Interior C_b have credal sets containing K′ in their relative interior, so (LF) holds
  at them with N = U (C2.1(4)).

For a bounded measurable f on U and t ∈ [0,1] put

  τ_f(t) := ∫_{M ∩ {x ≥ t}} f dλ + ∫_{N₊} f dλ,  D(f) := τ_f(1) = ∫_{N₊} f dλ.

τ_f is continuous in t. Every model X has E₁X = A ∪ N_X with A := E₁X ∩ M and N_X := N₊ ∖ X; X is regular iff
N_X is null, and X is determined by E₁X.

## 2. The design

Fix a ∈ (0,1) and h₀ = 2^{−m₀} with 1 − h₀ > a. A **design** is a family 𝒢 of pairs g = (P_g, Q_g) of non-null
measurable subsets of M, with g_* := 1_{Q_g} − 1_{P_g}, such that:
- **(D1)** P_g ⊆ c_a and Q_g ⊆ {x ≥ 1 − h₀};
- **(D2)** λ(Q_g ∩ Q_{g′} ∩ {x ≥ t}) > 0 for all g, g′ ∈ 𝒢 (equal or not) and all t < 1;
- **(D3)** for every η > 0 only finitely many g have λ(P_g) ≥ η;
- **(D4)** for every ε > 0 there are finitely many g ∈ 𝒢 and weights w_g > 0 with Σ w_g 1_{P_g} = 1_{c_a} and
  Σ w_g 1_{Q_g} ≤ ε everywhere on M.

**Lemma D2.2 (PROVED). Designs exist.**

*Construction.*
- Scale blocks B_m := {1 − 2^{−m} ≤ x < 1 − 2^{−m−1}}, m ≥ m₀, with the increasing affine maps u_m: B_m → [0,1).
- ι: [0,1) → [0,1)^ℕ, v ↦ (v_1, v_2, …), where v_n is read off the binary digits of v in positions whose index has
  2-adic valuation n − 1 (terminating expansions). ι is measure-preserving (Lebesgue to product Lebesgue) and
  defined everywhere.
- Level n ≥ 1: K_n := 2^n; a prime q_n ≥ 4^n; Π_n := q_n² + q_n + 1, the points of PG(2, q_n); J_{n,π} :=
  [π/Π_n, (π+1)/Π_n); L_n := ⌊Π_n/K_n⌋; an injective assignment (i, l) ↦ line ℓ_{n,i,l} (i < K_n, l < L_n).
- Ŷ_{n,i,l} := {v : v_n ∈ ⋃_{π ∈ ℓ_{n,i,l}} J_{n,π}} ⊆ [0,1).
- P_{n,i,l} := {i a/K_n ≤ x < (i+1) a/K_n}, Q_{n,i,l} := ⋃_{m ≥ m₀} (B_m ∩ u_m^{−1}(Ŷ_{n,i,l})).

*Proof.*
- (D1) holds by construction.
- (D2): given t < 1 take m ≥ m₀ with B_m ⊆ {x ≥ t}. Then λ(Q ∩ Q′ ∩ B_m) = λ(B_m) · Leb(Ŷ ∩ Ŷ′). Two lines of one
  projective plane meet in exactly one point, so at one level Leb(Ŷ ∩ Ŷ′) ≥ 1/Π_n. At different levels the
  coordinates v_n, v_{n′} are independent, so Leb(Ŷ ∩ Ŷ′) = (q_n+1)(q_{n′}+1)/(Π_nΠ_{n′}). Both are > 0.
- (D3): λ(P_{n,i,l}) = a 2^{−n}, and level n has finitely many members.
- (D4): weights 1/L_n at level n. Each source strip carries L_n generators, so Σ 1_P/L_n = 1_{c_a}. Every v_n lies
  in exactly one J_{n,π}, and π lies on q_n + 1 lines, so Σ_{i,l} 1_{Q_{n,i,l}}/L_n ≤ (q_n+1)/L_n everywhere.
  This is ≤ 2(q_n+1)2^n/q_n² → 0, because q_n ≥ 4^n. ∎

## 3. The ranking

Fix a design 𝒢. Let

  𝒦₀ := {f : f ≥ 0 a.e. on N₊; τ_f(t) ≥ 0 for all t ∈ [0,1]; and f ≥ 0 a.e. on M ∩ {x ≥ b*} for some b* < 1}.

𝒦₀ is a convex cone, closed under addition (take the larger b*). For a measurable δ: U → {−1, 0, 1}, world 1
**accepts** δ, δ ∈ 𝒜₁, by the following rules:
- **R⁻**: if D(δ) < 0, reject;
- **R⁺**: if D(δ) > 0, accept iff τ_δ(t) ≥ 0 for every t ∈ [a, 1];
- **R⁰**: if D(δ) = 0, accept iff δ ∈ 𝒦₀ or δ − g_* ∈ 𝒦₀ for some g ∈ 𝒢.

Then X ⪯₁ Y :⟺ 1_{E₁Y} − 1_{E₁X} ∈ 𝒜₁, and X ⪯₂ Y :⟺ λ(E₂X) ≤ λ(E₂Y).

In words:
- the base cone is first-order (tail) dominance in the chain coordinate, with unanimous-problem errors at the far
  right, except that it never moves mass out of a neighbourhood of x = 1;
- generators trade a thin left strip P_g for a thin set Q_g that is spread over every neighbourhood of x = 1;
- once a model errs on unanimous problems, the initial segment c_a costs world 1 nothing.

**Lemma D2.3 (PROVED).** 𝒜₁ contains every δ ≥ 0, contains no δ ≤ 0 other than 0, and contains δ₁ + δ₂ whenever
δ₁, δ₂ ∈ 𝒜₁ and δ₁ + δ₂ is {−1,0,1}-valued. Hence (write-up Lemma vectorform, P2 Lemma 1.1) ⪯₁ is a preorder on
M_U with strict (G) and (IB). World 2 is an additive ranking with density, so it has strict (G) and (IB) too.

*Proof.*
- *Fact (F).* If D(δ) = 0 and δ ∈ 𝒜₁, then τ_δ(t) ≥ 0 for t ∈ [a,1]. This is clear if δ ∈ 𝒦₀. If δ − g_* ∈ 𝒦₀,
  then τ_δ(t) ≥ τ_{g_*}(t) = λ(Q_g ∩ {x ≥ t}) ≥ 0 for t ≥ a, by (D1).
- *Near-one lemma.* If δ − g_* ∈ 𝒦₀, then δ ≥ 1_{Q_g} a.e. on M ∩ {x ≥ t*} for some t* < 1. Indeed
  g_* = 1_{Q_g} on {x ≥ 1 − h₀}, by (D1).
- *δ ≥ 0.* Then D ≥ 0. Under R⁺ all tails are ≥ 0. Under R⁰, δ ∈ 𝒦₀.
- *δ ≤ 0, δ ≠ 0.* Then D ≤ 0, and R⁻ rejects if D < 0. Suppose D = 0.
  - If δ ∈ 𝒦₀, then τ_δ(0) = ∫δ ≥ 0, so δ = 0.
  - If δ − g_* ∈ 𝒦₀, the near-one lemma and (D2) with g′ = g give δ = 1 on a non-null set. Contradiction.
- *Sums.* Let σ := δ₁ + δ₂ be ternary. D(σ) = D(δ₁) + D(δ₂) ≥ 0.
  - If D(σ) > 0: each τ_{δ_i} is ≥ 0 on [a,1], by R⁺ or by (F). So σ satisfies R⁺.
  - If D(σ) = 0, then D(δ₁) = D(δ₂) = 0.
    - If δ₁, δ₂ ∈ 𝒦₀, then σ ∈ 𝒦₀.
    - If δ₁ − g_* ∈ 𝒦₀ and δ₂ ∈ 𝒦₀, then σ − g_* ∈ 𝒦₀.
    - If δ₁ − g_*, δ₂ − g′_* ∈ 𝒦₀, the near-one lemma gives σ ≥ 2 on Q_g ∩ Q_{g′} ∩ {x ≥ t*}, which is non-null
      by (D2). This contradicts ternarity, so this case cannot occur. ∎

**Lemma D2.4 (PROVED; closed sections at world 1, every model).** Let X be any model, E₁X = A ∪ N_X, and
S₁(X) := {b ∈ [0,1] : C_b ⪯₁ X}; write δ_b := 1_{A ∪ N_X} − 1_{c_b}.

- **(i)** If λ(N_X) > 0, then S₁(X) = [0, min{1, a + λ(N_X) + λ(A ∩ {x ≥ a})}].
- **(ii)** If N_X is null, S₁(X) is a closed initial segment of [0,1].

*Proof of (i).*
- D(δ_b) = λ(N_X) > 0, so R⁺ applies.
- For t ≥ b, τ_{δ_b}(t) ≥ 0. For t < b, τ_{δ_b}(t) = ψ(t) − b with ψ(t) := t + λ(N_X) + λ(A ∩ {x ≥ t}).
- ψ is continuous and nondecreasing, since its derivative is 1 − 1_A ≥ 0.
- So the condition on [a,1] holds iff b ≤ a or b ≤ ψ(a).

*Proof of (ii).*

1. **D(δ_b) = 0**, and δ_b = 0 on N₊. So S₁(X) = B₀ ∪ ⋃_g B_g, where B₀ := {b : δ_b ∈ 𝒦₀} and
   B_g := {b : δ_b − g_* ∈ 𝒦₀}.
2. **B₀.**
   - For b < 1, δ_b = 1_A ≥ 0 on {x ≥ b}, so only the tails matter.
   - (b − t)⁺ ≤ λ(A ∩ {x ≥ t}) for all t iff b ≤ t + λ(A ∩ {x ≥ t}) for all t < b, iff b ≤ λ(A), by monotonicity
     as in (i).
   - For b = 1, δ₁ = −1_{M∖A} lies in 𝒦₀ iff A = M a.e.
   - So B₀ = [0, λ(A)] if λ(A) < 1, and B₀ = [0,1] if A = M.
3. **B_g.**
   - b = 1 is excluded: δ₁ − g_* ≤ −1 on Q_g ∩ {x ≥ t} for every t, which is non-null by (D2).
   - For b < 1 the near-one clause says Q_g ∩ {x ≥ t} ⊆ A a.e. for some t < 1. This is a condition on A only
     (eligibility).
   - The tail clause reads (b − t)⁺ ≤ u_g(t) for all t, with u_g(t) := λ(A ∩ {x ≥ t}) − τ_{g_*}(t), which is
     continuous in t.
   - *Initial segment.* Let b ∈ B_g and b′ < b. For t ≥ b, u_g(t) ≥ 0. For t ∈ [b′, b), u_g(t) ≥ b − t > 0. For
     t < b′, b′ < b ≤ t + u_g(t).
   - *Closed.* Let b_k ↑ β with b_k ∈ B_g. For t ≥ β, t ≥ b_k, so u_g(t) ≥ 0. For t < β, eventually t < b_k, so
     b_k ≤ t + u_g(t), and in the limit β ≤ t + u_g(t).
   - *Bounds.* At t = 0: b ≤ λ(A) + λ(P_g) − λ(Q_g). If b > a, at t = a:
     b ≤ a + λ(A ∩ {x ≥ a}) − λ(Q_g) ≤ 1 − λ(Q_g) < 1.
   - So B_g is empty or [0, β_g] with β_g ≤ min{λ(A) + λ(P_g), 1 − λ(Q_g)}.
4. **The union is closed.**
   - If A = M, S₁(X) = [0,1].
   - Otherwise put β₀ := λ(A) < 1 and s := sup of S₁(X). If s ≤ β₀, then S₁(X) = B₀.
   - If s > β₀, every g with β_g > (s + β₀)/2 has λ(P_g) ≥ β_g − β₀ > (s − β₀)/2. By (D3) there are finitely many
     such g, so s = max β_g is attained. ∎

**Theorem D2.1 (PROVED).** The ranking (⪯₁, ⪯₂) on M_U with selection p ↦ C_{p₂} satisfies strict (G), (IB),
(LA), (S) (competitiveness on supp p, closed sections for every model at both worlds), (C), C_L = {C_b : b ∈ [0,1]},
(LF) at every interior C_b; and world 1 does not add up: every endorsing weight vanishes on c_a.

*Proof.* Fix a model X, E₁X = A ∪ N_X, and a cut b. Put P := c_b ∖ A and Q := A ∖ c_b. Then:
- E₂X = (M ∖ A) ∪ N_X;
- C_b ⪯₂ X ⟺ λ(Q) ≤ λ(P) + λ(N_X);
- C_b ⪯₁ X ⟺ 1_{Q ∪ N_X} − 1_P ∈ 𝒜₁.

1. **(G), (IB).** Lemma D2.3.
2. **Competitiveness.**
   - *Vertices.* C_0 = P₁ has E₁ = ∅, so C_0 ⪯₁ X by (G). Likewise C_1 ⪯₂ X.
   - *Interior b.* Suppose C_b ⋠₂ X, i.e. λ(Q) > λ(P) + λ(N_X).
     - If λ(N_X) > 0, R⁺ applies: τ ≥ 0 trivially for t ≥ b, and for t < b, τ ≥ λ(N_X) + λ(Q) − λ(P) > 0.
     - If N_X is null, 1_Q − 1_P ∈ 𝒦₀: it is ≥ 0 on {x ≥ b}, its tails are ≥ λ(Q) − λ(P) ≥ 0 below b, and it is 0
       on N₊.
     - So C_b ⪯₁ X. This is (K) for every model.
3. **Closed sections.**
   - World 2: S₂(X) = {b : λ(A ∩ d_b) ≤ λ(c_b ∖ A) + λ(N_X)}, which is closed because both sides are continuous
     in b.
   - World 1: Lemma D2.4.
   - p ↦ p₂ is continuous, so the sections in p are closed. Hence (S).
4. **No weak domination of C_b.** Suppose X ⪯₁ C_b and X ⪯₂ C_b, and put δ′ := 1_P − 1_{Q ∪ N_X}.
   - D(δ′) = −λ(N_X), so R⁻ forces N_X to be null.
   - Under R⁰:
     - if δ′ ∈ 𝒦₀, then τ_{δ′}(b) = −λ(Q) ≥ 0, so Q is null;
     - δ′ − g_* ∈ 𝒦₀ is impossible: δ′ − g_* ≤ −1 on Q_g near 1, by (D2).
   - Then X ⪯₂ C_b gives λ(P) ≤ λ(Q) = 0. So E₁X = c_b and X = C_b.
5. **C_L, (C), (LA).**
   - By 4, every C_b is undominated, and the only model tied with C_b at both worlds is C_b.
   - By Theorem kkm (which needs (LA) and (S), both available), every undominated model is tied at every world
     with some selected C_b, hence equals it.
   - So U_L = C_L = {C_b}, all coherent; (LA) and (C) hold.
6. **(LF).** C2.1(4).
7. **World 1 does not add up.**
   - For g ∈ 𝒢 let X_g be the regular model with E₁X_g = (c_a ∖ P_g) ∪ Q_g.
   - Then 1_{E₁X_g} − 1_{c_a} = g_*, and g_* − g_* = 0 ∈ 𝒦₀. So C_a ⪯₁ X_g, a relevant comparison
     (C_a ∈ C_L, X_g regular).
   - Let ν ≥ 0 be finitely additive on U, zero on null sets, with ν(c_a) ≤ ν(E₁X_g), i.e. ν(P_g) ≤ ν(Q_g), for all g.
   - Fix ε > 0 and take (D4). Then
     ν(c_a) = Σ w_g ν(P_g) ≤ Σ w_g ν(Q_g) = ∫ Σ w_g 1_{Q_g} dν ≤ ε ν(M).
   - So ν(c_a) = 0, while c_a is non-null. No weight positive on non-null sets endorses the relevant comparisons:
     world 1 fails SP^reg (write-up Def. addup(b)). ∎

*Remarks (PROVED by inspection unless marked).*
- **Mode.** The certificate is of mode (M2). Since the selection is nested, N17.3 excludes finite obstructions.
- **Consistency with the corpus.** Prop. Q15 forbids simple, star and vanishing-target certificates next to an
  additive world; here every pair of targets meets near x = 1, so no two exotic comparisons chain (Lemma D2.3, last
  case). Lemma T, (QC₁) and (SR₁) hold:
  - φ₁(P) ≥ λ(P) by the base cone;
  - a fixed source can use only finitely many generators with λ(P_g) bounded below, by (D3), and each has a target
    of fixed positive measure.

  The rate is superlinear: for level-n sources, η₁(P,1) ≤ λ(Q_g) ≈ h₀/q_n ≪ λ(P) = a2^{−n}. This is exactly what
  Prop. LIN requires of any ratio certificate, and what Prop. ExA showed to be compatible with the axioms.
- **Why R⁺ is needed (the (R5) closure).** Suppose unanimous-problem errors were treated like M (tail dominance
  with costed moves into N₊). Then sums of generators become possible by moving their overlaps into N₊. For
  X with A = {a ≤ x < a + r} and λ(N_X) = η, the section would then be [0, a + r + η − κ) with κ > 0 the least
  total target cost, which is not closed. R⁺ is the limit of those sums. It concerns only non-regular models, so
  no relevant comparison is affected (N19 Prop R3 is the analogous freedom).
- **Why the protected end.** Without the near-one clause in 𝒦₀, tail transport separates the targets, and the
  summed comparisons contradict (QC₁) and (SR₁) (§0). With the clause at an interior point instead of at x = 1, (K)
  next to an additive world fails on cut pairs whose left part meets the protected zone.

## 4. Status

| Item | Statement | Label |
|---|---|---|
| D2.2 | designs exist (projective planes, multi-scale at x = 1, independent levels) | PROVED |
| D2.3 | world 1 is a preorder with strict (G), (IB) | PROVED |
| D2.4 | closed world-1 sections for every model | PROVED |
| D2.1 | full two-world system on M_U; world 1 fails SP^reg (mode M2); world 2 additive | PROVED; NUMERICS |
| N17.B′, N17.B′(2), Q1.C1 | refuted | PROVED (by D2.1) |
| (R2) of §8.5(f) | negative answer | PROVED (by D2.1) |
| (R1) mirrored simple pairs; (R4) | untouched | open |

## 5. What this does and does not give for T1

- **It removes the main exclusion route.** M0closed excludes rankings all of whose worlds add up, and the hoped-for
  last step was "every world of a full system adds up". In n = 2 that step is false, with an additive neighbour.
- **It is not a cover of T1.** A cover needs n = 3, T1 ∈ C_L, and a world that fails to add up on comparisons that
  carry the corner holonomy at T1 (write-up Thm R3, N17.5).
- The D2 mechanism is edge-local. It uses a chain of selected models, an additive complementary world, and a
  protected end of the chain. On an edge e_ij of a three-world system the end of the chain is the vertex model P_j,
  and the edge results transfer under (Nest_e) (Prop. Q35). So the mechanism can be placed on an edge region R_ij.
- **CONJECTURE D2.C.** The D2 world can be installed on one edge region R_ij of a three-world full system on M_U
  (world i's comparisons on R_ij as in §3, all other comparisons generated through the link classes with the exact
  consistency test and R5), keeping every axiom.
  - This would give a three-world full system with a world that does not add up.
  - It would still not be a cover of T1. That would additionally need the non-additive comparisons at the corner
    holonomy, which lie at interior selected models (N17.5), not at an edge end.
  - Not attempted here.

## 5a. Files (`d2py/`)

- `d2_check.py` (+ `d2_check.out`): finite cell model, levels n = 1, 2 (q = 3, 5), three scale blocks at x = 1,
  N₊ appended. It checks:
  - every generator comparison is accepted;
  - the source cover and the target multiplicity bound;
  - pairwise meeting of all targets in the last block;
  - (K), no weak domination, strict (G), transitivity on a model pool, incompatibility of generator pairs;
  - sections are initial segments, and the formula of D2.4(i).

  The near-one clause is proxied by "the last block". 0 failures.
