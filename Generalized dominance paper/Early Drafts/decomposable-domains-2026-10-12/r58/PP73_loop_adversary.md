# PP73. Adversary on the exact rescaling loop: two edges and a splice, two branches, Theorems Q and E

24 October 2026. Adversary, Brief 58. One author; not refereed. Section 5 attacks PP72 as posted in its DRAFT section (D1)–(D4); later PP72 sections were not available when this note was finished.

**Labels.**
- PROVED: complete argument here, or a cited result used inside its stated hypotheses.
- CHECKED: exact computation. (None used in this draft.)
- NUMERICS: Monte Carlo on a standard Gaussian sample, in `r9/PP73_py/`. Used only as illustration or where marked.
- CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF58; AUDIT_round58 and its answers (binding); DESIGN_MEMO §8.25–§8.26 with their correction bullets; PP57 §4 (Lemma 4.1, Theorem Q); PP62 (Lemma 1.1, Cor 1.2, Lemma 1.3, Theorem E, Lemma S, Cor E.2); PP56 §4 (u¹, (2V), Λ, Theorem L); PP63 (Lemma 3.1, Lemma 4.1, Prop 4.2); PP68 Lemma 1.2; PP71 Prop 2.6; BRIEF54 encodings. No axiom is added. Hypotheses that are properties of a *design* (not of the axioms) are named where used and kept out of every axiom-level claim.

**Conventions.** X ⪯_w Y means "X is at least as good as Y at world w". Records are rec(X → Y) = (support : old values → new values). Acc(r) and Ref(r) are the sets of worlds accepting and refusing r. "Member" means an installed coherent posterior model C_a; T = C_u. For the loop at scale a > 1 put b := a⁻³ ∈ (0, 1) and

  P₀ := T = C_u, P₁ := C_{m₁}, m₁ ∝ (1, 1, b), P₂ := C_{m₂}, m₂ ∝ (b, 1, b),

which are the brief's m₁ ∝ d₃ and m₂ ∝ d₁d₃. Layers: L_{ij} := {P_i ≠ P_j}. For a layer L and odd world o, L^{(o)} is its odd-world-o part. A is the majority answer, B the minority answer.

---

## 0. Verdict

1. **One exact loop is a guidance triangle, and it contains no balanced swap for any field (§1; PROVED).** Each pair of P₀, P₁, P₂ differs by a single-coordinate likelihood shift, so each pair is strictly guidance-ordered at one world (P₀ ≻₃ P₁, P₁ ≻₁ P₂, P₂ ≻₂ P₀). Consequently no strictly guiding additive field (u¹ or any other) has a null non-conic swap between two members of one loop. Theorems Q and E have nothing to bite on *inside one loop*. The brief's warning that "the loop members have member-to-member balanced swaps" is true only across different scales (§4.1).

2. **Task 1. The two-edges-plus-splice obligations are consistent at the source level, and the splice clauses are uniformly satisfiable; but in one exact loop each repair edge fails on an explicit non-null family of fills, which are exactly splices with the third member (§2; PROVED).**
   - *Fill–splice identity (Thm 2.3).* For the edge P_i →(k) P_{i+1} with predecessor P_{i−1}, let S_k := Sil(P_i) ∩ M_k ∩ {P_i ≠ P_{i−1}}. On S_k, P_{i−1} = A and P_{i+1} = A. So a class-k fill of P_i on E ⊆ S_k is the splice P_i[E ↦ P_{i−1}], and the designated repairer agrees with it on all of E.
   - *Agreement obstruction* (audit, re-proved as Lemma 2.4): P_{i+1} cannot dominate it. So the *fixed successor* fails on the loop's own splices, at every scale a > 1. The obstruction concerns a choice (the fixed successor), not the axioms.
   - Every repairer of such a splice-fill must refuse P_i at the two other worlds (forced pattern) and must differ from A on part of E. Among rescaling repairers on the same ray, splice-fills concentrated near one face force the repair scale to 1 (Prop 3.5).
   - All splice clauses between consecutive members (defence, protection, (TC) with signed propagation) are satisfied uniformly in the splice set by PP56's Λ (Prop 2.2). Λ also strictly dominates every fill that has a non-null "−h part", by a ray member at a scale window (Prop 2.5).
   - **No axiom-level conflict found.** What Λ cannot supply is exactly the domination of *u¹-null type* rivals: pure-h fills and member–member splices (Prop 2.5(c)). These need a departure from u¹ in the place Theorems Q and E constrain (§4). Consistency of the full configuration **with closed sections**, for all measurable fills: **OPEN** at my end. It is the constructor's problem, and I could not reduce it to a contradiction.

3. **Task 2. A fixed rival approached along two branches forces no failure by itself (§3; PROVED).** The exact limit statement is the germ lemma (PP63 Lemma 4.1(c)): branch-forced acceptance worlds must lie in Acc at the limit. The forced acceptances available are the four kinds of PP63 §4.1. Checking each against the loop gives three *design constraints*, all PROVED, none axiom-level contradictions:
   - (Prop 3.2) **two-branch exclusion:** a repairer used for class-k fills of C_s cannot also be used for class-j fills (j ≠ k) of sources accumulating at s;
   - (Prop 3.3) **endpoints repel:** the dominators of a fixed fill or of a fixed splice cannot accumulate at the source or at either splice end;
   - (Prop 3.4) **tie transfer:** if two branches of dominators of one fixed incoherent X converge to s, and their dominations are *tight* on complementary sets of worlds, with the matching member comparisons accepted, then X is all-world tied with C_s. This is a direct-(C) failure. It is the precise form of the audit's "incoherent all-world tie at the limit", and it is avoidable.
   - For the loop's own rays the three branches of a member meet only at that member, so Prop 3.2 is never triggered by rescaling repairs.

4. **Task 3. Theorems Q and E (§4).**
   - **Balanced swaps across scales exist (Prop 4.1; PROVED under (2V)).** Examples: m₁(a) versus m₂(a′) for a′ ≠ a, and u versus m₁(a′)∘d₁(a″) for a′ ≠ a″.
   - **Splices force a second scale** (by §2, for in-family repairs). So any non-isolated loop family that repairs its own splices in-family contains balanced member pairs.
   - **Theorem Q applies (Prop 4.3; PROVED).** Any rule satisfying (L0⁺) for u¹, with closed sections on a family containing an interval of the m₁-ray and one m₂(a′), fails direct (C). This includes Λ, every tie-breaking of Λ, and R₀. The m₁-ray alone supplies the three section directions needed: inward for world 3, outward for worlds 1 and 2.
   - **Theorem E applies only where the family contains a direction in O_w for the refusing world w (Thm 4.4, Table 4.5).** On the two-ray star each member has exactly one such direction, and an endorsed allocation survives there (Prop 4.6, explicit). On a family whose members are approached from three O-directions (for example a 2-D closure), every u¹-endorsed rule fails.
   - **Do the loop's commitments force (L0⁺) or endorsement? No (Prop 4.2).** The loop's forced refusals are all u¹-unfavourable (V < 0 at every forced-refused world), so they never refute (L0⁺). Fill dominations are u¹-endorsable exactly at the *mass-balanced* scale for pure-h fills: p(a) = e, a knife-edge with a u¹-null domination record. For fills with a −h part they are endorsable on the window e + f ≤ p ≤ e + 2f. So neither envelope is forced, and neither is excluded by the commitments alone. They are excluded by Theorem Q (lower envelope; always on two scales) and by Theorem E (upper envelope; given enough directions).

5. **Task 4 (PP72's posted draft, §5).**
   - **No axiom-level conflict.** The repair rule avoids the agreement obstruction. The forced refusals are never derived by its u¹-argmax defence 𝒟₀ or by section limits, and the two-branch traps are not triggered.
   - **Decisive weak point (PROVED).** By the (1 2) and (1 3) symmetries, 𝒟₀ is an *exact tie* along R₃-outward (worlds 1, 2) and along R₂-inward (worlds 1, 3), for every rival that is null against the member.
     - So the balanced-swap test (Theorem Q(ii), F2) is decided entirely by PP72's tie rule. It passes iff the tie rule satisfies (ρ1)–(ρ3) of §5.2.
     - Any tie rule that alternates along a ray fails.
   - **Coordinator relay.** At u, the m₂-ray is Theorem Q's world-2 sequence and the m₁-ray supplies worlds 1 and 2. Theorem Q's hypotheses therefore hold at u except for the single null verdict T ⪯₃ X. Dually, Theorem E forbids any endorsed rule from refusing a balanced rival at world 2 at u (Prop 4.8).
   - **Still owed by PP72:** dominators for all measurable splices between installed models (its 2-D defender set included), and its (TC) closure with non-endorsed domination records (§5.3–5.4).

| Item | Result | Label |
|---|---|---|
| Posterior = pullback; group action | Lemma 1.1 | PROVED |
| Single-coordinate shift: guidance at the shifted world; odd-world effects | Lemma 1.2 | PROVED |
| One loop is a guidance triangle; no ψ-balanced swap inside one loop | Cor 1.3 | PROVED |
| u¹ ledger of the loop: refused worlds have V < 0 | Lemma 1.4 | PROVED at u; NUMERICS elsewhere |
| Forced literals of two edges + splice; splice clauses | Prop 2.1, 2.2 | PROVED |
| Fill–splice identity; fixed successor fails on S_k | Thm 2.3 | PROVED |
| Agreement obstruction | Lemma 2.4 | PROVED |
| Λ dominates fills with a −h part; never pure-h fills or member splices | Prop 2.5 | PROVED |
| Germ lemma; two-branch exclusion; endpoints repel; tie transfer | Lemma 3.1, Props 3.2–3.4 | PROVED |
| In-family scale accumulation at the source | Prop 3.5 | PROVED |
| Balanced swaps across scales | Prop 4.1 | PROVED under (2V); NUMERICS illustration |
| u¹ accounting of fill dominations | Prop 4.2 | PROVED |
| Theorem Q on the two-ray star | Prop 4.3 | PROVED (balanced swap by Prop 4.1) |
| Theorem E with family directions; applicability | Thm 4.4, Table 4.5, Prop 4.6 | PROVED; (H_Γ) at members NUMERICS |
| Consistency of two edges + splice with closed sections, all measurable fills | — | OPEN |

---

## 1. One loop

**Lemma 1.1 (PROVED).** C_a(g) = T(a∘g). Hence C_{a∘c}(g) = C_a(c∘g). Since a∘g has the sign pattern of g, correctness at each world is unchanged by the substitution.

*Proof.* M_a = {a∘p/(a·p) : p ∈ M}, and σ(a∘p)·g/(a·p) > 0 iff σ p·(a∘g) > 0, because a·p > 0. ∎

**Lemma 1.2 (single-coordinate shifts; PROVED, no (2V) needed).** Let b = a∘(1, …, s at coordinate j, …, 1) with s ∈ (0, 1). Write q_v(a; g) := Σ_i a_i v_i g_i for the three vertices v of M. Then:
- (a) C_b is pointwise weakly j-worse than C_a, and strictly worse on a non-null open cone.
- (b) At an odd-k point with k ≠ j: C_b answers A ⇒ C_a answers A, and C_a answers B ⇒ C_b answers B. So C_b weakly *improves* world k there.
- (c) At an odd-j point, C_b weakly worsens world j (by (a)).

For s > 1 every statement holds with the roles of a and b exchanged.

*Proof.* q_v(b) = q_v(a) − (1 − s) a_j v_j g_j.
- Let τ := sign g_j, the j-correct answer. Then τq_v(b) < τq_v(a) and −τq_v(b) > −τq_v(a). So τ-answers can only be lost, and (−τ)-answers can only be gained. Each such change weakly raises the j-rank.
- The boundary planes {q_v(a) = 0} and {q_v(b) = 0} differ for the binding vertex, so the change set contains an open cone. This gives (a).
- At an odd-k point with k ≠ j, g_j has the majority sign, so τ = A. That gives (b), and (c) is (a). ∎

PP57 Lemma 4.1 is the case s > 1 of (a). PP62 Lemma 1.1 is the (2V) version of (b) and (c).

**Corollary 1.3 (one loop is a guidance triangle; PROVED).**
- m₁ = m₀∘(3 : b), m₂ = m₁∘(1 : b) and m₀ ∝ m₂∘(2 : b). So P₁ is strictly 3-worse than P₀, P₂ is strictly 1-worse than P₁, and P₀ is strictly 2-worse than P₂. By strict (G):

  P₀ ⪯₃ P₁, P₁ ⋠₃ P₀;  P₁ ⪯₁ P₂, P₂ ⋠₁ P₁;  P₂ ⪯₂ P₀, P₀ ⋠₂ P₂.

- For every strictly guiding additive field ψ and every non-null F ⊆ L_{ij}, the ψ-increment of (F : P_i → P_j) has a fixed nonzero sign at the shifted world. So **no pair inside one loop has a ψ-balanced swap**, for any ψ.
- The reverse orientation P₀ → P₂ → P₁ → P₀ contains a strict guidance refusal at every world: P₂ ⪯₁ P₁, P₀ ⪯₂ P₂ and P₁ ⪯₃ P₀. So it never yields a (TC) clause.
- Once edges e1 and e2 of §2 are installed, the forward orientation P₀ → P₁ → P₂ → P₀ is also blocked at every world, by the forced refusals of Prop 2.1(a): P₀ ⋠₁ P₁, P₀ ⋠₂ P₁ and P₁ ⋠₃ P₂. So the source triangle then contributes no clause.

*Proof.* The first two items follow from Lemma 1.2. The last two are read off the displayed refusals. ∎

**Lemma 1.4 (u¹ ledger; PROVED at u, NUMERICS along the loop).** Put V(r) := Φ(new) − Φ(old) for u¹ (PP62 §1.1; positive V_w means the old side is u¹-better at w).
- (a) By the 1↔2 symmetry fixing u and m₁: V(P₀ → P₁) = (−p, −p, 2p), with p = p(a) := α + β > 0, where α and β are the |g|-masses of the odd-3 and the odd-1 parts of L₀₁.
- (b) NUMERICS (`loop73.out`; a ∈ {1.01, 1.03, 1.1, 1.17}): V(P₁ → P₂) and V(P₂ → P₀) are positive exactly at the guidance world and negative at the other two. Examples: (0.171, −0.094, −0.078) and (−0.088, 0.176, −0.088) at a = 1.1. The three increments sum to 0.
- (c) (2V) holds along the loop for a ≤ (16/7)^{1/3} ≈ 1.317 at m₁, and for a ≤ (23/14)^{1/3} ≈ 1.18 at m₂ (from normalise(1/m) ≥ c). It is CHECKED on samples for a ≤ 1.17: zero −h answers.

*Proof of (a).* Lemma 1.2 with j = 3. Odd-3 layer points worsen world 3, contributing −ε₃|g| = (−1, −1, 2)|g| (PP62 (1.1)). Odd-1 and odd-2 points improve their own odd world, contributing ε₁|g| and ε₂|g|. The symmetry gives equal odd-1 and odd-2 masses β. So V = α(−1, −1, 2) + β(−2, 1, 1) + β(1, −2, 1). ∎

So the source-level pattern of the loop is **exactly u¹-consistent**. Every forced refusal is at a u¹-unfavourable world, and every guidance acceptance is at the favourable one. This is the measurable form of the audit's toy vectors.

---

## 2. Task 1: two adjacent repair edges and one splice

Fix a > 1 in the (2V) range. The configuration is:
- **e1:** P₁ dominates X_E := P₀[E ↦ A], with E ⊆ Sil(P₀) ∩ M₃ non-null and non-conic;
- **e2:** P₂ dominates Y_F := P₁[F ↦ A], with F ⊆ Sil(P₁) ∩ M₁ non-null and non-conic;
- **one splice**, either Z_H := P₁[H ↦ P₂] (H ⊆ L₁₂) or Z⁰_K := P₀[K ↦ P₁] (K ⊆ L₀₁), each non-conic with a non-null complement in its layer.

Domination means acceptance at all three worlds of r₁ := rec(P₁ → X_E) and r₂ := rec(P₂ → Y_F), with Ref(r₁⁻¹) ≠ ∅ and Ref(r₂⁻¹) ≠ ∅. The latter is protection, since X_E and Y_F are incoherent.

**Prop 2.1 (forced literals of the two edges; PROVED).**
- (a) e1 forces P₀ ⋠₁ P₁ and P₀ ⋠₂ P₁; P₀ ⪯₃ P₁ is guidance. e2 forces P₁ ⋠₂ P₂ and P₁ ⋠₃ P₂; P₁ ⪯₁ P₂ is guidance. If the third edge is installed (P₀ dominates a class-2 fill of P₂), it forces P₂ ⋠₁ P₀ and P₂ ⋠₃ P₀.
- (b) Remaining member defences: P₁ against P₀ at 1 or 2; P₂ against P₁ at 2 or 3; P₀ against P₂ at 1 or 3. These are disjunctive. Each world in them is open; no member–member clause forces a choice (Cor 1.3).
- (c) Records compose: r₁ = (L₀₁∖E_in : P₁ → P₀) ⊕ (G : S → A), where E_in := E ∩ L₀₁ (on which P₁ = A) and G := E ∖ L₀₁.
- (d) **A repair followed by a defence.** On F ⊆ Sil(P₁) ∩ M₁, let F_r := F ∩ L₀₁. There P₀ = A, since by Lemma 1.2(b) P₁ only loses A relative to P₀ on odd-1 points. So Y_F restores P₀ on F_r.
  - If F = F_r, then Y_F = P₀[L₀₁ ∖ F ↦ P₁], and r₁ = (F : P₁ → P₀) ⊕ rec(Y_F → X_E).
  - The triangle (P₁, X_E, Y_F) at w ∈ {2, 3}: P₁ ⪯_w X_E (r₁) and Y_F ⪯_w P₁ (guidance: Y_F is 2- and 3-better). Strict guidance refuses P₁ ⪯_w Y_F.
  - Hence **X_E ⋠₂ Y_F and X_E ⋠₃ Y_F**, for every such E and F. At world 1: ¬[Y_F ⪯₁ X_E] ∨ ¬[X_E ⪯₁ P₁].

*Proof.*
- (a) is the forced pattern (audit): X_E ⪯_i P₀ is guidance for i ≠ 3, and (TC) on P₀ → P₁ → X_E → P₀ with strict (G) does the rest. Likewise for e2 and the third edge.
- (b) uses strict (G) from Cor 1.3.
- (c) and (d) are direct computations of supports. In (d), the second triangle would force the reverse P₁ ⪯_w Y_F, which strict (G) refuses. ∎

These are *refusals between incoherent models*. By PP63 Lemma 3.1 they cost nothing except defence slack, and no member is an old side of these records. They propagate no further.

**Prop 2.2 (the splice clauses, uniformly in H; PROVED).** For K ⊆ L₁₂ write α_w(K) := [(K : P₁ → P₂) ∈ Acc_w] and γ_w(K) := [(K : P₂ → P₁) ∈ Acc_w].
- (a) Guidance: P₁ ⪯₁ Z_H ⪯₁ P₂, with both reverses strictly refused.
  - α_w(K) = 1 is forced when K ⊆ L₁₂^{(3)} (w = 2) or K ⊆ L₁₂^{(2)} (w = 3).
  - α₂(K) = α₃(K) = 0 is forced when K ⊆ L₁₂^{(1)}.
- (b) Defence of P₁ against Z_H holds at world 1. Defence of P₂ against Z_H is γ₂(L∖H) ∨ γ₃(L∖H). Protection of P₂ against Z_H is ¬α₂(L∖H) ∨ ¬α₃(L∖H). Protection of P₁ holds at world 1.
- (c) (TC), signed: for w ∈ {2, 3}, γ_w(L₁₂) ⇒ ¬α_w(H) ∨ ¬α_w(L₁₂∖H). With w* the world defending P₂ against P₁, *every bipartition of L₁₂ has a half refused at w**.
- (d) **All of (a)–(c), for all H at once, hold in Λ** (and in the u¹ weak order). On an H-record the three increments sum to 0, and V₁(K : P₁ → P₂) > 0. So V₂ and V₃ are never both ≥ 0, which gives protection. For the same reason −V₂ and −V₃ are never both < 0, which gives defence. And V_w(H) + V_w(L∖H) = V_w(L₁₂) < 0 for w ∈ {2, 3} (Lemma 1.4), which gives (c).
- The same holds for the T/P₁ splices Z⁰_K (worlds 1, 2 in place of 2, 3).

*Proof.* The clauses are read off the triangles P₁ → Z_H → P₂ → P₁ and its reverse. One link of the reverse is refused by e2. (d) is PP56 Theorem L restricted to these records, together with the displayed sign facts. ∎

**Theorem 2.3 (fill–splice identity in one exact loop; PROVED).** Index the edges as P₀ →(3) P₁ →(1) P₂ →(2) P₀ (so k₀ = 3, k₁ = 1, k₂ = 2), with indices mod 3. For each i let

  S_i := Sil(P_i) ∩ M_{k_i} ∩ {P_i ≠ P_{i−1}}.

Then:
- (a) P_{i−1} = A a.e. on S_i;
- (b) P_{i+1} = A a.e. on S_i;
- (c) S_i is non-null for every a > 1.

Consequently, for E ⊆ S_i the class-k_i fill P_i[E ↦ A] **is the splice** P_i[E ↦ P_{i−1}], and the designated repairer P_{i+1} agrees with it on all of E.

*Proof.*
- m_{i−1} = m_i∘(k_{i−1} : 1/b). This raises a world that is not the odd world of S_i. By Lemma 1.2(b) with s > 1, P_{i−1} only gains A and loses B relative to P_i on odd-k_i points. Where P_i is silent, P_{i−1} ≠ P_i forces P_{i−1} = A. This is (a).
- m_{i+1} = m_i∘(k_i : b) = m_{i−1}∘(k_{i−1} : b)(k_i : b) ∝ m_{i−1}∘(k_{i+1} : 1/b). Again this raises a non-odd world, so P_{i−1} = A ⇒ P_{i+1} = A. This is (b).
- (c): P_{i−1}'s A-boundary on M_{k_i} moves (Lemma 1.2(a) applied to that boundary), so the gained set is a non-null open cone.

NUMERICS (`splice73.out`): at a ∈ {1.01, 1.05, 1.17}, (a) and (b) hold at 100% of the S_i sample points for all three edges. |S_i| is 1.2%–20% of Sil ∩ M_k. ∎

**Lemma 2.4 (agreement obstruction; PROVED).** Let C be a protected selected model. Let B be coherent, with B = A a.e. on a non-null non-conic E ⊆ Sil(C). Then B ⪯_w C[E ↦ A] for all three w is impossible.

*Proof.*
- The record rec(B → C[E ↦ A]) is (L_{BC} ∖ E : B → C), which equals rec(B[E ↦ C] → C).
- By (IB), B[E ↦ C] ⪯_w C at every w. Protection then gives the reverses, so C is all-world tied with B[E ↦ C].
- B[E ↦ C] differs from the coherent B on the non-conic E, so it is incoherent. That contradicts direct (C). ∎

**So in one exact loop at any scale a > 1, the fixed successor fails on the non-null family of splice-fills E ⊆ S_i, at every edge.** Their repairers must differ from P_{i+1}, from P_{i−1}, and from every model that answers A on all of E. They inherit the forced pattern: P_i ⋠_j B for j ≠ k_i, and P_i ⪯_{k_i} B.

A loop-family repair of these splice-fills therefore needs **a second scale or an outside defender.** With a second scale, §4 applies.

**Prop 2.5 (what Λ does and does not supply; PROVED).** Work in the (2V) range and use PP56's Λ (members are the posterior models of a (2V) family containing the m₁-ray).
- (a) Take a class-3 fill of T, E = E^h ∪ E^{−h}, where E^{−h} is the part on which A = −h (the h = B points of Sil(T) ∩ M₃). Let e and f be the |g|-masses of E^h and E^{−h}. Then

  V(P₁(a) → X_E) = (p(a) − e − f, p(a) − e − f, −2p(a) + 2e + 4f).

- (b) If f > 0 and e + f < p(a) < e + 2f, then P₁(a) strictly dominates X_E in Λ, at level 0 at all three worlds. Every fill with a non-null −h part and e + 2f below sup p is therefore dominated within Λ at a window of scales. Λ satisfies every non-section clause (PP56 Thm L).
- (c) **No member dominates an H-model in Λ.** Here an H-model is a model equal to the common advice off R and in {h, S} on R: pure-h fills (f = 0) and every member–member splice are H-models. So pure-h fill domination and splice domination are exactly what Λ cannot supply.

*Proof.*
- (a): V(P₀ → X_E) = e(−1, −1, 2) + f(−1, −1, 4). The h-row and the "otherwise" row of u¹ (PP56 §4.1) apply to A = h and A = −h respectively. Subtract Lemma 1.4(a).
- (b) is immediate from (a).
- (c): for an H-record out of a member, λ·(u¹(new) − u¹(old)) = 0 pointwise, with λ = (1, 1, 1) (PP62 (U3)). Localising to a box keeps this. So every level ℓ of Λ has Σ_w Δ^ℓ_w = 0. At the first level whose vector is nonzero, some coordinate is negative. At that world all earlier entries vanish, so the member refuses. ∎

NUMERICS (`fills73.out`): the formula in (a) is reproduced to Monte Carlo precision over a grid of scales. A pure-h fill admits a nonnegative V only at the knife-edge p(a) = e.

**Answer to Task 1.**
- The axioms force exactly Props 2.1–2.2. The (2V)-family part of these forced constraints is satisfied by Λ uniformly in E, F and H, including all copies (Λ is record-based) and all (TC) triangles. **No axiom-level conflict exists in them.**
- The fixed successor is refuted on S_i (Thm 2.3 + Lemma 2.4).
- The remaining obligations — dominating pure-h fills and member splices — cannot be met by Λ or by any rule that agrees with u¹'s level-0 strict verdicts on H-records (Prop 2.5(c)). That is where every construction must depart from u¹, and §4 shows that the departure must leave both u¹-envelopes once two scales are present.
- I found no contradiction in those remaining obligations. Their consistency with closed sections, for all measurable fills, is **OPEN** here.

---

## 3. Task 2: a fixed rival along two branches

**Lemma 3.1 (germ lemma; PP63 Lemma 4.1(c), restated).** Fix a rival R and a limit source s. Let s_n → s be family sources with C_{s_n} ⪯_w R for all n. Closed sections give C_s ⪯_w R.
- A failure *at the limit* can only be of two kinds: (i) a branch forces acceptance at a world in Ref(s, R); or (ii) the limit acceptances complete an all-world tie with an incoherent R.
- Refusals never pass to limits. So a defence failure "at the limit" can only come from refusals forced directly at s.
- Near s, refusals forced at s spread to a neighbourhood. A branch point x in that neighbourhood that is forced to refuse at the remaining world is undefended.

The forced acceptances available along a branch are guidance, (TC) completion, defence with two refused worlds, and section limits (PP63 §4.1). The loop adds two more kinds: the **forced-pattern acceptance** C ⪯_k B (for B repairing a class-k fill of C), and **domination acceptances**.

**Prop 3.2 (two-branch exclusion; PROVED).** Suppose B dominates a class-k fill of a selected interior C_s, and B dominates class-j fills of selected C_{s_n} with s_n → s and j ≠ k. Then the closed section of the fixed rival B at world j is violated.
- More precisely: C_{s_n} ⪯_j B (forced pattern at s_n) and closed sections give C_s ⪯_j B.
- But C_s ⋠_j B (forced pattern at s).
- Hence for every repairer B, the class-j source set of B has no accumulation point in its class-k source set, for k ≠ j.

For rescaling repairs, the class-k sources of C_y lie on y's +e_k ray (C_x repaired by C_{x∘d_k} ⟺ x ∝ y∘(k : a³)). The three rays meet only at y. So rescaling repairs never trigger Prop 3.2 with s ≠ y.

**Prop 3.3 (endpoints repel; PROVED).**
- (a) The dominators of a fixed fill C[E ↦ A] form a closed subset of the family. This closed set does not contain the source C, because C ⋠_i C[E ↦ A] for i ≠ k by strict (G).
- (b) For a splice X = C_b[F ↦ C_c] between members (F non-conic in L_{bc}), both ends refuse X at some world. So the dominators of X accumulate at neither end.
  - At c: rec(C_c → X) = (L∖F : C_c → C_b) = rec(C_c[F ↦ C_b] → C_b), so direct (C) for C_b forces a refusal.
  - At b: symmetrically, rec(C_b → X) = rec(C_b[L∖F ↦ C_c] → C_c), and direct (C) for C_c forces a refusal.
- (c) In the loop, a splice-fill of Thm 2.3 with E ⊆ S₀(a₀) equals P₀[E ↦ P₂(a)] **for every a ≥ a₀**, because the layers along the +e₂ ray are nested and A is kept. So its dominators avoid u and every P₂(a) with a ≥ a₀.

*Proof.* (a) is closed sections plus strict (G). (b) is (IB) plus direct (C) on the incoherent models displayed. (c) is Lemma 1.2(b) applied monotonically along the ray. ∎

**Prop 3.4 (tie transfer; PROVED).** Let X be incoherent. Let B_n → s and B′_n → s be family dominators of X (sections give C_s ⪯_w X at every w). Suppose that for each world v there is a branch member D_n ∈ {B_n, B′_n} with:
- X ⪯_v D_n (the domination is *tight* at v), and
- D_n ⪯_v C_s.

Then X ⪯_v C_s at every v, which is a direct-(C) failure at s.

*Proof.* The triangle C_s ⪯_v X ⪯_v D_n ⪯_v C_s is accepted at v. (TC) installs its reverses, including X ⪯_v C_s. ∎

Typical trigger: branch 1 strict only at world 1, branch 2 strict only at world 2, with the member comparisons accepted at the tight worlds. Then both branches are tight at world 3; branch 2 is tight at world 1 and branch 1 at world 2, so every world is covered. **This is a design trap, not an axiom-level obstruction.** It is avoided if the two branches share a strict world or if one of the member comparisons is refused.

**Prop 3.5 (in-family scale accumulation; PROVED for repairers on the −e₃ ray at T).**
- (a) *Thin boundary fills.* Let E ⊆ {g ∈ Sil(T) ∩ M₃ : τ₀ ≤ ρ < τ₀(1 + η)}, where ρ := |g₃|/(|g₁| + |g₂|) and τ₀ = c/(c + ε), with E meeting every ρ-level of the band. Then P₁(a′) can dominate X_E only if a′³ < 1 + η.
- (b) *Splice-fills of Thm 2.3.* Let E ⊆ S₀(a) be supported in directions θ := |g₂|/(|g₁| + |g₂|) < η. Then a ray repairer P₁(a′) needs a′³ − 1 < η(a³ − 1).
- In both cases the repairer index tends to u as η → 0, so **in-family repairs accumulate at their source**. The same holds at every member and edge, by Lemma 1.1.

*Proof.* On the M₃ quadrant, P₁(a′) answers A iff ρ < τ₀a′³. In (b), P₂(a) answers A iff ρ < τ₀(1 + θ(a³ − 1)), up to the orientation of the quadrant. So P₁(a′) covers E — and Lemma 2.4 then excludes it — once a′³ exceeds the stated bound. ∎

This is in-family only, as the audit's rescoping requires. Repairers outside the ray are not constrained by it.

**Answer to Task 2.**
- Closed fixed-rival sections plus the accepted comparisons force **no** incoherent all-world tie and **no** defence failure at the limit by themselves.
- The obstructions they do produce are Props 3.2–3.4. Each is a constraint on repair choices, and each is PROVED with every clause derived from the axioms.
- The audit's suggested limit tie occurs exactly under the hypotheses of Prop 3.4, which a construction can avoid.

---

## 4. Task 3: Theorems Q and E on loop members

**Prop 4.1 (balanced swaps across scales; PROVED under (2V)).** Let a′ < a, with m₁(a) ∝ (1, 1, b) and m₂(a′) ∝ (b′, 1, b′), where b′ = a′⁻³ > b. Then the odd-2 part of {C_{m₁(a)} ≠ C_{m₂(a′)}} contains non-null open cones on which C_{m₂(a′)} improves world 2, and others on which it worsens world 2. So there is a non-conic F (radial slabs of equal |g|-mass) with V(F) = 0 at all three worlds.

The same holds with the roles of the two worlds exchanged for a′ > a, and for u versus m₁(a′)∘d₁(a″) with a′ ≠ a″.

*Proof.*
- The ratio m₂(a′)/m₁(a) = (b′, 1, b′/b) lowers world 1 and raises world 3. On odd-2 points both are non-odd worlds, so by Lemma 1.2(b) the first change improves world 2 and the second worsens it.
- Explicitly, at an odd-2 point with g₁, g₃ > 0 > g₂, the A-condition is c(z₁g₁ + z₃g₃) > (c + ε)z₂|g₂|.
  - It is gained where g₃/g₁ > (1 − b′)/(b′ − b).
  - It is lost where the reverse strict inequality holds.
  - Both regions meet the A-boundary in open cones.
- PP62 (1.1): a set made of odd-2 points with c₂(F) = 0 has V(F) = 0. Lyapunov's theorem (μ atomless) and radial slabs give non-conic F.

NUMERICS (`balanced73.out`): explicit balanced F for (m₁(1.05), m₂(1.10)), (m₁(1.10), m₂(1.05)), (u, m₁(1.10)∘d₁(1.05)) and (u, m₁(1.05)∘d₁(1.10)), with |V(F)| ≤ 2·10⁻⁶. Same-loop pairs show one sign only, as Cor 1.3 predicts. ∎

**Prop 4.2 (u¹ accounting of the commitments; PROVED).**
- (a) Every forced refusal of the loop lies at a world with V < 0 (Lemma 1.4 at u; NUMERICS along the loop). So the forced refusals never contradict (L0⁺).
- (b) A domination of a class-3 fill of T by P₁(a) is u¹-endorsed iff e + f ≤ p(a) ≤ e + 2f (Prop 2.5(a)).
  - For pure-h fills this is the knife-edge p(a) = e. The domination record is then u¹-null at all three worlds.
  - At that scale the agreement obstruction is automatically avoided: the A-gained part of L₀₁ has mass ≤ α < p(a) = e, so E cannot lie inside it.
- (c) So the commitments neither force nor exclude (L0⁺) or endorsement. A construction can keep all its *forced* comparisons inside both envelopes. Theorems Q and E then decide.

**Prop 4.3 (Theorem Q on the two-ray star; PROVED).** Let the source family contain {m₁(a) : a ∈ I} for an open interval I, together with one m₂(a′) with a′ ∉ I and a′ ≠ a for some a ∈ I. Let the relation satisfy (L0⁺) for u¹ — for instance Λ, any tie-breaking of Λ, R₀, or "accept iff V_w ≥ ρ_w" with ρ ≥ 0 — and have closed sections at m₁(a). Then direct (C) fails for C_{m₂(a′)}.

*Proof.*
- Theorem Q(i) needs, for each world w, family sources b_k → m₁(a) with Γ_w(m₁(a), b_k) > 0.
  - Inward ray points (smaller a) are +e₃ shifts, which gives w = 3.
  - Outward ray points are −e₃ shifts. These are strictly u¹-better at worlds 1 and 2 (Lemma 1.4(a) at the base point; NUMERICS, `balanced73.out` (H_Γ) block, at m₁(a)). This gives w = 1, 2.
- So C_{m₁(a)} ⪯_w X at every w for X := C_{m₁(a)}[F ↦ C_{m₂(a′)}] with the balanced F of Prop 4.1.
- Theorem Q(ii) then shows that C_{m₂(a′)}[F ↦ C_{m₁(a)}] is weakly no worse than C_{m₂(a′)} at all three worlds. ∎

The only non-axiom hypothesis is (L0⁺). So **every rule on a two-scale loop family must refuse some strictly u¹-favourable comparison out of ray members.**

**Theorem 4.4 (Theorem E with family directions; PROVED).** Let a be a family member, b a member with a balanced non-conic F ⊆ {C_a ≠ C_b}, and X := C_a[F ↦ C_b]. Let w be any world with C_a ⋠_w X; one exists by (IB) and direct (C) for C_b. Suppose the family contains a_n → a with Γ(a, a_n) ∈ O_w, that is, both coordinates v ≠ w negative. Then no allocation is at once:
- u¹-endorsed out of the a_n against X,
- closed in sections at a for X, and
- defended at the a_n.

*Proof.* PP62 Theorem E, steps 1–5, with the pure shift replaced by a_n. Only Γ(a, a_n) ∈ O_w is used. ∎

**Table 4.5 (directions in O_w available in the loop family; Lemma 1.2 and NUMERICS).** A single-coordinate shift that *raises* coordinate w lies in O_w. One that *lowers* a coordinate lies in no O_w.

| member | family neighbours | O-directions available |
|---|---|---|
| u | m₁-ray (−e₃), m₂-ray (+e₂) | O₂ only |
| m₁(a), interior of the ray interval | ray inward (+e₃), outward (−e₃); class-1 repairer (−e₁) | O₃ only |
| m₂(a), interior of the ray interval | ray outward (+e₂), inward (−e₂); class-2 repairer u (−e₂) | O₂ only |
| any member of a family whose closure contains a neighbourhood of it | all | O₁, O₂, O₃ |

**Prop 4.6 (endorsement survives the star; PROVED).** On the two-ray star, with balanced pair (m₁(a), m₂(a′)) and r := rec(C_{m₁(a)} → X), the following assignment satisfies every clause of Theorem 4.4's configuration, including spreading and defence of the ray neighbours:
- Ref(r) = {1} and Acc(r) = {2, 3};
- Ref(r⁻¹) = {1} and Acc(r⁻¹) = {2, 3};
- ray neighbours accept at the endorsed worlds: outward m₁-points at 2 (Γ₂ > 0), inward at 3; outward m₂-points at 2, inward at 3.

*Proof.* Theorem 4.4 needs O₁ at either end, and the star has none. By Table 4.5 the refusing world must avoid 3 at m₁(a) and 2 at m₂(a′). The displayed choice also keeps one endorsed accepting world after spreading. ∎

So **Theorem E excludes u¹-endorsed rules only on richer families**: those whose members are approached from the O-direction of their refusing world. Prop 3.5 shows that in-family recursion makes every member a limit of its repairers along −e₁, −e₂ and −e₃. If the family also contains approximately equal pairs of steps (for example two classes of repair at nearly equal scales), it approaches each member from directions near +e_w for every w. Then Theorem 4.4 applies at every member with a balanced partner.

**Lemma 4.7 (exact ties along the rays; PROVED).**
- The transposition (1 2) of coordinates preserves μ, |g| and M. It fixes u and every point of the m₁-ray R₃. So for a, a′ ∈ R₃ ∪ {u}, Γ₁(a, a′) = Γ₂(a, a′) **exactly**.
- Likewise (1 3) fixes u and every point of the m₂-ray R₂ (indices ∝ (b, 1, b)). So Γ₁ = Γ₃ exactly along R₂.
- NUMERICS (`argmax73.out`): the top-two gaps on R₃-outward and R₂-inward are 0.001–0.07, i.e. Monte Carlo noise. On R₃-inward and R₂-outward the guidance coordinate wins by about 0.85–0.94 (per unit shift).

**Prop 4.8 (coordinator's relay: Theorem Q at u along the m₂-ray; PROVED).** The middle members m₂(a) ∝ (1, a³, 1) are u's pure world-2 shifts, so they are Theorem Q's sequence at u for w = 2. The m₁-ray gives u a second sequence, along which Γ(u, ·) = (p, p, −2p) with p > 0 (Lemma 1.4(a)), favourable at worlds 1 **and** 2. There is no family sequence at u with Γ₃ > 0.
- (a) A rule satisfying (L0⁺) on 𝔽 therefore forces, at u and for every rival X with V(T → X) = 0, acceptance at worlds 1 and 2 (from R₃) and at world 2 (from R₂). It never forces acceptance at world 3.
- (b) Theorem Q(ii) is completed at u exactly when the rule *also* accepts such an X at world 3. This holds, for instance, if it accepts null records at worlds other than a fixed w₀ ≠ 3, as R₀ does. Then T is all-world weakly dominated by a balanced swap toward any installed partner. In PP72's 𝓘, the partners include the defenders sδ₃ + tδ₁ with s ≠ t: their log-coordinates (s − 2t, s + t, t − 2s) have a strictly middle entry, and the Prop 4.1 argument gives both-sign layers. The result is a direct-(C) failure for that partner.
- (c) Dually, the R₂ direction lies in O₂. So by Thm 4.4, **an endorsed rule can never refuse a balanced X at world 2 at u.** The refusing world must be 1 or 3. If the rule accepts at world 1 (via R₃), it must be 3.

So the hypotheses of Theorem Q hold at u for worlds 1 and 2 under any (L0⁺)-type verdicts out of the rays. The failure then hinges on a single verdict: the null comparison T ⪯₃ X.

**Answer to Task 3.**
- Loop members have balanced swaps only across scales (Cor 1.3, Prop 4.1).
- The commitments do not force (L0⁺) or endorsement (Prop 4.2).
- But Theorem Q excludes (L0⁺) on any family that contains an interval of one ray and a second scale on the other (Prop 4.3). The splices of §2 force such a second scale for in-family repair.
- Theorem E excludes endorsement wherever the family supplies the refusing world's O-direction (Thm 4.4).
- So the relation must refuse some u¹-favourable comparisons out of ray members, and on richer families must also accept some u¹-unfavourable ones (PP62 Cor E.2). Neither is an axiom-level contradiction.

---

## 5. Task 4: attack on PP72 (its posted DRAFT: (D1)–(D4) with the u¹-argmax defence 𝒟₀)

PP72 takes:
- the family 𝔽 = {u} ∪ R₃ ∪ R₂, i.e. the two-ray star of §4;
- the installed set 𝓘 = {C_{m+tδ_k} : m ∈ 𝔽, t ≤ t₀}, with the members of 𝓘 ∖ 𝔽 as defenders (defence and protection only);
- the repair rule B(m, E) = C_{m+τδ_k}, with τ half the agreement threshold;
- the least relation 𝓡(𝒟) generated by guidance, the domination records and their copies, and one defence world 𝒟(C, X) per pair, closed under (TC), rules III–IV and section limits on 𝔽, with everything else refused;
- the first candidate 𝒟₀(C, X) = argmax_w V_w(rec(C → X)), with ties "toward the record's designated world".

**5.1 What survives (PROVED).**
- (a) **Agreement.** At τ = ½·(threshold), C_{m+τδ_k} is silent on a non-null part of E, so Lemma 2.4 is never triggered by (D3).
- (b) **The forced refusals are never derived.** For B = C_{m+τδ_k} we have V(C_m → B) = −Γ(m, m + τδ_k), which has its top coordinate at k, with margin of order τ (Table 4.5; NUMERICS margin ≈ 0.85–0.94·τ). For a fixed B and m′ → m, V(C_{m′} → B) → V(C_m → B). So 𝒟₀ assigns k at every m′ near m, and section limits never install C_m ⪯_i B for i ≠ k.
  - The coordinator's point stands: the loop pairs are mixed at the two other worlds, so these refusals are *committed* (by PP72's default refusal), not guidance. They are not undone by 𝒟₀ or by section limits.
  - Whether a (TC) cascade from non-endorsed domination records reaches them is §5.3.
- (c) **Two-branch tests (§3).**
  - Each fill has one dominator, so Props 3.3 and 3.4 are not triggered.
  - For a defender y, its class-k sources in 𝔽 are the points of y − R₊δ_k on R₃ ∪ R₂ ∪ {u}. Since δ_k is parallel to neither ray, there are at most two of them. So Prop 3.2 is not triggered.
  - Defender y = sδ₃ + τδ₁ is both a class-1 repairer (of sδ₃ ∈ R₃) and a class-3 repairer (of τ(δ₃ + δ₁) ∈ R₂). These two sources are distinct and isolated, so the forced patterns at them do not interact.
- (d) **Endorsement of 𝒟₀.** Every installed model is λ-Bayes for u¹ with λ = (1, 1, 1) (PP62 (U2), within (2V)). So max_w V_w ≥ 0 and 𝒟₀'s acceptances are u¹-endorsed. With guidance and copies, the only non-endorsed acceptances in 𝓡(𝒟₀) are the domination records and what (TC) derives from them.

**5.2 Where 𝒟₀ is decided by its tie rule alone (PROVED; the decisive attack).**
- Let a ∈ R₃ (interior or u), and let X be any rival with V(C_a → X) = 0. Examples are the balanced swaps of Prop 4.1 toward an R₂ member, or toward a defender.
- Along R₃ outward, V(C_{a′} → X) = Γ(a, a′) has **exactly tied** coordinates 1 and 2 (Lemma 4.7). Along R₃ inward, the argmax is robustly 3. At a itself all three coordinates are 0.
- So, writing ρ for PP72's tie rule:

  Acc(rec(C_a → X)) ⊇ {3} ∪ {ρ-choices on the R₃-outward records} ∪ {ρ(C_a, X)}.

- For b ∈ R₂ and Y with V(C_b → Y) = 0, R₂-inward is an exact (1, 3) tie and R₂-outward is robustly 2:

  Acc(rec(C_b → Y)) ⊇ {2} ∪ {ρ-choices on the R₂-inward records} ∪ {ρ(C_b, Y)}.

- At u: Acc(T → X) ⊇ {2} ∪ {ρ on R₃ (1 or 2)} ∪ {ρ(T, X)} (Prop 4.8).
- For a balanced pair X = C_a[F ↦ C_b] we have Y = C_b[F ↦ C_a] and rec(C_b → Y) = rec(X → C_a). So F2 (an incoherent all-world tie, via Theorem Q(ii)) occurs **iff** one of these sets is {1, 2, 3}.

Hence 𝓡(𝒟₀) passes the balanced-swap test **only if** ρ satisfies all of:
- (ρ1) along each R₃-outward sequence the 1/2 choice is eventually constant, say ρ₁; and ρ(C_a, X) ∈ {3, ρ₁};
- (ρ2) along each R₂-inward sequence the 1/3 choice is eventually constant, say ρ₂; and ρ(C_b, Y) ∈ {2, ρ₂};
- (ρ3) at u, ρ(T, X) ≠ 3 whenever the R₃ choice is 1.

These conditions are also sufficient for this test. Openness then holds: the refusing world spreads to the ray neighbours, which keep an endorsed accepting world (as in Prop 4.6).

A rule that breaks ties "toward the record's designated world" leaves the designated world **undefined** for balanced swaps, which are not repair records. So PP72 must specify ρ on null records out of every member, and it must satisfy (ρ1)–(ρ3) uniformly in the rival.

In particular, **any ρ that alternates between 1 and 2 along R₃-outward kills 𝒟₀** (F2 at the R₂ partner).

An equivariant ρ cannot break the tie on a τ-invariant record at all. However, 𝓘 contains no τ-invariant balanced rival: the τ-invariant installed indices all lie on R₃, and R₃ pairs are pure shifts. So equivariance alone is not fatal, but ρ must choose between X and X^τ asymmetrically and consistently.

**5.3 Non-endorsed domination records and (TC) (partly PROVED, rest OPEN).**
- For pure-h fills, (D3)'s τ is generically not the mass-balanced scale. So r_E = rec(B → X_E) is accepted at a world with V_w < 0 (Prop 4.2(b)). Lemma S says the closure must refuse a split or accept two more u¹-unfavourable comparisons.
- I tried the natural F1 triangle: r_E, a strict guidance link, and a copy of a 𝒟₀-acceptance by T. It fails at u. The copy link must have argmax at the deficient world, and at u the relevant records out of T have V = (e_in − p, e_in − p, 2p − 2e_in), whose argmax is 3 (because e_in ≤ α < p).
- So I found no F1. Whether the full closure stays clean is OPEN, and it is the first thing PP72's SAT runs (`sat72b.py`) should report, with section literals pinned on R₃ ∪ R₂.

**5.4 Obligations PP72's draft does not yet address (brief, binding).**
- (a) **Splices between installed models.** The brief requires domination of ALL measurable splices between installed models, and 𝓘 now contains a 2-parameter set of defenders. (D3) supplies dominators for fills only.
  - The splices between a source and its own repairer, T[H ↦ C_{τδ₃}], are splices inside 𝔽 itself.
  - By Prop 2.5(c) no rule agreeing with u¹'s level-0 strict verdicts on H-records can let a member dominate them. 𝒟₀'s defence acceptances are of that kind; the domination records would have to be added explicitly, with their copies and (TC) consequences.
- (b) **Splices that are fills.** The class-k fills of C_m inside {B(m, E) = A} are splices C_m[E′ ↦ B]. (D3) repairs them at scale ≤ τ/2 (consistent). But the remaining, non-fill splices C_m[H ↦ B] have no repairer.
- (c) **The loop is used only on a null set of (m, E).** τ = s is a coincidence, so almost every repair goes to a defender with no fill obligations.
  - This avoids the recursion of Prop 3.5, but it is a fixed-direction "one move" scheme. The mixed-class recurrence the brief asks for is not exercised.
  - The splice obligations of (a) are the rivals generated by those defenders, which the success criterion explicitly includes.

**Verdict on PP72's draft.** No axiom-level conflict. The design is viable *only* with an asymmetric null-record tie rule satisfying (ρ1)–(ρ3). Its (TC) closure with non-endorsed domination records is untested. It still owes dominators for all measurable splices between installed models, including its own defenders.

**Relay items (REFEREE_round57).**
- Forced refusals must be committed. This is confirmed, and they survive 𝒟₀ and section limits (5.1(b)).
- PP71's splice core (≥ 10 extra splices) and PP70 Prop 1.5 (last segment only) are not used here.

---

## 6. Axiom-level versus choice-level

| Finding | Axiom-level? | What does the work |
|---|---|---|
| Forced pattern; splice clauses (Props 2.1–2.2) | yes (forced literals; consistent) | (TC), strict (G), defence, protection |
| Agreement obstruction (Lemma 2.4) | yes (a constraint) | (IB), protection, direct (C), non-conicity |
| Fixed successor fails on S_i (Thm 2.3) | no: it refutes a choice | the fixed successor |
| Λ cannot dominate H-models (Prop 2.5(c)) | no: it refutes a rule | Λ's levels |
| Two-branch exclusion; endpoints repel (Props 3.2–3.3) | yes (constraints on choices) | sections, forced pattern, (IB), (C) |
| Tie transfer (Prop 3.4) | conditional | tight dominations on complementary worlds |
| Theorem Q on the star (Prop 4.3) | no | (L0⁺) |
| Theorem E with directions (Thm 4.4) | no | endorsement |
| Any contradiction from the mixed-class obligations themselves | **none found** | — |

---

## 7. Scripts (`r9/PP73_py/`; run `python3 -I -B <script>.py` inside the folder; outputs in `<script>.out`)

| Script | Content | Label |
|---|---|---|
| `lib73.py` | members, ranks, odd worlds, u¹ | — |
| `loop73.py` | Cor 1.3 guidance along the loop; Lemma 1.4 ledger; (2V) | NUMERICS |
| `splice73.py` | Thm 2.3 (a), (b) on samples | NUMERICS |
| `balanced73.py` | Prop 4.1 balanced swaps; (H_Γ) at loop members | NUMERICS |
| `fills73.py` | Prop 2.5(a) formula (error ≤ 6.5·10⁻⁴); knife-edge for pure-h fills; windows for −h and mixed fills | NUMERICS |
| `argmax73.py` | Lemma 4.7: argmax of Γ along the four ray directions (ties are Monte Carlo noise) | NUMERICS |
