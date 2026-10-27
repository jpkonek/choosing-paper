# Brief, round 6 (13 Oct 2026, 14:30): NON-ADDITIVE rankings with thin undominated sets. Read BRIEF.md–BRIEF4.md first.

## Why this round
- Additive rankings on decomposable domains cannot cover T1 except through irregular charts (R15 escapes (E1)–(E4)); this is
  the CPM "discontinuity frontier". Weakened guidance (forced/permitted small-stakes ties) does not help (N1–N7).
- Independently, for n ≥ 4 additive rankings cannot cover proper credal sets containing three vertices (v3, additive
  obstruction and Appendix C). So full coverage needs non-additive rankings anyway.
- The binding additive constraint is: every model that is Bayes at a strictly positive weighting is undominated, hence
  (by (S) via KKM, and (C)) coherent. This holds whatever the selection's indexing. For a NON-additive ranking satisfying
  (IB) and (G), "undominated" no longer means "Bayes at some weighting", so the set that must be coherent can be much
  thinner — ideally little more than the selected family {u_p}. (S) never requires u_p to be Bayes for p (LDG
  ex:rescale: identity selection, no Bayes choices). The author insists this freedom must be used.
- Known limits: sandwiched rankings (each world pinned between additive losses; includes Pareto/unanimity of additive
  losses, any cardinality) reduce to additive ones for single interior targets in n = 3 (R11 Thm W + R13 Prop S + CCIBU).
  Lexicographic rankings can ENLARGE undominated sets but (S) kills that (R2 Prop 8). In the earlier all-model work on
  the vacuous model (Incomplete Rankings and Coverage.tex), any escape needed ≥ 2 incomplete worlds outside the
  sandwiched class, violating (NC) (exact finite cancellations among accepted changes).

## Setting (unchanged)
n = 3, binary problems (pairs {g, −g}), four kinds of advice, four-rank strict guidance order (good < silence < bad < contradictory),
models measurable modulo Gaussian-null sets, (G) strict = strictly better rank on a non-null set. Rankings: one PREORDER
per world (incompleteness allowed, LDG v2 §1), on a decomposable domain (SC + closed in measure), satisfying (G), (IB), (LA),
(S) [competitiveness in LDG's sense for preorders: for every m some ω ∈ supp p has u_p ⪯_ω m; sections
{p : u_p ⪯_ω m} closed], (C), (E), (LF) at the target. Target T1 = D_K, K = (1−ε)u + εΔ (ε = 0.3 first). No cheap
realisation; nothing making (G) or (IB) vacuous. Rankings need NOT be additive, sandwiched, complete or continuous.

## Questions
Q1 (structure). For general such rankings with T1 ∈ U_L:
 (a) What must U_L contain (vertex models? anchoring e_i ∈ V_i as in R10a Thm V? edge families? closure facts)?
     Which steps of R10a Thm V, R10b Thm PL (no plateau), R3 §2.1 (constant-level lemma, completeness-free), R15 use
     additivity, completeness, or the Bayes structure, and which are ranking-level?
 (b) PLATEAU TEST: can a ranking have u_p = T1 for all p in an open set of indices? Prove impossibility at ranking level
     or isolate exactly which additive ingredient PL needs.
 (c) Lower bounds on the size of U_L under (S)+(C): must it contain a 2-parameter family near T1? Must u be "locally
     injective" anywhere?
Q2 (construction). Build, or show impossible, a non-additive ranking covering T1 exactly. Candidate tools: plateau
selections with ordinal (non-Archimedean / lexicographic / filter-Pareto with infinitely many criteria / (NC)-violating)
worlds; the exact ordinal consistency test in "Coverage after Neutral Abstention.tex" (choose a coherent family and
closed sections A_i(X), generate the forced comparisons by (G), (IB), transitivity, check for conflicts); the
transfinite/least-closure bookkeeping of "Vacuous Targets and Transfinite Construction.tex". Every requirement must be
verified: preorders, strict (G), (IB) in LDG's form, (S) with an explicit selection and closed sections for EVERY model
of the domain, (LA), (C), (LF), measurability.

## Files
This folder (r9): all briefs, R1–R18, N1–N7, CCIBU.tex, Consolidated Statements. Most relevant: R2_notes.md (Theorem N,
Thm R, Prop 8, Conjecture 1), R3_notes.md (constant-level lemma, lex rankings, error-only primaries), R5_notes.md
(sandwiched, Thm UN), R7_notes.md (two-level lex), R10a/R10b (Thm V, Thm PL), R11 (Thm W), R15.
Earlier papers (read-only): /mnt/user-data/uploads/Generalized dominance paper/ — "Loss Dominance Generalized v2.tex"
(axioms; KKM; ex:rescale; ex:incomparable), "Coverage after Neutral Abstention.tex" (exact consistency test),
"Vacuous Targets and Transfinite Construction.tex", "Incomplete Rankings and Coverage.tex", "Beyond Additive Guidance
Rankings.tex", "Independent Rankings Without Additive Structure.tex", "Full Coverage by Homothetic Credal Families
v3.tex". Python available; scripts in a new subfolder of r9 named after your note.

## Labels and discipline
PROVED / CHECKED / CONJECTURE / NUMERICS. State every hypothesis beyond the adopted axioms. Never assume the selected
model for p is Bayes for p, that boundary-index models are Bayes or coherent, completeness, or continuity, unless you
prove it. Label restricted-class results as such.
