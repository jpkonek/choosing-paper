# PP24. The two-model test over a family: T-anchored gates, three chains, and what the test does not discriminate

22 October 2026. One author; not refereed.

**Labels.** PROVED: complete argument here (or in a refereed note that is cited). CHECKED: exact finite computation (rational geometry; cells with radial splitting; sampled rival sets where stated). NUMERICS: random sampling whose outcome is not a proof. CONJECTURE: unproved. Finite cells are diagnostics only.

**Scripts** (`r9/PP24_py/`; run `python3 -B <script>` inside the folder; outputs in the matching `.out` files):

| Script | Content | Label |
|---|---|---|
| `geom.py` | exact geometry: M, the points q_k(δ), the chains Γ_u(t) | library |
| `check_geometry.py` | Lemma 3.1 (single-region footprints, sharpness of δ*), nesting, unions, chain monotonicity | CHECKED |
| `cells.py` | 26 directions × 2 radial atoms; the keys of Def 3.4; vectorised gate | library |
| `check_cells.py` | threshold property; competitiveness and undominatedness of 37 members against 3.5 million rivals; acyclicity; strict (G) | CHECKED (sampled rivals) |
| `check_dominations.py` | Theorems 6.1–6.2, Cor 6.3, Prop 6.5 | CHECKED (sampled rivals) |
| `check_departures.py` | lead's observations 3 and 4; Prop 2.7 | CHECKED |
| `check_competitive_class.py` | which coherent cell models are competitive (Conj 7.3) | NUMERICS |

**Inputs.** BRIEF46; AUDIT_local_defences §§5–7; PP20; AUDIT_completion; PP21 (Lemmas 2.1–2.4, Q); REFEREE_Z_PP19 (Lemma H, Prop S); DESIGN_MEMO §§5, 8; gate2d (Lemma 2, refereed); PP2 Theorem 6 (refereed). Only Brief 46's axioms are used.

---

## 0. Verdict

1. **The two-model test passes, uniformly over a family, in a strong form (Theorem 3.5, PROVED).** There is one record-based system in which:
   - T and every member of a family 𝓕 of non-vertex coherent models are coherent, undominated, and competitive against **every** model, not only against bounded rivals. 𝓕 consists of T and three one-parameter paths Γ_1, Γ_2, Γ_3 that leave T towards the three vertices.
   - Each path starts with single-region coarsenings of T (PP20-type defenders, now with their own defences), continues with a second footprint, and ends with a contraction towards e_u.
   - Strict (G), (IB) with every copy, and (TC) hold. In fact every world is acyclic, so there are no ties at any world; (LA) and direct (C) follow for every model.

   The defence rule and the geometry are chosen together. Each world compares by a **gate**: X ⪯_w Y is accepted iff Y is a pointwise weak worsening at w, or every world-w rank step that Y adds has lower priority than every step it removes. The priority (key) is **T-anchored**: T's own steps rank above all other steps. Within T's steps the order is the exit order along the world's path; at the top of the other steps it is the entry order into that world's single-region coarsening.

2. **The defences transfer by one lemma (Lemma 2.5, PROVED).** A move that improves a u-ward member at world u adds only non-T steps and removes only T-steps at each other world. So it passes the other worlds' gates whatever their internal orders are. This is the lead's observation 5 (each region is a two-world problem) made into a proof. It also forces the geometry: under T-anchored keys every competitive coherent model is u-ward of T for some u (Prop 2.7, PROVED).

3. **Non-additivity is retained and relevant (Prop 4.1, PROVED).** Out of every member, at each world where it is a threshold set, the accepted bounded comparisons are endorsed by no finite, finitely additive charge that is positive on non-null sets. These comparisons are the members' own local defences (audit Cor 4). PP20's non-endorsed family out of T is accepted verbatim. All of PP20's optional T-defences are present: **T ⪯_w X iff X is worse than T somewhere at w.** Nothing had to be reassigned.

4. **KKM material (Theorems 6.1–6.2, Cor 6.3, PROVED).**
   - T strictly dominates, at all three worlds, every model that is worse than T somewhere at each world.
   - The coarsening C_k(δ) strictly dominates every model satisfying an explicit condition. Hence every fill of T's silence, and all of PP20's class 𝓛 (models equal to T on the footprints), are strictly dominated at all three worlds by members. In PP20 the defenders had no defences of their own; here they are members. This carries out audit §5's input/output operation at this scale.

5. **Limits, and the requested three-way classification (§7).**
   - *Axioms plus requested defences:* no contradiction (Theorem 3.5 is a model).
   - *Optional old comparisons:* none had to be dropped (point 3).
   - *Chosen geometry:* the footprint rivals C_k(δ*)[E → A] are dominated by no member (Prop 6.5, PROVED). This is exactly PP20 Prop 5.1's residual zone.
   - *Mechanism:* every world is a fixed-key gate whose key has null level sets on the vertex-class steps. So **PP2 Theorem 6 (screen S11) shows that no selection satisfying (S) exists for this relation, or for any extension that keeps one world so gated.**

   **The two-model test, even uniformly over a family and with dominations, is therefore passed by a mechanism already screened out for (S): as posed, it does not discriminate.** §7.4 states what a discriminating test should add. §7.5 gives a concrete escape route suggested by the proofs: the T/non-T split is all that the transfer lemma uses.

---

## 1. Setting and notation

Brief 46's setting is used throughout. There are three worlds and problems g ∈ R³ modulo sign, with μ Gaussian. The domain is the full four-advice domain, and models are taken modulo null sets. M_k is the set of mixed problems whose minority world is k; U is the set of unanimous problems. On M_k the advice values are A (majority answer), S (silence), B (minority answer) and ⊥ (contradiction). Their ranks are:
- at the two majority worlds of M_k: 0, 1, 2, 3;
- at the minority world k: 2, 1, 0, 3.

On U the ranks are 0 (correct), 1 (S), 2 (wrong), 3 (⊥). Indices of worlds are taken mod 3. T = D_M, with M = c𝟙 + εΔ and 3c + ε = 1, 0 < ε < 1. Its vertices are v_k = c𝟙 + εe_k.

**Steps.** I := {problems} × {1,2,3}, with ν := μ ⊗ counting. U_w(X) := {(g,j) : r_w(g,X) ≥ j} is the set of world-w steps of X. For a pair (X, Y):
- Add_w(X,Y) := U_w(Y) ∖ U_w(X) are the steps Y adds (world-w losses);
- Rem_w(X,Y) := U_w(X) ∖ U_w(Y) are the steps Y removes (gains).

Both are determined by the record rec(X,Y). The rank at a world determines the advice (a.e.). So for X ≠ Y at least one of Add_w and Rem_w is non-null.

- X ≤_w Y ("X no worse at w") means U_w(X) ⊆ U_w(Y).
- W(X) := {w : X is worse than T somewhere at w} = {w : Add_w(T,X) non-null}.
- **T-steps** at w are the steps in U_w(T). T is coherent, so it never has a step on U or at level 3.

**Regular advice and u-ward moves.** Coherent models are *regular*: they take values in {A, S, B} on mixed problems and are correct on U. On M_k the three regular values lie on the line A – S – B. Call Y **u-ward of** a regular Z if Y ≤_u Z. Then Y is regular, Y = Z on U, and Y differs from Z only by moves along the line in the *u-ward direction*: A-ward on M_k for k ≠ u, B-ward on M_u. For worlds u ≠ v, write v′ for the third world.
- The u-ward and v-ward directions agree on M_{v′}: the worlds are *aligned* there.
- They are opposite on M_u and on M_v: the worlds are *opposed* there.

**Lemma 1.1 (rank injectivity; PP20 Lemma 1.1).** If X ≤_w N at all three worlds and N is coherent, then X = N.

---

## 2. The mechanism: T-anchored gates

**Definition 2.1 (gate with trivial verdict).** Let k_w : I → R be measurable with null level sets. Then X ⪯_w Y iff one of the following holds:
- X = Y;
- Rem_w(X,Y) is null (guidance);
- Add_w(X,Y) is non-null and ess sup_{Add_w(X,Y)} k_w ≤ ess inf_{Rem_w(X,Y)} k_w (*separated*).

So a non-guidance comparison is accepted exactly when every step that the rival adds has lower priority than every step it removes. This is gate2d's rule with verdict Φ ≡ 0.

**Lemma 2.2 (acyclicity; gate2d Lemma 2, refereed; PROVED).** No world has a cycle X_0 ⪯_w X_1 ⪯_w … ⪯_w X_m = X_0 with a nontrivial step. Hence:
- reflexivity, strict (G) and (IB) (the definition is record-level, so every copy is covered);
- (TC), since there is no nontrivial accepted triangle;
- no ties between distinct models at any world, hence (LA) for undominated T and direct (C) for every model.

*Proof sketch.* Each nontrivial accepted step adds a non-null set of steps. Take the step whose added set has the lowest essential infimum β*. The window {β* < k_w < γ}, where γ is the least essential infimum of the removed sets, is never removed from, and is strictly enlarged at that step. ∎

**Definition 2.3 (T-anchored).** The key k_w is *T-anchored* if k_w ∈ [0,1] on T-steps and k_w < −1 off them. N is a *threshold set* of k_w if U_w(N) = {k_w ≥ κ} a.e. for some κ. In particular T is a threshold set (κ = 0) of every T-anchored key.

**Lemma 2.4 (threshold lemma; PROVED).** Let N be a threshold set of k_w and Y ≠ N.
- (a) N ⪯_w Y iff Y is worse than N somewhere at w (Add_w(N,Y) non-null).
- (b) Y ⪯_w N iff Y ≤_w N.

*Proof.* Add_w(N,Y) ⊆ {k_w < κ} and Rem_w(N,Y) ⊆ {k_w ≥ κ}.
- (a) If Add is non-null, the pair is separated, so it is accepted. If Add is null, then Rem is non-null and Y is a strict improvement, which is refused.
- (b) Here Add_w(Y,N) ⊆ {k ≥ κ} and Rem_w(Y,N) ⊆ {k < κ}. If both are non-null, separation would force both into the null level set {k = κ}. So acceptance needs Rem_w(Y,N) null, that is, Y ≤_w N. ∎

**Lemma 2.5 (u-ward moves pass the other gates; PROVED).** Let the key at world v be T-anchored, let u ≠ v, let Z be u-ward of T, and let Y be u-ward of Z. Then:
- Add_v(Z,Y) contains only non-T steps;
- Rem_v(Z,Y) contains only T-steps;
- Add_v(Z,Y) is non-null iff Y ≠ Z on a non-null part of M_u ∪ M_v.

Consequently:
- (a) if Y ≠ Z, then Z ⪯_v Y for some v ≠ u;
- (b) if Y ⪯_v Z, then Y ≤_v Z.

*Proof.* Work pointwise on M_k, along the line T → Z → Y, which moves in the u-ward direction.
- If v is aligned with u on M_k (k = v′), the v-rank decreases along the line. So the move Z → Y removes levels at or below r_v(Z) ≤ r_v(T): these are T-steps.
- If v is opposed to u on M_k (k ∈ {u, v}), the v-rank increases. So Z → Y adds levels above r_v(Z) ≥ r_v(T): these are non-T steps.
- Nothing moves on U.

T-anchoring then gives separation whenever Add is non-null. A nontrivial u-ward move is non-null on M_u ∪ M_v or on M_u ∪ M_{v′}, which gives (a).

For (b), Add_v(Y,Z) consists of T-steps (keys ≥ 0) and Rem_v(Y,Z) of non-T steps (keys < −1). So separation is impossible unless one of them is null, and acceptance needs Rem_v(Y,Z) null. ∎

**Theorem 2.6 (defence transfer; PROVED).** Suppose every world's key is T-anchored. Let N be coherent, u-ward of T, and a threshold set of k_u. (T itself qualifies, for every u.) Then:
1. N is competitive against every model;
2. no Y ≠ N has Y ⪯_w N at all three worlds, so N is undominated.

*Proof.*
1. If Y is worse than N somewhere at u, then N ⪯_u Y by Lemma 2.4(a). Otherwise Y ≤_u N, so Y is u-ward of N, and Lemma 2.5(a) gives a world v ≠ u with N ⪯_v Y.
2. Lemma 2.4(b) at u gives Y ≤_u N, so Y is u-ward of N. Lemma 2.5(b) at both other worlds gives Y ≤_v N there too. Lemma 1.1 then gives Y = N. ∎

**Proposition 2.7 (the geometry is forced; PROVED; CHECKED in `check_departures.out`, 231/231 cell models).** Suppose every key is T-anchored. Let C be coherent and *not* u-ward of T for any u. Then some Y differing from C only on a bounded set, of arbitrarily small measure, has C ⋠_w Y at every w.

*Proof.* For each w, the set where C is worse than T at w is a non-null cone. Pick a bounded non-null piece S_w of it, with the three pieces disjoint. Let Y := C[S → T] with S = S_1 ∪ S_2 ∪ S_3. At world w:
- on S_w, Y removes non-T steps (C's extra steps), so Rem_w is non-null;
- wherever Y adds steps, it adds T-steps (re-adding steps of T that C lacks).

So either Add_w is null, and Y is a strict improvement, or Add_w has keys ≥ 0 above Rem_w's keys < −1. In both cases the comparison is refused. ∎

So under T-anchoring, the competitive coherent models lie in the three "cones" of models u-ward of T. The family below fills one chain in each cone.

---

## 3. The family and the keys

**Lemma 3.1 (single-region coarsenings; PROVED; CHECKED exactly, including sharpness).** For k with {i, j} = the other two worlds, put

  q_k(δ) := (v_i + v_j)/2 + δ((e_i + e_j)/2 − e_k),  δ* := cε/(3c + 2ε)

(δ* = 7/130 for ε = 3/10), and C_k(δ) := D_{conv(M ∪ {q_k(δ)})}. Then for 0 < δ ≤ δ*:
- (i) C_k(δ) = T except on a non-null open cone F_k(δ) ⊆ {g ∈ M_k : T(g) = B}, where C_k(δ) is silent. So C_k(δ) only retreats from T's minority answers on M_k. This is A-ward on M_k, so it is both i-ward and j-ward of T.
- (ii) F_k(δ) increases with δ. The entry time e_k(g) := inf{δ : g ∈ F_k(δ)} has null level sets.
- (iii) For a ≠ b, the model D_{conv(M ∪ {q_a(δ), q_b(δ′)})} equals T except for silence on F_a(δ) ∪ F_b(δ′).
- (iv) For δ > δ* the inclusion in (i) fails.

*Proof.*
- (i) Let T accept g, so min_l v_l·g > 0, and let q·g < 0, where q = q_k(δ).
  - *g_k > 0.* If g_k ≤ 0, then v_k·g > 0 gives Σg > 0, hence g_i + g_j > −g_k ≥ 0. Then q·g = (c − δ)g_k + (c + (ε + δ)/2)(g_i + g_j) > −g_k(δ + (ε + δ)/2) ≥ 0, a contradiction.
  - *Both g_i, g_j < 0.* Some coordinate is negative, since q ∈ int Δ. Suppose g_i = −a < 0 ≤ g_j = b, with g_k = K > 0. Then v_i·g > 0 gives a < cK′/(c + ε), with K′ := K + b. And q·g < 0 gives a > b + αK, with α := (c − δ)/(c + (ε + δ)/2). Both hold only if b(1 − β) < K(β − α), where β := c/(c + ε). But β ≤ α exactly when δ ≤ δ*, so this is impossible.
  - Hence g ∈ M_k with only g_k positive, and T's answer (accept g) is the minority answer B.
  - The region is non-null because q ∉ M: its k-coordinate is c − δ < c.
  - Off the separating lines, C_k(δ) agrees with T: it is a coarsening, silence stays silence, and on U it is correct.
- (ii) q_k(δ) lies on [mid, q_k(δ′)] for δ < δ′, so the credal sets are nested. Level sets of e_k lie in planes {q_k(δ)·g = 0}.
- (iii) Over a convex hull, min m·g is attained at an extreme point.
- (iv) For δ > δ*, choose b small and a strictly between the two bounds. `check_geometry.out` gives exact witnesses in M_i at δ = 1.1δ* and 1.5δ*. ∎

**Lemma 3.2 (contraction; PROVED).** For a closed convex K ⊆ Δ, the models D_{(1−θ)K + θe_u} move u-ward monotonically in θ, and equal V_u for θ near 1 at each g with g_u ≠ 0.

*Proof.* Over (1−θ)K + θe_u, the values m·g form the interval [(1−θ)lo + θg_u, (1−θ)hi + θg_u], where [lo, hi] is the interval for K. Each endpoint is linear in θ, so it changes sign at most once, towards the sign of g_u. ∎

**Definition 3.3 (the three paths).** For u ∈ {1,2,3} and t ∈ [0,1), Γ_u(t) := D_{K_u(t)}, where:
- phase 1, t ∈ [0, 1/3]: K_u(t) = conv(M ∪ {q_{u−1}(3tδ*)});
- phase 2, t ∈ [1/3, 2/3]: K_u(t) = conv(M ∪ {q_{u−1}(δ*), q_{u+1}((3t − 1)δ*)});
- phase 3, t ∈ [2/3, 1): K_u(t) = (1 − θ)K_u(2/3) + θe_u, with θ = 3t − 2.

By Lemma 3.1, phases 1–2 retreat only from T's minority answers on M_{u−1} and then on M_{u+1}. These retreats are A-ward, hence u-ward. Phase 3 is u-ward by Lemma 3.2. So **Γ_u is monotone u-ward, every member is u-ward of T, and Γ_u(0) = T.**

The phase-1 members are the coarsenings C_{u−1}(δ) = Γ_u(δ/(3δ*)). In particular C_k(δ) lies on Γ_{k+1}. The family is

  𝓕 := {T} ∪ {Γ_u(t) : u ∈ {1,2,3}, 0 < t < 1}.

Every member is non-vertex and coherent. CHECKED: monotonicity, u-wardness and the absence of contradictions on 4,000 directions × 60 parameter values per path.

**Definition 3.4 (keys).** At world u:
- **T-steps:** k_u(g,j) := sup{t ∈ [0,1) : (g,j) ∈ U_u(Γ_u(t))} ∈ [0,1], the exit time along Γ_u.
- **Top non-T steps:** for (g,1) with g ∈ F_u(δ*) (there T = B is u-correct, so the step is not a T-step), k_u := −1 − e_u(g)/(2δ*) ∈ [−3/2, −1).
- **All other non-T steps:** k_u := −3/2 − φ(g,j)/2, with φ : I → (0,1) any measurable function with null level sets.

**Lemma 3.4′ (PROVED).**
- Each k_u is T-anchored and has null level sets. Exit times are attained on the boundaries of the cones {min_{K} m·g = 0} or {max_K m·g = 0}, which are null.
- U_u(Γ_u(t)) = {k_u ≥ t}, since Γ_u is monotone.
- U_u(C_u(δ)) = U_u(T) ∪ {(g,1) : g ∈ F_u(δ)} = {k_u ≥ −1 − δ/(2δ*)}. Here C_u(δ) retreats from u-correct answers, adding exactly those steps at world u.

So **Γ_u(t) is a threshold set at u, and C_k(δ) is a threshold set at two worlds, k and k + 1.** CHECKED on cells (C1).

**Theorem 3.5 (main; PROVED).** Let the relations ⪯_w be given by Definition 2.1 with the keys of Definition 3.4. Then:
1. Reflexivity, strict (G), (IB) with every common-context copy, and (TC) hold. Every world is acyclic, so there are no ties at any world. (LA) holds, and direct (C) holds for every model.
2. T and every member of 𝓕 are coherent, non-vertex and undominated. Each is competitive against every model, in particular against every measurable rival that differs from it on a bounded region, however small.
3. The proofs are uniform in (u, t). A rival Y of Γ_u(t) is defended:
   - at world u if Y is worse there somewhere;
   - otherwise at a world v ≠ u at which Y differs on M_u ∪ M_v.

   T defends at every world where the rival is worse somewhere.

*Proof.* Item 1 is Lemma 2.2. For item 2, Lemma 3.4′ makes every member a threshold set at its own world. Members are u-ward of T (Definition 3.3), and T is a threshold set everywhere. Apply Theorem 2.6. Item 3 restates that proof. ∎

**CHECKED (cells, `check_cells.out`).** 26 directions × 2 radial atoms, with coherent members constant on directions. 37 members (T and 12 parameters per path). For each member: all rivals on 1–2 atoms, 60,000 three-atom rivals, audit-Prop-1 rivals and 20,000 random models (3.5 million in total). Results:
- 0 competitiveness failures;
- 0 all-world weak dominations;
- 0 failures of Lemma 2.4/2.5 as used;
- on a pool of 961 models: 0 cycles of any length at any world and 0 strict-(G) violations.

**Named rivals.**
- *Audit Prop 1's rival* (N corrected at i on E_i, changed on H): defended wherever it worsens N at the member's threshold world. Otherwise it is u-ward, and the defence is at another world.
- *Audit's concrete rival against C_w* (on Q ⊆ N_w, T's answer on one piece and the opposite on another): T's answer B on a piece of F_k(δ) is worse than silence at world k + 1, where C_k(δ) is a threshold set. So it is accepted at k + 1.
- *Departures and retreats of members* (observation 4): see §5.

---

## 4. Non-additivity

**Proposition 4.1 (PROVED).** Let N ∈ 𝓕 and let w be a world at which N is a threshold set: every world for T, w = u for Γ_u(t), and w ∈ {k, k+1} for C_k(δ). Fix disjoint bounded non-null sets:
- G, where N is not w-correct;
- H_0, where N is w-correct (on U, or on a mixed region).

For non-null H ⊆ H_0 let Y_H := N[H → S, G → w-correct]. Then N ⪯_w Y_H for every H. No bounded, finitely additive charge π on I, vanishing on null sets and positive on non-null sets, satisfies π(Add_w) ≥ π(Rem_w) for all these comparisons.

*Proof.* Add_w(N, Y_H) = H × {1} lies outside U_w(N), and Rem_w lies inside it. So Lemma 2.4(a) applies. For the charge, split H_0 into n non-null pieces. Some piece H has π(H × {1}) ≤ π(H_0 × {1})/n < π(Rem_w) for large n, because π(Rem_w) is a fixed positive number. ∎

The same argument works for each member separately. So the non-additivity is uniform over 𝓕 and sits in **the members' own local defences**, which are the comparisons that audit Cor 4 shows to be necessary.

**PP20's comparisons retained (PROVED).** Take E_1 ⊆ Sil(T) ∩ M_1 and E_2 ⊆ Sil(T) ∩ M_2. Then T[E_1 ∪ E_2 → A] adds the non-T step (g,2) on E_1 at world 1, so T ⪯_1 T[E_1 ∪ E_2 → A] by Lemma 2.4(a). PP20's non-endorsement proof (§3, "Not additive in disguise") therefore applies verbatim.

More generally, **T ⪯_w X iff w ∈ W(X)**. This is the PP17/PP20 all-worlds rule in its largest form, so no old T-defence had to be frozen or reassigned.

---

## 5. The lead's observations

**Observation 1 (uniformity from (IB)).** Correct. Here the rule is *defined* on records, and its uniformity over 𝓕 comes from Lemma 2.5, which holds whatever the old side is.

**Observation 2 (triangle lemma; PROVED).** supp rec(A,C) ⊆ supp rec(A,B) ∪ supp rec(B,C). So a triangle has 0, 2 or 3 essentially unbounded edges.

**Lemma 5.1 (PROVED).** Let C ≠ N be coherent and let X differ from N on a bounded set. Then rec(C,X) is unbounded.

*Proof.* {C ≠ X} ⊇ {C ≠ N} ∖ {X ≠ N}. The first set is a non-null cone, so by homogeneity (REFEREE_Z_PP19 §2) a non-null part of it lies outside every ball. ∎

So the local defences of a model N (bounded records out of N) and the dominations of N's local rivals by other coherent models (necessarily unbounded) meet only in triangles with exactly one bounded edge. This is how the lead's lemma organises any (TC) proof that mixes the two layers. In Theorem 3.5 no such triangle closes, because each world is acyclic. The two layers are genuinely different: the members' defences against bounded rivals use bounded records, while every domination in §6 of a bounded rival of N by another member uses an unbounded record. Any extension that adds unbounded comparisons only has to check triangles with two or three unbounded edges; their bounded edge, if any, lies in the acyclic gated layer.

**Observation 3 (departures; PROVED; CHECKED, 0 violations on a 218-model pool).** At each world, guidance together with every departure that is not a pure improvement at w satisfies (TC), with all copies.

*Proof.*
- *Two departures in a row.* They compose only on disjoint supports, because the second needs silence where the first has just answered. The composite is a departure that keeps the first one's harm at w. The closing edge is the inverse of that composite: its old side is not silent, so it is not a departure, and it improves at w, so it is not guidance.
- *A departure next to guidance.* If the third edge is guidance, the departure is the inverse of a composite of two guidance links, so it is a weak improvement, which is impossible. If the third edge is a departure, the previous case applies to that pair of adjacent departures. ∎

This rule alone defends every model against fills of its own silence. It does not defend against retreats or flips.

**Observation 4 (the pump; CHECKED).** Correct. On cells, with A ⪯_i B a departure and B ⪯_i C a retreat, C is a strict improvement of A at i. Adding non-improving retreats creates more than 340 (TC) violations per world on the pool.

The gate resolves the pump by **orientation**. At world w, a departure and a retreat at the same place are accepted only if the steps each adds lie below the steps it removes. Both directions of a cycle can never pass (Lemma 2.2).

The bullet "retreats cannot simply be refused" is also right. Let Z be T made silent on majority-answer pieces of M_1, M_2 and M_3. In our system T ⪯_w Z at every world, so T strictly dominates Z.

**Observation 5 (regions are two-world problems).** This is exactly Lemma 2.5. On M_k the worlds aligned with the u-ward direction see only removals of T-steps, and the opposed worlds see only additions of non-T steps.

---

## 6. Dominations: material for KKM

All dominations below are strict at all three worlds, by antisymmetry (Lemma 2.2).

**Theorem 6.1 (PROVED; CHECKED, 50,019/50,019).** T ⪯_w X iff w ∈ W(X). So T strictly dominates X iff X is worse than T somewhere at every world, that is, iff X is not u-ward of T for any u.

*Proof.* Lemma 2.4 at every world. ∎

This class includes:
- every rival that touches U or uses contradiction;
- every fill of T's silence that reaches all three M_k with harm at each world;
- Λ_T, and the precise uniform model V_{c*} (a coherent model; dominating it is allowed).

**Theorem 6.2 (PROVED; CHECKED, 23,636 random rivals, 0 exceptions).** Let δ ∈ (0, δ*] and C := C_k(δ). Let X satisfy:
- (a) X is worse than C somewhere at each of the three worlds;
- (b) on F_{k+1}(δ*), X does not lower T's rank at world k + 2.

Then C ⪯_w X at all three worlds.

*Proof.*
- *Worlds k and k + 1.* C is a threshold set at both (Lemma 3.4′), so (a) and Lemma 2.4(a) apply.
- *World k + 2.* Path Γ_{k+2} runs phase 1 through q_{k+1} and phase 2 through q_k. Write κ := 1/3 + δ/(3δ*).
  - *Added steps.* On F_k(δ), where C = S and T = B, X can only add (g,2), with key 1/3 + e_k(g)/(3δ*) ≤ κ, and (g,3), which is non-T. Off F_k(δ), where C = T, it can only add non-T steps.
  - *Removed steps.* On F_k(δ), X can remove (g,1), which exits only in phase 3 (key ≥ 2/3). Off F_k(δ), X removes T-steps whose keys lie in phase 3, or in phase 2 at entry times above δ (keys > κ), or in phase 1 on F_{k+1}(δ*). Condition (b) excludes the last case.
  - So sup Add ≤ κ < inf Rem, and Add is non-null by (a). ∎

**Corollary 6.3 (PROVED; CHECKED: 33,975 fills and 29,945 rivals in PP20's class, 755,656 predicted dominations, 0 failures).** Let X ≠ T with X = T a.e. on F := F_1(δ*) ∪ F_2(δ*) ∪ F_3(δ*). This is PP20's class 𝓛 for these footprints. It contains:
- every measurable fill of T's silence, bounded or conic;
- every change of T's answers off F;
- X*, Y_12, and the A_i, B_i, R_i fills.

Then **every C_k(δ) with k ∈ W(X) and δ ∈ (0, δ*] strictly dominates X**.

*Proof.* (a) holds:
- at k, because X is worse than T somewhere, necessarily off F, where C = T;
- at k + 1 and k + 2, because on F_k(δ) the rival keeps B, which is wrong at both majority worlds, while C is silent.

(b) holds because X = T on F_{k+1}(δ*). ∎

So **every incoherent fill of T's silence is strictly dominated by a member at all three worlds.** This is PP20 Theorem 3.2(3), now with defenders that are themselves competitive and undominated by the same rule (Theorem 3.5).

**What is left.** By Theorem 6.1, the rivals not dominated by T are exactly the models that are u-ward of T for some u. Corollary 6.3 serves those that leave a footprint untouched. The rest change T on a whole footprint.

**Proposition 6.5 (residual footprint rivals; PROVED; CHECKED, 63/63 undominated, and 63/63 dominated once B is restored on one footprint atom).** For every k and every non-null E ⊆ Sil(T) ∩ M_k, the model X := C_k(δ*)[E → A] is dominated by no member of 𝓕. X is incoherent if E is bounded, by Lemma H.

*Proof.* X is (k+1)-ward and (k+2)-ward of T, and changes only M_k (A-ward).
- *T:* X is strictly better at k + 1.
- *Γ_{k+1}:* each member is (k+1)-ward. At world k + 2 the opposed regions are M_{k+1} and M_{k+2}. There X = T, so a deviation of N there contributes removals of non-T steps, while any added steps are T-steps. So either the pair is not separated or it is a strict improvement; both are refused.
  - If N deviates only on M_k, then N is a phase-1 member C_k(δ). X is weakly better than C_k(δ) at k + 1 and strictly better on E, so world k + 1 refuses.
- *Γ_{k+2}:* the same argument at world k + 1. Every member deviates on F_{k+1} ⊆ M_{k+1}, which is an opposed region.
- *Γ_k:* at world k + 1, the deviation on M_{k+2} adds T-steps.
  - If N also deviates on M_{k+1} (phases 2–3), that deviation removes non-T steps, so the pair is not separated.
  - If N = C_{k+2}(δ) (phase 1), the added steps are (g,2) on F_{k+2}, with phase-2 keys of Γ_{k+1}. X removes (g,2) on all of F_k(δ*), whose keys are phase-1 keys of Γ_{k+1}, so the added keys exceed the removed ones and the gate fails. ∎

This is PP20's Proposition 5.1 zone, met again. Any (S)-extension must dominate these incoherent rivals by Theorem Z and KKM. In this system no member does.

---

## 7. Limits, classification, and what next

### 7.1 Theorem 6 of PP2 applies

PP2 Theorem 6 (refereed) assumes:
- (H2) at some world w, every accepted non-guidance comparison passes the weak gate of a fixed key whose restriction to {(g,1) : g ∈ M_w} has null level sets;
- (H3) strict (G) at the other worlds.

Under these, no selection with (S) and closed sections exists, for any verdicts and any target. Our system satisfies (H2) at every world, and the theorem's proof is symmetric in the world. **So the relation of Theorem 3.5 admits no (S)-selection, and neither does any extension that keeps any one world a gate with such a key.** PROVED, by citation.

### 7.2 The requested classification

| Kind of failure | Outcome |
|---|---|
| Contradiction from (G), (IB), (TC) plus the requested defences, uniformly over a family | **None.** Theorem 3.5 is a model. The test as posed is consistent. |
| Contradiction caused by an optional old comparison | **None.** PP20's a-, b- and t-records, and its non-endorsed family, all have counterparts. T's defences are installed at every non-improving world (§4). |
| Failure of the chosen geometry | **For KKM:** Proposition 6.5. Footprint-changing one-world improvers of T are dominated by no member. |
| Failure of the mechanism | **For (S):** §7.1. Fixed keys with null level sets on vertex classes. |

In addition, Proposition 2.7 shows that under T-anchoring the geometry is not a free choice: it must lie in the three cones.

### 7.3 Which coherent models are competitive here

**CONJECTURE 7.3.** In the system of Theorem 3.5, the competitive coherent models are exactly the members of 𝓕.

*Evidence.*
- PROVED: such a model must be u-ward of T (Prop 2.7). If it is a threshold set of k_u, it is some Γ_u(t), because U_u determines a model.
- NUMERICS (`check_competitive_class.out`): of 600 random coherent cell models (polygons, contractions to random points, random coarsenings), every one that is not a member fails some rival. Three of them survived all rivals on 1–3 atoms but fell to a 6-atom rival with one crossing pair per world (PP2 Prop 3 shape).

Threshold sets of one key form a chain, so no two-dimensional family can be made of threshold members. In a fixed-key system, a 2-dimensional family would need PP2's third shape ("threshold at no world, every cheap gain paid by a cheap loss elsewhere"), which Proposition 2.7 excludes under T-anchoring.

### 7.4 Why the test does not discriminate, and what would

The two-world laboratory stopped discriminating once gates were found (DESIGN_MEMO §8.3). The same now happens to the three-world two-model test, even in its family form: a gate, which passes it, is already excluded for (S) by S11.

A discriminating version should add at least one of the following:
- (i) **a two-dimensional family**, which fixed-key gates cannot supply (§7.3);
- (ii) **domination of the footprint rivals of the members' own coarsenings** (Prop 6.5), by members, as Theorem Z and KKM require;
- (iii) **that the relation, at each world, accept some non-guidance comparison out of a member that fails every fixed-key gate on that world's vertex-class steps.** This is exactly the negation of (H2).

Fixed-rival sections are also not closed here. At the threshold world, {t : Γ_u(t) ⪯_u X} is an up-interval that can be open at its left end, as the trivial verdict gives no continuity (gate2d needed (V1)–(V2) for that). This is a further, independent obligation.

### 7.5 A concrete escape route suggested by the proofs (CONJECTURE, with a partial proof)

Lemma 2.5 and Proposition 2.7 use only the **two-level split**: T-steps above non-T steps. The fine orders inside the two levels are used only for the chains' threshold property (Γ_u), the anti-side threshold property (C_u), and Theorem 6.2.

The paths' phases 1–2 never move world u's own vertex-class steps {(g,1) : g ∈ M_u}. So one may collapse all T-steps on that vertex class at world u into an **atom** at key 1, and refuse a separated pair whenever both its added and its removed sets meet the atom.

- The acyclicity proof survives. Steps whose added set lies inside the atom remove nothing, and below the atom the window argument is unchanged. (PROVED in outline; to be written out.)
- Theorems 2.6, 3.5 (truncated to t ≤ 2/3, that is, the coarsening phases), 6.1 and 6.2 and Corollary 6.3 survive, because none of them adds or removes atom steps on both sides.
- The step "c ↦ μ{k_1(·,1) ≥ c} takes the value μ(M_1)/2" in PP2 Theorem 6 can then fail. Whether it does depends on whether T's S- and A-regions fill more than half of M_1. Whether every variant of Theorem 6 is escaped is open.

This is PP2's route (E2), with the content of the tie rule moved to the region structure that Lemma 2.5 already controls. It is the most direct next test of whether a gate-like local layer can coexist with (S).

### 7.6 Summary of status

| Item | Status |
|---|---|
| T-anchored gates: acyclic, (G), (IB), (TC), no ties (Lemma 2.2) | PROVED (gate2d, refereed) |
| Threshold lemma, transfer lemma, defence transfer (2.4–2.6) | PROVED |
| Competitive coherent ⇒ u-ward of T (2.7) | PROVED |
| Single-region coarsenings, sharp δ* (3.1); contraction (3.2) | PROVED; CHECKED exactly |
| Main theorem: family 𝓕 competitive against every model, undominated, uniform (3.5) | PROVED; CHECKED on cells |
| Non-endorsement out of every member; PP20 family and defences retained (4.1) | PROVED |
| Departures alone are (TC)-safe; the pump (obs. 3, 4) | PROVED; CHECKED |
| T dominates all non-u-ward rivals; C_k(δ) dominations; all fills and PP20's 𝓛 (6.1–6.3) | PROVED; CHECKED |
| Residual footprint rivals dominated by no member (6.5) | PROVED; CHECKED |
| No (S) for this system or any extension keeping one world gated (7.1) | PROVED (PP2 Thm 6) |
| Competitive coherent class = 𝓕 (7.3) | CONJECTURE; NUMERICS |
| Atom escape from Theorem 6 (7.5) | CONJECTURE (partial proof) |
