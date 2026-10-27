# Brief 67: completion round. Full-domain infinite-world theorem, the repair theorem, the status of compactness in LDG, and proof outlines (26 Oct 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Write in plain English. Write only in this folder (`r67/`).

## Binding inputs
- `AUDIT_r67_message2.md` holds the author's decisions via the auditor. It is BINDING.
  - This is a completion round. Do not start the definitive manuscripts, and do not search for new constructions.
  - The completion criterion is a fully checked theorem with an explicit scope and a short chain of dependencies.
- `AUDIT_r67_message1.md` and `AUDIT_r67_brief.md` are the auditor's round-66 assessment. Its §2 contains the full-domain infinite proof.
- `AUDIT_r67_compactness.md` is the auditor's compactness weakening for LDG, with its strict-separation example.
- Refereed sources:
  - `Universal coverage of coherent sets of desirable gambles (draft).tex` and its PDF: the finite theory; §7 covers infinite worlds on one-sided domains.
  - `IW66a_notes.md`, `IW66b_notes.md` and `REF66_iw_section_notes.md`: infinite worlds.
  - `TS66_notes.md` and `REF66_ts_notes.md`: finite two-sided domains, Lemma E, hull-closed domains.
  - `SR66_notes.md` and `REF66_un_notes.md`: the simple ranking.
  - `REF65_hA_notes.md`: minimax and contraction.
  - `LDG_v3.3.tex` and its PDF, with `REF66_ldg_notes.md`.
- `ROUND66_report.md`.

## Decisions already taken
1. **The application paper leads with the repair theorem.** Every incoherent model X has a coherent N that is better by a uniform positive margin at every world, with N ⊆ hull(X∖N). Here the hull of a set with no supporting state is the whole space. The ranking is a corollary.
2. **Scope and generality.**
   - The score is the integrated payoff under any measure satisfying the stated assumptions. Positive reweightings are absorbed into the measure. Make no claim that other scores fail.
   - State separately: the set of worlds, which is arbitrary; the gamble space, which is a separable sup-norm-closed space of bounded gambles with an order unit; coherence modulo the chosen measure; and strict versus uniform improvement.
3. **The abstract compactness condition (CC) is equivalent to the dominance conclusion.**
   - Proof: give the undominated coherent models the cofinite topology, and for each rival take its dominator as a singleton closed set.
   - The substantive infinite-world theorem for LDG is the *local* one: guarantees established on each finite set of worlds, linked through one compact family.
4. **LDG** covers what follows from a given family of rankings, with checkable sufficient conditions. The ranking construction belongs to the application paper; LDG gets at most a short remark.
5. **Jargon must go from the definitive versions.** This includes "certificate", "record", "safe", "routes", and labels such as (GI), (GP), (SI), (RS), (TG), (TS) and (FCC). Statements in the outlines should already be written without them.

## Roles

### RF67a and RF67b: two independent referees of the full-domain infinite-world theorem (AUDIT_r67_brief §2)
Work independently, and do not read each other's notes. Referee the Proposition (the uniformly losing part) and the Theorem (full-domain coverage on E) in the established setting.

Check in full:
- the existence and attainment of the minimax;
- that the relaxed choice is represented by the measurable set L = X ∩ {q* < 0}, including that {q* = 0} is null;
- that m(L) ≤ −η at every world, and that this means at every state;
- the case where X₊ = X ∩ {q* > 0} is coherent, and the case where it is null;
- that applying the one-sided infinite theorem inside hull(X₊) is legitimate, including which "K′" and which domain play their roles, and that step C's non-null gain uses q* ∈ Q_{X₊};
- that the defender N lies in {q* > 0}, so L ⊆ X∖N a.e.;
- that Q_L = ∅, via a state applied to a Bochner integral, so no coherent model contains X∖N;
- the uniform total improvement;
- protection on the full domain with uncountably many worlds. Use the countable norming set and the null-boundary assumptions. Sure gains are uniformly positive a.e. and sure losses uniformly negative a.e.; check this needs {P_S = 0} null and the analogous set for −h.
- the passage between sets and their equivalence classes;
- that literal (LF) holds on E;
- that every coherent target D_Q (Q any nonempty weak-* compact convex set of states) is covered;
- what full support is needed for (uniqueness of Q; distinctness of coherent models).

Also check the corollaries:
- finite worlds and two-sided domains: does the theorem contain TS66's finite result as the case E = ℝⁿ with Lebesgue-equivalent μ?
- restricted domains (one-sided D_{K′}, hull-closed domains).

Try to break the theorem: rivals containing both h and −h; X with Q_X = ∅ where the sure loss is spread thinly; E = C(Ω) with Ω uncountable.

Outputs: `RF67a_notes.md` and `RF67b_notes.md`, each with a verdict table. State at the top whether the theorem holds, and under exactly which hypotheses.

### OUT67: proof outline for the application paper (writer–mathematician)
Produce `OUT67_application_outline.md`: a complete, plain-English chain of statements with full proofs. It is a mathematical skeleton, not a manuscript, and should be at most about 12 pages of markdown. The chain:
1. **Setting.** E (finite worlds being E = ℝ^Ω), states, the measure, models modulo μ, coherent models D_Q, and the hull. Make the measure-relative identification explicit.
2. **Minimax lemma.** A single statement covering both uses: optimise relaxed acceptance choices against all states; attainment; the optimal relaxed choice is an ordinary set.
3. **Trimming lemma.** The contraction lemma: hull(X∖N) = hull(X) after the shrink.
4. **Repair theorem.** For every incoherent X there is a coherent N with a uniform positive improvement at every world and N ⊆ hull(X∖N), where hull = E when there is no supporting state. The proof has two cases:
   - *consistent commitments:* optimise within the hull, then trim;
   - *inconsistent commitments:* remove the uniformly losing part, then repair the remainder.

   Check carefully that N ⊆ hull(X∖N) holds for **all of N** in both cases, including that the inconsistent case gives hull(X∖N) = E.
5. **Ranking corollary.** At a world, accept guidance, or accept a strictly score-improving change that no coherent model can make. Prove:
   - all the agreed properties: strict guidance, independence, acyclicity (TC) and finite-chain consistency, disjoint additivity;
   - protection;
   - dominance;
   - undominated = coherent;
   - (C), (W) and (LF) on the full space.

   State that the ranking is not transitive.
6. **Corollaries for restricted domains.** One-sided D_{K′}, with its exact (LF) condition in finite and in infinite dimensions; hull-closed domains; finite worlds.
7. **Scope statement.** Half a page, covering:
   - worlds versus the gamble space;
   - the separable order-unit assumption;
   - coherence modulo μ, with the dependence on μ;
   - strict versus uniform improvement;
   - which open questions remain (nonseparable spaces, spaces without an order unit, domains that are not hull-closed).
8. **One representative structured construction.** Choose the simplest self-contained example covering genuinely imprecise models, probably veto–Brier on the visibility class. Give its statement and the reason for including it: a complete, transitive, score-based ranking at each world, with an intelligible assessment of individual errors. Add a one-paragraph proof sketch with a pointer.
9. **Cut list.** For each source (the universal note, the covering paper), list what is essential, what is kept as an example or figure, and what is dropped.
10. **Glossary.** Map each current term to its plain replacement.

Mark any statement whose proof depends on the RF67 verdicts as "pending RF67". RF67's notes will appear in this folder; incorporate them if they arrive before you finish.

### CC67: compactness in LDG (referee and theorem formulation)
1. **Check (CC) ⟺ the dominance conclusion (W).** Assume (LA) and that the undominated coherent class is nonempty. Use the cofinite-topology argument. Check whether reflexivity or anything else is needed.
2. **Referee the strict-separation example** in AUDIT_r67_compactness §5. Re-interpret it: it shows that (I) + (B∞) is strictly stronger than (W).
3. **Formulate and prove the substantive local theorem.** For each finite set F of worlds there are guarantees on the simplex Δ_F, with closed sections and support-wise coverage. Each of them sits inside one global compact family whose relevant sets are closed. Check whether this local version can be verified without already knowing the conclusion. Check whether it, too, collapses into (W) under some trivial choice; try the cofinite topology and discrete choices.
   - If it does collapse, find the nearest version that does not, or say exactly what extra structure gives it content (for example: a fixed index space given in advance, continuity of the local-to-global map, Bayes-choice structure).
   - Write the statement without the word "certificate".
4. **Determine what the old pair (I) + (B∞) implies that the local theorem does not.** In particular, list which appendix results of LDG v3.3 need extra hypotheses (scores, Bayes choice, lower semicontinuity).
5. **Concrete applications.** Confirm that LDG's applications satisfy the local theorem's hypotheses directly: Nielsen-type probabilism on arbitrary domains, the countable example, proper scores.

Output: `CC67_notes.md` with a verdict table.

### LDGO67: proof outline for the final LDG (after CC67)
This role starts after CC67 reports; the lead will brief it then.

## Output
Each role writes its notes and returns a concise summary (at most one page) as its final message. If you are blocked from writing a file, return the full content in the final message.
