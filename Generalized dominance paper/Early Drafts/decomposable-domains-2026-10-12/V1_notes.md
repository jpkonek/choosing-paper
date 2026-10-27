# V1 (round 24). Segment-host all-(Loc) covers: the U1.5 field passes every known exclusion; every all-(Loc) cover carrying it has a sheltered discontinuity in its selection; end-first sheltering is impossible; the cover was not completed

16 Oct 2026 (BRIEF13 rules; task: answer Q_U1 of U1 §6.3, i.e. build an all-(Loc) cover of T1 on M_U with segment-host
edge selections and U1.5's σ-finite field, or prove that none exists). Labels: **PROVED** (full proof here, from inputs
whose status is named), **CHECKED** (step-by-step reading, not a re-derivation), **CONJECTURE**, **NUMERICS**
(`v1py/`, run each script with `python3 -I -B <script>` from inside `v1py/`; outputs `*.out`; no proof rests on them).
No assumption is added. (Z), (UB), (H_Q) below are hypotheses of the results that use them. They are PROVED for U1.5's
field (Prop. V1.0).

Notation: R21 §1 (n = 3, U = D_{K′}, M, N₊, P_k, E_k, σ_k, Q_l, R_ij, (H_U)); Q2 Part I ((Loc) datum (ρ_k, D^k),
D-localized = "δ ≤ 0 a.e. on D_m for some m" (K3 §1), enlarged data D̃^k, B_t = {t·c > 0}, Z_t = {t·c = 0}); H1 §2
(Φ_t(Y) := ∫_{Y△B_t} |t·c| dμ); U1 §§3, 6 (orthant charts, R₊, R₋, h, segment models S[a, b], segment hosts).
c = (ρ_kσ_k) is the σ-finite field of the (Loc) data.

For a selection p ↦ C_p put Γ(p) := {w ∈ Δ_{supp p} : C_p is c-Bayes at w} (B_w ⊆ C_p ⊆ B_w ∪ Z_w a.e., ties free) and
Γ̂(p) := {w ∈ Δ : C_p is c-Bayes at w} ⊇ Γ(p). The selection is **continuous in measure at p** if p_n → p implies
μ(C_{p_n} △ C_p) → 0.

---

## 0. Outcome

**Neither a cover nor a closing theorem.** I could not build the cover, and I did not prove that segment-host all-(Loc)
covers are impossible. What is proved locates exactly where any such cover has to defeat M0closed(a), and it shows
that the natural way to do so fails.

1. **The field is not excluded by any known theorem (Prop. V1.0, PROVED; §1).** U1.5's field, with any positive base
   densities, satisfies the following:
   - it is strictly signed and σ-finite;
   - every tie set Z_t, t ∈ Δ, is null (Z);
   - T1 = B_u exactly;
   - its boundary Bayes sets are segment models;
   - it has two further properties used below, (UB) and (H_Q).

   M0closed(a) applies to the field by itself, and it says only that B_t is incoherent for a non-null set of interior t.
   NUMERICS put that set at almost all of Δ°. The coherent interior weights are u, three vertex caps, and short pieces
   of the medians. Q2.11(c), Q2.12–Q2.14, H1.2 and K3.5 either hold for the field or do not apply to it (§1.2). So the
   field does not have coherent Bayes models at every interior weight. That is why no known theorem excludes it. A
   cover carrying it must make (W) fail.
2. **Where (W) fails: at a sheltered discontinuity of the selection (Theorems V1.3, V1.5, PROVED).** Take an all-(Loc)
   cover whose field satisfies (Z), (UB), (H_Q), for example any cover carrying U1.5's field as (Loc) data. Then:
   - **(a) Order upper semicontinuity (Lemma V1.2).** For every p, every world k, every non-null W′ ⊆ Q_k ∖ E_k(C_p)
     and every p_n → p, eventually k ∈ supp p_n and C_{p_n} ⪯_k C_p △ W′. This uses only strict (G) and (S).
   - **(b) Discontinuities are sheltered (Theorem V1.3).** If C_{p_n} does not converge to C_p in w-cost
     (w ∈ Γ(p)), then for some k ∈ supp w and j ≠ k, both non-(CA⁺), the approaching models beat C_p at k inside
     D̃^k_M ∩ D̃^j_m ∩ R_kj, at every pair of depths M, m. So there is persistent sheltering on R_kj, and the
     selection uses it.
   - **(c) Such a discontinuity exists (Theorem V1.5).**
     - Otherwise the selection is continuous in measure.
     - Then Γ̂ has a closed graph, is convex-valued, and is face-preserving by (UB).
     - A Kakutani argument (Lemma V1.4) makes Γ̂ onto Δ, which is (W).
     - (W) contradicts M0closed(a) through Q2.16(6).

   This proves, for these fields, the step at which Q2 §6.3 stopped ("continuity of the selection in measure at
   sheltered depths"): the selection is continuous wherever no world uses a shelter. For (E∗)-type covers (world 1
   (CA⁺)) the sheltering pair is {2, 3}.
3. **End-first sheltering is impossible (Prop. V1.6, PROVED).** Suppose two worlds rank by a shared "end coordinate"
   first, with opposite preferences (for example lexicographically: a charge at the end first, an additive density
   second). Then closed sections force that coordinate to be constant along the selection. That is impossible between
   P_i and P_j. So the non-localized acceptances that V1.2–V1.3 force at the discontinuity cannot come from
   lexicographic ends. They must be of P1's tail-cone kind, or something else not yet known.
4. **Edge blocks on segment hosts (Lemma V1.1 PROVED; transfer CHECKED; §2).** Every property of the linear host that
   T2n.2 / P1.10–P1.14 use holds for segment hosts:
   - the chain is nested;
   - its level sets are null;
   - it has a continuous first-error coordinate pushing λ to Lebesgue measure;
   - every chain member is coherent;
   - every chain member is an edge model;
   - its endpoints are P_i and P_j.

   So the edge blocks of (E∗_seg) exist on segment hosts.
5. **Where the construction broke (§7).** It broke at the interior, as in T2n and U1. The obstruction is now one
   statement:
   - **realize a sheltered discontinuity (V1.5) with closed sections, using blind worlds that are not end-first (V1.6).**

   At the discontinuity point p, the blind world k must accept C_{p_n} ⪯_k Y″ for the explicit tests Y″ of V1.3.
   These comparisons are forced and non-localized. Meanwhile the partner j must reject the corresponding tests
   by ρ_j-mass. I found no acceptance structure doing this.

| | Statement | Label |
|---|---|---|
| V1.0 | U1.5's field: (Z), (UB), (H_Q); no known exclusion applies; (γ) fails off u, the vertex caps and ∂Δ | PROVED; NUMERICS (W-map) |
| V1.1 | segment hosts have every chain property used by T2n.2 / P1.10–P1.14 | PROVED; transfer CHECKED |
| V1.2 | order upper semicontinuity of the selection at every world | PROVED |
| V1.2′ | for an additive integrable world, ψ_k∘C is continuous wherever Q_k ∖ E_k(C_p) is non-null | PROVED |
| V1.3 | discontinuities in cost are carried by sheltered gains on some R_kj, k ∈ supp w | PROVED |
| V1.4 | face-preserving closed-graph convex-valued correspondences on Δ are onto | PROVED |
| V1.5 | every all-(Loc) cover with (Z), (UB), (H_Q) has a sheltered discontinuity | PROVED |
| V1.6 | end-first worlds sharing an end cannot coexist with closed sections | PROVED |
| Q_V1 | can non-end-first blind worlds carry a sheltered discontinuity with closed sections? | open (sharpens Q_U1) |

---

## 1. The field U1.5 against the known exclusions

### 1.1 Properties

**Proposition V1.0 (PROVED).** Let c be U1.5's field with arbitrary positive measurable base densities h_l on Q_l, so
that ρ_l = h_l at the odd world l of Q_l and the other two densities are fixed by the rule ρ_m/ρ_k = R₊(|g_m|/|g_k|)
whenever g_k > 0 > g_m. Then:
- **(i)** c is strictly signed and σ-finite (0 < ρ_k < ∞ everywhere on M).
- **(Z)** Z_t is null for every t ∈ Δ, including t ∈ ∂Δ.
- **(UB)** For every k, ess sup over Q_k of ρ_k/(ρ_i + ρ_j) is ∞.
- **(H_Q)** For every t ∈ Δ and every k ∈ supp t, B_t is k-correct on a non-null subset of Q_k.
- **(ii)** B_u = D_{T1} a.e., every B_t with t ∈ ∂Δ is a segment model (hence coherent), and B_t is incoherent for a
  non-null set of t ∈ Δ°.

*Proof.*
- **(i)** This is immediate from the rule: R₊ is a bijection of (0, ∞).
- **(Z)** By 0-homogeneity it suffices to work in the orthant charts of U1 §0.
  - On O_l⁺, chart (1, −a, −b) at the odd world l, t·ĉ = t_l − t_kR₊(a) − t_{k′}R₊(b).
  - On O_l⁻, chart (−1, a, b), t·ĉ = −t_l + t_kR₋(a) + t_{k′}R₋(b).
  - If t_k > 0, then for fixed b the equation t·ĉ = 0 has at most one solution a, because R± is strictly
    increasing. So the zero set is null by Fubini. The case t_{k′} > 0 is the same.
  - If t_k = t_{k′} = 0, then t·ĉ = ±t_l ≠ 0.
- **(UB)** The gambles g = (1 at k, −a, −b) with a, b → 0 lie in U ∩ O_k⁺ ⊆ Q_k. There ρ_i/ρ_k = R₊(a) → 0 and
  ρ_j/ρ_k = R₊(b) → 0.
- **(H_Q)** On the same gambles, B_t is k-correct (it accepts) iff t_k > t_iR₊(a) + t_jR₊(b). Since R₊(x) ≤ (κ+1)x/2
  near 0, this holds for a, b < t_k/(κ+1). That is a non-null set.
- **(ii)** The first two claims are U1.5(b), (c) [PROVED in U1]. The last is M0closed(a) [R2], applied with the
  admissible interior weight u, as U1 §6.1 notes. ∎

NUMERICS (`v1_checks.out` (A)): the ratio ρ_k/(ρ_i + ρ_j) reaches 3·10²–4·10³ at a = b = 10⁻⁴, for four (ε, s). For
200 random t per world, B_t is k-correct on 100% of the sampled gambles near the e_k ray.

**Where the Bayes sets are coherent (NUMERICS; `v1_wcoh2.py`, `v1_wmap.py`, `v1_median.py`, `v1_wcoh3.py`).**
- *Method.* Take the cross-section g = 𝟙 + w, w ∈ 𝟙^⊥, on a 700² grid (U lies in u·g > 0). B_t is coherent iff its
  section is convex. The test counts grid points inside the convex hull of the section that lie outside B_t by a
  margin of 10⁻³.
- *Result, for (ε, s) = (0.3, 0.9) and (0.6, 0.5).* The section is convex only:
  - near the vertices (t_k ≳ 0.75–0.8);
  - at t = u;
  - on short pieces of the medians next to u and next to the vertices.
- *Elsewhere* in Δ° the non-convex fraction is between 10⁻³ and 4·10⁻² (the ASCII maps are in `v1_wmap_*.out`).
- *Near u.* At distance 0.02 toward e₁ the fraction is already about 6·10⁻³, and along the median it is 0 there. At
  smaller distances the test cannot resolve anything.

So W_coh := {t : B_t coherent} is, at test resolution, ∂Δ, the three vertex caps, and u with a short median piece.

### 1.2 The known exclusions, one by one

| Exclusion | Does it exclude U1.5's field, or a cover carrying it? |
|---|---|
| M0closed(a) [R2] | Not the field alone: its hypothesis (γ) is false here (V1.0(ii)). It excludes the cover only if (W) holds. That is exactly what V1.5 turns into a statement about the selection. |
| Q2.11(c) [R1] (interior admissibility) | It holds, with p̂ = u, and exactly (Z_u is null). Not an obstruction. |
| Q2.12–Q2.14 [R1] (edges are ratio chains; homogeneity; link classes) | They hold. The edge ratios are R₊ on {g_i > 0 > g_j} and R₋ on {g_i < 0 < g_j}, which are 0-homogeneous. On Q_i, r_ij/r_ik = ρ_j/ρ_k by construction. |
| U1.1–U1.3 [PROVED in U1] | They hold. The separating level is S[m₀, m₀′] (U1.5(d)). |
| Q2.10(b),(c), T2n.3 [R1] (patch impossible, persistent sheltering) | These are constraints on the cover's localizing families, not on the field. A cover needs D̃^i_m ∩ D̃^j_m ∩ R_ij non-null for every m. With a (CA⁺) world k, the pair is the other two. |
| H1.2 [R1] | It needs configuration (V) (one blind world, two integrable partners) and concludes ¬(Loc). In an all-(Loc) (E∗)-type cover two worlds are non-(CA⁺) (T2n.3), so H1.2's hypotheses fail. |
| K3.5 [R1] (patch theorem) | It excludes the cover as soon as one patch Y° exists. Q2.10(b) and T2n.3 show that a patch exists unless the localizations shelter, so the cover must shelter. The field is untouched. |
| K1.6 / Q_W pair form [R1 / open] | Anti-safe indices with {i, j} ⊆ supp p are needed for every admissible safe triple. This is a constraint on the selection, again not on the field. |

**Conclusion of §1 (PROVED, from the table).** No proved theorem excludes the field. Every proved obstruction that a
cover carrying it meets is an obstruction on the localizing families or on the selection, and all of them say that
the cover must shelter. §§3–5 say where the selection must use the shelter.

---

## 2. Edge blocks on segment hosts

**Lemma V1.1 (PROVED).** Let {i, j} be an edge with third world l. Let r = r_ij be the U1.5 edge ratio on R_ij, equal
to R₊(x) on {g_i > 0 > g_j} and R₋(x) on {g_i < 0 < g_j}, with x = |g_j|/|g_i|. Let λ be a finite measure equivalent to
μ on R_ij ∩ U. For s ∈ [0, ∞] let C^s be the edge model with world-i errors {r > s} on R_ij, equal to P_i on Q_l and
accepting N₊. Put ξ(g) := λ({r > r(g)})/λ(R_ij) ∈ [0, 1] and b(s) := λ({r > s})/λ(R_ij). Then:
1. **(segment models)** C^s = S[a(s), b(s)] a.e. (U1.5(b)). It is coherent, and it lies in the edge domain 𝓔_ij of
   T2n.2: K := co(K′ ∪ [a, b]) meets [e_i, e_j] and lies in co(K′ ∪ [e_i, e_j]), so K3.7′ [R1] gives D_K = P_i on Q_l.
2. **(nested, no flat jumps)** s ↦ {r > s} is decreasing, and every level set {r = s} is null: it is the union of the
   two cones {x = R±⁻¹(s)}. So s ↦ C^s is continuous in measure, C^∞ = P_i and C^0 = P_j.
3. **(first-error coordinate)** ξ pushes λ/λ(R_ij) to Lebesgue measure on [0, 1], and E_i(C^s) ∩ R_ij = {ξ < b(s)} a.e.
4. **(index map)** For the selection on the edge, s(p) = p_i/p_j makes p ↦ b(s(p)) continuous on [e_i, e_j], with
   b = 0 at e_i and b = 1 at e_j.

*Proof.*
- **1.** For [a, b] ⊆ [e_i, e_j], K ∩ [e_i, e_j] ⊇ [a, b] ≠ ∅, and K ⊆ co(K′ ∪ [e_i, e_j]). Apply K3.7′.
- **2.** The distribution function F(s) := λ({r ≤ s}) is continuous, because the level sets are null.
- **3.** Since F is continuous, ξ = 1 − F(r)/λ(R_ij) is uniform. Also {ξ < b(s)} = {r > s} up to the null level set.
- **4.** p ↦ s(p) is continuous into [0, ∞], and b is continuous and monotone. ∎

**Transfer (CHECKED: a reading of T2n.2 [R1, T12n_referee §2.2] and P1.10–P1.14 [R1, P1_referee]).** The referee's
re-derivation of T2n.2 (T12n_referee §2.2, "Sign analysis", "F is continuous") uses only the following:
- (R_ij ∩ U, λ) is non-atomic;
- there is a chain coordinate pushing λ to Lebesgue measure, with c_b = {x < b} (mod null);
- each C_b is coherent and lies in 𝓔_ij;
- the N₊ rules;
- the continuity of the index map.

All of these hold by V1.1(1)–(4). P1's block construction (blocks, thin sources, selectors, the cones T and T′) is
written entirely in (λ, x, b) (P1 §§2–3). The one exception is (LF) at the interior chain members (C2.1(4)), which
T2n.1 states for the two-world system. It is not needed in a three-world cover: there, (LF) is required only at T1
and is automatic on M_U. Hence the three edge blocks of (E∗_seg) exist on the U1.5 segment hosts:
- on 𝓔₂₃, P1 ⊕ mirror with λ = normalised μ;
- on 𝓔₁₂ and 𝓔₁₃, P1.10 with λ = ρ₁μ normalised.

In each block both non-additive worlds are totally blind on the edge region. This verifies U1.6's "edge blocks"
item directly. U1.6's (Loc) clause remains a CONJECTURE. It is not used below: §§3–5 assume all-(Loc).

---

## 3. Order upper semicontinuity

**Lemma V1.2 (PROVED; inputs strict (G) and (S) only).** Let a ranking on M_U satisfy strict (G) and (S). Let p ∈ Δ,
let k be a world, let W′ ⊆ Q_k ∖ E_k(C_p) be non-null, and put Y := C_p △ W′. Let p_n → p. Then there is N with
k ∈ supp p_n and C_{p_n} ⪯_k Y for all n ≥ N. More generally, for any model Y and any set J of worlds with C_p ⋠_j Y
for all j ∈ J, eventually some k ∉ J, k ∈ supp p_n, has C_{p_n} ⪯_k Y.

*Proof.*
- On W′ ⊆ Q_k, C_p is k-correct and so wrong at both other worlds j. Toggling W′ makes Y j-correct there. So
  E_j(Y) = E_j(C_p) ∖ W′, a strict decrease, and strict (G) gives Y ≺_j C_p, hence C_p ⋠_j Y, for both j ≠ k.
- Y ∈ M_U, and it is regular if C_p is.
- By competitiveness, each n has k_n ∈ supp p_n with C_{p_n} ⪯_{k_n} Y.
- If k_n = j ≠ k for infinitely many n (one fixed j), the section {q : C_q ⪯_j Y} is closed (S) and contains those
  p_n, hence contains p. Then C_p ⪯_j Y, a contradiction. So k_n = k for all large n.
- The general form has the same proof. ∎

**Corollary V1.2′ (PROVED).** Let world k be additive with integrable density, so that X ⪯_k Y ⟺ ψ_k(X) ≤ ψ_k(Y). Then
f_k(p) := ψ_k(C_p) is lower semicontinuous on Δ. It is continuous at every p with Q_k ∖ E_k(C_p) non-null.

*Proof.*
- {f_k ≤ γ} = {p : C_p ⪯_k X} for any X with ψ_k(X) = γ, and such X exist by non-atomicity. This set is closed by (S).
- Upper semicontinuity: V1.2 gives f_k(p_n) ≤ f_k(p) + ρ_k(W′) eventually, and ρ_k(W′) can be taken arbitrarily
  small. ∎

*Reading.* V1.2 is a semicontinuity of the selection in the **order** at world k. A selection may jump, but the
models it jumps to must be at least as good at k as C_p made slightly worse at k. The next result turns this into
measure-continuity wherever the comparisons involved are localized.

---

## 4. Discontinuities are sheltered

**Standing hypothesis (A).**
- (H_U) holds on M_U, and every world k has a (Loc) datum.
- For a (CA⁺) world (ρ_k ∈ L¹, endorsing every relevant comparison), the datum is (ρ_k, ∅).
- For every other world, the datum is enlarged as in Q2.10(a) [R1] to (ρ_k, D̃^k), so ρ_k ≤ m off D̃^k_m.
- Γ(p) ≠ ∅ for every p (Q2.11(a) [R1]).

**Theorem V1.3 (PROVED).** Assume (A). Let p ∈ Δ and w ∈ Γ(p), with Z_w null and with B_w k-correct on a non-null
part of Q_k for every k ∈ supp w (this is (Z) and (H_Q) at w). Let p_n → p with limsup_n Φ_w(C_{p_n}) > 0. Then there
are k ∈ supp w and j ≠ k, both with non-empty localizing families, such that the following holds for every m and N:
there is n ≥ N with

  μ(G_n ∩ D̃^k_M ∩ D̃^j_m ∩ R_kj) > 0 for every M,  where G_n := E_k(C_p) ∖ E_k(C_{p_n}).

In words: at infinitely many n, at every depth M of k's family and every depth m of j's family, C_{p_n} is k-correct
on a sheltered set of R_kj where C_p is k-wrong (hence j-correct). In particular D̃^k_M ∩ D̃^j_m ∩ R_kj is non-null for
all M, m.

*Proof.* C_p = B_w a.e., by Z_w null. Fix η > 0 with Φ_w(C_{p_n}) > 3η for infinitely many n.

1. **Gain sets.** For k ∈ supp w choose a non-null W′_k ⊆ Q_k ∖ E_k(C_p) with:
   - W′_k ⊆ M ∖ D̃^k_{m₁} for some m₁;
   - ρ_i ≤ m₁ on W′_k for every i;
   - Σ_{k∈supp w} w_kρ_k(W′_k) < η.

   This is possible by (H_Q), since the deep sets shrink to null sets. Note that ρ_i(W′_k) > 0 for i ≠ k.
2. **Tests.** Fix m₀ ≥ m₁. For k ∈ supp w with D^k ≠ ∅, let
   - S^k_{m₀} := ⋃_{i≠k} (D̃^i_{m₀} ∩ R_ki), with D̃^i := ∅ for (CA⁺) worlds i;
   - K^k_M := (E_k(C_p) ∩ D̃^k_M) ∖ S^k_{m₀};
   - **Y″_k := (C_p △ W′_k) △ K^k_M**: it equals C_p made k-wrong on W′_k and k-correct on K^k_M.

   Choose M = M(m₀) ≥ m₀ so large that, for both i ≠ k,
   - m₀μ(D̃^k_M) < ρ_i(W′_k) when D^i ≠ ∅;
   - ρ_i(D̃^k_M) < ρ_i(W′_k) when i is (CA⁺).

   For a (CA⁺) world k put Y″_k := C_p △ W′_k. Every Y″_k is regular.
3. **C_p ⋠_i Y″_k for both i ≠ k.** Put δ := 1_{E_iY″_k} − 1_{E_iC_p}.
   - δ = −1 on W′_k.
   - δ ≤ 0 on K^k_M ∖ R_ki, where i agrees with k.
   - δ = +1 only on K^k_M ∩ R_ki ⊆ D̃^k_M ∖ D̃^i_{m₀}.

   So δ ≤ 0 on D̃^i_{m₀} and the comparison is D̃^i-localized and relevant. If it were accepted, (Loc) would give
   ρ_i(W′_k) ≤ ρ_i(δ⁻) ≤ ρ_i(δ⁺). But ρ_i(δ⁺) ≤ m₀μ(D̃^k_M) (or ρ_i(D̃^k_M) in the (CA⁺) case), which is < ρ_i(W′_k).
4. **Forced acceptances.** By step 3 and the general form of V1.2 (with J = the other two worlds), there is N(m₀)
   such that C_{p_n} ⪯_k Y″_k for every n ≥ N(m₀) and every k ∈ supp w.
5. **If all are localized, the cost is small.** Fix n ≥ N(m₀) and suppose every comparison C_{p_n} ⪯_k Y″_k
   (k ∈ supp w) is D̃^k-localized. Write A := C_{p_n}.
   - (Loc) gives ρ_k(E_kA ∖ E_kY″_k) ≤ ρ_k(E_kY″_k ∖ E_kA) < ∞.
   - E_kY″_k ∖ E_kC_p = W′_k, and E_kY″_k ⊆ E_kC_p ∪ W′_k. Hence E_kA ∖ E_kC_p ⊆ (E_kA ∖ E_kY″_k) ∪ W′_k and
     E_kY″_k ∖ E_kA ⊆ (E_kC_p ∖ E_kA) ∪ W′_k. So D_k := ρ_k(E_kA ∖ E_kC_p) − ρ_k(E_kC_p ∖ E_kA) ≤ 2ρ_k(W′_k), with
     the positive part finite. (D_k = −∞ is allowed a priori.)
   - The pointwise identity Σ_k w_kρ_k(1_{E_kA} − 1_{E_kB_w}) = |w·c|·1_{A△B_w} holds on M (H1.0(b); H12_referee
     §1.2). Each summand with k ∈ supp w has an integrable positive part. So the integrals add, and
     Φ_w(A) = Σ_{k∈supp w} w_kD_k ≤ 2Σ_k w_kρ_k(W′_k) < 2η.
6. **So some acceptance is not localized.** For every m₀ and every n ≥ N(m₀) with Φ_w(C_{p_n}) > 3η (infinitely many
   such n), some k ∈ supp w has a non-localized acceptance C_{p_n} ⪯_k Y″_k.
   - By the construction, k then has D^k ≠ ∅. Then 1_{E_kY″_k} − 1_{E_kC_{p_n}} is not ≤ 0 on any D̃^k_{M′}.
   - On D̃^k_{M′} (M′ ≥ M), Y″_k is k-wrong only on (E_k(C_p) ∩ S^k_{m₀}). So for every M′ the set
     G_n ∩ D̃^k_{M′} ∩ S^k_{m₀} is non-null.
   - S^k_{m₀} is a union over the two worlds i ≠ k, and the sets decrease in M′. So one i =: j has
     G_n ∩ D̃^k_{M′} ∩ D̃^j_{m₀} ∩ R_kj non-null for every M′. Then D^j ≠ ∅.
7. **Pigeonhole.** Some pair (k, j) arises in step 6 for infinitely many m₀, each time with arbitrarily large n. Since
   D̃^j_{m₀} ⊆ D̃^j_m for m ≤ m₀, the statement holds for every m. ∎

*Remarks.*
- This is K3.5 Step 1 / K1.2 run **along a convergent sequence of indices** instead of against a fixed near-Bayes
  test. The KKM covering is replaced by Lemma V1.2, which needs only closed sections at the limit index. No
  integrability is used. Infinite minority mass and infinite costs are allowed, because only difference sets enter,
  and these sit off the deep sets.
- The sheltering found here is **used by the selection**: the approaching models beat C_p at k exactly on the shelter.
  T2n.3 / Q2.10(c) only say that a shelter exists.
- (CA⁺) worlds never occur in the pair. So in (E∗)-type covers (k, j) ∈ {(2, 3), (3, 2)}, in agreement with T2n.3.

---

## 5. Every such cover has a sheltered discontinuity: where M0closed(a) is defeated

**Lemma V1.4 (PROVED).** Let Γ̂ : Δ ⇉ Δ have a closed graph and non-empty convex values, and let it be face-preserving:
Γ̂(p) ⊆ Δ_{supp p}. Then every t ∈ Δ lies in Γ̂(p) for some p.

*Proof.*
- Let P(w) := argmin_{q∈Δ} q·(w − t). Then P is a closed-graph correspondence with non-empty convex compact values.
- Kakutani's theorem on Δ × Δ, applied to (p, w) ↦ P(w) × Γ̂(p), gives p ∈ P(w) and w ∈ Γ̂(p).
- Put K := argmin_k (w_k − t_k) and μ* := min_k (w_k − t_k), so μ* ≤ 0 since Σ(w − t) = 0. Then supp p ⊆ K.
- By face-preservation, w_j = 0 for every j ∉ supp p, in particular for j ∉ K. Hence Σ_{k∈K} w_k = 1. Since
  w_k = t_k + μ* for k ∈ K, this gives |K|μ* = 1 − Σ_{k∈K} t_k ≥ 0.
- So μ* = 0, every w_k − t_k ≥ 0, and since they sum to 0, w = t. ∎

**Theorem V1.5 (PROVED).** Assume (A), and suppose c satisfies (Z), (UB) and (H_Q). Then the selection is not
continuous in measure at some p ∈ Δ. For every sequence p_n → p along which μ(C_{p_n} △ C_p) does not tend to 0, and
every w ∈ Γ(p), we have limsup Φ_w(C_{p_n}) > 0. So the conclusion of Theorem V1.3 holds: some pair (k, j) of
non-(CA⁺) worlds, k ∈ supp w, carries the discontinuity by sheltered gains on R_kj. This applies to every all-(Loc)
cover whose (Loc) data carry U1.5's field, with any base densities (Prop. V1.0).

*Proof.* First, the second sentence. Let w ∈ Γ(p). By (Z), C_p = B_w a.e., and |w·c| > 0 a.e. If Φ_w(C_{p_n}) → 0,
then μ(C_{p_n} △ C_p) → 0: split according to whether |w·c| > ε, and use μ({|w·c| ≤ ε}) → μ(Z_w) = 0 as ε → 0. So
along a sequence without convergence in measure, limsup Φ_w(C_{p_n}) > 0, and Theorem V1.3 applies (its hypotheses
at w are (Z) and (H_Q)). It remains to show that the selection cannot be continuous in measure at every p. Suppose it
is.
1. **Closed graph.** Let p_n → p, w_n ∈ Γ̂(p_n) and w_n → w. Along a subsequence 1_{C_{p_n}} → 1_{C_p} a.e. At a.e.
   g ∈ C_p, eventually g ∈ C_{p_n}, so w_n·c(g) ≥ 0 and in the limit w·c(g) ≥ 0. The same holds off C_p. So
   w ∈ Γ̂(p). Γ̂(p) is convex (the Bayes condition is linear in w) and non-empty (it contains Γ(p)).
2. **Face-preservation.** Let p ∈ Δ_S, take w′ ∈ Γ(p) ⊆ Δ_S, and suppose w ∈ Γ̂(p) has w_k > 0 for some k ∉ S.
   - On Q_k the two worlds i, j ≠ k agree, so w′·c has sign σ_i ≠ 0. By (Z), C_p = B_{w′} is k-wrong on all of Q_k.
   - Being w-Bayes, C_p then forces w_kρ_k ≤ w_iρ_i + w_jρ_j a.e. on Q_k. So ρ_k/(ρ_i + ρ_j) ≤ 1/w_k there,
     against (UB).
3. **Contradiction.** Lemma V1.4 makes every t ∈ Δ° a Bayes weight of a selected, hence coherent, model. That is (W)
   of Q2.16, and Q2.16(6) [R1; via M0closed(a), R2, and Q2.11(c), which uses T1 ∈ C_L] contradicts (H_U). ∎

**Reading: exactly where the cover must defeat M0closed(a).**
- The σ-finite field is strictly positive, and T1 is its Bayes model at u. M0closed(a) then says that (γ) fails.
- Q2.16 reduced the all-(Loc) case to (W). V1.5 shows that (W) can fail only through a **discontinuity of the
  selection in measure** at which, for every pair of depths, the approaching selected models beat the limit model at
  a world k ∈ supp w(p) **inside the common localizing set of k and a partner j on R_kj**.
- With the NUMERICS of §1.1 the Bayes weights of the selection must jump across the incoherent region I. They go from
  the component of W_coh carrying T1 (if T1 is selected) or T1's tie partner, to the vertex caps or the boundary. The
  shelter is used at that jump.
- Combined with V1.2, the blind world k must **accept** the specific non-localized comparisons C_{p_n} ⪯_k Y″_k of
  V1.3 (step 4), for every choice of (W′, m₀, M).
- Relation to K1.6 / Q_W in pair form: V1.5 does not produce anti-safe indices, and K1.6 does not produce
  discontinuities. Both are necessary. V1.5 is the statement at the level of the selection with no test triple. In
  (E∗) covers both concern the pair {2, 3}.

---

## 6. End-first sheltering is impossible

**Proposition V1.6 (PROVED).** Let a ranking (any number of worlds) have a selection with closed sections, and let
C_{e_i} = P_i and C_{e_j} = P_j for two worlds i ≠ j. Let x : M_U → [0, 1] satisfy x(P_i) = 0 and x(P_j) = 1, and:
- **(E2) end-first, opposite:** x(X) < x(Y) ⇒ X ≺_i Y, and x(X) > x(Y) ⇒ X ≺_j Y;
- **(E3) test models at each level:** for every a ∈ (0, 1) there are models X^a_r, Z^a_r (r ∈ ℕ) with x = a such
  that every p with x(C_p) = a has C_p ⋠_i X^a_r and C_p ⋠_j Z^a_r for all large r.

Then the hypotheses are contradictory.

*Proof.*
- Put f(p) := x(C_p) and fix a ∈ (0, 1). By (E2), x(C_p) < a ⇒ C_p ≺_i X^a_r, and x(C_p) > a ⇒ X^a_r ≺_i C_p.
  With (E3) this gives {f < a} = ⋂_r {p : C_p ⪯_i X^a_r}, which is closed. Likewise {f > a} is closed, using world j
  and Z^a_r.
- e_i ∈ {f < a} and e_j ∈ {f > a}. If a ∉ f(Δ), these two disjoint closed sets would cover the connected Δ. So every
  a ∈ (0, 1) is a value of f.
- Then {f = a} = Δ ∖ ({f < a} ∪ {f > a}) is open and non-empty for every a ∈ (0, 1). These are uncountably many
  disjoint non-empty open subsets of the separable space Δ, which is impossible. ∎

**The lexicographic case satisfies (E2), (E3).** Let Ξ_m ⊆ R_ij ∩ M be decreasing, non-null, with μ(Ξ_m) → 0 (a
shared end). Let π be a state on L^∞ that vanishes on M ∖ Ξ_m for every m and has π(Ξ_m) = 1, and put
x(X) := π(E_i(X) ∩ Ξ_1). Let worlds i and j rank lexicographically:
- world i by (x(X), ψ_i(X));
- world j by (π(E_j(X) ∩ Ξ_1) = 1 − x(X), ψ_j(X));
- with integrable densities ρ_i, ρ_j > 0.

Then:
- (E2) holds.
- For (E3), take X^a_r equal to P_i off Ξ_r, and on Ξ_r i-wrong on a subset of π-measure a. Then x(X^a_r) = a and
  ψ_i(X^a_r) ≤ ρ_i(Ξ_r) → 0.
- A selected C_p with x(C_p) = a ∈ (0, 1) has ψ_i(C_p) > 0, so C_p ⋠_i X^a_r for large r. Similarly for Z^a_r.

So **no end-first lexicographic pair shares an end along a closed-section selection**. The jump of the end coordinate
from P_i to P_j cannot even sit at a vertex.

*Why P1 escapes.*
- The P1 worlds are not end-first. Their cones T = {f : ∫_{x≥t} f dλ ≥ 0 ∀t} weigh the end only through tail
  integrals of finite λ-mass.
- In T2n.1 the two ends are disjoint (x → 1 and x → 0). So V1.6 does not apply, consistent with T2n.1 being a full
  system.

*Consequence for Q_U1.* The non-localized acceptances that V1.3 step 4 forces at a sheltered discontinuity cannot come
from an end-first preference on the shelter. They have to come from an acceptance structure that is not end-first, and the
acceptances themselves must be non-localized: by V1.3 step 5, localized (hence endorsed) acceptances force
Φ_w(C_{p_n}) → 0.

---

## 7. The construction attempt, and where it stopped (failure report)

**Target.** (E∗_seg):
- world 1 additive with integrable ρ₁ > 0;
- worlds 2, 3 of P1 type, with the edge blocks of §2 on the U1.5 segment hosts;
- the σ-finite field equal to U1.5's;
- a selection p ↦ C_p through T1, defined on all of Δ;
- worlds 2, 3 defined on all of M_U, including comparisons out of interior selected models, through the exact
  consistency test (P3.2 with R5), with explicit sections.

**What any completion must contain (PROVED above).**
1. Every selected model is an exact Bayes model of the field, C_p = B_{w(p)} with w(p) ∈ W_coh ∩ Δ_{supp p} (Q2.11(a)
   with (Z)). So the interior selection uses only u (T1), the vertex caps, the median pieces and boundary weights
   (NUMERICS §1.1).
2. ψ₁(C_p) is continuous wherever C_p is right at 1 on part of Q₁ (V1.2′), and lower semicontinuous everywhere.
3. A sheltered discontinuity on R₂₃ exists (V1.5). At it, world 2 (say) must accept C_{p_n} ⪯₂ Y″₂ for all tests of
   V1.3 step 2, and these acceptances are not localized.
4. The shelter can be the natural one of T2n.7: the overlap of world 2's 12-end and world 3's 23-end near the e₃
   ray, which persists for segment hosts because their chain ends are those of the linear host. On it, B_t is
   3-correct at depth iff t₃ > 0 or t = e₁ (NUMERICS (B) in `v1_checks.out`, three depths, two geometries). Then one
   side of the discontinuity is a {1, 2}-edge model (w₃ = 0) selected at interior indices, and the other side has
   w₃ > 0.
5. World 2's preference on the shelter cannot be end-first (V1.6).

**Attempts that failed.** The first two fail for proved reasons. The third is a reading.
- *Selection T1 on a closed set S ⊆ Δ°, with p ↦ C_{π(p)} elsewhere, for a continuous retraction π of Δ ∖ int S onto
  ∂Δ.*
  - By degree, π(∂S) = ∂Δ. So some p ∈ ∂S has π(p) arbitrarily close to e₁.
  - At such p, V1.2′ makes ψ₁(C_{p_n}) → ψ₁(T1) along p_n → p from outside S.
  - But ψ₁(C_{π(p_n)}) is close to ψ₁(C_{π(p)}), which tends to 0 < ψ₁(T1) as π(p) → e₁. Contradiction.
- *Lexicographic blind worlds:* a charge at the shared end first, ρ_k second. This makes worlds 2, 3 (Loc) with
  data (ρ_k, ends), but it is excluded by V1.6.
- *P1 tail-cone worlds extended to interior indices.* On the edge chain their acceptances are tail inequalities of
  finite λ-mass. Such inequalities pass to limits in measure, so on their own they cannot produce the non-localized
  acceptances of item 3. (This is a reading, not a theorem.) The generators g_F of P1 (the blocks) are the only non-closed ingredient. I could not place generators on the shelter of item 4 so that the
  forced acceptances of item 3 hold while the partner rejections of V1.3 step 3 and closed sections in the 2-simplex
  survive. This is where the construction broke.

**The single remaining obstruction.**

> **Q_V1.** Is there a pair of (Loc) blind worlds k, j, sheltering each other on R_kj, not end-first in the sense of
> (E2)–(E3), together with a selection with closed sections, such that at some p, for a sequence p_n → p with
> limsup Φ_{w(p)}(C_{p_n}) > 0, world k accepts every forced comparison C_{p_n} ⪯_k Y″_k of V1.3 (for all W′, m₀, M)?
> All the other axioms of (H_U) must hold as well.

- **No** closes every all-(Loc) cover whose field satisfies (Z), (UB), (H_Q). In particular it closes Q_U1 for U1.5's
  field and every segment-host cover carrying it. The reason is V1.5.
- **Yes** must still supply the anti-safe indices of K1.6 for every admissible safe triple, and T1 ∈ C_L.
- Not closed by anything here:
  - covers with a non-(Loc) world;
  - all-(Loc) covers whose field has non-null ties at some weight (then V1.3 gives convergence only off Z_w);
  - fields failing (UB) (then Γ̂ need not be face-preserving).

---

## 8. Dependencies, risk points, files

**Used (status).**
- Q2.10(a), Q2.11(a), (c), Q2.16(6) [R1, Q24_referee].
- M0closed(a) [R2], through Q2.16 and V1.0(ii).
- H1.0(b) identity with the H12_referee §1.2 bound [R1].
- K3.7′ [R1].
- U1.5 [PROVED in U1, unrefereed].
- T2n.2 / P1.10–P1.14 [R1], for the transfer only.
- T2n.3 [R1], T2n.7 [R1], K1.6 [R1], for readings only.
- Kakutani's fixed-point theorem.
- Fubini.

**Not used.**
- (C), except through (H_U) inside Q2.16.
- (Nest_e).
- Any bounded endorser.
- L4, M1, N1, N2.
- The interior definition of any world.

**Points a referee should check, by risk.**
1. V1.3 step 3: that δ⁺ lies in D̃^k_M ∖ D̃^i_{m₀}. This needs the exclusion S^k_{m₀} in the definition of K^k_M.
   Also that the (CA⁺) case uses integrability rather than enlargement.
2. V1.3 step 5: the inclusions giving D_k ≤ 2ρ_k(W′_k), and adding the integrals when some D_k = −∞ (only positive
   parts are known to be finite).
3. V1.3 step 6: "not localized" ⟺ gains of C_{p_n} over C_p in D̃^k_{M′} ∩ S^k_{m₀} for all M′. This uses the fact
   that W′_k misses D̃^k_{M′} for M′ ≥ m₁.
4. V1.5 step 2: face-preservation from (UB). This uses C_p = B_{w′} with w′ ∈ Γ(p) ⊆ Δ_S.
5. Lemma V1.4: the Kakutani step and the computation μ* = 0.
6. V1.6: closedness of {f < a} as an intersection of sections. (E3) is needed for every a ∈ (0, 1).
7. V1.1 / transfer: that nothing in P1.10–P1.14 uses the linear form of the host beyond (λ, x, nested c_b, coherence
   of C_b).

**Files** (`v1py/`; run each with `python3 -I -B` from inside `v1py/`).
- `v1_common.py`: U1.5 field (re-implemented from U1's description).
- `v1_checks.py` → `v1_checks.out`: (A) (UB), (H_Q); (B) the deep behaviour of B_t on H_η.
- `v1_wcoh2.py`: the convexity test.
- `v1_wmap.py` → `v1_wmap_0.3_0.9.out`, `v1_wmap_0.6_0.5.out`: maps of W_coh. Arguments ε, s, N.
- `v1_median.py` → `v1_median.out`; `v1_wcoh3.py` → `v1_wcoh3.out`: rays and medians through u.
