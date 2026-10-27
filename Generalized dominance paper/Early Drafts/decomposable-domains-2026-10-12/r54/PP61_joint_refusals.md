# PP61. Joint refusals: the exact instance, the countable closure theorem, and the adaptive game

23 October 2026. Task PP61 (Solver) of Brief 54. One author; not refereed. It takes in the coordinator's relay of REFEREE_round53 (§3.3, §6) and reads PP63 §2–4 (adversary) for consistency only.

**Labels.**
- PROVED: the argument is complete here.
- CHECKED: an exact rational computation in `r9/PP61_py/`; every script re-verifies its witnesses.
- NUMERICS: none is used. Floating-point LP solutions are only *candidates*; every q or α reported has been re-verified in exact rational arithmetic.
- CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF54 and its four binding audits; PP56 §1–5; PP57 §4; PP59 (ledger); REFEREE_round53 §3.3, §5–7; code in PP56_py and PP57_py (reused: PP50's exact arrangement enumerator, PP56's balanced field u¹). No axiom is added. Extra hypotheses are named where they enter, and are always marked as *pattern hypotheses*, never as axioms.

---

## 0. Verdict

1. **Theorem C (countable closure; PROVED).** For any countable set of (source, fixed rival) pairs in N, a comeagre set of common weights q makes the reweighted relation Λ_q satisfy every non-section axiom on all of N and have locally constant verdicts at every listed pair. So all section conditions there hold, including every cofinite restriction on approximants (REFEREE §3.3 SR(c)), once the approximants are listed too.
   - **No finite or countable exact instance can be (R),** and the adaptive game with revisable worlds is (OK) at every countable stage.
   - An axiom-level section obstruction must choose its rival or point *depending on the relation*, as Theorem Q and PP56 Prop 5.1 do.
   - This replaces PP55 SR(c), which the referee left unproved, by a proved and stronger statement.
   - **Cor C.5:** no finite hierarchical (multi-level, branch-menu) propositional instance is UNSAT either. So the coordinator's two-level run is SAT for every finite encoding, and any obstruction must be quantitative.
2. **Exact instance (CHECKED).** G3 = {u, B, D} in the 2-D neighbourhood N = conv{B, D, B′, D′}, with (2V) PROVED on N.
   - Exact cells, and atoms that are actual radial slabs.
   - Nine pure-shift germs with exact wedges, and oriented-matroid stability PROVED for t ∈ (0, 10⁻⁵].
   - 198 overlapping, balanced and non-conic swaps with all copies, plus 156 pads: 532,873 records with exact (IB).
   - Clauses G, DEF, UND, C, SEC, and (TC) on every ordered triple.
   - **Encoder validation:** three generic Λ_w satisfy every clause; unit-mass Λ violates exactly 193 SEC clauses, all on balanced swaps (Theorem Q reproduced).
3. **Adaptive game (CHECKED, 5 adversary moves, each an exactly q_n-balanced overlapping swap).**
   - Revisable worlds: **(OK) at every step.** A generic perturbation of relative size ≤ 10⁻³ restores every section clause, and q does not concentrate.
   - Frozen promises (541–571 earlier refusals fixed): straddling assignments are (OK). Same-world and {2, 3}-internal assignments are **(W¬R)**: exact α = (1, 1) on the new inverse pair only, and the relations are SAT.
   - **No (R) outcome anywhere.** No cyclic certificate arose.
4. **α-certificates (exact; by Prop A″ obstructions for every reweighted relation).**
   - (1, 2) on one record refused at worlds 1 and 3;
   - (1, 1) on inverse pairs at the same world, or straddling-violating;
   - (1, ½) on **two different overlapping swaps**, an inconsistent mass order with no inverse pair.
5. **One explicit allocation (E2; CHECKED; CANDIDATE).** All 24 balanced swaps are incomparable at world 3, with patterns R(r)/R(r⁻) ∈ {13/23, 23/13, 23/23}.
   - Their refusals persist along all three pure-shift rays at both ends.
   - Defence, protection and (TC) hold on the whole instance.
   - No common q certifies it.

   This is the brief's target shape on a finite 2-D instance.
6. **PP62 Cor E.2 run (coordinator's priority; CHECKED).** The configuration is u, B, six pure shifts at two scales, a balanced X, all Lemma S splits and all copies.
   - **SAT with axioms only.** The model is R₀ with w₀ = 3 plus exactly one u¹-unfavourable acceptance per e₃-germ, at world 2.
   - Adding u¹-endorsement at the shifted members gives **UNSAT with a 13-clause core**: C, 3 DEF, 3 SEC and 6 endorsement units. That is Theorem E, and the only non-axiom clauses are the endorsement units.
   - **No axiom-level obstruction.**

---

## 1. The exact instance

### 1.1 Sources, the neighbourhood, (2V)

- **N** := conv{B, D, B′, D′} with B′ = 2u − B, D′ = 2u − D. It is a compact, genuinely two-dimensional neighbourhood of u (u is its centre).
- **(2V) on N (PROVED).** Every coordinate of every a ∈ N lies in [373, 427]/1200. Then 1/a_i ≥ (1/427)·1200 and Σ_j 1/a_j ≤ 3·1200/373, so 1/a_i ≥ c Σ_j 1/a_j as soon as 373/427 ≥ 3c = 0.7, which holds (0.873). This says that (1/a)/Σ(1/a) ∈ M, i.e. u ∈ M_a. Hence every C_a with a ∈ N answers only with the sign of u·g, and on the disagreement region R(N) every member says the common answer h(g) or S. CHECKED for the listed sources (`geom61.out`).
- **Source grids.** G3 = {u, B, D} (affinely spanning, so genuinely 2-D; u is a vertex of conv G3 but interior to N), and G5 = G3 ∪ {B′, D′} (u interior to conv G5). All relational runs use G3 (cost); the geometry, wedges and stability are CHECKED for both.
- **Cells.** One representative ray per open cell of the arrangement of all source planes and the coordinate planes, with u·g > 0; cells with equal (sign pattern, advice tuple) are merged into a *class*. G3: 31 classes, 18 with disagreement (exactly PP56's 18). G5: 55 and 42.

### 1.2 Atoms (actual positive-measure sets)

For each disagreement class K:
- **K.c1, K.c2**: two radial slabs (|g| ∈ [r₀, r₁), [r₁, r₂)) of a compact angular core of one geometric cell of K. Further radial splits K.c1a, K.c1b, … are made by the adversary in the game (atomlessness: any prescribed value of ∫ q|g| up to the parent's is realised by a radial slab).
- **K.r**: the rest of K; **K.n**: the antipodal class −K (the models are odd).

Every model in the instance is a value vector over atoms (P, M, S, C relative to the atom's ray). The u¹-increment of a record on an atom is |g| times an exact integer vector (PP56 `lex56.phi_cell`; on R the answer h and S are λ-indifferent with λ = (1, 1, 1)). Since q is free on each atom, only the products w_p = ∫_p q|g| matter for every weight question, and every positive vector w is realised by some q.

### 1.3 Pure-shift germs, exactly (PROVED + CHECKED)

For each source a ∈ G3 and world w put a_t = a∘(1 + t e_w), normalised. The shift wedge σ_t = {C_{a_t} ≠ C_a} is computed exactly as a union of cells of the refined arrangement (base planes + the three moving planes m_j∘a_t) at t* = 10⁻⁵, split by class and by C_{a_t}'s value: 20 σ-atoms per shift for G3 (28 for G5), including antipodes.

*Stability (PROVED; CHECKED, `geom61.out`).* The moving normals are affine in t. For every triple of normals containing a moving one, the 3×3 determinant is a polynomial in t of degree ≤ 3. For all 232 (G3) and 511 (G5) such polynomials that are not identically zero, after removing powers of t, there is no root in (0, t*] (exact Sturm count, sympy). So the oriented matroid, hence the cell structure and every advice value, is the same for every t ∈ (0, t*]. Every compact angular core is disjoint from σ_t for small t, so the core slabs never meet a wedge.

*Lemma 4.1 of PP57, re-checked:* on every σ-atom, C_{a_t} is strictly better at w than C_a (all 9 + 15 shifts).

### 1.4 Models

G3 instance (`run61a_G3.out`): 357 base models.
- 3 sources (coherent, selected).
- 198 swaps X = C_a[F ↦ C_b], every one used in both orders, so the common-context copy Y = C_b[F ↦ C_a] of each swap is present. F ranges over (build61.py):
  - single core slabs (72; guidance-decided);
  - **balanced** pairs {K.c1, K′.c1} with vec(K) = −vec(K′) (24; zero u¹-value at all three worlds at unit masses);
  - **overlapping** variants {K.c1, K′.c2}, {K.c2, K′.c1}, {K.c1, K.c2, K′.c1}, {K.c1, K′.c1, K′.c2} (96);
  - the big union of all c1 slabs of a pair (6).

  All F are bounded and non-conic, so every swap is incoherent (coherent models agreeing off a bounded set agree a.e.).
- 156 guidance pads: C_a[K.c1 ↦ w-correct] on silent slabs, and pads inside balanced swaps (PP30 / Prop K auxiliaries: N[G → S, E → w-correct] in the PP59 sense).
- In each of the nine shift sub-instances: the shifted source C_{a_t} (selected), X_t = C_{a_t}[F ↦ C_b] for each swap out of a, and P = C_b[F ↦ C_a, σ_t ↦ C_{a_t}]. That is 137 new models per shift.

  **No identification of shifted records is ever assumed.** Every record is computed literally as a set with its two restrictions. P's record against C_b equals rec(C_{a_t} → X) only when σ_t ∩ {C_a ≠ C_b} is null. PP63 Prop 2.1–2.2 shows that this fails for every pure shift of the kink triple, and the brief's suggested identification is false in general. In our instance P is therefore just one more incoherent model with its own (correct) record and obligations.

Mixed triangles are therefore present in all three forms the brief asks for. Examples:
- (C_u, C_u[F₁ ↦ C_B], C_u[F₂ ↦ C_D]) with F₁ ∩ F₂ ≠ ∅: two swaps out of one source, overlapping;
- (C_u, X, C_D): a swap plus another selected source;
- (C_u, X, PAD): a swap plus a guidance link.

### 1.5 Records, variables, clauses

A record is the literal set {X ≠ Y} with the two restrictions (sub-atoms are merged back into their parent whenever the pair agrees on all of them). So equal records are identified exactly ((IB)), across the base instance and all shift sub-instances. G3: 532,873 records, 1,598,619 variables [r accepted at i].

Clauses, all from the axioms (`inst61.Encoding`):
- **G**: strict guidance units;
- **DEF**: ⋁_i [S ⪯_i X] for every selected S (sources and shifted sources) and every other model;
- **UND**: undominatedness against coherent rivals;
- **C**: direct (C) against incoherent rivals;
- **TC**: (TC) on *every* ordered triple of every (sub-)instance at every world. These are generated lazily, and every final assignment is re-checked on all triples by a matrix test (`tc_check_full`);
- **SEC**: [C_{a_t} ⪯_i X] ⟹ [C_a ⪯_i X], for every *fixed* base rival X (never one containing σ-atoms), every shift and every world.

*Soundness of SEC and of the shifted literals (PROVED).* Fix one shift. For each t ∈ (0, t*] the sub-instance I(t) is an actual finite instance with the same combinatorics (§1.3), so it satisfies every axiom clause. Its verdict vector takes finitely many values, so some sequence t_k → 0 has a constant verdict vector. Along that actual sequence, with the rival fixed, a closed section gives SEC. So a shifted literal in a model of the clause set means "this verdict holds along an actual sequence t_k → 0". This implies the brief's germ literal ("frequently accepted"), and all per-t clauses (defence of C_{a_t}, (C) for the copies P, (TC) through C_{a_t}) hold for it. PP63 §4.4 gives an alternative justification ("choose t* after the base rivals") and confirms the clauses are sound.

*What is not represented (coordinator item 4).* REFEREE_round53 §3.3 SR(c): a closed section can force *cofinite* restrictions on approximants, e.g. "[C_{a_k} ⪯₂ X] ∨ [C_{a_k} ⪯₃ X] for all but finitely many k". The encoding sees only one subsequence per shift and only pure-shift directions. Such cofinite restrictions would enter as additional clauses on further shifted literals: one copy per approximant, per direction, per fixed rival. **Theorem C below shows that adding all of them, for any countable family of base points and rivals, can never produce unsatisfiability.**

---

## 2. Validation of the encoder (CHECKED, `run61a_G3*.out`)

1. **Generic additive relations satisfy everything.** For three random integer weight vectors w (∈ [10⁶, 10⁹] per atom), the relation Λ_w satisfies all 62,079 clauses and (TC) on every ordered triple of every sub-instance: 0 violations. Λ_w is PP56's relation with field q·u¹, where w_p = ∫_p q|g|, σ-atoms carry mass ε → 0, and the localisations are the atoms first.
2. **Theorem Q reproduced.** With unit masses (every balanced swap exactly u¹-balanced), Λ₁ violates exactly 193 clauses, **all of kind SEC**, and every one is on a balanced swap. For example, SEC at the shift (B, e₁) for the rival B[K09.c1 ∪ K11.c1 ↦ D] at world 1. No G, DEF, UND, C or TC clause fails, as Theorem L predicts.

This is the solver's consistency check. Any clause that is not an axiom consequence would be violated by some Λ_w, by Theorem L.

---

## 3. The countable closure theorem

**Theorem C (PROVED).** Assume (2V) on the compact neighbourhood N. Let Γ be any countable set of pairs (a, X), with a ∈ N and X a measurable rival. Then there is a bounded q ≥ 1 such that the reweighted relation Λ_q:
- satisfies every non-section axiom (reflexivity, strict (G), (IB), (TC), defence, undominatedness, direct (C), (LA)) for every member of N against every measurable rival; and
- for every (a, X) ∈ Γ and every world i, has a verdict [C_{a′} ⪯_i X] that is constant for a′ in a neighbourhood of a.

In particular, every fixed-rival section condition at every (a, X) ∈ Γ holds, along every sequence a_k → a. Moreover, the set of such q is comeagre in Q := {q ∈ L^∞ : 1 ≤ q ≤ 2}.

*Proof.*
1. Λ_q satisfies all non-section axioms on N for every q ∈ Q (AUDIT_robust_refusals §1; REFEREE_round53 §5, which checks each Theorem L step for q·u¹ with q common to all worlds).
2. For (a, X) ∈ Γ and world i, put d = u¹_i(X) − u¹_i(C_a) ∈ L¹ and f(a′) := ∫ q[u¹_i(X) − u¹_i(C_{a′})]. This is continuous in a′ (REFEREE_round53 §5). If ∫ q d ≠ 0, then f has a constant sign near a, and Λ_q's verdict, which is decided at level 0, is constant near a.
3. If X = C_a a.e., the verdict at a is acceptance by reflexivity, and the section condition at a holds trivially. Otherwise d ≠ 0 on a non-null set.
4. Let Z := {q ∈ Q : ∫ q d = 0}. It is closed in the complete metric space Q, since q ↦ ∫ q d is L^∞-continuous.
5. Z has empty interior. Given q ∈ Z and 0 < δ < ½, pick a non-null E on which d has one sign and q lies on one side of 3/2. Then q ± δ1_E ∈ Q, it is within δ of q, and ∫(q ± δ1_E)d = ±δ∫_E d ≠ 0.
6. Γ × {1, 2, 3} is countable. By Baire's theorem, the complement of the union of the sets Z is comeagre, hence non-empty. ∎

**Corollaries (PROVED).**
1. **No countable section certificate.** No proof of impossibility can use closed sections only at a countable set of (point, rival) pairs fixed independently of the relation. This holds even with all their cofinite consequences at countably many approximants (put the approximants into Γ), and with all non-section axioms everywhere. This is the corrected and strengthened form of PP55 Prop SR(c), which REFEREE_round53 §3.3 left unproved: sections *can* couple, but never into a contradiction on a countable carrier.
2. **Finite exact instances are never (R).** Every instance of §1 (any finite number of sources, shifts and fixed rivals) is satisfied by Λ_w for all w outside finitely many hyperplanes. §2 item 1 checks this directly.
3. **The adaptive game with revisable worlds never fails at a countable stage.** Each adversary move adds countably many pairs. The current q can be perturbed by an arbitrarily small amount, keeping every earlier strict refusal (an open condition), and diagonally even at the limit of a countable sequence of moves. **No concentration of q is needed.** Theorem Q is uncountable in nature: for each fixed q it picks the rival *after* q.
4. **Where an obstruction must live.** Any axiom-level obstruction on N must choose its point or rival in dependence on the relation (the audit's "for every rule there exists a rival", AUDIT_robust_refusals §2), over an uncountable family. Prop 5.1 of PP56 and Theorem Q are of exactly this form.

**Corollary C.5 (no finite propositional certificate at any depth; PROVED).** This answers the coordinator's two-level request.

*Setting.* Consider any instance of PP63 Prop 4.4's hierarchical kind:
- finitely many levels;
- at each level a finite menu of rivals, which may include, for every possible verdict pattern of earlier levels, the rival an adversary would pick in that branch;
- level-k rivals built from shift layers at scales t₁ ≫ … ≫ t_k;
- stable combinatorics, so that the propositional formula Φ (record identities, guidance, DEF/UND/C, (TC), SEC) does not depend on the numerical scales.

*Claim.* Φ is satisfiable.

*Proof.*
1. Fix in advance a sequence of scale tuples whose levels tend to 0 in hierarchical order.
2. Let Γ be the countable set of all (member, rival) pairs over all branches and all tuples, the shifted members included. Choose q generic for Γ by Theorem C.
3. Λ_q's verdict is locally constant at every pair in Γ. Pick the first-level scale from the sequence small enough that the shifted members lie in the neighbourhoods at level 0. Then pick the second-level scale small enough for the neighbourhoods at the chosen first-level members, and so on.
4. At these scales, Λ_q satisfies every clause of the actual instance. That instance has the same formula Φ.

Masses never enter Φ. So "a swap balanced for the allocation's own weighting" has no propositional content: the adversary's branch-dependent choice is just one more menu entry. ∎

*Consequence.* The requested two-level run (the rival balanced after the first-level verdicts) is SAT by Corollary C.5 for every finite encoding, so I did not spend machine time on it. This sharpens PP63 Cor 4.5 from "one level is never enough" to "**no finite number of levels is enough**". A section obstruction, if one exists, must be quantitative. It has to compare relation-chosen refusal radii with masses (PP63 Remark 4.3), or use a rival family depending continuously on the relation (Theorem Q, PP62 Theorem E, PP63 Prop 4.6). It cannot be a finite clause set over records.

*Remark (dimension count; CONJECTURE-level heuristic, not used).* For a fixed rival X, the balanced locus {a ∈ N : z_q(C_a → X) = 0 ∈ ℝ³} is cut out by three equations (two independent ones, since λ·z ≥ 0 is pointwise Bayes) in two parameters. So for a fixed rival it is generically a finite set or empty. Theorem Q needs rivals that move with q.

---

## 4. The weight test, read through Prop A″

REFEREE_round53 Prop A″: within the reweighted family Λ_q (any common q, any tie-break), an *open* refusal of C_a ⪯_w X exists iff ∫ q d < 0. So **every α-certificate below is an exact obstruction for the entire reweighted family**, not a failure of one partition or one search.

Here d_k is constant per |g| on each atom and vanishes off the atoms. So Gordan's alternative on atoms is the pointwise alternative itself: an α found on atoms satisfies Σ α_k d_k ≥ 0 a.e. (`lp61.py`, all witnesses exact).

**4.1 The kink sector is a mass-order problem (PROVED).** Every balanced swap in the instance has increments ±v per unit mass on its two parts, with v ∝ (−2, 1, 1) (world 1 distinguished). Write Q(E) := ∫_E q|g|. For such a record r = (F₊ ∪ F₋ : x → y), whose increment is +v on F₊ and −v on F₋:
- "r refused at 1" ⟺ Q(F₊) > Q(F₋) (up to orientation of v);
- "r refused at 2" ⟺ "r refused at 3" ⟺ Q(F₊) < Q(F₋).

So every q-certifiable allocation refuses each kink-type record exactly on {1} or exactly on {2, 3}, with r⁻ on the complement. Every refusal set outside {{1}, {2, 3}} carries an α-certificate of support ≤ 2:
- {1, 3}: α = (1, 2) on (1, 3);
- {1, 2}: α = (1, 2) on (1, 2);
- {2} with r⁻ refused at {3}: α = (1, 1).

A family of such orientations is q-feasible iff the strict inequalities between sums of atom weights it prescribes are consistent. **This makes it a mass-ordering problem.** An α-certificate is exactly a positive combination in which the atoms cancel. Two kinds occur:
- **(a) Inverse pairs.** r and r⁻ both refused at a world, or non-straddling: the audit's and referee's pattern.
- **(b) Overlapping swaps, with no inverse pair involved.** These are inconsistent mass orders, which can be cyclic.

**4.2 Exact certificates found (all re-verified in rationals).**

| id | prescribed refusals | α | kind |
|---|---|---|---|
| A1 | C_B refuses B[K09.c1 ∪ K11.c1 ↦ D] at worlds 1 and 3 (from the E2 allocation) | (1, 2) | single record, non-additive refusal set |
| A2 | u refuses r_n at 1 and r_n⁻ at 1 (game, every step) | (1, 1) | inverse pair, same world |
| A3 | u refuses r_n at 2 and r_n⁻ at 3 (game, every step) | (1, 1) | inverse pair, non-straddling |
| A4 | u refuses u[K10.c1 ∪ K17.c1 ∪ K17.c2 ↦ B] at 2, and u[K10.c1 ∪ K17.c2 ↦ B] at 1 | (1, ½) | **two different overlapping swaps** (E5a) |

A4 reads: Q(K10.c1) > Q(K17.c1) + Q(K17.c2) and Q(K17.c2) > Q(K10.c1). These cannot both hold, and α = (1, ½) makes the cancellation pointwise. It is the simplest instance of kind (b). A cyclic certificate with every pair feasible, as in REFEREE_round53 §6.1, needs four kink swaps P₁|Q₁, P₂|Q₁, P₂|Q₂, P₁|Q₂ with alternating orientations. Our families contain three of the four (no c2|c2′ pair), so no such cycle is realised in this instance. The game never produced one either (§5).

Whether the A4 orientations are *relationally* consistent was left undecided (§6, E3/E5). The weight side is exact.

---

## 5. The adaptive game (CHECKED, `run61c.out`)

**Set-up.** Sources G3 with all nine pure-shift germs. Swap families: singles for every pair, the bal2/ovl/big families of (u, B) and (u, D), and source pads. Weights w = ∫ q|g| per atom start at unit masses. The game swaps live on the kink cells Ep = K13 (Maj1, u answers alone) and Em = K20 (Min1, u answers alone), which are disagreement cells of both (u, B) and (u, D). So successive swaps toward B and toward D share pieces, and the triangles (C_u, C_u[F ↦ C_B], C_u[F′ ↦ C_D]) are in the instance.

At step n:
- The adversary takes an **existing** Ep slab P (overlap with earlier swaps) and carves a **new** radial sub-slab Q′ of an Em slab with ∫_{Q′} q_n|g| = ∫_P q_n|g|.
- He adds X_n = C_u[P ∪ Q′ ↦ C_b], with b alternating B, D, together with its copy.
- X_n is exactly q_n-balanced (CHECKED: its q_n-value is (0, 0, 0)). This is Theorem Q's rival for q_n.

All obligations are regenerated on the refined instance. The records are the same sets, so nothing is dropped.

**Outcomes (CHECKED, five adversary moves, `run61c.out`).**

| step | adversary swap | Λ_{q_n} on the new instance | V1 (worlds revisable) | V2 (all 541–571 earlier refusals frozen) |
|---|---|---|---|---|
| 0 | — (unit masses) | 73 SEC violations, all on u¹-balanced swaps | **(OK)** after a generic perturbation, max relative change 9.8·10⁻⁴ | — |
| 1 | u → B on K13.c1 ∪ K20.c1a | 4 SEC violations, all on X_n's copy | (OK), 1.0·10⁻³ | see below |
| 2 | u → D on K13.c1 ∪ K20.c2a | 4 SEC | (OK), 9.4·10⁻⁴ | see below |
| 3 | u → B on K13.c1a ∪ K20.c2a | 4 SEC | (OK), 9.8·10⁻⁴ | see below |
| 4 | u → D on K13.c1aa ∪ K20.c2a | 4 SEC | (OK), 9.9·10⁻⁴ | see below |
| 5 | u → B on K13.c1aa ∪ K20.c2aa | 4 SEC | (OK), 9.5·10⁻⁴ | see below |

V2 is identical at every step 1–5. Here i is the world refusing r_n = rec(C_u → X_n) and j the world refusing r_n⁻:

| (i, j) | weights (exact LP) | relations (exact SAT, with every frozen promise as a unit clause) | class |
|---|---|---|---|
| (1, 2), (2, 1) | q exists | SAT | (OK) |
| (1, 1) | α = (1, 1) on (r_n at 1, r_n⁻ at 1) | SAT | **(W¬R)** |
| (2, 2) | α = (1, 1) on (r_n at 2, r_n⁻ at 2) | SAT | **(W¬R)** |
| (2, 3) | α = (1, 1) on (r_n at 2, r_n⁻ at 3) | SAT | **(W¬R)** |

**Reading.**
1. **No (R) at any step.** Weights never fail when the worlds are revisable: an arbitrarily small perturbation (relative 10⁻³) restores every section clause, and q does not concentrate. These are Theorem C's corollaries 2–3, now CHECKED.
2. Weights fail exactly on the **non-straddling** assignments, as in REFEREE_round53's table: both refusals at one world, or both inside {2, 3}. Even with 541–571 promises frozen, every α-certificate found has support 2 and involves **only the new pair**. The frozen promises never enter a certificate, because they are strict at q_n and the new swap is balanced at q_n. In particular **no cyclic (non-pairwise) certificate arises in the game.** For the cycle mechanism see §4, E5.
3. **The relations always survive.** Every (W) outcome is (W¬R): single-world incomparability of the inverse pair (r_n, r_n⁻), at world 1 or at world 2, and the non-straddling (2, 3) pattern are all relationally consistent, with every earlier promise kept and every section clause at the nine germs.

### 5.1 The PP62 Cor E.2 configuration at u (coordinator's priority run; CHECKED, `run61d.out`)

**Instance.**
- Sources: u and B, plus the six pure shifts u∘(1 + s τ e_w) for w = 1, 2, 3 and τ ∈ {1, 1/10}, with s → 0. That is two scales per direction, and all of them are selected members.
- Rival: X = C_u[F ↦ C_B] with F = Ep.c1 ∪ Em.c1, each slab split radially into halves of equal mass, so that F and its two "cross" halves are u¹-balanced.
- Models (314 in all):
  - C_u[E ↦ C_B] and C_B[E ↦ C_u] for all 15 non-empty E ⊆ F. These are X, Y, every Lyapunov split of the base record, and every reverse and copy.
  - At each shifted member u_t: the splits Z = C_{u_t}[E′ ↦ X] of rec(C_{u_t}, X), for E′ = E ∪ (layer or half-layer or nothing), and the copy C_B[F ↦ C_u, layer ↦ C_{u_t}].
- The arrangement of u, B and all six shifted members is exact. Its oriented matroid is constant on (0, s*], s* = 10⁻⁵ (2,805 determinants, exact root counts), so the instance is the same for every small s.
- Clauses: G, DEF, UND/C; (TC) on every ordered triple (lazy, then a full re-check); SEC along s → 0 for every s-independent rival. **No endorsement assumed.**

**Results.**

| run | added hypothesis | outcome |
|---|---|---|
| V0 | none (axioms only) | **SAT**; exact re-check of every clause and of (TC) on all 314³ ordered triples at all worlds: 0 violations |
| V1 | u¹-endorsement of every acceptance on records supported in F | **SAT**, same re-check, 0 violations |
| V2 | V1 + u¹-endorsement of acceptances out of the shifted members against the 15 base swaps | **UNSAT**, minimal core of 13 clauses (below) |

**The V0/V1 model, i.e. the local shape of an interior rule (CHECKED).** It is R₀ with w₀ = 3, modified exactly on the germs of the e₃ direction:
- **Base record:** R(rec(C_u → X)) = R(rec(X → C_u)) = R(rec(C_B → Y)) = {3}. So there is incomparability at 3 and ties at 1 and 2. This is PP62's R₀ with w₀ = 3.
- **Germs.** Shifts toward e₁: refused at {2, 3}, accepted at 1 (u¹-favourable). Toward e₂: refused at {1, 3}, accepted at 2 (favourable). **Toward e₃: refused at {1, 3}, accepted at 2, where V₂ < 0.** This is a **u¹-unfavourable acceptance**, exactly PP62 Cor E.2(i) with w = 3 and v = 2, at both scales. The refusal at 3 persists along the very ray on which C_{u_t} strictly improves at 3, so the section at u is closed for X.
- **Splits (Cor E.2(ii)).** Over the records from the shifted members to their splits Z, (TC) is met by a mixture: 138 accepted-unfavourable, 30 refused-favourable, 300 accepted-favourable, 252 refused-unfavourable, and 90 null. So both escape routes of Lemma S are used. There are 3,644 single-world incomparabilities in the model, 4,519 in V1.

**The V2 core (all clauses listed; CHECKED minimal).** For the balanced sub-swap X′ = C_u[Ep.a ∪ Em.a ↦ C_B], with Y′ its copy:
1. C: ¬[Y′ ⪯₁ C_B] ∨ ¬[Y′ ⪯₂ C_B] ∨ ¬[Y′ ⪯₃ C_B]. This is direct (C) for C_B; by (IB) it is the same as rec(C_u → X′).
2. DEF ×3: ⋁_i [C_{u_t^w} ⪯_i X′] for w = 1, 2, 3 (coarse scale).
3. SEC ×3: [C_{u_t^w} ⪯_w X′] ⟹ [C_u ⪯_w X′], for w = 1, 2, 3.
4. END2 ×6: ¬[C_{u_t^w} ⪯_v X′] for the two worlds v ≠ w. These are the endorsement units: V_v < 0 there, by PP62 Lemma 1.3(b).

This is PP62's Theorem E, reproduced clause by clause with no (TC) and no (G). **Every clause except the six END2 units is an axiom instance.** So the obstruction is exactly the endorsement hypothesis, and V0/V1 show that dropping it at the shifted members suffices.

**Answer to the coordinator.** The Cor E.2 configuration, with closed sections along actual pure-shift sequences at two scales, all Lemma S splits and all (IB) copies, is **relationally SAT**. It is not an axiom-level obstruction, and by Theorem C no finite or countable version of it can be. The extracted local shape is R₀ with w₀ = 3 everywhere, *except* that the e₃-germ accepts at world 2 against u¹. This is the single non-endorsed acceptance Cor E.2 demands, met exactly once per direction and scale, with (TC) on the splits absorbed by a mixture of refused-favourable and accepted-unfavourable split comparisons.

*Caveat.* The ε-masses of layer atoms are taken equal in the endorsement units (V2). The signs that matter for the core, V_v < 0 for v ≠ w on the whole layer, are PP62 Lemma 1.3(b) (PROVED at u, by symmetry), so the core does not depend on that choice.

---

## 6. The surviving allocation

**E2: one explicit allocation (CHECKED, `run61b_E2.out`, `extract61_E2.out`).**

*Instance.* The full G3 instance of §1 (357 base models, 198 swaps, 9 germs, 532,873 records).

*Pattern hypothesis.* Every one of the 24 balanced swaps X = C_a[F ↦ C_b] has some world refusing both r = rec(C_a → X) and r⁻ = rec(X → C_a).

*Result.* Relational SAT. The assignment was re-checked exactly: every G, DEF, UND, C and SEC clause, every pattern clause, and (TC) on every ordered triple of the base instance and all nine germ sub-instances, at every world. 0 violations.

*The allocation on the balanced swaps.* All 24 balanced swaps have u¹-increments ±(−2, 1, 1) per unit mass, so world 1 is the distinguished world. Each falls in one of three patterns:

| R(r) | R(r⁻) | world 1 | world 2 | world 3 | count |
|---|---|---|---|---|---|
| {1, 3} | {2, 3} | r refused, r⁻ accepted | r accepted, r⁻ refused | **both refused** | 10 |
| {2, 3} | {1, 3} | r accepted, r⁻ refused | r refused, r⁻ accepted | **both refused** | 10 |
| {2, 3} | {2, 3} | both accepted (single-world tie) | **both refused** | **both refused** | 4 |

- **Every balanced inverse pair is incomparable at world 3**, and four are also incomparable at world 2 (with a tie at world 1). Across all source-versus-rival pairs there are 43 single-world incomparabilities at world 3, 8 at world 2 and 6 at world 1, and 4 single-world ties, all at world 1.
- **Openness in the source.** For every balanced swap and every pure-shift direction e₁, e₂, e₃, the refusal set of the shifted record rec(C_{a_t} → X) equals R(r), and that of rec(C_{b_t} → Y) equals R(r⁻) (all 24 × 6 germs, "13/13/13" and "23/23/23" in `extract61_E2.out`). So the refusals persist along every pure-shift ray, *including* the ray along which C_{a_t} strictly improves at the refusing world. Λ fails exactly there.
- **Defence and protection** hold for every source and every shifted source against every rival in the instance, including the copies P = C_b[F ↦ C_a, σ_t ↦ C_{a_t}].
- **Unassigned records.** Inside the instance: none. Every record among the 357 base models and the 9 × 137 germ models is accepted or refused at every world. Outside the instance: everything else is unassigned. In particular nothing is claimed for rivals not in the instance, for sources other than G3 and their pure-shift germs, or for non-pure-shift sequences.

*Weights.* No common q certifies the prescribed refusals: exact α-certificate α = (1, 2) on "C_B refuses B[K09.c1 ∪ K11.c1 ↦ D] at world 1" and "… at world 3". The increments are (−2, 1, 1) on one atom and (2, −1, −1) on the other, so d₁ + 2d₃ = 0 pointwise. By Prop A″ this is an obstruction for every reweighted relation. Every incomparability at one world also gives its own α = (1, 1).

**This is the brief's target outcome, on a finite instance and with the status of a CANDIDATE.** One explicit record-based allocation handles a genuinely 2-D finite family of sources (G3 and its germs) and overlapping, balanced and non-conic swap rivals with all their common-context copies. Its refusals are open along every germ, defence and protection hold, (TC) holds on every triple, and no common q certifies it. By Theorem C, a finite instance cannot show more than this: the continuum statement is the constructor's (PP62) business. The allocation suggests a rule: **keep an additive verdict at the distinguished world and one other world, and refuse both directions of a balanced record at the remaining world.** That rule is non-additive in the precise sense of Theorem Q: it refuses at world 3 records whose first-level value there is strictly favourable, at the shifted sources.

**E3 and E5 (pattern hypotheses that are relationally constrained; status at the time of writing).** Two further runs were set up on the full instance:
- E3: every kink-type balanced swap is non-straddling with a tie at world 1;
- E5a/b: the overlapping orientations of A4, prescribed as exact refusal sets.

A purely lazy (TC) search did not converge in the time available. A first, **local** run (records not touching the pattern frozen at Λ_w) returned UNSAT. But its core contained freezing units, so it is **not** an obstruction. Its core identifies the first forced change, in a genuine (TC) step:
- E3's tie at world 1 between B and B[K09.c1 ∪ K17.c1 ↦ D];
- the guidance link on K09.c2;
- together these force C_B to refuse the overlapping swap B[K09.c1 ∪ K09.c2 ∪ K17.c1 ↦ D] at world 1 (Lemma S in miniature).

A core-guided relaxation (release every frozen record that appears in a core, and re-solve) was stopped unfinished when the note closed. **No conclusion is drawn from E3 or E5.** By Theorem C, neither can give an axiom-level obstruction: any UNSAT would be relative to the pattern hypothesis.

---

## 7. Side test: world-dependent weights q_i (minor; PROVED)

With q_i per world, a refusal requirement at world i reads ∫ q_i d < 0.
- **Same-world incomparability is still never certified:** d and −d at the same world use the same q_i, and α = (1, 1).
- **Non-straddling patterns become certifiable.** For example, r refused at 2 and r⁻ at 3 on a kink swap needs Q₂(Ep) < Q₂(Em) and Q₃(Ep) > Q₃(Em). Here Q_i(E) := ∫_E q_i|g|.
- REFEREE_round53 §5 notes that world-dependent q breaks Theorem L's common Bayes step. So these weights certify refusals but give no relation with the non-section axioms. No further work was done on this branch, as the audit asked.

---

## 8. Scripts (`r9/PP61_py/`; run `python3 -I -B <script>` inside the folder)

| Script | Content | Label |
|---|---|---|
| `geom61.py` → `geom61.out` | sources, (2V), classes, atoms, exact shift wedges, chirotope stability, Lemma 4.1 | CHECKED, ALL PASS |
| `inst61.py` | instance, exact records ((IB)), clause generator, lazy (TC) CEGAR, full (TC) re-check, Λ_w evaluator | library |
| `build61.py` | balanced / overlapping / non-conic swap families | library |
| `lp61.py` | exact q / α alternative (Gordan on atoms = pointwise certificate) | library |
| `run61a.py` → `run61a_G3_part1.out` (the SAT part of this script was superseded by run61b) | §2: Λ_w satisfies every clause; Λ₁ fails exactly SEC on balanced swaps | CHECKED |
| `run61b.py` → `run61b_E2.out` (E2), `run61b_E35loc.out` (E3/E5, unfinished) | §4, §6 pattern experiments | CHECKED (E2); E3/E5 open |
| `run61c.py` → `run61c.out` | §5 adaptive game | CHECKED |
| `extract61.py` → `extract61_E2.out` | §6 allocation extraction | CHECKED |
| `run61d.py` → `run61d.out` | §5.1 Cor E.2 configuration: V0/V1 SAT (model extracted), V2 UNSAT (core) | CHECKED |
