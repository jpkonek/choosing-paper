# Research brief: coverage under decomposable domains (12 Oct 2026, 17:00)

You are working on an open mathematical problem for a professional mathematician. Rigour standard: journal.
Label every claim PROVED (full proof written), CHECKED (verified carefully, proof sketched), or CONJECTURE.
Never present a conjecture as a result. If you find an obstruction, state exactly its hypotheses.

## Files (read-only; do NOT edit anything in these folders)
- /mnt/user-data/uploads/Generalized dominance paper/  (GD)
- /mnt/user-data/uploads/CPMs/                          (CPM)
- Device-only folders (read-only via mcp__remote-devices__device_bash, if available to you):
  "$HOME/mnt/Generalized dominance paper", "$HOME/mnt/CPMs". Never write, move or delete there.
Current versions of the status files: /mnt/user-data/outputs/audit/START HERE -- Coverage Status.md and /mnt/user-data/outputs/audit/Audit of Imported Assumptions 2026-10-12.md (the copies under GD are older). The Domain Closure note is staged at /mnt/user-data/uploads/CPMs/outputs/domain-axioms/Domain Closure and Extendability.tex.
Key files: GD "Loss Dominance Generalized v2.tex" (LDG; §§1-3 axioms and KKM dominance theorem),
GD "Full Coverage by Homothetic Credal Families v3.tex" (v3; §1 the four-rank guidance order, (G), (IB);
thm:general; App. C obstruction and lem:bayes-necessary), GD "START HERE -- Coverage Status.md" (read the
dated 16:45 section first), GD "Audit of Imported Assumptions 2026-10-12.md", CPM
"outputs/domain-axioms/Domain Closure and Extendability.tex" (device; decomposable domains, exact extension theorem,
vertex lemma prop:ideal), GD "Conditional Shunning of Error.tex" (Σ_T systems), GD "Coverage after Neutral
Abstention.tex" (exact consistency test thm:closure), CPM "LSP_CPMs_v19b.tex" (CPMs, domains, non-tangency,
realisation of parallel bodies Thm 7.15, Bayes bridge §9), CPM "nonadditive_losses.tex" (lem:additive,
thm:aggregation, thm:obstruction for ε-contamination), CPM "truth_directed_losses.tex" (thm:obstruction,
rem:designs, ex:jamesian, rem:unsettled), CPM "CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md", GD "Incomplete
Rankings and Coverage.tex" (finite cancellation Thm NC, chain lemma), GD "Closed Choice Forces Fineness.tex".
Do not rediscover these; cite them.

## Setting (agreed, 12 Oct)
n ≥ 2 worlds; gambles g ∈ ℝⁿ; a gamble g represents the binary choice {g,0} (equivalently {a,b} for any a−b = g);
g and −g represent the same choice, the pair {g,−g}, indexed by its member g ∈ H = {g_1>0}; Gaussian measure μ,
models = measurable acceptance sets modulo null sets; advice on a pair: + (accept g), − (accept −g),
0 (silence), × (both). At world i the background order is good < silence < bad < contradictory
(good = the orientation that pays at ω_i). Accepted weakenings: (a) an exceptional system for the vacuous
model D_Δ (good ~ silence on mixed problems); (b) Σ_T systems (at worlds in T, good ~ silence on mixed
problems; strict elsewhere). Coherent models: D_K = {g : min_{m∈K} m·g > 0} ∪ {g ≥ 0, g ≠ 0}, K a credal
set.
A ranking system L: a DECOMPOSABLE DOMAIN M_L of evaluable models — a measurable advice range A(g) ⊆ {+,0,−,×}
(the kinds of advice that evaluable models give on the choice represented by g), and M_L = all measurable
models whose advice lies in the advice ranges (equivalently: closed under splicing and under convergence in
measure). This restricts only which models are evaluated; no decision problem is altered or removed;
a preorder ⪯_i on M_L at each world (incompleteness allowed; NOT necessarily numerical or additive)
satisfying, within M_L:
 (G) weak and strict guidance improvement (strict: pointwise at least as good at world i, strictly better on
     a non-null set ⇒ strictly better);
 (IB) independence across binary problems (v3 eq. (independence)), applied to models in M_L.
LDG axioms: (LA) C_L ≠ ∅ (coherent undominated members of M_L); (S) a selection p ↦ C_p ∈ C_L, competitive
on supp p AGAINST M_L, with {p : C_p ⪯_i X} closed for all i, X ∈ M_L; (C) closure under equal profiles (mod
null sets); (E) every model evaluated by some ranking in the class (handled by an all-model Brier ranking).
Coverage (A_LF): every coherent target D is in C_L for some L satisfying (LF): there is an open N ⊇ ∂D\{0}
such that every measurable R with R △ D ⊆ N (a.e.) lies in M_L. (LF) is required at the target only;
tangency of other selected models (e.g. at boundary priors) is allowed.
Forbidden: anything that makes (G) or (IB) vacuous (that is why domains must be decomposable domains), and
"cheap" realisation (target protected by excluding its borderline competitors; (LF) blocks this).

## Known
- Dominance half: LDG Theorem thm:kkm (closed covering + simplex lemma) — done in general.
- Vertex lemma (Domain Closure note, prop:ideal): with strict (G) at world i and (S), C_{e_i} gives at every
  problem the best advice in the advice range at world i. More generally (easy): for supp p = S, C_p's advice on each
  problem is not strictly beaten at every world of S by advice in the advice range.
- Competitiveness depends on p only through supp p: for all interior p it is the same condition
  "competitive on Ω". The prior enters only through closedness of sections and the face structure.
- Closedness forces the selection's profile to be continuous modulo ties: if p_k → p and the selection
  jumps, C_p must tie its one-sided limits at every world (take X = the neighbours).
- Additive (integral) rankings on decomposable domains: (S) + simplex lemma force every Bayes model at every prior
  to be (tied with) a coherent selected model (v3 lem:bayes-necessary (a),(b), NAL lem:additive(c), valid
  on decomposable domains). Per problem g the Bayes advice as a function of the prior is the minimisation diagram
  of ≤ 4 affine functions whose values at the vertex δ_i respect the guidance order among the advice in the advice range.
  With advice range {+,0}: the set of priors whose Bayes model accepts g is an open half-space section of Δ
  containing exactly the vertices δ_i with g_i > 0 ("vertex-respecting half-space chart"). With advice range
  {+,0,−}: acceptance region = intersection of two vertex-respecting half-spaces, one of which is shared
  (complemented) with the rejection region. So additive coverage = realisation by a measurable,
  restricted to the advice ranges, sign-preserving coherence-preserving map (CPM without continuity, on non-cone domains).
- Positive coverage known: precise targets; normalized boxes and Σ_T closures (CSE); parallel bodies (v19,
  cone domains); every target for n = 2 (v3); D_Δ (exception).
- Negative known (scope matters!): v3 additive obstruction (all-model domains; targets with 3 vertices);
  v19 Cor 12.11 (continuous CPMs, boundary targets); CONTAMINATION_NOGO (continuous non-tangential CPMs,
  ε-contamination, n=3); NAL thm:obstruction (truth-directed additive field with ε-contamination as Bayes
  at every prior in an open set); TDL thm:obstruction (vanishing exchange rates); complete-ranking
  theorems for D_Δ on all-model domains. None of these is known to apply to decomposable domains with (LF) at the
  target and arbitrary (IB) rankings.
- My own (unrefereed) observation: diagonal-projective polytope families (K_p = conv of normalized
  p⊙d^j) cannot have vertex-respecting half-space charts for all sign patterns unless all d^j coincide
  (forces precise), and generic triangles also fail the "uniform order" needed for two-slope charts.

## Simplest open test targets (n = 3)
T1: ε-contamination of the uniform prior, K = (1−ε)u + εΔ (a triangle in int Δ).
T2: a generic triangle in int Δ. T3: a segment in int Δ (lower-dimensional). T4: a boundary target such as
conv{e_1, u}.
