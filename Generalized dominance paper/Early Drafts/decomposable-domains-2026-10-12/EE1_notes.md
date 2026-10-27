# EE1 (round 33, BRIEF25). Strict-slack threshold closure: the process is a static fixed-point problem, the forced chains it can produce, and the four-model exchange chain that no one-step invariant controls

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full proof here, one reader (me), not refereed;
- **CHECKED**: exact finite computation (rational arithmetic, exhaustive closure), reproducible script;
- **NUMERICS**: floating point or sampling; nothing depends on it;
- **CONJECTURE**.

Scripts are in `ee1py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`.

Setting throughout: the full four-advice domain, three worlds, the patched posterior family of DD1 §1 (coherent,
injective, through T1 = C_u and the seed bases B_k = C_{q_k}), the synchronized seeds of AUDIT_CC_seeds §2,
records and composition as in X1 Lemma X1.1.2 and the transition lemma (X1 Thm X1.1.1). No assumption is added;
every extra hypothesis is a hypothesis of a stated result.

---

## 0. Outcome

**The decisive theorem is neither proved nor refuted.** I found no strict-slack assignment whose closure I can
certify, and no obstruction valid for every assignment. What this round establishes:

1. **The transfinite process is a static problem (Thms 1.2, 1.3; PROVED; toy CHECKED).**
   - The closure step is a monotone, deflationary operator Φ on threshold assignments. The process from r⁰ computes
     the greatest fixed point of Φ below r⁰. It succeeds **iff some clean fixed point lies below r⁰**.
   - Failures (F1), (F2) are absorbing, and success is **up-closed**: if r⁰ succeeds, so does every r′ ≥ r⁰.
   - Limit stages can never be where a failure first appears unless no clean fixed point lies below r⁰. In this
     setting R5 (the limit rule) is built into the closed caps.
   - Hence the decisive theorem is equivalent to: **there is one clean fixed point r\* with Σᵢ r\*ᵢ(X) < 1 for every
     nonselected X**. Equivalently, there is an **exact-budget defence map** w : models → Δ, w(C_p) = p, whose closure
     stays clean after some positive uniform slack. Choosing r⁰ "cleverly" is the same as choosing the final
     thresholds; the iteration adds nothing.
2. **Verification theorem (Thm 2.1; PROVED).** Any such r\* yields a full system:
   - strict (G), (IB), transitivity;
   - (LA); (S) with exact closed sections and competitiveness; (C); (LF);
   - T1 = C_u undominated;
   - every synchronized seed retained, so world 1 has the CC1 certificate at every scale.

   The construction is therefore complete **modulo producing r\***. Continuity of the selection is never used.
3. **The invariant, exactly (Thm 3.1; PROVED).** r is a clean fixed point iff (F2) is absent and **every record of
   the closure is r-monotone along every one of its realizations**. One-step consequences follow (§3, PROVED):
   - verdict constancy;
   - local maps ρᵗ that depend on the base only through qᵢ;
   - sub-composition ρ^{t⊔t′} ≤ ρᵗ∘ρ^{t′};
   - a local form of slack;
   - the splice rule.
4. **What no one-step invariant can control (Thm 4.1, Prop 4.2; PROVED. Example 4.3; CHECKED. Prop 4.4; NUMERICS).**
   - Require r to be monotone along every realization of every generator, even after saturation by guidance. This
     condition is **not** preserved by closure.
   - After saturation the only remaining mechanism is a **four-model exchange**. Caps from two different selected
     bases cancel on a set C where the target's advice is a third kind. The (IB) context change on C then turns
     them into a selected comparison C_s ⪯ᵢ C_z.
   - **Exchange lemma.** If z_i > s_i, every clean assignment has r_i(X) > p_i or r_i(Y) > q_i, for two explicit
     cross-splice models X, Y.
   - A 3-cell instance shows this producing (F1) while every one-step test passes.
   - Such configurations occur generically **at T1 itself** in the posterior family.
   - Additive thresholds satisfy every exchange inequality identically. Any non-additive rule for r must be designed
     against them first.
   - This is the threshold form of the audit's coupling warning and of DD3's gap C2 (transports of composites are
     not composites).
5. **The brief's suggested initial assignments fail, with explicit forced chains (§5).**
   - **Scaled pointwise defence index (1−δ)g: (F2) already at installation.** It fails for every δ compatible with
     slack, for an unbalanced two-world improvement of T1. PROVED reduction; NUMERICS instance.
   - **Additive or conjugate-additive positions: slack fails.** Lyapunov gives a nontrivial splice placed exactly
     at an endpoint. PROVED, under DD1's zero-sum hypothesis.
   - **"Veto" positions: slack fails** on mixed splices. PROVED.
   - **"Generous" positions near the strict-guidance bound: (F1)** via the splice rule. PROVED.
6. **Nearby targets (§6).**
   - **Local germ at T1.** A rule for r on cross-splices near T1 satisfying the exchange inequalities, the splice
     rule and slack. This is the first test any candidate must pass.
   - **The r-independent selected-layer closure** for the patched family, which must be clean for every
     assignment. CONJECTURE: it is clean.
   - **Exchange-cycle obstruction search.** This would be a decisive negative.

---

## 1. The closure process is a static fixed-point problem

### 1.1 Definitions

- 𝓜 is the class of all models and Σ := {C_p : p ∈ Δ} the selected models. p ↦ C_p is injective (DD1 Prop 1.1(d)).
- An **assignment** is r : 𝓜 → [0,1]³ with r(C_p) = p.
- **Generators at world i**:

  Γᵢ(r) := Wᵢ ∪ Sᵢ ∪ Kᵢ(r).
  - Wᵢ: the i-worsening records, including ι.
  - S₁: the seed records rec(B_k, X_k^A), for every k and every measurable bundle set A; S₂ = S₃ = ∅.
  - Kᵢ(r) := {rec(C_p, X) : p_i ≥ r_i(X)}: the **caps**.
- **Closure.** Aᵢ(r) is the closure of Γᵢ(r) under composition of composable records. By the transition lemma,
  X ⪯ᵢ Y :⟺ rec(X,Y) ∈ Aᵢ(r) is the least preorder with (IB) containing guidance, the seeds and the caps.
  These are the brief's "least generated relations".
- **Lowering.** For X ∉ Σ put Φ(r)ᵢ(X) := inf{p_i : rec(C_p, X) ∈ Aᵢ(r)}, and Φ(r)(C_p) := p.
- **Failure.**
  - (F1): rec(C_p, C_q) ∈ Aᵢ(r) with p_i < q_i;
  - (F2): Aᵢ(r) contains a nontrivial i-improving record.

  r is **clean** if neither occurs. It is a **fixed point** if Φ(r) = r.
- **The process.** r^{α+1} := Φ(r^α); r^λ := inf_{α<λ} r^α at limits. Stop at the first stage that fails or is
  fixed. This is the brief's process: the caps are closed by definition, so "include the endpoint" is automatic.

### 1.2 Order theory

**Lemma 1.1 (PROVED).**
- (a) **Monotone.** If r ≤ r′ pointwise, then Aᵢ(r) ⊇ Aᵢ(r′), Φ(r) ≤ Φ(r′), and Fail(r′) ⟹ Fail(r).
- (b) **Deflationary.** Φ(r) ≤ r.
- (c) **Exact sections.** At a clean fixed point, {p : rec(C_p, X) ∈ Aᵢ(r)} = {p : p_i ≥ r_i(X)} for every X and i.

*Proof.*
- (a) Kᵢ(r) ⊇ Kᵢ(r′), and closure is monotone.
- (b) The cap of X contains points p with p_i = r_i(X).
- (c) For X ∉ Σ: the forced set contains the cap, and every forced p has p_i ≥ inf = r_i(X). For X = C_q: the
  inclusion ⊇ holds by the caps, and ⊆ is the absence of (F1). ∎

**Theorem 1.2 (the process; PROVED).**
- (a) The process stops at some ordinal stage.
- (b) If it stops without failing, its terminal r^∞ is the greatest fixed point of Φ below r⁰, and it is clean.
- (c) **It succeeds iff there is a clean fixed point r\* ≤ r⁰.** In that case r^α ≥ r\* at every stage, limit stages
  included, and no stage fails.
- (d) **Up-closure.** If the process succeeds from r⁰, it succeeds from every r′ ≥ r⁰.

*Proof.*
- (a) (r^α) is non-increasing, and strictly decreasing until it stops. A strictly decreasing well-ordered family in
  [0,1]^{𝓜×3} has bounded length.
- (b) If r′ = Φ(r′) ≤ r^α, then r′ ≤ Φ(r^α) = r^{α+1}, and infima preserve this. Cleanness is checked at the terminal
  stage.
- (c), (⇐) If r^α ≥ r\*, then Φ(r^α) ≥ Φ(r\*) = r\*, and infima preserve this. Also Aᵢ(r^α) ⊆ Aᵢ(r\*), which is clean,
  so Fail(r^α) never holds.
- (c), (⇒) Take r\* := r^∞.
- (d) The clean r\* ≤ r⁰ ≤ r′ serves for r′. ∎

So **limit stages are harmless**: a failure can appear at a limit only if no clean fixed point lies below r⁰. In that
case the process fails at some stage anyway. The closedness problem behind R5 is absorbed by the closed caps.

**Theorem 1.3 (equivalent forms of the decisive theorem; PROVED).** The following are equivalent.
- **(i)** Some r⁰ with Σᵢ r⁰ᵢ(X) < 1 for all X ∉ Σ has a successful process. This is the brief's decisive theorem.
- **(ii)** There is a clean fixed point r\* with Σᵢ r\*ᵢ(X) < 1 for all X ∉ Σ.
- **(iii)** There are w : 𝓜 → Δ with w(C_p) = p and θ : 𝓜∖Σ → (0,1] such that the process from
  r⁰_θ := (w − θ𝟙/3)₊ succeeds. It then succeeds for every θ′ ≤ θ.

*Proof.*
- (i)⇒(ii): the terminal has Σ r^∞ ≤ Σ r⁰ < 1.
- (ii)⇒(iii): put w := r\* + (1 − Σr\*)𝟙/3 and θ := 1 − Σr\*. Then r⁰_θ = r\*.
- (iii)⇒(i): Σ r⁰_θ ≤ 1 − θ < 1.
- Monotonicity in θ: r⁰_{θ′} ≥ r⁰_θ, then Thm 1.2(d). ∎

*Reading.* The slack is never a resource to be spent. One may start arbitrarily close to the exact-budget face, with
every model assigned a **defence point** w(X) ∈ Δ. The assignment's content is the map w together with the robustness
of its closure under an infinitesimal uniform enlargement of all non-selected caps. The enlarged caps contain a whole
neighbourhood of w(X) at all three worlds; this is audit Lemma 3 at installation.

**Proposition 1.4 (the exact-budget limit; PROVED).** Let (iii) hold for w and every θ ≤ θ₀. Write r_θ for the
terminal of the process from r⁰_θ.
- r_θ increases as θ ↓ 0.
- r₀ := sup_θ r_θ is a clean fixed point with r₀ ≤ w, so Σ r₀ ≤ 1.
- The process from w itself succeeds, and its terminal is a clean fixed point lying above r₀.

*Proof.*
- r_θ is a fixed point below r⁰_θ ≤ r⁰_{θ′} for θ′ < θ, hence below the greatest one, r_{θ′}.
- Aᵢ(r₀) ⊆ Aᵢ(r_θ), so r₀ is clean.
- Φ(r₀) ≥ Φ(r_θ) = r_θ for all θ, so Φ(r₀) ≥ r₀. With (b), Φ(r₀) = r₀.
- w ≥ r₀, so Thm 1.2(c) applies to w. ∎

*Remarks.*
- Nothing in §§1–3 uses continuity of p ↦ C_p. Coordinate thresholds give closed sections for any injective
  selection.
- CC1 Thm 4.1 and DD2 Thm 3.3 do use continuity (CC1 Lemma 3.3).
- **CHECKED (toys).** `check_process.py` implements records, composition closure, Φ and both failure tests exactly,
  on random finite cell fragments.
  - In 9 000 two-cell instances and 300 three-cell instances, every successful run ended at a fixed point with
    exact sections. That is 150 successes in the two-cell runs; no three-cell run succeeded.
  - Every raised assignment r′ ≥ r\* again succeeded, with r\* ≤ r′_∞ ≤ r′. This was 150 out of 150.
  - Outputs: `check_process_n2.out`, `check_process_n3.out`.

---

## 2. Verification theorem

**Theorem 2.1 (PROVED).** Let r be a clean fixed point with Σᵢ rᵢ(X) < 1 for all X ∉ Σ, and put
X ⪯ᵢ Y :⟺ rec(X,Y) ∈ Aᵢ(r). Then:
- (a) **Each ⪯ᵢ is a preorder with strict (G) and (IB).**
  - Aᵢ(r) contains ι and all worsening records.
  - It is composition-closed.
  - It contains no nontrivial improving record (no (F2)).
  - The transition lemma applies.
- (b) **(S).** Sections are exactly {p : p_i ≥ rᵢ(X)} (Lemma 1.1(c)), so they are closed. Competitiveness on supp p
  holds for every p ∈ Δ because Σr ≤ 1 (DD1 Thm 2.1(c)).
- (c) **Protection and (LA).** Let X ⪯ᵢ C_p at every i.
  - Exact sections and transitivity give rᵢ(X) ≥ p_i for all i, so Σ ≥ 1 and X ∈ Σ.
  - Write X = C_q. Then q ≥ p, so q = p.
  - Hence every C_p is undominated, and in particular T1 = C_u.
- (d) **(C).** Every X ∉ Σ is strictly dominated at every world by C_{p(X)}, where p(X) := r(X) + (1 − Σr(X))𝟙/3
  (audit Lemma 3). So the undominated models are exactly Σ. A model tied with some C_p at every world equals C_p,
  by (c).
- (e) **(LF)** holds at T1 on the full domain.
- (f) **Seeds.** Every seed record is a generator, so B_k ⪯₁ X_k^A for every k and A. The bases are in C_L by (c),
  and X_k^A is regular. The four-record certificate (audit Lemma 3) therefore holds on every positive-measure
  bundle set: **no strictly positive finitely additive ladder weight endorses world 1's relevant comparisons**. ∎

So the decisive theorem is exactly the existence of r as in Thm 1.3(ii). Everything else is automatic.

---

## 3. The invariant and its one-step consequences

**Theorem 3.1 (static characterization; PROVED).** For an assignment r, the following are equivalent:
- r is a clean fixed point;
- (F2) does not occur, and for every i, every d ∈ Aᵢ(r) and every realization (X,Y) of d, rᵢ(Y) ≤ rᵢ(X).

*Proof.*
- (⇒) If X ⪯ᵢ Y and C_p ⪯ᵢ X, then C_p ⪯ᵢ Y. With exact sections, this gives rᵢ(Y) ≤ rᵢ(X).
- (⇐) Take the realization (C_p, X) of a forced record rec(C_p, X): it gives rᵢ(X) ≤ p_i. So the forced set equals
  the cap, and Φ(r) = r. The case X = C_q excludes (F1). ∎

The monotonicity is required on **all realizations of all closure records**, not only of the generators. §4 shows
the difference is real.

Fix a clean fixed point r. For a record t, let A_t := {q : C_q has t's from-advice a.e. on supp t}.

**Corollary 3.2 (local maps; PROVED).**
- (a) For q, q′ ∈ A_t, the record rec(C_q ⊕ t, C_{q′} ⊕ t) equals rec(C_q, C_{q′}), so it is accepted iff
  q_i ≥ q′_i. Hence rᵢ(C_q ⊕ t) = ρᵢᵗ(q_i) for a nondecreasing function ρᵢᵗ on the projection of A_t.
- (b) **Verdict constancy.** [q_i ≥ ρᵢᵗ(q_i)] does not depend on q ∈ A_t. The record of (C_q, C_q ⊕ t) is t itself.
- (c) **Sub-composition.** Let t, t′ have disjoint supports, with p′ ∈ A_t and p″ ∈ A_t ∩ A_{t′}. Then

  ρᵢ^{t⊔t′}(p″_i) ≤ ρᵢᵗ(p′_i) whenever p′_i ≥ ρᵢ^{t′}(p″_i).

  In particular ρ^{t⊔t′} ≤ ρᵗ∘ρ^{t′} where both sides are defined. The proof is the realized chain
  C_p ⪯ C_{p′} ⊕ t ⪯ C_{p″} ⊕ t ⊕ t′, whose second record is the cap rec(C_{p′}, C_{p″} ⊕ t′).
- (d) **Local slack.** If C_q ⊕ t ∉ Σ, then Σᵢ ρᵢᵗ(q_i) < 1 = Σ q_i. So some world accepts t from every base in
  A_t, with a strict margin.
- (e) **Splice rule.** Let s = rec(C_a, C_b) and Y_E := C_a ⊕ s|_E. Then rec(Y_E, C_b) is the cap record
  rec(C_a, Y_{E^c}). So

  rᵢ(Y_{E^c}) ≤ aᵢ ⟹ rᵢ(Y_E) ≥ bᵢ, and rᵢ(Y_{E^c}) ≤ bᵢ ⟹ rᵢ(Y_E) ≥ aᵢ.

  Together with slack, Σᵢ max(bᵢ[rᵢ(Y_{E^c}) ≤ aᵢ], aᵢ[rᵢ(Y_{E^c}) ≤ bᵢ]) < 1 for nontrivial E.
- (f) **Frontier rule.** Put w(X) := r(X) + (1 − Σr(X))𝟙/3, the defence point of Thm 1.3. Then C_{w(X)} ⪯ᵢ X at
  every world. If X ≠ C_{w(X)}, no selected C_v may agree with X a.e. on supp rec(C_{w(X)}, X). Otherwise DD1's
  model Y (C_v reset to C_{w(X)}'s advice there) has rec(Y, C_v) = rec(C_{w(X)}, X), so Y ⪯ᵢ C_v at every world.
  That contradicts Thm 2.1(c). This is DD1 Lemma 3.2(b) under slack.

*Proofs.* Each is a single realized chain of one or two caps followed by Thm 3.1. ∎

There is no reverse inequality to (c) in general. The closure only lowers. Lower bounds on thresholds come only from
the selected layer, through (F1), and from strict guidance, through (F2). So any successful r is free to be strictly
**sub-compositional**. This is the room the audit's slack opens, and it is exactly what Prop 5.3 shows additive
positions lack.

---

## 4. What one-step monotonicity misses: the four-model exchange

**Definition 4.0.** The **saturated generators** are Γᵢ^sat(r) := {γ∘g∘γ′ : g ∈ Γᵢ(r), γ and γ′ i-worsening, composable}.
Pointwise, a saturated cap may replace an arrow a→b by x→z with rk(x) ≤ rk(a) and rk(z) ≥ rk(b). Where g improves,
it may also delete the arrow, i.e. replace it by ι, which leaves the context there free.

r is **saturated one-step monotone (SOM)** at world i if rᵢ is non-increasing along every realization of every member
of Γᵢ^sat(r). This is a condition on single generators, with no chains. Every candidate "explicit invariant on
(relations, thresholds)" built from r alone has this form.

**Theorem 4.1 (localization; PROVED).** Let r be SOM at world i. Let d ∈ Aᵢ(r) and let (X,Y) be a realization of d
with rᵢ(Y) > rᵢ(X), for instance an (F1) or a cap-exactness violation. Then every derivation d = e₁∘⋯∘e_m with
e_j ∈ Γᵢ(r) has a non-null set F ⊆ {d = ι} of problems such that, at each f ∈ F:
- the arrows of the derivation at f form a closed loop x₀ → ⋯ → x₀ containing **at least two distinct
  non-guidance steps** (caps or seeds);
- X(f) ≠ x₀.

*Proof.*
1. At problems where d is nontrivial, the derivation's own intermediate advice factorizes any realization. The same
   holds where d = ι and either no step acts or X(f) = x₀(f).
2. Let F₀ be the set where d = ι, some step acts, and X(f) ≠ x₀(f). A loop made only of guidance arrows cannot
   close, because ranks strictly increase along nontrivial worsening arrows.
3. On the part of F₀ where exactly one non-guidance step e_j acts, the guidance arrows at those problems commute past
   every other step, which is ι there.
4. So they can be merged into γ|∘e_j∘γ′|. This element lies in Γᵢ^sat and is ι at those problems.
5. The modified derivation has no step there, so the realization factorizes there.
6. If the remaining set (loops with ≥ 2 non-guidance steps) were null, (X,Y) would factorize a.e. along a derivation
   from Γᵢ^sat. SOM would then give rᵢ(Y) ≤ rᵢ(X). The loop patterns are finite in number, so all sets involved are
   measurable. ∎

The minimal such configuration is the following.

**Proposition 4.2 (four-model exchange lemma; PROVED).** Let C_s, C_z, C_p, C_q be selected, i a world. Let D₁, D₂, C
be disjoint measurable sets of problems with:
- Δ(s,z) := {C_s ≠ C_z} = D₁ ⊔ D₂;
- C_p = C_s on D₁ and C_q = C_s on D₂;
- C_s = C_z and C_p ≠ C_q on C.

Put:
- X := C_p, changed to C_z's advice on D₁ and to C_q's advice on C;
- Y := C_q, changed to C_p's advice on C and to C_z's advice on D₂.

Then:
- (a) rec(C_p, X) = (D₁: s→z) ⊔ (C: p→q) and rec(C_q, Y) = (C: q→p) ⊔ (D₂: s→z). They are composable, in either
  order, and both composites equal rec(C_s, C_z). So **if p_i ≥ rᵢ(X) and q_i ≥ rᵢ(Y), then C_s ⪯ᵢ C_z.** Every clean
  assignment therefore satisfies

  z_i > s_i ⟹ rᵢ(X) > p_i or rᵢ(Y) > q_i.     (EX)
- (b) If C_s = C_p a.e. on C (resp. C_s = C_q), the realization (C_s, C_z) factorizes in the first (resp. second)
  order. Then SOM alone already forces rᵢ(C_z) ≤ rᵢ(C_s), and the chain is visible to one-step tests. On the part of
  C where C_s, C_p, C_q give **three different kinds of advice**, it factorizes in neither order. That is the
  genuinely non-local case of Thm 4.1.
- (c) **No single exchange is forced by guidance.** Suppose guidance forced both caps, i.e. X were pointwise
  i-worse than C_p and Y pointwise i-worse than C_q. Then both p→q and q→p would have to worsen world i on the
  non-null set C. That is impossible.
- (d) **Additive thresholds satisfy (EX) identically.** With Lᵢ additive, the exchange identity is
  Lᵢ(X) + Lᵢ(Y) = Lᵢ(C_p) + Lᵢ(C_q) + Lᵢ(C_z) − Lᵢ(C_s). Both caps, Lᵢ(C_p) ≤ Lᵢ(X) and Lᵢ(C_q) ≤ Lᵢ(Y), would then
  give Lᵢ(C_s) ≤ Lᵢ(C_z).

*Proof.* (a) is checked pointwise. Off D₁ ∪ D₂ ∪ C both records are ι. On C the arrows are p→q and q→p, or the
reverse, so they cancel. On D₁ and D₂ the from-advice is C_s's by hypothesis. (b) and (c) are as stated. ∎

**Example 4.3 (CHECKED, `verify_example.py`, `two_cap_F1.py`).** Take three cells f, g, h with sign patterns
(world 1, 2, 3) f: (−,+,−), g: (+,+,−), h: (+,−,+). Advice is listed in the order (f, g, h).

| model | advice | index |
|---|---|---|
| C_p | (−, −, 0) | (1/3, 0, 2/3) |
| C_q | (+, +, +) | (5/12, 7/12, 0) |
| C_s | (0, −, +) | (1/12, 1/6, 3/4) |
| C_z | (0, +, −) | (1/4, 2/3, 1/12) |

- **The exchange.** C = {f}, D₁ = {g}, D₂ = {h}. At f, C_s, C_p, C_q give three different kinds of advice.
  X = (+, +, 0) and Y = (−, +, −).
- **Thresholds.** The SOM process, i.e. lowering along realizations of saturated generators, starts from r⁰ with
  r₁(X) = p₁, r₁(Y) = q₁ and r = 2 elsewhere off Σ (no caps). It terminates without failure. The toys impose no
  slack; they test the closure mechanism only.
  - r is SOM at every world.
  - Both rec(C_p, X) and rec(C_q, Y) are caps at world 1.
  - Their composite is rec(C_s, C_z), with s₁ = 1/12 < z₁ = 1/4. This is **(F1)**.
- **The closure process.** From the same r⁰ it fails with (F1).
- **Frequency.** In planted searches, 13 of 105 consistent four-model instances behave like this
  (`two_cap_F1.out`, two seeds). In a variant where the target Z is not selected (`two_cap_search2.py`), 24 of 152
  instances pass the unsaturated one-step test but are not cap-exact. There the closure process merely lowers further
  and succeeds.
- **Random instances.** On 9 300 unplanted random instances, one-step and closure processes always agreed. The
  mechanism needs the planted geometry.

**Proposition 4.4 (the exchange occurs at T1; NUMERICS, `tce_posterior.py`, `tce_verify.py`).** In the posterior
family, take:
- s = u, so C_s = T1;
- z = (0.3451, 0.3253, 0.3296), so z₁ > 1/3;
- p = (0.506, 0.383, 0.111) and q = (0.288, 0.355, 0.357).

All four lie outside the DD1 bumps: q is at distance 0.0288 from the nearest centre, and the radius is 0.025
(`bump_check.out`). So they are also patched-family models. On 10⁶ Gaussian directions:
- Δ(u,z) splits as D₁ := Δ(u,z) ∩ {C_u = C_p} (2 829 hits) and D₂ (10 961 hits), with no violation of C_u ∈ {C_p, C_q}
  on Δ(u,z);
- the three-advice set C := {C_u = C_z, with C_u, C_p, C_q pairwise different} has 3 183 hits.

Four further configurations were found among 20 000 random trials (`tce_posterior.out`). So **(EX) binds at T1**. Every
successful system must place one of these two cross-splices strictly above its base at world 1:
- C_p with Δ(u,z)∩{C_u=C_p} moved to z and C moved to q;
- C_q with C moved to p and the rest of Δ(u,z) moved to z.

*Reading.*
- The brief asks for "an explicit invariant on the evolving (relations, thresholds) pair". Thms 3.1 and 4.1 say what
  such an invariant must be: monotonicity of r along **all** closure records.
- The only part not checkable one generator at a time is the family of exchange inequalities (EX), and their
  multi-cap analogues, over quadruples of selected models.
- They are conic: all sets involved are cones. So the bounded seed cells cannot take part except through the
  thresholds of non-selected models. This is consistent with DD2's lesson that coherent models are cones.
- They are the threshold form of the coupling warning (AUDIT_CC_plan §3). Changing the context on a cancellation set
  is the rearrangement that warning forbids, here aimed at a selected target.

---

## 5. Natural initial assignments and their forced chains

By Thm 1.3, an initial assignment matters only through the clean fixed points below it. Each item below tests a
candidate for the final r, or for the defence map w.

### 5.1 Windows (PROVED)

Put:
- gᵢ(X) := inf{p_i : C_p pointwise weakly i-better than X}, the guidance cap;
- hᵢ(X) := sup{p_i : X pointwise strictly i-better than C_p}, the strict-guidance bound.

Then every clean fixed point has hᵢ(X) < rᵢ(X) ≤ gᵢ(X).
- The upper bound is a forced coordinate.
- If rᵢ(X) ≤ hᵢ(X), the cap installs C_p ⪯ᵢ X with X strictly better. That is (F2).
- Joint feasibility with slack is Σᵢ hᵢ(X) < 1. This is DD1's (NC), and it holds for the posterior family
  (DD1 Prop 2.5).

### 5.2 The scaled defence index fails at installation

**Proposition 5.2.** Let X := C_u ⊕ t, where t changes silence to "accept" on a small bounded neighbourhood D of a
problem h with signs (+,+,−) just outside facet F₃. Then t improves worlds 1 and 2 and worsens world 3. The following
are PROVED:
- **(a)** h₁(X) = h₂(X) = 1/3 and g₃(X) = 1/3.
  - A model pointwise comparable with X differs from C_u, in the opposite direction, only on a cone contained in D.
    Such a cone is null (DD1 Lemma 2.7).
  - So the comparison passes to C_u, and the selected-layer thresholds apply.
- **(b)** Write Δⱼ := gⱼ(X) − 1/3. If Δ₂ ≥ 2Δ₁, no δ makes r = (1−δ)g both strictly competitive (Σr < 1) and free of
  (F2). The two requirements are 1−δ > 1/(1+3Δ₁) and 1−δ < 1/(1+Δ₁+Δ₂). So **the brief's suggested index
  produces (F2) already at installation**: it installs C_u ⪯₁ X although X is strictly 1-better.

**NUMERICS** (`defence_index.py`, grid 1/1200, fibre criterion of DD1 Lemma 2.2). For h = (1, 0.02, −0.4552):
- v·h = (0.432, 0.138, −0.005);
- g₁ ≈ 0.3383 and g₂ ≈ 0.5033.

So Δ₂/Δ₁ ≈ 34 ≫ 2. The same failure holds for h₂/h₁ ∈ {0.05, 0.1, 0.3}, and not for the balanced h = (1, 1, −0.89).

Repairing it needs world-dependent placement inside the windows of §5.1. That is admissible, but then the placement
must also pass §3 and §4.

### 5.3 Additive and conjugate-additive positions (PROVED)

**Proposition 5.3.** Let (a,b) be a selected pair with S := supp rec(C_a, C_b). Suppose there are:
- increasing bijections Fᵢ;
- a non-atomic vector measure m on S,

such that rᵢ(Y_E) = Fᵢ⁻¹(Fᵢ(aᵢ) + mᵢ(E)) for all E ⊆ S. Suppose also that Σ_k λ_k m(E_k) = 0 for some disjoint
non-null E_k ⊆ S and λ_k > 0; this is DD1's zero-sum condition. Then strict slack fails.

*Proof.*
- Lyapunov gives F_k ⊆ E_k with m(F_k) = (λ_k/max λ)m(E_k). The union E is non-null and has m(E) = 0.
- So r(Y_E) = a and Σ r(Y_E) = 1.
- Y_E ≠ C_a. If Y_E were some C_v, then v = r(C_v) = a, contradicting injectivity. Also E ≠ S, since m(S) ≠ 0.
- So Y_E is a nonselected model with Σ r(Y_E) = 1, contradicting strict slack. ∎

This is DD1 Cor 3.3(b) for any reparametrization and under slack. It is why Cor 3.2(c) must be **strict** somewhere:
path-additive (flow-type) splice positions are excluded.

### 5.4 Two non-additive extremes (PROVED)

**Veto positions.** At a world where b improves on a, a forward splice piece is defended only if it contains no
improving problems; dually for backward pieces. Let the move a→b improve worlds 1 and 2 and worsen world 3, and let E
contain non-null parts of both I₁ ∩ I₃ and I₂ ∩ I₃. Here Iⱼ is the set where the move improves world j. Then:
- **world 1:** E meets I₁, so a does not defend Y_E;
- **world 2:** E meets I₂, so a does not defend Y_E;
- **world 3:** E ⊆ I₃, so the forward piece contains no world-3 loss, and a does not defend Y_E.

Hence r(Y_E) > a coordinatewise and Σ > 1. This is the threshold form of the audit's veto warning.

**Generous positions.** Suppose rᵢ(Y_E) is just above hᵢ(Y_E) < min(aᵢ, bᵢ) for complementary splices E and E^c, at
a world with aᵢ < bᵢ. Then rᵢ(Y_{E^c}) ≤ aᵢ, while the splice rule needs rᵢ(Y_E) ≥ bᵢ. That is (F1).

So a working rule must allow compensation, which veto positions forbid, and must not hug the guidance bounds. By 5.3 it
must also be non-additive, and by 4.2 it must satisfy (EX).

---

## 6. Status of the decisive theorem, and the nearby targets

**Where it stands.** By Thms 1.3 and 2.1, the decisive theorem is equivalent to one static existence statement: find r
with r(C_p) = p, strict slack, no (F2), and r-monotonicity along every realization of every closure record.

The necessary conditions identified are:
- the windows (h, g] of §5.1;
- verdict constancy, sub-composition and the splice rule (§3);
- **the exchange inequalities (EX)**, together with their multi-cap analogues (§4).

The first three are one-step conditions. (EX) is the first non-local family, and it is generic at T1. Additive r
satisfies all of them but violates slack at T1, by the imported additive exclusion. Every non-additive rule tested
here fails one of them (§5).

Nothing found excludes a non-additive r. Nor is there a construction.

**Nearby targets.** These are offered in the spirit of the brief: each is reachable, and each bears directly on the
decisive theorem.
- **(N1) The local germ at T1.** Construct r on the cross-splices of selected models near u satisfying all of the
  following simultaneously, near T1 only:
  - the windows of §5.1;
  - the splice rule;
  - (EX) for every quadruple;
  - strict slack.

  Proposition 4.4 gives explicit quadruples.
  - **What (EX) says.** Whenever a selected move s→z gains at world i, at least one of its two exchange pieces must be
    valued as a strict world-i gain over its own base. The pieces are X, a modification of C_p, and Y, a
    modification of C_q.
  - **What the rule must therefore do.** It must attribute the gain of every selected move to its pieces consistently
    across different bases. This is the multi-base form of the splice rule.
  - **Placing by nearest selected model fails.** Placing each cross-splice just below the index of the selected model
    it differs from least violates (EX) when both pieces are small. Then r(X) ≈ p and r(Y) ≈ q, both minus the slack.
  - **Additive attribution passes automatically**, by 4.2(d), but fails slack (Prop 5.3).

  The sharpest open sub-question is whether a non-additive attribution can meet (EX), its multi-cap analogues
  (Thm 4.1) and slack together. **CONJECTURE (40/60): it cannot without becoming conjugate-additive on splices**,
  which Prop 5.3 forbids.
- **(N2) The r-independent part.** The selected-layer closure, of guidance, seeds and the selected caps
  rec(C_p, C_q) with p_i ≥ q_i, must be clean for **every** assignment. DD1 Prop 2.6 handles commuting squares. Its
  cross-base exchanges (Prop 4.2 with X, Y selected) need six cones to align. **CONJECTURE: the patched family's
  selected-layer closure is clean.** A counterexample would be an obstruction for every initial assignment. That is
  the only kind of r-independent forced chain this analysis leaves.
- **(N3) An exchange-cycle obstruction.** Seek finitely many quadruples at T1 whose (EX) disjunctions, combined with
  slack for the shared cross-splices and the windows, are jointly unsatisfiable. This is a finite SAT/LP once the
  sets are discretized. If UNSAT, it is a decisive negative, with the forced chain identified. I expect finite
  fragments to be satisfiable, because the additive exclusion is a continuum phenomenon; so this has low prior.

---

## 7. Status table

| Item | Statement | Label |
|---|---|---|
| 1.1–1.2 | Φ monotone and deflationary; process = greatest fixed point below r⁰; succeeds iff a clean fixed point lies below; failures absorbing; success up-closed; limit stages harmless | PROVED; toys CHECKED |
| 1.3 | decisive theorem ⟺ clean fixed point with strict slack ⟺ exact-budget defence map w robust to positive slack | PROVED |
| 1.4 | exact-budget limit r₀: clean fixed point with Σ ≤ 1 | PROVED |
| 2.1 | any such r gives a full system: all axioms, T1 undominated, seeds and certificate retained | PROVED |
| 3.1 | clean fixed point ⟺ no (F2) and r monotone along all realizations of all closure records | PROVED |
| 3.2 | local maps, verdict constancy, sub-composition, local slack, splice rule, frontier rule | PROVED |
| 4.1 | under SOM, every violation contains a multi-cap loop with a context change | PROVED |
| 4.2 | four-model exchange lemma (EX); additive identity; not forced by guidance | PROVED |
| 4.3 | SOM-clean thresholds whose closure has (F1) | CHECKED (exact) |
| 4.4 | exchange configurations through T1 in the posterior/patched family | NUMERICS |
| 5.1 | windows h < r ≤ g | PROVED |
| 5.2 | scaled defence index gives (F2) at installation for unbalanced moves | PROVED (reduction); NUMERICS (instance) |
| 5.3 | conjugate-additive splice positions violate strict slack | PROVED (under zero-sum) |
| 5.4 | veto positions violate slack; generous positions give (F1) | PROVED |
| N1 | a non-additive gain attribution meets (EX), its multi-cap analogues and slack | CONJECTURE (40/60 against) |
| N2 | patched family's selected-layer closure is clean | CONJECTURE |
| — | decisive theorem | **open**: neither proved nor refuted |
| — | T1 cover | **not obtained** |

## 8. Files (`ee1py/`)

- `toy.py`: exact finite record calculus (four advices, records, composition, closure, caps, Φ, the process,
  (F1)/(F2) tests, guidance saturation, the SOM process).
- `check_process.py` → `check_process_n2.out`, `check_process_n3.out`: Thms 1.2–1.3 on random toys (CHECKED). The
  one-step and closure processes agree on unplanted instances.
- `two_cap_search.py`: helpers, and a planted search whose composite is realizable from a selected base. That
  composite is itself a cap (absorbed case); no gap was found, as expected.
- `two_cap_search2.py` → `two_cap_search2.out`: planted cross-base composites with a non-selected target. They pass
  the unsaturated one-step test but are not cap-exact; the closure only lowers further.
- `two_cap_F1.py` → `two_cap_F1.out`: planted four-model exchanges. 13 of 105 are SOM-clean but give (F1).
- `verify_example.py` → `verify_example.out`: Example 4.3, recomputed independently of the closure code, with the SOM
  check.
- `tce_posterior.py` → `tce_posterior.out`, `tce_verify.py` → `tce_verify.out`: Prop 4.4 (NUMERICS).
- `defence_index.py` → `defence_index.out`: Prop 5.2 instance (NUMERICS).
- `bump_check.py` → `bump_check.out`: the indices of Prop 4.4 lie outside the DD1 bumps.
