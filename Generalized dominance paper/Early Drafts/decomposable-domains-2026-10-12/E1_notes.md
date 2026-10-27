# E1. Installing the D2 mechanism at T1: what M0closed needs, where protection can live, and why it is invisible

15 Oct 2026, BRIEF13/14 rules. Labels: **PROVED** (full proof here), **CHECKED**, **CONJECTURE**, **NUMERICS**
(scripts in `e1py/`, run with `python3 -I`; no proof depends on them). No assumption is added. Setting and notation:
write-up §§2–3, §7.7, §8.5 "Notation"; n = 3, ε ∈ (0,1), K′ = u + s(T1 − u), U = D_{K′}, M_U, P_i, E_i(X) = X △ P_i,
M (mixed part of U), N₊, R_ij, link classes Q_i (B1 notes); (H_U) = strict (G), (IB), (LA), (S), (C), T1 ∈ C_L.

A **shadow** is ν = (ρ_iμ)_i with ρ_i > 0 a.e. and integrable on U; its field is c^ν_i := ρ_iσ_i, its strict Bayes
sets B^ν_t := {g ∈ U : t·c^ν(g) > 0}, tie sets Z^ν_t. ν is **admissible** if D_{T1} = B^ν_{p*} ∪ S with S ⊆ Z^ν_{p*}
for some p* ∈ Δ°. A **dominator comparison** of ν at t is a comparison C ⪯_k B^ν_t (k = 1, 2, 3) in which the coherent
model C satisfies C ⪯_k B^ν_t at every world k.

---

## 0. Outcome

**No cover was constructed. The attempt broke at step (2), before any selection was chosen: the D2 mechanism cannot
be made to fail the endorsements that Theorem M0closed needs, wherever it is installed.**

**Single obstruction revealed: protection and visibility are mutually exclusive.**
- D2 keeps its ratio certificate consistent by *protection*. Every generator comparison is +1 on a target that meets
  every neighbourhood of an *end*, and every other accepted comparison is eventually ≥ 0 there.
- In three worlds an end can only sit where the protected world is eventually correct for T1, and for every selected
  model with a forced trade (Lemma E1.3). These are limits of near-unanimous problems. No fixed region qualifies.
- At such an end, the M0closed argument may use a shadow that is arbitrarily heavy there (Lemma E1.4). The Bayes
  models of that shadow are then correct deep in the end. So no dominator comparison against them is positive there,
  and none is a protected comparison.
- Theorem M0closed needs one admissible shadow and only its dominator comparisons (Theorem E1.1). So protected
  failures of adding up are invisible to it. Theorem E1.5 turns this into an exclusion.

In the brief's terms, D2's mechanism has two parts:
- **The base.** This is the selected model out of which the generators compare. It can be moved anywhere, including
  T1 = C_{p*}.
- **The protection.** This is the end, and it cannot be moved off the unanimity boundary.

What M0closed needs unendorsed are dominator comparisons into incoherent shadow-Bayes models. These models can be
taken within η of T1, at shadow weights near a vertex (Theorem E1.2). A shadow that is heavy at the ends separates the
two.

| | Statement | Label |
|---|---|---|
| E1.1 | M0closed(b) uses exactly one admissible shadow's dominator comparisons at a.e. weight. T1's own out-comparisons are never needed. | PROVED (from M0closed(a), Thm kkm) |
| E1.2 | Theorem R3 without its case split: case (ii) always holds, with admissible shadows. | PROVED; NUMERICS |
| E1.3 | Ends of an end-protected world are T1-correct next to two endorsing worlds; under (Nest_e) no fixed region is unsourced. | PROVED |
| E1.4 | Sink-heavy reweighting keeps admissibility and makes every Bayes model correct deep in the ends. | PROVED; NUMERICS |
| E1.5 | No cover of T1 has all worlds end-protected decorations of bases that add up with end-heavy densities. | PROVED |
| E1.6 | D2's world 1 is such a decoration. Its heavy shadow's Bayes models are exactly the selected path. | PROVED; NUMERICS |

Consequence for D2 §5: the sentence "nothing known excludes covers whose non-additive worlds are of the D2 type"
is superseded by E1.5, for the D2 type proper (end protection over a base like D2's). Even if Conjecture D2.C holds,
the world it installs cannot carry a cover of T1.

---

## 1. Task (1): exactly which endorsements M0closed uses

**Theorem E1.1 (PROVED).** Assume (H_U), and let ν be an admissible shadow. Put
I_ν := {t ∈ Δ° : Z^ν_t null, B^ν_t incoherent}.
- **(a)** I_ν is not Lebesgue-null.
- **(b)** For every t ∈ I_ν, Theorem kkm gives an undominated selected C with C ⪯_k B^ν_t at every k. For every
  coherent C with this property, some world j has ν_j(E_jC) > ν_j(E_jB^ν_t). That is, a dominator comparison
  C ⪯_j B^ν_t is not endorsed by ν.

Conversely, **(c)**: if some admissible ν endorses at every world the dominator comparisons supplied by Theorem kkm
at a.e. t ∈ Δ°, then (H_U) is contradictory.

*Proof.*
- **(a)** For each g, {t : t·c^ν(g) = 0} is a line, so by Tonelli Z^ν_t is null for a.e. t. If I_ν were null, B^ν_t
  would be coherent for a.e. t ∈ Δ°. That is property (γ) for the strictly signed field c^ν. Admissibility is
  D_{T1} = B^ν_{p*} ∪ S with S ⊆ Z^ν_{p*}. Theorem M0closed(a) excludes this.
- **(b)** Let C be coherent with C ⪯_k B_t at every k, and suppose every such comparison were endorsed. Then
  t·ψ^ν(C) ≤ t·ψ^ν(B_t), where ψ^ν_k(X) := ν_k(E_kX).
  - C is regular: a coherent model accepts every nonzero nonnegative gamble.
  - B_t is the pointwise, hence unique (mod null), minimiser of t·ψ^ν over all models, since Z_t is null.
  - So C = B_t a.e., which contradicts the incoherence of B_t.
  - Theorem kkm needs (LA) and (S) and supplies the undominated selected dominator.
- **(c)** Under that endorsement, the argument of (b) shows that I_ν is null, against (a). ∎

*What this says (task (1)).*
- **Which comparisons.** Only dominator comparisons C ⪯_k B^ν_t of a single admissible shadow ν, at all three worlds.
  They are needed for t in a full-measure part of Δ°, and only the dominators that Theorem kkm supplies matter.
- **T1's out-comparisons are never used.** Condition (α) of Prop. M0 is obtained by *choosing* ν. Admissible shadows
  exist whatever the ranking is: ν^L of Prop. Q31 has B_t = D_{T1} with null ties on Q_L. Prop. M0 instead derives
  (α) from endorsement of T1's out-comparisons, because there the shadow is extracted from the ranking.
- **Relation to M0closed(b).** If every world adds up with countably additive weights, those weights form an
  admissible shadow (Prop. M0(α), via N17 Prop. 2.1) that endorses everything, so (c) applies. For purely finitely
  additive weights, M0closed(b) keeps its own route (N13 Prop. B). (c) is a different sufficient condition, not a
  restatement.
- **Which weights.** I_ν cannot be confined to a compact subset of Δ° in general: for ν^L, I_{ν^L} ∩ Q_L = ∅
  (Prop. Q32), so it lies near ∂Δ. This is the index non-locality of Prop. Q31.
- **Which worlds.** If worlds j, k have densities ρ_j, ρ_k that endorse all of their comparisons (for example leading
  densities, B1.0), take ν_j = aρ_j and ν_k = bρ_k. Then every failure in (b) is at the third world.

**Theorem E1.2 (R3 without the case split; PROVED).** Assume (H_U). For every η > 0 there are:
- an admissible shadow ν′;
- a weight t ∈ Δ° with null ties, at which B^{ν′}_t is incoherent and μ(B^{ν′}_t △ D_{T1}) < η;
- a selected undominated C with C ⪯_k B^{ν′}_t at every k;
- a world j at which C ⪯_j B^{ν′}_t is not endorsed by ν′.

*Proof.* Use ν^L (L > 2, weights L where T1 is correct at world i, 1 elsewhere) and the cone C_η of the proof of
Theorem R3.
- Multiply the correct-world weights by M = 2/min_i t_i + 1 off C_η. Call the result ν′.
- **ν′ stays admissible with p* = u.**
  - Off C_η: LM·u_i ≥ LM/3 > 2/3 ≥ Σ_{err} u_i.
  - On C_η: some world is correct, so L/3 > 2/3 ≥ Σ_{err} u_i.
  - So B^{ν′}_u = D_{T1} with null ties.
- **At t near e_j** (w_j < 0, t generic):
  - Off C_η, B^{ν′}_t = D_{T1}.
  - On C_η, a non-null part is rejected.
  - So B^{ν′}_t = T1 ∖ C′ is incoherent and η-close to T1, exactly as in R3.
- Theorem kkm gives C, and Theorem E1.1(b) gives the unendorsed comparison. ∎

R3 needed the case split only to keep ν′ in 𝒩, the shadows that endorse T1's out-comparisons. By E1.1 that is
unnecessary. The dominator may be T1 itself.

NUMERICS (`e1py/e1_bathtub.py`, `.out`; ε = 0.3, s = 0.9, L = 5, 4·10⁵ samples):
- B_u = T1 for ν^L and for every ν′, with no ties;
- for θ ∈ {0.2, 0.1, 0.05} and t = (d, d, 1 − 2d), d ∈ {0.02, 0.01, 0.005}: B′_t = T1 off C_η, B′_t ⊆ T1, and all
  of C_η is removed;
- convexity is violated at 1798 of the 1800 removed points tested: each is the midpoint of two points of
  D_{T1} ∖ C_η that B′_t accepts. For the other 2 the search (20 random directions) found no witness; incoherence
  of B′_t does not depend on them, since it holds by the proof.

**Answer to task (1).** A non-adding-up world breaks M0closed only if it does the following for **every** admissible
ν (all of them, not one): on a non-null set of weights t, some dominator comparison into the incoherent model B^ν_t
is left unendorsed. By E1.2 these incoherent models may be taken arbitrarily close to T1 in measure. Leaving T1's own
out-comparisons unendorsed (R3 case (i), the natural first reading of "install D2 at T1") breaks nothing.

---

## 2. Task (2): installing D2-type protection in three worlds

### 2.1 What D2's protection is, abstractly

**Definitions.**
- An **end** is a sequence S = (S_m) of measurable subsets of M, decreasing, each non-null, with μ(⋂_m S_m) = 0.
- A ternary δ is **S-positive** if μ({δ = 1} ∩ S_m) > 0 for every m. It is **eventually ≥ 0** (resp. **= 0**) on S
  if δ ≥ 0 (resp. = 0) a.e. on some S_m.
- World i is **end-protected** with a countable family 𝒮_i of ends if, for every relevant comparison C ⪯_i X
  (C ∈ C_L, X regular), the vector δ := 1_{E_iX} − 1_{E_iC} satisfies one of:
  - it is S-positive for some S ∈ 𝒮_i;
  - it is eventually ≥ 0 on every S ∈ 𝒮_i.

**D2 is of this form (PROVED, from Lemma D2.3).** Take 𝒮_1 = {S} with S_m := M ∩ {x ≥ 1 − 2^{−m}}.
- A relevant world-1 comparison has D(δ) = 0, so rule R⁰ applies.
- Either δ ∈ 𝒦₀, which is eventually ≥ 0 by the near-one clause;
- or δ − g_* ∈ 𝒦₀, so that δ ≥ 1_{Q_g} near x = 1, which is S-positive by (D2).

The generator comparisons of any D2-type design are therefore S-positive. "Targets that meet at every scale"
**is** S-positivity at an end.

### 2.2 Where an end can sit

**Lemma E1.3 (PROVED).** Assume (H_U).

**(a) Ends are T1-correct.** Let worlds 2 and 3 have densities ρ₂, ρ₃ that endorse all of their comparisons between
regular models (for example leading densities, B1.0, or additive worlds). Let world 1 be end-protected with family
𝒮₁. Then for every S ∈ 𝒮₁, μ(S_m ∩ E₁(T1)) = 0 for some m.

*Proof of (a).*
- Suppose μ(S_m ∩ E₁(T1)) > 0 for all m.
- Let R₀ := (+,−,−) ∩ D_{T1}. It is non-null: it contains a neighbourhood of a point just inside D_{T1} near the
  corner ray r_23 = (κ+1, −1, −1).
- Choose depths m(S′) for the countably many S′ ∈ 𝒮₁ so that R := R₀ ∖ ⋃_{S′} S′_{m(S′)} is non-null. This uses
  μ(⋂S′_m) = 0 and a summable choice.
- Let p := ⋃_{m ≥ m₀} p_m with p_m ⊆ S_m ∩ E₁(T1) non-null, m₀ := m(S), and ρ₂(p) + ρ₃(p) < min(ρ₂(R), ρ₃(R)).
- Put X := T1 △ (p ∪ R); X is regular. R consists of world-2 and world-3 errors of T1, and p costs at most ρ_k(p).
  So ρ_k(E_kX) < ρ_k(E_kT1) for k = 2, 3.
- By endorsement T1 ⋠₂ X and T1 ⋠₃ X.
- T1 is competitive on {1,2,3}: by Theorem kkm it is tied at every world with a selected model. Hence T1 ⪯₁ X.
- This comparison is relevant, with δ = 1_R − 1_p.
- **Not eventually ≥ 0 on S:** δ = −1 on p ∩ S_m, which is non-null for every m.
- **Not S′-positive for any S′ ∈ 𝒮₁:** {δ = 1} = R misses S′_{m(S′)}.
- This contradicts end-protection. ∎

*The same argument at any selected C_p.* It works for any selected C_p competitive on {1,2,3} with C_p ∩ (+,−,−)
non-null. On e₁₂ it uses world 2 alone. So ends are eventually world-1-correct for every selected model that has
forced world-1 trades.

**(b) No fixed protected region.** Assume (Nest_e) at world 1 on e₁₂ and e₁₃, and that ρ₂, ρ₃ endorse as in (a).
Let A ⊆ M be non-null. Then world 1 has a relevant comparison whose vector is −1 on a non-null subset of A. So no
non-null fixed region Π has all forced world-1 comparisons ≥ 0 on Π, which is the near-one property D2 uses.

*Proof of (b).*
- M = R₁₂ ∪ R₁₃. Say μ(A ∩ R₁₂) > 0.
- By Prop. Q35(1), c_b = E₁(C_p) increases continuously in measure to R₁₂ as b → 1. So μ(A ∩ c_b) > 0 for some
  b ∈ (0,1), and d_b = R₁₂ ∖ c_b is non-null.
- Take a non-null piece ⊆ A ∩ c_b, and R ⊆ d_b with ρ₂(R) > ρ₂(piece).
- X := C_p △ (piece ∪ R) is strictly ρ₂-better than C_p. Competitiveness on {1,2} gives C_p ⪯₁ X, with
  δ = 1_R − 1_piece. ∎

So D2-type protection exists only in the limit form, at an end where the protected world is eventually correct for
T1 and for every selected model with forced trades. These are the near-unanimous limits:
- for world 1, gambles approaching the e₁ ray inside (+,−,−) ⊆ Q₁;
- for world 1, gambles approaching the face {h₂ = 0} inside (+,−,+) ⊆ Q₂, which is the e₂-end of the e₁₂ chain used
  in D2.C;
- in two worlds, D2's x → 1.

The link classes change nothing: each such end lies in a single sign class.

### 2.3 Ends are invisible

**Lemma E1.4 (PROVED).** Let ν be admissible, with D_{T1} = B^ν_{p*} ∪ S, S ⊆ Z^ν_{p*}. For each world i let 𝒮_i be a
countable family of ends with S_m ∩ E_i(T1) null for large m. Then there is an admissible ν′ with the following
properties:
- ν′_i = ν_i(1 + f_i), where f_i ≥ 0 is supported in the ends of world i;
- for every t ∈ Δ°, every i and every S ∈ 𝒮_i, B^{ν′}_t is world-i-correct a.e. on S_m for m ≥ m(S, t).

Consequently, no vector 1_{E_iB^{ν′}_t} − 1_{E_iC} (any model C) is S-positive for any S ∈ 𝒮_i.

*Proof.*
- **The reweighting.** Enumerate the pairs (S, l) with S ∈ ⋃_i 𝒮_i and l ∈ ℕ. Pick depths m_l(S) beyond which
  S ∩ E_i(T1) is null, with (ρ_j + ρ_k)(S_{m_l(S)}) ≤ 2^{−r(S)} l^{−3}, where r(S) is the index of S. Put
  f_i := Σ_{S ∈ 𝒮_i} Σ_l l·(ρ_j + ρ_k)/ρ_i · 1_{S_{m_l(S)}}. Then ρ_i f_i is integrable.
- **Admissibility.** On supp f_i, T1 is correct at world i a.e. Raising ρ_i there raises the margin
  p*·c(g)·(±1 according to g ∈ T1). So D_{T1} = B^{ν′}_{p*} ∪ S′ with S′ ⊆ S.
- **Correctness deep in the ends.** On S_{m_l(S)}, f_k = 0 a.e. at every world k at which T1 errs, by the choice of
  depths. At the worlds where T1 is correct, σ_k = σ_i. Hence
  t·c^{ν′}(g)σ_i(g) ≥ t_iρ_i(1 + f_i) − t_jρ_j − t_kρ_k ≥ (t_i·l − 1)(ρ_j + ρ_k) > 0 once l > 1/t_i. ∎

**Theorem E1.5 (end-protected decorations are excluded; PROVED).** Assume (H_U). Suppose that each world i is
end-protected with a countable family 𝒮_i (possibly empty), and that there are densities ρ_i > 0, integrable, with:
- **(b)** every relevant comparison of world i whose vector is eventually = 0 on every S ∈ 𝒮_i is ρ_i-endorsed (the
  **base adds up**);
- **(h)** for every S ∈ 𝒮_i, ess inf_{S_m} ρ_i/(ρ_j + ρ_k) → ∞ as m → ∞ (the density is **heavy at its ends**).

Then there is a contradiction. So no cover of T1 on M_U has this form.

*Proof.* Let ψ := (ρ_iμ).

1. **ψ is admissible.**
   - Suppose a regular X has ψ_k(X) < ψ_k(T1) for all k.
   - Let Y agree with X except on S_m for every end S of every world, where it agrees with T1. Take the depths so
     deep that the ψ-mass of the change is below the margin. Y is regular and still strictly ψ-better at every world.
   - By competitiveness (via Theorem kkm, as in E1.3(a)), T1 ⪯_k Y for some k.
   - Its vector is eventually = 0 on every end of world k, so by (b) ψ_k(T1) ≤ ψ_k(Y). This is a contradiction.
   - So ψ(T1) is weakly Pareto in the convex compact (Lyapunov) set {ψ(X) : X regular}. A supporting weight
     p* ∈ Δ exists, and T1 is a pointwise ψ-minimiser on M.
   - p* is interior. At p = (p₁, p₂, 0) or at a vertex, the non-null set of (−,−,+)-gambles that T1 accepts near
     r₁₂ (and its cyclic images) would contradict pointwise minimality.
2. **(D) holds for ψ.**
   - Let t ∈ Δ° have null ties, and let C ⪯_i B^ψ_t at every i.
   - By (h), B^ψ_t is world-i-correct deep in every S ∈ 𝒮_i, by the computation of E1.4 with f = 0. So
     δ = 1_{E_iB_t} − 1_{E_iC} is ≤ 0 there and S-positive for no S.
   - End-protection makes δ eventually ≥ 0 on every S ∈ 𝒮_i, hence eventually = 0.
   - By (b) it is ψ_i-endorsed.
3. Theorem E1.1(c) gives the contradiction. ∎

*Scope.*
- (b) and (h) concern a base density that is heavy at its ends. Lemma E1.4 alone does not let one reweight a base
  that adds up only with a non-heavy density, because (b) is not inherited by ρ_i(1 + f).
- The general form of the statement is unconditional, via E1.1 and E1.4: in **any** cover and for **every**
  admissible ν, the end-heavy ν′ has unendorsed dominator comparisons, and none of them is end-positive. So the
  failures M0closed needs are always carried by comparisons that are eventually 0 at every end, never by D2-type
  generators.
- Additive bases of gauge-mixture type (R10a Thm M) satisfy (h) automatically at the e₁-ray end. There
  c₂(h), c₃(h) → c₂(e₁), c₃(e₁) = 0 while c₁ stays bounded away from 0 (CHECKED by inspection of Thm M). So the
  brief's "additive near-cover plus D2 modifications" falls under E1.5.

**Proposition E1.6 (D2's own non-additivity is M0-invisible; PROVED).** In the system of Theorem D2.1, let
w : [0,1) → [1, ∞) be nondecreasing, λ-integrable in the chain coordinate x, with w(x) → ∞ as x → 1. Let
ν′ := (w(x)λ on M and λ on N₊ at world 1; λ at world 2). Then:
- **(i)** ν′ endorses every relevant world-1 comparison that is not end-positive;
- **(ii)** for a.e. t, B^{ν′}_t = C_{x_t} with x_t := inf{x : t₁w(x) > t₂}, a selected model.

So D2's world 1 meets (b) and (h) of E1.5 in its two-world system. Its failure of SP^reg sits entirely in
end-positive comparisons, which never meet the shadow's Bayes models.

*Proof.*
- **(i)** Such a comparison has δ ∈ 𝒦₀ with D(δ) = 0. With τ(t) := ∫_{x ≥ t}δ ≥ 0 and τ(1) = 0, summation by parts
  gives ∫wδ dλ = w(0)τ(0) + ∫τ dw ≥ 0. For unbounded w, pass to the limit through min(w, n).
- **(ii)** On M, σ₁ = −σ₂, so t·c(g) = σ₁(g)(t₁w(x) − t₂). Thus E₁(B_t) ∩ M = {w < t₂/t₁}, an initial segment, and
  N₊ is accepted. Ties are non-null only for the countably many values t₂/t₁ at which w has a flat piece. A regular
  model is determined by its world-1 error set. ∎

NUMERICS:
- `e1py/e1_d2_invisible.py` (exact integer cell model, 64 cells, last block as end):
  - 20000 𝒦₀ elements, no negative w-sums, and the summation-by-parts identity holds exactly;
  - 3000 heavy shadows, every Bayes error set an initial segment;
  - dominator vectors vanish on the end; generator vectors are ≥ 1 on their targets.
- `e1py/e1_heavy.py` (T1, ε = 0.3, s = 0.9):
  - 20 random admissible shadows keep B_u = T1;
  - on the (+,−,−) end near the e₁ ray (depths 3–17), unweighted shadows reject 7 980 080 sink samples over random
    t, while the heavy reweighting rejects none at depth > 1/t₁;
  - heaviness keeps B_u = T1;
  - an instance of E1.3(a): toggling p ∪ R lowers both neighbour losses (−33087, −31599).

### 2.4 Moving the mechanism, and Conjecture D2.C

- **The base.** D2's generators compare out of an interior chain point C_a. In three worlds the same design can
  compare out of any selected model, T1 included: sources in E₁(T1), targets in a T1-correct end. That makes every
  shadow fail on T1's out-comparisons (R3 case (i)). By E1.1 this is irrelevant.
- **The end.** It cannot be moved to p*, or anywhere off the unanimity boundary (E1.3). It is not a feature of edge
  chains as such: it is the one place that no forced world-1 trade can empty.
- **Conjecture D2.C.** If it holds, it would install an end-protected world 1 on R₁₂ over a D2-like base. E1.5
  excludes that world from every cover of T1 as soon as its base adds up with a density heavy at its end, which is
  what D2's base does (E1.6). So D2.C, true or false, does not bear on T1.

---

## 3. Task (3): not reached

No selection was built: by §2, every D2-type installation is excluded or inert before one is chosen.

What a cover still needs (E1.1, E1.4) is the following. For every admissible ν, and in particular for every end-heavy
one, there must be a non-null set of weights t at which some dominator comparison into the incoherent B^ν_t is
unendorsed and is eventually 0 at every end. These are unprotected comparisons, so the D2 mechanism cannot keep them
consistent.

In two worlds next to an additive world, D2 §0 states, without a proof in the corpus, that unprotected ratio
certificates can be separated by transport and then summed into a violation of (SR₁)/(QC₁). Whether this holds in
three worlds is the open point. I state no conjecture beyond it.

## 4. Files (`e1py/`, run with `python3 -I`)

- `e1_common.py`: geometry of T1, U and shadows.
- `e1_bathtub.py` (+ `.out`): E1.2.
- `e1_heavy.py` (+ `.out`): E1.4 and an E1.3(a) instance.
- `e1_d2_invisible.py` (+ `.out`): E1.6 in the exact cell model.
