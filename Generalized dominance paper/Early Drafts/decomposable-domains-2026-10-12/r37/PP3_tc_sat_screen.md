# PP3. SAT screen for (TC) itself on PP1's finite cells

20 October 2026, Brief 37. Labels:
- **PROVED**: full argument given here (one reader, me; not refereed).
- **CHECKED**: exhaustive exact finite computation, re-verified by an independent script.
- **CONJECTURE**.
- **NUMERICS**: solver output. Every SAT witness quoted was re-verified by an independent checker. Nothing in the PROVED items rests on it.

No assumptions are added. Scripts are in `PP3_py/`; PP1's geometry (`PP1_py/core.py`, `arrangement.py`) is imported unchanged.

---

## 0. Verdicts

1. **No arrangement came out UNSAT.** The question had no gates, keys or verdict formula: free record-based verdicts with (IB), strict (G), (TC) on every triple of the whole regular model set, competitiveness on every support, a KKM dominator for every rival, and no selected model dominated.
   - **SAT on 14 of PP1's 19 arrangements** (CHECKED: exact witnesses, independently verified). These are the 6-line triangles 3, 5, 6, 7, 8; the 7-line triangles 0, 3, 4, 5; the 7-line hexagons 0, 2, 3, 4; and the 8-line triangle 0.
   - On all 14 the witness is plain **additive**: one fixed, strictly positive step weighting per world, with modest integer weights (largest-to-smallest ratio below 140). On 7 of the 14, a direct free-verdict solve with (TC) on all triples also returned SAT.
   - **Undecided on 5.**
     - Hexagons 1 and 5 (7 lines): no additive solution exists (exact z3 proof, independently re-checked), and the free-verdict search did not converge.
     - 7-line triangle 1 and 8-line triangles 1, 2: the exact additive search did not return within about 1–2 hours of z3 time per instance (twice for 7/1), and the free-verdict search was not run to the end.
   - There is no UNSAT core to report. PP1's UNSAT results are failures of *fixed keys and gates*, not of the axioms on these cells.
2. **Audit's triple-certificate condition is exactly (TC) plus strict (G) on the triple (PROVED by a reduction to six numbers and an exhaustive exact case check).** So the condition removes nothing: every solution in item 1 satisfies it on every triple, and it "stays SAT" trivially (§3).
3. **Non-additive cycles are not needed where SAT was found.**
   - The free solver's own solutions happen to be non-additive. Out of selected models, no single positive weight endorses them: Farkas certificates use 5–13 comparisons, i.e. cycles of length ≥ 4.
   - But on all 14 SAT arrangements an additive solution exists. **Plainly: on these finite cells an additive ranking already satisfies everything.**
   - It is additive but not Bayes: many selected (model, support) pairs are Bayes acts of it nowhere in the support. That is 28 of 78 for the triangles 6/5 witness, and 59 of 65 for a second witness on 6/3. These models survive as non-supported Pareto points, which only atoms permit (§5).
   - Where no additive solution exists (hexagons 1 and 5), lexicographic hierarchies of additive weightings are excluded too (Remark 3). Whether some non-additive (TC) system works there is open.
4. **Transfer (§5).** Nothing positive transfers.
   - On atoms, closed sections are impossible at every jump of the selection (PROVED), so KKM on cells is only a proxy.
   - On atoms, competitiveness does not force Bayes-ness, which is why additive rules pass. In any atomless blow-up it does (PROVED). In the Gaussian continuum, additive covers of these targets are excluded (FF2 Thm 4.1).
   - What transfers: the certificate equivalence (§3, a measure-level statement), and the rule that an UNSAT on a sub-collection is valid.

**Net.** The finite free-verdict screen cannot discriminate (TC)-based designs on most arrangements: additive rankings pass it, and the continuum results already exclude them. The two hexagon arrangements with no additive solution are the only cells here where a (TC) design would face a non-trivial test. To screen designs meaningfully, the model must be atomless (§6).

---

## 1. What is encoded

**Cells.** These are exactly PP1's arrangements: `random_lines(N, seed)`, the homothetic triangles K_p = p + 3 min(p)·(3/20)(e_k − c) ('hom'), and the hexagons |x_i − p_i| ≤ p_i/4 ('mult').
- The selected models and their supports come from PP1's exact enumeration (`arrangement.enumerate_models`): every atom-coherent C_p, at cells and at boundary indices, with every supp p at which it occurs.
- The model set is all 3^N regular cell-constant models.
- The arrangements are those where PP1's fixed-key search was UNSAT: 6-line triangles 3, 5, 6, 7, 8 (as listed in `exact6_hom.out`; PP1's text says 6 of 10, the file lists five), 7-line triangles 0, 1, 3, 4, 5, 7-line hexagons 0–5, and 8-line triangles 0–2.

**Unknowns.** One boolean v_w(rec) per world and record rec = (lines where X and Y differ, X's advice there, Y's advice there), meaning X ⪯_w Y. Pairs with the same record share the variable: that *is* (IB).
- **Strict (G)** fixes the forced values. If Y is a pointwise weak worsening of X at w, then v = true. If Y is a strict pointwise improvement, then v = false. (A regular change on a line changes the rank at every world, so a weak worsening with X ≠ Y is strict.)

**Constraints.**
- (S)-support: for each selected C, each of its supports s and each X ≠ C, ∨_{w∈s} v_w(C,X).
- Undominated: for each selected C and each X, ¬(∀w v_w(X,C) ∧ ∃w ¬v_w(C,X)).
- KKM: for each non-selected X, ∨_{C selected} ∧_w v_w(C,X).
- (TC): for every world and every ordered triple, ¬(X⪯Y ∧ Y⪯Z ∧ Z⪯X ∧ ¬X⪯Z).
  - This is imposed counterexample-guided on **all** triples: solve, build the three M×M verdict matrices, find every violation by a Boolean matrix product, add the clauses, repeat.
  - A SAT answer has (TC) on every triple of the model set. An UNSAT answer would rest on a subset of the (TC) clauses and so would be valid.
- Solver: CaDiCaL via pysat (`tcsat.py`, `run_atoms.py`). `run_relax.py` is the same search, warm-started from a near-additive verdict through assumption literals that are released by UNSAT cores.

**Independent SAT verification (`verify.py`, no shared code with the encoder).** It recomputes ranks from the signs of the normals and re-keys records differently. It then checks (IB) (the verdict is constant on every record class), strict (G), (TC) on all triples (integer matrix product), competitiveness, KKM and undominatedness.

**Additive search (`additive_smt.py`).** The unknowns are rational step weights W ≥ 1 per (line, world, step), with L_w(X) = Σ_c Σ_{j ≤ r_w(c,X)} W.
- The three requirements become disjunctions of linear inequalities.
- They are solved counterexample-guided with z3 (exact linear real arithmetic), and all constraints are re-evaluated in exact integers at each round.
- "unsat" on an active subset proves that no additive solution exists.
- Witnesses are re-verified by `verify_additive.py`, which builds X ⪯_w Y iff L_w(X) ≤ L_w(Y) and runs `verify.py`.
- Non-existence is re-checked by `additive_z3check.py`. It rebuilds the active constraints from the normals with its own model decoding, its own ranks and its own coherence check of the selected models at their stored indices.

**Domain.** Regular models on the N mixed lines. For additive witnesses nothing is lost (Remark 1).

**Remark 1 (additive witnesses extend to the full four-advice domain with unanimous problems; PROVED).** Give the contradiction step and the unanimous steps any positive weights.
- For a model X, let X° replace contradiction by silence and correct the unanimous problems. Then X° is regular, and L_w(X°) ≤ L_w(X) at every world, strictly at every world if X ≠ X°.
- **Competitiveness.** If X° = C, then X is a pointwise worsening of C, so C ⪯_w X. Otherwise C beats X° at some w ∈ s, hence beats X.
- **KKM.** A dominator of X° dominates X.
- **Undominatedness.** If X ≠ X° dominated C, then X° would dominate C strictly at every world. ∎
- A numerical confirmation on the 4^6-model domain with contradiction was started but did not finish in the time available.

---

## 2. Results per arrangement (item 1)

"PP1" is PP1's result for fixed keys with weak gates (competitiveness and dominators together). "free" is this screen with free verdicts, solved directly. "additive" says whether one positive weighting per world satisfies everything (weights in parentheses).

| family, lines, seed | selected models | PP1 | free verdicts, (TC) on all triples | additive |
|---|---|---|---|---|
| triangles 6/3 | 38 | UNSAT | **SAT**, verified | **yes** (64–4583), verified |
| triangles 6/5 | 50 | UNSAT | **SAT**, verified (≈ 400 rounds) | **yes** (256–4661), verified |
| triangles 6/6 | 37 | UNSAT | **SAT**, verified | **yes** (64–853), verified |
| triangles 6/7 | 41 | UNSAT | **SAT**, verified | **yes** (64–2882), verified |
| triangles 6/8 | 49 | UNSAT | **SAT**, verified | **yes** (256–12811), verified |
| triangles 7/0 | 40 | UNSAT | **SAT**, verified | **yes** (512–31957), verified |
| triangles 7/1 | 69 | UNSAT | stopped (no convergence) | undecided (z3 time-out, twice) |
| triangles 7/3 | 44 | UNSAT | not run to the end | **yes** (16–443), verified |
| triangles 7/4 | 47 | UNSAT | not run to the end | **yes** (64–5860), verified |
| triangles 7/5 | 72 | UNSAT | not run | **yes** (80–4780), verified |
| hexagons 7/0 | 41 | UNSAT | **SAT**, verified | **yes** (384–30772), verified |
| hexagons 7/1 | 68 | UNSAT | **undecided** (§4) | **no** (z3; independent re-check: unsat) |
| hexagons 7/2 | 40 | UNSAT | not run to the end | **yes** (384–26134), verified |
| hexagons 7/3 | 45 | UNSAT | not run to the end | **yes** (128–5386), verified |
| hexagons 7/4 | 51 | UNSAT | not run to the end | **yes** (64–4338), verified |
| hexagons 7/5 | 72 | UNSAT | not run | **no** (z3; independent re-check: unsat) |
| triangles 8/0 | 46 | UNSAT | not run | **yes** (256–33842), verified on all 6561 models |
| triangles 8/1, 8/2 | 83, 50 | UNSAT | not run | undecided (z3 time-out for 8/1; 8/2 not reached) |

- "Verified" means the independent checker confirmed every axiom on the whole regular model set: (IB), strict (G), (TC) on all triples, competitiveness, KKM, undominatedness.
- An additive witness is a SAT witness for item 1, so the free-verdict runs left unfinished there lose nothing.

**Cores.** No arrangement is UNSAT for item 1, so no core was extracted for it. The machinery is in place: `tcsat.core` (selector-based, deletion-minimised) and `z3check.py` (an independent rebuild of every core constraint from the normals, with an exact check that each selected model is coherent at its stored index).

---

## 3. Triple certificates are (TC) (item 2)

**Proposition 1. PROVED.** Fix a world and three models X, Y, Z, with any measurable step sets and any measure. Let ⪯ be the accepted relation on {X, Y, Z}, assumed reflexive and accepting the guidance pairs. The following are equivalent:
- (a) some strictly guiding additive evaluator (step density w > 0, integrable) supports every accepted comparison among X, Y, Z, with every strict comparison strict;
- (b) on the triple, ⪯ accepts no strict pointwise worsening (strict (G)) and has no (TC) violation.

*Proof.*
1. **Reduction.** Split the steps where the three step sets are not all equal into six types: steps held by exactly X, Y, Z, XY, XZ or YZ.
   - The evaluator enters the three losses only through W_T = ∫_T w, up to a common constant: L(X) = W_X + W_XY + W_XZ, and likewise for Y and Z.
   - With w > 0, the W_T are arbitrary positive reals on the non-null types and 0 on the null ones: put w = W_T/μ(T) on T.
   - So (a) depends only on which types are null (64 cases) and on the accepted relation (64 cases), and in each case it is a linear feasibility problem.
2. **(a) ⇒ (b).**
   - A strict worsening has strictly larger L, so it cannot be supported.
   - A (TC) violation X ⪯ Y ⪯ Z ⪯ X with Z ≺ X would give L(X) ≤ L(Y) ≤ L(Z) < L(X).
3. **(b) ⇒ (a).** Exhaustive case check. 1,207 of the 4,096 cases satisfy (b). For every one, an integer certificate with W_T ∈ {1, …, 6} exists, and it was checked in integer arithmetic (`cert_exact.py`; the LP table `cert.py` and `cert_vs_tc.py` agree). ∎

**Consequences for item 2.**
- Every SAT solution and every additive witness in §2 satisfies audit's condition on every triple, so the lazily enforced condition changes nothing.
- Direct confirmation: a scan of all 64.6 million unordered triples of the free solution for triangles 6/3 with the exact table finds 0 failing triples at each world (`endorse.py --scan`).
- Audit's proposal is correct that it gives (TC) immediately and permits longer non-additive cycles. But that is *all* it gives: it is a re-description of (TC), not a design constraint beyond it.

**Non-additive cycles in the solver's solutions.** For each free SAT solution and world, an LP asks whether one positive weight endorses every accepted C ⪯_w X with C selected (strict ones strictly). It does not, except at one world of triangles 7/0. The Farkas certificates have these numbers of comparisons per world:

| solution | world 1 | world 2 | world 3 |
|---|---|---|---|
| triangles 6/3 | 9 | 9 | 5 |
| triangles 6/5 | 7 | 5 | 7 |
| triangles 6/6 | 10 | 10 | 5 |
| triangles 6/7 | 9 | 7 | 9 |
| triangles 6/8 | 11 | 10 | 10 |
| triangles 7/0 | 7 | 13 | endorsed |
| hexagons 7/0 | 11 | 10 | 9 |

These are non-additive cycles of length ≥ 4, which (TC) permits. They are an artefact of the solver's arbitrary choice of free records: additive solutions exist on the same arrangements.

---

## 4. Where no additive solution exists

**Hexagons 7/1 (68 selected) and 7/5 (72 selected): no additive solution. CHECKED** (z3 exact linear real arithmetic).
- The proofs use 5,000 active constraints for 7/1 (2,376 competitiveness, 2,196 undominatedness, 428 KKM) and 3,656 for 7/5.
- An independent rebuild (`additive_z3check.py`) is again unsat for both.
- A selector core for 7/1 has 105 constraints. Its deletion-minimisation did not finish in the time available.

**Remark 3 (lexicographic hierarchies of weightings do not help; PROVED).**
- Comparing losses lexicographically under a finite hierarchy of weightings is the same as one weighting with values in an ordered field R(ε) (ε infinitesimal), with strict positivity read in that field.
- "Some such weighting satisfies the finite system of strict and weak linear inequalities and disjunctions" is an existential first-order sentence over ordered fields.
- By Tarski's transfer principle it holds in the real closure of R(ε) iff it holds in R. ∎
- So on 7/1 and 7/5 no lexicographic-additive rule works either.

**Free verdicts on hexagons 7/1: undecided (NUMERICS).** Two searches were run:
- the plain counterexample-guided search: 77 rounds, with (TC) violations falling from 2.0 M to 0.3 M per round, stopped for time;
- the repair search warm-started from a near-additive verdict: 1,862 rounds, 82,655 records released, 3.6 M (TC) clauses, violations 0.5–1.0 M per round with no downward trend, stopped.

Neither found a (TC)-consistent assignment, and neither found a contradiction.
- Restricted versions that fix every record changing fewer than 3, 4 or 5 lines to the near-additive verdict are UNSAT. Those are restrictions, so they prove nothing about the free problem.
- What they do show is that the near-additive verdicts on 2-line swaps already conflict with the requirements.
- CONJECTURE (weak): on these two arrangements the free problem is SAT only through non-additive verdicts on small swaps. If so, they are the first finite cells on which the non-additive freedom (TC) leaves is actually used.

---

## 5. What transfers to the continuum, and what does not (item 3)

**(i) Closedness on atoms is impossible, so KKM on cells is only a proxy. PROVED.**
- Let p be a boundary index at which the atom selection jumps across one switching line: C_p = B, and a face adjacent to p carries A ≠ B, differing from B on one mixed line.
- Two distinct regular advices on a mixed line are ordered oppositely at worlds of opposite sign, so A is a strict pointwise improvement of B at some world w₀.
- The section {q : C_q ⪯_{w₀} A} contains A's face by reflexivity. If it is closed it contains p, so B ⪯_{w₀} A, which strict (G) forbids. ∎
- So no atom system has closed sections. The cell-level KKM requirement (a dominator among the selected atom models) is a *proxy*, and it is stronger than the continuum's KKM, whose dominators may be split models at boundary indices.
- Hence the SAT results hold under the stronger cell-only KKM; adding split dominators could only help. An atom-level UNSAT driven by KKM would not have transferred without splits (PP1 included splits for this reason). None occurred.

**(ii) Atoms let additive rules be competitive without being Bayes. PROVED (atomless direction).**
- *On cells.*
  - The per-line Bayes LP at the coherent indices is infeasible on every line of every arrangement tried (`additive.py`): the switching curves bend at p_i = p_j, and the cells pin the bend.
  - The additive witnesses therefore cannot be Bayes at the coherent indices. Many of their selected models are not Bayes anywhere in the support either (`bayes_reindex.py`): 28 of 78 (selected model, support) pairs for triangles 6/5, and 59 of 65 for a second witness on 6/3 (`additive_ls_hom_N6_s3.json`). Those models are competitive only as non-supported Pareto points of a finite set.
- *Atomless.* Blow each line up into an atomless neighbourhood, so that rivals may change any measurable part of it. Then C is competitive on s against all rivals iff C is a per-problem Bayes act for some weight q ≥ 0, q ≠ 0, supported in s.
  - *Proof.* By Lyapunov, the loss-difference vectors of rivals form a convex cone generated by the per-problem changes.
  - Competitiveness says this cone misses the open orthant {d : d_w < 0 for w ∈ s}.
  - Separation gives q ≥ 0 on s, q ≠ 0, with q · (per-problem change) ≥ 0 for almost every problem and every advice: Bayes at q. ∎
  - Varying the weights within a neighbourhood does not help: integrating the per-problem Bayes inequalities gives constant weights that satisfy the same cell constraints.
- So the mechanism that lets additive rules pass on cells disappears in any atomless setting.
- In the Gaussian continuum, FF2 Thm 4.1 (refereed) says no single integrable weighting endorses all local comparisons out of selected models near the target. Additive rules cannot cover these imprecise interior targets there.
- The cells' additive witnesses are thus artefacts of atoms. This is consistent with the recorded fact that additive covers exist for some interior targets: on these cells they exist for 14 of the 16 arrangements decided.
- A fractional-rival version of the exact additive search (`additive_smt.py --frac`, the atomless competitiveness test above) is implemented, but its test run did not finish.

**(iii) What does transfer.**
- Proposition 1 is measure-level, and holds verbatim in the continuum.
- The UNSAT-validity rule holds (record variables shared by (IB), any subset of the necessary constraints), but no UNSAT occurred.
- Nothing SAT transfers: every SAT here is an atom-level SAT, and on 14 arrangements it is additive.

---

## 6. What this means for the design phase

- PP1's obstructions are obstructions to **fixed keys**, not to the axioms on cells. With free record-based verdicts, (TC) is easy on cells, and on most arrangements additive rankings already suffice.
- Audit's triple certificates add nothing beyond (TC) (Proposition 1). The freedom they seem to offer, "longer non-additive cycles", is exactly the freedom (TC) already leaves.
- A meaningful finite screen for (TC) designs must remove the two atom artefacts:
  - (a) **fractional rivals** on each line neighbourhood, so that competitiveness forces Bayes-ness (§5 ii);
  - (b) **split models with closedness implications** at boundary indices: if a face model A satisfies A ⪯_w X, then the split S at an adjacent boundary point satisfies S ⪯_w X. Each boundary point is its own model, with unlinked records.
- Hexagons 7/1 and 7/5 already defeat additive and lexicographic-additive rules on plain cells. They are the natural first test beds for non-additive (TC) verdicts. Deciding their free problem needs a better (TC) encoding than counterexample-guided triples, e.g. symmetry under translation of records.

## Scripts (`PP3_py/`)

| purpose | files |
|---|---|
| encoding, (TC) by counterexample-guided search, cores | `common.py`, `tcsat.py`, `run_atoms.py` (logs `atoms_*.out`, solutions `sol_atoms_*.npz`), `run_relax.py` (`relax_mult7_s1.out`) |
| independent SAT verifier | `verify.py` |
| independent z3 core checker | `z3check.py` |
| triple certificates | `cert.py` (exact table `cert_table.pkl`), `cert_vs_tc.py`, `cert_exact.py` |
| endorsement LP / Farkas, certificate scan | `endorse.py` |
| additive solutions | `additive_smt.py` (exact; `smt_*.out`, `additive_smt_*.json`), `verify_additive.py` (`verify_additive_all.out`), `additive_z3check.py` (`addz3check_*.out`), `additive_core.py`, `bayes_reindex.py`, `verify_additive_contra.py`; Bayes and hinge LP in `additive.py`; superseded searches `additive_milp.py`, `additive_ls.py`, `ls_multi.py`, `ls_phase.py` |
| arrangement re-sampling with face/boundary labels | `enum2.py` |
