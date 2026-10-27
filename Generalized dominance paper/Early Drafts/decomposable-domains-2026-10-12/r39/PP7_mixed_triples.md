# PP7. Mixed triples: additive-first allocation with symmetric thinning

21 October 2026, Round 39 (construction test). Labels:
- **PROVED**: the full argument is given here. One reader (me); not refereed.
- **CHECKED**: an exact finite computation.
  - Rivals are built on exact rational cones.
  - Masses are interval solid angles (mpmath.iv, 40 digits); L_i comes from PP6's perimeter formula in interval arithmetic.
  - Guidance is tested exactly on cells, and anchor polygons are exact.
  - SAT verdicts come from an exact clause encoding. Every UNSAT verdict is re-run on interval masses with all signs certified, and confirmed where stated by a second, independent search.
- **NUMERICS**: the same exact geometry, but with double-precision solid angles (determinants and dot products are taken exactly on the integer rays, then rounded). This is pool evidence, not proof.
- **OPEN**.

**Grid and pool success is NUMERICS, not proof. Certified violations and UNSAT certificates are CHECKED.**

Family: K_p = p + 3ε min_j p_j (Δ − u), C_p = D_{K_p}, with ε = 0.3 and 0.1. Centres:
- near e₁: p₀ = (.9, .06, .04), off the symmetric line;
- near u: p₀ = (.35, .33, .32).

Scripts are in `PP7_py/` (`python3 -I <script>` inside that folder; outputs in `*.out`). I add no assumption to the programme.

---

## 0. Verdicts

**The rule tested is the brief's.**
- Eligibility pool: Φ⁴_i = 4ν(P_i) − ν(Q_i) ≥ 0.
- Additive-first (AF): accept at every world with add_i = ν(P_i) − ν(Q_i) ≥ 0. When every add_i < 0 (the *sticky branch*), accept at any chosen subset of the eligible worlds.
- Guidance: always accepted.
- Repairs: only *symmetric thinning*, i.e. remove a record and its reverse at one world, keeping every face obligation of both directions.

**1. No stable allocation exists. The cascade terminates, but it ends blocked.**
- Thinning only removes acceptances, so every repair sequence stops.
- I encoded *every* state such a sequence can reach: all symmetric thinnings and all sticky subsets. The encoding is UNSAT, so every order of repair ends with a violation that cannot be repaired without breaking an obligation.
- **PROVED (Theorem 4.2), with no numerical hypothesis.** At every interior selected model C_{p₀}, for every 0 < ε < 1, AF with symmetric thinning cannot satisfy (TC) together with the defence clause of (S). The witness is a 3-parameter family of nested PP5-type rivals spliced onto C_{p₀} on arbitrarily small cones.
- **CHECKED (`t8`).** In all four settings, C_{p₀} plus 8 nested rivals is UNSAT, confirmed independently by an exhaustive colouring search. Deletion-minimal cores have **one selected model and six spliced rivals**.
- **Second mechanism.** It runs through the selected layer instead (Theorem 4.4 PROVED under a NUMERICS hypothesis; `t3` CHECKED).
  - One rival suffices, against 14–15 selected models.
  - Mixed cores have 2 selected models and 6–8 rivals (`t6`, CHECKED).
- Undominatedness, direct (C) and closedness are never used. Every UNSAT holds without them.

**2. Minimal configurations, by level.**

| level | configuration | under AF | repairable by symmetric thinning? |
|---|---|---|---|
| (a) pair | C_q and a rival Y that additively dominates it (PP5's silence→majority) | Y ⪯_i C_q at every world, so undominatedness forces an all-world tie, which direct (C) forbids (Y certified incoherent) | **yes** (CHECKED) |
| (b) pump | (X, C_q, Y) with X = Y plus a tiny pure worsening | X ⪯_j C_q ⪯_j Y ≺_j X at every defending world j | **yes** (PROVED; CHECKED: SAT on the full single-base pump configuration) |
| (c₁) guidance-gluing | (Y(t′), C_q, Y(t)) for nested sticky rivals | defences are ties (Lemma 4.1); two rivals tied with C_q at world w and ordered by guidance at w violate (TC) | **no**. Theorem 4.2, PROVED. Core: C_q + 6 rivals (CHECKED) |
| (c₂) selected gluing | (C_{q′}, Y, C_q) with Y additively dominating both | ties through Y force world j to drop the selected link, and W_add's lonely-world obligation forbids that | **no**. Theorem 4.4. Core: 14–15 selected + Y (CHECKED) |

- Random small modifications, splices of two selected models, and returns produce maximal-AF violations of every triple type. With no additively dominating rival among them, all 8 tested pools are repairable. Every repair but one is a sticky deselection of a record that does not come out of a selected model; the exception is a single pair-level tie thinning (NUMERICS, §5).
- **The driver is a rival that additively dominates a selected model.** FF2 Thm 4.1 guarantees such rivals at every interior index. PP5 Prop 4.3 gives them explicitly, at any small mass.

**3. Non-additive defences.**
- The defence clause forces sticky (non-additive) acceptances out of selected models: rec(C_q, Y) has all add < 0 and q ∈ A(rec(C_q, Y)).
- A purely additive rule leaves C_q dominated by Y (Prop. 2.1). So repairs cannot push the rule back to additive.
- Under AF, every sticky defence is a tie (Lemma 4.1), and the ties glue (level c).
- So AF with symmetric thinning can neither drop the non-additive defences nor keep them.

**4. The nearby reachable rule: sticky-strict.**
- **Change:** at a world where a sticky record is accepted, the additive reverse may be refused on its own. The defence C_q ≺_j Y is then strict, not a tie.
- **NUMERICS.** Sticky-strict is SAT on every configuration where AF with symmetric thinning is UNSAT. Its solutions re-check with 0 (TC) violations, all obligations met, no domination and no ties. This covers:
  - the single-base cores;
  - the t3 lattices;
  - the dense mixed pool;
  - the boundary-crossing rival families.
- **I propose shifting the aim to this rule.**
- **OPEN.**
  - Closedness at the boundary of the sticky branch.
  - A record-level statement of the return quarantine it needs.
  - Screens S9 and (P).
  - Its global reading as a per-world non-additive value for rivals (§6–8).

---

## 1. Setting

- **Verdicts.** For d = rec(X,Y): add_i = L_i(Y) − L_i(X), with L_i(X) = ν(U_i(X)), and Φ⁴_i = 4ν(P_i) − ν(Q_i).
- **AF's base verdict at world j.** It is one of:
  - G (guidance: Q_j null; exact cell test);
  - A (add_j ≥ 0);
  - S (every add < 0 and Φ⁴_j ≥ 0; acceptance free);
  - refused.
  - Among selected models AF is W_add (PP6), because no selected model is additively dominated by another on any lattice used (certified).
- **Rivals.** A rival is a selected base with its advice overridden on exact simplicial cones; each cone changes together with its antipode. Types:
  - **R**: random small modifications to A, S, B or contradiction;
  - **SP**: splices, i.e. C_p with C_q's advice on cells of D(C_p, C_q);
  - **ST / Y**: PP5 sticky rivals, i.e. silence → A on cones S₁, S₂, S₃ in the three classes' silent regions;
  - **RT, Z_j**: returns, i.e. the base improved at one world on a tiny cone;
  - **Xc, Xu**: Y plus contradiction, or Y plus silence on unanimous problems.
- **Face obligations.** Exact anchor polygons A(d) for an arbitrary old side (PP5's per-ray linear constraints, on arrangements that include the diagonal planes). A record whose old side is contradictory somewhere on D has A(d) = ∅.
- **Incoherence.** Certificates follow HH3 Lemma 1.2.
- **SAT (`pool.py`).** Variables: thinning per (world, unordered pair) and sticky choice per (world, record). Clauses:
  - (TC) on every ordered triple at every world;
  - every face obligation;
  - undominatedness of each selected model;
  - direct (C) against certified-incoherent rivals.

  UNSAT means that no removal-only repair sequence ends stable.
- **Code audit.** Two bugs were found during the round and fixed before any reported run: a clause filter that dropped clauses containing literal 1, and a float overflow on huge integer rays. Every SAT state reported is re-checked by an independent brute-force checker.

---

## 2. Level (a): the pair

**Proposition 2.1 (PROVED).** Let Y additively dominate a selected C_q, i.e. every add_i(rec(C_q,Y)) < 0. Under AF, before thinning:
- Y ⪯_i C_q at every world;
- undominatedness then forces C_q ⪯_i Y everywhere, i.e. an all-world tie;
- direct (C) then forces Y to be coherent and undominated.

*Proof.* add_i(rec(Y,C_q)) = −add_i(rec(C_q,Y)) > 0 at every i. ∎

**CHECKED (`t1_pairs_pumps.py`).** Y = C_{p₀} with A on one exact cone in each class's silent region, with balanced masses m.

| centre, ε | m (problem mass per cone) | add(rec(C_{p₀},Y)) | Φ⁴ (each world) | A(rec(C_{p₀},Y)) meets | A(rec(Y,C_{p₀})) | Y incoherent |
|---|---|---|---|---|---|---|
| e₁, .3 | 6.633e-4 | −m at each world | 2m > 0 | full face only | ∅ | certificate |
| e₁, .1 | 1.888e-4 | −m | 2m | full | ∅ | certificate |
| u, .3 | 6.713e-3 | −m | 2m | full | ∅ | certificate |
| u, .1 | 2.277e-3 | −m | 2m | full | ∅ | certificate |

**The repair is available.** The reverse has no obligation, so thinning {C_{p₀}, Y} at one world removes the tie at no cost.

---

## 3. Level (b): pumps (X, C_q, Y)

**Proposition 3.1 (PROVED).** Suppose world j accepts C_q ⪯_j Y with add_j(rec(C_q,Y)) < 0. Let X be a strict pointwise world-j worsening of Y with L_j(X) − L_j(Y) < −add_j(rec(C_q,Y)). Then X ⪯_j C_q, which AF accepts additively, must be refused at j.

*Proof.* AF accepts X ⪯_j C_q additively, and Y ≺_j X by strict (G), giving X ⪯_j C_q ⪯_j Y ≺_j X. ∎

**The two kinds of partner X.**
- For X = Y plus contradiction, A(rec(X,C_q)) = ∅, so the thinning is free.
- For regular worsenings, the return is additively safe at the other worlds.

**CHECKED (`t1`, 10 models: C_{p₀}, Y, Xc, Xu, Z₁₋₃, YZ₁₋₃).**
- Maximal AF has 242–261 (TC) violations, 86–90 of which contain C_{p₀}. Every violation has exactly one sticky link (patterns ASG, SAG, ASA, SAA). There are also 6 incoherent all-world ties.
- **Exact SAT: SAT in all four settings.** The state re-checks clean: 0 TC, 0 obligations, 0 dominated, 0 ties.
- In it, C_{p₀} keeps one sticky defence per sticky rival, spread over the worlds, and 26 additive returns are thinned.
- Greedy repair stalls; that is an artefact of the order.

---

## 4. Level (c): gluing

### 4.1 Ties

**Lemma 4.1 (PROVED).** Suppose every add_i(rec(C_q,Y)) < 0 and world j accepts rec(C_q,Y) in a final state. Then j also accepts rec(Y,C_q), so C_q ≈_j Y.

*Proof.* The reverse has add_j > 0, so AF accepts it, and only a symmetric thinning removes it. ∎

### 4.2 Guidance-gluing with one selected model (no hypothesis)

**Theorem 4.2 (PROVED).** Let p₀ be interior and 0 < ε < 1. No allocation of the form "AF + symmetric thinning + any sticky subset" satisfies, on the models C_{p₀} and the rivals Y(t) below:
- strict (G);
- (TC);
- the defence clause q ∈ A(rec(C_q, ·)) at q = p₀.

**Construction.**
- int K_{p₀} ≠ ∅, so C_{p₀} is silent on a non-null open set of lines in each class M_w (PP5 Prop 4.3).
- Choose closed simplicial cones T_w inside silent cells, with equal masses m. Let S_w(t) be the cone shrunk towards T_w's centre by t ∈ (0,1]. These cones are nested: S_w(t) ⊊ S_w(t′) with difference of positive measure for t < t′, and their mass μ_w(t) is continuous.
- Y(t) := C_{p₀} with A on S₁(t₁) ∪ S₂(t₂) ∪ S₃(t₃).
- add_i(rec(C_{p₀},Y(t))) = μ_i(t_i) − Σ_{w≠i} μ_w(t_w), which equals −m at t = (1,1,1). So every add_i < 0 on an open box U ⊂ (0,1]³ near (1,1,1).

*Proof.*
1. **Every rival needs a tied defence.** For t ∈ U the record rec(C_{p₀},Y(t)) is sticky, and p₀ ∈ A(rec(C_{p₀},Y(t))) with p₀ interior. So some world c(t) accepts it, and by Lemma 4.1 C_{p₀} ≈_{c(t)} Y(t).
2. **Guidance between rivals.** For u, v ≠ w, world w is in the majority in M_u and M_v, and in the minority in M_w. Suppose t ≠ t′ with t_u ≥ t′_u, t_v ≥ t′_v and t_w ≤ t′_w. Then Y(t) is a strict pointwise world-w improvement of Y(t′): it has more good A-lines in M_u and M_v and fewer bad ones in M_w. So Y(t) ≺_w Y(t′) by (G), and this link can never be thinned. Call this order ≤_w.
3. **Same colour forbids comparability.** If c(t) = c(t′) = w and t, t′ are ≤_w-comparable, say Y(t) ≺_w Y(t′), then Y(t′) ⪯_w C_{p₀} ⪯_w Y(t) ≺_w Y(t′), violating (TC). So each colour class c⁻¹(w) is an antichain of ≤_w.
4. **Antichains are thin.** ≤_w is a coordinatewise order on ℝ³ after reflecting one coordinate. If x, y lie in an antichain, x − y lies in no closed orthant of that order. Those orthants contain the circular double cone of half-angle arcsin(1/√3) around the reflected diagonal d. Hence the antichain projects injectively onto d^⊥, with a Lipschitz inverse. By McShane extension it lies in a closed Lipschitz graph, which is Lebesgue-null.
5. **Contradiction.** U is covered by three null closed sets, which is impossible. ∎

**Remarks.**
- The theorem uses neither W_add, nor (AC), nor the pool size, nor undominatedness, direct (C) or closedness.
- It uses only:
  - Lemma 4.1 (AF accepts the additive reverse);
  - guidance with strict (G);
  - the trivial anchor.
- The rivals can be taken at any small mass, so the obstruction is local at *every* interior selected model.

**CHECKED (`t8_single_base.py`).** Grid t ∈ {1, 9/10}³, so 8 rivals plus C_{p₀}.
- All masses are interval-certified, and every rival certifiably dominates C_{p₀} additively.
- The exact guidance pattern among rivals equals the predicted product-order pattern (0 mismatches, 45 strict guidance links).

| centre, ε | max over rivals of max_i add_i | exact SAT (all states) | same, without undominated / direct (C) | guidance-colouring search (independent) | deletion-minimal core |
|---|---|---|---|---|---|
| e₁, .3 | −4.14e-4 | **UNSAT** | **UNSAT** | no colouring | C_{p₀} + 6 rivals |
| e₁, .1 | −1.18e-4 | **UNSAT** | **UNSAT** | no colouring | C_{p₀} + 6 |
| u, .3 | −4.19e-3 | **UNSAT** | **UNSAT** | no colouring | C_{p₀} + 6 |
| u, .1 | −1.42e-3 | **UNSAT** | **UNSAT** | no colouring | C_{p₀} + 6 |

The 6-rival cores (e.g. Y001, Y010, Y011, Y101, Y110, Y111, where digit k indexes S_k's shrink parameter and 0 is the largest cone) also use the obligations of rival-to-rival records.
- By (IB) these are records out of C_{p₀}: D is an annulus on which the old side agrees with C_{p₀}. Some of them are anchored at vertices too, and guidance meets those.
- Dropping these obligations makes the 6-rival core SAT. The 8-rival set is refuted by guidance alone.

### 4.3 Selected-model gluing (one rival, many selected models)

**Lemma 4.3 (PROVED).** Suppose world j accepts both sticky records rec(C_q,Y) and rec(C_{q′},Y), and L_j(q) < L_j(q′). Then j must refuse rec(C_q, C_{q′}).

*Proof.* Otherwise C_{q′} ⪯_j Y ⪯_j C_q ≺_j C_{q′}, using Lemma 4.1 for the middle link and (AC) for strictness. ∎

**Lonely worlds.** For distinct interior q, q′, W_add splits the worlds 2 + 1. The singleton direction cannot be thinned, because q ∈ A(rec(C_q,·)) needs some accepting world. Call its world λ(q,q′).

**Colouring criterion.** A final state yields a colouring c of {q : Y dominates C_q additively} with c(q) = c(q′) = j only if j ≠ λ(q,q′).

**Theorem 4.4 (PROVED, given hypothesis H).**
- **(H)** p₀ is interior with a unique minimum coordinate, and ∇L(p₀) has a strictly positive normal.
- **Conclusion.** No AF + symmetric-thinning allocation exists near p₀.

*Proof.*
1. Under (H), world j is lonely on an open double cone Γ_j of displacement directions.
2. By real-analyticity of L off the chamber boundaries, this holds uniformly for pairs in a ball B ⊂ N(Y).
3. So c⁻¹(j) ∩ B has no two points with difference in Γ_j. Such a set lies on a Lipschitz graph, which is null.
4. Three null sets cannot cover B. ∎

(H) is NUMERICS: it holds at PP6's 7,021 points, and here (`t7_sectors.py`):

| centre, ε | λ (normalised) | lonely-sector widths per side (deg) |
|---|---|---|
| e₁, .3 | (.388, .303, .310) | 65.3, 55.5, 59.1 |
| e₁, .1 | (.412, .339, .249) | 65.0, 71.2, 43.7 |
| u, .3 | (.293, .287, .420) | 55.1, 52.5, 72.3 |
| u, .1 | (.332, .323, .345) | 60.8, 58.2, 61.0 |

**CHECKED (`t3_tieglue.py`).** Y has balanced masses m (as in §2). The selected models are q = p₀ + h(i(1,−1,0) + j(1,0,−1)) with |i|, |j| ≤ 3, all certified to lie in N(Y). The encoding is the weakest one: sticky acceptance at all three worlds, full-face obligations only, no undominatedness or direct (C).

| centre, ε | h | selected layer alone | with Y | deletion-minimal core | colouring search on core |
|---|---|---|---|---|---|
| e₁, .3 | 8.85e-5 | SAT | **UNSAT** | 14 selected + Y | no colouring (3,115 nodes) |
| e₁, .1 | 2.81e-5 | SAT | **UNSAT** | 14 + Y | none (1,498) |
| u, .3 | 4.65e-4 | SAT | **UNSAT** | 14 + Y | none (3,133) |
| u, .1 | 1.42e-4 | SAT | **UNSAT** | 15 + Y | none (2,974) |

The cores and the lonely world of every core pair are in `t3_tieglue_cores.txt`.

**Remark (beyond AF's selected layer).** The argument of Theorem 4.4 does not need W_add. It needs only that every world is strict on some open double cone of displacement directions near p₀.
- PP6 §2.2 (NUMERICS) shows that this is forced at generic interior points and near u.
- Near e₁ PP6 allows one world to be locally inactive; that world could absorb all tied defences, but only with a non-W_add selected layer.
- In any case, Theorem 4.2 needs no selected layer at all.

### 4.4 Mixed small cores (`t6_onesided.py`, CHECKED)

A 3×3 selected lattice, with Y, Xc, Z_j, YZ_j and PP5's family (m, sm, sm) for s = 0.7, 0.55, 0.45, 0.3 in two class arrangements.
- AF with symmetric thinning is UNSAT in every setting.
- The deletion-minimal cores are re-run with interval masses: UNSAT, with all signs certified, also without undominatedness and direct (C).


| centre, ε | deletion-minimal core |
|---|---|
| e₁, .3 and e₁, .1 | C7, C8 + Xc, YZ₁, YZ₂, YZ₃, Y₂₃(.7), Y₁₃(.7), Y₁₃(.55), Y₁₃(.45): 2 selected + 8 rivals |
| u, .3 | C7, C8 + Y, YZ₁, YZ₂, Y₂₃(.7), Y₁₃(.7), Y₁₃(.55): 2 + 6 |
| u, .1 | C7, C8 + Y, YZ₁, YZ₂, YZ₃, Y₂₃(.7), Y₁₃(.55): 2 + 6 |

These cores combine both gluing mechanisms. The rivals are partly ordered by guidance, and partly tied through the two selected models. The member Y₁₃(.45), which is sticky against only 2 of the 9 selected models, enters one core.

---

## 5. Mixed pools (NUMERICS; `t4_mixed_pool.py`, `t5_dense_pool.py`)

Each pool is 7 selected models (p₀ and a hexagon) plus 11–12 rivals. Counts are maximal-AF (TC) violations by triple type: two selected and one rival is "(C_q,C_p,X)"; one selected and two rivals is "(X,Y,C_p) / (C_p,X,Y)".

| pool | sticky records out of selected | violations (two sel. / one sel. / rivals only) | greedy cascade | exact SAT |
|---|---|---|---|---|
| e₁ .3, R+SP+RT, seed 1 | 0 | 25 / 113 / 80 | stable (51 sticky deselections) | SAT |
| e₁ .3, R+SP+RT, seed 2 | 0 | 56 / 206 / 138 | stable (63 + 1 tie thinning) | SAT |
| e₁ .3, ST+R+SP+RT | 12 | 97 / 287 / 142 | blocked at C0 ⪯₃ ST9 ⪯₃ C5 ≺₃ C0 | SAT |
| u .3, R+SP+RT, seeds 1, 2 | 0 | 0 / 4 / 9 and 0 / 0 / 0 | stable | SAT |
| u .3, ST+R+SP+RT | 6 | 40 / 125 / 68 | blocked (gluing) | SAT |
| e₁ .1, R+SP+RT, seeds 1, 2 | 0 | 13 / 57 / 46 and 15 / 81 / 55 | stable | SAT |
| e₁ .1, ST+R+SP+RT | 6 | 35 / 75 / 31 | blocked (gluing) | SAT |
| u .1, R+SP+RT, seeds 1, 2 | 0 | 1 / 10 / 6 and 0 / 0 / 0 | stable | SAT |
| u .1, ST+R+SP+RT | 4 | 19 / 91 / 58 | blocked (RT ⪯₃ ST9 ⪯₃ C6) | SAT |

**Dense pool (`t5`, e₁, ε = .3).** 49 lattice models, Y, Xc, Xu, returns, three random modifications and two splices.
- Maximal AF: 16,055 violations and 147 incoherent ties.
- Greedy repair stalls at C1 ⪯₃ Y ⪯₃ C7 ≺₃ C1.
- **Exact SAT: UNSAT.** Deleting rivals one by one leaves a single rival (Xu, itself a dominating sticky rival).
- Sticky-strict: SAT. It re-checks clean, with 148 strict sticky defences and 509 refused additive acceptances.

**Readings.**
- Random modifications, splices and returns create ASA / SAA violations of both mixed types. These are always cured by deselecting a sticky record that does not come out of a selected model.
- Sparse pools pass even with sticky rivals, because seven points can still be coloured. This is misleading: dense pools fail, as the theorems require.

---

## 6. The nearby rule: sticky-strict (NUMERICS)

**Variant.** An additive record d may be refused at world j on its own if rev(d) is in the sticky branch. Everything else is as before.

| configuration | AF + sym. thinning | sticky-strict | re-check of sticky-strict state |
|---|---|---|---|
| t8 single base (4 settings) | UNSAT | SAT | 0 TC, 0 obligations, 0 dominated, 0 ties |
| t3 lattices, selected layer frozen at W_add (4 settings) | UNSAT | SAT | clean; defended sets are L_j-sublevel sets |
| t6 boundary-crossing families (4 settings) | UNSAT | SAT | clean; 81 strict sticky defences, 0 ties |
| t5 dense pool | UNSAT | SAT | clean |

**What it costs.**
- A strict defence C_q ≺_j Y forces world j to refuse Y ⪯_j X for every X that j ranks at or above C_q. This is a return quarantine of Prop. 3.1 type, propagated along guidance and along W_add.
- In the solutions, world j behaves as if each rival Y had a value θ_j(Y) ≥ L_j(Y) placed in its L_j-order.
- Locally the rule is therefore **a per-world non-additive value for rivals**. Its premium θ_j − L_j must be a function of records under (IB).

---

## 7. Closedness (argued; not testable on finite pools)

- **AF.** The accepted sets are closed: add and Φ⁴ are ρ-Lipschitz (constants 6 and 15), and guidance is closed.
- **Symmetric thinning.** Removing an open, reversal-symmetric set keeps them closed (audit's Theorem 4).
  - The level (a) and (b) repairs are such sets: balls around rec(Y,C_q), and unions of balls around returns.
  - The returns accumulate on rec(Y,C_q), which may remain accepted, and a refused open set may do that.
- **Level (c) is not a closedness issue.** It is a finite contradiction between (TC) and obligations, certified on exact records. No choice of neighbourhoods avoids it.
- **Sticky-strict.** The refusal set rev(Sticky_j) must be open, while Sticky_j itself is closed. The consistent version:
  - refuses only on the open interior of the sticky branch;
  - ties on its boundary.

  The boundary is lower-dimensional, so the null-set arguments of §4 do not apply to it. Whether a finite certificate lives on the boundary is OPEN.

---

## 8. Answers to the brief

1. **Stable allocation, or a non-terminating repair cascade?**
   - **Neither.** The removal-only cascade terminates and ends blocked, at every interior selected model.
   - PROVED: Theorem 4.2, with no hypothesis.
   - CHECKED: near e₁ and near u, at ε = 0.3 and 0.1.
   - Stable outcomes on sparse or random pools are NUMERICS only, and misleading.
2. **Minimal configurations.**
   - One selected model plus six nested sticky rivals (guidance-gluing).
   - One sticky rival plus 14–15 selected models (selected gluing).
   - 2 selected models plus 6–8 rivals (mixed).
   - Pairs (a) and pumps (b) are repairable sub-mechanisms.
3. **Non-additive defences.**
   - Repairs do not push the rule back to additive: a purely additive rule leaves selected models dominated (Prop. 2.1).
   - Under AF the required non-additive defences are ties, and the ties make the system inconsistent.
   - On finite pools a positive-field test cannot decide non-endorsement (PP3: finite cells do not discriminate). Non-additivity is forced by FF2 Thm 4.1, not shown here.
4. **Proposed shift (nearby result).** Replace "symmetric thinning only" by **sticky-strict**: at the defending world, a sticky defence is a strict preference. This is the minimal change that defeats every obstruction found here (NUMERICS).
5. **Open for the next round.**
   - (i) A closed, record-based formulation of sticky-strict, including its boundary ties.
   - (ii) Its quarantine as a record-level rule.
   - (iii) S9: the refusal is triggered by an additive pattern ("the reverse is sticky"), so anchoring must be checked.
   - (iv) PP4's (P), between strict defences and returns.
   - (v) FF2 Cor 4.3: some world's values θ_j cannot come from one positive field.

---

## 9. Scripts (`PP7_py/`)

| script → output | content | label |
|---|---|---|
| `core.py` | family for general ε; rivals on exact cones; records by exact cells (float or interval); general anchor polygons; interval perimeter formula; exact cone carving and nested shrinking | library |
| `pool.py` | AF verdicts, guidance, faces, incoherence certificates; exact SAT over all symmetric-thinning states (+ sticky subset, undominated, direct (C), optional sticky-strict); independent checker; greedy cascade | library |
| `t0_validate.py` → `.out` | reproduces PP5's certified rec(C_a,C_b) (10 digits); L_iv agrees with cells to 12 digits | CHECKED |
| `t1_pairs_pumps.py` → `.out` | levels (a) and (b) | CHECKED |
| `t3_tieglue.py` → `.out`, `t3_tieglue_cores.txt` | selected gluing: lattices, cores, colouring search; sticky-strict with W_add frozen | CHECKED (sticky-strict: NUMERICS) |
| `t4_mixed_pool.py` → `t4_mixed_pool_*.out` | random pools: violation types, cascades, SAT | NUMERICS |
| `t5_dense_pool.py` → `.out` | dense mixed pool: UNSAT, single-rival core, sticky-strict | NUMERICS |
| `t6_onesided.py` → `t6_onesided_all.out` | mixed small cores (interval re-run); sticky-strict on boundary-crossing families | CHECKED (cores) / NUMERICS |
| `t7_sectors.py` → `.out` | hypothesis (H) of Theorem 4.4 | NUMERICS |
| `t8_single_base.py` → `t8_single_base_all.out` | guidance-gluing at one selected model: UNSAT, colouring search, cores, obligation dependence; sticky-strict | CHECKED (sticky-strict: NUMERICS) |
