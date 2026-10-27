# N1 (round 20). Blind targets cannot be built: blindness crosses an edge, and on a nested chain it is an initial segment

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up or
the notes mark proved, each named), **CHECKED**, **CONJECTURE**, **NUMERICS** (`n1py/n1b_*.py`, run with
`python3 -I -B` from inside `n1py/`; no proof rests on them). No assumption is added.

Notation: write-up §§2–3; K3 §1 (𝔚_i, 𝒩_i, localizing families, D-localized, Yosida–Hewitt ν = ρ_νμ + π_ν);
M1 §1 (P_k, E_k, R_ij, Q_l, W_l, J_l, Y_k, (H_U)). For a world i satisfying (NC), ν*_i is the maximal endorser of
K3.1(c), ρ*_i its CA density, **Λ_i := {ρ*_i = 0} ∩ M** (the CA-blind set) and **V_i := M ∖ Λ_i** (the visible
set). D^ν is the localizing family of K3.1(b) for ν. An **edge-selected** model is C_p ∈ C_L with supp p = {i, j}
(for n = 2: p interior). For n = 2, R_12 = M.

(The 13 Oct note that previously occupied this file, "N1: negligible-stakes indifference (NSI_θ)…", 13 Oct, is kept
verbatim at the end, after the line "ARCHIVE". Its scripts `n1py/rand_check.py`, `t1_arcs.py`, `thresholds.py` are
untouched; the new scripts are `n1py/n1b_*`.)

---

## 0. Outcome

**The requested construction is impossible, and the reason is a theorem, not a failed design.** But the impossibility
does **not** settle T1: M1.7 forces a blind-target exchange only in covers of shadow type. What is settled is the
following.

1. **Lemma N1.1 (the swap lemma; PROVED; any n, no closedness used).** Let C be edge-selected on {i, j}, let
   ν ∈ 𝒩_i, and let P ⊆ E_iC ∩ R_ij be visible for ν (ρ_ν > 0 on P). Let Q ⊆ R_ij ∖ E_iC be CA-blind for ν
   (ρ_ν = 0 on Q) and lie off the carrier D^ν_m of ν's purely finitely additive part. Then **every endorser of world j
   vanishes identically on Q**.
   - In words: a blind target with a visible source is never paid at world i except at its "end".
   - Off the end, competitiveness of C against the swap C △ (P′ ∪ Q) must be supplied by world j.
   - Shrinking P′ then makes Q worthless to world j as well.
2. **Theorem N1.2 (edge dichotomy; PROVED).** In every ranking on M_U with strict (G) and (S), for every ordered
   pair (i, j) of worlds with (NC), one of the following holds.
   - **(R) rigid:** Λ_i ∩ R_ij = E_i(C) ∩ R_ij for an edge-selected (or vertex) model C. This is the shape of
     K3.7(β′) and of L2.
   - **(D) doubly blind:** Λ_i ∩ Λ_j ∩ R_ij is non-null, and world j is totally null on a non-null part of it.
3. **Corollary N1.3 (PROVED).**
   - **(a) Q_M1 has answer NO.** No ranking with every axiom has the T1-shadow c^T as its maximal endorser field. More
     generally, no cover has a world i with Λ_i ∩ R_ij = E_i(T1) ∩ R_ij while world j is CA-visible a.e. on
     E_i(T1) ∩ R_ij.
   - **(b) M1's (W2) is impossible in its required form.** In every cover, if the M1.7 source F_j is partly visible at
     world i, then the CA-blind part of the target F_i is totally null at world j (off D^{ν*_i}_m).
   - **(c) L1.D's residual is rigid.** If all blind sets are pairwise null on the edge regions (the case of
     CONJECTURE L1.D), every Λ_i has the rigid form of K3.7(β′), with **selected** between models on both edges.
4. **Theorem N1.5 (blind sets are initial segments; PROVED).** Consider a two-world full system on M_U whose C_L is
   a chain (nested). This holds in every known full system, and whenever some world is monotonely continuous (S1.6).
   Then for **every** endorser ν of world 1, whatever world 2 is, {ρ_ν = 0} ∩ M is an initial segment c_g = E_1(C_g)
   of the chain. The same holds on any edge region R_ij of a three-world system under (Nest_e).
   - This generalizes K3.8, which needed an additive partner.
   - **Consequently (Corollary N1.6) no relevant comparison has a CA-blind target and a CA-visible source.** The
     tilted orientation is impossible; L2's orientation (blind sources) is the only one, and L2 attains it.
5. **The two-world construction, if it exists at all, lives in S1's uninhabited residual (PROVED reduction).** It
   needs all three of the following:
   - a non-nested C_L, i.e. a rigid or tied crossing (S1 §4);
   - both worlds failing (MC_sel) along the crossing;
   - its blind target totally null at the partner world (N1.1).
6. **Gluing (part 2 of the brief).** Three blind-target edge systems would glue to a cover whose maximal endorser
   field is shadow-like. By N1.3(a)–(b) the glued ranking cannot satisfy (S), and the failing instance is explicit
   (§5): competitiveness of the M1.7 witness C against one swap model.

**What this settles for T1, precisely.**
- Excluded: every cover whose maximal endorser field is c^T (Q_M1). With M1 §5 this removes the shadow type from the
  residual.
- Excluded more generally: every (NC) cover in which, for some ordered pair (i, j), Λ_i ∩ R_ij is neither the
  world-i error set of a selected edge model nor meets Λ_j non-nullly (N1.2).
- Excluded under (Nest_e) on the edge: every cover whose M1.7 exchange at world i has a CA-blind target and a
  CA-visible source (N1.5).
- **Not settled:**
  - (NC) covers whose maximal fields satisfy the N1.2 dichotomy. These include rigid L2-shaped blind segments
    (the field-level question Q_A of K3, now with several weakly signed worlds) and doubly-blind overlaps;
  - (M1) worlds.

  The brief's sentence "impossibility would settle T1 via M1.7" is therefore correct only for shadow-type covers.
  M1.7 is a consistency condition, not a blind-target requirement, in every cover whose targets F_i are partly
  CA-visible or whose sources F_j are CA-blind.

| | Statement | Label |
|---|---|---|
| N1.0 | π-null pieces; edge-selected models equal P_i on Q_k; swap vectors | PROVED |
| N1.1 | swap lemma: blind target + visible source ⇒ partner totally null on the target off the end (also an interior version) | PROVED |
| N1.2 | edge dichotomy: Λ_i ∩ R_ij rigid (selected edge model) or doubly blind | PROVED |
| N1.3 | (a) Q_M1: No; (b) (W2) only with a partner-null target; (c) pairwise-null blind sets are rigid with selected between models | PROVED |
| N1.4 | edge chains under (Nest) have no jumps; strict escape along any nested edge chain | PROVED |
| N1.5 | nested chain (n = 2, or an edge under (Nest_e)): every endorser's CA-blind set is an initial segment E_i(C_g) ∩ R | PROVED |
| N1.6 | no CA-blind target with a CA-visible source (n = 2 with nested C_L; edges under (Nest_e)); K3.8 for every partner | PROVED |
| N1.7 | gluing three blind-target edge systems: the exact failing instance of (S) | PROVED (from N1.1) |
| N1.C | every coherent between model other than P_i, P_j crosses T1 on R_ij | CONJECTURE; NUMERICS |

---

## 1. Three small facts

**Lemma N1.0 (PROVED).**
- **(a) π-null pieces.** Let π ≥ 0 be a purely finitely additive charge on M vanishing on null sets, and B ⊆ M
  non-null. Then some non-null Q ⊆ B has π(Q) = 0.
- **(b) Edge-selected models are vertex-like off R_ij.** If C = C_p with supp p = {i, j} (n = 3), then C = P_i = P_j
  a.e. on Q_k ∩ M. Every coherent model is regular.
- **(c) Swap vectors.** For C as in (b) (or any C ∈ C_L when n = 2), P ⊆ E_iC ∩ R_ij and Q ⊆ R_ij ∖ E_iC, the model
  X := C △ (P ∪ Q) is regular and lies in M_U. Its relevant vectors at C are δ_i = 1_Q − 1_P and δ_j = 1_P − 1_Q.

*Proof.*
- **(a)** By K3.1(b) Step 1, for each k there is E_k with μ(E_k) < 2^{−k−1}μ(B) and π(M ∖ E_k) < 1/k. Put
  Q := B ∖ ⋃_k E_k. Then μ(Q) ≥ μ(B)/2, and π(Q) ≤ π(M ∖ E_k) < 1/k for every k.
- **(b)** Worlds i and j agree on Q_k. Suppose C errs (at both) on a non-null Z ⊆ Q_k ∩ M. Then X := C △ Z is
  strictly better at i and at j by strict (G), so C ⪯_i X and C ⪯_j X both fail. This contradicts competitiveness
  on supp p.
- **(c)** X ⊆ U and X = C on N₊. Toggling the advice on a set toggles the error status at every world.
  - At i: E_iX = (E_iC ∖ P) ∪ Q.
  - At j: on R_ij exactly one of i, j errs for either advice (g_ig_j < 0, and the advice is "accept" or "silence"),
    so E_jX ∩ R_ij = R_ij ∖ E_iX.
  - Since X = C off R_ij, this gives the two vectors. ∎

---

## 2. The swap lemma

**Lemma N1.1 (PROVED).** Let n ≥ 2, and let a ranking on M_U have (S)-competitiveness at C ∈ C_L on {i, j}, where C
is edge-selected (or n = 2). Let ν ∈ 𝒩_i, with ρ := ρ_ν and D := D^ν. Suppose:
- P ⊆ E_iC ∩ R_ij is non-null, with ρ > 0 a.e. on P;
- Q ⊆ R_ij ∖ E_iC has Q ∩ D_m = ∅ for some m, and ρ = 0 a.e. on Q.

Then ν_j(Q) = 0 for every ν_j ∈ 𝒩_j.

*Proof.*
- Fix a non-null P′ ⊆ P and put X := C △ (P′ ∪ Q). By N1.0(c), δ_i = 1_Q − 1_{P′} and δ_j = 1_{P′} − 1_Q.
- Competitiveness of C on {i, j} gives C ⪯_i X or C ⪯_j X.
- **World i rejects.** Suppose C ⪯_i X.
  - It is a relevant comparison (C ∈ C_L, X regular), so δ_i ∈ 𝔚_i.
  - It is D-localized: δ_i > 0 only on Q, and Q misses D_m.
  - So K3.1(b) gives ∫ρδ_i dμ ≥ 0, i.e. 0 = ρ(Q) ≥ ρ(P′) > 0. This is a contradiction.
- **World j accepts.** Hence C ⪯_j X, a relevant comparison, and every ν_j ∈ 𝒩_j has ν_j(Q) ≤ ν_j(P′).
- **Shrinking the source.** Take pairwise disjoint non-null P′_1, P′_2, … ⊆ P (μ is atomless). Then
  Σ_n ν_j(P′_n) ≤ ν_j(M) = 1, so ν_j(Q) ≤ inf_n ν_j(P′_n) = 0. ∎

*Remarks.*
- **(i)** Neither closedness, nor strict (G) at i, nor (IB) is used. Strict (G) enters only through N1.0(b), and only
  for n = 3.
- **(ii) Interior version (PROVED, same proof).** Let n = 3 and let C = C_p with p ∈ Δ°. Take P, Q as above but
  inside Q_i, where j and k agree. Then for some l ∈ {j, k}, every endorser of world l vanishes on Q.
  - For each P′_n, world j or world k must accept, since δ_j = δ_k on Q_i.
  - Some l occurs for infinitely many n.
- **(iii)** Without localization the same holds for any Q on which ν itself vanishes. By N1.0(a), every non-null
  CA-blind set contains such a Q, so the end D^ν plays no role beyond being avoidable.

---

## 3. The edge dichotomy and the shadow

**Lemma (M1.3, face KKM; re-proved here because M1 is unrefereed).** Assume strict (G) and (S). For X ∈ M_U there is
p ∈ [e_i, e_j] with C_p ⪯_i X and C_p ⪯_j X. If C_p ≠ X, then C_p fixes a non-null part of X's errors at i and at j.

*Proof.*
- The sets S_l := {p ∈ [e_i, e_j] : C_p ⪯_l X} (l = i, j) are closed by (S).
- Competitiveness on supp p gives e_i ∈ S_i, e_j ∈ S_j and S_i ∪ S_j = [e_i, e_j]. Connectedness gives
  S_i ∩ S_j ≠ ∅ (the KKM lemma on a segment).
- If E_lX ∖ E_lC_p were null at some l ∈ {i, j}, then E_lX ⊊ E_lC_p, since a model of M_U is determined by E_l. Strict
  (G) would then give X ≺_l C_p. ∎

**Theorem N1.2 (edge dichotomy; PROVED).** Let n ∈ {2, 3}, and let a ranking on M_U have strict (G) and (S). Let i ≠ j
be worlds satisfying (NC). Put X_Λ := the regular model equal to P_i off Λ_i ∩ R_ij and to P_j on Λ_i ∩ R_ij, so that
E_iX_Λ ∩ R_ij = Λ_i ∩ R_ij and X_Λ = P_i on Q_k. Then at least one of the following holds.

- **(R)** X_Λ = C_p for some p ∈ [e_i, e_j]. So X_Λ is coherent and selected, and Λ_i ∩ R_ij = E_i(C_p) ∩ R_ij. By
  K3.7′, C_p = D_K with K ∩ [e_i, e_j] ≠ ∅ and K ⊆ conv(K′ ∪ [e_i, e_j]).
- **(D)** There is an edge-selected C with the following properties:
  - Z_ij := Λ_i ∩ V_j ∩ R_ij ⊆ E_iC;
  - B := (Λ_i ∖ E_iC) ∩ R_ij is non-null, B ⊆ Λ_i ∩ Λ_j, and every endorser of world j vanishes on B ∖ D^{ν*_i}_m
    for every m;
  - (E_iC ∖ Λ_i) ∩ R_ij is non-null.

*Proof.*
- Apply the face KKM to X_Λ. This gives C = C_p ⪯_i X_Λ, ⪯_j X_Λ, with p ∈ [e_i, e_j].
- If C = X_Λ, we are in (R).
- Otherwise C fixes a non-null part of X_Λ's errors at both worlds:
  - F_i := E_iX_Λ ∖ E_iC = (Λ_i ∖ E_iC) ∩ R_ij is non-null;
  - F_j := E_jX_Λ ∖ E_jC is non-null. On R_ij, E_jX_Λ = R_ij ∖ Λ_i and E_jC = R_ij ∖ E_iC; off R_ij the errors of
    X_Λ are those of P_i, which are fixed by nothing. So F_j = (E_iC ∖ Λ_i) ∩ R_ij = E_iC ∩ V_i ∩ R_ij.
- p is not a vertex. If p = e_i then C = P_i and F_j = ∅. If p = e_j then C = P_j, E_iC ⊇ R_ij, and F_i = ∅.
- **Z_ij ⊆ E_iC.** Suppose Q := Z_ij ∖ E_iC is non-null. Choose m with Q ∖ D^{ν*_i}_m non-null. Apply Lemma N1.1 with
  ν = ν*_i, P = F_j (visible) and Q ∖ D_m (blind, off the end). It gives ν*_j(Q ∖ D_m) = 0. But
  ν*_j ≥ ρ*_jμ and ρ*_j > 0 a.e. on Q ⊆ V_j, which is a contradiction.
- **The rest.**
  - B = F_i ⊆ Λ_i ∖ Z_ij = Λ_i ∩ Λ_j ∩ R_ij.
  - The total nullness of world j on B ∖ D_m is Lemma N1.1 again, with Q := B ∖ D_m.
  - (E_iC ∖ Λ_i) ∩ R_ij = F_j is non-null. ∎

**Corollary N1.3 (PROVED).** Let n = 3 and assume (H_U).
- **(a) No shadow.** Let world i satisfy Λ_i ∩ R_ij = E_i(T1) ∩ R_ij, and world j satisfy ρ*_j > 0 a.e. on
  E_i(T1) ∩ R_ij, for some j ≠ i. Then there is a contradiction. In particular **Q_M1 (M1 §5) has answer No**: no
  ranking with every axiom has maximal endorser field c^T, since c^T has both properties on every edge.
- **(b) The M1.7 exchange.** Let C, F_i, F_j be an M1.7 witness on edge {i, j}. If F_j ∩ V_i is non-null, then every
  endorser of world j vanishes on F_i ∩ Λ_i ∖ D^{ν*_i}_m for every m. In particular F_i ∩ Λ_i ⊆ Λ_j.
  - So M1's requirement (W2), "π*_i(F_i) ≥ ρ*_i(F_j) > 0 with F_i ⊆ Λ_i", forces F_i to be doubly CA-blind.
  - It also forces F_i to be totally null at world j, on a set where T1 is right at j.
- **(c) Pairwise-null blind sets are rigid.** Suppose Λ_i ∩ Λ_j ∩ R_ij is null for all i ≠ j. Then every world i has
  Λ_i = (E_i(C^{ij}) ∩ R_ij) ∪ (E_i(C^{ik}) ∩ R_ik), where C^{ij} and C^{ik} are **selected** edge (or vertex) models.
  - This is the K3.7(β′) shape, now with selection, at every world and with no hypothesis on the partners.
  - M1.5(b) had this only for CA endorsers, and K3.7 only next to two integrable worlds.

*Proof.*
- **(a)** On R_ij exactly one of i, j errs for T1, so E_i(T1) ∩ E_j(T1) ∩ R_ij = ∅. Then
  Λ_i ∩ Λ_j ∩ R_ij ⊆ E_i(T1) ∩ Λ_j ∩ R_ij, which is null, so (D) fails and (R) holds.
  - (R) gives a coherent C with E_iC ∩ R_ij = E_i(T1) ∩ R_ij and C = P_i on Q_k, i.e. C = Y_k.
  - Y_k is incoherent (M1.6(b)), which is a contradiction.
  - For c^T: Λ_i = E_i(T1) ∩ M, and V_j = R⁰_j ⊇ E_i(T1) ∩ R_ij.
- **(b)** This is Lemma N1.1 with P = F_j ∩ V_i ⊆ E_iC ∩ R_ij and Q = F_i ∩ Λ_i ∖ D_m ⊆ (R_ij ∖ E_iC) ∩ Λ_i
  (M1.7's proof places F_i, F_j there). Positivity of ρ*_j would contradict ν*_j(Q) = 0.
- **(c)** (D) needs Λ_i ∩ Λ_j ∩ R_ij non-null, so (R) holds for (i, j) and for (i, k). On Q_i = R_ij ∩ R_ik both
  descriptions equal Λ_i ∩ Q_i. ∎

*Reading.*
- M1.1′(c) showed that no argument using only the CA fixed point excludes covers, because c^T passes every
  fixed-point test.
- N1.2 is a constraint on the maximal field that comes from the ranking: localization of the purely finitely additive
  part plus competitiveness at one edge model. c^T violates it on every edge.
- So "fixed point + N1.2" is strictly stronger than the fixed-point route. The shadow's degeneracy (pairwise-disjoint
  blind sets on each R_ij that are not edge-model error sets) is exactly what N1.2 forbids.

NUMERICS (`n1b_edge_check.py`, `.out`; 300 000 samples per (ε, s), half of them near ∂D_{T1}; three (ε, s); three
edges):
- (1) The set algebra used in (a): on R_ij, E_i(T1) = W_i ⊔ J_j, E_j(T1) = W_j ⊔ J_i, and
  E_i(T1) ∩ E_j(T1) ∩ R_ij is empty. Verified on every sample.
- (2) **CONJECTURE N1.C.** Every coherent between model other than P_i, P_j crosses T1 on R_ij. Evidence:
  - 300/300 random between models D_K per edge have both (E_iT1 ∖ E_iC) ∩ R_ij and (E_iC ∖ E_iT1) ∩ R_ij
    non-empty. The smaller of the two pieces holds ≥ 629 samples.
  - (3) 50/50 members of the nested family conv(K′ ∪ {(1−t)e_i + te_j}) cross T1 on R_ij.
  - Consequence if N1.C holds: under the shadow hypotheses of (a), N1.1 forbids **every** intermediate edge-selected
    model, not only the M1.7 witness.

---

## 4. Nested chains: blindness is an initial segment

**Setting.** Either (two worlds) n = 2 with C_L a chain, R := M, i = 1, j = 2; or (edge) n = 3, an edge {i, j} with
(Nest_e), R := R_ij. Index the edge selection by t ∈ [0,1] (C_t := C_{(1−t)e_i+te_j}) and put c_t := E_i(C_t) ∩ R. By
(Nest), c_t is nondecreasing, with c_0 = ∅ (C_0 = P_i) and c_1 = R (C_1 = P_j). By N1.0(b), C_t = P_i off R (n = 3).

**Lemma N1.4 (PROVED).**
- **(a) No jumps.** For τ ∈ (0,1], c_τ = ⋃_{s<τ} c_s. For τ ∈ [0,1), c_τ = ⋂_{s>τ} c_s (mod null).
- **(b) Strict escape.** For t ∈ [0,1) and non-null D ⊆ R ∖ c_t, let X := C_t △ D (world-i errors added on D). Then
  C_{t′} ⪯_i X for some t′ ∈ (t, 1).

*Proof.*
- **(a), left.** Suppose N := c_τ ∖ ⋃_{s<τ} c_s is non-null. Pick non-null N″ ⊆ N and let X be regular, equal to C_τ
  off R, with E_iX ∩ R = c_τ ∖ N″.
  - For s < τ, E_iC_s = c_s ⊆ E_iX, so C_s ⪯_i X by (G).
  - Closedness of the world-i section gives C_τ ⪯_i X. But E_iX ⊊ E_iC_τ, so X ≺_i C_τ by strict (G).
  - (For τ = 1 the section is closed at the vertex e_j, as (S) requires.)
- **(a), right.** This is the mirror argument, with E_iX ∩ R = c_τ ∪ N″, N″ ⊆ ⋂_{s>τ}c_s ∖ c_τ.
  - For s > τ, E_jC_s ∩ R = R ∖ c_s ⊆ R ∖ E_iX = E_jX ∩ R, so C_s ⪯_j X by (G).
  - Closedness at j gives C_τ ⪯_j X, against X ≺_j C_τ.
- **(b)**
  - E_jX = E_jC_t ∖ D, so X ≺_j C_t, and t ∉ S_j(X).
  - S_j(X) is closed, so some interval (t − η, t + η) misses it.
  - For t′ ∈ (t, min(t + η, 1)), competitiveness of C_{t′} on {i, j} gives C_{t′} ⪯_i X. ∎

**Theorem N1.5 (PROVED).** In the setting above, let ν ∈ 𝒩_i, ρ := ρ_ν, Λ_ν := {ρ = 0} ∩ R. Then
Λ_ν = c_g = E_i(C_g) ∩ R (mod null) for some g ∈ [0,1]. No hypothesis is placed on world j beyond the axioms.

*Proof.*
- **Step 1 (local spreading).** Let T := {t ∈ [0,1) : Λ_ν ∖ c_t non-null}. T is an initial segment of [0,1). Fix
  t ∈ T, and choose m with D := (Λ_ν ∖ c_t) ∖ D^ν_m non-null.
  - N1.4(b) gives t′ > t with C_{t′} ⪯_i C_t △ D.
  - Its vector is 1_{c_t ∪ D} − 1_{c_{t′}} = 1_{D ∖ c_{t′}} − 1_{c_{t′} ∖ (c_t ∪ D)} (off R both models equal P_i).
  - This comparison is relevant, and D^ν-localized, since its positive part lies in D.
  - K3.1(b) gives 0 = ρ(D ∖ c_{t′}) ≥ ρ(c_{t′} ∖ (c_t ∪ D)). With ρ = 0 on D: **ρ = 0 on c_{t′} ∖ c_t**.
- **Step 2 (to the left end).** Fix t₀ ∈ T, let S := {s ∈ [0, t₀] : ρ = 0 a.e. on c_s} ∋ 0, and τ := sup S.
  - By N1.4(a) (left), c_τ = ⋃_{s<τ, s∈S} c_s up to the trivial case τ ∈ S, so τ ∈ S.
  - If τ < t₀, then τ ∈ T, and Step 1 gives τ′ > τ with ρ = 0 on c_{τ′}. So min(τ′, t₀) ∈ S, which contradicts the
    definition of τ.
  - Hence **ρ = 0 on c_{t₀} for every t₀ ∈ T**.
- **Step 3.** Let g := sup T (g := 0 if T = ∅).
  - By Step 2 and N1.4(a), ρ = 0 on c_g (for g = 1: on ⋃_{t<1} c_t = R).
  - For t > g, Λ_ν ∖ c_t is null. By N1.4(a) (right), Λ_ν ∖ c_g = ⋃_{t↓g}(Λ_ν ∖ c_t) is null.
  - So Λ_ν = c_g. ∎

**Corollary N1.6 (PROVED).** In the setting of N1.5:
- **(a) No blind targets.** Let C_t ⪯_i X be a relevant comparison, with target Q := (E_iX ∖ c_t) ∩ R and source
  P := (c_t ∖ E_iX) ∩ R. If Q ∩ Λ_ν is non-null for an endorser ν, then P ⊆ Λ_ν.
  - In particular no relevant comparison has a CA-blind target and a CA-visible source, for any endorser.
  - In two worlds with C_L a chain this covers every relevant comparison: every member of C_L equals some C_t, since
    a member tied at both worlds with C_t and nested with it equals it by strict (G).
- **(b) K3.8 for every partner.** Every Λ_D and Λ_∞ of K3.1(d) is an initial segment. The proof is the same, with
  the blind piece of Step 1 chosen off both D^ν_m and the given family's D_m, so that the strict-escape comparison is
  D-localized. K3.8 had this only for an additive partner.
- **(c) Sharpness.** L2.1/L2.4 attain Λ = c_a for every a ∈ (0,1) in a full two-world system. So the shape in N1.5
  is attained, and the orientation of L2 (blind sources, visible targets) is the only orientation a CA-blind set can
  have.
- **(d) The M1.7 exchange on a (Nest_e) edge.** If F_i ∩ Λ_i is non-null, then F_j ⊆ Λ_i.
  - So the exchange ν_i(F_i) ≥ ν_i(F_j) is either between CA-visible pieces (a consistency condition) or between two
    CA-blind pieces.
  - In the second case it is satisfied by any world that is totally null on c_g, as L2's world is.

*Proof.*
- (a): Q ⊆ R ∖ c_t meets Λ_ν = c_g, so g > t and P ⊆ c_t ⊆ c_g.
- (b): N1.5 with that choice of blind piece, applied to the members of 𝒩(𝔚_D). Maximal supports are unions of final
  segments.
- (d): M1.7's proof places F_i ⊆ R ∖ c_t and F_j ⊆ c_t for its witness C = C_t. ∎

**The two-world construction of the brief.** By N1.6(a), a two-world full system with blind targets must have a
**non-nested** C_L. By S1.2–S1.6 that requires the following:
- a rigid or tied crossing of members of C_L;
- both worlds failing (MC), indeed (MC_sel), along it. So neither world is additive, nor (CP-a) with a countably
  additive credal set (S1.7);
- by N1.1, its blind target totally null at the partner world, off the end of world 1;
- consequently (N1.1) its blind target lies, off the end, in Λ_1 ∩ Λ_2, so the system is in alternative (D) of N1.2.

S1 §4 records that neither kind of crossing has been inhabited. I did not construct one, and I do not conjecture that
one exists.

---

## 5. Part (2): gluing three edge systems, and exactly where it breaks

**The intended assembly.** For each edge {i, j} take a two-world blind-target system S_ij on R_ij, with blind target
F_i ⊆ E_i(T1) ∩ R_ij at world i, visible source F_j at i, and the mirror at j. Then define world i on M_U by
lexicographic or unanimity combination of its two edge orders (on R_ij and R_ik, overlapping on Q_i). Add a coupling
on interior selected models with T1 = C_p for p ∈ T1 (VB-type plateau). The L4/M1 criterion is that the maximal
endorser field be c^T: (W1) blindness on E_i(T1), (W2) a pfa exchange π*_i(F_i) ≥ ρ*_i(F_j) > 0, (W3) every axiom,
and (W4) the M1.7 witnesses.

**Theorem N1.7 (PROVED; the failing instance).** Every ranking on M_U with (W1), (W2) at some edge {i, j}, and world j
CA-visible a.e. on E_i(T1) ∩ R_ij (as in c^T) violates (S). The violation can be named.
- Let C be the edge witness of (W4) (M1.7).
- Pick Q ⊆ F_i ∖ D^{ν*_i}_m non-null. Then ρ*_i = 0 on Q by (W1), and ρ*_j(Q) > 0.
- F_j ∩ V_i is non-null, since ρ*_i(F_j) > 0 by (W2). Pick a non-null P′ ⊆ F_j ∩ V_i with π*_j(P′) = 0 and
  ρ*_j(P′) < ρ*_j(Q).
  This is possible by N1.0(a) and absolute continuity.
- Then the swap model X := C △ (P′ ∪ Q) has C ⋠_i X and C ⋠_j X, so C is not competitive on supp p.

*Proof.*
- C ⪯_i X would be D-localized with ρ*_i(Q) = 0 < ρ*_i(P′), against K3.1(b).
- C ⪯_j X would give ν*_j(Q) ≤ ν*_j(P′) = ρ*_j(P′) < ρ*_j(Q) ≤ ν*_j(Q). ∎

So the gluing breaks **at competitiveness of the edge witness**, before closedness, (C) or (LF) are reached.
- The obstruction is local to one edge, one selected model and one swap.
- It is insensitive to where the end of world i is placed: Q is taken off the end. This includes ends at
  ∂U ∩ {h_i < 0}, ends in thin shells along ∂D_{T1}, and L2-type block ends.
- It is insensitive to how closed sections are obtained (compact selectors or anything else), since N1.1 uses no
  closedness.

---

## 6. Why the suggested mechanisms fail, and the relation to L3.4

- **L2's compact selectors and blocking geometry, in the tilted orientation.** These yield closed sections. But
  N1.5 shows that any mechanism, closed or not, on a nested chain produces CA-blind sets that are initial segments.
  - The spreading step is strict escape, forced by the partner world's closedness and (K).
  - A blind point to the right of a cut makes a slab just right of the cut blind (Step 1). No-jump continuity then
    carries this to the left end (Step 2).
  - So the tilted orientation is excluded by the partner's closedness, not by world 1's construction. This is why
    K3.3 (world-1 sections open) and L2 (orientation reversed) were the only examples.
- **Ends inside the blind target, at ∂U ∩ {h_i < 0} or anywhere else.** These are excluded by N1.1, which uses the
  part of the target off the end, and by N1.5, which is location-free.
- **L3.4 does not apply, and is not the reason.**
  - L3.4 concerns a world that refines an additive veto Φ = ∫ω dμ (countably additive, on wrong advice) paid at a
    vertex, together with (Imp).
  - A blind-target world's decisive level would be purely finitely additive, not of this form. A purely finitely
    additive leading level is in any case excluded in full nested n = 2 systems (Cor. E2′, P4B §8.3).
  - N1.1 uses competitiveness at one edge model only, with no veto, no (Imp), and no continuum-of-values (FC)
    argument. N1.5 uses closedness only through strict escape and the no-jump lemma.
  - So the obstruction here is independent of L3.4, and it would apply even to worlds that are not lexicographic.

---

## 7. The nearby reachable result, and the single open question

**Nearby result (PROVED; this is the shift of aim the impossibility suggests).** The reachable form of "blindness on
the target's errors" is **rigid blindness**.
- On a nested chain, every endorser's CA-blind set is the error set of a selected model, oriented as in L2 (N1.5).
  L2 attains it in a full two-world system for every cut a (N1.6(c)).
- In three worlds, without any nesting hypothesis, every blind set on every edge region is either rigid in this
  sense, with a **selected** between model, or meets the partner's blind set (N1.2).
- So the shadow has to be replaced by a field whose blind sets are L2-shaped edge segments. At such a field, M1.7 is
  satisfied by totally null blind segments (N1.6(d)), exactly as in L2.

**Single open question (Q_N1, field level).** Is there a field c = (ρ_kσ_k)_k on M (ρ_k ≥ 0 integrable) with the
following properties?
- **(γ₀)** d_t(c) = 0 for all t ∈ Δ.
- B_q is coherent for q ∈ Δ° whenever c ≠ 0 a.e.
- T1 = B_{p*} ∪ S with S ⊆ Z_{p*}, for some p* ∈ Δ.
- **(N1.2)** for every ordered pair (i, j), either Λ_i ∩ R_ij = E_i(D_K) ∩ R_ij for a coherent between model D_K, or
  Λ_i ∩ Λ_j ∩ R_ij is non-null.
- At least one Λ_k is non-null (M0closed excludes the rest).

The two answers:
- **"No"** excludes every cover in which all three worlds satisfy (NC). This is by L4.1 (every endorser tuple, in
  particular the maximal one, has the first three properties) together with N1.2 and M0closed. T1 on M_U would then
  reduce to covers with an (M1) world.
- **"Yes"** gives the exact shape a construction must realise: L2-type rigid edge segments (the open lift Q_L2 of L2
  §7), or doubly-blind overlaps.
- With one blind world and the rigid alternative this is K3's Q_A (open).
- The shadow c^T is a field with all properties except (N1.2), so Q_N1 is a strict sharpening of the question the
  fixed-point route left (M1.1′(c)).

---

## 8. Dependencies and files

**Used.**
- K3.1(b) (localization of purely finitely additive parts; Step 1 for N1.0(a)) and K3.1(c), (d) (maximal endorsers;
  Λ_D).
- K3.7′ (between lemma).
- M1.6(b) (Y_k incoherent; only in N1.3(a)). M1.3 is re-proved in §3. M1.7's placement of F_i, F_j is used in
  N1.3(b) and N1.6(d).
- S1.2–S1.7 (two-world class structure; (MC) ⇒ nested; only in the reduction of §4).
- L2.1, L2.4 (sharpness only); L4.1 and M0closed (only in the reading of Q_N1); E2′ (§6 only).

**Not used.** (IB); (C) beyond (H_U) in N1.3/N1.7; (LF); M0closed in any proof; Lyapunov; any (Nest_e) result
other than the hypothesis of N1.5 itself.

**Not refereed.** Points to check, in order of risk:
1. N1.1: that the swap comparison is D^ν-localized, and that K3.1(b) applies to the maximal endorser of 𝔚_i.
2. N1.4(a): the no-jump argument at τ = 1 (closedness at the vertex).
3. N1.5 Step 2: the sup argument's use of left continuity.
4. N1.2: the vertex cases of the face KKM.

`n1py/` (run with `python3 -I -B` from inside it):
- `n1b_common.py`: T1/U geometry, samplers (uniform on mixed U, and near ∂D_{T1}), error indicators.
- `n1b_edge_check.py` (+ `n1b_edge_check.out`):
  - (1) set algebra on R_ij;
  - (2) random between models cross T1 on R_ij (evidence for N1.C);
  - (3) the nested family conv(K′ ∪ {(1−t)e_i + te_j}) crosses T1 on R_ij.

---

# ARCHIVE: earlier note N1 (13 Oct 2026), kept verbatim

# N1: negligible-stakes indifference (NSI_θ): infrastructure and the triangle obstructions

13 Oct 2026. Labels as in BRIEF.md: **PROVED** (full proof written here), **CHECKED** (verified, proof
sketched), **CONJECTURE**. NUMERICS are evidence only. Scripts: `n1py/`.

Citations: R1 (Lemma 1.1–1.5, Prop 2.1, Thm 2.2, Prop 2.6, Prop 3.1), R10a (Thm V, Thm R, Thm M), R10b
(Prop V, Lemma FS, Lemma UVN, Lemma M, Thm PL), R14 (Thm A, Lemma B2, B4), R15 (Thm 1, Lemma 4.1,
Lemma 6.1, Thm 6.2), all as repaired in R6, R8, R12, R17, R18; CCIBU; LDG thm:kkm.

---

## 0. Outcome

**The answer to the author's question is negative, and the reason is structural rather than a matter of
θ being too small.** For additive systems on decomposable domains, NSI_θ adds no coverage of T1, of any interior
triangle, or (with the norms I checked) of any interior target, **for any θ**.

1. **Infrastructure carries over.** In additive form, (G) under NSI_θ *forces* ℓ_i(g,good) = ℓ_i(g,0) on band
   problems; it does not merely allow it (Lemma 1.2). The following carry over:
   - Interior Bayes uniqueness: R1 Lemma 1.4's splicing argument is unchanged (Prop 2.2).
   - The chart characterisation, with modified vertex charts (Thm 2.4).
   - Interiority of the target prior. This now has a two-line proof valid for every θ (Prop 2.3).
2. **Closed choice in three worlds, with no vertex condition (Thm 3.1, PROVED).**
   - In three worlds, an additive system with integrable envelopes whose interior Bayes models are unique and
     coherent (IBU) satisfies (LA), (S), (C). This holds under **any** guidance order, NSI_θ and Σ_T
     included.
   - The selection is R14's Chebyshev least-norm selection. Its vertex localisation repairs CCIBU's vertex
     step, so **no condition replaces "strict guidance at vertices"**: IBU alone suffices.
   - CCIBU's quadratic selection, by contrast, fails for NSI_θ systems with (LF) at an interior target
     whenever θ is below an explicit target-dependent value. For T1 at ε = 0.3 that value is 0.916
     (Prop 3.3).
3. **Chord pinning (Lemma 4.1, PROVED; any n ≥ 3, any θ > 0, any advice ranges compatible with (LF)).**
   - Suppose a facet point h′ of ∂D_T has 0 < h′_c < θ‖h′‖. Then the touching point m(h′) of T lies in K_q for
     **every** q on the half-chord (e_c, p\*].
   - Reason: world c is indifferent there, so the + vs 0 comparison has the same sign all along the chord.
4. **Acceptance needs a non-negligible winning stake (Lemma 4.2, PROVED).** Every h ∈ ∂D_T∖0 has a
   coordinate h_c ≥ θ‖h‖. Hence θ ≤ θ₁(T) := min_{h∈∂D_T} max_c h_c/‖h‖.
5. **Band no-go (Thm 4.3, PROVED; any n ≥ 3).**
   - If θ < θ₀(T) := max_c max_{h∈∂D_T} h_c/‖h‖, no additive NSI_θ system covers D_T. A non-degeneracy
     condition is needed; it is automatic when the relevant band edge lies inside a facet, and it holds for
     T1.
   - The contradiction: on the facet, chord pinning meets strict reward just past the band edge
     |h_c| = θ‖h‖. This is the brief's "crossings at the band edges replacing g_i = 0", made exact.
6. **No window (Thm 4.5).**
   - θ₁ < θ₀ always: PROVED for Euclidean and sup norms in n = 3; CHECKED for n ≥ 4.
   - So coverage would need θ₀ ≤ θ ≤ θ₁, which is impossible.
   - **For T1, every θ ∈ (0,1) fails, for either norm.** Euclidean values, with κ = (1+2ε)/(1−ε):
     θ₀(T1) = √((1+κ²)/(2+κ²)), between 0.816 and 1; θ₁(T1) = κ/√(2κ²+4), between 0.408 and 0.707.
     For the sup norm, θ₀ = 1 for every interior target.
   - **Answer to "how small can θ be": there is a target-dependent lower bound θ₀(T), and it is large**
     (θ₀(T1) ≥ √(2/3) for every ε). Above it, a second obstruction θ > θ₁(T) takes over.
7. **Triangle obstructions under NSI_θ (§5).**
   - Steps using strict reward for right answers at negligible stakes, near coordinate crossings, fail as
     stated. These are Thm V / Prop V, Thm 1(c), UVN(a) at crossings, Lemma M Step 4, and the A-witnesses of
     Lemma 6.1.
   - They survive with band edges replacing crossings, for θ below the facet values b_c(v).
   - Steps using strict penalty for wrong answers survive unchanged: FS, UVN(b), (a₋)_c ≤ 0, and the
     B-witnesses.
   - R10a Thm R becomes *stronger*: no concave chart representative exists for any θ > 0 and any target with
     a crossing.
   - R15's hypotheses (DF) + (ND) become *inconsistent* with NSI_θ, so Thm 6.2 is vacuous. Thm 4.3
     supersedes it.
8. **Nearby statement (Cor 4.6, CHECKED).** The same proof applies to *any* good~silence tie region Θ_c.
   - Near ∂D_T, a tie region at world c must contain the whole positive-c arc of ∂D_T or miss it.
   - Every boundary point needs a strictly rewarded positive coordinate.
   - So near the target boundary only world-wise (Σ_T-type) indifference is viable. For T1 not even that is
     viable: each positive-c arc contains points whose only positive coordinate is c.
   - Hence every tie-based weakening reduces T1 to strict guidance near ∂D_T. That is the original open
     problem, where all triangle obstructions apply unchanged.

**Recommendation (§6).** Do not pursue NSI_θ for coverage. The mirror weakening, "errors at negligible
stakes ~ silence", is not killed by the same argument on two-sided domains (advice range {+,0,−}). It is the only nearby
variant I could not close (§6.2, open).

---
## 1. Formalisation

### 1.1 The order

**Setting.** n ≥ 2 worlds. A binary problem is a pair {g, −g}, represented by g ∈ H. The kinds of advice
are +, 0, −, ×. At world i, "good" means accepting the orientation h ∈ {g, −g} with h_i > 0, and "bad"
means accepting the other one.

**Band.** Fix a norm ‖·‖ on ℝⁿ and θ ∈ (0,1). The pair is *in the i-band* if
- it is **mixed** (some coordinate positive and some negative), and
- |g_i| ≤ θ‖g‖.

The condition is invariant under g ↦ −g, so it is a property of the pair. Write Band_i for the set of such
pairs.

**Choice of norm.**
- With either the Euclidean norm or the sup norm, θ ≥ 1 puts every mixed pair in every band. That is
  total indifference on mixed problems, which is the D_Δ / Σ_Ω regime. So θ ∈ (0,1) throughout.
- All PROVED statements in §§1–5 hold for **every** norm, with the thresholds computed in that norm.
- The "no window" step (Thm 4.5) is PROVED for the Euclidean and sup norms in n = 3. For other norms it
  is a CONJECTURE.
- Numerical thresholds are given for both norms. The default is the Euclidean norm |·|.

**NSI_θ guidance order at world i** (rank classes, best first):
- on Band_i: {good, silence} < bad < ×;
- off Band_i, and on every unanimous pair: good < silence < bad < × (the original four-rank order).

So silence ties only with *good* advice. Bad advice is strictly worse than silence everywhere, and × is
strictly worst everywhere.

**(G_θ) on M_L.**
- (weak) If X is at least as good as Y in this order at world i on a.e. pair, then X ⪯_i Y.
- (strict) If, in addition, X is in a strictly better rank class on a non-null set, then X ≺_i Y.

Since swapping good and silence on band pairs is a weak improvement in both directions, (G_θ) **forces**
ties. It is not a weakening of (G) in the sense of an inclusion of axiom sets. As in the brief's
treatment of D_Δ and Σ_T, NSI_θ systems are an *additional admissible class*: a target counts as covered
if a strictly guiding system covers it **or** an NSI_θ system does. All other axioms are unchanged: decomposable
domains, (IB), (LA), (S), (C), (E), and (LF) at the target.

### 1.2 Additive form

**Lemma 1.2 (PROVED).** An additive ranking L_i(X) = ∫ ℓ_i(g, a_X(g)) dμ on a decomposable domain satisfies (G_θ)
at world i iff, for a.e. g and all a, b ∈ A(g) (the advice range of g):
- (i) ℓ_i(g,a) < ℓ_i(g,b) whenever a is in a strictly better NSI_θ class at i than b; and
- (ii) ℓ_i(g,good) = ℓ_i(g,0) whenever g ∈ Band_i and both are in A(g).

*Proof.*
- (i), and "if" for both parts: as in R1 Lemma 1.1.
- "Only if" for (ii): let E ⊆ Band_i ∩ {good, 0 ∈ A(g)} be measurable. Let X, Y ∈ M agree off E and give
  good, respectively silence, on E. Both are in M because M is a decomposable domain. Each is a weak improvement
  on the other, so L_i(X) = L_i(Y), i.e. ∫_E (ℓ_i(good) − ℓ_i(0)) dμ = 0.
- Since E is arbitrary, the integrand vanishes a.e. ∎

**Chart vectors.** As in R1 Prop 2.1, put c = ℓ(0) − ℓ(+), c′ = ℓ(0) − ℓ(−) and d = c − c′ = ℓ(−) − ℓ(+),
wherever the relevant kinds of advice are in the advice range. At a mixed pair g and world i, Lemma 1.2 gives:

| | g_i > θ‖g‖ | 0 < g_i ≤ θ‖g‖ | −θ‖g‖ ≤ g_i < 0 | g_i < −θ‖g‖ |
|---|---|---|---|---|
| c_i | > 0 | **= 0** | < 0 | < 0 |
| c′_i | < 0 | < 0 | **= 0** | > 0 |
| d_i | > 0 | > 0 | < 0 | < 0 |

So:
- c is weakly sign-preserving, with zeros exactly on the band coordinates where + is good;
- d remains **strictly** sign-preserving everywhere (good vs bad is never tied).

The table of charts for each advice range in R1 Prop 2.1 is otherwise unchanged:
- {+,0}: R(g) = {c·p > 0};
- {+,−}: R(g) = {d·p > 0};
- {+,0,−}: R(g) = {c·p > 0, d·p > 0} and R(−g) = {c′·p > 0, d·p < 0}.

**Lemma 1.3 (modified vertex property; PROVED).** Let h have advice range {+,0} or
{+,0,−} (so accepting h is in the advice range, but not every evaluable model accepts h). Then:
- δ_i ∈ R(h) if h_i > θ‖h‖;
- δ_i ∉ R(h) if 0 < h_i ≤ θ‖h‖, and in that case δ_i lies on the c-line, a tie;
- δ_i ∉ cl R(h) if h_i < 0.

*Proof.* Read off the table; d_i > 0 whenever h_i > 0. ∎

**Lemma 1.4 (radial invariance; PROVED).** Let h ∈ Band_c with h_c > 0 and both + and 0 in the advice range, and
let q = (1−s)e_c + s p with s ∈ (0,1]. Then:
- c(h)·q = s·c(h)·p;
- d(h)·q = (1−s)d_c + s·d(h)·p, with d_c > 0.

Hence for advice range {+,0} the + vs 0 decision is constant along every ray from e_c. For advice range {+,0,−}:
- "+ is the unique minimiser at p" propagates to all of (e_c, p];
- "+ loses to 0 at p" (c·p < 0) propagates to the whole ray.

*Proof.* c_c = 0 and d_c > 0 by the table. The minimiser conditions are the strict inequalities of R1
Prop 2.1, and both are preserved by these formulas. ∎

This is the mechanism behind everything in §4. It is also the exact sense in which the vertex e_c "does
not see" band problems.

## 2. Infrastructure under NSI_θ: additive systems on decomposable domains

### 2.1 Facts that need no guidance

**Prop 2.1 (PROVED).** Let L be additive with integrable envelopes and satisfy (G_θ) on a decomposable domain.
- (a) R1 Lemma 1.2 holds: Bayes models are exactly the pointwise minimisers.
- (b) R1 Lemma 1.3 holds: (LA) + (S) give a coherent p-Bayes model at every p; an undominated model is Bayes
  at some p; interior Bayes models are undominated.
- (c) The attainable set R is compact and convex.
- (d) LDG thm:kkm holds: (LA), (S), (C) imply U_L = C_L.

*Proof.* None of these uses (G). For LDG thm:kkm I re-read its proof: it uses (LA), (S) and (C) only,
through KKM on the sets A_ω = {p : c_p ⪯_ω m}. The other items are R1's proofs verbatim: splicing,
Lyapunov, and p_j > 0. ∎

### 2.2 Interior Bayes uniqueness

**Prop 2.2 (R1 Lemma 1.4 under NSI_θ; PROVED).** Assume (LA), (S), (C). For every interior p:
- (i) every p-Bayes model is coherent;
- (ii) the pointwise minimiser is a.e. unique.

*Proof.*
- (i): Prop 2.1(b), (d).
- (ii): R1's splicing argument goes through unchanged. Suppose two distinct kinds of advice both minimise on a
  non-null set. They differ in acceptance of g or of −g. This is still true for the tied pair (good, 0) at
  vertices; but the claim concerns interior p, and × is never an interior minimiser because it is strictly
  worst at every world. The splices X_F are evaluable models (the domain is closed under splicing) and all p-Bayes, hence all coherent by (i), hence
  all a.e. cones. Polar Fubini then gives the contradiction exactly as in R1.
- Strictness of (G) was never used. The only property of the kinds of advice used is that distinct kinds of advice in
  {+, 0, −} differ in acceptance. ∎

So in any n, under NSI_θ: (LA) + (S) + (C) ⇒ (IBU). (IBU) is the hypothesis "every interior w·L has an
a.e. unique minimiser, and it is coherent". The converse for n = 3 is Thm 3.1.

*Remark.* Interior ties are not forced by the band zeros. A tie between + and 0 at an interior p means
c·p = 0, and that set is null for a fixed p unless c ≡ 0 on a non-null set. c ≡ 0 is impossible on mixed
pairs, because c_j < 0 at every negative coordinate. If all positive coordinates of g are in the band,
then c ≤ 0 and c ≠ 0, so + loses at every interior prior. This is the content of Lemma 4.2.

### 2.3 The target prior is interior

**Prop 2.3 (PROVED; any n ≥ 2; any θ, indeed any guidance order in which bad is strictly worse than
silence at every world).** Let D_K ∈ C_L with K ⊆ int Δ, and assume (LF) at D_K. Then every p\* at which
D_K is Bayes is interior.

*Proof.*
- Let S = supp p\* ≠ Ω. Put g(t) = −1_S + t·1_{S^c}. Then P_K(g(t)) changes sign, because m(S^c) > 0 on K.
  So there is g₀ ∈ ∂D_K∖0 with (g₀)_S < 0.
- Every h near g₀ has h_S < 0, and by (LF) silence is in its advice range. Accepting h is strictly worse than
  silence at every world of S, so at p\* accepting h is never a minimiser.
- But a non-null part of that neighbourhood lies in D_K, and D_K is p\*-Bayes. Contradiction. ∎

This is shorter than R1 Prop 2.6. It uses only strict *penalty* of wrong answers, which NSI_θ keeps.

### 2.4 Chart characterisation

**Theorem 2.4 (R1 Thm 2.2 under NSI_θ; PROVED).**

**(N) Necessity.** Assume (LA), (S), (C). Then:
- (N1), (N2) hold verbatim (Prop 2.2).
- (N3_θ) At e_i: off Band_i the e_i-Bayes advice is a.e. unique and is the best advice in the advice range at
  world i. On G_i := Band_i ∩ {good and 0 both in the advice range} it may be either good or silence.
  - The world-i minimising face is F_i := argmin_R y_i = x⁰ + {∫_E δ dμ : E ⊆ G_i}, with
    δ(g) = ℓ(g, good_i) − ℓ(g, 0) and δ_i = 0.
  - Every Pareto-efficient point of F_i has a **unique** realisation, and it is coherent. This holds under
    (IBU), by R14 Thm A with the admissible sequence (e_i, w), w = (0, α, β), α, β > 0. Strict guidance
    is not needed (R17 §1.3).
  - Inefficient e_i-Bayes models may be incoherent.
- (N4) holds verbatim.

**(S) Sufficiency (n = 3).** (IBU) alone implies (LA), (S), (C), as well as (G_θ) and (IB) (Thm 3.1). No
condition at boundary priors or at vertices is needed. This replaces R1 Thm 2.2(S), which assumed
uniqueness at all p ∈ Δ.

**(T)** holds verbatim, and p\* is interior by Prop 2.3.

**The charts themselves.**
- R1 Prop 2.1's table holds with the vertex property of Lemma 1.3.
- The "vertex-respecting half-space" chart becomes: an open half-plane that contains δ_i for every
  out-of-band positive coordinate, has δ_i **on its boundary line** for every in-band positive coordinate,
  and has every δ_j with a negative coordinate outside its closure.
- A pair whose positive coordinates are all in band has R(g) ∩ int Δ = ∅. So it is accepted at no
  interior prior. ∎

**Modified Prop V / Thm V (vertex anchoring).** See §5, item V.

## 3. Closed choice in three worlds: the vertex step repaired

Notation is as in R14:
- R is the attainable set and a_i < min_R y_i.
- For q ∈ Δ, f_q(y) = max_i q_i(y_i − a_i), t\*(q) = min_R f_q, and B(q) = argmin_R f_q.
- σ(B) is the least-norm point argmin_{y∈B} Σ(y_i − a_i)², and x(q) := σ(B(q)).
- F_i = argmin_R y_i and m_i = min_R y_i.

**Theorem 3.1 (PROVED; n = 3; any guidance order).** Let L be additive on a decomposable domain, with integrable
envelopes, and assume (IBU). Then:
- every coordinate of q ↦ x(q) is lower semicontinuous on Δ;
- each x(q) is efficient and supp(q)-competitive, with a unique coherent realisation C_q.

Hence (LA), (S), (C) hold. (G) and (IB), for whatever guidance order the penalties respect, hold because
the rankings are additive. In particular the theorem covers NSI_θ, Σ_T, and strict guidance.

*Proof.*

*Step 1: efficiency, competitiveness, realisation.*
- x(q) is efficient and supp(q)-competitive by R14 Lemma B2(i). That proof uses neither guidance nor
  interiority of q (R17 §1.7).
- Uniqueness and coherence of the realisation is R14 Thm A, which uses (IBU) only.

*Step 2: active sets.*
- For q ∈ Δ put c_i(q) = a_i + t\*(q)/q_i for i ∈ supp q. Let m ∈ ri B(q) and I(q) = {i ∈ supp q : m_i = c_i}.
  I(q) is non-empty and independent of m.
- By R14 Lemma B4(i), which is pure convexity, y_I = c_I for every y ∈ B(q).
- Since B(q) = R ∩ {y_j ≤ c_j, j ∈ supp q}, there are three cases:
  - |I| = |supp q|: B(q) is a point if supp q = Ω. If supp q has two elements, B(q) is the segment
    R ∩ {y_S = c_S}.
  - |I| = 2 < |supp q| = 3: B(q) = R ∩ {y_I = c_I, y_k ≤ c_k}, a segment in direction e_k.
  - |I| = 1, I = {i}: the minimality argument of R14 B4(ii) (no guidance used) gives m_i = min_R y_i. So
    B(q) ⊆ F_i, and B(q) = F_i ∩ {y_l ≤ c_l(q), l ∈ supp q∖i}.
- In the first two cases B(q) is a point or a segment parallel to a coordinate axis, so it has a
  coordinatewise **least element**, and then σ(B(q)) is that least element.

*Step 3: the vertex regime V_i.* Let
 V_i := {q ∈ Δ : ∃ y ∈ F_i with q_l(y_l − a_l) < q_i(m_i − a_i) for all l ∈ supp q∖{i}}.
- q ∈ V_i iff I(q) = {i}.
  - "If": the witness y has f_q(y) = q_i(m_i − a_i) ≤ f_q(z) for every z ∈ R, since z_i ≥ m_i. So y ∈ B(q)
    with the inactive inequalities strict, which places i alone in the active set of ri B(q).
  - "Only if": a relative-interior point m of B(q) is such a witness.
- V_i is relatively open in Δ. The inequalities are strict and continuous in q. A coordinate l ∉ supp q
  enters with q′_l small, so q′_l(y_l − a_l) is small.
- e_i ∈ V_i (the condition is vacuous), and the V_i are pairwise disjoint.
- On V_i, B(q) = {y ∈ F_i : g_l(q,y) := q_l(y_l − a_l) − q_i(m_i − a_i) ≤ 0, l ≠ i}. Here F_i is compact
  and convex, and the g_l are jointly continuous and convex in y, with a Slater point at each q ∈ V_i.
- So q ↦ B(q) is Hausdorff-continuous on V_i:
  - lower hemicontinuity: Slater plus convexity (move a point slightly toward the Slater point);
  - upper hemicontinuity: closed graph.
- By Berge with a strictly convex objective, σ∘B is continuous on V_i.

*Step 4: lower semicontinuity everywhere.*
- At q ∈ ∪V_i, x is continuous (Step 3, V_i open).
- At q ∉ ∪V_i, B(q) has a least element ℓ(q) = x(q) (Step 2). Let q_m → q.
  - Every cluster point z of x(q_m) lies in B(q), by upper hemicontinuity of B (R14 Lemma B2(iii); Berge
    on the fixed compact R).
  - Hence z ≥ ℓ(q) = x(q) coordinatewise.
- So every coordinate of x is lower semicontinuous.

*Step 5: (S) and (C).*
- {p : C_p ⪯_i X} = {p : x_i(p) ≤ L_i(X)}, which is closed by Step 4.
- Competitiveness on supp p is Step 1.
- (C) holds because tied profiles have the same unique realisation (R14 Thm A).
- (LA) holds because each C_q is coherent and undominated. ∎

**What replaces "strict guidance at vertices".** Nothing beyond (IBU).
- CCIBU needed argmin_R y_i to be a point. Chebyshev localisation instead makes the selection constant,
  equal to σ(F_i), on the open set V_i ∋ e_i. So interior indices approaching e_i from different
  directions do not produce different cluster points.
- On an edge (e_i, e_j) near e_i, the selection slides continuously through σ(F_i ∩ {y_j ≤ c_j(q)}) to
  the y_j-minimal point of F_i. This is the "lexicographic tie-break" the brief suggested, produced
  automatically.

**Corollary 3.2.** R14 §1 point 4 flagged the three-world Σ_T case as breaking exactly at vertex
selections. That gap is closed: Thm 3.1 applies to Σ_T systems verbatim.

For n ≥ 4 the R14 residual remains: (L) on open faces of dimension ≥ 2. Without strict guidance it is
worse, because the Prop B5 oscillating-fibre geometry is no longer excluded by Lemma B3.

**Prop 3.3 (CCIBU's quadratic selection fails under NSI_θ; PROVED).** Let n = 3, let D_K have (LF) and
K ⊆ int Δ.
- The plane {h_i = 0} meets ∂D_K∖0 in two rays, w ∈ (0,+,−) and w′ ∈ (0,−,+) in the (i, j, k) coordinates.
  The cone D_K ∩ {h_i = 0} contains e_j and e_k, so its boundary rays lie in opposite open quadrants.
- Suppose w_j > θ‖w‖ or w′_k > θ‖w′‖. For example, for the Euclidean norm and T1 this holds whenever
  θ < (b′+ε)/√(b′² + (b′+ε)²), where b′ = (1−ε)/3; that is 0.916 at ε = 0.3.
- Then the projection Φ′_{e_i} of F_i to the two omitted coordinates has no least element.
- By R14 Prop B1, with the R17 repair at vertices, the CCIBU selection then violates (S) at e_i.

*Proof.*
- Φ′_{e_i} = x⁰_{jk} + {∫_E (δ_j, δ_k) dμ : E ⊆ G_i}, with signs:
  - δ_l < 0 iff good_i is good and out of band at l;
  - δ_l = 0 iff good_i is good and in band at l;
  - δ_l > 0 iff good_i is bad at l.
- y_j is minimised by E ⊇ {δ_j < 0} with E ∩ {δ_j > 0} = ∅, and y_k likewise. A least element exists iff
  {δ_j < 0 < δ_k} ∪ {δ_k < 0 < δ_j} is null.
- Say w_j > θ‖w‖. Near w, inside N, both good_i and 0 are in the advice range.
- The orientations with h_i ∈ (0, θ‖h‖), h_j > θ‖h‖ and h_k < 0 form a non-null set there. On it
  δ_j < 0 < δ_k.
- The case w′_k > θ‖w′‖ is symmetric. ∎

## 4. The new obstructions: chord pinning and the band no-go

### 4.0 Standing hypotheses

**(H_θ).**
- n ≥ 3, θ ∈ (0,1), any norm.
- An additive NSI_θ system (Lemma 1.2) on a decomposable domain with integrable envelopes, satisfying (LA), (S),
  (C). By Prop 2.2 this gives (IBU); in n = 3 it is equivalent to (IBU) by Thm 3.1.
- A target D_K ∈ C_L with K ⊆ int Δ and dim K = n−1, and (LF) at D_K with neighbourhood N.
- D_K is Bayes at p\*, which is interior by Prop 2.3, so D_K ≈ B_{p\*}.

**Notation.**
- Γ = ∂D_K ∖ 0. Every point of Γ is mixed, because K ⊆ int Δ.
- φ_c(h) = h_c/‖h‖.
- T(h) = argmin_{m∈K} m·h is the touching set. h ∈ Γ is *smooth* if T(h) is a single point m(h).
  Smooth points are dense in Γ: a convex cone's boundary is differentiable a.e.
- Shrink N so that N ∩ (−cl D_K) = ∅. This is possible because dim K = n−1 (R10a §1, R12).

### 4.1 Chord pinning

**Lemma 4.1 (chord pinning; PROVED under (H_θ)).** Let h′ ∈ Γ with 0 < h′_c < θ‖h′‖. Then for every
q ∈ (e_c, p\*]:
- K_q ∩ T(h′) ≠ ∅;
- if h′ is smooth, m(h′) ∈ K_q.

In particular, for a polytope K and h′ in the relative interior of the facet F_v, the vertex v lies in
K_q along the whole half-chord.

*Proof.*
1. *Choosing U.* Take a convex open ball U ∋ h′ with U ⊆ N, every point of U mixed, U ⊆ {0 < h_c < θ‖h‖},
   and U ∩ (−cl D_K) = ∅. Then for a.e. h ∈ U, + and 0 are in the advice range, and c(h)_c = 0 (Lemma 1.2).
2. *Points of D_K ∩ U.* For a.e. such h, + is the unique p\*-minimiser, since B_{p\*} ≈ D_K and the
   minimiser is unique (IBU). So c·p\* > 0, and also d·p\* > 0 if − is in the advice range. By Lemma 1.4, + is the
   unique minimiser at every q ∈ (e_c, p\*].
3. *Points of U ∖ cl D_K.* For a.e. such h, neither h nor −h is in D_K, so the p\*-minimiser is 0. Hence
   c·p\* < 0, using that ties are null at p\*. By Lemma 1.4, c·q < 0 at every q on the ray, so + is not a
   minimiser.
4. *Agreement on U.* So B_q ∩ U ≈ D_K ∩ U. By (IBU), B_q ≈ D_{K_q} up to nonnegative gambles, which do not
   meet U. Hence D_{K_q} ∩ U and D_K ∩ U are a.e.-equal open convex sets, and therefore equal.
5. *Touching.* P_{K_q}(h′) = 0, because h′ ∈ ∂(D_K ∩ U). Take m ∈ argmin_{K_q} m·h′.
   - P_{K_q} ≤ m·(·) everywhere, so m·h > 0 on D_K ∩ U, and therefore m·h ≥ 0 on cl D_K ∩ U.
   - Since cl D_K is a convex cone and m·h′ = 0: for y ∈ cl D_K and small t, h′ + t(y − h′) ∈ cl D_K ∩ U,
     which gives m·y ≥ 0.
   - So m lies in (cl D_K)\* ∩ Δ = K, and m·h′ = 0. That is, m ∈ T(h′). ∎

**Why this is new.** Under strict guidance, Lemma 1.4 fails: c_c > 0 tilts the + vs 0 comparison toward
acceptance as q → e_c. NSI_θ removes exactly that tilt on band problems. The target's local boundary
structure is then frozen along a whole segment of priors ending at a vertex of Δ. This is the
"plateau"/pinning phenomenon of R10b, but on a segment, and **forced** by the axioms rather than assumed.

### 4.2 Acceptance needs a winning stake

**Lemma 4.2 (W; PROVED under (H_θ)).** Every h ∈ Γ has max_c φ_c(h) ≥ θ. Moreover a.e. h ∈ D_K ∩ N has
max_c φ_c(h) > θ. Hence θ ≤ θ₁(K) := min_{h∈Γ} max_c φ_c(h).

*Proof.*
- Let h ∈ D_K ∩ N be mixed with every positive coordinate in band. Then c(h) ≤ 0, with c_j < 0 at every
  negative j (table, §1.2). So c·p\* < 0, and + is not a p\*-minimiser, since 0 is in the advice range by (LF).
- So such h form a null subset of D_K ∩ N. The condition "every positive coordinate is in band" is open,
  so if some h ∈ Γ had max_c φ_c(h) < θ, a non-null piece of D_K ∩ N near h would consist of such points.
  Contradiction. ∎

### 4.3 The band no-go

**UVN_θ (R10b Lemma UVN(a) under NSI_θ; PROVED).** Let x ∈ N be mixed with x_c > θ‖x‖. Then there is a
relative neighbourhood V of e_c with x ∈ D_{K_q} for every interior q ∈ V.

*Proof.* This is R10b's proof with one change.
- Choose x⁻ < x, close to x, with x⁻_c > θ‖x⁻‖, and a ball B₀ ∋ x⁻ inside N ∩ {h_c > θ‖h‖}.
- For a.e. h ∈ B₀, + is in a strictly better NSI_θ class at c than 0, −, × (good, out of band), so it is
  the strict ℓ_c-minimiser. The gap argument and dominated convergence give μ(B₀ ∖ B_q) → 0 as q → e_c.
- The half-ball argument puts x⁻ ∈ D_{K_q}, and upward closure gives x ∈ D_{K_q}. ∎

**Theorem 4.3 (band no-go; PROVED).** Assume (H_θ). Suppose there are a world c and a pair (h₀, m₀) such
that:
- (B1) h₀ ∈ Γ, h₀_c = θ‖h₀‖, and h₀ = lim h′_k for smooth h′_k ∈ Γ with 0 < (h′_k)_c < θ‖h′_k‖ and
  m(h′_k) → m₀;
- (B2) (non-degeneracy) some k ∈ ℝⁿ has m₀·k < 0 and β′(h₀; k) > 0, where β(h) := h_c − θ‖h‖ (concave)
  and β′ denotes the one-sided directional derivative.

Then **no such system exists**: D_K is not covered by any additive NSI_θ system.

*Proof.*
1. By Lemma 4.1, m(h′_k) ∈ K_q for all q ∈ (e_c, p\*]. K_q is closed, so m₀ ∈ K_q. Also m₀·h₀ = 0.
2. Put x = h₀ + tk with t > 0 small. Then x ∈ N, x is mixed, β(x) > 0, and m₀·x = t·m₀·k < 0.
3. By UVN_θ, x ∈ D_{K_q} for interior q in a neighbourhood V of e_c. The half-chord (e_c, p\*] meets V.
4. At such q, P_{K_q}(x) ≤ m₀·x < 0. Contradiction. ∎

The priors used all lie on one segment ending at e_c. No edge prior, no vertex model, no regularity
(DF)/(NA), and no box is needed. This is consistent with R10b Prop L: the priors accumulate at e_c ∈ ∂Δ.

**Prop 4.4 (when (B1), (B2) hold).** Let θ₀(K) := max_c max_{h∈Γ} φ_c(h).

(a) **PROVED.** If θ < θ₀(K), (B1) holds for some c.
- Pick c and h\* ∈ Γ with φ_c(h\*) > θ. The set {h_c = 0} ∩ Γ ≠ ∅ (n ≥ 3; R10b Prop V, first step).
- Γ ∩ S^{n−1} is a topological (n−2)-sphere, hence connected. Take a path in it from a zero of φ_c to h\*.
  Let h₀ be the first point on the path with φ_c ≥ θ, and let the path start at the last zero before h₀.
- Between that zero and h₀, φ_c ∈ (0, θ). Smooth points are dense there, and a subsequence of touching
  points converges.

(b) **PROVED.** Let K be a polytope, n = 3, and use the Euclidean norm.
- On the facet arc F_v (a great-circle arc), φ_c(h(t)) = R_{v,c} cos(t − τ), with R_{v,c} := |π_{v^⊥}e_c|.
  So for θ ≠ R_{v,c}, the level θ is crossed transversally.
- Suppose (B2) fails at h₀. Then m₀ = λ(e_c − θĥ₀) with λ > 0 (the alternative to the existence of k,
  since ∂β(h₀) = {e_c − θĥ₀}). If h₀ ∈ relint F_v, then m₀ = v.
- With v·ĥ₀ = 0, this forces ĥ₀ ∝ π_{v^⊥}e_c and θ = R_{v,c}. At a corner h₀, m₀ is the strip-side
  vertex, and the same identity results.
- Hence (B2) holds for every θ < θ₀(K) outside the finite set E(K) := {R_{v,c}}.

(c) **PROVED (sup norm, n = 3, polytope).** ∂‖·‖_∞ at h₀ is conv{sgn(h₀_j)e_j : |h₀_j| = ‖h₀‖}, with
j ≠ c because h₀_c = θ‖h₀‖ < ‖h₀‖.
- (B2) fails only if m₀ ∈ int Δ is a positive multiple of e_c − θΣα_j sgn(h₀_j)e_j.
- That requires both j ≠ c to have h₀_j = −‖h₀‖, i.e. h₀ ∝ (θ, −1, −1) up to order, together with m₀ the
  matching vertex.
- This is again a finite exceptional set of θ.

(d) **T1 (PROVED; numerics confirm).**
- *Euclidean.* For θ < θ₀(T1), every first band-edge point lies in a facet relative interior, with
  θ < R_{v,c} there. So (B2) holds. (`n1py/t1_arcs.py`: about 400 endpoints for each ε ∈ {.05, .3, .6},
  none at a corner.)
- *Sup norm.* h₀ ∝ (θ, −1, −1) on F_2 would need θ = (2b′+ε)/b′ > 1. So (B2) holds for every θ < 1.

### 4.4 No window

Thm 4.3 excludes θ < θ₀(K) (outside E(K)), and Lemma 4.2 excludes θ > θ₁(K). Since θ₁(K) ≤ θ₀(K) always,
any surviving θ must satisfy max_c φ_c ≡ θ on Γ (or be exceptional).

**Theorem 4.5 (PROVED; n = 3; Euclidean or sup norm).** No credal K ⊆ int Δ with dim K = 2 has
max_c φ_c ≡ θ on Γ in a way compatible with Lemma 4.2. Hence θ₁(K) < θ₀(K), and **no θ ∈ (0,1) outside
E(K) admits additive NSI_θ coverage of D_K.**

*Proof (Euclidean).* Suppose φ_c ≤ θ on Γ for every c, together with Lemma 4.2. Let
C_c = {h : h_c > θ|h|}, a round convex cone of half-angle α = arccos θ about e_c.
1. *Starting point.* The arc cos t·e₁ + sin t·e₂, for t ∈ (−π/2, 0), starts in D_K, at e₁, and leaves cl D_K
   before reaching −e₂. Its exit point h¹ ∈ Γ has φ₁ = max_c φ_c, since φ₂ < 0 = φ₃. So φ₁(h¹) = θ.
2. *Locally D_K = C₁.* Near h¹, φ₂ < 0 and φ₃ ≈ 0 < θ. By Lemma 4.2, a.e. point of D_K near h¹ has φ₁ > θ.
   So locally D_K ⊆ C₁, and Γ ⊆ {φ₁ = θ} = ∂C₁. Being open and relatively closed in C₁ near h¹, D_K agrees
   with C₁ locally.
3. *Following ∂C₁.* Follow Γ along the circle ∂C₁ ∩ S², which is parametrised by
   θe₁ + √(1−θ²)(cos s·e₂ + sin s·e₃), starting from s = π.
   - If θ < 1/√2: φ₃ = √(1−θ²) sin s reaches θ at some s₁. Past that point ∂C₁ enters C₃, where φ₃ > θ, so
     Γ must leave ∂C₁ there and continue on ∂C₃. By step 2 applied at both sides, D_K is locally C₁ ∪ C₃
     near the junction ray. The two circles cross transversally, so this union has a reflex edge, and D_K
     is not convex.
   - If θ ≥ 1/√2: φ₂, φ₃ ≤ √(1−θ²) ≤ θ on ∂C₁, with equality only at tangency points, where the same
     reflex/pinch argument applies. So Γ is all of ∂C₁ and D_K = C₁. But e₂ ∈ D_K and φ₁(e₂) = 0. ∎

*Sup norm.* The same argument applies with C_c = {h_c > θ|h_j| for all j ≠ c}.
- The exit point is h¹ ∝ (θ, −1, 0).
- Along the face h₁ = −θh₂ of C₁, φ₃ = h₃/‖h‖ reaches θ at (θ, −1, θ). The face normals (1, θ, 0) and
  (0, θ, 1) differ, so the union is non-convex.
- Going the other way, one passes the convex edge (θ, −1, −1) of C₁ and then meets C₂ in the same way.
- Otherwise D_K = C₁, which is again impossible. ∎

*n ≥ 4 (CHECKED, sketch).* Lemma 4.1, Lemma 4.2, UVN_θ, Thm 4.3 and Prop 4.4(a) are dimension-free. The
window argument runs the same way in the 2-plane spanned by e₁, e₂, then follows ∂C₁ within the 3-space
spanned by e₁, e₂, e_j. A full write-up of the junction step for general n is not attempted.

**Corollary (T1 and the threshold question; PROVED).** Put κ = (1+2ε)/(1−ε) and b′ = (1−ε)/3.
- *Euclidean.*
  - θ₀(T1) = √((1+κ²)/(2+κ²)). It is attained at the foot of e_c on v_k^⊥ (k ≠ c), which lies in
    relint F_k. As ε increases from 0 to 1 it rises from √(2/3) ≈ 0.816 to 1: 0.858, 0.928, 0.984 at
    ε = .1, .3, .6.
  - θ₁(T1) = κ/√(2κ²+4). It is attained at h ∝ (κ/2, κ/2, −1) ∈ relint F_3. It rises from 1/√6 ≈ 0.408
    to 1/√2: 0.485, 0.601, 0.685 at ε = .1, .3, .6.
  - θ₁ < θ₀ ⟺ κ² < 2 + 2κ², which always holds.
  - Every θ < θ₀ is excluded by Thm 4.3 (no exceptional values for T1), and every θ > θ₁ by Lemma 4.2.
    **So no θ ∈ (0,1) works.**
- *Sup norm.*
  - θ₀ = 1 for every interior K: take h = e_c − t(𝟙 − e_c) at its boundary value t₀ = min_K m_c/(1−m_c),
    which is ≤ 1 for some c, since some m_c ≤ 1/2.
  - So Thm 4.3 alone excludes every θ < 1, for every interior target satisfying (B2), T1 included.
  - θ₁(T1) = min(1, κ/2).
- NUMERICS (`n1py/thresholds.py`, `n1py/rand_check.py`).
  - The formulas match to 4 digits.
  - Over 391 random interior triangles (Euclidean): min θ₀ = 0.912, max θ₁ = 0.660. So the excluded
    ranges overlap with a margin of at least 0.338.

**Answer to (c)(2).** There is a target-dependent threshold θ₀(T) below which the obstruction persists. It
is the largest normalised positive stake on the target's boundary, and for T1 it is at least √(2/3) for
every ε. Above θ₁(T) a second obstruction takes over. For T1, and every interior triangle tested, the two
ranges cover (0,1).

### 4.5 Arbitrary tie regions (the nearby statement)

**Cor 4.6 (CHECKED).** Replace the band by any measurable family of tie regions: at world c, good ~
silence on Θ_c (a set of mixed pairs), and the order is strict elsewhere. Assume each Θ_c equals the
closure of its interior up to a null set.

The proofs of Lemmas 1.2, 1.4, 4.1, 4.2 and of UVN_θ, Thm 4.3 go through with:
- "0 < h_c < θ‖h‖" replaced by "h_c > 0 and h ∈ int Θ_c";
- "h_c > θ‖h‖" replaced by "h_c > 0 and h ∉ cl Θ_c".

Consequences, near Γ:
- (i) For each c, the positive-c part of Γ cannot contain both interior points of Θ_c and points of its
  exterior that are adjacent to them along Γ, apart from non-degenerate exceptions. So, up to such
  exceptions, Θ_c ⊇ a neighbourhood of Γ ∩ {h_c > 0}, or Θ_c misses one. That is, near the boundary the
  ties are world-wise, i.e. of Σ_T type.
- (ii) Every h ∈ Γ needs a positive coordinate outside the tied worlds.

For T1, every positive-c arc Γ ∩ {h_c > 0} contains points whose only positive coordinate is c (the foot
points of §4.4). So no world can be tied near Γ, and **any tie-based weakening leaves T1 with strict
guidance on a neighbourhood of Γ.** That is the original open problem; §5 shows its obstructions are
unaffected.

*Consistency checks.*
- With Θ_c = all mixed pairs, i.e. Σ_{{c}}, (ii) says that no boundary point of the target may have c as
  its only positive coordinate. That means K touches the face {m_c = 0}, which matches the shape of the
  Σ_T closures in CSE.
- With all worlds tied, nothing mixed near Γ can be accepted, which is the D_Δ exception.

*Remark (dim K < n−1, e.g. T3).* Lemma 4.1 needs only h′ ∉ −cl D_K. That fails only for h′ ⊥ K, a
nowhere-dense set of directions in Γ, so Thm 4.3 extends with h′_k chosen off it. CHECKED.

---

## 5. Triangle obstructions under NSI_θ, item by item (small θ > 0)

**Two kinds of strictness.**
- "Strict reward" means c_c > 0 for h_c > 0: the right answer beats silence. NSI_θ removes it on
  0 < h_c ≤ θ‖h‖.
- "Strict penalty" means c_c < 0 for h_c < 0, and d strict: the wrong answer is worse than silence or the
  right answer. NSI_θ keeps it.

Below, b_c(v) := sup_{h∈relint F_v} φ_c(h). For T1, b_c(v_k) = θ₀(T1) for every crossing pair (k, c).

| Item | Status under NSI_θ | Step that used strict reward at negligible stakes |
|---|---|---|
| **R10a Thm V / R10b Prop V** (e_i ∈ K_{e_i}) | **FAILS as stated.** Survives in modified form V_θ (PROVED, below): dist(e_i, K_{e_i}) ≤ C·θ | Prop V: B_{e_i} ∩ B ≈ {h_i > 0} on a ball B around the crossing w (w_i = 0). Thm V: h^θ = h⁰ + θk with tiny positive h_i is accepted. On Band_i the vertex model may be silent |
| R10a Cor V1 / R10b Cor V1 (every evaluable model accepts h only if h ≥ 0) | Modified (PROVED): every evaluable model accepts h only if min_i h_i ≥ −C′θ‖h‖ | via V_θ |
| **R10b Lemma FS** | **Survives** for z′ with z′_S < 0. Needs either a ball inside N, or margin z′_s < −C′θ‖z′‖ to exclude that every evaluable model accepts z′ (V1_θ) | none: it uses strict *penalty* |
| R10b Lemma UVN(a) | Survives with the **band edge replacing the crossing**: x_c > θ‖x‖ (UVN_θ, §4.3) | the vertex strict minimiser for h_c > 0 |
| R10b Lemma UVN(b) | **Survives unchanged** for x ∈ N, where 0 is in the advice range. Elsewhere it needs a C′θ margin | none (strict penalty) |
| R10b Lemma D, Lemma P (geometry) | Survive unchanged | none |
| **R10b Lemma M** | Survives in modified form M_θ for θ < b_c(v) (CHECKED). Take w₊ ∈ relint F_v with (w₊)_c > θ‖w₊‖, and replace U by a convex tube in N around the facet segment [w₋, w₊] meeting no other facet. Steps 1–3 are unchanged (R4 Thm B uses only d, which is still strict). Step 4 uses UVN_θ at w₊ and (a₋)_c ≤ 0 (strict penalty) | Step 4, UVN(a) at w₊ near the crossing (w₊ → w) |
| **R10b Thm PL** | Survives for pairs v ≠ v′ with θ < b_c(v) and θ < b_{c′}(v′); for T1, for θ < θ₀(T1). CHECKED. Superseded by Thm 4.3 | via Lemma M and UVN(a) at w_j > 0 |
| **R10a Thm R** (ray lemma, concave charts) | **Strengthened** (PROVED, Thm R_θ below): for every θ > 0 and every target with a crossing, no concave sign-respecting representative exists. No corner rays are needed | Step 3: "f_i has the sign of h_i near the zero line on a crossing facet" |
| R10a Thm M (gauge mixtures) | Gauge mixtures violate (G_θ): f_i > 0 on band-positive h. Any NSI_θ variant would need f_i = 0 there, which Thm R_θ forbids | — |
| **R15 Thm 1 (a), (b), (d)** | Survive (they use no guidance) | — |
| **R15 Thm 1 (c)** (crossing rows, λ > 0) | **FAILS.** Replaced by the flatness Lemma 5.1 (PROVED): crossing facets are first-order flat. So **(DF) + (ND) are inconsistent with NSI_θ** | two-sided clusters at the crossing; λ > 0 via UVN(a) at h_i > 0 near the crossing |
| R15 Lemma 3.2, Thm 5.1, Prop 5.2, 5.3 | Vacuous (they presuppose (c)) | — |
| R15 Lemma 4.1 (p\* drops out) | Survives (no guidance) | — |
| **R15 Lemma 6.1** (vertex-limit box) | The **mechanism survives** (CHECKED): FS at edge priors near e_b, with **A-witnesses restricted to A_b > θ‖A‖**, beyond the b-band edge of F_{k′}. B-witnesses are unchanged (strict penalty). The quantitative Λ_{ab} ≤ 1 needs (DF), which is inconsistent with NSI_θ, so the box has no first-order content | the threshold A_b > s|c_a|/((1−s)λ_{bk′}) → 0 as s → 0, i.e. reward λ_{bk′}A_b > 0 for arbitrarily small A_b. Under NSI_θ, c_b(A) = 0 for A_b ≤ θ‖A‖, so c·q₀ = s·c_a(A) < 0 and A is never accepted |
| **R15 Thm 6.2** (all-facing no-go) | **Vacuously true** (hypotheses inconsistent). Superseded by Thm 4.3, which needs no (DF), (ND), (NA_w), box, or corner rays | via (c) and Lemma 6.1 |

**V_θ (PROVED; Euclidean norm).** Let w ∈ Γ with w_i = 0 and |w| = 1, and let B(w, r) ⊆ N. Assume
θ < r/4. Then every coherent e_i-Bayes model D_{K_{e_i}} has a point m₀ ∈ K_{e_i} with
 |m₀ − e_i| ≤ (1+√2)(2 + 4/r)·θ.

*Proof.*
1. At e_i, h ∈ N with h_i < 0 is strictly rejected (strict penalty). Hence P := P_{K_{e_i}} ≤ 0 on
   N ∩ {h_i < 0}, and by continuity P ≤ 0 on Π := {h_i = 0} ∩ B(w, r/2).
2. For h ∈ Π, h + 2θe_i ∈ N is out of band (2θ > θ√(1 + 4θ²)), so it is strictly accepted. Hence
   P(h + 2θe_i) ≥ 0, and so P(h) ≥ −2θ.
3. Let m₀ ∈ argmin_{K_{e_i}} m·w, and let u ⊥ w be a unit vector in e_i^⊥. Then m₀·(w ± (r/2)u) ≥ −2θ and
   m₀·w = P(w) ∈ [−2θ, 0]. So |m₀·u| ≤ 4θ/r.
4. Hence the projection of m₀ onto e_i^⊥ = span{w, u} has length ≤ 2θ + 4θ/r. Since m₀ ∈ Δ,
   1 − (m₀)_i ≤ √2·|π m₀|, and the bound follows. ∎

The order θ cannot be improved to e_i ∈ K_{e_i}. Locally, K = conv{(1−δ)e_i + δe_j, (1−δ)e_i + δe_k}
with δ ≈ θ/2 meets both constraints near w but excludes e_i. CHECKED.

**Thm R_θ (PROVED).** Let K ⊆ int Δ, n = 3, and suppose some vertex v_k has a crossing in coordinate i.
Then no family f₁, f₂, f₃, concave and positively homogeneous on a neighbourhood of cl D_K∖0, satisfies
both of the following:
- (i_θ) on Γ, f_i > 0 where h_i > θ‖h‖, f_i = 0 where 0 < h_i ≤ θ‖h‖, f_i < 0 where h_i < 0;
- (ii) Σ_i p\*_i f_i = 0 on Γ.

*Proof.*
- By R10a Thm R Step 2, f_i is linear on F_k.
- The band strip {0 < h_i < θ‖h‖} ∩ relint F_k is open in v_k^⊥ and non-empty, because there is a
  crossing. f_i vanishes on it, so f_i ≡ 0 on F_k.
- But f_i < 0 on the non-empty open part {h_i < 0} ∩ relint F_k. ∎
- Strictness of the negative sign for an a.e.-signed representative follows from concavity, by R12's
  repair of Cor R1. This holds for every θ > 0, with no condition on corners or p\*.

**Lemma 5.1 (flat crossing facets; PROVED).** Assume R15's (SH) with NSI_θ in place of strict guidance,
and (DF) at p\*. Let coordinate c cross on F_k. Then:
- Γ_k h·(e_c − p\*) = 0 for all h ∈ v_k^⊥;
- moreover Γ_k ≡ 0 (first-order flat), if either θ < b_c(v_k), or (NA_w) holds near the negative part
  {h_c < 0} ∩ relint F_k.

*Proof.*
1. *Band strip.* On the band strip, c(h)_c = 0 a.e. So every cluster has ĉ_c = 0. By R15 Thm 1(b), which
   uses no guidance, the unique cluster is ∝ Γ_k h with ĉ·p\* = 0. Hence Γ_k h·(e_c − p\*) = 0 on an open
   subset of the plane v_k^⊥. By linearity (Thm 1(a)) it vanishes on all of v_k^⊥.
2. *Consequence.* So for every h ∈ relint F_k with Γ_k h ≠ 0, the cluster's zero line is line(p\*, e_c).
3. *Case θ < b_c(v_k).* For h with h_c > θ‖h‖, UVN_θ gives ĉ·q ≥ 0 on a neighbourhood V_c of e_c. That
   neighbourhood straddles line(p\*, e_c), which is a contradiction unless Γ_k h = 0.
4. *Case (NA_w).* For h with h_c < 0, UVN(b) with full half-plane charts gives ĉ·q ≤ 0 on V_c, with the
   same contradiction.
5. In either case Γ_k vanishes on an open set, hence identically. ∎

So under NSI_θ, any realisation of any target with a crossing must be **non-differentiable or
first-order flat at p\*** on every crossing facet. This is R15's escape (E1)/(E3), now forced.
Thm 4.3 shows that it does not help either.

---

## 6. Assessment

### 6.1 Answers

**(c)(1) Can NSI_θ deliver coverage of T1 or of interior triangles?**
- **No, for additive systems on decomposable domains.** The proof is complete for T1 and both norms, for all
  θ ∈ (0,1): Thm 4.3 with Prop 4.4(d), Lemma 4.2, and the T1 corollary.
- For every interior target with dim K = 2 in three worlds (Euclidean or sup norm), the same holds outside
  a finite exceptional set E(K) of θ-values where band edges are degenerate (Thm 4.3, 4.5).
- Even precise interior targets are not NSI_θ-covered. They stay covered by strict systems, since NSI_θ
  systems are an *added* class.
- Under NSI_θ, every one of the triangle obstructions either survives in a band-edge form or becomes
  vacuous (§5). But they are no longer needed.

**(c)(2) How small can θ be?** There is no "small θ" regime that helps.
- The no-go threshold θ₀(T) is the largest normalised positive stake on the target boundary. For T1 it is
  ≥ √(2/3) ≈ 0.816 at every ε (0.928 at ε = 0.3).
- For θ < θ₀(T) the chord pinning lemma meets strict reward just past the band edge (Thm 4.3).
- For θ > θ₁(T) (0.601 at ε = 0.3), Lemma 4.2 kills acceptance near the target boundary.
- The intervals overlap for T1, and for all 391 sampled triangles.
- The author's ideal, "for every θ > 0 every coherent target is covered", is false for all interior
  targets in three worlds under the norms checked.

**Ordinal (IB) preorders.**
- Lemma 4.1 and Lemma 4.2 are additive arguments: they compare + and 0 through prior-weighted sums.
- If the R11/R13 sandwich reduction extends to NSI_θ, the no-go transfers to sandwiched ordinal NSI_θ
  systems. That needs sandwiching penalties that respect the forced ties of Lemma 1.2 (CONJECTURE).
- For general (IB) preorders it is open.

### 6.2 Nearby results and leads (per the project preference: what is reachable)

1. **Theorem 3.1 is a genuine positive by-product.** In three worlds, closed choice follows from (IBU)
   alone, for every guidance order. This closes the vertex gap for Σ_T systems that R14 flagged
   (Cor 3.2).
2. **What the obstruction says about any tie-based weakening (Cor 4.6).** Near ∂D_T, ties must be
   world-wise (Σ_T-type), and each boundary point needs a strictly rewarded positive coordinate. For T1
   this forces strict guidance on a neighbourhood of ∂D_T. **So no good~silence weakening, stake-based or
   otherwise, can change the status of T1.** The decisive question remains the strict-guidance
   single-target problem of BRIEF2, with R15's residual (DF)/(ND)/(NA_w) escapes.
3. **The mirror weakening NSE_θ** ("bad ~ silence when the stake is negligible") is the one nearby
   variant not closed here. Findings (CHECKED, sketches):
   - Chord pinning holds on the *negative* band strip when the advice ranges there are {+,0}. Then UVN(a), which
     needs no band because reward is still strict, gives a contradiction for **every** θ > 0, whenever the
     target has a crossing.
   - With advice range {+,0,−} on the negative strip, the identity d·q = (1−s)d_c + s·d·p\* has
     d_c < 0. So pinning holds only on a sub-segment [s₀, 1] away from e_c, and the argument does not
     close.
   - A Lemma 4.2 analogue requires every h ∈ Γ to have a coordinate h_j < −θ‖h‖. That holds for T1 when
     θ ≲ 0.34 at ε = 0.3, the value at the foot points; the minimum over Γ was not computed.
   - The R15 flatness argument (Lemma 5.1) also applies, so NSE_θ realisations must be non-smooth at p\*.
   - Whether an NSE_θ realisation of T1 on a two-sided domain exists is open. I would not prioritise it: it trades
     strict penalty for strict reward and still has to beat the corner/box mechanism.

---

## 7. Status table

| Claim | Label |
|---|---|
| Lemma 1.2: (G_θ) for additive rankings ⇔ strict on classes and **forced** ℓ_i(good) = ℓ_i(0) on band | PROVED |
| Lemma 1.3 (modified vertex property); Lemma 1.4 (radial invariance) | PROVED |
| Prop 2.1: Bayes / Lyapunov / thm:kkm facts need no guidance | PROVED (thm:kkm re-read) |
| Prop 2.2: R1 Lemma 1.4 (interior uniqueness, splicing) under NSI_θ | PROVED |
| Prop 2.3: target prior interior, any θ (strict penalty only) | PROVED |
| Thm 2.4: chart characterisation under NSI_θ | PROVED |
| Thm 3.1: n = 3, (IBU) ⇒ (LA), (S), (C), any guidance order (Chebyshev selection) | PROVED |
| Cor 3.2: closes R14's Σ_T vertex gap (n = 3) | PROVED |
| Prop 3.3: CCIBU's quadratic selection fails under NSI_θ (explicit θ-range) | PROVED |
| Lemma 4.1: chord pinning | PROVED |
| Lemma 4.2: θ ≤ θ₁(K) | PROVED |
| UVN_θ | PROVED |
| Thm 4.3: band no-go under (B1), (B2) | PROVED |
| Prop 4.4: (B1) for θ < θ₀; (B2) outside finite E(K) (polytopes, Euclidean or sup norm); T1 has no exceptions | PROVED (T1 also NUMERICS) |
| Thm 4.5: no window (n = 3; Euclidean, sup) | PROVED |
| Thm 4.5 for n ≥ 4; other norms | CHECKED (sketch) / CONJECTURE |
| T1 formulas θ₀ = √((1+κ²)/(2+κ²)), θ₁ = κ/√(2κ²+4) (Euclidean); θ₀ = 1, θ₁ = min(1, κ/2) (sup) | PROVED (NUMERICS agree) |
| Cor 4.6: arbitrary tie regions, Σ_T-type near ∂D_T; T1 forces strict guidance near ∂D_T | CHECKED |
| V_θ: dist(e_i, K_{e_i}) = O(θ) | PROVED (sharpness of order: CHECKED) |
| Thm R_θ (no concave representative, any θ > 0) | PROVED |
| Lemma 5.1: (DF) ⇒ crossing facets flat; (DF) + (ND) inconsistent | PROVED |
| Lemma M_θ, Thm PL for θ < b_c(v); Lemma 6.1 mechanism with band-edge witnesses | CHECKED |
| Ordinal / sandwiched transfer | CONJECTURE |
| NSE_θ (mirror) | open; partial claims CHECKED |

## 8. Files (`n1py/`)

| File | Purpose |
|---|---|
| `thresholds.py` | θ₀, θ₁ (and an auxiliary edge-prior threshold, superseded by Prop 2.3) for T1 at both norms; the random part is slow, see the next row |
| `rand_check.py` | θ₀ vs θ₁ over random interior triangles (both norms) |
| `t1_arcs.py` | location of T1's band-edge endpoints (facet relint vs corner) |
