# Audit brief (12 Oct 2026)

All source files are staged read-only under /mnt/user-data/uploads/Generalized dominance paper/ (GD) and
/mnt/user-data/uploads/CPMs/ (CPM). Do NOT edit them. Write your report to the path given in your task.

## The permitted axioms (the ONLY assumptions the programme is entitled to)
From "Loss Dominance Generalized v2.tex" (LDG, sections 1-2, lines 35-130): a ranking L has an evaluation
domain M_L (a SUBSET of all models; nothing requires M_L = all models) and a preorder at each world on M_L
(incomplete allowed). (E) every model lies in some M_L (collectively, across the class of rankings);
(LA) C_L := coherent members of M_L undominated within M_L is nonempty; (A) every coherent model is in some
C_L; (C) closure of C_L under equal profiles; (S) a map p -> u_p in C_L, competitive on supp p AGAINST
MODELS IN M_L ONLY, with {p : u_p <=_w m} closed for every world w and every m in M_L.
From "Full Coverage by Homothetic Credal Families v3.tex" (v3, lines 48-145): binary-problem advice
(+,0,-,x) on H={g_1>0}, background order good < silence < bad < contradictory, (G) guidance improvement
(weak and strict, applied to models in the domain), (IB) independence across binary problems (applies when
the four models involved are in the domain). Agreed weakenings: an exceptional system for V (good ~ silence
on mixed problems), and the "conditional values" systems Sigma_T (conditional on worlds in T only shun
error; strict (G) off T).

NEW (12 Oct, from the author): rankings need NOT evaluate all measurable models. What is required instead is a
principled non-tangency condition: the selected/undominated coherent models C_L should lie in the interior
of the evaluation domain M_L. The model for this is LP-CPM v19 (CPM/LSP_CPMs_v19b.tex, Def. def:cpm and
def:cpm-loss, lines 185-260 and 1890-1960): a CPM domain is an open convex cone V containing the nonnegative
orthant minus 0; the loss evaluates the rules lying in V up to null sets (M_L = {D : lambda(D \ V)=0});
a realisation of D is non-tangential if closure(D)\{0} is contained in V. So "v19-type domain" below means:
M_L = all measurable models whose acceptances lie (a.e.) in a fixed open convex cone V (V may be a proper
cone, so domain models cannot accept gambles outside V), and every selected coherent model C_p has
closure(C_p)\{0} inside V.

## What to flag
For each main result (theorem/proposition/lemma that is used later or stated as a conclusion), record:
1. its exact hypotheses, with file and label/line;
2. EVERY assumption beyond the permitted list. In particular:
   (a) M_L = all measurable models (stated or implicit). When implicit, identify the specific competitor
       or auxiliary models the proof needs to be in the domain (e.g. ideal models D_i, splices, pointwise
       Bayes models, models accepting gambles outside some cone, models far from the selected family);
   (b) completeness of rankings; (c) additive/integral/finitely additive representation or one-sided
       extension hypotheses; (d) Bayes choice; (e) closedness for all m, continuity beyond (S);
   (f) problem-space modelling choices (only binary problems, Gaussian measure, null-set identification,
       H) — note these but they are probably part of the agreed setup;
   (g) anything else (fineness, Archimedean conditions, homogeneity, specific families, etc.).
3. VERDICT under a v19-type domain with non-tangency: SURVIVES (proof goes through verbatim),
   SURVIVES-WITH-REPAIR (say what repair), FAILS (say which step uses a model outside the domain and give
   the simplest reason it can't be repaired, or an example), or UNCLEAR (say why).
Be concrete and cite line numbers. Do not speculate beyond what you can check in the proof text. Be
honest about what you did not read in full.
