# FF1 (round 34, BRIEF26). The decisive tie test: the plain posterior family passes it completely, at every world, at every closure depth, for every ε

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full proof here, one reader (me), not refereed;
- **CHECKED**: exact computation (rational or integer arithmetic, full saturation), reproducible script;
- **NUMERICS**: evidence from finite searches about an infinite object; nothing depends on it;
- **CONJECTURE**.

Scripts are in `ff1py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. No script outside
`ff1py/` was modified (`arr.py` copies and adapts `ee2py/cells.py`). No assumption is added; every extra hypothesis is a
hypothesis of a stated result.

---

## 0. Outcome

**No certificate exists, and none can be found by any search: the audit's decisive tie test is passed by the plain
posterior family, in both tiers, for every ε ∈ (0,1).** The reason is structural and short.

1. **The scheme ranks world i by upper probability (Lemma 4.2; PROVED).** On the plain family
   K_p = ν(p⊙T1(ε)), the upper probability of world i is P̄_{K_p}({i}) = φ(p_i), with
   φ(x) = (c0+ε)x/(c0+εx) strictly increasing. So the imposed ties C_p ~_i C_q (p_i = q_i) are exactly the level sets of
   p ↦ P̄_{K_p}({i}), and the strict comparisons order those levels.
2. **Bets against world i resolve these levels (Lemma 4.1; PROVED, CHECKED).** The gamble θ𝟙 − e_i ("bet against i at
   odds θ") is accepted by D_K iff P̄_K({i}) < θ, and accepting it is bad at world i. Slightly rotated bets split each
   level line at any point. Every finite set of selected models is thereby cut into initial segments of a total order
   that refines the level order.
3. **One world, both tiers (Theorem 5.1; PROVED).** For every finite set S of selected models and every world i there is a
   bounded, strictly guiding additive world-i ranking on the full four-advice domain that reproduces the scheme exactly
   on S: equal losses on each level, strictly smaller losses on higher levels. The tie relation and the stronger tier
   are finitary (every derivation uses finitely many selected comparisons), and an additive ranking is invariant under
   (IB) for **every** record, cancelled-change composites included. Hence, at every world:
   - no (G)-certificate (no X ~_i Y with X weakly guidance-better everywhere and strictly on a non-null set);
   - in the stronger tier (all ties, all strict selected comparisons, all guidance comparisons, (IB), transitivity):
     no strict cycle, no reversed selected comparison (F1), no strict guidance reversal (F2).
4. **Three worlds (Theorem 5.2; PROVED).** For **every** selected C_p, in particular T1 = C_u, the set of models tied
   with C_p at all three worlds is {C_p}. This holds for the tie closure and also for ties derived in the stronger tier.
   So there is no (C)-certificate at T1, nor at any other selected model.
5. **Exact computations (§6; CHECKED).** Full saturations of the (IB)+transitivity closure on exact cell arrangements with
   up to 19 selected models and 378 merged cells were computed. They contain genuine cancelled-change composites: 38 of
   2137 records per world, in the hexagon of radius 2 at u, are obtainable only that way. They contain nonzero records
   tied at all three worlds (46 of them), but none is realisable at any selected model, and no improving record occurs.
   Exact rational additive witnesses were found on 7 fragments: up to 37 models and 1239 cells, including the boundary
   and vertices, for ε ∈ {1/20, 1/10, 3/10, 1/2}.
6. **Patched family (§7).**
   - The proof uses gradedness (item 1), which the DD1 patches destroy. Exactly: (q_2)_1 = u_1 = 1/3, yet
     P̄_{K_2}(1) = 19/30 ≠ 8/15 = P̄_{T1}(1) (PROVED).
   - Any certificate for a patched family must use a selected model inside a bump (PROVED).
   - Exact searches on seven patched fragments find none, including dense ones through bump 2 and near its centre
     (CHECKED per fragment; NUMERICS for the family).
   - **CONJECTURE:** the patched family also passes.
7. **What this changes (§8).**
   - Per the audit's decision rule, the selected ties are not the obstruction. Coordinate-threshold sections are **not**
     to be abandoned for the plain family on this ground.
   - The method that settles the test also gives the nearby reachable extension theorem. If every finite set of
     comparisons (guidance, selected layer, caps, seeds) has, at each world, an additive witness that separates every
     forbidden cap, then the closure is a clean fixed point (Prop 8.1; PROVED). With strict slack, EE1 Thm 2.1 then gives
     a full cover of T1.
   - By Q4.2, any cover obtained this way is necessarily "finitely additive, globally non-additive".

**Single most important open point.** Choose thresholds r for the nonselected models, with strict slack, such that each
world's comparisons are *finitely additively separable* in the sense of Prop 8.1. The witnesses may change with the
finite set, and Q4.2 says they must.

---

## 1. Definitions fixed from the write-up (§2 of "The Contamination Triangle")

- **Domain.** The full four-advice domain: every Lebesgue-measurable D ⊆ ℝ³ (mod μ-null sets) is evaluable. Pairs {f,−f}
  are indexed by H = {f_1 > 0}. The advice a_D(f) is + (f ∈ D, −f ∉ D), − (−f ∈ D, f ∉ D), 0 (neither) or × (both).
- **Coherent models.** D_K = {g : P_K(g) > 0} ∪ {g ≥ 0, g ≠ 0} with P_K(g) = min_{m∈K} m·g. For mixed g, D_K accepts g iff
  K lies in the open half-plane H_g = {m : m·g > 0}.
- **Guidance order at world i**, better first: good ≺ no advice ≺ bad ≺ contradictory. Accepting f is good at i iff
  f_i > 0.
- **(G)** (verbatim): "If X gives advice at least as good as Y at world i for a.e. g, then X ≼_i Y; if moreover it is
  strictly better on a non-null set, then X ≺_i Y."
- **(IB)** (verbatim): "For measurable A = −A and measurable F, G ⊆ A^c (with all four models in M_L):
  (D∩A)∪F ≼_i (E∩A)∪F iff (D∩A)∪G ≼_i (E∩A)∪G."
  - On the full domain this says exactly that the verdict on (X, Y) depends only on the **transition record**
    rec(X, Y): the ordered advice pair where X and Y differ, and an identity symbol where they agree, with the common
    advice forgotten (AUDIT_nonlinear_programme).
  - Records compose where their arrows match at the middle advice. Where two arrows cancel, the composite is the
    identity, and (IB) transports it to **every** common advice there. These are the cancelled changes of EE1 Example
    4.3 and AUDIT_EE_ties §1.
- **The family.** T1 = T1(ε) = co{v_k}, v_k = c0𝟙 + εe_k, c0 = (1−ε)/3, ε ∈ (0,1). The plain posterior family is
  K_p = co{ν(p⊙v_k)} for p ∈ Δ (boundary included), and C_p := D_{K_p} = {g : p⊙g ∈ D_{T1}} (EE2 Prop 2.3a). T1 = C_u.
  The patched family is DD1 §1.
- **Orientation of the scheme** (DD1 Thm 2.1, AUDIT_EE_ties): C_p ≼_i C_q ⟺ p_i ≥ q_i (smaller is better; e_i is best at
  world i).
  - Ties: C_p ~_i C_q iff p_i = q_i.
  - Strict selected comparisons: C_p ≺_i C_q iff p_i > q_i.
- **Tie tier.** ~_i is the least equivalence relation on all models that contains every tie C_p ~_i C_q (p_i = q_i,
  p, q ∈ Δ), is closed under (IB) and is transitive. O_i(X) is the class of X.
  - **(G)-certificate:** X ~_i Y with X weakly guidance-better at i everywhere, strictly on a non-null set.
  - **(C)-certificate:** an incoherent X ∈ O_1(T1) ∩ O_2(T1) ∩ O_3(T1).
- **Stronger tier.** ≼*_i is the least preorder closed under (IB) that contains all ties (both ways), all
  C_p ≼_i C_q with p_i > q_i, and all guidance comparisons. A strict cycle is a derived C_q ≼*_i C_p with p_i > q_i (F1),
  or a derived X ≼*_i Y with Y strictly guidance-better than X (F2). Every strict cycle through a strict generator is of
  one of these two forms.

## 2. The closure is finitary and lives on a finite cell arrangement

**Lemma 2.1 (PROVED).**
- (a) Every pair in ~_i (resp. ≼*_i) has a finite derivation from finitely many generators. So it lies in the relation
  ~_i^S (resp. ≼*_i^S) generated by the ties (resp. selected comparisons) among a finite set S ⊂ Δ, together with
  (IB) and transitivity (and guidance).
- (b) The record set of ~_i^S is the closure E_i(S) of the tie records and their inverses under realisable composition.
  X ~_i^S Y iff rec(X, Y) ∈ E_i(S).
- (c) Let 𝒞(S) be the merged cells: the classes of problems on which every C_p, p ∈ S, and the sign pattern of the
  problem are constant. Each is a finite union of non-null open cones (EE2 Lemma 2.3 decision procedure). Every record
  in E_i(S) is constant on each cell.

*Proof.*
- (a) Both relations are generated by finitary rules: the generators, (IB) transport of one pair, and transitivity of
  two pairs.
- (b) This is the transition lemma (AUDIT_nonlinear_programme), applied to an equivalence relation. The set
  {(X,Y) : rec(X,Y) ∈ E} is an equivalence relation (E contains ι and is closed under inverse and composition). It
  depends only on records, and it contains the generators. Conversely, any relation with these properties contains
  every composite: realise the two factors through a common middle model, filling identity entries with the needed
  middle advice; the full domain allows this.
- (c) Generator records are constant on cells, and composition is pointwise. ∎

**Binary form near u (CHECKED; used only in §6).** If S lies close to u, every active cell is binary: the models of S
give only {+, 0} or only {−, 0} there (`closure_check.out`, `invariants.out`).
- Encode a record by x ∈ {−1, 0, 1}^cells, with +1 meaning silence → the acting advice.
- Composability is then exactly "x + y ∈ {−1,0,1}^cells", and the composite is x + y.
- A cell where x_c = −y_c ≠ 0 becomes an identity with a free context.
- So E_i(S) is the closure of the tie vectors under partial addition inside the cube, which is the "admissible
  composition" closure of AUDIT_nonlinear_programme. It is in general strictly smaller than the lattice they span.

## 3. Additive witnesses: what they certify and when they exist

Fix a finite S and a world i. A **cell witness** is a bounded penalty ψ(h, a) = ψ_c(a)/μ(c) for h ∈ c ∈ 𝒞(S), with
ψ_c(0) = 0, ψ_c(+) = −a_c, ψ_c(−) = −b_c, ψ_c(×) any number above the other three values, and τ_c a_c > 0 > τ_c b_c, where τ_c = sign(h_i)
on c. Its ranking is L(X) := ∫ ψ(h, a_X(h)) dμ(h). This is defined for **every** model.

**Lemma 3.1 (PROVED).**
- (a) L is a bounded additive ranking with strict (G) on the full domain.
- (b) The relation L(X) ≤ L(Y) is a total preorder that satisfies (IB) for every record. This includes transports of
  composites whose changes cancel, because L(Y) − L(X) is an integral over the support of rec(X,Y).
- (c) Suppose L(C_p) = L(C_q) whenever p_i = q_i (p, q ∈ S). Then every X ~_i^S Y has L(X) = L(Y).
- (d) Suppose moreover L(C_p) < L(C_q) whenever p_i > q_i. Then every derived X ≼*_i^S Y has L(X) ≤ L(Y), and
  L(X) < L(Y) whenever the derivation uses a strict selected comparison or a nontrivial guidance step.

*Proof.*
- (a) Ranks: × is worst, and the sign conditions order +, 0, − correctly at each cell. μ(c) > 0, and there are
  finitely many cells.
- (b) Immediate from additivity.
- (c), (d) Induction on derivations: the generators satisfy the claim, and (IB) and transitivity preserve it. ∎

**Corollary 3.2 (PROVED).** If for every finite S ⊂ Δ such a witness exists at world i:
- tie tier, with (c): no (G)-certificate at world i, since it would give L(X) = L(Y) together with L(X) < L(Y);
- stronger tier, with (d): no (F1) and no (F2) at world i.

Write A(g) := {p : C_p accepts the oriented gamble g}, and F_λ(g) := λ(A(g)) for a finite signed measure λ on S.

**Lemma 3.3 (alternative; PROVED).** A witness with properties (c) and (d) exists for S at world i unless there is a
signed measure
  λ = Σ_k κ_k (δ_{q_k} − δ_{p_k}),  with each (p_k, q_k) ∈ S² either a tie (κ_k ∈ ℝ) or a strict pair p_{k,i} > q_{k,i}
  (κ_k ≥ 0),
such that
  sign(g_i)·λ(A(g)) ≥ 0 for every oriented gamble g in an open cell,         (★)
and either some strict κ_k > 0 or F_λ ≢ 0.

In words: a combination of scheme-allowed moves (ties either way; from a better level to a worse one) that is pointwise
improving at world i.

*Proof.* The unknowns are (a_c, b_c). The conditions are:
- strict sign conditions;
- tie equalities;
- strict inequalities L(C_q) − L(C_p) > 0 for p_i > q_i.

All are linear, with L(C_q) − L(C_p) = −Σ_c (a_c Δ⁺_c + b_c Δ⁻_c), where Δ^± is the change of the indicator of +, −.
- Motzkin's transposition theorem: infeasibility is equivalent to a vanishing combination with nonnegative coefficients
  on the strict rows, free coefficients on the equalities, and some strict-row coefficient nonzero.
- The unit sign rows contribute exactly the elementary pointwise improvements.
- Reading the combination as λ (the move from p to q contributes F_{δ_q − δ_p}) gives (★).
- Recording the reverse orientation −g of each cell turns the two components into the single condition (★) over all
  oriented g. ∎

## 4. Upper-probability grading and bets that resolve it

For a credal set K write P̄_K(i) := max_{m∈K} m_i.

**Lemma 4.1 (bets against world i; PROVED).** Fix θ ∈ (0,1) and {i, j, l} = {1, 2, 3}.
- (a) D_K accepts b_θ := θ𝟙 − e_i iff P̄_K(i) < θ. Accepting b_θ is bad at world i, since (b_θ)_i = θ − 1 < 0.
- (b) **Rotations.** Let w lie on the line {m_i = θ}, and put g_t := b_θ + t(w_l e_j − w_j e_l). For small |t| ≠ 0,
  D_K accepts g_t iff one of the following holds:
  - P̄_K(i) < θ;
  - K touches {m_i = θ} at a single point z with sign(t)(z_j w_l − w_j z_l) > 0.

  This holds simultaneously for any finite list of credal sets, each touching the line in at most one point, with w
  distinct from every contact point. Also (g_t)_i < 0, and g_t lies in an open cell.
- (c) **Level 0.** Suppose K lies in the edge {m_i = 0}, and write [ρ_−(K), ρ_+(K)] for its range of m_j/m_l. Take η > 0
  small and put
  - g := −e_i + η(e_j − r e_l): D_K accepts g iff ρ_−(K) > r;
  - g := −e_i + η(r e_l − e_j): D_K accepts g iff ρ_+(K) < r.

  Every credal set in a finite list with P̄(i) > 0 is rejected.

*Proof.*
- (a) m·b_θ = θ − m_i.
- (b) m·g_t = θ − m_i + t(w_l m_j − w_j m_l) vanishes at m = w. For small t, the line {m·g_t = 0} is uniformly close to
  {m_i = θ}. Sets strictly below the level stay inside, and sets reaching above it stay outside. A set touching the
  level only at z is inside iff z is, because a unique maximiser of m_i over a polygon is a vertex with both edges
  strictly descending.
- (c) On the edge, m·g has the sign of m_j − r m_l (resp. r m_l − m_j). A set with a point at m_i = P̄ > 0 gives
  m·g ≤ −P̄ + O(η) < 0. ∎

**Definition.** A selection p ↦ K_p is **graded at world i** if:
- (i) p_i < q_i ⟺ P̄_{K_p}(i) < P̄_{K_q}(i);
- (ii) for p_i > 0, K_p touches {m_i = P̄_{K_p}(i)} in a single point z_p, and p ↦ z_p is injective on each level;
- (iii) for p_i = 0, K_p lies in the edge {m_i = 0}, and ρ_−(K_p), ρ_+(K_p) are strictly increasing functions of one
  common parameter of the level.

**Lemma 4.2 (the plain family is graded at every world, for every ε ∈ (0,1); PROVED, CHECKED).**
- (i) P̄_{K_p}(i) = φ(p_i), with φ(x) = (c0+ε)x/(c0+εx), a strictly increasing bijection of [0,1].
- (ii) The contact point is z_p = ν(p⊙v_i). It determines p, because v_i > 0.
- (iii) For p_i = 0, K_p is the edge segment with m_j/m_l ∈ [r c0/(c0+ε), r(c0+ε)/c0], where r = p_j/p_l ∈ [0, ∞].

*Proof.*
- The vertex ν(p⊙v_k) has i-th coordinate p_i v_{ki}/(p·v_k), with p·v_k = c0 + εp_k.
- Compare k = i with k ≠ i: (c0+ε)(c0+εp_k) − c0(c0+εp_i) = c0ε(1 + p_k − p_i) + ε²p_k > 0. So the maximum is attained
  only at k = i, and equals φ(p_i).
- (iii) is read off the three vertices. ∎

**Corollary 4.3 (PROVED).** For the plain family:
- {p ∈ Δ : C_p accepts b_{φ(c)}} = {p_i < c} for every c ∈ (0,1);
- rotating about a point of the level splits the level at that point, on either side;
- at level 0, the two families of (c) cut the edge in a single order from either end.

`level_problems.py` checks all three statements on every point of Δ ∩ (1/n)ℤ³ (n = 7, 12; boundary and vertices
included) for ε ∈ {1/20, 3/10, 1/2, 9/10}: 992 instances, 0 failures (CHECKED).

## 5. The theorems

**Theorem 5.1 (one world, both tiers; PROVED).** Let p ↦ K_p be graded at world i; for example, the plain posterior
family for any ε ∈ (0,1). Then for every finite S ⊂ Δ there is a cell witness with
- L(C_p) = L(C_q) whenever p_i = q_i;
- L(C_p) < L(C_q) whenever p_i > q_i (p, q ∈ S).

Consequently (Lemma 2.1(a), Lemma 3.1, Corollary 3.2):
- the tie closure ~_i has no (G)-certificate;
- the stronger tier ≼*_i has no strict cycle, no (F1) and no (F2).

These hold at every closure depth, with cancelled-change composites included.

*Proof.* By Lemma 3.3 it suffices to show that every λ satisfying (★) is 0.
1. **The strict part vanishes.** Put Φ(c) := λ{p : p_i < c}.
   - Ties have equal i-coordinates and contribute nothing to Φ.
   - A strict pair with κ ≥ 0 contributes κ([q_i < c] − [p_i < c]) ≥ 0, since q_i < p_i. So Φ ≥ 0.
   - The bet b_{φ(c)} is bad at world i and accepted exactly on {p_i < c} (Corollary 4.3). By (★), Φ(c) ≤ 0, so
     Φ ≡ 0 on (0,1).
   - Let m be the least q_{k,i} over strict pairs with κ_k > 0. For c slightly above m, Φ(c) ≥ κ_k > 0. This is a
     contradiction, so every strict κ_k vanishes.

   So λ is a combination of ties: λ has zero mass on every level {p_i = c}.
2. **Every atom vanishes.** Fix a level c ∈ (0,1) and order its atoms z_{p_1}, …, z_{p_m} along the level line.
   - Rotating about a point between z_{p_k} and z_{p_{k+1}} (Lemma 4.1(b)) gives bad-at-i gambles in open cells,
     accepted exactly on {p_i < c} ∪ {p_1, …, p_k}, and, for the other sign of t, on {p_i < c} ∪ {p_{k+1}, …, p_m}.
   - By (★) and Φ = 0: λ{p_1..p_k} ≤ 0 and λ{p_{k+1}..p_m} ≤ 0.
   - The two sum to λ(level) = 0, so both vanish for every k. Hence every atom on the level is 0.
   - Level 0 is handled the same way with Lemma 4.1(c), using grading (iii). Level 1 is the single point e_i, with mass
     0.
3. So λ = 0 and F_λ = 0, and no alternative in Lemma 3.3 exists. ∎

**Theorem 5.2 (three worlds: every selected model is alone in its three-world class; PROVED).** Let the selection be
graded at all three worlds; for example, the plain posterior family for any ε ∈ (0,1). Let p ∈ Δ, and let X be any model
with X ~_i C_p for i = 1, 2, 3. Then X = C_p a.e. The same holds if X and C_p are only tied in the stronger tier
(X ≼*_i C_p ≼*_i X for all i).

In particular there is no (C)-certificate at T1 = C_u, nor at any other selected model.

*Proof.*
1. **Reduction to cells.** Let S be finite, contain p and every selected model used in the six derivations, and be
   such that 𝒞(S) refines everything in sight. For c ∈ 𝒞(S) and an advice a, put
   π_c(a) := μ(c ∩ {a_X = a})/μ(c). For every cell witness, L(X) − L(C_p) is a linear function of the penalty vector
   whose coefficients are π_c(a) − [a_{C_p}(c) = a].
2. **Linear constraint at each world.** Let W_i be the set of cell witnesses satisfying (c) and (d) of Lemma 3.1. By
   Theorem 5.1 it is nonempty. It is relatively open in the linear space V_i of penalty vectors satisfying the tie
   equalities, so it spans V_i. Lemma 3.1 gives L(X) = L(C_p) on W_i, hence on all of V_i.
3. **No contradictory advice.** The values ψ_c(×) are unconstrained in V_i. So π_c(×) = 0 for every c.
4. **The difference is a tie combination.** The remaining coefficient vector
   z := (π_c(+) − [C_p = + on c], π_c(−) − [C_p = − on c])_c
   annihilates V_i. Since V_i is the annihilator of the tie vectors, z lies in their span. So z = F_{λ_i} for a signed
   measure λ_i on S with zero mass on every level of coordinate i.
5. **One measure for all three worlds.** F is injective on measures on S: the bets of world 1 realise all initial
   segments of a total order of S (Corollary 4.3). So λ_1 = λ_2 = λ_3 =: λ, with zero marginals in all three
   coordinates.
6. **Values in [0,1].** For every oriented gamble g in an open cell,
   (δ_p + λ)(A(g)) = π_{c(g)}(acceptance of g) ∈ [0,1].
7. **Levelwise argument.** Fix a coordinate i and a level c ≠ p_i. Put β := (δ_p + λ){q_i < c} = [p_i < c] ∈ {0,1}.
   - Let P := λ{first k atoms of the level}. The rotated bets give β + P ∈ [0,1] and β − P ∈ [0,1], using λ(level) = 0.
   - If β = 0 this forces P ∈ [0,1] ∩ [−1,0]; if β = 1 it forces P ∈ [−1,0] ∩ [0,1]. Either way P = 0.
   - So every atom off {q_i = p_i} vanishes. Level 0 uses Lemma 4.1(c).
8. **Conclusion.** Doing this for i = 1, 2, 3 gives supp λ ⊆ {p}. Zero marginal gives λ = 0. So π_c is the advice of
   C_p on every cell, and X = C_p a.e. ∎

*Remarks.*
- Neither theorem uses continuity of the selection, the seeds, any threshold of a nonselected model, or the size of ε.
  They hold on all of Δ, boundary and vertices included.
- Theorem 5.2 does not merely exclude certificates. The three tie relations are jointly **rigid** at every selected
  model, even though each single O_i(C_p) is large: EE2 §2.4's level-line transports already give nonselected
  members of O_1(C_s), and §6 finds thousands of records per world.
- A single global witness at world i (one L with L(C_p) = f(p_i) for all p ∈ Δ) is neither claimed nor needed.

## 6. Exact computations (CHECKED)

All on exact cell arrangements (`arr.py`, exact rational enumeration adapted from `ee2py/cells.py`; cells merged by
column; pairs indexed by g_1 > 0).

**Additive witnesses** (`invariants.py` → `invariants.out`). Exact rational cell witnesses were obtained by LP
(HiGHS), then rounding, then exact orthogonal projection onto the tie equalities, then exact verification of every sign
and strict inequality. They were found at all three worlds, in both tiers, on:

| fragment | ε | models | active cells | cell kinds |
|---|---|---|---|---|
| hexagon R=2 at u, step 1/100 | 3/10 | 19 | 378 | {+,0}, {−,0} |
| hexagon R=3 at u, step 1/200 | 3/10 | 37 | 1239 | binary |
| hexagon R=2 at (1/5,3/5,1/5) | 3/10 | 19 | 358 | binary |
| Δ ∩ (1/6)ℤ³ (edges, vertices) | 3/10 | 28 | 1065 | {+,−}, {+,−,0} |
| hexagon R=2 at u | 1/10 | 19 | 378 | binary |
| hexagon R=2 at u, step 1/50 | 1/2 | 19 | 378 | binary |
| Δ ∩ (1/5)ℤ³ | 1/20 | 21 | 585 | ternary |

**Full closures** (`closure.py`, `closure_check.py` → `closure_check.out`). These are integer computations, saturated
over all pairs, with cancelled composites included.

| fragment | world | \|E_i(S)\| | via single-generator chains | only via cancelled composites | improving | \|E_1∩E_2∩E_3\| | realisable at a selected model |
|---|---|---|---|---|---|---|---|
| hexagon R=1 at u | each | 27 | 27 | 0 | 0 | 3 | 0 |
| hexagon R=2 at u | each | 2137 | 2099 | 38 | 0 | 47 | 0 |
| hexagon R=2 at (1/5,3/5,1/5) | 1, 2, 3 | 2451, 2541, 2451 | 2449, 2529, 2449 | 2, 12, 2 | 0 | 45 | 0 |
| hexagon R=2 at u, ε=1/10 | each | 2137 | 2099 | 38 | 0 | 47 | 0 |

The counts in the last two columns include the identity record. The nonzero three-world records are the discrete
"alternating hexagon" measures, with zero mass on every line of all three directions. They tie incoherent models with
incoherent models at all three worlds, but never touch a selected model, as Theorem 5.2 says.

The **selected part of the stronger tier** is the closure of ties ∪ {rec(C_a, C_b) : a_i > b_i}. It was computed in
full on the same fragments (6519 records per world for the R=2 hexagon at u). It has no reversed strict pair, no
improving record, and no two-way accepted record outside E_i(S). Guidance records are covered by the witnesses.

## 7. The patched family

**Proposition 7.1 (PROVED; the numbers are CHECKED from DD1 `test_geom.out`).**
- In DD1's design, (q_2)_1 = 1/3 = u_1, since d_2 = √(2/3)(0, √3/2, −√3/2). So the scheme imposes B_2 ~_1 T1.
- But P̄_{K_2}(1) = 19/30 > 8/15 = P̄_{T1}(1), and the lower probabilities satisfy P_{K_2}(1) = 1/5 < 7/30 = P_{T1}(1).
- So the patched family is **not graded** at world 1:
  - bets against 1 at odds θ ∈ (8/15, 19/30] are accepted by T1 and not by B_2, so B_2 is better there;
  - bets on 1 at odds θ ∈ (1/5, 7/30) are accepted by T1 and not by B_2, so T1 is better there.
- The imposed tie is therefore a genuine exchange, and Lemma 4.1 no longer cuts the selected models along their
  levels. Inside every bump, P̄_{K_p}(i) = (1−β)φ(p_i) + βP̄_{K_k}(i) is not a function of p_i. Theorems 5.1 and 5.2
  do not apply.

**Corollary 7.2 (PROVED).** A (G)- or (C)-certificate, or a stronger-tier violation, for a patched family must use a
selected model inside a bump. A derivation using only models outside the bumps is a plain-family derivation, and
T1 = C_u lies outside every bump.

**Exact searches** (`patched.py`, `patched_adv.py`, `patched_center.py` → `.out`). These use a rational surrogate
of DD1's design: bump centre q2 = (1/3, 1/3 + 53/1250, 1/3 − 53/1250), |q2 − q_2| < 3·10⁻⁵, ρ = 1/40, β = (1 − s²)².
This is itself a patched family in DD1's sense, and DD1 Prop 1.1 applies verbatim.

| fragment | models (in bump) | cells | witnesses | full closures |
|---|---|---|---|---|
| level line p_1 = 1/3 through u and q2 | 9 (6) | 117 | all worlds, both tiers | \|E_1\| = 291, no improving record |
| hexagon R=2 at q2, step 1/200, + u | 20 (19) | 545 | all, both | no improving record; \|∩\| = 7, none realisable |
| two hexagons + level-line points | 19 (11) | 426 | all, both | no improving record; \|∩\| = 5, none realisable |
| 3 levels across bump 2 (adversarial A) | 24 (10) | 657 | world 1, both tiers | – |
| 5 levels across bump 2 (adversarial B) | 35 (14) | 1343 | world 1, both tiers | – |
| bump-centre hexagon R=2, step 1/400 | 19 (19; β ≥ 0.846) | 536 | all, both | – |
| bump-centre hexagon R=3, step 1/600 | 37 (37; β ≥ 0.846) | 1978 | all, both | – |

Each line is CHECKED for that fragment. As evidence about the patched family it is NUMERICS. The adversarial
fragments were chosen to make the non-graded exchange bite: several level lines cut the bump where P̄(1) varies along
the level. Near the centre, β is stationary, so models on small circles coincide to leading order while their p_1
differ.

**CONJECTURE 7.3.** The patched family passes both tiers as well. A proof needs a substitute for Lemma 4.1: a family of
bad-at-i problems whose acceptance sets cut every finite S along a refinement of its p_i-levels. Inside a bump the
bets θ𝟙 − e_i cut along the levels of P̄_{K_p}(i) instead, which cross the p_i-levels.

## 8. What this means for the programme, and the nearby reachable result

1. **The audit's decision.**
   - For the plain posterior family, the imposed selected ties force neither certificate, at any depth and in either
     tier. The commitment C_p ≼_i C_q ⟺ p_i ≥ q_i is, world by world, the order by upper probability of the true world.
     It is finitely additive: every finite piece of it is an additive ranking.
   - Coordinate thresholds are therefore not refuted at the selected layer. DD1's nine forbidden configurations (far
     bumps) and EE1's exchange inequalities (EX) live entirely in the thresholds of **nonselected** models.
   - Theorem 5.1 settles EE1's N2 (the r-independent selected-layer closure: guidance and selected comparisons) for the
     plain family, which carries no seeds. That part of A_i(r) is clean for every assignment.
2. **Proposition 8.1 (finite additive separability suffices; PROVED).** Let Γ_i be any set of world-i comparisons that
   contains guidance, and let Φ_i be a set of pairs. Suppose that for every finite G ⊆ Γ_i:
   - some cell witness L satisfies L(A) ≤ L(B) for all (A ≼ B) ∈ G (with equality on two-way pairs); and
   - for each (Y, Z) ∈ Φ_i some such L also has L(Y) > L(Z).

   Then the least (IB)-closed preorder containing Γ_i has strict (G) and contains no pair of Φ_i.

   *Proof.* Lemma 3.1 and finiteness of derivations. (F2) is excluded because any respecting L satisfies
   L(X) ≤ L(Y) < L(X). ∎

   Apply this with Γ_i = guidance ∪ selected scheme ∪ caps of r ∪ seeds, and Φ_i = {(C_q, X) : q_i < r_i(X)}. Then r is
   a clean fixed point (EE1 Thm 3.1), and with strict slack EE1 Thm 2.1 yields a full system covering T1.
   - Additive witnesses satisfy EE1's exchange inequalities identically (EE1 Prop 4.2(d)).
   - The Lyapunov obstruction to additive positions (EE1 Prop 5.3) uses a whole non-atomic family of splices of one
     selected pair. A finite G sees only finitely many, and the witness may change with G.
3. **The constraint that remains (remark; imported status).** Q4.2 (BB2/CC3, PROVED at its stated status) says some
   world of any cover of T1 fails to add up. Under the hypothesis of Prop 8.1 no world has a finite obstruction. Such a
   cover is therefore necessarily of the write-up's type (M2): every finite subfamily of a world's relevant
   comparisons is additively endorsable, but no single strictly positive weight endorses all of them. On the full domain
   this uses BB2's transcription of "adds up".

   The single most important open point is accordingly: **construct strict-slack thresholds r whose world-wise
   comparisons are finitely additively separable** (Prop 8.1). This is a family of finite LPs whose witnesses must
   genuinely vary with the finite set. Theorem 5.1 is its selected-layer case.

## 9. Status table

| Item | Statement | Label |
|---|---|---|
| 2.1 | closure finitary; records of S-derivations are S-cell measurable; ternary cube form near u | PROVED; binary form CHECKED |
| 3.1–3.2 | cell witnesses are bounded strictly guiding additive rankings, (IB) for all records incl. cancelled composites; they exclude (G), (F1), (F2) | PROVED |
| 3.3 | witness exists unless a combination of allowed moves is pointwise improving | PROVED |
| 4.1 | bets against i: acceptance iff P̄(i) < θ; rotations split a level at any point; level-0 bets | PROVED |
| 4.2–4.3 | plain posterior family graded at every world, all ε ∈ (0,1) | PROVED; CHECKED (992 exact instances) |
| 5.1 | graded ⇒ for every finite S an exact additive realisation of the scheme at world i; no (G), no strict cycle, no (F1)/(F2) | PROVED |
| 5.2 | graded at all worlds ⇒ three-world tie class of every selected model is a singleton; no (C) at T1 or anywhere | PROVED |
| 6 | witnesses on 7 plain fragments (up to 37 models, 1239 cells, 4 values of ε); full closures with cancelled composites; no certificate | CHECKED |
| 7.1 | patched family not graded: B_2 ~_1 T1 with P̄(1) = 19/30 vs 8/15 | PROVED (CHECKED numbers) |
| 7.2 | any patched certificate uses a bump model | PROVED |
| 7 searches | seven patched fragments (up to 37 models, 1978 cells): exact witnesses in both tiers on all seven; full closures on three, with no certificate | CHECKED per fragment; NUMERICS for the family |
| 7.3 | patched family passes | CONJECTURE |
| 8.1 | finite additive separability of all comparisons ⇒ clean fixed point (⇒ cover with strict slack, via EE1 Thm 2.1) | PROVED |
| 8 remark | such a cover is necessarily of type (M2) (by Q4.2) | at Q4.2's imported status |
| — | T1 cover | **not obtained**; the tie test is not the obstruction |

## 10. Files (`ff1py/`)

- `arr.py`: exact cell arrangement for posterior models (adapted copy of `ee2py/cells.py`); triangular grids.
- `lin.py`: cell witnesses by LP, followed by exact rational projection and exact verification (tie tier and stronger
  tier; cells with any of +, 0, −).
- `closure.py`: exact saturation of the (IB)+transitivity closure on binary arrangements (cube form), and the
  single-generator-chain closure for comparison.
- `invariants.py` → `invariants.out`: §6 witnesses on plain fragments.
- `closure_check.py` → `closure_check.out`: §6 full closures, (G)/(C) searches, and the selected part of the stronger
  tier.
- `level_problems.py` → `level_problems.out`: Corollary 4.3 on exact grids (992 instances).
- `patched.py` → `patched.out`; `patched_adv.py` → `patched_adv.out`; `patched_center.py` → `patched_center.out`: §7.
