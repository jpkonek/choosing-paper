# N17. Rankings that do not add up: what a T1 cover would need, and whether (S) allows it (exploratory)

13 Oct 2026. Labels: **PROVED** (full proof here), **CHECKED** (verified, proof sketched or imported by inspection),
**CONJECTURE**, **NUMERICS** (scripts in `n17py/`; no proof depends on them).

**Standing hypotheses (H).**
- n = 3 unless stated otherwise.
- T = T1 = D_K, with K = (1−ε)u + εΔ, vertices v_j = (1−ε)u + εe_j, and c0 = (1−ε)/3. Numbers use ε = 0.3.
- Domain: R3's U-domain M_U (N9.4), whose evaluable models are the measurable subsets of U. Here U = D_{K′}, K′ = u + s(K−u), s ∈ (0,1); s = 0.9 in numerics.
  M_U has (LF) at T and is the domain of N10's frontier statement F3.
- Each world has a preorder with strict (G) and (IB) on M_U. The axioms are (LA), (S) in LDG's preorder sense, (C), (E).
- Fact 0 = LDG thm:kkm for preorders: every X has a selected C with C ⪯_j X at every world j.
- Lemma IC (R11, refereed in R13): T ∈ C_L is competitive on Ω.
- No selection is assumed Bayes for its index. No completeness or continuity is assumed.

**Notation (N9.4).**
- P_i = U ∩ {h_i > 0}, and E_i(X) = X △ P_i is the world-i error set. The ranking ⪯_i is a relation ≤_i on measurable
  subsets of U: strictly monotone, cancellative (A ≤ B ⇔ A∖B ≤ B∖A), and a preorder.
- 𝒞 is the set of measurable {−1,0,1}-valued functions on U, modulo null sets. The *acceptance set* is
  𝒜_i = {1_B − 1_A : A ≤_i B}. By cancellation, A ≤_i B ⇔ 1_B − 1_A ∈ 𝒜_i.
- 𝔚_i = {1_{E_i X} − 1_{E_i C} : C ∈ C_L, C ⪯_i X}. These are the comparisons made from coherent undominated models.
- 𝔉_i is a *cover family*: for each non-null A, finitely many vectors 1_A − 1_{Q_k} ∈ 𝒜_i whose sets Q_k cover U. It
  exists iff world i is *fine*.
- (NC_𝔊): no finite nonnegative combination of members of 𝔊 is ≤ −1.
- (NC⁺_𝔊): no such combination is ≤ 0 and ≠ 0.
- (NC) means (NC_{𝒜_i}).
- "Does not add up" means that (NC) fails at that world.

---

## 0. Outcome

**Verdict.** The route is **not closed, and no evidence was found that it is open.**

On the negative side for impossibility proofs:
- (NC)-violating worlds can be fine (N17.7).
- They are compatible with every axiom, (S) included (N17.8, n = 2).
- Even two additive worlds leave T1's competitiveness consistent (N17.4).

On the negative side for the route:
- In the only system I could build, the violation is *decorative*. The world still satisfies (NC) on 𝔚, the comparisons
  the reduction uses (N17.8(c)).
- A useful violation must sit inside 𝔚. It must be built on a cycle of selected models whose error sets cross
  (N17.3), and it must reverse a continuum of near-T comparisons (N17.5).
- The literal finite-atom test the brief proposes cannot satisfy (S) for any target (N17.6).

Numbered claims:

**N17.1 (PROVED) Single-layer normal form for (NC).** On M_U:
- (a) The acceptance sets of rankings with (G) and (IB) are exactly the sets 𝒜 ⊆ 𝒞 such that:
  - 𝒜 contains every δ ≥ 0;
  - 𝒜 contains no δ ≤ 0 with δ ≠ 0;
  - 𝒜 is closed under every pairwise sum that stays in 𝒞.
- (b) *Chaining lemma.* If δ_1, …, δ_m ∈ 𝒜 have pairwise disjoint positive parts and pairwise disjoint negative parts,
  then Σ δ_k ∈ 𝒜. Hence Σ δ_k is not ≤ 0 unless it is 0. In particular there is no "money pump": no cyclic family of
  accepted trades I_k ≤ J_k with the I_k disjoint, J_k ⊆ I_{k+1} (indices mod m), and some I_{k+1}∖J_k non-null.
- (c) (NC_𝔊) holds iff some finitely additive probability ν (vanishing on null sets) has ν ≥ 0 on 𝔊. This is IRC
  Thm NC(a). If 𝔊 ⊇ 𝔉_i, every such ν is strictly positive, and (NC_𝔊) ⇔ (NC⁺_𝔊). On M_U only the cover clause is
  needed: there is a single layer, so IRC's two "pairs" are superfluous.
- (d) Any violation of (NC) needs at least 5 accepted exchanges, counted with multiplicity, two of which have
  overlapping positive parts on a non-null set (IRC Lemma smallcanc, plus counting). One layer of IRC Example half5
  attains 5.

**N17.2 (PROVED for CA charges; CHECKED for general charges) Only 𝔚 matters, and this is where a cover must stop
adding up.** Suppose every world i has a strictly positive charge ν_i with ν_i ≥ 0 on 𝔚_i (equivalently, by N17.1(c),
(NC_{𝔚_i ∪ 𝔉_i})), with countably additive part of density ρ_i > 0 a.e. Then the system is in N13 Prop B's class:
- an integral field ψ_i(X) = ∫_{E_i X} ρ_i dμ;
- T Bayes at an interior weight;
- for a.e. weight, the Bayes model is a.e. unique and selected, hence coherent;
- coherent Bayes models at every weight, and the vertex models P_i.

Consequently every T1 cover outside the additive class has a world i at which one of the following holds:
- (i) (NC_{𝔚_i ∪ 𝔉_i}) fails ("does not add up where it matters");
- (ii) it holds, but no weak charge has an a.e.-positive countably additive part;
- (iii) world i is not fine and every weak charge vanishes on a non-null set (blind regions, as in N9 Design B).

"Must" is conditional, because Prop B's class is excluded only under N14 §6 ((DD), and uniqueness at every weight).

**N17.3 (PROVED) Shape of a useful cancellation.** Let δ_k = 1_{E_i X_k} − 1_{E_i B_k} ∈ 𝔚_i, with λ_k > 0,
Σ λ_k δ_k ≤ 0 and Σ λ_k δ_k ≠ 0. Then:
- the positive part of each δ_k lies outside E_i(B_k) and inside ∪_{l≠k} E_i(B_l);
- no B_k has an error set E_i(B_k) that contains all the others.

Hence, if the world-i error sets of the members of C_L form a chain, (NC⁺_{𝔚_i}) holds automatically. A useful
violation needs at least two undominated models with crossing world-i error sets, arranged cyclically. For coherent
models, E_i(D_M) ⊆ E_i(D_{M′}) iff D_{M′} ∩ {h_i > 0} ⊆ D_M and D_M ∩ {h_i < 0} ⊆ D_{M′}. So crossing is generic in
n = 3 and nothing is excluded. By contrast, a selection along a nested path (as in n = 2) has no useful violation.

**N17.4 (PROVED) Two additive worlds: the edge lemma.** Let worlds 1 and 2 have weak charges on 𝔚 with CA densities
ρ_1, ρ_2 > 0 a.e. Let world 3 be arbitrary, and put r = ρ_2/ρ_1. Then:
- **(a)** For all but countably many s ∈ (0,1), the two-world Bayes model B_s (accept h iff s ρ_1 σ_1(h) + (1−s) ρ_2 σ_2(h) > 0)
  is a.e. equal to a selected model, hence coherent.
- **(b)** Exchange-rate condition: ess inf_{R_a} r ≥ ess sup_{R_b} r, where
  - R_a = [(+,−,+)∖T] ∪ [(−,+,−) ∩ T];
  - R_b = [(−,+,+)∖T] ∪ [(+,−,−) ∩ T].
- **(c)** Suppose the interval [ess sup_{R_b} r, ess inf_{R_a} r] has interior. Take any s* with s*/(1−s*) in that
  interior and with null ties. Then B_{s*} = D_M ∩ U, where:
  - the ratios {m_1/m_2 : m ∈ M} are exactly K's, namely [c0/(c0+ε), (c0+ε)/c0] = [0.4375, 2.2857];
  - M meets the edge [e_1, e_2].

NUMERICS: Brier-type ρ_i = |h_i| fails (b) (0.440 < 2.277). The facet-switching field of §5 satisfies (b) with
c* = 1.

**N17.5 (PROVED / CONJECTURE / NUMERICS) Where the reversals must sit.**
- (PROVED) Take any CA strictly positive triple ν and any interior weight t with null ties at which the ν-Bayes model
  B_t is incoherent. Then the cover contains a selected C and a world j with C ⪯_j B_t but ν_j(E_j C) > ν_j(E_j B_t).
  Call this a ν-reversal.
- (CONJECTURE) The additive no-go is local at p\*: N12's argument works with P(p\*+tδ, ·) as t ↓ 0, at the crossings
  and corner rays of ∂T. If so, the forced reversals can be taken against models B_t → T, and they differ from coherent
  models only near the corner rays and crossings of ∂T.
- (NUMERICS) For the facet-switching field, ρ_i(h) = v_{j(h),i}|h_i| with j(h) = argmin_j v_j·h, T1 is the Bayes model
  at u. For t near u, B_t differs from the natural coherent candidate D_{K_t} only within distance about 0.005 of the
  corner rays of D_T. All non-convexity witnesses found sit there.
- (PROVED, N9 Cor 3.3) Any dominating C whose index lies near the target fibre is competitive only on Ω, never on an
  edge.

**N17.6 (PROVED) Finite-atom models cannot test (S), for any target.** Suppose the measure algebra is replaced by a
finite Boolean algebra, with strict (G) at two worlds and (S) with closed sections on Δ. Then:
- the closed tie-class fibres (N9.2) are finitely many;
- they partition each connected edge, so there is only one fibre on it;
- but P_1 ≺_1 P_2, a contradiction.

So the suggested "finite atoms + triangulation + closed sections" configuration is inconsistent before any ranking is
chosen. A heuristic must keep an atomless algebra. The constructions below use finitely many *cells*, with atomless
sets inside each cell, and they are exact, not heuristics.

**N17.7 (PROVED) Fine (NC)-violating worlds exist.** Take ten cells R_S of measure 1/10 partitioning U, one for each
2-subset S ⊆ {1..5}. Let g_i = +1 on C_i = ∪_{S∋i} R_S and −1 elsewhere. For θ < 1/25 put
- G_θ = {δ : μ(δ⁻) ≤ θ μ(δ⁺)};
- 𝒢_i = {δ : μ(C_i ∖ δ⁺) + (θ/(1−θ)) ∫(1−δ) ≤ 1.2θ/(1−θ)}.

Then 𝒜 = G_θ ∪ 𝒢_1 ∪ … ∪ 𝒢_5 is the acceptance set of a fine ranking with (G) and (IB), with g_i ∈ 𝒜 and
Σ g_i = −1. So it has no weakly agreeing charge at all.
- (CHECKED) The same construction on IRC's two-layer space H′ × {1,2} is fine and has an SI pair and a weakly AC pair.
  It violates (NC), so it has no full extension (IRC Cor NCext(i)).
- This answers IRC §EXT's remark "we know no fine world with (IB) that violates (NC)" at the level of the order
  axioms. Whether (S), (T1o) and (EP) exclude such worlds is untouched.

**N17.8 (PROVED) Compatibility with (S), but decorative (n = 2).**
- (a) There is a two-world system on the U-domain satisfying strict (G), (IB), (LA), (S), (C), (E) and
  (LF). World 2 is additive. World 1 is fine and violates (NC). Every coherent model on the selection path is
  vindicated.
- (b) The violation is invisible to the reduction: world 1 satisfies (NC_{𝔚_1}), with the strictly positive density
  e^{Mx}.
- (c) More generally, in any two-world system whose selected world-1 error sets are nested, (NC⁺_{𝔚_1}) holds (N17.3).

So "does not add up" is compatible with closed competitive choice, but in this example it does no work.

**N17.9 Assessment (§7).**
- (a) No ranking-level theorem excludes the route.
- (b) Against the route: every known (NC)-violation is either outside 𝔚, or built from rigid exact-cover acceptances
  (half5 type). A T1 cover needs reversals inside 𝔚, against a continuum of incoherent near-T models (N17.5), produced
  by a cyclic, overlapping arrangement of crossing error sets of selected models (N17.3, N17.1(d)). No such
  arrangement is known, even as a decoration.
- (c) For the route: T1's additive contradiction is a cyclic "holonomy" condition around the three corners of D_T
  (N12 Thm 3.1, final step). Non-additive rankings are exactly those that can carry a non-potential exchange structure.
  N17.1(b) shows the simple money-pump direction is forbidden for every ranking. The open question is whether the
  T1 certificate can be written with disjoint supports (then it would kill every ranking) or needs overlapping ones.
- CONJECTURE N17.A: two worlds as in N17.4 already exclude T1 (the T1 analogue of TAW, which would give the analogue
  of IRC Cor twoNC).
- CONJECTURE N17.B: (S) forces (NC⁺_{𝔚_i}) at every world.

---

## 1. Single-layer normal form (N17.1)

**(a)** This is N9 Prop 1.1 written in vectors.
- If 𝒜 is the acceptance set of a ranking, then:
  - δ ≥ 0 is weak (G);
  - excluding δ ≤ 0, δ ≠ 0 is strict (G);
  - for sum-closure, take δ = 1_B − 1_A ∈ 𝒜 and δ′ ∈ 𝒜 with δ + δ′ ∈ 𝒞. Choose pointwise: if δ = 1, put A ∌ h ∈ B;
    if δ = −1, put A ∋ h ∉ B; if δ = 0, put h in B or not according to δ′. Then there is C with 1_C − 1_B = δ′
    (IRC Lemma accept(c), single layer). So A ≤ B ≤ C and δ + δ′ = 1_C − 1_A ∈ 𝒜.
- Conversely, given such an 𝒜, define A ≤ B ⇔ 1_B − 1_A ∈ 𝒜. This is reflexive (0 ≥ 0), transitive (sum-closure), and
  cancellative (it depends only on 1_B − 1_A). It is monotone and strictly monotone by the two sign conditions.

**(b)** At each point at most one δ_k is +1 and at most one is −1. So every partial sum lies in 𝒞, and (a) applies
inductively. The sum is then accepted, so it is not ≤ 0 unless it is 0.

For the money pump:
- The I_k are disjoint, and J_k ⊆ I_{k+1} makes the J_k disjoint.
- Σ(1_{J_k} − 1_{I_k}) = −Σ 1_{I_{k+1} ∖ J_k}. This is ≤ 0 and non-zero, which is impossible. ∎

**(c)** "If" is IRC Thm NC(a), with Ω′ replaced by U. The proof is a minimax argument on the finite algebra generated by
the γ's, followed by Tychonoff, and uses nothing about rankings. "Only if": ν(Σ λ γ) ≤ −1 < 0 contradicts ν ≥ 0.

Strict positivity: ν(U) = 1. For non-null A, a cover 1_A − 1_{Q_k}, k ≤ q, gives ν(Q_k) ≤ ν(A), so
1 ≤ Σ ν(Q_k) ≤ q ν(A).

(NC⁺) from (NC) under fineness: suppose c = Σ λ γ ≤ 0 and c ≤ −η on a non-null S. Then
(q/η) c + Σ_k (1_S − 1_{Q_k}) ≤ q 1_S − 1_U − q 1_S = −1_U. ∎

**(d)** Suppose Σ γ_k ≤ −1, with rational weights cleared (IRC §NCsetup). Lemma smallcanc (single layer, (G) + (IB))
gives a non-null set where two γ's equal +1. There, ≤ −1 needs at least three −1's, so m ≥ 5.

One layer of half5 (IRC Ex. half5) is the ranking with acceptance set {δ : δ ≥ 0 or δ ≥ g_i for some i}. Its proof
there is layerwise and carries over. Σ_{i≤5} g_i = −1. ∎

## 2. Only 𝔚 matters (N17.2)

**Prop 2.1 (PROVED).** Assume (H). Suppose that at each world ν_i is a countably additive measure ρ_i μ, with ρ_i > 0
a.e. on U and ν_i ≥ 0 on 𝔚_i. Put ψ_i(X) = ν_i(E_i X). Then:
- (α) T is ψ-Bayes at some π ∈ int Δ;
- (β) for Lebesgue-a.e. t ∈ Δ the ψ-t-Bayes model B_t is a.e. unique and equals a selected model, hence is coherent
  and in C_L;
- (γ) B_{e_i} = P_i.

*Proof.*
- **(α)**
  - By Lemma IC, for each X some i has T ⪯_i X. The vector 1_{E_i X} − 1_{E_i T} lies in 𝔚_i, so ψ_i(T) ≤ ψ_i(X).
    Hence no X has ψ(X) < ψ(T) in every coordinate.
  - The attainable set {ψ(X) : X ∈ M_U} is convex and compact (Lyapunov; R2 §1).
  - Separation gives π ∈ Δ with π·ψ(T) ≤ π·ψ(X) for all X.
  - Suppose π_3 = 0. Silence T on T ∩ {h_1 < 0, h_2 < 0}. This set is non-null (N9 Cor 3.3), and silencing it lowers
    ψ_1 and ψ_2 strictly (ρ > 0), contradicting minimality. The other faces are similar, and at a vertex T would equal
    P_i.
- **(β)**
  - Accepting h costs Σ_{h_i<0} t_iρ_i. Silence costs Σ_{h_i>0} t_iρ_i.
  - For each mixed h the tie set of weights is a chord of Δ. By Fubini on Δ × U, μ(ties at t) = 0 for a.e. t.
  - Fix such a t. Fact 0(a) gives a selected C with C ⪯_j B_t at every j. Then ψ_j(C) ≤ ψ_j(B_t), so C is t-Bayes and
    C = B_t a.e.
- **(γ)** This is the vertex lemma. ∎

*Remarks.*
- (W) is used only for comparisons out of T and out of selected models, i.e. inside 𝔚. For a merely finitely additive
  ν_i with CA part ρ_i > 0 a.e., the same conclusions are N13 Prop B (α)–(δ). By inspection of its proof and of N11
  Cor 3.2, (W) is again invoked only on 𝔚 (CHECKED).
- Unlike N11.2, detection is not needed. On M_U the Bayes rule is pointwise, so uniqueness at a.e. weight comes from
  ρ > 0 alone. That is the price N13 noted: Prop B's class is excluded only modulo "uniqueness at every weight", the
  N13 open point, and N14's (DD).

**What the analogue of IRC Thm twoNC / Cor twoNC gives for T1.** IRC's chain is:
1. (S) and (T1o) give fineness and the two pairs (V-specific edge sweeps).
2. Cor NCext: (NC_{𝔚∪𝔉}) ⇔ the world is a (W)-world.
3. TAW: at most one (W)-world.
4. Hence at least two worlds violate (NC).

For T1 on M_U:
- Step 2 is N17.1(c). It is simpler: one layer, no pairs.
- Step 1 is open. I found no argument that (S) forces fineness of ≤_i for T1. The V proof sweeps edge selections
  E^y_x(a) along the vacuous model's silence, and T1 has no analogue.
- Step 3 has only its three-world version, Prop 2.1 combined with N14 (conditional).

So the T1 statement is: *at least one* world fails (NC_{𝔚∪𝔉}), or alternative (ii) or (iii) of §0 holds, conditional
on N14's hypotheses. "At least two" is CONJECTURE N17.A. §4 gives what two (W)-worlds force.

## 3. Shape of a 𝔚-cancellation (N17.3)

**Lemma 3.1 (PROVED).** Let δ_k = 1_{E_i X_k} − 1_{E_i B_k} ∈ 𝔚_i (k ≤ m), with λ_k > 0 and
Σ_k λ_k δ_k ≤ 0 a.e. Then:
- for every k, δ_k⁺ := E_i(X_k) ∖ E_i(B_k) ⊆ ∪_{l≠k} E_i(B_l) a.e.;
- if some E_i(B_{k₀}) contains every E_i(B_l), then δ_{k₀} = 0.

Consequently, if {E_i(C) : C ∈ C_L} is totally ordered by inclusion (mod null sets), (NC⁺_{𝔚_i}) holds.

*Proof.*
- At a point of δ_k⁺, the sum is ≤ 0 only if some δ_l = −1 there. That means the point lies in
  E_i(B_l) ∖ E_i(X_l) ⊆ E_i(B_l), with l ≠ k.
- If E_i(B_{k₀}) ⊇ E_i(B_l) for all l, then δ_{k₀}⁺ lies outside every E_i(B_l), so it is null. Then δ_{k₀} ≤ 0, and
  it is accepted, so δ_{k₀} = 0 by strict (G).
- In a chain, remove the vector with the largest error set and induct. All δ_k vanish and the sum is 0. ∎

*Reading.* A cancellation that matters must be cyclic: each selected model's improvement region is paid for inside
other selected models' error sets. With N17.1(d), there are at least 5 exchanges and overlapping positive parts. For
coherent models, E_i(D_M) ⊆ E_i(D_{M′}) iff D_{M′} ∩ {h_i > 0} ⊆ D_M ∩ {h_i > 0} and D_M ∩ {h_i < 0} ⊆ D_{M′}. So
two credal sets give nested world-i error sets only if one model is more cautious on world-i-good gambles and bolder on
world-i-bad ones. In n = 3 near T this is not forced, and Lemma 3.1 excludes nothing for T1.

## 4. Two additive worlds (N17.4)

Hypotheses: (H). At worlds 1 and 2, ν_j = ρ_j μ with ρ_j > 0 a.e. and ν_j ≥ 0 on 𝔚_j. World 3 is any preorder with
strict (G) and (IB).

**(a) Proof.**
- On problems where σ_1(h) ≠ σ_2(h), the tie set Z_s = {s ρ_1 = (1−s) ρ_2} determines s. So the Z_s are disjoint and
  only countably many are non-null.
- For other s, B_s is the a.e.-unique minimiser of Φ_s = s ψ_1 + (1−s) ψ_2 (pointwise).
- Fact 0(a) gives a selected C ⪯_j B_s at j = 1, 2, 3. Since C ∈ C_L, (W) at worlds 1 and 2 gives Φ_s(C) ≤ Φ_s(B_s).
  So C = B_s a.e.
- World 3 and (C) are not used. ∎

**(b) Proof.**
- Label each problem by its exchange from T: add h ∉ T, or remove h ∈ T. Every point of R_a ∪ R_b is a world-3 gain.
  On R_a the move changes (ψ_1, ψ_2) by (−ρ_1, +ρ_2); on R_b by (+ρ_1, −ρ_2).
- Suppose ess inf_{R_a} r < c < ess sup_{R_b} r. Take a non-null B ⊆ R_b ∩ {r > c}. Then take A ⊆ R_a ∩ {r < c} with
  ν_1(A) = (1+η) ν_1(B). Here η > 0 is small and Lyapunov (non-atomic ν_1) is used.
- Then ν_2(A) < c ν_1(A) = c(1+η) ν_1(B) < ν_2(B) for small η. So X = T △ (A ∪ B) has ψ_1(X) < ψ_1(T) and
  ψ_2(X) < ψ_2(T).
- X is a strict pointwise world-3 improvement of T, so X ≺_3 T.
- Lemma IC gives some j with T ⪯_j X. Worlds 1 and 2 are excluded by (W), since T ∈ C_L, and world 3 is excluded.
  Contradiction. ∎

**(c) Proof.**
- Take κ* = s*/(1−s*) in the interior of the interval, with null ties. Then B_{s*} rejects (+,−,+)∖T and (−,+,+)∖T,
  and accepts (+,−,−) ∩ T and (−,+,−) ∩ T. On (+,−,·) it accepts iff r < κ*; on (−,+,·) iff r > κ*. This gives the
  four agreements.
- By (a), B_{s*} = D_M ∩ U with M ⊇ K′.
- A.e. inclusions of open sets are inclusions up to closure. So D_M ∩ (+,−,+) ⊆ cl T. Suppose a point
  (h_1, h_2, 0) with h_1 > 0 > h_2 and |h_2|/h_1 > ρ₋ := c0/(c0+ε) lay in D_M. Being open, D_M would contain points
  with small h_3 > 0 outside cl T, which is impossible. So the trace of D_M on Q₊₋ = {h_1 > 0 > h_2, h_3 = 0} lies in
  {|h_2|/h_1 < ρ₋}.
- Conversely T ∩ (+,−,−) ⊆ cl D_M. For an open convex cone meeting the plane, cl(D_M) ∩ plane = cl(D_M ∩ plane). So
  the open trace contains {|h_2|/h_1 < ρ₋}.
- The trace on Q₊₋ is {|h_2|/h_1 < min_M m_1/m_2}. Hence min_M m_1/m_2 = ρ₋, and symmetrically max_M m_1/m_2 = 1/ρ₋.
- B_{s*} rejects every (−,−,·) problem in U. These include (−1, −1, L) for all large L. Compactness then gives m ∈ M
  with m_3 = 0. ∎

*Reading.* Two additive worlds turn the edge [e_1,e_2] into an additive two-world chart. They pin the exchange rate
c* = π_1/π_2 at which T sits, and force a coherent edge model that copies K's (1,2)-ratio range. For instance, with
m_e = (c0, c0+ε, 0)/(2c0+ε) and m_e′ = (c0+ε, c0, 0)/(2c0+ε), the set M = conv(K′ ∪ {m_e, m_e′}) is consistent with
(c), so there is no contradiction yet.

Conversely, for ρ_1, ρ_2 with null ties at c*, a strictly positive ρ_3 making T jointly Bayes always exists. On world-3
gains it is bounded above by the positive quantity −(π_1τ_1ρ_1 + π_2τ_2ρ_2)/π_3; on world-3 losses it is bounded below.
These are disjoint regions. So T's competitiveness alone never forces world 3 to violate (NC). Any T1-TAW
(CONJECTURE N17.A) must use (S) at selected models other than T.

NUMERICS (`t1_fields.py` (A)):
- Brier-type ρ_i = |h_i|: inf_{R_a} r = 0.440 < sup_{R_b} r = 2.277, so (b) fails. These are the predicted
  c0/(c0+ε) = 0.4375 and (c0+ε)/c0 = 2.2857.
- Facet-switching field: inf = 1.004 ≥ sup = 0.9985, so (b) holds with c* = 1.

## 5. Where the reversals must sit (N17.5)

**Lemma 5.1 (PROVED).** Let ν be CA with densities ρ_j > 0 a.e. Let t ∈ int Δ have null ties, and let the ν-t-Bayes
model B_t be incoherent. Then some selected C and some world j have C ⪯_j B_t and ν_j(E_j C) > ν_j(E_j B_t).

*Proof.* Fact 0(a) gives a selected C ⪯_j B_t at every j. Suppose ν_j(E_j C) ≤ ν_j(E_j B_t) for all j. Then C is
t-Bayes, hence C = B_t a.e., and B_t is coherent. ∎

Consider any candidate "additive shadow" ν that makes T Bayes at an interior π. One example is the facet-switching field
ρ_i(h) = v_{j(h),i}|h_i|, for which Σ_i u_i ρ_i σ_i = (1/3) min_j v_j·h. N14 §6 gives incoherent B_t under its
hypotheses, and the cover must then reverse ν at those B_t.

**CONJECTURE 5.2 (locality).** N12/N14's contradiction uses only Bayes models at q → p\* (pivot chords, crossings w_{ik},
corner rays r_{kj}, the edge box). So the incoherent B_t can be taken with t → π, B_t → T in measure, differing from a
coherent model only near the corner rays and crossings of ∂D_T. I have not re-verified that N12's proof never uses
far-away weights. The edge box N12.3 uses whole charts, which are half-planes by additivity and not by coherence.

**NUMERICS** (`t1_fields.py` (B), (C)), facet-switching field, t = u + d with |d| ≤ 0.04:
- B_t △ D_{K_t} has measure about 10⁻⁴ μ(U). On it the median distance to ∂T is 0.005–0.010, and the median seam gap
  (second-smallest minus smallest v_j·h) is 0.002–0.004, against 0.125 on U. So it sits at the corner rays.
- Non-convexity witnesses (h, h′ ∈ B_t, h + h′ ∈ U ∖ B_t) occur only in samples concentrated near corner rays, for
  example at r_12 with sign pattern (−,−,+).
- Which corners are involved depends on the direction of t − u.
- For this shadow, the cover must reverse comparisons between selected models and *corner-perturbations* of models near
  T. By N9 Cor 3.3, any of those selected models indexed near the target fibre is competitive only on Ω.

## 6. Finite models and the explicit configurations (N17.6–N17.8)

**Prop 6.1 (N17.6, PROVED).** Replace the measure algebra by a finite algebra 2^N. Models are unions of atoms, P_1 ≠ P_2
are unions of atoms, worlds 1 and 2 have strict (G), and (S) holds with closed sections on Δ. Then there is a
contradiction.

*Proof.*
- Vertex: u_{e_1} ⪯_1 P_1 gives E_1(u_{e_1}) ≤_1 ∅. Strict monotonicity then gives u_{e_1} = P_1. Likewise
  u_{e_2} = P_2.
- The fibres {p : u_p ~ C at every world} are closed (N9 Lemma 3.1) and there are at most 2^N of them. They partition
  the connected edge [e_1,e_2], so there is only one.
- But E_1(P_1) = ∅ ⊊ E_1(P_2), so P_1 ≺_1 P_2. ∎

The same argument, with Sierpiński, gives uncountably many fibres on every edge in the atomless case (N9.2). So the only
honest finite heuristics drop closedness, and then they test nothing (S)-specific.

Instead I use finitely many **cells** carrying atomless sets. The constructions are exact.

**Prop 6.2 (N17.7, PROVED).** Notation as in §0. Put κ = θ/(1−θ), W_i(s) = μ(C_i ∖ s⁺) + κ ∫(1−s) dμ, and
𝒢_i = {W_i ≤ 1.2κ}. If θ < 1/25, then 𝒜 = G_θ ∪ ⋃_i 𝒢_i satisfies N17.1(a), is fine, and violates (NC).

*Proof.*
- **G_θ is sum-closed.** Write a = μ(δ⁺), b = μ(δ⁻), and a′, b′ likewise; let x, y be the cross-cancellations. Then the
  negative part of the sum is b + b′ − x − y ≤ θ(a + a′) − x − y ≤ θ(a + a′ − x − y).
- **W_i does not increase under G_θ-steps.** Let s ∈ 𝒞 and t ∈ G_θ with s + t ∈ 𝒞. The deficit increases only where
  s = 1 and t = −1, so δD ≤ μ(t⁻). Also δcap = μ(t⁻) − μ(t⁺). So
  δW ≤ (1+κ)μ(t⁻) − κμ(t⁺) ≤ μ(t⁺)[θ(1+κ) − κ] = 0. Hence 𝒢_i + G_θ ⊆ 𝒢_i.
- **Two 𝒢's cannot be added.** For s ∈ 𝒢_i we have μ(C_i ∖ s⁺) ≤ 1.2κ. For i ≠ j, s ∈ 𝒢_i and s′ ∈ 𝒢_j are both +1
  on a part of R_{ij} of measure at least 0.1 − 2.4κ > 0 (κ < 1/24). So s + s′ = 2 there. For i = j use C_i:
  0.4 − 2.4κ > 0.
- **Sign conditions.** G_θ ⊇ 𝒞₊. A nonpositive non-zero s is excluded from G_θ trivially, and from 𝒢_i since there
  W_i ≥ μ(C_i) = 0.4 > 1.2κ.
- **Generators.** Every δ ≥ g_i has W_i ≤ 0 + κ · 2 · 0.6 = 1.2κ, so g_i ∈ 𝒢_i.
- **(NC) fails.** Σ_i g_i = −1_U, since every cell lies in two C_i's and outside three.
- **Fine.** For non-null A, every Q disjoint from A with μ(Q) ≤ θμ(A) has Q ≤ A, and finitely many such Q together
  with A cover U. ∎

*Two-layer version (CHECKED).*
- Run the construction on Ω′ = H′ × {1,2} with cells R_S × {1,2} and measure μ ⊗ counting/2. Keep only change vectors
  in IRC's 𝒞; the g_i take the values (1,1) and (−1,−1), which are allowed. Sum-closure for 𝒞-valued sums follows from
  the single-layer case.
- Debt and credit covers come from G_θ.
- An SI pair (D,Z) needs μ(D) ≤ θμ(Z). A weakly AC pair (D′,Z′) needs μ(Z′) ≤ θμ(D′).
- So IRC Cor NCext(i) applies: no full extension.

NUMERICS (`fine_world.py`, 40 bins, exact rationals):
- No increase of W_i in 20 000 random steps.
- At θ = 0.7 an explicit two-step chain reaches a nonpositive non-zero vector, so the smallness of θ matters.
- At θ = 0.039, 300 adversarial chains stay inside 𝒜 and never reach one.

**Prop 6.3 (N17.8, PROVED). A two-world system with all the axioms and a fine (NC)-violating world.**

*Problem side.*
- n = 2, K′ = [a′, b′] ⊂ (0,1), U = D_{K′}.
- The mixed problems (mixed pairs on which evaluable models can differ) form L = {x < α′} (g ∈ U; advice range {accept g, silence}) and R = {x > β′} (−g ∈ U; advice range {accept −g, silence}), with
  x = |g_2|/g_1. (On mixed pairs with α′ ≤ x ≤ β′, g ∉ U and −g ∉ U, so every evaluable model gives no advice.)
- Coherent models: X_{α,β} = {x < α} ∪ {x > β}, with α ≤ α′ < β′ ≤ β.
- On mixed problems each kind of advice in the advice range is good at exactly one world, so E_2 is the complement of E_1.
- Choose any monotone path from P_1 = X_{α′,∞} to P_2 = X_{0,β′}. Map L ∪ R measure-preservingly onto I = [0,1]
  (normalised μ) by the order in which points enter E_1 along the path. Then the path is u_p with E_1(u_p) = [0, a(p)),
  where a(p) = 1 − p.
- The nonnegative problems of U are placed as an extra cheap block to the left of 0 (see the remark below).

*World 2.* Additive: X ↦ μ(E_2 X).

*World 1.*
- Cells J_1, …, J_10 partition I from left to right, with m_k ∝ 5^{−k}, so m_k > 3R_k where R_k = Σ_{l>k} m_l. Assign
  the cells bijectively to the 2-subsets S_k, and let C_i, g_i be as before.
- Put T_x(δ) = ∫_x^1 δ and T^θ_x = θT_0 + (1−θ)T_x.
- 𝒜_band = {δ : T^θ_x(δ) ≥ 0 for all x}. This is the unanimity over increasing densities with values in [θ, 1].
- 𝒢_i = {δ : T^θ_x(δ) ≥ T^θ_x(g_i) for all x}.
- World 1's acceptance set is 𝒜 = 𝒜_band ∪ ⋃_i 𝒢_i, with 0 < θ < min_k (1−θ)(m_k − 3R_k)/3. Here θ = 10⁻⁷ works:
  min_k(m_k − 3R_k) = 4.1·10⁻⁷.

*Claims and proofs.*
1. **𝒜 is a ranking.**
   - 𝒜_band is sum-closed, since its conditions are linear.
   - 𝒜_band + 𝒢_i ⊆ 𝒢_i.
   - For s ∈ 𝒢_i and s′ ∈ 𝒢_j: take x = x_k, the left end of the cell of {i,j} (any C_i-cell if i = j). Then
     T^θ_x(s + s′) ≥ 2[−θ + (1−θ)(m_k − R_k)]. This exceeds θ + (1−θ)(m_k + R_k) = max_𝒞 T^θ_x. So s + s′ ∉ 𝒞.
   - Sign conditions: 𝒜_band excludes nonpositive non-zero vectors through T_0. 𝒢_i excludes them because
     T^θ_{x_k}(g_i) > 0 for k ∈ C_i.
   - g_i ∈ 𝒢_i and Σ g_i = −1, so (NC) fails.
   - Fineness: λ(Q∖A) ≤ θλ(A∖Q) implies Q ≤ A.
2. **(i′) Competitiveness of u_p on {1,2}.**
   - If u_p ⋠_2 A, then λ(A) > a.
   - Then 1_A − 1_{[0,a)} has T_x ≥ 0 for all x. Indeed λ(A ∩ [x,1]) ≥ λ(A) − x ≥ a − x for x < a. So it lies in
     𝒜_band.
3. **(ii′) Undominatedness, and (C).** Suppose B ≤_1 [0,a) with λ(B) ≥ a, B ≠ [0,a). Write δ = 1_D − 1_E with
   D = [0,a) ∖ B and E = B ∖ [0,a), so λ(E) ≥ λ(D).
   - Case δ ∈ 𝒜_band: T_0 ≥ 0 forces λ(E) = λ(D). Then T_a(δ) = −λ(E) ≥ 0 forces E = D = ∅.
   - Case δ ∈ 𝒢_i: let x\* be the left end of the last C_i-cell. Then T^θ_{x\*}(δ) ≥ T^θ_{x\*}(g_i) > 0.
     - If a ≤ x\*, then D ∩ [x\*,1] = ∅, so T^θ_{x\*}(δ) ≤ 0.
     - If a > x\*, then E ⊆ [x\*,1] and T^θ_{x\*}(δ) ≤ (1−θ)(λ(D) − λ(E)) ≤ 0.
     Either way, a contradiction.
   - So u_p is undominated, ties with u_p are trivial, and (C) holds.
   - Every undominated model is tied with a selected model (Fact 0(b)), so it is selected.
4. **(iii) Closed sections.**
   - {a : [0,a) ≤_1 A} is a finite union of sets {a : T^θ_x(1_A − 1_{[0,a)}) ≥ c(x) for all x}. Each is closed, since
     the left side is continuous in a.
   - World 2's sections {p : λ(A) ≤ 1 − p} are closed.
   - Vertices: E_1 = ∅ is world-1-best, and E_1 = I is world-2-best.
5. **(b): world 1 satisfies (NC) on 𝔚_1.** Take ν with density e^{Mx}, M ≥ max_i 1/e\*_i, where
   e\*_i = (c\*_i − θ)/(1−θ) and c\*_i = T^θ_{x\*}(g_i). Every δ ∈ 𝔚_1 is 1_E − 1_D with D ⊆ [0,a) and E ⊆ [a,1].
   - Case δ ∈ 𝒜_band: T_0 ≥ 0 gives ν(δ) ≥ e^{Ma}(λ(E) − λ(D)) ≥ 0.
   - Case δ ∈ 𝒢_i, a ≤ x\*: the condition at x\* gives λ(E ∩ [x\*,1]) ≥ e\*. Then
     ν(δ) ≥ e^{Mx\*} e\* − e^{Mx\*}/M ≥ 0.
   - Case δ ∈ 𝒢_i, a > x\*: the condition at x\* gives λ(E) ≥ λ(D ∩ [x\*,a)) + e\*. Then
     ν(δ) ≥ e^{Ma} e\* − e^{Mx\*}/M ≥ 0.
6. **(c)** This is Lemma 3.1. ∎

*Remark (nonnegative problems).*
- Unaccepted nonnegative gambles in U are errors at both worlds. Place them as a block [−p_0, 0) to the left of I in
  world 1's coordinate (cheap errors), with g_i = −1 there. Count them in E_2 at world 2.
- The proofs of 1–5 go through with T_0 replaced by T_{−p_0}. Only θ-terms change, since x\*, x_k ∈ I.
- Competitiveness and undominatedness only ever involve E_1 ∩ I. If u_p ⋠_2 X, then λ(E_1 X ∩ I) > a. And B ⪯_2 u_p
  forces λ(E_1 B ∩ I) ≥ a.

NUMERICS (`n2_world.py`, 6/12/3 bins per cell):
- the inequalities hold;
- the largest value of λ(B) − a among exotic comparisons B ≤_1 [0,a) is −0.0049 < 0;
- the cutting-plane LP for (NC_{𝔚_1}) closes in round 0 with density e^{30x}.

*Reading.* The exotic comparisons of world 1 say that errors covering a heavy cell family C_i are worse than anything
else. They never compare a selected model unfavourably with something it should beat, and an exponential density sees
through them. This is the "decorative" phenomenon: the violation lives in 𝒜_1 ∖ 𝔚_1. It also shows why n = 2 cannot
host a useful violation: nested error sets (Lemma 3.1).

## 7. Assessment (N17.9)

**What a T1 cover by non-additive rankings must look like** (combining N17.2–N17.5 with N9/N10). All of this holds
under (H) and is conditional on N14 §6 where the additive class is invoked.
1. At some world i the comparisons out of C_L do not add up, (NC_{𝔚_i ∪ 𝔉_i}) failing, unless (ii) or (iii) of §0
   holds.
2. The certificate has at least 5 exchanges out of selected models. At least two have overlapping improvement regions,
   and the selected models involved have crossing, cyclically arranged world-i error sets.
3. If exactly one world is non-additive in this sense, the other two satisfy N17.4. There is then a coherent edge model
   with K's ratio range, and T sits at the exchange rate c\*. Proving that this is contradictory is CONJECTURE N17.A,
   the T1 analogue of TAW. It would give the analogue of IRC Cor twoNC: at least two non-additive worlds.
4. Against every additive shadow making T Bayes, the cover must contain reversals C ⪯_j B_t against incoherent Bayes
   models B_t. These are expected near T, at the corner rays and crossings of ∂D_T (CONJECTURE 5.2; NUMERICS at the
   corner rays for the facet-switching shadow). Any dominating C indexed near the target fibre is competitive only on Ω (N9 Cor 3.3).

**Evidence for the route.**
- No theorem excludes it.
- The axioms permit fine (NC)-violators (N17.7), even inside a system satisfying (S) and (C) (N17.8).
- T1's additive contradiction is a cyclic exchange-rate (holonomy) condition around the three corners. Non-additive
  rankings are exactly the ones that need not carry a potential.
- N17.1(b) forbids only the *simple* money pump. Cancellations with overlapping supports, the only kind N17.1(d)
  allows, are not excluded by any axiom.

**Evidence against the route.**
- In the only full system built, the violation is decorative and confined outside 𝔚 (N17.8(b)).
- Every known violation (K4, half5, N17.7) consists of *rigid* acceptances. Each needs an exchange that covers a whole
  heavy cell family exactly, and only one of them can be used in any chain.
- A T1 cover needs load-bearing reversals for a *continuum* of incoherent near-T models B_t (all t near π), out of
  selected models whose indices move continuously, with closed sections.
- I could not make rigid acceptances do this. Making them flexible (G_θ- or band-like) restores additivity, because
  band rankings are (CP-a) and reduce (N11/N13).
- This is a heuristic tension, not a theorem.

**Honest bottom line.** The route is open. It is now sharply posed:

> Is there a ranking with (G), (IB) on M_U, with closed competitive choice, in which (NC⁺) fails on 𝔚_i, the
> comparisons out of selected models? Equivalently, by N17.1(c), is there a world with no strictly positive weak
> charge on 𝔚_i?

- CONJECTURE N17.B (that (S) forces (NC⁺_{𝔚_i})) would close the route, modulo the charge issues (ii) and (iii) and the
  additive core.
- Its n = 2 nested case is PROVED (Lemma 3.1).
- Its n = 3 content is the cyclic case.

Suggested next test: an n = 3 system for an *easy* target (a precise target or a box), with one world replaced by a
band ranking plus exotic acceptances placed on 𝔚. This would show whether a load-bearing (NC)-violation on 𝔚 is
compatible with (S) at all. It is a cleaner question than T1 itself, and a negative answer would prove N17.B.

## 8. Files (`n17py/`, run with `python3 -I`)
- `fine_world.py` (+ `.out`): Prop 6.2 checks (potential monotonicity, threshold, explicit failure at θ = 0.7,
  adversarial chains at θ = 0.039).
- `n2_world.py [bins]` (+ `.out`): Prop 6.3 inequalities, the (ii′) LP, the (NC_{𝔚_1}) cutting-plane LP.
- `t1_fields.py` (+ `.out`): N17.4(b) for Brier and facet-switching fields; location of the incoherence of
  facet-switching Bayes models (corner rays).
