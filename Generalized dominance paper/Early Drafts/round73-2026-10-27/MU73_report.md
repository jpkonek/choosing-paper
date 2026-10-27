# MU73 report: how much does consolidation depend on μ?

Round 73, 27 Oct 2026. Sources: BRIEF73, ROUND72 §§1–2.4, AX72 §C3 and §4, REF72b, GUIDANCE_after_r71 §§2–3, app.tex §2 and §§6, 8. Hand proofs; small numerics in `r73/mu73_py/checks73.py` (all checks pass).

Conventions: ⪰_ω means "at least as good at ω", as in the briefs. 𝟙 is the constant gamble. "z pays more than w at every world" means z(ω) > w(ω) for all ω. P_S(h) = inf_Ω h, so D_S = {inf h > 0} is open.

---

## 0. Answers first

| | Question | Answer | Label |
|---|---|---|---|
| 1a | Exact triples for a positive continuous density on Rⁿ | **Partly.** Non-collinearity is not the relevant condition; it is an artefact of AX72's polar maps. In R² the two pushforward identities form a determined first-order system: prescribed divergence plus prescribed Jacobian. The hint's decoupling fails, because T fixes S. The system is elliptic exactly when ρ(x)^{-1/2}, ρ(y)^{-1/2}, ρ(x+y)^{-1/2} satisfy strict triangle inequalities; then exact triples exist for Hölder ρ. Otherwise (hyperbolic) existence is expected but not shown. For merely continuous ρ it is unclear. | Elliptic case PROVED in outline; locally constant ρ PROVED; hyperbolic CONJECTURE; C⁰ UNCLEAR |
| 1b | Atoms; density vanishing on regions | **Atoms are harmless; vanishing density is a real gap.** By (M2) every atom lies in D_S or in {sup h < 0}. On those gambles, step 1 of C3.7(ii) already fixes any strictly defended model. Where μ vanishes, every form of C3 loses force. There is a ranking that satisfies C3 (exact and margin forms) and strictly defends an incoherent model when (M3) fails. | PROVED (counterexample §1.3; NUMERICS for the inequalities) |
| 1c | General Ω, separable E ⊆ ℓ∞(Ω) | **Exact form: unclear.** There are no density points. For Gaussian μ, exact triples exist in special global forms (a 120° rotation of the Cameron–Martin space for sums; a two-coordinate product reduction for midpoints). They cannot be placed inside an arbitrary incoherent model. **Margin form (below): works in full generality.** | Gaussian constructions CHECKED in outline; exact-form C3.7(ii) UNCLEAR |
| 2 | A less μ-dependent reformulation | **Yes: consolidation with a margin (C3m).** Drop the bijections. Ask only that G₁, G₂, G₃ have equal measure (G₃ has twice the measure for midpoints), and that every gamble in G₃ pays more at every world than the sum (or average) of any gamble in G₁ and any gamble in G₂. Such triples exist for every atomless μ with full support, in the paper's general setting. (i) C3m excludes R_{s'} and every distorted-score counterexample. (ii) R0, R∩, the round-71 maximal rankings and veto–Brier satisfy it, even in its strongest variant. (iii) C3.7(ii) holds for C3m, now with every step written, under (M2), (M3) and atomless μ (or a full-support atomless part). Two other proposals fail. A version with only absolute continuity of the pushforwards is **violated by R0**. A guided correction cannot replace mass-matching without quantifying payoffs. | PROVED |
| 3 | Is C3 the integral in disguise? | **No, but it is the integral's motivation in qualitative form.** Among integral scores with continuous densities, (G) and C3 together hold iff each world's score is s_ω(X) = a_ω∫_X h(ω)⁺dμ − b_ω∫_X h(ω)⁻dμ with b_ω ≥ a_ω > 0. Such a score is local, and loss-neutral or loss-averse. Linear is a = b. Bayes sets are then coherent D_Q, and imprecise when b > a. C3 uses only the linear structure of gambles and μ-mass; the margin form also uses the pointwise payoff order. It is genuinely weaker than the integral, because the integral's linearity is global and C3 reaches only as far as μ connects gambles by sums (§1.3). Its real commitment is that stakes count by payoff, which rules out error-counting. Paper-ready statement in §3.5. | Classification PROVED; assessment is judgement |

**Unchanged:** dominance in every maximal member of 𝓡 + C3 (C3.8) is still OPEN. Every form of C3 forbids only strict chains.

---

## 1. Existence of matched triples (Question 1)

### 1.1 (a) Positive continuous density on Rⁿ: exact triples

**What the identities say.** For C¹ maps, T_*(μ|G₁) = μ|G₂ and S = id + T with S_*(μ|G₁) = μ|G₃ are
- ρ(T h)·|det DT(h)| = ρ(h), and
- ρ(h + T h)·|det(I + DT(h))| = ρ(h).

For midpoints, S = (id + T)/2 and S_*(μ|G₁) = ½μ|G₃, so the second equation becomes ρ(S h)·|det(I + DT)| = 2ⁿ⁺¹ρ(h).

**The hint does not decouple the problem (WRONG as a strategy).** The hint was: get T from the isomorphism theorem and S from Dacorogna–Moser. But S = id + T, so choosing T fixes S, and choosing S fixes T = S − id. Precomposing T with a μ-preserving θ keeps T's identity and leaves one scalar equation for θ. That equation is a second-order fully nonlinear PDE (Monge–Ampère type); it is the same difficulty, repackaged.

**Structure in R² (PROVED).** In R², det(I + M) = 1 + tr M + det M. So, with A := ρ(h)/ρ(Th) and B := ρ(h)/ρ(h+Th), the system is

  div T = B − A − 1,  det DT = A.

This is *prescribed divergence and prescribed Jacobian*: two equations for two unknown functions. For n ≥ 3 it is underdetermined.

**Linear model and its type (PROVED).**
- Near (x, y), look for T ≈ y + L(h − x) with det L = α := ρ(x)/ρ(y) and det(I + L) = β := ρ(x)/ρ(x+y). In R², such L exist for all α, β > 0: take tr L = β − 1 − α.
- The linearised operator is σ ↦ (div σ, tr(adj L · Dσ)). Its symbol is injective for all ξ ≠ 0 iff L has no real eigenvalue, that is, iff (β − 1 − α)² < 4α.
- Equivalently, 1, √α, √β form a strict triangle. Dividing by √ρ(x): **ρ(x)^{-1/2}, ρ(y)^{-1/2}, ρ(x+y)^{-1/2} form a strict triangle** (elliptic case).
- For midpoints, the third side is 2√2·ρ((x+y)/2)^{-1/2}.
- Orientation-reversing choices are always hyperbolic.

**Consequences.**
- *Locally constant density (e.g. Lebesgue).* Affine maps give exact triples near **any** x, y with x, y, x+y distinct, collinear included (PROVED).
  - Sums: T(h) = y + R₁₂₀(h − x), so S = id + T = x + y + R₆₀(h − x). Both are rotations, with det 1.
  - Midpoints: L = diag(3+2√2, 3−2√2) gives det L = 1 and det((I+L)/2) = 2.
  - NUMERICS: `checks73.py` §3.
- *Hölder ρ, elliptic configurations* (PROVED in outline; standard, not written in full).
  1. Rescale: h = x + εz and T = y + ετ(z), with τ = Lz + σ.
  2. As ε → 0, A and B tend to the constants α and β in C^{0,γ}, at rate ε^γ.
  3. The system becomes div σ = small, and tr(adj L Dσ) + det Dσ = small. The quadratic term is exactly det Dσ in R².
  4. The constant-coefficient elliptic part reduces to ∂̄ by a linear change of variables. That operator has a bounded right inverse C^γ → C^{1,γ} on a disc.
  5. A Schauder fixed point (not a contraction, since ρ is only Hölder) gives a C^{1,γ'} solution with Dτ ≈ L.
  6. T and S are then injective local diffeomorphisms, the Jacobian identities hold exactly, and G₁ = x + εB₁/₂, G₂ = T(G₁), G₃ = S(G₁) are disjoint near-ellipses of bounded eccentricity. That eccentricity bound is what density-point arguments need.
  - AX72's Gaussian configuration (−1.5, 1), (1, −1.5) is elliptic for both clauses (NUMERICS).
- *n ≥ 4, C¹ ρ.* Write h = (u, w) with u ∈ R² and T = (τ(u, w), y_w + M(w − x_w)), with M chosen so that the u-problem has constants (1, 1). This reduces to the elliptic two-dimensional case, with parameter w. The implicit function theorem gives measurable dependence on w (outline). n = 3 has less freedom and is not settled.
- *Hyperbolic configurations* (the triangle fails, e.g. collinear Gaussian pairs such as (1,0), (2,0)). The system is hyperbolic. Local solvability for smooth ρ is expected from characteristic methods but is not checked: **CONJECTURE.**
- *Merely continuous ρ*: **UNCLEAR.** Dacorogna–Moser needs Hölder data. Jacobian equations with C⁰ data can lack bi-Lipschitz solutions (Burago–Kleiner; McMullen). Measurable non-Lipschitz solutions are not ruled out, but I have no construction.

**Verdict on (a).** Exact triples are a genuine PDE question: elliptic or hyperbolic depending on density ratios, with regularity demands. That is a reason not to build the principle on them (§2).

### 1.2 (b) Atoms

- Exact or margin triples through an atom need pieces of exactly matching mass. A bijection cannot spread an atom over a diffuse set. So atoms almost never take part in triples.
- **This is harmless (PROVED).** By (M2), every atom a lies in D_S or in {sup h < 0}. Otherwise inf a ≤ 0 ≤ sup a, some state q has q(a) = 0, and μ{q = 0} ≥ μ{a} > 0 (REF72b C3).
- Step 1 of C3.7(ii) uses only (G) and (SC). It forces a strictly defended model X to contain D_S a.e. and to miss {sup h < 0} a.e. So X agrees with every coherent model on every atom.
- Hence X is coherent for μ iff it is coherent for the atomless part μ_c. The argument of §2.4 runs with μ_c, provided **μ_c has full support**. Example: Gaussian plus a point mass at 𝟙.

### 1.3 (b) Density vanishing on regions: a real gap (PROVED; NUMERICS for the arithmetic)

**Setting.**
- E = R². μ is Lebesgue measure restricted to three sup-norm balls of radius r = 0.05 about a = (−1.5, 1), b = (1, −1.5) and n = (−1, −1).
- (M1) and (M2) hold: every {P_Q = 0} is a union of at most two rays, which is Lebesgue-null. (M3) fails.
- X* = B(a) ∪ B(b) is incoherent modulo μ. A state positive on B(a) needs q₁ < 0.4, and one positive on B(b) needs q₁ > 0.6.

**Ranking.** R_g with p = (½, ½):
- g₁(h) = h₁ everywhere;
- g₂(h) = 3h₂ on B(a), ⅓h₂ on B(b), and h₂ on B(n).
- Both are truth-directed, so R_g ∈ 𝓡. The AX72 §0 argument works: the two-world lemma "a change some coherent model could make that raises s at both worlds is guided at neither" uses only (M2) and sign conditions.
- The Bayes values at the centres are 0.75, 0.25 and −1. So X* = {Σ p_ω g_ω > 0} a.e., and X* is strictly preferred to every rival at some world (Bayes fact plus defence lemma).

**C3 holds, in every form.**
- Every accepted non-null change raises s_ω. So it suffices that every triple supported by μ has c·g(z) ≥ g(x) + g(y) at both worlds.
- With centres a, b, n and margin consolidations, the supported triples are:
  - within-ball midpoints;
  - (a, n → a), (b, n → b), (n, n → a), (n, n → b) and (n, n → n).
  - No triple pairs B(a) with B(b): a + b = (−½, −½) and (a+b)/2 are above nothing in the support.
- World 1 is linear, so it passes. The world-2 slacks over the balls are ≥ 0.65, 0.92, 4.75 and 1.38 for the cross-ball cases; the within-ball cases are linear and increasing.
- The exact form has even fewer instances.
- So R_g satisfies C3 (exact) and C3m, and X* is undominated in every strict-preserving extension. Maximal members above R_g exist, because chain unions preserve C3m and Ω is finite.

**Morals.**
1. C3 has force only where μ connects gambles by sums.
2. The integral does more. R0 (Def. 6.1) still dominates X* here, because Theorem `thm:main` of app.tex needs only (M1) and (M2). Linear payoffs are a global constraint; consolidation is local to the support.
3. **(M3), or full support of μ_c, is needed for C3.7(ii).** With D_S charged as well, the analogous score counterexamples break down: sums with large gambles in D_S force the world-2 slopes to agree. Whether some non-score ranking survives there is OPEN.

### 1.4 (c) The paper's general setting

- **Exact form.** There is no Lebesgue density theorem, and natural μ are singular under dilations and most shifts.
  - For a centred Gaussian μ, some exact triples exist (CHECKED in outline).
    - *Sums.* Let U rotate each pair of an orthonormal basis of the Cameron–Martin space by 120°. Then U and I + U (rotation by 60°) are orthogonal. Their measurable extensions preserve μ. Sector sets {arg(ξ₁ + iξ₂) ∈ (0, π/6)} give disjoint G₁, UG₁ and (I+U)G₁.
    - *Midpoints.* Split μ = γ₂ ⊗ μ′ along two Paley–Wiener coordinates. Let T act as AX72's two-dimensional map on those coordinates and as the identity on the rest. Then (h + Th)/2 is also the identity on the rest.
  - These triples are localised in finitely many coordinates only. They cannot be placed inside an arbitrary incoherent X, so **the exact form's C3.7(ii) is UNCLEAR for infinite-dimensional E.**
- **Margin form.** Everything in §2 uses only:
  - separability (Lindelöf, and countable covers by sup-norm balls);
  - openness of D_S;
  - Lemma `lem:identify`(b);
  - (M2), (M3) and atomlessness.
  So it holds for arbitrary Ω and separable E ⊆ ℓ∞(Ω) (PROVED).

### 1.5 Where C3 has force (summary)

**Exact C3 (AX72)** constrains a ranking at (x, y) iff exact triples exist near (x, y, x+y), or near (x, y, (x+y)/2). This is known:
- everywhere for locally constant densities;
- at non-collinear pairs for rotation-invariant μ on R²;
- at elliptic configurations for Hölder ρ on R² (outline);
- in special global forms for Gaussian μ in infinite dimensions;
- through atoms only when masses coincide;
- nowhere where μ vanishes.

It is unknown at hyperbolic configurations and for merely continuous ρ.

**C3m (§2)** constrains a ranking at every (x, y, z) with z − (x+y)/c ∈ D_S, where c = 1 or 2, and x, y, z lie in the support of the atomless part of μ. Under (M3) with atomless μ, that is every such configuration. It is silent exactly where μ_c vanishes, and §1.3 shows that silence can matter.

---

## 2. A reformulation with less dependence on μ (Question 2)

### 2.1 Two proposals that do not work

**Absolute continuity only (WRONG; PROVED).** Suppose T_*(μ|G₁) and S_*(μ|G₁) are only required to be absolutely continuous, so the masses of G₁, G₂, G₃ may differ. Then R0 violates the principle.
- Take x, y ∈ D_S, S(h) = h + T(h), and G₃ near x + y with μ(G₃) = μ(G₁)/10.
- The splitting change Z′ → Z adds G₁ ∪ G₂ ⊆ D_S. Every coherent model contains D_S, so no coherent model could make the change.
- At every ω its increment is m_ω(G₁) + m_ω(G₂) − m_ω(G₃) ≈ μ(G₁)·0.9·(x + y)(ω) > 0.
- R0 therefore accepts it, by clause (ii), at every world, and refuses the reverse. So Z ≻_ω Z′.
- **Mass equality is indispensable:** "the same amount" is what makes consolidation a like-for-like substitution.

**Guided correction ("consolidation up to a change guided at every world").**
- If Z″ is obtained from Z′ by a non-null change guided at every world, then C3 for Z′ implies C3 for Z″, since Z″ ≻ Z′ everywhere. So this version is weaker as an axiom.
- But it still needs the exact Z′, so it does not reduce the dependence on μ.
- Using a guided set to *make up* a mass shortfall would require saying how much positive mass compensates for how much missing payoff. That is a quantitative trade-off between μ-mass and payoff size, which is the integral again. Not recommended.

### 2.2 What exactness was really buying

The pairing h ↔ T(h) ↔ S(h) does two jobs:
1. it matches **amounts** (pushforward equalities);
2. it matches **payoffs** (S(h) = h + T(h) exactly).

Job 1 is free: for atomless μ, any two pieces of equal mass are isomorphic. Job 2 is what produced the PDE. Payoff matching can be relaxed to **payoff domination**, and the bijections can be dropped altogether.

### 2.3 Consolidation with a margin (C3m): definition

**Margin triple of order c ∈ {1, 2}.**
- Pairwise disjoint non-null models G₁, G₂, G₃ with μ(G₁) = μ(G₂) = μ(G₃)/c.
- For μ⊗³-almost every (x, y, z) ∈ G₁ × G₂ × G₃, the gamble z pays more than (x + y)/c at every world.

For a model Z with G₁ ∪ G₂ ⊆ Z a.e. and Z ∩ G₃ null, its consolidation is Z′ = (Z ∖ (G₁ ∪ G₂)) ∪ G₃, as before.

**(C3m)** At no world is there a chain Z ⪰_ω Z₂ ⪰_ω … ⪰_ω Z′ with a strict link.

**Variants.**
- **C3p** is the pairing form. Keep bijections T, S with exact pushforwards, as in AX72, and require S(h) ≥ h + T(h), or S(h) ≥ (h + T(h))/2, at every world.
- C3p with "≥" contains AX72's exact C3 as a special case. Its strict version contains C3m, because any isomorphisms pair a margin triple.
- So exact C3 and C3m are each implied by C3p(≥).
- Everything below for C3m is proved; the satisfaction results in §2.5 also hold for C3p(≥). **C3m is the weakest form that does all the work, and the simplest to state.**

**Use of μ.** C3m uses μ beyond its null sets only through the equality of three numbers, μ(G₁) = μ(G₂) = μ(G₃)/c. It needs no maps and no density. It uses the linear structure of gambles and the pointwise payoff order; guidance already uses the latter.

**Preserved by chain unions** (PROVED). A forbidden chain with a strict link in the union lies, with its strict link, in some stage. So for finite Ω, maximal members of 𝓡 + C3m exist above any member (AX72 §0, REF72 Lemma 2).

### 2.4 Existence and the full C3.7(ii) (PROVED)

**Lemma W (witness characterisation).** Assume (M2) and (M3). Let X be a model with D_S ⊆ X a.e. and X ∩ {sup h < 0} null. For c ∈ {1, 2}, let

  W_c := {(x, y, z) ∈ X × X × (E∖X) : z − (x + y)/c ∈ D_S}.

Then X is coherent iff μ⊗³(W₁) = μ⊗³(W₂) = 0.

*Proof.*

(⇒) Suppose X = D_Q a.e. For x, y ∈ D_Q, superadditivity of P_Q and P_Q ≥ P_S give

  P_Q(z) ≥ P_Q((x + y)/c) + P_S(z − (x + y)/c) > 0.

So z ∈ D_Q, and W_c is null.

(⇐) Let X⁺ := supp(μ|X). It contains a.e. point of X, because E is separable. Put

  V := ⋃_{x, y ∈ X⁺, c ∈ {1,2}} ((x + y)/c + D_S),

which is open.

1. *V ⊆ X a.e.*
   - By Lindelöf, V is a countable union of the sets (x_k + y_k)/c + D_S.
   - If μ(V ∖ X) > 0, some k has a point z in supp(μ|((x_k + y_k)/c + D_S) ∖ X). Write 3δ := inf_Ω(z − (x_k + y_k)/c).
   - Sup-norm balls of radius δ/2 about x_k, y_k and z then give μ⊗³(W_c) > 0, a contradiction.
2. *X ⊆ cl V a.e.* For x ∈ X⁺, the term (x + x)/2 + D_S = x + D_S lies in V, and x ∈ cl(x + D_S).
3. *V ⊆ X⁺.* V is open with V ⊆ X a.e., and (M3) applies. The same holds for D_S. Hence:
   - V + V ⊆ V, because v₁ + v₂ = (v₁ − ε𝟙) + v₂ + ε𝟙 with v₁ − ε𝟙 ∈ V;
   - (V + V)/2 ⊆ V, in the same way;
   - D_S ⊆ V.
4. *V is an open convex cone.*
   - An open midpoint-convex set is convex.
   - For λ ∈ (0, 1) and v ∈ V: convexity with ε𝟙 ∈ D_S gives λ(v − η𝟙) + (1 − λ)ε𝟙 ∈ V. Choosing ε = λη/(1 − λ), this point is λv.
   - Sums give 2ᵏv ∈ V, and convexity fills in between.
5. *V misses the non-positive gambles.* Otherwise some v − ε𝟙 ∈ V has sup < 0, and an open neighbourhood of it inside V ∩ {sup < 0} has positive measure.
6. *Conclusion.*
   - By Lemma `lem:identify`(b), D_K ⊆ V ⊆ C_K for K = K_V.
   - C_K is closed and D_K ⊆ V is open, so ∂V ⊆ {P_K = 0}, which is null by (M2).
   - Hence X = V = D_K a.e. ∎

This replaces AX72's step 3 ("routine density-point argument, not written"). It is written here in full, for any Ω, without density points.

**Lemma T (margin triples exist).** Let μ be atomless. If μ⊗³(W_c) > 0, there is a margin triple of order c with G₁, G₂ ⊆ X and G₃ ⊆ E ∖ X.

*Proof.*
1. W_c = ⋃_δ {inf_Ω(z − (x+y)/c) ≥ δ}, so some δ gives a positive-measure piece.
2. Cover E by countably many sup-norm balls of radius δ/8 (E is separable). Some product B₁ × B₂ × B₃ meets that piece in positive measure.
3. For every x ∈ B₁, y ∈ B₂ and z ∈ B₃: inf(z − (x+y)/c) ≥ δ − (δ/4)(1 + 2/c) > 0.
4. By Fubini, μ(X ∩ B₁), μ(X ∩ B₂) and μ(B₃ ∖ X) are positive.
5. Choose G₁ ⊆ X ∩ B₁, G₂ ⊆ (X ∩ B₂) ∖ G₁ and G₃ ⊆ B₃ ∖ X with masses m, m and cm. Sierpiński's theorem allows this, with m small enough to keep G₁ and G₂ disjoint if B₁ ∩ B₂ ≠ ∅. ∎

**Theorem (C3.7(ii) for C3m).** Assume (M2), (M3) and μ atomless; or, with atoms, that the atomless part of μ has full support (§1.2). Let R satisfy (G), (SC) and (C3m). If a model X has, against every rival, a strict defence at some world, then X is coherent. Only (G), (SC) and C3m are used.

*Proof.*
- **Step 1 (AX72).** If D_S ∖ X is non-null, adding it is guided at every world. If X ∩ {sup h < 0} is non-null, removing it is guided at every world. In either case the rival is strictly better everywhere, and (SC) forbids a defence against it.
- **Step 2.** If X is incoherent, Lemma W gives μ⊗³(W_c) > 0 for c = 1 or 2. Lemma T gives a margin triple inside X, X and E∖X. C3m forbids a strict defence of X against the consolidation X′ at any world. Contradiction. ∎

### 2.5 Checks (i)–(iii) for C3m

**(i) It excludes R_{s'} (PROVED; NUMERICS).**
- Take x near a = (−1.5, 1), y near b = (1, −1.5), and z near (a+b)/c + δ𝟙, in balls of radius r ≪ δ.
- Per unit mass, the splitting change Z′ → Z has increment −δ (c = 1) or −2δ (c = 2) at world 1. At world 2 it is f(1) + f(−1.5) − c·f(·) ≈ +1.5 − O(δ).
- NUMERICS (`checks73.py` §1):

  | c | δ | world 1 | world 2 |
  |---|---|---|---|
  | 1 | 0.05 | −0.05 | +1.475 |
  | 2 | 0.05 | −0.10 | +1.450 |

- The change lowers s′₁, so it does not raise s′ at both worlds. Hence it is accepted at world 2 and its reverse is refused there, so Z ≻₂ Z′.
- Every distorted-score counterexample of the ROUND72 general form is excluded too: see §3.1, where C3m forces coherent Bayes sets.

**(ii) The covering constructions satisfy it (PROVED).** For a margin triple, let m = μ(G₁) and π := (μ|G₁ ⊗ μ|G₂ ⊗ μ|G₃)/(c·m²). Its marginals are μ|G₁, μ|G₂ and μ|G₃/c, so ∫_{G₃} φ dμ = c·∫ φ(z) dπ. This also works with atoms whenever the masses match.
- **R0, R∩, round-71 maximal rankings.**
  - At every ω, m_ω(Z′) − m_ω(Z) = ∫ [c·z(ω) − x(ω) − y(ω)] dπ > 0.
  - Every accepted non-null step strictly raises m_ω (Prop. `prop:structure`(b); likewise for R∩ and the round-71 maximal rankings).
  - So a chain from Z′ up to Z with a strict link would give m_ω(Z) > m_ω(Z′). Contradiction.
  - For C3p(≥) the same computation along the pairing gives ≥ 0, which also suffices.
- **Veto–Brier** (on U; triples in U).
  - Since v_i ≥ 0 and cz ≥ x + y: c[−v_i·z]⁺ ≤ [−v_i·(x+y)]⁺ ≤ [−v_i·x]⁺ + [−v_i·y]⁺. So the veto level a_i does not rise.
  - The Brier level b_i strictly falls, by the margin.
  - Each ⪯_i is a total preorder, so Z′ is strictly better than Z and no chain can return from Z′ up to Z.
  - NUMERICS: 400 random Gaussian triples; minimum m-margin 0.050 > 0; veto inequality ≥ 0.

**(iii) C3.7(ii) holds:** Theorem of §2.4, PROVED in full.

### 2.6 Limiting or approximate forms

An ε-approximate exact form, with pushforward densities in [1−ε, 1+ε] and payoffs within ε, conflicts with R0 unless the margin beats the mass error times the payoff size. That is again a quantitative trade-off and is not recommended. C3m is the useful "approximate" form: exact in amounts, and inexact for payoffs only in the direction that favours the consolidated model.

---

## 3. Is C3 the integral in disguise? (Question 3)

### 3.1 The additive scores it admits (PROVED)

**Lemma K.** Let g: E → R be continuous and superlinear (superadditive and positively homogeneous, hence concave). Let it be truth-directed at ω: g ≥ 0 on {h(ω) > 0} and g ≤ 0 on {h(ω) < 0}, strictly on a non-null set. Then, with 0 < a ≤ b,

  g(h) = a·h(ω)⁺ − b·h(ω)⁻.

*Proof.*
1. *h(ω) > 0.* For k ∈ ker δ_ω, the map t ↦ g(h(ω)𝟙 + tk) is concave and ≥ 0 on R, hence constant. So g(h) = a·h(ω), with a := g(𝟙).
2. *h(ω) = 0.* By continuity, g = 0 there.
3. *h(ω) < 0.* φ := a·δ_ω − g is sublinear and vanishes on {h(ω) ≥ 0}. For k ∈ ker δ_ω:
   - φ(−𝟙 + k) ≤ φ(−𝟙) + φ(k) = φ(−𝟙), and
   - φ(−𝟙) ≤ φ(−𝟙 + k) + φ(−k) = φ(−𝟙 + k).
   So φ(h) = (b − a)|h(ω)| with b := −g(−𝟙). Also b − a = φ(−𝟙) ≥ −φ(𝟙) = 0. ∎

**Corollary.** Consider integral scores s_ω(X) = ∫_X g_ω dμ with continuous g_ω and μ of full support. The rankings R_g of AX72 §0 satisfy (G) and C3 (exact, for the Gaussian) or C3m (any atomless μ with full support) **iff**

  s_ω(X) = a_ω∫_X h(ω)⁺ dμ − b_ω∫_X h(ω)⁻ dμ, with b_ω ≥ a_ω > 0, at every world.

*Proof.* (G) forces truth-direction a.e. C3 or C3m forces superlinearity: this is AX72 C3.7(i), and for C3m let z ↓ (x+y)/c. Then apply Lemma K. Conversely, these g are superlinear and increasing, and the chain argument gives C3m. ∎

So C3 forces each world's score to be **local** (it depends only on the payoff at that world) and **loss-neutral or loss-averse**. A loss is weighted at least as much as a gain of the same size. The linear score is a_ω = b_ω. The auditor's s′ is excluded at world 2, where gains are weighted 2 and losses ½. The common-kink counterexample E1 has the same gain-seeking shape at both worlds and is excluded for the same reason.

Without (G), for example the veto level of veto–Brier, C3m admits any superlinear, increasing density, such as min(0, v·h).

**Bayes sets.** For finite Ω and weights p, Σ_ω p_ω g_ω(h) = min over c ∈ Π_ω[a_ω, b_ω] of Σ_ω p_ω c_ω h(ω). So the Bayes set is D_Q, with Q the normalised set {(p_ω c_ω)_ω}. This is coherent, and **imprecise whenever some b_ω > a_ω**. NUMERICS: no disagreement on 2·10⁵ samples (`checks73.py` §4). C3 forces coherence of optimal models, not precision.

### 3.2 What C3 mentions

- **Exact C3:** the linear structure of gambles (sums or averages, taken at all worlds at once) and μ-amounts. It says nothing about payoff size at any single world.
- **C3m:** the same, plus the pointwise payoff order, which is the order guidance already uses. μ enters only through the equality of three masses.
- It does not mention a score, completeness, transitivity, additivity over disjoint sets, or any world-specific weighting.

### 3.3 Honest assessment

C3 is **not** the integral in disguise.
- It admits rankings that are not integral-score rankings: R0, which is incomplete and intransitive, and veto–Brier, which is lexicographic.
- Within integral scores it leaves a free loss-aversion parameter at every world.
- It is strictly weaker in reach. In §1.3 the integral-based R0 dominates an incoherent model that a C3 ranking defends, because the integral's linearity holds across all of E while C3 binds only where μ links gambles by sums.

But C3 **shares the integral's two load-bearing ideas**:
1. μ measures how much of each kind of gamble a model accepts;
2. a unit's stake is its payoff, and stakes add across units.

Its substantive cost is exactly this payoff-weighted reading of accuracy. **It rules out pure error-counting**, which scores each correct acceptance +1 and each error −1. Under counting, holding a winner and a loser beats holding their losing sum. A philosopher who counts errors should reject C3, and ROUND72 shows that such a philosopher can then have incoherent admissible models. The integral's motivation in app.tex §2 ("the payoff-weighted measure of the wrong acceptances") is the same commitment. So C3 is best described as that motivation, stated without the integral and without linearity.

### 3.4 Plain-English motivation

μ says how much of each kind of gamble a model accepts. Accepting some amount of a gamble x together with an equal amount of a gamble y pays, at every world, what accepting that amount of x + y pays (or twice that amount of their average). Suppose we pool them into gambles that pay even more than that, at every world. The pooled holding should not then count as less accurate than the split one. Splitting a commitment into pieces that add up to less cannot make a model more accurate. So no sequence of comparisons, each at least as good and one strictly better, should lead from the pooled holding up to the split holding.

### 3.5 Paper-ready statement (C3m)

> **Consolidation.** Let G₁, G₂ and G₃ be disjoint non-null models with μ(G₁) = μ(G₂) = μ(G₃), such that for almost all x ∈ G₁, y ∈ G₂ and z ∈ G₃ the gamble z pays more than x + y at every world; or with μ(G₃) = 2μ(G₁) = 2μ(G₂) and z paying more than (x + y)/2 at every world. If a model Z contains G₁ and G₂ and is disjoint from G₃, replacing G₁ ∪ G₂ by G₃ yields a model Z′ that pays more in total at every world. We require that at no world does a sequence of comparisons, each at least as good and at least one strictly better, lead from Z′ up to Z.

Short gloss for the paper: consolidation uses μ only to say that two sets of gambles are the same size. It holds for the ranking of Definition 6.1 and for the veto–Brier rankings, and it excludes every ranking that rewards splitting a commitment.

---

## 4. Bottom line for the author

1. **Replace AX72's exact C3 by C3m.** Its instances exist for every atomless μ with full support, in the paper's general setting. It needs only mass equalities, and it keeps every good property: it excludes R_{s'}, it is satisfied by R0, R∩, round-71 and veto–Brier, and C3.7(ii) is now fully proved.
2. **(M3) is needed** (counterexample §1.3). Atoms are harmless (§1.2).
3. **Score-free, C3m gives "no incoherent model is strictly defended against every rival".** Dominance in every maximal member (C3.8) is still open.
4. Exact matched triples are a PDE question (elliptic or hyperbolic, with regularity demands). They are not needed and should not appear in the paper.

## Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/MU73_report.md` (this report)
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/mu73_py/checks73.py` (sections 1–5: R_{s'} split increments under margin triples; R0 and veto–Brier inequalities; linearised type of the exact-triple system; Bayes set = D_Q for kinked scores; the (M3)-failure example)
