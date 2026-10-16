# PropD: precise regions are constant or diagonal-projective (complete proof), global transport, and the empty-interior case

14 Oct 2026. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Script: `propd_py/checks.py` (output `checks.out`).
Notation as in the write-up (WU) §§2–5: Ω = int Δ, ν(x) = x/(𝟙·x), P(q,g) = min_{m∈K_q} m·g, ℓ_g = g^⊥ ∩ aff Δ (a line of
probabilities), d-line {q : d·q = 0} (a line of priors). For w ∈ (0,∞)³ put σ_w(q) := ν(w⊙q).

## 0. Outcome

1. **Prop D holds in full, with no injectivity hypothesis (Theorem D, PROVED).** Let O ⊆ Ω be open and connected with
   K_q = {σ(q)} on O. Assume the chart hypothesis (C) below. Then σ is constant on O, or σ = σ_w on O for some w > 0. In the
   second case σ is injective. R8's GAP (the step "non-constant ⇒ injective") is closed: partial plateaus, folds and
   one-dimensional images are all impossible.
   - **No external theorem is used.** In particular the local fundamental theorem of projective geometry is not used:
     the diagonal form is obtained directly from the vertex pencils and a Pexider equation.
   - **(C) is the only chart input.** It says that, for a.e. pair, the accept-g and accept-(−g) regions lie on opposite
     open sides of one line whose normal d has the strict sign pattern of g.
     - Half-plane charts, three-ray charts and {+,−} charts all satisfy it, adjacent or split, whether or not d-faces
       meet O.
     - It holds for every solution of CF(T), for every T. It also holds for every strictly guiding additive cover with
       integral penalties on every decomposable domain (Lemma 1.1).
   - **No regularity is used.** Nothing beyond continuity of σ on O, which Hausdorff continuity of K gives. No
     measurability of g ↦ d(g) is needed.
2. **Transport (Theorem T, PROVED).** If one open precise region O has σ = σ_w (non-constant), then for a.e. g whose line
   ℓ_g meets σ_w(O), d(g) ∝₊ w⊙g. Hence:
   - (a) R(±g) ⊆ {±σ_w(q)·g > 0} on all of Ω;
   - (b) **every precise prior q′ ∈ Ω** (in O or not, interior point or not) has K_{q′} = {σ_w(q′)};
   - (c) all non-constant open precise regions share one w, and no open wall (constant precise region) exists anywhere;
   - (d) a cone law for every non-precise K_{q′} (Cor T2).

   **So I2 step 4 (Prop 4(a)–(c)) is PROVED as stated, including "one w at all three vertices".** C2's Prop 5.2 is the
   same statement and is also PROVED.
3. **Consequences for the users.**
   - *I2 Prop 4.* Now rests only on Thm D and Prop vertexfree(i).
   - *C2.* The step "σ_b constant or ν(W_b·) on O_b" is PROVED. C2's Prop 4.3 (W_b depends on b) contradicts (c)
     immediately.
   - *C1.* Lemma 5.0 holds without injectivity, and **P_wild = ∅** (C1 Cor 5.4).
   - *Observation (status of the cited inputs, all unrefereed).* I2 Thm 3 / C2 Thm 4.1 (forced precise collar at each
     vertex) + vertexfree(i) + Thm D give an open, non-constant, diagonal-projective precise region in every cover of T1.
     C1 Thm A forbids that. So these three inputs already exclude every cover, without I2's transition algebra or C2's
     Bezout pinning (§6).
4. **Precise sets of positive area and empty interior (§7).** C1's (M1) is reduced but not settled.
   - PROVED: the segment law, collinearity on P, and the density-point d-line law hold on any precise set. If int P has
     a non-constant component, then all of P is σ_w.
   - CHECKED: a positive-measure precise set cannot mix two different w's, or a wall and a projective piece.
   - CONJECTURE: (M1) itself, i.e. that σ on a positive-area precise set with empty interior is a.e. locally constant or
     σ_w. The exact missing step is stated in §7.4.

## 1. Hypotheses

**Standing.** q ↦ K_q assigns a credal set (nonempty compact convex ⊆ Δ) to each q ∈ Ω. O ⊆ Ω is open and connected,
with K_q = {σ(q)} for q ∈ O, and σ is continuous on O.
- Continuity is automatic if K is Hausdorff-continuous on O, since |σ(q) − σ(q′)| = d_H(K_q, K_{q′}).
- Nothing about K off O is assumed in §§2–4.

**(C) on a set Q ⊆ Ω.** There is a null set N ⊆ ℝ³ such that every mixed g ∉ N satisfies at least one of:
- (C0) P(q,g) ≤ 0 for all q ∈ Q;
- (C0′) P(q,−g) ≤ 0 for all q ∈ Q;
- (C1) there is d = d(g) ∈ ℝ³ with sign d_i = sign g_i (i = 1,2,3) such that
  {q ∈ Q : P(q,g) > 0} ⊆ {d·q > 0} and {q ∈ Q : P(q,−g) > 0} ⊆ {d·q < 0}.

No choice of d is required to be measurable in g. Non-mixed g never enter.

**Lemma 1.1 (who satisfies (C) on Q = Ω). PROVED.**
- (a) *Every solution of CF(T), for any T.* Take d = c − c′; it has the strict sign of g. R(g) = {c·q > max(0, c′·q)} ⊆
  {d > 0}, and R(−g) ⊆ {d < 0}.
- (b) *Every strictly guiding additive ranking with integral penalties on a decomposable domain whose p-Bayes model is
  a.e. D_{K_p} at every p ∈ Ω.* This covers every cover, by WU Prop necessary(a). Let R_pen(h) be the set of p at which
  accepting h is the unique minimiser of p·ℓ(g,·) over A(g). It is an intersection of finitely many open half-planes,
  so it is open and convex, and R_pen(g) ∩ R_pen(−g) = ∅.
  - *Fubini.* The set {(p,g) : P(p,g) > 0, p ∉ R_pen(g)} is Borel, since P is jointly continuous and the penalties are
    measurable. Each of its p-sections is contained in D_{K_p} ∖ B_p, which is null. So for a.e. g, V := {P(·,g) > 0}
    satisfies λ(V ∖ R_pen(g)) = 0, and likewise for −g.
  - *From a.e. to exact.* V ∖ cl R_pen(g) is open and null, hence empty. So V ⊆ int cl R_pen(g) = R_pen(g) (if
    R_pen(g) = ∅, then V = ∅).
  - *The three cases.* If + ∉ A(g), then R_pen(g) = ∅ and (C0) holds. If − ∉ A(g), (C0′) holds. Otherwise put
    d := ℓ(g,−) − ℓ(g,+). Then R_pen(g) ⊆ {d > 0} and R_pen(−g) ⊆ {d < 0}, and by strict guidance
    ℓ_i(g,+) < ℓ_i(g,−) when g_i > 0 (and the reverse when g_i < 0). That is (C1).
  - (× in the advice range changes nothing; ties at a.e. g are excluded by uniqueness of the Bayes model.)
- (c) *Not checked here:* bounded-charge penalties. The pointwise chart R_pen(g) is not defined there. (C) holds as soon
  as such a system has a pointwise chart field reproducing its Bayes models a.e., which is the form in which I2/C2 use
  it.

So in all three users (I2, C2: covers; C1: CF(T1) solutions) (C) holds on Ω. Note that (C) contains no reference to c,
c′, silence cells, adjacency, half-plane versus three-ray form, or d-faces.

## 2. Two elementary lemmas

**Lemma SL (segment law). PROVED.** Assume (C) on a convex Q. Let q₁, q₂ ∈ Q with K_{q_i} = {m_i}, and q ∈ [q₁,q₂]. Then
K_q ∩ [m₁,m₂] ≠ ∅; in particular, if K_q = {m}, then m ∈ [m₁,m₂].

*Proof.*
1. Let C := {g : m₁·g > 0, m₂·g > 0}, an open nonempty cone. Take a mixed g ∈ C∖N.
   - (C0) fails, since P(q₁,g) = m₁·g > 0.
   - If (C0′) holds, then P(q,−g) ≤ 0.
   - If (C1) holds, then q₁, q₂ ∈ {d > 0}, so q ∈ {d > 0}, so q ∉ {P(·,−g) > 0}.

   In every case max_{K_q} m·g = −P(q,−g) ≥ 0. Non-mixed g ∈ C are ≥ 0, where this is trivial.
2. g ↦ max_{K_q} m·g is continuous, and a.e. g ∈ C is covered by step 1. Hence max_{K_q} g ≥ 0 for every g ∈ C.
3. If K_q ∩ [m₁,m₂] = ∅, strictly separate these compact convex sets in aff Δ by an affine function, and extend it to a
   linear g on ℝ³. Then g ∈ C and max_{K_q} g < 0, a contradiction. ∎

**Lemma Z (zero lines). PROVED.** Assume (C) on a convex open V ⊆ O. Let g ∉ N be mixed with σ·g taking both signs on V,
and put Z_g := {q ∈ V : σ(q)·g = 0}. Then:
- (C1) holds for g;
- L_d := {d·q = 0} meets V in a non-degenerate chord, and L_d ∩ V ⊆ Z_g;
- {σ·g > 0} ∩ V ⊆ {d > 0} and {σ·g < 0} ∩ V ⊆ {d < 0};
- if Z_g is convex and null, then Z_g = L_d ∩ V.

*Proof.*
- (C0) and (C0′) fail, because P(q,±g) = ±σ(q)·g on V.
- d·q is positive somewhere and negative somewhere on the convex open V, so L_d ∩ V is a nonempty relatively open chord.
  Its points lie in neither open side, so σ·g = 0 there.
- If q ∈ Z_g ∖ L_d, then conv({q} ∪ (L_d ∩ V)) ⊆ Z_g has positive area. ∎

## 3. Theorem D

**Lemma 2 (no segment images). PROVED.** Let V ⊆ O be convex and open. Then σ(V) is not a non-degenerate segment.

*Proof.*
1. *Set-up.* Suppose σ(V) = I = [a,b], a ≠ b; by Lemma SL, σ(V) is convex. For m ∈ σ(V), the fibre σ^{-1}(m) ∩ V is
   convex (Lemma SL with m₁ = m₂ = m).
2. *Good gambles.* By Fubini on the closed set {(q,g) ∈ V × ℝ³ : σ(q)·g = 0}, whose q-sections are planes, there is a
   null N′ such that λ(Z_g) = 0 for g ∉ N′. Call g *good* if it is mixed and g ∉ N ∪ N′.
3. *Pencils.* Put m(s) = a + s(b − a). Choose smooth bases A(s), B(s) of m(s)^⊥ and let F(s,α,β) := αA(s) + βB(s). Since
   m·A ≡ 0 gives m·A′ = −(b−a)·A (and likewise for B), the Jacobian of F is non-singular exactly where (b−a)·g ≠ 0, i.e.
   where ℓ_g is transverse to line(a,b). So F is a local diffeomorphism there, and pulls null sets back to null sets.
4. *Fubini.* For a.e. s ∈ (0,1), a.e. g ∈ m(s)^⊥ is good. Fix such an s. The point m := m(s) is not a vertex of Δ
   (vertices are extreme points of Δ, and m is interior to I).
5. *One d-line for the whole pencil.* Take a good g ∈ m^⊥ with ℓ_g ≠ line(a,b). Then ℓ_g ∩ I = {m}, and I has points
   strictly on both sides, so σ·g takes both signs on V and Z_g = σ^{-1}(m) ∩ V is convex and null. By Lemma Z,
   σ^{-1}(m) ∩ V = L_{d(g)} ∩ V, a fixed non-degenerate chord independent of g. Hence d(g) = λ_g d₀ with λ_g ≠ 0 for one
   fixed strictly signed d₀, and sign g = ±sign d₀ for every such g.
6. *Contradiction.* The plane m^⊥ (m ∈ Δ, not a vertex) meets at least two different mixed pair-classes {s, −s} in open
   cones of positive area: three when m ∈ Ω, two when m lies on an edge (NUMERICS (2) confirms 3 and 2). Removing the
   line {(b−a)·g = 0} leaves good gambles of two different classes, which contradicts step 5. ∎

**Lemma 3 (constant or injective). PROVED.** On every convex open V ⊆ O, σ is constant or injective.

*Proof.*
- Suppose σ(x) = σ(y) = m with x ≠ y, and σ is not constant on V. Pick z ∈ V ∖ line(x,y) with σ(z) ≠ m (perturb, by
  continuity), and let W := int conv{x,y,z} ⊆ V.
- Each p ∈ W lies on [z,p′] for some p′ ∈ [x,y], and σ(p′) = m (convex fibre). So by Lemma SL, σ(W) ⊆ [σ(z), m].
- σ(W) is convex, so it is a point or a non-degenerate segment. A segment is excluded by Lemma 2. If σ ≡ m′ on W, then
  continuity at x, z ∈ cl W gives σ(z) = m′ = σ(x) = m, a contradiction. ∎

**Lemma 4 (injective ⇒ diagonal-projective). PROVED.** If σ is injective on a convex open V ⊆ O, then σ = σ_w on V for
some w ∈ (0,∞)³.

*Proof.*
1. *Homeomorphism and collinearity.*
   - By invariance of domain (in the plane aff Δ), σ(V) is open, so σ(V) ⊆ Ω, and σ : V → σ(V) is a homeomorphism.
   - By Lemma SL and continuity, σ maps each segment [q,q′] ⊆ V onto [σq, σq′]. Combined with injectivity, σ^{-1} maps
     segments of σ(V) onto segments, so σ^{-1} also preserves collinear triples.
   - Hence, for every g in the open set G_V := {g : ℓ_g ∩ σ(V) ≠ ∅}, σ^{-1}(ℓ_g) = Λ(g) ∩ V for a line Λ(g) of priors.
2. *Continuity of the zero line.* Λ(g) depends continuously on g ∈ G_V: take two points of ℓ_g ∩ σ(V), approximate them
   on ℓ_{g_n}, and use continuity of σ^{-1}. Let δ(g) ∈ ℝ³ be the unit vector with {δ·q = 0} = Λ(g) and δ·q > 0 on
   σ^{-1}({m·g > 0}). It is unique, because an affine function on aff Δ determines its coefficient vector, and it is
   continuous on G_V.
3. *Strict signs.* For good g ∈ G_V (a.e.), Lemma Z gives L_{d(g)} = Λ(g) with the same orientation, so
   δ(g) = d(g)/|d(g)| has the strict sign of g.
   - At g ∈ G_V with g_i = 0, good gambles arbitrarily close on both sides of {g_i = 0} exist, so δ_i(g) = 0 by
     continuity.
   - **This is the only use of the diagonal (strict-sign) structure.**
4. *Vertex pencils are preserved.*
   - For g ∈ G_V with g₃ = 0, ℓ_g is a line through e₃ (so g₁g₂ < 0), and Λ(g) = {δ₁q₁ + δ₂q₂ = 0} is a line through e₃.
   - So for q, q′ ∈ V with q₁/q₂ = q′₁/q′₂, take g with g₃ = 0 and ℓ_g ∋ σ(q). Then Λ(g) = line(e₃, q) ∋ q′, so σ(q′) ∈ ℓ_g.
   - Hence σ₁/σ₂ = F₃(q₁/q₂), and cyclically σ₂/σ₃ = F₁(q₂/q₃), σ₃/σ₁ = F₂(q₃/q₁). The F_i are continuous and positive,
     since σ(V) ⊆ Ω and q ↦ q₁/q₂ is open.
5. *Pexider.* Put s = log(q₁/q₂), t = log(q₂/q₃), f_i = log F_i ∘ exp. Then f₃(s) + f₁(t) + f₂(−s−t) = 0 on the open
   connected image E of V.
   - On a rectangle in E, shifting s and t separately shows that φ(h) := f₃(s+h) − f₃(s) = f₁(t+h) − f₁(t) is
     independent of s and t and locally additive. Being continuous, φ(h) = αh.
   - So f₃ and f₁ are locally affine with a common slope. The projections of E are intervals, so there is one slope α.
   - Hence σ = ν(w⊙q^α) on V (componentwise power), with w = (c₁c₃, c₁, 1) > 0 for the constants c_i of F_i(x) = c_i x^α.
6. *α = 1.* On a segment {q₃ = c} in V, collinearity of the images (step 1) means the vectors
   (w₁s^α, w₂(k−s)^α, w₃c^α) span a 2-plane, i.e. Aw₁s^α + Bw₂(k−s)^α + Cw₃c^α ≡ 0 with (A,B,C) ≠ 0.
   - Differentiating gives α(Aw₁s^{α−1} − Bw₂(k−s)^{α−1}) ≡ 0. α = 0 is excluded by injectivity.
   - If A or B vanished, all three would vanish. Otherwise (s/(k−s))^{α−1} is constant on an interval, so α = 1.
   - (NUMERICS (1): the collinearity defect is 0 only at α = 1.) ∎

**Theorem D. PROVED.** Under the standing hypotheses and (C) on O, either σ is constant on O, or σ = σ_w on O for a
single w ∈ (0,∞)³. In the second case σ is injective, being the restriction of the bijection σ_w of Ω.

*Proof.*
- Let C₀ := {q ∈ O : σ is constant near q}, an open set.
- If q ∉ C₀, every convex ball B ∋ q in O carries a non-constant σ, which is injective by Lemma 3. Then B ∩ C₀ = ∅.
  So O ∖ C₀ is open too.
- By connectedness, either C₀ = O, and σ is locally constant, hence constant, or C₀ = ∅. In the latter case Lemma 4
  gives σ = σ_{w_B} on each convex ball.
- σ_w = σ_{w′} on an open set forces w ∝ w′, because the ratios σ_iq_j/(σ_jq_i) equal w_i/w_j. So w is locally
  constant up to scale, hence global. ∎

*Remarks.*
- (i) Hypotheses used: (C) on O and continuity of σ on O. Not used: (PC), (NS), the target, Hausdorff continuity off O,
  any regularity of chart data, and any half-plane or three-ray form.
- (ii) In the non-constant case every pair whose ℓ_g meets σ(O) is either adjacent through O (its closed d-face
  contains L_d ∩ O), or degenerate-split with c′ = −γc. Adjacency is therefore forced, not excluded. This is why the
  proof works on I2's collar and C2's caps.
- (iii) R4's sketch is repaired as follows:
  - its "(G)-signs exclude non-injective maps" is replaced by Lemma SL and Lemmas 2–3;
  - its appeal to the local fundamental theorem is replaced by steps 3–6 of Lemma 4;
  - R8's invariance-of-domain point is step 1 of Lemma 4.

## 4. Theorem T: one map for all precise priors

Assume (C) on Ω, and let O be as in Theorem D with σ = σ_w. Put G_O := {g mixed : ℓ_g ∩ σ_w(O) ≠ ∅} (open).

**Theorem T. PROVED.**
- (a) For every g ∈ G_O ∖ N, (C1) holds with d(g) ∝₊ w⊙g. Hence, on all of Ω,
  {P(·,g) > 0} ⊆ {σ_w(q)·g > 0} and {P(·,−g) > 0} ⊆ {σ_w(q)·g < 0}.
- (b) For every q′ ∈ Ω and every g ∈ G_O: P(q′,g) > 0 ⇒ σ_w(q′)·g ≥ 0.
- (c) (Cor T2, cone law.) For every q′ ∈ Ω and every m₀ ∈ σ_w(O) ∖ K_{q′}: σ_w(q′) ∈ m₀ + ℝ₊(K_{q′} − m₀).
- (d) Every precise q′ ∈ Ω has K_{q′} = {σ_w(q′)}.
- (e) If O′ is another open precise region with σ = σ_{w′}, then w′ ∝ w. No open wall (constant precise region) exists
  anywhere in Ω.

*Proof.*
- (a) σ_w(q)·g = (w⊙g)·q/(w·q). For g ∈ G_O, σ_w(O) is open, so it meets both sides of ℓ_g. Lemma Z (on a convex ball
  around a point of σ_w^{-1}(ℓ_g)) gives L_d = {(w⊙g)·q = 0} with matching orientation. So d ∝₊ w⊙g as vectors, and
  (C1) holds on Ω.
- (b) The condition P(q′,g) > 0 is open in g, and a.e. nearby g′ ∈ G_O satisfies (a). So σ_w(q′)·g′ > 0, and the limit
  gives ≥ 0.
- (c) Every g ⊥ m₀ lies in G_O and is mixed. Apply (b) to those g with K_{q′} strictly on the positive side of ℓ_g. The
  intersection of the resulting closed half-planes is the closed cone m₀ + ℝ₊(K − m₀); it is closed because m₀ ∉ K.
- (d) Take K = {σ′} in (c). σ_w(q′) lies on the closed ray from m₀ through σ′ for every m₀ ∈ σ_w(O) ∖ {σ′}. Two such m₀
  not collinear with σ′ (σ_w(O) is open) force σ_w(q′) = σ′.
- (e) By (d) for O and for O′, σ_w = σ_{w′} on O′, so w ∝ w′. A wall V would need σ_w ≡ m₀ on the open V, which is
  impossible since σ_w is injective. ∎

**Verdict on I2 step 4 (Prop 4).**
- (a) PROVED: Thm D. The constant case would be ≡ e_b, because U_b accumulates at e_b and K_q → {e_b}; that is excluded
  by vertexfree(i).
- (b) PROVED: Thm T(a).
- (c) PROVED: Thm T(d), (e). One map governs all precise priors, with the same w at all three vertices.

C2 Prop 5.2 = Thm T(e) (PROVED; C2's proof is also correct). C2's own Prop 4.3, which has W_b depending on b, therefore
contradicts T(e) directly; that is how C2 concludes.

## 5. Where each user stands now

| User | Step | Status after this note |
|---|---|---|
| I2 | Prop 4 (a)–(c) | PROVED (Thm D, Thm T) + vertexfree(i) |
| C2 | Thm 4.1 ⇒ "σ_b constant or ν(W_b·)" | PROVED (Thm D) |
| C2 | Prop 5.2 | PROVED (Thm T(e)) |
| C1 | Lemma 5.0 | PROVED, injectivity hypothesis dropped |
| C1 | Cor 5.4 | P_wild = ∅ (Thm D) |
| C1 | Prop 6.1 | no longer needs (LD): every component of int P is a wall or diagonal-projective, and Thm A leaves walls only |
| C1 | (W1) | becomes J_g ⊆ (P ∖ int P) ∪ N₁ for a.e. adjacent g |

## 6. Observation: a shorter route to "no cover of T1" (status = cited inputs)

The chain:
- I2 Thm 3 (≡ C2 Thm 4.1) gives an open precise set along the failing edge near each e_b.
- Thm D gives σ = σ_w there (constant excluded by vertexfree(i)).
- C1 Thm A says that no CF(T1) solution, hence no cover (Prop CF ⇒), has an injective open precise region.

Contradiction. Inputs and their status:
- I2 Lemma 1 / C2 Lemma 3.1, with Thm TSalways and (PC) cluster uniqueness: unrefereed.
- C1 Thm A: unrefereed; uses vertexfree(iv), one referee.

**This makes I2 §6 (transition algebra) and C2 Prop 4.3 (Bezout pinning) unnecessary for the impossibility.** It does
not raise the status beyond that of the three cited inputs.

## 7. Precise sets of positive area and empty interior (C1's (M1))

Let P := {q ∈ Ω : K_q a singleton}, relatively closed, with σ continuous on P, and assume (C) on Ω.

**Prop W. PROVED.**
- (W-i) Lemma SL holds for all q₁, q₂ ∈ P and every q ∈ [q₁,q₂] ⊆ Ω, precise or not: K_q ∩ [σq₁, σq₂] ≠ ∅.
- (W-ii) For every line L, σ maps L ∩ P into a line, order-preservingly (weakly).
- (W-iii) (Density d-line law.) For a.e. g with (C1), every Lebesgue density point y ∈ P ∩ L_{d(g)} of P has
  σ(y) ∈ ℓ_g.

  *Proof.* By Fubini, λ{q ∈ P : σ(q)·g = 0} = 0 for a.e. g. So near y, a.e. point of P ∩ {d > 0} (which has positive
  measure, by density) has σ·g > 0, and a.e. point of P ∩ {d < 0} has σ·g < 0. Continuity at y gives σ(y)·g = 0. ∎
- (W-iv) If int P has a non-constant component, then K_q = {σ_w(q)} on all of P (Thm T(d)).

For CF(T1) solutions, C1 Thm A excludes (W-iv)'s hypothesis. So int P consists of walls (or is empty), and (M1) is
exactly the question for P ∖ int P.

**Prop W′ (CHECKED, sketch).** Let P₁, P₂ ⊆ P have positive measure.
- They cannot carry σ_{w₁}, σ_{w₂} with w₁ ∦ w₂. Lines through density balls of P₁ and of P₂ meet both sets in positive
  length for a positive-measure set of g. By (W-iii), the d-line of such g is pinned to both {(w_i⊙g)·q = 0}, which is
  impossible for generic g.
- They cannot carry a wall and a projective piece. The pinned d-lines would cross a density ball of the wall, while the
  wall must lie on one side of each.

**Conjecture (M1).** At a.e. point of a positive-area precise set, σ is locally constant or σ_w (on P).

**7.4 Exactly where the proof breaks.**
- Lemma SL, Lemma Z and (W-iii) survive on P.
- What fails is the passage from "segment law" to "constant or injective homeomorphism". Lemma 3's triangle W and
  Lemma 4's invariance of domain and continuous zero line g ↦ Λ(g) all need σ on an open set.
- On P with empty interior:
  - the d-line of g is pinned only through density points;
  - g ↦ d-line is not known to be continuous (not even measurable);
  - σ^{-1}(ℓ_g) need not be contained in a line.
- A proof of (M1) needs a measure-theoretic replacement:
  - **either** approximate continuity of g ↦ L_{d(g)} at a.e. g (that suffices for step 3 of Lemma 4, "δ_i = 0 at
    g_i = 0", and steps 4–6 then run on density points);
  - **or** a direct proof that σ is injective on P at density points where it is not locally constant.

  Local fan- or Cantor-type candidates fail the pencil test (Lemma 2's mechanism: a pencil m^⊥ meets 2–3 sign classes,
  while separating lines through a thin gap realise one). I could not make this general.

## 8. Numerics (`propd_py/checks.py`, `checks.out`)

- (1) Images of random segments under ν(w⊙q^α): max |det|/|a−b|² is 0.31 (α = −1), 0.024 (α = .5),
  1.2·10⁻³ (α = .99 and α = 1.01), 2·10⁻¹⁵ (α = 1), 0.23 (α = 2).
- (2) Pencils m^⊥: the minimum number of mixed pair-classes is 3 for interior m and 2 for edge m (300 samples each).
- (3) σ = ν(Aq): the fraction of crossing gambles whose d = Aᵀg lacks the sign of g is 0 for diagonal A, and 1.5–6.5%
  for three non-diagonal positive A. So (C) singles out the diagonal maps.
- (4) Example E (f = (−1,2,2)) transported by D = diag(1,3,.5): 0 violations of (C) with d = D⁻¹g in 14 987 samples;
  the segment law holds to 10⁻¹⁶. This is a sanity check only, since the precise set there is convex.

## 9. What a second reader should check first

1. Lemma 2, step 3: the Jacobian identity m·A′ = −(b−a)·A, and that Fubini is applied to the Borel null superset of the
   bad gambles.
2. Lemma 4, step 2: continuity of Λ(g) uses only continuity of σ^{-1} on the open set σ(V).
3. Lemma 4, step 3: the two-sided approximation at g_i = 0 needs good gambles in G_V on both sides. G_V is open and the
   good set is co-null.
4. Thm T(a) is applied to every precise q′, including boundary points of P and points far from O. (C) on Ω is needed
   there, not just on O.
5. Lemma 1.1(b): the passage from a.e. to exact inclusion uses convexity of R_pen(g), not quasi-concavity of P.
