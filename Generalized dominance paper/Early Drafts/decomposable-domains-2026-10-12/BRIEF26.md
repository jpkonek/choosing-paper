# Brief, round 34 (17 Oct 2026, 22:30): test the imposed selected ties; drop coordinate thresholds

Read FIRST: AUDIT_EE_ties.md (audit's assessment of round 33). Adopt its corrections.

## Corrections adopted (from audit)
1. **EE2 Lemma 1.1 is not established.** Monotonicity on the generators does not suffice. Two records can compose to the identity on a region (cancelled changes). (IB) then transports the composite to a new common advice there, where the original steps cannot be realised. The correct condition quantifies over EVERY realisation of EVERY record in the closure (EE1 Thm 3.1; EE1 Example 4.3).
2. **EE2 §4.2 covers only switch-parameter splices Y_J,** not all measurable splices of the endpoint models. Consistency along a single selected segment of the full domain is therefore NOT established.
3. **EE3 Prop EE3.1 is conditional.** It needs selected-layer guidance compatibility and (NC*), which are only NUMERICS for the patched family. EE3 is not a referee report on EE1/EE2.
4. **EE1's slack bound.** With r_i = (w_i − θ/3)_+, the bound Σ r_i ≤ 1 − θ is false. The correct bound is Σ r_i ≤ 1 − θ/3 < 1 for 0 < θ ≤ 1 and Σ w_i = 1.
5. **Strategic point.** "Clean fixed point exists" is the open construction problem restated, not a reduction of it. The threshold scheme imposes
   C_p ≼_i C_q ⟺ p_i ≥ q_i,
   so the selected family is complete at every world, with ties along every coordinate level set. The axioms do not require this. Do NOT treat the threshold scheme, the patched family or the seeds as a description of what a cover must look like.

## The decisive tie test (audit's necessary test)
- For each world i, let ~_i be the least equivalence relation on evaluable models of the full four-advice domain that:
  - contains C_p ~_i C_q whenever p_i = q_i (selected models of the chosen family);
  - is closed under (IB), i.e. replacement of common advice, applied to composites as well as generators;
  - is closed under transitivity at every stage.
- Let O_i(T1) be the class of T1 = C_u.
- **Certificate (G):** X ~_i Y with X weakly guidance-better than Y everywhere and strictly on a non-null set. This contradicts strict (G).
- **Certificate (C):** an incoherent X in O_1(T1) ∩ O_2(T1) ∩ O_3(T1). Then X is undominated whenever T1 is, contradicting (C).
- **Validity.** A certificate counts only with:
  - an explicit non-null geometric realisation (exact cells, e.g. EE2 Lemma 2.3 decision procedure);
  - a derivation using actual selected-model comparisons.
- Satisfiability on a finite arrangement is NOT a coverage proof.
- **Stronger tier (still assignment-independent).** Also include all strict selected comparisons C_p ≺_i C_q for p_i < q_i (with the scheme's orientation; check it in DD/EE notes) and all guidance comparisons. Look for a strict cycle.
- **Families to test:**
  - the plain posterior family K_p = D-posterior (no bumps);
  - the patched family of DD1/EE1/EE2.
  A certificate for the plain family that survives every patch geometry is the strongest outcome.
- **Useful facts:**
  - EE2 Lemma 2.2: transports of selected comparisons are splices.
  - EE2 Lemma 2.3: exact cell decision procedure.
  - EE2 Prop 2.3a: diagonal invariance; the maps x ↦ ν(x⊙d) preserve splice triples.
  - EE2 Thm 2.4: local splice directions at u.
  - EE2 §2.4: T1 is a splice of two family members; the level line {x_1 = 1/5} through (1/5,3/5,1/5) is a splice line; the level line of x_1 through u is not.

## Positive programme without coordinate thresholds
- Selected coherent models may be INCOMPARABLE with each other.
- The seeds need not be kept. Q4.2 (any cover needs a world that does not add up) must still be respected.
- Resolve only the comparisons jointly needed for:
  - (C): every incoherent model strictly dominated;
  - closed sections for every evaluable model;
  - competitiveness on supp p;
  - strict (G), (IB), transitivity, (LA), (LF) at T1, and T1 undominated.
- The deliverable must be a complete covering construction, or an extension theorem with an invariant that provably survives (IB) INCLUDING cancelled-change composites. A reformulation of existence does not count.

## Read
- AUDIT_EE_ties.md;
- EE1_notes.md (Thm 3.1, §4 exchange constraint, Example 4.3), EE2_notes.md (§§1–2.4), EE3_referee.md;
- AUDIT_DD_slack.md, DD1_notes.md (patched family);
- AUDIT_nonlinear_programme.md (transition records, transition lemma, joint construction);
- writeup/"The Contamination Triangle.tex" §2 (axioms and domains; exact meaning of (S), closed sections, competitiveness, (C), guidance order);
- for the positive agent also: L3_notes.md (VB near-miss, vetoes cannot be paid), L4_notes.md (fixed-point / blind field necessary condition), BB2_notes.md and CC3_referee.md (Q4.2/M3.9).

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it, in this folder. Exact arithmetic for any certificate.
