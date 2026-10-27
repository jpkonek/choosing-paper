# REF67_out: referee report on `OUT67_application_outline.md` (revision 2)

26 October 2026. Referee REF67_out. I re-derived every proof in the outline by hand, and I checked the outline against its sources (RF67a, RF67b, TS66, REF66_ts, REF66_iw, the universal note and the covering paper). The verdicts below rest on the outline's own proofs.

Labels: PROVED (re-derived or proved here) / CHECKED (exact or high-accuracy computation) / NUMERICS. The script is `ref67out_py/check_examples.py`; run `python3 -I check_examples.py` from that folder. It writes `check_examples.out`.

## Verdict at the top

**The chain is correct.** Every load-bearing step holds as written, under the stated hypotheses:
- setting;
- minimax lemma, for arbitrary Borel G and arbitrary x;
- contraction and trimming;
- Lemma 3.3(a)–(c);
- Theorem 4.1 in both cases, including the location clause;
- ranking corollary;
- Cor 6.1 and Cor 6.2.

The new direct proof of the consistent case is correct. It removes every use of K′ and avoids the circularity that RF67b raised. The one-sided dominance theorem is therefore a genuine restriction of Theorem 4.1.

**N ⊆ hull(X∖N) holds for all of N in both cases, and literally as sets.**
- In the consistent case, hull(X∖N) = hull(X) ⊇ N₀ ⊇ N.
- In the inconsistent case, Q_{X∖N} = ∅, so hull(X∖N) = E.

The safety test "Q_B = ∅ or μ(A ∩ hull B) > 0" is correct, and so is the remark that the hull = E convention alone misclassifies (∅, B).

**One ERROR, in an unrefereed remark.** The flag in Remark 3.4 ("N ⊆ hull(B) requires Q_B = Q") is wrong, and it is contradicted by the outline's own n = 2 example. Under Q_B = Q the family collapses to X = N a.e.

**Five GAPs that need text changes:**
- Part 8: Theorem 8.1 is stated in the visibility form, but its "worked instance" is not an instance of it.
- Cor 6.3(b)–(e) need a Lebesgue-equivalent μ, not just (M1)–(M2).
- Scope: the stated reason for excluding nonseparable spaces is inaccurate, and a nearby positive result is available (§2.4).
- Lemma 1.3(b) calls a strictly larger class "Walley-coherent".
- Theorem 4.1's proof must fix region (B) for the location clause.

There are also several minor wording items. None affects a theorem.

---

## 1. Verdict table

### 1.1 Dependency chain (check 1)

| # | Item | Verdict | Note / repair |
|---|---|---|---|
| C1 | Lemma 1.1 (states, envelopes, norming set) | CORRECT; minor GAP | (e) needs Q₁ convex and weak-* closed (a credal set). Since D_{Q₁} = D_{conv Q₁}, the result is false for nonconvex Q₁. State "for credal sets Q₁, Q₂". (f): Ω′ norms infima, hence also suprema (apply it to −h_j). The 2ε-approximation from the dense sequence is fine. |
| C2 | Lemma 1.2 (existence of μ) | CORRECT | As refereed. |
| C3 | Integrated payoff; accuracy reading c_ω − m_ω(X) | CORRECT | c_ω − m_ω(X) = ∫_{X^c∩{h(ω)>0}} \|h(ω)\| + ∫_{X∩{h(ω)<0}} \|h(ω)\|, finite by (M1). |
| C4 | §1.3 sets versus classes | CORRECT; nit | L and X₊ also depend on the choice of minimiser q\*. Say "for a fixed minimiser". |
| C5 | Lemma 1.3(a) | CORRECT | The counterexample without (M3) (μ carried by D_S ∪ −D_S) satisfies (M1)–(M2) trivially, since P_Q ≠ 0 there. |
| C6 | Lemma 1.3(b) | CORRECT mathematics; **GAP (terminology)** | The class "convex cone, 0 ∉ D, containing every h with inf h > 0" is **strictly larger** than Walley's coherent sets, which must contain every nonzero h ≥ 0. Example: D_{{e₁}} = {h₁ > 0} on ℝ² is in the class but is not Walley-coherent, since (0,1) ∉ D. So "that is, a Walley-coherent set" is false. Repair: "a coherent set of desirable gambles in the weak sense used here; Walley's coherent sets are a subclass". Add: every D_Q is a.e. equal to the Walley-coherent set D_Q ∪ {h ≥ 0, h ≠ 0}, because the difference lies in {P_Q = 0}. So modulo μ the two notions give the same classes. The scope line "Walley-coherent sets are a.e. equal to sets D_Q" is true. |
| C7 | Lemma 1.4(a),(b),(e),(f) | CORRECT | (e) needs no (M2). (f) needs (M2) for {q}. |
| C8 | Lemma 1.4(c),(d) | CORRECT; minor GAP | The "⇐" directions use B ⊆ hull(B) a.e., which is (b) under (M2). Without (M2) they fail: take B ⊆ {q = 0} and Q = {q}. The lemma flags (M2) only in (b), (c)'s last sentence and (f). Add "(M2)" to the equivalences in (c) and (d). |
| C9 | Lemma 2.1 (minimax, any Borel G, any x ∈ E) | CORRECT | Sion applies on S × Z with Φ(q,z) = q(z − x). Both optima are attained. The saddle step shows that every maximiser is 𝟙_{G∩{q\*>0}} for **every** minimiser q\*. Nothing depends on x ∈ T(F_G). |
| C10 | Cor 2.2 | CORRECT | v ≥ 0 because 𝟙_X ∈ F_G. Coherent X gives G = X a.e., so the bracket at q ∈ Q_X is ∫_X q⁻ = 0. If v = 0, then X = G ∩ {q\* > 0} a.e., which is coherent. |
| C11 | Cor 2.3 | CORRECT | With G = X and x = m(X), the bracket is ∫_X q⁻. The maximiser is 𝟙_{X₊}, so q(m(L)) ≤ −v at every state. In (c), "third ⇒ second" uses that m(L) ≠ 0, so L is non-null. The sign convention (keep X₊) is neater than RF67's −T(F_X). |
| C12 | Lemma 3.1 (contraction) | CORRECT | Uses q′ ≥ P on X for q′ ∈ Q_X. Needs no (M2). |
| C13 | Lemma 3.2 (trimming) | CORRECT | Uses only the (M2)-free half of Lemma 1.4(b) (P ≥ 0 a.e. on X). |
| C14 | Lemma 3.3(a) (strict at every world, with (M2)) | CORRECT | If the change is open to D_Q, then Q ⊆ Q_B, so hull(B) ⊆ D_Q. Then A is null and m(N) − m(X) = −m(B) > 0 at every world. So B is non-null, and Lemma 1.4(f) gives Q_B = ∅, a contradiction. N need not be coherent. |
| C15 | Lemma 3.3(b) (uniform, no measure condition) | CORRECT; wording | The proof needs (M1), since m must be defined, but not (M2). Write "without (M2)". |
| C16 | Lemma 3.3(c) | CORRECT | Does not use N ⊆ hull(X∖N) at all. |
| C17 | Theorem 4.1, consistent case (new direct proof) | **CORRECT** (PROVED §2.2) | No step uses an element of K′. The margin comes from τ alone, and μ(N∖X) > 0 comes afterwards from Lemma 3.3(b)+(c), with no circularity. All inclusions are literal. |
| C18 | Theorem 4.1, inconsistent case (one extra minimax) | CORRECT; **GAP (proof must fix region (B))** | Steps 1–4 are correct for both regions. Item 3 of the theorem asserts N ⊆ hull(X₊). This holds for (B). It **can fail for (A)**: there N = D_{conv{q\*,π\*}}, and N ⊆ hull(X₊) would need Q_{X₊} ⊆ conv{q\*,π\*}. The theorem is existential, so it is true, but the proof as written ("choose one of two regions") does not prove item 3 under (A). Repair: prove the theorem with (B), and move (A) to a remark ("on E one may instead take G₁ = {q\* > 0}; the location clause then weakens to N ⊆ {q\* > 0}"). |
| C19 | Location clause and degenerate cases | CORRECT | X₊ null: G₁ = D_S, N = D_S. N∖X null: closed because Q_{X∖N} = ∅. X = E: N = hull({q\*>0}). This is literally D_{q\*} under (M3) and a.e. equal to it otherwise. With (A) it is a.e. D_{q\*}, because q\* is itself a minimiser of the second problem (v₁ = v). |
| C20 | Lemma 5.1 (test) | CORRECT | See check 2. Joining needs no disjointness for this step. |
| C21 | Def 5.2, Prop 5.3 | CORRECT; nit | Prop 5.3(b): positivity of a guided increment follows from the strict inequalities in "guided". The appeal to {h(ω) = 0} null is not needed there; it is needed in Lemma 5.4, step 3. |
| C22 | Lemma 5.4 and the protection note | CORRECT | The −(ω−s)² counterexample was re-derived: P_Q(h_s) = 0 forces Q = {δ_s}, and the curve {h_s} meets each line g + ℝ𝟙 at most once, so it is μ_std-null. |
| C23 | Props 5.5–5.6 | CORRECT | The change from C to Y is open to C. (iii)⇒(ii)⇒(i) is trivial and should be listed. |
| C24 | Theorem 5.7(a)–(f) under (M1)–(M2) | CORRECT | N ≠ X a.e. because N is coherent and X is not. |
| C25 | Example 5.8 | CORRECT | REF66_iw §2.1's construction works verbatim on E. B ⊆ V ⊆ {a + b/2 > 0} gives Q_B ∋ q_{1/2}, and hull(B) ⊇ D_S ⊇ A₀. |
| C26 | Example 5.9 (ℝ², not transitive) | CORRECT; CHECKED independently | Disjoint balls. Q_A = {t ≥ 0.535444}. min over Q_A × A₁ of q·h = 0.358 > 0. Increment 0.014511 > 0. A′ ⊆ {h₂ < 0}. |
| C27 | Cor 6.1(a)–(d) | CORRECT | (b): X∖(N∩U) = X∖N because X ⊆ U, so the hull clause survives the trace. Uses region (B) (see C18). |
| C28 | Cor 6.2(a),(c),(d) | CORRECT | (c): k₀ ∈ K, as the norm limit of normalised partial sums. k₀(h) = 0 with h ∈ C_K forces h ∈ K_⊥. (d): both contamination claims were re-derived via full support of p, resp. r, and continuity. |
| C29 | Cor 6.2(b) | CORRECT; GAP (no proof given) | Add: for finite n, "k(h) > 0 for all h ∈ C_K∖{0}" ⟺ K is full-dimensional and k ∈ relint K. This is the note's Lemma "LF"(b), or the covering paper's Lemma "fulldim"(c),(d), via a supporting hyperplane. |
| C30 | Cor 6.3(a) | CORRECT | The case E = ℝⁿ. |
| C31 | Cor 6.3(b)–(e): hypotheses | **GAP** | The heading assumes only "(M1)–(M2); for example …". But (b)–(d) are (LF) characterisations, which need (M3): open O ⊆ U a.e. must imply O ⊆ U. (e) uses Lebesgue density points, which needs Lebesgue's null sets. (d) with the note's definition of one-sidedness (U ∩ −U null) also uses symmetric null sets; with Cor 6.2(c)'s definition it does not. Repair: assume μ has Lebesgue's null sets (the finite (M)) for (b)–(e), and use one definition of "one-sided" throughout (6.2(c)'s). |
| C32 | Cor 6.3(b) | CORRECT (with C31) | V₀ = {sup h > 0} is closed under hulls. An open O ⊆ V₀ a.e. avoids int(−ℝⁿ₊), hence avoids −ℝⁿ₊. If K ∩ relint Δ = ∅, then some coordinate i vanishes on K, and −e_i ∈ ∂D_K∖V₀. |

### 1.2 The hull inclusion and the test (check 2)

| # | Item | Verdict | Note |
|---|---|---|---|
| H1 | N ⊆ hull(X∖N) for **all** of N, consistent case | CORRECT | Literal. Q_{X∖N} = Q_X exactly (Lemma 3.2), so hull(X∖N) = D_{Q_X} = G ⊇ N₀ ⊇ N. |
| H2 | N ⊆ hull(X∖N), inconsistent case; hull(X∖N) = E | CORRECT | N ⊆ G₁ ⊆ {q\* > 0} and L ⊆ {q\* < 0}, so L ⊆ X∖N literally. Q_{X∖N} ⊆ Q_L = ∅ (Lemma 1.4(a),(e)). This holds with either region. |
| H3 | Convention hull(B) = E when Q_B = ∅ | CORRECT, consistent | It agrees with D_∅ = E. On ℝⁿ it is also the value of the hull formula cone(B_d) + ℝⁿ₊₊ (§2.3). Lemma 3.3 never evaluates the convention: openness forces Q_B ≠ ∅. **Expository addition:** in the inconsistent case the clause holds *because* the abandoned commitments are inconsistent. The informative facts there are Q_{X∖N} = ∅ and N ⊆ hull(X₊). One sentence after item 2 of Theorem 4.1 would prevent a reader from taking the clause as substantive in that case. |
| H4 | Test "Q_B = ∅ or μ(A ∩ hull B) > 0" (Lemma 5.1) | CORRECT | If Q_B ≠ ∅ and μ(A ∩ hull B) = 0, the change is open to the coherent set hull(B) ⊇ B a.e. (needs (M2)). Conversely, openness to D_Q gives hull(B) ⊆ D_Q. The misclassification remark about (∅, B) is correct, and it is the only misclassification. |

### 1.3 Items listed as unrefereed (check 3)

| # | Item | Verdict | Note |
|---|---|---|---|
| U1 | Remark 1.5 (reweighting) | CORRECT (PROVED) | μ_w is finite (∫w < ∞). It has μ's null sets (w > 0), hence (M2). (M1) holds by ∫w‖h‖ < ∞. (M3) holds because w > 0. Per-world positive constants leave the ranking unchanged, since only signs of m_ω-differences enter. Nit: say "the ranking is unchanged". Theorem 4.1's *uniform* margin for the rescaled score needs inf_ω c_ω > 0. |
| U2 | Remark 3.4, second bullet (n = 2 example) | CORRECT (PROVED; CHECKED) | Q_{X∖N} = {(½,½)}: the masses of (X∖N) ∩ {q·h < 0} are positive for t ≠ ½ (Gaussian μ). hull(X∖N) = X ⊇ N. The change (∅, X∖N) is open to X. (½,½)·m(X∖N) = 0.084 > 0. State the measure: any μ of full support works. **Weakness:** X is coherent here, so the change is trivially open to X itself. An incoherent instance is stronger (§2.1): X′ = int ℝ²₊ ∪ (B ∩ {\|h\| > 1}). I recommend replacing the example with it. |
| U3 | Remark 3.4, third bullet (flag "Q_B = Q") | **ERROR** (PROVED §2.1) | Write B for X∖N, so B is disjoint from D_Q and non-null. Literal N ⊆ hull(B) ⟺ D_Q ⊆ D_{Q_B} ⟺ **Q_B ⊆ Q** (Lemma 1.1(e)). Openness of (∅, B) ⟺ Q_B ≠ ∅. So the correct family is **∅ ≠ Q_B ⊆ Q**. RF67b's "Q ⊆ Q_B" is a reversed inclusion, and "Q_B = Q" is the degenerate case: Q ⊆ Q_B gives B ⊆ D_Q a.e. under (M2), so B is null and X = N a.e. The outline's own n = 2 example has Q = Δ ⊋ Q_B = {(½,½)}, contradicting the flag. Repair: "RF67b's family: X = D_Q ∪ B with B disjoint from D_Q, non-null, and ∅ ≠ Q_B ⊆ Q; then N = D_Q ⊆ hull(B) and the change is open to hull(B). The n = 2 example is the case Q = Δ." |
| U4 | Cor 6.1, example D_{K′} ∪ F, F ⊆ {sup h ≤ 0} | CORRECT; GAP (proof incomplete) | The outline proves only that B ∩ F is null. Complete it: then B ⊆ D_{K′} a.e., so K′ ⊆ Q_B, so hull(B) = D_{Q_B} ⊆ D_{K′} ⊆ U. Require F Borel. This is the infinite-dimensional form of the **refereed** TS66 Prop 3.2(b) ("D_{K′} ∪ E with E ⊆ −ℝⁿ₊", REF66_ts row 7b). Cite it, so the item is not new. |
| U5 | Assembly of the consistent case on E without Thm 7.7 | CORRECT (PROVED §2.2) | No circularity. Lemma 3.3(b) uses only the margin and the hull inclusion. (c) then gives μ(N∖X) > 0. The outline's claim that Thm 7.7's only K′-dependent step is replaced is accurate: Step A's use of K′ is replaced by the hypothesis Q_X ≠ ∅, and Step C's by Lemma 3.3(c). |
| U6 | Cor 6.3(e) (geometric test) | CORRECT under Lebesgue null sets (PROVED §2.3); GAP (hypothesis, C31) | Both disjuncts were re-derived. Q_B = ∅ ⟺ cone(B_d) meets −ℝⁿ₊₊, by separating a convex set from an open convex cone; conic Carathéodory gives ≤ n points. When Q_B ≠ ∅, μ(A ∩ hull B) > 0 ⟺ some a ∈ A_d lies in cone(B_d) + ℝⁿ₊₊ (the note's Lemma "hullformula", whose proof does not use U). |
| U7 | Remark 3.4 flag | see U3 | — |

### 1.4 Scope statement (check 4)

| # | Claim | Verdict | Note / repair |
|---|---|---|---|
| S1 | Ω arbitrary; E separable, closed, with inf e > 0 | CORRECT | — |
| S2 | "ℓ∞(Ω) … nonseparable, and a nonseparable normed space carries no finite full-support Borel measure" | TRUE but **misleading (GAP)** | The fact is true: an uncountable ε-separated set gives uncountably many disjoint balls. But by the scope's own account, (M3) is used only for identification. So this is not why the theorem fails to reach ℓ∞(Ω). **Nearby result (PROVED, sketch, §2.4):** on any closed F ⊆ ℓ∞(Ω) with 𝟙 ∈ F, nonseparable allowed, Theorems 4.1 and 5.7 hold verbatim for every finite Borel μ concentrated on a separable closed subspace E ∋ 𝟙. By Marczewski–Sikorski, that is every finite Borel μ, unless the density character of F is real-valued measurable. What is lost is only identification: distinct credal sets of F with the same restriction to E give the same model. Repair the bullet and the "Open" list accordingly ("nonseparable spaces: existence and dominance hold; the open question is an analogue of (M3)"). This needs an independent referee before it is stated as a theorem. |
| S3 | Order unit: "a world at which every gamble pays 0 makes every model undominated" | CORRECT | At such ω₀ only null changes are guided or have positive increment. |
| S4 | Coherence modulo μ; μ-dependence; mutually singular admissible μ | CORRECT | — |
| S5 | "(M3) only identifies distinct credal sets with distinct models" | **Incomplete** | (M3) is also used for the (LF) characterisations of Cor 6.2 and Cor 6.3(b)–(d), as §1.2 of the outline itself says. Add this. |
| S6 | Score: every μ with (M1)–(M2); reweightings absorbed; no claim about other scores | CORRECT | Matches the decision (AUDIT_r67_message2 §3). |
| S7 | Strict vs uniform; finite worlds coincide | CORRECT | — |
| S8 | "The dominance relation depends on the world set (Ω versus Ω₀). The undominated set does not." | CORRECT but unsupported in the outline | Cite REF66_iw §2.3 (refereed example: m(r) = β(ω − ω\*)² in span{1, ω, ω²}). Note in one line that Prop 5.5 and Lemma 5.4 already allow any Ω′ norming infima. |
| S9 | Interpretation paragraph | CORRECT | — |
| S10 | Open list | Mostly CORRECT | "Uniform (LF)" is not defined anywhere in the outline. Define it in one line (a norm-open tube of fixed radius) or drop it. Revise the nonseparable item per S2. |
| S11 | Completeness | GAP (minor) | Also say that Part 8 is finite-world and one-sided, and that the finite corollaries (Cor 6.3(b)–(e)) need Lebesgue-equivalent μ. |

### 1.5 Representative construction (check 5)

| # | Item | Verdict | Note / repair |
|---|---|---|---|
| V1 | Theorem 8.1 versus covering paper Thm "vis" (last sentence) and Thms "family", "cover" | CORRECT as a pointer | K full-dimensional; K′ = K_δ; A_i = K ∩ conv(K′ ∪ {e_i}); veto max(0, max_{A_i}(−v·h)) then −∫h_i, lexicographic. Complete, transitive, (G), (IB), (GC), (C), (ID), (W); D_K undominated; (LF). The undominated family is D_{K(W₀,β,α)}. All match. The outline's definition of uniform visibility builds in K_δ ≠ ∅, which is harmless (decreasing δ preserves it). |
| V2 | "Worked instance" (contamination) | **GAP (mismatch)** | Cor "contam" uses K′ = {p} (or p + s(K − p)) and A_i = {v_i}. This is **not** of the form K′ = K_δ, A_i = K ∩ conv(K_δ ∪ {e_i}), so it is not an instance of Theorem 8.1 as stated: its veto differs. It is an instance of the general Thm "cover" (any K′ ⊆ relint K, A_i ⊆ conv(K′ ∪ {e_i}) compact, K = conv(K′ ∪ ⋃A_i)). **Repair:** state Theorem 8.1 in that general form, which is simpler and self-contained. Then state the visibility characterisation (Thm "vis") as the description of the class. |
| V3 | Class sentence | GAP (wording) | "every K for n = 2" should be "every full-dimensional K for n = 2" (Cor "n2"). Lower-dimensional K are never covered on one-sided domains. "ε-contaminations" should be "interior ε-contaminations (p ∈ relint Δ)". "Total-variation neighbourhoods" needs δ < min p_j. |
| V4 | Proof sketch, step 5 | GAP (wording) | "the minimiser with weight p ∈ K′ at every world" is garbled. It should say: the admissible triple (Ω, p, ∅), with every veto forced to zero and Brier weights p, gives K(Ω,p,∅) = conv(K′ ∪ ⋃A_i) = K. Steps 1–4 match Thm "route" and Lemmas "lyap", "zorn", "sep", "unique", "coh". |
| V5 | Refereeing pointer "[…; earlier rounds]" | GAP | No referee note for Thms "family"/"cover"/"vis" is in this folder. Name the round and report that refereed them; otherwise mark the section "pointer to an unrefereed draft result". |
| V6 | Framing ("not an independent justification of coherence") | CORRECT | Matches AUDIT_r67_message2 §5. |

### 1.6 Cut list and glossary (check 6)

| # | Item | Verdict | Note |
|---|---|---|---|
| K1 | Universal-note cut list | Sensible | Nothing essential is cut. Two imports are missing: REF66_iw §2.3 (world-set dependence, for Part 7) and Lemma "fulldim"(c),(d) or the note's Lemma "LF"(b) proof (for Cor 6.2(b)). |
| K2 | Covering-paper cut list | Sensible | Keeping Lemma "dominance"(b) and the Remark "TC" footnote is right. Part 8 also needs Lemma "LF"(a) of the covering paper; it is absorbed by Cor 6.2(a). |
| K3 | Glossary | Sensible; one inversion | (TC) is the two-step case of (FCC). (FCC) *is* acyclicity (no strict reversal of any finite chain). Mapping (TC) → "acyclicity" and (FCC) → "finite-chain consistency" inverts the natural names. Suggest (TC) → "no strict reversal of a two-step chain" and (FCC) → "acyclicity". The same applies to Prop 5.3(b)'s wording. |

### 1.7 Jargon check (check 7)

| # | Item | Verdict | Note |
|---|---|---|---|
| J1 | "certificate", "record", "safe", LDG labels in statements | PASS | They occur only in the glossary and in the cut list's description of sources. |
| J2 | "route(s)" | Minor FAIL (not in statements) | Lines 254 ("RF67b's route"), 301 ("one-minimax route"), 306 ("The audit's route"). Replace with "proof" or "argument". |
| J3 | "relaxed minimax" (proof heading, line 287) | Minor FAIL | The glossary replaces "relaxed choice" with "weighted acceptance choice". Write "one more application of Lemma 2.1". |
| J4 | Referee tags and file names in headers | Fine for an outline | They must be stripped from the manuscript. |
| J5 | Named theorem environments | Note for the manuscript | The author's convention is no names in theorem environments, as in `\begin{theorem}\label{…}`. The parenthetical names ("(repair)", "(minimax over weighted acceptance choices)") should become prose before the statement. |

---

## 2. Supporting proofs (PROVED)

### 2.1 Remark 3.4: the correct family, and an incoherent example

**Claim.** Let X = D_Q ∪ B, with B Borel, disjoint from D_Q and non-null, and let N = D_Q.
- N ⊆ hull(B) (literally) ⟺ ∅ ≠ Q_B ⊆ Q, or Q_B = ∅.
- The change from X to N is open to a coherent model ⟺ Q_B ≠ ∅.

So the hull inclusion holds while the change is open exactly when ∅ ≠ Q_B ⊆ Q.

*Proof.*
- If Q_B ≠ ∅: D_Q ⊆ D_{Q_B} ⟺ Q_B ⊆ Q, by Lemma 1.1(e) applied to the credal sets Q and Q_B. The converse is immediate.
- The change is (∅, B). It is open to Z ⟺ B ⊆ Z a.e. Some coherent Z works ⟺ Q_B ≠ ∅ (Lemma 1.4(d), with (M2)).
- If Q ⊆ Q_B, then B ⊆ D_Q a.e. under (M2), contradicting "B disjoint from D_Q, non-null". So "Q_B = Q" is impossible in a non-degenerate instance. ∎

**Incoherent instance (CHECKED numerically).**
- n = 2, Gaussian μ, Q = Δ, N = int ℝ²₊.
- B′ := {h₁ + h₂ > 0, min(h₁,h₂) ≤ 0, \|h\| > 1}. It contains neighbourhoods of (−t, t+s) and (t+s, −t) for all large t, so Q_{B′} = {(½,½)} ⊆ Q.
- X′ := N ∪ B′. Its hull is {h₁ + h₂ > 0}, and it misses the non-null set B ∩ {\|h\| ≤ 1} (mass 0.100). So X′ is incoherent.
- N ⊆ hull(X′∖N) = {h₁ + h₂ > 0}.
- The change (∅, B′) is open to {h₁ + h₂ > 0}.
- m(B′) = (0.0672, 0.0672), so the gain −m(B′) is negative at both worlds.

This shows directly, for an *incoherent* model, that the hull inclusion alone does not close the change.

### 2.2 The consistent case on E (assembly)

Hypotheses: (M1)–(M2), X incoherent, Q_X ≠ ∅.
1. G = D_{Q_X}. X ⊆ G a.e., and P ≥ 0 a.e. on X (Lemma 1.4(b)).
2. Cor 2.2 gives v > 0, q\* and N₀ = D_{conv(Q_X ∪ {q\*})}, with q(m(N₀) − m(X)) ≥ v for all q ∈ S.
3. N_τ = D_{conv(Q_X ∪ {q\*} ∪ Q_τ)}. This is a credal set: the convex hull of finitely many weak-* compact convex sets is compact.
4. P_{Q_τ} = P − τ(P − P_S) ↓ in τ. P > 0 on N₀. So N_τ ↑ N₀ as τ ↓ 0.
5. ‖m(N₀) − m(N_τ)‖ ≤ ∫_{N₀∖N_τ} ‖h‖ dμ → 0 (dominated convergence, (M1)). Choose τ with this ≤ v/2. States have norm 1, so q(m(N) − m(X)) ≥ v/2 for all q.
6. Lemma 3.2 (no (M2) needed): Q_{X∖N} = Q_X, so hull(X∖N) = G ⊇ N₀ ⊇ N. These are literal set equalities and inclusions.
7. Lemma 3.3(b) (margin v/2 plus 6) gives closedness. Lemma 3.3(c), with Q_{X∖N} = Q_X ≠ ∅, gives μ(N∖X) > 0.

Step 7 does not feed back into the choice of τ, so there is no circularity. No element of any K′ is used. ∎

### 2.3 Cor 6.3(e) (μ with Lebesgue's null sets)

1. **Q_B in terms of density points.** Q_B = {q ∈ Δ : q·b ≥ 0 for all b ∈ B_d} (density points carry mass, and B∖B_d is null).
2. **When Q_B is empty.** Q_B = ∅ ⟺ the convex cone cone(B_d) meets the open convex cone −ℝⁿ₊₊.
   - If they are disjoint, a separating q ≠ 0 has q ≥ 0, and q ≥ 0 on B_d, so q/(𝟙·q) ∈ Q_B.
   - Conversely, a point of cone(B_d) ∩ −ℝⁿ₊₊ excludes every q ∈ Δ.
   - Conic Carathéodory gives at most n generators. This is the first disjunct.
3. **The hull formula.** hull(B) = cone(B_d) + ℝⁿ₊₊. The note's proof of Lemma "hullformula" uses no domain. When Q_B = ∅ the same argument shows the right side is ℝⁿ, which agrees with the convention.
4. **When Q_B is nonempty.** μ(A ∩ hull B) > 0 ⟺ some a ∈ A_d lies in the open set hull(B) ⟺ a − Σ_{j≤n} t_j b_j ≫ 0. This is the second disjunct.
5. **Assembly.** By Lemma 5.1, the change is closed ⟺ (first disjunct) or (Q_B ≠ ∅ and second disjunct). The second disjunct with Q_B = ∅ is subsumed by the first. ∎

### 2.4 Nonseparable gamble spaces (nearby result; sketch, needs a referee)

**Setting.**
- F ⊆ ℓ∞(Ω) is closed with 𝟙 ∈ F. It may be nonseparable.
- μ is a finite Borel measure on F with μ(F∖E) = 0 for some separable closed subspace E ∋ 𝟙.
- Assume (M1), and (M2) for the credal sets of F.

**The restriction map.** Let r : S(F) → S(E) be restriction. It is affine and weak-* continuous. It is onto: a state of E is dominated by the sublinear map p(h) = sup_Ω h on F, and a Hahn–Banach extension dominated by p is positive and normalised.

**What r does.**
- For a credal set Q ⊆ S(F), r(Q) is credal in S(E), and D_Q ∩ E = D^E_{r(Q)}.
- For a credal set Q′ ⊆ S(E), r⁻¹(Q′) is credal in S(F) and r(r⁻¹Q′) = Q′.
- Q^F_B = r⁻¹(Q^E_{B∩E}), so hull^F(B) ∩ E = hull^E(B ∩ E).
- (M2) on F ⟺ (M2) on E.
- The Bochner integral m takes values in E. m_ω, guidance and the test of Lemma 5.1 agree on traces.

**Transfer.** Apply Theorem 4.1 on E and lift the repair: N := D^F_{r⁻¹(Q′)}. Its trace on E is the E-repair.
- The hull inclusion lifts literally: Q^E_{X∖N} ⊆ Q′ gives r⁻¹(Q^E_{X∖N}) ⊆ r⁻¹(Q′).
- Protection is Lemma 5.4 on E.

Hence Theorems 4.1 and 5.7(a)–(f) hold on F.

**What fails.** (M3) fails, since a finite measure on a nonseparable metric space has no full support. Distinct credal sets with the same restriction r(Q) give the same model.

**When the hypothesis holds.** By the Marczewski–Sikorski theorem, every finite Borel measure on a metric space whose weight is not real-valued measurable has separable support. So the concentration hypothesis is automatic for ℓ∞(Ω) unless 2^{\|Ω\|} is at least a real-valued measurable cardinal.

**Consequence for the scope.** For nonseparable spaces the existence and dominance theorems are not open. What is open is identification: whether some natural measure-class assumption replaces (M3).

## 3. Numerics (`ref67out_py/check_examples.out`)

**Example 5.9** (standard Gaussian, polar quadrature, tolerance 10⁻¹¹):
- m₁(A) = 0.0018348;
- m₁(A₁) = 0.0190130;
- m₁(A₂) = −0.0026671;
- increment 0.0145111 > 0 (RF67b: 0.01451);
- Q_A = {t ≥ 0.535444};
- min over Q_A × A₁ of q·h = 0.3582 > 0;
- all disjointness and sign conditions hold.

**Remark 3.4** (grid quadrature, step 0.02, \|h\| ≤ 12):
- μ(B ∩ {q·h < 0}) > 0 for t ∈ {0.3, 0.45, 0.49, 0.51, 0.55, 0.7}, and = 0 at t = ½;
- (½,½)·m(B) = 0.0842;
- incoherent variant as in §2.1.

These computations illustrate; the verdicts rest on §1–§2.

## 4. Required changes, ranked

1. **(U3, ERROR.)** Rewrite Remark 3.4's third bullet. The family is X = D_Q ∪ B with B disjoint from D_Q, non-null, and ∅ ≠ Q_B ⊆ Q. "Q_B = Q" forces B null. The n = 2 example is the case Q = Δ. Also note that RF67b's "Q ⊆ Q_B" is reversed.
2. **(V2–V5.)** Part 8:
   - state Theorem 8.1 in the general Thm "cover" form, so that the contamination instance is a real instance, with Thm "vis" as the class description;
   - fix "every K for n = 2" (full-dimensional), "interior" contaminations, and step 5's wording;
   - give a concrete refereeing pointer, or mark the section unrefereed.
3. **(C31, U6.)** Cor 6.3: assume μ has Lebesgue's null sets for (b)–(e). Use Cor 6.2(c)'s definition of one-sidedness.
4. **(S2, S5, S8, S10, S11.)** Scope:
   - replace the nonseparability sentence with the accurate statement (§2.4), and update "Open";
   - add the (LF) characterisations to the uses of (M3);
   - cite REF66_iw §2.3;
   - define or drop "uniform (LF)";
   - mention the finite and one-sided scope of Part 8 and Cor 6.3(b)–(e).
5. **(C18, H3.)** Theorem 4.1: prove the inconsistent case with region (B), and give (A) as a remark with its weaker location clause. Add one sentence saying that in the inconsistent case the hull clause holds because the abandoned commitments are inconsistent; the content is Q_{X∖N} = ∅ and N ⊆ hull(X₊).
6. **(C6.)** Lemma 1.3(b) and Part 7: the class is coherence in the weak sense, which strictly contains Walley's. Every D_Q is a.e. equal to a Walley-coherent set, so the classes modulo μ coincide.
7. **(U2.)** Replace or supplement the n = 2 example with the incoherent instance of §2.1, and state the measure (any μ of full support).
8. **(U4, C29.)** Complete the D_{K′} ∪ F proof (K′ ⊆ Q_B) and cite TS66 Prop 3.2(b). Add the one-line proof of Cor 6.2(b).
9. **(C1, C8, C15.)** Hypothesis hygiene:
   - Lemma 1.1(e) needs credal sets;
   - Lemma 1.4(c),(d) "⇐" needs (M2);
   - Lemma 3.3(b) is "without (M2)" (it still needs (M1)).
10. **(K3, J2, J3, J5.)** Wording:
    - glossary names for (TC) and (FCC);
    - remove "route(s)" and "relaxed minimax";
    - no named theorem environments in the manuscript.
11. **(Minor.)**
    - "Thinly spread" remark: specify countable unions. The finite-sub-union fact is not what gives v > 0; Cor 2.3(a) is.
    - Naive-repair remark: "at the minimax prior" (REF66_ts G8).
    - Prop 5.3(b) proof: drop the unnecessary null-set appeal.
    - Prop 5.6: list (iii)⇒(ii)⇒(i).
    - §1.3 item 1: "for a fixed minimiser q\*".

**Bottom line.** With changes 1–6 made, I would accept the outline as the mathematical skeleton for the definitive application paper. The headline theorem, its location clause and the ranking corollary are correct under (M1)–(M2) as stated.
