# Brief, round 38 (18 Oct 2026, 17:45): the protected weak-additive leading field

Read FIRST: AUDIT_II.md and AUDIT_II_summary.md (audit's assessment of round 37). Adopt its corrections.

## Corrections adopted
1. **NOT an equivalence.** II1 Thm 4.1 / II2 Cor 2.4 give a SUFFICIENT route only.
   - Non-(NT) ("tie") designs remain unresolved (II1 §6; II2 (★), §3).
   - The claim "if not tie-free, explicit rivals break the design" is withdrawn.
2. **Terminology: "leading-level protection" (NT/SLP).** Each C_p is the ONLY model whose leading costs are weakly lower at every world of supp p. This excludes strict improvements at some worlds as well as equal cost vectors.
3. **II2 Cor 2.2 excludes only one special adversarial sequence.** The rate-bound attack is refined (mixed-sign adversaries: II1 Thm 3.3, II2 Thm 3.1), not invalidated.
4. **The silence/wrong-advice ties belong to the AUXILIARY leading score only.** The final ranking still distinguishes them strictly through the second level. Guidance is not weakened.
5. **Audit's direct proof of the positive margin (AUDIT_II.md).**
   - Put c(a) = inf { max_{i∈supp p} [Φ_i(X) − Φ_i(C_p)] : disagreement(C_p, X) ≥ a }. Under (NT), continuity in measure and integrability, c(a) > 0 for every a > 0.
   - The proof uses compactness and purification of the attainable set, with disagreement size as one coordinate; this also handles boundary supports.
   - So (RB) holds with rate bound B/c(a).
6. **Scope of a negative theorem.** It would close the protected-leading-field subclass only, not the rate class and not FC covers in general.

## The sufficient theorem (to be refereed this round)
- **Hypotheses:**
  - an integrable, weakly guiding, additive leading field Φ = (Φ_1, Φ_2, Φ_3) on a decomposable (LF) domain (the full domain: (NT) is impossible on M_U, II1 Prop 5.1);
  - a coherent selection p ↦ C_p, continuous in measure, through T1, satisfying (NT).
- **Conclusion.** For ANY strictly guiding integrable second level Ψ, the rate system 𝒜^k (BRIEF29) is a full (FC) cover of T1. This includes strict (G), (IB), (FC), closed sections, competitiveness, admissibility of every C_p, direct (C), (LF) and T1 undominated.

## Construction guidance (audit)
- Construct Φ and the selected family TOGETHER.
- Do NOT require C_p to be Bayes at its label p. A sufficient certificate is unique Bayes optimality at some weighting w(p) with supp w(p) = supp p; arbitrary reindexing is allowed. Do not replace (NT) by uniqueness at a single weighting.
- Do NOT impose without need:
  - full-dimensional credal sets at interior indices (II1 Prop 5.4 suggests degenerate selected sets may be essential);
  - symmetry or continuity of penalties;
  - injectivity of the selection.

  Continuity in measure is the hypothesis.
- Test GLOBAL protection across the whole simplex, boundary included, not only optimality of T1.
- **Known constraints (II1 Prop 5.2, modulo gm).** On the full domain Φ must strictly favour each world's best advice, every zero of Φ must be a silence~bad tie, and the zero set must be non-null.
- **Elementary necessary condition** (verify and use). Let T1 be silent on a mixed problem with sign pattern (+,−,−). Then:
  - switching to "accept" must raise Φ strictly at world 2 or world 3, so the silence~bad tie cannot sit at both;
  - switching to "reject" must raise Φ_1 strictly, so there is no tie at world 1 on that problem.

  Similar constraints hold for every selected model on its silence set. So the tie pattern must avoid each selected model's "defending" worlds problem by problem.

## Read
- AUDIT_II.md, AUDIT_II_summary.md, BRIEF29.md, AUDIT_HH_rate.md;
- II1_notes.md (whole: Thm 4.1, Props 5.1–5.4, §6), II2_notes.md (whole: Thm 2.1, Cor 2.3–2.4, (★), Lemma 5.2), II3_notes.md (Thm 3.2 repaired HH2 Thm 2.1);
- HH2_notes.md (Prop 6.1(a)–(d)), HH1_notes.md (KKM without transitivity);
- writeup/"The Contamination Triangle.tex" §2 and Theorem gm with its three routes (§6), and the zero-pattern residuals (search N9.9, N10, R16, N26 in the write-up and in notes N9_notes.md, N10_notes.md, R16_notes.md, N26_notes.md if present);
- FF1_notes.md (plain posterior family), FF2_notes.md (Thm 4.1 chain, Step 6).

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Exact arithmetic for checks.
