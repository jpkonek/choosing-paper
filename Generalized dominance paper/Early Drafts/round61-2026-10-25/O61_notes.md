# O61 — Obstructor notes: where visibility is necessary, and where it is not (25 Oct 2026)

Labels: PROVED (here, not refereed) / CHECKED / CONJECTURE / NUMERICS. Scripts: `o61py/` in this folder
(`geom.py`, `search.py`, `lpcheck.py`, `cuts.py`, `hexcheck.py`, `tangential.py`). Plain English throughout.

---

## 0. Verdict in brief

1. **The obstruction is real and much more robust than S2 claims.** For rankings whose levels at each
   world are some non-negative "veto" levels followed by an error level, I prove that non-visible
   corners cannot be covered. The vetoes may be any measurable non-negative integrands, at any number
   of levels. They need not be convex, homogeneous or continuous, and need not vanish on the target in
   advance. The domain may be any one-sided domain with (LF). With a Brier-type error level
   (Theorem A), all non-visible extreme points must lie in one face of K exposed by a single prior π.
   For polytopes this means **at most one non-visible vertex**. The reversed triangle has three, so it
   is not covered. With a convex error level (Theorem B, which is S5 made rigorous and strengthened),
   the reversed triangle is again not covered.
2. **"Every extreme point visible" is not necessary, even for VB-type rankings.** One extreme point can
   be exempt (Theorem C, PROVED). The auditor's theorem extends to K = conv(K′ ∪ A₁ ∪ … ∪ Aₙ ∪ {π\*})
   for any π\* ∈ K. For polytopes in relint Δ₃ this gives a near-exact characterisation in the
   veto-plus-Brier class:
   - all but at most one vertex strictly visible ⇒ covered;
   - two vertices that are not even weakly visible ⇒ not covered.
   The only gap is tangential visibility.
3. **The reversed triangle sits exactly on the boundary.**
   - Chamfer all three corners by chords, however short: every new vertex is strictly visible, so the
     auditor's theorem itself covers the hexagon (NUMERICS/CHECKED).
   - Chamfer two corners: the exemption covers the pentagon.
   - So the reversed triangle is a Hausdorff limit of covered polytopes. Only the sharp corners fail.
4. **In the full class the question stays open.** The full class is complete, transitive,
   finite-statistics (IB) rankings. It contains single-level additive rankings with arbitrary measurable
   sign-correct integrands. Covering by those is the CPM realisation problem with non-tangency relaxed.
   So a necessity theorem for the full class would settle that problem for the reversed triangle. I
   isolate exactly what an escape must use (§7). No axiom of the binding framework has to be given up.
   What must go is the architecture "vetoes, then a Brier or convex error level".

---

## 1. Setting, classes, and visibility

**Setting** (binding).
- Worlds 1..n. μ is absolutely continuous with a finite first moment.
- The domain is one-sided: there is a measurable A ⊆ ℝⁿ with A ∩ (−A) = ∅, and the models are the
  measurable X ⊆ A, modulo null sets.
  - A forced part L ⊆ X can be added. (IB) cancels it, and every statement below goes through with
    statistics taken relative to L. I suppress it.
  - I do not assume that A is convex. (LF) at D_K: A ⊇ D_K, and A contains an open neighbourhood of
    ∂D_K∖0.
- A model X is coherent if X = A ∩ D_Q a.e. for some nonempty closed convex Q ⊆ Δ. The stricter reading
  X = D_Q also works: every use below is an inclusion.
- K ⊆ relint Δ is closed and convex.

**Remark 1.1 (PROVED).** A one-sided domain with (LF) at D_K forces K to be full-dimensional.
- If K is lower-dimensional, cl D_K contains a line ℓ = cone(K)^⊥.
- Its points are boundary points of D_K, so (LF) makes both h and −h available near ℓ. That is a
  two-sided problem.
- So precise models and lower-dimensional K need two-sided domains. This answers part of P61(b)
  negatively.

**Faces.** For an extreme point v of K, let F_v := {h ∈ cl D_K : v·h = 0}, the normal cone of K at v. It
is nonzero, pointed and convex. Each world j stands in one of three relations to v:
- **weakly visible from j:** F_v ⊆ {h_j ≤ 0}. By bipolarity this is v − e_j ∈ cl T_K(v), the tangent
  cone, since h_j = (e_j − v)·h on F_v.
- **strictly visible from j:** v + t(v − e_j) ∈ relint K for some t > 0. Equivalently,
  v ∈ conv(K′ ∪ {e_j}) for some compact K′ ⊆ relint K.
- **non-visible from j:** F_v meets {h_j > 0}. This splits into anti-visible (F_v ⊆ {h_j ≥ 0}) and
  crossing (both signs occur).

v is **non-visible** if it is non-visible from every world. **Tangential** means weakly but not strictly
visible.

**Classes of rankings.** Every class below is complete and transitive at each world.
- **𝒢** (the full class of the question): world k ranks models lexicographically by finitely many
  integral levels ∫_X f_{k,1}, …, ∫_X f_{k,r}, with each f_{k,i} integrable (see §2 for why this is the
  general form).
- **𝒱** (veto-first rankings): at world k, the first r_k levels have non-negative integrands φ_{k,i} ≥ 0
  (vetoes; r_k = 0 is allowed). The next level, the error level ℓ_k, is *strict*: ℓ_k ≠ 0 a.e. on the
  veto-free set Z_k := A ∩ ⋂_i {φ_{k,i} = 0}. Any further levels are arbitrary.
- **𝒱_B:** 𝒱 with a Brier-type error level, ℓ_k(h) = −w(h)h_k on N := ⋂_k Z_k, with one weight
  w > 0 for all worlds. Brier itself is w ≡ 1.
- **𝒱_conv:** 𝒱 with each ℓ_k convex, hence continuous, on an open convex set G ⊇ A. This is the
  brief's "concave sign-correct secondary scores" with the sign convention of losses.

VB, the auditor's ranking, and the S2 class all lie in 𝒱_B. Neither convexity nor homogeneity of the
vetoes is assumed anywhere below.

---

## 2. S6 (Hausner–Wendel), and what the general form really is

**S6 as stated (PROVED; standard).**
- Let ⪯ be a complete, transitive, translation-invariant and positively homogeneous preorder on ℝ^k.
- Then P := {x ⪰ 0} is a convex cone with P ∪ (−P) = ℝ^k. N := P ∩ (−P) is a subspace, and ℝ^k/N is a
  totally ordered real vector space.
- Hausner–Wendel then gives linear functionals λ₁..λ_r with x ⪰ 0 ⟺ (λ₁x, …, λ_rx) ≥_lex 0.
- Only finitely many statistics are needed. On Z − Z, which is a symmetric convex neighbourhood of 0 in
  its span (Lyapunov), the cone can be extended by homogeneity.

**Hypotheses that are not automatic.**
- (a) **Translation invariance.** I take finite-statistics (IB) to *mean* that X ⪯_k Y depends only on
  z(X) − z(Y). This follows from the splice form of (IB) and Lyapunov when there is room to move the
  common part, but I have not checked the global case. CONJECTURE that it holds in general.
- (b) **Rational homogeneity is forced; real homogeneity is not (PROVED).**
  - Rational homogeneity: suppose X ⪯ Y differ on P ∪ Q with d = z(P) − z(Q). Lyapunov halves P and Q
    exactly, giving X₁ with z(X₁) − z(Y) = d/2.
  - If d/2 ⋡ 0 failed, then Y ≺ X₁ ≺ X, contradicting X ⪯ Y. Thirds work the same way.
  - Real homogeneity fails in general. Take statistics (Brier, τ) at world k and the order "Brier, then
    f(τ-difference)", with f additive but not linear (Hamel basis).
  - This order is complete, transitive and translation-invariant, and it satisfies (G), since every
    guidance move changes Brier strictly. It is not ℝ-homogeneous.
  - So S6 needs homogeneity, or a measurability or Archimedean hypothesis, as an explicit assumption.
    Such pathological tie-breakers also defeat the compactness step of LDG Lemma lem:zorn.
- (c) **The general form is 𝒢, not 𝒱.** S6 yields levels with arbitrary integrable integrands
  f_{k,i} = Σ_s c_{k,i,s}g_s. They need not be vetoes.
  - (G) forces exactly this (PROVED): a.e. on A ∩ {h_k > 0}, the vector (f_{k,1}(h), …, f_{k,r}(h)) is
    <_lex 0, and a.e. on A ∩ {h_k < 0} it is >_lex 0.
  - So the leading level is always weakly sign-correct: ≤ 0 on correct acceptances and ≥ 0 on wrong ones.
  - It is a veto exactly when it is ≥ 0. The obstruction theorems below are about 𝒱. §7 says what lies
    in 𝒢 ∖ 𝒱.

---

## 3. Four lemmas valid for every 𝒱-ranking on every one-sided (LF) domain

**Standing hypotheses.**
- K ⊆ relint Δ (closed, convex).
- A 𝒱-ranking with (G).
- D_K is undominated.
- The models named in Lemma 3 are coherent. This is all that "every undominated model is coherent" is
  used for.

**Lemma 1 (vetoes are silent on correct advice; PROVED).** Every φ_{k,i} = 0 a.e. on A ∩ {h_k > 0}.
- Otherwise take the first level i at which this fails, and a non-null S ⊆ A ∩ {h_k > 0} on which
  φ_{k,i} > 0 and all earlier vetoes vanish.
- Then S ∖ S = ∅ beats S at world k at level i. But ∅ is a strict world-k worsening of S, which (G)
  forbids.
- Consequently Z_k ⊇ A ∩ {h_k > 0} a.e. Also, on Z_k, (G) and strictness give ℓ_k < 0 a.e. on {h_k > 0}
  and ℓ_k > 0 a.e. on {h_k < 0}.

**Lemma 2 (= S3, strengthened: the target pays no veto; PROVED).** D_K ⊆ Z_k a.e. for every k.
- Let W₀ = {k : every veto of D_K at world k is 0}. For k ∉ W₀, let κ_k be the first veto level that
  D_K pays.
- Let 𝒵 be the models whose vetoes at W₀-worlds are all 0 and whose vetoes at levels < κ_k (k ∉ W₀)
  are 0.
  - These are exactly the models inside a fixed set, so their range is convex.
  - 𝒵 contains D_K and ∅. All statistics of ∅ vanish, so no auxiliary "all-zero model" hypothesis is
    needed.
- A model in 𝒵 with b_k < b_k(D_K) for every k ∈ W₀ and a_{k,κ_k} < a_{k,κ_k}(D_K) for every k ∉ W₀ would
  strictly dominate D_K. Here b_k := ∫ℓ_k.
- Separation gives β ≥ 0 on W₀ and α ≥ 0 off W₀, not both zero, such that D_K minimises
  J = Σ_{W₀}β_k b_k + Σ_{∉W₀}α_k a_{k,κ_k} over 𝒵.
  - If β = 0, then J(∅) = 0 < J(D_K), a contradiction. So β ≠ 0.
  - Minimality gives g := Σβ_kℓ_k + Σα_kφ_{k,κ_k} ≤ 0 a.e. on D_K, hence Σ_{W₀}β_kℓ_k ≤ 0 a.e. on D_K.
- If W₀ ≠ [n], pick j₀ ∉ W₀. The open set O := D_K ∩ {h_k < 0 ∀k ∈ W₀} is nonempty: it contains
  −Σ_{W₀}e_k + Me_{j₀} for large M, because min_K m_{j₀} > 0.
  - On O the W₀-vetoes vanish (they vanish on D_K), so ℓ_k > 0 a.e. there by Lemma 1.
  - So Σβ_kℓ_k > 0 a.e. on O, a contradiction. Hence W₀ = [n]. ∎
- This holds for *any* strict error level, not only Brier. The only place K ⊆ relint Δ is used is
  min_K m_{j₀} > 0.
- **Escape E3:** for K touching ∂Δ, Lemma 2 can fail, and the target may pay vetoes. This does not
  matter for the reversed triangle.

**Lemma 3 (slab pieces of zero sets are forced to be coherent; PROVED).** For j ≠ k, the model
X_{kj} := Z_k ∩ A ∩ {h_j > 0} is undominated.
- X_{kj} ⊆ Z_j by Lemma 1, and ⊆ Z_k, so it pays no veto at worlds j and k.
- Let Y weakly dominate X_{kj}. Lexicographic order with non-negative vetoes forces Y's vetoes at j and k
  to vanish, so Y ⊆ Z_j ∩ Z_k, and also b_j(Y) ≤ b_j(X_{kj}).
- On Z_j, ℓ_j has the sign of −h_j a.e. So X_{kj} = Z_j ∩ Z_k ∩ {ℓ_j < 0} is the a.e.-unique minimiser
  of b_j over models inside Z_j ∩ Z_k. Hence Y = X_{kj}. ∎
- Later levels play no role. So under the coverage requirement, **Z_k ∩ {h_j > 0} must be a.e.
  A ∩ D_Q**, a convex cone intersected with A. **This replaces S4**; see §6.

**Lemma 4 (collar forcing; PROVED).** Let v ∈ ext K be non-visible. Then every r ∈ relint F_v has a ball
B(r, ρ) contained a.e. in N = ⋂_k Z_k.
- *Spreading step.* Let j be a world and P_j := relint F_v ∩ {h_j > 0}, a relatively open convex cone.
  Let D_Q be an open convex cone containing D_K ∩ {h_j > 0} and a ball B(p, ρ) with p ∈ P_j. Then D_Q
  contains a ball around every r ∈ P_j.
  - If r = sp, use homogeneity.
  - Otherwise q := r + t(r − p) ∈ P_j for small t, and r = λp + (1 − λ)q with λ = t/(1 + t).
  - Any h ∈ B(r, λρ/2) can be written λ(p + d) + (1 − λ)(q + ζ𝟙) with |d| < ρ and small ζ > 0.
  - Since q + ζ𝟙 ∈ D_K ∩ {h_j > 0}, convexity gives h ∈ D_Q.
- *From a.e. to genuine inclusion.* If an open O ⊆ A lies a.e. in A ∩ D_Q, then O ⊆ int cl D_Q = D_Q.
- *Induction along the overlap graph.* Fix k. The worlds j with P_j ≠ ∅ are all worlds, because v is
  non-visible. Join j and l when P_j ∩ P_l ≠ ∅.
  - This graph is connected. Along a segment from a ∈ P_j to b ∈ P_l inside relint F_v ∌ 0, the open
    intervals {t : γ(t)_i > 0} cover [0, 1], since every nonzero point of F_v has a positive coordinate.
    An open interval cover of a connected set has a connected overlap graph.
  - Start: for r ∈ P_k, B(r, ρ) ⊆ A ∩ {h_k > 0} ⊆ Z_k, by (LF) and Lemma 1.
  - Step: suppose balls around all of P_j lie in Z_k, and l ~ j with l ≠ k. Pick p ∈ P_j ∩ P_l. By
    Lemma 3, X_{kl} = A ∩ D_Q contains B(p, ρ), and it contains D_K ∩ {h_l > 0} by Lemma 2.
  - Spreading then puts balls around all of P_l into D_Q ∩ A ∩ {h_l > 0} = X_{kl} ⊆ Z_k.
- Since relint F_v = ∪_j P_j, and there are finitely many k, the claim follows. ∎

In the convex-veto setting of S2 a one-line version suffices, and S2's collar claim is CHECKED in that
setting. The point of Lemma 4 is that convexity of the vetoes is never needed: coherence of the
X_{kl} supplies exactly the convexity that is used.

---

## 4. Theorem A (Brier-type error levels)

**Theorem A (PROVED).**
- Hypotheses: a 𝒱_B-ranking on a one-sided domain with (LF) at D_K, K ⊆ relint Δ, D_K undominated, and
  the models X_{kj} coherent.
- Conclusion: there is π ∈ K with π·h = 0 for every h ∈ F_v and every non-visible extreme point v.
- Equivalently, the faces G_v := {m ∈ K : m ⊥ F_v}, which are the faces exposed by relint F_v, have a
  common point.

*Proof.*
1. By Lemma 2, D_K ⊆ N a.e. Every Y ⊆ N pays no veto anywhere. Its error vector is
   b(Y) = (−∫_Y w h_k)_k, and the range of b over models inside N is convex (Lyapunov).
2. D_K is not strictly dominated inside N. So some π ∈ Δ has D_K minimising −∫_Y w π·h over Y ⊆ N.
   Hence D_K ⊇ N ∩ {π·h > 0} and D_K ∩ {π·h < 0} is null. The latter gives π ∈ K.
3. Fix v non-visible and r ∈ relint F_v. Lemma 4 gives B(r, ρ) ⊆ N.
   - If π·r > 0, shrink ρ until π·h > 0 on the ball. Then the ball lies a.e. in D_K.
   - But the ball contains the open set {v·h < 0}, which lies outside cl D_K. Contradiction.
   - So π·r = 0 on relint F_v, hence on F_v. ∎

The proof also shows *how* the target fails: if no such π exists, some veto-free model *strictly*
dominates D_K. Removals from D_K are allowed, so S2's positive-combination condition is not needed.

**Corollaries (PROVED).**
- (a) **Polytopes.** F_v is a facet of cl D_K, so G_v = {v}. Hence at most one vertex is non-visible.
- (b) **Reversed triangle K = {m_i ≤ 2/5}.** Every vertex is anti-visible from one world and crossing for
  the other two (CHECKED, `geom.py`). So **no 𝒱_B-ranking covers it, on any one-sided (LF) domain**,
  whatever the vetoes (measurable, any number of levels) and whatever later levels follow.
- (c) **n = 3 smooth points are never non-visible.** If F_v is a ray ℝ₊r, then v·r = 0 and v ≫ 0 give
  some r_j < 0, so v is visible from j. Strict visibility also holds, since (v − e_j)·r = −r_j > 0.
- (d) **Tangential corners count as non-visible (PROVED; sketch only, not refereed).**
  - Let v be tangential from exactly one world i and non-visible from the others. Let r ∈ F_v with
    r_i = 0, and pick j with r_j > 0.
  - X_{ij} contains A ∩ {h_i > 0} near r and D_K ∩ {h_j > 0}.
  - Their convex hull contains an open set just beyond relint F_v near r. The construction: combine
    p = r + γe_i − δ𝟙, with γv_i < δ < γ, with q = r′ + ζ𝟙, r′ ∈ relint F_v.
  - Lemma 4 for k ≠ i then puts that set in N, and the proof of Theorem A gives π = v.
  - A corner tangential from *two* worlds (one at each boundary ray of F_v) is not settled. CONJECTURE:
    it also counts as non-visible.

S2's example points CHECKED (`geom.py`):
- (4,0,−2) ∈ relint F_{v₁}, (−2,0,4) ∈ relint F_{v₃} and ½(−1,2,0) ∈ relint F_{v₂}.
- Their sum is (1.5, 1, 2) ≫ 0.

NUMERICS (`lpcheck.py`, 6·10⁴ Gaussian samples, linear-programming relaxation x_h ∈ [0,1], which is the
Lyapunov convexification):
- Over models inside D_K ∪ collars of width δ, the best *uniform* Brier gain against D_K is
  3.0·10⁻³, 6.7·10⁻³ and 1.0·10⁻² for δ = .02, .05, .1. So D_K is strictly dominated.
- Control: with N = D_K the gain is 1·10⁻¹⁰.

---

## 5. Theorem B (convex error levels: S5 made rigorous)

**Theorem B (PROVED).** No 𝒱_conv-ranking covers the reversed triangle. The vetoes are arbitrary
measurable and the domain is any one-sided (LF) domain contained in G.

*Proof.*
1. **The target's error-level prior.** As in Theorem A, steps 1–2, with ℓ in place of −wh: there is
   π ∈ Δ with D_K ⊇ N ∩ {Γ < 0} and D_K ∩ {Γ > 0} null, where Γ := Σπ_jℓ_j.
2. **Γ vanishes on each face.** On a ball B(r, ρ) ⊆ N around r ∈ relint F_v (Lemma 4): Γ ≤ 0 a.e. on
   B ∩ D_K and Γ ≥ 0 a.e. on B ∖ cl D_K. By continuity Γ = 0 on relint F_v, for all three vertices.
3. **Each π_jℓ_j is affine on each face.** A sum of convex functions that is linear on a convex set has
   each summand affine there.
4. **A crossing world is a multiple of h_j on the face.** Let j cross at v. On B ⊆ N ⊆ Z_j, ℓ_j has the
   sign of −h_j a.e. So ℓ_j = 0 on relint F_v ∩ {h_j = 0}, which is an open ray. The affine function is
   therefore linear and equals −κh_j on span F_v.
5. **One slope per world (subgradient step).**
   - At r₀ ∈ relint F_v with r₀_j = 0, ℓ_j vanishes on a relative neighbourhood of r₀ in {h_j = 0}. So
     every subgradient at r₀ is −κe_j.
   - Hence ℓ_j ≥ −κh_j on all of G.
   - On any other crossing face, ℓ_j = −κ′h_j with h_j taking both signs, which forces κ′ = κ =: κ̂_j.
   - κ̂_j > 0: otherwise ℓ_j ≥ 0, contradicting ℓ_j < 0 a.e. on A ∩ {h_j > 0}.
6. **The three rays.** The rays of cl D_K are r₁₂ = (2,2,−3), r₁₃ = (2,−3,2) and r₂₃ = (−3,2,2).
   - At each ray, every world crosses at one of the two faces meeting there.
   - Continuity gives Γ(r) = −Σ_j π_jκ̂_j r_j = 0 for all three rays.
   - The ray matrix has determinant −25 (CHECKED). So x := π⊙κ̂ = 0, hence π = 0. Contradiction. ∎

This is the brief's computation. Its intermediate relations x₂ = x₃ = 2x₁ and x₁ = x₃ = 2x₂ are CHECKED.

**General form (PROVED).** With convex error levels, *at most one* non-visible vertex can have every
world crossing.
- At such a vertex, step 5 gives Γ = −x·h on F_v, so x ∝ v.
- x ≠ 0, because every κ̂_j > 0 there.

For mixed anti-visible/crossing vertices the condition is the linear system of steps 4–6. I have not
solved it in general (CONJECTURE: equivalent to Theorem A's condition for polytopes in relint Δ₃).

---

## 6. S2 and S4: verdicts

- **S2.** CHECKED in its own setting: convex, homogeneous vetoes that vanish on the target, and a Brier
  error level. Theorem A supersedes it.
  - Every hypothesis S2 adds is unnecessary: convexity, homogeneity, and "vetoes vanish on the target",
    which is forced by Lemma 2.
  - The conclusion is stronger: two non-visible vertices already suffice.
- **S4.** Not established as stated. What is true and needed is the following.
  - Lemma 3: for j ≠ k the slab piece Z_k ∩ {h_j > 0} must be coherent.
  - More generally, ⋂_{k∈W} Z_k ∩ {β·h > 0} must be coherent for β ≥ 0 supported on W. The proof is the
    same as Lemma 3: it is the unique minimiser of Σβ_k b_k inside ⋂_W Z_k.
  - A concrete failure, NUMERICS (`lpcheck.py` E): put Z_i = D_K ∪ {h_i ≥ 0} for i = 1, 2 and
    β = (1,1,0). The resulting undominated model is not convex: 37 of 20 000 sampled midpoints fall
    outside it.
  - Whether Z_k itself must be convex is open, and it is not needed: Lemma 4 runs on the slab pieces.

---

## 7. What an escape must do (the full class 𝒢)

Every 𝒢-ranking is lexicographic in integrable levels, and its first level is weakly sign-correct (§2).
At each world call the leading block of non-negative levels the vetoes, and the first level that is not
≥ 0 the error level. Theorems A and B then show that a cover of a polytope with two or more non-visible
vertices must use at least one of the following:

- **R1. A strict error level that is neither Brier-type nor convex.** The proof of Theorem A shows what
  is then required.
  - There must be π with Σπ_jℓ_j changing sign exactly across ∂D_K on the forced neighbourhoods of
    every non-visible face.
  - Every lexicographic-Bayes set N(W₀) ∩ {Σα_kφ_k + Σ_{W₀}β_kℓ_k < 0} must also be coherent.
  - Writing ℓ_j = −ω_j(h)h_j, this is a *local prior* q(h) ∝ π⊙ω(h) whose mixtures stay coherent near
    ∂D_K. That is the CPM realisation problem, localised to a neighbourhood of ∂D_K, with tangency
    allowed away from the target.
  - Piecewise-constant local priors fail here. The mixtures' boundary planes rotate under diagonal
    rescaling (the fan of ν(β⊙K) is diag(β)⁻¹·fan(K)), producing non-convex kinks at the rays inside
    the forced region (CHECKED by hand).
  - This route is excluded by the brief's instruction to avoid CPM-equivalent designs.
- **R2. A non-strict error level, so that later signed levels decide on its zero set.**
  - A signed level with a non-null zero set splices independent Bayes problems on complementary regions.
    At level 1 the weights are α, at the next level β, and they are chosen independently.
  - Such splices are generically incoherent. CONJECTURE: R2 reduces to R1 or fails.
- **R3. K touching ∂Δ** (Lemma 2 fails). Irrelevant for the reversed triangle.
- **R4. Leaving the class:**
  - non-homogeneous (pathological) statistic orders (§2(b));
  - incomplete world orders (E61's route);
  - two-sided domains (F61's route).

**Reduction (PROVED).** Single-level 𝒢-rankings ∫_X f_k with measurable sign-correct f_k cover D_K iff:
- (i) every Bayes minimiser (including the non-unique ones) is coherent, for every π ∈ Δ; and
- (ii) D_K is Bayes for some π.

The proof: Lyapunov plus separation, and the converse that unique minimisers are undominated. These are
CPM conditions (1)–(2) without non-tangency (5). So "visibility is necessary in 𝒢" would imply that no
measurable CPM with relaxed tangency realises the reversed triangle. **Status: OPEN.** I do not think
the round can settle it.

---

## 8. Positive side: the exemption, and nearby results

**Theorem C (exemption; PROVED).** Keep the auditor's hypotheses: K′ ⊆ relint K compact convex, and
compact A_i ⊆ conv(K′ ∪ {e_i}). Let π\* ∈ K be arbitrary, and suppose
K = conv(K′ ∪ A₁ ∪ … ∪ Aₙ ∪ {π\*}). Then the auditor's ranking (veto φ_i from A_i, then Brier) covers
D_K on U = D_{K′}.

*Proof.*
- The auditor's steps for (G), (IB), compactness, coherence of undominated models, (C) and (LF) never
  use the target.
- The veto-free region is N = D_{K_N} a.e., with K_N := conv(K′ ∪ ⋃A_i). So D_K = N ∩ {π\*·h > 0} a.e.
- This is the a.e.-unique minimiser of Σπ\*_i b_i over models inside N, so it is undominated. The
  converse lemma (VB note, referee's addition) gives this. ∎

Theorem A shows that one point is the most a Brier error level can exempt.

**Polytopes in relint Δ (PROVED, from Theorems A and C).** In 𝒱_B:
- all vertices but at most one strictly visible ⇒ covered;
- two vertices not even weakly visible ⇒ not covered;
- the gap is tangential vertices (Cor. A(d)).

Strictly visible vertices go in A_i, the points v + t(v − e_i) go in K′, and the exempt vertex is π\*.

NUMERICS (`search.py`, Dirichlet(4) triangles with all coordinates ≥ .05; 19 683 accepted):

| Non-visible vertices | Share of triangles | Covered? |
|---|---|---|
| 0 | 9.6% (1899) | auditor |
| 1 | 27.4% (5394) | new, by Theorem C |
| 2 | 50.3% (9906) | excluded by Theorem A |
| 3 | 12.6% (2490) | excluded by Theorem A |

So the exemption roughly quadruples the covered class.

Worked example (`lpcheck.py` D):
- The triangle has vertices (.335,.431,.234), visible from world 2; (.572,.209,.219), visible from
  world 1; and (.147,.335,.518), which every world crosses.
- 0 guidance violations, N ∩ {π\*·h > 0} = D_K exactly, Brier slack of veto-free rivals 8·10⁻¹⁰, and
  0 convexity failures over 200 random lexicographic-Bayes minimisers.

**The reversed triangle is a limit of covered polytopes (CHECKED exactly, plus NUMERICS).**
- Cut corner v₁ by the chord from v₁ + s(v₃ − v₁) to v₁ + s(v₂ − v₁).
- The new vertex on [v₁, v₃] is strictly visible from world 2. This is exact:
  v₁ − e₂ = (v₃ − v₁) + 3(v₂ − v₃), with both coefficients positive, and moving along the edge only adds
  a positive multiple of v₃ − v₁.
- Hence, for every s ∈ (0, 1):
  - **the chamfered hexagon is in the auditor's class** (`cuts.py`, `hexcheck.py`: 0 guidance
    violations, veto-free region = D_K exactly, s = .1, .02);
  - **the pentagon with one sharp corner is covered by Theorem C.**
- As s → 0 these converge to K in the Hausdorff metric. Rounded corners are also covered (n = 3 smooth
  points are visible, Cor. A(c)), subject to P61's uniformity check.
- So the reversed triangle is not covered by 𝒱_B or 𝒱_conv rankings, but it is a Hausdorff limit of
  covered targets.
  - The nearby result: every chamfer, or rounding, of the corners, however small, is covered.
  - The exact target needs R1 or R2, or a route outside the class.

---

## 9. Status table

| Item | Status |
|---|---|
| S6 (Hausner–Wendel) with positive homogeneity | PROVED (standard) |
| S6: rational homogeneity forced by Lyapunov; real homogeneity not forced by (G),(IB), completeness, transitivity | PROVED (Hamel-basis example) |
| (IB) for finite statistics ⇒ translation invariance on differences | taken as definition; general derivation CONJECTURE |
| (G) ⇒ pointwise lex sign-correctness; leading level weakly sign-correct; 𝒢 ⊋ 𝒱 | PROVED |
| Rem 1.1: one-sided (LF) domains force full-dimensional K (no precise models) | PROVED |
| Lemma 1 (vetoes vanish on correct advice) | PROVED |
| Lemma 2 = S3 (target pays no veto; any strict error level; no "all-zero model" hypothesis) | PROVED |
| Lemma 3 (slab pieces Z_k∩{h_j>0} undominated, hence coherent) | PROVED |
| Lemma 4 (collar forcing for measurable vetoes; overlap-graph connectivity) | PROVED |
| **Theorem A (Brier-type error: all non-visible extreme points share one exposing π; polytopes ≤ 1 non-visible vertex)** | **PROVED** |
| **Reversed triangle not covered by any 𝒱_B-ranking, on any one-sided (LF) domain** | **PROVED** |
| S2 (as stated) | CHECKED; superseded by Thm A |
| Cor A(c): n=3 smooth extreme points are strictly visible | PROVED |
| Cor A(d): tangential-from-one-world corners count as non-visible | PROVED (sketch only, not refereed) |
| Tangential from two worlds | CONJECTURE (non-visible) |
| **Theorem B = S5 (convex error levels: reversed triangle not covered; ≤ 1 all-crossing vertex)** | **PROVED** |
| Convex-error system for mixed vertices ≡ Thm A condition | CONJECTURE |
| S4 as stated | not established; replaced by Lemma 3; NUMERICS for an incoherent example |
| **Theorem C (one exempt point: conv(K′∪⋃A_i∪{π\*}) covered)** | **PROVED** |
| Polytope characterisation in 𝒱_B (all but one strictly visible ⇒ covered; two non-weakly-visible ⇒ not) | PROVED (gap: tangential) |
| Chamfered reversed triangles (all s ∈ (0,1)) in auditor's class; one-sharp-corner pentagons by Thm C | CHECKED (exact) + NUMERICS |
| Random-triangle census (0/1/2/3 non-visible: 9.6/27.4/50.3/12.6%) | NUMERICS |
| "Every extreme point visible" necessary for VB-type rankings | REFUTED (Thm C) |
| Visibility (all but one) necessary in full class 𝒢 | OPEN: equivalent difficulty to tangency-relaxed CPM realisation (Reduction §7) |
| R2 (stacked signed levels) reduces to R1 or fails | CONJECTURE |
