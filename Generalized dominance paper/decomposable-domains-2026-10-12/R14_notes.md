# R14. Referee of CCIBU.tex, and the extension to n ≥ 4 worlds

13 October 2026. Labels: **PROVED** (full proof written here), **CHECKED** (verified, proof
sketched), **CONJECTURE**. Setting: BRIEF.md, BRIEF2.md (incl. the 13 Oct update), CCIBU.tex.
Standing notation: M a decomposable domain (advice ranges A(g)), ℓ(g,a) ∈ ℝⁿ local penalties with integrable envelope,
L(X) = ∫ ℓ(g,a_X(g)) dμ, R = {L(X) : X ∈ M} (compact convex, Aumann/Lyapunov),
a ∈ ℝⁿ with a_i < min_R y_i. Hypothesis (IBU): for every w ∈ int Δ the minimiser of w·L on M
is a.e. unique and coherent. "Efficient" = Pareto-undominated in R. "S-competitive"
(S ⊆ Ω) = no z ∈ R with z_i < y_i for all i ∈ S. For an additive ranking, (S) for a selection
p ↦ C_p with profile x(p) = L(C_p) is exactly: each x(p) efficient with a coherent unique
realisation, x(p) supp(p)-competitive, and every coordinate p ↦ x_i(p) lower semicontinuous.

## 0. Summary

**Part 1 (referee).** CCIBU is correct. Every item checks. There are no gaps, only five
presentational points (§1). One observation sharpens it: strict guidance is used *only* at
vertex indices. Theorem A below removes it from the uniqueness half.

**Part 2 (n ≥ 4).**
* (a) **Efficient-profile uniqueness holds in every dimension (Theorem A, PROVED).** Every
  efficient profile is the lexicographic optimum of an *admissible* sequence (first nonzero
  entry of every column positive). Proper separation from the cone {d_Z = 0, d_{Z^c} ≤ 0}
  supplies the sequence, so relative-boundary points and steps with zero weight on all new
  coordinates are handled. The interior perturbation then gives uniqueness and coherence.
  Strict guidance is **not** needed. Consequently (C) holds and C_L = {realisations of
  efficient profiles} for any n.
  The brief's form ("each later objective nonzero on some new coordinate") is too strong. Steps
  that put zero weight on every new coordinate but cut the face are sometimes necessary. CCIBU's
  endpoint case is an instance.
* (b) **Closed selection.**
  - The quadratic selection does not extend (Prop B1, PROVED). The interior Q-map extends to an
    (S)-selection iff every boundary fibre has a coordinatewise-least point in the omitted
    coordinates. For n = 3 this is automatic. For n ≥ 4 it fails for zonotope-type faces that
    are compatible with strict guidance (Ex. B1′, CHECKED at the level of R).
  - **Chebyshev localisation (Lemma B2, PROVED).** For f_q(y) = max_i q_i(y_i − a_i), the
    argmin set B(q) on R is locally constant in the omitted weights near every boundary index.
    It equals the argmin for the face weights q_S. So lower semicontinuity of any
    Chebyshev-based selection reduces to its behaviour *inside* each open face.
  - **Theorem C (PROVED, any n).** Assume (IBU). Suppose the correspondence q ↦ B(q) is lower
    hemicontinuous on the relative interior of each face of Δ (condition (L)). Then the
    least-norm selection σ(B(q)) is continuous on all of Δ, and (LA), (S), (C) hold.
  - Under strict guidance:
    · every face of R with a constant coordinate is a singleton (Lemma B3);
    · B(q) is a singleton whenever its active set is a singleton (Lemma B4);
    · fibres over 2-coordinate fronts vary continuously (Lemma B6).
    Hence (L) holds at all vertices and on all edges of Δ in every n (Prop B7). In particular
    (S) holds on a neighbourhood of the 1-skeleton of Δ.
  - **Strict guidance is essential (Prop B5, PROVED).** There is a compact convex R ⊂ ℝ⁴ with
    oscillating fibres for which *no* selection whatsoever satisfies (S). It violates Lemma B3,
    so it is not the attainable set of any strictly guiding system. It is a candidate
    obstruction for the weakened (Σ_T) guidance orders (realisability unverified).
  - **Residual (n ≥ 4).** Condition (L) at indices in open faces of dimension ≥ 2. There the
    Chebyshev touching set is a non-singleton fibre-type set (active set of size ≥ 2). No
    counterexample is known. CONJECTURE: (L) holds under strict guidance + (IBU), which would
    give the full n-world theorem. §2.5 states exactly what a counterexample needs.

---

## 1. Part 1: referee of CCIBU.tex

| Item | Verdict | Note |
|---|---|---|
| Standing facts (l.58–69) | CORRECT | R compact convex (Aumann integral of a finite-valued, integrably bounded correspondence over an atomless measure). Coherent class closed in measure. L continuous in measure by dominated convergence |
| Lemma direction | CORRECT | See (i) |
| Lemma efficient, interior / vertex w | CORRECT | Vertex case uses strict guidance (unique pointwise ℓ_i-minimiser) |
| Lemma efficient, edge w, a < x₁ < b | CORRECT | See (ii) |
| Lemma efficient, endpoints x₁ = a or b | CORRECT | See (iii) |
| Lemma efficient, a = b | CORRECT, terse | See (iii) |
| Selection x(p) | CORRECT | See (iv) |
| Lemma lsc | CORRECT | Uses joint continuity of (p,x) ↦ Q_p(x) and closedness of argmin |
| Main theorem (LA), (S), (C) | CORRECT | See (v) |
| Reindexing remark | CORRECT | See (vi) |
| Corollary sandwich | CORRECT | Inputs: R11 Thm W(a),(d) as refereed in R13, plus R13 Prop S |

**(i) Lemma direction.**
- w + sv has all coordinates positive for 0 < s < min_{i: v_i<0} w_i/|v_i|. This needs only
  v₃ > 0. The signs of v₁, v₂ are free, as the proof uses with v = (−λ,0,1).
- Fix g with a non-null tie between a ≠ b. The (w+sv)-minimisers on A(g) equal the
  v-minimisers on A_w(g) for s < s₀(g) (finitely many kinds of advice, positive w-gap).
- Countable union: N = ⋃_M ⋂_{m≥M} N_m, so some N_m is non-null. Two measurable models
  (giving the min-index / max-index advice among the tied kinds of advice) are two distinct (w+s_m v)-Bayes models.
- Convergence and coherence are as written.

**(ii) Interior subgradient case.**
- On F, y₂ = (c − w₁y₁)/w₂, so h is a finite convex function on [a,b].
- Undominatedness gives x₃ = h(x₁).
- A finite subgradient λ gives y₃ − λy₁ ≥ x₃ − λx₁ on F.
- Realisations of x are w-Bayes, hence models whose advice lies in A_w. Minimising v·L over such models
  (a decomposable domain) is pointwise, so every realisation is a pointwise v-minimiser on A_w.

**(iii) Endpoints and a = b.**
- x₁ = a means x minimises y₁ on F. Realisations are then pointwise ℓ₁-minimisers on A_w,
  unique by strict guidance at world 1. The maximiser case is the same.
- The s²u term is genuinely needed: w ± s e₁ has third coordinate 0.
- Interiority: w − s e₁ + s²u has first coordinate w₁ − s + s²/3 > 0 for small s.
- If a = b, strict guidance forces |A_w(g)| = 1 a.e. Otherwise the models with pointwise ℓ₁-min and ℓ₁-max
  advice would have different L₁. So the realisation is unique for a trivial reason. Suggest
  saying this explicitly.

**(iv) Selection.**
- Edge: two Q_p-minimisers with different (x₁,x₂) would give a strictly better midpoint
  (strict convexity in the supported coordinates). So the supported coordinates are fixed, and
  the secondary minimisation fixes x₃.
- Undominatedness: each summand (x_i − a_i)² is strictly increasing on R.
- Vertex: argmin Q_{e_i} = argmin_R y_i. Under strict guidance this is a single point, since
  every model attaining min y_i is the pointwise ℓ_i-minimiser. Suggest saying so: it is what
  makes "z = x(p)" in Lemma lsc immediate at vertices.

**(v) Main theorem.**
- (LA): C_p is coherent and undominated.
- Competitiveness: if L_i(X) < x_i(p) for every i ∈ supp p, then Q_p(L(X)) < Q_p(x(p)).
- (S): sections {p : x_i(p) ≤ c} are closed by lower semicontinuity. Only levels c in the range
  of L_i matter.
- (C): via Lemma efficient. The rankings are untouched.

**(vi) Reindexing remark.**
- Put p_i ∝ w_i/(x_i − a_i) > 0. Then ∇Q_p(x) ∝ w, and convexity gives Q_p(y) ≥ Q_p(x) on R.
- p is interior, so x is the unique Q_p-minimiser.
- X is the unique realisation of x, by (IBU) at w. So C_p = X.

**(vii) Corollary sandwich.**
- R11 Thm W(a) supplies exactly (IBU) for the aggregate ψ.
- ψ is strictly increasing a.e. with integrable envelope (R13 §2.1).
- W(d) gives D_K = B_{p_T} with p_T ∈ int Δ (this needs K ⊆ int Δ, as stated).
- The domain is unchanged, so (LF) is kept. Additive rankings give strict (G) and (IB).

**Presentational suggestions.**
1. In Lemma direction, state the range of s explicitly; v₁ and v₂ may be negative.
2. Add the one-line reason for a = b given in (iii).
3. State that argmin Q_{e_i} is a singleton under strict guidance.
4. In "Scope", note that strict guidance is used only at vertex supports and vertex indices.
   Theorem A below shows uniqueness of efficient realisations needs only (IBU). So for
   weakened guidance (Σ_T) the n = 3 proof breaks exactly at the selection at vertices
   e_i, i ∈ T. There argmin y_i can be a non-singleton face with two omitted coordinates:
   the same fibre problem as in n ≥ 4.
5. Lemma efficient can be replaced by Theorem A below. That is shorter, and it covers the
   subgradient and endpoint cases uniformly.

---

## 2. Part 2: n ≥ 4

### 2.1 (a) Efficient-profile uniqueness in every dimension

**Definition.** A finite sequence W = (w¹,…,w^k) in ℝⁿ is *admissible* if for every
coordinate j the first nonzero entry among w¹_j,…,w^k_j exists and is positive. Then
W(s) := Σ_r s^{r−1} w^r has all coordinates positive for small s > 0. Let A^W(g) be the
pointwise lexicographic argmin of (w¹·ℓ(g,a), …, w^k·ℓ(g,a)) over A(g), and F_W the lexicographic
argmin face of R.

**Lemma A0 (successive minimisation; PROVED).** For any sequence V (signs arbitrary), the
models X ∈ M with L(X) ∈ F_V are exactly (a.e.) the measurable models whose advice lies in A^V.
*Proof.* ∫ v¹·ℓ(g,a_X(g)) ≥ ∫ min_{A(g)} v¹·ℓ(g,·). The right side is attained by a measurable
model, and equality holds iff its advice is pointwise minimal a.e. The models whose advice lies in A^{v¹}
form a decomposable domain. Induct. ∎

**Lemma A1 (admissible lex sequences give unique coherent models; PROVED).** Assume (IBU) and
let W be admissible. Then |A^W(g)| = 1 a.e. The unique model B^W with advice in A^W is coherent, and it is the
limit in measure of the W(s)-Bayes models as s ↓ 0.
*Proof.*
- For a, b ∈ A(g), W(s)·(ℓ(g,a) − ℓ(g,b)) is a polynomial in s. For small s its sign is that
  of its first nonzero coefficient.
- Hence there is s₀(g) > 0 with argmin_{A(g)} W(s)·ℓ(g,·) = A^W(g) for all 0 < s < s₀(g).
- Let N = {g : |A^W(g)| ≥ 2} and s_m ↓ 0. Then N = ⋃_M ⋂_{m≥M} N_m, where
  N_m = {g ∈ N : argmin W(s_m)·ℓ = A^W(g)}. If N is non-null, some N_m is non-null.
- The models giving the min-index and the max-index advice in A^W then differ on N_m. Both are pointwise
  W(s_m)-minimisers, i.e. two W(s_m)/|W(s_m)|-Bayes models. This contradicts (IBU).
- The unique W(s_m)-Bayes model equals B^W at g for all m ≥ M(g). So it converges a.e., hence
  in measure, and the limit is coherent because the coherent class is closed. ∎

**Lemma A2 (lexicographic support of efficient points; PROVED, any compact convex R).** Let
x ∈ R be efficient. There is an admissible W with F_W = {x}, built in at most 2n steps.
*Construction.* Start with F⁰ = R and Z₀ = ∅ (activated coordinates). At step k we have
x ∈ F^{k−1} and an admissible prefix. Stop if F^{k−1} = {x} (append u = (1,…,1); then
F = {x} still) or if Z_{k−1} = Ω. Otherwise let
 C₁ = F^{k−1} − x (convex, ∋ 0),  C₂ = {d : d_Z = 0, d_{Z^c} ≤ 0} (Z = Z_{k−1} ≠ Ω).

**Separation step.**
- ri C₂ = {d_Z = 0, d_{Z^c} < 0}. A point of C₁ ∩ ri C₂ would give y ∈ F^{k−1} ⊆ R with y_Z = x_Z
  and y_{Z^c} < x_{Z^c}, i.e. a dominator of x. So ri C₁ ∩ ri C₂ = ∅.
- By Rockafellar Thm 11.3 there is ν with inf_{C₁} ν ≥ sup_{C₂} ν, not both sets inside one
  level set.
- Since 0 ∈ C₁ ∩ C₂, both bounds are 0. Then sup_{C₂} ν = 0 gives ν_{Z^c} ≥ 0, and
  inf_{C₁} ν = 0 gives x ∈ argmin_{F^{k−1}} ν.
- Properness: either ν is non-constant on F^{k−1}, so F^k := argmin_{F^{k−1}} ν is a proper face
  of strictly smaller dimension; or ν_{Z^c} ≠ 0, so some new coordinate j has ν_j > 0 and Z grows.
- Put w^k := ν. Admissibility is kept, because ν ≥ 0 off Z.

**Termination.** Dimension drops at most n times and Z grows at most n times.
- If we stop with Z = Ω, W is admissible with every column activated. Lemma A1 gives
  |A^W| = 1 a.e., and Lemma A0 then makes F_W a single point. That point is x, because
  x ∈ F_W at every step.
- If we stop with F = {x}, append u. ∎

**Theorem A (PROVED; any n; strict guidance not needed).** Under (IBU), every efficient
x ∈ R has exactly one realisation in M modulo null sets, namely B^W for the W of Lemma A2,
and that realisation is coherent.
*Proof.* A realisation X of x has L(X) ∈ F_W. By Lemma A0 its advice lies in A^W, which is
a.e. a singleton, so X = B^W a.e. (Lemma A1). ∎

**Consequences (PROVED).**
1. (C) holds for the additive rankings.
2. C_L is exactly the set of realisations of efficient profiles, and each is coherent.
3. Vertex supports need no strict guidance either: W = (e_i, u).

**Answer to the brief's question (a).** The scheme "w¹ ≥ 0, then objectives that may be
negative on supported coordinates but ≥ 0 and nonzero on some new coordinate" is too
restrictive. Some steps must have zero weight on all new coordinates while cutting the face.
Example (n = 3, already in CCIBU's endpoint case):
- Let w¹ = (w₁,w₂,0), with face F parametrised by y₁ ∈ [a,b] and lower boundary
  h(t) = −√(t − a).
- At x = (a, ·, h(a)) no v with v₃ > 0 supports x on F, because the subgradient is −∞.
- The admissible sequence is (w¹, e₁, u). Its middle step has v₃ = 0.

What *is* true is the dichotomy in the separation step: every step either lowers the face
dimension or activates a new coordinate with a positive weight. Both relative-boundary
points and "zero weight on all omitted coordinates" are covered by proper separation. The
only failure mode would be a dominator of x, which efficiency excludes.

### 2.2 (b) Why the quadratic selection does not extend

For boundary p with S = supp p, write Φ_p = argmin_R Q_p = {y ∈ R : y_S = x*_S(p)}.
Here x*_S(p) is the unique Q_p-minimiser on the projection R_S. Let Φ′_p ⊆ ℝ^{S^c} be its
projection to the omitted coordinates.

**Prop B1 (PROVED).** Let x be any selection with x(q) = argmin_R Q_q for q ∈ int Δ. If x
satisfies (S), then for every boundary p, Φ′_p has a coordinatewise-least element ℓ_p and
x(p) = (x*_S(p), ℓ_p). Conversely, if every Φ′_p has a least element, this rule satisfies
(S): CCIBU's Lemma lsc applies verbatim, with "minimise the omitted coordinate" replaced by
"take the least element".

*Proof.*
1. Fix r ∈ int Δ. Let y_s := argmin Q_{(1−s)p+sr}.
   - For z ∈ Φ_p: Q_p(y_s) + (s/(1−s))Q_r(y_s) ≤ Q_p(z) + (s/(1−s))Q_r(z), and
     Q_p(y_s) ≥ Q_p(z). So Q_r(y_s) ≤ Q_r(z).
   - By upper hemicontinuity of the argmin, every cluster point lies in Φ_p, and it minimises
     Q_r there.
   - So y_s → λ_r(p) := argmin_{Φ_p} Σ_{j∉S} r_j(y_j − a_j)², a single point because the
     objective is strictly convex in y_{S^c} and y_S is fixed.
2. Lower semicontinuity forces x(p) ≤ λ_r(p) for all r.
   - In S-coordinates both sides equal x*_S(p). So x(p) ∈ Φ_p.
   - Take r = (1−η)e_j + ηu with j ∉ S and η ↓ 0. Then λ_{r,j}(p) → min_{Φ′_p} y_j.
   - So x(p)_{S^c} is at most the ideal point of Φ′_p, and lies in Φ′_p: a least element.
3. Converse: as in CCIBU Lemma lsc. Every cluster point lies in Φ_p, and so is ≥ ℓ_p
   coordinatewise. The least element is efficient: a dominator would lie in Φ_p (S-coordinates
   ≤ means equal for Q_p-minimisers) and be below ℓ_p. ∎

For n = 3, every Φ′_p is a compact interval or a point, so it has a least element. This
recovers CCIBU. For n ≥ 4 it can fail.

**Ex. B1′ (CHECKED at the level of R).** Take n = 4 and
 δ¹ = (1,−1,1,−2), δ² = (1,−1,−2,1),
and let ζ_1,…,ζ_m be further generators with all coordinates nonzero and (1,1,0,0)·ζ_k ≠ 0.
Let R = [0,δ¹] + [0,δ²] + Σ_k [0,ζ_k], a zonotope all of whose generators have all
coordinates nonzero. Then:
- F_w for w = (1,1,0,0) is the parallelogram [0,δ¹] + [0,δ²] + (vertex of the ζ-part).
- The fibre over each point of the relative interior of its S-projection is a segment in
  direction δ¹ − δ² = (0,0,3,−3). Its endpoints are incomparable, so there is no least element.
- For an open arc of edge indices p ∈ (e₁,e₂), x*_S(p) lies in that relative interior, so the
  Q-selection fails (S) there.
- Each generator has a mixed-sign pattern, which is the shape ℓ(+) − ℓ(0) takes on mixed
  problems under strict guidance. So this R is compatible with Lemma B3 below.
- Realising it by a field with (IBU) has **not** been checked.

The point is only that CCIBU's device does not extend. Ex. B1′ itself admits a closed
selection by Prop B7 below.

### 2.3 Chebyshev localisation and a sufficient condition

Let f_q(y) = max_i q_i(y_i − a_i) for q ∈ Δ, let t*(q) = min_R f_q > 0, and let
B(q) = argmin_R f_q. Let σ(B) = argmin_{y∈B} Σ_i (y_i − a_i)², and put x(q) := σ(B(q)).

**Lemma B2 (PROVED).**
(i) Every y ∈ B(q) is supp(q)-competitive. Moreover σ(B(q)) is efficient in R, and unique.
(ii) (Localisation) Let b ∈ Δ with supp b = S. There is a neighbourhood U of b in Δ such
that, for all q ∈ U, B(q) = B(π(q)) with π(q) := q_S/|q_S| ∈ relint Δ_S. Hence
x(q) = x(π(q)) on U.
(iii) q ↦ B(q) is upper hemicontinuous on Δ, with nonempty compact convex values.

*Proof.*
(i) Competitiveness:
- Off S the terms q_i(y_i − a_i) are 0. On S they are positive.
- So z_S < y_S (strictly in every coordinate of S) gives f_q(z) < f_q(y).
Efficiency:
- If y′ ∈ R and y′ ≤ σ := σ(B(q)), then f_q(y′) ≤ f_q(σ) = t*, so y′ ∈ B(q).
- Its norm is ≤, with equality only if y′ = σ.
- σ is unique by strict convexity.

(ii) Choose U so that q_i ≥ b_i/2 for i ∈ S and q_j(M_j − a_j) < τ for j ∉ S, where
M_j = max_R y_j and τ := ½ min_{i∈S} (b_i/2)(min_R y_i − a_i) > 0. Then:
- For every y ∈ R, max_{i∈S} q_i(y_i − a_i) ≥ 2τ > max_{j∉S} q_j(y_j − a_j).
- So f_q = max_{i∈S} q_i(y_i − a_i) on R, which is |q_S|·f_{π(q)}.
- Argmin sets are invariant under positive scaling.

(iii) Berge's maximum theorem: f is jointly continuous and R is fixed and compact. ∎

**Theorem C (PROVED, any n).** Assume (IBU). Assume also

 (L) for every nonempty S ⊆ Ω, the restriction of q ↦ B(q) to relint Δ_S is lower
   hemicontinuous.

Then x(q) = σ(B(q)) is continuous on Δ. With C_q := the unique realisation of x(q)
(Theorem A), the additive rankings satisfy (LA), (S) and (C).

*Proof.*
1. On relint Δ_S, B is continuous (upper hemicontinuity from B2(iii), lower from (L)) with
   compact convex values. Berge with the strictly convex objective makes σ∘B continuous there.
2. At any b ∈ Δ, Lemma B2(ii) gives x = x∘π on U. The map π is continuous into relint Δ_S
   with π(b) = b. So x is continuous at b.
3. x(q) is efficient and supp(q)-competitive (B2(i)). Its realisation is unique and coherent
   (Theorem A).
4. Continuous coordinates give closed sections, so (S) holds. (LA) follows, and (C) is
   Theorem A. ∎

*Remark.* Lemma B2(ii) is the device that replaces CCIBU's secondary minimisation. Near a
face, the Chebyshev objective ignores the omitted weights *exactly*, not just to first order.
So interior indices near b cannot approach b from different directions in the omitted
coordinates. That direction-dependence is exactly what defeats Q (Prop B1).

### 2.4 What strict guidance gives: (L) on the 1-skeleton

**Lemma B3 (face lemma; PROVED).** Suppose the penalties are strictly guiding at world j.
Then every face of R on which y_j is constant is a single point. The same holds for every
projection R_S with j ∈ S.

*Proof.*
1. Every face F of a compact convex set is an iterated exposed face: F is a face of a proper
   exposed face, then induct on dimension. So F = F_V for some finite sequence V (signs
   arbitrary).
2. By Lemma A0, the profiles in F are the integrals of models whose advice lies in A^V.
3. Suppose |A^V(g)| ≥ 2 on a non-null G. The models with pointwise ℓ_j-min and ℓ_j-max advice in A^V
   (equal off G) differ strictly in ℓ_j on G, by strict guidance. Their profiles are both in F
   and differ in y_j. Contradiction.
4. So A^V is a.e. a singleton, and F is a point.
5. For R_S: a face G of R_S with constant y_j pulls back to the face R ∩ π_S^{-1}(G) of R.
   That face has constant y_j, so it is a point, and so is G. ∎

(This is the n-world form of the fact CCIBU uses at vertices. It also explains why Ex. B1′
uses only all-nonzero generators.)

**Lemma B4 (PROVED).** Assume strict guidance. Let q ∈ relint Δ_S, c_i := a_i + t*(q)/q_i
(i ∈ S), m ∈ ri B(q), and I := {i ∈ S : m_i = c_i} ≠ ∅. Then:
(i) y_I = c_I for every y ∈ B(q);
(ii) if |I| = 1, B(q) = {m}.

*Proof.*
(i) y_i ≤ c_i on the convex set B(q), with equality at a relative-interior point. So y_i is
constant on B(q).
(ii) Let I = {i}.
- The terms for S ∖ {i} are < t* at m. For z ∈ R with z_i < m_i, small steps from m toward z
  lower f_q. That contradicts minimality.
- So m_i = min_R y_i, and by (i) B(q) ⊆ argmin_R y_i.
- argmin_R y_i is a face with constant y_i, hence a point (B3). ∎

**Lemma B6 (PROVED).** Assume strict guidance at the worlds of S, with |S| = 2. Then the
fibre map Φ(c) := R ∩ π_S^{-1}(c) is Hausdorff-continuous on Eff(R_S).

*Proof.*
1. If c is an extreme point of R_S, Φ(c) is a face of R with y_S constant, hence a point (B3).
   Φ has closed graph, so it is continuous at c.
2. Otherwise c lies in the relative interior of a segment face G of the planar set R_S, and
   nearby points of Eff(R_S) lie in G.
3. On G, F_G := R ∩ π_S^{-1}(G) is compact convex. Write c′ = (1−t)c + te, with e an endpoint
   of G beyond c′. Then y′ = (1−t)y + t y_e ∈ Φ(c′) → y. This gives lower hemicontinuity;
   upper hemicontinuity holds by closed graph. ∎

**Prop B7 (PROVED; any n).** Under strict guidance, (L) holds on every vertex and on the
relative interior of every edge of Δ. More generally it holds at every q at which B(q) is a
single point.

*Proof.*
1. A single-valued, upper hemicontinuous correspondence is continuous at that point. Vertices
   are trivial.
2. Edge S = {i,j}: the touching set T = π_S(B(q)) = R_S ∩ (c_S − ℝ²₊) is a single point.
   - Apply the argument of B4 to R_S (B3 applies to R_S).
   - If the relative-interior active set is one coordinate, T is a point.
   - If it is both coordinates, T ⊆ {c_S}.
3. Hence c_S(q) ∈ Eff(R_S), it depends continuously on q, and B(q) = Φ(c_S(q)).
4. This is continuous by B6. ∎

**Consequence (PROVED).** By Lemma B2(ii) and Prop B7, the Chebyshev least-norm selection is
continuous at every index whose support has at most 2 worlds. It is also continuous on a
neighbourhood in Δ of each such index. So under (IBU) + strict guidance, the closed-selection
problem in any n is solved near the 1-skeleton.

### 2.5 Strict guidance is essential; what a counterexample would need

**Prop B5 (PROVED).** There is a compact convex R ⊂ ℝ⁴ for which no map x : Δ → R
satisfies both of the following:
- x(p) is supp(p)-competitive for every p;
- every coordinate of x is lower semicontinuous.
So no additive ranking with attainable set R admits an (S)-selection, whatever the
uniqueness properties.

*Construction.*
1. Front.
   - Let φ(θ) = 1 − √(1 − (1−θ)²) on [0,1], the circle of radius 1 about (1,1), and
     γ(θ) = (θ, φ(θ)).
   - φ is strictly convex and strictly decreasing, with γ(0) = (0,1) and γ(1) = (1,0).
   - Fix θ₀ ∈ (0,1). Let σ(θ) = ½(1 + sin(1/(θ₀ − θ))) for θ < θ₀ and σ(θ) = ½ for θ ≥ θ₀.
   - Let K = {(γ(θ), σ(θ), 1 − σ(θ)) : θ ∈ [0,1]} and R := conv(cl K).
2. Then R_S = conv γ([0,1]) for S = {1,2}.
   - Its weakly efficient set is exactly the arc Γ = γ([0,1]). A chord point (ε,1−ε) is
     strictly dominated by γ(ε′) for ε′ ∈ (ε²/2, ε), and there are no axis-parallel pieces.
   - Each γ(θ) is an exposed point of R_S. So the fibre over γ(θ) is a face of R:
     · a point (σ(θ),1−σ(θ)) for θ ≠ θ₀;
     · at θ₀, the segment [A,B] with A = (0,1) and B = (1,0) in (y₃,y₄), since cl K adds all
       cluster values of σ.

*Proof of the obstruction.*
1. Let E = [e₁,e₂] be the edge, parametrised by [0,1]. Competitiveness on {1,2} puts x_S(p) on
   Γ for p in the relative interior of E. Competitiveness at e₁ and e₂ gives x_S(e₁) = (0,1)
   and x_S(e₂) = (1,0).
2. On Γ, x₂ = φ(x₁). Lower semicontinuity of x₂, with φ⁻¹ continuous and decreasing, makes x₁
   upper semicontinuous. With lower semicontinuity of x₁, x₁ is continuous on E.
3. Let p* = min{p : x₁(p) = θ₀}. On [0,p*), x₁ < θ₀, and x₁ is continuous.
   - By the intermediate value theorem every θ ∈ (x₁(0), θ₀) is attained there.
   - By compactness, the attaining indices tend to p* as θ ↑ θ₀.
4. Choose θ_k ↑ θ₀ with σ(θ_k) → 0 and θ′_k ↑ θ₀ with σ(θ′_k) → 1, attained at p_k → p* and
   p′_k → p*. The fibres there are single points, so x(p_k) → (γ(θ₀), A) and
   x(p′_k) → (γ(θ₀), B).
5. Lower semicontinuity at p* requires x₃(p*) ≤ 0 and x₄(p*) ≤ 0. But x(p*) lies in the fibre
   over γ(θ₀), where y₃ + y₄ = 1. Contradiction. ∎

**Why this is not a counterexample to the theorem.** The fibre over γ(θ₀) is a face of R
with y₁ constant and is not a point. Lemma B3 forbids this under strict guidance at world 1.
So Prop B5 shows the n ≥ 4 theorem *cannot* be proved from (IBU) and geometry alone: some
input like strict guidance is necessary. It also flags the weakened orders (Σ_T, ties
between good and silence). There, faces with constant coordinates are allowed, and an
oscillating-fibre field could block (S). CONJECTURE: such a field exists with (IBU). Not
attempted here.

**The residual (precise).** Under (IBU) + strict guidance, the n-world theorem follows from
Theorem C once (L) holds at indices q ∈ relint Δ_S with |S| ≥ 3. By Prop B7, failure needs a
point q with all of the following:
- B(q) is not a single point;
- the relative-interior active set I has |I| ≥ 2, so B(q) ⊆ {y_I = c_I} is a fibre-type set
  inside a face of R whose normal is supported in I;
- c_I lies in the relative interior of a positive-dimensional face of R_I that is not
  relatively open in the front of R_I (impossible when |I| = 2), or the active set jumps
  between q and nearby indices;
- the nearby touching sets B(q′) approach only part of B(q). An oscillation of the kind in
  Prop B5 would have to occur over a *non-extreme* front point, since B3 kills it over extreme
  points.

For n = 4 this concerns the four open 2-faces of Δ (|S| = 3) and int Δ. In the examples I
checked (zonotope faces like Ex. B1′; cuts of fibres by binding constraints y_J ≤ c_J), B
varies continuously. CONJECTURE: (L) holds under strict guidance and (IBU). That would give
(LA), (S), (C) in every n.

Note that (L) is sufficient, not necessary. Theorem C needs only lower semicontinuity of
σ∘B on each open face. And (S) may use other selections, including blow-up reindexings of
open faces of dimension ≥ 2, which have room that edges lack. So a genuine counterexample
must defeat all selections, not just the Chebyshev one. A 1-dimensional oscillation as in
B5 cannot do this under strict guidance (B6/B7). A 2-dimensional analogue over a 3-coordinate
front would also have to defeat blow-ups. I could not build one.

### 2.6 Status table

| Claim | Status |
|---|---|
| CCIBU (n = 3) | Correct; five presentational points (§1) |
| Unique coherent realisation of every efficient profile, any n, (IBU) only | PROVED (Thm A) |
| (C) for additive rankings under (IBU), any n | PROVED |
| Q-selection extends to n ≥ 4 iff every boundary fibre has a least element | PROVED (B1); fails for Ex. B1′-type faces (CHECKED for R) |
| Chebyshev localisation; (L) ⇒ (LA), (S), (C), any n | PROVED (B2, Thm C) |
| (L) at vertices and on edges under strict guidance, any n | PROVED (B7) |
| (L) on open faces of dimension ≥ 2, n ≥ 4 | CONJECTURE |
| Without strict guidance: R with no (S)-selection | PROVED for R (B5); realisability with (IBU) under Σ_T is a CONJECTURE |
| Sandwich corollary for n ≥ 4 | Follows from R11/R13 + Thm A + Thm C *whenever (L) holds*; open otherwise |
