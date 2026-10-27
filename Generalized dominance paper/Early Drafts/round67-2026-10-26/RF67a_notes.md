# RF67a: referee report on the full-domain infinite-world theorem (AUDIT_r67_brief §2)

26 October 2026. Referee RF67a. I worked independently and did not read `RF67b_notes.md`. I checked every step by hand against the established setting (§7 of the universal-coverage draft) and the refereed one-sided theorem (Theorem 7.7 = `thm:Hinf`). Labels: PROVED (re-derived here) / CHECKED / NUMERICS / CONJECTURE. The scripts are in `rf67a_py/`; run `python3 -I fulldomain_check.py` from that folder, which writes `fulldomain_check.out`.

## Verdict at the top

**The full-domain theorem holds.** The Proposition (the uniformly losing part) and the Theorem (full-domain coverage on E) are both correct. I found no error in any step that carries weight. One auxiliary sentence in the protection paragraph is false as written ("sure losses uniformly negative a.e."). It is not needed, and the repair is one line (E3). The other items are expository gaps or sharpenings of scope.

### Exact hypotheses

| | Hypothesis | Used for |
|---|---|---|
| H1 | Ω is any nonempty set. | — |
| H2 | E ⊆ ℓ∞(Ω) is a sup-norm-closed, **separable** linear subspace with **1 ∈ E**. The constant 1 may be replaced by some e ∈ E with inf_Ω e > 0, by transport (Remark 7.11). | S is weak-* compact and metrizable; P_Q(h + t1) = P_Q(h) + t; Bochner integrals; the countable norming set |
| H3 | (M1) μ is a finite Borel measure on (E, ‖·‖) with ∫‖h‖ dμ < ∞. | Bochner integrals; L∞ = (L¹)*; dominated convergence |
| H4 | (M2) μ{P_Q = 0} = 0 for every credal set Q (nonempty, weak-* closed, convex). | Instances used: Q = {q} for states q (including q\* and δ_ω), Q = Q_B, the convex hulls in Theorem 7.7, (1−τ)Q + τS, and **Q = S (essential for protection; Example 7.4)** |
| H5 | (M3) Full support. | **Only** to make Q ↦ [D_Q] injective, so that distinct credal sets give distinct models and every coherent model has a unique credal set. It is **not** used for the Proposition, the Theorem, protection, the ranking properties, or coverage on E. |

**Conventions.**
- Models are the Borel subsets of E (equivalently, sets measurable for the completion of μ) modulo μ-null sets.
- A model is coherent if its class contains some D_Q, Q a credal set. By Prop. 7.16, which needs only (M2), these are exactly the classes of the coherent sets of desirable gambles.
- Q_B := {q ∈ S : q(h) ≥ 0 for μ-a.e. h ∈ B}. hull(B) := D_{Q_B}, with hull(B) := E when Q_B = ∅.

### Statement as verified

> **Proposition (PROVED).** Assume H2–H4 (only Q = {q} is needed from H4). For Borel X ⊆ E, Q_X = ∅ holds if and only if η := min_{q∈S} ∫_X q(h)⁻ dμ > 0. In that case there is q\* ∈ S such that L := X ∩ {q\* < 0} satisfies q(m(L)) ≤ −η for **every state** q. Equivalently, m(L)(ω) ≤ −η for every ω ∈ Ω.
>
> **Theorem (PROVED).** Assume H2–H4. Every incoherent model X on E has a coherent N with the following properties.
> - **Margin.** inf_{q∈S} q(m(N) − m(X)) > 0, so the margin is uniform at every world.
> - **Hull inclusion.** N ⊆ hull(X∖N).
> - **Safety.** The record r(N,X) is safe.
>
> If Q_X ≠ ∅, then in addition hull(X∖N) = hull(X) and μ(N∖X) > 0. If Q_X = ∅, then in addition N ⊆ D_{{q\*}}, Q_{X∖N} = ∅ (so hull(X∖N) = E), and the margin is at least η.
>
> Consequently the simple ranking on M_E has all of the following:
> - reflexivity, a.e.-ties, (G), (IB), (TC), (FCC) and (Add);
> - for Y ≠ X a.e.: weak dominance ⟺ dominance ⟺ strict dominance ⟺ r(Y,X) safe and m_ω(Y) > m_ω(X) for every ω;
> - no coherent model has a weak dominator other than itself;
> - undominated = coherent;
> - (GC), (ID), (W), and strong (C);
> - it **covers every D_Q, Q any credal set**, with literal (LF) (N = E). This includes precise and finitely generated Q in infinite-dimensional E.
>
> With H5 these targets are pairwise distinct models.

**Not claimed, and false.** Not every dominance relation has a uniform margin. REF66_iw §2.1's counterexample works verbatim on E. Only the constructed repair N is uniform.

---

## 1. Verdict table

| # | Item (BRIEF67 check list) | Verdict | Note / repair |
|---|---|---|---|
| P1 | Z = {−∫ f h dμ : f ∈ F_X} is norm-compact and convex | CORRECT | Same proof as Step B of Thm 7.7, with G replaced by any Borel X. F_X is weak-* compact because L∞(μ) = L¹(μ)* (μ finite). T is a uniform limit, on the L∞ unit ball, of finite-rank weak-*-continuous maps. Z is a continuous linear image of a compact convex set. |
| P2 | Minimax: existence, attainment, value | CORRECT | Sion's theorem applies on S × Z with S ⊆ (E\*, w\*), Z ⊆ (E, ‖·‖) and payoff q(z). The payoff is bilinear and jointly continuous, since ‖q‖ = 1. **Value:** max_z q(z) = ∫_X q(h)⁻ dμ =: F(q). **Attainment:** z ↦ min_S q(z) = inf_Ω z is 1-Lipschitz on the compact Z; F is weak-* continuous on S (dominated convergence with dominating function ‖h‖, along sequences, since S is metrizable); S is compact. |
| P3 | η > 0 | CORRECT | F(q) = 0 ⟺ q ∈ Q_X. F is continuous and positive on the compact S, so min F > 0. **Separability is used here**, through sequential continuity. |
| P4 | The relaxed choice is the indicator of L = X ∩ {q\* < 0}; {q\* = 0} is null | CORRECT | Saddle: η = min_S q(z\*) ≤ q\*(z\*) ≤ max_Z q\*(·) = η. So with z\* = −T f\*, f\* maximises ∫ f·(−q\*(h)) dμ over F_X, which forces f\* = 1 a.e. on X ∩ {q\*<0} and f\* = 0 a.e. on X ∩ {q\*>0}. X ∩ {q\* = 0} is null by (M2) with Q = {q\*}. Hence z\* = −m(L). Non-injectivity of T is harmless. **Neither non-atomicity nor Lyapunov is needed.** μ may even have atoms at gambles h with inf h > 0 or sup h < 0, since these lie off every {q = 0}. |
| P5 | m(L) ≤ −η at every world, and this means at every state | CORRECT | min_S q(−m(L)) = η, so q(m(L)) ≤ −η for **all** q ∈ S, including states that are not evaluations. By Lemma 7.1(b), sup_Ω m(L) = max_S q(m(L)). So "at every world" and "at every state" are equivalent here. L is non-null, since m(L) ≠ 0. |
| P6 | Converse and Lemma E | CORRECT (nearby result) | If some Borel L ⊆ X and ε > 0 have m(L) ≤ −ε1, then Q_X = ∅. So Q_X = ∅ ⟺ η > 0 ⟺ X contains a Borel part with a uniform sure-loss moment. This is the infinite-world Lemma E. Unlike TS66's version, it needs no Lyapunov. |
| T1 | Case Q_X ≠ ∅: applying Thm 7.7 | CORRECT; GAP (which K′) | Cleanest choice: K′ := {q₀} for any q₀ ∈ Q_X, with U′ := D_{q₀}. Then X ⊆ U′ a.e. by (M2) for {q₀}. Use the model X ∩ U′, which is incoherent because it equals X a.e. Thm 7.7 needs only (M1)–(M2). It returns N ⊆ hull(X) = hull(X∖N) with μ(N∖X) > 0 and a margin at every state. The audit's choice K′ = Q_X with U′ = hull(X) is also legitimate (Q_X is a credal set by the proof of Lemma 7.5(a), which does not use K′). Hull invariance is preserved under a.e. modification. **Repair:** name K′ and U′ explicitly. |
| T2 | Safety transfers from U′ to E | CORRECT | Lemma 7.6 (i)⟺(ii): on U′, safe ⟺ the record applies to no D_Q at all, which is safety on E. Explicitly: μ((N∖X) ∩ hull(X∖N)) = μ(N∖X) > 0, and if r applies to D_Q then hull(X∖N) ⊆ D_Q. |
| T3 | Case Q_X = ∅: X₊ := X ∩ {q\* > 0}, and m(X₊) − m(X) = −m(L) ≥ η1 | CORRECT | X = X₊ ⊔ L ⊔ (X ∩ {q\* = 0}), where the last set is null. Margin ≥ η at every state. |
| T4 | q\* ∈ Q_{X₊} | CORRECT | q\*(h) > 0 on X₊, pointwise. |
| T5 | X₊ coherent: N := X₊ | CORRECT; GAP (representative) | Take N := D_Q for a Q with X₊ = D_Q a.e. Then N ⊆ {q\* > 0} **a.e.** (literally under (M3), by Lemma 7.5(d)), which suffices. The record is (N∖X, X∖N), with N∖X null. It is accepted because m_ω(X∖N) ≤ −η. **Repair:** say "N := D_Q with X₊ = D_Q a.e.". |
| T6 | X₊ null | CORRECT | Under (M3), D_S is non-null, so X₊ is incoherent. Thm 7.7 with K′ = {q\*} returns N = D_S (Q_∅ = S). Without (M3), D_S may be null; then X₊ = D_S a.e. is coherent and N = D_S. Both branches give the same N. CHECKED numerically (R4: X = {sup h < 0}). |
| T7 | X₊ incoherent: Thm 7.7 inside hull(X₊) is legitimate; which K′ and which domain; Step C uses q\* ∈ Q_{X₊} | CORRECT | **Cleanest choice:** K′ := {q\*}, domain U′ := D_{q\*}. X₊ ⊆ U′ **literally**, so no a.e. adjustment is needed. Thm 7.7, Step A: hull(X₊) = D_{Q_{X₊}} ⊆ U′ because q\* ∈ Q_{X₊}. Step C: the non-null gain uses k := q\* ∈ K′, with k(h) > 0 on U′. **Alternative:** K′ := Q_{X₊}, U′ := hull(X₊), using X₊ ∩ U′ (= X₊ a.e. by Lemma 7.5(b)). Any element of Q_{X₊} serves in Step C, and q\* is a canonical one. The result is N ⊆ hull(X₊) ⊆ D_{q\*} with q(m(N) − m(X₊)) ≥ v′/2 > 0 for every state q. |
| T8 | N ⊆ {q\* > 0}, so L ⊆ X∖N a.e. | CORRECT | Literal in T7, a.e. in T5. L ⊆ X and L ∩ N is null. |
| T9 | Q_L = ∅ via a state applied to a Bochner integral; no coherent model contains X∖N | CORRECT | If q ∈ Q_L, then q(m(L)) = ∫_L q(h) dμ ≥ 0, because a bounded linear functional commutes with the Bochner integral. But q(m(L)) ≤ −η < 0. Q is antitone under a.e. inclusion, so Q_{X∖N} ⊆ Q_L = ∅. If D_Q ⊇ X∖N a.e., then ∅ ≠ Q ⊆ Q_{X∖N}, which is impossible. So r(N,X) applies to no coherent model and is safe, **whatever N∖X is**. |
| T10 | Uniform total improvement | CORRECT | q(m(N) − m(X)) = q(m(N) − m(X₊)) + q(m(X₊) − m(X)) ≥ 0 + η in T5, and ≥ v′/2 + η in T6–T7, for every state q. η can be tiny (2.4·10⁻⁹ in the numerics) but is positive. |
| T11 | Strict dominance of X by N | CORRECT | r(N,X) is safe and m_ω(N) − m_ω(X) > 0, so N ⪯_ω X at every ω. N ≠ X a.e., because N is coherent and X is not. Lemma 6.1(a) then gives N ≺_ω X at every ω. |
| E1 | Protection with uncountably many worlds: the added part | CORRECT | Countable norming Ω₀ (Lemma 7.8(b)). Let r(Y,C) = (A,B) be guidance at every ω ∈ Ω₀. Off countably many null sets, h ∈ A has h > 0 on Ω₀, so inf_Ω h ≥ 0. Off the null set {P_S = 0} **(M2 with Q = S: essential, Example 7.4)**, A ⊆ D_S ⊆ C a.e. A = Y∖C misses C, so A is null. |
| E2 | Protection: the removed part | CORRECT | Off countably many null sets, h ∈ B has h < 0 on Ω₀, so sup_Ω h ≤ 0. Then q(h) ≤ sup_Ω h ≤ 0 for every state q (positivity applied to (sup h)1 − h), so P_Q(h) ≤ 0 and h ∉ D_Q = C **literally**. But B = C∖Y ⊆ C, so B is null. **No null-set assumption is used for B.** |
| **E3** | Audit sentence: "the null-boundary assumptions make these uniformly positive and **uniformly negative** a.e." | **ERROR (auxiliary sentence; theorem unaffected)** | The second half needs μ{sup_Ω h = 0} = μ(−{P_S = 0}) = 0. This is not implied by H3–H5 when null sets are not symmetric. **Counterexample (PROVED):** take E = C[0,1] and μ := μ_std + μ₀, where μ_std is as in Lemma 7.3 and μ₀ is the law of h_s := −(ω − s)², s ~ U[0,1]. Then: (M1) holds (‖h_s‖ ≤ 1); (M3) holds (from μ_std); (M2) holds for μ₀ because q(h_s) < 0 unless q = δ_s, so P_Q(h_s) = 0 forces Q = {δ_s}, a set of at most one s. But μ{sup h = 0} ≥ μ₀(E) = 1. Moreover (∅, {h_s : s ∈ [0,1]}) is a non-null record that is guidance at **every** world (h_s(ω) < 0 unless s = ω). It is harmless, since no D_Q contains any h_s. **Repair:** "…adds gambles with inf h ≥ 0 and removes gambles with sup h ≤ 0, a.e. Off the null set {P_S = 0}, the former lie in D_S, which every coherent model contains. No coherent model contains any of the latter." Then cite E1–E2. |
| E4 | (A5) on E: every non-null record that is guidance everywhere is safe | CORRECT; GAP (Lemma 7.8(c) does not transfer verbatim) | On E such a record is a.e. (A,B) with A ⊆ D_S and B ⊆ {sup h ≤ 0}, and **B may be non-null**. Lemma 7.8(c)'s "(A, ∅)" uses B ⊆ U = D_{K′}. Safety: if A is non-null, A ⊆ D_S ⊆ D_Q a.e. blocks application; if A is null and B non-null, no D_Q contains B. **Repair:** state the E-version of Lemma 7.8(c). It is needed only for the dominance characterisation (Lemma 6.1(f)). |
| E5 | (A1), (G) at each world | CORRECT | (M2) with Q = {δ_ω}. No countable reduction is needed (IW66b F2). |
| E6 | (A4), (IB), (TC), (FCC), (Add) | CORRECT | Set-theoretic (Lemma 7.1(b), 6.1(a),(e)). Domain-free. |
| S1 | Passage between sets and equivalence classes | CORRECT; GAP (state it) | Q_B, hull, m, records, guidance, safety and coherence all depend only on a.e.-classes. L and X₊ depend on the representative of X only up to null sets. The defenders are literal open sets D_{Q′}. Completion-measurable sets (e.g. coherent sets of desirable gambles, Prop. 7.16) differ from Borel sets by null sets. **Repair:** one sentence that all notions are class-invariant, and that "coherent" means "a.e. equal to some D_Q". This is a measure-relative notion (scope §5). |
| S2 | Literal (LF) on E | CORRECT | Take N = E. Every Borel X with X △ D_K ⊆ E lies in E. D_K ∈ M_E always. |
| S3 | Every coherent target D_Q (any credal Q) is covered | CORRECT | Definition "cover" (i)–(vi): (G), (IB) (E5–E6); (GC), strong (C), (ID) (T11, E1–E2, Lemma 6.1(d)); D_Q ∈ M_E and undominated by protection; (LF) by S2. **No** K_⊥ = {0}, full dimensionality, or strictly positive member of Q is needed. E is not one-sided in §7.6's sense, so Thm 7.13(c) does not apply. |
| S4 | What full support is needed for | GAP (scope sharpening) | The audit says full support is "included when … stating coverage". On E, coverage of every target needs only (M1)–(M2). (M3) is needed only for: injectivity of Q ↦ [D_Q] (uniqueness of the credal set; distinct targets are distinct models; Lemma 7.5(d)); and, in the corollaries, the one-sided (LF) characterisation (Prop. 7.12) and one-sidedness of D_{K′}. The numerics use a measure **without** full support (finitely many lines). |
| S5 | Hull convention hull(B) := E when Q_B = ∅ | CORRECT; GAP (consequence) | It agrees with D_∅ = {P_∅ > 0}, where P_∅ = +∞. But hull(B) is then no longer "the smallest coherent model containing B" (E is incoherent). The safety test reads: **safe ⟺ Q_B = ∅ or μ(A ∩ hull(B)) > 0**, not "μ(A ∩ hull(B)) > 0" alone. Example: (∅, B) with Q_B = ∅ is safe. |
| S6 | The repair theorem's clauses imply safety (for OUT67) | CORRECT (nearby result, PROVED §2.2) | If N is coherent, N ⊆ hull(X∖N) and inf_S q(m(N) − m(X)) > 0, then r(N,X) is safe. So the author's two clauses (uniform margin, N ⊆ hull(X∖N)) suffice for the ranking in **both** cases. Uniformity, i.e. positivity at every state rather than at every world, is exactly what the argument needs. |
| C1 | Finite worlds, two-sided: TS66 as E = ℝⁿ | CORRECT (contained, and extended) | With Ω = {1..n}, E = ℝⁿ and S = Δ, (M) implies (M1)–(M3) (Lemma D(b)). Hence TS66 Cor. 5.3(a) (one ranking covers every credal set on ℝⁿ) is the case E = ℝⁿ. The theorem also allows any μ with (M1)–(M2): singular to Lebesgue measure, or with atoms off the indifference sets. The audit's Q_X = ∅ construction is TS66's "alternative route" (REF66_ts row 6g); TS66's main construction is the one-minimax variant of §2.3. |
| C2 | Restricted domains: one-sided D_{K′} | CORRECT | By Lemma 7.6, safety on D_{K′} equals safety on E. So the ranking on M_{D_{K′}} is the restriction of the ranking on M_E. Every incoherent X ⊆ D_{K′} has Q_X ⊇ K′ ≠ ∅, and its defender lies in hull(X) ⊆ D_{K′}. Theorem 7.9 is therefore recovered. Coverage on D_{K′} still requires Prop. 7.12's condition (with M3), which is not automatic. |
| C3 | Restricted domains: hull-closed U (hull(B) ⊆ U a.e. whenever B ⊆ U and Q_B ≠ ∅), infinite-dimensional | CORRECT (PROVED §2.4) | Safety on U (against C_U = {D_Q ⊆ U a.e.}) equals safety on E. Both defenders lie in U, since N ⊆ hull(X) or N ⊆ hull(X₊). Protection holds on any domain. So the simple ranking on U is a universal cover: it covers K ⟺ D_K ⊆ U a.e. and (LF) at D_K, and every cover needs both. Examples: E, D_{K′}, every U ⊇ {sup h > 0}. Exact (LF) conditions on such U in infinite dimensions (analogues of TS66 Prop. 5.2) were **not** checked. |
| B1 | Break attempt: rivals containing h and −h | No counterexample | X = E, D_S ∪ (−D_S), D_K ∪ (−D_K): Q_X = ∅. For X = E, N = D_{q\*} and the record is (∅, {q\* < 0}). Numerics R1–R3 pass in both spaces. Under symmetric null sets, Q_X ≠ ∅ already forbids a non-null B with B, −B ⊆ X (q = 0 a.e. on B, and {q = 0} is null). With asymmetric null sets nothing changes, since everything is computed under μ. |
| B2 | Break attempt: Q_X = ∅ with a thinly spread sure loss | No counterexample | η > 0 comes from compactness of S and continuity of F, not from any finite sub-family. Numerics R6: three tiny pairwise-consistent bets (each pair has a common state, the triple has none) plus D_S. η reaches 2.4·10⁻⁹, the saddle identity holds to 1.5·10⁻⁹, and every check passes. |
| B3 | Break attempt: E = C(Ω), Ω uncountable | No counterexample | For Ω compact metric, C(Ω) is separable and every step applies. Uncountability enters only through (G) per world (E5) and protection via Ω₀ (E1–E2). The counterexample in E3 lives in C[0,1] and does not affect the theorem. Non-metrizable compact Ω makes C(Ω) nonseparable, which lies outside H2 (draft §9.3). |
| B4 | Break attempt: degenerate cases | No counterexample | Covered: X null (Q_X = S, N = D_S); X₊ null (T6); X₊ coherent with N ⊆ X (T5); η attained at a non-evaluation state (q\* ∈ S∖Ω̂ is allowed, since all objects are state-defined); L is never null (P5). |

**Score.** 34 items. ERROR: 1 (E3, an auxiliary sentence that the theorem does not use). GAP: 7 (T1, T5, E4, S1, S4, S5, and S6 as a recommended addition). All load-bearing steps are CORRECT.

---

## 2. Proofs supporting the verdicts (PROVED)

### 2.1 The Proposition, written out
- Let F_X = {f ∈ L∞(μ) : 0 ≤ f ≤ 1_X}, T f = ∫ f(h) h dμ ∈ E, and Z = −T(F_X). Then Z is norm-compact and convex.
- Put Φ(q,z) = q(z). By Sion,

  η := max_{z∈Z} min_{q∈S} q(z) = min_{q∈S} max_{z∈Z} q(z) = min_{q∈S} F(q), with F(q) = ∫_X q(h)⁻ dμ.

- Let z\* and q\* attain the two outer optima. F(q\*) = η > 0 by P3.
- Then η ≤ q\*(z\*) ≤ η, so f\* (with z\* = −T f\*) maximises −∫ f q\*(h) dμ over F_X. Hence f\* = 1_L a.e., using (M2) for {q\*}.
- So min_S q(−m(L)) = η.

### 2.2 Safety from the two repair clauses (for OUT67's repair theorem)

**Lemma.** Let N be coherent, N ⊆ hull(X∖N) (with hull := E when Q_{X∖N} = ∅), and inf_{q∈S} q(m(N) − m(X)) > 0. Then r(N,X) applies to no D_Q, so it is safe.

*Proof.* Suppose r(N,X) applies to D_Q: X∖N ⊆ D_Q a.e. and (N∖X) ∩ D_Q is null.
- Then ∅ ≠ Q ⊆ Q_{X∖N}, so hull(X∖N) = D_{Q_{X∖N}} ⊆ D_Q, and N ⊆ D_Q.
- Hence N∖X ⊆ D_Q ∩ (N∖X) is null, that is, N ⊆ X a.e.
- Then, for q ∈ Q: q(m(N) − m(X)) = −∫_{X∖N} q(h) dμ ≤ 0. This contradicts the margin at the state q. ∎

The margin is needed at **states**, not just worlds. By Lemma 7.1(b), "inf_Ω(m(N) − m(X)) > 0" is the same thing, so "uniform at every world" is exactly the right clause. A merely pointwise margin would not suffice for this argument.

The Lemma also yields μ(N∖X) > 0 in the consistent case: if N ⊆ X a.e. and Q_X ≠ ∅, then any k ∈ Q_X contradicts the margin. This is Step C.

### 2.3 Optional simplification of the inconsistent case: one more relaxed minimax, no shrink
- This is TS66 Thm 3.4 in the relaxed form. Let G₁ := D_{q\*}, or hull(X₊), and x := m(X).
- Run the minimax of Step B over F_{G₁} with payoff q(T f − x).
- 1_{X₊} ∈ F_{G₁}, so the value v″ ≥ min_S q(m(X₊) − m(X)) ≥ η > 0.
- The saddle point gives the indicator of N := G₁ ∩ {π\* > 0}. This N is coherent (for G₁ = D_{q\*}, N = D_{conv{q\*, π\*}}, a "two-prior" model). It satisfies N ⊆ D_{q\*} and min_S q(m(N) − m(X)) = v″ ≥ η.
- Safety follows as in T9.
- No contraction lemma, shrink or case split on whether X₊ is coherent is needed.

This matches AUDIT §3's architecture ("one minimax lemma, two uses") and is CHECKED numerically below. The audit's route via Thm 7.7 is also correct. Its only extra yield is μ(N∖X) > 0 when X₊ is incoherent.

### 2.4 Hull-closed domains (C3)
Let U be hull-closed and C_U = {D_Q : D_Q ⊆ U a.e.}. For a record (A,B) of subsets of U:
- If it is safe on E, it is safe on U (C_U ⊆ C_E).
- Conversely, suppose it applies to some D_Q. Then Q_B ≠ ∅, and it applies to hull(B), which lies in U a.e. So hull(B) ∈ C_U.

Defenders:
- Q_X ≠ ∅: N ⊆ hull(X) ⊆ U a.e.
- Q_X = ∅: N ⊆ hull(X₊) ⊆ U a.e., since X₊ ⊆ U and q\* ∈ Q_{X₊}. With the §2.3 variant, take G₁ = hull(X₊).

Replace N by N ∩ U. Protection holds on every domain (E1–E2). Lemma 6.1 then gives undominated = C_U. (LF) at D_K ⟺ some open O ⊇ ∂D_K∖{0} has O ⊆ U a.e. (test the model D_K ∪ O). Neither direction needs (M3). ∎

## 3. Numerics (`rf67a_py/fulldomain_check.py` → `fulldomain_check.out`; NUMERICS)

**Setting.**
- dim E = 3, E = {g + t1}, with two world sets:
  - (A) Ω = 3 worlds, E = ℝ³, states Δ;
  - (B) Ω = a 201-point grid in [0,1], E = span{1, ω, ω²}, a curved state polygon with 201 extreme states.
- μ = Σ_k w_k law(g_k + t1), t ~ N(0,1), on 40–43 lines (Lemma 7.3 with atomic ν). This μ satisfies (M1)–(M2), is singular to Lebesgue measure, and has **no full support**.
- On each line every D_Q is a half-line, so all masses, moments and hulls are closed form.
- Q-sets are polygons, computed by clipping. Emptiness is certified by an LP slack.

**For each rival with Q_X = ∅, the script checks:**
- η > 0;
- the saddle identity max_ω m(L)(ω) = −η;
- q\* ∈ Q_{X₊};
- the defender, by the audit route (N = X₊, or Thm 7.7 in hull(X₊) with the shrink) **and** by the one-minimax route of §2.3;
- N ⊆ {q\* > 0} and L ⊆ X∖N;
- Q_{X∖N} = ∅;
- hull invariance in Thm 7.7;
- total margin ≥ η.

**Rivals.**
- R1 X = E; R2 D_S ∪ −D_S; R3 D_K ∪ −D_K; R4 {sup h < 0}; R5 E∖D_S.
- R6 thin pairwise-consistent bets plus D_S, at three scales.
- R7 12 random rivals per space.
- C0–C3 unions of two precise models with holes (these turn out to have Q_X = ∅).
- D0–D3 controls with Q_X ≠ ∅ (D_{K₁} ∪ D_{K₂} with K₁ ∩ K₂ ≠ ∅, with holes), run through Thm 7.7 directly.

**Results.**
- **56/56 OK**: 48 rivals with Q_X = ∅ (R1–R7 and C0–C3, in both spaces) and 8 with Q_X ≠ ∅ (D0–D3, in both spaces).
- The one-minimax route passed 48/48.
- Smallest η: 2.4·10⁻⁹. Largest |max_ω m(L)(ω) + η|: 1.5·10⁻⁹.
- X₊ was coherent in 3 rivals. X₊ was null in R4, where the defender was D_S.

These computations illustrate the theorem; the verdict rests on the proofs.

## 4. Requested repairs (ranked)

1. **(E3, ERROR in an auxiliary sentence.)** Replace "uniformly positive and uniformly negative a.e." with the E1–E2 argument. The added part lies in D_S off {P_S = 0}. The removed part has sup h ≤ 0, and no D_Q contains such h. Do not assume μ{sup h = 0} = 0 (counterexample in E3).
2. **(T1, T7.)** Name the auxiliary domain: K′ = {q₀} with q₀ ∈ Q_X (consistent case), and K′ = {q\*}, U′ = D_{q\*} (inconsistent case). Say that Step C uses k = q\*.
3. **(S4.)** State that coverage on E needs only (M1)–(M2), and that (M3) only identifies distinct credal sets with distinct models.
4. **(E4.)** State the E-version of "guidance at every world": a.e. (A,B) with A ⊆ D_S and B ⊆ {sup h ≤ 0}. B can be non-null on E.
5. **(T5, S1, S5.)** For X₊ coherent, take N = D_Q. Add a one-line class-invariance remark. With hull(∅-supported) = E, write the safety test as "Q_B = ∅ or μ(A ∩ hull B) > 0".
6. **(S6, optional.)** State the repair theorem with its two clauses and derive safety by §2.2's lemma, so that the ranking corollary is one line.
7. **(Optional.)** Use the one-minimax variant (§2.3) for the inconsistent case.
8. **(Scope.)** As in REF66_iw: dominance in general is pointwise, not uniform; only the repair N is uniform. "1 ∈ E" means "some e ∈ E with inf_Ω e > 0", not an abstract order unit.

## 5. Files (`rf67a_py/`)
| File | Content | Label |
|---|---|---|
| `fulldomain_check.py` / `.out` | Proposition and full-domain repair on lines measures in ℝ³ and in span{1,ω,ω²} with 201 worlds; 56 rivals; audit route and one-minimax route | NUMERICS |
