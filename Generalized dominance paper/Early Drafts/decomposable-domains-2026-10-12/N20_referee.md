# N20: independent referee report on N15_notes.md (13 Oct 2026)

I did not write N15 and assumed nothing in it was correct until I had re-derived it. I formed every verdict below
**before** opening N18_referee.md. §9 compares the two reports.

**Read.** BRIEF7; N12 (all: N12.1 equivalence, Lemma 2.1, N12.3 box, Thm 3.1, Lemma 4.3); N14 (all, especially §§2, 3(iv),
5, 6); R15 §§1–6; R10b (§1, UVN, Lemma D, Lemma M, Lemma P, Thm PL, Cor PL2); N15 in full.

**Scripts** (`n20py/`; NUMERICS only, the verdicts rest on the hand derivations):
- `n15py/gauge_sanity.py` rerun: all output reproduced exactly (brackets 0.04779 ≤ 0.04899 ≤ 0.05019 etc.; corners 1.53e-6).
- `sandwich_check.py`: Lemma 2.3 and property (M) on 91 random synthetic families with non-crossing straight levels,
  including log-periodic level spacing: 0 violations in 3 640 tests. The pencils through (±r₀,0) attain the bounds,
  so the constants r₀/(r₀±|y|) are sharp.
- `window_check.py`: §6 Step 3 illustrated. For a ridge family with rotating chords and a log-periodic (non-concave)
  profile, τ ↦ G(Yu₀+x₀n₀, τ) fails concavity at every Y, and the rescaled window converges to φ(x₀+s) (error 1e-4,
  1e-6, 1e-8 at Y = 10, 100, 1000). With affine a(τ) and a concave non-linear φ, concavity holds (max defect 2e-13).
- `lemma41_grid.py`: Lemma 4.1 on the gauge realisation, 5 780 grid priors: no interior zero.

Verdict scale: CORRECT / CORRECT WITH REPAIR (local fix given) / GAP / FALSE.

---

## 0. Summary table

| Item | Verdict | One-line reason |
|---|---|---|
| Lemma 2.1 (exact half-planes, level strips) | **CORRECT** | Convexity of {f>c}, {f≤c}, {f<c}, {f≥c} from level clusters at nearby levels; weak separation. Wording: the "strip" is the region between two lines that may meet outside Ω (a truncated wedge) |
| Lemma 2.2 (monotone profiles) | **CORRECT** | |
| Lemma 2.3 (parallel-level sandwich) | **CORRECT** (expository repair) | Upper-bound step 3 tacitly assumes ∂{f<c} crosses the normal line above p\*. The convex-hull (triangle) argument covers all cases. Hypotheses can be weakened: f ≤ 0 on λ∩B(p\*,r₀) suffices, and f(q) ∈ I_g is not needed. Bounds are sharp |
| Uniformity remark (levels < c₀) | **CORRECT**, inessential | |
| Lemma 3.1 (caps; semicontinuity) | **CORRECT** (trivial slip) | γ(τ₀+η) may be 0. Use an interior point for "> 0". (e): ∂⁻ = inf (usc), ∂⁺ = sup (lsc), both verified |
| Lemma 4.1 (no partial pinning; Cor PL2 on G ∌ p\*) | **CORRECT** | Lemma M and Cor PL2 never use p\*. W_v(Ũ) ⇒ Γ_v checks. The chart-convexity step int conv(G∪V_j) ⊆ Γ is a valid Fubini upgrade (§3) |
| Thm 4.2 Step 0–1 (λ⁺_τ ∋ p\*) | **CORRECT** | Choice of σ₁, σ₂ checked in every case, including τ = τ_i and τ = τ_j |
| Thm 4.2 Step 2 (monotone) | **CORRECT WITH REPAIR** | Gluing the monotone pieces on (0,τ_j) and (τ_i,1) needs non-constancy on the overlap. That is Step 4.1, which is independent of Steps 2–3. Reorder |
| Thm 4.2 Steps 3–5 (continuity, strictness, crossing values, thin zero set) | **CORRECT** | |
| Thm 4.2 last clause (unique clusters) | **CORRECT WITH REPAIR** | A cluster line might a priori miss Ω. It cannot, because Ψ(·,τ) takes both signs. Add this line |
| Facet sign structure, general all-facing T | **CORRECT WITH REPAIR** | §1 proves it for T1 only. The general proof is two lines (§4.0) |
| Thm 4.3 (no sliding edges) | **CORRECT** | |
| Lemma 5.1 (slope–rotation inequalities) | **CORRECT** | Both sides re-derived. The semicontinuity directions are right. Gauge numerics cannot test them (S⁺ = S⁻ there) |
| Lemma 5.2 (rising sun) | **CORRECT** | |
| Prop 5.3(a)–(d) | **CORRECT** | (b) also kills singular chord maps. In fact L^\* ≥ c_J > 0 on compacts (§5.3) |
| §6 (M) | **CORRECT** | Follows from Lemmas 2.2–2.3 at scale t |
| §6 Step 1 (first blow-up) | **CORRECT** | |
| §6 Step 2 (sweep) | **CORRECT WITH REPAIR** (cosmetic) | Take τ₀ ∈ E′ ∩ int J, so that σ_± ∈ J |
| §6 Step 3 (window) | **CORRECT** | Re-derived. Every blow-up profile is concave. This kills log-periodic oscillation (`window_check.py`) |
| §6 Step 4 (second zoom) | **CORRECT** | |
| §6 Step 5 (projectivity) | **CORRECT WITH REPAIR** | "Projective on each compact J₁, hence on (0,1)" needs the lemma that positively proportional affine maps with non-constant direction differ by a constant factor. Proof in §6.5 |
| Thm 7.1 (assembly with N12 Thm 3.1) | **CORRECT** | (PC) and (NS) are exactly as N12 Thm 3.1 needs. Unique clusters feed its box step |
| Cor 7.2 (non-adjacent decomposable domains) | **CORRECT** (given N14 §3(iv)) | Simplest route: K̂ satisfies N12.1 (★), so it *is* a realisation on the U-domain (evaluable models: the measurable subsets of U = D_{K′}). Apply Thm 7.1 to it |
| Cor 7.3 (charges) | **CORRECT**, conditional on existence of interior Bayes minimisers | via N14 Thm C2 |
| Scope: every ε ∈ (0,1), every interior p\* | **CORRECT** | p\* enters only through r₀. The ε-dependence enters only through N12 Thm 3.1's algebra, valid for all ε |
| Formulation "no regularity assumptions" | **CORRECT WITH REPAIR** (statement) | Continuity is not automatic from an a.e.-in-q half-plane condition. One needs (R1) at **every** q, which gives Hausdorff continuity (N12 Prop 1.2), or continuity assumed. Otherwise "K_{p\*} = T" is vacuous (§8) |
| N15.10 numerics | **Reproduced** | Script comments use stale theorem numbers (Thm 3.1/3.4, Lemma 4.2) |

**Overall verdict: CORRECT.** N15's theorem holds after the repairs above, all of them local or expository.
- On the U-domain there is no realisation of T1, for any ε ∈ (0,1) and any interior p\*.
- The same holds for every all-facing triangle in general position.
- No (DD), (DF), (ND) or (NA_w) is needed. The only regularity used is Hausdorff continuity of q ↦ K_q, which follows
  from (R1) at every interior q.

I found no GAP and nothing FALSE.

---

## 1. Lemma 2.1–2.3 and the uniformity remark

**Lemma 2.1.**
- I_g = (min g_i, P_{K′}(g)), since g − c𝟙 ∈ U ⇔ c < P_{K′}(g), and P_{K′}(g) < max g_i.
- f = P(·,g) takes values in [min g_i, P_{K′}(g)], because K_q ⊇ K′. So in Step 2 any c′ ∈ (c, min f(q_i)) lies in I_g.
- **Step 2.** q_i ∉ Π⁻_{c′} gives q_i ∈ int Π⁺_{c′}. Then [q₁,q₂] ⊆ int Π⁺_{c′} ∩ Ω ⊆ {f ≥ c′}.
- **Step 3.** Both inclusions check.
- **{f<c} and {f≥c}.** These are the mirror images. For convexity of {f<c}, take c′ ∈ (max f(q_i), c), which exceeds
  min g_i.
- **Step 4.** In ℝ² any two disjoint nonempty convex sets are weakly separated. Openness then gives the exact form.
  - The degenerate case is harmless: a cluster line through a vertex with Ω on one side gives "∅ or Ω".
- **Step 6.** Two open half-planes whose boundary lines cross at x share a wedge at x.
- **Wording.** The lines may cross *outside* Ω. So "closed strip" should read "the closed region between two lines that
  do not meet in Ω".

**Lemma 2.2.** {s ∈ [0,r₀) : D⁺(s) > c} is a terminal sub-ray for each c ∈ (0, sup I_g). Monotonicity follows by
choosing c between two values. The endpoint value sup I_g is handled by a limit. Correct.

**Lemma 2.3.**
- *Lower bound.* As written. If L met λ at z ∈ Ω, a half-plane with boundary through z contained in A would equal A near
  z, contradicting f(z) = 0. The graph computation then puts q above L.
- *Upper bound.* Step 3 ("height ≥ s′(1−|y′|/r₀)") presumes that L′ = ∂{f<c} crosses the normal line at some s′ > s₁′.
  - L′ may instead cross it at s′ < 0, or be parallel to n.
  - In those cases q is again on p\*'s side, so the conclusion survives.
  - Cleanest proof: {f<c′} is convex for every c′ ∈ (D⁺(s₁′), c) ⊆ I_g. It contains the open chord
    {p\* + y′u : |y′| < r₀} and p\* + s₁′n, hence the open triangle they span, whose height over y is
    s₁′(1 − |y|/r₀) > x.
  - The lower bound has the same proof with {f ≤ c} and apex q.
- *Weaker hypotheses.*
  - Only f ≤ 0 on λ ∩ B(p\*,r₀) is used, not "zero set exactly λ ∩ Ω".
  - f(q) ∈ I_g is not needed: use intermediate levels.
  - One needs x·r₀/(r₀−|y|) < r₀, i.e. small x.
- *Sharpness* (`sandwich_check.py`). The pencil of levels through (r₀,0) gives f = x/(1−y/r₀), attaining the upper
  bound. The pencil through (−r₀,0) attains the lower bound.

**(M).** Let q = p\*+t(yu+xn) and q′ = p\*+t(y′u+x′n) with 0 < x < x′. Lemma 2.3 gives
f(q) ≤ D⁺(tx r₀/(r₀−t|y|)) ≤ D⁺(tx′ r₀/(r₀+t|y′|)) ≤ f(q′) once t is small. The mixed-sign and negative cases use Thm 4.2's
strict signs and the mirror lemma.

**Uniformity remark.** True by compactness of the closed facet: corner rays are mixed. It is inessential, given the
weakened Lemma 2.3.

---

## 2. Lemma 3.1

- (a), (b), (d): correct. In (b), the zeros of γ lie on ∂{γ ≥ 0}, and cl{γ>0} = {γ ≥ 0}.
- (c): γ′₊(τ₀) = sup_{τ>τ₀} γ(τ)/(τ−τ₀) > 0. The displayed bound "≥ γ(τ₀+η)/η > 0" can fail at the endpoint, where
  γ(τ₀+η) may be 0. Use any τ ∈ (τ₀, τ₀+η). Finiteness holds because γ is concave on all of ℝ.
- (e): the backward chord slope (γ(τ)−γ(τ−s))/s decreases as s ↓ 0, so γ′₋ = inf_s, which is usc. The forward slope
  increases as s ↓ 0, so γ′₊ = sup_s, which is lsc. Each quotient is jointly continuous in (q,τ).
- g_q(τ) = P(q, h(τ)) is concave on all of ℝ (P(q,·) is concave on ℝ³ and h is affine). This is needed at τ = 0 in
  Thm 4.3. Correct.

---

## 3. Lemma 4.1 (Cor PL2 away from p\*)

**Proof steps.**
1. Concavity gives Ψ ≥ 0 on G × [σ₁,σ₂].
2. Shrink the R10b ball U at w = h(τ_i) until F_k ∩ cl Ũ ⊆ cone h([σ₁,σ₂]).
   - R10b's other requirements survive the shrinking. They are: U inside N; U inside the UVN ball at w for j; points
     w_± ∈ U″ with (w_±)_c ≷ 0.
   - Lemma M Step 4 needs UVN only at points near w₊, not a ball containing U, so nothing is circular.
3. K_q ⊆ {m·h(σ₁) ≥ 0, m·h(σ₂) ≥ 0} ⊆ W_v(Ũ).
   - R10b §1 then gives q ∈ Γ_v.
   - The step: for h ∈ U⁺, w″ = h − (v·h)𝟙 ∈ v^⊥ ∩ Ũ ⊆ F_v, so m·h = m·w″ + v·h > 0.

**Cor PL2 on G ∌ p\*.** I re-ran Lemma M with G an arbitrary open connected subset of Γ_v.
- Step 1 is the only use of K_Q ≠ {v}. It is replaced by two-element advice ranges: the chart is {c(h)·q > 0} ∩ Ω.
- Steps 2–4 use only the following:
  - a point s ∈ β_v near Q, and Lemma D's collar at s;
  - (1.1) for good h;
  - UVN(a) at w₊ for world c;
  - the strict sign at world c.
- None of these involves p\*.
- So ∂_Gβ_v = ∅. Since β_v is relatively open in Γ_v (R12), G ⊆ α_v or G ⊆ β_v.

**Exclusion of α.**
- V_j ∩ Ω ⊆ Γ ∩ β, by UVN(a) at w with U ⊆ B₁.
- *Chart convexity, int conv(G ∪ V_j) ⊆ Γ (the one Fubini passage).*
  - For every h ∈ U⁺, P(·,h) > 0 on G ∪ (V_j∩Ω).
  - For good h this open set is a.e. inside H(h), hence inside H(h), hence its convex hull is too.
  - Fubini on (int conv) × U⁺ gives, for a.e. q, a.e. h ∈ U⁺ in D_{K_q}. So D_{K_q} ⊇ U⁺, since U⁺ = U ∩ D_T is open
    and convex.
  - Continuity in q then gives every q (R10b §1, last bullet).
  - Valid.
- The connected open set int conv(G ∪ V_j) ⊆ Γ meets α (at G) and β (at V_j ∩ Ω). This contradicts the dichotomy,
  whose no-d-face hypothesis is automatic on this domain.

**Positivity.**
- h(σ₁) and h(σ₂) restricted to 𝟙^⊥ are independent, because 𝟙 ∉ v_k^⊥. So W ∖ {v_k} ⊆ {m·h(τ) > 0} for τ ∈ (σ₁,σ₂).
- K_q is compact and misses v_k, so Ψ(q,τ) > 0.

**Correct.**
- This is the genuinely new idea: G need not contain p\*, and the interval [σ₁,σ₂] may be much larger than any pinning
  arc. That is why every pinning arc dies, crossing-free arcs included, which N14 §5.2 left open.
- Sanity check (`lemma41_grid.py`): 0 interior zeros among 5 780 grid priors in the gauge realisation.

---

## 4. Theorem 4.2 and Theorem 4.3

**4.0 Sign structure.**
- For T1 it is as stated.
- For general all-facing T, write v_k = a e_k + b v_i + c v_j with a, b, c > 0. For 0 ≠ h ∈ F_k,
  0 = h·v_k = a h_k + b h·v_i + c h·v_j, and h·v_i, h·v_j ≥ 0 are not both 0. So h_k < 0.
- At a crossing of i, h_k < 0 and h_i = 0 force h_j > 0. With both coordinates crossing once (C_k = {i,j}, affine
  along the facet), this gives the stated pattern.
- Add this to §1.

**Step 0.** Ψ(p\*,τ) = P_T(h(τ)) = 0. UVN applies at h(τ) ∈ N. Lemma 2.1 at c = 0 ∈ I_{h(τ)}. Correct.

**Step 1.** Cases checked:
- τ ≤ τ_i: σ₁ ∈ (0,τ), σ₂ ∈ (τ_i,τ_j);
- τ_i < τ < τ_j;
- τ ≥ τ_j, including τ = τ_j: σ₁ ∈ (τ_i,τ_j), σ₂ ∈ (τ,1).

In each case [σ₁,σ₂] contains a crossing, and h(σ₁), h(σ₂) share a positive coordinate.
- G = int(P_{σ₁} ∩ P_{σ₂}) is open, convex and nonempty, with p\* ∈ cl G.
- Interiors are taken in the plane. Since Ω is open, int(C ∩ Ω) = int C ∩ Ω.
- Correct.

**Step 2.**
- The wedge inclusion plus 2-D Farkas gives betweenness, and betweenness on an interval gives monotonicity. Correct on
  each of (0,τ_j) and (τ_i,1).
- *Repair.* Gluing the two pieces needs the angle to be non-constant on the overlap (τ_i,τ_j). That is Step 4.1, which
  uses only Lemma 3.1(b) and UVN, not Steps 2–3. State Step 4.1 first.
- The one-sided limits used in Step 3 need only the local pieces.

**Step 3.**
- W is nonempty even when n(τ₀+) = −n(τ₀−).
- The convex hull of (p\*+W) ∪ (p\*−W) near p\* is a neighbourhood of p\*. This contradicts p\* ∈ cl A_{τ₀}.
- Correct.

**Step 4.**
- cl A_τ ∖ A_τ ⊆ Z_τ, and Lemma 3.1(b) applies.
- A line through a boundary point of a closed half-plane, contained in that half-plane, is its boundary.
- The sign change of n_τ·(e_i − p\*) across τ_i uses UVN(a)/(b) and the "a line through e_i and p\* cuts V_i" argument.
- Correct.

**Step 5.** λ⁻ ∌ p\*, so a half-disc at p\* lies in Z_{τ₀}. The test prior and the cap lemma then give a contradiction
with continuity of n. Correct.

**Last clause.**
- *Repair.* If a cluster line ℓ missed Ω, then Ψ(·,τ) would be one-signed on Ω (≥ 0 or ≤ 0), contradicting A_τ, B_τ ≠ ∅.
- So ℓ meets Ω, and the two closed sides force ℓ = λ_τ with the same orientation.

**Thm 4.3.**
- On the open double wedge O, P(·,r) is both ≥ 0 (facet k) and ≤ 0 (facet j).
- The zero set is convex (Lemma 2.1; r ∈ U is mixed), so it contains a ball B around p\*.
- The test prior: J⁺(q) is an interval containing τ > 0 and missing (0,ε), so 0 ∉ cl J⁺(q). Lemma 3.1(b) applied to
  g^k_q, concave on ℝ, then gives P(q,r) < 0. Contradiction.
- The orientation is fixed by positivity on each facet.
- Correct.

**Counterexample attempts.**
- (i) A pinned arc without crossings, i.e. P(·,h(τ)) ≡ 0 near p\* for τ ∈ (a,b): killed by Step 1 with a wider
  [σ₁,σ₂], because G accumulates at p\*.
- (ii) A fat zero set at a single τ₀: killed by Step 5.
- (iii) A sliding edge: killed by Thm 4.3.

I could not make any of them survive. Each fails at a step that I verified.

---

## 5. Lemma 5.1, Lemma 5.2, Prop 5.3

**5.1 D⁺ side.**
- Coordinates of the anchor relative to λ_{τ₁}: (y,x) = (ξcosΔ, ξsinΔ). Lemma 2.3 plus monotonicity of D⁺ give the
  sandwich with factors r₀/(r₀±ξ).
- Cap at τ₀: (τ₁−τ₀)g(τ₂)/(τ₂−τ₀) ≤ g(τ₁) ≤ (τ₁−τ₀)g′₊(τ₀).
- *Upper bound.* Use g′₊ ≤ g′₋ and usc of ∂⁻ at (q_{τ₁}(ξ),τ₁), since q_{τ₀}(ξ) → q_{τ₁}(ξ) by continuity of θ. This
  gives limsup ≤ S⁻.
- *Lower bound.* For fixed τ₂, joint continuity applies. The sup over τ₂ ↓ τ₁ is S⁺, positive because q_{τ₁} has a
  right cap.
- (τ₁−τ₀)/sinΔ has limsup 1/L_\* and liminf 1/L^\*.
- The map Δ ↦ x is a continuous bijection near 0, so the limits in x match the limits in τ₀.
- Products of nonnegative factors behave as needed.

**5.2 D⁻ side.**
- Left cap: γ′₊(τ₀) ≤ γ′₋(τ₀) < 0.
- Lower constant: liminf |∂⁺Ψ(q′_{τ₀},τ₀)| ≥ liminf(−∂⁻Ψ(q′_{τ₀},τ₀)) ≥ −∂⁻Ψ(q′_{τ₁},τ₁) > 0, since −∂⁻ is lsc.
- Upper constant: inf over τ₂ of |γ(τ₂)|/(τ₂−τ₁) = |γ′₊(τ₁)|.
- The note's constants are exactly these. The semicontinuity directions are right.

**Numerical caveat.** In gauge mixtures the normal fan of K_q does not depend on q. I checked that all kinks of
Ψ(q,·) sit at the corner rays, where h_i = u·h. So S⁺ = S⁻ at every relint anchor, and the numerics of N15.10 cannot
detect a wrong semicontinuity direction. The analytic check above is what settles them.

**5.3 Lemma 5.2 and Prop 5.3.**
- *Lemma 5.2.* Correct. It even gives L_\* ≥ ε′.
- *(a).* Lemma 5.2 is applied on two disjoint intervals left of J and one right of J. At those points Lemma 5.1 gives
  D^± ≤ C′x, and Lemma 2.3 gives |Ψ(p\*+δ,σ)| ≤ 2C′|δ|. On J:
  - concave extrapolation gives the upper bound;
  - the minimum of the endpoint values gives the lower bound.
  - Correct.
- *(b).* θ′ = 0 at a point gives L^\* = 0, and the lower bound of Lemma 5.1 is then ∞. This contradicts (a). Correct.
  - This also excludes Cantor-type strictly increasing θ.
  - Stronger: S⁺(τ) = ∂⁺Ψ(q_τ(ξ),τ) is lsc and positive in τ, so it is ≥ s_J > 0 on J. Then (a) gives
    L^\* ≥ s_J(r₀−ξ)/(r₀ξC) > 0 everywhere on J. So θ − c·id is nondecreasing, and θ′ ≥ c a.e. Not needed, but cleaner.
- *(c), (d).* Correct.
  - In (d), existence of lim D^±(x)/x is existence of the derivative along ±n. So (F2) is impossible.

**Counterexample attempt.** Slow rotation (θ′ = 0) combined with a Lipschitz profile is impossible by (b). Fast rotation
(θ′ = ∞) is allowed only on a null set, which §6 never needs.

---

## 6. §6, the two-stage blow-up

**6.0 Preamble.** |Ψ_t| ≤ C|δ| on J′ with concavity gives the Lipschitz constant 2C|δ|/dist(J,∂J′) on J, uniformly in t.
Correct.

**6.1 Step 1.**
- Arzelà–Ascoli plus a diagonal argument over Q. Correct.
- (M) passes to the limit for each fixed triple (δ,δ′,τ).

**6.2 Step 2 (sweep).**
- φ^± are finite by (M).
- The forward sweep: n_{σ₊}·δ ≥ x₀+2.5ε > x₀+1.5ε ≥ n_{σ₊}·δ′ for large Y. Then G(δ,σ₊) ≥ G(δ′,σ₊) ≥ φ⁺(x₀) − L₁|σ₊−τ₀|.
- The backward sweep is the mirror image.
- The Lipschitz bound uses |δ| ≈ Y and |σ_±−τ₀| ≈ 3ε/(Yϑ). Then 𝒥 ≤ 6Lε/ϑ + o(1), so 𝒥 = 0.
- *Repair (cosmetic).* Take τ₀ ∈ int J.
- The step uses only that θ is differentiable at τ₀ with θ′ ∈ (0,∞). A positive lower Dini bound on both sides would
  suffice.
- *Consequences.* φ⁻ is left-continuous and φ⁺ right-continuous, so equality gives continuity. G(δ,τ₀) = φ(n₀·δ) on Q
  by (M). Squeezing gives convergence for every δ. Convergence on the dense set E′ ∩ J plus equi-Lipschitz gives uniform
  convergence on J.
- Correct.

**6.3 Step 3 (window).**
- h_Y is concave as a restriction of G(δ_Y,·).
- For σ ∈ E′:
  - G(δ_Y,σ) = φ_σ(z), with z = Y sinΔ + x₀cosΔ = x₀ + s + o(1) uniformly in |s| ≤ r;
  - φ_σ(z) = G(zn_σ,σ) = G(zn_σ,τ₀) + O(L|z|r/(Yϑ)) = φ_{τ₀}(z cosΔ) + O(1/Y).
- The two estimates agree on a dense set of s, and both sides are continuous. A uniform limit of concave functions is
  concave.
- Correct.
- The mechanism: one fixed far point δ_Y on the chord sees every transverse position x₀ + s as the chord rotates through
  an angle of order 1/Y.
- `window_check.py` shows the contrapositive: a log-periodic profile x(2 + 0.4 sin log(1/|x|)) violates concavity in τ
  at every Y.

**6.4 Step 4.**
- α ≥ c_{τ₀} by Prop 5.3(c), and β ≤ C.
- The extension off E′ via continuity of G₂(δ,·) and of n checks.
- α > 0 everywhere: a concave function ≥ 0 that vanishes at an interior point is ≡ 0.
- β ≥ α passes to limits.
- Correct.

**6.5 Step 5.**
- N12 Lemma 4.3's proof needs exactly the following:
  - f_δ concave;
  - the two-slope form;
  - n, α, β continuous, with α > 0 locally;
  - n nowhere locally constant.
- All are present. So a = αn is affine on int J₁.
- *Repair: patching.* Let a, a′ be affine on an interval with a′(τ) = μ(τ)a(τ), μ > 0, and a(τ) = p + τv with p, v
  independent. Then (p′+τv′) × (p+τv) ≡ 0 forces p′ = κp, v′ = κ′v and (κ−κ′) p×v = 0, so a′ = κa. Hence the
  normalisations on nested J₁'s agree up to constants, and a extends affinely to [0,1].
- *Rank 2.*
  - If a(0) and a(1) were parallel, the direction would be constant.
  - If they were antiparallel, a would vanish inside (0,1), contradicting α > 0.
  - So Γ_k r = a(0) ≠ 0.
- Correct.

---

## 7. Theorem 7.1, Corollaries 7.2–7.3, scope

**Thm 7.1.**
- (PC): Γ_k h ≠ 0 on relint F_k. Cl(h) = {λ_h}, with λ_h = {Γ_k h·(q−p\*) = 0} and positive side {Γ_k h·(q−p\*) > 0}.
  This is Thm 4.2 plus §6.5.
- (NS): a^k(0) ∝₊ lim n^k_τ = n^k(0+) = n^j(0+) ∝₊ a^j(0), by Thm 4.3.
- N12 Thm 3.1 (refereed CORRECT in N14) uses (R1), (R2), (PC), (NS), and unique clusters at the box witnesses. The
  witnesses lie in relint, near the crossings.
- So the contradiction follows. Correct.

**Cor 7.2.**
- Under non-adjacency, N14 §3(iv) shows that K̂_q = conv(K_q ∪ K′) satisfies N12.1's hypotheses with U = U′ = D_{K′}.
- By N12 Prop 1.4 (converse), K̂ is itself a U-domain realisation of T. So Thm 7.1 applies verbatim.
- No separate check of Cor PL2's hypothesis is needed.
- Correct, given N14 §3(iv).

**Cor 7.3.** Correct via N14 Thm C2, conditional on existence of interior Bayes minimisers.

**Scope.**
- Every interior p\*: p\* enters only through r₀ = dist(p\*,∂Δ) > 0. Nothing uses p\* = u.
- Every ε ∈ (0,1): T1's facet sign structure holds for all ε, and N12 Thm 3.1's T1 contradiction holds for all κ > 1.
  That contradiction is x + 1/x = κ + 1 with x² ∈ [1/κ, κ].
- All-facing general-position triangles: correct, with §4.0 added.

---

## 8. Audit: a.e./Fubini passages, silent regularity, corners

| Passage | Kind | Status |
|---|---|---|
| N12 Lemma 2.1(a)/(b) (imported) | Fubini to a.e. g, then open-set upgrade to all q; clusters for every mixed g | valid (N14) |
| UVN (imported) | dominated convergence at vertex priors | valid |
| Lemma 4.1 chart convexity | for good h ∈ U⁺, H(h) ⊇ G ∪ V_j; Fubini on int conv × U⁺; continuity to every q | valid (§3) |
| Cor PL2/Lemma M (imported) | good h ∈ U⁻, collars, cluster limits | valid on arbitrary G |
| N12 Thm 3.1 box (imported) | Fubini over (A,B,λ) | valid (N14) |
| N15 §§2, 4–6 | deterministic: every q, every τ. Lebesgue differentiation of monotone θ (a.e. τ) | valid |

**Silent regularity: none.**
- Only joint continuity of P is used, i.e. Hausdorff continuity of K_q.
- Lipschitz control at p\* (Prop 5.3(a)), a.e. differentiability of θ, Lipschitz and BV regularity of a (inside Lemma
  4.3), and continuity of α and β are all derived.

**Formulation caveat (statement-level repair).**
- If the realisation is given only as "for a.e. g, {q : P(q,g) > 0} = H(g) ∩ Ω for a.e. q", continuity is not automatic.
- Altering K_q on a q-null set, p\* included, preserves that condition. So "K_{p\*} = T" would carry no information.
- The theorem therefore needs one of the following:
  - (R1) at every interior q (B_q = D_{K_q} a.e.), which yields Hausdorff continuity by N12 Prop 1.2;
  - or Hausdorff continuity as part of the hypotheses.
- In the BRIEF7 formulation continuity is available, so this is a wording point.

**Corners.**
- Facet-by-facet statements (Thm 4.2, §6) live on relint F_k.
- Corners enter in only two places:
  - Thm 4.3 (chord limits at r), which uses concavity of g^k_q on ℝ across τ = 0;
  - the affine extension a(0) = Γ_k r.
- The two are combined consistently in Thm 7.1.
- The orientation convention (normal into A) is the same on both facets.

**Boundary priors and selections.** No boundary-prior coherence is used. Vertex coherence is automatic on the domain.
No Bayes-at-index selection is used.

---

## 9. Comparison with N18_referee.md (read after the verdicts above)

**Agreement on every item.** In particular:
- Lemma 4.1 / Cor PL2 away from p\*: both CORRECT.
- Lemma 5.1's semicontinuity directions: both CORRECT, both noting that gauge numerics cannot discriminate them.
- §6 sweep and window: both CORRECT, with the cosmetic τ₀ ∈ int J.
- Thm 7.1: both CORRECT.
- Overall: both CORRECT. On the U-domain (and on non-adjacent domains), the additive core (B) for T1 is
  closed for every ε and every interior p\*.

**Same repairs found independently:**
- Thm 4.2 step order (N18 R-a);
- the cluster line must meet Ω (R-b);
- the general all-facing sign structure (R-c);
- τ₀ ∈ int J;
- the affine-patching lemma in Step 5.

**Minor differences (no disagreement on correctness):**
1. *Lemma 2.3.*
   - N18 lists "zero set exactly λ ∩ Ω" and f(q) ∈ I_g among what is used. Neither is needed: f ≤ 0 on λ ∩ B(p\*,r₀)
     suffices, and intermediate levels replace I_g. This matters only for reuse.
   - I also note that the bounds are sharp.
   - N18's triangle proof of the upper bound is the same repair I give for Step 3.
2. *Prop 5.3(b).* I add the uniform form L^\* ≥ c_J > 0 on compacts (lsc of S⁺), hence θ′ ≥ c_J a.e. N18 does not state
   it. It is not needed.
3. *Cor 7.2.*
   - N18 transfers Γ_v, α_v, β_v and UVN from K to K̂ item by item.
   - I would instead apply Thm 7.1 to K̂ as a realisation in its own right (N12 Prop 1.4 converse).
   - Both are valid. Mine has fewer moving parts.
4. *Formulation caveat (§8).* N18 does not mention it. It is not an error in N15, which takes continuity from N12.1. But
   any write-up stating the theorem as "for the K_q family, with no regularity" must include (R1) at every q, or
   continuity.
5. *Lemma 3.1(c).* The trivial endpoint slip γ(τ₀+η)/η > 0 is not in N18. It is cosmetic.

**Disagreements: none.**

---

## 10. Requested edits to N15

1. Thm 4.2: state Step 4.1 (non-constancy) before Step 2's gluing. Add "cluster lines meet Ω" to the last clause.
2. §1: give the sign-structure proof for general all-facing T (§4.0).
3. Lemma 2.3: replace upper-bound Step 3 by the triangle argument. Weaken the hypotheses to f ≤ 0 on λ ∩ B(p\*,r₀).
4. Lemma 2.1 / N15.1: "strip" → "region between two lines not meeting in Ω".
5. Lemma 3.1(c): use an interior point for strict positivity.
6. §6: τ₀ ∈ E′ ∩ int J. Add the affine-patching lemma (§6.5) to Step 5.
7. N15.8 statement: say explicitly that Hausdorff continuity comes from (R1) at every interior q (N12 Prop 1.2).
8. `gauge_sanity.py`: update the theorem numbers in its comments.

## 11. Files (`n20py/`)

| File | What | Result |
|---|---|---|
| `sandwich_check.py` | Lemma 2.3 and (M) on random synthetic straight-level families (non-crossing in B(0,r₀), oscillating level spacing); sharpness via pencils through (±r₀,0) | 0/3640 violations; bounds attained |
| `window_check.py` | §6 Step 3: ridge families with rotating chords; non-concave log-periodic φ versus affine a with concave φ | non-concave: concavity in τ fails at every Y, and the window converges to φ(x₀+s); concave case: defect ≤ 2e-13 |
| `lemma41_grid.py` | Lemma 4.1 on the gauge realisation: priors with both endpoint values ≥ 0 | 0 interior zeros among 5 780 priors (all four σ-intervals straddle a crossing) |
