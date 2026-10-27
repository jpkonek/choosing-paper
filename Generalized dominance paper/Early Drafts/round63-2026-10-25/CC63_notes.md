# CC63: composition constructor notes (25 Oct 2026)

Labels:
- **PROVED**: proved here, not yet independently refereed.
- **CHECKED**: exact rational computation.
- **CONJECTURE**.
- **NUMERICS**: none used for any claim below.

Scripts are in `cc63py/`. Run each from the folder `r63/` with `python3 -I cc63py/<name>.py`; each writes a `.out` file. Every decision is made in exact `Fraction` or integer arithmetic. The n = 4 hulls are computed by exact brute force, with no floating-point hull.

| Script | What it checks |
|---|---|
| `common.py` | exact hulls (n = 3 and n = 4), normal cones, world types S/T/A/C, cevian tests |
| `n3_composition.py` | the structure of orthant-planar polygons; the n = 3 no-new-target theorem on 1 500 random compositions; full hulls for the cyclic triangle and both hexagons |
| `n4_box_composition.py` | the new n = 4 target (entire hull); the pullback identity; the explicit VB certificate; a 25-case family test |
| `n4_facet_transfer.py` | Lemma NP on the n = 4 example |
| `verify_rc63.py` | independent checks of RC63's boundary pentagon and n = 4 instance, of RC63's ratio lemma and decoupling, and of the two-pair rule on random n = 4 compositions |
| `twopair_gap.py` | the one case where the two-pair rule misses a non-strictly-visible vertex |
| `contamination_check.py` | the tangent-cone step of Prop ZC, for n = 3, 4, 5 |
| `n3_triangles.py` | task (c): triangles with one or two cevian edges |

## 0. Summary

The composition theorem is assumed throughout. RC63 found it correct, and found that the composed ranking is VB(L′,A) run on the pushed-forward measure c₊μ.

1. **n = 3 with interior factors: composition produces no new target.**
   - I proved this independently, by a different route (Theorem N3: root-cone tiling of orthant-planar polygons).
   - It agrees exactly with RC63's ratio lemma, which I also confirmed (CHECKED: 8 037 vertices, 0 mismatches; decoupling 2 283 extreme points, 0 mismatches).
   - So task (a) as posed (n = 3, the cyclic triangle or a non-box hexagon as K₀) cannot succeed. The explicit hulls show exactly one surviving non-strictly-visible vertex (§2.4).
2. **Both of RC63's new examples are confirmed independently** (CHECKED, own exact hull code):
   - the n = 3 pentagon with its exempt point on an edge of the simplex;
   - the n = 4 interior target, with 31 vertices, 32 facets, 3 non-strictly-visible vertices and 6 facet normals with no zero coordinate.
3. **A geometric sufficient condition for n ≥ 4** (§4).
   - The ratio pattern R(x;K) is the set of ordered pairs (i,j) such that x minimises m_i/m_j over K. It decouples under composition, in any n: R(ν(q⊙m); L⋆K₀) = R(q;L) ∩ R(m;K₀) (PROVED).
   - An extreme point whose pattern has two pairs with different second index is never strictly visible (PROVED).
   - This gives Theorem F, a broad family: any normalised box composed with any VB-type L whose exempt point is the barycentre and which otherwise lies in the open region where one fixed world is most probable. Every member is covered, has at least 2^{n−1} − n ≥ 4 non-strictly-visible vertices (so it is not VB-type), and has a facet normal with three or more nonzero coordinates (so it is not orthant-planar).
   - A new explicit target: n = 4, 32 vertices and 33 facets, given in full in §4.6 (CHECKED).
   - The two-pair rule predicted the non-strictly-visible set exactly in 25 of 25 family cases, and in 19 of 20 unconstrained random cases. The 20th case shows the rule is sufficient but not necessary (CHECKED, §4.7).
4. **Boundary exempt points** (§5).
   - If π\* lies in the relative interior of a face Φ_S of the simplex with |S| ≥ 2, and L contains no e_i with i ∈ S, then L⋆K₀ is covered and lies outside both earlier classes, in every n ≥ 3 (PROVED). This generalises RC63's pentagon.
   - **ε-contaminations whose centre p has exactly one zero coordinate are never composed targets**, in any n ≥ 3, for any orthant-planar K₀ of any dimension and any VB-type L, wherever its exempt point lies (Prop ZC, PROVED; key step CHECKED).
5. **Task (c), n = 3 triangles.**
   - A triangle is a composed target iff it is VB-type: at most one vertex fails strict visibility.
   - Equivalently, the simplex vertices occupy the open opposite angles of at least two different vertices of the triangle.
   - **Two cevian edges: never.**
   - **One cevian edge: only if** the two simplex vertices off the cevian line sit in the opposite angles of two different vertices. That held in 690 of 5 000 random cases, and those triangles are already covered by O61 Thm C.
   - Everything else stays OPEN.

## 1. Setting and hypotheses (named)

- (H1) n worlds, simplex Δ, ν(x) := x/(𝟙·x). The barycentre is ū = 𝟙/n. The coordinate product is ⊙.
- (H2) μ is absolutely continuous with a finite first moment.
- (K0) K₀ ⊆ relint Δ is compact, convex and orthant-planar: on every mixed orthant σ, D_{K₀} ∩ σ = {d_σ·h > 0} ∩ σ.
- (L) L ⊆ Δ is compact and convex, with L = conv(L′ ∪ A₁ ∪ … ∪ A_n ∪ {π\*}). Here:
  - L′ ⊆ relint L is compact and convex;
  - each A_i ⊆ conv(L′ ∪ {e_i}) is compact.
  - "VB-type with exempt point π\*" means exactly this. For a polytope, it means every vertex except π\* is strictly visible.
- Composition: L⋆K₀ := conv{ν(q⊙m) : q ∈ L, m ∈ K₀}.
- The composition theorem is ASSUMED (AUDIT_r62 §1; refereed CORRECT by RC63). Under it, D_{L⋆K₀} is covered on U = D_{L′⋆K₀}, under global coherence, strict (G), (IB), transitivity, (C) and (LF).
- **The two earlier classes.**
  - *VB-type:* targets of some VB(K′,A) with at most one exempt point. For K ⊆ relint Δ this means all but at most one extreme point is uniformly visible (P61 Cor V6). For polytopes: at most one vertex is not strictly visible.
  - *Orthant-planar:* R2's class, inside relint Δ.
- World types at an extreme point x (O61): S strictly visible, T tangential, A anti-visible, C crossing. A point is "bad" if no world is S.

**Basic facts used.**

- **(F1) Normalisation (PROVED).** L⋆K₀ = ν(L⊘π\*) ⋆ ν(π\*⊙K₀) whenever π\* ≫ 0. So for interior π\* one may take π\* = ū.
- **(F2) Associativity (PROVED).** Projective diagonal maps preserve convex hulls, so ⋆ is associative. With the auditor's closure lemma, a second orthant composition gives L⋆(K₀⋆K₁): the same family again.
- **(F3) Reach (auditor; RC63 CORRECT).**
  - Extreme points of L⋆K₀ come from pairs of extreme points.
  - Strict visibility of q in L passes to ν(q⊙m).
  - Bad extreme points lie in ν(π\*⊙K₀).
  - Uniform visibility also transfers (PROVED). If q ∈ conv(L_δ ∪ e_j), then ν(q⊙m) ∈ [ν(k⊙m), e_j] with k ∈ L_δ, and ν(L_δ⊙K₀) is a compact subset of relint(L⋆K₀).

**Lemma O1 (any n; PROVED).** If K₀ ⊆ relint Δ is orthant-planar, then:
- every edge of K₀ lies on a line through a vertex of Δ (it is cevian);
- every facet of K₀ is two-term, of the form {r m_i − m_j ≥ 0}, written (i→j).

*Proof.*
- **Edges.** Suppose an edge [a,b] is not cevian. Its normal face F_a ∩ F_b has relative interior open in {a,b}^⊥, which is not contained in any coordinate hyperplane.
  - So it contains a point h with no zero coordinate, lying in some open orthant σ. This σ is mixed: ∂D_K misses both pure orthants.
  - Near h, ∂D_K ∩ σ contains open pieces of the two distinct hyperplanes a^⊥ and b^⊥. So D_K ∩ σ is not a half-space.
  - The same argument works for lower-dimensional K₀ (the normal face of an edge still has dimension n − 2).
- **Facets.** A facet Φ in a hyperplane Π has, at any vertex, at least n − 2 edges with independent directions. Each edge lies on a line x–e_i inside Π.
  - Distinct edges at a vertex use distinct i: two edges on the same line x–e_i would be collinear.
  - So Π contains at least n − 2 vertices of Δ, and its normal has at most two nonzero coordinates.
  - It has both signs, since K₀ ⊆ relint Δ. ∎

Consequences:
- A facet normal with three or more nonzero coordinates certifies "not orthant-planar".
- So does a non-cevian edge.

---

## 2. n = 3 with interior factors: no new targets

### 2.1 Structure of orthant-planar polygons (PROVED; CHECKED)

**Lemma A.** Let K₀ ⊆ relint Δ₃ be orthant-planar and w a vertex with normal cone F_w. Put G_w := {w⊙h : h ∈ F_w} ⊆ 𝟙^⊥. Then:
- (i) G_w is spanned by two of the six roots e_a − e_b, and the cones G_w of all vertices tile 𝟙^⊥.
- (ii) w is strictly visible iff G_w = cone{e_a − e_j, e_b − e_j}, a 60° "S-gap" (S at j).
- (iii) Otherwise G_w contains exactly one "A-gap" cone{e_a − e_b, e_a − e_c}, and a is the unique world from which w is anti-visible. G_w is either that 60° gap (type ATT) or a 120° arc made of an A-gap plus an S-gap (type ATC).
- (iv) Hence K₀ has exactly three bad vertices, anti-visible from worlds 1, 2 and 3 respectively.

*Proof.*
- An active facet r e_i − e_j has w_j = r w_i, so w⊙(r e_i − e_j) = w_j(e_i − e_j).
- In log coordinates z = log m (modulo 𝟙), K₀ becomes {z_j − z_i ≤ log r_ij}, a convex polygon. Its outward normal cone at w is −G_w, and normal fans tile.
- y_j = w_j h_j has the sign of h_j. Among arcs spanned by roots, only cone{e_a − e_j, e_b − e_j} avoids {y_j ≥ 0}∖0.
- The six 60° gaps alternate S₁, A₃, S₂, A₁, S₃, A₂ around the circle. A vertex arc is shorter than 180°, so it contains at most one A-gap.
- Each A-gap lies in exactly one vertex arc. ∎

CHECKED (`n3_composition.out`): cyclic triangles t = 3/2, 2, 3; the R10b hexagon; the REF62 holonomy-11/10 hexagon; the box [1,2]³; and 400 random cevian polygons. Every one has exactly 3 bad vertices, A-worlds {1,2,3}, and G-arcs tiling the circle.

### 2.2 The local obstruction (PROVED)

**Lemma B.** Normalise π\* = ū (F1). Let w be a vertex of K₀ that is an extreme point of K = L⋆K₀ and is not strictly visible in K. Then L ⊆ M_a := {q : q_a ≥ q_b for all b}, where a is w's anti-visible world in K₀.

*Proof.*
- Take h ∈ F^K_w. Since K ⊇ K₀, h ∈ F^{K₀}_w. Since ν(q⊙w) ∈ K, q·(w⊙h) ≥ 0 for all q ∈ L.
- So y := w⊙h lies in G_w ∩ D, where D := (L − ū)^* ∩ 𝟙^⊥.
- **Type ATT** (A at l). Non-strict visibility from k₁ forces the root e_l − e_{k₂} into D, and from k₂ it forces e_l − e_{k₁} into D.
- **Type ATC** (A at k₁). World k₂ forces e_{k₁} − e_l into D. World l then forces e_{k₁} − e_{k₂} into D, by convexity.
- In both cases D contains {e_a − e_b, e_a − e_c}, so L − ū lies in their dual, which is M_a − ū. ∎

### 2.3 Theorem N3 (PROVED; CHECKED)

**Theorem N3.** Let n = 3, let K₀ satisfy (K0), and let L be VB-type with exempt point π\* ∈ relint Δ (L of any dimension, but not a single point). Then L⋆K₀ has at most one bad extreme point, and every other extreme point is uniformly visible. So L⋆K₀ is VB-type (P61 V6) and is already covered by O61 Thm C.

*Proof.*
- By F1 and F3, bad extreme points are vertices of K₀ = ν(ū⊙K₀).
- Two bad ones have different anti-visible worlds (Lemma A(iv)). By Lemma B, L ⊆ M_a ∩ M_{a′} = {q_a = q_{a′} ≥ q_c}, a ray from ū along the cevian through e_c, away from e_c.
- **L full-dimensional:** impossible.
- **L a segment [ū, b]:** b lies on that ray on the far side from e_c, so b ∉ conv(L′ ∪ e_i) for every i. Then b would be a second exempt point.
- Uniform visibility of the remaining extreme points comes from F3. ∎

This is equivalent to RC63's count N(L⋆K₀) ≤ min(N(L), N(K₀)). Their "q\* minimises both q_a/q_b" is exactly "ν(L⊘q\*) ⊆ M_a".

CHECKED:
- `n3_composition.out`: 1 500 random VB-type L with exempt point anywhere in relint Δ, against named and random K₀. The number of bad vertices was 0 in 389 cases and 1 in 1 111 cases, never more. Every bad vertex lies in ν(π\*⊙K₀), with the normalised L inside M_a.
- `verify_rc63.out`: RC63's ratio lemma (8 037 vertices) and decoupling (2 283 extreme points), with 0 mismatches.

### 2.4 Requested factors computed exactly (CHECKED)

Factor: L = conv{ū, (9,5.4,5.6)/20, (11,5.4,3.6)/20, (9,7.4,3.6)/20}, i.e. conv(ū, (1−ε)p₀ + εe_j) with p₀ = (5,3,2)/10 and ε = 1/10. Here:
- L ⊆ M₁;
- ū is exempt;
- the other vertices are strictly visible.

| K₀ | vertices of L⋆K₀ | bad vertices | non-cevian edges | verdict |
|---|---|---|---|---|
| cyclic triangle (t = 2) | 7 | 1: (1,4,2)/7, type ATC, the A-at-1 vertex | 4 | VB-type (exempt), not new |
| R10b hexagon | 10 | 1: (2/9,4/9,1/3), type ATT | 4 | VB-type, not new |
| REF62 hexagon (holonomy 11/10) | 10 | 1: (1/5,2/5,2/5), type ATT | 4 | VB-type, not new |

`n3_composition.out` lists every vertex with its source pair and its edge normals. In each case the surviving bad vertex is exactly the vertex of K₀ anti-visible from world 1, as Lemma B predicts.

---

## 3. Independent verification of RC63's examples (CHECKED, `verify_rc63.out`)

**Boundary pentagon (RC63 §3.5).**
- K₀ is the cyclic triangle and L = conv{(1,2,2)/5, (1/2,1/2,0), (1,3,1)/5}, with π\* = (1/2,1/2,0).
- The other two vertices of L are strictly visible (from worlds 3 and 2).
- My hull gives exactly the stated pentagon: (1,12,2)/15, (1,8,4)/13, (1,1,4)/6, (2,1,0)/3, (1,4,0)/5.
- Its extreme points with support exactly {1,2} are (2/3,1/3,0) and (1/5,4/5,0). These are the endpoints of ν(π\*⊙K₀).
- RC63's L′ (the centre and the points v + (v−e_j)/10) lies strictly inside L. L′⋆K₀ lies strictly inside K.
- Edges 2 and 4 are cevian; the other three are not. **Confirmed.**

**n = 4 interior instance (RC63 §3.6).**
- L = ν of the five given vectors. My exact brute-force hull finds exactly 1 bad vertex of L.
- K₀ = ν([1,2]×[1,3]×[1,5/2]×[1,9/5]).
- K has 31 vertices, 32 facets and 61 edges; Euler gives 31 − 61 + 32 = 2.
- It has exactly 3 bad vertices, of types TATT, TAAT and TTAT. All three are tangential from some world, so none is "non-visible" in O61's strong sense.
- 6 facet normals have no zero coordinate. All 3 bad vertices are ν(q\*⊙m) with m bad in K₀. K lies inside relint Δ.
- The two-pair rule (§4.3) predicts exactly these 3. **Confirmed.**

---

## 4. n ≥ 4: a geometric sufficient condition and a broad family

### 4.1 Ratio patterns and decoupling (PROVED; CHECKED)

For x ∈ K, put R(x;K) := {(i→j) : i ≠ j, x minimises m_i/m_j over K}. For a polytope K ⊆ relint Δ, (i→j) ∈ R(x;K) iff the two-term vector r e_i − e_j (with r = x_j/x_i) lies in F_x.

**Lemma R (any n, interior factors).** For x = ν(q⊙m) with q ∈ L and m ∈ K₀:

  R(x; L⋆K₀) = R(q;L) ∩ R(m;K₀).

*Proof.* Ratios multiply: the (i,j) ratio of ν(q′⊙m′) is (q′_i/q′_j)(m′_i/m′_j).
- (⊇) is immediate, and minimising over the hull equals minimising over the products.
- (⊆): fix m and vary q′ ∈ L, then fix q and vary m′ ∈ K₀. ∎

For a box K₀ = ν([α,β]) and a vertex ν(x) with lower set L(x) and upper set H(x): R = L(x) × H(x).

### 4.2 Two-pair rule (any n; PROVED)

**Lemma TP.** Let x be an extreme point of a full-dimensional K ⊆ relint Δ. If R(x;K) contains (i₁→j₁) and (i₂→j₂) with j₁ ≠ j₂, then x is not strictly visible from any world.

*Proof.* g = r e_i − e_j ∈ F_x has g_k ≥ 0 for every k ≠ j. For each world k, use a pair whose j differs from k. Then apply Lemma V1. ∎

### 4.3 Theorem G (sufficient condition for bad extreme points of L⋆K₀; PROVED)

Let K₀ satisfy (K0), let L be compact and convex, let w be a vertex of K₀, and let Π ⊆ R(w;K₀) be a set of active facet pairs. Assume:
- (G1) q_i ≥ q_j on L for every (i→j) ∈ Π. Equivalently, ū ∈ L and (i→j) ∈ R(ū;L).
- (G2) L ∩ {q_i = q_j for all (i→j) ∈ Π} = {ū}.
- (G3) the second indices of the pairs in Π take at least two values.

Then w is an extreme point of K = L⋆K₀, and w is not strictly visible from any world.

*Proof.*
- **Support.** r q_i m_i − q_j m_j ≥ q_j(r m_i − m_j) ≥ 0, so each g is a supporting normal of K at w. Lemma TP then gives non-strict visibility.
- **Extremality.** Equality forces q_i = q_j and m on the facet. So the face E = K ∩ ⋂_Π{g·m = 0} equals the face K₀ ∩ ⋂_Π{g·m = 0} of K₀. Its extreme point w is therefore extreme in K. ∎

**Feasibility.** (G1)–(G3) can be met for several vertices at once by a full-dimensional L iff the union of all chosen pairs is acyclic as a directed graph on worlds. One can then take L∖{ū} inside the open order cone.
- For n = 3 the union is always cyclic, which is Theorem N3 again.
- For n ≥ 4 it need not be.

### 4.4 Lemma NP (box factor: the facets of L reappear; PROVED; CHECKED)

Let K₀ = ν([α,β]) and let η be a facet normal of L (η·q ≥ 0 on L). Put m\* := ν(x\*), where x\*_i = α_i if η_i ≥ 0 and x\*_i = β_i if η_i < 0. Then η⊘m\* is a facet normal of L⋆K₀, with the same zero pattern as η.

*Proof.*
- Σ_i q_i η_i x_i/x\*_i ≥ Σ_i q_i η_i ≥ 0: positive terms only grow, and negative terms only shrink in size.
- The hyperplane contains ν(q⊙m\*) for every q in the facet. That set is (n−2)-dimensional. ∎

CHECKED: all 6 facets of the §4.6 factor L reappear in K (`n4_facet_transfer.out`).

### 4.5 Theorem F: the box family (PROVED, given the composition theorem)

**Hypotheses.**
- n ≥ 4.
- (F-a) K₀ = ν([α,β]) with 0 < α ≪ β.
- (F-b) L ⊆ relint Δ is full-dimensional and VB-type with exempt point ū.
- (F-c) L∖{ū} ⊆ int M_a for some world a, i.e. q_a > q_b for all b ≠ a.
- (F-d) some facet normal of L has three or more nonzero coordinates.

**Conclusions,** for K := L⋆K₀:
1. K is covered on U = D_{L′⋆K₀} by the composed ranking. The chart is c_j(h) = α_j h_j for h_j > 0 and β_j h_j for h_j < 0.
2. Every box vertex ν(x) with x_a = α_a and at least two coordinates at β is a bad extreme point of K. Take Π = {a→j : j ∈ H(x)} in Theorem G. There are at least 2^{n−1} − n ≥ 4 of them, so K is **not VB-type** (P61 V6).
3. K has a facet normal with three or more nonzero coordinates (Lemma NP), so K is **not orthant-planar** (Lemma O1).

So K is a covered target outside both earlier classes.

**The family is non-empty and open-ish (PROVED).** Take L = conv({ū} ∪ {(1−ε)p₀ + εe_j : j}) with p₀ ∈ int M_a and ε < min_{b≠a} (p₀_a − p₀_b)/(1 + p₀_a − p₀_b). Then (F-b) and (F-c) hold, with an explicit certificate:
- L′ = {p₀}, which is interior to L;
- A_j = {(1−ε)p₀ + εe_j} ⊆ [p₀, e_j];
- π\* = ū.

(F-d) held in every random instance (CHECKED).

### 4.6 The explicit new target (CHECKED, `n4_box_composition.out`)

**Factors.**
- K₀ = {m : m_j ≤ 2m_i for all i, j} = ν([1,2]⁴): 14 vertices, 12 two-term facets, cevian edges, 10 bad vertices.
- L = conv{ū, v₁, …, v₄}, with v_j = (19/20)p₀ + (1/20)e_j and p₀ = (4,3,2,1)/10:
  - ū = (1/4,1/4,1/4,1/4), type CCCC (exempt);
  - v₁ = (43/100, 57/200, 19/100, 19/200), type SCCC;
  - v₂ = (19/50, 67/200, 19/100, 19/200), type CSCC;
  - v₃ = (19/50, 57/200, 6/25, 19/200), type CCSC;
  - v₄ = (19/50, 57/200, 19/100, 29/200), type CCAS.
- L∖ū lies in the open chamber q₁ > q₂ > q₃ > q₄.
- Facets of L: (−19,−19,−19,181), (−19,−19,81,−19), (−19,29,9,−19), (−19,43,−19,−5), (5,−19,33,−19), (67,−57,−57,47). All six have 3 or more nonzero coordinates.

**Composed ranking.** At world i, on X ⊆ U:
- c(h) = h⁺ − 2h⁻;
- U = D_{K′}, with K′ = ν(p₀⊙K₀) = {m_j/m_i ≤ 2p₀_j/p₀_i};
- a_i(X) = ∫_X max(0, −v_i·c(h)) dμ;
- b_i(X) = −∫_X c_i(h) dμ;
- the levels are ordered lexicographically, and the exempt point is ū.

**The entire hull K = L⋆K₀.** It has 32 vertices, 63 edges and 33 facets; Euler 32 − 63 + 33 = 2. Each vertex is listed with its world types (in world order) and its source (L-vertex index, K₀-vertex index). "bad" marks vertices that are not strictly visible.

| # | vertex | types | source |
|---|---|---|---|
| 1 | (1/5,1/5,1/5,2/5) | AAAS | ū |
| 2 | (1/5,1/5,2/5,1/5) | AASA | ū |
| 3 | (1/6,1/6,1/3,1/3) | AATT **bad** | ū |
| 4 | (1/5,2/5,1/5,1/5) | ASAA | ū |
| 5 | (1/6,1/3,1/6,1/3) | ATAT **bad** | ū |
| 6 | (1/6,1/3,1/3,1/6) | ATTA **bad** | ū |
| 7 | (1/7,2/7,2/7,2/7) | ATTT **bad** | ū |
| 8 | (1/3,1/6,1/6,1/3) | TAAS | ū |
| 9 | (1/3,1/6,1/3,1/6) | TASA | ū |
| 10 | (2/7,1/7,2/7,2/7) | TATT **bad** | ū |
| 11 | (2/7,2/7,1/7,2/7) | TTAS | ū |
| 12 | (86/143,57/286,19/143,19/286) | SAAA | v₁ |
| 13 | (172/305,57/305,38/305,38/305) | SAAT | v₁ |
| 14 | (43/81,19/108,19/81,19/324) | SATA | v₁ |
| 15 | (172/343,57/343,76/343,38/343) | SATT | v₁ |
| 16 | (172/343,114/343,38/343,19/343) | STAA | v₁ |
| 17 | (86/181,57/181,19/181,19/181) | STAT | v₁ |
| 18 | (172/381,38/127,76/381,19/381) | STTA | v₁ |
| 19 | (76/267,134/267,38/267,19/267) | ASAA | v₂ |
| 20 | (38/143,67/143,19/143,19/143) | ASAT | v₂ |
| 21 | (76/305,134/305,76/305,19/305) | ASTA | v₂ |
| 22 | (152/343,134/343,38/343,19/343) | TSAA | v₂ |
| 23 | (76/181,67/181,19/181,19/181) | TSAT | v₂ |
| 24 | (152/381,134/381,76/381,19/381) | TSTA | v₂ |
| 25 | (19/62,57/248,12/31,19/248) | AASA | v₃ |
| 26 | (76/305,114/305,96/305,19/305) | ATSA | v₃ |
| 27 | (38/81,19/108,8/27,19/324) | TASA | v₃ |
| 28 | (152/343,57/343,96/343,38/343) | SAST | v₃ |
| 29 | (152/381,38/127,32/127,19/381) | TTSA | v₃ |
| 30 | (38/143,57/143,19/143,29/143) | ASAS | v₄ |
| 31 | (152/305,57/305,38/305,58/305) | SAAS | v₄ |
| 32 | (76/181,57/181,19/181,29/181) | TTAS | v₄ |

**Facet normals** (h with h·m ≥ 0 on K):
- 12 two-term facets: (2,−1,0,0), (2,0,−1,0), (2,0,0,−1), (0,2,−1,0), (0,2,0,−1), (0,0,2,−1), (−57,172,0,0), (−19,0,0,172), (−19,0,86,0), (0,−19,0,134), (0,−19,67,0), (0,0,−19,96). The first six are exactly the box facets (i→j) with i < j: the chamber order of L.
- 15 facets with 3 nonzero coordinates: (−57,248,−57,0), (−38,134,0,−29), (−19,−19,0,286), (−19,−19,143,0), (−19,0,−19,248), (−19,0,105,−19), (−9,0,94,−38), (−9,56,−19,0), (0,−19,−19,210), (0,−19,86,−19), (0,−9,56,−19), (0,29,−19,9), (29,−19,9,0), (32,−19,0,6), (58,0,−57,56).
- 6 facets with 4 nonzero coordinates, each a triangle: (−19,−19,−19,362), (−19,−19,162,−19), (−19,58,18,−19), (−19,86,−19,−5), (10,−19,66,−19), (134,−57,−57,94). These are the six facets of L transferred by Lemma NP.

**Verdicts (CHECKED).**
- K has 5 bad vertices, nos. 3, 5, 6, 7 and 10. These are the box corners (1,1,2,2), (1,2,1,2), (1,2,2,1), (1,2,2,2) and (2,1,2,2), normalised.
- Theorem G predicts exactly these five. Corner (2,1,2,2) is caught through the pairs 2→3 and 2→4, which L's chamber order allows.
- So K is **not VB-type**.
- 24 of the 63 edges are non-cevian, and 21 facets are not two-term. So K is **not orthant-planar**.
- Pullback identity {h : c(h) ∈ D_L} = D_K: 20 000 random integer gambles, 0 mismatches, and the 38 exact ties agree.
- The same identity holds for Q = L′ = {p₀} and for each Q = {v_j} (4 000 gambles each, 0 mismatches).

All bad vertices are tangential from 2 or 3 worlds. So O61 Thm A, which needs non-visibility in the strong sense, says nothing about them. Exclusion from VB-type rests on P61 V6, which only needs non-strict visibility.

### 4.7 How sharp is the condition? (CHECKED / CONJECTURE)

- **Family test** (`n4_box_composition.out`): 25 random boxes, random a, and random L of the contamination-cone form, some with an extra vertex.
  - 0 failures of Theorem F.
  - In all 25 cases the Theorem G prediction (pairs i→j with q_i > q_j on L∖ū) equals the exact bad set.
- **Unconstrained L** (`verify_rc63.out`): 20 random L with at most one bad vertex, against random boxes.
  - The two-pair rule is always a subset of the bad set (as proved), and equals it in 19 of 20 cases.
- **The gap case** (`twopair_gap.out`).
  - The vertex x = (9/109, 144/545, 126/545, 46/109), of type ATTT, has R(x;K) = {1→4} only. Worlds 1, 2 and 3 are covered by the two-term normal (46,0,0,−9).
  - World 4 is covered by the three-term normal (448,−35,−120,0). Its zero is at coordinate 4: x is a silhouette point of K seen from e₄.
  - So the two-pair rule is **sufficient, not necessary**.
- **Silhouette decoupling (PROVED).** Let π_j drop coordinate j and renormalise. Then π_j(ν(q⊙m)) = ν(π_j(q)⊙π_j(m)), so π_j(L⋆K₀) = π_j(L)⋆π_j(K₀), computed in n − 1 worlds.
  - x is strictly visible from j iff π_j(x) ∈ relint π_j(K) and x is the end of K ∩ line(e_j, x) nearer e_j. This is a reformulation of P61 V1.
  - An exact recursive description of the bad extreme points of L⋆K₀ for n ≥ 4 should be built from Lemma R and this decoupling. **CONJECTURE**: it closes. I have not proved the fibre-endpoint part.

**Necessary conditions for any n (PROVED).**
- (N1) RC63's symmetric reach: bad interior extreme points are ν(q\*⊙m) with m bad in K₀.
- (N2) Lemma NC. If dim K₀ = d ≥ 1, every extreme point x of L⋆K₀ in relint Δ is a vertex of some copy ν(q⊙K₀) ⊆ K with q ∈ ext L ∩ relint Δ. That copy is orthant-planar with cevian edges (Lemma O1). So the tangent cone T_xK contains at least d independent directions of the form ±(e_j − x).
  - Proof: x is extreme in K, hence in the copy; the copy is a projective diagonal image of K₀.

---

## 5. Boundary exempt points

### 5.1 Theorem BE (any n ≥ 3; PROVED, given the composition theorem)

**Hypotheses.**
- K₀ satisfies (K0) and is full-dimensional.
- L is full-dimensional and VB-type with exempt point π\* ∈ ∂Δ, where π\* lies in the relative interior of the face Φ_S = {m : supp m ⊆ S} with |S| ≥ 2.
- (BE) e_i ∉ L for every i ∈ S.

**Conclusions.**
- (i) K = L⋆K₀ is covered on U = D_{L′⋆K₀}. O61 Thm C allows π\* ∈ ∂Δ, and RC63 checked the exempt identity there.
- (ii) K ∩ Φ_S = ν(π\*⊙K₀). This is the coordinate projection of K₀ onto R^S, renormalised and rescaled by π\*. It has dimension |S| − 1 ≥ 1, so it has at least two extreme points of support exactly S.
- (iii) Hence K is not VB-type. In K(W0,β,α), the generators with support exactly a proper S are:
  - none from K′ (interior);
  - from A_ω, only e_ω;
  - from Ŵ, at most one extreme one.
  This is RC63's count, re-derived here: the coefficient pattern is forced to λ ∈ {0,1}, and supp β ⊆ W0.
- (iv) K is not orthant-planar, because it meets ∂Δ.

*Proof of (ii).* Points of L in Φ_S:
- L′ is interior, so it contributes none.
- Points of A_i other than e_i are interior.
- e_i ∉ L by (BE).
- So L ∩ Φ_S = {π\*}. Products with q = π\* give ν(π\*⊙K₀). ∎

RC63's pentagon is the case n = 3, S = {1,2}.

This class is broad: any π\* in the relative interior of a face, any VB-type completion of L, and any orthant-planar K₀ (cyclic triangles, hexagons, boxes).

### 5.2 Prop ZC: zero-support ε-contaminations are never composed targets (PROVED; CHECKED)

**Statement.** Let n ≥ 3, 0 < ε < 1, and let p have exactly one zero coordinate k. Then K = (1−ε)p + εΔ is not L⋆K₀ for any orthant-planar K₀ (of any dimension) and any VB-type L, wherever the exempt point lies.

*Proof.*
- **Case dim K₀ = 0.** The composition is VB itself, and P61 D3 excludes K.
- **The interior vertex.** v_k = (1−ε)p + εe_k lies in relint Δ. Its tangent cone is T = cone{e_i − e_k : i ≠ k}.
- **Only one cevian direction fits.** Of the 2n directions ±(e_j − v_k), only v_k − e_k lies in T. CHECKED exactly for n = 3, 4, 5, with 500 random (p, ε) each and 0 exceptions. In general:
  - e_j − v_k has negative coordinates at every i ∉ {j,k}, since p_i > 0;
  - v_k − e_j is negative at j;
  - e_k − v_k is negative off k.
- **dim K₀ ≥ 2.** By Lemma NC, v_k would need at least 2 independent cevian directions in T. Impossible.
- **dim K₀ = 1.** K₀ is a cevian segment (Lemma O1, edge part). Its copy through v_k must run along line(e_k, v_k), so K₀ lies on a line through e_k.
  - Then all coordinate ratios not involving k are constant on K₀, and ν(π\*⊙K₀) is a single point.
  - But the face K ∩ {m_k = 0} = (1−ε)p + εΔ_{Ω∖k} has n − 1 ≥ 2 extreme points.
  - That face must be conv(ν(π\*⊙K₀) ∪ E′) with E′ a set of simplex vertices, and E′ is empty because e_i ∉ K. Contradiction. ∎

So the boundary composition (Theorem BE) does **not** reach the D3-excluded contaminations. It reaches different boundary targets: faces ν(π\*⊙K₀) on ∂Δ attached to interior parts whose corners carry two cevian directions.

---

## 6. Task (c): n = 3 triangles with one or two cevian edges (PROVED; CHECKED, `n3_triangles.out`)

**Vertex-region lemma.** w is strictly visible from j iff e_j lies in the open opposite angle at w, i.e. e_j = w + s(w−w′) + t(w−w″) with s, t > 0. This is because strict visibility means w − e_j lies in the interior of the tangent cone.

The three opposite angles of a triangle are disjoint. A simplex vertex lying on an edge line lies in none of them.

CHECKED: 3 000 random triangles; the normal-cone test and the angle test give 0 mismatches.

**Classification** (interior triangles, n = 3; composed with interior factors, hence VB-type by N3):
- **Two cevian edges** (necessarily through two different simplex vertices). Only the third simplex vertex can occupy an opposite angle, so at least two vertices are bad: **never composed**, and not orthant-planar.
  - CHECKED on 3 000 random cases: 2 bad in 1 994, 3 bad in 1 006.
  - Example: conv{(6,4,1)/11, (3/5,1/10,3/10), (3/4,1/8,1/8)}, types CTC, CCT, SAA.
- **One cevian edge, through e_k.** At most two vertices can be strictly visible, so at least one is bad.
  - It is composed (and already covered by O61 Thm C) **iff** e_i and e_j lie in the opposite angles of two different vertices.
  - CHECKED on 5 000 random cases: 1 bad in 690, 2 bad in 3 489, 3 bad in 821. The angle criterion agreed in all 5 000.
  - Covered example: conv{(1,6,1)/8, (6,1,10)/17, (6,1,1)/8}, types CSC, CCT, SCA.
  - Open example: conv{(1,6,1)/8, (6,1,3)/10, (6,1,1)/8}, types CCC, CAT, SCA.
- **Boundary variant (Theorem BE).** A composed n = 3 target with π\* on an edge has an edge on ∂Δ, so it is never an interior triangle.

---

## 7. What is still not reached (exact statements)

1. **n = 3, interior targets.** Composition adds nothing (Theorem N3; RC63).
   - The unreached interior class is unchanged: compact convex K ⊆ relint Δ₃ with at least two extreme points that are not uniformly visible, and which are not cevian polygons.
   - For polygons: at least 2 bad vertices and at least 1 non-cevian edge.
   - This includes the reversed triangle, T1, every triangle with exactly two cevian edges, every one-cevian triangle failing the angle criterion, and about 63% of random triangles (O61 numerics).
2. **n = 3, boundary targets.**
   - Reached: Theorem BE targets and VB-type targets.
   - Not reached:
     - zero-support contaminations (Prop ZC);
     - any boundary target with an interior extreme point whose angle contains fewer than two cevian rays (Lemma NC), unless the target is VB-type.
   - A characterisation of the composed boundary targets is OPEN.
3. **n ≥ 4.**
   - Reached: Theorem F (box family), Theorem G instances with other orthant-planar K₀, and RC63's instance.
   - Not reached by any composition:
     - targets whose bad interior extreme points are not all of the form ν(q\*⊙m) with m bad in an orthant-planar K₀ (N1);
     - targets violating N2;
     - every pari-mutuel model, since all its vertices are bad and so K = ν(q\*⊙K₀) would be orthant-planar, but its facets are not two-term (Lemma O1);
     - zero-support contaminations.
   - An exact characterisation of bad extreme points of L⋆K₀ (§4.7) is CONJECTURE.
   - The inverse problem (given K, find L and K₀) is OPEN.
4. **Lower-dimensional targets** stay outside every one-sided construction (P61 D1).
5. **Composition is closed.** Iterating it, or composing two orthant maps, adds nothing new (F2 and the closure lemma). New targets need a new mechanism: a second exempt point, or a non-VB inner ranking. O61 Thm A blocks the first within Brier-type error levels.

---

## 8. Status table

| Item | Status |
|---|---|
| Lemma O1: orthant-planar ⇒ cevian edges ⇒ two-term facets (any n) | PROVED |
| F1 normalisation, F2 associativity, F3 uniform visibility transfer | PROVED |
| Lemma A: G-cones of n = 3 orthant-planar polygons are root arcs that tile; exactly 3 bad vertices with distinct anti-visible worlds | PROVED; CHECKED (406 polygons) |
| Lemma B: a surviving bad vertex forces ν(L⊘π\*) ⊆ M_a | PROVED |
| Theorem N3: n = 3, interior factors ⇒ L⋆K₀ is VB-type (any L except a point) | PROVED; CHECKED (1 500 compositions) |
| Requested n = 3 factors (cyclic triangle, two hexagons): full hulls, 1 bad vertex each | CHECKED |
| RC63 ratio lemma and decoupling (n = 3) | CHECKED (0 mismatches) |
| RC63 boundary pentagon | CHECKED independently |
| RC63 n = 4 instance (31 / 61 / 32, 3 bad, 6 normals with no zero coordinate) | CHECKED independently |
| Lemma R: ratio patterns decouple, any n | PROVED; CHECKED (n = 3) |
| Lemma TP and Theorem G (sufficient condition, any n) | PROVED |
| Lemma NP: box factor transfers the facets of L | PROVED; CHECKED |
| **Theorem F (box family, n ≥ 4): covered, ≥ 2^{n−1} − n bad vertices, not orthant-planar** | **PROVED** (given the composition theorem) |
| Explicit n = 4 target: entire hull (32 / 63 / 33), 5 bad vertices, 21 non-two-term facets, 24 non-cevian edges | CHECKED |
| Pullback identity on that target (Q = L, L′, each v_j) | CHECKED (0 mismatches) |
| Family test, 25 cases; Theorem G exact on all | CHECKED |
| Two-pair rule necessary in general | FALSE (CHECKED counterexample) |
| Silhouette decoupling π_j(L⋆K₀) = π_j(L)⋆π_j(K₀) | PROVED |
| Exact recursive characterisation of bad points for n ≥ 4 | CONJECTURE |
| Lemma NC (necessary condition: cevian corners) | PROVED |
| Theorem BE (boundary exempt point, any n): covered, not VB-type, not orthant-planar | PROVED (given the composition theorem and RC63's exempt identity on ∂Δ) |
| Prop ZC: zero-support contaminations never composed | PROVED; key step CHECKED |
| Task (c): vertex-region lemma; two-cevian triangles never composed; one-cevian iff the angle criterion | PROVED; CHECKED |

---

## 9. Hypotheses and dependencies, for referees

- **"Covered" claims** (Theorems F and BE, the §4.6 target) depend on the composition theorem as refereed by RC63. Theorem BE also depends on its exempt-point step with π\* ∈ ∂Δ.
- **"Not VB-type"** depends on P61 Cor V6 (for interior K), or on the generator count of P61 Thm B and D3 (for boundary K).
- **"Not orthant-planar"** depends on Lemma O1 (proved here) or on R2's relint requirement.
- **Uniqueness, regularity and homogeneity** are not used as axioms anywhere. The orthant chart is a construction device.
