# PRO73: dominance under consolidation

27 Oct 2026. Setting unless stated: Ω = {1,…,n} finite, E = Rⁿ, μ the standard Gaussian (positive continuous density, finite first moment, null sets = Lebesgue null sets). D_S is the open positive orthant, −D_S the open negative orthant. "Consolidation change" means the change that adds G₃ and removes G₁ ∪ G₂ for a matched triple (sum or midpoint); its reverse is the splitting change. Class 𝓡 = (R), (G), (I), (SC), (P) with all coherent models protected.

## Results (one line each)

1. **PROVED (Theorem S).** A model that contains D_S a.e., misses −D_S a.e., and admits no consolidation change (sum or midpoint) is coherent. This finishes C3.7(ii) step 3 for arbitrary measurable models.
2. **CHECKED + NUMERICS (Lemma LT).** Matched triples of both kinds exist near every non-collinear pair for the Gaussian on Rⁿ, for every n ≥ 2. This extends C3.1 from R². Jacobian identities hold to 7·10⁻⁹ for n = 2, 3, 4.
3. **PROVED (C3.7(ii), complete).** Let R ∈ 𝓡 + (C3). A model that has a strict defence against every rival (the world may depend on the rival) is coherent.
4. **PROVED (extension audit).** Adding a consolidation change at one world, in every context, to R ∈ 𝓡 + (C3) never breaks (R), (G), (I) or (P), and keeps every strict comparison. It can break only (SC) or (C3), and only through two explicit path configurations, (O1) and (O2).
5. **CHECKED (Example R1).** Some member of 𝓡 + (C3) does not accept a consolidation change at a world, yet adding that change alone is forbidden: a chain of ties already joins the split model to its consolidation. Adding the tie in both directions is allowed there.
6. **PROVED (Theorem D).** Suppose R satisfies (G) and (SC) together with:
   - **(CA)** the consolidated model is at least as good as the split one, at every world;
   - **(TT)** transitivity through ties.

   Then every incoherent model is dominated. No maximality, (I) or (P) is used. Within 𝓡, (CA) implies (C3).
7. **PROVED (Proposition GC, Ω = {1, 2}).** The ranking R_GC accepts at ω exactly the changes that are finite sums of changes guided by ω and consolidation changes. It is in 𝓡, is transitive, satisfies (CA), and protects every coherent model. It is defined without any score. So the class of Theorem D is nonempty for two worlds, and R_GC dominates every incoherent model.
8. **PROVED (weaker objective, score-free, two worlds).**
   - Every extension of R_GC that keeps its weak and strict comparisons dominates every incoherent model.
   - In particular, every maximal member of 𝓡 + (C3), or of 𝓡 + (C3) + (CT), above R_GC does so.
   - Such maximal members exist by Zorn's lemma.
9. **PROVED, but possibly vacuous.** Every member of 𝓡 + (C3) that is complete at each world dominates every incoherent model, because completeness with (SC) gives transitivity and, with (C3), gives (CA).
   - CHECKED: no complete ranking given by world-wise integral scores is in 𝓡 + (C3) for n = 2.
   - Whether any complete member exists: UNCLEAR.
10. **OPEN (main target).** Is every incoherent model dominated in every maximal member of 𝓡 + (C3)? I found neither a proof nor a counterexample. Two steps fail:
    - (i) maximality does not give X′ ⪰ X for a consolidation X′ (items 4 and 5);
    - (ii) even when X′ is tied with X at every world, carrying a domination of X′ over to X needs (TT), which maximality does not supply.
    
    Closure under ties (CT) touches neither step.
11. **UNCLEAR.** Whether R_GC protects every coherent model for n ≥ 3. The positive functionals available to the proof are separable across worlds, and with three or more worlds a coherent model need not be the positive set of a separable function. Theorem D itself holds for every finite n; only nonemptiness of its class is open there.

**Recommendation.** Replace "maximal member of 𝓡 + (C3)" by the score-free axioms (CA) + (TT). These are the weak counterpart of consolidation, plus transitivity through ties. With them the dominance theorem is proved outright (item 6). The class is nonempty, by a score-free ranking, for two worlds (item 7). If maximality is kept, the honest statement is item 8, together with the open problem in item 10.

---

## 1. Local triples (Lemma LT): CHECKED, NUMERICS

**Statement.** Let x, y ∈ Rⁿ be non-collinear, and let s = x + y (sum) or s = (x + y)/2 (midpoint). There are a neighbourhood U of x and C¹ diffeomorphisms T, S from U onto their images with:
- T(x) = y and S(x) = s;
- S = id + T (sum) or S = (id + T)/2 (midpoint);
- for every Borel U′ ⊆ U, T_*(μ|U′) = μ|T(U′), and S_*(μ|U′) = μ|S(U′) (sum) or ½ μ|S(U′) (midpoint).

**Construction.** Let P = span(x, y), and write h = (h_P, h_⊥) with m = n − 2.
- Put T(h) = (T_P^{h_⊥}(h_P), h_⊥).
- In polar coordinates on P, T_P^{h_⊥}(r, φ) = (τ(r), φ + θ(r)), where e^{−τ²/2} = e^{−r²/2} + C and τ(r₀) = |y|.
- Then S(h) = (S_P(h_P), 2h_⊥) for sums and (S_P(h_P), h_⊥) for midpoints. S_P has the form (σ(r), φ + β(r)), where e^{−σ²/2} = λ e^{−r²/2} + C′ and σ(r₀) = |s|.
  - For sums, λ = 2^{−m} e^{3|h_⊥|²/2}.
  - For midpoints, λ = 2.
- θ(r) solves |r + τ(r)e^{iθ}| = σ(r) for sums, or = 2σ(r) for midpoints. A solution exists near r₀ because |x|, |y| and |x + y| form a non-degenerate triangle.

Both Jacobians are block-triangular, so the measure identities reduce to the radial ODEs. The construction is C¹ in h_⊥. `pro73_py/lt_check.py` checks the identities by finite differences at 200 points per case.

## 2. Density lemma and Theorem S: PROVED

**Lemma D.** Assume (LT). Let x, y be non-collinear Lebesgue density points of a model X, and let s (= x + y or (x + y)/2) be a density point of E∖X. Then there is a matched triple of that kind with G₁ ∪ G₂ ⊆ X and G₃ ∩ X null.

*Proof.*
- Let L be a Lipschitz constant for T and S near x, and put B = B(x, r).
- Let G₁ = B ∩ X ∩ T⁻¹X ∩ S⁻¹(E∖X).
- Using the pushforward identities, μ(B∖G₁) ≤ μ(B(x, r)∖X) + μ(B(y, Lr)∖X) + μ(B(s, Lr) ∩ X) = o(rⁿ), while μ(B) ≍ rⁿ.
- So μ(G₁) > 0 for small r. Then G₂ = T(G₁) and G₃ = S(G₁), and the restriction of a matched triple is matched.
- The three sets are pairwise disjoint for small r, because x, y and s are distinct. ∎

**Theorem S.** Let X be a model with D_S ⊆ X a.e. and X ∩ (−D_S) null. Suppose no matched triple has G₁ ∪ G₂ ⊆ X and G₃ ∩ X null. Then X is coherent.

*Proof.* Let X̃ be the set of density points of X and Ỹ the set of density points of E∖X. Then E∖(X̃ ∪ Ỹ) is null, and X = X̃ a.e.

- **Claim 1.** If x, y ∈ X̃ are non-collinear, then a ball about s lies in X̃.
  - Fix s′ ∈ B(s, r). The maps x′ ↦ s′ − x′ (sum) and x′ ↦ 2s′ − x′ (midpoint) send B(x, r) into B(y, 3r) and preserve Lebesgue measure.
  - For small r, uniformly in s′, all but a small fraction of x′ ∈ B(x, r) have x′ ∈ X̃ and y′ ∈ X̃, and these pairs are non-collinear.
  - By Lemma D and the hypothesis, s′ ∉ Ỹ. So B(s, r) ⊆ X̃ ∪ null, so B(s, r)∖X is null, and every point of B(s, r) is a density point of X.
- **Claim 2.** Let K = int X̃.
  - D_S ⊆ K, because an open set that lies a.e. in X consists of density points of X.
  - K ∩ (−D_S) = ∅, by the same reasoning applied to E∖X.
  - K is closed under sums and midpoints: for non-collinear points use Claim 1; for collinear points perturb to x + δ and y − δ inside K.
- **Claim 3.** K is an open convex cone.
  - An open midpoint-convex set is convex.
  - Closure under sums gives tx ∈ K for t ≥ 1.
  - For 0 < t < 1, write tx = t(x + b) + (1 − t)d with d ∈ D_S small and b = −(1 − t)d/t.
  - 0 ∉ K, since K misses −D_S.
- **Claim 4.** X = K a.e.
  - For x ∈ X̃ and small d ∈ D_S not collinear with x, Claim 1 gives x + εd ∈ K for small ε > 0. So X̃ ⊆ cl K.
  - The boundary of a convex set is Lebesgue-null.
- **Conclusion.** K is a convex cone with 0 ∉ K that contains every h with inf h > 0. By app.tex Lemma `lem:identify`(b) and (M2), K = D_{K_K} a.e. ∎

**C3.7(ii), complete.** Let X have a strict defence against every rival.
- If D_S∖X or X ∩ (−D_S) is non-null, then Y = (X ∪ D_S)∖(−D_S) differs from X and the change is guided at every world. So Y ≻_ω X at every ω, and (SC) forbids a defence against Y.
- If some consolidation change is available to X, then (C3) forbids a defence against its result X′.
- Theorem S then shows that X is coherent. ∎

## 3. Extension audit: PROVED

Let R ∈ 𝓡 + (C3), let d be a consolidation change, and suppose d is not accepted at ω. Let R⁺ add d at ω in every context: W′ ⪰ W for every W ⊇ G₁ ∪ G₂ with W ∩ G₃ null, where W′ = (W∖(G₁ ∪ G₂)) ∪ G₃.

- **(R), (I).** Clear.
- **(G).** A splitting change is never guided: the parts h and T(h) would pay off at ω while their sum loses there.
- **(P).** No coherent model contains G₁ ∪ G₂ while missing G₃ (coherent models are convex cones). So no new comparison starts from a coherent model.
- **Strict comparisons kept.** The only pairs that change are d-instances. A strict W ≻ W′ in R is forbidden by (C3).
- **New links are strict.** W ⪰ W′ in R would make −d accepted with d not accepted, which is a strict splitting preference, and (C3) forbids it.
- **What can fail:**
  - **(O1)** there are contexts W₁, …, W_k and R-chains at ω from W_i down to W′_{i+1} (indices mod k);
  - **(O2)** there are a triple τ″ with split model Z and consolidation Z″, and contexts with R-chains Z ⇝ W′₁, W₁ ⇝ W′₂, …, W_k ⇝ Z″.
- R⁺ ∈ 𝓡 + (C3) iff neither configuration exists.
- Adding −d alone always violates (C3). Adding d and −d together removes the strictness of the new links, but it can still fail, through an old strict chain from W′ up to W, or through (O2) with −d-links.

**Consequence.** Let R be maximal in 𝓡 + (C3), and let X be incoherent and undominated. Then:
- X ⊇ D_S a.e. and X ∩ (−D_S) is null;
- by Theorem S, X admits a consolidation change d;
- for each such d, either d is a tie at every world, or at some world d is not accepted and adding it is blocked by (O1) or (O2).

## 4. Example R1: CHECKED

**Construction.**
- Start from R0, the manuscript rule with the linear score m. It lies in 𝓡 + (C3).
- Take a sum triple d. Note that Δm(d) = 0 at both worlds.
- Take a change e = (E⁺, E⁻) with E± small balls in −D_S, disjoint from the G_i, and Δm₁(e) = 0.
- At world 1, add ties for ±e and ±(d − e).

**R1 ∈ 𝓡 + (C3).**
- These four changes are unavailable to every coherent model, since each removes an inconsistent set. So (P) holds.
- They are neither guided nor anti-guided at world 1.
- Every accepted link has Δm₁ ≥ 0, and every strict link has Δm₁ > 0. This gives (SC) and (C3).

**What R1 shows.**
- R1 contains W ~₁ W + e ~₁ W′, but not W′ ⪰₁ W.
- So adding d alone at world 1 creates W′ ≻ W ~ ~ W′. That is (O1) with k = 1.
- Adding the tie {d, −d} is allowed, by the same Δm argument.

So maximality cannot be expected to force acceptance of single consolidation changes. At best it forces ties, which is case (a) of C3.8.

## 5. Theorem D: PROVED

**Axioms.**
- **(CA)** For every matched triple and every world, W′ ⪰_ω W.
- **(TT)** If Z ~_ω X and Y ⪰_ω Z, then Y ⪰_ω X.

**Theorem.** Assume (G), (SC), (CA) and (TT), with finite Ω and Gaussian μ on Rⁿ. Then every incoherent model is dominated.

*Proof.* Suppose X is incoherent and undominated.

1. X ⊇ D_S a.e. and X ∩ (−D_S) is null. Otherwise the rival guided at every world dominates X, by (G).
2. **Tie lemma.** If Z ~_ω X at every ω, then Z is undominated.
   - Suppose Y dominates Z. Then (TT) gives Y ⪰ X at every world.
   - At the world where Y ≻ Z, the comparison X ⪰ Y would close the chain Z ⪰ X ⪰ Y against Y ≻ Z, which (SC) forbids.
   - So Y dominates X, a contradiction.
3. **Consolidations are ties.** For any consolidation X′ of an undominated X, (CA) gives X′ ⪰ X at every world. Undominatedness gives X ⪰ X′ at every world. So X′ ~ X, and X′ is undominated by step 2.
4. **No D_S piece is ever removed.** No undominated model admits a consolidation with G₂ ⊆ D_S: by step 3 the result would be undominated, yet it misses part of D_S, contradicting step 1.
5. **X admits no consolidation.** Suppose X admits one.
   - Restrict it to G₁ ∩ B(x₀, ρ), where x₀ is a density point of G₁, and call the result X′. X′ is undominated by step 3.
   - Take z = x₀. Choose w in the annulus 3ρ < |w − x₀| < 5ρ with z − w ∈ D_S, w a density point of X, and w not collinear with z. Such w form a set of positive measure for small ρ.
   - Then w and d = z − w are density points of X′, since X′ agrees with X near them, and z is a density point of E∖X′.
   - Lemma D gives a sum triple for X′ with G₂ ⊆ D_S, contradicting step 4 for X′.
6. By Theorem S, X is coherent, a contradiction. ∎

**Remarks.**
- Within 𝓡, (CA) implies (C3): a strict chain from split to consolidated, closed by W′ ⪰ W, violates (SC).
- In any 𝓡-member satisfying (CA) and (TT), closure under ties holds automatically. A model tied everywhere with an undominated coherent model is undominated (step 2), hence coherent (Theorem D).
- **Item 9.** Completeness with (SC) gives transitivity, hence (TT). Completeness with (C3) gives (CA).
- **CHECKED.** With n = 2, consider complete integral rankings "s_ω(X) ≥ s_ω(Y)". (C3) forces superlinear g_ω. (P) together with Lyapunov's theorem forces a single π with π·g = 0 on both mixed quadrants. Then g₁ = −c·g₂ there, so both are linear on each quadrant, and continuity at the axes contradicts the sign conditions.

## 6. Proposition GC: PROVED for Ω = {1, 2}

**Definition.** cone_ω is the set of finite sums of signed measures of three kinds:
- ±1_K μ, with K ⊆ {h_ω > 0} for + and K ⊆ {h_ω < 0} for −;
- (1_{G₃} − 1_{G₁} − 1_{G₂})μ, for any matched triple of either kind.

X ⪰_ω Y iff (1_X − 1_Y)μ ∈ cone_ω.

**Membership in 𝓡, transitivity and (CA).**
- (R) and (I) hold.
- Transitivity holds, because 1_X − 1_Z = (1_X − 1_Y) + (1_Y − 1_Z). So (SC) and (TT) hold.
- (CA) holds by construction.
- **(G).** Every element of cone_ω has ∫ h_ω dν ≥ 0, while the reverse of a non-null guided change has ∫ h_ω dν < 0.

**(P).**
- Every functional ν ↦ ∫ f(h_ω) dν, with f(t) = c₊t for t > 0 and f(t) = c₋t for t < 0 and c₋ ≥ c₊ ≥ 0, is non-negative on cone_ω. It is non-negative on the guided pieces by the signs, and on consolidation pieces because f is superadditive and concave.
- Each coherent model is D_Q with Q = {(t, 1 − t) : a ≤ t ≤ b}. Put:
  - c₊¹ = 1 and c₋² = (1 − a)/a;
  - c₊² = s and c₋¹ = s·b/(1 − b), with s ∈ [(1 − b)/b, (1 − a)/a], which is nonempty since a ≤ b.
  
  Then F = f₁(h₁) + f₂(h₂) has {F > 0} = D_Q up to its two boundary rays. In the edge cases a = 0 or b = 1 the corresponding c₊ is 0.
  - For Q = S, use F = Σ c₋ min(h_ω, 0) if A is non-null, and F = h₁ otherwise.
- If Y ⪰_ω D_Q at both worlds and Y ≠ D_Q a.e., then ν = 1_A − 1_B, with A outside D_Q and B ⊆ D_Q, gives 0 ≤ ∫ F dν = ∫_A F − ∫_B F < 0, a contradiction.
- So no coherent model has a weak dominator other than itself.
- NUMERICS: {F > 0} agrees with D_Q at 10⁶ sample points.

**Item 8.** Strict-preserving extensions keep Y ⪰ X at every world and the strict comparison, so domination in R_GC persists. Chain unions preserve (C3) and (CT), and Ω is finite, so Zorn's lemma gives maximal members above R_GC.

## 7. The main target: precise obstruction (item 10)

Let R be maximal in 𝓡 + (C3), and let X be incoherent and undominated.

**What is proved.**
- X ⊇ D_S a.e., X ∩ (−D_S) is null, and X admits a consolidation change d (Theorem S).
- Each such d is a tie at every world, or is blocked at some world by (O1) or (O2) (section 3).

**What is missing.**
- **(a) Ties.** Even when X′ ~ X at every world, the contradiction in Theorem D needs a guided dominator of a later consolidation X″ to dominate X. Without (TT), adding Y ⪰_ω X is an independence-wide addition of the change X→Y. It can be blocked in other contexts, exactly as in (O1).
- **(b) Context blocking.** (O1) with k ≥ 2 needs only chains W₁ ⇝ W′₂ and W₂ ⇝ W′₁ in different contexts. (C3) says nothing about these.
- **Search.** I did not find a member of 𝓡 + (C3) in which both d and the tie {d, −d} are blocked at a world. A score-based search cannot find one: in any ranking whose links all satisfy Δs ≥ 0 with Δs(d) = 0, the tie is always addable. So a counterexample, if one exists, must be non-additive.
- **(CT).** Closure under ties constrains only ties with coherent models. Steps (a) and (b) involve only incoherent models, so (CT) gives nothing here. Whether (CT) together with maximality implies (TT): UNCLEAR.

**Nearby results that are available.**
- Theorem D, with (CA) + (TT) in place of maximality.
- Item 8, maximality above the score-free R_GC.
- Item 9, complete members.
- C3.7(ii), now complete.

## Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/PRO73_report.md`
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/pro73_py/lt_check.py`: Jacobian check of the local triples (n = 2, 3, 4; sum and midpoint), and the check that {F > 0} = D_Q.
