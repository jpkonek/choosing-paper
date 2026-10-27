# Y1. The interior subsystem for the posterior family: an obstruction for lexicographic-additive orders, and the exact residual

16 Oct 2026 (round 27, BRIEF19, Milestone 1). Labels: **PROVED** (proof here, not refereed), **CHECKED** (exact rational computation, reproducible), **CONJECTURE**, **NUMERICS**. Scripts are in `y1py/`; run them with `python3 -I y1py/<script>`; outputs are in the matching `.out` files.

Read: BRIEF19, AUDIT_X123 (with the interior-locality lemma), BRIEF18, AUDIT_nonlinear_programme, X1, X2, X3, write-up §§2–4. Nothing is assumed beyond the write-up's §2 axioms. "Model" means a measurable model on the full four-advice domain.

---

## 0. Outcome

**No genuine interior subsystem was constructed.** What I found instead is a **proved obstruction** for the posterior selection, valid for a broad class of world orders that contains every construction tried so far. I also isolate the exact residual problem.

1. **Monotone rays (Lemma Y1.1, PROVED).** Write q = ν(p ⊙ (s e_i + e_j + e_l)) with s > 1, i.e. move p toward e_i, keeping p_j : p_l.
   - C_q is then pointwise weakly better than C_p at world i, and strictly better on a non-null set.
   - Conversely, C_q is pointwise weakly i-better than C_p **only** for q of this form.

   *Consequences.* Distinct posterior models can never be tied at every world, which rules out the "tie plateau" escape. Every section {q : C_q ⪯_i X} is star-shaped toward e_i.

2. **Closedness along improving rays (Lemma Y1.2, PROVED, for all orders).** Suppose C_{q_t} ⪯_i X along such a ray q_t → p. Then C_p ⪯_i X.

3. **The balanced field does everything except (C) (Prop. Y1.3, PROVED).** There is a strictly guiding additive ranking, with a finite measure and "balanced" world penalties, that has the following properties.
   - It satisfies strict (G), (IB), transitivity, competitiveness on Ω, undominatedness, and closed sections, on all of Δ°. This holds for **every** coherent selection that is continuous in measure, the posterior family included.
   - Its only failure is (Csel): incoherent models tie the selected ones at every world.

   So for the posterior family the interior problem is **exactly a tie-breaking problem**.

4. **Main obstruction (Theorem Y1.4, PROVED; geometric input CHECKED).** Let N₀ be any nonempty open subset of Δ°, and take the posterior selection on N₀. No ranking in the class 𝓛 (defined below) has both of these properties:
   - every section {p ∈ N₀ : C_p ⪯_i X} is closed in N₀;
   - no incoherent model ties a selected one at every world.

   The class 𝓛 consists of world orders that are lexicographic towers whose level 0 is a single strictly guiding additive functional, and whose later levels are additive functionals, or unanimity over families of additive functionals, with bounded penalties.

   The proof uses neither competitiveness nor protection. 𝓛 contains:
   - all additive rankings;
   - Brier-type rankings with any additive or credal tie-break;
   - the balanced lexicographic rules of X2.7, transplanted to a finite measure.

   The mechanism has three steps:
   - **(a)** By Lemmas Y1.1 and Y1.2, closedness forces every C_p to be world-i-minimal in its level-0 level set.
   - **(b)** By Lyapunov and Lagrange, together with a Topkis argument (the only pointwise-comparable pairs lie on the monotone rays), every lexicographic level is minimised by **all** C_q (q ∈ N₀) simultaneously. So each world's tie class of C_p contains the "box" of all pointwise mixtures of selected models that have C_p's level-0 values.
   - **(c)** Lyapunov again. Either an incoherent box model ties C_p at every world, or each C_p is the unique lexicographic Bayes choice of a linear functional on ℝ³ inside the box. The second option is impossible, because the posterior's advice regions (half-planes and *wedges*, from the attribution max) shatter four points of N₀. Homogeneous half-spaces of ℝ³ cannot shatter four points. The shattering is checked exactly for ε ∈ {0.1, 0.3, 0.6, 0.9} at three scales (`shatter.out`).

5. **Answer to the brief's question.** I do **not** claim that the posterior selection cannot work under arbitrary orders. In 𝓛 it cannot, by Y1.4. This is a precise statement of what the audit suspected about X2: the nonlocal comparisons between nearby selected models cannot be ordered by any lexicographic or credal additive rule without either an incoherent all-world tie or an open section.

6. **Nearby reachable targets** (the project preference; §6):
   - **(i) Leave 𝓛 at level 0.** By Y1.2, any order must still satisfy the ray-closure property. The precise residual question Q_Y1 is stated in §6.
   - **(ii) Change the selection.** Step (a) uses monotone rays. The contamination family K_p = (1−ε)p + εΔ also passes through T1 at u, and it has **no** pointwise-comparable pairs near u (PROVED to first order; NUMERICS for finite pairs, in `contam_check.out`). So it escapes step (a) entirely, and its advice regions are half-planes, so it also escapes step (c).
   - The contamination family is therefore the natural selection for a second attempt at Milestone 1 within 𝓛. I did not complete a construction for it.

---

## 1. The interior problem

Fix ε ∈ (0,1). Put c₀ = (1−ε)/3 and λ = ε/c₀. The posterior family is K_p = ν(p ⊙ T1) and C_p = D_{K_p} (X2.5). For a mixed pair with majority orientation h, write o for the odd world (h_o < 0 < h_j, h_l). By X2.6:

- C_p is at **M** iff m_h(p) := p·h + λ p_o h_o > 0;
- C_p is at **O** iff f_{h,j}(p) < 0 and f_{h,l}(p) < 0, where f_{h,k}(p) := p·h + λ p_k h_k;
- C_p is at **S** otherwise.

So for fixed h:
- the M-region {p : C_p(h) = M} is an open half-plane;
- the O-region is the open convex wedge W_h = {f_{h,j} < 0} ∩ {f_{h,l} < 0}. Its two boundary lines are distinct (since λ > 0) and meet on the kink line {p_j h_j = p_l h_l} through e_o.

**(S_N), the requirements of Milestone 1.** N ⊆ Δ° is a closed neighbourhood of u, and N₀ := int N. World preorders ⪯_i on all models must satisfy:
- strict (G), (IB) and transitivity;
- for every p ∈ N and every model X:
  - competitiveness on Ω;
  - no model dominates C_p;
  - (Csel): no incoherent X ties C_p at every world;
- {p ∈ N : C_p ⪯_i X} is closed in N.

---

## 2. Monotone rays

**Lemma Y1.1 (PROVED; NUMERICS in `mono_check.out`).** Let p ∈ Δ°, i ∈ Ω, and q = ν(p ⊙ d) with d ∈ ℝ³_{>0}. Let {j, l} = Ω ∖ {i}.

- (a) If d_j = d_l < d_i, then C_q is pointwise weakly better than C_p at world i a.e., and strictly better on a non-null set.
- (b) If d_j ≠ d_l, there is a non-null set of pairs on which C_q is strictly worse than C_p at world i.
- (c) If d_j = d_l > d_i, then C_q is pointwise weakly worse at world i.

*Proof.* All conditions are homogeneous of degree 1 in p, so normalisation is irrelevant. Write η = log d.

- (a) The condition for M at q is m_h(p ⊙ d) = Σ_m p_m d_m k_m, with k = h + λ h_o e_o.
  - On Q_o with o ≠ i, the coefficient of d_i is p_i k_i > 0 and the other coefficients are unchanged. Increasing d_i can only create M (S→M or O→M). M is i-good there, since i is a majority world.
  - On Q_i the coefficient p_i k_i is negative, so M can only disappear. M is i-bad there, since i is odd.
  - The same computation applies to f_{h,j} and f_{h,l}. On Q_o with o ≠ i they increase, so O can only disappear (O is i-bad). On Q_i they decrease, so O can only appear (O is i-good).
  - Unanimous pairs are unaffected.
  - Distinct posterior models differ on a non-null set (AUDIT_X123 lemma), so the improvement is strict somewhere.
- (b) Say d_j < d_l, and normalise d_l = 1. Take h ∈ Q_l, where i and j are majority worlds and l is odd. With h_i small, the M-condition at p is approximately p_j k_j + p_l k_l > 0, and at q it is approximately p_j d_j k_j + p_l k_l > 0.
  - Choose k_l < 0 with −p_j k_j < p_l k_l < −p_j d_j k_j.
  - This is an open set of h: C_p is at M and C_q is not.
  - M is good for the majority world i, so C_q is i-worse there.
- (c) The reverse of (a). ∎

**Corollary Y1.1′ (PROVED).** In any ranking with strict (G):
- (i) no two distinct C_p, C_q (p, q ∈ Δ°) are tied at every world;
- (ii) if C_q ⪯_i X and p lies on the segment from q to e_i, then C_p ⪯_i X. Indeed C_p ⪯_i C_q by (a) and weak (G), and then transitivity applies. So sections are star-shaped toward e_i.

(i) rules out making all selected models of N one all-world tie class. That plateau would have made sections trivially closed. By X3.1, plateaus of *distinct* models are therefore unavailable for the posterior.

---

## 3. Closedness along improving rays; the balanced field

**Lemma Y1.2 (PROVED; any preorders).** Suppose sections are closed in N. Let p ∈ N₀ and q_t := ν(p ⊙ (1+t, 1, 1)) for world i = 1, and similarly for other worlds. If C_{q_t} ⪯_i X for all small t > 0, then C_p ⪯_i X.

*Proof.* q_t → p, the points q_t lie in the section, and the section is closed. ∎

**Proposition Y1.3 (the balanced field; PROVED).** Let μ be Gaussian, and fix any bounded measurable weight w(h) > 0. Define penalties ψ_i(h, a) as follows.

- **Unanimous pairs**, at every world: correct 0, S 1, wrong 2, × 3.
- **Pairs of Q_o:**

| advice | majority world i ≠ o | odd world o |
|---|---|---|
| M | 0 | 0 |
| S | w | −2w |
| O | 2w | −4w |
| × | 3w | w |

Put ψ_i(X) := ∫ ψ_i(h, a_X(h)) dμ and X ⪯_i Y :⟺ ψ_i(X) ≤ ψ_i(Y). Let p ↦ C_p be any coherent selection on Δ° that is continuous in measure; the posterior family is one. Then:

1. strict (G), (IB) and transitivity hold, and so do competitiveness on Ω, undominatedness of every C_p, and closed sections, on all of Δ°;
2. (Csel) fails at every p.

*Proof.*
- **Guidance.** The penalties are strictly increasing in each world's rank (X2.1).
- **Balance.** Σ_i ψ_i(h, a) = 0 for a ∈ {M, S, O} on mixed pairs. It is > 0 for ×, and for non-correct advice on unanimous pairs. Hence Σ_i ψ_i(X) ≥ Σ_i ψ_i(C) for every regular C, with equality iff X is regular.
- **Competitiveness.** Some i has ψ_i(X) ≥ ψ_i(C_p).
- **Undominatedness.** If ψ(X) ≤ ψ(C_p) componentwise, then the sums force equality, so the inequality is not strict.
- **Closed sections.** p ↦ ψ_i(C_p) is continuous, so {p : ψ_i(C_p) ≤ ψ_i(X)} is closed.
- **(Csel) fails.**
  - Take a small ball F of pairs strictly inside the accepted cone of C_p. Removing it creates a hole, so the resulting model is incoherent, by the cone-hull argument of Y1.4 step (d) below.
  - C_p is silent on non-null parts of each Q_o (its band). The S→M moves there have Δψ-directions proportional to (2,−1,−1), (−1,2,−1) and (−1,−1,2). These positively span the plane Σ = 0.
  - Lyapunov's theorem, as in Y1.4 step (d), compensates the hole's ψ-change away from F. The result is an incoherent X with ψ(X) = ψ(C_p), which is a tie at every world. ∎

So every axiom of (S_N) other than (Csel) is met by a single field, for the posterior family itself, with nonlocal comparisons included. **The interior milestone for the posterior is precisely: break the incoherent all-world ties without losing closed sections.** Theorem Y1.4 shows that lexicographic or credal additive tie-breaking cannot do this.

---

## 4. The obstruction theorem

**The class 𝓛.** A world order ⪯_i belongs to 𝓛 if it is a lexicographic tower (𝔩⁰, 𝔩¹, 𝔩², …) indexed by an ordinal, where:
- 𝔩⁰ is one additive functional ψ_i(X) = ∫ ψ_i(h, a_X) dμ, strictly guiding, with bounded penalties and finite μ;
- each 𝔩^α (α ≥ 1) is unanimity over a family Φ^α_i of additive functionals with bounded penalties. A single functional is a special case. No guidance is required at levels α ≥ 1.

The comparison X ⪯_i Y holds iff one of the following holds:
- ψ_i(X) < ψ_i(Y);
- or the first level α at which X and Y are not tied has X strictly below Y in the unanimity preorder at α;
- or X and Y are tied at every level.

(IB), transitivity and strict (G) hold automatically, the last because of 𝔩⁰. The three worlds may use different towers.

**Theorem Y1.4 (PROVED).** Let N₀ ⊆ Δ° be nonempty and open, and take the posterior selection. No ranking whose three world orders lie in 𝓛 satisfies both:
- {p ∈ N₀ : C_p ⪯_i X} is closed in N₀ for every i and every X;
- no incoherent X ties any C_p (p ∈ N₀) at every world.

Neither competitiveness nor protection is used. Hence Milestone 1 with the posterior selection has no solution in 𝓛, for any N.

*Proof.* Fix a world i. Write ψ = ψ_i, and c_p := ψ(C_p).

**(a) Level-set minimality.** Let X satisfy ψ(X) = c_p, with p ∈ N₀.
- By Y1.1(a), ψ(C_{q_t}) < c_p for q_t on the monotone ray toward e_i.
- So C_{q_t} ≺_i X, already at level 0.
- By Y1.2, C_p ⪯_i X.

Hence **C_p ⪯_i X for every X in the level set Λ(p) := {ψ = c_p}.** In the tower this means that C_p is minimal for every functional of level 1 on Λ(p), then for every functional of level 2 on the level-1 tie set, and so on.

**(b) Every level is minimised by all selected models at once.** By induction on α, I show the following.
- There is a measurable box A^α(h) ⊆ {+, 0, −, ×}, independent of p, containing B(h) := {C_q(h) : q ∈ N₀}.
- The level-<α+1 tie set of C_p inside Λ(p) is T^α(p) = {X : X(h) ∈ A^α(h) a.e., ψ(X) = c_p}.

Start with A⁰ ≡ all advice and T⁰(p) = Λ(p).

*Step.* Let χ ∈ Φ^{α+1}. By (a), C_p minimises χ on T^α(p).
- **Lyapunov.** The set {(ψ(X), χ(X)) : X(h) ∈ A^α(h)} is convex and compact.
- **c_p is interior to the ψ-range.** The box contains C_q for q on the e_i-ray through p, on both sides of p (p ∈ N₀ is interior), and ψ(C_q) lies strictly on both sides of c_p (Y1.1(a), (c)).
- **Lagrange.** So there is a finite subgradient κ = κ_χ(p) ∈ ℝ such that C_p minimises χ + κψ over box models. This minimisation is pointwise: C_p(h) ∈ argmin_{a ∈ A^α(h)} (χ + κψ)(h, a) a.e.
- **Topkis.** Suppose κ_χ(p) < κ_χ(q). Adding the two minimality inequalities gives ψ(h, C_q(h)) ≤ ψ(h, C_p(h)) a.e. So C_q is pointwise weakly i-better than C_p, and by Y1.1(b) q lies on the e_i-ray beyond p.
  - Hence κ_χ(p) = κ_χ(q) whenever p and q are not on a common e_i-line.
  - If p and q are on a common e_i-line, compare both with some r off that line.
  - So κ_χ ≡ τ_χ is constant on N₀.
- **New box.** Put A^{α+1}(h) := ⋂_{χ ∈ Φ^{α+1}} argmin_{A^α(h)} (χ + τ_χ ψ)(h, ·). Every C_q (q ∈ N₀) lies in it, so B ⊆ A^{α+1}.
- **New tie set.** For X ∈ T^α(p), each of the following is equivalent to the next:
  - χ(X) = χ(C_p);
  - (χ + τ_χψ)(X) = min;
  - X is a pointwise minimiser.

  This gives the form of T^{α+1}(p).
- **Limit stages.** Intersect. A strictly decreasing chain of boxes strictly decreases ∑_a μ{h : a ∈ A(h)}, so it stabilises at a countable ordinal.

**(c) Ties.** Let 𝔅 := {X : X(h) ∈ B(h) a.e.}. Every X ∈ 𝔅 with ψ_i(X) = ψ_i(C_p) is tied with C_p at world i at every level. Since 𝔅 does not depend on the world, X ∈ 𝔅 is tied with C_p at **every world** iff Ψ(X) = Ψ(C_p), where Ψ := (ψ_1, ψ_2, ψ_3) collects the three level-0 functionals.

**(d) Dichotomy.** Let Y := Ψ(𝔅) ⊆ ℝ³. It is convex and compact (Lyapunov). Put y := Ψ(C_p).
- **Face recursion.** Starting from F₀ := Y:
  - if y ∉ ri F_k, choose a supporting functional c_{k+1} exposing a proper face F_{k+1} ∋ y;
  - the models with values in F_{k+1} are the pointwise c_{k+1}·Ψ-minimisers within the box 𝔅_k, forming a box 𝔅_{k+1} with Ψ(𝔅_{k+1}) = F_{k+1};
  - after k ≤ 3 steps, y ∈ ri Ψ(𝔅_k), and C_p ∈ 𝔅_k.
- **(T)** Suppose 𝔅_k(h) has at least two elements on a non-null set G. Then there is an incoherent X ∈ 𝔅_k with Ψ(X) = y.
  - Take a density point h₀ ∈ G off ∂C_p (it exists, since ∂C_p is null). Take a small ball U ∋ h₀ inside the region where C_p's advice is constant, and a much smaller concentric ball F ⊆ U, with F ∩ G non-null. Flip C_p on F ∩ G to another box value; this is a hole or a bump in a convex cone.
  - Let w be the resulting change in Ψ. Then w ∈ V := aff Ψ(𝔅_k) − y and |w| ≤ C μ(F).
  - Since y ∈ ri, there are box models Z_1, …, Z_r whose values Ψ(Z_j) − y positively span V. Their restrictions to U^c still positively span V when μ(U) is small.
  - Lyapunov's theorem for the joint vector measure partitions U^c into r pieces carrying equal shares of every Z_j-record.
  - Applying a fraction of the Z_j-record on the j-th piece yields X ∈ 𝔅_k with Ψ(X) = y and X = C_p on U ∖ F.
  - X is incoherent. If X = D_K a.e., then, D_K being a convex cone, the rays through F ∩ G meet U ∖ F on both sides. This forces X's advice on F ∩ G to equal C_p's, a contradiction.
  - By (c), X ties C_p at every world, which violates (Csel).
- **(U)** Otherwise 𝔅_k(h) = {C_p(h)} a.e. Then C_p(h) is the unique lexicographic minimiser over B(h) of ℓ_p := (c_1·Ψ, …, c_k·Ψ), for a.e. h.

**(e) (U) cannot hold for all p ∈ N₀.** Take pairs h with B(h) = {b, b′} (two elements). For these, C_p(h) = b iff ℓ_p(α_h) <_lex 0, where α_h := Ψ(h, b) − Ψ(h, b′) ∈ ℝ³, and the lexicographic sign is non-zero by uniqueness.
- By Lemma Y1.5 there are four points p_1, …, p_4 ∈ N₀ and, for each of the 16 labellings, a non-null open set of such pairs h realising it.
- Choose one h per labelling outside the four exceptional null sets.
- Replace each lexicographic functional ℓ_{p_k} by the vector c̃_k = c_1 + δc_2 + δ²c_3 with δ small. This preserves the 16 non-zero signs.
- So the four vectors c̃_k ∈ ℝ³ are shattered by homogeneous half-spaces {c : c·α > 0}, which have VC dimension 3. Contradiction.

So (T) occurs at some p, contradicting the no-tie hypothesis. ∎

**Lemma Y1.5 (four-point shattering; PROVED, CHECKED exactly).** For every disc around u (so inside every N₀ ∋ u, and by translating the apex, around every point of Δ°), there are four points robustly shattered by the posterior advice sets {q : C_q(h) = b}. Only pairs h with two-element box over an open square N₀ are used.

*Proof.* The configuration has d inside triangle abc.
- Half-planes realise every labelling except {d} versus {a, b, c}. Every line through N₀ is the M/S boundary of a pair h ∈ Q_o for the o at which the line's normal has its single negative entry: h_o = k_o/(1+λ), and the other h_m = k_m. Near such a line the O-conditions are far from active, since p·h = −λ p_o h_o > 0 there, so the box is {M, S}.
- {d} is realised by the wedge W_{h*} with h* = (−(2+λ), 1, 1), apex u:
  - d is just inside, on the bisector;
  - a and b are just outside each boundary ray, at distance R;
  - c is on the opposite side.
  - d ∈ triangle abc once the offsets are ≪ Rδ, where δ > 0 is the angle between the two boundary lines.
  - On N₀ the M-condition for h* is negative, so the box is {S, O}.
- All conditions are strict, hence open in h, and they are invariant under homothety about the apex.
- `shatter.py` verifies everything in exact rationals for ε ∈ {1/10, 3/10, 3/5, 9/10} and R ∈ {10⁻², 10⁻⁴, 10⁻⁷}: all 16 labellings, the two-element boxes at the vertices of N₀, and d ∈ abc. ∎

**Remarks.**
1. **What each hypothesis does.**
   - Monotone rays give (a) and the Topkis step.
   - Wedges, which come from the attribution max of X2.6, give (e).
   - Lyapunov, through finite μ and bounded penalties, gives (b), (d) and (T).
   - The "single strictly guiding functional at level 0" hypothesis is used only in (a). With unanimity at level 0, (a) yields minimality on a smaller set, and the Lagrange step has several multipliers, so Topkis fails.
2. **Relation to X2.7.** X2.7's balanced Haar-lexicographic rule, with ν replaced by a finite measure, lies in 𝓛. So by Y1.4 it admits no closed extension even on a small interior N, with no vertex involved. This confirms and sharpens AUDIT_X123's point that nonlocal comparisons are the real issue, and it is independent of X2.9. With the infinite Haar measure, Lyapunov fails, and nonlocal records have infinite mass, so the rule is undefined there.
3. **Relation to X1.** For any order in 𝓛 no plan works. So a successful plan V for the posterior must come from a system outside 𝓛. In particular it cannot come from Cor. X1.3.5 ultralimits of finitely many additive levels. Hyperreal ultralimits are not covered by Y1.4: Lyapunov fails for hyperreal-valued measures.
4. **Additive rankings.** As the one-level special case: for every additive ranking with bounded penalties and finite μ, sections along the posterior family are automatically closed, because p ↦ C_p is continuous in measure. So some incoherent model ties some C_p (p ∈ N₀) at every world. This is local, and independent of Thm gm.

---

## 5. Does the posterior selection "work"? What is and is not shown

- **Shown.** With the posterior family on any open interior set, every lexicographic or credal-additive tower with a strictly guiding additive first level fails (Y1.4). The failing requirements are closed sections and (Csel), for nonlocal records reaching the coordinate planes. Competitiveness and protection are not needed for the failure, and Y1.3 shows that they cost nothing.
- **Not shown.** Failure for arbitrary preorders. Steps (b), (d) and (T) need Lyapunov convexity, which holds for every countably additive, finite, bounded-penalty level. A construction for the posterior must therefore leave 𝓛 in an essential way:
  - either a first level that is not a single additive functional;
  - or levels that are not countably additive with finite mass: hyperreal or Haar-infinite levels, or charges.
- **Why posterior, specifically.** Y1.4 uses three features of the selection: monotone rays (Y1.1), the absence of other pointwise-comparable pairs, and VC dimension > 3 of the advice regions (the attribution wedges). The first two are the posterior's equivariance seen from inside the interior; the third is X2.6's p-dependent attribution. So the obstruction attacks exactly the two properties that made the posterior attractive in X2.

## 6. Nearby reachable targets and the precise residual

**Q_Y1 (posterior, outside 𝓛).** Are there preorders with strict (G), (IB) and transitivity, satisfying Y1.2's ray closure, in which some incoherent box mixtures X ∈ 𝔅 with Ψ(X) = Ψ(C_p) are strictly worse than C_p at some world?

By Y1.4(c), in 𝓛 they are tied at every world. Outside 𝓛 this requires *complementarity*: a whole tie record rec(C_p, C_q) must be a tie while its parts are strict worsenings from both ends. Writing t = rec(C_p, C_q) and E ⊆ supp t, this means C_p ≺_i C_p ⊕ t|_E ≻_i C_q (consistent with transitivity, as checked in the analysis behind Y1.4). Additive and credal levels forbid complementarity by Lyapunov. This is the exact non-additive mechanism a posterior construction must supply.

**Changing the selection (BRIEF19 allows this once the posterior is excluded; it is excluded only within 𝓛).** The contamination family K_p = (1−ε)p + εΔ satisfies K_u = T1 and is Hausdorff-continuous. Its advice regions are half-planes:
- M iff (1−ε)p·h + εh_o > 0;
- O iff (1−ε)p·h + ε max h < 0.

So step (e) does not apply to it. It also has no monotone rays:
- *First order (PROVED).* At p near u, a direction δ (Σδ = 0) that improves world i pointwise would have to satisfy δ_i ≥ r δ_o and δ_l ≥ r δ_o on Q_o for o ≠ i, and the reverse inequalities on Q_i, with r = (1−ε)p_m/((1−ε)p_o + ε) < 1. These inequalities force δ = 0.
- *Finite pairs (NUMERICS, `contam_check.out`).* 179 of 180 random pairs near u are crossing at all three worlds. The remaining one is a search miss: the witnesses lie in thin strips.

So step (a) of Y1.4 is not available verbatim. Two caveats, which are sketches only and not checked in detail:
- The lexicographic closedness argument still forces level-set minimality at every p that is not a local minimum of q ↦ ψ_i(C_q).
- For a **balanced** level 0 (Y1.3), the within-box classifiers live in the plane Σ = 0. That plane has VC dimension 2, which is below the half-planes' 3. So within 𝓛 the contamination family would need an *unbalanced* first level, for which competitiveness is no longer free.

**Proposed next milestone (CONJECTURE that it is the right one).** Decide whether the contamination family on a small N admits a two-level 𝓛-system:
- level 0: a strictly guiding additive ψ making every C_p (p ∈ N) Pareto-optimal;
- level 1: a box-penalty tie-break.

This is a local realisation problem with half-plane charts: Prop. reduction (e) of the write-up, restricted to N. Global Thm gm does not decide it, because its proof needs vertex neighbourhoods (write-up §4.2).

## 7. Status

| Item | Status |
|---|---|
| Y1.1 monotone rays of the posterior family; converse | PROVED; NUMERICS (`mono_check.out`, 12 000 ray samples, 0 violations; 897/897 off-ray witnesses) |
| Y1.1′ no all-world tie between distinct posterior models; sections star-shaped toward e_i | PROVED |
| Y1.2 ray closure for any preorders | PROVED |
| Y1.3 balanced field: everything but (Csel), for any continuous coherent selection | PROVED |
| **Y1.4 no 𝓛-system for the posterior on any open N₀ ⊆ Δ° (closed sections + (Csel))** | PROVED (not refereed) |
| Y1.5 four-point robust shattering by posterior advice sets with two-element boxes | PROVED; CHECKED exactly (`shatter.out`, 4 values of ε × 3 scales) |
| Contamination family: no pointwise-comparable directions near u | PROVED (first order); NUMERICS (finite pairs) |
| Contamination family: escapes steps (a) and (e) | (e) PROVED; (a) only partially; balanced-level-0 failure sketched |
| A genuine interior subsystem through T1 | **not obtained** |
| Q_Y1 (posterior outside 𝓛: complementarity) | open |

**Referee priorities.**
1. Y1.4(b): the Lagrange interior condition at each level, and the Topkis constancy across all of N₀.
2. Y1.4(d)(T): the compensation step (equal-share Lyapunov partition) and the incoherence of the flipped model.
3. Y1.4(e): replacing lexicographic signs by real vectors, and VC dimension 3 for homogeneous half-spaces in ℝ³.

## 8. Files (`y1py/`)
- `post.py`: exact posterior advice (X2.6 form), world ranks, rays.
- `mono_check.py` / `.out`: Lemma Y1.1, numerically.
- `shatter.py` / `.out`: Lemma Y1.5, exact rationals with an LP for candidate lines. Every line is then verified exactly, including its two-element box on N₀.
- `contam_check.py` / `.out`: contamination family crossing, numerically.
