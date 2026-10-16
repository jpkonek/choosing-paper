# Changes, round 9 (14 Oct 2026): "The Contamination Triangle.tex"

Backup of the previous version: `The Contamination Triangle (pre-round9).tex` (775 lines). New version: 1119 lines,
41 pp. Compiles with `latexmk -pdf`: no errors, no undefined references, no overfull boxes. Two underfull-box
warnings (badness ≤ 2293) remain in the `sloppypar` bullet "Earlier no-go for continuous maps" (§8), lines
1082–1083. They are cosmetic.

Line numbers refer to the **new** file. "Old" numbers refer to the backup.

## 1. Global

| Lines | Change | Source |
|---|---|---|
| 37–38 | New macros `\Ltwo` (the class 𝓛₂ˢ) and `\Nb` (the compact collar N₀ᵇ). | — |
| 42 | Date set to 14 October 2026 (round 9). | — |
| 65–70 (old 63–66) | "What is shown". Item 2 (general decomposable domains) rewritten: forced competition, no pinning, reduction to CF(T1). New item 4 (rankings that add up, M0). New item 5 (permitted ties). Item 6 points to the two open questions. | N25–N28 |
| 73 (old 69) | Status paragraph. It now explains CONFIRMED (WITH REPAIR), that referee repairs take precedence, that a referee-only result has been checked by nobody else, and the labels CHECKED and NUMERICS. | brief |
| 86–114 (old 81–94) | Status table. New rows: collar/ray transfer; (TS) always; apex/vertex-free; Lemma R1; CF reduction; diagonal symmetries; CF(T1) open; M0 reduction; structure of E(ψ); p\* ∈ E and genericity; (E_ψ) consequences; R-a′/R-b′; two-world construction; 𝓛₂ˢ; N26 referee Prop R1; permitted ties (theorem, corollary, open window). The row "(E5a), (E4′) open" is replaced. | as in each row |
| 1095, 1109–1114 (old 756, 769) | Sources. Added BRIEF8, N25–N28 (notes and referee reports), the START HERE Glossary and the auditor's note. | — |

## 2. Auditor's corrections (A1–A5)

| Item | Lines | Change |
|---|---|---|
| A1 relevant comparisons | 213–233 (new §2.7) | Def. 2.6(a): B ⪯_i X with B ∈ C_L and X regular. Paragraph after it: restricting to regular X is essential, citing N19 §3.3 (Prop R3). A lexicographic priority on unanimous errors destroys adding-up for unrestricted comparisons but does not help coverage. |
| A2 content of the reduction | 895–907 (Prop 6.13 and the paragraph after it) | Same domain. T1 is Bayes at an interior weighting. At least one coherent Bayes model at **every** weighting. A unique coherent Bayes model at a.e. interior weighting. At exceptional weightings coherent and incoherent minimisers coexist, the additive loss cannot distinguish them, and the original ranking must. |
| A3 non-adjacency | 184 (§2.4), 191 (§2.5) | Plain-words definition: the advice range may contain both acceptances, provided they never compete directly as best advice across an interior weighting boundary (silence may separate them). Adjacency depends on the penalties. "Advice range ⊆ {+,0}" is labelled a sufficient special case. |
| A4 terminology | 213–233, throughout | "Supporting additive assessment" is defined in Def. 2.6(c), with "not claimed to be close" stated explicitly. The phrase "additive approximation" does not occur (checked by grep). |
| A5 M1/M2 | 225–232; 1066 (§7.3 bullet) | (M1) is a finite obstruction to strictly positive error weights, not necessarily an executable sequence of trades. (M2) is no finite obstruction but still no strictly positive supporting weight. The split is called logical bookkeeping, and the reduction is the substantive theorem. The four-trade, overlapping-gain and crossing restrictions are stated to apply only to M1 certificates in that formulation. The old §7.2 bullet (old 727) is rewritten in these terms. |

## 3. §5 General decomposable domains (old 536–609 → new 579–778)

| Lines | Change | Source (note + claim) |
|---|---|---|
| 583–592 | The conic N₀ is replaced by the compact collar N₀ᵇ of the compact set Σ: facet segments, crossings, box-witness limits (−β,0,1), (1,0,−β), and the test-gamble limits. Two numerical conditions: (N1) c̄ < η/√3; (N2) r₁ is chosen after c̄ with \|Ψ_k\| < c̄ on B₁×[0,1]. M_U and Cor 4.2 are unaffected. For a.e. h in ℝ₊N, accepting h lies in the advice range. | N27 Repair 27.1, §1.5 (confirmed, N27_referee §§1, 2.4); N28 Lemma 0 (confirmed with repair = (N1)–(N2)) |
| 594–605 | **Lemma 5.1** (ray transfer of charts; advice ranges along rays; conic chart form of Lemma B1). | N27 Lemma 27.2, Cor 27.3, 27.3′ (confirmed; c-form supplied by N27_referee §2.3) |
| 157–159 (§2.2, after Def. LF) | One paragraph: (LF) is the open-set form. The auditor's example. M_U uses U. Pointer to Lemma 5.1. | N27 §3 edit 2 |
| 608–610 | Lemma quasiconcave now includes N21.1′ (A_τ ⊆ H⁺). The status adds "holds for every g". | N21 Cor N21.1′ (refereed N23 §2); N28_referee §2 |
| 613 | Lemma B1: r₁ satisfies (N2). | N27 Repair 27.1 |
| 620–622 | Thm TS: "(PC) for h near Σ, extended by linearity". | N27_referee §1.4 |
| 629, 656, 661 | Status notes. Thm cuts is sharpened by Thm 5.15. Branch (II) of the dichotomy is empty. Cor R23.4's last sentence no longer needs (TS). | N28 |
| 668–687 | New §5.1. Definitions of walls 𝒲_{m₀} and 𝒜_b. **Lemma 5.12** (convexity facts). | N28 Lemmas 2.1–2.4 (confirmed) |
| 689–695 | **Theorem 5.13** ((TS) in every cover; (E5a) empty). Its status lists the once-refereed inputs. | N28 Prop 3.1, Lemmas 3.2–3.4, Thm 3.5 (confirmed, N28_referee §3) |
| 697–704 | **Corollary 5.14** (branch (I) always; T1 not covered if a non-null set of mixed pairs lacks an orientation; precise vertices, edge confinement). | N28 Cor 3.6 (confirmed) |
| 706 | Notation for (a,b,c), w′, w, λ_b, ℓ′, ℓ. Fact 4.0. The failing pairs for x±. | N28 Fact 4.0; N28_referee `failing_edge.out` (NUMERICS) |
| 708–714 | **Theorem 5.15** (a\* = e_b). | N28 Thm 4.1 (confirmed) |
| 716–722 | **Lemma 5.16** (global one-sidedness of chords). Referee-only. | N28_referee §4.2 Lemma R1 |
| 724–736 | **Proposition 5.17** (vertex-free interiors, chord duality, two-sided chords, no precise chord points, full-neighbourhood identity cap excluded). The strict forms come from Lemma R1. | N28 Prop 4.3 (confirmed), N28_referee §4.2–4.3 |
| 738–746 | New §5.2. **Definition 5.18** CF(T). | N28 §5 |
| 748–754 | **Proposition 5.19** (cover ⇒ CF(T1); converse at CCIBU status; p\* arbitrary). The selection argument is repaired. | N28 Prop 5.1 (CHECKED), N28_referee §5.1 repair |
| 756–763 | **Proposition 5.20** (a), (b) diagonal invariance of CF. (c) is the ranking-level symmetry for every T and every transport-closed class (referee-only). | N28 Prop 5.2; N28_referee Prop R3 |
| 765 | (E4″) is CF(T1) together with the necessary conditions. The list is not exhaustive. | N28_referee §6 repairs 1, 6 |
| 768–778 (old 601–609) | "What remains open" rewritten. (E5a) closed. (E4′) reduced to CF(T1). **The sector-cap example C1 is recorded (NUMERICS)**: N28's derived constraints do not exclude vertex-scale consistency, and N28's inference to the contrary was wrong. NUMERICS N1. Where a solution would have to live. Conjecture 5.21 is now "CF(T1) has no solution", replacing Conj N21, with the two directions of the equivalence stated separately. | N28_referee §§4.3, 6, 7 |

## 4. §6 Coherent almost-preferences and rankings that add up (old 611–712 → new 780–1007)

| Lines | Change | Source |
|---|---|---|
| 780 | Section retitled. | — |
| 856–859 | **Remark 6.9**: on M_U, E(P) is a countable union of vertex-cutting atom chords. (U) fails iff every member choice has one. Flagged as our application of Thm 6.14. | N25_referee Prop F (applied here) |
| 887–893 | New §6.5. Standing hypotheses (H_M0). Definitions of B_q, Z_q, E(ψ), V_ψ and the face 𝔉_t. | N25 §0 standing hypotheses |
| 895–907 | **Proposition 6.13** (α)–(δ) and E(ψ) ≠ ∅. The citations follow the N25 referee: N17 Prop 2.1 / N19, N13 Prop B, N19 Prop R3(a), N22 Cor 2.3 / N24. | N25_referee §3 |
| 909–922 | **Theorem 6.14** (structure of E(ψ)). (a) differentiability. (b) a countable union of atom chords, each cutting off the odd-world vertex, and **no fan points**. (c) countability on other lines. (d) coherent envelopes; coexistence of coherent and incoherent minimisers. (e) atom anatomy. | N25 Claim 1 = Thm 2.1, Cor 2.2; Thm 3.3; Thm 4.1 (confirmed). "No fans" is N25_referee Prop F (**referee only**) |
| 924–929 | **Theorem 6.15** (p\* ∈ E blocks the chain), as repaired. Addition: the accepting extreme and corner pattern (CHECKED). | N25 Thm 9.1; N25_referee §4 repair and addition (N26 Prop 4.3 transferred) |
| 931–939 | **Proposition 6.16** (genericity, as repaired: normalise the charges; rescaling invariance; every ψ ∈ 𝒩 has an atom chord in a cover). | N25 Thm 6.2, Prop 6.4(a); N25_referee §§1, 3 (part (c) referee-only) |
| 941 | The hypothesis (E_ψ): definition, when it holds, why it is not automatic. j-improvable, ℓ°, splits. | N25 standing hyp., N25.12; N25_referee §3 |
| 943–953 | **Proposition 6.17** (consequences of (E_ψ)): face points selected; profile continuity; staircase; ideal tie-breaking; IB transport along chords. | N25 Lemma 1.2, Lemmas 7.1–7.4, Thm 7.5, Cor 7.6, Lemma 8.1, Thm 8.2 (confirmed) |
| 955–963 | New §6.6. Residuals **R-a′, R-b′** as corrected. Fans and N25.L closed or vacuous. Localisation: N25 Prop 9.3 (CHECKED); the edge box is E-robust; Lemma chords/levels survive off a null E; the clopen step across a chord is the genuine obstruction. | N25_referee §§5, 7; N25 Props 9.2, 9.3; N26_referee §4.2 |
| 965–967 | New §6.7. Definition of 𝓛₂ˢ and of "improvable". | N26 §0 |
| 969–981 | **Theorem 6.18** (N26.1: the two-world ranking resolving an exceptional additive tie, intermediate target). Marked as a genuine M0 mechanism with no coverage gain in n = 2. | N26 §1 (confirmed, N26_referee §1) |
| 983–994 | **Theorem 6.19** (N26.2–N26.7 for 𝓛₂ˢ, ψ = primary, as repaired). The status line states that the results do **not** transfer to general M0 rankings, and why. | N26 Lemmas 2.1–2.3, Thm 3.1, Cor 3.2, Thm 3.3, Cor 3.4, Thm 4.1, Cor 4.2; N26_referee §§2–3; N25_referee §6 |
| 996–1002 | **Proposition 6.20** (the pivot cluster-line conclusion removes the chords in 𝓛₂ˢ). Referee-only. | N26_referee §4.3 Prop R1 |
| 1004–1007 | **Conjecture 6.21** (N26.R, sharpened; N26.R′). | N26 §4.4; N26_referee §4 (R2 CHECKED sketch, R3) |

## 5. §7 "What is excluded and what is open" (old 714–735 → new 1009–1074)

Section numbers are unchanged (the M0 material is inside §6). Inside §7 the new §7.1 shifts the old subsections: old §7.1 (weakened guidance) is now §7.2, old §7.2 is §7.3, and old §7.3 is §7.4.

| Lines | Change | Source |
|---|---|---|
| 1011–1022 | New §7.1 "Two concrete open questions", in the auditor's framing. The two escapes. Neither has been ruled out. (Q1): can exceptional additive ties be resolved ordinally? It does not demand that ψ satisfy (S)/(C), nor that its Bayes weights equal the selection indices. (Q2): can two-sided domains (advice range {+,0,−}) cover T1 additively, i.e. CF(T1)? No forced move to approximation. | auditor's note; BRIEF8 |
| 1028 (old 720) | Permitted-ties bullet: "has not been examined" is replaced by a pointer to Thm 7.1. | N27 §3 edit 3 |
| 1030 | (C) forces (BU) for every θ and both norms. The BRIEF4/N5/N7 IBU caveat is deleted. | N27 Prop 27.4; N27_referee §3.1 |
| 1032–1037 | Definitions: permitted-tie realisation, (X_ik), (VP), θ_x(T). | N27 §§2.1–2.2 |
| 1039–1049 | **Theorem 7.1**. Sup norm: every θ ∈ (0,1). Euclidean: θ < √((κ²+1)/(κ²+2)). θ < √(2/3) uniformly in ε. Same with (VP). Referee addition on the half-space maximiser. | N27 Thm 27.6, Prop 27.4, Lemmas 27.5, 27.5′ (confirmed, N27_referee §§3, 6) |
| 1051–1053 | **Corollary 7.2** (non-adjacent (LF) domains), CHECKED. Lemma 27.7 is described in words. | N27 Cor 27.8, Lemma 27.7; N27_referee §4 |
| 1055–1058 | Open Euclidean window, with (VP) as repaired: "not automatic" rather than "fails"; the all-tied configuration; the vertex-limit form; W′ = co(K′ ∪ {e_l, v_k}) replaces [e_l, v_k]; the conjecture stated norm by norm. Not examined: adjacent domains and charges under ties. | N27 §2.7; N27_referee §5 |
| 1064 | Lexicographic bullet: pointer to 𝓛₂ˢ results and Conj 6.21. | N26 |
| 1065 | Arbitrary-preorder bullet: pointer to M0 (§§6.5–6.6, Q1). | N25 |
| 1066 (old 727) | "Rankings that do not add up" rewritten with M1/M2 (A5). The identification of the "almost every" gap with the M0 residual is attributed to BRIEF8/N25 §10. The identification with (U) is marked as ours. | N17, N19 §4, auditor |
| 1082 (old 743) | Positive-results bullet: "general decomposable domains: open and reduces to CF(T1)". | N28 |

## 6. Points where notes and referees disagreed, and how they were resolved

In every case the refereed version was used.
1. **N28 §0.5, §6, Conj N28 evidence.** N28 says that excluding the identity cap removes the support for vertex-scale
   consistency. The N28 referee says this is WRONG: the sector cap C1 passes every derived constraint (NUMERICS). Lines
   770–771 state the referee's position, and say explicitly that N28's inference was wrong.
2. **N28 Def 5.3.** N28 presents (E4″) as a proper sub-case of CF(T1). The referee shows (E4″) = CF(T1) (via Prop 5.1 ⇐)
   and that the constraint list is not exhaustive. Line 765 follows the referee.
3. **N28 Prop 5.1.** The note's measurable-selection sentence is invalid. The referee's polygon test is used. (⇒) is
   specific to T1, and (⇐) has CCIBU status (lines 748–754).
4. **N28 Lemma 0.** It omits N27's two quantitative conditions. These are adopted as (N1)–(N2).
5. **N28 Remark after Prop 4.3 (CHECKED).** It is superseded by the referee's Lemma R1 (PROVED, one reader).
6. **N27 §0/§2.7.** N27 says "(X_lk) fails for θ ≥ θ_x". The referee says it is "not automatic". N27's escape
   W = [e_l, v_k] is replaced by the referee's W′. The conjecture is stated by norm.
7. **N25 Thm 9.1.** N25 claims "no limit at p\*". The referee repairs this to "does not converge to 0", which suffices.
8. **N25 Thm 6.2.** The normalisation is repaired (charges, not ∫|c_k|).
9. **N25 fan points (Thm 5.1, Remark 5.2 "natural escape", R-c, Conj N25.L).** The N25 referee proves Prop F: there are
   no fans. Fan configurations are therefore recorded as closed and N25.L as vacuous. Prop F is labelled referee-only.
10. **N26 referee §3.3 vs N25 referee Prop F.** The N26 referee lists fans as open for general M0 rankings and gives a
    strictly signed field with a fan point. That field lacks property (γ), so it is consistent with Prop F, and the
    N26 referee did not have Prop F. The status of Thm 6.14 records this.
11. **N26 Cor 3.2, Thm 3.3, Lemma 2.2 summaries.** The ±σ patterns, the fixed-segment faces and the
    "multiplier values" wording all follow the referee.
12. **N26 Prop 4.3.** The single-pattern hypothesis is not automatic. It is used only as a conditional (Thm 6.15,
    addition).
13. **N26 claims vs generality.** N26.5–N26.7 are stated for 𝓛₂ˢ with ψ = primary only. Both referees agree that they
    do not transfer. "No isolated exceptional point" holds in general, but only via Prop F.
14. **N25 citation of (α)–(δ).** N25 cites N22 Thm 2.1. The referee asks for N19 §2.2 with N13 Prop B, and that is what
    is used.
15. **N25 §0.** It says (E_ψ) is used "only in §§1.2, 7–9". The referee notes that Lemma 1.1 also uses it. The writeup
    states (E_ψ) explicitly wherever it is needed.

## 7. Statements added by the editor (not in the sources), flagged in the text

- Remark 6.9 (line 857): Thm 6.14 / Prop F applied to the (CP-a) field ψ^P on M_U.
- Line 962: the referee's "Lemma levels survives off E" is used beyond 𝓛₂ˢ, marked "on our reading" (N25_referee §5
  makes the same point for straight levels).
- Line 1066: identifying the "almost every" gap with (U).

## 8. Files

- `writeup/The Contamination Triangle.tex` (edited) and its PDF and build files (regenerated).
- `writeup/The Contamination Triangle (pre-round9).tex` (backup).
- `writeup/CHANGES_round9.md` (this file).
- Two temporary text fragments and a build log were written to the session scratchpad (outside `r9/`) during editing.
  Nothing was deleted.
