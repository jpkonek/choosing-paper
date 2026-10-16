# K2. Finite cancellation certificates (mode M1) in full systems: the divisibility theorem, the two-world reduction, the frontier family, and why decorating an additive base fails

15 Oct 2026, round 19 (BRIEF16; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up
marks proved), **CHECKED**, **CONJECTURE**, **NUMERICS** (scripts in `k2py/`, run with `python3 -I`; no proof
depends on them). No assumption is added. Setting and notation: write-up §§2–3 (axioms, M_U, regular models,
Def. addup, modes M0/M1/M2), N17 §0–§3 (acceptance sets 𝒜_i, the class 𝒞 of {−1,0,1}-valued functions on U,
N17.1(a) normal form, N17.1(b) chaining lemma, N17.3 Lemma 3.1), B1 §0 (sign classes Q_l, edge regions
R_ij = Q_i ∪ Q_j, leading densities, Lemma B1.0), P3 §2–3 (forced comparisons, rule R5).

Throughout, "full system" means a ranking on M_U with strict (G), (IB), (LA), (S) (a selection p ↦ C_p,
competitive on supp p, closed sections for every model) and (C). An **(M1) certificate at world i** is a finite
family of relevant comparisons B_k ⪯_i X_k (B_k ∈ C_L, X_k regular) with vectors
δ_k := 1_{E_iX_k} − 1_{E_iB_k} and weights λ_k > 0 such that Σ λ_k δ_k ≤ 0 a.e. and ≠ 0.

---

## 0. Outcome

**Neither target was reached.** No full system with an (M1) world was constructed (task (1)), so task (2) (aiming
it at T1) was not started, and no general impossibility theorem was proved (task (3)). What was proved closes two
classes outright, reduces the n = 2 route to a known open conjecture, and kills the natural construction route by a
theorem.

1. **K2.1 Divisibility Theorem (PROVED; any n, any target).** No certificate consists of *divisible* accepted
   vectors (vectors all of whose proportional sub-moves are accepted). **K2.2 (PROVED):** every comparison that
   competitiveness *forces* at world i next to worlds with leading densities (for instance additive worlds with
   integrable densities) is divisible, also after transport to tied members of C_L.
   - **Class closed:** certificates made of forced comparisons. Every (M1) certificate must contain a rigid,
     unforced relevant comparison. These are decorations of the kind D2 uses, but placed where error sets cross.
2. **K2.3 Two worlds (PROVED).** In n = 2 an (M1) certificate at either world forces C_L to cross. Then, by the
   refereed Theorems S22 and MC, neither world has a nonzero leading charge or (MC_sel), and C_L is a counterexample
   to the open **Conjecture Q2N**.
   - **Class closed:** n = 2 whenever one world is additive with a density, (CP-a) with countably additive members,
     lexicographic with a charge first level, or monotonely continuous.
   - **The brief's "n = 2 with a non-nested selection" route** requires first refuting Q2N. That conjecture has
     resisted rounds 13–18.
3. **K2.4 Three worlds next to two additive worlds (PROVED): the frontier family.** If worlds j, k are additive
   with integrable densities (the H1 setting of every surviving T1 configuration with integrable neighbours), then:
   - C_L contains the (j,k)-Bayes models F_s;
   - their world-i error sets cross whenever the density ratio ρ_k/ρ_j interleaves on Q_j and Q_k;
   - no comparison out of them is forced through an index whose support contains {j, k}.

   So N17.3's crossing requirement is met for free, and the (M1) question in this class is purely one of
   *consistency* of world i's acceptance set.
   - Restriction (PROVED): a certificate based only on frontier models always contains two comparisons with
     disjoint gains. The overlap device of N17.7 cannot protect every pair there.
4. **K2.5 A sufficient construction scheme (PROVED).** Take an additive base whose Bayes models are coherent at
   every weight. Replace world 1 by
   𝒦 ∪ ⋃_k (g_k + 𝒦), with 𝒦 the dual of a cone Ψ of linear endorsers of the forced comparisons.
   - This gives a full system with **every axiom verified** (closed sections included, with no R5 bookkeeping) and
     an (M1) world, provided finitely many vectors g_k satisfy four finite conditions: fit, (E), (P), (Cert).
   - So task (1) reduces to a finite-dimensional problem.
5. **K2.6 The single proved obstruction (PROVED).** Over additive Bayes bases satisfying a mild genericity
   condition at the two world-1 edges ((SPREAD) or (ADJ); both hold for the Brier base, PROVED), the forced
   comparisons at those edges kill every linear endorser except ρ_1.
   - Then (E) and (Cert) contradict each other, so the scheme of K2.5 is **empty**.
   - The mechanism is K2.7's sweep: edge selections near a vertex reach every region (PROVED, any n). Their forced
     comparisons trade world-1 errors across a level of the edge order. Any endorser that weights the other worlds'
     disagreements is then caught between two points of the same level with different density ratios.

**The single obstruction, in words.** A finite certificate needs rigid comparisons (K2.1–2.2) whose pairwise gains
are protected against the forced cone of world i. Protection needs endorsers of that cone that concentrate on the
overlaps (K2.5's (P)). At an edge of world i the forced cone is a tail cone in the edge order, and that order
interleaves the two sign classes of the edge region. Interleaving pins the endorser's weights on the other worlds to
zero (K2.6). What is left is ρ_i, which endorses every forced comparison and therefore cannot leave any rigid
comparison unendorsed.

**The precise open question (§9).** Does some full system have an (M1) world whose selection, on the indices
where that world is in the support, is *not* the Bayes family of an additive field with (SPREAD) or (ADJ) at its
edges? Equivalently, within the H1 class: can the third world reshape the selection itself, rather than decorate
an additive one? K2.6′ (CONJECTURE) would say that the Bayes case is closed for every world order, not only for the
scheme.

Scripts:
- `k2py/divisibility.py` (CHECKED: the piece assignment of K2.1 on 3000 random certificates, exact);
- `k2py/frontier_and_edges.py` (NUMERICS: the frontier error-set formula and crossing, and K2.6's edge violations
  for c₂ > 0, on the Brier base for T1 with ε = 0.3, s = 0.9).

---

## 1. Preliminaries used

- **N17.1(a) (PROVED there).** A set 𝒜 ⊆ 𝒞 is the acceptance set of a world with strict (G) and (IB) iff:
  - it contains every δ ≥ 0;
  - it contains no δ ≤ 0 with δ ≠ 0;
  - it is closed under every pairwise sum that stays in 𝒞.
- **N17.1(b) chaining lemma (PROVED there).** If δ_1, …, δ_m ∈ 𝒜 have pairwise disjoint positive parts and
  pairwise disjoint negative parts, then Σ δ_k ∈ 𝒜.
- **N17.3 Lemma 3.1 (PROVED there; refereed in N19 §4).** If the world-i error sets of members of C_L form a chain,
  there is no certificate at world i.
- **Lemma B1.0 (PROVED there).** Let ρ be a leading density of world j on M, meaning that ρ(E_jZ ∖ E_jY) >
  ρ(E_jY ∖ E_jZ) implies Y ⪯_j Z for regular Y, Z. Then Y ⪯_j Z implies ρ(E_jY) ≤ ρ(E_jZ).

  Hence, for regular X, Y: ρ(E_jX) < ρ(E_jY) implies X ≺_j Y (strictly). Additive worlds with integrable densities
  ρ_j > 0 have this property.
- **Error changes.** For a toggle of world-i error status on a set, world j's error status flips the same way on
  A_ij := {σ_i = σ_j} ∩ U (the agreement set, which contains N₊) and the opposite way on R_ij.

  So if X, Y are models with δ := 1_{E_iX} − 1_{E_iY}, then

  ρ_j(E_jX) − ρ_j(E_jY) = ∫ δ η_j dμ,  η_j := ρ_j on A_ij, −ρ_j on R_ij.  (1.1)

  Write ρ̃_j := −η_j.

---

## 2. The Divisibility Theorem (K2.1) and forced comparisons (K2.2)

**Definition.** A vector δ ∈ 𝒜_i is **divisible** if there is a finite family ℳ_δ of finite measures on U,
absolutely continuous with respect to μ and containing μ|_U, with the following property.
- Let δ′ ∈ 𝒞 satisfy δ′⁺ ⊆ δ⁺ and δ′⁻ ⊆ δ⁻.
- Suppose there is some f ∈ (0,1] with m(δ′⁺) = f·m(δ⁺) and m(δ′⁻) = f·m(δ⁻) for every m ∈ ℳ_δ.
- Then δ′ ∈ 𝒜_i.

**Theorem K2.1 (PROVED).** Let world i have strict (G) and (IB). Let δ_1, …, δ_r ∈ 𝒜_i be divisible and
λ_1, …, λ_r ≥ 0 with Σ λ_k δ_k ≤ 0 a.e. Then Σ λ_k δ_k = 0 a.e. In particular no (M1) certificate consists of
divisible comparisons.

*Proof.* Suppose Σ λ_k δ_k < 0 on a non-null set.

1. **Integer weights.**
   - Let c_1, …, c_N be the non-null atoms of the finite algebra generated by the sets δ_k^±, and D_{ck} := δ_k(c).
   - The cone Λ := {λ ∈ ℝ^r_{≥0} : Dλ ≤ 0} is polyhedral with integer data. By Minkowski–Weyl it is generated by
     finitely many integer vectors w_s.
   - Write λ = Σ μ_s w_s with μ_s ≥ 0. If (Dλ)_{c₀} < 0, some w_s with μ_s > 0 has (Dw_s)_{c₀} < 0.
   - So there is n ∈ ℤ^r_{≥0} with Dn ≤ 0 and (Dn)_{c₀} < 0. Discard the k with n_k = 0.
2. **Equipartition.**
   - Put N₀ := max_c Σ_{k: δ_k(c) = −1} n_k. This is ≥ 1, because c₀ carries a negative.
   - Let ℳ := ⋃_k ℳ_{δ_k}, a finite family of atomless finite measures.
   - By Lyapunov's theorem, each cell c can be partitioned into N₀ pieces c^1, …, c^{N₀} with m(c^s) = m(c)/N₀ for
     every m ∈ ℳ. (Equipartitions of an atomless vector measure exist, by induction on the number of pieces.)
3. **Assignment.** In each cell c:
   - give each k with δ_k(c) = −1 its own n_k pieces. This is possible since Σ_{neg} n_k ≤ N₀.
   - give each k with δ_k(c) = +1 its own n_k pieces chosen among those already given to negatives. This is
     possible since Σ_{pos} n_k ≤ Σ_{neg} n_k by Dn ≤ 0.
   - Positive pieces are pairwise distinct. A positive piece of k is a negative piece of some l with δ_l(c) = −1,
     so l ≠ k.
4. **Pieces are accepted.**
   - Let δ′_k be +1 on k's positive pieces and −1 on its negative pieces, over all cells.
   - Then δ′_k^± ⊆ δ_k^±, and m(δ′_k^±) = (n_k/N₀)·m(δ_k^±) for every m ∈ ℳ_{δ_k}.
   - Here n_k ≤ N₀, since in any cell where k is nonzero, n_k is at most the number of negative pieces there.
   - By divisibility δ′_k ∈ 𝒜_i.
5. **Contradiction.**
   - The δ′_k have pairwise disjoint positive parts and pairwise disjoint negative parts. By the chaining lemma,
     Σ_k δ′_k ∈ 𝒜_i.
   - On each piece the sum is 0 (a positive piece lies inside a negative piece) or −1 (an uncovered negative
     piece). In cell c₀, Σ_{pos} n_k < Σ_{neg} n_k, so some negative piece is uncovered.
   - So Σ_k δ′_k ≤ 0 with Σ_k δ′_k ≠ 0, which contradicts strict (G) (N17.1(a)). ∎

CHECKED (`k2py/divisibility.py`): the assignment of steps 3–5 on 3000 random certificates (2–7 cells, 2–6
comparisons, weights 1–4), exact. Every piece is a gain of at most one comparison and a loss of at most one, and the
sum is ≤ 0 and ≠ 0. 0 failures.

**Definition (forced comparison).** Let B ⪯_i X be a relevant comparison (B ∈ C_L, X regular). It is **forced** if
there is a selected C_p with all of the following:
- B ∼_l C_p at every world l;
- p_i > 0;
- every j ∈ J := supp p ∖ {i} has a leading density ρ_j on M (B1 Def.), with ρ_j(E_jX) < ρ_j(E_jB).

**Proposition K2.2 (PROVED).** A forced comparison holds, B ⪯_i X, and its vector δ = 1_{E_iX} − 1_{E_iB} is
divisible.

*Proof.*
- **It holds.** For j ∈ J, B ∼_j C_p and Lemma B1.0 (applied both ways) give ρ_j(E_jB) = ρ_j(E_jC_p). So
  ρ_j(E_jX) < ρ_j(E_jC_p), hence X ≺_j C_p and C_p ⋠_j X. Competitiveness of C_p on supp p leaves C_p ⪯_i X, and
  B ∼_i C_p gives B ⪯_i X.
- **Divisible.** Take ℳ_δ := {μ|_U} ∪ {ρ_jμ|_{A_ij}, ρ_jμ|_{R_ij} : j ∈ J}.
  - Since B and X are regular, δ = 0 on N₊. Let δ′ be as in the definition, with fraction f.
  - Let X′ be the model with E_iX′ = E_iB △ supp δ′. It is regular, and 1_{E_iX′} − 1_{E_iB} = δ′.
  - By (1.1), ρ_j(E_jX′) − ρ_j(E_jB) = ρ_jμ|_A(δ′⁺) − ρ_jμ|_A(δ′⁻) − ρ_jμ|_R(δ′⁺) + ρ_jμ|_R(δ′⁻)
    = f·(ρ_j(E_jX) − ρ_j(E_jB)) < 0.
  - So B ⪯_i X′ is forced through the same C_p, hence holds, and δ′ ∈ 𝒜_i. ∎

**Corollary K2.2′ (PROVED).** In a full system, every (M1) certificate at world i contains a comparison that is
not divisible, and in particular not forced. If every world other than i has a leading density, every certificate
contains a comparison B ⪯_i X such that, for every selected C_p tied with B with p_i > 0, X is not strictly better
than B at some j ∈ supp p ∖ {i}.

*Remarks.*
- (CHECKED) D2's generators g_* = 1_{Q_g} − 1_{P_g} are not divisible. A proportional part has negative tails
  below a, so it is not in 𝒦₀. One can choose its target part to miss a little of every tail of every Q_{g′}
  (the Q's meet pairwise near 1), so it also fails every near-one clause.
- (CHECKED) N17.7's g_i = 2·1_{C_i} − 1 are not divisible. For f < 1 a proportional part fails G_θ, since
  0.6f > θ·0.4f, and fails 𝒢_i, since W_i ≥ 0.4(1 − f) > 1.2κ for f ≤ 1/2.
- Rigidity is therefore necessary, not an artefact of those designs.
- K2.1 uses neither (S) nor (C). K2.2 uses competitiveness and the leading property only.
- The certificate's rational weights are essential to the proof: one rigid comparison with large weight next to
  divisible ones is not excluded. Proportional pieces cannot reuse a support twice.

---

## 3. Two worlds (K2.3)

**Theorem K2.3 (PROVED).** Let n = 2 and let the ranking satisfy every axiom on M_U. If either world has an (M1)
certificate, then:
- (a) {E_1C : C ∈ C_L} is not a chain, so Conjecture Q2N fails for this ranking;
- (b) neither world has a leading charge nonzero on M, and neither half of (MC_sel) holds (write-up Cor. MC(b));
  in particular neither world is additive with a density, (CP-a) with countably additive members, lexicographic
  with a charge first level, or monotonely continuous on M;
- (c) the certificate contains two bases B_k, B_l whose error sets cross. Every non-corner splice pair between them
  is strictly ordered the same way at both worlds (write-up Lemma rigid). C_L is a linear continuum in the order of
  world 1 (Cor. continuum), with a jump without a tie at every crossing (necessary shape, status of Thm MC).

*Proof.*
- On regular coherent models, E_2 = M ∖ E_1. So if the world-1 error sets of C_L form a chain, so do the world-2
  error sets, and N17.3 Lemma 3.1 excludes certificates at both worlds.
- Hence (a). Lemma 3.1 also yields (c): applied to the bases of the certificate alone, it needs two of them to
  cross.
- (b) is Theorem S22 (leading charge ⇒ chain) together with Theorem MC (one half of (MC_sel) ⇒ chain), as
  summarised in Cor. MC(b). ∎

*Reading.* The brief's "n = 2 with a non-nested selection" is not merely hard. Every (M1) example in two worlds is
a counterexample to Q2N, and moreover one in which both worlds lack leading charges and monotone continuity. Since
Q2N is open after five rounds, this route is at least as hard as Q2N. (C) is what forces nestedness (Prop. R71
satisfies all axioms but (C), with a crossing selection). A two-world (M1) example *without* (C) is not excluded by
anything here, but it would not be a full system.

---

## 4. Three worlds next to two additive worlds: the frontier family (K2.4)

Let n = 3, a full system, i the third world, and j, k additive with integral penalties: ψ_l(X) =
∫_{E_lX} ρ_l dμ, ρ_l > 0 a.e. integrable (l = j, k).
- For s ∈ (0,1) let F_s := {g ∈ U : sρ_jσ_j + (1−s)ρ_kσ_k > 0}, the (j,k)-Bayes set at weight (s, 1−s).
- Let 𝒯 be the set of s whose tie set {sρ_j = (1−s)ρ_k} ∩ R_jk is non-null. It is countable.
- Put r := ρ_k/ρ_j and κ(s) := s/(1−s).

**Theorem K2.4 (PROVED).** For s ∉ 𝒯:
- **(a)** F_s is a.e. equal to a selected model, and F_s ∈ C_L.
- **(b)** No regular X ≠ F_s has ψ_j(X) ≤ ψ_j(F_s) and ψ_k(X) ≤ ψ_k(F_s). Hence:
  - F_s is undominated, whatever world i's order is;
  - no comparison F_s ⪯_i X is forced through a selected index p with {j, k} ⊆ supp p.
- **(c)** E_i(F_s) = Q_i ∪ (Q_j ∩ {r < κ(s)}) ∪ (Q_k ∩ {r > κ(s)}) a.e.
- **(d)** For s < s′ outside 𝒯, F_s and F_{s′} cross iff both μ(Q_j ∩ {κ(s) ≤ r < κ(s′)}) > 0 and
  μ(Q_k ∩ {κ(s) < r ≤ κ(s′)}) > 0.
- **(e)** Let a certificate at world i have only frontier bases F_{s_1}, …, F_{s_m}, s_l ∉ 𝒯. Then every comparison
  whose base has the least s has its gain in Q_j, and every comparison whose base has the largest s has its gain in
  Q_k. These gains are disjoint.

*Proof.*
- **(a)** This is N17.4(a) with the roles of the worlds relabelled.
  - For s ∉ 𝒯, F_s is the a.e.-unique minimiser of sψ_j + (1−s)ψ_k.
  - Fact 0 gives a selected undominated C with C ⪯_l F_s at every l.
  - Additivity at j and k makes C a minimiser, so C = F_s a.e.
- **(b)** Such an X would also be a minimiser, hence equal to F_s.
  - A dominator of F_s would have to be weakly better at j and k.
  - A forcing index p ⊇ {j, k} would need X strictly better at both j and k.
- **(c)** Check each class.
  - On Q_i, worlds j and k agree with each other against i, and F_s takes their side.
  - On Q_j (worlds i, k against j), F_s takes world j's side iff sρ_j > (1−s)ρ_k, i.e. r < κ. That is exactly where
    it errs at world i.
  - On Q_k it errs at world i iff (1−s)ρ_k > sρ_j, i.e. r > κ.
  - On N₊ it is correct.
- **(d)** E_i(F_s) ∖ E_i(F_{s′}) = Q_k ∩ {κ < r ≤ κ′}, and E_i(F_{s′}) ∖ E_i(F_s) = Q_j ∩ {κ ≤ r < κ′}.
- **(e)** By N17.3 Lemma 3.1, the gain of a comparison based at F_s lies outside E_i(F_s) and inside some
  E_i(F_{s_l}).
  - Outside E_i(F_s) on M means Q_j ∩ {r ≥ κ(s)} or Q_k ∩ {r ≤ κ(s)}.
  - For s minimal, every other base has κ_l ≥ κ(s), so its error set meets Q_k ∩ {r ≤ κ(s)} only in a null set.
    The gain therefore lies in Q_j. The maximal case is symmetric. ∎

NUMERICS (`k2py/frontier_and_edges.py` (A)): Brier base ρ_l = |g_l| on U for T1 (ε = 0.3, s = 0.9), 60 000 samples.
Formula (c) has 0 mismatches over 3 weights. F_{0.4} and F_{0.6} cross, with 2148 and 2220 sampled points in the two
differences.

*Reading.*
- **The setting is exactly the H1 class.** H1.2 requires two integrable worlds and some a.e.-finite endorser at
  the third world; an (M1) world has no positive endorser at all, so it sits in H1's surviving case (A).
- **What K2.4 adds.**
  - C_L automatically contains a crossing family. Its comparisons at world i are constrained by neither
    competitiveness nor undominatedness, only by consistency of 𝒜_i with everything world i must accept, by
    closed sections and by (C).
  - So N17.3's "crossing error sets of selected models" is free in this class.
  - (e) shows that the N17.7 overlap device cannot be used on the frontier alone: the extreme pair is always
    executable as a pair.

---

## 5. A sufficient construction scheme (K2.5)

**Base.** Let c = (ρ_1σ_1, ρ_2σ_2, ρ_3σ_3) be a strictly signed integrable field on U = D_{K′} whose Bayes sets
B_q := {g ∈ U : q·c(g) > 0} are coherent with null ties for **every** q ∈ Δ. The Brier field c(g) = g is an
example: B_q = D_{co(K′ ∪ {q})}. Worlds 2 and 3 are additive (ψ_2, ψ_3), and the selection is C_q := B_q.

**Endorsers.**
- For c = (c_0, c_1, c_2) ∈ ℝ³_{≥0} put φ_c := c_0ρ_1 + c_1ρ̃_2 + c_2ρ̃_3, with ρ̃_j as in (1.1) relative to
  world 1.
- A **forced vector** is t = 1_{E_1X} − 1_{E_1B_q} with q_1 > 0, X any model (regular or not), and
  ψ_j(X) < ψ_j(B_q) for every j ∈ supp q ∖ {1}.
- Let Ψ = {φ_c : c ∈ C}, where C ⊆ ℝ³_{≥0} is a set with:
  - (1, 0, 0) ∈ C;
  - c_0 > 0 for every c ∈ C;
  - φ_c ≥ 0 on U;
  - ∫ t φ_c ≥ 0 for every forced vector t.

**Theorem K2.5 (PROVED).** Let g_1, …, g_m ∈ 𝒞 satisfy:
- **(fit)** g_k = 1_{E_1X_k} − 1_{E_1B_{q_k}} for some q_k ∈ Δ and regular X_k;
- **(E)** for every k some φ ∈ Ψ has ∫ g_k φ > 0;
- **(P)** for every k, l (k = l allowed) some φ ∈ Ψ has ∫ (g_k + g_l) φ > ∫_U φ;
- **(Cert)** some λ ≥ 0 has Σ λ_k g_k ≤ 0 and ≠ 0.

Put 𝒦 := {f ∈ L^∞(U) : ∫ f φ ≥ 0 for all φ ∈ Ψ}, 𝒜_1 := 𝒞 ∩ (𝒦 ∪ ⋃_k (g_k + 𝒦)), and
X ⪯_1 Y :⟺ 1_{E_1Y} − 1_{E_1X} ∈ 𝒜_1.

Then (⪯_1, ψ_2, ψ_3) with the selection q ↦ B_q satisfies:
- strict (G), (IB), (LA);
- (S), with closed sections for every model;
- (C), with C_L = {B_q : q ∈ Δ}.

World 1 has an (M1) certificate.

*Proof.*
1. **Normal form (N17.1(a)).**
   - Every δ ≥ 0 lies in 𝒦, since Ψ ≥ 0.
   - A nonzero δ ≤ 0 is not in 𝒦, since ρ_1 ∈ Ψ is > 0 a.e.
   - Nor is it in g_k + 𝒦: for the (E)-witness φ of k, ∫ δ φ ≤ 0 < ∫ g_k φ, while membership would give
     ∫ δ φ ≥ ∫ g_k φ.
   - Sums: 𝒦 + 𝒦 ⊆ 𝒦 and 𝒦 + (g + 𝒦) ⊆ g + 𝒦.
   - If s ∈ g_k + 𝒦 and s′ ∈ g_l + 𝒦, then for the (P)-witness φ,
     ∫(s + s′)φ ≥ ∫(g_k + g_l)φ > ∫_U φ ≥ ∫ τ φ for every τ ∈ 𝒞. So s + s′ ∉ 𝒞.
   - Hence ⪯_1 is a preorder with strict (G) and (IB). Worlds 2 and 3 are additive.
2. **Competitiveness.**
   - At q with q_1 = 0, B_q is (2,3)-Bayes, and for every X some j ∈ supp q has ψ_j(B_q) ≤ ψ_j(X).
   - At q = e_1, B_q = P_1 and 1_{E_1X} ≥ 0 lies in 𝒦.
   - At q with q_1 > 0, either some j ∈ supp q ∖ {1} has ψ_j(B_q) ≤ ψ_j(X), or the vector is forced, hence lies in
     𝒦 ⊆ 𝒜_1.
3. **Undominatedness, and (C).** Let Y satisfy Y ⪯_1 B_q and ψ_j(Y) ≤ ψ_j(B_q) for j = 2, 3.
   - *Case q_1 = 0.* (2,3)-Bayes uniqueness gives Y = B_q, and at the vertices strict (G) gives the same.
   - *Case q_1 > 0.* Put w := 1_{E_1B_q} − 1_{E_1Y} ∈ 𝒜_1.
     - Bayes optimality gives q_1(ψ_1(B_q) − ψ_1(Y)) ≤ Σ_{j=2,3} q_j(ψ_j(Y) − ψ_j(B_q)) ≤ 0, where ψ_1 is the
       ρ_1-integral.
     - So ∫ w ρ_1 ≤ 0, with equality only if Y is q-Bayes, i.e. Y = B_q (null ties).
     - By (1.1), ∫ w ρ̃_j = ψ_j(Y) − ψ_j(B_q) ≤ 0.
     - So if Y ≠ B_q, every φ_c ∈ Ψ has ∫ w φ_c < 0, because c_0 > 0. Then w ∉ 𝒦.
     - Also w ∉ g_k + 𝒦: that would give ∫ w φ ≥ ∫ g_k φ > 0 at k's (E)-witness.
   - Hence every B_q is undominated, and the only model tied with it at all worlds is B_q itself.
   - By Theorem kkm, every undominated model is tied with a selected one. So C_L = {B_q}, all coherent, and (LA)
     and (C) hold.
4. **Closed sections.**
   - q ↦ B_q is continuous in measure on Δ (null ties at every q; dominated convergence).
   - So for every model X and every φ ∈ Ψ, q ↦ ∫(1_{E_1X} − 1_{E_1B_q})φ is continuous.
   - Hence {q : B_q ⪯_1 X} is a finite union of intersections of closed sets: {q : v_q ∈ 𝒦} and
     {q : v_q − g_k ∈ 𝒦}, with v_q := 1_{E_1X} − 1_{E_1B_q}. It is closed.
   - Worlds 2 and 3 have closed sections by continuity.
   - Rule R5 is therefore automatic. No reservation bookkeeping (P3) is needed, because the number of
     generators is finite.
5. **(M1).**
   - Since 0 ∈ 𝒦, g_k ∈ 𝒜_1, so B_{q_k} ⪯_1 X_k. This is a relevant comparison, since B_{q_k} ∈ C_L and X_k is
     regular.
   - (Cert) makes the family a certificate. ∎

*Remark (which linear endorsers are admissible at interior indices; PROVED).*
- Let t be forced at an interior q. Bayes optimality gives q_1Δ_1 ≥ q_2|Δ_2| + q_3|Δ_3| > 0, where
  Δ_1 = ∫ t ρ_1 and Δ_j = ∫ t η_j.
- Hence ∫ t φ_c = c_0Δ_1 + c_1|Δ_2| + c_2|Δ_3| > 0 for every c ≥ 0.
- So interior indices constrain only φ_c ≥ 0. The constraints on C come from the two world-1 edges, and they are
  the subject of K2.6.

---

## 6. The obstruction: edges kill the linear endorsers (K2.6)

**Edge conditions.** Put r_2 := ρ_2/ρ_1.
- **(SPREAD₁₂).** There are θ > 0, a ≥ 0 and δ > 0 such that, for every ε ∈ (0, θ), both sets
  - Q_1 ∩ {θ < r_2 < θ + ε, ρ_3/ρ_2 > a + δ}, and
  - Q_1 ∩ {θ − ε < r_2 ≤ θ, ρ_3/ρ_2 < a}

  are non-null.
- **(ADJ₁₂).** There are θ > 0 and a > 0 such that, for every ε ∈ (0, θ), both sets
  - Q_1 ∩ {θ < r_2 < θ + ε, ρ_3/ρ_2 > a}, and
  - Q_2 ∩ {θ − ε < r_2 ≤ θ, ρ_3/ρ_2 > a}

  are non-null.
- (SPREAD₁₃) and (ADJ₁₃) are the same with 2 and 3 exchanged (r_3 := ρ_3/ρ_1, Q_1 and Q_3).

**Theorem K2.6 (PROVED).** In the setting of K2.5, suppose (SPREAD₁₂) or (ADJ₁₂) holds, and (SPREAD₁₃) or (ADJ₁₃)
holds. Then:
- every c ≥ 0 such that φ_c endorses all forced vectors has c_1 = c_2 = 0;
- so Ψ ⊆ {c_0ρ_1}, and no g_1, …, g_m satisfy both (E) and (Cert).

The scheme of K2.5 is empty over such bases.

*Proof.*
1. **Setting up the edge comparison.**
   - Take the edge index q = (q_1, q_2, 0) with q_1/q_2 = θ.
   - On Q_1 ∪ Q_2 = R_12, B_q takes world 2's side iff q_2ρ_2 > q_1ρ_1. So E_1(B_q) ∩ R_12 = {r_2 > θ}, and B_q is
     correct on Q_3.
   - Let B ⊆ {r_2 > θ} and B′ ⊆ {r_2 ≤ θ} be non-null subsets of R_12. By Lyapunov choose them with
     ρ_2μ(B′) = (1 + η)ρ_2μ(B), η > 0.
   - Let X := B_q △ (B ∪ B′). This moves world-1 errors from B to B′.
   - On R_12 a world-1 error is a world-2 correct point, so ψ_2(X) − ψ_2(B_q) = ρ_2μ(B) − ρ_2μ(B′) < 0.
   - Since supp q = {1, 2}, the vector t = 1_{B′} − 1_B is forced. Endorsement needs ∫_{B′} φ_c ≥ ∫_B φ_c.
2. **On the sign classes.**
   - On Q_1 (both 2 and 3 disagree with 1): φ_c = ρ_2(c_0/r_2 + c_1 + c_2ρ_3/ρ_2).
   - On Q_2 (world 3 agrees with 1): φ_c = ρ_2(c_0/r_2 + c_1 − c_2ρ_3/ρ_2).
3. **Under (SPREAD₁₂).** Take B ⊆ Q_1 in the first set and B′ ⊆ Q_1 in the second, at scale ε. Then
   - ∫_{B′} φ_c ≤ (c_0/(θ−ε) + c_1 + c_2a)(1+η)ρ_2μ(B);
   - ∫_B φ_c ≥ (c_0/(θ+ε) + c_1 + c_2(a+δ))ρ_2μ(B).

   Letting ε, η ↓ 0 gives c_2δ ≤ 0, so c_2 = 0.
4. **Under (ADJ₁₂).** Take B ⊆ Q_1 in the first set and B′ ⊆ Q_2 in the second. The same estimate, with the bound
   −c_2ρ_3/ρ_2 < −c_2a on Q_2, gives 2c_2a ≤ 0, so c_2 = 0.
5. **The other edge.** The edge (1,3) gives c_1 = 0 in the same way.
6. **Conclusion.** With Ψ ⊆ {c_0ρ_1}, (E) gives ∫ g_k ρ_1 > 0 for every k. (Cert) gives Σ λ_k ∫ g_k ρ_1 < 0,
   because ρ_1 > 0 a.e. and Σ λ_k g_k ≤ 0 with Σ λ_k g_k ≠ 0. These contradict each other. ∎

**Proposition K2.6a (PROVED). The Brier base satisfies (SPREAD₁₂) and (SPREAD₁₃) for every K′ ⊆ relint T1 of the
form u + s(T1 − u).**

*Proof.*
- On the open set Q_1 ∩ U ∩ {g_1 > 0}, the map g ↦ (|g_2/g_1|, |g_3/g_2|) is smooth with surjective differential.
- So it maps non-null sets onto sets with non-empty interior and pulls back open sets to non-null sets.
- Pick (θ, a + δ/2) in the interior of the image, with an open rectangle (θ − ε₀, θ + ε₀) × (a − δ₀, a + 2δ) inside
  the image (shrinking δ if needed). Its two sub-rectangles have non-null preimages for every ε < ε₀.
- (SPREAD₁₃) is symmetric. ∎

NUMERICS (`k2py/frontier_and_edges.py` (B), ε = 0.3, s = 0.9, θ = 1, band 0.05; 116 × 136 sampled forced pairs):

| c | worst (φ_c/ρ_2)(h) − (1+η)(φ_c/ρ_2)(h′) | verdict |
|---|---|---|
| (1, 0, 0) | 0 | endorsed |
| (1, 0.3, 0) | 0 | endorsed at this edge; killed by edge (1,3) |
| (1, 0, 0.05) | +0.63 | violation |
| (1, 0, 0.2) | +2.55 | violation |

**CONJECTURE K2.6′ (the scheme-free form).** Let worlds 2 and 3 be additive with integrable densities. Suppose
that, on the indices with q_1 > 0, the selected world-1 error sets are those of the Bayes family of an additive
field with (SPREAD or ADJ) at both world-1 edges. Then world 1 has a leading density, so it adds up (B1.0) whatever
its order. In particular it carries no (M1) certificate.

*Evidence.*
- The forced cone at interior indices is a two-parameter family of "half-planes" in the coordinates
  (ρ̃_2/ρ_1, ρ̃_3/ρ_1). The endorser analysis of K2.5's Remark, run with the Motzkin alternative instead of the
  linear ansatz, makes every endorser affine in those coordinates on the swept region (projective rigidity of a
  two-parameter family of lines). Then K2.6 applies.
- What is missing is (i) a rigorous version of that rigidity for densities, and (ii) a transfer chain (in the
  manner of B1.2) showing that the generated cone, not only its closed convex hull, contains every ρ_1-strict
  improvement.

*Remark (non-generic bases).* (SPREAD) and (ADJ) can both fail only if, along each world-1 edge order, the density
ratio of the other two worlds on the link class Q_1 is essentially a monotone function of the edge coordinate, and
Q_1 is never adjacent above Q_2 (resp. Q_3).
- Total separation of Q_1 from Q_2 along r_2, in either order, makes the edge Bayes model at the separating level
  incoherent (CHECKED: it is the "majority-positive" or the "anti-world-3" model, and both fail convexity on
  explicit pairs in U for every interior K′).
- Partial separations were not analysed. These non-generic bases are the only place where K2.5's scheme (with
  linear endorsers) is not yet known to be empty.

---

## 7. Edge sweep (K2.7): why protection cannot sit at a fixed place

**Lemma K2.7 (PROVED; any n, any target; uses only strict (G) and (S)).** Let e_ie_j be an edge and p_m → e_j along
the open edge. There is no non-null A ⊆ R_ij with A ∩ E_i(C_{p_m}) = ∅ for all m.

*Proof.*
- On R_ij, being correct at world i means erring at world j. So such C_{p_m} err at world j on all of A.
- Take a non-null A′ ⊆ A with A ∖ A′ non-null, and X := P_j △ A′. This model errs at world j exactly on A′.
- Then E_jX ⊊ E_jC_{p_m}, so X ≺_j C_{p_m} by strict (G), and C_{p_m} ⋠_j X.
- Competitiveness on {i, j} gives C_{p_m} ⪯_i X. Closedness gives C_{e_j} ⪯_i X.
- C_{e_j} ⪯_j P_j and strict (G) give C_{e_j} = P_j. So P_j ⪯_i X.
- But E_iX = E_iP_j ∖ A′ ⊊ E_iP_j, so X ≺_i P_j. This is a contradiction. ∎

*Use.*
- Since M = R_ij ∪ R_ik, every non-null Π ⊆ M meets world-i error sets of edge-selected models with p_i > 0.
- Next to a world j with a leading density, those models carry forced comparisons that fix world-i errors on parts
  of Π (whenever C_p ≠ P_j). This is the case "every region is reached by the forced cone".
- D2 escapes only because its protected zone is an *end*, reached only in the limit, which yields mode M2.
- K2.6 is the quantitative form at a fixed level: an endorser cannot weight the other worlds' disagreements and
  still endorse the edge trades across that level.

---

## 8. Task (2), T1: not reached; what K2 implies for T1

The (M1) world was not built, so it could not be aimed at T1, and the M0closed criterion for every admissible
shadow (E1.1 / L3) was not tested. Consequences for a T1 cover on M_U in the H1 class (worlds 2, 3 integrable,
world 1 exceptional; the only class H1.2 leaves for one exceptional world):
- **(PROVED, K2.2′)** If world 1 is (M1), each certificate contains an unforced relevant comparison.
  - L3's holonomy reversals have the form C ⪯_1 X, with C the KKM dominator of a near-Bayes X (H1.0), so C is
    weakly better than X at worlds 2 and 3. These are unforced at C's index. This is consistent with K2.2, so K2
    does not by itself exclude L3's reversals forming a certificate.
- **(PROVED, K2.4)** The crossing bases a certificate needs are available, through the frontier family.
- **(PROVED, K2.6)** If the selection on the indices with q_1 > 0 is the Bayes family of an additive field with
  SPREAD or ADJ at its edges, the decoration scheme gives nothing. For T1 that scheme is excluded anyway, because
  an additive shadow with coherent Bayes models at every weight does not exist (Theorem main and M0closed(a)).
- **What a T1 cover with an (M1) world must therefore do.** Its selection is non-Bayes for every additive field on
  an open set of indices, and its rigid comparisons are protected by endorsers of a forced cone that is not a
  half-plane family.

---

## 9. The precise open question

> **(Q-K2)** Is there a full system on M_U, with two worlds additive with integrable densities, whose third world i
> has an (M1) certificate? By K2.2′ the certificate must contain an unforced comparison. By K2.4 its crossing bases
> may be frontier models, but not only those if every pair of gains is to overlap (K2.4(e)). By K2.6 the selected
> world-i error sets at the indices with p_i > 0 cannot be the Bayes sets of an additive field with (SPREAD) or
> (ADJ) at both world-i edges, at least for decorations of K2.5's type.

- A **negative answer** would close class (i) of BRIEF16 within the H1 class.
- A **positive answer** must come from a world order that reshapes its own selection on the interior. That is the
  same requirement M0closed's argument already places on any T1 cover.

Two sharper sub-questions, each of which would settle part of (Q-K2):
- **(Q-K2a)** CONJECTURE K2.6′ (Bayes-shaped selections force a leading density at world i).
- **(Q-K2b)** Do non-generic additive bases (failing both (SPREAD) and (ADJ) at an edge) with coherent Bayes models
  at every weight exist? If they do, does K2.5's scheme with linear endorsers admit data (fit), (E), (P), (Cert)?

---

## 10. Status table

| Item | Statement | Label |
|---|---|---|
| K2.1 | no certificate of divisible accepted vectors (any n) | PROVED; CHECKED (script) |
| K2.2, K2.2′ | forced comparisons (next to leading densities) are divisible; every (M1) certificate has an unforced, non-divisible comparison | PROVED |
| K2.3 | n = 2: (M1) ⇒ C_L crosses ⇒ ¬Q2N, and no leading charge or (MC_sel) at either world | PROVED (from N17.3, Thms S22, MC) |
| K2.4 | frontier models in C_L, unforced, crossing iff ratio interleaves; extreme pair has disjoint gains | PROVED; NUMERICS |
| K2.5 | dual-cone decoration of an additive Bayes base gives a full system with an (M1) world from finite data (fit), (E), (P), (Cert) | PROVED |
| K2.6 | (SPREAD or ADJ) at both world-1 edges ⇒ only ρ_1 endorses ⇒ the scheme is empty | PROVED; NUMERICS |
| K2.6a | Brier base satisfies (SPREAD) | PROVED |
| K2.6′ | Bayes-shaped selection ⇒ world i has a leading density | CONJECTURE |
| K2.7 | edge sweep: edge-selected world-i error sets meet every non-null subset of R_ij near e_j | PROVED |
| Task (1) | first full system with an (M1) world | not achieved |
| Task (2) | (M1) cover of T1 | not reached |
| Task (3) | general impossibility | not achieved; closed: forced-only certificates (any n), n = 2 with a leading-charge or (MC_sel) world, K2.5 decorations over generic additive Bayes bases |

## 11. Files (`k2py/`)

- `divisibility.py` (+ `.out`): the piece assignment of K2.1 on 3000 random integer certificates (exact).
- `frontier_and_edges.py` (+ `.out`): (A) the formula of K2.4(c) and crossing of F_{0.4}, F_{0.6} on the Brier
  base; (B) the edge-forced violations of K2.6 for c₂ > 0.

## 12. Dependencies

- N17.1(a), (b) and N17.3 Lemma 3.1 (proved; refereed N19);
- Lemma B1.0 (proved);
- Theorem kkm / Fact 0 (proved);
- N17.4(a) (proved);
- Theorems S22 and MC, Cor. MC(b), Lemma rigid, Cor. continuum (proved; refereed);
- Lyapunov's convexity theorem; Minkowski–Weyl.
- **Not used:** M0closed, H1.0–H1.3, any T1-specific algebra (only in §8's remarks), (Nest_e), P3's reservations.
- Not yet refereed.
