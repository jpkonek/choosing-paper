# Referee report: *A target-preserving coherent-defender extension* (AUDIT_guard_extension.md)

21 October 2026. Adversarial referee. I read the note in full, together with DESIGN_MEMO §8.11, PP13_repairs.md, PP14_cut_skeleton.md, and (for §7) AUDIT_rescaling_construction.md §§3–6 and `PP13_py/s1_certificate.out`.

**Verdict labels**
- **CONFIRMED**: the argument is correct as written, or its gaps are only the routine "up to null sets" kind.
- **CONFIRMED WITH REPAIR**: the claim is true, but the text needs the stated change.
- **WRONG**: the claim, or the conclusion drawn from it, is false. A proof or counterexample is given.

**Scripts** are in `REFEREE_guard_py/`. Run each one inside that folder as `python3 -I -B <script>`. Outputs are in the `*.out` files.
- `geom.py`: exact rational geometry at ε = 3/10, a = 20, L = 5.
- `cells.py`, `run_cells.py`, `cycles_any_subcollection.py`, `witness_s12.py`, `tr_forces_codesign.py`: exhaustive checks on a 6-cell abstraction.
  - The cells are G1, G2, G3, O1 (class 1), O2 (class 2), O3 (class 3).
  - All 4⁶ = 4096 four-advice models are included: coherent, incoherent, silent and contradictory.
  - The cell patterns of T and C₁, C₂, C₃ are the ones `geom.py` certifies exactly for the posterior defenders.

---

## 0. Summary

| Item | Verdict |
|---|---|
| §2 guard sets exist | CONFIRMED |
| §2 defender neighbourhoods V_i | CONFIRMED |
| §3 extension rule and record-based restatement | CONFIRMED (one wording clarification, R0) |
| Prop. 1 (exposed defenders; uniform triple; property (A)) | CONFIRMED |
| Thm 2: (G), (IB), no composition, no mixed triangle, (TC) for any subcollection, strictness, protection of T and of defenders, direct (C) | CONFIRMED |
| Lemma 3 (target-reference base) | CONFIRMED |
| §11 co-designed defenders C_i = D_{Φ_{s_i}(T)} | CONFIRMED |
| §11 non-additivity (infinite obstruction; finitely additive weights too) | CONFIRMED |
| §12 trap | CONFIRMED |
| §12 "(E_C) rules out precisely that direct composition" | CONFIRMED (as a literal statement) |
| §12 "(E_C) is a safeguard against the §12 obstruction" | **WRONG** (F2) |
| Lemma 4 (two-sided exposure) | CONFIRMED |
| §13 failure of (S) in the current relation | CONFIRMED |
| §13 / §0 "further extendability is the unresolved issue" for the strongest version (§11 + §12) | **WRONG** (F1, F2) |
| §6 local freedom | CONFIRMED |
| §7 retained certificate, protection condition (P_A) | CONFIRMED WITH REPAIR (F3: the t-range) |
| §8 discontinuity example | CONFIRMED |
| §10 axiom table | CONFIRMED, except the (S) row (see §3 below) |

**Bottom line**
- The consistency mathematics is sound. That covers the guards, the record rule, Prop. 1, Theorem 2, Lemma 3, the co-designed defenders, Lemma 4, (LA) and direct (C).
- The new problem is extendability, not consistency. For the "strongest self-contained version" (target-reference base, the three co-designed defenders, two-sided exposure), the open question of §0 and §13 is settled **negatively**:
  - In every extension satisfying (G) and (TC), T has no defence against its own defender C₃ (F1). So no extension satisfies (S) with T selected.
  - If the extension also keeps T undominated and has no distinct all-world ties, no extension satisfies (S) at all.
  - The only loophole left is the one the note already names: T could be an unselected all-world tie of some other selected model.

---

## 1. Line-by-line verdicts

### §1–§2. Guards and V_i: CONFIRMED

**Guards.**
- Take δ = min_{m∈M,k} m_k and the gamble γ_k = L·e_k − (1 − e_k). Then m·γ_k = (L+1)m_k − 1 ≥ (L+1)δ − 1, which is positive iff δL − (1−δ) > 0.
- γ_k has the minority sign at world k, and T accepts it strictly. A small compact cone around γ_k keeps this uniformly. The three guards lie in different sign classes, so they are disjoint.
- `geom.py` checks this exactly at L = 5, aperture 1/50, ε = 3/10.
- *Certificate base.* The guards must also avoid the four certificate cones, which lie in class 1. G₁ near (L,−1,−1) with L large lies far from them. So the condition "whenever U leaves the required sets available" is met.

**V_i.**
- On G_i we have e_i·γ_i = L > 0, which is the minority answer.
- On G_k (k ≠ i) we have e_i·γ_k = −1 < 0, which is the majority answer.
- These signs are uniform on compact neighbourhoods, so a neighbourhood V_i of e_i works.
- Because D_K's acceptance is a minimum over the compact set K, every D_K with K ⊂ V_i has the guard pattern **at every problem** of the guards, not just almost everywhere.
- This matters for item 1 of the brief: no installed record can miss a non-null part of a guard (see §2 below).

### §3. Extension rule and restatement: CONFIRMED

Take C = D_K with K ⊂ V_i and X ∈ X_G. Then D = {C ≠ X} has the following properties:
- it misses G_i (both C and T give the minority answer there);
- it contains G_k for k ≠ i up to a null set, with old side majority and new side minority (X = T there);
- (E_T) says that the new side differs from T on a non-null part of D.

The converse construction (X := b on D, D_K off D) gives X ∈ X_G and rec(D_K, X) = d. So the record-level reformulation is exact, and only the record is inspected.

**Clarification R0.** Read the starting hypothesis world by world: "every comparison accepted at world w that is not a pointwise weak worsening *at w* has D ⊂ U". This is the property the mixed-triangle step uses. All three bases satisfy it.

### Prop. 1: CONFIRMED

- *Silence is impossible for all three defenders at once.* At a coordinate i where |g_i| is maximal, every m ∈ K_i has m_i > ½. Then |m·g − m_i g_i| ≤ (1 − m_i)|g_i| < m_i|g_i|, so m·g has the strict sign of g_i.
- *Acceptance by all three implies acceptance by T.* M ⊂ {m_j ≥ η} = conv{v₁, v₂, v₃}, so if v_i·g > 0 for each i, then m·g > 0 for every m ∈ M.
- *Pigeonhole.* On {X ≠ T}, property (A) forces some C_i ≠ X. So some i satisfies (E_T).
- *Small gap.* v_{i,i} = 1 − 2η > ½ needs η < ¼. This is covered by "η sufficiently small".
- *Checks.* `geom.py` verifies (A) exactly on 1,097 random problems where the three posterior defenders agree. `run_cells.out` reports "rivals with no qualifying defender: 0".

### Theorem 2: CONFIRMED, with the brief's special point 1 answered in §2 below

- **(IB).** Installed sets are unions of whole record classes.
- **(G), weak half.** It is inherited from R⁰.
- **(G), strict half.** On G_k (k ∉ {i, w}, or k ≠ i when w = i), every copy of a new record goes from majority (rank 0 at w) to minority (rank 2 at w). So no copy is a pointwise improvement at w.
- **No composition.** G_k ⊂ D₁ ∩ D₂ up to a null set, for k ∉ {i, j}. The middle model would have to be minority (new side of d₁) and majority (old side of d₂) on a non-null set.
- **No mixed triangle.** Around any accepted cycle the rank change at each problem sums to zero. On G_k, the new link contributes +2, old non-guidance links contribute 0 (D ⊂ U), and guidance links contribute ≥ 0.
- **Strictness.** The reverse of a new record is not guidance, because it improves on G_k at every w. It is not an old record, because its D meets the guards. It is not a new record, by noncomposition.
- **Protection of T and of defenders.** The new side equals T on all of D only when (E_T) fails, so no new link ends at T. The new side is minority on some G_k where a V_j-defender is majority, so no new link ends at a defender. Domination needs incoming links, and adding comparisons can only remove strictness.
- **Direct (C).** New links are strict, so all-world ties are those of R⁰.

All of these steps are correct. The exhaustive cell check reports, at every world, for both bases and both filters, for the full collection and for one defender per rival:
- 0 (TC) violations, 0 strict-(G) violations, 0 weak-(G) misses;
- 0 distinct ties;
- 0 accepted reverses of new links;
- T and every defender undominated.

### Lemma 3 (target-reference base): CONFIRMED

- At a problem in the worsening set of a target-reference record, the rank at world i stays strictly above r_i(T). Guidance links only raise it, and another target-reference link needs the advice to be T there.
- "Nontrivial cycle" includes 2-cycles. So the base has **no distinct ties even at a single world**. The proof gives this, although the note does not say it.
- T undominated: an incoming target-reference link to T would need old = T on D = {Y ≠ T}. So all incoming links are guidance, and the weighted rank identity (weights 2/1/1) excludes them.
- Defence of T: for X ∈ X_G, D ⊂ U, and some world worsens on a non-null set.
- Checks: `cycles_any_subcollection.out` (no 2- or 3-cycles in the base) and `run_cells.out` ("X_G rivals against which T has no defence: 0").

### §11 co-designed defenders: CONFIRMED

- **K_i ⊂ V_i and m_i > ½ for large a.** Checked exactly at a = 20 for all vertices and all guard generators.
- **M ⊂ conv{v_i} with v_i = (a,1,1)/(a+2) ∈ K_i.** Exact. This is the image of u ∈ M.
- **C_i ≤_i T pointwise.** Scaling g_i by a > 1 raises both lower and upper previsions when g_i > 0, and lowers both when g_i < 0. So acceptance of the i-correct side is kept, and acceptance of the i-wrong side can only be lost. Checked on 11,727 exact samples.
- **Undominated under the target-reference base.** Correct as written.

**Referee's addition (PROVED; `tr_forces_codesign.out`, 81/81).** Under the target-reference base, an i-defender C is undominated **iff** C ≤_j T pointwise off the guards at some world j.
- *(⇒)* Otherwise the splice Y := C on W, T off W is target-reference-below C at every world, and strictly so. So Y dominates C.
- *(⇐)* This is the note's own argument.
- When V_i ⊂ {m_j < λ·m_i} for small λ (posteriors with large a), C is strictly worse than T at every j ≠ i on an off-guard open set. That set is the class-j problems e_j − λ′e_i − μe_k, which T accepts and C rejects. So j = i is forced.
- *Consequence.* For concentrated defenders the co-design property is not optional: **every usable defender is a strict pointwise world-i improvement of T**. This feeds F1.

### §11 non-additivity: CONFIRMED

- T ⪯_i X_n is target-reference-accepted: X_n adds step 1 on A_n and removes step 2 on B. The comparison is strict, since the reverse has old side ≠ T and is mixed at i.
- Endorsement would need ν(step 1, A_n) ≥ ν(step 2, B) > 0. Summing over N disjoint sets bounds N·ν(step 2, B) by the finite total mass.
- Only finite additivity is used, so finite finitely additive charges are excluded as well. The caveat about unbounded and non-Archimedean representations is correct.
- `geom.py` exhibits A-type and B-type problems outside the guards.
- Note: the obstruction arises because target-reference records are vetoes (one non-null worsening suffices). It is genuine, but cheap.

### §12 trap: CONFIRMED. (E_C) as a safeguard: WRONG

- **The trap.** The record d = rec(I₃, X) is exposed. Its old side matches Y on D = G₁ ∪ G₂ ∪ E. The copy Y → Z gives Z = T plus silence on E, which strictly improves T at worlds 1 and 2. World 3 is refused by strict (G). In any (G) + (TC) extension, T ⪯_w Y fails at every w. The KKM consequence and the tie loophole are stated correctly.
- **(E_C).** "(E_C) fails iff the old side equals T on D ∖ W" is exact. So (E_C) excludes exactly the records that compose *at T itself* with a W-only target comparison. CONFIRMED as stated.
- **As a safeguard: WRONG** (see F2). With (IB), the obstruction reappears through copies of rec(T, Y) in other contexts. The same Y stays permanently undefendable under the filtered rule.

### Lemma 4: CONFIRMED

- If (E_C) fails for i, then X = C_i a.e. on {T silent, C_i definite} ∖ W.
- On a neighbourhood of e_i − e_j, T is silent, C_i accepts and C_j rejects, provided a > 1 + ε/c. So that neighbourhood witnesses both conditions for j.
- Checked exactly for all six ordered pairs at a = 20 > 16/7.

### §13: the failure of (S) is CONFIRMED; the "open" framing is WRONG for the strongest version

- **The failure.** At world 3 Y strictly improves T, so guidance refuses T ⪯₃ Y. At worlds 1 and 2 guidance is mixed. Target-reference records live off the guards. New records start from majority advice on two guards. The KKM argument with no distinct ties is correct.
- **The framing.** See F1 and F2.

### §6 local freedom: CONFIRMED

- G_k lies in T's strict-acceptance cone and −G_k in its strict-rejection cone. Both are compact and avoid ∂T ∖ {0}.
- Any R with R △ T ⊂ N leaves both g and −g unchanged on the guards. So R ∈ X_G.

### §8: CONFIRMED

- rec(I_i, T) has an empty exposure set.
- At w ≠ i it is mixed on G_w and G_k.
- At w = i it is accepted by guidance; the note leaves this implicit.

### §7: CONFIRMED WITH REPAIR (F3)

- The base is the four certificate records with their copies, plus guidance. Optionally the reversed records are included at worlds 2 and 3; the counting works under either reading.
- The 3-positive/1-negative counting rules out 2- and 3-cycles.
- The weighted-identity argument rules out domination of regular models.
- (P_A) protects the extra sources.
- The t-range must be corrected (F3).

---

## 2. Special point 1: does "no composition" cover every realizable 3-chain? Yes

- **Null sets.** K ⊂ V_i is compact and the guard signs are uniform. So D_K has the guard pattern at **every** problem of G_k. X ∈ X_G equals T on G_k up to a null set N. Hence every installed record satisfies G_k ∖ N ⊂ D, and its old/new labels on G_k ∖ N are majority/minority. The record-based restatement imposes the same thing. So no qualifying record has a D that misses a non-null part of G_k, and every argument uses only μ(G_k ∩ D₁ ∩ D₂) > 0.
- **Every accepted 3-cycle at a world w** contains 0, 1, 2 or 3 new links. Any two edges of a directed triangle are consecutive.
  - Two or three new links: noncomposition (it covers i = j, including a record composed with itself).
  - One new link: the rank sum on G_k. This covers **mixed chains of one repair, one target-reference copy and one guidance link**, because target-reference copies have D ⊂ complement of W and contribute 0 on G_k.
  - Zero new links: a (TC) instance of R⁰.
  - Degenerate triples (A = B, etc.) cannot violate (TC).
- **Any subcollection.** The proof shows a *monotone* property: no accepted 2- or 3-cycle passes through a new link. This passes to every subcollection, and old triples satisfy (TC) in R⁰.
  - CHECKED exhaustively on the full collections for guidance and target-reference bases, with the three co-designed defenders and with three extra generic defenders that are not ≤_i T: 0 cycles through new links at every world (`cycles_any_subcollection.out`).
- **Contradictions and incoherent middles** are covered, since all advice labels are distinct and single-valued.

## 3. Special point 2: is the axiom table accurate?

| Row | Verdict |
|---|---|
| Reflexivity; both halves of (G); (IB); (TC) for arbitrary measurable models | CONFIRMED |
| Target undominated; chosen coherent defenders undominated | CONFIRMED (guidance and certificate bases; target-reference base with co-designed defenders) |
| **(LA)** | **CONFIRMED.** (LA) is C_L ≠ ∅, and T is coherent and undominated in R⁺ |
| **Direct (C)** | **CONFIRMED, in a stronger form than claimed** (see below) |
| Every distinct guard-preserving rival strictly dominated at every world | CONFIRMED (C ⪯_w X at all w, and the reverse is refused at all w) |
| (LF) neighbourhood included | CONFIRMED |
| (S), defence clause | CONFIRMED that the current relation fails |
| (S), "further extension open" | CONFIRMED WITH REPAIR for the guidance and certificate bases with the uniform triple (still open). **WRONG** if read as covering the strongest version of §§11–12 (F1) |
| (S) fixed-rival sections; full coverage | CONFIRMED (not established) |

**Direct (C) in detail.** There are no distinct ties even at a **single** world, for incoherent and contradictory models included:
- guidance ties are identities, since distinct advice has distinct ranks;
- the target-reference base has no 2-cycles (Lemma 3);
- the certificate base has no 2-cycles (counting);
- new links are strict.

So X ≈ C forces X = C, and direct (C) holds. `run_cells.out` reports "distinct ties 0" for all 4096 models in every configuration.

---

## 4. New findings

### F1 (PROVED; CHECKED in cells): the strongest version cannot be extended to (S) with T selected

**Setting.** Target-reference base, defenders C₁, C₂, C₃ = D_{Φ_{s_i}(T)} with a large, any filter, and **any** subcollection that covers X_G ∖ {T}.

**Step 1: a rival whose only defender is C₃.**
- Let E ⊂ M₃ ∖ W be a non-null open set on which T gives the minority-3 answer and C₁, C₂ are silent. Example: a neighbourhood of (−θ/a, −θ/a, 1), checked exactly at ε = 3/10, a = 20, θ ∈ {3/4, 1, 3/2}. C₃ also accepts there.
- Let X* := T except silence on E. Then X* ∈ X_G.
- (E_T) fails for C₁ and C₂, because X* differs from T only on E and C₁ = C₂ = X* there.
- C₃ satisfies (E_T) on E. It satisfies (E_C) on F = {T silent, C₃ majority} ∖ W, which is non-null; `geom.py` exhibits points in classes 1 and 2.
- So **every covering subcollection installs d* = rec(C₃, X*) at every world**.

**Step 2: T cannot be defended against C₃.** In any relation containing d* and satisfying (G) and (TC):
- *w = 1, 2:* T ⪯_w C₃ ⪯_w X*, and X* strictly improves T at w (silence beats the wrong minority-3 answer on E). Strict (G) gives X* ≺_w T, so (TC) forbids T ⪯_w C₃.
- *w = 3:* C₃ ≤₃ T pointwise and C₃ ≠ T, so strict (G) refuses T ⪯₃ C₃.

**Consequence.** T is non-competitive against C₃ in every (G) + (TC) extension, so it can never be selected. By the note's own KKM argument, no extension that keeps T undominated and has no distinct all-world ties satisfies (S).

**Check.** `run_cells.out`, "Forced trap": the unique qualifying defender is C₃, and adding T ⪯_w C₃ creates forced (TC) violations or strict-(G) violations at every world, both for "install all" and for "one defender per rival".

**Mechanism.** By Lemma R1, every concentrated defender that is undominated under the target-reference base is a strict world-i improvement of T. Using it against a rival that strictly improves T at the other two worlds kills T's last defences against that defender. A three-element defender pool lets the rival force this.

### F2 (PROVED; CHECKED in cells): (E_C) does not protect T's defence against §13's Y

Under the entire filtered collection (C₃ or I₃ available), §13's Y = T + majority on G₁ ∪ G₂ can never be defended.

**The record.**
- Let F₁ ⊂ M₁ ∖ W be non-null with T silent and C₃ majority. Put X₁ := C₃ except T on G₁ ∪ G₂ and the minority answer on F₁.
- Then X₁ ∈ X_G, and F₁ witnesses both (E_T) and (E_C). So d₁ = rec(C₃, X₁) = (G₁ ∪ G₂ ∪ F₁, majority, minority) is installed.

**The chain at world 1.**
- A := T + majority on F₁;
- B := A + majority on G₁ ∪ G₂;
- C := T + minority on F₁.
- A ⪯₁ B is an (IB) copy of rec(T, Y), and B ⪯₁ C is a copy of d₁.
- C strictly improves A at world 1 (F₁ moves from majority to minority, rank 2 → 0). So (TC) forbids T ⪯₁ Y.

**The other worlds.** World 2 is the same with F₂ ⊂ M₂. World 3 is refused by strict (G).

**Check.** `witness_s12.out` prints exactly these chains under both bases.

**Conclusion.** The direct-composition test at T is not the right filter: (IB) copies in other contexts reproduce the trap. An exact record-level test is available. A record d = (D, a, b) at w blocks T ⪯_w Y iff, with D₀ = {T ≠ Y}:
- a = Y on D ∩ D₀;
- Y ≤_w T on D₀ ∖ D;
- b ≤_w T on D ∩ D₀;
- b ≤_w a on D ∖ D₀;
- strict on a non-null set;
- and the symmetric condition holds for the other order.

### F3: the §7 t-range (CONFIRMED WITH REPAIR)

- "Choose r·p_j/p_k < t < r" does not make the source silent in general. Silence also needs t < p_j/(r·p_k), which is binding when p_j/p_k < r².
- For p₃ = (5278, 5761, 34)/11073 with i = 1 or 2: at t = r − 1/1000 the source accepts −g, i.e. gives the majority answer (`geom.out`).
- **Repair.** Take t ∈ (r·p_j/p_k, min(r, p_j/(r·p_k))). This interval is non-empty, since r < 1.
- (P_A) needs only "source ≠ T", so it survived anyway.
- For (p₃, i = 3) the patch range contains the x-coordinate of PP13's cone B₃ (0.4028). So δ must be below B₃'s |g₃| ≈ 1.0·10⁻³. "Take δ small" suffices.

---

## 5. Nearby reachable target (proposal, unproved)

**What survives.** Theorem 2, Lemma 3, Lemma 4, (LA), direct (C) and the infinite non-additivity.

**What fails.** Extendability of the strongest version, through F1 and F2.

**A nearby target that avoids both:**
1. **Variable defender pool.** Use co-designed defenders Φ_s(T), with s large in one coordinate, chosen after seeing the rival. §3 already permits this.
   - For X* of F1, a more concentrated 1-defender (a′ ≫ a) gives the majority answer on E. So it is exposed and avoids C₃.
2. **Reserved worlds.** Give each installed defender C (label i, strict world-i improvement of T by Lemma R1) a reserved world ρ(C) ≠ i. Install C only against rivals that do not strictly improve T at ρ(C). Rivals that improve T at two worlds must then take a defender labelled by one of those two worlds.
3. **Copy filter.** Replace (E_C) by F2's exact record-level test against the comparisons T ⪯_{ρ(C)} C that are to be added later. Then verify (TC) for the enlarged relation. The guard argument does not cover links T ⪯_w C, because their D meets the guards with T's minority advice as the old side.

Whether such an allocation covers X_G and keeps (TC) is the concrete next question. It replaces the note's "further extendability" question for the strongest version.

---

## 6. Scripts

| script → output | content | label |
|---|---|---|
| `geom.py` → `geom.out` | guards, V_i and K_i containment, η < c, property (A), C_i ≤_i T, Lemma 4 patches, F1 regions E and F, §11 sets, §7 t-ranges (F3) | CHECKED (exact) |
| `run_cells.py` → `run_cells.out` | Thm 2 / Lemma 3 axioms on all 4096 models, both bases, both filters, all records or one per rival; F1 forced trap; §12 trap with and without the filter | CHECKED (exhaustive on cells) |
| `cycles_any_subcollection.py` → `.out` | no 2- or 3-cycle through a new link (monotone, hence every subcollection); base cycles | CHECKED |
| `witness_s12.py` → `.out` | F2 chains through (IB) copies | CHECKED |
| `tr_forces_codesign.py` → `.out` | Lemma R1: undominated under the target-reference base iff ≤_j T off the guards at some world j (81/81; the naive "≤_i T everywhere" form fails, 43/81) | CHECKED |

The cell abstraction treats cells as atoms. It certifies the combinatorics of the record rules exactly, but not the measure-theoretic statements. Those statements are proved above, and their geometric inputs are checked in `geom.py`.
