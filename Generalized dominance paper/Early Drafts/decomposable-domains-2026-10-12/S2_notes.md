# S2. Trying to refute (R4) — what blocks it, and a proof that leading charges need no nestedness

Round 13 (BRIEF12), construction side, task (R4). Scripts: `s2py/` (run with `python3 -I`).
Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. No assumption is added to the framework. Terminology follows
TERMFIX_RULES (U-domain = class of evaluable models D ⊆ U).

## 0. Summary

I did **not** build a non-nested system. The attempts failed in a way that can be proved, and the proof gives
more than I was asked for. Two theorems come out of it.

| # | Statement | Label |
|---|---|---|
| S2.0 | **The tie remark made precise.** (a) In every additive ranking (any n), Bayes error sets at distinct weights are strictly nested, whatever tie-break is used. So a crossing can only sit inside one tie face. (b) n = 2: a purely additive system with a non-null tie at an interior weight violates (S)+(C) (an incoherent tied splice exists). (c) n = 3, additive: every edge selection satisfying the axioms is nested. **So the write-up's remark (before Prop. comonotone) that (Nest_e) "can fail at exceptional edge weights where a non-null tie set is split in crossing ways" cannot happen in any additive system satisfying the axioms.** | PROVED |
| PL | **Parallelogram lemma** (any n). Take models C, F and D ⊆ C△F, and put X = C△D, X′ = F△D. Then C ⪯_k X ⟺ X′ ⪯_k F at every world k. If F ∈ C_L and C weakly dominates X at every world, then (C) makes X and X′ coherent. | PROVED |
| **S2.1** | **Leading charges are strictly positive, with no nestedness hypothesis** (any n ≥ 2, M_U, K′ ⊆ Δ°). If π is a leading charge of world i on M (finitely additive allowed), then π is 0 on M or π(D) > 0 for every non-null D ⊆ M. In the second case its countably additive part has density > 0 a.e., π endorses every world-i comparison, and world i adds up (SP^reg_i). The proof uses only strict (G), (IB) and (S) on the edges at e_i. | PROVED |
| S2.1′ | Consequences. Theorem E2 holds without (Nest). Theorem Q36(a), (b) and Corollary Q37 hold without (Nest_e) for worlds with a nonzero leading charge, in particular for every world that is lexicographic with charge levels. | PROVED (Q37 at the status of Thm M0closed(b)) |
| **S2.2** | **Q2.N in the leading-charge class.** If n = 2, every axiom holds, and *either* world has a nonzero leading charge on M, then {E_1C : C ∈ C_L} is a chain. Each member is fixed a.e. by its π-level. | PROVED |
| S2.3 | Hence any two-world refutation of (R4) needs *both* worlds without a nonzero leading charge: no additive world, and no lexicographic world whose first level is a charge. These are the worlds of the open SP^reg class. Non-nestedness therefore cannot carry a failure of SP^reg at any world that has a leading charge. | PROVED (from S2.1, S2.2) |
| S2.4 | Three worlds, edge e_ij: the level-function argument transfers, but PL needs the third world k. I give the necessary anatomy of a crossing edge selection: it requires C_L fans resolved by incomparability at world k, at a continuum of levels. None was constructed. | PROVED (necessary conditions); construction not achieved |

The brief proposed a route: an additive atom tie, then crossing splits, made essential. That route provably dies:
- with no tie-breaker, at (C);
- with any tie-breaker that keeps a leading charge (additive primaries, N26.1-type lexicographic systems, lexicographic worlds with charge levels), at S2.2.

A half-vanishing leading charge would have made non-nestedness carry a failure of SP^reg (§5c). It is excluded by S2.1.

---

## 1. Setting and notation

M_U is the U-domain; for n = 2 take K′ = [α′, β′] in the weight t of world 2. The mixed part is M = M⁻ ⊔ M⁺:
- M⁻ = {g₁ < 0 < g₂}, with coordinate σ ∈ (0, α′);
- M⁺ = {g₁ > 0 > g₂}, with coordinate τ ∈ (β′, 1).

The coherent models are D_{[α,β]} (Prop. lattice), with E_1 = {σ < α} ∪ {τ ≤ β} and E_2 = M ∖ E_1. Two coherent models cross iff their endpoint pairs are not comonotone. Then A := E_1F ∖ E_1C lies in one half and B := E_1C ∖ E_1F in the other.

By N9.4 / Lemma vectorform, world k is a strictly monotone, cancellative order ≤_k on world-k error sets, and C ⪯_k X depends only on the pair of difference sets (E_kC ∖ E_kX, E_kX ∖ E_kC).

A *leading charge* of world i on M (write-up, before Thm Q36) is a bounded charge π ≥ 0 vanishing on null sets such that, for measurable A, B ⊆ M:

  (i) π(B∖A) > π(A∖B) ⇒ A ≤_i B;  (ii) A ≤_i B ⇒ π(B∖A) ≥ π(A∖B).

Write π = ρμ + σ (Yosida–Hewitt). Since σ is purely finitely additive, for every ε > 0 there is a carrier Z with μ(Z) < ε and σ(M∖Z) = 0 (N14 Lemma Y).

Edge facts (Lemma Q34): for p ∈ e_ij the model C_p agrees with P_i off R_ij, and E_jC_p = R_ij ∖ E_iC_p. For A ⊆ R_ij, X_A is the edge test model: equal to P_i off R_ij, with E_iX_A = A and E_jX_A = R_ij ∖ A. Moreover C_{e_i} = P_i (by competitiveness on {i} and strict (G)), so E_iC_{e_i} = ∅, and C_{e_j} = P_j, so E_iC_{e_j} = R_ij.

## 2. The additive tie, made precise (S2.0)

**S2.0(a) (PROVED).** Let ψ be an additive ranking on M_U with strictly positive densities, any n. Take an edge, or n = 2, with weights (1−t, t). Put r(g) = ρ_i/(ρ_i+ρ_j) on R_ij. Then g ∈ E_i(B_t) when r(g) < t, g ∉ E_i(B_t) when r(g) > t, and the choice is free when r(g) = t. For t < t′ the largest t-Bayes error set {r ≤ t} is contained in the smallest t′-Bayes error set {r < t′}. So Bayes error sets at distinct weights are nested for every tie-break, and two crossing Bayes models are Bayes at one common weight t₀ and differ only on the tie set Z_{t₀}.
NUMERICS: `s2py/additive_tie.py` (a), exact rationals, 39 weights, every pair.

**S2.0(b) (PROVED).** n = 2. If Z_{t₀} is non-null for an interior t₀, then every t₀-Bayes model is undominated. Some of them are incoherent:
- Z_{t₀} is a cone mod null, and a radial splice is not a cone (R2 Lemma U);
- inside the double atom used here, a non-threshold split of equal ρ₁-mass also works.

By Fact 0 (Theorem kkm), an undominated incoherent model is tied at both worlds with a selected model, against (C).

So the scenario "additive two-world system with an atom tie whose selection chooses crossing splits" is not a system at all. The coherent t₀-Bayes models do form a rectangle full of crossing pairs. But on Z, ρ₂ = κρ₁, so an incoherent split with the same ρ₁-mass has the same profile at both worlds.
NUMERICS: `additive_tie.py` (b), (c): a 5×5 rectangle with 100 crossing pairs, and an explicit incoherent tied splice.

**S2.0(c) (PROVED).** n = 3, all three worlds additive with strictly positive densities, every axiom. Then every edge selection is nested.

*Proof.*
1. An edge-selected C_p is competitive on {i, j}, hence weakly Pareto for (ψ_i, ψ_j). By Lyapunov it is supported, so it is s-Bayes for worlds i, j at some s. By (a), crossing edge models C, F share s₀ and differ only on Z := Z_{s₀} ⊆ R_ij, where ρ_j = κρ_i.
2. Same ρ_i-level. Then ψ_i and ψ_j are equal, so undominatedness forces ψ_k to be equal too (k the third world), and C, F are tied at every world. A Lyapunov half-splice of the difference (for the vector measure (ρ_i, ρ_k-signed)) is incoherent and tied, against (C).
3. Different levels. Each is ψ_k-minimal at its level among the splits of Z; otherwise a split with the same ψ_i, ψ_j and smaller ψ_k dominates it. By the bathtub principle a minimiser has E_i ∩ Z = {f > λ} ∪ (part of {f = λ}), where f is the world-k cost per unit ρ_i. Crossing forces a common λ and A ∪ B ⊆ {f = λ}. On that set, P ⊆ A and Q ⊆ B with ρ_i(P) = ρ_i(Q) give X = C△(P∪Q) with equal ψ_i, ψ_j, ψ_k, again against (C) (choose X incoherent). ∎

NUMERICS: `s2py/face_np.py`, 500 random faces: the NP splits are nested; a flat block allows crossing optima together with an equal-profile splice.

*Correction to the write-up.* The sentence before Prop. comonotone, "it can fail at exceptional edge weights where a non-null tie set is split in crossing ways", is true of the family of Bayes face models, not of any edge selection of an additive system satisfying the axioms. For edges, the only surviving mechanism is a non-additive third world (§6).

## 3. The parallelogram lemma (PL)

**Lemma PL (PROVED, any n).** Let C, F ∈ M_U and D ⊆ C△F, and put X := C△D, X′ := F△D. Then, at every world k:

  (E_kC ∖ E_kX, E_kX ∖ E_kC) = (E_kX′ ∖ E_kF, E_kF ∖ E_kX′).

Hence C ⪯_k X ⟺ X′ ⪯_k F for every ranking satisfying (G) and (IB). If F ∈ C_L and C ⪯_k X at every world k, then X′ ⪯_k F at every k. Undominatedness of F forbids any strict comparison, so X′ ~_k F at every k and also C ~_k X. By (C), X′ and X are coherent.

*Proof.* E_kX = E_kC △ D and E_kX′ = E_kF △ D. On D, C and F give opposite advice, so E_kF ∩ D = D ∖ E_kC. Therefore:
- E_kC ∖ E_kX = D ∩ E_kC = D ∖ E_kF = E_kX′ ∖ E_kF;
- E_kX ∖ E_kC = D ∖ E_kC = D ∩ E_kF = E_kF ∖ E_kX′. ∎

In words, C → X and X′ → F are the same exchange. NUMERICS: `s2py/pl_identity.py`, 20 000 random configurations, n = 2, 3, 4, no violation.

*Cross-agreement (PROVED, n = 2, from PL plus competitiveness).* Let C, F ∈ C_L cross, and let P ⊆ A, Q ⊆ B be such that C△(P∪Q) or F△(P∪Q) is incoherent. Then:
- the two worlds never order P against Q in opposite strict directions;
- the pair is never tied at both worlds;
- if the worlds are complete, both order P against Q the same way, strictly.

In additive terms this forces ρ₂/ρ₁ to be constant on A ∪ B, i.e. a tie. So any crossing needs the two worlds to behave on the difference sets like a common, tie-like order. This motivated §4.

## 4. Theorem S2.1: leading charges are strictly positive, without (Nest)

**Theorem S2.1 (PROVED).** Let n ≥ 2, M_U with K′ ⊆ Δ° (n = 2: K′ an interval), and a ranking with strict (G), (IB) and (S). Let π be a leading charge of world i on M. Then either π(M) = 0, or π(D) > 0 for every non-null measurable D ⊆ M. In the second case:
- ρ > 0 a.e. on M (N19 Lemma R1);
- by (ii), π endorses every world-i comparison between subsets of M;
- the weight π + μ|_{N₊} is positive on non-null subsets of U and endorses every relevant comparison, so world i adds up (SP^reg_i).

Not used: (LA), (C), nestedness, completeness, countable additivity of π, any hypothesis on interior indices.

*Proof.* Fix j ≠ i with π(R_ij) > 0. On e_ij put m(p) := π(E_iC_p).

1. **m is lower semicontinuous on e_ij.**
   - Let p* ∈ e_ij with E_iC_{p*} non-null; otherwise m(p*) = 0 and there is nothing to show.
   - Given ε, take a carrier Z of σ with μ(Z) small, and a non-null D ⊆ E_iC_{p*} ∖ Z with ρμ(D) < ε.
   - Put A := E_iC_{p*} ∖ D. Then π(A) > m(p*) − ε. Every q ∈ e_ij with m(q) < π(A) has C_q ⪯_i X_A by (i), so q ∈ S_i(X_A).
   - If such q accumulate at p*, closedness gives C_{p*} ⪯_i X_A. But X_A ≺_i C_{p*} by strict (G), since its world-i errors are fewer by the non-null set D.
   - Hence liminf_{q→p*} m(q) ≥ m(p*) − ε for every ε.
2. **m is upper semicontinuous on e_ij.**
   - Suppose q_k → q* in e_ij with m(q_k) > m(q*) + η, η > 0. Then R_ij ∖ E_iC_{q*} is non-null.
   - Take a non-null D in it, off a small carrier, with π(D) < η, and put A := E_iC_{q*} ∪ D. Then π(A) < m(q_k).
   - By (ii), C_{q_k} ⋠_i X_A. Since q_k ≠ e_i, competitiveness on supp q_k ∋ j gives C_{q_k} ⪯_j X_A. Closedness of S_j(X_A) then gives C_{q*} ⪯_j X_A.
   - But E_jX_A = E_jC_{q*} ∖ D, so X_A ≺_j C_{q*} by strict (G). Contradiction.
3. **Every level is attained.** m is continuous on the segment e_ij, with m(e_i) = 0 and m(e_j) = π(R_ij). So m attains every v ∈ [0, π(R_ij)].
   - Call v *generic* if it is not the value of a weak local maximum or minimum of m. Such values are countable (each is the min or max of m over a rational interval), so generic v ∈ (0, π(R_ij)) exist.
4. **Optimality at both worlds.** Let v be generic and m(p) = v. Every neighbourhood of p contains indices with m < v and indices with m > v. For every A ⊆ R_ij with π(A) = v:
   - indices with m(q) < v lie in S_i(X_A) by (i);
   - indices with m(q) > v lie in S_j(X_A), by (ii) and competitiveness as in step 2.
   - By closedness, C_p ⪯_i X_A and C_p ⪯_j X_A.
5. **No non-null π-null set in R_ij.** Let N′ ⊆ R_ij be non-null with π(N′) = 0.
   - If N′ ∩ E_iC_p is non-null, A := E_iC_p ∖ N′ has π(A) = v and X_A ≺_i C_p (strict (G)), against step 4.
   - If N′ ∖ E_iC_p is non-null, A := E_iC_p ∪ N′ has π(A) = v and X_A ≺_j C_p, against step 4.
   - So π is strictly positive on R_ij.
6. **Linking** (as in Thm Q36). R_ij ∩ R_ik ⊇ a neighbourhood of e_i − η(e_j + e_k) in U, which is non-null since K′ ⊆ Δ°. So positivity on R_ij gives π(R_ik) > 0, hence positivity on R_ik.
   - M = ⋃_{j≠i} R_ij, so either π(R_ij) = 0 for every j (π|_M = 0) or π is strictly positive on M.
   - For n = 2, R_12 = M and step 6 is void. ∎

*Why nestedness was never needed.* Earlier proofs parametrised the edge selection by its chain c_b. Here the edge is parametrised by the π-level m(p). Closed sections plus competitiveness make m continuous. At a generic level the selected model is optimal at *both* edge worlds among all edge test models of that level. Strict (G) then forbids π-null sets, from either side. Strict escape and the drop lemmas are not used.

**Corollaries (PROVED).**
- (a) **E2 without (Nest).** In a two-world system with strict (G), (IB) and (S), every leading charge is 0 or strictly positive with ρ > 0 a.e. This is the conclusion of Thm E2, with (Nest), (K) and the chain removed.
  - Prop. B2(b) becomes: lex(ν⁺, λ) cannot be world 1 of *any* full system, nested or not.
  - Corollary E2′ (lexicographic worlds with charge levels) holds without (Nest).
- (b) **Theorem Q36(a), (b) without (Nest_e)**, for any n, any K′ ⊆ Δ°.
- (c) **Corollary Q37, strengthened.** Assume (H_U). If every world is (CP-a), or has a leading charge nonzero on M (in particular is lexicographic with countably many bounded charge levels), or is complete and satisfies (Nest_e) on both edges at e_i, then T₁ is not covered.
  - Status: as Thm M0closed(b), i.e. imports N13 Prop. B and N19 Prop. R3(a), each read once; CHECKED where a complete world enters (Savage).
  - Contrapositive (replacing (E-a)/(E-b) after Cor. Q37): every world of a cover of T₁ that does not add up is not (CP-a), has **no** leading charge nonzero on M (unconditionally), and, if it is complete, has a non-nested edge family at e_i.
- (d) The write-up's lifting bullet in (f), "a proof of (R4) in its edge form removes (Nest_e) from Thm Q36 and Cor Q37", is now discharged for leading charges without (R4). (R4) remains relevant only for:
  - complete worlds, through Savage fineness (Prop Q35(5) needs (Nest_e));
  - general acceptance cones.

*Referee request.* S2.1 is short but it changes the status of several write-up statements. It has had one reader (me). Steps 1–2, the carrier choice and the use of competitiveness on supp q_k, need an independent check before the write-up is updated.

## 5. Theorem S2.2: two worlds — a leading charge at either world forces a chain

**Theorem S2.2 (PROVED).** Let n = 2 with every axiom (strict (G), (IB), (LA), (S), (C)). Suppose world 1 has a leading charge with π(M) > 0; the case of world 2 is symmetric. Then:
- π is strictly positive (S2.1);
- C_L is a chain;
- for every F ∈ C_L, E_1F = Q(π(E_1F)) a.e. for one increasing family Q(·). So (Nest) and Conjecture Q2.N hold.

*Proof.*
1. Let m, generic levels and step 4 be as in S2.1, on Δ = e_12. Every C_L member is tied at both worlds with a selected model (Fact 0 with (C)). By (ii), ties preserve π-levels.
2. At a generic v, the selected C(v) is optimal at both worlds among all regular X with π(E_1X) = v. So every C_L member at level v is tied with C(v).
3. **A generic member is nested with every member.** Let C = C(v) be generic and F ∈ C_L, and suppose they cross.
   - Take a middle σ-band P ⊆ E_1F ∖ E_1C and Q ⊆ E_1C ∖ E_1F, both off a small carrier, non-null, with ρμ(P) = ρμ(Q). Then π(P) = π(Q).
   - X := C△(P∪Q) has level v, so C ⪯_1 X and C ⪯_2 X by step 2.
   - PL gives X′ := F△(P∪Q) ∈ C_L. But X′ is incoherent: E_1X′ ∩ M⁻ = {σ < α_F} ∖ P is not an initial σ-set. Contradiction.
4. **Fans collapse.**
   - Let F ∈ C_L have level v_F ∈ (0, π(M)). For generic v < v_F, step 3 and strict positivity give E_1C(v) ⊆ E_1F.
   - Let Q_− be the union of these sets (an increasing family). Then π(Q_−) ≥ sup v = v_F = π(E_1F), so E_1F ∖ Q_− is π-null, hence null.
   - So E_1F = Q_−(v_F), and members are ordered by level.
   - Level 0 gives P_1; level π(M) gives P_2. ∎

So the brief's suggested route (a tie set, crossing splits, then many crossings) has no realisation in the leading-charge class. The recorded attempts and the step at which each fails:

- (a) *Pure additive tie.* Fails (C) (S2.0(b)).
- (b) *Lexicographic tie-breaking, N26.1-style, with frontiers.* At one primary level, a frontier of pairwise crossing coherent models (an S₁-best end and an S₂-best end) passes every local test. These are: R2 Thm 7 (improvable models only at a local minimum of the primary), the jump test (a frontier must be traversed on an index interval), and competitiveness.
  - It dies globally. The spine below the frontier level is optimal at both worlds (step 2), hence nested with every frontier member (step 3). The spine limit Q_− is contained in every frontier member with the same π-level, so the frontier is one model (step 4).
  - Without S2.2 I had only the additive-secondary case: Lyapunov plus multiplier normal form make the spine limit optimal at both worlds, and every other level model is weakly dominated by it.
- (c) *Half-vanishing leading charge (the load-bearing candidate).* Before S2.1 was available, I derived the forced anatomy of a two-world system with a countably additive leading charge vanishing on a non-null N:
  - N ⊆ E_1C(v) for every generic v (from Lemma G-SE);
  - the first top-level index selects the model with E_1 = M ∖ N, so N = M⁻ or N = M⁺;
  - the selection is the non-nested "Z-path": (0,β′) → (α′,β′) → (α′,1⁻), a jump to (0,1), then (α′,1);
  - world 1 then fails SP^reg: the relevant comparisons C(v) ⪯_1 C(v) ∖ Z ∪ D, with Z ⊆ N and D small with π(D) > 0, force every endorsing charge to vanish on N.

  This would have been exactly "non-nestedness carrying a failure of SP^reg". It is excluded by S2.1 step 5: the generic C(v) is optimal at both worlds, so it can neither contain nor avoid a non-null π-null set. The exclusion uses only the edge selection.
- (d) *Exact test with R5.* By Thm R5(3), a successful system for a crossing selection exists iff some total choice κ has Cl_5(κ) clean. In the leading-charge class, S2.2 shows none is clean. The outcome reached is (c) of the exact test: an incoherent X′ tied with a selected F, through PL. If the frontier is not traversed on an interval, it is instead a non-closed section. I did not run the test numerically: a computable instance would need an explicit non-additive cone, and every explicit cone I tried had a leading charge.

## 6. Three worlds, edges, T₁'s U-domain (S2.4)

On an edge e_ij of a three-world system:
- S2.1 transfers in full;
- the level function m is continuous on e_ij;
- at generic levels the edge-selected model is optimal at worlds i and j among edge test models of its level.

What does **not** transfer is PL's conclusion, because C ⪯_k X at the third world k is not forced. So (Nest_e) is not proved even when worlds i and j are additive.

**Proposition S2.4 (necessary anatomy; PROVED).** Let n = 3 and assume every axiom. Let world i have a nonzero leading charge π (strictly positive by S2.1). Suppose edge-selected C (at a generic level v) and F ∈ C_L cross on e_ij. Then:
1. For every P ⊆ E_iF ∖ E_iC and Q ⊆ E_iC ∖ E_iF with π(P) = π(Q) and X′ := F△(P∪Q) incoherent, X := C△(P∪Q) satisfies C ⋠_k X (PL plus step 2).
2. Equivalently, for every such exchange the third world does not weakly prefer C; since X is not in C_L, and in the cases built here (worlds i, j additive, so the face is tied at those worlds) it is weakly dominated by a selected Y at the same level that beats it strictly at world k.
3. Hence C_L contains, at level v, at least two non-tied coherent members that are tied at worlds i and j and incomparable at world k: a *fan*.
4. If worlds i, j are additive, a crossing of the edge selection on a continuum of levels needs fans at a continuum of levels in one (i, j)-tie face. That is a two-parameter family in C_L, which must be selected (up to ties) at interior indices.
5. If world k also has a strictly positive leading charge and C is world-k-correct on a non-null part of both A and B, then step 1 fails by (i), so no crossing. A crossing therefore needs C to be world-k-wrong on almost all of A or of B.

No three-world example was constructed. Specifying the interior selection of the two-parameter fan family with closed sections at all three worlds is the open step. I stopped there for two reasons:
- by S2.1, such an example could not disturb SP^reg at any world with a leading charge;
- on T₁'s domain it could matter only at a complete world (Q36(c), through Savage fineness) or at a world without a leading charge.

So the three-world edge version of (R4) is now relevant only to those two cases.

## 7. What a refutation of (R4) must look like (for the proof side)

- **Two worlds.** Neither world has a nonzero leading charge (S2.2). So neither is additive, lexicographic with a charge first level, or of B2-type. Also needed:
  - cross-agreement on the difference sets of every crossing pair (§3);
  - no selected model at any generic level of any candidate "level" that is optimal at both worlds.

  This is the same class in which ¬SP^reg would have to live. By S2.1 a world with a leading charge adds up whether or not the selection is nested, so in the leading-charge class non-nestedness gives a cover nothing.
- **Three worlds, edge.** A crossing needs third-world fans as in S2.4. It is irrelevant to leading-charge worlds. The remaining uses of (Nest_e) are Q36(c) (complete worlds, via Prop. Q35(5)) and Thm Q36's comment on general acceptance cones.
- **Candidate true statement (CONJECTURE).** In two worlds Q2.N holds in general. The proof would need a substitute for the leading charge: a real "level" with (i), (ii) and inner/outer approximation. A complete world with a real-valued representation satisfying an approximation property would do. Whether (S) supplies such a level for complete worlds without (Nest) is open; it is the missing step for Q36(c) without (Nest_e).

## 8. Changes the write-up would need (after refereeing S2.1, S2.2)

- §8.4(c) and §8.5: Thm E2 and Cor. E2′ hold without (Nest), via S2.1; restate them, or add S2.1 after Thm Q36. Thm Q36(a), (b) drop (Nest_e). Cor. Q37 and its contrapositive (E-a)/(E-b) are as in §4(c).
- The sentence before Prop. comonotone: correct as in S2.0 (additive systems always have nested edge selections; crossing tie-splits occur only in the family of face models).
- Conj. Q2.N: proved when some world has a nonzero leading charge (S2.2).
- (f)(R4) and the lifting bullets: the first bullet is discharged for leading charges. (R4) now matters only for complete worlds (Savage fineness) and for worlds without leading charges.
- The "precise open class" in two worlds: "without a nonzero leading charge" no longer needs (Nest).

## 9. Files

- `s2py/additive_tie.py`, `.out`: S2.0(a)–(b), exact rationals. Nesting across 39 weights with every tie-break; a 5×5 rectangle of coherent t₀-Bayes models with 100 crossing pairs; an explicit incoherent split with identical (ψ₁, ψ₂) (NUMERICS).
- `s2py/pl_identity.py`, `.out`: the PL set identity, 20 000 random configurations, n ∈ {2, 3, 4}, 0 violations (NUMERICS).
- `s2py/face_np.py`, `.out`: S2.0(c). NP splits are nested on 500 random faces without ties; a flat block gives crossing optima together with an equal-profile splice (NUMERICS).
