# S4. Mirrored simple pairs (R1), the rate in Lemma T (R3), and general certificates (R2), two nested worlds

15 Oct 2026, round 13, exclusion side. Labels: **PROVED** (full proof here from the cited inputs), **CHECKED**,
**CONJECTURE**, **NUMERICS**. Terminology as in TERMFIX_RULES and the write-up (decomposable domain, U-domain M_U,
advice range). No assumption is added to the framework. Scripts: `s4py/` (run with `python3 -I`); no proof uses them.

Inputs (all refereed): write-up §8.4(c) ((Nest), (K), Lemma B0, strict escape SE = Prop strictescape), §8.5(c)
(cut-pair form, Lemma T₁, T₂, Thm LF, Cor IS, Prop MP, Cor MP-loop, Props NS, Q15, N1, N2), Thm witness (§8.4(a));
P4B_referee §8 (DL, DR, Lemma T); N19 Lemma R1; N9.4 normal form.

---

## 0. Outcome

**(R1) is not settled.** No system with a mirrored simple pair was constructed and none was excluded. §5 is the failure
report. What was proved changes the picture of how R1 and R2 can be attacked.

1. **Theorem RATE (PROVED).** The qualitative rate (R3) is a *single joint property* of the two worlds. The following are
   equivalent:
   - (R3) at world 1;
   - (R3) at world 2;
   - a rate in strict escape at either world;
   - **no doubly-light sequence**: no sets S_k with μ̄(S_k) ≥ m > 0 such that world 1 ranks each S_k below a set
     concentrating at the right end and world 2 ranks each S_k below a set concentrating at the left end.
   Failure of R3 is therefore a "light fat sets at both worlds" phenomenon. It is the exact dual of a mirrored pair,
   which is "thin sets heavy at both worlds".
2. **Corollary SR (PROVED).** (R3) holds at both worlds whenever world 2 has a strictly positive endorsing weight
   ν₂ ∈ 𝓜₂ with ν₂(c_t) → 0 as t ↓ 0. In particular (R3) holds whenever world 2 is additive with an integrable density.
   That is the setting of Q1.C1, where R2 is still open. So **qualitative R3 cannot be the missing lemma for R2.**
3. **Example A and Prop LIN (PROVED).** To exclude the ratio certificates of N4 through MP, the rate must be *linear*:
   η₁(P,1) ≥ c·μ̄(P). Example A satisfies every axiom, has world 2 additive with density 1 (μ̄) and world 1 additive,
   and has η₁(P,1) ≤ μ̄(P)²/2. Variants give η₁(P,1) ≈ μ̄(P)^q for any q ≥ 2. So **no linear rate follows from the
   axioms, even next to an additive world**. In Example A, ratio certificates are excluded only because world 1 is
   additive. A proof of R2 by rates would have to use the failure of SP itself. The write-up's statement that (R3)
   "would give Q1.C1" should be withdrawn or changed to the linear form; see §4.3 for the precise correction.
4. **Prop MP♯ (PROVED).** MP has an exact threshold. For non-null Z put τ(Z) := sup{t : Z ≤₁ d_t}. Then d_t ≤₂ A for
   every A with Z ≤₁ A and every t > τ(Z), and this fails for some such A at every t < τ(Z). When world 2 is μ̄:
   inf{μ̄(A) : Z ≤₁ A} = 1 − τ(Z) (NUMERICS agree to 10⁻⁵).
   **Loop lemma (PROVED):** the MP ping-pong never raises the exported initial segment. This sharpens N2.
5. **R1 is not a rate problem (PROVED observations, §5).** In R1 the sources are fixed, so Lemma T's per-source radius
   already applies and any rate adds nothing. What is missing is a *fibre-sensitive* comparison that sends thin, spread
   targets into a slab. LF cannot provide it: next to world 2 = μ̄, any LF transport of A ∩ c_a needs receivers of total
   measure ≥ a, however thin A is. The uniform-escape route (Lemma UE) leaves exactly a thin residue.
6. **Pointer for the construction side.** A surviving system must contain thin spread sets that both worlds rank as
   heavy errors. A system failing R3 must contain fat sets that both worlds rank as light. Both phenomena generate only
   comparisons in the favourable direction (N2, Loop lemma, §2.4), so (U), (K) and (C) cannot detect them. Only
   closedness in the chain parameter can, and that closedness is blind to the fibre direction. The family to try is
   §6: worlds that are additive along the chain and spread-heavy across fibres.

---

## 1. Setting

**(Nest):** n = 2 on M_U, with strict (G), (IB), (LA), (S), (C). The world-1 error sets of 𝒞_L form a chain c_b,
with μ̄(c_b) = b, d_b := M∖c_b, and slabs [s,t) := c_t∖c_s, all mod null. Both worlds are cancellative, strictly
monotone preorders on the measurable subsets of M (N9.4).
- A ≤₁ B compares world-1 error sets.
- B ≤₂ B′ compares world-2 error sets.
- A model with E₁ = A has E₂ = M∖A on M.

Notation:
- φ₁(A) := max{b : c_b ≤₁ A}. The section S₁(A) = [0, φ₁(A)] is closed (B0).
- φ₂(B) := min{t : d_t ≤₂ B}, for B a world-2 error set. S₂(B) = [φ₂(B), 1].
- **(K)**: for interior b and every measurable A ⊆ M, c_b ≤₁ A or d_b ≤₂ M∖A.
- **Sum closure** (cancellation plus transitivity): if L₁ ≤ R₁ and L₂ ≤ R₂ and L₁, L₂, R₁, R₂ are pairwise disjoint,
  then L₁ ∪ L₂ ≤ R₁ ∪ R₂.
- *Concentrating at x*: a sequence of non-null sets Q_k with Q_k ⊆ (x − r_k, x + r_k), r_k → 0. Lemma T_i says no
  fixed non-null set is ≤_i every member of such a sequence.

Rates. For m > 0 define:
- **(SR₁)** σ₁(m) := inf{φ₁(P) : μ̄(P) ≥ m} > 0.
- **(SR₂)** σ₂(m) := inf{1 − φ₂(W) : μ̄(W) ≥ m} > 0.
- **(R3₁)** (the brief's form) For every m, g > 0 there is η > 0 such that: whenever P ⊆ c_b, μ̄(P) ≥ m and x ≥ b + g,
  no non-null Q ⊆ (x−η, x+η) has P ≤₁ Q.
- **(R3₁ᵘ)** (uniform form) For every m > 0 there is η > 0 such that: for every P with μ̄(P) ≥ m and every
  x ∈ [0,1], no non-null Q ⊆ (x−η, x+η) has P ≤₁ Q. (Necessarily η < m/2.)
- **(R3₂), (R3₂ᵘ)** mirror: W ⊆ d_b, x ≤ b − g, and W ≤₂ Q.

Each is meant "for every m > 0" and within one fixed system. Across systems no positive bound exists; see Example A,
remark (iii).

---

## 2. Theorem RATE

### 2.1 Statement (PROVED)

Under (Nest), the following are equivalent:
(R3₁), (R3₁ᵘ), (SR₁), (R3₂), (R3₂ᵘ), (SR₂), and

**(NDL)** there is no **doubly-light sequence**. A doubly-light sequence is a sequence S_k ⊆ M with
inf_k μ̄(S_k) > 0, together with non-null R_k concentrating at 1 and non-null V_k concentrating at 0, such that
S_k ≤₁ R_k and S_k ≤₂ V_k for all k.

Moreover, if (SR₁) fails at m, then a doubly-light sequence exists with μ̄(S_k) ≥ m/3 and S_k ⊆ [m/3, 1 − m/3).

### 2.2 Proof

**Step A: (SR₁) ⇒ (R3₁ᵘ).**
- Suppose (R3₁ᵘ) fails at m. Then there are P_k with μ̄(P_k) ≥ m, points x_k, and non-null
  Q_k ⊆ (x_k − 1/k, x_k + 1/k) with P_k ≤₁ Q_k.
- Pass to a subsequence with x_k → x̄. The Q_k then concentrate at x̄.
- Put σ := σ₁(m) > 0. Since φ₁(P_k) ≥ σ and S₁(P_k) is the initial segment [0, φ₁(P_k)], we have c_σ ≤₁ P_k ≤₁ Q_k.
- The fixed non-null set c_σ is therefore ≤₁ a sequence concentrating at x̄. This contradicts Lemma T₁ (one point).

**Step B: (R3₂) ⇒ (SR₁).** (The mirror argument gives (R3₁) ⇒ (SR₂).)
- Suppose (SR₁) fails at m. Then there are P_k with μ̄(P_k) ≥ m and φ₁(P_k) → 0. Put g := m/3, and choose
  t_k ∈ (φ₁(P_k), g) with t_k → 0.
- Since t_k ∉ S₁(P_k), (K) at the interior cut t_k gives d_{t_k} ≤₂ M∖P_k. By cancellation this is
  d_{t_k} ∩ P_k ≤₂ c_{t_k} ∖ P_k =: V_k.
- Put W_k := P_k ∩ d_g ⊆ d_{t_k} ∩ P_k. By monotonicity W_k ≤₂ V_k.
- μ̄(W_k) ≥ 2m/3, so W_k is non-null. Hence V_k is non-null, by strict (G) (W_k ≤₂ ∅ is impossible).
- V_k ⊆ c_{t_k} concentrates at 0, and W_k ⊆ d_g. So (R3₂) with gap g fails at measure 2m/3.

**Step C: closing the cycle.**
- (R3₁ᵘ) ⇒ (R3₁) is trivial. Steps A and B and their mirrors then give
  (SR₁) ⇒ (R3₁ᵘ) ⇒ (R3₁) ⇒ (SR₂) ⇒ (R3₂ᵘ) ⇒ (R3₂) ⇒ (SR₁).

**Step D: (NDL) is equivalent to the rest.**
- (NDL) fails ⇒ (R3₁ᵘ) fails: S_k ≤₁ R_k with the R_k concentrating at 1.
- (SR₁) fails ⇒ (NDL) fails:
  - Keep W_k ≤₂ V_k from Step B.
  - If φ₂(W_k) ≤ 1 − σ′ along a subsequence, then d_{1−σ′} ≤₂ W_k ≤₂ V_k, against Lemma T₂ at x = 0 (fixed source
    d_{1−σ′}). So φ₂(W_k) → 1.
  - Take τ_k ∈ (1 − g, φ₂(W_k)) with τ_k → 1. Then d_{τ_k} ≰₂ W_k. (K) at τ_k for the model with E₂ = W_k (that is,
    E₁ = M∖W_k) gives c_{τ_k} ≤₁ M∖W_k, i.e. c_{τ_k} ∩ W_k ≤₁ d_{τ_k} ∖ W_k =: R_k.
  - Put S_k := W_k ∩ c_{1−g}. Then S_k ≤₁ R_k by monotonicity, and S_k ≤₂ W_k ≤₂ V_k.
  - μ̄(S_k) ≥ m − 2g = m/3. R_k is non-null by strict (G), and R_k ⊆ d_{τ_k} concentrates at 1.
  - S_k ⊆ [g, 1 − g). ∎

### 2.3 Remarks (PROVED)

- **(i) The sources must move.** In a doubly-light sequence, no non-null Z is contained in infinitely many S_k
  (Lemma T₁ at 1). More generally, the S_k can share no common lower bound for ≤₁.
- **(ii) Duality with R1.** The two configurations are exact duals:

  | | R1 (mirrored pair) | ¬R3 (doubly-light) |
  |---|---|---|
  | Sources | **fixed**: c_{s₀} at world 1, d_{b₀} at world 2 | **moving**, fat |
  | Targets | **thin**, spread (uniformly Cesàro-thin) | **concentrated** at the far end of each world |
  | In words | thin sets heavy at both worlds | fat sets light at both worlds |

  In each case, Lemma T is what forces the other half to move (targets in R1, sources in ¬R3).
- **(iii) Rates are per system.** Across systems no lower bound depending only on (m, gap) exists. In Example A
  (§4.1), make θ steep near 1 while keeping θ(1/2) = 1: then η₁([1/2 − m, 1/2), 1) is as small as desired for fixed m.

### 2.4 Doubly-light sequences generate only favourable comparisons (PROVED)

- Fix a cut b. Write S_k = S^L ∪ S^R, with S^L ⊆ c_b and S^R ⊆ d_b.
- The comparisons that the definition and (K) produce are S^L ≤₁ R_k and S^R ≤₂ V_k. These are cut pairs in the
  favourable direction at their worlds: left ≤₁ right, and right ≤₂ left.
- (U) forbids only the reverse acceptances. So, exactly as for mirrored pairs (N2), undominatedness gives no
  contradiction.
- Any exclusion of doubly-light sequences, like any exclusion of mirrored pairs, must use closedness beyond Lemma T.
  Closedness used *for a fixed source* is exhausted by Lemma T, which is how it enters Steps A–D.

---

## 3. Rates next to a world with SP; the exact form of MP

### 3.1 Corollary SR (PROVED)

**Statement.** Assume world 2 has an endorsing weight ν₂ ∈ 𝓜₂ that is positive on non-null sets and has
ν₂(c_t) → 0 as t ↓ 0. Then Theorem RATE's conditions hold, so (R3) holds at both worlds. The same holds with the worlds
exchanged, using ν₁(d_t) → 0 as t ↑ 1.

The hypothesis holds when world 2 is additive with an integrable density ρ₂ > 0 a.e. (the Q1.C1 setting).

*Proof.*
1. **A uniform lower bound.** By N19 Lemma R1, the countably additive part of ν₂ has a density ρ > 0 a.e. Put
   κ(m) := inf{ν₂(B) : μ̄(B) ≥ m}. Then κ(m) > 0:
   - if ∫_{B_k} ρ → 0 with μ̄(B_k) ≥ m, then μ̄(B_k ∩ {ρ ≥ ε}) ≤ ε⁻¹∫_{B_k}ρ → 0;
   - so μ̄{ρ < ε} ≥ m for every ε > 0;
   - this contradicts μ̄{ρ = 0} = 0, by continuity from above.
2. **The contradiction.** Suppose (SR₁) fails at m. Step B uses the comparison d_{t_k} ≤₂ M∖P_k, which is relevant:
   C_{t_k} ⪯₂ X with X regular and E₂X = M∖P_k. Endorsement and additivity of ν₂ give
   ν₂(d_{t_k} ∩ P_k) ≤ ν₂(c_{t_k} ∖ P_k).
   - The left side is ≥ κ(m/2) once t_k ≤ m/2.
   - The right side is ≤ ν₂(c_{t_k}) → 0.
   - This is a contradiction. Now apply Theorem RATE. ∎

**Reading.** In the setting of Q1.C1 (world 2 additive) the qualitative rate of R3 holds outright. R2 is open there
(Q1.C1). So qualitative R3 does not imply R2.

### 3.2 Proposition MP♯ (PROVED): the exact threshold of MP

**Statement.** For non-null Z ⊆ M put τ(Z) := sup{t ∈ [0,1) : Z ≤₁ d_t}. The set over which the sup is taken
contains t = 0, and the set {t : Z ≤₁ d_t} is an initial segment.
- (a) τ(Z) < 1 by Lemma T₁ at x = 1. Also τ(Z) > 0 unless Z = M.
- (b) For every A ∈ 𝒰₁(Z) := {A : Z ≤₁ A} and every t ∈ [τ(Z), 1): d_t ≤₂ A.
- (c) For every t < τ(Z) there is A ∈ 𝒰₁(Z) with d_t ≰₂ A.
- (d) So ⋂_{A∈𝒰₁(Z)} S₂(A) = [τ(Z), 1] exactly. For ν ∈ 𝓜₂:
  lim_{t↓τ(Z)} ν(d_t) ≤ inf_{A∈𝒰₁(Z)} ν(A) ≤ ν(d_{τ(Z)}).
  If world 2 is μ̄, then inf{μ̄(A) : Z ≤₁ A} = 1 − τ(Z).

*Proof.*
- (b) Let t ∈ (τ(Z), 1) and A ∈ 𝒰₁(Z), and consider the cut pair (A ∩ c_t, d_t∖A).
  - If A ∩ c_t ≤₁ d_t∖A, cancellation gives A ≤₁ d_t, so Z ≤₁ d_t, against t > τ(Z).
  - So (K) gives d_t∖A ≤₂ A ∩ c_t, which is d_t ≤₂ A.
  - The point t = τ(Z) is included because S₂(A) is closed.
- (c) Take t < t′ < τ(Z) with Z ≤₁ d_{t′}, and A := d_{t′}. Then d_t ⊋ d_{t′} with non-null difference, so
  d_{t′} <₂ d_t by strict (G).
- (a) If τ(Z) = 0, then (b) with A = Z gives d_t ≤₂ Z for every t ∈ (0,1), and closedness gives M ≤₂ Z, so Z = M.
- (d) The first claim combines (b) and (c). The lower bound on inf ν(A) is (b) with endorsement. The upper bound takes
  A = d_{t′} with t′ ↑ τ(Z). For μ̄ both bounds equal 1 − τ(Z). ∎

NUMERICS `s4py/rate_examples.py` (2): additive world 1 with θ = (1−x)^{-1/2} and world 2 = μ̄. The bathtub minimum of
μ̄(A) over A with c_s ≤₁ A equals 1 − τ(s) for s = 0.05, 0.2, 0.5, 0.8, to within 10⁻⁵.

MP is the special case b₀(Z) ≥ τ(Z). MP♯ improves N1(c): the modulus is ν₂(d_{τ(Z)}), not ν₂(d_{b₀(Z)}).

### 3.3 Loop lemma (PROVED): the ping-pong never raises the exported segment

**Definitions.** T(s) := τ(c_s) (world 1) and S(t) := inf{s : d_t ≤₂ c_s} (world 2). Mirror of MP♯: for
B ∈ 𝒰₂(d_t) and s′ < S(t), c_{s′} ≤₁ B.

**Statement.** For every s and every t > T(s):

  𝒰₁(c_s) ⊆ 𝒰₂(d_t) ⊆ 𝒰₁(c_{s′}) for all s′ < S(t), and S(t) ≤ s.

*Proof.*
- The two inclusions are MP♯(b) and its mirror.
- For S(t) ≤ s, apply (K) to the cut pair (c_s, d_t) at any cut in (s,t). Since t > T(s), c_s ≰₁ d_t, so
  d_t ≤₂ c_s, i.e. S(t) ≤ s. ∎

**Reading.** Each round of MP-loop returns a world-1 statement about an initial segment no longer than the one it
started from. This is the quantitative form of N2: the mirrored pair is a fixed point of the ping-pong, and (K) is used
up in reaching it.

---

## 4. Why the rate route to R2 is closed

### 4.1 Example A (PROVED; axioms verified through writeup Thm witness)

**The system.**
- n = 2 on M_U with K′ = [k₁, k₂]. Let b ↦ C_b be the coherent comonotone path of write-up §8.5(e), and
  x(h) := inf{b : h ∈ c_b} on M. Its image measure is Lebesgue.
- Fix θ : [0,1) → (0,∞), continuous, strictly increasing, integrable, with θ(x) → ∞ as x → 1. Example A proper uses
  θ(x) = (1−x)^{-1/2}.
- World 2: ψ₂(X) := μ̄(E₂X). World 1: ψ₁(X) := ∫_{E₁X} ρ₁ dμ̄, with ρ₁ := θ(x(h)) on M and 1 on N₊.
- Selection: C_p := the p-Bayes model.

**C_p lies on the chain.** For interior p put r := p/(1−p).
- On M⁺ (h₁ > 0 > h₂), C_p rejects h, which is the world-1 error, iff θ(x) < r.
- On M⁻ it accepts h, which is the world-1 error, iff θ(x) < r.
- The tie set {θ(x) = r} is a single level set of x, so it is null.
- Hence C_p = C_{b(p)} with b(p) := θ⁻¹(r) when r > θ(0), and b(p) := 0 otherwise.
- So the selection is continuous onto the chain, coherent, and nested.

**(W1)–(W4) of Thm witness hold.**
- **(W1)** Competitiveness: a Bayes model minimises p·ψ.
- **(W2)** Undominatedness:
  - at interior p, by uniqueness of the Bayes model;
  - at p = e₁, ψ₁(X) = 0 forces X = P₁ on U, since ρ₁ > 0.
- **(W3)** p ↦ ψ_i(C_p) is continuous, by dominated convergence with integrable ρ₁.
- **(W4)** ψ(X) = ψ(C_p) forces X = C_p a.e.:
  - at interior p, by uniqueness of the Bayes model;
  - at a vertex, by the argument in (W2).

So the system is successful: every axiom holds, with closed sections for every model and 𝒞_L the selection. Strict (G)
holds because both densities are > 0 a.e. Both worlds are additive, so both satisfy SP.

**The radius at x = 1.** Let P_m := [1/2 − m, 1/2) ⊆ c_{1/2} (gap 1/2 to x = 1). Then
ρ₁(P_m) ≤ θ(1/2)·m = √2·m, while ρ₁(d_{1−η}) = 2√η. So P_m ≤₁ d_{1−η} once η ≥ m²/2, and

  η₁(P_m, 1) ≤ m²/2.

Variants:
- θ = (1−x)^{-α} gives η₁ ≈ ((1−α)ρ₁(P_m))^{1/(1−α)}, of order m^{1/(1−α)}.
- θ with ∫_{1−η}^1 θ ≈ 1/log(1/η) gives η₁ ≈ e^{−c/m}.
- With world-2 density w(h) := |x(h) − x₀|^{-1/2} and world-1 density θ(x)w(h), the same phenomenon occurs at any
  interior x₀, at either world.

NUMERICS `s4py/rate_examples.py` (1):
- θ = (1−x)^{-1/2}: η/m² → 0.500.
- θ = (1−x)^{-0.9}: log η / log m → 10.
- (3): w = |x − 0.3|^{-1/2} gives η₂(m)/m → 0, with κ(m) ≈ 1.2m.

### 4.2 Proposition LIN (PROVED; conditional, and vacuous as a route)

**Statement.** Let world 2 be μ̄ (or any SP world whose weight ν₂ satisfies ν₂(d_t) ≥ c′(1−t)). Suppose there are
c > 0 and m₀ > 0 with η₁(P,1) ≥ c·μ̄(P) for every P with μ̄(P) ≤ m₀. Then world 1 has no ratio certificate of the type
in N4 with ε < c·c′·a.

*Proof.*
- Let P_i ≤₁ Q_il, with μ̄(P_i) = a/K and average μ̄(Q_il) ≤ ε/K.
- Lemma T₁ for P_i at x = 1 has radius ≥ c·a/K, so b₀(P_i) ≤ 1 − c·a/K, and τ(P_i) ≤ b₀(P_i).
- MP♯(b): d_t ≤₂ Q_il for t ≥ 1 − c·a/K. Endorsement gives μ̄(Q_il) ≥ c′·c·a/K for every l. This contradicts the
  average once ε < cc′a. ∎

**Reading.**
- Through MP, a rate f excludes N4 certificates only if liminf_{m→0} f(m)/m > 0.
- Example A has world 2 = μ̄ and f(m) ≤ m²/2. So the linear rate is **not** a consequence of the axioms, even in the
  Q1.C1 setting.
- In Example A, N4 certificates are absent only because world 1 is additive.
- A proof of R2 or of Q1.C1 through rates must therefore derive linearity from the hypothetical ¬SP certificate
  itself. No such mechanism is known.
- Together with Corollary SR: the qualitative R3 is free where it was supposed to help, and the linear R3 is false in
  general.

### 4.3 Correction proposed for write-up §8.5(f), item (R3)

Replace "(R3) would give Q1.C1" by:
- The qualitative rate is equivalent to the absence of doubly-light sequences (Theorem RATE). It holds next to any
  additive world (Corollary SR), so it does not give Q1.C1.
- What MP needs is a rate that is linear in μ̄(P). That fails in additive systems with every axiom (Example A), so it
  cannot be a general lemma.

The claim "with LF it would give a Vitali argument for N17.B′(2)" is not supported either; see §5.2.

---

## 5. (R1): failure report, and what is still provable

Fix a mirrored pair:
- a non-null Z and a uniformly Cesàro-thin 𝒜 ⊆ 𝒰₁(Z);
- s₁ = max{s : c_s ≤₁ A for all A ∈ 𝒜} > 0 and t₁ = min{t : d_t ≤₂ A for all A ∈ 𝒜} < 1 (N2).

### 5.1 Rates are irrelevant to R1 (PROVED, by inspection)

- The sources c_{s₁} and d_{t₁} are fixed. Lemma T₁ and T₂ already give their radii.
- No step of a contradiction would need uniformity over sources. Any additional rate (R3) leaves the configuration
  untouched.
- Concretely: Corollary SR, Theorem RATE and every conclusion of §3 are consistent with the mirrored-pair data,
  because all of them are lower bounds on φ₁ and φ₂. R1 needs an *upper* bound: φ₁(A) → 0 as A becomes thin.

### 5.2 LF cannot concentrate thin targets (PROVED in the class where world 2 is μ̄; an illustration of the mechanism)

The natural Vitali step goes as follows:
- cut A ∩ c_a into slab pieces of width < δ;
- send each piece by LF to a receiver W_l ⊆ d_a, with the receivers pairwise disjoint;
- sum (sum closure);
- repeat until the target lies in d_{1−η(Z,1)}, which contradicts Lemma T₁.

This cannot work, for the following reason.
- When world 2 is μ̄, W ≤₂ Q forces μ̄(Q) ≥ μ̄(W).
- So the radius of Lemma T₂ for W is μ̄(W)/2, and the width that LF's proof supplies (slabs on which W ≤₂ Q is
  excluded, so that (K) forces Q ≤₁ W) obeys δ(W_l, a) ≤ μ̄(W_l).
- A cover of c_a by pieces of widths ≤ δ_l therefore needs Σ_l μ̄(W_l) ≥ Σ_l δ_l ≥ a.

So LF transport (comparisons obtained through LF's mechanism) turns any subset of c_a, however thin, into receivers of total measure ≥ a. The thinness of A is lost
at the first step, and the process never reaches a slab of width η(Z,1) once a > η(Z,1).

LF sees only *where* a set lies along the chain, never *how thin it is in the fibre*. Every closedness consequence
proved so far has this form (DL, DR, SE, Lemma T, LF, IS, MP, MP♯). What R1 needs is a fibre-sensitive comparison:
"a small subset of a narrow slab is ≤₁ a set of comparable measure". That is an additivity property, not a closedness
property, and no proof of it from the axioms was found.

### 5.3 Uniform escape (Lemma UE, PROVED; inconclusive)

**Statement.** Let 𝒜 be pairwise disjoint, with c_x ≤₁ A for every A ∈ 𝒜. Suppose there is κ > 0 with
c_{x+κ} ≤₁ c_x ∪ A for every A ∈ 𝒜 ("uniform escape at x"). Then c_{x+κ} ≤₁ A ∪ A′ ∪ B for any three distinct
members A, A′, B.

*Proof.*
1. c_x ≤₁ B reads c_x∖B ≤₁ (B ∩ [x, x+κ)) ∪ (B ∩ d_{x+κ}).
2. Escape for A, with monotonicity, gives B ∩ [x, x+κ) ≤₁ A ∩ d_{x+κ}. Here B ∩ [x,x+κ) ⊆ [x,x+κ)∖A because A and B are
   disjoint.
3. Substituting 2 into 1 (sum closure with B ∩ d_{x+κ}) gives c_x∖B ≤₁ (A ∪ B) ∩ d_{x+κ}.
4. Escape for A′ gives [x, x+κ)∖(A ∪ A′ ∪ B) ≤₁ A′ ∩ d_{x+κ}.
5. All left and right pieces in 3 and 4 are pairwise disjoint. Sum closure, then monotonicity on the left, give
   c_{x+κ}∖(A ∪ A′ ∪ B) ≤₁ (A ∪ A′ ∪ B) ∩ d_{x+κ}. ∎

**Consequences.**
- Three-fold unions of a disjoint thin family are uniformly thin. Hence uniform escape at s₁ raises s₁ by κ along the
  family 𝒜^{(3)}.
- Iterating, along 𝒜^{(3^k)} the escape radii κ_k must be summable.
- Where uniform escape fails at x, for every κ some A ∈ 𝒜 has c_{x+κ} ≰₁ c_x ∪ A. (K) then gives
  A ∩ d_{x+κ} ≤₂ [x, x+κ)∖A: a **thin** world-2 source below a narrow slab. Lemma T₂ and any rate concern
  non-thin sources, so nothing follows. A additive world 2 accepts such comparisons too.
- So the route ends with exactly a thin residue.

### 5.4 Weakest statements still provable (PROVED)

- **(W-a)** No mirrored pair exists if either world has SP (Prop Q15, N1(c)). The modulus is now exact:
  inf{ν₂(A) : Z ≤₁ A} ≥ lim_{t↓τ(Z)} ν₂(d_t), by MP♯.
- **(W-b)** In a mirrored pair the targets cannot concentrate (Lemma T). Nor can they be carried to a slab by any
  finite chain of LF, DR or DL moves (§5.2), so any exclusion must use a comparison that is not of these types.
- **(W-c)** The ping-pong is idempotent (Loop lemma): iterating MP♯ and its mirror on initial and final segments
  produces nothing beyond N2. (Whether (K), (U), (C) have other consequences for mirrored pairs is not decided here.)
- **(W-d)** R1 and ¬R3 are the two dual "favourable-only" configurations (§2.3(ii), §2.4). Excluding both would give,
  next to an SP world, nothing new (both are already excluded there). Without an SP world, both are open.

**Status:** R1 open; R2 open (the rate route is closed by §4); R3 qualitative is equivalent to (NDL), and is open
without an SP partner.

---

## 6. Pointer for the construction side (CONJECTURE / heuristic, not claimed)

A mirrored pair needs worlds that are **spread-heavy**: thin sets spread along the whole chain must weigh at least an
initial segment (world 1) or a final segment (world 2). They must also be **closed along the chain**, i.e. pass DL and
the closed-section test of Prop Q13. Additivity along the chain direction is ruled out by NS, by the tilt example N3,
and by §5.2.

The obstruction found here suggests looking in the fibre direction for the non-additivity. Worlds of the form

  A ≤₁ B iff for every chain position the fibre-profiles satisfy a non-additive dominance,

where the dominance is invariant under rescaling the chain, are the natural candidates. Whether they have closed
sections for every model is not checked.

Their failure point, if any, will be (IB)-sum closure across fibres. Q2 §4.4 found that lexicographic shadows fail at
primary ties. This is the same place.

CONJECTURE S4.1 (no evidence either way): (NDL) holds in every system satisfying the axioms. If it fails, the
construction would also give the first system with all axioms and without a uniform strict-escape rate.

---

## 7. Status table

| Statement | Status |
|---|---|
| Theorem RATE: R3₁ ⇔ R3₂ ⇔ SR₁ ⇔ SR₂ ⇔ uniform forms ⇔ no doubly-light sequence | **PROVED** |
| §2.4 doubly-light sequences give only favourable comparisons | PROVED |
| Cor SR: R3 holds next to an SP world whose weight has ν₂(c_t) → 0 (e.g. additive) | **PROVED** |
| Prop MP♯: exact threshold τ(Z); inf μ̄(A) = 1 − τ(Z) next to μ̄ | **PROVED**; NUMERICS agree |
| Loop lemma (S(T(s)+) ≤ s; ping-pong idempotent) | PROVED |
| Example A: all axioms, world 2 = μ̄, η₁(P,1) ≤ μ̄(P)²/2 (any power, or exponentially small) | **PROVED** (via Thm witness); NUMERICS |
| Prop LIN: a linear rate excludes N4 certificates next to μ̄ | PROVED (conditional; hypothesis false in general) |
| Correction to write-up §8.5(f)(R3) | proposed (§4.3) |
| §5.2 LF transport fattens to total measure ≥ a (world 2 = μ̄) | PROVED |
| Lemma UE (uniform escape raises s₁ along 3-unions) | PROVED; inconclusive |
| (R1) mirrored simple pairs | **open** (failure report §5) |
| (R2) general certificates | open; rate route closed (§4) |
| CONJECTURE S4.1 ((NDL) always holds) | CONJECTURE |

**Hypotheses added: none.** Example A is an explicit system with every axiom verified. Prop LIN and Cor SR state their
hypotheses explicitly; these are hypotheses of the propositions, not additions to the framework.
