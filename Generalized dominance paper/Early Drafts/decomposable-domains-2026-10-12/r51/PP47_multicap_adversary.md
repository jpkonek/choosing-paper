# PP47. Adversary on the multicap programme: the checkpoint, the box, and what is forced

23 October 2026. Task PP47 of Brief 51. One reader (me); not refereed.

**Labels.** PROVED: complete argument here, or a cited refereed result. CHECKED: exact rational computation in `PP47_py/` (all three scripts ALL PASS). NUMERICS: none is used for a claim here. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF51; AUDIT_round51, AUDIT_multicap, AUDIT_round51_answers (binding); PP42 (design TWG, Thm 3.1, Thm 3.2, Lemma 4.1, Props 4.4, 5.1, 5.2); PP43 (Lemma 3.1, Lemma 3.3, Thm 3.4); PP30 Thm 3.1; PP33 Thm 3.1; PP36 Prop K; PP40 Prop 3.1 (splice form); AUDIT_completion. Two coordinator relays during the task: REFEREE_round50 (Thm R1, Lemma S, CG2 necessity without the agreement hypothesis, the s_i ≤ 2ε/3 caveat), and the constructor's PP45 (type lemma, Thm 3.1, Cor 3.2, Cor 3.3, the tripod). I add no axioms. Extra hypotheses are named where they enter.

**Conventions.** (R): a gate accepts a record whose own-field value is > 0. (R0): it accepts ≥ 0. A *gate union* accepts a record at w iff it is guidance or some gated realiser of its old side passes it. The bands are H_b := H_b(s_b) ⊆ Sil(T). The cap answer σ_b on H_b is b-wrong. Each band carries three *families* (PP45 Lemma 1.1; CHECKED again here):
- A_b: σ wrong only at b;
- B_j: σ right only at j;
- B_k: σ right only at k.

Each family meets every band and every strip H_b(s) ∖ H_b(r), r < s, in a non-null open set (`geom47.out` (b)–(d)).

---

## 0. Verdict

1. **Question 1. Yes: there is a necessary obstruction for every gate-union design, and it does not come from the strong test.**
   - The constructor's Theorem 3.1 (PP45) is correct (§2.4). T and any combined cut C_(a,b,0) cannot both be gated.
   - I remove its one open loophole, the case where T's own Bayes optimum is not unique:
     - **Under (R0)**, which Lemma S needs for closed sections, the non-unique case forces an all-world tie between T and an incoherent fill. That violates direct (C) (Thm 2.5).
     - **Under (R)**, at the four-model checkpoint, it makes T uncompetitive.
   - The obstruction comes from the **gate-union architecture**, not from the axioms and not from the stronger test. It also covers lexicographic gates whose bounded-record verdicts are additive, and combined cuts that are dominators without being gated (Prop 2.6).
   - The other levers named in the brief are consequences of (TC), and add no constraint beyond CG2 and Thm R1 (Prop 2.1):
     - Prop K and its splice form;
     - PP30 Thm 3.1;
     - PP33 Thm 3.1.
   - PP43 Thm 3.4 does not bite near s = 0 (Prop 2.2). What remains of it is a forced continuity: the selection must converge to T at T's index (Cor 2.3).

2. **Question 2. The two-corner rival needs a dominator near T that misses at most one vertex.**
   - Which models are excluded follows from strict (G) and a sign table (Prop 3.1): T, caps at the third vertex k, and caps at i or j whose cut contains their own piece.
   - At every world where the domination is not guidance, a gated realiser that agrees with the dominator off a bounded set carries it (Prop 3.2). So **no dominator may be a refinement of T that misses two vertices**, gated or not (Cor 3.3). That answers the coordinator's (c): yes.
   - Dominators of shrinking rivals converge to T (Lemma 2.4).
   - Domination by a combined cut is ruled out twice: by the type test, and independently, for small rivals, by T's own Bayes margin (Cor 3.4).

3. **Question 3. The test is tight under (R), and almost tight under (R0).**
   - **Under (R).** I re-derive the referee's Thm R1 by a short independent route (Lemma 1.3 and Gordan's alternative). The closed interval-triangle test is exactly (TC).
   - **Under (R0)**, the case the referee left open, the exact two-valued test is Thm 4.1, PROVED and CHECKED:
     - (TC) holds iff the closed test holds with positive constants;
     - **and** no triple is *tight with all three bounding extremes attained*.
   - **A tight attained triple is a genuine forbidden configuration.** It gives an exact nontrivial triangle with all three link values 0. (R0) accepts it, and every reverse is refused (`tc_r0_47.out` Ex1).
   - Two corrections follow:
     - the audit's "open intervals" form of the strict test is stronger than (TC) needs;
     - the closed test alone is weaker than (TC).

4. **The eight-model box fails as a gated family; three nearby aims remain.**
   - With T gated, only the tripod {t·e_i} survives (PP45 Cor 3.2, confirmed). My independent argument from the A-families alone already excludes the full cut (Thm 2.7); the B-families exclude the double cuts.
   - **Aim (i): the tripod**, extended by cuts at one vertex with variable tilt (PP45 §6).
   - **Aim (ii): non-refinement two-vertex modifications** whose families at each vertex are restricted. The type test is then passable at the level of orderings (Prop 5.1; geometric realisability CONJECTURE).
   - **Aim (iii): bounded-record verdicts that are not additive.** This is a separately labelled branch.

| Item | Result | Source of the obstruction | Label |
|---|---|---|---|
| Own weak Bayes forced | Lemma 1.2 (= PP45 Lemma 2.3) | architecture | PROVED |
| Nontrivial accepted gate links have refused reverses | Lemma 1.3 | architecture + CG2 | PROVED |
| Prop K, splice K^S, PP30, PP33 impose nothing beyond (TC) | Prop 2.1 | — | PROVED |
| PP43 Thm 3.4 reduces to own-Bayes failure; no bite near s = 0; selection must converge to T | Prop 2.2, Cor 2.3 | axioms (sections) + (S2) | PROVED |
| Dominators of shrinking fills converge to T | Lemma 2.4 | architecture + CG2, under (U) | PROVED |
| T + combined cut impossible (PP45 Thm 3.1), now without T's uniqueness under (R0) | Thm 2.5 | **architecture** | PROVED; CHECKED |
| Reach: lexicographic gates with additive bounded verdicts; ungated combined-cut dominators | Prop 2.6 | architecture | PROVED |
| T + full cut impossible from A-families alone | Thm 2.7 | architecture | PROVED; CHECKED |
| Two-corner rival: exclusions, realisers, no two-vertex refinement as dominator | Props 3.1, 3.2, Cor 3.3, 3.4 | axioms (strict (G)) + architecture | PROVED |
| (TC) under (R) ⇔ closed test (Thm R1) | §4.1 | — | PROVED (referee; re-derived) |
| (TC) under (R0) ⇔ closed test + no attained tight triple | Thm 4.1 | — | PROVED; CHECKED |
| Order-level feasibility of restricted two-vertex modifications | Prop 5.1 | — | PROVED (order level); CONJECTURE (geometry) |

---

## 1. Three tools

**Lemma 1.1 (bands; PROVED in PP45 Lemma 1.1; CHECKED `geom47.out`).** On H_b, σ is b-wrong and every point lies in A_b, B_j or B_k. All three families meet every band and every strip H_b(s) ∖ H_b(r) (0 ≤ r < s ≤ δ) in non-null open sets.
- `geom47` checks the union lemma and two-valuedness on 7,033 problems × 8 models.
- It checks the sign pattern of every sampled band point, with all three families found at 12 (ε, b, t) cases.
- It finds exact strict A-family witnesses in 24 strips.

**Lemma 1.2 (own Bayes is forced; PROVED in PP45 Lemma 2.3).** In a gate union under (R) or (R0), a gated member that is competitive on supp p against every measurable rival is weakly λ-Bayes for its own field at some λ ∈ Δ_supp p. Every multicap member's λ is interior, because T's minority answers on Ans(T) are right only at one world.

The proof uses Lyapunov's theorem, separation, and PP43's contradiction shell. The shell blocks every other realiser.

**Lemma 1.3 (gate links are strict; PROVED).** Fix a world w. Assume one of:
- (R) with CG2 for every pair of gated members at w;
- (R0) with CG2 strict a.e. for every pair.

Let a nontrivial record P → Q be accepted at w, through guidance or through a gate. Then its reverse Q → P is refused at w. In particular **no two distinct models tie at w**, and (TC) at w ⇔ no nontrivial triangle is accepted at w.

*Proof.*
1. **Guidance.** If the reverse were a weak w-worsening, P → Q would be a nontrivial weak w-improvement. Every strictly guiding field rates that < 0, and guidance refuses it, so P → Q could not have been accepted.
2. **Gates.** Let N be a gated realiser accepting P → Q, and M any gated realiser of Q on the support D. Then N = P ≠ Q = M on D, so D ⊆ D_NM, and on D the move N → M is the move P → Q.
   - CG2 gives c_N f^N ≤ c_M f^M (strictly a.e. in the (R0) case).
   - So ∫_D f^M ≥ (c_N/c_M)∫_D f^N ≥ 0, with strict inequality under (R) because ∫ f^N > 0, and under (R0) because the inequality is strict a.e.
   - M's gate value of Q → P is −∫_D f^M < 0, so M refuses.
3. **The last claim.** A violation of (TC) is an accepted triangle with a missing reverse. By the above, every accepted nontrivial triangle has all three reverses missing. ∎

---

## 2. Question 1: necessary obstructions for gate-union designs

### 2.1 The listed levers are consequences of (TC)

**Proposition 2.1 (PROVED).** Each of the following is derived from reflexivity, strict (G), (IB) and (TC) alone (each in its source):
- PP36 Prop K;
- PP40 Prop 3.1 (K^S);
- PP30 Thm 3.1(b);
- PP33 Thm 3.1.

So in a gate union satisfying CG2 and the triple test of Thm R1 (§4), they hold automatically. They are **not** additional constraints on fields. Each refusal they demand is delivered by a CG2 inequality between the dominator's realiser and the refusing member (as in PP42 Lemma 3.3).

For the two-corner rival, the concrete instances are Prop 3.3 below.

### 2.2 PP43 Thm 3.4 near s = 0

PP43's killer uses one feature: a *bounded* part on which the post-jump model keeps a uniform Bayes margin over T, *added* to a tail part. A gate union has no common bounded part, so the analogue is the following.

**Proposition 2.2 (PROVED).** Let N be gated in a gate union under (R) or (R0).
- (a) If N is not weakly own-Bayes on supp p, an explicit rival refused at every world of supp p exists. Conversely, weak own-Bayes gives every rival a passing world of N's own gate:
  - under (R0), always;
  - under (R), unless Φ^N_w(N → X) = 0 at every w ∈ supp λ. Thm 2.5(c) exploits this exception.
- (b) Assume closed fixed-rival sections at T's index p_0, and members C_n at indices p_n → p_0. Then for every w and every gated realiser M of C_n on {C_n ≠ T}:

    limsup_n Φ^M_w(C_n → T) ≤ 0,

  provided the realisers' fields have a common envelope on a fixed bounded set (as in Lemma S's (S2)).

*Proof.*
- (a) The first claim is Lemma 1.2's shell rival. For the converse, weak own-Bayes gives λ·Φ^N(N → X) ≥ 0, so some w ∈ supp λ has Φ^N_w ≥ 0, and that is > 0 unless all such values vanish.
- (b) PP43 Lemma 3.1 verbatim:
  1. Take X = T[F ↦ w-correct], with F bounded, off the bands. Then T ⋠_w X.
  2. Closed sections give C_n ⋠_w X for large n, so every realiser M refuses: Φ^M_w(C_n → T) + Φ^M_w(T → X) < 0 (≤ 0 under (R)).
  3. The second term is −α^M_w(F) ≥ −∫_F env.
  4. Let F shrink. ∎

**Corollary 2.3 (the selection must converge to T; PROVED, under Lemma S's (S1)–(S2)).** Let the gated family be compact (Θ), with C_p = N_θ(p). If p_n → p_0, every limit θ* of θ(p_n) has N_θ* = T. Otherwise:
- by (S2) and Prop 2.2(b), Φ^θ*_w(N_θ* → T) ≤ 0 at every w;
- this contradicts N_θ*'s a.e.-unique own Bayes optimum;
- if that optimum is only weak, the values vanish on supp λ, so under (R0) N_θ* ⪯_w T at every w. Lemma 1.3 (strict CG2) then refuses every reverse, so N_θ* strictly dominates T, which contradicts T's undominatedness.

**So Thm 3.4 does not bite near s = 0.** Its uniform margin is replaced by own margins λ_θ·Φ^θ(N_θ → T). Under (S2) these tend to 0 exactly when θ → 0. The residue is Cor 2.3: no selection may jump away from T at p_0. The audit's "2-D selection through T's index" must be continuous at p_0 in this sense. A selection whose image near p_0 accumulates on members other than T fails sections, whatever the fields.

### 2.3 Dominators of small fills

**Lemma 2.4 (dominators of shrinking fills converge to T; PROVED under PP42's (U)).** Let X_n = T[G_n ↦ ·] with μ(G_n) → 0, and let a model N_n satisfy N_n ⪯_w X_n at every w in a gate union where CG2(T, M) holds for every gated realiser M. Then

  λ_T·Φ^T(T → N_n) ≤ κ_n := max_w sup_M (c_M/c_T)·∫_{G_n} env^M → 0,

and N_n → T in measure.

*Proof.*
1. Fix w. If the acceptance is by guidance, Φ^T_w(N_n → X_n) ≥ 0.
2. Otherwise it goes through a realiser M of N_n on supp ⊇ {N_n ≠ T} ∖ G_n. M agrees with N_n off a bounded set, and both are conic, so M = N_n on {N_n ≠ T}. Additivity gives

     Φ^M_w(N_n → X_n) = Φ^M_w(N_n → T) + Φ^M_w(T → X_n).

   The second term is at most ∫_{G_n} env^M.
3. CG2(M, T) on {N_n ≠ T} ⊆ D_MT gives c_T Φ^T_w(N_n → T) ≥ c_M Φ^M_w(N_n → T) > −c_M ∫_{G_n} env^M.
4. So Φ^T_w(T → N_n) < κ_n at every w, and hence λ_T·Φ^T(T → N_n) < κ_n.
5. Convergence in measure is PP42 Prop 2.3, step 1, which uses only T's a.e.-unique λ_T-Bayes property for ℓ^T. ∎

This agrees with the referee's item (3): dominating caps' indices approach T's. A fixed member D ≠ T dominates a fill T[G ↦ ·] only if ∫_G env ≳ λ_T·Φ^T(T → D).

### 2.4 The obstruction: PP45 Thm 3.1, audited and completed

**Audit of PP45 Lemma 2.1 and Thm 3.1 (coordinator's (a)).**
- The type lemma is a correct pointwise computation. Its inputs are:
  - interior weights (Lemma 1.2's remark);
  - CG2 at all three worlds (necessary under both (R) and (R0) by REFEREE_round50's form of PP42 Thm 3.1(c), which needs no agreement region);
  - strict preference of T and weak preference of AB at a.e. point of D_{T,AB}.
- The six families of Lemma 1.1 exclude every world from the top of D. The B_2 and B_3 families come from band 1 and B_1 from band 2.
- I also checked the forbidden configuration of PP45 §3.2. It is the triangle of PP42 Thm 3.1(c), with a strict guidance closing link. So the use of (TC) is legitimate under (R0) as well.
- The only gap is the hypothesis that **T is a.e.-uniquely own-Bayes**, which PP45 flags as a loophole. I close it under (R0).

**Theorem 2.5 (T + combined cut, without T's uniqueness; PROVED; algebra CHECKED `fullcut47.out` (v)).** Let AB = C_(a,b,0), a, b > 0. Consider a gate union in which T and AB are gated, CG2(T, AB) holds at all worlds, and both are weakly own-Bayes. (All three conditions are necessary for (TC) and universal competitiveness.)
- (a) Then D (PP45's vector) is constant, and both models are **exactly tied** at a.e. point of D_{T,AB} = H_1 ⊔ H_2:
  - λ_T·e^T = 0;
  - e^AB_w = γ_w e^T_w with γ_w > 0.
- (b) Under (R0), T has an all-world tie with an incoherent fill T[E ↦ AB]. Direct (C) fails, and rule IV gives F2.
- (c) Under (R), in the four-model checkpoint {T, C_(a,0,0), C_(0,b,0), AB}, T is not competitive against that fill.

*Proof.*
- (a) Run PP45's proof of (★) with T weak. The chain Σ_W b − Σ_R b ≥ e^{−m}(Σ_W a − Σ_R a) ≥ 0, together with AB's weak preference, forces both sums to be 0. Tightness needs D_w = m at every world with a_w > 0, which is all three worlds. So D is constant, and every inequality is an equality at every point of D_{T,AB}.
- (b)
  1. **The fill.** By (a), the vectors e^T(g) lie in the plane λ_T^⊥ at every point. The B-families present (B_2 and B_3 on band 1, B_1 on band 2) have sign patterns with exactly one negative entry, at three different worlds. Inside λ_T^⊥ these are three alternate sectors of the six mixed-sign sectors. Three vectors from alternate sectors positively span the plane: two of them lie in an open half-plane, and the third lies in the opposite sector between them. That is `fullcut47` (v) up to a global sign.
  2. **Exact zero.** By Lyapunov, as in PP43 Lemma 3.2, there is a bounded non-null E ⊆ D_{T,AB} with ∫_E e^T = 0 ∈ R³. Put X := T[E ↦ AB], which is incoherent by Lemma H.
  3. **The tie.** T's gate value of T → X is the zero vector. AB realises X on E, and its value of X → T is −(γ_w ∫_E e^T_w)_w = 0. Under (R0) both directions are accepted at every world.
- (c) E meets both bands. In the checkpoint the only gated model silent on both pieces is T, and T's own value is 0. Guidance refuses, since the record is mixed at every world. So T is refused at every world. ∎

**Theorem 2.7 (full cut, from the A-families alone; PROVED; CHECKED `fullcut47.out` (i)–(iv)).** Let F = C_s with s_1, s_2, s_3 > 0, or more generally any gated model that answers σ where a gated N is silent on non-null A-family parts of all three bands. If CG2(N, F) holds and both are weakly own-Bayes, then (under (R0) or with N a.e.-unique) contradiction.

*Proof.*
1. **Reduction.** Put μ_w := λ_F,w c_N,w/c_F,w and r_w := λ_N,w/μ_w.
2. **The A-family criterion.** At an A-family point of band b, a vector δ with N preferring S and F preferring σ exists iff r_b > min(r_j, r_k).
3. **Contradiction.** The band b minimising r fails, and the weak case reduces to Thm 2.5's equality structure.

This is independent of PP45. It is weaker than PP45 for double cuts, which need the B-families. The mixed case, where one band is of each kind, is always feasible (`fullcut47` (iv)). That matches PP45's "at most one up and one down". ∎

### 2.5 Reach of the obstruction (coordinator's (b))

**Proposition 2.6 (PROVED).**
- **(a) Lexicographic gates.** Let each gated member's verdict on **bounded** records be the sign of an additive strictly guiding bounded-level field, aggregated by union with guidance. Tail-first lexicographic gates (PP43 §4) are of this kind. Then Thm 2.5 and PP45 Thm 3.1 hold for the bounded-level fields. Every ingredient uses bounded records only:
  - the shell rival of Lemma 1.2;
  - the CG2 necessity triangle of PP42 Thm 3.1(c);
  - the zero-sum fill.
- **(b) Combined cuts as ungated dominators.** In a gate union with T gated, no model N that agrees with AB off a bounded set can dominate any rival X. Two reasons combine:
  - At some world, rec(N, X) is not a weak worsening. A two-valued rival never makes N pointwise better at all three worlds.
  - At that world a gated realiser M must agree with N off a bounded set. So M answers σ on cones at two vertices, and M fails the type test against T.
  - In addition, an *ungated* N cannot be selected, since by PP45 Lemma 2.3(b) it would have to be perfect at a world.
- **(c) What escapes.** The argument fails, and nothing is claimed, for:
  - non-additive bounded verdicts (lexicographic **within** bounded records, or a non-union aggregation);
  - installed acceptance records, which also violate Lemma S's (S4);
  - designs in which T is not gated (impossible, since T is selected and not perfect).

### 2.6 Classification for Question 1

| Requirement in the brief | Status in gate unions |
|---|---|
| Unique own Bayes of each member | weak form forced (Lemma 1.2); uniqueness not needed for the obstruction under (R0) (Thm 2.5) |
| Universal competitiveness against all measurable rivals | forces weak own Bayes; with CG2 it forces Thm 2.5 |
| Explicit domination of the repair class, two-corner rival included | forces dominators near T (Lemma 2.4) that miss at most one vertex (Cor 3.3) |
| (TC) with all copies | ⇔ CG2 + the triple test, exactly (§4) |
| Closed sections along a 2-D selection | forces the selection to converge to T at p_0 (Cor 2.3); fine on the tripod (PP45 Thm 5.1(iii)) |

**Answer.** The family {T, single caps, combined cut} has a necessary obstruction in **every** gate-union design: the combined cut cannot be gated beside T. Its source is the **architecture**: additive per-model fields, a union of realisers' gates, and CG2 necessity. It is not the stronger compatibility test, because CG2 and Thm R1 are exact. Nothing is known at the level of the axioms. The ground rules exclude making T's field a single realising field, and no axiom-level argument is offered.

---

## 3. Question 2: the two-corner rival

Let X := T[G_i ↦ σ_i, G_j ↦ σ_j], with bounded non-null G_i ⊆ H_i(s_i) and G_j ⊆ H_j(t_j). Write N = C_r for a box member.

**Proposition 3.1 (exclusions by strict (G); PROVED).** If G_i ⊆ A_i and G_j ⊆ A_j, then X is a strict pointwise improvement at the stated world of each of the following, so none of them is weakly no worse than X there:
- T, at world k;
- every N with r_i = r_j = 0 (caps at k), at k;
- every pure i-cap whose cut contains G_i, at i;
- every pure j-cap whose cut contains G_j, at j.

For other family choices, replace "k" by the worlds where both σ's are right. If G_i ⊆ B_j(band i) and G_j ⊆ B_i(band j), for example, there is no such world for T.

*Proof.* This is region-by-region sign bookkeeping with Lemma 1.1's patterns, checked on all seven regions of rec(N, X). A combined cut keeps a retreat on the complement of G in its cones. That retreat is mixed at every world, because every family meets every strip. ∎

This is PP45 Prop 4.1, extended to the box.

**Proposition 3.2 (who carries the domination; PROVED).** Suppose N ⪯_w X with N coherent, at a world where rec(N, X) is not a weak worsening. Then the acceptance is carried by a gated M with M = N on {N ≠ T} ∖ (G_i ∪ G_j), hence on {N ≠ T}, since both are conic.
- If N covers both pieces, M has σ on both cones. Single caps never realise it.
- If N = C^i_r does not cover G_i and G_i meets every H_i(r′) (a piece hugging the arc), then M must have i-cut exactly r and j-cut 0.

For a two-valued X, such a world always exists. N pointwise no worse than X at all three worlds would need σ right at all worlds, or wrong at all worlds, on a non-null set. Neither happens on a band (Lemma 1.1).

**Corollary 3.3 (coordinator's (c); PROVED).** Assume T is gated, in a gate union or a design as in Prop 2.6(a). Then no model whose disagreement with T contains, off a bounded set, refinement cones at two vertices of M can dominate **any** rival through the ranking. Such models include:
- the combined cuts;
- every refinement missing two vertices (PP45 Cor 3.3).

*Proof.* By Prop 3.2 the carrying realiser M has the same cones. PP45 Lemma 2.2 at both vertices produces B_1, B_2 and B_3 for the pair (T, M), so M cannot be gated. Thm 2.5 removes T's uniqueness under (R0). ∎

So the two-corner rival **must** be dominated by a model near T (Lemma 2.4) that misses at most one vertex, or that is not a refinement at all. In the tripod, that leaves caps at i or j that do not contain their piece (PP45 Prop 4.1). PP45's numerics find no tripod dominator for the four two-corner rivals tested. I have no proof that none exists; OPEN.

**Proposition 3.3′ ((IB) transfer: what a domination at i costs; PROVED).** Take any design in which some N covering both pieces had N ⪯_i X. Then (TC) and (IB) force, for every gated M′ silent on H_j(r_j):

  Φ^{M′}_i(H_j(r_j): S → σ_j) ≤ 0   (< 0 under (R0)),

and in particular T ⋠_i C^j_{r_j}. The same holds with i and j exchanged, and T ⋠_k N.

*Proof.* X ≺_i C^i_{r_i} by guidance. The record C^i_{r_i} → N equals, by (IB), every copy (H_j(r_j): S → σ_j). Prop K's triangle then refuses it. ∎

These are compatible with ℓ^T's own signs (PP42 Lemma 4.1(iv)). So single-cap defences give no **additional** conflict. The conflict is Cor 3.3.

**Corollary 3.4 (independent of the type test; PROVED under (U)).** A fixed covering combined cut D dominates X only if ∫_{G_i ∪ G_j} env ≳ λ_T·Φ^T(T → D)/κ (Lemma 2.4). So D could serve only two-corner rivals that are large relative to D. Small rivals need dominators converging to T, which brings back Cor 3.3.

---

## 4. Question 3: is the interval test tight?

### 4.1 Strict gates (R): yes (Thm R1, referee; independent proof)

Assume CG2 for every pair, so that by Lemma 1.3, (TC) ⇔ no accepted nontrivial triangle.

1. **Achievable links.** Fix an ordered triple of gates (N_1, N_2, N_3). The achievable link vectors (ℓ_1, ℓ_2, ℓ_3) of triangles P → Q → R → P whose links N_1, N_2, N_3 realise form a convex set V, by Lyapunov on bounded sets.
2. **Gordan.** V misses the open positive orthant ⇔ there is κ ≥ 0, κ ≠ 0, with κ·v ≤ 0 for a.e. pointwise vector v.
3. **Two-valued points.** At a point where N_m is the odd member, the pointwise vectors are exactly the two pairwise CG2 vectors for (N_m, N_l), l ≠ m. So the condition is: common κ ≥ 0 satisfying all three pair sandwiches.
4. **Positive constants.** Zero constants can occur only if some pair's disagreement is one-signed at w, that is, AΔB = {w}. A zero constant then forces another, unless all three pairs are one-signed. Fully one-signed triples impose no cycle constraint (the half-line intervals always close).
5. **Conclusion.** The closed interval-triangle test with positive constants is exactly (TC).

### 4.2 Zero-accepting gates (R0): the exact test (new)

**Theorem 4.1 (PROVED; CHECKED `tc_r0_47.out`).** Two-valued family, (R0), (BR), and strict CG2 a.e. for every pair (which (R0) needs anyway for strict dominations, PP42 Thm 3.2(c)). Then (TC) at w holds iff, for every triple:
- **(a)** the closed interval cycle test holds with positive constants; and
- **(b)** if the cycle is tight in an orientation (the sum of the three relevant bounds is 0, which forces κ up to scale), then at least one of the three bounding essential extrema is **not attained** on a non-null set.

*Proof.*
1. **Reduction.** By Lemma 1.3 (strict case), (TC) ⇔ no nontrivial triangle has all three link values ≥ 0.
2. **(a) is necessary.** If it fails, Gordan gives a triangle with all links > 0.
3. **The tight attained case fails (TC).**
   - The forced κ is positive.
   - At points of the three attained sets, the pointwise vectors lie on the rays (κ_B, −κ_A, 0), (0, κ_C, −κ_B) and (−κ_C, 0, κ_A), all with one orientation, because tightness is of one sum.
   - These sum to 0 with positive weights (κ_C/κ_B, κ_A/κ_B, 1). Exact masses on the three sets give a nontrivial triangle with ℓ = 0.
   - (R0) accepts it, and by Lemma 1.3 every reverse is refused.
4. **Sufficiency when not tight.** Choose κ in the relative interior of the feasible set. Every pair inequality is then strict a.e., unless a pair interval is degenerate, which strict pair CG2 excludes. So every nontrivial triangle has κ·ℓ < 0.
5. **Sufficiency when tight with an unattained bound.** That pair is strict a.e. for the forced κ. Pointwise vectors with κ·v = 0 then lie on at most two of the three rays. Those rays are linearly independent, and no positive combination of them, or of them with vectors having κ·v < 0, is ≥ 0 except the trivial one. ∎

**CHECKED (`tc_r0_47.out`).** The family is T, C^i, C^j at a two-signed world; the pair intervals are R_AB, R_AC ∈ [1, 2].
- **Ex1, tight with all extremes attained** (R_BC ∈ [2, 3]). There is an exact zero triangle through gates (A, B, C), with pieces 3/4 on Q1a, 27/28 on P2a and 1 on Q2a.
  - All three links are exactly 0.
  - Every reverse is refused: link 1 has no realiser; link 2 is refused by C at −3/4; link 3 by A at −3/4 and by B at −3/8.
  - No positive triangle exists, so (R) is fine and (R0) is not.
- **Ex2, slack** (R_BC ∈ [3/2, 3]). The LP finds no triangle with links ≥ 0 for any gate order.
- **Ex3, the closed test fails** (R_BC ∈ [5/2, 3]). There is an exact triangle with links (1/22, 1/22, 1/22) and all reverses refused.

**Answer.** Failure of the closed test is always a forbidden configuration, under (R) and under (R0). Under (R0) a tight triple with attained extremes is one too, even though the closed test passes. The audit's open-interval strict test is sufficient but stronger than needed: a tight triple with one unattained extreme is (TC)-safe. Since Lemma S requires (R0), **the design target for the box is Thm 4.1, not the closed test alone**.

---

## 5. The eight-model box

**Status.** With T gated, the gated part of the box is at most {T, three single caps} (PP45 Cor 3.2). By Thm 2.5 this holds under (R0) without T's uniqueness. The double cuts fail through the B-families, and the full cut also fails through the A-families (Thm 2.7). Pairs within the tripod pass the type test, and the box's triple conditions are moot. Consequences:
- The audit's "fields on the parameter box" cannot exist as gated fields in a gate union.
- Lemma S's Θ cannot be the closed box. It can be the tripod (PP45 Thm 5.1(iii)).
- No 2-D gated family through T exists in the box. The 2-D selection must collapse onto a 1-D tripod.

That is compatible with Cor 2.3, but it leaves the weight-simplex dimension unmatched (PP45 §4, CONJECTURE).

**Nearby reachable aims (per the brief's preference).**
- **(i) Tripod plus tilt.** Single-vertex cuts of variable tilt. They pass the type test against T (PP45, necessary test only) and give a 2-parameter family per vertex. Every T-fill and every two-corner rival must then be dominated from within it (Cor 3.3).
- **(ii) Restricted two-vertex modifications that are not refinements.**

  **Proposition 5.1 (order level; PROVED).** A model D_K disagreeing with T near m_i and m_j passes PP45's order test against T if, for example:
  - its refinement points near m_i carry only the families {A_i, B_j};
  - those near m_j carry only {B_i};
  - its "T answers, D_K silent" points carry no family whose swapped reading excludes the order k > i > j.

  The constraints are:
  - "i not bottom" (from A_i);
  - "j not top" (from B_j);
  - "i not top" (from B_i).

  The order k > i > j satisfies all three.

  For refinements this is impossible (PP45 Cor 3.3: every small corner at a missed vertex shows all three families). For K ⊄ M, a point of K outside M near m_j blocks every separating line through m_j of the wrong edge ratios. So the families at m_j can be restricted.

  CONJECTURE: such K exist with the required family sets, coherent and close to M. Every K, being convex, gives a coherent model. Lemma 2.4 requires K_n → M.
- **(iii) Non-additive bounded verdicts** (Prop 2.6(c)). A separately labelled branch with its own (TC) and section proofs (audit item 3).

---

## 6. Status and scripts

| Result | Label |
|---|---|
| Lemma 1.1 (bands, strips) | PROVED (PP45); CHECKED `geom47` |
| Lemmas 1.2, 1.3 | PROVED |
| Prop 2.1, Prop 2.2, Cor 2.3, Lemma 2.4 (under (U)) | PROVED |
| PP45 Thm 3.1 audit: correct; Thm 2.5 removes the uniqueness loophole under (R0) and at the (R) checkpoint | PROVED; algebra CHECKED `fullcut47` (v) |
| Thm 2.7 (full cut from A-families) | PROVED; CHECKED `fullcut47` (i)–(iv) |
| Prop 2.6 (lexicographic bounded-additive gates; ungated dominators) | PROVED |
| Props 3.1, 3.2, 3.3′, Cors 3.3, 3.4 | PROVED (3.4 under (U)) |
| Tripod dominators of two-corner rivals | OPEN (PP45 numerics: none found) |
| Thm R1 re-derived (strict gates) | PROVED |
| Thm 4.1 (exact (R0) test, two-valued) | PROVED; CHECKED `tc_r0_47` |
| Prop 5.1 order level / its geometric realisation | PROVED / CONJECTURE |

**Scripts** (`r9/PP47_py/`; run `python3 -I -B <script> > <script>.out` inside the folder; all ALL PASS):

| Script | Content |
|---|---|
| `geom47.py` | Union lemma and two-valuedness (7,033 problems × 8 models); band patterns with all three families (12 cases); exact strict A-family witnesses in 24 strips. Floats only propose; Fractions verify. |
| `fullcut47.py` | Thm 2.7's per-band criterion (4,044 failing bands re-verified on random sector vectors); never all three bands (4,000 pairs); explicit two-band example; mixed-kind criterion; zero-sum lemma (2,000 instances, exact). |
| `tc_r0_47.py` | Thm 4.1, Ex1–Ex3: the LP proposes; every triangle is rebuilt in Fractions and checked against all realisers and guidance. |

**Most important next step.** Under (R0), test aim (i) against the two-corner rival with Thm 4.1 as the (TC) criterion. Concretely: the 2-parameter tilted single-vertex family, fields jointly designed, and the two-corner rival's dominator taken as a tilted cap at i or j that does not contain its piece. If that fails, decide between aim (ii) and the separately labelled non-additive branch (iii).
