# Referee report on M1_notes.md (round 20)

16 Oct 2026. Adversarial reading against L4_notes + L4_referee, L1_notes + L1_referee, K3_notes + K3_referee,
L2_notes, L23_referee, BRIEF13/BRIEF17, and the write-up §§2–3 and §7 (Thm. kkm, Prop. M0, Thm. Estructure, Lemmas
quasilin/ball, Props. crosspin/chainchords/carrying, Thm. M0closed). Every PROVED item was re-derived line by line.

Numerics:
- `m1py/shadow_check.py` and `m1py/vertex_check.py` were rerun with `python3 -I`. Both outputs are byte-identical to
  the stored `.out` files (reruns in `m1ref_py/shadow_rerun.out`, `m1ref_py/vertex_rerun.out`).
- My checks are in `m1ref_py/ref_checks.py` (+ `.out`): (A) the set identities behind M1.1/M1.6/M1.7 (0 violations);
  (B) the M1.11 mechanism (Λ₁ = E₁(T1), ρ₂ = ρ₃ = 1: B_q = Y₂ exactly near e₁, and B_q fails midpoint convexity);
  (C) the R_ij-arcs of each facet; (D) the M1.2 values m·w₂₁ = m·w₃₁ = −a. NUMERICS only; no verdict rests on them.

---

## 0. Verdicts

| Item | Verdict |
|---|---|
| §1 objects (C(g), J_l, W_l, Y_l, A(c), (ZER)) | CORRECT |
| **M1.1(a)** T1-shadow: c ≠ 0, B_q = T1 at every q ∈ Δ°, A(c) = Δ, d_t ≡ 0, blind-set structure | **CORRECT** |
| **M1.1(b)** A(c) = Δ ⇔ vertices ⇔ ρ_k = 0 on E_k(T1) | **CORRECT** |
| **M1.1(c)** the (V) field (0, σ₂, σ₃) | **CORRECT** |
| M1.1′(a), (b) | CORRECT |
| M1.1′(c) "fixed-point route cannot conclude"; sharpness of Thm. main / M0closed(a) in strict signs | CORRECT. **GAP (wording):** "use strict signs *exactly* in Lemma UVN" is false (§1.3) |
| **M1.2** (V) under (B1): e₂ ∈ K₁, e₃ ∈ K₀, Λ₁ ⊇ M ∩ {g₁ > 0}, V₁ ⊆ {g₁ < 0} ∖ cl D_{T1} | **CORRECT** (in fact K₁ ∩ [e₁, e₂] = {e₂}) |
| M1.10 edge limits | CORRECT |
| **M1.11** exact shadow-blindness at one world next to a world seeing J_j ∪ J_k | **CORRECT**. Reading sentence "needs all three worlds blind, as in c^T" overstates (§2.3) |
| §2.4 (L1.D) | correctly labelled CONJECTURE; "strongest form" is informal |
| **M1.3** face KKM with strict (G) | **CORRECT** |
| M1.4 Pareto-tie principle | CORRECT |
| M1.5(a), (b), (c) | CORRECT. **GAP (wording):** (c) "upgrades K3.7(β)" only when world 1's ρ₁μ endorses *all* relevant comparisons (§3.3) |
| **M1.6(a)** facet-plane lemma; **(b)** Y_l incoherent | **CORRECT**. (a) is local: any open N ∋ h suffices (needed for M1.9′(b)) |
| **M1.7** edge exchange in every cover | **CORRECT**, fully re-derived. It uses only (LA), (S), strict (G) (§4) |
| M1.8 (and the shadow corollary) | CORRECT; independent second proof via M1.5(b) (§4.3) |
| **M1.9** | **CORRECT**; second proof directly from M1.7; extends to arbitrary (non-CA) endorsers (§5.1) |
| M1.9′(a), (c) | CORRECT ((c) needs the CA endorsers of M1.9, implicit) |
| **M1.9′(b)** "two-sided tie shell, frozen ratio along every R_ij-arc of some facet" | **GAP (fixable).** Each one-sided accumulation statement is proved; "two-sided … of *some* facet", "frozen ratio" and "shell" are not (§5.2). Sharper replacement given |
| §4.1 (W1)–(W4) | CORRECT ("thin pieces" in (W2) is not proved) |
| §4.2.1 lexicographic / zero-exchange-rate worlds excluded | CORRECT (one such world already suffices) |
| §4.2.2 L2's device: (ZER) and wrong orientation | CORRECT as a description; (i) is a proved exclusion only for the device as built, with its blind set aimed *exactly* at E_i(T1) ∩ R_ij |
| §4.2.3 K3.3 tilt: right orientation, no closed sections | CORRECT as a description; "L2 repaired closedness by finitely many levels, which re-creates a CA endorser" is heuristic, not PROVED |
| §4.3 (V) (2,3)-Bayes condition on E₁(T1) ∩ R₂₃ | CORRECT (with worlds 2, 3 additive with positive densities) |
| §0 headline "every remaining degenerate case is settled POSITIVELY" | **GAP (wording).** Not shown for two-blind-world interior cases; L1.D is conjectured *negative* (§6) |
| **Q_M1** | well posed; **GAP:** "Equivalently … admissible at all three vertices" is not an equivalence; the "No ⇒ only these remain" list is incomplete (§6) |

**Net assessment.** The note's two central claims are right and important.
1. **M1.1** is a clean, elementary and correct theorem: with weak signs allowed, the shadow c^T satisfies everything the
   fixed point of L4.1 is known to satisfy, and even (BU) with K_q ≡ T1. So Theorem main and M0closed(a) are sharp in
   their strict-sign hypothesis, and no argument from the CA field alone can close the degenerate cases.
2. **M1.7** is correct and is genuinely the right ranking-level tool. It is the first statement that uses (S) and
   strict (G) *against* blind sets, and with it M1.8/M1.9 kill every zero-exchange-rate realisation.

The flagged-risky items M1.3, M1.9 and M1.11 are correct. M1.9′(b) overstates what is proved; the repair is easy
and gives a sharper dichotomy.

---

## 1. Field level: M1.1, M1.1′

### 1.1 M1.1(a) — CORRECT
- On M, C(g) ≠ ∅ (T1 accepts ⇒ correct where g_k > 0; T1 rejects ⇒ correct where g_k < 0; g mixed) and C(g) ≠ Ω.
- For k ∈ C(g), σ_k(g) = s_T(g); for k ∉ C(g), ρ_k = 0. Hence q·c = s_T Σ_{k∈C(g)} q_kρ_k, nonzero with sign s_T
  for q ∈ Δ°, ≥ 0 times s_T for q ∈ ∂Δ. So B_q = D_{T1} (mod null, D_{T1} ⊆ U), Z_q ∩ M = ∅, A(c) = Δ.
- d_t = 0 at every t ∈ Δ: T1 is coherent and is a pointwise ψ^t-minimiser (rejecting minus accepting costs t·c).
- Λ_i ∩ Λ_j = {C(g) ⊆ {l}} = J_l; J₃ ⊇ D_{T1} ∩ (−,−,+) near r₁₂ (a non-empty open set); Λ₁ ∩ Λ₂ ∩ Λ₃ = ∅.
- J_l = E_i(T1) ∩ Q_l: "wrong at i and j, right at l" forces sign g_i = sign g_j ≠ sign g_l. `ref_checks` (A): 0
  violations.
- The side statement is the definition of E_k(T1) read on each side of a facet point off the coordinate planes.

### 1.2 M1.1(b), (c) — CORRECT
- (b): A(c) is closed and convex; e_k ∈ A(c) iff s_Tρ_kσ_k ≥ 0 a.e. iff ρ_k = 0 where T1 errs at k. And
  "T1 c-p-Bayes ⇔ p ∈ A(c)" is the definition (T1 ⊇ B_p and T1 ∖ B_p ⊆ Z_p).
- (c): θ > ½ gives P₂, θ < ½ gives P₃, θ = ½ gives P₂ ∩ P₃ = D_{co(K′∪{e₂,e₃})} (D_{K₁} ∩ D_{K₂} = D_{co(K₁∪K₂)}). Open
  edges [e₁, e_j]: P_j. e₁: everything Bayes. d_t ≡ 0. Consistent with M1.2: here S₁ = P₂ = D_{co(K′∪{e₂})}, so
  e₂ ∈ K₁.

### 1.3 M1.1′ — CORRECT, one wording GAP
- (a): c^T is a counterexample to L1.D without its pairwise-null hypothesis (T1 Bayes at every interior p*, (γ),
  ρ_k > 0 off Λ_k). Correct.
- (c), sharpness: c^T satisfies (BU) at every q ∈ Δ° (null ties, B_q = D_{T1}) and (TP) at every p*, and fails only the
  strict-sign clause of Definition realisation. So Theorem main and M0closed(a) are false for weakly signed fields with
  c ≠ 0 a.e. This is a correct and useful sharpness statement.
- **GAP (wording).** "Theorem main and M0closed(a) use strict signs exactly in Lemma UVN" is false. L4_referee §5
  lists four kinds of strict-sign use in M0closed(a) (UVN; the last line of Lemma ball; edgebox; "chords miss the
  vertices"), plus the weak-sign uses in Lemma chords(b). **Fix:** "For c^T, Lemma UVN fails at every vertex
  (K_q ≡ T1), so the chain already fails at pivot Step 0."
- "No argument that uses only the CA fixed point excludes covers": correct for every property derived so far from the
  field alone (all Bayes models, directional limits, edge and vertex limits of c^T equal T1). It does not cover
  arguments using the endorsers themselves; M1.7 is such an argument. Say "the CA field alone".

---

## 2. M1.2, M1.10, M1.11

### 2.1 M1.2 — CORRECT
- L4.3 at p* = e₁ gives Λ₁ ⊇ E₁(T1) ∩ M. On (−,+,+) ⊆ Q₁ ⊆ R₁₂ ∩ R₁₃ the world-1 error set of a model is the model,
  so (β′) gives D_{K₁} ∩ (−,+,+) ⊇ D_{T1} ∩ (−,+,+) and D_{K₀} ∩ (−,+,+) ⊇ D_{T1} ∩ (−,+,+) a.e.
- Open convex sets: A ⊆ B a.e. ⇒ A ⊆ cl B. So P_{K₁}, P_{K₀} ≥ 0 on cl(D_{T1} ∩ (−,+,+)).
- w₂₁ = (−1, 0, κ) and w₃₁ = (−1, κ, 0) lie in relint F₁ (v₁·w = c₀(κ−1) − ε = 0, v₂·w, v₃·w > 0), and the plane
  {g₂ = 0} (resp. {g₃ = 0}) is transverse to v₁^⊥. So both crossings lie in that closure.
- m = (a, 1−a, 0): m·w₂₁ = −a; m = (a, 0, 1−a): m·w₃₁ = −a (`ref_checks` (D)). Hence every point of K₁ ∩ [e₁, e₂] is
  e₂, and every point of K₀ ∩ [e₁, e₃] is e₃: **K₁ ∩ [e₁, e₂] = {e₂}**, slightly more than stated.
- (ii): D_{K₁} ⊆ P₂ empties (+,−,−) ∪ (+,−,+) ⊆ R₁₂; D_{K₀} ⊆ P₃ empties (+,+,−) ⊆ R₁₃. On g₁ > 0 every rejection is
  a world-1 error. (iii) is the table of L4 §4 on the g₁ < 0 orthants.
- Reading: the (V) case under (B1) has Λ₁ ⊇ M ∩ {g₁ > 0} ∪ (D_{T1} ∩ {g₁ < 0}). This is strictly larger than the
  L4.7 boundary case, as it must be.

### 2.2 M1.10 — CORRECT
- Ties: off Λ_i ∩ Λ_j, e_θ(g) vanishes for at most one θ (never if σ_i = σ_j, once if σ_i ≠ σ_j). Fubini.
- The B_{q_m} are coherent. This needs the every-B_q clause of L4.1.2, which holds under (γ₀) + c ≠ 0 a.e. (the
  L4_referee repair); M1.10 assumes exactly that. Alternatively take q_m off the null exceptional set.
- On Λ_i ∩ Λ_j, sign q_m·c = σ_k. Limits in measure of coherent models are coherent. K3.7′ applies when
  Λ_i ∩ Λ_j ∩ Q_k is null. For c^T, E_θ = T1 (on R_ij only the T1-correct one of i, j is live).

### 2.3 M1.11 — CORRECT (flagged risky)
- First limit (s ↓ 0, η fixed): off Λ_i, (1−s)ρ_iσ_i dominates, so the sign tends to σ_i = T1's advice on R⁰_i. On
  Λ_i = W_i ∪ J_j ∪ J_k the sign is that of ηρ_jσ_j + (1−η)ρ_kσ_k, independent of s.
  - Ties on W_i: none, because σ_j = σ_k = s_T and c ≠ 0 forbids ρ_j = ρ_k = 0 there.
  - Ties on J_j ∪ J_k: at most one η per point, since ρ_k > 0 there. For a.e. η they are null.
  - So M_η is a limit in measure of coherent B_q (every B_q coherent, as in §2.2), hence coherent.
- Second limit (η ↓ 0 along good η): W_i → T1; J_k → s_T (ρ_k > 0); J_j → −s_T (ρ_k > 0). The limit is Y_j, coherent.
  This contradicts M1.6(b).
- Both hypotheses are used: Λ_i ⊆ E_i(T1) gives T1 on R⁰_i, and Λ_i ⊇ E_i(T1) puts W_i ∪ J_j ∪ J_k on the frozen
  side. `ref_checks` (B) shows the mechanism directly (B_q = Y₂ near e₁ and midpoint failures).
- **Reading (wording).** "A shadow-type degeneracy with exact blind sets needs all three worlds blind, as in c^T"
  overstates. M1.11 applied to (i, j, k) and (i, k, j) gives only this: ρ_k and ρ_j each vanish on a non-null part of
  J_j ∪ J_k, on disjoint parts since c ≠ 0. It does not give Λ_j = E_j(T1) or Λ_k = E_k(T1). Say so.

---

## 3. Ranking level: M1.3–M1.6

### 3.1 M1.3 — CORRECT (flagged risky)
- S_i = {p ∈ Δ_I : C_p ⪯_i X} is closed: (S) gives closed sections in Δ, intersected with the closed face.
- KKM cover: for J ⊆ I and p ∈ Δ_J, competitiveness of C_p on supp p ⊆ J gives some j ∈ supp p ⊆ J with p ∈ S_j.
  This is the KKM hypothesis on the simplex Δ_I, so ⋂_{i∈I} S_i ≠ ∅. Running kkm on a face is legitimate: competitiveness
  is on supp p, and the face is a simplex.
- C_p ∈ C_L by (S).
- **"E_i determines the model on M_U."** X = E_iX △ P_i. On a pair g ∈ U the evaluable advice is "accept g" or silence,
  and at world i exactly one of them is the better one. So "X's advice is at least as good as C's at g" iff
  g ∉ E_iX ∖ E_iC. Pairs with neither orientation in U give identical advice. Strict (G) then gives X ≺_i C from
  E_iX ⊊ E_iC (mod null).

### 3.2 M1.4 — CORRECT
The kkm dominator C of M1.3 gives relevant comparisons C ⪯_i X (C ∈ C_L, X regular). Endorsement and the hypothesis
give E_{i₀}X ⊆ E_{i₀}C, so C fixes no error at i₀, and M1.3 forces C = X = C_p, p ∈ Δ_I.

### 3.3 M1.5 — CORRECT, one wording GAP
- (a): Σ_I t_iψ_i(Y) − Σ_I t_iψ_i(T) = ∫_{(Y△T)∩M} |Σ_I t_iρ_iσ_i| ≥ 0. Equal-or-better ψ_i at all i ∈ I (t_i > 0)
  forces (Y △ T) ∩ M ⊆ Z^I_t. There T = P_{i₀}, so Y errs at i₀ wherever it differs from T on M. On N₊ T has no
  error. So E_{i₀}T ⊆ E_{i₀}Y and M1.4 applies.
- (b): correct. Only world i's CA endorser is used; world j enters only as i₀. K3.7′ applies because X_ij = P_i on
  Q_k.
- (c): correct for a.e. θ (null ties since ρ_j, ρ_k > 0).
- **GAP (wording).** "This upgrades K3.7(β)'s 'coherent' to 'selected'" holds only when ρ₁μ endorses *all* relevant
  comparisons (a (ZER)-type world 1). K3.7's ρ₁ = ρ_∞ endorses only D̂-localized comparisons, and in L4's (B1) the
  density ρ₁ is the CA part of ν*₁, which endorses nothing by itself. State the restriction.

### 3.4 M1.6 — CORRECT
- (a): open convex A, B with A ∩ N = B ∩ N a.e. on open N give A ∩ N ⊆ int cl B = B, hence equality and equal
  boundaries in N. At h ∈ α, P_K(h) = 0 with minimiser m. If m ≠ v_m, the open wedge {v_m·g > 0 > m·g} near h, with
  v_l·g > 0 (l ≠ m, h ∈ relint F_m), lies in D_{T1} ∖ D_K. So m = v_m.
  - **Remark.** The proof is local at one point h. "Open cone N ⊇ α" can be replaced by "open set N ∋ h, h ∈ relint F_m
    ∩ U". M1.9′(b) needs this form (§5.2).
- (b): `ref_checks` (C) confirms the arc structure: F₁: (−,−,+)Q₃ | (−,+,+)Q₁ | (−,+,−)Q₂; F₂: (−,−,+)Q₃ | (+,−,+)Q₂ |
  (+,−,−)Q₁; F₃: (+,−,−)Q₁ | (+,+,−)Q₃ | (−,+,−)Q₂. So F₁-middle, F₂-middle and the F₃ r₂₃-corner lie in
  R₁₂ = Q₁ ∪ Q₂, giving v₁, v₂, v₃ ∈ K. Y₃ = P₁ on Q₃ accepts the non-null set (+,+,−) ∩ U ∖ cl D_{T1} outside F₃'s
  middle arc. The permutation symmetry of T1, K′, U is right.

---

## 4. M1.7 and M1.8 — fully verified

### 4.1 M1.7 — CORRECT
Every line was re-derived.
- Y_k = T1 on R_ij and P_i (= P_j) on Q_k. It is regular, and incoherent by M1.6(b).
- M1.3 with I = {i, j} gives C ∈ C_L with C ⪯_i Y_k and C ⪯_j Y_k, C ≠ Y_k. Hence F_i := E_iY_k ∖ E_iC and
  F_j := E_jY_k ∖ E_jC are both non-null.
- E_i(Y_k) = E_i(T1) ∩ R_ij, since Y_k is right at i on Q_k and E_i(T1) ∩ Q_k = J_k. Likewise for j.
- On R_ij exactly one of i, j is right for any model. So on F_j (C right at j) C is wrong at i, while Y_k = T1 (wrong at j)
  is right at i: F_j ⊆ E_iC ∖ E_iY_k. Symmetrically F_i ⊆ E_jC ∖ E_jY_k. F_i ∩ F_j = ∅.
- Relevance: C ∈ C_L and Y_k regular. For a bounded endorser, ν_i(E_iC) ≤ ν_i(E_iY_k). Subtracting the common part
  gives ν_i(F_i) ≥ ν_i(E_iC ∖ E_iY_k) ≥ ν_i(F_j), and likewise at j.
- One witness C serves all endorsers simultaneously, which is what M1.8 needs.
- `ref_checks` (A): the identities, and the inclusion F_j ⊆ E_iC ∖ E_iY_k for random C, hold on every sample.

**Scope (should be stated).** The proof uses only (LA), (S) and strict (G) on M_U. It does not use T1 ∈ C_L, (C) or
(IB). So M1.7 holds in **every** such ranking on M_U, cover or not. It binds a cover only through blindness: T1 ∈ C_L
enters through admissibility (L4.1.3/L4.3), which makes the CA parts vanish on E_i(T1). "Key necessary condition for
covers" should read "a property of all rankings with (LA), (S), strict (G), which is binding where the endorsers are
CA-blind".

### 4.2 M1.8 — CORRECT
- Main statement: 0 = ρ_i(F_i) ≥ ρ_i(F_j) > 0.
- Shadow corollary: K3.1(c) makes every endorser's CA part vanish on Λ_i ⊇ F_i. So π_i(F_i) ≥ ρ_i(F_j) + π_i(F_j),
  and for ν*_i, ρ*_i > 0 on F_j ⊆ E_j(T1) ∩ R_ij ⊆ R⁰_i. Hence π*_i charges E_i(T1) ∩ R_ij for both j ≠ i, no
  maximal endorser is CA, and (ZER_i) fails.

### 4.3 An independent second proof of M1.8's (ZER) case
M1.5(b) applied to a CA endorser with V_i ∩ R_ij = E_j(T1) ∩ R_ij gives a coherent X_ij equal to T1 on R_ij and to P_i
on Q_k. That model is Y_k, which is incoherent. This reaches the same exclusion by a different route, and it also shows
something stronger: **for any world with a CA endorser, the blind set on each R_ij is the world-i error set of a
coherent "between" model** (K3.7(β′) without (γ) or positivity at the other worlds). I recommend recording this.

---

## 5. M1.9 and M1.9′

### 5.1 M1.9 — CORRECT (flagged risky)
- The two inequalities are exactly "T^i_θ = T1 on R_ij" (σ_i ≠ σ_j there, ties go to P_i). On Q_k, T^i_θ = P_i. So
  T^i_θ = Y_k, which M1.5(a) makes coherent, against M1.6(b). The exchanged version (T^j_θ) is the same.
- **Second proof, from M1.7 alone.** With the one witness pair (F_i, F_j):
  θρ_i(F_i) ≥ θρ_i(F_j) ≥ (1−θ)ρ_j(F_j) ≥ (1−θ)ρ_j(F_i) > θρ_i(F_i).
- **Nearby strengthening (PROVED by the same chain).** M1.9 holds for **arbitrary** bounded endorsers ν_i, ν_j
  (purely finitely additive parts allowed) in charge form. Suppose θν_i(A) ≥ (1−θ)ν_j(A) for every A ⊆ E_j(T1) ∩ R_ij,
  and (1−θ)ν_j(A) > θν_i(A) for every non-null A ⊆ E_i(T1) ∩ R_ij (or the exchanged pair). Then (H_U) fails. This
  needs neither CA endorsers nor M1.5. It is the clean statement of "zero/positive exchange rate" for (W2).

### 5.2 M1.9′
- **(a) CORRECT.** Every θ works. As stated, M1.8 at world j already suffices.
- **(c) CORRECT**, with the CA endorsers of M1.9 understood. Note that the ties there are exactly the joint zero set
  {ρ_i = ρ_j = 0}, not a frozen ratio.
- **(b) GAP (fixable; flagged risky).** What is proved:
  - Z^{(i)} and Z^{(j)} are both non-null (correct: each strict inequality would trigger M1.9 with T^i resp. T^j).
  - T^i_{θ*} = T1 △ (J_k ∪ Z^{(i)}) is coherent (M1.5(a)). By the local form of M1.6(a) (§3.4), if some point h on an
    R_ij-arc of F_m (open orthant, relint, off crossings) has a neighbourhood O with μ(Z^{(i)} ∩ O) = 0, then v_m ∈ K.
    If this happened for all three m, then D_K ⊆ D_{T1}, against T^i ⊇ J_k ∖ D_{T1}, which is non-null (it lies just
    outside a middle arc in the two-plus orthant of Q_k). **So there is a facet F_m such that Z^{(i)} has positive
    measure in every neighbourhood of every point of every R_ij-arc of F_m.** This much is CORRECT, and the "every
    neighbourhood of every point" formulation is the right one, *provided M1.6(a) is used in its local form*. The
    cone form, as stated in M1.6(a), does not give it.
  - The same holds for Z^{(j)}, with a facet F_{m′}.

  What is **not** proved:
  - **Two-sidedness on one facet.** m′ may differ from m. Z^{(i)} ⊆ E_i(T1) and Z^{(j)} ⊆ E_j(T1) lie on opposite sides
    of ∂D_{T1} only arc by arc, so "two-sided … along every R_ij-arc of *some* facet" needs m = m′.
  - **"Frozen ratio."** Ties on R_ij are {θ*ρ_i = (1−θ*)ρ_j}, *including* the joint zero set {ρ_i = ρ_j = 0}. The
    note's own bullet lists both, but the summary (and §0 item 4) drops the second.
  - **"Shell."** Positive measure in every neighbourhood is accumulation (possibly a sparse "dust"), not a one-sided
    collar.

  **Fix (and a sharper statement, PROVED here).** Let I_e := {θ : θe_i + (1−θ)e_j ∈ A(c)}, a closed interval.
  - If I_e has interior, then at every interior θ both inequalities are strict except on {ρ_i = ρ_j = 0}. (The defect
    (1−θ)ρ_j − θρ_i is strictly decreasing in θ where ρ_i + ρ_j > 0, and ≥ 0 at the right end.) So the escape from M1.9
    is **joint blindness**: {ρ_i = ρ_j = 0} meets both E_i(T1) ∩ R_ij and E_j(T1) ∩ R_ij non-nully, each accumulating at
    every point of the R_ij-arcs of some facet (F_m for one side, F_{m′} for the other).
  - If I_e = {θ*}, the escape is accumulation of {ρ_i/ρ_j = (1−θ*)/θ*} ∪ {ρ_i = ρ_j = 0} on each side, again along all
    R_ij-arcs of some facet per side.

  Replace "a two-sided tie shell: a frozen density ratio along every R_ij-arc of some facet" by this dichotomy, here and
  in §0 item 4.

---

## 6. §4, §0 and Q_M1

### 6.1 §4.1 (W1)–(W4) — CORRECT
- (W1) is K3.1(c) with K3.1(f) for the trivial localizing family (𝔚_∅ = 𝔚). It needs (NC), which holds since
  endorsers exist.
- (W2): ∫ρ*_iδ_i = −ρ*_i(E_iC ∖ E_iY_k) ≤ −ρ*_i(F_j) < 0. Since δ_i⁺ = F_i, K3.1(b) forces μ(F_i ∩ D_m) > 0 for every
  m. Correct. "Thin pieces" is not proved: F_i is only non-null and meets every D_m.
- (W4) is M1.7.

### 6.2 §4.2 — correct as descriptions; labels
- **4.2.1.** The lexicographic world is (ZER_i), and M1.8 excludes it. The concrete M1.3 argument is right: the primaries
  force C = T1 off J_k, and C fixes no error of Y_k at i, so C = Y_k. In fact **one** such world on the edge suffices:
  C = T1 on R⁰_i ∩ R_ij makes F_j null.
- **4.2.2 L2.** L2.4(b)'s λ|_{d_a} is a CA endorser of maximal support (positive exactly off c_a), so the device is
  (ZER). The orientation reading is right. In L2, C_a ⪯₁ X′ has δ = 1_{Q′} − 1_P, with the negative part P ⊆ c_a
  (blind) and the positive part Q′ ⊆ d_a (visible). (W2)'s comparison C ⪯_i Y_k has its positive part F_i in the blind
  set and its negative part ⊇ F_j visible.
  - Note that the shadow needs **both** orientations: L2-type certificates for (W1), *and* (W2)-type trades.
  - (i) is a proved exclusion only when the blind set is aimed exactly at E_i(T1) ∩ R_ij (so that ρ > 0 on
    E_j(T1) ∩ R_ij). §4.3 shows that M1.5(b) excludes any CA blind set of that shape.
- **4.2.3 K3.3.** The description is correct: positive parts are thin far targets, and every bounded endorser lives at
  the far end (ν(c_b) = 0 for b < 1). Closed sections fail (K3.3(a)). The sentence on L2 "re-creating a CA endorser by
  finitely many levels" is a heuristic. In L2 the CA endorser comes from sources ⊆ c_a, targets ⊆ d_a and tail-dominance
  at a. Label it.
- **§0 item 4** labels these consequences PROVED. Only the M1.8 consequence and the L2 (ZER) observation are proved;
  the orientation and tilt sentences are readings.

### 6.3 §4.3 — CORRECT
With worlds 2, 3 additive (positive densities), J₂ ∪ J₃ = E₁(T1) ∩ R₂₃ (W₁ ⊆ Q₁). The swap Y = T1 △ (A₂ ∪ A₃) is
world-1-better by strict (G), and weakly better at 2 and 3 iff ρ₂(A₂) ≤ ρ₂(A₃) and ρ₃(A₃) ≤ ρ₃(A₂). Non-atomicity
produces such A₂ ⊆ J₂, A₃ ⊆ J₃ unless ess sup_{J₂} ρ₃/ρ₂ ≤ ess inf_{J₃} ρ₃/ρ₂, which is (2,3)-Bayes-ness of T1 on J₂ ∪ J₃.
"Excluded only by this" is informal.

### 6.4 §0 headline — GAP (wording)
"Every remaining degenerate case is settled POSITIVELY" at field level is shown for the following:
- three blind worlds (c^T);
- p* on an open edge or at a vertex (c^T; (0, σ₂, σ₃) under (B1)).

It is not shown for these:
- two blind worlds at an interior p* (M1.11 excludes the exact-shadow version and no example is given);
- pairwise-null blind sets (L1.D, conjectured *impossible*).

Restate it as "settled positively for three blind worlds and for every boundary type".

### 6.5 Q_M1
- **Well posed.** BRIEF13's axioms include T1 ∈ C_L, so "Yes" is a cover ((LF) is automatic on M_U).
- **GAP: "Equivalently, … T1 admissible at all three vertices."** By M1.1(b), admissibility at the vertices gives
  only Λ_k ⊇ E_k(T1) ∩ M. A maximal field equal to c^T needs equality (ρ*_k > 0 a.e. on R⁰_k). The vertex formulation is
  strictly weaker (it allows, e.g., M1.2-type enlargements), and M1.8's shadow corollary needs ρ*_i > 0 on F_j ⊆ R⁰_i.
  Replace "Equivalently" by "a special case of: …", or require Λ_k = E_k(T1) ∩ M.
- **"Necessary: each world is a closed-section tilt …"** The proved content is (W1)–(W4). "Tilt" is a metaphor.
- **GAP: the "No" list is incomplete.** Excluding the shadow does not leave only {(V) under (B1); (E) with tie shells or
  without ZER; L1.D; strongly (M1)}. Also open:
  - interior p* with two or three blind worlds whose pairwise intersections are non-null but not of shadow shape (M1.11
    covers only exact shadow-blindness at one world with the third seeing J_j ∪ J_k);
  - vertex cases with more than one blind world (outside (B1));
  - (E) with joint-blindness escapes (§5.2).

  Either add these or say "among the configurations examined here".
- **Recommended first test (agrees with the note).** Find a two-world full system whose world 1 has no CA endorser of
  maximal support. By §4.3 of this report, such a world cannot have a CA endorser at all with the blind shape needed.

---

## 7. Requested changes
1. M1.1′(c): replace "exactly in Lemma UVN" by the UVN-failure statement (§1.3); say "the CA field alone".
2. M1.11 reading: replace "needs all three worlds blind, as in c^T" by the precise consequence (§2.3).
3. M1.5(c): restrict "upgrades K3.7(β)" to fully endorsing CA ρ₁ (§3.3).
4. M1.6(a): state it locally (open N ∋ h). M1.9′(b) depends on this (§3.4, §5.2).
5. M1.7: state its scope (only (LA), (S), strict (G)), and that it binds covers through blindness (§4.1).
6. Add the charge form of M1.9 and the M1.7-only proof (§5.1); add the M1.5(b) route to M1.8 (§4.3).
7. M1.9′(b), §0 item 4, §4.3, Q_M1: replace "two-sided tie shell / frozen ratio along every R_ij-arc of some facet" by
   the interval dichotomy of §5.2 (one-sided accumulation per side, possibly on different facets; joint blindness when
   the admissible edge interval has interior).
8. §0 headline, §0 item 4 labels, §4.2.2(i), §4.2.3: relabel the readings (§6.2, §6.4).
9. Q_M1: drop "Equivalently"; complete or qualify the "No" list (§6.5).

## 8. Files
- `m1ref_py/shadow_rerun.out`, `m1ref_py/vertex_rerun.out`: reruns of `m1py/`, identical to the stored outputs.
- `m1ref_py/ref_checks.py` (+ `ref_checks.out`): checks (A)–(D) above, three (ε, s).
