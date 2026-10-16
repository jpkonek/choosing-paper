# Brief, round 11 (14 Oct 2026, 20:45): the ambitious positive proposal — build ordinal rankings that cover T1

## Read first
1. termfix/TERMFIX_RULES.md in the scratchpad.
   - Domains are only restrictions on the class of evaluable models.
   - Use "decomposable domain", "advice range" and "U-domain"; never the superseded terms.
2. writeup/"The Contamination Triangle.tex":
   - §§2–3 (setting, axioms, the U-domain, adding up, M0/M1/M2);
   - §6 (the NEW theorem: no additive cover of T1 on any decomposable domain);
   - §7 (rankings that add up: the supporting assessment ψ, atom chords, residuals R-a′/R-b′, the two-world tie-breaking construction N26.1, the lexicographic class);
   - §8 (what is open).
3. The ordinal-construction sources (read-only copies), in /mnt/user-data/uploads/Generalized dominance paper/:
   - "Coverage after Neutral Abstention.tex" §3: the EXACT CONSISTENCY TEST (Theorem closure).
     - Fix a coherent selection C_p containing the target, and closed sets A_i(X) with the covering condition (5).
     - Close under four rules: reflexivity, transitivity, (IB)-transfer, and undominatedness of selected models.
     - Forbidden outcomes: (a) reversing a strict guidance improvement; (b) C_p ⪯_i X with p ∉ A_i(X); (c) an incoherent model tied everywhere with a selected one.
     - No forbidden outcome ⟺ preorders with (G), (IB), (S), (C) exist, with exactly those sections.
   - "Vacuous Targets and Transfinite Construction.tex" §5:
     - increasing unions preserve (G), (IB) and undominatedness;
     - closedness of sections is NOT preserved;
     - a sufficient invariant: permanently reserved open neighbourhoods of rejected comparisons;
     - the missing piece is the EXTENSION LEMMA.
   - "Ordinal Refinement by Slack Envelopes.tex": the unrestricted refinement lemma is false (§5); a simultaneous refinement succeeded before (IB) was imposed.
   - "Independent Rankings Without Additive Structure.tex"; "Incomplete Rankings and Coverage.tex" (incompleteness and (NC)); "Loss Dominance Generalized v2.tex" §§1–3 (axioms, KKM).
   - CPMs copy: /mnt/user-data/uploads/CPMs/outputs/domain-axioms/"Domain Closure and Extendability.tex" (exact extension to all models on decomposable domains).
4. Scratchpad notes, in this folder:
   - N9_notes.md: N9.4 normal form. On the U-domain, (G)+(IB) at a world means exactly a strictly monotone comparative ordering of that world's error sets, satisfying de Finetti cancellation A ≤ B ⟺ A∖B ≤ B∖A. N9.5 and N9.6 (lexicographic).
   - N17_notes.md and N19_referee.md: rankings that do not add up.
     - Shape of a useful cancellation: ≥ 4–5 exchanges, overlapping gains, crossing, cyclically arranged error sets.
     - Fine (NC)-violating worlds exist.
     - The only known violation is decorative.
     - Conjecture N17.B′ (closed choice forces positive weights on the relevant comparisons).
     - Nearby lemma: in n = 2 with nested selected error sets, closed sections force the Archimedean property.
   - R2_notes.md (Thm 7, countable staircases), R3_notes.md (Thm L), R7_notes.md.
   - N25_notes.md / N25_referee.md (structure of the exceptional set; Prop F, no fan points).
   - N26_notes.md / N26_referee.md (the two-world tie-breaking construction; the lexicographic class 𝓛₂ˢ).
   - I1_notes.md / I1_referee.md and I2_notes.md / I2_referee.md (the new additive impossibility proofs: what exactly they use).

## OBJECTIVE
Build preorders, one per world, on a decomposable domain with (LF) at T1 (the U-domain is the natural choice), satisfying:
- strict (G);
- (IB);
- (LA);
- (S): an explicit coherent selection p ↦ C_p, closed sections for EVERY model of the domain, competitiveness on supp p;
- (C);
- T1 ∈ C_L.

That is: an EXACT cover of T1 by non-additive rankings. Or find a genuine obstruction.

The additive route is closed (writeup §6). Do not substitute "additive" for "reasonable".

## WHAT A CONSTRUCTION MUST ESCAPE (verify before relying on any of these)
- **If every world adds up on the relevant comparisons (case M0).** A supporting additive assessment ψ exists:
  - it has the same domain, T1 is ψ-Bayes at an interior p*, and there is a coherent ψ-Bayes model at every weighting;
  - its exceptional ties lie on countably many atom chords, at least one of which is forced;
  - the original ranking must break those ties ordinally (N26.1 shows that this can be done in two worlds).
  - The new additive impossibility proofs (I1, I2) used the Bayes family at EVERY interior weighting. Do they survive atom chords? If so, case M0 is dead and the construction must be M1 or M2.
- **Otherwise (M1 or M2).** At some world no strictly positive error weight endorses the relevant comparisons.
  - Under M1, the certificate is cyclic, with crossing error sets.
  - The additive contradiction for T1 is a cyclic "exchange-rate" (holonomy) condition around the three corners: facet maps, corner equation, box or edge pinning. Non-additive rankings are exactly those that need carry no potential. This is the heuristic reason the route might work.
- **Lexicographic rankings with additive levels.** These fail closed choice (R2 Prop 8, R3 Thm L, N9.5–N9.6), except that countable staircases are allowed (R2 Thm 7).

## RULES
- Every construction must be verified axiom by axiom, preferably through the exact consistency test. Closed sections are required for EVERY model, not just coherent ones.
- Add no assumption to the framework.
- Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- Local constructions serve the global objective. If the attempt fails, give an honest failure report: the exact point of failure, and what an obstruction would have to show.
- Write only your own note, with scripts in a subfolder named after it, in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/.
