# Round 81 brief: connecting the desirability results to LDG (research round; NO manuscript changes)

Folder (write ONLY here): /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r81/

Sources:
- AUDIT_A_finite_sequence.md and AUDIT_B_brief.md: the auditor's notes. Follow B as the brief.
- appshort.tex: the author's current Short application paper. Its Theorem thm:dominance says that (A1)–(A4) imply every incoherent model is dominated. Its proof is in §3.
- app_long.tex: the longer version, which contains the repair theorem.
- ldgshort_app.tex: the LDG Short with the applications proposal. Selection (S) is defined there; see thm:finite, cor:closed-choice and thm:local.
- ldg_full_current.tex: the full LDG.

The papers follow two conventions. In LDG, ⪯ means "at least as good". In the application, ⪰ means "at least as good". Keep the two straight.

Labels: PROVED / CHECKED / CONJECTURE / UNCLEAR / FAILS. Plain English. Be rigorous.

## Strand 1 (agent FS81): the finite-sequence theorem, the geometric lemma, and removing (A2)

1. **Check the finite-sequence theorem** (AUDIT_A). Statement: if x₁,…,x_r each weakly dominate their predecessor, starting from x₀, and z weakly dominates x_r, strictly at some world, then some member of x₁,…,x_r,z dominates x₀.
   - Prove it.
   - Determine the weakest tie-substitution hypothesis it needs. Is it enough to have substitution through **all-world ties**: if a and b are tied at every world and c ⪯_ω a, then c ⪯_ω b? Or is worldwise (A3) needed?
   - Give a counterexample showing that some such hypothesis is needed.
2. **Extract a ranking-free geometric lemma** from the proof in appshort.tex §3. Under (M2) and (M3), every incoherent model X admits a sequence X = X₀ → X₁ → … → X_r → Z with r ≤ 2. Each X_{j+1} is a consolidation of X_j, as defined in def:change, with the triples genuinely legitimate: masses, disjointness, uniform margin, inclusions a.e. The last step is a non-null change guided at every world.
   - Check carefully that the constructions use undominatedness only in the contradiction argument.
   - Where the current proof uses facts about undominated models (that they contain D_S° and miss −D_S°, upward closure, tie preservation), replace them with an explicit case split on X.
   - Handle null sets, atoms and (M2) exactly.
   - State the lemma precisely and prove it.
3. **Conclude a new dominance theorem.** Under (M2) and (M3), every ranking satisfying (A1), (A4) and the tie-substitution hypothesis from item 1 dominates every incoherent model. Check whether (A3) can be weakened to all-world-tie substitution, and whether (A2) is used anywhere.
4. **Give paper-ready statements** (not inserted into any manuscript):
   - an LDG proposition, the finite-sequence theorem, in LDG's convention;
   - the geometric lemma;
   - the revised Theorem 4.1 with its proof.
   Note any change to the consistency proposition: (A2) is simply dropped.

Output FS81_report.md.

## Strand 2 (agent S81): reopen selection (S)

Work in finitely many worlds first: Ω = {1,…,n}, E = ℝⁿ, μ with Lebesgue null sets and a finite first moment. Use the actual formulation of (S) in LDG thm:finite: closed **subsets** A_ω(X) of the acceptance sections, assigned models c_p ∈ C_L, and the serving condition that every p lies in A_ω(X) for some ω ∈ supp p.

1. **The current integral ranking** (appshort def:integral). Does (S) hold?
   - The auditor's constraint: every almost coherent model must lie in the image.
   - The lead's sketch, to be proved or refuted. Distinct coherent models are incomparable at every world unless the change between them is guided there, because a change between coherent models is available to its starting model. So for an interior prior p and a coherent rival X ≠ c_p, the condition c_p ⪯_ω X at some ω ∈ supp p would need the change from X to c_p to be guided at ω. That should fail for suitable X, so the serving condition fails. Vertices are fine, since the change to {h(ω) > 0} is guided at ω.
   - Determine exactly whether (S) fails, with a proof, for n ≥ 2.
2. **Possibility 1: consolidation-guided selection.** Can a prior p guide consolidation towards a coherent c_p in a way that gives the defence inequality and closed witnessing sets? If the current ranking blocks this, say exactly why.
3. **Possibility 2: coherent all-world ties.** Design a ranking in which almost coherent models fall into all-world tie classes, possibly all of them tied, while incoherent models stay out of those classes. Verify each of the following, or show impossibility:
   - (A1), (A3), (A4), and (A2) if possible;
   - closure under ties;
   - admissibility of coherent models;
   - (S).
   Candidates include losses that are constant on the coherent class, and modifications of the integral ranking that accept changes between coherent models. Check (A4) carefully: consolidation must never make a model worse at any world.
4. **Possibility 3: target-relative admissibility.** Here each ranking protects only a family, for example the rescaled family M_m from the round-71 guidance, or a single credal set's model, and other coherent models may be dominated. Does (S) become attainable? A natural test: a loss ranking built from a strictly proper score on the induced forecasts. Report the exact additional assumptions needed.
5. **Consistency.** For any modified ranking where (S) is verified, check that the consistency construction still works: some family satisfies the hypotheses of the dominance argument.

Output S81_report.md, results first, separating:
- whether (S) holds for the current ranking;
- any modified ranking for which (S) is actually verified;
- the exact additional assumptions;
- whether consistency still works.

## Both agents
Final message: under 250 words.
