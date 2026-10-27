# RA68a: referee report on "Coherence and accuracy for sets of desirable gambles"

26 October 2026. Referee RA68a (independent; I did not read RA68b_notes.md).

**What I reviewed.** The manuscript `Coherence and accuracy for sets of desirable gambles.tex` and its PDF (24 pp.), together with `WA68_changes.md`.

**Method.** I re-derived every proof from the manuscript's own text, not from the source notes. The context files were used for two purposes only:
- to check that nothing was lost in compression (REF67_out, RF67a, RF67b, COV Cor contam / Thm cover, VB_dominance_note);
- to check the author's addition and the audit decisions (BRIEF68, AUDIT_r68_message).

**Supporting files.**
- Script: `ra68a_py/checks.py`. Run `python3 -I checks.py` from that folder; it writes `checks.out`.
- Recompile: `ra68a_py/build/` (pdflatex, 3 passes).
- The numerics illustrate; the verdicts rest on the proofs.

Labels: CORRECT / GAP (wording or hypothesis, repair given) / ERROR (a false claim, repair given).

## 0. Verdict at the top

**The mathematics is correct.**
- Every numbered result is proved under its stated hypotheses, and every load-bearing step holds.
- No proof uses deleted material, LDG, or any unrefereed source item.
- The completion-measurable definition of models breaks nothing.
- The new elementary items are all correct: Prop 6.3, the guidance-only sentence, Remark 4.4 part 1, Example 6.4 in ℝ², the §9.2 implication, and the §9.3 disjoint lines.
- The compile is clean: no warnings, no undefined references, no overfull or underfull boxes; 24 pages.

**One false claim in prose (ERROR, minor).** The manuscript says, unconditionally, that the ranking "is incomplete and intransitive". This appears in the abstract, the introduction (twice) and §8 (twice).
- With one world (E = ℝ, which the standing hypotheses allow), the ranking is **transitive**.
  - Proof: if X ⪯ Y ⪯ Z with X ≠ Z a.e., then m(X) > m(Z).
  - A change available to the only coherent model (0,∞) removes only positive gambles and adds only non-positive ones a.e.
  - Such a change cannot raise the score, so the change from Z to X is guided or accepted under clause (ii).
  - Enumeration in `checks.out` confirms this: 0 transitivity violations, but 64 incomparable pairs.
- Example 6.4 proves the claim only for its instance.
- **Repair:** write "in general incomplete and intransitive", or "need not be transitive or complete (Example 6.4)". This is exactly the brief's wording: "generally incomplete and not transitive".

**One inaccurate explanatory sentence (minor).** The minimax explanation after Lemma 3.1 says: "With finitely many worlds, Lyapunov's theorem makes the set of score vectors of ordinary acceptance sets convex and compact."
- This needs μ to be non-atomic.
- (M2) allows atoms at gambles with inf h > 0 or sup h < 0. The paper's own example μ = δ_𝟙 + δ_{−𝟙} (after Lemma 2.3) satisfies (M1)–(M2) and has a two-point range.
- **Repair:** "With finitely many worlds and a non-atomic μ, Lyapunov's theorem …; in general, and in infinite dimensions, it need not be."
- The argument itself never uses Lyapunov (Remark 5.2(c) is right), so nothing else changes.

**Main presentational gap against the audit.** The audit wants the scope qualifications "in the statements and introduction". The introduction has them. The headline statements (Thm 5.1, Thm 6.8) do not repeat them:
- that Ω is arbitrary but E is separable, closed and contains 𝟙 (or an order unit);
- that models are classes modulo μ-null sets.

Add one sentence to each statement (change 3 below).

## 1. Verdicts per numbered result

| # | Result | Verdict | Notes (re-derivation; hypotheses used) |
|---|---|---|---|
| 2.1(a) | States: norm 1; S convex, weak-* compact, metrizable | CORRECT | The order unit gives \|q(h)\| ≤ ‖h‖. Weak-* closed, so compact by Alaoglu. Metrizable because E is separable (A–B Thm 6.30; see §5). |
| 2.1(b) | P_S = inf_Ω, q ≤ sup | CORRECT | — |
| 2.1(c) | P_Q Lipschitz, concave, translation; ∂D_Q = {P_Q = 0}; D_S ⊆ D_Q; no h with sup ≤ 0; D_{Q₁} ∩ D_{Q₂} = D_{conv} | CORRECT | ∂D_Q: cl D_Q = {P_Q ≥ 0}, via h + t𝟙. conv(Q₁ ∪ Q₂) is compact as a continuous image of Q₁ × Q₂ × [0,1]. |
| 2.1(d) | (1−τ)Q + τS | CORRECT | — |
| 2.1(e) | D_{Q₁} ⊆ D_{Q₂} ⟺ Q₂ ⊆ Q₁ | CORRECT | Stated for credal sets, as REF67_out C1 required. Strict separation in (E\*, w\*) and a shift by c𝟙. |
| 2.1(f) | Countable norming Ω₀ | CORRECT | The second "≤" is in fact "=", which is harmless. |
| 2.2 | Existence of μ; Lebesgue-equivalent μ on ℝⁿ | CORRECT | Φ(g,t) = g + t𝟙 is a linear homeomorphism E₀ × ℝ → E. Fubini over lines h + ℝ𝟙 gives (M2) for all Q at once. Works when E₀ = {0}. |
| 2.3(a) | Under (M3): O ⊆ D_Q a.e. ⟹ O ⊆ D_Q; injectivity of Q ↦ D_Q | CORRECT | — |
| 2.3(b) | Weak-sense coherent D is a model, and D = D_{K_D} a.e.; Walley version | CORRECT | Steps 1–5 checked: HB for the point 0 and the open convex int D; bipolar; int cl D = int D. The terminology matches REF67_out C6 (weak sense versus Walley). |
| 2.4(a)–(d) | Q_B closed and convex; B ⊆ hull(B) a.e.; hull minimality; losing part ⟹ inconsistent | CORRECT | (M2) is flagged exactly where it is used, as REF67_out C8 required. |
| Def 2.5 | Change, "could make", guidance | CORRECT | The result (Z∖B) ∪ A is checked. A ∩ B = ∅ as sets. |
| 2.6 | Test | CORRECT | Two disjuncts, and the explanatory sentence is right. |
| 2.7 | Joining | CORRECT | Indicator identity off the null set. |
| **3.1** | **Minimax lemma** | **CORRECT** | **Compactness:** F_G is weak-* compact in L^∞ = (L¹)\*, since μ is finite. **Continuity:** T is weak-*-to-norm continuous on F_G as a uniform limit of the T_k, with \|f\| ≤ 1. **Minimax:** Sion on S × Z. Both optima are attained: z ↦ inf_Ω(z − x) is 1-Lipschitz on compact Z, and q ↦ max_Z Φ is lsc on compact S. **Inner maximum:** (M2) for {q} makes the maximiser unique a.e. **Saddle step:** Φ(q\*, z\*) is squeezed to v, so every maximiser equals 𝟙_{N\*} for every minimiser q\*. |
| 3.1, explanation | Fractional acceptance and the null boundary | CORRECT except the Lyapunov sentence | See §0. The rest is accurate and clear: the problem is convexified, made compact, and turned back into an ordinary set by q\*; then G ∩ {q\* > 0} = D_{conv(Q′ ∪ {q\*})}. |
| 3.2 | Consistent case: v > 0, N₀ coherent | CORRECT | 𝟙_X ∈ F_G, so v ≥ 0. If v = 0, then X = N\* a.e., which is coherent. |
| 3.3(a)–(c) | Losing part; equivalences | CORRECT | The bracket is ∫_X q⁻. X ∩ {q\* = 0} is null by (M2). Q_L = ∅ because q(m(L)) ≤ −v < 0 ≤ ∫_L q. |
| 4.1 | Contraction | CORRECT | T′ⁿ(q′) − q = (c/(1+c))ⁿ(q′ − q) in norm. The case c = 0 is trivial. No (M2) needed. |
| **4.2** | **Trimming** | **CORRECT** | Writing c = (1−τ)/τ: on X ∩ N, (1−τ)P + τP_S > 0 gives q ≥ P_S > −cP. On X∖N a.e., q ≥ 0 ≥ −cP, using P ≥ 0 a.e. on X (Lemma 2.4(b), the half without (M2)). N ⊆ D_{Q_τ} may be read literally or a.e. |
| **4.3** | **Change lemma** | **CORRECT** | Q ⊆ Q_B, so hull(B) ⊆ D_Q, so N ⊆ D_Q a.e. Then A is null and m(N) − m(X) = −m(B), so the hypothesis gives m_ω(B) < 0 at every world. So B is non-null and inconsistent (2.4(d)), contradicting ∅ ≠ Q ⊆ Q_B. N need not be coherent. |
| **4.4** | **Neither hypothesis can be dropped** | **CORRECT; GAP (strength and wording)** | **Part 1 (balls), checked.** m(N) has equal coordinates ∫_W(h₁+h₂) > 0, by swap-invariance of the Gaussian (2.0e−3 in `checks.out`). D_Δ ∩ N = ∅, so D_Δ could make the change. Wording: "W′ its mirror image about (−1,3)" reads as a point reflection; write "its mirror image under exchange of coordinates, the ball about (−1,3)". **Part 2, checked.** Q_B = {(½,½)}, and (½,½)·m(B) > 0 (0.083). But X = N ∪ B = {h₁ + h₂ > 0} **is itself coherent**, so the change is trivially available to X; the text does not say so. Recommend REF67_out U2's incoherent variant B′ = B ∩ {\|h\| > 1}: X′ = D_Δ ∪ B′ is incoherent, Q_{B′} = {(½,½)}, and m(B′) > 0 at both worlds (numerics: (0.066, 0.067); μ(B ∩ {\|h\| ≤ 1}) ≈ 0.098). The "same mechanism" sentence (∅ ≠ Q_B ⊆ Q) is correct and matches REF67_out U3. |
| **5.1** | **Repair theorem** | **CORRECT** | **Consistent case.** N_τ = D_{conv(Q_X ∪ {q\*} ∪ Q_τ)} is coherent. P_{Q_τ} = P − τ(P − P_S) decreases in τ, so N_τ ↑ N₀ as τ ↓ 0, and dominated convergence (M1) bounds the loss by v/2. Then η = v/2, and (1) holds at every state. Lemma 4.2 gives hull(X∖N) = hull(X) ⊇ N₀ ⊇ N, literally; Lemma 4.3 gives (4); Lemma 2.6 gives μ(N∖X) > 0. **Inconsistent case.** It uses region hull(X₊), as REF67_out C18 required. q\* ∈ Q_{X₊} gives G₁ ⊆ {q\* > 0}, and v₁ ≥ v because 𝟙_{X₊} ∈ F_{G₁}. N = D_{conv(Q_{X₊} ∪ {π\*})}. L ⊆ X∖N as sets, since N ⊆ {q\* > 0} and L ⊆ {q\* < 0}; hence Q_{X∖N} ⊆ Q_L = ∅. (4) then follows from 2.4(c). **Location clause:** correct in both cases, and literal. Only (M1)–(M2) are used. |
| 5.2 | Remarks | CORRECT | (b): X₊ null gives G₁ = D_S. (c): "no Lyapunov, non-atomicity or full support" is true. |
| Def 6.1 | The rule | CORRECT; wording | "Note that the second clause is the same at every world" is inaccurate, since the score part of clause (ii) depends on ω. Write: "whether a coherent model could make the change does not depend on ω". |
| 6.2(a)–(c) | Reflexivity, independence, no ties, acyclicity, strict guidance, disjoint additivity | CORRECT | (b) uses only the strict inequalities in "guided"; no (M2). (c): if a coherent model could make the union, then by Lemma 2.7 it could make the clause-(ii) part, a contradiction; the other part has gain ≥ 0. |
| — | "Guidance-only relation has every property of Prop 6.2" | CORRECT | Null changes are guided; independence is clear; (b) is as in 6.2(b); a union of two guided changes is guided. It also satisfies (1)–(3) of Prop 6.3. So the sentence correctly shows that 6.2 and (1)–(3) do not characterise ⪯. |
| **6.3** | **Maximality** | **CORRECT** | Checked both directions; the lead's check is right. ⪯ has (1) by (i), (2) by 6.2(b), and (3) because (ii) excludes available changes. For containment, take R with the properties and X R Y. If X = Y a.e., the change is null and so guided. Otherwise (2) gives strict gain; if the change is available, (3) makes it guided; if not, clause (ii) applies. **Sharpening (optional):** the containment uses only (2) and (3). So ⪯_ω is the largest relation satisfying (2) and (3), and (1) is automatic. One sentence after the proof would make plain that guidance acceptance is not an extra constraint. The largest relation exists because (2) and (3) are pairwise conditions, closed under unions. |
| **6.4** | **Not transitive, not complete (ℝ²)** | **CORRECT** | Checked exactly. The balls are disjoint and inside C. a′ − (3/5)b′ > (0.04, 1.04), so P_{Q_B} > 0 on A, so A ⊆ hull(B) and, by Lemma 2.6, no coherent model could make the change. The gain is > 1.075δ (a Gaussian instance gives 1.245δ). C → X is not guided (B₊) and is available to C. X → C is not guided (B₋) and has gain m₁(B) < 0. Lemma 2.6 is applied with B consistent, as WA68 flags; the move to ℝ² is sound. |
| 6.5 | Guided at every world | CORRECT | Uses Ω₀ and (M2) for S and for {δ_ω}. No condition on μ{sup h = 0} (matches RF67a E3, RF67b row 14). |
| 6.6 | Protection | CORRECT | — |
| 6.7 | Weak = dominance = strict ⟺ (iv) | CORRECT | The direct (i)⇒(iv) is fine. (iii)⇒(ii)⇒(i) is listed. |
| **6.8** | **Main theorem** | **CORRECT; GAP (statement)** | (a) bijection via 2.3(a)(M3) and 2.1(e). (b) via 5.1 + 6.7 + 6.6; uniform because η > 0. (c) 6.6 + 6.2(b). (d) requirement (3) because distinct models are never tied; requirement (6) because the domain is E. **Without (M3):** correct. Only the injectivity of Q ↦ D_Q uses (M3); surjectivity onto the undominated models remains. **Statement gap:** add the standing hypotheses on E and "models modulo μ-null sets", per the audit (change 3). |
| — | "Finite worlds: strict = uniform; infinite: not" | CORRECT | Cites Ex B.1. |
| **7.1** | **Restricted-domain corollary** | **CORRECT** | (a) hull(B) ∩ U is a coherent model on U that could make the change. (b) X₊ ⊆ X ⊆ U is consistent, so N ⊆ hull(X₊) ⊆ U a.e.; X∖(N ∩ U) = X∖N. (c) The proofs of 6.2–6.7 are domain-free, and 6.6 on U uses C itself. (d) The "only if" holds by definition, so it is a trivial but true remark. Only (M1)–(M2) are needed, as stated. |
| — | Examples of hull-closed domains | CORRECT | The D_{K′} ∪ F proof is complete (REF67_out U4 repaired). |
| **8.1** | **Veto–Brier contamination** | **CORRECT; minor GAP** | See §1.1. (a) lists strict guidance and independence, but covering requirement (1) also needs acyclicity. It is immediate from transitivity; add three words. |
| B.1 | Dominance need not be uniform | CORRECT | Lyapunov–Lindenstrauss range ⇒ R ⊇ ball(c). A₀ ⊆ D_S with \|m(A₀)\| < c/2, and β < c/2. The gain is βω, positive at every world with infimum 0. The test is applied with A₀ ⊆ D_S ⊆ hull. c > 0 numerically. |
| B.2 | μ{P_S = 0} = 0 is essential | CORRECT; nit | The ray R has μ(R) = 1 and lies in {P_S = 0}. C = D_Q is disjoint from R. Adding R is guided at every world, so C ∪ R strictly dominates C. Nit: β is reused (a constant in B.1, an exponential variable here). |
| B.3 | Replacing 𝟙 | CORRECT | Margins at states are preserved exactly; at worlds they are scaled by e(ω) ≥ inf e. |
| C.1(a)–(c) | One-sided domains | CORRECT | (a) via 7.1(d), 2.3(a) and 2.1(e). (b) via the supporting hyperplane, Rockafellar Thm 11.6 (correct citation). (c) K_⊥ ∋ ±h gives balls W and −W inside a.e. The finite-codimension argument is right. One-sidedness of D_{K′}: D ∩ (−D) = ∅ by superadditivity. |
| §9.2 | "(3) ⟹ coherent admissibility" | CORRECT; GAP (hypothesis) | The argument uses Lemma 6.5, hence (M2); say so ("under (M2)"). It needs no tie convention: if Y = C as classes, Y R_ω C for every ω already gives C R_ω C, so there is no strict step. "(3) is stronger": correct. One could add a witness: put into ⪯ one extra non-guided pair between incoherent models whose change is available to a coherent model and raises the score. Coherent models stay undominated, but (3) fails. |
| §9.3 | Mutually singular measures (glue) | CORRECT | L ∩ L′ = ∅: evaluate at ω₀ to get t = s, so x₀ ∈ D₀ − D₀. D_S is non-null for μ′ by (M3). Nit: "Admissible measures" is undefined here; write "measures satisfying (M1)–(M3)". |
| §9.3 | Reweighting | CORRECT | — |

### 1.1 Theorem 8.1 / Appendix D, step by step (s = 0, domain {p·h > 0})

- **Setting.** U = D_{{p}} is closed under coherent hulls and one-sided under (M3). The figure's coordinates are consistent: ε = 0.45, and v_i lies on segment p e_i.
- **Step 1.** v_i·h = (1−ε)p·h + εh_i ≥ 0 when h ∈ U and h_i ≥ 0. Correct, including ε = 1.
- **Step 2.** On X∖Y, φ_i = 0 a.e., so Δa ≤ 0 and Δb < 0. Strict guidance follows, and so does independence (lex is translation-invariant). Correct. Acyclicity is not stated; add it (see the table).
- **Step 3 (Lyapunov).** ψ is integrable (\|φ_i\|, \|h_i\| ≤ \|h\|_∞, (M1)), and μ is non-atomic because it has Lebesgue's null sets. So Z is compact and convex. The completion and Borel ranges coincide. Dominance is a function of z: ⊴ is a product of lex orders, and z(Y) ≠ z(X) means strict at some i. Correct.
- **Step 4 (Zorn).** Correct.
  - Finite subfamilies of {T_γ} share the least index, so the family has the finite intersection property in compact Z.
  - The per-coordinate argument (a_i attained or not) gives y^∞ ⊴ γ.
  - Transitivity of ⊴ puts y^∞ in D.
  - Zorn for partial orders gives a minimal y\*, and minimality excludes dominators.
- **Step 5 (separation).** Correct.
  - W₀ ≠ ∅, because ∅ would otherwise strictly dominate.
  - pr(Z′ − y\*) ∩ P = ∅. Only *some* model realising y is needed, not one inside N(W₀).
  - Rockafellar Thm 11.3 (proper separation; ri P = P) is correctly cited, and both sides are 0.
  - Testing on cl P gives β, α ≥ 0 and γ = 0.
  - If β = 0, then J ≥ 0 and J(∅) = 0 force a_ω(X\*) = 0 for some ω ∉ W₀, a contradiction.
- **Step 6 (uniqueness).** Correct.
  - g(h + t𝟙) ≤ g(h) − t 𝟙·β, so g is strictly decreasing along lines; {g = 0} is closed and meets each line at most once.
  - Fubini then makes {g = 0} null.
  - Hence X\* = N(W₀) ∩ {g < 0} a.e.
- **Step 7 (coherence).** Correct.
  - [−v·h]⁺ = max_t(−t v·h) gives g = max_{w∈W}(−w·h). Each w ≥ 0 with 𝟙·w ≥ 𝟙·β > 0, so {g < 0} = D_{Ŵ}.
  - Hyperplanes are null, so N(W₀) = D_{{p} ∪ {v_ω}} a.e.
  - K\* contains p and v_ω for ω ∈ W₀ ≠ ∅.
  - Random check of {g < 0} = D_{Ŵ}: 0 mismatches in 4·10⁵ samples.
- **Step 8.** Correct.
  - a_i(D_K) = 0, and weak dominance forces a_i(Y) = 0, so Y ⊆ N(Ω) = D_K a.e. (p = Σ p_i v_i).
  - Σ p_i Δb_i = ∫_{D_K∖Y} p·h ≤ 0 forces D_K∖Y to be null.
  - Ties: z(Y) = z(X).
  - Incoherent X: a non-dominating weak dominator would be tied at every world (completeness), so X would be undominated and hence coherent.
- **Step 9.** Correct. The affine bijection fixes p, so p ∈ relint K, and the C.1(b) argument gives p·h > 0 on ∂D_K∖{0}.
- **Contrast "U itself is dominated".** Correct: by (b), U = D_{K\*} a.e. would force {p} = K\* ∋ v_i ≠ p, using (M3) via 2.3(a).
- **Dependence.** Self-contained: no LDG, no visibility theorem. It matches COV Cor contam with s = 0 (K′ = {p}, A_i = {v_i}) and VB_dominance_note Steps 0–3.

## 2. Models as completion-measurable sets modulo null sets

**Nothing breaks.** Checked point by point:
- **Scores and integrals.** m(X), F_G ⊆ L^∞(μ) and 𝟙_G are class-invariant, and the completion and Borel integrals agree.
- **Lemma 2.3(b).** The weak-sense coherent set D is sandwiched between D_{K_D} and C_{K_D}, which differ by a null set. So D is completion-measurable, and the definition is what makes D a model. This is the reason for the choice, and it is sound.
- **Lemma 2.4(a),(b).** The countable unions of null sets are fine for completion-measurable B.
- **Lyapunov (App D, Ex B.1).** The range over completion-measurable sets equals the Borel range.
- **Statements made "as sets".** Thm 5.1(2) "as sets" and "L ⊆ X∖N as sets" refer to a fixed representative of X. N = D_Q is a fixed open set, and hull is class-invariant, so they are correct. REF67_out C4 asked for "for a fixed minimiser q\*"; Thm 5.1(3) inherits it implicitly from Cor 3.3. Optional: say "for a fixed minimiser".
- **Domains.** "Models on U are the models contained in U" is used with literal representatives, as in Cor 7.1(b) (N ∩ U). Fine. Optional: "contained in U (a.e.; we use the representative inside U)".
- **Relations.** Relations on models are class-invariant (Prop 6.2(a)). Prop 6.3 also works for relations on raw sets.

## 3. Hypotheses versus use; dependencies

- **(M1)–(M2) only.** Lemmas 3.1–4.3, Thm 5.1, Props 6.2–6.7, Thm 6.8(b)–(d) and Cor 7.1 use only (M1)–(M2), as stated.
- **(M3).** It is used in Lemma 2.3(a), Thm 6.8(a) (bijection), App C, and the §8 "U is dominated" remark. §9.3 lists two of these, and the third (§8) is an instance of "telling credal sets apart". Consistent.
- **Separability.** It is used for:
  - metrizability of S;
  - Ω₀ (2.1(f));
  - Bochner integrability of the identity (Pettis), on which the score and the minimax continuity rest;
  - the existence proof of Lemma 2.2.

  §9.3 names only the first two. Add the others (minor).
- **Theorem 8.1** needs Lebesgue-equivalent μ, which is stated, and n ≥ 2, also stated.
- **No dependence** on LDG, deleted results (uniform local freedom, world sets, visibility class, the half-space alternative), or the nonseparable sketch. I grepped for LDG, "loss dominance", selection, Bayes and compact family: none.
- **No circularity.** Thm 5.1's consistent case fixes τ before invoking Lemmas 4.3 and 2.6.
- **WA68 glue items.** All re-checked and correct:
  - ∂D_Q = {P_Q = 0};
  - δ_𝟙 + δ_{−𝟙};
  - Ex 6.4 move;
  - direct (i)⇒(iv);
  - Remark 4.4 part 1;
  - §9.2;
  - §9.3 lines;
  - Ex B.1 write-up;
  - Thm 8.1(b) "contains p and some v_i";
  - "U is dominated".

## 4. The author's addition and the audit

| Point | Met? | Comment |
|---|---|---|
| 1. Plain rule; "could make" via added and removed gambles | Yes | Abstract, introduction, and the paraphrase after Def 6.1; Def 2.5 plus the sentence after it. |
| 2. Definition versus consequences | Yes, with one wording fix | Prop 6.2 gives guidance (strict), independence, acyclicity (= finite-chain consistency), disjoint additivity and no ties. "Do not characterise it" appears with the guidance-only witness. "Incomplete and not transitive" must become "in general …" (§0). |
| 3. Short exact characterisation | Yes | Prop 6.3 is correct, short and elementary. Optional sharpening: (1) is redundant for maximality. |
| 4. Repair theorem central | Yes | §1 leads with it; §9.1 says explicitly that maximality does not replace it. |
| 5. Stronger assumption recorded, not investigated | Yes | §9.2 and the open questions. Add "(under (M2))" to the one-line implication. |
| Lead with the repair theorem before the setting | Yes | — |
| Minimax mechanism explained | Yes, except the Lyapunov sentence | See §0. |
| Full-support headline, then how to drop it | Yes | Thm 6.8 last sentence, and introduction item (3). |
| Scope points in statements *and* introduction | Introduction yes; statements partly | Thm 5.1 and 6.8 rely on the "Throughout" of §2.1. Add the hypotheses on E and "modulo null sets" (change 3). The non-uniformity caveat sits right after Thm 6.8; adding a pointer inside 6.8(b) would satisfy "in the statements" literally. |
| Achievement and limitation stated together | Yes | Abstract, the introduction paragraph "What this achieves…", and §9.1. Balanced: neither trivialising nor overclaiming. Optional: "coherence can be characterised by accuracy dominance" (abstract, line 2) could read "represented exactly by a dominance criterion", to pre-empt the independent-argument reading. The abstract does qualify it at the end. |
| One veto–Brier example; rule and significance in text; proofs in appendix; contrast | Yes | No visibility theorem, no catalogue. |
| Restricted-domain corollary kept; one-sided classification demoted | Yes | Cor 7.1; App C. |
| Open questions: nonseparable, no order unit, further domains | Yes | §9.4. |

## 5. Conventions

| Convention | Status |
|---|---|
| Jargon | Line 1075 has "the classical **route** from admissibility to coherence"; "route" is on the banned list. Write "the classical argument". "Region" (line 1079) is ordinary usage and is fine. No certificate, record, safe or gate. The labels (M1)–(M3) carry descriptive names, which the brief allows. |
| Names on theorem-like environments | None as optional arguments. But Ex B.1 ("*Dominance need not be uniform.*"), Ex B.2 ("*The null boundary … is essential.*") and Rem B.3 ("*Replacing 𝟙.*") open with italic titles that act as names. Rewrite them as plain first sentences, e.g. "This example shows that dominance need not be uniform." |
| \coloneqq | Used throughout; no ":=" remains. |
| "Models" | Used throughout the body. The abstract uses "set/sets" for models ("every incoherent set … coherent set"). Either add "(models)" at first use or keep "sets" deliberately for the abstract. Minor. |
| Dominance nomenclature | Standard: weak, dominance, strict, uniform (§6.2). |
| No commentary on drafts | None found. |
| Clean compile | Yes. Recompiled 3× in `ra68a_py/build/`: 0 warnings, 0 overfull, 0 underfull; 24 pages. |
| Citations | Mostly correct; details below. |

Citations in detail:
- **Correct:** Sion (PJM 8:171–176, 1958); Lindenstrauss (J. Math. Mech. 15:971–972, 1966); Lyapunov (Izv. 4:465–478, 1940); Predd et al. (IEEE TIT 55:4786–4792, 2009); Joyce (Phil. Sci. 65:575–603, 1998); Diestel–Uhl (AMS 1977); Walley 1991; Rockafellar Thm 11.3 (proper separation) and Thm 11.6 (supporting hyperplane through a point not in ri), both correctly used.
- **Quaeghebeur chapter, pp. 1–27:** consistent with my knowledge.
- **Aliprantis–Border Thm 6.30:** to my knowledge, the 3rd edition's §6.6 ("Metrizability of weak topologies") has Thm 6.30 as "the closed unit ball of X\* is w\*-metrizable iff X is separable". That is the right result for Lemma 2.1(a). I could not confirm the number online; **the author should confirm against the book.**
- **Standard results cited without reference:** Banach–Alaoglu, Hahn–Banach, bipolar, L^∞ = (L¹)\*. Acceptable, or cite A–B for them too.

## 6. Required changes, ranked

1. **(ERROR, prose.) "Incomplete and intransitive" is stated unconditionally** (abstract l.58; intro l.123–124, l.160–161; §8 l.1005, l.1087). Write "in general incomplete and intransitive" / "need not be transitive or complete (Example 6.4)". With one world the ranking is transitive (proof in §0).
2. **(Inaccuracy, explanation of the minimax lemma, l.455–457.)** Lyapunov's convexity needs non-atomic μ, and (M2) allows atoms (the paper's own δ_𝟙 + δ_{−𝟙}). Add "and a non-atomic μ", and replace "in infinite dimensions it does not" with "in general it need not".
3. **(Audit compliance, statements.)** Add one sentence to the statements of Thm 5.1 and Thm 6.8: "Here Ω is any set, E ⊆ ℓ^∞(Ω) is a separable closed subspace containing 𝟙 (or an order unit, Remark B.3), and models are identified up to μ-null sets." In Thm 6.8(b), add: "(not every dominance is uniform; Example B.1)".
4. **(§9.2.)** Insert "under (M2)" in the one-line implication, since it uses Lemma 6.5. Optional: give the one-pair witness that (3) is strictly stronger.
5. **(Remark 4.4, part 2.)**
   - State that X = N ∪ B = {h₁ + h₂ > 0} is coherent, or (better) replace B by B′ = B ∩ {‖h‖ > 1}. This makes X′ = D_Δ ∪ B′ incoherent, as REF67_out U2 recommended, and the conclusion and proof are unchanged (Q_{B′} = {(½,½)}; m(B′) > 0 at both worlds).
   - Part 1: "mirror image under exchange of coordinates (the ball about (−1,3))".
6. **(Theorem 8.1(a).)** Add "and acyclicity (each ⪯_i is transitive)", since covering requirement (1) includes it.
7. **(Jargon and undefined term.)** l.1075 "route" → "argument". l.1147 "Admissible measures" → "Measures satisfying (M1)–(M3)".
8. **(Names.)** Rewrite the italic lead-ins of Ex B.1, Ex B.2 and Rem B.3 as plain sentences.
9. **(Wording, after Def 6.1.)** "the second clause is the same at every world" → "whether some coherent model could make the change does not depend on ω".
10. **(Optional, Prop 6.3.)** One sentence: the proof shows ⪯_ω is the largest relation with (2) and (3); (1) then follows. This strengthens the explanatory point that the substance lies in (3) and the repair theorem.
11. **(Minor.)**
    - §9.3: also list Bochner integrability and Lemma 2.2 as uses of separability.
    - Introduction scope item (1): "and it is not covered" clashes with the technical "covers"; write "and our results do not apply to it".
    - Abstract: "uses a single minimax argument twice" → "uses one minimax lemma, once in the consistent case and twice in the inconsistent case". Also add "up to null sets" to the first sentence.
    - Ex B.2: rename the exponential variable (β is the margin in Ex B.1).
    - Confirm A–B Thm 6.30 against the book.
12. **(Flag for the lead, not a referee change.)** The author block reads Konek and Campbell-Moore, as the brief requires.

**Recommendation:** accept after changes 1–9. All are local text edits, and none touches a proof.
