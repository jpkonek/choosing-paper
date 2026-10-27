# X3 — finite joint search over world-labelled transition records

16 October 2026. Note X3 for BRIEF18. Scripts are in `x3py/`, with logs in `x3py/out/`. The earlier draft scripts of this note were moved, untouched, to `x3py/old/`.

Labels:
- **PROVED**: a proof is given here.
- **CHECKED**: a computer-verified finite statement, with the check named.
- **NUMERICS**: computational evidence only.

Nothing finite below proves anything about the continuum problem. Section 2 makes this precise: (S) has no faithful finite form.

## 0. Outcome

1. **Every finite instance tested is satisfiable once the requirements are stated soundly, and it has an additive solution.** The search covered 24 and 42 cells, grids m = 3 and 6, ε ∈ {0.1, 0.3, 0.6}, and the closed-section proxies "none", ring-vx, ring-bd and ring. In each case the joint three-world SAT search succeeds, and so does the restriction to additive world orders (z3, on the same family F).
   - For three instances (m = 3, 24 cells, ε ∈ {0.1, 0.3, 0.6}; (G), (IB), (T), grid (K), (P), (C)), the additive solution was checked against **all 3^24 models**, not only against F. The check is exact, with z3 over the rationals (CHECKED).
   - So in this finite model non-additivity is **never needed**. The question "are there non-additive solutions where additive ones fail?" has no instance at the resolutions reached.
2. **Every UNSAT core found is local and is explained by a short proof.** None of them bears on T1:
   - the edge-selection core → Lemma X3.2;
   - the "thick/simplicial" proxy core → Lemma X3.3;
   - the literal neighbour-propagation proxy → Lemma X3.4;
   - the finite KKM shadow (W) → certificate C3, an artefact of having no finest scale.
3. **PROVED, general: a closed competitive selection meets uncountably many all-world tie classes.** This is Theorem X3.1, via Sierpiński's theorem. Hence no finite (or countable) discretisation can satisfy (S), and every grid proxy for closed sections is a heuristic, not a consequence of the axioms.
4. **A repeatable rule for the extension lemma: composition modulo worsening glue.**
   - Transitivity restricted to triples inside F let the solver return several systems with a world that does not add up. Each had an (M1)-type certificate (Farkas support) of 2–9 accepted records.
   - Each of the certificates tested **composes, modulo worsening glue, into a pure improvement**, sometimes only after 8–11 compositions (CHECKED, `certcheck.py`, `closure_check.py`). So none of those systems is a genuine non-additive world: each violates (T)+(IB)+(G) in the full finite world.
   - With that closure enforced (CEGAR on Farkas certificates), every solution found in the smaller m = 6 instances was additively endorsable at every world (NUMERICS).
   - One exception remains undecided. In the largest instance (m = 6, rt1 = 2, ring), 154 compositional certificates were cut. The final solution's world 1 still has a 10-record certificate, and it survived a closure search of depth 11 (4.8·10^5 composites) without a contradiction. It is neither shown compositional nor shown closed. On the same F an additive solution exists anyway.
   - The derived rule (r then s is accepted whenever, at every cell, the junction advice only gets worse) is the operational closure that X1/X2 should use when testing extension lemmas, rather than exact middle matching.

## 1. The finite model

### Cells
One cell is one binary problem (one ± pair), represented by an oriented mixed gamble g_c. In `cells.make_cells`:

- **Facet cells.** On each facet F_k of D_{T1}, take the chord h(τ) between its corner rays.
  - Take ntau sample points in each of the three crossing intervals. In those intervals the two crossing coordinates have the sign patterns (−,+), (+,+) and (+,−).
  - The crossings are at τ = 0.3/0.7 for ε = 0.1, at 0.2333/0.7667 for ε = 0.3, and at 0.1333/0.8667 for ε = 0.6.
  - Each sample gives an inside cell h + δ1, which T1 accepts, and an outside cell h − δ1, on which T1 is silent. Here δ = 0.05.
- **Corner cells.** The three corner rays r_kj ± δ1.
- **Totals.** ntau = 1 gives 24 cells and ntau = 2 gives 42. The construction is symmetric under the cyclic permutation of worlds.

Each cell carries the background order at world i: good < silent < bad. The advice range is {+, 0, −} on every cell, so the domain is the full two-sided one.

**Lemma X3.0 (PROVED).** Contradictory advice and unanimous pairs may be dropped. A cover on the domain "no ×, correct on unanimous pairs, {+,0,−} on mixed pairs" extends to a cover on the full domain, and conversely.

*Proof.*
- **Converse.** Restriction of a cover is a cover. The smaller domain is decomposable and has (LF) at T1, because ∂D_{T1} \ 0 consists of mixed pairs. Selected models lie in it. Competitiveness, closedness, protection and (C) restrict.
- **Extension, definition.** Let π(g, a) be:
  - 1 if a = × on a mixed pair, and 0 otherwise;
  - on unanimous pairs, 0, 1, 2 or 3 for correct, silent, wrong and ×.

  Put Φ(X) = ∫ π(g, a_X(g)) dμ. Let φ(X) be X with × replaced by silence on mixed pairs and with unanimous pairs corrected. Rank X ≤_i Y iff Φ(X) < Φ(Y), or Φ(X) = Φ(Y) and φ(X) ≤_i φ(Y) in the base ranking.
- **(IB).** Φ is additive and world-independent, and φ commutes with splicing.
- **(G).**
  - π is nondecreasing in every world's rank, because × is worst everywhere and the order on unanimous pairs is world-independent.
  - Suppose Φ(X) = Φ(Y) and X is pointwise at least as good. Then π(X) = π(Y) a.e., because π is injective on unanimous pairs and on mixed pairs it only separates ×. So any strict improvement lies on base advice, and the base order is strict there.
- **Remaining axioms.** If Φ(X) > 0, X is strictly worse at every world than every selected model (for which Φ = 0). Its sections are all of Δ, which is closed, and it is not tied with any member of C_L. ∎

### Models, coherence and records
- **Models** are elements of {+, 0, −}^N.
- **Coherence** is tested at the representatives: a pattern is coherent if some D_K gives exactly this advice on the representatives. The largest admissible K = {m ∈ Δ : m·x ≥ δ' for every accepted x} is tested against each rejected orientation by LP.
  - This is weaker than coherence of cell unions, a deliberate abstraction.
- **Records.** A record d(X, Y) gives each cell either the identity symbol or an ordered advice pair, so 7 codes per cell.
- **Variables.** acc_i(r) means X ≤_i Y. Acceptance depends only on the record, so (IB) is built in.
- **Strict (G).** Records with no world-i improvement are fixed TRUE. Records whose only changes are world-i improvements are fixed FALSE.

### Grid and selection
- The grid on Δ has m = 3 (10 points) or m = 6 (28 points).
- Vertex e_j: the world-j-best model B^j, which strict (G) and competitiveness force.
- Target point u = (1/3, 1/3, 1/3): T1.
- Other points: SAT chooses one candidate:
  - `prec`: D_p;
  - `seg`, `segL`, `segR`: D_K with K a segment of the edge of length 1/m or 1/(2m) at p (edge points only);
  - `VB`: D_{co(T1 ∪ {p})}, the veto–Brier selection (interior points only).

### Family F
F consists of:
- the candidates and T1;
- the Hamming balls of radius rsel around the candidates, rt1 around T1, and rvx around the vertex models.

The sizes in the runs below:

| run | |F| | records realised in F |
|---|---|---|
| m = 3 | 1348–1372 | about 1.5·10^6 |
| m = 6, reduced family | 223–238 | — |
| m = 6 with rt1 = 2 | 1336 | — |

### Constraint families
Each family has an activation literal, so that unsatisfiable cores are reported by family.

- **(K)[v]** For every X ∈ F: ⋁_{i ∈ supp v} acc_i(d(C_v, X)), a world-labelled disjunction. The world is not chosen beforehand. At a vertex (K) is automatic.
- **(P)[C]** If C is selected and X ≤_i C at every world, then C ≤_i X at every world. That is, C is not strictly dominated.
- **(C)[C]** An incoherent X ∈ F is never tied with a selected C at every world.
- **(T)** Transitivity, generated lazily:
  - (T_F) on triples X, Y, Z ∈ F;
  - (T_rec) at record level. When a world's accepted trades admit no strictly positive ladder endorsement, the LP's Farkas certificate seeds a closure search by composition modulo worsening glue, with provenance. A derived pure improvement gives the clause "not all of these records". A derived F-record that is currently rejected gives "not all of these, or accept it". Both clauses are sound in the full finite world.
- **(W)** The finite KKM shadow. Every X ∈ F is weakly dominated at all worlds by some protected coherent member of F. This is a strengthening, and artefact-prone (see C3).
- **(CL)** Closed-section proxies. Write s(v, X, i) for "C_v ≤_i X"; it is an exact literal, since exactly one candidate is selected at each grid point.
  - **ring**: for every v, X and i: if s(w, X, i) holds at all grid neighbours w of v, then s(v, X, i). A point surrounded by section points belongs to the section.
  - **ring-bd**: ring at boundary grid points only, which is where veto–Brier fails (L33/L34).
  - **ring-vx**: ring at the three vertices only.
  - **simp** ("thick"): on every face σ of the triangulation, some i ∈ ⋃ supp(σ) has s(v, X, i) at all vertices of σ. Lemma X3.3 shows it is inconsistent.
  - **literal** "rejected at p ⇒ rejected at the grid neighbours": inconsistent by Lemma X3.4.
  - None of these proxies follows from (S), nor (S) from them; Theorem X3.1 explains why.

**Relaxation versus strengthening.** (K), (P), (C), (CL) and (T) are universally quantified over models. Restricting them to X ∈ F is a *relaxation*, so UNSAT on F means UNSAT for the whole finite world. (W) is existential in its dominator, so restricting dominators to F *strengthens* it, and an UNSAT involving (W) may be an artefact.

**Additive restriction** (`addz.py`; `addx.py` is the big-M MILP, superseded).
- World i has penalties 0 < s_i(c) < b_i(c) for silent and bad advice, with increments ≥ 1. The order is complete, X ≤_i Y iff L_i(X) ≤ L_i(Y).
- Rejections and strict comparisons have margin 1. This is no loss of generality: there are finitely many homogeneous constraints, so a solution can be rescaled.
- The same families K, P, C and CL. Disjunctions are solved by z3 over the rationals, with lazily generated instances.
- `add_full.py` adds competitor generation. An exact MILP oracle (`oracle.py`) searches **all** 3^N models for violators of K, P, C or CL and adds them to F, until none remain. `verify_add.py` re-checks the final system exactly with z3 over the rationals, against all 3^N models.

## 2. General statements

**Theorem X3.1 (PROVED).** Take any ranking, with preorders ≤_i on any domain, and a selection p ↦ C_p (p ∈ Δ) with these properties:
- every C_p is undominated;
- every section {p : C_p ≤_i X} is closed.

Write p ≈ q when C_p and C_q are tied at every world. Then:

(a) every ≈-class is closed in Δ;

(b) if C_{e_1} and C_{e_2} are not tied at every world, there are uncountably many ≈-classes.

(c) Part (b)'s hypothesis holds under strict (G) and competitiveness at the vertices whenever the world-1-best and world-2-best models differ on a non-null set; on two-sided domains they always do.

Consequently a ranking whose domain has only countably many models modulo all-world ties has no such selection. This covers every finite discretisation.

*Proof.*
- **(a)** Fix a class S = {q : C_q ~ C} with C = C_{q_0}, and let p ∈ cl S. For each i, the section {q : C_q ≤_i C} is closed and contains S, so C_p ≤_i C at every world. C is undominated, so no inequality is strict. Hence C ≤_i C_p for every i, C_p ~ C, and p ∈ S.
- **(b)** The classes partition Δ, a metric continuum, into pairwise disjoint closed sets, and e_1, e_2 lie in different classes. By Sierpiński's theorem (1918), a continuum is not a countable union of at least two pairwise disjoint nonempty closed sets.
- **(c)** Competitiveness on {j} makes C_{e_j} world-j-optimal. Strict (G) forces any world-j-optimal model to agree a.e. with B^j. If C_{e_1} and C_{e_2} were tied at every world, B^2 would be world-1-optimal, hence equal to B^1 a.e. ∎

*Remarks.*
- (a) says the selection, modulo ties, is a decomposition of Δ into closed sets.
- At most countably many classes have interior. These are the plateaus; veto–Brier's plateau C_p = T1 on T1 is one. Every other class is closed and nowhere dense.
- The complement Z of the union of the plateau interiors is a nonempty closed set. If it were empty, Δ would be a disjoint union of open classes, so there would be only one class, which contradicts (b).
- Together with the "improvable undominated models take countably many values" mechanism of R2 Thm 7 (used in L34), this says that uncountably many tie classes of the selection consist of unimprovable models.
- No independence, target or third world is used.

**Lemma X3.2 (PROVED).** Let p ∈ (e_j, e_k) and let C_p be competitive on {j, k}. On a domain where, for a.e. pair whose orientations satisfy g_j g_k > 0, the advice that is good at both j and k is available (for example a two-sided domain), C_p gives that advice a.e. If C_p = D_K, then K ⊆ [e_j, e_k].

*Proof.* Change C_p to the jk-good advice on the non-null set where it fails. By strict (G) the result is strictly better at both j and k, which contradicts competitiveness. If some m ∈ K had m_l > 0 for the third world l, the open cone of g with g_j, g_k > 0 and m·g < 0 would be non-null and not accepted. ∎

*Comments.* On M_U this fails, as it should: silence is the only alternative there, and veto–Brier's edge selections co(K' ∪ {p} ∪ {v_i, v_j}) are fine on M_U. On the full domain the edge selection is a sub-segment of the edge, so the edge problem is one-dimensional. This is consistent with L36(b)'s precise-edge discussion.

**Lemma X3.3 (PROVED).** Let w ≠ e_j be a point on an edge [e_j, e_k]. Let Q be the set of pairs with g_j g_k < 0 on which C_w ≠ B^j, and suppose Q is non-null. Then the thick condition on the face {e_j, w} fails, for every ranking with strict (G) on a two-sided domain.

*Proof.* Split Q = Q_1 ⊔ Q_2 into non-null pieces. Let X be C_w off Q_1, and j-good (= B^j) on Q_1.
- At world j, X is strictly better than C_w (on Q_1), so C_w ≤_j X fails.
- At world k, X is strictly better than B^j (on Q_2, where X = C_w is not j-good, hence not k-bad), so B^j ≤_k X fails.

Neither i ∈ {j, k} serves both vertices of the face. ∎

The finite core of the `simp` run was a single family, CL at the face {(0,0,3), (1,0,2)}, which is exactly this situation.

**Lemma X3.4 (PROVED, elementary).** The literal proxy "if C_p ≤_i X is rejected at a grid point, it is rejected at its grid neighbours" is inconsistent.

*Proof.* On a connected grid it propagates, so every section is ∅ or the whole grid. Vertex competitiveness puts e_j in every world-j section, so every world-j section is the whole grid. Then every selected model is world-j-optimal for every j, which is impossible when B^1 ≠ B^2. ∎

**Remark X3.5 (trivial, but it matters for design).** At interior grid points (K) is the same constraint for every p, since supp p = {1, 2, 3}. So in any grid model, interior weightings are distinguished only by the closed-section proxy. A plateau of T1 costs nothing finitely. The content of the interior of Δ is entirely in (S).

## 3. Runs (NUMERICS unless marked)

Defaults: 24 cells, δ = 0.05, (G), (IB), (T_F), (K), (P), (C). Edge candidates: m = 3 uses prec, seg, segL and segR; m = 6 uses VB (interior), prec and seg, with rsel = 0, rt1 = 1 and rvx = 1.

| instance | CL | joint SAT (non-additive) | additive z3 on F |
|---|---|---|---|
| ε 0.1, m 3 | none / vx / bd / ring | SAT ×4 (about 145 s each) | SAT ×4 |
| ε 0.3, m 3 | none / vx / bd / ring | SAT ×4 | SAT ×4 |
| ε 0.6, m 3 | none / vx / bd / ring | SAT ×4 | SAT ×4 |
| ε 0.3, m 3, 42 cells | ring | SAT (207 s) | SAT |
| ε 0.3, m 3, rt1 = 2 | ring | — | SAT |
| ε 0.3, m 6 | none / bd / ring | SAT ×3 | SAT ×3 |
| ε 0.1 and 0.6, m 6 | ring | SAT ×2 | — |
| ε 0.3, m 6, rt1 = 2 (|F| = 1336) | ring | SAT (468 s; with closure CEGAR: SAT after 154 cuts, 2289 s; see C4) | SAT (28 s) |
| ε 0.3, m 3, edge candidates VB / co(p, v_i, v_j) | none | **UNSAT**, core (K) at (2,1,0) → C1 | **UNSAT** |
| ε 0.3, m 3 | simp | **UNSAT**, core CL at face {e_3, (1,0,2)} → C2 | — |
| ε 0.3, m 3, + (W) | none | **UNSAT**, core {P, C, W} → C3 | — |

**Additive on the whole finite world (CHECKED).** For ε = 0.3, m = 3, 24 cells, with (K), (P) and (C), `add_full.py` converged after 27 rounds of competitor generation (|F| = 1166). `verify_add.py` then confirmed exactly, with z3 over the rationals and against all 3^24 models, that the following hold for every model:
- (K) at every grid point;
- (P) at every selected model;
- (C): every all-world tie of a selected model is coherent.

The order is additive, so (G), (IB) and (T) hold on all models automatically. The selection, at x3py/out/C_m3_e0.3_none.json:

| grid point | selected model |
|---|---|
| vertices | B^j |
| u | T1 |
| (0,1,2) | `+++++0++++--0000--++--00` (an edge segment, not precise) |
| (0,2,1) | `++++++++00--++++--++--++` |
| (1,2,0) | `--++++--00++++++++--++++` |
| (2,0,1) | `00----+0++++--++++00++--` |
| others | precise |

The same holds for **ε = 0.1** (41 rounds, |F| = 1393) and **ε = 0.6** (47 rounds, |F| = 1485), both with "exact check against all 3^24 models: OK" (out/C_m3_e0.1_none.*, out/C_m3_e0.6_none.*).

Some competitor-generation loops did not converge before the runs were stopped:

| instance | stopped at | violators found |
|---|---|---|
| ring, ε = 0.3, m = 3 | 34 rounds, 2400 s | at edge points: two-world (K) and (P) against new X |
| m = 6, no CL | 7 rounds, z3 slow | same kind |
| 42 cells, m = 3, no CL | 54 rounds, |F| = 3040 | same kind |

These are unresolved, not failures. So "additive on the whole finite world" is CHECKED only for the three m = 3 instances without CL. On F, the additive search is SAT for every instance where the joint search is SAT.

## 4. Certificates (human-readable)

Cells are named F{k}.{interval}{sample}{i|o} and r{kj}{i|o}. Here i means inside D_{T1} and o means outside.

**C1 (edge selections; Lemma X3.2).** At p = (2,1,0), with C = D_{co(T1 ∪ {p})}, C is silent on F1.00i, F1.00o, F2.00i, F2.00o, r12i and r12o (sign pattern (−,−,+)), and on F3.10o (pattern (+,+,−)). Let X be C with those cells set to the advice good at worlds 1 and 2. X is strictly better at worlds 1 and 2 by strict (G). With C = D_{co(p, v_1, v_2)}, the same holds on five cells. One-line proof: Lemma X3.2.

**C2 (thick proxy; Lemma X3.3).** The face {e_3, (1,0,2)}. X is built as in the proof of X3.3 from two cells on which C_{(1,0,2)} ≠ B^3.

**C3 (KKM shadow, an artefact).** With precise edges, m = 3, F = candidates ∪ Hamming-1 balls (|F| = 490) and only (P), (C), (W):
- The instance is UNSAT after 16 CEGAR rounds and 2.5·10^6 transitivity clauses.
- The minimal core is (P), (C) and eight (W)-instances. Each of the eight X is a vertex model with one cell changed. For example, B^3 = `++++--++++--------++----` becomes `++++--++++--0-----++----`; that is, cell F3.00i changes from − to 0.
- No single X is UNSAT alone, so the eight interact through (T) and protection.

Reading: in the continuum, such near-vertex perturbations are weakly dominated by selections C_p with p → e_j, which accept or flip thin cones near the coordinate planes. A finite F has no members fine enough. This is a resolution artefact, not evidence.

**C4 (non-endorsable worlds are compositional, CHECKED).** Without (T_rec), the solver returned systems in which world 1 (and, in one run, world 2) does not add up. The Farkas supports had 2, 3 (with multiplicities 2:1:1) and 7 records. Each composes, modulo worsening glue, into a pure improvement:
- 2 records directly (m = 6, no CL);
- 3 records as the chain r1 → r2 → r3 → r2 (m = 6, ring-bd; r2 is used twice);
- 7 records at closure depth 4 (m = 6, ring, rt1 = 2; `closure_check.py`).

Smallest example (out/A_m6_none.pkl, world 1):
- r1 = F3.00i 0→+, F3.10i 0→+, F3.20i 0→+, r23i 0→+, r31i 0→− (better on 4 cells, worse on 1);
- r2 = a record better on 19 cells and worse on F3.20i only (+→0).
- Chain r1 then r2: at r31i the junction is − then 0. That is a world-1 worsening, accepted by (G), so the chain is legitimate. The composite is better at world 1 on every changed cell.

So F-triple transitivity is materially weaker than (T) in the full finite world.

With (T_rec) enforced (closure search to depth 7, later 16), the following solutions were additively endorsable at all three worlds:
- m = 6 with none, ring and ring-bd;
- m = 6 with ε = 0.1 and ε = 0.6, ring;
- m = 3 with ring (no (T_rec) clause was needed).

The numbers of (T_rec) clauses needed were 7 (none), 3 (ring), 11 (ring-bd), and 0 for the others.

**The undecided case** is m = 6, rt1 = 2, ring.
- The first pass, at depth 7, left certificates of 9 records (world 1) and 8 records (world 2). A deeper search found pure improvements at depth 11 and depth 8, so both were compositional.
- The rerun at depth 16 needed 154 (T_rec) clauses. It ended SAT with worlds 2 and 3 endorsable and world 1 not.
- World 1's Farkas support is 10 records: 8 short trades (2–4 cells) and 2 long ones. Its closure, generated from those 10 records alone, reached 4.8·10^5 composites by depth 11 without a pure improvement or a rejected F-record (out/E2_m6_ring_rt2.pkl; `closure_check.py out/E2_m6_ring_rt2.pkl 1 30`).
- Status: undecided. A contradiction may need records outside the support, or more depth. Either way non-additivity is not *needed* there, because additive z3 is SAT on the same F.

## 5. What this does and does not show, and what X1/X2 can use

- **Not shown.** Nothing about T1 in the continuum. Theorem X3.1 shows that finite models cannot carry (S). At the resolutions reached, the finitely expressible requirements — grid (K), (P), (C), the ring proxies and (T) — are met by additive rankings, in one instance against the whole finite world. So the additive obstruction (Theorem thm:main) and every known non-additive obstruction live in the limit structure: closed sections across scales, plus the absence of a finest scale. This matches the audit's warning. It is now an explicit statement (X3.1), not only a caveat.
- **Repeatable rules worth turning into theorems.**
  1. *Closure rule.* The least A_i containing a set S of trades, all worsenings, and closed under transition-lemma composition is closed under **composition modulo worsening glue**. At each cell, the composite of a chain is "tail of the first arrow → head of the last", provided every junction is a world-i worsening (or an equality). Every (M1) certificate met in these runs was such a chain, after allowing repeats of records.
     - Conjecture-level question for X1 (not supported beyond NUMERICS): on two-sided ladders, is a set closed under this rule and free of pure improvements always strictly endorsable when the certificate support has at most 3 records? Comparative-probability counterexamples (Conder–Slinko) show the answer is no in general for larger supports, so the useful version needs a support bound.
  2. *Tie-class decomposition* (X3.1). The selection modulo ties is a decomposition of Δ into closed sets, uncountably many of them, with at most countably many plateaus. An extension lemma must produce this structure in the limit. It cannot be built by finitely many stages of finitely valued selections.
  3. *Edge selections are edge credal sets on two-sided domains* (X3.2). With X3.1 restricted to an edge, the edge problem is a one-dimensional family of sub-segments K_p ⊆ [e_j, e_k] meeting uncountably many tie classes. This is the natural first test for an extension invariant ("one crossing configuration").
- **Closed-section proxies.** The thick and literal proxies are inconsistent with every ranking (X3.3, X3.4), so they must not be used. The ring proxies are weak: they never produced an UNSAT here.

- **Caveat on endorsable SAT solutions.** If a world's accepted trades are endorsed by a strictly positive ladder density, then their full composition closure contains no pure improvement, so (G) is safe in the full finite world. (P), (C) and (CL) were checked only on F, with F-triple transitivity plus the (T_rec) cuts. For a guaranteed full-finite-world system use the additive solutions (§3), which are transitive on all models by construction.

## 6. Files

**Core**
- `x3py/cells.py`: geometry, cells, point-level coherence, grid.
- `family.py`: candidates and the family.
- `satx.py`: joint SAT engine; CEGAR for (T_F) and (T_rec).
- `run.py`: driver.

**Additive**
- `addz.py`: z3 additive search.
- `addx.py`: MILP version, superseded.
- `add_run.py`: driver.
- `oracle.py` and `add_full.py`: competitor generation over all 3^N models.
- `verify_add.py`: exact check.

**Diagnostics**
- `diag.py`: endorsement LP and Farkas support.
- `certcheck.py` and `closure_check.py`: compositionality.
- `wcert.py`: the C3 core.
- `certifiers.py`: which worlds certify T1.

**Batches and logs**
- `batch*.sh` and `sweep_add.sh`.
- Logs and pickles in `out/`: A_*, B_*, C_*, D_*, E*_*. Their summaries are `batchA.summary` to `batchD.summary` and `batchC2.summary`.
