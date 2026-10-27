# UN66: changes from "Universal coverage by comparison deletion (draft)" to "Universal coverage of coherent sets of desirable gambles (draft)" (26 Oct 2026)

Files written (all in `r66/`):
- `Universal coverage of coherent sets of desirable gambles (draft).tex` and `.pdf`. 17 pages. pdflatex (three passes) gives no warnings, no overfull or underfull boxes and no undefined references.
- `un66build/`: build copies and logs only.

Labels: PROVED (hand proof in the note) / CHECKED / unrefereed. Nothing labelled CONJECTURE or NUMERICS is used in the note.

## Status table

| Item | Content | Source | Status |
|---|---|---|---|
| §2 (framework) | Unchanged from the round-65 note: Lemma 2.1 (D_S), Lemma 2.2 (hull), dominance terms, Brier loss, requirements, Def 2.4 (cover), Lemma 2.5 (LF). (Add) is now defined in §2.4 | round-65 note | refereed CORRECT (REF65_un) |
| §3.1 Lemma 3.1 | (a) a record applies to Z ⟺ it is r(Y,Z) for some Y; (b) r(X,Z) = r(X,Y) ⊔ r(Y,Z) for non-overlapping steps; (c) record relations give reflexivity, a.e. ties, (IB) | round-65 note (attack, ⊔ identity, Lemma 3.1) | refereed CORRECT; (b) now has a full pointwise proof |
| §3.1 Lemma 3.2 | Safety test: safe ⟺ μ(A ∩ hull B) > 0; null record unsafe; B null ⟹ safe ⟺ μ(A ∩ int ℝⁿ₊) > 0; safety upward closed under ⊔ | round-65 Cor 4.2 (attack ⟺ hull-null); AUDIT_r66_extension §2–3 | PROVED; first part refereed (REF65_un item 5); SR66 C1 checks it (6000 records, incl. B null and Q_B = Δ) |
| §3.2 Def 3.3 | **The safe-improvement ranking** (main construction): Acc_i = G_i ∪ {safe r : m_i(r) > 0} | AUDIT_r66_extension §2 (binding) | under refereeing by SR66 |
| Lemma 3.4 | Guidance increments are ≥ 0, = 0 only for null records; ∩_i G_i = {(A,∅): A ⊆ int ℝⁿ₊}, and its non-null members are safe | new write-up of the audit's steps 1 and 4 | PROVED |
| Prop 3.5 | Reflexivity, a.e. ties, (IB); strict Brier increase for every nontrivial comparison (so no nontrivial ties, sub-relation of Brier); (G); (FCC), (TC) and "every cycle is trivial"; (Add) | AUDIT_r66_extension §2 steps 1–3 | PROVED; SR66 C2–C4 |
| Prop 3.6 | **New characterisation**: weak dominance with Y ≠ X ⟺ dominance ⟺ strict dominance ⟺ r(Y,X) safe and m(Y) − m(X) ≫ 0 | new (writer); combines audit steps 4–5 | PROVED; not separately refereed |
| Cor 3.7 | Protection: no coherent model has a weak dominator other than itself | audit step 4 | PROVED; SR66 C5 |
| §3.3 Lemma 3.8, Cor 3.9 | Hull formula hull(B) = cone(B_d) + int ℝⁿ₊; finite witness form of safety | round-65 Lemma 4.3, Cor 4.4 | refereed CORRECT |
| §4.1 Lemma 4.1 | **Contraction lemma** (now its own subsection, with a plain-English gloss) | REF65_hA Lemma S | refereed CORRECT |
| Prop 4.2 | **Hull-preserving shrink**: Q_{X∖N} = Q_X, hull(X∖N) = hull(X) for N ⊆ D_{Q_τ}; plus: if N ⊆ hull(X) and μ(N∖X) > 0 then r(N,X) is safe. Followed by the plain-English mechanism (the additions are implied by the removals) | round-65 Cor 5.2; AUDIT_r66_message | refereed CORRECT (first part); second part a two-line consequence |
| Thm 4.3 | Repair theorem: N coherent, m(N) − m(X) ≫ 0, N ⊆ hull(X) = hull(X∖N), μ(N∖X) > 0, record safe. Proof: relative minimax (Lyapunov + Sion), uniform shrink, Prop 4.2 | round-65 Thm 5.3 (REF65_hA Step 1′ + shrink + Lemma S) | refereed CORRECT; statement now lists hull(X∖N) = hull(X) explicitly |
| Remark 4.4 | (a) hypotheses not used, now also naming where K′ ≠ ∅ and (M) are used; (b) explicit defender and witness; (c) **reworded**: "the proof does not show that r(N₀,X) is safe" (no unproved claim); (d) Step 1 with G = U | round-65 Remark 5.4 | (a),(b),(d) refereed CORRECT |
| Thm 5.1 | Main theorem for the new ranking: (a) axioms incl. (Add), (FCC), no nontrivial ties; (b) 𝒰 = 𝒞* = 𝒞_U; (c) strict dominance of incoherent models with the geometric properties; (d) (GC), (ID), (W), strong (C); (e) covers K ⟺ K full-dimensional and K′ ⊆ relint K | AUDIT_r66_extension §2 Proposition | PROVED; under refereeing (SR66) |
| Def 5.2, Cor 5.3, Cor 5.4 | Universal cover on U; every full-dimensional K covered on some domain | round-65 note | refereed CORRECT; now stated for the new ranking (the proofs use only Lemma 2.5 and Thm 5.1(e)) |
| **Prop 5.5 (corrected)** | (a) If K is lower-dimensional and K′ ⊆ K, then D_K is coherent on U and **undominated, with no weak dominator other than itself**; (b) (LF) fails on every one-sided domain, so no ranking covers K. Paragraph: what fails is (LF), hence coverage as defined; not the admissibility of D_K | AUDIT_r66_message point 4; AUDIT_r66_extension §7.5; BRIEF66 | PROVED; SR66 C8 checks an instance |
| §6 Lemma 6.1 | **Abstract construction lemma**: hypotheses (A1) guidance strictly improves its world's score; (A2) guidance alone cannot weakly dominate a coherent model; (A3) safe repair at every world; (A4) composition of guidance and upward-closed safety on non-overlapping triples. Conclusions (a)–(e), each clause naming the hypotheses it uses. Followed by the verification of (A1)–(A4) for the gamble ranking | AUDIT_r66_extension §3 | PROVED; under refereeing (SR66 §3). See flag 3 |
| placeholder | `% INFINITE-WORLD SECTION: pending refereeing`, between §6 and §7 | BRIEF66 | — |
| §7.1 Example 7.1 | **New**: an exact failure of (Tr) at world 1 for every μ satisfying (M); n = 2, K′ = {(½,½)}; elementary hand proof (balls of radius 1/10, measures δ/2, δ, δ/4) | new (writer). SR66 C7 independently found an exact instance of the same kind | PROVED; not separately refereed |
| §7.2 | Relation to Brier: sub-relation, incomplete; dominance = safe uniform Brier improvement; coherent models that are Brier-dominated yet undominated | round-65 §7.4, Prop 3.6 | as cited |
| §7.3 | Remark on the strict margin: with only a weak improvement the lexicographic score (m_i, Σ_j m_j) would do; Theorem 4.3 makes it unnecessary | AD65 lexicographic variant, adapted | proof sketched ("goes through") — see flag 4 |
| §8 Scope | 8.1 universality relative to a fixed U (plus: finitely many worlds, the coherent models D_Q, (M)); 8.2 coherence-informed definition, protection is definitional but dominance needs Thm 4.3, no cross-world dependence; 8.3 representation, not justification | round-65 §7.1–7.2; BRIEF66 | factual |

## Removed

- The comparison-deleted Brier ranking CD(𝒩): deletion world i(r), Def 3.3, the deletion lemma (Lemma 3.2), the reduction theorem (Theorem 4.1), condition (★), condition (H) and Corollary 4.2's (ID) ⟺ (H). Their content survives where needed: "attack" became "applies to" (Lemma 3.1(a)); the hull test is Lemma 3.2(a).
- Example 7.1 of the round-65 note (failure of (Add) for CD). It concerns CD only, and the new ranking satisfies (Add). It does not transfer: (S₁,∅) is unsafe for the new ranking.
- Proposition 7.2 (the lexicographic ranking LD(𝒩)). Replaced by the short remark §7.3.
- The sentence "Whether a comparison is deleted at world i also depends on the moments of the record at the other worlds": false for the new ranking, and replaced by the opposite, correct statement in §8.2.

## Corrections required by the brief

1. **Lower-dimensional statement.** The round-65 note said only that lower-dimensional K are covered on no one-sided domain. That is true, but it read as if such targets were not admissible. Proposition 5.5(a) now states that D_K is undominated, with no weak dominator other than itself, whenever K′ ⊆ K. The text says that what fails is (LF), and hence coverage as defined. The abstract and §8.1 say the same.
2. **Infinite worlds.** Not included. The placeholder comment is in place. §8.1 says factually that all results concern finitely many worlds.
3. **Scope.** Kept factual, under three headings: fixed U; coherence-informed definition; representation versus justification.

## Flags

1. **SR66.** `SR66_notes.md` arrived before I finished and has been incorporated (see the section below). It found no error in the Proposition. Its abstract-lemma GAP (four unstated hypotheses) does not apply to the note's Lemma 6.1, which states all four explicitly or assumes them; see below.
2. **New, unrefereed content.** Proposition 3.6 (the dominance characterisation) and Example 7.1 (the (Tr) failure) are mine. Both have complete elementary proofs. Proposition 3.6(i)⇒(iv) uses the observation that a non-null record that is guidance at every world is safe (Lemma 3.4(c)). This is what makes "weak dominance by a different model" already strict.
3. **Abstract lemma, hypotheses beyond the audit's §3.** To make the lemma self-contained I had to add:
   - an explicit record map with 0 ⟺ equality;
   - score differences that factor through records (d_ω);
   - an explicit set 𝒯 of non-overlapping triples.

   I stated (Add) as (A4): guidance composes and safety is upward closed on 𝒯. I did not state it as closure of guidance under a disjoint-union operation on records. Measurability plays no role in the abstract lemma.
4. **§7.3 (lexicographic remark).** It asserts that the proofs of Props 3.5 and 3.6 "go through" with the lexicographic score. I checked this by hand: the ordered-group property gives (Add), and the strict lexicographic increment gives (FCC). But no written proof is given in the note. If a referee wants full rigour, delete the remark or expand it into a proposition.
5. **Citations** [KCM, Prop. 2.10] and [KCM, Cor. 5.9] are unchanged from round 65, where REF65_un verified them against the paper's aux file. I did not recompile the covering paper.
6. **Author block:** name only.

## Incorporation of SR66_notes.md

SR66 rates every clause of the Proposition CORRECT (P1–P9, S1–S4), the lower-dimensional correction CORRECT (C1), and confirms that (Tr) fails (X1). Changes made:

| SR66 item | Change in the note |
|---|---|
| X2 (converse: (ID) ⟺ strict safe repair) | Already contained in Prop 3.6. Added a sentence after Prop 3.6 (dominance is never merely weak at some world). Added a paragraph after Thm 5.1: (ID) for this ranking is equivalent to the safe strict repair of Thm 4.3 |
| P6 / Rec. 4 (protection wording) | Cor 3.7 now has a direct proof: r(Y,C) is unsafe, hence guidance at every world; Y∖C ⊆ int ℝⁿ₊ ⊆ C; C∖Y ⊆ {h ≪ 0}, which no coherent model meets. A sentence records that only these two properties of coherent models are used. No claim about two-sided domains is made |
| C1 precisions (i), (ii) | The paragraph after Prop 5.5 now says: (i) lower-dimensional coherent models on U exist iff K′ is not full-dimensional; (ii) for lower-dimensional K ⊇ K′, requirements (i)–(v) hold and exactly (vi) fails; for K′ ⊄ K, (iv) fails as well |
| X1 (Tr fails) | Already Example 7.1 (my hand-proved instance, valid for every μ satisfying (M)). It is of the same type as SR66's C7 |
| L1 (abstract lemma, unstated hypotheses) | Lemma 6.1 already has: null record ∈ guidance (A1); potentials σ_ω with record-based differences d_ω; equality of models as the identity (so null invariance is built into the model class). On the reading of safety: the note defines safety as "not the record of a change out of a coherent model" and **assumes** upward closure in (A4). It does not derive it, so no decomposability is needed. A sentence now says this, and says why (A4) holds in the application (Lemma 3.1(a)) |
| X2 / (R5) in the abstract | Added hypothesis (A5): non-null records that are guidance at every world are safe. Added clause (f): weak dominance by a different model forces a safe record and strict improvement at every world; under (A1) and (A5), (A3) ⟺ every incoherent model is dominated by a coherent one. In the application, (A5) is Lemma 3.4(c) |
| §3.3 (record layer essential) | Added a paragraph after the proof of Lemma 6.1. Without records, "accept improvements out of incoherent models" gives protection and dominance but loses (IB) and (Add). Safety is the record-level substitute |
| §2.5 / Rec. 5 (no cross-world dependence) | Already in §3.2 and §8.2 |
| S1 scope note (two-sided: "Q_B = ∅ or …") | Not included. The note treats only U = D_{K′}, where Q_B ⊇ K′ ≠ ∅ |

The revised note compiles cleanly to 17 pages: no warnings, no overfull or underfull boxes, and no undefined references.

---

# Revision 2 (26 Oct 2026): REF66_un changes and the infinite-world section

Backup of revision 1: `un66build/rev1_backup.tex`. The revised note compiles cleanly with pdflatex (three passes) to **28 pages**: no warnings, no overfull or underfull boxes, and no undefined references. File name unchanged.

**Title.** I propose keeping "Universal coverage of coherent sets of desirable gambles". It is neutral between finite and infinite worlds, and Proposition 7.16 now justifies "coherent sets of desirable gambles" modulo null sets. If a change is wanted: "Universal coverage of coherent sets of desirable gambles, for finitely and infinitely many worlds".

## Part 1: REF66_un required changes

| # | Change |
|---|---|
| R1 (ERROR) | The record-free paragraph after Lemma 6.1 now uses the comparator with the guidance clause: accept if r(X,Y) is guidance, or if Y ∉ 𝒞 and the score improves. It shows both failures with Example 8.1's sets: (IB) fails, because (∅,B) is refused from C but accepted from C∖A; (Add) fails, because C∖(A∪B) ⪯₁ C∖A ⪯₁ C holds with disjoint supports but C∖(A∪B) ⪯₁ C does not. It adds the one-line proof that C∖A is incoherent: a.e. equality with D_Q would force D_Q ⊇ U∖cl A by Lemma 2.1(d), whose convex hull contains A |
| R2 (GAP) | §7.3 deleted. Replaced by one sentence with no claims: "One can also define a lexicographic variant of the ranking, using the score (m_i, Σ_j m_j) at world i; we do not use it." |
| R3 | §9.1 now says that §§2–5 concern finitely many worlds, while Lemma 6.1 and §7 allow any set of worlds. It states the infinite-world coverage set |
| R4 | Remark 4.4(a): K′ ≠ ∅ is used throughout (it makes hull(X) and the maximisers models on U, and Lemma 4.1 applicable) and also in Step 2. (M) is used in Steps 1 and 2 and, through Lemma 2.2(b), in Step 3 |
| R5 | §6, last paragraph: the lemma yields the order-theoretic and dominance clauses. The geometric clauses come from Theorem 4.3, and uniform Brier dominance uses the finiteness of Ω |
| R6 | The paragraph after Theorem 5.1 now says that (ID) is equivalent to the existence of a coherent N with m(N) − m(X) ≫ 0 and a safe record, by Prop 3.6 and Cor 3.7. Theorem 4.3 gives more (hull invariance) |
| R7 | The introduction's gloss of "covers" now includes (C) and D_K ∈ ℳ_U, and points to Definition 2.4 |
| R8 | Witness count r → k; λ_j → t_j (Lemma 3.8, Cor 3.9, Remark 4.4(b)); the separating set E → W in Lemma 3.8 (E now denotes the gamble space); ball B(h,r) → Ball(h,ρ) in Lemma 2.5(c), noting that Lebesgue-null sets are symmetric; aff Δ ≔; Step 1 cites the non-atomicity from §2.1 |

## Part 2: §7 "Infinitely many worlds" (new), with sources and verdicts

Both IW66a and IW66b found the audit theorem (AUDIT_r66_extension §4–5) CORRECT, with no mathematical error. Every repair they requested is incorporated.

| Note | Content | Source | Referee verdict / repair applied |
|---|---|---|---|
| §7.1 setting | Ω arbitrary; E separable, norm-closed, 𝟙 ∈ E; states S; credal sets = weak-* closed convex subsets of S | audit §4 | IW66a S1–S2, IW66b S1–S2: CORRECT |
| Lemma 7.1 | (a) ‖q‖ = 1; S weak-* compact, convex, metrizable. (b) P_S = inf_Ω. (c) Ω̂ := closure of the evaluations; E embeds isometrically, order-preserving and unital, in C(Ω̂); every state is given by a regular Borel probability on Ω̂ (Hahn–Banach with max, then Riesz) | audit §4; (c) IW66b §5 | CORRECT (IW66b, PROVED). Proof of (c) written out here |
| Lemma 7.2 | P_Q 1-Lipschitz; D_Q norm-open; D_{Q₁} ∩ D_{Q₂} = D_{conv}; ∂D_Q ⊆ {P_Q = 0}; P_{(1−τ)Q+τS} = (1−τ)P_Q + τP_S; (d) D_{Q₁} ⊆ D_{Q₂} ⇒ Q₂ ⊆ Q₁ (weak-* separation) | IW66b §1.4, §1.5 (c∞), §2.5 | CORRECT. **Measurability:** D_Q, hull(X), N₀, N_τ norm-open (IW66b S4) |
| (M1)–(M3) and "where used" | first moment; null boundaries for every credal set; full support. **(M3) is used only for identification** (uniqueness of Q, K′ ⊆ Q, (LF)). The defender and protection do not use it | IW66a hypothesis table; IW66b hypotheses 1–5 | CORRECT. The stated (M2) is "every credal set". Lemma 7.3 also gives every nonempty weak-* compact Q |
| Lemma 7.3 (existence of μ) | μ = law of g + t𝟙; ν full support, ∫‖g‖ < ∞, e.g. atomic with Σ w_k(1 + ‖g_k‖) < ∞; λ full support, atomless, first moment. **Φ(g,t) = g + t𝟙 is a linear homeomorphism**, and the product of full-support measures has full support. Fubini gives the null boundaries. The text says μ may be carried by countably many lines | audit §4; IW66a S3/S4 (GAP a, b), IW66b §1.3 (GAP) | Both GAPs repaired as requested |
| Example 7.4 | {P_S = 0} not null ⇒ pure guidance strictly dominates a coherent model: Ω = (0,1], E = span{1, ω}. Added: C∪R is a coherent set of desirable gambles | IW66b §4.3 | IW66b PROVED. My additions: the explicit check that (∅,R) is refused, and (in §7.8) that C∪R differs from every D_Q on a non-null set |
| Lemma 7.5 (coherent-class lemma) | (a) Q_B is credal and contains K′. (b) **For every removed set B**: P_{Q_B} ≥ 0 a.e. on B, and B ⊆ hull(B) a.e. (c) hull(B) is the least D_Q containing B. (d) The infinite-dimensional domain lemma (d∞) under (M3): D_Q ⊆ U a.e. ⟺ K′ ⊆ Q; Q unique; 𝒞_U = coherent models on U | IW66a S6, A1–A3; IW66b §1.5, §2.1, §3.1 | GAPs (unstated domain lemma; hull step for every B) repaired |
| Lemma 7.6 | safe ⟺ applies to no D_Q at all ⟺ μ(A ∩ hull B) > 0; B null ⇒ hull = D_S | IW66b §3.1 (F1), IW66a T4 | CORRECT |
| Theorem 7.7 | Repair theorem. Steps A–D: Step A hull; **Step B relaxed choices F_G, T weak-*-to-norm continuous, Sion's minimax theorem named**, attainment, uniqueness, v > 0, saddle ⇒ indicator; Step C shrink, uniform margin, non-null gain; **Step D contraction (norm convergence in E\*), citing Step A** for P ≥ 0 on the removed part. **Margin at every state**, not only at every world | audit §4 Steps A–D; IW66a B1–B8, C1–C3, D1–D2, P5; IW66b §2 | CORRECT. Citation GAP (Sion) and Step D citation GAP repaired |
| Lemma 7.8 | (a) strict guidance increments (M2 with δ_ω). (b) countable norming set Ω₀. (c) **Step E**: guidance at every world of any norming Ω′ ⇒ (A,∅) with A ⊆ D_S a.e.; such records are guidance everywhere, and safe if non-null | audit Step E; IW66a E1–E3; IW66b §4.1–4.2 | CORRECT |
| Theorem 7.9 | Ranking: (a) reflexive, a.e. ties, (G), (IB), (TC), (FCC), (Add), no nontrivial ties; (b) dominance characterisation; (c) protection; (d) strict dominance with margin at every state; (e) undominated = 𝒞_U, (GC), (ID), (W), strong (C); = all coherent models under (M3). Proof via Lemma 6.1 | audit §4 "Consequently", §4 Step E; IW66a T1–T5; IW66b §3 (E3) | CORRECT. Note: (GC), (ID), (W) and (C) do not need (M3) |
| "Worlds and norming sets" | **Dominance over Ω₀ is defined by different conditions** (positive on Ω₀ gives only inf_Ω ≥ 0). **Same undominated set**: Lemma 6.1 applies with world set Ω₀, and with any Ω′ between Ω₀ and Ω | IW66b §4.2 (F3) | PROVED. See flag 2 |
| Remark 7.10 | The finite setting is the special case; Theorem 7.7 gives Theorem 4.3 without Lyapunov, and for measures singular to Lebesgue | IW66a §1 ("strictly extends") | IW66a NUMERICS on lines. The statement is a direct consequence |
| Remark 7.11 | **Order unit** e with inf e > 0 (transport h ↦ h/e); dead-world counterexample; c₀ open | IW66a P4; IW66b §7.1 | PROVED by both. The transport is written as a remark with its checks listed |
| §7.6 one-sidedness | **New definition** for this section: no nonempty open O with O ⊆ V a.e. and −O ⊆ V a.e.; U is one-sided under (M3) | mine | **Flag 1** |
| Prop 7.12 (**P1**) | Under (M2),(M3): D_K ∈ ℳ_U and (LF) ⟺ K′ ⊆ K and every k ∈ K′ is strictly positive on C_K∖{0}. In finite dimensions: full-dimensional and K′ ⊆ relint K (Lemma 2.5) | IW66a P1 (1 ⇔ 2); IW66b §6.2 (a ⇔ b) | PROVED by both. The normal-cone form (3)/(c) is omitted |
| Theorem 7.13 (**P2**) | (a) Covers K ⟺ the P1 condition; universal cover on U. (b) Every K with K_⊥ = {0} is covered on D_{k₀}, k₀ = Σ 2^{−j} k_j (k₀ ∈ K by norm convergence). (c) K_⊥ ≠ {0} ⇒ (LF) fails on every one-sided domain; in infinite dimensions this excludes finitely generated and precise targets | IW66a P2; IW66b §6.2 | PROVED. (c) uses the one-sidedness of flag 1 |
| Prop 7.14 | **The uniform (tube) (LF) fails**, for every K′ ⊆ K on E = C(Ω), Ω infinite compact metric: bumps on disjoint open sets of vanishing k-mass | IW66a §3 ("PROVED", sketch); IW66b §6.3 | Full proof written here, for any k ∈ K′. **Flag 3** (scope: C(Ω)) |
| Prop 7.15 (contamination) | (a) p full support, every **ε ∈ (0,1]**: covered on D_{p}; D_K undominated **by protection**; (LF) literal with **N = U**. (b) p without full support: (LF) fails on D_{p}. (c) **Nearby result**: for every p, covered on D_{k′}, k′ = (1−ε)p + εr, r full support | audit §5; IW66a K1–K6; IW66b §6.1, §6.4 | CORRECT. Wording repairs applied (protection, literal (LF)). (b) and (c) are PROVED in IW66b |
| Prop 7.16 (**P3**) | Under (M2), every coherent set of desirable gambles D satisfies D_{Q_D} ⊆ D ⊆ C_{Q_D} and D = D_{Q_D} a.e. | IW66a P3; REF66_un §6 (finite case) | PROVED (IW66a). Proof expanded: separation, positivity, bipolar, int cl D = int D |
| §9.3 scope (new) | separability essential (no full-support measure on a nonseparable space; S metrizable ⟺ E separable); order unit needed, c₀ open; null boundary {P_S = 0}; μ-dependence, with mutually singular admissible measures and an explicit set that is coherent for μ and incoherent for μ′; (LF) literal, not uniform; states versus countably additive probabilities on Ω̂; coherent models = coherent sets of desirable gambles modulo μ | IW66a L1–L6, §4; IW66b §8 items 1–6, §7.2 | All requested items included |
| Abstract, introduction, §9.1, §9.4 | Updated to include the infinite-world results | lead | — |

## Not included (deliberately)

- IW66a P1(3) / IW66b §6.2(c), the normal-cone form of the (LF) characterisation.
- IW66b §6.5, contamination in a general separable E with p strictly positive.
- The extension of the ranking to the ideal worlds Ω̂∖Ω.
- IW66b's converse that S non-metrizable ⇒ no full-support measure is not stated as a result. It appears only in the scope bullet, with its one-line argument.
- IW66a's remark that no σ-finite measure is quasi-invariant under all translations (cited there as classical, without proof).

## Flags (Revision 2)

1. **One-sidedness in infinite dimensions (repair beyond both referees).** IW66a P2(c) and the finite Lemma 2.5(c) use −Ball(−h,ρ) ⊆ −V a.e. This needs μ-null sets to be symmetric under h ↦ −h. Lebesgue measure has this property, but the measures of Lemma 7.3 need not: a line g_k + ℝ𝟙 carries mass, while −g_k + ℝ𝟙 may not. §7.6 therefore defines a one-sided domain as one for which no nonempty open O has O ⊆ V a.e. and −O ⊆ V a.e. With that definition the proof is symmetric-free; U = D_{K′} is one-sided under (M3); and in finite dimensions the definition follows from §2's definition. Please have a referee confirm that this is the intended notion.
2. **Ω versus Ω₀.** I state that dominance over Ω₀ is *defined by different conditions*, with the C[0,1] function as illustration, and I prove that the undominated set is the same. I do not exhibit two models whose dominance status actually differs. IW66b also gives none ("No, as relations" is argued at the level of the conditions).
3. **Uniform (LF).** The lead asked for "fails for every infinite Ω". As proved (Prop 7.14), the result is for E = C(Ω) with Ω infinite compact metric. It cannot hold for every E: if E is finite-dimensional, for example span{1, ω, ω²} on [0,1], uniform and literal (LF) coincide by compactness of the unit sphere, even with infinitely many worlds.
4. **My own additions in §7, not separately refereed:**
   - the written proof of Lemma 7.1(c);
   - the general proof of Prop 7.14;
   - the claim in Example 7.4 / §7.8 that C∪R differs from every D_Q on a non-null set;
   - the explicit μ/μ′ example in §9.3;
   - the order-unit transport, written as Remark 7.11 with its checks listed.

   All are short and elementary.
5. **Not verified by me:** I did not run the referees' scripts (`iw66a_py/`, `iw66b_py/`, `ref66un_py/`). I relied on their reported outputs, which are labelled NUMERICS or CHECKED and are not used in the note.

---

# Revision 3 (26 Oct 2026): REF66_iw_section items 1–9 and REF66_un second-round items 1–4

Backup of revision 2: `un66build/rev2_backup.tex`. The note compiles cleanly with pdflatex (three passes) to 28 pages: no warnings, no overfull or underfull boxes, and no undefined references. No theorem, proposition or lemma statement changed, except that Prop 7.16 now also states that D is measurable for the completion of μ.

| Item | Change |
|---|---|
| IW 1 / UN 1 (ERROR, §9.4) | "every dominance relation a uniform Brier improvement" → "a Brier improvement at every world, uniform when Ω is finite; the repair N of Theorem 7.7 improves uniformly in every case" |
| IW 2 (ERROR, before Prop 7.14) | Now: "on E = C(Ω) with Ω infinite the uniform version fails (Prop 7.14), although in other infinite-dimensional spaces it can hold". The ℝ ⊕₁ ℓ¹ example is not included |
| IW 3 / UN 2–4 (abstract, introduction) | Added "full support" to the measure hypotheses, "ε > 0" and "on C(Ω)" for contamination, and "when the space of gambles is infinite-dimensional" for precise and finitely generated targets |
| IW 4 (§7.6, one-sidedness) | Added: (a) the notion depends only on the a.e.-class of V; (b) it is implied by §2's definition under (M) and strictly weaker (V = int ℝⁿ₊ ∪ F with F a closed, symmetric, nowhere dense set of positive measure), so Theorem 7.13(c) extends Lemma 2.5(c); (c) §2's definition fails a.e.-invariance under asymmetric null sets (the union L of the lines, with L ∩ (−L) = ∅, is a.e. equal to E). §7.6 now has a label, and §9.1 says "one-sided in the sense of Section 7.6" |
| IW 5 (G1, relative interior) | "when Ω is infinite", with the one-line proof: s ≤ ((1+t)/t)p is required; take s = δ_x at a p-null point, or a sparse atomic s if p is purely atomic |
| IW 6 (flag 2, norming sets) | Replaced "defined by different conditions" with the referee's example: E = span{1, ω, ω²} on [0,1], Gaussian μ, ω* ∉ Ω₀. The Lyapunov argument gives a safe record with moment β(ω − ω*)², so Y strictly dominates X with world set Ω₀ but not with world set Ω |
| IW 7 (W5, Remark 7.11 and the §9.3 bullet) | "Some order unit is needed" → "Some condition of this kind is needed: [dead world] …; whether a strictly positive gamble without a positive lower bound suffices (c₀, e(n) = 1/n) is open". The scope bullet is renamed "The constants" and reworded the same way |
| IW 8 (G4, Prop 7.16) | Proof reorganised into five numbered steps; the second functional renamed ψ. The statement now says that D is measurable for the completion of μ |
| IW 9 (minor) | Prop 7.14: "h_j ∉ D_K while h_j + t𝟙 ∈ D_K, hence h_j ∈ ∂D_K". Lemma 7.5(d): the converse now cites "K′ ⊆ Q gives P_Q ≤ P_{K′}". §9.3 singular-measures example: "for a credal set Q ⊇ K′". "Where the conditions are used": (M3) is also used for the one-sidedness of U. Lemma 7.1(c): L(1) = q(𝟙) = 1 directly |

Remaining flags from Revision 2: flag 2 (Ω vs Ω₀) is resolved by the referee's example. Flag 3 is confirmed: the C(Ω) restriction is necessary. Flag 1 is confirmed as the right notion, with the justification now in the text. Not verified by me: the referees' scripts, which nothing in the note uses. The new examples (§7.6, norming sets, relative interior) are taken from REF66_iw_section §2–3, where they are PROVED, and I checked each by hand.
