# Brief, round 7 (13 Oct 2026, 17:15): impossibility for COHERENT-PREFERENCE rankings. Read BRIEF.md–BRIEF5.md first.

## Goal (author's request)
Prove (or refute) that T1 cannot be covered under the adopted axioms PLUS the hypothesis that each world-indexed accuracy
ranking is a coherent (almost-)preference in Walley's sense. Elegance is wanted.

T1: ε ∈ (0,1) (compute at ε = 0.3), u = (1/3,1/3,1/3), K = (1−ε)u + εΔ (vertices v_i = (1−ε)u + εe_i),
D_K = {g : (1−ε)(g1+g2+g3)/3 + ε g_i > 0, i = 1,2,3}.
(LF) at D: D ∈ C_L and there is an open cone N ⊇ ∂D∖0 such that the domain contains every model differing from D only on
gambles in N (on decomposable domains: for a.e. pair with an orientation g ∈ N the advice range contains both "accept g"
and silence).

## Walley's models (Walley 1991 §§3.7–3.8, Thm 3.8.1; Walley 2000 §6). Text extracts:
/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/w1991.txt lines 8200–8600 and .../scratchpad/w2000.txt lines 575–720.
- Almost-desirability D0–D4 (closed convex cone) ⇔ almost-preference R0–R5 (R4 continuity) ⇔ coherent lower prevision ⇔
  closed convex set M of (finitely additive) linear previsions: X ≽ Y iff P(X−Y) ≥ 0 ∀P ∈ M.
- Strict desirability (D2,D3,D5–D7, openness) ⇔ strict preference (R2,R3,R5–R8) ⇔ the same lower prevision:
  X ≻ Y iff P̲(X−Y) > 0, or X ≥ Y and X ≠ Y.
- Walley 2000 coherent partial preference P1–P5 ⇔ coherent set of desirable gambles D1–D4 (no openness/closure;
  non-Archimedean, lexicographic-type structure allowed).

## The hypothesis, made precise (state your variant explicitly)
(CP) For each world i there are measurable bounded penalties λ_i(g,a), strictly increasing in world-i guidance rank on each
advice range, and a coherent model of one of the above kinds on L^∞(H, μ) (gambles on the PROBLEM space, modulo μ-null sets, with
"positive" read as ≥ 0 a.e. and > 0 on a non-null set), such that the world-i ranking of models is the induced relation on
their loss gambles λ_i(·, X): main variant (CP-a) X ⪯_i Y iff λ_i(·,Y) − λ_i(·,X) is almost-desirable for M_i.
On the U-domain (the evaluable models are the measurable subsets X of U = D_{K′}, K′ a shrunk copy of K) the canonical encoding is the error
indicator 1_{E_i(X)}, E_i(X) = X △ (U ∩ {h_i > 0}). (IB) is then automatic. Additive rankings (M_i a singleton
countably additive with positive density) are instances of every variant.

## Consequence (verify): any such impossibility contains "T1 has no additive covering". So the theorem splits:
(A) REDUCTION: under (CP-a) [and, if possible, the Walley-2000 variant], coverage of T1 forces an additive field ψ
    (finitely additive penalties allowed) with a.e.-unique coherent Bayes models at every interior weighting and T1 Bayes
    at an interior weighting. Model: R11 Thm W (refereed; countably many integral losses): competitiveness of T from (S)
    + (LF) (Lemma IC) ⇒ no X beats T under ψ at every world ⇒ separation ⇒ T ψ-Bayes; KKM + detection (R) ⇒ every
    interior ψ-Bayes model tied with a selected model ⇒ coherent. Gaps for (CP-a): uncountably many finitely additive
    previsions (R13's L¹ separability unavailable; need countable detection on the relevant pairs, or a different
    aggregation); convexity/compactness of the attainable set for charges (Lyapunov needs countable additivity; consider
    closures, strongly non-atomic charges, Yosida–Hewitt decomposition as in CBOI). Non-Archimedean (2000) variant:
    reduce to lexicographic levels; N9.5/N9.6 (lex-IBU, face-continuum theorem) are the tools.
(B) ADDITIVE CORE: no strictly guiding additive field (integral penalties, and then finitely additive ones) on a decomposable
    domain with (LF) has unique coherent Bayes models at every interior weighting and T1 among them. Known: R15 Thm 6.2
    (excluded under (DF), (ND), (NA_w)); permitted ties irrelevant (N5–N7); CPM continuous no-go (/mnt/user-data/uploads/CPMs/
    CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md, same equations). On the U-domain (NA) is automatic, so the
    open cases are failures of (DF) (kinked facets, sliding edges) and (ND) (first-order-flat facets), plus purely
    finitely additive penalties concentrated near ∂D (Yosida–Hewitt), which could mimic kinks.

## Labels/discipline as in BRIEF5. Files: this folder; papers in /mnt/user-data/uploads/Generalized dominance paper/ and
/mnt/user-data/uploads/CPMs/ (read-only). Scripts in a subfolder named after your note.
