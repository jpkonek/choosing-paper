# PP30. Surgery on the additive precise system S_0

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full proof here. CHECKED: exact rational computation of proof bookkeeping on atoms (cells). Cells say nothing about (S). NUMERICS: floating-point illustration; no proof depends on it. CONJECTURE / OPEN: as stated.

**Scripts** (`r9/PP30_py/`; run `python3 -I -B <script>`; outputs in the `.out` files; all end ALL PASS):

| Script | Content | Label |
|---|---|---|
| `kill_exact.py` | Theorem 3.2 bookkeeping: 364 (p, ε) configurations, exact rationals | CHECKED |
| `kill_mc.py` | Theorem 3.2 with genuine balls and Gaussian μ: every v_w > 0 by > 4 s.e. | NUMERICS |
| `zonoid_lp.py` | Prop 3.4: kills inside thin and outer parts of Sil(T); segment targets (Remark 3.6) | NUMERICS |
| `ans_rigidity.py` | (a) T is the unique S_0-Bayes answer on Ans(T) for every m ∈ M; (b) Lemma 5.3 | CHECKED / NUMERICS |

**Inputs.** Brief 47; AUDIT_selected_realizability §2 (S_0) and §4; AUDIT_answers47; PP19 (Lemma 0.2, Theorem 1, Theorem 5); PP23 §4 (Lemma 4.1, inverted departures); LEAD_selection_count (Lemmas A, B); AUDIT_completion; REFEREE_Z_PP19 (Lemma H). Only Brief 47's axioms are used. Each result says which ones it uses.

---

## 0. Verdict

**Short answer: obstruction.** No surgery of S_0 can keep S_0's comparisons outside a neighbourhood of T's fibre. In fact no system can keep S_0's comparisons for even **one** precise model, at any index, vertices included. The obstruction is not local to p_0, and it uses no closed sections. It comes from S_0's verdicts on records that live inside T's silent cone. The nearby result that can be reached is a surgery in **problem space**, not index space. Keep S_0 on records supported where T answers, and redesign the records that meet T's silence. Its forced geometry is determined below.

| Question | Answer | Where | Source of obstruction |
|---|---|---|---|
| Lead's observation | **Correct.** Strengthened: wherever kept precise models accumulate, the limit model is that precise model and it inherits S_0's strict acceptances. | Prop 2.1, Lemma 2.2 (PROVED) | kept comparison + sections + strict (G) |
| Q1/Q2: index collar and gluing | **None exists.** For every p ∈ Δ, T1's competitiveness forces a world w at which the retreat D_p[G → S] is no worse than D_p. Then D_p must refuse there its own tiny w-improved retreats, which S_0 accepts. This holds for every G inside T's silence, and S_0 contradicts it for an explicit G (two small balls). | Thms 3.1, 3.2, Cor 3.3 (PROVED; CHECKED; NUMERICS) | **kept comparison + axioms** ((IB), strict (G), (TC), T competitive). No sections, no geometry. |
| Which additive bases survive | A rank-weighted additive base on Sil(T) survives the kill for D_p iff some λ ∈ Δ makes D_p's answers λ-no-better than silence on Sil(T). This never holds for S_0's weights \|g_w\|. It always holds for balanced weights, which have no room. | Prop 3.4, Remarks 3.5–3.6 (PROVED) | kept comparison |
| Q3: lost dominators | For every p, the rivals Z = D_p[G → S, E → w-correct] lose D_p as dominator. Every new dominator is a selected coherent C ≠ D_p that differs from Z on an **unbounded** set. So no bounded record, and in particular no inverted departure, can re-dominate them. Dominators stay at positive distance from every index where D_p is selected. | Prop 4.2 (PROVED) | **axioms** (KKM, direct (C), Lemma H) |
| Non-additivity spreads | At the refusal world, every small strict worsening of D_p must be kept from being strictly below the retreat. That is a whole family of non-S_0 verdicts. | Prop 4.1 (PROVED) | axioms + kept comparison |
| Shifted aim: S_0 kept on records supported in Ans(T) | (a) T's competitiveness is never refuted by (TC) chains of guidance links and kept links. (b) Every selected model is S_0-Bayes on Ans(T). Hence it is **precise, or a refinement D_K of T (K ⊆ M)**. Edge indices carry precise models from their own edge. PP20's coarsenings are excluded. (c) Every comparison between distinct selected models meets Sil(T), so the kept part decides none of them. | Thms 5.1, 5.2, Lemma 5.3, Cor 5.4, Prop 5.5 (PROVED) | kept comparison + competitiveness (forced geometry, not chosen) |
| Q4: additivity ledger | §6 | | |

**What I recommend.** Replace "index-space surgery" by "Ans(T)-kept surgery". The selected family must then consist of precise models and refinements of T (Cor 5.4); this is forced, not chosen. All the remaining work is on records that meet Sil(T). The first concrete test is who dominates the vertex rivals V_1[G → S, E → w-correct] (§7).

---

## 1. Setting and notation

Brief 47's setting applies: three worlds; problems g ∈ R³ modulo sign; μ Gaussian; the full four-advice domain; models modulo null sets. Ranks are correct 0, silent 1, wrong 2, contradictory 3. Coherent models are D_K for compact convex K ⊆ Δ; D_K accepts g iff m·g > 0 for all m ∈ K. T = T1 = D_M, with M = c·1 + εΔ, c = (1−ε)/3, centre u = (1/3,1/3,1/3).

**S_0** (audit §2). L_w(X) = ∫ |g_w| r_w(X, g) dμ, and X ⪯_w Y iff L_w(X) ≤ L_w(Y). C_p = D_p. The **S_0 value** of a record r = (D, a, b) at w is ∫_D |g_w| (r_w(b) − r_w(a)) dμ. S_0 accepts r at w iff its value is ≥ 0. For every p ∈ Δ, D_p is the unique a.e. minimiser of Σ_w p_w L_w (audit §2).

**T's two regions.** Sil(T) := {g : min_M m·g < 0 < max_M m·g} (T silent) and Ans(T) := its complement, up to null sets (T answers). Since c·1·g = c Σg, the extremes are min_M m·g = cΣg + ε min_w g_w and max_M m·g = cΣg + ε max_w g_w. Sil(T) is an open cone. It contains every g ≠ 0 with Σg = 0 (the plane u^⊥), and it contains no unanimous problem.

**Kept.** A system *keeps S_0 on a class 𝒦 of records* if, at every world, each record in 𝒦 carries its S_0 verdict. The obstruction in §3 needs much less: only that three particular records with **positive** S_0 value are accepted.

**The objects of §3.** Fix p ∈ Δ and a bounded non-null G ⊆ Sil(T). D_p answers a.e. on G. For a world w and a non-null E ⊆ G, define:
- X_{p,G} := T[G → D_p] (T with D_p's answers on G);
- R_{p,G} := D_p[G → S] (D_p retreating to silence on G);
- Y^w_E := T[E → w-correct];
- Z^w_{p,G,E} := R_{p,G}[E → w-correct] = D_p[G → S, E → w-correct].

Write s_p(g) := sign(p·g), and

  v^p_w(G) := ∫_G g_w s_p(g) dμ,  𝒢_p := {G : v^p_w(G) > 0 for w = 1, 2, 3}.

Note that |g_w|(1 − r_w(D_p, g)) = g_w s_p(g): it is +|g_w| where D_p is w-correct and −|g_w| where D_p is w-wrong.

**Record identities (PROVED; CHECKED in `kill_exact.py`).** Each line is a single record:
- rec(T, X_{p,G}) = rec(R_{p,G}, D_p) = (G, S, D_p);
- rec(X_{p,G}, Y^w_E) = rec(D_p, Z^w_{p,G,E}). Its support is (G∖E) ∪ (E ∩ {D_p not w-correct}), its old side is D_p, and its new side is S on G∖E and w-correct on E;
- rec(Y^w_E, T) = rec(Z^w_{p,G,E}, R_{p,G}) = (E, w-correct, S).

So by (IB), each comparison among T, X, Y has the same verdict as the corresponding comparison among R, D_p, Z.

**S_0 values (PROVED, direct computation).**
- R_{p,G} ⪯_w D_p has value −v^p_w(G).
- D_p ⪯_w Z^w_{p,G,E} has value v^p_w(G) − ∫_E |g_w| dμ.
- Z^w ≺_w R_{p,G} is strict guidance.

---

## 2. The lead's observation

**Proposition 2.1 (lead's naive surgery fails; PROVED — the lead's argument, checked).** Suppose C_{p_0} = T, and C_p = D_p carries S_0's verdicts for p ≠ p_0. Then (S) fails at p_0.

*Proof.*
- Σ_w p_{0,w} L_w(D_{p_0}) < Σ_w p_{0,w} L_w(T), by unique minimisation. So L_i(D_{p_0}) < L_i(T) for some i.
- When p_0 = u, both T and D_u are invariant under permuting worlds. So L_i(D_u) < L_i(T) at **every** i.
- Take X := Y^i_E, with E ⊆ Sil(T) so small that L_i(D_{p_0}) < L_i(X) < L_i(T).
- By dominated convergence L_i(D_p) → L_i(D_{p_0}). So D_p ⪯_i X near p_0, and the closed section gives T ⪯_i X.
- But X ≺_i T by strict (G). ∎

The lead's reading is also correct: selected models near Φ_T must refuse at i every X ≺_i T (PP19 Theorem 1).

**Lemma 2.2 (rigidity where kept precise models accumulate; PROVED).** Uses strict (G), closed sections and S_0's verdicts out of the D_{p_n}. Let p_n → p with C_{p_n} = D_{p_n}, each carrying S_0's verdicts. Then:
- C_p = D_p;
- C_p ⪯_w X at every world w, for every X with L_w(X) > L_w(D_p).

*Proof.* Put Y := C_p.
- **Each L_w(Y) ≤ L_w(D_p).** Suppose L_w(Y) > L_w(D_p) at some w. Then Y is not w-perfect. Fill a small non-null E ⊆ {Y not w-correct} with the w-correct answer to get X, with L_w(D_p) < L_w(X) < L_w(Y).
  - For large n, L_w(D_{p_n}) < L_w(X), so D_{p_n} ⪯_w X.
  - The closed section then gives Y ⪯_w X, against X ≺_w Y.
- **So Y = D_p.** Summing, Σ p_w L_w(Y) ≤ Σ p_w L_w(D_p). Unique minimisation gives Y = D_p a.e.
- **Inheritance.** The second claim is inheritance through the same sections. ∎

So any surgery needs a non-kept region with interior around Φ_T, as the lead said. §3 shows the non-kept region must be everything.

---

## 3. The obstruction: no precise model can keep S_0's verdicts

**Theorem 3.1 (T-mimicry is forced on every precise model; PROVED).** Uses only reflexivity, strict (G), (IB) and (TC), together with T competitive at all three worlds. This holds whenever T is selected, because by Lemma E its index is interior. Let p ∈ Δ, and let G ⊆ Sil(T) be bounded and non-null. Then there is a world w = w(p, G) such that:
- (a) R_{p,G} ⪯_w D_p, and T ⪯_w X_{p,G};
- (b) D_p ⋠_w Z^w_{p,G,E} for every non-null E ⊆ G.

*Proof.*
- (a) T is competitive against X_{p,G}, so T ⪯_w X_{p,G} for some w. By the first record identity this is R_{p,G} ⪯_w D_p.
- (b) Y^w_E ≺_w T by strict (G). If X_{p,G} ⪯_w Y^w_E held, then T ⪯_w X_{p,G} ⪯_w Y^w_E ≺_w T would violate (TC). So X_{p,G} ⋠_w Y^w_E, and the second record identity turns this into (b). ∎

In words: at the world where T accepts D_p's answers on G, the precise model D_p must rank **no better than its own retreat to silence on G**. It must also refuse every retreat on G improved at w on any piece E. Inside T's silence, every precise model has to behave like T at some world, separately for each piece G.

**Theorem 3.2 (S_0 contradicts this at every index; PROVED; CHECKED; NUMERICS).** For every p ∈ Δ, 𝒢_p ≠ ∅. For G ∈ 𝒢_p, S_0 refuses (a) at every world, with value −v^p_w(G) < 0. For each w and every non-null E ⊆ G with ∫_E |g_w| dμ < v^p_w(G), S_0 accepts the comparison that (b) refuses.

*Proof.* The S_0 values are those in §1. It remains to construct G ∈ 𝒢_p.
- **The direction.** Put g_p := (p − u) × 1 if p ≠ u, and g_u := (1, −1, 0). Then g_p ≠ 0, g_p ⊥ 1 and g_p ⊥ p. Since its coordinates sum to 0, it has coordinates of both signs.
- **The centres.** Fix 0 < t < ε · min(max_w g_{p,w}, −min_w g_{p,w}) and set h± := ±g_p + t·1.
- **Silence.** For m = c·1 + εδ ∈ M, m·h± = 3ct + ε(t ± δ·g_p). So min_M m·h± = t + ε min_w(±g_p)_w < 0 < t + ε max_w(±g_p)_w = max_M m·h±. Hence h± ∈ Sil(T).
- **D_p's answer.** p·h± = t > 0.
- **The balls.** Sil(T) and {p·x > 0} are open. Choose r ∈ (0, t/2), and closed balls B± around h± of radii at most r, inside both sets, disjoint (also modulo sign), with μ(B+) = μ(B−) =: m > 0. Equal masses are possible by continuity of the radius. Put G := B+ ∪ B−.
- **The estimate.** On G, s_p = +1 and x_w ≥ h_w − r. Hence v^p_w(G) ≥ m(h+_w + h−_w − 2r) = 2m(t − r) > 0 at every w.
- **The set E.** Since μ is atomless, a non-null E ⊆ G with ∫_E |g_w| dμ < v^p_w(G) exists. ∎

CHECKED (`kill_exact.py`):
- with atoms in place of balls, the 91 points p of the 1/12-grid (vertices, edges, centre) for each ε ∈ {1/10, 3/10, 1/2, 9/10};
- each h± is strictly silent under T; D_p accepts it; v = 2t·1;
- the three record identities hold;
- for every world and both atom choices of E: S_0 accepts D_p ⪯_w Z^w, Y^w is a strict w-improvement of T, and T ⪯_w X has S_0 value −v_w < 0.

NUMERICS (`kill_mc.py`, real balls, Gaussian μ): all v_w > 0 by more than 4 standard errors, at 28 grid points and ε ∈ {0.1, 0.3, 0.6}.

Example, ε = 3/10, p = e_1 (the vertex model V_1): h+ = (0.15, −0.85, 1.15) ∈ M_2 and h− = (0.15, 1.15, −0.85) ∈ M_3. V_1 gives the majority answer on both. That answer is wrong at world 2 on the first ball and at world 3 on the second, and the two balls cancel those errors in S_0's |g_w|-weighting.

**Corollary 3.3 (no surgery keeps S_0 anywhere; PROVED).** Uses (IB), strict (G), (TC), and T1 competitive at all worlds. No such system agrees with S_0 on all the comparisons **out of** a single precise model D_p, for any p in the closed simplex. Whether D_p is selected does not matter. For a vertex model V_k, the comparisons involved are at its two other worlds; at world k they are guidance.

Indeed, take G ∈ 𝒢_p. Theorem 3.1(b) says some world refuses a record out of D_p, chosen with E small, that S_0 accepts at every world. In particular:
- no surgery keeps S_0's comparisons at the indices outside a neighbourhood of Φ_T;
- the selection need not be continuous for this, sections are not used, and no geometry near T is involved.

**Classification.** The obstruction comes from *optional kept comparisons* (S_0's verdicts on three retreat-records out of D_p, inside Sil(T)) combined with the *axioms* (IB), strict (G), (TC) and T's competitiveness. The axioms alone force only Theorem 3.1. That is a statement about every (S)-system selecting T1, and it is not a contradiction. Nothing comes from a chosen geometry.

**Proposition 3.4 (which additive bases survive; PROVED).** Let a world-indexed rank-weighted base be ℓ_w(g, a) = h_w(g) r_w(g, a), with h_w > 0 integrable. Let R ⊆ Sil(T) be a measurable cone. Call G ⊆ R a *kill* if the three records of Theorem 3.1(b), for small E, all have positive ℓ-value. Then a kill inside R exists iff there is **no** λ ∈ Δ with

  (Σ_w λ_w h_w(g) sign(g_w)) · s_p(g) ≤ 0 for a.e. g ∈ R.

For S_0 (h_w = |g_w|), the condition reads (λ·g)(p·g) ≤ 0 a.e. on R.

*Proof.* The ℓ-value at w of D_p ⪯_w Z is ∫_G h_w sign(g_w) s_p dμ − (small).
- **Convexity.** The set {(∫_G h_w sign(g_w) s_p dμ)_w : G ⊆ R} is the range of a finite atomless vector measure. By Lyapunov it is convex, and it contains 0.
- **Separation.** It misses the open positive orthant iff some λ ∈ Δ has λ·v ≤ 0 on it. That happens iff the integrand λ-combination is ≤ 0 a.e. on R. ∎

**Second proof that S_0 always has a kill.** Suppose (λ·g)(p·g) ≤ 0 on the open set Sil(T) ⊇ u^⊥ ∖ {0}.
- **On the plane.** Restricted to the plane u^⊥, the two linear forms have product ≤ 0 everywhere. So they are negatively proportional, or one of them vanishes on u^⊥.
- **A common zero.** In every case some g ∈ u^⊥ ∖ {0} is a zero of both. When both forms vanish on u^⊥, any g works. Otherwise take the zero line of the non-vanishing one.
- **Contradiction.** Since λ·1 = p·1 = 1, we get (λ·(g + t1))(p·(g + t1)) = t² > 0 for small t ≠ 0, while g + t1 ∈ Sil(T).

NUMERICS (`zonoid_lp.py`, LP on sampled directions, 45 grid points p):
- kills exist inside the thin core {|cos(g, 1)| ≤ 0.05} of Sil(T);
- kills also exist inside the outer shell (|cos| at least half its maximum on Sil(T)), at every grid p and ε ∈ {0.1, 0.3, 0.6}.

So the records that must change are not confined near u^⊥.

**Remark 3.5 (balanced bases escape, and have no room).** Suppose there is λ with Σ_w λ_w h_w sign(g_w) ≡ 0 on Sil(T). An example is PP23's weights: 2 on the world's own minority class and 1 elsewhere, with λ = u. Then Prop 3.4 gives no kill for any p.

These are exactly the bases under which T's silence is λ-Bayes on Sil(T). By the same Lyapunov argument, such a base is **equivalent** to T being competitive against every rival that differs from T only on Sil(T), through acceptances the base endorses (value ≥ 0).

Balance forces λ to be interior: on Sil(T) ∩ M_k the identity needs λ_k > 0. Hence every endorsed all-world domination between regular models differing only on Sil(T) has value **zero** at every world. The base therefore cannot drive any domination there. Compare PP23 Prop 3.2 and Lemma 4.1.

S_0 sits at the other extreme: its weights kill T against **every** precise model. Neither extreme works. The verdicts out of precise models inside Sil(T) must be non-additive, or additive for a field that is neither S_0-like nor balanced. Prop 3.4 is the exact test for any proposed field.

**Remark 3.6 (other targets; PROVED; NUMERICS).** The proof of Theorem 3.2 uses only an interior point k of K in place of u, with g ∈ k^⊥ ∩ p^⊥.
- **K with nonempty interior.** The theorem holds for every D_K competitive at all worlds. No precise model escapes.
- **Segments K = [a, b].** The escaping p are exactly the points of Δ on the line ab outside the open segment. There λ = the far endpoint certifies Prop 3.4. Every other p has a kill: off the line by the construction above, inside the open segment by Prop 3.4. LP agrees at 91/91 grid points.
- **Precise targets.** No kill; their silence is null.

So the obstruction attaches to the two-dimensionality of T1's credal set, not to T1's position.

**Scope.** Theorem 3.1 needs T competitive at all three worlds. On the tie route (T unselected), it applies to a selected tie partner D_K whenever K has interior (Remark 3.6). A **precise** tie partner of T escapes this mechanism; that case is OPEN.

---

## 4. What must change, and the rivals that lose their dominators (Q1, Q3)

By Theorem 3.1, for every p and every G ⊆ Sil(T) (bounded, non-null), one world w(p, G) carries:
- (i) R_{p,G} ⪯_w D_p, a comparison **into** D_p, refused by S_0 when G ∈ 𝒢_p;
- (ii) D_p ⋠_w Z^w_{p,G,E} for all E, comparisons **out of** D_p, accepted by S_0 for small E.

At the other worlds S_0 may stay. D_p's competitiveness against R_{p,G} and against Z can use any other world in supp p, where S_0's positive values accept. For V_k, w(p, G) is one of the two non-own worlds.

(i) and (ii) fit a total preorder at w: R_{p,G} ⪯_w D_p (a tie, or D_p worse), and Z ≺_w R_{p,G} by guidance. S_0 instead has D_p strictly better than R_{p,G} at w. Locally this is easy. The difficulty is that it is needed for every p and every G simultaneously.

**Proposition 4.1 (non-additivity spreads at the refusal world; PROVED).** Uses (TC) and strict (G). Let G ∈ 𝒢_p and w = w(p, G). Let D′ be a strict pointwise w-worsening of D_p with S_0-size η := L_w(D′) − L_w(D_p) < v^p_w(G); for example, contradiction on a small set. Then **not both** D′ ⪯_w R_{p,G} and R_{p,G} ⋠_w D′ hold. S_0 gives both, with values v_w − η > 0 and η − v_w < 0. So at w the pair (D′, R_{p,G}) cannot keep its S_0 order, for every such D′.

*Proof.* R ⪯_w D_p ⪯_w D′ by Theorem 3.1(a) and guidance. (TC) then forbids D′ ≺_w R. ∎

This is PP23's tiny-worsening collapse (Lemma 4.1), with T's forced acceptance as the negative-value record.

**Proposition 4.2 (lost dominators and certificates; PROVED).** Assume full (S) with direct (C). Let G ⊆ Sil(T) be bounded, w = w(p, G), E ⊆ G non-null, and Z := Z^w_{p,G,E}.
- **(a) Z needs a new dominator.** Z is incoherent, by Lemma H: it differs from the coherent D_p exactly on a bounded set, which is non-null because otherwise Z = D_p and (b) of Theorem 3.1 would contradict reflexivity. So it is strictly dominated by some selected coherent C: KKM gives C_q ⪯_v Z at all v, and an all-world tie would make Z coherent by direct (C). Also C ≠ D_p, since D_p ⋠_w Z. In S_0, D_p dominates Z whenever G ∈ 𝒢_p and E is small. So these rivals **lose** their S_0 dominator.
- **(b) The new record is unbounded.** {C ≠ Z} has non-null parts outside every ball. Hence rec(C, Z) is never a bounded record, and in particular never an inverted departure. **Incoherence certificates of PP23's bounded kind cannot supply these dominators.**
- **(c) The dominator is away from D_p.** If C_{q*} = D_p (for instance q* = e_k for V_k), then q* has a neighbourhood containing no index of a dominator of Z.

*Proof.*
- (a) As stated, using KKM and direct (C) as in AUDIT_completion §5.
- (b) {C ≠ D_p} is a non-null cone, since both models are coherent. A non-null cone has non-null parts outside every ball (REFEREE_Z_PP19 §2). Off the bounded set G, Z = D_p.
- (c) A_w(Z) is closed and does not contain q*. ∎

**Answer to Q3.**
- **Which rivals lose their dominators.** At least, for every p and every G ∈ 𝒢_p, the w(p, G)-improved retreats Z^w_{p,G,E} (E small). These are forced by the axioms; the list is not specific to a surgery. Any further losses depend on how the remaining records meeting Sil(T) are re-decided.
- **Re-domination.** Their dominators must differ from them on unbounded sets and must avoid D_p's selection points. The bounded inverted-departure certificates of PP23 §4.2 cannot dominate them directly. They can still help indirectly: Lemma 4.4 still blocks pumps, as in Theorem 4.5. Whether unbounded dominators can be installed without breaking (TC) is OPEN. The vertex case is the first test (§7).
- **What does not conflict.** T dominating its own inverted rivals T·d (AUDIT_answers47 item 4) does not conflict with Theorem 3.1. Those records have old side S and incoherent new side, so no record of Theorem 3.1 copies onto them. Lemma 0.2 then only requires T·d to refuse at every world all Y ≺_w T. This is not checked here against triangle completions with the forced acceptances (i).

---

## 5. The nearby reachable aim: surgery in problem space

The obstruction lives entirely on records meeting Sil(T). So the natural shift is to keep S_0 exactly on the records supported in Ans(T) and redesign the rest. Call this **Ans(T)-kept**.

**Theorem 5.1 (no (TC)-chain kills T; PROVED).** Uses strict (G), (TC) and Ans(T)-kept verdicts. Take any model X, and for each world w a chain

  X = Y⁰ ⪯_w Y¹ ⪯_w ⋯ ⪯_w Yⁿ ≺_w T.

Suppose each weak link is either guidance (pointwise ≤_w) or a kept record (supported in Ans(T)). Suppose the strict link is strict guidance, or kept in both directions. Then such chains cannot exist at all three worlds for the same X. In particular, (TC) applied to such chains never refutes T's competitiveness.

*Proof.*
- **On Sil(T).** Kept links do not change advice there, and guidance links only worsen at w. Hence Yⁿ ≥_w X pointwise on Sil(T). The strict link forces Yⁿ ≤_w T = S on Sil(T). So X ∈ {S, w-correct} on Sil(T).
- **X = T on Sil(T).** This holds for all three w, and Sil(T) contains only mixed problems, so X = S there.
- **On Ans(T).** Every link is now a guidance link or a kept link, and both raise L_w weakly. So L_w(X) < L_w(T) at every w, with X − T supported in Ans(T).
- **Contradiction.** On Ans(T), T = D_m for every m ∈ M, and it is the unique S_0-Bayes answer there. Hence Σ m_w (L_w(X) − L_w(T)) ≥ 0. ∎

CHECKED (`ans_rigidity.py` (a)): uniqueness of T's S_0-Bayes answer at 20,000 random rational g ∈ Ans(T), for 24 points m of M.

Theorem 3.2 is exactly such a chain, with a kept link out of D_p **inside** Sil(T). Theorem 5.1 says that removing the kept Sil(T)-records removes every kill of this kind. It says nothing about kills that use other forced links, such as competitiveness of other selected models or protection rules.

**Theorem 5.2 (Ans-rigidity; PROVED).** Uses competitiveness and Ans(T)-kept verdicts. Let C_q be selected.
- If q is interior, there is λ ∈ Δ with C_q = D_λ a.e. on Ans(T).
- If supp q = {i, j}, the same holds with λ ∈ [e_i, e_j].

*Proof.* Rivals differing from C_q only on Ans(T) give kept records. Competitiveness says that their vectors of S_0 values (ΔL_w)_{w ∈ supp q} never lie in the open negative orthant.
- **Convexity.** Over measurable modifications on Ans(T), these vectors form a convex set (Lyapunov/Aumann).
- **Separation.** Some λ ≥ 0, supported in supp q, satisfies Σ λ_w ΔL_w ≥ 0 for all of them. Pointwise, C_q minimises Σ_w λ_w |g_w| r_w(g, ·) a.e. on Ans(T).
- **Uniqueness.** The minimiser is unique off the null plane λ^⊥, and it is D_λ's answer. ∎

**Lemma 5.3 (PROVED; NUMERICS).** For coherent D_K and λ ∈ Δ: D_K = D_λ a.e. on Ans(T) iff K = {λ}, or K ⊆ M and λ ∈ M.

*Proof.* Lines in the plane of Δ correspond to planes g^⊥. "g ∈ Ans(T)" means the line misses M. D_K and D_λ disagree on an open set of such g iff some line missing M strictly separates a point of K from λ.
- **λ ∈ M.** Any k ∈ K ∖ M can be strictly separated from M by a line, so we need K ⊆ M. Conversely, K ⊆ M gives D_K = T = D_λ on Ans(T).
- **λ ∉ M and k ∈ K, k ≠ λ.** Pick x on the open segment (k, λ), close to λ, with x ∉ M. The lines through x that miss M form a nonempty open set of directions. Any such direction other than that of the segment gives a line separating k from λ. So K = {λ}. ∎

NUMERICS (`ans_rigidity.py` (b)): 400 random (K, λ), in five cases, all as predicted.

**Corollary 5.4 (forced geometry of an Ans(T)-kept system; PROVED).** Every selected model is one of the following:
- at an interior index, **precise** (D_λ, any λ), or a **refinement of T** (D_K with K ⊆ M, K ≠ ∅), T itself included;
- at an index on [e_i, e_j], a precise D_λ with λ ∈ [e_i, e_j];
- at a vertex, V_k.

This geometry is forced, not chosen. Two consequences:
- **Excluded models.** Every non-precise credal set not inside M is excluded from selection. This includes PP20's coarsenings conv(M ∪ {q_w}), and any K with K ⊄ M that is not a singleton.
- **The collar near Φ_T.** It consists of refinements of T and precise models. Precise boundary selections become forced in this version, although audit item 5 rightly does not require them in general.

**Proposition 5.5 (the kept part decides no inter-model comparison; PROVED).** In an Ans(T)-kept system, any two distinct selected models differ on a non-null part of Sil(T).
- **Two refinements.** They agree with T on Ans(T).
- **A refinement and a precise model.** The refinement is silent on part of Sil(T); the precise model answers there.
- **Two precise models D_λ ≠ D_λ′.** Take x on (λ, λ′) and m ∈ int M off the line λλ′. The line through x and m crosses the segment transversally and cuts M. Nearby lines do too.

So every record between selected models, every KKM domination of a rival that differs from its dominator on Sil(T), and every comparison at a junction of fibres is decided by the redesigned part.

**Q2 in this form.** The gluing is along the boundary of the cone Sil(T), not along a curve in the simplex. At a junction of a refinement fibre with a precise fibre, closed sections for fixed rivals constrain only comparisons that meet Sil(T) (Prop 5.5). The one fact forced from both sides is the audit's: constant models C approaching a boundary index p force C_p ⪯_w C at every world, so C_p ≈ C when C is undominated. Ties between a refinement and a precise model are coherent–coherent ties on a conic set. Lemma H and direct (C) allow them. No obstruction found; OPEN.

Lemma 2.2's argument does not carry over. Every rival that is fixed while selected models vary meets Sil(T) in its record with them, unless the models are constant there.

---

## 6. Additivity ledger (Q4)

| Comparisons | Status | Reason |
|---|---|---|
| Records supported in Ans(T) | **May be S_0.** No (TC)-chain kill (Thm 5.1). Keeping them forces Cor 5.4. | PROVED |
| Records out of every precise D_p inside Sil(T) | **Must deviate from S_0** at one world per G ∈ 𝒢_p (Thm 3.1(b), Thm 3.2), for every p including the vertices | PROVED |
| T's acceptance of X_{p,G}, i.e. R_{p,G} ⪯_w D_p | **Non-S_0** (negative value at every world when G ∈ 𝒢_p); forced at one world | PROVED |
| Pairs (D′, R_{p,G}), D′ a small worsening of D_p | **Non-S_0** at w(p, G) (Prop 4.1) | PROVED |
| Records out of D_p inside Sil(T) under another rank-weighted field | Allowed iff Prop 3.4's λ-condition holds. Balanced fields always pass, but they make T's silence Bayes and leave no room (Remark 3.5). | PROVED |
| Dominations of the lost rivals Z | **Unbounded records** from a coherent C ≠ D_p (Prop 4.2). Whether they can be additive under some field is OPEN. | PROVED / OPEN |
| Comparisons between distinct selected models in an Ans(T)-kept system | Free: all meet Sil(T) (Prop 5.5). Additive or not is a design choice. | PROVED |

---

## 7. Status, and the next step

**PROVED here:**
- the lead's observation and its rigidity form (Prop 2.1, Lemma 2.2);
- the axiom-level T-mimicry of every precise model (Thm 3.1);
- the S_0 contradiction at every index (Thm 3.2, Cor 3.3);
- the exact test for additive bases (Prop 3.4) and its extension to other targets (Remark 3.6);
- the spreading (Prop 4.1) and the lost dominators (Prop 4.2);
- for the Ans(T)-kept aim: no chain kill (Thm 5.1) and the forced geometry (Thm 5.2, Lemma 5.3, Cor 5.4, Prop 5.5).

**Not done:** a construction. No (S)-system selecting T1 is produced, and the Ans(T)-kept aim is not shown consistent.

**OPEN:**
1. **Vertex test.** For Z = V_1[G → S, E → w-correct], with G ∈ 𝒢_{e_1} and w ∈ {2, 3} the refusal world: find a selected coherent dominator at positive distance from e_1, through an unbounded record. Check its triangle completions against R_{e_1,G} ⪯_w V_1 and against the copies of Theorem 3.1 at nearby precise indices.
   - A natural candidate is D_λ with λ on [e_1, e_w′] (w′ the non-refusing world), at a rival-dependent distance from e_1. At world 1 it must accept a large loss on the cone between λ^⊥ and e_1^⊥ in exchange for a bounded gain on G. That is non-additive at world 1, and so not an S_0 comparison.
2. **Maximal keepable class.** Is Ans(T)-kept the largest class of records on which S_0 can be kept? Prop 3.4 and the LP show kills in every part of Sil(T) for every p. But keeping S_0 on Sil(T)-records that belong to no kill has not been examined.
3. **Precise tie partner.** The tie route with a precise tie partner of T (end of §3).
4. **Refinements.** Whether refinements K ⊊ M must actually be selected near Φ_T, or whether precise models can meet T's fibre directly in an Ans(T)-kept system. Nothing kept forces either (Prop 5.5).

**For the record.** Theorem 3.1 is a property of every (S)-system selecting T1, independent of S_0: *each precise model, at some world, ranks no better than its own retreat to silence on any piece of T's silence.* I think it is the right lens for the next round. It makes the co-design problem of Brief 47 concrete at every index, including the vertices, without fixing any geometry near T.
