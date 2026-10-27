# FF3 (round 34, BRIEF26). The decisive tie test, analytically: no (G)-certificate and a clean selected layer for the plain posterior family; (C) open

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument here, one reader (me), not refereed;
- **CHECKED**: exact rational computation with a stated script;
- **NUMERICS**: floating point; nothing rests on it;
- **CONJECTURE**.

Scripts are in `ff3py/`. Run `python3 -I <script>.py` inside that folder; outputs are in `*.out`. Setting: full four-advice
domain, three worlds, ε = 3/10, T1 = C_u. Constants: c_0 = 7/30, κ′ := ε/c_0 = 9/7, K := 1 + κ′ = 16/7.
- **Plain family**: C_x = D_{K_x} with K_x = co{ν(x⊙v_k)}, for x ∈ Δ.
- **Patched family**: DD1 §1.

Ties are as in the audit. ~_i is the least equivalence on models containing C_p ~_i C_q whenever p_i = q_i, closed under
(IB) and transitivity. Equivalently, T_i is the least set of records that contains these generator records and is
closed under inversion and realisable composition, cancelled-change composites included. X ~_i Y iff rec(X, Y) ∈ T_i.
No assumption is added.

---

## 0. Outcome

1. **No (G)-certificate exists for the plain posterior family, at any world (Theorem 3.4, Corollary 3.5; PROVED).**
   - Take any finite set of world-1 generator pairs, with endpoints anywhere in Δ, boundary models included. There is
     an explicit *strictly guiding additive record functional* W that vanishes on all of them.
   - Every record derived from those generators therefore has W = 0. This covers (IB) transports and all realisable
     composites, cancelled-change composites included.
   - A monotone nontrivial record would have W ≠ 0. Every certificate uses finitely many generators, so none exists.
     Worlds 2 and 3 follow by permutation symmetry.
2. **The stronger tier passes too (Corollary 3.5(ii); PROVED).** Close the following under (IB) and transitivity:
   - all ties;
   - all selected comparisons C_p ≼_i C_q for p_i ≥ q_i;
   - all guidance comparisons.

   The result contains no strict cycle, no (F1) and no (F2). This is EE1's target (N2), the selected-layer closure is
   clean for every assignment, proved for the plain family without seeds.
3. **Patched family (Corollary 3.5(iii); PROVED).** Any (G)-certificate, strict cycle, (F1) or (F2) in the patched
   family's tie/selected-layer closure must use a generator with an endpoint inside a bump. Beyond that, the patched
   family is not settled.
4. **Why only finite pieces can be represented (Proposition 4.1; PROVED).**
   - No *single* strictly guiding additive functional of homogeneous type respects all world-1 ties on Δ°.
   - The only weakly guiding homogeneous ones live on one class of arrows: rejections of (+,−,−) gambles.
   - The obstruction is a net-convexity identity whose mass sits at the two edges x_2 → 0 and x_3 → 0. Finite
     derivations never reach it.
   - So the ties are additively representable piece by piece but not globally. The survival theorem is genuinely
     finitary.
5. **(C) is open.**
   - The natural route fails at its first step. T1 is not a splice along its own level line (EE2 Thm 2.4(a)), and
     there is no level splice triple (u, a, b) on {x_1 = 1/3} (CHECKED on a grid; Lemma 5.1).
   - Every (C)-certificate must satisfy infinitely many linear moment identities at each world (Lemma 5.2). One
     explicit consequence is D(φ) = κ(cos φ − sin φ).
   - Additive functionals of the homogeneous kind cannot decide (C) (Remark 5.3).
   - **The single most important open point is (C) for the plain family** (§5.4).

---

## 1. A chart in which the plain family is explicit

Index each pair by its member g with g_1 > 0, normalised to g = (1, σ_2 t_2, σ_3 t_3), with t ∈ (0, ∞)². The pairs
fall into four classes:
- **P1**: (σ_2, σ_3) = (−, −);
- **P2**: (−, +);
- **P3**: (+, −);
- **unanimous**: (+, +).

Coordinate planes are null. Lebesgue measure dt on each class has the same null sets as μ on pairs. At world 1,
accepting g is good and rejecting it is bad, in every class. Every coherent model accepts all unanimous pairs, so no
generator acts there.

For x with x_1 > 0, put r = (r_2, r_3) := (x_2/x_1, x_3/x_1) ∈ [0, ∞)². Level sets of x_1 are the lines
r_2 + r_3 = S := (1 − x_1)/x_1.

**Lemma 1.1 [PROVED; CHECKED `regions_check.out`, `boundary_check.out`].** Put s := (r_2 t_2, r_3 t_3). Then C_x's advice
is given by the following table.

| class | accept g | reject g |
|---|---|---|
| P1 | 1 − s_2 − s_3 − κ′ max(s_2, s_3) > 0 | s_2 + s_3 > K |
| P3 | 1 + s_2 > K s_3 | s_3 > 1 + s_2 + κ′ max(1, s_2) |
| P2 | 1 + s_3 > K s_2 | s_2 > 1 + s_3 + κ′ max(1, s_3) |

*Proof.*
- (x⊙v_k)·g = c_0 x_1 (Σ_j y_j + κ′ y_k), with y := r⊙g and r_1 := 1.
- C_x accepts g iff min_k (x⊙v_k)·g > 0, i.e. Σy + κ′ min y > 0. It rejects iff Σy + κ′ max y < 0.
- Evaluate with y = (1, σ_2 s_2, σ_3 s_3).
- Nothing divides by x_2 or x_3, so the table holds on the edges x_3 = 0 and x_2 = 0.
- The script compares the table with the direct test on 60 000 random rational cases, plus 60 000 cases on the edges:
  0 mismatches. ∎

**Lemma 1.2 (ray forms) [PROVED; CHECKED].** Write t = ρ(c, s) with c = cos φ, s = sin φ, φ ∈ (0, π/2). Each advice set
is {ρ < 1/f} or {ρ > 1/f} (with 1/0 = ∞), for the forms f = f(r, φ) below. Every f is homogeneous of degree 1 in r and
piecewise linear.

| class | advice | region | f |
|---|---|---|---|
| P1 | + | ρ < 1/f | M := r_2c + r_3s + κ′ max(r_2c, r_3s) |
| P1 | − | ρ > 1/f | N := (r_2c + r_3s)/K |
| P3 | + | ρ < 1/f | P_3 := (K r_3 s − r_2 c)_+ |
| P3 | − | ρ > 1/f | Q_3 (piecewise, below) |
| P2 | + | ρ < 1/f | P_2 := (K r_2 c − r_3 s)_+ |
| P2 | − | ρ > 1/f | Q_2 (piecewise, below) |

The rejection forms are:
- Q_3 = (r_3s − r_2c)/K if r_3s ≥ (K+1)r_2c;
- Q_3 = r_3s − K r_2c if K r_2c < r_3s < (K+1)r_2c;
- Q_3 = 0 otherwise;
- Q_2 is Q_3 with (r_2, c) ↔ (r_3, s).

*Proof.*
- The P1 rows and P3-acceptance are linear in ρ.
- P3-rejection: ρ ↦ ρ(r_3s − r_2c) − 1 − κ′ max(1, ρ r_2 c) is concave and piecewise linear, starts at −K, and has
  final slope r_3s − K r_2c. So the set where it is positive is (1/Q_3, ∞) or empty. Solving on the two linear pieces
  gives Q_3.
- `regions_check.out` checks these exactly (0 mismatches). ∎

**Edge x_1 = 0 [PROVED; CHECKED `boundary_check.out`].** Put a := x_2/(K x_3) ∈ [0, ∞]. Then:
- P1 is always rejected;
- P3 is accepted iff tan φ < a and rejected iff tan φ > K²a;
- P2 is accepted iff tan φ > K²a and rejected iff tan φ < a.

Each advice set is a union of whole rays.

---

## 2. Additive record functionals

A **weight system at world 1** assigns, on each class, a weight for each kind of advice:
- ω(t, 0) := 0 (silence);
- ω(t, +) := ω_+(t) (acceptance);
- ω(t, −) := ω_−(t) (rejection);
- ω(t, ×) := ω_−(t) + 1 (contradictory advice).

On the unanimous class put ω_+ = −1 and ω_− = 1. The system is **strictly guiding** if ω_+ < 0 < ω_− a.e. on P1, P2 and
P3. Then ω is strictly increasing in world-1 rank at a.e. pair.

For a record d (support F, arrows a(t) → b(t)) put

  W(d) := ∫_F [ω(t, b(t)) − ω(t, a(t))] dt,

whenever the negative part of the integrand is integrable. W then takes values in (−∞, +∞].

**Lemma 2.1 [PROVED].**
- (a) W depends only on the record, so it is invariant under (IB) transport.
- (b) Let d_1, d_2 be realisably composable, each with integrable negative part. Then the composite d has integrable
  negative part and W(d) = W(d_1) + W(d_2). This includes cancelled-change composites.
- (c) If W(d) is finite (absolutely convergent), then W(d^{−1}) = −W(d).

*Proof.* (a) is immediate. For (b), at every t the composite's increment is the sum of the two increments. A step
that does not act at t contributes 0, and on a cancellation set the two increments cancel. Hence the integrands add
pointwise. Their negative parts are dominated by the sum of integrable negative parts. (c) is immediate. ∎

**Corollary 2.2 [PROVED].** Let 𝒢 be a finite set of world-1 generator pairs, and 𝒮 a finite set of selected
comparisons (p, q) with p_1 ≥ q_1. Let ω be strictly guiding, with:
- W(rec(C_p, C_q)) = 0, absolutely convergent, for every (p, q) ∈ 𝒢;
- W(rec(C_p, C_q)) ∈ [0, ∞], with integrable negative part, for every (p, q) ∈ 𝒮.

Then:
- (i) No record derived from 𝒢 by inversion, transport and realisable composition is a nontrivial world-1-monotone
  record. So no (G)-certificate uses only 𝒢.
- (ii) Close 𝒢 (both directions), 𝒮 and all guidance-worsening records under transport and composition. Every record
  d in this closure has W(d) ≥ 0, and W(d) > 0 if d contains a step of 𝒮 with W > 0 or a nontrivial guidance step.
  Hence:
  - there is no strict cycle;
  - there is no (F2), i.e. no nontrivial improving record;
  - there is no (F1), i.e. no rec(C_p, C_q) with W(rec(C_p, C_q)) < 0, which includes the case p_1 < q_1 whenever
    W < 0 there.

*Proof.*
- (i) By Lemma 2.1 every derived record has W = 0. A nontrivial monotone record has every increment of one strict
  sign on a non-null set, so its W is nonzero.
- (ii) Guidance-worsening records have nonnegative integrands. All steps have integrable negative parts, so Lemma
  2.1(b) applies.
- (F2): an improving record has a negative integrand on a non-null set and none positive, so W < 0.
- (F1): the record of the pair is fixed, and its W is negative or −∞. Either way it differs from the computed sum. ∎

Every certificate in the audit's sense, and every strict cycle, (F1) or (F2), has a finite derivation. So Corollary
2.2 settles them once a suitable ω exists for each finite (𝒢, 𝒮).

---

## 3. The functionals

### 3.1 Homogeneous weights

Take ω_+ = −ρ^{−3}A_j(φ) and ω_− = ρ^{−3}B_j(φ) on class j, with A_j, B_j > 0 in L¹(0, π/2). Write W_j for the six
profiles (A1, B1, A3, B3, A2, B2).

**Lemma 3.0 [PROVED].** Let x, y have x_1, y_1 > 0. Then W(rec(C_x, C_y)) = Φ(r_y) − Φ(r_x), absolutely convergent,
where

  Φ(r) := ∫_0^{π/2} [A1·M + B1·N + A3·P_3 + B3·Q_3 + A2·P_2 + B2·Q_2](r, φ) dφ.

*Proof.* By Lemma 1.2, each class and advice type contributes ∫ρ^{−2} over the ray interval between the two
boundaries. This equals ±(f(r_y) − f(r_x)), with signs that turn the weight −A into +A·f and +B into +B·f. Both
boundaries are at ρ ≥ 1/max f > 0, and |f(r_y) − f(r_x)| ≤ C|r_y − r_x|. ∎

So Φ(λr) = λΦ(r). Put g(ζ) := Φ(1, ζ) and ŵ_j(τ) := W_j(arctan τ)·sin³(arctan τ).

**Lemma 3.2 (kinks) [PROVED; NUMERICS `kink_check.out`, max discrepancy 8·10^{−6}].** As a measure on (0, ∞),

  g″(ζ) = Σ_k (coef_k / λ_k) ŵ_{j(k)}(λ_k/ζ),

with the following seven kinks.

| form j | kink at tan φ = λ/ζ, λ = | slope jump / sin φ = coef |
|---|---|---|
| A1 (M) | 1 | κ′ |
| A3 (P_3) | 1/K | K |
| B3 (Q_3) | K | 1 |
| B3 (Q_3) | K+1 | −(K−1)/K |
| A2 (P_2) | K | 1 |
| B2 (Q_2) | 1/(K+1) | −(K²−1)/K |
| B2 (Q_2) | 1/K | K |

B1's form N is linear and has no kink.

*Proof.*
- Each f_j(1, ·, φ) is piecewise linear in ζ with the listed slope jumps.
- Differentiate under the integral. Then ∫W sin φ coef δ(ζ − λ cot φ) dφ = W sin φ coef λ/(ζ² + λ²) at
  tan φ = λ/ζ, which is coef·ŵ(λ/ζ)/λ. ∎

### 3.2 The sector functional (explicit)

Fix Z > 1 and put Y := (K+1)Z. Define b : (0, ∞) → (0, ∞) by:
- b(y) := y³ on [1/Y, Y];
- b(y) := y³(yY)^{1/2} for y < 1/Y;
- b(y) := Y³(Y/y)^{1/2} for y > Y.

Put b̃(y) := y³ b(1/y), so b̃ = 1 on [1/Y, Y]. Choose the profiles through their ŵ:

  B̂3 := b,  B̂2 := b̃,  Â3 := b/2,  Â2 := b̃/2,  Â1 := (47/96)(b + b̃),  B̂1 := b + b̃.

All six profiles are positive. All are in L¹: ∫W dφ = ∫ŵ(τ)(1+τ²)^{1/2}τ^{−3} dτ < ∞. (`local_invariant.out` lists the
values.)

**Theorem 3.3 [PROVED; NUMERICS `local_invariant.out`, `endtoend.out`].** For every r with 1/Z ≤ r_3/r_2 ≤ Z,

  Φ(r) = α (r_2 + r_3),  α := Φ(1,1)/2 > 0.

Hence W vanishes on every world-1 tie whose endpoints lie in the sector Σ_Z := {x ∈ Δ° : 1/Z ≤ x_3/x_2 ≤ Z}, and the
weight system is strictly guiding.

*Proof.*
- **The kink equation on [1/Z, Z].** For ζ ∈ (1/Z, Z), every argument λ_k/ζ lies in [1/Y, Y]. Write z = 1/ζ. By
  Lemma 3.2, g″(ζ) equals

    E(z) := κ′Â1(z) + K²Â3(z/K) + K^{−1}Â2(Kz) + K²B̂2(z/K) + K^{−1}B̂3(Kz) − c_3 B̂3((K+1)z) − c_2 B̂2(z/(K+1)),

  where c_3 = (K−1)/(K(K+1)) and c_2 = (K−1)(K+1)²/K. Note c_3(K+1)³ = c_2, and c_2 − K² = 95/112.
- **E vanishes there.** Substituting the explicit values gives

    E = (1 + z³)[(9/7)(47/96) + 1/(2K) + K² − c_2] = (1 + z³)(141 + 49 − 190)/224 = 0.

  So g is affine on [1/Z, Z], say g = α_0 + βζ.
- **Symmetry.** The relation ŵ_2(τ) = τ³ŵ_3(1/τ) is equivalent to W_2(φ) = W_3(π/2 − φ). It holds for (B2, B3) and
  (A2, A3), and Â1, B̂1 are self-symmetric. The forms satisfy P_2(r_2, r_3, φ) = P_3(r_3, r_2, π/2 − φ), the same for
  Q, and M, N are symmetric. Hence Φ(r_2, r_3) = Φ(r_3, r_2).
- **Slope equals intercept.** Therefore g(ζ) = ζ g(1/ζ). On [1/Z, Z] this gives α_0 + βζ = α_0ζ + β, so α_0 = β =: α.
  Homogeneity then gives Φ(r) = r_2 g(r_3/r_2) = α(r_2 + r_3).
- **Positivity.** α > 0 because every form is ≥ 0 and M > 0.
- **The ties.** Lemma 3.0 converts this into W(rec(C_x, C_y)) = 0 for x_1 = y_1 with both points in Σ_Z.
- **Numerically**, Φ/S is constant to 3·10^{−13} on level segments inside the sector, and increases outside it. A
  direct 2-D quadrature with the raw acceptance test of D_{K_x} agrees with Lemma 3.0 to grid accuracy. ∎

### 3.3 All generators, boundary models included

**Theorem 3.4 [PROVED].** Let 𝒢 be any finite set of world-1 generator pairs and 𝒮 any finite set of selected
comparisons (p, q), p_1 ≥ q_1, with endpoints anywhere in Δ. There is a strictly guiding weight system satisfying the
hypotheses of Corollary 2.2 for (𝒢, 𝒮).

*Proof.* Group the endpoints into four kinds:
- interior points;
- points on the edges x_3 = 0 (ζ = 0) or x_2 = 0 (ζ = ∞) with 0 < x_1 < 1;
- points on the edge x_1 = 0;
- the vertex e_1.

Ties join endpoints of equal x_1. So pairs on the edge x_1 = 0 involve only models on that edge.

- **Step 1 (interior points).** Choose Z with every interior endpoint in Σ_Z, and take Theorem 3.3's system.
- **Step 2 (the edges ζ = 0, ∞).**
  - The edge model at level S has r = (S, 0), and Φ(S, 0) = S·g(0). Ties with interior points need g(0) = α.
    Numerically g(0) − α = 21.6 for Z = 3 (`edge_gap.out`), so a correction is needed.
  - By Lemma 1.2, the P1-rejection boundary of the edge model is at ρ = K/(S cos φ). This tends to ∞ as φ → π/2. The
    corresponding boundaries of the finitely many interior and ζ = ∞ endpoints stay below a common ρ_T on
    φ ≥ π/4.
  - Choose φ_T close enough to π/2 that K/(S cos φ) ≥ ρ_T for all used levels S and all φ ≥ φ_T.
  - On R_T := {φ > φ_T, ρ > ρ_T}, change B1's density to ρ^{−3}(W_{B1} + h) with h > −W_{B1}. This changes Φ(S, 0) by
    (S/K)∫_{φ_T}^{π/2} h cos φ dφ, which is exactly linear in S. Choose ∫h cos φ dφ = K(α − g(0)).
  - Enough room is available. Enlarge B̂1 symmetrically on the tail first. This changes α and g(0) by the same
    amount, because N is linear.
  - Do the mirror-image change on {φ < π/2 − φ_T, ρ > ρ_T} for the edge ζ = ∞.
  - These regions meet no other endpoint's boundaries. So all ties and comparisons among the used endpoints at
    0 < x_1 < 1 now have W = Φ(target) − Φ(source), with Φ = α(r_2 + r_3) on them, and Φ = 0 at e_1.
- **Step 3 (the edge x_1 = 0).**
  - Edge models differ on whole rays (end of §1). Pick ρ_0 below every boundary 1/f of the non-edge endpoints.
  - On ρ < ρ_0 in P2 and P3, multiply the four densities by positive cut-offs. The resulting radial totals
    R_j(φ) := ∫_0^∞ ρ^{−2}χ_j dρ can be any values above 1/ρ_0.
  - Choose them with W_{B2}R_{B2} = W_{A3}R_{A3} and W_{B3}R_{B3} = W_{A2}R_{A2} pointwise, and every W_jR_j ∈ L¹.
  - For two edge models with parameters a, a′, W(rec) = Ψ(a′) − Ψ(a), where

      Ψ(a) = ∫_{tan φ < a}(W_{B2}R_{B2} − W_{A3}R_{A3}) + ∫_{tan φ > K²a}(W_{B3}R_{B3} − W_{A2}R_{A2}),

    which is ≡ 0.
  - Comparisons from a non-edge model to an edge model have W = +∞: near ρ = 0 the first accepts P1 and the edge
    model rejects it. Their negative parts are integrable. Comparisons from an edge model to a non-edge model are not
    in 𝒮, since p_1 ≥ q_1.
- **Positivity and monotonicity.** All weights stay positive, so the system is strictly guiding. On the used
  endpoints, Φ is non-decreasing in S = (1 − x_1)/x_1, with Φ(e_1) = 0 and +∞ on the edge x_1 = 0. So 𝒮-records have
  W ≥ 0. ∎

**Corollary 3.5 [PROVED].**
- (i) **(G).** In the plain posterior family there is no X ~_i Y, at any world, with X weakly guidance-better
  everywhere and strictly on a non-null set. Worlds 2 and 3 follow from world 1 because C_{πx} = π(C_x) for every
  coordinate permutation π (T1 is symmetric).
- (ii) **Stronger tier.** At each world, close the following under (IB) and transitivity:
  - the ties;
  - the selected comparisons C_p ≼_i C_q for p_i ≥ q_i (the threshold scheme's orientation);
  - all guidance comparisons.

  The result has no strict cycle, no (F1) and no (F2). So EE1's (N2) holds for the plain family without seeds, and
  selected-layer (G) holds with (IB) included.
- (iii) **Patched family.** Generator records with both endpoints outside the bumps coincide with plain-family
  records. So any (G)-certificate, strict cycle, (F1) or (F2) in the patched family's closure uses a generator or
  comparison with an endpoint in a bump.

*Proof.* Corollary 2.2 together with Theorem 3.4. A violation has a finite derivation, and Theorem 3.4 supplies an ω
for its finite (𝒢, 𝒮). ∎

**What this does and does not give.**
- The audit's tie test cannot kill coordinate thresholds for the plain family through (G) or through strict cycles.
- The survival quantity is the family {W_ω}: for each finite derivation one strictly guiding additive functional. It
  is not a single functional per world, and §4 shows it cannot be one of homogeneous type.
- Seeds are not included.

---

## 4. Why no single functional works

**Proposition 4.1 [PROVED].** Let homogeneous profiles W_j ≥ 0 in L¹ give a Φ that depends only on x_1 on all of Δ°.
Then W_j = 0 a.e. for j ∈ {A1, A3, B3, A2, B2}, and ∫B1(cos φ − sin φ) dφ = 0. In particular, no strictly guiding
homogeneous additive functional respects all world-1 ties.

*Proof.*
- **Affine.** g is affine on (0, ∞), so g″ ≡ 0.
- **Integral of g″.** By Lemma 3.2 and the substitution ζ = λ cot φ,

    ∫_0^∞ g″ dζ = Σ_j N_j ∫_0^{π/2} W_j sin φ dφ.

  Here N_j is the sum of coef over the kinks of form j, so N = (κ′, 0, K, 1/K, 1, 1/K) for (A1, B1, A3, B3, A2, B2).
  The integral is absolutely convergent.
- **Conclusion.** All N_j except B1's are positive and W_j ≥ 0, so those W_j vanish. With only B1 left,
  Φ = ∫B1 (r_2c + r_3s)/K. ∎

**Reading.**
- Every ray form is "net convex" in ζ: its slope at ζ = ∞ exceeds its slope at ζ = 0.
- The global obstruction is therefore supported at the edges x_3 → 0 and x_2 → 0. In the multiplicative dilation
  variable of world 1 (x ↦ ν(λx_1, x_2, x_3)), it is a statement "at infinity".
- Finite derivations stay at bounded scale, which is why Theorem 3.4 can localise. This mirrors the project's
  additive exclusions: the obstruction is holonomy-like and global.
- The only global weakly guiding functionals are the **P1-rejection functionals** Φ_{B1}, with ∫B1(c − s) = 0. They
  are also exact on boundary models: edge-x_1 = 0 models reject all of P1.

---

## 5. (C)

### 5.1 The natural route fails at u

**Lemma 5.1.**
- (a) [PROVED, EE2 Thm 2.4(a)] T1 is not a splice of two models on its own world-i level line. The level direction
  lies in the excluded sector E_i at u, and the wedge argument works for any segment length.
- (b) [CHECKED `level_u_triples.out`] Take all rational pairs a, b on {x_1 = 1/3} with x_2 ∈ (1/240)ℤ and a strictly
  between u and b: 6 162 triples. The exact support-function test finds **no** triple (u, a, b) with C_a a splice of
  T1 and C_b. The test is exact for each triple; covering only a grid, (b) is a finite check, not a proof for all
  pairs.

So no single transported tie produces X ~_1 T1 from a level splice at u. Any (C)-certificate needs genuine chains or
cancellation composites.

### 5.2 Necessary conditions

**Lemma 5.2 [PROVED].** Let X ∈ O_1(T1). Then W(rec(T1, X)) = 0 for every weight system, of any sign, that vanishes on
the generators of some derivation of rec(T1, X). In particular:
- (a) **The global P1-rejection functionals.** Put

    D(φ) := ∫_0^∞ ρ^{−2}[1(X rejects g) − 1(T1 rejects g)] dρ   (g ∈ P1 at angle φ).

  Then D(φ) = κ (cos φ − sin φ) a.e., for some constant κ.
- (b) **Sector functionals.** The same identity holds for every sign-free tuple of profiles that solves E = 0 on
  [1/Z, Z] and is symmetric (Theorem 3.3's construction without positivity), for Z large enough to cover the
  derivation.

The analogous identities hold at worlds 2 and 3, in their own charts. A (C)-certificate must satisfy all of them at
all three worlds.

*Proof.* Lemma 2.1 holds without sign conditions on absolutely convergent records. For (a), the functionals with
∫B1(c − s) = 0 vanish on every generator, boundary ones included (§4). Hence ∫B1 D = 0 for all bounded B1 ⊥ (c − s).
Their annihilator consists of the multiples of c − s. ∎

**Remark 5.3.**
- Homogeneous functionals see a record only through its radial moments m_j(φ) = ∫ρ^{−2}Δχ_j dρ: one function per
  class and advice type, in each world's own dilation chart.
- A model that reshuffles T1's advice along rays while keeping all these moments at all three worlds is invisible to
  every such functional. Incoherent reshuffles exist at one world: shift a little acceptance outward beyond T1's P1
  boundary and remove the same ρ^{−2}-mass just inside it.
- Whether some incoherent X has zero moments at all three worlds simultaneously is CONJECTURE (expected yes).
- Non-homogeneous local functionals plausibly exist too. A degree-2 analogue of the kink equation has coefficients of
  both signs (CONJECTURE, not worked out). So radial blindness is claimed for the homogeneous class only.
- Either way, **additive functionals are not expected to decide (C)**. A survival proof needs a non-additive
  invariant. A refutation needs an explicit record in T_1 ∩ T_2 ∩ T_3.

### 5.3 Patched family

Only Corollary 3.5(iii) is known. A (G)-certificate in the patched family would have to use bump generators.

### 5.4 The open question

> **(C) for the plain posterior family, ε = 3/10.** Are there an incoherent model X and three finite derivations, one at
> each world i (generators C_p ~_i C_q with p_i = q_i, (IB) transports, realisable compositions including
> cancelled-change composites), each ending at the same record rec(T1, X)?

By §5.2 such an X must:
- satisfy D(φ) = κ_i(cos φ − sin φ) in each world's chart;
- satisfy the sector moment identities at every world.

By Lemma 5.1, it must arise from chains, not from a single level splice at u. If no such X exists, the plain family
passes the whole decisive tie test, given Corollary 3.5.

---

## 6. Part B: corrections requested by the audit

**B1. EE2 Lemma 1.1.** The correct statement is the following.
- (a) If r is a clean fixed point, then r_i(Y) ≤ r_i(X) for every realisation (X, Y) of every record in A_i(r),
  generators in particular.
- (b) Conversely, r is a clean fixed point iff (F2) is absent and r_i(Y) ≤ r_i(X) for **every realisation of every
  record of the closure** (EE1 Thm 3.1).
- (c) Monotonicity along every realisation of every generator, even after guidance saturation, does **not** imply
  (b). EE1 Example 4.3 is an exact SOM-clean assignment whose closure has (F1), and EE1 Thm 4.1 locates the
  mechanism.

EE2's proof of "⇐" fails at "monotonicity along generators passes to composites by transitivity". A cancelled-change
composite can be realised at a context where its factors cannot be, so no chain of generator realisations connects
its endpoints.

*Did EE2 use the false direction?*
- Lemma 1.2 and the reduction to Λ use only (a).
- §§3 and 5 analyse realised chains of length ≤ 2, which factor by construction.
- Thm 4.1 uses an invariant (RF/LB) that is a property of records. It is preserved by composition with cancellation
  and by transport, so it is independent of Lemma 1.1.
- Thm 4.2 builds additive orders on the cube, which needs no lemma.
- The only affected statements are the status-table entry "fixed points ⟺ monotone along generators" and the reading
  of §4.1 "(i)–(iii) avoid all chains". Both must be restricted to realised chains of length ≤ 2.
- No EE2 conclusion that was claimed as PROVED rested on the false direction, as far as I can find.

**B2. EE2 §4.2.**
- *What it proves.* On one splice segment, it treats the switch-parameter cube {Y_J : J a finite union of
  intervals}: models that switch exactly where λ\*(h) ∈ J. Thm 4.1 (discrete) and Thm 4.2 (additive switch densities)
  give strict-slack fixed points for transports and caps *inside that cube*.
- *What is needed.* All measurable splices Y_E, E ⊆ Δ(x_0, x_1) arbitrary, plus consistency with every other model.
- **The extension is a real gap, not a formality [PROVED].** Thm 4.2's rule accepts every pure-forward record (F, ∅)
  at a D-world. On a non-guidance segment, the forward switch set contains both world-i-improving and worsening
  problems. Let F be its improving part, which is non-null. The measurable splice Y_F satisfies Y_F ≺_i C_{x_0} by
  strict (G), yet the rule gives C_{x_0} ≼_i Y_F. Hence any extension must give up "accept all forward records" and
  use a guidance-aware density.
- Theorem 3.3's method supplies such densities for ties. Redoing the strict-slack (bathtub) argument with them is not
  done here.

**B3. EE3 Proposition EE3.1.**
- *Hypotheses:* (SL) consistent with weak and strict (G) at the selected layer; (NC\*): Σλ(X) < 1 for nonselected X;
  bounded seed cells.
- *Its conclusion (c)* concerns the closure under transitivity and cap completion **only**, without (IB) transport.
  It is therefore not a fixed-point theorem. Part (a)'s empty-witness case is a sketch.
- *Status for the patched family:* (SL)–(G) and (NC\*) are NUMERICS (DD1: 18 equal-projection pairs; transition-zone
  and near-diagonal searches).
- *Status for the plain family:* now (SL)–(G) holds even with (IB) and transitivity (Corollary 3.5(ii)). (NC) is
  PROVED on interior triples (DD1 Prop 2.5).
- FF3 adds for the patched family: a selected-layer failure must involve a bump endpoint (Corollary 3.5(iii)).
- EE3 is not a referee report on EE1 or EE2.

**B4. EE1's slack bound.** Let r⁰_θ = (w − θ𝟙/3)_+ with w ∈ Δ and 0 < θ ≤ 1.
- Some w_i ≥ 1/3 ≥ θ/3, and every other coordinate contributes at most w_i. Hence

    Σ_i r⁰_{θ,i} = Σ_{w_i ≥ θ/3}(w_i − θ/3) ≤ 1 − θ/3 < 1.

- The bound is sharp: w = (1, 0, 0) gives 1 − θ/3 > 1 − θ. So the displayed bound Σ ≤ 1 − θ is false.
- EE1 Thm 1.3 (iii)⇒(i) holds with the corrected bound. (ii)⇒(iii) is unaffected, because w = r\* + θ𝟙/3 gives
  r⁰_θ = r\* without truncation.
- θ depends on the model, so this is not a uniform slack.

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| 1.1–1.2 | chart: closed-form advice and ray forms, including all edges | PROVED; CHECKED (exact, 150 000 cases) |
| 2.1–2.2 | additive record functionals survive (IB), cancelled composites, transitivity; exclude certificates, strict cycles, (F1), (F2) | PROVED |
| 3.2 | kink formula for g″ | PROVED; NUMERICS |
| 3.3 | explicit strictly guiding sector functional, Φ = α(r_2 + r_3) on Σ_Z | PROVED (exact identity E ≡ 0); NUMERICS end-to-end |
| 3.4 | strictly guiding functional for every finite (𝒢, 𝒮), boundary models included | PROVED |
| 3.5(i) | no (G)-certificate, plain family, all worlds | PROVED |
| 3.5(ii) | tie + (SL) + guidance closure clean (no strict cycle, F1, F2); EE1 (N2) without seeds | PROVED |
| 3.5(iii) | patched family: failures need bump endpoints | PROVED |
| 4.1 | no single homogeneous strictly guiding functional; edge net-convexity | PROVED |
| 5.1 | level-splice route at u fails | (a) PROVED (EE2); (b) CHECKED (grid) |
| 5.2 | moment identities for (C)-certificates | PROVED |
| 5.3 | additive functionals do not decide (C) | CONJECTURE |
| (C), plain family | incoherent X ∈ O_1∩O_2∩O_3(T1)? | **open** |
| (G), patched family, bump generators | | **open** |
| B1–B4 | corrections | PROVED |

## 8. Files (`ff3py/`)

- `regions_check.py` → `.out`: Lemma 1.1, 1.2 against the direct test (exact).
- `boundary_check.py` → `.out`: edges x_3 = 0, x_2 = 0 and x_1 = 0 (exact).
- `kink_check.py` → `.out`: Lemma 3.2 by finite differences (NUMERICS).
- `kink_positivity.py` → `.out`: an earlier global trial b = z³/(1+z)³. Its residual has two positive roots, as
  Proposition 4.1 predicts for any L¹ global choice (exact).
- `local_invariant.py` → `.out`: Theorem 3.3 by quadrature.
- `endtoend.py` → `.out`: Theorem 3.3 with the raw acceptance test.
- `edge_gap.py` → `.out`: g(0) ≠ α, so Step 2 of Theorem 3.4 is needed.
- `level_u_triples.py` → `.out`: Lemma 5.1(b).
