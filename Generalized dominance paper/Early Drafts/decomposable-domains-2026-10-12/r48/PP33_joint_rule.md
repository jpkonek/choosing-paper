# PP33. A joint rule for forced defences and their replacement dominators

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full proof here. CHECKED: exact rational computation of proof bookkeeping (`PP33_py/geometry_exact.py`, ALL PASS). NUMERICS: Monte Carlo illustration; no proof depends on it (`PP33_py/budget_mc.py`). CONJECTURE / OPEN: as stated.

**Inputs.** Brief 48; AUDIT_round48_instructions (binding); PP30 (Thm 3.1, Prop 4.2); REFEREE_round47; PP28 (separation lemma), PP29 (retreat split); PP32; AUDIT_completion (rules I–IV, F1/F2); AUDIT_selected_realizability §4; REFEREE_Z_PP19 (Lemma H, Prop S); PP19 (Lemma 0.2, Lemma 5.0, Thm 5); LEAD_selection_count; PP25 (Theorem A, the triangle lemma, Lemma 6). Only Brief 48's axioms are used; each result says which.

---

## 0. Verdict

**I deliver a rule with a proved invariant, on a stated scope, plus one new axiom-level theorem that ties the choice of w to the choice of K. The rule does not yet give (S): one precisely located step is missing.**

| Item | Result | Label | Source of any obstruction |
|---|---|---|---|
| The record ρ_j(G) | Guidance-decided iff G misses one of the two non-j classes. Otherwise mixed at both candidate worlds. ρ_j(G) = ρ_k(G) iff G ⊆ M_l. For G ⊆ M_a ∪ M_b it is T's majority-fill record, so T's choice for X*-type fills fixes V_j's forced defence. (§2) | PROVED | — |
| **Vertex-world endorsement** | If D_K ⪯_j Z, with Z = V_j off a bounded set, then **every bounded record Z → V_j[H ↦ D_K] (H ⊆ {D_K ≠ V_j} bounded) is refused at j.** If the bounded records at j are judged by any potential with a positive leading density ρ_j, this forces **L_j(D_K) ≤ L_j(Z)**. (Thm 3.1) | PROVED | axioms (strict (G), (TC)) for the refusal; the inequality needs the optional potential |
| Consequence | w and K cannot be chosen separately. w fixes Z, Z fixes a budget at world j, and K's cone must fit inside it. Dominators of small rivals converge to V_j in measure. (Cor 3.2, 3.3) | PROVED | as above |
| **The joint rule** | w: every world where PP25's potential L accepts the record. K: the precise model on the ray from e_j towards the centre, D_{λ_j(d)}, with d chosen inside the budget. The rule is applied to V_j **and to every ray model it registers** (the regress). (§4) | definition | — |
| **Invariant and main theorem** | Every installed domination record is (i) strictly endorsed by L at its family's vertex world, (ii) compensated at the two other worlds, (iii) supported far out on a ray wedge, and (iv) unable to land on a member. Under (i)–(iv): strict (G), (IB), (TC) for the whole relation; T, V_1, V_2, V_3 and every ray model are undominated; no single-world ties; closure rules I–IV force nothing; F1 and F2 do not occur. (Thm 5.1) | PROVED | — |
| Survives its own defenders | Yes, for the **forward class**: every rival of a registered model that is worse than it under L_j at its vertex world. This includes **every vertex rival V_j[G ↦ S, E ↦ w-correct]**, for all G, all E and all w. (Prop 4.2) | PROVED | — |
| Sections | Closed **relative to the partial index domain** I = three rays ∪ {p_T}. This is not extension to the simplex. (Prop 6.1) | PROVED (relative) | — |
| Backward class | The rivals of ray models that are L_j-better than their member. No forward ray model can dominate them (PROVED). Backward ray dominators exist but create shadows with forward links (CHECKED). TC for them is OPEN. (§8.1) | PROVED / OPEN | chosen geometry (rays) |
| Missing step for (S) | T and the ray models are competitive against every **bounded** rival, but not yet against unbounded rivals. Extending the potential to unbounded records breaks (TC) at every world where some installed record is L-negative, and balance makes every family have such a world. (Prop 8.2) | PROVED | chosen design (L as the bounded layer) plus the forced endorsement of Thm 3.1 |

**In one sentence.** PP30's forced defence makes V_j refuse its own improved retreat Z; Theorem 3.1 shows that whoever replaces V_j as Z's dominator must, at world j, fit inside a budget that Z itself sets; the ray rule meets that budget with a precise model at the right distance from e_j, and the same rule applied to its own defenders closes into a consistent relation, except for one class of rivals and for competitiveness against unbounded rivals.

---

## 1. Setting and notation

Brief 48's setting. Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain; models modulo null sets. Ranks: correct 0, silent 1, wrong 2, contradictory 3. On a mixed problem of class M_k, A is the majority answer and B the minority answer. T = D_M, M = c·1 + εΔ. Sil(T) is T's silent cone. It contains no unanimous problem.

For a fixed j, write a and b for the other two worlds.

**Records.** rec(X, Y) = (D, X|_D → Y|_D) with D = {X ≠ Y}. (IB): one verdict per record and world. A(r) is the set of worlds accepting r.

**The bounded layer L (PP25 Theorem A).** Put ρ_w = 2 on M_w and ρ_w = 1 elsewhere. For any record r and world w, let

  Φ_w^{(1)}(r) := ∫ ρ_w (r_w(new) − r_w(old)) dμ,

which is finite for **every** record, bounded or not, because ρ is bounded and μ is finite. Write L_w(X) := ∫ ρ_w r_w(X) dμ, so Φ_w^{(1)}(rec(X, Y)) = L_w(Y) − L_w(X). The rule L accepts a **bounded** record at w iff (Φ_w^{(1)}, then the integrals over a fixed countable generating family of bounded boxes) ≥ 0 lexicographically.

Two facts are used repeatedly.
- **Balance.** On a mixed problem, Σ_w ρ_w (r_w(x) − r_w(y)) = 0 for x, y ∈ {A, S, B}. So Σ_w Φ_w^{(1)}(r) = 0 for every record between models that are regular (never contradictory) and agree on U.
- **PP25 Theorem A.** L satisfies strict (G), (IB) and (TC) on bounded records; it has no single-world ties; every model correct on U and never contradictory is strictly competitive against every bounded rival and is dominated by no bounded rival.

**Rays and wedges.** For j and s ∈ [0, 1) put λ_j(s) := (1 − s)e_j + s·u and R_j(s) := D_{λ_j(s)}, so R_j(0) = V_j. For a problem g with g_j·Σg < 0, put s0_j(g) := g_j / (g_j − Σg/3) ∈ (0, 1); otherwise s0_j(g) := ∞.

**Lemma 1.1 (ray threshold; PROVED; CHECKED (2)).** R_j(s) gives j's answer at g iff s < s0_j(g), and the opposite answer iff s > s0_j(g).

*Proof.* λ_j(s)·g = (1 − s)g_j + sΣg/3 is affine in s, equals g_j at s = 0, and changes sign exactly once, at s0_j, when g_j and Σg have opposite signs. ∎

So R_j(m) and R_j(d) (m < d) differ exactly on the **wedge** W_j(m, d) := {m < s0_j < d}, an open cone. There R_j(m) gives j's answer and R_j(d) gives the other one.

**Lemma 1.2 (wedge geometry; PROVED; CHECKED (3), (4), (7)).** For 0 ≤ m < d < 1:
- (a) W_j(m, d) meets M_j, M_a, M_b and Sil(T), each in a non-null open set;
- (b) W_j(0, 1) ∩ W_k(0, 1) ⊆ M_l, where l is the third world, and there j's answer = k's answer = A;
- (c) for every x < 1, W_j(m, d) ∩ M_l contains a non-null open set where s0_k > x.

*Proof.* (a) Explicit points with s0_j = t for any t ∈ (0, 1), written for j = 1: (−α, 1, 1) ∈ M_1 with α = 2t/(3 − 2t); (−α, 1, −β) ∈ M_3 and (−α, −β, 1) ∈ M_2 with β small and α = t(1 − β)/(3 − 2t); (−α, −2, 3) ∈ Sil(T) with α = t/(3 − 2t) ∈ (0, 1). For the last: Σ = 1 − α ∈ (0, 1), so cΣ − 2ε < 0 < cΣ + 3ε. All conditions are open.
(b) s0_j, s0_k < ∞ means g_j and g_k both have the sign opposite to Σg. Then g_l has the sign of Σg, so l is the minority world.
(c) g_j = −a, g_k = −K, g_l = a + K + 1, with K large and a = t/(3(1 − t)). ∎

---

## 2. The record ρ_j(G)

Fix j, a bounded non-null G ⊆ Sil(T), and write G_k := G ∩ M_k. The record is ρ_j(G) := (G, S → V_j|_G): S → B on G_j, S → A on G_a ∪ G_b. Per unit mass, the rank changes are:

| piece | world j | world a | world b |
|---|---|---|---|
| G_j (S → B) | −1 | +1 | +1 |
| G_a (S → A) | −1 | +1 | −1 |
| G_b (S → A) | −1 | −1 | +1 |

**Proposition 2.1 (classification; PROVED).**
- (a) j ∉ A(ρ_j(G)): it is a strict j-improvement.
- (b) **Guidance-decided.** If G_b is null, ρ_j(G) is a weak a-worsening, so a ∈ A by guidance. Then the forced refusal V_j ⋠_a Z is itself strict guidance: Z is a strict a-improvement of V_j. Symmetrically if G_a is null. In particular, if G lies in one class the obligations are trivial.
- (c) **Mixed.** If G_a and G_b are both non-null, the record is a genuine trade at both a and b. T must accept it at one of them (PP30 Thm 3.1), and every accepting world w carries the forced refusal V_j ⋠_w Z^w_{G,E} for all E.
- (d) **Shared across vertices.** ρ_j(G) = ρ_k(G) iff G ⊆ M_l (l ∉ {j, k}), because V_j = V_k exactly on M_l ∪ U.
- (e) **Shared with T's fills.** For G ⊆ M_a ∪ M_b, ρ_j(G) = (G, S → A) is T's majority-fill record. So T's choice of defence world against the two-class fill T[G ↦ A] (the referee's X*) **is** V_j's forced defence. There is one record and therefore one verdict.
- (f) **Shared with registered models.** For any coherent N with N = V_j on G, (G, S → N|_G) = ρ_j(G). So every such N inherits the refusal N ⋠_w N[G ↦ S, E ↦ w-correct] at every w ∈ A(ρ_j(G)), by the same (TC) argument as PP30 Thm 3.1(b).

*Proof.* Read off the table. (f): N[G ↦ S] ⪯_w N is a copy of T ⪯_w T[G ↦ V_j]; the improved retreat is a strict w-improvement of N[G ↦ S]; then apply (TC). ∎

**The verdict for w.** By (IB), w can depend only on the record. In the construction the verdict is L's (Table, CHECKED (1)):

  Φ_a^{(1)}(ρ_j(G)) = μ(G_j) + 2μ(G_a) − μ(G_b),  Φ_b^{(1)} = μ(G_j) + 2μ(G_b) − μ(G_a),  Φ_j^{(1)} = −(2μ(G_j) + μ(G_a) + μ(G_b)).

The two non-j values sum to 2μ(G_j) + μ(G_a) + μ(G_b) > 0, so at least one world accepts. When |μ(G_a) − μ(G_b)| < μ(G_j) + min(μ(G_a), μ(G_b)), both do. This is the only freedom (IB) allows: **w is a function of the record, and every accepting world brings its own forced refusal.** The joint choice therefore cannot run from K back to w. It runs from w to K, through Z. Section 3 shows that this direction is forced.

NUMERICS (`budget_mc.out` (a)): for PP30's two balls (G_a in M_2 and G_b in M_3, equal mass), the values at worlds 2 and 3 are both positive (≈ +3.3·10⁻⁴ and +3.0·10⁻⁴). This is a mixed record accepted at both candidate worlds.

---

## 3. The vertex-world endorsement theorem

**Theorem 3.1 (forced endorsement at a world without compensation; PROVED).** Uses reflexivity, strict (G) and (TC) only. Let N be any model, v a world, and Y a model with Y = N off a bounded set. Let C be a model with C ⪯_v Y, and suppose C **has no v-compensation relative to N**: N ≤_v C pointwise on Q := {C ≠ N}, and Q is not essentially bounded. Then for every bounded H ⊆ Q,

  Y ⋠_v B_H,  where B_H := N[H ↦ C].

The record rec(Y, B_H) is bounded.

*Proof.* B_H = C on H. Off H, B_H = N. Ranks at one world are injective on the four advice values, so N <_v C strictly on Q, and Q ∖ H is non-null. So B_H ≤_v C pointwise, strictly on Q ∖ H, and strict (G) gives B_H ≺_v C. If Y ⪯_v B_H held, then C ⪯_v Y ⪯_v B_H ≺_v C would violate (TC). The record is supported in the bounded set {Y ≠ N} ∪ H. ∎

**This applies to every dominator of every vertex rival.** V_j is j-perfect, so any C ≠ V_j has no j-compensation relative to V_j. If C is coherent, Q = {C ≠ V_j} is a non-null cone (Lemma H), hence not essentially bounded. Take N = V_j, v = j, Y = Z = V_j[G ↦ S, E ↦ w-correct].

**Corollary 3.2 (budget at the vertex world; PROVED).** Suppose, in addition, that at world v every bounded record with Φ_v^{(1)} > 0 is accepted, where Φ_v^{(1)} = ∫ρ_v Δr_v and ρ_v > 0 is bounded. L is one such rule. Then, under the hypotheses of Theorem 3.1,

  L_v(C) ≤ L_v(Y).

*Proof.* By the theorem, Φ_v^{(1)}(rec(Y, B_H)) = L_v(B_H) − L_v(Y) ≤ 0 for every bounded H ⊆ Q. Let H increase through Q ∩ (balls of radius n). Then B_H → C pointwise, and dominated convergence gives L_v(C) ≤ L_v(Y). ∎

For a vertex rival the budget is explicit:

  L_j(Z) − L_j(V_j) = 2μ(G_j∖E) + μ((G_a ∪ G_b)∖E) + 4μ(E ∩ G_j) + 2μ(E ∩ G_w),

while a dominator's cost is ∫_{C ≠ V_j} ρ_j r_j(C) dμ. So **w (through E's w-correct answers) and K (through its cone) enter one inequality.**

**Corollary 3.3 (dominators of small rivals accumulate at V_j; PROVED).** Under Cor 3.2's hypothesis at world j, every dominator C of a vertex rival Z satisfies μ{C ≠ V_j} ≤ L_j(C) ≤ L_j(Z) → 0 as μ(G) → 0. (Each point where C ≠ V_j contributes ρ_j·rank ≥ 1.) So the replacement dominators converge to V_j in measure. PP30 Prop 4.2(c) keeps each one's index away from e_j for a fixed Z; Corollary 3.3 says the models approach V_j anyway, at a rate set by the rivals.

**Classification.** Theorem 3.1 comes from the axioms, plus PP30 Thm 3.1 (T selected) to make the domination necessary. Cor 3.2 adds an optional choice: the bounded records at j are judged by a positive-density potential. Theorem 3.1 also explains why PP19 Thm 5 and Prop S do not bite on V_j's dominators. Those kills build a rival from the dominator's compensation set at the world being killed. At j that set is empty, so V_j defends at j by guidance. **Endorsement replaces compensation at the vertex world.**

---

## 4. The joint rule

**Members.** 𝓜 := {T} ∪ {R_j(s) : j = 1, 2, 3; s ∈ [0, 1)}. This includes V_j = R_j(0). All are coherent, correct on U and never contradictory.

**Forced rivals.** For each ray member N = R_j(m) and each bounded non-null G ⊆ Sil(T), let A_G := {w : L accepts (G, S → N|_G) at w}. For each w ∈ A_G and each non-null E ⊆ G with Z ≠ N, put

  Z = Z(N, G, E, w) := N[G ↦ S, E ↦ w-correct].

Every one of them is refused by N at w (Prop 2.1(f), or PP30 Thm 3.1(b) when N = V_j). They are incoherent by Lemma H, so each needs a dominator.

**Forward class.** Z is *forward* if L_j(Z) > L_j(N).

**Lemma 4.1 (PROVED).** Every vertex rival is forward. For a ray member N = R_j(m), if Z is forward then {Z ≠ N} ∩ {s0_j > m} is non-null.

*Proof.* Z ≠ V_j and V_j is j-perfect, so L_j(Z) > 0 = L_j(V_j). For the second claim, suppose {Z ≠ N} ⊆ {s0_j ≤ m}, up to a null set. There N gives the non-j answer, which is j-wrong (Lemma 1.1). At each such point Z gives S or the w-correct answer, and differs from N's answer. A w-correct answer different from N's must be the j-answer, since there are only two answers. So Z's advice there is S or j-correct, both strictly j-better than N's. Hence Z ≤_j N pointwise, strictly on a non-null set, and L_j(Z) < L_j(N). This contradicts forwardness. ∎

**The rule (forward class).** For forward Z with member N = R_j(m), call d ∈ (m, 1) *admissible* if:
- (E) L_j(R_j(d)) < L_j(Z)  (strict endorsement at the vertex world);
- (X) {Z ≠ N} ∩ {s0_j > d} is non-null  (exposure, no landing).

Both conditions are monotone in d. The cost L_j(R_j(d)) − L_j(N) = 2∫_{W_j(m,d)} ρ_j dμ decreases to 0 as d ↓ m, and (X) holds for d near m by Lemma 4.1. So the admissible set is an interval (m, m + δ*) with δ* > 0. **Install**

  K(Z) := R_j(m + δ*/2),  and accept rec(K(Z), Z) at all three worlds,

together with all its (IB) copies. Register K(Z) as a member. It already lies on the ray, so the family 𝓜 is closed under the rule.

**Where each defender is selected.** C_{λ_j(s)} := R_j(s) for s ∈ [0, 1); in particular C_{e_j} = V_j. T is selected at one interior index p_T off the three rays. This gives the partial index domain I := {p_T} ∪ ⋃_j λ_j([0, 1)).

**Proposition 4.2 (the rule survives its own defenders, forward class; PROVED).** Every member's forward rivals receive a dominator in 𝓜 satisfying (E) and (X). The new dominators are members, and their own forward rivals are handled by the same rule. In particular, **all of the brief's family** (V_j, every bounded G ⊆ Sil(T), every non-null E ⊆ G, every accepting w) is covered.

*Proof.* Admissibility is nonempty, as shown above. Lemma 4.1 covers the vertex case. ∎

NUMERICS (`budget_mc.out` (b), (c)): for PP30's balls, with w = 2 and E = the M_2 ball, the budget is L_1(Z) − L_1(V_1) ≈ 9.6·10⁻⁴. Ray costs are ≈ 0.48·d. The values d = 0.0005, 0.001 and 0.0015 are admissible; d = 0.003 is not. For d = 0.001 the installed record's first-level values are (+4.8, −7.5, +2.7)·10⁻⁴: endorsed at world 1, **not** endorsed at world 2, and summing to 0 by balance. The dominator beats V_1 on its wedge at worlds 2 and 3, and nowhere at world 1.

---

## 5. The invariant and the main theorem

Let 𝒢 be the set of installed records and all their copies. The relation at world v is

  X ⪯_v Y  :⟺  rec(X, Y) is bounded and accepted by L at v; or rec(X, Y) is an unbounded weak v-worsening (guidance); or rec(X, Y) ∈ 𝒢.

**Invariant (Inv).** Each installed record r = rec(C, Z), with member N = R_j(m), C = R_j(d), d > m, satisfies:
- (i) Φ_j^{(1)}(r) > 0 (strict endorsement at the family's vertex world);
- (ii) at both a and b, C is strictly better than N on a non-null subset of the wedge W := W_j(m, d), so the far part of r is not a weak improvement there (**compensation**);
- (iii) the far part of r is rec(C, N) on W, from the non-j answer to the j-answer;
- (iv) {C ≠ Z} ∩ G ⊇ a non-null set where C ≠ Z, and no member M satisfies M = Z a.e. on {C ≠ Z} (**no landing**).

**Lemma 5.0 (the rule maintains Inv; PROVED; CHECKED (6)).** (i) is (E). (iii) is Lemma 1.1. (ii): on W ∩ M_j (non-null by Lemma 1.2(a)), C says A and N says B. A is correct at a and at b, while B is wrong at both. (iv): see the proof of Thm 5.1, item 4.

**Two further facts.**
- **(B2) No mutually inverse far parts (PROVED).** Within a family every far part runs non-j → j. Across families, W_j ∩ M_j is disjoint from W_k (Lemma 1.2(b)), so the supports differ.
- **Shadow-freeness (PROVED; CHECKED (5): 900 link pairs, 0 shadow points).** For installed records r_1 (member N_1, dominator C_1, far support S_1) and r_2 (N_2, C_2, S_2), N_1 ≠ C_2 at every point of S_1 ∩ S_2.
  - *Same family:* on S_1 ∩ S_2, N_1 = R_j(m_1) gives the j-answer (s0_j > m_1) and C_2 = R_j(d_2) gives the non-j answer (s0_j < d_2).
  - *Families j ≠ k:* the overlap lies in M_l, where N_1 gives A (its own family's answer) and C_2 gives B (the opposite of k's answer, which is A), by Lemma 1.2(b).

**Theorem 5.1 (main theorem; PROVED).** For the relation above:
1. **Strict (G) and (IB).**
2. **(TC).**
3. **No single-world ties** between distinct models. Hence direct (C) holds vacuously.
4. **Every member is undominated.** Each installed domination is strict at all three worlds.
5. **Closure.** Rules I–IV of AUDIT_completion force nothing new, and F1 and F2 do not occur.
6. **Competitiveness.** V_j is competitive at j against every model. T and every ray model R_j(s) with s > 0 (interior index, full support) are strictly competitive against every **bounded** rival.

*Proof.*

**1.** All three pieces are record-based. Weak worsenings are accepted: bounded ones by L, unbounded ones by guidance. Now take a non-trivial pure improvement at v. L refuses it if it is bounded (PP25 Thm A). Guidance does not accept it. It is not in 𝒢: at v = j because Φ_j^{(1)} of a pure j-improvement is < 0, against (i); at v ∈ {a, b} by (ii).

**2.** (TC) is equivalent to: every accepted triangle has all three reverses. By PP25's triangle lemma, a triangle has 0, 2 or 3 unbounded edges.
- **0:** L's own (TC).
- **2:** the bounded edge e and two unbounded links ℓ, ℓ′ whose far parts are mutually inverse.
  - (Guid, Guid): both far parts are weak worsenings and mutually inverse, so they are trivial; contradiction.
  - (Guid, r ∈ 𝒢): r's far part is a weak v-improvement. At v ∉ {r's vertex world} this contradicts (ii). At r's vertex world j, add the first-level values around the triangle: e ≥ 0 (lexicographic acceptance), the guidance link ≥ 0, r > 0 by (i). They must sum to 0, since Φ_j^{(1)} is additive along composed copies; contradiction.
  - (𝒢, 𝒢): excluded by (B2).

  So no triangle with exactly one bounded edge is accepted.
- **3 unbounded:**
  - *At most one 𝒢 link.* Rank changes sum to 0 pointwise around a triangle. With two guidance links, the 𝒢 link r is a weak v-improvement as a whole record. That contradicts (ii) at a non-vertex world and (i) at the vertex world, as above. Three guidance links are each trivial.
  - *At least two 𝒢 links.* Any two edges of a triangle are consecutive: ℓ_1 = rec(P, Q), ℓ_2 = rec(Q, R). On the overlap of their far supports, Q equals both N_1 (new side of ℓ_1) and C_2 (old side of ℓ_2). By shadow-freeness the overlap is null.
    - *Three 𝒢 links:* each far point of S_1 lies in no other far support, so ℓ_1's rank change could not cancel there; contradiction.
    - *Two 𝒢 links and a guidance link ℓ_3:* on far S_1, ℓ_3's change is minus ℓ_1's, so ℓ_1's far part is a weak v-improvement. That contradicts (ii) unless v is ℓ_1's vertex world j. Likewise for ℓ_2, so both are j-family links at v = j. Then the first levels sum to > 0; contradiction.

  So the only accepted triangles are inside L, or are trivial.

**3.** A tie at v needs r and r⁻¹ both accepted.
- Bounded: L has no ties.
- Guidance with guidance: trivial.
- Guidance with 𝒢: excluded by (ii) or (i), as in 2.
- 𝒢 with 𝒢: excluded by (B2).

**4.** Suppose B weakly dominates a member M. The single record rec(B, M) is accepted at all worlds.
- If it is bounded, PP25 Thm A(5) applies.
- If it is accepted by guidance at all worlds, then B → M is a weak worsening at every world at every point. Between U-correct regular advice that forces B = M.
- If it lies in 𝒢 (at even one world it is a copy of some rec(C, Z)), then M = Z a.e. on S := {C ≠ Z}: a *landing*. Exclude it.
  - S contains the open cone W far out, where Z = N. Since M and N are coherent, M = N on all of W (their disagreement is conic).
  - Among members, only R_j(x) with x ≤ m agree with N on W. T is silent on W ∩ Sil(T) (non-null, Lemma 1.2(a)), where N answers. V_k and R_k(x) (k ≠ j) say A on W ∩ M_j, where N says B. (Lemma 1.2(b) puts W_j ∩ M_j outside W_k.)
  - So M = R_j(x), x ≤ m, which is precise. If G ∖ E is non-null, Z is silent there and C answers, so G ∖ E ⊆ S. M is never silent; no landing.
  - If E = G: on {Z ≠ N} ∩ {s0_j > d}, which is non-null by (X), C = N ≠ Z. So this set lies in S. There M = R_j(x) = N (both give the j-answer, since s0_j > d > x) ≠ Z. No landing.

  No landing means no weak dominator. Since there are no ties (3), every weak acceptance of an installed domination has a refused reverse, so each installed domination is strict at every world.

**5.**
- Rule I: the relation is record-based.
- Rule II: item 2.
- Rule III: by item 4, a weak all-world dominator of a member is impossible.
- Rule IV: vacuous by item 3.
- F1: strict guidance reversals are excluded by item 1.
- F2: only members are registered, and they are coherent.

**6.** V_j is j-perfect, so every record out of V_j is a weak j-worsening and is accepted at j (by L or by guidance). For T and the interior ray models, use PP25 Thm A(4). It needs only U-correctness and non-contradiction, and the indices are interior. ∎

**Mixed triangles across different (G, E) and j, and shared records.** These are all inside Theorem 5.1(2), because the relation is record-based and the proof runs over arbitrary copies.

Three instances that previous rounds flagged are worth naming:
- (α) **One record, two roles.** ρ_j(G) for G ⊆ M_a ∪ M_b is both T's X*-defence and V_j's forced defence (Prop 2.1(e)). L gives it one verdict. The refusal it forces on V_j and on every ray-j member agreeing with V_j on G is a consequence of (TC), which item 2 proves.
- (β) **Two vertex families overlapping.** A V_1-rival's dominator wedge and a V_2-rival's dominator wedge overlap only in M_3, where the V_1-side member says A and the V_2-side dominator says B. That is not a shadow, so no GG triangle forms (CHECKED (4), (5)).
- (γ) **A chain of defenders.** V_j's dominator R_j(d), then R_j(d)'s own dominator R_j(d′), and so on. The wedges are consecutive intervals of s0_j, so their far supports are disjoint and no consecutive pair has a shadow. A closed cycle of j-family dominations cannot occur at all, because the first levels Φ_j^{(1)} of its links are all > 0 but must sum to 0.

---

## 6. Sections on the partial index domain

**Proposition 6.1 (relative closedness; PROVED).** Fix a model X and a world w. Then A_w(X) ∩ I is closed **relative to I** = {p_T} ∪ ⋃_j λ_j([0, 1)).

*Proof.* p_T is isolated in I. On a ray, parametrise by s ∈ [0, 1). {s : R_j(s) ⪯_w X} is the union of three sets.
- **Bounded acceptances.** At most one s: if rec(R_j(s), X) and rec(R_j(s′), X) are both bounded, then R_j(s) and R_j(s′) agree off a bounded set. Their disagreement W_j(s, s′) is a cone, so it is null, so s = s′ (Lemma 1.2(a)).
- **Guidance.** Contained in {s : R_j(s) ≤_w X a.e.}, which is closed: if s_n → s, then R_j(s_n)(g) = R_j(s)(g) eventually for every g with s0_j(g) ≠ s, which is a.e. Inside this closed set, the bounded-record points are accepted by L anyway, because a bounded weak worsening is L-accepted. So the guidance part together with its bounded points is exactly the closed set.
- **𝒢-copies.** At most two s.
  - A copy (Y[S ↦ C], Y[S ↦ Z]) with old model R_j(s) has X = R_j(s) off S and X = Z on S.
  - If R_j(s) = C, then X = Z, and s is the index of Z's unique dominator.
  - Otherwise R_j(s) = C on the wedge W_j(m, d) forces s ≥ d (Lemma 1.1). Then X's far non-j set in the s0_j coordinate is (0, m) ∪ (d, s), whose supremum s is read off X.
  - Old models from other families, T, or V_k (k ≠ j) are impossible, because each differs from C = R_j(d) on a non-null part of the wedge W := W_j(m, d), where C gives the non-j answer.
    - R_k(x) differs on the part of W ∩ M_l with s0_k > x (Lemma 1.2(c)). There R_k(x) says A and C says l's answer B.
    - T differs on W ∩ Sil(T).
    - V_k differs on W ∩ M_{k′}, k′ the third world. There C says B (k′'s answer) and V_k says A.

A closed set union finitely many points is closed. ∎

**What this is not.** I is not closed in Δ (u is a limit point of all three rays and is not in I). The edges and the rest of the interior carry no selection. Relative closedness on I is **not** a substitute for a whole-simplex section; see §8.3.

---

## 7. Where the other tools enter

- **PP30 Thm 3.1, Prop 4.2.** They generate the forced rivals (§4). Prop 4.2(b): every installed record is unbounded, because its far part is the cone W. Prop 4.2(c): for a fixed Z, its dominator index m + δ*/2 is > m, hence away from N's index.
- **PP19 Thm 5 / Prop S (compensation).** At a and b the dominators are compensated, by (ii). At j they are not, and none is needed: N = V_j defends at j by guidance, and ray members defend at j against the Lemma 5.0 rivals by guidance as well, because their dominators are j-worse everywhere on W. Theorem 3.1 is what takes compensation's place at j.
- **PP28 separation lemma.** It is not used. It governs bounded certificate records. Here the dominations are unbounded, and its role is taken by **shadow-freeness**, the unbounded analogue. Two dominations can close a triangle only if one's member equals the other's dominator on overlapping far supports. Nested-and-disjoint wedges along one ray, and the M_l-only overlap across rays, rule this out.
- **PP29 retreat split.** It is not needed. Every bounded record, including every retreat out of a new defender, gets L's single record-based verdict. In particular T does **not** dominate inverted departures, which the audit allows.
- **Lemma H.** Used for incoherence of Z, conic disagreement of members (landing and sections), and the cone Q in Theorem 3.1.
- **Rules I–IV, F1/F2.** Theorem 5.1(5): the explicit relation is already closed.
- **PP32.** L is a single positive field on bounded records, so by PP32 Thm 3.1 it cannot be kept once edge indices are selected. Nothing in Theorem 5.1 uses edges. Theorem 3.1, however, survives any replacement: at each vertex world, whatever potential judges bounded records must endorse the vertex rivals' dominators.

---

## 8. What is not done, precisely

### 8.1 The backward class (OPEN)

A rival Z of a ray member N = R_j(m), m > 0, with L_j(Z) ≤ L_j(N). For example, G inside N's j-wrong wedge, with w = j accepted by guidance.

**Proposition 8.1 (PROVED).** No R_j(d) with d > m dominates such a Z. Any dominator must be j-better than N somewhere: it must have j-compensation.

*Proof.* R_j(d) has no j-compensation relative to N. Theorem 3.1 and Cor 3.2 then give L_j(R_j(d)) ≤ L_j(Z) ≤ L_j(N) < L_j(R_j(d)); contradiction. ∎

**Backward ray models.** R_j(x) with x < m, chosen with L_j(R_j(x)) < L_j(Z) (possible since L_j(V_j) = 0 < L_j(Z)), are compensated at all three worlds. But they have **shadows** with forward links of the same family and of other families (CHECKED (5): 816 and 261 shadow points in the two test pairs). So Lemma 6 of PP25 no longer excludes GG triangles. The same-family 3-cycle is still excluded by the first-level sum. Mixed cycles are not settled.

- Classification: **chosen geometry** (ray dominators).
- Nearby target: dominators of the backward class taken off the rays, for example R_j-models tilted toward the edge [e_j, e_w], whose wedges avoid the forward wedges.

### 8.2 Competitiveness against unbounded rivals (missing for (S))

T and the ray models defend against bounded rivals only. Against an unbounded rival, the relation offers just guidance and 𝒢. So, for example, T ⪯_w R_1(s) holds at no world. **The relation is not an (S)-system.**

**Proposition 8.2 (located obstruction; PROVED).** Let v be a world, and r = rec(C, Z) ∈ 𝒢 with Φ_v^{(1)}(r) < 0. Then accepting at v every unbounded record with Φ_v-lex ≥ 0 violates (TC). By balance, every installed record has such a world: Σ_w Φ_w^{(1)}(r) = 0 and Φ_j^{(1)}(r) > 0.

*Proof.* Let Q := Z[F ↦ contradiction] for a small non-null bounded F off {C ≠ Z}, with 0 < Φ_v^{(1)}(rec(Z, Q)) < −Φ_v^{(1)}(r).
- Z ⪯_v Q holds by guidance.
- Q ⪯_v C holds under the extended potential, since Φ_v^{(1)}(rec(Q, C)) = −Φ_v^{(1)}(r) − Φ_v^{(1)}(rec(Z, Q)) > 0.
- C ⪯_v Z holds in 𝒢.

The reverse C ⪯_v Q has Φ_v^{(1)} = Φ_v^{(1)}(r) + Φ_v^{(1)}(rec(Z, Q)) < 0, so neither the potential nor guidance accepts it (a weak worsening has Φ_v^{(1)} ≥ 0). It is not in 𝒢 either: every installed record has a new side free of contradictions. So (TC) fails. ∎

So the unbounded layer at the non-vertex worlds must be **non-additive**: it must accept enough of T's and the ray models' defences against unbounded rivals without containing a potential that refuses some installed domination.
- Classification: chosen design (L as the bounded layer), combined with the forced endorsement of Theorem 3.1 and balance.
- This is exactly where PP19's Lemma 5.0 kills would live: they are T's or a member's defences against unbounded rivals built from compensation sets.

### 8.3 From I to the simplex

The edges are missing. By PP32, L cannot be the bounded layer there. Theorem 3.1 says what any replacement must keep: at each vertex world, every dominator of a vertex rival is endorsed by the bounded potential.

### 8.4 T's own rivals

The incoherent X_G = T[G ↦ V_j] also need dominators under (S). They are outside Brief 48's family and are not installed here.

**CONJECTURE 8.3.** Theorem 5.1 extends to the backward class with off-ray dominators chosen per rival, keeping (i)–(iv) and shadow-freeness. Evidence: (B2), the vertex-world argument and the landing argument all carry over verbatim. Only shadow-freeness needs a new geometric choice.

---

## 9. Status

| Result | Label |
|---|---|
| Lemma 1.1, 1.2 (rays, wedges) | PROVED; CHECKED |
| Prop 2.1 (record classification, shared records) | PROVED; table CHECKED |
| **Thm 3.1** (vertex-world refusal), Cor 3.2 (budget), Cor 3.3 (accumulation at V_j) | PROVED |
| Rule §4; Lemma 4.1; Prop 4.2 (closure under own defenders, forward class) | PROVED |
| **Thm 5.1** ((G), (IB), (TC), no ties, members undominated, closure clean, bounded competitiveness) | PROVED |
| Prop 6.1 (sections closed **relative to I**) | PROVED (relative only) |
| Prop 8.1 (backward class needs j-compensation); backward shadows | PROVED; CHECKED |
| Prop 8.2 (no potential extension to unbounded rivals) | PROVED |
| Budget and admissible d for PP30's balls | NUMERICS |
| Backward class (TC); unbounded competitiveness; edges; T's own rivals | OPEN; Conj 8.3 |

**Scripts** (`r9/PP33_py/`; run `python3 -I -B <script>` inside the folder):

| Script | Content | Label |
|---|---|---|
| `geometry_exact.py` → `.out` | (1) record table under L; (2) ray threshold on 3,906 rational cases; (3) 3,600 explicit wedge points in M_j, M_a, M_b, Sil(T), for wedges across (0, 0.99); (4) overlap ⊆ M_l with j-answer = k-answer = A (705 points); (5) shadow test: 900 forward link pairs on 7,917 points, 0 shadows; forward–backward shadows present; (6) compensation at both non-vertex worlds and none at the vertex world (40 links); (7) Lemma 1.2(c), 1,800 points. ALL PASS. | CHECKED |
| `budget_mc.py` → `.out` | PP30's balls: L-values of ρ_1(G); vertex-world budget; admissible d; first-level values of the installed record (sum 0); compensation masses. 4·10⁶ Gaussian samples, standard errors printed. | NUMERICS |

**Most important next step.** Build a non-additive unbounded layer at the non-vertex worlds that gives T and the ray models a defence against every unbounded rival while accepting every installed domination. Prop 8.2 says it cannot be the extended potential. Theorem 5.1's shadow argument says the dominations themselves impose only far-part conditions. So the natural candidate is an angular (far-part) verdict that is **positive on the installed wedges at a and b** and decides other unbounded records by far parts first. PP25 Prop D is the template, and (ii) is exactly its hypothesis at the non-vertex worlds.
