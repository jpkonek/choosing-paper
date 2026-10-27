# PP1. The weak gate in three worlds: construction side

20 October 2026, Brief 36. Labels:
- **PROVED**: the full argument is given here (one reader, me; not refereed).
- **CHECKED**: a standard fact, or a step read line by line.
- **CONJECTURE**.
- **NUMERICS**: exact-rational scripts in `PP1_py/`. Nothing rests on them.

I add no assumptions to the programme. Where a hypothesis belongs to one result only (a key family, a verdict class), it is stated in that result.

---

## 0. Verdicts

1. **A shared problem order fails (PROVED; the lead's sketch made precise).** Suppose all three worlds key the regular steps of mixed problems by one common order of problems.
   - Then no regular model outside the image of the selection has a KKM dominator, whatever the verdicts.
   - So (S) with closed sections is impossible.
   - In the continuum, competitiveness also fails at every index where the shared order does not separate the two decided zones of one class, through a tie at the infimum.
   - NUMERICS: on atoms there are no ties, and there competitiveness and undominatedness hold, yet every non-selected regular rival (e.g. 2147 of 2147) has no dominator among the selected cell models.
2. **Mass-sensitive verdicts fail whatever the keys (PROVED).** This class includes the sticky 2·on − off, audit's coordinated variants and every additive-type verdict.
   - At an interior index, competitiveness forces world i to separate, on full reversals of odd-i problems, exactly as a *strong* gate would. Odd-i problems are those whose line puts e_i alone on one side.
   - Two interior credal sets that are *crossed* (each lies on e_i's side of some odd-i line that has the other beyond it) make this impossible.
   - Exact crossed pairs exist for the homothetic-triangle family and for the hexagon family (§3).
   - So, for families with small credal sets, the weak gate does **not** rescue the sticky verdict. On these records any surviving verdict must ignore masses, i.e. be lexicographic.
3. **Sup-present keys are the three-world analogue of the two-world keys (PROVED).** Define k_w(s) := sup{p_w : step s ∈ U_w(C_p)}.
   - Then C_p ⪯_w X passes the gate whenever p_w > ψ_w(X), where ψ_w(X) is the lowest key of a world-w step of X.
   - Hence (S)-competitiveness and KKM dominators hold for every rival with ψ_1 + ψ_2 + ψ_3 < 1.
   - For the hexagon family this covers every precise rival D_r.
   - The two-world keys l⁻¹(t), u⁻¹(t) are exactly these keys.
   - NUMERICS: the construction still fails, near the target as well, against rivals that only change *silent* advice on tilted lines (explicit instance in §4).
   - Median-ray keys fail far more often (non-competitive pairs: 36 of 40, 58 of 69, 35 of 39, 37 of 44 on four layouts).
4. **No fixed keys at all, even with the most permissive verdict (NUMERICS; CONJECTURE for the continuum).** The test uses finite cell models with exact enumeration of the selected cells and of the models at boundary indices, a SAT search over all three key orders, and an independent z3 recheck. The verdict is gate-only (Φ ≡ +).
   - Competitiveness alone is satisfiable in every instance run (24 of 24).
   - Dominator existence alone is satisfiable in 22 of 24 instances.
   - **Both together are unsatisfiable** in 6 of 10 six-line layouts, in 5 of 6 seven-line layouts (triangles), in 6 of 6 seven-line layouts (hexagons) and in 3 of 3 eight-line layouts (triangles).
5. **Undominatedness is automatic (PROVED)**: it follows from competitiveness by antisymmetry, for any verdict. **(TC) is automatic (CHECKED)**: no cycles in 8 exact runs.
6. **Closedness.** The failures in 1 and 4 are failures of the meeting point that closed sections force. What would be needed is in §6.

**Net (CONJECTURE).** For continuous selections through an interior imprecise target, no weak gate with fixed per-world keys gives (S) with closed sections in three worlds, whatever the verdict.
- The obstruction is not (TC). It is that competitiveness needs one world per rival, while the KKM dominator needs all three worlds per rival.
- What *is* reachable is item 3: the reduction to rivals with ψ₁ + ψ₂ + ψ₃ ≥ 1, i.e. local rivals near selected models. §7 says where the remaining freedom lies.

---

## 1. Set-up, and three reductions

**Setting.** As in the brief and the gate note.
- Problems g ∈ R³ modulo sign. A mixed problem is a line L_g through the open simplex.
- It is **odd-i** if it puts e_i alone on one side. Orient it so that accepting g is right at world i and wrong at the other two.
- C_p = D_{K_p}. Rank steps (g, j), j = 1, 2, 3, present at world w iff r_w(g, X) ≥ j.
- **Weak gate.** C ⪯_w X iff
  - X = C, or
  - T^off_w := U_w(C) ∖ U_w(X) is null, or
  - T^on_w := U_w(X) ∖ U_w(C) is non-null, ess inf_{T^on} k_w < ess inf_{T^off} k_w, and Φ_w(C, X) ≥ 0.
- Contradiction steps and unanimous-problem steps have the lowest keys.
- A **regular** rival has no contradictory advice and is correct on unanimous problems.

**R1 (only regular rivals matter for the gate). CHECKED.** Out of a coherent C, contradiction and unanimous errors add steps with the lowest keys at every world, and C never has such steps. So a rival containing them passes the gate at all three worlds, and only Φ decides. For the sticky verdict at interior indices, Σ_i off_i ≤ 2 Σ_i on_i (note, audit section) gives competitiveness against such rivals.

**R2 (the gate-only verdict is the most permissive).** Φ can only remove gated acceptances. So if competitiveness or dominator existence fails with Φ ≡ +, it fails for every Φ.
- With Φ ≡ +, world w out of C is a lexicographic test: C ⪯_w X iff the lowest-key difference at world w is a step that X *adds*, or X is a pure world-w worsening.

**Lemma U (competitiveness implies undominatedness). PROVED.** Suppose C is competitive on a non-empty support and X ≠ C. Some w has C ⪯_w X. Each weakly gated world is antisymmetric (the note's no-cycle lemma, which uses only ess inf_{T^on} < ess inf_{T^off}), so X ⋠_w C, and X does not weakly dominate C.

**KKM. CHECKED.** Suppose the sections A_w(X) = {p : C_p ⪯_w X} are closed and competitiveness holds on supp p. Then each face conv{e_i : i ∈ S} is covered by ⋃_{i∈S} A_i(X), and the KKM lemma gives q ∈ A_1(X) ∩ A_2(X) ∩ A_3(X).
- So every X needs a **dominator**: a q with C_q ⪯_w X at all three worlds.
- Under the weak gate with Φ ≡ +, this says that at every world the lowest-key difference between C_q and X is a step X adds.

---

## 2. A shared problem order

**Proposition 1. PROVED.**
- *Hypothesis.* There is a measurable κ on mixed problems with null level sets and, for each w, a continuous strictly increasing h_w, such that k_w(g, 1) = k_w(g, 2) = h_w(κ(g)) for every mixed g.
- *Claim.* For every coherent C and every regular X ≠ C, there is a world w with C ⋠_w X, whatever the verdicts.
- *Consequence.* No regular model outside the image of the selection has a dominator. So competitiveness on supp p and closed sections cannot both hold, by KKM. Regular models outside the image exist, e.g. incoherent ones.

*Proof.*
1. Let Δ be the set where X and C differ. It is non-null and consists of mixed problems: on unanimous problems both models are correct.
2. On Δ both advices are regular, since C is coherent.
3. A change has a **type**: the sign pattern of g, the advice of C and the advice of X. There are finitely many types.
4. Let κ* := ess inf_Δ κ. Every band Δ ∩ {κ < κ* + ε} is non-null. By pigeonhole, some type τ meets every such band in a non-null set.
5. A regular change moves the world-w rank by s_w·d, where s_w = sign(g_w) and d ≠ 0. Since g is mixed, s_{w₀}·d < 0 for some w₀, so τ removes steps at world w₀.
6. Hence T^off_{w₀} is non-null and ess inf_{T^off} k_{w₀} ≤ h_{w₀}(κ*).
7. T^on_{w₀} lies over Δ, so its essential infimum is at least h_{w₀}(κ*).
8. So the strict inequality fails, the pair is not a guidance pair, and X ≠ C. Hence C ⋠_{w₀} X. ∎

*What it says about keys.* At the bottom of every difference set, the three worlds must disagree about which problem comes first. A common order puts one regular change there, and that change is a gain at some world.

**Remark (competitiveness also fails in the continuum, where the zones overlap). PROVED.**
- *Hypothesis.* At an interior index p and for some class, say odd-3, the essential κ-ranges of C_p's two decided zones overlap in an interval. The zones are where C_p accepts g and where it accepts −g.
- *The rival.* Pick c inside the overlap, and let X change C_p to silence on both zones intersected with {c < κ < c + ε}.
  - On the zone where C_p accepts −g, the change removes at worlds 1 and 2 and adds at world 3.
  - On the zone where C_p accepts g, it removes at world 3 and adds at worlds 1 and 2.
- *Conclusion.* At every world, additions and removals have the same essential infimum h_w(c). So the strict gate fails at all three worlds, and C_p is not competitive.
- *Scope.* I have not shown that some interior index always has overlapping zones. If none does, κ separates the two decided zones at every interior index, in an orientation that may depend on p. This is weaker than the fixed-orientation threshold of §3, so §3 does not exclude it.
- On atoms keys are distinct and this tie never occurs, which is why the finite check below shows competitiveness holding.

**NUMERICS (`run_common.py`; exact cells; 7 lines; gate-only).**

| family, layout | selected | non-selected regular rivals | competitiveness failures | dominated selected | rivals without a cell dominator |
|---|---|---|---|---|---|
| triangles, seed 0 | 40 | 2147 | 0 | 0 | 2147 |
| triangles, seed 1 | 69 | 2118 | 0 | 0 | 2118 |
| hexagons, seed 0 | 41 | 2146 | 0 | 0 | 2146 |
| hexagons, seed 1 | 68 | 2119 | 0 | 0 | 2119 |

On atoms, some split models at boundary indices (§5) do dominate. For the triangles, 960 of 2147 rivals (seed 0) still have no cell-or-split dominator; for the hexagons, all 2146 have none. In the continuum, split models are coherent models C_q, so Proposition 1 covers them.

---

## 3. Mass-sensitive verdicts: the weak gate becomes a strong gate

**Records.** Fix world i and an interior index p. Put
- A_p^i := odd-i problems where C_p accepts g (right at i, wrong at the other two worlds);
- B_p^i := odd-i problems where C_p accepts −g.

A **full reversal** on R ⊆ A_p^i and Q ⊆ B_p^i flips the advice on R ∪ Q.
- World i loses both steps on R and gains both on Q.
- The other two worlds j, k gain on R and lose on Q.

**Definition (mass-sensitive).** There is λ ≥ 1 such that every full reversal with μ(R) > λ μ(Q) has Φ_j(C_p, X) < 0 and Φ_k(C_p, X) < 0. In words: a world rejects a record whose gain outweighs its loss by the factor λ.
- Sticky 2·on − off: λ = 2, since Φ_j = 4μ(Q) − 2μ(R).
- Additive on − off: λ = 1.
- Any three-world transcription of audit's coordinated variants with weights α ∈ [½, 2]: λ = 4.
- Any verdict ∫_on a dν − ∫_off b dν with a ≤ A and b ≥ β > 0: λ = A/β.

**Proposition 2. PROVED.** Assume the weak gate with **any** keys (null level sets) and a mass-sensitive verdict. Let κ_i := min(k_i(·, 1), k_i(·, 2)) on odd-i problems.
- **(a)** If C_p (p interior) is competitive, then ess sup_{A_p^i} κ_i ≤ ess inf_{B_p^i} κ_i for every i: the odd-i reversal threshold.
- **(b)** Call p and q **crossed at world i** if both A_p^i ∩ B_q^i and A_q^i ∩ B_p^i are non-null; that is, each credal set lies on e_i's side of an odd-i line that has the other strictly beyond. Then C_p or C_q is not competitive.

*Proof.*
- (a) Suppose some c has A_p^i ∩ {κ_i > c} and B_p^i ∩ {κ_i < c} both non-null.
  1. Take R as the first set, and Q ⊆ the second with μ(Q) < μ(R)/λ (μ is atomless).
  2. Worlds j and k then have Φ < 0.
  3. At world i, T^on = R × {1, 2} and T^off = Q × {1, 2}. So ess inf_on k_i ≥ c > ess inf_off k_i: the gate fails.
  4. T^off is non-null, so this is not a guidance pair. So C_p loses at all three worlds.
- (b) Write a ≤ b for the cut of p from (a), and a′ ≤ b′ for q.
  1. On A_p ∩ B_q, κ ≤ a and κ ≥ b′; on A_q ∩ B_p, κ ≤ a′ and κ ≥ b.
  2. So a ≤ b ≤ a′ ≤ b′ ≤ a, all four are equal, and κ is constant on a non-null set.
  3. That contradicts null level sets. ∎

**Exact crossed pairs (CHECKED with exact arithmetic; `crossing2.py`).**
- **Homothetic triangles.** K_p = p + 3 min(p)·T, with T = (3/20)(e_k − c).
  - Indices p = (1/3, 29/60, 11/60) and q = (1/3, 11/60, 29/60).
  - The odd-1 line through (5/24, 19/24, 0) and (13/30, 0, 17/30) has K_p on e₁'s side and K_q beyond.
  - The odd-1 line through (67/120, 53/120, 0) and (1/120, 0, 119/120) has the reverse.
  - The pair (3/5, 3/10, 1/10), (3/5, 1/10, 3/10) is also crossed.
- **Hexagons.** K_p = {x : |x_i − p_i| ≤ p_i/4}: imprecise everywhere except the vertices, and a hexagon at the centre.
  - The pair (3/5, 3/10, 1/10), (3/5, 1/10, 3/10) is crossed, through the lines (13/60, 47/60, 0)–(91/120, 0, 29/120) and (19/24, 5/24, 0)–(7/120, 0, 113/120).
  - In both cases the open sets of nearby lines have positive Gaussian measure.

**Geometry (sketch).** Take two disjoint small credal sets and a point m between them. The three directions from m to the vertices cut the line directions into three arcs, and lines through m with direction in the arc facing e_i are odd-i. If the direction from one set to the other lies inside the arc facing e_i, the two sets are crossed at world i. The arcs cover all directions, so *generic* pairs of disjoint small sets are crossed at some world.

What survives Proposition 2:
- verdicts that are lexicographic on full reversals, i.e. ignore masses there; or
- families whose interior credal sets are pairwise crossed at no world, e.g. sets that pairwise intersect. Near the vertices and edges such families are hard to arrange, because edge models must be edge-contained (§6). This is not settled here.

**NUMERICS (`run_exact.py … comp sticky`; exact cells; 7 lines).** Sticky competitiveness alone is unsatisfiable for **every** key order in 3 of 6 triangle layouts and in 3 of 6 hexagon layouts. The minimal certificate from an earlier grid run (`core_sticky.py`) uses rivals on odd-2 lines near e₂: the same mechanism.

---

## 4. Sup-present keys: what carries the two-world construction, and where it stops

**Definition.** k_w(s) := sup{p_w : s ∈ U_w(C_p)}, the largest e_w-coordinate of a selected model that still has step s.
- In two worlds this is the gate note's key: sup{p : t ≥ l(p)} = l⁻¹(t) and sup{p : t > u(p)} = u⁻¹(t). At world 2, with index 1 − p, it gives 1 − u⁻¹ and 1 − l⁻¹.
- For the families here these keys are ≥ 0, so they sit above the contradiction and unanimous keys.

**Lemma 3. PROVED (any family).** Write ψ_w(X) := ess inf of k_w over U_w(X). If p_w > ψ_w(X), then the pair (C_p, X) passes the weak gate at world w, so C_p ⪯_w X under Φ ≡ +.

*Proof.*
1. Every step of C_p has key ≥ p_w, by definition.
2. The set U_w(X) ∩ {k_w < p_w} is non-null, misses U_w(C_p), and so lies in T^on. Its essential infimum is < p_w.
3. T^off ⊆ U_w(C_p) ⊆ {k_w ≥ p_w}. ∎

**Corollary 3′. PROVED.** Suppose ψ₁(X) + ψ₂(X) + ψ₃(X) < 1.
- Every C_p is competitive against X: on any face, Σ_{w∈supp p} p_w = 1 > Σ_{w∈supp p} ψ_w(X).
- X has a dominator: any q with q_w > ψ_w(X) for all w.

For the hexagon family, every precise rival D_r with r interior qualifies.
1. D_r has both world-w steps on the level line {x_w = c} for every c > r_w, and on the lines near it.
2. The step-2 key of that line is sup{p_w : max_{K_p} x_w < c} = φ(c). Here max_{K_p} x_w = p_w + ¼·min(p_w, 1 − p_w), and φ is the inverse of that increasing map. The key is continuous in the line, so lines near the level line have keys near φ(c).
3. So ψ_w(D_r) ≤ φ(r_w) < r_w, and Σ_w ψ_w(D_r) < 1.

For the triangle family the bound is only ≤ r_w, because that family is precise on the boundary. Imprecision supplies the slack.

**Where it stops (NUMERICS; `sup_failures.py`, `sup_central.py`, `sup_example.py`).**
- Rivals with Σψ ≥ 1 are local rivals near selected models, and they are not covered.
- There are such failures in 3 of 4 random layouts; the minimum of Σψ over the failures is 1.11 to 1.26.
- With lines concentrated near the target, there are 23 to 56 non-competitive (model, support) pairs in each of 5 layouts, and most have indices within 0.15 of the centre.

Explicit instance (triangles):
- **Index and base.** p ≈ (0.394, 0.288, 0.318). C_p is silent on four lines (two odd-3, one odd-2, one odd-1).
- **Rival.** X decides all four silent lines.

| world | X adds (lowest key) | X removes (lowest key) | p_w | gate |
|---|---|---|---|---|
| 1 | 0.655 | 0.451 | 0.394 | fails |
| 2 | 0.549 | 0.414 | 0.288 | fails |
| 3 | 0.380 | 0.339 | 0.318 | fails |

- **What it says about the keys.** A step that C_p lacks inherits a high key from a distant model that has it. The line is tilted, so models far along it reach larger p_w.
- In three worlds the index p_w does not order tilted lines, so the threshold property of the two-world Lemma 1 fails, in both directions at once.
- Band keys repair the silent band: sup and inf of p_w over models whose credal set meets the line. Every silent-only rival is then defeated. But they are bad on decided zones (28 to 66 non-competitive pairs per layout; `band_keys.py`).

---

## 5. All key orders at once (NUMERICS)

**Finite model.** N mixed lines, each blown up into a small neighbourhood with positive mass. Keys are continuous, hence constant on each neighbourhood up to small variation. Rivals are regular and constant on neighbourhoods, with 3^N of them.

**Selected models.** Enumerated exactly (`arrangement.py`):
- the switching curves of both families are piecewise linear in p;
- the full line arrangement in the index simplex is built exactly, and every face is sampled;
- this was checked against a 200-grid, which misses tiny cells (65 cells found by the grid against 69 by enumeration).

**Candidate dominators.**
- The selected cell models.
- The **split models** at boundary indices. At an index on a switching curve, the neighbourhood of that line is split between the advices of the adjacent cells. Every advice differing from the rival contributes its changed steps, and distinct steps have distinct keys, so the order inside a neighbourhood is fixed. Splits are taken at every arrangement vertex and edge; a superset is harmless for unsatisfiability.

**Solver.**
- The unknowns are the three key orders, one total order per world on the 2N regular steps.
- `satsplit.py` encodes, with Φ ≡ +:
  - competitiveness of every selected cell model on each of its supports against every regular rival;
  - and/or a dominator for every non-selected regular rival.
- Solver: CaDiCaL. Certificates are minimised by deletion and re-checked with an independent z3 encoding using integer keys (`z3_exact_cert.py`).

| lines, family | layouts | competitiveness only | dominators only | both |
|---|---|---|---|---|
| 5, triangles | 2 | SAT 2/2 | SAT 2/2 | SAT 2/2 |
| 6, triangles | 10 | SAT 10/10 | SAT 10/10 | **UNSAT 6/10** |
| 7, triangles | 6 | SAT 6/6 | SAT 5/6 | **UNSAT 5/6** |
| 7, hexagons | 6 | SAT 6/6 | SAT 5/6 | **UNSAT 6/6** |
| 8, triangles | 3 | not run | not run | **UNSAT 3/3** |

**Minimal certificates (z3: unsat).**
- 6 lines, triangles, seed 3: 5 rivals with 13 competitiveness constraints.
- 7 lines, seed 0: 4 rivals with 14 constraints. Files: `cert_hom_N6_s3.pkl`, `cert_hom_N7_s0.pkl`.
- They involve edge models (two active worlds) and interior models near the edges.

**The mechanism (not extracted).** I have not reduced the exact certificates to a hand-readable argument. On inspection they sit on edge models (two active worlds) and on interior models near the edges.
- The recurring local pattern is a pair of lines crossing an edge close together.
- The edge model must beat the local rival "silence both" at one of its two active worlds. That fixes, at that world, which of the two lines comes first.
- Nearby rivals with the opposite local pattern need dominators with the reverse order at all three worlds.

This reading came from a smaller grid-based certificate. With exact enumeration that certificate is void: one of its rivals is a tiny selected cell that the grid missed. So the reading is a guide only.

**Status.** NUMERICS, with the caveats:
- the finite model is not the Gaussian setting;
- keys are assumed continuous;
- no transfer theorem is claimed.

The trend is unsatisfiable more often as lines are added: 0/2 at 5 lines, 6/10 at 6, 11/12 at 7, 3/3 at 8. Earlier grid-based runs were discarded: an independent rerun on a finer grid found that a 60-grid had missed a cell, and the cell enumeration is exact.

---

## 6. (TC), closedness, and edges

- **(TC). CHECKED** (`tc_check.py`).
  - Full four-advice domain with one unanimous problem.
  - Random keys, with contradiction and unanimous steps lowest.
  - Gate-only and sticky verdicts.
  - A topological sort of each world's whole accepted relation finds no cycle in 8 of 8 runs, as the no-cycle lemma predicts.
- **Closedness.**
  - Closedness can fail as follows. Take p_n → p. For C_{p_n} the lowest-key difference with X can be an addition lying in the thin set where C_{p_n} differs from C_p, near a boundary problem of C_p. In the limit that set vanishes, and the first difference of (C_p, X) can be a removal.
  - So at every boundary problem of every selected model, the keys must not undercut the comparisons with rivals.
  - The split models of §5 are exactly this requirement made finite. Proposition 1 is its clean continuum form.
  - On atoms closedness itself is untestable, as the brief says; the dominator test is its testable consequence.
- **Edges. PROVED.** A selected model at an index on edge e_ie_j must have its credal set inside that edge.
  - Otherwise there is an open set of odd-k problems, near the edge, on which the advice is not (i, j)-correct.
  - Fixing it is a pure improvement at both active worlds, which strict (G) forbids.
  - Edge models therefore carry a two-world structure, and §5 shows it colliding with three-world dominators.

---

## 7. What the keys would need, and what is reachable

**Necessary conditions found here.** These hold for continuous fixed keys; items (iii) and (iv) are local, first order, and sketched only.
1. At the bottom of every difference set, the worlds' orders must disagree (Proposition 1).
2. With a mass-sensitive verdict, a strong-gate threshold is needed on odd-i reversals at every interior index (Proposition 2). It is impossible for crossed pairs.
3. **(sketch)** At a boundary point of an imprecise C_p, the gradients of the relevant step keys must have no common ascent direction straddling the boundary. Otherwise a tie rival defeats the gate at all three worlds.
4. **(sketch)** At a precise interior C_p, the three keys restricted to the pencil of lines through p must share a minimiser.

**Reachable (PROVED).** Sup-present keys handle every rival with Σψ < 1 (Corollary 3′), including all precise rivals for the hexagon family, with (TC), strict (G) and (IB) untouched.
- The residual class is precise: rivals that, at every world w, add no step whose top index is below ψ_w.
- These are local modifications at crossings, i.e. tilted lines.
- That is where a three-world mechanism must do new work.

**Suggested next step.** The surviving freedom is outside fixed per-world keys: key orders chosen from the disagreement itself (gate note, Next steps (a)), with (TC) checked directly.
- The finite framework here (exact cells, boundary splits, SAT over the rule's free choices) can screen such rules before any proving round.
- Any verdict used with them must be lexicographic on odd-i full reversals for small-set families (Proposition 2).

---

## Scripts (`PP1_py/`)

| purpose | files |
|---|---|
| core finite model | `core.py`, `evalkeys.py`, `satrelax.py` (grid helpers) |
| shared order | `run_common.py` |
| crossed pairs | `crossing.py`, `crossing2.py` |
| sup-present keys | `supkeys.py`, `sup_failures.py`, `sup_central.py`, `sup_example.py`, `run_sup_mult.py`; band keys `band_keys.py`; ray keys `ray_keys.py`; older keys `keyfams.py`, `run_structured2.py` |
| exact cells and SAT | `arrangement.py`, `check_arrangement.py`, `satsplit.py`, `run_exact.py` (outputs `exact7.out`, `exact6_hom.out`, `exact6_comp.out`, `exact_more.out`) |
| certificates | `core_exact.py`, `core_exact_kkm.py`, `z3_exact_cert.py`, `cert_*.pkl` / `.txt` |
| (TC) check | `tc_check.py` |
| earlier grid runs (superseded; their unsatisfiable verdicts on sticky competitiveness are valid, since a grid gives a subset of constraints) | `harness.py`, `run_componly.py`, `core_sticky.py` |

Run with `python3 -I <script>` inside `PP1_py/`.
