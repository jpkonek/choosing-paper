# AA3 — The intermediate test (∂Δ plus a path from T1): an endpoint obstruction for smooth additive fields

17 Oct 2026, round 29 (BRIEF21, intermediate test). Labels:
- **PROVED**: full proof here, not refereed;
- **CHECKED**: exact rational arithmetic (none needed this round);
- **CONJECTURE**;
- **NUMERICS**: floating-point; nothing depends on it.

Scripts are in `aa3py/`. Run each with `python3 -I aa3py/<script>`; outputs are in the matching `.out` files. No assumption is added: every extra hypothesis is a hypothesis of the result that states it.

**Read:** BRIEF21, AUDIT_Z123_loop (+ `audit_loopcheck/check.py`), Z1, Z2 (Z2.5–Z2.7, Z2.C, Q_Z2), Z3_referee, Y2, Y3, write-up §2.

**Notation** (write-up §2, Z2): c₀ = (1−ε)/3, λ = ε/c₀, A = 1+λ, **b\* := 1/(A+1)** (Z2's b), u = 𝟙/3. Worlds a, b, c always denote the three distinct worlds.

---

## 0. Outcome

**1. The additive question reduces exactly to six monotone functions (Prop. AA3.2, PROVED).** Suppose an additive strictly guiding field on the full domain carries the test: a closed coherent selection on ∂Δ ∪ γ, every axiom against every measurable competitor, with T1 selected at the start of γ. Then:
- the boundary pins the field to six nondecreasing *edge functions* s_ij;
- T1 at u becomes two families of functional equations (E1, E2) on them; and
- the test holds iff the set of interior weights carrying a coherent Bayes model contains a connected set Z ∋ u with cl Z ∩ ∂Δ ≠ ∅.

Reparametrisations, selections that are competitive without being Bayes at their own index, non-posterior families and ties are all covered: every selected model is Bayes at *some* weight, and Z is built from those weights.

**2. Endpoint obstruction (Thms AA3.7–AA3.8, PROVED).** Let 𝒞 be the class of fields whose six edge functions are C¹ with positive derivative except at x = A+1. In 𝒞, no such Z exists. **So no additive field in 𝒞 passes the intermediate test.**
- The kink at A+1 is *forced* by T1's corners (Lemma AA3.10), so 𝒞 is the natural smooth class.
- 𝒞 contains fields with T1 as u-Bayes model and coherent Bayes models on all of ∂Δ (Example AA3.11, PROVED). The theorem is not vacuous.
- The obstruction is new in kind. Z2.C locates the failure at T1 (isolation); this result locates it at the **far end** of the path, wherever the path meets ∂Δ:
  - approaching ∂Δ forces the two edge functions *out of the vanishing world* to be concave (or linear);
  - T1's corner identity needs one of them to accelerate.
- It does not need, and does not prove, isolation of u.

**3. Outside 𝒞 (CONJECTURE AA3.C).** The proofs use smoothness only at named places. Any additive counterexample must put a flat, a jump or a kink of an edge function exactly at:
- the endpoint's odds level; or
- x = 0 or x = A (vertex plateaus on edges, or jumps at A).

Each such feature is excluded near u for every departure direction except a median-type one (Remark AA3.12). Settling these residual cases is the remaining additive task. I do not claim it.

**4. Non-additive construction: not attempted.** The obstruction is proved only in 𝒞, so the brief's precondition for that branch (Z2.C proved for *all* additive rankings) is not met. §6 states precisely what a non-additive design must decouple.

**Nearby result (project preference).** The literal target, a decisive additive verdict, is reached for the natural smooth class 𝒞 and reduced to an explicit finite list of non-smooth escapes otherwise.

---

## 1. Reduction

Fix an additive strictly guiding field Ψ with integrable envelope on the full domain, and a selection p ↦ C_p on I := ∂Δ ∪ γ. Here γ is a path in Δ from an index p₀ with C_{p₀} = T1 to an index p₁ ∈ ∂Δ. The selection satisfies:
- coherence;
- competitiveness on supp p;
- closed sections relative to I.

The other clauses are not needed for the obstruction.

**Lemma AA3.1 (Bayes weights; PROVED).** Put Φ(p) := {w ∈ Δ : C_p is w-Bayes}. Then:
- (a) Φ(p) is nonempty, compact and convex, and Φ(p) ⊆ face(supp p);
- (b) Φ is upper hemicontinuous on I;
- (c) W := Φ(γ) is a continuum. After the rescaling of Prop diag(a), u ∈ W, and W ∩ ∂Δ ≠ ∅.

*Proof.*
- **(a)** The range {L(X) − L(C_p)} is convex (Aumann/Lyapunov; Y3.7 Step 0, Z3 §1.8). Competitiveness on supp p gives a separating weight supported in supp p.
- **(b)** This is Steps 2–4 of Thm Z2.6, which use only closed sections and compactness in measure of coherent models. Let p_n → p, w_n ∈ Φ(p_n), w_n → w\*. Then C_{p_n} → C\* along a subsequence, and C\* is w\*-Bayes. Closed sections and the interval range of each L_i give L(C_p) ≤ L(C\*) coordinatewise. Hence w\*·L(C_p) ≤ w\*·L(C\*), so w\* ∈ Φ(p).
- **(c)** A u.h.c. image of a connected compact set with connected compact values is a continuum.
  - T1 is Bayes at some interior weight, since it is not competitive on any proper face (Cor Z2.2′). Rescaling the world losses moves that weight to u.
  - Φ(p₁) lies in a proper face by (a). ∎

**Lemma AA3.1′ (boundary bumping; PROVED, standard).** Let Z be the component of W ∩ Δ° that contains u. Then Z is connected, Z ⊆ Δ°, and cl Z ∩ ∂Δ ≠ ∅. Every w ∈ Z has a coherent w-Bayes model, namely some C_p with w ∈ Φ(p).

*Proof.* Boundary bumping theorem (Nadler, *Continuum Theory*, Thm 5.4): in a continuum, the closure of every component of a proper open subset meets that subset's boundary. Apply it to the relatively open set W ∩ Δ°, which is proper because W meets ∂Δ. ∎

**Edge selection.** The same argument on each edge index-arc shows that every edge weight carries a coherent Bayes model (the Bayes-weight image of an edge arc is a continuum joining its two vertices). Its credal set is edge-supported (X3.2).

**Proposition AA3.2 (normal form; PROVED).** Under the above, there are nondecreasing functions s_ij : (0,∞) → [0,∞], one for each ordered pair i ≠ j, with the following properties.

- **(i) Pinning.** s_ij(x) is the switching odds w_j/w_i, on edge ij, of gambles with g_i > 0 > g_j and g_i/|g_j| = x. For a.e. mixed g and every w ∈ Δ, the Bayes acceptance of g at w is decided by the following, where S_ij(v) := 1/s_ij(1/v):
  - **M_c** (h_c = −1, h_a = x, h_b = y): accept iff w_a s_ac(x) + w_b s_bc(y) > w_c;
  - **O_c** (g_c = 1, g_a = −y, g_b = −z): accept iff w_a S_ca(y) + w_b S_cb(z) < w_c.
- **(ii) Edge coherence** is s_ij(x)·s_ji(1/x) ≤ 1, equivalently S_ij ≥ s_ji. Under it the two conditions in (i) are never both positive for the pair {h, −h}. So the Bayes advice *is* (i), with no M/O competition.
- **(iii) T1 at u.** Write facet F_c for the pair of edge functions s_ac, s_bc *into* c, and corner c for the slice O_c. Then:
  - **(E1)** s_ac(x) + s_bc(A − x) = 1 on (0, A), for every c;
  - **(E2)** S_ca(y) + S_cb(1 − Ay) = 1 on [b\*, 1/A], for every c. Equivalently, S_cb(z) = 1 − S_ca((1−z)/A) on [0, b\*].

  These hold wherever the functions are continuous.
- **(iv) Corner inequality.** S_ca(b\*−) + S_cb(b\*−) ≤ 1.
- **(v) Additive version of the test.** The test is solvable iff some such field has a connected Z ⊆ G′ := {w ∈ Δ° : some coherent w-Bayes model}, with u ∈ Z and cl Z ∩ ∂Δ ≠ ∅.
  - (⇒) Lemma AA3.1′.
  - (⇐) When the Bayes models along a path in G′ ∪ ∂Δ are a.e. unique and continuous in measure, Lemma Z1.2 (identity reparametrisation, plan V(p,i,X) = {q : Ψ_i(C_q) > Ψ_i(X)}) gives every axiom.

*Proof.*
- **(i)** This is edge pinning (Z2 §3, Y2.7). A coherent Bayes model at each edge weight forces the edge chart to depend on x alone, up to null sets. The function is monotone because the edge credal family sweeps.
  - With n(g) = m⊙g, the ratios m_i/m_j = s_ij(x)/x are fixed on every opposite-sign pair of coordinates. A mixed g has two such pairs, so n(g) is fixed up to a positive scale.
  - Writing out w·n(g) > 0 gives the M and O forms.
- **(ii)** Take h = (−1, x, y) in the M_a slice, so −h is an O_a gamble with the same (x, y). Accepting both would give w_b s_ba(x) + w_c s_ca(y) > w_a > w_b S_ab(x) + w_c S_ac(y). This contradicts S_ab ≥ s_ba and S_ac ≥ s_ca, which is the product condition (Z2 §3).
- **(iii)** T1's M_c boundary is x + y = A; its O_c boundary is the broken line through the corner (b\*, b\*) (Y2 §2, Z2 §3).
- **(iv)** The points (b\* − η, b\* − η) lie inside T1's O_c region. Use monotonicity.
- **(v)** As stated. ∎

**Remark.** Flats in s_ij are ties at edge weights, and jumps are flat credal endpoints. Prop AA3.2 allows both; non-uniqueness only enlarges G′, and (v) uses "some coherent Bayes model".

---

## 2. Two lemmas on approaching the boundary

All regions in the slice planes of Prop AA3.2(i) are monotone sets:
- M-regions are up-closed;
- O-regions are down-closed.

A coherent Bayes model has a convex accepted cone, so each slice region is convex. An up-closed set {(x, y) : y > Y(x)} is convex iff Y is convex, and similarly for the other cases.

**Lemma AA3.5 (endpoint concavity; PROVED).** Let w_n ∈ G′ with:
- w_n → p, where p_a, p_b > 0 and p_c = 0;
- s_ba strictly differentiable at x\* := s_ba⁻¹(p_a/p_b), with s_ba′(x\*) > 0.

Then s_ca is concave on (0, ∞).

*Proof.*
- **The slice.** In M_a, divide by w_b. Put κ_n = w_c/w_b → 0 and θ_n = w_a/w_b → θ = p_a/p_b. The region is {s_ba(x) > θ_n − κ_n s_ca(y)}.
- **Its boundary** is X_n(y) = σ(θ_n − κ_n s_ca(y)), where σ = s_ba⁻¹ is strictly differentiable at θ with σ′(θ) = D > 0. X_n is convex in y.
- **The limit.** For y, y′ in a compact subset of (0, ∞):
  [X_n(y) − X_n(y′)]/κ_n → −D(s_ca(y) − s_ca(y′)),
  uniformly, by strict differentiability, since the arguments converge to θ.
- Pointwise limits of convex functions are convex. So −D·s_ca is convex. ∎

**Variant at a vertex (PROVED, same proof).** Let w_n → e_c with w_{b,n}/w_{a,n} → ρ ∈ [0, ∞), and let s_ca be strictly differentiable at 0⁺ with s_ca′(0⁺) > 0.
- Normalise M_a by ε_n = w_a/w_c.
- If ρ > 0, s_ba is concave on {x : ρ s_ba(x) < 1}.
- If ρ = 0, normalise by w_b/w_c instead; then s_ba is concave on (0, ∞).
- The boundary is Y_n(x) = σ_ca(ε_n − ζ_n s_ba(x)), with σ_ca strictly differentiable at 0⁺.

**Lemma AA3.6 (crossing inequality; PROVED).** Let w ∈ G′ and let i, j, k be distinct. Put x₀ := s_ij⁻¹(w_j/w_i). Suppose s_ij is differentiable at x₀, s_kj at 0⁺ and S_ik at 0⁺, all with positive derivatives. Then

  s_ij(x₀) · S_ik′(0⁺) ≥ x₀ · s_kj′(0⁺).

If moreover s_ij is C¹ at A, then (E1) and (E2) turn this into **s_ij(x₀) ≥ x₀/A**.

*Proof.*
- **The plane.** In the plane g_j = −1, near (g_i, g_k) = (x₀, 0), the accepted set is {g_i > G(g_k)}, with G(0) = x₀.
  - For g_k > 0 it is the M_j slice: w_i s_ij(G) + w_k s_kj(g_k) = w_j, so G′(0⁺) = −w_k s_kj′(0)/(w_i s_ij′(x₀)).
  - For g_k < 0 it is the O_i slice: w_j S_ij(1/G) + w_k S_ik(|g_k|/G) = w_i. Using S_ij′(1/x₀) = s_ij′(x₀) x₀²/s_ij(x₀)² and s_ij(x₀) = w_j/w_i, this gives G′(0⁻) = −w_k w_j S_ik′(0)/(w_i² s_ij′(x₀) x₀).
- **Convexity.** The plane section of a convex cone is convex, so G is convex and G′(0⁻) ≤ G′(0⁺). This rearranges to the inequality.
- **The reduction to s_ij alone.**
  - (E1) in facet F_j gives s_kj′(0⁺) = s_ij′(A⁻).
  - (E2) in corner i gives S_ik′(0⁺) = S_ij′(1/A⁻)/A = A s_ij′(A⁺).
  - With C¹ at A, the inequality becomes s_ij(x₀) ≥ x₀/A. ∎

So along G′ every ordered pair satisfies s_ij(x₀) ≥ x₀/A at its own switching ratio. At u this is equality, since s_ij(A) = 1.

---

## 3. The endpoint obstruction

**Class 𝒞.** Every s_ij is C¹ with s_ij′ > 0 on (0, ∞) ∖ {A+1}, and has finite positive one-sided derivatives at A+1. In 𝒞:
- each s_ij is continuous and strictly increasing, so ties are null and every Bayes model is a.e. unique;
- (E1) and (E2) hold everywhere;
- s_ij(0⁺) = 0, s_ij(A) = 1 and s_ij(∞) = ∞.

The last item follows from (E1) and (E2) together with continuity:
- M_a at u gives s_ba(A) = 1 − s_ca(0⁺) ≤ 1;
- O_b at u gives s_ba(A) = 1/(1 − S_bc(0⁺)) ≥ 1;
- so s_ba(A) = 1 and s_ca(0⁺) = 0. In the same way S_ba(0⁺) = 0, which gives s_ba(∞) = ∞.

**Theorem AA3.7 (no endpoint on an open edge; PROVED).** Let Ψ ∈ 𝒞 have T1 as a u-Bayes model and coherent edges. No connected Z ⊆ G′ with u ∈ Z has a closure point p in an open edge (a, b).

*Proof.*
- **Step 1 (concavity).** Choose w_n ∈ Z with w_n → p. The level θ = p_a/p_b lies in (0, ∞) = s_ba((0, ∞)). Let x\* = s_ba⁻¹(θ).
  - If x\* ≠ A+1, Lemma AA3.5 applies directly.
  - If x\* = A+1, σ = s_ba⁻¹ has one-sided derivatives D_± > 0 at θ. Repeat the proof along a subsequence with (θ_n − θ)/κ_n → c ∈ [−∞, ∞]. The limit of the normalised boundaries is y ↦ φ(c − s_ca(y)), where φ(t) = D_+ t for t > 0 and D_− t for t < 0. Its convexity forces s_ca to be concave on {s_ca < c} and on {s_ca > c}.
  - These two sets meet at most at the single point y_c = s_ca⁻¹(c). If y_c < A+1, s_ca is C¹ at y_c, and a C¹ function concave on both sides of a point is concave across it. So s_ca is concave on (0, A+1] in all cases.
- **Step 2.** The same holds for s_cb, using M_b and the level p_b/p_a.
- **Step 3 (heights).** s_ca(0⁺) = 0, s_ca(A) = 1, and s_ca is concave on (0, A+1]. So s_ca(x)/x is nonincreasing, and s_ca(A+1) ≤ (A+1)/A. That is, **S_ca(b\*) ≥ A/(A+1)**. Likewise S_cb(b\*) ≥ A/(A+1).
- **Step 4 (corner).** Prop AA3.2(iv) and continuity give S_ca(b\*) + S_cb(b\*) ≤ 1. But the sum is at least 2A/(A+1) > 1. ∎

**Theorem AA3.8 (no endpoint at a vertex; PROVED).** Under the same hypotheses, no connected Z ⊆ G′ with u ∈ Z has e_c as a closure point.

*Proof.* Choose w_n ∈ Z with w_n → e_c and w_{b,n}/w_{a,n} → ρ. Relabel so that ρ ∈ [0, 1].

1. **(M_a endpoint.)** s_ca is C¹ at 0⁺, with s_ca′(0⁺) = s_ba′(A) > 0 by (E1). The vertex variant of Lemma AA3.5 then gives: s_ba is concave on {ρ s_ba < 1} ⊇ (0, A).
2. **(Sweep and crossing for (c, a).)** r := w_a/w_c is continuous on the connected set Z. It equals 1 at u and tends to 0 along w_n, so r(Z) ⊇ (0, 1].
   - Every x₀ ∈ (0, A] is therefore a switching ratio s_ca⁻¹(r) at some w ∈ Z.
   - Lemma AA3.6 (s_ca is C¹ at A and on (0, A]) gives s_ca(x₀) ≥ x₀/A on (0, A].
3. **s_ba and s_ca are linear on [0, A].**
   - By (E1), s_ba(x) = 1 − s_ca(A − x) ≤ x/A on (0, A).
   - Concavity with s_ba(0⁺) = 0 gives s_ba ≥ x/A.
   - Hence s_ba = s_ca = x/A on [0, A].
4. **s_ab and s_cb are linear on [0, A].**
   - Crossing for (c, b) (r = w_b/w_c sweeps (0, 1]) gives s_cb ≥ x/A on (0, A], hence s_ab ≤ x/A by (E1).
   - Crossing for (a, b): r = w_b/w_a sweeps an interval containing 1 and ρ, so s_ab ≥ x/A on [s_ab⁻¹(ρ), A].
   - If ρ > 0, the vertex variant for M_b makes s_ab concave on {s_ab < ρ}. A concave function with s_ab(0⁺) = 0, lying below x/A and equal to it at s_ab⁻¹(ρ), equals x/A there.
   - Hence s_ab = s_cb = x/A on [0, A]. The case ρ = 0 needs only the crossing.
5. **The functions out of c beyond 1/A.** S_ca(v) = Av and S_cb(v) = Av for v ≥ 1/A.
6. **(O_c endpoint.)** At w_n, the part of the O_c region with y ≥ 1/A is
   {1/A ≤ y < (w_c − w_b S_cb(z))/(A w_a)}.
   - Convexity forces z ↦ −S_cb(z) to be concave on {w_b S_cb(z) < w_c − w_a}.
   - That set increases to (0, ∞), since (w_c − w_a)/w_b → ∞.
   - So **S_cb is convex on (0, ∞)**. No regularity is used in this step.
7. **(Heights.)** A convex function that equals Av on [1/A, ∞) lies above that line. So S_cb(b\*) ≥ Ab\* = A/(A+1). By the symmetric argument (the part of the region with z ≥ 1/A), S_ca(b\*) ≥ A/(A+1).
8. **(Corner.)** This contradicts S_ca(b\*) + S_cb(b\*) ≤ 1. ∎

**Corollary AA3.9 (PROVED).** No additive strictly guiding field in 𝒞 passes the intermediate test: a closed coherent selection on ∂Δ plus a path from T1 to ∂Δ, even with arbitrary reparametrisation, non-Bayes-at-index selections, and any coherent families. Proof: Lemma AA3.1′ together with Theorems AA3.7 and AA3.8. ∎

**Reading.**
- Every way of reaching ∂Δ ends in the same conflict.
  - The last stretch of the path forces the two edge functions *out of the vanishing world* (s_ca and s_cb, or their S-forms) into concave or linear shape.
  - T1's corner in the O_c slice needs S_ca(b\*) + S_cb(b\*) = 1. Concave or linear shape caps each term below by A/(A+1) > 1/2.
- In words: the corner of T1 opposite world c needs one of the two edge families out of c to "accelerate" between odds A and A+1, and approaching the boundary forbids that.
- This is a statement about the **far end** of the path. It is compatible with u being non-isolated in G′ for some fields of 𝒞. Isolation (Z2.C) is neither proved nor needed.

---

## 4. Scope of 𝒞

**Lemma AA3.10 (the kink at A+1 is forced; PROVED).** If S_ca and S_cb are both differentiable at b\*, then S_ca′(b\*) = 0. So no field with T1 at u has all edge functions C¹ with positive derivative, and 𝒞 is the largest "smooth" class.

*Proof.* By (E2):
- S_ca′(b\*⁻) = S_cb′(b\*⁺)/A, and S_cb′(b\*⁻) = S_ca′(b\*⁺)/A.
- Equal one-sided derivatives give S_ca′ = S_ca′/A², so S_ca′(b\*) = 0. ∎

**Example AA3.11 (𝒞 is nonempty; PROVED).** Take, for all six ordered pairs:
- s_ij(x) = x/A on (0, A];
- S_ij = ρ on [b\*, 1/A], with ρ(v) = 1 + A(v − 1/A) + κ(v − 1/A)² and κ = (b\* − ½)/(1/A − b\*)² < 0;
- S_ij(v) = 1 − ρ((1−v)/A) on [0, b\*].

Then:
- (E1) and (E2) hold by construction, since ρ(b\*) = ½. So T1 is the a.e.-unique u-Bayes model.
- ρ′ ≥ A > 0, and ρ′(1/A) = A, so S is C¹ at 1/A.
- **Product condition.** Concavity gives ρ(Y) ≤ AY. Hence:
  - on [0, b\*], S(v) ≥ v ≥ v/A;
  - on [b\*, 1/A], ρ lies above its chord, which lies above v/A;
  - for v ≥ 1/A, S(v) = Av ≥ s(v).

  So every boundary Bayes model is coherent and a.e. unique.
- NUMERICS (ε = 3/10):
  - `c_example.out`: T1 error 1.4·10⁻¹⁴; max product 0.437; edge curvature ≥ 0.
  - `c_map.out`: on the 1/12-grid only u carries a coherent Bayes model. On circles of radius 0.05, 0.01 and 0.002 round u, 0/24 directions are coherent.

  This field therefore also isolates T1. Corollary AA3.9 needs no such fact.

**Remark AA3.12 (where non-smooth escapes would have to sit; PROVED for (a); the rest is analysis).**
- **(a) Kinks or jumps at A are excluded near u.** Suppose s_ca has a kink or jump at A, and Z leaves u in a direction δ with δ_c ≠ δ_a. Then the M_a or O_c slice at u + tδ shows a boundary piece whose normal ratio differs from that at T1's vertex v_a by the fixed factor s_ca′(A⁻)/s_ca′(A⁺).
  - The minimiser of m·h over K_t, for h near the crossing direction (−1, 0, A), must tend to v_a, because K_t → T1 in the Hausdorff metric (a.e.-uniqueness of the u-Bayes model).
  - Contradiction. So such a feature needs every departure direction to satisfy δ_a = δ_c.
- **(b) The Theorem AA3.7 escape.** It needs a flat or jump of s_ba at the endpoint level θ (ties there, or a flat credal endpoint), or a kink of s_ba at θ combined with a convex kink of s_ca below A+1.
  - Such a convex kink, visited in M_a at weights near u, is unbalanced unless Z stays on one line through u.
- **(c) The Theorem AA3.8 escape.** It needs s_ca(0⁺) > 0 (a vertex plateau E_c on part of edge ca). By (E1) this forces a jump of s_ba at A, which brings it back to case (a).

**CONJECTURE AA3.C.** Corollary AA3.9 holds without the class restriction: no additive field passes the intermediate test. The open cases are exactly the features in Remark AA3.12 at the named points, compatible with a median-type departure from u.

**NUMERICS (exploration, not relied on).**
- `t0_sanity.out` and `t2_vf.out` reproduce Z2.7 with the new code: Ψ^∂ is incoherent at u + tδ.
- `t1_e3design.out`: a design that is first-order consistent toward e₃ fails at t ≈ 0.01 at the O₃ corner. The cause is the corner-quadrant curvature μ_ρ31(b\*) + μ_ρ32(b\*) < 0, which is the local shadow of Step 2 of Theorem AA3.8.

---

## 5. Relation to earlier results

| Earlier result | Relation to this note |
|---|---|
| Z2.C (isolation) | Not proved. The intermediate-test consequence that Z2.C was wanted for is proved in 𝒞 by a different, end-of-path mechanism. Ψ^∂ ∉ 𝒞 (kinks at A); Example AA3.11 ∈ 𝒞. |
| Z1.8, audit loop L₁₂ | Consistent. L₁₂ omits two edges, so only one facet pair is pinned and the corner identity is never confronted with both edges out of a vanishing world. |
| Thm gm | Corollary AA3.9 is a one-dimensional localisation of Thm gm *within 𝒞*: boundary plus one path, not a 2-cell. |
| Lemma Z1.2 | Supplies the converse in Prop AA3.2(v). |

---

## 6. What a non-additive system must do (target, not a construction)

In the proofs, additivity enters in exactly one way: **one function s_ca governs three things.**
- (α) world comparisons at T1's O_c corner, at u;
- (β) the M_a and O_c competitiveness of the models selected near the endpoint;
- (γ) the crossing comparisons along the path.

A non-additive triple of independent preorders must keep all three families of forced comparisons while letting the "corner" record and the "endpoint" record of edge family ca be compared differently. Concretely:
- the comparisons that fix T1's corner (strict at b\*) must not imply concavity-type comparisons between near-endpoint models;
- yet both must be endorsed by guidance and (IB).

> **Q_AA3.** Is there a triple of independent preorders on the full domain, with a closed coherent selection on ∂Δ ∪ γ through T1, in which the world-c orders restricted to the record classes Q_a ∪ Q_b near the corner (b\*, b\*) and near the endpoint p are not jointly representable by one monotone edge function s_ca?

By the fixed-point theorem (L4, M3), the Hahn–Banach endorsers of such a system are degenerate somewhere. This note suggests where: at the endpoint, on the classes M_a and O_c.

---

## 7. Status

| Item | Status |
|---|---|
| AA3.1, AA3.1′ Bayes weights; component Z reaches ∂Δ | PROVED |
| AA3.2 normal form: six edge functions, E1/E2, no M/O overlap, corner inequality, equivalence with the test | PROVED |
| AA3.5 endpoint concavity (edge; vertex variant) | PROVED |
| AA3.6 crossing inequality s_ij(x₀) ≥ x₀/A along G′ | PROVED |
| **AA3.7 no endpoint on an open edge (class 𝒞)** | **PROVED** |
| **AA3.8 no endpoint at a vertex (class 𝒞)** | **PROVED** |
| **AA3.9 no additive field in 𝒞 passes the intermediate test** | **PROVED** |
| AA3.10 kink at A+1 forced; 𝒞 maximal smooth class | PROVED |
| AA3.11 𝒞 nonempty (T1 at u, coherent ∂Δ) | PROVED; NUMERICS (G′ = {u} on grids) |
| AA3.12(a) kinks or jumps at A excluded off median-type departures | PROVED |
| AA3.C no additive field at all | CONJECTURE |
| Non-additive construction for the test (Q_AA3) | not attempted (precondition unmet) |

**Referee priorities.**
1. Lemma AA3.6: signs of G′(0±), and the two reflections (E1 gives s_kj′(0⁺) = s_ij′(A⁻); E2 gives S_ik′(0⁺) = A s_ij′(A⁺)).
2. Theorem AA3.8, Steps 2 and 6: that r(Z) ⊇ (0, 1] uses connectedness of Z (Lemma AA3.1′); and the O_c region part {y ≥ 1/A} is convex iff S_cb is convex where it is defined.
3. Theorem AA3.7, Step 1 at x\* = A+1: the limit φ(c − s_ca) and its convexity.
4. Lemma AA3.1(b): u.h.c. of Φ, which relies on Z2.6 Steps 2–4.

## 8. Files (`aa3py/`)

- `vf.py`: vectorised pinned field from the six edge functions; Bayes thresholds H(θ) of the accepted cone; support-function test (H″ + H ≥ 0); monotonicity check.
- `fw.py`, `diag.py`: scalar version and defect locator.
- `t0_sanity.py`, `t2_vf.py` / `.out`: reproduce Z2.7 (NUMERICS).
- `t1_e3design.py` / `.out`: failed local design toward e₃ (NUMERICS).
- `c_example.py` / `.out`: Example AA3.11 checks (NUMERICS).
- `c_map.py` / `.out`: coherence map of Example AA3.11 (NUMERICS).
