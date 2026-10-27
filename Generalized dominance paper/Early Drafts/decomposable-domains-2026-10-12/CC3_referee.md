# CC3. Referee report on BB2_notes.md (M3.9 in full), incorporating AUDIT_BB's repair

17 Oct 2026, round 31. This is an adversarial, independent reading of BB2 §§1–8 against the write-up (§4 analytic chain;
§5 setting), M3 §§5–6 with M23_referee §6, D1 with D1_referee, Q4 §3 with Q24_referee §2, N21 §3, N23_referee §7 and
N28 §3. Every lemma of BB2 was re-derived, not read. The imported analytic lemmas of write-up §4 were also re-derived;
§7 below lists which. NUMERICS: `cc3ref_py/` (run `python3 -I cc3_checks.py` inside it). The BB2 script was rerun with
`python3 -I` and its output is identical to the stored one (`cc3ref_py/bb2_rerun.out`). No verdict rests on numerics.

---

## 0. Verdict

**M3.9 is CORRECT once one repair is made: AUDIT_BB's Lemma 2.0, "every Bayes model at a weight q ∉ E is coherent".
I verified that repair. It is needed in more places than the audit names, and one insertion covers all of them. I
found no gap that touches the mechanism.**

Beyond the audit's gap I found:
- one false clause, which is unused: the δ-clause of Lemma 2.6(a);
- one correction to the record that overclaims: correction 3 says "false" where the note shows only "not established";
- five cosmetic points.

The consequence holds on every decomposable domain with (LF), at the status of its other inputs (§8):

> no ranking whose worlds all add up covers T1 (Q4.2, which contains M3.10 and M3.10′).

| Item | Verdict |
|---|---|
| **Audit gap** (Lemma 2.2(a): (H3) is applied on a ray) | **GAP (fixable), confirmed.** The audit's repair is CORRECT. It is also needed in 2.1(d), 2.2(b), 2.2(d), 2.3, 2.4(a) and Def 4.0. Fix: insert Lemma 2.0 (§1) |
| 2.1 tie anatomy (a)–(e) | CORRECT |
| 2.2 (a) | GAP, closed by Lemma 2.0. An alternative direct fix is given in §1 |
| 2.2 (b)–(e) | CORRECT (given Lemma 2.0) |
| 2.3 exact charts | CORRECT. The second bullet needs one extra line when R(g) = ∅ (§2) |
| 2.4 vertex continuity, UVN | CORRECT. This re-derives Q4.0(a) and Q4.3 |
| 2.5 (0), (a)–(d) | CORRECT, including the silence caveat |
| **2.6(a), ♭-clause** | CORRECT |
| **2.6(a), δ-clause** | **WRONG** as stated: it fails on a non-null set of g at off-E points of their chart lines. It is **unused**; delete it (§2) |
| **2.6(b), (c)** (E inside B; exact quasi-linearity of P♭) | **CORRECT** |
| 2.7 (W1)–(W5) | CORRECT |
| **2.8(a)** (sign-pattern lemma), 2.8(b) | **CORRECT** |
| Prop 3.1 (P1)–(P8) | CORRECT. Wording of (P7) (§3) |
| **3.3(a), (b)** | CORRECT. One line is missing in (a): the case x ∈ ∂H⁺ |
| **3.3(c)** (thin zero sets at every point of B, E included) | **CORRECT** |
| 3.4 (c-clusters) | CORRECT |
| **Thm 3.2** Steps 1–6 | **CORRECT** |
| **Thm 3.2** Step 7 (transfer of the analytic lemmas) | **CORRECT.** Read literally, the write-up's sandwich proof needs continuity at one endpoint. The half-plane form of the levels gives the exact bound without it (§3.4) |
| Cor 3.5 (crossing rows, corner equation, vector cluster) | CORRECT |
| Def 4.0 (a)–(f); generic segments | CORRECT |
| **Lemma 4.1** (walls across chords, with the D1_referee open-chart Step 1) | **CORRECT.** Cosmetic: in Step 3 the collar widths must tend to 0 (§4) |
| **Thm 4.2** (cluster walls Ẑ_v; generic segment; two first-point searches) | **CORRECT** |
| **Lemma 4.3** (R23.1 for K♭ by a clopen argument) | **CORRECT** |
| **§5** (5.1–5.7, the TSalways cascade) | **CORRECT.** Cosmetic constant in 5.6 |
| Thm 6.1, Cor 7.1 | CORRECT at the input status listed in §8 |
| Corrections to the record 1, 2, 4 | CORRECT |
| Correction 3 | CORRECT in substance. **GAP (wording):** "false globally" is asserted without an example; replace it by "not established" (§6) |

---

## 1. The audit gap and its repair

### 1.1 The gap, confirmed and located

(H3) gives coherence of the q-Bayes model only for q in a full-measure set 𝒢 ⊆ Ω ∖ E. Lemma 2.2(a) takes
q_m = q + s_mδ ∉ E on a fixed ray, which is a null set, and asserts "these Bayes models are coherent by (H3)". That does
not follow.

The same unproved fact, coherence of the unique Bayes model at an **arbitrary** q ∉ E, is also used silently in:
- 2.1(d), "the Bayes model at q_n ∉ E";
- 2.2(b) and (d), "K_q for q ∉ E";
- 2.3, "for q ∉ E the unique Bayes model is D_{K_q}";
- 2.4(a), "D_{K_q} off E";
- Def 4.0, the sets K_{q_n} with q_n ∉ E.

Outside BB2 it is used in M3.7, M3.8, Q4.1 Step 3 and D1.1(a). Every later lemma inherits it.

### 1.2 The repair (AUDIT_BB), verified

> **Lemma 2.0.** Under (H1)–(H3), for every q ∈ Ω ∖ E the a.e.-unique pointwise q-optimum X_q is a model of 𝓜 and is
> coherent: X_q = D_{K_q} a.e.

*Proof (checked step by step).*
1. **Margin.** For a.e. g the q-optimum is unique, with margin μ_q(g) > 0, and env(g) < ∞.
   - If |q′ − q|₁ < μ_q(g)/(2 env(g)), the q′-optimum on g is the same advice.
   - So for q_n → q, the q_n-optimum differs from X_q only on {μ_q ≤ 2|q_n − q|₁ env} ∪ Z_{q_n}.
2. **Approximating weights.** 𝒢 has full measure, so it is dense. Take q_n ∈ 𝒢 with q_n → q.
   - Then Z_{q_n} is null.
   - The first set in step 1 decreases to the null set {μ_q = 0} ∪ {env = ∞}.
   - μ is finite, so Bayes(q_n) → X_q in measure.
3. **Coherence.** Each Bayes(q_n) is coherent by (H3). By [I2] the coherent class is closed in L¹, so X_q = D_K a.e.
   for some credal set K.
4. **Membership.** X_q ∈ 𝓜 by [I1]. ∎

Placed before Lemma 2.1, Lemma 2.0 uses nothing from §2, so there is no circularity. With it, 2.2(a) holds verbatim:
the ray meets E countably, and every q_m ∉ E now has a coherent Bayes model.

The repair is already on record in two places:
- B2_referee, Lemma 1, cosmetic repair 2: "off E the Bayes model is coherent: it is a limit in measure of generic Bayes
  models";
- D1_referee §1(a).

So BB2 should cite it. D1 itself is not affected.

*Alternative direct fix of 2.2(a).* Take q_m := q + s_mδ_m ∈ 𝒢 with s_m ↓ 0 and δ_m → δ, which is possible because 𝒢
has full measure in every cone around the ray.
- For a.e. g tied at q, every tie vector v has v·q = 0 and v·δ ≠ 0. So v·q_m = s_m v·δ_m eventually has the sign of
  v·δ.
- So Bayes(q_m) → D^δ_q pointwise a.e.

This avoids Lemma 2.0 in 2.2(a). Lemma 2.0 is still needed for the other uses listed above. NUMERICS (5): the advice
mismatch fraction scales linearly in |q_n − q|.

---

## 2. Foundations (§2)

**2.1: CORRECT.**
- (a)
  - Two distinct great circles meet in two m_c-null points, so only countably many carry positive m_c-mass.
  - q ↦ q^⊥ is injective on Ω.
  - μ(Z_q) ≤ m(q^⊥).
  - Ties with × are unanimous and never lie on q^⊥ for q ∈ Ω.
- (c)
  - Generic t ∈ E lies on exactly one atom line. Tied differences in any other direction have mass
    ≤ m_c(t^⊥) + m_a(t^⊥ ∖ {±b′}) = 0.
  - Tied advices stay tied along ℓ′, and the untied ones stay worse off {μ_t ≤ C|q − t| env}.
  - Hence μ(Z_q) → μ(Z_t) > 0 along ℓ′.
- (d)
  - On each open side the tied values κ_{aa′} b′·q are pairwise distinct, so the side-minimiser a^±(g) is unique.
  - Each X_n has its own exceptional null set, and the union of these is null.
  - Convergence is pointwise a.e., hence Hausdorff by [I2].
- (e) Signs, re-derived: c(g) and d(g) have pattern σ(g), and c′(g) has pattern −σ(g). NUMERICS (1): 0 failures in
  20 000 instances. So a tie vector ∝ ±b′ forces σ(g) = ±σ′.
- "Generic" excludes C₀, i.e. the pencil points D1_referee flagged, because C₀ ⊆ C_E.

**2.2 (b)–(e): CORRECT (given Lemma 2.0).**
- (b)
  - For a tie with a, the directions θ not choosing +g contain an open half-circle, so the dense Θ meets them.
  - ⋂_θ D_{K^θ} differs from D_{K♭} only on {P_{K♭} = 0}, which is null.
  - An a.e. inclusion D_{K₁} ⊆ D_{K₂} gives P_{K₂} ≥ P_{K₁} by level shifts, hence K₂ ⊆ K₁.
- (c) Every cluster set K\* satisfies D_{K\*} ⊇ D♭_q a.e., so K\* ⊆ K♭_q, which gives lower semicontinuity.
- (d) The estimate uses |m|₂ ≤ 1 on Δ.
- (e)
  - The δ-accept set is ⋂_a ({q·v_a > 0} or {q·v_a ≥ 0}), and the type of each half-plane is fixed by sign(δ·v_a).
  - The ball B′ around g₀ − t′𝟙 is a.e. accepted at q, so B′ ⊆ cl D_{K^F_q} and P^F(q, g₀) ≥ t′.

**2.3: CORRECT.**
- (q, g) ↦ P♭(q, g) is lower semicontinuous in q and 1-Lipschitz in g, hence Carathéodory and jointly Borel, so Fubini
  applies.
- Two open convex planar sets that agree a.e. are equal.
- *Second bullet, one line to add.* If q₀ ∈ C := {P^δ(·, g) > 0}, then K^δ_{q₀} is the Hausdorff limit of K_{q₀+s_mδ}
  along off-E points (2.2(a) and [I2]). So P(q₀ + s_mδ, g) > 0 for large m, and q₀ ∈ cl R(g).
  - This covers R(g) = ∅, where the a.e. argument alone fails because a null convex set need not be empty.
  - The same line justifies the P^δ part of the "Robustness" remark of §3.1.

**2.4: CORRECT.**
- (a) The vertex margin bound is as Q24_referee checked it.
- (b) (LF) gives the ball around x in D_{V_l} for x_l > 0 and its complement for x_l < 0. P_{V_l}(x) ≤ −s follows by
  the level shift x + s𝟙. Uniform convergence on bounded sets finishes.
- This independently re-derives Q4.0(a) and Q4.3. Q4.3 now has two readings.

**2.5: CORRECT.**
- (0) X_{e_i} accepts g iff accepting g is available and g_i > 0. A cone that a.e. contains N ∩ {g_i > 0} contains
  ℝ₊(N ∩ {g_i > 0}).
- (c)
  - The Fubini-over-δ step needs the set of directions that choose −h to be non-empty. In the triple tie it is
    {θ·c′ > 0, θ·d < 0}. This is empty only if c′ − λd ∈ ℝ𝟙 with λ > 0, which the strict pattern −σ of c′ − λd
    excludes.
  - The dichotomy "W(h) = ∅ or int W(h) ≠ ∅" is the same fact. NUMERICS (2): 15 013 nonempty cells, 0 thin.
  - The a.e. set of h does not depend on q, because W(h) is a fixed polyhedron. That is what makes the conclusion hold
    "for every q".
- (d) Strong acceptance, strong rejection and strong silence each pin the advice for every K within ω/2 of T1. The
  remaining directions shrink to the compact set S² ∩ (∂D_{T1} ∪ −∂D_{T1}), which lies inside the open set 𝒞 ∪ −𝒞.

**2.6(a): ♭-clause CORRECT; δ-clause WRONG (unused).**
- The ♭-clause is 2.3 combined with 2.5(c).
- The δ-clause asserts g ∈ D_{K^δ_q} whenever c(g)·q = 0 and δ·c(g) > 0, for good g and **every** q ∈ B. It is false:
  - Take g that is not an atom gamble and whose chart line meets B. That line meets E ∩ B countably (2.6(b)).
  - At an off-E point q₀ of the line, K^δ_{q₀} = K♭_{q₀}. So the ♭-clause gives g ∉ D_{K^δ_{q₀}}, while the δ-clause
    asserts g ∈ D_{K^δ_{q₀}}.
  - Such g with δ·c(g) > 0 form a non-null set (replace δ by −δ if necessary).
- What is true is the pointwise statement about the *model* D^δ_q, which agrees with D_{K^δ_q} only a.e. at each q.
- The clause is cited nowhere else (grep: line 358 only). **Fix: delete it.**

**2.6(b): CORRECT.**
- 𝒞 ∩ −𝒞 = ∅, because P_{K″}(h) + P_{K″}(−h) ≤ 0, so the identity μ(Z_q) = m_𝒞(q^⊥) involves no double counting.
- An atom chord of m_𝒞 through p\* would put p\* ∈ E.
- A line through p\* meets each atom chord at most once.

**2.6(c): CORRECT.**
- Both halves were re-derived. The mirror half takes t′ ∈ (max_i P♭(q_i, g₀), t) and a ball B′ outside every
  cl D_{K♭_{q_i}} and inside D_{K♭_q}.
- The condition g₀ − t′𝟙 ∈ 𝒞 holds for t′ near t because 𝒞 is open, and c̄ < η/√3 keeps h^k(τ) − t𝟙 ∈ int N₀.

**2.7: CORRECT.**
- (W1) y·(w′ + z) ≥ 0 for z ∈ v^⊥ small, and |Proj_{v^⊥} y| ≥ c|y| on 𝟙^⊥ since v·𝟙 = 1.
- (W2) The decomposition h = w″ + (v·h)𝟙 has |w″ − w| ≤ (1 + √3) rad U. The third claim uses v′·w″ > 0 on the compact
  set F_k ∩ cl Ũ.
- (W3) is pure duality.
- (W4) An open convex set containing a dense subset of an open set contains that set.
- (W5) Two vectors h(σ₁), h(σ₂) spanning v_k^⊥ give m ∈ ℝv_k ∩ aff Δ, so m = v_k.

**2.8: CORRECT.**
- (a) The ingredients are: v, v′ independent; W + ℝn = W; W connected; cl O_σ ∩ cl O_{−σ} = {0}. NUMERICS: the BB2
  checks (1), (5) were rerun and agree.
- (b) The pattern change happens in exactly one coordinate, so σ₂ ∉ {σ₁, −σ₁}.

---

## 3. The local chain under (TS) (§3)

### 3.1 Prop 3.1: CORRECT
- (P7) should read "uniform for τ in compact subsets of {τ : h(τ)_l > 0}, respectively {τ : h(τ)_l < 0}". Every use is
  of this form.
- (P2) uses K♭_{p\*} = T1, which holds because p\* ∉ E.

### 3.2 Lemma 3.3: CORRECT
- **(a)**
  - Separating the open convex set A_τ ∩ B from its convex complement gives A_τ ∩ B = H⁺ ∩ B exactly.
  - In "A_τ ⊆ H⁺ globally", the case x ∈ A_τ ∩ ∂H⁺ needs one line. A_τ is open, so it also contains points strictly on
    the far side, and the hull argument then applies.
  - The hull of x and a point y ∈ H⁺ ∩ B near p\* crosses ∂H⁺ inside B, so it meets B ∖ cl H⁺.
- **(b)** If B_τ ∩ B ≠ ∅ lay in a line L′, then {Ψ ≥ 0} ∩ B ⊇ B ∖ L′. Its convex hull is B, which contradicts (P4).
  Separation then gives H⁻ ∩ B ⊆ B_τ ∩ B ⊆ cl H⁻.
- **(c)** I checked each step.
  - The two lines through p\* coincide, because the open half-discs are disjoint.
  - Z_τ ∩ B ⊆ λ_τ.
  - Ψ = 0 at off-E points of λ_τ ∩ B, by (P5).
  - B_τ ∩ λ_τ ∩ B is convex (P4) and lies in the countable set E ∩ λ_τ ∩ B (P6). So it has at most one point.
  - Its complement in λ_τ ∩ B is {Ψ ≥ 0} ∩ λ_τ ∩ B, which is convex, because A_τ ∩ λ_τ = ∅. An open interval minus
    one point is not convex.
  - **So Z_τ ∩ B = λ_τ ∩ B at every point, points of E included.** This needs only lower semicontinuity, exact
    quasi-linearity on B, and the countability of E on lines through p\*. All three are in place.

### 3.3 Lemma 3.4 and Theorem 3.2, Steps 1–6: CORRECT
- **3.4**
  - On A_τ ∩ B: P♭(q, h) > 0, so g_m ∈ D_{K♭_q} and ĉ·q ≥ 0.
  - On int(B_τ ∩ B): ĉ·q ≤ 0.
  - ĉ is not ∝ 𝟙.
  - So ĉ·p\* = 0 and {ĉ > 0} = H⁺_τ.
  - The vertex sign follows from c(g_m)_i < 0.
- **Step 1** A line through p\* and e_l would cut V_l ∩ Ω.
- **Step 3**
  - The pairwise intersections come from V_j on (0, τ_j) and from V_i on (τ_i, 1).
  - Farkas on the wedges gives n_τ ∈ cone(n_σ, n_σ′).
  - Betweenness inside an open half-circle gives monotone angle.
- **Step 4**
  - On W and on −W the one-sided limits in τ give Ψ ≥ 0 and Ψ ≤ 0. Ψ(q, ·) is concave and finite, hence continuous.
  - (P4) turns the double wedge into a disc.
  - This contradicts (TS_A).
  - Continuity at τ₀ itself follows from betweenness.
- **Step 5** If n is constant on [a, b], then Ψ(q, ·) = 0 on [a, b] along λ (3.3(c)), so Ψ(q, ·) ≤ 0 (caps(a)). This
  forces λ_τ = λ for all τ, which contradicts the vertex signs on both sides of τ_i. The glued angle is strictly
  monotone, and λ_{τ_i} = lin(p\*, e_i).
- **Step 6** Every step is pointwise in q. Caps(a) at the test point gives Ψ^k(q, 0) < 0 inside the disc where
  P♭(·, r) = 0.
- The "A-half only" claim for Steps 1, 3 and 4 is right. Lemma 5.1 needs it.

### 3.4 Step 7: transfer of the analytic lemmas: CORRECT, with one corrected justification

I re-derived each imported lemma for Ψ = P♭(·, h(τ)) on B, using only (P1)–(P8) and 3.3(c).

- **Sandwich.** The write-up proves the upper bound from "D⁺(s₁) < f(q) with s₁ > s\*\* := xr/(r − |y|)". Without
  continuity in q, that literally yields only f(q) ≤ D⁺(s\*\*+), and P♭ can jump across atom chords on the axis.
  - The exact bound still holds. By (P3), (P4) and separation, {f > t} ∩ B = H_t ∩ B with H_t an **open** half-plane,
    so B ∖ H_t is a closed half-plane intersected with B.
  - Suppose f(q) > t > D⁺(s\*\*). The closed half-plane contains the open chord λ ∩ B and the apex p\* + s\*\*n. Hence
    it contains the closed triangle they span, and q lies on that triangle's edge. But q ∈ H_t: contradiction.
  - The lower bound is the mirror argument with apex q.
  - Monotonicity of D⁺ uses the same half-plane form at levels t ∈ (0, c̄); (N2) keeps every relevant level ≤ c̄.
  - NUMERICS (4): lower-semicontinuous jump profiles with the pencil at distance ≥ r, including points placed exactly
    at jump preimages: 161 094 points, 0 failures.
  - BB2's table entry is right. Its justification should cite the closed-half-plane form, not continuity.
- **Caps (a)–(c).**
  - (a) and (b) are standard concavity facts.
  - (c): a difference quotient is continuous at (q₀, τ₀) as soon as Ψ is jointly continuous at (q₀, τ₀) and
    (q₀, τ₀ − s). So upper semicontinuity of ∂⁻ holds **at** a point q₀ ∉ E, even when the approaching points lie in E.
- **Rotation.**
  - The approaching anchors q_{τ₀}(ξ) lie on λ_{τ₀}, so Ψ(q_{τ₀}, τ₀) = 0 at every point (3.3(c)).
  - Also Ψ(q_{τ₀}, σ) > 0 for σ slightly > τ₀, since n_σ·u_{τ₀} = sin(θ_σ − θ_{τ₀}) > 0 and A_σ ∩ B = H⁺_σ ∩ B.
  - Caps(b) is pointwise.
  - Caps(c) and joint continuity are used only at the limit anchor q_{τ₁}(ξ) ∉ E. Such a ξ exists by (P6), one per τ.
  - 0 < S⁺ ≤ S⁻ < ∞ follows from the strict sign change at τ₁, which uses (TS) at all σ near τ₁.
- **Risingsun.** If L_* ≤ 0 on (a, b], then the upper left Dini derivative of −θ is ≥ 0 everywhere. For continuous
  functions this makes −θ nondecreasing, which contradicts strict increase.
- **Regularity (a)–(d).**
  - (a) Risingsun points, rotation, then sandwich (exact, as above), then concavity in τ (pointwise).
  - (b) Lebesgue's theorem; θ′ = 0 is excluded via (a).
  - (c) Rotation with L_* = L^*.
  - (d) Sandwich at scale t.
- **Blow-up.**
  - Equi-Lipschitz in τ: concavity plus the bound (a), pointwise in q.
  - Property (M) follows directly from the half-plane levels. A level line separating p\* + tδ from p\* + tδ′ cannot
    cross λ ∩ B, so it is within angle O(t/r) of λ.
  - Sweep and window use only (M), the Lipschitz bound in τ, and θ′ ∈ (0, ∞) on E′. I re-derived the jump bound
    J ≤ 6Lε/ϑ + o(1).
  - Arzelà–Ascoli is applied on a countable dense set. (M) extends the limit to every δ, so no continuity in q is
    needed.
- **Twoslope.**
  - Concavity of a·δ on the open cone C_J makes a a difference of concave functions, hence locally Lipschitz.
  - Continuity of n puts the density of a″ in −ℝ₊n.
  - d(a × a′) = a × a″ = 0.
  - L_a = 0 would force n′ = 0, so L_a ≠ 0. Then β/α is constant, and m_a = 0.
- **PCNS.** Two positively proportional affine maps with non-constant direction differ by a constant factor. I checked
  this in a basis {a₀, a₁}. The patching and the rank-2 claim follow.
- **Boxbridge (a), (b); corner algebra.**
  - Re-derived: r₁₂ = (−1, −1, κ+1) with κ + 1 = (2+ε)/(1−ε).
  - Proportionality holds iff x₁ + 1/x₂ = κ+1. φ is hyperbolic, so φ³ has the fixed points x± only.
  - NUMERICS (3a): 0 failures in 10 000 tests. (3b): the exact quadratic of M³, 0 failures in 5000 values of κ.
  - The normalisation p\* = u rescales the **penalties** (p\* ⊙ ℓ), not the gambles, so T1 and the domain are fixed.

**Corollary 3.5: CORRECT.**
- (d): normalised vectors with the same zero line and orientation in aff Δ are equal, because aff Δ spans ℝ³.
  Uniformity follows by contradiction.

---

## 4. Walls across chords (§4)

**Def 4.0: CORRECT.**
- (a) diagonal argument.
- (b) continuity off E.
- (c) Near a generic Q ∈ E the off-E points lie on the open sides, since ℓ′ ∩ B(Q, ρ) ⊆ E.
- (d) continuity at p\*.
- (e) follows from (W2), third claim, applied at the q_n themselves (off E).
- (f) is trivial.
- The genericity of a.e. (o, y) follows from countably many null conditions.

**Lemma 4.1: CORRECT.**
- *Case Q ∉ E.* If Q ∈ β_v, continuity puts the off-E points of [o, Q) near Q into β_v. Such points exist because S
  meets E countably. So Q ∈ α_v.
- *Case (A).* The collar lies in D_{K^o} ∖ D_{K^s}. 2.8(b) with s < δ_{K^o}/2 then contradicts 2.1(e).
- *Case (B).* The bound K_p ⊄ B(v, ρ) is uniform on B(Q, r′) ∖ E, by sequential one-sided convergence on each side.
- *Steps 1–4.* I re-derived each, with the D1_referee open-chart Step 1:
  - R(−h) ∩ B° ≠ ∅ would give q ∉ E with K_q ⊆ B(v, |h − w′|/c₀) ⊆ B(v, ρ);
  - {c > 0} ∩ B° ⊆ {d ≥ 0}, so R(h) ∩ B° = {c > 0} ∩ B° (silence is available, since U ⊆ N);
  - Step 2 uses that R(h) is open and E is null;
  - Step 3(i) uses the exact chart 2.3 at off-E points;
  - Step 4 uses UVN at w₊, which is global.
- *Cosmetic.* In Step 3, choose h±ⁿ within min(δ(s_n), 1/n) of the facet. Otherwise "h₋ⁿ lies in q's collar for large
  n" in (ii) can fail. The write-up's PL2 has this as "so close to the facet".

**Theorem 4.2: CORRECT.** I checked every link.
- V_j ∩ Ω ⊆ Γ_v and (V_j ∩ Ω) ∖ E ⊆ β_v, by 2.4(b) applied to all of U.
- S ⊆ int co(O ∪ V_j), as a segment between interior points.
- y ∈ cl β_v even when y ∈ E.
- Q₁ ∈ Ẑ_v, by Lemma 4.1.
- The balls B(q_n, r_n) ⊆ Γ_{v′} come from continuity of K♭ at q_n ∉ E (2.2(d)) together with (W2).
- [o, Q₁) ⊆ G′, by the explicit ball (1 − t)B(o, ε) + tq_n.
- The case Q₂ < Q₁ applies Lemma 4.1 to the generic subsegment [o, Q₂] ⊆ G′ and then 4.0(e).
- The case Q₂ = Q₁ ∉ E contradicts K_{Q₁} = {v}.
- The case Q₂ = Q₁ ∈ E:
  - K^s ∋ v, v′ (off-E points of [o, Q₁) lie in G ∩ G′);
  - K^o = {v}, by 4.0(c), since K^s ≠ {v};
  - W = {v·g > 0 > v′·g} ⊆ D_{K^o} ∖ cl D_{K^s} carries patterns other than ±σ′, which contradicts 2.1(e).

  This is exactly the configuration M3's reading missed (§6, correction 2).
- No endpoint other than o and y needs to be generic. GAP (ii) of M23_referee is closed.

**Lemma 4.3: CORRECT.**
- Γ follows from concavity and (W2).
- β♭ is open by upper semicontinuity: if v ∉ K♭_q, every cluster set misses v.
- p\* ∈ α♭.
- For Q ∈ α♭ ∩ cl β♭, the exact charts 2.6(a) hold at **every** q ∈ B_ρ. In Step 3(i) this gives
  {a₊ > 0} ∩ B_ρ ⊆ β♭ itself, not just its closure.
- Step 1 is unnecessary, because 2.5(c) excludes reject cells in B.
- Step 4 uses global UVN at w₊.
- Connectedness of B_ρ finishes the argument.

---

## 5. The TSalways cascade (§5): CORRECT

- **5.1.**
  - D⁻ ⊆ Z_{τ₀}.
  - n is constant, by concavity and continuity at τ₀.
  - The B-half fails outside [τ_i, τ_j]: Lemma 3.4 at a single τ, against Step 1's sign.
  - Lemma 4.3 on B(p\*, ρ) with crossing τ_i kills A_{τ_i}.
- **5.2.**
  - {Ψ(·, σ_i) ≥ 0} is convex and contains p\* and V_l ∩ Ω, where V_l is the intersection of the neighbourhoods for σ₁
    and σ₂. G is its interior.
  - The concave vanishing argument holds on O.
  - (W5).
  - Lemma signs gives w_l > 0 at the crossing in both Options, so UVN at h(τ_c) for world l puts V_l ∩ Ω ∖ E into β.
  - Lemma 4.1 then applies along a.e. segment.
- **5.3.**
  - n·(e_l − p\*) ≤ 0, by 3.4.
  - Y can be chosen, even when n·(e_l − p\*) = 0.
  - Wall points are limits of off-E q_n with P(q_n, h^i(τ₁)) → v_m·h^i(τ₁) > 0, so they lie in cl A^i ⊆ cl H⁺.
  - The estimate is t ≤ δ/(δ + b).
- **5.4.** Lemma 4.3 plus Theorem 4.2. Shrinking U enlarges Γ and leaves α and β (defined by v ∈ K) unchanged.
- **5.5.** The combinatorics was re-derived over all three cases of the position of β.
- **5.6.**
  - The error is |ε_i| ≤ 2δ, not 3δ. This is harmless.
  - t_i ≥ (d − δ)/2.
  - The smallness of δ depends on dist(p\*, ∂Δ), as the BB2 numerics (4) show.
- **5.7.** The quantifier order is right: η is fixed for one τ on F_n, then d > 0, then δ. The cascade, the three walls,
  the convexity of A^n_τ and Ψ^n(p\*, τ) = 0 together give the contradiction.

---

## 6. The corrections to the record

1. **M3.6(c), the silence caveat: CORRECT.** N is open, not a cone, so on 𝒞 ∖ N the advice range can be {+, −}.
   - Then 2.5(c) makes "accept" the strict optimum on all of B(p\*, r₁).
   - Every gamble the chain uses lies in int N₀ ⊆ N.
2. **M3's reading of Lemma 3.2, case Q ∈ E: CORRECT.**
   - In the operative configuration (Thm 4.2, Q₂ = Q₁ ∈ E), K^o = {v}, so v′ is **not** in both one-sided limits.
   - D1.6 case (B) treats K^o = {v} as success: the wall is reached. It cannot give a contradiction there.
   - Lemma 2.8(a) is the mechanism.
3. **"Lines through p\* meet E countably" fails globally: CORRECT in substance; GAP (wording).**
   - BB2 needs and proves only the local statement 2.6(b).
   - The global claim is not proved on two-sided domains. An atom ℓ_k ∋ p\* whose tied advices are not optimal near p\*
     is not excluded by any argument on record.
   - But BB2 gives no field realising it, so "false" is unsupported. Write: "not established on two-sided domains, and
     not needed".
4. **D♭ coherent at every q (M3.4.2): CORRECT**, given Lemma 2.0, through 2.2(a) and (b).

---

## 7. Imports: what was re-derived here

**Re-derived (this report):**
- write-up Lemma signs; Lemma caps (a)–(c); Lemma sandwich (exact, for P♭, §3.4); Lemma rotation; Lemma risingsun;
  Prop regularity (a)–(d); Prop blowup (first blow-up, sweep, window, second zoom); Lemma twoslope; Cor PCNS;
  Prop boxbridge (a), (b); the corner algebra of Prop T1;
- R1 Prop 3.1 ([I2]): K ↦ 1_{D_K} is a continuous injection from a compact space into L¹. This uses that μ is finite
  and gives null mass to cone boundaries and positive mass to open sets. The image is closed by compactness;
- R10b Lemmas D and M; Lemma PL2 (as Lemma 4.1 Steps 1–4 and Lemma 4.3);
- N21.4 items 1–8 (as Thm 3.2); N21.9 (as Prop 5.2); R23.1, R23.2 (as 4.3, 5.1); N28 Prop 3.1 and Lemmas 3.2–3.4,
  Thm 3.5 (as §5);
- Q4.0(a) and Q4.3 (as 2.4).

AUDIT_BB verified none of these. It verified the Lemma 2.0 repair and stated that the analytic chain, the fixed-point
reduction and target uniqueness were unchecked.

**Not re-derived (used only in the consequence §8, at their recorded status):**
- M3.1 (endorsers on the ladder, adds-up clause), M3.4 (fixed point), D1 (p\* ∉ E), M3.7(d), M3.8 (route I1), Q4.1
  (one cut cell ⇒ (Av)). Each was refereed once: M23_referee, D1_referee, Q24_referee.
- [I1] Remark advicerange; [I3] R1 Lemma 1.2.
- Prop T1's box certificate. It is used in M3.8 and Q4.1, not in M3.9.

M3.7, M3.8, Q4.1 Step 3 and D1.1(a) also need Lemma 2.0 (§1.1). With it their off-E arguments stand as refereed.

---

## 8. Repaired statements

> **Lemma 2.0 (PROVED; AUDIT_BB, verified here).** Let 𝓜 be decomposable, ψ strictly guiding with measurable penalties
> and env < ∞ a.e., and suppose (γ) holds: for a.e. q ∈ Ω the q-Bayes model is a.e. unique and coherent. Then at
> **every** q ∈ Ω ∖ E the q-Bayes model is a coherent model of 𝓜, D_{K_q}.

> **Theorem M3.9 (PROVED: BB2 + Lemma 2.0; full independent reading CC3).** Let 𝓜 be a decomposable domain with (LF) at
> D_{T1} (open N ⊇ ∂D_{T1} ∖ 0; for a.e. pair with an orientation h ∈ N, "accept h" and silence are available). Let ψ
> be a strictly guiding field with measurable penalties, env < ∞ a.e., satisfying (γ). Let D_{T1} be the a.e.-unique
> ψ-Bayes model at some p\* ∈ Ω. Then there is a ball B ∋ p\* such that:
> - (a) **(TS)** holds on every facet F_k at every τ ∈ (0,1). It is the same for P♭, for P at q ∉ E, and for every
>   directional family P^δ.
> - (b) For every facet and τ ∈ (0,1), Z_τ ∩ B = λ_τ ∩ B **at every point**, with λ_τ ∋ p\*. Also
>   A_τ ∩ B = H⁺_τ ∩ B, B_τ ∩ B = H⁻_τ ∩ B, and A_τ ⊆ H⁺_τ. The chord normal n_τ is continuous and strictly monotone,
>   with λ_{τ_i} = lin(p\*, e_i). There is no sliding at the corners.
> - (c) **(PC)** holds with rank-2 Γ_k, and **(NS)** holds. The crossing rows are c_k(h)_i = λ_{ik}h_i with λ_{ik} > 0.
>   After the normalisation p\* = u (penalty rescaling), the corner equations give x₁ = x₂ = x₃ ∈ {x₊, x₋}.
> - (d) **Vector cluster clause.** For good g → h ∈ h^k((0,1)) (or scalings of it, with silence available),
>   c(g)/|c(g)| → c_k(h)/|c_k(h)|.
>
> Hence (C2) and (C3) of M3 §6 hold. Not used: (Av), edge confinement, integrability, (γ₀) at boundary weights, R4
> Thm B, Thm gm, Prop chainchords as a black box.

> **Corollary Q4.2 (contains M3.10, M3.10′; PROVED at the status: M3.9 as above; M3.1, M3.4, M3.7(d), M3.8, D1, Q4.1
> refereed once each; Q4.3 twice).** Let 𝓜 be a decomposable domain with (LF) at D_{T1}. Let a ranking satisfy strict
> (G), (IB), (LA), (S) (closed sections for every model), (C), T1 ∈ C_L, and (NC) at every world. Then every endorser
> tuple ν has a degenerate ladder field ψ^ν: some world has a non-null ladder-blind set. In particular, **no ranking whose
> worlds all add up covers T1 on any (LF) decomposable domain.**
>
> *Chain.*
> 1. M3.4: a non-degenerate ψ^ν is a (γ₀)-field with T1 Bayes at an interior p\*.
> 2. D1: p\* ∉ E.
> 3. Lemma 2.0 and M3.9: (C2), (C3).
> 4. Q4.1: (Av) holds.
> 5. M3.8 with M3.7(d): contradiction.
> 6. If all worlds add up, M3.1 makes ψ^{ν\*} non-degenerate.
>
> M3.10 and M3.10′ are the (Av)-domain special case. On M_U the premise also holds independently, by Thm M0closed(b).

**Scope of the premise.** "Every cover of T1 needs a world that does not add up" now holds on every decomposable domain
with (LF). What it leaves open is exactly R21's (GS), (GL) and (GnAv-d): a strongly (M1) world failing (NC), or a
degenerate (ladder-blind) world. (LF) cannot be dropped from D1: Example D1.0 shows this.

---

## 9. Requested changes to BB2

1. Insert Lemma 2.0 before Lemma 2.1, citing AUDIT_BB, B2_referee Lemma 1 repair 2 and D1_referee §1(a). In 2.2(a),
   replace "coherent by (H3)" with "coherent by Lemma 2.0".
2. Delete the δ-clause of Lemma 2.6(a).
3. Lemma 2.3: add the one-line Hausdorff argument for C ⊆ cl R(g).
4. Lemma 3.3(a): add the case x ∈ ∂H⁺.
5. Lemma 4.1 Step 3: take collar widths ≤ 1/n.
6. (P7): restate the uniformity domain.
7. §3.3, Step 7 table, sandwich row: justify the bound by the closed-half-plane form (§3.4), not by continuity.
8. Lemma 5.6: the constant is 2δ.
9. Correction 3: "false" → "not established on two-sided domains; not needed".
10. Status lines: M3.9 PROVED (one full referee reading, CC3). Q4.2, M3.10 and M3.10′ are PROVED at the status listed in
    §8.

## 10. Files

`cc3ref_py/`:
- `bb2_rerun.out`: identical to `bb2py/bb2_checks.out`.
- `cc3_checks.py` (+ `.out`). NUMERICS only:
  - (1) tie-vector patterns: 0 failures in 20 000 instances;
  - (2) reject-cell dichotomy: 15 013 nonempty cells, 0 thin;
  - (3a) corner proportionality equivalence: 0 failures in 10 000 tests;
  - (3b) fixed points of φ³: 0 failures in 5000 values of κ;
  - (4) exact sandwich for lower-semicontinuous jump profiles: 0 failures in 161 094 points;
  - (5) margin convergence behind Lemma 2.0: the mismatch fraction scales linearly in |q_n − q|.
