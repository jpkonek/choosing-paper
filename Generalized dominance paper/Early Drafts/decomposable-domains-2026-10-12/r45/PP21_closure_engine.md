# PP21. An exact closure engine for rules I–IV: where clean closures exist on cells, and where F1/F2 is forced

22 October 2026. One author; not refereed.

**Labels.**
- PROVED: a complete argument is given here.
- CHECKED: exact finite computation in rational arithmetic, exhaustive where stated and otherwise on the stated sample.
- CONJECTURE: unproved.

No NUMERICS were used.

**Scope.** All computation concerns finite cell models, in which cells are atoms.
- Sections are not modelled.
- KKM is replaced by an explicit finite list of dominator obligations.
- §7 lists the continuum implications that are omitted.

**Nothing here is evidence about (S).** The finite results only tell the measurable work which request patterns close cleanly and which force F1/F2. Each failure comes with a derivation that can be turned into a proof.

**Scripts.** They are in `r9/PP21_py/`. Run `python3 -B <script>` inside that folder; outputs are in the matching `*.out` files.
- `cells.py`: geometry, exact coherence, catalogue, splitting.
- `engine.py`: the closure, F1/F2 and derivations.
- `search.py`: obligations, depth-first search (DFS), greedy search, minimisation.
- `verify.py`: independent checks.
- Experiments: `exp_single`, `exp_pairs`, `exp_props`, `exp_joint` (parts a–f), `exp_inert`, `exp_deadends`, `exp_partial`, `exp_partial_twin_bytype`, `exp_split` (t, p), `exp_tight`, `exp_tight_diag`, `exp_corner`, `exp_verify_big`, `exp_defmap`, `corner_cut`, `lemmaQ_check`.

The coordinator's three points are covered here:
- Prop S rival and defender pair: §4.
- Where F2 relies on cell-level coherence: §1 and §7.
- Single-world ties: §§3–5.

---

## 0. Summary

| Question | Answer | Label |
|---|---|---|
| Does the engine compute the least closure under I–IV, with F1/F2 and derivations? | Yes. The triangle search is complete (Lemma 2.1). The engine agrees with a model-level brute-force fixpoint on 40/40 random small instances. 27 clean closures (J1 ×12, J2 ×2, twin ×2, 6 tightening and 5 corner rounds) were re-verified from the definitions, with 0 errors. | PROVED + CHECKED |
| One rival and its defender | Every failure falls into four named types: the defender is nowhere better at some world; exposure (Lemma 0.4); T defends at a world where the defender strictly improves T; Lemma 0.2. 0 unclassified failures in 16 rivals × 3,202 defenders. A single-world tie T ~_w C succeeds exactly when T R_w C does. | CHECKED |
| Pairs of choices | Every minimal failing set has 2 requests, or 4 when single-world ties are used. Shapes: two-link F1 (exact criterion, Lemma 2.4); exposure against *another* protected model; short chains through completed triangles. | CHECKED |
| Referee's Prop S on geometric cells | Reproduced: a coherent defender pair, each harmless alone, leaves T with no defence against T[H_1 ∪ H_2 → maj]. The two-link criterion matches the engine on 36,882/36,882 tests. | CHECKED |
| Joint class: X*, Y_12, Λ_T, V_{c*}; fills of single cells, of cell pairs, and 1,000 random fills | Clean closures exist for every defender order, for weak and tie-first defences, for all 36 choices of T's worlds against the named four, and in a strict variant that treats every all-world tie as F2. | CHECKED |
| Shape of the clean solutions | With weak defences they are **inert**: rules II–IV add nothing. The fewest-changes order uses only **tightenings**, which agree with T wherever T answers. | CHECKED |
| Partial sources T[D′ → C] (PP19 Prop 9) | These separate the choices. Defenders with large support that serve fills harming different worlds leave T undefended against some of their own partial sources (59 cases in J1, 16 in the twin model, all certified by two-link kills). Small or corner tightenings: 0 such cases. | CHECKED |
| Corner tightenings | A corner tightening K ⊆ M keeps the two vertices v_i, v_j of M. Its new answers are all wrong at world k (Lemma Q), so T defends against it, and against all its partial sources, by guidance. | PROVED |
| Refinement | Twin splitting commutes with closure for lifted requests, so both failures and clean closures persist (Lemma 2.2). With half-cell rivals added, and in a perturbed model (31 cells), clean closures still exist. | PROVED + CHECKED |

**What this suggests (§8).**
- Aim the measurable theorem at an **inert extension**: verify the pairwise, pointwise conditions of Lemma 2.3 rather than run a closure.
- Build it from **corner tightenings**, assigning to each rival a tightening at a world the rival harms.
- The open pieces are exposure for fills near T's boundary, Prop S between installed T-defences and defenders, and dominators for the tightenings' own partial sources. The last of these is where the finite search last got stuck.

---

## 1. The finite model

**Base model** (`cells.py`). ε = 3/10, c = 7/30, T = D_M with M = c·1 + εΔ (the PP17 instance, d = 1/10, L = 5). There are 25 cells, each a representative gamble.
- On the axis g = (−x at i, 1, 1), for each world i:
  - J_i at x = 1/2: T answers with the majority.
  - Gp_i, R_i and B_i at x = 6/5, 17/10 and 19/10: T is silent; the uniform prior gives the majority answer.
  - A_i and Gm_i at x = 21/10 and 3: T is silent; the uniform prior gives the minority answer.
- O_i, off the axis, e.g. (−2, 1/2, 8/5): T is silent.
- W_ij: T gives the minority answer.
- U: unanimous.

T is silent on 18 cells, which represent audit's A_i, B_i, R_i together with generic majority- and minority-favouring regions.

**Coherence is exact** (PROVED; CHECKED). A vector is coherent iff some closed convex K ⊆ Δ realises it at each representative with strict inequalities. Two tests are implemented:
- (a) Polygon clipping in the simplex.
- (b) The meet-closure of the sign vectors of the 202 open faces of the line arrangement {m·g_k = 0}. A meet of faces is realised by the convex hull of interior points; conversely, any realising K can be pushed into open faces.

The catalogue has **27,478** coherent vectors. The two tests agree on all of them and on 9,000 random mutations (`cells.out`).

**Cells see only conic sets.** By strictness, a coherent cell vector is realised on small open conic neighbourhoods of the representatives. The referee's Lemma H (a non-conic splice of a coherent model is incoherent) is therefore invisible on cells. Every F2 found, and every F2 *avoided* because a splice happens to be coherent on cells, relies on the cell-level test. The strict variant in §5 removes the avoided cases.

**Refinements.**
- Twin split: the 18 silent cells are doubled with equal gambles, giving 43 cells. Coherent models must agree on twins; rivals may fill half a cell.
- Perturbed split: 6 extra nearby gambles, 31 cells, catalogue 70,274.
- Corner model: 6 cells added where corner tightenings give minority answers (§5.4), 31 cells, catalogue 91,482.

---

## 2. Engine and lemmas

**Representation** (`engine.py`). Acceptance at w depends only on rec(A, B), so R_w is stored as weak guidance (implicit) plus an explicit set of installed records. Rule I is then automatic.

Requests:
- dom(C, X): C enters P, and C R_i X is installed at every i;
- cmp(A, B, w);
- tie(A, B, w).

Rules:
- **Rule II** tests each new record against every installed record, in both orders. When the copies compose and the inverse of the composite is accepted, it installs inv r, inv s and comp(r, s).
- **Rule III** fires on each record that is accepted at all worlds and ends at a member of P: it installs the inverse at all worlds.
- **Rule IV** registers the source of that record.

F1 is an installed weak improvement; F2 is an incoherent member of P. Every record and every member of P carries a justification, so a failure prints a numbered derivation; those quoted below are verbatim.

**Lemma 2.1 (complete triangle search; PROVED).**
- An accepted triangle with at least two installed links has two cyclically adjacent installed links. The later one is tested against the other, and the third link is the inverse of their composite.
- A triangle with exactly one installed link r forces r to be a weak improvement, since its rank changes are minus the sum of two guidance links. That is F1.
- Purely guidance triangles are trivial.

*CHECKED (`verify.out`).*
- On 3-cell spaces (64 models), the engine and a naive fixpoint over all triples agree on 40/40 random request sets: status, every record, and P.
- 97 clean closures show 0 violations over all triples.
- 27 clean closures from §§5–6 (J1 ×12, J2 ×2, twin ×2, 6 tightening rounds, 5 corner rounds) were re-checked from the definitions with clipping-based F2: 0 errors.

**Lemma 2.2 (twin splitting commutes with closure; PROVED).** Let ι duplicate twin values. Then:
- ι commutes with rec, inverse and composition;
- it preserves guidance and improvements;
- it preserves coherence.

By induction over the rules, the closure of lifted requests is the lift of the closure. *Failures and clean closures both persist verbatim. Refinement matters only by enlarging the rival class.*

**Lemma 2.3 (inert extension; PROVED).** Let Q be a set of requested records and P₀ ∋ T a set of coherent models. Suppose:
- (a) no requested record is a weak improvement at its world;
- (b) for requested r, s at the same world whose copies compose to a nonempty composite, inv(comp(r, s)) is neither guidance nor requested;
- (c) no record accepted at all three worlds, with at least one link requested, ends at a member of P₀.

Then Guid ∪ Q is closed under I–IV with neither F1 nor F2, and audit's extension theorem applies. *Proof:* by Lemma 2.1, (a) and (b) say that no accepted triangle misses a reverse, and (c) says that rules III and IV have no premise. ∎ Conditions (a)–(c) are a.e. pointwise conditions on pairs of records, so they hold verbatim for measurable records.

**Lemma 2.4 (two-link criterion; PROVED).** Suppose C R_w X and T R_w Y are accepted, with r = rec(C, X) and s = rec(T, Y). If r then s compose and comp(r, s) is a nonempty weak improvement at w, then F1 follows; likewise for s then r. For r then s this means:
- X = T on D_r ∩ D_s;
- X ≤_w C on D_r ∖ D_s;
- Y ≤_w C on D_r ∩ D_s;
- Y ≤_w T on D_s ∖ D_r;
- strictness holds somewhere.

PP19's Lemma 5.0 is the case X = T off E, D_s ∩ E = ∅, D_s ⊇ {C <_w T} ∖ E and Y ≤_w C on D_s. *Proof:* the accepted triangle (copy of r, copy of s, guidance link) makes rule II install a reversed strict guidance comparison. ∎

**Lemma P (own partial source; PROVED).** Suppose C R_w X, where X = T off E and X ≤_w C on E, strictly on a non-null part of E ∩ {C ≠ X}. Then T ⋠_w C[E → T] = T[{C ≠ T} ∖ E → C]. *Proof:* Lemma 5.0 with D_Y = {C ≠ T} ∖ E and y = C. ∎

**Lemma Q (corner tightenings; PROVED; CHECKED in `lemmaQ_check.out`, 3,667 new answers, 0 exceptions).** Let K ⊆ M be closed and convex, and contain the vertices v_i, v_j of M (where {i, j, k} = {1, 2, 3}). Then wherever T is silent and D_K answers, the answer is wrong at world k. Hence:
- D_K ≤_k T pointwise;
- T R_k D_K holds by guidance;
- T R_k T[D′ → D_K] holds by guidance for every partial source.

*Proof.* Suppose D_K accepts s·g where T is silent. The linear map m ↦ m·sg is positive on K ∋ v_i, v_j and negative somewhere on the triangle M, hence negative at v_k. From v_k − v_i = ε(e_k − e_i) we get (sg)_k < (sg)_i, and similarly (sg)_k < (sg)_j. If (sg)_k ≥ 0, then all coordinates are ≥ 0 and v_k·sg = cΣ(sg) + ε(sg)_k ≥ 0, which is false. So (sg)_k < 0. ∎

Example: the corner cut K = M ∩ {m_k ≤ t}. It gives the majority answer on part of M_k, **and the minority answer on parts of M_i and M_j** (`corner_cut.out`). All of these answers are wrong at k.

---

## 3. One rival and its defender (`exp_single.out`; CHECKED)

The test covers 16 rivals:
- X*, Y_12, Λ_T and V_{c*};
- maj/min fills of R3, A3, Gp3, Gm3 and O3;
- Y_H(Gp1+Gp2) and Y_H(Gm1+O2).

They were tested against 202 precise and 3,000 random imprecise defenders. **Every failure falls into one of these types (0 unclassified):**

- **F1dom.** At some world, C is nowhere strictly better than X. Between 163 and 655 defenders per rival.
- **Exposure (Lemma 0.4).** If C = X on {X ≠ T}, then T[D → C] is forced into P. The outcome is:
  - F2, if that model is incoherent;
  - F1, if it strictly improves T by guidance at some world;
  - a clean all-world tie with T, if it is coherent. This happened only for coherent rivals.
- **T R_w C fails** exactly when C strictly improves T at w, or X ≺_w T by strict guidance (**Lemma 0.2**).
  - Majority fill on M_k: world k only.
  - Minority fills on M_k, X* and Y_12: the other two worlds.
  - Λ_T and V_{c*}: any world.
- **Single-world ties.** T ~_w C succeeds in exactly the cases where T R_w C does. Ties never rescue a Lemma 0.2 world, but they generate the longer derivations of §4.

Derivation (X = T[R3 → maj], T R_1 C):

```
[1] world 1: T→C {…, R3:S>N, …}     <- request cmp: T R_1 C
[2] world 1: C→X {…, R3:N>P, …}     <- request dom: C R_i X
[3] world 1: {R3:P>S}               <- weak guidance
[4] world 1: {R3:S>P}               <- rule II, triangle [1],[2],[3]      F1
```

---

## 4. Pairs, Prop S and minimal failing sets (CHECKED)

**Random pairs** (`exp_pairs.out`). 2,000 pairs of individually clean choices were sampled; 1,897 close cleanly. The failures, reduced to deletion-minimal sets:

| Shape | # | Minimal set |
|---|---|---|
| two-link F1 (Lemma 2.4) | 59 | cmp T R_w C′ + dom(C, X) |
| exposure against another protected model (rule IV, F2) | 9 | dom + dom (one: dom + reg) |
| rules III×3, IV, then F2 | 1 | dom + dom |
| exposure tie, then rule II, then F1 | 1 | dom + dom |

Exposure against a defender, in the case of dom(C, Y_H(Gp1+Gp2)) and dom(C′, min[A2]): rec(C, Y_H) ends at C′, which pulls a splice of C′ into P:

```
[1] P contains C(min[A2])                                   <- request
[2-4] worlds 1-3: {Gp1:S>P, Gp2:S>P, Gp3:P>S, R3:P>S, B3:P>S, A3:P>S, W13:S>P}   <- request dom(C, Y_H)
[5] P contains PPPSSPPSPPSPPSPPSNPSSPSPP                    <- rule IV: all-world tie with C(min[A2])      F2
```

This is Lemma 0.4 with N a second protected model. **No protected model may equal a dominated rival on its dominator's disagreement set.**

**Prop S on geometric cells** (`exp_props.out`). The test used:
- majority fills on two distinct M_3 cells;
- 25 single-clean defenders for each, with T defending at world 3;
- Y_H = T[H_1 ∪ H_2 → maj], with H_1 ∈ M_1 and H_2 ∈ M_2.

Results:
- In 36,882 tests of T R_w Y_H (w = 1, 2), the engine fails **iff** the two-link criterion holds: 320 failures, 0 mismatches.
- PP19's Lemma 5.0 accounts for 256 of these failures.
- A referee-type pair occurs with E = Gp3, E′ = O3 and Y_H = maj[Gp1+Gp2]. Each defender alone leaves T a defence. Together, world 1 is killed through C, world 2 through C″, and world 3 by strict (G):

```
T R_1 Y_H: [1] C→X_E {Gp1:P>S, Gp2:P>S, Gp3:S>P, R1:P>S, …}  [2] T→Y_H {Gp1:S>P, Gp2:S>P}
           [3] guidance {Gp3:P>S, R1:S>P, …}                 [4] rule II {Gp3:S>P, R1:P>S, …}   F1
T R_2 Y_H: [1] C″→X_E′ {Gp1:P>S, Gp2:P>S, B1:N>S, …}         [2] T→Y_H
           [3] guidance {B1:S>N, …}                          [4] rule II {B1:N>S, …}            F1
```

**Dead ends of the joint search** (`exp_deadends.out`).
- Without ties, all 15 failing options are 2-request two-link kills.
- With tie-first defences, there are 344 failing options: 332 two-link and **12 deeper**, each with a 4-request minimal set. In these, completion first closes a *non-guidance* triangle T ⪯ C ⪯ X ⪯ T, where X ⪯_1 T comes from the requested tie; the completed record then forms a two-link kill with another tie:

```
[1] X→T {Gp1:P>S, B2:P>S}  <- tie   [2] T→C <- cmp   [3] C→X <- dom
[4] C→T                    <- rule II from [1],[2],[3]          (completed non-guidance triangle)
[5] T→V′ <- tie   [6] guidance {B2:P>N}   [7] {B2:N>P} <- rule II from [4],[5],[6]      F1
```

---

## 5. Joint search (CHECKED)

**Obligations** (`search.py`).
- (D): every rival needs some N ∈ P with N R_i X at all i. If X is coherent, reg(X) is offered first.
- (T): T must be competitive against every rival **and every member of P**.

Since closure is monotone, the DFS scans each obligation once and backtracks on F1/F2.

**5.1 Results** (`exp_joint_*.out`).

| Class | Rivals | Runs | Outcome |
|---|---|---|---|
| J1: named four + 36 single-cell fills + 108 two-class majority fills | 148 | 6 orders × weak / tie-first | 12/12 clean, \|P\| = 11–35 |
| J1 with T's worlds fixed against X*, Y_12, Λ_T, V_{c*} | 148 | 36 combinations × 2 orders | 72/72 clean |
| J2 = J1 + every maj/min fill of two silent cells | 796 | 3 orders | clean, \|P\| = 30–47 |
| J3 = J2 + 1,000 random fills of T's silence | 1,796 | 3 orders | clean, \|P\| = 30–47 |
| Strict: no reg, and every all-world tie is F2 | 148 / 796 | 3 orders each | clean, \|P\| = 6–20 |

**5.2 The clean solutions are inert** (`exp_inert.out`, `exp_verify_big.out`).
- With weak defences, every record in every verified clean closure (J1 × 6 orders, J2 × 2, twin × 2) is requested, and no rule-IV member arises.
- With tie-first defences, rule II adds between 24 and 107 completed records, and the closures stay clean.

In the cell model, joint cleanliness therefore never needed completion: it only had to avoid two-link kills and exposure. That is exactly the hypothesis of Lemma 2.3.

**5.3 Who defends whom** (`exp_defmap.out`, order nearT on J1). P consists of:
- T;
- V_{c*} (registered);
- T[Gp_k → maj] (the cell shadow of a k-corner cut);
- T[Gm_k → min];
- unions T[Gp_k ∪ Gp_l → maj].

T[Gp_1 → maj] dominates X*, Y_12, every majority fill on an M_1 cell, and minority fills on M_2 and M_3 cells. T defends against it at world 1 by guidance, and T itself dominates Λ_T.

**5.4 Partial sources: the choice that matters** (`exp_partial*.out`, `exp_tight*.out`, `exp_corner.out`).

(S) also needs a defence by T, and a dominator, for every T[D′ → C] with C ∈ P. The table counts partial sources against which T has **no** clean defence at any world, given the solution found:

| Solution | Undefended / tested | Source of the certificates |
|---|---|---|
| J1 nearT (single-cell tightenings) | 0 / 152 | — |
| J1 precise; rand1; rand2 | 39 / 2,329; 1 / 364; 19 / 1,485 | two-link at every world, 2 requests each |
| twin nearT, full catalogue | 16 / 862 | all from non-tightenings; tightenings 0 / 12 |
| twin nearT, tightenings only | 3 / 996 | one precise-like tightening shared by min[Gm1a] and maj[Gp1a] |
| J1 tightenings only, nearT; rounds 0–2, partial sources fed back | 0 / 135, 0 / 1,046, 0 / 6,417 | all rounds clean; \|P\| = 11 → 23 → 92 |
| corner model, finite catalogue of 60 credal sets K ⊆ M, nearT | round 0: 0 / 153; round 1: 0 / 542 | defenders: the three corner cuts at t = c + ε/2 |
| corner model, rand1 | 1 / 596 | one corner+edge cut serving maj[Gp1+R2] and maj[Gp1+R3] |

Every certificate has the same form: **one defender serves fills that harm different worlds, and Lemma P kills its partial source at each world through a different fill** (Prop S with C = C″). For example, in the corner rand1 run:

```
T R_1 Y:  dom(corner1+edge2, maj[Gp1+R2]) + cmp T R_1 Y  ->  composite {R2:S>P}: F1
T R_2 Y:  dom(corner1+edge2, maj[Gp1+R3]) + cmp T R_2 Y  ->  composite {R3:S>P}: F1
```

Feeding the J1-rand1 partial sources back as rivals exhausted an 8,000-node budget, with 7,898 dead ends. In the corner model with nearT, round 2 (822 rivals) left the greedy search stuck at a **dominator** obligation for a partial source of a corner cut. Every candidate failed by cross-exposure (F2) against another corner cut. Greedy is not complete, so this is not a proof of infeasibility.

---

## 6. Refinement (`exp_split_*.out`; PROVED + CHECKED)

- **Twin split** (43 cells). By Lemma 2.2, every failure above persists verbatim, and so does every clean closure of lifted requests. The enlarged class has 148 rivals: the lifted named four, fills of all whole and half silent cells, and Y_H on half cells. It closes cleanly:
  - from scratch: \|P\| = 16, 29, 19;
  - by extending the lifted J1-nearT solution (225 fixed requests): \|P\| = 21, 30, 22.
- **Perturbed split** (31 cells, 106 rivals): clean under all three orders, \|P\| = 9, 27, 14.
- **What refinement changes is the rival class.** The new failures in the twin and corner models (§5.4) come from partial sources and half-cell fills, never from re-running old requests.

---

## 7. Continuum implications the finite models omit

1. **Finer (IB) copies inside a cell.** Twin splitting adds one level only. The partial sources T[D′ → C] for all non-conic D′, and fills on arbitrary subsets of a tightening's answer region, are sampled at most to depth one.
2. **Non-conic sets (Lemma H).** Cells see only conic sets. F2 decisions about splices rely on the cell test. In the continuum, any all-world tie with a non-conic splice is F2; the strict variant (§5.1) imposes this everywhere and still closes.
3. **Hidden regions.** The 25-cell axis model sees only the majority part of a corner cut's answers. The corner model adds one cell per hidden region, but not their continuum shape. W and J cells were never split, so loosenings such as T[W_23 → S] have no partial sources on cells.
4. **Closed sections.** Not modelled. The implication "p ∈ cl{q : C_q R_i X} ⇒ C_p R_i X" is not finitary.
5. **KKM for every model.** At most 2,391 rivals were imposed in one run; (S) needs a defence and a dominator for all models. §5.4 shows that the partial sources of the chosen defenders are the first place this bites.
6. **Other selected models, uniformity, infinite chains.** Only T's competitiveness is imposed. PP19's collars are invisible. Closures on cells are finite, while continuum rule-II chains may not stabilise in ω steps once sections are added.

None of §§3–6 is evidence about (S).

---

## 8. What this suggests for the measurable theorem

1. **Prove an inert extension.** Every clean joint solution with weak defences was inert. Every failure was a two-link kill, an exposure (against T or against another protected model), or a short chain through completed tie triangles. So state the construction as a list of requests and verify (a)–(c) of Lemma 2.3 pointwise. No closure computation is needed.
2. **Use corner tightenings as defenders, assigned by harmed world.** For a rival that harms world k, use a k-corner tightening K ⊆ M with v_i, v_j ∈ K. By Lemma Q:
   - T defends against the defender, and against all its partial sources, **by guidance at k**, so these T-defences install no records;
   - by Lemma 0.2, a k-tightening must never dominate a rival with X ≺_k T.

   The clean solutions follow this pattern:
   - majority fills on M_k get k-tightenings;
   - minority fills on M_k get i- or j-tightenings;
   - X* and Y_12 get a 1- or 2-tightening;
   - Λ_T is dominated by T itself;
   - V_{c*} is registered; in the strict variant, where registration is barred, T defends against it at all three worlds.
3. **CONJECTURE.** For majority and minority fills of T's silence on arbitrary measurable sets, together with X*, Y_12, Λ_T and V_{c*}, there is an assignment of corner tightenings satisfying Lemma 2.3. The installed records would then be only the dom records and T's defences against the mixed rivals (X*, Y_12, Λ_T, V_{c*} and mixed fills).
4. **What remains to prove**, each item stated measurably:
   - (i) *Exposure.* The tightening must not give the majority answer on a.e. point of the fill. This is the hard case for fills accumulating at T's boundary near the corner direction: one must choose t, or a different K containing v_i and v_j, accordingly.
   - (ii) *Prop S / two-link.* There must be no two-link kill between dom records and T's installed defences of the mixed rivals. This is the only place where installed T-records meet defenders.
   - (iii) *Exposure across P (Lemma 0.4).* No tightening may equal a dominated rival on another tightening's disagreement set.
   - (iv) *Dominators for partial sources of tightenings.* Their T-defence is automatic (Lemma Q), but they still need dominators. This is where the finite corner search got stuck (§5.4).
5. **Avoid** defenders with large support shared across worlds (Lemma P), and loosenings or edge cuts that do not contain two vertices of M. Single-world ties are also to be avoided: they never rescued a choice, and they caused the only longer derivations. The choice of T's world against the named rivals is free on cells (72/72).
