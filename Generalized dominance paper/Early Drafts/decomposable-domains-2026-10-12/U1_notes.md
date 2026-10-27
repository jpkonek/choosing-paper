# U1 (round 23). (E∗) cannot be completed: an all-(Loc) cover needs a T1-separating model on every edge, and the linear host has none

16 Oct 2026 (BRIEF13 rules; task: complete the blueprint (E∗) of T2n §4 into a full three-world cover of T1 on M_U,
or prove that it cannot be completed). Labels: **PROVED** (full proof here, from inputs whose status is named),
**CHECKED** (step-by-step reading, not a re-derivation), **CONJECTURE**, **NUMERICS** (`u1py/u1_checks.py`, run
`python3 -I -B u1_checks.py` from inside `u1py/`; output `u1_checks.out`; no proof rests on it). No assumption is
added: every hypothesis beyond (H_U) is a hypothesis of the result that uses it.

Notation: R21 §1 (n = 3, U = D_{K′}, K′ = u + s(T1 − u), M, N₊, P_k = U ∩ {g_k > 0}, E_k(X) = X △ P_k, σ_k, Q_l,
R_ij = Q_i ∪ Q_j, (H_U)); Q2 Part I ((Loc) datum (ρ_k, D^k), enlarged data, B_t, Z_t, edge models, E^{θ,±});
T2n §4 (blueprint (E∗)); Q1 §1 (cut moves, (TC)). c₀ = (1−ε)/3, κ = (1+2ε)/(1−ε) > 1, v_k = c₀𝟙 + εe_k (the vertices
of T1), and K′ has vertices v′_k = c₀′𝟙 + ε′e_k with ε′ = sε < ε, c₀′ = (1−ε′)/3, κ_U := (1+2ε′)/(1−ε′) < κ.

Orthants. For each world l, the sign class Q_l (world l odd) is the union of two orthants (intersected with U):
- the **one-positive** orthant O_l⁺ := {g_l > 0 > g_k, g_{k′}} (for l = 1: (+,−,−)),
- the **two-positive** orthant O_l⁻ := {g_l < 0 < g_k, g_{k′}} (for l = 1: (−,+,+)).

On O_l⁺, T1 is the quadrilateral of the chart g = |g_l|(e_l − a e_k − b e_{k′}):
**quad** := {(a, b) ∈ (0,∞)² : κa + b < 1, a + κb < 1}, with corner (c, c), c := 1/(κ+1), and intercepts 1/κ.
On O_l⁻, T1 is {a + b > κ} in the chart g = |g_l|(−e_l + a e_k + b e_{k′}); there U is {a + b > κ_U}.
(Both follow from min_k v_k·g, the minimum being attained at the most negative coordinate; write-up §2.3.)
T1 is right at the odd world l exactly on
  **W_l := Q_l ∖ E_l(T1) = (O_l⁺ ∩ D_{T1}) ∪ (O_l⁻ ∖ D_{T1}).**

The **linear host** on the edge {i, j} is the chain L_m := U ∩ {m·g > 0} (∪ N₊), m ∈ [e_i, e_j]; these are the coherent
models D_{co(K′∪{m})} used by T2n.2, T2n.7, T2n.8 and Q1.26 as the edge chains of (E∗).

---

## 0. Outcome

**(E∗) cannot be completed (Corollary U1.4, PROVED for continuous base densities; CHECKED for measurable ones).** The
obstruction is not where T2n §4.3 located it. It does not involve the interior definition of worlds 2 and 3, the
sheltering cone, safe tests or Q_W. It is a theorem about every cover in which all three worlds are (Loc), and it uses
only T1's competitiveness, closed competitive choice on the edges, and the facet geometry of T1.

1. **Theorem U1.1 (edge separation; PROVED from R1 inputs).** In every all-(Loc) cover of T1 on M_U, each edge
   selection [e_i, e_j] contains a coherent model X_ij that **agrees with T1 a.e. on W_i ∪ W_j**: wherever T1 is right
   at the odd world of Q_i or of Q_j, so is X_ij.
   - Source: T1 is Bayes at an interior weight p̂ for the σ-finite field c = (ρ_kσ_k) (Q2.11(c) [R1]). On W_i the third
     world's positive density makes the inequality strict: ρ_j/ρ_i < p̂_i/p̂_j on W_i, and > p̂_i/p̂_j on W_j. The extreme
     edge Bayes model at that ratio is edge-selected (Q2.12(a) [R1]).
2. **Lemma U1.2 (which edge models separate; PROVED, elementary).** A coherent D_K separates on {1, 2} iff
   K ⊆ Π₁₂ (an explicit polytope) and K meets **both** cevian segments [m₀, v₁] and [m₀′, v₂], where
   m₀ = (κ,1,0)/(κ+1), m₀′ = (1,κ,0)/(κ+1): the parts of the lines e₃v₁ and e₃v₂ between T1 and the edge [e₁, e₂].
   **No linear-host model separates** (nor do P₁, P₂). Separating edge models exist, e.g. co(K′ ∪ [m₀, m₀′]) and
   co(K′ ∪ {v₁, v₂, m}).
3. **Theorem U1.3 (no linear edge; PROVED).** No all-(Loc) cover of T1 on M_U has a linear-host edge selection on
   **any one** edge.
4. **Corollary U1.4 ((E∗) cannot be completed).** Every completion of (E∗) is all-(Loc): world 1 is (CA⁺), and worlds 2,
   3 accept cut moves along both of their (transverse) linear edge chains, so Q1.22–Q1.23 make them (Loc) (this is
   T2n.8, re-verified here: the 23-block's base cone contains the 23-cut moves). All three edge chains of (E∗) are
   linear hosts. U1.3 applies.
5. **What it closes and why it was missed (§5).** It closes (E∗) outright, and every all-(Loc) cover with a linear edge,
   in every R21 configuration. Q_W in pair form does not arise for (E∗). T2n.4/T2n.5 found "no field-level obstruction"
   because they tested the **bounded** CA fields, which are degenerate in (E∗) (c♮ = (ρσ₁, 0, 0)). The σ-finite field of
   the (Loc) data is non-degenerate and is interior-admissible, and that is what the edges cannot carry.
6. **The nearby target that survives (§6; PROVED + NUMERICS).** Replace the linear hosts by **segment hosts**
   co(K′ ∪ [a, b]), [a, b] ⊆ [e_i, e_j]. Proposition U1.5 gives an explicit σ-finite field, one increasing function R₊
   used on every edge, whose edge chains are segment hosts and whose interior Bayes model at u is **exactly** T1. It
   passes Q2.11–Q2.14 and U1.1–U1.3. The linear host is precisely the special case R₊(x)R₊(1/x) ≡ 1, which T1's facets
   forbid; the segment host relaxes it to ≥ 1.

**Single open question (Q_U1, §6.3).** Is there an all-(Loc) cover of T1 on M_U with segment-host edge chains, i.e. the
blueprint (E∗) with its three linear hosts replaced by segment hosts? By T2n.3, Q2.16 and K1.6 this is again Q_W in pair
form, now for (E∗_seg). U1.3 shows it cannot be answered "No" at edge-plus-admissibility level.

| | Statement | Label |
|---|---|---|
| U1.1 | all-(Loc) cover ⇒ every edge selection contains a model agreeing with T1 on W_i ∪ W_j | PROVED (Q2.11(c), Q2.12(a): R1) |
| U1.2 | separating edge models: characterization; linear host and vertex models never separate; examples | PROVED; NUMERICS (A), (B) |
| U1.3 | no all-(Loc) cover with a linear-host edge selection on any edge | PROVED |
| U1.4 | every completion of (E∗) is all-(Loc); (E∗) cannot be completed | PROVED (continuous ρ₁, dλ/dμ: Q1.22–Q1.23 R1); CHECKED (measurable: T1n.5) |
| U1.5 | segment-host template: T1 = B_u exactly, edge chains segment hosts, R₊ ≥ R₋ | PROVED; NUMERICS (C)–(F) |
| U1.6 | (E∗_seg): edge blocks exist; worlds 2, 3 (Loc) by gluing | edge blocks PROVED at the status of T2n.2 (unrefereed); (Loc) CONJECTURE (reading) |
| Q_U1 | all-(Loc) cover with segment hosts? (= Q_W pair form for (E∗_seg)) | open |

---

## 1. Inputs

| Input | Use | Status |
|---|---|---|
| Theorem kkm | T1 tied with a selected C_p (inside Q2.11(c)) | write-up, proved |
| Q2.10(a) | enlarged (Loc) data (ρ_k, D̃^k), ρ_k ≤ m off D̃^k_m | R1 (Q24_referee §1.1) |
| Q2.11(c) (via H1.1) | all-(Loc) ⇒ D_{T1} = B_{p̂} ∪ S′, S′ ⊆ Z_{p̂}, p̂ ∈ Δ° | R1 (Q24_referee §1.1; H1.1 R1, H12_referee) |
| Q2.12(a) (via M1.3, Q2.11(b)) | extreme edge Bayes models E^{θ,±} of (ρ_i, ρ_j) are edge-selected | R1 (Q24_referee §1.2; needs (LA), which (H_U) has) |
| Q1.20, Q1.21 | cut moves, composition | R1 (Q13_referee §§1.1–1.2) |
| Q1.22, Q1.23, Q1.26 | gluing; (Loc); (TC) for the linear host | R1, continuous case (Q13_referee §§1.4–1.7; Q1.23 quantifier GAP, routine fix given there) |
| T1n.5 | Q1.22–Q1.23 for measurable densities | PROVED in T1n, unrefereed |
| P1.10–P1.14, T2n.1, T2n.2 | the edge blocks of (E∗) | R1 (P1_referee); T2n unrefereed |

Throughout, "a.e." refers to μ; all sets below are cones (0-homogeneous), and "non-null" is checked in the 2-dimensional
charts above (μ is equivalent to Lebesgue measure and the chart maps are smooth bijections from rays to points).

---

## 2. Edge separation

**Theorem U1.1 (PROVED).** Assume (H_U) on M_U and that every world k has a (Loc) datum (ρ_k, D^k). Let p̂ ∈ Δ° be the
interior weight of Q2.11(c) for the field c = (ρ_kσ_k). Fix i ≠ j, let l be the third world, and put
θ_ij := p̂_i/p̂_j ∈ (0, ∞) and r_ij := ρ_j/ρ_i on R_ij. Then:
- **(i)** r_ij < θ_ij a.e. on W_i, and r_ij > θ_ij a.e. on W_j;
- **(ii)** the edge model X_ij with world-i errors {r_ij > θ_ij} on R_ij (equal to P_i = P_j on Q_l, accepting N₊) is
  C_q for some q in the **open** edge (e_i, e_j), hence coherent, and X_ij = T1 a.e. on W_i ∪ W_j.

*Proof.*
- **(i)** By Q2.11(c), for a.e. g ∈ U: if T1 accepts g then p̂·c(g) ≥ 0; if T1 rejects g then p̂·c(g) ≤ 0 (since
  B_{p̂} ⊆ D_{T1} and D_{T1} ∖ B_{p̂} ⊆ Z_{p̂}).
  - Let g ∈ W_i. T1 is right at i there, hence wrong at j and l (on Q_i worlds j and l agree and oppose i). So T1's
    advice has the sign σ_i, and the Bayes inequality reads σ_i·p̂·c(g) ≥ 0, i.e.
    p̂_iρ_i ≥ p̂_jρ_j + p̂_lρ_l. Since ρ_l > 0 a.e., p̂_iρ_i > p̂_jρ_j a.e. on W_i, i.e. r_ij < θ_ij.
  - On W_j the same computation with i and j exchanged gives p̂_jρ_j > p̂_iρ_i, i.e. r_ij > θ_ij.
- **(ii)** With θ := θ_ij/(1+θ_ij) ∈ (0,1), X_ij is the model E^{θ,−} of (ρ_i, ρ_j) (its world-i errors on R_ij are
  {e_θ < 0} = {r_ij > θ_ij}). By Q2.12(a) and its proof [R1], E^{θ,−} = C_q for some q ∈ [e_i, e_j]; it is in C_L,
  hence coherent.
  - By (i), the world-i error set {r_ij > θ_ij} misses W_i and contains W_j (mod null).
  - On W_i: X_ij and T1 are both right at i, so they give the same advice (on U the advice is determined by the error
    status at one world).
  - On W_j ⊆ Q_j: X_ij errs at i. On Q_j worlds i and l agree and oppose j, so X_ij is right at j, as T1 is. Same advice.
  - W_i and W_j are non-null (§3, (3.1)). So X_ij ≠ P_i (P_i has no world-i errors, but X_ij errs on W_j) and
    X_ij ≠ P_j (P_j errs at i on all of R_ij ⊇ W_i). Hence q ∉ {e_i, e_j}. ∎

*Remarks.*
- Nothing about blindness, (C), closed sections at interior indices, sheltering, safe tests or the interior
  definition of any world is used. The inputs are T1's competitiveness (inside Q2.11(c)), the face KKM on the edge
  (M1.3, inside Q2.12(a)), strict (G), (IB) and (LA).
- The statement holds for **every** choice of (Loc) data. p̂ and X_ij depend on the data.
- (i) is the edge shadow of the full Bayes condition at p̂. Its strictness comes from the **third** world; this is
  exactly where the bounded fields of T2n.4–T2n.5 (third density 0) are silent.

---

## 3. Which edge models separate

By the coordinate permutations (which preserve T1, K′ and U), it suffices to treat {i, j} = {1, 2}, l = 3. Then

  W₁ = (O₁⁺ ∩ D_{T1}) ∪ (O₁⁻ ∖ D_{T1}),  W₂ = (O₂⁺ ∩ D_{T1}) ∪ (O₂⁻ ∖ D_{T1}),

with O₁⁺ = (+,−,−), O₁⁻ = (−,+,+), O₂⁺ = (−,+,−), O₂⁻ = (+,−,+). A model agrees with T1 on W₁ ∪ W₂ iff it
- **(a1)** accepts O₁⁺ ∩ D_{T1}, **(a2)** accepts O₂⁺ ∩ D_{T1}, **(b1)** rejects O₁⁻ ∖ D_{T1}, **(b2)** rejects O₂⁻ ∖ D_{T1}.

**(3.1) The four sets in charts.** Put x := |g₂|/|g₁| on R₁₂.
- O₁⁻ ∖ D_{T1}: g = |g₁|(−1, s, t) with κ_U < s + t < κ. For every s ∈ (0, κ) the t-section is a non-empty open
  interval. So {x ∈ J} ∩ (O₁⁻ ∖ D_{T1}) is non-null for every open J ⊆ (0, κ).
- O₂⁻ ∖ D_{T1}: g = |g₂|(s′, −1, t′) with κ_U < s′ + t′ < κ, and x = 1/s′. So {x ∈ J} ∩ (O₂⁻ ∖ D_{T1}) is non-null for
  every open J ⊆ (1/κ, ∞).
- O₁⁺ ∩ D_{T1} and O₂⁺ ∩ D_{T1} are the (open, non-empty) quadrilaterals of the charts (1, −a, −b) and (−a, 1, −b).

So W₁ and W₂ are non-null, and since **κ > 1**, the x-ranges (0, κ) and (1/κ, ∞) of the two rejected regions overlap.

**Lemma U1.2 (PROVED).** Let K ⊇ K′ be a credal set.
- **(a)** (a1) ∧ (a2) hold for D_K iff K ⊆ Π₁₂, where
  Π₁₂ := {m ∈ Δ : κm₁ ≥ m₂, κm₁ ≥ m₃, (κ+1)m₁ ≥ m₂ + m₃, κm₂ ≥ m₁, κm₂ ≥ m₃, (κ+1)m₂ ≥ m₁ + m₃}.
- **(b)** (b1) holds iff K meets R⁽¹⁾ := {m ∈ Δ : κm₂ ≤ m₁, κm₃ ≤ m₁}; (b2) holds iff K meets
  R⁽²⁾ := {m ∈ Δ : κm₁ ≤ m₂, κm₃ ≤ m₂}.
- **(c)** Π₁₂ ∩ R⁽¹⁾ = [m₀, v₁] and Π₁₂ ∩ R⁽²⁾ = [m₀′, v₂], with m₀ = (κ,1,0)/(κ+1), m₀′ = (1,κ,0)/(κ+1). Hence D_K
  agrees with T1 on W₁ ∪ W₂ iff **K ⊆ Π₁₂ and K meets both [m₀, v₁] and [m₀′, v₂]**. Both segments lie on the lines
  e₃v₁, e₃v₂, between T1 (which they touch only at v₁, v₂) and the edge [e₁, e₂].
- **(d) The linear host never separates.** No L_m (m ∈ [e₁, e₂]) satisfies (b1) and (b2). Neither does P₁ or P₂.
- **(e) Separating edge models exist.** K_a := co(K′ ∪ [m₀, m₀′]) and, for m ∈ [e₁, e₂] with m₁/m₂ ∈ [1/κ, κ],
  K_b := co(K′ ∪ {v₁, v₂, m}) are coherent {1,2}-edge models (equal to P₁ on Q₃) that agree with T1 on W₁ ∪ W₂.

*Proof.*
- **(a)** For m ∈ Δ the function m·g is affine in the chart (1, −a, −b) of O₁⁺. D_K ⊇ O₁⁺ ∩ D_{T1} iff
  min_{m∈K} m·g > 0 on the open quad, iff every m ∈ K has m·g ≥ 0 at the four vertices (0,0), (1/κ, 0), (0, 1/κ),
  (c, c) of the quad (an affine function ≥ 0 at the vertices is > 0 inside unless it vanishes identically, which
  m ∈ Δ excludes). The vertices give m₁ ≥ 0, κm₁ ≥ m₂, κm₁ ≥ m₃, (κ+1)m₁ ≥ m₂ + m₃. (a2) is the same in the chart
  (−a, 1, −b) of O₂⁺. (Mod-null inclusion of the open set O₁⁺ ∩ D_{T1} in D_K is equivalent to inclusion, since D_K is
  open in U up to the null set ∂D_K.)
- **(b)** In the chart (−1, s, t) of O₁⁻, D_K ∩ O₁⁻ = {(s, t) : m₂s + m₃t > m₁ for all m ∈ K} and
  O₁⁻ ∖ D_{T1} = {κ_U < s + t < κ} (null boundaries ignored).
  - If m ∈ K ∩ R⁽¹⁾: for s, t > 0 with s + t ≤ κ, m₂s + m₃t − m₁ ≤ κ max(m₂, m₃) − m₁ ≤ 0. So D_K rejects
    O₁⁻ ∖ D_{T1}.
  - If K ∩ R⁽¹⁾ = ∅: the bilinear function F(m, (s,t)) := m₂s + m₃t − m₁ on the compact convex sets K and
    Tr := {s, t ≥ 0, s + t ≤ κ} has max_{Tr} F(m, ·) = κ max(m₂, m₃) − m₁ > 0 for every m ∈ K. By the minimax theorem
    there is (s, t) ∈ Tr with min_K F(·, (s,t)) =: δ > 0, and by continuity (uniform on compact K) an open set of
    (s, t) with s, t > 0, s + t < κ and min_K F > δ/2. Those gambles lie in D_K ⊆ U and outside cl D_{T1}: a non-null
    part of O₁⁻ ∖ D_{T1} that D_K accepts. (b2) is the same in the chart (s′, −1, t′) of O₂⁻.
- **(c)** On R⁽¹⁾ ∩ Π₁₂: κm₂ ≤ m₁ ≤ κm₂ gives m₁ = κm₂; then (κ+1)m₂ ≥ m₁ + m₃ gives m₃ ≤ m₂, and every other
  inequality of Π₁₂ and R⁽¹⁾ follows. So m ∝ (κ, 1, μ), μ ∈ [0, 1]: μ = 0 is m₀ and μ = 1 is v₁ = c₀(κ,1,1). These
  points have m₂ < c₀ for μ > 1 and m₃ < c₀ for μ < 1, while T1 = {m : m_k ≥ c₀ ∀k}; so only v₁ is in T1. Symmetrically
  for R⁽²⁾. Combine with (a), (b).
- **(d)** L_m = U ∩ {m·g > 0}, m = (m₁, m₂, 0). In the chart of O₁⁻, m·g = −m₁ + m₂s, so L_m rejects O₁⁻ ∖ D_{T1}
  (a.e.) iff the non-null set {m₁/m₂ < s < κ} ∩ (O₁⁻ ∖ D_{T1}) is empty (3.1), iff m₁/m₂ ≥ κ. In the chart of O₂⁻,
  m·g = m₁s′ − m₂, so L_m rejects O₂⁻ ∖ D_{T1} iff m₂/m₁ ≥ κ. Both together need κ ≤ m₁/m₂ ≤ 1/κ, impossible since
  κ > 1. P₁ accepts O₂⁻ (g₁ > 0) and P₂ accepts O₁⁻ (g₂ > 0), and both rejected sets are non-null.
- **(e)** K′ ⊆ T1 ⊆ Π₁₂ (T1 is in the dual cone of D_{T1}). Check m₀, m₀′, v₁, v₂ and m against the six inequalities
  directly (m₀: κ²/(κ+1) ≥ 1/(κ+1), κ ≥ 1/(κ+1), κ/(κ+1) ≥ κ/(κ+1), 1 ≥ κ/(κ+1); m₀′ symmetric; m with
  m₁/m₂ ∈ [1/κ, κ] and m₃ = 0 satisfies all). K_a contains m₀ ∈ [m₀, v₁] and m₀′ ∈ [m₀′, v₂]; K_b contains v₁, v₂. By (c)
  both agree with T1 on W₁ ∪ W₂.
  - *Edge model.* On (−,−,+) ∩ U, m₀·g, m₀′·g, m·g < 0, so D_K rejects, as P₁ does. On (+,+,−) ∩ U, g = (a, b, −c) with
    c₀′(a+b−c) − ε′c > 0, i.e. c < c₀′(a+b)/(c₀′+ε′); then every point of K′, the edge points, and v₁, v₂ give
    positive values (for v₁: v₁·g = c₀(a+b−c) + εa ≥ c₀(a+b)ε′/(c₀′+ε′) > 0). So D_K = P₁ on Q₃. Also K ⊆
    co(K′ ∪ [e₁, e₂]) = co(e₁, e₂, v′₃): v₁ = γv′₃ + (rest on [e₁,e₂]) with γ = c₀/(c₀′+ε′) ≤ 1 and non-negative rest. ∎

NUMERICS (A), (B) (`u1_checks.out`, four (ε, s) pairs, ε up to 0.9): for 400 values of m₁/m₂ on a log grid in
[10⁻³, 10³], a sampled witness against (b1) ∧ (b2) is found for every L_m; K_a and K_b agree with T1 on all sampled
points of W₁ ∪ W₂ (up to 10⁵ points) and equal P₁ on all sampled points of Q₃.

*Reading of (c).* A separating edge model must reach, with its credal set, both of T1's "facet directions" adjacent to
the edge: the point m₀ (where the facet F₁'s supporting direction meets the edge plane) and m₀′. A linear-host credal set
co(K′ ∪ {m}) has only one edge point and K′ is deep inside T1, so it can reach at most one side.

---

## 4. No linear edge; (E∗) cannot be completed

**Theorem U1.3 (PROVED).** Let a ranking satisfy (H_U) on M_U, with every world (Loc). Then for every edge {i, j} the
edge selection p ↦ C_p, p ∈ [e_i, e_j], contains a model that is not a linear-host model L_m. In particular no
all-(Loc) cover of T1 on M_U has a linear-host edge selection on any edge.

*Proof.* U1.1(ii) gives an edge-selected X_ij that agrees with T1 on W_i ∪ W_j. By U1.2(d) (transported to {i, j} by
the coordinate permutation), X_ij is neither a vertex model nor any L_m. ∎

**Corollary U1.4 ((E∗) cannot be completed).** Let a ranking satisfy (H_U) on M_U and realise the blueprint (E∗) of
T2n §4:
- world 1 is (CA⁺): ρ₁ ∈ L¹(M), ρ₁ > 0 a.e., ρ₁μ endorses every relevant world-1 comparison (additive worlds qualify);
- the three edge selections are the linear hosts;
- the comparisons of worlds 2 and 3 supported in R₂₃ are those of the two worlds of T2n.1 on 𝓔₂₃ (one is P1's world 1,
  the other its mirror; base measure λ ~ μ on R₂₃, chain coordinate pushing λ to Lebesgue measure); say world 2 is the
  mirror (the other case is the same with x and x′ exchanged); on R₁₂, R₁₃ worlds 2, 3 are any worlds with strict (G),
  (IB) (the P1.10 blocks qualify).

Then (H_U) is contradictory. **PROVED** when ρ₁ and dλ/dμ are continuous and positive; **CHECKED** for measurable
densities (through T1n.5).

*Proof.*
1. **World 1 is (Loc)** with datum (ρ₁, ∅).
2. **World 2 accepts cut moves along both of its edge chains.**
   - *12-chain.* World 2's errors at L_m on R₁₂ are an initial segment of its chain coordinate x₂₁ (a monotone function
     of |g₁|/|g₂| pushing ρ₁μ|_{R₁₂}, normalised, to Lebesgue measure). Lemma Q1.20 [R1], with world 2 in the role of
     world 1 and world 1 (CA⁺, hence (RL-2)) as the partner, gives: S ⊆ {x₂₁ < b}, T ⊆ {x₂₁ ≥ b}, ρ₁(T) > ρ₁(S) ⇒
     1_T − 1_S is accepted at world 2.
   - *23-chain.* In T2n.1 world 2's errors at the edge model C_b are {x′ < 1 − b} with x′ := 1 − x, and its R⁰-rule
     accepts every regular δ with δ|_{R₂₃} ∈ T′ := {f : ∫_{x′≥t} f dλ ≥ 0 ∀t} (selector F ≡ ⊥). For S ⊆ {x′ < b′},
     T ⊆ {x′ ≥ b′}, λ(T) ≥ λ(S), f := 1_T − 1_S has ∫_{x′≥t} f dλ = λ(T) − λ(S ∩ {x′ ≥ t}) ≥ 0 for t ≤ b′ and
     = λ(T ∩ {x′ ≥ t}) ≥ 0 for t > b′. So f ∈ T′ and 1_T − 1_S is accepted. By Lemma vectorform the acceptance of a
     vector supported in R₂₃ is the same in the three-world ranking as in the edge block.
3. **(TC) at Q₂.** The two chain coordinates of world 2 on its link class Q₂ = R₁₂ ∩ R₂₃ are monotone functions of
   |g₁|/|g₂| and of |g₃|/|g₂|. Q1.26 [R1, Q13_referee §1.7], transported by the transposition (1 2), gives (TC).
4. **World 2 is (Loc).** Q1.22–Q1.23 use the partners only through the conclusion of Lemma Q1.20 (acceptance of cut
   moves conserving the step's base mass), plus strict (G), (IB) and (TC) (Q1 §§2–4; Q13_referee §§1.4–1.5 re-derive
   them in this form; the gluing measure on the 23-chain is λ instead of a partner density). So they give a.e.-finite
   ρ*₂ = ρ₁φ(x₂₁) on R₁₂ and λψ(x₂₃) on R₂₃, endorsing every D-localized relevant world-2 comparison. For continuous
   ρ₁, dλ/dμ this is Q1.22–Q1.23 (continuous case, R1; the quantifier fix of Q13_referee §1.5 is routine). For
   measurable densities it is T1n.5(a),(b), whose proof also uses only cut moves (T1n §6: "only ω enters"), read here,
   not re-derived: CHECKED.
5. **World 3 is (Loc)** by the transposition (2 3): its 13-cut moves come from world 1 (Lemma Q1.20), its 23-cut moves
   from P1's world 1 on 𝓔₂₃, whose base cone T = {f : ∫_{x≥t} f dλ ≥ 0 ∀t} contains them by the same computation with
   x in place of x′.
6. All three worlds are (Loc), and all three edge selections are linear hosts. Theorem U1.3 (one linear edge suffices)
   contradicts (H_U). ∎

*Remarks on U1.4.*
- Only one linear edge is needed. E.g. if only the 12-edge of (E∗) is a linear host and worlds 2 and 3 are (Loc) by
  any means, (H_U) already fails.
- Nothing in the proof depends on how worlds 2 and 3 are defined at interior indices, on (C), on closed sections
  beyond the edges, or on T1's selection index. So **no interior definition of worlds 2 and 3 (in particular no
  choice κ in the exact consistency test P3.2, no interior base cone, no gluing rule) can complete (E∗)**: the cut
  moves that make worlds 2, 3 (Loc) come from the edge blocks and from Lemma Q1.20 alone, and the contradiction then
  needs only T1's competitiveness and closed choice on the edges.

---

## 5. What this closes, what it does not, and Q_W for (E∗)

**Closed (PROVED, at the status of U1.3 / U1.4).**
1. **(E∗)**, in every completion, whatever is done at interior indices.
2. **Every all-(Loc) cover of T1 on M_U with a linear-host edge selection on some edge.** In R21's tree this is the
   all-(Loc) part of (P0), (PD), (E), (X) (and of (V) with (Loc) partners) whenever an edge selection is a linear host.
   It also covers every all-(Loc) cover in which, for some (Loc) data, one edge ratio is **one-sided**: r_ij(g) a
   function of |g_j|/|g_i| alone, the same on {g_i > 0 > g_j} and on {g_i < 0 < g_j} (R₊ = R₋ in the notation of §6).
   Then the separating model {r_ij > θ_ij} of U1.1(ii) is a linear-host model, against U1.2(d). By Q2.12–Q2.13 [R1] a
   linear-host edge chain forces such a ratio.
3. **Q_W in pair form for (E∗)** does not arise: there is no cover to test. The anti-safe question (K1.Q, T2n §5) is
   downstream of an obstruction that already fires on the boundary of Δ and at T1's own index.

**Why T2n missed it.** T2n.4 and T2n.5 tested **bounded** (CA) fields: for (E∗) the universal fixed point is
c♮ = (ρσ₁, 0, 0), with A(c♮) = [e₂, e₃], and such a field has no third positive density to make U1.1(i) strict.
The σ-finite field of the (Loc) data (which exists in (E∗) by U1.4 steps 2–5, i.e. T2n.8) is strictly positive at every
world, T1 is Bayes for it at an **interior** weight (Q2.11(c)), and that is what the linear edges cannot carry. Q2.16
had all the inputs but routed them only through (W) and M0closed(a), which need (γ) on a non-null set; U1.1 needs (γ)
only at p̂ and on the edges (Q2.13(c)).

**Not closed.**
- All-(Loc) covers whose three edge selections each contain a separating model (U1.2(c)); §6 shows the field level
  allows them.
- Covers with a non-(Loc) world. With linear hosts this needs, at a blind world, an edge block that does **not** accept
  all cut moves of that edge (in (E∗): a 23-block whose world-2 base cone omits some 23-cut moves; then Q1.22 does not
  apply on Q₂). No such block is known, and nothing here constrains it.
- (S), general domains: untouched.

---

## 6. The nearby target: segment hosts

**6.1 Segment hosts.** For {i, j} with third world l, the **segment model** S[a, b] := D_{co(K′∪[a,b])}, with
a, b ∈ [e_i, e_j] and a no farther from e_i than b, is a coherent {i,j}-edge model. With x := |g_j|/|g_i| on R_ij,
α := a_i/a_j ≥ β := b_i/b_j, its world-i errors on R_ij are
- {x > α} on {g_i < 0 < g_j} (accepted points; the binding constraint is a),
- {x ≥ β} on {g_i > 0 > g_j} (rejected points; the binding constraint is b).

A nested family S[a(θ), b(θ)], with α(θ), β(θ) decreasing continuously from ∞ to 0, is a **segment host**; the linear
host is a = b. If a ratio r_ij has superlevel sets equal to the world-i error sets of a segment host, then
r_ij = R₊^{ij}(x) on {g_i > 0 > g_j} and R₋^{ij}(x) on {g_i < 0 < g_j}, with R₊^{ij} ≥ R₋^{ij} nondecreasing; and
conversely any such pair (R₊^{ij} ≥ R₋^{ij}, continuous, strictly increasing from 0 to ∞) arises (put β(s), α(s) the
inverse functions at level s; α ≥ β). The linear host is R₊ = R₋. By U1.1(i), at p̂ = u (θ_ij = 1) a separating level
needs R₋^{ij} < 1 on (0, κ) and R₊^{ij} > 1 on (1/κ, ∞), which a segment host allows.

**Proposition U1.5 (segment-host template; PROVED, NUMERICS (C)–(F)).** Let c := 1/(κ+1) and
- h(t) := (κ+1)t/2 for 0 < t ≤ c, and h(t) := 1 − (κ+1)(1 − κt)/2 for c ≤ t ≤ 1/κ;
- R₊(x) := h(x) for 0 < x ≤ 1/κ, and R₊(x) := κx for x ≥ 1/κ;
- R₋(x) := 1/R₊(1/x) (so R₋(x) = x/κ for x ≤ κ and 1/h(1/x) for x ≥ κ).

Define a field by the single rule

  **whenever g_k > 0 > g_m:  ρ_m/ρ_k := R₊(|g_m|/|g_k|),**

with an arbitrary positive base density on each Q_l (on Q_l the rule fixes the two ratios to the odd world; the two
agreeing worlds are not compared). Then:
- **(a)** the field is well defined, and on each edge region R_ij, r_ij = ρ_j/ρ_i equals R₊(x) on {g_i > 0 > g_j} and
  R₋(x) on {g_i < 0 < g_j}, x = |g_j|/|g_i|;
- **(b)** R₊ and R₋ are continuous, strictly increasing bijections of (0, ∞), and R₊ ≥ R₋; so every r_ij is the ratio
  chain of a segment host (6.1), and every edge Bayes model B_t, t ∈ ∂Δ, is a segment model, hence coherent;
- **(c)** **B_u = D_{T1} exactly** (no ties off null sets): T1 is the strict Bayes model at the centre;
- **(d)** at p̂ = u, U1.1(i) holds strictly: r₁₂ < 1 on W₁ and r₁₂ > 1 on W₂ (and cyclically), and the separating model
  of U1.1(ii) is S[m₀, m₀′] = K_a of U1.2(e).

*Proof.*
- *Properties of h.* h is continuous and strictly increasing on (0, 1/κ], h(0+) = 0, h(c) = 1/2, h(1/κ) = 1, and
  **h(t) + h(1 − κt) = 1 for t ∈ [c, 1/κ]** (then 1 − κt ∈ [0, c]). Also h(t) ≥ t/κ on (0, 1/κ]: both sides are linear on
  [0, c] and on [c, 1/κ], and the inequality holds at 0, c and 1/κ ((κ+1)/2 ≥ 1/κ, 1/2 ≥ c/κ, 1 ≥ 1/κ²).
- **(a)** On O_l⁺ (l positive, k, k′ negative) the rule gives ρ_k/ρ_l and ρ_{k′}/ρ_l; on O_l⁻ (l negative) it gives
  ρ_l/ρ_k and ρ_l/ρ_{k′}. No other pair has opposite signs. For (i, j) with g_i < 0 < g_j the rule (with k = j, m = i)
  gives ρ_i/ρ_j = R₊(|g_i|/|g_j|), i.e. r_ij = 1/R₊(1/x) = R₋(x).
- **(b)** R₊ is continuous at 1/κ (h(1/κ) = 1 = κ·(1/κ)) and strictly increasing; R₋ inherits this. R₊ ≥ R₋ ⟺
  R₊(x)R₊(1/x) ≥ 1: for x ≤ 1/κ it is κh(x)/x ≥ 1, i.e. h(x) ≥ x/κ; for 1/κ ≤ x ≤ κ it is κx·κ/x = κ² ≥ 1; x ≥ κ is the
  case x ≤ 1/κ with x and 1/x exchanged. For t = (t_i, t_j) in the open edge, B_t on R_ij is world-i-wrong exactly on
  {r_ij > t_i/t_j}, the error set of a segment model by 6.1; on Q_l it is P_i; so B_t = S[a, b] up to the null tie cone.
- **(c)** Sign of u·c, orthant by orthant (normalise the base to 1 at the odd world):
  - O_l⁺, chart |g_l|(e_l − a e_k − b e_{k′}): u·c ∝ 1 − R₊(a) − R₊(b). If a > 1/κ (or b > 1/κ), R₊ > 1, the bracket
    is negative, and the point is outside the quad (κa + b > 1). On (0, 1/κ]², with a ≥ b: if a ≤ c the point is in the
    quad and h(a) + h(b) < 1 unless a = b = c (boundary); if a ∈ (c, 1/κ], the point is in the quad iff b < 1 − κa iff
    h(b) < h(1 − κa) = 1 − h(a). So the bracket is > 0 exactly on the quad.
  - O_l⁻, chart |g_l|(−e_l + a e_k + b e_{k′}): u·c ∝ −1 + ρ_k/ρ_l + ρ_{k′}/ρ_l = −1 + R₋(a) + R₋(b), using
    ρ_k/ρ_l = 1/R₊(|g_l|/|g_k|) = R₋(a). For a, b ≤ κ this is (a + b)/κ − 1, positive iff a + b > κ; if a > κ then
    R₋(a) > 1, the bracket is positive and a + b > κ. So the bracket is > 0 exactly on T1 ∩ O_l⁻.
  - Equality holds only on ∂D_{T1}, a null set. So B_u = D_{T1} a.e. and Z_u is null.
- **(d)** W₁ = (quad of O₁⁺) ∪ {κ_U < a + b < κ in O₁⁻}. On the quad of O₁⁺, r₁₂ = R₊(a) ≤ 1 − R₊(b) < 1. On the rejected part
  of O₁⁻, r₁₂ = R₋(a) ≤ 1 − R₋(b) < 1. W₂ is the mirror. The level {r₁₂ > 1} has α = R₋⁻¹(1) = κ and
  β = R₊⁻¹(1) = 1/κ, i.e. a = m₀ and b = m₀′. ∎

NUMERICS (`u1_checks.out`, (ε, s) ∈ {(0.1,0.9), (0.3,0.9), (0.6,0.5), (0.9,0.3)}):
- (C) 4 × 4·10⁵ random g ∈ U: sign(u·c) = 1_{D_{T1}} at every sample, in every orthant; no ties.
- (D) R± monotone and R₊ ≥ R₋ on a log grid; for 60 random levels per edge, {r_ij > s} = world-i errors of
  S[a(s), b(s)] on every sampled point of R_ij (180/180).
- (E) r₁₂ < 1 on every sampled point of W₁, > 1 on W₂.
- (F) Control: the same construction with R₊ on both sides, or R₋ on both sides (one-sided ratios, as a linear host
  forces), is **not** T1-Bayes at u (2·10³ to 7·10⁴ mismatches per run).

*Reading.* The template is the "asymmetric linear" field ρ_k ∝ |g_k| for positive and κ|g_k| for negative coordinates
(R₊(x) = κx), whose Bayes model at u is D_{T1} on every two-positive orthant, with R₊ bent to h on (0, 1/κ] so that
the corners of T1 in the one-positive orthants come out exactly. The bend is what the corner equation of write-up §4
could not absorb with additive coherent B_q at every q; here coherence is required only on ∂Δ and at u, and the bend
costs nothing there. By M0closed(a), B_q is incoherent for a non-null set of interior q, as it must be.

**6.2 The blueprint (E∗_seg) (U1.6).** Keep (E∗) and replace each linear host by the segment host of U1.5.
- *Edge blocks (PROVED at the status of T2n.2, which is unrefereed).* T2n.2's proof of the P1.10/T2n.1 edge blocks uses only (R_ij ∩ U, λ, x), a nested chain
  and the N₊ rules. A segment host is nested (6.1), and its chain coordinate x (first-error time, pushing λ to
  Lebesgue) exists; so all three edge blocks exist on segment hosts, with both non-additive worlds totally blind on
  their edge regions.
- *(Loc) of worlds 2, 3 (CONJECTURE; a reading).* On each orthant of Q₂ the two chain coordinates of world 2 are
  monotone functions of |g₁|/|g₂| and |g₃|/|g₂| (with different reparametrisations on the two orthants), so (TC1)
  holds orthant by orthant; the X₁₂-ranges of the two orthants overlap, which should give (TC2). Then U1.4 steps 2–5
  apply and (E∗_seg) is all-(Loc). Not checked line by line.
- *Field level.* U1.5 shows that U1.1–U1.3, Q2.11–Q2.14 and the boundary (γ) of Q2.13(c) are all satisfiable by
  segment hosts. Blindness at the ends is compatible: R₊(x), R₋(x) → ∞ as x → ∞ (world j's end on the {i,j}-chain) and
  → 0 as x → 0, and the base densities on each Q_l are free.

**6.3 Single open question.**

> **Q_U1.** Is there a ranking satisfying (H_U) on M_U, all-(Loc), whose three edge selections are segment hosts (for
> instance those of U1.5), i.e. the blueprint (E∗_seg)?

- By T2n.3 [PROVED there] and Q2.16 [R1], such a cover needs persistent sheltering on R₂₃ between the two blind worlds;
  by K1.6 [R1] it needs anti-safe indices with {2, 3} in their support for every admissible triple. So Q_U1 is Q_W in
  pair form for (E∗_seg): the interior definition of worlds 2, 3 is again the open step, exactly as T2n §4.3 described,
  but now on a blueprint that survives the edge-plus-admissibility test.
- **"No"** would close every all-(Loc) cover with segment hosts. Closing all-(Loc) entirely would further need the same
  for every separating host (U1.2(c)).
- **"Yes"** must still deliver every axiom; U1.5 supplies the σ-finite field it must carry.

---

## 7. Dependencies, risk points, files

**Used.** Q2.10(a), Q2.11(b),(c), Q2.12(a) [R1, Q24_referee §§1.1–1.2]; H1.1 and Theorem kkm (inside Q2.11(c)); M1.3
[R1] (inside Q2.12(a)); Lemma vectorform; Q1.20–Q1.23, Q1.26 [R1 continuous case, Q13_referee]; T1n.5 [unrefereed;
measurable case of U1.4 only]; T2n.1, T2n.2 and P1.10 (the edge blocks; U1.4 and U1.6); T2n.3, Q2.16, K1.6 (§6.3 only);
M0closed(a) (a remark in §6.1 only); the minimax theorem (U1.2(b)).

**Not used.** Blindness, (C), (LF), closed sections at interior indices, the interior definition of any world,
sheltering, safe tests, any bounded endorser, L4.1, M1.x beyond M1.3.

**Points a referee should check, by risk.**
1. U1.1(i): the direction of the Bayes inequality on W_i and W_j (T1 accepts ⇒ p̂·c ≥ 0; rejects ⇒ ≤ 0), and that the
   strictness comes from ρ_l > 0.
2. U1.1(ii): that Q2.12(a)'s proof gives X = C_q **on the edge** (not merely X ∈ C_L), and that X ≠ P_i, P_j.
3. U1.2(d): the two chart computations and the non-nullness ranges (3.1): (0, κ) for O₁⁻ ∖ D_{T1} and (1/κ, ∞) for
   O₂⁻ ∖ D_{T1}; their overlap is exactly κ > 1.
4. U1.4 step 4: that Q1.22–Q1.23 (and T1n.5) use the partner on a chain only through accepted cut moves, so that the
   designed 23-cut moves of the edge block may replace Q1.20 on that chain.
5. U1.2(b): the minimax step and the closure issue when e₁ ∈ K (then D_K ∩ O₁⁻ = ∅ and (b1) holds trivially, and
   e₁ ∈ R⁽¹⁾, consistent).
6. U1.5(c): the corner case analysis on the quad, and R₋(a) = ρ_k/ρ_l on O_l⁻.

**Files** (`u1py/`, run with `python3 -I -B` from inside it):
- `u1_checks.py`, `u1_checks.out`: NUMERICS (A) linear host never separates (400/400 grid values, four (ε, s));
  (B) K_a, K_b separate and are edge models; (C) template T1 = B_u (0 mismatches in 1.6·10⁶ samples); (D) segment-host
  structure of the template ratios (180/180 levels per run); (E) U1.1(i) on the template; (F) one-sided control fails.
