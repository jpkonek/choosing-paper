# L4. The universal undefeated shadow: the fixed point exists, it is degenerate exactly on blind sets, and in the one-blind-world case the degeneracy is pinned to one configuration

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up
or refereed notes mark proved, each named), **CHECKED** (a step-by-step reading, not a re-derivation),
**CONJECTURE**, **NUMERICS** (`l4py/`, run with `python3 -I`; no proof rests on it). No assumption is added.
Notation: write-up §§2–3, §7.7 (Prop. M0, Thm. Estructure, Lemmas quasilin/ball, Props. crosspin/chainchords/
carrying, Thm. M0closed), §4 (Lemma UVN, PL2, nopin, Thm. pivot, Prop. boxbridge, Prop. T1); E1 §1; H1 §§1–3
(Φ, d_t, H1.0, H1.1); K3 §1–§2 (𝔚_k, ba, 𝒩_k, Yosida–Hewitt, K3.1, blind set Λ), K3.7 and K3_referee §7
((Q1)–(Q3)). n = 3, U = D_{K′}, K′ = u + s(T1 − u), M = mixed part of U, N₊ = nonnegative part,
σ_k = sign h_k, P_k = U ∩ {h_k > 0}, E_k(X) = X △ P_k, Q_l = sign class with odd world l, R_ij = Q_i ∪ Q_j.
(H_U) = strict (G), (IB), (LA), (S) with closed sections for every model, (C), T1 ∈ C_L, on M_U.

---

## 0. Outcome

**The universal undefeated shadow theorem is not proved, and T1 is not settled. But the fixed point the brief asks
for exists outright, with no iteration; the whole question is whether it is degenerate.**

1. **The fixed point (Theorem L4.1, PROVED).** Take a ranking with (H_U) in which every world satisfies (NC):
   no finite positive combination of relevant comparison vectors is ≤ −1. Then **every** tuple ν = (ν₁, ν₂, ν₃) of
   Hahn–Banach endorsers (bounded, finitely additive, K3.1(a)) is a generalised shadow that is undefeated at every
   test. By the absorption lemma L4.0, its gap is zero at every weight, and this gap dominates the gap of its
   countably additive part. So the countably additive field c^ν = (ρ_kσ_k) has two properties:
   - **(γ₀)** at **every** interior weight, some Bayes model is coherent;
   - T1 is c^ν-Bayes at some p* ∈ Δ (H1.1, with the localization carried by the purely finitely additive parts).

   No patch is needed and no world needs to be integrable. Hence:
   - the contradiction of E1.1/H1.0 is available **iff** c^ν is strictly signed with p* ∈ Δ°, and then
     M0closed(a) applies;
   - the theorem fails exactly when the fixed point is **degenerate**: some density vanishes on a non-null set (a
     blind set), or p* ∈ ∂Δ.
2. **By-product (Corollary L4.2, PROVED).** This gives a short proof of Theorem M0closed(b) for general finitely
   additive weights from M0closed(a). It bypasses N13 Prop. B and N19 Prop. R3(a), the once-read imports that the
   write-up's status line for M0closed(b) names.
3. **Each residual mechanism is a degeneracy of the fixed point (Proposition L4.4, PROVED).**
   - An (M1) certificate that satisfies (NC) makes its negative set blind (CA and f.a. parts both vanish there).
   - A K3 blind set is a blind set (Λ ⊇ Λ_∞).
   - Sheltering is not an obstruction to L4.1, because L4.1 never patches. It survives only as joint blindness of two
     worlds. Boundary admissibility p* ∈ ∂Δ forces exactly such joint blindness on a joint T1-error set (L4.3).
   - Only **strongly (M1)** worlds, those failing (NC), lie outside the theorem.
4. **One blind world (Theorem L4.9, PROVED, with one CHECKED step).** This is the K3.7 case, with worlds 2, 3 having
   strictly positive endorsing densities, generalised from Λ_∞ to the plain blind set Λ₁. There a cover forces one
   of two configurations:
   - **(I) the single obstruction.** The line L* through e₁ and p* is an exceptional vertex chord. The blind set
     carries tie atoms at p*, with c ∝ ±(0, 1−θ*, −θ*), and these accumulate on the middle arc of F₂ at its
     coordinate-1 crossing w₂ = (0, −1, κ) (or on the middle arc of F₃ at w₃ = (0, κ, −1)), where they carry T1's
     boundary.
   - **(V) the vertex case.** p* = e₁ and Λ₁ ⊋ E₁(T1) ∩ M. The equality case Λ₁ = E₁(T1) ∩ M is excluded
     (Example L4.7).

   Everything else is excluded:
   - every frozen arc with null ties (Lemma L4.8);
   - the "separated" blind sets, which are moreover shown to be non-generic (Lemma L4.6(c): P_{K₁}(w₂) ≤ 0 always,
     and the blind set **must** reach w₂ unless P_{K₁}(w₂) = 0, which forces K₁ ∩ [e₁, e₂] = {e₁});
   - the case P_{K₁}(w₂) = 0 = P_{K₀}(w₃) (CHECKED audit, §5.4).
5. **The configuration handed over (§6).** (I) is the precise template for a positive answer through a blind world:
   - chart lines of the blind gambles pass through e₁;
   - the crossing row c₂(h)₁ = λ₁₂h₁ of the corner system (Prop. boxbridge(a)) is not derivable at w₂;
   - so the holonomy x + 1/x = κ + 1 loses one of its pinned rows there.

   It is also the precise target for a proof: excluding (I) and (V) closes the K3.7 class (one non-adding-up
   world next to two adding-up worlds) entirely, M1 worlds with (NC) included.

| | Statement | Label |
|---|---|---|
| L4.0 | absorption: Gap_t(ν) ≥ d_t(c^ν) for every bounded ν ≥ 0 | PROVED |
| L4.1 | endorser tuples are undefeated; c^ν has (γ₀) at every interior weight and T1 Bayes at some p* ∈ Δ | PROVED |
| L4.2 | M0closed(b) for general f.a. weights, from M0closed(a), without N13 Prop. B | PROVED |
| L4.3 | p* ∈ ∂Δ forces joint blindness on a joint T1-error set | PROVED; NUMERICS (non-null) |
| L4.4 | M1 with (NC), K3 blind sets, sheltering, all are degeneracies of the fixed point | PROVED |
| L4.5 | the gap alone cannot decide: degenerate fixed points with zero gap and admissibility exist abstractly | PROVED |
| L4.6 | one blind world: all B_q coherent; vertex fan; (+,−,−)-contact lemma; forced reach to w₂, w₃ | PROVED; NUMERICS (margins) |
| L4.7 | Λ₁ = E₁(T1) ∩ M (the K3.7(γ) boundary case) is impossible | PROVED; NUMERICS |
| L4.8 | frozen-arc lemma: no two-sided blind collar of a facet arc with null ties | PROVED |
| L4.9 | one blind world: a cover forces (I) or (V) | PROVED, except case (II) of §5.4: CHECKED |
| Q_L4 | can configuration (I) or (V) occur? | open |

---

## 1. Definitions

- **Generalised shadow.** ν = (ν₁, ν₂, ν₃) with each ν_k ∈ ba₊(M): bounded, nonnegative, finitely additive,
  vanishing on μ-null sets. Yosida–Hewitt: ν_k = ρ_kμ + π_k, with 0 ≤ ρ_k ∈ L¹(M) and π_k purely finitely
  additive. On N₊ every regular model is correct at every world, so N₊ carries no cost. Put ρ_k := 1 on N₊ when a
  field on all of U is needed (as K3 §5 does).
- **Costs.** For t ∈ Δ and a model X, t·ν(X) := Σ_k t_kν_k(E_kX ∩ M). With ν^t_− := Σ_k t_kν_k(· ∩ {σ_k < 0}) and
  ν^t_+ := Σ_k t_kν_k(· ∩ {σ_k > 0}) (charges on M), t·ν(X) = ν^t_−(X ∩ M) + ν^t_+(M ∖ X).
- **Gap.** Gap_t(ν) := inf{t·ν(C) : C ∈ M_U coherent} − inf{t·ν(X) : X ∈ M_U regular} ≥ 0.
  - The inequality holds because coherent models are regular.
  - For the countably additive field c^ν := (ρ_kσ_k)_k, put ψ^t(X) := Σ_k t_k∫_{E_kX∩M} ρ_k dμ and
    d_t(c^ν) := inf_coh ψ^t − min ψ^t. The minimum is attained by any c^ν-t-Bayes model.
  - If the tie set Z_t := {t·c^ν = 0} ∩ M is null, then d_t(c^ν) = 0 iff B_t := {t·c^ν > 0} is coherent (H1.0(a):
    the infimum over the compact set of coherent models is attained, and Φ_t vanishes only on B_t).
- **Undefeated at a test X.** For a regular X, some C ∈ C_L with C ⪯_k X at every k satisfies
  ν_k(E_kC) ≤ ν_k(E_kX) at every k.
  - E1's "defeated at t" is the failure of this at X = B^ν_t.
  - H1/K3's near-Bayes tests are the X with t·ν(X) close to the infimum.
- **(NC) at world k** (K3.1(a)). No finite combination Σλ_jδ_j with λ_j ≥ 0 and δ_j ∈ 𝔚_k is ≤ −1 a.e. on M.
  It holds at every world that is not (M1). It can hold at (M1) worlds: a certificate that is ≤ 0 and ≠ 0 need not
  be ≤ −1. A world failing (NC) is **strongly (M1)**.
- **Endorser tuple.** ν with ν_k ∈ 𝒩_k for each k: ν_k(M) = 1, and ν_k(δ) ≥ 0 for every δ ∈ 𝔚_k. By K3.1(a),
  𝒩_k ≠ ∅ iff (NC) at world k. By K3.1(c) there is ν*_k ∈ 𝒩_k whose density ρ*_k is positive exactly off the
  blind set Λ_k (mod null). Λ_k is null iff world k adds up.
- **(γ₀)** for a field c: d_t(c) = 0 for every t ∈ Δ°.

---

## 2. Absorption and the fixed point

**Lemma L4.0 (absorption; PROVED).** For every ν ∈ ba₊(M)³ and every t ∈ Δ, Gap_t(ν) ≥ d_t(c^ν).

*Proof.*
1. **Localizing the purely finitely additive parts.** π := Σ_k π_k is purely finitely additive (K3.1(c), fact
   (F2), proof). By K3.1(b) Steps 1–2 there is a decreasing family D_m ⊆ M with μ(D_m) → 0 and π(M ∖ D_m) ≤ 2^{−m}.
2. **An upper bound for the regular infimum.**
   - Write π^t_± for the parts of ν^t_± coming from the π_k. By the lattice formula (K3.1(b) Step 1),
     OPT := inf_{A⊆M}(π^t_−(A) + π^t_+(M ∖ A)) = (π^t_− ∧ π^t_+)(M).
   - Pick A_m ⊆ D_m with π^t_−(A_m) + π^t_+(D_m ∖ A_m) ≤ (π^t_− ∧ π^t_+)(D_m) + 2^{−m} ≤ OPT + 2^{−m}.
   - Let B be a ψ^t-minimiser (pointwise). Put X_m := (B ∖ D_m) ∪ A_m ∪ N₊. It is regular.
   - Its countably additive cost is ψ^t(X_m) ≤ min ψ^t + ∫_{D_m} Σ_k t_kρ_k dμ → min ψ^t (absolute continuity).
   - Its purely finitely additive cost is at most OPT + 2^{−m} + π(M ∖ D_m) ≤ OPT + 2^{1−m}.
   - So inf_X t·ν(X) ≤ min ψ^t + OPT.
3. **A lower bound for the coherent infimum.** For every coherent C, the CA cost is ψ^t(C) ≥ min ψ^t + d_t(c^ν),
   and the purely finitely additive cost is π^t_−(C ∩ M) + π^t_+(M ∖ C) ≥ OPT. So
   inf_coh t·ν ≥ min ψ^t + d_t(c^ν) + OPT.
4. Subtracting 2 from 3 gives the claim. ∎

**Theorem L4.1 (the fixed point; PROVED).** Assume (H_U), and (NC) at every world. Let ν be an endorser tuple.
1. ν is undefeated at every regular test X, and Gap_t(ν) = 0 for every t ∈ Δ.
2. c^ν has (γ₀). In particular B_t is coherent at every t ∈ Δ° with Z_t null. Moreover the strict Bayes set B_q is
   coherent for **every** q ∈ Δ°.
3. T1 = B_{p*} ∪ S with S ⊆ Z_{p*}, for some p* ∈ Δ.
4. p* ∈ Δ° whenever c^ν is strictly signed on M. In that case (H_U) is contradictory, by M0closed(a).

*Proof.*
1. **Undefeated.** Theorem kkm gives C ∈ C_L with C ⪯_k X at every k. Each comparison is relevant (C ∈ C_L, X
   regular), so ν_k(1_{E_kX} − 1_{E_kC}) ≥ 0. (The vectors live on M: both models are correct on N₊.) Hence
   t·ν(C) ≤ t·ν(X) for every X, so inf_coh ≤ inf_reg and Gap_t(ν) ≤ 0. Gap_t ≥ 0 always.
2. **(γ₀).**
   - Lemma L4.0 gives d_t(c^ν) ≤ 0, hence = 0, at every t.
   - For null Z_t, use §1.
   - *Every* B_q, when c ≠ 0 a.e. on M (true in §§4–5, since ρ₂ > 0). Fix q ∈ Δ°. By Tonelli, Z_t is null for
     a.e. t, so B_t is coherent for a.e. t. For every direction δ ∈ 𝟏^⊥ outside a null set:
     - Z_q ∩ {δ·c = 0} is null. Fubini: c(g) is never a nonzero multiple of 𝟏 on M, since on M either c(g) has a
       zero coordinate or two coordinates of opposite sign; and {δ : δ·c(g) = 0} is a line for every other g.
     - B_{q+sδ} is coherent for a.e. small s > 0 (polar coordinates around q).
     - As s ↓ 0 these converge in measure to B_q ∪ (Z_q ∩ {δ·c > 0}).
     - Limits in measure of coherent models of M_U are coherent (H12_referee §1.1).
     - The intersection of the limits for δ and −δ is B_q (mod null), and D_K ∩ D_{K′} = D_{co(K∪K′)}.

     This is Thm. Estructure(d)'s argument. It uses no sign condition on c.
3. **Admissibility.** Let D^k be the K3.1(b) family of π_k, and D_m := ⋃_k D^k_m. Let T1 ⪯_k Y be relevant with
   Y = T1 on D_m, and put δ := 1_{E_kY} − 1_{E_kT1}. Then δ = 0 on D_{m′} for all m′ ≥ m, so
   |π_k(δ)| ≤ π_k(M ∖ D_{m′}) ≤ 2^{−m′}. Endorsement gives ∫ρ_kδ dμ = ν_k(δ) − π_k(δ) ≥ −2^{−m′} for all m′, so
   ∫ρ_kδ ≥ 0. This is the hypothesis of Lemma H1.1, with ρ_k ≥ 0 integrable. Its steps 1–3 and 5 use no positivity
   (K3.7(γ) proof), and give p* ∈ Δ with p*·c ≥ 0 a.e. on D_{T1} ∩ M and ≤ 0 a.e. on M ∖ D_{T1}.
4. **Interior.** This is H1.1 step 4, which uses ρ_k > 0 on the three sets (−,−,+) ∩ D_{T1}, (−,+,−) ∩ D_{T1},
   (+,−,−) ∩ D_{T1}. With 2 and 3, M0closed(a) (which uses no integrability) applies to c^ν. ∎

*How this answers the brief's route.*
- **The "adaptive reweighting toward the world-k orders' own endorsers" has its fixed point at the start.** Reweight
  every ν_k all the way into 𝒩_k. Hahn–Banach supplies the endorsers, and weak-* compactness of 𝒩_k is all that is
  needed. Kakutani or Ky Fan is unnecessary, and the closed-graph problem (K1 §6.2–6.3: (S) gives closedness in the
  index, never continuity in the tested model) never arises.
- **What the route cannot do is produce a positive gap.** For an endorser tuple the gap is identically zero (L4.1.1).
  A contradiction comes only from M0closed(a)-type rigidity of the countably additive part, and that needs
  positivity.
- Conversely, an undefeated generalised shadow with Gap_t > 0 at some t contradicts (H_U) outright (L4.1.1 read
  backwards). So "undefeated and gap-positive" shadows exist iff (H_U) fails. The universal theorem is therefore
  exactly a gap theorem for the degenerate fixed points.

**Corollary L4.2 (M0closed(b) without N13 Prop. B; PROVED).** On M_U no ranking with (H_U) in which every world
adds up (Def. addup, finitely additive weights allowed) has T1 ∈ C_L.

*Proof.*
- A world that adds up has a weight that is positive on non-null sets and endorses its relevant comparisons. After
  normalisation on M, this is an element of 𝒩_k whose density is > 0 a.e. on M (K3.1(c), last bullet, which is N19
  Lemma R1 re-derived).
- So (NC) holds, and the tuple of these weights has a strictly signed c^ν. Apply L4.1.4. ∎

*Dependencies:* Yosida–Hewitt; K3.1(b) Step 1 (π ∧ μ = 0); N19 Lemma R1 / K3.1(c); Theorem kkm; H1.0(a); H1.1;
M0closed(a).

*Not used:* N13 Prop. B, N19 Prop. R3(a), N17 Prop. 2.1, (E_ψ), Prop. M0 (α)–(δ). The write-up's status line for
M0closed(b) says "a second reading of [the imports] would put (b) at the standard of (a)". L4.2 removes that
dependence instead. It also supplies Corollary CPaU(b) through the same route, since CPaU(b) places
(CP-a) worlds inside (M0).

---

## 3. Degeneracies, and what each residual mechanism must be

**Proposition L4.3 (boundary admissibility forces joint blindness; PROVED).** In L4.1, let l be the third world.
- If p* lies in the open edge (e_i, e_j), then ρ_i = ρ_j = 0 a.e. on the joint T1-error set
  J_l := Q_l ∩ E_i(T1) = Q_l ∩ E_j(T1). On Q_l, worlds i and j agree, and T1 errs at both.
- If p* = e_i, then ρ_i = 0 a.e. on E_i(T1) ∩ M.

*Proof.* Step 3 of L4.1 gives p*·v ≥ 0 a.e. on M, where v_k = ρ_k if T1 is correct at k and −ρ_k if not.
- On J_l, v_i = −ρ_i and v_j = −ρ_j, so −p*_iρ_i − p*_jρ_j ≥ 0.
- At p* = e_i, the condition reads v_i ≥ 0. ∎

The sets J_l are non-null. For example J₃ ⊇ D_{T1} ∩ (−,−,+) near r₁₂. (NUMERICS `l4py/l4_checks.py` (2): about
2–6% of U for three (ε, s).)

**Proposition L4.4 (the residual mechanisms as degeneracies; PROVED).**
- **(a) (M1) with (NC).** Let Σλ_jδ_j ≤ 0 be a certificate at world k, and W := {Σλ_jδ_j < 0} (non-null). Every
  ν_k ∈ 𝒩_k has ν_k(W) = 0. So W ⊆ Λ_k, and π_k(W) = 0 as well.
  - *Proof.* f := Σλ_jδ_j is a simple function (finitely many values), so f ≤ −η on W with η > 0 its least
    negative value in absolute size. Then 0 ≤ Σλ_jν_k(δ_j) = ν_k(f) ≤ −η ν_k(W). ∎
- **(b) K3 blind sets.** Λ_k ⊇ Λ_∞ at world k (K3.1(d): Λ_∞ ⊆ Λ_D ⊆ Λ).
- **(c) Sheltering.** L4.1 uses no patch model and no localized endorsers. Every comparison is endorsed by a full
  endorser, and the localization is carried by the purely finitely additive parts inside Lemma L4.0. So the K3.5′
  residual (R-i) and H1's case (B) are not obstructions to L4.1.
  - Two worlds sheltering one another reappear only as two blind sets that meet on a common region.
  - Joint blindness on a joint T1-error set is exactly what boundary admissibility requires (L4.3).
- **(d) Strongly (M1) worlds** (failing (NC)) have 𝒩_k = ∅ and are the only worlds outside L4.1.

So, for systems with (NC), the property every residual mechanism must have is this: it must make **every**
endorser tuple degenerate in a way that survives (γ₀) and admissibility. The maximal-support tuple ν* has the
smallest blind sets Λ_k. A cover therefore needs the field c* := c^{ν*}, with blind sets exactly Λ_k, to satisfy
(γ₀) and admissibility while either some Λ_k is non-null with p* ∈ Δ°, or p* ∈ ∂Δ.

**Proposition L4.5 (the gap alone cannot decide; PROVED).** There are ν ∈ ba₊(M)³ with every ν_k(M) = 1,
Gap_t(ν) = 0 for every t, and T1 t·ν-optimal at an interior weight.

*Proof.* Let r ∈ D_{T1} ∩ (+,−,−) be a ray, and let π be a {0,1}-valued charge vanishing on null sets that lives on
every open cone around r. (Take an ultrafilter containing the cones around r and all co-null sets.) Put
ν₁ = ν₂ = ν₃ := π.
- A model's cost is t₂ + t₃ if it accepts near r (in the π-sense), and t₁ if it rejects.
- T1 (which accepts near r) and P₂ (which rejects all of (+,−,−)) are coherent and realise both values, so
  Gap ≡ 0.
- T1 is optimal whenever t₁ ≥ t₂ + t₃, for instance at t = (3/4, 1/8, 1/8). ∎

So no argument that uses only the zero gap of the fixed point can reach a contradiction. Positivity of the
countably additive part, at least on the regions where M0closed(a)'s chain runs, is the entire content. Whether
such a purely finitely additive ν can be the endorser tuple of a ranking with (H_U) is not decided here.

---

## 4. One blind world: structure

**Standing hypotheses (B1) for §§4–5.**
- c = (ρ₁σ₁, ρ₂σ₂, ρ₃σ₃), measurable, with ρ₂, ρ₃ > 0 a.e. on M and ρ₁ ≥ 0. Put Λ₁ := {ρ₁ = 0} ∩ M.
- (γ₀) holds, or merely (γ) for a.e. t.
- T1 = B_{p*} ∪ S with S ⊆ Z_{p*}.

By L4.1 this is the situation of every cover in which worlds 2 and 3 add up and world 1 satisfies (NC): take
ν = (ν*₁, weight₂, weight₃). Then p* ∈ Δ° unless p* = e₁ and Λ₁ ⊇ E₁(T1) ∩ M (L4.3, plus H1.1 step 4 with
ρ₂, ρ₃ > 0). This is K3.7's setting with Λ₁ in place of Λ_∞, and with M1 worlds that satisfy (NC) allowed.

Write L* for the line through e₁ and p*, θ* := p*₂/(p*₂ + p*₃), and m(g) := θ*ρ₂σ₂ + (1−θ*)ρ₃σ₃. From K3.7 and
K3_referee §7, whose proofs use only (γ) and ρ₂, ρ₃ > 0:
- **(β)** S_θ := P₁ on M ∖ Λ₁, G_θ := {θρ₂σ₂ + (1−θ)ρ₃σ₃ > 0} on Λ₁ is coherent for a.e. θ, and S₁, S₀ are
  coherent.
- **(β′)** S₁ = D_{K₁} and S₀ = D_{K₀}, with:
  - K₁ ∩ [e₁, e₂] ≠ ∅ and K₁ ⊆ conv(K′ ∪ [e₁, e₂]);
  - K₀ ∩ [e₁, e₃] ≠ ∅ and K₀ ⊆ conv(K′ ∪ [e₁, e₃]);
  - Λ₁ ∩ R₁₂ = E₁(D_{K₁}) ∩ R₁₂ and Λ₁ ∩ R₁₃ = E₁(D_{K₀}) ∩ R₁₃.
- **(Q1)** If p* ∈ Δ°, then Λ₁ ∩ (+,−,−) ⊆ (+,−,−) ∖ D_{T1}, and Λ₁ ∩ (−,+,+) ⊆ D_{T1}.

Orthant by orthant, (β′) reads:

| orthant | Λ₁ there | S_θ there |
|---|---|---|
| (+,−,−) | (+,−,−) ∖ D_{K₁} = (+,−,−) ∖ D_{K₀} | D_{K₁} ∩ (+,−,−), for every θ |
| (−,+,+) | D_{K₁} ∩ (−,+,+) | D_{K₁} ∩ (−,+,+), for every θ |
| (+,−,+) | (+,−,+) ∖ D_{K₁} | D_{K₁} ∪ (G_θ ∩ Λ₁) |
| (−,+,−) | D_{K₁} ∩ (−,+,−) | G_θ ∩ D_{K₁} |
| (+,+,−) | (+,+,−) ∖ D_{K₀} | D_{K₀} ∪ (G_θ ∩ Λ₁) |
| (−,−,+) | D_{K₀} ∩ (−,−,+) | G_θ ∩ D_{K₀} |

On the first two orthants G_θ is constant (c = (0,−,−) or (0,+,+) on Λ₁).

**Lemma L4.6 (PROVED).** Assume (B1) with p* ∈ Δ°.
- **(a) Vertex fan.**
  - As q → e₁ in Δ°, every Hausdorff cluster value K̂ of K^♭_q gives D_{K̂} equal a.e. to P₁ on M ∖ Λ₁.
  - On (+,−,−) and (−,+,+), D_{K̂} equals D_{K₁} (the first two rows of the table).
  - Off Λ₁, the sign of q·c tends to σ₁ pointwise as q → e₁, because ρ₁ > 0 there and |q·c − q₁ρ₁σ₁| ≤ ρ₂ + ρ₃.
  - On Λ₁ ∩ ((+,−,−) ∪ (−,+,+)), the sign of q·c is constant.
  - Then use dominated convergence and R1 Prop. 3.1.
- **(b) Contact lemma.** On the open (+,−,−)-portions of F₂ and of F₃ (corner ray r₂₃ excluded, crossing excluded),
  P_{K₁} > 0. Equivalently P_{K₀} > 0, since D_{K₁} and D_{K₀} agree on (+,−,−). Consequently Lemma UVN at e₁ holds
  at every point of these portions.
- **(c) Forced reach.**
  - P_{K₁}(w₂) ≤ 0 at w₂ = (0, −1, κ) ∈ F₂, with equality only if K₁ ∩ [e₁, e₂] = {e₁}.
  - If P_{K₁}(w₂) < 0, then Λ₁ contains (+,−,+) ∩ O for a neighbourhood O of w₂. In particular Λ₁ contains a
    two-sided conic neighbourhood of every sufficiently short arc of the middle arc of F₂ near w₂.
  - Likewise P_{K₀}(w₃) ≤ 0 at w₃ = (0, κ, −1) ∈ F₃ (equality only if K₀ ∩ [e₁, e₃] = {e₁}), and if
    P_{K₀}(w₃) < 0 then Λ₁ ⊇ (+,+,−) ∩ O′ near w₃.

*Proof.*
- **(b).**
  - By (Q1) and (β′), D_{T1} ∩ (+,−,−) ⊆ D_{K₁}. So P_{K₁} ≥ 0 on the closed portions, by closure.
  - τ ↦ P_{K₁}(h(τ)) is concave. If it vanished at an interior point of a portion, it would vanish on the whole
    portion (a concave function ≥ 0 on an interval that is zero inside it is zero on the interval).
  - Then ∂D_{K₁} would contain an open piece of the facet plane, with D_{K₁} on the D_{T1} side.
    - Take h in that piece and m ∈ K₁ with m·h = 0.
    - If m ≠ v_k, the planes m^⊥ and v_k^⊥ through h differ. So near h there is g with v_k·g > 0 > m·g, i.e. a point
      of D_{T1} ∩ (+,−,−) ⊆ D_{K₁} with P_{K₁}(g) < 0, which is absurd.
    - So v_k ∈ K₁. Since D_{K₀} ∩ (+,−,−) = D_{K₁} ∩ (+,−,−), the same argument gives v_k ∈ K₀.
  - For F₃ (k = 3): v₃ ∈ K₁ ⊆ conv(K′ ∪ [e₁, e₂]) is impossible, because max_{conv(K′∪[e₁,e₂])} m₃ = max_{K′} m₃
    and (v₃)₃ − max_{K′} m₃ = (1 − s)·2ε/3 > 0.
  - For F₂: v₂ ∈ K₀ ⊆ conv(K′ ∪ [e₁, e₃]) is impossible, by the same margin in coordinate 2.
  - **UVN.** By (a), every cluster model at e₁ contains a ball around h inside (+,−,−) ∩ D_{K₁}. Hausdorff
    compactness and joint continuity of (K, g) ↦ P_K(g) give P(q, h′) > 0 uniformly for q near e₁ and h′ near h.
    The half-plane statement for a.e. h′ follows from the charts (Lemma quasilin(c)).
- **(c).**
  - K₁ meets [e₁, e₂] (β′). For m = (a, 1−a, 0) ∈ K₁, m·w₂ = −(1 − a) ≤ 0, and < 0 unless m = e₁. So
    P_{K₁}(w₂) ≤ 0, with equality only if K₁ ∩ [e₁, e₂] = {e₁}. If P_{K₁}(w₂) < 0, continuity gives
    P_{K₁} < 0 on a neighbourhood O of w₂.
  - Then (+,−,+) ∩ O ⊆ (+,−,+) ∖ D_{K₁} = Λ₁ ∩ (+,−,+).
  - Points of the middle arc of F₂ near w₂ lie in the open orthant (+,−,+), on both sides of the facet.
  - For w₃ use m = (a, 0, 1−a) ∈ K₀: m·w₃ = −(1 − a). ∎

NUMERICS (`l4py/l4_checks.py` (1)): on a 25 × 25 grid of (ε, s), both margins equal (1 − s)2ε/3 exactly.

So the "separated" configuration (Λ₁ at positive angular distance from ∂D_{T1}) is non-generic. Unless
P_{K₁}(w₂) = 0 = P_{K₀}(w₃) (which forces K₁ ∩ [e₁, e₂] = {e₁} = K₀ ∩ [e₁, e₃]), the blind set reaches the
coordinate-1 crossing of F₂ or of F₃. The gambles
there have c₁ = 0, so their chart lines pass through e₁. This is the K3_referee's (Q3), now shown to be forced.

**Example L4.7 (the K3.7(γ) boundary case; PROVED).** Under (B1) without the assumption p* ∈ Δ°,
Λ₁ = E₁(T1) ∩ M (mod null) is impossible.

*Proof.*
- **S₁ copies T1 on R₁₂.**
  - Off Λ₁, T1 is world-1-correct, so S₁ = P₁ = T1 there.
  - On Λ₁ ∩ R₁₂, T1 errs at world 1, hence is correct at world 2, so S₁ = P₂ = T1 there.
- **So v₃ ∈ K₁.** The corner portion of F₃ at r₂₃ lies in the open class Q₁ ⊆ R₁₂, with both sides in Q₁. On a cone
  around an arc of it, S₁ = D_{K₁} agrees with D_{T1}. The argument of L4.6(b) gives v₃ ∈ K₁.
- **Contradiction.** This contradicts K₁ ⊆ conv(K′ ∪ [e₁, e₂]) (the margin above). ∎

NUMERICS (`l4py/l4_checks.py` (3)): the splice "T1 on Q₁ ∪ Q₂, P₁ on Q₃" fails midpoint convexity on 281, 1139 and
16 of 200 000 sampled accepted pairs, for three (ε, s).

Hence the vertex case (V) of §0 needs Λ₁ ⊋ E₁(T1) ∩ M.

---

## 5. One blind world: the exclusions

### 5.1 The frozen-arc lemma

**Lemma L4.8 (PROVED).** Assume (B1) with p* ∈ Δ°. Then there is no open arc Γ in the relative interior of a facet
F_k, off the crossings, together with an open cone N ⊇ Γ inside one open orthant and meeting no other facet, such
that N ∖ Λ₁ is null (a two-sided blind collar) and Z_{p*} ∩ N is null.

*Proof.*
- **Step 0 (orthants (+,−,−), (−,+,+)).** There c = (0,−,−) or (0,+,+) on Λ₁, so B_{p*} is constant on N. But T1
  accepts on one side of Γ and rejects on the other, while S ∩ N is null. Contradiction.
  - So N lies in Q₂ ∪ Q₃, where σ₂ ≠ σ₃.
- **Step 1 (frozen along L*).** For q ∈ L* ∩ Δ°, q·c = (q₂ + q₃)m on Λ₁. So B_q ∩ N = B_{p*} ∩ N = D_{T1} ∩ N
  (mod null).
- **Step 2.**
  - By L4.1.2 (or Thm. Estructure(d)'s argument under (γ)), B_q = D_{K^♭_q}.
  - Two open sets that agree a.e. on N have the same closure there. So P^♭(q, ·) = 0 on Γ: positivity at h ∈ Γ would
    put a ball around h into D_{K^♭_q} ⊆ cl D_{T1} on N, and every such ball leaves cl D_{T1}.
- **Step 3.** τ ↦ P^♭(q, h(τ)) is concave and vanishes on the parameter interval of Γ. So it is ≤ 0 on R
  (Lemma caps(a)). Thus P^♭(q, ·) ≤ 0 on all of F_k, for every q ∈ L* ∩ Δ°.
- **Step 4 (the two ends of L*).**
  - As q → e₁ along L*, B_q → C₀ := (P₁ on M ∖ Λ₁) ∪ (B_{p*} ∩ Λ₁) ∪ N₊ in measure. The pointwise argument is
    L4.6(a), and on Λ₁ the sign is constant along L*.
  - As q → ē := L* ∩ (e₂, e₃), B_q → C₁ := {m > 0} ∪ (Z(m) ∩ P₁ ∖ Λ₁) ∪ N₊ in measure.
  - Both are coherent, being limits in measure of coherent models (H12_referee §1.1). Their credal sets are Hausdorff
    limits of K^♭_q (R1 Prop. 3.1). So P_{C₀} ≤ 0 and P_{C₁} ≤ 0 on F_k.
- **Step 5 (contradiction).**
  - *k = 2 or 3.* F_k has an open (+,−,−)-portion. There C₀ ∩ (+,−,−) = (+,−,−) ∖ Λ₁ = D_{K₁} ∩ (+,−,−), which
    contains a ball around each point of the portion (L4.6(b)). So P_{C₀} > 0 there.
  - *k = 1.* F₁'s middle arc lies in (−,+,+), where m = θ*ρ₂ + (1−θ*)ρ₃ > 0. So C₁ ⊇ (−,+,+) ∩ U, and P_{C₁} > 0 on
    the middle arc. ∎

### 5.2 The theorem

**Theorem L4.9 (PROVED, except case (II), which is CHECKED in §5.4).** Assume (B1) with p* ∈ Δ°. Then at least one
of the following holds:
- **(I₂)** P_{K₁}(w₂) < 0, and for every short arc Γ of the middle arc of F₂ near w₂ (inside {P_{K₁} < 0}),
  every cone N around Γ meets Z_{p*} ∩ Λ₁ non-nully.
- **(I₃)** The same at w₃ ∈ F₃ with K₀.

In both cases Z_{p*} ∩ Λ₁ is non-null. By the ball lemma (whose steps 1–4 are sign-free) it is a union of the two
oriented atoms on which c ∝ ±b*, with b* := (0, 1−θ*, −θ*). Its chord {q : q·b* = 0} = L* passes through e₁. Every
q ∈ L* is exceptional, and S charges these atoms along F₂ (resp. F₃) near w₂ (resp. w₃).

If neither (I₂) nor (I₃) holds, there is a contradiction.

*Proof.*
- **Case (α): P_{K₁}(w₂) < 0, and some such arc has a cone N with null ties.** By L4.6(c), N can be chosen
  inside Λ₁ ∩ (+,−,+). Lemma L4.8 gives a contradiction. Likewise at w₃.
- So if (I₂) and (I₃) both fail, then for each of w₂, w₃ either the corresponding value P_{K₁}(w₂), P_{K₀}(w₃) is
  0 (L4.6(c)), or case (α) applies. Only the following remains.
- **Case (II): P_{K₁}(w₂) = 0 = P_{K₀}(w₃).** See §§5.3–5.4. ∎

### 5.3 What case (II) looks like (PROVED)

- By L4.6(c), K₁ ∩ [e₁, e₂] = {e₁} and K₀ ∩ [e₁, e₃] = {e₁}. So e₁ ∈ K₁ ∩ K₀, and D_{K₁}, D_{K₀} ⊆ P₁. By (β′),
  Λ₁ ⊆ M ∩ {g₁ > 0}: world 1 is blind only to errors of rejection.
- Λ₁ avoids a neighbourhood of every point of:
  - the open (+,−,−)-portions of F₂ and F₃ (L4.6(b));
  - the open middle arcs of F₂ and F₃.

  For the middle arc of F₂: τ ↦ P_{K₁}(h(τ)) is concave, is > 0 on the open (+,−,−)-portion (L4.6(b)), and is 0
  at w₂ (case (II)). A concave function that is positive at some a and zero at a later point b is positive on [a, b):
  P(λa + (1−λ)b) ≥ λP(a) > 0. So it is > 0 at the crossing (κ, −1, 0) and on the open middle arc. Since
  Λ₁ ∩ (+,−,+) = (+,−,+) ∖ D_{K₁}, Λ₁ misses a neighbourhood of each such point. F₃ is the same with K₀.
- Λ₁ misses F₁ entirely (F₁ ⊆ {h₁ < 0}), and every neighbourhood of a point of F₂, F₃ with h₁ < 0.
- So Λ₁ can touch ∂D_{T1} ∖ 0 only at the three rays w₂, w₃, r₂₃.
- UVN at e₁ holds at every boundary gamble x with x₁ ≠ 0 other than r₂₃:
  - on h₁ > 0 portions, by the ball in D_{K₁} or D_{K₀} ⊆ every cluster model (table, L4.6(a));
  - on h₁ < 0 portions, because every cluster model misses the open orthants (−,·,·) on R₁₂ and on R₁₃ (S_θ ⊆ D_{K₀}
    or D_{K₁}, both ⊆ P₁), and an open convex cone that misses a ball around x has P(x) < 0.
- No ball centred on {g₁ = 0} lies in Λ₁ (Λ₁ ⊆ {g₁ > 0}).

### 5.4 Case (II): the audit (CHECKED)

The proof of M0closed(a) (Props. chainchords, carrying, crosspin and the §4 chain they audit) uses strict signs of c
at world 1 in exactly four kinds of place. This is from a reading of the printed proofs, not a re-derivation:
- **(i)** Lemma UVN at e₁. It is used:
  - in Thm. pivot Steps 0, 1, 2, 4 at gambles h(τ), τ ∈ (0,1), with h₁ ≠ 0;
  - in Lemma nopin at crossings w with w₁ > 0 (on F₂: (κ, −1, 0); on F₃: (κ, 0, −1));
  - in Lemma PL2 at points w₊ near a crossing of coordinate 1;
  - in Prop. carrying(d) at middle-arc points.

  It is never used at r₂₃, w₂ or w₃ themselves. Those are endpoints, or have x₁ = 0.
- **(ii)** The last line of the ball lemma ("strict signs give the orthant"), used in crosspin, chainchords (PL2
  across chords) and carrying(b), for balls centred on {g₁ = 0}.
- **(iii)** Lemma edgebox's "negative on the whole closed edge". With one blind world, c(A + λB)·q₀ ≤ q₀,b c_b < 0 at
  every q₀ in the open edge [e_a, e_b] minus its vertices. Prop. T1 applies the box only at q₀ = (s, 1−s, 0) with
  s ∈ (0,1), and the transposed field c^σ is again a one-blind field (blind at world 2), for which the same bound
  holds. So (iii) never fails with one blind world.
- **(iv)** Thm. Estructure(b)'s "chords miss the vertices", in Prop. carrying(d). An atom inside Λ₁ has b₁ = 0.
  - Inside (+,−,−) or (−,+,+), Λ₁ carries no ties at an interior p*.
  - At r₁₂ ((−,−,+), odd world 3), carrying(d) can be run on F₁ (j = 2, b₃ > 0 > b₂).
  - At r₃₁ ((−,+,−)), it can be run on F₁ (j = 3, b₂ > 0 > b₃).
  - Theorem M0closed(a)'s last step needs π⁺ > 0 at one point of α_G on one facet. So (iv) never fails with one
    blind world.

In case (II), §5.3 restores (i) at every point where it is used, and (ii) everywhere. So the chain, chainchords and
carrying all run, and give a contradiction exactly as for strictly signed fields. Two labels apply:
- The restoration statements are PROVED (§5.3).
- That the list (i)–(iv) is exhaustive is CHECKED (one reading of the write-up's printed proofs).

---

## 6. The single obstruction, and the configuration handed over

**What is settled.**
- In any ranking with (H_U) and (NC) at every world, the undefeated generalised shadow exists (L4.1), and its
  countably additive field is a "weak realisation": (γ₀) at every interior weight, and T1 Bayes at some p* ∈ Δ.
- The universal theorem holds iff no such weak realisation can be degenerate.
- With one blind world, degeneracy is pinned to (I₂)/(I₃) or (V).

**The single precise obstruction (configuration (I₂); (I₃) is its mirror under the transposition of worlds 2 and 3,
which preserves T1, U and u).** All of the following must hold:
1. Worlds 2 and 3 have strictly positive endorsing densities ρ₂, ρ₃. World 1 satisfies (NC) and has full endorsers
   whose densities vanish on a rigid blind set Λ₁ (β′), with P_{K₁}(w₂) < 0 (this holds whenever K₁ meets [e₁, e₂] at a
   point other than e₁, L4.6(c)). Hence Λ₁ ⊇ (+,−,+) near
   w₂ = (0, −1, κ) (L4.6(c)).
2. On a non-null cone of Λ₁ accumulating along the middle arc of F₂ at w₂, the density ratio is frozen at the target
   weight: ρ₃/ρ₂ = θ*/(1 − θ*). So c ∝ ±(0, 1−θ*, −θ*) there (two tie atoms).
3. T1 = B_{p*} ∪ S, with S charging those atoms. T1's facet F₂ near w₂ is carried by a tie shell, not by a strict
   chart.
4. The chord L* through e₁ and p* is exceptional (all its points are tie weights). The chart lines of the blind
   gambles near w₂ pass through e₁.
5. Every B_q is coherent, the vertex fan S_θ at e₁ is coherent, and the frozen-arc obstruction of L4.8 is evaded only
   because of the ties in item 2.

**Why this is the place a positive answer would live.**
- In Prop. boxbridge(a) the crossing row of coordinate 1 on F₂ (λ₁₂, normalised to 1 in Prop. T1) is derived from
  "the cluster line at w₂ is lin(p*, e₁)" together with the strict sign of n_τ·(e₁ − p*) on both sides of w₂
  (Lemma UVN at e₁).
- In (I₂), the gambles on the (+,−,+) side of w₂ are blind at world 1. Their charts contain e₁ on their boundary, and
  the vertex limit at e₁ is the fan S_θ. So the sign is lost on that side, and the row c₂(h)₁ = λ₁₂h₁ is not
  available.
- The corner equations x₁ + 1/x₂ = x₂ + 1/x₃ = x₃ + 1/x₁ = κ + 1, which together with the box contradict each other,
  then lose one pinned row on F₂. This is one degree of freedom in the holonomy, exactly where the tie shell sits.
- **CONJECTURE: none.** I did not compute whether the freed parameter absorbs the box contradiction. That is the first
  computation for anyone attempting a construction: redo Prop. T1 with c₂(h)₁ replaced by an affine function of h
  that vanishes on the chord through e₁ at the shell, and test the box.

**The vertex case (V)** (p* = e₁, Λ₁ ⊋ E₁(T1) ∩ M) is the other unexcluded one-blind configuration. It is degenerate
in the opposite way: T1 is "Bayes" only because world 1 is blind wherever T1 errs at world 1. Example L4.7 excludes
its minimal instance.

**Outside the one-blind analysis.** These remain open:
- patterns with two or three blind worlds, including the joint blindness forced by p* in an open edge (L4.3);
- strongly (M1) worlds.

L4.5 shows that none of them can be closed by the gap argument alone. Each needs M0closed(a)-type rigidity of the
countably additive part on the regions where the chain runs.

**Question Q_L4 (open).** Can configuration (I₂) (equivalently (I₃)) or (V) occur for a field satisfying (B1)?
- "No" closes, for T1 on M_U, every cover in which two worlds add up and the third satisfies (NC). That includes the
  whole of K3.7's class and every (M1) world whose certificates are not uniformly negative.
- "Yes" gives the weak field that a positive construction would then have to realise by a ranking. Step 3 of K3 §7
  ("build world 1 so that its full endorsers are exactly the multiples of ρ₁ off Λ₁") is still required.

---

## 7. Dependencies and files

**Used.**
- Yosida–Hewitt; K3.1(a)–(c) (refereed CORRECT, K3_referee §1); K3.7(β), (β′), K3.7′ (refereed CORRECT);
  K3_referee §7 (Q1).
- Theorem kkm; H1.0(a), H1.1 (refereed in H12); H12_referee §1.1 (limits in measure of coherent models are
  coherent); R1 Prop. 3.1.
- Theorem M0closed(a) (proved, two readers); Thm. Estructure(d)'s directional-limit argument; Lemma caps(a);
  steps 1–4 of Prop. F (sign-free).
- §4 of the write-up and Props. chainchords, carrying, crosspin, read for the §5.4 audit.

**Not used.** N13 Prop. B, N19 Prop. R3(a), N17 Prop. 2.1, (E_ψ), K3.5's patch, any localized endorser, J1, K1, K2
(cited only), D2, edge results.

**Not yet refereed.** A referee should check, in order of risk:
- the exhaustiveness of the §5.4 list (CHECKED only);
- L4.6(b)'s "planes differ" step;
- Step 4 of L4.8 at the ē end;
- the claim in L4.1.2 that every B_q is coherent when c has a zero on a non-null set (there the coherent Bayes models
  given by (γ₀) at nearby weights are used in place of B_{q+sδ}).

`l4py/` (run with `python3 -I` from inside it):
- `l4_checks.py` (+ `l4_checks.out`), three checks:
  - (1) the two margins (1 − s)2ε/3 on a grid;
  - (2) non-nullity of the joint T1-error sets J_l;
  - (3) midpoint-convexity failures of the splice of Example L4.7.
