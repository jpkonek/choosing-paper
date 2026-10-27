# RF67b: referee report on the full-domain infinite-world theorem (AUDIT_r67_brief §2)

26 October 2026. Referee RF67b, working independently of RF67a; I have not read `RF67a_notes.md`. I re-derived every step by hand.

Labels: PROVED (re-derived or proved here by the referee) / CHECKED (exact computation) / NUMERICS / CONJECTURE.

Scripts are in `rf67b_py/`. Run each with `python3 -I <script>` from that folder; each writes an `.out` file.

## Verdict at the top

**The full-domain theorem holds.** I found no mathematical error in the Proposition or in the Theorem. The repair statement holds in the strong form the author wants: N is coherent, N ⊆ hull(X∖N) for all of N, the margin is uniform, and the change cannot be applied to any coherent model. Every ranking consequence also holds, as does coverage of every coherent target on E with literal (LF).

There are **five gaps**. None affects the truth of the theorem.
- One sentence in the protection paragraph is false as written: "sure losses uniformly negative a.e.". It is not needed. See P2.
- One lemma of §7 must be restated for U = E: Lemma 7.8(c) and the (A2) step that cites it. Its proof uses "h ∉ U". See P1.
- The theorem statement should record where N lies. Without this, the restricted-domain results do not follow as corollaries. See G3.
- The safety test must be stated with the empty-hull case kept separate. The convention "hull = E" alone gives the wrong test when nothing is added. See G1.
- "Full support … when stating coverage" overstates the role of (M3). See G4.

**Exact hypotheses under which the theorem holds (PROVED).**
1. **Worlds and gambles.**
   - Ω is any nonempty set.
   - E ⊆ ℓ∞(Ω) is a sup-norm-closed, **separable** linear subspace with 1 ∈ E. Alternatively, E contains some e with inf_Ω e > 0, by Remark 7.11, which transfers verbatim.
   - S is the set of states.
2. **The measure.** μ is a finite Borel measure on (E, ‖·‖) with:
   - **(M1)** ∫‖h‖ dμ < ∞;
   - **(M2)** μ{P_Q = 0} = 0 for every credal set Q.

   The only instances of (M2) the proof actually uses are:
   - Q = {q} for every state q;
   - Q = Q_B for Borel B;
   - Q = S;
   - Q = {δ_ω}.
3. **Models and coherence.**
   - Models are the Borel subsets of E, identified modulo μ.
   - A model is coherent if it equals some D_Q a.e., with Q a credal set: nonempty, weak-* closed and convex.
   - A record is safe if it applies to no coherent model.
   - The simple ranking is the one of §7.5, with this safety.
4. **Conclusions under (M1) and (M2) alone.** The following hold:
   - the repair theorem;
   - protection;
   - undominated = coherent;
   - (G), (IB), (TC), (FCC), (Add), (GC), strong (C), (ID) and (W);
   - "every credal set K is covered on E".
5. **Full support (M3)** is needed only for the identification of coherent models:
   - Q ↦ [D_Q] is injective;
   - the credal set of a coherent model is unique.

   Without (M3), distinct targets may be the same model, so "covers every target" loses content but stays true.
6. **Not needed:**
   - (M3), for any existence or dominance claim;
   - any K′;
   - μ{sup h = 0} = 0;
   - Lyapunov's theorem;
   - countable additivity of states;
   - K_⊥ = {0}, full dimensionality, or a strictly positive member of K.

**Recommended statement (PROVED).** Assume (M1) and (M2). Let X ⊆ E be Borel and incoherent modulo μ. Then there is a credal set Q, with N := D_Q a literal open coherent set, such that the following hold:
- **(i) Uniform margin.** inf_{q∈S} q(m(N) − m(X)) > 0. Equivalently, inf_Ω (m(N) − m(X)) > 0.
- **(ii) Hull inclusion.** N ⊆ hull(X∖N), where hull(B) := D_{Q_B} if Q_B ≠ ∅ and hull(B) := E if Q_B = ∅.
- **(iii) Location.**
  - If Q_X ≠ ∅: N ⊆ hull(X), and hull(X∖N) = hull(X).
  - If Q_X = ∅: N ⊆ hull(X ∩ {q* > 0}) ⊆ {q* > 0}, where q* is the state of the Proposition.
- **(iv) Safety.** r(N,X) applies to no coherent model. In fact (ii) together with improvement at every world already implies this (Proposition R below).

**Dependency chain (PROVED; this is the shortest I can certify):**
1. Lemma 7.1: states.
2. Lemma 7.2: envelopes.
3. Lemma 7.5(a)–(c), restated without K′ and with Q_B possibly empty.
4. The relaxed-choice minimax lemma (Step B of Theorem 7.7).
5. The Proposition: the uniformly losing part.
6. Theorem 7.7: the one-sided repair, used inside a coherent hull.
7. The full-domain theorem.
8. Lemma 7.8(b), and Lemma 7.8(c) restated for U = E (P1).
9. Lemma 6.1, which gives the ranking.
10. (LF) with N = E.

Theorem 7.7 is an **ingredient** of the full-domain theorem, not a corollary of it. The one-sided *dominance* result therefore cannot be presented as a consequence of the headline theorem without circularity. The one-sided and hull-closed *coverage characterisations* are separate domain statements (G3, item 20).

---

## 1. Verdict table

| # | Item | Verdict | Note / repair |
|---|---|---|---|
| 1 | Setting on U = E: models, coherent class, Q_B and hull with Q_B possibly empty | CORRECT, **GAP (expository)** | Lemma 7.5(a)–(c) and Lemma 7.6 are stated with K′. On E they hold with "Q_B is weak-* closed and convex, possibly empty". When Q_B ≠ ∅: P_{Q_B} ≥ 0 a.e. on B, B ⊆ hull(B) a.e., and B ⊆ D_Q a.e. ⟺ Q ⊆ Q_B ⟺ hull(B) ⊆ D_Q. The proofs never use K′: closedness by sequences, density in the compact metrizable Q_B, then (M2) for Q_B. Restate them once for E. |
| 2 | Existence and attainment of the minimax (Proposition) | CORRECT | See §2.1. Sion: S is compact and convex in (E\*, w\*); Z is compact and convex in (E, ‖·‖); Φ(q,z) = q(z) is bilinear and separately continuous. z ↦ min_S q(z) = inf_Ω z is 1-Lipschitz on compact Z, so its maximum is attained. q ↦ max_Z q(z) = ∫_X q(h)⁻ dμ is weak-* lower semicontinuous (in fact continuous, by dominated convergence along sequences, since S is metrizable), so its minimum is attained. The minimum is positive because Q_X = ∅. |
| 3 | The relaxed choice is the set L = X ∩ {q\* < 0}; {q\* = 0} is null | CORRECT, **GAP (exposition)** | The audit compresses the saddle step. Write it out (§2.1): η = min_S q(z\*) ≤ q\*(z\*) ≤ max_Z q\* = η, so z\* maximises q\* over Z. Then every preimage f\* is a relaxed maximiser of ∫ f(−q\*(h)) dμ over 0 ≤ f ≤ 1_X. This forces f\* = 1_L a.e., using (M2) with Q = {q\*} (a credal set). L is Borel. Any minimiser q\* works, because saddle points form a product. |
| 4 | m(L) ≤ −η at every world, and the meaning "at every state" | CORRECT | The saddle gives q(m(L)) ≤ −η for **every state** q. Because P_S(h) = inf_Ω h (Lemma 7.1(b)), this is **equivalent** to m(L)(ω) ≤ −η for every ω ∈ Ω, with no exceptional set. The state q\* need not be an evaluation, and need not be countably additive on Ω (§4.1, §4.2). |
| 5 | Case X₊ coherent; case X₊ null | CORRECT, **GAP (minor)** | m(X₊) − m(X) = −m(L) ≥ η1, since X ∩ {q\* = 0} is null. *Coherent X₊:* take N := hull(X₊) = D_{Q_{X₊}}, not "X₊". It is a literal D-set, a.e. equal to X₊ (if X₊ = D_Q a.e., then X₊ ⊆ hull(X₊) ⊆ D_Q a.e.), and it lies in {q\* > 0} as a set. *Null X₊:* Q_{X₊} = S and hull(X₊) = D_S. Under (M3), ∅ is incoherent and Theorem 7.7 on U = D_S (K′ = S, so C_U = {D_S}) returns N = D_S. Without (M3), D_S may be null, ∅ is then coherent, and N = D_S. Both are covered by the audit's text. Say so. |
| 6 | Theorem 7.7 inside hull(X₊): which K′ and which domain; Step C uses q\* ∈ Q_{X₊} | CORRECT | Two legitimate choices. (a) **K′ = Q_{X₊}, U = hull(X₊)**: Q_{X₊} ∋ q\* is a credal set; X₊ ⊆ U a.e. (item 1); X₊ ∉ C_U because X₊ is globally incoherent; k(h) ≥ P_{Q_{X₊}}(h) > 0 on U for k ∈ K′. (b) **K′ = {q\*}, U = {q\* > 0}**: X₊ ⊆ U as sets. In both, Step C's non-null gain uses k ∈ K′ with k ≥ 0 a.e. on X₊; q\* serves, since q\* > 0 on X₊. The output N = D_Q with Q ⊇ K′ ∋ q\* is globally coherent. Theorem 7.7 needs (M1) and (M2), not (M3). |
| 7 | Case Q_X ≠ ∅ | CORRECT | Theorem 7.7 with K′ = Q_X, U = hull(X), or with K′ = {q₀} for any q₀ ∈ Q_X and U = {q₀ > 0} (X ⊆ U a.e. because {q₀ = 0} is null). Q_B, and hence hull, does not depend on U, so 7.7(ii) is the full-domain hull statement. Safety against **every** D_Q follows from Lemma 7.6 (iii)⇒(ii), whose proof uses only Lemma 7.5(c). |
| 8 | N ⊆ {q\* > 0}, so L ⊆ X∖N | CORRECT | N = D_Q with q\* ∈ Q. So N ⊆ {q\* > 0} **as sets**, and L ⊆ X∖N as sets, not merely a.e. |
| 9 | Q_L = ∅ via a state applied to a Bochner integral | CORRECT | States are bounded linear functionals with norm 1, so q(m(L)) = ∫_L q(h) dμ (Hille). If q ∈ Q_L, the right side is ≥ 0, while the left side is ≤ −η. Q is antitone, so Q_{X∖N} ⊆ Q_L = ∅, and no D_Q contains X∖N a.e. **Nearby strengthening (PROVED, §3.3):** μ(L) > 0 and m(L) ≤ 0 at every world already force Q_L = ∅. |
| 10 | The record r(N,X) is safe | CORRECT | Case 1: μ((N∖X) ∩ hull(X∖N)) = μ(N∖X) > 0. Case 2: Q_{X∖N} = ∅. This holds even when N∖X is null: the record (∅, X∖N) applies to nothing. |
| 11 | Uniform total improvement | CORRECT | Case 2: q(m(N) − m(X)) ≥ η + v′/2 ≥ η for every state q, where v′ is Theorem 7.7's value for X₊ (v′ = 0 when N = hull(X₊)). Case 1: ≥ v/2. |
| 12 | N ⊆ hull(X∖N) for **all** of N, in both cases | CORRECT | Case 1: 7.7(ii) gives hull(X∖N) = hull(X) ⊇ N₀ ⊇ N. Case 2: Q_{X∖N} = ∅, so hull(X∖N) = E. **New (PROVED, §3.2, Proposition R):** coherent N with N ⊆ hull(X∖N) and m_ω(N) > m_ω(X) for every ω together *imply* safety. The two clauses of the repair theorem therefore suffice for the ranking. |
| 13 | Protection with uncountably many worlds on E | CORRECT, **GAP P1 (must restate a lemma)** | Lemma 7.8(c) concludes "B is null" via "h ∉ U". This fails for U = E. The correct full-domain version (PROVED, §3.1): guidance at every world gives A ⊆ D_S a.e. and B ⊆ {sup_Ω h ≤ 0} a.e. Every D_Q contains D_S and excludes {sup h ≤ 0}, since q(h) ≤ sup h. So (A2) holds: Y = C a.e. (A5) also holds: a non-null such record is safe. Both proofs use the countable norming set, (M2) with Q = S, and (M2) with Q = {δ_ω}. |
| 14 | "Sure gains uniformly positive a.e. and sure losses uniformly negative a.e."; is {P_S = 0} null needed, and the analogous set for −h? | **GAP P2: one half false as written; not needed** | {P_S = 0} null is **needed and essential**. Example 7.4 transfers to E verbatim: C ∪ R strictly dominates C. The analogous set {sup h = 0} = −{P_S = 0} is **not** null under (M1)–(M3) in general. Counterexample (PROVED, §3.4): E = C[0,1], with μ = (admissible μ₀) + law of h_U = −(x − U)², U uniform. Then μ{sup h = 0} ≥ 1, while μ{P_Q = 0} = 0 for every Q. The record (∅, {h_U}) is guidance at every world and removes gambles that are not uniformly negative. Uniform negativity is **not needed**: D_Q is defined by strict inequality, so sup h ≤ 0 already excludes h from every D_Q. Repair: replace the sentence with "…adds gambles that are uniformly positive a.e. (by μ{P_S = 0} = 0) and removes gambles that are nowhere positive; every coherent model contains the former and excludes the latter." |
| 15 | Ranking clauses: (G), (IB), (TC), (FCC), (Add), undominated = coherent, (GC), strong (C), (ID), (W) | CORRECT | Lemma 6.1 with (A1) from 7.8(a), using (M2) for δ_ω; (A2) and (A5) from P1; (A3) from the Theorem; (A4) set-theoretic. Strictness: the reverse record has a negative increment at every world (at most −η in Case 2, at most −v/2 in Case 1), so it is neither guidance nor safe-accepted. **Non-transitivity on E (PROVED; CHECKED numerically, `intransitive_full.out`).** Example 8.1 lives on a one-sided U, so it does not transfer automatically. A full-domain example: E = ℝ² with Gaussian μ; A = ball(0.1) about (1,−1); A′ = A₁ ∪ A₂ with A₁ = ball(0.3) about (1.5,−0.5) and A₂ = ball(0.1) about (−1,−0.5). At world 1: A′ ⪯₁ A (the record (A′, A) is safe because A₁ ⊆ hull(A), and m₁(A′) − m₁(A) ≈ 0.0145 > 0); A ⪯₁ ∅ (guidance); but not A′ ⪯₁ ∅ (A₂ has h₁ < 0, and (A′, ∅) applies to D_{e₂} = {h₂ > 0}). By the special case of row 21, this is an instance of the infinite-world setting. |
| 16 | Sets versus equivalence classes; what "every coherent model" means | CORRECT, **GAP G2 (statement)** | Every ingredient depends only on the μ-class: Q_X, hull, m, L and X₊ up to null sets, guidance, "applies to", safety. "Coherent" means "a.e. equal to some D_Q". By Proposition 7.16 (which uses (M2) only), this equals "a.e. equal to a coherent set of desirable gambles". Such a set is measurable for the completion only, so it is a model through its Borel version D_{Q_D}. The statement must say three things: (a) a raw set can be literally incoherent yet coherent mod μ (e.g. D_Q ∪ any null set; with line-supported μ, anything agreeing with D_Q on the lines); (b) the classification is **μ-relative**: mutually singular admissible μ, μ′ classify the same raw set differently; (c) the defender can always be taken to be a literal open D_Q (item 5). |
| 17 | Literal (LF) on E | CORRECT | Take N = E. Every Borel X satisfies X ⊆ E. This is vacuous, as it should be: (LF) is a domain condition. No K_⊥ = {0}, relint, full-dimensionality or strictly positive k is needed. Theorem 7.13(c) concerns one-sided domains, and E is not one-sided (take O = E). |
| 18 | Every coherent target D_Q is covered (Q any credal set) | CORRECT | The cover clauses are (i) (G) and (IB); (ii) (GC); (iii) (C); (iv) D_K ∈ M_E and undominated (protection); (v) (ID); (vi) (LF) with N = E. **(M3) is not used.** Precise targets {p} are covered for any state p, including states that are not evaluations. So are boundary targets, K = S, and finitely generated K. |
| 19 | What full support is needed for | CORRECT, **GAP G4** | (M3) gives the following. *Uniqueness of Q:* D_{Q₁} = D_{Q₂} a.e. ⇒ Q₁ = Q₂, by Lemma 7.5(d) and Lemma 7.2(d); the K′ part is irrelevant on E. *Distinctness:* distinct targets are distinct models, so the undominated classes correspond bijectively to credal sets. Without (M3): if μ is carried by D_S ∪ (−D_S), every D_Q is a.e. D_S and there is only one coherent model. The audit's "full support … when … stating coverage" should read "…when identifying distinct coherent models; the coverage clauses themselves do not use it". |
| 20 | Corollaries for restricted domains (one-sided D_{K′}; hull-closed) | **GAP G3 (statement); repaired here (PROVED, §3.5)** | The theorem as stated ("a coherent N with a safe record and uniform improvement") does not say where N lies, so nothing follows for U ≠ E. With location clause (iii), the following holds. *Hull-closed U* (hull(B) ⊆ U a.e. whenever B ⊆ U and Q_B ≠ ∅; this includes D_{K′}, E, and every U ⊇ {sup h > 0}): U-safety equals E-safety for records inside U; the defender lies in U; so the U-ranking is the restriction of the E-ranking, with undominated = C_U. *One-sided D_{K′}:* here Q_X ⊇ K′, so Case 2 never occurs, and the dominance part **is** Theorem 7.7, an ingredient. The (LF) characterisations (Proposition 7.12, Theorem 7.13; in finite dimensions, Lemma LF) are separate domain statements, not consequences. |
| 21 | Finite worlds: TS66's finite result as the case E = ℝⁿ with Lebesgue-equivalent μ | CORRECT | (M) ⇒ (M1) (‖h‖∞ ≤ \|h\|), (M2) (Lemma D(b)) and (M3). The states are Δ, the coherent class, safety and ranking are TS66's on U = ℝⁿ, and hull(∅-supported) = ℝⁿ is TS66's D_∅ convention. So TS66 Corollary 3.5 (on ℝⁿ), Theorem 4.1 (U = ℝⁿ) and Corollary 5.3(a) ("every credal set is covered on ℝⁿ, including precise, lower-dimensional and boundary targets such as {e₁}, [e₁,e₂], Δ") are special cases. The theorem is strictly more general in μ, e.g. line-supported measures singular to Lebesgue (Remark 7.10). TS66 Lemma E (i)⟺(iii)⟺(iv) also transfers (§3.3). **Not** special cases: Lemma 2.1(c) (a sure-loss combination of ≤ n density points: Carathéodory, finite-specific); Proposition 5.2 / Corollary 5.3(b),(d) ((LF) on V₀ and on n = 2 sectors: domain statements); Proposition 3.2(c),(d). Hull-closed U in general: via item 20. |
| 22 | Scope: arbitrary worlds versus the gamble space; order unit | CORRECT | Ω is arbitrary. E must be separable with an order unit bounded below. ℓ∞(Ω) for infinite Ω is excluded (no full-support finite measure, and S is non-metrizable). Remark 7.11 transports the full-domain statement unchanged: the D_Q, the states, signs at each world, and m_ω = e(ω)·m̃_ω. |
| 23 | Adversarial: rivals containing h and −h | **No counterexample** | X = E (§4.1, exact). In E = {a + bω} on (0,1], q\* = q₀ (the "limit at 0" state, not an evaluation), η = 1/√(2π), L = {a < 0}, N = D_{q₀}; the margin is exactly η at every world. In E = span{1, ω, ω²} on [0,1], q\* = δ₀. Also D_Q ∪ (−D_Q): Q_X = ∅ under (M3). Sets B ∪ (−B) with −B null (asymmetric μ) are just B mod μ. NUMERICS confirm (`whole_space.out`). |
| 24 | Adversarial: Q_X = ∅ with the sure loss spread thinly | **No counterexample** | Compactness rules out an "infinitely thin" failure: if X = ∪_n X_n, then Q_X = ∩_n Q_{X₁∪…∪X_n} is a decreasing intersection of compact sets, so Q_X = ∅ is already witnessed by a finite sub-union. η > 0 always, however small. NUMERICS (`thin_sure_loss.out`): on Ω = [0,1], X is a union of thin cones around the continuum g_c = δ − (ω − c)², each positive near c, so no single direction is a sure loss. Five rivals; saddle identity max_ω m(L)(ω) = −η to relative error ≤ 3·10⁻⁵; the defender's margin is ≥ η; N ⊆ {q\* > 0}; L ∩ N = ∅. q\* was an evaluation in three rivals and an interior (non-extreme) state in one. |
| 25 | Adversarial: E = C(Ω), Ω uncountable | **No counterexample** to the theorem | The norming set is countable (separability). The only hazard found is item 14's false sentence, whose counterexample lives exactly here. Example 7.4 confirms that μ{P_S = 0} = 0 is essential. |

**Score:** 25 items. ERROR: 0. GAP: 7 rows (1, 3, 5, 13, 14, 16, 19) are expository or wording gaps; one row (20) is a statement gap that needs the location clause. All other rows are CORRECT.

---

## 2. The Proposition and the Theorem, written out (PROVED)

### 2.1 Proposition (uniformly losing part)

Assume (M1) and (M2). Let X be Borel with Q_X = ∅. Then X is non-null, since Q_∅ = S.

1. **The compact set.** Put F_X = {f ∈ L∞(μ) : 0 ≤ f ≤ 1_X}. By Step B of Theorem 7.7 (with G replaced by any Borel set), Z := {−T f : f ∈ F_X} is norm-compact and convex.
2. **Minimax.** Put Φ(q,z) = q(z) on S × Z. By Sion's theorem:

   η := max_Z min_S Φ = min_S max_Z Φ.

   Here max_Z Φ(q,·) = ∫_X (q(h))⁻ dμ. This is attained by f = 1_{X∩{q<0}}.
3. **Attainment.** As in item 2 of the table.
4. **Positivity.** If ∫_X q⁻ = 0, then q ≥ 0 a.e. on X, so q ∈ Q_X. Since Q_X = ∅, the function is positive at every q, and so η > 0.
5. **The saddle step.** Let z\* attain the maximin and q\* the minimax. Then

   η = min_S q(z\*) ≤ q\*(z\*) ≤ max_Z q\* = η.

   Write z\* = −T f\*. Then f\* maximises ∫ f·(−q\*(h)) dμ over F_X. Hence f\* = 1 a.e. on X ∩ {q\* < 0} and f\* = 0 a.e. on X ∩ {q\* > 0}. By (M2) with Q = {q\*}, the set {q\* = 0} is null, so f\* = 1_L a.e. and z\* = −m(L).
6. **Conclusion.** min_S q(−m(L)) = η. That is, q(m(L)) ≤ −η for every state q. Equivalently, m(L) ≤ −η1 pointwise on Ω. ∎

### 2.2 Theorem: the repair on E

**Case 1: Q_X ≠ ∅.** Apply Theorem 7.7 as in rows 6–7.

**Case 2: Q_X = ∅.**
1. Take q\*, η and L from §2.1, and put X₊ := X ∩ {q\* > 0}. Then m(X₊) − m(X) = −m(L) ≥ η1, and q\* ∈ Q_{X₊}.
2. **Choice of N.**
   - If X₊ is coherent, put N := hull(X₊).
   - Otherwise, take N from Theorem 7.7 applied to X₊, with K′ = Q_{X₊} and U = hull(X₊).

   In both cases N = D_Q with q\* ∈ Q, so N ⊆ {q\* > 0} and L ⊆ X∖N.
3. **Safety.** By §2.1 and row 9, Q_L = ∅, so Q_{X∖N} = ∅.
4. **Margin.** q(m(N) − m(X)) = q(m(N) − m(X₊)) + q(m(X₊) − m(X)) ≥ 0 + η. ∎

**Optional simplification (PROVED).** Case 2 needs no shrink and no contraction lemma.
- Let G₁ be either hull(X₊) or the half-space {q\* > 0}, and run the relaxed minimax of Step B on G₁ with x = m(X). Note that x ∉ Z_{G₁} in general.
- The value is v′ := max_{Z_{G₁}} min_S q(z − x) ≥ min_S q(m(X₊) − m(X)) ≥ η, because m(X₊) ∈ Z_{G₁}.
- The saddle maximiser is N = G₁ ∩ {π\* > 0}, a coherent set inside {q\* > 0}, with margin ≥ η.

This is TS66's main route, transferred. The audit's route through Theorem 7.7 is also valid.

---

## 3. Supporting proofs (PROVED)

### 3.1 P1: Lemma 7.8(c) on U = E

**Lemma.** Assume (M2). Let Ω′ ⊆ Ω with inf_{Ω′} h = inf_Ω h for every h ∈ E. Let (A,B) be guidance at every ω ∈ Ω′. Then:
- A ⊆ D_S a.e.;
- B ⊆ {h : sup_Ω h ≤ 0} a.e.;
- (A,B) is guidance at every ω ∈ Ω;
- if (A,B) is non-null, it is safe.

*Proof.*
1. **Reduction to countably many worlds.** As in Lemma 7.8(c), take a countable Ω″ ⊆ Ω′ that norms both infima and suprema. Off a countable union of null sets:
   - every h ∈ A satisfies h > 0 on Ω″, so inf_Ω h ≥ 0;
   - every h ∈ B satisfies h < 0 on Ω″, so sup_Ω h ≤ 0.
2. **The added part.** Removing the null set {P_S = 0} gives A ⊆ D_S a.e.
3. **Guidance at every world.** For each ω, B ∩ {h(ω) ≥ 0} ⊆ {h(ω) = 0}, which is null by (M2) with Q = {δ_ω}.
4. **Safety.**
   - If B is non-null: every q has q ≤ sup h ≤ 0 on B, and {q = 0} is null. So no q is ≥ 0 a.e. on B, and Q_B = ∅.
   - If B is null and A is non-null: hull(B) = D_S ⊇ A.

   Either way the record is safe. ∎

**(A2) on E.** Suppose r(Y,C) is guidance at every world, with C = D_Q a.e. Then:
- Y∖C ⊆ D_S ⊆ D_Q a.e. But Y∖C is disjoint from C, so Y∖C is null.
- C∖Y ⊆ D_Q ∩ {sup h ≤ 0} = ∅ a.e., since q(h) ≤ sup h.

So Y = C a.e. This is TS66 Lemma 2.3 transferred: one-sidedness is not used.

### 3.2 Proposition R: hull inclusion plus improvement implies safety

Assume (M2). Let N, X be models with N ⊆ hull(X∖N) and m_ω(N) > m_ω(X) for every ω. Then r(N,X) applies to no coherent model.

*Proof.*
1. Write A = N∖X and B = X∖N. Suppose r applies to D_Q: that is, B ⊆ D_Q a.e. and A ∩ D_Q is null.
2. Then Q ⊆ Q_B, so Q_B ≠ ∅ and N ⊆ hull(B) ⊆ D_Q. Hence A ⊆ D_Q, and so A is null.
3. Then m(N) − m(X) = −m(B) > 0 at every world. So m(B) ≤ 0 pointwise, and B is non-null.
4. By §3.3, Q_B = ∅. This contradicts step 2. ∎

The hull inclusion alone is not enough. Example: X = D_Q ∪ B with ∅ ≠ Q ⊆ Q_B and N = D_Q. Then (∅, B) applies to hull(B). Strict improvement is exactly what excludes such cases. This confirms AUDIT_r67_message2 §2: "the accompanying score improvement is essential."

### 3.3 A pointwise nonpositive moment already gives an empty hull

Assume (M2). If μ(L) > 0 and m(L)(ω) ≤ 0 for every ω, then Q_L = ∅.

*Proof.* Let q ∈ Q_L. Then q ≥ 0 a.e. on L. The set {q = 0} is null, so q > 0 a.e. on L, and therefore q(m(L)) = ∫_L q(h) dμ > 0. But q is positive and m(L) ≤ 0, so q(m(L)) ≤ 0. Contradiction. ∎

**Consequence: Lemma E on E.** The following are equivalent:
- Q_X = ∅;
- some non-null Borel L ⊆ X has m(L) ≤ 0 at every world;
- some L ⊆ X has m(L) ≤ −η1 for some η > 0.

The second implies the first by §3.3, the first implies the third by §2.1, and the third implies the second trivially.

### 3.4 Counterexample: μ{sup h = 0} > 0 is compatible with (M1)–(M3)

**Setting.**
- Ω = [0,1] and E = C[0,1].
- μ₀ is as in Lemma 7.3, so it satisfies (M1)–(M3).
- ν′ is the law of h_U(x) = −(x − U)², with U uniform on [0,1].
- μ := μ₀ + ν′.

**(M1) and (M3).** ‖h_U‖ ≤ 1, so (M1) holds. (M3) is inherited from μ₀.

**(M2).** Let Q be any nonempty compact set of states. Then

  P_Q(h_U) = −max_{q∈Q} ∫(x − U)² dq(x).

This is 0 only if every q ∈ Q equals δ_U, that is, only if Q = {δ_U}. That happens for at most one value of U, so ν′{P_Q = 0} = 0.

**The boundary is not null.** Every h_U has sup h_U = 0, attained at x = U, so μ{sup h = 0} ≥ 1.

**Consequences.**
- The record (∅, {h_U : U ∈ [0,1]}) is guidance at every world: h_U(ω) < 0 unless U = ω.
- It removes gambles that are not uniformly negative.
- Protection still holds, because no D_Q contains any h with sup h ≤ 0.

### 3.5 Restricted domains (G3)

Call U **hull-closed** if hull(B) ⊆ U a.e. for every Borel B ⊆ U with Q_B ≠ ∅. Put C_U := {D_Q : D_Q ⊆ U a.e.}. Then:

**(a) U-safety equals E-safety for records inside U.** Suppose a record (A,B) inside U applies to some D_Q. Then Q ⊆ Q_B, hull(B) ⊆ D_Q ∩ U, and the record applies to hull(B) ∈ C_U.

**(b) The defender lies in U.**
- If Q_X ≠ ∅: N ⊆ hull(X) ⊆ U.
- If Q_X = ∅: N ⊆ hull(X₊) ⊆ U, because X₊ ⊆ U. This includes X₊ null, where hull(∅) = D_S ⊆ U by hull-closedness applied to B = ∅.

**(c) Protection on U** is the argument of §3.1. It does not use the domain.

**Conclusion.** On every hull-closed U, the simple ranking has undominated set C_U, with the same margins. Coverage of K on U ⟺ D_K ⊆ U a.e. and (LF) at D_K. The (LF) condition is a separate domain computation: Proposition 7.12 on D_{K′}; Lemma LF and TS66 Proposition 5.2 in finite dimensions.

---

## 4. Computations (`rf67b_py/`)

### 4.1 `whole_space.py` → `whole_space.out` (NUMERICS; the exact values are PROVED in row 23)

**Space (1): Ω = (0,1], E = {a + bω}.**
- The states are q_s(a + bω) = a + bs for s ∈ [0,1].
- F(q_s) = E[(a + bs)⁻] = √(1 + s²)/√(2π), which is minimised at s = 0. So q\* = q₀, which is not an evaluation.
- Monte Carlo gives argmin s = 0 and η ≈ 0.3995 (exact value 0.3989), with m(L) ≈ (−0.3995, −0.0005) (exact value (−η, 0)).

**Space (2): Ω = [0,1], E = span{1, ω, ω²}.** The argmin is δ₀, with the same η.

**In both spaces.** N = D_{q\*} = X₊ is coherent, and the margin is exactly η at every world.

### 4.2 `thin_sure_loss.py` → `thin_sure_loss.out` (NUMERICS)

**Setting.**
- Ω = [0,1], E = span{1, ω, ω²}, and μ is the standard Gaussian on the coefficients.
- The states are (1, m₁, m₂), with (m₁, m₂) in the moment space. This state space is curved, and its extreme points are the evaluations.
- Quadrature: 3·10⁶ Fibonacci directions, together with the radial factor E[R] = 2√(2/π).

**Rivals.**
- X is the union of the cones of angular radius ρ around g_c = δ − (ω − c)², for c ∈ [0,1].
- Every state is negative on some g_c: take |c − mean| > √δ. Every g_c is positive near c.
- Five rivals: (δ, ρ) = (.02, .06), (.05, .04), (.01, .08), and the first two again with the half-space {Lebesgue-mean > 0} adjoined. The adjoined half-space gives μ(X) ≈ 0.51, so that removing L matters.

**Results.**

| Check | Result |
|---|---|
| η | between 4.1·10⁻⁴ and 1.9·10⁻³ |
| Saddle identity max_ω m(L)(ω) = −η | relative error ≤ 2.7·10⁻⁵ (≤ 10⁻⁸ in four rivals) |
| m(L) ≤ −η(1 − 10⁻³) at every world | true in all five rivals |
| Defender, route A (G₁ = {q\* > 0}) | margin min_ω(m(N) − m(X)) ≥ η in every rival |
| Defender, route B (G₁ = hull(X₊)) | margin min_ω(m(N) − m(X)) ≥ η in every rival |
| Samples of N with q\* ≤ 0 | 0 |
| Samples of L inside N | 0 |

**Further observations.**
- q\* was the evaluation δ_{0.33}, δ_{0.35}, δ_{0.33} and δ_{0.52} in four rivals, and an interior state in the fifth. In that fifth rival, m(L) is nearly constant.
- The computed Q_{X₊} was, to grid accuracy, {q\*}. So hull(X₊) = {q\* > 0}, and routes A and B coincide.
- In the half-space variants, the margin (≈ 2.1·10⁻³ and 1.1·10⁻³) is barely above η. The removal of L, not the gain, carries the improvement.

**Status.** These are illustrations. The verdict rests on §2–§3.

---

## 5. Requested repairs

| # | Where | Repair |
|---|---|---|
| G1 | Safety test on E | State "safe ⟺ Q_B = ∅ or μ(A ∩ hull B) > 0". With the convention hull(B) = E when Q_B = ∅, the form "μ(A ∩ hull B) > 0" alone misclassifies (∅, B) with Q_B = ∅, which is safe. Optionally add Proposition R (§3.2). |
| G2 | Statement of the Theorem | Say explicitly that the following hold modulo μ: incoherence, the coherent class (= coherent sets of desirable gambles a.e., Proposition 7.16), and "undominated = coherent". Say that the defender is a literal D_Q. Add μ-relativity. |
| G3 | Statement of the Theorem | Add location clause (iii) and the hull-inclusion clause (ii). Then state the hull-closed corollary (§3.5). Do not call the one-sided dominance theorem a corollary: it is an ingredient. |
| G4 | "Full support … stating coverage" | (M3) is used only for uniqueness of Q and distinctness of the D_Q; the coverage clauses hold under (M1) and (M2). |
| P1 | Lemma 7.8(c) and the (A2) step | Restate as in §3.1 for U = E: the removed part is nowhere positive and lies outside every D_Q. |
| P2 | Protection paragraph | Replace "uniformly negative a.e." with "nowhere positive". Note that μ{sup h = 0} = 0 is neither assumed nor needed (§3.4), while μ{P_S = 0} = 0 is essential (Example 7.4). |
| E1 | Proposition proof | Write out the saddle step (§2.1, step 5). Optionally note that any minimiser q\* works. |
| E2 | Case 2 | Take N := hull(X₊) when X₊ is coherent. Mention the null X₊ case. Optionally use the shrink-free route (§2.2). |

With G1–G4 and P1–P2 made, I would accept the full-domain theorem as the headline result, under the hypotheses stated at the top.

## 6. Files (`rf67b_py/`)

| File | Content |
|---|---|
| `thin_sure_loss.py` / `.out` | Case 2 with a continuum-spread sure loss on [0,1]: q\*, η, saddle identity, and both defender routes. Five rivals. NUMERICS. |
| `intransitive_full.py` / `.out` | Non-transitivity of the simple ranking on the full domain ℝ² (row 15). |
| `whole_space.py` / `.out` | X = E in two spaces: q\* is a non-evaluation state (q₀) and δ₀; m(L) = −η1. Monte Carlo confirmation of exact values. |
