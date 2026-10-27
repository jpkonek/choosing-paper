# HH3 (round 36, BRIEF28, audit item 4). The exact finite search, adapted to the non-transitive question: every fragment is satisfiable under (FC), (TC) and transitivity alike; what four selected models do obstruct is strict additive Bayes realisation

18 Oct 2026. Rules of BRIEF13 and BRIEF28. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports keep their recorded status.
- **CHECKED**: exact computation (rational or integer arithmetic, or an exactly verified rational certificate),
  reproducible from a script in `hh3py/`.
- **NUMERICS**: heuristic search or sampling about an infinite object; nothing rests on it.
- **CONJECTURE**.

Scripts are in `hh3py/` (run `python3 -I <script>.py` from inside it; outputs are the `*.out` files there; rational
certificates are in `hh3py/certs/`). `arr3.py` is an adapted copy of `ff1py/arr.py` (itself adapted from
`ee2py/cells.py`); nothing in `ff1py/` or `ee2py/` was modified. No assumption is added: every extra hypothesis is a
hypothesis of a stated result, and the two finite *proxies* of §7 are labelled as proxies wherever they occur.

---

## 0. Outcome

1. **The search (§§1–2).** I built an exact SAT formulation of the brief's question on finite fragments of the
   full four-advice domain. The ingredients are:
   - finitely many selected models C_p of the plain posterior family, including T1 = C_u, plus vertices and boundary
     points where stated;
   - a finite set of competitor models, all measurable for the exact cell arrangement of the selected models;
   - one Boolean variable per (world, transition record). (IB) is therefore built in: two pairs share a variable
     exactly when their records are equal a.e., that is, when they have the same support and the same before/after
     advice on every non-null cell.

   The constraints are reflexivity, strict (G), joint competitiveness, undominatedness of every selected model, and
   direct (C) on certified-incoherent models. The no-reversal condition is added lazily as cuts: strict cycles found
   by directed reachability for (FC), strict 3-cycles for (TC), and transitivity for the transitive comparison (TR).
   Minimal UNSAT cores are extracted over the requirement groups.

   Every constraint used in §§3–6 is a necessary condition on the restriction of any full system with the plain
   selection (Lemma 1.1; PROVED).
2. **Every fragment is satisfiable, in all three modes (§3; CHECKED per fragment).**
   - There are 12 fragments: six complete cell worlds (every cell-measurable model; each run with all ordered pairs,
     up to 4096 models and 531 440 records per world, and also with the pairs C_p × N), sparse fragments with up to
     3 832 models and 53 592 comparison edges, fragments with vertices, the boundary grid Δ ∩ (1/6)ℤ³, and a
     fragment built around the §6 certificate. They cover ε ∈ {1/10, 3/10, 1/2} and steps from 1/6 down to 1/1000.
   - Every fragment is SAT in every mode run: (FC), (TC) and (TR) on all of them, except that (TC) was not run on the
     second hexR1 fragment.
   - On every fragment where I ran the test (10 of them), an **additive** system with *strict* competitiveness also
     exists (exactly verified rational cell witnesses). It is transitive and complete, and gives all of (FC), (TC),
     (TR), undominatedness and (C) on the fragment.
   - So no fragment produced an UNSAT core under (FC), (TC) or (TR). Transitivity is never what makes a fragment hard.
3. **Why no certificate can appear on these selected sets (§5; PROVED, with CHECKED input).** For the selected sets
   hexR1 and hexR2 around u (ε = 3/10 and 1/10; steps 1/20, 1/100, 1/1000), exact rational weights q^p and cell
   vectors w_c exist that realise every C_p as the a.e.-unique q^p-Bayes model of **one** bounded strictly guiding
   additive ranking on the full domain (Proposition 5.1).
   - In that ranking each C_p is competitive on Ω against **every** evaluable model, is undominated, and is tied at
     every world with no other model.
   - Hence no fragment whose selected models lie in such a set can be UNSAT, in any mode, whatever its competitors
     or comparison pairs. Refining the competitors or the grid of competitor models can never help.
   - The ranking is not a cover: off the selected set its Bayes models are cell-measurable and generically
     incoherent. This is exactly where gm bites.
4. **What four selected models do obstruct (§6; PROVED, with CHECKED certificates).**
   - **Theorem 6.1.** For ε = 3/10, take the hexagon of radius 3 around u, at any step 1/200, 1/2000 or 1/20000.
     It contains four selected models, T1 = C_u among them, that are **not simultaneously a.e.-unique Bayes models of
     any additive ranking with integrable penalties, at any weights**. The proof is Radon's theorem applied to seven
     explicit rational problems.
   - The same holds for ε = 1/2 already on the radius-2 hexagon, and at ε = 3/10 on the radius-2 hexagon centred at
     (1/5, 3/5, 1/5). No four-model certificate was found at ε = 1/10: none in the radius-2 or radius-3 hexagons,
     and none containing u in the radius-4 hexagon (step 1/1000). There is none in the radius-2 hexagon at u for
     ε = 3/10 either, where the full selected set is in fact realisable (item 3).
   - The certificate is scale-invariant: the same four offsets at all three steps.
   - This is a finite, exact witness that the plain selection near T1 cannot be realised by the a.e.-unique Bayes
     models of any additive ranking. It needs only four selected models.
   - It is **not** a certificate against (FC) or (TR). It is about Bayes structure, which binds an additive world
     only through Lyapunov convexity: for additive rankings, competitiveness against all measurable models forces
     Bayes. Non-additive worlds, transitive or not, are not bound by it. On a
     fragment built around the certificate, all three modes are again SAT (§6.3).
5. **The required reports.**
   - **Structure of the satisfying systems (§4).** (FC) solutions are far from transitive: up to 8 337
     non-transitive triples per world on sparse fragments, and up to 1.8 million non-transitive pairs per world on
     complete cubes. They carry many incomparabilities and few ties. None of the solutions returned is exactly
     additive. Some are additively Suzumura-extendable at one or more worlds, some at none (sparse fragments), and on
     the complete 4096-model cubes at every world. But on every fragment a different, additive solution also exists,
     so none of these non-transitive features is forced.
   - **(TC)-only solutions have longer strict cycles, reported explicitly (§4.2; CHECKED).** For example, on the
     hexR1 fragment the world-1 cycle F(C4; c79) → C4 → F(C0; c8) → C1 → F(C4; c79) has its first edge strict by
     guidance. It contains no strict 3-chain.
   - **Proxies (§7).** The closed-section proxy at u is SAT. The proxy "every incoherent model is dominated by a
     selected model *of the fragment*" is UNSAT under both (FC) and (TR), with a 7-group minimal core. The core is
     fully explained by an IB domination-transfer lemma (Lemma 7.1; PROVED), and it is an artefact of finiteness: the
     dominator must be a selected model outside the fragment.

**Single most important finding.** At the finite level the weakening from transitivity to (FC) buys nothing that a
finite search can detect, because transitivity is never the binding constraint. On every fragment, (FC), (TC) and
(TR) stand or fall together (all stood). Additive systems already meet every finite requirement against finitely
many competitors. For the radius-2 hexagons around T1 they meet every requirement against **all** competitors
(Prop. 5.1). The first genuinely finite obstruction near T1 is to strict additive Bayes realisation: four selected
models, T1 among them, at every scale (Thm 6.1). It is escaped by every non-additive world, transitive or not.

Hence an obstruction specific to (FC) must use either infinitely many selected models (closed sections) or the
continuum of competitors in an essentially non-Lyapunov way. A positive (FC) construction must spend its
non-transitive freedom on exactly the comparisons that the four-model certificate makes non-additive: the seven
cells of §6, against fractional competitors.

---

## 1. Formulation

**Setting (write-up §2; BRIEF28).**
- Full four-advice domain on ℝ³. Pairs are indexed by f_1 > 0.
- Advice is +, 0, − or ×.
- Background order at world i: good < none < bad < contradictory.
- Plain posterior family C_p = D_{K_p}, with K_p = co{ν(p⊙v_k)} and T1 = T1(ε) = C_u.
- Each world relation ≼_i is reflexive, with one of (FC), (TC), or (TR: transitivity, for comparison).
- (S) requires C_p ∈ C_L (coherent and undominated) and C_p competitive on supp p.
- Direct (C): X ≈ C with C ∈ C_L implies X ∈ C_L.

**Cells and models (exact).** `arr3.py` enumerates the open cells of the selected models' arrangement in exact
rational arithmetic: open θ-arcs times open c-intervals. They are merged by column, i.e. by the advice of every listed
model together with the sign pattern of the problem (EE2 Lemma 2.3; FF1 §2).

Each merged cell is a finite union of non-null open cones, and every advice and sign is constant on it. A
**fragment model** assigns one advice to each merged cell. On the full domain every such assignment is an evaluable
model, because a merged cell is a measurable symmetric set of pairs.

**Records (exact identity).** rec(X, Y) is the list of (cell, X-advice, Y-advice) over the cells where X and Y differ.
Cells are non-null, so two records agree a.e. iff the lists are equal. In other words, the supports and the
before/after advice coincide a.e. (AUDIT_nonlinear_programme).

In the code, records are hashed to two independent 61-bit keys, and **every** record row is then compared with its
class representative, so a hash collision would abort the run (`sat4.py`, `fast.py`).

**Variables.** y_i(r) means "record r is accepted at world i". Then X ≼_i Y iff y_i(rec(X,Y)), and X ≺_i Y iff
y_i(rec(X,Y)) and not y_i(rec(Y,X)). Every pair in the fragment with the same record reads the same variable.
**This is (IB):** a decision on a record applies at every realisation of that record within the fragment.

**Constraints.**

| name | clause(s) | status |
|---|---|---|
| (G) | y_i(r) = 1 if r is a strict pointwise improvement at i; y_i(r) = 0 if a strict worsening | hard |
| (FC) | for every directed cycle of accepted edges A→B→…→A containing a strict edge: some edge rejected, or the strict edge's reverse accepted | hard, lazy |
| (TC) | for A≼B≼C: not C≺A | hard, lazy |
| (TR) | y(AB) ∧ y(BC) → y(AC) | hard, lazy (comparison only) |
| comp(p, X) | ⋁_{i ∈ supp p} y_i(rec(C_p, X)) | group |
| und(p, X) | not [∀i y_i(rec(X,C_p)) ∧ ∃j ¬y_j(rec(C_p,X))], for **every** selected p (so T1 in particular) | group |
| C(X, p) | not [∀i (y_i(rec(X,C_p)) ∧ y_i(rec(C_p,X)))], X certified incoherent | group |
| csp, cdom | closed-section and dominator proxies (§7) | **proxy** |

**Lemma 1.1 (necessity; PROVED).** Let L be any system on the full domain that satisfies the axioms of BRIEF28, with
(FC), resp. (TC), resp. transitivity, and with the plain posterior selection on Δ. Restrict L to the models and pairs
of a fragment whose selected models are plain models. The restricted verdicts satisfy every hard constraint and every
comp, und and C group above.

*Proof.*
- (G) and (IB) restrict verbatim. (IB) on the full domain means the verdict depends only on the record
  (AUDIT_nonlinear_programme, transition-record form; FF1 §1).
- A directed cycle among fragment models is a cycle of L. A 3-chain, or a transitive triple, is likewise one of L.
- comp is competitiveness of C_p on supp p against the evaluable model X.
- und is the statement that C_p ∈ C_L is undominated, which (S) requires.
- C(X, p): if X ≈ C_p, direct (C) puts X ∈ C_L, so X is coherent. That contradicts the certificate. ∎

**Lemma 1.2 (incoherence certificates are sound; PROVED).** `fast.py` certifies X incoherent in one of two ways:
- X gives × on a cell; or
- there are interior points g_1, g_2 of open cells where X accepts, and a rational t > 0, such that g_3 = g_1 + t g_2
  is an interior point of an open cell where X does not accept.

*Proof.* D_K ∩ −D_K = ∅, which covers the first case. For the second, suppose X = D_K a.e.
- Then P_K ≥ 0 on the open cells around g_1 and g_2. By concavity and positive homogeneity, P_K > 0 there: a zero of
  P_K at an interior point would give m·g = 0 for some m ∈ K, and m·g′ < 0 nearby.
- By superadditivity, P_K > 0 on an open neighbourhood of g_3, so D_K accepts a non-null set on which X does not.
  This is a contradiction. ∎

Every certificate is re-checked exactly before use. A model without a certificate receives no (C) constraint.

## 2. Solver

`sat4.py` (sparse edge sets) and `sat3.py` (all ordered pairs) are both built on python-sat (Glucose 4).
- Requirement clauses are added directly. For cores they are guarded by selector literals.
- The solve loop is: solve, then compute strongly connected components of each world's accepted digraph (scipy).
- Every strict edge inside a component yields a cut: the shortest return path by BFS. This is directed
  reachability, and nothing is ever *installed* by it, as BRIEF28 requires.
- (TC) and (TR) cuts come from accepted 2-paths.
- Cores are minimised over requirement groups by deletion. The cuts are kept, since each is a valid consequence of
  the hard axiom.

`additive.py` asks for a per-world additive cell witness (FF1 §3), with ψ(good) ≤ −1 and ψ(bad) ≥ 1 per cell, such
that for every selected p and every fragment X some i ∈ supp p has L_i(X) − L_i(C_p) ≥ 1. This is solved as a MILP
(HiGHS), rounded to rationals and **verified exactly**.

Such a witness is a bounded strictly guiding additive ranking on the full domain (FF1 Lemma 3.1). It is complete,
transitive and (IB) for every record. Strict competitiveness implies comp, und and C on the fragment.

## 3. Results (CHECKED per fragment)

ε = 3/10 unless stated; δ is the grid step; "cube" means every cell-measurable model using the advices the selected
models give.

| fragment | selected | models | comparison pairs | (FC) | (TC) | (TR) | additive |
|---|---|---|---|---|---|---|---|
| cube {u, u+δ(1,−1,0)}, δ=1/100, all pairs | 2 | 256 | 65 280 | SAT | SAT | SAT | FOUND |
| cube {u, u±δ(2,−1,−1)} (EE2 splice triple), δ=1/100, all pairs | 3 | 4 096 | 16.8 M | SAT | SAT | SAT | FOUND |
| same, δ = 1/1000 | 3 | 4 096 | 16.8 M | SAT | SAT | SAT | FOUND |
| same, ε = 1/10 | 3 | 4 096 | 16.8 M | SAT | SAT | SAT | FOUND |
| same, ε = 1/2 | 3 | 4 096 | 16.8 M | SAT | SAT | SAT | FOUND |
| cube {u, e_1, e_2, e_3}, all pairs | 4 | 1 728 | 3.0 M | SAT | SAT | SAT | FOUND |
| hexR1 + all single flips + all pair flips of C0 | 7 | 3 832 | 53 592 | SAT | SAT | SAT | FOUND |
| hexR1 + all single flips + all pair flips of u | 7 | 3 832 | 53 592 | SAT | – | SAT | – |
| hexR2 + 2 rounds of parallelograms + flips of u + 400 pair flips + sign-splices | 19 | 1 202 | 45 296 | SAT | SAT | SAT | FOUND |
| hexR2 + vertices + parallelograms + flips of u | 22 | 805 | 34 914 | SAT | SAT | SAT | FOUND |
| Δ ∩ (1/6)ℤ³ (edges, vertices) + parallelograms | 28 | 37 | 1 260 | SAT | SAT | SAT | FOUND |
| hexR3 (δ = 1/200) around the Thm 6.1 certificate (§6.3) | 37 | 626 | 44 918 | SAT | SAT | SAT | **not completed** (out of memory) |

Notes on the table:
- The six cube rows come from `battery.py` → `battery_cubes.out` (pairs C_p × N, with the additive test) and from
  `cube_dense.py` → `cube_dense.out` (all ordered pairs; the pair counts shown). The next four rows come from
  `battery_hexR1.out` and `battery_R2.out`, the second hexR1 row from `proxies.out`, and the last from
  `cert_fragment.out`.
- The complete cubes are the strongest fragments here: within their cell structure they contain **every**
  competitor, and **every** realisation of every record.
- The splice-triple cube contains the complementary splice and all IB transports of EE2 Lemma 2.2.
- "Parallelograms" are a + b − c cellwise (x = a where b = c, x = b where a = c). These are exactly the models with
  rec(c, a) = rec(b, x) and rec(c, b) = rec(a, x), i.e. the IB transports of selected-layer comparisons onto
  non-selected pairs.
- "Pair flips" are two-cell exchanges, whose verdicts are the exchange-rate variables.
- No UNSAT core arose under (FC), (TC) or (TR) on any fragment. So there is no core to test for persistence. §§5–6
  explain why, and what persists instead.

## 4. Structure of the satisfying systems (diagnostics)

### 4.1 The (FC) and (TR) solutions

Per-world counts, given as ties / strict / incomparable / non-transitive (triples A ≼ B ≼ C with A ⋠ C on sparse
fragments; ordered pairs with a 2-path and no edge on cubes):

| fragment | mode | world 1 | world 2 | world 3 |
|---|---|---|---|---|
| hexR1 + flips, sparse | FC | 607/18 883/7 306/8 199 | 62/9 028/17 706/8 337 | 51/5 947/20 798/5 279 |
| same | TR | 92/22 411/4 293/0 | 126/17 878/8 792/0 | 0/2 801/23 995/0 |
| hexR2 + parallelograms etc. | FC | 417/16 591/5 640/11 546 | 20/8 344/14 284/9 516 | 1/2 868/19 779/3 444 |
| splice-triple cube, all pairs | FC | 0/927 970/7 458 590/1 810 430 | 0/869 570/7 516 990/579 150 | 0/527 345/7 859 215/0 |
| same | TR | 0/2 766 400/5 620 160/0 | 0/1 448 720/6 937 840/0 | 0/527 345/7 859 215/0 |

Reading the table:
- **Non-additive as returned.** No solution is exactly additive at any world (exact LP, `diag.py`).
- **Extension test.** Additive Suzumura extendability means an additive ranking keeping every accepted comparison and
  every strict one. On the 4096-model cubes the (FC) solutions pass at every world. On the larger sparse fragments they
  pass at one world or at none.
- **The violations are not forced.** On each of these fragments an additive solution exists (§3). The non-transitive
  and non-extendable features are therefore artefacts of the solver's choice of solution.
- **Where non-transitivity sits.** In the (FC) solutions it sits in composites of a selected-to-competitor comparison
  with a competitor-to-selected comparison: X ≼ C_p ≼ Y without X ≼ Y. The composite record is left unaccepted
  instead of being installed. On cubes the (FC) solutions have almost no ties, and the relations are nearly strict
  partial orders with massive incomparability.
- **Cost of the two modes.** (FC) needed far more cuts than (TR), e.g. 2.4 M against 67 k on hexR1. The solver's
  default solutions are permissive and close cycles, while transitivity cuts converge faster.

### 4.2 (TC)-only solutions contain longer strict cycles (reported explicitly; CHECKED)

`tc_cycle.py` (output `tc_cycle.out`) takes the hexR1 fragment (models 0–6 are C0…C6, with C3 = T1) and solves it under
(TC) only. It finds, at world 1, 200+ strict cycles of length ≥ 4; at worlds 2 and 3 the battery found 0
(`battery_hexR1.out`). The shortest one is:

  F(C4; c79: 0→+) → C4 → F(C0; c8: +→0) → C1 → F(C4; c79: 0→+).

- The first edge is strict by (G): the one-cell flip is strictly better at world 1.
- The third edge is a tie.
- The other edges are mixed records, strictly accepted.
- No consecutive 3-chain closes strictly backwards, so (TC) holds and (FC) fails.

The hexR2 fragments show 38–50 such cycles per world at worlds 1–2 (`battery_R2.out`). So the two conditions really
do differ on solutions, but not on satisfiability.

## 5. Why these fragments cannot fail: finite Bayes realisation

**Definition.** Let S ⊂ Δ° be finite and let 𝒞(S) be its merged cells. Suppose every cell is binary for S: the
selected models give either a single acting advice there (accepting the oriented gamble h_c) or silence. A **strict
Bayes realisation** of S consists of:
- weights q^p ∈ Δ° for p ∈ S;
- for each c ∈ 𝒞(S), a vector w_c ∈ ℝ³ with sign(w_{c,i}) = sign((h_c)_i) for all i;

such that q^p·w_c ≠ 0, and q^p·w_c > 0 iff C_p gives the acting advice on c, for all p and c.

**Proposition 5.1 (PROVED).** If S has a strict Bayes realisation, there is a bounded strictly guiding additive
ranking L on the full four-advice domain with the following properties:
- (a) every world of L is a complete preorder with strict (G) and (IB) for every record, hence (FC), (TC) and
  transitivity;
- (b) for each p ∈ S, C_p is the a.e.-unique minimiser of q^p·L. Hence C_p is undominated, coherent, and
  competitive on Ω against **every** evaluable model;
- (c) X ≈ C_p implies X = C_p a.e.

Consequently, for every fragment whose selected models lie in S, with any competitors, any comparison pairs and any
of the modes FC, TC, TR, the verdicts of L satisfy all hard constraints and all comp, und and C groups. **No such
fragment is UNSAT.**

*Proof.* On a cell c with measure μ(c) > 0 and acting gamble h = h_c, set, per world i:
- ψ_i(accept h only) = −w_{c,i}/μ(c);
- ψ_i(silence) = 0;
- ψ_i(accept −h only) = M/μ(c) if h_i > 0 and −η/μ(c) if h_i < 0;
- ψ_i(×) = (M + |w_c|_1 + 1)/μ(c).

Here η > 0 is small, and M is large enough that M·min_{p,i} q^p_i > η + |w_c|_1 + 1.

*Strict guidance.* Accepting h is good at i iff h_i > 0 iff ψ_i < 0. Accepting −h is bad at i iff h_i > 0, and then
ψ_i = M > 0; otherwise it is good and ψ_i = −η < 0. × exceeds both acceptances at every world.

*Bayes advice.* At q = q^p the four values are −q·w_c, 0, a positive number exceeding |w_c|_1 (h has a positive
coordinate, since it is accepted by a coherent model or is the f_1 > 0 orientation), and a larger number. So the
unique minimiser is "accept h" iff q·w_c > 0, and silence iff q·w_c < 0. This is C_p's advice.

*Integration.* Penalties are constant on cells and the cells cover a conull set. So q^p·L(X) − q^p·L(C_p) ≥ 0, with
equality iff X = C_p a.e.

- (a) is FF1 Lemma 3.1.
- (b): a dominator, or any X with L_i(X) < L_i(C_p) for all i, would have a smaller q^p-loss (q^p interior).
- (c): X ≈ C_p gives equal q^p-loss, so X = C_p.

The fragment statement follows from Lemma 1.1's list, each item of which L satisfies. ∎

**Remark 5.2 (L is not a cover).** At weights q ∉ {q^p}, the Bayes models of L are cell-measurable. They are
generically not of the form D_K, so L has no closed competitive coherent selection on Δ. Consistently with gm, the
finite realisation does not extend; it is the full-requirement form of FF1's "finitely additive, globally
non-additive".

**Realisations found (CHECKED: exact rational q^p and w_c on every merged cell).** Each certificate is also
cross-checked on 20 000 random rational gambles per configuration, with the advice of every C_p recomputed from its
polygon. There were 0 mismatches (`realise.py` → `realise.out`, `certs/*.json`; `bayes_real.py`).

| S | models | cells | realisation |
|---|---|---|---|
| hexR1 at u, δ = 1/100, ε = 3/10 | 7 | 85 | FOUND |
| hexR2 at u, δ = 1/100, ε = 3/10 | 19 | 388 | FOUND |
| hexR2 at u, δ = 1/100, ε = 1/10 | 19 | 388 | FOUND |
| hexR2 at u, δ = 1/20, ε = 3/10 | 19 | 388 | FOUND |
| hexR2 at u, δ = 1/1000, ε = 3/10 | 19 | 388 | FOUND (joint search, `t8b.out`; exact check in `verify`) |
| hexR2 at u, δ = 1/100, ε = 1/2 | 19 | 388 | impossible (Thm 6.1) |
| hexR2 at (1/5, 3/5, 1/5), ε = 3/10 | 19 | 368 | impossible (Thm 6.1; 64 obstructed 4-sets, `fourpt_offcentre.out`) |
| hexR3 at u, δ = 1/200, ε = 3/10 | 37 | 1 249 | impossible (Thm 6.1) |

Notes:
- The 1/1000 certificate was produced by the joint search and verified by `bayes_real.verify` (exact rationals). It is
  not written to `certs/`; `realise.py` reproduces the other four.
- Where realisation is possible, the q^p differ from p. At q = p, 3 of 75 (hexR1) and 42 of 378 (hexR2) cells are not
  linearly separable: these are the wedge cells of EE2 Thm 2.4. So the realisation genuinely re-parametrises the
  weights.

## 6. A four-model certificate against strict additive Bayes realisation, T1 included

### 6.1 The theorem

**Lemma 6.0 (Radon; PROVED).** No four points of the plane admit, by strictly separating lines, all four singleton
splits and all three 2|2 splits.

*Proof.* By Radon's theorem, four points split into two parts whose convex hulls meet. That split is a 2|2 or a 1|3
split, and parts whose hulls meet cannot be strictly separated by a line. ∎

**Theorem 6.1 (PROVED; the data CHECKED).** Let L be any additive ranking on the full domain with integrable
penalties ℓ_i(g, a). Let a, b, c, d be four selected models of the plain family. Suppose there are seven non-null open
cells, all binary for {a, b, c, d}, on which the set of models giving advice realises each singleton split and each
2|2 split (up to complement). Then a, b, c, d are not simultaneously a.e.-unique q-Bayes models of L, at any weights
q^a, …, q^d ∈ Δ.

*Proof.*
- A q-Bayes model minimises q·ℓ(g, ·) for a.e. g (R1 Lemma 1.2).
- A.e.-uniqueness on the full domain forces a strict minimiser for a.e. g. Otherwise, switching to the other
  minimiser on a non-null set gives a different Bayes model.
- On a cell where the four models give acting h or silence, put c(g) = ℓ(g, 0) − ℓ(g, h). Then model p gives advice at
  g iff q^p·c(g) > 0, and is silent iff q^p·c(g) < 0, for a.e. g.
- Picking one such g in each of the seven cells gives seven strict linear separations of {q^a, …, q^d}. This
  contradicts Lemma 6.0. ∎

No orthant condition, no interiority of q and no closed sections are used.

**Certificates (CHECKED; `fourpt_cert.py` → `fourpt_cert.out`).** The advice of each model at each gamble is recomputed
directly from its polygon, and the cell of each gamble is re-identified by the exact classifier.

- **ε = 3/10, hexagon of radius 3 at u.** At step δ = 1/200 the four models are C_p with p − u = δ·(−3,0,3),
  δ·(−2,0,2), 0, δ·(2,1,−3). **The third is T1.**
  - The first three are collinear on the edge-parallel line through u. This is the non-splice direction of EE2
    Thm 2.4, so the middle singleton is realised.
  - The seven witnessing problems are explicit rational gambles. For example, the singleton {u} vs the rest is
    witnessed at g = (3547636505/24432472878, −28761443707/61081182195, 46925102/337465095), where C_u is silent and
    the other three accept −g.
  - The same four offsets give certificates at δ = 1/2000 and δ = 1/20000.
  - There are 408 obstructed 4-sets at each of the three scales, 12 of them containing u.
- **ε = 1/2.**
  - Radius 3: 4 482 obstructed 4-sets (678 containing u).
  - Radius 2, δ = 1/100: 192 obstructed 4-sets, e.g. offsets (−2,0,2), (−1,0,1), 0, (1,1,−2), T1 again included.
- **Searches with no certificate found.**
  - ε = 1/10: radius 3, δ = 1/200, gave 0 obstructed 4-sets.
  - The radius-2 hexagons at ε = 3/10 and ε = 1/10 gave 0, consistently with §5.
  - At ε = 1/10 the radius-4 hexagon at step 1/1000 (61 models, 3 084 active cells) has no obstructed 4-set
    containing u (`fourpt_small_eps.out`). Larger radii were not finished (the search is cubic in the number of
    models).
- **Off centre, ε = 3/10, radius 2 at (1/5, 3/5, 1/5), δ = 1/100:** 64 obstructed 4-sets. One is the offsets
  (−2,0,2), (−2,1,1), (−1,0,1), (1,1,−2), with all seven gambles exact (`fourpt_offcentre.out`).
- `four_point2.py` also counts 4-sets that include vertices as labelled points (444 at hexR3, 76 off centre). Only
  the purely selected 4-sets are used as certificates.

**Persistence (CHECKED).** Once present, the certificate persists:
- under adding selected models (monotone);
- under rescaling the hexagon about u (the same offsets at three scales, as the local blow-up of EE2 Thm 2.4
  predicts);
- at the larger ε = 1/2, where it appears already at radius 2.

### 6.2 What Theorem 6.1 does and does not say

- It concerns the plain selection only, and additive rankings only.
- Nothing about (FC) or transitivity enters. A non-additive world, transitive or not, is not bound by
  pointwise-Bayes structure, and Lyapunov convexity (the source of "competitive against all models ⇒ Bayes") is an
  additive fact.
- It does show something the project had not isolated. For ε = 3/10 and ε = 1/2, no additive ranking has T1 and three
  nearby plain models as a.e.-unique Bayes models, at every scale tested. The
  non-additivity required by Q4.2 and FF2 Cor 4.3 has a finite shadow, located on seven explicit problem cells.
- At ε = 1/10 no certificate was found in the hexagons searched (radius ≤ 3, and radius 4 through u).

**CONJECTURE 6.2.** For every ε ∈ (0,1), some finite set of plain models near u admits no strict Bayes realisation.
(Expected from gm by compactness, but the finite form needs uniform margins, which I have not proved.)

### 6.3 The certificate fragment under (FC), (TC), (TR)

`cert_fragment.py` (output `cert_fragment.out`) builds a fragment on the 37 hexR3 models with the following
competitors:
- for each certificate model, all 2^7 modifications on the seven certificate cells (508 new models);
- one round of parallelograms (81).

That gives 626 models, 248 of them certified incoherent, and 44 918 comparison edges (44 168 records).

**Result (CHECKED for this fragment).** SAT under (FC) (205 lazy rounds, 665 374 cuts), under (TC) and under (TR)
(`cert_fragment.out`).

**Not completed.**
- A first version also contained all 2 471 single flips of T1 (3 097 models). It was killed by a container restart
  before any result, so the fragment was shrunk.
- The additive MILP, and the LP diagnostics of §4, ran out of memory at 1 249 cells and were not completed. So for
  this fragment it is open whether an additive system exists.

A finite fragment cannot carry the Lyapunov force of Theorem 6.1, because a cell witness may change its weights cell
by cell. So SAT was expected in all three modes, and it is not evidence about Theorem 6.1.

## 7. Proxies and their cores

**csp (closed-section proxy at u).** If C_q ≼_i X for all six neighbours q of u, then C_u ≼_i X. On the hexR1
fragment (3 832 models) both (FC) and (TR) are SAT. Closedness of sections constrains only limits. On a finite grid
the proxy is not a consequence of (S), and it binds nothing here.

**cdom (dominator proxy).** Every certified-incoherent fragment model is dominated by a selected model **of the
fragment**. HH1 Prop 1 gives a selected dominator somewhere in Δ; requiring it to lie in the fragment is the proxy.

Under (FC) and (TR) alike this is UNSAT on the same fragment, with minimal core
{cdom(X*), und(C6, F(Ck; c81: 0→+)) for k = 0,…,5}. Here X* = F(C6; c81: +→0) deletes C6's advice on a cell c81 on
which only C6 among the seven acts (`proxies.out`, `cdom_core.py`).

**Lemma 7.1 (domination transfer; PROVED).** Let X = C_p with its advice deleted on a non-null set E on which C_p acts.
If a selected C_q is silent a.e. on E and dominates X, then C_q ⊕ (C_p's advice on E) dominates C_p.

*Proof.* rec(C_q, X) = rec(C_q ⊕ (C_p on E), C_p): the two pairs agree on E and on the complement. Apply (IB) at
every world. No transitivity is used. ∎

So the core says only this: the dominator of X* must act on a non-null part of c81, and in the fragment only C6 does,
while C6 cannot dominate X* because c81 is mixed. In Δ there are other selected models acting on c81, so the core
is an artefact of finiteness. It holds identically under (FC) and (TR).

## 8. What the weakening buys, measured on the same fragments

- **Satisfiability.** Identical on every fragment: (FC), (TC) and (TR) were all SAT, and an additive solution existed
  wherever the MILP was run (§3). On the realisable selected sets of §5, Proposition 5.1 proves the identity for all
  fragments.
- **Solutions.** (FC) admits solutions with many non-transitive triples and incomparabilities (§4.1). But since
  transitive solutions always existed, nothing finite forces them.
- **The finite obstruction near T1 that does exist** (Theorem 6.1) is to *strict-Bayes additivity*, not to
  transitivity. Both (FC) and transitive non-additive worlds escape it.

**CONJECTURE 8.1.** For every finite fragment N of the plain posterior family (finitely many selected models,
finitely many competitors, any comparison pairs), the following are equivalent: SAT under (FC); SAT under (TC);
SAT under (TR); existence of an additive cell-witness system with strict competitiveness on N. All four always hold.

Evidence for it is NUMERICS (12 fragments). It is PROVED for selected sets with a strict Bayes realisation (Prop. 5.1),
and in that case even with competitiveness against all models.

**Consequence for the programme.**
- An (FC)-specific obstruction must use infinitely many selected models, through closed sections or a continuum
  limit, or infinitely many competitors in a non-Lyapunov way.
- A positive (FC) construction must place its non-transitive verdicts on the comparisons that Theorem 6.1 makes
  non-additive: the cells of the certificate at T1, against fractional competitors.

## 9. Status table

| Item | Statement | Label |
|---|---|---|
| 1.1 | all hard constraints and comp, und, C groups are necessary on restrictions of full systems | PROVED |
| 1.2 | incoherence certificates (×; cone violation) sound | PROVED; certificates re-checked exactly |
| §3 | 12 fragments (complete cubes up to 4 096 models, 531 440 records per world, 16.8 M pairs; sparse up to 3 832 models; vertices; boundary; ε = 1/10, 3/10, 1/2; δ = 1/1000…1/6): SAT in FC, TC, TR | CHECKED per fragment |
| §3 | additive strict-competitive cell witnesses on every fragment where the MILP was run (10) | CHECKED (exact rational verification) |
| §4.1 | (FC) solutions non-transitive, not additive, extendable only sometimes; never forced | CHECKED per solution |
| 4.2 | explicit strict 4-cycle in a TC-only solution (hexR1, world 1) | CHECKED |
| 5.1 | strict Bayes realisation ⇒ one additive ranking meets every requirement at S, against all models; no fragment over S is UNSAT | PROVED |
| §5 table | realisations for hexR1 and hexR2 at u (ε = 3/10, 1/10; δ = 1/20, 1/100, 1/1000) | CHECKED (exact; 0/20 000 random mismatches) |
| 6.0–6.1 | Radon: four models with all 1- and 2-splits on binary cells are not simultaneously unique Bayes for any additive ranking | PROVED |
| §6 certs | ε = 3/10: T1 and three neighbours at δ = 1/200, 1/2000, 1/20000; ε = 1/2 at radius 2 and 3 | CHECKED |
| 6.2 | finite non-realisability for every ε | CONJECTURE |
| §6.3 | certificate fragment (626 models): SAT under FC, TC, TR; additive MILP **not completed** (memory) | CHECKED (SAT parts) |
| 7.1 | domination transfer; explains the cdom core | PROVED |
| 8.1 | FC-SAT ⟺ TR-SAT ⟺ additive-SAT on every finite fragment | CONJECTURE (NUMERICS) |
| — | a cover of T1 under (FC) | not obtained; no finite obstruction specific to (FC) exists on the realisable sets |

## 10. Files (`hh3py/`)

- **Core modules.**
  - `arr3.py`: exact arrangement (adapted copy of `ff1py/arr.py`), keeping all piece representatives and an exact
    classifier.
  - `fast.py`: vectorised fragments, generators (cubes, flips, parallelograms, splices), exact rank tables, record
    hashing with full verification, incoherence certificates.
  - `sat4.py` (sparse edges) and `sat3.py` (all pairs): SAT encodings, lazy FC/TC/TR cuts, cores.
  - `additive.py`: additive MILP with exact verification.
  - `diag.py`: solution diagnostics.
- **Experiments.**
  - `battery.py` → `battery_cubes.out`, `battery_hexR1.out`, `battery_R2.out`.
  - `cube_dense.py` → `cube_dense.out`.
  - `proxies.py` → `proxies.out`; `cdom_core.py`.
  - `tc_cycle.py` → `tc_cycle.out`.
  - `cert_fragment.py` → `cert_fragment.out`.
- **Realisation and certificates.**
  - `bayes_real.py`, `realise.py` → `realise.out`, `certs/`; the joint search `t8.py` → `t8.out`, `t8b.out`.
  - `four_point.py`, `four_point2.py`, `fourpt_cert.py` → `fourpt_cert.out`, `fourpt_small_eps.py` →
    `fourpt_small_eps.out`.
- `cegar_additive.py` is an unfinished CEGAR for additive covers of complete cell worlds. It did not converge on
  hexR1 and nothing rests on it.
