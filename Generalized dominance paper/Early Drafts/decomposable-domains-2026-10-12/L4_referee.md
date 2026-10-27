# Referee report on L4_notes.md (round 20)

16 Oct 2026. Read against BRIEF17, K3_notes + K3_referee, H1_notes + H12_referee, E1_notes, and the write-up
§§2–3, §4 (for the audit) and §7 (Prop. M0, Thm. Estructure, Lemmas quasilin/ball, Props. crosspin/chainchords/
carrying, Thm. M0closed, Thm. kkm). I assumed every claim was wrong until I had re-derived it.

Numerics:
- `l4py/l4_checks.py` was rerun with `python3 -I`. Its output is byte-identical to `l4_checks.out`.
- My own scratch checks are in `l4ref_py/ref_checks.py` (+ `.out`). They are NUMERICS only, and no verdict rests on
  them.

---

## 0. Verdicts

| Item | Verdict |
|---|---|
| Definitions: (NC), endorser tuple, generalised shadow, Gap, "undefeated" | CORRECT |
| L4.0 (absorption) | CORRECT |
| L4.1.1 (undefeated, Gap ≡ 0), L4.1.3 (admissibility), L4.1.4 (interior ⇒ contradiction) | CORRECT |
| L4.1.2, (γ₀) | CORRECT |
| L4.1.2, "B_q is coherent for **every** q" | **GAP**. Stated unconditionally but proved only when c ≠ 0 a.e. on M; false without that (§1.3). Fix: add the hypothesis, which holds in §§4–5. |
| Degeneracy dichotomy | CORRECT in the proved direction. "p* ∈ ∂Δ" is a sub-case of "blind set" (L4.3). GAP (wording): "the theorem fails exactly when…" and "holds iff…" overclaim (§1.4). |
| L4.2 (M0closed(b) from M0closed(a), general f.a. weights) | CORRECT. M0closed(a) does apply to c^ν (§2). |
| L4.3 | CORRECT |
| L4.4 (a), (b), (d) | CORRECT |
| L4.4 (c) | GAP (wording). Two interpretive sentences sit inside a PROVED item. |
| L4.5 | CORRECT |
| L4.6 (a)–(c) | CORRECT. The "planes differ" step was re-derived. |
| L4.7 | CORRECT. It does not even need p*. |
| L4.8 | CORRECT, and it can be strengthened: "Z_{p*} ∩ N null" can be weakened to "S ∩ N null" (§4.1). |
| L4.9 as stated | CORRECT modulo case (II). "S charges these atoms" is a GAP, fixed by the strengthened L4.8. |
| **L4.9's conclusion (I₂)/(I₃)** | **Not sharp: configuration (I) is impossible** (Proposition R, §4.2). |
| §5.3 | CORRECT |
| §5.4, "four places" (CHECKED) | CONFIRMED at the level of the printed proofs, by my own re-derivation, with four additions (§5). |
| §6, "the single obstruction (I)" and the proposed "first computation" | **WRONG.** (I) is excluded. Also, in (I) one has p* ∈ E, so the corner/box branch the computation targets is the wrong branch (§6). |
| Q_L4 | Answered for (I): **No.** (V) remains open. |

**Net effect.** The paper-level gain is larger than L4 claims.

> Under (H_U) on M_U, suppose worlds 2 and 3 add up and world 1 satisfies (NC). Then for the maximal-support
> endorser tuple, T1 can be c*-Bayes **only at p* = e₁**, with Λ₁ ⊋ E₁(T1) ∩ M.

Status of this statement:
- It is PROVED except for case (II) of L4 §5.4, which is CHECKED.
- It rests on L4.1, L4.6–L4.9 and Proposition R below.
- So configuration (V) is the only remaining one-blind-world configuration, and it is the right next target. This is
  the nearby reachable result; I recommend that the note state it as its main theorem.

---

## 1. Definitions and Theorem L4.1

### 1.1 Definitions
- **(NC) at world k.** "No finite nonnegative combination of members of 𝔚_k is ≤ −1 a.e. on M." This is K3's
  (NC_𝔚). By K3.1(a), 𝒩_k ≠ ∅ iff (NC) holds, in both directions (refereed CORRECT, K3_referee §1.1).
  - (NC) can hold at (M1) worlds: a certificate that is ≤ 0 and ≠ 0 need not be ≤ −1 uniformly. "Strongly (M1)" is
    well defined.
- **Undefeated.** L4 defines this as "some C ∈ C_L with C ⪯_k X at every k and ν_k(E_kC) ≤ ν_k(E_kX) at every k".
  - This generalises E1.1's "defeated at t". E1.1 fails this at X = B^ν_t for every kkm dominator, and L4's negation
    is exactly "every such C fails at some world".
  - For an endorser tuple, "undefeated at every regular X" is immediate from the definition: kkm dominators give
    relevant comparisons. The content of L4.1 is therefore L4.0, not the undefeatedness.
- **Gap.**
  - Coherent models are regular, so Gap_t ≥ 0.
  - d_t(c^ν) agrees with H1.0's inf Φ, since ψ^t(Y) − min ψ^t = ∫_{Y△B_t}|t·c| for regular Y (H1.0(b) identity).

### 1.2 L4.0 — CORRECT
I re-derived each step.
- π := Σ_kπ_k is purely finitely additive, by K3.1(c)(F1)/(F2).
- K3.1(b) Steps 1–2 give D_m with μ(D_m) → 0 and π(M ∖ D_m) ≤ 2^{−m}.
- **Upper bound for the regular infimum.** The π-cost of X is π^t_−(X ∩ M) + π^t_+(M ∖ X). For
  X_m = (B ∖ D_m) ∪ A_m ∪ N₊:
  - the π-cost is at most π^t_−(A_m) + π^t_+(D_m ∖ A_m) + π(M ∖ D_m), using t_k ≤ 1;
  - the CA cost is at most min ψ^t + Σt_k∫_{D_m}ρ_k.
  - Hence inf_reg ≤ min ψ^t + (π^t_− ∧ π^t_+)(M). The lattice formula inf_A{α(A) + β(M∖A)} = (α∧β)(M) is standard.
- **Lower bound for the coherent infimum.** Every coherent C has π-cost ≥ OPT and CA cost ≥ inf_coh ψ^t. All
  quantities are finite (bounded charges, ρ_k ∈ L¹).

### 1.3 L4.1
- **Item 1.** CORRECT. Selected models lie in C_L by (S), and kkm gives weak domination.
- **Item 2, (γ₀).** CORRECT.
  - d_t(c^ν) ≤ Gap_t(ν) = 0 at every t ∈ Δ.
  - The coherent infimum of ψ^t is attained: coherent models are compact in measure (H1.0(a)), and ψ^t is continuous
    in measure (ρ ∈ L¹). So a coherent ψ^t-Bayes model exists at every t.
- **Item 2, "every B_q is coherent".** GAP.
  - The directional-limit proof is correct when c ≠ 0 a.e. on M. On M, c(g) is never a nonzero multiple of 𝟏, so for
    a.e. δ the set Z_q ∩ {δ·c = 0} is null. The limits are coherent (H12_referee §1.1), and the intersection of the
    two limits is B_q.
  - The theorem *statement*, however, makes the claim with no hypothesis. The note's own list of risks (item 4) shows
    that the author was unsure.
  - **The claim is false for fields with (γ₀) and a non-null zero set.** Take the realising field c(g) = g. Every
    B_t = U ∩ {t·g > 0} is coherent. Now put c := 0 on a thin open cone W around a ray inside (+,−,−) ∩ {u·g > 0} ∩ U.
    - (γ₀) still holds: at each t, B_t^{new} ∪ (W ∩ {t·g > 0}) is a Bayes model of the new field, since W ⊆ Z_t, and
      it is the old coherent B_t.
    - But B_u^{new} = (U ∩ {u·g > 0}) ∖ W is not convex. `ref_checks.py` (C) finds midpoint violations.
  - Whether c^ν coming from an actual ranking can behave like this is not decided.
  - **Fix.** State "Moreover, if c ≠ 0 a.e. on M, then…". This is all that §§4–5 use, since ρ₂ > 0.
- **Item 3.** CORRECT.
  - Y = T1 on D_m ⊇ D_{m′} gives |π_k(δ)| ≤ π_k(M ∖ D^k_{m′}) ≤ 2^{−m′}, so ∫ρ_kδ ≥ 0.
  - H1.1 steps 1–3 and 5 use neither positivity nor more than integrability (H12_referee §1.3; K3.7(γ)).
- **Item 4.** CORRECT. With c^ν strictly signed, H1.1 step 4 gives an interior p*. M0closed(a) applies by §2.

### 1.4 The degeneracy dichotomy
- **The proved content.** If the CA field of an endorser tuple is strictly signed, (H_U) is contradictory.
- **"or p* ∈ ∂Δ" is redundant.** A strictly signed field forces p* ∈ Δ° (L4.1.4), and p* ∈ ∂Δ forces blindness on a
  non-null set (L4.3). So the dichotomy is simply "some ρ_k vanishes on a non-null set".
- **GAP (wording).** Two phrasings assert an equivalence that is not proved:
  - §0.1: "the theorem fails exactly when the fixed point is degenerate";
  - §6: "the universal theorem holds iff no such weak realisation can be degenerate".

  A degenerate weak realisation does not yield a cover, and L4.5 shows that degenerate fixed points exist abstractly.
  Moreover, an admissible shadow that is not an endorser tuple might still be undefeated at the Bayes tests that E1
  uses. Only the "if" direction is proved. Replace "iff" with "if".
- **Cosmetic.** In §2, "'undefeated and gap-positive' shadows exist iff (H_U) fails" is wrong as written. Under (H_U),
  undefeated at every test forces Gap ≡ 0 by L4.1.1's argument, so such shadows never exist. Without (H_U) the notion
  is vacuous.

---

## 2. Corollary L4.2 — CORRECT; M0closed(a) really extends

**A world that adds up gives an element of 𝒩_k with positive density.**
- Take the Def. addup weight ν_k. Restrict it to M and normalise; ν_k(M) > 0 because M is non-null.
- The relevant comparisons have vectors vanishing on N₊, because coherent and regular models accept N₊ a.e. So the
  normalised restriction is an element of 𝒩_k.
- Its density is > 0 a.e. on M. I re-read K3.1(c)'s last bullet (N19 Lemma R1): Y′ = Y ∖ ⋃E_k has ν(Y′) < 1/k for
  every k.
- So (NC) holds at every world, and c^ν is strictly signed on M. Put ρ := 1 on N₊ and the field is strictly signed on
  U.

**M0closed(a)'s hypotheses hold for c^ν.**
- *(γ):* (γ₀) together with Tonelli (Z_t is null for a.e. t, since c(g) ∦ 𝟏 on M and c ≡ (1,1,1) on N₊ has no
  ties).
- *Admissibility at an interior p*:* L4.1.3–4.
- *Integrability:* c^ν is integrable anyway, and M0closed(a) does not use integrability.

**Hence (H_U) is contradictory.**

**What is bypassed.** The proof bypasses N13 Prop. B, N19 Prop. R3(a), N17 Prop. 2.1 and (E_ψ). Relevance enters only
through kkm dominators and T1's out-comparisons, both of which are relevant. Its remaining inputs are:
- K3.1(a)–(c), refereed once;
- H1.0(a) and H1.1, refereed in H12;
- H12_referee §1.1;
- Thm. kkm;
- M0closed(a).

**One correction.** "It also supplies Corollary CPaU(b) through the same route" is true, but CPaU(b)'s weight
ν_i(A) = P_i(w_i1_A) needs P_i ∈ 𝒫⁺_i, i.e. Theorem fullsupport (refereed once). That dependency remains and should be
named.

**Recommendation.** Record L4.2 in the write-up as an alternative proof of M0closed(b) that removes the "second
reading of the imports" caveat. Its status is that of K3.1 and H1.1, each read once by a referee.

---

## 3. L4.3–L4.5

- **L4.3: CORRECT.**
  - On Q_l, worlds i and j agree, so v_i = −ρ_i and v_j = −ρ_j on J_l, and p*_l = 0.
  - J₃ ⊇ D_{T1} ∩ (−,−,+) near r₁₂ is a non-empty open set. This is a proof; the numerics are superfluous.
- **L4.4(a): CORRECT.** f is simple, f ≤ −η on W, and 0 ≤ ν_k(f) ≤ −ην_k(W).
- **L4.4(b): CORRECT.** Λ_∞ ⊆ Λ_D ⊆ Λ.
- **L4.4(d): CORRECT.**
- **L4.4(c): GAP (wording).** These two statements are interpretations, not proved results:
  - "Two worlds sheltering one another reappear only as two blind sets that meet on a common region";
  - "Joint blindness … is exactly what boundary admissibility requires" (L4.3 gives a necessary condition only).

  Move them out of the PROVED item, or label them.
- **L4.5: CORRECT.**
  - The ultrafilter generated by the cones around r and the co-null sets gives a {0,1}-charge vanishing on null sets.
  - Every model's cost is t₂ + t₃ or t₁, and both values are realised by coherent models (T1 and P₂).

---

## 4. One blind world: §§4–5

### 4.1 L4.6, L4.7, L4.8

Setting checks:
- (B1) is correctly derived from L4.1. Take the tuple (ν*₁, weight₂, weight₃).
- p* ∈ Δ° unless p* = e₁ and Λ₁ ⊇ E₁(T1) ∩ M, by H1.1 step 4 with ρ₂, ρ₃ > 0. I checked the three edges.
- K3.7(β), (β′) use only (γ), ρ₂, ρ₃ > 0 and ρ₁ > 0 off Λ₁. I re-read both proofs, so they hold with the plain blind
  set Λ₁.
- (Q1) follows from c = (0,−,−) and c = (0,+,+) on Λ₁ ∩ Q₁, with no ties at an interior p*.
- The orthant table of §4 is correct; I checked all six rows.
- The facet geometry was checked: F₂ runs (−,−,+) | w₂ | (+,−,+) | (κ,−1,0) | (+,−,−), and F₃ runs
  (+,−,−) | (κ,0,−1) | (+,+,−) | w₃ | (−,+,−). See `ref_checks.py` (A).

**L4.6(a): CORRECT.** Off Λ₁, |q·c − q₁ρ₁σ₁| ≤ ρ₂ + ρ₃ and ρ₁ > 0 give sign → σ₁. Hausdorff cluster values pass to
convergence in measure.

**L4.6(b): CORRECT.** I re-derived it.
- D_{T1} ∩ (+,−,−) ⊆ D_{K₁} holds a.e. Since both are open and D_{K₁} is convex, it gives D_{T1} ∩ (+,−,−) ⊆ cl D_{K₁},
  hence P_{K₁} ≥ 0 on the closed portions.
- **The "planes differ" step.** If P_{K₁} vanished at an interior point of a portion, it would vanish on the whole
  portion (concavity, ≥ 0). Take h there and a minimiser m ∈ K₁ with m·h = 0.
  - If m ≠ v_k, then m and v_k are independent. So some direction a has v_k·a > 0 > m·a.
  - g = h + ηa then lies in the open orthant, has v_j·g > 0 for j ≠ k (h ∈ relint F_k), and is in D_{T1} with
    P_{K₁}(g) < 0. This is absurd.
- P_{K₀} vanishes on the same piece, because D_{K₀} and D_{K₁} agree on the open orthant.
- The margins (1 − s)2ε/3 are correct, as the rerun of l4py (1) confirms.

**L4.6(c): CORRECT.** m·w₂ = −(1 − a) for m = (a, 1 − a, 0), and Λ₁ ∩ (+,−,+) = (+,−,+) ∖ D_{K₁} (`ref_checks.py`
(B)). "Equality only if" is a necessary condition, correctly stated.

**L4.7: CORRECT.**
- S₁ = T1 on R₁₂ ∪ (M ∖ Λ₁), and the r₂₃-portion of F₃ is two-sidedly in Q₁ ⊆ R₁₂. So v₃ ∈ K₁, against the margin.
- p* is not used. The statement holds under (B1) alone.

**L4.8: CORRECT.**
- Step 2 argues only the case P^♭ > 0 on Γ. P^♭ < 0 is symmetric: a ball would miss cl D_{K^♭} but meet D_{T1} ∩ N.
- Step 4 at the ē end: along L* ∩ Δ°, q·c → m on M, and the residual q₁ρ₁σ₁ decides Z(m) off Λ₁. The limit C₁ is
  as stated and coherent. It is needed **only for k = 1**. For k = 2, 3, Step 5 uses only C₀ and L4.6(b).
- **Strengthening (used below).** Steps 0–1 need only B_{p*} ∩ N = D_{T1} ∩ N, i.e. **S ∩ N null**, where
  S = D_{T1} ∖ B_{p*}. Ties outside D_{T1} are rejected by both. So L4.8 holds with "S ∩ N null" in place of
  "Z_{p*} ∩ N null".

### 4.2 L4.9, and Proposition R: configuration (I) is impossible

**L4.9 as stated.** The case analysis is correct.
- If (I₂) fails, then either P_{K₁}(w₂) = 0, or some arc Γ and cone N ⊆ Λ₁ ∩ (+,−,+) have null ties, which L4.8
  excludes. Likewise at w₃.
- "Z_{p*} ∩ Λ₁ is a union of the two oriented atoms c ∝ ±b*" needs no ball lemma. On Λ₁, p*·c = 0 iff
  ρ₃/ρ₂ = θ*/(1 − θ*) with σ₂ ≠ σ₃.
- **GAP.** "S charges these atoms along F₂ near w₂" does not follow from (I₂) as stated: the ties might all lie
  outside D_{T1}. With the strengthened L4.8 it does follow. Under (I₂), for every short arc Γ ⊆ middle arc ∩
  {P_{K₁} < 0} near w₂ and every cone N ⊇ Γ, the set S ∩ N is non-null.

**Proposition R (PROVED here, one reading).** Under (B1) with p* ∈ Δ°, (I₂) is impossible. By the transposition of
worlds 2 and 3, (I₃) is impossible too. Hence P_{K₁}(w₂) = 0 = P_{K₀}(w₃): only case (II) can occur, and L4 §5.4
(CHECKED) excludes it.

*Proof.*

1. **Set-up on F₂.**
   - B_{p*} = D_{K^♭} is coherent (L4.1.2, since c ≠ 0 a.e.), and T1 = B_{p*} ∪ S. So K^♭ := K^♭_{p*} ⊇ T1, and
     S = D_{T1} ∖ D_{K^♭} mod null.
   - γ(τ) := P^♭(p*, h(τ)) on F₂ is concave and ≤ 0. Its zero set is a closed interval. Its negative set is
     I₁₂ ∪ I₂₃, where each piece is an interval containing the endpoint r₁₂ resp. r₂₃, possibly empty. (Each
     m ∈ K^♭ is linear along F₂.)
   - `ref_checks.py` (D)(i): 0 violations in 400 random K ⊇ T1.
2. **γ < 0 on an open sub-arc near w₂.**
   - Suppose γ ≡ 0 on an open sub-arc Γ′ of the middle arc. Then ∂D_{K^♭} contains the flat piece R₊Γ′ ⊆ v₂^⊥. A convex
     cone is, near a relative-interior point of a flat 2-dimensional piece of its boundary, the open half-space: take
     the open hull of a small disc of the piece and an interior point.
   - So D_{K^♭} ⊇ D_{T1} near Γ′, and S ∩ N is null for a small cone N around a compact sub-arc of Γ′. This
     contradicts (I₂) as strengthened.
   - So the zero interval meets (τ₁, τ₁ + η) in at most one point. Hence γ < 0 on an open sub-arc Γ⁰ ⊆ middle arc ∩
     {P_{K₁} < 0} near w₂, and Γ⁰ lies in I₁₂ or in I₂₃.
3. **The shell.**
   - For an arc α on which γ < 0, put Sh(α) := {λh + s𝟏 : λ > 0, h ∈ α, 0 < s < λ|γ|}. It is open and connected, and
     lies in D_{T1} ∖ cl D_{K^♭} ⊆ S ⊆ Z_{p*}.
   - By the sign-free part of Lemma ball (Prop. F steps 1–4) and connectedness, c ∝ b a.e. on Sh(α) for one vector b.
     This is exactly carrying(b)'s step.
   - **Sign bound.** P^♭ ≥ min_i h_i, so 0 < s < |γ| ≤ −min_i h_i. Over points near r₂₃ the shell with small s lies in
     (+,−,−). Over Γ⁰ the shell with small s lies in (+,−,+) ∩ {P_{K₁} < 0} ⊆ Λ₁. `ref_checks.py` (D)(ii): 0
     violations of the bound.
   - So whenever α ⊇ Γ⁰, the shell has a non-null part in Λ₁. There c₁ = 0, so **b₁ = 0**, and then c₁ = 0 a.e. on
     the whole shell, i.e. Sh(α) ⊆ Λ₁.
4. **Case Γ⁰ ⊆ I₂₃.** The shell over I₂₃ contains a non-null open set in (+,−,−) near r₂₃, and it lies in Λ₁. But
   Λ₁ ∩ (+,−,−) carries no ties at an interior p*, since c = (0,−,−) there. Contradiction.
5. **Case Γ⁰ ⊆ I₁₂.**
   - Some m ∈ K^♭ has m·r₁₂ < 0. So the negative arc α_G around r₁₂ extends into F₁. On F₁ it stays inside the
     (−,−,+) corner portion, because crosspin applied to K^♭ at F₁'s crossings uses only worlds 2 and 3.
   - The shell over α_G is one atom G with b = (0, b₂, b₃), b₂ < 0 < b₃, and chord ℓ = L* ∋ p*.
   - Run carrying(c), carrying(d) and M0closed(a)'s last step **on F₁**, with r = r₁₂, j = 2 and odd world o = 3:
     - carrying(c) uses N25 Thm. 4.1(c), (e) and Lemma 3.1, which are sign-free;
     - carrying(d) uses UVN for P^{A_δ} at e₂ and e₃ (strict signs at worlds 2, 3) and ℓ separating e₃ from e₂
       (b₃ > 0 > b₂);
     - the last step uses N25 4.1(d) and crosspin for K_δ on F₁ (balls centred on {g₂ = 0} and {g₃ = 0}, strict
       signs).
   - Together they give h ∈ α_G ∩ relint F₁ with P_{K_δ}(h) > 0 ≥ P_{K_δ}(h). Contradiction.
   - This is precisely the route L4 §5.4(iv) describes for blind carrying atoms at r₁₂. ∎

*Reading.*
- L4 treated (I) as escaping because crosspin and carrying(b)'s "no crossing in the negative set" can fail at w₂.
  Both can fail, but the negative set of P^♭ on a facet still consists of corner intervals (a sign-free fact). So the
  tie shell near w₂ is connected to r₁₂ or to r₂₃.
  - Through r₂₃ it would have to be blind inside (+,−,−), which is impossible.
  - Through r₁₂ it is a carrying atom whose finale runs on F₁, where world 1 never enters.
- **Inputs beyond L4's own lemmas:** exactly those L4 §5.4(iv) already relies on. This proposition therefore stands
  at the standard of L4.9.
- **Label.** PROVED (one reading).

### 4.3 §5.3 — CORRECT
- Case (II) gives e₁ ∈ K₁ ∩ K₀. So D_{K₁}, D_{K₀} ⊆ P₁ and Λ₁ ⊆ {g₁ > 0}.
- The concavity step works: γ(a) > 0 and γ(b) = 0 give γ > 0 on the segment toward a. It gives P_{K₁} > 0 on F₂'s
  open middle arc and at (κ,−1,0), and P_{K₀} > 0 on F₃'s.
- UVN at e₁ holds at every facet point with x₁ ≠ 0 except r₂₃:
  - on h₁ < 0, cluster models equal P₁ there, because Λ₁ ⊆ {g₁ > 0};
  - on h₁ > 0, Λ₁ is missed, and compactness gives uniformity.

---

## 5. The CHECKED "four places" claim (§5.4) — CONFIRMED, by my own re-derivation

I listed every step of M0closed(a)'s printed proof chain (§7: quasilin, ball, crosspin, chainchords' audit of §4,
carrying, the final step; §4: signs, chords, levels, sandwich, caps, UVN, PL2, nopin, pivot, nosliding, rotation,
regularity, blowup, twoslope, PCNS, edgebox, boxbridge, Prop. T1). For each step I asked where c₁ ≠ 0 with sign σ₁
is used. The strict-sign uses at world 1 are exactly these:

1. **UVN at e₁** (quasilin(b): "q·c(g) → c_l(g) ≠ 0"). It enters through:
   - pivot Steps 0, 1, 2, 4;
   - the λ₁ₖ > 0 crossing rows of boxbridge(a), i.e. x₃ = λ₁₃ in Prop. T1's box (the F₃ row at w₃);
   - nopin at (κ,−1,0) and (κ,0,−1) with j = 1;
   - PL2's "(a₊)_c > 0" for c = 1;
   - carrying(d) for atoms with o = 1 or j = 1.
2. **Ball lemma, last line**, for balls centred on {g₁ = 0}: crosspin at w₂ and w₃, chainchords' PL2 for K^♭, and
   carrying(b)'s "no crossing in the negative set". **Add:** N25 Thm. 4.1(a) ("G ⊆ O_σ"), the source of carrying(b)'s
   "sign pattern of the corner ray".
3. **Edgebox.** L4's bound holds, with "minus e_a" in place of "minus its vertices". It holds for c and for c^σ at
   q₀ = (s, 1−s, 0), s ∈ (0,1).
4. **Estructure(b)/N25 4.1(a), "chords miss the vertices"**, in carrying(d). For blind atoms at r₁₂ and r₃₁, F₁ is
   available. Atoms at r₂₃ are never blind at an interior p*.

**Additions** (none changes the conclusion):
- **(a) Weak-sign uses.** Two steps use signs only weakly, and these survive c₁ = 0:
  - Lemma chords(b)'s vertex statements;
  - PL2's "(a₋)_c ≤ 0 because c_c(h⁻) < 0" (≤ 0 suffices).
- **(b) Symmetry steps.** Prop. T1 applies the whole chain to c^σ (σ = (1 2)), which is blind at world 2, and to
  p*⊙c.
  - The restoration needed for c^σ is the σ-image of §5.3: UVN at e₂ off σ(r₂₃) = r₃₁.
  - It holds by equivariance, B^σ_q = σB_{σq}. This should be stated.
- **(c) Sign-free inputs.** Estructure(d) (directional limits; usc of K^♭), the "countable meets" of Estructure(c),
  Lemma quasilin(a), (c), and N25 4.1(c)–(e) and Lemma 3.1 are sign-free.
  - One new feature: the great circle e₁^⊥ may carry non-atomic mass of γ_*μ. It corresponds to q = e₁ ∉ Δ°, so it
    is harmless.
- **(d) Scope of the reading.** This is a reading of the write-up's printed sketches. The source proofs behind them
  were not re-read for sign use: R10b Lemma UVN/D/M, N15, N12, P4 Lemmas 2.4–2.5, N25 Lemma 3.1 and Thm. 3.3.
- **Label.** CHECKED is the right label. With the case-(II) restoration of §5.3, case (II) is excluded at that
  standard.

---

## 6. §6 and Q_L4

- **"The single precise obstruction (I₂)" is WRONG.** Proposition R excludes it.
- **The proposed "first computation" is aimed at the wrong branch.** It proposes redoing Prop. T1 with a modified row
  c₂(h)₁.
  - In (I), Z_{p*} ∩ Λ₁ is non-null, so p* ∈ E and L* is an exceptional chord.
  - The corner/box chain at p* (chainchords) then does not start, by Thm. pstarE's mechanism. The relevant branch is
    crosspin/carrying, and that is where Proposition R closes it.
- **What remains in the one-blind-world class (K3.7's class, including (M1) worlds with (NC)):**
  - (V): p* = e₁ and Λ₁ ⊋ E₁(T1) ∩ M (L4.7 excludes equality);
  - the CHECKED status of case (II).
- **Suggested aim for the next round.** Exclude (V).
  - There T1 = P₁ off Λ₁, and (β′) forces D_{K₁} ⊆ D_{T1} on (+,−,−) and (+,−,+), D_{K₁} ⊇ D_{T1} on (−,+,+) and
    (−,+,−), and the K₀ analogues.
  - Alternatively, upgrade §5.4 by reading the sources listed in §5(d).

---

## 7. Requested changes

1. L4.1.2: add "if c ≠ 0 a.e. on M" to the every-B_q clause (§1.3; counterexample in `ref_checks.py` (C)).
2. §0.1, §2, §6: replace the "iff"/"exactly when" claims by the proved one-way statements. Note that p* ∈ ∂Δ is a
   sub-case of blindness.
3. L4.4(c): move the interpretive sentences out of the PROVED item.
4. L4.2: name Theorem fullsupport as an input for the CPaU(b) remark. Recommend the write-up adopt L4.2.
5. L4.8: state the stronger hypothesis "S ∩ N null". Add the P^♭ < 0 half of Step 2. Note that the ē end is used only
   for k = 1.
6. L4.9: replace "S charges these atoms" with the strengthened-L4.8 derivation. Add Proposition R. Restate the theorem
   as "(B1) with p* ∈ Δ° is contradictory (PROVED except case (II), CHECKED)".
7. §5.4: add items (a)–(d) of §5. Name N25 Thm. 4.1(a) under (ii) and (iv). State the σ-equivariance.
8. §6: withdraw (I) as the handed-over configuration. Hand over (V), and say that (I) lies in the p* ∈ E branch.

## 8. Files
- `l4py/l4_checks.py`: rerun with `python3 -I`; output identical to `l4_checks.out`.
- `l4ref_py/ref_checks.py` (+ `ref_checks.out`):
  - (A) facet sign patterns;
  - (B) L4.6(c) values and the blind (+,−,+) region near w₂;
  - (C) the counterexample to the unconditional every-B_q clause (25 midpoint violations in 3·10⁵);
  - (D) the interval structure of the negative set of P_K on F₂ for K ⊇ T1, and the shell sign bound (0 violations
    in 400 trials).
