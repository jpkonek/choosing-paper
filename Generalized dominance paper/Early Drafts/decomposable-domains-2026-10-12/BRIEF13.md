# Brief, round 14 (15 Oct 2026, 14:10): ambitious attempts at a POSITIVE answer — an exact cover of T1

## Author's directive (verbatim intent)
Keep pushing the T1 question. Do not settle for small results that do not substantially move the project forward. Focus on big, ambitious attempts at a positive answer.

Your deliverable is a complete construction, with every axiom verified, of a ranking system that covers T1 exactly.
- Partial lemmas are only worth reporting if they are steps of that construction.
- If the construction fails, give one honest failure report. Say where the global attempt broke, and what single obstruction (if any) that reveals.
- Do not produce catalogues of necessary conditions.

## Read first
1. termfix/TERMFIX_RULES.md (domains are classes of evaluable models).
2. writeup/"The Contamination Triangle.tex":
   - Introduction, especially "Summary for T1";
   - §§2–3 (setting, axioms, the U-domain, adding up, M0/M1/M2);
   - §6 (no additive cover on any decomposable domain: routes I1, I2, C2 and their inputs);
   - §7.7 (M0 closed on the U-domain, ONLY there);
   - §8.4–8.5 (the ordinal programme, the exact consistency test with the limit rule R5, the two-world core, edges, leading charges, the Level Lemma, mirror pairs).
3. Source papers (read-only) in /mnt/user-data/uploads/Generalized dominance paper/:
   - "Coverage after Neutral Abstention.tex" (§3, the exact consistency test);
   - "Loss Dominance Generalized v2.tex" (§§1–3: axioms, KKM);
   - "Full Coverage by Homothetic Credal Families v3.tex" (positive two-world constructions);
   - "Independent Rankings Without Additive Structure.tex";
   - "Incomplete Rankings and Coverage.tex".
4. Scratch notes in this folder, as needed. Note R10a_notes.md: Thm M, gauge-mixture covers of polygons arbitrarily close to T1 (a positive additive construction to deform).

## What any cover of T1 must escape (established)
- **Additive rankings** are excluded on every decomposable domain with (LF), for integral penalties.
- **On the U-domain:**
  - rankings whose worlds all add up are excluded (M0 closed);
  - (CP-a) rankings are excluded;
  - any world with a nonzero leading charge adds up (no nestedness needed);
  - complete worlds add up when their edge selections are nested.
- **So a cover on the U-domain needs a world W with:**
  - no strictly positive weight endorsing its relevant comparisons;
  - no leading charge;
  - not (CP-a);
  - either incomplete, or complete with crossing edge selections.
- **The edge results** under (Nest_e) only constrain comparisons between subsets of one edge region R_ij. NOTHING constrains a world's comparisons out of INTERIOR selected models, whose error sets cross. A cyclic (M1) certificate there needs at least 4 comparisons with overlapping gains (N17.3).
- **On general decomposable domains** (two-sided advice near the target), only additive rankings are excluded. Rankings that add up with ties broken ordinally (M0) have NOT been excluded there. The M0 closure used the U-domain chain.
- **Heuristic.** The additive contradiction is a cyclic exchange-rate (holonomy) condition around the three corners: the corner equation x + 1/x = κ + 1 against the box, or against I1's edge pinning. A ranking that need not carry a potential could absorb it.

## RULES
- Every axiom must be verified:
  - strict (G), (IB), (LA);
  - (S), with an explicit coherent selection, closed sections for EVERY evaluable model, and competitiveness on supp p;
  - (C);
  - (LF) at T1;
  - T1 ∈ C_L.
- Use the exact consistency test (with R5) wherever it helps.
- Add no assumptions.
- Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- Write only your own note, plus scripts in a subfolder named after it, in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/.
