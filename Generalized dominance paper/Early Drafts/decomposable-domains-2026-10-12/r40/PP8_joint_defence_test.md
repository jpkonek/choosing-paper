# PP8. The joint-defence candidate, implemented: anchored defences are lost and sections are not closed

21 October 2026, Round 40 (implementation attack on `AUDIT_joint_defence.md`). Labels as in PP7:
- **PROVED**: the full argument is given here. One reader (me); not refereed.
- **CHECKED**: an exact finite computation.
  - Exact rational cones and exact anchor polygons.
  - Every cell mass has a rigorous error radius (160-bit arb balls; python-flint). Every sign and comparison used is certified against an error bound.
  - Each reported failure is re-derived by a **second, independent implementation**: per-pair local cell arrangements, PP7's own `record`/`anchor_set` routines, 40-digit mpmath intervals, and a separate coding of the 64-state choice and the priorities.
- **NUMERICS**: survival in a finite pool, statements holding at sampled path points, and LP solutions without an exact certificate.
- **OPEN**.

Scripts are in `PP8_py/` (`python3 -I -B <script>`; outputs in `*.out`). `pp7core.py` is an unmodified copy of `PP7_py/core.py`. I add no assumption to the programme. The candidate is implemented **exactly as audit states it**. Variants appear only in §6, are labelled as variants, and are never used for items 1–4.

**Finite pools are a valid test of failure.** R⁰ is record-local, and the priorities (s, m) are functions of the record pair. So every violating triangle in a pool is a violating triangle of the continuum rule, with the same lowest pair. A deletion found in a pool is a deletion of the rule. Survival in a pool is not proof.

---

## 0. Verdicts

**1. Yes: anchored records lose every required defender (CHECKED, all four settings; mechanism PROVED).** There are two mechanisms. Both sit at the point a where a dominating rival's *reverse* record becomes anchored. Every lost defence found comes from one of the following two kinds of triangle.

- **F-A, PP5's pump (κ = 4 version).**
  - *The configuration.* Y is C_a with advice A on three small cones, one per class, where C_a is silent and a nearby C_q says A. Y beats C_a additively at every world. But q ∈ A(rec(Y, C_a)), so the reverse comparison "Y ⪯ C_a" is eligible everywhere.
  - *The joint choice.* It therefore gives C_a **one** defence, at the world j* of least c_j, and that defence has s = 0.
  - *The triangle.* Let Z be C_a improved for world j* on a tiny cone. Then
    - C_a ⪯_{j*} Y is the only defence, with priority (0, 1.000);
    - Y ⪯_{j*} Z is an anchored, additively safe return, with priority (0, 1.956);
    - Z ≺_{j*} C_a is compulsory guidance.
  - *The deletion.* This triangle marks {C_a, Y}. Afterwards C_a ⪯_i Y holds at no world, although a ∈ A(rec(C_a, Y)) imposes the full-face obligation.
  - *Status.* PROVED as Propositions 2.1–2.2. CHECKED in 11 of the 12 (setting, lead world) instances. The exception is e1_1 with lead world 3: there the return's own reverse is anchored and takes world j*, so the pump does not fire for the four T cells tried.
- **F-B, an edge obligation with three models {C_a, C_p, Y}.**
  - *The obligation.* rec(Y, C_a) has an anchor polygon that meets the edge Δ₁₂. So Y ⪯ C_a must hold at world 1 or 2.
  - *The joint choice.* It puts the reverse at worlds {2, 3}.
  - *The triangle.* For a selected p next to a,
    - C_a ⪯₂ C_p is additive, priority (0, 3.66);
    - C_p ⪯₂ Y is a protected defence, priority (1, ·), because the reverse of rec(C_p, Y) is not anchored;
    - Y ⪯₂ C_a has priority (0, 2.5), and C_a ⪯₂ Y is refused.
  - *The deletion.* This triangle deletes the world-2 defence, so the edge obligation is left with world 3 only.
  - *Status.* CHECKED in all four settings by both implementations.
- **PP7's certified configurations do not fail.** These are t8, t1, the t3 core and the t6 core, on which AF + symmetric thinning was UNSAT. Pools are closed under splicing, up to 100 models. In every setting, (TC) is restored and **no obligation is lost** (NUMERICS: survival is not proof). So the joint choice's strict defences do defeat PP7's gluing obstructions on these pools. The failure lies elsewhere: dominating rivals whose reverse is anchored.

**2. Sections are not closed (rival held fixed, p moving along selected models).**
- **(a) R⁰ itself is not closed (CHECKED at the points listed; mechanism PROVED, Lemma 3.1).**
  - On two paths through a, in all four settings, R⁰ accepts C_p ⪯ Y at worlds {1, 2, 3} for t = ±10⁻⁶, ±10⁻⁸, ±10⁻¹⁰, ±10⁻¹². At t = 0 it accepts only at {j*}.
  - Cause: the reverse is anchored exactly at a. The joint choice then hands the two other worlds to the reverse.
  - So {p : C_p R⁰_i Y} has an isolated hole at a for both i ≠ j*.
- **(b) After the deletion, the hole is at all three worlds, and covering fails at a.** No world in supp a accepts C_a ⪯ Y (F-A).
- **(c) A second, deletion-made hole lies at the boundary of N(Y).** Here N(Y) is the set of p at which Y beats C_p additively at every world.
  - s = 1 needs b_j < 0 at all three worlds, which is an open condition. So s drops to 0 *at* the boundary point.
  - At certified bracketing points 10⁻¹⁴ apart, the defence survives at every world just inside. Just outside it is deleted at one or two worlds, by a triangle through C_a (or through Z), with priority margins ≥ 0.8.
  - Hence the boundary point itself is deleted (s = 0 there) while points just inside are accepted. CHECKED at the brackets; the conclusion at t* is by continuity (NUMERICS).
- For PP7's rival Y, whose reverse is never anchored, no non-closed section was found along a path crossing ∂N(Y) (NUMERICS).

**3. Undominatedness and direct (C) (CHECKED on every pool).** No selected model is dominated, before or after the deletion, and there is no all-world tie with a selected model. So direct (C) is never engaged. Undominatedness survives F-A: after the deletion Y ⪯ C_a holds at most at the two non-defending worlds.

**4. Non-additivity.**
- **PP7 pools.** At every world a strictly positive field endorses all surviving non-guidance defences out of selected models. The field is CHECKED by exact rational re-verification. The one exception is u_1, t3 core, world 2: the LP is feasible only at zero margin, with no exact certificate (NUMERICS). So non-additivity is not visible on these pools, as PP3 and PP7 found.
- **Pump pools.** At the defending world **no** positive field endorses the surviving defences (CHECKED, exact Farkas certificate). The defences rec(C_a, Y+T) and rec(C_q, C_q − cones + T) have step vectors whose sum (weights ¼, ¼) is a pure improvement: the cone steps cancel and the T steps add.

**5. Nearby rules (NOT the candidate; NUMERICS; §6).** Three record-local patches were tried. Each repairs the pump and moves the failure elsewhere.
- **V1**: protect every additively dominated defence (drop "A(bar d) = ∅" from s). It fails on the mixed pools: 2–8 lost obligations, on edge-anchored returns.
- **V2 + V1**: close R⁰ at anchored-reverse points. Worse: 8–12 lost obligations.
- **V3**: put obligation-critical pairs first. It survives every pump and mixed pool. But on the path pool the triangle C_a ⪯ C_p ⪯ Y ⪯ C_a deletes **both** initial defenders of the selected record rec(C_a, C_p) at once. This is exactly audit's §6 worry.

**Proposed shift (§7).** The defect is structural, not a matter of tuning. A one-shot, lowest-priority, simultaneous deletion cannot see coverage. I propose keeping the joint choice, which does defeat PP7's obstructions, and replacing step 4 by a **coverage-constrained deletion**: a record-based set of deletions that hits every violating triangle and leaves every face obligation a defender. On finite pools this is a SAT problem of PP7's kind. The open problem is a closed, record-level rule that realises it.

---

## 1. What was run

**Rule (`jd.py`), exactly as specified.**
- **Records.** For d = rec(X, Y): b_i = ν(P_i) − ν(Q_i), Φ_i = 4ν(P_i) − ν(Q_i), c_i = ν(Q_i)/(ν(P_i) + ν(Q_i)).
- **Eligibility.**
  - Guidance is compulsory, and its strict reverse is forbidden.
  - A non-guidance direction is eligible at i iff A(d) ≠ ∅ and Φ_i ≥ 0.
  - The face requirements apply to d and to bar(d).
- **Joint choice.** All 4³ states, in the order:
  1. minimise the number of both-worlds;
  2. maximise the number of accepted non-guidance directions;
  3. minimise Σc;
  4. tie-break.
- **The tie-break (objective 4).**
  - The rational boxes are the unit cubes ∏[a_j, a_j + 1], a ∈ {−1, 0}³, taken lexicographically: one explicit start of audit's determining family.
  - The first nonzero world-1 integral of r₁(new) − r₁(old) orients the pair.
  - States are ordered forward-only < reverse-only < both < neither, world 1 first.
  - Exact ties (as opposed to float near-ties) are certified exactly. The test looks for a signed coordinate permutation that carries the P-step function onto the Q-step function, checked on the common refinement of the arrangement and its image.
- **Priorities.** (s, m) exactly as specified, on pairs present at i with no guidance in either direction.
- **Deletion.**
  - Every ordered violating triple of the pool at every world is inspected.
  - All pairs of lowest priority are marked; exact equality is used, and the number of uncertified near-ties is 0 in every run.
  - A marked record is deleted together with its reverse at that world, in every context.
- **Records across contexts.** Each pool lives on one global central arrangement. Records are identified by exact equality of (changed cells, old advice, new advice).
- **Closure under the pool's own records.** For every record rec(X, Y) and every pool model Z agreeing with X on D, add Z with Y's advice on D. Iterate to a fixpoint. Every pool closed except e1_1's mixed pool, which was capped at 400 models.

**Certification counts.** Over all runs:
- uncertified Φ signs: 0;
- uncertified objective-3 comparisons: 0;
- uncertified priority comparisons: 0.

Objective 4 was reached only through exact mirror ties.
- In PP5's diagnostic there are two: (.95,.01,.04)/(.95,.04,.01) and (.96,.03,.01)/(.96,.01,.03), where b₁ = 0 exactly.
- On the e₁ .3 path along (0,1,−1) there are six, because a = (.9,.05,.05) lies on the mirror line.

The orientation was exact in every case. (TC) holds after the deletion in every pool, as audit's §5 argument requires (CHECKED on pools).

**Configurations.** Settings: near e₁, p₀ = (.9, .06, .04); near u, p₀ = (.35, .33, .32); ε = .3 and .1.

| config | source | models after closure |
|---|---|---|
| t8 | PP7: C_{p₀} + 8 nested sticky rivals | 16 |
| t1 | PP7: C_{p₀}, Y, Xc, Xu, Z₁₋₃, YZ₁₋₃ | 64 |
| t3c | PP7 deletion-minimal core, 14–15 selected + Y | 52–100 |
| t6c | PP7 mixed core, 2 selected + 6–8 rivals | 72–96 |
| pump (lead world 1, 2, 3) | PP5 t7, κ = 4 version: C_a, C_q, Y, Z | 8 |
| mix | PP7 t1 + pump models on C_{p₀} | 384–400 |
| diag | PP5's selected a, b, c, y₁, y₂ + grid triples (e₁, .3 only) | 10 |

For the pump at e₁, ε = .3, lead world 1, a and q are PP5's own: a = (9/10, 1/20, 1/20), q = (901/1000, 51/1000, 48/1000). Elsewhere q is found by search (`pump_q`).
- Y carries A on one exact cone per class where C_a is silent and C_q says A. The masses are (m, ¾m, ¾m), with the lead class m.
- Z carries B on a cone of the lead class where both C_a and C_q are silent.

Bugs found and fixed before the final runs:
- Point location ignored the coordinate planes. It was used only by the symmetry test and the incoherence search, and did not affect any reported verdict.
- The LP's normalisation cap w ≤ 1000·mass produced one spurious "infeasible". Replaced by an uncapped retry.

---

## 2. Item 1: lost defences

### 2.1 The mechanism (PROVED)

**Lemma 2.0.** For a non-guidance direction e at world i, m_i(e) = (4P − Q)/(P + Q) < 3/2 iff b_i(e) < 0.

*Proof.* 8P − 2Q < 3P + 3Q ⟺ P < Q. ∎

So **within s = 0, every additively unsafe comparison has lower priority than every additively safe one**. The only protection a defence against a dominating rival has is s = 1.

**Proposition 2.1 (a single, unprotected defence).** Let a be interior, d = rec(C_a, Y), and suppose:
- (i) A(bar d) ≠ ∅;
- (ii) b_j(d) < 0 for all j;
- (iii) P_j(d) > 0 for all j, so neither direction is guidance anywhere;
- (iv) the only face obligation of d is the full face;
- (v) J = {j : Φ_j(d) ≥ 0} ≠ ∅, and j* = argmin_{j∈J} c_j(d) is unique.

Then R⁰ accepts d exactly at j* and bar d exactly at the other two worlds. At j* the pair has priority (0, m) with m < 3/2.

*Proof.*
1. **bar d is eligible at every world.** It is non-guidance by (iii). A(bar d) ≠ ∅ by (i). And Φ_j(bar d) = 4Q_j − P_j > 0 by (ii).
2. **No vertex obligation of bar d sits at j*.** Suppose bar d had the vertex obligation {j*}. Then C_{e_{j*}}, which is correct at world j* on every problem, would agree with Y on D. So Y would have rank 0 at j* on D, and bar d would be guidance at j*, contradicting (iii).
3. **The value of objectives 1 and 2.** Every face obligation of bar d therefore meets {1, 2, 3} ∖ {j*}. So "d at j*, bar d elsewhere" is feasible, with 0 both-worlds and 3 accepted directions. This is optimal for objectives 1 and 2, which therefore force exactly one direction per world, with d's set W nonempty (by (iv)) and W ⊆ J.
4. **Objective 3.** The c-sum is Σ_j c_j(bar d) + Σ_{j∈W} (2c_j(d) − 1), and each summand 2c_j(d) − 1 is > 0 by (ii). So W = {j*}.
5. **Priority.** At j* only d is accepted. s = 0 by (i), and m < 3/2 by Lemma 2.0. ∎

**Proposition 2.2 (the pump deletes it).** In addition, let Z satisfy:
- (a) Z is a strict pointwise world-j* improvement of C_a;
- (b) R⁰ accepts rec(Y, Z) but not rec(Z, Y) at j*;
- (c) b_{j*}(rec(Y, Z)) > 0.

Then (C_a, Y, Z) violates (TC) at j* in R⁰, and its unique lowest removable pair is {C_a, Y}. Hence R accepts C_a ⪯ Y at no world, and (S)'s defence clause fails at a for Y.

*Proof.*
1. **The violation.** C_a ⪯ Y (Prop. 2.1), Y ⪯ Z (b), and Z ⪯ C_a (compulsory, by (a)). C_a ⪯ Z is forbidden, as a strict guidance reverse.
2. **The priorities.** {Z, C_a} is not removable. {Y, Z} has s = 0 by (c), and m > 3/2 by Lemma 2.0. {C_a, Y} has (0, m < 3/2).
3. **The deletion.** {C_a, Y} is marked, and it was accepted only at j*. ∎

Condition (b) holds, for instance, when A(rec(Y, Z)) ≠ ∅, A(rec(Z, Y)) = ∅ and (c) holds. In the failing e1_1 lead-3 instance, rec(Z, Y) is anchored and its single forced world is j*, so (b) fails.

**Why this is not a corner case.**
- Hypothesis (i) says exactly that Y's disagreement with C_a is realised out of another selected model. So Y is a splice of C_a and some C_q.
- PP5 Prop. 4.3 and t7 build such rivals at every interior index.
- Theorem 3 of `AUDIT_optional_defenders.md` gives κ = 4 *two* eligible worlds for d. The joint choice's objective 3 nevertheless spends only one of them, because the anchored reverse is cheaper at the other two worlds.
- So audit's "Concrete consequence" (§2), which yields at least two strict defences, applies only when A(bar d) = ∅. That hypothesis is essential.

### 2.2 Certificates (CHECKED; `t3_pump_certificate.py`, independent implementation)

At the lead world j*, with masses (m, ¾m, ¾m):
- c_{j*} = 0.6 and c = 0.7 elsewhere;
- the objective-3 optimum is 1.2, unique and certified, among 42 feasible states;
- m({C_a, Y}) = 1.000 and m({Y, Z}) = 1.956.

| setting | lead world | b(rec(C_a, Y)) (all < 0, certified) | R⁰ worlds of d / of bar d | deleted, obligation failed |
|---|---|---|---|---|
| e₁ .3 | 1 / 2 / 3 | (−1.67, −3.35, −3.35)e-6 (lead 1) | {j*} / other two | yes / yes / yes |
| e₁ .1 | 1 / 2 | (−0.93, −1.87, −1.87)e-7 (lead 1) | {j*} / other two | yes / yes |
| e₁ .1 | 3 | (−2.49, −2.49, −1.25)e-7 | {3} / {1, 2} | **no**: rec(Z, Y) is anchored and forced to world 3, so Y ⪯₃ Z is refused (4 T cells tried) |
| u .3 | 1 / 2 / 3 | (−0.81, −1.61, −1.61)e-6 (lead 1) | {j*} / other two | yes / yes / yes |
| u .1 | 1 / 2 / 3 | (−0.53, −1.07, −1.07)e-6 (lead 1) | {j*} / other two | yes / yes / yes |

The same failures appear in the global-arrangement runs (`t1_main_*.out`, rows pump1–3). There the pools are closed under splicing (8 models).

### 2.3 The full collection of triangles responsible (`t5_triangles.py`; every marking triangle in each closed pool)

- **Pump pools, all settings and lead worlds that fail.** At j* there are **12 ordered marking triangles**. All of them realise **one** triple of record pairs, {rec(C_a,Y)}, {rec(Y,Z)}, {rec(Z,C_a)}, in four contexts:
  - (C_a, Y, Z);
  - (C_q, C_q with S on the cones, Z with C_q's advice off the cones);
  - (C_q, Z^[C_a>C_q], Z^[Y>C_q]);
  - (Y, Z, Z^[C_a>Y]).

  Each context gives a strict 3-cycle, counted in its three rotations. In plain English:
  > *C_a is at least as good as Y at world j* (its only defence); Y is at least as good as Z there (Z is C_a made better for world j* on a tiny cone, and Y's comparison with it is anchored at q and additively safe); Z is strictly better than C_a there (compulsory). The defence is the least protected of the three: s = 0 because Y's comparison back to C_a is anchored, and its margin 1.0 is below the return's 1.96.*
- **Mixed pools (PP7 t1 + pump).** Two records fail: rec(C_{p₀}, Y) and rec(C_{p₀}, Y + T). In e1_3 there are 576 and 96 ordered marking triangles. They realise 2 and 1 record triples, and in e1_1 6 and 4. The extra triples replace the guidance link by an **additively safe return**. For example: C_{p₀} ⪯₁ Y (1.000); Y ⪯₁ Z₂^[C_{p₀}>Z₁] (1.506); Z₂^[C_{p₀}>Z₁] ⪯₁ C_{p₀} (1.500); C_{p₀} ⪯₁ Z₂^[C_{p₀}>Z₁] not chosen. By Lemma 2.0 the defence loses to any two additively safe links.

### 2.4 F-B: the edge obligation (CHECKED; `t7_edge_certificate.py`, independent implementation)

The three models are C_a, C_p and Y, with p = a + t v.

| setting | t, v | world-2 priorities {C_a,C_p} / {C_p,Y} / {Y,C_a} | R⁰ worlds of rec(Y,C_a), anchored on Δ₁₂ | result |
|---|---|---|---|---|
| e₁ .3 | 10⁻⁶, (1,−1,0) | (0, 3.657) / (1, 0.389) / (0, 2.500) | {2, 3} | edge obligation fails |
| e₁ .1 | 10⁻⁸, (1,−1,0) | (0, 3.998) / (1, 0.476) / (0, 2.500) | {2, 3} | fails |
| u .3 | −10⁻⁶, (0,1,−1) | (0, 3.674) / (1, 0.190) / (0, 2.500) | {2, 3} | fails |
| u .1 | 10⁻⁸, (1,−1,0) | (0, 3.687) / (1, 0.493) / (0, 2.500) | {2, 3} | fails |

In plain English:
> *C_a is at least as good as C_p at world 2 (additive order); C_p is at least as good as Y there (C_p's defence, protected because nothing is anchored on the way back); Y is at least as good as C_a there (the reverse comparison, which some precise model on the edge [e₁, e₂] needs defended at world 1 or 2); C_a ⪯₂ Y was given to world 1 only. The reverse is the lowest removable pair, so its only edge defender goes.*

The pp7 anchor polygon of A(rec(Y, C_a)) meets Δ₁₂ exactly (CHECKED). The protection of {C_p, Y} is the audit's s = 1, which is what pushes the deletion onto the edge-anchored reverse.

### 2.5 PP7's certified configurations (NUMERICS: survival in closed pools)

In every row: (TC) final 0, lost obligations 0, dominated 0, ties 0.

| setting | t8 / t1 / t3c / t6c: models | initial (TC) violations per world | anchored records losing *some* defender |
|---|---|---|---|
| e₁ .3 | 16 / 64 / 60 / 96 | [0,24,12] / [96,48,144] / [234,246,108] / [324,114,372] | 3 / 3 / 70 / 16 |
| e₁ .1 | 16 / 64 / 52 / 96 | [12,24,0] / [96,48,96] / [258,390,48] / [168,114,960] | 3 / 2 / 173 / 25 |
| u .3 | 16 / 64 / 60 / 72 | [0,24,12] / [96,0,0] / [78,264,246] / [36,72,348] | 3 / 1 / 78 / 7 |
| u .1 | 16 / 64 / 100 / 72 | [0,24,12] / [48,96,96] / [114,858,204] / [54,480,804] | 3 / 2 / 151 / 22 |

**Larger pool.** PP7's full t6 pool at e₁ .3 (9 selected + 16 rivals) was run with closure capped at 400 models (`t1_main_e1_3_t6.out`).
- Initial (TC) violations: [4806, 17595, 35904]; final: 0.
- 2,064 anchored records lose some defender. **None loses all.**
- No domination and no ties. Endorsed at every world (exact field).

On these rivals A(rec(Y, C_q)) = ∅ for every q in the pool. Their defences are strict at every eligible world and protected (s = 1). Every non-guidance defence out of a selected model in the final relations is strict: there are no ties, in any pool. PP5's diagnostic (selected models only) has no violation at all: among selected models R⁰ is the additive order W_add.

---

## 3. Item 2: sections and covering

### 3.1 R⁰ is not closed (Lemma PROVED; hypotheses CHECKED at the listed points)

**Lemma 3.1.**
- *Hypotheses.* Let Prop. 2.1 hold at p = a. Let p_n → a be selected indices such that, for d_n = rec(C_{p_n}, Y):
  - A(bar d_n) = ∅;
  - bar d_n is not guidance;
  - Φ_i(d_n) ≥ 0 at every i.
- *Conclusion.* R⁰ accepts d_n at every world, but accepts d only at j*. So for i ≠ j*, {p : C_p R⁰_i Y} is not closed.

*Proof.* bar d_n is never eligible, while d_n is eligible everywhere (p_n ∈ A(d_n)). Objective 2 then accepts d_n at every world, while Prop. 2.1 applies at a. ∎

The mechanism is general. Eligibility of the reverse is a closed condition (A ≠ ∅ is closed), and the joint choice *removes* the forward direction where the reverse becomes eligible and cheaper. So R⁰ acceptance is anti-monotone in a closed condition.

**CHECKED (`t6_r0_sequence.py`, independent implementation).** The paths are p = a + t v with v = (1,−1,0) and (0,1,−1), in all four settings.
- At t = 0: A(rev) ≠ ∅, and R⁰ gives {1} / {2, 3}.
- At t = ±10⁻⁶, ±10⁻⁸, ±10⁻¹⁰, ±10⁻¹²: A(rev) = ∅, and R⁰ gives {1, 2, 3} / ∅. The unique optimum is certified at every point.
- At e₁ .1, t = ±10⁻⁶ already leaves N(Y), and the forward is still accepted at two worlds.

That A(rec(Y, C_p)) = ∅ for **all** small p ≠ a is NUMERICS.

### 3.2 After the deletion (`t2_sections.py`; NUMERICS on path pools; signs certified)

Pool: 13 path points t ∈ {0, ±10⁻⁶, ±10⁻⁵, ±3·10⁻⁵, ±10⁻⁴, ±3·10⁻⁴, ±10⁻³}, together with C_q, Y and Z. Example at e₁ .3, v = (1,−1,0) ('#' means accepted):

| world | R⁰ section | R section |
|---|---|---|
| 1 | `...##########` | `...###.######` |
| 2 | `######.#.....` | `######.#.....` |
| 3 | `######.######` | `######.#.....` |

- Isolated refused point at t = 0 at every world after the deletion.
- **Covering fails at a**: no world accepts C_a ⪯ Y.
- The same pattern holds on both paths in every setting.
- The path pools also exhibit F-B. In e₁ .3 they have 2–3 failed obligations.

### 3.3 The boundary of N(Y) (CHECKED at the brackets; the conclusion at t* is NUMERICS)

Bisection on b locates t* to within 10⁻¹⁴. Pool: C_p(t), C_a, C_q, Y, Z.

| setting, v | t* | just inside (s = 1) | just outside (s = 0) | deleting triangle; priorities |
|---|---|---|---|---|
| e₁ .3, (1,−1,0) | 2.2354319e-6 | R = {1,2,3} | R = {1} | C_p ⪯ Y ⪯ C_a ⪯ C_p at worlds 2, 3; (0, .278) vs 2.5, 3.66 and (0, .665) vs 2.5, 1.63 |
| e₁ .3, (0,1,−1) | ±4.7918205e-6 | {1,2,3} | {1,2} or {1,3} | same shape; (0, .216) vs 2.5, 3.26 |
| e₁ .1, (1,−1,0) | −2.4871993e-7 | {1,2,3} | {2,3} | C_p ⪯ Y ⪯ Z ⪯ C_p at world 1; (0, .539) vs 1.956, 3.63 |
| u .3, (1,−1,0) | 7.199609e-7 | {1,2,3} | {1} | through C_a; (0, .283) vs 2.5, 3.63 and (0, .687) vs 2.5, 1.52 |
| u .1, (1,−1,0) | 4.028075e-7 | {1,2,3} | {1} | through C_a; (0, .278) vs 2.5, 3.69 and (0, .681) vs 2.5, 1.53 |
| u .1, (0,1,−1) | 7.981200e-7 / −8.357306e-7 | {1,2,3} | {1,2} / {1,3} | through C_a; (0, .163) vs 2.5, 3.57; (0, .121) vs 2.5, 3.66 |

At the boundary point the values of b are certified on either side (|b| ≈ 10⁻¹⁵ > error bound), and every link of the deleting triangle has a large margin.
- At t* itself s = 0 by definition, since s = 1 needs b_j < 0 at all three worlds.
- The triangle's links persist across the bracket, and the priority gap is ≥ 0.8 in every row.
- So t* is deleted while t ↑ t* is accepted: **the section is not closed at t***.

The step "persist at t*" uses continuity of ν(P_i), ν(Q_i) in t, and A(rec(Y, C_{p(t*)})) = ∅. It is NUMERICS. Some brackets show no deletion (e.g. e₁ .3, v = (1,−1,0) at t < 0), because no triangle is present there.

### 3.4 PP7's rival Y (reverse never anchored)

Paths cross ∂N(Y) (at e₁ .3, between ±0.8 and ±1.3·10⁻³), with rivals Y, YZ₁₋₃ and Xc in the pool. In all four settings:
- the R⁰ and R sections coincide;
- the sections are intervals, ending only where Φ⁴ changes sign (a closed condition);
- no deletion occurs on these sections;
- covering holds at every path point (NUMERICS).

---

## 4. Item 3: undominatedness and direct (C) (CHECKED on every pool)

- **Dominated selected models.** 0 initially and 0 finally, in every pool, all settings.
- **All-world ties with a selected model.** 0, so direct (C) is never engaged and no incoherence certificate was needed.
- **Under F-A.** Y ⪯ C_a holds at most at the two non-defending worlds. So Y does not dominate C_a; the failure is the defence clause, not undominatedness.

---

## 5. Item 4: is the surviving system non-additive? (LP on the pool)

The test, per world i, asks for strictly positive weights w(cell, level) > 0 with Σ_{P(d)} w − Σ_{Q(d)} w ≥ 0 for every surviving non-guidance defence d = rec(C_q, X) accepted at i. On a pool this is **exactly** the existence of a strictly positive field endorsing those comparisons: any positive cell weights are realisable by a positive density.
- *Feasible.* Max-margin LP, then exact rational re-check of the field.
- *Infeasible.* LP Farkas multipliers, rationalised and verified exactly.

| pools | result |
|---|---|
| PP7 t8, t1, t3c, t6c; PP5 diag; mixed pools (all settings) | **endorsed** at every world: CHECKED, exact field, margin 1. Exception: u .1 t3c, world 2, endorsed only at zero margin; some defences are forced to ties in every endorsing field; NUMERICS |
| pump pools, at the defending world j* | **not endorsed**: CHECKED, Farkas ¼·step(rec(C_a, Y+T)) + ¼·step(rec(C_q, C_q−cones+T)) ≤ 0 with a strict negative part; the cone steps cancel exactly and the T steps are pure improvements at j* |
| pump pools, other worlds | endorsed (CHECKED) |

So on PP7's configurations the candidate's surviving defences are additive *on the pool*. FF2 Thm 4.1 forces non-additivity only in the atomless limit, as PP3 warned. Non-additivity does appear in the pump pools, through records realised out of two different selected models. Those are the same configurations in which the defence is lost.

---

## 6. Nearby rules (NOT the candidate; NUMERICS; `t4_variant.py`, `t8_nearby.py`)

Lost face obligations in closed pools:

| variant | pump (11 firing instances) | mixed pools (e₁.3 / e₁.1 / u.3 / u.1) | PP7 pools | pump path pool (e₁ .3) |
|---|---|---|---|---|
| candidate | 1 each | 2 / 2 / 2 / 2 | 0 | 2–3 |
| V1: s = 1 for every accepted additively dominated defence | 0 | 2 / 8 / 8 / 4 | 0 | — |
| V2 + V1: also close R⁰ at anchored-reverse points (ties) | 2 each (lead 1, 2); lead 3: 0–1, plus 1 dominated selected model | 8 / 12 / 12 / 12 | 0 | — |
| V3: priority (crit, s, m), crit = sole initial cover of some obligation | 0 | 0 / 0 / 0 / 0 | 0 | **2** (path v = (1,−1,0)) |
| V2 + V3 | 3 (e₁ .3, lead 1, 2) | 3 (e₁ .3) | 0 | 0 |

- **V1.** It turns F-A into F-B-type failures: edge-anchored returns such as rec(Z₂^[C_{p₀}>Z₁], C_{p₀}) lose both edge defenders.
- **V3.** It fails on the path pool through the triangle C_a ⪯ C_p ⪯ Y ⪯ C_a, which is violating at worlds 2 *and* 3. The selected record rec(C_a, C_p) has two initial defenders, so neither is critical, and both are deleted in the same pass. This is a concrete instance of audit's §6 worry: "different triangles could mark both initial strict defenders". Here it is the same triangle at two worlds.
- **V2.** It does not repair the R⁰ section hole in the deleted relation (`t8_nearby_e1_3.out`).

---

## 7. What this means, and the proposed shift

**The aim's spirit is: keep the joint, strict defences and get (TC) by explicit deletion.**
- **The first half works where PP7 failed.** On every PP7 configuration where AF + symmetric thinning was UNSAT, the joint choice plus deletion restores (TC) with no lost obligation, no domination and no ties (NUMERICS).
- **The second half cannot, as specified.**
  1. Priorities that are local to a record pair cannot see coverage. Lemma 2.0 makes every additively unsafe defence the victim in a triangle with additively safe links unless s = 1. Broadening s (V1) or adding criticality (V3) only moves the victim.
  2. Simultaneous deletion can remove every defender of a record in one pass (V3).
  3. Both objective 3 (the reverse wins where it becomes eligible) and the open condition in s make sections non-closed. This happens at the anchored-reverse point and at ∂N(Y).

**Proposed nearby target.**
- Keep §1–§2 of the candidate: eligibility, joint choice and the initial strict defences.
- Replace §4 by a **coverage-constrained deletion**: choose a set O = rev(O) of record pairs per world that meets every violating triangle and leaves every face obligation with a defender.
  - By audit's Theorem 4, symmetric deletion creates no new (TC) violations. So (TC) then holds, and the defence clause holds by construction.
  - On finite pools this is exactly a SAT problem of PP7's kind. Its satisfiability on these pools is the next check.
- **OPEN.**
  - A closed, record-level rule realising such an O on the continuum.
  - Closed sections at anchored-reverse points. Here R⁰ itself must change: the natural closed choice is a tie at the defending world's complement exactly on the closed set where the reverse becomes anchored (V2). V2 alone fails with the current deletion, so it must be paired with the constrained deletion, not with a priority.

---

## 8. Scripts (`PP8_py/`)

| script → output | content | label |
|---|---|---|
| `pp7core.py` | unmodified copy of `PP7_py/core.py` | library |
| `jd.py` | the candidate: global arrangement with arb-certified cell masses, exact record identity, closure under splicing, anchors, joint choice (with the exact objective-4 tie-break), priorities, simultaneous deletion; obligation, dominance, tie and incoherence checks; LP endorsement with exact certificates; variant switches V1–V3, off by default | library |
| `configs.py` | PP7 t8/t1/t3/t6 and PP5 diag/t7-pump builders (PP7 code copied) | library |
| `driver.py`, `t1_main.py` → `t1_main_<setting>.out` (+ `t1_main_u_1_t3c.out`, rerun after the LP fix; `t1_main_e1_3_t6.out`, PP7's full t6 pool) | items 1, 3, 4 on all configurations | CHECKED (failures, LP certificates) / NUMERICS (survival) |
| `t2_sections.py` → `t2_sections_e1_3_e1_1_u_3_u_1.out` | item 2: sections along paths, covering, s-boundary bisection | CHECKED (brackets) / NUMERICS |
| `t3_pump_certificate.py` → `.out` | F-A, independent implementation, 4 settings × 3 lead worlds | CHECKED |
| `t5_triangles.py` → `t5_triangles_*.out` | full collections of marking triangles, grouped by record triples | CHECKED |
| `t6_r0_sequence.py` → `.out` | R⁰ section hole at a, t = ±10⁻⁶…±10⁻¹² | CHECKED |
| `t7_edge_certificate.py` → `.out` | F-B, independent implementation, 4 settings | CHECKED |
| `t4_variant.py` → `t4_variant_<setting>.out`; `t8_nearby.py` → `t8_nearby_e1_3.out` | variants V1, V2, V3 | NUMERICS (not the candidate) |

**Dependency.** python-flint 0.9.0 (arb), installed for this round; numpy, scipy (HiGHS), pysat and mpmath as in PP7.
