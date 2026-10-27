# PP16. From one target to a selection: a selection architecture around audit's guarded construction, its couplings, and an exact obstruction

21 October 2026. One reader (me); not refereed.

**Labels.** PROVED: the full argument is given here. CHECKED: exact rational computation (`fractions.Fraction`), complete over the stated finite cell model. NUMERICS / SCREEN: evidence only. OPEN / CONJECTURE: as stated. "Imported" marks a result used from an earlier note and not re-proved.

**Scripts** are in `PP16_py/`. Run each as `python3 -I -B <script>` inside that folder; outputs are in `*.out`. Code uses 0-based worlds; the note uses 1-based worlds.

**Instance used for the checks.** Contamination target T = D_M with ε = 3/10 (c = 7/30). Guards G_k are small cones (aperture 1/50) around g^k = 4e_k − (1 − e_k), so L = 4. Audit's defenders are C_i = Φ_{s_i}(T) with a = 10. `s1` checks every hypothesis audit's §§2, 4, 11 place on this instance.

**No assumption is added.** The axioms are those of the brief: (S) with closed fixed-rival sections, (G) both halves, (IB), (TC), undominatedness, and direct (C). "Audit's relation" means AUDIT_guard_extension.md: the guidance or target-reference base R⁰, the two-sided exposure filter, and repair records installed at every world. Every extension below is an extension of that relation, in which comparisons are added and none removed.

---

## 0. Verdicts

1. **The architecture (§2).**
   - Central plateau: C_p = T on a compact region P₀.
   - Defender plateaus P_i carrying audit's C_i.
   - Transition families between them.
   - Edges: the rescaled edge orbit, run as a two-world gated system with a modified verdict Ψ.
   - Vertices: the ideals I_i.

2. **The couplings (§3).** The coupling constraints of this architecture are derived exactly and listed as K0–K8. Each is a condition linking the acceptances of T (or of C_i, or of I_i) to those of neighbouring or edge models. The status of each is given in the table in §3.

3. **First violated coupling: K0, T's own section on the plateau. This is an exact obstruction (Theorem B, PROVED; CHECKED).**
   - *The forced repair.* Let X* be T with the majority answer on a small cone S ⊂ M_1 on which T is not A and every 2- or 3-defender says A. X* preserves the guards, so audit's guarantee says it must be repaired. It can be repaired only by a 1-defender C.
   - *The killed rival.* Let Y_C be C on M_2 ∪ M_3 (guards included) and T on M_1 ∪ U.
   - *Why T loses everywhere.* The forced record rec(C, X*), accepted at worlds 2 and 3, closes a 3-cycle with rec(T, Y_C) and a strict guidance link at each of those worlds. World 1 is refused by strict (G).
   - *Conclusion.* In every extension of audit's relation satisfying strict (G), (IB) and (TC), T is defended against Y_C at no world.
   - *Scope.* This holds for every subcollection of repairs that meets audit's covering guarantee. It holds for audit's strongest version (target-reference base, defenders C_1, C_2, C_3, two-sided filter). It also holds for variable defenders drawn from the maximal V_2, V_3, as long as the 1-defender used is pointwise no worse than T at world 1.
   - *Consequence.* No selection containing T works, including the plateau architecture. Following audit's §13 KKM argument, no extension without distinct all-world ties satisfies (S).
   - *Not covered.* The case of T unselected but all-world tied with a selected model (audit's caveat), and constructions that give up the covering guarantee for rivals like X*.

4. **Audit's §13 rival Y, exactly (Theorem A and Theorem P, PROVED; CHECKED).**
   - *Full filtered batch.* The full filtered batch kills every defence of T against each pure two-guard rival Y_jk = T[G_j ∪ G_k → majority]. Audit's §13 Y is Y_12. The killing records are rec(C_i, X^(w)) with X^(w) = I_w off the guards, w ≠ i, and they pass both exposure tests.
   - *Kill-free subcollections.* A subcollection is kill-free when no installed label-i repair has its rival weakly w_i-better than its defender off the guards. For such a subcollection, adding T's three defences σ_jk keeps (G), (IB) and (TC), keeps T undominated, and creates no ties.
   - *They exist.* Kill-free covering subcollections exist for all 8 choices of defending worlds (exact, complete cell search).
   - *What this settles.* Audit's §13 question is answered both ways: Y itself is defensible, but Theorem B's Y_C is not.

5. **Vertex and tilt couplings (§7, PROVED; CHECKED).**
   - *The T-trap.* If the record ρ_jk = (G_j ∪ G_k, A → B) is accepted at both j and k, then Y_jk dominates T.
   - *A coupling it causes.* rec(I_i, I_i[W → T]) is exactly ρ_jk. So by closed sections, i-defenders that repair I_i[W → T] at every world cannot accumulate at e_i.
   - *Which designs this kills.* The "continuum of tilts from C_i to I_i" option fails if the variable-defender batch is installed: T becomes dominated. So does a C_i-plateau touching e_i when C_i repairs I_i[W → T].

6. **Edges (§8, PROVED; CHECKED).**
   - *The naive template fails.* Take the gate2d template on each edge: lowest keys for off-edge steps and verdict Φ = 2on − off at both support worlds. It accepts records that kill all six (pair, world) defences of T. With equal guard masses, an explicit instance is given.
   - *The repair.* The verdict Ψ_w = min(Φ_w, Φ_w − Φ_{w'}) keeps everything gate2d gives on the edge: closed sections, covering, acyclicity and undominated edge models.
   - *Why the repair works.* Every kill-capable record out of an edge model at one support world is a pure worsening at the other support world (proof, plus an exhaustive per-problem check on 43 edge models). So Ψ refuses it.

7. **Plateau geometry (§3, PROVED; CHECKED).**
   - *Isolation.* Under audit's covering guarantee, every selected model other than T lies outside X_G, at measure-distance at least η > 0 from T. So the interpolation into the plateau must jump, and the rescaled family cannot be used near T.
   - *Edges.* The closure of the plateau cannot contain the edge index carrying T's projection model E_{π_k(c*)}, and it can meet at most two open edges (the Λ coupling).

8. **Nearby reachable target (§10, SCREEN).** Do not repair one-label rivals like X* with defenders. Dominate them instead with selected models of the opposite edge Δ_23, away from the projection point.
   - For four such edge models, the record is admissible under (G) at all three worlds.
   - It fully kills no pair's defence (the single-record screen, exact).
   - Audit's C_1, by contrast, fully kills the pair {2,3}.

---

## 1. Setting and notation

- **Problems and advice.**
  - Problems are lines g ∈ R³ (mod sign). The classes are M_w (minority world w) and U (unanimous).
  - Advice is given relative to the majority orientation h: A (majority answer; correct on U), S (silence), B (minority answer), X (contradiction).
- **Ranks.**
  - On M_w at world w: B 0, S 1, A 2.
  - On M_w at the two majority worlds: A 0, S 1, B 2.
  - On U: A 0, S 1, B 2. Contradiction X has rank 3 everywhere.
  - "A-ward" refers to the order A > S > B.
- **Guards and defenders.**
  - Guards G_k ⊂ M_k, with W := G_1 ∪ G_2 ∪ G_3. On G_k, T says B (audit's "minority answer"), strictly.
  - An i-defender says B on G_i and A on G_j, G_k. X_G is the set of models equal to T on W.
- **Records.** A repair rec(C, X), with C an i-defender, has label i.
  - It satisfies D ⊇ G_j ∪ G_k (C = A, X = B there) and D ∩ G_i = ∅.
  - Write D' := D ∖ W.
  - It is installed at every world, together with all its (IB) copies.
  - It is strict (audit Thm 2).
- **Two-guard rivals.**
  - Y_jk := T[G_j ∪ G_k → A]: it is a strict improvement of T at the third world i.
  - σ_jk := rec(T, Y_jk) = (G_j ∪ G_k, B → A).
  - ρ_jk := the reverse of σ_jk.
- **General two-guard rival.** Y is T with A on G_j ∪ G_k and any change y on a set N off the guards, with y weakly i-better than T. Then T ⋠_i Y by strict (G), and T must defend Y at j or k.

---

## 2. The architecture 𝔄

- **Index regions.** Δ is cut into closed regions, each with its own models:
  - P₀ ∋ c* (central): C_p = T.
  - P_i (near e_i, not containing e_i): C_p = C_i.
  - Transition regions between P₀, the P_i and the edges: coherent models still to be chosen (for example the rescaled family reparametrised; see K2 for why that fails near P₀).
  - Open edges Δ_ij: C_r = E_r, the rescaled edge orbit (an imprecise segment of Δ_ij; this satisfies the face lemma).
  - Vertices: I_i (forced: C_{e_i} ⪯_i I_i requires C_{e_i} = I_i by strict (G)).
- **Relation.** Audit's R⁺ (any subcollection meeting its covering guarantee), together with:
  - T's guard defences (σ-records);
  - on each edge, a two-world gated system on the records out of edge models (§8);
  - whatever further comparisons the transition models need.
- **Sections.** A_w(X) := {p : C_p ⪯_w X}. They must be closed, satisfy KKM (e_w ∈ A_w, and supp p ⊆ the worlds that accept), and each C_p must be undominated.

---

## 3. The coupling constraints (PROVED unless marked)

Fix a rival X and write W_C(X) := {w : C ⪯_w X}.

**K0 (plateau competitiveness).** For every X, W_T(X) ≠ ∅. This is forced by C_p = T on P₀ ≠ ∅.

**K1 (plateau boundary).** For every X there is a neighbourhood N_X of P₀ such that, for q ∈ N_X ∖ P₀, C_q ⪯_w X implies w ∈ W_T(X). The same holds for P_i with W_{C_i}(X).
- *Proof.* If w ∉ W_T(X), then A_w(X) is closed and disjoint from the compact set P₀, hence at positive distance from it. ∎
- *In words.* Near the plateau, the transition models may defend X only at worlds where T itself defends X.

**K2 (isolation, from audit's guarantee).**
- (a) Every selected C_q ≠ T lies outside X_G.
- (b) Hence ρ(C_q, T) ≥ η > 0 for a constant η depending only on the guards.

*Proof.*
- (a) Audit's relation strictly dominates every X ∈ X_G ∖ {T}.
- (b) A coherent D_K that differs from T on a non-null part of a guard has K containing a point m with m·g ≤ 0 for some guard g. Since T accepts g with a uniform margin, m lies outside a fixed neighbourhood of M. The lines strictly separating m from M lie in {D_K ≠ T}, and their measure is bounded below uniformly over the compact set of such m. ∎

*Consequences.*
- K1 is a non-local coupling: the neighbours of P₀ are far from T.
- Rescaled models near c* are T on the guards (CHECKED in `s8` (a): p = c* ± 1/3000, 1/1000, 1/600). So they are dominated and cannot interpolate into P₀.

**K3 (plateau–edge contact).** If r ∈ cl(P₀) ∩ relint Δ_ij, then T ⪯_w X ⇒ E_r ⪯_w X for every X and every w, including the off-support world k. Two consequences:
- **(K3a) The projection point is excluded.** cl(P₀) does not contain an index carrying E_m with m = π_k(c*). (On Δ_12, m = (1/2, 1/2, 0).)
  - Take X := T[N → A] with N ⊂ M_k non-null and T ≠ A on N. Then W_T(X) ⊆ {k}: X is a strict improvement of T at i and j.
  - T is weakly A-ward of E_m on M_i ∪ M_j (PP12 (P1), imported; CHECKED in `s10`).
  - E_m = A on M_k.
  - So X is a strict world-k improvement of E_m, and strict (G) refuses E_m ⪯_k X. ∎
  - For r ≠ m some cell of M_i ∪ M_j has E_r strictly A-ward of T, and the argument fails there (`s10`).
- **(K3b) The Λ coupling.** Λ is a strict world-k improvement of every edge model on Δ_ij (PP12 Lemma 3.1(b); CHECKED in `s10`). So T ⪯_k Λ forces cl(P₀) to avoid relint Δ_ij. Since W_T(Λ) ≠ ∅, cl(P₀) meets at most two open edges.

**K4 (vertex closure).**
- C_{q_n} ⪯_w X with q_n → e_i implies I_i ⪯_w X.
- Combined with the T-trap (§7), e_i ∉ A_j(X_I) ∩ A_k(X_I), where X_I := I_i[W → T].

**K5 (selected i-pattern models).** For every selected S with the exact i-pattern on the guards, the record rec(S, S[W → T]) is ρ_jk. So S ⪯_j S[W → T] and S ⪯_k S[W → T] cannot both hold (T-trap).

**K6 (edge–interior closure).** Let r ∈ relint Δ_ij with off-support world k, and let interior q → r. If C_q ⪯_k X along a sequence, then E_r ⪯_k X. So the interior models near r must refuse at k:
- every X that strictly improves E_r at world k;
- every X whose record from E_r is of kill type for T's k-defences (K7).

**K7 (guard couplings; Lemma K, §4).** T can defend a two-guard rival Y on the pair {j,k} at w ∈ {j,k} only if no record accepted at w closes a 3-cycle with rec(T, Y) and a guidance link.

**K8 (vulnerable selected models).** Let a selected S say B on two full guards G_j ∪ G_k. Then S is strictly dominated as soon as a label-i repair of S[G_i → B] is installed. The (IB) copy (S[D → C], S) of rec(C, S[G_i → B]) ends at S, because that repair's D misses G_i. So the allocation must not install such repairs.

**Status table** (tests against audit's relation):

| coupling | status against audit's relation | reference |
|---|---|---|
| K0 | **VIOLATED** in every subcollection meeting audit's guarantee | Theorem B (§6) |
| K0 restricted to the pure Y_jk | violated by the full filtered batch; satisfiable by kill-free subcollections | Theorems A, P (§5) |
| K1 | non-local, because of K2; no violation found; competitiveness of the transition models OPEN | §3, §9 |
| K2 | holds; forces a jump at ∂P₀ | `s8` (a) |
| K3 | axiom-level; satisfiable by keeping cl(P₀) off the edges | `s10` |
| K4, K5 | violated by a tilt continuum with the variable batch, and by a C_i-plateau touching e_i that repairs X_I | §7, `s8` |
| K6 | satisfiable at the edge model itself; the interior side is OPEN | §8 |
| K7 at the edges | violated by the naive gated template; satisfied by Ψ | §8, `s9` |
| K8 | allocation constraint; avoidable when the one-guard restoration has another exposed label | §3 |

---

## 4. Lemma K: the kill cycles

The setting:
- Y is a two-guard rival on {j,k} (third world i), with Y weakly i-better than T off the guards.
- e := rec(T, Y), accepted at w ∈ {j,k}.
- R = rec(c, x) is any record accepted at w.

A **kill** is a 3-cycle at w made of R, e and a guidance link. It violates (TC) whenever the guidance link is strict, and also whenever R is strict (audit's repairs are strict). There are two orders, and each problem must satisfy one of the following (`pp16lib.cycle_atom_ok`; here ≤_w compares world-w ranks).

| problem lies in | K1: A₀ –R→ B₀ –e→ Z₀ –G→ A₀ | K2: A₀ –e→ B₀ –R→ Z₀ –G→ A₀ |
|---|---|---|
| D_R ∩ D_e | x = T and y ≤_w c | y = c and x ≤_w T |
| D_R only | x ≤_w c | x ≤_w c |
| D_e only | y ≤_w T | y ≤_w T |

*Proof.* Write out the (IB) copy conditions.
- In K1: A₀ = c and B₀ = x on D_R; B₀ = T and Z₀ = Y on D_e; A₀ = B₀ off D_R and Z₀ = B₀ off D_e.
- In K2: A₀ = T on D_e and B₀ = c on D_R.
- In both orders the closing link needs Z₀ weakly w-better than A₀. ∎

**Special case: pure two-guard rivals (N = ∅).** A label-i repair kills σ_jk at w iff x ≤_w c on D' (strict where x ≠ c). Call this K(i, w).

**Only label-i repairs can kill σ_jk (PROVED).** In a 3-cycle at w that contains σ_jk@w:
- G_w goes B → A, a w-worsening. Its return A → B is a w-improvement, which only a repair labelled ≠ w can perform (guidance, target-reference records and σ's cannot).
- If that repair has label k, it also changes G_i from A to B. Undoing this at w would be a w-improvement on M_i, and no link can perform it. Contradiction.
- Hence the repair has label i. The third link then changes no guard, so it is guidance (a target-reference link would need x = T on D', which violates (E_T)).
- Two σ's at the same world never share a cycle: G_w would change twice in the same direction.

So **the only (TC) violations involving one σ are the K(i, w) cycles.**

---

## 5. Audit's §13 rival: Theorems A and P

**Theorem A (PROVED; CHECKED, `s2`).** In the full filtered batch with defenders C_1, C_2, C_3, T is defended against Y_12, Y_13, Y_23 at no world, in any extension satisfying (G), (IB) and (TC).

*Proof.*
1. Fix i ≠ w and let l be the third index. Put X^(w) := I_w off W and T on W, which lies in X_G.
2. On M_l both i and w are majority worlds. C_i is weakly A-ward of T there, and strictly so somewhere (PP13 Lemma 3.2). Because the B-region of C_i is a strict sub-down-set of T's, just outside its boundary C_i = S and T = B.
3. So N_{i,w} := {g ∈ M_l ∖ W : T = B, C_i = S} is non-null, and I_w = A there.
4. On N_{i,w}: C_i ≠ X^(w) ≠ T and C_i ≠ T. This gives (E_T) and (E_C).
5. I_w is w-optimal, so x ≤_w c holds on D'. This is K(i, w).
6. The six pairs (i, w), w ≠ i, kill σ_jk at both j and k for each pair. At the third world, guidance refuses. ∎

*CHECKED.* For all six (i, w): exact generic witnesses with T, C_i, I_w = B, S, A, and the cell-model triangle A ⪯_w B ⪯_w Z ≺_w A.

**Theorem P (PROVED).** Choose w_i ∈ {j,k} for each label i. Call a subcollection **kill-free** if no installed label-i repair satisfies K(i, w_i). Then R⁺_kf ∪ {σ_jk@w_i, with all copies} satisfies:
- (G) and (IB);
- (TC) (§4);
- T undominated: no σ-copy ends at T, since its new side is A on the guards.
- C_i undominated (a σ-copy into C_i is refused at world i by strict (G)).
- no new ties (ρ is never installed).

**Kill-free covering subcollections exist (CHECKED, `s3`, exact and complete).**
- The off-guard space is partitioned into the 97 open cells of the arrangement of the 15 planes {g_j = 0} ∪ {v·g = 0 : v a vertex of M, K_1, K_2, K_3}. These are all the cells (completeness proof in the docstring; random check in `s3b`).
- For all 8 choices of (w_1, w_2, w_3), every X ∈ X_G ∖ {T} has a two-sided-exposed defender C_i with K(i, w_i) false.
- *Sanity check.* No X ≠ T is unexposed for all three defenders, which is audit's Lemma 4.

So audit's §13 Y is defensible, but only if the subcollection is chosen. The next section shows that this does not rescue K0.

---

## 6. Theorem B: the forced repair

**Hypotheses.**
- **(H0)** There is a non-null S ⊂ M_1 ∖ W on which T ≠ A and every 2- or 3-defender that may be used says A.
- **(H1)** Audit's guarantee holds: every X ∈ X_G ∖ {T} is strictly dominated by an installed repair.
- **(H2)** The repairing 1-defender C is pointwise no worse than T at world 1.

**Definitions.**
- X* := T[S → A]. It lies in X_G and differs from T.
- Y_C := C on M_2 ∪ M_3 and T on M_1 ∪ U. On G_2 ∪ G_3 it says A, and on G_1 it says B.

**Lemma B1.**
- (a) (E_T) fails for every 2- or 3-defender against X*.
- (b) So by (H1) some rec(C, X*), with C a 1-defender, is installed at every world.
- (c) If (H2) holds, then (C, X*) is two-sided exposed whenever C ≠ T off W ∪ S.

*Proof.*
- (a) {D_K ≠ X*, X* ≠ T} = S ∩ {D_K ≠ A} = ∅.
- (c) On S, T ≠ A and C ≤_A T, so C ≠ A = X*. This gives (E_T). Off W ∪ S, X* = T, which gives (E_C). ∎

**Theorem B (PROVED).** Under (H0)–(H2), every extension of audit's relation satisfying strict (G), (IB) and (TC) has T ⋠_w Y_C for w = 1, 2, 3.

*Proof.*
1. **World 1.** C ≤_1 T pointwise, so C is weakly A-ward of T on M_2 ∪ M_3. Hence Y_C is a weak world-1 improvement of T. It is strict on G_2 ∪ G_3, so strict (G) refuses T ⪯_1 Y_C.
2. **Setting up the cycle at w ∈ {2, 3}.** Let D := {C ≠ X*}. Put A₀ := C on D, T off D, and B₀ := X* on D, T off D. Then (A₀, B₀) is an (IB) copy of rec(C, X*), which is accepted at w.
3. **The second link.** Let D_e := {Y_C ≠ T} = (M_2 ∪ M_3) ∩ {C ≠ T}. On D_e, X* = T ≠ C, so D_e ⊆ D and B₀ = T there. Put Z₀ := B₀[D_e → Y_C]. Then (B₀, Z₀) is a copy of rec(T, Y_C). Suppose T ⪯_w Y_C.
4. **Comparing Z₀ with A₀.**
   - On D_e, Z₀ = C = A₀. Off D, both equal T.
   - D ∖ D_e ⊆ M_1 (C is correct on U, and C = X* on G_1). There Z₀ = X* ∈ {T, A}, while A₀ = C ≤_A T.
   - So Z₀ is weakly w-better than A₀, because w is a majority world on M_1. It is strictly better on S ∩ {C ≠ A}, which is non-null.
5. **Conclusion.** A₀ ⪯_w B₀ ⪯_w Z₀ ≺_w A₀ violates (TC). ∎

**Corollary B2.**
- No selection in which T is selected, including the plateau architecture, satisfies (S) in any extension of audit's relation.
- No extension without distinct all-world ties satisfies (S): by KKM, T would have to be selected (audit §13).

**When (H0)–(H2) hold.**
- **Audit's protocol (§11: only C_1, C_2, C_3).** (H0) needs C_2 = C_3 = A ≠ T on a non-null subset of M_1. The A-regions of C_2 and C_3 are the A-region of T translated by log a along the two axes of the M_1 chart. A point just outside the A-region of T, where its boundary is strictly decreasing, lies in both translates. CHECKED: the cell (M_1, T = B, C = (B, A, A)) exists (`s3`). (H2) holds for C_1 (audit §11).
- **Variable defenders from the maximal V_2, V_3 (audit's guard shape).** Every m ∈ V_2 ∪ V_3 has m_1 < 1/(L+1), so on h = (−1, t, t) the product m·h = −m_1 + t(1 − m_1) is positive once t ≥ 1/L. T ≠ A there iff t ≤ (1 + ε/c)/2. The interval (1/L, (1 + ε/c)/2) is nonempty for every ε ∈ (0,1) and every admissible L > (1−c)/c, because 2(1−ε)² < (1+2ε)(2+ε). CHECKED at h₀ = (−1, 1, 1): all four vertices of each maximal V, on the whole S-cone (`s6`).
- **(H2) for variable 1-defenders.** It holds for every cevian tilt toward e_1 and for I_1 (PP13 Lemma 3.1, imported). CHECKED for C_1 and for tilts b = 9, 40, 1000, and for I_1 (`s6`).

*CHECKED (`s6`).* For each of these defenders, on the exact cell model (the arrangement cells, the S-cone and the guard cones): X* ∈ X_G; exposure; Y_C a strict world-1 improvement of T; both copy identities; and a strict guidance link at worlds 2 and 3.

*CHECKED (`s5`, exact and complete).*
- Searched over all cell-wise rivals X₁, X₂, unexposed for the two other defenders, together with a two-guard Y.
- Forced kills at both worlds of a pair exist for every label (12 configurations).
- *Supersedes `s4`.* `s4` showed that a fixed defending world per pair fails against general two-guard rivals for all 8 choices; `s5` and Theorem B supersede it.

**Scope, exactly.** The theorem uses only strict (G), (IB) and (TC), together with audit's installed repair of X*.
- **Not covered:**
  - T unselected but all-world tied with a selected model (the cycle does not transfer to the tie partner);
  - 1-defenders that are not pointwise no worse than T at world 1;
  - giving up (H1) for rivals of X*'s kind (§10).

---

## 7. Vertices, tilts and the T-trap (PROVED; CHECKED in `s8`)

**T-trap.** If ρ_jk is accepted at both j and k, then:
- Y_jk ⪯_j T and Y_jk ⪯_k T as copies of ρ_jk;
- Y_jk ⪯_i T by guidance, since A is i-best on M_j and M_k;
- T ⋠_i Y_jk by strict (G).

So T is dominated.

**Vertex coupling.** rec(I_i, I_i[W → T]) = ρ_jk (CHECKED). The same holds for rec(S, S[W → T]) for any selected S with the exact i-pattern on the guards. By closed sections (K4, K5):
- In the full filtered batch over variable defenders, the tilts C_b toward e_i are i-defenders, and (C_b, I_i[W → T]) is two-sided exposed (CHECKED for b = 10, 10², 10³, 10⁴). So a continuum of tilts reaching e_i forces I_i ⪯_j and I_i ⪯_k of I_i[W → T]. Then T is dominated.
- The same holds at an interior tilt b₀: (C_b, C_{b₀}[W → T]) is exposed for b ↑ b₀ (CHECKED for b₀ = 10, b = 9, 9.9, 9.99).
- In audit's three-defender protocol, the coupling only requires that P_i not touch e_i if C_i repairs I_i[W → T]. Along the path from P_i to e_i the sections then switch.

---

## 8. Edges

**The naive template kills (PROVED; CHECKED in `s9` (a)).** Edge model E on Δ_13 at r = (1/20, 0, 19/20), with guard pattern (A, A, B). Take the record x: B on G_1 and G_2 (mass 1 each), and B on one class-1 cell (mass 1/2).
- At world 1 the added steps lie only in M_2, the off-edge class with the lowest keys, so the gate passes. Φ_1 = 2·2 − 3 = 1 ≥ 0, so the naive rule accepts.
- The record closes K1 with σ_12 at world 1.
- By symmetry, edge models near e_3 on Δ_13 and Δ_23, near e_2 on Δ_12 and Δ_23, and near e_1 on Δ_12 and Δ_13 kill the six (pair, world) defences.

**The repaired verdict Ψ (PROVED).** On edge Δ_ab, at support world a with other support world b, put Ψ_a := min(Φ_a, Φ_a − Φ_b).
- **Closed sections.** A_a(X) ∩ edge = {Ψ_a ≥ 0} ∪ {rec(E_r, X) a weak a-worsening}, a union of two closed sets. Here Ψ_a is continuous (as in gate2d (V1)). A pure a-improvement has Ψ_a ≤ Φ_a < 0.
- **Covering.** Φ_a + Φ_b ≥ 0 holds in the three-world edge setting:
  - changes on M_c, on U, and into X add steps at both support worlds;
  - regular changes on M_a ∪ M_b are two-world-like.

  So max(Φ_a, Φ_b) ≥ 0, and the larger of the two has Ψ ≥ 0.
- **Acyclicity and threshold structure.** Acyclicity holds because any sub-verdict of a gated rule stays acyclic (gate2d Lemma 1). The threshold structure of edge models comes from PP14 Prop 3.6 (imported), with all off-class steps keyed lowest. So edge models are undominated within the edge system and competitive on {a, b}.
- **Kill-capable records are refused.**
  - Every record out of E that can close a kill cycle at a, for any two-guard Y and either order, is problem-wise a weak b-worsening. CHECKED exhaustively on 43 edge models, all edges and pairs, both orders (`s9` (b)).
  - Such records contain no contradiction and no change on U (the table in §4 excludes both). On M_c, where E = A, every change worsens a and b by the same rank, since both are majority worlds there. On M_a ∪ M_b the ranks at a and b are opposite, and a weak b-worsening adds no b-step, so it adds no a-step either. So on_a ≤ on_b.
  - Hence Φ_a − Φ_b ≤ −off_a < 0, because the record returns G_a from A to B, which is an a-improvement. Therefore Ψ_a < 0.
- **The other support world.** Such a record is a weak b-worsening, so world b accepts it by guidance. Edge competitiveness is not affected.

**OPEN.** (TC) between the Ψ-edge records and audit's repairs and target-reference records, beyond the kill cycles.

---

## 9. Item 3: competitiveness across the simplex, and KKM near the edges

- **Plateau.** K0 fails (Theorem B). Nothing else is needed to sink the architecture as posed.
- **Near the edges.**
  - If the plateau comes near an edge, K3 transfers every T-acceptance to the edge model, including at the off-support world. That is excluded at the projection point and on all three edges at once.
  - If it stays away (cl(P₀) ⊂ int Δ), the transition models must switch from W_T(X) (K1) to the worlds of the edge model.
  - For X := T[N → A] with N ⊂ M_k, the only plateau world is k, while E_{π_k(c*)} refuses k. So the transition path toward that projection point must contain a model accepting X both at k and at i or j. This is allowed but forced (K1, K3a).
- **KKM near the edges.** Consider a rival that strictly improves an edge model E_r at its off-support world k, for example E_r[N → B] with N ⊂ M_k.
  - Its section A_k avoids a neighbourhood of r, so its KKM dominator is an interior transition model.
  - E_r itself accepts at both support worlds by guidance.
  - The Ψ-system never accepts at k beyond guidance, so all such KKM dominators must come from interior transition models.
  - Those models are at distance at least η from T (K2).
- **OPEN.** Whether transition models exist that meet K1 and K6 and supply these dominators.

---

## 10. Nearby reachable target

Theorem B rests on one design choice: audit's guarantee that every guard-preserving rival is dominated **by a defender repair at every world**. Rivals like X* are improvements of T at worlds 2 and 3, made on M_1. Their natural KKM dominators sit toward the edge Δ_23, not at C_1.

- **Proposal.** Keep the architecture and Theorem P. Replace (H1) for one-label rivals of X*'s type by "strictly dominated by a selected model". Take that model from the opposite edge (Δ_23 for X*), away from the projection point.
- **Screen (`s7`, exact).** For each candidate D*, it is checked whether rec(D*, X*), installed at every world, fully kills a pair's defence (for some two-guard Y, at both of its worlds).

| D* | X* strictly improves D* at worlds | pairs fully killed |
|---|---|---|
| audit's C_1 (control) | none | {2,3} |
| away-tilts ν(b,1,1), b ∈ {1/2, 1/4, 1/10, 1/100} | 1, so they cannot dominate X* | none |
| E at (0, 1/2, 1/2), the projection point | 1 | none |
| E at (0,1/3,2/3), (0,2/3,1/3), (0,2/5,3/5), (0,3/5,2/5) | **none** | **none** |

- **Remaining checks.**
  - The edge models (0, 2/5, 3/5) and (0, 3/5, 2/5) say B on two guards. They are vulnerable under K8, so the allocation must avoid the corresponding repairs. The edge models at (0, 1/3, 2/3) and (0, 2/3, 1/3) are not vulnerable.
  - Still OPEN: (TC) of these records with the repairs, the target-reference base and the Ψ-edge records; a record-level rule that identifies the "one-label" rivals; and closedness of the resulting sections.

---

## 11. Scripts (`PP16_py/`)

| script → output | content | label |
|---|---|---|
| `pp16lib.py` | exact geometry; complete plane-arrangement cell enumeration; kill-cycle predicate; pair-kill search | library |
| `s1_setup.py` → `.out` | guards, defender and ideal patterns on cones, Prop. 1 hypotheses, K_i ⊂ V_i | CHECKED |
| `s2_theoremA.py` → `.out` | Theorem A: six exposure witnesses and kill triangles | CHECKED |
| `s3_allocation.py`, `s3b_completeness.py` → `.out` | Theorem P allocations (8/8 kill-free); Lemma 4 sanity; completeness of the cell enumeration | CHECKED |
| `s4_allocation_general.py` → `.out` | a fixed defending world fails against general two-guard rivals (superseded by s5) | CHECKED |
| `s5_forced_kills.py` → `.out` | forced kills for every label (12 configurations) | CHECKED |
| `s6_theoremB.py` → `.out` | Theorem B on the cell model, for C_1, three tilts and I_1; maximal V's | CHECKED |
| `s7_nearby_screen.py` → `.out` | §10 screen of the opposite-edge dominators | CHECKED (screen only) |
| `s8_isolation_vertex.py` → `.out` | K2 isolation; vertex and tilt exposures; ρ_12 identity; T-trap ranks | CHECKED |
| `s9_edges.py` → `.out` | naive edge kill; per-problem certificate for Ψ | CHECKED |
| `s10_plateau_edge.py` → `.out` | K3a projection exclusion; Λ against edge models | CHECKED |
