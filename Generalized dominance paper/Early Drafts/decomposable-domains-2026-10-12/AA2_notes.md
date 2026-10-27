# AA2 — Filling a 2-cell with closed choice: an exact extension criterion, a no-go for local principles, and the audit's loop does not fill

17 Oct 2026, round 29 (BRIEF21, obligation 2). Labels:
- **PROVED**: full proof here, not refereed;
- **CHECKED**: exact rational arithmetic on stated samples;
- **CONJECTURE**;
- **NUMERICS**: floating point; nothing depends on it.

Scripts are in `aa2py/`. Run each with `python3 -I aa2py/<script>`; outputs are in the `.out` files there. No assumption is added: every hypothesis beyond the §2 axioms is a hypothesis of the result that states it.

**Read:** BRIEF21, AUDIT_Z123_loop (the loop field Ψ_A), AUDIT_X123, AUDIT_Y123, AUDIT_nonlinear_programme, X1 + X12_referee, X2, Y2, Y3, Z1 (Z1.2–Z1.4, Z1.8), Z2 (Z2.6, tripod), write-up §2 and §6 (Thm gm).

**Notation.**
- Full two-sided domain M: every measurable model is evaluable.
- A **system on S ⊆ Δ** (S closed) is a triple of preorders ⪯ = (⪯₁,⪯₂,⪯₃) on M with strict (G), (IB) and transitivity, together with a selection p ↦ C_p (p ∈ S) such that:
  - C_p is coherent;
  - (K) C_p is competitive on supp p;
  - (R4) C_p is undominated;
  - (Csel) only C_p ties C_p at every world;
  - (CS) {p ∈ S : C_p ⪯_i X} is closed in S, for every i and every X ∈ M.
- R := co{u, e₁, e₂} = {w ∈ Δ : w₃ = min_k w_k}. Its boundary ∂R is the audit's loop L₁₂.
- The **loop data** are the posterior selection C_p = D_{K_p}, K_p = ν(p⊙T1), for p ∈ L₁₂.
- An additive field Ψ (strictly guiding, integrable envelope, on M) **realises the loop data at identity** if D_{K_p} is a p-Bayes model of Ψ for every p ∈ L₁₂. The audit's field Ψ_A does this (AUDIT_Z123_loop §2: author-checked; exact loop check in its script; my `aa2_sanity.out` re-confirms the O-vectors).
- For an additive Ψ:
  - W_Ψ(C) := {w ∈ Δ : C is w-Bayes};
  - G*(Ψ) := {w ∈ Δ : Ψ has a coherent w-Bayes model}.

---

## 0. Outcome

**1. The extension problem for a fixed triple of orders is exactly a homotopy problem (Thm AA2.4, PROVED).**
- Closed sections (CS) say precisely that p ↦ C_p is continuous into the space of models with the *order topology* τ_⪯. Its closed subbase is the sets {C : C ⪯_i X}.
- Boundary data on ∂R extend to a system on R, with the same orders, iff the boundary loop is null-homotopic in the admissible space (𝒜_Ω, τ_⪯).
- Pasting along locally finite closed covers is automatic (Lemma AA2.3). So all difficulty sits in (a) the orders and (b) the global topology of 𝒜_Ω.

**2. A genuine extension criterion with independently checkable hypotheses (Thm AA2.7, PROVED).** Fix any additive strictly guiding field Ψ, and any orders that **retain Ψ's strict comparisons**: Ψ_i(X) < Ψ_i(Y) ⇒ X ≺_i Y. This includes Ψ itself, every lexicographic refinement of Ψ, and every refinement by arbitrary later rules. Then:
- **(i) Necessity.** If boundary models are Ψ-Bayes at their own index, every system on R extending them forces R ⊆ G*(Ψ). That is, Ψ has a coherent q-Bayes model at every q ∈ R.
  - The interior selection may be arbitrary: it need not be Bayes-indexed or continuous.
  - Neither uniqueness, nor (C), nor (R4), nor (Csel) is used.
- **(ii) Sufficiency.** Conversely, if every q ∈ R has an a.e.-unique coherent q-Bayes model, then C_p := B_p is a system on R.
- **The new ingredient** is a covering lemma (AA2.6): an upper hemicontinuous convex-valued weight map that is the identity on ∂R covers R. It is proved by a winding-number argument.
- This closes the caveat of Z1 §2: "competitive selected models are Bayes at some weight, but the weight need not depend continuously on p". Continuity is not needed.

**3. Varying orders: a valid gluing theorem, and a rigidity lemma (Thm AA2.8, Lemma AA2.9, PROVED).**
- *Gluing.* Local systems whose selections agree on overlaps glue under the **unanimity** of their orders, provided a checkable hypothesis (H_out) holds: every acceptance out of a selected model by its own chart is accepted by every chart.
- *Rigidity.* Two additive orders that agree, in both directions, on all comparisons out of one model C ≠ E_i coincide at world i.
- *Consequence.* For additive charts, compatibility of orders on overlaps collapses everything to one fixed order, which is item 1.

**4. The test: the audit's loop does NOT fill, for any additive field and any refinement of one (Thm AA2.11, PROVED given the exact certificates, which are CHECKED).**
- Every additive field that realises the loop data at identity has its two acceptance lines **forced** on an open set of pairs, through the posterior's crossing points on L₁₂ (Lemma AA2.10). Its Bayes advice inside R is then forced on those pairs.
- At explicit rational interior points q ∈ int R, that forced advice is non-convex: two forced-accepted gamble balls have a forced-rejected sum ball.
  - 25 exact certificates: ε ∈ {1/20, 1/10, 3/10, 1/2, 4/5}, 2–6 interior points each.
  - Two independent exact implementations; all branch tests are strict, with minimum gaps between 3·10⁻⁵ and 1.3·10⁻³.
- So q ∉ G*(Ψ′) for **every** realising Ψ′. By Thm AA2.7(i), no system on R extends the loop data under orders that retain the strict comparisons of any realising additive field.
- The hypothesis that fails is (H2): R ⊆ G*(Ψ′).
- **The additive obstruction of Thm gm already lives inside the one sector R** for this boundary data, even though the loop itself is additive.

**5. No extension principle built from local data can hold (Prop. AA2.13, PROVED).** For the audit's own orders Ψ_A, one triple of complete additive orders:
- every point of R has a closed neighbourhood carrying a system that extends the loop data there;
- yet no system on R extends the loop data.

So "boundary system + local systems near every point (even sharing one global triple of orders, which handles every nonlocal record) ⇒ global system" is **false**. Adding order compatibility on overlaps does not help, because the counterexample already uses one order. Any valid principle needs a *global* topological hypothesis: a global selection (item 3), a null-homotopy (item 1), or covering of R by the weight map (item 2).

**6. What non-additive data must do (Cor. AA2.14, PROVED).** In ANY system on R extending the loop data, every realising additive field Ψ′ (in particular Ψ_A) must be broken in one of two ways:
- **(a)** some interior selected model is Ψ′-Pareto-dominated at all three worlds, but kept competitive by the orders. This is Z2's (A1) violation, now forced inside R.
- **(b)** some Ψ′_i ∘ C fails to be lower semicontinuous on R.

Whether non-additive orders can do this while keeping closed sections is **open**. The fixed-order criterion (item 1) is the exact form of the question.

**Plain-English status.**
- There is a correct extension principle. For orders built on any additive score, it says: you can fill the triangle exactly when the score's Bayes models inside the triangle are all coherent.
- For the audit's loop that fails at explicit points, for every additive score that reproduces the loop. So the loop is additive, but the triangle it bounds is not, even with arbitrary interior reselection.
- Local patches always exist, so no "local" principle can work. The obstruction is a hole in weight space that the boundary winds around.

---

## 1. Fixed orders: closed choice is continuity into the order topology

**Definition.** For orders ⪯ on M, τ_⪯ is the topology on M generated by the closed subbase F_{i,X} := {C ∈ M : C ⪯_i X}, for i ∈ Ω and X ∈ M. For S ⊆ Ω, 𝒜_S denotes the set of coherent models that are competitive on S, undominated, and tied at every world only with themselves. Note 𝒜_S ⊆ 𝒜_Ω.

**Lemma AA2.1 (PROVED).** A map C : S → M satisfies (CS) iff it is continuous from S (Euclidean) to (M, τ_⪯). So a system on S is a τ-continuous map with C_p ∈ 𝒜_{supp p}.

*Proof.* (CS) says preimages of subbasic closed sets are closed. That is continuity. ∎

**Lemma AA2.2 (PROVED).** C ∈ cl_τ{C′} iff C ⪯_i C′ at every world. On undominated models this holds iff C ~_i C′ at every world. So the quotient of 𝒜_Ω by all-world ties is a T₁ space.

*Proof.*
- C lies in every subbasic closed set containing C′ iff (C′ ⪯_i X ⇒ C ⪯_i X for all i, X). Taking X = C′ gives C ⪯_i C′. The converse is transitivity.
- If C ⪯_i C′ at every i and C′ is undominated, then no C ≺_j C′. Since C ⪯_j C′, this forces C′ ⪯_j C. ∎

So no "generic point" trick can contract 𝒜_Ω. A model weakly better than all of 𝒜_Ω at every world would tie all of it, and Lemma Z2.1(a) forbids that (E_k ≺_k every other model).

**Lemma AA2.3 (pasting; PROVED).** Let S = ⋃_α S_α be a locally finite cover by closed sets. Suppose that, for one fixed ⪯, selections C^α on S_α satisfy the clauses relative to S_α, and C^α_p ~_i C^β_p at every world for p ∈ S_α ∩ S_β. Then any choice C_p ∈ {C^α_p : p ∈ S_α} satisfies the clauses on S.

*Proof.*
- (K), (R4) and (Csel) are pointwise.
- By transitivity, {p : C_p ⪯_i X} = ⋃_α {p ∈ S_α : C^α_p ⪯_i X}. This is a locally finite union of sets that are closed in S_α, hence closed in S. ∎

**Theorem AA2.4 (fixed-order extension = null-homotopy; PROVED).** Let R ⊆ Δ be compact and convex with nonempty interior. Fix ⪯, and a system on ∂R with these orders. There is a system on R with the same orders extending the boundary selection iff the map ∂R → (𝒜_Ω, τ_⪯), p ↦ C_p, is null-homotopic.

*Proof.*
- Interior points of R have full support, and 𝒜_{supp p} ⊆ 𝒜_Ω on ∂R. So by Lemma AA2.1 an extension is a continuous extension of a map S¹ ≅ ∂R → 𝒜_Ω to D² ≅ R.
- For any topological space Y, a map S¹ → Y extends to D² iff it is null-homotopic. The quotient S¹ × [0,1] → D² collapsing S¹ × {1} is closed (compact to Hausdorff), so a homotopy to a constant induces a continuous map on D²; conversely restrict the radial homotopy. ∎

**Remark (Michael-type selection).** For fixed orders the admissible-value map p ↦ 𝒜_{supp p} is *constant* on int R. So a continuous-selection theorem of Michael's finite-dimensional type, with a 2-dimensional domain, has exactly one substantive hypothesis: the value space must be simply connected (and locally so). Cor. AA2.12 shows that for the audit's orders this fails: π₁(𝒜_Ω, τ_{Ψ_A}) contains an essential loop.

---

## 2. Orders that retain an additive primary: the covering lemma and an exact criterion

Throughout this section, Ψ is a strictly guiding additive field with integrable envelope on M. The orders ⪯ **retain Ψ** if Ψ_i(X) < Ψ_i(Y) ⇒ X ≺_i Y for every i. Nothing else is assumed about ⪯: neither completeness nor any representation. For a selection C on S put W(p) := W_Ψ(C_p).

**Lemma AA2.5 (PROVED).** Let ⪯ retain Ψ, and let C satisfy (K) and (CS) on S.
- **(a)** W(p) is a nonempty compact convex subset of Δ, and it contains some w with supp w ⊆ supp p.
- **(b)** Each Ψ_i ∘ C is lower semicontinuous on S.
- **(c)** W has closed graph; hence it is upper hemicontinuous.
- **(d)** W(p) ⊆ G*(Ψ), and G*(Ψ) is closed.

*Proof.*
- **(a)** Let T = supp p.
  - By (K), for every X there is i ∈ T with C_p ⪯_i X. By retention, then Ψ_i(C_p) ≤ Ψ_i(X).
  - So the set {(Ψ_i(X) − Ψ_i(C_p))_{i∈T} : X ∈ M} misses the open negative orthant. That set is convex (Lyapunov: nonatomic μ, finitely many advice kinds, integrable losses; as in Z2.6 Step 1).
  - A separating w ≥ 0, w ≠ 0, supported in T, makes C_p w-Bayes.
  - W(p) = {w ∈ Δ : w·(Ψ(X) − Ψ(C_p)) ≥ 0 for all X} is an intersection of closed half-spaces with Δ.
- **(b)** Retention gives two inclusions: Ψ_i(C_p) < Ψ_i(X) ⇒ C_p ⪯_i X, and C_p ⪯_i X ⇒ Ψ_i(C_p) ≤ Ψ_i(X).
  - The range of Ψ_i is an interval I (Lyapunov). For c ∈ I with c < sup I, pick X_{c′} with Ψ_i(X_{c′}) = c′ for c′ ↓ c.
  - Then {p : Ψ_i(C_p) ≤ c} = ⋂_{c′} {p : C_p ⪯_i X_{c′}}, an intersection of closed sets. (For c ≥ sup I the set is S.)
- **(c)** Let p_n → p, w_n ∈ W(p_n), w_n → w.
  - Pass to a subsequence with Ψ(C_{p_n}) → y; the envelope bounds these values.
  - For every X, w·y = lim w_n·Ψ(C_{p_n}) ≤ w·Ψ(X).
  - By (b), Ψ(C_p) ≤ y coordinatewise, and w ≥ 0. So w·Ψ(C_p) ≤ w·Ψ(X) for all X, that is, w ∈ W(p).
- **(d)** C_p is coherent, so W(p) ⊆ G*(Ψ). For closedness, let w_n → w with coherent w_n-Bayes models X_n.
  - Coherent models are compact in measure (write-up, proof of Lemma H10(a)), so X_n → X along a subsequence, with X coherent.
  - Ψ is continuous in measure, so X is w-Bayes. ∎

**Lemma AA2.6 (covering lemma; PROVED).** Let R ⊆ aff Δ be compact and convex with nonempty interior. Let W : R ⇉ aff Δ be upper hemicontinuous with nonempty compact convex values, with p ∈ W(p) for every p ∈ ∂R. Then for every q ∈ R there is p ∈ R with q ∈ W(p).

*Proof.*
- For q ∈ ∂R take p = q. Let q ∈ int R and suppose q ∉ W(p) for all p.
- **Local separating directions.** For each p, the compact convex set W(p) misses q, so some unit ν_p has ν_p·(w − q) ≥ m_p > 0 on W(p). By upper hemicontinuity there is an open V_p ∋ p with W(p′) inside the m_p/2-neighbourhood of W(p) for p′ ∈ V_p. So ν_p·(w − q) > 0 on W(p′) for p′ ∈ V_p.
- **A global field.** Take a partition of unity (φ_k) on R subordinate to a finite subcover (V_{p_k}). Put v(p) := Σ φ_k(p) ν_{p_k}. Then v is continuous and v(p)·(w − q) > 0 for all w ∈ W(p), so v(p) ≠ 0.
- **On the boundary.** For p ∈ ∂R, w = p gives v(p)·(p − q) > 0. So the straight homotopy (1−t)v(p) + t(p − q) never vanishes, and v|∂R is homotopic in aff Δ ∖ {0} to p ↦ p − q.
- **Winding.** The latter has winding number 1, since ∂R is a convex Jordan curve around q. But v extends to the disc R without zeros, so its winding number is 0. Contradiction. ∎

(Equivalently: Ky Fan's 1969 fixed-point theorem for upper hemicontinuous maps with inward values, applied to p ↦ p + q − W(p).)

**Theorem AA2.7 (extension criterion for primary-retaining orders; PROVED).** Let R ⊆ Δ be compact and convex with nonempty interior, Ψ as above, and a boundary selection on ∂R with C_p Ψ-Bayes at p for each p ∈ ∂R.
- **(i)** Suppose some orders retaining Ψ carry a selection on R that extends the boundary selection and satisfies (K) and (CS) relative to R. Then R ⊆ G*(Ψ).
- **(ii)** Conversely, suppose every q ∈ R has an a.e.-unique coherent q-Bayes model B_q. Then the orders of Ψ with C_p := B_p form a system on R (all clauses, with a fixed plan) that extends the boundary selection.

*Proof.*
- **(i)** By Lemma AA2.5, W is upper hemicontinuous with nonempty compact convex values in G*(Ψ), and p ∈ W(p) on ∂R. Lemma AA2.6 gives R ⊆ ⋃_p W(p) ⊆ G*(Ψ).
- **(ii)** Uniqueness at each q makes q ↦ B_q continuous in measure on R. Off the null tie set of q, the strict Bayes inequalities persist at nearby weights; then use dominated convergence. Apply Lemma Z1.2 with φ = id, which is face-respecting. ∎

**Reading.**
- The hypotheses are independently checkable. (H2) "every Bayes model of Ψ at weights in R is coherent" is a property of the field alone. It is tested pair by pair (charts) and by convexity, without reference to any order construction, selection or plan.
- The criterion is exact up to the uniqueness clause in (ii).
- It strengthens Z1.4 and Z2.6:
  - the interior selection may be any closed competitive selection, not a reparametrised Bayes family;
  - no uniqueness or isolation is needed for the obstruction direction.

**Remark (reindexed boundaries).** The proof of Lemma AA2.6 only uses, on ∂R, that the field v can be homotoped to p − q. So (i) extends as follows. Suppose the boundary weight correspondence admits, for some q ∉ G*(Ψ), a continuous σ : ∂R → aff Δ with σ(p) ∈ W(p) and winding number of σ − q nonzero. Then no extension exists. I have not used this more general form below.

---

## 3. Varying orders: unanimity gluing and additive rigidity

**Theorem AA2.8 (local certification of a global selection; PROVED).** Let S = ⋃_α S_α be a locally finite closed cover. Suppose:
- each chart α is a system (⪯^α, C^α) on S_α with all clauses relative to S_α;
- C^α_p = C^β_p a.e. on overlaps;
- **(H_out)** for all α, β, all p ∈ S_α, all X and all i: C^α_p ⪯^α_i X ⇒ C^α_p ⪯^β_i X.

Put ⪯_i := ⋂_β ⪯^β_i, and let C be the pasted selection. Then (⪯, C) is a system on S. If T1 is selected somewhere, T1 ∈ C_L.

*Proof.*
- **The orders.** Intersections of preorders with (IB) are preorders with (IB). For strict (G): if X is guidance-better than Y at i, strictly on a non-null set, then X ⪯^β_i Y and Y ⋠^β_i X for every β. So X ≺_i Y.
- **Comparisons out of selected models.** By (H_out), C^α_p ⪯_i X ⟺ C^α_p ⪯^α_i X. Hence (K) and (CS) transfer, the latter by Lemma AA2.3.
- **(R4).** Suppose X ⪯_i C^α_p at every i, and X ≺_j C^α_p at some j. Then X ⪯^α_i C^α_p at every i. Also C^α_p ⋠_j X, which by (H_out) means C^α_p ⋠^α_j X. So X dominates C^α_p in chart α, which is impossible.
- **(Csel).** A global tie at every world is a tie in chart α. ∎

(H_out) is a finite family of checkable implications per pair of charts. It is non-local: it concerns all pairs of charts, not only overlapping ones. It is satisfiable without the charts' orders agreeing.

**Lemma AA2.9 (additive rigidity; PROVED).** Let Ψ^α, Ψ^β be additive and strictly guiding with integrable envelopes on M. Fix a world i and a model C ≠ E_i a.e. that gives no contradictory advice on a non-null set. Suppose that for every X:

  Ψ^α_i(C) ≤ Ψ^α_i(X) ⟺ Ψ^β_i(C) ≤ Ψ^β_i(X).

Then Ψ^β_i = κΨ^α_i + const for some κ > 0. In particular the two world-i orders coincide.

*Proof.*
- **The planar set.** Let K := {(x, y)} with x = Ψ^α_i(X) − Ψ^α_i(C) and y = Ψ^β_i(X) − Ψ^β_i(C). K is convex (Lyapunov) and contains 0.
- **Points on both sides.** By strict (G), K has a point P₁ with x₁ < 0 (improve C at world i; possible since C ≠ E_i), and then y₁ < 0. It also has a point with x > 0, obtained by switching to contradictory advice somewhere.
- **The x > 0 points lie on one line.** Take P₂ with x₂ > 0, so y₂ ≥ 0. On the segment P₁P₂, points with x < 0 have y < 0. Points with x ≥ 0 have y ≥ 0. So the segment crosses x = 0 at y = 0, i.e. passes through the origin. Hence all P₂ lie on the line through P₁ and 0.
- **The x = 0 points.** A point (0, y₀) with y₀ > 0 would put points with x < 0 and y > 0 on its segment to P₁. So x = 0 forces y = 0.
- **Conclusion on K.** K lies on the line y = κx with κ > 0.
- **Pointwise.** Taking X = C off a set E, and a fixed advice on E, gives ∫_E [δ^β − κδ^α](h, a) dμ = 0 for all E, where δ(h, a) := ℓ_i(h, a) − ℓ_i(h, C(h)). So δ^β = κδ^α a.e. for each advice a, and the claim follows by additivity. ∎

**Consequence.** For additive charts on a connected S, the natural local compatibility condition (two-sided agreement on all comparisons out of selected models in overlaps, at models ≠ E_i) propagates along chains of overlaps to *one* order. Then the gluing question is exactly the fixed-order question of §1, and §5 shows that local existence does not settle it.

---

## 4. The test: the audit's loop and the triangle R

### 4.1 Forced charts

Index a mixed pair by its majority orientation h (one negative coordinate o, normalised h_o = −1), as in Z1 and the audit. Write f_k(w) := w·h + λw_k h_k, so that (w⊙v_k)·h ∝ f_k(w). The posterior D_{K_w} advises:
- M (accept h) iff min_k f_k(w) > 0, i.e. c·w > 0 with c := h + λh_o e_o;
- O (accept −h) iff max_k f_k(w) < 0.

Along each side of L₁₂ the f_k are affine, so the posterior M-set and O-set on L₁₂ are finite unions of intervals with computable endpoints.

Say h is of **class F1** if all of the following hold:
- both the posterior M-set and the posterior O-set on L₁₂ are proper arcs, each with two endpoints in the open sides, and all roots are simple and distinct;
- with ℓ := z₁ × z₂ the vector through the two O-endpoints (oriented positive on the O-arc), the closed half-planes {c·w ≥ 0} and {ℓ·w ≥ 0} are disjoint on R. Equivalently max_R min(c·w, ℓ·w) < 0. This is checked at the vertices of R and at the points of ∂R where c·w = ℓ·w.

**Lemma AA2.10 (chart forcing; PROVED).** Let Ψ′ realise the loop data at identity. For a.e. h of class F1, and every q ∈ R with c·q ≠ 0 ≠ ℓ·q, every q-Bayes model of Ψ′ gives on the pair of h:
- M if c·q > 0;
- O if ℓ·q > 0;
- S otherwise.

Unanimous pairs are forced to the correct advice at every weight.

*Proof.*
- **Acceptance vectors.** Let γ := ℓ′(h,S) − ℓ′(h,M) and γ′ := ℓ′(h,S) − ℓ′(h,O). Contradictory advice is never Bayes at any w ∈ Δ: by strict (G) it is worse than both acceptances at every world. So the w-Bayes advice is the argmax of {0, γ·w, γ′·w}.
- **Fubini.** For every w ∈ L₁₂ the posterior advice is Bayes for a.e. h. So for a.e. h it is Bayes for a.e. w ∈ L₁₂ (length measure).
- **M-endpoints.** Fix such an h of class F1. On the M-arc γ·w ≥ 0 a.e., and on the adjacent S-arcs γ·w ≤ 0 a.e. These S-arcs have positive length, since the closed half-planes are disjoint on R. By continuity γ·z = 0 at both M-endpoints z₁′, z₂′.
- **γ is c.** By (G), γ has the strict sign pattern of h, so it is not a multiple of 𝟙 and its zero set in aff Δ is a line. Hence γ ∝ z₁′ × z₂′ ∝ c, positively by the sign on the M-arc.
- **γ′ is ℓ.** In the same way, γ′ = κ′ℓ with κ′ > 0.
- **Advice on R.** Disjointness on R gives: c·q > 0 ⇒ γ′·q < 0 < γ·q; ℓ·q > 0 ⇒ γ·q < 0 < γ′·q; both negative ⇒ S. Each case has a unique Bayes advice. ∎

The audit's own O-vector d is the forced ℓ on every class-F1 pair tested: 5162 of 5162 exact pairs (`aa2_sanity.out`). So Ψ_A is one realisation, and nothing in this lemma depends on its particular formulas.

### 4.2 The certificates

**Theorem AA2.11 (no realising field has coherent Bayes models throughout R; PROVED from the exact certificates, which are CHECKED).** For ε ∈ {1/20, 1/10, 3/10, 1/2, 4/5} there are rational q ∈ int R, at the points listed in `aa2py/certify_*.out`, such that **no** additive strictly guiding field realising the loop data at identity has a coherent q-Bayes model. That is, q ∉ G*(Ψ′) for every such Ψ′.

*Proof.* Each certificate consists of rational gambles a₁, a₂ and s = a₁ + a₂ such that:
- **(1)** each pair is unanimous or of class F1;
- **(2)** the forced advice at q accepts a₁ and a₂ and rejects s;
- **(3)** every branch decision of the classification is a strict inequality at a₁, a₂ and s. The minimum recorded gap is 2.9·10⁻⁵ to 1.3·10⁻³; it covers all root differences, the endpoints, disjointness, and c·q, ℓ·q.

**Local constancy.** By (3), the classification and the forced advice are constant on open balls B₁ ∋ a₁, B₂ ∋ a₂ and B_s ∋ s. All the quantities involved are continuous on a neighbourhood where the branch pattern is fixed. Shrink so that B₁ + B₂ ⊆ B_s.

**Contradiction.** Let B be a q-Bayes model of a realising Ψ′. By Lemma AA2.10, B contains a.e. point of B₁ and of B₂ and misses a.e. point of B_s. If B = D_K a.e., then:
- D_K is open and convex, so it contains B₁ and B₂ entirely. Otherwise a separating line would cut off a positive-measure part of a ball.
- Hence it contains B₁ + B₂, by cone convexity.
- That contradicts a.e. rejection on the open set B₁ + B₂. ∎

CHECKED:
- **`aa2_certify.py`** (implementation 1: exact trace computation, strictness gaps).
  - 25 certificates in all. ε = 1/20, 1/10, 3/10: 6 interior points each; ε = 1/2: 5; ε = 4/5: 2.
  - Every gamble is of class F1.
  - In addition, 300 exact random relative perturbations of size 10⁻⁷ per certificate: 0 changes of advice (supplement only).
- **`aa2_recheck.py`** (implementation 2: the audit's vectors c, d; independent exact arc endpoints by root enumeration; loop agreement at 19 points per side; disjointness; advice at q).
  - **All 25 re-verified** (`recheck.out`).

Example (ε = 3/10):
- q = (666667/10⁶, 266667/10⁶, 33333/500000);
- a₁ = (−174251/500000, 2160803/10⁶, −637221/10⁶);
- a₂ = (−30829/10⁶, 85753/250000, −291717/10⁶);
- a₁ and a₂ are forced-accepted, and a₁ + a₂ is forced-rejected.

**Corollary AA2.12 (PROVED).** No system on R extends the loop data under any orders that retain the strict comparisons of some field realising the loop data at identity. This covers Ψ_A, all its refinements, and all additive fields of that kind. Equivalently, by Thm AA2.4, the loop data form an **essential loop** in (𝒜_Ω, τ_{Ψ′}) for every such Ψ′.

*Proof.* Thm AA2.7(i) with Thm AA2.11. ∎

**Where is the hole? (NUMERICS, `map_3_10.out`, `concav_*.out`.)**
- On a 1/8-grid of int R at ε = 3/10, float-level fully forced certificates appear at 14 of 21 points.
- None are found at the three grid points on the median q₁ = q₂, nor at four points with |q₁ − q₂| = 1/8. On the median, Ψ_A's Bayes model also passes a midpoint-concavity test of its lower prevision, with defects ≤ 10⁻⁹ (for example 5·10⁻¹⁰ at u).
- Off the median, defects of order 10⁻³–10⁻² appear.
- The posterior control passes everywhere, with defects ≤ 3·10⁻¹⁵.
- So G*(Ψ′) ∩ R appears to consist of a region around the median plus the loop. The boundary loop winds around holes on both sides of the median.

**What this says about Thm gm.**
- The additive obstruction for this boundary data is internal to the single sector R. The loop is additive (audit), but its interior cannot be filled additively, even with arbitrary closed reselection inside R (Thm AA2.7(i) does not require Bayes indexing).
- Mechanism: the forced chord replaces the posterior's convex broken O-boundary (the max of two f_k's) inside R. That makes the O-acceptance region too small on one side of the median, and convexity breaks. This is the 2-cell form of Z1.8's three-point forcing.
- It does **not** prove gm's full statement in R for every boundary data. A boundary selection that is Ψ′-Bayes at non-identity weights is outside Thm AA2.11. The Remark after AA2.7 gives the winding condition such a reindexing would have to defeat.

---

## 5. No principle built from local data can hold

**Proposition AA2.13 (local systems everywhere, no global system; PROVED, given the audit's loop theorem).** Use the orders of the audit's field Ψ_A, one triple of complete additive orders, and the loop data on ∂R. Take ε in the list of Thm AA2.11.
- **(a)** Every x ∈ R has a closed neighbourhood N_x relative to R, and a selection on N_x satisfying all clauses relative to N_x, with these same orders, equal to the loop data on N_x ∩ ∂R.
- **(b)** There is no selection on R with these orders, or with any orders retaining them, that satisfies (K) and (CS) and extends the loop data.

*Proof.*
- **(a), interior points.** For x ∈ int R, let N_x be a closed ball in int R and C ≡ T1 = B_u. T1 is the a.e.-unique u-Bayes model, so it is competitive on Ω, undominated and Csel; its sections are ∅ or N_x.
- **(a), boundary points.** For x ∈ ∂R, let N_x := R ∩ B̄(x, r) with r small. Then N_x ∩ ∂R is an arc through x, a segment or a corner. Let φ_x : N_x → N_x ∩ ∂R be a retraction; an arc is an absolute retract, and explicit radial formulas also work.
  - φ_x is face-respecting: interior points have full support, and φ_x fixes ∂R.
  - On L₁₂, Ψ_A's Bayes models D_{K_w} are a.e. unique, coherent, and continuous in measure (audit §2; K_w is Hausdorff-continuous with null boundaries).
  - Lemma Z1.2 with C_y := B_{φ_x(y)} gives all clauses relative to N_x.
- **(b)** Thm AA2.7(i) with Ψ = Ψ_A, and Thm AA2.11. ∎

**Consequences.**
1. "Boundary system + a local system near every point ⇒ global system" is false. This holds even when all local systems share one global triple of complete additive orders, which settles every nonlocal record between nearby (indeed all) selections. So the X2.7 programme of "local systems that also handle nonlocal records" cannot be completed into an extension principle by local hypotheses alone.
2. Adding compatibility of orders on overlaps does not help: the counterexample has identical orders. By Lemma AA2.9, for additive charts such compatibility *forces* identical orders anyway.
3. Adding agreement of the *selections* on overlaps makes the principle true (Lemma AA2.3, Thm AA2.8). But that hypothesis is a global section: it already contains the filling, which is where the obstruction lies.
4. So a valid extension principle must carry a global topological hypothesis: a null-homotopy in (𝒜_Ω, τ) (Thm AA2.4) or a covering/winding condition on weights (Thm AA2.7). The brief's suggested form, a continuous-selection theorem for a lower hemicontinuous map with "convex-like" values, fails exactly at simple connectivity of the values (Remark after AA2.4).

---

## 6. What non-additive data must do

**Corollary AA2.14 (PROVED).** Take any orders ⪯ (G, IB, transitive; no retention assumed), any system on R extending the loop data, ε as in Thm AA2.11, and any additive Ψ′ realising the loop data at identity, for example Ψ_A. At least one of the following holds:
- **(a)** some selected C_p (p ∈ int R) is Ψ′-Pareto-dominated: some X has Ψ′_i(X) < Ψ′_i(C_p) at all three worlds. Yet C_p ⪯_j X at some world j, so the orders discard that strict Ψ′-comparison;
- **(b)** some Ψ′_i ∘ C is not lower semicontinuous on R.

*Proof.* Suppose neither holds.
- By (a)'s failure and Lyapunov convexity, every W′(p) := W_{Ψ′}(C_p) is nonempty, compact and convex.
- By (b)'s failure, the proof of Lemma AA2.5(c) gives a closed graph; that part does not use retention.
- On ∂R, p ∈ W′(p) by realisation at identity.
- Lemma AA2.6 gives q ∈ W′(p) for the certificate point q. So C_p is a coherent q-Bayes model of Ψ′, contradicting Thm AA2.11. ∎

So any filler must, for every realising additive field simultaneously, either keep a Ψ′-Pareto-dominated model competitive (the (A1) failure of Z2 §5, now forced inside R) or let some Ψ′-loss jump upward along the selection. Both are compatible with (CS) for non-retaining orders. AUDIT_Y123 Prop. 4 shows retention is exactly what forces level-set minimality.

**Open (Q_AA2).** Is there a triple of preorders, not retaining any field that realises the loop data at identity, for which the loop data are null-homotopic in (𝒜_Ω, τ_⪯)? By Thm AA2.4 this is *equivalent* to filling R. By Cor. AA2.14, any such triple must realise (a) or (b) against Ψ_A and against every other realising field.
- I have no construction.
- I also have no proof that (a)/(b) are incompatible with (G) and (IB). Their incompatibility would be a non-additive obstruction already in one sector.

---

## 7. Status

| Item | Status |
|---|---|
| AA2.1 (CS) ⟺ continuity into the order topology τ_⪯ | PROVED |
| AA2.2 specialisation = weak domination; 𝒜_Ω/ties is T₁ | PROVED |
| AA2.3 pasting along locally finite closed covers | PROVED |
| **AA2.4 fixed-order extension over a 2-cell ⟺ null-homotopy in (𝒜_Ω, τ)** | **PROVED** |
| AA2.5 retention ⇒ W nonempty, convex, u.h.c.; Ψ∘C l.s.c.; G* closed | PROVED |
| **AA2.6 covering lemma (u.h.c. convex weight map, identity on ∂R, covers R)** | **PROVED** |
| **AA2.7 exact criterion: fill ⇒ R ⊆ G*(Ψ); unique coherent Bayes on R ⇒ fill** | **PROVED** |
| AA2.8 unanimity gluing under (H_out), given a global selection | PROVED |
| AA2.9 additive rigidity (two-sided agreement out of one model ⇒ same order) | PROVED |
| AA2.10 chart forcing for fields realising the loop at identity | PROVED |
| **AA2.11 no realising additive field has coherent Bayes models throughout R** | **PROVED from 25 exact certificates (CHECKED twice; 5 values of ε)** |
| AA2.12 loop data essential in (𝒜_Ω, τ_{Ψ′}); no fill with primary-retaining orders | PROVED |
| **AA2.13 local systems near every point, one shared order, no global system** | **PROVED** (uses the audit's author-checked loop theorem) |
| AA2.14 any filler violates (A1) or l.s.c. against every realising field | PROVED |
| Location of the holes (off the median q₁ = q₂) | NUMERICS |
| Q_AA2: non-retaining orders that fill R | open |
| Fill with boundary models Bayes at non-identity weights | open (winding condition stated) |

**Referee priorities.**
1. Lemma AA2.6: the partition-of-unity field and the winding step.
2. Lemma AA2.5(b): lower semicontinuity from closed sections under retention (it uses the Lyapunov interval).
3. Lemma AA2.10: that the posterior S-arcs adjacent to the M- and O-arcs have positive length, so that γ·z = 0 at the endpoints.
4. Thm AA2.11: that the recorded gaps cover every branch decision (`aa2strict.py`).
5. Lemma AA2.9: the planar convexity step.

## 8. Files (`aa2py/`)

- `aa2common.py`, `aa2forced.py` (forced charts), `aa2strict.py` (forced charts with strictness gaps), `aa2audit.py` (the audit's c, d).
- `aa2_sanity.py` / `.out`: the forced O-line equals the audit's d on all tested class-F1 pairs (CHECKED).
- `aa2_certify.py` / `certify_{1_20,1_10,3_10,1_2,4_5}.out`: exact certificates (CHECKED). Candidates are found by float search in `aa2_cert_explore.py`.
- `aa2_recheck.py` / `recheck.out`: independent exact re-verification of all 25 (CHECKED).
- `aa2_concav.py` / `concav_post_3_10.out`, `concav_audit_3_10.out`: midpoint-concavity scan of lower previsions (NUMERICS).
- `aa2_map.py` / `map_3_10.out`: where the holes are (NUMERICS).
- `aa2_search.py`, `aa2_auditscan.py`: coarse grid searches, which miss the defects; kept as a record (NUMERICS).
