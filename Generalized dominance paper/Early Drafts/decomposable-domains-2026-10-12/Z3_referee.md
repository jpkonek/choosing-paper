# Z3 — Referee report on Y3, on Y1 at its corrected scope, and on the splice lemmas of AUDIT_Y123

17 Oct 2026. Labels as in BRIEF13:
- **PROVED**: proof given or completed here; one reader (me);
- **CHECKED**: exact rational computation, reproducible;
- **NUMERICS**: sampling only;
- **CONJECTURE**.

Verdicts are CORRECT / GAP (fixable; fix given) / WRONG.

Scratch scripts are in `z3ref_py/`. Run each with `python3 -I <script>` from inside that folder.

**Reruns.**
- All six `y3py/` scripts were rerun with `python3 -I`. Each output is **byte-identical** to the stored `.out` (`z3ref_py/*.rerun`).
- `y1py/shatter.py` was rerun: identical (`z3ref_py/shatter.rerun`).

Notation is that of Y3 and the write-up §2. Additionally:
- A = 1+λ = κ;
- Bayes(w) is the w-Bayes model of an additive field;
- Ψ = (Ψ₁, Ψ₂, Ψ₃) is the vector of world losses.

---

## 0. Verdict table

| Item | Verdict |
|---|---|
| Y3 Lemma Y3.1 (a)–(e) | CORRECT |
| Y3 Lemma Y3.3a (B₁ corner = T1 at u on Γ_η) | CORRECT. The bound η < 1/(A+1) is **sharp** (PROVED + CHECKED here, §1.2). |
| Y3 Lemma Y3.3b (field = B₁ family on N) | CORRECT |
| Y3 Lemma Y3.3c (Λ = 16√(6/π)A²) | CORRECT |
| **Y3 Theorem Y3.2** | **CORRECT**. It can be strengthened: global (C) holds, and the Bayes selection on all of Δ satisfies everything except coherence off N∪{u} (§1.3). |
| Y3 Cor Y3.3 (fragments, thin competitors, X2.2(c) records) | CORRECT. The plan/fragment content is automatic (§1.4). |
| Y3 Cor Y3.4 (vertex locality barrier) | CORRECT. Strengthened form in §1.3. |
| Y3 Prop Y3.5 (cube = posterior on ∂Δ) | CORRECT |
| Y3 Prop Y3.7(a) (box rigidity) | CORRECT |
| Y3 Prop Y3.7(b) (two box vertices incompatible) | CORRECT |
| Y3 Cor Y3.6 | CORRECT |
| Y3 Remark Y3.8 (posterior not additive near e₁, identity parametrisation) | CORRECT |
| Y3 §5 "homogeneous families ⇒ boxes" (labelled PROVED) | GAP (§1.7). Not used elsewhere. |
| Y3 Conjecture Y3.C | Open; plausible. Needs a precise statement; reformulation in §1.8. |
| Y1 Lemma Y1.1 (monotone rays and converse) | CORRECT |
| Y1 Cor Y1.1′(i) | **WRONG** (audit's counterexample verified; CHECKED). What survives is (i′), §2.1. |
| Y1 Cor Y1.1′(ii), Lemma Y1.2 | CORRECT |
| **Y1 Prop Y1.3** (balanced field) | **CORRECT** |
| **Y1 Theorem Y1.4** | **CORRECT at scope 𝓛**, with one fixable measurability GAP (§2.3). The exact surviving scope is in §2.4. |
| Y1 Lemma Y1.5 (four-point shattering) | CORRECT (rerun, exact) |
| Y1 Q_Y1 "complementarity" description; "additive/credal levels forbid complementarity by Lyapunov" | **WRONG** as stated. Corrected residual in §2.5. |
| AUDIT §2 counterexample to Y1.1′(i) | CORRECT (CHECKED) |
| AUDIT Prop 1 (no cancellation) | CORRECT |
| AUDIT Prop 2 (Y1's pattern is additive) | CORRECT |
| AUDIT Prop 3 (undominated tied pair) | CORRECT |
| AUDIT Prop 4 (retained strict primary ⇒ level-set minimality) | CORRECT |
| AUDIT Prop 5 (forced splice ties) | CORRECT |
| AUDIT §5 trivial interior subsystem; plateau replacing u | CORRECT |
| AUDIT §1 "Y3 does not establish global (C)" | Superseded: global (C) **does** hold for Ψ⁽¹⁾ (§1.3) |

The splice results are written as exclusion rules for X1's machinery in §3. All of them are **derivable** from Θ_C ∪ Plan(V), or from Θ_C ∪ Plan(V) ∪ RET for Props 4–5. So they are sound and change no satisfiability verdict; their value is short certificates and fragment closure (§3.0).

A small new consequence is §3.6: under retained additive primaries, (Csel) forces p ↦ Ψ(C_p) to be injective.

---

## 1. Y3

### 1.1 Lemma Y3.1 — CORRECT

**(a) Guidance.** For h_i > 0 the losses are
- M: −m_i(h)h_i < 0;
- S: 0;
- O: m_i(−h)h_i ≤ A|h| < 2A|h|, the loss of ×.

The order is good < silence < bad < contradictory, as required. Unanimous pairs are similar, and the envelope 2A|h| is Gaussian-integrable.

**(b) Bayes models.** For box fields both acceptances can never be positive: w·n(h) = min_{m∈B}(w⊙m)·h and w·n(−h) = −max_{m∈B}(w⊙m)·h.

**(c) Box families.** The corner argument is correct. Ties form a finite union of hyperplane pieces, since m is constant on orthants.

**(d), (e).** As stated.

**Remark (used below).** For *every* w ∈ Δ, the pointwise minimiser of w·ℓ(h,·) is a.e. unique for the fields Ψ⁽¹⁾ and Ψ^□. The tie loci are:
- (w⊙m(h))·h = 0;
- (w⊙m(−h))·h = 0;
- (w⊙(m(h)+m(−h)))·h = 0.

Each is a finite union of pieces of hyperplanes, because m is constant on finitely many cones and w⊙m ≠ 0. The value of × is strictly positive while S gives 0, so × is never a minimiser.

### 1.2 Lemma Y3.3a — CORRECT; the bound is sharp

I re-derived all three cases.

The case g₂ > 0 > g₃ with g₁ < −|g₃|:
- M = g₂ is forced, because |g₃| < |g₁| ≤ ηM < M;
- the bounds τ₁, b ≥ M(1−(A+1)η) are right.

**Sharpness (PROVED; CHECKED in `z3_eta_sharp.py`).** Take g = (−x, 1, −y) with x = 1/(A+1)+δ and y = 1−Ax+δ².
- Then 0 < y < x, τ₁ = −δ² < 0, and b = τ₃ = 1−x−Ay > 0.
- So the B₁ corner accepts while T1 is silent, and g ∈ Γ_η for every η ≥ x.

Mismatches therefore exist for every η > 1/(A+1). Y3's control at η = 1.6/(A+1) does not show this by itself; the claim "not slack" is nonetheless true.

### 1.3 Theorem Y3.2 and Cor Y3.4 — CORRECT, and a strictly stronger form

Every clause checks:
- (1) uniqueness of the u-Bayes model, from Y3.3a on Γ_η and the frozen T1 attribution off Γ_η;
- (2) Y3.3b;
- (3) Lemma Y3.1(d), (e), with u isolated;
- (4) the plan, from Y3.3c;
- (5) the finitary form, which is trivial once a genuine ranking exists.

The plan is relative to the index set N∪{u}: V(u,i,X) = {u} is open there, not in Δ. That is what the theorem claims.

**Strengthening (PROVED).** The convexity step of Prop Y3.7, Step 0 (Lyapunov/Richter on the full domain), shows that every undominated model of an additive field is w-Bayes for some w ∈ Δ. By the Remark in §1.1, the w-Bayes model of Ψ⁽¹⁾ is a.e. unique for every w. Hence:
- **(i) Global (C).** A model tied at every world with an undominated X is also w-Bayes, hence equals X. So (C) holds for *all* members of C_L, not only Csel at N∪{u}. The audit's caveat (§1 of AUDIT_Y123) is unnecessary.
- **(ii) The Bayes selection on all of Δ.** Put C_p := Bayes(p) for every p ∈ Δ.
  - C_u = T1.
  - p ↦ C_p is continuous in measure on Δ. For each p the tie loci are null, so the advice converges a.e.; then apply dominated convergence. So all sections are closed on Δ.
  - C_p is competitive on supp p: if L_i(X) < L_i(C_p) on supp p, then p·L(X) < p·L(C_p).
  - C_p is undominated, and Csel and (R4) hold at every p.
  - The **only** clause of (S) that can fail is coherence of C_p, and it holds on N∪{u}.

**Cor Z3.1 (strong vertex locality barrier; PROVED).** On the full domain the following premises are jointly satisfiable, by Ψ⁽¹⁾ with its Bayes selection:
- global strict (G), (IB), (LA) and (C);
- (LF) at T1, and T1 ∈ C_L;
- a selection on **all of Δ** with C_u = T1;
- at every p: competitiveness on supp p, closed sections, (R4) and Csel;
- coherence of C_p for p ∈ N∪{u}.

So any exclusion of T1 must use **coherence of selected models at indices outside N∪{u}**. This is sharper than Y3.4, and it states the vertex barrier in the realisation-problem form of the write-up §3.

### 1.4 Cor Y3.3 — CORRECT; the plan content is automatic

- Once a genuine ranking with closed sections exists, the maximal plan always works (X1.3.3(e)). Every finite fragment is then satisfied by the restriction of one assignment. So "never shrunk" is automatic.
- The genuine extra is the explicit radius Λ⁻¹·gap, from Lemma Y3.3c. I re-derived it:
  - slab |ê·ĝ| ≤ A√3|p−q|;
  - cost per pair ≤ 2A|h|;
  - E|g| = 2√(2/π), and ê·ĝ is uniform on [−1, 1];
  - four corners.
  - The bound over H is a further factor-2 overestimate, which is harmless.
- **X2.2(c) records.** The silencing cost ∫_P|n₁(−h)| and the bound Ψ₁(Σ_p) − Ψ₁(B¹) ≤ Λ|p−e₁| are right. "Σ_p at O on P near e₁" needs P to have |h₁| ≥ c|h| on P, which holds because P is a closed cone in the open Q₁. N_P is then explicit.

### 1.5 Prop Y3.5 — CORRECT

- **Corner formulas.** On Q_o:
  - corner(h) puts A at o, giving M iff w·h + λw_oh_o > 0;
  - corner(−h) puts A at j, l, giving O iff w·h + λ(w_jh_j + w_lh_l) < 0.
- **Edges.** ν(p⊙[1,A]³) and ν(p⊙T1) are the same odds segment [r/A, rA].
- **Interior.** The hexagon is ⊋ K_p.
- T1 is not a Bayes credal set, and all undominated models are unique-Bayes (§1.1 Remark), so T1 is dominated.
- (C) holds globally, by the §1.3 argument.

### 1.6 Prop Y3.7 and Cor Y3.6 — CORRECT

**Step 1 (pinning).**
- On ℓ_g ∩ int N, the max − min of (p⊙m)·g over B equals Σ_j p_j(β_j−α_j)|g_j| > 0. So the box model is silent on the far side, and S is a minimiser there.
- The gain functional is linear in p, ≥ 0 on one side and ≤ 0 on the other on a dense set. So it vanishes on the segment ℓ_g ∩ N.
- Two independent points of that segment span the plane {(corner⊙g)·p = 0}. Hence the gain is a positive multiple of corner_B(g)⊙g, and it is non-zero by (G).

**Step 2 (crossing families).**
- For g = (−a, 1, −c) with c near 1/A > a: min τ = τ₃ = 1−a−Ac, and P_{T1}(−g) = c₀(a−1+c) − ε < 0.
- The coefficient identities give β₁w₁ = α₂w₂ = β₃w₃/A. The (+,+,−) family gives α₁w₁ = α₂w₂ = β₃w₃/A.
- With the mirror families, α₁ = β₁, β_j = Aα_j and α_jw_j = α₁w₁.
- The degenerate case w₃ = 0 is correctly excluded, and similarly w₁ = 0.

**Step 3, (b).**
- The derivation in (a) holds for *every* w\* at which T1 is Bayes, so a common w\* serves both vertices. Uniqueness of w\* is not needed.
- For g = (x, −y, 1): the corners are (1,A,1) for B₁ and (1,1,1) for B₂, and the cross product is non-zero.
- CHECKED: `y3_twobox.out`, rerun.

**The "exactly B₁ up to reparametrisation" remark.** Rescaling world i's penalties by 1/w\*_i preserves (G), (IB) and every preorder, and maps p-Bayes to ν(p⊘w\*)-Bayes. So the converse holds too. CORRECT.

### 1.7 Y3 §5, "homogeneous ⇒ Minkowski ⇒ box" — GAP

Let f(s,t) = σ_{K′(s,t)}(−y). If f is 1-homogeneous and has straight level lines, then:
- f = a·(s,t) on {f > 0} and f = b·(s,t) on {f < 0};
- continuity across the zero line gives a = αν, b = βν, with ν normal to that line.

Then f = α(ν·x)₊ − β(ν·x)₋. This is linear **only if α = β**.

So "hence Minkowski sP+tQ" needs an argument that α = β for every y whose zero line enters the quadrant. Two possible routes are sublinearity of y ↦ σ (convexity of each K′) together with the edge data, or a direct counterexample.

The claim is labelled PROVED but is not used elsewhere. Downgrade it to CONJECTURE or supply the step.

### 1.8 Conjecture Y3.C — open; needs a precise statement

**Reformulation (PROVED for additive fields on the full domain).** The range R = {L(X)−L(T1)} is convex, and so are its projections onto faces. Hence:
- a model competitive on Ω is w-Bayes for some w ∈ Δ;
- a model competitive on {i, j} is w-Bayes for some w ∈ [e_i, e_j].

So any closed competitive coherent selection on N₁∪N₂∪{u} has the form C_p = Bayes(φ(p)), with supp φ(p) ⊆ supp p.

Closed sections are equivalent, for additive rankings, to lower semicontinuity of each p ↦ Ψ_i(C_p). The proof uses Lyapunov: the Ψ_i-range is an interval.

So Y3.C is the statement: *no strictly guiding additive field with T1 ∈ C_L has a face-respecting index map φ on relative neighbourhoods of two vertices, with each Ψ_i∘Bayes∘φ l.s.c. and Bayes(φ(p)) coherent.*

**Precision requests.**
- the domain (full);
- "near" (relative neighbourhoods containing edge segments);
- whether Csel/(R4) are required. They are automatic when Bayes models are unique.

**Status.** It is not implied by Y3.7(b), which covers identity-parametrised boxes only. It is not implied by Thm gm, whose routes use the chart form at every interior prior. Plausible.

### 1.9 Remark for the connection milestone (PROVED; CHECKED)

- **(a) Junction rule.** In an additive ranking with closed sections, take p_n → p\* in the index set. Every limit point y of Ψ(C_{p_n}) satisfies Ψ(C_{p\*}) ≤ y componentwise. This is lower semicontinuity, as above.
  - Suppose the C_{p_n} are Bayes models of a field with unique, continuous Bayes models, so that y = Ψ(Bayes(w)) for a limit weight w.
  - Undominatedness then forces Bayes(w) = C_{p\*}.
- **(b) Consequence.** For a junction at C_{p\*} = T1 in Ψ⁽¹⁾, the weights must accumulate at {w : Bayes(w) = T1}.
- **(c) Ψ⁽¹⁾ fails along the symmetric segment.** The Bayes models of Ψ⁽¹⁾ are **incoherent at weights arbitrarily close to u** along the symmetric segment from ∂N to u.
  - Mechanism: off Γ_η the field freezes the attribution k(g) = argmin g_k, which is correct only at w = u. So w·n(g) jumps across {g₁ = g₂ < g₃} whenever w₁ ≠ w₂.
  - CHECKED: an exact robust midpoint-convexity witness at t ∈ {3/4, 9/10, 99/100, 999/1000} (whenever the witness family lies off Γ_η), for ε ∈ {1/10, 3/10, 1/2, 4/5} (`z3_bayes_path3.out`).
  - NUMERICS (`z3_bayes_path2.out`) also show non-convex plane sections at other intermediate weights.
- **CONJECTURE.** u is isolated in {w : Bayes_{Ψ⁽¹⁾}(w) coherent}. If so, Ψ⁽¹⁾ itself cannot carry a connection: a connection needs a different field, consistent with BRIEF20.

---

## 2. Y1 at its corrected scope

### 2.1 Lemma Y1.1 — CORRECT; Cor Y1.1′(i) — WRONG

**Lemma Y1.1.** I re-derived all parts:
- the advice formulas of X2.6;
- (a): coefficient signs p_ik_i on Q_o (o ≠ i) and on Q_i;
- (b): the open set k_l ∈ (−p_jk_j/p_l, −p_jd_jk_j/p_l), with h_i small;
- (c).

**Y1.1′(i) is WRONG.** The audit's reweighting is correct:
- w_i = 1/a_i on {d_i > 0} and 1/b_i on {d_i < 0}. This is bounded and positive, so strictly guiding.
- It gives L_i(C_q) − L_i(C_p) = 1 − 1 = 0.
- For p = u and q = (1/2, 1/3, 1/6), crossing at every world holds. CHECKED: exact witnesses of both signs at each world for ε = 1/10 and 1/2, with Monte Carlo a_i, b_i > 0 (`z3_y11i_counterexample.out`).

**What survives, (i′) (PROVED).** Two distinct posterior models on a common e_i-ray are never tied at world i, by strict (G). Hence no relatively open set of selected models, and no ray segment, is an all-world tie class. This is all that Y1's remark about the "tie plateau" needs. Y1.4 does not use (i).

**Y1.1′(ii) and Y1.2.** CORRECT: the segment toward e_i is the monotone ray.

### 2.2 Prop Y1.3 — CORRECT

- **Penalty table.** It is strictly increasing in each world's rank.
- **Balance.** Σ_i ψ_i = 0 for M, S and O on mixed pairs, and is > 0 otherwise. This gives competitiveness on Ω (interior p), undominatedness, and continuity of p ↦ ψ_i(C_p).
- **Csel failure.** No Lyapunov is needed:
  - the S→M moves on Q₁, Q₂, Q₃ have fixed directions (2,−1,−1)w, (−1,2,−1)w and (−1,−1,2)w, which positively span {Σ = 0};
  - the hole's change lies in that plane, provided F is a ball of *mixed* pairs, as the note implicitly requires;
  - incoherence follows from the cone argument of Y1.4(T).

### 2.3 Theorem Y1.4 — CORRECT within 𝓛, one GAP

Checked step by step:
- **𝓛 orders are transitive.** At the same first differing level, X ≤ Y ≤ Z unanimously with χ₀(X) < χ₀(Y) gives χ₀(X) < χ₀(Z).
- **(IB) and strict (G)** hold.
- **(a)** This is AUDIT Prop 4.
- **(b), Lagrange.** The lower boundary of the convex compact {(ψ, χ)} has a finite subgradient at an interior abscissa.
- **(b), Topkis.** It yields pointwise weak i-dominance, hence the ray, by the converse in Y1.1. Comparing through an off-line r shows that the subgradient is unique and constant.
- **(c)** Correct, because B ⊆ A^α at every stage, and B is world-independent.
- **(d), face recursion.**
- **(d), (T).** The centre of y ∈ relint, the Lyapunov equal-share partition of U^c, and the cone argument (rays through F meet U∖F on both sides, using h₀ ≠ 0 and F ≪ U) are all correct.
- **(e)** Finitely many non-zero lexicographic signs survive c̃ = c₁ + δc₂ + δ²c₃. Homogeneous half-spaces in ℝ³ have VC dimension 3. Complements are free, since the sign is non-zero.
- **Shrinking N₀** to the small square of Y1.5 is legitimate: the hypotheses restrict.

**GAP (measurability; fixable).** A^{α+1}(h) := ⋂_{χ∈Φ^{α+1}} argmin(…) is an intersection over a possibly uncountable family of penalty *versions*. The resulting set map need not be measurable or version-independent, and "C_q(h) ∈ A^{α+1}(h) a.e." needs one null set for all χ.

*Fix.* Define 𝔅^{α+1} := ⋂_χ {X ∈ 𝔅^α : X pointwise minimises χ + τ_χψ}.
- This is an intersection of decomposable classes that are closed in measure, so it is decomposable and closed in measure.
- It is nonempty, since it contains C_p.
- By Hiai–Umegaki (write-up Remark advicerange) it equals {X : X(h) ∈ A^{α+1}(h) a.e.} for a measurable A^{α+1}, the essential intersection.
- Define B via a countable dense set D ⊆ N₀. Advice regions are relatively open in q off null boundary lines, so every advice attained on an open set is attained on D.
- Then C_q ∈ 𝔅^{α+1} for each q. The tie-set characterisation is unchanged, and the limit stages are essential intersections.

### 2.4 What survives of Y1 (exact scope)

**Theorem Y1.4 (as repaired).** Take the full domain, the posterior selection, and any nonempty open N₀ ⊆ Δ°. No ranking whose three world orders are towers of the following kind has both closed sections on N₀ and Csel at every p ∈ N₀:
- level 0: **one** strictly guiding, countably additive functional with integrable penalties (μ finite and non-atomic; integrable rather than bounded suffices for Lyapunov);
- levels α ≥ 1, any ordinal length: unanimities over arbitrary families of countably additive functionals with integrable penalties.

Competitiveness and protection are not used.

**Not covered:**
- a unanimity at level 0;
- charges or finitely additive states at any level. So "any credal tie-break" in Y1 §0 must be read as *countably additive* credal members;
- hyperreal or Haar-infinite levels;
- **arbitrary non-representable tie-breakers** after an additive level 0. Y1 §5 omits this third route. Only step (a) survives there, as AUDIT Prop 4, together with the splice-tie Prop 5.

**Also surviving:**
- Y1.1, Y1.1′(i′), Y1.1′(ii), Y1.2, Y1.3, Y1.5;
- Remark 4: additive one-level case;
- Remark 2: X2.7 transplanted to a finite measure.

### 2.5 Q_Y1 — the complementarity description is WRONG; corrected residual

Y1 §6 asks for C_p ≺_i Z ≻_i C_q with C_p ~ C_q, and says additive or credal levels forbid this "by Lyapunov".
- By AUDIT Prop 2 this pattern is ordinary additive behaviour. It forces W ≺_i C_p, and nothing forbids it.
- What 𝓛 forbids is different: a box mixture X with Ψ(X) = Ψ(C_p) that is not tied with C_p at every world (Y1.4(c)).

**Corrected residual (PROVED reductions).** Suppose an escape keeps a scalar additive primary L_i at every world with all its strict comparisons, and has closed sections on N₀.
- By Prop 4, C_p ⪯_i X for every X with L_i(X) = L_i(C_p).
- By Prop 5, any splice Z of C_p and C_q with L_i(Z) = L_i(C_p) = L_i(C_q) is tied. So the two-model complementarity of Q_Y1 is **impossible**, not merely non-additive, whenever the two models have equal primaries.
- By §3.6, distinct selected models have distinct primary vectors.

So the residual question is: *multi-model* box mixtures X (Ψ(X) = Ψ(C_p), X ∈ 𝔅 incoherent) must be made strictly worse at some world by later rules, while C_p ⪯ X holds everywhere. Otherwise the escape must **discard** strict primary comparisons, as the audit says.

Prop 3 does not exclude the multi-model case: there is no tied partner.

---

## 3. The splice lemmas of AUDIT_Y123 as exclusion rules (X1's framework)

### 3.0 Proof verdicts and status

All five proofs are CORRECT as written. I re-derived each one.

CHECKED: `z3_splice_exhaustive.out` enumerates all 55 (IB)-preorders on the 2×2 product domain, with no guidance imposed. Every instance of Props 1, 2, the Prop 5 core and Prop 3 (2 and 3 worlds) passes. This is a sanity check; the proofs are general.

**Status inside X1.**
- Props 1–3 are **derivable** from (Σ) and (R4), with record identity from Lemma X1.1.2(i).
- Props 4–5 are derivable from Plan(V) together with retention literals RET.

Hence adding them to Θ_C ∪ Plan(V) (∪ RET) **cannot change satisfiability** (Prop X1.3.2). They are legitimate in the strongest sense, and their use is:
- (i) **fragment closure**: whenever a fragment contains a record r and a symmetric set E, add r_E, r_{E′} and their inverses;
- (ii) **short certificates**: at most 5 Horn steps for Prop 3, and at most 31 clauses for the all-world Prop 5 test.

**Notation.** For models A, B and a symmetric measurable set E:
- r := rec(A,B); r_E := r on E and ι off E; r_{E′} := r on E^c and ι on E;
- Z := B on E, A off E; W := A on E, B off E.

**Record identities** (Lemma X1.1.2):
- rec(A,Z) = rec(W,B) = r_E;
- rec(A,W) = rec(Z,B) = r_{E′};
- r = r_E∘r_{E′};
- r⁻¹∘r_{E′} = (r_E)⁻¹;
- r_E∘r⁻¹ = (r_{E′})⁻¹.

All of these are composable. The (IB) "transfers" of the audit are literally **the same variable**.

### 3.1 Rule SP1 (Prop 1: no cancellation)

- **SP1a**: x_{i,r_E} ∧ x_{i,r_{E′}} → x_{i,r}.
- **SP1b**: x_{i,r⁻¹} ∧ x_{i,r_{E′}} → x_{i,(r_E)⁻¹}.

Both are (Σ) instances.

**Exclusion form:**
⊥ ← x_{i,r_E}, ¬x_{i,(r_E)⁻¹}, x_{i,r_{E′}}, x_{i,r⁻¹},
with the same rule for E and E′ exchanged.

In words: two weak worsenings, one strict, never compose to a tie or an improvement.

### 3.2 Rule SP2 (Prop 2: Y1's pattern; a derivation, not an exclusion)

x_{i,r}, x_{i,r⁻¹}, x_{i,r_E}, ¬x_{i,(r_E)⁻¹} ⊢ x_{i,(r_{E′})⁻¹}, ¬x_{i,r_{E′}}.

That is, A ~ B and A ≺ Z give W ≺ A.
- The first conclusion is (Σ) with r_E∘r⁻¹ = (r_{E′})⁻¹.
- The second is SP1b, contraposed.

The premise set is satisfiable additively (audit's ±1 example). It must **not** be listed as forbidden.

### 3.3 Rule SP3 (Prop 3: undominated tied pair), at a selected index p

Let r := r_p^B = rec(C_p, B). Then:

⊥ ← ⋀_j x_{j,r⁻¹}, ⋀_j x_{j,r_E}, ¬x_{k,(r_E)⁻¹}  (any k),

with the same rule for E and E′ exchanged.

Derivation (5 steps):
1. (Σ) gives x_{j,(r_{E′})⁻¹} for every j (W ⪯_j C_p).
2. (R4) with X = W, where r_p^W = r_{E′}, gives x_{k,r_{E′}}.
3. SP1b gives x_{k,(r_E)⁻¹}, contradicting the last premise.

Only B ⪯_j C_p at every j is used, not the full tie. For a non-selected undominated A, the rule holds in every successful system: route it through the selected model tied with A (Thm kkm), at the cost of extra literals.

### 3.4 Rule SP4 (Prop 4), conditional on retention

**Hypothesis literals.** For a scalar primary L_i at world i:

RET_i := { x_{i,rec(X,Y)}, ¬x_{i,rec(Y,X)} : L_i(X) < L_i(Y) }.

**Rule.** Fix p and X with L_i(X) ≥ L_i(C_p). For any plan V, pick q ∈ V(p,i,X) with L_i(C_q) < L_i(C_p). Then

x_{i,r_q^X} (from RET) and Plan: ¬x_{i,r_q^X} ∨ x_{i,r_p^X}  ⊢  x_{i,r_p^X}.

**Applicability.** p ∈ cl{q ∈ I : L_i(C_q) < L_i(C_p)}, so a suitable q exists in *every* open V(p,i,X). This holds at every interior p for the posterior family and a strictly guiding additive L_i, along the improving ray (Y1.1(a)).

The certificate has 2 literals per instance and is independent of the plan.

### 3.5 Rule SP5 (Prop 5: forced splice ties)

Suppose:
- SP4 applies at p and at q at world i;
- L_i(C_p) = L_i(C_q) = l;
- d := rec(C_p, C_q), and E is such that L_i(Z) = l, where Z := C_q on E, C_p off E. For additive L_i this gives L_i(W) = l.

SP4 then derives:
- x_{i,d} (X = C_q at p);
- x_{i,d⁻¹} (X = C_p at q);
- x_{i,d_E} (X = Z);
- x_{i,d_{E′}} (X = W).

(Σ) then gives x_{i,(d_E)⁻¹} = x_{i,d_{E′}∘d⁻¹} and x_{i,(d_{E′})⁻¹}. So C_p ~_i C_q ~_i Z ~_i W.

**All-world exclusion.** Suppose the hypotheses hold at all three worlds for one E, so that Ψ(Z) = Ψ(C_p) = Ψ(C_q), and Z is incoherent. Then:

⊥ by (Csel) at p with X = Z, since r_p^Z = d_E.

The certificate uses at most 4 RET literals, 4 plan clauses and 2 (Σ) clauses per world, plus one (Csel) clause.

### 3.6 New consequence: injectivity under retained primaries (PROVED)

**Claim.** Assume:
- full domain;
- additive, strictly guiding, integrable primaries L_i whose strict comparisons are retained at every world;
- closed sections on I;
- the SP4 approach condition at p and q at every world.

If p ≠ q and C_p ≠ C_q, then (Csel) forces Ψ(C_p) ≠ Ψ(C_q).

*Proof.* Suppose Ψ(C_p) = Ψ(C_q) = y.
1. The splice box 𝔅_{pq} = {X : X(h) ∈ {C_p(h), C_q(h)}} has Ψ-range y + {∫_E ρ}, where ρ is the record density on D = supp d.
2. This is a zonoid, centrally symmetric about y + ½∫_D ρ = y. So y ∈ relint Ψ(𝔅_{pq}).
3. The box has two elements on the non-null set D. The construction of Y1.4(T) (hole in a ball of constant advice, Lyapunov compensation) gives an incoherent X ∈ 𝔅_{pq} with Ψ(X) = y.
4. X is a complementary splice Z, with E = {X = C_q} ∩ D. Apply SP5 at all worlds. ∎

For the posterior on N₀ ⊆ Δ° this applies at every pair of interior points.

It is a genuine exact exclusion. For example, it kills at once any search that adopts a primary of the audit's §2 type (equal Ψ at two selected models).

It is not by itself an obstruction: injectivity of a map from a 2-dimensional set into ℝ³ is generic.

### 3.7 AUDIT §5, trivial interior subsystem — CORRECT

The field n(g) = g⊙(𝟙 + λe_{argmin g}) is Y3's off-wedge field used globally, since argmin_k v_k·g = argmin_k g_k.
- **Bayes at u.** u·n(g) = (1/3)(Σg + λ min g) = P_{T1}(g)/(3c₀). So D_{T1} is the a.e.-unique u-Bayes model.
- **Contradictory advice.** A penalty of 2A|g| makes every world strictly guiding.
- **Constant selection.** The constant selection T1 on a compact interior N has:
  - competitiveness on supp p = Ω (it concerns only the support);
  - protection and Csel, from uniqueness;
  - sections equal to N or ∅, hence closed.

  It needs no plan (Cor X1.3.4).
- **Global (C)** also holds, by the §1.3 argument: Bayes models are unique at every weight.
- **Replacing u by a plateau.** In Ψ⁽¹⁾, replacing u by a closed interior plateau P disjoint from N keeps every clause. The sections are (closed ⊆ N) ∪ (P or ∅).

So an isolated interior component is trivial, and the content of BRIEF20 is the connection. By §1.9(a), a junction with the plateau forces the adjacent selected models to converge in Ψ-value to T1's.

---

## 4. Files (`z3ref_py/`)

- `*.rerun`: reruns of all `y3py/` scripts and of `y1py/shatter.py` (byte-identical to the stored outputs).
- `z3_eta_sharp.py` / `.out`: sharpness of η < 1/(A+1) in Lemma Y3.3a (CHECKED).
- `z3_bayes_path2.py` / `.out`: plane-section coherence test of Bayes_{Ψ⁽¹⁾}(w) (NUMERICS).
- `z3_bayes_path3.py` / `.out`: exact robust incoherence witnesses for Bayes_{Ψ⁽¹⁾}(w), w → u on the symmetric segment (CHECKED).
- `z3_y11i_counterexample.py` / `.out`: crossing at every world for (u, (1/2,1/3,1/6)) (CHECKED witnesses; NUMERICS a_i, b_i).
- `z3_splice_exhaustive.py` / `.out`: exhaustive check of the splice Props 1, 2, 3 and the Prop 5 core on all (IB)-preorders of the 2×2 domain (CHECKED).
