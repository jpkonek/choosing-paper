# REF73b: referee report on Theorem D′ (DPR73 §2 and REF73 §5)

27 Oct 2026. Independent referee. Hand checks throughout. One script: `ref73b_py/lp_m3.py`, an exact linear-programming check of the three-ball example.

Labels: PROVED / CHECKED / WRONG / UNCLEAR. "Slip" means a local error that does not affect the conclusion.

## Verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | **Theorem D′** (DPR73 §2): (G) + (SC) + (CAm) + (TT) imply that every incoherent model is dominated, in setting (S) | **PROVED.** I checked every line. There are no gaps. Two slips concern only the "explicit dominator" remark (§1.8). The hypotheses can be weakened (§4). |
| 1.1 | Lemma 1 (undominated ⇒ (U1)) | PROVED |
| 1.2 | Lemma 2 (tie lemma) | PROVED. It uses only the three-model case of (SC), and (TT) once. |
| 1.3 | Lemma 3 (consolidations of undominated models are ties, and are undominated) | PROVED |
| 1.4 | Lemma 4 and Corollary 4′ (undominated ⇒ (U2)) | PROVED. The triple is a genuine margin triple of order 1 with a uniform margin δ/4. |
| 1.5 | Lemma 5 (V = X⁺ + D_S; closure under sums and midpoints ⇒ coherent) | PROVED. Coherence comes from `lem:identify`(b) together with (M2) applied to ∂V. |
| 1.6 | Lemma 6 (a gap in V gives a consolidation that breaks (U2)) | PROVED. All four margin-triple conditions hold, with a uniform margin. |
| 1.7 | Assembly of the theorem | PROVED |
| 1.8 | Explicit dominator (item 1a) | **CHECKED, with two slips.** (i) The guided rival of X^D is X^D ∪ ((G₁ ∪ G₂) ∩ D_S), not (X^D ∪ G₂) ∖ N. (ii) "At most three models" is a miscount. The correct statement is: at most two margin consolidations, followed by at most one change guided at every world. |
| 1.9 | Item 1b: only uniform-margin triples in small balls are needed; both orders are used | CHECKED |
| 1.10 | Item 1b: "midpoints cannot be dropped: sums alone do not force cones" | **The geometric claim is CHECKED** (example in §1.9). **The claim that the theorem fails for sums-only (CAm) is UNCLEAR**: no ranking is given. Reword it as a remark about the proof. |
| 1.11 | Item 1c (atoms, atomless part with full support) | **CHECKED, with one slip.** The atom–atom case misses the subcase where z lies in N. The repair is one line (§1.10). |
| 1.12 | Item 1d (restricted domain U, an open convex cone containing D_S) | **CHECKED.** The Lemma 6 modification is more complicated than it needs to be. V ⊆ U and s ∈ U hold automatically (§1.11). |
| 2 | Comparison with REF73 §5 | **Both proofs are correct and agree.** There is no disagreement on any result. REF73's Lemma U omits the disjointness of G₁ and G₂, a one-line fix (§2). |
| 3a | R0 satisfies (CAm) at every world, strictly, and (TT) | PROVED. Pointwise-strict margins suffice, for any Ω. |
| 3b | Veto–Brier satisfies (CAm) strictly on U, and (TT) | PROVED |
| 3c | R0 violates exact (CA) | **PROVED, provided an exact triple exists**, for example Gaussian μ on Rⁿ with n ≥ 2 (PRO73 Lemma LT, CHECKED by REF73). If μ admits no exact triple, (CA) holds vacuously. Both reports state this claim without the qualification. |
| 4 | (M3) cannot be dropped (three-ball example) | **CHECKED.** I checked by hand and by exact LP that every margin triple supported by μ is accepted at both worlds by R_g. X* is undominated by the Bayes fact. The counterexample does not need (P). |
| 5 | DPR73 item 4(d): (CAm) + (SC) ⇒ (C3m); the converse fails (R_γ) | PROVED. I checked this as well, although it was not part of the task. |

---

## 1. Line-by-line check of DPR73 §2

**Notation.** ⪰_ω means "at least as good". The paper's Def. 6.1 writes this as X ⪯_ω Y. N = {sup h < 0} and D_S = {inf h > 0}. Both are open in the sup norm.

### 1.0 Setting, measurability and null sets

- **Models and product sets.** Models are measurable for the completion of μ. The sets used are P_X, W^D and the product boxes. Each is the intersection of a product of models with an open subset of E² or E³. Separability of E gives Borel(E^k) = Borel(E)^{⊗k}, so these open sets are product-measurable. Tonelli for the completed product then applies. ✓ (DPR does not say this; it is worth one sentence in the paper.)
- **Supports.** X⁺ := supp(μ|X) is closed. μ(X ∖ X⁺) = 0, because E is hereditarily Lindelöf. ✓
- **Sierpiński.** It applies to the completion of an atomless measure, which is atomless. The sets G_i can be taken Borel. ✓
- **"Pays more at every world" when Ω is uncountable.** DPR (following MU73) defines a margin triple by: for μ⊗³-a.e. (x, y, z), z(ω) > (x + y)(ω)/c for **all** ω.
  - The set {z − (x+y)/c > 0 pointwise} is the complement of an uncountable union of closed sets. For arbitrary Ω it need not be Borel.
  - Read "a.e." as "outside a μ⊗³-null set". This is harmless, because only fixed-ω sections (closed sets) are ever integrated (§3.1).
  - **The theorem never uses such triples.** Every triple built in Lemmas 4 and 6 has a *uniform* margin: inf_Ω(z − (x+y)/c) ≥ κ > 0 for every triple in G₁ × G₂ × G₃, not merely almost every one. The defining set is then closed.
- **Three readings of the margin, as axioms.** (CAm-pt) uses the pointwise-strict margin. (CAm-D) requires z − (x+y)/c ∈ D_S a.e. (CAm-u) requires a uniform κ.
  - As axioms, (CAm-pt) ⇒ (CAm-D) ⇒ (CAm-u), because more triples make a stronger axiom.
  - Theorem D′ needs only (CAm-u).
  - R0 and veto–Brier satisfy (CAm-pt).
  - So nothing is lost under any reading. The theorem is strongest when stated with (CAm-u) (§4).

### 1.1 Lemma 1: PROVED

- The change from X to (X ∪ D_S) ∖ N adds D_S ∖ X, since D_S ∩ N = ∅. It removes X ∩ N.
- Each added gamble is > 0 at every ω, and each removed gamble is < 0 at every ω. So the change is guided by every world.
- If the change is non-null, (G) gives strictness at every world, and so domination.
- Only "everywhere-guided" instances of (G) are used.
- Using N = {sup < 0} rather than {sup ≤ 0} is correct and sufficient.
  - μ{sup h = 0} need not be 0 under (M2). (M2) controls {inf = 0}, not {sup = 0}.
  - The proof never needs it. X ∩ {sup ≤ 0} null comes out at the end from X = D_K a.e.

### 1.2 Lemma 2 (tie lemma): PROVED

- (TT) with Z ~_ω X and Y ⪰_ω Z gives Y ⪰_ω X at every ω.
- At ω₀ with Y ≻ Z, the comparison X ⪰ Y would give the chain Z ⪰ X ⪰ Y, whose last model is strictly better than its first. (SC) with k = 2 forbids this.
- **Only the three-model condition is used.** It is used here and nowhere else.

### 1.3 Lemma 3: PROVED

- (CAm) with context W = X gives X′ ⪰ X everywhere.
- X is undominated, so X′ ≻ X holds at no world, hence X ⪰ X′ everywhere.
- Lemma 2 then transfers any domination of X′ to X.
- The context condition holds in every application: G₁ ∪ G₂ ⊆ X a.e. and G₃ ∩ X null.

### 1.4 Lemma 4 and Corollary 4′: PROVED

**Step 1.**
- The y-section of W^D at (x, z) ∈ P_X is D_S ∩ (z − x − D_S).
- It is open and contains (z − x)/2, since both (z − x)/2 and z − x − (z−x)/2 lie in D_S. By (M3) it has positive measure.
- Tonelli gives μ⊗³(W^D) = ∫_{P_X} μ(section) > 0. ✓

**Steps 2–4.**
- Countable union over j, then a countable cover by products of δ/8-balls.
- For points in the same δ/8-ball, ‖·‖ < δ/4. So inf(z − x − y) > δ − 3δ/4 for **every** point of the box. ✓

**Steps 5–6.**
- Tonelli gives the three positive masses. By (U1), μ(D_S ∩ X ∩ B₂) = μ(D_S ∩ B₂).
- With m < μ(D_S ∩ X ∩ B₂)/2, the set (D_S ∩ X ∩ B₂) ∖ G₁ still has mass > m. ✓

**Margin-triple audit.**
- *Masses:* m, m, m, as required for c = 1.
- *Disjointness:* G₃ ⊆ E ∖ X, and G₁, G₂ are disjoint by construction.
- *Margin:* inf(z − x − y) ≥ δ/4 for every triple. This is a uniform margin.
- *G₃ misses the model:* G₃ ∩ X = ∅.
- *Conclusion:* X^D misses G₂ ⊆ D_S, which is non-null. ✓

### 1.5 Lemma 5: PROVED

**(a) V ⊆ X a.e.**
- Lindelöf reduces V to countably many translates x_k + D_S.
- Pick z ∈ A ∩ supp(μ|A) with 3δ = inf(z − x_k). Then, for x ∈ B(x_k, δ) and z′ ∈ B(z, δ), inf(z′ − x) > δ.
- μ(X ∩ B(x_k, δ)) > 0 because x_k ∈ X⁺. μ(A ∩ B(z, δ)) > 0, with A ⊆ E ∖ X.
- So μ⊗μ(P_X) > 0. ✓

**(b) X ⊆ cl V a.e.** ✓

**(c) cl V + D_S ⊆ V.** ✓ This also uses V + D_S ⊆ V, which is not stated but holds because D_S + D_S ⊆ D_S.

**(d) D_S ⊆ X⁺, D_S ⊆ V, and V ∩ {sup ≤ 0} = ∅.**
- D_S ⊆ X⁺ follows from (M3) and (U1). Then D_S ⊆ V, writing d = (d − t𝟙) + t𝟙.
- For the last part: V is open, so v ∈ V gives v − t𝟙 ∈ V ∩ N. That is a nonempty open set, which has positive measure by (M3), against (U1). ✓

**(e) Closure under sums and midpoints ⇒ coherent.**
- An open midpoint-convex subset of a normed space is convex (dyadic combinations plus openness). ✓
- Positive homogeneity: the λ < 1 trick and doubling. ✓
- So V is a convex cone, D_S ⊆ V and 0 ∉ V. `lem:identify`(b) gives the credal set K = K_V with D_K ⊆ V ⊆ C_K.
- **Where coherence comes from.**
  - C_K is closed, so cl V ⊆ C_K. D_K ⊆ V and V is open. Hence cl V ∖ V ⊆ C_K ∖ D_K = {P_K = 0}, which is null by (M2).
  - (a) and (b) give V ⊆ X ⊆ cl V a.e. So X = V = D_K a.e.
- **There is no openness or boundary issue.** Openness of V is what makes the boundary exactly cl V ∖ V. (M2) is needed for the single credal set K_V, which is not known in advance, so the full (M2) is used. This is the only use of (M2) in the theorem.

### 1.6 Lemma 6: PROVED

I recomputed every estimate.

**Balls around v_i′.** ‖v_i′ − v_i‖ = η, so B(v_i′, r) ⊆ B(v_i, η + r) ⊆ B(v_i, 2η) ⊆ V ⊆ X a.e. ✓

**The ball around z₀.**
- For z ∈ B(z₀, r): inf(s − z) ≥ η/c − r ≥ η/2 − η/8 > 0.
- (s − D_S) ∩ cl V = ∅, because w ∈ cl V with s − w ∈ D_S would put s in cl V + D_S ⊆ V.
- So B(z₀, r) ∩ X is null, by (b). ✓

**Margin.**
- z₀ − s′ = (η/c)𝟙. So inf(z − (x+y)/c) ≥ η/c − r − 2r/c.
- This is 5η/8 for c = 1 and η/4 for c = 2, for **every** triple. ✓

**The ball L₀.**
- ‖(v₁′ − 3r𝟙) − v₁‖ = η + 3r, so L₀ ⊆ B(v₁, η + 4r) = B(v₁, 1.5η) ⊆ V.
- For x ∈ B(v₁′, r) and w ∈ L₀, inf(x − w) > 3r − 2r = r.
- So L₀ ∩ B(v₁′, r) = ∅. ✓

**Masses.** m < μB(v₂′, r)/2 leaves room for G₂ off G₁. m < μB(z₀, r)/c gives G₃ of mass cm. ✓

**Margin-triple audit.**
- *Masses:* m, m and cm.
- *Disjointness:* G₃ ⊆ s − D_S, which misses cl V ⊇ G₁ ∪ G₂.
- *Margin:* uniform.
- *Context:* G₁ ∪ G₂ ⊆ X a.e. (choose G_i inside X), and G₃ ∩ X null. ✓

**X′ violates (U2).**
- L = L₀ ∖ G₂ has μ(L) > μ(L₀)/2.
- L misses G₁ and G₂, and also G₃ (which misses cl V). L ⊆ X a.e., so L ⊆ X′ a.e.
- G₁ ∩ X′ = ∅.
- So P_{X′} ⊇ L × G₁ up to null sets, which has measure ≥ μ(L)·m > 0. ✓

### 1.7 Assembly: PROVED

The chain is: Corollary 4′, then the contrapositive of Lemma 5(e), then Lemma 6, then Lemma 3, then Corollary 4′ for X′. This is a contradiction.

(M1) is never used. (R), (I), (P) and maximality are never used. Atomlessness is used only through Sierpiński.

### 1.8 Explicit dominator: CHECKED, with two slips

**Slip (i).**
- X satisfies (U1), so D_S ∖ X^D = ((G₁ ∪ G₂) ∩ D_S) ∖ G₃ a.e. G₁ may meet D_S.
- G₃ ∩ N = ∅. Every z ∈ G₃ satisfies z > x + y pointwise for some x ∈ G₁ with sup x ≥ 0 (a.e. x ∈ G₁, since X ∩ N is null) and some y ∈ D_S. So sup z > 0.
- Hence the guided rival is (X^D ∪ D_S) ∖ N = X^D ∪ ((G₁ ∪ G₂) ∩ D_S) a.e.
- The argument is unaffected. Only the displayed formula is wrong.

**Slip (ii).**
- In the (U1) + (U2) branch, the dominator is one of X′, the guided rival of X′, X′^D, or the guided rival of X′^D.
- These are four candidates, not "at most three".
- The correct description is: at most two uniform-margin consolidations, then at most one change guided at every world. Lemma 2 is applied once per tie.

### 1.9 Item 1b

- "Only uniform-margin, small-ball triples are used; both c = 1 (Lemma 4) and c = 2 (Lemma 6, when midpoint closure fails) occur": CHECKED.
- **"Sums alone do not force cones": the geometric claim is CHECKED.**
  - Example: E = R², V = D_S ∪ {h₁ + h₂ > 1}.
  - V is open, closed under sums, satisfies cl V + D_S ⊆ V, contains D_S and misses {sup ≤ 0}.
  - It is not convex: the midpoint of (−10, 11.5) and (0.1, 0.1) is (−4.95, 5.8), which lies outside V.
  - So the proof needs midpoints.
- **The theorem-level claim, that sums-only (CAm) does not imply D′, is UNCLEAR.** That would need a ranking satisfying (G), (SC), (TT) and sums-only (CAm) that leaves such an X undominated. None is given. Reword it as "the proof uses both orders".

### 1.10 Atoms (item 1c): CHECKED, with one slip

**Atom locations.** By (M2), atoms lie in D_S ∪ N. If inf a ≤ 0 ≤ sup a, then S is connected and q ↦ q(a) is continuous, so some state q has q(a) = 0, and then μ{q = 0} > 0. ✓

**Pairs in P_X that involve an atom.**
- *Diffuse x and atom z:* DPR's argument is correct.
- *Atom x and diffuse z:* DPR's argument is correct.
- *Atom–atom pairs (slip):* DPR treats only z ∈ D_S, where the atom z would have to lie in X. If instead z ∈ N, then x ∈ z − D_S ⊆ N, so x is an atom in X ∩ N, against (U1). Add this line.

**The rest is correct.**
- (U1) is for μ. (U2), and Lemmas 4–6, run with μ_c. This needs (M3) for μ_c, and (M2) for μ_c, which follows from (M2) for μ.
- Choosing G_i off the countable set of atoms makes μ-masses equal μ_c-masses. So the triples are margin triples for μ.
- X = D_K holds μ_c-a.e. It extends to the atoms because both X and D_K contain the D_S-atoms and miss the N-atoms.

### 1.11 Restricted domain (item 1d): CHECKED, with a simplification

Let U be an open convex cone with D_S ⊆ U. U + D_S ⊆ U, because u + d = 2(u/2 + d/2).

**Lemma 1.** The guided rival lies in U.

**Lemma 4.** For (x, z) ∈ P_X with x ∈ U, z ∈ x + D_S ⊆ U automatically. So G₃ can be taken in U.

**V ⊆ U.**
- X⁺ ⊆ cl U.
- cl U + D_S ⊆ U: write u + d = u_n + (u − u_n + d) with u − u_n + d ∈ D_S for large n.

**Lemma 6.**
- s = (v₁ + v₂)/c ∈ U automatically, since U is a convex cone containing V.
- So η can be chosen with B(s, 2η) ⊆ U. Then B(z₀, r) ⊆ B(s, η/c + r) ⊆ U.
- DPR's extra steps (shifting the v_i, "V ∖ cl U open and null") are correct but unnecessary.

**Lemma 5(d).** N ∩ U = ∅ unless U = E. If h ∈ U ∩ N, then −h ∈ D_S ⊆ U, so 0 ∈ U, and an open cone containing 0 is E.

**Conclusion.** X = D_K a.e. with D_K ⊆ V ⊆ U. ✓

---

## 2. Comparison with REF73 §5

**The skeleton is the same.**
1. The guided rival gives (U1).
2. A consolidation with G₂ ⊆ D_S gives upward closure modulo μ. This is REF73's Lemma U: "no x ∈ X⁺ and z ∈ (E∖X)⁺ with z − x ∈ D_S", which is equivalent to (U2).
3. Incoherence gives a witness triple. REF73 uses MU73's Lemma W, which REF73 itself rated PROVED. DPR is self-contained through Lemma 5. I checked that the two are equivalent.
4. Shift G₁ upward so that part of X lies strictly below it. Consolidating removes G₁ and opens a gap, against upward closure.
   - DPR uses the ball L₀ below v₁′.
   - REF73 uses x = x₀ + t𝟙 below x₁ = x₀ + η𝟙.

**REF73 step 3, rechecked.**
- {t : ‖x₀ + t𝟙 − y₀‖ ≤ 2ρ} is an interval of length ≤ 4ρ, so a good t ∈ (η/8, η/2) exists once ρ < 3η/32.
- dist(x, B(x₁, ρ)) ≥ η/2 − ρ.
- inf(z − x) ≥ η − t − ρ > 0. ✓

**One omission in REF73's Lemma U.** The balls B(x, ρ) and B(d, ρ) may overlap, so G₁ and G₂ must be chosen disjoint. Sierpiński with m < ½ min μ(X ∩ B_i) does this, as in MU73's Lemma T. This is a one-line fix.

**No disagreements.**
- Both reports say R0 ∈ class and R0 ∉ exact (CA). Both omit the qualification that an exact triple must exist (§3c).
- Both say veto–Brier satisfies (CAm) and (TT).
- Both say R_GC with margin generators protects coherent models for two worlds.
- REF73 shows R0 is outside exact (CA) via the hull test with (M2). DPR's direct argument (§3.1) needs no (M2) and is cleaner. Both are correct.
- DPR adds the atoms and domain sketches, the explicit dominator, R_γ, and the (M3) example. REF73 adds nothing that DPR lacks for this theorem.

---

## 3. Membership

### 3a. R0: (CAm) at every world, strictly, and (TT). PROVED

**No coherent model could make the change.**
- Suppose G₁ ∪ G₂ ⊆ D_Q a.e.
- For a.e. z ∈ G₃, pick (x, y) ∈ D_Q² with p := z − (x+y)/c ≥ 0. This is possible by Tonelli, using the fixed-ω-free formulation "outside a null set".
- Then P_Q(z) ≥ (P_Q(x) + P_Q(y))/c + P_Q(p) > 0, because P_Q is superadditive and positively homogeneous, and q(p) ≥ 0.
- So G₃ ⊆ D_Q a.e. This contradicts G₃ ∩ D_Q null with μ(G₃) > 0.
- This handles consistent and inconsistent G₁ ∪ G₂ together. It needs neither (M2) nor a uniform margin. ✓

**The score rises.**
- π = (μ|G₁ ⊗ μ|G₂ ⊗ μ|G₃)/(cm²) has marginals μ|G₁, μ|G₂ and μ|G₃/c.
- m_ω(W′) − m_ω(W) = ∫(cz(ω) − x(ω) − y(ω)) dπ.
- At each fixed ω the integrand is > 0 off a null set, because its zero set is closed and contained in the failure set. It is integrable by (M1). So the difference is > 0. ✓
- Clause (ii) of Def. 6.1 then gives W′ ⪰_ω W. Since R0 has no ties between distinct models (`prop:structure`(b)), the comparison is strict.

**(TT).** Z ~_ω X forces Z = X a.e. Independence (`prop:structure`(a)) gives Y ⪰_ω Z iff Y ⪰_ω X. ✓

### 3b. Veto–Brier on U: (CAm) strictly, and (TT). PROVED

**The veto level a_i does not rise.**
- v_i ∈ Δ is ≥ 0 and nonzero, and cz > x + y pointwise. So v_i·(cz) > v_i·(x + y).
- t ↦ [−t]⁺ is non-increasing and subadditive. Hence c[−v_i·z]⁺ ≤ [−v_i·x]⁺ + [−v_i·y]⁺, so Δa_i ≤ 0.

**The Brier level b_i falls.** Δb_i = −∫(cz_i − x_i − y_i) dπ < 0.

**Conclusion.**
- Lexicographically, W′ ≺_i W strictly, at every i.
- Total preorders give (SC) and (TT). (G) holds by Thm `thm:vb`(a).
- The setting (Lebesgue-equivalent μ on Rⁿ, U = {p·h > 0}) satisfies the hypotheses of item 1d: μ is atomless, satisfies (M2) and (M3), and U is an open convex cone containing D_S.
- So Theorem D′ on U applies. It only reproduces `thm:vb`(c), "every incoherent model on U is dominated", which is a consistency check.
- Veto–Brier fails (P), since D_{p} = U is dominated. So it lies outside the class 𝓒 of DPR73's item 5.

### 3c. R0 violates exact (CA): PROVED, with a qualification

**Sum triple.** For S = id + T with S_*(μ|G₁) = μ|G₃, the increment is ∫_{G₁}[S h − h − T h](ω) dμ = 0.

**Midpoint triple.** For S_*(μ|G₁) = ½μ|G₃, ∫_{G₃} = 2∫_{G₁} ∘ S = ∫_{G₁} + ∫_{G₂}. The increment is again 0.

**Neither clause of Def. 6.1 applies.**
- Guidance at ω would need T h(ω) < 0 and h(ω) < 0 for a.e. h ∈ G₁, while S h(ω) > 0 for a.e. h. That is impossible, because S h = h + T h (or its half).
- Clause (ii) needs a strict increase, and the increment is 0.
- So R0 accepts neither direction at any world.

**Qualification.** This needs at least one exact triple. Context W = G₁ ∪ G₂ then works. Exact triples exist, for example, for Gaussian μ on Rⁿ with n ≥ 2 (PRO73 LT) and for locally constant densities on R² (MU73 §1.1). For a μ that admits none, exact (CA) is vacuous and R0 satisfies it. The correct statement is: "R0 violates (CA) whenever μ admits an exact matched triple."

---

## 4. Sharpness of (M3): CHECKED

**Setting.**
- μ is Lebesgue measure on three sup-norm balls of radius 0.05 about a = (−1.5, 1), b = (1, −1.5) and n = (−1, −1).
- μ is atomless and satisfies (M1) and (M2). (M3) fails.
- X* = B(a) ∪ B(b) is incoherent: positivity on B(a) needs q₁ < 0.4, and positivity on B(b) needs q₁ > 0.6, up to O(r).

**The supported margin triples.** I enumerated them by exact LP: for each ball combination and c, maximise the slack t subject to z − (x+y)/c ≥ t𝟙. The list agrees with DPR and MU73:
- c = 2: within-ball triples only, (a,a→a), (b,b→b) and (n,n→n);
- c = 1: (a,n→a), (b,n→b), (n,n→a), (n,n→b) and (n,n→n), together with the symmetric orders.
- No triple pairs B(a) with B(b).

**Minimum of c·g_ω(z) − g_ω(x) − g_ω(y) over the closed feasible set.**

| Combination | World 1 | World 2 |
|---|---|---|
| a, n → a | 0.85 | 0.65 |
| b, n → b | 0.85 | 0.917 |
| n, n → a | 0.35 | 4.75 |
| n, n → b | 2.85 | 1.383 |
| n, n → n | 0.85 | 0.85 |
| within-ball midpoints | 0 on the closure | 0 on the closure |

For the within-ball cases g_ω is linear on the ball, so the integrand is a positive multiple of the margin and is > 0 on the actual (strict) set. If a G_i straddles balls, Δs is a sum over positive-mass sub-combinations, each of which is admissible, so Δs > 0.

**R_g accepts every margin consolidation at both worlds.** A margin consolidation is unavailable to every coherent model, by §3a; that argument uses neither (M2) nor (M3). So it is never "dangerous", and R_g accepts it because s rises at both worlds.

**The other hypotheses.**
- Every accepted non-null change strictly raises s_ω. This gives (SC), no ties between distinct models, and hence (TT).
- (G) holds because g is truth-directed, and a refusal happens only at a non-guided world.

**X* is undominated.**
- X* is the a.e.-unique maximiser of Σ p_ω s_ω: the Bayes values are ≥ 1.3 on B(a), ≥ 0.43 on B(b) and < 0 on B(n).
- So for any Y ≠ X*, the change from Y to X* raises s at some world where it is accepted, and the reverse is refused there.

So (G), (SC), (TT) and (CAm) hold, and an incoherent model is undominated. **This uses no (P).** (P) is AX72/MU73's additional claim, which I did not re-referee; it is not needed for sharpness. `ref73b_py/lp_m3.py` reproduces the table, and DPR's sampling script also passes.

---

## 5. Corrections to carry forward

1. **Explicit dominator (DPR item 1a):**
   - the guided rival of X^D is X^D ∪ ((G₁ ∪ G₂) ∩ D_S) a.e.;
   - replace "one of at most three models" with "obtained from X by at most two uniform-margin consolidations followed by at most one change guided at every world".
2. **Midpoints remark (DPR item 1b):** reword as "the proof uses both orders; closure under sums alone does not make V convex (example: D_S ∪ {h₁ + h₂ > 1})". Do not claim that the theorem fails without midpoints. That is UNCLEAR.
3. **Atoms (DPR §2.7):** add the atom–atom subcase z ∈ N.
4. **Domain (DPR §2.8):** replace the Lemma 6 modification with "V ⊆ U, so s ∈ U; choose η with B(s, 2η) ⊆ U".
5. **R0 and exact (CA)** (DPR item 4(a′); REF73 verdict 4e and §5): add "whenever μ admits an exact triple".
6. **REF73 Lemma U:** choose G₁ and G₂ disjoint (Sierpiński, small m).
7. **Paper text:**
   - one sentence that separability makes the open sets in E² and E³ product-measurable;
   - define the margin uniformly (below), which also removes the measurability question for uncountable Ω.

---

## 6. Clean statement

**Setting.**
- Ω is any nonempty set. E ⊆ ℓ∞(Ω) is a separable, norm-closed subspace containing 𝟙.
- μ is a finite Borel measure on E satisfying (M2).
- μ's atomless part μ_c has full support. For example, μ is atomless and satisfies (M3).
- Models are μ-completion-measurable sets, modulo μ-null sets.
- (M1) is not needed.

**Uniform margin triple of order c ∈ {1, 2}.**
- Pairwise disjoint non-null models G₁, G₂, G₃ with μ(G₁) = μ(G₂) = μ(G₃)/c.
- There is κ > 0 such that z(ω) ≥ (x(ω) + y(ω))/c + κ for all ω and **all** x ∈ G₁, y ∈ G₂, z ∈ G₃.
- If W ⊇ G₁ ∪ G₂ a.e. and W ∩ G₃ is null, then W′ := (W ∖ (G₁ ∪ G₂)) ∪ G₃.

**Theorem D′.** Let ⪰_ω (one relation per world) satisfy the following:
- **(G_E)** if the change from X to Y is non-null and guided by every world, then Y ≻_ω X at every ω. Strict guidance implies this.
- **(SC₃)** there are no A ⪰_ω B ⪰_ω C with C ≻_ω A. The chain condition implies this.
- **(TT)** if Z ~_ω X and Y ⪰_ω Z, then Y ⪰_ω X.
- **(CAm)** for every uniform margin triple, every such W and every ω, W′ ⪰_ω W.

Then every incoherent model X is dominated. A dominator is obtained from X by at most two uniform-margin consolidations followed by at most one change guided at every world. It need not be coherent. The same holds for models on an open convex cone U ⊇ D_S, with triples and contexts in U.

**Status.**
- PROVED (DPR73 §2, as corrected; independently REF73 §5).
- (M3) cannot be dropped: CHECKED (§4).
- (G) cannot be dropped: trivial.
- Whether (TT) or (SC) can be dropped, and whether midpoints can be dropped: UNCLEAR.

**Nonempty class.** Let μ also satisfy (M1). Then R0 (Def. 6.1) satisfies (R), (G), (I), (SC), (P), (TT), and (CAm) even for pointwise-strict margins. Such μ exist for every Ω and E: the measure of `lem:measure` is atomless. Members of this class satisfy coverage requirements (1)–(4b). Requirement (5), dominance by an *undominated coherent* model, remains OPEN in general.

## Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/REF73b_report.md` (this report)
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/ref73b_py/lp_m3.py` (exact LP check of the three-ball example)
