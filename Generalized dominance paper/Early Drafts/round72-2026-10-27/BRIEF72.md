# Round 72 brief (27 Oct 2026)

## Setting (the application paper app.tex, §2)
- Worlds Ω; gamble space E (finite-dimensional R^n here unless stated).
- μ: a finite measure with a positive density and a finite first moment (e.g. Gaussian).
- Models: measurable sets of gambles modulo μ-null sets. A model is coherent iff it equals D_Q a.e. for a credal set Q. Every D_Q is a convex cone.
- Change from Y to X: adds A = X∖Y and removes B = Y∖X. It is available to C iff B ⊆ C and A ∩ C is null.
- Guided at ω: A ⊆ {h(ω) > 0} and B ⊆ {h(ω) < 0}, modulo null sets.
- Dominance (manuscript definitions): Y dominates X iff Y ⪰_ω X at every world, and at some world the reverse comparison fails (strict).

## Score-free ranking class 𝓡 (no score, no integral in the axioms)
A ranking gives one relation ⪰_ω on models for each world, satisfying:
- (R) Reflexivity. A.e.-equal models are tied.
- (G) Strict guidance. If the change Y→X is guided at ω, then X ≻_ω Y: X ⪰_ω Y, and not Y ⪰_ω X.
- (I) Independence. The verdict at ω depends only on the change (A, B), not on the unchanged background.
- (SC) Chain condition (Suzumura consistency). No chain X1 ⪰_ω X2 ⪰_ω … ⪰_ω Xk has Xk ≻_ω X1.
  - The weaker three-model condition (TC) is: A ⪯ B and B ⪯ C imply not C ≺ A.
- (P) Admissibility. Every model in a protected family 𝓟 is undominated.
  - For the counterexample, 𝓟 = all coherent models, under one ranking (the strongest premise).
- Closure under ties is NOT assumed. If it is used anywhere, label it separately, in words.

Two notions of extension, for "maximal in 𝓡":
- (E-strict), Suzumura extension. R ⊆ R′ as weak relations, AND every strict preference of R is strict in R′.
- (E-incl), ordinary inclusion of weak relations. Strict preferences may become ties.

Objective. Every incoherent model is dominated under every maximal member of 𝓡. The dominator need not be coherent or undominated.

## The proposed counterexample (auditor's two-world version; to be refereed)
Ω = {1,2}, E = R², μ Gaussian.
- s′_1(X) = ∫_X h_1 dμ.
- s′_2(X) = ∫_X f(h_2) dμ, where f(t) = 2t for t ≥ 0 and f(t) = t/2 for t < 0.

R_{s′}: at ω, accept a non-null change if it strictly raises s′_ω. One exception: a change that some coherent model could make, and that raises s′ at both worlds, is refused at exactly one world where it is not guided. Such a world exists by the guidance-protection lemma, which concerns sets only.

X* = {h : h_1 + f(h_2) > 0} is the unique maximiser of s′_1 + s′_2. It is incoherent: a = (−3/2, 1) and b = (1, −3/2) are in X*, but a + b is not, and this persists on neighbourhoods.

Claims:
- R_{s′} ∈ 𝓡.
- X* is strictly preferred to every rival Y at some world.
- So X* stays undominated in every (E-strict) extension, including the maximal ones. These exist for finite Ω by Zorn's lemma, since chain unions preserve (R), (G), (I), (SC) and (P) when Ω is finite.

## Lead's earlier note
Weights common to all worlds only change μ, and are harmless. The counterexample uses a world-dependent distortion of payoff magnitudes.
