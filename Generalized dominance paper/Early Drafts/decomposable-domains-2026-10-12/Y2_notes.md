# Y2. Joint edges on the full two-sided domain: shared boundary triples, link-class rigidity, and what T1 needs from the boundary

16 Oct 2026, round 27 (BRIEF19, milestone 2). Labels:
- **PROVED**: full proof here, from the cited results.
- **CHECKED**: an exact finite computation (rational arithmetic) that is reproducible.
- **CONJECTURE**.
- **NUMERICS**: sampling evidence; no proof depends on it.

Scripts are in `y2py/`. Run each with `python3 -I <script>` from inside `y2py/`; the outputs are in the matching `.out` files. No assumption is added: every hypothesis beyond the axioms is stated in the result that uses it.

Read for this note:
- BRIEF19, AUDIT_X123, BRIEF18, AUDIT_nonlinear_programme;
- X1, X2 and X3 (X3.2);
- L3 (L3.1, L3.4, L3.6);
- B1 (link classes, transfer chains), Q1 Part I (gluing, (TC)), T1n (§§1–2);
- M3 §§0–1 (ladder normal form, M3.10);
- write-up §2;
- *Full Coverage by Homothetic Credal Families v3*: §§3–5 and App. C (Lemma bayes-necessary, Lemma three-world).

---

## 0. Outcome

**No cover of T1. Milestone 2 is answered as follows.** All four results are PROVED.

1. **Edge selections.**
   - Two edge families meet the precise vertex models and extend through T1 in the interior:
     - the **posterior** edges P: the odds band o·[1/A, A];
     - the **precise** edges D_p.
   - P is exactly the boundary of the two-step Brier "box" field with s₂/s₁ = A (Prop. Y2.3). So P has an *additive* shared boundary triple. Its interior is a box family, not T1.
2. **Compatibility lemma.** Three ingredients:
   - (K) at an edge involves only that edge's two regions (Lemma Y2.4).
   - In the class 𝒱 of worlds whose ladder acceptances form a convex cone, two edge cones that agree on the link class always amalgamate (Lemma Y2.5). The amalgam is consistent, conservative over each edge, and contains the union closed under realizable composition.
   - Explicit sufficient conditions (E1)–(E4) give every boundary axiom (Thm Y2.6):
     - no strict reversal;
     - protection of edge models;
     - no (C)-ties;
     - closed sections along each edge, vertices included.
3. **The exact obstruction: link-class rigidity (Thm Y2.8).** On the full domain the two edge chains at a vertex are *automatically transverse* on the link class; this is the (TC) that Q1 had to assume on M_U (Lemma Y2.1(c)). Suppose the partners have countably additive endorsers. Then:
   - **imprecise edges** (P, for example): any two endorsers of a world are proportional on all mixed pairs;
   - **precise edges**: only the *totals* are pinned. The silence/wrong split is free, subject to the mediant inequality φ_i + φ_j ≥ 1.

   Consequences:
   - Credal (unanimity) worlds collapse to additive ones on P (Cor. Y2.9).
   - Non-additive *two-world* credal systems exist on a P-edge (Example Y2.9′), but no two of them can be shared at a vertex. This is the audit's compatibility hazard, as a theorem.
4. **Construction (Thm Y2.10).** Take the precise edges and, at each world, the unanimity of two-step Brier fields whose silence split φ ranges over an admissible family. This triple:
   - satisfies every boundary axiom on the full domain;
   - is incomplete, so it is neither additive nor lexicographic.
5. **Attachment (Thms Y2.11, Y2.12).** Suppose T1 is competitive at u. Suppose also that each world has one strictly positive, countably additive two-step field endorsing both its edge comparisons and its comparisons out of T1. Then:
   - **precise edges: contradiction** (Y2.12);
   - **posterior edges:** the endorsers must be **half-edge blind**. Every edge's Bayes function K is constant on each half of the edge, jumping at the midpoint. Equivalently, every endorser ratio on Q_c jumps exactly at T1's coordinate-plane crossing levels t = A^{±1}, and q satisfies three linear relations.
     - Such endorsers exist (CHECKED: K ∈ {1/2, 2}, q = u).
     - The box field is not of this kind, so T1 is not Bayes there at any q (NUMERICS, consistent with the theorem).

**Nearby result (project preference).**
- Target (3), as stated, is reached only on precise edges, and Thm Y2.12 shows it cannot be attached to T1 while the worlds add up.
- On imprecise edges, the target is provably out of reach for credal worlds (Cor. Y2.9).
- The reachable statement that matters is the shape forced on any T1-compatible boundary:
  - either some world has **no** strictly positive countably additive endorser of its edge and T1 comparisons;
  - or the boundary is posterior-type with half-edge-blind endorsers, so that each world's order must be strictly finer than its endorser on the blind regions.
- §7 lists, from the proved results, what an interior extension must satisfy in each case.

---

## 1. Setting

**Domain and regions.**
- Use the full domain. For the general theorems, Lemma X3.0 lets us work on D\*: mixed pairs carry advice in {M, S, O}, unanimous pairs are correct, and × is absent. The construction (§5) is written directly on the full four-advice domain.
- For a.e. mixed pair, take its **majority orientation** h (two positive coordinates). Its odd world c = o(h) is the one with h_c < 0.
- Q_c is the set of pairs with odd world c. Write
  - R_ij := Q_i ∪ Q_j (the pairs with h_i h_j < 0);
  - the **link class** of world i is Q_i = R_ij ∩ R_ik (B1).
- On Q_c write h ∝ (−1, t_a, t_b) in coordinates (c, a, b), with t_a, t_b ∈ (0, ∞). Positions: M accepts h, S is silence, O accepts −h.
  - World c ranks O < S < M.
  - The majority worlds a, b rank M < S < O (X2.1).

**Ladder (M3.0).**
- A world-m field is a pair of measurable functions (s_m, w_m) > 0 on mixed pairs:
  - s_m is the **silence increment**, the cost of correct → silent;
  - w_m is the **wrong increment**, the cost of silent → wrong.
- Write τ_m := s_m + w_m and φ_m := s_m/τ_m ∈ (0,1) (the split).
- Fields are integrable. On unanimous pairs and on ×, any fixed strictly guiding integrable increments are used; they never enter the arguments below.
- L_m(X) := ∫ (cost of X's advice) dμ.
- A field **endorses** world m's comparisons out of C if C ⪯_m X implies L_m(C) ≤ L_m(X), for every model X.

**Steps on Q_c.**
- The odd world's silence step is the O–S step, and its wrong step is S–M.
- A majority world's silence step is M–S, and its wrong step is S–O.

**The boundary problem (B).** This is the "edge-model sub-domain" of the brief. It asks for:
- world orders ⪯_m on **all** models of the full domain, with strict (G) and (IB);
- a coherent selection p ↦ C_p on ∂Δ with C_{e_m} = B^m := {h : h_m > 0}, such that for p ∈ ∂Δ:
  - C_p is competitive on supp p against every model;
  - C_p is undominated;
  - no incoherent model ties C_p at every world;
  - every section {p ∈ ∂Δ : C_p ⪯_m X} is closed in ∂Δ, for every m and every X.

(B) is (S), protection and (C) restricted to boundary priors, with competitors unrestricted.

---

## 2. Milestone 1: edge selections

**Lemma Y2.1 (threshold form; PROVED).** Let p lie in the open edge (e_i, e_j) and let C_p be competitive on {i, j}.

- **(a)** C_p = D_{K_p} with K_p ⊆ [e_i, e_j] (X2.2(a), X3.2). Write K_p = {m : m_j/m_i ∈ [ℓ, r]}, with 0 ≤ ℓ ≤ r ≤ ∞. Then:
  - on Q_i: C_p is at O for t_j < 1/r, at S for 1/r ≤ t_j ≤ 1/ℓ, and at M for t_j > 1/ℓ;
  - on Q_j, with u := h_i/|h_j|: C_p is at M for u > r, at S for ℓ ≤ u ≤ r, and at O for u < ℓ;
  - on Q_k: C_p is at M (correct for both i and j);
  - on unanimous pairs: C_p is correct.

  So on each link class an edge model is a threshold set in **one** ratio, and it ignores the third coordinate.
- **(b)** The posterior family K_p = ν(p ⊙ T1) (X2.5) has, with o := p_j/p_i:
  - ℓ = o/A and r = Ao, where A := (c₀ + ε)/c₀ = (1 + 2ε)/(1 − ε). This is the write-up's κ.
  - The precise family has ℓ = r = o.
  - Both families are **regular sweeping** families: ℓ and r are C¹ bijections of (0, ∞) in o, with positive derivative. The posterior family is imprecise (ℓ < r); the precise one has ℓ = r.
- **(c) Automatic transversality.** On Q_i the edge-ij models depend only on t_j and the edge-ik models only on t_k. The image of μ|_{Q_i} under (t_j, t_k) is equivalent to Lebesgue measure on (0, ∞)². This is Q1's (TC) with G = (0,∞)², and it holds for **every** edge selection on the full domain.

*Proof.*
- (a) For m ∈ K_p, m·h = m_i h_i + m_j h_j. On Q_i this is m_i(−1 + (m_j/m_i) t_j), up to a positive factor. Acceptance of h needs (m_j/m_i) t_j > 1 for every m ∈ K_p, that is ℓ t_j > 1. Acceptance of −h needs r t_j < 1. Q_j is symmetric. On Q_k, h_i and h_j are both positive.
- (b) The odds m_j/m_i of p ⊙ v_k are o·v_{k,j}/v_{k,i}. These equal oA, o/A and o for k = j, i, and the third index.
- (c) The map h ↦ (h_j/|h_i|, h_k/|h_i|) is a smooth submersion of the open cone {h_i < 0 < h_j, h_k} onto (0,∞)², with ray fibres. The Gaussian density is positive. ∎

**Proposition Y2.2 (both families extend through T1; PROVED).**
- **(P)** K_p = ν(p ⊙ T1) on Δ: K_u = T1, its edges are P, its vertices are precise, and p ↦ K_p is Hausdorff-continuous (X2.5).
- **(D)** K_p := p + r(p)(T1 − u), with r(p) := min(1, 3 min_m p_m / ε):
  - T1 − u = ε(Δ − u), so K_p ⊆ Δ iff r ≤ 3 min_m p_m/ε;
  - K_u = T1;
  - K_p = {p} on ∂Δ;
  - p ↦ K_p is continuous.

Both families satisfy every constraint that X2.2 forces on a selection: edge support, precise vertices, vertex shrinking. Nothing is claimed here about interior competitiveness. ∎

**Proposition Y2.3 (the posterior boundary is additive; PROVED, CHECKED).** Let Ψ be the two-step Brier field with s_m = |h_m|, w_m = A|h_m|, and × penalty 2(1 + A)|h_m|. Then:
- its q-Bayes model at every q ∈ Δ is unique a.e. and equals D_{ν(q⊙[1,A]³)} (a normalised box);
- for q ∈ ∂Δ this is the posterior edge model;
- hence Full Coverage v3, Thm general, makes Ψ a full additive system;
- its interior selection is the box family. That family never contains T1 (L3.1(c)), so T1 is dominated in Ψ (Lemma bayes-necessary(b)).

*Proof.* On a mixed pair, accepting beats silence iff
Σ_{h_m>0} q_m h_m > A Σ_{h_m<0} q_m |h_m|,
that is, iff min over c ∈ [1, A]³ of Σ_m q_m c_m h_m > 0. Accepting also beats rejecting, because the sum then exceeds the negative part. The ties form a null set. On an edge, the odds of q ⊙ c range over o·[1/A, A]; compare Y2.1(b). ∎

CHECKED (`edges_check.out`, exact rationals, ε ∈ {1/10, 3/10, 3/5}):
- 6000 random edge instances each: posterior = unique box-Bayes advice, 0 mismatches;
- vertices exact;
- interior mismatches occur (41–57 of 3000);
- the threshold formulas of Y2.1 and the T1 position formulas below: 0 failures.

**T1 on Q_c (used repeatedly; PROVED, CHECKED).** With λ := ε/c₀ = A − 1:
- T1 is at M iff t_a + t_b > A;
- T1 is at O iff t_a + t_b + λ·max(t_a, t_b) < 1;
- T1 is at S otherwise.

The band B_c := {T1 at S} ⊆ (0,∞)² is connected, has nonempty interior, and projects onto (0, A) in each coordinate.

---

## 3. Milestone 2: the compatibility lemma

**Lemma Y2.4 (edge reduction; PROVED).** Let p lie in the open edge ij, with any world orders satisfying weak (G). Suppose C_p ⪯_i X′ or C_p ⪯_j X′ holds for every X′ that agrees with C_p off R_ij and has advice in {M, S, O} there. Then competitiveness of C_p on {i, j} holds against every model.

*Proof.* Given X, let X′ be X on R_ij with every × replaced by C_p's advice, and C_p elsewhere. C_p is correct for both i and j on Q_k and on unanimous pairs, and × is worst at every world. So X is pointwise weakly worse than X′ at both i and j. By weak (G) and transitivity, C_p ⪯_m X′ implies C_p ⪯_m X. ∎

**Class 𝒱.**
- On D\*, the ladder difference δ_m(r) ∈ L^∞(Γ) of a record r is
  - the change of the indicator "not correct" (silence step), and
  - the change of "wrong" (wrong step),

  pair by pair. Here Γ := mixed pairs × {s, w}.
- Realizable composition is addition of ladder differences (M3.0), and the m-worsenings are exactly δ_m ≥ 0.
- A world is in 𝒱 if A_m = {r : δ_m(r) ∈ 𝒦_m} for a convex cone 𝒦_m ⊆ L^∞(Γ) with 𝒦_m ⊇ L^∞₊ and 𝒦_m ∩ (−L^∞₊) = {0}.
- By the transition lemma (X1.1.1), every such A_m is a preorder with strict (G) and (IB).
- Members of 𝒱 include:
  - additive worlds;
  - credal unanimities of additive worlds;
  - lexicographic worlds;
  - the X2.7 rules.
- Not every world is in 𝒱: membership asks that the *posi* closure be consistent, which is the substantive extra condition stressed in AUDIT_nonlinear_programme.
- An **edge cone** 𝒦^{ij}_m (m ∈ {i, j}) is a cone in L^∞(Γ|R_ij) with the same two properties.

**Lemma Y2.5 (amalgamation over the link class; PROVED).** Let 𝒦^{ij} and 𝒦^{ik} be edge cones of world i. Suppose they agree on the link class:
𝒦^{ij} ∩ L(Q_i) = 𝒦^{ik} ∩ L(Q_i) =: 𝒜_i.
Put 𝒦_i := 𝒦^{ij} + 𝒦^{ik} + L^∞₊ (Minkowski sum, extending by 0). Then:
- **(a)** 𝒦_i ∩ (−L^∞₊) = {0}: the amalgam has no strict reversal.
- **(b)** 𝒦_i ∩ L(R_ij) = 𝒦^{ij} and 𝒦_i ∩ L(R_ik) = 𝒦^{ik}: the amalgam is conservative.
- **(c)** The union of the two edge record sets, closed under realizable composition, lies in {r : δ_i(r) ∈ 𝒦_i}. So it is consistent, and conservative over each edge.

*Proof.* Subscripts denote restrictions to Q_j, Q_i, Q_k.
- **(a)** Let a ∈ 𝒦^{ij}, b ∈ 𝒦^{ik}, ϖ ≥ 0, with a + b + ϖ ≤ 0.
  - On Q_j, a_j ≤ −ϖ_j ≤ 0. So a_i = a + (−a_j) ∈ 𝒦^{ij} (adding a positive element), hence a_i ∈ 𝒜_i. Likewise b_i ∈ 𝒜_i.
  - On Q_i, a_i + b_i ≤ −ϖ_i ≤ 0, and a_i + b_i ∈ 𝒜_i. Consistency gives a_i + b_i = 0 and ϖ_i = 0.
  - Then b_i = −a_i ∈ 𝒜_i ⊆ 𝒦^{ij}. So a_j = a + b_i ∈ 𝒦^{ij}, and a_j ≤ 0. Hence a_j = 0 and ϖ_j = 0. Symmetrically b_k = 0 and ϖ_k = 0.
  - So a + b + ϖ = 0.
- **(b)** Let c = a + b + ϖ be supported in R_ij.
  - Then b_k = −ϖ_k ≤ 0, so b_i = b − b_k ∈ 𝒦^{ik} ∩ L(Q_i) = 𝒜_i ⊆ 𝒦^{ij}.
  - Hence c = a + b_i + ϖ_i + ϖ_j ∈ 𝒦^{ij}.
- **(c)** A realizable composite of accepted records has ladder difference equal to the sum of theirs, which lies in 𝒦_i. ∎

The vector argument uses rearrangement of sums, so it needs the cone hypothesis. For worlds outside 𝒱 (closure under realizable composition only) it is open whether link agreement suffices (part (b) of Q_Y2, §8).

**Theorem Y2.6 (compatibility lemma; PROVED).** Fix an edge selection on ∂Δ with C_{e_m} = B^m. For each edge ij fix edge cones 𝒦^{ij}_i, 𝒦^{ij}_j. Assume:

- **(E1) Edge (K).** For p in the open edge and every X′ = C_p off R_ij: δ_i(rec(C_p, X′)) ∈ 𝒦^{ij}_i or δ_j(rec(C_p, X′)) ∈ 𝒦^{ij}_j.
- **(E2) Strong two-world protection.** For such X′: if δ_i(rec(X′, C_p)) ∈ 𝒦^{ij}_i and δ_j(rec(X′, C_p)) ∈ 𝒦^{ij}_j, then X′ = C_p.
- **(E3) Link agreement** at each world, as in Lemma Y2.5.
- **(E4) Closed amalgam sections.** For each m and X, {p ∈ ∂Δ : δ_m(rec(C_p, X)) ∈ 𝒦_m} is closed. This holds, for example, if each 𝒦_m is closed under L¹-convergence of uniformly bounded sequences, since C_p is continuous in measure along ∂Δ.

Then the amalgams 𝒦_1, 𝒦_2, 𝒦_3 solve (B). Conversely, every solution of (B) in 𝒱 satisfies (E1), (E3) and (E4) for its own restrictions 𝒦_m ∩ L(R_mn).

*Proof.*
- **Strict (G) and (IB):** by Lemma Y2.5(a) and X1.1.1.
- **(K):** by (E1), Lemma Y2.4, and 𝒦^{ij}_i ⊆ 𝒦_i. At a vertex, B^m is pointwise m-optimal.
- **Protection and (C).** Suppose X ⪯_m C_p at every world, with p in the open edge ij.
  - Let σ := δ_i(rec(X, C_p)). C_p is i-correct on Q_k, so σ_k ≤ 0. Hence σ − σ_k ∈ 𝒦_i, and it is supported in R_ij, so it lies in 𝒦^{ij}_i by Lemma Y2.5(b). The same holds for j.
  - (E2) then gives X = C_p on R_ij. So σ = σ_k ≤ 0 with σ ∈ 𝒦_i, hence σ = 0 and X = C_p.
  - At a vertex, X ⪯_m B^m forces X = B^m by strict (G).
- **Sections:** by (E4).
- **Converse:** immediate from the definitions. ∎

*Use.* Theorem Y2.6 reduces "three edge systems glue" to two kinds of check:
- the two-world checks (E1) and (E2), one edge at a time;
- the two global checks (E3) and (E4).

(E3) is where the obstruction lives (§4). Additive edge systems glue iff their densities are proportional on each link class (Y2.5, Y2.8).

---

## 4. The obstruction: link-class rigidity

**Lemma Y2.7 (edge pinning; PROVED).** Let edge ij carry a regular sweeping family, with odds band [ℓ(o), r(o)].
- Assume (K) on {i, j} at every p in the open edge.
- Assume that field (s_i, w_i) endorses world i's comparisons out of these edge models, and (s_j, w_j) endorses world j's.

Then there is a nondecreasing K_{ij} : (0, ∞) → (0, ∞) (the edge's **Bayes function**) such that every edge model C_p is a weak pointwise minimiser of L_i + K_{ij}(o) L_j. Moreover, a.e.:

- **Imprecise case (ℓ < r).**
  - On Q_i: s_i/w_j = K_{ij}(r⁻¹(1/t_j)) and w_i/s_j = K_{ij}(ℓ⁻¹(1/t_j)).
  - On Q_j: s_i/w_j = K_{ij}(r⁻¹(u)) and w_i/s_j = K_{ij}(ℓ⁻¹(u)).

  For P this means s_i/w_j = K(1/(A t_j)) and w_i/s_j = K(A/t_j) on Q_i.
- **Precise case.** τ_i/τ_j = K_{ij}(1/t_j) on Q_i and τ_i/τ_j = K_{ij}(u) on Q_j. Also the **mediant inequality** holds a.e. on R_ij:
  s_i s_j ≥ w_i w_j, equivalently φ_i + φ_j ≥ 1.

Here the pairs (s_i, w_j) and (w_i, s_j) are matched as on Q_i: i's silence step against j's wrong step, which is the same O–S boundary.

*Proof.*
- **Pareto.**
  - Suppose L_j(X) < L_j(C_p). Endorsement gives C_p ⋠_j X, so (K) gives C_p ⪯_i X, and endorsement gives L_i(C_p) ≤ L_i(X).
  - So no X is strictly better than C_p for both fields. By Full Coverage v3, Lemma bayes-necessary(b) (atomless, finite losses), C_p minimises αL_i + βL_j for some (α, β) ≥ 0, not both zero.
  - If α = 0, then C_p = B^j a.e., because the field is strictly guiding; but the thresholds of C_p are finite. So we may set κ(o) := β/α ∈ (0, ∞). This uses only finite losses and that the attainable loss set is convex, so the minimisation is pointwise a.e. (integrate the pointwise excess).
- **Pointwise inequalities on Q_i**, with weights (1, κ):
  - O ≤ S ⟺ s_i/w_j ≥ κ;
  - S ≤ M ⟺ w_i/s_j ≥ κ;
  - O ≤ M ⟺ τ_i/τ_j ≥ κ.

  (Costs: O ↦ κτ_j, S ↦ s_i + κ s_j, M ↦ τ_i.)
- **Imprecise case.**
  - Put o_B(h) := r⁻¹(1/t_j) < o_A(h) := ℓ⁻¹(1/t_j). Then C_{p(o)} is at O iff o < o_B(h), at S iff o_B ≤ o ≤ o_A, and at M iff o > o_A.
  - So, for each rational o, a.e.:
    - s_i/w_j ≥ κ(o) on {o_B > o};
    - s_i/w_j ≤ κ(o) and w_i/s_j ≥ κ(o) on {o_B < o < o_A};
    - w_i/s_j ≤ κ(o) on {o_A < o}.
  - **κ is nondecreasing.** For o′ < o close enough to o, the set {o′ < o_B < o < o_A} is non-null, because o_B, o_A are continuous in t_j with o_B < o_A. On it κ(o′) ≤ s_i/w_j ≤ κ(o). Chaining gives the claim for all o′ < o.
  - Let K be the monotone function κ. Then a.e. s_i/w_j ∈ [K(o_B⁻), K(o_B⁺)] and w_i/s_j ∈ [K(o_A⁻), K(o_A⁺)].
  - K has countably many jumps. Their preimage is a countable union of level sets {t_j = const}, which is null. This gives the formulas on Q_i.
  - Q_j is the same computation with weights (1, κ): M ≤ S ⟺ s_i/w_j ≥ κ and S ≤ O ⟺ w_i/s_j ≥ κ, and C_p is at M iff o < r⁻¹(u).
  - The same κ(o) serves both steps and both regions, because it is attached to p.
- **Precise case.**
  - The same argument with the single O|M threshold gives τ_i/τ_j = K(1/t_j).
  - On {C_p = O}, also s_i/w_j ≥ κ. On {C_p = M}, also w_i/s_j ≤ κ.
  - At continuity levels this gives s_i/w_j ≥ K ≥ w_i/s_j, that is, s_i s_j ≥ w_i w_j. In terms of splits, φ_iφ_j ≥ (1 − φ_i)(1 − φ_j). ∎

**Theorem Y2.8 (link-class rigidity; PROVED).** Let both edges at e_i carry regular sweeping families of the same type (both imprecise or both precise), with (K) on them. Let (s_j, w_j) endorse world j's comparisons out of edge-ij models, and (s_k, w_k) endorse world k's out of edge-ik models. Let ω = (s_i, w_i) and ω̃ = (s̃_i, w̃_i) both endorse world i's comparisons out of the models of both edges.

- **(a) Imprecise edges.** ω̃ = c·ω a.e. on all mixed pairs, for a constant c > 0, at both steps.
- **(b) Precise edges.** τ̃_i = c·τ_i on all mixed pairs. Every endorser's split obeys the mediant inequality against each partner endorser, and nothing more is forced on it by these edges.
- **(c) Pinning identity (imprecise).** On Q_i, the partners' endorsers have product-form ratios:
  - w_j/w_k = K_{ik}(o_B^{ik}(t_k)) / K_{ij}(o_B^{ij}(t_j));
  - s_j/s_k = K_{ik}(o_A^{ik}(t_k)) / K_{ij}(o_A^{ij}(t_j)).

*Proof.*
- **(a)**
  - By Lemma Y2.7 on edge ij, s̃_i/s_i = (s̃_i/w_j)/(s_i/w_j) is a.e. a function of t_j on Q_i. By the lemma on edge ik, it is a function of t_k.
  - By Lemma Y2.1(c) and Fubini, a function of t_j that equals a.e. a function of t_k on (0,∞)² is a.e. constant. So s̃_i = c_s s_i on Q_i, and likewise w̃_i = c_w w_i.
  - Then K̃_{ij} = c_s K_{ij} a.e. through the B-levels, and K̃_{ij} = c_w K_{ij} through the A-levels. The level maps are C¹ diffeomorphisms, so these are a.e. statements in o. Hence c_s = c_w =: c.
  - On Q_j, s̃_i/w_j = K̃_{ij}(level) = c·s_i/w_j, so s̃_i = c s_i. Likewise w̃_i = c w_i. Q_k is the same through edge ik, with the same c, since the constant is fixed on Q_i.
- **(b)** The same argument applied to τ.
- **(c)** Divide the two edge formulas of Lemma Y2.7 on Q_i. ∎

*Comparison with Q1.* Q1.22 needed (TC) and partners with (RL-2), and pinned one step on M_U. Here:
- transversality is automatic (Y2.1(c));
- both ladder steps are pinned;
- the conclusion holds on the whole link class, not only off the chain ends.

The only freedom left is the precise-edge split.

**Corollary Y2.9 (credal worlds collapse on imprecise edges; PROVED).** Suppose that on comparisons out of boundary models, each world's order is the unanimity of a family W_m of strictly positive integrable two-step fields, and the edges are imprecise and regular sweeping (for instance P). Then each W_m is a single ray on mixed pairs. So no non-additive credal triple has posterior edges.

*Proof.* Every member is an endorser; apply Y2.8(a). ∎

**Example Y2.9′ (two-world credal systems exist but cannot be shared; PROVED, CHECKED).** On one P-edge [e_i, e_j], let Ψ and Ψ′ be positive bounded functions bounded away from 0, with Ψ/Ψ′ nondecreasing.
- **Members.** Multiply each step weight of the box field by Ψ (world i) or Ψ′ (world j), evaluated at that step's level in o:
  - on Q_i the levels are 1/(A t_j) and A/t_j;
  - on Q_j the levels are A u and u/A.
- **Pinning.** Then s_i/w_j = K(level) and w_i/s_j = K(level), with K(o) := o·Ψ(o)/Ψ′(o) strictly increasing. So every member pair has the posterior edge model as its unique pointwise minimiser at weights (1, K(o)).
- **Two-world system.** Take 𝒫_i := {1, 1 + 1[o > 1]} and 𝒫_j := {1, 1 + 1[o < 1]}. The unanimities over these families satisfy (K), protection, (C) and closed sections on the edge. They are non-additive: world i's two members have first-step ratio ∈ {1, 2}, a non-constant function of t_j.
- **Not shareable.** By Y2.8(a), world i cannot keep both members at a vertex where its other partner is endorsed.

CHECKED: `two_world_credal.out` — 20 000 exact member/prior/pair triples, 0 failures; the member ratio is non-constant. So "two-world existence theorems do not show that the two appearances of each world agree" (AUDIT_X123) is a theorem here, not only a hazard.

---

## 5. Milestone 3: a jointly compatible non-additive triple (precise edges)

**Admissible split families.** For each world m, fix a nonempty family Φ_m of measurable φ : H → (0, 1) satisfying:

- **(Med)** for every edge {i, j} and all φ_i ∈ Φ_i, φ_j ∈ Φ_j: φ_i(h) + φ_j(h) ≥ 1 for a.e. h ∈ R_ij.

There is no constraint on Q_k for edge ij, and none on unanimous pairs.

Examples:
- **(U)** Φ_m = {φ ≡ 1/2, φ ≡ 9/10}, or all measurable φ with values in [1/2, 19/20].
- **(R)** On Q_c: φ_c ∈ [1/5, 3/10] for the odd world, and φ_a, φ_b ∈ [4/5, 9/10] for the majority worlds. Silence is cheap for the odd world and dear for the majority.

**Member penalty and world order.**
- ℓ^φ_m(h, a) := |h_m|·(0, φ(h), 1, 2), according as a is correct, silent, wrong or ×.
- X ⪯_m Y :⟺ L^φ_m(X) ≤ L^φ_m(Y) for every φ ∈ Φ_m.

**Selection.** C_p := D_p (precise) for p ∈ ∂Δ, and C_{e_m} = B^m.

**Theorem Y2.10 (PROVED; CHECKED).** On the full four-advice domain:

- **(a) Order axioms.** Each ⪯_m is a preorder with strict (G) and (IB).
- **(b) Competitiveness.** Each C_p, p ∈ ∂Δ, is competitive on supp p against every model.
- **(c) Protection and (C).** If p ∈ (e_i, e_j) and X ⪯_i C_p and X ⪯_j C_p, then X = C_p a.e. Likewise X ⪯_m B^m forces X = B^m. So every boundary model is undominated, and no other model ties one at every world.
- **(d) Closed sections.** For every model X and world m, {p ∈ ∂Δ : C_p ⪯_m X} is closed, vertices included.
- **(e) (LA).** B^m is coherent and undominated.
- **(f) Not additive, not lexicographic.** If some Φ_m has two members differing on a non-null set, then ⪯_m is incomplete. Hence it is neither additive nor lexicographic over linear functionals, since both of those are total.
- **(g)** The edge selection is the boundary of the T1-selection (D) of Prop. Y2.2.

*Proof.*
- **(a)** Every member is strictly increasing in world-m rank, with integrable envelope 2|h_m|. So a pointwise strict improvement lowers every member, and the unanimity has strict (G). Each member is additive, so the four comparisons in an (IB) instance agree member by member.
- **Pointwise lemma.** Let p ∈ (e_i, e_j), φ_i ∈ Φ_i, φ_j ∈ Φ_j. For a.e. h, D_p's advice is the **unique** minimiser over {+, 0, −, ×} of p_i ℓ_i + p_j ℓ_j.
  - If h_i h_j > 0, both worlds have the same correct advice, and it is uniquely best.
  - Otherwise, say h_i > 0 > h_j. The costs are:
    - +: p_j|h_j|;
    - −: p_i h_i;
    - 0: p_iφ_i h_i + p_jφ_j|h_j|;
    - ×: more than both of the first two.
  - If p_i h_i > p_j|h_j|, then by (Med)
    cost(0) − cost(+) = p_iφ_i h_i − p_j(1 − φ_j)|h_j| ≥ φ_i(p_i h_i − p_j|h_j|) > 0.
    The other case is symmetric. Ties lie on {p·h = 0}, which is null.
- **(b)** Suppose C_p ⋠_i X and C_p ⋠_j X. Then some members φ_i, φ_j have L^{φ_i}_i(X) < L^{φ_i}_i(C_p) and L^{φ_j}_j(X) < L^{φ_j}_j(C_p). Integrating the pointwise lemma gives p_iL_i + p_jL_j (X) ≥ (C_p), a contradiction. At a vertex, B^m is pointwise m-optimal for every member.
- **(c)** Fix any members. Both inequalities give p_iL_i(X) + p_jL_j(X) ≤ p_iL_i(C_p) + p_jL_j(C_p). Uniqueness in the pointwise lemma gives X = C_p.
- **(d)** For a.e. h, p ↦ sign(p·h) is locally constant on ∂Δ off at most three points. So p ↦ C_p is continuous in measure on ∂Δ, including D_p → B^i at the vertices. Dominated convergence makes p ↦ L^φ_m(C_p) continuous. The section is ⋂_φ {p : L^φ_m(C_p) ≤ L^φ_m(X)}, which is closed.
- **(e)** By (c).
- **(f)** Take φ⁻ < φ⁺ on a non-null set S′ of mixed pairs. Let X be B^m silent on a subset S ⊆ S′, and Y be B^m wrong on a disjoint set W.
  - With a := ∫_S |h_m| and b := ∫_W |h_m|, the members' losses are ∫_S φ|h_m| and b.
  - Choose S inside a set where φ⁻ ≤ θ < θ′ ≤ φ⁺, and W so that b ∈ (θ a, θ′ a). Then neither X ⪯_m Y nor Y ⪯_m X.
- **(g)** Prop. Y2.2(D). ∎

CHECKED (`credal_precise.out`, exact rationals):
- the pointwise lemma on 20 000 random edge instances for each of (U) and (R), with members drawn independently per pair, 0 failures;
- vertices exact;
- with φ_i + φ_j < 1, silence is the strict edge minimiser in 6243 of 20 000 trials, so (Med) is necessary for (b);
- an explicit incomparable pair;
- a 60-cell empirical model with 400 random competitors: 0 failures of (K) and of protection.

**Remarks.**
- **A plan on ∂Δ.** For each (p, m, X), the rejected set ∂Δ ∖ {section} = ⋃_φ {p : L^φ_m(C_p) > L^φ_m(X)} is an explicit union of open sets, the same for every fragment. So Y2.10 supplies a fixed reservation plan on the boundary in the sense of X1.3.3; compare milestone 3 of BRIEF19.
- **Vertex domination at the boundary.** The edge form of X2.2(c) holds automatically. Near e_k on edge kj, world k accepts C_p ⪯_k B^k ⊕ S(P), because L^φ_k(C_p) → L^φ_k(B^k) < L^φ_k(B^k) + φ⁻∫_P|h_k|.
- **No X2.9-type obstruction.** At the boundary no symmetry is assumed, so X2.9 does not apply.
- **Consistency with rigidity.** All members have the same totals |h_m| and satisfy (Med), as Y2.8(b) requires.

---

## 6. Attaching T1: what the boundary forces

Throughout this section T1 is competitive on Ω at u. Only that one instance of (K) is used, and nothing else about the interior.

**Hypothesis (End).** Each world m has a strictly positive integrable two-step field (s_m, w_m) that endorses world m's comparisons out of the models on both edges at e_m, **and** its comparisons out of T1.

Under (End), (K) at u and Lemma bayes-necessary(b) make T1 a weak pointwise q-Bayes act of (L_1, L_2, L_3) for some q ∈ Δ.

Bayes inequalities on Q_c at weight q:
- M ≤ S ⟺ q_c w_c ≤ q_a s_a + q_b s_b;
- S ≤ O ⟺ q_c s_c ≤ q_a w_a + q_b w_b.

**Theorem Y2.12 (precise edges cannot carry T1 under (End); PROVED, NUMERICS).** Suppose all three edges are precise (C_p = D_p on ∂Δ) and (K) holds there. Then (End) and the competitiveness of T1 at u are incompatible.

*Proof.*
- **Step 1: the band forces equality.** Fix c and put x := q_aτ_a, y := q_bτ_b, z := q_cτ_c. By Lemma Y2.7 (precise case) on edges ca and cb, φ_a ≥ 1 − φ_c and φ_b ≥ 1 − φ_c a.e. on Q_c. On T1's band B_c, T1 is at S, so S ≤ M and S ≤ O:
  - (1 − φ_c)(x + y) ≤ φ_a x + φ_b y ≤ (1 − φ_c) z;
  - φ_c z ≤ (1 − φ_a)x + (1 − φ_b)y ≤ φ_c(x + y).

  Since 0 < φ_c < 1, this gives z = x + y a.e. on B_c, that is,
  q_c τ_c = q_a τ_a + q_b τ_b.
- **Step 2: q is interior.** If q_b = 0, the identity on B_b ⊆ Q_b reads 0 = q_cτ_c + q_aτ_a > 0. So q is interior.
- **Step 3: the Bayes functions are constant.**
  - Divide by τ_c and use τ_c/τ_a = K_{ca}(1/t_a) (Lemma Y2.7): a.e. on B_c,
    q_a/K_{ca}(1/t_a) + q_b/K_{cb}(1/t_b) = q_c.
  - Both summands are nondecreasing functions of one variable, and B_c is connected open with projections (0, A). So both are constant there:
    - K_{ca} = k_{ca} on (1/A, ∞);
    - K_{cb} = k_{cb} on (1/A, ∞);
    - q_c = q_a/k_{ca} + q_b/k_{cb}.
  - The same on Q_a, with K_{ac}(o′) = 1/K_{ca}(1/o′), gives K_{ca} constant on (0, A). The two ranges overlap, so K_{ca} ≡ k_{ca}.
- **Step 4: the linear system has no positive solution.**
  - Q_a gives q_a = q_c k_{ca} + q_b/k_{ab}.
  - Q_c times k_{ca} gives q_c k_{ca} = q_a + q_b k_{ca}/k_{cb}.
  - Subtracting: q_b(k_{ca}/k_{cb} + 1/k_{ab}) = 0, so q_b = 0, contradicting Step 2. ∎

NUMERICS (`t1_attach.out` (C)): 12 random pinned field triples (random monotone step K, random splits obeying (Med)). For every q on a 496-point grid, a T1 band pair violates weak q-Bayes.

**Corollary Y2.13 (attaching T1 to the triple of Y2.10; PROVED).** Let a ranking have the boundary selection D_p and T1 = C_u. Suppose its world orders agree with Thm Y2.10's on comparisons out of boundary models. If T1 is competitive at u, then some world m has **no** strictly positive integrable two-step field endorsing both its boundary comparisons and its comparisons out of T1. In particular:
- the members of Φ_m cannot endorse world m's T1-comparisons;
- T1 is not competitive at u in the triple itself.

**Where the freedom is (PROVED, elementary).** Precise boundary models are never silent on mixed pairs. So a record out of T1 that starts at S on a non-null part of T1's band is not realizable out of any boundary model. By (IB), the boundary fixes no verdict on it. The non-endorsable acceptances that Y2.13 demands can therefore sit on silence-starting records of T1's band, or on composites of them. This is the L3.6(b) "precise-edge escape", made specific: it requires a world that does not add up with a strictly positive countably additive weight.

**Theorem Y2.11 (posterior edges force half-edge blind endorsers; PROVED, CHECKED).** Suppose all three edges are posterior (P), (K) holds there, (End) holds, and T1 is competitive at u. Then:

- **(a)** T1's Bayes weight q is interior.
- **(b)** Every edge Bayes function is two-valued: K_{xy} = k^<_{xy} on (0, 1) and k^>_{xy} on (1, ∞), with k^< ≤ k^>. Equivalently, on Q_c:
  - s_c/w_a = k^>_{ca} for t_a < 1/A, and k^<_{ca} for t_a > 1/A;
  - w_c/s_a = k^>_{ca} for t_a < A, and k^<_{ca} for t_a > A.

  The jumps sit exactly at the levels where T1's boundary meets the coordinate plane h_b = 0. The jump in o is at the midpoint edge model, the one that coincides with T1 on that plane.
- **(c)** For each c, with {a, b} the other two worlds:
  q_c = q_a/k^>_{ca} + q_b/k^>_{cb},
  where k^>_{ac} = 1/k^<_{ca}.
- **(d) Half-edge blindness.** The weighted endorser loss L_x + k^>_{xy} L_y is the same for all edge models with o > 1, and L_x + k^<_{xy} L_y is the same for all with o < 1.
- **Converse.** For any two-valued K's with k^< ≤ k^> and any q satisfying (c), the fields
  - (s_c, w_c) := (|h_c|, A|h_c|) on Q_c,
  - s_a := w_c/K_{ca}(A/t_a), w_a := s_c/K_{ca}(1/(A t_a)), and likewise for b,

  make every posterior edge model a weak pairwise Bayes act and T1 a weak q-Bayes act. Solutions exist: K_{xy} ∈ {1/2, 2} on every edge, with q = u.
- **The box field** (K(o) = o) is not of this form. So T1 is q-Bayes for no q in the box system (consistent with Prop. Y2.3).

*Proof.*
- **Set-up.** By Lemma Y2.7, on Q_c:
  - s_c/w_a = K_{ca}(1/(At_a)) and w_c/s_a = K_{ca}(A/t_a).
  - Put H(s) := 1/K(1/s), which is nondecreasing, and Ψ(s₁, s₂) := q_a H_{ca}(s₁) + q_b H_{cb}(s₂).
  - Then M ≤ S ⟺ q_c ≤ Ψ(t/A), and S ≤ O ⟺ q_c ≤ Ψ(At).
- **The forced equality.**
  - T1's M-region gives Ψ ≥ q_c on {s₁ + s₂ > 1}.
  - T1's O-region gives Ψ ≤ q_c on {At : t_a + t_b + λ max < 1} = {min(s) + A·max(s) < A}.
  - Their intersection 𝒪 is open and connected, and both its projections are (0, 1), because A/(1 + A) > 1/2. So Ψ = q_c on 𝒪.
  - Hence q_a H_{ca} and q_b H_{cb} are constant on (0, 1).
- **(a)** If q_b = 0, then on Q_b one gets Ψ_b = q_c H_{bc} + q_a H_{ba} > 0 = q_b on 𝒪_b. So q is interior.
- **(b)** H_{ca} is constant on (0, 1), so K_{ca} is constant on (1, ∞). From Q_a, K_{ac} is constant on (1, ∞), so K_{ca} is constant on (0, 1). Monotonicity gives k^< ≤ k^>.
- **(c)** The constant value on 𝒪.
- **(d)** Two edge models with o, o′ on the same side of 1 differ only on pairs whose level lies between o and o′. On those pairs the relevant ratio equals that side's constant, which is a pointwise tie at the stated weights.
- **Converse.**
  - With these fields, Ψ = q_c on (0, 1)², and Ψ ≥ q_c everywhere, since H = 1/k^< ≥ 1/k^> above 1.
  - **T1 is a weak q-Bayes act.** Every inequality holds:
    - on T1's band: t/A ∈ (0,1)², and S ≤ O always;
    - on T1's O-region: At ∈ (0,1)², with O ~ S ~ M tied;
    - on T1's M-region: M ≤ S and M ≤ O.

    Here O ≤ M reads w_cΨ(t/A) + s_cΨ(At) ≤ q_c τ_c.
  - **Edge models are weak pairwise Bayes acts.** By the three pointwise criteria of Lemma Y2.7 with K nondecreasing. ∎

CHECKED (`t1_attach.out` (A)), exact, flat K ∈ {1/2, 2}:
- T1 is a weak u-Bayes act on 20 000 random pairs, 0 failures;
- the posterior edge models are weak pairwise Bayes acts on 20 000 trials, 0 failures.

NUMERICS (`t1_attach.out` (B)):
- box field: of 496 grid points q, none makes T1 q-Bayes on 3000 sample pairs;
- flat field: exactly one grid point does, namely q = u, as (c) predicts.

**Relation to M3.10.** M3.10 uses all the axioms and (NC). It concludes that every endorser tuple of a cover is degenerate: some increment vanishes on a non-null set. Y2.11 and Y2.12 use only:
- (K) on ∂Δ;
- (K) at u;
- (End).

Under these weaker hypotheses:
- with precise edges, strictly positive endorsers are impossible;
- with posterior edges, they must be half-edge blind.

The flat endorsers of Y2.11 are strictly positive. They therefore escape Y2.12 but not M3.10, which is not contradicted: the flat fields need not have coherent Bayes models at interior t ≠ u, which M3.4's (γ₀) requires.

---

## 7. What an interior extension must satisfy to attach

Everything below is a consequence of §§4–6; no new claim.

**To the precise-edge triple of Y2.10:**
1. **Agree with the boundary.** Its verdicts on records realizable out of boundary models are fixed, by (IB).
2. **Non-endorsement (Y2.13).** At some world, the accepted comparisons out of T1 admit no strictly positive countably additive two-step endorser compatible with that world's boundary comparisons. The room for this is the silence-starting records on T1's band.
3. **Closed sections across ∂Δ.**
   - If C_{p_n} ⪯_m X for interior p_n → p ∈ ∂Δ, then C_p ⪯_m X must hold in the boundary orders. Its complement is the explicit open union of Remark (plan).
   - In particular, the vertex-domination acceptances X2.2(c) at interior p near each vertex.
4. **Interior selection.** The selection is shrinking to precise models at ∂Δ, for example Y2.2(D).

**To posterior edges with adding-up worlds:**
1. **Unique endorsers.** By Y2.8(a), the endorsers are unique up to scale.
2. **Half-edge blindness.** By Y2.11, they must be half-edge blind, with the jump at the midpoint and q satisfying (c).
3. **Finer orders.** The world orders must be strictly finer than these endorsers on the blind regions. Protection of the edge models must come from comparisons the endorsers tie, which is the next ladder level (M3).
4. **No credal design.** By Y2.9, such a boundary cannot be credal.

**Either way.** A boundary compatible with T1 needs, at some world, either
- an order without strictly positive countably additive endorsement (precise edges, or posterior edges without (End)), or
- maximally tied endorsers.

The additive box boundary (Y2.3) and every credal boundary are excluded as attachments.

---

## 8. Status

| Item | Statement | Label |
|---|---|---|
| Y2.1 | threshold form of edge models; P and D are regular sweeping; automatic transversality on Q_i | PROVED |
| Y2.2 | P and D both extend through T1 (posterior; shifted contamination) | PROVED |
| Y2.3 | P = boundary of the two-step box Brier field (s₂/s₁ = A); additive boundary triple; T1 dominated there | PROVED; CHECKED |
| Y2.4 | edge (K) reduces to R_ij | PROVED |
| Y2.5 | amalgamation of link-agreeing edge cones in 𝒱 (consistent, conservative, contains the composition closure) | PROVED |
| Y2.6 | compatibility lemma (E1)–(E4) ⇒ boundary problem (B); (E1), (E3), (E4) necessary in 𝒱 | PROVED |
| Y2.7 | edge pinning by endorsers (imprecise: both steps; precise: totals + mediant) | PROVED |
| Y2.8 | link-class rigidity; pinning identity | PROVED |
| Y2.9 | credal worlds collapse on imprecise edges | PROVED |
| Y2.9′ | two-world credal edge systems on P exist and are not shareable | PROVED; CHECKED |
| **Y2.10** | **precise-edge split-credal triple: every boundary axiom; incomplete; not lexicographic** | **PROVED; CHECKED** |
| **Y2.12** | **precise edges + (End) + T1 competitive at u: impossible** | **PROVED; NUMERICS** |
| Y2.13 | attaching T1 to Y2.10 needs a non-endorsable world | PROVED |
| **Y2.11** | **posterior edges + (End) + T1 at u ⇒ half-edge blind endorsers; converse; example exists; box fails** | **PROVED; CHECKED; NUMERICS** |
| Q_Y2 | see below | open |

**Q_Y2 (single open question).** Is there a boundary triple solving (B) with posterior edges, such that:
- its endorsers are the half-edge blind fields of Y2.11, or some world has no endorser at all;
- its orders are not lexicographic over those endorsers?

This splits into two parts:
- **(a)** This is the only shape left for a T1-compatible boundary with imprecise edges.
- **(b)** For worlds outside 𝒱, does link agreement alone make the union, closed under realizable composition, consistent?

CONJECTURE: (b) can fail outside 𝒱, since comparative-probability orders without posi-consistency are the natural candidates; but no example has been constructed.

**Referee priorities.**
1. Lemma Y2.7: monotonicity of κ, and the jump-level null-set argument.
2. Theorem Y2.11, step "Ψ = q_c on 𝒪": the projections of 𝒪 and its connectedness.
3. Theorem Y2.12, Step 1: the use of (Med) on both edges at c.
4. Lemma Y2.5(a): the order of the cancellations.

**Files (`y2py/`).**
- `common.py`: exact helpers.
- `edges_check.py` / `.out`: Prop. Y2.3, Lemma Y2.1, T1 formulas.
- `credal_precise.py` / `.out`: Thm Y2.10 pointwise lemma, necessity of (Med), incomparability, cell-model sanity.
- `two_world_credal.py` / `.out`: Example Y2.9′.
- `t1_attach.py` / `.out`: Thm Y2.11 (flat example, box), Thm Y2.12 numerics.
