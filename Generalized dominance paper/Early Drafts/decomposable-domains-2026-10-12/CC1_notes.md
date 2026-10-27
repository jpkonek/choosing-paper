# CC1 (round 31, BRIEF23 design A). A verified non-priceable seed through T1; an explicit invariant whose extension steps reduce to static conditions; and the incompatibility that invariant meets at T1

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full proof here, one reader (me), not refereed;
- **CHECKED**: exact finite computation (rational arithmetic or exhaustive search), or a step-by-step reading;
- **NUMERICS**: floating-point or sampled; nothing depends on it;
- **CONJECTURE**.

Scripts are in `cc1py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. No assumption is
added. Every extra hypothesis is a hypothesis of a stated result, and is named where it is used.

**Domain.** The seed (§1) lives on the **full four-advice domain**. Its comparisons change advice only between
"accept h" and silence, on cells inside U = D_{K′}. So it is also, verbatim, a seed on the U-domain M_U. The invariant
and the theorems of §§2–4 are stated for any decomposable domain with bounded strictly guiding penalties. They are
used on the full domain, and on M_U as a special case. I did not need to prove that M_U suffices, so I do not claim it.

---

## 0. Outcome

1. **Seed: constructed and verified (§1; CHECKED exact, with PROVED lemmas).** On the full domain, near T1
   (ε = 3/10), there are:
   - four coherent models B_1 = D_{T1}, B_2, B_3, B_4, with B_2–B_4 rational triangles whose vertices lie within 1/10
     of T1's vertices;
   - seven disjoint open polyhedral cells in U, away from the coordinate planes;
   - four world-1 comparisons B_k ⪯_1 X_k, with X_k regular.

   These have the following properties.
   - (a) The world-1 change vectors sum, with weights 1, to 0 on six cells and to −4 on the seventh. This holds for
     every strictly guiding penalty, ladder steps included. So no strictly positive finitely additive endorser
     exists at world 1.
   - (b) Every realisable composition of the four seed records with all guidance records contains **at most one**
     seed record. Hence the closure contains no strict guidance reversal.
   - (c) The comparisons are rigid (K2.1) and have the N17 shape: four comparisons, pairwise-overlapping gains, and
     pairwise-crossing world-1 error sets. At worlds 2 and 3, every X_k improves on some cell. So guidance never
     forces B_k ⪯_2 X_k or B_k ⪯_3 X_k, and each seed comparison can be the accepting world of (K) at its base.
2. **Invariant I(𝔈) (§2; PROVED).** Each world's accepted comparisons lie in a fixed envelope
   𝒜*_i = 𝒦_i ∪ ⋃_{g∈G_i}(g + 𝒦_i). Here 𝒦_i is the dual cone of a set Ψ_i of bounded densities, and G_i is a finite
   set of seeds with two finite conditions, (E) and (P). The invariant is a property of single comparisons, and it
   is independently checkable. It is preserved by:
   - composition closure and (IB)-transport;
   - unions at limit stages, so the finitary issue disappears;
   - closed sections through one fixed reservation plan, given a selection continuous in measure.

   Adding a competitor at index q can be done inside I **iff** the static covering condition (Cov) holds at q.
   Protection and the no-(C)-tie rule are automatic under one static condition (Prot). So the whole transfinite
   construction collapses to **static** conditions. When they hold, the maximal envelope relations form a full
   system, and the seed's certificate stays intact (Thm 2.4).
3. **Exact form of (Cov) (§3; PROVED).** In any system whose acceptance sets lie in such envelopes, competitiveness of
   C_q holds iff, for **every** choice of one density per world, C_q is a pointwise weak Bayes model of the additive
   field (φ_iλ_i) at a weight supported in supp q (Thm 3.1). With a selection continuous in measure, these weights
   cover Δ (Lemma 3.4, a Brouwer argument). So every such tuple field has coherent, a.e.-unique Bayes models at a.e.
   weight: this is property (γ).
4. **Incompatibility at T1 (§4; PROVED modulo the imported chain D1, M3.8, M3.9 = BB2 Thm 6.1, Q4.1).** No ranking
   with strict (G), (IB), (S) has T1 ∈ C_L when its acceptance sets lie in finite-seed envelopes and its selection is
   continuous in measure. This holds **whatever the world orders are inside the envelopes**: additive partners, Brier
   edges and continuity of densities are not assumed (Thm 4.1). Since B_1 = T1, **the seed of §1 cannot be completed
   to a T1 system inside I**. This is the explicit obstruction asked for in task (3).
5. **Not achieved:** a full system for any target with the seed's non-endorsement intact. For targets other than T1,
   class I is reduced to the static problem of Thm 2.4. It is not excluded, and it is not solved (§5). What a
   successful construction must therefore use is stated in §5: infinitely many seeds with vanishing margins, or
   envelopes that are not countably additive cones, or a selection that is not continuous in measure.

---

## 1. The seed (task (1))

### 1.1 Data (exact, rational)

Take ε = 3/10, u = (1/3, 1/3, 1/3) and T1 = co{v_1, v_2, v_3} with v_k = (1−ε)u + εe_k. Concretely, v_1 = (8/15, 7/30,
7/30), cyclically.

Put K′ := u + (9/10)(T1 − u), so U = D_{K′}. On the full domain U plays no role in the axioms; it only locates the
cells. Every credal set below contains K′, so every model below accepts only gambles of U. On a cell it therefore
accepts h or is silent; it never accepts −h.

The four credal sets are K_k = co(K′ ∪ V_k), with:
- V_1 = {v_1, v_2, v_3}, so K_1 = T1 and **B_1 = D_{T1}**;
- V_2 = {(19/30, 3/20, 13/60), (17/60, 8/15, 11/60), (1/5, 11/60, 37/60)};
- V_3 = {(13/30, 1/5, 11/30), (11/60, 3/5, 13/60), (19/60, 13/60, 7/15)};
- V_4 = {(31/60, 3/10, 11/60), (3/20, 13/30, 5/12), (1/6, 1/3, 1/2)}.

Every coordinate of V_2–V_4 is within 1/10 of the corresponding coordinate of T1's vertices. Write B_k := D_{K_k}.

For h ∈ U, B_k accepts h iff m·h > 0 for every m ∈ V_k (because K′·h > 0 already). B_k is **correct at world 1** at h
iff it accepts exactly when h_1 > 0.

**Cell centres** (indices are the bases that are correct at world 1). Each centre has every coordinate of modulus at
least 0.15 times its largest coordinate.

| cell | centre h^S | signs | accepted by | world-1 correct |
|---|---|---|---|---|
| R_{12} | (1, −0.30809, −0.15) | + − − | B_1, B_2 | {1,2} |
| R_{13} | (1, −0.15, −0.319) | + − − | B_1, B_3 | {1,3} |
| R_{14} | (0.15, −0.46328, 1) | + − + | B_1, B_4 | {1,4} |
| R_{23} | (−0.2766, 1, −0.2766) | − + − | B_1, B_4 | {2,3} |
| R_{24} | (−0.29159, −0.23288, 1) | − − + | B_1, B_3 | {2,4} |
| R_{34} | (1, 1, −0.91083) | + + − | B_3, B_4 | {3,4} |
| R_∅ | (−0.22449, 1, 1) | − + + | all four | ∅ |

The decimals are exact rationals (`seed_exact.py`).

**Cells.** For each S, R_S is the open polyhedral cone of h such that:
- each coordinate has the sign of h^S_i;
- v·h > 0 for every vertex v of K′;
- m·h > 0 for every m ∈ V_k, for each k that accepts h^S;
- m*_k·h < 0 for one fixed witness vertex m*_k with m*_k·h^S < 0, for each k that does not accept h^S.

Every inequality is strict at h^S (CHECKED exactly; no vertex value and no coordinate is 0). So R_S is open, non-null
and contained in U. On R_S the acceptance pattern and the signs are constant, and so is the correctness of every B_k
at every world. The seven world-1 patterns are distinct, so the cells are pairwise disjoint.

**Competitors.** Let R := ⋃_S R_S. X_k is B_k with "accept h" and silence swapped on R, and unchanged elsewhere. It is
measurable and regular: it is unchanged on unanimous problems.

**Seed records.** At world 1:
- on R_S with k ∈ S: B_k is correct, and the swap moves world-1 rank up by one ladder step (good → silence if
  h_1 > 0; silence → bad if h_1 < 0). This is the gain set P_k := ⋃_{S∋k} R_S;
- on R_S with k ∉ S (including R_∅): B_k errs, and the swap moves world-1 rank down by one step. This is N_k.

The seed S consists of the comparisons B_k ⪯_1 X_k, k = 1, …, 4, at world 1. Seeds are assigned to world 1 only;
worlds 2 and 3 get none.

### 1.2 Properties

**Theorem 1.1 (seed; CHECKED exactly for the data, PROVED for the consequences).**

**(a) Certificate.** Let λ be any strictly guiding penalty at world 1, and write Λ_1X := λ(·, a_X(·)). Then
Λ_1X_k − Λ_1B_k = w·g_k. Here w(h) > 0 is the single ladder step used at h, and g_k := 1_{P_k} − 1_{N_k}.
- Σ_k g_k = 0 on the six pair cells (two gains, two losses), and = −4 on R_∅. So Σ_k (Λ_1X_k − Λ_1B_k) = wΣ_k g_k is
  ≤ 0 everywhere and nonzero.
- Hence no finitely additive charge ν, strictly positive on non-null sets, has ν(Λ_1X_k − Λ_1B_k) ≥ 0 for all k:
  summing would give ν(4w1_{R_∅}) ≤ 0.
- Each problem of R carries exactly one changed ladder increment: the silence increment where h_1 > 0, the wrong
  increment where h_1 < 0. So the same certificate is a certificate on M3's ladder (a pair of charges per world, Prop.
  M3.2).
- On M_U this is exactly an (M1) obstruction in the sense of write-up Def. addup, provided the B_k are in C_L.

**(b) Closure.** Let 𝒮 be the set of world-1 records consisting of all guidance (pointwise rank-nondecreasing)
records and the four seed records with all their (IB)-transports. Every realisable composition of members of 𝒮
contains at most one seed record. Hence every composition either is a guidance record, or has rank change ≥ +1 on
some P_k. No composition is a strict guidance reversal.

*Proof.*
1. A realisable composition is a finite sequence of models X^0 → X^1 → … → X^m, each step a member of 𝒮.
2. An (IB)-transport of seed k changes advice only on R. Point by point it requires B_k's advice before the step and
   produces X_k's advice after it.
3. Suppose two seed steps k, then l (k = l allowed), have only guidance steps between them. Take h ∈ P_k ∩ P_l. This
   set is non-null: it is R_{kl} if k ≠ l, and P_k ⊇ R_{kl′} if k = l.
4. At h, B_k and B_l both give the world-1-correct advice. Seed step k raises the world-1 rank at h above the correct
   rank; guidance steps never lower it; seed step l needs the correct rank at h before it. This is a contradiction.
5. So seed steps are never separated by guidance alone. Two seed steps would have to be consecutive or separated by
   guidance, so at most one seed step occurs.
6. If no seed step occurs, the composition is guidance. If seed k occurs once, the rank at points of P_k before it is
   at most the correct rank (guidance only raises), and after it at least one more. ∎

CHECKED (`closure_check.py`): exhaustive breadth-first search over all start states in {0,1}^7 on the seven-cell
ladder model (ranks 0–3, the four seed moves, unit guidance steps). There were 1 190 095 state visits; no strict
reversal is reachable; the maximum number of seed records on a path is 1.

**(c) Shape and compatibility.**
- **Rigidity (K2.1).** Let 0 < f < 1. Let δ′ be any "proportional part" of g_k: δ′⁺ ⊆ P_k, δ′⁻ ⊆ N_k, with
  μ(δ′^±) = f·μ(g_k^±). Then δ′ is not in the closure of (b). By (b), the closure is the guidance records together
  with the records lying above some g_m, and δ′ lies above none of them:
  - δ′ ≥ g_k fails, since δ′⁺ is smaller than P_k;
  - for m ≠ k, P_m contains a cell R_{mj} with j ≠ k, which is disjoint from P_k.

  So no g_k is divisible relative to the seed closure (PROVED).
- **N17 shape.** There are four comparisons. Gains overlap pairwise: P_k ∩ P_l = R_{kl}. The world-1 error sets of
  the B_k, restricted to R, are E_1(B_k) ∩ R = N_k. They cross pairwise: N_k ∖ N_l ⊇ R_{lj} for j ∉ {k,l}. CHECKED.
  N17.3's necessary conditions hold: each gain lies in the other bases' error sets.
- **Competitiveness compatibility.** For each k, X_k improves on B_k at world 2 on at least one cell, and at world 3
  on at least one cell (table in `seed_exact.out`; for example X_4 improves at world 2 on R_{14} and at world 3 on
  R_{23}, R_{24}, R_{34}). So neither B_k ⪯_2 X_k nor B_k ⪯_3 X_k is forced by guidance. At an index q_k of B_k, the
  disjunction (K) for the competitor X_k can be resolved at world 1 by the seed comparison itself, with worlds 2 and
  3 rejecting. This is a consistency statement only. Whether the other worlds can in fact reject is part of the
  global problem (§§2–4).
- **Near T1.** B_1 = D_{T1}. B_2–B_4 are interior credal triangles within 1/10 of T1. Their undominatedness can only
  be settled inside a full system; §4 shows what prevents that within I.

*Remark (why polygons).* With one extra vertex per model, B_k = D_{co(K′∪{m_k})}, an LP search over 20 000 random
4-tuples found no K4 realisation (`lp_seed.py`, NUMERICS). Heuristically, the needed six separable 2-sets with e_1 on
a prescribed side do not fit four points. With triangles near T1 they are easy (`lp_seed3.py`, `lp_margin.py`;
the data above maximise the smallest LP margin over 400 rational trials).

---

## 2. The invariant (task (2))

### 2.1 Envelope data

Fix a decomposable domain with advice ranges A(h), here the full domain or M_U. For each world i fix a bounded,
strictly guiding penalty λ_i(h, a). Put Λ_iX := λ_i(·, a_X(·)) ∈ L^∞(H), and

  ω_i(h) := max_{a∈A(h)} λ_i(h,a) − min_{a∈A(h)} λ_i(h,a).

On M_U take λ_i to be the error indicator, so that Λ_iX = 1_{E_iX} and ω_i = 1 on pairs meeting U. For any models X, Y
the difference Λ_iY − Λ_iX is the **record** of the comparison X ⪯_i Y. It depends only on the advice of X and Y where
they differ.

**Envelope data** 𝔈 = (λ_i, Ψ_i, G_i)_{i≤3} consist of:
- a nonempty set Ψ_i of bounded measurable functions φ ≥ 0, containing at least one φ_i^+ > 0 a.e.;
- a **finite** set G_i ⊆ L^∞ of seed records,

subject to:
- **(E)** for each g ∈ G_i there is φ ∈ Ψ_i with ∫gφ dμ > 0;
- **(P)** for all g, g′ ∈ G_i (g = g′ allowed) there is φ ∈ Ψ_i with ∫(g + g′)φ dμ > ∫ω_iφ dμ.

Define
- 𝒦_i := {f ∈ L^∞ : ∫fφ dμ ≥ 0 for every φ ∈ Ψ_i};
- 𝒜*_i := 𝒦_i ∪ ⋃_{g∈G_i} (g + 𝒦_i);
- X ≤*_i Y :⟺ Λ_iY − Λ_iX ∈ 𝒜*_i.

This is K2.5's scheme with the ansatz removed. Ψ_i is arbitrary, every world may carry an envelope, and no world is
assumed additive.

**The invariant.** A partial system consists of:
- relations R_i on evaluable models;
- a selection q ↦ C_q on a closed index set Π ⊆ Δ;
- a reservation plan.

It satisfies **I(𝔈)** if
- **(I1)** X R_i Y implies X ≤*_i Y, for every i;
- **(I2)** each reserved neighbourhood V(q,i,X) is disjoint from the envelope section {q′ ∈ Π : C_{q′} ≤*_i X}.

Both clauses are conditions on single comparisons. They can be checked independently of how the comparisons were
generated, and they are not a restatement of finite satisfiability.

**Lemma 2.0 (the seed carries envelope data at world 1; PROVED).** For the seed of §1, choose λ_1 as follows:
- on R ∩ {h_1 > 0}, ranks good, silence, bad, contradiction cost 0, 1, 1+η, 1+2η;
- on R ∩ {h_1 < 0}, they cost 0, η, 1+η, 1+2η;
- off R, any strictly guiding penalty with ω_1 ≤ 1 + 2η.

Then Λ_1X_k − Λ_1B_k = g_k exactly. Put φ_{kl} := 1_{R_{kl}} + η′. For η, η′ small enough relative to
min_S μ(R_S)/μ(H), the set Ψ_1 ⊇ {φ_{kl}} satisfies (E) and (P) for G_1 = {g_1, …, g_4}, and φ_{kl} > 0 everywhere.

*Proof.* We have ∫(g_k + g_l)φ_{kl} ≥ 2μ(R_{kl}) − 2η′μ(R), while ∫ω_1φ_{kl} ≤ (1+2η)(μ(R_{kl}) + η′μ(H)). For the case
k = l use φ_{kj} with any j ≠ k: ∫2g_kφ_{kj} ≥ 2μ(R_{kj}) − 2η′μ(R). Condition (E) follows from the same estimates. ∎

The witnesses are existential: (E) and (P) survive enlarging Ψ_1. What the envelope must also accommodate is
competitiveness; that is §3.

### 2.2 Preservation

**Lemma 2.1 (closure; PROVED).** For data satisfying (E) and (P), each ≤*_i is a preorder on the domain with strict
(G) and (IB). Consequently I(𝔈) is preserved by:
- installing guidance comparisons;
- transitive closure;
- (IB)-transport (replacing shared advice).

*Proof.*
- **Reflexive:** 0 ∈ 𝒦_i.
- **(IB):** the record does not change when shared advice is replaced.
- **Transitive.** Records add: Λ_iZ − Λ_iX = (Λ_iZ − Λ_iY) + (Λ_iY − Λ_iX).
  - We have 𝒦_i + 𝒦_i ⊆ 𝒦_i and 𝒦_i + (g + 𝒦_i) ⊆ g + 𝒦_i.
  - If Λ_iY − Λ_iX ∈ g + 𝒦_i and Λ_iZ − Λ_iY ∈ g′ + 𝒦_i, then for the (P)-witness φ,
    ∫(Λ_iZ − Λ_iX)φ ≥ ∫(g + g′)φ > ∫ω_iφ. But Λ_iZ − Λ_iX ≤ ω_i pointwise, which is a contradiction. So that case
    never occurs.
- **Weak (G):** a pointwise worsening has record ≥ 0, which lies in 𝒦_i because Ψ_i ≥ 0.
- **Strict (G).** Let f ≤ 0 with f ≠ 0.
  - f ∉ 𝒦_i, since ∫fφ_i^+ < 0.
  - f ∉ g + 𝒦_i: that would give ∫fφ ≥ ∫gφ > 0 for g's (E)-witness φ, while ∫fφ ≤ 0. ∎

**Lemma 2.2 (limit stages; PROVED).** Let (R_i^α) be an increasing ordinal-indexed family of stages satisfying (I1).
Then the union satisfies (I1). With the union lemma (Vacuous Targets, Lemma union), it is a preorder with (G) and (IB)
in which every protected model stays undominated and every competitiveness witness stays installed. (I2) is a
condition on the fixed plan, so it is not affected by unions.

*Proof.* (I1) is a property of each comparison separately, so it passes to unions. The remaining statements are
Lemma union. ∎

This is how the finitary issue is handled. Closure of an increasing union of closed sections is never needed: every
section of every stage lies inside the **fixed** closed envelope section, and the plan reserves its complement once
and for all.

**Lemma 2.3 (closed sections through a fixed plan; PROVED).** Let q ↦ C_q be continuous in measure on a closed
Π ⊆ Δ. Then for every i and every model X, the envelope section Σ*_i(X) := {q ∈ Π : C_q ≤*_i X} is closed. The plan
V(q,i,X) := Π ∖ Σ*_i(X) is relatively open, and no I-preserving step ever installs a comparison it forbids.

*Proof.*
- λ_i is bounded and the advice converges in measure, so q ↦ Λ_iC_q is L¹-continuous.
- Each φ ∈ Ψ_i is bounded, so 𝒦_i and each g + 𝒦_i are L¹-closed. 𝒜*_i is a finite union of closed sets.
- Σ*_i(X) is therefore the preimage of a closed set under a continuous map.
- By (I1), every installed comparison C_q ⪯_i X has q ∈ Σ*_i(X). ∎

**Theorem 2.4 (the extension problem inside I is static; PROVED).** Let 𝔈 satisfy (E) and (P). Let q ↦ C_q,
q ∈ Δ, be coherent and continuous in measure. Consider:
- **(Cov)** for every q ∈ Δ and every model X there is i ∈ supp q with C_q ≤*_i X;
- **(Prot)** for every q: if Y ≤*_i C_q at every world i, then Y = C_q a.e.;
- **(Fit)** each g ∈ G_i equals Λ_iX_g − Λ_iC_{q_g} for some index q_g and some regular X_g.

Then:
- **(a) The maximal system works.** If (Cov), (Prot) and (Fit) hold, then (≤*_1, ≤*_2, ≤*_3) with the selection C_q
  satisfies strict (G), (IB), (LA), (S) (closed sections for every model) and (C), with C_L = {C_q : q ∈ Δ}. Every
  seed comparison C_{q_g} ⪯_i X_g is accepted and relevant. If some world's seeds satisfy (Cert) (a positive
  combination ≤ 0 and ≠ 0), that world has an (M1) certificate, intact.
- **(b) Each extension step, done inside I.**
  - Installing the competitor comparison C_q ⪯_i X at some i ∈ supp q preserves I **iff** C_q ≤*_i X. So the
    competitiveness disjunction at (q, X) can be met inside I iff (Cov) holds at (q, X).
  - Composition closure, (IB), guidance and unions always preserve I (Lemmas 2.1, 2.2).
  - Closed sections are delivered by the fixed plan (Lemma 2.3).
  - Under (Prot), the protection rule ("X ⪯_i C_q at every world ⇒ C_q ⪯_i X at every world") never fires except for
    X = C_q.
  - Under (Prot), forbidden outcome (c), an incoherent model tied everywhere with a selected model, never occurs.
- **(c) Necessity.** Any construction whose final relations satisfy (I1) and (S) satisfies (Cov).

*Proof.*
- **(a)**
  - Lemma 2.1 gives (G) and (IB).
  - (Cov) is competitiveness on supp q.
  - Lemma 2.3 with Π = Δ gives closed sections.
  - **Undominated.** If Y ⪯_i C_q at every world, then (Prot) gives Y = C_q. So no model dominates C_q, and C_q ties
    everywhere only with itself.
  - **(C).** By thm:kkm, every undominated model is tied everywhere with some C_q, hence equals it. So C_L = {C_q},
    and any model tied everywhere with a member of C_L equals that member, which is coherent.
  - **Seeds.** 0 ∈ 𝒦_i gives g ∈ 𝒜*_i, so C_{q_g} ⪯_i X_g. It is relevant, since C_{q_g} ∈ C_L and X_g is regular.
- **(b)** Immediate from the definitions and Lemmas 2.1–2.3.
- **(c)** Competitiveness witnesses are installed comparisons. ∎

So the extension lemma demanded by BRIEF23 holds for I in the strongest form available. Every step except
competitor-addition is unconditional. Competitor-addition is possible exactly under the static condition (Cov). The
transfinite construction collapses: if (Cov) and (Prot) hold, take the maximal relations; if (Cov) fails at one
(q, X), no I-preserving construction exists at all.

---

## 3. What (Cov) is: competitiveness inside an envelope is "Bayes for every tuple"

Throughout this section a **system in class I** is a ranking that has strict (G), (IB) and a competitive selection
(competitive on supp q at every q ∈ Δ), and whose acceptance relations satisfy ⪯_i ⊆ ≤*_i for envelope data 𝔈 with
(E). Maximality and (P) are not needed for this section. For a tuple τ = (φ_i)_i with φ_i ∈ Ψ_i, write ℓ^τ_i := φ_iλ_i.
This is a bounded additive penalty field, strictly guiding when every φ_i > 0 a.e. Write v^τ_a(h) ∈ R³ for the vector
with components φ_i(h)[λ_i(h,a) − λ_i(h, a_C(h))] (relative to a fixed model C).

**Theorem 3.1 (PROVED).** Let q ∈ Δ and J := supp q.
- **(a) Necessity.** If C_q is competitive on J in a system of class I, then for every τ ∈ Π_{i∈J} Ψ_i there is a
  weight w ∈ Δ_J with
  
    Σ_{i∈J} w_i φ_i(h)[λ_i(h,a) − λ_i(h, a_{C_q}(h))] ≥ 0 for every a ∈ A(h), for a.e. h.   (WB)
  
  That is, C_q is a pointwise weak w-Bayes model of the additive field ℓ^τ.
- **(b) Sufficiency for the cones.** Conversely, if (WB) holds for every such τ, then every model X has some i ∈ J
  with Λ_iX − Λ_iC_q ∈ 𝒦_i. So (Cov) holds at q even without seeds.

*Proof of (a).*
1. Fix τ and suppose no w ∈ Δ_J satisfies (WB).
2. Let E be the finite set of (E)-witnesses of all seeds of the worlds in J.
3. For a model X put z(X) := (∫(Λ_iX − Λ_iC_q)φ_i dμ)_{i∈J}, and let z⁺(X) be z(X) extended by the coordinates
   ∫(Λ_iX − Λ_iC_q)φ dμ, for i ∈ J and φ ∈ E.
4. **Convexity.** By Lyapunov's theorem for finitely many advice choices on a nonatomic measure, the range
   Z⁺ := {z⁺(X)} is convex and compact. Hence so is its projection Z = {z(X)}. Also 0 = z⁺(C_q) ∈ Z⁺.
5. **Separation.** Suppose Z misses the open negative orthant N of R^J. Separating the convex sets Z and N gives
   w ≥ 0, w ≠ 0, with w·z ≥ 0 on Z (the constant is 0, since 0 ∈ Z ∩ cl N). Normalise w ∈ Δ_J.
6. Then ∫_D w·v^τ_a dμ ≥ 0 for every measurable D and every a. Indeed, use X := C_q with advice a on D, intersected
   with {a ∈ A(h)}. So w·v^τ_a ≥ 0 a.e.: this is (WB), a contradiction. Hence some X has z(X) ∈ N.
7. **Shrinking.** By convexity, t·z⁺(X) ∈ Z⁺ for t ∈ (0,1]. So there is X_t with z⁺(X_t) = t·z⁺(X).
8. **No world in J accepts C_q ⪯_i X_t.**
   - Λ_iX_t − Λ_iC_q ∉ 𝒦_i, because ∫(·)φ_i = t·z_i(X) < 0.
   - For any seed g ∈ G_i with witness φ ∈ E, ∫(Λ_iX_t − Λ_iC_q)φ = t·z⁺_{i,φ}(X). This is < ∫gφ once t is small.
     So Λ_iX_t − Λ_iC_q ∉ g + 𝒦_i. There are finitely many seeds, so one t works for all of them.
9. So C_q ⋠_i X_t for every i ∈ J, which contradicts competitiveness.

*Proof of (b).* Suppose Λ_iX − Λ_iC_q ∉ 𝒦_i for every i ∈ J. Pick φ_i ∈ Ψ_i with ∫(Λ_iX − Λ_iC_q)φ_i < 0, and let
w be the (WB)-weight of this tuple. Integrating (WB) along a_X gives Σ_i w_i ∫(Λ_iX − Λ_iC_q)φ_i ≥ 0. But every term
is negative and w ≠ 0, which is a contradiction. ∎

*Reading.*
- In class I, "competitiveness as a choice among worlds" is equivalent, up to the finitely many seeds (which can never
  be load-bearing for small moves), to one statement: the selection is simultaneously a weak Bayes family of the
  whole product family of additive fields ℓ^τ. The weight may depend on τ and is supported in supp q.
- This is where the seed world's freedom goes. Every member φ of Ψ_1, including the cell-concentrated (P)-witnesses,
  must make C_q weak-Bayes for (φ, φ_2, φ_3), for every choice of partners.

**Corollary 3.2 (edge form, M_U; PROVED).** Let q lie on the open edge (e_1, e_2), and let φ ∈ Ψ_1, ψ ∈ Ψ_2 be
positive a.e. Put G_q := R_{12} ∖ E_1(C_q).
- If the (WB)-weight of (φ, ψ) is interior, then ess inf_{G_q} φ/ψ ≥ ess sup_{R_{12}∖G_q} φ/ψ, and C_q is correct at
  worlds 1 and 2 a.e. on Q_3.
- If the weight is e_1 or e_2, then C_q equals P_1 or P_2, respectively.

So along every world-1 edge, the edge split of R_{12} is a common threshold set of φ/ψ for all pairs (φ, ψ). Each
pair (φ, φ′) ∈ Ψ_1² must give log(φ/ψ) and log(φ′/ψ) the same edge order. This is the (TH) and pump structure of BB1
and the forced cone of K2.6, obtained here without additive partners and without continuity.

*Proof.* On R_{12}, s_2 = −s_1. (WB) reads s_1(w_1φ − w_2ψ) ≥ 0, where s_1 = +1 on G_q. On Q_3, s_1 = s_2, and (WB)
reads s_1(w_1φ + w_2ψ) ≥ 0. ∎

*Consequence for cell-concentrated witnesses (PROVED).* Let φ_{kl} ∈ Ψ_1 be concentrated on one cell in R_{12}.
Then the edge splits must take that cell **after** every point of lower φ_{kl}/ψ. With several cells in R_{12} and a
common partner ψ, the cells must be ordered along the edge, with ψ-masses decaying steeply in that order. This is
the structure of N17.8's band, with m_k > 3R_k. It is not excluded by edges alone. The exclusion at T1 comes from §4.

### 3.3 From many tuples to one coherent additive shadow

Fix a tuple τ = (φ_1, φ_2, φ_3) of a.e.-positive members, and put

  W̃_τ(q) := {w ∈ Δ : C_q satisfies (WB) for ℓ^τ at w}  (all weights, not only those in Δ_{supp q}).

**Lemma 3.3 (PROVED).** Assume class I, and that q ↦ C_q is continuous in measure. Then:
- W̃_τ(q) is nonempty, closed and convex;
- it meets Δ_{supp q} (Thm 3.1(a));
- its graph is closed.

*Proof.*
- Convexity and closedness are clear: (WB) is a family of linear inequalities in w.
- **Closed graph.** Let q_n → q and w_n ∈ W̃(q_n) with w_n → w. A subsequence has a_{C_{q_n}}(h) → a_{C_q}(h) for a.e.
  h. Advice takes four values, so the advice is eventually equal. The inequalities (WB) at (q_n, w_n) then pass to
  the limit pointwise. ∎

**Lemma 3.4 (covering; PROVED).** Let W: Δ ⇉ Δ have nonempty closed convex values and closed graph, and let
W(q) ∩ Δ_{supp q} ≠ ∅ for every q. Then every interior q* ∈ int Δ lies in W(q) for some q.

*Proof.*
1. Suppose not. For each q, q* ∉ W(q), so the open convex cone O(q) := {v ∈ T : v·(w − q*) > 0 ∀w ∈ W(q)} is
   nonempty, where T := {Σx = 0}.
2. The graph {(q, v) : v ∈ O(q)} is open: W has closed graph with compact range, hence is upper hemicontinuous. By
   Browder's selection theorem there is a continuous v: Δ → T with v(q) ∈ O(q).
3. g(q) := π_Δ(q − v(q)) is a continuous self-map of Δ, where π_Δ is the nearest-point projection. By Brouwer it has a
   fixed point q. Then −v(q) lies in the normal cone N_Δ(q).
4. If q is interior, this forces v(q) = 0, impossible.
5. If q is in the relative interior of the face {q_3 = 0}, then v(q) = c(e_3 − u)_T with c > 0.
   - Pick w_0 ∈ W(q) ∩ Δ_{supp q}. Then w_{0,3} = 0.
   - So v(q)·(w_0 − q*) = c(w_{0,3} − q*_3) = −cq*_3 < 0, contradicting v(q) ∈ O(q).
6. Vertices are handled in the same way. At e_1, v = c_2(e_2 − u) + c_3(e_3 − u) with c ≥ 0, c ≠ 0, and w_0 = e_1
   gives v·(w_0 − q*) = −c_2q*_2 − c_3q*_3 < 0. ∎

**Lemma 3.4′ (faces; PROVED).** Under the same hypotheses, every point t ∈ Δ, including boundary points, lies in some
W(q).

*Proof.*
- **Relative interior of a face F.** Apply the proof of Lemma 3.4 inside F to the correspondence
  q ∈ F ↦ W(q) ∩ F. It has closed graph and convex values, and it meets Δ_{supp q} ⊆ F, so it is nonempty. The
  normal-cone computation is the same in lower dimension.
- **Vertices.** W(e_i) ∋ e_i, because W(e_i) meets Δ_{{i}} = {e_i}. ∎

This is the covering argument of AA2. AA_audit's repair is built in: the full correspondence W̃ is used for the closed
graph, and only the existence of a supported weight is used at the boundary.

**Corollary 3.5 (every tuple field has properties (γ₀) and (γ); PROVED).** In class I, with a selection continuous
in measure:
- for every tuple τ of a.e.-positive members and **every** t ∈ Δ, some selected model is a weak t-Bayes model of ℓ^τ
  (Lemma 3.4′). This is (γ₀) of Q4/M3.4.2: a coherent Bayes model at every weight;
- for every tuple τ of a.e.-positive members, and for a.e. w ∈ int Δ, the w-Bayes model of ℓ^τ is a.e. unique, and
  it equals a selected model, so it is coherent;
- if a model T ∈ C_L is tied everywhere with C_{q_0}, then T satisfies (WB) at every w ∈ W̃_τ(q_0).

*Proof.*
- **Null ties.** For two distinct kinds of advice a ≠ b, every world ranks them differently. So every component of
  v^τ_a − v^τ_b is nonzero a.e., and each tie set {w : w·(v^τ_a − v^τ_b)(h) = 0} is a line. By Fubini on Δ × H, ties
  are null for a.e. w.
- For such an interior w, Lemma 3.4 gives q with w ∈ W̃(q). A weak Bayes model with null ties equals the a.e.-unique
  Bayes model, so the Bayes model is C_q.
- **Ties.** Suppose T ~_i C_{q_0} at every world, with records f_i = Λ_iC_{q_0} − Λ_iT and −f_i both in 𝒜*_i.
  - The cases (f ∈ g + 𝒦, −f ∈ 𝒦) and (f ∈ g + 𝒦, −f ∈ g′ + 𝒦) are impossible. The first contradicts the
    (E)-witness of g. The second gives 0 ∈ g + g′ + 𝒦, which contradicts (P), whose right-hand side is ≥ 0.
  - So f_i ∈ 𝒦_i ∩ (−𝒦_i), and ∫f_iφ_i = 0. Thus T and C_{q_0} have the same ℓ^τ-loss vector.
  - Since C_{q_0} minimises w·ℓ^τ for w ∈ W̃(q_0), so does T. Minimisation of an additive loss is pointwise a.e., so
    T satisfies (WB). ∎

---

## 4. The incompatibility at T1 (task (3), failure branch)

**Theorem 4.1 (PROVED, modulo the imported chain listed below).** Let 𝓜 be a decomposable domain with (LF) at
D_{T1}: the full four-advice domain, or M_U. Let a ranking on 𝓜 satisfy strict (G), (IB) and (S), where (S) means a
coherent selection, competitive on supp q, with closed sections. Suppose:
- **(i)** the selection q ↦ C_q is continuous in measure;
- **(ii)** every world's acceptance relation lies in a finite-seed envelope: ⪯_i ⊆ ≤*_i for data 𝔈 with (E) and
  (P), bounded Ψ_i containing an a.e.-positive member, and finite G_i.

Then T1 ∉ C_L.

This holds for **every** world order inside the envelopes, complete or not, adding up or not, and with or without an
(M1) certificate. No additivity of partner worlds, no Brier-type edges and no continuity of densities are assumed.

*Proof.*
1. Suppose T1 ∈ C_L. By thm:kkm (it needs only (LA) and (S)), T1 is tied at every world with some selected C_{q_0}.
2. Fix τ := (φ_1^+, φ_2^+, φ_3^+). Then ℓ^τ is a strictly guiding additive field with bounded integral penalties.
3. By Cor 3.5, ℓ^τ has (γ), and the exceptional set E of weights with non-null ties is null.
4. Again by Cor 3.5 (which uses (P)), T1 satisfies (WB) for every w ∈ W̃_τ(q_0). This set is nonempty by Thm 3.1(a).
   So T1 minimises w·ℓ^τ, i.e. it is ℓ^τ-Bayes at w.
5. **Lemma 4.2:** w ∈ int Δ.
6. Theorem D1 (statement for any strictly guiding additive field with integrable envelope and (γ), on any (LF)
   domain) gives w ∉ E. So D_{T1} is the a.e.-unique ℓ^τ-Bayes model at the interior weight p* := w.
7. These are exactly the standing hypotheses (H1)–(H4) of M3.9 = BB2 Thm 6.1, which yields (C2) and (C3).
8. **The contradiction.**
   - By Cor 3.5, ℓ^τ is a non-degenerate (γ₀)-field (it is a ladder field in M3's normal form), with D_{T1} the
     unique Bayes model at p*, and (C2), (C3) and the cluster clause hold at p* (BB2 Thm 6.1). So Q4.1 applies: V_b = {e_b} and edge confinement M3.7(d).
   - On the full domain, (Av) holds trivially, and M3.8 gives the contradiction. M3.8 needs E null and p* ∉ E, both
     established above.
   - On M_U, Q4.1's Step 4 is already the contradiction (Prop T1), as recorded in BB2 Cor 7.1. ∎

**Lemma 4.2 (PROVED).** If D_{T1} satisfies (WB) for a strictly guiding field at w ∈ Δ, then w ∈ int Δ.

*Proof.*
- **Two-world weight.** Suppose w_3 = 0 and w_1, w_2 > 0.
  - Let t* := 2c_0/(c_0+ε). The gamble h* = (1, 1, −t*) lies on ∂D_{T1}, since v_3·h* = 0 and v_1·h*, v_2·h* > 0.
  - Gambles h = (1, 1, −t) with t slightly larger than t*, together with an open neighbourhood, lie in U ∖ cl D_{T1}.
    Here U ⊃ cl D_{T1} ∖ 0 is open, and on M_U we use this U; on the full domain any open N from (LF) will do.
  - On that non-null open set D_{T1} is silent, while "accept h" lies in the advice range and is good at worlds 1
    and 2.
  - (WB) with a = accept h gives w_1φ_1(λ_1(acc) − λ_1(sil)) + w_2φ_2(λ_2(acc) − λ_2(sil)) ≥ 0 there. Both terms
    are negative, which is a contradiction.
  - The other edges follow by symmetry.
- **Vertex weight.** For w = e_1, (WB) makes D_{T1} pointwise world-1-optimal on its advice range, i.e. D_{T1} = P_1
  a.e. on 𝓜. That is false. ∎

**Imported chain and its status** (each item as recorded in BB2 §7 and M3):
- thm:kkm [proved];
- Theorem D1 [R1, after repairs];
- M3.7(d), M3.8 [R1];
- M3.9 = BB2 Thm 6.1 [one reading, unrefereed];
- Q4.1 / Prop T1 [R1].

I checked that these statements apply to an arbitrary strictly guiding (γ)-field with D_{T1} Bayes at an interior
weight. Their stated standing data (BB2 (H1)–(H4); M3 §5) do not mention endorsers or fixed points. That check is
CHECKED by reading the statements; I did not re-derive them.

**Corollary 4.3 (the seed cannot be completed for T1 inside I; PROVED modulo the same chain).** No full system
satisfying I(𝔈) with a selection continuous in measure contains the seed of §1. The reason is that its base B_1 = D_{T1}
would be in C_L, whatever the remaining envelope data and partner worlds.

*Reading.*
- K2.6 and BB1 found this obstruction under additive or continuously endorsed partners, Brier-type edges, and the
  linear ansatz. Theorem 4.1 removes all of these.
- What it really uses: competitiveness against **small** moves sees only the cone part of the envelope (Thm 3.1). A
  cone of countably additive densities turns competitiveness into Bayes-optimality for an additive shadow. Continuity
  of the selection turns that into (γ), via covering (Lemma 3.4).
- Rigid seeds, however cleverly protected, are invisible to small moves. They cannot help T1 inside a finite-seed
  countably additive envelope.

---

## 5. What survives, and what a construction must therefore use

Theorem 4.1 is a theorem about the invariant class, not about all covers. A T1 cover with the seed's mechanism must
break at least one of its hypotheses. Each item below is an exact escape from a named step of the proof.

1. **Infinitely many seeds with margins tending to 0.** Step 8 of Thm 3.1(a) needs inf_g ∫gφ_E^g > 0 over the seeds
   meeting small moves. D2's thin sources ("only finitely many generators above any η", D2 (D3)) are exactly of this
   kind. So an envelope with countably many seeds whose (E)-margins → 0, accumulating at small moves, is not
   excluded. This is the natural next invariant: I_∞(𝔈) with G_i countable and (P) for all pairs. Lemma 2.1 survives
   unchanged; Lemma 2.3 needs local finiteness of the seeds above every η, as in D2.
2. **Envelopes that are not countably additive cones.** For example, duals of sets of finitely additive charges, or
   lexicographic cones. Thm 3.1(a) uses Lyapunov convexity of the range of finitely many countably additive
   integrals. With charges, the zonoid argument fails. AUDIT_AA's lexicographic cone is the simplest such envelope.
   Its closed-section behaviour is the open point.
3. **Selections not continuous in measure.** Only Lemma 3.3 (closed graph) uses continuity. Closed sections do not
   imply it. A selection with jumps along a fat level set is constrained by Cor 3.2 together with closedness (each
   jump must be ≤ both one-sided limits in every world's envelope functionals). I did not settle whether such jumps
   can occur.
4. **Targets other than T1.** Thm 2.4 reduces the existence of a full system with an (M1) world in class I to (Cov),
   (Prot), (Fit), (Cert). By Thm 3.1 these are concrete:
   - the selection must be weak-Bayes for every tuple;
   - the cell-concentrated (P)-witnesses must survive that (Cor 3.2);
   - (Cert) must hold.

   **CONJECTURE 5.1 (projective rigidity).** On any region of problems where the selection's charts form a
   2-parameter family of lines (non-degenerate), every φ ∈ Ψ_1 coincides there with a member of K2.5's linear family
   c_0φ_1^+ + c_1φ̃_2 + c_2φ̃_3.

   *Evidence.* Two tuples differing only in world 1 induce, through their (WB) weights, a map of the weight simplex
   taking a 2-parameter family of lines to lines. Locally such a map is projective. It fixes the pencil structure
   forced by the shared partners, which leaves the affine form. I have not controlled the measurability and
   uniqueness of the weights needed to make this rigorous.

   If CONJECTURE 5.1 holds, K2.6's SPREAD/ADJ argument closes class I over non-degenerate selections for **every**
   target. The only room left is degenerate (pencil) chart regions carrying the cells. That is K2's question
   (Q-K2b), now without the additive-partner hypothesis.

Note on the brief's directives. Theorem 4.1 applies equally to two additive partners (Ψ_2, Ψ_3 singletons) and to
three jointly built incomplete worlds. Building the worlds jointly does not by itself escape it. What escapes it is
leaving the finite-seed countably additive envelope, or the continuity of the selection.

---

## 6. Status

| Item | Statement | Label |
|---|---|---|
| 1.1(a) | K4 seed through T1 on the full domain (and M_U); penalty- and ladder-robust certificate Σg_k ≤ 0, ≠ 0 | CHECKED (exact rational); PROVED (consequence) |
| 1.1(b) | realisable compositions with guidance contain ≤ 1 seed record; no strict reversal | PROVED; CHECKED (exhaustive cell model) |
| 1.1(c) | rigid (K2.1) relative to the seed closure; N17 shape; X_k improves at worlds 2 and 3 | PROVED; CHECKED |
| 2.0 | seed admits envelope data (E), (P) at world 1 | PROVED |
| 2.1–2.3 | envelope relations are preorders with strict (G), (IB); I(𝔈) preserved by closure, unions, fixed-plan sections | PROVED |
| 2.4 | extension problem inside I is exactly static: (Cov), (Prot), (Fit) ⇒ full system with the seed intact; (Cov) necessary | PROVED |
| 3.1 | (Cov) ⇔ the selection is weak-Bayes for every tuple of envelope densities | PROVED |
| 3.2 | edge form: common threshold sets; cell witnesses need steep partner mass decay | PROVED |
| 3.3–3.5 | closed graph, covering lemma (Brouwer + Browder), property (γ) for every tuple field | PROVED |
| 4.1 | finite-seed countably additive envelopes + continuous selection ⇒ T1 ∉ C_L | PROVED modulo D1, M3.7(d), M3.8, M3.9 (BB2), Q4.1; applicability CHECKED by reading |
| 4.3 | the seed of §1 cannot be completed to a T1 system inside I | as 4.1 |
| 5.1 | projective rigidity ⇒ linear endorsers on non-degenerate chart regions | CONJECTURE |
| — | full system (any target) with the seed's non-endorsement intact | **not achieved** |

## 7. Files (`cc1py/`, run `python3 -I <name>.py` inside the folder)

- `seed_exact.py` → `seed_exact.out`: exact rational verification of the cells, the K4 pattern, the certificate,
  pairwise positive overlaps, crossing, and the world-2/3 effects (CHECKED).
- `closure_check.py` → `closure_check.out`: exhaustive search on the seven-cell ladder model; no reachable strict
  reversal; at most one seed per composition (CHECKED).
- `lp_seed.py`, `lp_seed2.py`, `lp_seed3.py`, `lp_margin.py`: LP searches that found the configuration (NUMERICS;
  the result is re-verified exactly by `seed_exact.py`). `lp_margin.py` writes `best_seed.txt`.
- `search_seed.py`: an abandoned sampling search, kept for the record.
