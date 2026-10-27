# Brief 54: build the refusal allocation itself (23 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- **Audit, ALL BINDING:**
  - `AUDIT_round54.md` (assessment of round 53);
  - `AUDIT_round54_test.md` (the simultaneous-inequality test; the swap example; the allocation is the object to extend);
  - `AUDIT_round54_answers.md` (answers to the lead's questions; the plan for this round);
  - `AUDIT_robust_refusals.md` (robust refusal lemma; quantifiers; PP55 Prop SR is flawed; scope of Theorems L and Q).
- **The two theorems this round starts from:**
  - `PP56_kink_translation.md` §4: hypothesis (2V), the balanced field u¹, the relation Λ, Theorem L, Cor 4.3 (no section-free certificate), §5;
  - `PP57_tie_completion.md` §4: (L0⁺), Lemma 4.1 (pure likelihood shifts), Theorem Q, Cors 4.3–4.4, Prop 4.5.
- **Ledger:** `PP59_hypotheses_ledger.md`. A derived clause enters only with its hypotheses checked.
- **Tools:**
  - `PP56_py/` (cells56.py, lex56.py, instance56.py: the kink cells, the balanced field, exact instances);
  - `PP57_py/`;
  - `PP21_py/` (closure engine with F1/F2 detection);
  - `PP50_py/` (kink geometry);
  - `PP49_sufficiency_theorem.md`;
  - `DESIGN_MEMO.md` §8.21–8.22.
- **Architectures already killed.** Do not rebuild these under a new name:
  - single fields, additive or general (REFEREE_PP32, Contamination Triangle Q4.2);
  - rankings that one bounded weighting summarises, including intersections of additive rankings (`EXPLORATION_MAP_2026-10-16.md` item 2a.1; also item 2a.5 (L4 / R21: any FULL cover needs a degenerate endorser field with blind sets — a structural hint, not a binding constraint on a module));
  - the bounded kernel ℓ^T (PP38 Thm 3.1);
  - realiser-gated unions of additive gates near u (PP50 Thm K, PP60 Thm K′);
  - lexicographic levels (Theorem Q).
  
  Some of these are full-cover results. Whether each one applies to a LOCAL module on the four-advice domain is a ledger question, so state applicability before you rely on it.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain, with models modulo null sets.
- Ranks: correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, with M = c·1 + εΔ and c = (1−ε)/3; ε = 3/10.
- Posterior family C_a = D_{M_a}, with index = likelihood.
- The test family is a compact, genuinely two-dimensional neighbourhood N of u, small enough that (2V) holds.
- **Axioms:**
  - reflexivity; strict (G); (IB); (LA); direct (C);
  - (TC) only: A ⪯_i B, B ⪯_i C, C ⪯_i A ⟹ all three reverses. Single-world ties are allowed. Incomparability is allowed.
  - (S): coherent selected models, undominated, competitive on supp p, with closed fixed-rival sections.
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## The object of this round (audit, binding)
- **The allocation is the ranking.** Let R(r) ⊆ {1, 2, 3} be the set of worlds refusing the ordered record r = rec(X, Y). Define X ⪯_i Y iff i ∉ R(r). Once R satisfies the axioms, the construction is finished. Weights q are tools for finding or certifying parts of R; the final relation need not possess any. There is NO later stage that "realises" R by a score.
- **Openness.** For each FIXED rival X and each world i, the set {a : i ∈ R(rec(C_a, X))} is open. This is required only for a fixed rival, not as the rival changes. Its size may depend on the rival and the world. Uniform bounds are certificates where reweighting supplies them, not requirements.
- **Exact encodings** (from BRIEF53, still binding):
  - **Defence:** ⋁_{i ∈ supp a} [C_a ⪯_i X].
  - **Undominatedness:** (⋀_i [X ⪯_i C_a]) ⟹ (⋀_i [C_a ⪯_i X]).
  - **Direct (C):**
    - for an incoherent X, some world refuses X ⪯ C_a;
    - for a coherent X, either some world refuses or there is an all-world tie.
  - **(IB)** applies to every record, including reverse records and all common-context copies.
- **Partial allocations.** Mark every comparison as accepted, refused or UNASSIGNED. Unassigned is not incomparability; incomparability at i requires both directions refused at i. Every write-up must list exactly which records remain unassigned.
- **Scope of records.** Records whose old side is selected are not enough. Also include:
  - their reverse records;
  - every record in the relevant mixed triangles;
  - all common-context copies.

## The simultaneous-inequality test (audit)
- **Statement.** Requirements are "C_{a_k} refuses X_k at world i_k", with d_k(g) = u_{i_k}(g, X_k(g)) − u_{i_k}(g, C_{a_k}(g)) for the balanced field u = u¹.
- **Alternative.** One common bounded q, bounded away from zero, with ∫ q d_k dμ < 0 for all k, exists iff no α ≥ 0, α ≠ 0, satisfies Σ_k α_k d_k ≥ 0 a.e.
- **Computation.** Use q = 1 + Σ_ℓ t_ℓ 1_{E_ℓ} on a partition. This is a linear feasibility problem. Failure on one partition is NOT a general certificate; an α-certificate is.
- **Example.** Mutually inverse records refused at the SAME world are always q-infeasible: α = (1, 1) gives d + (−d) = 0. So incomparability at a single world can never be certified by one common weighting. Treat this as a candidate source of "weights fail, relations survive". It is not established until defence, protection, (TC) on reverses of accepted cycles, (G), and openness are checked.

## Section clauses: how they enter a finite certificate
Audit's rule stands: no neighbour heuristics. A suggested exact device is the **germ literal**. For source a, rival X, world i and direction v (at least the pure shifts a∘(1 + t e_w)), let γ(a, X, i, v) mean "C_{a_t} ⪯_i X is accepted for arbitrarily small t > 0 along this ray". Then:
- Closed sections give γ(a, X, i, v) ⟹ [C_a ⪯_i X].
- Defence of the shifted sources gives ⋁_i γ(a, X, i, v).
- The shifted records are r ⊕ σ_t (σ_t is the shift cone). Every (IB) copy of them carries its own obligations, including direct (C) for incoherent copies such as C_b[F ∪ σ_t ↦ C_{a_t}].

Prove any such identification exactly before using it.

## Target outcome (audit's priority)
> One explicit record-based allocation handles a compact, genuinely two-dimensional family of sources and overlapping measurable swap rivals. Its refusals are open in the source, its defence and protection obligations hold, and its relevant common-context copies satisfy (TC). No common q certifies the prescribed refusals (prove this with an α-certificate).

This is a module, not full coverage.

**Rival families: overlapping swaps, not an isolated collection.**
- X = C_a[F ↦ C_b] for a, b ∈ N, with F a union of pieces of {C_a ≠ C_b}, including balanced ones (zero u¹-value at all worlds) and non-conic ones.
- Several sources sharing pieces.
- Inverse records.
- The applicable PP30 consequences and Prop K splices, when the ledger says they apply.
- **Triangles in which** one link concerns one swap, a second link concerns a different swap, and the third is guidance or a comparison with another selected source. These interactions are the substantive test.

## Adaptive experiment (audit, binding)
At each step, retain:
- the exact records;
- the accumulated refusal requirements (world choices stay revisable);
- every promised refusal neighbourhood;
- all applicable defence, guidance, protection, (IB) and (TC) constraints.

When a new balanced swap is added, re-check JOINT feasibility of the accumulated relational requirements. Do not drop earlier obligations. Classify each outcome as one of:
- (W) the weight problem fails (a limitation of common reweighting only);
- (R) the relational constraints fail (a possible axiom-level obstruction, to be checked clause by clause);
- (W¬R) weights fail and the relations survive (the positive outcome): extract the allocation.

Growing concentration of q is diagnostic only.

World-dependent weights q_i: one small, labelled side test at most.

## Roles
- **Solver (PP61):** compatible refusal patterns, exact failures of common weighting (α-certificates), the adaptive game, and the relational feasibility checks.
- **Constructor (PP62):** one explicit rule for a parameterised family of records, independent of any solver weights, with proofs.
- **Adversary (PP63):** mixed triangles, inverse records, fixed-rival limits, (IB) copies; attacks on PP62's rule; an attempt at an axiom-level certificate coupling several rivals.
- **Referee (REFEREE_round53):** the imported results and any claimed continuum extension.
