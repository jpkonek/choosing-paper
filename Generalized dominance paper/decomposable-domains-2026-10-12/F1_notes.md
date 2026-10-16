# F1. The auditor's claims (A)–(C) on D2 and Conjecture conj:sigmaB

15 Oct 2026. Labels: **PROVED** (full proof here, or from results the write-up marks proved and confirmed, each
named), **CHECKED** (read off a cited proof), **CONJECTURE**, **NUMERICS** (scripts in `f1py/`, run with
`python3 -I`; no proof depends on them). No assumption is added. Notation as in D2_notes §§1–3 and write-up §§2–3:
n = 2, K′ = [α′, β′] ⊆ (0,1) (weight t of world 2), U = D_{K′}, M_U, P_i, E_i(X) = X △ P_i, M (mixed part of U),
N₊, λ = μ/μ(M) on U, chain coordinate x, c_b = M ∩ {x < b}, d_b = M ∖ c_b, regular models, relevant comparisons
(write-up Def. addup(a)).

---

## 0. Outcome

| Claim | Verdict |
|---|---|
| **(A)** the far end x → 1 of D2's chain lies in the interior of U, so 1/(1−x) is not locally integrable on U | **Half right; conclusion PROVED.** The far end is **two** rays: R₊(1,0), approached from M⁺ (h₁ > 0, h₂ ↑ 0). This ray is **interior** to U. The other is the boundary ray R₊(−α′, 1−α′) of U, approached from M⁻. On every compact neighbourhood in U of a point of R₊(1,0), 1/(1−x) has infinite integral (Lemma F1.1). The write-up's sentence "blows up only … near the boundary ray of U on the side of e₂, and is bounded on every closed subcone of U" is **false**. |
| **(B)** no endorsing measure of D2's world 1 is finite on compact subsets of U | **PROVED (Theorem F1.3)**, under every reading of "endorse" with property (R) of §2.1. This includes the write-up's own reading (total costs in [0,∞]) and the cancellation reading. Every σ-finite endorser has the form φ(x)λ on M with φ nondecreasing and ∫^1 φ = ∞. The comparisons used are relevant. **Conjecture conj:sigmaB is FALSE as written** (n = 2). Under the one reading that escapes, "constrain only comparisons whose two costs are both finite", conj:sigmaB is trivially true in every system (|h|^{−2}), so that reading is not a candidate. |
| **(C)** a D2′ with every target inside one compact subset of U, trades at payoffs bounded away from zero, protected end at ∂U, and (ideally) no endorser finite on compact subsets of M | **Not constructible as stated** next to an additive world (Theorem F1.4, Corollary F1.5). Targets inside one compact subset of U that avoid near-unanimous problems lie in some c_{b₀}, b₀ < 1, and no certificate can live there. **Nearby result PROVED (Theorems F1.6, F1.8):** two explicit full systems D2′_A and D2′_B, with every non-additive trade inside one compact subset of ℝ²∖{0} on which \|h₁\|,\|h₂\| ≥ c > 0, and with target overlaps and protection at ∂U. In D2′_A (C2.1 host) no endorser is finite on compact subsets of U: the blow-up is **forced at the interior ray R₊(1,0), where no non-additive trade occurs**. In D2′_B (two-phase host, whose far end is pure ∂U) world 1 is endorsed by a density locally integrable on U. "None finite on compact subsets of M" is equivalent to "no σ-finite endorser" (F1.2). It is **impossible** for every D2-type world (F1.7), and open in general (Conjecture F1.C). |

**The main new fact (Theorem F1.2, PROVED, general).** Next to an additive world with integrable density w, every
σ-finite endorser of the other world's relevant comparisons is **chain-monotone**: ν = φ(x)·wμ on M, with φ
nondecreasing and finite on [0,1). So an endorsing density can blow up **only at the far end of the chain of
selected error sets**, and must do so wherever that end lies, whether or not any non-additive trade happens there.
Whether conj:sigmaB holds is therefore decided by the **selection** (does the chain's far end meet U?), not by where
the exotic comparisons sit.

**Repaired conjecture (suggested, CONJECTURE F1.C′).** Replace "ρ_i locally integrable on U" in conj:sigmaB by
"ρ_i locally integrable on M" (the open set of mixed problems of U). D2, D2′_A and D2′_B satisfy it. ∂D_{T₁}∖0 ⊆ M,
so it still serves the localisation route of the conj:sigmaB status note (§2.6).

---

## 1. Geometry of the chain (claim A)

Polar coordinates h = r(cos θ, sin θ). For mixed h put **T(h) := h₁/(h₁ − h₂) = cos θ/(cos θ − sin θ)**, the weight t at
which (1−t, t)·h = 0. Let θ_β := arg(β′, β′−1) ∈ (−π/2, 0) and θ_α := arg(−α′, 1−α′) ∈ (π/2, π). Then:

- U = {θ_β < θ < θ_α};
- M⁺ := {θ_β < θ < 0} (h₁ > 0 > h₂), where T = τ ∈ (β′, 1);
- M⁻ := {π/2 < θ < θ_α} (h₁ < 0 < h₂), where T = σ ∈ (0, α′);
- N₊ = {0 ≤ θ ≤ π/2}.

The function T is increasing on both arcs, with T′(θ) = (cos θ − sin θ)^{−2} ∈ [1/2, 1] on the closed arcs, since
|cos θ − sin θ| = √2|cos(θ + π/4)| ∈ [1, √2] there.

The two hosts used below are the following.
- **Host A** is the C2.1 path K_s = [α′s, β′ + (1−β′)s], i.e. D2's host. Its raw coordinate is x_A = (T − β′)/(1−β′) on
  M⁺ and x_A = T/α′ on M⁻.
- **Host B** is the two-phase path K_s = [0, β′ + 2(1−β′)s] for s ≤ ½ and K_s = [α′(2s−1), 1] for s ≥ ½. Its raw
  coordinate is x_B = (T − β′)/(2(1−β′)) on M⁺ and x_B = ½ + T/(2α′) on M⁻.

In both hosts the uniform coordinate is x := G(x_raw), with G(s) := λ{x_raw < s}.

**Lemma F1.1 (PROVED).**
- **(a) Host facts, both hosts.** For s ∈ [0,1], C_s := D_{K_s} is coherent, regular, and contained in U. Its error
  sets are E₁C_s ∩ M = {x_raw < s} (mod null), E₁C_s ∩ N₊ = ∅, and E₂C_s = M ∖ E₁C_s. The endpoints are C_0 = P₁
  and C_1 = P₂. After reindexing by b = G(s): c_b = {x < b}, λ(c_b) = b, and x pushes λ|_M to Lebesgue measure on
  [0,1). x is continuous on M. For b ∈ (0,1), K_b ⊇ K′ in its relative interior, ∂C_b ∖ 0 ⊆ U, and (LF) holds at C_b
  with N = U.
- **(b) Ends.**
  - Host A: x → 1 iff θ → 0⁻ (in M⁺, towards **R₊(1,0)**) or θ → θ_α⁻ (in M⁻, towards **R₊(−α′, 1−α′)**).
  - Host B: x → 1 iff θ → θ_α⁻ only. Points of M⁺ have x < λ(M⁺) < 1.
  - R₊(1,0) ⊆ U, because P_{K′}(1,0) = 1 − β′ > 0. R₊(−α′, 1−α′) ⊆ ∂U, because P_{K′}(−α′, 1−α′) = 0.
- **(c) Density bound at the interior ray (host A).** Fix 0 < r₁ < r₂ and η ∈ (0, |θ_β|), and put
  K_η := {r₁ ≤ |h| ≤ r₂, |θ| ≤ η}, a compact subset of U. Then for every Borel g ≥ 0 on [0,1),
  ∫_{K_η∩M} g(x) dλ ≥ κ ∫_{x(−η)}^{1} g(s) ds, with κ > 0 depending on K′, r₁, r₂ only. Likewise at θ_α in M⁻.
- **(d)** Hence ∫_{K_η} (1−x)^{−1} dλ = ∞. **1/(1−x) is not locally integrable on U.** In host B, every compact
  K ⊂ U has K ∩ M ⊆ c_{b₀} for some b₀ < 1.

*Proof.*
- **(a)** For h ∈ M⁻, m·h is increasing in t, so h ∈ D_{[l,r]} iff (1−l)h₁ + l h₂ > 0 iff T(h) < l. A world-1 error on
  M⁻ is an acceptance, so h is an error iff T(h) < l. For h ∈ M⁺, m·h is decreasing in t, so h ∈ D_{[l,r]} iff
  T(h) > r. A world-1 error there is a rejection, so h is an error iff T(h) ≤ r. Hence:
  - E₁(D_{[l,r]}) ∩ M = {h ∈ M⁻ : T < l} ∪ {h ∈ M⁺ : T ≤ r}.
  - Host A: this is {x_A ≤ s}.
  - Host B: for s ≤ ½, l = 0 and this is M⁺ ∩ {T ≤ β′ + 2(1−β′)s} = {x_B ≤ s}. For s ≥ ½, r = 1 and this is
    M⁺ ∪ {σ < α′(2s−1)} = {x_B < s} up to the null level set.

  The model D_K contains {g ≥ 0, g ≠ 0}, so it is regular and E₁ ∩ N₊ = ∅. Each mixed h is an error at exactly one
  world, so E₂ ∩ M = M ∖ E₁. Since K_s ⊇ K′, D_{K_s} ⊆ D_{K′} = U.

  Under λ, θ has density 1/|M|_ang on M (where |M|_ang := (0 − θ_β) + (θ_α − π/2)), independently of r. Since T′ is
  bounded above and below, the law of x_raw has a continuous density bounded above and below on [0,1], so G is a C¹
  bijection with G′ ≥ c > 0 and x is uniform. For the relative interiors:
  - Host A: K_b = [α′s, β′ + (1−β′)s] with 0 < s < 1, so α′s < α′ and β′ + (1−β′)s > β′.
  - Host B: K_b = [0, r] with r > β′, or K_b = [l, 1] with l < α′.

  In both cases K′ ⊆ relint K_b. The boundary rays of D_{K_b} are then {T = l} ⊆ M⁻ or R₊(0,1), and {T = r} ⊆ M⁺ or
  R₊(1,0), all in U. So every R with R △ C_b ⊆ U lies in M_U.
- **(b)** This is read off the formulas in (a) and the values of P_{K′} on the two rays.
- **(c)** On M⁺ ∩ K_η, λ(dθ × [r₁, r₂]) = ϖ dθ/|M|_ang, with ϖ := e^{−r₁²/2} − e^{−r₂²/2}. Also
  dx/dθ = G′(x_A)·T′(θ)/(1−β′) ≤ D < ∞. Change variables θ ↦ x. The M⁻ case is the same.
- **(d)** Apply (c) with g = (1−s)^{−1}. For host B, K ∩ M⁺ has x < λ(M⁺) < 1, and K ∩ M⁻ has T ≤ T₀ < α′ by
  compactness, so x < 1 uniformly on K ∩ M. ∎

NUMERICS (`f1py/geometry.out`, α′ = 0.3, β′ = 0.6):
- (1 − x_A)/|θ| → 2.309 as θ → 0⁻ on M⁺;
- the truncated integral of 1/(1−x_A) over K_{0.05} (1 ≤ |h| ≤ 2) is 0.053, 0.128, 0.203, 0.278, 0.353 at cut-offs
  10^{−2}, …, 10^{−6} (logarithmic growth);
- host B gives 0.0087 (bounded).

*So the auditor's (A) is right in substance and wrong in one detail.* D2's chain ends at two rays, and only the M⁻ one is the
"boundary ray of U on the side of e₂". D2's targets Q_g are defined through x alone (D2_notes §2), so they occupy
**both** components of every scale block. The design itself therefore places exotic mass at the interior ray as well.

---

## 2. Endorsing measures (claim B)

### 2.1 What "endorse" means for infinite measures

Let ν be a countably additive measure on U with ν ≪ μ. ν must vanish on null sets, since models are classes mod
null. Assume ν(Z) > 0 for every non-null Z. For a relevant comparison B ⪯₁ X write δ := 1_{E₁X} − 1_{E₁B}. Then
δ⁻ = E₁B ∖ E₁X and δ⁺ = E₁X ∖ E₁B. The candidate readings are:

- **(E1) total costs:** ν(E₁B) ≤ ν(E₁X) in [0, ∞]. This is the write-up's reading: Def. addup(b), Prop. D2sigma, and
  the shadow notation of §8.5.
- **(E2) cancellation:** ν(δ⁻) ≤ ν(δ⁺) in [0, ∞]. Equivalently, ∫δ dν ≥ 0 whenever it is defined, with ∞ ≥ ∞ counted
  as true. (IB) makes this the natural reading, since the ranking sees only δ.
- **(E4) both-finite only:** require ν(E₁B) ≤ ν(E₁X) only when both are finite.

**Property (R):** if ν(E₁X) < ∞, endorsement implies ν(E₁B) ≤ ν(E₁X).
- (E1) has (R) trivially.
- (E2) has (R): ν(E₁B) = ν(δ⁻) + ν(E₁B ∩ E₁X) ≤ ν(δ⁺) + ν(E₁B ∩ E₁X) = ν(E₁X).
- All arguments below use only (R). When ν(E₁B) and ν(E₁X) are both finite, every reading reduces to
  ν(δ⁻) ≤ ν(δ⁺).

**(E4) trivialises conj:sigmaB (PROVED).** Let ρ(h) := |h|^{−2} on U. It is positive and locally integrable on U.
Every coherent B has E₁B = B △ P₁ a cone (mod null). A non-null measurable cone has
ρμ-mass ∫_angles ∫_0^∞ r^{−2} e^{−r²/2} r dr dθ/2π = ∞. So under (E4) every relevant comparison is either vacuous
(E₁B non-null) or trivial (E₁B null). Hence every world of every system on M_U would satisfy conj:sigmaB under (E4),
so (E4) cannot be the conjecture's reading. This is the auditor's loophole: it is real only under (E4).

### 2.2 Chain monotonicity (general)

**Theorem F1.2 (PROVED).** Consider a two-world system on M_U with strict (G), (IB), (LA), (S), (C), in which world 2
is additive with an integrable density w > 0 (ν₂ := wμ). The selection is then nested (write-up Thm S22 / Cor MC),
with chain c_b, uniform coordinate x, and (K) at interior cuts (Lemma N0). Let ν be as in §2.1, σ-finite on M,
endorsing every relevant world-1 comparison under a reading with (R), and put ρ := dν/dν₂ on M (so 0 < ρ < ∞ a.e.).
Then:
- **(a)** ν(c_b) < ∞ for every b < 1;
- **(b)** ρ = φ∘x a.e. on M, for a nondecreasing φ: [0,1) → [0,∞) that is finite everywhere and positive on (0,1);
- **(c)** if no countably additive **bounded** measure, positive on non-null sets, endorses world 1's relevant
  comparisons, then ∫_{d_t} ρ dν₂ = ∞ for every t < 1.

*Proof.* Every comparison used below is C_b ⪯₁ X with b ∈ (0,1) and X regular. C_b ∈ C_L, so it is **relevant**.
For P ⊆ c_b and Q ⊆ d_b let X be the regular model with E₁X = (c_b ∖ P) ∪ Q. Then
ν₂(E₂X) = ν₂(d_b) − ν₂(Q) + ν₂(P). If ν₂(Q) > ν₂(P), then C_b ⋠₂ X, so **(K) gives C_b ⪯₁ X**.

- **(a)** Put P′_n := c_b ∩ {ρ ≤ n}. Since ρ < ∞ a.e., ν₂(c_b ∖ P′_n) → 0 and ν₂(d_b ∩ {ρ ≤ n}) → ν₂(d_b) > 0. Fix n
  and Q ⊆ d_b ∩ {ρ ≤ n} with ν₂(Q) > ν₂(c_b ∖ P′_n), and take P := c_b ∖ P′_n. Then C_b ⪯₁ X, and
  ν(E₁X) = ν(P′_n ∪ Q) ≤ n(ν₂(P′_n) + ν₂(Q)) < ∞. By (R), ν(c_b) ≤ ν(E₁X) < ∞.
- **(b)** Fix b ∈ (0,1) and c₁ < c₂. Suppose A := c_b ∩ {ρ > c₂} and B := d_b ∩ {ρ < c₁} are both non-null.
  - Choose ε > 0 with c₁(1+ε) < c₂, and non-null P ⊆ A, Q ⊆ B with ν₂(Q) = (1+ε)ν₂(P) (ν₂ is non-atomic).
  - Then C_b ⪯₁ X, and ν(E₁X) ≤ ν(c_b) + c₁ν₂(Q) < ∞ by (a). (R) and finite subtraction give ν(P) ≤ ν(Q).
  - But ν(P) ≥ c₂ν₂(P) > c₁(1+ε)ν₂(P) ≥ ν(Q), a contradiction.

  Hence ess sup_{c_b} ρ ≤ F(b) := ess inf_{d_b} ρ, for every b, and F is nondecreasing.
  - Off one null set, for every rational b: x(h) < b ⇒ ρ(h) ≤ F(b), and x(h) ≥ b ⇒ ρ(h) ≥ F(b). So
    F(x(h)⁻) ≤ ρ(h) ≤ F(x(h)⁺).
  - F has countably many jumps, and x_*(ν₂|_M) ≪ Lebesgue, so ρ = φ∘x a.e. with φ(s) := F(s⁺).
  - φ(s) ≤ F(b) < ∞ for s < b < 1, because ρ < ∞ a.e. on the non-null d_b. Also φ > 0 on (0,1), because ρ > 0 a.e.
- **(c)** ∫_{c_t} ρ dν₂ ≤ φ(t)ν₂(c_t) < ∞. If also ∫_{d_t} ρ dν₂ < ∞, then ν|_M + ν₂|_{N₊} is a bounded, countably
  additive measure, positive on non-null sets. Relevant comparisons see only M (E₁B, E₁X ⊆ M for regular models), so
  it endorses them all. ∎

*Remarks.*
- (b) uses only (K) and the reading. No property of world 1 beyond (K) and transitivity enters. In particular, the
  near-one clause, the generators and the location of the targets play no role.
- The comparisons trade mass across the cut between the **two** components of a fibre {x ≈ b}. This is the coupling
  that carries a blow-up at one end-ray over to the other.

### 2.3 D2 (claim B)

**Theorem F1.3 (PROVED).** In the system of Theorem D2.1 (host A, any design), let ν be as in §2.1 and endorse the
relevant world-1 comparisons under a reading with (R).
1. If ν is σ-finite on M, then ν|_M = φ(x)λ with φ as in F1.2(b) and ∫_t^1 φ = ∞ for every t < 1.
   - Consequently ν(K) = ∞ for every compact K ⊂ U that has a point of R₊(1,0) in its interior.
   - Also ν(V ∩ M⁻) = ∞ for every neighbourhood V ⊆ ℝ² of a point of R₊(−α′, 1−α′).
2. In particular, **no endorsing measure is finite on compact subsets of U**: such a measure is σ-finite on the
   σ-compact set U, and (1) applies.
3. Such σ-finite measures exist (write-up Prop. D2sigma: φ = 1/(1−x)). All of them are finite on every c_b with b < 1,
   hence on every compact subset of M.
4. Endorsing countably additive measures that are **not** σ-finite also exist. For any t ∈ (0, 1),
   ν_t := λ|_{c_t} + ∞·λ|_{d_t} (on M; λ on N₊) is one.

*Proof.*
- **(1)** F1.2(b) applies with w = 1/μ(M). D2.1 step 7 excludes every bounded endorsing weight positive on c_a, so F1.2(c)
  gives ∫_t^1 φ = ∞. Then Lemma F1.1(c) with g = φ gives ν(K_η) ≥ κ∫_{x(−η)}^1 φ = ∞, and any such K contains some
  K_η. The M⁻ statement uses the M⁻ half of F1.1(c).
- **(3)** See the referee's proof in D2_referee2 §3.1, or the general Lemma F1.7(b) below.
- **(4)** ν_t is countably additive: a countable union lies in c_t iff every piece does. It vanishes exactly on null
  sets. Let δ be relevant, so δ⁻ ⊆ c_b with b < 1, δ⁺ ⊆ d_b, and D(δ) = 0.
  - If δ⁺ meets d_t non-nully, then ν_t(δ⁺) = ∞ = ν_t(E₁X), so (E1) and (E2) hold.
  - Otherwise δ⁺ ⊆ c_t a.e. If δ⁺ is null, then δ ≤ 0 and δ = 0 by strict (G). If not, b < t, so δ⁻ ⊆ c_b ⊆ c_t and
    E₁X ⊆ c_t, where ν_t = λ is finite.
    - δ is not of generator type, since that would force δ ≥ 1_{Q_g} near 1, so δ⁺ would meet d_t.
    - Hence δ ∈ 𝒦₀ and ∫δ dλ = τ_δ(0) ≥ 0, i.e. λ(δ⁻) ≤ λ(δ⁺). ∎

**Consequences (PROVED).**
- **conj:sigmaB is false as written.** D2 (n = 2) satisfies strict (G), (IB), (LA), (S), (C). The world-1 measure the
  conjecture asks for, ρ₁μ with ρ₁ > 0 a.e. and locally integrable on U, is finite on compact subsets of U, which
  Theorem F1.3(2) excludes under (E1) and (E2).
- On host A next to world 2 = λ, the σ-finite form and the bounded form coincide. If world 1 has an endorser finite
  on one compact neighbourhood of a point of R₊(1,0), F1.3(1) gives ∫^1 φ < ∞ and hence a bounded, countably
  additive endorser.
- **Write-up text to correct:**
  - conj:sigmaB status: "blows up only as x→1, that is, near the boundary ray of U on the side of e₂, and is bounded
    on every closed subcone of U", and "Theorem D21 does not refute it".
  - D2_referee2 §3.3: the same sentence.
  - Intro / summary / Status / table rows: "the σ-finite form of N17.B′ is open (Conjecture sigmaB)".
  - Prop. D2sigma ("integrable away from that end") is correct as stated. Its reading "the protected end" should name
    both rays.

### 2.4 The repaired conjecture and T₁

- **CONJECTURE F1.C′ (suggested).** In the setting of conj:sigmaB, every world has a countably additive endorsing
  measure ρ_iμ with ρ_i > 0 a.e. and **ρ_i locally integrable on M** (the open set of mixed problems in U).
  - D2 satisfies it (1/(1−x) is finite on c_b ⊇ K ∩ M for every compact K ⊂ M).
  - D2′_A and D2′_B satisfy it (F1.8).
  - By F1.2, in two worlds next to an additive world, F1.C′ at the other world is equivalent to the existence of a
    σ-finite endorser (§5).
- **For T₁ (CHECKED by inspection, a reading).**
  - Let h ∈ ∂D_{T₁} ∖ 0. If h ≥ 0, then v_k·h > 0 for every k (the v_k are positive vectors), so h is interior to
    D_{T₁}. If h ≤ 0, then v_k·h < 0 for every k, so h is interior to the complement. Hence h has a positive and a
    negative coordinate: ∂D_{T₁} ∖ 0 ⊆ M, and M is open.
  - The localisation route of the conj:sigmaB status note therefore needs only F1.C′.
  - The far ends of edge chains at near-unanimous rays (Lemma E13 status: e.g. the e₁ ray inside (+,−,−)) are outside
    M, and e₁ ∈ int D_{T₁}, so they are away from ∂D_{T₁}.

---

## 3. Why (C) as stated cannot be built next to an additive world

**Theorem F1.4 (PROVED; inputs: Lemma N0 (K), Lemma vectorform, Cor. SR, Prop. MP♯(a)(b), all proved and confirmed
in the write-up).**
- *Setting:* the system of Theorem F1.2, with world 2 additive with integrable density w > 0, ν₂ = wμ.
- *Data:* b₀ ∈ (0,1) and a non-null S ⊆ c_{b₀}.
- *Claim:* there is θ = θ(S, b₀) > 0 such that, for every finite family of accepted world-1 comparisons P_k ≤₁ Q_k
  (i.e. 1_{Q_k} − 1_{P_k} ∈ 𝒜₁, with P_k ∩ Q_k = ∅ and P_k, Q_k ⊆ c_{b₀}) and weights w_k > 0 with
  Σ_k w_k 1_{P_k} ≥ 1_S, we have
  **Σ_k w_k ν₂(Q_k) ≥ θ.**
- *Consequence:* no D2-type certificate (Σw_k1_{P_k} = 1_S, ‖Σw_k1_{Q_k}‖_∞ ≤ ε for every ε > 0) has all its sources and
  targets in c_{b₀}.

*Proof.* Write P ≤₁ Q for 1_Q − 1_P ∈ 𝒜₁. Transitivity is closure of 𝒜₁ under {−1,0,1}-valued sums (Lemma vectorform;
D2_referee2 §1), and (G) puts every δ ≥ 0 in 𝒜₁. Hence:
- **(i) Shrinking.** P′ ⊆ P and P ≤₁ Q give P′ ≤₁ Q, since (1_Q − 1_P) + 1_{P∖P′} = 1_Q − 1_{P′}.
- **(ii) Cut move.** If Q ⊆ c_{b₀}, R ⊆ d_{b₀} and ν₂(R) > ν₂(Q), then Q ≤₁ R, by (K) at b₀ as in F1.2.
- **(iii) Chaining.** P ≤₁ Q ≤₁ R with R disjoint from P ∪ Q gives P ≤₁ R.
- **(iv) Disjoint sums.** Accepted δ's with pairwise disjoint supports sum to an accepted δ.

Now let Γ := Σ_k w_k ν₂(Q_k). Replacing w_k by min(w_k, 1) keeps Σ w 1_P ≥ 1_S and does not raise Γ. Then:

1. **Rounding.** Keep each k independently with probability w_k.
   - Each h ∈ S is missed with probability Π_{k: h∈P_k}(1 − w_k) ≤ e^{−1}, so the covered part of S has expected
     λ-mass ≥ cλ(S), with c := 1 − e^{−1}.
   - Since that mass is ≤ λ(S), it is ≥ cλ(S)/2 with probability ≥ c/2 > 1/4.
   - The kept cost Σ_{kept} ν₂(Q_k) has expectation ≤ Γ, so by Markov it is ≤ 4Γ with probability ≥ 3/4.
   - Fix an outcome J with both properties.
2. **Disjointify.** Order J = {k_1, …, k_r} and put P′_i := P_{k_i} ∖ ∪_{j<i} P_{k_j}. Then P′_i ≤₁ Q_{k_i} by (i),
   and Z := ⊔ P′_i has λ(Z) ≥ m := cλ(S)/2.
3. **Export.**
   - If Γ ≥ ν₂(d_{b₀})/8 we are done. Otherwise 4Γ < ν₂(d_{b₀})/2.
   - For small η > 0 choose pairwise disjoint R_i ⊆ d_{b₀} with ν₂(R_i) = ν₂(Q_{k_i}) + η/r.
   - Then P′_i ≤₁ R_i by (ii) and (iii), and Z ≤₁ R := ⊔R_i by (iv), with ν₂(R) ≤ 4Γ + η.
4. **Lower bound.**
   - Cor. SR applies (world 2 additive with integrable density). It gives (SR₁): s_m := inf{φ₁(P) : λ(P) ≥ m} > 0.
   - Sections are closed initial segments, so c_{s_m} ≤₁ Z ≤₁ R.
   - Prop. MP♯(a)(b) for the fixed source c_{s_m} give t* := t_{c_{s_m}} < 1 and d_{t*} ≤₂ R. World 2 being additive,
     ν₂(R) ≥ κ_m := ν₂(d_{t*}) > 0.
   - Hence 4Γ + η ≥ κ_m for every small η, and θ := min(ν₂(d_{b₀})/8, κ_m/4) works. ∎

NUMERICS (`f1py/rounding.out`):
- per-point miss probability ≤ 0.343 < 1/e;
- a good selection was found in 300/300 random and projective-plane fractional covers. In the projective covers the
  sources pairwise intersect, so no disjoint subfamily has more than one member.

**Corollary F1.5 (PROVED).** In the setting of F1.4, let K ⊂ U be compact with h₂ ≤ −c|h| on K ∩ M⁺ for some c > 0.
This is "payoffs bounded away from zero"; on K ∩ M⁻ nothing is needed. Then K ∩ M ⊆ c_{b₀} for some b₀ < 1. So no
D2-type certificate with sources in some c_a has all its targets in K. A certificate whose targets lie in one
compact subset of U must, for every c > 0, use targets with h₂ > −c|h|, i.e. targets accumulating at the
near-unanimous ray R₊(1,0).

*Proof.*
- By Prop. lattice the selected models are D_{[l(b), r(b)]}, with l, r nondecreasing. By the computation in F1.1(a),
  c_b = {M⁻ : T < l(b)} ∪ {M⁺ : T ≤ r(b)}.
- Since λ(d_b) = 1 − b → 0, we have r(b) → 1 and l(b) → α′. Otherwise a fixed non-null sector stays in every d_b.
- On K ∩ M⁺, T = h₁/(h₁ − h₂) ≤ 1/(1+c). On K ∩ M⁻, T ≤ T₀ < α′ by compactness, since T = α′ only on ∂U.
- Take b₀ ≥ a with r(b₀) ≥ 1/(1+c) and l(b₀) > T₀, and apply F1.4. ∎

So the auditor's three requirements for D2′ are inconsistent next to an additive world:
- "every target inside ONE compact subset of U";
- "payoffs bounded away from zero";
- a certificate.

Without the second requirement, the only option is targets at R₊(1,0), D2's own end (Remark F1.9). Scope: F1.4 uses
that world 2 has a strictly positive, uniformly absolutely continuous endorsing charge (Cor. SR, Prop. Q15). With
both worlds non-additive the literal (C) is **open**.

---

## 4. The nearby reachable systems D2′_A and D2′_B

### 4.1 Construction (n = 2, any K′)

- **Host.** H ∈ {A, B} as in §1, with uniform x, chain c_b, d_b, and C_L-candidates C_b (Lemma F1.1(a)).
- **Fibre coordinates.** On M⁺ put z(h) := λ(M⁺ ∩ {T < T(h)})/λ(M⁺). On M⁻ put y(h) := λ(M⁻ ∩ {T < T(h)})/λ(M⁻).
  Both are uniform under normalised λ and independent of |h|. z → 0 at the ∂U ray θ_β, and y → 1 at the ∂U ray θ_α.
- **Trade window.** Fix 0 < r₁ < r₂ and A₀ := {r₁ ≤ |h| ≤ r₂}, with ϖ := μ(|h| ∈ [r₁, r₂]). Fix z₀, y₀ ∈ (0,1) with
  sup_{z<z₀} x < inf_{y≥y₀} x. (Host B: any z₀, y₀. Host A: z₀ small and y₀ close to 1; x is increasing in T on each
  component.) Put:
  - S := M⁺ ∩ A₀ ∩ {z < z₀}, the source window, adjacent to the ∂U ray θ_β;
  - W := M⁻ ∩ A₀ ∩ {y ≥ y₀}, the target and protection window, adjacent to the ∂U ray θ_α;
  - a := sup_S x ∈ (0,1). Then S ⊆ c_a and W ⊆ d_a.

  On cl(S ∪ W) we have |h| ∈ [r₁, r₂] and |h₁|, |h₂| ≥ c|h| ≥ cr₁ > 0. So **every non-additive ingredient lies in one
  compact subset of ℝ²∖{0} with payoffs bounded away from zero**. Its closure meets ∂U but not the unanimous rays.
- **Design.**
  - Blocks: B′_m := {y ∈ [1 − 2^{−m}, 1 − 2^{−m−1})}, for m ≥ m₀ with 1 − 2^{−m₀} ≥ y₀, with u_m: B′_m → [0,1) affine.
  - The digit splitting ι, and the levels n (K_n = 2^n, primes q_n ≥ 4^n, Π_n, L_n = ⌊Π_n/K_n⌋, lines ℓ_{n,i,l}, sets
    Ŷ_{n,i,l}), are exactly as in D2_notes §2.
  - P_{n,i,l} := S ∩ {iz₀/K_n ≤ z < (i+1)z₀/K_n}.
  - Q_{n,i,l} := ∪_{m≥m₀} (W ∩ {y ∈ B′_m, u_m(y) ∈ Ŷ_{n,i,l}}).
  - 𝒢 is countable. Write g_* := 1_{Q_g} − 1_{P_g}.
- **Ranking.** λ, τ_f(t) := ∫_{M∩{x≥t}} f dλ + ∫_{N₊} f dλ and D(f) := ∫_{N₊} f dλ are as in D2. Put

  𝒦₀^W := {f : f ≥ 0 a.e. on N₊; τ_f(t) ≥ 0 ∀t ∈ [0,1]; f ≥ 0 a.e. on **W** ∩ {x ≥ b*} for some b* < 1}.

  The rules are:
  - R⁻: reject if D(δ) < 0;
  - R⁺: if D(δ) > 0, accept iff τ_δ ≥ 0 on [a,1];
  - R⁰: if D(δ) = 0, accept iff δ ∈ 𝒦₀^W or δ − g_* ∈ 𝒦₀^W for some g.

  Then X ⪯₁ Y ⟺ 1_{E₁Y} − 1_{E₁X} ∈ 𝒜₁, and X ⪯₂ Y ⟺ λ(E₂X) ≤ λ(E₂Y). The selection is p ↦ C_{p₂}.

  The protection is thus confined to the ∂U-adjacent window W, and nothing near R₊(1,0) or R₊(0,1) is protected or
  traded. D2′_H denotes this system on host H.

**Lemma F1.5′ (design properties, PROVED).**
- (D1′) P_g ⊆ S ⊆ c_a and Q_g ⊆ W ⊆ d_a.
- (D2′) λ(Q_g ∩ Q_{g′} ∩ {x ≥ t}) > 0 for all g, g′ and all t < 1. Note Q_g ⊆ W, so this is the overlap at the ∂U end.
- (D3) For every η > 0, only finitely many g have λ(P_g) ≥ η.
- (D4′) For every ε > 0 there are finitely many g and w_g > 0 with Σw_g1_{P_g} = 1_S and Σw_g1_{Q_g} ≤ ε everywhere.

*Proof.*
- (D1′) is by construction.
- **(D2′).** On M⁻, x and y are increasing functions of T that tend to 1 together, so {x ≥ t} ⊇ M⁻ ∩ {y ∈ B′_m}
  for large m. On W ∩ {y ∈ B′_m}, λ is λ(M⁻) × ϖ × Lebesgue in y, because the angle is independent of the radius. So
  λ(Q_g ∩ Q_{g′} ∩ B′_m) = λ(M⁻)ϖ 2^{−m−1} Leb(Ŷ_g ∩ Ŷ_{g′}). This is > 0: two lines of PG(2,q_n) meet, and different
  levels use independent coordinates (D2_notes §2, D2_referee2 §2.1).
- **(D3).** λ(P_{n,i,l}) = λ(M⁺)ϖz₀2^{−n}, and each level is finite.
- **(D4′).** Use weights 1/L_n at level n. Σ_{i,l}1_{P_{n,i,l}}/L_n = 1_S. Pointwise, Σ_{i,l}1_{Q_{n,i,l}}/L_n ≤
  (q_n+1)/L_n ≤ 2^{1−n}, by the incidence count of D2.2. ∎

### 4.2 Every axiom

Throughout, X is a model, A := E₁X ∩ M, N_X := N₊ ∖ X (so X is regular iff N_X is null), and for a cut b,
P := c_b ∖ A and Q := A ∖ c_b. Then E₁X = A ∪ N_X and E₂X = (M ∖ A) ∪ N_X.

**Lemma F1.6a (strict (G), (IB), preorder; PROVED).** 𝒜₁ contains every δ ≥ 0 and no δ ≤ 0 other than 0, and it is
closed under {−1,0,1}-valued sums. Hence ⪯₁ is a preorder with strict (G) and (IB) (Lemma vectorform). World 2 is
additive with density 1 w.r.t. λ, so it has strict (G) and (IB).

*Proof.*
- **(F)** If D(δ) = 0 and δ − g_* ∈ 𝒦₀^W, then for t ≥ a: τ_δ(t) ≥ τ_{g_*}(t) = λ(Q_g ∩ {x ≥ t}) ≥ 0, because
  P_g ⊆ c_a by (D1′).
- **Near-end lemma.** If δ − g_* ∈ 𝒦₀^W, then δ ≥ 1_{Q_g} a.e. on W ∩ {x ≥ t*}, with t* := max(b*, a). This holds
  because g_* = 1_{Q_g} on {x ≥ a}.
- **δ ≥ 0.** Then D(δ) ≥ 0. If D > 0, all tails are ≥ 0 (R⁺). If D = 0, δ ∈ 𝒦₀^W.
- **δ ≤ 0, δ ≠ 0.** R⁻ rejects if D < 0. Suppose D = 0.
  - δ ∈ 𝒦₀^W gives ∫_M δ = τ_δ(0) ≥ 0, so δ = 0 on M. On N₊, δ ≥ 0 and δ ≤ 0. So δ = 0, a contradiction.
  - δ − g_* ∈ 𝒦₀^W gives δ ≥ 1 on W ∩ Q_g ∩ {x ≥ t*}, which is non-null by (D2′). Impossible.
- **Sums.** Let σ = δ₁ + δ₂ be ternary. D is additive and D ≥ 0 on 𝒜₁.
  - If D(σ) > 0, each τ_{δ_i} ≥ 0 on [a,1], by R⁺ or by (F), so σ passes R⁺.
  - If D(σ) = 0, then D(δ_i) = 0, and on N₊ both δ_i are ≥ 0, hence 0.
    - 𝒦₀^W is a convex cone closed under addition (take the larger b*). So 𝒦₀^W + 𝒦₀^W ⊆ 𝒦₀^W and
      (g_* + 𝒦₀^W) + 𝒦₀^W ⊆ g_* + 𝒦₀^W.
    - Two generator translates would give σ ≥ 2 on Q_g ∩ Q_{g′} ∩ W ∩ {x ≥ t*}, which is non-null by (D2′). This
      contradicts ternarity. ∎

**Lemma F1.6b (closed world-1 sections for every model; PROVED).** Let S₁(X) := {b : C_b ⪯₁ X} and
δ_b := 1_{A∪N_X} − 1_{c_b}.
- (i) If λ(N_X) > 0, then S₁(X) = [0, min{1, ψ(a)}] with ψ(t) := t + λ(N_X) + λ(A ∩ {x ≥ t}).
- (ii) If N_X is null, S₁(X) is a closed initial segment.

*Proof.*
- **(i)** D(δ_b) = λ(N_X) > 0, so R⁺ applies. For t ≥ b the tails are ≥ 0, and for t < b, τ_{δ_b}(t) = ψ(t) − b. ψ
  is nondecreasing, since ψ(t₂) − ψ(t₁) = (t₂ − t₁) − λ(A ∩ [t₁, t₂)) ≥ 0. So the condition on [a,1] is b ≤ a or
  b ≤ ψ(a), and ψ(a) ≥ a.
- **(ii)** D(δ_b) = 0, δ_b = 0 on N₊, and S₁(X) = B₀ ∪ ⋃_g B_g.
  - **B₀ = [0, λ(A)]** (= [0,1] if A = M).
    - For b < 1, δ_b = 1_A ≥ 0 on {x ≥ b}, so the W-clause holds with b* = b. The tails read (b − t)⁺ ≤ λ(A ∩ {x ≥ t}),
      which by monotonicity of t + λ(A ∩ {x ≥ t}) is b ≤ λ(A).
    - For b = 1, δ₁ = −1_{M∖A} ∈ 𝒦₀^W iff A = M.
  - **B_g.**
    - b = 1 is excluded: δ₁ − g_* ≤ −1 on Q_g ∩ {x ≥ t} ⊆ W, which is non-null for every t by (D2′).
    - For b < 1 the clause asks Q_g ∩ {x ≥ t} ⊆ A a.e. for some t < 1 (take b* ≥ max(a, b)). This **eligibility**
      depends on A only.
    - The tail clause is (b − t)⁺ ≤ u_g(t) := λ(A ∩ {x ≥ t}) − τ_{g_*}(t).
    - *Bounds first.* At t = 0: b ≤ λ(A) + λ(P_g) − λ(Q_g). If b > a, at t = a:
      b ≤ a + λ(A ∩ d_a) − λ(Q_g) ≤ 1 − λ(Q_g). So B_g ⊆ [0, max(a, 1 − λ(Q_g))] ⊆ [0,1).
    - *Initial segment.* Let b ∈ B_g and b′ < b. For t ≥ b, u_g(t) ≥ 0. For t ∈ [b′, b), u_g(t) ≥ b − t > 0. For
      t < b′, b′ − t < b − t ≤ u_g(t).
    - *Closed.* Let b_k ↑ β with b_k ∈ B_g. Then β < 1, eligibility is unchanged, and for each t, (b_k − t)⁺ ≤ u_g(t)
      passes to the limit.
    - So B_g is ∅ or [0, β_g], with β_g ≤ λ(A) + λ(P_g).
  - **Union.** If A = M we are done. Otherwise let β₀ := λ(A) < 1 and s := sup S₁(X).
    - If s > β₀, every g with β_g > (s + β₀)/2 has λ(P_g) > (s − β₀)/2. There are finitely many such g by (D3), so
      s = max β_g is attained.
    - Otherwise S₁(X) = B₀. ∎

**Theorem F1.6 (PROVED).** For H ∈ {A, B}, D2′_H on M_U satisfies:
- strict (G), (IB), (LA);
- (S), with competitiveness on supp p and closed sections for every model at both worlds;
- (C), with C_L = {C_b : b ∈ [0,1]};
- (LF) at every interior C_b.

World 2 is additive. World 1 fails SP^reg: every bounded finitely additive ν ≥ 0 that vanishes on null sets and
endorses the relevant world-1 comparisons has ν(S) = 0. The failure is of type (M2).

*Proof.*
1. **(G), (IB):** Lemma F1.6a.
2. **Competitiveness.** C_0 = P₁ has E₁ = ∅ and C_1 = P₂ has E₂ = ∅, so both are competitive by (G). For
   b ∈ (0,1), suppose C_b ⋠₂ X, i.e. λ(Q) > λ(P) + λ(N_X).
   - If λ(N_X) > 0, R⁺ applies: tails at t ≥ b are ≥ 0, and at t < b they are ≥ λ(N_X) + λ(Q) − λ(P) > 0.
   - If N_X is null, 1_Q − 1_P ∈ 𝒦₀^W: it is ≥ 0 on {x ≥ b} ⊇ W ∩ {x ≥ b}, 0 on N₊, and has tails
     ≥ λ(Q) − λ(P) ≥ 0 below b.
   - So C_b ⪯₁ X: (K) holds for every model.
3. **Closed sections.**
   - World 2: S₂(X) = {b : λ(A ∩ d_b) ≤ λ(c_b ∖ A) + λ(N_X)}. Both sides are continuous in b, so S₂(X) is closed.
   - World 1: Lemma F1.6b.
   - p ↦ p₂ is continuous.
4. **No weak domination of C_b.** Suppose X ⪯₁ C_b and X ⪯₂ C_b, and put δ′ := 1_P − 1_{Q∪N_X}.
   - R⁻ forces N_X to be null.
   - If b = 1: X ⪯₂ P₂ forces E₂X to be null, so X = C_1.
   - If b < 1: δ′ ≤ 0 on {x ≥ b}, so δ′ − g_* ≤ −1 on Q_g ∩ {x ≥ max(a, b, b*)} ⊆ W, which is non-null by (D2′).
     So the generator branch fails. The branch δ′ ∈ 𝒦₀^W gives τ_{δ′}(b) = −λ(Q) ≥ 0, so Q is null. Then X ⪯₂ C_b
     gives λ(P) ≤ λ(Q) − λ(N_X) = 0. So X = C_b.
5. **C_L, (C), (LA)** (direct, without Thm kkm; D2_referee2 §2.5).
   - If X is regular, put b := λ(A). Then C_b ⪯₂ X with equality, and C_b ⪯₁ X by B₀. By step 4 (X ⪯₂ C_b holds),
     X ≠ C_b forces X ⋠₁ C_b, so C_b strictly dominates X.
   - If X is non-regular, put b := max(0, λ(A) − λ(N_X)). Then C_b ⪯₂ X. Also b ≤ λ(A) ≤ a + λ(A ∩ d_a) ≤ ψ(a), so
     C_b ⪯₁ X by F1.6b(i). X ⋠₁ C_b by R⁻, since D = −λ(N_X) < 0.
   - So U_L = {C_b}. Every C_b is undominated by step 4, and all are coherent, so C_L = U_L ≠ ∅. A model tied with
     C_b at both worlds equals C_b.
6. **(S):** the selection p ↦ C_{p₂} ∈ C_L, with steps 2 and 3. **(LF):** Lemma F1.1(a).
7. **Certificate.** For each g let X_g be the regular model with E₁X_g = (c_a ∖ P_g) ∪ Q_g. Then
   1_{E₁X_g} − 1_{c_a} = g_*, and g_* − g_* = 0 ∈ 𝒦₀^W, so C_a ⪯₁ X_g. This comparison is **relevant**. For a bounded ν,
   (D4′) gives ν(S) = Σw_gν(P_g) ≤ Σw_gν(Q_g) ≤ εν(M) for every ε, so ν(S) = 0.
8. **(M2).** Let f = Σλ_kδ_k ≤ 0 with λ_k > 0 and each δ_k relevant (so D(δ_k) = 0).
   - Each δ_k is ≥ 0 on W ∩ {x ≥ b_k*} (base) or ≥ 1_{Q_{g_k}} there (generator).
   - On W ∩ {x ≥ max}, f ≥ Σ_{gen} λ_k 1_{Q_{g_k}}. Since f ≤ 0, (D2′) excludes every generator term.
   - So f ∈ 𝒦₀^W, ∫f = τ_f(0) ≥ 0, and f = 0. ∎

NUMERICS (`f1py/d2prime_cell.out`). The model is an exact-integer cell model with an S-source part of c_a, W
sub-cells (PG(2,3) × PG(2,5)) in two near-one blocks, and interleaved non-W cells at the same levels. 0 failures in:
- 40 generator comparisons;
- 820 pairwise target meetings in W;
- 1040 strict-(G) tests;
- 10 835 transitivity triples (85-model adversarial pool);
- 85 initial-segment, 75 D2.4(ii)-union and 10 D2.4(i) section tests;
- 35 190 (K) tests and 35 181 no-weak-domination tests;
- 792 endorsements by a nondecreasing ρ.

A ρ that is heavy on W but light on the non-W cells of the same levels **fails** 3 relevant cut moves, exactly as
Theorem F1.2 predicts. Cuts inside the proxy near-one block are excluded, which is the known proxy artefact
(D2_referee §4).

### 4.3 Endorsement in D2′

**Lemma F1.7 (PROVED; any host, any countable design with (D2′); the "D2 architecture").**
- (a) If φ: [0,1) → [1, ∞) is nondecreasing, then ν_φ := φ(x)λ on M (λ on N₊) endorses every relevant base
  comparison under (E1) and (E2).
- (b) There is such a φ with ∫_{Q_g ∩ {x≥t}} φ dλ = ∞ for all g and all t < 1. Then ν_φ endorses **every** relevant
  comparison, is σ-finite, and is finite on every c_b, b < 1, hence on every compact subset of M.

*Proof.*
- **(a)** Take φ right-continuous (this changes it only on a λ∘x^{−1}-null countable set). A relevant δ has
  δ⁻ ⊆ c_b with b < 1 (C_1 ⪯₁ X regular forces δ ≤ 0, so δ = 0), so ∫δ⁻φ ≤ φ(b) < ∞.
  - Write φ(x) = φ(0) + ∫_{(0,1)} 1_{u≤x} dφ(u) and apply Tonelli to δ⁺ and δ⁻ separately. This gives
    ∫_M δφ(x) dλ = φ(0)τ_δ(0) + ∫ τ_δ(u) dφ(u), with the negative part finite. A base δ has τ_δ ≥ 0 and D(δ) = 0,
    so the integral is ≥ 0. That is (E2).
  - ν_φ(c_b) < ∞, so (E1) follows as well.
- **(b)** Enumerate 𝒢 = {g₁, g₂, …}, put t_m := 1 − 2^{−m} and a_{j,m} := λ(Q_{g_j} ∩ {t_m ≤ x < t_{m+1}}).
  - Let φ := A_m on [t_m, t_{m+1}), with A_m := max(A_{m−1}, 1, max{1/a_{j,m} : j ≤ m, a_{j,m} > 0}).
  - By (D2′), a_{j,m} > 0 for infinitely many m. For t < 1 pick m_t with t_{m_t} ≥ t. Then
    ∫_{Q_{g_j}∩{x≥t}} φ ≥ Σ_{m ≥ max(j, m_t)} A_m a_{j,m} ≥ #{m ≥ max(j, m_t) : a_{j,m} > 0} = ∞.
  - A generator-branch relevant δ satisfies δ ≥ 1_{Q_g} on W ∩ {x ≥ t*}, so ν_φ(δ⁺) = ∞ > ν_φ(δ⁻), and
    ν_φ(E₁X) = ∞ ≥ ν_φ(c_b).
  - A compact K ⊂ M has x(K) ⊆ [0, b₀] with b₀ < 1, by continuity of x, so ν_φ(K) ≤ φ(b₀) < ∞. ∎

(For the design of §4.1, φ = 1/(1−x) also works. On M⁻ near θ_α, 1 − x ≍ 1 − y, so each block B′_m contributes
≳ Leb(Ŷ_g) to ∫_{Q_g} φ. CHECKED.)

**Theorem F1.8 (PROVED; endorsement in D2′_H).** Let ν be a countably additive measure on U, with ν ≪ μ and ν > 0 on
non-null sets, and let it endorse the relevant world-1 comparisons of D2′_H under a reading with (R).
1. No such ν is bounded (Theorem F1.6, step 7).
2. If ν is σ-finite on M, then ν|_M = φ(x)λ with φ nondecreasing and finite on [0,1), and ∫_t^1 φ = ∞ for all t < 1
   (F1.2 + 1). So **ν blows up exactly at the far end of the chain and nowhere else**: it is finite on every c_b, b < 1.
   - ν(V ∩ M⁻) = ∞ for every neighbourhood V of every point of the ∂U ray R₊(−α′, 1−α′) (F1.1(c) on M⁻).
   - **Host A:** in addition ν(K) = ∞ for every compact K ⊂ U with a point of R₊(1,0) in its interior. **No endorsing
     measure of D2′_A is finite on compact subsets of U.** This holds although no generator, target or protected set
     comes near R₊(1,0): the blow-up there is forced through the fibre coupling of F1.2(b).
   - **Host B:** x → 1 only at θ_α ∉ U (F1.1(d)), so ν|_M is finite on compact subsets of U for every σ-finite
     endorser. N₊ is unconstrained; take ν = λ there. The
     world-1 measure of Lemma F1.7(b) is locally integrable on U. Together with ρ₂ ≡ 1, **D2′_B satisfies
     conj:sigmaB.**
3. Such σ-finite endorsers exist (F1.7(b)). They are finite on every compact subset of M. Non-σ-finite ones also
   exist: ν_t of F1.3(4), whose proof uses only D = 0, base tails and δ ≥ 1_{Q_g} near the end, all of which carry over
   verbatim.

So, for (C), **"where must an endorsing σ-finite density blow up in D2′":**
- exactly on the far end of the chain of selected error sets, i.e. on {x → 1};
- on host A that is the interior ray R₊(1,0) together with the ∂U ray R₊(−α′, 1−α′);
- on host B it is the ∂U ray alone;
- nowhere else.

The density is necessarily a nondecreasing function of x, constant on fibres, and it necessarily blows up there. The
location of the non-additive trades plays no role.

**Remark F1.9 (PROVED by the same proofs; targets in one compact subset of U).** On host A, replace W by
W′ := M⁺ ∩ A₀ ∩ {θ ≥ −η} (near R₊(1,0)), and replace y by the analogous M⁺ coordinate near θ = 0. All of §4.2 goes
through. Every target then lies in the single compact set K_η ⊂ U. Any endorser under (R) that is finite on K_η
violates the certificate directly: under (E1), first get ν(c_a) < ∞ from F1.2(a); then
ν(S) ≤ Σw_gν(Q_g) ≤ εν(K_η). This is the auditor's "targets inside one compact subset of U", and by Corollary F1.5 it
is the only way to realise it: payoffs are **not** bounded away from zero (h₂ → 0⁻).

---

## 5. "None finite on compact subsets of M"

- **Equivalence (PROVED, from F1.2).** Next to an additive world, world 1 has an endorser (as in §2.1) finite on
  compact subsets of M iff it has a σ-finite one.
  - (⇐) F1.2 gives φ(x)wμ, finite on c_{b₀} ⊇ K ∩ M.
  - (⇒) M is σ-compact; put ν₂ on N₊.
- So the auditor's ideal "kill every σ-finite rescue" is the statement that **world 1 has no σ-finite endorser at
  all**.
- **Impossible in the D2 architecture (PROVED, Lemma F1.7(b)).** This covers any host, any countable design with
  overlap at the end (which transitivity forces in that architecture), and any window W.
- **CONJECTURE F1.C.** In a full two-world system on M_U next to an additive world with integrable density, the other
  world has a σ-finite endorsing measure (equivalently, by F1.2, one of the form φ(x)wμ, and one finite on compact
  subsets of M). Evidence:
  - F1.4: certificates must reach the far end, where F1.2 lets φ be infinite.
  - F1.7: the claim holds for every D2-type world.
  - No counterexample shape is known: by F1.4 it would need certificates whose targets reach the far end but defeat
    every nondecreasing φ with ∫^1 φ = ∞.

---

## 6. Status

| Item | Statement | Label |
|---|---|---|
| F1.1 | geometry: the far end of host A is R₊(1,0) (interior) ∪ R₊(−α′,1−α′) (∂U); 1/(1−x) is not locally integrable on U; host B's end is pure ∂U | PROVED; NUMERICS |
| (A) | the auditor's claim | conclusion PROVED; "the far end is the (1,0) direction" is half of it |
| §2.1 | readings (E1)/(E2) have (R); (E4) makes conj:sigmaB trivially true (\|h\|^{−2}) | PROVED |
| F1.2 | chain monotonicity of σ-finite endorsers next to an additive world | PROVED |
| F1.3 | D2: no endorser finite on compact subsets of U; σ-finite ones are φ(x)λ with ∫^1φ = ∞; non-σ-finite ones exist | PROVED |
| conj:sigmaB | as written | **FALSE** (n = 2, D2; readings E1, E2) |
| F1.C′ | conj:sigmaB with "locally integrable on M" | CONJECTURE (D2, D2′_A, D2′_B satisfy it) |
| F1.4, F1.5 | no compact-target certificate in any c_{b₀} next to an additive world; (C) as stated is inconsistent | PROVED (from confirmed write-up results) |
| F1.6 | D2′_A, D2′_B are full systems: (G), (IB), (LA), (S), closed sections for every model, (C), C_L, (LF); world 1 fails SP^reg, type (M2) | PROVED; NUMERICS |
| F1.7 | D2-architecture worlds always have σ-finite endorsers finite on compact subsets of M | PROVED |
| F1.8 | D2′: blow-up exactly at the chain's far end; D2′_A has no endorser finite on compact subsets of U; D2′_B satisfies conj:sigmaB | PROVED |
| F1.9 | targets in one compact K_η ⊂ U at R₊(1,0) | PROVED (same proofs) |
| F1.C | σ-finite endorser always exists next to an additive world | CONJECTURE |
| literal (C) with both worlds non-additive | — | open |

**Text to revise in the write-up:**
- the conj:sigmaB statement and its status note;
- the Intro, summary, §8.5(e)/(g) and table sentences that call conj:sigmaB open or say that Thm D21 does not refute
  it;
- the "Reading" in the Prop. D2sigma status (the protected end has an interior component);
- D2_referee2 §3.3's subcone sentence.

## 7. Files (`f1py/`)

- `geometry.py` (+ `.out`): T on both arcs, the end rays, T′ bounds, x_A, x_B, (1−x_A)/|θ| near the interior ray,
  and truncated ∫_{K_η} 1/(1−x) for both hosts.
- `d2prime_cell.py` (+ `.out`): the exact cell model of D2′ (W-restricted clause, interleaved non-W cells), with the
  tests listed in §4.2, including the forced-coupling test.
- `rounding.py` (+ `.out`): the rounding step of F1.4 on random and projective fractional covers.
