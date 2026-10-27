# AA4: referee report on the audit's additive posterior loop (AUDIT_Z123_loop.md), Z1 and Z2

17 October 2026. Adversarial referee.

**Labels.**
- PROVED: proof checked line by line here.
- CHECKED: exact rational arithmetic.
- NUMERICS: floating point only.

**Verdicts.**
- CORRECT: the item stands as stated.
- GAP: the item is fixable, and the fix is given here.
- WRONG: the item is false as stated.

**Scripts.**
- Every script supplied with the three notes was rerun with `python3 -I`. Every output agrees byte for byte with the stored `.out` file. The reruns are in `aa4ref_py/rerun/`.
- My own scripts are in `aa4ref_py/`:
  - `loop_exact.py`
  - `z18_symbolic.py`
  - `z19_check.py`

---

## 0. Summary

| Item | Verdict |
|---|---|
| **Audit loop theorem** (§2): Ψ^L is strictly guiding and additive; its a.e.-unique w-Bayes model is D_{K_w} for every w ∈ L₁₂ | **CORRECT** |
| Audit: selected-model clauses and fixed plan on L₁₂ | **CORRECT** |
| Audit §2a: radial modification; uniqueness at every w ∈ Δ; global (C) | **CORRECT** |
| Audit §3: why Z1.8 misses L₁₂ (it needs a crossing on [u,e₃]) | **CORRECT** (made precise in §1.4) |
| Z1.1 vertex plateau; Y3.C false as stated | CORRECT |
| Z1.2 / Z1.3 / Cor. Z1.4 | CORRECT (Z1.4 needs two words added; see §2.2) |
| Z1.5 / Z1.6 star field | CORRECT |
| **Thm Z1.7** additive star through T1; plan V(p,i,X) | **CORRECT**. It extends much further (Prop AA4.1). |
| **Prop Z1.8** three-point forcing | **GAP, now fixed.** The all-ε claim needed a symbolic witness, supplied in §2.4. |
| Z1 §0, §4 "Meaning", §5.3–4: "loops / enclosed 2-D regions / an edge plus the arms are where additivity stops" | **WRONG.** Refuted by the audit's loop and by Prop AA4.1. |
| Remark Z1.9 | CORRECT for its stated claims (CHECKED here). Its field is incoherent near the vertices (§2.5), so it does not bear on Z1.C. |
| Conjecture Z1.C | Open, and well posed. Its relevance is reduced by Prop AA4.1. |
| Z2.1 | (a), (b) CORRECT. **(c) GAP**: a hypothesis is missing. |
| Z2.2, Z2.2′, Z2.3 | CORRECT. In Z2.2′ "rejects" should read "is silent on". |
| Z2.4a, Thm Z2.4 tripod | CORRECT |
| Z2.4: "global (C)" paragraph | GAP (M/O tie nullity is asserted, not proved). Fix: the audit's radial device. |
| Cor. Z2.4′ | CORRECT in substance. "Must use open-edge indices" needs the AR-extension step; it sharpens to "a full edge" (Prop AA4.1). |
| Thm Z2.5 boundary + T1 | CORRECT. Its global (C) clause has the same GAP and the same fix. |
| **Thm Z2.6** isolation ⇒ no connection | **CORRECT** |
| **Prop Z2.7** Ψ^∂ isolates T1; certificates | **CORRECT** |
| Conjecture Z2.C | Open. **The stated corollary needs a no-jump lemma and a uniqueness hypothesis** (§3.6). A single coherent edge does *not* isolate T1, by the audit's loop. |
| Q_Z2 | A legitimate question. **The gloss "must violate (A1)" is unsupported** (§3.7). |

**Main new point (Prop AA4.1, PROVED below).** Positive results:
- Ψ^★ (or Ψ^Y) carries a closed selection through T1 on **every closed I ⊆ Δ that contains no full closed edge**. The selection satisfies all selected-model clauses with a fixed plan.
- Ψ^L does the same on **every closed I ⊆ Δ∖{e₃}**, and it also has global (G), (IB) and (C).

Consequently, any additive exclusion of T1 must use an index set that contains **all three vertices and at least one full edge**.

Two-dimensional regions, loops, and T1 joined to a full coherent edge are all additively harmless. The minimal open additive configuration is "a full edge, the opposite vertex and T1 in one connected index set". Z1.8 settles it negatively only for the posterior family.

---

## 1. The audit's additive posterior loop

### 1.1 Set-up

With h_o = −1 and t = h_j, s = h_k:
- the posterior M-condition is c·w > 0, with c = h + (A−1)h_o e_o, on all of Δ;
- the posterior O-condition is the conjunction of
  - (a) w_o > A t w_j + s w_k, and
  - (b) w_o > t w_j + A s w_k.

Here A − 1 = 3ε/(1−ε), so A = (1+2ε)/(1−ε), as stated. The posterior's O-set on each segment is an interval, because it is an intersection of two half-lines. So the theorem reduces to matching the endpoints.

### 1.2 Line-by-line verification (PROVED)

**Case I (o ∈ {1,2}, D < 1).**
- On [u,e_j] put R = w_j/w_o, so that w_k = w_o. Then O holds iff R < r = min((1−s)/(At), (1−As)/t).
- The identity 1 − Atr = max(s, 1−A+A²s) = b is direct. So d·w/w_o = At(r−R), with the right root.
- On [u,e_o], d is positive at u, since At(r−1) > 0, and positive at e_o. The posterior is at O on the whole arm, because increasing w_o only loosens (a) and (b).
- On the edge, (a) binds because A > 1, and d·w = w_o − Atw_j matches it.

**Case I (D ≥ 1).**
- At + b = max(At+s, t+As) = D.
- On [u,e_o] the two constraints collapse to w_o > Dw_j, and d matches.
- On [u,e_j], d ≤ 0 at u and d < 0 at e_j. The posterior has no O there, since the constraints tighten as R grows.

**Case II.**
- The arm roots solve −d₁r − d₂ = 1 and −d₁ − d₂z = 1.
- 1 + d₁ + d₂ = (r−1)(z−1)/(rz−1) > 0.
- d₁, d₂ < 0, so there is no O on [e₁,e₂], where the posterior has none either.

**Case III.**
- d·u = (1−D)/3 ≤ 0, and d < 0 at e₁ and e₂. The posterior has no O on the loop.

**Sign pattern and guidance.** b > 0, and r, z > 1 when D < 1. The contradiction penalty 2|h| exceeds every bad loss.

**Selected-model clauses.**
- Bayes optimality gives (K) on supp w.
- A.e.-uniqueness gives (R4) and (Csel).
- w ↦ K_w is Hausdorff-continuous, with T ⊂ Δ°. Since boundaries are null, this gives continuity in measure, hence continuity of L_i(C_w).
- Hence the sections are closed, and the plan V(w,i,X) = {v : L_i(C_v) > L_i(X)} is fixed.

**The vertices.** At the vertices, K_{e_k} = {e_k} and E_k is the unique e_k-Bayes model by strict guidance.

### 1.3 §2a and global (C) (PROVED)

**Uniqueness at every w.** I verified the zero-set claims:
- Case I: the three affine forms.
- Case III.
- Case II: the polynomial identity is CHECKED on 2000 exact samples, with 0 failures. The branch t, s > 1/(A+1) is incompatible with D < 1. The other branches reduce to (−t,−As,1) or (−At,−s,1); I checked the reduction by hand.

**The radial device.** For a fixed generic direction, the tie M = O is w·ĉ = f(R)·w·d̂ with w·d̂ ≠ 0. Since f is strictly monotone, this has at most one root R, and Fubini makes the tie set null. Contradictory advice is never Bayes, and the decisions on L₁₂ are unchanged because at most one acceptance vector is positive there.

**Global (C).**
- Lyapunov convexity holds: the measure is nonatomic, there are finitely many actions, and the envelope is integrable.
- Separation from the open negative orthant needs only "not strictly dominated at every world", so it covers every undominated model.
- Uniqueness at the separating weight then forces any all-world tie to be the same model a.e.

So global (C), (G), (IB) and transitivity hold on all of Δ for the modified field.

### 1.4 Independent exact check, and why Z1.8 misses the loop

`loop_exact.py` (CHECKED) replaces the grid with an exact comparison of interval endpoints on each leg.
- **Coverage:** 7 values of A, 3 odd worlds, and 4 sampling modes:
  - generic;
  - small coordinates;
  - D within 10⁻³ to 10⁻⁸ of 1, on either side;
  - a coordinate within 10⁻² to 10⁻⁷ of the kink 1/(A+1).
- **Result:** 15 120 interval comparisons, **0 mismatches**, every case represented (I<: 2125, I≥: 1235, II: 1046, III: 634).
- **Control:** on the absent arm [u,e₃] the loop field differs from the posterior for 1704 of 5040 pairs. The field really does use its freedom there.

**Forced O–S points per pair on L₁₂.** For a single additive line, the forced points on L₁₂ are at most two in every case:

| Odd world | Case | Forced points | Other constraint |
|---|---|---|---|
| o ∈ {1,2} | A | x_j (non-odd arm) and z (edge) | the odd arm is only a sign constraint |
| o ∈ {1,2} | B | x_o and z | |
| o = 3 | A | x₁ and x₂ | the edge is only a sign constraint |
| o = 3 | B | none | |

Z1.8's three points (x₂, x₃, z for o = 1) need the arm S₃ ⊄ L₁₂. The audit's diagnosis is exact.

**Minor issues.**
- The note cites `loop-check/check.py`; the file is `audit_loopcheck/check.py`.
- The supplied script samples 31 grid points per leg. The analytic proof plus `loop_exact.py` close that gap.

---

## 2. Z1

### 2.1 Prop Z1.1: CORRECT

- **(K).** For p ∈ N_k we have k ∈ supp p, and E_k = B^k is world-k optimal by weak (G).
- **(R4)/(Csel).** Strict (G) gives X ⪯_k B^k ⇒ X = B^k a.e.
- **Pieces.** For η < 1/2 the pieces N_k are pairwise disjoint and miss u, since η < 2/3.
- **Sections.** The sections are unions of clopen pieces.

**Consequence.** Y3.C, as literally stated in Y3 §5, is false. This holds even under Z3's reformulation (§1.8 there): the plateau is the face-respecting map φ ≡ e_k. Consequence (d) cites Z1.9, which is only a sketch. It is now independently supplied by the audit's Ψ^L, which has a full posterior edge [e₁,e₂] with T1 = B_u.

### 2.2 Lemma Z1.2, Lemma Z1.3, Cor. Z1.4: CORRECT

**Z1.2.** It is correct as stated. (K) uses supp φ(p) ⊆ supp p.

**Z1.3.** The standard no-retraction argument is complete:
- φ(F) ⊆ F by face-respect;
- the straight homotopy on ∂F stays in carrier faces;
- the case dim F = 1 is covered by S⁰.

**Z1.4.** Add "continuous" to the description of the reparametrisation, since it is a hypothesis of Z1.2. Also note that continuity in measure of w ↦ B_w on W(Ψ) = Δ is automatic for an additive field with a.e.-unique Bayes models (pointwise a.e. convergence of argmins).

Z1.4's list of obstruction types ("a 2-cell whose boundary is mapped essentially") is misleading; see §2.6.

### 2.3 Lemmas Z1.5, Z1.6 and Theorem Z1.7: CORRECT

**Z1.5.**
- (a): every piece equals v_{k′,k}h_k > 0 at e_k, and the convexity argument is right.
- (b): on S_o the max is at max(h_j,h_l), so g_o is affine.

**Z1.6, case A.**
- u, x_j, x_l are non-collinear because they lie on two distinct arms, off u. Hence c′·u ≠ 0.
- c′·e_o = 3c′·u − c′·e_j − c′·e_l > 0.
- On S_o, c′ is positive at both ends, matching "O on all of S_o".

**Z1.6, case B.** On S_j, w_o ≤ 1/3 < θ. Correct.

**Z1.7.** ρ_k ≤ 3η/2 < 1, φ_k = id on S_k ∩ N_k, the pasting is valid and φ is face-respecting. Lemma Z1.2 then applies.

**Scope.** "No (C)-ties" means (Csel) at selected models. Global (C) for Ψ^★ is not proved. The audit's radial device would give it once w·c′(h) = 0 is shown to be null for each w.

### 2.4 Prop Z1.8: GAP, fixed here

The argument is sound:
- O–S boundary points lie on the single line {w·(ℓ(O)−ℓ(S)) = 0}, so ℓ(S) ≠ 0 is harmless;
- at x₂, x₃ and z the posterior passes O → S, never O → M, because min < max = 0 there;
- the dense-set argument is the standard one.

The weakness is the all-ε claim, which rested on samples at three values of ε. Here is a symbolic witness, PROVED.

**Homogeneous coordinates.** For o = 1 and h = (−1, t₂, t₃):
- x₂ = (1, r₂, 1);
- x₃ = (1, 1, r₃);
- z = (At₂, 1, 0);

with r₂ = min((1−t₃)/(At₂), (1−At₃)/t₂) and r₃ = min((1−t₂)/(At₃), (1−At₂)/t₃).

**The determinant.**

  det[x₂; x₃; z] = (1 − At₂) − r₃(1 − At₂r₂).

On the open square 0 < t₂, t₃ < 1/(A+1):
- D < 2/(A+1) + λ/(A+1) = 1, so the pair is automatically in case A;
- r₂ = (1−t₃)/(At₂) and r₃ = (1−t₂)/(At₃);
- hence **det = (A−1)(1 − (A+1)t₂)/A > 0**.

This square has positive measure for every ε ∈ (0,1), which proves Z1.8 for every ε.

**When collinearity occurs.** It occurs exactly when t₂ ≥ 1/(A+1), case A. Then x₂, x₃ and z all lie on constraint (a), {w₁ = At₂w₂ + t₃w₃}. This explains Z1's 11–16 collinear cases out of 200.

**Check.** `z18_symbolic.py`, CHECKED: ε ∈ {1/1000, 1/20, 3/10, 1/2, 4/5, 99/100}, 900 case-A pairs, crossings computed independently with Z1's root finder. Both the formula and the classification have 0 failures.

### 2.5 Remark Z1.9: CORRECT for its claims, with an addition

`z19_check.py`, CHECKED:
- T1 = B_u: 0 of 12 000 mismatches, including all D_o pairs hit;
- the edge [e₁,e₂] is posterior: 0 of 9000;
- the other edges are posterior below ratio 1/(2A): 0 of 18 000.

I checked the 1/(2A) bookkeeping by hand. On Q₃ ∩ D₃, At₂ − λt₁ ≥ t₂ ≥ 1/(2A).

**Addition (CHECKED).** At interior weights near e₁, the field's Bayes models are **not coherent**.
- The mechanism: on gambles (−a, 1, −b) in the strip D₂ (small a, b ≈ 1/A), the modified O-line accepts a thin bump beyond the cube's straight O-boundary.
- Exact certificates (g₊ and g₋ strictly accepted, g₊ + g₋ strictly not accepted) were found at all 6 tested weights, w ∈ {(.9,.06,.04), (.95,.03,.02), (.8,.15,.05)} for ε ∈ {1/10, 3/10}.

So Z1.9 gives exactly what it says: u plus the edges, via plateaus or retractions. It is no candidate against Z1.C. This is consistent with Y3.6.

### 2.6 The interpretive claims: WRONG

The following statements are false:
- Z1 §0, "Plain-English status": "what additive rankings cannot do starts as soon as the index set encloses a two-dimensional region, or contains a full edge together with the arms".
- §4, "Meaning": "adding any loop … produces a third forced point".
- §5.3–4: "filling obstruction (a 2-cell …)"; "the non-additive target … the loop L₁₂".

**Counterexamples.**
- The audit's Ψ^L realises the posterior on L₁₂, which is a loop with a full edge and two arms.
- Prop AA4.1 below gives additive closed selections through T1 on index sets that enclose any 2-D region, using Z1's own field Ψ^★.

What survives is precisely Prop Z1.8: the *posterior* family on all three arms *plus* a full edge.

### 2.7 Conjecture Z1.C: open, well posed

The statement is precise enough after one change: allow T1 = B_{w*} for any interior w*, or say explicitly that it is rescaled to u.

The heuristic blow-up reduction is not a proof, as the author says. Z1.9 is not a counterexample (§2.5). By Prop AA4.1, Z1.C is not needed for any index-set obstruction. It is a question about the geometry of W(Ψ).

---

## 3. Z2

### 3.1 Lemma Z2.1

- **(a), (b): CORRECT.**
- **(c): GAP.** "T1 competitive on Ω" with complete orders gives undominatedness in the strict sense. It does not give (R4) or "tied with no other model". Fix: add "T1 is undominated and tied at every world only with itself". The stated example (a.e.-unique Bayes) has both properties.
- **Consequence "Y3.C false": CORRECT.** It duplicates Z1.1.

### 3.2 Lemma Z2.2, Corollary Z2.2′, Lemma Z2.3: CORRECT

**Z2.2** uses protection of M ∈ C_L; that is legitimate.

**Z2.2′.** Change the competitor to "accept g on the non-null set where g₁, g₂ > 0 > g₃ and T1 is *silent*". Where T1 accepts −g, accepting g as well would produce ×.

**Z2.3 and the Φ_l remark.** Both are correct. The claim "L(C_q) → L(T1)" also needs inf_{Φ_l} L_l = L_l(T1), which holds:
- mix T1 by Lyapunov with a model better at i and j;
- T1's u-optimality gives the lower bound.

### 3.3 Lemma Z2.4a and Theorem Z2.4: CORRECT

**|J| = 2.** The separation argument is correct. If the line crossed leg l, all three vertices would lie on the side opposite a ∈ Δ°.

**|J| = 1.** I verified n·x_j = 0 and n·a = σ(a_k+a_l)s_j/((1−s_j)a_j+s_j) symbolically. The sign pattern is σ, σ, −σβ.

**|J| = 0** means a unanimous g; n = g is then right.

**Theorem Z2.4.** The map φ is continuous and face-respecting, and continuity in measure holds along the legs.

**Global (C) paragraph: GAP.** The claim that w·n(h) − w·n(−h) is "non-constant on each piece" is asserted, not shown. Two ways to fix it:
1. Apply the audit's radial device: multiply n(−h) by f(|h|). The leg decisions are unchanged, since at most one vector is positive on the legs. What remains is nullity of {w·n(±h) = 0}:
   - for |J| = 1 this is a level set of β, which is strictly monotone in s_j;
   - for |J| = 2 it is the condition w ∈ line(x_j, x_k), a codimension-1 condition in (s_j, s_k).
2. Give explicit non-vanishing witnesses on each piece.

### 3.4 Thm Z2.5: CORRECT, with the same (C) GAP

**Edge pinning.**
- A coherent edge Bayes model is edge-supported: g with g_i, g_j > 0 is accepted whatever g_l is. So it depends on (g_i, g_j) only, and the switching odds depend on x alone.
- Every strictly guiding additive field has acceptance-vector form n = ℓ(S) − ℓ(M), because × is never Bayes. So pinning applies to all additive fields, not just a subclass.

**(E1) and (E2).** Verified, with b = 1/(2+λ) = 1/(A+1). That identity is what makes z = 1 − Ay ≤ b on T1's broken line, so the (E2) bookkeeping on [b, 1/A] is right.

**Product condition and credal interval.** Verified, including [2r/(2+λ), Ar] for r ≤ 1/2 and [1/A, A] at the midpoint.

**"Only at u".**
- Interior weights: the limit y → 0 in (E1) forces w_i = w_j for each pair.
- Boundary weights: the Bayes model is edge-supported, but T1 is not.

**Global (C).** "Global (C) by the argument of §2" inherits the §3.3 gap. The same fix applies: the radial device leaves u and all boundary decisions unchanged.

### 3.5 Theorem Z2.6: CORRECT

**W is closed** (Z2.2). T1 ∈ C_L because C_{p₀} ~ T1 forces C_{p₀} to be u-Bayes, hence C_{p₀} = T1.

**W is open.**
- Step 1: convexity of the range; supp w_n ⊆ supp p_n.
- Step 2: coherent models are compact in measure (Blaschke selection on the K_n; D_K boundaries are null); Bayes optimality passes to the limit.
- Step 3: the lower-semicontinuity argument is right. If L_i(C*) is the maximum of the range, the inequality is trivial.
- Step 4 and Step 5: no issues.

**Remark.** Hypothesis (i) follows from the conclusion of Z2.C itself. The set of weights at which T1 is Bayes is convex (a normal cone) and lies in G. If it contained some w ≠ u, it would contain [u,w], and u would not be isolated.

### 3.6 Prop Z2.7: CORRECT

**The slope computation.**
- Left of z*: slope −q_k k_S/(Aq_j).
- Right of z*: slope −q_k/(Aq_j).

The hypothesis q_i − q_j < q_k/2 is exactly what gives z* < b = 1/(2k_S).

**The certificate** in `z2_isolation.py` uses the full Bayes advice, including the M/O comparison. Near u, −g is not accepted on this slice, since q_j s(y) + q_k s(z) ≈ 1/(3A²) < q_i. 216/216 certificates, rerun.

**Isolation.** Every q ≠ u within distance about 1/6 of u has a suitable pair (i,j).

**Cosmetic.** The script's docstring calls the result "Prop Z2.4"; the note calls it Z2.7.

### 3.7 Conjecture Z2.C and Q_Z2

**Status of Z2.C.** It remains open; the evidence is heuristic, as stated.

**GAP in the corollary.** The corollary reads "no additive ranking carries a closed selection on ∂Δ ∪ γ". It needs a step that the note omits.

> **No-jump lemma (PROVED).** Suppose an additive field has a.e.-unique Bayes models at every weight of an edge, and some closed competitive coherent selection exists on that whole edge. Then the field has coherent Bayes models at **every** weight of the edge.
>
> *Proof sketch.* Suppose (a,b) is a gap. Take p₀ at the frontier between indices with weight ≤ a and indices with weight ≥ b. Then Steps 2–4 of Z2.6 make C_{p₀} equal to Bayes limits at some a′ ≤ a and b′ ≥ b. So it is Bayes on [a′, b′], which contradicts the gap.

Without the uniqueness hypothesis the corollary does not follow from Z2.C. So add uniqueness at boundary weights to the corollary, or handle non-unique fields separately.

**Scope (new).** The audit's Ψ^L has a.e.-unique coherent posterior Bayes models on the full edge [e₁,e₂], with T1 = B_u, and u is **not** isolated in G (the arms lie in G). So:
- coherence on one edge never forces isolation;
- Z2.C, if true, must use at least two edges.

By edge pinning, Z2.C is a statement about six increasing functions s_ij, subject to:
- (E1) and (E2);
- the product conditions;
- interior coherence.

I recommend stating it in that form.

**Q_Z2.** The question itself is legitimate. The gloss "such a triple must violate (A1)" is **unsupported**. Z2.6 is a theorem about one additive representation. A non-additive triple has no canonical "Bayes" notion. Even if it is represented by some numeric L′ with a convex range, it can escape through isolation failing for *its own* G′, or through (A2) or (A3).

Correct statement: an escape must break (A1), (A2), (A3) or isolation for every numeric representation it admits, or admit none.

---

## 4. Referee's nearby results

**Proposition AA4.1 (localisation of additive obstructions; PROVED).**

- **(a)** Let Ψ be Ψ^★ (Z1) or Ψ^Y (Z2). Let I ⊆ Δ be closed and contain **no full closed edge**, and let P₀ ⊆ I ∩ Δ° be closed. Then there is a closed selection on I with C_p = T1 for p ∈ P₀ that satisfies (K) on supp p, (R4), (Csel), closed sections and the fixed plan V(p,i,X) = {q ∈ I : Ψ_i(C_q) > Ψ_i(X)}.
- **(b)** Let Ψ be the audit's Ψ^L (with §2a), and let I ⊆ Δ∖{e₃} be closed. Then the same holds, and Ψ^L also satisfies global (G), (IB) and (C).

By relabelling, (b) holds with e₃ replaced by any vertex.

*Proof.*
- **The tree.** Let Y be a finite tree in W(Ψ) on which w ↦ B_w is continuous in measure:
  - in (a), Y = Σ, the star or tripod;
  - in (b), Y = [u,e₁] ∪ [e₁,e₂] ⊆ L₁₂.
- **φ₀ on the boundary trace.** Define φ₀ on the closed set A := (I ∩ ∂Δ) ∪ P₀ as follows.
  - In (a), on each edge pick x_ij ∉ I. Send the points of I ∩ [e_i,e_j] on e_i's side of x_ij to e_i, and the rest to e_j.
  - In (b), let φ₀ = id on I ∩ [e₁,e₂], φ₀ ≡ e₁ on I ∩ [e₁,e₃], and φ₀ ≡ e₂ on I ∩ [e₂,e₃]. These pieces avoid e₃.
  - In both cases put φ₀ ≡ u on P₀.
- **Properties of φ₀.** It is continuous, because it is locally constant across the gaps and agrees at the vertices. It is face-respecting, because each boundary point goes to a vertex in its support, or to itself.
- **Extension.** Y is an absolute retract (a finite tree), so φ₀ extends to a continuous φ : I → Y (Borsuk–Dugundji). Face-respect is vacuous at interior points.
- **Conclusion.** Lemma Z1.2 applies. ∎

**Consequences.**
1. Every additive exclusion of T1 uses an index set containing **all three vertices and a full edge**. Enclosed 2-D regions, loops and T1 joined to a full coherent edge are additively harmless. The one exception is I = Δ itself, which by Z1.3 forces W = Δ (Thm gm).
2. In particular, for every r > 0, the set Δ ∖ B(e₃, r) carries an additive system through T1 with all the selected-model clauses and global (C). Thm gm's obstruction therefore cannot be localised away from any vertex.
3. **Minimal open additive configuration (recommended diagnostic).** Is there a strictly guiding additive field with T1 = B_u for which W(Ψ) contains a connected set holding u, the full edge [e₁,e₂] and e₃? Z1.8 answers no for the posterior star plus edge. Every other family is open.
4. Cor. Z2.4′ is now correct as stated, and in sharper form.

---

## 5. Files

- `AA4_referee.md`: this report.
- `aa4ref_py/loop_exact.py` / `.out`: exact interval check of the audit's loop field, the third-arm control and the §2a polynomial identity.
- `aa4ref_py/z18_symbolic.py` / `.out`: symbolic witness for Z1.8 and the collinearity classification.
- `aa4ref_py/z19_check.py` / `.out`: the claims of Z1.9 (CHECKED), plus incoherence certificates near e₁.
- `aa4ref_py/rerun/`: reruns of every supplied script; all identical to the stored outputs.
