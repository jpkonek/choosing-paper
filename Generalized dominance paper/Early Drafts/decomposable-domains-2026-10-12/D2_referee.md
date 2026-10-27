# Referee report on D2_notes.md (Theorem D2.1: a full two-world system in which world 1 fails SP^reg)

15 Oct 2026. I started from the assumption that the claim is false and re-derived every step from the
definitions in write-up §§2–3 (axioms, M_U, regular models, Def. addup) and §8.4–8.5 (Nest, cut form, Q15, LIN,
S32–S34), C2_notes §1 (the host path), N9 (vector/normal form), N17/N19 (N17.B′), P4 §5.5 / P4B §8.5,
P3 (Thm R5) and Q1 (Q1.C1).
Scratch: `d2ref_py/` (run with `python3 -I`). No verdict here depends on the scripts.

## Summary verdict

**Theorem D2.1 is CORRECT.** I found no error that affects the theorem. There are four small gaps, each fixed in
one or two lines, plus two labelling/numerics remarks:
- step 4 at b = 1;
- the weights must be **bounded** charges, and this must be said;
- an ordering slip in Lemma D2.4(ii);
- two remarks that are labelled PROVED but are heuristic;
- the numerics test of ternary-sum closure ran only once.

The consequences hold as stated:
- N17.B′ is refuted, already as N17.B′(2), in two worlds with a nested selection;
- Q1.C1 is refuted;
- (R2) has a negative answer;
- the failure is of mode (M2).

The mechanism is genuinely new relative to the corpus. A **protected end** stops the base cone from packing mass
towards x = 1, which defeats Prop. S33(c). **Thin sources** keep every section closed: generator contributions
shrink to the base value rather than climbing to an unattained supremum, which defeats Prop. S32(d).

| Item | Verdict |
|---|---|
| (1) strict (G) for every model, including non-regular ones, under R⁺ | CORRECT |
| (2) preorder, transitivity, cancellation on all error sets; R⁺ × base cone × generators | CORRECT |
| (3) closed sections for every model at both worlds (Lemma D2.4) | CORRECT (one ordering GAP, cosmetic) |
| (4) (K)/competitiveness, undominatedness, (C), C_L, (LA), (LF) | CORRECT; GAP at b = 1 in step 4 (fixable) |
| (5) relevant comparisons carry the obstruction; design (D1)–(D4); multiplicity bound | CORRECT; GAP: "bounded" must be stated |
| (6) refutes N17.B′ / N17.B′(2), Q1.C1; (R2) negative; mode (M2) | CORRECT |
| Remarks "Why R⁺ is needed", §0 "What made it work" | overlabelled: HEURISTIC, not PROVED |
| NUMERICS | rerun identical; one artefact and one weak test noted (§7) |

## 1. Strict (G) for every model (brief item 1)

On M_U each world's advice at h ∈ U is either correct or an error, so (G) at world 1 says the following. If
1_{E₁X} ≤ 1_{E₁Y} a.e., then X ⪯₁ Y, and if moreover the difference is non-null, then Y ⋠₁ X. In acceptance
terms, 𝒜₁ contains every δ ≥ 0 and no nonzero δ ≤ 0.

The decisive point is that **acceptance depends on δ alone, never on X**, so "non-regular X" plays no role in (G).

- **δ ≥ 0.** Then D(δ) ≥ 0.
  - If D(δ) > 0, R⁺ applies and every tail of δ is ≥ 0.
  - If D(δ) = 0, then δ ∈ 𝒦₀: δ ≥ 0 everywhere, so the tails and the near-one clause hold.
- **δ ≤ 0, δ ≠ 0.** Then D(δ) ≤ 0, and D(δ) < 0 is rejected by R⁻. Suppose D(δ) = 0.
  - If δ ∈ 𝒦₀, then τ_δ(0) = ∫δ ≥ 0, so δ = 0.
  - If δ − g_* ∈ 𝒦₀, then by (D1) g_* = 1_{Q_g} on {x ≥ 1 − h₀}. So δ ≥ 1 on Q_g ∩ {x ≥ t*}, which is non-null
    by (D2) with g′ = g. This is impossible.
- **The brief's case.** Let X be non-regular and let Y add a non-null error Z ⊆ c_a ∖ E₁X.
  - Then δ = 1_Z with D(δ) = 0, so R⁺ never enters.
  - −1_Z is rejected: its total mass is negative, and near 1 it is 0 while g_* ≥ 1_{Q_g} there.
  - R⁺ affects only comparisons in which the *worse* model has strictly more unanimous-problem errors.
- **Checks.** Strict (G) passed 300 times on exactly this configuration (`d2ref_check.py`), and also 1317 + 1317
  times on random δ ≥ 0 and δ ≤ 0.

## 2. Preorder, cancellation, interaction of R⁺ with the cone and the generators (item 2)

The order is defined through δ := 1_{E₁Y} − 1_{E₁X}, and E₁ is a bijection from M_U onto the measurable subsets
of U.
- (IB) and de Finetti cancellation therefore hold on **all** error sets, not just on the cell model. This is
  N9's normal form and write-up Lemma vectorform.
- Reflexivity holds: 0 ∈ 𝒦₀.
- Transitivity follows from closure of 𝒜₁ under sums that stay {−1,0,1}-valued. I re-derived this closure for
  arbitrary ternary δ₁, δ₂, which is more than chains require.
  - Both summands are accepted, so D(δ_i) ≥ 0, and D(σ) > 0 or D(δ₁) = D(δ₂) = 0.
  - **Case D(σ) > 0.** Fact (F) applies to each summand. If δ_i is accepted by R⁺, its tails on [a,1] are ≥ 0.
    If δ_i ∈ 𝒦₀, all its tails are ≥ 0. If δ_i − g_* ∈ 𝒦₀, then τ_{δ_i} ≥ τ_{g_*} =
    λ(Q_g ∩ {x ≥ t}) − λ(P_g ∩ {x ≥ t}), and the second term vanishes for t ≥ a because P_g ⊆ c_a. This is
    exactly where the threshold a in R⁺ is needed, and it is the only interaction of R⁺ with the generators. It
    is correct.
  - **Case D(σ) = 0.** 𝒦₀ is a convex cone; the near-one clause survives addition by taking the larger b*. So
    𝒦₀ + 𝒦₀ ⊆ 𝒦₀ and (g_* + 𝒦₀) + 𝒦₀ ⊆ g_* + 𝒦₀.
  - **Two generator translates never add to a ternary function.** σ ≥ 2 on Q_g ∩ Q_{g′} ∩ {x ≥ t*}, which is
    non-null by (D2). This is the step that needs (D2) **for every t < 1**, and the multi-scale construction
    supplies it.
- **Checks.** I built an independent cell model: three scale blocks, levels q = 2, 3, and all three rule types.
  - 26,236 ternary sums of accepted vectors were accepted: 400 accepted vectors, of which 180 base-cone, 134
    generator and 86 R⁺.
  - All 2,945 constructed chains X ⪯ Y ⪯ Z gave X ⪯ Z.
  - There were 0 failures.

## 3. Closed sections for every evaluable model (item 3; Lemma D2.4)

**(i) N_X non-null.**
- D(δ_b) = λ(N_X) > 0, so R⁺ applies.
- For t < b the tail is ψ(t) − b with ψ(t) = t + λ(N_X) + λ(A ∩ {x ≥ t}).
- ψ is nondecreasing: ψ(t₂) − ψ(t₁) = (t₂ − t₁) − λ(A ∩ [t₁, t₂)) ≥ 0.
- For t ≥ b the tail is ≥ 0.
- So the R⁺ condition on [a,1] holds iff b ≤ a or b ≤ ψ(a). Since ψ(a) > a, the section is
  S₁ = [0, min(1, ψ(a))]. **CORRECT.**

**(ii) N_X null.** Then S₁ = B₀ ∪ ⋃_g B_g, and each piece behaves as follows.
- **B₀ = [0, λ(A)]** (or [0,1] if A = M). For b < 1 the near-one clause is automatic, because δ_b = 1_A on
  {x ≥ b}. The tail condition reduces to b ≤ ψ₀(0) = λ(A) by monotonicity of ψ₀(t) = t + λ(A ∩ {x ≥ t}).
  For b = 1 it forces A = M.
- **B_g.** For b < 1 the near-one clause is a condition on A alone: Q_g ∩ {x ≥ t} ⊆ A a.e. for some t < 1. It
  is independent of b because b* may be taken ≥ b. The tail clause (b − t)⁺ ≤ u_g(t) defines an initial
  segment. I re-derived this, including the region t ∈ [b′, b) where u_g ≥ b − t > 0. The value b = 1 is
  excluded.
- **Union.** Every closed initial segment B_g has β_g ≤ λ(A) + λ(P_g), from the tail at t = 0. Only finitely
  many g have λ(P_g) above any η, by (D3). So the supremum of the union is attained. **CORRECT.** Limits of
  models whose sections use ever more generators, which are the brief's "accumulating generators", are exactly
  what this step handles: those generators have λ(P_g) → 0, so they cannot push the section past
  λ(A) + o(1). The sections of the model's own limit are covered because the lemma holds for *every* model.
- **World 2.** S₂(X) = {b : λ(A ∩ d_b) ≤ λ(c_b ∖ A) + λ(N_X)}. Both sides are continuous in b, so S₂(X) is closed.

**GAP (cosmetic).** In (ii), step 3 proves "Closed" before "Bounds". The closedness argument evaluates the near-one
clause at the limit β, which requires β < 1, and that comes from the bound β_g ≤ max(a, 1 − λ(Q_g)) < 1. *Fix:*
state the bound first.

**A contrast worth recording.** Take S32's test model D = [a, a+d) ∪ [1−h, 1).
- Every generator is eligible, with β_g ≤ d + h + λ(P_g) − λ(Q_g) ↓ d + h.
- So the generator contributions *decrease* to the base value λ(D), and the section is closed.
- In S32 the sources are all of c_a, so β_F = a + d + h − μ̄(F) *increases* to an unattained supremum. Thin
  sources are what reverse the direction.

**Checks.** On an 85-cut grid:
- 80 sections were initial segments;
- 34 non-regular sections matched the formula of (i) exactly;
- 46 regular section tops were ≤ λ(A) + max λ(P_g);
- there were 0 failures.

## 4. (K), undominatedness, (C), C_L, (LA), (LF) (item 4)

- **(K) for every model.** The two cases (λ(N_X) > 0 via R⁺; N_X null via 𝒦₀, using Q ⊆ {x ≥ b} and b < 1) are
  correct. The vertices are correct: C₀ = P₁ has E₁ = ∅, and C₁ = P₂ has E₂ = ∅. **CORRECT.**
- **Step 4: no weak domination.**
  - R⁻ forces N_X to be null.
  - τ_{δ′}(b) = −λ(Q) ≥ 0 forces Q to be null.
  - World 2 then gives λ(P) ≤ 0.
  - **GAP:** the sentence "δ′ − g_* ≤ −1 on Q_g near 1" is false at b = 1, where P = M ∖ A can contain Q_g
    near 1. *Fix:* treat b = 1 separately. X ⪯₂ C₁ = P₂ gives λ(E₂X) = 0, so X = C₁. For b < 1 the sentence is
    true, since δ′ ≤ 0 on {x ≥ b}.
- **C_L.**
  - Each C_b is coherent and, by step 4, undominated. So C_b ∈ C_L directly, (S) and (LA) hold, and there is no
    circularity.
  - Thm kkm then shows that every undominated model is tied with some C_b, hence equals it.
  - So U_L = C_L = {C_b}, and (C) holds. **CORRECT.**
- **(LF) at interior C_b.** By C2.1(4): K_b ⊇ K′ strictly at both ends, so ∂C_b ∖ 0 ⊆ U, and on M_U every set
  differing from C_b inside U is evaluable. **CORRECT.**
- **Checks.** In 1500 adversarial (K) tests (target mass placed in the last block) and 1500 undominatedness tests
  there were 0 failures, once the following artefact was excluded.
  - **Artefact.** At cuts *inside* the last block, the finite proxy for the near-one clause ("≥ 0 on the last
    block") is stricter than the real clause. (K) then fails in the proxy only. I diagnosed all 3 such hits: P
    lay in the last block below b.
  - **Bearing on the author's script.** The author's T1 test draws cuts there too and passed only because P was
    sparse. The real clause is fine at every b < 1.

## 5. The obstruction (item 5; Lemmas D2.2, D2.3, step 7)

**The generator comparisons are relevant.**
- X_g, with E₁X_g = (c_a ∖ P_g) ∪ Q_g, is regular.
- 1_{E₁X_g} − 1_{c_a} = g_*, which is accepted because g_* − g_* = 0 ∈ 𝒦₀.
- C_a ∈ C_L because a ∈ (0,1).

**The design.**
- **(D1) and (D3)** hold by construction.
- **(D2)** holds by the following facts.
  - Two distinct lines of PG(2,q) meet in exactly one point, so Leb(Ŷ ∩ Ŷ′) = 1/Π.
  - One line has Leb(Ŷ) = (q+1)/Π.
  - Different levels use independent coordinates, because ι splits the binary digits by 2-adic valuation, which
    is a measure-preserving map onto [0,1)^ℕ.
  - The affine maps u_m transport λ|B_m to uniform measure, so the intersection is non-null in **every** block,
    hence near every point of x = 1.
- **(D4)**
  - Weights 1/L_n reproduce 1_{c_a} exactly.
  - A point v_n lies in exactly one cell J_π, and π lies on q+1 lines, of which at most q+1 are chosen. So the
    multiplicity is ≤ (q+1)/L_n.
  - L_n = ⌊Π/2^n⌋ ≥ q²/2^n, because (q+1)/2^n ≥ 1, so the bound is ≤ 2·2^n/q_n ≤ 2^{1−n} → 0.
  - `design_check.py` verifies the incidence facts for q ≤ 17 and the inequalities for n ≤ 11, with q_n the
    least prime ≥ 4^n, and checks K_nL_n ≤ Π_n.
- **Endorsing weights vanish on c_a.** ν(c_a) = Σ w_g ν(P_g) ≤ Σ w_g ν(Q_g) ≤ ε ν(M) for every ε. **CORRECT.**

**GAP (must be stated).** The last inequality needs **ν(M) < ∞**.
- With [0,∞]-valued finitely additive weights the conclusion is false. Put ν(S) := λ(S) if S ∩ {x ≥ t} is null
  for some t < 1, and ν(S) := ∞ otherwise.
- This ν is finitely additive, zero on null sets and positive on non-null sets.
- It endorses **every** relevant comparison:
  - if A reaches x = 1, then ν(A) = ∞;
  - otherwise only the 𝒦₀ clause can accept c_b ≤₁ A, since the generator clause forces A ⊇ Q_g near 1, and
    τ(0) ≥ 0 gives b ≤ λ(A);
  - for b = 1 the comparison forces A = M.
- The corpus convention is bounded charges: Def. addup(c) takes the countably additive part (Yosida–Hewitt), N19
  Lemma R1 says "bounded charge", and N17.B′ says "charge". So the theorem stands.
- *Fix:* write "bounded finitely additive ν ≥ 0" in step 7 and in Theorem D2.1.

**Mode (M2), proved directly here (independent of N17.3).**
- Suppose finitely many relevant δ_k and λ_k > 0 give f = Σ λ_k δ_k ≤ 0 with f ≠ 0.
- Near x = 1 each δ_k is ≥ 0, or ≥ 1_{Q_{g_k}}. So f ≤ 0 excludes every generator term.
- Then f ∈ 𝒦₀ and ∫f ≥ 0, so f = 0, a contradiction. **CORRECT.**

**Consistency with the corpus.** I re-derived each of these in D2's system.
- **φ₁(P) ≥ λ(P)** (from B₀), hence (SR₁).
- **(QC₁).** κ₁(Z) ≥ min(λ(Z)/2, min{λ(Q_g) : λ(P_g) ≥ λ(Z)/2}) > 0, by the tails at 0 and at a and by (D3).
- **No simple certificate.**
  - Generators with λ(P_g) ≤ λ(Z)/2 force λ(A) ≥ λ(Z)/2.
  - Each of the finitely many other generators forces λ(A) ≥ λ(Q_g) > 0 (tail at a).
  - Bounded overlap is impossible in both cases. This agrees with Prop. Q15.
- **Lemma T₁.** η₁(P_g, 1) ≤ λ(Q_g) ≈ h₀/q_n ≪ λ(P_g) = a2^{−n}, which agrees with Props LIN and MP♯(e).
- **S33(c) right-packing fails**, because of the near-one clause. **S34's** "infimum 0 ⇒ S32/S33 apply" is a
  pointer; neither proposition covers protected cones with thin sources.
- **No nonzero leading charge.** This agrees with Thm E2: by the protected end, no cut pair that moves mass out of
  a neighbourhood of 1 is accepted.
- **No contradiction found** with any proved statement of §8.5.

## 6. Consequences (item 6)

- **N17.B′ (N19 §4)** asks, on M_U under strict (G), (IB), (LA), (S), (C), for a charge ≥ 0 on 𝔚^reg_i that is
  strictly positive on mixed problems. D2 gives n = 2, with every hypothesis met, and every such bounded charge
  vanishes on c_a ⊆ M. **Refuted.** The nested selection makes this a counterexample to **N17.B′(2)** (P4 §5.5)
  as well.
- **Q1.C1** assumes n = 2, (Nest), and a world 2 with a strictly positive, uniformly absolutely continuous
  endorsing charge; here world 2 is λ itself. Its conclusion SP^reg₁ fails. **Refuted.**
- **(R2)** asks: "if neither world has a simple certificate, must both satisfy SP^reg?"
  - World 2 is additive, so it has no certificate.
  - World 1 has none, by Prop. Q15, re-derived directly in §5.
  - World 1 fails SP^reg. So the answer is **no**.
- **Mode.** (M2), by §5.
- **Scope, correctly stated in D2 §5.**
  - This is n = 2. It is not a cover of T1, and the n = 3 installation (CONJECTURE D2.C) is not attempted.
  - The write-up sentences "No world failing to add up has been found in a full system" (Introduction and §8.5(f)),
    the §1 summary "No such world is known in a full system for any target", and the §8.4 sentence "No system is
    known … (M1) or (M2) … together with (S)" must be revised.
  - The claim "the positive route for T1 is open again" is a reading, not a theorem. What is proved is that the
    exclusion route "N17.B′ + M0closed" fails in two worlds.

## 7. Labelling and numerics

- **Remark "Why R⁺ is needed".** The alternative system ("treated like M, with costed moves into N₊") is not
  specified, so the claimed section [0, a + r + η − κ) cannot be PROVED as written. Relabel it HEURISTIC; it is
  not used anywhere.
- **Remark "Why the protected end".** The second sentence is correct by inspection: a cut pair at b > x₀ with P in
  the protected zone and Q to its right, λ(Q) > λ(P), is rejected by world 1 and by world 2.
- **§0 "What made it work".** This is a reading (HEURISTIC). It should be labelled as such.
- **Rerun.** `python3 -I d2py/d2_check.py` reproduces `d2_check.out` byte for byte (0 failures).
- **Weak sum-closure test.** "T4 closure under ternary sums" ran **1** test: random accepted pairs are almost never
  ternary-compatible. My stress test (26,236 sums) replaces it.
- **Proxy artefact.** The T1 cut range includes cuts inside the last block, where the proxy is stricter than the
  real clause (§4); a 0-failure count there is luck, not evidence.

## 8. Requested repairs (all minor)

1. **Step 4.** Handle b = 1 through world 2: X ⪯₂ P₂ forces E₂X null.
2. **Bounded weights.** State "bounded charge" in Theorem D2.1, step 7 and §0, and note that an extended-valued
   weight (∞ on every set reaching x = 1) would endorse world 1.
3. **Lemma D2.4(ii).** Put "Bounds" before "Closed".
4. **Labels.** Relabel the "Why R⁺" remark and §0 "What made it work" as HEURISTIC.
5. **Numerics.** Restrict T1 cuts to b ≤ start of the last block, and replace T4 by a targeted sum-closure test.
6. **Write-up.** Revise the sentences listed in §6, and move N17.B′(2), Q1.C1 and (R2) to "refuted / answered
   negatively (D2)".

## Files (`d2ref_py/`)

- `d2_check_rerun.out`: the rerun of the author's script, identical to `d2py/d2_check.out`.
- `d2ref_check.py` (+ `.out`): an independent cell model, with 0 failures. It covers:
  - strict (G), including non-regular X with added c_a errors;
  - 26,236 ternary sums and 2,945 transitive chains;
  - adversarial (K) and undominatedness;
  - sections against the closed forms of D2.4.
- `design_check.py` (+ `.out`): the PG(2,q) incidence facts for q ≤ 17, and the (D4) bound and K_nL_n ≤ Π_n for
  n ≤ 11, with 0 failures.
