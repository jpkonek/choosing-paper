# Brief 62: an explicit signed scoring rule covering the reversed triangle (25 Oct 2026)

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Write only in this folder. Name every hypothesis.

## Binding inputs (read first)
- `AUDIT_round62_brief.md` (auditor; ALL BINDING) and `AUDIT_round61_message.md`.
- Background: `ROUND61_report.md` (note the auditor's scope corrections), `VB_dominance_note.md`, `AUDIT_VB_general.md`, `P61_notes.md`, `O61_notes.md` (Thm B: convex error levels fail), `E61_notes.md` (Cor 5.2: concave charts fail; §4: lower-prevision chart fails at prior (1,2,3)), `F61_notes.md`.

## Target
Reversed triangle K = {m ∈ Δ_3 : m_i ≤ 2/5} (uniform pari-mutuel, δ = 1/5). Vertices v_1 = (1,2,2)/5 and permutations. Lower prevision P(h) = (2(h_1+h_2+h_3) − max_i h_i)/5. D_K = {P > 0}. Domain: one-sided U = D_{K'} with K' compact convex ⊆ relint K (K' is a design variable). Models: measurable X ⊆ U modulo null sets; coherent model = D_Q (globally), Q nonempty closed convex ⊆ Δ.

## Ranking class (auditor §4)
World i maximises ∫_X c_i(h) dμ(h), with c_i positively homogeneous, integrable, sign(c_i(h)) = sign(h_i) a.e. on U. No vetoes. Not required to be convex or concave.

## Sufficient certificate (auditor §4)
1. sign correctness on U;
2. for every nonzero π ≥ 0, {h ∈ U : π·c(h) = 0} is null;
3. every Bayes set B_π = U ∩ {π·c > 0} is a globally coherent cone;
4. for some π* > 0, B_{π*} = D_K.
Then: compact score range, separation and uniqueness give that every undominated model is some B_π, hence coherent; the target is the unique optimum at π*, hence undominated; (C), (G), (IB), transitivity hold.

## Lead's reformulation of condition 3 (UNVERIFIED; check before relying on it)
For fixed h, k ∈ U write a = c(h), b = c(k), d = c(h+k). "For every π ≥ 0, π·a > 0 and π·b > 0 imply π·d > 0" holds iff (Farkas) d ∈ ℝ³₊ + ℝ₊a + ℝ₊b, with a positive coefficient on a or b unless d has suitable positivity. Since B_π contains the positive orthant (sign correctness) and excludes non-positive gambles, condition 3 for all π should be equivalent to the pairwise "quasi-superadditivity"
   c(h+k) ∈ ℝ³₊ + ℝ₊c(h) + ℝ₊c(k)   for all h, k ∈ U (a.e., with the strictness detail),
plus openness/continuity details. Concave c (c(h+k) ≥ c(h)+c(k)) is the special case with coefficients 1 — this recovers the box construction. Equivalent dual view: a family of credal sets Q_π whose acceptance region {π : h ∈ D_{Q_π}} is, for every h, the half-space {π·c(h) > 0}.
Known facts: (i) concave c cannot work for K (E61 Cor 5.2, O61 Thm B); (ii) the natural chart c_i(h) = v(h)_i h_i (v(h) the minimising vertex) fails; (iii) the affine family c(h) = (1+δ)h − δ(max h)𝟙 has convex Bayes sets for every π (superlevel sets of a concave function of h) and B_u = D_K, but it violates sign correctness where 0 < h_i < δ/(1+δ)·max h, which occurs near the faces of D_K; for π near the boundary its Bayes sets can also miss positive gambles (so they are not coherent there). A construction must reconcile these.

## Roles
- **CONSTRUCTOR (C62):** Following auditor §4 exactly: (a) positive control: recover the box construction under your test; (b) search for an explicit continuous piecewise-linear c (finite conic partition, matrices M_σ, starting from coordinate planes and facet planes of D_K, extra subdivisions allowed) and K' meeting conditions 1–4 for the reversed triangle; (c) certify exact rational coefficients and verify condition 3 for ALL π ≥ 0 by an exact finite argument (e.g. the pairwise quasi-superadditivity, verified cone-configuration by cone-configuration, or a direct convexity proof of each B_π); (d) if the ansatz fails, isolate the exact seam constraint responsible, and state precisely what the failure shows (only about that ansatz). You may relax continuity or allow more cones if justified. Use numerics only to find coefficients or witnesses.
- **ADVERSARY (A62):** Independently: (a) verify or refute the lead's quasi-superadditivity reformulation (exact statement, strictness, boundary π, null sets); (b) derive the strongest NECESSARY conditions on c near the faces and extreme rays of D_K for the reversed triangle (sign seams where faces cross coordinate planes), checking they are satisfied by the box control; (c) attack natural candidate families (pari-mutuel-affine with sign repair, "local prior" charts, mixtures of box rules, piecewise families) by exhibiting exact witnesses (π, h, k) with π·c(h) > 0, π·c(k) > 0, π·c(h+k) ≤ 0, or non-null ties; (d) state precisely the design space that survives. Do not claim impossibility beyond the ansatz you actually exclude.
- **FOUNDATIONS (FD62):** (a) Verify the auditor's F61 counterexample (x = (1,−1,−20), y = (1,4,−1)); determine exactly what F61's Theorem D does prove (trace coherence), and whether ANY two-sided domain larger than U can support global coherence for T1 (or give the exact obstruction); (b) reconcile every broad exclusion in round 61 with the known box coverage (which domain? which ranking?), and list corrected scope statements; (c) produce a corrected status table for round 61.
- **WRITER (W62):** Draft a self-contained LaTeX note "Covering coherent sets of desirable gambles by veto–Brier rankings": setting and axioms; the admissibility route (Zorn + separation + uniqueness); the covering theorem (auditor/P61 Thm A) with full proof; one exempt point; visibility characterisation (P61 Thm V, with uniform/strict/tangential qualifications); examples with corrected scope (contaminations, TV balls, belief functions with m(Ω)>0 and positive singletons, strictly 2-monotone cores, smooth K, n=2, probability-interval condition); what the construction does not reach (stated as limits of THIS construction only). Conventions: no names on theorem-like environments; \coloneqq; standard dominance nomenclature; models called "models"; self-contained, no commentary comparing to earlier versions. Compile it (pdflatex). No claims beyond refereed results.

Each role: write `<ROLE>_notes.md` (W62: `W62_note.tex` + PDF) with a status table; return a concise summary (≤ 1 page) as your final message. If blocked from writing a file, return the full content in the final message.
