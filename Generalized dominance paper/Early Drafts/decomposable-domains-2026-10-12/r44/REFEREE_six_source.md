# Referee report PP17: audit's six-source note (§§9–14) and the lead's selection-count note

22 October 2026. Independent referee. I read Brief 44, `AUDIT_six_source.md` (all of it, with §§1–2 and §§9–14 checked line by line), `LEAD_selection_count.md`, DESIGN_MEMO §8, and the definitions of records and copies in `AUDIT_guard_extension.md` and the (S)/(LA) wording in gate2d and earlier notes.

**Labels.** PROVED = a proof is given here or the author's proof was checked line by line. CHECKED = exact finite computation. NUMERICS = floating point (none used). CONJECTURE = unproved.

**Verdicts.** Correct / correct with repair (repair given) / wrong (counterexample given) / unclear.

**Scripts** are in `r9/PP17_py/`. They use exact rationals and were written without reading the audit's code.
- `geom.py`: the geometry.
- `records.py`: the record algebra.
- Run them as `python3 -B records.py three|six2|six_all|mut_noQ|mut_rev|six2_tref|six2_tref1|six_all_tref1`. Outputs are in the `*.out` files.

---

## 0. Summary

| Claim | Verdict |
|---|---|
| §9 geometry and advice table; W_ij overlap sets | Correct (CHECKED at ε = 3/10; PROVED for every 0 < ε < 1 with explicit h, d, L) |
| §13 geometry; table with R_i; F_i pointwise no worse than C_i at world i | Correct (same, plus a general lemma) |
| §10–11 three-source extension theorem | Correct |
| §11 "necessary division among defenders" | Correct |
| §13 eligibility rule (Q): every X ≠ T has an eligible source | Correct |
| §14 (TC) proof | Correct. The case analysis is complete for every copy, order and rotation (§3 below). |
| §14 (IB) copies: no repair ends at T or at a coherent source; source copies end only at the named source, with source exactly the named source | Correct |
| §14 undominatedness of all seven sources | Correct with repair R2 ("that direction is not installed" needs a record-identity argument; supplied) |
| §14 strictness, no new ties, (G), (LA), direct (C) | Correct |
| §14 non-endorsement at every world | Correct with repair R3 (state the endorser class; the proof then goes through as written) |
| §13 "retains every comparison of section 10" | Correct with repair R1 (fix d once, for both sections) |
| §9 / §13 "only geometric conditions used" | Correct with repair R4 (§13 also uses F_i ≤_i C_i pointwise, which is not an advice-table condition) |
| Lead, Lemma A | Correct, and true for every undominated M, selected or not |
| Lead, Lemma B | Correct |
| Lead, Theorem C(i), C(ii), and the use of Sierpiński | Correct |
| Lead, Theorem C(iii) "OPEN" | Correct that it is open; wording repaired; the topological route provably cannot settle it (§7.3) |
| Lead, Lemma D | Correct |
| Lead, "Relevance" paragraph and Brief 44's "only countably many sources" | Correct with repair: the count is of witness groups, not of sources |
| Lead, Lemma E | Correct, and holds when T is undominated but not selected |

**Bottom line.**
- The six-source theorem is a correct theorem, and so is the non-endorsement corollary.
- The construction is still not an (S)-system. One point is missing from the note and matters next. In the module as built, **T has no defence at any world against many rivals in its own class**: 18 of the 153 two-cell rivals and 2,277 of the 4,095 cell rivals (CHECKED). An explicit one is in §5.
- Two ways of adding target-reference records T ⪯_w X were tested on cells (§5):
  - installing them at every world where X worsens T makes every C_i dominated through (IB) copies;
  - installing them at a single world passes every finite check.
  That one-world version is the nearby result I recommend proving next.

---

## 1. Conventions used in checking

- A record is (D, a, b): a disagreement set D, with old advice a and new advice b on D.
- A copy of the record is any pair (A, B) with A = a and B = b on D, and A = B off D.
- At world w the rank change of a copy at a problem g is r_w(b(g)) − r_w(a(g)) on D and 0 off D. **It does not depend on the context.** Every "nondecreasing on R_i" or "+1 on B_i" argument in the note is therefore automatically valid for all copies.
- Composition of two copies A → B → C is possible exactly when b_r = a_s on D_r ∩ D_s.
  - The composite A → C is then fixed by r and s alone: a_r → b_s on D_r, and a_s → b_s on D_s \ D_r.
  - So a 3-cycle A ⪯ B ⪯ C ⪯ A through a new link exists iff one of two things happens:
    - (i) two installed records compose and the reverse of the composite is accepted; or
    - (ii) one installed record has no strict worsening point, so that two guidance links can close it.
  - Every rotation of every cycle falls under (i) or (ii), because in a 3-cycle any two links are cyclically adjacent.
  - This is what `records.py` enumerates.
- (TC) forbids only A ⪯ B ⪯ C with C ≺ A. For every record type, the audit's arguments show something stronger: **no accepted 3-cycle passes through any new record at all**. The finite checks confirm this: 0 accepted 3-cycles in every run.
- (LA) is read as in the write-up: the class of coherent undominated models is nonempty.
- Direct (C) is automatic when there are no distinct all-world ties.

---

## 2. Geometry (§3, §9, §13)

### 2.1 Exact values at ε = 3/10 (CHECKED, `geom.out`)

Here c = 7/30.

**§3 table, with h = 7/60 and d = 1/5:**
- (1, 1, −11/5): T has lower −53/75 and upper 19/75; every m ∈ K gives −1/15.
- (1, 1, −9/5): T has lower −37/75 and upper 26/75; every m ∈ K gives +1/15.

All four values agree with the note.

**§9 and §13 tables.** These were checked for (h, d, L) = (7/60, 1/10, 5), (7/60, 1/5, 5) and (7/60, 1/10, 4). Every strict sign claim holds:
- T is strictly silent on all nine sets A_i, B_i, R_i.
- (C_i, F_i) give (minority, minority) on A_i, (majority, minority) on B_i and (majority, majority) on R_i.
- C_j and F_j, j ≠ i, are strictly silent on A_i, B_i and R_i.
- On W_ij, T accepts the minority-k answer, while C_i, F_i, C_j and F_j are all strictly silent.
- F_i has coordinate i equal to 1/(3 − 2d) exactly.
- Note that d = 1/5 already satisfies the stronger §13 bound, since 3d = 3/5 < min(1, 9/7, 9/8) = 1.

### 2.2 Every 0 < ε < 1 (PROVED)

**Linear forms.** For g with coordinate i equal to −x and the other two coordinates equal to 1:
- T: lower = c(2 − x) − εx and upper = c(2 − x) + ε.
- A member of K_j (j ≠ i) with coordinate i = t gives 1 − (1 + x)t, so it changes sign at t = 1/(1 + x).
- A member of K_i gives (2 − x)/3.
- A member of F_i gives ((2 − 2d) − x)/(3 − 2d).

With x = 2 + d, 2 − d, 2 − 3d these signs reproduce the table exactly. T's strict silence on all nine sets is equivalent to d < ε/c together with 3d < 2ε/(c + ε). The note's "3d < min(1, ε/c, 2ε/(c + ε))" is sufficient.

**Explicit choice.** Take
- h = c/2,
- L = ½((1 − c)/c + (1 − h)/h),
- d = min(1/5, ε/(2c), ε/(3(c + ε))).

**Other groups are strictly silent.** C_j, j ≠ i, ranges over t ∈ [h, 2/3 − h]. F_j ranges over t ∈ [h′, 1 − f − h′], where
- f = 1/(3 − 2d),
- h′ = 3h(1 − d)/(3 − 2d) < h,
- 1 − f − h′ = (1 − d)(2 − 3h)/(3 − 2d).

The thresholds 1/(3 + d), 1/(3 − d) and 1/(3 − 3d) all lie in (1/3.2, 1/2.4] when d ≤ 1/5. Because h ≤ 1/6 and (1 − d)(2 − 3h)/(3 − 2d) ≥ 0.8 · 1.5/2.6 > 0.46 > 1/2.4, every threshold lies strictly inside both ranges.

**W_ij.** At (L, −1, −1), with L in coordinate k, T's lower prevision is cL + c − 1 > 0 iff L > (1 − c)/c. Members of C_i or F_i give (L + 1)t − 1, where t is coordinate k. Silence needs (L + 1)·(lowest t) < 1 < (L + 1)·(highest t):
- the left inequality follows from L < (1 − h)/h and h′ < h;
- the right one follows from L + 1 > 1/c ≥ 3 and highest t ≥ 0.4.
The interval for L is nonempty because h < c.

**Disjointness.** The 9 + 3 central problems are pairwise distinct directions modulo sign. All inequalities are strict, so small open neighbourhoods work.

`geom.py` confirms this explicit choice exactly at 44 values of ε, from 1/1000 to 999/1000.

### 2.3 F_i is pointwise no worse than C_i at world i (PROVED; the claim is correct)

F_i(g) = C_i(S g), where S multiplies coordinate i by a = 1/(1 − d) > 1. Lower and upper previsions are monotone in the gamble.
- If g_i > 0, then Sg ≥ g. So C_i accepting g implies F_i accepts g, and F_i rejecting g implies C_i rejects g.
- If g_i < 0, the same holds with the inequalities reversed.

Either way r_i(F_i(g)) ≤ r_i(C_i(g)) at **every** g. This holds for any credal set, so it survives thickening. A random exact test of 4,000 gambles × 3 worlds found 0 failures. The inequality is strict on B_i, and at the other two worlds B_i goes from good to bad, as stated.

---

## 3. The (TC) proof in §14: completeness of the case analysis (correct)

Fix a world w.

**Records with an old source in another group.** Let S be in group i ≠ w, with new side T, a group-w source, or a rival (types s2, s3, and repairs from group i at world w). Each such record is +1 on all of R_i: majority, which is good at w, becomes silence.

Every accepted record at w is ≥ 0 on R_i:
- a_S and b_SX are 0 there, because group-w sources and rivals are silent;
- r_i and r_j are 0;
- records from the third group are 0;
- guidance is ≥ 0.

So no cycle of any length contains these records. This is the correct use of "R_i outside the six sets".

**Records containing r_i (i ≠ w).** Rank changes on B_i:
- r_i is +2;
- a, r_j (j ≠ i) and every other record left after the step above are 0;
- b is at least −1, since it starts from silence;
- guidance is ≥ 0.

So:
- r_i with at most one b sums to at least +1;
- r_i with two b's sums to −2 on R_w;
- r_i with r_j and a third link needs −2 on B_i, which nothing supplies;
- two r_i are not composable.

These cases are exhaustive, including mixed cycles with guidance.

**Only a, b and guidance remain.** On R_w, a is +1 and b is −1.
- Two a's cannot compose: after an a, R_w carries the majority answer, and the next a needs silence there.
- Two b's cannot compose, for the mirror reason.
- Three new links sum to an odd number.

For an a/b pair in either order, I re-derived the three bullet cases independently. Let E be the (Q) witness set. On E:
- if a_Q acts first at g, then Q(g) = S(g) is forced, and the net change is T → X, which is > 0;
- otherwise the net change is S → X, which is > 0;
- b then a cannot both act at g, because X(g) ≠ T(g).

So the composite has a strictly positive point and no guidance link closes it. A single a has its witness on R_w, and a single b has its witness on E.

**Conclusion.** Every rotation is covered, because the two new links in a mixed 3-cycle are adjacent in some rotation.

**CHECKED.** The finite runs match the proof:

| Run | Records per world | Composable ordered pairs | Accepted 3-cycles | Records without a worsening witness | Accepted reverses |
|---|---|---|---|---|---|
| 153 two-cell rivals | 742 | 4,596 | 0 | 0 | 0 |
| All 4,095 cell rivals | 21,040 | 81,624 | 0 | 0 | 0 |

The record counts 173 (three-source) and 742 (six-source, two-cell) agree with the audit's own scripts, which were written independently.

---

## 4. (IB) copies, source protection, undominatedness, (Q), strictness

### (Q) (correct)

Since T is silent on all six sets, every X ≠ T has a non-null set on which X takes one of three values on one A_i or B_i. The case table:

| Set | X's value | Eligible sources |
|---|---|---|
| A_i | majority | C_i, F_i |
| A_i | minority-i | group-j sources (silent; bad at j) |
| A_i | contradiction | C_i, F_i, and group j |
| B_i | majority | F_i only (C_i is bad at i there, so it is not eligible) |
| B_i | minority-i | group j |
| B_i | contradiction | F_i, and group j |

Every repair has a worsening witness at every world where it is installed: E at its own group's world, and R_i elsewhere.

### Copies ending at named models (correct)

**Repairs.** No repair ends at:
- T, because of the witness E, where X ≠ T;
- its own group, because on R_i the new side is silent while both members say majority;
- group j, because on W_ij the new side is T's definite answer while group j is silent.

**Source records.**
- T → S and S′ → S (S in group i) cover both R_i and B_i. They end only at S, and their source is then exactly T or S′.
- S → T ends only at T, with source exactly S. It cannot end at group i (R_i) or at group j (W_ij).
- C_i → F_i is supported on {C_i ≠ F_i}, which contains B_i, where its new side is the minority answer. That answer differs from T, from C_i and from every other group. So it ends only at F_i, with source exactly C_i.

CHECKED: `six2.out` lists every incoming copy at each of the seven sources. All of them come from the stated named source.

### Undominatedness (correct with repair R2)

The five bullets of §14 are right. In each, "that direction is not installed" should be proved by record identity, not asserted. Here is a uniform argument. At world w, the R-signature (the rank change on R_1, R_2, R_3) of each installed type is:

| Type | On R_w | On R_i (i ≠ w) |
|---|---|---|
| a | +1 | 0 |
| b | −1 | 0 |
| s2, s3, repairs from group i | 0 (s2, repairs) or +1 (s3) | +1 on their own R_i |
| r | 0 | 0 |
| guidance | ≥ 0 | ≥ 0 |

Each proposed dominating comparison has a −1 or −2 point where the guidance column is ≥ 0, so it is not guidance. Where its signature coincides with an installed type, the old or new side differs from that type on R_i, B_i or a witness set, so it is not that record either. (Example: S → T at world i has signature −1 on R_i, like b. It would equal a b-record only if its rival were T.)

CHECKED: in the six-source runs, all candidates, meaning every named source and every source of an incoming copy, fail to dominate. No advice value at any cell is weakly better at all three worlds than any source's value, so there is no pure-guidance dominator either.

### Strictness, ties, (G), (LA), direct (C) (correct)

- Every installed record has a strict worsening point at its world, so strict (G) holds.
- No installed record's reverse is accepted. The reverse of a would equal a repair only if X = T, and similarly for b. The reverses of the other types have a −1 on some R_i, or a −2 on B_i.
- So every new comparison is strict, and there are no ties even at a single world. (LA) and direct (C) follow.

### Non-endorsement (correct with repair R3)

The note should define the class. At world i, write L(X) = Σ_{j=1..3} ν_j({g : r_i(X(g)) ≥ j}), where the ν_j are finite, finitely additive charges with ν_j(E) > 0 for every non-null E. "Weakly endorses" means that every accepted comparison of the kinds used implies L(X) ≤ L(Y).

With that class the proof is correct:
- T ⪯_i F_i **is installed**. It is the a-type at world i, and it appears in `six2.out` as `a:T->F1` at world 1.
- δ = L(C_i) − L(F_i) ≥ ν_1(B_i) + ν_2(B_i) > 0. This uses §2.3 (no negative contributions anywhere) and positivity on B_i, so δ > 0 is justified.
- C_i is eligible for every X_n.
- Hence ν_2(E_n) ≥ δ for infinitely many disjoint E_n ⊆ A_i, contradicting ν_2(A_i) < ∞.

Only finite additivity, positivity on B_i, and finiteness of ν_2 on A_i are used. The statement is sharp in the way the note says: it does not reach non-Archimedean or unbounded representations.

### Repairs

- **R1.** §13 says "choose d sufficiently small" and then claims to retain §10's comparisons. That is literally true only if §9 and §10 use the same d. Fix d once, at the start of §9, by the §2.2 choice. That d satisfies every condition in both sections.
- **R2.** As above.
- **R3.** As above.
- **R4.** In §13, besides the advice table and the W_ij condition, the proof also uses "F_i is pointwise no worse than C_i at i". It is used for F_i ≺_i C_i, for undominatedness, and for δ > 0. That condition is automatic for the rescaling (§2.3), but it is not an open advice-table condition, so it belongs in the list.
- **Minor.** §15 names the folder `reciprocal-source-check/`, but the scripts are in `AUDIT_reciprocal_py/`. The two probe scripts fail under `python3 -I` because they import `check` from their own folder; they run with `python3 -B`, and all three passed when run that way.

---

## 5. What the theorem does not give: T's own defences (CHECKED; not claimed by the audit)

**An explicit undefended rival.** Let X* = T with the majority answer on A_1 ∪ A_2.
- At world 3, X* is a strict pointwise improvement of T, so strict (G) refuses T ⪯_3 X*.
- At worlds 1 and 2, X* is mixed, for example bad at world 1 on A_1 and good at world 1 on A_2. Nothing installs T ⪯_1 X* or T ⪯_2 X*.

So T has no defence against X* at any world. T therefore cannot be selected at any index of an (S)-system that contains this relation unchanged.

**How common this is (CHECKED).** T has no defence against:
- 11 of the 63 rivals in the three-source module;
- 18 of the 153 two-cell rivals;
- 2,277 of the 4,095 cell rivals.

**Two attempted fixes.**
- *Target-reference records at every world where X worsens T somewhere* (`tref_allworlds.out`). This fails. Take X = T[A_1 → minority, B_1 → majority], which agrees with C_1 on its support. The (IB) copy of T ⪯_w X ends at C_1 at all three worlds. Its source C_1[A_1 ∪ B_1 → silent] then dominates C_1. This is the audit's own §2 exposure mechanism.
- *A single world* (`tref1.out`, `tref1_all.out`). Install T ⪯_w X only when T has no guidance defence, and only at one world w where X worsens T (the first such world). On all 4,095 cell rivals this gives:
  - 0 accepted 3-cycles;
  - 0 non-strict records;
  - all seven sources undominated;
  - a defence by T against every rival.

  This is CHECKED on cells only. A measurable proof is not given. Part of the §14 argument carries over (the new records are 0 on every R_i), but cycles mixing r_i with these records need the ordering argument on B_i that I sketched only informally.

**Recommendation.** State and prove the one-world target-reference extension of §13 as the next theorem. It is the nearest result to T-competitiveness inside the class.

---

## 6. Finite check: design and limits

**Cells.** There are 15 cells: A_1–A_3, B_1–B_3, R_1–R_3, W_12, W_13, W_23, a unanimous cell U, and two common mixed cells H1 = (10, −1, −1) and H2 = (1, 1, −10). Every advice value is computed exactly from the credal sets at ε = 3/10, h = 7/60, d = 1/10, L = 5.

**Rivals.** Three runs: all 63 on A (three-source); all 153 changing at most two of the six cells; and all 4,095 on the six cells.

**What is checked.**
- every two-record composition in every common context, in both orders;
- closure by any accepted record (guidance or installed);
- a worsening witness for every installed record (this covers new + guidance + guidance cycles);
- accepted reverses;
- all copies ending at each source, and their sources;
- domination of each source by every candidate;
- eligibility, and strict all-world domination of every rival.

**Mutation tests (`mutations.out`).** The checker does catch faults:
- installing repairs while ignoring (Q) produces 93 (TC) violations per world and 12 dominators of T;
- installing C_i ⪯_i F_i is flagged as non-strict, and each F_i becomes dominated.

**Limits.** As the brief says, the cells are evidence for the record algebra only. They say nothing about (S): an atom cannot carry the infinitely many E_n of the non-endorsement argument, and closed sections are not tested.

---

## 7. The lead's note

### 7.1 Lemma A (correct)

The proof is right. It uses only that M is undominated and that the sections A_w(M) are closed. (S) demands closed sections for **every** fixed X, so Lemma A holds for every undominated M, selected or not.

### 7.2 Lemma B, Theorem C(i), Theorem C(ii) (correct)

**Lemma B.** Competitiveness at e_i together with strict (G) is exactly what is needed.

**C(i).**
- Φ_M ⊆ U_K holds because C_p ≈ M puts C_p into M's tie component; ≈ is not transitive, but components do not need transitivity.
- F_M ⊆ Φ_M holds by reflexivity.
- With finitely many values, the U_K form a finite closed partition with at least two pieces, {V_1} and {V_2}. That contradicts connectedness.

**C(ii).** With no ties, F_M = Φ_M is closed. Sierpiński's theorem (1918) says a continuum is not the union of countably many, and at least two, pairwise disjoint nonempty closed sets. It applies because Δ is a compact connected metric space and the fibres include those of V_1, V_2 and V_3. So there are uncountably many fibres.

### 7.3 Theorem C(iii) (open; correct with repair)

**Wording repair.** The proof of (i) and (ii) shows more than the note states. If every U_K were closed, Sierpiński would apply to the countably many components, and {V_1} is a component with U = F_{V_1} closed. So in case (iii) **some tie component K must be infinite, with U_K not closed**. It need not contain an infinite chain: a component with a vertex of infinite degree and no infinite path is not excluded. "Chain" should read "component".

**The closedness data alone cannot settle (iii) (PROVED).**
- Take a triangulation of Δ \ {e_1, e_2, e_3} that is locally finite there, with cells accumulating only at the vertices.
- Label each open cell σ by its own model, and each vertex by V_i.
- Declare σ ~ τ iff both lie in the closure of a common cell.

Then Φ_σ is the closed star of σ: a finite union of closed simplices, closed in Δ and missing the vertices. The vertex labels are isolated and the number of labels is countable. So every conclusion that Theorem C's proof draws from Lemmas A and B holds in this labelling. Any proof or refutation of (iii) must therefore use more of the axioms: sections for non-selected X, competitiveness, or the content of the models.

**Two facts that point that way (PROVED, short).**
- *(a) Accumulation.* If q ∈ cl F_N, then C_q = N or C_q ≈ N. Proof: Φ_N is closed and contains F_N.
- *(b) Edge ties.* Let p lie on the open edge {i, j}. Then every model N with C_p ≈ N is ij-complete: it gives the common answer a.e. where worlds i and j agree. Proof: otherwise fill N's failure set with the common answer to get X with X ≺_i N and X ≺_j N. Competitiveness gives w ∈ {i, j} with C_p ⪯_w X, and then N ⪯_w C_p ⪯_w X ≺_w N violates (TC). This is the lead's Lemma E argument with T replaced by N.

Together: every selected model whose fibre accumulates at an open-edge point is ij-complete. If it is coherent, its credal set lies in the edge face [e_i, e_j]. This rigidity near the boundary is the most promising lever on (iii). It does not settle it.

### 7.4 Lemma D (correct); the "Relevance" paragraph (correct with repair)

**Lemma D** is right. Pairwise intersections are null, and a finite measure has only countably many almost-disjoint non-null sets.

**The application overstates.** Audit's R_i is private to a **group**: both C_i and F_i are definite there. Within a group, the members are told apart by B_i, where both are definite. So Lemma D bounds the number of groups that have private witnesses, not the number of sources.

Repaired statement: *without ties, all but countably many selected models lie in groups with no private witness set, or share their group's private set with other selected models.* Lemma D puts no bound on the size of a group. Brief 44's line "private witness sets of audit's kind can protect only countably many sources" needs the same repair.

The six-source proof already uses shared witnesses as well, the W_ij, so the dichotomy "private or shared" describes it accurately.

### 7.5 Lemma E (correct)

The proof is correct.
- The required set E exists for T1 at every ε, edge and pair: near (1, 1, −2) rotated, T1 is strictly silent.
- Vertices are excluded by Lemma B.

**Strengthening (PROVED).** Neither Lemma A nor the (TC) step uses that T is selected. So if T is merely undominated, {p : C_p ≈ T} is a compact subset of the open simplex. This bears directly on live route (b) of DESIGN_MEMO §8.12, "T unselected but tied": any selected models tied with T sit at interior indices bounded away from the boundary.

---

## 8. Files

- `r9/PP17_py/geom.py`, `geom.out`: §2.
- `r9/PP17_py/records.py`: §§3–6.
- Outputs:
  - `three.out`, `six2.out`, `six_all.out`: PASS;
  - `mutations.out`: the injected faults are caught;
  - `tref_allworlds.out`: C_i dominated under the all-worlds fix;
  - `tref1.out`, `tref1_all.out`: one-world target reference, no failures except the expected copies ending at C_i, which dominate nothing.

A note on reading the `tref*` files: their final line says FAIL. That is not a failure of the checks. The script raises a deliberate flag whenever a copy from an unnamed source ends at a source. Those copies are expected for t-records, and none of them dominates.
