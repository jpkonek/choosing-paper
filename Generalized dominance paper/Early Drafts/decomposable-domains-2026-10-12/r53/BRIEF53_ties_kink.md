# Brief 53: does the kink survive single-world indifference? (23 October 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- Audit, ALL BINDING:
  - `AUDIT_round53.md`;
  - `AUDIT_section_topology.md` (tripod surjectivity; addition lemma; local construction theorem);
  - `AUDIT_round53_transfer.md` and `AUDIT_radial_transport.md` (radial compression: an exact isomorphism, NOT a reduction);
  - `AUDIT_round53_ties.md`;
  - `AUDIT_round53_final.md` (the exact encoding instructions).
- The kink:
  - `PP51_cycle_search.md` (kink certificate, Thm 5.1; PP51_py/);
  - `PP50_no_global_prices.md` (Theorem K; PP50_py/kink_box.py, kink_check.py);
  - `PP52_selective_rule.md` (Thm 4.1, which survives single-world ties but assumes closedness along changing-rival paths; Prop 7.3; Conj 7.2).
- Tools:
  - `PP49_sufficiency_theorem.md`;
  - `REFEREE_round50.md` (Thm R1; Lemma S);
  - `PP47_multicap_adversary.md` (Thm 4.1);
  - `PP21_closure_engine.md` and `PP21_py/` (exact closure engine with F1/F2 detection, reusable);
  - `AUDIT_completion.md` (closure rules I–IV);
  - `LEAD_selection_count.md`;
  - `DESIGN_MEMO.md` §8.

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets. Ranks correct 0 < silent 1 < wrong 2 < contradictory 3.
- T = T1 = D_M, M = c·1 + εΔ, c = (1−ε)/3; ε = 3/10 for the kink.
- Posterior family C_a = D_{M_a}, index = likelihood. The kink triple is u, (406,421,373)/1200, (406,373,421)/1200.
- The test target is a full 2-D posterior neighbourhood of u. This is a test commitment, not a final family.
- Axioms: reflexivity; strict (G); (IB); (TC); (S): coherent selected models, undominated, competitive on supp p, fixed-rival sections closed; (LA); direct (C).
  - (TC) means exactly: A ⪯_i B, B ⪯_i C, C ⪯_i A ⟹ B ⪯_i A, C ⪯_i B, A ⪯_i C. Single-world ties are ALLOWED.
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## Exact encoding (audit, binding)
- **Defence:** for each selected C_a and rival X, the clause ⋁_{i ∈ supp(a)} [C_a ⪯_i X]. The defending world is NOT chosen in advance.
- **Undominatedness** (A_i = [C_a ⪯_i X], B_i = [X ⪯_i C_a]): (⋀_{i=1..3} B_i) ⟹ (⋀_{i=1..3} A_i).
- **Direct (C):**
  - for an INCOHERENT X: some world refuses X ⪯_i C_a (no all-world tie);
  - for a COHERENT X: either some world refuses, or the pair ties at every world.
  - Use all three worlds for domination and direct (C); support restrictions belong ONLY to the defence clause.
- **(IB):** applies to every installed comparison, including reverse comparisons. Acceptances need NOT come from old-side coherent realisers.
- **Finite instances:** cells must be actual positive-measure measurable sets, with exact realisation of models and records, exact guidance and common-context identifications, and every clause following from an axiom.
  - An unsatisfiable such instance PROVES impossibility.
  - A satisfiable instance is only a candidate.
  - Do NOT assume verdicts depend only on masses.
- **Sections:** NO neighbour heuristics. Sections enter a certificate only via an actual sequence a_k → a with the SAME rival X and acceptance proved at every a_k.
- **Labelling:** derived clauses from earlier results are used only after their hypotheses are checked (ledger). Unchecked ones go in separately labelled conditional runs.
- **Recorded scope:** a module checking selected models does not verify (C) for every coherent undominated model in an eventual system.

## Corrections to keep in mind
- Not every earlier impossibility used a tie prohibition. PP52 Thm 4.1 concludes "dominated OR tied at every world with an incoherent model", which survives allowing single-world ties; its extra assumption is closedness along changing-rival paths.
- Triangle completion is not new (AUDIT_completion; PP21 found failures ending in strict guidance). The new question is whether the kink admits a different completion once defender choices stay disjunctive and protection is encoded exactly.
