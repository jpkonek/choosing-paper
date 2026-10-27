# N18: adjudication of N15 (gap closed) versus N16 (ratchet facets survive)

13 Oct 2026. Independent referee. I wrote neither note and assumed nothing in either was correct until I had checked it.

**What I read.** BRIEF6, BRIEF7; N12 (all); N14 (all, especially §§0, 2, 5, 6); R10b (Lemma D, Lemma M, Cor PL2, UVN);
R15 §6 and R18 §6 (the all-facing sign structure); N15 and N16 in full.

**What I re-derived.** Every step of N15 §§1–7, by hand. N16.1–N16.10 by hand. Priority went to the five points N15 §8
flags.

**Scripts.**
- Rerun, with output reproduced exactly: `n15py/gauge_sanity.py` and `n16py/hfp_verify.py`. The latter gives
  Λ = 0.4375 (six pairs), a sign margin of 1.56e-4, and concavity defects of 9e-11, 3e-11 and 4e-13.
- New, in `n18py/`:
  - `ratchet_anchor.py` tests N16's ratchet data against N15 Lemma 5.1;
  - `gauge_indep.py` is my own code. It checks Thm 4.2, Thm 4.3, Lemma 5.1 and Prop 5.3(a) on a gauge realisation at
    an off-centre prior, and tests Lemma 2.3 on synthetic straight-level families, with a control.

**Verdict scale.** CORRECT / CORRECT WITH REPAIR (a local fix is given here) / GAP / FALSE.

---

## 0. Summary

### 0.1 Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| **N15.1** Lemma 2.1 (exact half-planes, strips) | **CORRECT** | Convexity of {f>c} and {f≤c} from the level chords, then separation. The strip lines cannot cross in Ω |
| N15 Lemma 2.2 (monotone transverse profiles) | **CORRECT** | A half-plane missing p\* meets the normal ray in a terminal sub-ray |
| **N15 Lemma 2.3** (parallel-level sandwich) | **CORRECT** | Re-derived. A shorter proof of the upper bound is in §1.3. Tested on 6 500 synthetic points with 0 violations; the control, levels pivoting inside the disc, fails 1713/1713 |
| N15 Lemma 3.1 (caps; (e) semicontinuity) | **CORRECT** | ∂⁻ = inf of continuous functions, so usc. ∂⁺ = sup of continuous functions, so lsc. Directions verified |
| **N15.2** Lemma 4.1 (Cor PL2 on G ∌ p\*) | **CORRECT** | R10b Lemma M and Cor PL2 hold for any open connected G ⊆ Γ_v. p\* plays no role in them. The inclusion G ⊆ Γ_v via W_v(Ũ) checks |
| **N15.3** Thm 4.2 (pivot chord theorem) | **CORRECT WITH REPAIR** | Steps 0–5 check. Three repairs (§1.5): order of Steps 2–4; a cluster line must meet Ω; the sign structure for general all-facing T needs a two-line proof, given here |
| **N15.4** Thm 4.3 (no sliding edges) | **CORRECT** | A zero set with interior at p\* contradicts the cap lemma at a test prior |
| **N15.5** Lemma 5.1 (profile–rotation inequalities) | **CORRECT** | Both sides re-derived. Only S⁻ (finite, by usc) appears in the upper bound and only S⁺ (positive) in the lower bound. Brackets hold in 54/54 independent gauge cases |
| N15 Lemma 5.2 (rising sun) | **CORRECT** | |
| **N15.6** Prop 5.3(a)–(d) | **CORRECT** | (a) gives Lipschitz control without any (DD). (b) also excludes singular (Cantor-type) chord maps |
| **N15.7** §6 Steps 1–5 (sweep, window, second zoom, projectivity) | **CORRECT WITH REPAIR** | Cosmetic only: take τ₀ ∈ int J, and let σ_± lie in J for large Y. Sweep and window re-derived in full |
| **N15.8** Thm 7.1 (no T1 realisation, U-domain, i.e. evaluable models the measurable subsets of U = D_{K′}) | **CORRECT** | (PC) and (NS) are established. N12 Thm 3.1 (refereed) then applies |
| N15.9(a) Cor 7.2 (non-adjacent decomposable domains) | **CORRECT** (CHECKED-level, complete) | N14 §3(iv) gives the K̂ reduction. UVN and Cor PL2 transfer, because P_{K′} > 0 on U′ |
| N15.9(b) Cor 7.3 (charges) | **CORRECT** | Conditional on existence of interior Bayes minimisers (part (A)) |
| N15.10 numerics | **Reproduced** | Independently confirmed off-centre (`gauge_indep.py`) |
| **N16.1** level chords never meet | **CORRECT** | |
| **N16.2** angle modulus | **CORRECT** | Rhombus argument checked |
| **N16.3** limit chords; unique cluster at two-signed rays | **CORRECT** | |
| **N16.4** spirals impossible; (NS) at two-signed corners | **CORRECT** | (iii) is superseded by N15.4, which holds at every corner |
| **N16.5** ridge lemma | **CORRECT** | Its error is additive (4ρ²/r). It is therefore useless at finite distance from p\*. This is why N16 missed N15.5 (§3) |
| **N16.6** (F2) impossible | **CORRECT** | Same conclusion as N15 Prop 5.3(d) |
| N16.7(a) radial vertex motion | **CORRECT WITH REPAIR** | A slip: F vanishes on w^⊥, not on ℝw. The line ℝw is excluded because F is mirror-symmetric across it. The conclusion stands |
| N16.7(b) ridge profiles | **CORRECT** | |
| N16.8(a) | **CORRECT WITH REPAIR** | Needs α(τ₂) > 0 at some τ₂ with n(τ₂) ≠ n(τ₁), i.e. "β ≡ 0 and α ≢ 0" |
| N16.8(b) HF₁ ⇔ b″ = λb, λ ≥ 0, S(z) = −2λ | **CORRECT** (vacuous for realisations) | By N15.6(c), α > 0 a.e. So no HF₁ arc exists |
| N16.9 two-point distortion | **CORRECT** | Sz = −2w″/w with w = (z′)^{−1/2}. Checked |
| **N16.10** order-p blow-ups (CHECKED) | **Local algebra CORRECT; conclusion FALSE for realisations** | Under N16.10's own hypothesis (Lipschitz chord field), N15 Lemma 5.1 forces liminf D^±(x)/x > 0. So p > 1 is impossible, not "ratchet". With p < 1 also excluded, p = 1 |
| **N16.13** explicit ratchet model | **Numerics CORRECT; "survives every leading-order constraint" FALSE as a statement about realisations** | θ′ ∈ [0.98, 4.63] on all facets. Lemma 5.1 then demands D^±(x) ≥ c·x, while the model has D^±(x) = O(x^p). The data are not the blow-up of any realisation (§3) |
| N16.12 / CONJ N16.C1 (HF₁ infeasible) | **Moot** | HF₁ arcs cannot occur at all. C1 survives only as an abstract statement about the first-order system, and nothing needs it |
| N16 §0/§7 "N14's route C1′ fails exactly here"; remaining gap (G-osc), (G-ratchet), (G-HF₁) | **FALSE / superseded** | C1′ holds with m(t) = t at a.e. facet gamble (N15 Prop 5.3(c), §6 Step 4). (G-osc) is neutralised by N15 §6; (G-ratchet) and (G-HF₁) are excluded by N15.5–N15.6 |
| N16 §7(1) "a proof must use information beyond the leading-order blow-up at p\*" | **CORRECT** | N15 does exactly this. Lemma 5.1 uses concavity in h at priors at a fixed distance ξ from p\* |

### 0.2 Adjudication

- **N15 is right and N16 is missing a constraint.** N15's inequality is correct.
- **The missing constraint** is concavity in h at a prior q on the pivot chord λ_{τ₁}, at a fixed distance ξ from p\*.
  Three facts combine:
  1. N15 Thm 4.2 gives the strict sign change of τ ↦ Ψ(q,τ) at τ₁, so Lemma 3.1(c) makes both one-sided τ-slopes
     at q nonzero.
  2. Finite rotation speed of the chords turns a τ-distance into a transverse distance ≈ ξθ′·(τ₁ − τ₀).
  3. Lemma 2.3 gives *relative* ridge control out to |y| ≤ r₀/2 (straight level lines cannot cross λ inside
     B(p\*, r₀)). It carries the value at q back to the normal ray at p\*, with distortion factor in
     [r₀/(r₀+ξ), r₀/(r₀−ξ)].
- Hence D^±(x) ≍ x wherever θ′ ∈ (0, ∞), which is almost everywhere. A one-signed order-p > 1 profile is impossible
  there.
- **Why N16 missed it.** N16 imposed concavity only on the blow-up, and on fixed-q concavity inside the scale-t ridge
  window (§6.3). Its ridge lemma N16.5 has additive error 4ρ²/r, which carries no information at ρ = ξ fixed.

### 0.3 Justified status

On every decomposable domain whose pairs meeting U′ are non-adjacent (the U-domain in particular), the additive
core (B) for T1 is **closed**:
- no strictly guiding additive realisation exists with integral penalties, (R1), (R2) and (LF);
- no regularity of q ↦ K_q beyond its automatic Hausdorff continuity is needed;
- this holds for every ε ∈ (0,1), at every interior p\*, and for every all-facing triangle in general position.

The proof chain is N15 plus the refereed imports: N12 Lemma 2.1, Lemma 4.3 and Thm 3.1; R10b UVN and Cor PL2; N14
§3(iv).

The same holds for bounded charges vanishing on null sets, **given existence** of interior Bayes minimisers.

What remains open is §5 below.

---

## 1. N15 line by line

### 1.1 Lemma 2.1 (N15.1). CORRECT.

- **Step 2.** Choose c′ ∈ (c, min f(q_i)) ∩ I_g. This is possible because I_g = (min g_i, P_{K′}(g)) is open. Then
  q_i ∉ Π⁻_{c′}, the segment lies in int Π⁺_{c′} ∩ Ω, and f ≥ c′ > c on it.
- **Step 3.** {f ≤ c} = ∩_{c′∈(c,c+η)} Π⁻_{c′} ∩ Ω. Both inclusions are as stated.
- **Steps 4–5.** A convex open set and its relative complement in convex Ω are both convex. A weakly separating line L
  then gives {f>c} = Ω ∩ int L⁺.
- **Step 6.** Two disjoint open half-planes whose boundary lines cross at x ∈ Ω would share a wedge at x, which meets Ω.
- This is the exact form of N14's "possibly fat level set" remark.

### 1.2 Lemma 2.2. CORRECT.

A line through p\* meets an open half-plane that misses p\* in an open ray, or in nothing. So {s ≥ 0 : D⁺(s) > c} is
terminal for each c ∈ (0, sup I_g).

### 1.3 Lemma 2.3 (risk point 2). CORRECT.

**Lower bound.**
- If D⁺(s₂) > c, then L = ∂{f>c} cannot meet λ ∩ Ω. A half-plane with boundary through z ∈ λ, contained in A, equals A
  near z, which is incompatible with f → 0 at z.
- So L crosses λ only at |y₀| ≥ r₀, and crosses the normal at some s_c < s₂ (strictly, by openness).
- Its height at y is then < s₂(1 + |y|/r₀) = x. So q ∈ {f > c}, a contradiction.

**Upper bound, shorter proof.**
- H′ = {f < c} is convex. It contains the open chord {p\* + y′u : |y′| < r₀} and the point p\* + s₁′n.
- So it contains their open convex hull, a triangle whose height over y is s₁′(1 − |y|/r₀) > x.
- Hence q ∈ H′, a contradiction.

**What is used.** That the zero set is exactly λ ∩ Ω (Thm 4.2, proved later with no circularity), B(p\*, r₀) ⊆ Ω, and
f(q) ∈ I_g.

**The distortion is relative.** This is the decisive difference from N16.5 (§3).

**Numerics (`gauge_indep.py`).**
- 200 random non-crossing families, 6 500 points: 0 violations.
- Control, where the levels pivot at |Y| = r₀/2 inside the disc: 1713/1713 violations. So the test is sensitive.

### 1.4 Lemma 3.1. CORRECT.

- (b): if γ(d) = 0 with d outside cl J, concavity on [x, d] (x ∈ J) gives γ(sup J) > 0, a contradiction.
- (e), left derivative: the backward chord slope (γ(τ) − γ(τ−s))/s is nondecreasing in s, so γ′₋ = inf_s. An infimum of
  jointly continuous functions is usc.
- (e), right derivative: symmetrically, γ′₊ = sup_s, which is lsc.

### 1.5 N15.2 Lemma 4.1 and N15.3 Thm 4.2 (risk point 1).

**Lemma 4.1. CORRECT.**
- *Cor PL2 away from p\*.* R10b Lemma M is stated for any open connected G ⊆ Γ_v.
  - Its Steps 2–4 work at a boundary point Q ∈ ∂_Gβ_v with Q ∈ α_v.
  - Step 1 (local non-adjacency) is the only use of K_Q ≠ {v}, and it is vacuous when there are no d-faces.
  - Hence ∂_Gβ_v = ∅. Since β_v is open, connectedness gives G ⊆ α_v or G ⊆ β_v.
  - Nothing involves p\*. N16 §6.3 uses Cor PL2 the same way.
- *G ⊆ Γ_v.*
  - Concavity of g_q gives Ψ ≥ 0 on G × [σ₁,σ₂], hence m·w″ ≥ 0 on F_k ∩ cl Ũ once Ũ is small enough that
    F_k ∩ cl Ũ ⊆ cone h([σ₁,σ₂]).
  - Then R10b §1 applies: h = w″ + (v·h)𝟙 with v·h > 0 on U⁺. So K_q ⊆ W_v(Ũ) implies q ∈ Γ_v.
  - Shrinking R10b's ball is harmless (the w_± stay in U″).
- *Excluding α.*
  - V_j ⊆ Γ ∩ β by UVN(a) at w (U ⊆ B₁).
  - int conv(G ∪ V_j) ⊆ Γ, because for good h ∈ U⁺ the half-plane H(h) contains G ∪ V_j.
  - That set is connected and meets α and β, which contradicts the dichotomy.
- *Positivity.* v_k ∉ K_q, and W ∖ {v_k} ⊆ {m·h(τ) > 0}, because h(σ₁), h(σ₂) are independent modulo 𝟙. Compactness
  of K_q then gives Ψ > 0.

**Thm 4.2. CORRECT WITH REPAIR.**
- **Step 1 checks.** G = int(P_{σ₁} ∩ P_{σ₂}) is open, convex and nonempty. It is nonempty because
  A_{σ₁} ∩ A_{σ₂} ⊇ V_l(σ₁) ∩ V_l(σ₂) ∩ Ω. Also p\* ∈ cl G. Lemma 4.1 gives G ⊆ A_τ, so
  p\* ∈ cl A_τ ∖ A_τ = λ⁺_τ.
- **Steps 3 and 5 check as written.**
  - Step 3: a jump wedge W gives Z_{τ₀} ⊇ (p\* + W) ∪ (p\* − W) near p\*. Its convex hull is a neighbourhood of p\*,
    contradicting Step 1.
  - Step 5: the cap lemma at a test prior q ∈ A_{τ₁} ∩ D⁻ forces n_{τ₀}·(q − p\*) ≥ 0.

Repairs:
- **(R-a) Order of Steps 2–4.** Step 2 proves monotonicity separately on (0,τ_j) and on (τ_i,1). This is enough for the
  one-sided limits used in Step 3, since every τ₀ lies inside one of the two intervals. That the two monotonicity
  directions agree needs non-constancy on the overlap. That comes from Step 4, whose first half is independent and whose
  second half uses only Step 3. Say so.
- **(R-b) Last clause.** A cluster line ℓ could a priori meet Δ only at a vertex (N14 §2.2). That is impossible here:
  Ψ would then be one-signed on Ω, but A_τ and B_τ are both nonempty. So ℓ ∩ Ω ⊆ Z_τ = λ_τ ∩ Ω forces ℓ = λ_τ.
- **(R-c) Sign structure for general all-facing T.** §1 proves it only for T1. The general proof:
  - Write v_k = a e_k + b v_i + c v_j with a, b, c > 0 (all-facing; R18 §6). For h ∈ F_k this gives
    0 = h·v_k ≥ a h_k, so h_k < 0.
  - At the corners, R15 Thm 6.2 Step 2 gives r_k, r_i < 0 < r_j at r_{ki}, and symmetrically at r_{kj}.
  - h_i and h_j cannot both be ≤ 0, since then h ≤ 0 and h·v_k < 0.
  - So each of h_i, h_j crosses zero once, with τ_i < τ_j, giving the pattern (−,+), (+,+), (+,−).

### 1.6 N15.4 Thm 4.3. CORRECT.

- If n^k(0+) ≠ n^j(0+), then P(·,r) vanishes on two opposite wedges at p\*. By convexity of the zero set (Lemma 2.1,
  since r ∈ U is mixed), it vanishes on a neighbourhood B.
- A test prior q ∈ B ∩ A^k_τ with n^k(0+)·(q − p\*) < 0 has J⁺(q) bounded away from 0. Then Lemma 3.1(b) gives
  P(q,r) < 0, a contradiction.
- The vector equality fixes the orientation.

### 1.7 N15.5 Lemma 5.1 (risk point 3). CORRECT.

**D⁺ side.** The anchor q = q_{τ₀}(ξ) has coordinates (ξ cosΔ, ξ sinΔ) relative to λ_{τ₁}. Lemma 2.3 with |y| ≤ ξ and
monotone D⁺ gives the sandwich. The cap lemma at q gives

  (τ₁−τ₀)Ψ(q,τ₂)/(τ₂−τ₀) ≤ Ψ(q,τ₁) ≤ (τ₁−τ₀)∂⁺Ψ(q,τ₀).

- *Upper bound.* limsup ∂⁺Ψ(q_{τ₀},τ₀) ≤ limsup ∂⁻Ψ(q_{τ₀},τ₀) ≤ ∂⁻Ψ(q_{τ₁},τ₁) = S⁻, by usc at (q_{τ₁}, τ₁).
  Then limsup (τ₁−τ₀)/sinΔ = 1/L_\*.
- *Lower bound.* For each fixed τ₂, Ψ(q_{τ₀},τ₂)/(τ₂−τ₀) → Ψ(q_{τ₁},τ₂)/(τ₂−τ₁) by joint continuity. Since
  Ψ(q_{τ₁},τ₁) = 0, the supremum over τ₂ ↓ τ₁ is S⁺. Then liminf (τ₁−τ₀)/sinΔ = 1/L^\*.
- *Coverage.* Δ ↦ x is a continuous strict bijection near 0, so every small x is covered.
- *Products.* limsup(ab) ≤ limsup a · limsup b, and liminf(ab) ≥ liminf a · liminf b, for nonnegative factors.

**D⁻ side.**
- For a left cap, γ(τ)/(τ−τ₀) is nonincreasing and γ′₊(τ₀) ≤ γ′₋(τ₀) < 0. This gives the displayed chain.
- |∂⁺| ≥ |∂⁻| and −∂⁻ is lsc. So the left constant is |∂⁻Ψ(q′,τ₁)| > 0, positive because g_{q′} > 0 to the left of τ₁.
- The infimum over τ₂ gives |∂⁺Ψ(q′,τ₁)| on the right.

**Design point.** Only the profile at the **fixed** index τ₁ enters, and the anchors move. No uniformity in τ of any
asymptotics is assumed. This matters against N16 (§3).

**Numerics.**
- `gauge_indep.py`: p\* = (.5,.3,.2), γ = .4, six facets, three values of τ₁, ξ up to 0.95·r₀/2, both sides. 54/54
  brackets hold.
- `gauge_sanity.py` reproduced.
- Caveat: in gauge families S⁺ = S⁻ at every relint point (their normal fans do not depend on q). So numerics cannot
  discriminate the semicontinuity directions. The analytic check above is what settles them.

### 1.8 Lemma 5.2 and N15.6 Prop 5.3. CORRECT.

- (a) Lemma 5.2 is applied on two subintervals left of J and one right of J. Lemma 5.1's upper bound gives D^± ≤ C′x
  there, and Lemma 2.3 extends this to |Ψ(p\*+δ,σ)| ≤ 2C′|δ|. Concave extrapolation from the left and the
  min-of-endpoints bound then give two-sided control on J. Uniform constants: checked (`gauge_indep.py`, Lipschitz ratio
  equals C).
- (b) Lebesgue's theorem gives θ′ finite a.e. If θ′(τ) = 0 then L^\* = 0, and Lemma 5.1 gives D⁺(x)/x → ∞, which
  contradicts (a).
  - Note: this also excludes strictly increasing *singular* chord maps (θ′ = 0 a.e.). A priori those were a natural
    adversary candidate.
- (c) and (d): as written.

### 1.9 N15.7 §6 (risk point 4). CORRECT WITH REPAIR (cosmetic).

**Step 1.**
- Equi-Lipschitz in τ, with constant 2C|δ|/dist(J, ∂J′), follows from concave functions bounded by C|δ| on J′.
- (M) follows from Lemma 2.3 at scale t, since the factors r₀/(r₀ ± t|y|) → 1. N16.5 would also do.

**Step 2 (sweep).**
- Choose σ_± with sinΔ = ±3ε/Y, by continuity and strict monotonicity of θ.
- The inequalities n_{σ₊}·δ ≥ x₀ + 2.5ε > n_{σ₊}·δ′ and their mirror images hold for large Y.
- The bounds 𝒥 − o(1) ≤ G(δ,σ₊) − G(δ,σ₋) ≤ L|δ||σ₊ − σ₋| ≈ 6Lε/ϑ use only θ′(τ₀) = ϑ ∈ (0,∞).
- Then Y → ∞ and ε → 0 give 𝒥 = 0.
- Repair: take τ₀ ∈ E′ ∩ int J, so that σ_± ∈ J for large Y.

**Step 2 consequences.** φ⁻ ≤ φ⁺ by (M); equality gives continuity; squeezing gives convergence for all δ;
equi-Lipschitz convergence on the dense set E′ ∩ J gives convergence on all of J. All check.

**Step 3 (window).**
- h_Y is concave as a restriction of G(δ_Y,·).
- For σ ∈ E′ there are two estimates. First, z = n_σ·δ_Y = Y sinΔ + x₀cosΔ → x₀ + s uniformly on |s| ≤ r. Second,
  φ_σ(z) = G(zn_σ,σ) = G(zn_σ,τ₀) + O(1/Y) = φ_{τ₀}(z cosΔ) + O(1/Y).
- These agree on a dense set of s, and both sides are continuous. A uniform limit of concave functions is concave.
- So φ_{τ₀} is concave on ℝ. This is the rigorous form of N16.7(b): the rotating chord makes one facet sweep see every
  transverse position at once.

**Step 4.** α, β exist by concavity; c_τ ≤ α ≤ β ≤ C; the extension off E′ via continuity of G₂ checks; and α > 0
because a concave function ≥ 0 that vanishes at an interior point is ≡ 0.

**Step 5.**
- N12 Lemma 4.3 needs exactly: concave f_δ, the two-slope form, continuous n, α, β with α > 0 locally, and n nowhere
  locally constant (Thm 4.2). All are present.
- Affine maps a₁, a₂ with a₂ ∝₊ a₁ and non-constant direction differ by a constant factor. So the projective pencil map
  on (0,1) is well defined.
- a(0) ≠ 0, since a(0) = 0 would make the direction constant.

### 1.10 N15.8 Thm 7.1, and N15.9. CORRECT.

- (PC) and (NS) are as required by N12 Thm 3.1. The box step needs unique clusters at the witnesses, which Thm 4.2
  supplies.
- Cor 7.2 (non-adjacent domains):
  - D_{K̂_q} ∩ U = D_{K_q} ∩ U near ∂D_T, because P_{K′} > 0 on U′. So Γ_v, α_v and β_v coincide for K and K̂.
  - UVN's sign conclusions transfer.
  - Cor PL2's hypothesis (no d-face meeting G for a.e. h ∈ U⁻ ⊆ U′) is non-adjacency.
  - (★) for K̂ is N14 §3(iv).
- Cor 7.3: given N14 Thm C2, conditional on existence.

### 1.11 Audit

- Fubini appears only inside the imports (N12 Lemma 2.1, UVN, Thm 2.4).
- No "for each q, a.e. g" is upgraded silently.
- No silent regularity: Lipschitz control and a.e. differentiability of θ are derived.
- No coherence at boundary priors.
- No Bayes-at-index selection.

---

## 2. N16 lemmas N16.1–N16.10, briefly

- **N16.1–N16.3: CORRECT.**
  - N16.2: the rhombus has half-diagonals ρ/sin(α/2) and ρ/cos(α/2).
  - N16.3(c): uniqueness of the cluster needs u ∈ ℓ₀ (two-signedness) and non-crossing with ℓ_c.
- **N16.4: CORRECT.** (iii) is now subsumed by N15.4 at all corners, with no two-signedness proviso.
- **N16.5: CORRECT,** but the additive error 4ρ²/r makes it a purely infinitesimal statement.
- **N16.6: CORRECT.**
- **N16.7(a): CORRECT WITH REPAIR.**
  - The reflection-invariant lines are ℝw and the lines {w·x = a}.
  - F vanishes on w^⊥, not on ℝw.
  - ℓ_c = ℝw is excluded because F is symmetric across ℝw, so {F > c} cannot be one side of it.
- **N16.7(b): CORRECT.**
- **N16.8: (a) CORRECT WITH REPAIR** (requires α(τ₂) > 0 at a τ₂ with n(τ₂) ≠ n(τ₁)). **(b) CORRECT.** The converse
  checks: at a zero of b·δ, min(·,0) has a concave kink, and atoms of b″ lie along n ⊥ δ.
- **N16.9: CORRECT.** The integral of ŵ^{−2} for affine ŵ is (c−a)/(w(a)w(c)).
- **N16.10: local algebra CORRECT; conclusion FALSE in realisations** (§3).
- **N16.11–N16.13 numerics: reproduced.** Their interpretation is addressed in §3.

---

## 3. N15.5–N15.6 versus N16's ratchet (N16.10, N16.13)

### 3.1 Does N15's inequality exclude N16's data? Yes.

- N16.13's chord maps have θ′ ∈ [0.977, 2.728], [1.331, 2.363] and [1.673, 4.632] on the three facets
  (`ratchet_anchor.py`). They are one-signed and finite everywhere. So L_\* = L^\* = θ′ ∈ (0, ∞) at every τ.
- Lemma 5.1, negative side: liminf D⁻(x)/x ≥ |∂⁻Ψ(q′,τ₁)|·(r₀−ξ)/(r₀ξθ′) > 0. The positivity holds in **every**
  realisation, because g_{q′} > 0 left of τ₁ (Thm 4.2) and Lemma 3.1(c) applies.
- The ratchet has D⁻(x) = β x^p with p = 5. The largest anchor slope compatible with it,
  S_max(x) = (D⁻(x)/x)·r₀ξθ′/(r₀−ξ), is about 1e-16 at x = 1e-2 and about 1e-24 at x = 1e-4, at every facet, τ₁ and ξ
  tested. It tends to 0.
- Hence |∂⁻Ψ(q′,τ₁)| = 0, which is a contradiction.
- The positive side fails the same way: N16 needs D⁺ = O(x^{2p−1}), but Lemma 5.1 gives D⁺ ≥ c·x.

### 3.2 Concrete illustration (`ratchet_anchor.py`)

- Extend N16's model to the disc as a ridge, with straight levels, zero chord λ_τ and strict signs. On the positive side
  add any cut η[n_τ·x]₊^m, with m ∈ {1, 2p−1} and η ∈ {1e-3, 1e-1}.
- At anchors on λ_{0.5} at ξ = 0.05 and 0.15, τ ↦ Ψ(q,τ) violates the necessary condition of Lemma 3.1(c):
  g(τ)/(τ−τ₁) increases, by up to 3e-2 for m = 1. This happens on all three facets.
- Yet N16's own p\*-local test on the same family passes, with defect ≤ 1e-10.
- η = 0 is pinning, which is excluded by N15 Lemma 4.1 / Cor PL2. N16 §6.3 agrees.

### 3.3 Is N16 missing a constraint, or is N15's inequality wrong?

**N16 is missing a constraint. N15's inequality is right** (§1.7). The constraint is concavity in h at priors at
**fixed** distance ξ from p\* on the pivot chord, coupled to the p\*-profile by Lemma 2.3's relative ridge bound.

N16 has neither ingredient:
- its fixed-q estimate (§6.3) is run at distance t → 0, inside the window where the o(t^p) blow-up is a ridge;
- its ridge lemma N16.5 has error 4ρ²/r, which says nothing at ρ = ξ fixed.

Run at finite ξ with Lemma 2.3, N16's own §6.3 estimate becomes the contradiction: f′(τ₀+) ≤ f′(τ₀−) = 0.

**Consequence for N16.10.** Under its hypothesis that the chord field is Lipschitz, p > 1 is impossible (N15.6(c)), and
p < 1 is impossible (N16.10). So p = 1, and the ratchet regime is empty.

**What survives of the ratchet.** A one-signed profile can occur only at τ with L^\*(τ) = ∞, a null set. N15 §6 needs
only a.e. τ, and fills in the rest by continuity of G₂ and Lemma 4.3. So this is harmless.

### 3.4 N16's meta-claim, corrected

- "(G-ratchet) data are consistent with every first-order constraint at p\*" is **true**. It is the reason N16's §7(1)
  is right that blow-up data alone cannot close the gap.
- "N14 C1′ fails" is **false**:
  - by N15 Prop 5.3(c) and §6 Step 4, at a.e. facet gamble the linear-rate blow-up exists along a subsequence and is
    two-signed and bi-Lipschitz;
  - proving this needs the finite-distance information above.

---

## 4. Which brief-flagged risk points needed repair

| N15 §8 point | Outcome |
|---|---|
| 1. Cor PL2 at G ∌ p\* | Sound. Lemma M/Cor PL2 never use p\*. The W_v(Ũ) ⇒ Γ_v step and the ball shrinking check |
| 2. Lemma 2.3 | Sound. Relative distortion r₀/(r₀ ± |y|). Shorter triangle proof of the upper bound in §1.3 |
| 3. Semicontinuity in Lemma 5.1 | Sound on both sides. The usc of ∂⁻ controls the upper bound; the lsc of −∂⁻ controls the D⁻ lower bound |
| 4. Sweep and window | Sound. They need only θ′(τ₀) ∈ (0,∞), supplied a.e. by Prop 5.3(b). Cosmetic repair: τ₀ ∈ int J |
| 5. N12 Lemma 4.3 for G₂ | Sound. Every hypothesis of its proof is present |

---

## 5. Justified status, and what remains

**PROVED (N15 with the repairs of §1.5 and §1.9, and the refereed imports).** There is no strictly guiding additive
realisation of T1 with:
- every interior Bayes model a.e. unique and coherent, and T1 Bayes at an interior p\*;
- (LF) at T1;
- integral penalties;
- on any decomposable domain on which a.e. pair meeting U′ is non-adjacent (the U-domain, domains whose advice ranges
  near ∂T have two elements, full-dimensional interior K_q).

This holds:
- with **no** (DD), (DF), (ND) or (NA_w);
- for every ε ∈ (0,1), at every interior p\*;
- for every all-facing triangle in general position, including every interior ε-contamination.

**So the additive core (B) for T1 on non-adjacent domains is closed.**

**Exact remaining items** (none of them is the (DD) gap):
1. **Adjacent decomposable domains.** The box bridge needs (NA_w) near the six crossings: d-faces with K_p ⊆ g^⊥ (N14 (E4)).
   Cor PL2 also needs no d-faces meeting G.
2. **Charges.** Closed given existence of interior Bayes minimisers (N14 Thm C2). Existence is a part-(A) question.
3. **Part (A)**, the reduction from coherent-preference rankings (CP-a) to an additive field, remains as in BRIEF6.
4. **Scope.** Non-all-facing triangles (CONJECTURE R15, classes (1,2,3) and non-facing (2,2,2)) and n > 3.
   - §§2–6 of N15 apply facet by facet wherever a facet has a crossing with a shared positive coordinate on both sides.
   - So a candidate nearby result is to rerun N12 Thm 3.1's algebra for those classes, with (PC) and (NS) now free.

**Requested edits to N15:**
- (R-a) order Steps 2–4 of Thm 4.2;
- (R-b) cluster lines meet Ω;
- (R-c) the general all-facing sign structure (§1.5);
- §6: τ₀ ∈ int J;
- state in §0 that HF₁ and ratchet facets (N16) are excluded by Prop 5.3(c).

**Requested edits to N16:**
- relabel N16.10's ratchet conclusion "p > 1 impossible for realisations with finite rotation speed (N15.6)";
- withdraw "C1′ fails";
- repair N16.7(a) and N16.8(a);
- mark §7's gap as superseded.

---

## 6. Files (`n18py/`)

| File | What | Result |
|---|---|---|
| `ratchet_anchor.py` | N16.13 data: θ′ ranges; Lemma 5.1 slope budget S_max(x); ridge extension with cuts m ∈ {1, 2p−1}, tested by Lemma 3.1(c) at finite anchors | θ′ ∈ [0.98, 4.63], finite and positive. S_max ≤ 2e-15 → 0. Every cut violates concavity at the anchors, while N16's local test passes |
| `gauge_indep.py` | Own code. Gauge realisation at p\* = (.5,.3,.2), γ = .4: Thm 4.2 on circles of radius .01 and .1, monotone angle, Lemma 5.1 (both sides, 54 cases), Prop 5.3(a), corners. Synthetic Lemma 2.3 test with control | All pass. Lemma 2.3: 0/6500 violations; control 1713/1713 violations |

NUMERICS illustrate. The verdicts rest on the hand re-derivations in §§1–3.
