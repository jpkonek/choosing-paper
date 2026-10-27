# Q2 (round 22). Localization in three worlds: what closed choice forces on edges, the link-class escape, and the all-(Loc) residual

16 Oct 2026, round 22 (BRIEF13 rules; task: the global localization theorem (I) and the multi-world patch theorem
(II)). This file has two parts. **Part I** is the new note. **Part II** (after the double rule) is the earlier note
"Q2" of 15 Oct 2026 (round 12), kept verbatim because other notes cite it; a copy is in
`q2py/archive_Q2_notes_2026-10-15.md`. New results are numbered **Q2.10–Q2.19** to avoid clashes with Part II.

Labels: **PROVED** (full proof here, from results marked proved and refereed, each named with its status),
**CHECKED** (a step-by-step reading, not a re-derivation), **CONJECTURE**, **NUMERICS** (none: no statement here rests
on computation, so `q2py/` holds only the archive copy). No assumption is added; every extra hypothesis is a
hypothesis of a stated result.

Notation: R21 §1 (n = 3, U = D_{K′}, K′ = u + s(T1 − u), M, N₊, P_k, E_k, σ_k, Q_l, R_ij = Q_i ∪ Q_j, J_l, (H_U), (NC),
Λ_k, V_k, ν*_k, ρ*_k, A*); K3 §1 and K3_referee (𝔚_k, localizing families, D-localized, (E2), property (R)); L2's
names **(Loc)** / **(Loc_int)** for K3's class (S) / (S_int); N2 Part I (edge models, e_θ, E^{θ,±}, θ-Bayes,
L_θ, U_θ). A **(Loc) datum** for world k is a pair (ρ_k, D^k): ρ_k measurable on M with 0 < ρ_k < ∞ a.e., D^k a
localizing family, and ρ_kμ(δ⁻) ≤ ρ_kμ(δ⁺) for every D^k-localized relevant world-k vector δ. A function f on a
subset of U is **0-homogeneous** if f(λg) = f(g) a.e. (λ > 0), i.e. f agrees a.e. with a function of g/|g|.

---

## 0. Outcome

**(I) is NOT proved, and it cannot be proved by any argument that uses only edge structure and the bounded fixed
point. (II) is NOT proved in full; it is reduced to one precise question.** In detail:

1. **The link-class theorem (Theorem Q2.14, PROVED). Closed choice forces compatibility exactly on the visible part
   of the link class, and nowhere else.**
   - If worlds i and j are both (Loc), with any data, then every extreme edge Bayes model of (ρ_i, ρ_j) is selected.
     So the edge selection on {i, j} is the chain of superlevel sets of r_ij := ρ_j/ρ_i (nested up to ratio ties),
     and r_ij is **0-homogeneous** on R_ij (Theorems Q2.12, Q2.13). This is N2.3 for σ-finite endorsers. It is the
     three-world form of F1.2's chain monotonicity, with no additive partner and no (Nest_e) assumed.
   - Hence, if all three worlds are (Loc), on each link class Q_i the ratio of the two agreeing worlds' densities
     factorizes through world i's two edge chains: ρ_j/ρ_k = r_ij/r_ik, each factor a monotone function of one
     edge-chain coordinate. On the **visible** part V_i ∩ Q_i the same factorization holds for the bounded CA
     densities ρ*, automatically (N2.3).
   - On the **blind** part Λ_i ∩ Q_i nothing forces it. There the edge-selected models are θ = 1 models, and every
     known constraint (N2.1, N2.3, N1.2, K3.7(β′), (V1)–(V6)) sees the partners only through σ_j(ρ_j + ρ_k) (CHECKED).
2. **The competing construction is real at the level of necessary conditions (Corollary Q2.15, PROVED).** Let worlds j,
   k be (Loc), e.g. additive with integrable densities. World i is **not** (Loc) as soon as one of the following holds
   on a non-null part of Λ_i ∩ Q_i:
   - the partners' ratio ρ_j/ρ_k is not 0-homogeneous (a radial dependence is enough);
   - more generally, it is not a product of a function of x_ij and a function of x_ik;
   - or an edge selection at i is not nested modulo ratio ties.

   In configuration (V), Λ₁ ∩ Q₁ ⊇ (+,−,−) ∩ U is non-null ((V1)). So H1.2's extra requirement on (V) next to
   integrable partners ("world 1 must be ¬(Loc)"; P1.19 (V6), Q_P1) costs nothing: it is met by any choice of partner
   densities whose ratio is not 0-homogeneous on (+,−,−) ∩ U. On that region no proved constraint touches the ratio.
   This is the **positive lead** asked for. (I) is false at world 1 of any (V)-cover with such partners, if one
   exists, and the natural lift of P1.10/L2 escapes H1.2 by partner choice alone.
3. **(II) for covers in which every world is (Loc) (Theorem Q2.16, PROVED, with one open input).**
   - Enlarge each localizing family by {ρ_k > m}. Then K3.5′(c)'s residual "infinite minority mass" is **empty**, and
     K3.6's "shadowed" alternative is **empty** (Lemma Q2.10).
   - T1 is c-Bayes at an **interior** weight p̂ for the σ-finite field c = (ρ_kσ_k), whatever the sheltering
     (Q2.11(c)).
   - Every selected C_p is c-Bayes at a weight in Δ_{supp p} (σ-finite Pareto, Q2.11).
   - Every edge Bayes set B_t, t ∈ ∂Δ, is coherent, and c = h·ĉ with ĉ 0-homogeneous (Q2.13).
   - A cover must have **persistent sheltering**: for every choice of (Loc) data, some edge region R_ij carries a
     non-null joint localizing set at every depth.
   - By M0closed(a), all of this closes the case except for one input:
     **(W) a.e. interior weight is the Bayes weight of some coherent model** (equivalently (γ) for ĉ).
   - (W) would follow from upper hemicontinuity of the Bayes-weight correspondence p ↦ Γ(p) of the selection. That is
     a continuity property of p ↦ C_p which (S) is not known to give (§6.3).
4. **What remains for T1 (§7).**
   - **(S)**: Q_S, unchanged.
   - **Branch I.** All six configurations (V0), (V+), (P0), (PD), (E), (X) stay open, sharpened as follows:
     - their all-(Loc) parts reduce to (W);
     - their parts with a non-(Loc) world cannot be closed by localization, because of item 2. They need the
       field-level questions (Q_N1, L1.D) or a ranking-level argument on the blind link class.
   - **General domains (GS), (GL), (GnAv-nd), (GnAv-d)**: untouched. Q2.11–Q2.13 have no ladder version.

| | Statement | Label |
|---|---|---|
| Q2.10 | enlarged (Loc) data; K3.5′(c) residual (R-ii) empty; K3.6 "shadowed" empty; persistent sheltering forced | PROVED |
| Q2.11 | σ-finite Pareto off the localizing sets; σ-finite admissibility of T1 at an interior weight | PROVED |
| Q2.12 | σ-finite N2.3: extreme edge Bayes models of (ρ_i, ρ_j) are selected; edge chains = ratio chains | PROVED |
| Q2.13 | ratios 0-homogeneous on edge regions; c = hĉ; (γ) on ∂Δ | PROVED |
| Q2.14 | link-class theorem: factorization on Q_i, forced on V_i ∩ Q_i, free on Λ_i ∩ Q_i | PROVED (freedom: CHECKED) |
| Q2.15 | non-(Loc) criteria; the (V) escape from H1.2 | PROVED |
| Q2.16 | all-(Loc) covers: structure, and no cover under (W) | PROVED |
| Q2.17 | bounded ratios are monotone functions of σ-finite ratios on edges (transport of ratios) | PROVED |
| Q2.18 | P1.15–P1.18 transfer to a nested edge next to an (RL) partner | CHECKED |
| Q_W | does a.e. interior weight carry a coherent Bayes model in an all-(Loc) cover? | open |
| Q2.C | the three-world lift of L2.1 with non-0-homogeneous partners on Q₁ is a full system with an (NC), ¬(Loc) world | CONJECTURE |

---

## 1. Standing conventions

- **Inputs, with status.**
  - Theorem kkm (write-up, proved).
  - M1.3, the face KKM on an edge with strict (G) (R1, M1_referee §3.1).
  - K3.1, K3.5, K3.5′, K3.6, K3.7′ (R1, K3_referee).
  - H1.0, H1.1 (R1, H12_referee).
  - N2.1, N2.3, N2.3′ (R1, N12_referee §§2.1, 2.3).
  - N1.0, N1.2 (R1, N12_referee §1).
  - M0closed(a) (R2; no integrability used, H12_referee §1.4).
  - Coherent models of M_U are the D_K with K ⊇ K′, and limits in measure of coherent models are coherent
    (H12_referee §1.1).
  - L4.1 (R1).
- **Cones.** For coherent D_K, the sets D_K, P_i, E_i(D_K) are invariant under g ↦ λg (λ > 0), because U is a cone
  and P_K is positively homogeneous.
- **Edge models.** An edge model for {i, j} equals P_i on Q_k, accepts N₊, and is determined by its world-i error set
  c ⊆ R_ij. Every C_q with q ∈ [e_i, e_j] is one (N2 Part I, "Edge models"). For densities ρ_i, ρ_j > 0 on R_ij put
  r_ij := ρ_j/ρ_i. Then e_θ < 0 ⇔ r_ij > θ/(1−θ), so E^{θ,−} and E^{θ,+} have world-i errors {r_ij > s} and
  {r_ij ≥ s} with s = θ/(1−θ) ∈ [0, ∞].

---

## 2. Enlarged data: infinite minority mass disappears

**Lemma Q2.10 (PROVED).** Assume (H_U).
- **(a) Enlargement.** Let (ρ_k, D^k) be a (Loc) datum. Put D̃^k_m := (D^k_m ∪ {ρ_k > m}) ∩ M. Then (ρ_k, D̃^k) is a
  (Loc) datum and ρ_k ≤ m a.e. on M ∖ D̃^k_m.
- **(b) No minority mass.** Let every world be (Loc) with enlarged data (ρ_k, D̃^k). If for some m₀ the sets
  D̃^i_{m₀} ∩ D̃^j_{m₀} ∩ R_ij are null for all i ≠ j, then (H_U) is contradictory.
- **(c) Persistent sheltering.** Hence in a cover with every world (Loc), for **every** choice of (Loc) data there is a
  pair {i, j} with H^{ij}_m := D̃^i_m ∩ D̃^j_m ∩ R_ij non-null for every m.
- **(d) No shadows.** With enlarged data, K3.6's alternative "(shadowed)" never occurs. So for every k, every open
  mixed orthant O and every measurable W ⊆ O ∩ E_k(T1), there is m with ρ_k(W ∖ ⋃_{j∈V(W)} D̃^j_m) < ∞. A T1-wrong
  blow-up of ρ_k lives only inside the localizing sets of the worlds that disagree with k on O.

*Proof.*
- **(a)**
  - D̃^k is decreasing.
  - μ(D̃^k_m) ≤ μ(D^k_m) + μ({ρ_k > m}) → 0, since ρ_k < ∞ a.e.
  - A D̃^k-localized vector is D^k-localized, because D̃^k_m ⊇ D^k_m. So ρ_k endorses it.
- **(b)** Apply K3.5′(c) (R1) to the data (ρ_k, D̃^k). Its hypothesis (i) is the assumption. Its hypothesis (ii) is the
  sum Σ_k ∫_{D̃^k_{m₀}} Σ_{j : σ_j ≠ σ_k} ρ_j dμ + ∫_{M ∖ ⋃_k D̃^k_{m₀}} min(ρ₊, ρ₋) dμ. Bound it as follows.
  - A point with σ_j ≠ σ_k lies in R_jk. On D̃^k_{m₀} ∩ R_jk the set D̃^j_{m₀} is null by (i). So ρ_j ≤ m₀ a.e. there
    by (a).
  - Off ⋃_k D̃^k_{m₀}, every ρ_k ≤ m₀.
  - So the sum is at most 9m₀μ(M) < ∞, and K3.5′(c) gives the contradiction.
- **(c)** By (b), for every m some pair has H^{ij}_m non-null. Some pair occurs for infinitely many m. The H^{ij}_m
  decrease in m, so that pair works for every m.
- **(d)** K3.6 (R1) applies to any (Loc) data, in particular to the enlarged data.
  - Its alternative (shadowed) says that some j ∈ V(W) has ρ_j(W ∖ D̃^j_m) = ∞ for every m.
  - But ρ_j ≤ m off D̃^j_m, so ρ_j(W ∖ D̃^j_m) ≤ mμ(M).
  - Hence (sheltered) holds. ∎

*Reading.*
- K3.5′(c) left two residuals, (R-i) sheltering and (R-ii) infinite minority mass. The K3 referee (§5.3) showed (R-ii)
  disappears under Q_K3 "No". Q2.10 shows it disappears **unconditionally**: minority mass is always relocatable into
  the localizing family, because the families may be enlarged by the sets where the densities are large.
- What survives is sheltering alone. It always occurs on one edge region R_ij, at every depth.
- The sheltered set may come from the original families or from a **common blow-up** {ρ_i > m} ∩ {ρ_j > m}.

---

## 3. σ-finite Pareto and σ-finite admissibility

**Theorem Q2.11 (PROVED).** Let a ranking on M_U satisfy strict (G) and (S).
- **(a) Pareto off the localizing sets.** Let C ∈ C_L be competitive on S ⊆ {1,2,3}, and let every k ∈ S have a (Loc)
  datum, enlarged as in Q2.10(a). Put χ_k := +1 where C is correct at k and −1 where it errs. Then there is w ∈ Δ_S
  with Σ_{k∈S} w_kχ_kρ_k ≥ 0 a.e. on M. That is, C is c-Bayes at w for c = (ρ_kσ_k), ties free.
- **(b) Edge form.** If S = {i, j} and C is an edge model, then C is θ-Bayes for (ρ_i, ρ_j) with θ = w_i.
- **(c) Interior admissibility.** Assume (H_U) and that every world is (Loc). Then D_{T1} = B_{p̂} ∪ S′ with
  S′ ⊆ Z_{p̂}, for some **p̂ ∈ Δ°**, where B_t := {t·c > 0} and Z_t := {t·c = 0}. Sheltering plays no role.

*Proof.*
- **(a)**
  - Put G_m := M ∖ ⋃_{k∈S} D̃^k_m, an increasing family with ⋃_m G_m = M mod null.
  - Suppose some W ⊆ G_m has ∫_W χ_kρ_k dμ < 0 for every k ∈ S. These integrals are finite, since ρ_k ≤ m on G_m.
  - X := C △ W is regular (C is coherent, W ⊆ M), so every C ⪯_k X is relevant. Competitiveness gives k ∈ S with
    C ⪯_k X.
  - Its vector δ_k = 1_{E_kX} − 1_{E_kC} vanishes off W, hence on D̃^k_m. So it is D̃^k-localized, and (E2) gives
    ∫_W χ_kρ_k = ρ_k(δ⁺) − ρ_k(δ⁻) ≥ 0 (both finite). This is a contradiction.
  - The vector measure W ↦ (∫_W χ_kρ_k)_{k∈S} on G_m is finite and non-atomic, so its range is compact and convex
    (Lyapunov). The range contains 0 and misses the open negative orthant.
  - Separation gives w^{(m)} ∈ Δ_S with Σ_k w^{(m)}_kχ_kρ_k ≥ 0 a.e. on G_m (test W = {Σ < 0} ∩ G_m).
  - Take w^{(m)} → w along a subsequence. For fixed m₀ and all m ≥ m₀ the inequality holds on G_{m₀}, so it holds in
    the limit on G_{m₀}. Let m₀ → ∞.
- **(b)** This is N2.1(c)'s computation:
  - on Q_k, C is correct at both i and j;
  - on R_ij, χ_j = −χ_i.
- **(c)** Put D_m := ⋃_k D̃^k_m, a localizing family; every ρ_k ≤ m on M ∖ D_m.
  - A relevant comparison T1 ⪯_k Y with Y regular and Y = T1 on D_m has δ = 0 on D_m ⊇ D̃^k_m. So it is D̃^k-localized
    and (E2)-endorsed.
  - These are exactly the hypotheses of Lemma H1.1 (R1), and its step 4 uses only ρ_k > 0. ∎

*Remarks.*
- (a) is N2.1 with the purely finitely additive carriers replaced by the localizing families.
  - N2.1 needs the carriers to be avoided by an arbitrary small removal.
  - Here W simply stays off D̃_m, and the enlarged family makes all masses on W finite.
- (c) is H1.1 at three σ-finite worlds at once.
  - H1.3 needed integrable densities.
  - K3.5 needed a patch.
  - Admissibility needs neither, because T1's out-comparisons that leave D_m untouched are localized at **every**
    world simultaneously.
  - The obstruction to H1.3's conclusion is therefore not admissibility. It is (γ) (§6).

---

## 4. Edges between two (Loc) worlds: closed choice makes the selection a ratio chain

**Theorem Q2.12 (σ-finite N2.3; PROVED).** Let a ranking on M_U satisfy strict (G) and (S). Let worlds i ≠ j have
(Loc) data (any localizations; enlarge them as in Q2.10(a)), and put r := r_ij = ρ_j/ρ_i on R_ij. Then:
- **(a)** for every θ ∈ [0, 1], both E^{θ,−} and E^{θ,+} of (ρ_i, ρ_j) belong to C_L. In other words, the edge models
  with world-i errors {r > s} and {r ≥ s} on R_ij (s ∈ [0, ∞]) are selected;
- **(b)** every edge-selected C_q (q in the open edge) has world-i errors c with {r > s} ⊆ c ⊆ {r ≥ s} for some
  s ∈ [0, ∞];
- **(c)** so the edge selection is nested except inside the tie sets {r = s}. In particular (Nest_e) holds on {i, j}
  whenever every tie set {r = s} is null.

*Proof.*
- **(a)** Let X be E^{θ,−} or E^{θ,+}, with world-i errors A. X is a regular edge model in M_U.
  - M1.3 (R1) gives p ∈ [e_i, e_j] with C := C_p ⪯_i X and C ⪯_j X. Write c := E_i(C) ∩ R_ij.
  - *Vertices.* If p = e_i, then C = P_i (strict (G) and competitiveness on {i}) and c = ∅. Then C ⪯_j X with
    E_jX ∩ R_ij = R_ij ∖ A forces A null by strict (G), so X = P_i ∈ C_L. The case p = e_j is the mirror.
  - *Interior p.* C is competitive on {i, j}, so it is θ′-Bayes for (ρ_i, ρ_j) by Q2.11(b). Because ρ_i, ρ_j > 0 a.e.,
    e_θ′ − e_θ = (θ′ − θ)(ρ_i + ρ_j) has the strict sign of θ′ − θ a.e. The four cases of N2.3 give c ⊇ A or c ⊆ A:
    - θ′ ≤ θ, X = E^{θ,−}: c ⊇ {e_θ′ < 0} ⊇ {e_θ < 0} = A;
    - θ′ > θ, X = E^{θ,−}: c ⊆ {e_θ′ ≤ 0} ⊆ {e_θ < 0} = A;
    - θ′ < θ, X = E^{θ,+}: c ⊇ {e_θ′ < 0} ⊇ {e_θ ≤ 0} = A;
    - θ′ ≥ θ, X = E^{θ,+}: c ⊆ {e_θ′ ≤ 0} ⊆ {e_θ ≤ 0} = A.
  - In the first case C ⪯_i X and strict (G) at i give c = A. In the second, C ⪯_j X and strict (G) at j give
    c = A. Both models are edge models, so X = C ∈ C_L.
- **(b)** C_q is θ-Bayes for some θ (Q2.11(b)). Then {e_θ < 0} ⊆ c ⊆ {e_θ ≤ 0}, i.e. {r > s} ⊆ c ⊆ {r ≥ s} with
  s = θ/(1 − θ).
- **(c)** Two such sets with s < s′ are nested. With the same s they differ only inside {r = s}. ∎

**Theorem Q2.13 (homogeneity; PROVED).** In the setting of Q2.12:
- **(a)** r_ij is 0-homogeneous on R_ij, and so is every tie set {r_ij = s}. Only countably many tie sets are
  non-null.
- **(b)** Suppose (H_U) holds and every world is (Loc). Then c = (ρ_kσ_k) = h·ĉ, with h > 0 measurable and ĉ
  0-homogeneous: on Q_l take h := ρ_l (l the odd world), so that ĉ = (σ_l, r_{lj}σ_j, r_{lk}σ_k) there. Every Bayes set
  B_t and tie set Z_t is a cone (mod null).
- **(c) (γ) on the boundary.** In the setting of (b), B_t is coherent for **every** t ∈ ∂Δ. At p̂ (Q2.11(c)), B_{p̂} ⊆
  D_{T1} ⊆ B_{p̂} ∪ Z_{p̂}, and D_{T1} is coherent.

*Proof.*
- **(a)**
  - For θ ∈ (0, 1), E^{θ,−} is selected and hence coherent: E^{θ,−} = D_K a.e. with K ⊇ K′ (H12_referee §1.1). So
    {r > s} ∩ R_ij = E_i(D_K) ∩ R_ij a.e., which is a cone, for every s ∈ (0, ∞).
  - Let K_s be that cone for rational s, and N the null union of the sets {r > s} △ K_s. Put
    r̂(g) := sup{s ∈ ℚ₊ : g ∈ K_s}. Then r̂ is 0-homogeneous, and r = r̂ off N.
  - Tie sets are differences of such cones. They are pairwise disjoint, and μ is finite, so only countably many are
    non-null.
- **(b)**
  - Apply (a) to the three edges.
  - On Q_1 ⊆ R₁₂ ∩ R₁₃, ρ₂ = r₁₂ρ₁ and ρ₃ = r₁₃ρ₁, with r₁₂ and r₁₃ 0-homogeneous. Q₂ and Q₃ are the same.
  - So t·c = h·(t·ĉ). The sets {t·ĉ > 0} and {t·ĉ = 0} are cones.
- **(c)**
  - For t in the open edge (e_i, e_j), t·c has sign σ_i on Q_k, so B_t = P_i there. On R_ij, t·c = σ_i(t_iρ_i − t_jρ_j),
    so B_t is world-i-correct where r_ij < s := t_i/t_j, world-i-wrong where r_ij > s, and rejects on the tie cone
    {r_ij = s}.
  - Hence B_t = E^{θ,−} ∩ E^{θ,+} a.e. with θ = t_i: off the tie cone both equal B_t, and on it E^{θ,−} accepts only
    P_i and E^{θ,+} only U ∖ P_i. Both are selected (Q2.12(a)), hence coherent, D_K and D_{K″}. Then
    D_K ∩ D_{K″} = D_{co(K∪K″)} is coherent. At the vertices B_{e_i} = P_i.
  - The statement at p̂ is Q2.11(c), and T1 ∈ C_L is coherent. ∎

**Proposition Q2.17 (transport of ratios between the bounded and the σ-finite field; PROVED).** Assume (H_U) and (NC)
at worlds i, j. Let ν*_i, ν*_j be maximal endorsers with CA densities ρ*_i, ρ*_j. Put J* := {ρ*_i = ρ*_j = 0} ∩ R_ij
and r* := ρ*_j/ρ*_i ∈ [0, ∞] off J*. Suppose also that i, j have (Loc) data with ratio r = ρ_j/ρ_i. Then:
- for every s ∈ ℚ₊, ess sup r* over {r ≤ s} ∖ J* is at most ess inf r* over {r > s} ∖ J*;
- hence r* = F(r) a.e. off J* and off the non-null tie sets of r, for a nondecreasing F: [0, ∞] → [0, ∞];
- on each non-null tie set {r = s}, r* lies in [F(s⁻), F(s⁺)];
- in particular (Λ_i ∖ J*) ∩ R_ij = {r* = ∞} is a superlevel set of r, up to one tie set, and (Λ_j ∖ J*) ∩ R_ij is a
  sublevel set.

*Proof.*
- The edge model with world-i errors {r > s} is a selected C_p (Q2.12(a)).
- If p is interior, N2.1(c) (R1) makes it θ*-Bayes for (ρ*_i, ρ*_j). Off J*, e*_{θ*} ≤ 0 iff r* ≥ s* := θ*/(1−θ*) (with
  s* = ∞ at θ* = 1). So r > s ⇒ r* ≥ s*, and r ≤ s ⇒ r* ≤ s*.
- If p is a vertex, {r > s} is null or all of R_ij, and the inequality is vacuous.
- The rest is F1.2(b)'s step from a family of cut inequalities to a monotone function. The atoms of the law of r are
  exactly its non-null tie sets. ∎

*Reading.*
- Q2.12 and Q2.13 are the three-world, any-partner version of F1.2(b) ("σ-finite endorsers are monotone along the
  chain"), read in the other direction: **the selection is the ratio chain.**
- Q2.17 is the requested "transport of ratios" between the two kinds of endorser. Where both exist, the bounded CA
  ratio is a monotone reparametrization of the σ-finite one. Blind sets are then superlevel sets of the σ-finite
  ratio, which is N1.2(R)'s rigidity seen from the σ-finite side.
- None of this uses T1 ∈ C_L, (C) or (LA).

---

## 5. The link class

Recall Q_i = R_ij ∩ R_ik, where worlds j and k agree and world i is odd.

**Theorem Q2.14 (the link-class theorem; (a), (b) PROVED, (c) CHECKED).** Let a ranking on M_U satisfy strict (G) and
(S).
- **(a) Three (Loc) worlds.** If i, j, k all have (Loc) data, then on Q_i
  **ρ_j/ρ_k = r_ij/r_ik**, and r_ij, r_ik are 0-homogeneous. Each of r_ij, r_ik is, up to a nondecreasing
  reparametrization, the chain coordinate of world i's edge selection on {i, j} and on {i, k} (Q2.12(b)). So the
  partners' ratio on the link class is a quotient of monotone functions of world i's two edge chains. In particular
  it is 0-homogeneous.
- **(b) The visible part (compatibility is forced).** Assume (H_U) and (NC) at i, j, k, with maximal endorsers, and
  Λ_i ∩ Λ_j ∩ R_ij and Λ_i ∩ Λ_k ∩ R_ik null.
  - By N2.3 (R1), r*_ij and r*_ik have cones as superlevel sets, so they are 0-homogeneous ([0, ∞]-valued), by the
    proof of Q2.13(a).
  - On V_i ∩ Q_i (where ρ*_i > 0), ρ*_j/ρ*_k = r*_ij/r*_ik wherever ρ*_j + ρ*_k > 0. This is the same factorization
    through world i's edge chains, obtained from closed choice alone.
- **(c) The blind part (compatibility is not forced; CHECKED).** On Λ_i ∩ Q_i, r*_ij = r*_ik = ∞. Each of the
  following sees ρ*_j, ρ*_k (and any σ-finite partner densities) on Λ_i ∩ Q_i **only through the sign σ_j = σ_k and
  positivity**:
  - N2.1 (w_jχ_jρ*_j + w_kχ_kρ*_k ≥ 0 with χ_j = χ_k);
  - N2.3 on R_ij (e*_θ = −(1−θ)ρ*_j);
  - L4.1(γ₀) (B_q = P_j there);
  - H1.1 / L4.1.3 (p*·v with v_i = 0);
  - N1.2, K3.7(β′) (statements about Λ_i);
  - (V1)–(V6) ((V5) lives on J₂ ∪ J₃ ⊆ Q₂ ∪ Q₃);
  - the edge {j, k} (R_jk = Q_j ∪ Q_k misses Q_i).

  Inside Λ_i ∩ R_ij the edge-selected models are θ = 1 models (N12_referee §2.1), so the edge chain there is also
  unconstrained by any CA field.

**Corollary Q2.15 (when a world with (NC) fails (Loc); PROVED).** Let worlds j, k have (Loc) data. For instance, take
them additive with integrable densities w_j, w_k, with data (w_j, ∅) and (w_k, ∅). Then world i is **not** (Loc) if
any of the following holds:
- **(N0)** an edge selection at i is not nested off countably many cones;
- **(N1)** ρ_j/ρ_k is not 0-homogeneous on Q_i;
- **(N2)** ρ_j/ρ_k is not of the form A(r_ij)/B(r_ik) for monotone A, B and 0-homogeneous r's whose superlevel sets
  are the edge-selected error sets.

By Q2.14(b), (N1) and (N2) can only hold on Λ_i ∩ Q_i (under its hypotheses). (N0) can only hold inside the CA tie
sets of N2.2′.

*Proof.* If world i were (Loc), Q2.12–Q2.14(a) would apply to the three data and contradict each of (N0)–(N2). ∎

**Corollary Q2.15′ (the escape from H1.2 in configuration (V); PROVED, with one CHECKED reading).** In configuration
(V) (R21 §2), Λ₁ ⊇ M ∩ {g₁ > 0} ⊇ (+,−,−) ∩ U, a non-null part of Q₁ ((V1); L4.3, M1.2, R1).
- If worlds 2 and 3 are (Loc), in particular additive with integrable densities (H1.2's setting), and the partner
  ratio is not 0-homogeneous on some non-null part of (+,−,−) ∩ U, then world 1 is ¬(Loc) by Q2.15 (N1).
- So it escapes H1.2 automatically, and by K3.7 (R1) it is (M1) or (N).
- By Q2.14(c), no proved constraint on a (V)-cover touches the partner ratio on (+,−,−) ∩ U (CHECKED).
- Consequently:
  - H1.2's extra requirement on (V) ("world 1 must be ¬(Loc)", P1.19 (V6), R21 (V+)) is **not an independent
    obstruction**. Q_P1 reduces to Q_N2⁽³⁾ / Q_V+ for additive partners with a non-0-homogeneous ratio on (+,−,−).
  - **(I) is false at world 1 of any such (V)-cover, if one exists.** No proof of (I) can work by edge or fixed-point
    arguments alone: it would have to show that the **partners'** densities factor through world 1's edge chains on
    its blind link class.

*Reading: the competing construction, exactly.*
- World i's two edge restrictions each carry a σ-finite endorser of the F1.2 form: φ_j(x_ij)·ρ_j on R_ij and
  φ_k(x_ik)·ρ_k on R_ik (Q2.18 below, under (Nest_e) and (RL) partners).
- They are compatible on Q_i iff ρ_j/ρ_k = φ_k(x_ik)/φ_j(x_ij) there.
- Closed choice forces this on the visible part (Q2.14(b)), where the edge chains are level sets of ρ_j/ρ*_i and
  ρ_k/ρ*_i.
- On the blind part the chains are θ = 1 chains, chosen by the selection independently of the partners. Coherent edge
  models are cones, so x_ij and x_ik are 0-homogeneous. Additive partners may have any radial profile.
- So the theorem "closed choice forces compatibility" is true exactly on V_i ∩ Q_i, and its failure on Λ_i ∩ Q_i is
  exactly the failure of (Loc).

**CONJECTURE Q2.C.** The three-world lift of L2.1 / P1.10 has blocks at the e₁-ray end in (+,−,−), worlds 2 and 3
additive with densities whose ratio is not 0-homogeneous on (+,−,−) ∩ U, and the requirements (i)–(v) of L2 §7.1.
Q2.C asserts that this lift is a full three-world system on M_U (T1 ∈ C_L not required) in which world 1 satisfies
(NC) and is ¬(Loc), so in (N).
- Q2.15 makes ¬(Loc) automatic.
- What is unproved is L2 §7.1 (ii)–(v): the wedge-leak blocking, strictness, closed sections in the 2-simplex, and
  (C).

---

## 6. (II): covers in which every world is (Loc)

### 6.1 The assembly

**Theorem Q2.16 (PROVED).** Assume (H_U) and that every world is (Loc). Fix enlarged data. Then:
1. **(persistent sheltering)** some edge region R_ij has D̃^i_m ∩ D̃^j_m ∩ R_ij non-null for every m (Q2.10(c)).
   This holds for **every** choice of data.
2. **(admissibility)** T1 is c-Bayes at an interior p̂ (Q2.11(c)).
3. **(Pareto)** every C_p is c-Bayes at some w(p) ∈ Δ_{supp p} (Q2.11(a)).
4. **(homogeneity and boundary (γ))** c = hĉ with ĉ 0-homogeneous; B_t is coherent for every t ∈ ∂Δ; every extreme
   edge Bayes model is selected (Q2.12, Q2.13).
5. **(link classes)** on each Q_i, ρ_j/ρ_k = r_ij/r_ik factors through world i's two edge chains (Q2.14(a)).
6. **(the missing input)** If moreover
   **(W)** for a.e. t ∈ Δ° some coherent model is c-Bayes at t (ties free),
   then (H_U) is contradictory.

*Proof of 6.*
- c ≠ 0 a.e., so by Tonelli Z_t is null for a.e. t.
- For such t, a coherent t-Bayes model C satisfies C = B_t a.e. So (W) gives property (γ): B_t is coherent for a.e.
  t ∈ Δ°.
- c is strictly signed and measurable, and T1 is admissible at an interior weight (item 2).
- So Theorem M0closed(a) applies (R2; no integrability used, H12_referee §1.4), and contradicts (γ). ∎

So (II), for covers in which every world is (Loc), is **equivalent** to (W), i.e. to (γ) for ĉ (given items 1–5).
K3.5 proves (γ) whenever a patch exists. A patch exists whenever the enlarged localizations are pairwise compatible on
the edge regions (Q2.10(b)). So:

> **Single open question for (II), Q_W.** In a cover with every world (Loc), with sheltering on R_ij at every depth,
> can B_t be incoherent for a non-null set of t ∈ Δ°?

- "No" closes every all-(Loc) cover, in every Branch I configuration.
- "Yes" must come from sheltering, by Q2.10(b).

### 6.2 What sheltering is, after Q2.10–Q2.14

- **Where it lives.** H_m := D̃^i_m ∩ D̃^j_m ∩ R_ij. On it, T1 is right at exactly one of i, j. By Q2.10(d), the T1-wrong
  world's density is non-integrable there only inside the partner's localizing set.
- **Two sources.** Either the original localizations overlap, or there is a **common blow-up** {ρ_i > m} ∩ {ρ_j > m}.
  - In the second case r_ij is 0-homogeneous (Q2.13), so the blow-up is a blow-up of the common factor h along
    directions where r_ij is bounded above and below.
  - The patch theorem then fails for a reason that is neither (R-ii) nor a bad ratio: every model errs at i or at j on
    H_m, at infinite cost to one of them, while each world localizes there.
- **Why N1.2 / N2.3 rigidity does not close it.**
  - Those results constrain the CA blind sets Λ and the bounded ratios r*.
  - The σ-finite data are strictly positive, so N1.1's blind-target swap is vacuous for them.
  - Q2.17 says the bounded ratio is a monotone function of the σ-finite ratio. That is compatible with any common
    factor h.
- **Why the T1 geometry does not close it.**
  - Item 2 shows that the T1 geometry is compatible with sheltering: admissibility at an interior p̂ holds anyway.
  - M0closed(a) needs (γ) at a.e. interior weight. Items 2 and 4 give (γ) only at p̂ and on ∂Δ.

### 6.3 A route to (W), and where it stops

Let Γ(p) := {w ∈ Δ_{supp p} : C_p is c-Bayes at w}. It is non-empty (item 3), convex (the Bayes condition is linear in
w) and face-preserving. A face-preserving, convex-valued correspondence of Δ into itself **with closed graph** is onto
Δ. This is the standard degree / approximate-selection argument. I record it only as the route, and claim nothing
for it.

Ontoness would give (W), with the coherent model C_p itself. Closedness of the graph at (p, w) needs C_{p_n} → C_p in
measure along p_n → p. Compactness gives a coherent limit D_K of C_{p_n}, and D_K is w-Bayes. Nothing shows D_K = C_p:
(S) gives closed sections in the index, not continuity in the tested model (K1 §6.2–6.3). Taking the closure of the
graph loses either face-preservation or convexity. So the route stops exactly at **continuity of the selection in
measure at sheltered depths**.

---

## 7. Edges next to an (RL) partner: P1.15–P1.18 in three worlds (CHECKED)

**Q2.18 (CHECKED).** Let {i, j} be an edge with (Nest_e), indexed by measure as Lemma N0 / Q3.5 do on edges
(N12_referee §1.4), with chain c_b ⊆ R_ij. Let world j satisfy (RL) with density ρ_j > 0 (for instance additive). Then
P1.15(a)(b), P1.16, P1.17 and P1.18(a) hold verbatim on R_ij, with λ := ρ_jμ|_{R_ij} normalized, ≤_i for accepted
world-i vectors, and "cut pair at b" meaning an edge model C_b △ (P ∪ Q).
- *Cut moves.* If ρ_j(Q) > ρ_j(P), then ψ_j(X) < ψ_j(C_b), so C_b ⋠_j X by (RL-2). Competitiveness of C_b on {i, j}
  then gives C_b ⪯_i X.
- *Equality case and capacity.* These use only closed world-i sections along [e_i, e_j] (part of (S)) and strict (G) at
  the vertex e_j, where P_j ⪯_i X would have vector −1_S.
- *Transport and window bounds.* These are pure consequences of cut moves, chaining and disjoint sums (F1.4(i)–(iv)),
  which hold at any world with (IB) and transitivity.
- F1.2(b) transfers the same way: any σ-finite (E2)-endorser of world i is φ(x_ij)ρ_j on R_ij with φ nondecreasing.
  With Q2.12–Q2.13 this says again that ρ_j/ρ_i is a 0-homogeneous monotone function of the chain coordinate.

*Why this does not give (I).*
- Q2.18 bounds trade ratios inside windows of **each** edge chain. That is the two-world half of the heuristic for L2.C,
  now on edges.
- A (Loc) endorser of world i must, in addition, glue the two edge forms on Q_i. By Q2.15 the gluing is exactly the
  partners' factorization on Λ_i ∩ Q_i, which no window bound can produce.
- So even a full proof of L2.C on each edge would leave (I) open at every world with Λ_i ∩ Q_i non-null.

---

## 8. What remains for T1

This is R21's tree with this note's results inserted. Statuses are as in R21; this note's items are unrefereed.

**On M_U.**
1. **(S)** (some world fails (NC), with a non-(RL) partner): **Q_S**, unchanged. Nothing here applies, because (Loc)
   is not assumed and the bounded endorsers do not exist.
2. **Branch I** ((NC) at every world). The configurations (V0), (V+), (P0), (PD), (E), (X) all remain open. Each splits
   along this note's line.
   - **(a) Every world (Loc).** Here Q2.16 applies. The configuration is closed iff **Q_W** has answer No, i.e. iff
     sheltering cannot make (γ) fail at interior weights. This is a single question for all six configurations at
     once. In (V) with integrable partners, H1.2 already closes this part, which is consistent with Q2.16.
   - **(b) Some world with (NC) is ¬(Loc), i.e. in (N) or (M1)-with-(NC).**
     - (I) fails there, and by Q2.15 it fails cheaply: a non-factorizing partner ratio on the blind link class
       suffices.
     - These parts are therefore **not** closable by localization. They need what R21 already lists:
       - (V0): Q_N2⁽³⁾ (now without the ¬(Loc) clause of Q_P1);
       - (V+): Q_V+;
       - (P0): L1.D;
       - (PD), (E), (X): Q_N1[int, overlap], Q_N1[edge], Q_N1[vtx].
     - A ranking-level argument on Λ_i ∩ Q_i would also do. Q2.14(c) records that none exists yet.
   - **Sharpened inputs** for all of these:
     - every edge between two (Loc) worlds is a ratio chain with 0-homogeneous ratio (Q2.12, Q2.13);
     - bounded ratios are monotone in the σ-finite ones (Q2.17);
     - T1 is σ-finite-admissible at an interior weight whenever every world is (Loc) (Q2.11(c)).
3. **Unchanged fixable gaps** (R21 §5.7):
   - I.1(int) is closed only at [CH];
   - L1.7 needs L1.7⁰;
   - N2.5(b) must be restated per side.

**On general (LF) domains** (R21 Part B): (GS), (GL), (GnAv-nd), (GnAv-d) are untouched. Q2.11 transfers verbatim to
any domain, since it uses only competitiveness, localization and Lyapunov. Q2.12 needs the edge-model calculus of M_U:
one error grade per world, R_ij = Q_i ∪ Q_j, and coherent models that are cones. It has no ladder version. On two-sided
domains the analogue of "the selection is the ratio chain" would need N2.3 for ladders, which no one has written.

**The one-line summary.**
- On M_U, Branch I covers in which every world is (Loc) are closed iff Q_W is No.
- Every other Branch I cover has an (NC) world outside (Loc). Such worlds are unconstrained by every edge result,
  because compatibility of edge endorsers is forced only on the visible link class.

---

## 9. Dependencies, and what a referee should check

**Used** (status):
- K3.1(b), K3.5, K3.5′(c), K3.6, K3.7 (R1);
- H1.1, H1.2, H12_referee §§1.1–1.4 (R1);
- M1.3 (R1);
- N2.1(c), N2.3 (R1), N12_referee §§1.4, 2.1;
- N1.2 (R1; Q2.14(c) only);
- M0closed(a) (R2);
- Theorem kkm (write-up);
- F1.2(b) (proved in F1, refereed in F12_referee; Q2.17, Q2.18);
- P1.15–P1.18 (unrefereed, Q2.18 only);
- L2 §7.1 and P1 §7 (Q2.C only);
- R21's configuration definitions and (V1) (L4.3, M1.2, R1);
- Lyapunov's convexity theorem.

**Not used:** T1 ∈ C_L, except in Q2.10(b), Q2.11(c), Q2.16; (C) and (LA), except through (H_U) in those items;
(Nest_e), except in Q2.18; closed sections, except through M1.3 and Q2.18.

**Points to check, in order of risk.**
1. Q2.12(a), the four inclusions: they need ρ_i, ρ_j > 0 a.e. (strict sign of e_θ′ − e_θ). This is where σ-finiteness
   replaces N2.3's null-joint-blindness hypothesis.
2. Q2.11(a): the comparison C ⪯_k (C △ W) with W ⊆ G_m is D̃^k-localized at every k ∈ S **simultaneously**, because
   its vector vanishes off W.
3. Q2.13(a): scale-invariance of null sets (μ is equivalent to Lebesgue measure on U), so the null set N can be
   absorbed.
4. Q2.13(c): B_t = E^{θ,−} ∩ E^{θ,+} on edges, including the tie cone.
5. Q2.14(c) is a reading of the listed results, not a theorem that nothing constrains the partner ratio. Q2.15′'s
   "no proved constraint" rests on it.
6. Q2.10(b): the bound on K3.5′(c)(ii) uses (i) on D̃^k_{m₀} ∩ R_jk.

`q2py/`: `archive_Q2_notes_2026-10-15.md` (verbatim copy of Part II). No scripts: no statement rests on NUMERICS.

---
---

# Part II — the earlier note Q2 (15 Oct 2026, round 12), verbatim

# Q2. Conjecture N17.B′ in two worlds: the null sets of a failing world are initial segments, and certificates come in mirror pairs

15 Oct 2026, round 12, exclusion side. Labels: **PROVED** (full proof here, from the cited inputs), **CHECKED**,
**CONJECTURE**, **NUMERICS**. Terminology as in TERMFIX_RULES and the writeup (decomposable domain, U-domain M_U,
advice range). Inputs used, all refereed: P4B_referee (Lemma N0, Lemma B0, Lemma B1 with Cor N1, Lemmas DL, DR,
Lemma T, Thms E2, E3, the cut-pair reformulation of §5), N22 Lemma 1.1 / Thm 1.2, N19 Lemma R1, writeup Thm kkm
("Fact 0"). No assumption is added. No script was needed this round, so `q2py/` was not created; no proof uses NUMERICS.

---

## 0. Outcome

**Nested n = 2 (the setting of P4 §5, P4B §1).** N17.B′(2) is **not** proved in full. New structural results (LF, IS, MP)
cut the open class down considerably.

- **Theorem LF (PROVED; left-fineness).** Fix a cut a ∈ (0,1) and a non-null Z to the right of it (Z ⊆ d_a). Then
  c_a splits into finitely many slabs, and every subset Q of any of them satisfies Q ≤₁ Z. These are relevant
  comparisons. The proof uses competitiveness together with Lemma T **of the other world**. A Lebesgue-number form
  gives the "uniform Lemma DR" that P4B §8.5 asked for.
- **Corollary IS (PROVED; the null sets are initial).** World 1 fails SP^reg iff some initial segment c_a with a > 0
  is null for every endorsing charge. More precisely, let a\* := inf over endorsing charges ν of
  sup{a : ν(c_a) = 0}. Then:
  - SP₁ ⇔ a\* = 0;
  - if a\* > 0, every c_a with a < a\* is 𝓜₁-null, and every 𝓜₁-null set lies in c_{a\*};
  - some single endorsing charge is strictly positive on d_{a\*}.

  So a spread-out certificate can only export the mass of an **initial segment**. It can never isolate a set lying in
  the middle or at the right.
- **Proposition MP (PROVED; mirror pairs).** Suppose a non-null Z satisfies Z ≤₁ A_j for infinitely many pairwise
  disjoint A_j (P4's "minimal shape"; bounded overlap suffices). Then some final segment d_{b₀}, b₀ < 1, satisfies
  d_t ≤₂ A_j for all j and all t ∈ [b₀,1). So **world 2 fails SP^reg too**, with the mirror certificate.
- **Corollary MP′ (PROVED).** In such a system, neither world is complete, CP-a, or has a nonzero leading charge.
  - The open class of P4B §8.5 must therefore be inhabited at **both** worlds at once.
  - Neither world can be additive, even on a sub-family containing the base comparisons, in the way that N17.8's band
    is (Prop NS).
- **Exact surviving certificate shape (§4).**
  - It exports the mass of an initial segment c_a.
  - Its targets avoid every slab near every point (Lemma T).
  - The left-fineness comparisons do not help it.
  - In its simple form it is mirrored by a world-2 certificate exporting a final segment through the **same** targets.
  - §4.3 states exactly where the proof stops: a quantitative link between the width of Lemma T's neighbourhoods and
    the measure of the target is missing.

**Non-nested n = 2 (§5).**
- PROVED: on M_U, coherent world-1 error sets form a two-parameter lattice {σ < α} ∪ {τ ≤ β}.
- PROVED: one-dimensional KKM, and a general strict-escape lemma (Lemma G-SE) for any selection.
- Lemmas DL, DR, T, LF all need the chain. Nothing beyond G-SE is proved without nestedness. Whether (S) forces a
  nested C_L in n = 2 is **open** (CONJECTURE Q2.N).

**n = 3 (§6).** What transfers:
- G-SE, in a weakened form;
- the reduction "¬SP ⇔ an 𝓜-null set", via N22.

What breaks, all from one cause: the absence of a complementary world along a cut.
- LF uses (K) on a cut pair with **exactly one** other world. In n = 3 a cut pair's failure at world 1 is absorbed by
  either of two other worlds, and neither is forced.
- Mirror pairs become cyclic triples, with no Lemma T available for them.

---

## 1. Setting

(Nest) as in P4B §1:
- n = 2 on M_U, with strict (G), (IB), (LA), (S), (C);
- the world-1 error sets of the members of C_L form a chain {E_b : b ∈ [0,1]};
- c_b := E_b, d_b := M∖E_b, and [s,t) := E_t∖E_s ("slabs"), where M is the set of mixed problems of U.
- By Lemma N0, C_L is the chain, and (K) holds at every interior b.

World orders are the N9.4 relations ≤₁, ≤₂ on measurable subsets of M:
- they are cancellative and strictly monotone;
- world 2 compares world-2 error sets, and E₂ = M∖E₁ on mixed problems.

**Cut pairs (P4B §5, PROVED there).** For b ∈ (0,1), P ⊆ c_b and Q ⊆ d_b:
- the relevant comparison C_b ⪯₁ X with E₁X = (c_b∖P) ∪ Q is equivalent to P ≤₁ Q;
- the relevant comparison C_b ⪯₂ X with E₂X = (d_b∖Q) ∪ P is equivalent to Q ≤₂ P;
- **(K)** says: P ≤₁ Q or Q ≤₂ P.

𝔚^reg₁ consists exactly of the vectors 1_Q − 1_P for cut pairs with P ≤₁ Q. Put

  𝓜₁ := {probability charges ν on M, vanishing on null sets, with ν(P) ≤ ν(Q) for every cut pair P ≤₁ Q}.

𝓜₁ is weak\*-compact, convex and nonempty. Since it is weak\*-closed, it is also norm-closed. SP^reg₁ means that some
ν ∈ 𝓜₁ is strictly positive on non-null sets. Define 𝓜₂ in the mirror way.

**Symmetry.** Reverse the chain, b ↦ 1 − b, and swap the worlds. The hypotheses ((Nest), (Cl) at both worlds, (K),
strict (G) at both worlds) are invariant. So every result of P4B §8 (DL, DR, T, E2, E3) holds verbatim for world 2,
with c and d exchanged. In particular:

**Lemma T₂ (PROVED by symmetry from P4B Lemma T).** Let W be non-null and x ∈ [0,1]. There is η > 0 such that no
non-null Q contained in the slab (x−η, x+η) satisfies W ≤₂ Q.

*Proof.* Lemma T for world 2, with m = 1, says that there is no sequence of non-null Q_j ⊆ (x−1/j, x+1/j) with
W ≤₂ Q_j for all j. If every j admitted such a Q_j, they would form one. ∎

Lemma T₁ is the same statement for world 1.

---

## 2. Left-fineness, and why null sets are initial

### 2.1 Theorem LF (PROVED)

Let a ∈ (0,1) and let Z ⊆ d_a be non-null. There are finitely many slabs J_1, …, J_m covering c_a such that every
measurable Q ⊆ c_a ∩ J_i satisfies Q ≤₁ Z, for every i.
- Each comparison Q ≤₁ Z is a relevant comparison (a cut pair at a).
- Hence every ν ∈ 𝓜₁ satisfies ν(c_a) ≤ m·ν(Z).
- *Uniform form:* there is δ = δ(Z,a) > 0 such that Q ≤₁ Z for every Q ⊆ c_a lying in a slab of width < δ.

*Proof.*
1. For each x ∈ [0,a], Lemma T₂ (applied with W = Z) gives η_x > 0 such that no non-null Q ⊆ (x−η_x, x+η_x)
   satisfies Z ≤₂ Q.
2. The open intervals (x−η_x, x+η_x) cover the compact interval [0,a]. Take a finite subcover J_1, …, J_m, and a
   Lebesgue number δ for it. Every slab of width < δ inside [0,a] then lies in some J_i.
3. Let Q ⊆ c_a ∩ J_i.
   - If Q is null, Q ≤₁ Z by monotonicity (Q ~₁ ∅ ⊆ Z).
   - If Q is non-null, (Q, Z) is a cut pair at the interior cut a. By (K), Q ≤₁ Z or Z ≤₂ Q. The second is excluded
     by step 1. So Q ≤₁ Z.
4. For ν ∈ 𝓜₁: ν(c_a) ≤ Σ_i ν(c_a ∩ J_i) ≤ m·ν(Z). ∎

*Inputs used:*
- (K) at one interior cut;
- Lemma T for world 2, which uses (Cl) at both worlds, (K) and strict (G) at both worlds (P4B §7 table, mirrored).

*Reading.*
- This is P4B's Lemma DR made uniform: the width δ depends on Z only, not on the position x.
- It is the "left half" of Savage fineness, obtained without completeness: (K) converts world 2's inability to rank a
  concentrated set above Z into world 1's ranking of that set below Z.
- It concerns only sets to the **left** of Z. Relevant comparisons are always "left ≤₁ right", so LF bounds ν on the
  left by ν on the right. It gives no lower bound on the left. That is exactly why it does not finish the proof.

### 2.2 Corollary IS (PROVED; the 𝓜₁-null ideal is generated by an initial segment)

For ν ∈ 𝓜₁ put a₀(ν) := sup{a ∈ [0,1] : ν(c_a) = 0}, and a\* := inf_{ν∈𝓜₁} a₀(ν).
- (i) If ν ∈ 𝓜₁, then ν(Z) > 0 for every non-null Z ⊆ d_{a₀(ν)}.
- (ii) Some ν̄ ∈ 𝓜₁ has a₀(ν̄) = a\*. So ν̄ is strictly positive on non-null subsets of d_{a\*}.
- (iii) SP^reg₁ ⇔ a\* = 0.
- (iv) If a\* > 0:
  - every c_a with a < a\* is 𝓜₁-null;
  - every 𝓜₁-null set is contained in c_{a\*} (mod null).

  Hence ¬SP^reg₁ ⇔ some initial segment c_a, a > 0, is 𝓜₁-null. Equivalently, for every ε > 0 there are cut pairs
  P_k ≤₁ Q_k and λ_k ≥ 0 with

    1_{c_a} + Σ_k λ_k (1_{Q_k} − 1_{P_k}) ≤ ε  a.e.

*Proof.*
- (i)
  - Let Z ⊆ d_{a₀} be non-null, with a₀ = a₀(ν) < 1. The case a₀ = 1 is vacuous.
  - By countable additivity of μ, Z ∩ d_b is non-null for some b ∈ (a₀,1).
  - ν(c_b) > 0, since ν(c_·) is nondecreasing and b > a₀.
  - LF at the cut b gives ν(c_b) ≤ m·ν(Z ∩ d_b). So ν(Z) > 0.
- (ii)
  - Choose ν_k ∈ 𝓜₁ with a₀(ν_k) ↓ a\*, and put ν̄ := Σ_k 2^{−k}ν_k. It lies in 𝓜₁, which is convex and norm-closed,
    and the series converges in norm.
  - For a > a\*, some k has a₀(ν_k) < a, so ν̄(c_a) ≥ 2^{−k}ν_k(c_a) > 0. Hence a₀(ν̄) ≤ a\*, and so a₀(ν̄) = a\*.
  - Apply (i).
- (iii)
  - (⇐) By (ii) with a\* = 0, ν̄ is strictly positive on M = d_0. It endorses every relevant comparison, since in the
    nested case these are exactly the cut pairs (Lemma N0(ii)). So SP^reg₁ holds.
  - (⇒) A strictly positive ν has ν(c_a) > 0 for every a > 0, so a₀(ν) = 0.
- (iv)
  - For a < a\* ≤ a₀(ν), ν(c_a) = 0 for every ν.
  - If Z is non-null with Z ∩ d_{a\*} non-null, then Z ∩ d_b is non-null for some b > a\*, and ν̄(Z) > 0 by (ii).
  - The certificate form is the separation step of P4 §5.5 (CONFIRMED in P4B §5), applied to B = c_a. ∎

*Remark (relation to N22 Lemma 1.1).*
- N22 Lemma 1.1 produces *some* non-null 𝓜-null set inside any set on which every member's countably additive part
  vanishes.
- Cor IS says much more in the nested two-world case: the 𝓜₁-null ideal contains no set disjoint from c_{a\*}.
- So the "spread-out" certificates of P4B §8.5 are spread out only in their **targets** Q_k. What they export is
  always the mass of an initial segment.

### 2.3 Mirror statements (PROVED by symmetry)

- For world 2 the right-fineness theorem LF₂ holds: for Z ⊆ c_a, d_a is a finite union of slabs whose subsets are
  ≤₂ Z.
- ¬SP^reg₂ ⇔ some final segment d_b, b < 1, is 𝓜₂-null.

---

## 3. Simple certificates come in mirror pairs

### 3.1 Proposition MP (PROVED)

Let Z be non-null. Suppose Z ≤₁ A_j for j = 1, 2, …, where the A_j have bounded overlap: Σ_j 1_{A_j} ≤ r.
(These need not be relevant comparisons.) Then there is b₀ ∈ (0,1) such that, for every j and every t ∈ [b₀,1):
- d_t ≤₂ A_j;
- this is the relevant world-2 comparison C_t ⪯₂ X with E₂X = A_j.

Consequently every ν ∈ 𝓜₂ vanishes on d_{b₀}, and **¬SP^reg₂**.

*Proof.*
1. Lemma T₁ at x = 1 with Z gives η > 0 such that no non-null Q ⊆ d_{1−η} satisfies Z ≤₁ Q. Put
   b₀ := max(1−η, ½).
2. Fix t ∈ [b₀,1) and j. Consider the cut pair (P, Q) := (A_j ∩ c_t, d_t ∖ A_j) at the interior cut t.
   - Suppose P ≤₁ Q. By cancellation this is A_j ≤₁ d_t, because A_j∖d_t = P and d_t∖A_j = Q.
   - Then Z ≤₁ A_j ≤₁ d_t, with d_t ⊆ d_{1−η} non-null. This contradicts step 1.
   - So P ≰₁ Q, and (K) gives Q ≤₂ P. That is C_t ⪯₂ X with E₂X = (d_t∖Q) ∪ P = (d_t ∩ A_j) ∪ (A_j ∩ c_t) = A_j.
     In set form, d_t ≤₂ A_j.
3. For ν ∈ 𝓜₂: ν(d_t) ≤ ν(A_j) for all j. Summing over j gives J·ν(d_t) ≤ Σ_{j≤J} ν(A_j) ≤ r for all J. So
   ν(d_t) = 0. ∎

**Corollary MP-loop (PROVED).** Apply MP, then its mirror image (to W := d_{b₀} ≤₂ A_j). This gives s₀ > 0 with
c_s ≤₁ A_j for all j and all s ∈ (0, s₀]. So:
- a simple world-1 certificate with *any* exported set Z upgrades to one exporting an initial segment, with the same
  targets (consistent with Cor IS);
- a simple certificate in either world forces one in the other, through the **same** targets A_j.

**Corollary MP′ (PROVED).** Suppose a system has a simple certificate (as in MP) at world 1. Then **each** world is:
- not complete;
- not CP-a;
- without a nonzero leading charge.

*Proof.*
- World 1:
  - A complete world has a strictly positive P with B ≤₁ C ⇒ P(B) ≤ P(C) (Thm E3, CHECKED). Then P(Z) ≤ P(A_j) → 0,
    a contradiction.
  - A CP-a world has a member with countably additive density > 0 a.e. (N22 Thm 1.2), and that member endorses all of
    its comparisons. The same contradiction follows.
  - A nonzero leading charge is strictly positive and satisfies A ≤₁ B ⇒ π(A∖B) ≤ π(B∖A) (Thm E2). The same
    contradiction follows.
- World 2: the same three arguments, applied to d_{b₀} ≤₂ A_j (MP), using E2, E3 and N22 for world 2 (by symmetry). ∎

### 3.2 What this means for constructions

**Proposition NS (PROVED; no additive scaffold).** Let π be any charge ≥ 0 vanishing on null sets. Suppose world 1
accepts every cut pair that π strictly favours, i.e. π(P) < π(Q) ⇒ P ≤₁ Q, at least for cut pairs at cuts
t ∈ [b₀,1). If world 1 has a simple certificate Z ≤₁ A_j, then π(d_{b₀}) = 0.

*Proof.*
- By step 2 of MP, A_j ∩ c_t ≰₁ d_t∖A_j for t ≥ b₀. Hence π(d_t∖A_j) ≤ π(A_j ∩ c_t) ≤ π(A_j).
- So π(d_t) ≤ 2π(A_j). The A_j are disjoint (or of bounded overlap), so π(A_j) → 0 along a subsequence. Hence
  π(d_t) = 0. ∎

*Consequence.*
- N17.8's architecture, "an additive band (unanimity over densities bounded below) plus exotic patches", cannot carry
  a simple certificate.
- Its band contains the strict μ-comparisons on cut pairs, and μ(d_{b₀}) > 0.
- More generally, any world 1 in such a system must reject cut pairs of the form "tiny spread set ≤₁ almost-full
  final segment" near the right end. World 2 must reject their mirrors near the left end.
- In particular the strict comparisons of every ν₂ ∈ 𝓜₂, which (K) forces into world 1, give nothing on d_{b₀}.
  This is consistent with MP.

---

## 4. Nested n = 2: what survives, and where the proof stops

### 4.1 Exact shape of a surviving certificate (PROVED necessary conditions)

If world 1 fails SP^reg in a nested two-world system, then all of the following hold.

- **(a) What is exported.** The exported set is an initial segment c_a with a > 0 (Cor IS). For every ε there are cut
  pairs P_k ≤₁ Q_k (P_k left of the cut a_k, Q_k right of it) with 1_{c_a} + Σλ_k(1_{Q_k} − 1_{P_k}) ≤ ε. Every set
  disjoint from c_{a\*} is charged by the single endorsing charge ν̄.
- **(b) The targets are not concentrated.**
  - No non-null set is ≤₁ sets shrinking to finitely many points (Lemma T₁).
  - In particular no exported mass can be sent into a fixed small slab around any point.
- **(c) Left-fineness holds and is irrelevant.** Subsets of narrow slabs to the left of any non-null Z are ≤₁ Z (LF).
  These comparisons only bound mass on the left by mass on the right.
- **(d) Escape.** Strict escape (B1, Cor N1) and the slab-dropping lemmas DL and DR hold.
- **(e) If simple, it is mirrored.**
  - If the certificate can be taken simple (Z ≤₁ A_j with bounded overlap), then world 2 fails SP^reg through the
    mirror certificate d_t ≤₂ A_j, with the **same** targets (MP).
  - Neither world is complete, CP-a, or has a nonzero leading charge (MP′).
  - Neither world accepts all strict cut comparisons of a charge charging the far end (Prop NS).
- **(f) Charge bounds.** By (a) and §5.5 of P4 there is a charge ν̄ ∈ 𝓜₁, positive on non-null subsets of d_{a\*},
  with ν̄(c_a) = 0 for a < a\*. Integrating the certificate against ν̄ gives
  0 ≤ λ_k(ν̄(Q_k) − ν̄(P_k)) ≤ ε for every k.
  So each target Q_k is ν̄-almost as light as its source P_k, while the sources jointly cover c_a with weight ≥ 1 − ε.

### 4.2 Two remarks ((i) PROVED; (ii) a remark and an open case)

- **(i) The world-1 restriction to d_{a\*} has SP.**
  - Its endorsing charge is ν̄ restricted to d_{a\*}.
  - It endorses the cut comparisons inside d_{a\*}, by monotonicity of ≤₁ (P ∩ d_{a\*} ⊆ P).
  - So the failure is *localised*: the system restricted to the right of a\* is fine.
  - The failure is the impossibility of extending any such ν̄ to the left. That is, the exported mass of c_a is
    always absorbed by targets that every endorsing charge sees as arbitrarily light.
- **(ii) Trivial members of 𝓜₁, and the case a\* = 1.**
  - Every charge concentrated at 1⁻ lies in 𝓜₁: ν(d_b) = 1 for all b < 1, for instance a Banach-limit density at 1
    from the left. Such a ν vanishes on every c_t with t < 1, so ν(P) = 0 ≤ ν(Q) for every cut pair at a cut t < 1.
  - So 𝓜₁ ≠ ∅ is automatic and carries no information. Every ν with a₀(ν) = 1 is of this degenerate kind.
  - Nothing proved here excludes a\* = 1, i.e. that *only* such charges exist. That is the extreme form of the open
    case.

### 4.3 Where the proof stops (honest failure report)

The missing step is to show that c_a, a > 0, cannot be 𝓜₁-null. The natural attempt is to perturb ν̄ by a small charge
τ that charges c_a. The constraint is

  τ(P) − τ(Q) ≤ ν̄(Q) − ν̄(P)  for every cut pair P ≤₁ Q.

This fails exactly on cut pairs whose source P has substantial τ-mass in c_a and whose target Q is ν̄-light.

The available tools control *where* such Q can lie:
- not inside any shrinking neighbourhood of finitely many points (Lemma T₁);
- if the certificate is simple, the same targets are also small in world 2's eyes against final segments (MP).

They do not control *how much* ν̄-mass Q carries. Turning (b) into a lower bound on ν̄(Q) would need a quantitative
link between:
- the radius η in Lemma T₁ (which depends on Z and x, with no rate), and
- the measure of the target.

Closedness of sections supplies only qualitative limits, one cut at a time. Concretely:
- Lemma T₁ excludes Z ≤₁ Q_j when the Q_j shrink to points;
- it says nothing when the Q_j are *thin but spread*. Examples are slabs × thin fibres in the radial coordinate of
  M_U (a mixed problem g and 2g lie on one ray but are distinct problems), or fat-Cantor families in the chain
  coordinate.

A Vitali-type argument that would push spread targets to the right piece by piece needs disjoint receivers D_i whose LF
width δ(D_i) beats the piece width. LF supplies a width for each receiver, but with no rate. That is the same circle
P4B §8.5 identified, now with the "uniform DR" half supplied and the "rate" half missing.

**General certificates versus simple ones.** MP needs the simple shape (one exported set, bounded-overlap targets).
For a general certificate, Lemma T₁ cannot be applied comparison by comparison: the sources P_k are not the exported
set, and the chain of transfers passes through intermediate regions. So **"¬SP₁ ⇒ ¬SP₂" is open in general.** For
simple certificates it is PROVED.

### 4.4 What a counterexample (construction side) must do in n = 2 nested

All PROVED necessary conditions, combining §§2–4 with P4B §8.
1. At world 1: an initial segment c_a, a > 0, null for every endorsing charge, exported to spread-out, thin targets.
   No target family may concentrate near finitely many points.
2. If the export is simple, then world 2 must export a final segment d_b to the **same** targets. Both worlds must
   then lie in the open class: incomplete, not CP-a, no leading charge.
3. Neither world may contain the strict cut comparisons of any charge that charges the far segment (Prop NS). In
   particular the N17.8 "band + exotic patches" architecture is excluded.
4. (K) must hold for every cut pair. Near the right end, world 2 must accept "almost-full final segment ≤₂ thin spread
   set". Near the left end, world 1 must accept "initial segment ≤₁ thin spread set". In between, each cut pair must be
   accepted by at least one world, while every section stays closed.

The natural place to look is the radial (fibre) direction of M_U: targets of the form slab × thin radial set, which
Lemma T cannot see. I did not find a world with closed sections there. Every lexicographic attempt with a non-additive
"shadow" primary (primary = chain-measure of the set of rays a set meets) fails closedness at primary ties, by the
R2 Thm 7 mechanism. For example A = (whole chain) × (thin radial band) has section [0,½), which is open. Every
unanimity-of-charges attempt is CP-a, hence SP. Every strict-unanimity attempt fails closedness at its boundary.
**No construction is claimed.**

---

## 5. n = 2 without nestedness

### 5.1 The coherent error-set lattice on M_U (PROVED)

Let K′ = [α′, β′] ⊂ (0,1), with t the weight on world 2. Write the mixed problems of U as M = M⁺ ⊔ M⁻:
- M⁺ := {g ∈ U : g₁ > 0 > g₂}, with τ(g) := g₁/(g₁−g₂) ∈ (β′,1);
- M⁻ := {g ∈ U : g₁ < 0 < g₂}, with σ(g) := −g₁/(g₂−g₁) ∈ (0,α′).

The coherent members of M_U are the D_K with K = [α,β] ⊇ K′. Their world-1 error sets are

  E₁(D_{[α,β]}) = {g ∈ M⁻ : σ(g) < α} ∪ {g ∈ M⁺ : τ(g) ≤ β},  α ∈ [0,α′], β ∈ [β′,1],

and E₂ = M∖E₁.

*Proof.* For g ∈ M⁺, t ↦ (1−t)g₁ + tg₂ decreases, so D_K accepts g iff β < τ(g). Not accepting is the world-1 error.
For g ∈ M⁻ it increases, so D_K accepts g iff α > σ(g), which is the world-1 error. D_K ⊆ U iff K ⊇ K′. ∎

So E₁ is a two-parameter family, increasing in (α,β) for the product order. C_L is nested iff (α,β) is co-monotone
along it. (This is N17.8's X_{α,β}.)

### 5.2 What holds for any selection (PROVED)

**Fact 0 in one dimension.** For every regular X:
- S₁(X) := {p : C_p ⪯₁ X} and S₂(X) := {p : C_p ⪯₂ X} are closed;
- 0 ∈ S₁(X) and 1 ∈ S₂(X), by competitiveness at the vertices;
- S₁(X) ∪ S₂(X) = [0,1], by competitiveness on {1,2} at interior p.

Hence S₁(X) ∩ S₂(X) ≠ ∅ by connectedness. This is writeup Thm kkm for n = 2.

**Lemma G-SE (strict escape, any selection).** Let C_p ∈ C_L, and let X be regular with E₁X ⊋ E₁C_p (non-null
difference). Then some selected C_q satisfies:
- C_q ⪯₁ X;
- C_q ≺₂ C_p;
- C_q ⋠₁ C_p.

*Proof.*
- Take q ∈ S₁(X) ∩ S₂(X). Then E₂X ⊊ E₂C_p, so X ≺₂ C_p by strict (G), and C_q ⪯₂ X ≺₂ C_p.
- C_p is undominated, so C_q ⋠₁ C_p. ∎

In the nested case G-SE is P4's Lemma B1: q is the point φ₁(A) > b.

### 5.3 What breaks

- Lemma N0 (continuity of β, identification of C_L with the chain) uses nestedness.
- So do B0 (sections are initial segments), the cut-pair form of 𝔚^reg, DL, DR, T, and hence LF, IS and MP. All of
  them parametrise the selection by the position of a single cut.
- Without nestedness, a relevant comparison is P ≤₁ Q with P ⊆ E₁C, Q ⊆ M∖E₁C, for a lattice element E₁C. There are
  two independent "cuts", in M⁻ and in M⁺.
- The sections S₁(X) are closed but need not be intervals, so B0's φ₁ is not defined.

**CONJECTURE Q2.N.** In n = 2 on M_U, strict (G), (IB), (LA), (S) and (C) force {E₁C : C ∈ C_L} to be a chain, i.e.
(α_p, β_p) co-monotone.

If true, the nested analysis above is the whole n = 2 case. I have no proof. The natural route, a non-co-monotone
crossing p < q, combined with G-SE applied to E₁C_p ∪ E₁C_q (the lattice join, a coherent model), produces a third
selected model but no contradiction.

---

## 6. n = 3: what transfers and what breaks

**Transfers (PROVED as stated):**
- Lemma G-SE, in the form: for X with E_iX ⊋ E_iC_p, some selected C_q ⪯_i X with C_q ⪯_j X for all j. This is
  Fact 0. If moreover E_jX ⊆ E_jC_p for all j ≠ i, with one inclusion strict, then C_q ≺_j C_p at that j.
  - On M_U in n = 3, E_j is **not** M∖E_i. So "growing E_i" does not shrink the other error sets, and the second clause
    has no automatic instances. This is the first break.
- The reduction ¬SP_i ⇔ some non-null 𝓜_i-null set ⇔ ε-certificates (N22 Lemma 1.1 + separation). This is
  dimension-free.

**Breaks:**
1. **LF** uses (K) on a cut pair: when world 1 fails, world 2 must accept, and Lemma T₂ forbids that acceptance for
   concentrated sets.
   - In n = 3, competitiveness on {1,2,3} of C_p at interior p gives: C_p ⪯₁ X or C_p ⪯₂ X or C_p ⪯₃ X.
   - A world-1 failure is absorbed by world 2 **or** world 3, and the choice can vary with the concentrated set Q.
   - LF would need Lemma T at both other worlds *jointly*, i.e. no Q in a small neighbourhood with W ≤₂ Q **or**
     W ≤₃ Q. That needs a common neighbourhood, which compactness supplies.
   - But first Lemma T itself is needed at worlds 2 and 3. Its proof (DL, DR, Cor N1) runs along one chain with a
     complementary world, and both are missing along the two-dimensional selection.
2. **Mirror pairs (MP).** The step "A_j ≤₁ d_t is impossible, so world 2 accepts the mirror" turns into "world 2 or
   world 3 accepts". This gives a cyclic distribution of mirror certificates over two worlds, with no single world
   forced to fail SP.
3. **Initial segments (IS)** use the linear order of the cuts. In n = 3 the selected error sets cross (N17.3), and the
   𝓜_i-null ideal has no reason to be generated by one selected error set.

**What a proof in n = 3 would need.**
- A Lemma T at every world: no non-null set is ⪯_i-below sets that shrink to finitely many points, along a
  two-dimensional selection.
- In n = 2 this came from closedness plus strict escape along a chain.
- In n = 3 the natural analogue replaces the chain by the segment of selected models on an edge of Δ. There the third
  world is inactive (competitiveness on a two-element support), so the n = 2 machinery should run on each edge with the
  third world as a spectator.

**CONJECTURE Q2.E.** On each edge [e_i, e_j] of Δ in n = 3, the edge selection, restricted to the problems on which the
third world's error is unchanged along the edge, satisfies the hypotheses of §1, so LF, IS and MP hold there.

This would give the n = 3 analogues for comparisons out of edge models only. Interior selected models, which are the
ones the cyclic (M1) certificates of N17.3 use, would remain open.

---

## 7. Status table

| Statement | Status |
|---|---|
| Lemma T₂ (Lemma T for world 2) | PROVED (symmetry of P4B Lemma T) |
| **Theorem LF (left-fineness; uniform DR)** | **PROVED** |
| **Cor IS: ¬SP₁ ⇔ some initial segment c_a (a > 0) is 𝓜₁-null; 𝓜₁-null sets ⊆ c_{a\*}; ν̄ positive on d_{a\*}** | **PROVED** |
| Mirror statements LF₂, IS₂ | PROVED |
| **Prop MP: a simple world-1 certificate forces a world-2 certificate with the same targets** | **PROVED** |
| Cor MP-loop; Cor MP′ (both worlds incomplete, non-CP-a, no leading charge) | PROVED (MP′ uses E3, which is CHECKED, for the "complete" clause) |
| Prop NS (no additive scaffold; N17.8 architecture excluded) | PROVED |
| §4.1 necessary conditions on a surviving certificate | PROVED |
| N17.B′(2), nested, general certificates | **open** (§4.3: missing a rate in Lemma T) |
| "¬SP₁ ⇒ ¬SP₂" for general certificates | open |
| §5.1 lattice of coherent error sets; Fact 0 in 1-D; Lemma G-SE | PROVED |
| CONJECTURE Q2.N (C_L nested in n = 2) | CONJECTURE |
| n = 3: transfers / breaks (§6) | PROVED as stated; N17.B′(3) open; CONJECTURE Q2.E |
| Construction of a ¬SP world with closed sections | none found; §4.4 lists PROVED necessary conditions |

**Hypotheses added: none.** (Nest) in §§1–4 is the declared hypothesis of the nested case. §5 drops it. All inputs are
listed in the header. No NUMERICS were used.
