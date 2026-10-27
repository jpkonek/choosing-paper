# F2. Audit of E1 and of the B3 summary line, against the external auditor's objections and the ∂U proposal

15 Oct 2026. Adversarial audit. Labels: **PROVED** (full proof here, or a re-derivation of a cited proof), **CHECKED**
(verified by inspection of a cited proof), **CONJECTURE**, **NUMERICS** (scripts in `f2py/`, run with `python3 -I`;
no verdict rests on them), **GAP**, **WRONG**. No assumption is added. Every hypothesis of every statement is written
out. Setting and notation: write-up §§2–3, §7.7, and the §8.5 Notation; E1_notes §1–§2.1 (shadow, admissible, dominator
comparison, end, S-positive, end-protected). Read: E1_notes (all), D2_notes, D2_referee2, B1_notes/referee,
B3_notes/referee, write-up §§2–3, §7.7, §8.5(e)–(g), starthere "Update, 15 October 2026, evening", roundreport
"Rounds 14–16 addendum".

---

## 0. Outcome

1. **The auditor is right on both counts.**
   - **(i) B3.** The summary sentence "a world in a cover that does not add up must be incomplete" is **conditional on
     Conjecture B3.C**. What is proved is narrower: a total world of a cover that does not add up is not almost
     representable on M (§3).
   - **(ii) E1.** The summary sentence "D2-type failures are invisible to M0closed / E1 excludes D2-type worlds"
     omits hypotheses. Theorem E1.5 excludes a cover only when **all three** worlds are end-protected decorations.
     Each must have an **integrable** base density, and the three densities must be **jointly** heavy at the ends
     (condition (h) involves the other worlds' densities). Lemma E1.3(a) needs the two other worlds to carry densities
     that endorse their comparisons out of T1.
2. **E1's location claim is unproved, and false as a characterisation.**
   - E1 §0, §2.2 and §2.4 say that ends are "near-unanimous limits" and that protection "cannot be moved off the
     unanimity boundary". Nothing proves this.
   - What E1.3(a) proves is eventual **T1-correctness** of the ends at the protected world. That holds at ∂U as well:
     on a collar of ∂U, T1 rejects everything, so world i is correct wherever h_i < 0 (Prop. F2.1).
   - Under (Nest_e) on both edges at e_i, ends must approach **either** the near-unanimous boundary (h_i > 0) **or**
     ∂U ∩ {h_i < 0}. E1 lists only the first (Cor. F2.3).
   - D2's own end {x → 1} is partly at ∂U: about 56 % of its mass in the NUMERICS of `f2py/f2_d2_geometry.py`.
3. **But the E1 mechanism is location-free.**
   - Lemma E1.4 (heavy reweighting) needs only that the ends are eventually T1-correct. At ∂U ∩ {h_i < 0} this is
     automatic (F2.1), so it needs no hypothesis on the other worlds there.
   - Theorem E1.5 does not use E1.3 at all.
   - So moving the protection to ∂U (the auditor's D2′) does **not** escape E1.4. It escapes E1.5 exactly when the
     protected world's base has no integrable end-heavy endorsing density compatible with the other worlds, or when
     another world fails to add up integrably.
4. **New result: D2 refutes Conjecture σB as stated (Prop. F2.4).**
   - In D2, every countably additive endorser of world 1 whose density is finite and positive a.e. gives **infinite
     mass to every neighbourhood of every point of the ray (1,0)**. That ray lies in the interior of U.
   - So no locally integrable endorser exists, and Conjecture σB (write-up Conj. sigmaB) is **false**.
   - The write-up's status sentence "bounded on every closed subcone of U" is **WRONG**: ρ = 1/(1−x) blows up at
     (1,0).
   - This confirms the auditor's infinite-mass observation, already for D2 itself. It concerns endorsers of
     **base + generators** only. E1.5 needs an endorser of the **base** alone, and in D2 an integrable heavy one exists
     (E1.6). So F2.4 does not touch E1.5.
5. **Nothing proved excludes a three-world cover of T1 with protection at ∂U.** The open route is stated precisely in
   §4.3.

---

## 1. Task 1: what E1.1–E1.6 prove, with all hypotheses

### 1.1 Objects

- **Shadow:** ν = (ρ_iμ)_{i=1,2,3} with ρ_i ∈ L¹(μ) and ρ_i > 0 a.e. on U. Its field is c^ν_i = ρ_iσ_i. Its strict
  Bayes sets are B^ν_t, its tie sets Z^ν_t.
- **Admissible:** D_{T1} = B^ν_{p*} ∪ S with p* ∈ Δ° and S ⊆ Z^ν_{p*}.
- **End:** a decreasing sequence (S_m) of non-null measurable subsets of M with μ(⋂S_m) = 0. Nothing restricts its
  location: it may shrink to ∂U, to the near-unanimous boundary, to ∂D_{T1}, or to a single interior ray.
- **End-protected world i** (with a countable family 𝒮_i): every *relevant* comparison C ⪯_i X (C ∈ C_L, X regular)
  has vector δ = 1_{E_iX} − 1_{E_iC} that is S-positive for some S ∈ 𝒮_i, or eventually ≥ 0 on every S ∈ 𝒮_i.
- **Base of world i:** its relevant comparisons that are S-positive for no S ∈ 𝒮_i. Under end-protection, these are
  exactly the relevant comparisons whose vector is eventually = 0 on every S ∈ 𝒮_i (PROVED: not S-positive gives
  δ ≤ 0 a.e. on some S_m; end-protection gives δ ≥ 0 a.e. on some S_{m′}).
- **"World i is an end-protected decoration of a base that adds up with an end-heavy density"** means, formally, that
  world i is end-protected with a countable 𝒮_i and that some ρ_i ∈ L¹(μ), ρ_i > 0 a.e., satisfies:
  - **(b)** ρ_iμ endorses every base comparison of world i;
  - **(h)** for every S ∈ 𝒮_i, ess inf_{S_m} ρ_i/(ρ_j + ρ_k) → ∞, where ρ_j and ρ_k are the densities chosen for the
    other two worlds.

  **(h) is not a property of world i alone.** E1.5 is a statement about a triple (ρ₁, ρ₂, ρ₃). A world with
  𝒮_i = ∅ qualifies iff an integrable a.e.-positive density endorses all its relevant comparisons. Only relevant
  comparisons are needed, not all comparisons between regular models.

### 1.2 Verdicts

| Item | Exact content (all hypotheses) | Verdict |
|---|---|---|
| E1.1 | (H_U); ν an admissible **integrable** shadow. (a) I_ν is not null (integrability not used). (b) At every t ∈ I_ν, every coherent C with C ⪯_k B^ν_t at all k has some j with ν_j(E_jC) > ν_j(E_jB^ν_t) (uses finiteness of ψ^ν). (c) If one admissible integrable ν endorses, at every world, the kkm dominator comparisons at a.e. t, then (H_U) is contradictory | **PROVED** (re-derived). **GAP** in the remark "Which worlds": "take ν_j = aρ_j, ν_k = bρ_k; then every failure is at the third world" needs an admissible completion (ν_i, aρ_j, bρ_k), which is not automatic (§1.3) |
| E1.2 | (H_U) only. For every η > 0 there are an admissible integrable ν′, a weight t with null ties, B^{ν′}_t incoherent and η-close to T1, a selected dominator, and an unendorsed dominator comparison | **PROVED** (re-derived). No hypothesis on any world |
| E1.3(a) | (H_U); world 1 end-protected with countable 𝒮₁; ρ₂, ρ₃ > 0 a.e., **finite a.e.**, endorsing the relevant comparisons **out of T1** at worlds 2, 3 (i.e. ρ₂μ ∈ 𝒩₂, ρ₃μ ∈ 𝒩₃ in the notation of Thm R3, with integrability relaxed to a.e. finiteness). Then every S ∈ 𝒮₁ is eventually T1-correct at world 1. Variant: the same holds for any C ∈ C_L competitive on {1,2,3} that is world-1-correct and world-2,3-wrong on a non-null set outside the deep ends, provided ρ₂, ρ₃ endorse the comparisons out of C | **PROVED**. E1 states the hypothesis as "endorse all comparisons between regular models", which is stronger than needed. Uses only comparisons out of T1 (resp. C) |
| E1 §2.2 "these are the near-unanimous limits"; §0/§2.4 "cannot be moved off the unanimity boundary" | — | **WRONG / unproved**. T1-correct regions include a collar of ∂U ∩ {h₁ < 0} (F2.1), the correct side of ∂D_{T1}, and interior regions. Even under (Nest_e) on both edges, ∂U ∩ {h₁ < 0} remains (F2.3) |
| E1.3(b) | (H_U); (Nest_e) at world 1 on e₁₂ and e₁₃; world 2 (resp. 3) with a density, a.e. positive and finite, that endorses comparisons out of edge-selected models. For non-null A ⊆ M, some relevant world-1 comparison has vector −1 on a non-null part of A | **PROVED**. It excludes fixed protected regions only. The same construction, with pieces at every depth, gives the edge constraint F2.2 on ends |
| E1.4 | ν admissible integrable shadow; for each world i a countable family 𝒮_i of ends, each **eventually T1-correct at world i**. Then the reweighting ν′_i = ν_i(1 + f_i) (f_i ≥ 0 supported in the world-i ends) is an admissible integrable shadow, and B^{ν′}_t is world-i-correct deep in every S ∈ 𝒮_i for every t ∈ Δ° | **PROVED** (re-derived). **Location-free.** It needs no hypothesis on the rankings, only T1-correctness of the ends |
| E1.5 | (H_U); **every** world end-protected (countable 𝒮_i, possibly empty); integrable ρ_i > 0 a.e. with (b) and (h) for the triple. Contradiction | **PROVED** (re-derived; no gap found). **Location-free; does not use E1.3.** Needs integrability (Lyapunov range, finite Bayes risks) |
| E1.5 "Scope: unconditional general form" | "In any cover, for every admissible ν, the end-heavy ν′ has unendorsed dominator comparisons, none end-positive" | **Correct only when every end is eventually T1-correct at its world** (the hypothesis of E1.4). This is automatic at ∂U ∩ {h_i < 0}. Elsewhere it holds under E1.3(a)'s hypotheses, and not otherwise |
| E1.6 | Two-world system of D2.1 (any design); w nondecreasing, integrable, → ∞. (i) wλ endorses every non-end-positive relevant world-1 comparison. (ii) Bayes sets are chain models | **PROVED** (re-derived). Two-world only; it says nothing about a three-world installation |
| E1 §2.4 "D2.C, true or false, does not bear on T1" | — | **Overstated**. It holds only if the installed world's base has an integrable end-heavy endorser on all of M, compatible with integrable endorsers of the other two worlds. That is not shown (E1.6 is two-world) |

### 1.3 Proof checks (where something could break)

- **E1.1(a).** The complement of I_ν in Δ° is {Z_t non-null} ∪ {B_t coherent}. The first set is null by Tonelli. So a
  null I_ν would give (γ) for the strictly signed field c^ν, and with admissibility Thm M0closed(a) applies. M0closed(a)
  uses no integrability. ✓
- **E1.1(b).** Since Z_t is null, t·ψ^ν(X) = const − ∫_X t·c^ν dμ has the a.e.-unique minimiser B_t. Endorsement of
  all three comparisons C ⪯_k B_t would give C = B_t. ✓ The kkm dominator C is in C_L and B_t is regular, so the
  comparison is relevant. Finite ψ is used: for non-integrable ρ only differences on C △ B_t are available.
- **E1.1 remark GAP.**
  - Admissibility of (ν_i, aρ_j, bρ_k) needs, on {T1 correct only at j}, a lower bound on aρ_j/(bρ_k) (and
    symmetrically on {T1 correct only at k}). Raising ν_i cannot help there, because T1 errs at i.
  - So the remark holds only when such a completion exists.
- **E1.2.**
  - ν^L is admissible with p* = u, because every g ∈ U has a world at which T1 is correct: T1 ⊇ N₊, and U contains no
    nonzero g ≤ 0.
  - The ν′ estimates and the midpoint argument re-derive.
- **E1.3(a).**
  - X = T1 △ (p ∪ R), with R ∩ p = ∅ since R misses S_{m(S)} ⊇ p. Worlds 2 and 3 strictly improve, so endorsement
    gives T1 ⋠₂ X and T1 ⋠₃ X.
  - T1 is competitive on {1,2,3}: it is tied at every world with some C_p (kkm), and C_p is competitive on
    supp p ⊆ {1,2,3}. So T1 ⪯₁ X, and δ = 1_R − 1_p violates end-protection. ✓
  - Only a.e. finiteness of ρ₂, ρ₃ is used: a non-null set has non-null subsets of arbitrarily small ρ-mass.
- **E1.4.**
  - ∫ρ_if_i ≤ Σ_S 2^{−r(S)} Σ_l l^{−2} < ∞. ✓
  - Admissibility: ρ_i is raised only where T1 is correct at i. ✓
  - Deep in S, the worlds where T1 errs keep their weights. The worlds where T1 is correct have σ_k = σ_i. Hence
    t·c′σ_i ≥ (t_i l − 1)(ρ_j + ρ_k) > 0 once l > 1/t_i. ✓
  - NUMERICS (`f2_ends_T1.py` (3)): with a ∂U end in (−,+,+), the heavy ν^L keeps B_u = T1 with no ties, and its Bayes
    sets never err at world 1 deep in the end (0 of 462 558 samples).
- **E1.5.**
  - Step 1: Y = X off the deep ends and Y = T1 on them. The comparison T1 ⪯_k Y is a base comparison, so (b) applies.
    The Lyapunov range is compact and convex, so a supporting p* exists. p* is interior because T1 accepts a non-null
    set of (−,−,+) gambles near r₁₂ (and cyclic images). ✓
  - Step 2: (h) alone makes B^ψ_t world-i-correct deep in S. The computation is that of E1.4 with f = 0 and does not
    need T1. The dominator comparison is relevant, and not S-positive, so it is base. (b) endorses it. ✓
  - Step 3 is E1.1(c). ✓
  - E1.3 is not used. Nor is any location of the ends.
- **E1.6.** For δ ∈ 𝒦₀, ∫min(w,n)δ dλ = min(w,n)(0)τ(0) + ∫τ d min(w,n) ≥ 0. Pass to the limit by dominated convergence
  (|δ| ≤ 1, w integrable). ✓

### 1.4 Where ends can sit

**Prop. F2.1 (PROVED).**
- **Statement.** There is η₀ > 0 with D_{T1} ∩ {h : P_{K′}(h) < η₀|h|} = ∅ (mod null). So on that collar of ∂U, T1
  rejects every gamble, and T1 is world-i-correct a.e. on the collar ∩ {h_i < 0}. Consequently, every end of world i
  that eventually lies in {P_{K′}(h) < η|h|, h_i < 0} for some η ≤ η₀ satisfies the hypothesis of E1.4, with no
  hypothesis on any world.
- *Proof.* cl D_{T1} ∖ 0 ⊆ U (write-up §2.5). P_{K′} is continuous and positive on the compact set
  cl D_{T1} ∩ {|h| = 1}, so its minimum η₀ there is positive. ∎
- NUMERICS (`f2_ends_T1.py` (1)): within margin 2·10⁻³ of ∂U, T1 accepts nothing in any sign class. World 1 is correct
  on all of (−,−,+), (−,+,−), (−,+,+) and wrong on all of (+,·,·).

**Prop. F2.2 (edge constraint on ends; PROVED).**
- **Hypotheses.** Strict (G), (IB), (LA), (S) on M_U. (Nest_e) at world 1 on e₁₂. A density ρ₂ > 0, finite a.e., whose
  measure endorses the world-2 comparisons C_p ⪯₂ X with p in the open edge e₁₂ and X regular. World 1 end-protected
  with a countable 𝒮₁.
- **Conclusion.** For every S ∈ 𝒮₁, every b < 1 and large m, μ(S_m ∩ c_b) = 0. Hence for every η > 0 and large m,
  S_m ∩ R₁₂ ⊆ {h : m₂(h) < η|h|} mod null. Here m₂(h) := min(P_{K′}(h), h₂) if h₁ < 0 < h₂, and m₂(h) := −h₂ if
  h₁ > 0 > h₂.
- *Proof.*
  - *First claim.* Run E1.3(b)'s construction at C := C_p, β(p) = b. Take R ⊆ d_b off the deep ends, and
    p ⊆ ⋃_{m ≥ m(S)} (S_m ∩ c_b) with pieces at every depth and ρ₂(p) < ρ₂(R) < ∞. Put X := C △ (p ∪ R).
    - World 2 strictly improves, so C ⋠₂ X by endorsement.
    - C is competitive on {1,2}, so C ⪯₁ X with vector 1_R − 1_p.
    - That vector is neither eventually ≥ 0 on S nor S′-positive for any S′. This contradicts end-protection.
  - *Second claim.* By Prop. Q35(1), μ(c_b △ R₁₂) → 0 as p → e₂. Off R₁₂, C_p = P₁ = P₂ (Lemma Q34). So C_p → P₂ in
    measure, and K_p → co(K′ ∪ {e₂}) in Hausdorff distance (R1 Prop 3.1, as used in Lemma quasilin(b)).
    - If h₁ < 0 < h₂ and m₂(h) ≥ η|h|: P_{K_p}(h) ≥ m₂(h) − d_H|h| > 0 once d_H < η, so h ∈ E₁(C_p).
    - If h₁ > 0 > h₂ and −h₂ ≥ η|h|: K_p has a point m within d_H of e₂, with m·h < 0, so h ∈ E₁(C_p).
    - Hence d_b ⊆ {m₂ < η|·|} for b near 1, and the first claim gives the inclusion. ∎
- So the far end of the e₁₂ chain is **near ∂U ∩ {h₁ < 0 < h₂}, or near the plane {h₂ = 0}**.
  - The plane part includes the near-unanimous face (+,0,+).
  - It also includes mixed directions in the interior of U, such as (−1,0,b) for b ≳ 2.15 and (1,0,−b) for b ≲ 0.45
    (`f2_ends_T1.py` (2)).

**Cor. F2.3 (PROVED).**
- **Hypotheses.** Those of F2.2 on e₁₂ and on e₁₃, the latter with world 3 and ρ₃.
- **Conclusion.** For every end of world 1 and every η > 0, its pieces eventually lie:
  - in (+,−,−), within η of the e₁ ray;
  - in (+,−,+), within η of the face {h₂ = 0}; in (+,+,−), within η of the face {h₃ = 0};
  - in (−,+,+), (−,+,−) and (−,−,+), within η of ∂U.
- *Proof.*
  - Q₁ ⊆ R₁₂ ∩ R₁₃, so both constraints apply there. Q₂ ⊆ R₁₂ only, and Q₃ ⊆ R₁₃ only.
  - In (−,+,−) a small h₂ with h₁, h₃ < 0 forces P_{K′}(h) < 0 (compactness), so the end must approach ∂U. The same
    holds for (−,−,+).
  - The mixed-plane directions (±,0,∓) violate the other edge's constraint. ∎
- So, even under (Nest_e) on both edges, ends sit at the **near-unanimous boundary (h₁ > 0) or at ∂U ∩ {h₁ < 0}**.
  T1 is world-1-correct at both, so E1.4 applies at both.
- Without (Nest_e), only E1.3(a) and its C_p-variant constrain the ends. These permit, subject to the selection:
  - ends shrinking to the T1-correct side of ∂D_{T1};
  - ends shrinking to interior rays;
  - ends at the mixed-plane directions.

  Nothing proved excludes these. Under (Nest_e) on both edges they are excluded by F2.3.

---

## 2. Task 2: protection at ∂U (the auditor's D2′)

### 2.1 E1.4 at ∂U

**PROVED** (F2.1 + E1.4). Let a protected world i have countably many ends, each eventually inside a collar of
∂U ∩ {h_i < 0}. Then:
- for every admissible integrable ν, the reweighting ν′ of E1.4 is admissible;
- its Bayes models are world-i-correct deep in every end;
- so no dominator comparison into B^{ν′}_t is end-positive.

No hypothesis on the other worlds is needed. By E1.1(b), what M0closed needs unendorsed is therefore a **base**
comparison of world i, or a comparison at another world. Placing the protection at ∂U does **not** make it visible.

If the protection sat at ∂U ∩ {h_i > 0}, T1 would err there at world i. That location is excluded by E1.3(a) under
its hypotheses, and by F2.3 under (Nest_e).

### 2.2 E1.5 at ∂U

**PROVED (by inspection of §1.3).** E1.5 is location-free. So a three-world cover with ∂U protection is excluded by
E1.5 **iff** its worlds meet E1.5's hypotheses:
- every world is end-protected with countably many ends;
- there are integrable densities with (b) and (h) **jointly**.

**Nothing proved shows that a three-world installation of D2 (at ∂U or anywhere) meets them.** D2.C is not constructed,
and E1.6 is two-world.

### 2.3 Base alone vs base + generators

**Prop. F2.4 (PROVED). In D2, every σ-finite endorser of world 1 is infinite near an interior ray of U.**

*Statement.*
- Setting: the system of Theorem D2.1, with any design.
- Let ν = gλ on M, with g measurable and 0 < g < ∞ a.e., and suppose ν endorses every relevant world-1 comparison in
  [0, ∞]: ν(c_b) ≤ ν(E₁Y) whenever C_b ⪯₁ Y and Y is regular.
- Then ν(V ∩ M) = ∞ for every neighbourhood V of every point (r, 0), r > 0. Each such point lies in the interior of U.

*Proof.*
- **(A) ν(c_b) < ∞ for every b < 1.**
  - Suppose ν(c_b) = ∞. Let E_k := c_b ∩ {g ≤ k}, so ν(E_k) < ∞, and take A ⊆ d_b non-null with ν(A) < ∞.
  - Choose k with λ(B) ≤ λ(A), where B := c_b ∖ E_k. Note λ(B) > 0, since otherwise ν(c_b) = ν(E_k) < ∞.
  - Choose A′ ⊆ A with λ(A′) = λ(B), and let Y be the regular model with E₁Y = E_k ∪ A′.
  - Then δ = 1_{A′} − 1_B is ≥ 0 on {x ≥ b}, 0 on N₊, and has tails ≥ 0. So δ ∈ 𝒦₀, and C_b ⪯₁ Y is a relevant
    comparison.
  - Endorsement gives ∞ ≤ ν(E_k) + ν(A′) < ∞, a contradiction.
- **(B) Monotonicity.** Let x′ < x″ < 1. Then ess sup_{x<x′} g ≤ ess inf_{x>x″} g.
  - Otherwise there are c′ < c″ and non-null sets B ⊆ {x < x′, g > c″} and A ⊆ {x > x″, g < c′} with λ(A) = λ(B).
  - For b ∈ (x′, x″), the regular Y with E₁Y = (c_b ∖ B) ∪ A has δ = 1_A − 1_B ∈ 𝒦₀.
  - By (A), endorsement gives ν(B) ≤ ν(A). But ν(B) > c″λ(B) > c′λ(A) > ν(A).
- **(C) ν({x ≥ 1 − h₀}) = ∞.**
  - The generator comparisons give ν(P_γ) ≤ ν(Q_γ), using (A) and Q_γ ∩ c_a = ∅.
  - With (D4): ν(c_a) ≤ ε ν({x ≥ 1 − h₀}). Since g > 0, ν(c_a) > 0.
- **(D) Bounds by a monotone function.**
  - Put m(x) := ess sup_{x(h)<x} g. If m(x) = ∞ for some x < 1, then (B) makes g = ∞ a.e. above x. So m is finite and
    nondecreasing on (0, 1).
  - For a.e. h, m(x(h)−) ≤ g(h) ≤ m(x(h)+).
  - By (C), ∫^1 m(s+) ds = ∞.
- **(E) Conclusion.**
  - On M⁺, x → 1 as h → (1,0) direction-wise, since τ → 1.
  - Under x, λ restricted to V ∩ M has density ≥ c > 0 near s = 1: μ is rotation-invariant, and dx/dφ is bounded near
    φ = 0⁻.
  - Hence ν(V) ≥ c ∫_{s₀}^1 m(s−) ds = ∞. ∎

NUMERICS (`f2_d2_geometry.py`, α′ = 0.3, β′ = 0.6):
- x ≥ 0.99977 within angle 10⁻⁴ of (1,0);
- the near-unanimous part carries a stable 0.437 of the levels near x = 1;
- the sector density in x is ≥ 0.437 up to 1;
- ∫ 1/(1−x) over the sector grows like log.

*Consequences.*
- **Conjecture σB (write-up Conj. sigmaB, n = 2) is FALSE.** D2 has every axiom, and no locally integrable endorser
  exists.
  - The status sentence "bounded on every closed subcone of U" is **WRONG**. The far end x → 1 contains the interior
    ray (1,0), and not only a boundary ray of U.
  - D2_referee2 §3.3 has the same slip.
- **Nearby surviving target (CONJECTURE, the σ-finite form only).** Every world of a full system has a countably
  additive endorser whose density is > 0 and finite a.e.
  - D2 satisfies it, with 1/(1−x).
  - For T1 it would also need versions of E1.1 and E1.5 for shadows that are non-integrable only at ends. These are not
    proved; see §4.3.
- **No effect on E1.5.**
  - F2.4 concerns endorsers of base **and** generators. E1.5 needs an endorser of the **base** only.
  - In D2 an integrable end-heavy base endorser exists (E1.6). Its proof uses only 𝒦₀ and the monotonicity of w(x).
  - So E1.6 holds whatever the placement of the targets within {x ≥ 1 − h₀}, the ∂U part included.

**Does E1's argument need a shadow that endorses the protected world's dominator comparisons, and could that be
impossible?**
- Yes, it needs one (E1.1(c)). But under (h) those comparisons are base comparisons (E1.5 step 2), so a base endorser
  suffices. Generators never appear.
- The needed shadow is impossible only if the base has no integrable end-heavy endorser compatible with the other
  worlds. In that case E1.5 does not apply, and nothing else excludes the cover.

---

## 3. Task 3: B3 on total ("complete") worlds

| Statement | Hypotheses | Label |
|---|---|---|
| B3.1: a charge is leading iff it almost agrees | world total on subsets of M | PROVED (one referee) |
| B3.2: a total AR world adds up; under (H_U), a total world of a cover that does not add up is **not AR on M** | strict (G), (IB), (S) on M_U, any n, K′ | PROVED at the status of Thm S21 |
| some edge family at e_i is then not nested | as above | CHECKED (Savage, Thm Q36(c)) |
| B3.5 (+ Remark R2): no nontrivial cancellative **leading top level** with dense null sets, total or not; B3.6: no signature or IRWAS-type top levels; B3.7: no top level ν + κ∘S with 4 max\|κ\| < ν(M) | strict (G), (IB), (S) | PROVED (one referee) |
| **B3.C**: every total world is AR | strict (G), (IB), (S) | **CONJECTURE** (open; first test B3.C′) |
| "a world of a cover that does not add up is not total (incomplete)" | — | **only if B3.C holds** |
| a (CP-a) world adds up, so no (CP-a) world, complete in the credal-singleton sense or not, fails to add up in a cover | Cor. CPaU(b) | PROVED in a referee report (one reader), at the status of M0closed(b) |

The roundreport line "A world in a cover that does not add up must be incomplete (as reworded by the referee)" is
**WRONG as a statement of what is proved**. The referee's rewording was explicitly conditional on B3.C.

---

## 4. Task 4: corrected statements and the open route

### 4.1 Replacements (one sentence each)

- **starthere, "But it does not help T1 (E1 …)":**
  > E1 (not yet refereed; audited in F2) shows that Theorem M0closed uses only the dominator comparisons of one
  > admissible integrable shadow, and it excludes a cover of T1 only when every world is end-protected with countably
  > many ends and has an integrable density that endorses its non-end-positive relevant comparisons and is, jointly
  > with the other worlds' densities, heavy at its ends; D2's world 1 has this form in its two-world system, but no
  > result shows that a three-world installation does.
- **roundreport, "D2-type protection lives only at ends (near-unanimous limits) …":**
  > An end of a protected world i on which T1 is eventually correct at world i — automatic at ∂U ∩ {h_i < 0} (F2.1),
  > and forced elsewhere when the other two worlds endorse their comparisons out of T1 (E1.3(a)) — is invisible to a
  > suitably reweighted admissible shadow (E1.4); such ends need not be near-unanimous, and under (Nest_e) on both
  > edges they lie at the near-unanimous boundary or at ∂U ∩ {h_i < 0} (F2.3).
- **roundreport, B3 line:**
  > A total world of a cover of T1 that does not add up is not almost representable on M and has no nontrivial
  > cancellative leading top level with dense null sets (proved); that it cannot be total at all is Conjecture B3.C,
  > which is open.
- **roundreport, "Assessment … σ-finite form of N17.B′":**
  > The locally integrable σ-finite form (Conjecture σB) is false already in D2 (F2.4); the surviving target is an
  > endorser with density finite a.e., together with a σ-finite version of E1.1/E1.5, and neither is proved.
- **Exclusions for T1 on M_U, in one sentence:**
  > Every cover of T1 on M_U has a world that does not add up (M0closed(b)); such a world is not (CP-a), has no leading
  > density on one of its edge regions (B1.4), is not a glued credal world (C1), is non-AR if total (B3.2), and — by
  > E1.5, unrefereed — not every world of the cover can be an end-protected decoration with integrable, jointly
  > end-heavy base densities; nothing proved fixes where protection sits.
- **Write-up items to correct when next revised** (flagged; not edited here):
  - §8.5(f) "cannot be moved off the near-unanimous limits";
  - the §8.5(g) bullet "Its ends … sit only at near-unanimous limits";
  - the §8.5(g) clause "when the other worlds add up with integrable densities";
  - the status of Conj. sigmaB (and the conjecture itself, now refuted).

### 4.2 Is a three-world T1 cover with protection at ∂U excluded by anything proved?

**No.** Such a cover is excluded only when all its worlds meet E1.5's joint hypotheses. E1.4 (with F2.1) shows only
where the failure must be, not that it cannot occur.

### 4.3 The open positive route (precise)

A ranking on M_U with (H_U) covers T1 only if it has a world i with all of the following properties:
1. World i does not add up.
2. It has no leading density on some edge region.
3. It is not a glued credal world.
4. It is not AR if total (and not total at all, if B3.C holds).
5. For **every** admissible integrable shadow ν, on a non-null set of weights t, some kkm dominator comparison into the
   incoherent B^ν_t is unendorsed (E1.1).
   - This includes the E1.4 reweightings at every end of every end-protected world whose ends are eventually
     T1-correct, in particular every end at ∂U ∩ {h_i < 0}.
   - For those shadows, the unendorsed comparison at an end-protected world is a **base** comparison (eventually 0 at
     every end).

The route that remains open after correcting E1 is a world with D2-type protection that has either property below.
The ends may sit at near-unanimous limits or at ∂U ∩ {h_i < 0}.
- **(R-a)** Its base has **no integrable density that endorses it and is heavy at its ends relative to integrable
  endorsers of the other worlds**. This covers bases that add up only with a non-heavy density (E1.4 does not transfer
  (b)), only σ-finitely, or not at all.
- **(R-b)** It sits next to a second world that fails to add up. Then E1.3(a) and E1.5 lose their hypotheses, although
  ∂U ends remain T1-correct by F2.1.

Also not covered: protection that is not of end type, or that uses uncountably many ends.

**Nearby reachable result (CONJECTURE).** E1.1(c) and E1.5 extend to shadows with ρ_i finite a.e. and integrable off
every deep end. In E1.5's step 2 the dominator comparisons avoid the deep ends of all worlds, so their ψ-differences are
finite. What is missing is a Lyapunov-free admissibility step.

---

## 5. Files (`f2py/`, run with `python3 -I`)

- `f2_d2_geometry.py` (+ `.out`): the far end of the D2 chain (n = 2). It checks:
  - x → 1 at the interior ray (1,0) and at ∂U;
  - the near-unanimous share 0.437;
  - the sector density in x is bounded below;
  - ∫1/(1−x) grows like log near (1,0).
- `f2_ends_T1.py` (+ `.out`): the T1 instance, ε = 0.3, s = 0.9. It checks:
  - (1) T1-correctness on the ∂U collar, by sign class;
  - (2) the e₁₂ far end is ∂U ∪ {h₂ = 0}, with mixed interior directions on the plane;
  - (3) E1.4 at a ∂U end in (−,+,+): admissibility is kept, and 0 world-1 errors occur deep in the end.
