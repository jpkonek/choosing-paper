# S81 report: reopening selection (S) for sets of desirable gambles

Strand 2 of BRIEF81. No manuscript was modified. Labels: PROVED / CHECKED / CONJECTURE / UNCLEAR / FAILS.

**Convention.** Throughout, I use the application's convention: `Y ⪰_ω X` means "Y is at least as good as X at ω". LDG's condition `c_p ⪯_ω m` in thm:finite is written here as `c_p ⪰_ω X`.

---

## 0. Results first

| # | Claim | Label |
|---|---|---|
| 1 | **(S) fails for the current integral ranking (appshort def:integral) whenever n ≥ 2.** This holds in all three forms: thm:finite, cor:closed-choice and thm:local. For n = 1, (S) holds trivially. | PROVED |
| 2 | **General obstruction (Theorem A / Prop C).** Take any ranking satisfying (S) in finitely many worlds. Then every undominated coherent model is tied at every world with an undominated **precise** model D_r. If the ranking is score-consistent (`Y ⪰_ω X ⇒ s_ω(Y) ≥ s_ω(X)`), then C_L contains only precise models. | PROVED |
| 3 | The lead's sketch is correct as far as it goes. Serving against coherent rivals alone forces c_p = H_ω := {h_ω > 0} for some ω ∈ supp p (Prop 1). Vertex models do serve every rival. The failure is topological: the witnessing sets cannot all be closed. | PROVED |
| 4 | **Possibility 1** (consolidation-guided selection) is blocked for the current ranking. The obstruction lies entirely among coherent rivals, and coherent models admit no consolidations. Hence (S) cannot be derived from (A1)–(A4), coherent admissibility and closure under ties: the integral ranking satisfies all of these and fails (S). | PROVED |
| 5 | **Possibility 2** (coherent all-world ties). Two things fail. Keeping single-world guidance from coherent models together with ties and tie-substitution is inconsistent with admissibility plus closure under ties (Prop B). Declaring all coherent models tied inside the integral ranking violates (A3). | PROVED (both FAIL) |
| 6 | **A modified ranking for which (S) is verified: the coherence-floor ranking R\*.** All almost coherent models are tied at every world. Comparisons with an incoherent model as the worse model use the strict integral score. No incoherent model is ever at least as good as a coherent one. R\* satisfies (A1)–(A4), closure under ties and admissibility of every almost coherent model. It satisfies (S) via thm:finite with c_p = D_p := {p·h > 0}; the *closed-subset* form is used. For arbitrary Ω it satisfies (S) via thm:local. | PROVED |
| 7 | **Possibility 3** (target-relative admissibility). (a) The pure integral-score ranking L_lin is natural and score-consistent, and satisfies (S) via cor:closed-choice. It protects exactly the precise models. (b) By Theorem A, no score-consistent ranking satisfying (S) protects any imprecise target, including every member of the rescaled family M_m of an imprecise M. (c) A target-relative coherence floor R\*_Q, with tie class {D_Q} ∪ {precise models}, satisfies (S) and everything in item 6. | PROVED |
| 8 | **Consistency.** {R\*}, {R\*_Q : Q a credal set} and {L_lin, R\*} each satisfy LDG's (E), (A), (S) and (T), as well as (A1)–(A4). So LDG thm:argument applies directly. Every incoherent model is then dominated by a *precise* model D_{p\*}. The integral ranking cannot belong to any family that LDG's (S) is meant to cover. | PROVED |
| 9 | Selection for the variant that keeps the availability clause (R5 below). The Bayes choice c_p = D_p fails to serve. Whether some other selection works is open. | PROVED (D_p fails) / UNCLEAR (in general) |
| 10 | The integral ranking for infinite Ω under thm:local. Theorem A's proof does not transfer directly. | UNCLEAR |

**The price of (S), in one sentence.** By item 2, any ranking satisfying (S) that leaves an imprecise model undominated must declare that model tied, at every world, with some precise model. Yet in score terms an imprecise D_Q is strictly beaten at every world by a precise model with r ∈ Q (CHECKED for n = 2 below). So the tie is a stipulation, not something accuracy delivers. R\* is the cleanest such stipulation, and Prop B shows that it must also drop single-world guidance out of coherent models.

---

## 1. Setting (finite worlds)

- **Space and measure.** Ω = {1,…,n}, E = ℝⁿ. μ is a finite Borel measure with the Lebesgue null sets and a finite first moment (M1). So μ is atomless and has full support. Boundaries of convex cones are null, which gives (M2) and (M3). Null sets are invariant under h ↦ λh.
- **Scores.** s_ω(X) = ∫_X h_ω dμ, and m(X) = (s_ω(X))_ω ∈ ℝⁿ.
- **Almost coherent models.** By app_long lem:identify(b) under (M2), these are exactly the models a.e. equal to D_Q = {P_Q > 0} for a credal set Q ⊆ Δ.
  - *Precise* models: D_r = {r·h > 0}, r ∈ Δ.
  - *Vertex* models: H_ω = D_{δ_ω} = {h_ω > 0}.
  - *Vacuous* model: V = D_Δ = {h ≫ 0}.
  - Distinct credal sets give distinct models, because D_Q Δ D_{Q'} contains an open set.
- **Coherent class.** C = the almost coherent models. M_L = all models. C_L = the undominated members of C.

**Fact F1 (Bayes uniqueness).** For r ∈ Δ, Σ_ω r_ω s_ω(X) = ∫_X r·h dμ ≤ ∫_{D_r} r·h dμ, with equality iff X = D_r a.e. The reason is that r·h ≠ 0 a.e., by (M2) with Q = {r}.

**Fact F2 (Lyapunov).** The vector measure X ↦ m(X) is ℝⁿ-valued and non-atomic, since it is ≪ μ and μ is atomless. Its range Z is therefore convex and compact.

**Fact F3 (duality).** For credal sets A and B:
- cl D_B = {P_B ≥ 0};
- D_A ⊆ cl D_B ⇔ B ⊆ A;
- D_A ∩ H_ω = D_{conv(A ∪ {δ_ω})}.

*Proof.* If b ∈ B \ A, separate b from A inside the affine hull of Δ. This gives h with min_A a·h > 0 > b·h, so h ∈ D_A and h ∉ cl D_B. The last identity holds because P_{conv(A∪{δ_ω})} = min(P_A, h_ω).

**Fact F4 (perturbation).** For every model Y and δ > 0 there is an incoherent Y' with μ(Y Δ Y') < δ, and hence ‖m(Y) − m(Y')‖ < ε(δ) → 0 by (M1).

*Proof.* If Y is coherent, say Y = D_Q, let Y' = D_Q \ B for a small ball B ⊂ D_Q with 0 ∉ cl B. Suppose Y' were a.e. equal to a cone. Scale-invariance of null sets would then give Y' = λY' a.e. for all λ > 0, which fails for any λ with λB ∩ B = ∅, since μ(B), μ(λB) > 0.

---

## 2. Item 1: (S) for the current integral ranking

**Integral ranking.** Y ⪰_ω X iff the change X → Y is (i) guided at ω, or (ii) available to no almost coherent model and has s_ω(Y) > s_ω(X).

**Two facts about it.**
- It is *score-consistent*: Y ⪰_ω X ⇒ s_ω(Y) ≥ s_ω(X).
- Distinct models are never tied (appshort, "Strict score increase").

**Reduction to thm:finite.** For finite Ω, thm:local reduces to thm:finite. Taking G = Ω forces F = Ω. Then c'_p := c_{θ_Ω(p)} and A_ω(X) := A^Ω_ω(X) satisfy (i) and (ii) of thm:finite. cor:closed-choice is a special case of thm:finite. So it suffices to refute the hypotheses of thm:finite with c_p ∈ C_L.

### Theorem A and Prop C (general obstruction) — PROVED

**Prop C.** Let Ω be finite, n ≥ 1, with μ as in §1. Let L be any ranking on all models that is *score-consistent against incoherent rivals*: whenever Y is incoherent and c ⪰_ω Y, we have s_ω(c) ≥ s_ω(Y). Suppose L satisfies the hypotheses of thm:finite with every c_p ∈ C_L. Then every c ∈ C_L is tied at every world with some c_{p\*} ∈ C_L, and c_{p\*} = D_r a.e. for some r ∈ Δ with supp r ⊆ supp p\*.

*Proof.*
1. Let c ∈ C_L. thm:finite with m := c gives p\* such that c_{p\*} weakly dominates c.
2. Since c is undominated, Lemma lem:ties(a) of LDG ties them at every world.
3. Put F = supp p\* and c' = c_{p\*}. By (i) and (ii) of thm:finite, every model Y has some ω ∈ F with c' ⪰_ω Y. For incoherent Y this gives s_ω(c') ≥ s_ω(Y).
4. Suppose some model Y had s_ω(Y) > s_ω(c') for all ω ∈ F. F4 would give an incoherent Y' with the same strict inequalities, contradicting step 3. So m(c')|_F is weakly maximal in the convex set Z|_F (F2).
5. Separate Z|_F from the open orthant m(c')|_F + int ℝ^F_+. This gives r ∈ Δ_F with Σ_{ω∈F} r_ω s_ω(Y) ≤ Σ_{ω∈F} r_ω s_ω(c') for all Y.
6. Extend r by zeros. By F1, c' = D_r a.e. ∎

**Theorem A.** If L is score-consistent and satisfies (S) (finite Ω), then C_L ⊆ {D_r : r ∈ Δ}.

*Proof.* By Prop C, c is tied with D_r at every world. Score-consistency in both directions gives m(c) = m(D_r). So c attains the maximum in F1, and c = D_r a.e. ∎

**Corollary A1.** (S) fails for the integral ranking whenever n ≥ 2.

*Proof.* The integral ranking is score-consistent and leaves every almost coherent model undominated (prop:consistent). For n ≥ 2 there are imprecise credal sets. ∎

For n = 1, Δ is a single point, C = {H_1}, and H_1 ⪰_1 every model by guidance. So (S) holds trivially.

### Prop 1: the lead's sketch, made exact — PROVED

This proof is independent of Theorem A and uses only coherent rivals.

- **(a) Vertex models always serve.** H_ω ⪰_ω X for every model X. The change X → H_ω adds H_ω \ X ⊆ {h_ω > 0} and removes X \ H_ω ⊆ {h_ω ≤ 0}; the set {h_ω = 0} is null.
- **(b) Only guidance links coherent models.** For a coherent rival X, the change X → c_p is available to X. So clause (ii) cannot apply, and c_p ⪰_ω X iff the change is guided at ω. This is the lead's observation.
- **(c) Against the vacuous model.** If the change V → D_R is guided at ω, then δ_ω ∈ R. Otherwise some open set inside D_R ∩ {h_ω < 0} is added (F3 separation), and that set misses V.
- **(d) Against a precise interior model.** For q interior and the change D_q → D_R guided at ω, we have R ⊆ [q, δ_ω]. The removed set must lie in {h_ω < 0} a.e. So D_q ∩ H_ω ⊆ cl D_R, by openness and full support. F3 then gives R ⊆ conv{q, δ_ω}.
- **(e) Serving forces vertex models.** Suppose c_p = D_R serves every coherent rival at worlds in supp p.
  1. The rival V gives some ω₀ ∈ supp p with δ_{ω₀} ∈ R.
  2. Each rival D_q with q interior gives some ω(q) ∈ supp p with R ⊆ [q, δ_{ω(q)}].
  3. The only vertex on [q, δ_ω] is δ_ω, so ω(q) = ω₀.
  4. Letting q → δ_{ω₀} gives R = {δ_{ω₀}}.

  So **c_p = H_{ω(p)} with ω(p) ∈ supp p**, and by (a) every such assignment serves every model.
- **(f) Closedness fails.** Fix q interior. For ω' ≠ ω, H_{ω'} ⪰_ω D_q fails, by (d), since δ_{ω'} ∉ [q, δ_ω]. So A_ω(D_q) ⊆ {p : c_p = H_ω}, and these sets are pairwise disjoint and closed. Serving makes them cover Δ, with δ_ω ∈ A_ω(D_q), so at least two of them are nonempty. That is impossible in the connected set Δ when n ≥ 2. Equivalently, KKM yields a common point. ∎

**Verdict on the sketch.** It is right that a non-vertex c_p fails against a suitable coherent rival. It is wrong to expect the serving condition alone to fail: vertex assignments pass it. The refutation needs the closed-set step (f).

**The auditor's image constraint.** It holds: the image of p ↦ c_p would have to contain every almost coherent model. Theorem A sharpens it into a contradiction for every score-consistent ranking.

**Exact check (n = 2, standard Gaussian μ, cone models as unions of arcs).** Scores are exact: s₁(arc(α,β)) ∝ sin β − sin α and s₂ ∝ cos α − cos β. Script: `s81py/check.py`.
- In 2·10⁴ random interval pairs there were 0 mismatches against the rule implied by (c) and (d) for n = 2. That rule is: D_{[a,b]} → D_{[c,d]} is guided at world 1 iff c ≥ a and d ≥ b, and at world 2 iff c ≤ a and d ≤ b.
- For every sampled imprecise [a,b], some precise t ∈ [a,b] has s_ω(D_t) > s_ω(D_{[a,b]}) at both worlds. The margin is at least ≈ 0.26 (b − a)². CHECKED.

---

## 3. Item 2: Possibility 1 (consolidation-guided selection) — blocked, PROVED

- **Consolidation never touches the obstruction.** The obstruction in Prop 1 involves only coherent rivals (V and D_q), and coherent models have no consolidations at all. A consolidation needs G₁ ∪ G₂ ⊆ X a.e. and G₃ ∩ X null. For X almost coherent, G₁ ∪ G₂ ⊆ X forces G₃ ⊆ X a.e. (proof of (A4) in prop:consistent). So consolidation supplies no comparison between c_p and any coherent rival. Under the integral ranking those comparisons go only through single-world guidance (Prop 1(b)).
- **There is a structural mismatch.** A consolidation endpoint depends on the rival X. (S) needs c_p to depend on p alone. Consolidation therefore naturally feeds Strand 1's finite-sequence theorem, which allows rival-dependent dominators, not a p-indexed selection.
- **The defence inequality is not the issue.** For c_p = D_p, the Bayes inequality Σ p_ω (s_ω(D_p) − s_ω(X)) > 0 holds for every X ≠ D_p (F1). What blocks the integral ranking is its acceptance rule, not a missing inequality. Theorem A shows that no other choice of c_p helps.
- **Consequence.** (S) is not implied by (A1)–(A4), coherent admissibility and closure under ties. The integral ranking satisfies all of these and fails (S).

---

## 4. Item 3: Possibility 2 (coherent all-world ties)

### 4a. Modifying the integral ranking by accepting all changes between coherent models — FAILS (A3)

**R2.** Add clause (iii) to the integral ranking: "X and Y are both almost coherent".

**Counterexample to (A3), and to all-world-tie substitution.** Take Z = V and X = H₂, which are tied at every world by (iii). Let S be a small ball in {h₁ < 0 < h₂}, and put Y = V ∪ S; Y is incoherent.
- Y ⪰₂ V by guidance, since the change only adds S ⊆ {h₂ > 0}.
- The change H₂ → Y adds nothing, because S ∪ V ⊆ H₂. It removes H₂ \ (V ∪ S), a non-null subset of {h₂ > 0}, so it is not guided at world 2.
- That change is available to the coherent model H₂, so clause (ii) is excluded. Clause (iii) does not apply because Y is incoherent.
- So Y ⋡₂ H₂ although Y ⪰₂ V ∼ H₂.

### 4b. Prop B (impossibility) — PROVED

**Prop B.** Let n ≥ 2. Suppose a ranking satisfies:
- (G1) if the change X → Y is guided at ω, then Y ⪰_ω X;
- all-world-tie substitution: if a and b are tied at every world and c ⪰_ω a, then c ⪰_ω b.

Suppose further that H_{ω\*} is tied at every world with some coherent C' ⊆ H_{ω\*}, C' ≠ H_{ω\*}. Then either H_{ω\*} is dominated, or C_L is not closed under ties.

*Proof.*
1. Write C' = D_{Q'} with δ_{ω\*} ∈ Q' (by F3) and pick q' ∈ Q' \ {δ_{ω\*}}.
2. Let t₀ have t₀(ω\*) = M > 0 small and t₀(ω) = −1 for ω ≠ ω\*. Then q'·t₀ < 0. Take a small ball T around t₀; it lies inside H_{ω\*} ∩ {h_ω < 0 ∀ω ≠ ω\*} and misses cl C'.
3. Put Y = H_{ω\*} \ T. Y is incoherent by the F4 argument.
4. The change H_{ω\*} → Y removes only T ⊆ {h_ω < 0}. It is guided at every ω ≠ ω\*, so Y ⪰_ω H_{ω\*} there.
5. The change C' → Y adds Y \ C' ⊆ H_{ω\*} and removes nothing, since C' ⊆ Y. It is guided at ω\*, so Y ⪰_{ω\*} C'.
6. Substitution through the tie C' ∼ H_{ω\*} gives Y ⪰_{ω\*} H_{ω\*}.
7. So Y weakly dominates H_{ω\*}. Either Y dominates it, or they are tied at every world with Y ∉ C. ∎

**Moral.** If coherent models are to share all-world tie classes, single-world guidance *out of* coherent models must be dropped. Appshort's (A1) asks only for guidance at *every* world, so this is allowed.

### 4c. The coherence-floor ranking R\* — (S) verified, PROVED

**Definition (assume (M1)).**

> Y ⪰\*_ω X iff **(a)** X and Y are both almost coherent; or **(b)** X is incoherent and (Y = X a.e. or s_ω(Y) > s_ω(X)).

An incoherent Y is never ⪰\* a coherent X. A guided non-null change raises s_ω (appshort, "Strict score increase"), so (b) contains single-world guidance *into* any model from an incoherent one. The relation depends only on a.e. classes.

**Axioms.**
- **(A1).** A non-null change guided at every world cannot start at a coherent model (lem:guidedeverywhere of app_long). So X is incoherent, and s_ω(Y) > s_ω(X) at every ω, which gives Y ⪰\*_ω X. Now consider X ⪰\*_ω Y. If Y is coherent, this needs X coherent. If Y is incoherent, it needs s_ω(X) > s_ω(Y). Neither holds, so the comparison is strict.
- **(A4).** Only incoherent models have consolidations (§3). A consolidation raises s_ω by at least ctκ > 0 at every ω (prop:consistent), so clause (b) applies.
- **Ties.**
  - Any two almost coherent models are tied at every world.
  - No mixed ties, because an incoherent model is never at least as good as a coherent one.
  - Distinct incoherent models are never tied, because ties would need strict score increases both ways.
- **(A3).** The only non-trivial ties are between coherent models. If Y ⪰\*_ω Z with Z coherent, then Y is coherent, so Y ⪰\*_ω X by (a).
- **(A2).** Suppose X ⪰\* Y, Y ⪰\* Z and Z ≻\* X.
  - If X is coherent, then Z ⪰\* X makes Z coherent, so Z and X are tied and Z ≻\* X fails.
  - So X is incoherent. Then X ⪰\* Y forces Y incoherent, and likewise Z.
  - With all three incoherent, the comparisons give s(X) ≥ s(Y) ≥ s(Z) > s(X), a contradiction.
- **Admissibility and closure.** Only coherent models are ⪰\* a coherent C, and they are tied with C. So C_L = C, and C_L is closed under ties.

**(S) via thm:finite.** Take c_p := D_p = {p·h > 0}. This is almost coherent: D_p ∪ {h ⪈ 0} is coherent and differs from D_p by a subset of the null set {p·h = 0}.
- For a coherent rival X, set A_ω(X) := Δ. Clause (a) gives c_p ⪰\*_ω X.
- For an incoherent rival X:
  1. Put d_ω(p) := s_ω(D_p) − s_ω(X). It is continuous in p, by dominated convergence: 1_{p_k·h>0} → 1_{p·h>0} off the null set {p·h = 0}, with dominating function ‖h‖.
  2. g_X(p) := Σ_ω p_ω d_ω(p) is > 0 on Δ by F1, since X ≠ D_p. Let ε_X := min_Δ g_X > 0.
  3. Set A_ω(X) := {p : d_ω(p) ≥ ε_X}. These sets are closed. For p ∈ A_ω(X), s_ω(D_p) > s_ω(X), so D_p ⪰\*_ω X.
  4. Since Σ_{supp p} p_ω d_ω(p) ≥ ε_X, some ω ∈ supp p has p ∈ A_ω(X). ∎

The comparison sets {p : d_ω(p) > 0} are open. The proof uses LDG's *closed-subset* form of (S), as the brief anticipated. Whether the cor:closed-choice form also holds is not needed and not checked.

**Arbitrary Ω (separable E containing the constants, (M1), (M2)).** Use thm:local with:
- Θ = S, the states, weak-\* compact and metrizable because E is separable;
- c_θ = D_θ := {θ(h) > 0};
- K_ω(X) = Θ for coherent X, and K_ω(X) = {θ : s_ω(D_θ) − s_ω(X) ≥ ε_X} for incoherent X, where ε_X := min_S g_X and g_X(θ) := θ(m(D_θ) − m(X)) > 0;
- θ_F(p) = Σ p_ω δ_ω and A^F_ω = θ_F^{-1}(K_ω).

Continuity of θ ↦ m(D_θ) in norm follows from sequential weak-\* convergence, a.e. convergence of the indicators by (M2), and Bochner dominated convergence. The serving step is the same inequality as above. PROVED; written as a careful sketch.

---

## 5. Item 4: Possibility 3 (target-relative admissibility)

**(a) The pure-score ranking L_lin: Y ⪰_ω X iff s_ω(Y) ≥ s_ω(X). PROVED.**
- **Axioms.** (A1)–(A4) hold. (A2) and (A3) hold because each relation is a total preorder. Guided-everywhere changes and consolidations raise every s_ω strictly.
- **C_L is exactly the precise models.**
  - *Undominated.* D_p is undominated by F1.
  - *Nothing else is.* A model that is not weakly Pareto-maximal in Z has some Y with m(Y) ≫ m(X), and that Y dominates X. A weakly maximal model is supported by some r (F2 and separation), so it equals D_r by F1.
- **Ties.** An all-world tie means equal m. Equal m with a precise D_r forces equality with D_r (F1), so closure under ties holds.
- **(S) via cor:closed-choice.** Take c_p = D_p. The sets {p : s_ω(D_p) ≥ s_ω(X)} are closed by continuity. The Bayes inequality gives a defending ω ∈ supp p.
- **Role.** L_lin is the "strictly proper score" test case: the p-Bayes model is unique and equals D_p. It protects the precise models only, and every imprecise or incoherent model is dominated by a precise one.
- **Link to the rescaled family.** For a precise interior target {q}, the round-71/72 family M_m (m interior) is exactly the set of interior precise models. So L_lin protects the rescaled family of any precise target.

**(b) Imprecise targets under score-consistent rankings: impossible. PROVED.** By Theorem A, (S) forces C_L ⊆ precise. This covers:
- the target-relative integral ranking L_Q ("unavailable to D_Q" in place of "to every coherent model");
- any ranking whose protected family contains an imprecise model, in particular M_m for imprecise M, since rescaling preserves non-singleton credal sets;
- any family of score-consistent (S)-rankings, which can therefore never satisfy LDG's (A) for imprecise models.

**(c) Target-relative coherence floor R\*_Q. PROVED.** Let T_Q := {D_Q} ∪ {D_r : r ∈ Δ}. Define R\*_Q as R\*, with "almost coherent" replaced by "in T_Q".
- The proofs in §4c go through word for word. Only incoherent models, which lie outside T_Q, have consolidations, and (S) uses only that X ∉ T_Q implies X is not precise.
- Other imprecise models are dominated. F2 gives Y with m(Y) ≫ m(D_{Q'}).
- So C_L = T_Q and closure under ties holds.

Prop C shows that tying D_Q with *some* precise model is necessary. I did not determine the minimal tie class. A tie class {D_Q, D_r} with a single r fails, because the vertex defenders would need to be in T.

---

## 6. Item 5: consistency — PROVED

- **{R\*}.** (E) holds because every ranking evaluates all models. (A) holds because C_L = C. (S) holds by §4c. (T) holds because C is closed under ties. LDG thm:argument therefore gives: the permissible models are exactly the almost coherent ones, and each incoherent model is dominated by a member of C_L. Here the dominator is the precise D_{p\*} from thm:finite.
- **{R\*_Q : Q a credal set}.** (A) holds because each D_Q lies in C_{R\*_Q}. The rest is as for {R\*}.
- **{L_lin, R\*}.** This also works. L_lin is closed under ties and satisfies (S).
- **Application.** Each of R\*, R\*_Q and L_lin satisfies (A1)–(A4). R\* and the family {R\*_Q} meet the admissibility premise of cor:ldg. Measures exist (lem:measure; Gaussian for finite Ω).
- **The integral ranking** cannot belong to a family to which LDG's (S) applies (Corollary A1). It remains covered by appshort Theorem 4.1 and by Strand 1's route.

## 7. Exact additional assumptions

| Result | Assumptions beyond the basic setting |
|---|---|
| R\* and R\*_Q satisfy (S) | (M1) and (M2) only. (M3) and atomlessness are not needed. Arbitrary Ω needs E separable (already assumed). |
| Theorem A, Prop C, Prop 1 | Finite Ω; μ with the Lebesgue null sets (used for atomlessness in Lyapunov, full support, and scale-invariance of null sets); (M1). |
| Prop B | Single-world guidance (G1); all-world-tie substitution. |
| Ranking R\* itself | Stipulates the coherent tie class. Gives up score-consistency, which Theorem A shows is unavoidable. Gives up single-world guidance out of coherent models, which Prop B shows is unavoidable. |

## 8. Open

- **R5** keeps the integral availability clause for incoherent worse models and adds clause (a). It satisfies (A1)–(A4), closure under ties and admissibility.
  - The Bayes selection D_p *fails* to serve. Example with n = 2, p = (½, ½), Q = [a, b] ∋ ½: let X = D_p \ (S₁ ∪ S₂), with balls S₁ ⊂ (D_p \ D_Q) ∩ {h₁ < 0} and S₂ ⊂ (D_p \ D_Q) ∩ {h₂ < 0}. The change X → D_p is available to D_Q and guided at neither world. PROVED.
  - Whether another selection works is UNCLEAR.
- **Theorem A for infinite Ω** under thm:local is UNCLEAR.
