# PP52. The selective branch: own-argmax gates, the KKM test, and what selectivity can and cannot buy

23 October 2026. Task PP52 of Brief 52. One reader (me); not refereed. Includes the coordinator's mid-task request: test the rule against PP51's kink triple.

**Labels.** PROVED: complete argument here (or a cited refereed result, named). CHECKED: exact rational computation in `r9/PP52_py/` (LPs only propose; Fractions verify feasible points and Farkas certificates). NUMERICS: floating-point search; no proof rests on it. CONJECTURE / OPEN: as stated. Worlds are 1, 2, 3 (the scripts index them 0, 1, 2 internally and print 1, 2, 3).

**Inputs.** BRIEF52; AUDIT_round52, AUDIT_posterior_pairs, AUDIT_round52_answers §5 (binding); PP42 (TWG, Lemma 3.0, Thms 3.1–3.2, Lemma 3.3, Prop 3.5); REFEREE_round50 (Thm R1, Lemma S, CG2 necessity without the agreement region); PP45 (Lemmas 2.1–2.3, Thm 3.1); PP46 (Lemma A0, Thms A–B, Prop C); PP47 (Lemma 1.3, Thms 2.5, 2.7, 4.1); LEAD_selection_count; AUDIT_completion; REFEREE_PP32 (ℓ^T, Q4.2); PP12 (Thm E); DESIGN_MEMO §5–6, §8.11, §8.20; and, by relay, PP51 (Thm 5.1, the kink triple). No axiom is added; extra hypotheses are named where they enter.

---

## 0. Verdict

1. **A fully specified selective rule exists, and it reduces every axiom to three field hypotheses, (PX), shape certificates and L¹-continuity (§2–3, PROVED).** Whether fields meeting them exist is the open question tested in §§4–7. The rule is *own-argmax* (OA). Every gated realiser of a record speaks; each speaks only at the world(s) where its own role-weighted gate value is largest, with ties all accepted. The role weights θ^b may be the index itself, θ^b = b.
   - **Designated set.** The designated set is all gated realisers. It depends only on the record. A record with no gated realiser is judged by guidance alone, and it carries no defence obligation.
   - **Changing realisers.** Fixed-rival sections are closed even when the realiser changes along a sequence, and closedness reaches up to the boundary (Thm 3.5).
   - **Defence.** Every model is defended on its own support against every measurable rival, through its own gate (Thm 3.1).
   - **Protection.** Undominatedness, absence of all-world ties and direct (C) follow from one pair condition, (PX) (Thm 3.3).
   - **(TC).** (TC) holds for all common-context copies under triangle-local shape certificates. These are "tilted" versions of CG2/CG3 (Thm 3.4).
   - **Room for dominators.** KKM then supplies a strict selected dominator for every rival (Thm 3.6).
   - **Single winner.** A single designated winner is worse: its sections need an upper-hemicontinuity property that the realiser sets violate (Prop 2.1).
2. **Selectivity does not escape the combined-cut obstruction. That obstruction never depended on universal acceptance (Thm 4.1, PROVED; CHECKED).** The real source is a KKM argument inside one gate's own record space.
   - **Setting.** Let N be any model whose own-gate verdicts on its records are closed cones in its additive gate values; this covers union, OA and every closed selective rule. Suppose some coherent M beats N at all worlds but k, on some piece, for each k = 1, 2, 3.
   - **Conclusion.** Then some bounded modification of M is no worse than M at all three worlds. So M is dominated, or all-world tied with an incoherent model.
   - **Instance.** With N = AB (the combined cut) and M = T, this is PP46 Thm A / Prop C and PP45 Thm 3.1, now without CG2, without (TC) and without uniqueness of T's Bayes optimum.
   - **Rule-independence.** The proof uses only strict (G), N's defence and continuity of verdicts along mass paths. That is the same continuity that section proofs use.
3. **Own-argmax selectivity does not escape the pair type test either (Thm 4.3, PROVED; CHECKED).** The only type-test failures not covered by item 2 are of one kind (E1). For E1, (PX) fails at some world for every field. Outside a degenerate tie case, (TC) fails too.
   - So at the level of *which pairs can be gated together*, OA can do exactly what the zero-accepting union can do: pass the PP45 type test.
4. **The posterior family passes both pair tests on the whole closed simplex (Prop 5.1, Cor 5.2, PROVED; CHECKED).** The pair ordering extends to boundary indices. For interior pairs, the single types missing are exactly those at argmin D and argmax D, with D = log(a/b).
   - **This is what D does under selectivity.** It is the certificate that Theorem 4.1 can never bite, not a role-assignment rule.
   - **Role-restricted acceptance via D** cannot be defined for incoherent rivals without choosing an explanation (Prop 2.2). OA's self-referential role is the disagreement-based replacement that the audit asked for.
5. **What OA does buy: strictly more field systems, though not, by itself, freedom from global witnesses (§6; CHECKED).**
   - **(a) Strictly larger design space.** For T and a single cap, a field system was found in which CG2 fails at worlds 2 and 3, so the union rule fails (TC), while every OA check passes exactly.
   - **(b) Witnesses persist.** Every additive witness of the union rule remains a witness of OA (monotonicity, PROVED). The example in (a) still has an additive witness at every world. Selectivity cannot remove global prices. It can only enlarge the space of fields among which witness-free systems must be sought.
6. **The kink triple (coordinator's request; §7).**
   - **(i) Designated realisers cannot defend ungated selected models (PROVED).** Every selected non-vertex model must carry its own gate in any realiser-gated rule (PP45 Lemma 2.3(b) generalises verbatim). So PP51's escape (a), "gate a kink-free subfamily and defend the ungated remainder by designated realisers", is not available: under index = likelihood all three kink models must be gated.
   - **(ii) OA does not escape the kink either, on the evidence (NUMERICS; CONJECTURE).** The rule no longer forces PP51's closed triple test. But (PX) for the two pairs through T, (u, B) and (u, D), was never achieved in a search over OA certificate space.
     - Every nearest miss leaves exactly one infeasible cell, and it is always one of PP51's two certificate cells (T answering alone at class M₁, "above" or "below").
     - The union-dual control stalls at the same cells.
     - The nearest-miss design built from a score-1 certificate has exact co-active two-cycles and exact (TC) violations (CHECKED).
     - The obstruction needs only the two pairs through T; the pair (B, D) plays no part.
   - **(iii) Designation does not rescue it (Prop 7.3, PROVED).** A strict co-activity on records with several realisers reappears on nearby records with a single realiser. So designating one speaker on shared records cannot remove it.
   - **(iv) Consequence.** For the posterior family near T, PP50's "selective exit" is closed for every closed, realiser-gated, argmax-type rule. This rests on Conjecture 7.2. What remains is rules whose verdicts are not closed along mass paths (they lose Lemma S), or a change of family to half-plane answer regions, where OA's extra room (Prop 6.1) applies.

| Item | Result | Label |
|---|---|---|
| OA rule; designation = all gated realisers; ties accepted | Def 2.0 | — |
| Winner-take-all designation needs upper hemicontinuity | Prop 2.1 | PROVED |
| D-roles undefined for incoherent rivals; realiser-invariant roles = one field | Prop 2.2, Rem 2.3 | PROVED |
| OA ⊆ union (R0): inclusion, embedding of strict-CG2 designs, witness monotonicity | Prop 2.4 | PROVED |
| Defence on every support, incl. boundary | Thm 3.1 | PROVED |
| Reverse refusal; protection; direct (C) | Lemma 3.2, Thm 3.3 | PROVED (under (PX)) |
| (TC) via triangle-local tilted certificates; padding | Thm 3.4, Rem 3.4′ | PROVED |
| Closed sections with changing realisers, edge and vertex limits | Thm 3.5 | PROVED (under (S1), (S2′)) |
| Consolidated reduction with KKM dominators | Thm 3.6 | PROVED |
| KKM test (rule-independent) | Thm 4.1, Cor 4.2 | PROVED; CHECKED |
| Argmax selectivity keeps the type test | Thm 4.3, Cor 4.4 | PROVED; CHECKED |
| Posterior pairs pass both tests on the closed simplex | Prop 5.1, Cor 5.2 | PROVED; CHECKED |
| OA accepts fields the union rejects; still witnessed | Prop 6.1 | CHECKED |
| Ungated selected models are indefensible | Prop 7.1 | PROVED |
| Kink triple: (PX) through T fails under OA in every design found | §7.2 | NUMERICS (search); CHECKED (near-miss verdicts); CONJECTURE (all designs) |
| Designation on shared records cannot remove a strict co-activity | Prop 7.3 | PROVED |
| Non-closed verdicts as the last selective lever | §7.3 | OPEN |

---

## 1. Setting and the proposal–selection framework

Brief 52's setting:
- three worlds; Gaussian μ; the full four-advice domain; ranks 0 < 1 < 2 < 3;
- posterior selection a ↦ C_a = D_{M_a} on the closed simplex Δ, with C_u = T and C_{e_i} = V_i.

A **record** is r = (D, x → y). Its **realisers** are P(r) := {b ∈ Δ : C_b = x a.e. on D}. P(r) depends only on r, and it is closed in Δ, because b ↦ C_b is continuous in measure (PP12 §1; AUDIT_posterior_pairs §1).

A **gate** at b consists of three things:
- a strictly guiding integrable field ℓ^b;
- a Bayes weight λ_b with supp λ_b ⊆ supp b, such that C_b is the a.e.-unique λ_b-Bayes model of ℓ^b;
- role weights θ^b ∈ R³_{≥0}, with θ^b_w > 0 on supp λ_b and θ^b_w = 0 off supp b.

The gate values are Φ^b_w(r) := ∫_D [ℓ^b_w(g, y) − ℓ^b_w(g, x)] dμ, and the **role vector** is R^b(r) := θ^b ⊙ Φ^b(r).

**Defence reduces to a hitting condition (BRIEF47, PROVED there).** (S)'s defence clause says: for every record r and every p ∈ P(r), some accepted world lies in supp p. A *proposal–selection rule* lets gates propose and lets a record-based selector decide which proposals are accepted. The brief's question is which selectors keep the hitting condition while weakening (TC)'s demands.

---

## 2. The rule, and the two candidate rules of the audit

**Definition 2.0 (OA, own-argmax gates).** Accept r at world w iff either:
- r is a weak w-worsening (guidance); or
- some gated b ∈ P(r) has R^b_w(r) = max_v R^b_v(r).

Vertices carry the trivial gate θ = e_i; on V_i's records it coincides with guidance at i.

- **Ties.** Every maximiser is accepted. This is the closed convention, and Thm 3.5 needs it.
- **Records with no gated realiser** are judged by guidance only. They carry no defence obligation.
- **(IB).** P(r) and every R^b(r) depend only on r. So all common-context copies share their verdicts.
- **Strict (G).** For a nontrivial record realised by b, max_v R^b_v > 0, by own-Bayes and θ^b > 0 on supp λ_b. A pure w-improvement has R^b_w ≤ 0 (strictly negative when θ^b_w > 0), so w is never a maximiser and the record is refused at w.
- **Canonical role weights.** θ^b := b. Each posterior model speaks at the world where its likelihood-weighted gate value is largest. The Bayes weight λ_b remains free, as the audit requires; λ_a = a is not imposed.

**(i) Designated realiser: why the designated set must be all of P(r).**

**Proposition 2.1 (PROVED).** Fix a rival X, a world w, and indices p_n → p. Write r_n = rec(C_{p_n}, X) and r = rec(C_p, X).
- (a) Limits of realisers of r_n realise r. This is Lemma S, step 2.
- (b) P(r) can be strictly larger than the set of these limits. This happens whenever μ{C_p ≠ X} < liminf μ{C_{p_n} ≠ X}.
- (c) Consequently, if acceptance must pass through a designated subset B*(r) ⊆ P(r), closedness of A_w(X) at p needs the following: whenever r_n is accepted through b_n ∈ B*(r_n), with b_n → b, the record r is accepted at w through B*(r). With B* = P(r) this is automatic, because b ∈ P(r).

For a winner-take-all B* (for example, the realiser nearest u), it fails generically. Take X = C_q[E ↦ y] with E small, and p_n → q. Then P(r_n) shrinks to {q}, but P(r) contains every model agreeing with C_q on E, and the winner over P(r) need not be q.

So the audit's suggestion of a designated *set* is right, and the set that needs no extra hypothesis is P(r) itself. Its cost is that every realiser's proposals count, which is what §3 handles.

Defence never needs designation. Every gated realiser defends itself (Thm 3.1). "A model's defence may come from another model's gate" is allowed, but it is never required.

**(ii) Role-restricted acceptance via D = log(a/b).**

**Proposition 2.2 (PROVED).** A role rule that reads the world from D(b, c) = log(b/c), for b ∈ P(r) and c ∈ P(r⁻¹), assigns no role when P(r⁻¹) = ∅.
- For a bounded modification X of a selected C_p, P(rec(X, C_p)) = ∅. Coherent models agreeing on a non-null set off a bounded set agree a.e. (AUDIT_completion §1).
- Every defence against such rivals therefore needs a role that does not refer to a second coherent model.
- Choosing a "nearest coherent explanation" c is a designation on P(r⁻¹), and Prop 2.1 applies to it.

OA's role, the argmax of R^b(r), is computed from the record and the realiser alone. It covers every measurable rival. §5 shows what D does instead: it certifies that the pair-level obstructions of §4 never apply to posterior pairs.

**Remark 2.3 (realiser-invariant roles collapse to one field; PROVED).** Suppose every two realisers of every record had the same role worlds. Then by Lyapunov the pointwise role increments θ^b⊙δ^b would be positively proportional to one field L on each agreement region, and C_b would be the (λ_b/θ^b)-Bayes model of L there. That is a single-field realisation. So realiser dependence of the roles is necessary, and the union over realisers in Def 2.0 is the price of it.

**Proposition 2.4 (OA versus the zero-accepting union; PROVED).** Fix the fields.
- (a) Every OA acceptance is a union (R0) acceptance.
- (b) Designs meeting PP42 Thm 3.1(b) (strict CG2 and CG3) meet the hypotheses (PX) and (TC-cert) of §3 with diagonal certificates. The local potential of PP42 Lemma 3.0 gives each nontrivial gate pattern a strictly negative weighted sum.
- (c) If U_w is an additive witness for the union (U_w ≥ 0 on accepted records), it is a witness for OA.
- (d) PP42 Thm 2.1's direction "competitive ⇒ U-Bayes" (REFEREE_round50 §1.1) holds for every acceptance rule.

So OA's design space contains the union's. Selectivity can never remove a witness that the union has (§6).

---

## 3. What OA delivers

**Theorem 3.1 (defence on every support; PROVED).** Let b be gated and X ≠ C_b measurable. Some world w ∈ supp λ_b ⊆ supp b accepts rec(C_b, X) through b's own gate.

*Proof.* By uniqueness, λ_b·Φ^b(C_b → X) > 0, so some v ∈ supp λ_b has Φ^b_v > 0 and R^b_v > 0. Any maximiser w then has R^b_w > 0, hence θ^b_w > 0, hence w ∈ supp b. Vertex models are covered by guidance. ∎

Every selected non-vertex model must be gated (Prop 7.1), so this is the whole of the defence clause, including edge supports.

**(PX), the pair condition.** For gated N ≠ M and every world w, there is no D ⊆ {N ≠ M} such that N accepts (D: N → M) at w and M accepts (D: M → N) at w. In words: there are no co-active two-cycles.

**Lemma 3.2 (reverse refusal; PROVED under (PX)).** If a nontrivial record P → Q is accepted at w through a gate N, then Q → P is refused at w.

*Proof.*
- *Guidance.* If guidance accepted Q → P, then P → Q would be a nontrivial weak w-improvement, so R^N_w ≤ 0 < max R^N, and N could not have accepted it.
- *Another gate.* If a gated M accepted Q → P, then M = Q ≠ P = N on D. The two acceptances form a co-active two-cycle on D ⊆ {N ≠ M}, which (PX) excludes. ∎

So, under (PX), (TC) at w is equivalent to the absence of nontrivial accepted triangles at w (as in PP47 Lemma 1.3).

**Theorem 3.3 (protection; PROVED under (PX)).** No Y ≠ N satisfies Y ⪯_w N at all three worlds. Hence every gated model is undominated and has no all-world tie partner, and direct (C) holds for it.

*Proof.* Let w₀ be a maximiser of R^N(rec(N, Y)). Then R^N_{w₀} > 0 and N accepts rec(N, Y) at w₀.
- *Guidance cannot accept rec(Y, N) at w₀.* That would make N → Y a weak w₀-improvement, giving R^N_{w₀} ≤ 0.
- *No gate can accept it either.* A gated realiser M of Y on D would form, with N, a co-active two-cycle at w₀, which (PX) excludes.

So Y ⋠_{w₀} N. ∎

**Shape certificates.** A *shape* is σ = (κ₁, κ₂, κ₃) ∈ ({G} ∪ gates)³, fixed at a world w. Link i of the triangle X → Y → Z → X is judged by guidance (κ_i = G) or by gate κ_i (then the link's old side equals C_{κ_i} on its support).

At a problem g, the allowed patterns (x, y, z) are those consistent with these constraints. A **certificate** for σ at w is a choice of ζ^i in the dual of κ_i's role cone, one for each gate link. In role units that dual is {ζ : ζ_w ≥ Σ_{v≠w} |ζ_v|, ζ_v ≤ 0}. The certificate must satisfy, for a.e. g and every allowed nontrivial pattern,

  Σ_{gate links i nontrivial at g} ζ^i · θ^{κ_i} ⊙ (ℓ^{κ_i}(g, t_i) − ℓ^{κ_i}(g, s_i)) < 0.

With ζ^i = c_i e_w this is the pointwise form of the CG2/CG3 cycle inequalities. The off-diagonal "tilts" are OA's extra freedom.

**Theorem 3.4 ((TC) for all copies; PROVED).** Assume (PX), and assume a certificate for every shape with at most three distinct gates, at every world. Then no nontrivial triangle is accepted, and (TC) holds for all common-context copies.

*Proof.* An accepted gate link has R^{κ_i}(L_i) in κ_i's role cone, so ζ^i · R^{κ_i}(L_i) ≥ 0. Summing over links, the total equals the integral of the certificate expression. That integral is < 0 for a nontrivial triangle: nontrivial patterns fill a non-null set, and all-guidance nontrivial patterns are impossible because ranks are injective. This is a contradiction. Apply Lemma 3.2. ∎

- **Triangle-local.** Each triangle needs only its own certificate. No global constants and no global witness are assumed.
- **Exactness in type models.** When fields are constant on finitely many cell types, the achievable link vectors of a shape form a finitely generated cone (Lyapunov). Absence of an accepted nontrivial triangle is then an LP, decided exactly by `oa_lib.py`. Every claim in §§4, 6 and 7 uses this.

**Remark 3.4′ (padding; PROVED).** In the union rule, adding w-improvements to a gate link only lowers Φ_w. In OA it can help w become the argmax, because it may lower other coordinates more. So the certificates must also cover "pad" patterns: a gate link moving its own advice to a w-better value, closed by guidance. Diagonal certificates cover pads automatically; tilted ones do not.
- *Exact symmetry removes pads.* Suppose at every mixed point the role-scaled penalties of the two majority worlds coincide (SYM). Then every w-improvement has w as its most negative role coordinate, and pads can be stripped from any accepted triangle.
- *But SYM excludes two-sided classes.* Under SYM, every class on which a pair disagrees in both directions (moves worse only at the odd world, and moves worse only at the two majority worlds) violates (PX). Along the segment between the two types, the role vectors live in the plane v_j = v_k. There argmax ∈ {c} or {j, k}, and the two crossing points of the intermediate value theorem cannot be ordered both ways.
- Posterior pairs have two-sided classes whenever min(ρ_j, ρ_k) < ρ_c < max(ρ_j, ρ_k), with ρ = b/a. So SYM is a tool for examples, not a design rule.

**Theorem 3.5 (closed sections with changing realisers; PROVED).** Assume:
- **(S1)** b ↦ C_b is continuous in measure on Δ;
- **(S2′)** for each pair of advice values x, y, b ↦ θ^b⊙(ℓ^b(·, y) − ℓ^b(·, x)) is continuous from Δ into L¹, vertices included.

Then for every measurable rival X and world w, A_w(X) = {p : C_p ⪯_w X} is closed in Δ.

*Proof.* Put

  F_w(X) := {(p, b) : C_b = C_p a.e. on {C_p ≠ X}, R^b_w(rec(C_p, X)) ≥ R^b_v(rec(C_p, X)) for all v}.

F_w(X) is closed. Realisation is closed (Lemma S, step 2). The role vector is jointly continuous by (S1), (S2′) and absolute continuity, as in Lemma S, step 3. The argmax condition is a finite set of closed inequalities.

A_w(X) is the union of the projection of F_w(X) onto p and the guidance set. The projection is closed, because b ranges over the compact Δ. The guidance set is closed (Lemma S, step 1). ∎

- **Boundary behaviour.**
  - Edge-support competitiveness is Thm 3.1.
  - A limit realiser b on a face with θ^b_w = 0 can carry acceptance at w only for a trivial record: its own records have max R^b > 0 = R^b_w.
  - So fixed-rival limits approaching an edge or a vertex need no boundary layer beyond (S2′).
  - Realisers are compact because P(r) is closed in Δ.
- **What (S2′) asks.** It is a design requirement on the fields, not an axiom. With θ^b = b it requires the fields to stay bounded as a world's likelihood vanishes; θ then removes that world.

**Theorem 3.6 (consolidated reduction; PROVED).** Assume:
- **(H1)** gates as in §1 at every non-vertex index;
- **(H2)** (PX) for all pairs;
- **(H3)** shape certificates as in Thm 3.4;
- **(H4)** (S1) and (S2′).

Then reflexivity, strict (G), (IB), (TC) for all copies, (S) on Δ, (LA) and direct (C) all hold. Moreover, every rival X is strictly dominated by a selected model, or is selected.

*Proof.*
- Sections are closed (Thm 3.5) and cover Δ in the KKM sense (Thm 3.1). So KKM gives p with C_p ⪯_w X at all w.
- If X ≠ C_p, Thm 3.3 excludes an all-world tie, so the domination is strict.
- By the same KKM argument every undominated model is tied with, hence equal to, a selected one. So direct (C) holds globally (AUDIT_completion §5). ∎

So, as the audit anticipated for the whole-simplex reduction, explicit repairs are not needed: **the field problem (H2)–(H4) is everything.** §§4–7 test what (H2) and (H3) can be.

---

## 4. The pair obstructions do not come from universal acceptance

**Theorem 4.1 (the KKM test; PROVED).** Let N be a model with defence on its support. Suppose its verdicts on records realised by N are closed along mass paths. This holds whenever its own-gate acceptance at w is "Φ^N(r) ∈ Γ^N_w" with Γ^N_w closed; it covers union, OA and every closed selective rule.

Let M be any model. Suppose there are bounded non-null E₁, E₂, E₃ ⊆ {N ≠ M} such that, on E_k, M is pointwise strictly better than N at every world except k. Then some bounded non-null D ⊆ ∪E_k has, with Y := M[D ↦ N], Y ⪯_w M at all three worlds. Hence M is dominated by Y or all-world tied with Y. If M is coherent, Y is incoherent, so M cannot be coherent and undominated under direct (C).

*Proof.*
1. **The path.** Let v_k := Φ^N(E_k : N → M). Its k-coordinate is > 0 and its other two are < 0. By Lyapunov choose nested E_k(t) with Φ^N(E_k(t)) = t v_k. Put D(s) := ∪_k E_k(s_k) for s ∈ Δ. Then r(s) := (D(s) : N → M) is realised by N.
2. **The closed sets.** The sets F_w := {s : r(s) accepted at w} are closed by hypothesis.
3. **The face condition.** On the face spanned by S ⊆ {1, 2, 3}, r(s) is a strict pure v-improvement for every v ∉ S. So it is refused at v (strict (G)). By N's defence it is accepted somewhere, hence at a world of S ∩ supp N.
4. **KKM.** KKM gives s* in all three F_w. Now rec(Y, M) = r(s*) by (IB), so Y ⪯_w M at every w.
5. **Incoherence.** Coherent models agreeing off a bounded set agree a.e. (AUDIT_completion §1), so Y is incoherent. ∎

In type language, write K₁(N, M) := {k : some disagreement has M better than N exactly at k} and K₂ := {k : M worse exactly at k}. **The test fails iff K₁ or K₂ is all three worlds.** It is applied in both orientations.

**Corollary 4.2 (PROVED; CHECKED, `kkm_census.out` (A), (C)).**
- **(a) Combined cut.** For AB = C_(a,b,0), the B-families B₁, B₂, B₃ are three single-better types for T against AB. So T is dominated, or tied with an incoherent fill, in every system in which AB is selected with closed own verdicts. This is PP45 Thm 3.1 and PP46 Thm A/Prop C, without CG2, without (TC) and without T's uniqueness.
- **(b) Full cut.** It fails in both orientations. This includes PP47 Thm 2.7.
- **(c) Single cap.** It passes: K₁ = {2, 3}, K₂ = {1}.
- **(d) Checks.**
  - For 300 random AB fields under three closed rules (union; OA with random θ; "near-argmax" with a random κ), the KKM point s* was computed and AB's own gate verified to accept (D* : AB → T) at all three worlds, exactly, 300/300.
  - Exact multicap disagreement censuses reproduce (a)–(c).

**What would escape.** Only rules whose own verdicts are not closed along mass paths: non-closed role regions (strict argmax with tie-breaking), or verdicts depending on fine support structure. Lemma S's section mechanism *is* L¹-closedness of verdicts, so these rules lose the only section proof we have.

**Theorem 4.3 (argmax selectivity keeps the type test; PROVED; CHECKED, `e1_type_obstruction.out`).** Consider any rule whose role cones contain those of some role-weighted argmax rule; this covers union and OA. Suppose gated N, M fail PP45's type test. Then (PX) fails at some world, for every choice of fields.

*Proof.*
1. **Classification.** The type test fails iff K₁ = all, or K₂ = all, or K₁ = K₂ = {j, k} (both "not top" and "not bottom" exclude the same two worlds, PP45 Lemma 2.2). The first two cases are Thm 4.1. In the third (call it E1, with j, k = 2, 3) the disagreement types are W = {2}, W = {1, 3}, W = {3} and W = {1, 2}.
2. **Dual form of (PX).** (PX) at w is equivalent to a dual certificate (p^w, q^w) in the duals of the role cones with p^w·α(g) + q^w·β(g) < 0 at every disagreement point. Here α is N's role vector of N → M and β is M's of M → N. This uses separation on the finitely generated cone of four type generators (one sub-record per type), which suffices.
3. **Unblocked types.** Gordan's alternative shows that a type (W, R) admits fields iff there is no t in the simplex with x(t) := Pᵀt/π^N in cone(1) + S(W, R) and y(t) := Qᵀt/π^M in cone(1) + S(R, W). For E1 these four conditions read T₂(x)∧B₂(y), B₂(x)∧T₂(y), T₃(x)∧B₃(y) and B₃(x)∧T₃(y), with:
   - T_w(z): z_w ≥ max(0, z_others);
   - B_w(z): min(z_others) ≥ max(0, z_w).
4. **The KKM point of x.** The rows of P are positive at their own world and ≤ 0 elsewhere, with nonnegative weighted sums. So "top of x" is a KKM labelling, and there is a t* with x(t*) = κ𝟙, κ ≥ 0. At t*, T₂, T₃, B₂ and B₃ all hold for x. So either some condition already holds at t*, or y(t*) has world 1 as strict top and y₂, y₃ < 0.
5. **The segment.** In the latter case, take a_x on the edge [e₂, e₃] with x₂ = x₃. Along [a_x, t*], x satisfies T₂ ∧ T₃. y₁ is ≤ 0 at a_x and is the strict top at t*. At the first point where y₁ = max(y₂, y₃), B₂(y) or B₃(y) holds. ∎

- **CHECKED, dual side.** 2,000 random exact certificates; in each, the predicted violation point is verified in Fractions (1,986 at t*, 14 on the segment).
- **CHECKED, primal side.** 16 random own-Bayes E1 type models with all agreement regions present: every one has an exact co-active two-cycle and an exact (TC) violation with a nontrivial guidance link, which is always a genuine violation.
- **(TC) failure.** It follows whenever a co-active record can be taken interior on one side, by the CG2-necessity triangle of REFEREE_round50 §1.2 with the robust link on that side. The fully degenerate case, where ties persist on the whole co-active cone, is OPEN.

**Corollary 4.4 (PROVED, modulo that degenerate case).** For argmax-type selective rules, the pairs that can be gated together are exactly those passing the PP45 type test. For a single pair, the type test suffices for the union (PP46 Thm B, converse), hence for OA (Prop 2.4(b)). **At the level of pairs, selectivity gains nothing.**

---

## 5. The posterior family

**Proposition 5.1 (pair ordering on the closed simplex; PROVED; CHECKED).** Let a ≠ b ∈ Δ, boundary included. At any disagreement of C_a and C_b, let W be the worlds where C_b is worse and R those where it is better. Then there is no κ with b_w ≥ κa_w on W and b_r ≤ κa_r on R. The constraint on κ is κ ≥ 0 when C_b answers and κ > 0 when C_b is silent.

*Proof.* C_a accepts h iff Σ_i p_i a_i h_i > 0 for all p ∈ M, since a·p > 0. With this, the proof of AUDIT_posterior_pairs §2 goes through verbatim:
- *Silence to answer.* Some p has Σ p a h ≤ 0, and termwise b_i h_i ≤ κ a_i h_i. So Σ p b h ≤ κΣ p a h ≤ 0, contradicting C_b's acceptance.
- *Answer to silence.* Termwise b_i h_i ≥ κ a_i h_i with κ > 0, so Σ p b h ≥ κΣ p a h > 0 for every p, contradicting C_b's silence.
- *Opposite answers.* Treat as silence to answer for the new answer; W and R coincide. ∎

For interior a, b this is min_W (b/a) < max_R (b/a), the audit's theorem.

**Corollary 5.2 (posterior pairs pass the KKM test everywhere; PROVED; CHECKED).** For a ≠ b ∈ Δ, K₁ ≠ {1, 2, 3} and K₂ ≠ {1, 2, 3}.
- *Interior.* W = {k} never occurs for k ∈ argmax(b/a) = argmin D, and R = {k} never occurs for k ∈ argmax D.
- *Boundary.* Put S := {k : a_k = 0 < b_k}.
  - If |S| ≥ 2, a is a vertex, and W always contains it.
  - If S = {k*}, W = {k*} is excluded with κ large.
  - If S = ∅, W = {argmax_{supp a} b/a} is excluded with κ = that maximum.
  - Swapping a and b handles K₁.

CHECKED (`kkm_census.out` (B)): 280 exact index pairs (interior, near u, edge, vertex mixtures), 268,894 exact disagreements. Prop 5.1 holds at every one, no pair fails the test, and the predicted missing worlds are missing. In 237 pairs one side shows two of the three single types, so the test is tight, not vacuous.

**Reading.** Under any closed selective rule, Thm 4.1 is the pair-level shadow of the KKM theorem that delivers dominators (Thm 3.6). D = log(a/b) is the certificate that this shadow never falls on two posterior models. With the audit's pair-ordering theorem (the type test) and Cor 4.4, **every posterior pair is gateable under OA, as under the union.** The posterior family's difficulty is not at pair level.

---

## 6. Room and global prices

**Proposition 6.1 (CHECKED, `oa_room.out`).** Take the type model of T and the single cap at vertex 1. There are three band pieces (A₁, B₂, B₃) and all ten agreement regions. Own-Bayes type-constant fields were found such that:
- (i) CG2 fails at world 2 (sup 969/154 > inf 161/594) and at world 3 (235/54 > 136/63), and the union rule has an exact (TC) violation at world 2;
- (ii) under OA all 33 checks (PX at three worlds; ten shapes at three worlds) pass, with exact Farkas certificates.

So OA strictly enlarges the space of admissible fields at fixed models.

- **(iii) Witnesses at every world.** The OA-accepted set nevertheless has an exact additive witness at every world. So at worlds 2 and 3 there are *no rescaled-gate prices*, yet the design is witnessed. "No CG2 constants" is weaker than "no additive endorser" once acceptance is selective. PP51 Lemma 2.4's equivalence is specific to the union rule.
- **What this means for the audit's question.** By Prop 2.4(c) selectivity never removes a witness, and by Prop 2.4(d) a witness at every world makes every competitive model U-Bayes, which is the excluded route. So OA does not by itself let the constraints avoid global prices. It replaces scalar pair constants by dual certificates with tilts. Witness-freeness still has to come from triangle-local certificates that are globally inconsistent, as in audit §3's four-cycle and PP51 Thm 4.1. OA only enlarges the space in which those must be found.

---

## 7. The kink triple (coordinator's request)

**Proposition 7.1 (ungated selected models are indefensible; PROVED).** In any rule in which non-guidance acceptance requires a gated realiser, every selected model that is not perfect at some world of its support must carry a gate.

*Proof (PP45 Lemma 2.3(b), verbatim).* Let X equal C_p except:
- on a thin contradiction shell, which blocks every other coherent realiser;
- on small sets, one for each w ∈ supp p, where X is w-correct and C_p is not.

Only C_p realises rec(C_p, X), and guidance refuses it at every w ∈ supp p. ∎

So "gate a kink-free subfamily and defend the rest by designated realisers" (PP51 §5.3(a)) is impossible under index = likelihood on a 2-D patch. Designation can only decide *which realiser speaks* on a record with several realisers. It cannot exempt a selected model from carrying a gate. With all of A = u, B = (406, 421, 373)/1200, D = (406, 373, 421)/1200 selected, all three are gated.

### 7.2 OA on the kink triple

**Setting (CHECKED geometry, `kink_oa.py`).** The cell arrangement is enumerated exactly, with PP51's code. This gives 28 (class; advice of A, B, D) types; PP51's 31 types merge where all three models are silent. The family is two-valued. One region per type loses nothing (PP51 Lemma 2.2; the same per-type argument applies to OA's dual certificates).

**Search in certificate space (NUMERICS, `kink_oa_dual.py`).**
- By the dual form used in Thm 4.3, (PX) for a set of pairs holds iff there are certificates (p, q), one pair of rows per pair and world, in the duals of the role cones, together with Bayes weights. Given these, every cell type is an LP in the role-unit increments of A, B, D.
- Score = the number of infeasible cells. Restarts with local moves were run in OA duals ("tilt") and in union duals ("diag", the CG2 constants), for the pairs (A, B), (A, D).
- **Result.** Neither reached 0.
  - In every restart that reached score 1, the single infeasible cell was one of PP51's two certificate cells. These are class M₁, with T answering alone: the majority answer (wrong only at world 1, "above") or the minority answer (right only at world 1, "below").
  - Counts (in the `.out` files): tilt reached score 1 in 12 of 20 restarts, with the bad cell "below" 7 times and "above" 5 times. Diag reached score 1 in 3 of 21 restarts, always at "above". Neither ever reached 0.
- Adding the third pair only adds constraints.

**Nearest-miss verdicts (CHECKED, `kink_oa_nearmiss.out`).** From a score-1 certificate, type-constant fields were built (exact own-Bayes). Exact LPs then find:
- co-active two-cycles for (A, B) and (A, D) at world 2;
- exact accepted triangles with a nontrivial guidance link, which are genuine (TC) violations, in 10 shape–world combinations.

**CONJECTURE 7.2.** For every OA (indeed every argmax-type, closed) rule, every own-Bayes field system on {u, B, D} at ε = 3/10 fails (PX) for (u, B) or (u, D). Outside degenerate ties it then fails (TC).
- **Why it should hold.** The two certificate cells are a two-sided class for both pairs through T: type W = {2, 3} and type W = {1}, with A's increments shared between the pairs. That is the structure that defeated SYM in Rem 3.4′ and the union rule in PP51. The search shows that tilted duals buy freedom elsewhere but not there.
- **A proof would follow** PP51 Thm 5.1, with the dual rows of Thm 4.3 in place of the constants z^N. OPEN.

**Reading together with PP50 Theorem K.** PP50 shows that under the union rule every gated set of posterior indices meets a neighbourhood of u in a null set. Prop 7.1 shows that *every* realiser-gated rule must gate every selected model. If Conjecture 7.2 holds uniformly on PP50's box, as the mechanism suggests, then OA cannot realise a positive-measure posterior family through T either. The "selective" exit of PP50 would then be closed for argmax-type rules.

### 7.3 What is left on the selective side

**Proposition 7.3 (designation on shared records cannot remove a strict co-activity; PROVED).**
- **Hypotheses.** Let N and M be gated. Suppose N accepts (D: N → M) at w and M accepts (D: M → N) at w, both with a strict argmax and strictly positive maximum. Suppose D is also realised by another gated M′. Suppose finally that {N ≠ M} ∖ {M = M′} is non-null.
- **Conclusion.** Under every designation rule, the co-activity reappears on records with M as sole realiser. The CG2-necessity triangle (REFEREE_round50 §1.2) then gives a (TC) violation.

*Proof.* Add to D a small set E ⊆ {N ≠ M} on which M′ ≠ M. Then the M-side of D ∪ E has M as its only realiser, so no designation choice is available. Strict argmax and strict positivity survive small perturbations of both role vectors. ∎

On the kink cells B = D, and the co-activities found are generic, hence strict. So **designation within shared records does not help there**. The only selective lever left is:
- **Verdicts not closed along mass paths (OPEN).** Examples are strict argmax with tie-breaking, or lexicographic roles. Such rules escape Thms 4.1 and 4.3 and Prop 7.3, but they lose Lemma S. A section proof would have to use the fixed-rival structure instead.

The other exit, half-plane answer regions (PP51 §5.3(b), PP50 §4), changes the family and not the rule. There OA's extra room (Prop 6.1) is what the selective branch can contribute.

---

## 8. Status, scripts, next step

| Result | Label |
|---|---|
| Def 2.0; Props 2.1, 2.2, 2.4; Rem 2.3 | PROVED |
| Thms 3.1, 3.3–3.6; Lemma 3.2; Rem 3.4′ | PROVED (3.3–3.4 under (PX)/(TC-cert); 3.5 under (S1), (S2′)) |
| Thm 4.1, Cor 4.2 | PROVED; CHECKED |
| Thm 4.3, Cor 4.4 | PROVED ((TC) part outside the degenerate tie case); CHECKED |
| Prop 5.1, Cor 5.2 | PROVED; CHECKED |
| Prop 6.1 | CHECKED |
| Props 7.1, 7.3 | PROVED |
| Conjecture 7.2 (the kink survives OA) | NUMERICS (search); CHECKED (near-miss verdicts); CONJECTURE |
| Non-closed verdicts; proof of Conjecture 7.2 on PP50's box | OPEN |

**Scripts** (`r9/PP52_py/`; run `python3 -I -B <script> > <script>.out` inside the folder; the CHECKED scripts end ALL PASS):

| Script | Content | Label |
|---|---|---|
| `oa_lib.py` | type models; OA and union rules; (PX), triangle-shape and guidance-violation LPs; exact feasible points and Farkas certificates; additive-witness LP | library |
| `kkm_census.py` | (A) Thm 4.1 at (T, AB), 300 exact KKM points under three closed rules; (B) posterior census, 280 pairs, 268,894 disagreements; (C) multicap controls | CHECKED |
| `e1_type_obstruction.py` | Thm 4.3: 2,000 exact dual-side certificates with the predicted violation verified; 16 primal models with exact (PX) and (TC) failures | CHECKED |
| `oa_room.py` | Prop 6.1: OA-admissible, union-inadmissible fields for (T, cap); exact witnesses at every world | CHECKED (the search itself is NUMERICS) |
| `kink_oa.py` | exact cell enumeration of the kink triple (PP51's code), type model, per-cell certificate LPs, design builder | library (its own primal search mode is NUMERICS) |
| `kink_oa_dual.py` | §7.2 certificate-space search, OA ("tilt") and union ("diag") duals; outputs `kink_oa_dual_tilt_two.out`, `kink_oa_dual_diag_two.out` | NUMERICS |
| `kink_oa_nearmiss.py` | §7.2 nearest-miss design with exact own-Bayes, (PX) and (TC) verdicts | CHECKED (search NUMERICS) |

**Most important next step.** Prove Conjecture 7.2 in the dual-row form of Thm 4.3, uniformly on PP50's kink box; that would settle the selective exit for closed rules. In parallel, carry OA, with its strictly larger field space (Prop 6.1), to a family with half-plane answer regions (PP51 §5.3(b)). Thms 4.1 and 4.3 are passed there, and the audit's four-model test of witness-freeness is the decisive check.
