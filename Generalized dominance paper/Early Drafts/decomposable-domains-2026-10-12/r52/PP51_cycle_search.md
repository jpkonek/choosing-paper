# PP51. Four posterior models: exact search for triple-compatible gates with no global prices

23 October 2026. Task PP51 of Brief 52. One reader (me); not refereed. Includes the coordinator's two mid-task requests: verify PP53 Thm 3.3, and the width-budget and field-ratio questions.

**Labels.**
- PROVED: a complete argument is given here.
- CHECKED: exact rational computation in `r9/PP51_py/`. LPs and MILPs only *propose* solutions; Fractions verify them.
- NUMERICS: floating-point or Monte Carlo output. No proof rests on it.
- CONJECTURE / OPEN: as stated.

**What is exact and what is discretised.** Nothing that matters is discretised.
- The disagreement regions are enumerated exactly, as the cells of a plane arrangement, each with a rational interior ray.
- Every constraint depends only on a point's cell type (Lemma 2.2). So fields that are constant on cells (times |g|) lose nothing. The brief's "fine angular partition" is unnecessary; I use at most one extra sub-cone per cell, for witnesses.
- Bayes, CG2, the triple test and the global-infeasibility certificates are all verified in Fractions.
- Only three things are numerical, and none is used in a proof:
  - the Monte Carlo masses in `geometry51.out`;
  - the tropical survey (§6);
  - the bisection bounds and scaling trends of §7.2 (every design reported there is verified exactly).

---

## 0. Verdict

1. **The checkpoint is met, exactly, for two arrangements around u (Thm 4.2; CHECKED).** The arrangements are R (a rectangle with u at one corner) and Y (u at the centre of a triangle), both at ε = 3/10. In each, the four posterior gates have:
   - strictly guiding fields;
   - strict unique own-Bayes on all four advice values;
   - strict pointwise CG2 for every triple's constants;
   - every triple passing the closed test with slack at every world, hence (TC) under (R0) by PP47 Thm 4.1 and under (R) by Thm R1.

   **No global constants exist at any of the three worlds.** Each world has an explicit Farkas certificate: a 4-cycle whose lower bounds have product 2⁸ > 1. By Lemma 2.4 this also means there is **no additive endorser** at any world. The fields are listed in `design51_{R,Y}.json`.
2. **Mechanism (Thm 4.1, PROVED).** Start from any global witness and shift each triple's constants by an arbitrary bounded amount. The fields then absorb the shifts, at the cost of Bayes margin. **So in fat configurations, nothing forces global prices.** Not own-Bayes (weights drop out exactly; Lemma 2.1), not posterior geometry, and not acceptance.

   The global witness used is the **likelihood witness**, with constants c^N_w ∝ 1/N_w and fields P(g)∘N. It exists exactly in every fat arrangement tested. The checkpoint design is a bounded perturbation of it, and is precisely the "single witness" pattern the audit warned about, made non-additive by hand.
3. **Independent check of PP53 Thm 3.3 (CHECKED, §7).** My code reproduces its 28 cell types and its exact intervals, and certifies no global constants at worlds 1 and 2 (deficits 0.200 and 0.098). The likelihood witness exists for PP53's four models, and they carry no kink certificate.
4. **The decisive negative: the posterior family cannot be gated as a whole (Thm 5.1, the kink obstruction; PROVED; instances CHECKED).** At ε = 3/10, the three indices
   - A = u,
   - B = (406, 421, 373)/1200,
   - D = (406, 373, 421)/1200

   (all within 0.04 of u, and two-valued) admit **no** own-Bayes fields passing the closed triple test at every world, under either strict or zero-accepting gates. The hypotheses are that T's own-Bayes is a.e. unique, or that CG2 is strict on two cells; one residual tie case is stated in §5.2.
   - The certificate uses two cells where T answers alone, one of each sign type at world 1, plus the pair type tests.
   - Instances were found at ε = 1/10, 3/10 and 1/2, and at three scales down to distance 2·10⁻⁴ from u.
   - So any design that gates every C_a near u fails (TC). PP49's architecture is such a design, with index = likelihood.
   - **This is a failure of this architecture and family**, not of co-design generally.
5. **The continuum question (§7).**
   - For a 2-D patch containing the item-4 triple (or its copies at smaller scales, found down to 2·10⁻⁴), the answer is negative. Such a patch has triples with no fields at all, so there is nothing for the multipliers to vary continuously between. That every patch through u contains one is CONJECTURE (scale invariance).
   - On fat sub-configurations, exact-Bayes LPs with likelihood × vortex constants give exactly verified designs. On PP53's four models, a deficit of 0.095 needs within-cell field ratios of only e^1.15, and the maximum is 0.19 at e^6.6, far below PP53's e^30.
   - A fifth and a sixth member can be added. PP53's width budget is then met with near equality, but each member lowers the attainable deficit (0.115 with five, 0.088 with six).
   - The deficit scales linearly with the configuration's size: about ten times smaller when the configuration is ten times closer to u.
   - Most candidate sixth members destroy the likelihood witness (8 of 9, exact).

| Item | Result | Label |
|---|---|---|
| weights absorbed; interior forced | Lemma 2.1 | PROVED |
| cell types suffice (no angular discretisation needed) | Lemma 2.2 | PROVED |
| one constant set ⇔ ω-separability of every cell | Lemma 2.3 | PROVED |
| no global constants at w ⇔ no additive endorser at w | Lemma 2.4 | PROVED |
| 4-cycle deficit ≤ width of each diagonal | Lemma 2.5 | PROVED |
| exact geometry of R and Y; pair-ordering theorem on all cells | §3 | CHECKED |
| perturbation theorem | Thm 4.1 | PROVED |
| R and Y checkpoint designs, all three worlds globally infeasible | Thm 4.2 | CHECKED |
| kink obstruction | Thm 5.1 | PROVED; instances CHECKED |
| obstruction at every tested ε and scale | §5.2 | CHECKED; all scales CONJECTURE |
| PP53 Thm 3.3 | §7.1 | CHECKED (independent code) |
| width budget, fifth and sixth members, field ratios | §7.2 | CHECKED (designs); trends NUMERICS |

---

## 1. Setting

- M = c·1 + εΔ, with c = (1−ε)/3.
- C_a answers h iff (a∘m_v)·h > 0 for v = 1, 2, 3.
- All indices used satisfy u ∈ M_a (CHECKED). So no two members ever give opposite answers, and the common answer at g is h = sign(Σg)·g. Every family here is two-valued.
- At a point with answer set 𝒜 (and silent set 𝒮), Cor = {w : h_w > 0} and Wr = {w : h_w < 0}.
- For model N write E^N_w := |ℓ^N_w(h) − ℓ^N_w(S)| > 0 (strict guidance).
- CG2 for N ∈ 𝒜 and M ∈ 𝒮, with the constants of a group (one triple, or all four) at world w, reads:
  - c_N E^N_w ≤ c_M E^M_w if w ∈ Cor;
  - c_N E^N_w ≥ c_M E^M_w if w ∈ Wr.
- I^w_NM is the realised interval for log(c_N/c_M). The triple test, Thm R1 and PP47 Thm 4.1 are used as in PP47 §4.
- Advice −h and "contradictory" never occur on disagreement sets. They enter only own-Bayes, and are completed explicitly (`verify51.complete`).

## 2. Reductions (PROVED)

**Lemma 2.1 (weights).**
- *Interior weights are forced.* For every w, each posterior model answers, on an open cone, some h that is correct only at w. So λ_w = 0 would contradict weak own-Bayes.
- *Weights then drop out.* Replace E^N_w by 3λ^N_w E^N_w and c^N_w by c^N_w/(3λ^N_w). The CG2 products c·E are unchanged, and λ-Bayes becomes u-Bayes.

So the bilinear coupling between weights and fields in brief item 2 disappears exactly. I take λ = u throughout. `construct51` re-verifies its designs at random interior weights.

**Lemma 2.2 (cells suffice).** Every constraint at a point g (Bayes for each model, CG2 for each disagreeing pair and each group containing it) depends only on g's cell type (𝒜, Cor), and on no other point. So a solution on one representative per type, copied over the type's cells, is a solution, and realised intervals are extremes over finitely many values. Witness tightness needs at most one extra sub-cone per cell.

**Lemma 2.3 (one constant set ⇔ ω-separability).** Fix a group 𝒢 with positive constants c^N and put ω^N := 1/c^N.
- *(⇐)* Fields exist at a cell, with strict Bayes, if there is P > 0 such that n := σ∘P (σ = sign h) has n·ω^N > 0 for N ∈ 𝒜 and n·ω^N < 0 for N ∈ 𝒮.
- *(⇒)* The converse holds under either of two hypotheses: strict own-Bayes, or weak own-Bayes with CG2 strict on that cell.

*Proof.*
- (⇐) Take E^N := P∘ω^N. CG2 then holds with equality, and humility factors (1 ∓ η) make it strict.
- (⇒) Put Q^N := c^N∘E^N. CG2 says Q^𝒜_c ≤ Q^𝒮_c at correct worlds and the reverse at wrong worlds.
  1. Let P_c := min_𝒮 Q_c and P_r := max_𝒮 Q_r.
  2. Then σ·(P∘ω^N) ≥ σ·E^N for every answerer, and ≤ σ·E^M for every silent model.
  3. With strict Bayes, or strict CG2 on the answerers' side, the answerer inequality is strict. ∎

*Consequences.*
- "Global prices" means a single ω for all four models. "Triple feasibility" means an ω^τ for each triple, with fields shared across triples.
- For a single pair, Lemma 2.3 reduces to the pair-ordering condition. For a pair with all four disagreement types, admissible constants must order the worlds as D = log(a/b) does (§3).

**Lemma 2.4 (no prices ⇔ no additive endorser).** In a two-valued gate union, the following are equivalent at a world w, provided every gated model has moves that are two-signed at w:
- there is an additive, strictly guiding U_w that is ≥ 0 on every accepted bounded record;
- the gated models admit global positive CG2 constants at w.

*Proof.* For gated N, the records realised by N form a Lyapunov-convex range. Separation, as in REFEREE_round50 §1.1 "⇒", gives f^U ≥ κ_N f^N on N's moves. Mixed records make κ_N common to all partners. Strict guidance then forces κ_N > 0 at an improving move. Adding the inequalities for N → M and M → N gives κ_N f^N ≤ κ_M f^M, which is global CG2. The converse is PP42 Lemma 3.0. ∎

So the checkpoint, when met, is exactly "no additive endorser at w" for the four gates.

**Lemma 2.5 (deficit ≤ diagonal width).** Take a 4-cycle A→B→C→D with every triple passing the closed test. Then
  Σ_cycle L ≤ width(I_AC), and likewise ≤ width(I_BD).

*Proof.* Triangle ABC gives L_AB + L_BC ≤ U_AC, and triangle ACD gives L_CD + L_DA ≤ −L_AC. Add. ∎

Consequence: wide diagonals are necessary. This is the four-model form of PP53's width budget.

## 3. Geometry (brief item 1; CHECKED, `geometry51.out`)

Both arrangements are at ε = 3/10, with t = 1/100.
- **R:** A = u, B = u + t(1,−1,0), C = u + t(2,0,−2), D = u + t(1,1,−2). Perimeter A-B-C-D, diagonals AC and BD.
- **Y:** A = u, with B, C, D = u + t(2,−1,−1), u + t(−1,2,−1), u + t(−1,−1,2).

Exact enumeration gives:
- R: 114 cells, 41 types, 28 of them with disagreement;
- Y: 106 cells, 37 types, 24 with disagreement.

Every disagreement cell has an exact interior ray. In both arrangements every 1–3, 2–2 and 3–1 split that occurs is listed, with the correct worlds and an MC mass between 10⁻⁴ and 8·10⁻³. In R and Y the answer sets are always separable from the silent sets within the index plane. Non-separable "XOR" splits occur only in thin arrangements (§5).

**Pairs (R).** W is the set of worlds where the second model is worse, R the set where it is better. All pieces satisfy the pair-ordering theorem exactly (rational ratio comparisons, all cells).

| pair | D = log(a/b) order | types (W | R) occurring | admissible order of log(c_b/c_a) |
|---|---|---|---|
| AB | 2>3>1 | {1,2}|{3}, {2}|{1,3}, {2,3}|{1}, {3}|{1,2} | 2>3>1 only |
| AC | 3>2>1 | {1,3}|{2}, {2}|{1,3}, {2,3}|{1}, {3}|{1,2} | 3>2>1 only |
| AD | 3>1=2 (tie) | {1,3}|{2}, {2,3}|{1}, {3}|{1,2} | 3>1>2 or 3>2>1 |
| BC | 3>1>2 | {1}|{2,3}, {1,3}|{2}, {2,3}|{1}, {3}|{1,2} | 3>1>2 only |
| BD | 3>1>2 | four types | 3>1>2 only |
| CD | 1>3>2 | four types | 1>3>2 only |

Each type occurs with both members as the answerer. Y is analogous: three pairs have a tie and two admissible orders, the others one (see the `.out` file).

**Reading.** When all four types occur, the type test pins the pair's constant vector to the open Weyl chamber of D. That fixes orderings across worlds, but leaves each world's interval position and width free.

## 4. The feasibility programme and the checkpoint (brief item 2)

**Programme.** The unknowns are integer log₂-fields per cell representative, integer log₂-constants per triple, and binaries choosing each model's dominant world per cell. Bayes is imposed in the sufficient form: the dominant world beats every opposing world by ≥ 2 in log₂, which with base 2 implies exact strict Bayes. CG2 is imposed with margin 1. This is a MILP (`prog51.py`).

It is only a sufficient relaxation, and §6 shows it is too strict to certify infeasibility. So I use it only to propose. The theorem and the exact verifier do the work.

**Theorem 4.1 (perturbation; PROVED).** Take four two-valued gated models, cell representatives, and the following data in log₂ units:
- integer global constants X and fields Y with tropical Bayes margin ≥ m and strict CG2 margin ≥ 1 against X;
- for each edge P→Q of an oriented 4-cycle at world w₀, a witness sub-cone in a cell where Q is w₀-worse than P, with CG2 slack exactly 1.

Let φ^τ_N be arbitrary integers with |φ^τ_N − φ^τ_M| ≤ 2s, where φ_Q − φ_P = s on each cycle edge in both triples containing it. Put x^τ := X + φ^τ, and take y := Y + ψ, where:
- generically, ψ = ∓s on correct worlds and ±s on wrong worlds (sign − for answerers, + for silents);
- at a witness sub-cone, at world w₀, ψ solves the one-directional system with the witness arc tight. Silents are set first and answerers take the largest allowed values, or vice versa at a wrong world.

If m ≥ 4s + 2, then:
- every Bayes and strict CG2 inequality holds exactly against every triple's constants;
- every triple passes the closed test with slack, so it is not tight;
- the realised cycle lower bounds sum to 4(s − 1) > 0 for s ≥ 2.

*Proof.*
1. At a cell and a world, the constraints are ψ^N − ψ^M ≤ b_NM (correct worlds) or ≥ b_NM (wrong worlds), with N ∈ 𝒜 and M ∈ 𝒮. Here b_NM = slack(Y) + min_τ φ-difference − 1, or the analogous max form.
2. The arcs run only from 𝒮 to 𝒜, so the system has no cycles and is always solvable.
3. The generic choice gives differences ∓2s, which beats |φ-difference| ≤ 2s plus the margin.
4. At a witness, b_PQ = s, so |ψ| ≤ 3s.
5. Each model's dominant-world margin therefore drops by at most 4s.
6. Triple slack: the constants x^τ sit at distance ≥ 1 from every realised bound. ∎

The φ used, 0, s, 2s along each triple's consecutive cycle edges (diagonals ±2s), is a discrete **vortex**: φ^τ = s × the angular position of the member around the cycle's centre, cut at the triple's largest gap.

**Theorem 4.2 (CHECKED, `construct51.out`).** For R and Y at ε = 3/10, the procedure gives, with m = 40 and s = 3:
- a MILP-proposed integer likelihood-type global witness;
- the perturbation of Thm 4.1, using a different oriented cycle per world where a world lacks witness cells for one orientation. For R these are ABCD at worlds 1 and 2 and ADCB at world 3.

The resulting designs satisfy all of (V1)–(V6) exactly:
- strict guidance;
- strict own-Bayes over all four advice values, with minimum tropical margin 28;
- realised intervals from the full fields;
- strict CG2 for every triple's constants;
- closed triple test with slack at every world;
- two-signedness.

**No global constants exist at worlds 1, 2 and 3.** The certificates are 4-cycles whose lower bounds on log₂(c_N/c_M) sum to 8. For R at world 1 the cycle is A→D→C→B→A, with bounds 43 + 84 − 39 − 80 = 8.

R's world-1 intervals, in log₂:

| AB | AC | AD | BC | BD | CD |
|---|---|---|---|---|---|
| [78, 80] | [116, 130] | [43, 45] | [37, 39] | [−48, −34] | [−725, −84] |

The edges are narrow and the diagonals wide, as Lemma 2.5 requires. The fields are 2^y·|g| on cells, with y ∈ [−403, 400]. They are exact but extreme, because the integer relaxation needs large margins. §7.2 shows that exact-Bayes LPs need only ratios of about e.

## 5. Explanation (brief item 3) and the kink obstruction

### 5.1 What forces global prices

At the four-model level, nothing does in fat configurations.
- **Own-Bayes:** weights are absorbed exactly (Lemma 2.1), and PP53 Lemma 3.1 adds pointwise rescaling.
- **Posterior geometry:** it constrains only orderings (chambers, §3). Through Lemma 2.3 it supplies a global witness, the likelihood witness, whenever every cell is separable by some n ∈ O_σ. That happens exactly in every fat arrangement tested (`linwit51.out`, `compare51.out`).
- **Acceptance:** the triple test is triple-local, and Thm 4.1 inserts holonomy.

**So the non-additivity in Thm 4.2 is installed by hand, not produced by the geometry.** The relevant question is what happens where the geometry itself defeats the likelihood witness.

### 5.2 The kink obstruction

**Theorem 5.1 (PROVED).** Consider three two-valued gated models A, B, D, with own-Bayes fields and positive constants passing the closed triple test at all three worlds. Assume own-Bayes is a.e. unique for A, or CG2 is strict a.e. on the two cells below. Fix a world i, let j, k be the other two, and put z^N := (ω^N_j/ω^N_i, ω^N_k/ω^N_i).

The configuration is impossible if all three of the following hold:
- **(K1) Two opposite cells.** There are two non-null cells in which A answers alone, with h's sign at i opposite to its signs at j and k: one with h_i < 0 ("above") and one with h_i > 0 ("below"). The same holds with "A silent alone" and the roles swapped.
- **(K2) Betweenness.** The pair type sets of (A,B) and (A,D) force z^B_j ≥ z^A_j ≥ z^D_j, or the reverse, for every admissible constant vector.
- **(K3) Two-signedness.** Every pair is two-signed at every world. This makes nonnegative solutions of Thm R1(ii) positive.

*Proof.*
1. By Lemma 2.3 applied to the triple, the "above" cell gives a positive linear form ℓ with ℓ(z^A) > θ ≥ max(ℓ(z^B), ℓ(z^D)).
2. The "below" cell gives a positive form ℓ′ with ℓ′(z^A) < θ′ ≤ min(ℓ′(z^B), ℓ′(z^D)).
3. Let S be the point of the segment [z^B, z^D] whose j-coordinate equals z^A_j; it exists by (K2).
4. If S_k ≥ z^A_k, then ℓ(S) ≥ ℓ(z^A) > θ ≥ ℓ(S). Otherwise ℓ′(S) < ℓ′(z^A) < θ′ ≤ ℓ′(S). Either way, contradiction.
5. So the closed test fails at some world. By Thm R1(ii) under (R), or PP47 Thm 4.1(a) under (R0), (TC) fails. ∎

**Instance (CHECKED, `kink51.out`).** At ε = 3/10, take A = u, B = (406, 421, 373)/1200 and D = (406, 373, 421)/1200. Then:
- lone world i = 1;
- the "above" cell has T answering h ∝ (−2387917/3240000000, 2384389/2160000000, 756973/1296000000), correct at {2, 3}, with B and D silent;
- the "below" cell has T answering h ∝ (6543/256000, −11939/1536000, −11939/1536000), correct at {1} only, with B and D silent;
- the admissible orders are log(ω^A/ω^B): 3>1>2 only, and log(ω^A/ω^D): 2>1>3 only. These force z^B_2 ≥ z^A_2 ≥ z^D_2.

In words: B and D lie far apart along e₂ − e₃, slightly offset towards e₁, and T sits between them. T answers alone on both sides of world 1, because the answer region of C_a in index space is a **wedge** (two vertex constraints active near a corner ray), not a half-plane. No single linear witness per triple can reproduce a wedge on both sides.

**Where it occurs (CHECKED, `kinkscan51.out`).** I scanned triples A = u, B, D = u + t(m ± L(0,1,−1)), with base half-length L and midpoint offset m.

| ε | m = (2,−1,−1) | m = (1,0,−1) | m = (−2,1,1) or m = 0 |
|---|---|---|---|
| 1/10 | from L = 24 | from L = 12 | never (L ≤ 32) |
| 3/10 | from L = 8 | from L = 5 | never |
| 1/2 | from L = 6 | from L = 3 | never |

- The kite8 instance persists at t = 1/400, 1/4000 and 1/40000.
- The odd model need not be T. In the arrangement rand1 at ε = 1/2 the obstructed triple has C as the odd model (`compare51.out`).
- Collinear triples never carry the certificate.
- R, Y and PP53's configuration carry none.

**Comparison (`compare51.out`, 17 arrangements × 3 ε).**
- Every arrangement with a kink-obstructed triple also lacks the likelihood witness, as it must.
- One arrangement (rand3) lacks the likelihood witness, through a degenerate cell, but has neither a kink nor any shortage of global witnesses (the tropical MILP finds one).
- I found **no** arrangement in which global prices fail for geometric reasons while (TC) stays feasible. CONJECTURE: in this architecture, posterior geometry yields either a global witness or a (TC) failure, never the checkpoint by itself.

CONJECTURE (scale invariance near u): for every ε ∈ (0, 1), every neighbourhood of u contains obstructed triples.

**Consequence (PROVED from the instances).** No gate-union design with own-Bayes gates can gate all posterior models near u, at ε ∈ {1/10, 3/10, 1/2}. The same holds for PP49's architecture, where every index is gated. Coherent selection a ↦ C_a on the whole simplex is therefore not realisable in this architecture.

This also answers the coordinator's framing. "Posterior gates always admit global prices" is **false**: they don't, in fat configurations (Thm 4.2, and PP53). But the geometric mechanism that defeats global prices, the wedge, also defeats (TC). The trade-off is quantified in §7.2.

**Gap.** Weak own-Bayes for T together with non-strict CG2 on a non-null part of both certificate cells is not covered. That case would need exact ties for T; compare PP47 Thm 2.5.

### 5.3 Nearby reachable aims (per the standing preference)

- **(a) Gate a kink-free sub-family.** `tripod51.out` (CHECKED) tested two straight lines through u (6 points each) and tripods made of u plus two radii on each of three rays (7 points). None of their triples carries a kink certificate. That is only evidence, not feasibility, because Thm 5.1 is a sufficient obstruction.

  If such a set is (TC)-feasible, Thm 4.1's vortex shifts can supply holonomy around u. The other posterior models would then be defended through designated realisers, which is the audit's selective branch. This keeps index = likelihood for the selection, but not "gate every index". Note that §7.2 shows how fragile the likelihood witness is once a set has more than five members.
- **(b) Adjust the family near corner rays.** The obstruction is the wedge of C_a's answer region in index space. A family whose answer region at each h is a half-space in index space would be kink-free. It would also have a likelihood-type witness everywhere, so Thm 4.1 would be the only source of non-additivity. Whether that is compatible with Thm N's requirement is OPEN.
- **(c) Close the weak-tie gap of Thm 5.1**, or exploit it. It is the only escape left inside the architecture.

## 6. The tropical relaxation is not a test

`survey51.out` runs the integer/tropical MILP (global constants G, triple constants T) on 17 arrangements × 3 ε. All "1" entries are sound: they give exact designs.

The "0" entries are **not** infeasibility claims:
- **kite4** (A = u, B = u + (2,3,−5)/400, C = u + (4,−2,−2)/400, D = u + (2,−5,3)/400). Its triple ABD alone is tropically infeasible, with an irreducible infeasible set of just three cells: B alone answering, correct at {2,3}; B and D answering, correct at {1}; D alone answering, correct at {2,3}. Yet its likelihood witness exists exactly (`linwit51.out`), so all of its triples are feasible. The reason is that tropical separators are 120° sectors, whereas exact separators are half-planes.
- **rand3** (ε = 3/10) has no likelihood witness (an exact Farkas vector, from a degenerate cell), but it has a tropical global witness and no kink.

So the exact statements in this note use Lemma 2.3 (LP per cell) and Thm 5.1, never the MILP's infeasibility.

## 7. The coordinator's requests

### 7.1 PP53 Thm 3.3, verified independently (CHECKED, `check_pp53.out`)

From PP53's JSON I took only data: indices, per-type magnitudes as exact binary floats, and weights. Everything else is my own code:
- exact cell enumeration: 28 disagreement types, identical to PP53's;
- my own completion of −h and contradictory values;
- guidance and strict own-Bayes at PP53's weights, on every cell;
- realised intervals from the full fields;
- the closed triple test with slack;
- the global certificate.

**Results.** All pass. The world-1 intervals agree with PP53's table to four decimals.
- World 1 has no global constants: cycle A→D→C→B→A with product of lower bounds e^0.2000.
- World 2 has none either: A→C→D→B→A, e^0.0983.
- World 3 is consistent; AC is one-signed there.
- The configuration has a likelihood witness and no kink certificate. **It is a fat configuration, like R and Y.**

### 7.2 Width budget, fifth and sixth members, smallest field ratios (`exactfit51.out`)

**Method.** Constants are fixed and rational:
  c^τ_{N,w} = q^{k_τ(N)·[w = 1]} / N_w,
with k_τ the vortex rank (likelihood × vortex).

For fixed constants, each cell is an LP in the field magnitudes E ∈ [1, K] with:
- exact strict Bayes (margin 10⁻⁴ relative);
- strict CG2 against every triple containing the pair (factor 1 ∓ 10⁻³);
- one witness sub-cone per cycle edge.

The LP minimises K, the largest within-cell field ratio. Solutions are rationalised and the whole design is re-verified by `verify51` (exact) for every triple, including those with the extra members.
- The fifth member E is the centre of PP53's parallelogram, (21, 21, 18)/60.
- The sixth member F is the outside point (9, 10, 11)/30.
- All six are two-valued.

PP53's configuration, cycle A→B→C→D→A at world 1. The configuration's size is its distance from u. Every row is an exactly verified design.

| size | members | largest feasible step log q | log q used | deficit Γ (w1) | log K | Σ widths to the cycle |
|---|---|---|---|---|---|---|
| 1/30 | A–D | 0.0476 | 0.0476 | 0.190 | 6.65 | — |
| 1/30 | A–D | | 0.0238 | 0.095 | 1.15 | — |
| 1/30 | A–D + E | 0.0231 | 0.0231 | 0.115 | 7.28 | E: 0.115 |
| 1/30 | A–D + E | | 0.0115 | 0.058 | 3.12 | E: 0.058 |
| 1/30 | A–D + E + F | 0.0146 | 0.0146 | 0.088 | 8.12 | E: 0.088; F: 0.088 |
| 1/30 | A–D + E + F | | 0.0073 | 0.044 | 3.23 | E: 0.044; F: 0.044 |
| 1/300 | A–D | 0.0049 | 0.0049 | 0.020 | 4.81 | — |
| 1/300 | A–D | | 0.0025 | 0.010 | 1.10 | — |
| 1/300 | A–D + E, and A–D + E + F | < 8·10⁻⁵ | not resolved at η = 10⁻⁵ | | | |

(E = (64,61,55)/180 lies strictly inside the cycle; F = (61,59,60)/180 lies outside, next to u.)

**Sixth members are delicate (`sixth51.out`, exact).** For 8 of the 9 candidate sixth members tried, the six-model set loses the likelihood witness. Each failure comes with an exact Farkas vector, at some one-world-correct cell. So the likelihood × vortex route does not scale freely with the number of members. Whether those six-model sets admit (TC) at all is OPEN. Neither kink certificates nor an ω-search were run on them.

**Readings.**
- **Width budget.** PP53 Lemma 3.4 is met, and with near equality: each extra member's widths to the cycle sum to Γ + O(10⁻⁴). That is what the vortex gives, because a member's intervals are hulls of rank differences over its triples. So the budget is necessary (PP53) and essentially attained by this construction. Each extra member costs deficit: the largest feasible step halves with E, and drops again with F.
- **Small ratios suffice.** A deficit of 0.095 needs within-cell field ratios of only e^1.15. Pushing the step to its maximum costs ratios of e^5–e^8. PP53's e^30 and my 2^400 come from their search formulations, not from the problem.
- **Scaling.** When the configuration is ten times closer to u, the largest feasible step and the deficit both drop by about ten (0.0476 → 0.0049; 0.190 → 0.020), at similar field ratios. So holonomy per loop scales with loop size, and its density per unit area grows like 1/size. This is NUMERICS for the trend; each design is CHECKED.

  This is the continuum datum the constructor needs. With constants of likelihood × vortex type, the holonomy a loop can carry is limited by the Bayes margins of the likelihood witness on the loop's cells. In these runs that limit is proportional to the loop's size. CONJECTURE: this holds in general.

  But by Thm 5.1, a full 2-D patch through u contains triples with no fields at all. **The question "how must the multipliers vary over a 2-D patch" has a negative answer in this architecture.** What survives is the kink-free sub-family route of §5.3(a).

## 8. Scripts (`r9/PP51_py/`)

Run `python3 -I -B <script> > <script>.out` inside the folder.

| Script | Content | Label |
|---|---|---|
| `post51.py` | exact posterior geometry; cell enumeration (vertex-ray sectors) | library |
| `arrangements51.py` | arrangements R, Y | data |
| `geometry51.py` | §3: cells, multi-model types, pair types, pair-ordering theorem, admissible orders; MC masses | CHECKED (masses NUMERICS); ALL PASS |
| `prog51.py` | tropical/integer MILP builder | proposes only |
| `verify51.py` | exact verifier (V1)–(V6), any number of members, log₂ or rational fields and constants | library |
| `construct51.py` | Thm 4.1 construction for R and Y; exact verification; certificates; `design51_{R,Y}.json` | CHECKED; ALL PASS |
| `linwit51.py` | likelihood witness per cell: rational P or an exact Farkas vector | CHECKED |
| `kink51.py` | Thm 5.1 certificates; R, Y clean | CHECKED |
| `kinkscan51.py` | §5.2 scan over shapes, ε, scales | CHECKED |
| `compare51.py` | likelihood witness against kinks on 17 arrangements × 3 ε | CHECKED |
| `survey51.py` | tropical survey (§6) | sufficient relaxation only |
| `check_pp53.py` | §7.1 independent verification of PP53 | CHECKED; ALL PASS |
| `exactfit51.py` | §7.2 exact-Bayes LP designs with 4–6 members; width budget; field ratios (bisection on the step is float LP; every reported design is verified exactly) | CHECKED (designs) |
| `sixth51.py` | §7.2 likelihood witness with a sixth member, nine candidates | CHECKED |
| `tripod51.py` | §5.3 kink certificates on straight lines and on tripods through u | CHECKED |

**Most important next step.** Decide between §5.3(a) and (b). For (a), test the posterior tripod: three straight rays through u, gated, with vortex holonomy around u. Check it for kink certificates on all triples, and check that designated realisers defend the ungated 2-D remainder.
