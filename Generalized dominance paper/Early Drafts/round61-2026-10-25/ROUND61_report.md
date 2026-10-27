# Round 61 report: the admissibility route and coverage of coherent sets of desirable gambles

25 October 2026. Four constructors (P61, O61, E61, F61) and two independent referees, one for the positive results and one for the impossibility results. Labels: PROVED (refereed once unless stated) / CHECKED / CONJECTURE / NUMERICS. Notes in this folder: `P61_notes.md`, `O61_notes.md`, `E61_notes.md`, `F61_notes.md`, `REF61_pos_notes.md`; the impossibility referee's verdicts are summarised in §4.

## 1. Answer to the question
**Is the admissibility route the right generalisation? Yes, for the dominance half, and it gives a clean covering theorem for a large class. It does not by itself give universal coverage.**
- The route has three steps: compact score range plus Zorn; undominated implies lexicographic-Bayes, hence coherent; target undominated.
- It covers every target in the "visibility class" with a one-page proof. That includes most standard imprecise-probability models.
- It fails at credal sets with "sharp" corners, such as pari-mutuel models. There, every non-CPM ranking class examined is provably blocked. What remains open is exactly a CPM-type "chart" problem.

## 2. Positive results (all refereed CORRECT, except where noted)

**Covering theorem (auditor's theorem; P61 Thm A).**
- *Setting:* finitely many worlds, and a full-dimensional credal set K.
- *Hypothesis:* K = conv(K′ ∪ A_1 ∪ … ∪ A_n) for some compact convex K′ ⊆ relint K and compact A_i ⊆ conv(K′ ∪ {e_i}).
- *Ranking:* at world i, veto φ_i(h) = max(0, sup_{v∈A_i} −v·h), then Brier error −∫_X h_i, on the domain U = D_{K′}.
- *Conclusion:* D_K is covered under strict (G), (IB), transitivity, (LA), direct (C), (LF) and the dominance conclusion.
- *Two simplifications:* uniqueness needs no polyhedrality (monotone along 𝟙, then Fubini), and (C) follows from uniqueness.

**Exact undominated family and one exempt point (P61 Thm B, = O61 Thm C).**
- The undominated models of this ranking are exactly the unique minimisers of the lexicographic weightings.
- K = conv(K₀ ∪ {π*}) is covered for any one extra point π* of the simplex.

**Visibility characterisation (P61 Thm V).**
- *Definition:* a point v ≠ e_j of K is visible from world j iff every nonzero h in its face F_v of cl D_K has h_j < 0. Equivalently, the ray from e_j through v continues into K. (The lead's weaker condition F_v ⊆ {h_j ≤ 0} is false.)
- The auditor's condition holds iff K is uniformly visible.
- For K in the open simplex: K is a VB-type target iff all but at most one extreme point is uniformly visible.
- For polytopes: every vertex is visible, or is a vertex of the simplex.

**Standard classes (P61 §I, with the referee's correction).**
- **Covered, in any number of worlds:**
  - interior ε-contaminations;
  - total-variation balls with δ < min p_j;
  - belief functions with m(Ω) > 0 and positive singleton masses;
  - strictly 2-monotone cores with positive singletons, including strictly convex distortion models, the PRI rule, and the *core* of the constant-odds-ratio lower probability;
  - every smooth credal set in the open simplex;
  - every full-dimensional target when n = 2.
- **Probability intervals:** covered iff each vertex has at most one coordinate at its upper bound. This includes generic hexagons for n = 3; most intervals for n = 4 are not covered.
- **Not covered by VB-type rankings:**
  - pari-mutuel models (the reversed triangle {m_i ≤ 2/5} is the uniform pari-mutuel model with δ = 1/5);
  - normalised boxes, which are covered separately by L3's box systems on two-sided domains;
  - the constant-odds-ratio credal set, which is a normalised box (referee correction; P61 listed it as covered).

**Two-sided domain for contaminations (F61 Thm D; referee re-checked with unequal ε_i, n = 3–5).**
- *Targets:* K = conv{(1−ε_i)p + ε_i e_i} with p interior. This includes T1 and every interior ε-contamination, in any number of worlds.
- *Domain:* A_K, the gambles with at most one positive coordinate, or with v_k·h ≥ 0 at every positive coordinate k. It is two-sided on the single-negative part of each facet.
- *Ranking:* charge only wrong acceptances beyond facets, 1[h_m < 0]·[−v_m·h]_+, then Brier.
- *Conclusion:* every requirement holds, and the undominated models are A_K ∩ D_{K*}.
- *Maximality:* A_K is maximal for veto-led rankings, up to one exempt facet (Cor B3). Exact maximality is a CONJECTURE.

**Dense coverage (E61 Prop 6.1).** Every full-dimensional K in relint Δ, for any n, is a Hausdorff limit of exactly covered polytopes K_s, each on its own domain. The rate is d_H ≤ (1−s)·max|k − u|. For the reversed triangle these are corner-cut hexagons, with d_H = 0.0645 / 0.0135 / 0.0014 at s = 0.5 / 0.9 / 0.99.

**Precise targets.** These are covered on the full two-sided domain by plain Brier.

## 3. Impossibility results (refereed CORRECT, except where noted)
- **Lower-dimensional targets need two-sided domains.** A one-sided domain with (LF) forces K to be full-dimensional; this includes precise targets (P61 D1, O61 Rem 1.1).
- **Veto-then-error rankings.** Take complete rankings with any measurable vetoes, any number of veto levels, then a Brier-type error level, on any one-sided (LF) domain (O61 Thm A):
  - the target pays no veto;
  - veto-free "collars" are forced beyond every non-visible corner;
  - the faces of all non-visible extreme points must share one prior;
  - so polytopes with two or more non-visible vertices, including the reversed triangle, are not covered.
- **Convex error levels** do not help (O61 Thm B; ray system with determinant ±25).
- **Concave "charts" are impossible** (E61 Cor 5.2).
- **Unanimity rankings fail too.** Rankings whose worlds are unanimities of arbitrarily many views fail, even with incomplete orders, purely finitely additive levels (via Yosida–Hewitt) and two-sided domains, provided the target pays none of the vetoes (E61 Cor 5.3).
- **The full four-advice domain** (F61 Thms A, B):
  - convex first levels give only normalised boxes;
  - vetoes collapse to sure losses, so with Brier only precise targets are covered;
  - strictly guiding first levels reduce to CPM realisation (Prop E).
- **Reduction.** Within finite-view integral rankings, covering a target such as the reversed triangle forces a CPM-type chart (E61 Thm 5.1, forward direction). The converse needs (LF) at the rays. O61's single-level "iff" must be stated as a sandwich (referee).

## 4. Referee corrections to incorporate
1. The constant-odds-ratio credal set moves to "not covered"; its lower-probability core is covered.
2. ε-contaminations with zeros in p (n ≥ 3): the referee's repair covers every zero pattern. P61 D3's intermediate sentence was false, but its conclusion holds.
3. Scope restrictions:
   - O61 chamfers need s ≤ 1/2;
   - P61's truncation hexagon needs η < 1/10;
   - Rem B′ only for targets in relint Δ;
   - D1 needs μ with a positive density.
4. Delete F61's side remark "A_K ⊇ D_{K′}".
5. O61 Cor A(d): repaired for n = 3 polytopes. A corner tangential from two worlds remains a CONJECTURE.
6. E61 §4.5: wrong reason, but the conclusion holds; it hides a homogeneity assumption. E61 Cor 3.3 needs density points; repaired.
7. O61 §7: the "iff" becomes a sandwich, {unique Bayes acts} ∪ {all full-support Bayes acts} ⊆ U_L ⊆ {all Bayes acts}. "Piecewise-constant local priors fail" is relabelled CONJECTURE.
8. F61 Lemma T0 must add a strictly sign-correct second level.

## 5. Where the frontier is
- **Covered:** the visibility class (all but one extreme point uniformly visible); normalised boxes (two-sided); precise targets (full domain); contaminations (two-sided A_K); every full-dimensional target approximately.
- **Open:** sharp-cornered credal sets (pari-mutuel models, the constant-odds-ratio set, most probability intervals for n ≥ 4) under finite-statistics rankings not covered by the impossibility theorems. That remaining problem is CPM-type. The best supported conjecture is that no non-CPM ranking covers them.
