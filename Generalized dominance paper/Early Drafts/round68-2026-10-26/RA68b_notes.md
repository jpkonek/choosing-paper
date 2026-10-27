# RA68b: referee report on "Coherence and accuracy for sets of desirable gambles" (definitive, 24 pp.)

26 October 2026. Independent referee. I read the `.tex` line by line and the PDF, and re-derived every proof in the manuscript itself rather than in its sources. I did not read `RA68a_notes.md`.

**Context read:**
- `BRIEF68.md`, `AUDIT_r68_message.md` and `WA68_changes.md`;
- `REF67_out_notes.md` and the GAP/ERROR rows of `RF67a`/`RF67b`;
- COV §§2, 4 (`def:cover`, `thm:family`, `thm:cover`, `cor:contam`);
- `VB_dominance_note.md` and `REF61_pos_notes.md` §1.

**Scripts:** `ra68b_py/checks.py`, with output in `ra68b_py/checks.out`. These are Monte Carlo sanity checks of Ex 6.4, Rem 4.4 (both parts, plus the incoherent variant) and Ex B.1. They are only sanity checks; every claim was checked by hand.

## 0. Bottom line

All the mathematics in the manuscript is correct. I found no error in any proof, and no proof depends on LDG or on deleted material. The PDF compiles cleanly to 24 pages with no warnings, no undefined references and no overfull boxes.

There is **one ERROR in a statement**. It is a definitional mismatch with an easy repair:
- §6.3, requirement (1), imports "acyclicity (as in Proposition 6.2(b))". That clause includes "every cycle consists of models equal a.e.".
- The veto–Brier ranking fails that clause, so "Hence the veto–Brier ranking covers K" (Thm 8.1) is false as literally written.

There are also **two overclaims** that need text changes:
- §9.1 says "the same holds" on hull-closed domains.
- §1 and §8 say the "weaker ordering structure is not needed to cover genuinely imprecise targets".

There are **two scholarly gaps** that a top journal would require:
- the IP-specialist definition of coherence in the abstract and the first paragraph;
- the missing IP-accuracy literature, together with "requirements usually placed on accuracy rankings".

Everything else is minor.

## 1. Verdict per numbered result

| Result | Verdict | Notes (my re-derivation) |
|---|---|---|
| Lemma 2.1(a)–(f) | **CORRECT** | (a) Norm 1 via −‖h‖𝟙 ≤ h ≤ ‖h‖𝟙. Weak-* compact by Banach–Alaoglu. Metrizable by separability. (c) ∂D_Q = {P_Q = 0}: cl D_Q ⊆ {P_Q ≥ 0}, and h + t𝟙 ∈ D_Q when P_Q(h) = 0. conv(Q₁∪Q₂) is the continuous image of Q₁×Q₂×[0,1]. (e) Strict weak-* separation, with weak-* functionals equal to evaluations. (f) Dense sequence plus a 2η estimate. |
| Lemma 2.2 | **CORRECT** | Φ(g,t) = g + t𝟙 is a linear homeomorphism E₀×ℝ → E, so the Borel σ-algebra is the product σ-algebra (both factors are separable metric spaces). (M2) follows by Fubini because {P_Q = 0} is a graph over E₀. (M3) holds because ν has dense atoms. In ℝⁿ, (M2) holds by the line-section argument. |
| Lemma 2.3(a) | **CORRECT** | Uses only (M3), not (M2). O ∩ {P_Q < 0} is open and null, hence empty. Then shift by −η𝟙. |
| Lemma 2.3(b) | **CORRECT** | Steps 1–5 check: int D ⊇ D_S ≠ ∅; nonnegative functionals are multiples of K_D; Hahn–Banach on int D; bipolar gives cl D = C_{K_D}; int cl D = int D. D is completion-measurable because it is sandwiched between D_{K_D} and C_{K_D}, and the difference is null by (M2). The Walley converse also checks. See §2(i) for the framing issue. |
| Lemma 2.4(a)–(d) | **CORRECT** | (M2) is flagged exactly where it is used: (b) second sentence, (c) converse, and (d). (d) uses (M2) for {q}. |
| Def 2.5, Lemma 2.6 | **CORRECT** | The "only if" direction does not need (M2). The two-disjunct remark is right. |
| Lemma 2.7 | **CORRECT** | The indicator identity holds off (X△Y)∩(Y△Z). |
| Lemma 3.1 | **CORRECT** | L^∞ = (L¹)\* because μ is finite. F_G is weak-* compact. T is a uniform limit of weak-*-to-norm continuous maps T_k, so Z is norm-compact and convex. Sion applies with S (weak-\*) and Z (norm) compact and convex, and Φ continuous and affine in each variable. Attainment holds by continuity / lower semicontinuity. Saddle chain: v = min_S Φ(·,z\*) ≤ Φ(q\*,z\*) ≤ max_Z Φ(q\*,·) = v. Uniqueness uses (M2) for {q\*}. |
| Cor 3.2 | **CORRECT** | 𝟙_X ∈ F_G uses (M2) through 2.4(b). If v = 0, then X = N\* a.e., which is coherent. |
| Cor 3.3(a)–(c) | **CORRECT** | The bracket is ∫_X q⁻. Then m(X) = m(X₊) + m(L) off {q\* = 0}. L is inconsistent because q(m(L)) ≤ −v < 0. |
| Lemma 4.1 | **CORRECT** | T′(q′) − q = (c/(1+c))(q′ − q), so the iterates converge in norm. No measure assumption is needed. |
| Lemma 4.2 | **CORRECT** | Uses Lemma 2.1(d) for Q_X and only the first sentence of 2.4(b), so no (M2). |
| Lemma 4.3 | **CORRECT** | |
| Remark 4.4 | **CORRECT** | First part (new): both coordinates of m(N) equal ∫_W(h₁+h₂) > 0, since h₁+h₂ ≥ 2 − ½√2 on W. D_Δ misses N. MC gives (0.00201, 0.00197), equal within sampling error. Second part: Q_B = {(½,½)} (MC confirms the masses at t ≠ ½). N ⊆ hull(B) by 2.1(e), and (½,½)·m(B) ≈ 0.083 > 0. The "same mechanism" family "∅ ≠ Q_B ⊆ Q" is correct (REF67_out U3 repaired). **Weakness:** X = N ∪ B = {h₁+h₂ > 0} is itself coherent. See change 11. |
| Thm 5.1 | **CORRECT** | Consistent case: N_τ ↑ N₀ as τ ↓ 0 because P_{Q_τ} = P − τ(P − P_S) is non-increasing in τ. Dominated convergence by (M1). The (2) inclusions are literal. μ(N∖X) > 0 via Lemma 2.6. Inconsistent case: G₁ = hull(X₊) ⊆ {q\* > 0} as sets. v₁ ≥ v via 𝟙_{X₊} ∈ F_{G₁}. L ⊆ X∖N literally, and Q_{X∖N} ⊆ Q_L = ∅. The location clause is proved for the (B) region, so REF67_out C18 is repaired. |
| Remark 5.2 | **CORRECT** | (c) is right: atoms are allowed, e.g. μ = δ_𝟙 + δ_{−𝟙} satisfies (M2). |
| Def 6.1 | — | Clear. The plain-language rule matches the clauses. |
| Prop 6.2 | **CORRECT** | Needs no (M2) and no (M3). The guided increment is ∫_A\|h(ω)\| + ∫_B\|h(ω)\| > 0. In (c), the non-guided part is clause (ii); "cannot be made" passes to the union by 2.7; the other part has increment ≥ 0. **But see change 1** about the bullet "every cycle consists of models equal a.e.". It is true for this ranking, but it is not a requirement that other rankings meet. |
| Prop 6.3 | **CORRECT, with no assumption beyond (M1)** | ⪯_ω has (1) by clause (i), (2) by 6.2(b), and (3) because clause (ii) applies only where no coherent model can make the change. Maximality: if X = Y a.e., the change is null, hence guided; otherwise (2) gives a strict gain; then either (3) forces guidance (clause (i)) or clause (ii) applies. **It holds without (M2) or (M3)**, since neither Def 6.1 nor 6.2(b) uses them. (M1) is needed only to define m_ω. The lead's check in BRIEF68 is correct. |
| Ex 6.4 | **CORRECT** | Exact bounds: a′ − ⅗b′ > (0.04, 1.04); increment > 1.075δ. Balls inside C, since min(h₁+h₂) ≥ 0.86. X⪯₁Y⪯₁C, but X and C are incomparable at world 1. Not X⪯₁C: C can make the change and B₊ ⊆ {h₁ > 0}. Not C⪯₁X: m₁(B) < −1.9δ + 0.275δ. The move to ℝ² is sound: it needs 2.6 with B consistent, and μ(A ∩ hull B) = μ(A) > 0. |
| Lemma 6.5 | **CORRECT** | The countable union of null sets comes from guidance itself, not from (M2). (M2) is used only for {P_S = 0}. |
| Prop 6.6 | **CORRECT** | Under (M2). |
| Prop 6.7 | **CORRECT** | The direct (i)⇒(iv) is valid. (iv)⇒(iii) needs no (M2). |
| Thm 6.8 | **CORRECT** | Proof assembly checked. "Without (M3) everything holds except the bijection" is accurate; see §2(ii). |
| Cor 7.1(a)–(d) | **CORRECT** | (a) hull(B) ∩ U is a coherent model on U. (b) Uses the location clause. (c) The restricted ranking is the restriction of the full one. (d) "Needs both conditions" is tautological but true. The four domain examples check, including D_{K′} ∪ F, now completed as REF67_out U4 asked. |
| Thm 8.1(a)–(d) | **Mathematics CORRECT; conclusion "covers K" is an ERROR as written** (change 1) | See §2(vi). |
| Ex B.1 | **CORRECT** | States are q_s, s ∈ [0,1], with q₀ not an evaluation. The Lyapunov–Lindenstrauss range is ∫(2f−1)h. The support function ∫_V\|λ·h\| > 0 (MC minimum ≈ 0.019 for a test ball) gives a disc of radius c inside R. A₀ ⊆ D_S has \|m(A₀)\| < c/2. Gain βω, with infimum 0. "No coherent model could make it" holds because hull(B) ⊇ D_S ⊇ A₀. |
| Ex B.2 | **CORRECT** | R ⊆ {P_S = 0} with μ(R) = 1. C∪R ≺_ω C at every ω. It shows exactly that μ{P_S = 0} = 0 is needed for protection. See §2(iii). |
| Rem B.3 | **CORRECT** | h ↦ h/e is an isomorphism that preserves signs pointwise. m_ω = e(ω)·m̃_ω. |
| Prop C.1(a)–(c) | **CORRECT** | (a) Both directions check. (b) The relint perturbation k ± td and Rockafellar 11.6 are right. (c) ±h ∈ ∂D_K∖{0} gives W ∪ (−W) ⊆ O. Codim ≤ m. |
| App D (proof of 8.1) | **CORRECT** | Re-derived step by step; see §2(vi). |
| §9.2 "(3) implies coherent admissibility" | **CORRECT under (M2)** | It uses Lemma 6.5. Say "(M2)". |
| §9.3 mutually singular measures | **CORRECT** | Lines d + ℝ𝟙 (d ∈ D₀) are pairwise disjoint (evaluate at ω₀). L ∩ L′ = ∅ because x₀ ∉ D₀ − D₀. D_Q∖L′ is μ-a.e. D_Q but μ′-null, while every coherent model ⊇ D_S has μ′(D_S) > 0. Needs dim E ≥ 2, which is stated. |
| §9.3 reweighting | **CORRECT** | w > 0 a.e. preserves null sets and support. |

## 2. Focus points

### (i) Setting
- **Models as completion-measurable classes.**
  - The setting is consistent: every notion is class-invariant, and the Borel representative exists.
  - With (M2), Lemma 2.3(b) makes every weak-sense or Walley-coherent set a model, and a.e. a D_Q. So "literally models" (WA68 flag 6) is right, but *only under (M2)*.
- **Coherence modulo μ.** The definition is correct and correctly flagged as μ-relative (§2.3, §9.3).
- **Walley-coherence.** The mathematics is right. The framing is not:
  - The abstract's first sentence ("A set of desirable gambles is coherent when it is represented by a closed convex set of probabilities") and the intro's definition ("accepts h exactly when every member of Q gives h positive expectation") misdescribe the standard notion.
  - Walley-coherent sets are only sandwiched, D_K ⊆ D ⊆ C_K. Lexicographic sets such as {p·h > 0} ∪ {p·h = 0, q·h > 0} are coherent but not of the form D_Q ∪ {h ≥ 0, h ≠ 0}.
  - An IP referee will flag this immediately. **Repair (change 3):** "up to its boundary, a coherent set of desirable gambles is represented by…; under our null-boundary condition boundaries are invisible, so modulo μ coherent models are exactly the sets D_Q (Lemma 2.3(b))."
- **A nearby point worth one sentence: (M2) does a second job.** Without (M2), Walley coherence and coherence modulo μ diverge. Example (checked by hand):
  - Take E = ℝ², and let μ be the standard Gaussian plus the law of (t, −t) with t ~ Exp(1).
  - D ≔ {h₁+h₂ > 0} ∪ {(t,−t) : t > 0} is Walley-coherent (lexicographic).
  - D = D_Q a.e. would force Q = {(½,½)} from the Gaussian part, but also q′₁ > ½ for all q′ ∈ Q from the charged ray. That is a contradiction.
  - So (M2) is what makes "undominated ⇔ coherent" mean Walley-coherent modulo μ, beyond making the minimax optimum an ordinary set.
- **Identification of distinct credal sets under full support.** Lemma 2.3(a) plus 2.1(e) is correct. It uses (M3) only, not (M2).

### (ii) Full-support headline and what is lost without it
- The headline (Thm 6.8) assumes (M1)–(M3). The sentence "Without (M3), everything holds except the bijection in (a)" is accurate, and so is intro scope item (3).
- I checked that (M3) is used only in:
  - Lemma 2.3(a), which gives the bijection;
  - App C (local-freedom characterisations, and one-sidedness of D_{K′});
  - the §8 contrast ("U itself is dominated", via 2.3(a), under Lebesgue-equivalent μ).
- **What is lost, made concrete (optional addition):**
  - Coverage claims then concern μ-classes. "Covers K" no longer distinguishes K from other credal sets with the same class.
  - In the paper's own example μ = δ_𝟙 + δ_{−𝟙}, there is a single coherent model. Every target is then "covered" by a ranking whose only undominated model is D_S.
  - One sentence after Thm 6.8 would make the loss vivid without weakening the headline.

### (iii) Null-boundary condition and Example B.2
- (M2) is used exactly where it is flagged: Lemmas 2.3(b), 2.4(b)–(d), 2.6, 3.1, 4.3 and 6.5, and Props 6.6–6.7.
- Example B.2 is correct, and its title "The null boundary {P_S = 0} is essential" is accurate. It shows that *that part* of (M2) is needed for protection.
- It does not show that the rest of (M2) is needed for the repair theorem, but the paper does not claim so.
- Recommend adding the Walley-divergence point from (i) as the other half of "why (M2)" (change 3).

### (iv) Non-uniform dominance; mutually singular measures
- Both are **CORRECT**; see the table.
- Ex B.1 correctly uses Prop 6.7 to turn "score gain βω > 0 everywhere, plus no coherent model can make the change" into strict dominance.

### (v) Proposition 6.3
- **CORRECT as stated, with no null-boundary assumption.** Only (M1) is needed, to define m_ω.
- The proposition carries no hypothesis line, which is right. It could say "No assumption beyond (M1) is used."
- The sentence after it ("Property (2) also makes guided changes improve the score, which is consistent, since …") is garbled. Rephrase as: "(1) and (2) are compatible, because a non-null guided change strictly improves the score at its world (Prop 6.2(b))."

### (vi) Veto–Brier example
**Specialisation to s = 0.** This is correct.
- COV Cor contam allows 0 ≤ s < 1. With s = 0, K′ = {p} and U = D_{{p}} = {p·h > 0}.
- p ∈ relint K holds via the affine bijection m ↦ (1−ε)p + εm.
- A_i = {v_i} ⊆ [p, e_i] = conv(K′ ∪ {e_i}).
- K = conv(K′ ∪ ⋃A_i).
- The veto max(0, −v_i·h) matches a_i.

**App D re-derived.**
- Step 1 (sign condition): uses p·h > 0. For ε = 1, v_i = e_i.
- Step 2 (strict guidance, independence):
  - Δa ≤ 0 and Δb < 0 give a strict lexicographic decrease.
  - The lexicographic order is translation-invariant.
- Step 3 (Lyapunov range):
  - μ has no atoms because it has Lebesgue's null sets.
  - ⊴ is a product of total orders, hence a partial order.
  - The dominance and tie characterisations are right.
- Step 4 (Zorn):
  - The finite intersection property holds for cl T_γ.
  - y^∞ ⊴ γ holds in both cases.
  - y^∞ ⊴ z(X₀) follows by transitivity.
  - Minimality excludes dominators.
- Step 5 (separation):
  - If W₀ = ∅, then ∅ strictly dominates X\*.
  - The P-disjointness argument holds.
  - Signs from cl P: β, α ≥ 0 and γ = 0. β ≠ 0, via J(∅) = 0.
- Step 6 (uniqueness): t ↦ g(h + t𝟙) is strictly decreasing at rate ≥ 𝟙·β; Fubini.
- Step 7 (coherence):
  - [−v·h]⁺ = max_{t∈[0,1]}(−t v·h), and the α ≥ 0 sum of maxima is a maximum.
  - Ŵ is compact.
  - K\* ∋ p and v_ω for ω ∈ W₀ ≠ ∅, so the clause "K\* contains p and some v_i" is correct.
- Step 8:
  - a_i(D_K) = 0.
  - A weak dominator lies in N(Ω) = D_K a.e.
  - The Σp_i argument applies.
  - Ties at every world mean equal z.
  - Dominance of incoherent models follows.
- Step 9 (local freedom): via the C.1(b) argument with k = p.

**Does it meet every requirement of the paper's own cover definition?** Requirements (2)–(6) are met. **Requirement (1) is the problem:**
- (1) asks for "acyclicity (as in Proposition 6.2(b))". The acyclicity bullet of 6.2(b) reads "no chain A₀⪯…⪯A_k has A_k≺A₀, **and every cycle consists of models equal a.e.**".
- The veto–Brier ranking has ties between distinct models. By Lyapunov there is T ⊆ S with z(T) = z(S)/2 for any non-null S ⊆ U with z(S) ≠ 0. Then T and S∖T are distinct, tied at every world, and form a 2-cycle.
- So under the literal reference, Thm 8.1's "Hence … covers K" is false.
- Requirement (3) ("closure under ties") presupposes that ties between distinct models are allowed, and COV's (TC) is only the first clause. The intended requirement is therefore clearly the chain clause alone.
- **Repair (change 1):**
  - state acyclicity explicitly in (1) as the chain clause;
  - in Prop 6.2(b), list "every cycle consists of a.e.-equal models" as a consequence of "no ties" for this ranking, not as part of acyclicity;
  - add to Thm 8.1(a) "hence acyclic (by transitivity)", because (1) also requires it and Thm 8.1(a) currently lists only strict guidance and independence.

**Is the contrast accurate?** The three bullets in §8 are accurate:
- the veto–Brier world orders are total preorders;
- "U = D_{p} is dominated", via (b) and 2.3(a) with ε > 0;
- precise targets cannot be covered on one-sided domains for n ≥ 2, since K_⊥ ≠ 0;
- dependence on the target is acknowledged.

The framing sentences overgeneralise (change 4):
- Intro: "this weaker ordering structure is not needed to cover genuinely imprecise targets on restricted domains".
- §8 opening: "a weaker ordering structure is not necessary to cover genuinely imprecise targets".

COV itself shows many imprecise targets are *not* veto–Brier targets (e.g. contaminations centred on ∂Δ, boxes, pari-mutuel models). The example establishes "not needed for *some* genuinely imprecise targets (interior ε-contaminations) on a one-sided domain". The abstract's "can cover" is fine.

**Recommended addition: a same-domain comparison.**
- On the same U = D_{{p}}, the universal ranking also covers this K, by Cor 7.1(d) and Prop C.1(a),(b), because K is full-dimensional with p ∈ relint K.
- It covers every such K at once, whereas each veto–Brier ranking is built for one K.
- This makes the trade-off precise: total preorders against universality.

**No LDG dependence.** App D carries Lyapunov, Zorn and separation in full. "Fubini argument of Lemma 2.2" and "argument in the proof of Prop C.1(b)" are both present in the manuscript.

## 3. Hypotheses versus proofs
- Every stated hypothesis matches its proof. Unneeded assumptions are absent: Props 6.2–6.3 and Lemmas 4.1–4.2 carry none. The earlier hygiene gaps (REF67_out C1, C8, C15, C18; RF67b rows 13–14, 16, 19–20) are all repaired in the manuscript.
- **Theorem 8.1 states no hypotheses.** It relies on the section's setup: n ≥ 2, μ Lebesgue-equivalent with finite first moment, p ∈ relint Δ, 0 < ε ≤ 1. Put them in the statement (change 8).
- §9.2: "Property (3) implies [coherent admissibility]" uses Lemma 6.5, hence (M2). Say so.
- §9.3 "Separability is used for…" omits two uses:
  - Bochner integrability of the identity (strong measurability);
  - the existence of full-support measures in Lemma 2.2.
- **No dependence on deleted material or on LDG.** Every `\ref` resolves to a result present in this manuscript; I grepped for LDG, round, draft, outline and earlier, with no hits. The source labels named in WA68 are not cited.

## 4. The author's addition (BRIEF68 points 1–5)
1. **Rule stated plainly.** Done in three places: intro ¶"The ranking", Def 6.1 and the sentence after it, and the abstract. "Could make" is explained through added and removed gambles (intro, Def 2.5, after Def 6.1). ✓
2. **Definition versus consequences.**
   - Prop 6.2 proves guidance (strict), independence, finite-chain consistency (called "acyclicity"; see change 1 for the wording), disjoint additivity and no ties.
   - Ex 6.4 shows the ranking is incomplete and not transitive.
   - "These properties do not characterise it" is shown by the guidance-only relation, which I checked has every property of 6.2. ✓
   - Minor: abstract and intro say "is incomplete and intransitive" without qualification. For degenerate μ (e.g. δ_𝟙 + δ_{−𝟙}, with four models) this need not hold. Write "in general" or "for instance with Lebesgue-equivalent μ on ℝ²".
3. **Exact characterisation.** Prop 6.3 is correct and short, and its proof is elementary. See §2(v) for the garbled follow-up sentence. ✓
4. **Repair theorem central.** Yes:
   - the intro leads with it;
   - §9.1 ¶2 says explicitly that maximality does not replace it;
   - the "What this achieves" paragraph says the rule protects coherent models but does not build in dominance of incoherent ones. ✓
5. **Stronger assumption recorded, not investigated.** §9.2 is accurate: (3) is per-comparison, per-world; coherent admissibility is global; (3) implies it (under (M2)); independent justification is open; whether it can be weakened is future work, also listed in §9.4.
   - "(3) is stronger" is asserted with only a heuristic reason.
   - A one-line witness exists if wanted: add to ⪯_ω the non-guided, score-improving comparisons, available to a coherent model, between two *incoherent* models. The result keeps (1), (2) and coherent admissibility but violates (3).
   - Optional; the brief says not to investigate.

**Scope qualifications in statements and introduction.**
- In the intro: all four (separable with order unit; null-set identification; full support and how to drop it; some uniform repair, but not every dominance uniform). ✓
- In the statements: the null-set identification appears (Thm 6.8(a), "a.e."), and full support and how to drop it appear (Thm 6.8, last sentence).
- *Not* in the statements:
  - the gamble-space standing assumption;
  - the uniformity caveat, which sits in the paragraph after Thm 6.8.
- The audit said "in the statements and introduction". Recommend a one-clause recall in Thm 6.8 (and Thm 5.1): "E as in §2.1 (separable, closed, containing 𝟙); models up to μ-null sets". Add to 6.8(b): "(dominance between arbitrary models need not be uniform: Example B.1)" (change 9).
- Intro scope item (1) ends "…is not separable, and **it is not covered**". This clashes with the technical sense of "covers K", and could be read as an impossibility claim, which is not proved. Write "and our results do not apply to it" (change 7).

**Achievement and limitation stated together.**
- They are stated together in the abstract, in the intro ¶"What this achieves, and what it does not", and in §9.1. The balance is good: "The repair theorem is substantial; the motivation … remains a separate philosophical question."
- One tension remains. Abstract sentence 2, "We show that coherence can be characterised by accuracy dominance", reads as the stronger claim that the abstract later disclaims.
- Suggest: "We show that coherence can be characterised exactly by dominance in a ranking built from an accuracy score" (change 6).
- Also: "the requirements usually placed on accuracy rankings" (intro and §6.3) overclaims. Closure under ties, local freedom and incoherent-model dominance are the authors' requirements, not standard ones. Write "the requirements we adopt", and cite truth-directedness and additivity sources for (1) (change 5).

## 5. Conventions and clarity
- **Jargon.**
  - One survivor: "the classical **route** from admissibility to coherence" (§8, l.1075). Change it to "argument".
  - (M1)–(M3) are labels, but they come with descriptive names; acceptable per the brief.
  - No other forbidden labels.
- **Names on theorem-like environments.**
  - No optional-argument names are used.
  - Rem 4.4, Ex B.1, Ex B.2 and Rem B.3 open with italic run-in titles ("Dominance need not be uniform.", "Replacing 𝟙.", …), which function as names.
  - For strict compliance, fold them into the first sentence. Optional.
- **`\coloneqq`** is used throughout, with no bare `:=`. "Models" and the dominance nomenclature are standard. ✓
- **Inessential material.**
  - The sentence after Prop 6.3 (rephrase or cut).
  - "which is closed under coherent hulls" in §8 is unused, unless it is used for the same-domain comparison recommended in §2(vi).
- **Missing material.**
  - (a) **Related literature on imprecise accuracy.** These are the papers a referee will ask about:
    - Seidenfeld, Schervish and Kadane, "Forecasting with imprecise probabilities", IJAR 53 (2012): no strictly proper real-valued score for IP;
    - Mayo-Wilson and Wheeler (2016);
    - Schoenfield (2017);
    - Konek, "Epistemic conservativity and imprecise credence", PPR (2019);
    - Berger and Das (2020);
    - Pettigrew, *Accuracy and the Laws of Credence* (2016).
  - The paper should say in two or three sentences how it sidesteps the SSK impossibility: it scores acceptance sets, not credal sets, with an incomplete, non-transitive, world-wise ranking. This positioning is part of stating the achievement and limitation accurately.
  - (b) Optionally, Walley 1991 on strict desirability (I have not checked the section number), since the D_Q are exactly the open/strict coherent sets.
- **Local wording.**
  - The §3 discussion says "With finitely many worlds, Lyapunov's theorem makes the set of score vectors … convex and compact". This needs non-atomic μ, and Remark 5.2(c) stresses that atoms are allowed. Add "for non-atomic μ".
  - §6.3 "the models on U are the models contained in U": write "contained in U a.e." for consistency.
- **Citations.**
  - All checked entries are correct in substance: de Finetti 1974; Joyce 1998, 65:575–603; Predd et al. 2009, 55:4786–4792; Sion 1958, 8:171–176; Lyapunov 1940, 4:465–478; Lindenstrauss 1966, 15:971–972; Diestel–Uhl 1977; Rockafellar Thms 11.3 and 11.6, used correctly; Walley 1991.
  - Quaeghebeur, ch. 1, pp. 1–27 in Augustin et al. (2014) matches my recollection.
  - Aliprantis–Border Thm 6.30 (weak-\* metrizability of the dual ball of a separable space) matches my recollection, but I could not confirm the number online. **Lead: verify against the 3rd edition.**
- **Figure.** Coordinates check: p = (2.5, 1.732) and ε = 0.45 give the v_i exactly. The figure illustrates a retained result. ✓
- **Author block:** Konek and Campbell-Moore, as briefed. The lead is to flag this to the author.

## 6. Required changes, ranked

1. **(ERROR in a statement, §6.3 req. (1) / Prop 6.2(b) / Thm 8.1.)**
   - Define acyclicity in requirement (1) explicitly as "no chain A₀⪯…⪯A_k with A_k≺A₀".
   - Move "every cycle consists of a.e.-equal models" out of the acyclicity bullet of Prop 6.2(b), as a consequence of "no ties".
   - Add "hence acyclic" to Thm 8.1(a).
   - Without this, Thm 8.1's "covers K" is false, because veto–Brier has 2-cycles of distinct tied models (Lyapunov halving).
2. **(Overclaim, §9.1.)** "The same holds on every domain closed under coherent hulls" includes "covers every credal set", which is false on restricted domains. Replace with: "…except that coverage is then exactly of the K with D_K ⊆ U a.e. and local freedom (Cor 7.1(d))".
3. **(IP framing of coherence: abstract sentence 1, intro ¶1, and §2.3.)**
   - State that coherent sets of desirable gambles are represented by credal sets *up to their boundary* (D_K ⊆ D ⊆ C_K), and that under (M2) boundaries are null, so the D_Q are the coherent models modulo μ (Lemma 2.3(b)).
   - Add one sentence (with the ℝ² ray example of §2(i)) that without (M2) the notions diverge, which is (M2)'s second role.
4. **(Contrast overgeneralised, intro ¶"A structured contrast" and §8 ¶1.)**
   - "is not needed to cover genuinely imprecise targets" → "is not needed for some genuinely imprecise targets (interior ε-contaminations) on a one-sided domain".
   - Recommended: add the same-domain comparison, in which the universal ranking on U = D_{p} covers this K and all full-dimensional K with p ∈ relint K at once (Cor 7.1(d), Prop C.1).
5. **(Scholarship.)**
   - Add a short related-work passage on imprecise accuracy (SSK 2012 and the others listed in §5), saying how the result sidesteps the SSK impossibility.
   - Replace "requirements usually placed on accuracy rankings" (intro and §6.3) with "the requirements we adopt", citing standard sources for truth-directedness (strict guidance) and additivity (independence).
6. **(Achievement and limitation.)**
   - Abstract sentence 2 → "can be characterised exactly by dominance in a ranking built from an accuracy score".
   - "The ranking is incomplete and intransitive" → "in general".
7. **Intro scope (1):** "and it is not covered" → "and our results do not apply to it". This avoids a clash with the technical "covers" and an unproved impossibility.
8. **Thm 8.1:** state its hypotheses (n ≥ 2; μ Lebesgue-equivalent with finite first moment; p ∈ relint Δ; 0 < ε ≤ 1) in the theorem.
9. **Statements carry the scope (audit).**
   - Thm 6.8 (and Thm 5.1) should recall E (separable, closed, containing 𝟙) and identification modulo μ.
   - Thm 6.8(b) should add that dominance between arbitrary models need not be uniform (Ex B.1).
10. **§9.2:** "Property (3) implies it" → "Under (M2), property (3) implies it". Optionally give the one-line witness that (3) is strictly stronger (§4, point 5).
11. **Rem 4.4, second part:** replace or supplement the coherent X with the incoherent instance X′ = D_Δ ∪ (B ∩ {‖h‖_∞ > 1}).
    - REF67_out U2 recommended this, and it was not adopted.
    - I re-checked it: Q_{B′} = {(½,½)} (MC masses 0.0064 at t = 0.45 and 0.55); (½,½)·m(B′) ≈ 0.064 > 0. X′ is incoherent because D_Q ⊇ B′ a.e. forces Q ⊆ {(½,½)}.
12. **Minor wording.**
    - Rephrase the sentence after Prop 6.3 (§2(v)).
    - Lyapunov "for non-atomic μ" (§3 discussion).
    - "route" → "argument" (§8).
    - "contained in U a.e." (§6.3).
    - §9.3: add Bochner measurability and Lemma 2.2 to the uses of separability.
    - Optionally drop the italic run-in titles in Rem 4.4, Ex B.1, Ex B.2 and Rem B.3.
13. **Optional:** one sentence after Thm 6.8 making concrete what is lost without (M3), e.g. with μ = δ_𝟙 + δ_{−𝟙} there is one coherent model, and "covers K" no longer distinguishes targets.
14. **Lead:** verify Aliprantis–Border Thm 6.30 and the Quaeghebeur page range against the printed editions.

**Recommendation.** Accept after changes 1–9; changes 10–14 are minor. The mathematics is ready. The required changes are about statements, framing and scholarship, not proofs.

---

# Second round: check of Revision 2 (26 Oct 2026)

I re-read the revised `.tex` (26 pp.) and `WA68_changes.md`, Revision 2. The compile is clean: the log has no warnings, no undefined references and no overfull or underfull boxes. This round I also read RA68a's §6, as the lead requested, but no other part of `RA68a_notes.md`.

## A. My required changes 1–9

| # | Status | Check |
|---|---|---|
| 1 | **DONE, correct** | Requirement (1) now defines acyclicity as the chain clause. Prop 6.2(b) has a separate bullet deriving "every cycle is a.e.-equal" from "no ties". Thm 8.1(a) reads "complete and transitive, hence acyclic". The new §8 tie sentence has a small gap (see B5). |
| 2 | **DONE, correct** | §9.1 now says that on hull-closed domains the ranking covers exactly the K with D_K ⊆ U a.e. and local freedom (Cor 7.1(d)). |
| 3 | **DONE, correct** | Abstract, intro ¶1 and §2.3 now say "represented up to its boundary". Lemma 2.3 is split: (b) is the sandwich without (M2), plus a.e. equality under (M2); (c) is the Walley form. In App A, Steps 1–4 indeed use no (M2): I re-checked Hahn–Banach on int D and the bipolar step. The second role of (M2) is in §2.3 and §9.3; see B2. |
| 4 | **DONE; new sentence has an ERROR** | "Some genuinely imprecise targets" appears in the abstract, intro and §8. The same-domain sentence is mis-stated; see B3. |
| 5 | **DONE** | Related-work paragraph added (see B1). "The requirements we adopt" now cites Joyce for truth-directedness and Pettigrew for additivity; both analogies are fair. |
| 6 | **DONE** | Abstract: "characterised exactly by dominance in a ranking built from an accuracy score", and "in general incomplete and intransitive". |
| 7 | **DONE** | "Our results do not apply to it". |
| 8 | **DONE** | Thm 8.1 now carries n ≥ 2, Lebesgue-equivalent μ with finite first moment, p ∈ relint Δ, 0 < ε ≤ 1, and identification modulo μ. |
| 9 | **DONE** | Thms 5.1, 6.8 and 8.1 carry E (separable, closed, containing 𝟙 or an order unit) and identification modulo μ. Thm 6.8(b) has the uniformity caveat. |

Also made:
- my 10–13 (including "Under (M2)" in §9.2, the incoherent Rem 4.4, and the (M3) loss sentence);
- the new Thm 6.8(c) ("every model is weakly dominated by an undominated coherent model"). It is **correct**: a coherent model weakly dominates itself, and an incoherent one is dominated by (b). Cor 7.1(c) is renumbered consistently.

## A′. RA68a's required changes 1–9

| # | Status |
|---|---|
| 1 | **DONE**: "in general incomplete and intransitive" appears in the abstract, intro ×2 and §8 ×2. Ex 6.4 now opens "need not be transitive or complete". |
| 2 | **DONE**: the Lyapunov sentence now says "with finitely many worlds and a non-atomic μ … in general, and in infinite dimensions, it need not be". |
| 3 | **DONE** (same as my 9). |
| 4 | **DONE**: §9.2 "Under (M2)…", citing Lemma 6.5. |
| 5 | **DONE**: part 2 uses B′ = B ∩ {‖h‖ > 1}; part 1 says "image under exchange of coordinates", with exchange-invariance of the Gaussian stated. |
| 6 | **DONE** (same as my 1). |
| 7 | **DONE**: "route" and "admissible measures" are gone (grep finds neither). |
| 8 | **DONE**: Ex B.1, Ex B.2 and Rem B.3 now open with plain sentences. Rem 4.4 and Thm 5.1 have plain or parenthetical labels. |
| 9 | **DONE**: "Whether some coherent model could make the change does not depend on ω". |

RA68a's 10 is also in: the Prop 6.3 sharpening, which is **correct**. The containment proof never invokes (1), so ⪯_ω is the largest relation with (2) and (3), and it has (1) by clause (i).

## B. New text not previously refereed

**B1. Related-work paragraph (§1).**
- **SSK summary: accurate in substance, but it hides the key hypothesis.** SSK's impossibility result (Prop. 5 in the CMU preprint) is "There is no real-valued strictly proper IP **continuous** scoring rule". Propriety there is relative to a decision rule that reduces to expected-utility maximisation for precise credences and satisfies a weak admissibility principle.
- SSK also give a positive result: strictly proper **lexicographic** IP scores exist for Γ-maximin and for E-admissibility followed by Γ-maximin.
- "Under natural conditions" is defensible, but continuity is the substantive hypothesis, and the lexicographic escape bears directly on §8, where the veto–Brier ranking is lexicographic.
- **Recommended rewrite:** "…showed that no continuous real-valued scoring rule for imprecise forecasts is strictly proper (relative to decision rules that reduce to expected-utility maximisation for precise credences), although lexicographic strictly proper scores exist."
- The rest of the paragraph is accurate: this paper scores sets of gambles, uses per-world real scores and a non-total ranking, and singles out coherence by undominatedness, not expected-score optimality.

**B2. The (M2) example (§2.3).** **CORRECT.**
- D = {h₁+h₂ > 0} ∪ {(t,−t) : t > 0} is a convex cone without 0 and contains every nonzero h ≥ 0, so it is Walley-coherent.
- If D = D_Q μ-a.e., then D = D_Q a.e. for the Gaussian part as well. Lemma 2.3(a) applied to that full-support part gives Q = {(½,½)}, so D_Q misses the ray, which has μ-measure 1.
- μ{P_Q = 0} ≥ 1 is right.
- Wording nit: "Applying (a) to the Gaussian part" means applying it to the measure γ, not to μ. Say "applying (a) with μ replaced by its Gaussian part γ, which satisfies (M3)".

**B3. Same-domain sentence (§8, "Reach").** **ERROR in wording; the mathematics is right once restated.**
- It says the ranking of Def 6.1 on U covers "every credal set with nonempty relative interior containing p in that interior". Every nonempty convex set has nonempty relative interior *relative to its own affine hull*.
- Read that way, the sentence includes K = {p}, which is not covered on U (Prop C.1(c), K_⊥ ≠ 0 for n ≥ 2), and every lower-dimensional K through p.
- Prop C.1(b) requires a nonempty interior **relative to the affine hull of Δ**, that is, a full-dimensional K.
- **Fix:** "every credal set K with nonempty interior relative to aff Δ and p ∈ relint K". The same slip is in WA68's change item 7.
- With that fix the claim is correct. Lemma 2.2 gives (M1)–(M3). Cor 7.1(d) and Prop C.1(a),(b) with K′ = {p} then give coverage, and this contamination K qualifies via the affine bijection.

**B4. Remark 4.4, incoherence proof.** **CORRECT.**
- Q_B = {(½,½)}: the open witnesses (−a, a+s) have ‖·‖ > 1 for large a, and MC in round 1 confirms this. N = D_Δ ⊆ hull(B).
- Incoherence: X = D_Q a.e. gives B ⊆ D_Q a.e., so Q ⊆ Q_B. Then D_Q = {h₁+h₂ > 0}, which contains the nonempty open set {h₁ < 0 < h₁+h₂, ‖h‖ < 1}, e.g. (−0.1, 0.5). X misses that set, since N needs h₁ > 0 and B needs ‖h‖ > 1, and the set has positive Gaussian measure.
- The conclusion follows because (½,½)·m(B) > 0.
- Part 1's exchange description is right.

**B5. Acyclicity redefinition and consequences.** **CORRECT, with one small gap in §8.**
- Prop 6.2(b): the chain clause follows from the score inequalities. The cycle bullet follows from no ties.
- Requirement (1) uses the chain clause only. Thm 6.8(e) is unaffected. Thm 8.1(a) "hence acyclic" holds by transitivity.
- With this definition, Thm 8.1's "covers K" is now **true**.
- The §8 sentence "a non-null Y ⊆ U has a subset T with z(T) = z(Y)/2 … then T and Y∖T are tied at every world" does not say why T and Y∖T are *distinct* models. They are, since both are non-null:
  - Σ_i p_i b_i(Y) = −∫_Y p·h dμ < 0, so z(Y) ≠ 0;
  - hence z(T) = z(Y∖T) = z(Y)/2 ≠ 0.
  - Add that half-sentence.

**B6. Other new sentences.**
- The (M3)-loss sentence after Thm 6.8 is correct (δ_𝟙 + δ_{−𝟙} gives one coherent model).
- §9.1 "Under (M2), properties (2) and (3) protect coherent models" is correct; only (3) plus Lemma 6.5 is needed.
- Intro ¶1's representation sentence is correct: D ⊆ C_K means no gamble with some q(h) < 0.

## C. Bibliography (web-verified)

| Reference as cited | Verdict |
|---|---|
| Seidenfeld, Schervish, Kadane, "Forecasting with imprecise probabilities", IJAR 53:1248–1261, 2012 | **Confirmed.** Springer reference list in Phil. Stud. 10.1007/s11098-020-01491-2; CMU preprint. Issue 8 is not printed in the manuscript, which is fine. |
| Mayo-Wilson and Wheeler, "Scoring imprecise credences: a mildly immodest proposal", PPR 93:55–78, 2016 | **Confirmed**: author's CV gives vol. 93, issue 1, pp. 55–78; the UW page gives the full subtitle. |
| Schoenfield, "The accuracy and rationality of imprecise credences", Noûs 51:667–685, 2017 | **Confirmed**: PhilArchive gives 51(4):667–685, with an online-first date of 2015; the volume year is 2017. |
| Berger and Das, "Accuracy and credal imprecision", Noûs 54:666–703, 2020 | **Confirmed**: PhilArchive gives 54(3):666–703; Wiley lists 2020, DOI 10.1111/nous.12274. |
| Pettigrew, *Accuracy and the Laws of Credence*, OUP, 2016 | **Confirmed** (OUP Academic). |
| **Konek, "Epistemic conservativity and imprecise credence", PPR, 2019** | **Cannot confirm the year, and the year "2019" is suspect.** The paper exists under this title in PPR. Academia.edu lists it as PPR 2015, and papers of 2019–2020 (Carr; Phil. Stud. 2020) cite it as "forthcoming". I found no volume or pages. **The author should supply the actual year, volume and pages, or cite it as "forthcoming"/early view with its DOI.** Do not print "2019" unverified. |
| Companion: Konek and Campbell-Moore, "Coherence, dominance, and generalized loss", manuscript 2026 | Title words match WL68's `\title{Coherence, Dominance, and Generalized Loss}`; only the case differs, and sentence case is consistent with this bibliography's style. The pointer's content matches LDG §§1, 7, 9. There is no circularity: the application says "proofs … self-contained", and LDG cites the application only for the existence result. |
| Aliprantis–Border Thm 6.30 | Still flagged in a LaTeX comment; I still could not confirm the number online. |

## D. Remaining required changes (all local)

1. **(ERROR, B3.)** In the same-domain sentence, write "nonempty interior relative to aff Δ" (full-dimensional) instead of "nonempty relative interior". As written, the sentence includes {p}, which Prop C.1(c) excludes.
2. **(Citation, C.)** Konek's PPR entry: the year "2019" cannot be confirmed. The author should supply the year, volume and pages, or "forthcoming" with the DOI.
3. **(Accuracy, B1.)** Name continuity in the SSK summary, and mention their lexicographic strictly proper scores.
4. **(Gap, B5.)** §8 tie sentence: add that T and Y∖T are non-null because Σp_i b_i(Y) < 0, hence distinct.
5. **(Wording, B2.)** "Applying (a) with μ replaced by its Gaussian part".

**Verdict:** accept after D1–D5. All the mathematics is correct, and every first-round required change from RA68a and from me is made correctly.
