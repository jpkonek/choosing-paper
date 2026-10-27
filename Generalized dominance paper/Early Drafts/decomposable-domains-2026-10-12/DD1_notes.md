# DD1 (round 32, BRIEF24). Coordinate-threshold defence regions on the patched posterior family: what the selected layer forces, an exact necessary condition, explicit forbidden configurations, and the status of the decisive lemma

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full proof here, one reader (me), not refereed;
- **CHECKED**: exact rational computation (reproducible script) or step-by-step reading;
- **NUMERICS**: floating-point search; nothing depends on it;
- **CONJECTURE**.

Scripts are in `dd1py/` (run `python3 -I <script>.py ...` from inside that folder; outputs in `*.out`). Domain: the
full four-advice domain (every measurable model evaluable; (LF) holds at every target, in particular at T1). No
assumption is added; every extra hypothesis is a hypothesis of a stated result.

---

## 0. Outcome

**No full system covering T1 was obtained. The decisive lemma is neither proved nor refuted.** Coordinate thresholds
survived every finite test I could formulate, except one, which fails for a design reason that can be repaired: the
placement of the designated indices of the patched family. What was established:

1. **The patched family (§1; PROVED).** K_p = (1−β_k(p))K_p^0 + β_k(p)K_k is constructed explicitly: three disjoint
   bumps of radius ρ = 1/40, centred at q_k = u + (3/50)d_k. It is a coherent selection, Hausdorff-continuous, hence
   continuous in measure. It gives T1 at u, keeps the boundary family, and passes through K_2, K_3, K_4 at q_2, q_3,
   q_4. It is **injective** (edge-direction count), which r(C_q) = q needs.
2. **Thresholds are the selected layer plus closed sections (Thm 2.1; PROVED).** Given (G) and (IB), "C_p ≼_i C_q ⟺
   p_i ≥ q_i" together with closed sections is equivalent to coordinate thresholds with r(C_q) = q. Competitiveness is
   then exactly Σ_i r_i(X) ≤ 1, and closed sections are automatic.
3. **An exact necessary condition (Thm 2.4, (NC); PROVED).** Coordinate thresholds, competitiveness and strict (G)
   force the following. If one model X is pointwise weakly i-better than C_{p^i} for i = 1, 2, 3, then
   Σ_i p^i_i < 1 (unless all three p^i are equal). Existence of such an X is a finite geometric condition on the
   three credal sets (Lemma 2.3). (NC) contains selected-layer strict (G) as a special case.
   - The **unpatched posterior family satisfies (NC) exactly, with a linear margin and with equality only on the
     diagonal (Prop 2.5; PROVED).** This is why C_p ≼_i C_q ⟺ p_i ≥ q_i is natural for it.
4. **Explicit forbidden configurations: designated-index windows (§2.4; CHECKED exactly).** Nine exact rational
   certificates show (q_2)_1 < 47/80, (q_2)_2 < 99/200, (q_2)_3 < 217/400, and similarly for q_3 and q_4. A
   designated index outside its window gives an explicit finite violation of competitiveness. Example: (q_2)_2 ≥
   99/200, which occurs if the bump is centred 1/4 from u. **So the patched family works only with designated
   indices near u.** The design of item 1 respects all nine windows. On that design:
   - (NC) in the transition zones: no violation (minimum margin 0.0315; near-diagonal search) (NUMERICS);
   - selected-layer (G) on all 18 equal-projection pairs found inside the bumps: all oriented correctly (NUMERICS).
5. **(IB) at the selected layer (Prop 2.6; PROVED).** Two different selected pairs with the same record form a
   "commuting square". The posterior family has none. For the patched family their absence is a CONJECTURE.
6. **Seeds are consistent with thresholds at the coherent layer (Lemma 2.7; PROVED).**
   - Strict (G) never forces r_1(X_k^A) above (q_k)_1 through coherent models: a cone contained in the bounded cells
     is null.
   - For the same reason, the audit's coupling composition (rearranging within regions) cannot be triggered by any
     pair of coherent models.
7. **Two rigidity theorems for the decisive lemma (§3; PROVED).**
   - **Frontier rule (Lemma 3.2).** For every X, the record from C_{r(X)} to X is accepted at all three worlds. No
     selected model may agree with X on its support.
     - Consequence (Cor 3.3): no splice of two selected models can sit at either endpoint's index.
     - Consequence: under a mild pattern hypothesis, **positions cannot be additive on splices** (Lyapunov). This is
       Y1.3's failure, now in threshold form.
   - **Pexider rigidity (Prop 3.4).** On every connected open part of an agreement region, the positions of the
     transported modifications C_q ⊕ t are affine in q with a common slope: Bayes-like homotheties.
   - Neither theorem yields a contradiction (checked against local records, the frontier, edges and seeds; §3.4).
8. **Which assumption is responsible.** The one failure found is caused by **the patched family's designated indices
   (r(C_{q_k}) = q_k with q_k far from u)**, not by coordinate thresholds. Nothing found so far shows coordinate
   thresholds themselves must fail. The relaxation to general closed covers was therefore not needed for any
   obstruction found.

---

## 1. The patched family

**Data.**
- ε = 3/10, u = (1/3, 1/3, 1/3), T1 = co{v_k}, v_k = (1−ε)u + εe_k.
- K_p^0 := co{ν(p⊙v_k)}, where ν is normalisation.
- K_1 := T1, and K_k := co(K′ ∪ V_k) for k = 2, 3, 4, with K′ = u + (9/10)(T1 − u). These are CC1's seed credal sets.
  They have 4, 5 and 6 vertices respectively (`test_geom.out`).
- Directions in the plane Σ = 0: d_k := √(2/3)(cos θ_k, cos(θ_k − 120°), cos(θ_k + 120°)), with θ = 90°, 210°, 330°
  for k = 2, 3, 4.
- Designated indices q_k := u + D d_k, with D = 3/50. Bump radius ρ = 1/40.
- β_k(p) := φ(|p − q_k|/ρ), where φ(s) = (1 − s²)² for s < 1 and φ(s) = 0 otherwise. This is C¹.

**Definition.**

  K_p := (1 − β_k(p))K_p^0 + β_k(p)K_k   (Minkowski combination)

for p in bump k, and K_p := K_p^0 elsewhere. The bumps are pairwise disjoint (|q_k − q_l| = D√3 > 2ρ), do not
contain u (D > ρ), and lie in Δ°. Set C_p := D_{K_p} (`family.py`).

**Proposition 1.1 (PROVED).**
- (a) Each K_p is a nonempty closed convex subset of Δ, so C_p is coherent.
- (b) p ↦ K_p is Hausdorff-continuous on Δ. Hence p ↦ C_p is continuous in measure.
- (c) K_u = T1, K_{q_k} = K_k, and K_p = K_p^0 near ∂Δ (boundary family unchanged).
- (d) p ↦ K_p is injective.

*Proof.*
- **(a)** Minkowski combinations of compact convex subsets of Δ with weights summing to 1 lie in Δ and are compact
  and convex.
- **(b)** K_p^0 is continuous on all of Δ, because v_k ∈ Δ° gives p·v_k > 0. β is continuous, and Minkowski
  combination is Hausdorff-continuous. For h with P_K(h) ≠ 0 and P_K(−h) ≠ 0, the advice of D_K is locally constant
  under Hausdorff perturbation of K. The exceptional set is ∂D_K ∪ −∂D_K, which is null. Dominated convergence gives
  μ(C_{p_n} △ C_p) → 0.
- **(c)** Immediate.
- **(d)** In the plane, the set of edge directions of A + B is the union of those of A and B. K_p^0 is a triangle. By
  `edge_dirs.out` (CHECKED), dir(K_k) has 4, 5, 6 elements for k = 2, 3, 4, and |dir(K_k) ∖ dir(K_l)| ≥ 4 for k ≠ l.
  - A patched set with β > 0 in bump k has at least 4 directions besides those of a triangle. So it equals no
    posterior triangle.
  - It equals no patched set of another bump l: the ≥ 4 directions of K_k not in K_l would all have to come from one
    triangle, which has only 3.
  - Within one bump, suppose (1−β)T + βK_k = (1−β′)T′ + β′K_k with β < β′.
    - Cancelling βK_k (support functions) gives (1−β)T = (1−β′)T′ + (β′−β)K_k.
    - Triangles are Minkowski-indecomposable, so K_k would be a homothet of a triangle. That is false.
    - Hence β = β′, then T = T′, and posterior injectivity gives p = p′. ∎

---

## 2. The selected layer

### 2.1 Thresholds versus the selected layer

**Theorem 2.1 (PROVED).** Let ≼_i be preorders with (G), and let p ↦ C_p be a selection.
- (a) Suppose (SL) holds: C_p ≼_i C_q ⟺ p_i ≥ q_i. Then, for each X, the section {p : C_p ≼_i X} is an up-set of
  the total preorder "p_i ≥ q_i". If it is closed, it equals {p : p_i ≥ r_i(X)}, where
  r_i(X) := min{p_i : C_p ≼_i X} ∈ [0,1], or +∞ if the section is empty.
- (b) Conversely, coordinate thresholds with r(C_q) = q give (SL).
- (c) Under coordinate thresholds, C_p is competitive on supp p for every p ∈ Δ and every X iff Σ_i r_i(X) ≤ 1 for
  every X.
- (d) Under coordinate thresholds every section is closed. So (S) reduces to the choice of r.

*Proof.*
- **(a)** If C_p ≼_i X and q_i ≥ p_i, then C_q ≼_i C_p ≼_i X.
- **(b)** Immediate.
- **(c), forward direction.** Suppose Σr_i ≤ 1 and every i ∈ supp p had p_i < r_i. Then
  1 = Σ_{supp p} p_i < Σ r_i ≤ 1, a contradiction.
- **(c), converse.** Suppose Σr_i > 1. Put p := r/Σr; any infinite entry is replaced by a number large enough that
  p_i < r_i still holds. Then every i ∈ supp p has p_i < r_i.
- **(d)** Immediate. ∎

So r ∈ Δ, as the brief takes it, is the tightest competitive choice. Σr < 1 is the general one. Everything below
that uses r ∈ Δ says so.

### 2.2 Pointwise comparability of coherent models

**Lemma 2.2 (fibre criterion; PROVED).** D_K is pointwise weakly i-better than D_L (a.e.) iff both of the following
hold:
- (A) K ⊆ co(L ∪ {e_i});
- (B) every segment [l, e_i] with l ∈ L meets K.

Equivalently, in the central projection from e_i the two sets have the same image, and on every fibre both the
nearest and the farthest points of K are at least as close to e_i as those of L.

*Proof.* On mixed g, being weakly i-better is equivalent to two inclusions:
- g_i > 0 and g ∈ D_L ⟹ g ∈ D_K;
- g_i < 0 and g ∈ D_K ⟹ g ∈ D_L.

Each rejection statement is the acceptance statement for −g. By duality of closed convex cones, the first inclusion
is cone(K) ⊆ cone(L ∪ {e_i}), which is (A). The second is cone(L) ⊆ cone(K ∪ {−e_i}): every l has l + ce_i ∈ cone K
for some c ≥ 0, which is (B). Coordinate planes and boundaries are null. ∎

**Lemma 2.3 (one model better than three; PROVED, CHECKED).** For credal sets K^1, K^2, K^3, a model X pointwise
weakly i-better than D_{K^i} for every i exists iff, for each odd world o and each j ≠ o, K^o ≤_o K^j. Here L ≤_o K
means:
- every m ∈ L is o-dominated by some k ∈ K;
- every k ∈ K o-dominates some m ∈ L.

"k o-dominates m" means k_o m_j ≥ k_j m_o and k_o m_l ≥ k_l m_o, where {j, l} = Ω ∖ {o}. Call such a triple
**compatible**.

*Proof.*
- On a mixed h ∈ Q_o, a feasible advice exists iff two conditions hold for each j ≠ o:
  - acc(K^j) ⊆ acc(K^o);
  - rej(K^o) ⊆ rej(K^j).
  This is a direct enumeration of the three ranks.
- Unanimous problems are unconstrained, since coherent models agree there. X is then any measurable selection.
- By duality, acc(L) ⊆ acc(K) on Q_o iff K ⊆ cone(L ∪ {e_j, e_l, −e_o}), and rej(K) ⊆ rej(L) on Q_o iff
  L ⊆ cone(K ∪ {e_o, −e_j, −e_l}).
- m ∈ cone(K ∪ {e_j, e_l, −e_o}) iff some k ∈ K o-dominates m. (Take a = min(m_j/k_j, m_l/k_l).)

`geom.py` implements both the cone test and the two-dimensional test. They agree on 768 cases (`test_fast.out`). For
the posterior family, ≤_o is the ratio order: K_p^0 ≤_o K_q^0 iff p_o/p_j ≤ q_o/q_j and p_o/p_l ≤ q_o/q_l. There
are 0 mismatches in 900 exact random tests (`test_geom.out`). ∎

### 2.3 The necessary condition

**Theorem 2.4 (NC; PROVED).** Assume:
- strict (G);
- competitiveness on supp p at every p;
- coordinate thresholds for every model, with arbitrary r.

Let (K_{p^1}, K_{p^2}, K_{p^3}) be compatible, and let X be as in Lemma 2.3.
- If X ∉ {C_{p^1}, C_{p^2}, C_{p^3}}, then p^1_1 + p^2_2 + p^3_3 < 1.
- If moreover r(C_q) = q, the same conclusion holds whenever the p^i are not all equal.

*Proof.*
- X ≠ C_{p^i} and X is weakly i-better, so X ≺_i C_{p^i} and C_{p^i} ⋠_i X. Hence r_i(X) > p^i_i.
- If Σ_i p^i_i ≥ 1, put p := (p^i_i)_i / Σ_i p^i_i. Then p_i ≤ p^i_i < r_i(X) for all i, and competitiveness fails
  at p.
- If X = C_{p^m}, then r(X) = p^m and r_i(X) > p^i_i for i ≠ m (injectivity). So
  Σ_i p^i_i < p^m_m + Σ_{i≠m} p^m_i = 1. ∎

Taking (p^1, p^2, p^3) = (p, q, q) and X = C_q gives selected-layer strict (G): if C_q is pointwise 1-better than
C_p, then p_1 < q_1. (NC) is strictly stronger: it only needs the six "half-comparisons" on the regions Q_o, and
these hold on an open set of triples.

**Proposition 2.5 (the posterior family satisfies (NC), tightly; PROVED).** For K_p^0 = ν(p⊙T1):
- compatibility implies Σ_i p^i_i ≤ 1;
- equality holds only if p^1 = p^2 = p^3;
- 1 − Σ_i p^i_i ≥ c(p^1)(|p^2 − p^1| + |p^3 − p^1|), with c continuous and positive on Δ°.

*Proof.*
- acc-inclusion on Q_o is q ∈ cone(p, e_j, e_l, −e_o) (Lemma 2.3 and the ratio form). Write
  q = ap + be_j + ce_l − de_o.
- Then p_o − q_o = (b+c)p_o + d(1−p_o) ≥ min(p_o, 1−p_o)(b+c+d). Also |q − p| ≤ 2(b+c+d).
- So q_o ≤ p_o, with a linear gap. Apply this to (o, j) = (2,1) and (3,1):
  Σ_i p^i_i ≤ p^1_1 + p^1_2 + p^1_3 = 1, with the gaps p^1_2 − p^2_2 and p^1_3 − p^3_3. ∎

### 2.4 The patched family: windows for the designated indices, and the explicit forbidden configuration

For K_k (k = 2, 3, 4) in slot i and posterior sets in the other two slots, compatibility gives
(q_k)_i < U_i(k) := 1 − p^j_j − p^l_l. A grid search (`nc_bounds.py`, NUMERICS) located the optima. `nc_window_exact.py`
refined them to exact rational compatible triples, and `verify_certs.py` re-verified them with the independent cone
test (CHECKED; `verify_certs.out`):

| | slot 1 | slot 2 | slot 3 |
|---|---|---|---|
| q_2 | < 47/80 | < 99/200 | < 217/400 |
| q_3 | < 43/100 | < 47/100 | < 93/200 |
| q_4 | < 91/200 | < 213/400 | < 199/400 |

No compatible triple with K_k in two slots and a posterior set in the third was found. So the grid search gave no
lower bounds.

**Explicit forbidden configuration (CHECKED).** Let p^1 = (6/25, 173/400, 131/400) and p^3 = (17/50, 79/200, 53/200).
Then (K_{p^1}^0, K_2, K_{p^3}^0) is exactly compatible. Let X be the pointwise model of Lemma 2.3. Then:
- X ≺_1 C_{p^1}, X ≺_2 B_2, X ≺_3 C_{p^3};
- so r(X) > (6/25, (q_2)_2, 53/200).

If (q_2)_2 ≥ 99/200, then at p = (6/25, 99/200, 53/200)/Σ every world rejects X, and competitiveness fails. For
example, centring the bumps at distance D = 1/4 gives (q_2)_2 ≈ 0.5101, and the witnesses p^1, p^3 lie outside all
bumps. **This is a genuine finite composition killing that design.** The responsible assumption is "r(C_{q_k}) = q_k
with q_k far from u": K_k's shape is close to T1's, so its index must stay close to T1's.

**The design of §1 (D = 3/50) is inside all nine windows.** For example, q_2 = (0.3333, 0.3758, 0.2909). NUMERICS on
that design:
- **Transition zones.** For 7 transition sets per bump (β ∈ {1, 0.56, 0.08}), 3 slots each, against posterior
  partners, the minimum of U_i(c) − c_i is +0.0315 (`nc_transition_U.out`).
- **Near-diagonal search.** 27 000 random near-diagonal triples around transition centres found no compatible triple
  with Σ ≥ 1. The best had Σ − 1 = −2.4·10⁻³ (`nc_local.out`). Shape change makes nearby patched sets mostly
  incomparable.
- **Equal-projection pairs.** Pointwise comparability needs equal central projections (Lemma 2.2), a codimension-2
  condition. Newton's method from mirror seeds found 18 such pairs inside bumps. All are fibrewise comparable, and all
  are oriented as (SL) requires (`pair_G.out`).
- **Widths.** The projection widths of K_k differ from the posterior width 1.6534 at every world, so B_k is never
  pointwise comparable with a posterior model (`proj_width.out`).

These checks give no proof of (SL)-(G) on the whole patched family; the label is NUMERICS.

### 2.5 (IB) at the selected layer

**Proposition 2.6 (PROVED).**
- (a) If rec(C_p, C_q) = rec(C_{p′}, C_{q′}) with (p′, q′) ≠ (p, q) and p ≠ q, the four models form a commuting
  square: C_q = C_p ⊕ R1, C_{p′} = C_p ⊕ R2, C_{q′} = C_p ⊕ R1 ⊕ R2, with disjoint non-null supports. (IB) then
  demands [p_i ≥ q_i ⟺ p′_i ≥ q′_i] and [p_i ≥ p′_i ⟺ q_i ≥ q′_i].
- (b) Near any open piece of a facet of D_{K_p} that both supports approach, they lie on opposite sides; otherwise
  they would overlap. Then D_{K_{q′}} is not convex there. So every vertex of K_p must be a vertex of K_q or of
  K_{p′}.
- (c) Distinct posterior triangles share at most one vertex: ν(p⊙v_a) = ν(q⊙v_b) fixes q, and two such equations
  are incompatible because v_a/v_b ≠ v_c/v_d. So the posterior family has no commuting squares, and (IB) imposes
  nothing at its selected layer.

*Proof of (a).* Put R1 := rec(C_p, C_q) and R2 := rec(C_p, C_{p′}). The records agree, so C_{p′} = C_p on supp R1,
hence supp R2 ∩ supp R1 = ∅. Off supp R1, C_{q′} = C_{p′}. So rec(C_q, C_{q′}) = R2, which gives the square. ∎

For the patched family, a commuting square needs two patched polygons sharing a vertex. Every vertex of
(1−β)K_p^0 + βK_k has a posterior component that moves with p, so this needs non-generic coincidences. The absence
of commuting squares in the patched family is a **CONJECTURE**.

### 2.6 The seeds

**Lemma 2.7 (cones versus bounded cells; PROVED).** Let R be a bounded measurable set and B, C coherent models. If
B ⊕ t, with supp t ⊆ R, is pointwise weakly i-better than C, then C is pointwise weakly i-worse than B a.e.

*Proof.* The set where C is strictly i-better than B is a cone, because coherent advice and sign(h_i) are invariant
under h ↦ λh with λ > 0. By hypothesis this cone lies in R up to a null set. A measurable cone that is null outside a
bounded set is null: scale the shells {1 ≤ |h| ≤ 2}. ∎

Consequences.
- **(i)** The retained seeds C_{q_k} ≼_1 X_k^A need r_1(X_k^A) ≤ (q_k)_1. Strict (G) forces r_1(X_k^A) > p_1 only
  through coherent C_p ≺-below X_k^A. By Lemma 2.7 these are 1-worse than B_k, and C_p ≠ B_k because X_k^A is worse
  than B_k on the cells S ∋ k. So p_1 < (q_k)_1 by (SL). There is no conflict at any bundle scale.
- **(ii)** The audit's coupling composition needs world 1 to accept the "undo" records that rearrange correctness
  within the pair cells. These are supported in the bounded cells, and by Lemma 2.7 no pair of distinct coherent
  models has such a record. So the coupling contradiction cannot be produced through the selected layer. It could
  only arise through thresholds of non-coherent models, which is the subject of §3.
- **(iii)** None of the seven seed patterns is realised by an edge model. This was checked by hand from the cell
  signs, using that edge-jk models ignore h_i. So (IB) never transports a seed verdict to ∂Δ.

---

## 3. The decisive lemma

### 3.1 Exact form

By Theorem 2.1 and the transition lemma (AUDIT_nonlinear_programme), a full system with coordinate thresholds and the
retained seeds is exactly a map r: models → {Σ ≤ 1} with r(C_q) = q satisfying the following (PROVED, as a
restatement). Let A_i be the closure, under realisable composition, of three sets:
- the guidance-worsening records;
- the records rec(C_p, X) with p_i ≥ r_i(X);
- (i = 1) the seed records.

Then:
- (T1) A_i contains no rec(C_p, X) with p_i < r_i(X);
- (T2) A_i contains no strict guidance improvement;
- (T3) no X ≠ C_p has rec(X, C_p) ∈ A_i at every i.

T1 = C_u is then covered. The decisive lemma asks that r can be chosen competitor by competitor.

### 3.2 The frontier rule

**Lemma 3.2 (PROVED).** Assume a system as in §3.1 with r(X) ∈ Δ for all X. Put w := r(X) and ρ_X := rec(C_w, X).
- (a) ρ_X ∈ A_i for every i.
- (b) If X ≠ C_w, no selected C_v agrees with X a.e. on supp ρ_X.

*Proof.*
- **(a)** w_i ≥ r_i(X) for all i.
- **(b)** Suppose C_v agrees with X on supp ρ_X. Put Y := C_v with supp ρ_X reset to C_w's advice. Then
  rec(Y, C_v) = ρ_X, so Y ≼_i C_v at every world by (IB). Also Y ≠ C_v, because ρ_X ≠ id. This contradicts (T3). ∎

**Corollary 3.3 (PROVED).** Let p ≠ q, s := rec(C_p, C_q), and X_E := C_p ⊕ s|_E for a non-null E ⊊ supp s.
- (a) r(X_E) ∉ {p, q}.
  - If r(X_E) = p, take C_v = C_q on E.
  - If r(X_E) = q, then ρ = s⁻¹|_{supp s∖E}; take C_v = C_p.
- (b) **Additive positions are impossible.** Suppose r(X_E) = p + ν(E) for a μ-continuous vector measure ν. Suppose
  also that there are disjoint non-null E_1, …, E_m ⊆ supp s and λ_k > 0 with Σλ_kν(E_k) = 0. Then (a) fails.
  - By Lyapunov there are F_k ⊆ E_k with ν(F_k) = (λ_k/max λ)ν(E_k), and E := ∪F_k has ν(E) = 0.
  - The hypothesis holds, for instance, when s has non-null parts on which it improves world 1 only, world 2 only
    and world 3 only. On Q_o an M→S change has pattern {o}, so this happens whenever C_q accepts less than C_p on
    some part of each Q_o.

This is Y1.3's failure mode (incoherent all-world ties of additive fields) in threshold form. Positions must be
non-additive on the splices of every such selected pair.

### 3.3 Pexider rigidity

**Proposition 3.4 (PROVED).** Let t be a record with from-advice b on D := supp t, and let
A_t := {q : C_q = b a.e. on D}. Assume (SL), (IB), transitivity and coordinate thresholds with r(X) ∈ Δ. Put
X_q := C_q ⊕ t for q ∈ A_t.
- (a) rec(X_q, X_{q′}) = rec(C_q, C_{q′}). Hence r_i(X_q) = ρ_i(q_i) with ρ_i nondecreasing.
- (b) The verdict of t at world i is the same at every q ∈ A_t.
- (c) On every connected open U ⊆ A_t, there are c ≥ 0 and d (Σd = 1 − c) with r(X_q) = cq + d for q ∈ U.
  - So r(X_q) is a homothety cq + (1−c)z when c ≠ 1, or a translation when c = 1.
  - The verdict is v_i(t) = [z_i ≤ q_i], constant on U.

*Proof.*
- **(a)** For q, q′ ∈ A_t, X_q and X_{q′} carry t on D and agree with C_q, C_{q′} elsewhere. So X_q ≼_i X_{q′} iff
  q_i ≥ q′_i, and then the sections are nested.
- **(b)** (IB).
- **(c)** Σ_i ρ_i(q_i) = 1 gives Pexider's equation ρ_2(x) + ρ_3(y) = 1 − ρ_1(1−x−y) on an open set.
  - Fixing x, x′ shows ρ_1(s+a) − ρ_1(s) is locally independent of s. So it is a locally additive, monotone
    function of a, hence linear.
  - So all three ρ_i are affine locally, with the same slope, and connectedness globalises this. ∎

**Corollary 3.5 (PROVED).** Let t be local and strictly improve only world 1. Suppose A_t contains points of the
edges q_2 = 0 and q_3 = 0. Then guidance (r_2 ≤ q_2, r_3 ≤ q_3) and r ∈ Δ force d_2 = d_3 = 0. So
r(X_q) = cq + (1−c)e_1 with c < 1. By Lemma 3.2(b), r(X_q) also lies outside A_{t⁻¹}. Near the boundary between
A_t and A_{t⁻¹}, this forces 1 − c = O(diam D).

So small modifications move positions by a homothety towards the ideal of the improved world, of size proportional
to the modification. This is consistent.

### 3.4 What was tried, and where a proof stops

Each of the following tests passed; none produced a contradiction.
- **(NC) at all scales**, on the posterior family (proved) and on the patched family (numerics).
- **Edge structure.** Edge-jk models are the tied bottom of world i's selected chain. A local i-worsening of an edge
  model has r_i ≤ 0, and is accepted at world i from every selected model. This is consistent because no selected
  model is pointwise i-worse than an edge-jk model (Prop 2.5).
- **Single crossing pairs.** The conditions on the position map φ(E) = r(X_E) are monotonicity, the frontier rule,
  strict (G) and competitiveness. A concave "gain" or convex "loss" correction to an additive φ satisfies the
  composition conditions. On Lyapunov-proportional parts it then forces Σφ > 1, so it is not competitive. Additive φ
  violates Cor 3.3. A per-pair non-additive φ (additive plus a subadditive bulge along a fixed direction) satisfies
  all single-pair conditions except one composition inequality at worlds where the bulge direction is negative. I
  found neither a working general φ nor an impossibility proof.
- **Seeds and the coupling composition.** Through coherent models: impossible (Lemma 2.7). Through local
  modifications C_q ⊕ τ of the bundle patterns: Proposition 3.4 makes their positions affine. The required sandwich
  X_k ≤_1 C ≤_1 B_k on the parts with k ∈ S is impossible, which blocks the chain.

**Where a transfinite proof stops.** The natural invariant is the following. For every unassigned Y,
λ_i(Y) := sup{p_i : Y ≺_i C_p in the current closure} has Σλ < 1, and the forced upper bounds μ_i(Y) exceed λ_i(Y).
- Installing r(X) adds the transports of every rec(C_p, X) with p_i ≥ r_i(X). Each transport Y ≼_i Y′ raises
  λ_i(Y) to λ_i(Y′).
- The invariant is preserved if no Y inherits large λ-values at different worlds from different Y′. Excluding this
  is a three-world, many-pair condition of NC type on the non-selected layer.
- I can neither prove it nor produce a configuration violating it. The only global constraints I found on r are
  Lemma 3.2 and Proposition 3.4, and both are satisfiable locally.
- So the decisive lemma is **open**. Its exact remaining content: a position map on all models with the frontier
  rule, Pexider-affine on agreement regions, and **non-additive on splices** (Cor 3.3), whose (IB)-closure avoids
  (T1)–(T3).
- The CC1 obstruction (Thm 4.1) applies to finite-seed countably additive envelopes. A threshold system escapes it
  only if its small-move acceptance is not cone-like. Proposition 3.4 shows that small-move positions are affine.
  Whether this affine structure forces cone-like acceptance, and so brings back the BB2 chain, is the sharpest open
  sub-question. **CONJECTURE (50/50): it does not**, because the slope and centre (c_t, z_t) vary with the record t,
  and only their monotone relations under composition are constrained.

---

## 4. Status

| Item | Statement | Label |
|---|---|---|
| 1.1 | patched family: coherent, continuous in measure, T1 at u, boundary kept, injective | PROVED (+ CHECKED edge directions) |
| 2.1 | thresholds ⟺ (SL) + closed sections; competitiveness ⟺ Σr ≤ 1 | PROVED |
| 2.2–2.3 | fibre criterion; one-model-better-than-three ⟺ six EM conditions | PROVED; CHECKED (two exact tests agree) |
| 2.4 | (NC) necessary for coordinate thresholds | PROVED |
| 2.5 | posterior family satisfies (NC), tight, linear margin | PROVED |
| 2.4 table | designated-index windows; explicit forbidden configuration for far bumps | CHECKED (exact) |
| 2.4 design | D = 3/50, ρ = 1/40: (NC) and (SL)-(G) hold in all tests | NUMERICS |
| 2.6 | selected-layer (IB) conflicts only via commuting squares; none for posterior | PROVED |
| 2.6 patched | no commuting squares | CONJECTURE |
| 2.7 | seeds and coupling composition consistent at the coherent layer | PROVED |
| 3.2–3.3 | frontier rule; splices never at endpoint indices; additive positions impossible | PROVED |
| 3.4–3.5 | Pexider rigidity: local positions are homotheties | PROVED |
| decisive lemma | thresholds can always be assigned | **open**: not proved, no counterexample |
| T1 cover | | **not obtained** |

## 5. Files (`dd1py/`)

- `geom.py`: exact credal geometry. Includes the seed sets, posterior sets, the cone-membership EM test `le_o`, the
  two-dimensional test `le_o_fast`, and `compatible_fast`.
- `test_geom.py` → `test_geom.out`: posterior EM order = ratio order; vertex lists of K_1–K_4 (CHECKED).
- `test_fast.py` → `test_fast.out`: the two exact EM tests agree (CHECKED).
- `family.py`: the patched family (float), with default design D = 3/50, ρ = 1/40.
- `nc_bounds.py` → `nc_bounds.out`: grid search for the designated-index windows (NUMERICS).
- `nc_window_exact.py` → `.out`, `.json`; `verify_certs.py` → `verify_certs.out`: exact window certificates and the
  explicit forbidden configuration (CHECKED).
- `nc_transition_U.py` → `nc_transition_U.out`: (NC) margins for transition sets (NUMERICS).
- `nc_local.py` → `nc_local.out`; `nc_patched.py` → `nc_patched.out`; `nc_fold.py`: near-diagonal and fold searches
  (NUMERICS).
- `proj_width.py` → `proj_width.out`: projection widths and collision search (NUMERICS).
- `pair_G.py` → `pair_G.out`: equal-projection pairs inside bumps and their (G) orientation (NUMERICS).
- `edge_dirs.py` → `edge_dirs.out`: edge directions for injectivity (CHECKED).
