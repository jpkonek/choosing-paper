# M1. The degenerate fixed points: they exist in every remaining case (the T1-shadow), and what a ranking must do to realise them

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up or
refereed notes mark proved, each named), **CHECKED** (a step-by-step reading, not a re-derivation), **CONJECTURE**,
**NUMERICS** (`m1py/`, run with `python3 -I` from inside `m1py/`; no proof rests on them). No assumption is added.
Notation: write-up §§2–4, §7.7; L4 §1 (fixed point, endorser tuple, (NC), (γ₀), Λ_k, B_q, Z_q); K3 §1–§2; H1 §§1–3.
n = 3, U = D_{K′}, K′ = u + s(T1 − u), M = mixed part of U, N₊ = nonnegative part, σ_k = sign g_k,
P_k = U ∩ {g_k > 0}, E_k(X) = X △ P_k. Q_l = sign class with odd world l (Q₁ = (+,−,−) ∪ (−,+,+), Q₂ = (−,+,−) ∪ (+,−,+),
Q₃ = (−,−,+) ∪ (+,+,−)), R_ij = Q_i ∪ Q_j (where worlds i, j disagree). (H_U) = strict (G), (IB), (LA), (S) with closed
sections for every model, (C), T1 ∈ C_L, on M_U.

---

## 0. Outcome

**At the level of the fixed-point field, every remaining degenerate case is settled POSITIVELY. So the impossibility
for T1 on M_U cannot be completed through the fixed point of L4.1. T1 is not settled. What is new at the ranking level
is this: the realisation the brief proposes ("strict (G) with zero exchange rate on the blind sets") is impossible for
the canonical degenerate field. Any realisation needs a world mechanism that no known full system has.**

1. **Theorem M1.1 (the T1-shadow; PROVED, elementary).** Let ρ_k := 1 on R⁰_k := M ∖ E_k(T1), the problems where T1 is
   right at world k, and ρ_k := 0 on E_k(T1) ∩ M. Then the field c^T := (ρ_kσ_k)_k has the following properties.
   - **Bayes models.** c^T ≠ 0 a.e., and B_q = T1 for **every** q ∈ Δ°. So (γ₀) holds, every B_q is coherent, and no
     weighting is exceptional.
   - **Target.** T1 is c^T-Bayes at **every** p* ∈ Δ (interior points, open edges, vertices), and d_t(c^T) = 0 for
     every t ∈ Δ.
   - **Blind sets.** Λ_k = E_k(T1) ∩ M at each world. They are three, pairwise intersecting in the non-null sets
     J_l = E_i(T1) ∩ E_j(T1) ∩ M, and each touches every facet arc of D_{T1}.

   Conversely, T1 is c-Bayes at every weighting iff it is c-Bayes at the three vertices, iff every world is blind on
   its T1-error set. A variant for the vertex case under (B1) (ρ₂, ρ₃ > 0) is c = (0, σ₂, σ₃).

   So cases (a) (three blind worlds, including blind sets on the same facet arcs) and (b) (edges and vertices) both
   have explicit degenerate fields. The field c^T even satisfies (BU) with K_q ≡ T1, except for strict signs.
   Theorem main and M0closed(a) are therefore sharp in their strict-sign hypothesis.
2. **Proposition M1.2 ((V) under (B1); PROVED).** If p* = e₁ and ρ₂, ρ₃ > 0, then e₂ ∈ K₁ and e₃ ∈ K₀. Hence
   Λ₁ ⊇ M ∩ {g₁ > 0}: world 1 is blind on **every** problem where it advises acceptance. Off Λ₁ it sees only part of
   {g₁ < 0} ∖ cl D_{T1}.
3. **Ranking-level theorems (PROVED).**
   - **Lemma M1.3 (face KKM with strict (G)).** For every regular X and every face I, some selected C ⪯_i X (i ∈ I)
     either equals X or fixes some of X's errors at **every** i ∈ I.
   - **Theorem M1.7 (the edge exchange, in every cover).** For each pair {i, j}, there are non-null
     F_i ⊆ E_i(T1) ∩ R_ij and F_j ⊆ E_j(T1) ∩ R_ij with ν_i(F_i) ≥ ν_i(F_j) and ν_j(F_j) ≥ ν_j(F_i) for **every**
     endorser of world i and of world j.
   - **Theorem M1.9 (zero exchange rate at an edge).** Suppose worlds i, j have countably additive endorsers, and T1
     restricted to R_ij is an edge-(i, j) Bayes model of them, with ties toward one vertex. Then (H_U) is
     contradictory.
4. **Consequences for the realisation (PROVED).**
   - In a cover whose fixed point is the T1-shadow, the maximal endorser of **every** world has a purely finitely
     additive part that charges E_i(T1) ∩ R_ij, for both j ≠ i. So no world has a countably additive maximal endorser.
   - L2's blind-set device yields worlds with a countably additive endorser (L2.4(b)). Its trades also have the wrong
     orientation: the blind set is their negative part, whereas the shadow needs it as their positive part. So L2's
     device cannot realise the shadow.
   - The edge case realised at zero exchange rate needs a **two-sided tie shell**: a frozen density ratio along every
     R_ij-arc of some facet.
5. **The precise open question (Q_M1, §5).** Is there a full system whose maximal endorser field is the T1-shadow? By
   item 4 its worlds must be "tilted towards an end inside their own T1-error set", with closed sections. K3.3's
   tilted world is the only known mechanism with the needed endorser behaviour, and it violates closed sections.

| | Statement | Label |
|---|---|---|
| M1.1 | T1-shadow: degenerate field with (γ₀), all B_q = T1, T1 Bayes at every p* ∈ Δ; converse characterization | PROVED; NUMERICS |
| M1.1′ | (V) variant (0, σ₂, σ₃) under (B1) | PROVED; NUMERICS |
| M1.2 | (V) under (B1): e₂ ∈ K₁, e₃ ∈ K₀, Λ₁ ⊇ M ∩ {g₁ > 0} | PROVED; NUMERICS |
| M1.10 | edge limits of the fixed point are coherent; with pairwise-null blind sets they lie between e_i and e_j | PROVED |
| M1.11 | exact shadow-blindness at one world next to a world that sees J_j is impossible (field level) | PROVED |
| L1.D | (L1 §6.3) pairwise-null blind sets with p* ∈ Δ° are impossible | CONJECTURE (§2.4) |
| M1.3 | face KKM with strict (G) | PROVED |
| M1.4 | Pareto-tie principle; M1.5: tie-broken Bayes models and lexicographic edge models are selected | PROVED |
| M1.6 | Y_k := T1 △ J_k is incoherent; facet-plane lemma | PROVED; NUMERICS |
| M1.7 | edge exchange in every cover | PROVED |
| M1.8 | no world has a countably additive endorser blind on E_i(T1) ∩ R_ij and positive on E_j(T1) ∩ R_ij | PROVED |
| M1.9 | zero exchange rate + T1 edge-Bayes on R_ij ⇒ no cover; shadow and edge-case corollaries | PROVED; NUMERICS |
| Q_M1 | a full system realising the shadow | open |

---

## 1. Objects

- **Fixed point (L4.1).** Under (H_U) with (NC) at every world, every endorser tuple ν has countably additive parts
  ρ_k ≥ 0 (densities). The field c = (ρ_kσ_k) has:
  - (γ₀): d_t(c) = 0 for every t ∈ Δ, boundary included (L4.1.1 with L4.0);
  - every B_q, q ∈ Δ°, coherent when c ≠ 0 a.e. (L4.1.2);
  - T1 = B_{p*} ∪ S with S ⊆ Z_{p*}, for some p* ∈ Δ (L4.1.3).

  Λ_k := {ρ_k = 0} ∩ M. "Degenerate" means some Λ_k is non-null, or p* ∈ ∂Δ.
- **Admissible set.** A(c) := {p ∈ Δ : s_T(g) p·c(g) ≥ 0 for a.e. g ∈ M}, where s_T = +1 on D_{T1} and −1 off it.
  - It is closed and convex, and T1 is c-p-Bayes iff p ∈ A(c).
  - A convex subset of ∂Δ lies in one closed edge. So a degenerate configuration with A(c) ∩ Δ° = ∅ has A(c) a vertex
    (case (V)) or a segment of one closed edge (case (E)).
- **T1-correct worlds.** For g ∈ M let C(g) := {k : T1 is correct at world k at g}.
  - C(g) ≠ ∅: if g ∈ D_{T1} then v_k·g > 0 forces some g_k > 0; if g ∉ D_{T1} then g mixed has some g_k < 0.
  - C(g) ≠ Ω, since g is mixed.
  - R⁰_k := {k ∈ C(g)}. J_l := {C(g) = {l}} = E_i(T1) ∩ E_j(T1) ∩ M = E_i(T1) ∩ Q_l, the joint T1-error set of the
    other two worlds i, j. W_l := {C(g) = Ω ∖ {l}}, where T1 is wrong only at l.
- **The splices Y_l := T1 △ J_l.** Equal to T1 on Q_i ∪ Q_j = R_ij and to P_i (= P_j) on Q_l. Y_l is better than T1
  at worlds i and j on J_l, and changes nothing else. By strict (G), Y_l ≺_i T1 and Y_l ≺_j T1 in every ranking.
- **Countably additive (CA) endorser.** An endorser ν_k = ρ_kμ with no purely finitely additive part.
  - **(ZER_k)** ("zero exchange rate at world k"): world k has a CA endorser whose density is > 0 a.e. off Λ_k,
    i.e. one of maximal support.
  - Then ψ_k(X) := ∫_{E_kX ∩ M} ρ_k endorses every relevant world-k comparison.
  - Example: a world ranked lexicographically by a primary ψ_k, with strict (G) supplied by lower levels on Λ_k, is
    (ZER_k).

---

## 2. The field level

### 2.1 The T1-shadow

**Theorem M1.1 (PROVED).**
- **(a)** Let ρ_k ≥ 0 be integrable with ρ_k = 0 a.e. on E_k(T1) ∩ M and ρ_k > 0 a.e. on R⁰_k (k = 1, 2, 3), and
  put c := (ρ_kσ_k). Then:
  - c ≠ 0 a.e. on M;
  - B_q = T1 (mod null) for every q ∈ Δ°, so Z_q is null and q·c has the sign s_T a.e.;
  - A(c) = Δ, so T1 is c-Bayes at every interior weighting, at every point of every open edge, and at every vertex;
  - d_t(c) = 0 for every t ∈ Δ.

  The blind sets are Λ_k = E_k(T1) ∩ M. They are non-null, with Λ_i ∩ Λ_j = J_l non-null and Λ₁ ∩ Λ₂ ∩ Λ₃ = ∅. Each
  Λ_k contains one side of every open facet arc of D_{T1}: the inside where g_k < 0, the outside where g_k > 0.
- **(b) Characterization.** For any field c = (ρ_kσ_k) with ρ_k ≥ 0, the following are equivalent:
  - (i) A(c) = Δ;
  - (ii) e₁, e₂, e₃ ∈ A(c);
  - (iii) ρ_k = 0 a.e. on E_k(T1) ∩ M for k = 1, 2, 3.
- **(c) The (V) variant.** c := (0, σ₂, σ₃) has ρ₂, ρ₃ > 0, Λ₁ = M and A(c) ∋ e₁. Every B_q, q ∈ Δ°, is one of
  P₂, P₃ and P₂ ∩ P₃, so B_q is coherent and d_t(c) = 0 for every t ∈ Δ.

*Proof.*
- **(a)**
  - At g ∈ M, c_k(g) = 0 for k ∉ C(g), and for k ∈ C(g) the sign σ_k(g) equals s_T(g): T1 correct at k means it
    accepts iff g_k > 0.
  - Hence q·c(g) = s_T(g) Σ_{k∈C(g)} q_kρ_k(g). For q ∈ Δ° this is nonzero with sign s_T, since C(g) ≠ ∅ and
    ρ_k > 0 there. So B_q ∩ M = D_{T1} ∩ M. With ρ := 1 on N₊ (L4 §1), B_q ⊇ N₊.
  - For q ∈ ∂Δ the sum is ≥ 0. So s_T q·c ≥ 0 a.e., i.e. q ∈ A(c), with ties exactly where C(g) ∩ supp q = ∅.
  - d_t = 0: T1 is coherent and is a t-Bayes model for every t ∈ Δ.
  - Λ_i ∩ Λ_j = {C(g) = {l}} = J_l. It contains D_{T1} ∩ (−,−,+) near r₁₂ (for l = 3) and its cyclic images, so it is
    non-null.
  - Λ₁ ∩ Λ₂ ∩ Λ₃ = {C(g) = ∅} = ∅.
  - The side statement holds because T1 errs at k exactly inside D_{T1} where g_k < 0, and outside it where g_k > 0.
- **(b)**
  - A(c) is convex, so (ii) ⇔ (i).
  - e_k ∈ A(c) means s_Tρ_kσ_k ≥ 0 a.e., i.e. ρ_k = 0 wherever σ_k ≠ s_T, i.e. on E_k(T1) ∩ M.
- **(c)**
  - With θ = q₂/(q₂ + q₃): for θ > 1/2, B_q = {σ₂ = +} = P₂; for θ < 1/2, B_q = P₃; for θ = 1/2,
    B_q = U ∩ {g₂ > 0, g₃ > 0} = D_{co(K′ ∪ [e₂, e₃])}. All three are coherent.
  - On the open edges [e₁, e_j], B = P_j. At e₁ every model is Bayes, including T1. At e₂, e₃ the Bayes models are
    P₂, P₃.
  - e₁ ∈ A(c), since c₁ ≡ 0. ∎

NUMERICS (`m1py/shadow_check.py`, `.out`; 200 000 samples of M; three (ε, s) pairs):
- over 1 500 random interior q, 0 sign mismatches between q·c^T and T1, and 0 ties;
- over 60 boundary q, 0 strict mismatches;
- J_l covers 8.5–13% of M.

(`m1py/vertex_check.py` (4)): 0 midpoint-convexity violations for every B_q of (0, σ₂, σ₃).

**Corollary M1.1′ (what M1.1 settles; PROVED).**
- **(a) Blind sets at two or three worlds.** There are degenerate fields with three blind sets, with p* anywhere in
  Δ°, with c ≠ 0 a.e., and with every facet arc touched by all three blind sets. So L1.D cannot hold without its
  pairwise-null hypothesis, and that hypothesis is essential.
- **(b) Boundary cases.** There are degenerate fields with p* at a vertex (M1.1(a), and M1.1(c) under (B1)), and with
  p* on an open edge.
- **(c) The fixed-point route cannot conclude.**
  - c^T satisfies everything L4.1 extracts from a cover: (γ₀), d_t = 0 at every t ∈ Δ, admissibility, and moreover
    every interior B_q coherent and c ≠ 0 a.e.
  - It is even a "realisation of T1" in the sense of Definition realisation (with K_q ≡ T1), except that c₁, c₂, c₃
    are not strictly signed.
  - So no argument that uses only the countably additive fixed point excludes covers. L4.5 showed this for the gap
    alone and for purely finitely additive ν. M1.1 shows it with a CA field and all the M0closed-type regularity.
  - Theorem main and M0closed(a) use strict signs exactly in Lemma UVN. For c^T, UVN fails at every vertex:
    B_q ≡ T1 as q → e_k.

### 2.2 The vertex case under (B1)

**Proposition M1.2 (PROVED).** Assume (B1) of L4 §4 (ρ₂, ρ₃ > 0 a.e., (γ₀), T1 = B_{p*} ∪ S) with p* = e₁. Let K₁, K₀
be the credal sets of K3.7(β′), which uses only (γ) and ρ₂, ρ₃ > 0 (L4 §4). Then:
- **(i)** e₂ ∈ K₁ and e₃ ∈ K₀;
- **(ii)** Λ₁ ⊇ M ∩ {g₁ > 0}, i.e. Λ₁ ⊇ (+,−,−) ∪ (+,−,+) ∪ (+,+,−) on M;
- **(iii)** Λ₁ ∩ {g₁ < 0} = (D_{K₁} ∩ ((−,+,+) ∪ (−,+,−))) ∪ (D_{K₀} ∩ (−,−,+)) ⊇ D_{T1} ∩ {g₁ < 0}. So the visible
  set V₁ := M ∖ Λ₁ lies in {g₁ < 0} ∖ cl D_{T1}.

*Proof.*
- **Λ₁ ⊇ E₁(T1) ∩ M.** This is L4.3: p* = e₁ forces ρ₁ = 0 on E₁(T1) ∩ M.
- **Translating through (β′).** Λ₁ ∩ R₁₂ = E₁(D_{K₁}) ∩ R₁₂, and on (−,+,+) ⊆ Q₁ ⊆ R₁₂ the world-1 error set of a model
  is the model itself (g₁ < 0). So D_{K₁} ∩ (−,+,+) ⊇ D_{T1} ∩ (−,+,+) a.e.
  - Both sets are open. So P_{K₁} ≥ 0 on D_{T1} ∩ (−,+,+), and by continuity on its closure.
  - The closure contains the crossing w₂₁ = (−1, 0, κ) of F₁. Points of D_{T1} just inside F₁ with small g₂ > 0 lie in
    (−,+,+).
- **(i) for K₁.** K₁ meets [e₁, e₂] at some m = (a, 1−a, 0) (β′). Then 0 ≤ P_{K₁}(w₂₁) ≤ m·w₂₁ = −a, so a = 0 and
  e₂ ∈ K₁.
- **(i) for K₀.** The same argument on R₁₃ = Q₁ ∪ Q₃ ⊇ (−,+,+) gives D_{K₀} ⊇ D_{T1} on (−,+,+). Use the other crossing
  w₃₁ = (−1, κ, 0) of F₁'s middle arc, which is also approached from (−,+,+). For m = (a, 0, 1−a) ∈ K₀,
  m·w₃₁ = −a, so e₃ ∈ K₀.
- **(ii).** e₂ ∈ K₁ gives D_{K₁} ⊆ {g₂ > 0}. So on (+,−,−) ∪ (+,−,+) (⊆ R₁₂, g₁ > 0), D_{K₁} rejects everything, and
  Λ₁ = (·) ∖ D_{K₁} is everything. Likewise e₃ ∈ K₀ gives Λ₁ ⊇ (+,+,−) ⊆ R₁₃.
- **(iii)** is (β′) read on the three orthants with g₁ < 0, together with Λ₁ ⊇ E₁(T1). ∎

NUMERICS (`m1py/vertex_check.py` (5)): 300/300 random K₁ ⊆ co(K′ ∪ [e₁, e₂]) meeting the edge at a > 0 miss
D_{T1} ∩ (−,+,+) near w₂₁. With e₂ ∈ K₁, D_{K₁} ∩ (+,−,·) = ∅ on every sample.

*Reading.* L4.7 excluded the minimal (V) instance Λ₁ = E₁(T1) ∩ M. M1.2 shows that every (V) instance under (B1) is
far from minimal: world 1 must be CA-blind on all of its acceptance problems. M1.1(c) shows the extreme case Λ₁ = M is
consistent at the field level.

### 2.3 Two field-level restrictions

**Lemma M1.10 (edge limits; PROVED).** Let c have (γ₀) with c ≠ 0 a.e. Fix an edge {i, j} with third world k, and for
θ ∈ (0, 1) put e_θ := θρ_iσ_i + (1−θ)ρ_jσ_j. For a.e. θ, the model

  E_θ := ({e_θ > 0} on M ∖ (Λ_i ∩ Λ_j)) ∪ (P_k on Λ_i ∩ Λ_j) ∪ N₊

is coherent. On Q_k ∖ (Λ_i ∩ Λ_j) it equals P_i. Hence:
- if Λ_i ∩ Λ_j ∩ Q_k is null, E_θ = D_K with K ∩ [e_i, e_j] ≠ ∅ and K ⊆ co(K′ ∪ [e_i, e_j]) (Lemma K3.7′);
- for c^T, E_θ = T1.

*Proof.*
- **Ties are null for a.e. θ.** For g ∉ Λ_i ∩ Λ_j, e_θ(g) = 0 for at most one θ: if σ_i = σ_j it never vanishes; if
  σ_i ≠ σ_j it vanishes once or never. By Fubini, {e_θ = 0} ∖ (Λ_i ∩ Λ_j) is null for a.e. θ.
- **Convergence.** For such θ, take q_m → θe_i + (1−θ)e_j in Δ°. Off Λ_i ∩ Λ_j, sign(q_m·c) → sign(e_θ) pointwise
  off the ties. On Λ_i ∩ Λ_j, q_m·c = q_{m,k}ρ_kσ_k has sign σ_k (ρ_k > 0 there, since c ≠ 0).
- So B_{q_m} → E_θ in measure. Every B_{q_m} is coherent (L4.1.2), and limits in measure of coherent models are
  coherent (H12_referee §1.1).
- On Q_k, σ_i = σ_j, so e_θ has the sign σ_i wherever it is nonzero.
- For c^T: on R_ij exactly one of i, j is T1-correct, and only that one is live, so e_θ follows T1. On Q_k ∖ J_k both
  are T1-correct. On J_k = Λ_i ∩ Λ_j, P_k = T1. ∎

So the shadow's degeneracy is visible on every edge: its edge limits are T1 itself, not models between two vertices.
Pairwise-null blind sets force the edge limits back into the "between" form, which is the skeleton of the
strictly-signed chain.

**Proposition M1.11 (exact shadow-blindness at one world needs blindness at the others; PROVED).** Let c have (γ₀) with
c ≠ 0 a.e. Fix distinct i, j, k. Suppose Λ_i = E_i(T1) ∩ M (mod null), and ρ_k > 0 a.e. on J_j ∪ J_k. Then there is a
contradiction.

*Proof.*
- **The weights.** Index weights as (q_i, q_j, q_k) and take q = (1 − s, sη, s(1 − η)) ∈ Δ°.
- **Two successive limits.** First s → 0 with η fixed (for a.e. η the limiting ties on J_j ∪ J_k, where ηρ_j = (1−η)ρ_k,
  are null; Fubini). The limit M_η is coherent, being a limit in measure of the coherent B_q (L4.1.2, H12_referee
  §1.1). Then η → 0. Pointwise:
  - On R⁰_i (ρ_i > 0), sign(q·c) → σ_i, which is T1's advice there.
  - On Λ_i = E_i(T1), q·c = s(ηρ_jσ_j + (1−η)ρ_kσ_k).
    - On W_i (T1 wrong only at i; σ_j = σ_k = s_T) the sign is s_T: T1.
    - On J_k (correct only at k), it is s_T((1−η)ρ_k − ηρ_j), which tends to T1 because ρ_k > 0.
    - On J_j (correct only at j), it is s_T(ηρ_j − (1−η)ρ_k), which tends to −s_T: the opposite of T1.
- **Conclusion.** The limit model is T1 △ J_j = Y_j. It is coherent, as an iterated limit in measure of coherent
  models. This contradicts Lemma M1.6. ∎

Example: worlds 1 and 2 exactly shadow-blind and world 3 strictly positive is impossible. So a shadow-type degeneracy
with exact blind sets needs **all three** worlds blind, as in c^T.

### 2.4 What is left at the field level

**CONJECTURE L1.D (as stated in L1 §6.3).** No field with (γ₀), c ≠ 0 a.e. and **pairwise-null** blind sets has T1 Bayes at an interior
weighting.
- By M1.1 this is the strongest form L1.D can take.
- The single step of L1 that I could not transfer is crosspin at a pinned crossing of coordinate c (L1.4(e)), when Λ_c
  accumulates at that crossing. There the ball lemma no longer forbids a tie ball, because c_c ≡ 0 on Λ_c.
- L1.B applied to world c would put Λ_c in E_c(T1) near ∂D_{T1}, which excludes that accumulation. But L1.B's own
  proof uses crosspin at the other worlds' pinned crossings, so the argument is circular as it stands.
- M1.10 supplies the "between" edge models that a simultaneous induction would need.

---

## 3. The ranking level: what strict (G) adds to the fixed point

**Lemma M1.3 (face KKM with strict (G); PROVED).** Assume (LA), (S), strict (G). Let X ∈ M_U and ∅ ≠ I ⊆ Ω. Then there
is p in the face Δ_I with C := C_p ∈ C_L and C ⪯_i X for every i ∈ I. If C ≠ X, then μ(E_iX ∖ E_iC) > 0 for every
i ∈ I: C fixes some error of X at every world of I.

*Proof.*
- **The KKM cover.** Put S_i := {p ∈ Δ_I : C_p ⪯_i X} for i ∈ I. Each is closed by (S). For J ⊆ I and p ∈ Δ_J,
  competitiveness of C_p on supp p ⊆ J gives j ∈ J with p ∈ S_j, so Δ_J ⊆ ⋃_{j∈J} S_j.
- **KKM.** The KKM lemma on Δ_I gives p ∈ ⋂_{i∈I} S_i. (This is Theorem kkm's proof run on a face.)
- **Strict (G).** On M_U a model is determined by E_i(·) = · △ P_i. If μ(E_iX ∖ E_iC) = 0 and C ≠ X, then
  E_iX ⊊ E_iC (mod null), and strict (G) gives X ≺_i C, contradicting C ⪯_i X. ∎

**Lemma M1.4 (Pareto-tie principle; PROVED).** Assume (H_U). Let ν_i be endorsers at the worlds i ∈ I, let X be regular
and let i₀ ∈ I. Suppose every model Y with ν_i(E_iY) ≤ ν_i(E_iX) for all i ∈ I has E_{i₀}X ⊆ E_{i₀}Y. Then X ∈ C_L,
selected on Δ_I.

*Proof.*
- Take C from M1.3. The comparisons C ⪯_i X are relevant (C ∈ C_L, X regular), so ν_i(E_iC) ≤ ν_i(E_iX).
- By hypothesis E_{i₀}X ⊆ E_{i₀}C. So C fixes no error of X at i₀, and M1.3 gives C = X. ∎

**Corollary M1.5 (PROVED).** Assume (H_U). Let the worlds i ∈ I have CA endorsers ρ_iμ, and put ψ_i(X) := ∫_{E_iX∩M} ρ_i.
- **(a) Tie-broken Bayes models.** For t ∈ Δ with supp t = I and i₀ ∈ I, put
  B^I_t := {Σ_{i∈I} t_iρ_iσ_i > 0} and Z^I_t := {Σ_{i∈I} t_iρ_iσ_i = 0}. Then T^{i₀}_t := B^I_t ∪ (Z^I_t ∩ P_{i₀}) ∪ N₊
  is coherent and in C_L.
- **(b) Rigidity of blind sets, without (γ).** For i ≠ j, put V_i := {ρ_i > 0} ∩ M. Then
  X_{ij} := P_i on V_i, P_j on M ∖ V_i (and accepting N₊) is coherent and in C_L. Hence
  (M ∖ V_i) ∩ R_ij = E_i(D_K) ∩ R_ij for a coherent D_K agreeing with P_i on Q_k: K ∩ [e_i, e_j] ≠ ∅ and
  K ⊆ co(K′ ∪ [e_i, e_j]) (Lemma K3.7′).
- **(c) Lexicographic vertex fans.** If all three worlds have CA endorsers, with ρ_j, ρ_k > 0 a.e. (j, k ≠ i), then for a.e. θ the model
  S_θ := P_i on V_i, {θρ_jσ_j + (1−θ)ρ_kσ_k > 0} on M ∖ V_i is coherent and in C_L. This upgrades K3.7(β)'s
  "coherent" to "selected".

*Proof.*
- **(a)**
  - Σ_{i∈I} t_iψ_i(Y) − Σ_{i∈I} t_iψ_i(T) = ∫_{Y△T} |Σ_I t_iρ_iσ_i| dμ ≥ 0. This is the pointwise identity of
    H1.0(b), restricted to I.
  - So ψ_i(Y) ≤ ψ_i(T) for all i ∈ I forces equality in the sum, hence Y △ T ⊆ Z^I_t.
  - On Z^I_t, T = P_{i₀} is correct at i₀. So E_{i₀}T ⊆ E_{i₀}Y, and M1.4 applies.
- **(b)** ψ_i(Y) ≤ ψ_i(X_{ij}) = 0 forces Y = P_i on V_i. X_{ij}'s world-j errors lie in V_i ∩ R_ij, where Y errs
  too. Apply M1.4 with I = {i, j} and i₀ = j. The K3.7′ statement follows because X_{ij} = P_i on Q_k.
- **(c)** ψ_i(Y) = 0 forces Y = P_i on V_i. Then ψ_j(Y) ≤ ψ_j(S_θ) and ψ_k(Y) ≤ ψ_k(S_θ) force Y to be θ-Bayes on
  M ∖ V_i, so Y = S_θ off a null tie set (a.e. θ, Fubini). Apply M1.4 with I = Ω. ∎

**Lemma M1.6 (PROVED).**
- **(a) Facet-plane lemma.** Let K ⊇ K′ be a credal set, α an open arc of relint F_m, and N an open cone with
  α ⊆ N ⊆ U. If D_K ∩ N = D_{T1} ∩ N a.e., then v_m ∈ K.
- **(b)** For each l, Y_l = T1 △ J_l is incoherent.

*Proof.*
- **(a)**
  - Both sets are open, so ∂D_K ∩ N = ∂D_{T1} ∩ N ⊇ α. Take h ∈ α. Then P_K(h) = 0; let m ∈ K with m·h = 0.
  - Suppose m ≠ v_m. Two distinct points of Δ give non-proportional linear forms. Since v_l·h > 0 for l ≠ m, every
    neighbourhood of h contains a non-empty open set of g ∈ N with v_m·g > 0 > m·g and v_l·g > 0. This set lies in
    D_{T1} ∖ D_K, which is impossible. So m = v_m.
  - (This is the step of L4.6(b).)
- **(b)** Take l = 3 (the others follow by the cyclic symmetry, which preserves T1, K′ and U). Suppose Y₃ = D_K, so
  K ⊇ K′.
  - Y₃ = T1 on R₁₂ = Q₁ ∪ Q₂. Q₁ ∪ Q₂ contains three facet arcs with cones around them inside open orthants: the
    middle arc of F₁ in (−,+,+), the middle arc of F₂ in (+,−,+), and the r₂₃-corner portion of F₃ in (+,−,−)
    (Lemma signs).
  - By (a), v₁, v₂, v₃ ∈ K. So K ⊇ T1 and D_K ⊆ D_{T1}.
  - But Y₃ = P₁ on Q₃ accepts (+,+,−) ∩ U, which contains the non-null open set just outside F₃'s middle arc (that arc
    lies in (+,+,−)). This is a contradiction. ∎

NUMERICS (`shadow_check.py` (2)): midpoint-convexity violations are 137–282 per ~26 000 sums for Y₁, Y₂, Y₃, against
0 for T1, at all three (ε, s).

**Theorem M1.7 (the edge exchange; PROVED).** Assume (H_U). For each pair {i, j}, with third world k, there are C ∈ C_L
and non-null sets F_i ⊆ E_i(T1) ∩ R_ij and F_j ⊆ E_j(T1) ∩ R_ij with the following properties:
- C fixes T1's world-i errors on F_i and T1's world-j errors on F_j;
- every endorser ν_i of world i satisfies ν_i(F_i) ≥ ν_i(E_iC ∖ E_iY_k) ≥ ν_i(F_j);
- every endorser ν_j of world j satisfies ν_j(F_j) ≥ ν_j(F_i).

*Proof.*
- **The witness.** Apply M1.3 to X = Y_k (regular) and I = {i, j}. This gives C ∈ C_L with C ⪯_i Y_k and C ⪯_j Y_k.
  C ≠ Y_k, since Y_k is incoherent (M1.6). So F_i := E_iY_k ∖ E_iC and F_j := E_jY_k ∖ E_jC are non-null.
- **Where they lie.** E_i(Y_k) = E_i(T1) ∖ J_k = E_i(T1) ∩ R_ij, and likewise for j.
- **F_j costs C at world i.** On F_j ⊆ R_ij, C is correct at j and so wrong at i, while Y_k = T1 is correct at i
  there. So F_j ⊆ E_iC ∖ E_iY_k.
- **Endorsement.** It gives ν_i(E_iC) ≤ ν_i(E_iY_k). Subtracting ν_i(E_iC ∩ E_iY_k) (finite additivity) gives
  ν_i(F_i) ≥ ν_i(E_iC ∖ E_iY_k) ≥ ν_i(F_j).
- **World j.** Symmetrically, F_i ⊆ E_jC ∖ E_jY_k. ∎

*Reading.* In every cover, each world must value some piece of its own T1-error set on R_ij at least as highly as a
piece of the other world's T1-error set there, under every endorser. For strictly positive densities this is a
consistency condition and no more. For blind worlds it is the binding constraint.

**Corollary M1.8 (PROVED).** In a cover, no world i has a CA endorser ρ_iμ with ρ_i = 0 a.e. on E_i(T1) ∩ R_ij and
ρ_i > 0 a.e. on E_j(T1) ∩ R_ij, for some j ≠ i.
- **For the T1-shadow.** If the maximal endorser of world i has CA part positive exactly on R⁰_i (the shadow
  pattern), then every endorser ν_i = ρ_iμ + π_i of world i has π_i(F_i) ≥ ρ_i(F_j) + π_i(F_j). For the maximal
  endorser ν*_i this is > 0, for both j ≠ i. In particular (ZER_i) fails at every world.

*Proof.*
- The main statement: 0 = ρ_i(F_i) ≥ ρ_i(F_j) > 0.
- For the shadow: every endorser's CA part vanishes on Λ_i = E_i(T1) ⊇ F_i (K3.1(c)). So
  π_i(F_i) ≥ ρ_i(F_j) + π_i(F_j).
- Apply this to the maximal endorser ν*_i, whose CA part ρ*_i is > 0 on F_j ⊆ R⁰_i. Then ν*_i is not CA.
- If (ZER_i) held, its CA endorser ρμ would be > 0 a.e. on R⁰_i ⊇ F_j and 0 on F_i, so 0 = ρ(F_i) ≥ ρ(F_j) > 0. ∎

**Theorem M1.9 (zero exchange rate at an edge; PROVED).** Assume (H_U). Let worlds i, j have CA endorsers ρ_iμ, ρ_jμ
(not necessarily of maximal support). Suppose that for some θ ∈ (0, 1), T1 agrees on R_ij with the tie-broken
edge-Bayes model T^i_θ := {e_θ > 0} ∪ ({e_θ = 0} ∩ P_i), where e_θ = θρ_iσ_i + (1−θ)ρ_jσ_j. That is:
- θρ_i ≥ (1−θ)ρ_j a.e. on R_ij ∩ E_j(T1), where T1 is right at i; and
- (1−θ)ρ_j > θρ_i a.e. on R_ij ∩ E_i(T1), where T1 is right at j.

Then (H_U) is contradictory. The same holds with i and j exchanged (the strict inequality on the other side).

*Proof.*
- On Q_k, σ_i = σ_j, so e_θ is 0 or has the sign σ_i. Either way T^i_θ = P_i there.
- By hypothesis T^i_θ = T1 on R_ij. So T^i_θ = T1 on R_ij and P_i on Q_k, i.e. T^i_θ = Y_k.
- Corollary M1.5(a) (t = θe_i + (1−θ)e_j, I = {i, j}, i₀ = i) says T^i_θ is coherent. This contradicts M1.6(b). ∎

NUMERICS (`shadow_check.py` (3)): for c^T, T^i_θ = Y_k on every sample, for 4 values of θ, three edges, three (ε, s).

**Corollary M1.9′ (PROVED).**
- **(a) The shadow at zero exchange rate.** If worlds i, j have CA endorsers with ρ_i = 0 on E_i(T1), ρ_j = 0 on
  E_j(T1), and ρ_j > 0 a.e. on R_ij ∩ E_i(T1), then (H_U) fails. (M1.8 already gives this from world j alone.)
- **(b) The edge case at zero exchange rate: a two-sided tie shell.**
  - *Setting.* Let p* = θ*e_i + (1−θ*)e_j ∈ A(c), with (ZER_i) and (ZER_j). Put Z := Z_{p*}, and Z^{(i)} :=
    Z ∩ R_ij ∩ E_i(T1), Z^{(j)} := Z ∩ R_ij ∩ E_j(T1).
  - *Both ties are non-null.* Admissibility gives the two weak inequalities of M1.9 at θ*. If either strict one held
    a.e., M1.9 would give a contradiction. So Z^{(i)} and Z^{(j)} are both non-null.
  - *They form shells along whole facets.* T^i_{θ*} = T1 △ (J_k ∪ Z^{(i)}) is coherent (M1.5(a)). So, by M1.6(a) and
    the argument of M1.6(b), there is a facet F_m along all of whose R_ij-arcs Z^{(i)} is non-null in every
    neighbourhood of every point. Otherwise v₁, v₂, v₃ ∈ K and D_K ⊆ D_{T1}, against T^i ⊇ P_i ∩ J_k ⊄ cl D_{T1}.
    The same holds for Z^{(j)}.
  - *What the ties are.* On R_ij, ties of e_{θ*} are the points where ρ_i/ρ_j = (1−θ*)/θ* or ρ_i = ρ_j = 0. So the
    edge densities are frozen at the target ratio, on both sides of T1's boundary, along every R_ij-arc of some facet.
- **(c)** Whenever T1 is admissible at two vertices e_i, e_j, the only escape from M1.9 is the same two-sided tie
  shell.

*Proof.*
- (a): T^i_θ = T1 on R_ij under these hypotheses, for every θ ∈ (0, 1).
- (b): stated in the item.
- (c): admissibility at e_i and e_j makes ρ_i, ρ_j vanish on E_i(T1), E_j(T1). Then the first inequality of M1.9
  holds, and the second fails only on ties. ∎

---

## 4. What world orders must do to realise the shadow, and the realisation attempt

### 4.1 The precise requirements (each PROVED necessary)

A ranking with (H_U) on M_U whose maximal endorser field is c^T must satisfy all of the following at every world i
(for every j ≠ i).

- **(W1) Blindness on T1's own errors, positivity elsewhere.** Every endorser of world i has CA part vanishing on
  E_i(T1) ∩ M. The maximal one is positive a.e. on R⁰_i.
  - Equivalently, by K3.1(f): for every non-null B′ ⊆ E_i(T1) and every c > 0 there is a c-ratio certificate on B′
    built from relevant world-i comparisons. So T1's world-i errors are "certified cheap".
- **(W2) Positive exchange rate into the blind set (M1.7, M1.8).** Every endorser ν_i has
  π_i(F_i) ≥ ρ_i(F_j) + π_i(F_j), and the maximal one has π*_i(F_i) ≥ ρ*_i(F_j) > 0.
  - The world-i comparison C ⪯_i Y_k of M1.7 has strictly negative CA value: ∫ρ*_iδ_i ≤ −ρ*_i(F_j) < 0.
  - Its positive part F_i lies in the blind set and meets every member of the localizing family D^{ν*_i} of K3.1(b)
    (otherwise K3.1(b) would make ρ*_i endorse it).
  - So world i must accept trades that give up CA-visible correctness on F_j ⊆ R⁰_i in exchange for fixing thin
    pieces of its own T1-error set E_i(T1) ∩ R_ij, at an "end" carried by the purely finitely additive part.
  - No world is (ZER).
- **(W3)** Strict (G), (IB), closed sections for every model, (C), and T1 ∈ C_L.
- **(W4) The edge exchange on every edge (M1.7).** The witnesses C are coherent and selected on [e_i, e_j], and fix
  T1's errors at both i and j on R_ij.

(W1) holds automatically on its own: the trades it asks for are the ratio certificates. The binding requirement is
(W2) together with (W3).

### 4.2 The attempt

1. **"Strict (G) with zero exchange rate on the blind sets"** (the brief's suggestion, BRIEF17 §3). These are the
   lexicographic worlds: primary ψ_i(X) = ∫_{E_iX ∩ R⁰_i} ρ_i, and strict (G) supplied on E_i(T1) by lower levels.
   - They are (ZER_i), so M1.8 excludes them at every world.
   - Concretely, with two such worlds i, j, the edge selection on [e_i, e_j] fails. M1.3 needs a selected coherent
     C ⪯_{i,j} Y_k. Primaries force C = T1 off J_k. Strict (G) then forces C = Y_k, which is incoherent.
   - (This is M1.9 for c^T.)
2. **L2's blind-set device** (block levels, PG(2, q) targets, compactness of selectors). It gives full systems with
   non-localizable blind sets. But:
   - (i) its world has the CA endorser λ|_{d_a} (L2.4(b)), so it is (ZER) and is excluded by M1.8 as soon as its blind
     set is aimed at E_i(T1) ∩ R_ij;
   - (ii) its trades have the opposite orientation to (W2). L2's generators g = 1_Q − 1_P put the **negative** part P
     in the blind set c_a and the positive part Q in the visible set. (W2) needs the positive part in the blind set
     and the negative part visible.

   So L2's mechanism makes errors in the blind set cheap. The shadow needs them cheap in CA (W1), yet worth at least a
   visible loss at the margin, through a purely finitely additive part (W2).
3. **K3.3's tilt has the right orientation.** In the tilted world, comparisons with thin far targets beat fat sources,
   and every bounded endorser is purely finitely additive at the far end.
   - A shadow world would be such a tilt, with its end placed inside E_i(T1) ∩ R_ij for both j. Natural candidate
     ends: thin shells along the R_ij-arcs of ∂D_{T1} on the T1-wrong-at-i side, where the edge witnesses of M1.7
     must act.
   - It would have a CA-visible complement R⁰_i on which the endorser is positive, and closed sections.
   - K3.3's tilt fails closed sections (K3.3(a), Q12_referee N3): the union over κ of the tilted cones is not closed.
     L2 repaired closedness only by passing to finitely many levels, which re-creates a CA endorser.
   - I found no closed-section tilt. **This is where the attempt broke.**

### 4.3 Beyond the shadow (what M1.9 leaves for zero-exchange-rate realisations)

M1.9 and M1.9′ settle the zero-exchange-rate question for the shadow and for (E) without tie shells. Two cases remain
open for zero exchange rate:
- **(V)** under (B1), with world 1 CA-blind on M ∩ {g₁ > 0} ∪ (D_{K₁} ∪ D_{K₀}) ∩ {g₁ < 0} (M1.2). Here T1
  restricted to R_ij need not be edge-Bayes on any edge, so M1.9 does not apply.
  - M1.5(b), (c) only add that X₁₂ = D_{K₁}, X₁₃ = D_{K₀} and the fans S_θ are selected.
  - (PROVED) With worlds 2, 3 additive, T1 ∈ C_L also forces ess inf_{J₃} ρ₃/ρ₂ ≥ ess sup_{J₂} ρ₃/ρ₂, i.e. T1 is (2,3)-Bayes on
    E₁(T1) ∩ R₂₃. The trade A₂ ∪ A₃ that would otherwise dominate T1 (world-1-better by (G), additive-no-worse at
    2, 3) is excluded only by this.
  - I did not derive a contradiction.
- **Interior pairwise-null blind sets** (CONJECTURE L1.D).

---

## 5. The single open question

**Q_M1.** Is there a ranking on M_U satisfying every axiom of BRIEF13 (closed sections for every evaluable model) whose
maximal endorser field is the T1-shadow c^T? Equivalently, by M1.1(b), is there one in which T1 is admissible at all
three vertices?
- **Necessary (PROVED, §4.1).** Each world i is a closed-section tilt whose purely finitely additive "end" lies inside
  its own T1-error set E_i(T1) ∩ R_ij (both j). Its maximal endorser has CA part positive exactly on R⁰_i and a
  nonzero purely finitely additive part charging E_i(T1) ∩ R_ij.
- **"No".** This would exclude every cover whose degeneracy is of the shadow type. With L1, L4.9 and M1.9′(b) it would
  leave, among (NC) systems, only:
  - (V) under (B1) (M1.2);
  - (E) with two-sided tie shells or without zero exchange rate;
  - interior pairwise-null blind sets (L1.D);
  - strongly (M1) worlds.
- **"Yes".** This gives a cover of T1: (H_U) holds by hypothesis, and T1 ∈ C_L. Its world orders are those of §4.1.

The first test for a "yes" is two-world. Build a full two-world system on M_U whose world 1 has no CA endorser of
maximal support, with every bounded endorser purely finitely additive on a prescribed "end" set. K3.3 has no closed
sections, and L2 has a CA endorser, so no known example has this.

---

## 6. Dependencies and files

**Used.**
- L4.1, L4.0, L4.3 (the fixed point, absorption, boundary admissibility); L4 §4 (B1) with K3.7(β), (β′) and Lemma
  K3.7′.
- K3.1(b), (c), (f).
- Theorem kkm and its KKM proof (M1.3 runs it on a face).
- H1.0(b)'s pointwise identity; H12_referee §1.1 (limits in measure of coherent models are coherent; coherent models
  of M_U are the D_K with K ⊇ K′).
- Lemma signs; the step of L4.6(b) (in M1.6(a)).
- L2.4(b) (L2's CA endorser), K3.3 (the tilt) — only in §4.

**Not used.** M0closed's proof, the §4 chain, Prop. F, (E_ψ), Lyapunov (except through L4.1/H1.1), any (Nest_e) or
edge result.

**Not refereed.** Points to check, in order of risk:
- M1.3's use of KKM on a face, and the step "E_i determines the model" on M_U;
- M1.6(a) on cones N that meet ∂U (choose N ⊆ U);
- M1.9′(b)'s "every neighbourhood of every point" formulation;
- M1.11's two successive limits (a.e. η).

`m1py/` (run with `python3 -I` from inside it):
- `m1_common.py`: geometry for any (ε, s), samplers, midpoint-convexity test.
- `shadow_check.py` (+ `shadow_check.out`):
  - (1) B_q = T1 for interior q and admissibility at boundary q for c^T;
  - (2) incoherence of Y₁, Y₂, Y₃ versus a coherent baseline;
  - (3) T^i_θ = Y_k for c^T on three edges.
- `vertex_check.py` (+ `vertex_check.out`):
  - (4) coherence of the B_q of (0, σ₂, σ₃);
  - (5) the forcing e₂ ∈ K₁ of M1.2, and D_{K₁} ∩ (+,−,·) = ∅.
