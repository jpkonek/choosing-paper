# DPR73: dominance under consolidation with a margin (Theorem D′)

27 Oct 2026. Sources: BRIEF73; PRO73 §§2, 5, 6; MU73 §2; CEX73 §§1, 3; app.tex §2, Def. 6.1, Lemma `lem:test`, Props `prop:structure`, `prop:protect`, §8. Hand proofs. One numerical check: `dpr73_py/mu_m3_check.py`.

## Conventions

**Shorthand.**
- N := {h : sup_Ω h < 0} and D_S = {h : inf_Ω h > 0}. Both are open in E.
- B(h, r) is the open sup-norm ball.
- "Y dominates X" is the manuscript's notion: Y ⪰_ω X at every world, and X ⪰_ω Y fails at some world.

**Margin triple of order c ∈ {1, 2}** (MU73's convention):
- G₁, G₂, G₃ are pairwise disjoint non-null models with μ(G₁) = μ(G₂) = μ(G₃)/c. So μ(G₃) = 2μ(G₁) in the midpoint case.
- For μ⊗³-a.e. (x, y, z) ∈ G₁ × G₂ × G₃, z(ω) > (x + y)(ω)/c at every ω.
- For W ⊇ G₁ ∪ G₂ with W ∩ G₃ null, the consolidation is W′ = (W ∖ (G₁ ∪ G₂)) ∪ G₃.

**The axioms.**
- **(CAm)** For every margin triple, every such W and every world ω: W′ ⪰_ω W.
- **(TT)** If Z ~_ω X and Y ⪰_ω Z, then Y ⪰_ω X.

**Setting (S).** This is the paper's general setting:
- Ω is arbitrary.
- E ⊆ ℓ∞(Ω) is a separable, norm-closed subspace containing 𝟙.
- μ is a finite Borel measure that is atomless and satisfies (M2) and (M3).

(M1) is not used by Theorem D′. It is used only so that R0 is defined.

---

## Results

| # | Statement | Label |
|---|---|---|
| 1 | **Theorem D′.** In setting (S), let R satisfy (G), (SC), (CAm) and (TT). Then every incoherent model is dominated. (R), (I), (P) and maximality are not used. | **PROVED** |
| 1a | The dominator is explicit. It is one of at most three models built from X, using one consolidation, a second consolidation of the result, and the change that is guided at every world. It need not be coherent. | PROVED |
| 1b | (CAm) is needed only for triples with a uniform margin (inf_Ω(z − (x+y)/c) bounded below by a positive constant) whose pieces lie in small sup-norm balls. Both orders c = 1 and c = 2 are used. Midpoints cannot be dropped: sums alone do not force cones. | PROVED |
| 1c | **Atoms.** Theorem D′ still holds if μ has atoms, provided the atomless part μ_c has full support. | PROVED (sketch, §2.7) |
| 1d | **Restricted domain.** Let U be an open convex cone containing D_S, such as veto–Brier's {p·h > 0}. Rankings on the models on U that satisfy (G), (SC), (TT) and (CAm) for triples and contexts in U dominate every incoherent model on U. | PROVED (sketch, §2.8) |
| 2 | **(M3) cannot be dropped.** For MU73 §1.3's μ (Lebesgue measure on three small balls), the ranking R_g satisfies (G), (SC), (TT), (CAm) and (P), and leaves an incoherent model undominated. | CHECKED + NUMERICS |
| 3 | **(G) cannot be dropped.** The relation that ties every pair of models satisfies (SC), (CAm), (TT) and (P), and dominates nothing. | PROVED (trivial) |
| 4(a) | **R0 satisfies (CAm)**, strictly: W′ ≻_ω W at every world. The lead's argument is correct. A more direct form is in §3.1. R0 has no ties between distinct models, so (TT) holds trivially. | **PROVED** |
| 4(a′) | **Equality case.** R0 **violates** PRO73's exact (CA). For an exact triple, the score increment is 0 at every world, so R0 leaves W and W′ incomparable at every world. The same happens for every "≥"-margin triple with zero increment at some world. So the strict margin is essential for R0's membership, and moving from (CA) to (CAm) is necessary, not cosmetic. | PROVED |
| 4(b) | **Veto–Brier satisfies (CAm)** on U, strictly at every world, and (TT), because it is transitive. It does not protect every coherent model, so it fails (P). Theorem D′ on U (item 1d) applies to it. | PROVED |
| 4(c) | **R_GC** (PRO73, two worlds, exact-triple generators): whether it satisfies (CAm) is **UNCLEAR**. The obstacle is writing an arbitrary margin consolidation as a *finite* sum of exact consolidations and guided pieces. **R_GC^m**, the same construction with margin-triple generators, satisfies (R), (G), (I), (SC), (TT) and (CAm) for every Ω, and (P) for Ω = {1, 2} by PRO73's own argument. It is a score-free member of the full class for two worlds. | (R)–(TT), (CAm): PROVED. (P) for n = 2: PROVED, given PRO73 §6. (P) for n ≥ 3: UNCLEAR |
| 4(d) | **Within 𝓡, (CAm) implies (C3m)**; only (SC) is needed. The converse fails. The guided-only ranking R_γ lies in 𝓡 + (C3m) + (TT), violates (CAm), and leaves every incoherent model with D_S ⊆ X and X ∩ {sup ≤ 0} null undominated. So C3m cannot replace CAm in Theorem D′. | PROVED |
| 5 | **Exact statement (true).** See below. | PROVED |

**Item 5, exact statement.** Let Ω be any nonempty set, and let E ⊆ ℓ∞(Ω) be separable, norm-closed and contain 𝟙. Let μ be atomless and satisfy (M1)–(M3); such μ exist for every such Ω and E (the measure built in the proof of `lem:measure` is atomless). Let 𝓒 be the class of rankings satisfying (R), (G), (I), (SC), (P), (CAm) and (TT). Then:
- 𝓒 is nonempty, because R0 ∈ 𝓒;
- every member of 𝓒 dominates every incoherent model.

**What (P) adds.** In every member of 𝓒:
- a model is undominated iff it is coherent;
- (P) gives one direction and Theorem D′ the other.

As a result, every member of 𝓒 meets the following coverage requirements, for every credal set K:
- global coherence (2);
- closure under ties (3), because a model tied at every world with an undominated coherent model is undominated by the tie lemma, hence coherent by Theorem D′;
- the target is undominated (4b).

**Not delivered:** requirement (5), that each incoherent model be dominated by an *undominated coherent* model. That needs undominated weak dominators to exist. It holds for R0 (Theorem `thm:main`), but in 𝓒 in general it is OPEN.

**Not used:** maximality, (R), (I) and (M1) play no role in Theorem D′.

**Remaining OPEN questions.**
- Whether (TT) can be dropped.
- Whether R_GC (with exact generators) or R_GC^m protects every coherent model for |Ω| ≥ 3.
- Requirement (5) within 𝓒.

---

## 2. Proof of Theorem D′

Throughout §2, R satisfies (G), (SC), (CAm) and (TT), in setting (S).

**Preliminaries.**
- For a model X, X⁺ := supp(μ|X), the set of h with μ(X ∩ B(h, ε)) > 0 for all ε > 0. It is closed, and μ(X ∖ X⁺) = 0 by Lindelöf (E is separable metric).
- "Atomless" is used only through Sierpiński's theorem: every set of measure a contains subsets of every measure in [0, a].

**Properties of a model X.**
- **(U1)** D_S ⊆ X a.e. and X ∩ N is null.
- **(U2)** μ⊗μ(P_X) = 0, where P_X := {(x, z) ∈ X × (E∖X) : z − x ∈ D_S}.

In words, (U2) says X is upward closed modulo μ.

### 2.1 Lemma 1 (undominated ⇒ (U1))

*Proof.* Let Y := (X ∪ D_S) ∖ N. The change from X to Y adds D_S ∖ X and removes X ∩ N.
- Every added gamble pays more than 0 at every world, and every removed gamble pays less than 0 at every world. So the change is guided by every world.
- If it is non-null, (G) gives Y ≻_ω X at every ω, so Y dominates X. ∎

### 2.2 Lemma 2 (tie lemma)

**Statement.** If Z ~_ω X at every ω and Y dominates Z, then Y dominates X.

*Proof.*
- By (TT), Y ⪰_ω X at every ω.
- Let ω₀ be a world with Y ≻_{ω₀} Z. If X ⪰_{ω₀} Y, then Z ⪰ X ⪰ Y is a chain at ω₀ whose last model is strictly better than its first. (SC) forbids this.
- So X ⪰_{ω₀} Y fails, and Y dominates X. ∎

### 2.3 Lemma 3 (consolidations of undominated models)

**Statement.** If X is undominated and X′ is a margin consolidation of X, then X′ ~_ω X at every ω, and X′ is undominated.

*Proof.*
- (CAm) gives X′ ⪰_ω X at every ω. Since X′ does not dominate X, X ⪰_ω X′ at every ω, so the two are tied at every world.
- If some Y dominated X′, Lemma 2 would make Y dominate X. ∎

### 2.4 Lemma 4 (a margin consolidation that removes part of D_S)

**Statement.** Assume X satisfies (U1) but not (U2). Then X has a margin triple of order 1 with G₂ ⊆ D_S. Its consolidation X^D therefore violates (U1).

*Proof.*
1. Let W^D := {(x, y, z) ∈ X × D_S × (E∖X) : z − x − y ∈ D_S}. Take (x, z) ∈ P_X. Its y-section, D_S ∩ (z − x − D_S), is open and contains (z − x)/2, so it has positive measure by (M3). By Tonelli, μ⊗³(W^D) > 0.
2. W^D is the union over j of W^D_{1/j} := {inf_Ω(z − x − y) ≥ 1/j}. Fix δ with μ⊗³(W^D_δ) > 0.
3. Cover E by countably many balls of radius δ/8. Some product B₁ × B₂ × B₃ meets W^D_δ in positive measure.
4. Each coordinate of a point in B₁ × B₂ × B₃ lies within δ/4 of the corresponding coordinate of some point of W^D_δ. So inf_Ω(z − x − y) ≥ δ − 3δ/4 = δ/4 for **every** (x, y, z) in the product.
5. By Tonelli, μ(X ∩ B₁), μ(D_S ∩ B₂) and μ(B₃ ∖ X) are positive. By (U1), μ(D_S ∩ X ∩ B₂) = μ(D_S ∩ B₂).
6. Choose 0 < m < min{μ(X ∩ B₁), μ(D_S ∩ X ∩ B₂)/2, μ(B₃ ∖ X)}. Then pick G₁ ⊆ X ∩ B₁, G₂ ⊆ (D_S ∩ X ∩ B₂) ∖ G₁ and G₃ ⊆ B₃ ∖ X, each of mass m.
7. These sets are pairwise disjoint: G₃ lies outside X, which contains the other two.
8. X^D misses G₂ ⊆ D_S, and μ(G₂) = m > 0. ∎

**Corollary 4′.** Every undominated X satisfies (U1) and (U2).

*Proof.*
- Lemma 1 gives (U1).
- If (U2) failed, Lemma 4 would give X^D, which is undominated by Lemma 3 and violates (U1). That contradicts Lemma 1. ∎

### 2.5 Lemma 5 (the open part of X)

**Statement.** Assume (U1) and (U2), and put V := X⁺ + D_S. Then:
- (a) V is open, and V ⊆ X a.e.;
- (b) X ⊆ cl V a.e.;
- (c) cl V + D_S ⊆ V;
- (d) D_S ⊆ V, and V ∩ {sup ≤ 0} = ∅;
- (e) if V is closed under sums and midpoints, then X = V = D_K a.e. for K = K_V, so X is coherent.

*Proof.*

**(a)**
- V is a union of open sets, so it is open.
- By Lindelöf, V = ⋃_k (x_k + D_S) with x_k ∈ X⁺.
- Suppose μ(V ∖ X) > 0. Then some A := (x_k + D_S) ∖ X has μ(A) > 0. Take z ∈ A ∩ supp(μ|A), and set 3δ := inf_Ω(z − x_k) > 0.
- For x ∈ B(x_k, δ) and z′ ∈ B(z, δ), we have inf_Ω(z′ − x) > δ.
- μ(X ∩ B(x_k, δ)) > 0 and μ(A ∩ B(z, δ)) > 0, so μ⊗μ(P_X) > 0. This contradicts (U2).

**(b)** X ⊆ X⁺ a.e. For x ∈ X⁺, x + ε𝟙 ∈ V and x + ε𝟙 → x.

**(c)** Let v_n → v with v_n ∈ V, and let d ∈ D_S. Then v + d = v_n + (v − v_n + d), and v − v_n + d ∈ D_S for large n, because D_S is open.

**(d)**
- Every ball inside the open set D_S has positive measure (M3) and lies in X a.e. (U1). So D_S ⊆ X⁺.
- For d ∈ D_S, d = (d − t𝟙) + t𝟙 with d − t𝟙 ∈ D_S ⊆ X⁺ for small t > 0. So d ∈ V.
- Suppose v ∈ V has sup v ≤ 0. Then v − t𝟙 ∈ V for small t > 0, so the open set V ∩ N is nonempty, and it has positive measure by (M3). But V ∩ N ⊆ X ∩ N a.e., which is null by (U1). Contradiction.

**(e)**
- An open midpoint-convex set is convex.
- For λ ∈ (0, 1) and v ∈ V, choose η with v − η𝟙 ∈ V and put ε = λη/(1 − λ). Then λv = λ(v − η𝟙) + (1 − λ)ε𝟙 ∈ V, since ε𝟙 ∈ D_S ⊆ V.
- Sums give 2ᵏv ∈ V. So V is an open convex cone. It contains D_S, and 0 ∉ V by (d).
- By `lem:identify`(b), D_K ⊆ V ⊆ C_K, so ∂V = cl V ∖ V ⊆ {P_K = 0}, which is null by (M2).
- With (a) and (b): V ⊆ X ⊆ cl V a.e., so X = V a.e. Also V ∖ D_K ⊆ {P_K = 0}, so X = D_K a.e. ∎

### 2.6 Lemma 6 (a gap in V gives a consolidation that breaks upward closure)

**Statement.** Assume (U1) and (U2), let c ∈ {1, 2}, and let v₁, v₂ ∈ V with s := (v₁ + v₂)/c ∉ V. Then X has a margin triple of order c whose consolidation X′ violates (U2).

*Proof.*

**Choice of parameters.**
- Choose η > 0 with B(v_i, 2η) ⊆ V for i = 1, 2. Put r := η/8.
- Put v_i′ := v_i − η𝟙, s′ := (v₁′ + v₂′)/c = s − (2η/c)𝟙, and z₀ := s − (η/c)𝟙.

**The three balls.**
- B(v_i′, r) ⊆ B(v_i, η + r) ⊆ V, so these balls lie in X a.e.
- **No gamble near z₀ is in X.** For z ∈ B(z₀, r), inf_Ω(s − z) ≥ η/c − r > 0, so z ∈ s − D_S. The set s − D_S is disjoint from cl V: if w ∈ cl V and s − w ∈ D_S, then s ∈ cl V + D_S ⊆ V by Lemma 5(c), which is false. Hence B(z₀, r) ∩ X is null, by Lemma 5(b).
- **Margin.** For x ∈ B(v₁′, r), y ∈ B(v₂′, r) and z ∈ B(z₀, r):

  inf_Ω(z − (x + y)/c) ≥ η/c − r − 2r/c,

  which is 5η/8 for c = 1 and η/4 for c = 2. Both are positive.
- **A ball below G₁.** L₀ := B(v₁′ − 3r𝟙, r) ⊆ B(v₁, η + 4r) ⊆ V. Also inf_Ω(x − w) > r for every x ∈ B(v₁′, r) and w ∈ L₀. So L₀ is disjoint from B(v₁′, r).

**The triple.**
- Choose 0 < m < min{μB(v₁′, r)/2, μB(v₂′, r)/2, μB(z₀, r)/c, μ(L₀)/2}. Every term is positive by (M3).
- Pick G₁ ⊆ B(v₁′, r) of mass m, G₂ ⊆ B(v₂′, r) ∖ G₁ of mass m, and G₃ ⊆ B(z₀, r) of mass cm.
- G₃ is disjoint from G₁ ∪ G₂, since s − D_S misses cl V.
- G₁ ∪ G₂ ⊆ X a.e. and G₃ ∩ X is null. So this is a margin triple of order c inside X, with a uniform margin.

**X′ violates (U2).**
- Let L := L₀ ∖ G₂, so μ(L) > μ(L₀)/2 > 0. L misses G₁ ∪ G₂ and lies in X a.e., so L ⊆ X′ a.e.
- G₁ ∩ X′ = ∅.
- For (w, x) ∈ L × G₁, x − w ∈ D_S. So μ⊗μ(P_{X′}) ≥ μ(L)·μ(G₁) > 0. ∎

### 2.7 Proof of Theorem D′

Suppose X is incoherent and undominated.
1. By Corollary 4′, X satisfies (U1) and (U2).
2. By Lemma 5(e), V is not closed under sums or midpoints. So there are v₁, v₂ ∈ V and c ∈ {1, 2} with (v₁ + v₂)/c ∉ V.
3. Lemma 6 gives a margin consolidation X′ of X that violates (U2).
4. X′ is undominated by Lemma 3, so it satisfies (U2) by Corollary 4′. Contradiction. ∎

**The explicit dominator (item 1a).** Let X be incoherent.
- If X violates (U1), the model guided at every world, (X ∪ D_S) ∖ N, dominates X.
- If X satisfies (U1) but not (U2), take X^D from Lemma 4.
  - If X^D dominates X, it is the dominator.
  - Otherwise X^D ~ X at every world. Then the guided rival of X^D, namely (X^D ∪ D_S) ∖ N = (X^D ∪ G₂) ∖ N, dominates X^D, and so dominates X by Lemma 2.
- If X satisfies (U1) and (U2), take X′ from Lemma 6.
  - If X′ dominates X, it is the dominator.
  - Otherwise X′ ~ X at every world. Then apply the previous two cases to X′, which violates (U2), and transfer the dominator to X by Lemma 2.

**Atoms (item 1c), sketch.**
- By (M2), every atom lies in D_S ∪ N (MU73 §1.2).
- Under (U1), pairs in P_X that involve an atom are μ⊗μ-null:
  - atom–atom pairs: an atom z ∈ D_S ∖ X is excluded;
  - an atom x with diffuse z: then x ∈ D_S, so z ∈ D_S ∖ X, which is null;
  - a diffuse x with an atom z: then z ∈ N, so x ∈ z − D_S ⊆ N, which is null.
- So (U2) for μ is (U2) for μ_c. Run Lemmas 4–6 with μ_c, which needs (M3) for μ_c, and choose the G_i off the countable set of atoms.
- The conclusion X = D_K μ_c-a.e. extends to the atoms, because X and D_K both contain D_S and both miss N.

**Restricted domain U (item 1d), sketch.** Let U be an open convex cone containing D_S. Changes:
- The guided rival stays in U.
- In Lemma 4, take G₃ ⊆ (B₃ ∩ U) ∖ X. This is non-null because x + D_S ⊆ U.
- In Lemma 6:
  - First replace v_i by v_i − t𝟙. Then s ∉ cl V, by Lemma 5(c).
  - Then perturb v_i into the dense open set V ∩ U; V ∖ cl U is open and null, hence empty.
  - Now s ∈ U, and η can be chosen with B(s, 2η) ⊆ U. All three balls then lie in U.
- The conclusion is X = D_K a.e. with D_K ⊆ U.

---

## 3. Membership

### 3.1 R0 satisfies (CAm) strictly (PROVED; uses (M1))

Fix a margin triple of order c, a context W and a world ω. The change from W to W′ adds G₃ and removes G₁ ∪ G₂.

**No coherent model could make it.**
- Suppose D_Q ⊇ G₁ ∪ G₂ a.e.
- For a.e. z ∈ G₃, the margin holds for μ⊗²-a.e. (x, y) ∈ G₁ × G₂ (Tonelli). Pick such (x, y) with x, y ∈ D_Q.
- Put p := z − (x + y)/c ≥ 0. Then P_Q(z) ≥ P_Q((x + y)/c) + P_Q(p) ≥ (P_Q(x) + P_Q(y))/c > 0, using superadditivity and positive homogeneity of P_Q, and P_Q ≥ 0 on gambles that are ≥ 0.
- So G₃ ⊆ D_Q a.e., while the change needs G₃ ∩ D_Q null with μ(G₃) > 0.
- (M2) is not needed. This is the lead's "G₃ ⊆ hull(G₁ ∪ G₂)" when G₁ ∪ G₂ is consistent. When it is inconsistent, the first disjunct of `lem:test` applies.

**The score rises strictly.**
- Let π := (μ|G₁ ⊗ μ|G₂ ⊗ μ|G₃)/(c m²) with m = μ(G₁). Its marginals are μ|G₁, μ|G₂ and μ|G₃/c, and its total mass is m > 0.
- So m_ω(W′) − m_ω(W) = ∫[c z(ω) − x(ω) − y(ω)] dπ. The integrand is π-a.e. positive and integrable by (M1), so the difference is positive. This holds at every ω, with no uniformity needed.

**Conclusion.**
- Def. 6.1(ii) gives W′ ⪰_ω W at every ω. Since R0 has no ties between distinct models (`prop:structure`(b)), W′ ≻_ω W.
- So in R0, every margin consolidation strictly dominates the model it consolidates (`prop:strict`).
- **(TT):** Z ~_ω X forces Z = X a.e., and then Y ⪰_ω Z iff Y ⪰_ω X, by (R) and independence.
- **Membership in 𝓒:** (R), (G), (I) and (SC) come from `prop:structure`, and (P) from `prop:protect`.

### 3.2 Equality cases (item 4(a′), PROVED)

**Exact triples.** For an exact triple (sum, with S(h) = h + T(h)):
- The increment is ∫_{G₁} [S(h) − h − T(h)](ω) dμ = 0 at every ω, and the same holds for midpoints.
- The change is not guided at any ω: z(ω) > 0 > x(ω), y(ω) is impossible when z = x + y.
- So R0 accepts neither W′ over W nor W over W′, at any world. Hence R0 ∉ (CA).

**"≥"-margins.** For a "≥"-margin triple, R0 accepts at exactly the worlds where ∫(c z(ω) − x(ω) − y(ω)) dπ > 0. The availability test above still fails for every coherent model, because the argument only needs P_Q(p) ≥ 0.

So the strict pointwise margin is what puts R0 in the class.

### 3.3 Veto–Brier (PROVED)

Take triples and contexts on U. Let π be as in §3.1.

**The veto level a_i does not rise.**
- Since v_i ≥ 0 and c z ≥ x + y pointwise, c[−v_i·z]⁺ ≤ [−v_i·(x + y)]⁺ ≤ [−v_i·x]⁺ + [−v_i·y]⁺.
- So Δa_i = ∫(c[−v_i·z]⁺ − [−v_i·x]⁺ − [−v_i·y]⁺) dπ ≤ 0.

**The Brier level b_i falls strictly.**
- Δb_i = −∫(c z_i − x_i − y_i) dπ < 0.

**Conclusion.**
- Lexicographically, W′ is strictly better than W at every world, so (CAm) holds.
- ⪯_i is a total preorder, so (TT) holds. (G) and (SC) come from Thm `thm:vb`(a).
- (P) for all coherent models on U fails: U = D_{p} is dominated (§8 of app.tex).
- So veto–Brier is covered by item 1d but is not in 𝓒.

### 3.4 R_GC and R_GC^m (item 4(c))

**R_GC^m.** Let cone^m_ω be generated by:
- ±1_K μ, with K ⊆ {h(ω) > 0} for + and K ⊆ {h(ω) < 0} for −;
- (1_{G₃} − 1_{G₁} − 1_{G₂})μ, for margin triples of either order.

Put X ⪰_ω Y iff (1_X − 1_Y)μ ∈ cone^m_ω.

**Properties.**
- (R), (I) and transitivity are immediate, and transitivity gives (SC) and (TT). (CAm) holds by construction.
- **(G):** every generator has ∫h(ω) dν ≥ 0. For margin generators, ∫(c z(ω) − x(ω) − y(ω)) dπ > 0. The reverse of a non-null guided change has ∫h(ω) dν < 0. This uses (M1) and works for any Ω.
- So R_GC^m satisfies the hypotheses of Theorem D′ for every Ω.
- **(P) for Ω = {1, 2}:**
  - PRO73 §6 uses only that each generator ν of cone_ω has ∫ f_ω(h(ω)) dν ≥ 0, for f_ω increasing and superlinear.
  - For a margin generator, ∫[c f(z(ω)) − f(x(ω)) − f(y(ω))] dπ ≥ ∫[f((x + y)(ω)) − f(x(ω)) − f(y(ω))] dπ ≥ 0. The first step uses that f is increasing and homogeneous; the second that it is superadditive.
  - So PRO73's (P) proof transfers unchanged. Adding the exact generators as well is harmless.
- (P) for |Ω| ≥ 3 is UNCLEAR, for PRO73 item 11's reason: separable functionals give only special Bayes sets.

**R_GC with exact generators only.** I could not decide whether it satisfies (CAm).
- The natural decomposition is: an exact consolidation into the midpoint region, then a lift s → z. The lift is written as an exact sum triple (s, d → s + d) with d ∈ D_S, plus guided re-addition of d.
- This needs the arbitrary measurable G₃ to be tiled exactly by finitely many images of exact triples. I do not see how to do that.
- Dual considerations suggest that every functional nonnegative on cone_ω is nonnegative on margin generators. That is evidence for membership in the closure, not in the cone itself. UNCLEAR.

### 3.5 (CAm) versus (C3m) (item 4(d), PROVED)

**(CAm) + (SC) ⇒ (C3m).**
- Suppose there is a chain Z ⪰_ω … ⪰_ω Z′ with a strict link A_j ≻ A_{j+1}.
- Close it with Z′ ⪰_ω Z from (CAm), and rotate the cycle to start at A_{j+1}. Its last model A_j is strictly better than its first, which (SC) forbids.

**The converse fails.** Let R_γ accept exactly the changes guided by ω.
- R_γ is transitive: an added gamble of the composite is added by one of the two steps, and likewise for removals. It has no ties between distinct models. So it satisfies (SC) and (TT).
- It is in 𝓡: (P) follows from the proof of `prop:protect`.
- It satisfies (C3m): by transitivity a forbidden chain gives Z ⪰_ω Z′, so G₁, G₂ ⊆ {h(ω) > 0} and G₃ ⊆ {h(ω) < 0}. That contradicts z(ω) > (x + y)(ω)/c > 0.
- It violates (CAm): a consolidation is guided only in degenerate cases.
- Any X with D_S ⊆ X and X ∩ {sup ≤ 0} null is undominated in R_γ. A weak dominator must be reached by a change guided at every world, so by `lem:guidedeverywhere` it differs from X by a null set. This includes incoherent X such as MU73's X*.

### 3.6 Sharpness of (M3) (item 2, CHECKED)

**Setting.** μ is MU73 §1.3's measure: Lebesgue measure on three sup-balls of radius 0.05 about a, b and n. R_g is AX72's ranking with g₁ = h₁ and g₂ = 3h₂, h₂/3, h₂ on the three balls.

**R_g satisfies (CAm).**
- A margin consolidation is unavailable to every coherent model (§3.1), so the refusal exception never applies to it.
- R_g therefore accepts it at ω iff Δs_ω > 0. For that it suffices that c g_ω(z) − g_ω(x) − g_ω(y) > 0 for every admissible ball combination.
- `dpr73_py/mu_m3_check.py` checks all 27 × 2 combinations, with 2·10⁵ samples each. The combinations that occur are within-ball midpoint triples, (a, n → a), (b, n → b), (n, n → a), (n, n → b) and (n, n → n). All have a positive minimum.

**The other axioms.**
- R_g has no ties between distinct models, so (TT) holds.
- (G), (SC) and (P) hold by AX72 §0 and MU73.
- MU73 shows that X* is strictly preferred to every rival at some world, so X* is undominated.

So Theorem D′ fails without (M3). This matches MU73's moral: consolidation binds only where μ links gambles by sums.

---

## Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/DPR73_report.md` (this report)
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/dpr73_py/mu_m3_check.py` (the (CAm) check for R_g in MU73's example without (M3))
