# REF66_ts — referee report on TS66 (universal coverage on two-sided domains) (26 Oct 2026)

Referee: REF66_ts. Object of review: `TS66_notes.md` and `ts66py/`. Labels: PROVED (re-derived by the referee) / CHECKED (exact rational computation) / NUMERICS / CONJECTURE. Scripts: `ref66ts_py/` (run each with `python3 -I <script>` from that folder; each writes a `.out` file). The exact engine `poly3.py` is written from scratch and shares no code with `ts66py/geo3.py`; it agrees with geo3 exactly on 300 random cones (`check_engine.out`).

## Verdict at the top

**The main claim holds.** I re-derived every step and found no mathematical error. Precisely:

> **Theorem (TS66 Cor 5.3(a); referee-verified).** Let Ω be finite (n ≥ 2), let μ satisfy (M) (finite Borel measure on ℝⁿ with the null sets of Lebesgue measure and ∫|h| dμ < ∞), let U = ℝⁿ, let models be measurable subsets of ℝⁿ modulo null sets, and let the coherent models be the D_Q (a.e.) for **every** credal set Q (nonempty, closed, convex Q ⊆ Δ: boundary, lower-dimensional and precise Q included). Define safety as "applies to (attacks) no coherent model" and take the simple ranking: X ⪯_ω Y iff r(X,Y) is guidance at ω, or r(X,Y) is safe and m_ω(X) − m_ω(Y) > 0. Then this one ranking covers every credal set K, in the sense of the binding Definition "cover" (Definition "cover" of the covering paper and of the universal note), and satisfies (W), (Add), (FCC) and strong (C) as well.

More generally (TS66 Thm 4.1, Cor 5.3), on every **hull-closed** domain U the same ranking covers exactly the K with D_K ⊆ U a.e. and (LF) at D_K, so it is a universal cover there. ℝⁿ, V₀ = ℝⁿ∖(−ℝⁿ₊), every U between them, every one-sided D_{K′}, every D_{K′} ∪ (sure losses), and (n = 2) every domain admitting a (G)+(GC) ranking are hull-closed.

**Hypotheses actually used.** (M) (only: μ ≪ Lebesgue and Lebesgue ≪ μ on open sets, finiteness, first moment); finitely many worlds; hull-closedness of U (only for Case 1/Case 2 to keep the defender inside U, and for the "⇒" half of the safety test). Not used: any K′, any relint condition, pointedness, dimension of Q_X, continuity of the density.

**What "completes the finite-world programme" means, exactly.** It settles existence: every credal set is coverable, and by a single ranking on ℝⁿ. It does **not** settle universality on domains that are not hull-closed (TS66 §7.1, correctly marked OPEN), and it does not change the scope caveat that the ranking is coherence-informed (it refers to the coherent class through "safe"). It also falsifies the covering paper's open-problem-(4) conjecture (already falsified by round 65 on one-sided domains); that was a conjecture, not a refereed result, so nothing refereed is contradicted.

**Two independent confirmations (CHECKED).**
- The Case-2 construction (Lemma E + one relative minimax, no shrink) and the Case-1 construction (round-65 with K′ → Q_X) were re-implemented independently and certified exactly, under **two different measures** (TS66's density e^{−|h|₁} and the independent density e^{−|h|∞}), on every rival that the runs reached before they were stopped on the lead's instruction: 13 of TS66's 30 Case-2 rivals, its 2 lifted rivals, 9 new Case-2 rivals, and all 16 new Case-1 rivals. No failure occurred. Results: §3. These computations illustrate the result; the verdict rests on the proofs (§1–§2).
- TS66's two "obvious fix is unsafe" examples are reproduced exactly at the Brier-minimax prior, with an explicit attacked coherent model. Unsafety is stable within 10⁻⁴ of the minimax prior (25/25 exact grid priors at radii 10⁻⁶, 10⁻⁵, 10⁻⁴ for both rivals), while the minimax prior is located to within about 2·10⁻⁸. It is **not** stable at radius 10⁻² (and for lift L2 not at 10⁻³): nearby Brier-dominating half-spaces can be safe. §3.3.

**Gaps (none affects the main claim).** Eight GAPs, all expository or scope; repairs in the table. The most substantive:
- G5: Prop 3.2(c)'s "U ∪ (−U) is not hull-closed" is true for FD62's witness K′ but **false for K′ = Δ** (then U ∪ −U = int ℝⁿ₊ ∪ −int ℝⁿ₊, which is hull-closed by Prop 3.2(b)) and for singleton K′ (a.e. ℝⁿ). Scope the sentence to the witness.
- G2: Lemma E's "moreover" (λ* a minimiser) is not needed: Thm 3.4 works with *any* λ with m(X ∩ {λ·h<0}) ≪ 0, with margin ≥ min_i(−m_i(X ∩ {λ·h<0})). Worth saying; it simplifies the statement and the computations.
- G3: Thm 3.4 should say explicitly that X₁ may be null (then G₁ = hull(∅) = int ℝⁿ₊ and N = int ℝⁿ₊), and that A = N∖X may be null (then the record is (∅, X∖N), safe because Q_{X∖N} = ∅). Both cases are covered by the proof as written (N∖X null is CHECKED on T1, T2, T6, T9, T10, B1, B1b).

---

## 1. Verdict table

| # | Item (brief's check list) | Verdict | Note / repair |
|---|---|---|---|
| 1a | Setting: models on ℝⁿ, coherent = D_Q a.e. for any credal Q, strict (G) | CORRECT | Exactly the covering paper's §2 definitions with U = ℝⁿ ("the full domain"). Q is unique (covering paper Lemma "open"). No requirement of the binding framework mentions K′ or one-sidedness; (G), (IB), (TC), (GC), (C), (ID), (LF), (W), (Add) all carry over verbatim. On ℝⁿ, (LF) holds trivially with N = ℝⁿ. |
| 1b | 𝒞_U on a domain U | CORRECT | 𝒞_U := {D_Q : D_Q ⊆ U a.e.}. On U ⊇ V₀ this is every D_Q (D_Q ⊆ V₀). |
| 2a | Safety test: safe ⟺ Q_B = ∅ or μ(A ∩ hull B) > 0 (Lemma 2.2) | CORRECT | "⇐" holds on every domain (if D_Q ⊇ B a.e. then Q ⊆ Q_B, so D_Q ⊇ hull B; and Q_B = ∅ means no D_Q contains B). "⇒" needs hull(B) ∈ 𝒞_U, i.e. hull-closedness. Agrees with SR66 S1's scope note. An attack-search comparison was written (`ref_misc.py` (e)) but stopped before completing; not needed for the verdict. |
| 2b | Q_B = ∅: every record with removed part B is safe | CORRECT | Vacuous: no D_Q contains B a.e. (if it did, Q ⊆ Q_B). Includes A null: (∅, B) is safe and is accepted at ω iff m_ω(B) < 0. |
| 2c | Special cases B null / Q_B = Δ | CORRECT | Q_B = Δ ⟺ B ⊆ ℝⁿ₊ a.e. (TS66 says "whenever B ⊆ int ℝⁿ₊"; "iff B ⊆ ℝⁿ₊ a.e." is the sharp form — cosmetic). |
| 2d | The D_∅ := ℝⁿ reformulation | CORRECT | With that convention: safe ⟺ μ(A ∩ hull B) > 0, or (A null and Q_B = ∅). Note hull(B) = cone(B_d) + int ℝⁿ₊ is ℝⁿ exactly when Q_B = ∅, so the convention is the hull formula's own value. |
| 3 | Protection is free on every domain (Lemma 2.3) | CORRECT | Uses only: every D_Q ⊇ int ℝⁿ₊, no D_Q contains h ≪ 0, and r(Y,C) applies to C. Holds for every Q incl. boundary and precise. (The planned random check `ref_misc.py` (c) was stopped before completing.) |
| 4a | Lemma E (i)⟺(ii) | CORRECT | F(λ) = ∫_X(λ·h)⁻ is 1-Lipschitz in λ w.r.t. ∫|h|; its zero set is Q_X. |
| 4b | Lemma E (ii)⟹(iii) and "moreover": minimax | CORRECT | Saddle points of a zero-sum game form the product of the optimal sets, so the "moreover" holds for **every** minimiser λ* and (as a by-product) the maximin z* is unique. Uniqueness of the maximiser of λ*·m(Y) over Y ⊆ X uses only that {λ*·h = 0} is null (λ* ≠ 0). |
| 4c | Ordinary subsets vs relaxed choices; where Lyapunov is used | CORRECT (with an optional simplification) | Lyapunov (μ non-atomic, ∫|h| < ∞) makes M_X = {m(Y): Y ⊆ X} compact and convex, which the minimax needs; ordinary subsets suffice. Lyapunov is dispensable: run the minimax over relaxed f ∈ [0, 1_X] (range is trivially compact convex) and note that the optimal relaxed choice against λ* is the indicator of X ∩ {λ*·h>0} by the same uniqueness argument. This is the version that transfers to the infinite-world setting (TS66 §7.2). |
| 4d | (iii)⟹(iv)⟹(i); null sets | CORRECT | (iv)⟹(i) is one line (q·m(L) ≥ 0 for q ∈ Q_B, < 0 for m(L) ≪ 0). Null sets used: hyperplanes {λ·h=0}; {P_Q = 0}; −ℝⁿ₊ ∖ −int ℝⁿ₊. Both directions are also illustrated on every Case-2 rival in §3.1 (polygon-clipping Q_X = ∅ and an exact m(L) ≪ 0 certificate agree). |
| 4e | Lemma 2.1(c): Q_B = ∅ ⟺ sure-loss combination of ≤ n density points | CORRECT | Separation of the convex cone cone(B_d) from the open cone −int ℝⁿ₊; the normal is ≥ 0. Conic Carathéodory gives r ≤ n directly (the "−𝟙 − p" detour is unnecessary). |
| 5a | Case 1 (Q_X ≠ ∅) on ℝⁿ, Step 1 | CORRECT | The note's Step 1 uses only Q_X ≠ ∅, Lyapunov on G = D_{Q_X}, and uniqueness; G ∩ {λ·h>0} = D_{conv(Q_X ∪ {λ})} is coherent for every λ ∈ Δ. |
| 5b | **Step 2 (non-null gain) with k ∈ Q_X** | CORRECT | k·h ≥ 0 for a.e. h ∈ X (definition of Q_X), so k·(m(N₀) − m(X)) = −∫_{X∖N₀} k·h ≤ 0 if N₀∖X were null, contradicting m(N₀) − m(X) ≫ 0 and k ∈ Δ. The one-sided proof used the strict k·h > 0 on U only to get ≥ 0; ≥ 0 a.e. on X is all that is needed. |
| 5c | Step 3 (shrink), contraction lemma, Prop "shrink" | CORRECT | They use only Q_X nonempty, closed, convex and P_{Q_X} ≥ 0 a.e. on X. Holds for Q_X = {e₁}, Q_X an edge segment, Q_X precise on ∂Δ, Q_X = Δ. CHECKED: 16 Case-1 rivals × 2 measures (`ref_case1.out`, `ref_case1b.out`). |
| 5d | Case 1 requires hull(X) ⊆ U | CORRECT | Needed only to keep N in 𝓜_U; automatic on U ⊇ V₀. |
| 6a | Case 2: relative minimax inside hull(X₁) | CORRECT | M_{G₁} is compact convex (Lyapunov); m(X₁) ∈ M_{G₁} because X₁ ⊆ G₁ a.e.; v′ ≥ min_i(m(X₁) − m(X))_i ≥ v_X > 0; saddle point gives the unique maximiser G₁ ∩ {π*·h>0}. X need not lie in G₁. |
| 6b | N ⊆ {λ*·h>0} | CORRECT | λ* ∈ Q_{X₁} (λ*·h > 0 on X₁), so G₁ = D_{Q_{X₁}} ⊆ D_{{λ*}}. |
| 6c | Removed part has empty hull, record safe | CORRECT | L := X ∩ {λ*·h<0} is disjoint from N, so L ⊆ X∖N; Q is antitone, so Q_{X∖N} ⊆ Q_L = ∅ (m(L) ≪ 0, Lemma 2.1(d)). Safety by 2b. CHECKED with two independent certificates (polygon clipping, and m(L) ≪ 0 with L ⊆ X∖N a.e.). |
| 6d | Strict margin at every world | CORRECT | m(N) − m(X) ≥ v′𝟙 ≥ v_X𝟙. The reverse record has negative increments and is not guidance, so N ≺_ω X at every ω. |
| 6e | X₁ coherent | CORRECT | Then G₁ = X₁ a.e. and N = X₁ ∩ {π*·h>0}; possibly N = X₁, giving the record (∅, X∖X₁), safe with Q = ∅. CHECKED (T1, T2, T5, T6, T9, T10, B1, B1b). |
| 6f | X₁ null | CORRECT, **GAP (expository)** | Covered by the proof with Q_∅ = Δ: G₁ = int ℝⁿ₊, N = int ℝⁿ₊ (e.g. X = −int ℝⁿ₊: m(N) − m(X) ≫ 0, record (int ℝⁿ₊, X) safe since Q_X = ∅). Say so (G3). PROVED; the computed instances B5a–b were not reached. |
| 6g | Remark: G₁ := {λ*·h>0} on full domains; alternative route via Thm 3.3 on X₁ | CORRECT | Both certified by TS66; the first gives the "two-prior" defender D_{[λ*,π*]}. |
| 6h | Lemma E's "moreover" needed? | **GAP (simplification)** | No: any λ with m(X ∩ {λ·h<0}) ≪ 0 works, with margin ≥ min_i(−m(X ∩ {λ·h<0}))_i (G2). My checks use non-optimal certified λ throughout. |
| 7a | Def 3.1 hull-closed; Prop 3.2(a) equivalence with "traces of coherent models are coherent" | CORRECT | Both directions re-derived. Note: hull-closedness applied to B = ∅ forces int ℝⁿ₊ ⊆ U a.e.; both sides of (a) are false/vacuous together when U ⊉ int ℝⁿ₊. |
| 7b | Examples: ℝⁿ, V₀ and every U ⊇ V₀; D_{K′}; D_{K′} ∪ E; n = 2 sectors | CORRECT | D_Q ⊆ V₀; D_{K′} ∩ D_Q = D_{conv(K′∪Q)}; Q_B ≠ ∅ forces B ∩ (−ℝⁿ₊) null; n = 2 sector intersections re-derived (sectors (γ,δ), −π/2 ≤ γ ≤ 0, π/2 ≤ δ ≤ π, δ − γ ≤ π). |
| 7c | Prop 3.2(d): n = 2 domains with (G)+(GC) are sector + sure losses | CORRECT | B₁ = (γ₁, π/2), B₂ = (0, δ₂) are forced; union (γ₁, δ₂). So for n = 2, (G)+(GC) ⇒ hull-closed (PROVED), and the simple ranking is a universal cover on every n = 2 domain that admits any cover. |
| 7d | A_K not hull-closed | CORRECT | Checked by hand (and CHECKED in FD62/REF62): balls of sup-radius ½ around x = (1,−1,−20) and y = (1,4,−1) lie in A_K ∩ {h₁>0}; v₁·(x+y) = −5/3 with two positive coordinates, so a ball around x+y lies outside A_K. (`ref_misc.py` (a) was stopped before completing.) |
| 7e | U ∪ (−U) not hull-closed | CORRECT for FD62's witness; **GAP (scope)** | Checked by hand for K′ = conv{(.4,.3,.3),(.3,.4,.3)}: k₀·x = 2.015, k₁·x = 1.605; k₀·y = −1.57, k₁·y = −1.76; k₀·(x+y) = 0.445 > 0 > −0.155 = k₁·(x+y), with strict margins (REF62 CHECKED the same witness). False for K′ = Δ (U ∪ −U = int ℝⁿ₊ ∪ −int ℝⁿ₊ is hull-closed by Prop 3.2(b)) and for singleton K′ (a.e. ℝⁿ). Repair (G5): "for FD62's witness K′ (in particular not for K′ = Δ or a singleton)". |
| 8 | Ranking properties on hull-closed U: (G), (IB), (TC), (FCC), (Add), (GC), (C), (ID), (W) | CORRECT | Same proofs as SR66 P1–P8; no step uses one-sidedness. Safety is upward closed under ⊔ on every domain (set-theoretic attack). Every accepted non-null record has d_ω > 0, so ties are trivial and (C) holds in the strong form. "(TC) via the deletion lemma": cite the comparison-deletion note's Lemma "deletion", or (simpler) the direct potential argument of the new draft's Prop "structure"(d). |
| 9a | (LF) on ℝⁿ: every credal set, incl. boundary, precise, edge and vertex targets | CORRECT | (LF) holds with N = ℝⁿ; D_K ∈ 𝓜_{ℝⁿ}; D_K coherent ⇒ undominated. K = {e₁} (D_K = {h₁>0}), K = [e₁,e₂], K = {(½,½,0)}, K = Δ (D_K = int ℝⁿ₊) all covered. |
| 9b | Lemma 5.1, Prop 5.2 (LF on U = V₀ ∪ E) | CORRECT | ∂D_K = {P_K = 0}; on −ℝⁿ₊, P_K(h) = 0 ⟺ h vanishes on S_K. So ∂D_K∖{0} = (∂D_K ∩ V₀) ∪ F_K, with V₀ open. F_K = ∅ ⟺ S_K = Ω ⟺ K ∩ relint Δ ≠ ∅. |
| 9c | On V₀: exactly the K meeting relint Δ; n = 3 no-edge targets pass; n ≥ 4 two-face example fails on V₀, passes on ℝⁿ | CORRECT | n = 4, K = {(⅓,⅓,⅓,0)}: F_K = ray −e₄, and every neighbourhood of −e₄ contains a non-null set of sure losses. Consistent with FD-1: K meets no edge, so every covering domain is ⊇ V₀ and must also contain sure losses near −e₄. |
| 9d | Cor 5.3(d), n = 2 sector criterion | CORRECT | D_K = (φ₂ − π/2, φ₁ + π/2); with E null, (LF) ⟺ α < φ₂ − π/2 and φ₁ + π/2 < β. TS66 correctly notes that a non-null E helps only at the rays −π/2 and π (K touching a vertex). |
| 10 | Plain Brier on ℝⁿ covers exactly {p}, p ∈ Δ | CORRECT | Undominated = Pareto-maximal points of the Lyapunov range = unique maximisers of q·m = D_{{q}}, q ∈ Δ (including q ∈ ∂Δ); Brier is complete and transitive, so (GC) ⇒ (C); (LF) trivial. The covering paper's Cor. "precise" (p ∈ relint Δ) is correct and **understated** on ℝⁿ, exact on V₀. Citation slip: TS66 cites the note's Remark "H"(c); in the current draft it is Remark "H"(d) (G1). |
| 11 | Consistency with FD-1 (Thm 2.9), Prop 2.10 (lowdim), Cor precise, REF62 Thm R1 | CONSISTENT | ℝⁿ and V₀ are FD-1 branch (b); D_{K′} is branch (a); lower-dimensional K are covered only on non-essentially-one-sided U (Prop lowdim). Thm R1 / Cor "chartrigid" concern chart certificates; the simple ranking is incomplete, intransitive and not a chart ranking, so they do not apply (the covering paper's §8 scope paragraph says exactly this). The FD-1 reconciliation sentence should carry FD-1's hypotheses (n ≥ 3, K meets no edge, D_K ⊆ U a.e.) wherever "necessity of hull-closedness" is claimed (G6). |
| 12 | Adversarial attempts | **No counterexample** | §3: spread-thin sure losses (margins down to 10⁻¹⁰), rivals coherent on one half-space and wild on the other, the lifted rivals (v_Y ≈ 10⁻⁸), Q_X on ∂Δ / lower-dimensional / = Δ. Every case reached was certified under both measures. The boundary-direction (B3) and pure-sure-loss (B5) rivals were written but not reached before the runs were stopped; they are covered by the proof (rows 6e–6f). The two naive-unsafe lifts are re-verified exactly at the minimax prior (§3.3). |
| 13 | §7.2 infinite-world two-sided sketch | CONJECTURE (correctly labelled) | Plausible; the relaxed-choice form of Lemma E (row 4c) is the right tool. Not refereed further. |
| 14 | §7.1 "hull-closedness necessary for (GC)+(ID) under (G)" | CONJECTURE, correctly labelled; the PROVED parts are correct (n = 2; n ≥ 3 two-sided branch of FD-1 under FD-1's hypotheses) | (G6) |

---

## 2. Notes on the checks

### 2.1 Setting (check 1)

The binding framework is stated for an arbitrary measurable domain U (covering paper §2.2, "The full domain is U = ℝⁿ"). Coherence is global (D_Q with Q any credal set). Nothing in Definitions "dom", "cover" or the requirement list refers to K′ or to one-sidedness, so the framework carries over unchanged. On ℝⁿ:
- 𝒞 = {D_Q : Q credal}, every member contains int ℝⁿ₊ and no h ≪ 0;
- (LF) is satisfied by N = ℝⁿ for every K, so the coverage question on ℝⁿ reduces to "every coherent model undominated, every incoherent model dominated by an undominated coherent model, plus (G), (IB), (GC), (C)".

The two-sided novelty is exactly Q_X = ∅ (Lemma 2.1(c), Lemma E). Rivals with Q_X ≠ ∅ cannot contain non-null sets of sure losses, so they live in V₀ and behave as in round 65 with K′ replaced by any point of Q_X.

### 2.2 The two cases (checks 4–6), re-derived

*Case 1 (Q_X ≠ ∅).* The note's Theorem H goes through with three changes, exactly as TS66 says. The only place where strictness was used in round 65 is not needed: Step 2 needs k·h ≥ 0 a.e. on X, which is the definition of k ∈ Q_X. The contraction lemma and the hull-preserving shrink use only that Q_X is nonempty, closed and convex.

*Case 2 (Q_X = ∅).* The proof is short and correct. Two simplifications are worth recording:
1. **Any certified λ works.** If m(X ∩ {λ·h<0}) ≪ 0 for some λ ∈ Δ, put X₁ := X ∩ {λ·h>0}; then λ ∈ Q_{X₁}, m(X₁) − m(X) = −m(X ∩ {λ·h<0}) ≫ 0, and the relative minimax in hull(X₁) (or in the half-space {λ·h>0}) gives N with m(N) − m(X) ≥ min_i(−m_i(X ∩ {λ·h<0}))·𝟙. Optimality of λ is irrelevant.
2. **Mechanism in one line.** N ⊆ {λ·h>0}, so the change removes all of X ∩ {λ·h<0}, a set whose Brier moment is a sure loss; no coherent model can contain it, so no coherent model can undergo the change.

### 2.3 Hull-closed domains (check 7)

Prop 3.2(a) is a clean characterisation: on U, "the smallest coherent model containing B" lies inside U for every B with Q_B ≠ ∅ ⟺ U ∩ D_Q is coherent for every Q. Its role is precise: it is what makes the safety test computable (Lemma 2.2 "⇒") and what keeps both defenders inside U. Protection (Lemma 2.3) does not need it.

Scope correction for U ∪ (−U) (G5): with K′ = Δ, U ∪ −U = int ℝⁿ₊ ∪ −int ℝⁿ₊, which is of the form D_{K′} ∪ E and hence hull-closed. (It is also essentially one-sided, so it is FD-1 branch (a) and is not one of the "two-sided" domains FD-1a excludes; nothing refereed is affected.)

### 2.4 Coverage (checks 9–11)

Cor 5.3 is correct. The cleanest statement of the result is:

> On every hull-closed U, the simple ranking covers K ⟺ D_K ⊆ U a.e. and (LF) holds at D_K ⟺ some ranking on 𝓜_U covers K. On ℝⁿ this is every credal set; on V₀ it is exactly the credal sets meeting relint Δ; on D_{K′} it is exactly the full-dimensional K with K′ ⊆ relint K.

Plain Brier on ℝⁿ is the other extreme: it covers exactly the precise sets {p}, p ∈ Δ, because its undominated class is exactly the precise models. The simple ranking is a sub-relation of Brier (every accepted comparison is a strict Brier improvement at its world), so it keeps more models undominated: all coherent ones.

---

## 3. Computations (`ref66ts_py/`)

All conclusions are verified in exact rational arithmetic; floats are used only to find priors, and every prior is re-certified exactly. Every model is a finite disjoint union of open polyhedral cones in ℝ³. Measures: **L1** = density e^{−|h|₁} (TS66's), and **Linf** = density e^{−|h|∞} (independent; satisfies (M)). For a polytope unit ball B, μ(C) = 3!·vol(C ∩ B) and m(C) = 4!·∫_{C∩B} h dh for every cone C.

### 3.0 Engine (`check_engine.py` → `check_engine.out`)
- 300 random cones: mass and first moment agree **exactly** with geo3 (0 disagreements).
- 272 non-null cones: the Q polygons agree exactly (my generators are the vertices of C ∩ B, geo3's are pairwise cross products).
- Known values: μ(ℝ³) = 8 (L1), 48 (Linf); half-spaces have half the mass; m(ℝ³) = 0.

### 3.1 Case 2 (`ref_case2.py`; partial logs)
**Status: stopped on the lead's instruction before completion.** Logs: `ref_case2_ts66_part1.log` (first run, TS66 rivals T1–Rand2), `ref_case2_new.log` (lifts and new rivals), `ref_case2_ts66_from13.log` (one line: Rand3 under L1 hit the 600 s per-case limit of the float prior search). No `.out` summary was written. Reached and certified, **under both measures, with no failure**:
- TS66 T1–T10 and Rand0–Rand2 (13 of its 30 rivals). Rand3 timed out in the prior search (L1); Rand4–Rand19 were not reached.
- TS66's two lifted rivals (margins 1.4·10⁻⁴ and 1.1·10⁻⁴ under L1).
- New: B1 (int ℝ³₊ plus three thin cones whose directions sum to −δ𝟙, δ = 1/10, 1/50, 1/200; every two cones plus int ℝ³₊ are coherent; certified margins down to 1.2·10⁻¹⁰), B1b (reversed-triangle D_K plus such cones), B2 k = 0, 1, 2 (D_K ∩ {π·h>0} plus random cones below {π·h=0}) under both measures, and B2 k = 3 under L1. B2 k = 4, 5, B3a–f and B5a–d were not reached.

For each certified case, all of the following hold exactly: Q_X = ∅ (clipping); a rational λ with m(X ∩ {λ·h<0}) ≪ 0 (often not the minimiser, illustrating G2); λ ∈ Q_{X₁}; N = hull(X₁) ∩ {π·h>0} with m(N) − m(X) ≫ 0; N ∩ {λ·h<0} null; L ⊆ X∖N a.e. with m(L) ≪ 0; Q_{X∖N} = ∅ by clipping; record safe. Priors λ and π on ∂Δ occurred (Rand1, B1, B2 k = 2) and are handled.

### 3.2 Case 1 on ℝ³ (`ref_case1.py` → `ref_case1.out`; `ref_case1b.py` → `ref_case1b.out`)
16 rivals with Q_X ≠ ∅ that cannot occur on a one-sided domain with K′ ⊆ relint Δ: Q_X = {e₁} (C1), the edge [e₁,e₂] (C2), the boundary point (½,½,0) (C3), Q_X = Δ (C4), Q_X = {e₁} from two edge Bayes acts (C5), precise interior (C6), an edge-midpoint segment (C7), a segment ending at e₂ (C8), and 8 random rivals built on boundary priors. For each: X ⊆ hull(X) a.e., X incoherent, m(N_τ) − m(X) ≫ 0, μ(N_τ∖X) > 0, **Q_{X∖N_τ} = Q_X** (exact polygon equality), safe record with witness mass = μ(N_τ∖X).
- Linf: 16/16 certified. L1: 15/16; the failure (C1) is a **search failure** of the float prior search (the hole has mass ≈ 8·10⁻⁶), not a counterexample; with holes of size ε = ½, ⅓ the same rival is certified under both measures (`ref_case1b.out`).
- Control: in these rivals the unshrunk N₀ happened to be safe (REF65_hA found 2/25 unsafe on one-sided rivals; the shrink is still needed in general).

### 3.3 The two "obvious fix is unsafe" examples (`regen_lifts.py`, `ref_naive.py` → `ref_naive.out`)
Regeneration (`regen_lifts.py`): TS66's base rivals are iterations 39 and 99 of its seed-5 sequence; the lifts add thin cones around s = (−4/3, 7/3, 1) and (5/2, 1, −5) with ε = 1/200, giving 7 and 5 pieces, as TS66 reports. Q_Y = ∅ exactly, and Lemma-E certificates exist (m(Y ∩ {λ·h<0}) ≈ −4·10⁻⁸𝟙 and ≈ −(3, 0.8, 6)·10⁻⁹, exactly ≪ 0). The sure loss is very thin.

*At the minimax prior (`ref_naive2.out`, `ref_naive3.out`).* The dual π ↦ π·(m({π·h>0}) − m(Y)) is smooth with Hessian eigenvalues ≥ 4.7 on aff Δ. Its float minimisers are π* ≈ (0.5065498, 0.2791752, 0.2142750) (L1 lift) and (0.3668248, 0.4537478, 0.1794274) (L2 lift), matching TS66's 4-digit values; the dual gap ≈ 10⁻¹⁵ gives |π − π*| ≲ 2·10⁻⁸ (NUMERICS). At TS66's rationals and at the 10⁻⁸ roundings, exactly: m(N₀) − m(Y) ≫ 0 (min margin 0.051 and 0.065); B = Y∖N₀ ⊆ D_{Q_B} a.e.; μ((N₀∖Y) ∩ D_{Q_B}) = 0. So the record **attacks the coherent model D_{Q_B}** and is unsafe. The sure-loss cone E lies inside N₀ in both: the naive defender keeps the part that creates the incoherence and removes part of the base rival, whose hull is nonempty.

*Robustness (exact at grid points).* Radii 10⁻⁶, 10⁻⁵, 10⁻⁴: 25/25 unsafe for both lifts. Radius 10⁻³ (step 5·10⁻⁴): L1 24/24, L2 16/24. Radius 10⁻²: L1 9/13, L2 8/18 (the others are safe Brier-dominating half-spaces). For L2 an extreme ray g of a piece of Y has |π*·g|/|g|₁ = 3.98·10⁻⁴; this matches the distance from π* to the safe region.

*Crude prior (`ref_naive.out`).* The smallest-denominator certified prior gives a uniformly Brier-dominating half-space that is unsafe for L1 (π = (1/2, 2/7, 3/14)) but **safe** for L2 (π = (3/8, 4/9, 13/72), witness mass 0.27). Whether a Brier-dominating half-space is safe depends on the prior. That file's final line, "NO", refers only to this crude prior, not to TS66's claim.

*Verdict on TS66 §6.2:* CORRECT. Wording repair (G8): say that the minimax half-space is unsafe, that unsafety persists within 10⁻⁴ of the minimax prior, and that it is not stable at the 10⁻² scale.

### 3.4 Smaller checks (`ref_misc.py`; stopped, no output)
`ref_misc.py` (A_K and U ∪ −U witnesses; protection on random records; Lemma E both directions; safety test against an attack search) was **stopped on the lead's instruction before it wrote any output**; it prints only at the end. Its items are short proofs that I re-derived by hand (rows 2a, 3, 4d, 7d, 7e). The two domain witnesses were checked by hand (rows 7d–7e) and were CHECKED independently in FD62 and REF62.

### 3.5 What was not computed
Prop 3.2(a)–(d), Lemma 5.1, Prop 5.2 and Cor 5.3 are short proofs; I re-derived them by hand (§1) and checked only the A_K and U ∪ −U witnesses by computer. Higher n was not computed; the proofs are dimension-free.

---

## 4. Repairs requested

| # | Where | Repair |
|---|---|---|
| G1 | §5 "Plain Brier", bullet 1 | "the note's Remark 'H'(c)" → Remark "H"(d) (the current draft's numbering). |
| G2 | Lemma E / Thm 3.4 | Add: "Any λ ∈ Δ with m(X ∩ {λ·h<0}) ≪ 0 can replace λ*; the margin is then at least min_i(−m_i(X ∩ {λ·h<0}))." Keep the "moreover" as a remark (it holds for every minimiser, by the product structure of saddle points). |
| G3 | Thm 3.4 | Add the degenerate cases: X₁ null (G₁ = int ℝⁿ₊, N = int ℝⁿ₊) and N∖X null (record (∅, X∖N), safe since Q_{X∖N} = ∅, accepted since m(X∖N) ≪ 0). |
| G4 | Lemma 2.2, special cases | "Q_B = Δ also happens whenever B ⊆ int ℝⁿ₊" → "Q_B = Δ ⟺ B ⊆ ℝⁿ₊ a.e." (cosmetic). Lemma 2.2 refers forward to Def. 3.1; move the definition up. |
| G5 | Prop 3.2(c), status row 5 | Scope "U ∪ (−U) is not hull-closed" to FD62's witness K′; note that it is hull-closed for K′ = Δ and (a.e.) for singleton K′. |
| G6 | §0 item 7, §5 "Reconciliation", §7.1 | Wherever FD-1 is invoked (including "PROVED for n ≥ 3 in FD-1's two-sided branch"), state FD-1's hypotheses: n ≥ 3, K meets no edge, D_K ⊆ U a.e., (G), world-best models coherent. |
| G8 | §6.2 | State the precise scope of the naive-unsafe examples (§3.3): unsafe at the minimax prior, stable within 10⁻⁴, not stable at 10⁻². |
| G7 | Lemma 2.1(c) | The "−𝟙 − p" step is unnecessary; conic Carathéodory gives r ≤ n directly. Optional: note in Lemma E that Lyapunov can be replaced by relaxed choices plus uniqueness (row 4c); this is the form that transfers to §7.2. |

Suggested sentence for the universal note (replacing the last paragraph of its §"Lower-dimensional credal sets"): "On the full domain ℝⁿ the same ranking covers every credal set, including precise, lower-dimensional and boundary ones. Rivals with a nonempty coherent hull are handled as in Theorem H, with K′ replaced by any point of Q_X. A rival with an empty coherent hull contains a part, X ∩ {λ·h<0} for some prior λ, whose Brier moment is a sure loss; a coherent improvement inside {λ·h>0} removes that part, and no coherent model can undergo such a change."

## 5. Files (`ref66ts_py/`)

| File | Content |
|---|---|
| `poly3.py` | independent exact engine: polytope C ∩ B by vertex enumeration, μ and m for the L1 and Linf densities, generators, Q polygons, set algebra, safety test |
| `polyf.py` | vectorised float version (prior searches only) |
| `refcore.py` | independent Case-1 and Case-2 constructions with exact certification |
| `check_engine.py` / `.out` | engine vs geo3 (exact agreement) and sanity values |
| `regen_lifts.py`, `lifts.pkl` | regenerates TS66's two lifted rivals from its seed without TS66's searches |
| `ref_case2.py`, `ref_case2_*.log` | Case 2, two measures. Stopped early; partial logs only (§3.1) |
| `ref_case1.py` / `.out`, `ref_case1b.py` / `.out` | Case 1 on ℝ³ with boundary / lower-dimensional / full Q_X, two measures |
| `ref_naive.py` / `.out` | lifted rivals against a crude Brier-dominating half-space |
| `ref_naive2.py` / `.out`, `ref_naive3.py` / `.out` | the naive defender at the true minimax prior; exact robustness grids |
| `ref_misc.py` | A_K and U ∪ −U witnesses, protection, Lemma E, safety vs attack search: written, stopped before output |
