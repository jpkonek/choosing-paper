# R85b: referee report on the application construction in AUDIT_countable.md (§§4–8)

29 October 2026. Referee R85b. Every line of §§4–8 was checked against the definitions and lemmas of `appshort.tex` and `app_long.tex`. The proofs are given here in full where the note only sketches them. I did not take the note's own claims on trust.

Labels: **PROVED** (proof given or completed here), **CHECKED** (the note's argument is correct as written, perhaps with a small repair noted), **CONJECTURE**, **UNCLEAR**, **FAILS**.

Numerical spot checks are in `r85b_num.py`, with output in `r85b_num_output.txt` and `r85b_inc_check.py`. They are for exploration only. Nothing below depends on them.

---

## 0. Verdict in brief

1. **The mathematics of §§5–8 is correct.** I found no failing step. The repairs needed are minor and are listed in §7 below. The most notable is an unstated compactness step in the claim that G_ε increases to G.
2. **The step the brief singled out is correct** ("Y∖G_ε ⊆ Y∖b_q, so hull monotonicity gives b_q∖Y ⊆ G_ε ⊆ H(Y∖b_q)").
   - H is *increasing* under inclusion of its argument: a larger removed set has fewer supporting states, and so a larger hull.
   - The chain needs two separate facts: monotonicity gives H(Y∖b_q) ⊇ H(Y∖G_ε), and the robust hull inclusion gives H(Y∖G_ε) ⊇ G_ε.
3. **Conflict with the author's standing instruction (flagged plainly).** The ranking accepts only comparisons that strictly raise the integral payoff score m(·)(ω). It is therefore a subrelation of the integral-score ranking, which the author has ruled out (29 Oct).
   - Imprecise coherent models are not valued by this ranking. They are protected only because comparisons are refused.
   - Concretely, the audit's two-world target T is beaten **at every world** in raw score by the precise model D_(1/2,1/2). The ranking refuses that comparison at every world, and the reverse comparison also fails. So T and D_(1/2,1/2) are incomparable everywhere (§6 below).
   - Strict propriety of the integral score is also used essentially in the selection step: δ > 0 because G∩{q>0} is the *unique* q-best set.
   - **As written, the construction does not meet the author's requirement.** Its value now depends on whether R85c can replace the score.
4. **The neighbourhoods are real but very small.** The guaranteed radius always satisfies r ≤ ε/2 (§2.7). For the audit's own two-world pair this gives about 1.6·10⁻⁷ in ρ; for the three-world example, about 7·10⁻⁹.

---

## 1. §5, the ranking

The definition: for a change from X to Y, put A = Y∖X and B = X∖Y. Then Y ≥_ω X iff X = Y a.e., or both

- m(Y)(ω) > m(X)(ω), and
- the change is guided at ω, or A ⊆ H(B) a.e.

### 1.1 Independence on arbitrary sets — CHECKED

Let F and G be disjoint from D. Put X' = (X∩D)∪F and Y' = (Y∩D)∪F.

- The change from Y' to X' adds (X∩D)∖Y and removes (Y∩D)∖X. Neither depends on F.
- X' = Y' a.e. iff (X△Y)∩D is null.
- The score difference is m(A)(ω) − m(B)(ω). Guidance at ω and the clause A ⊆ H(B) depend only on A and B, modulo null sets.

So the verdict is the same with F replaced by G. This is the strong, arbitrary-set form required by the handoff.

### 1.2 World-by-world guidance — CHECKED

If a non-null change is guided at ω, then

    m(A)(ω) − m(B)(ω) = ∫_A |g(ω)| dμ + ∫_B |g(ω)| dμ > 0,

so Y ≥_ω X. The reverse comparison X ≥_ω Y would need the score to rise from Y to X, which is false. So Y >_ω X.

Only (M1) is used. The note's "by (M1)–(M2)" over-cites; this is harmless.

### 1.3 Three-model condition, finite-chain consistency, no ties — CHECKED

Every accepted comparison between distinct models strictly raises m(·)(ω), and identity comparisons are reflexive. Hence along any accepted chain X₀ ≥ X₁ ≥ … ≥ X_k, the score m(·)(ω) never decreases.

- **Chains.** If X_k ≠ X₀, then X_k >_ω X₀ would give m(X_k)(ω) > m(X₀)(ω) ≥ m(X_k)(ω), which is impossible. If X_k = X₀ a.e., the two are tied, so X_k >_ω X₀ fails.
- **Ties.** Distinct models are never tied, so transitivity through ties holds trivially.
- **LDG's (T).** Closure under ties also holds trivially in LDG's sense.

### 1.4 Protection of every almost coherent model — CHECKED, with details supplied

Under (M2), every almost coherent C equals D_Q a.e. for some credal set Q (app_long, Lemma identify(b)). Suppose Y dominates C.

- Since Y ≠ C, every comparison Y ≥_ω C is between distinct models, so m(Y)(ω) > m(C)(ω) **at every world**.
- Put A = Y∖C (disjoint from C) and B = C∖Y (contained in C).
- The clause A ⊆ H(B) does not depend on ω. So it either holds at every world or fails at every world.

**Case 1: A ⊆ H(B), including the pure-removal case A null.**

*Step 1: H(B) ⊆ C.*
- If B is null, then Q_B = S and H(B) = D_S = {g ≩ 0}, which lies in C a.e.
- Otherwise B ⊆ D_Q a.e. Hull lemma (c) gives Q ⊆ Q_B and H(B) ⊆ D_Q = C.

The note says only "H(B) ⊆ C". It omits the null subcase and the use of (M2) to write C = D_Q.

*Step 2: A is null.* A ⊆ C a.e. and A∩C = ∅.

*Step 3: contradiction.* Now m(Y) − m(C) = −m(B), so m(B)(ω) < 0 at every ω. In particular B is non-null.
- Take q ∈ Q. Then q ≥ P_Q ≥ 0 on D_Q, and {q = 0} is null by (M2) applied to {q}. So q > 0 a.e. on B, and q(m(B)) = ∫_B q dμ > 0.
- But m(B) ≤ 0 pointwise, so positivity of q gives q(m(B)) ≤ 0. Contradiction.

No uniform negative bound is needed, so the argument works verbatim for infinite Ω.

**Case 2: A ⊄ H(B).** Acceptance at every world then requires guidance at every world. Lemma guidedeverywhere (app_long) uses the countable set Ω₀ from separability of E. It gives A ⊆ D_S a.e. and B ⊆ −D_S a.e. Every coherent model contains A a.e. and meets B in a null set. Hence A and B are both null, so Y = C, a contradiction.

**Conclusion: PROVED.** All almost coherent models are undominated under this one ranking, for any Ω, with all measurable models evaluable.

---

## 2. §6, the consistent incoherent case

Fix a consistent incoherent X. Put Q = Q_X and G = D_Q. By hull lemma (b) and (M2), X ⊆ G a.e.

### 2.1 δ > 0 — CHECKED

For each q:

- The number ∫_G q⁺ dμ − q(m(X)) is ≥ 0, since ∫_X q dμ ≤ ∫_X q⁺ dμ ≤ ∫_G q⁺ dμ.
- Under (M2), it equals 0 iff X = G∩{q>0} a.e. This is Lemma minimax(b) with H = G.
- G∩{q>0} equals D_conv(Q∪{q}) a.e. (Cor consistent), which is coherent. Since X is incoherent, the gap is positive for every q.

*Continuity.* S is weak-* metrizable (app_long, Lemma states(a)). If q_n → q, then q_n(g) → q(g) for every g, and |q_n(g)⁺| ≤ ‖g‖, which is integrable by (M1). Dominated convergence gives continuity. The minimum over compact S is then positive. This δ is exactly the v of Cor consistent.

### 2.2 The buffer Q_ε — CHECKED, with one repair

*Basic properties.* f_X(q) = ∫_X q(g)⁻ dμ is convex, since r ↦ r⁻ is convex and q ↦ q(g) is affine. It is continuous by dominated convergence, and its zero set is Q_X. So Q_ε = {f_X ≤ ε} is compact, convex and contains Q. It also contains the relatively open set {f_X < ε} ⊇ Q, and ∩_ε Q_ε = Q.

*Repair: G_ε ↑ G.* The note asserts "consequently G_ε increases to G modulo the null boundary". The implication needs an argument.

- **G_ε ⊆ G.** Since Q_ε ⊇ Q, P_{Q_ε} ≤ P_Q.
- **Monotone in ε.** G_ε increases as ε decreases.
- **The union is all of G.** Let P_Q(h) > 0. Suppose P_{Q_ε}(h) ≤ 0 for every ε, and pick q_ε ∈ Q_ε with q_ε(h) ≤ 0. Any weak-* cluster point lies in ∩Q_ε = Q and satisfies q(h) ≤ 0, a contradiction. Gambles h ≩ 0 lie in every G_ε.

So ∪_ε G_ε = G exactly, with no null exception needed. Then e_ε = ∫_{G∖G_ε} ‖g‖ dμ → 0 by (M1) and continuity from above. **PROVED**

### 2.3 The trimming lemma applies; Q_{X∖G_ε} = Q — CHECKED

Let M = max_S f_X. For q ∈ Q and s ∈ S,

    f_X((1−λ)q + λs) ≤ (1−λ)·0 + λM ≤ ε

whenever λM ≤ ε; take λ = min(ε/M, 1/2).

- This gives (1−λ)Q + λS ⊆ Q_ε, so P_{Q_ε} ≤ P_{Q_λ}, and G_ε ⊆ D_{Q_λ}.
- Lemma trim (app_long), with τ = λ and N = G_ε, gives Q_{X∖G_ε} = Q_X.
- If M = 0, then Q = S = Q_ε, and the lemma applies with any τ.

### 2.4 Robust hull inclusion, H(Y∖G_ε) ⊇ G_ε when ρ(X,Y) < a/2 — CHECKED

*The metric.* ρ is a metric on classes modulo null sets because {0} ⊆ {P_Q = 0} is null under (M2).

*The bound a.* Put R = X∖G_ε and K = S∖int_S Q_ε. If K is nonempty, it is compact and disjoint from Q (since Q ⊆ {f_X < ε} ⊆ int Q_ε). For q ∈ K we have q ∉ Q_R = Q, so ∫_R q⁻ > 0. By continuity, a = min_K ∫_R q⁻ > 0.

*Robustness.* Since q(g)⁻ ≤ ‖g‖,

    |∫_{Y∖G_ε} q⁻ − ∫_R q⁻| ≤ ∫_{(X△Y)∖G_ε} ‖g‖ ≤ ρ(X,Y).

So for ρ(X,Y) < a/2, every q ∈ K has ∫_{Y∖G_ε} q⁻ > a/2 > 0. Hence Q_{Y∖G_ε} ⊆ int Q_ε ⊆ Q_ε.

*The inclusion.*
- If Q_{Y∖G_ε} is empty, then H = E.
- Otherwise P_{Q_{Y∖G_ε}} ≥ P_{Q_ε}, so H(Y∖G_ε) = D_{Q_{Y∖G_ε}} ⊇ D_{Q_ε} = G_ε.
- If K is empty, then Q_ε = S and G_ε = D_S ⊆ every hull.

Only Q_{Y∖G_ε} ⊆ Q_ε is needed. The interior is used only to obtain the positive margin a.

### 2.5 Uniform score gap q(m(b_q) − m(Y)) > δ/2 — CHECKED

Here b_q = G_ε∩{q>0}.

- **Lower bound for b_q.** q(m(b_q)) = ∫_{G_ε} q⁺ ≥ ∫_G q⁺ − e_ε, since q⁺ ≤ ‖g‖ on G∖G_ε.
- **Upper bound for Y.** q(m(Y)) ≤ q(m(X)) + ρ(X,Y).

So q(m(b_q) − m(Y)) ≥ δ − e_ε − ρ(X,Y) > δ − δ/4 − δ/4 = δ/2.

The note writes "≥ δ − e_ε − r". It should be ρ(X,Y) in place of r, and the final inequality is strict because ρ < r. This is cosmetic.

**Each b_q is coherent.** It equals D_conv(Q_ε∪{q}) a.e. (Lemma states(c)).

### 2.6 Hull monotonicity, and acceptance of every score-raising comparison from b_q to Y — CHECKED

*Monotonicity.* If B ⊆ B' a.e., then Q_{B'} ⊆ Q_B (hull lemma (a)), so P_{Q_{B'}} ≥ P_{Q_B} and H(B) ⊆ H(B'). If B is inconsistent, then so is B', and H(B') = E. **So H is increasing under inclusion of its argument.**

*The chain.* Since b_q ⊆ G_ε, we have Y∖b_q ⊇ Y∖G_ε. Hence

    b_q∖Y ⊆ b_q ⊆ G_ε ⊆ H(Y∖G_ε) ⊆ H(Y∖b_q).

The third inclusion is §2.4; the fourth is monotonicity.

*Acceptance.* The change from Y to b_q adds b_q∖Y and removes Y∖b_q, so the hull clause holds for every q. Hence b_q ≥_ω Y iff m(b_q)(ω) > m(Y)(ω). This includes pure removals.

### 2.7 A consequence the note does not state: r ≤ ε/2 — PROVED

Suppose K ≠ ∅. Then Q_ε is a proper nonempty closed subset of the connected set S, so it has a relative boundary point q. That point lies in K and satisfies f_X(q) ≤ ε. Since R ⊆ X, ∫_R q⁻ ≤ f_X(q) ≤ ε. Hence a ≤ ε and r ≤ ε/2.

Because f_X grows roughly quadratically off Q, ε must be very small before e_ε < δ/4.

### 2.8 Second consequence: no almost coherent model lies within r of X — PROVED

This is a useful consistency check. Suppose Y is almost coherent and ρ(X,Y) < r.

- Y∖G_ε ⊆ Y, so H(Y∖G_ε) ⊆ Y (§1.4, Step 1). With §2.4 this gives G_ε ⊆ Y a.e.
- For q ∈ Q_Y, the inclusion gives q(m(Y)) = ∫_Y q⁺ ≥ ∫_{G_ε} q⁺ = q(m(b_q)), contradicting §2.5.

The same holds in §7: Y∖U is inconsistent, hence so is Y. So **the incoherent models form a ρ-open set**, and the construction never claims to dominate a coherent model.

### 2.9 Closedness of K_ω(Y) — CHECKED

q ↦ m(b_q)(ω) = ∫_{G_ε} 1{q(g)>0} g(ω) dμ. If q_n → q, the indicators converge off {q = 0}, which is null by (M2) for the credal set {q}. They are dominated by ‖g‖, so the map is continuous by dominated convergence and sequential continuity on metrizable S. Hence K_ω(Y) = {q : m(b_q)(ω) − m(Y)(ω) ≥ δ/2} is closed.

### 2.10 Support coverage on Δ_F — CHECKED

The map θ_F(p) = Σ_{ω∈F} p_ω δ_ω is weak-* continuous, since p ↦ Σ p_ω h(ω) is continuous for each h. It does not depend on the rival.

For q_p = θ_F(p):

    Σ_{ω∈supp p} p_ω [m(b_{q_p})(ω) − m(Y)(ω)] = q_p(m(b_{q_p}) − m(Y)) > δ/2.

So some ω ∈ supp p has a bracket greater than δ/2, that is, q_p ∈ K_ω(Y).

### 2.11 KKM and compactness — CHECKED

- **KKM.** For finite F, the sets A_ω = θ_F⁻¹(K_ω(Y)) are closed and satisfy the face-cover condition. LDG's Lemma kkm gives a common point, so ∩_{ω∈F} K_ω(Y) ≠ ∅.
- **Compactness.** The closed sets K_ω(Y), for all ω ∈ Ω, have the finite intersection property in compact S. So some q* lies in all of them.
- **Dominance.** b_{q*} beats Y by at least δ/2 at every world, so it strictly dominates Y. It is coherent, and it is undominated by §1.4.

This matches the hypotheses of the note's §3, and also LDG's thm:local with F = G and Θ = S. The assigned models lie in C_L.

---

## 3. §7, the inconsistent case — CHECKED

Put h(q) = ∫_X min(q(g), 0) dμ = −f_X(q). It is concave and continuous, and negative everywhere because Q_X = ∅. Its maximum is attained at q₀, with h(q₀) < 0. Put U = {q₀ > 0} and L = X∖U = X∩{q₀ < 0} a.e. (by (M2)).

*Directional derivative.* Put q_t = (1−t)q₀ + tδ_ω ∈ S. The difference quotient of min(q_t(g), 0) is bounded by |g(ω) − q₀(g)| ≤ 2‖g‖, which is integrable by (M1). The pointwise one-sided limit is (g(ω) − q₀(g))·1{q₀(g) < 0} off the null set {q₀ = 0}. Dominated convergence gives

    h'(q₀; δ_ω − q₀) = m_L(ω) − q₀(m_L).

*The bound.* Maximality gives h'(q₀; δ_ω − q₀) ≤ 0, so m_L(ω) ≤ q₀(m_L) = h(q₀) = −d₀ for every ω. This is uniform in ω, and d₀ equals the v of Cor losing.

*The neighbourhood bound.* |m(Y∖U)(ω) − m_L(ω)| ≤ ρ(X,Y). So for ρ < d₀/2,

    sup_ω m(Y∖U)(ω) ≤ −d₀ + ρ < −d₀/2.

This is strict with a uniform constant, which matters when Ω is infinite.

*Inconsistency of Y∖U.* If q were a supporting state of Y∖U, then 0 ≤ q(m(Y∖U)) < −d₀/2.

*The assignment.* c_q = U∩{q>0} equals D_conv{q₀,q} a.e., so it is coherent.
- **Gap.** q(m(c_q)) = ∫_U q⁺ ≥ q(m(Y∩U)), so q(m(c_q) − m(Y)) ≥ −q(m(Y∖U)) > d₀/2.
- **Hull clause.** Y∖c_q ⊇ Y∖U is inconsistent, so its hull is E.
- **Conclusion.** The closedness, coverage and compactness steps of §2.9–2.11 apply verbatim with margin d₀/2.

---

## 4. §8, countability — CHECKED

*An isometric copy.* Let dν = ‖g‖ dμ. This is a finite Borel measure by (M1). The map X ↦ 1_X is an isometry from (models, ρ) into L¹(ν).

*Same null sets.* ν(N) = 0 iff N∖{0} is μ-null. So ν and μ have the same null sets exactly when μ{0} = 0, which (M2) guarantees. Without (M2), ρ would identify X with X∪{0}.

*Separability.*
- E is a separable metric space, so its Borel σ-algebra is countably generated, and L¹(ν) is separable.
- Completion adds no new classes, since every completion-measurable indicator equals a Borel indicator a.e.
- Subspaces of separable metric spaces are second countable, hence Lindelöf.

*Countable subcover.* The ρ-balls of §6 and §7, one around each incoherent X, cover the incoherent models. Countably many suffice. Each retained ball carries one fixed assignment: q ↦ b_q for a fixed (Q_X, ε), or q ↦ c_q for a fixed q₀.

---

## 5. Infinite worlds — CHECKED

- **Metrizability of S.** E is separable (app_long, Lemma states(a), via a dense sequence in the unit ball).
- **Continuity in q.** Every continuity claim in q (δ, f_X, ∫_R q⁻, m(b_q)(ω), m(c_q)(ω)) uses only sequential continuity, pointwise convergence q_n(g) → q(g), domination by ‖g‖ (M1), and (M2) for singleton credal sets.
- **The compact theorem's hypotheses.** With Θ = S, the maps θ_F(p) = Σ p_ω δ_ω and the closed sets K_ω(Y):
  - membership implies b_q ≥_ω Y, because the margin is positive and the hull clause holds;
  - coverage holds for every finite F (§2.10);
  - all-world ties are impossible, since distinct models are never tied.
- **Rival-independence.** The maps θ_F and the space Θ do not depend on the rival, or even on the assignment index.
- **Protection** uses Ω₀ from separability (§1.4).

The proof covers arbitrary Ω, a separable E containing constants, and measures satisfying (M1) and (M2). (M3) is not used anywhere in §§5–8.

---

## 6. The conflict with the author's instruction (29 Oct)

**The ranking is a subrelation of the integral-score ranking.** Every accepted comparison between distinct models strictly raises m(·)(ω). The hull and guidance clauses only delete comparisons that the score would accept. This is exactly the "strictly proper scoring rule" architecture the author has ruled out.

**Imprecise models are protected only by incomparability.** Numerical evidence, with exact Gaussian ray integrals plus stratified balls:

| Target | Raw score of target | Precise model with higher score | Its score | Margin at every world |
|---|---|---|---|---|
| Two-world T = {g₁+3g₂>0, 3g₁+g₂>0} | (0.25231, 0.25231) | D_(1/2,1/2) | (0.28209, 0.28209) | ≥ 0.0298 |
| Three-world contamination target, a = 0.2 | ≈ (0.1886, 0.1886, 0.1887) | D_uniform | ≈ (0.2303, 0.2304, 0.2304) | ≥ 0.0416 |

In both cases B = T∖D_p is null and A = D_p∖T ⊄ H(∅) = D_S. A also contains gambles that are negative at each world. So the ranking refuses D_p ≥_ω T at **every** world; T ≥_ω D_p fails too, because the score is lower. T survives only because the ranking leaves it incomparable with a model that beats it everywhere on the score.

**The selection step uses strict propriety.**
- δ > 0 (§2.1) rests on G∩{q>0} being the *unique* maximizer of q-expected integral score.
- The assigned models b_q and c_q are q-Bayes sets of the integral score, restricted to G_ε or U.

Replacing the score by a commission-averse, non-strictly-proper ψ (R85c's task) could break δ > 0 wherever the ψ-Bayes sets within G fail to be unique or coherent.

**What is independent of the score.** The buffer Q_ε, the trimming step, the robust hull inclusion (§2.4), hull monotonicity, and the countability argument (§4) are coherence and measure geometry. They do not use the payoff score. Only δ, e_ε and the gap in §2.5 do. This is the part R85c must replace.

**Verdict.** The construction is mathematically sound but **non-compliant**. It should not be presented to the author as meeting his requirement.

---

## 7. List of repairs (none fatal)

| # | Location | Issue | Status |
|---|---|---|---|
| 1 | §5 guidance | Cites (M1)–(M2); only (M1) is needed. | cosmetic |
| 2 | §5 protection | "H(B) ⊆ C" needs (M2), to write C = D_Q a.e., and the null-B subcase H(∅) = D_S. | supplied in §1.4 |
| 3 | §5 definition | "A ⊆ H(B)" should read "a.e." | cosmetic |
| 4 | §6 buffer | "G_ε increases to G" needs the compactness argument P_{Q_ε}(h) → P_Q(h). | supplied in §2.2 |
| 5 | §6 gap | "≥ δ − e_ε − r" should read "> δ − e_ε − ρ(X,Y)". | cosmetic |
| 6 | §6 | The sentence "Y∖G_ε ⊆ Y∖b_q, so hull monotonicity gives b_q∖Y ⊆ G_ε ⊆ H(Y∖b_q)" merges two facts. Monotonicity of H (increasing in its argument) gives H(Y∖b_q) ⊇ H(Y∖G_ε); the robust inclusion gives ⊇ G_ε. | correct; clarify |
| 7 | §6 | Unstated: a ≤ ε, so r ≤ ε/2 (tiny neighbourhoods). Also unstated: no coherent model lies within r. | added in §2.7–2.8 |
| 8 | §7 | The bound should be stated with the sup over ω: sup_ω m(Y∖U)(ω) ≤ −d₀ + ρ. This makes the strict inequality uniform in infinite Ω. | supplied in §3 |
| 9 | §8 | Relies on μ{0} = 0, from (M2), for ρ to separate classes. | noted |

---

## 8. Numerical spot checks (exploration only)

**Method.** Standard Gaussian μ. Cone integrals of 1-homogeneous integrands are computed exactly by ray quadrature: 4·10⁴ rays in two worlds, 6·10⁴ in three. Small balls are handled by stratified grids. Supporting-state sets are computed from the support on a state grid: 1001 states in two worlds, 11 239 in three (refined near Q_X).

**Two worlds, the audit's pair X = T ∪ E (round 83).** Sanity check: m(T) = 0.252307 against the exact κ·2/√10 = 0.252313.

- **Supporting states.** Q_X has q₁ ∈ [0.358, 0.642].
- **Parameters.** δ = 0.01864, attained near q = (0.508, 0.492). ε = 3.3·10⁻⁷, giving e_ε = 0.00450 < δ/4.
- **Trimming.** Q_{X∖G_ε} = Q_X on the grid.
- **Radius.** The computed a = 4.2·10⁻⁷ is a grid overestimate; §2.7 gives a ≤ ε, so r ≤ 1.6·10⁻⁷.
- **Gap.** min_q q(m(b_q) − m(X)) = 0.0176 > δ/2 = 0.0093.
- **The common point.** It is q* = (1/2, 1/2), with margins (0.0176, 0.0176).
- **The dominator.** Since q* ∈ Q_ε, b_{q*} = G_ε, with credal set q₁ ∈ [0.351, 0.649]. It is imprecise, contains T, and keeps 91.3% of E. Dropping part of E is exactly what round 83's copy lemma requires. Its hull clause was verified.
- **Perturbations inside r.** Six random perturbations (toggling tiny balls) all pass: the gap, the hull inclusion, a nonempty intersection of the K_ω, and A ⊆ H(B).
- **Larger perturbations.** Fifteen with ρ up to about 10⁻³, far outside r, also pass with the same assignment.

**Two worlds, inconsistent X = T ∪ (ball of negative gambles).**
- **Maximizer.** q₀ ≈ (0.239, 0.761), with h(q₀) = −0.00987.
- **Derivative bound.** At the coarsest ray resolution, the bound m_L(ω) ≤ q₀(m_L) is violated by 1.6·10⁻⁵. The violation shrinks to 1.8·10⁻⁶ and then 7·10⁻⁸ as the rays are refined (`r85b_inc_check.py`). It is a discretization effect: rays on {q₀ = 0} carry mass, which (M2) excludes. Finite-difference directional derivatives are ≤ 0 throughout.
- **Perturbations.** All pass: Y∖U is inconsistent, m(Y∖U) < −d₀/2, and the K_ω have a nonempty intersection.

**Three worlds, contamination target M = {q_i ≥ 0.2} plus three patches** (handoff §8.2: balls of radius 0.2 at the permutations of (−1.5, 1, 1)).
- **Parameters.** X is consistent, with δ = 0.0403. ε = 1.7·10⁻⁸, giving e_ε = 0.0078 < δ/4.
- **Trimming** holds on the grid.
- **Radius.** a = 1.4·10⁻⁸ ≤ ε, as predicted, so r = 7·10⁻⁹.
- **Gap.** min_q gap = 0.0399 > δ/2.
- **The common point.** It is q* ≈ (0.33, 0.34, 0.33), with all three margins about 0.04. A ⊆ H(B) holds.
- **Perturbations.** All tiny and larger perturbations pass.
- **A grid warning.** A coarser state grid (step 1/60) first produced a false trimming failure, with a = 0: Q_ε and Q_X coincided on the grid. Refining the grid near Q_X removed it.

---

## 9. Summary by brief item

| Brief item | Status |
|---|---|
| 1. Independence; world-by-world guidance; three-model condition, chains, no ties | CHECKED |
| 1. Protection of every almost coherent model, including pure removals and infinite Ω | PROVED (details supplied) |
| 2. δ > 0 | CHECKED |
| 2. Buffer Q_ε | CHECKED, with the G_ε ↑ G step supplied |
| 2. Trimming lemma applies | CHECKED |
| 2. Robust hull inclusion | CHECKED |
| 2. Uniform gap | CHECKED |
| 2. Acceptance of score-raising comparisons; the hull-monotonicity sentence | CHECKED (H is increasing in its argument; the direction is right) |
| 2. Closedness; coverage; KKM and compactness | CHECKED |
| 3. Derivative at q₀; uniform bound; neighbourhood bound | CHECKED |
| 4. Separability and countable subcover | CHECKED (uses μ{0} = 0) |
| 5. Weak-* metrizability; dominated convergence; compact-theorem hypotheses with Θ = S | CHECKED |
| Compliance with the 29 Oct instruction | **FAILS**: the ranking is a subrelation of the integral-score ranking, imprecise targets survive only through incomparability, and the selection step uses strict propriety. |
