# Check report: "The Contamination Triangle.tex"

13 Oct 2026. Independent check of the consolidated note against its sources (N11–N15, N18, N20–N24, R10a/b, R12,
R15, R18, R1/R2/R4/R6/R8 via the Consolidated Statements, CCIBU.tex, N4, N7, N9, N10, N17, N19, BRIEF–BRIEF7,
LDG v2, v3, CONTAMINATION_NOGO, Walley 1991 extract lines 8200–8600). I did not write the note or N23.
The note compiles cleanly after the edits (latexmk, no warnings, no overfull boxes).

## 1. Second reading of the one-reader results in N23

All three verdicts: **CORRECT**. No repair needed.

**Lemma R23.1 (N23 §7.1).** CORRECT.
- Step 1 (B ⊆ Γ_{v_k}): concavity gives Ψ ≥ 0 on B × [σ₁,σ₂]. Every point of F_k ∩ cl Ũ is a positive multiple of a
  convex combination of h(σ₁), h(σ₂) once Ũ is small, so K_q ⊆ {m·h(σ₁) ≥ 0, m·h(σ₂) ≥ 0} ⊆ W_{v_k}(Ũ), and R10b §1
  gives q ∈ Γ. Shrinking R10b's ball keeps the UVN and w_± requirements (as N18 §1.5 / N20 §3 note).
- Step 2: U ⊆ int N₀ is needed so that U⁻ ⊆ N₀; then N21.2 (K_q ⊇ K″ on B ⊆ B₁, Thm B) gives no d-faces of a.e.
  h ∈ U⁻ meeting B. Correct.
- Step 3: R10b Cor PL2's proof (Lemma M Steps 2–4 with Step 1 replaced by the no-d-face hypothesis) uses only that G is
  open, connected and inside Γ_v; containing p\* is harmless. So B ⊆ α or B ⊆ β.
- Step 4: p\* ∈ B ⊆ Γ and v_k ∈ T = K_{p\*}, so p\* ∈ α, hence B ⊆ α (α = {q ∈ Γ : v_k ∈ K_q}, R10b Lemma D).
- Step 5: Ψ(q,τ) ≤ v_k·h(τ) = 0 on [0,1]; with Step 1, Ψ(q,·) ≡ 0 on [σ₁,σ₂].

**Cor R23.2 (N23 §7.2).** CORRECT.
- Step 1: I re-checked that N21.4 items 1–4 use only the A-half on the given facet: A_τ ∩ B₁ is a proper non-empty
  half-plane ∩ B₁ (local straight levels, p\* ∈ cl A_τ ∖ A_τ), so p\* lies on its boundary; A_τ ⊆ H⁺_τ globally
  (N21.1′); betweenness/monotone pieces as in N15 Step 2; continuity (Step 3) uses Z_{τ₀} ∩ B₁ =
  {Ψ ≥ 0} ∩ (B₁ ∖ H⁺) convex and the jump double-wedge, contradicting p\* ∈ cl A_{τ₀}.
- Step 2: D⁻ ⊆ Z_{τ₀}; if n_{τ₁} ≠ n_{τ₀}, A_{τ₁} ∩ D⁻ ≠ ∅ (also when n_{τ₁} = −n_{τ₀}); concavity gives Ψ(q,τ) > 0
  strictly between τ₀ and τ₁, then continuity of n gives the contradiction. So n is constant.
- Step 3: if B_τ accumulates at p\* for τ < τ_i, local straight levels put p\* on ∂B_τ, the two lines through p\* cannot
  cross in B₁ and coincide, and the c-cluster argument (R15 Lemma C on B₁) gives n·(e_i − p\*) ≤ 0, against > 0 from
  V_i ∩ Ω ⊆ A_τ ⊆ H⁺ for τ > τ_i. Same at τ_j.
- Steps 4–5: Lemma R23.1 with σ₁ = τ′ < τ_i < σ₂ = τ‴ gives A_{τ_i} ∩ B(p\*,ρ) = ∅, contradicting p\* ∈ cl A_{τ_i}.

**Cor R23.4 (N23 §7.5).** CORRECT.
- (TS) case: N21.7(b) (needs a failing box at every b, exact for T1).
- Otherwise: by R23.2 some facet has p\* ∉ cl A_τ, which is exactly N21.9's hypothesis. N21.9(i) (σ₁,σ₂ as in N15
  Step 1, so p\* ∈ cl G, O ≠ ∅), (ii) (first point of cl β on a segment from O to V_j is in ∂_Gβ, so K_Q = {v_k} by
  Lemma M) and (iii) (B_Q ≈ {v_k·h > 0} ∪ {h ≥ 0} ⊆ Av) re-derived. For a.e. mixed g one of ±g has v_k·(±g) > 0.
- The two corollary sentences in the note follow (contrapositive; N21.8(b)).
- Not checked: Prop R23.3 (refined (E5a)); it is not used in any statement of the note.

## 2. Formula checks (all correct as printed)

- κ = (1+2ε)/(1−ε) = 1 + 3ε/(1−ε); c₀(κ−1) = ε; D_{T₁} and D_K as in BRIEF/BRIEF6.
- Corner rays r₁₂ = (−1,−1,κ+1) etc. and crossings w₂₁ = (−1,0,κ), w₃₁ = (−1,κ,0): verified against v₁, v₂, v₃.
- c₁, c₂, c₃ forms; corner equation x₁ + 1/x₂ = κ+1 (recomputed at r₁₂ and r₂₃); Möbius matrix, det 1, trace κ+1;
  x + 1/x = κ + 1.
- Box: A ∈ relint F₁, B ∈ relint F₃ (membership via c₀(1−β) = εβ), chart values xη(1−2s) − s and sx − (1−s)ζ, ratio
  condition η < βζ(1+η), limit βx² > 1 ⇒ x² ≤ κ. Transposition step: c^σ is a realisation and its facet ratio is
  1/x (recomputed), giving 1/κ ≤ x² ≤ κ. (κ+1) − (y+1/y) = (y−1)(y²+1)/y; x₊²/κ ≈ 3.80 at ε = 0.3.
- General all-facing pinching: matches R15 Thm 6.2 Steps 2–6 and R18 §6.
- Lemma signs proof (r_j > 0 at r_{ki}, τ_i < τ_j): correct.
- (CP-a) vs Walley 1991 Thm 3.8.1: X ≽ Y iff P̲(X−Y) ≥ 0 with rewards −Λ gives X ⪯_i Y iff P̲_i(Λ_iY − Λ_iX) ≥ 0;
  citations 3.3.3 (lower envelope) and §3.6 (weak-* compactness) are right; D0–D4, R0–R5 labels right; (CP-s) matches
  Thm 3.8.1(5) read as ≻ ∪ =. The null-invariance equivalence matches N24 §5.
- (IB) matches v3 eq. (independence); Theorem kkm matches LDG v2 thm:kkm.

## 3. Issues found and changed

| # | Where | Issue | Change |
|---|---|---|---|
| 1 | Intro, item 1 | "If an additive ranking covers T₁, the Bayes models … with half-plane charts": half-plane charts hold on M_U (Prop reduction), not on general decomposable domains | Added "on the U-domain" (the domain whose evaluable models are the measurable subsets of U = D_{K′}) |
| 2 | Intro item 1; Cor coverage | "pairs near the boundary of D_{T₁}" / "pairs near ∂D_{T₁} have advice range {+,0}" is weaker than the proved hypothesis: non-adjacency of all pairs with an orientation in D_{K′} ⊇ cl D_T∖0 (N14 §3(iv), N15.9, N18 §1.10). N14 §6 and N18 §5 loosely list two-element advice ranges near ∂T | Aligned both with the definition (pairs with an orientation in D_{K′}); added a sentence in the Cor coverage status explaining this |
| 3 | Intro, item 3 | Complete-worlds result stated without (UN) (N24 repair; N22 Cor 3.2) | Added "(on the U-domain, or under a mild domain condition (UN))" |
| 4 | Cor realisation | Statement mixed "a ranking covers T" with "there is such a ranking", and omitted (LF) on M and (LA), (S), (C) for the covering ranking | Restated as an equivalence between two existence claims on a decomposable domain with (LF) |
| 5 | §5, failing-box paragraph | Λ_{ab} never defined; β used for 1/κ while β = c′·q two lines earlier | Added a one-line gloss of Λ_{ab} (R15's vertex-limit ratio); wrote κ⁻², x₊²/κ, 1/(κx₊²) instead of β², βx₊², β/x₊² |
| 6 | Lemma R23.1, Cor R23.2, Cor R23.4 status lines; summary table | One-reader status | Updated to "second reading: CORRECT (CHECK_REPORT.md)" |
| 7 | Thm dichotomy status; table | Said the A-half refinement and R23.3 "rest on Cor R23.2 and are one-reader results". In fact branch (II) as stated itself needs R23.2, and R23.3 does not rest on R23.2 and is not used | Rewritten accordingly; table row notes that (II) also uses Cor R23.2 |
| 8 | Lemma signs status | "(both refereed)" for proofs that were written by the referees themselves | "general proof supplied independently by both referees of N15" |
| 9 | Lemma levels | "{f=t} is the region between two lines" only when both half-planes are proper (N15 Lemma 2.1) | Added "when both half-planes are proper" |
| 10 | Thm nosliding proof | (0,ε) clashes with the contamination parameter | Replaced by (0,η) |
| 11 | §6.5 (CP-b) | "countably many members strictly separate D_i ⇒ reduction as in Cor DCA or Thm integral": N11 Thm 6.4 needs the separating members all CA (then N11.2/Cor DCA conclusions) or all SN (then N11 Thm 5.5), and Thm integral is N22, not N11 | Restated with the CA proviso and the SN alternative |
| 12 | Table row, Cor charges | "refereed (N14 Thm C2 …)": Thm C2 was proved in the N14 referee report; its splice step was refereed as N22 Lemma 3.0 in N24 | Reworded |
| 13 | §7.1 permitted ties | Cited BRIEF5, which is the non-additive-rankings brief | Cite BRIEF4 only |
| 14 | §7.3 | "about 1350 random triangles"; R18 §7 counts 1340 | "about 1340" |
| 15 | §7.3 | "first-order arguments of §§4.1–4.6": §4.6 is the triangle-specific contradiction; N15 says §§2–6 = note §§4.1–4.5 | "§§4.1–4.5" |
| 16 | Style | Definitions written with "=" | \coloneqq for Ω, supp p, K′, λ (Lemma sandwich), W (pivot Step 3), Δθ, q (Lemma rotation), C_J, ϑ, δ_Y, O (edge box), q₀, ζ, η (box), A_r, B_r, s, t, α, β (§5) |

Style checks: no optional [..] names on theorem environments (none found); no red or coloured text (none found).

## 4. Checked and found faithful (no change)

Prop necessary (R1 Lemmas 1.4–1.5, Thm 2.2(N), Prop 2.6, R2 Lemma U, R6); Prop reduction and converse (N12 §1, N14
§2.1); Thm ccibu (CCIBU.tex; BRIEF2; N13 §2); Remark N20 (N20 §8); every lemma of §4 and its referee citations
(N15, N18, N20, N12, N14, R10b, R12); Prop boxbridge (N12 Thm 3.1, N14 §2.5, R18 §5); §5 statements (N21.1, N21.2 as
strengthened, N21.4, N21.5, N21.6, N21.7, N21.8, N21.9, (E5a), (E4′), Conj N21; N23 verdicts); §6 (N22 Lemma 1.0,
Thm 1.2, Thm 2.1, Cor 2.3, Thm 3.1, Cor 3.2, Prop 4.1; N24 §§1–6 including Props R1, R2 and the repairs; N11 §6;
N13 Prop A); §7 (N4, N7, N10, N19); §8 (R10a Thm M, Prop M′, Thm R, R12; NOGO §§2, 4–5).

## 5. Not changed, and why

- Prop A: the note says "even without (LA), (C) or a target"; N13 also drops (G). An understatement; left as is.
- Intro: "the same target was shown to have no continuous realiser" abbreviates the NOGO scope (continuous, positively
  homogeneous CPMs with weak, generically strict signs on an open convex conic domain). §8 states the scope; left.
- Thm main / Cor coverage rest on CCIBU only for the converse direction; CCIBU has no formal referee report. The note
  says so; nothing to change.
- Prop R23.3 (used only in the open-case description of (E5a)): not second-read; its status remains one reader.
- The "two-element advice ranges near ∂T" instance (issue 2): it is plausible that the proof only uses gambles near ∂D_T, but I did not
  verify this, so I aligned the note with the hypothesis that is proved rather than strengthening the sources' claim.
