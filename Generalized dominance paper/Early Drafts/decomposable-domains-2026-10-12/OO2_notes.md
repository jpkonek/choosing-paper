# OO2 (round 43, BRIEF35). The positive side: an exact (QS) family through T1 along a curve, and the obstruction met in two dimensions

19 Oct 2026. Rules of BRIEF13 and BRIEF35. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named, with their recorded status.
- **CHECKED**: exact rational or exact symbolic computation, script named.
- **NUMERICS**: floating point; used only as illustration, never in a proof.
- **CONJECTURE**: none is stated.

Scripts are in `oo2py/`. Run `python3 -I <script>.py` from inside that folder.
- `curve_check.py` → `curve_check.out` (Fractions; ε ∈ {1/10, 3/10, 1/2}; ends `ALL CHECKS PASSED`);
- `planes_check.py` → `planes_check.out` (sympy, ε symbolic; ends `ALL CHECKS PASSED`);
- `ansatzA_search_numerics.py` (NUMERICS; illustration for §3 only).

Setting: write-up §2. Three worlds, μ standard Gaussian, the full four-advice domain (so (LF) at every model is automatic). T1 = D_{K₀}, K₀ = (1−ε)u + εΔ, c₀ = (1−ε)/3, v_k = c₀𝟙 + εe_k, P(g) := P_{T1}(g) = min_k v_k·g. Judges, switch values σ_iv, branches, (QS) and the uniqueness certificate are as in AUDIT_LL, MM1 §1 and NN2 §1. No assumption is added; every extra hypothesis belongs to the result that states it.

---

## 0. Outcome

**Criterion met for a one-parameter family; not met for a family with two-dimensional image.**

1. **The curve (Theorem 2.3, PROVED; CHECKED).** There is a single strictly guiding, integrable additive field σ = (σ₁, σ₂, σ₃) and a nonconstant family of ε-contamination models
   K(ρ) = (1−ρ)O + ρK₀, O = (−1, 0, 2), ρ ∈ J := [1−η, 1+η], η := c₀/(4(c₀+2)),
   such that, at the weight λ(ρ) := u + (ρ−1)(1, 0, −1), the model D_{K(ρ)} is the **unique** pointwise minimiser of λ(ρ)·σ, for every ρ ∈ J. The proof is a pointwise sign identity, not a sampling argument. Consequences (Corollary 2.4, PROVED):
   - with n identical copies of each world's judge, (QS) holds **for every quorum q ≤ n** (in particular 3-of-4 and 5-of-7) at every index p = λ(ρ) of the open segment S := {u + t(1,0,−1) : |t| < η}, against **every** measurable rival, with C_p := D_{K(1+t)};
   - composing with t(p) := (p₁ − p₃)/2 gives a family on an open disc around u in int Δ (a genuine parameter neighbourhood), continuous in measure, nonconstant, through T1 at u, with exact (QS) at every index. **Its image is the curve.** I do not claim more.
2. **What the curve shows.** It needs no quorum at all: one additive field suffices. So at the level of curves, hypothesis (B) need not fail and the sum relation need not have rank ≥ 3. The NN1/NN2 requirements are necessary for escaping collapse, and collapse is fatal only through global or two-dimensional arguments. The isolation of T1 found in MM1 Thm 4.2 / NN2 Cor 3.2 is a property of the min-cell class, not of T1.
3. **Two dimensions: not achieved.** I give the precise obstruction met by the natural exact design.
   - Certificate weights that are affine in the index force every chart {p : g ∈ C_p} to be straight (Proposition 3.1, PROVED).
   - The natural exact two-dimensional ansatz (translates (1−ε)p + εΔ, finitely many "atom" functions, weights affine in p, an exact proportional identity) reduces to a finite cone problem (Proposition 3.2, PROVED).
   - That cone problem is **impossible in every dimension ≥ 4, for every (n, q) with 2q > n**, by a covering argument on spheres of Lusternik–Schnirelmann type (Lemma 3.3, PROVED). In dimension 3 it collapses to a single field that fails at the crossing rays (Corollary 3.4, PROVED; plane computation CHECKED).
   - So any two-dimensional success must use at least one of the following:
     - (a) proportionality constants c_F(g) that vary with the gamble on the band of boundaries;
     - (b) weights that are not affine in the index (curved charts);
     - (c) degenerate branch representations, in which a nonzero functional vanishes on all used judges of a branch. This is the mechanism of the T1-only certificate (MM1 Part A) and of NN2's collapse.

   I did not find a design of type (a), (b) or (c). I have no proof that none exists.

**Single most important open point.** Is there a coherent family with **two-dimensional image** through T1 and exact (QS)? By §3, such a family must escape the exact finite-dimensional ansatz through (a), (b) or (c). Already for a single field, I do not know whether a local family with two-dimensional image exists. The global exclusions (write-up Thm main, FF2 Thm 4.1) use vertex neighbourhoods and edges, so they do not settle the local question.

---

## 1. Tools

**1.1 Sign form (MM1 Lemma 1.1(b) and the realisation lemma, MM1 §1.1; refereed correct in NN3 §1.1).**
- Let C = D_K with K ⊆ int Δ a credal set, and let a single nonnegative nonzero mixture of judges have switch value Σ(g). Suppose sgn Σ(g) = sgn P_K(g) for a.e. g, both orientations included. Then C is the a.e.-unique pointwise minimiser of the mixture, over all advices, × included.
- Every family of bounded measurable functions σ_i with sgn σ_i(g) = sgn g_i a.e. is the switch field of strictly guiding judges with Gaussian-integrable envelopes.
- A common positive factor m(g) applied to all switch values changes no sign. So it is enough to construct σ homogeneous of degree one with |σ(g)| ≤ M|g|₁, and then divide by |g|₁.

**1.2 From the certificate to (QS) (AUDIT_LL; MM2 Lemma 1.1).**
- Suppose, for every branch F at p, some nonnegative nonzero mixture of F's judges has C_p as unique minimiser over models (pointwise a.e., hence over models by decomposability and integrability).
- Then for X ≠ C_p that mixture has strictly larger loss at X, so some judge of F strictly prefers C_p. Hence no branch has all increments ≤ 0, which is (QS) by MM2 Lemma 1.1.

**1.3 Homothets (elementary; PROVED).** For a point O of the affine plane {Σm = 1}, ρ > 0, and K(ρ) := (1−ρ)O + ρK₀ ⊆ Δ:

  P_{K(ρ)}(g) = (1−ρ) O·g + ρ P(g) =: f_g(ρ),                                                   (1.1)

because m ↦ (1−ρ)O + ρm is an affine bijection K₀ → K(ρ) and ρ > 0. So for each g, f_g is affine in ρ. Each K(ρ) is a triangle homothetic to Δ, i.e. an ε′-contamination class with ε′ = ρε.

---

## 2. The curve

Fix ε ∈ (0, 1). Put

  O := (−1, 0, 2),  d := (1, 0, −1),  η := c₀/(4(c₀ + 2)),  J := [1−η, 1+η],
  K(ρ) := (1−ρ)O + ρK₀,  λ(ρ) := u + (ρ−1)d   (ρ ∈ J).

Since c₀ ≤ 1/3, we have η ≤ 1/28. In particular η < 1/9 and η < c₀/(c₀ + 2).

**Lemma 2.1 (PROVED; CHECKED Part (a)).**
- (a) For ρ ∈ J, K(ρ) ⊆ int Δ, and λ(ρ) ∈ int Δ with every coordinate in [1/3 − η, 1/3 + η].
- (b) ρ ↦ D_{K(ρ)} is injective and continuous in measure, and D_{K(1)} = T1.

*Proof.*
- (a) The vertices of K(ρ) are (1−ρ)O + ρv_k. Each coordinate is at least ρc₀ − 2|1−ρ| ≥ (1−η)c₀ − 2η > 0, since η < c₀/(c₀+2). The coordinates sum to 1. The claim on λ is immediate from d.
- (b) The vertices depend affinely and injectively on ρ, and K ↦ D_K is injective (write-up §2.1). Continuity in measure follows because K(ρ) is Hausdorff-continuous: P_{K(ρ)}(g) → P_{K(ρ₀)}(g) for every g, and ∂D_{K(ρ₀)} is null, so 1_{D_{K(ρ)}} → 1_{D_{K(ρ₀)}} a.e. Dominated convergence then gives μ(D_{K(ρ)} △ D_{K(ρ₀)}) → 0. ∎

**The field.**
- For g with all coordinates of one strict sign, put σ(g) := g.
- For mixed g, put D := P(g) − O·g and N := |g|₁, and choose a number s = s(g) as follows.

| pattern of (g₁, g₂, g₃) | admissible interval for s | s |
|---|---|---|
| (+, −, +) | (max(\|D\|/2, 3P/2), ∞) | max(\|D\|/2, 3P/2) + N |
| (−, +, −) | (−∞, min(−\|D\|/2, 3P/2)) | min(−\|D\|/2, 3P/2) − N |
| (+, +, −) | (−D/2, min(D/2, 3P/2)) | midpoint, if nonempty |
| (+, −, −) | (max(−D/2, 3P/2), D/2) | midpoint, if nonempty |
| (−, +, +) | (D/2, min(−D/2, 3P/2)) | midpoint, if nonempty |
| (−, −, +) | (max(D/2, 3P/2), −D/2) | midpoint, if nonempty |

- If the interval is nonempty (call g *exact*), put

  σ(g) := (s + D/2, 3P − 2s, s − D/2).                                                          (2.1)

- Otherwise (call g *dominant*; then P(g) ≠ 0 a.e.), let Σ₊ := Σ_{g_i>0} g_i and Σ₋ := Σ_{g_i<0} |g_i|, and put:
  - if P(g) > 0: σ_i := (1 + 2Σ₋/Σ₊)g_i where g_i > 0, and σ_i := g_i where g_i < 0;
  - if P(g) < 0: σ_i := g_i where g_i > 0, and σ_i := (1 + 2Σ₊/Σ₋)g_i where g_i < 0.

The field is measurable and homogeneous of degree one, with |σ(g)| ≤ 12|g|₁: every quantity used is bounded by 3|g|₁, and the dominant factors satisfy (1 + 2Σ₋/Σ₊)g_i ≤ g_i + 2Σ₋.

**Sign of the field.** σ_i has the strict sign of g_i whenever σ is defined by the table and (2.1).
- In the pure cases this is trivial.
- In the dominant case the signs are those of g by construction.
- In the exact case the interval in each row is exactly the solution set of the three strict sign conditions. For example, in row (+, +, −): s + D/2 > 0, 3P − 2s > 0, s − D/2 < 0.

**Identity on exact gambles.** By (2.1), σ₁ + σ₂ + σ₃ = 3P and σ₁ − σ₃ = D. Hence u·σ = P and d·σ = P − O·g, and for every ρ:

  λ(ρ)·σ(g) = P(g) + (ρ−1)(P(g) − O·g) = f_g(ρ) = P_{K(ρ)}(g).                                   (2.2)

**Lemma 2.2 (crossing gambles are exact; PROVED; CHECKED).** Let g be mixed, with f_g(ρ₀) = 0 for some ρ₀ ∈ J, and not both P(g) = 0 and O·g = 0 (that exceptional set is contained in finitely many rays, hence null). Then g is exact. Consequently, if g is dominant, f_g has no zero on J, and its sign on J is sgn P(g).

*Proof.*
1. **The values at a crossing.** From (1.1), ρ₀P = (ρ₀ − 1)O·g. Hence:
   - O·g ≠ 0;
   - |P| = |ρ₀ − 1||O·g|/ρ₀;
   - D = P − O·g = −O·g/ρ₀.

   So |D| = |O·g|/ρ₀ > 3|ρ₀ − 1||O·g|/ρ₀ = 3|P|, because |ρ₀ − 1| ≤ η < 1/3.
2. **Rows (+, −, +) and (−, +, −).** Their intervals are always nonempty.
3. **Rows with g₁ > 0 > g₃.** Here O·g = −g₁ + 2g₃ < 0, so D > 0.
   - For g₂ > 0 the interval is nonempty iff −D/2 < 3P/2, which follows from D > 3|P|.
   - For g₂ < 0 it is nonempty iff 3P/2 < D/2, which follows from the same inequality.
4. **Rows with g₁ < 0 < g₃.** Here O·g > 0, so D < 0, and |D| > 3|P| again gives nonempty intervals.
5. **The consequence.** If g is dominant, f_g has no zero on the closed interval J. It is affine, so its sign there is constant and equals sgn f_g(1) = sgn P(g). ∎

**Theorem 2.3 (PROVED; CHECKED).** For every ρ ∈ J, D_{K(ρ)} is the a.e.-unique pointwise minimiser of the mixture λ(ρ)·σ of the judges realising σ (MM1 §1.1), over all advices, contradictory advice included. All three weights are positive.

*Proof.* By §1.1 it suffices to show sgn λ(ρ)·σ(g) = sgn P_{K(ρ)}(g) for a.e. g.
- **Pure gambles.** If g > 0, both sides are positive, since λ(ρ) > 0 and K(ρ) ⊆ int Δ (Lemma 2.1). If g < 0, both sides are negative.
- **Exact gambles.** Equality holds by (2.2).
- **Dominant gambles with P(g) > 0.**
  - By Lemma 2.2, P_{K(ρ)}(g) = f_g(ρ) > 0.
  - Using λ_i(ρ) ∈ [1/3 − η, 1/3 + η]:
    λ(ρ)·σ ≥ (1/3 − η)(Σ₊ + 2Σ₋) − (1/3 + η)Σ₋ = (1/3 − η)Σ₊ + (1/3 − 3η)Σ₋ > 0.
- **Dominant gambles with P(g) < 0.** This case is symmetric.
- **The remaining set.** The gambles not covered are the coordinate planes, {P = 0}, and the null exceptional rays of Lemma 2.2. All of these are null. ∎

**Corollary 2.4 (exact (QS) along the curve and on a neighbourhood; PROVED).**
- **The judges.** At each world i take n copies ℓ_iv := ℓ_i (v = 1, …, n) of the judge realising σ_i, with any quorum q ≤ n. The case 3q > 2n is included, e.g. (4, 3) or (7, 5).
- **(a) Along the segment.** For p = u + t d with |t| < η, put C_p := D_{K(1+t)}. Then p ↦ C_p is coherent, continuous in measure, injective, and C_u = T1. (QS) holds at every such p against every measurable rival: every branch contains one copy of each ℓ_i, and the mixture with weights λ(1+t) = p on those copies has C_p as unique minimiser (Theorem 2.3, §1.2). Note that the certificate weight at the index p is p itself.
- **(b) On a neighbourhood.** On the open disc N := {p ∈ Δ : |p − u| < η} ⊆ int Δ, put t(p) := (p₁ − p₃)/2, so |t(p)| < η, and C_p := D_{K(1+t(p))}. Then:
  - p ↦ C_p is continuous in measure, nonconstant, and C_u = T1;
  - (QS) holds at every p ∈ N with all three worlds active, by (a), because (QS) at an interior index depends only on the selected model and supp p = {1, 2, 3}.
  - The image of N is the curve {D_{K(ρ)} : ρ ∈ (1−η, 1+η)}. ∎

*Remarks.*
1. **Why it works.** Along a line of weights, each gamble's acceptance set is the half-line {ρ : λ(ρ)·σ(g) > 0}. A homothetic pencil has exactly this property, by (1.1). The pencil is not nested: its members share the two boundary rays where O·g = P(g) = 0, which lie in opposite mixed orthants. On one arc of the boundary it grows with ρ, and on the other it shrinks.
   - The sign constraints (§2, table) allow growth exactly where O·g < 0, which here means g₁ > 0 > g₃. They allow shrinkage exactly where O·g > 0, which means g₁ < 0 < g₃.
   - The centre O = (−1, 0, 2) was chosen to make these two sets coincide with the arcs on which the pencil grows and shrinks.
   - A nested family is impossible for a single field: for some mixed pattern no switch vector with the right signs moves the boundary in the required direction. This is an elementary computation, not used.
2. **Consistency with the exclusions.**
   - The global single-field exclusions (write-up Thm main via edges and vertex neighbourhoods; FF2 Thm 4.1 via the covering step) need a selection on all of Δ, so they do not apply.
   - MM1 Thm 4.2 and NN2 Cor 3.2 concern judges cellwise linear on the min-cells. σ is not of that form: it contains P, which is non-linear on M_k ∩ M_j.
   - NN3 Prop A(b) does not apply either. At T1's corner rays, σ involves P = min(v_k·g, v_j·g), which is not analytic there, and no common-factor × analytic form holds.
   - NN1 Thm 4.1: hypothesis (B) holds trivially, since all judges of a world coincide, and its conclusion ("one field on N(C_p)") is literally true. Collapse to a single field is therefore not, by itself, a local obstruction.
3. **Heterogeneity.** The criterion asks for fixed judges, not for pairwise non-proportional ones; copies are allowed by BRIEF35. Making the judges pairwise non-proportional while keeping this certificate is easy off the boundaries (NN1 §5 Remark). I do not pursue it, because it would be invisible on the boundaries and add nothing.

*Checks (`curve_check.out`; ε ∈ {1/10, 3/10, 1/2}).*
- **Sampling.** About 5 900 exact samples per ε. Half are uniform; half are placed on or within 10⁻² to 10⁻⁶ of ∂D_{K(ρ₀)} for random ρ₀ ∈ J.
- **What is verified.**
  - the parameter facts of Lemma 2.1(a);
  - the strict sign pattern of σ;
  - the identities u·σ = P and d·σ = P − O·g on exact gambles;
  - Lemma 2.2 on every dominant sample;
  - sgn λ(ρ)·σ(g) = sgn P_{K(ρ)}(g) at seven values of ρ ∈ J, with P_{K(ρ)} computed directly from the vertices of K(ρ), and equality (2.2) on exact gambles.

---

## 3. Two dimensions: the obstruction met

Here the target is a family with two-dimensional image. The natural candidate is the translate family

  C_p := D_{(1−ε)p + εΔ},  P_{K_p}(g) = (1−ε)p·g + ε min_i g_i = x(g)·p  (Σp = 1),

where x(g) := (1−ε)g + ε(min_i g_i)𝟙. It is injective and continuous on int Δ, with C_u = T1.

**Proposition 3.1 (affine weights force straight charts; PROVED).** Let Q ⊆ int Δ be open and p ↦ C_p = D_{K_p} a family on Q. Suppose a branch F has weights α_{F,iv}(p) = ℓ_{F,iv}·p (ℓ ∈ ℝ³), nonnegative and not all zero on Q, which certify C_p in the sign form of §1.1 for every p ∈ Q. Then:
- for a.e. g, the chart {p ∈ Q : g ∈ C_p} agrees, up to a null set of p, with Q ∩ {p : p·y(g) > 0}, where y(g) := Σ_F σ_iv(g)ℓ_{F,iv};
- if g lies on ∂C_p for some p ∈ Q and y(g) ≠ 0, then y(g) is a positive multiple of the normal of the zero line of p ↦ P_{K_p}(g) in Q.

*Proof.* The mixture at p is p·y(g). Apply Fubini on Q × ℝ³ to the set where sgn p·y(g) ≠ sgn P_{K_p}(g). ∎

For the translate family the chart of g is the half-plane {x(g)·p > 0}. So certification of a crossing gamble g by affine weights requires

  Σ_{(i,v)∈F} σ_iv(g) ℓ_{F,iv} = c_F(g) x(g),  c_F(g) > 0,  for every branch F.                    (3.1)

**The exact finite-dimensional ansatz (A).**
- Let G be a non-null set of mixed gambles that contains an open neighbourhood of every crossing ray of ∂T1 (MM1 §5: on F_k the coordinates i, j cross).
- **(A1)** On G, σ_iv(g) = J_iv·z(g) for fixed J_iv ∈ ℝ^d, with atoms z = (z₁, …, z_d) linearly independent as functions on G.
- **(A2)** The weights are affine, α_{F,iv}(p) = ℓ_{F,iv}·p ≥ 0 on an open Q ∋ u, and (3.1) holds on G with c_F **constant**, for every p ∈ Q.
- **(A3)** (Non-degeneracy.) For every branch F, the vectors J_iv of the judges of F with ℓ_{F,iv} ≠ 0 span V := span{J_iv : all i, v}.

**Proposition 3.2 (reduction; PROVED).** Under (A1)–(A2):
- the coordinates x₁, x₂, x₃ lie in span(z) on G: x = X z for a 3 × d matrix X of rank 3;
- Σ_F ℓ_{F,iv} J_iv^T = c_F X for every F;
- with w_{F,iv} := ℓ_{F,iv}·u, and with ξ := X^T u the atom representation of P = u·x, one has ξ = c_F^{−1} Σ_F w_iv J_iv, where w_iv > 0 exactly when ℓ_{F,iv} ≠ 0.

Conversely, in the case d = 6 with z = (g₁, g₂, g₃, min g, F₁, F₂), suppose:
- every 6 × 6 branch matrix J_F is invertible and ξ ∈ int cone{J_F};
- for every mixed sign pattern s, the vectors s_i·(J_iv)_{5,6} lie in an open half-plane.

Then the ansatz can be completed (choose F(g) := T|g|F*_{s(g)} with T large and F*_s in that half-plane) and gives exact (QS) on a neighbourhood of u with **two-dimensional image**. Lemma 3.3 shows that the hypothesis of this converse is never met.

*Proof.*
1. **Linear in p.** Both sides of (3.1), paired with p, are linear in p ∈ ℝ³ and agree on the open set Q of the plane Σp = 1. So the vector identity Σ_F (J_iv·z)ℓ_iv = c_F x holds on G.
2. **The matrix identity.** The left side lies in span(z), hence so does x. Independence of the atoms gives Σ ℓ J^T = c_F X. Applying u gives the identity for ξ.
3. **Positivity of the weights.** Since ℓ·p ≥ 0 on Q ∋ u, either ℓ·u > 0, or ℓ·(p−u) ≥ 0 for all small p − u ∈ 𝟙^⊥. In the second case ℓ ∈ ℝ𝟙 and ℓ·u = 0, so ℓ = 0.
4. **The converse.** By invertibility, L_F := J_F^{−T}X has rows ℓ_{F,iv} with ℓ·u > 0, hence ℓ·p > 0 on a small disc. Then Σ_F (ℓ·p)σ_iv = x(g)·p = P_{K_p}(g) on mixed gambles. Pure gambles are handled by σ = g. §1.1 applies. ∎

**Lemma 3.3 (three antipodal-free sets; PROVED).** Let V be a real vector space of dimension d and ξ ∈ V. For each world i ∈ {1, 2, 3} let J_i1, …, J_in ∈ V. Let 2q > n and b := n − q + 1. Suppose that for every choice F of b judges at each world there are F′ ⊆ F and weights w > 0 on F′ with
- ξ = Σ_{F′} w_iv J_iv, and
- span{J_iv : (i,v) ∈ F′} = V.

Then d ≤ 3.

*Proof.*
1. **The sphere.** Suppose d ≥ 4. Let A := {φ ∈ V* : φ(ξ) = 0}, of dimension at least d − 1 ≥ 3, and let S be its unit sphere (any norm). S is a sphere of dimension m ≥ 2.
2. **Some world has q negative judges.** Let φ ∈ S. Suppose every world had at least b judges with φ(J_iv) ≥ 0, and let F consist of such judges. With F′ and w as in the hypothesis, 0 = φ(ξ) = Σ_{F′} w φ(J), a sum of nonnegative terms. So φ vanishes on J_{F′}, which spans V, hence φ = 0, which is a contradiction. So some world has at least n − b + 1 = q judges with φ(J_iv) < 0.
3. **The sets.** Put N_i := {φ ∈ S : at least q of φ(J_i1), …, φ(J_in) are < 0}. These are three relatively open sets covering S. Since 2q > n, no N_i contains a pair φ, −φ.
4. **The contradiction.** By the Lusternik–Schnirelmann–Borsuk theorem, a cover of S^m by m + 1 open sets has a member containing a pair of antipodal points. Here m + 1 ≥ 3, which contradicts step 3. ∎

*Remarks.*
- **Dimensions 1 to 3 do occur.** NN1 Example 5.1 is the case d = 2, ξ = 0: three sectors cover the circle.
- **Committee size does not matter.** The bound is independent of (n, q) as long as 2q > n. With r worlds the same proof gives d ≤ r.
- **Degenerate certificates escape the hypothesis.** The T1-only certificate (MM1 Part A, NN2 Remark 3.5) has doubled or tripled judges: a functional can vanish on a whole branch. This is exactly what the spanning hypothesis forbids.

**Corollary 3.4 (the exact ansatz is impossible; PROVED; plane computation CHECKED).** No design satisfies (A1)–(A3) for the translate family, for any (n, q) with 2q > n and any number d of atoms.

*Proof.*
1. **Dimension.** By Proposition 3.2 and Lemma 3.3 (with ξ = X^T u and F′ the judges with ℓ ≠ 0), dim V ≤ 3.
2. **V is the row space of X.** The rows of X are combinations of the J_iv, by Proposition 3.2, and they are independent: on an open piece of a min-cell, x is an invertible linear image of g. So V = rowspace(X), J_iv = X^T a_iv, and σ_iv = a_iv·x(g) on G.
3. **Vanishing at the crossings.** Fix i and a crossing ray of coordinate i on facet k. Near it, G contains an open set in which x(g) = (1−ε)g + εg_k𝟙 is linear and continuous, and σ_iv must change sign across {g_i = 0}. So a_iv·x vanishes on the plane piece {g_i = 0} there. That is, a_iv is orthogonal to the plane spanned by x(e_k) = (1−ε)e_k + ε𝟙 and x(e_l) = (1−ε)e_l.
4. **The two planes differ.** The other crossing of coordinate i lies on facet l and gives the plane spanned by (1−ε)e_l + ε𝟙 and e_k. The two planes are span{e_l, e_k + εe_i} and span{e_k, e_l + εe_i}. They differ for ε > 0 (`planes_check.out`, symbolic in ε). So a_iv = 0, contradicting σ_iv ≠ 0 a.e. ∎

*Illustration (NUMERICS, not used).* `ansatzA_search_numerics.py` hill-climbed 40 random d = 6 configurations whose last two coordinates satisfy the half-plane condition of Proposition 3.2. The best worst-branch normalised weight was −0.175 (seed 1). This is what Lemma 3.3 predicts.

**What escapes, precisely.** Corollary 3.4 uses three things: constant c_F in (3.1), affine weights, and spanning used branches. Accordingly a two-dimensional construction must do at least one of the following.
- **(a) Vary c_F(g) on the band of crossing gambles.** Equivalently, the branch identity holds only projectively.
  - Encode c_F(g) = c_F⁰ + Σ_{m≤M} c_F^m h_m(g) by the atoms x_j and h_m x_j. Then d = 3(M+1), and the admissible targets fill a cone in a subspace W of dimension k = M + 1.
  - The proof of Lemma 3.3, run with A := W^⊥ in place of ξ^⊥, gives d − k ≤ 2 under the spanning hypothesis (PROVED by that proof verbatim).
  - Here d − k = 2(M+1). So M ≥ 1 is excluded, and M = 0 is Corollary 3.4.
  - So (a) needs c_F(g) outside every such finite encoding, or degenerate branches.
- **(b) Use weights not affine in the index.** Then charts may be curved (Proposition 3.1 fails). This is needed, for instance, for the plain posterior family, whose charts near corner rays are wedges.
- **(c) Use degenerate branches** (a functional vanishing on all used judges of a branch). This is the doubled-ray mechanism. Where it is of intersection form, NN2 Thm 2.3 collapses the branch structure to a single field on the boundary. Whether a single field admits a local family with two-dimensional image through T1 is open (§0).

---

## 4. Status table

| Item | Statement | Label |
|---|---|---|
| 1.3 | support function of homothets, (1.1) | PROVED |
| 2.1 | K(ρ) ⊆ int Δ, λ(ρ) ∈ int Δ; injective, continuous in measure, through T1 | PROVED; CHECKED (a) |
| 2.2 | crossing gambles are exact; dominant gambles have constant sign on J | PROVED; CHECKED |
| 2.3 | D_{K(ρ)} is the unique minimiser of λ(ρ)·σ for every ρ ∈ J | PROVED; CHECKED (sign identity on ~17 800 exact samples) |
| 2.4 | exact (QS), any (n, q) (copies), along the segment and on an open disc around u; image one-dimensional | PROVED |
| 2 Rem. 2 | consistency with MM1 4.2, NN2 3.2, NN3 A(b), NN1 4.1 | PROVED (by inspection of hypotheses) |
| 3.1 | affine weights ⇒ straight charts | PROVED |
| 3.2 | exact ansatz ⇔ finite cone problem (and the converse construction) | PROVED |
| 3.3 | spanning branch cones containing ξ ⇒ dim ≤ 3, any 2q > n | PROVED (via the Lusternik–Schnirelmann–Borsuk theorem) |
| 3.4 | exact finite-atom ansatz for translates impossible | PROVED; CHECKED (planes) |
| 3 illus. | random d = 6 search fails | NUMERICS (not used) |
| — | exact (QS) family through T1 with two-dimensional image | **open** |

**Imports.** MM1 Lemma 1.1 and the realisation lemma (refereed correct, NN3 §1.1); MM2 Lemma 1.1 (branch form; refereed, NN3 §2.1); write-up §2.1 (injectivity of K ↦ D_K). Nothing from FF2, edges or the lifting lemma is used. The lifting lemma (AUDIT_LL) applied to the family of Corollary 2.4 would give a closed-section quorum rule on the segment. It is not invoked, because its stated form needs a selection on the whole simplex.
