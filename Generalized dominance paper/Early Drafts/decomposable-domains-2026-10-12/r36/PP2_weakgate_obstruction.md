# PP2: the weak gate in three worlds (obstruction side)

20 October 2026. Answers Brief 36, obstruction side. Scripts are in `PP2_py/`, with outputs in `PP2_py/outputs.txt`. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.

## Summary

1. **Main result (Theorem 6, PROVED).** Fixed key functions fail in three worlds. This holds for any verdicts, any selection and any target.
   - **Hypotheses.** One world (say world 1) accepts every non-guidance comparison only through the weak gate of a fixed key k_1, whose level sets on the level-1 steps of the class M_1 are null. Worlds 2 and 3 satisfy strict (G).
   - **Conclusion.** No selection of coherent models is competitive on supp p at every p and has closed sections.
   - **How the proof works.** It uses only the two edges at e_1. KKM forces two families of world-1 threshold models to be selected: one family is A on M_3, the other is A on M_2. Coherence then makes world 1's level-1 thresholds on M_1 depend only on where a line meets [e1,e2], and also only on where it meets [e1,e3]. So k_1(·,1) is constant on M_1, which the null-level-set hypothesis forbids.
   - **Consequence for the strong gate.** A strong gate implies the weak gate, so this also proves the CONJECTURE after Proposition 9: fixed-order gates fail in three worlds altogether. The question of whether (S) forces a two-dimensional image is not needed.
2. **Shared order (item 1).**
   - The lead's sketch is correct for *problem-lexicographic* shared orders (Theorem 1, PROVED). There, no regular model beats another at all three gates, so KKM fails for every non-selected regular model.
   - With level offsets, the stated mechanism is false. A model dominates every rival that silences it on A-sets in two classes (PROVED; CHECKED, 9747/9747).
   - The conclusion survives for offsets that point the same way at every world, using other rivals (Proposition 2, PROVED). It survives for every offset pattern by Theorem 6.
3. **One index (item 2).**
   - Proposition 3 gives an exact recipe for a regular rival that fails all three weak gates.
   - Proposition 4 (PROVED) is the weak-gate analogue of Proposition 9: if C_p owns a bottom segment of every world's key order, then C_p is not competitive.
   - At a single interior imprecise model these conditions can be avoided (Proposition 5, PROVED). Being a threshold set at two worlds is enough.
   - So the obstruction is not local in p. It sits on the edges.
4. **Nearby (item 3).** World i's priority on the steps of M_i cannot be one fixed key serving both edges at e_i. What remains open:
   - priorities chosen from the record (at least: different on M_i for edge-ij and edge-ik records);
   - or ties on M_i, broken by a secondary rule.

   Both lose the proof of no cycles (Lemma 2 of the note), so (TC) must be checked directly. This is design (a) of the note's next steps, now forced.

## 0. Setting and one reformulation

**Classes.** A mixed problem has one coordinate of the odd sign. Call that world the *minority* w(g), and write M_w for the class; M_1, M_2, M_3 partition the mixed problems up to null sets. In the simplex, M_w consists of the lines that separate e_w from the other two vertices.

**Regular advice.** Write A for the advice good for the two majority worlds, B for the advice good for w, and S for silence.
- At a majority world the ranks are A 0, S 1, B 2. At w they are 2, 1, 0.
- So on M_w the two majority worlds have equal ranks, and r_w = 2 − r_maj.
- A *regular* model (no contradiction, correct on unanimous problems) is determined by its ranks at any single world.

**Coherent models.** On M_w, D_K is A if K lies strictly on the majority side, B if K lies strictly on e_w's side, and S if the line meets K.

**Which steps matter.** Two regular models differ only on mixed problems, and only in steps with j ≤ 2. So the brief's convention (contradiction and unanimous steps get the lowest keys) never enters a comparison between regular models.

Write C ▷_i X when the weak gate or guidance holds for the pair (C, X) at world i. That is, either T^off_i(C,X) is null, or T^on_i(C,X) is non-null and ess inf of k_i over T^on_i < ess inf of k_i over T^off_i. Steps of X that C lacks ("X-steps") are losses for X; steps of C that X lacks ("C-steps") are gains.

**Lemma 0 (PROVED; immediate from the definitions).**
- C ▷_i X says that, reading the world-i step sets upward from the lowest key, the first essential disagreement is an X-step: X is strictly worse in this lexicographic order.
- Ties of essential infima count as failures.

**KKM consequence (PROVED).** Take any rule in which every accepted C ⪯_i X with C ≠ X has C ▷_i X. Suppose every C_p is competitive on supp p and every section A_i(X) = {p : C_p ⪯_i X} is closed.
- KKM gives, for every X, some q with C_q ⪯_i X at all three worlds.
- Selected models are coherent, hence regular.
- So (★): *a regular X that no regular C ≠ X beats at all three worlds must itself be selected.* In fact, beating X at the worlds named in a lemma is enough.

## 1. A shared problem order (item 1)

**Lemma 1 (bottom-gainer lemma; PROVED).** Let κ be a function on mixed problems with null level sets, and let X be regular. Suppose the following holds for every regular C, every world i, and a.e. pair of problems g, g' on which C and X differ with κ(g) < κ(g'): if g carries a world-i C-step, then some world-i C-step at g has a smaller key than every world-i X-step at g'. Then no regular C ≠ X has C ▷_i X at all three worlds.

*Proof.*
1. Let Δ = {C ≠ X}, with β = ess inf of κ over Δ. Let G_i ⊆ Δ be the problems where X is better at world i, and L_i = Δ ∖ G_i.
2. At every problem in Δ all three ranks change: the majority worlds move one way and the minority world the other. So every problem in Δ lies in some G_i.
3. By pigeonhole over the sets Δ ∩ {κ < β + 1/n}, some i has ess inf of κ over G_i equal to β. Fix this i.
4. Write a and b for the essential infima of the keys of the C-steps and of the X-steps at world i. Suppose b < a, and pick a' with b < a' < a.
5. Some non-null set of X-steps has keys below a'. These steps lie over L_i, where κ > β a.e. So they include a non-null part over {κ > x} for some x > β.
6. The set G_i ∩ {κ < x} is non-null, and each of its problems carries a C-step. By hypothesis one of them has a key below the key of any of those X-steps, so below a'.
7. Hence a < a', a contradiction. So a ≤ b, and C ▷_i X fails. (The C-steps are non-null, so guidance does not apply.) ∎

**Theorem 1 (shared problem-lexicographic order; PROVED).**
- *Hypothesis.* There is a κ with null level sets such that, at every world, k_i(g,j) < k_i(g',j') whenever κ(g) < κ(g'), for all j, j' ≤ 2.
- *Freedom left.* Within one problem, each world may order its two levels as it likes. The orders between problems may also differ between worlds by increasing reparametrisations.
- *Conclusion.* No regular model beats another at all three weak gates. By (★), every regular model would have to be selected, but incoherent regular models exist. So no selection satisfies (S) with closed sections, for any verdicts and any target.
- *Proof.* The hypothesis of Lemma 1 holds for every X. ∎
- CHECKED: in `t1_basic.py`, shared-lexicographic keys leave all 729 (N = 6) and all 6561 (N = 8) regular models undominated.

**Where the sketch breaks: level offsets (PROVED; CHECKED).** Take k_i(g,1) = κ(g) and k_i(g,2) = κ(g) + 10 at every world, with κ ∈ (0,1).
- *The rival.* Let C be regular with A on non-null sets E_1 ⊆ M_1 and E_3 ⊆ M_3. Let X be C made silent on E_1 ∪ E_3.
- *World 2* (majority on both sets) only gains steps, so guidance applies.
- *World 1* gains level-1 steps on E_3 (keys below 1) and loses level-2 steps on E_1 (keys above 10). Its lowest change is a step X gains, which is a loss for X, so the gate passes.
- *World 3* is symmetric to world 1.
- So C ▷_i X at all three worlds: C dominates X at the gate level. The step "the bottom change is a gain at some world" fails because A → S is a gain only for the minority world, and only at level 2, which these keys place above every level-1 step.
- CHECKED: 9747/9747 such pairs on 9 cells (`t6_shared_order.py`).

**Proposition 2 (offsets in one direction; PROVED).** Let k_i(g,j) = φ_ij(κ(g)), with φ_ij strictly increasing and κ with null level sets.
- **(a)** If φ_i1 ≤ φ_i2 at every world, then every never-silent regular X has no regular dominator. One example is "A on every mixed problem", which is incoherent: it would need K on the majority side of lines near every edge.
- **(b)** If φ_i1 ≥ φ_i2 at every world, then X = (B on M_3, S on M_1 ∪ M_2) has no regular dominator. It is incoherent, because B on all of M_3 forces K = {e3}, and then M_1 lines are A, not S.

*Proof.* Apply Lemma 1 with a single increasing ψ_i per world such that, at a changed problem g, the lowest C-step key is at most ψ_i(κ(g)) and the lowest X-step key is at least ψ_i(κ(g)).
- In (a), take ψ_i = φ_i1. A world that gains against a never-silent X becomes good, so it loses level 1. Every added step is keyed at least φ_i1.
- In (b), take ψ_i = φ_i2 for i = 1, 2 and ψ_3 = φ_31. Check the six change types: at worlds 1 and 2 gains only leave "bad" (level 2), and every addition is keyed at least φ_i2. At world 3 every gain is keyed at most φ_31, and additions occur only as good → S (level 1). ∎

**Mixed directions (CHECKED, finite only).** For all 8 patterns of "which level is lower" at each world, with offsets 0.05 and 10, some class-constant regular rivals have no regular dominator on 9 cells (`t6_shared_order.py`). Among them are incoherent ones: "AAA", or "SSB" for pattern (2,2,2) with large offsets. This is not proved in the continuum, and it is not needed given Theorem 6.

## 2. One index (item 2)

Call a regular change of C on a set P *c-cheap for world i* if it removes, on a non-null set, world-i steps with key < c_i, and adds at no world j a step with key < c_j.

**Proposition 3 (rival recipe; PROVED).**
- *Recipe.* Suppose that for some c ∈ R³ each world has a non-null set of problems carrying c-cheap changes for it. Put those changes on pairwise disjoint non-null subsets; this is possible because μ is atomless. The resulting regular X has C ⋫_i X at all three worlds. Under the weak-gate rule, C ⪯_i X fails everywhere, whatever the verdicts.
- *Converse.* If C ⋫_i X at all three worlds, with strict inequalities between the essential infima, such a c exists: take c_j = ess inf of X's added world-j keys.
- *Proof.* At each world the removed steps reach below c_j and the added ones do not. ∎
- *Restated.* Say world i is *protected below c* if a.e. change of C that removes a world-i step keyed below c_i adds, at some world j, a step keyed below c_j. Then C is gate-competitive against regular rivals only if, for every c ∈ R³, some world is protected below c. The condition is also sufficient, up to rivals that win through an essential-infimum tie.

**Proposition 4 (weak-gate analogue of Proposition 9; PROVED).**
- *Statement.* Suppose that at every world i, C owns a bottom segment: for some c_i, C has a non-null set of world-i steps keyed below c_i, and the mixed regular steps keyed below c_i that C lacks form a null set. Then some regular X has C ⪯_i X at no world, so C is not competitive on {1,2,3}.
- *Proof.* Use Proposition 3 with this c. No added step can be keyed below c_j, and moving to the world-i-good advice on problems that carry C's low world-i steps is c-cheap for world i. ∎
- CHECKED: 35/35 random instances (`t7_single_index.py`).
- *Why Proposition 9's rival does not transfer.* Proposition 9 used contradiction to add steps at every world. Under the weak gate, added low-keyed steps help C: with the brief's convention, any rival that uses contradiction or unanimous errors passes the weak gate at every world. Only regular rivals can defeat C. "Owning the bottom" replaces "crossed pair".

**Proposition 5 (the conditions can be avoided at one index; PROVED).**
- **(a) Two thresholds.** Suppose U_1(C) and U_2(C) are threshold sets of k_1 and k_2. Then for every regular X ≠ C, some world passes the weak gate or guidance.
  - *Proof.* If X adds a step at world 1 or 2, that world's added steps lie below its threshold and its removed steps lie above it, so the gate passes there. Otherwise X is weakly better than C at worlds 1 and 2. Then X equals C on M_1 ∪ M_2 and is A-ward of C on M_3, so world 3 has guidance. ∎
  - Keys with this property exist for any regular C. So at a single interior imprecise model, Propositions 3 and 4 can be avoided.
- **(b) One threshold.** If only U_1(C) is a threshold set, C fails all three gates for some regular X if and only if (up to ties) the following holds. There are an A-ward change on a non-null P ⊆ M_3 (it gains at worlds 1 and 2) and an A-ward change on a non-null Q ⊆ M_2 (it gains at worlds 1 and 3) such that:
  - the lowest world-2 removed key on P is below the lowest world-2 added key on Q, and
  - the lowest world-3 removed key on Q is below the lowest world-3 added key on P.
  - *Proof.* Failing world 1 forces X to be a weak world-1 improvement. Then world 2 can gain only on M_3 and world 3 only on M_2, and M_1 changes add only losses. ∎
- CHECKED: (a) 300/300 instances; (b) 300/300 agreements with brute force (`t7_single_index.py`).

**Answer to item 2.** At one interior imprecise index nothing is forced, because a suitable choice of keys always protects C_p. What the keys must look like at each interior p is the protection condition of Proposition 3 for every c. It can be met in three shapes:
- C_p is a threshold set at two worlds;
- C_p is a threshold set at world i, and worlds j and k do not cross on the world-i-improvable parts of M_k and M_j, in the sense of Proposition 5(b);
- C_p is a threshold set at no world, and every cheap gain at one world is paid for by a cheap loss at another.

Threshold sets of one key form a chain, so a two-dimensional family cannot use the first two shapes on an open set. Section 3 makes the family question moot for fixed keys.

## 3. Fixed keys fail in three worlds (item 3)

For a problem g in M_1, let z_12(g) ∈ (0,1) be the point where its line meets [e1,e2], measured from e1, and define z_13(g) likewise on [e1,e3].
- Every pair in (0,1)² comes from exactly one line in M_1.
- Under the Gaussian measure, (z_12, z_13) has a positive continuous density on (0,1)². The reason is that z_12 = |g_1|/(|g_1|+g_2) and z_13 = |g_1|/(|g_1|+g_3) define a smooth submersion whose fibres are rays.

**Lemma 6.1 (edge threshold models; PROVED).** Fix c ∈ R. Let X_c be the regular model with:
- advice A on M_3;
- on M_1 ∪ M_2, world-1 rank r(g) equal to the largest r ≤ 2 with k_1(g,j) ≥ c for all j ≤ r.

Suppose every non-guidance comparison accepted by world 1 passes the weak gate of k_1, and world 2 satisfies strict (G). If C is regular with C ⪯_1 X_c and C ⪯_2 X_c, then C = X_c. The same holds for X'_c, which is A on M_2 and built the same way on M_1 ∪ M_3, with world 3 in place of world 2.

*Proof.*
1. Every world-1 step of X_c has key ≥ c. Wherever C has a higher world-1 rank than X_c on M_1 ∪ M_2, C has the step (g, r(g)+1), whose key is below c by the maximality of r.
2. So if those problems form a non-null set, the essential infimum of the keys of C's extra steps is below c, which is at most the essential infimum of the keys of X_c's extra steps. The weak gate fails, and guidance fails too, so C ⋠_1 X_c.
3. Otherwise C is weakly better than X_c at world 1 on M_1 ∪ M_2. The ranks of worlds 1 and 2 are opposite there, so C is weakly worse at world 2 on M_1 ∪ M_2. On M_3, X_c is A, which is best for world 2.
4. So X_c is a pointwise weak world-2 improvement of C. Strict (G) gives C ⋠_2 X_c unless C = X_c. ∎

**Lemma 6.2 (PROVED).** A coherent model that is A a.e. on M_3 is D_K with K ⊆ [e1,e2]. Its world-1 rank on M_1 is ≥ 1 exactly on {z_12 ≤ max K}, up to null sets, where max K is the far end of K measured from e1.

*Proof.*
- If m ∈ K had m_3 > 0, a non-null set of M_3 lines would pass between m and [e1,e2], and on them D_K would not be A.
- For K ⊆ [e1,e2], an M_1 line crossing the edge at z has K strictly on e1's side (world-1 rank 0) if and only if max K < z. ∎

**Theorem 6 (PROVED).** The following hypotheses are inconsistent:
- **(H1)** Three worlds; problems in R³ modulo sign with the Gaussian measure. Only the density fact above, and the non-null set of lines in Lemma 6.2, are used.
- **(H2)** At world 1, every accepted C ⪯_1 X with C ≠ X and T^off_1 non-null passes the weak gate of a fixed key k_1 whose restriction to {(g,1) : g ∈ M_1} has null level sets. The verdict Φ_1 is arbitrary.
- **(H3)** Worlds 2 and 3 satisfy strict (G).
- **(H4)** A selection p ↦ C_p of coherent models, competitive on supp p at every p of the closed simplex, with every section A_i(X) closed, for every regular X.

*Proof.*
1. The function c ↦ μ{g ∈ M_1 : k_1(g,1) ≥ c} has no jumps, because there are no atoms. So it takes the value μ(M_1)/2 at some c.
2. By (★) and Lemma 6.1, X_c and X'_c are selected, hence coherent.
3. Their world-1 ranks on M_1 are ≥ 1 exactly on E := {k_1(·,1) ≥ c}.
4. Lemma 6.2, and its analogue for [e1,e3], give E = {z_12 ≤ y} = {z_13 ≤ y'} a.e., with y, y' ∈ (0,1) because μ(E) = μ(M_1)/2.
5. But the difference of these two strips contains (0,y] × (y',1), which has positive measure. ∎

**What Theorem 6 does not use:** undominatedness, (TC), (IB), (LA), (C), (LF); any property of k_2, k_3 or of the verdicts; the target; and any interior index, apart from KKM itself. A strong gate implies the weak gate, so the theorem covers Proposition 9's setting too and proves its CONJECTURE: fixed-order gates fail in three worlds altogether.

**Where the conflict sits.** At e1, the problems in M_1 belong to both edge problems. On [e1,e2], the two-world construction keys world 1's level-1 steps by z_12; in the note this is l⁻¹(t). On [e1,e3] they must be keyed by z_13. One fixed key cannot do both.

**Checks.**
- CHECKED: on cells with a crossed pair in M_1 and lines hugging both edges at e1, every X_c and X'_c is unbeaten at its two worlds (exhaustive search), and every random key draw yields an incoherent one: 100/100 draws on 6 cells and 60/60 on 8 cells (`t5_edge_rigidity.py`).
- NUMERICS: on random arrangements of 6 and 9 lines without such lines, simulated annealing (`t4_coherent_pareto.py`) found keys for which the target interior model is unbeaten and every unbeaten model is coherent, in 5 of 6 runs. So screens of three-world mechanisms on cell models must include crossed pairs and edge-hugging lines.
- NUMERICS (`t2_minpareto.py`, `t3_inspect.py`): the smallest sets of unbeaten models for three lexicographic orders on 6 cells have 2N + 1 = 13 elements. They form a tripod centred at the incoherent model "A on every mixed problem".

## 4. Nearby: what a construction must change

The proof uses exactly two things:
- a single priority at world 1 on the steps of M_1, used both for comparisons with models that are A on M_3 and for comparisons with models that are A on M_2;
- null level sets of that priority.

So a design that keeps weak gates must do one of the following.

- **(E1) Priority chosen from the record on the vertex classes.** World i's priority on the steps of M_i must differ, at least, between records in the edge-[e_i,e_j] problem and records in the edge-[e_i,e_k] problem. Lemma 6.1 then fails as stated, because X_c is a threshold set for only one of the priorities.
  - *Price.* Lemma 2's proof that there are no cycles needs one order per world, so (TC) must be proved directly.
  - *Constraint from Theorem 1.* The three worlds' record-chosen priorities must not share a problem-lexicographic order.
- **(E2) Ties on the vertex classes.** Give k_i(·,1) an atom on M_i and decide the tie by a secondary rule. Lemma 2's window argument uses null level sets, so (TC) must again be re-proved. The content then moves into the tie-breaking rule, which is again record-based.

**Residual condition for any construction (from Lemma 6.1 and (★)).** Let k be any priority that world 1 uses, through a weak gate, on every comparison C ⪯_1 X_c with C regular (X_c built from k, so A on M_3). Then every edge threshold model X_c built from k must be selected. Its level-1 threshold sets on M_1 must therefore have the form {z_12 ≤ y}. The same holds for M_2 and M_3 at the other edges. I propose this as a new screen, **S11 (edge thresholds)**, to add to the design memo's list.

## Scripts (`PP2_py/`)

| Script | What it does | Label |
|---|---|---|
| `lexcore.py`, `geom.py` | Shared library: the weak gate as lexicographic codes; line cells; coherence by LP | — |
| `t1_basic.py` | Codes agree with the gate; shared-lexicographic keys leave every model unbeaten | CHECKED |
| `t2_minpareto.py`, `t3_inspect.py` | Smallest sets of unbeaten models are tripods | NUMERICS |
| `t4_coherent_pareto.py` | Random small arrangements do not show Theorem 6 | NUMERICS |
| `t5_edge_rigidity.py` | The mechanism of Theorem 6 | CHECKED |
| `t6_shared_order.py` | Offsets: the refutation, and rivals that no regular model beats at all three worlds | CHECKED |
| `t7_single_index.py` | Propositions 4 and 5 | CHECKED |
