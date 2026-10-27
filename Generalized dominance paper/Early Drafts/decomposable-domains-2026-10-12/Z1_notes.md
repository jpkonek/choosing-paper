# Z1 — Two vertices and T1 in one closed system: Conjecture Y3.C is false, and the connection through T1 is additive

17 Oct 2026, round 28 (BRIEF20, milestones 1–2). Labels:
- **PROVED**: full proof here, not refereed;
- **CHECKED**: exact rational arithmetic on stated samples;
- **CONJECTURE**;
- **NUMERICS**: sampling or floating-point LP; nothing depends on it.

Scripts are in `z1py/`. Run each with `python3 -I <script>` from inside `z1py/`; outputs are in the matching `.out` files. No assumption is added. Notation follows write-up §2 and Y3: worlds 1, 2, 3 (0, 1, 2 in code); c₀ = (1−ε)/3, λ = ε/c₀, A = 1+λ; v_k = c₀(𝟙 + λe_k); T1 = conv{v_k}; posterior family K_w := ν(w⊙T1) (X2.5), so K_u = T1 and K_{e_k} = {e_k}. B^k := {h : h_k > 0}. Domain: the full two-sided domain (every measurable model is evaluable, so (LF) at T1 holds trivially).

Read: BRIEF20, AUDIT_Y123, AUDIT_X123, AUDIT_nonlinear_programme, Y2, Y3, X1, X2, write-up §2, §6 (Thm gm, Prop vertexfree).

---

## 0. Outcome

**The milestone is delivered, and it goes further than asked: one additive system connects T1 to all three vertices.**

1. **Conjecture Y3.C is false, even in its literal form (Prop. Z1.1, PROVED).**
   - Take any ranking with strict (G) in which T1 satisfies its clauses at u, for example the audit's field of AUDIT_Y123 §5.
   - Select C_p := B^k on a closed neighbourhood N_k of each vertex e_k, and C_u := T1.
   - Every axiom holds on N₁ ∪ N₂ ∪ {u}, with a fixed plan. The reason is that B^k is the strict world-k optimum.
   - So the vertex locality barrier Y3.4 already follows from this plateau. Y3's box construction is not needed for it.
   - A *bare* two-vertex milestone therefore has no content. The content lies in connection, and in non-constant vertex selections.
2. **The connection through T1 is additive (Thm Z1.7, PROVED; core lemma CHECKED).**
   - Let Σ := [u,e₁] ∪ [u,e₂] ∪ [u,e₃] be the star of medians through u.
   - There is an explicit strictly guiding additive field Ψ^★ whose a.e.-unique Bayes model at **every** w ∈ Σ is the posterior model D_{K_w}. In particular T1 = B_u.
   - With the index set I := N₁ ∪ N₂ ∪ N₃ ∪ Σ (two vertices if preferred: N₁ ∪ N₂ ∪ [u,e₁] ∪ [u,e₂]), the selection is:
     - C_p := D_{K_p} on Σ;
     - C_p := D_{K_{φ(p)}} on N_k, where φ is a face-respecting retraction of N_k onto the near-vertex part of the median.
   - Consequences:
     - T1 is selected at a non-isolated index, joined continuously-in-measure to genuinely imprecise, non-constant interior selections near e₁ and near e₂;
     - every axiom holds against **every measurable competitor** on I: strict (G), (IB), transitivity, competitiveness on supp p, protection, no (C)-ties, and closed sections;
     - the plan is fixed: V(p,i,X) = {q ∈ I : Ψ_i(C_q) > Ψ_i(X)}. By X1.3.2, every finite fragment is satisfiable with this same plan.
3. **Where Y3.7(b)'s conflict actually lives.** Two facts locate it:
   - It is an artefact of *identity-parametrised Bayes coherence on two-dimensional neighbourhoods of both vertices*.
   - The reparametrisation lemma (Lemma Z1.2) shows that, for additive fields, any obstruction to T1 needs index sets that cannot be mapped face-respectingly into the set of weights with coherent unique Bayes models (Cor. Z1.4).
   
   The first concrete failure beyond the star is **star plus one full edge**. The posterior selection on Σ ∪ [e₁,e₂] is the Bayes family of no additive field (Prop. Z1.8, PROVED; CHECKED). The mechanism is *three-point forcing*: an additive O-chart is one line, but it must pass through three non-collinear boundary points.
4. **No non-additive orders were needed for the milestone**, so none were built. The precise non-additive target is now the loop u–e₁–e₂–u (§5).

**Plain-English status.**
- Two vertex neighbourhoods plus T1 is easy.
- Joining T1 to the vertices along lines is also possible with ordinary additive rankings, and it uses the natural "posterior" selection.
- What additive rankings cannot do starts as soon as the index set encloses a two-dimensional region, or contains a full edge together with the arms. That is where the T1 problem now sits.

---

## 1. The vertex plateau: Y3.C refuted

**Proposition Z1.1 (PROVED).** Let (⪯_i) be any triple of preorders on the full domain with strict (G) and (IB). Suppose T1 is competitive on Ω, undominated, and tied at every world only with itself. (The audit's field does this, AUDIT_Y123 §5, since T1 is its a.e.-unique u-Bayes model.) Let N_k := {p ∈ Δ : p_k ≥ 1−η}, with 0 < η < 1/2, and set:
- C_p := B^k for p ∈ N_k;
- C_u := T1.

Then on I₀ := N₁ ∪ N₂ ∪ {u} (or with N₃ too), every clause of Θ_C holds against every measurable X: (K) on supp p, (R4), (Csel). The sections {p ∈ I₀ : C_p ⪯_i X} are closed, with the fixed plan V(p,i,X) := the component of I₀ containing p.

*Proof.*
- **(K).** For p ∈ N_k we have k ∈ supp p, and B^k ⪯_k X for every X by weak (G), since B^k gives world-k-correct advice on a.e. pair.
- **(R4) and (Csel).** X ⪯_k B^k forces X = B^k a.e. by strict (G).
- **Closed sections.** Each section is a union of some of the closed, pairwise disjoint pieces N₁, N₂, N₃, {u}. Each piece is relatively clopen in I₀, so the plan clauses hold.
- **At u.** By hypothesis. ∎

*Consequences.*
- **(a) Y3.C is false as stated.** "No additive field with T1 ∈ C_L has closed competitive coherent selections near two vertices": the audit's field is additive with T1 ∈ C_L, and the plateau supplies the selections.
- **(b) Y3.4 follows from Z1.1 alone.**
- **(c) No global result is contradicted.** Plateaus are excluded only for *covers* (Prop vertexfree(i) needs (S) on all of Δ). Locally they are legitimate.
- **(d) Requiring "the edge [e₁,e₂] in between" does not help an obstruction.** Lemma Z1.2 below handles it additively once some field has coherent unique Bayes models on the whole edge and T1 = B_u.
  - Such a field exists. In the field Ψ^Z of Remark Z1.9, the edge is posterior.
  - The star field of §3 is the stronger statement and is the one proved in full.

So a meaningful two-vertex test must ask for *connection* through T1, or for non-constant selections near both vertices. Thm Z1.7 gives both.

---

## 2. Reparametrised Bayes subsystems

Let Ψ be a strictly guiding additive field on the full domain with integrable envelope, and B_w a w-Bayes model. Put

  W(Ψ) := {w ∈ Δ : B_w is a.e.-unique and coherent}.

**Lemma Z1.2 (PROVED).** Suppose w ↦ B_w is continuous in measure on a set W ⊆ W(Ψ). Let I ⊆ Δ and let φ : I → W be continuous and **face-respecting**: supp φ(p) ⊆ supp p. Put C_p := B_{φ(p)}. Then on I:
- (K) holds on supp p against every measurable X;
- C_p is undominated, and only C_p ties it at every world;
- sections are closed relative to I;
- V(p,i,X) := {q ∈ I : Ψ_i(C_q) > Ψ_i(X)} is a fixed plan.

*Proof.* Put w = φ(p).
- **(K).** If Ψ_i(X) < Ψ_i(B_w) for all i ∈ supp p ⊇ supp w, then w·Ψ(X) < w·Ψ(B_w), against Bayes optimality.
- **(R4) and (Csel).** If X ⪯_i B_w at every world, then w·Ψ(X) ≤ w·Ψ(B_w). So X is w-Bayes, and X = B_w a.e. by uniqueness.
- **Sections and plan.** q ↦ Ψ_i(C_q) is continuous, by dominated convergence along the continuous-in-measure q ↦ B_{φ(q)}. So {q : Ψ_i(C_q) ≤ Ψ_i(X)} is closed, and V is its open complement, independent of any fragment. ∎

**Lemma Z1.3 (PROVED; standard).** A continuous face-respecting map φ : Δ → Δ is surjective.

*Proof.*
- Let y ∉ φ(Δ), with y in the relative interior of a face F.
- φ maps F into F. Radial projection from y retracts F ∖ {y} onto ∂F, so ρ := r∘φ|_F : F → ∂F.
- On ∂F, the straight homotopy from x to φ(x) stays in the carrier face of x, which lies in ∂F and avoids y. So ρ|_{∂F} is homotopic to the identity of ∂F ≅ S^{dim F−1}.
- Hence the identity of ∂F extends to F, contradicting Brouwer. (For dim F = 0 the claim is trivial.) ∎

**Corollary Z1.4 (PROVED).** For an additive field, a reparametrised selection C_p = B_{φ(p)} on all of Δ forces W(Ψ) = Δ by Lemma Z1.3: all Bayes models are coherent. With T1 = B_{u′}, this is an additive cover, which Thm gm excludes.

So, within reparametrised Bayes selections, an additive obstruction to T1 must use an index set that admits no face-respecting map into W(Ψ). Two examples:
- every index set containing a 2-cell whose boundary is mapped essentially;
- every index set containing a full edge, whose image must cover the edge.

*Caveat.* Not every additive selection is reparametrised Bayes. Competitive selected models are Bayes at *some* weight (Y3.7, Step 0), but the weight need not depend continuously on p. Cor. Z1.4 is a statement about this construction method, not a characterisation.

---

## 3. The star field Ψ^★ and the connected system

**Pairs.** Index a.e. mixed pair by its majority orientation h (two positive coordinates), with odd world o (h_o < 0) (X2.1). Write g_k(s) := max_{k′} (w(s)⊙v_{k′})·h along the arm S_k := {w(s) = (1−s)u + s e_k : s ∈ [0,1]}.

The posterior model D_{K_w} gives advice as follows:
- M (accept h) iff min_{k′}(w⊙v_{k′})·h > 0. Since only h_o < 0, the minimum is at k′ = o, so this reads **c(h)·w > 0**, with

  c(h) := h + λ h_o e_o.

  This is linear in w, on all of Δ.
- O (accept −h) iff max_{k′}(w⊙v_{k′})·h < 0.

**Lemma Z1.5 (O-sets along the arms; PROVED, CHECKED).** For a.e. mixed h:
- **(a) Non-odd arms.** For k ≠ o, the O-set of the posterior on S_k is:
  - [u, x_k) with x_k ∈ (u, e_k), if T1 is at O on h;
  - ∅ otherwise.
- **(b) Odd arm.** On S_o it is:
  - all of S_o, if T1 is at O on h;
  - (x_o, e_o] with x_o ∈ (u, e_o), otherwise.

*Proof.*
- g_k is convex and piecewise affine in s (a maximum of affine functions). Its value at s = 0 decides T1's advice, since K_u = T1.
- **(a)** At s = 1, w = e_k, every piece equals v_{k′,k} h_k > 0, since h_k > 0 for k ≠ o.
  - If g_k(0) ≥ 0, some piece is ≥ 0 at 0 and > 0 at 1. So that piece, and hence g_k, is > 0 on (0,1].
  - If g_k(0) < 0, convexity and g_k(1) > 0 give exactly one root x_k.
- **(b)** On S_o the two non-odd coordinates of w(s) are equal. So g_o(s) = c₀ w·h + ε w_j max(h_j, h_l) is affine, with g_o(1) = c₀h_o < 0.
- The boundary cases g(0) = 0 lie on a null set of h. ∎

CHECKED (`z1_star_check.out`): 7500 exact pairs over ε ∈ {1/20, 1/10, 3/10, 1/2, 4/5}, with **0** O-sets of any other shape.

**Definition (the star field Ψ^★).** On a mixed pair with majority orientation h:

  ℓ(h,S) = 0, ℓ(h,M) = −c(h), ℓ(h,O) = −c′(h), ℓ_i(h,×) = 2A|h|,

where c′(h) is defined as follows (scaled to |c′| = |h|):
- **Case A (T1 at O on h).** Let j, l be the two non-odd worlds, and x_j, x_l the crossings of Lemma Z1.5(a). Put c′ := x_j × x_l, oriented so that c′·u > 0.
- **Case B (otherwise).** Let θ := (x_o)_o ∈ (1/3, 1) and c′ := e_o − θ𝟙.

On unanimous pairs (h ≥ 0, h ≠ 0) use Brier: ℓ(M) = −h, ℓ(O) = h, ℓ(S) = 0. The map h ↦ c′(h) is Borel: it is built from roots of piecewise-affine functions with rational-function coefficients.

**Lemma Z1.6 (PROVED, CHECKED).**
- **(a)** c has the strict sign pattern of h, and c′ that of −h. Hence Ψ^★ is strictly guiding, with integrable envelope 2A|h|.
- **(b)** For every w ∈ Σ:
  - the a.e.-unique w-Bayes model of Ψ^★ is D_{K_w};
  - at w = u it is T1;
  - at w = e_k it is B^k.

*Proof.*
- **(a)**
  - c is immediate.
  - Case A: u, x_j, x_l are not collinear, since they lie on distinct arms and differ from u. So c′·u > 0 strictly. Along S_j, c′·w is affine, positive at u and zero at x_j, hence negative at e_j; likewise at e_l. Then c′·e_o = 3c′·u − c′·e_j − c′·e_l > 0.
  - Case B: the pattern is immediate.
  - Strict guidance follows as in Y3.1(a): at a majority world, ℓ(M) = −c_j < 0 = ℓ(S) < ℓ(O) = −c′_j; at the odd world the order is reversed; × is worst.
- **(b) M-part.** The field's M-part is {c·w > 0}, which is exactly the posterior's M-part.
- **(b) O-part, case A.** c′·w is positive on all of S_o (it is positive at u and at e_o), and on S_j, S_l it is positive exactly on [u, x_j) and [u, x_l). This is Lemma Z1.5 in case A.
- **(b) O-part, case B.** c′·w = w_o − θ:
  - on S_o it is increasing and vanishes at x_o;
  - on S_j (j ≠ o), w_o ≤ 1/3 < θ, so it is negative.

  This is Lemma Z1.5 in case B.
- **(b) The cells.** Posterior M and O are disjoint, so on Σ never c·w > 0 and c′·w > 0 at once. The field's minimiser over {S, M, O, ×} is therefore M iff c·w > 0, O iff c′·w > 0, and S otherwise. (When c·w > 0 ≥ c′·w, M beats O.)
- **(b) Ties.** For fixed w ∈ Σ, the ties form a null set. c·w = 0 means P_{K_w}(h) = 0. c′·w = 0 on S_k means w = x_k(h), that is, max_{K_w} m·h = 0. Both are null cone boundaries. At u, c′·u ≠ 0 strictly in both cases.
- **(b) Vertices.** Strict guidance makes B^k the unique e_k-Bayes model. ∎

CHECKED (`z1_star_check.out`):
- 1500 exact pairs per ε ∈ {1/20, 1/10, 3/10, 1/2, 4/5};
- about 40 000 star points per ε, including u, the three vertices, and points 10⁻⁶ and 10⁻¹² on either side of every crossing;
- field Bayes advice = posterior advice: **0 mismatches**;
- sign-pattern failures: **0**;
- exact ties: 0;
- case A in 95–440 pairs, case B in the rest.

Negative control (`z1_controls.out` (1)): the same field with the O-attribution frozen at u (the X2.6 field at p = u) gives 10–40 mismatches per 6000 star points. So the construction of c′ is doing real work.

**Theorem Z1.7 (connected two- and three-vertex system through T1; PROVED).** Fix 0 < η < 1/2, N_k := {p : p_k ≥ 1−η}, and Σ as above. Put I := N₁ ∪ N₂ ∪ N₃ ∪ Σ (or N₁ ∪ N₂ ∪ S₁ ∪ S₂). Define:
- ρ_k(p) := 3 min_{j≠k} p_j and φ_k(p) := e_k + ρ_k(p)(u − e_k) on N_k;
- φ := id on Σ;
- C_p := B_{φ(p)} of Ψ^★.

Then:
1. **The selection.**
   - C_p = D_{K_p} (posterior) for p ∈ Σ, and C_u = T1.
   - C_p = B^k on N_k ∩ ∂Δ, the two incident edges near e_k.
   - C_p = D_{K_{φ_k(p)}}, an imprecise interior triangle varying with p, at interior p ∈ N_k.
   - I is connected and contains u as a non-isolated point.
2. **The axioms.** Against every measurable X, at every p ∈ I:
   - strict (G), (IB) and transitivity, globally;
   - (K) on supp p, (R4) and (Csel);
   - closed sections relative to I, with the fixed plan V(p,i,X) = {q ∈ I : Ψ^★_i(C_q) > Ψ^★_i(X)}.
3. **Fragments.** The assignment x_{i,r} := [Ψ^★_i(r) ≥ 0] satisfies Θ_C|_I ∪ Plan(V) ∪ {T1 ∈ C_L}. By Prop. X1.3.2, so does every finite fragment, with the same plan; nothing is re-chosen per fragment.
4. **The audit's guards.** The splice constraints of AUDIT_Y123 Props. 1–5 hold automatically, because the orders are additive.

*Proof.*
- **φ is well defined and continuous.**
  - On S_k ∩ N_k, p = e_k + r(u − e_k) has p_j = r/3 (j ≠ k), so ρ_k(p) = r and φ_k = id there.
  - η < 1/2 makes the N_k pairwise disjoint, and since η < 2/3 they miss u and the other arms.
  - The pieces are closed, so continuity follows by pasting.
- **φ is face-respecting.** If p ∈ N_k ∩ ∂Δ, then ρ_k = 0 and φ(p) = e_k with k ∈ supp p. Interior p have full support.
- **φ maps into Σ ⊆ W(Ψ^★)**, by Lemma Z1.6(b), and w ↦ D_{K_w} is continuous in measure, since p ↦ K_p is Hausdorff-continuous (X2.5) and the boundaries are null.
- Apply Lemma Z1.2. ∎

**What Z1.7 is and is not.**
- It is one triple of independent preorders that protects T1 and carries closed coherent selections on neighbourhoods of two (indeed three) vertices, connected through T1. It uses one shared plan and is not three separate systems.
- It is the "weaker first stage" of AUDIT_Y123 §6, and also the connected version, along one-dimensional arms.
- It does **not** carry a two-dimensional interior region through T1, nor any full edge (§4).
- The selection is the posterior family on the arms, with identity parametrisation, so the user's preferred candidate is used where it is defined. No selected model is required to be Bayes at its own index off Σ.

---

## 4. Where additivity stops: three-point forcing

**Proposition Z1.8 (PROVED; CHECKED).** No strictly guiding additive field on the full domain has the posterior model D_{K_w} as its w-Bayes model for (a dense set of) every w ∈ Σ ∪ [e₁,e₂].

*Proof.*
- **Chart lines.** For a.e. pair, the Bayes cells of an additive field are cut by the lines {c·w = 0}, {c′·w = 0} and {d·w = 0} (R1 Prop. 2.1). The usual countable-dense argument (Y3.7, Step 1) makes this hold for all w at once.
- **The O–S boundary is the c′-line.** At a posterior O-boundary point, the advice passes from O to S, never directly to M, because K_w is not a singleton there. So such a point lies on the c′-line.
- **Three points.** Take a case-A pair with o = 1. By Lemma Z1.5(a), the c′-line passes through x₂ ∈ S₂ and x₃ ∈ S₃. On the edge [e₁,e₂], the posterior edge model passes from O to S at w₂/w₁ = 1/(At₂) (Y2.1(b)), which gives a third point z.
- **Non-collinearity.** CHECKED below: for 184–189 of 200 exact case-A pairs per ε, z is not on the line x₂x₃. Non-collinearity is an open condition in h, so it holds on a set of positive measure.
- **Contradiction.** One line cannot pass through three non-collinear points. ∎

CHECKED (`z1_controls.out` (4)), exact: for example, at ε = 3/10 and h = (−3.41, 0.399…, 0.978…), the forced line meets the edge at s\* = 0.8819, while the posterior boundary is at 0.7888.

NUMERICS (`z1_controls.out` (3)): a per-pair LP over sampled constraints finds no admissible O-line for 2–5% of random pairs. This understates the failure, because the edge was sampled only at spacing 1/40. The exact test (4) is the reliable one.

*Meaning.*
- In additive form, the star works because every pair meets **at most two** forced O-boundary points: on the odd arm the chart is free (case A) or the other arms are empty (case B).
- Adding any loop (an edge, or a second path) produces a third forced point, and then non-collinearity kills additivity *for that selection*.
- This is the local, finite-certificate shadow of Thm gm. It is consistent with Y2.11 and Y2.12, whose hypotheses involve all three edges, and with Y3.8, which uses two-dimensional open sets.
- Prop. Z1.8 concerns the posterior selection only. A different family on the edge (Remark Z1.9) or on the arms might fit; that is the open question below.

**Remark Z1.9 (an additive field with a full posterior edge and T1; PROVED as sketched, not CHECKED).**
- Take the cube field Ψ^□ (Y3.5), whose Bayes models on all of ∂Δ are posterior.
- Replace its O-vectors c′ only on the bounded sets D_o where the cube's u-decision differs from T1's.
  - On Q₁ ∩ D₁, use c′ = (1, −At₂, −(t₃ + λ(t₃ − t₂)⁺)).
  - Q₂ ∩ D₂ is symmetric.
  - On Q₃ ∩ D₃, use b = (At₁, At₂ − λt₁) if t₂ ≥ t₁, and its mirror otherwise.
- The modified field has:
  - T1 = B_u, a.e. uniquely;
  - unchanged posterior Bayes models on the whole edge [e₁,e₂], and on edges [e₁,e₃], [e₂,e₃] within w₃/w₁, w₃/w₂ < 1/(2A).

  This follows because the modified coordinates enter only at weights where those ratios are ≥ 1/(2A), or not at all.
- With plateaus or edge retractions at N₁, N₂, Lemma Z1.2 then gives "two vertices plus the edge [e₁,e₂] plus T1" with genuinely posterior edges.
- T1 is still isolated here. Z1.7 supersedes it for connection, so I did not check it numerically.

---

## 5. What this changes, and the next target

1. **Y3.C** (two vertex neighbourhoods, additive, T1 ∈ C_L) is refuted:
   - trivially (Z1.1);
   - with the connecting edge (Z1.9);
   - with connection through T1 along arms, using non-constant interior selections near the vertices (Z1.7).
2. **Y3.7(b)** survives only in the form "identity-parametrised Bayes coherence on *two-dimensional* neighbourhoods of two vertices".
   - **CONJECTURE Z1.C** (this is what Y3.C should have said): no additive field with T1 = B_u has a.e.-unique coherent Bayes models at every weight of relative open neighbourhoods of e₁ and e₂.
   - *Heuristic reduction, not a proof.* If both families have blow-up (tangent-cone) limits at the vertices, the limits are homogeneous with straight level lines, hence boxes (Y3 §5). T1's pencils pin them to B₁ and B₂ (Y3.7(a)), and the third-axis gambles then conflict (Y3.7(b)).
   - Third-axis analysis (§0 item 3; derivation in my working, not CHECKED):
     - against B₂ at e₂, the e₁ family's "bottom-right" support point must be (s,t), while T1's mirror pencils pin it to (As,t) in box form;
     - discretely self-similar, non-box families are not excluded by this argument.
3. **For T1.** Within reparametrised additive constructions, the T1 obstruction is a *filling* obstruction (Cor. Z1.4): a 2-cell, or a full edge plus arms. Locally it appears as **three-point forcing** (Prop. Z1.8).
4. **The non-additive target, made precise.** Build independent preorders (transition records) on the loop
   L₁₂ := [u,e₁] ∪ [e₁,e₂] ∪ [e₂,u]
   that keep the posterior selection, or any coherent family, on L₁₂, with T1 at u.
   - The additive chart for a case-A pair is a single line forced through x₂, x₃ and z. A non-additive world must therefore accept, for such pairs, the O-boundary comparisons at the three points without their implied collinear extension.
   - In record terms: the comparisons that an additive primary makes between the edge model at z and the arm models at x₂, x₃ must be discarded where they cross, while every genuine guidance improvement stays strict (AUDIT_Y123 §4).
   - Lemma Z1.2 still handles everything off the loop, and the star field supplies the arms.
5. **Obstruction branch.** No obstruction valid for all independent preorders was found, and none can exist on index sets of the Z1.7 type, because Z1.7 is a model. Any such obstruction must use an index set that encloses a region or contains a full edge.

---

## 6. Status

| Item | Status |
|---|---|
| Z1.1 vertex plateau; literal Y3.C false; Y3.4 follows from it | PROVED |
| Z1.2 reparametrised Bayes subsystems (all clauses, fixed plan) | PROVED |
| Z1.3 face-respecting self-maps of Δ are surjective | PROVED (standard) |
| Z1.4 reparametrised additive selection on Δ ⇒ additive cover (excluded by Thm gm) | PROVED |
| Z1.5 O-sets of the posterior along the three medians are end-intervals | PROVED; CHECKED |
| **Z1.6 star field Ψ^★: Bayes = posterior on the whole star, T1 = B_u, strictly guiding** | **PROVED; CHECKED (0 mismatches, ~2·10⁵ exact points)** |
| **Z1.7 one additive system: T1 connected to neighbourhoods of two (three) vertices, all axioms against all measurable X, fixed plan** | **PROVED** |
| Z1.8 posterior on star + full edge is not additive (three-point forcing) | PROVED; CHECKED (exact); NUMERICS (LP) |
| Z1.9 cube field modified on D_o: full posterior edge + T1 | PROVED (sketch); not checked |
| Z1.C additive two-vertex 2-D Bayes coherence with T1 is impossible | CONJECTURE |
| Non-additive loop L₁₂ system | open (next target) |

**Referee priorities.**
1. Lemma Z1.5(a): the "all pieces positive at the far end" step.
2. Lemma Z1.6, case A: the orientation of c′ = x_j × x_l and the sign at e_o.
3. Lemma Z1.2: competitiveness uses supp φ(p) ⊆ supp p.
4. Prop. Z1.8: that the posterior O-boundary is an O–S transition, so that it lies on the c′-line.

## 7. Files (`z1py/`)
- `z1common.py`: exact helpers (posterior advice, arm crossings, the vectors c and c′, field advice).
- `z1_star_check.py` / `.out`: Lemmas Z1.5 and Z1.6 (CHECKED).
- `z1_controls.py` / `.out`:
  - (1) frozen-attribution negative control;
  - (2) NUMERICS: the star field differs from the posterior off the star (57–67 of 2000 random interior weights), as Y3.8 requires;
  - (3) LP NUMERICS for star plus edge;
  - (4) exact forced-line test for Prop. Z1.8.
