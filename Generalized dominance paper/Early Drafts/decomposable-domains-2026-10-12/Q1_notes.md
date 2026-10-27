# Q1 (round 21b). Incompatible edge endorsers cannot be built: gluing through the link class is forced

16 Oct 2026 (BRIEF13 rules; task: the two-edge world 1 with incompatible σ-finite endorsers, aimed at (V) of R21).
This file has two parts. **Part I** is the new note. **Part II** (after the double rule) is the earlier note "Q1" of
15 Oct 2026 (round 12), kept verbatim; a copy is in `q1py/archive_Q1_notes_2026-10-15.md`. New results are numbered
**Q1.20–Q1.26**, so they do not clash with Q1.1–Q1.10 and Q1.C1–C5 of Part II.

Labels: **PROVED** (full proof here, from results marked proved and refereed, each named), **CHECKED**, **CONJECTURE**,
**NUMERICS** (`q1py/q1_*.py`, run with `python3 -I -B` from inside `q1py/`; no proof rests on them). No assumption is
added: every hypothesis beyond the axioms is stated in the result that uses it.

Notation: R21 §1, B1 (Q_l, R_ij = Q_i ∪ Q_j, link class Q_1 = R_12 ∩ R_13), K3 §1 (𝔚, localizing families,
D-localized, (Loc) = K3's class (S), (Loc_int)), M2 §1 ((RL-1), (RL-2)), F1.2 (chain coordinate). For a measurable
weight f and a set A write f(A) := ∫_A f dμ.

---

## 0. Outcome

**No construction. The design is impossible in its natural setting, and the reason is a theorem: the gluing theorem
the brief asked for as the fallback, in a strong form.**

**Where it broke.** Step (1) asks for world 1 to be a P1/L2-type world on each of R_12 and R_13, with the σ-finite
endorsers of the two edge restrictions incompatible on Q_1, so that world 1 is ¬(Loc). Incompatibility can only
come from the two edge chains *crossing* on Q_1, and crossing chains are exactly what destroys it.
- Each edge chain lets world 1 move error freely *along its own level sets* (cut moves forced by competitiveness of
  the edge models; Lemma Q1.20). This costs nothing in the pinned potential ρ* below.
- On Q_1 the level sets of the two chains cross. So error can be moved from any point of M to any other along a
  "rook path" of level-set moves, at a cost arbitrarily close to neutral (§3).
- Strict (G) then pins every exchange rate of world 1 to a single potential ρ* (Prop. Q1.22). It forces world 1 to
  accept only ρ*-favourable trades, off the chain ends (Theorem Q1.23).

**The theorem (Q1.22–Q1.24, PROVED under (TC) of §1; (TC) holds for the linear host, Prop. Q1.26).**
- **Setting.** Worlds 2 and 3 satisfy (RL-2) with integrable densities w_2, w_3 > 0 (for instance additive with
  integral penalties). World 1 is any preorder with strict (G) and (IB). Its edge selections at e_1 are nested,
  competitive and closed. Their chain coordinates cross on Q_1 (TC).
- **(a) Pinning.** w_2/w_3 = ψ(x_3)/φ(x_2) on Q_1, with φ, ψ nondecreasing. Put ρ* := w_2·φ(x_2) on R_12 and
  w_3·ψ(x_3) on R_13. Every σ-finite endorser of world 1 is a multiple of ρ*. For the linear host with partner
  densities h|g_k|: **ρ* = h|g_1|**.
- **(b) Localized endorsement.** ρ*μ endorses every D-localized comparison of world 1 between regular models. Here D is
  an explicit localizing family that removes the chain ends. So **world 1 is (Loc)**, whatever its design.
- **(c) No cover.** With T1 ∈ C_L and the rest of (H_U), H1.2 [R1] gives a contradiction.
- **(d)** If ρ* is integrable (e.g. h ≡ 1), world 1 is (Loc_int). So Λ_∞ is null: **every blind set of world 1 is
  localizable**, and no three-world lift of L2/P1 with a non-localizable blind set exists in this class.

**Answers to the brief, item by item.**
- **(1) Two-edge world 1 with ¬(Loc).** Impossible when the partners are (RL-2) and the edges are nested and
  transverse: world 1 is (Loc) (Q1.23).
  - The brief's "key risk" is exactly what happens. The transfer chains of B1 do not even need interior models: two
    edge cut moves already carry a lifted generator's target back into its source. This gives an accepted nonzero
    vector ≤ 0 whenever the generator is ρ*-unfavourable. NUMERICS: `q1_fiber_return.out`, three placements of the
    target, all undone in 2–3 forced moves.
  - The only incompatibility that survives lives at the chain ends. The localization of H1.2 deletes it (Cor. Q1.25(c)).
- **(2) Aim at T1.** Not reached. Every T1 cover with two (RL-2) partners of one world and nested transverse edges at
  that world is excluded (Q1.24). This closes R21's **(V), origin II-a** (partners (RL)), under (Nest_e) + (TC) at
  e_1. It also closes origin I whenever the partners are (RL-2), e.g. additive.
- **Fallback (gluing theorem).** PROVED in the strong form: the two edge structures do glue on Q_1, and the glued
  potential is unique and governs every localized comparison.
  - It is the ranking-level form of Q1.C3 of Part II ("two additive worlds force the third to add up"). It is
    localized at the ends, and it needs only (RL-2) partners and nested transverse edges.
  - Unlike B1.3, it assumes nothing about world 1's own edge orders.

**Where a construction must go now (shift of aim, §6).** A cover in (V), or any non-(Loc) world next to two partners,
must use at least one of:
- partners that add up only with purely finitely additive parts at the cuts (not (RL-2));
- a non-nested edge at e_1;
- nested edges whose chains **share level sets on a non-null part of Q_1** (a "comonotone link"), where gluing has
  functional freedom.

Single open question: **Q_Q1** (§6).

| | Statement | Label |
|---|---|---|
| Q1.20 | edge cut moves are accepted at world 1 next to an (RL-2) partner | PROVED |
| Q1.21 | composition of moves; bookkeeping in ρ* | PROVED |
| Q1.22 | (a) w_2/w_3 = ψ(x_3)/φ(x_2) on Q_1; (b) φ, ψ nondecreasing; (c) σ-finite endorsers are multiples of ρ* | PROVED under (TC) (continuous case); measurable case CHECKED |
| Q1.23 | ρ* endorses every D-localized regular comparison: world 1 is (Loc) | PROVED under (TC) |
| Q1.24 | no cover of T1 with two (RL-2) partners and nested transverse edges at the third world | PROVED (Q1.23 + H1.2) |
| Q1.25 | consequences: (Loc_int) if ρ* ∈ L¹; blind sets localizable; incompatibility only at the ends; R21 (V) | PROVED |
| Q1.26 | the linear host satisfies (TC); ρ* = h\|g_1\| | PROVED (π ~ Lebesgue on G: CHECKED) |
| Q_Q1 | a non-(Loc) world next to two (RL-2) partners: needs non-nested or comonotone edges | open |

---

## 1. Setting and hypotheses

n = 3 on M_U, with U = D_{K′}, K′ = u + s(T1 − u), and μ the standard Gaussian (any finite measure with a positive
continuous density would do).

- **(H_W) World 1.** ⪯_1 is a preorder on M_U with strict (G) and (IB). By Lemma vectorform, X ⪯_1 Y iff
  1_{E_1Y} − 1_{E_1X} ∈ 𝒜_1, the set of accepted world-1 vectors.
- **(H_P) Partners.** For j = 2, 3: w_j ∈ L¹(M), w_j > 0 on M, and (RL-2): for every C ∈ C_L and regular X,
  C ⪯_j X ⇒ ψ_j(C) ≤ ψ_j(X), where ψ_j(X) := w_j(E_jX ∩ M).
  - Only (RL-2) is used. That is, w_j μ endorses every relevant comparison of world j: world j adds up with a
    *countably additive* integrable weight.
  - Additive worlds with integrable densities, and (RL) worlds, qualify.
  - For the PROVED level, w_2 and w_3 are also continuous on M.
- **(H_E) Edges at e_1.** For j = 2, 3 put C^j_t := C_{(1−t)e_1+te_j}, the edge selection.
  - The models C^j_t are in C_L and competitive on {1, j} for t ∈ (0,1). Sections are closed ((S)).
  - (Nest_e) holds on {1, j}.
  - By N1.4(a) [R1, with the N12_referee §1.4 fix] the chain c^j_t := E_1(C^j_t) ∩ R_1j has no jumps.
  - Reindexing as in F1.2 gives the **chain coordinate** x_j: R_1j → [0,1). It pushes w_j μ|_{R_1j}/w_j(R_1j) to
    Lebesgue measure. For every b ∈ (0,1) there is t ∈ (0,1) with c^j_t = {x_j < b} mod null.
  - By N1.0(b), C^j_t = P_1 = P_j off R_1j.
- **(TC) Transverse crossing on the link class.** Put χ := (x_2, x_3): Q_1 → (0,1)² and G := χ(Q_1).
  - **(TC1)** x_2 and x_3 are continuous; χ is an open map; π := χ_*(μ|_{Q_1}) is equivalent to Lebesgue measure on
    the open set G.
  - **(TC2)** G is rook-connected. Any two points of G are joined by a finite sequence in G whose consecutive points
    share their first or their second coordinate. (The sequence need not stay on segments inside G.)
  - **(TC3)** x_2(Q_2) ⊆ I_2 := proj_1 G and x_3(Q_3) ⊆ I_3 := proj_2 G.

  In words: the level sets of the 12-chain and of the 13-chain cross on Q_1, and every level set meets the crossing
  region. On M, "late in the j-chain" means large x_j.

On Q_1 put ω := w_2/w_3.

## 2. Cut moves and their composition

**Lemma Q1.20 (cut moves; PROVED).** Assume (H_W), (H_P), (H_E). Let j ∈ {2, 3} and b ∈ (0,1). Let S ⊆ R_1j ∩ {x_j < b}
and T ⊆ R_1j ∩ {x_j ≥ b} be measurable with w_j(T) > w_j(S). Then 1_T − 1_S ∈ 𝒜_1. Write S ⇒_j T.

*Proof.*
- Take t ∈ (0,1) with c^j_t = {x_j < b}, put C := C^j_t, and let X := C △ (S ∪ T) (advice toggled on S ∪ T ⊆ M).
- X is regular and lies in M_U. By N1.0(c), E_1X = (E_1C ∖ S) ∪ T. On R_1j each advice errs at exactly one of 1, j,
  so E_jX ∩ R_1j = R_1j ∖ E_1X. Off R_1j, E_jX = E_jC.
- Hence ψ_j(X) − ψ_j(C) = w_j(S) − w_j(T) < 0.
- If C ⪯_j X, then (RL-2) at C ∈ C_L gives ψ_j(C) ≤ ψ_j(X), a contradiction. So C ⋠_j X.
- Competitiveness of C on supp = {1, j} gives C ⪯_1 X, with vector 1_{E_1X} − 1_{E_1C} = 1_T − 1_S. ∎

This is F1.2's first paragraph, made three-world, with the partner only (RL-2). Neither the target's position in
the other coordinate nor its sign class matters: inside a thin band {b − η ≤ x_j < b + η}, error can be moved between
*any* two places, in either direction along the level set.

**Lemma Q1.21 (composition; PROVED).** Let E_0 ⊆ M, and for i = 1, …, N let S_i ⇒_{j_i} T_i with S_i ⊆ E_{i−1} and
T_i ∩ E_{i−1} = ∅. Put E_i := (E_{i−1} ∖ S_i) ∪ T_i. Then 1_{E_N} − 1_{E_0} ∈ 𝒜_1.

*Proof.* Let X_i be the regular model with E_1X_i ∩ M = E_i. By (IB), X_{i−1} ⪯_1 X_i. Transitivity. ∎

*Bookkeeping.* If ρ* = w_2φ(x_2) on R_12 (as in Q1.22), and S, T lie in a band {x_2 ∈ J} with w_2(T) = (1+η)w_2(S),
then ρ*(T)/ρ*(S) ≤ (1+η)·sup_J φ/inf_J φ. The same holds for j = 3 with ψ. So a move *along* a level set is
ρ*-neutral up to the oscillation of φ (or ψ) on J and the slack η. A move *across* level sets (J long) is
ρ*-favourable when φ is nondecreasing.

## 3. Pinning: the two edge structures glue, uniquely

**Proposition Q1.22 (PROVED; continuous w_j and (TC)).** Assume (H_W), (H_P), (H_E), (TC).
- **(a)** ω is constant on the fibres of χ. There are continuous φ: I_2 → (0,∞) and ψ: I_3 → (0,∞) with
  **ω = ψ(x_3)/φ(x_2) on Q_1**, unique up to a common positive factor.
- **(b)** φ and ψ are nondecreasing. Put **ρ* := w_2·φ(x_2) on R_12 and w_3·ψ(x_3) on R_13**. The two definitions agree
  on Q_1, by (a). ρ* is continuous, positive and finite on M, and it is defined on Q_2 and Q_3 by (TC3).
- **(c)** Every measurable ρ with 0 < ρ < ∞ a.e. on M that endorses (E2) all relevant comparisons of world 1 out of
  edge-selected models equals cρ* a.e. on M, for a constant c > 0. The same holds for D-localized ones, for any
  localizing D.

*Proof.*
- **Rook cycles.** Let z^0, z^1, …, z^N = z^0 be a closed rook cycle in G whose steps alternate: a **13-step** keeps
  the second coordinate, a **12-step** keeps the first. Pick g^i ∈ Q_1 with χ(g^i) = z^i (g^N = g^0). Let the first
  step be a 13-step; the other case is symmetric.

  *Claim:* Π := ∏_{i odd} ω(g^i) / ∏_{i even, 0 < i ≤ N} ω(g^i) ≥ 1.
  - Suppose Π < 1, and fix η > 0 with Π(1+η)^{4N} < 1.
  - Choose open neighbourhoods V^i ∋ g^i in Q_1 on which w_2 and w_3 vary by a factor ≤ 1+η. They are non-null, and
    each χ(V^i) is an open neighbourhood of z^i (TC1).
  - Every corner set {x_2 ≶ z^i_1} ∩ {x_3 ≶ z^i_2} ∩ V^i is open and non-null.
  - Take S^0 ⊆ V^0 ∩ {x_3 < z^0_2} ∩ {x_2 ≥ z^0_1} of small mass. It is on the source side of the first 13-step and the
    target side of the last 12-step.
  - Step i (from z^{i−1} to z^i, keeping coordinate k of the two equal coordinates, cut b := that common value):
    choose T^i ⊆ V^i on the target side of this cut and the source side of the next one, disjoint from everything
    used so far. Take w_j(T^i) = (1+η)w_j(T^{i−1}) (T^0 := S^0), with j = 3 for 13-steps and j = 2 for 12-steps.
    This is possible by non-atomicity when S^0 is small.
  - Converting w_3-mass to w_2-mass on V^i costs a factor ω(g^i)^{±1}(1+η)^{±1}. So the last step deposits
    w_2(T^N) ≤ Π(1+η)^{4N}·w_2(S^0) < w_2(S^0), and T^N can be taken inside S^0.
  - Lemma Q1.21 (E_0 = S^0) gives 1_{T^N} − 1_{S^0} ∈ 𝒜_1: a nonzero vector ≤ 0, against strict (G).

  Running the cycle backwards gives Π^{−1} ≥ 1. So **Π = 1 for every alternating rook cycle**.
- **(a)**
  - The degenerate cycle g^0 → g^1 → g^0 with χ(g^0) = χ(g^1) (a 13-step, then a 12-step) gives
    ω(g^0) = ω(g^1). So ω = Ω∘χ, and Ω is continuous on G (χ continuous and open, ω continuous).
  - Let Γ be the bipartite graph with vertex sets I_2, I_3 and one edge (α, β), of weight log Ω(α, β), for each
    (α, β) ∈ G. Γ is connected (TC2).
  - Every cycle of Γ is an alternating rook cycle in G, so its alternating weight sum is 0.
  - Hence log Ω(α, β) = g(β) − f(α) for functions f, g, unique up to a common additive constant. Put φ := e^f and
    ψ := e^g. They are continuous: φ(α) = ψ(β)/Ω(α, β), with β fixed and α in an open interval.
- **(b)**
  - Suppose α < α′ in I_2 with φ(α) > φ(α′). Pick z = (α, β) and z′ = (α′, β′) in G, with small neighbourhoods V, V′
    of preimages.
  - The cut move S ⇒_2 T at b ∈ (α, α′) (S ⊆ V ∩ {x_2 < b}, T ⊆ V′ ∩ {x_2 ≥ b}, w_2(T) = (1+η)w_2(S)) has
    ρ*(T)/ρ*(S) ≤ (1+η)^3 φ(α′)/φ(α) < 1, by the bookkeeping.
  - Return from z′ to z along a rook path (TC2). Each step is ρ*-neutral up to a factor (1+η)^3 (bookkeeping;
    φ and ψ are continuous, so their oscillation on small neighbourhoods is small).
  - For η small, the deposit in S has ρ*-mass < ρ*(S). As above, strict (G) fails. Likewise for ψ.
- **(c)**
  - F1.2(b) runs verbatim on each edge, with Lemma Q1.20 in place of (K). It needs only cut moves and property (R).
    It gives ρ = w_2φ̃(x_2) a.e. on R_12 and ρ = w_3ψ̃(x_3) a.e. on R_13, with φ̃, ψ̃ positive and finite. For
    D-localized endorsement, choose the cut-move targets off D_m, as in H1 §1 and N1.6(b).
  - On Q_1, ψ̃(x_3)/φ̃(x_2) = ω = ψ(x_3)/φ(x_2) a.e. So u(α) := φ̃/φ(α) equals v(β) := ψ̃/ψ(β) for Lebesgue-a.e.
    (α, β) ∈ G (TC1).
  - On each open box in G both are a.e. constant, and rook-connectivity makes the constants equal. So ρ = cρ* on
    R_12 ∪ R_13 = M. ∎

*Reading.* The edge-12 restriction alone allows any w_2φ̃(x_2) with φ̃ nondecreasing (F1.2); this is the large
two-world family that P1.14 and L2.5 tune. The edge-13 restriction allows any w_3ψ̃(x_3). On the link class the two
families meet along a single ray, fixed by the **partners** (by ω), not by world 1. The cycle identity Π = 1 is the
link-class analogue of the corner holonomy of write-up §4: around every rook rectangle the partners' exchange rates
compose exactly to 1, or strict (G) fails at world 1.

## 4. Localized endorsement: world 1 is (Loc), whatever it is

**The localizing family.** Let (q_k) enumerate the rationals in (0,1), and let B_{k,m} ⊆ (0,1)² be the union of the
two strips |α − q_k| < 2^{−k−m} and |β − q_k| < 2^{−k−m}. Put D_m := M ∩ (A_m ∪ B_m ∪ C_m), where:
- A_m := (R_12 ∩ {x_2 ∉ [1/m, 1−1/m]}) ∪ (R_13 ∩ {x_3 ∉ [1/m, 1−1/m]}). These are the chain starts and ends.
- B_m := χ^{−1}(⋃_k B_{k,m} ∪ {z ∈ G : dist(z, ∂G) < 1/m}) ∩ Q_1, together with
  Q_2 ∩ {dist(x_2, ∂I_2) < 1/m} and Q_3 ∩ {dist(x_3, ∂I_3) < 1/m}.
- C_m := {ρ* > m}.

D_m decreases. Its measure tends to 0: the strips have total width ≤ 4·2^{−m}, the marginals of π are absolutely
continuous, x_j ∈ (0,1) a.e., and ρ* < ∞. So D is a localizing family. (Removing thin neighbourhoods of all rational
level lines is allowed: H1.2 accepts any localizing family.)

**Theorem Q1.23 (PROVED; hypotheses of Q1.22).** Let X ⪯_1 Y with X, Y regular, W := E_1Y ∖ E_1X and
Z := E_1X ∖ E_1Y, and let W ∩ D_m = ∅ for some m. Then ρ*(Z) ≤ ρ*(W) in [0, ∞]. Hence ρ*μ endorses (E2) every
D-localized relevant comparison of world 1: **world 1 is (Loc)**.

*Proof.* Suppose ρ*(W) < ρ*(Z). (ρ*(W) ≤ m·μ(M) < ∞, since W misses C_m.) Fix ε > 0 with (1+ε)ρ*(W) < ρ*(Z).
- **Shrink Z.** Choose m′ ≥ m and Z_0 ⊆ Z ∖ D_{m′} with (1+ε)ρ*(W) < ρ*(Z_0) < ∞. This is possible because D_{m′}
  decreases to a null set.
  - The model X_0 with E_1X_0 := E_1X ∖ (Z ∖ Z_0) satisfies X_0 ⪯_1 X by (G), so X_0 ⪯_1 Y. Hence
    1_W − 1_{Z_0} ∈ 𝒜_1.
  - By (IB) it is accepted between the regular models X′, Y′ with E_1X′ ∩ M = Z_0 and E_1Y′ ∩ M = W.
  - The free room is M ∖ W. It contains Z_0 and the strip sets χ^{−1}(⋃_k B_{k,m′}) ∩ Q_1, since W, Z_0 ⊆ M ∖ D_{m′}.
- **Good region.** W, Z_0 ⊆ K := M ∖ D_{m′}.
  - On K, χ takes values in the compact set G′ := {z ∈ G : dist(z, ∂G) ≥ 1/m′} ∩ [1/m′, 1 − 1/m′]².
  - x_2(K ∩ Q_2) and x_3(K ∩ Q_3) lie in compact subsets of I_2 and I_3.
  - φ and ψ are positive and uniformly continuous on the relevant compact sets. Fix η > 0 and h > 0 such that φ and
    ψ oscillate by a factor ≤ 1+η on every interval of length 2h there.
- **Cells and routes.**
  - Partition K into finitely many cells, each inside one sign class: Q_1-cells with χ-image in a box of side < h,
    Q_2-cells with x_2-image in an interval of length < h, Q_3-cells likewise in x_3.
  - For each W-cell K_i and each Z_0-cell K_l, fix a rook route in G from χ(K_i) to χ(K_l). A Q_2-cell starts with a
    12-step into Q_1, which (TC3) permits; Q_3-cells use 13-steps.
  - Perturb the interior turning points so that each has a rational coordinate (G is open). There are finitely many
    routes and stops; let P be the maximal route length.
  - Around each stop z, the set of points of χ^{−1}(strip of its rational coordinate) that lie on the target side of
    the incoming cut and the source side of the outgoing cut is open and non-null (TC1). It is free. Shrink it so
    that φ and ψ oscillate by ≤ 1+η on it.
- **Plan.**
  - Split each W ∩ K_i by Lyapunov into pieces W_{il} with ρ*(W_{il}) = ρ*(W ∩ K_i)·ρ*(Z_0 ∩ K_l)/ρ*(Z_0).
  - Split each piece further into sub-pieces small enough to fit every stop region of its route.
  - Move the sub-pieces **one at a time** along their routes. Each step is a cut move (Lemma Q1.20), with target mass
    (1+η) times the source mass in the step's measure. A sub-piece reaches Z_0 ∩ K_l before the next one starts, so
    the stops are free again.
  - First and last steps: cut at the edge of the cell's interval (e.g. b := inf x_2 of a Z_0-cell, with the last
    stop just below b). These steps are ρ*-neutral up to (1+η)^3. So is every intermediate step.
- **Count.**
  - Each sub-piece arrives with ρ*-mass ≤ (1+η)^{3(P+1)} times its own. Choose η with (1+η)^{3(P+1)} < 1+ε.
  - Then the total deposit Z_1 into each Z_0 ∩ K_l has ρ*(Z_1 ∩ K_l) < ρ*(Z_0 ∩ K_l), so it fits, and Z_1 ⊊ Z_0.
  - Lemma Q1.21 gives 1_{Z_1} − 1_{Z_0} ∈ 𝒜_1 (from X′): an accepted nonzero vector ≤ 0, against strict (G).
- **Conclusion.** For a D-localized relevant comparison δ ∈ 𝔚_D, δ⁺ = W and δ⁻ = Z. ∎

No closedness is used beyond N1.4(a). No property of world 1 is used beyond preorder, strict (G) and (IB). No
interior selected model is used.

## 5. Consequences

**Corollary Q1.24 (no cover; PROVED).** Assume (H_U) on M_U for T1. Suppose that, for some world i (say i = 1), the
two partners satisfy (H_P), and the edges of i satisfy (H_E) and (TC), with continuous densities. Then (H_U) is
contradictory.

*Proof.* Q1.23 gives ρ_1 := ρ* with 0 < ρ* < ∞ on M, endorsing every D-localized relevant comparison of world 1.
Worlds 2 and 3 have integrable w_j > 0 endorsing all their relevant comparisons ((RL-2)). These are exactly the
hypotheses of Theorem H1.2 [R1, H12_referee]; its proof uses only regular comparisons. ∎

**Corollary Q1.25 (PROVED; hypotheses of Q1.22, no target needed).**
- **(a)** World 1 is (Loc), with the pinned ρ*.
- **(b)** If ρ* ∈ L¹(M), world 1 is (Loc_int). So Λ_∞ is null (K3.1(e)): every blind set of world 1 is localizable,
  and is killed by removing thin sets.
  - In particular, a three-world lift of L2 or P1 (non-localizable blind set Λ_∞ = c_a, or Λ = M with a σ-finite
    non-integrable endorser) is impossible for partners with integral penalties and the linear host. There
    ρ* = |g_1| (Q1.26).
- **(c) Incompatibility lives only at the ends.** Let ρ^{12} be an a.e.-finite endorser of the edge-12 relevant
  comparisons, and ρ^{13} one of the edge-13 ones. By F1.2, ρ^{12} = w_2φ̃(x_2) and ρ^{13} = w_3ψ̃(x_3). They glue on
  Q_1 iff both are multiples of ρ* there (Q1.22(c)).
  - So the families can be incompatible only through comparisons that ρ* does not endorse. By Q1.23 these put new
    errors into every D_m, i.e. at the chain ends or on the thin rational strips.
  - The localization in H1.2 deletes exactly such comparisons. The brief's mechanism is therefore invisible to H1.2:
    it cannot produce the ¬(Loc) that (V) needs.
- **(d) R21.**
  - (V), origin II-a (partners (RL)): excluded under (Nest_e) + (TC) at e_1. More generally, by Q1.24 directly (M2.6′
    is not needed), every T1 cover in which two worlds are (RL-2) and the third has nested transverse edges is excluded.
  - (V), origin I, with partners (RL-2) (e.g. additive): excluded likewise.
  - Partners that add up only with essential purely finitely additive parts are **not** covered: Q1.20 needs (RL-2)
    at the cut. With D^{ν*_j}-localized cut moves, Q1.22–Q1.23 still make world 1 (Loc) (CHECKED: choose the
    sources off the partners' carriers D^{ν*_j}_m, which K3.1(b) provides). But the exclusion then needs a σ-finite
    multi-world H1.3, which is not proved (H1 §4, scope remark).

**Proposition Q1.26 (the linear host satisfies (TC); PROVED, with π ~ Lebesgue CHECKED).** Take
C^j_θ := U ∩ {(1−θ)g_1 + θg_j > 0} = D_{co(K′ ∪ {(1−θ)e_1+θe_j})}. These are the Bayes edge models of every field
c_k = h·g_k, h > 0. Let w_j be continuous, positive and integrable. Then:
- **(i)** On R_1j the world-1 error set of C^j_θ is {r_j < θ/(1−θ)}, where r_j := |g_1|/|g_j|. So the chains are
  nested, and x_j = F_j(r_j) with F_j(r) := w̄_j(R_1j ∩ {r_j < r}).
  - F_j is a continuous increasing bijection (0,∞) → (0,1): the slabs {r < r_j < r′} ∩ Q_1 are non-empty open sets,
    and the level sets are null cones.
- **(ii)** In the charts (−1, s, t) of (−,+,+) and (1, −s, −t) of (+,−,−) (s = 1/r_2, t = 1/r_3), Q_1 ∩ U becomes
  D^− := {min_{q∈K′}(−q_1 + q_2s + q_3t) > 0} and D^+ := {min_{q∈K′}(q_1 − q_2s − q_3t) > 0}.
  - These are disjoint, open and convex. D^− projects onto all s > 0 and all t > 0; D^+ projects onto
    s ∈ (0, min_q q_1/q_2).
  - χ is a homeomorphism of each chart region onto its image and is constant along rays, so it is continuous and open.
  - The image measure has a positive continuous density (CHECKED; Gaussian density and C¹ maps F_j with F_j′ > 0).
- **(iii)** Each of χ(D^±) is open and connected, hence rook-connected (staircases). A single 12-step joins them,
  since their s-projections overlap. So (TC2) holds.
- **(iv)** proj_1 G = F_2((0,∞)) = (0,1) ⊇ x_2(Q_2), and likewise for x_3. So (TC3) holds.
- **(v)** For w_j = h|g_j| (any continuous h > 0 with h|g_2|, h|g_3| integrable): on Q_1, ω = |g_2|/|g_3| = r_3/r_2.
  So φ(x_2) = r_2 and ψ(x_3) = r_3 up to a common factor, and **ρ* = h|g_1|**.

NUMERICS (`q1_tc_linear.out`; ε = 0.3, s = 0.9, a 241×241 log-grid in (s, t)): both regions non-empty; D^− meets
every grid line; the s-projections overlap; the grid set G has a single rook component.

**Remark (measurable densities; CHECKED).** For merely measurable w_j and x_j, the proofs run with Lebesgue density
points instead of continuity. Neighbourhoods V^i become sets on which ω lies within a factor 1+η of its approximate
value, and the rook identities hold for a.e. cycle. I have not written this out.

**Remark (general hosts; a reading, no claim).**
- For arbitrary nested coherent edge chains, (TC) can fail only where the 12-chain and the 13-chain **share level
  sets on an open part of Q_1**. In the chart (−1, s, t), the level sets are the zero curves of
  min_{p∈K}(−p_1 + p_2s + p_3t). A shared piece means that both edge credal sets have a common active extreme point
  off both edges.
- Where an edge point of K is active, the level sets are the lines r_j = const, as in the linear host, and they cross.
- On a comonotone part H, the loops force ω to be constant along common fibres, and gluing has a free function. That
  is the only place left for an incompatible design.

## 6. What the brief's design does in the class covered, and where to go

**The lifted generators, concretely (NUMERICS, `q1_fiber_return.out`).** Linear host, h ≡ 1, so ρ* = |g_1|,
w_2 = |g_2|, w_3 = |g_3|.
- Source P is a cell early in the 12-chain, in (−,+,+). The target B has w_2(B)/w_2(P) = 1.7·10⁻³, a vanishing-ratio
  L2-type trade, and ρ*(B) = ½ρ*(P).
- **B at the 12-end in Q_1** (plane g_2 = 0). One 13-cut along t ≈ 4 to s ≈ 3.03, then one 12-cut at s = 3.02 into P.
  The deposit is a proper subset of P with ρ* = 0.516ρ*(P).
- **B at the 12-end in Q_2.** First a 12-cut into Q_1 along s ≈ 0.01, then as above. Deposit 0.572ρ*(P).
- **B near the e_1 ray in (+,−,−)** (where E1.3 places L2 §7.1's blocks). A 13-cut along t ≈ 0.01 into (−,+,+), then
  a 12-cut. Deposit 0.630ρ*(P).
- In each case the net vector 1_{deposit} − 1_P is accepted, nonzero and ≤ 0.

The generator is never "blocked": the room it would need to be blocked from is the whole level set, and level sets of
the other chain cross it.

**Pinning numerics (`q1_loops.out`).** Rook rectangles in (−,+,+) with cells of width 0.002:
- product-form ω (integral penalties): both orientations return 1.028 (= 1 + O(cell width));
- non-product ω (w_2 = |g_2|(1 + β|g_2||g_3|/|g|²), β = 0.5, −0.5, 2): one orientation returns 0.885, 0.824 and 0.687
  respectively, i.e. strict (G) fails, as Q1.22(a) says.

**Shift of aim.** The incompatibility idea is right in spirit but in the wrong place. A world can fail (Loc) next to
two countably additive partners only if its link class is not swept by two crossing families of forced level-set
moves. The three escapes are listed in §0. The most concrete is the **comonotone link**: nested edge chains at e_1
that share their level sets on a non-null part H of Q_1. There the two edge structures form a single two-world
chain, and a P1/L2-type structure could live on it. Q1.22–Q1.23 still apply on the transverse remainder, so the
design must keep every unendorsed trade inside H's chain and its ends.

**Single open question Q_Q1.** Is there a full three-world system on M_U (strict (G), (IB), (LA), (S) with closed
sections for every model, (C)), with worlds 2 and 3 satisfying (RL-2), in which world 1 is not (Loc)?
- By Q1.23, such a system must have, at e_1, a non-nested edge, or nested chains that fail (TC). Under (Nest_e), the
  failure must be a comonotone part of Q_1, by the reading above.
- **"No"** closes (V) with (RL-2) partners outright (via H1.2), including origin II-a, with no (TC) hypothesis.
- **"Yes"** is the template a (V) cover must extend; T1 ∈ C_L is still to be added.

## 7. Dependencies, risk points, files

**Used.**
- Lemma vectorform; competitiveness on supp p; N1.0(b),(c) and N1.4(a) [R1; N12_referee §1.4 fix].
- F1.2 (reindexing; part (b) for Q1.22(c)); K3 §1 and K3.1(b),(e) [R1]; M2 §1 ((RL-2)).
- H1.2 [R1] (Q1.24 only); Lyapunov.
- **Not used:** interior selected models, (C), (LF), (LA) beyond C_L ≠ ∅, any property of world 1 beyond preorder,
  strict (G), (IB).

**Not refereed.** Points to check, by risk:
1. Q1.23's routing. Stops must be free, which is why the rational strips are in D_m and pieces travel one at a time.
   The first and last cuts must be placed at cell edges.
2. Q1.22's cycle argument: the corner sets V^i ∩ {source side} ∩ {target side} are non-null, which uses that χ is open.
3. Q1.20: C^j_t ∈ C_L at every interior t (it is selected), and N1.4(a) gives every cut b ∈ (0,1).
4. Q1.22(c): F1.2(b) on an edge with D-localized cut moves.
5. Q1.26(ii): openness of χ and π ~ Lebesgue.

`q1py/` (new files; the old `band_exotic.py/.out` are untouched; run with `python3 -I -B` from inside `q1py/`):
- `q1_common.py`: charts, the linear host, Gaussian cone masses (C1 = 2(2π)^{−3/2}).
- `q1_fiber_return.py` (+ `.out`): the explicit 2–3-move return chains of §6.
- `q1_loops.py` (+ `.out`): rook loops, product versus non-product ω.
- `q1_tc_linear.py` (+ `.out`): (TC) for the linear host on a grid.
- `archive_Q1_notes_2026-10-15.md`: verbatim copy of Part II.

---
---

# Part II — the earlier note Q1 (15 Oct 2026, round 12), verbatim

# Q1. Does a world failing SP^reg exist inside a full system? (construction side)

15 Oct 2026, round 12 (BRIEF11, task A, construction side). Labels: **PROVED** (full proof here), **CHECKED**
(proof complete up to a cited result or a routine verification sketched here), **CONJECTURE**, **NUMERICS**
(scripts in `q1py/`, run with `python3 -I`; no proof depends on them). No assumption is added to the framework;
every hypothesis beyond the axioms is stated in the result that uses it.

Terminology follows termfix/TERMFIX_RULES.md: the U-domain M_U is the class of evaluable models D ⊆ U = D_{K′}
(measurable); this restricts only which models are evaluated.

---

## 0. Outcome

**No construction.** I did not find a full system (strict (G), (IB), (LA), (S) with closed sections for every
model, (C), (LF) at a target) with a world failing SP^reg, for any target or any n. Every attempt broke at one of
two places, always the same two: **closed sections at the non-additive world**, or **an edge of the simplex**,
where the system restricts to a two-world system and the two-world exclusions apply.

**What was proved instead** (details in §§2–5):

1. **(Q1.2, PROVED) ¬SP^reg is compatible with every axiom except closed sections at one world.** In n = 2 on
   M_U, for any interval target: world 2 additive, world 1 = (band cone) ∪ (exotic cones generated by
   c_a ≤₁ A_j for a disjoint spread family A_j). All of strict (G), (IB), (LA), competitiveness, undominatedness,
   (C), (LF), closed world-2 sections hold, and ¬SP^reg₁ holds. The **only** failure is a world-1 section of the
   form [0, β) (Q1.3, exact). This makes P3's compactness remark concrete: the failure of SP^reg is decided
   entirely by (R5).
2. **(Q1.4, PROVED) Mirroring.** Under (Nest), n = 2: if a fixed non-null Z is ≤₁ every member of a pairwise
   disjoint sequence A_j (a spread certificate, Lemma T's open case), then world 2 fails SP^reg too, with a
   certificate based at a right slab: d_{1−h} ≤₂ P_j for disjoint P_j, for all small h. Consequently
   (Q1.5) a spread certificate at one world is impossible whenever the other world satisfies SP^reg; in
   particular **when the other world is additive** (this is where attempt 1 had to fail), CP-a, lexicographic with
   charge levels, or complete. A counterexample to N17.B′(2) of star shape must fail SP^reg at **both** worlds,
   in mirror-image form.
3. **(Q1.7–Q1.9, CHECKED) Edge transfer to n ≥ 3.** On each edge [e_i, e_j] of Δ the selected models agree with
   P_i off M_ij = {h ∈ U : h_i h_j < 0}, and the edge is a two-world system on M_ij. Under edge nestedness
   (the edge analogue of (Nest)), strict escape, Lemma T, Theorems E2 and E3, and Q1.4 hold for the restriction of
   world i to M_ij. Since the M_ij (j ≠ i) cover the mixed problems and overlap pairwise in non-null sets,
   **E2 and E3 transfer to every n ≥ 3**: a world that is lexicographic with charge levels, or complete, satisfies
   SP^reg. This corrects the statement in P4B §6 / write-up §8.4(c) that nothing in the two-world results transfers:
   the complementary world along a chain is supplied by every edge. My n = 3 lexicographic construction attempt
   (§5.1) fails exactly there.
4. **Candidate lemmas for the exclusion side** (§6): N17.B′(2) when the other world is additive (CONJECTURE,
   with the star case PROVED); "two additive worlds make the third additive" (CONJECTURE, local argument
   sketched); edge nestedness forced by (S) (CONJECTURE); and the n ≥ 3 question reduced to certificates carried
   by *interior* (non-edge) selected models at an incomplete, non-lexicographic, non-CP-a world (Q1.C5).
   Conditions (Nest) and (Nest_ij) are hypotheses wherever used.

**Where the remaining route is.** After Q1.4 and Q1.9, a counterexample needs (n = 2) two mutually mirrored
non-SP worlds, or (n ≥ 3) a world whose edge restrictions all satisfy SP but whose *interior* relevant comparisons
(crossing error sets, cyclic, as N17.3 demands for (M1)) admit no common strictly positive weight. Neither was
realised.

---

## 1. The two-world problem in cut form (PROVED, a reformulation of P4B Lemma N0 and §5.5)

Setting (Nest) of P4B: n = 2, M_U, strict (G), (IB), (LA), (S); world-1 error sets of members of C_L form a chain.
M = mixed problems of U; c_b (b ∈ [0,1]) the chain, d_b = M ∖ c_b; [s,t) := c_t ∖ c_s. A model X is described by
A = E₁X ∩ M and N(X) = the unaccepted non-negative problems; E₁X = A ∪ N(X), E₂X = (M ∖ A) ∪ N(X).
A *cut pair* at b is (P, Q) with P ⊆ c_b, Q ⊆ d_b.

**Lemma Q1.0 (PROVED).** For regular X with E₁X ∩ M = A and P = c_b ∖ A, Q = A ∖ c_b:
- C_b ⪯₁ X ⟺ P ≤₁ Q; C_b ⪯₂ X ⟺ Q ≤₂ P (by cancellation, since E₂ = M ∖ E₁ on M).
- (K) competitiveness at regular models: every cut pair has P ≤₁ Q or Q ≤₂ P.
- (U) undominatedness plus (C) at regular models: no non-trivial cut pair has both Q ≤₁ P and P ≤₂ Q.
- The world-1 relevant comparisons 𝔚^reg₁ are exactly the cut pairs with P ≤₁ Q; the world-2 relevant
  comparisons 𝔚^reg₂ are exactly the cut pairs with Q ≤₂ P.

*Proof.* The first item is cancellation applied to E₁C_b = c_b, E₁X = A and to E₂C_b = d_b, E₂X = M ∖ A. The second
is competitiveness of C_b on {1,2} at X. For the third: X weakly dominates or is tied with C_b iff Q ≤₁ P and
P ≤₂ Q; a non-trivial tie partner is incoherent (it is not in the chain), so (C) forbids ties and undominatedness
forbids strict domination. The last item restates the definition with Lemma N0(ii) (C_L is the selection). ∎

SP^reg₁ asks for a charge ν ≥ 0, strictly positive on non-null subsets of M, with ν(P) ≤ ν(Q) for every cut pair with
P ≤₁ Q. A **spread certificate** at world 1 is a non-null Z with Z ≤₁ A_j for a sequence of pairwise disjoint A_j
(then every endorsing ν has ν(Z) ≤ inf_j ν(A_j) = 0). With Z = c_a it is the "minimal shape" of P4 §5.5; Lemma T
excludes A_j that shrink to finitely many points of the chain.

---
## 2. Attempt A (n = 2): band plus spread exotic cones — every axiom except one closed section

### 2.1 The system

*Problem side.* n = 2, K′ = [k₁, k₂] ⊂ (0,1) (first coordinate of the prior), U = D_{K′}. Coherent evaluable models
are D_{[α,β]} with α ≤ k₁ < k₂ ≤ β. Path α(t) = k₁(1−t), β(t) = 1 − t(1−k₂), t ∈ [0,1]. Both endpoints decrease,
so the world-1 error sets E₁D_{[α(t),β(t)]} ∩ M increase strictly (they are unions of rays in the two mixed sectors).
Put μ̄ := μ/μ(M) and let b(t) := μ̄(E₁D_{[α(t),β(t)]}), a continuous strictly increasing bijection [0,1] → [0,1];
write C_b for the model with E₁C_b = c_b. Selection: p ↦ C_{b(p₂)}. Then C_{e₁} = P₁ (E₁ = ∅), C_{e₂} = P₂ (E₁ = M),
and for b ∈ (0,1) the credal set of C_b strictly contains K′ on both sides, so cl D_K ∖ 0 ⊆ U and (LF) holds at
every interior C_b with N = U. **Target:** any C_b, b ∈ (0,1) (an interval target).

*Coordinate.* x(h) := inf{b : h ∈ c_b} on M; its image measure under μ̄ is Lebesgue on [0,1], and c_b = {x < b}.
Put x(h) := 2 on the non-negative problems Nn of U (they are placed to the *right*, see Remark 2.2). For
δ ∈ 𝒞 (measurable {−1,0,1}-valued functions on U) put τ_δ(x) := ∫_{x(h) ≥ x} δ dμ̄, x ∈ [0,2].

*World 2:* ψ₂(X) := μ̄(E₂X). Additive, strictly guiding.

*World 1.* Fix a ∈ (0,1) and any family 𝓕 of non-null measurable subsets of d_a. For F ∈ 𝓕 put
g_F := 1_F − 1_{c_a} and
- band := {δ ∈ 𝒞 : τ_δ ≥ 0 on [0,2]};
- 𝓖(F) := {δ ∈ 𝒞 : τ_δ ≥ τ_{g_F} on [0,2]};
- 𝒜₁ := band ∪ ⋃_{F∈𝓕} 𝓖(F), and X ⪯₁ Y :⟺ 1_{E₁Y} − 1_{E₁X} ∈ 𝒜₁.

Note τ_{g_F}(x) = μ̄(F) − (a − x) for x ≤ a, = μ̄(F ∩ {x(h) ≥ x}) =: G_F(x) for a ≤ x ≤ 1, and 0 for x > 1.

**Proposition Q1.1 (PROVED).** For every family 𝓕, 𝒜₁ satisfies N17.1(a) (contains 𝒞₊, contains no non-zero δ ≤ 0,
closed under sums that stay in 𝒞). Hence ⪯₁ is a preorder with strict (G) and (IB) (N9.4).

*Proof.*
- 𝒞₊ ⊆ band. A non-zero δ ≤ 0 has τ_δ(0) = −μ̄(δ⁻ ∩ M) − μ̄(δ⁻ ∩ Nn) < 0, so δ ∉ band; and δ ∈ 𝓖(F) would need
  τ_δ(a) ≥ μ̄(F) > 0, impossible for δ ≤ 0.
- band is a convex cone intersected with 𝒞; band + 𝓖(F) ⊆ 𝓖(F) since τ is linear.
- **Key step.** Let s ∈ 𝓖(F), t ∈ 𝓖(F′) with s + t ∈ 𝒞. For x ≥ a: τ_{s+t}(x) = τ_s(x) + τ_t(x) ≥ τ_{g_F}(x) +
  τ_{g_{F′}}(x) ≥ τ_{g_F}(x), because τ_{g_{F′}} ≥ 0 on [a,2]. For x < a: since s + t ≥ −1 pointwise and
  μ̄{x ≤ x(h) < a} = a − x (no non-negative problem lies there),
  τ_{s+t}(x) = τ_{s+t}(a) + ∫_{x ≤ x(h) < a}(s+t) ≥ μ̄(F) + μ̄(F′) − (a − x) ≥ τ_{g_F}(x).
  So s + t ∈ 𝓖(F). ∎

The point of the key step: exotic acceptances overlap in their negative parts (all are −1 on c_a), and
compatibility (s + t ≥ −1) caps how much negative mass a sum can carry, so no sum of exotic acceptances ever needs
to be accepted beyond what one of them already gives. (Contrast N17.7/N17.8, where rigidity came from overlapping
*positive* parts.)

**Proposition Q1.2 (PROVED).** For every 𝓕 the system (⪯₁, ⪯₂) with the selection above satisfies strict (G), (IB),
(LA), competitiveness of every C_p on supp p, undominatedness of every C_p, (C), C_L = the selection, (LF) at every
interior C_b, and closed world-2 sections for every model. If 𝓕 contains a pairwise disjoint sequence A₁, A₂, …,
then **¬SP^reg₁** holds: every charge ν ≥ 0 on 𝔚^reg₁ has ν(c_a) = 0.

*Proof.* Write a model as (A, N) with A = E₁X ∩ M, N = N(X).
- *Competitiveness.* At vertices, P₁ and P₂ are the world-best models. For b ∈ (0,1), if C_b ⋠₂ X then
  μ̄(M ∖ A) + μ̄(N) < 1 − b, i.e. μ̄(A) > b + μ̄(N). Then δ := 1_{A ∪ N} − 1_{c_b} ∈ band: τ_δ = μ̄(N) ≥ 0 on (1,2],
  τ_δ ≥ 0 on [b,1], and for x < b, τ_δ(x) ≥ μ̄(A) − x + μ̄(N) − (b − x) > 0. So C_b ⪯₁ X.
- *Undominatedness and ties.* Suppose X ⪯₁ C_b and X ⪯₂ C_b. With P := c_b ∖ A, Q := A ∖ c_b, world 2 gives
  μ̄(P) + μ̄(N) ≤ μ̄(Q) (#), and δ := 1_P − 1_{Q ∪ N} ∈ 𝒜₁. In both cases τ_δ = −μ̄(N) on (1,2], so N = ∅.
  If δ ∈ band, τ_δ(b) = −μ̄(Q) ≥ 0 gives Q = ∅, and (#) gives P = ∅. If δ ∈ 𝓖(F): when b ≤ a, δ ≤ 0 on d_a, so
  τ_δ(a) ≤ 0 < μ̄(F), impossible; when b > a, τ_δ(b) = −μ̄(Q) ≥ G_F(b) ≥ 0 gives Q = ∅, and (#) gives P = ∅.
  So X = C_b: every C_b is undominated and has no tie partner. By Fact 0 every undominated model is tied with a
  selected one, so C_L is the selection, and (C) and (LA) hold.
- *World-2 sections* {p : 1 − b(p₂) ≤ ψ₂(X)} are closed.
- *¬SP^reg₁.* g_{A_j} ∈ 𝓖(A_j) says C_a ⪯₁ X_j for the regular model with E₁X_j = A_j; these are relevant
  comparisons. An endorsing ν ≥ 0 has ν(c_a) ≤ ν(A_j) for all j, and Σ_j ν(A_j) ≤ ν(M) < ∞. ∎

**Remark 2.2.** Placing Nn to the left (as in N17.8) breaks the key step: a sum s + t can then carry −1 on Nn in
addition to c_a. To the right, unaccepted non-negative problems are expensive at world 1, which is harmless.

### 2.2 Exactly where it fails: world-1 sections

**Proposition Q1.3 (PROVED).** Let X be regular with E₁X ∩ M = D ⊆ d_a. Then
- for each F ∈ 𝓕 with G_D ≥ G_F on [a,1], {b : δ_b := 1_D − 1_{c_b} ∈ 𝓖(F)} = [0, β_F(D)] with
  **β_F(D) = min( 1, min_{x ∈ [a,1]} (x + G_D(x) − G_F(x)) )**; for other F it is empty;
- the band part is [0, min(μ̄(D), min_{x≥a}(x + G_D(x)))];
- hence S₁(X) = {b : C_b ⪯₁ X} is closed iff sup_F β_F(D) is attained or does not exceed the band value.

*Example (the failure).* Split [a,1) into J_k = [1 − (1−a)2^{−k}, 1 − (1−a)2^{−k−1}), k ≥ 0, and let A_j consist of
one sub-interval of length 2^{−j}|J_k| of each J_k, chosen disjoint across j. Then the A_j are pairwise disjoint,
G_{A_j} > 0 on [a,1), and G_{A_j}(x) ≤ 2^{1−j}(1−x). Take 𝓕 = {A_j} and D = [a, a+d) ∪ [1−h, 1) with a+d+h < 1.
Then min_x(x + G_D(x)) = a + d + h, attained exactly on [a, a+d], where every G_{A_j} > 0. So for all large j,
β_{A_j}(D) < a + d + h and β_{A_j}(D) → a + d + h, while the band value is μ̄(D) = d + h. Hence
**S₁(X) = [0, a + d + h)**, which is not closed. (NUMERICS `q1py/band_exotic.py`: sum-closure in 1970 random
compatible pairs, no violation; no non-positive vector accepted in 3000 trials; β_F values 0.43, 0.493, 0.4993 → 0.5
for profiles (1−x)/m, m = 10, 100, 1000, with a = 0.3, d = h = 0.1.)

*Proof.* For b ≤ a, δ_b − g_F = 1_D − 1_F + 1_{[b,a)}, whose tails are ≥ 0 iff G_D ≥ G_F on [a,1]. For b > a the
conditions read G_D(x) − G_F(x) ≥ (b − x)₊ for x ≥ a (the conditions at x < a reduce to the one at x = a, since
D, F ⊆ d_a); this is b ≤ min_x(x + G_D(x) − G_F(x)). The band conditions are the case F = ∅ plus
τ_{δ_b}(0) = μ̄(D) − b ≥ 0. The example is the computation just described. ∎

**Diagnosis.** The failure is not an accident of the example. In the failing section, the band moves the mass of
A_j to the right of x and concentrates it in [1−h, 1): c_a ≤₁ D′ for sets D′ ⊆ d_{1−h} of vanishing measure, which is
the configuration Lemma T forbids. The band cannot be removed: with world 2 additive, (K) forces world 1 to contain
every cut pair with μ̄(P) < μ̄(Q), which is the band on cut pairs. Q1.4 below turns this into a theorem. If the profile
set {G_F : F ∈ 𝓕} is compact in the sup norm, all sections are closed (the conditions are jointly closed in (b, G_F));
but a spread certificate needs G_{A_j} → 0 uniformly, so compactness is exactly what ¬SP destroys.

---
## 3. Mirroring: a spread certificate at one world forces one at the other (n = 2)

Setting: (Nest) as in P4B (n = 2, M_U, strict (G), (IB), (LA), (S), world-1 error sets of C_L a chain). Lemma T,
strict escape (SE) and Lemma Q1.0 are available.

**Theorem Q1.4 (PROVED).** Let Z be non-null and let A₁, A₂, … satisfy Z ≤₁ A_j for all j and Σ_j μ̄(A_j) < ∞.
(a) There are J₀ and h₁ > 0 such that for every h ∈ (0, h₁) and every j ≥ J₀, the set L_{j,h} := A_j ∩ c_{1−h} is
non-null and **every Q ⊆ d_{1−h} ∖ A_j satisfies Q ≤₂ L_{j,h}.** These are world-2 relevant comparisons (cut pairs at
the interior cut 1 − h, Lemma Q1.0).
(b) If the A_j are pairwise disjoint, then every charge ν ≥ 0 on 𝔚^reg₂ has ν(d_{1−h}) = 0 for all h ∈ (0, h₁);
so **¬SP^reg₂**, with a spread certificate based at the right slab d_{1−h}.
(c) The mirror statement holds with the worlds exchanged and the chain reversed (base near the left end c_h).

*Proof.* (a) Choose J₀ with Σ_{j≥J₀} μ̄(A_j) < μ̄(Z)/2 and h₁ with μ̄(Z ∩ d_{1−h₁}) < μ̄(Z)/4, and put
Z′ := (Z ∩ c_{1−h₁}) ∖ ⋃_{j≥J₀} A_j, which is non-null. For j ≥ J₀, cancellation gives Z ∖ A_j ≤₁ A_j ∖ Z, so by
monotonicity and transitivity Z′ ≤₁ A_j, with Z′ ∩ A_j = ∅.
Suppose (a) fails for every choice of h₁ (keeping J₀). Then there are h_k ↓ 0, j_k ≥ J₀ and Q_k ⊆ d_{1−h_k} ∖ A_{j_k}
with L_k := L_{j_k,h_k} ≤₁ Q_k: either L_k is null (take Q_k = ∅) or some Q_k has Q_k ≰₂ L_k, and then (K) at the
cut 1 − h_k gives L_k ≤₁ Q_k. Put R_k := A_{j_k} ∩ d_{1−h_k}, disjoint from L_k and Q_k. Cancellation gives
L_k ∪ R_k ≤₁ Q_k ∪ R_k, hence Z′ ≤₁ A_{j_k} ≤₁ Q_k ∪ R_k ⊆ d_{1−h_k}. If Q_k ∪ R_k is null, Z′ ≤₁ ∅ contradicts strict
(G); otherwise the non-null sets Q_k ∪ R_k lie in shrinking neighbourhoods of the point 1 of the chain, against
Lemma T (m = 1, x₁ = 1) for the fixed non-null Z′. So some h₁ works (shrink it below the earlier choice if needed),
and for h < h₁, j ≥ J₀, L_{j,h} is non-null and no Q ⊆ d_{1−h} ∖ A_j has L_{j,h} ≤₁ Q; by (K), Q ≤₂ L_{j,h}.
(b) Take Q = S_j := d_{1−h} ∖ A_j and P_j := L_{j,h}. An endorsing ν has ν(S_j) ≤ ν(P_j) ≤ ν(A_j), and
ν(d_{1−h}) ≤ ν(S_j) + ν(A_j) ≤ 2ν(A_j). Disjointness gives Σ_j ν(A_j) ≤ ν(M), so ν(A_j) → 0 and ν(d_{1−h}) = 0.
(c) Lemma T, SE and (K) are symmetric under exchanging the worlds and reversing the chain (b ↦ 1 − b, c ↔ d);
Lemma T covers the end point x₁ = 0. ∎

**Corollary Q1.5 (PROVED).** Under (Nest): if world 2 satisfies SP^reg₂, then world 1 has no spread certificate
(no non-null Z is ≤₁ every member of a pairwise disjoint sequence). By the known two-world results this applies when
world 2 is CP-a (N22 Thm 1.2), has a nonzero leading charge (Thm E2), in particular is lexicographic with charge
levels (E2′), or is complete (Thm E3, CHECKED); and in particular when world 2 is additive. Symmetrically with the
worlds exchanged. *Hence a star-shaped counterexample to N17.B′(2) must fail SP^reg at both worlds, with mirrored
certificates: right slabs cheap at world 2 relative to spread left sets, left slabs cheap at world 1 relative to
spread right sets.*

**Corollary Q1.6 (PROVED).** Under (Nest), suppose world 2 has an endorsing charge ν₂ (ν₂ ≥ 0 on 𝔚^reg₂) that is
strictly positive on non-null subsets of M and uniformly absolutely continuous (ν₂(A) → 0 as μ(A) → 0; for instance
world 2 additive with an integrable density). Then:
(a) no non-null Z is ≤₁ every member of a sequence A_j with μ(A_j) → 0;
(b) ¬SP^reg₁ has no *star certificate*: there is no fixed non-null N such that for every m there are a finite
partition N = P₁ ⊔ … ⊔ P_k and pairwise disjoint sets Q_{il} (i ≤ k, l ≤ m), disjoint from N, with P_i ≤₁ Q_{il}.

*Proof.* (a) Pass to a subsequence with Σμ̄(A_j) < ∞ and run (a) of Q1.4; then
ν₂(d_{1−h}) ≤ ν₂(P_j) + ν₂(A_j) ≤ 2ν₂(A_j) → 0, so ν₂(d_{1−h}) = 0, contradicting strict positivity.
(b) For fixed m and each l, the vectors 1_{Q_{il}} − 1_{P_i} (i ≤ k) have pairwise disjoint positive parts and pairwise
disjoint negative parts, so their sum 1_{B_l} − 1_N, B_l := ⊔_i Q_{il}, is accepted (chaining lemma N17.1(b)): N ≤₁ B_l.
The B_l are pairwise disjoint, so some B_l has μ̄(B_l) ≤ 1/m. Letting m → ∞ contradicts (a). ∎

**Consequence for constructions.** Attempt A had world 2 additive, so Q1.6 explains its failure without computing
sections. More generally, any n = 2 counterexample needs **both** worlds non-additive, both failing SP^reg, and its
certificates cannot be stars (with an additive partner). The weighted certificates of P4 §5.5 that remain have
overlapping left sets at many cuts.

---
## 4. Attempts with both worlds non-additive (n = 2): failure report

By Q1.5–Q1.6 both worlds must be non-additive and must fail SP^reg in mirror image. I tried three designs.

**B. Fibrewise bands.** M ≅ [0,1]_x × [0,1]_y (x the chain coordinate, y an auxiliary coordinate carried by the radial
direction of the mixed sectors). World 1 = unanimity over the densities f(x)g(y) with f increasing, g > 0 arbitrary
(acceptance iff the band condition holds on a.e. fibre y), plus exotic cones c_a ≤₁ [a,1] × Y_j (Y_j disjoint).
Fibrewise pushing keeps thin-in-y sets thin, so the Lemma T mechanism of §2.2 is blocked.
*Exact failure (PROVED, immediate):* (K). If world 2 is the mirror image (fibrewise band towards the left), a cut pair
with μ(Q_y) < μ(P_y) on one fibre set and μ(Q_y) > μ(P_y) on another is decided by neither world. If world 2 is
additive, (K) forces world 1 to accept every cut pair with μ̄(P) < μ̄(Q), i.e. the full band, and Q1.6 applies.
(K) needs the two worlds *jointly complete on cut pairs*, and fibrewise unanimity is too incomplete.

**C. A single deciding functional.** Decide each cut pair (P,Q) by world 1 if Φ(P,Q) ≥ 0 and by world 2 otherwise,
and take each world to be the closure of its decided pairs. With Φ(P,Q) = σ(Q) − σ(P), the transitivity and
cancellation closure requires σ to be additive on compatible sums (chaining lemma N17.1(b)); with σ additive the
system is the additive pair, which satisfies SP. I found no non-additive σ for which the closures stay free of
reversals (outcome (a) of the exact test) while spread sets are heavy: a set function heavy on spread sets is
subadditive, while chaining needs superadditivity on the positive side (any family of disjoint pieces each ≥ a fixed
set chains to a union that must also be ≥ it).

**D. Ping-pong.** Q1.4 applied to world 1's certificate gives world 2's certificate based at d_{1−h}, and Q1.4(c)
applied to that gives world 1 a certificate based at c_{h′}. The two are consistent with each other, and with SE, DL,
DR and Lemma T as far as I could check: no contradiction and no realisation. A realisation needs, at both worlds,
exotic generators whose tail profiles accumulate at 0 (so that the certificates are spread), and closed sections at
every model, which by Q1.3 needs the profile family to be compact. Within a single "band ∪ generators" world these two
requirements are incompatible (§2.2). A design that escapes would need world orders that are not of the form
"convex cone ∪ translates of it", and I have no candidate.

---

## 5. Three or more worlds

### 5.1 The lexicographic attempt and where it fails

Two-world Theorem E2 rests on strict escape, which needs a complementary world along a chain; P4B §6 and the write-up
(§8.4(c)) record that nothing transfers to n = 3 as it stands. I therefore tried n = 3 with world 1 lexicographic,
leading level F₁ = ∫_{E₁} a₁ dμ with a₁ = 0 exactly on a non-null cone A₀ of mixed problems, secondary level μ on A₀,
worlds 2 and 3 additive. ¬SP^reg₁ is then automatic once some selected model errs at world 1 on A₀ (A ≤₁ D for every
A ⊆ A₀ and every non-null D off A₀; Prop R2 of N19). The removal lemma B4 (any n) requires every selected model that
errs on A₀ to be a weak local minimum of q ↦ F₁(E₁C_q) along the selection, so I designed the selection to be
locally constant on the leading level (a partial plateau, N9.1) wherever it errs on A₀, with the A₀-advice varying
inside the plateau. *Exact failure:* the edges. On an edge [e₁, e_j] with A₀ ∩ M_{1j} non-null, a selected model that
follows world 1 on part of A₀ ∩ M_{1j} is not competitive on {1, j} (it can be beaten at world j on that part and at
world 1's leading level elsewhere, world j being additive), so edge models err at world 1 on A₀ along the whole open
edge, where F₁ increases from 0; B4 is violated. Theorem Q1.9 below shows this is not a feature of the design.

### 5.2 Edge transfer (the two-world results do transfer)

Fix worlds i ≠ j, and put M_{ij} := {h ∈ U : h_i h_j < 0}. Note P_i = P_j off M_{ij}.

**Lemma Q1.7 (PROVED).** In any system with strict (G), (IB) and (S) on M_U, every C_q with q in the edge
[e_i, e_j] agrees with P_i (= P_j) a.e. off M_{ij}.

*Proof.* At q = e_i, C_q = P_i (world-i best). For q in the open edge, let W be the set off M_{ij} on which C_q errs at
world i; there it errs at world j as well. Correcting C_q on W gives X with E_iX = E_iC_q ∖ W and E_jX = E_jC_q ∖ W, so
by strict (G) X ≺_i C_q and X ≺_j C_q if W is non-null, against competitiveness on {i,j}. ∎

**Proposition Q1.8 (CHECKED).** For A ⊆ M_{ij} let X_A be the model equal to P_i off M_{ij} with E_i X_A = A (then
E_j X_A = M_{ij} ∖ A, since on M_{ij} each advice errs at exactly one of i, j). Assume
**(Nest_{ij})**: the sets E_i C_q ∩ M_{ij}, q ∈ [e_i, e_j], form a chain mod null.
Then (≤_i, ≤_j) restricted to subsets of M_{ij}, with the edge selection, satisfy every hypothesis used in P4B §§1–2
and §8 with M := M_{ij}: the chain, (K) at interior cuts (competitiveness of edge models on {i,j} at the models X_A),
closed sections at the models X_A (restriction of a closed set of Δ to the edge), strict (G) and cancellation.
Hence Lemma N0 (i), (iii), strict escape (B1, N1), Lemmas DL, DR, **Lemma T, Theorem E2 (E2′), Theorem E3** and
Theorem Q1.4 hold for the restriction of world i to subsets of M_{ij} (E3 importing Savage's theorem as in P4B).

*Check.* By Lemma Q1.7 the edge models are exactly the X_{c} with c in the chain, and every model the P4B proofs
build is of the form X_A (they modify error sets inside M only). P4B §7's table shows that those proofs use closedness
only at such "regular" models, (K) only at interior cuts, strict (G), cancellation, and (LA) only through
non-emptiness; none uses n = 2 beyond these. ∎

**Theorem Q1.9 (CHECKED; any n ≥ 3).** Assume strict (G), (IB), (LA), (S) on M_U and (Nest_{ij}) for every j ≠ i.
(a) If world i is lexicographic with countably many levels that are bounded charges ≥ 0 vanishing on null sets, then
the first level that does not vanish on the mixed problems has a countably additive density > 0 a.e. on them, it
endorses every comparison between subsets of the mixed problems, and **SP^reg_i holds**.
(b) If ≤_i is complete on subsets of the mixed problems, **SP^reg_i holds**.

*Proof.* Mix := mixed problems of U = ⋃_{j≠i} M_{ij}. For j ≠ j′, M_{ij} ∩ M_{ij′} is non-null: it contains the open
set of gambles near e_i − ε(𝟙 − e_i), which lie in U because K′ ⊆ int Δ.
(a) Let k* be the least index with π_{k*}|Mix ≠ 0 (it exists by strict (G)). On every M_{ij} the levels before k*
vanish, so if π_{k*}|M_{ij} ≠ 0 it is the first nonzero level of the edge world, and E2′ on M_{ij} gives it a density
> 0 a.e. on M_{ij}. It is nonzero on some M_{ij₀}; hence it is nonzero on each M_{ij} (which meets M_{ij₀} in a
non-null set), hence a.e. positive on each, hence on Mix. Since earlier levels vanish on Mix, A ≤_i B for A, B ⊆ Mix
implies π_{k*}(B∖A) ≥ π_{k*}(A∖B). Error sets of selected and regular models lie in Mix, so π_{k*}|Mix endorses
𝔚^reg_i; it is strictly positive on mixed problems.
(b) The fineness step of E3 on the edge (Lemma T, completeness, compactness of the chain) gives, for every non-null
Z ⊆ M_{ij}, a finite partition of M_{ij} into pieces ≤_i Z. For arbitrary j′, some piece meets M_{ij} ∩ M_{ij′} in a
non-null Z″ ≤_i Z, and M_{ij′} has a finite partition into pieces ≤_i Z″ ≤_i Z. Refining gives a finite partition of
Mix into pieces ≤_i Z, for every non-null Z ⊆ Mix (use any M_{ij} meeting Z). So ≤_i on Mix is a fine complete
qualitative probability; Savage's theorem gives an almost agreeing finitely additive P, strictly positive by
fineness, vanishing on null sets, endorsing 𝔚^reg_i. ∎

**Corollary Q1.10 (CHECKED).** Under (Nest_{ij}), Q1.4–Q1.6 hold on M_{ij}: if world j satisfies SP^reg_j, world i has
no spread certificate with Z and all A_k inside one M_{ij}.

**Status of the hypothesis.** (Nest_{ij}) is the edge analogue of P4B's (Nest), which is also a hypothesis there. It
holds for edge selections that are Bayes for additive (or lexicographic-additive) edge systems, since then each
problem's advice is monotone along the edge. Whether (S) forces it is open (CONJECTURE Q1.C2 below).

**Reading.** Contrary to P4B §6 and write-up §8.4(c), strict escape *is* available in n ≥ 3: every edge supplies a
complementary world along a chain. What does not transfer is the conclusion *for comparisons from interior selected
models*: E2 and E3 transfer only because a leading charge, or a Savage measure, once positive, endorses **every**
comparison. For incomplete non-lexicographic worlds, the edges control only edge comparisons.

### 5.3 Two additive worlds (CONJECTURE Q1.C3, with a local argument)

*Claim.* n = 3, worlds 2 and 3 additive with strictly positive integrable densities, selection Bayes-like with
coherent models whose boundaries sweep the mixed problems: then world 1 adds up. *Local argument (sketch, not a
proof).* Competitiveness forces world 1 to accept 1_{E₁X} − 1_{E₁C_q} whenever X beats C_q at worlds 2 and 3. For X
obtained by flipping small sets near ∂C_q, these are first-order Bayes conditions along the whole circle
{q·h = 0} ∩ U, on which h₁ changes sign; for B_q = {q·h > 0} they force the world-1 weight to be a constant multiple
of a single density on mixed problems (a reindexing of the chart lines that is projective and fixes the boundary
circles must be diagonal). Then world 1 contains a half-space of a strictly positive measure on mixed problems, and by
P2's constraint 5 (an exotic δ₀ plus a half-space vector yields −1_E) it contains nothing else on relevant
comparisons. The gap is the passage from "sweeping" to the global half-space for a general selection.

---
## 6. What the failures suggest is true (candidate lemmas for the exclusion side)

- **Q1.C1 (CONJECTURE; star case PROVED as Q1.6).** n = 2, (Nest): if world 2 has a strictly positive, uniformly
  absolutely continuous endorsing charge (e.g. world 2 additive), then SP^reg₁ holds. Evidence: Q1.6 excludes every
  star certificate; attempt A fails exactly through it. Missing: reducing a general weighted certificate
  1_N + Σλ_k(1_{Q_k} − 1_{P_k}) ≤ ε (overlapping P_k at different cuts) to a star, or a direct construction of an
  endorsing weight from the band that (K) forces into world 1.
- **Q1.C2 (CONJECTURE).** (S) with strict (G) on M_U forces (Nest_{ij}) on every edge (and (Nest) in n = 2). This would
  make Q1.9 unconditional: lexicographic worlds with charge levels and complete worlds would be excluded in every n.
- **Q1.C3 (CONJECTURE, §5.3).** Two additive worlds force the third to add up (n = 3). This is the ranking-level form of
  N17.A for the relevant comparisons.
- **Q1.C4 (CONJECTURE, the sharpened n = 2 statement).** No n = 2 system has mirrored spread certificates at both
  worlds (Q1.4 ping-pong). With Q1.5 this would prove N17.B′(2) for all certificates that contain a spread star.
- **Q1.C5 (the precise n ≥ 3 question).** If at every edge pair the restrictions of the worlds to M_{ij} satisfy SP^reg
  (as Q1.9 gives for lexicographic and complete worlds, and Q1.C1 would give next to additive ones), does (S) force
  SP^reg_i on the comparisons out of *interior* selected models? A counterexample must be an (M1) or (M2) failure carried
  only by interior selected models with crossing error sets (N17.3), at a world that is incomplete, not lexicographic
  with charge levels, and not CP-a, with at least two non-additive worlds (Q1.C3).

**Where every attempt broke, in one line each.**
- A (band + spread exotics, n = 2): closed world-1 sections (Q1.3); forced by Q1.6 because world 2 was additive.
- B (fibrewise bands): (K), the two worlds are not jointly complete on cut pairs.
- C (single deciding functional): transitivity/cancellation closure of the decided pairs produces reversals unless the
  functional is additive.
- D (ping-pong): no realisation found; the "convex cone ∪ translates" form cannot have both spread certificates and
  compact profile families.
- n = 3 lexicographic: the edges (B4 along an edge; Q1.9 in general).

---

## 7. Status table and axiom bookkeeping

| Item | Status |
|---|---|
| Q1.0 cut form of (K), (U), 𝔚^reg in n = 2 | PROVED (reformulation of P4B N0, §5.5) |
| Q1.1 band ∪ any exotic family is a (G)+(IB) world | PROVED |
| Q1.2 all axioms except closed world-1 sections, with ¬SP^reg₁ | PROVED |
| Q1.3 exact world-1 sections; a non-closed section [0, a+d+h) | PROVED; NUMERICS `band_exotic.py` |
| Q1.4 mirroring (spread certificate at 1 ⇒ ¬SP^reg₂ with right-slab base) | PROVED (uses Lemma T, SE: P4B, one reader) |
| Q1.5 spread certificates impossible next to an SP world | PROVED (given E2, E3 as stated in P4B; E3 CHECKED) |
| Q1.6 additive partner: no Z ≤₁ vanishing sets; no star certificates | PROVED |
| §4 designs B, C, D | failure report; B's failure PROVED, C and D not |
| Q1.7 edge models agree with P_i off M_ij | PROVED |
| Q1.8 edge subsystem satisfies the P4B hypotheses under (Nest_ij) | CHECKED |
| Q1.9 E2 and E3 transfer to every n ≥ 3 under edge nestedness | CHECKED |
| Q1.10 mirroring on edges | CHECKED |
| Q1.C1–C5 | CONJECTURE |

*Axioms used.* Q1.2 verifies strict (G), (IB) (via N17.1(a)/N9.4), (LA), competitiveness, undominatedness, (C), (LF),
world-2 closedness, for *every* model including non-regular ones; it fails exactly world-1 closedness. Q1.4–Q1.6 use
(Nest), (K) at interior cuts, closed sections at regular models of both worlds (through Lemma T and SE), strict (G),
cancellation; not (C), not (E). Q1.7 uses strict (G) and competitiveness on edges; Q1.8–Q1.10 add (Nest_ij) and
import P4B's proofs; Q1.9(b) imports Savage's theorem. **No assumption added to the framework**; (Nest) and
(Nest_ij) are stated hypotheses of the results that use them.

---

## 8. Files (`q1py/`, run with `python3 -I`)

- `band_exotic.py` (+ `.out`): world 1 of §2 on a 60-bin grid with six spread disjoint exotic sets.
  (i) 1970 random compatible pairs of exotic/band members, sums all accepted (Q1.1);
  (ii) 3000 random non-positive vectors, none accepted;
  (iii) exact rational values β_F(D) for spread profiles (1−x)/m, m = 10, 100, 1000: 0.43, 0.493, 0.4993, with
  supremum 0.5 not attained and band value 0.2 (Q1.3).
- No proof depends on the script.
