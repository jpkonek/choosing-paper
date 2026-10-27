# N16: the adversary side of BRIEF7. Can a realisation of T1 escape the (DD) theorem?

13 Oct 2026. Task: BRIEF7, item N16. Labels: **PROVED** (full proof written here), **CHECKED** (verified, proof
sketched), **CONJECTURE**, **NUMERICS** (evidence only). Citations: N12 (with the N14 repairs), N14 §§2, 5, 6,
R15 §§1–6, R10a Thm M, R10b Lemma D, Lemma M, Cor PL2. Scripts are in `n16py/`.

Setting throughout (N12.1, refereed CORRECT in N14 §2.1):
- the U-domain (the evaluable models are the measurable subsets of U = D_{K′}); a realisation is a credal family q ↦ K_q (q ∈ int Δ) with K_q ⊇ K′ and K_u = T = T1;
- p\* = u is taken WLOG (N12 Prop 1.3);
- property (★): for a.e. g ∈ U, {q : P(q,g) > 0} is a.e. an open vertex-respecting half-plane H(g);
- notation: P(q,g) = min_{K_q} m·g. Level chords and cluster chords are as in N12 Lemmas 2.1(b) and 2.2.

r denotes a fixed radius with cl B(u, r) ⊆ int Δ. Distances and angles are Euclidean in aff Δ.

---

## 0. Outcome

**Verdict.**
- **No realisation of T1 was found.**
- Mechanisms (F1) and (F2) fail for general reasons, and these are now proved lemmas:
  - (F2) is impossible outright;
  - (F1) in its rotational ("spiralling") form is impossible outright;
  - (F1) in its magnitude form is impossible for vertex/polygon motion and for ridge profiles.
- (F3) splits into three cases:
  - "negative-side-flat" facets are impossible (PROVED);
  - first-order half-flat facets satisfy a negative-Schwarzian constraint, and with it the T1 first-order system is
    infeasible (NUMERICS, all ε tested; analytic completion is CONJECTURE N16.C1);
  - **fully first-order-flat "ratchet" facets of order p > 1** are the one mechanism the adversary could not kill.
- For ratchet facets there is an **explicit first-order(-p) model** (ε = 0.3, any p ≥ 4.34). It satisfies every
  first-order constraint now in the literature: crossing rows, strict vertex signs, corner matching, all six
  vertex-limit box inequalities (Λ = 0.4375 for each), and concavity in h of the blow-up.
- This is **not** a realisation. It shows that the gap cannot be closed by blow-up (first-order) data alone. In
  particular N14's route C1′, which asks for two-signed continuous blow-ups, fails exactly here: the natural blow-up
  of a ratchet facet is one-signed.

**Numbered claims.**

**N16.1 (PROVED) Level chords never meet.** Let g ∈ U and c ≠ c′ be admissible levels. Then any level chords
ℓ_c, ℓ_{c′} are disjoint in int Δ. If c < c′, the open positive side of ℓ_{c′}, intersected with int Δ, lies in the
closed positive side of ℓ_c (nesting).

**N16.2 (PROVED) Angle modulus.** Let two lines both meet B(u, ρ), with ρ < r, and be disjoint inside B(u, r). Then
the angle α between them satisfies sin(α/2) ≤ ρ/r.

**N16.3 (PROVED) Limit chords without (DD).** Let h ∈ ∂D_T∖0.
- (a) If P(·,h) > 0 at points arbitrarily close to u, then all positive-level chords ℓ_c converge, as c ↓ 0, to one
  oriented line ℓ⁺(h) through u. Quantitatively, with d(c) = dist(u, ℓ_c) → 0, sin(∠(ℓ_c, ℓ⁺)/2) ≤ d(c)/r.
- (b) The same holds for negative levels when P(·,h) < 0 arbitrarily close to u; the limit is ℓ⁻(h).
- (c) If h is **two-signed** (both (a) and (b) hold), then ℓ⁺ = ℓ⁻ =: ℓ\*(h), with the same orientation, and the
  cluster set is a single line: Cl(h) = {ℓ\*(h)}.

**N16.4 (PROVED) Consequences.**
- (i) Spiralling is impossible. The level chords of every facet gamble have a limiting direction, with the
  modulus above. In particular no vertex motion of the form t(cos log t, sin log t) can occur in a realisation; this
  is (F1), rotational form.
- (ii) The uniqueness half of (PC) holds at every two-signed facet ray, with no regularity assumed.
- (iii) (NS) holds at every two-signed corner ray. So **sliding edges can occur only at corners where P(·,r) is
  one-signed near u.**

**N16.5 (PROVED) Ridge lemma.** Let h be two-signed and n = n(h) the unit normal of ℓ\*(h). For ρ ≤ r/2 and
x, x′ ∈ B(0, ρ):

 P(u+x,h) > P(u+x′,h) ⟹ n·(x − x′) > −4ρ²/r.

So P(·,h) is monotone along n, up to a quadratic shift. One-signed versions hold on the non-flat side.

**N16.6 (PROVED) (F2) is impossible.** Suppose D(δ,h) = lim_{t↓0} P(u+tδ,h)/t exists in ℝ for every δ. Then
D(δ,h) = α[n·δ]₊ − β[n·δ]₋ with α, β ≥ 0. In particular D is continuous. Hence every (DD)-failure set satisfies
Z_k ⊆ (F1) ∪ (F3), and (F3) is exactly the case αβ = 0.

**N16.7 (PROVED) Magnitude oscillation of vertex motion is impossible.**
- (a) *Radial profiles.* Suppose a vertex near v_k is the unique active minimiser for an open set of gambles, and
  moves as v_k + ρ(|x|)Lx with L invertible. Then ρ must be constant. The obstruction comes from levels c ≠ 0, not
  from the zero chords.
- (b) *Ridge profiles.* Suppose P(u+x, h(τ)) = ψ(a(τ)·x) on an arc, with ψ fixed and a affine and non-constant. Then
  ψ is concave near 0, so its one-sided slopes exist and are positive. Hence (DD) holds.

**N16.8 (PROVED) Half-flat dichotomy.** Let I ⊆ relint F_k be an open arc on which D exists and the chord direction
n is non-constant.
- (a) β ≡ 0 on I is impossible.
- (b) If α ≡ 0 and β > 0 on I (half-flat, "HF₁"), then b := βn is Lipschitz and b″ = λb, where λ ≥ 0 is a Radon
  measure. Conversely, every such b gives concave first-order data.
  - Equivalently, the chord coordinate z = b_i/b_j is a ratio of solutions of y″ = λy, so its Schwarzian is
    S(z) = −2λ ≤ 0.
  - Projective chord maps (N12's (PC)) are exactly the case λ = 0.

**N16.9 (PROVED) Two-point distortion.** If S(z) ≤ 0 on [a, c], then z′(a)z′(c)(c−a)² ≤ (z(c)−z(a))², with
equality iff z is Möbius. Half-flat chord maps therefore distort cross-ratios in one fixed direction.

**N16.10 (CHECKED) Blow-ups of order p.** Suppose P(u+tδ,h) = t^p G(δ,h) + o(t^p), with G ≢ 0, holds on an arc
whose chord direction is non-constant and Lipschitz. Then:
- G = α[n·δ]₊^p − β[n·δ]₋^p;
- p < 1 is impossible;
- p > 1 forces α ≡ 0. This is the *ratchet* regime: the vertex is never cut at order p.
- Concavity in h is then equivalent to condition (HF_p) on B = β^{1/p}n (§6). For any p > 1, (HF_p) admits chord
  maps of either Schwarzian sign.
- Exact pinning on the positive side, P(·,h) ≡ 0 there, is excluded by R10b Cor PL2. So a ratchet facet must be cut
  at some higher order, ≥ 2p − 1 by a fixed-q concavity estimate (§6.3).

**N16.11 (NUMERICS) Half-plane tests** of explicit families, over 25 random facet gambles × 4 levels on a grid near u,
plus a global vertex-respect test (`halfplane_tests.py`).
- Spiral vertex motion fails at every level.
- Radial-oscillation vertex motion passes at level 0 and fails at levels ±0.01. This is N16.7(a).
- Independent linear vertex motions fail.
- Translations T1 + L(q − u), and joins conv(· ∪ {v_1}) and conv(· ∪ T1), pass locally but fail vertex-respect
  globally (173–206 of 300 gambles).
- The gauge-mixture control passes everything (3/300 marginal failures, from the test prior being 0.995e_i rather
  than e_i).

**N16.12 (NUMERICS) The first-order T1 system** (crossings, strict signs, corners, six box inequalities), with chord
maps in a given class (`firstorder_system.py`, `signed_lambda.py`, `eps_scan.py`, `hf_sensitivity.py`).

| class | ε = 0.1 | ε = 0.3 | ε = 0.6 |
|---|---|---|---|
| LIN: min of max Λ (R15 predicts x₊²/κ = 2.3433, 3.7978, 7.3137) | 2.3433 | 3.7978 | 7.3137 |
| HF₁ (λ ≥ 0, 18 parameters): best found | 2.3433 (λ → 0) | 3.7978 (λ → 0) | 7.55 (local; never below LIN) |
| forbidden sign λ ≤ 0: best found | **0.7500** | **0.4375** | **0.1818** |

- At ε = 0.3, every allowed single bump (λ = +0.5 on one of 18 pieces) raises the re-optimised minimum, to
  3.7989–3.8960.
- Every forbidden bump (λ = −0.5) lowers it, to 3.7844–3.7977.
- So the sign of the concavity constraint (S ≤ 0) is precisely what kills HF₁.

**N16.13 (NUMERICS) An explicit first-order-consistent ratchet model** (`riccati_check.py`, `minp.py`,
`hfp_verify.py`).
- Take the box-feasible chord maps of the forbidden class at ε = 0.3 (Λ_ab = 0.4375 for all six pairs; corner
  cosines 1; crossing residuals 2·10⁻¹²; strict-sign margin 1.6·10⁻⁴ on a 4001-point grid).
- They are carried by HF_p data on all three facets for p ≥ 4.34. The minimal p is 1.39, 1.48 and 4.34 on the three
  facets.
- Direct check at p = 5, for 4000 random δ: τ ↦ −[B(τ)·δ]₋^p is concave up to round-off (relative second-difference
  defect ≤ 10⁻¹⁰).
- Controls are clearly non-concave: R ≡ 1 gives defects of about 10⁻⁶ (with h² = 6·10⁻⁸), and exponent 1.5 gives
  defects of about 10⁻².

**CONJECTURE N16.C1.** The HF₁ system for T1 is infeasible for every ε ∈ (0,1). The suggested route is the
cross-ratio distortion of N16.9, applied facet by facet to the Möbius algebra of R15 Thm 6.2.

**Exact remaining gap (§7).** On a non-adjacent domain, a realisation of T1 must have, on some facet:
- (G-osc) genuine magnitude oscillation of P(u+tδ,h)/t, without any power-law blow-up, and not of vertex/ridge type;
- or (G-flat) first-order flatness:
  - either a ratchet facet of order p > 1 (or of non-power rate), cut only at higher order;
  - or HF₁ (excluded numerically).

Ratchet facets on all three facets mean that K_q = T1 + o(|q − u|) is **stationary** at p\* to first order. No known
argument excludes this. A lemma excluding it, a *first-order plateau theorem*, would close the gap modulo (G-osc).

---

## 1. Why the half-plane condition is so restrictive (and where it is cheap)

### 1.1 Four layers of the condition

Fix a direction θ in the m-plane (a gamble g up to positive scale and 𝟙-shifts). Write f_θ(q) for the lower support
of K_q in direction θ, so that P(q, g − c𝟙) = P(q,g) − c.

**(L1) Every level, not only the zero chord.** By (★) and N12 Lemma 2.2, the level sets of f_θ contain straight
chords, at every level c in (min_i θ_i, P_{K′}(θ)). By N16.1 these chords are pairwise disjoint in int Δ. So each
q ↦ f_θ(q) is *quasi-affine*: a function of position across a non-crossing family of chords.

**(L2) All directions at once.** (L1) holds simultaneously for all θ: a 2-parameter family of quasi-affine functions.

**(L3) Coupling in θ.** For each fixed q, θ ↦ f_θ(q) must be a support function, i.e. concave in g. This is the only
link between the chord families of different gambles. It is what produces linearity (N12 Lemma 4.3), the Schwarzian
sign (N16.8) and the (HF_p) condition (§6).

**(L4) Globality and vertex respect.**
- Each chord is a full line across Δ.
- Its positive side contains e_i iff g_i > 0, strictly; e_i lies off the closed half-plane when g_i < 0.
- These are the conditions that make the corner and box constraints (R15 §§4–6) bite.

### 1.2 Dual (incidence) form (CHECKED)

**The map Ψ.** Let L = {m·g = 0} be a line in the m-plane avoiding K′. Let Ψ(L) := ∂H(g), a line in the q-plane.
- For every q, Ψ⁻¹(lines through q) must be the tangent-line family of the convex curve ∂K_q. This is because
  L ∈ C_q ⟺ P(q,g_L) = 0, and the zero set of P(·,g_L) contains the chord Ψ(L).
- Ψ must preserve, for each vertex e_i, the side on which e_i lies.

**Examples.**
- Ψ = identity is the precise model K_q = {q}.
- Gauge mixtures are the Ψ with q·f(g) linear in q.

**What the dual form shows.** The structure (points L, curves C_q) is incidence-isomorphic to the classical plane.
So:
- every pair of curves C_q, C_{q′} meets once;
- the curves C_q with q on a fixed line all pass through one point.

A realisation is therefore a homeomorphic image of the dual plane in which every line becomes a convex curve bending
the same way, and the line u\* becomes the polygonal curve dual to ∂T1. N12.7(b) and §5 below are computations in
this picture.

### 1.3 What is cheap, and what costs (NUMERICS N16.11)

Locally near u, (★) is easy to satisfy:
- translations K_q = T1 + L(q−u) make P affine in q;
- joins K_q = conv(A_q ∪ C) with a fixed C keep half-planes, because P = min(P_A, P_C) and P_C does not depend on q.

All of these fail (L4): positivity sets become empty for gambles with v·g < 0 but g_i > 0, so the vertex-sided
structure near e_i is destroyed. Gauge mixtures pass, because their q-linearity is global.

Two observations explain the failure of the (F1) candidates:
- the spiral fails (L1) already at level 0, because its zero sets are spirals;
- radial oscillation passes level 0 and fails at c ≠ 0, because (L1) at nonzero levels sees the radial profile.

---

## 2. Level chords (N16.1–N16.4)

**Proof of N16.1.**
- By N12 Lemma 2.1(b) applied to g − c𝟙, P(·,g) = c on ℓ_c ∩ int Δ. Likewise P(·,g) = c′ on ℓ_{c′} ∩ int Δ. A common
  point would carry both values.
- *Nesting.* Points of int Δ in the open positive side of ℓ_{c′} have P ≥ c′ > c. Points in the open negative side of
  ℓ_c have P ≤ c. So no point of int Δ is in both sets. ∎

**Proof of N16.2.**
- Suppose the lines meet at x with acute angle α > 0.
- The set of points within distance ρ of both lines is a rhombus centred at x, with half-diagonals ρ/sin(α/2) and
  ρ/cos(α/2). It is contained in B(x, ρ/sin(α/2)).
- u lies in this set, so |x − u| ≤ ρ/sin(α/2).
- Disjointness in B(u, r) gives |x − u| ≥ r. Hence sin(α/2) ≤ ρ/r. (Parallel lines: α = 0.) ∎

**Proof of N16.3.**

(a), first step: d(c) → 0.
- Given η > 0, choose x with |x − u| < η and P(x,h) > 0.
- For 0 < c < P(x,h), the point x has P > c, so it lies in the open positive side of ℓ_c.
- The point u has P(u,h) = 0 < c, so it lies in the open negative side.
- Hence ℓ_c separates x from u, and d(c) < η.

(a), second step: convergence.
- For 0 < c, c′ < c₀, the lines ℓ_c and ℓ_{c′} are disjoint in int Δ (N16.1), and both meet B(u, ρ₀) with
  ρ₀ = sup_{c<c₀} d(c).
- So by N16.2 their angle is ≤ 2 arcsin(ρ₀/r), which tends to 0 as c₀ → 0. With d(c) → 0, the lines converge to a
  line ℓ⁺ through u.
- The quantitative bound follows by letting c′ → 0.
- *Orientation.* For c < c′ the positive sides are nested (N16.1) and both avoid u. Two nearly parallel lines through
  B(u, ρ₀) with nested positive sides, both not containing u, have nearly equal oriented normals. So the oriented
  normals converge.

(b) is symmetric.

(c), the two limits agree.
- Positive-level and negative-level chords are disjoint in int Δ (N16.1).
- If ℓ⁺ ≠ ℓ⁻ as lines through u, then for small c > 0 > c′ the chords ℓ_c and ℓ_{c′} would cross transversally near
  u, inside int Δ.
- Orientation: open positive side of ℓ_c ∩ int Δ ⊆ closed positive side of ℓ_{c′} (nesting with c′ < c). So the two
  limits have the same orientation.

(c), uniqueness of the cluster. Let ℓ₀ ∈ Cl(h). By N12 Lemma 2.1(b), P = 0 on ℓ₀ ∩ int Δ, P ≥ 0 on the positive
side and P ≤ 0 on the negative side.
- If u ∉ ℓ₀, then u lies strictly on one side, and P is one-signed on a neighbourhood of u. This contradicts
  two-signedness. So u ∈ ℓ₀.
- ℓ₀ is disjoint in int Δ from every ℓ_c with c > 0, since the values differ.
- If ℓ₀ ≠ ℓ\*, it crosses ℓ\* transversally at u, and hence crosses ℓ_c (c small) near u. Contradiction.
- So ℓ₀ = ℓ\*. ∎

**Proof of N16.4.**
- (i) and (ii) are restatements of N16.3.
- (iii) Let r be a two-signed corner ray, and let h → r along F_k.
  - Every cluster chord of h is a limit of good chords of gambles near h. So every limit point of such chords is a
    cluster at r (diagonal argument, as in R15 Thm 1(d), step 1).
  - Cl(r) = {ℓ\*(r)}, so the facet-k chords converge to ℓ\*(r). The same holds for facet j.
  - Hence the facet maps match at r.
  - No regularity of the facet chord maps is used. ∎

**Remark (what N16.3 adds).**
- N12 Lemma 4.2 obtained unique clusters from (DD); here two-signedness alone suffices.
- The failure mode "non-unique clusters (G2)" of N12 §7 is therefore confined to one-signed rays.
- The same applies to sliding edges (G4), at corners.

**Remark (inner clusters, used in §6).** Suppose P(·,h) < 0 arbitrarily close to u, even if P ≥ 0 on a whole side.
- Every *inner* cluster of h passes through u and equals ℓ⁻(h). (Inner: a limit of chords of good g ∈ D_T, g → h.)
- Reason: u lies in the closed positive side of such a limit. If it lay strictly inside, P ≥ 0 near u, a
  contradiction.
- The crossing-row argument (N12 Thm 3.1 item 3) and the box (Thm 2.4, with witnesses taken inner) therefore need
  only "P < 0 accumulates at u" at the relevant gambles.

---

## 3. The ridge lemma and the end of (F2) (N16.5, N16.6)

**Proof of N16.5.** Let P(u+x) > P(u+x′) (h suppressed), and choose a level s strictly between them.

*Case 1: 0 lies strictly between the values.* Use ℓ\*, which passes through u and has normal n. P(u+x) > 0 puts u+x
in the open positive side (it cannot lie in the closed negative side, where P ≤ 0). Likewise u+x′ is in the open
negative side. So n·x > 0 > n·x′.

*Case 2: otherwise.* Choose s ≠ 0 with the same sign as both values.
- ℓ_s strictly separates u+x from u+x′, so it meets the segment between them and d(s) ≤ ρ.
- By N16.3(a) or (b), sin(∠/2) ≤ ρ/r, so the unit normals satisfy |ν_s − n| ≤ 2ρ/r.
- Separation gives ν_s·(x − x′) > 0. Hence n·(x − x′) > −|ν_s − n||x − x′| ≥ −(2ρ/r)(2ρ). ∎

**Proof of N16.6.**

1. *Which normal.*
   - If P(·,h) ≡ 0 near u, then D ≡ 0, which has the stated form.
   - If h is two-signed, take n = n(h).
   - If P ≥ 0 near u but positive values accumulate, take n = n⁺. Then D ≥ 0, and only positive levels are needed
     below. Symmetrically for P ≤ 0.
2. *Monotonicity.* Suppose n·δ < n·δ′ but D(δ) > D(δ′).
   - Then P(u+tδ) > P(u+tδ′) for small t.
   - N16.5 with ρ = t·max(|δ|, |δ′|) gives n·(δ − δ′) > −4tmax(|δ|,|δ′|)²/r.
   - Letting t → 0 gives n·δ ≥ n·δ′, a contradiction. So D is nondecreasing in n·δ.
3. *Constancy on lines.* Let δ, δ″ lie on {n·δ = x} with x > 0.
   - (1+η)δ″ lies on a higher line, so D(δ) ≤ D((1+η)δ″) = (1+η)D(δ″).
   - Let η → 0 and swap the roles: D(δ) = D(δ″). For x < 0 use (1−η)δ″.
   - For x = 0: ηD(−n) = D(−ηn) ≤ D(δ) ≤ D(ηn) = ηD(n), so D(δ) = 0.
4. *Conclusion.* D(δ) = Φ(n·δ) with Φ positively homogeneous and nondecreasing. Hence Φ(x) = αx for x > 0 and βx for
   x < 0, with α = D(n) ≥ 0 and β = −D(−n) ≥ 0. ∎

**Remark (what N16.6 means for N12/N14).**
- In the classification of N14 §6, (F2) ("the limit exists but is discontinuous in δ") is empty.
- Continuity of D in (DD) is automatic. The only first-order hypotheses that matter are:
  - existence of the limit, which excludes (F1);
  - α, β > 0, which excludes (F3).

---

## 4. (F1): spirals and oscillating magnitudes

### 4.1 Rotational oscillation (spirals)

**Excluded by N16.3/N16.4(i).** Suppose the level chords of some facet gamble rotated by a non-vanishing angle as the
level c → 0, e.g. from vertex motion v_k + t·R(ω log t)Lδ. That contradicts the Cauchy property, since the angle
between ℓ_c and ℓ_{c′} is ≤ 2 arcsin(max(d(c), d(c′))/r).

NUMERICS: the spiral family fails (★) at all four levels tested, in 25/25, 22/25, 23/25 and 4/25 of the gambles.

### 4.2 Magnitude oscillation of vertex motion (N16.7(a))

**Setting.** Near u, suppose:
- K_q has a vertex v_k(q) = v_k + ρ(|x|)Lx (x = q − u, L invertible on 𝟙^⊥);
- v_k(q) is the unique minimiser of m·g over K_q for g in an open set G ∋ g₀ (so that P(q,g) = v_k(q)·g there);
- the gamble levels used below are in range.

**Proof that ρ is constant.**
1. Write w = L^T g ≠ 0. The function F(x) = ρ(|x|) w·x is invariant under reflection across ℝw.
2. Put g_c := g − (v_k·g + c)𝟙. For small c ≠ 0, g_c ∈ U is mixed, because P_{K′}(g) > v_k·g (v_k ∉ K′ is the
   unique minimiser), and P(u+x, g_c) = F(x) − c near 0. By (★) (applied at nearby good gambles and passed to the
   limit, N12 Lemma 2.1(b)), {F > c} agrees a.e. on a small disc B₀ centred at 0 with an open half-plane H_c. Its
   boundary ℓ_c passes near 0, because d(c) → 0 (N16.3).
   - {F > c} is reflection-invariant, and so is B₀. So H_c and its reflection agree a.e. on B₀. Two open
     half-planes whose boundaries meet B₀ and which agree a.e. there are equal. Hence ℓ_c is reflection-invariant.
3. A reflection-invariant line other than ℝw itself (where F = 0 ≠ c) is perpendicular to w. So ℓ_c = {w·x = a_c},
   with F > c on one side and F < c on the other, a.e. By continuity, F = c on ℓ_c ∩ B₀.
4. On ℓ_c, F(x) = ρ(|x|)·a_c, so ρ(|x|) is constant for |x| ∈ [|a_c|/|w|, radius(B₀)).
5. As c → 0, a_c → 0. Hence ρ is constant on (0, ρ₀). ∎

This is the precise reason radial oscillation passes level 0 and fails at c ≠ 0 (NUMERICS N16.11). For non-radial
vertex maps, (★) at all levels on an open set of gambles makes v_k a local homeomorphism sending an open set of lines
to lines, hence projective (N12.7(a); N14 notes the restricted-direction citation gap). Hence (DD).

### 4.3 Ridge profiles (N16.7(b))

**Claim.** If P(u+x, h(τ)) = ψ(a(τ)·x) on an arc, with a affine and non-constant and ψ independent of τ, then ψ is
concave near 0.

**Proof.**
- Fix x with a(τ₀)·x = 0 and a(τ)·x ≢ 0.
- τ ↦ ψ(t a(τ)·x) is concave for every small t (concavity of P in h), and t a(τ)·x sweeps an interval
  [−t η₁, t η₂] affinely. So ψ is concave on a neighbourhood of 0.
- Concavity together with ψ(0) = 0 and ψ > 0 for positive arguments gives 0 < ψ′(0+) ≤ ψ′(0−) < ∞. So (DD) holds,
  with α = ψ′(0+) and β = ψ′(0−). ∎

**The mechanism.** The pivot chord rotates along the facet, so at a fixed prior the facet sweep sees every scale of
the profile at once. Concavity in h then forbids scale-dependent slopes.

### 4.4 What remains of (F1)

Magnitude oscillation that is neither of vertex type (a curved boundary of K_q near v_k at the relevant scales) nor of
fixed-profile ridge type. A blow-up along subsequences gives monotone ridges G = Φ_h(n(h)·δ) (N16.5, applied at scale
t_j). But Φ_h need not be homogeneous, and the concavity argument of §4.3 needs Φ_h to vary slowly in h, which is not
known. This is (G-osc).

---

## 5. (F3) at first order: half-flat facets (N16.8, N16.9, N16.12)

**Proof of N16.8(a) (β ≡ 0 is impossible).**
- Choose τ₁, τ₂ ∈ I with n(τ₁) ≠ n(τ₂), and δ with n(τ₁)·δ < 0 < n(τ₂)·δ.
- f(τ) := D(δ, h(τ)) = α(τ)[n(τ)·δ]₊ ≥ 0 is concave on I: it is a pointwise limit of the concave functions
  τ ↦ P(u+tδ, h(τ))/t.
- f(τ₁) = 0 at an interior point, and f ≥ 0. A concave function attaining its minimum at an interior point is
  constant. So f ≡ 0, contradicting f(τ₂) > 0. ∎

**Proof of N16.8(b).**
1. *Form of D.* D(δ, h(τ)) = min(b(τ)·δ, 0) with b = βn.
2. *Continuity of b.* f_δ is concave, hence continuous, for every δ. If b(τ₀)·δ < 0, then f_δ(τ) = b(τ)·δ for τ near
   τ₀, so b(τ)·δ → b(τ₀)·δ. This holds for all δ in an open half-plane, so b is continuous.
3. *Second derivative.* For a small interval J, take δ ∈ −C_J, where C_J = {δ : n(τ)·δ > 0 ∀τ ∈ J}. Then
   f_δ = b·δ on J is concave. N12 Lemma 4.3 step 3, applied to b alone, gives b locally Lipschitz and b″ = n m_b
   with m_b ≥ 0.
4. *Converse.* If b″ = λb with λ ≥ 0, then on {b·δ < 0} we have (b·δ)″ = λ b·δ ≤ 0. At a zero of b·δ, the function
   min(·, 0) has a concave kink. An atom of m_b changes b′ only along n, which is ⊥ δ at that zero. So min(b·δ, 0) is
   concave for every δ.
5. *Coordinates.* The components b_i and b_j solve y″ = λy. The chord coordinate z = b_i/b_j is a ratio of two
   solutions of y″ + Qy = 0 with Q = −λ, so S(z) = 2Q = −2λ. (Classical; distributional when λ has atoms. The
   Wronskian, i.e. the angular momentum b × b′, is conserved, so θ′ is continuous.) ∎

**Proof of N16.9.**
- Put w = (z′)^{−1/2}. Then Sz = −2w″/w. So S ≤ 0 ⟺ w is convex.
- Let ŵ be the affine function through (a, w(a)) and (c, w(c)). Then w ≤ ŵ on [a, c], so
  z(c) − z(a) = ∫ w^{−2} ≥ ∫ ŵ^{−2} = (c−a)/(w(a)w(c)) = (c−a)√(z′(a)z′(c)).
- Equality holds iff w is affine, i.e. iff z is Möbius. ∎

### 5.1 The first-order system

The data of R15 Thm 6.2, written for arbitrary chord maps: per facet k, a curve c_k(τ) ∈ 𝟙^⊥, where τ is affine
between the two corner rays of F_k.

**Constraints.**
1. Crossing rows: c_k(τ_i)_i = 0 for i ≠ k.
2. Strict signs: sign c_k(τ)_i = sign h_i(τ) for all i and τ.
3. Corners: c_k(1) ∝₊ c_{k+1}(0).
4. Six box inequalities Λ_ab ≤ 1, with Λ_ab = κ_A/κ_B. Here
   - κ_A = lim s(A)/(A_b/|A_a|), with A ∈ F_a moving from the b-crossing into A_b > 0;
   - κ_B = lim s(B)/(|B_b|/B_a), with B ∈ F_c moving from the b-crossing into B_b < 0;
   - s is the a-weight of the point where the chord crosses [e_b, e_a].

**Validity of the box formula.**
- This is N12 Thm 2.4 together with the inner-cluster remark of §2. Only chords enter.
- The formula reproduces R15 exactly: LIN gives Λ_max = x₊²/κ to 4 decimals at three values of ε. So it is not
  restricted to linear maps.
- Rates are scale-free in c and in the τ-parametrisation.
- Λ_ab·Λ_cb is purely geometric when the chord maps are differentiable at the crossings. Both b-crossings have the
  same chord, line(u, e_b), so the angular rates cancel. For T1 the product is κ⁻². Check: LIN gives
  3.7978 × 0.0504 = 0.1914, and the forbidden-class model gives 0.4375² = 0.1914 = κ⁻² at ε = 0.3.
- So the box constrains only rate *ratios*, each to the interval [κ⁻², 1]. This is why arbitrary monotone chord maps
  make the box easy (the forbidden class shows it).

**Results (NUMERICS N16.12).**
- HF₁, with λ piecewise constant (6 pieces per facet) and SLSQP from many starts: the optimiser returns λ ≡ 0 and the
  LIN value.
- The forbidden sign λ ≤ 0 (S ≥ 0) is feasible, with large slack.
- The bump sensitivities at ε = 0.3 are one-signed (see §0).

**Interpretation.** Half-flatness relaxes N12's projectivity to S ≤ 0. N16.9 shows S ≤ 0 distorts cross-ratios in one
fixed direction, and the numerics show this is exactly the direction the R15 corner and box algebra forbids.

**Suggested proof of N16.C1.**
- On each facet the four special points are the two corners and the two crossings, with derivatives at the
  crossings.
- The R15 quantities are a, 1/b and κ: Möbius invariants of (z at corners, z′ at crossings).
- N16.9 and its three-point analogues (convexity of w against its chords and tangents) turn the corner equations
  a + 1/b = κ + 1 into one-sided inequalities, and the box into two-sided bounds on rate ratios.
- What has to be checked is that the signs line up as the sensitivities indicate. This was not completed.

---

## 6. (F3) beyond first order: ratchet facets (N16.10, N16.13)

### 6.1 Order-p blow-ups (CHECKED)

Assume P(u+tδ, h) = t^p G(δ,h) + o(t^p) as t ↓ 0 (full limit) on an arc of F_k.

**Form of G.** G is homogeneous of degree p, and by N16.5 it is monotone in n·δ. Steps 2–4 of the proof of N16.6,
run with degree p, give G = α[n·δ]₊^p − β[n·δ]₋^p.

**Two-signed and p ≠ 1 is impossible** (under Lipschitz n). Fix x, and let τ₀ be the zero of τ ↦ n(τ)·x. Then
f(τ) = G(x, h(τ)) is concave, vanishes at τ₀ and changes sign there.
- p > 1: the positive branch behaves like (τ − τ₀)^p, with zero slope at τ₀. A concave function vanishing at τ₀ with
  f′(τ₀+) = 0 is ≤ 0 on the right, a contradiction.
- p < 1: the negative branch is −β|c(τ−τ₀)|^p, which is convex there. So β ≡ 0, and N16.8(a) applies.

So p > 1 forces α ≡ 0 (the ratchet regime), and p < 1 is impossible.

**Condition (HF_p).**
- With B = β^{1/p}n, concavity of τ ↦ −[B(τ)·δ]₋^p for all δ means Y := −B·δ satisfies YY″ + (p−1)Y′² ≥ 0 wherever
  Y > 0.
- Write δ = −cos φ B̂ + sin φ B̂^⊥, and use the moving frame: R = |B|, A = B′·B̂, C = B′·B̂^⊥, D = B″·B̂, E = B″·B̂^⊥.
  Then for all t = tan φ: R(D − Et) + (p−1)(A − Ct)² ≥ 0. Equivalently,

  (HF_p) R E² + 4(p−1) E A C ≤ 4(p−1) C² D.

- As p → 1 this forces E = 0 and D ≥ 0, which is N16.8(b).
- For p > 1, in terms of θ = arg B and g = G′/G with G = R^p:

  (θ″ + 2θ′g)² ≤ 4(p−1)θ′²[G″/(pG) − θ′²].

  This is a Riccati inequality g′ ≥ F(τ, g), with g²-coefficient 1/(p−1) > 0. A carrier G > 0 exists on [0,1] iff
  the forward solution from g(0) = −∞ does not blow up: a non-oscillation condition.
- Example: θ = ωτ (so z = tan ωτ, with S(z) = 2ω² > 0) is carried iff ω ≤ π√((p−1)/p). So **positive Schwarzian
  is allowed for every p > 1.**

### 6.2 The explicit model (NUMERICS N16.13)

**Construction.**
- The box-feasible forbidden-class chord maps at ε = 0.3 have total rotations 1.91, 1.84 and 2.53 rad on the three
  facets, with θ′ ≥ 0.98.
- Carriers exist for p ≥ 1.39, 1.48 and 4.34 respectively (bisection on the Riccati test).

**Direct check at p = 5.** Build B_k = R_k(cos θ_k, sin θ_k) with R_k = G_k^{1/p} from the Riccati solution.
- For 4000 random δ, τ ↦ −[B_k(τ)·δ]₋^5 is concave on a 4001-point grid, up to 10⁻¹⁰.
- Both controls fail clearly, as listed in §0.

**The resulting first-order picture.** To order t^p:
- K_{u+tδ} = T1 together with curved bulges at each vertex v_k, with lower support −[B_k(h)·δ]₋^p in facet
  directions.
- No vertex is ever cut at order p.
- The vertex v_k bulges when q moves to the negative side of its chords. These are the directions from u that point
  roughly toward e_k, since every F_k chord has e_k on its negative side.

All the constraints of §5.1 hold, with Λ = 0.4375 < 1.

### 6.3 What the ratchet model must still satisfy

**Two facts (CHECKED).**
1. *No exact pinning.* If P(·,h) ≡ 0 on the positive side for an arc of h around a crossing, then v_k ∈ K_q, and
   K_q lies in the crossing wedge, for q in an open sector.
   - That is O ⊆ int α_{v_k} ∩ Γ_{v_k} in R10b's notation.
   - On the U-domain (advice ranges {+,0}) R10b Cor PL2 applies and gives a contradiction. Its proof needs an
     open O, not a neighbourhood of p\*.
   - So the positive side must be cut at some higher order.
2. *Order of the cut.* Fixed-q concavity in τ, with the zero at τ₀(q), gives the following.
   - For τ > τ₀: f(τ) ≤ f′(τ₀+)(τ−τ₀).
   - For τ < τ₀: |f(τ)| ≥ f′(τ₀+)|τ − τ₀|.
   - Where the ridge approximation holds (|τ − τ₀| ≳ t), the negative side is ≈ βt^p|c(τ−τ₀)|^p. Comparing at
     |τ − τ₀| ≈ Kt gives f′(τ₀+) ≲ t^{2p−1}.
   - Hence the positive side is O(t^{2p−1}).

**Status.** Neither fact excludes the model. Whether a *global* family realises such data, with (★) for every gamble
at every level and vertex models conv(K′ ∪ e_i), is open. The adversary did not construct one.

Two natural constructions fail:
- reparametrising gauge mixtures by a map σ with Dσ(u) = 0: σ must preserve an open set of lines, hence is
  projective with invertible derivative;
- joins with fixed sets: these violate (L4), N16.11.

---

## 7. Exact remaining gap, and what a proof must use

**Combined statement.** Combine N12 Thm 4.5 (with N14), N14 §§5.2–5.3, and N16.3–N16.10. A realisation of T1 on a
non-adjacent domain must have a facet F_k and a non-isolated set of rays on which one of the following holds:
- **(G-osc)** P(u+tδ,h)/t oscillates in magnitude, with no power-law blow-up. Rotation is excluded (N16.4), and so
  are vertex and ridge types (N16.7).
- **(G-HF₁)** α ≡ 0 < β at first order. By N16.8 this is S ≤ 0 chord maps. Excluded for T1 numerically at
  ε = 0.1, 0.3, 0.6; CONJECTURE N16.C1 for all ε.
- **(G-ratchet)** First-order flat (D ≡ 0). The natural blow-up is one-signed (ratchet, order p > 1 or a non-power
  rate), and the cut on the positive side is of higher order (≥ 2p − 1, and not ≡ 0 by R10b Cor PL2).

In addition, sliding edges and non-unique clusters can occur only at one-signed rays (N16.4).

**Consequences for N15 (the proof side).**
- (1) A proof via blow-ups (N14 C1′) cannot work as stated. In (G-ratchet) the blow-up exists and is continuous but
  one-signed, and N16.13 shows that one-signed blow-up data are consistent with every first-order constraint for T1.
  A proof must use information beyond the leading-order blow-up at p\*.
- (2) The most promising missing ingredient is a **first-order plateau theorem**, extending R10b Thm PL / Cor PL2
  from exact pinning to near-pinning. In R10b's notation, it would exclude the following on a whole side of the
  pivot chords:
  - v_k ∈ K_q up to o(|q−u|);
  - K_q ⊆ W_{v_k} up to o(|q−u|).
  R10b's mechanism transports pinning along segments toward a vertex neighbourhood V_j (Lemmas M, P). A quantitative
  version would control how the cut order (≥ 2p − 1) propagates along such segments.
- (3) If (2) is unavailable, the adversary's next step would be a global family whose facet support functions are
  fully flat at u: K_q = T1 + O(|q−u|^p) with ratchet bulges. The dual-incidence picture (§1.2) is the natural place
  to look: a homeomorphism Φ of the dual plane, flat to order p along u\*, mapping lines to convex curves. N12.7(b)'s
  curvature computation shows that the transversal degeneracy w = 0 escapes the second-order Möbius argument. The
  sign problem found there for quadratic flatness, where Y must be odd in y, is what the one-signed ratchet resolves.
  This was not attempted to completion.

**Honest scope.**
- Everything in §§2–5 is on the U-domain (or any non-adjacent domain), for integral penalties, or for
  charges given existence of interior Bayes minimisers (N14 Thm C2).
- §6 is local analysis at p\* plus the chord-level box. It is not a construction.

---

## 8. Files (`n16py/`)

| File | Purpose | Result |
|---|---|---|
| `halfplane_tests.py` | (★) tests: gauge control, translation, spiral, radial oscillation, independent linear vertices, joins; LP separability over 4 levels; vertex-respect | spiral fails at all levels; radial oscillation fails at c ≠ 0 only; translations and joins pass locally, fail globally; gauge passes |
| `firstorder_system.py` | first-order T1 system (crossings, signs, corners, box), LIN / HF₁ classes | LIN reproduces x₊²/κ |
| `signed_lambda.py` | same, λ of either sign | λ ≤ 0 feasible (Λ_max 0.4375 at ε = 0.3) |
| `eps_scan.py`, `eps_scan_out_eps0.{1,6}.txt` | ε = 0.1, 0.6 | table N16.12 |
| `hf_sensitivity.py` | single-bump sensitivities at ε = 0.3 | allowed bumps raise, forbidden lower |
| `riccati_check.py`, `minp.py` | HF_p carriers for the box-feasible chord maps; minimal p | p ≥ 1.39 / 1.48 / 4.34 |
| `hfp_verify.py` | direct concavity check of the explicit HF₅ model, fine-grid signs/corners/box, controls | concave to 10⁻¹⁰; controls fail |
| `hfp_system.py` | direct SLSQP in the HF_p class (moving-frame ODE) | too slow; not used for any claim |
| `lin_sol.npy`, `forbidden_sol.npy`, `hf_best.npy` | parameter vectors (ε = 0.3) | |

All numerics are evidence only. The claims labelled PROVED do not depend on them.
