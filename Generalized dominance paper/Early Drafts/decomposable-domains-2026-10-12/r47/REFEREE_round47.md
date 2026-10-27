# Referee report, round 47: PP28, PP29, PP30

22 October 2026. Independent referee. I read Brief 47, AUDIT_selected_realizability, AUDIT_answers47, PP23 §§1–4, REFEREE_round46 §§2.3–2.5, AUDIT_completion, LEAD_selection_count, REFEREE_Z_PP19 (Lemma H) and PP19 Theorem 4, and checked each listed claim line by line. I did not edit any note. My scripts are in `r9/PP31_py/`. Each writes a `.out` file. I also re-ran all 10 of the authors' scripts, 16 runs in all with 7 SAT configurations (§5).

**Labels.** PROVED: complete argument here or in the note, checked. CHECKED: exact finite computation. NUMERICS: sampling. CONJECTURE: unproved.

---

## 0. Verdicts at a glance

| Note | Claim | Verdict |
|---|---|---|
| PP28 | Lemma 2.1, Cor 2.2 (separation) | correct |
| PP28 | Thm 3.1 (certificates over any base) | correct |
| PP28 | Prop 3.2 (closure idle) | correct as stated. But §0's "closure rules I–IV force nothing" for *any* base needs a hypothesis: the base itself must be closed under I–IV. "No selected model is weakly dominated" holds only for linear bases. |
| PP28 | Prop 3.3 (sections) | **correct with repair**: Lemma A needs the selected models undominated in the full system. The use of Lemma H is correct. |
| PP28 | Lemma 3.4 | correct |
| PP28 | Thm 4.1 | correct |
| PP28 | §4.2 instance | every defence obligation is met (checked below). One bookkeeping slip in "accepting worlds". The (S) clauses verified are listed in §1.4. **Closed sections fail** (NUMERICS, a level-0 jump at ∂M). Undominated incoherent models exist (PROVED). |
| PP28 | Thm 5.1 | correct |
| PP28 | Cor 5.1′ | correct. The type-(c) wording is ambiguous; it is the same cone condition as type (b). |
| PP28 | Prop 5.2 | **correct with repair**: the stated 2A and 3A conditions are incomplete (exact counterexample). The conclusion is unaffected. |
| PP28 | Prop 6.1 | correct |
| PP28 | Lemma 6.2 (not on my list) | **gap** for unbounded Z. Correct for bounded Z with Z′ = Z. Region-first (Z = M_k) is already covered by PP26 Thm V. |
| PP29 | Thm 4.1 (retreat split) | correct. It meets every support-sensitive obligation, including those from vertex and edge models. Independently CHECKED (exact). |
| PP29 | Thm 5.1, Prop 5.2 | correct |
| PP29 | Props 6.2, 6.4 | correct. In 6.4 "T selected" is not needed. |
| PP29 | Classification of escapes | **partly overclaimed**: three rows (§2.5) |
| PP30 | Prop 2.1, Lemma 2.2 | correct |
| PP30 | Thm 3.1 | correct |
| PP30 | Thm 3.2 | correct. The explicit G was CHECKED exactly with genuine balls. |
| PP30 | Prop 3.4, Remark 3.6 | correct |
| PP30 | Prop 4.2 | correct. It needs T selected (to define w(p,G)); this is implicit. |
| PP30 | Thms 5.1, 5.2, Lemma 5.3, Cor 5.4, Prop 5.5 | correct |

---

## 1. PP28 (selected-family co-design)

### 1.1 Separation lemma: correct

- **Lemma 2.1.** On D, x acts on D₁ ∪ D₃ with old side b. If that set is null in a touched class, y's old side is b on all of D_k, which carries an inverted pair. If it meets both D_k^A and D_k^B, Lemma 4.3 is violated. So it lies in exactly one of them. The rest of the case analysis is right, including Q = B (respectively A) on D₃: Q is y's old side there, so it is regular.
- Lemma 4.3 holds for every nonempty closed convex K ⊆ Δ, vertices and edges included. Its proof uses only the two open/closed corner conditions.
- **Cor 2.2.** Choose g ∈ D_k^B and g′ ∈ D_k^A from the full-measure sets where the realisers answer as stated and line(g) ≤ line(g′). Then K′ ⊂ tri(g) ⊆ tri(g′) and K ∩ cl tri(g′) = ∅.
- CHECKED: `separation_check.py` reproduces 834 doubly realised decompositions and 0 intersecting pairs among 16,150.

### 1.2 Certificates over an arbitrary base

**Thm 3.1: correct.**
- Strict (G) and (IB) are immediate.
- For (TC) via PP23 Lemma 1.1, I checked every triangle type through an 𝓘-edge d:
  - a second 𝓘 edge forces the third edge to have old side b on supp d, so it is neither in 𝒞 nor a departure, hence guidance, and then d·x is kind I, which is impossible;
  - one guidance edge reduces to a (P1) pair (d, c), and Lemma 4.4 needs only coherence of c's old side, which selected models have;
  - two 𝒞 edges are exactly (iii_sel).
- One point the note does not mention: an inverted d out of T is itself selected-realised (old side S on D ⊆ Sil(T)), so d may lie in 𝒞_i ∩ 𝓘_i. The proof is unaffected.

**Prop 3.2: correct; scope of the summary.**
- (a) An 𝓘-acceptance X ⪯ C_p would put an inverted pattern on the coherent C_p. So every weak dominator acts through the base. In a linear base, antisymmetry plus competitiveness excludes weak dominators.
- (b)–(d) correct: d⁻¹ is never accepted, so 𝓘 creates no tie and no strict-part reversal.
- **Repair to §0 item 2 and the sentence "closure is idle".** For a non-linear base, rules III and IV force nothing *new* only if the base is already closed under I–IV, with P = the selected values. Under that hypothesis the full system is closed: rule I by record-basedness, II by Thm 3.1, III by (a), IV by (b). Without it, the base may need completion and the theorem says nothing. Likewise "the selected models stay undominated, with no ties at any world" (§0 item 2) is proved only for linear bases.

**Prop 3.3: correct with repair.**
- The identity of sections is right. If X = C·d = C′·d′, then C and C′ differ only inside the bounded set supp d ∪ supp d′. Their disagreement set is conic, and a conic set inside an annulus is null (REFEREE_Z_PP19 §2, the fact behind Lemma H). So C = C′ and d = d′, and J_w(X) is F_C or ∅.
- **Repair.** The closedness corollary uses LEAD Lemma A (Φ_C = ∩_w A_w(C)), which needs C *undominated in the full system*. This follows from Prop 3.2(a) if C is undominated in the base. Add that hypothesis. The no-all-world-tie hypothesis is stated.

**Lemma 3.4: correct.** A-holders are never realised at e_k (V_k is B on M_k). B-holders are never realised on the closed edge [e_j, e_l] (PP19 Thm 4(d), first step). This is the same fact as PP29 Lemma 3.3(4).

### 1.3 Theorem 4.1: correct

- A decomposition with x, y ∈ 𝒞_i needs two 𝒮°-realisers, and Cor 2.2 makes them disjoint (and distinct). Pairwise intersection excludes that.
- Vertex obligations are met by guidance, and vertex-only pieces enter only as guidance, which Lemma 4.4 handles.
- The theorem holds for *any* base made of 𝒮°-realised records. In particular it survives any further acceptances forced later, for example by sections, provided the enlarged base keeps its own (TC). This is a real strength.
- **Cross-note remark (PROVED).** Thm 4.1 with an Ω-subset base proves PP29's Conjecture 6.6 for every selection whose non-vertex values pairwise intersect. It does not use σ: A(rec(C, T)) is decided by Ω. The x-records rec(T·d, C) have incoherent old side, so they lie outside 𝒞 and can be accepted only as guidance, which Lemma 4.4 neutralises. Prop 6.1 shows that whole-simplex selections never have this form, so Conjecture 6.6 stays open in general.

### 1.4 The explicit instance (§4.2)

**Geometry: CHECKED exactly** (`pp28_geometry_exact.out`).
- T is silent on ℓ_B, ℓ_A and ℓ_F, and says B on ℓ_G.
- m₀ is a vertex of M and says A on ℓ_B.
- [m₀, p₁] says A on ℓ_A and S on ℓ_F; [m₀, (1/10, 1/10, 4/5)] says A on ℓ_A and B on ℓ_G.
- V₁ says B on ℓ_F; V₂ and V₃ say A on ℓ_B. P2 holds.
- Every decisive margin is ≥ 0.04, so all conditions persist on small neighbourhoods.

**Every defence obligation is met (PROVED).**

| Index | Value | Records r with p ∈ P(r) | Obligation | Met by |
|---|---|---|---|---|
| e_k | V_k | every record out of V_k | k ∈ A(r) | guidance at k: V_k is k-correct everywhere |
| p ∈ M | T | every record out of T, incl. inverted d | A(r) ≠ ∅ | PP23 Thm 3.1(e): Ω_i(r) ≥_lex 0 at some i, and r ∈ 𝒞_i ∪ W_i (realised at an interior index) |
| p ∈ int Δ ∖ M | D_[m₀,p] | every record out of it | A(r) ≠ ∅ | same |

- No other index exists, so no other obligation exists.
- Prop 4.7's x is obligatory (realised at p₁ and nearby) and accepted at world 1 only. Its partner y has no realiser. T, every D_[m₀,p] and V₂, V₃ say A on ℓ_B, and V₁ says B on F. So y is refused everywhere. The same holds for the ℓ_G route.
- All other decompositions have at most one 𝒮°-realised piece (Cor 2.2).

**Bookkeeping slip (repair).** "A(r) = {i : Ω_i(r) ≥_lex 0} for obligatory non-vertex records" is wrong for the inverted departures out of T. They are obligatory (realised by T) and accepted at every world, including the owner, where Ω₁(d) < 0 when d is B-heavy. Correct form: A(r) = {i : Ω_i(r) ≥_lex 0}, plus all three worlds if r is a bounded inverted departure.

**(S) clauses actually verified in §4.2.**

| Clause | Status |
|---|---|
| selected values coherent | yes |
| strict (G), (IB), (TC) | yes (Thm 3.1, Thm 4.1) |
| competitiveness on supp p, every p ∈ I | yes (table above) |
| every selected model undominated; (LA) | yes (Prop 3.2(a), linear base) |
| no single-world ties; hence direct (C) holds vacuously | yes (Ω linear plus Prop 3.2(b)) |
| selection on the whole simplex | **no**: the open edges are missing. By Prop 6.1 they cannot be added while keeping Thm 4.1's hypothesis, and by §6.2 not with an Ω base. |
| closed sections | **not verified by the authors, and they fail** (NUMERICS below). The failure is a jump in the leading level at ∂M, not the lexicographic subtlety the note mentions. |
| consequences of (S): KKM, so every undominated model is coherent | **fails** (PROVED below) |

**Closed sections fail at ∂M (NUMERICS, `pp28_section_numerics.out`).**
- Take p* = midpoint of the edge [m₀, c1 + εe₁] of M. The fixed rival is X := D_[m₀,p*], which is coherent, so A_w(X) is decided by the base alone. Let p_s → p* from outside M, in the direction (−1/2, 1, −1/2).
- Then Ω₂^{(0)}(rec(C_{p_s}, X))/s = 0.83 ± 0.012 (2 s.e.) at s = 0.04, 0.02 and 0.01, so p_s ∈ A₂(X).
- But C_{p*} = T and Ω₂^{(0)}(rec(T, X)) = −0.250 ± 0.0003, so p* ∉ A₂(X).
- The same happens at the midpoint of [m₀, c1 + εe₃].
- The cause is the jump from segments to T on ∂M.
- Similar jumps occur at the vertices: D_[m₀,p] → D_[m₀,e_k] ≠ V_k. That is the boundary layer of Prop 6.1.

**(C) fails (PROVED).**
- Let E ⊆ Ans(T) be bounded, non-null and inside the mixed problems, and put N := T[E → S]. N is regular, and incoherent by Lemma H.
- No certificate reaches N: N's answers are T's answers, so N carries no inverted pattern.
- So every weak all-world dominator X of N acts through W ∪ 𝒞 ⊆ Ω. Then X ≤^Ω_i N at every i.
- PP23 Thm 3.1(e) gives N ≤^Ω_j X at some j. By antisymmetry X = N, so N is undominated.
- This is PP23 Prop 3.2 ("Ω has no room") resurfacing. Only the models N·d gain dominators. The instance is a correct test of the certificate layer, not a step toward a cover.

**Nearby repair of the ∂M jump (PROVED).**
- Fix δ₀ > 0 below the distances from M of p₁ and of (1/10, 1/10, 4/5), and put φ(p) := max(0, 1 − dist(p, M)/δ₀). Off M, replace [m₀, p] by
  K_p := conv({p} ∪ (m₀ + φ(p)(M − m₀))).
- This K_p equals M on ∂M. It equals [m₀, p] once dist(p, M) ≥ δ₀, so p₁ still realises Prop 4.7's x and the adversary test is unchanged. It always contains m₀.
- So the family still pairwise intersects, and Thm 4.1 and the obligation table carry over verbatim (Ω covers every regular model).
- p ↦ K_p is Hausdorff-continuous on int Δ. Hence D_{K_p} is continuous in measure, because the lines that cut one of two Hausdorff-close convex sets but not the other form a set of small measure.
- So p ↦ Ω_w^{(0)}(rec(C_p, X)) = F_w^{(0)}(X) − F_w^{(0)}(C_p) is continuous, and a fixed-rival section can fail to be closed in int Δ only at indices where that leading level vanishes.
- The vertex jumps (D_{K_p} → D_[m₀,e_k] ≠ V_k) remain. They are the genuine open problem (E).

### 1.5 Growth: Theorem 5.1 and Corollary 5.1′

**Thm 5.1: correct.**
- (⇐): the owner-minimal allocation covers every obligation, because some world has Ω ≥ 0 and supports are full. Lexicographic additivity blocks the opponents. At world 1, a pair could collide only if the decomposition is forced.
- (⇒): a forced pair has world 1 as its only Ω-acceptable world. So every allocation puts both pieces there.
- It is a single-d statement, as stated.

**Padding form and Cor 5.1′: correct.**
- I recomputed the bookkeeping.
  - Case (b): Ω_j(x) = α + μ(D₃) + Ω_j(e) and Ω_j(y) = −β − μ(D₃) − Ω_j(e).
  - Case (c): Ω_j(x) = −β − μ(D₃) + Ω_j(e) and Ω_j(y) = α + μ(D₃) − Ω_j(e).
- The density table and the cone analysis are right. The only combinations of the six directions whose positive hull meets the open negative quadrant are those containing (−1, −1), or containing both (−2, 1) and (1, −2). CHECKED by LP over all 63 subsets (`pp28_geometry_exact.out` (4)).
- **Wording.** In case (c) the padding runs C_B → C_A and must land in the positive quadrant. Written as a direction C_A → C_B, that is the *same* condition as in case (b). "Roles swapped" should say so explicitly.

**Prop 5.2: correct with repair.**
- The straddle test, 1A, 2B, 3B and 1B are right. CHECKED exactly against a direct LP feasibility test on 400 random rational pairs: 0 mismatches.
- The stated "2A iff v − u < v′ − u′" and "3A iff v′ − u′ < v − u" are incomplete. They disagree with the exact test on 42 and 85 of the 400 pairs.
  - Correct forms: 2A iff u′ < u or v′ − u′ > v − u; 3A iff v′ < v or v′ − u′ < v − u. These give 0 mismatches.
  - Exact counterexample: k = u, k′ = (41/100, 3/10, 29/100), both in int M. The class-2 line −m₂ + (9/10)m₁ + (1/20)m₃ = 0 puts k strictly in the e₂-corner and k′ strictly outside, so 2A holds. The stated condition is false there.
- The conclusion ("forces in some order iff crossed at e₁") agrees with the exact test on 400/400 pairs. It also holds without the genericity hypothesis: when the pair is crossed, 1A and the straddle are strict.
- **Cor 5.3: correct.** Crossing at e_k means δ_k is the strict median. Non-crossed pairs have a tie among the δ's. A set whose differences all lie in three fixed directions is collinear or a 3-point triangle; I verified the "only common points" step.

### 1.6 Prop 6.1 and adjacent claims

**Prop 6.1: correct.**
- Edge values lie in their face (PP29 Lemma 3.3(2)).
- If all non-vertex values intersect, every non-vertex value on [e₁, e₂] contains e₁ and e₂.
- The fibres Φ_{V₁}, Φ_{V₂}, Φ_E are closed (Lemma A) and pairwise disjoint (Lemma B; ≈ is not transitive in general, but V_k has no tie partner, which is what is used). They cover the connected edge. Contradiction.
- Uses closed sections, competitiveness and strict (G).

**Cross-edge pairs and §6.2: correct.** I recomputed Ω₁ = −m, Ω₂ = −m and Ω₃ = 2m.

**Lemma 6.2 (adjacent; gap).**
- The proof sets X = V_k[Z′ → A] with Z′ ⊆ Z bounded. But rec(C, X) is C → B on (Z ∖ Z′) ∩ {C ≠ B}. That part is a j-loss and can be a non-null cone, so the hypothesis ("trivial on Z ∖ Z′") need not apply.
  - Under a Z-first lexicographic rule with Z = M_k, the leading level can then be positive. Example: any small interior D_K, whose A and S lines outside Z′ outweigh a small Z′.
- **Repair.**
  - For bounded (more generally non-conic) Z, take X := V_k[Z → A]. Then the record restricted to Z is C → A on Z ∩ {C ≠ A}, and the argument runs.
  - For Z = M_k, use PP26 Thm V (V-maj) directly, with the full fill.
  - For conic Z ⊊ M_k, X may be coherent, and nothing follows.
- The section's conclusion (region-first rules are excluded) stands, via PP26.

---

## 2. PP29 (forced realisation)

### 2.1 Theorem 4.1 (retreat split): correct, including vertex and edge obligations

- **Lemma 3.3 is the key, and it is right.**
  - C_{e_i} = V_i.
  - An open-edge value is A a.e. on the third class, by strict (G) against C_p[E → A] at both edge worlds. Its K lies in the face, because lines with g_{i″} ≪ 0 defeat any m with m_{i″} > 0.
- **Obligations by face, for a piece r of d⁻¹:**

| Realising face | A-marked: σ = G ∪ {j, l} | B-marked: σ = G ∪ {k} |
|---|---|---|
| e_k (V_k) | impossible (V_k is B on D^A) | k ✓ |
| e_j, e_l | j or l ✓ | impossible (V_j, V_l are A on M_k) |
| edge [e_k, e_j] / [e_k, e_l] | j / l ✓ | k ✓ |
| edge [e_j, e_l] | ✓ | impossible (A on M_k) |
| interior | ✓ | ✓ |

  For a realisable unmarked piece, H = {1, 2, 3} ∖ I(r) works whenever the selection is competitive, so "whenever satisfiable" is automatic under the theorem's own hypotheses.

- **Property 3: checked case by case.**
  - Both pieces realisable: G(A-marked) ∌ k and G(B-marked) ∌ j, l, since otherwise the partner's old side contains X. This holds in both role assignments (x A-marked or y A-marked).
  - One piece unrealisable: each of the four sub-cases forces the realisable piece to carry both marks, or its partner to carry X. I verified each.
  - Unmarked realisable piece: the partner's G is empty.
  - Neither realisable: G(x) ∩ G(y) = ∅, because d⁻¹ is kind M at every world.
- **CHECKED independently** (`pp29_sigma_cells.out`; my own record algebra, and exact realisability by LP vertex enumeration on every face).
  - Six configurations: owner k = 1 or k = 3; steep, both-steep, radial, padding in another class, a T-answering line, two departures.
  - 474,384 decompositions over all contexts P and intermediates Q with values in {A, S, B, X}.
  - 11,104 with both pieces realisable.
  - 0 failures of properties 1–3 under maximal face obligations; 0 realisable doubly-marked pieces.
  - The authors' `single_d_check.py` also reproduces.
- **What Thm 4.1 does not cover** (the note says so in §6): triangles not through d, and closed sections. Prop 6.3 shows sections already constrain σ.

### 2.2 Theorem 5.1: correct

- (b) and the obligation lemma make A(x), A(y) nonempty; (a) makes both equal {k}; (c) and Lemma 2.1 then give the violation.
- The hypotheses "B-heavy, P1–P3" are not used. They matter only for making (a) hold under Ω, as the note says. The diagnosis that (a), additivity at the opponents, does the work is correct and agrees with PP28 Thm 5.1 and §6.3.

### 2.3 Proposition 5.2: correct

- The two closed sections cover the edge, so they meet.
- Vertices are excluded because P is strictly j-better than V_k: on M_k, V_k says B, the worst regular value at j; on M_j, V_k says A, which is wrong at j; on M_l the two agree.
- Comparable intervals give a strict pointwise order at one world, because crossings fill (0, 1).
- The trichotomy is exhaustive (I listed all nine sign cases).
- Prop 3.4 and Cor 5.3 follow, using steepness P2 and inversion (z(B-lines) ≤ z(A-lines) in both coordinates).

### 2.4 Propositions 6.2 and 6.4: correct

- **6.2.**
  - y_C = rec(C, T) is a piece of d⁻¹ with Q = C.
  - It is B-marked for d (D^B ⊆ L₁) and A-marked for d′ (D′^A ⊆ L₂). It cannot carry both marks for one departure (Lemma 1.1).
  - G(y_C) = ∅.
  - So mark-restricted σ refuses it at every world.
  - The room for D^A above L₁ and D′^B below L₂ exists because the T-silent lines form an open set.
- **6.4.** It is a restatement of Lemma 2.1 with Q = C plus competitiveness. "T selected" is not needed: only A(d) = {1, 2, 3}, A(d⁻¹) = ∅ and C selected are used.

### 2.5 Classification of escapes: three rows overclaim

| Row | Verdict |
|---|---|
| "Collision of one padding pair never follows: not from the axioms, the selection or the geometry" | **Overclaim.** PROVED: supports, guidance, vertex and edge structure never force it. Closed sections and triangles not through d are not examined (Prop 6.3 shows sections bite). Same correction for §0's "closed sections and KKM never force…". |
| d⁻¹ refused everywhere ← optional comparisons | correct as a *sufficient* source. Lemma 2.2 shows the axioms force at least one refusing world. |
| Prop 4.7's owner collision ← Ω-additive opponents plus realisation | correct |
| y realised on [e_k, e_j] ← axioms unless straddle | correct |
| "x realised: selection choice only … never force it" | **Overclaim**: "no known argument forces it". Prop 5.2 on [e_k, e_l] with [s, t] = [inf_F z_kl, sup_F z_kl] forces an edge model that realises x, lies strictly inside, or straddles. Whether x itself can always be avoided is OPEN. |
| Opponent non-additivity | correct (Prop 6.1). The general-field version needs one padding F satisfying both opponents' intervals at once. That is an unstated joint-capacity condition. |
| "σ fails globally: the rule σ, not the axioms" | first half PROVED. "Not the axioms" is CHECKED on cells only. In the continuum it is proved only for intersecting partial families (my §1.3 remark). |
| J_d ← σ | correct |

---

## 3. PP30 (surgery on S_0)

**Prop 2.1: correct.**
- Strict weighted minimisation gives an i with L_i(D_{p₀}) < L_i(T).
- X = Y^i_E is squeezed between them.
- Dominated convergence gives D_p ⪯_i X near p₀, and the closed section transfers this to T.
- The continuity used is that of p ↦ L_i(D_p), a property of S_0's selection, not an assumption on general selections.

**Lemma 2.2: correct.**
- Each L_w(C_p) ≤ L_w(D_p): otherwise a small fill gives a strict w-improvement X of C_p that the sections force C_p to accept.
- Uniqueness of the p-weighted minimiser holds a.e. for every p in the closed simplex, unanimous problems included.

**Thm 3.1: correct.**
- The three record identities are right; I recomputed the supports.
- (a) is T's competitiveness against X_{p,G}. (b) is (TC) on T ⪯ X ⪯ Y ≺ T.
- Single-world ties are allowed throughout. The only real hypothesis is T competitive, i.e. T selected (Lemma E).

**Thm 3.2: correct; the explicit G CHECKED exactly** (`pp30_kill_balls_exact.out`).
- With genuine balls instead of atoms: on the 1/12-grid and ε ∈ {1/10, 3/10, 1/2, 9/10} (364 cases), all of the following hold exactly:
  - g_p ⊥ 1 and g_p ⊥ p;
  - h± is strictly T-silent, with margins lo±, hi± > 0;
  - p·h± = t;
  - a radius r = min(lo±, hi±, t/2)/2 > 0 keeps the ball inside Sil(T) ∩ {p·x > 0} (|m|₂ ≤ 1 on Δ);
  - the balls are disjoint modulo sign;
  - the lower bound v_w ≥ μ(B)·2(t − r) > 0.
- A simplification: |h+| = |h−| exactly (g_p ⊥ 1), so equal radii already give equal Gaussian mass.
- The authors' atom check and Monte Carlo reproduce.

**Prop 3.4: correct.**
- The Lyapunov range over bounded G ⊆ R is convex (an increasing union of convex sets), and separation from the open orthant gives λ ∈ Δ.
- The second proof for S_0 is right. Two linear forms with non-positive product on a plane share a nonzero zero g₀, and g₀ + t1 ∈ Sil(T) gives the product t² > 0.

**Remark 3.6: correct.**
- For K with interior, the construction works with any interior k, since g = k × p is never parallel to 1.
- For segments:
  - off the line ab, δ·g ≠ 0;
  - in the open segment, take k = p (simpler than Prop 3.4);
  - beyond an endpoint, λ = the far endpoint certifies (λ·g)(p·g) < 0 on Sil(D_[a,b]). PROVED, and CHECKED on 5,257 rational samples.

**Prop 4.2: correct.**
- Z is bounded, non-null and different from D_p, hence incoherent (Lemma H).
- KKM plus direct (C) give a strict dominator C ≠ D_p.
- {C ≠ Z} contains the cone {C ≠ D_p} outside G, so it is unbounded.
- A_w(Z) is closed and misses q*.
- Implicit hypothesis: T selected, so that w(p, G) exists.

**Thm 5.1: correct.**
- On Sil(T), kept links do nothing and guidance only worsens, so X ∈ {S, w-correct} for each w, hence X = S.
- The strict link's strictness must then lie in Ans(T). This step is not written out but holds: on Sil(T), Yⁿ ≥_w X = S and Yⁿ ≤_w T = S.
- So L_w(X) < L_w(T) at every w, with X − T supported in Ans(T). This contradicts T's unique m-Bayes property there.
- Chains longer than a triangle are not (TC) refutations without transitivity, so the theorem excludes more than it needs to.

**Thm 5.2, Lemma 5.3, Cor 5.4, Prop 5.5: correct.**
- Aumann/Lyapunov convexity, separation by λ supported on supp q, and pointwise uniqueness off λ^⊥.
- Lemma 5.3: the separating-line arguments are right in both directions, including λ ∈ ∂M.
- Prop 5.5: the transversal line through x ∈ (λ, λ′) and m ∈ int M lies in Sil(T).

---

## 4. Hidden-assumption audit

| Assumption | Where it might hide | Finding |
|---|---|---|
| Transitivity | PP28 Thm 3.1/5.1; PP30 Thm 5.1 | Not assumed. Ω and S_0 are transitive by construction. PP28 Thm 5.1 uses Ω's lexicographic additivity, a property of the chosen base. |
| No single-world ties | PP28 Prop 3.2(a), 3.3; PP29; PP30 Thm 3.1 | PP28 Prop 3.3 assumes no *all-world* ties among selected models (stated) and needs undominatedness (unstated; §1.2). Prop 3.2(a)'s strong form uses antisymmetry of a linear base (a property). PP29 and PP30 allow ties. |
| Continuity of the selection | PP30 Prop 2.1, Lemma 2.2; PP29 Prop 6.3 | Only continuity of p ↦ L(D_p), a property of S_0's selection. PP29 notes that continuity in measure implies J_d and does not assume it. Nowhere else. |
| Strict repairs everywhere | PP28 Prop 3.2(d); PP29 A(d⁻¹) = ∅ | Proved where claimed. PP29 imposes A(d⁻¹) = ∅ as the hard case and shows it is optional (Lemma 2.3). PP30 Prop 4.2 needs strictness at one world only. |
| Universal coverage | PP28 §5; PP29 cells | Removed. PP29's "maximal obligations" over-approximate any selection, so SAT transfers. Correct use. |
| T selected | PP30 Thm 3.1, Cor 3.3, Prop 4.2; PP29 Prop 6.4 | A real hypothesis of PP30 §§3–4 (stated in 3.1, implicit in 4.2). Not needed in PP29 Prop 6.4. |
| Base closed under I–IV | PP28 §0 item 2 | **Hidden**; needed for "closure forces nothing" over non-linear bases. |
| Joint padding capacity | PP29 Prop 6.1 (general field) | **Hidden**; one F must serve both opponents. |

---

## 5. Scripts

**Mine (`r9/PP31_py/`).**

| Script | Content | Label |
|---|---|---|
| `pp28_geometry_exact.py` | §4.2 geometry; e₁-below criterion; Prop 5.2 types against an exact LP test (400 pairs); 2A/3A counterexample | CHECKED |
| `pp28_section_numerics.py` | failure of closed sections in §4.2 at ∂M (4·10⁶ Gaussian samples, s.e. printed) | NUMERICS |
| `pp29_sigma_cells.py` | independent implementation of PP29 Thm 4.1: exact face realisability, 474,384 decompositions, 6 configurations, ALL PASS | CHECKED |
| `pp30_kill_balls_exact.py` | Thm 3.2 with genuine balls (exact radius bound, 364 cases); Remark 3.6 segment escape | CHECKED |

**Re-runs of the authors' scripts** (`rerun_*.txt`).
- PP28: `cells28`, `forced_list` and `polarity_witness` are identical.
- PP28 `separation_check`: the numbers are identical. Stdout also carries `cells28`'s report, because `cells28.py` has no `__main__` guard; this is cosmetic.
- PP29: `single_d_check` is identical. `forced_sat` C0 sel, C0 sel nostrict, C0 omega and C1 omega are identical up to timings.
- PP29 `forced_sat` C1noF omega: the headline (SAT) is identical; the stored file predates the script's extra diagnostics.
- PP29 `forced_sat` C5 sel is identical up to timings. C2 sel is identical in substance (SAT; σ UNSAT with 48 double-labelled records); one diagnostic line was relabelled in the script after the stored run.
- PP30: all four scripts are identical.

---

## 6. What the round establishes, and nearby targets

**Firm.**
- The certificate layer never causes trouble by itself. It is exact, section-neutral and closure-neutral over any (TC) base made of selected-realised records (PP28 Thm 3.1, Props 3.2–3.3, with the repairs above).
- For intersecting families it admits every bounded inverted departure (Thm 4.1).
- Supports alone never force a padding collision (PP29 Thm 4.1, PP28 Lemma 3.4: the same fact).
- Prop 4.7's obstruction comes from additivity at the opponents (PP28 Thm 5.1, PP29 Thm 5.1).
- (S) forces separated non-vertex pairs (PP28 Prop 6.1).
- In PP30, every precise model must imitate T on pieces of T's silence at some world (Thm 3.1), and S_0 contradicts this at every index (Thm 3.2).

**What is not established.**
- No partial family yet satisfies closed sections. §4.2 fails them at ∂M and at the vertices, and leaves undominated incoherent models.
- PP29's escape is a single-departure, support-level statement.

**Nearby targets** (proposals, not results).
1. **Remove the ∂M jump at no cost.** Use the interpolated segments K_p of §1.4. Then the only section failures in the interior are at zeros of the leading Ω-level, and the remaining failures sit at the vertices. That isolates (E) to the boundary layer, which is where PP28 §6.4 and PP30 Cor 5.4 both point.
2. **Combine PP28 Prop 6.1 with PP29 Thm 4.1 on one edge neighbourhood.** Cross-edge separated pairs have type 1A (PP28 §6). PP29's σ handles their pieces at the support level. The concrete question is whether a non-additive opponent rule (forced by PP29 Prop 6.1) can carry σ's verdicts for cross-edge pairs while keeping (TC) on triangles not through d. A cell SAT with edge models on [e₁,e₂] and [e₁,e₃], plus a steep padding line, would test this before any continuum work.
3. **Fix the two statements that are now wrong.** PP28 Prop 5.2's 2A/3A conditions, and the three rows of PP29's classification table.
