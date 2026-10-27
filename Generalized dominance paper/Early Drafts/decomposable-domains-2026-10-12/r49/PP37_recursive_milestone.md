# PP37. The recursive milestone: support-gated potentials, ties versus sections, and the first recursive constraint

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: complete argument here. CHECKED: exact rational computation on sampled problems (no cells are used). NUMERICS: Gaussian Monte Carlo; no proof depends on it. CONJECTURE / OPEN: as stated.

**Scripts** (`r9/PP37_py/`; run `python3 -I -B <script>` inside the folder; outputs in `.out` files):

| Script | Content | Label |
|---|---|---|
| `levels37.py` | Balance identity on every sample; the leading levels L⁰(N) − L⁰(T) for V_1–V_3 and 231 edge models (Lemma 1.2) | balance CHECKED pointwise; values NUMERICS (they match the exact values of Lemma 1.2) |
| `edgegate37.py` | Theorem 4.1's ratio condition against the band predicate of Cor 4.2, for 190 edge models on 6,000 exact rational problems in Sil(T); PP32 Lemma 1.1(i) | CHECKED, ALL PASS |

**Inputs.** Brief 49; AUDIT_round49_brief and AUDIT_round49_answers (binding); PP33 (Thm 3.1, domination geometry); PP34 ((CC), silent-wedge dominators); PP36 (Prop K, Lemma E, Prop SD); PP30 (Thm 3.1), PP32 (Lemmas 1.1, 2.1–2.3, Prop 2.4), REFEREE_PP32 (Cor A′); PP23 (Lemma 1.1, Ω), PP25 (Thm A, rule L); PP28, PP29; AUDIT_completion (rules I–IV, F1/F2); AUDIT_selected_realizability §4; REFEREE_Z_PP19 (Lemma H); LEAD_selection_count (Lemmas A, B, E); the coordinator's round-48 referee summary (§8). Only Brief 49's axioms are used. Every extra hypothesis is named where it is used.

---

## 0. Verdict

**The milestone is not reached. Here is the furthest point, with the obstruction that stopped each design, and the one design pattern that survives.**

1. **Universal competitiveness is solved, for every registered model of every generation (Theorem 3.1, PROVED).**
   - Each world accepts a record if it is guidance, an installed domination, or passes the *gate* of some registered model whose old side it is.
   - Full-support models use PP25's balanced potential L. Edge models use a two-world balanced edge potential E. Vertices use guidance.
   - Every registered model is then competitive against every measurable rival, bounded or not, on its own support.
   - This holds automatically for every new defender. Registration never threatens a model's own defence.
   - It fixes the defect of PP23/PP25 at the edges (R46.1) without using a Bayes-adapted (CPM-type) field: each gate is balanced.
2. **(TC) is localised (Theorem 3.2, PROVED).** Every (TC) violation needs an installed domination, or records from two different gates. World 3 is clean apart from dominations.
3. **The first cross-gate configuration is solved exactly (Theorem 4.1, Cor 4.2, Prop 4.3, PROVED).**
   - The configuration is PP30's: T accepts T[G ↦ D] for an edge model D, and D's improved retreat closes a pure improvement.
   - It is harmless iff the edge potential satisfies a ratio sandwich against L.
   - For a rank-linear edge potential that makes D competitive, this forces every non-vertex edge model's silent window to reach an end of the band J = (α, β). This is REFEREE_PP32's Cor A′, now forced by (TC) through PP30's kill instead of by single-field endorsement.
   - An explicit edge gate and an explicit continuous edge family pass it.
4. **The obstruction: ties against sections (§5, PROVED).** A potential gate must say what it does with records of value zero.
   - **Strict tie-breaking (lexicographic, as in PP23/PP25/PP33) is incompatible with closed sections on the path** (Theorem 5.1). It forces every path model to equal T, and then T's tie fibre reaches the boundary, against LEAD Lemma E.
   - **Accepting every zero-value record at every world creates an all-world tie between T and an incoherent splice** (Prop 5.5): F2, so direct (C) fails.
   - **Mixed patterns** (strict at some worlds only): **exactly one survives** (Theorem 5.6). It is strict at exactly one edge world w₀ ∈ {1, 2}. Along the whole path, every registered model must have the same world-w₀ level as T: L⁰_{w₀}(C) = 1 (*iso-level*).
   - On the edge the gate must be non-strict at both worlds (Prop 5.2).
   - Classification: the commitment responsible is *"the gate's verdict is a function of one potential's sign, with a uniform zero rule per world"*. Within that class nothing else escapes.
5. **The first recursive constraint (§6, PROVED).** A *realised* form of PP33 Thm 3.1 (Prop 6.1): a dominator C of a vertex retreat V_j[G′ ↦ S] is killed whenever some registered model C₂ is silent on G′ and agrees with V_j, inside {C ≠ V_j}, on more gate mass than G′ carries.
   - With C₂ = T this is a budget: C = V_j on {T = V_j} up to the mass of G′.
   - With later defenders as C₂, the forced agreement **accumulates over generations** (Cor 6.3).
   - Small V_3-retreats (V_3 is the vertex off the edge) can be dominated only by path models. Under Theorem 5.6 these must also be iso-level.
6. **Where I stopped (§7).** I have no proof that the iso-level path, the accumulating agreement constraint and the remaining cross-gate configurations can all be met for all generations. I also have no contradiction.
   - **Exact open step:** a family of coherent full-support dominators that are iso-level at w₀, agree with V_j wherever a registered model silent on their piece agrees with V_j, and close under their own forced rivals.
   - The candidate is refinements of T (credal sets inside M), which meet the generation-0 constraints exactly (Remark 6.4). This is CONJECTURE.

| Item | Status |
|---|---|
| Universal competitiveness, all registered models, all generations (Thm 3.1) | PROVED |
| (TC) localisation (Thm 3.2); single-gate safety with symmetric zero rule (Lemma 3.3) | PROVED |
| PP30 cross configuration: exact condition, band condition, explicit gate (Thm 4.1, Cor 4.2, Prop 4.3) | PROVED; CHECKED |
| Strict path gate impossible (Thm 5.1); edge gate must be non-strict (Prop 5.2); junction inequality (Prop 5.4); non-strict everywhere gives F2 (Prop 5.5); classification (Thm 5.6) | PROVED |
| Realised retreat kill and budget (Prop 6.1, Cor 6.2, 6.3) | PROVED |
| Dominators for all generations; all cross-gate configurations; sections with installed records | OPEN |
| Refinement dominators close the recursion (Conj 7.1) | CONJECTURE |

So the milestone fails at the same place for every design of the stated kind: closing sections while handling value-zero records. The surviving pattern (Theorem 5.6) is the nearby target, and §7 states what remains to prove for it.

---

## 1. Setting, milestone, notation

Brief 49's setting is used throughout.
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; the full four-advice domain, models modulo null sets.
- Ranks: correct 0 < silent 1 < wrong 2 < contradictory 3. Classes M_1, M_2, M_3; U is the unanimous set.
- T = D_M with M = c·1 + εΔ. Sil(T) is T's silent cone. W_12 := M_1 ∪ M_2, and θ := |g_2|/|g_1| on W_12.
- Band: α := c/(c+ε), β := 1/α, J := (α, β). By PP32 Lemma 1.1, θ < β on Sil(T) ∩ M_1 and θ > α on Sil(T) ∩ M_2, and both bounds are sharp.
- Records, copies, P1/P2: as in PP23 Lemma 1.1. (TC) is equivalent to "every accepted triangle has all three reverses" (AUDIT_completion §2).

**The milestone (audit, binding).** The index domain I contains:
- p_T, the three vertices, the complete edge [e_1, e_2];
- a path γ from p_T to that edge;
- all limit points.

Every registered model gets an index in I. Required:
- **Universal competitiveness:** every registered model is competitive on the support of its index against every measurable rival.
- **Closed sections:** for every measurable rival, A_w(X) ∩ I is closed in I.
- **Repair class:** explicit coherent dominators for the repair class.
- The other axioms, including direct (C). F1 and F2 must not occur.

**Path hypothesis (H_path).** The path γ lies in int Δ except for its endpoint q_e, which is an open-edge point of [e_1, e_2] or one of e_1, e_2. Put J := γ ∖ {q_e}. It is connected, and q_e is in its closure. This is the natural choice of domain. Theorem 5.1 needs only that some connected set of interior path indices containing p_T has a boundary point in its closure. Props 5.2–5.4 use (H_path) as stated.

**The leading level.** ρ_w := 2 on M_w and 1 elsewhere (PP25). For a model N put L⁰_w(N) := ∫ ρ_w r_w(N) dμ, and for a record r put Λ⁰_w(r) := ∫_{supp r} ρ_w δ_w dμ. This is finite for every record, bounded or not, because ρ is bounded and μ is finite. For a fixed countable π-system (B_n) of bounded Borel sets generating the Borel sets, with B_0 := R³, the n-th level is Λ⁽ⁿ⁾_w(r) := ∫_{B_n} ρ_w δ_w dμ.

**Lemma 1.1 (balance; PROVED, PP25).** For a coherent N and every g, Σ_w ρ_w(g) r_w(g, N(g)) = 4 if g is mixed and 0 if g ∈ U. Hence Σ_w L⁰_w(N) = 4μ(mixed) = 3 for every coherent N, and likewise Σ_w (level n) = 4μ(B_n ∩ mixed). For any record out of a coherent model, Σ_w ρ_w δ_w ≥ 0 pointwise, with equality on mixed changes among A, S and B. (CHECKED pointwise on all samples, `levels37.out` (a).)

**Lemma 1.2 (exact leading levels; PROVED).** L⁰_w(T) = 1 for every w. For every edge model D on [e_1, e_2], including V_1 and V_2, L⁰_3(D) = 3/2. Also L⁰_j(V_j) = 0 and L⁰_w(V_j) = 3/2 for w ≠ j.

*Proof.*
- **T.** Each mixed class has μ-mass 1/4 and U has mass 1/4 (orthant symmetry). By Lemma 1.1 the three levels of T sum to 3. T and μ are invariant under permuting coordinates, so each level is 1.
- **Edge models.** On M_3, D says A, which is 3-wrong, contributing 2·2·(1/4) = 1.
- **The map φ(g_1, g_2, g_3) := (g_1, g_2, −g_3).** It preserves μ, maps M_1 onto M_2, and preserves θ. D's answer on W_12 depends only on θ: 1-correct, silent or 2-correct, on both classes.
- **Pairing.** At world 3 (ρ_3 = 1 on W_12), the ranks at g and φ(g) sum to 2 in each case:
  - 1-correct is B on M_1 (3-wrong) and A on M_2 (3-correct);
  - silence gives 1 + 1;
  - 2-correct is A on M_1 (3-correct) and B on M_2 (3-wrong).

  So W_12 contributes μ(W_12)·1 = 1/2, and U contributes 0.
- **V_j.** It is j-perfect, so L⁰_j(V_j) = 0. The other two values follow from the same pairing. ∎

NUMERICS (`levels37.out`): every edge model in the grid gives L⁰_3(D) − L⁰_3(T) = 0.50 ± 0.006, and the vertex values agree with the lemma.

**Facts used repeatedly** (LEAD_selection_count; REFEREE_Z_PP19):
- **Lemma A.** Tie fibres are closed.
- **Lemma B.** C_{e_i} = V_i, and V_i has no all-world tie.
- **Lemma E.** No boundary index is tied with T.
- **Lemma H.** A splice on a set that is not a.e. a cone is incoherent.

All three lemmas hold relative to I, since their proofs use only sections at indices of I.

---

## 2. Why the systematic rule cannot be one potential per world

**Proposition 2.1 (PROVED; from PP32 Lemma 2.3 and R46.1).** Suppose each world's accepted records out of registered models are endorsed by one strictly guiding additive potential per world (ρ_w-integrals, or lexicographic stacks with that leading level), and every registered model is universally competitive. Then:
- every registered model at index p is pointwise Bayes, for some weight supported in supp p, for the leading fields;
- if those fields are balanced (as L is), every non-vertex edge model fails competitiveness on {1, 2} (R46.1; PP28 §6.2's B-ward trade has values (−m, −m, 2m));
- if they are not balanced, the registered family is a family of Bayes acts of one field, i.e. a CPM-type realisation, which Brief 49 excludes. For rank-linear fields it is also impossible with T and a complete edge (PP32 Thm 3.1).

*Proof.* The first bullet is Lemma 2.3 of PP32 applied to each registered model with Q equal to the whole space. The other two are the cited results. ∎

So the rule must use **more than one potential at a world**, and then (TC) is no longer automatic. §3 does this in the least damaging way: the potential is chosen by the *realiser* of the old side.

---

## 3. Support-gated potentials

**Definition (design Γ).** Fix the registered family P (finite or not, growing by generations), each member C with its index p(C) ∈ I. Each member carries a **gate**:
- **Full-support members** (p in int Δ) carry the L-gate at worlds {1, 2, 3}, with density ρ.
- **Edge members** (p in the open edge) carry the E-gate at worlds {1, 2}. E is a rank-linear potential with bounded densities σ_1, σ_2 > 0, *two-world balanced on W_12*: σ_1 = σ_2 there. Hence σ_1δ_1 + σ_2δ_2 = 0 for changes among A, S, B on W_12.
- **Vertex members** carry no gate (guidance only).

For a gate with density φ at world w, write Φ_w(r) := ∫_{supp r} φ_w δ_w dμ. Each gate has a *zero rule* at each of its worlds: **strict** or **symmetric**.

A record r is **accepted at w** iff one of the following holds:
1. r is a weak w-worsening (guidance);
2. r is a copy of an installed domination record;
3. there is a member C whose gate acts at w such that either
   - Φ_w(r) > 0 and C realises the old side (C = old side a.e. on supp r); or
   - Φ_w(r) = 0, the zero rule at w is symmetric, and C realises the old side or the new side.

Installed records are rec(C, Z) for a member C and a repair-class rival Z, accepted at all worlds. By design each is **unbounded** and is a pure improvement at no world.

**Theorem 3.1 (universal competitiveness; PROVED).** In Γ:
- strict (G) and (IB) hold;
- every member is competitive on its support against every measurable rival, provided the L-gate is not strict at all three worlds and the E-gate is not strict at both edge worlds.

This holds for every family P. So it holds at every generation, and for every new defender at the moment it is registered.

*Proof.*
- **(IB).** Each clause depends only on the record, given P.
- **Strict (G).** Guidance is accepted. A nontrivial pure w-improvement has Φ_w < 0 for every gate (positive densities), so no gate accepts it; installed records are never pure improvements.
- **Full-support member N, rival Y.** By Lemma 1.1, Σ_w Λ⁰_w(rec(N, Y)) ≥ 0. If some value is > 0, the L-gate of N accepts there. Otherwise all three values are 0, and some world has a symmetric zero rule; N realises the old side, so that world accepts.
- **Edge member N.** N says A a.e. on M_3 (PP32 Lemma 2.1), which is correct at worlds 1 and 2. So σ_1δ_1 + σ_2δ_2 ≥ 0 pointwise for records out of N:
  - on W_12, changes among A, S, B give 0;
  - on M_3 and U, N is correct at both worlds;
  - contradiction raises both ranks.

  So E_1 ≥ 0 or E_2 ≥ 0, and the same case analysis applies.
- **Vertex member.** Guidance at its world. ∎

**Lemma 3.3 (one gate is (TC)-safe; PROVED).** At a fixed world w, guidance together with the acceptances of a single gate has no (TC) violation.

*Proof.*
- **(P1).** Accepted records have Φ_w ≥ 0 (guidance included), and Φ_w adds along composition of copies. A nontrivial pure improvement has Φ_w < 0. So no two accepted records compose to one.
- **(P2).** Around an accepted triangle Φ_w sums to 0, so every edge has Φ_w = 0. A guidance edge with value 0 is trivial. So every nontrivial edge was accepted under the symmetric zero rule, and one of its sides is realised.
- **Reverses.** The reverse of such an edge has value 0, and its new side is the forward edge's old side (and vice versa). So the reverse is accepted under the symmetric zero rule. ∎

A strict zero rule is safe trivially: no nontrivial triangle is accepted at all.

**Theorem 3.2 (localisation; PROVED).** Every (TC) violation at world w in Γ involves an installed record, or records accepted only through two different gates. At world 3 there is one gate (L), so every violation there involves an installed record.

*Proof.* By Lemma 3.3. ∎

So the recursive task is exactly:
- **(a)** cross-gate configurations L/E at worlds 1, 2;
- **(b)** configurations through installed dominations;
- **(c)** sections.

---

## 4. The first cross-gate configuration: T's fill by edge answers

Fix a non-vertex edge member D and w ∈ {1, 2}. In Sil(T) ∩ Ans(D), let C_w(D) be the set where D is w-correct and R_w(D) the set where D is w-wrong. For bounded G ⊆ Sil(T) ∩ Ans(D) write G^c := G ∩ C_w(D) and G^r := G ∩ R_w(D). Put:
- x_G := (G, S → D), the record of T ⪯_w T[G ↦ D];
- y_{G,E} := rec(D, D[G ↦ S, E ↦ w-correct]), for non-null E ⊆ G.

x_G · y_{G,E} is the pure improvement (E, S → w-correct) out of T (PP30 Thm 3.1). The L-gate of T accepts x_G at w iff ρ_w(G^r) ≥ ρ_w(G^c); write > instead at a strict world.

**Theorem 4.1 (exact condition; PROVED).** The following are equivalent:
- (i) no configuration (x_G accepted at w, y_{G,E} accepted at w) occurs, for any G and E;
- (ii) ess sup over C_w(D) of σ_w/ρ_w ≤ ess inf over R_w(D) of σ_w/ρ_w (each side vacuous if its set is null).

*Proof.*
- **Values.** E_w(y_{G,E}) = [σ_w(G^c) − σ_w(G^r)] − σ_w(E), and Λ⁰_w(y_{G,E}) = [ρ_w(G^c) − ρ_w(G^r)] − ρ_w(E). (Bookkeeping: correct → S costs +1, wrong → S gains 1, wrong → correct gains 2, and correct → correct is no change.)
- **(ii) ⇒ (i).** If T accepts x_G, then ρ_w(G^r) ≥ ρ_w(G^c). By (ii), σ_w(G^r) ≥ κρ_w(G^r) ≥ κρ_w(G^c) ≥ σ_w(G^c), with κ between the sup and the inf. So both values are ≤ −(mass of E) < 0. Every realiser of y_{G,E} applies one of these two record-based values, so all gates refuse it.
  - y_{G,E} is bounded, so it is not installed.
  - It is guidance only if G^r is null, and then T refuses x_G.
- **(i) ⇒ (ii).** Suppose a < b, with σ/ρ ≥ b on a non-null A ⊆ C_w(D) and σ/ρ ≤ a on a non-null B ⊆ R_w(D). By atomlessness choose bounded A′ ⊆ A and B′ ⊆ B with ρ_w(B′) = (1+η)ρ_w(A′), where (1+η)a < b. Put G := A′ ∪ B′.
  - T accepts x_G, since ρ_w(G^r) > ρ_w(G^c).
  - σ_w(G^c) − σ_w(G^r) ≥ bρ_w(A′) − aρ_w(B′) > 0.
  - For small E ⊆ G^c, E_w(y_{G,E}) > 0, so D's E-gate accepts y_{G,E}: a P1 violation. ∎

**Corollary 4.2 (band condition; PROVED).** Suppose D is E-Bayes at some edge weight (a, b), for instance because its defences on Sil(T) ∩ W_12 come from its E-gate. If (ii) holds at both worlds, then the window (τ_0, τ_1) of D reaches an end of the band: τ_0 ≤ α or τ_1 ≥ β.

*Proof.*
- **Edge-Bayes (PP32 Prop 2.4).** With φ := σ_2/σ_1 and κ := a/b: φ ≤ κ where D is 1-correct and φ ≥ κ where D is 2-correct.
- **Combine with (ii) at both worlds** (constants κ_1, κ_2). At 1-correct points, φ ≥ (κ_2/κ_1)(ρ_2/ρ_1). At 2-correct points, φ ≤ (κ_2/κ_1)(ρ_2/ρ_1). With c′ := κκ_1/κ_2 this gives ρ_2/ρ_1 ≤ c′ at 1-correct points of Sil(T) and ρ_2/ρ_1 ≥ c′ at 2-correct points.
- **The ratio ρ_2/ρ_1** is 1/2 on M_1 and 2 on M_2.
  - If τ_0 > α, D is 1-correct on part of Sil(T) ∩ M_2, so c′ ≥ 2.
  - If τ_1 < β, D is 2-correct on part of Sil(T) ∩ M_1, so c′ ≤ 1/2.
- These cannot both hold. ∎

This recovers REFEREE_PP32's Cor A′ (windows reach an end of the band), but now **forced by (TC) through PP30's kill, with T judged by a different potential from the edge**. Single-field endorsement is not used. The rank-linear hypothesis on E is essential (REFEREE_PP32 §3.2).

**Proposition 4.3 (an explicit edge gate and edge family; PROVED; CHECKED).** Put σ_1 = σ_2 = 1 on W_12 ∪ U and σ_1 = σ_2 = 1/2 on M_3. Then:
- (a) every model that is A a.e. on M_3 and U-correct is E-competitive on {1, 2};
- (b) condition (ii) holds for D iff τ_0 ≤ α or τ_1 ≥ β;
- (c) there is an edge selection q ↦ D_{K(q)}, continuous in measure, that meets the edge-covering lemma (PP32 Lemma 2.2) and in which every non-vertex model satisfies (b).

*Proof.*
- **(a)** is Theorem 3.1's edge argument.
- **(b) The ratios σ_w/ρ_w.**
  - At world 1: 1/2 on M_1 and on M_3, and 1 on M_2.
  - At world 2: 1 on M_1, 1/2 on M_2 and on M_3.
  - **World 1.** C_1(D) consists of M_3, the low-θ part of M_1, and the low-θ part of M_2 when τ_0 > α. R_1(D) consists of the high-θ part of M_2, and the high-θ part of M_1 when τ_1 < β. So the sandwich fails exactly when M_2-points lie in C_1 and M_1-points lie in R_1, i.e. when τ_0 > α and τ_1 < β.
  - **World 2** is symmetric.
- **(c) Parametrise by τ_q**, the θ-threshold of the edge point q:
  - **τ_q ≤ α:** take the precise model D_q.
  - **α < τ_q < β:** take the segment with thresholds (α, τ_q).
  - **β ≤ τ_q ≤ β′ (fixed β′ > β):** take thresholds (α + (τ_q − β)(β′ − α)/(β′ − β), τ_q).
  - **τ_q > β′:** take D_q.

  The thresholds vary continuously, so the models vary continuously in measure (the disagreement sets are wedges of vanishing angle). Each K(q) contains q, and each window satisfies (b). ∎

CHECKED (`edgegate37.out`): on 6,000 exact rational problems in Sil(T), for all 190 grid edge models, condition (ii) at both worlds coincides with the band predicate. ALL PASS.

**Remark 4.4 (the coordinator's item (3)).** Corollary 4.2 does not use PP34 Prop 4.1(f). Edge models giving both answers on a one-class piece of Sil(T) are covered: C_w(D) and R_w(D) may meet one class.

---

## 5. Ties against sections

The gates of §3 still need a zero rule at each world. This section shows that the choice is almost forced, and that the standard choice (lexicographic strictness) is fatal.

Write a_w(q) := L⁰_w(C_q) for q ∈ J, and a⁽ⁿ⁾_w(q) for the n-th level.

**(H4).** No member at an index of J is A a.e. on M_3. Equivalently, no full-support member has its credal set inside the edge, by the argument of PP32 Lemma 2.1(ii). This hypothesis is used only at strict worlds 1 and 2, to stop an E-gate from also accepting the test records. It is not needed at world 3, where no E-gate acts.

**Test records (PROVED).** Fix q₀ ∈ J and a world w.
- **(T1)** There are bounded records out of C_{q₀} with any small prescribed negative value at w. One can take pure w-improvements, which every mechanism refuses.
- **(T2)** For any n, there are bounded records r out of C_{q₀}, supported in M_3 ∩ {C_{q₀} ≠ A}, with:
  - levels 0, …, n at w equal to 0;
  - first nonzero later level negative.

  *Construction.* Take a cell Q of the algebra of B_0, …, B_n, meeting P := M_3 ∩ {C_{q₀} ≠ A} non-nully. Let m > n be the first index whose B_m splits Q ∩ P; it exists because (B_n) generates the Borel sets and μ is atomless. On both pieces, C_{q₀} has S or B, so each piece admits a gaining change and a losing change at w; if needed, change to contradiction for the loss. Put a gaining change on a piece inside B_m and a losing change of equal ρ_w-mass on a piece outside it.

  Such an r is refused at w by every L-gate (the value is record-based), by every E-gate (no edge member realises it, since edge members are A on M_3), by guidance (it has a gain), and is not installed (it is bounded).

**Theorem 5.1 (strict path gates are impossible; PROVED).** Suppose the L-gate is lexicographically strict at every world: it accepts iff (Λ⁽ⁿ⁾_w)_n ≥_lex 0, with nontrivial values never zero. Assume (H4). Then sections cannot all be closed relative to I.

*Proof.*
- **Step 1 (local minima, level n).** Suppose levels below n are constant on J, and suppose q_m → q₀ in J with a⁽ⁿ⁾_w(q_m) < a⁽ⁿ⁾_w(q₀). Take r from (T2) and X := C_{q₀}·r. For each m, the record rec(C_{q_m}, X) has:
  - levels below n: a(q₀) − a(q_m) = 0;
  - level n: a⁽ⁿ⁾_w(q₀) − a⁽ⁿ⁾_w(q_m) > 0.

  So C_{q_m}'s own gate accepts it, and q_m ∈ A_w(X). Closedness gives q₀ ∈ A_w(X), but r is refused. Contradiction. Hence every point of J is a local minimum of a⁽ⁿ⁾_w, relative to J, for each w.
- **Step 2 (constancy).** Σ_w a⁽ⁿ⁾_w is constant (Lemma 1.1). So each a⁽ⁿ⁾_w is also a local maximum (the other two are local minima). A locally constant function on the connected set J is constant. By induction on n, all levels of C_q equal T's, so C_q = T a.e. for every q ∈ J (π–λ).
- **Step 3.** Φ_T ⊇ J, and Φ_T is closed in I (Lemma A). The closure of J contains a boundary index b, so C_b ≈ T. That contradicts Lemma E (edge index) or Lemma B (vertex). ∎

The same argument works for any record-based strict refinement of the sign of Λ⁰ that refuses some zero-level record out of each path model at each world.

**Proposition 5.2 (the edge gate must be non-strict at both edge worlds; PROVED).** Use (H_path). Assume edge members' records are accepted at worlds 1, 2 only through E-gates, guidance or installed records (call this (H_E)). Suppose E is balanced on W_12 at some edge weight and strict at some edge world. Then sections cannot be closed.

*Proof.*
- **Regularity.** Write b_w(q) := E⁰_w(C_q) on the open edge minus q_e.
  - At a strict world, the argument of Theorem 5.1, Step 1, makes every point a local minimum. The test record is any nontrivial record out of C_{q₀} with E⁰_w = 0 and a w-gain. It is refused at w by every E-gate (zero value, strict rule), by guidance, and by (H_E) by everything else.
  - At a non-strict world, (T1)-records make b_w lower semicontinuous: if b_w(q_m) ≤ c < b_w(q₀), a pure improvement out of C_{q₀} worth c − b_w(q₀) gives the contradiction.
  - λ_1b_1 + λ_2b_2 is constant, so both b_w are continuous. The strict one is then constant on each component, and so is the other.
- **The component U adjacent to e_1.** Let its values be (c_1, c_2).
  - **If U carries V_1 somewhere,** U carries only V_1. Indeed an edge model whose world-2 level equals V_1's is 2-wrong a.e. on W_12 and A on M_3, so it equals V_1.
    - Lemma A puts the far end of U in Φ_{V_1}. If q_e is a vertex, that end is e_2, and V_2 = V_1 is absurd.
    - Otherwise C_{q_e} = V_1 (Lemma B). On the component next to e_2, either every model is V_2 (then likewise C_{q_e} = V_2, absurd), or the next bullet applies at e_2 with worlds exchanged.
  - **Otherwise c_2 < E⁰_2(V_1).** Take X := V_1[F ↦ 2-correct] with F ⊆ W_12 small, so that E⁰_2(X) > c_2. Every q ∈ U accepts X at world 2 (positive value). Closedness gives V_1 ⪯_2 X, against strict (G). ∎

**Proposition 5.3 (regularity on the path; PROVED).** For any L-gate with a strict set S ⊆ {1, 2, 3} (zero rule strict exactly at the worlds of S), closed sections give:
- a_w is lower semicontinuous on J for w ∉ S (by (T1));
- every point of J is a local minimum of a_w for w ∈ S (by (T2) at level 0; this needs (H4) when w ∈ {1, 2});
- hence every a_w is continuous on J, and a_w ≡ L⁰_w(T) = 1 for every w ∈ S.

*Proof.* As in Prop 5.2: lower semicontinuous functions with constant sum are continuous, and a continuous function all of whose points are local minima is constant on a connected set. ∎

**Proposition 5.4 (junction inequality; PROVED).** For any gate that accepts positive-value records out of path models (strict or not), every world w at which C_{q_e} is w-wrong on a non-null set, and every sequence q_m → q_e in J:

  L⁰_w(C_{q_e}) ≤ liminf_m a_w(q_m).

*Proof.* Suppose not. Take X := C_{q_e}[F ↦ w-correct] with F small inside C_{q_e}'s w-errors, so that L⁰_w(X) > a_w(q_m) for infinitely many m. Those C_{q_m} accept X at w. Closedness gives C_{q_e} ⪯_w X, against strict (G). ∎

At world 3 the hypothesis always holds, and Lemma 1.2 gives L⁰_3(C_{q_e}) = 3/2. So **path models near the junction must be at least as bad at world 3 as edge models**, and **world 3 can never be strict on the path**. Otherwise a_3 ≡ 1 < 3/2.

**Proposition 5.5 (non-strict everywhere gives F2; PROVED).** Suppose S = ∅, and suppose:

**(H5)** some full-support member R ≠ T gives A on a non-null A_k ⊆ Sil(T) ∩ M_k and B on a non-null B_k ⊆ Sil(T) ∩ M_k, for some k.

Then the closure registers an incoherent model.

*Proof.*
- Take bounded A′ ⊆ A_k and B′ ⊆ B_k of equal mass, and X := T[A′ ∪ B′ ↦ R].
- The per-mass changes are S → A: (+2 at k, −1, −1) and S → B: (−2 at k, +1, +1). So rec(T, X) has Λ⁰_w = 0 at every world.
- rec(T, X) is accepted everywhere (T realises its old side). rec(X, T) is accepted everywhere (R realises its old side).
- So T ≈ X. Rule IV registers X, which is incoherent by Lemma H: F2. ∎

(H5) holds for every precise member D_m with m ∈ int M, and for every member whose credal set meets the interior of M while leaving it.

**Theorem 5.6 (classification of zero rules; PROVED, under (H_path), (H4), (H5)).** Among L-gates with a uniform zero rule per world, the only strict sets compatible with closed sections, direct (C) and the junction are S = {w₀} with w₀ ∈ {1, 2}. Then:
- every member at an index of J satisfies L⁰_{w₀}(C) = 1, the iso-level condition;
- the junction member satisfies L⁰_{w₀}(C_{q_e}) ≤ 1;
- path members near q_e satisfy liminf a_3 ≥ 3/2.

*Proof.*
- **S = ∅:** Prop 5.5.
- **3 ∈ S:** Prop 5.3 gives a_3 ≡ 1, against Prop 5.4 at world 3.
- **S = {1, 2}:** a_1 and a_2 are constant, so a_3 is constant, against Prop 5.4.
- **S = {w₀}:** consistent with all of the above. Prop 5.3 gives iso-level, and Prop 5.4 gives the two junction statements.
- **No F2:** zero records are refused at w₀, so no all-world tie passes through an L-gate. ∎

**Reading.** The obstruction is not in any particular dominator. Any potential gate has to decide value-zero records:
- refusing them breaks sections wherever path levels vary;
- accepting them everywhere ties T to splices.

The escape pays with an **iso-level path**: an invariant every registered path model must satisfy, in every generation. The commitment responsible is "one balanced potential L shared by all full-support members". Per-member balanced potentials (balanced at different weights λ) would replace the iso-level condition by cross-gate conditions between L-gates. That is the redesign left open (§7).

---

## 6. Dominations: the realised form of PP33 Theorem 3.1

**Proposition 6.1 (realised retreat kill; PROVED).** Let j be a world, G′ ⊆ Sil(T) bounded and non-null, and R := V_j[G′ ↦ S]. Let C be any model with C ⪯_j R, for instance an installed dominator. Let C₂ be a member whose gate (density φ) acts at j, with C₂ = S a.e. on G′. Put P := {C₂ = V_j} ∩ {C ≠ V_j} ∖ G′. If φ_j(P) > φ_j(G′), then (TC) fails at j.

*Proof.*
- **The set W.** Choose Q ⊆ P with φ_j(Q) > φ_j(G′) and P ∖ Q non-null. Put W := C on S′ ∖ Q and W := R elsewhere, where S′ := {C ≠ V_j} ∖ G′.
- **R ⪯_j W by guidance.** rec(R, W) = (S′ ∖ Q, V_j → C), a nontrivial j-worsening.
- **W ⪯_j C through C₂'s gate.** rec(W, C) = (Q, V_j → C) ∪ (G′ ∩ {C ≠ S}, S → C). Its old side is realised by C₂, and its value is ≥ φ_j(Q) − φ_j(G′) > 0 (C ≠ V_j on Q means rank ≥ 1).
- **The violation.** rec(W, R) is a nontrivial pure j-improvement, so R ≺_j W. Then W ⪯_j C ⪯_j R ≺_j W violates (TC). ∎

**Corollary 6.2 (budget relative to T; PROVED).** Take C₂ = T, which is silent on every G′ ⊆ Sil(T). Every model C with C ⪯_j V_j[G′ ↦ S] satisfies

  ρ_j({T = V_j} ∩ {C ≠ V_j}) ≤ ρ_j(G′).

In particular:
- edge members, V_1 and V_2 cannot dominate V_3-retreats on pieces with ρ_3(G′) < ρ_3({T = B} ∩ M_3). Indeed they say A on M_3, where T says the 3-correct B on a fixed cone.
- So **small V_3-retreats are dominated only by path members.** Under Theorem 5.6 these must be iso-level.

**Corollary 6.3 (accumulation; PROVED).** For every member C₂ silent on G′ (T, refinements of T, edge members whose window contains G′, earlier defenders), the dominator C of V_j[G′ ↦ S] agrees with V_j on {C₂ = V_j} up to φ_j-mass φ_j(G′). As the pieces shrink inside the silent cone of C₂, dominators are forced onto V_j on the growing union ⋃ {C₂ = V_j}, taken over all registered C₂ silent on the piece.

This is the continuum form of PP36's "cross-exposure", and it is what makes generation n+1 depend on generation n.

**Remark 6.4 (generation 0 passes the necessary conditions; PROVED for the conditions listed).**
- **Refinements of T, C = D_K with K ⊆ M.** They equal T on Ans(T), so the budget of Cor 6.2 holds with value 0.
  - K near the e_j-corner of M gives V_j's answer on part of a given piece, as Lemma E requires.
  - The precise centre D_u is iso-level at every world (permutation symmetry, Lemma 1.2's argument). Points of M on the curve L⁰_{w₀}(D_m) = 1 give a one-parameter family of iso-level candidates.
- **Silent-wedge edge models D_[e_j, λ]** (PP34 §5.4), for j ∈ {1, 2}. They meet Cor 6.2 for V_j's retreats when {T = V_j} misses the wedge. It does on the far wedges, where T gives the opponent's answer.
- I have not checked that these dominations survive every installed/gate configuration of Theorem 3.2(b). That is OPEN.

---

## 7. The recursion, and where it stops

**What a generation must preserve.** Let P_n be the members after n generations. Generation n+1 is safe given generation n if:
- **(I1) Gates.** Each new member is coherent; if at an edge index, it satisfies Cor 4.2 (true for edge models in Prop 4.3's family).
- **(I2) Iso-level.** Each new member placed on J has L⁰_{w₀} = 1 (Thm 5.6). The selection on J is continuous at the other worlds, and liminf a_3 ≥ 3/2 at q_e.
- **(I3) Realised budgets.** For each installed C ⪯ V_j[G′ ↦ S] and each member C₂ of P_{n+1} silent on G′, φ_j(P) ≤ φ_j(G′) (Prop 6.1). This applies to new C₂ against old dominations as well as to old C₂ against new ones.
- **(I4) Cross-gate configurations** between L-records and E-records other than §4's, at worlds 1 and 2.
- **(I5) Installed/gate configurations** of Theorem 3.2(b), beyond Prop 6.1.
- **(I6) Sections with installed records.**

Of these, Theorem 3.1 gives universal competitiveness for free. (I1) is solved (Prop 4.3). (I2) and (I3) are proved necessary.

**The obstruction I met.** (I3) runs in both directions.
- Registering a new defender C₂ that is silent on some piece G′ retroactively constrains every installed dominator of every V_j-retreat inside that piece.
- New defenders are themselves needed for retreats of earlier defenders, which by Lemma E answer on their pieces. So they are silent elsewhere.

I could not find a geometric invariant that controls this union of silent cones while keeping (I2). Refinements of T are the natural candidates, because:
- they are silent exactly where some point of M is not decisive;
- they are equal to T on Ans(T);
- the union ⋃ {C₂ = V_j} over refinements C₂ is still contained in {T = V_j} ∪ Sil(T).

**Conjecture 7.1.** Take refinement dominators D_K, K ⊆ M, with K iso-level at w₀ and chosen per rival with K shrinking toward the relevant corner of M. Together with Prop 4.3's edge gate and silent-wedge edge dominators for V_1 and V_2, they meet (I1)–(I3) for all generations. The open steps are (I4)–(I6).

**What is excluded, and why (the classification asked for).** For the stated class of designs (one balanced potential per gate, a uniform zero rule per world, realiser-gated acceptance):
- Theorem 5.6 shows that only S = {w₀} survives;
- Prop 6.1 shows that realiser-gating turns every silent member into a budget constraint on every dominator of a retreat inside its silence.

So the two optional commitments responsible are:
- **(C1)** all full-support members share one potential (forcing iso-level);
- **(C2)** a gate accepts a positive record whenever *any* member realises its old side (forcing Prop 6.1 for every silent member).

The natural redesign is to gate by **realiser and support index jointly**: a record is accepted through C₂'s gate only if C₂'s index is in the closure of the indices realising the record's old side. That would keep sections closed (that is the only place realisers matter for (S)) while removing far-away silent members from (I3). I have not checked it against Lemma 3.3. The (TC) safety of a single gate used only the realisation of one side of zero records, so it should carry over, but this is not checked.

---

## 8. The coordinator's round-48 referee items

1. **PP36's "one precise answerer at one defence world" is false.** The counterexample is an edge model giving the minority answer on balls in M_1 and in M_2. Nothing here uses that claim. Theorem 3.1 gives every edge member a defence against every dominator through its own E-gate, independently of how dominators are coloured. What Prop K still constrains is (TC) through installed records (§3(b)), not competitiveness. The repaired colouring rule (answerer, a support world where no served rival beats it) is compatible with Γ and can be used for the installed layer.
2. **PP33's ray models are not mutually competitive.** In Γ every member is competitive against every model (Theorem 3.1), so this defect cannot recur.
3. **PP34 Prop 4.1(f).** See Remark 4.4. Cor 4.2 allows both answers on a one-class piece.
4. **PP33 Lemma 1.2(a) and Prop 8.2.** Not used. The gates here replace the ρ-potential extension Prop 8.2 rules out. PP33's Prop 8.2 construction (contradiction on F) is blocked in Γ because the old side Z[F ↦ X] is realised by no member.

---

## 9. Status

| Result | Label |
|---|---|
| Lemma 1.1 (balance), Lemma 1.2 (exact levels 1 and 3/2) | PROVED; balance CHECKED; values NUMERICS-confirmed |
| Prop 2.1 (one potential per world: Bayes or edge failure) | PROVED (from cited results) |
| Thm 3.1 (universal competitiveness, all generations), Lemma 3.3, Thm 3.2 | PROVED |
| Thm 4.1 (exact PP30 cross condition), Cor 4.2 (band), Prop 4.3 (explicit gate and family) | PROVED; CHECKED |
| Thm 5.1, Props 5.2–5.5, Thm 5.6 (ties against sections; the single survivor) | PROVED under (H_path), (H4), (H5), (H_E) as stated |
| Prop 6.1, Cors 6.2–6.3 (realised retreat kill, budget, accumulation) | PROVED |
| Remark 6.4 (generation-0 candidates meet the necessary conditions) | PROVED for those conditions only |
| (I4)–(I6); dominators for every generation; T's fills X = T[G ↦ N] and their dominators; edge models' forced rivals' dominators | OPEN |
| Conjecture 7.1 | CONJECTURE |

**What is proved for all generations:** universal competitiveness of every member (Thm 3.1), and the necessary invariants (I2)–(I3). **What is not proved for any generation:** the full (TC) of the system with installed dominations, and closed sections with them. The milestone is therefore not reached. The furthest point is a design (Γ with S = {w₀}, Prop 4.3's edge gate) whose remaining obligations are listed exactly in §7.
