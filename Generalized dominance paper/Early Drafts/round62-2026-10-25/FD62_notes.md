# FD62 — Foundations: domains, global coherence, and the scope of round 61 (25 Oct 2026)

Labels: PROVED (proved here, not yet refereed) / CHECKED (exact rational computation) / CONJECTURE / NUMERICS.
Scripts: `fd62py/fd62_checks.py` (exact, `Fraction`) with `fd62_checks.out`; `fd62py/thmD_global.py` (LP) with `thmD_global.out`.

## 0. Answers in brief

**(a1) The auditor's counterexample is correct (CHECKED exactly).** On F61's domain A_K (uniform p, ε = 1/2), the world-1-best model X = A_K ∩ {h_1 > 0} is undominated under *every* ranking with strict (G). Yet x = (1,−1,−20) and y = (1,4,−1) lie in X, while x + y = (2,3,−21) is not even available. All 64 corner perturbations of size 1/2 (sup norm) keep this pattern, so X is not a.e. equal to any D_Q.

**(a2) What F61 Theorem D proves.** It proves *relative* (trace) coherence: every undominated model equals A_K ∩ D_{K*} a.e. It also proves that the target D_K is undominated and globally coherent, with (G), (IB), (C) and (LF). It does not prove global coherence, and global coherence is false for some undominated models: exactly the |W0| = 1 family (PROVED for n = 3 when |W0| ≥ 2; NUMERICS otherwise).

**(a3) Exact obstruction: a dichotomy theorem (Thm FD-1, PROVED).** Assume:
- n ≥ 3;
- a target K that meets no edge of Δ (for example K ⊆ relint Δ), with D_K a model;
- any ranking with strict (G);
- every undominated model is *globally* coherent.

Then the domain is either one-sided, or it is the full domain up to the sure-loss cone. **No two-sided domain strictly between a one-sided U and the full domain works**, whatever the ranking. For T1, global two-sided coverage is therefore exactly the full-domain problem. There:
- convex first levels are excluded (F61 Thm A, plus T1 is not a box);
- veto-led rankings with Brier are excluded (F61 Cor B1);
- strictly sign-correct charts are OPEN.

I add one necessary condition there (Lemma FD-3): a globally coherent Bayes act at a prior π depends only on the coordinates in supp π.

**(b) Normalised boxes are covered, on the full domain and on every one-sided U = D_{K′} with K′ ⊆ relint K (Prop FD-B, PROVED).** The ranking is the single-level additive *box chart* c_j(h) = min(l_j h_j, u_j h_j), a concave, positively homogeneous, piecewise-linear chart with a diagonal matrix on each orthant.
- It meets all four conditions of the auditor's §4 certificate.
- The constant-odds-ratio (COR) credal set is such a box. Its chart is Walley's own COR criterion: Σ_j p_j(h_j⁺ − k h_j⁻) > 0.
- So the COR set is **covered**. It is not covered by VB-type rankings.
- Every round-61 exclusion is consistent with this positive control once correctly scoped. Box corners are *tangential* from their upper-bound worlds and anti-visible from the rest (CHECKED, n = 3, 4, 5). So O61 Thm A does not touch them. O61 Thm B, E61 Cor 5.2 and O61's "piecewise-constant local priors fail" are statements about the reversed triangle only.

**(c)** The corrected round-61 status table is §6.

---

## 1. Setting and named hypotheses

- **(H1)** Worlds 1..n. Δ is the simplex with vertices e_i. For S ⊆ Δ, D_S := {h : m·h > 0 ∀ m ∈ S}.
- **(Hμ)** μ has a positive density (e.g. Gaussian) and a finite first moment. "Null" means μ-null, equivalently Lebesgue-null.
- **(Dom)** A domain is a measurable cone A ⊆ ℝⁿ of available gambles.
  - Models are measurable X ⊆ A, modulo null sets.
  - At the pair {h,−h}, the menu consists of the available acceptances, silence, and (if both orientations are available) the contradiction.
- **(G)** Strict guidance at world i: if X is pointwise at least as good as Y at i (correct < silent < wrong < contradictory) and differs from Y on a non-null set, then X ≺_i Y. Here ≺_i is the strict part of ⪯_i.
- **(GC) Global coherence.** X = D_Q a.e. for some nonempty closed convex Q ⊆ Δ. This is the binding notion (BRIEF62; AUDIT §2).
- **(RC) Relative (trace) coherence on A.** X = A ∩ D_Q a.e. This is F61 §1's notion.
- **(TS) Two-sided.** A ∩ (−A) ∩ M is non-null, where M := {h with a positive and a negative coordinate}. (Pairs made of a sure gain and a sure loss are irrelevant to undominated models, so they are excluded.)

**Lemma 0 (PROVED; standard).** Let P, Q ⊆ Δ be nonempty, closed and convex.
- (i) D_P ⊆ D_Q ⇔ Q ⊆ P.
- (ii) Under (Hμ): if O is open and O ⊆ D_Q a.e., then O ⊆ D_Q.
- (iii) D_P ∩ D_Q = D_{conv(P∪Q)}.

*Proof.*
- (i) "⇐" is clear. For "⇒", take q ∈ Q∖P. Strictly separate q from P inside aff Δ by an affine functional, and write it as h·m. Then h ∈ D_P∖D_Q.
- (ii) O∖cl D_Q is open and null, hence empty. So O ⊆ int cl D_Q = D_Q, because D_Q is open and convex with nonempty interior (it contains int ℝⁿ₊).
- (iii) is immediate. ∎

---

## 2. Part (a1)–(a2): the counterexample and what Theorem D proves

### 2.1 The counterexample (CHECKED, `fd62_checks.out` §1)

Take p = u and ε = 1/2, so that v_1 = (2/3,1/6,1/6), v_2 = (1/6,2/3,1/6), v_3 = (1/6,1/6,2/3). Recall

  A_K = {h : at most one coordinate is positive, or v_k·h ≥ 0 at every k with h_k > 0}.

| gamble | v_1·g, v_2·g, v_3·g | in A_K | in X = A_K ∩ {h_1>0} |
|---|---|---|---|
| x = (1,−1,−20) | −17/6, −23/6, −40/3 | yes (one positive coordinate) | yes |
| y = (1,4,−1) | 7/6, 8/3, 1/6 | yes (v_1·y, v_2·y > 0) | yes |
| x+y = (2,3,−21) | −5/3, −7/6, −79/6 | **no** (two positive coordinates, v_1·(x+y) < 0) | no |

**Robustness.**
- The defining inequalities have margins 1 at x, 1 at y and 5/3 at x+y.
- Every v ∈ Δ satisfies |v·d| ≤ ‖d‖_∞. So any x′, y′ within sup-distance d < 5/6 of x and y keep the pattern.
- For d = 1/2, all 64 corner pairs were checked exactly. That suffices, since every constraint is linear on each box.

**Why this defeats every ranking (Lemma W1, PROVED).**
- On any domain A, the model B_i := A ∩ {h_i > 0} gives the correct-at-i advice wherever it is available and is silent otherwise. It is therefore pointwise best at world i.
- Under (G), any Y ≠ B_i a.e. satisfies B_i ≺_i Y, so no Y weakly dominates B_i. Hence B_i is undominated.
- Only strict (G) at world i is used: no transitivity, (IB) or completeness.
- On A_K, B_1 = X contains the open sets N_x, N_y, and N_x + N_y lies outside A_K. If X = D_Q a.e., then N_x, N_y ⊆ D_Q by Lemma 0(ii), so N_x + N_y ⊆ D_Q. That would make D_Q∖X non-null, a contradiction.
- **So no strictly guiding ranking on A_K has only globally coherent undominated models.**

### 2.2 What F61 Theorem D does prove (precise statement)

Under the AVB ranking on M_{A_K}, with K = conv{(1−ε_i)p + ε_i e_i}, p interior and n ≥ 3:
- (i) strict (G) and (IB);
- (ii) a compact convex score range, so every model is weakly dominated by an undominated model;
- (iii) **(RC)**: every undominated model is X* = A_K ∩ D_{K*} a.e., with K* given by F61's formula;
- (iv) D_K is undominated;
- (v) direct (C);
- (vi) (LF) at D_K;
- (vii) two-sidedness near the single-negative ("middle") parts of the facets.

The referee checked it under (RC) (REF61 §3).

Equivalent reading of (iii):
- X* is the set of *available* gambles of the coherent model D_{K*}.
- Equivalently, X* avoids sure loss and is closed under natural extension *within the domain*: A_K ∩ posi(X* ∪ int ℝⁿ₊) ⊆ X*. This holds because posi(X* ∪ int ℝⁿ₊) ⊆ D_{K*}.
- Silence is the advice wherever D_{K*}'s acceptance is unavailable. In the counterexample, the model is silent at {x+y, −(x+y)} although it accepts x and y.

**Which undominated models of Thm D are globally coherent.**
- *Sufficient (PROVED):* K ⊆ K* implies D_{K*} ⊆ D_K ⊆ A_K, so X* = D_{K*}.
- *n = 3 and |W0| ≥ 2 (PROVED):* X* = D_{K*}. Proof:
  - Let h ∈ D_{K*} have positive coordinates k and j. We need v_k·h ≥ 0.
  - If k ∈ W0, then v_k ∈ K*.
  - If k ∉ W0, then W0 = {j, i}. If h_i ≥ 0, then h ≥ 0. If h_i < 0, then v_i·h > 0, and Lemma D1's computation gives p·h > 0, hence v_k·h > 0.
- *|W0| = 1:* global coherence can fail. The world-best model (W0 = {1}, β = e_1, α = 0, K* = {e_1}) fails, with LP witness (1,1,−11). NUMERICS (`thmD_global.out`): 138 of 208 random |W0| = 1 draws fail. All 392 draws with |W0| ≥ 2 pass.

**Verdict on (a2).** Theorem D is a correct coverage theorem *for the relative notion (RC)*. It is not a coverage theorem under the binding notion (GC). Using it requires an explicit argument that silence on unavailable acceptances counts as coherent. F61's Thm B, Cor B2, Cor B3 and the maximality of A_K were all proved under (RC). They remain true as stated (global coherence implies relative coherence), but Thm FD-1 below makes them moot for (GC).

---

## 3. Part (a3): which two-sided domains can support global coherence?

**Theorem FD-1 (domain dichotomy; PROVED).** Assume:
- (H1), (Hμ), (Dom) and n ≥ 3;
- a closed convex K ⊆ Δ meeting no edge [e_i,e_j] of Δ (e.g. K ⊆ relint Δ; T1 qualifies), with D_K ⊆ A a.e., i.e. D_K is a model;
- a ranking with strict (G) at every world;
- every undominated model satisfies (GC).

Then:
- (a) For each i, A ∩ {h_i > 0} = D_{Q_i} a.e., with e_i ∈ Q_i ⊆ conv(K ∪ {e_i}) and the **compatibility** condition Q_j ⊆ conv(Q_i ∪ {e_j}) for all i, j.
- (b) **Dichotomy.** Either
  - every pair Q_i, Q_j intersects, and then A is one-sided (A ∩ (−A) ∩ M is null); or
  - Q_i = {e_i} for every i, and then A ⊇ ℝⁿ∖{h ≤ 0} a.e.: the full domain up to sure losses.

No (LF), (IB), transitivity, completeness, or undominatedness of the target is used.

*Proof.*
1. **World-best cones.** By Lemma W1, B_i = A ∩ {h_i > 0} is undominated, so B_i = D_{Q_i} a.e.
   - D_{Q_i} is open and a.e. inside {h_i > 0}, so D_{Q_i} ⊆ {h_i > 0} = D_{{e_i}} by Lemma 0(ii). Lemma 0(i) then gives e_i ∈ Q_i.
2. **Compatibility.** D_{Q_i} ⊆ A a.e., so D_{conv(Q_i∪e_j)} = D_{Q_i} ∩ {h_j > 0} ⊆ A ∩ {h_j > 0} = D_{Q_j} a.e. Lemma 0(ii) and then (i) give Q_j ⊆ conv(Q_i ∪ e_j).
3. **Target.** D_{conv(K∪e_i)} = D_K ∩ {h_i > 0} ⊆ D_{Q_i} a.e. So Q_i ⊆ conv(K ∪ e_i).
4. **Disjoint pairs lie in an edge.**
   - Let f(m) := 1 − m_i − m_j, which is ≥ 0 on Δ and 0 at e_i, e_j. Write s_i := max_{Q_i} f and s_j := max_{Q_j} f.
   - Every point (1−λ)e_i + λq of conv(Q_j ∪ e_i) has f = λf(q) ≤ s_j, so s_i ≤ s_j. By symmetry s_i = s_j =: s.
   - If s > 0, take a ∈ Q_i with f(a) = s and write a = (1−λ)e_i + λq with q ∈ Q_j. Then λf(q) = s with f(q) ≤ s, so λ = 1 and a = q ∈ Q_i ∩ Q_j.
   - Hence Q_i ∩ Q_j = ∅ forces s = 0, i.e. Q_i, Q_j ⊆ [e_i,e_j].
5. **The edge forces precise vertices.**
   - A point (1−t)k + te_i (k ∈ K, t < 1) lying in [e_i,e_j] would force k ∈ [e_i,e_j], which is excluded. So conv(K ∪ e_i) ∩ [e_i,e_j] = {e_i}, and step 3 gives Q_i = {e_i}. Likewise Q_j = {e_j}.
   - For any other l, step 2 gives Q_l ⊆ conv(Q_i ∪ e_l) = [e_i,e_l], and step 3 gives Q_l ⊆ conv(K ∪ e_l). Together these force Q_l = {e_l}.
6. **Sidedness.** If h ∈ A ∩ M and −h ∈ A, then h ∈ D_{Q_i} (h_i > 0) and −h ∈ D_{Q_j} (−h_j > 0), with i ≠ j. A common point q of Q_i and Q_j would give q·h > 0 and q·(−h) > 0. So two-sidedness requires a disjoint pair, and step 5 then gives the full branch.
   - Conversely, if all Q_l = {e_l}, then A ⊇ ∪_l {h_l > 0} a.e. ∎

**Corollaries (PROVED).**
- **FD-1a (A_K and kin).** A_K, U ∪ (−U), and every other two-sided domain that is not full up to sure losses support (GC) under *no* strictly guiding ranking, for any K meeting no edge. In each case the witness is a world-best model B_i.
  - For A_K the witness is the auditor's B_1. It also follows abstractly, since (2,3,−21) ∉ A_K has positive coordinates, so A_K is not full.
- **FD-1b (T1 on two-sided domains).** Globally covering T1, or any interior ε-contamination with n ≥ 3, on a two-sided domain is exactly the full-domain coverage problem. There:
  - worlds refining convex first levels give only normalised boxes (F61 Thm A), and T1 is not a box (L3.1(c), F61 Cor A1);
  - veto-led rankings with (L2) collapse to their level-2 ranking (F61 Cor B1), and with Brier only precise targets survive;
  - strictly sign-correct first levels need every a.e.-unique Bayes act to be coherent for a.e. prior (F61 Prop E). **This case is OPEN.**
  - On A = ℝⁿ, (RC) and (GC) coincide, so F61's full-domain theorems apply unchanged.
- **FD-1c (lower-dimensional targets).** P61 D1 and O61 Rem 1.1 already force two-sided domains for lower-dimensional K. With n ≥ 3, K meeting no edge, and (GC), they force *the full domain*.
  - Precise targets and degenerate boxes (some l_j = u_j) are covered there (Prop FD-B), so this branch is not empty.
- **FD-1d (n = 2).** Here the only edge is Δ itself, so the proof does not apply. Intermediate two-sided compatible tuples exist (e.g. disjoint Q_1 = [e_1,a] and Q_2 = [b,e_2]). Whether they support coverage was not examined; the known n = 2 two-sided coverage is on the full domain (REF61 §3.3).
- **FD-1e (the one-sided branch).** A = ⋃_i D_{Q_i} (off sure losses) for a pairwise-intersecting compatible tuple. A need not be convex. A convex one-sided U is D_{K′} (P61 remark).

**Lemma FD-3 (support restriction on the full domain; PROVED).** On the full domain, let each c_j be strictly sign-correct. Let X_π be the Bayes act of the prior π ≥ 0 with support S, and suppose X_π = D_{Q_π} a.e. Then Q_π ⊆ Δ_S := conv{e_s : s ∈ S}. So X_π depends only on (h_s)_{s∈S}: it is a cylinder over a cone in ℝ^S.

*Proof.*
- If h_s > 0 for all s ∈ S, then π·c(h) > 0 > π·c(−h), so h is accepted. Hence D_{Δ_S} = {h_S ≫ 0} ⊆ X_π a.e.
- Lemma 0 then gives Q_π ⊆ Δ_S. ∎

This is a strong necessary condition at edge priors that one-sided domains do not impose: there U ∩ {h_S ≫ 0} only gives Q_π ⊆ conv(K′ ∪ Δ_S). The box chart satisfies it, since Q_π = ν(π⊙Q) ⊆ Δ_S. Whether some strictly sign-correct chart realises T1 on the full domain is OPEN.

**Nearby reachable results** (following the project preference to name what *is* available):
1. T1 is globally covered on one-sided U by VB (P61 Thm A). Nothing is lost by staying one-sided.
2. If two-sidedness is wanted, Thm D gives it under (RC). Adopting (RC) as the official notion is a definitional change. It needs a stated justification: availability as a description of which problems are posed, with silence as non-commitment. It cannot be presented as the binding notion.
3. Under (GC) the only two-sided target domain is the full domain. The precise open problem there is a strictly sign-correct chart on ℝⁿ satisfying the round-62 certificate, with Lemma FD-3 as a necessary condition.

---

## 4. Part (b): box coverage, and reconciling every broad exclusion

### 4.1 Box chart (positive control; PROVED)

**Proposition FD-B.** Let Q = ∏_j [l_j,u_j] with 0 < l_j ≤ u_j, and K = ν(Q) := {q/𝟙·q : q ∈ Q}, so K ⊆ relint Δ. Put

  c_j(h) := min(l_j h_j, u_j h_j)   (= l_j h_j if h_j ≥ 0, = u_j h_j if h_j < 0),

and let world j maximise ∫_X c_j dμ. On the full domain, a contradiction at {h,−h} scores −2u_j|h_j| at world j.

Then, on the full domain and on every U = D_{K′} (K′ compact convex ⊆ relint K), the auditor's certificate holds, and D_K is covered with strict (G), (IB), transitivity, (C), (LF) and (GC). The covered set includes:
- the COR credal set ν(p⊙[1,k]ⁿ) = {m : m_i/p_i ≤ k·m_j/p_j};
- precise targets (l = u);
- degenerate (lower-dimensional) boxes on the full domain.

*Proof.*
- **Sign.** c_j has the sign of h_j everywhere.
- **(G).** At world j with h_j > 0, the four options score: correct l_j h_j > silent 0 > wrong −u_j h_j > contradiction −2u_j h_j.
- **Bayes sets.** π·c(h) = Σ_j min_{q_j∈[l_j,u_j]} π_j q_j h_j = min_{q∈Q} (π⊙q)·h.
  - So {π·c > 0} = D_{π⊙Q} = D_{ν(π⊙Q)}, which is coherent for every nonzero π ≥ 0.
  - The zero set lies in finitely many hyperplanes {(π⊙q)·h = 0} with π⊙q ≥ 0 and π⊙q ≠ 0, so it is null.
- **Full domain.** π·c(h) + π·c(−h) = −Σ_j π_j(u_j − l_j)|h_j| ≤ 0, so at most one orientation has positive value, and contradictions always lose. The a.e.-unique Bayes act is D_{ν(π⊙Q)}, and (GC) holds.
- **On U.** The Bayes act is U ∩ D_{ν(π⊙Q)} = D_{conv(K′ ∪ ν(π⊙Q))}, which is (GC).
- **Target.** π* = 𝟙 gives D_Q = D_K (and U ∩ D_K = D_K because K′ ⊆ K).
- **(LF).** It holds trivially on the full domain, and on U by P61 A11.
- **Conclusion.** The auditor's §4 argument applies: Lyapunov and Zorn, separation, uniqueness, coherence, the target as unique optimum, and (C) from score equality.
- **COR.** m ∈ ν(p⊙[1,k]ⁿ) iff max_i m_i/p_i ≤ k·min_j m_j/p_j. Its chart sum is Σ_j p_j(h_j⁺ − k h_j⁻): h is desirable iff E_p h⁺ > k·E_p h⁻, which is Walley's constant-odds-ratio criterion. ∎

CHECKED exactly (`fd62_checks.out` §3), for the COR box with p ∝ (1,…,n), k = 2, n = 3, 4, about 4000 random rational (π, h, g) each, with π allowed zeros:
- the identity π·c = min over corners: 0 failures;
- superadditivity (π·c(h), π·c(g) > 0 ⇒ π·c(h+g) > 0): 0 failures;
- both orientations positive: never;
- sign errors: 0;
- target set versus the vertex description of D_K: 0 mismatches in 3000.

The box chart is continuous and piecewise linear with c(h) = M_σh, M_σ diagonal on each orthant σ. So it is a *piecewise-constant local prior*, in O61's words, and it lies in the round-62 ansatz. It is C62's positive control.

### 4.2 Visibility type of corners (CHECKED, `fd62_checks.out` §§2, 4)

For each vertex v, world j is classified by the signs of h_j on the generators of F_v:
- S: strictly visible;
- T: tangential (≤ 0 everywhere, = 0 on some ray);
- A: anti-visible;
- C: crossing.

| target | vertex patterns | P61 "not visible" (no S) | O61 "non-visible from every world" (only A/C) |
|---|---|---|---|
| COR box, n = 3 | AAS, ASA, SAA, ATT, TAT, TTA | 3 | **0** |
| COR box, n = 4 | 4 with one S; 10 with T's and A's | 10 | **0** |
| COR box, n = 5 | 5 with one S; 25 with T's and A's | 25 | **0** |
| reversed triangle | ACC, CAC, CCA | 3 | 3 |
| interior PMM, n = 3, 4, 5 (p ∝ (2,3,…), δ = 1/5, 1/10, 1/10) | one A and the rest C at every vertex | all | all |

General rule (PROVED, from the generators):
- At a box vertex ν(w) with upper set H and lower set L, the face is generated by u_i e_j − l_j e_i (i ∈ H, j ∈ L). So each world in H is tangential when |H| ≥ 2 (strictly visible when |H| = 1), and each world in L is anti-visible.
- At an interior PMM vertex, the generators are u_i𝟙 − e_i (i ∈ H, |H| = n−1). So worlds in H cross and the free world is anti-visible.
- At an interval (PRI) vertex with |H| ≥ 2, every world is non-visible.

**So "sharp corners" is not one notion.** Box corners are not strictly visible (VB fails), but they are weakly visible from every upper-bound world. PMM and reversed-triangle corners are visible from no world. The round-61 exclusions that rely on O61-non-visibility (O61 Lemma 4 and Thm A) apply to PMMs and not to boxes.

### 4.3 Claim-by-claim reconciliation

Each entry gives the round-61 claim, then the domain and ranking actually covered by the proof, then the corrected statement.

1. **ROUND61 §1, "fails at sharp corners … every non-CPM ranking class examined is provably blocked."**
   - Overbroad. The VB construction (P61 V6, two-level sublinear-veto–Brier rankings on a convex one-sided domain, K ⊆ relint Δ) fails when two or more extreme points are not uniformly visible.
   - Sharp corners as such are no obstruction: boxes have 3, 10 and 25 non-visible vertices (n = 3, 4, 5) and are covered (Prop FD-B).
   - Corrected: *"For the reversed triangle, the classes 𝒱_B, 𝒱_conv, E61's concave charts, view-unanimity with target-neutral vetoes and Brier, and one explicit non-concave chart are excluded. Other classes are open."*
2. **"Remaining problem is exactly CPM."**
   - Not proved. O61 §2 leaves translation invariance as a CONJECTURE and shows that real homogeneity is not forced. O61 R2 (stacked signed levels) is a CONJECTURE. E61 Thm 5.1 assumes finite views, each with a non-negative first level and a sign-correct second level, and it is stated for the reversed triangle.
   - Its conclusion is a chart that is *weakly* sign-correct, with D_K a possibly tied Bayes act and coherence of *a.e.-unique* Bayes acts only. The converse needs strict charts with unique coherent Bayes acts for all priors.
   - Corrected: *"Within E61's finite-view architecture, a cover of the reversed triangle forces a chart with properties 5.1(a)–(d), and strict charts with all-priors unique coherent Bayes acts suffice: a sandwich. Rankings outside that architecture are not classified."*
   - The phrase "CPM-type" is not a delimited class: the box chart is itself a chart, a piecewise-constant local prior.
3. **ROUND61 §5, "Open: … the constant-odds-ratio set."**
   - Wrong. The COR credal set is a normalised box, covered by its box chart on the full domain and on every U = D_{K′} with K′ ⊆ relint K.
   - Correct entries: *COR credal set: covered (box chart), not VB-type. Its 2-monotone envelope (core of f∘p): covered by VB-type (P61 I2).*
4. **ROUND61 §2 "Not covered by VB-type: … COR" and §4.1 "COR moves to not covered."**
   - Keep "not VB-type" (REF61 row 14). Delete "not covered" without qualifier.
5. **ROUND61 §2, "normalised boxes … covered separately by L3's box systems on two-sided domains."**
   - Make it precise as Prop FD-B: covered under the current (GC) framework, on the full domain *and* on every one-sided U, by the box chart.
   - L3 and R10a used the older selection axioms. FD-B does not depend on them.
6. **ROUND61 §3, "Convex error levels do not help (O61 Thm B)."**
   - Proved only for the reversed triangle. The general form says at most one all-crossing vertex, and box vertices have no crossing world.
   - The box chart is a 𝒱_conv ranking (no vetoes, convex losses −c_j) that covers boxes.
   - Corrected: *"Convex error levels cannot cover the reversed triangle."*
   - Extending to all interior n = 3 PMM triangles looks routine: the proof uses only the ACC face pattern and the independence of the three rays. CONJECTURE until written out.
7. **ROUND61 §3, "Concave charts are impossible (E61 Cor 5.2)."**
   - For the reversed triangle only, since its κ-system uses the ACC face structure. Concave charts cover every box.
   - Corrected: *"Concave charts (within Thm 5.1's architecture) cannot cover the reversed triangle."*
8. **ROUND61 §3, O61 Thm A ("polytopes with two or more non-visible vertices … not covered").**
   - The hypotheses are: 𝒱_B (vetoes, then an error level −w(h)h_k with *one* weight w for all worlds), a one-sided (LF) domain, K ⊆ relint Δ, and "non-visible" meaning non-visible **from every world** (O61's sense, not P61's).
   - It excludes the reversed triangle and every interior PMM with n ≥ 3 (all vertices A/C, CHECKED), and intervals with two or more vertices having |H| ≥ 2.
   - It says nothing about boxes, whose corners are tangential. The box chart is not in 𝒱_B: its sign- and world-dependent weights cannot be made common unless l = u.
   - Whether 𝒱_B covers boxes is O61's CONJECTURE (two-world tangency). Since FD-B uses a different class, there is no conflict.
9. **O61 R1, "piecewise-constant local priors fail."**
   - CONJECTURE (referee), and for the reversed triangle only. It is false in general: the box chart is a working piecewise-constant local prior.
10. **E61 Cor 5.3 (unanimity) "…even with two-sided domains."**
    - Scope: the reversed triangle; target-neutral vetoes; finitely many finitely additive statistics; a Brier level.
    - The two-sided extension is only CHECKED ("same proof"). Under (GC), Thm FD-1 reduces two-sided domains to the full domain anyway.
11. **F61 full-domain results.**
    - Thm A: convex first levels give boxes only. With FD-B this becomes an exact characterisation: *on the full domain, for K ⊆ relint Δ, worlds refining convex first levels cover exactly the normalised boxes.*
    - Cor B1 (veto-led with Brier gives precise targets only) is correct.
    - Prop E is a *necessary* condition, not a reduction to an equivalent problem.
12. **F61 Thm D, ROUND61 §2 "every requirement holds", §5 "Covered: contaminations (two-sided A_K)."**
    - Covered under (RC) only. Under (GC), A_K is inadmissible for every (G) ranking (§2.1, FD-1a).
    - Also note: T1 and every interior contamination are already globally covered on one-sided U by VB.
13. **F61 "A_K maximal (up to one exempt facet)."**
    - True under (RC). Under (GC) it is superseded by FD-1: the only admissible two-sided domain is the full domain.
14. **ROUND61 §4.2, "the referee's repair covers every zero pattern."**
    - Misdescribed. REF61 §2.6 extends an **exclusion** from VB(K′,A) targets (including Ŵ) to all zero patterns of p (n ≥ 3).
    - Coverage of such contaminations by other rankings is OPEN. They touch ∂Δ, so O61 Lemma 2 and F61 T0 do not apply (escape E3). FD-1 applies when |supp p| ≥ 3, but not when |supp p| ≤ 2, since K then meets an edge.
15. **ROUND61 §2, probability intervals "covered iff each vertex has ≤ 1 coordinate at its upper bound."**
    - Corrected: *by VB-type rankings, for K ⊆ relint Δ, iff all but at most one vertex has |H| ≤ 1* (P61 table, Thm B exemption).
    - "Most n = 4 intervals not covered" means not by VB-type (NUMERICS, 136/150), and not by 𝒱_B when two or more vertices have |H| ≥ 2. Otherwise OPEN.
16. **E61 Prop 6.1 and ROUND61 "every full-dimensional target approximately."**
    - This is Hausdorff approximation by targets each covered on its own domain U_s. It is not coverage of K, and on a fixed domain there is no uniform version (E61 Prop 6.2).
17. **E61 §4.6, "two-sided domains are harder, not easier."**
    - Under (GC) this is now a theorem in a sharp form (FD-1): two-sided means the full domain. "Harder" is target-specific, since boxes and precise targets are covered there.
18. **P61 D1 / O61 Rem 1.1.**
    - Correct, with μ of positive density. Strengthened by FD-1c.

---

## 5. Status of FD62's own results

| Item | Status |
|---|---|
| Auditor's counterexample (x, y, x+y; v_3·y = 1/6 also > 0); robustness radius 5/6, 64 exact corner pairs | CHECKED |
| Lemma W1: on any domain, A ∩ {h_i>0} is undominated under strict (G) alone | PROVED |
| Thm D proves (RC) exactly; X* globally coherent if K ⊆ K*, or if n = 3 and \|W0\| ≥ 2; fails for the world-best models | PROVED; NUMERICS (138/208 failures at \|W0\| = 1; 0/392 at \|W0\| ≥ 2) |
| Thm FD-1 (domain dichotomy under (GC), n ≥ 3, K meets no edge, any (G) ranking) | PROVED |
| FD-1a: A_K, U ∪ −U, and every non-full two-sided domain inadmissible under (GC) | PROVED |
| FD-1b: global two-sided coverage of T1 equals full-domain coverage; there, open only for strictly sign-correct charts | PROVED (reduction); full-domain chart for T1 OPEN |
| FD-1c: lower-dimensional targets under (GC) need the full domain; degenerate boxes and precise targets covered there | PROVED |
| Lemma FD-3: full-domain Bayes acts at prior π are cylinders over supp π | PROVED |
| Prop FD-B: boxes (including COR, precise, degenerate) covered by the box chart, on the full domain and on every U = D_{K′}, K′ ⊆ relint K | PROVED; CHECKED |
| Corner types: boxes T/A/S only (never O61-non-visible); reversed triangle and interior PMMs all A/C | PROVED (generators); CHECKED (n = 3, 4, 5) |
| On the full domain, convex first levels cover exactly the normalised boxes (K ⊆ relint Δ) | PROVED (F61 Thm A + FD-B) |
| O61 Thm B extends to all interior n = 3 PMM triangles | CONJECTURE |

---

## 6. Corrected round-61 status table

Refereed status is as in REF61 and the impossibility referee. "Scope" lists every hypothesis the statement needs.

| # | Result | Scope (precise) | Status |
|---|---|---|---|
| 1 | Covering theorem (auditor; P61 Thm A) | n finite; μ a.c. with finite first moment; K full-dimensional; K′ ⊆ relint K compact convex; A_i ⊆ conv(K′∪e_i) compact; K = conv(K′∪⋃A_i); VB ranking on U = D_{K′}; (GC) holds | PROVED (refereed) |
| 2 | Exact undominated family; one exempt point (P61 Thm B = O61 Thm C) | Same setting; any π* ∈ Δ; K full-dimensional with K′ ⊆ relint K | PROVED (refereed) |
| 3 | Visibility: V1 (strict form), Thm V, V3–V5 | Full-dimensional K; uniform visibility; strict, not tangential | PROVED (refereed) |
| 4 | V6: VB-type targets = all but at most one extreme point uniformly visible | K ⊆ relint Δ; VB-type = two-level sublinear-veto–Brier on a convex one-sided domain | PROVED (refereed) |
| 5 | Covered by VB-type | Interior ε-contaminations; TV balls with δ < min p; belief functions with m(Ω) > 0 and positive singletons; strictly 2-monotone cores with positive singletons (including the COR *core* and strictly convex distortions); smooth K ⊆ relint Δ; every full-dimensional K at n = 2 | PROVED (refereed) |
| 6 | Probability intervals | VB-type iff all but at most one vertex has \|H\| ≤ 1 (K ⊆ relint Δ). Not 𝒱_B if two or more vertices have \|H\| ≥ 2. Otherwise OPEN | PROVED / OPEN |
| 7 | **Normalised boxes, including the COR credal set, precise targets and degenerate boxes** | **Covered** by the box chart on the full domain and on every U = D_{K′} (K′ ⊆ relint K); not VB-type (P61 I6) | PROVED (FD-B, not refereed); exclusion refereed |
| 8 | Pari-mutuel models (interior, n ≥ 3), including the reversed triangle | Not VB-type (P61 I5). Not 𝒱_B on any one-sided (LF) domain (O61 Thm A; all vertices A/C). Exact coverage OPEN (round-62 target) | PROVED / OPEN |
| 9 | Reversed triangle, further exclusions | Not 𝒱_conv (O61 Thm B); not by concave charts within E61 Thm 5.1's architecture (Cor 5.2); not by view-unanimity with target-neutral vetoes, finitely many f.a. levels and Brier on one-sided (LF) domains (Cor 5.3; two-sided CHECKED only); the lower-prevision chart fails at prior (1,2,3) (one chart) | PROVED / CHECKED |
| 10 | Reduction for the reversed triangle | E61 Thm 5.1: finite views, veto then sign-correct level ⇒ weakly sign-correct chart with coherent unique Bayes acts (necessary). The converse needs strict charts and unique coherent Bayes acts at all priors. **Sandwich, not equivalence.** O61 §7: {unique} ∪ {full-support Bayes acts} ⊆ U_L ⊆ {all Bayes acts} | PROVED (sandwich) |
| 11 | General form of rankings | O61 §2: Hausner–Wendel needs homogeneity, which is not forced; translation invariance is a CONJECTURE; stacked signed levels (R2) are a CONJECTURE; piecewise-constant local priors failing for the reversed triangle is a CONJECTURE (false for boxes) | OPEN / CONJECTURE |
| 12 | Lower-dimensional targets | Need two-sided domains (P61 D1, μ positive density; O61 Rem 1.1). Under (GC), n ≥ 3 and K meeting no edge, they need the full domain (FD-1c). Precise targets and degenerate boxes are covered there | PROVED |
| 13 | Full domain (F61 Thm A, Cor B1, Prop E) | K ⊆ relint Δ. Convex first levels cover exactly the boxes. Veto-led with Brier covers only precise targets. Strictly guiding first levels give the necessary condition "a.e.-prior Bayes acts coherent" | PROVED (refereed A/B; with FD-B) |
| 14 | **Contaminations on A_K (F61 Thm D)** | **Relative coherence (RC) only.** Under (GC), A_K is inadmissible for every strictly guiding ranking (auditor counterexample; FD-1a) | PROVED under RC (refereed); fails under GC (CHECKED) |
| 15 | A_K maximality; Cor B2, B3 | Under (RC). Superseded under (GC) by FD-1 | PROVED (RC) |
| 16 | Two-sided domains under (GC) | Only the full domain (n ≥ 3, K meeting no edge, any (G) ranking) | PROVED (FD-1) |
| 17 | T1 on two-sided domains under (GC) | Equals the full-domain problem; open only for strictly sign-correct charts; Lemma FD-3 necessary | OPEN |
| 18 | Contaminations with zeros in p (n ≥ 3) | **Excluded from VB(K′,A) for every zero pattern** (P61 D3 + REF61 §2.6). Coverage by other rankings OPEN | PROVED (exclusion) / OPEN |
| 19 | Dense approximation (E61 Prop 6.1) | Every full-dimensional K ⊆ relint Δ is a Hausdorff limit of exactly covered K_s, each on its own U_s; no fixed-domain version (Prop 6.2) | PROVED (refereed) |
| 20 | Chamfers / truncations / one exact vertex | O61 chamfers need s ≤ 1/2; P61 hexagon needs η < 1/10; N3 | PROVED (refereed) |
| 21 | Scope restrictions from REF61 | Rem B′ only for W0 = Ω (targets in relint Δ); D1 needs positive density; delete "A_K ⊇ D_{K′}" (true if p ∈ K′); O61 Cor A(d): one-world tangency sketched, two-world tangency CONJECTURE (boxes live here, outside 𝒱_B) | as stated |

**Corrected frontier sentence.**
- *Covered (globally):* the VB visibility class; normalised boxes, including the COR set (box chart, one-sided or full domain); precise and degenerate boxes (full domain); interior contaminations (one-sided U).
- *Covered relatively (RC):* contaminations on A_K.
- *Approximately:* every full-dimensional K ⊆ relint Δ.
- *Open:* the reversed triangle and interior PMMs; intervals with two or more |H| ≥ 2 vertices; contaminations with zeros. In each case the open part is outside the excluded classes listed in rows 8–11.
- No conjecture about "non-CPM rankings" is supported, since CPM-type is not a delimited class.
