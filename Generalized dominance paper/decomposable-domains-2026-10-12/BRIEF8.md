# Brief, round 9 (14 Oct 2026, 09:45). Read the Glossary at the top of
"/mnt/user-data/uploads/Generalized dominance paper/START HERE -- Coverage Status.md" FIRST (it fixes terminology;
use it), then BRIEF5–BRIEF7, then writeup/"The Contamination Triangle.tex" (consolidated statements and statuses).

## Focus (auditor's recommendation, adopted by the author): the exceptional-tie case M0
Setting: n = 3, target T1, the U-domain M_U (evaluable models: the measurable subsets of U = D_{K′}), a ranking (one preorder per world) with strict (G), (IB),
(LA), (S) [LDG preorder sense], (C). Suppose every world adds up on the relevant comparisons (B ⪯_i X, B coherent
undominated, X regular). Then (N13 Prop B, N22 Thm 2.1, N24) there is a supporting additive assessment ψ (integral,
densities > 0 a.e.) on the same domain with: T1 ψ-Bayes at an interior weighting; at least one coherent ψ-Bayes model
at EVERY weighting; a unique coherent ψ-Bayes model at almost every interior weighting. The main theorem (N15; refereed
N18, N20) needs uniqueness at EVERY interior weighting, so a cover forces a nonempty exceptional set E(ψ) of interior
weightings with non-null ψ-ties (N22 Cor 2.3). N24 R1: E(ψ) is exactly where ψ's coherent Bayes family is
discontinuous. At t ∈ E(ψ), coherent and incoherent ψ-minimisers coexist; ψ cannot tell them apart; the original
ranking must (by KKM + (C), every undominated model is coherent): each incoherent ψ-minimiser Y at t is weakly dominated
by a selected C with ψ(C) = ψ(Y) coordinatewise, and some world strictly prefers C — a strict comparison ψ does not
detect (N22 Prop 4.1).

THE QUESTION: can the original ranking resolve ψ's exceptional ties while retaining (G), (IB), (S), (C)?
Do NOT require ψ itself to satisfy (S) or (C), and do NOT require ψ's Bayes weightings to equal the selection indices
(LDG's conditional-probability example: an auxiliary numerical representation can fail to supply the obvious selection
without the original ranking failing closed choice).

Possibly useful facts/ideas (verify before use):
- V(t) = min_X t·ψ(X) is concave on Δ; E(ψ) is its set of non-differentiability points (Bayes profiles non-unique) —
  null, a countable union of Lipschitz curves in general (Zajíček-type), possibly dense.
- At t ∈ E the ψ-Bayes face's extreme profiles are limits of nearby unique Bayes models, hence coherent (coherent
  models are closed in measure); interior points of the face include splices (incoherent).
- The set of supporting assessments is a convex cone; perturbing ψ within it may remove ties (genericity), or may not.
- Lexicographic tie-breaking: R2 Thm 7 / R3 P1–P3 / R7 Lemma 7′ — closed sections force countable "staircases" of
  improvable primary levels; N9.5 lex-IBU; N9.6 face-continuum theorem (fails (S) only under a CONTINUUM of levels).
  So tie-breaking at countably many exceptional faces might be compatible with (S).
- T1 might sit exactly at an exceptional weighting (p* ∈ E), as an intermediate coherent minimiser; the local analysis
  of N15 at p* would then not apply as stated.

## Second question (keep in view): additive coverage of T1 on general decomposable domains that are two-sided near the
target (advice range {accept g, accept −g, silence}), where acceptances may compete (the adjacency escape (E4′), (E5a)).
Also two repairs flagged by the auditor: (i) the general-decomposable-domain section (N21) assumed a CONIC neighbourhood N₀ ⊆ N of
∂D_T, but (LF) only gives an arbitrary open N (e.g. N = {g : dist(g, ∂D) < e^{−‖g‖}}); repair or qualify; (ii) the
unconditional argument (N15) has not been checked under PERMITTED negligible-stakes ties (BRIEF4).

Labels PROVED / CHECKED / CONJECTURE / NUMERICS; no silent assumptions; scripts in a subfolder named after your note.
