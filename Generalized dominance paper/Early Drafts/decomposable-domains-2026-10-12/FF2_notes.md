# FF2 (round 34, BRIEF26). A minimal-commitment cover certified by an end-priority invariant: what the invariant secures, where the attempt breaks, and the obstruction behind the break

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Where a step imports a result, the import and its recorded status are named.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: floating point or sampling. Nothing below rests on NUMERICS.
- **CONJECTURE**.

Scripts are in `ff2py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. All verdicts use exact rational arithmetic.

Setting: the full four-advice domain, three worlds, T1 the ε-contamination of u (any ε ∈ (0,1); the exact checks use ε = 3/10). Notation follows the write-up §2. A pair is indexed by its majority orientation h (two positive coordinates, one negative, the odd world o). Positions are M (accept h only), S (silence), O (accept −h only) and × (both). Records and their composition are those of AUDIT_nonlinear_programme (transition lemma). No assumption is added. Every extra hypothesis is a hypothesis of a stated result.

---

## 0. Outcome

**No cover of T1 was obtained. The attempt fails at competitiveness, the positive half of (S). The failure is an instance of one theorem (Theorem 4.1, PROVED modulo a named import chain).**

1. **The attempt (§§1–2).** I used the brief's minimal-commitment closure. The world orders A_i are the least relations closed under (IB) and transitivity that contain guidance, the dominations D(X) ≺_i X, and the chosen competitiveness comparisons. Selected models are comparable only where a generator forces it.
   - Consistency is certified by an **invariant**: a fixed record-level order P_i that contains every generator.
   - Membership in P_i is preserved by composition, including cancelled-change composites, because P_i is a set of records closed under composition (Lemma 1.1, PROVED). This is the precise sense in which the EE1 obstacle (EE1 Thm 3.1, Example 4.3) disappears.
   - The P_i chosen is **end-priority**. World i first compares a purely finitely additive charge E_i, concentrated at the coordinate planes. It then compares an integrable body field B_i, namely the X2.6 field with its attribution frozen at u.
2. **What the invariant secures (§2, PROVED).**
   - (IB), transitivity and strict (G) for every closure under it (Prop 2.1, Lemma 1.1).
   - T1 undominated in every such closure: T1 is strictly protected in P (Prop 2.3; sanity checks (C1)–(C3) CHECKED).
   - Non-additivity: no world of P has a bounded endorser positive on non-null sets, and every endorser's countably additive density vanishes on T1's error set (Prop 2.2).

   So the five design requirements of the brief are met at the level of the invariant (table in §2.4). Theorem gm does not apply. Q4.2 and L4 are satisfied with total blindness. The leading level is not a veto, so L3.4 does not apply. Interior selected models, which differ at the planes (the interior-locality lemma), are compared at the planes.
3. **Why the closure must be minimal (Lemma 2.4 and Cor 2.5, PROVED).** P itself cannot be the ranking. A leading functional that is neutral on some local improvement out of every selected model must be locally minimal along the selection at every such index. So it must be locally constant wherever it is continuous. For the posterior family, E_i(C_p) is continuous and non-constant on int Δ, so some section of P is not closed. This is the general form of the "vetoes cannot be paid" mechanism. Because the closure A need not refine E_i, the lemma does not bind A.
4. **Where A breaks (§3).**
   - Records supported away from the coordinate planes have zero end level, so the body judges them alone.
   - Competitiveness of C_p in A therefore forces C_p to be a pointwise Bayes model of the body field at some weight supported in supp p (Step 1 of Theorem 4.1). This holds whatever generators are chosen.
   - For the posterior family this fails at indices arbitrarily close to u. There are exact certificates at six indices, the closest p = (167/500, 333/1000, 333/1000) (CHECKED; `witness.out`, `witness_near_u.out`). Lemma 3.2 (PROVED) turns each certificate into a bounded-support modification of C_p that P, and hence A, ranks strictly better than C_p at every world.
5. **The obstruction (Theorem 4.1).** Take a selection continuous in measure, competitive on supp q at every q, with T1 selected. Suppose some integrable, strictly guiding additive field endorses every accepted comparison out of a selected model that changes advice only inside a fixed exhausting family of regions (for example, regions bounded away from the coordinate planes). Then the system is impossible.
   - The proof is CC1 Theorem 4.1's argument with its envelope hypothesis **localized**.
   - It uses neither (IB), nor transitivity, nor closed sections, nor (C), nor strict (G) of the ranking.
   - Corollary 4.3: in every cover whose selection is continuous in measure, **some world's accepted bounded-support comparisons out of selected models are endorsed by no integrable strictly guiding penalty**.
   - **So non-additivity confined to the coordinate planes cannot rescue a cover.** This covers finitely additive end levels, end vetoes, lexicographic priority near the planes and end-supported seeds. It closes, for continuous selections, the part of CC1 §5's escape (2) that lives at the planes.
6. **Partial-success statement, as the brief asks.** For the class tried, (G), (IB), transitivity, T1 undominated and (LF) are verified. Competitiveness fails, by Theorem 4.1 and concretely by the certificates of §3. (C), (LA) and closed sections of A were never reached.

**Single most important open point.** Does Theorem 4.1 survive when the selection is **not** continuous in measure? If it does, every cover of T1 needs a world that is non-additive on bounded-support comparisons out of selected models. A positive construction would then have to put its non-additivity in the body, near T1, not at the planes. If it does not, a jump of the selection (as in V1) is the only way left for locally additive worlds.

---

## 1. Setting: the minimal-commitment closure and what an invariant must be

### 1.1 Records

For models X, Y, rec(X, Y) is the measurable map that is the identity symbol ι where X and Y agree and the ordered advice pair (X(h), Y(h)) elsewhere, modulo null sets. Records compose where their arrows match at the middle advice. Opposite arrows compose to ι. By the transition lemma (AUDIT_nonlinear_programme; X1 Thm X1.1.1), on the full domain the preorders with (IB) and strict (G) at world i are exactly the sets of records that:
- contain ι;
- are closed under composition;
- contain every i-worsening record;
- contain no non-trivial i-improving record.

Here X ⪯_i Y ⇔ rec(X, Y) ∈ A_i.

### 1.2 The inheritance lemma

**Lemma 1.1 (PROVED).** For each world i, let P_i be a set of records with the four properties above. Let Γ_i ⊆ P_i contain ι and every i-worsening record, and let A_i be the closure of Γ_i under composition. Write X ⪯_i Y for rec(X,Y) ∈ A_i. Then:
- (a) A_i ⊆ P_i, and ⪯_i is a preorder with (IB) and strict (G).
- (b) Suppose no model Y ≠ T1 has rec(Y, T1) ∈ P_1 ∩ P_2 ∩ P_3. Then in A, T1 is undominated and is tied at every world with no other model.
- (c) If rec(C, X) ∈ Γ_i and rec(X, C) ∉ P_i, then C ≺_i X in A.
- (d) If C_p is competitive on supp p in A, it is competitive on supp p in P.

*Proof.*
- (a) P_i is closed under composition and contains Γ_i, so it contains the closure A_i. A_i contains ι and every i-worsening record by choice of Γ_i. It is closed under composition by construction. It contains no non-trivial i-improving record, because P_i contains none. The transition lemma gives the rest.
- (b) If Y weakly dominates T1, or is tied with it at every world, then rec(Y, T1) ∈ ∩_i A_i ⊆ ∩_i P_i. Hence Y = T1.
- (c) rec(X, C) ∉ P_i ⊇ A_i.
- (d) A_i ⊆ P_i. ∎

*Reading.*
- The closure A_i contains every composite, including those whose arrows cancel on a region and are then realized with a new common advice there. Such composites are records in A_i, and A_i ⊆ P_i.
- So **an invariant that is a composition-closed set of records survives (IB) transport and cancelled-change composites automatically**.
- The difficulty of EE1 (Thm 3.1, Example 4.3) arises only for invariants defined on *models*, such as thresholds r_i(X), whose monotonicity must be checked along every realization of every closure record.
- The price of a record-level invariant moves elsewhere. By (d), P must itself make every selected model competitive. Closed sections are a property of A, not of P.

### 1.3 The generators

- **(G)** every i-worsening record, and ι.
- **(D)** for each non-selected X, one selected C_{s(X)} with rec(C_{s(X)}, X) ∈ P_i and rec(X, C_{s(X)}) ∉ P_i at every world. This installs C_{s(X)} ≺_i X at every world (Lemma 1.1(c)). It is the brief's choice D(X); the selection rule s is left free.
- **(K)** for each p ∈ Δ and each model X, one world i ∈ supp p with rec(C_p, X) ∈ P_i.

Nothing else is generated. Selected models are comparable in A only through these generators and their composites. By Lemma 1.1, A has (IB), transitivity and strict (G), and it inherits T1's protection from P. What must still be proved is that (D) and (K) can be met inside P, and that sections of A are closed. §3 shows that (K) cannot be met.

---

## 2. The invariant: an end-priority certificate

### 2.1 Definitions

**Body field.** Put λ := ε/c₀, where c₀ = (1−ε)/3. On a mixed pair with majority orientation h and odd world o, let a(h) := argmax_{j≠o} h_j (defined off the null set h_j = h_l). Define:
- F_i(h, M) = −h_i + λ[i=o]|h_o|;
- F_i(h, S) = 0;
- F_i(h, O) = h_i(1 + λ[i = a(h)]);
- F_i(h, ×) = max(F_i(h,M), F_i(h,O)) + |h_i|.

On unanimous pairs (orientation h > 0), F_i = −h_i, 0, h_i and 2h_i for M, S, O and ×.

This is X2.6's field with the attribution a(h) = argmax_{j≠o} p_jh_j frozen at its value for p = u. It is strictly guiding:
- on Q_o, a world i ≠ o has F_i(M) < F_i(S) < F_i(O) < F_i(×);
- world o has F_o(O) < F_o(S) < F_o(M) < F_o(×).

Its penalties satisfy |F_i(h, ·)| ≤ (2+λ)|h_i|. So F has integrable envelope under the Gaussian μ (CHECKED (C1) in `ff2_checks.out`, 19 968 exact random pairs, 0 violations). Put B_i(X) := ∫ F_i(h, a_X(h)) dμ.

**End charges.** For k ∈ {1,2,3} and m ≥ 1, let ψ_{k,m}(h) := h with h_k replaced by h_k/m. This is a linear isomorphism, so it preserves μ-null sets. Fix a Banach limit LIM. For bounded measurable f, put

  Λ_k(f) := LIM_{m→∞} ∫ f(ψ_{k,m}h) dμ(h).

- Λ_k is positive and linear, and is well defined on classes mod μ-null sets.
- It vanishes on every f supported in H_n := {h : |log|h_a| − log|h_b|| ≤ n for all a, b}. Indeed ψ_{k,m}^{-1}(H_n) lies in {|log|h_k| − log|h_a| − log m| ≤ n}, whose μ-mass tends to 0.
- So it is purely finitely additive and concentrated at the plane π_k := {h_k = 0}.

The sets H_n increase, and ∪_n H_n is co-null (its complement lies in the coordinate planes). A record or modification is **local** if it is supported in some H_n.

**End level and order.** Put λ_i(h, a) := F_i(h, a)/|h|, which is bounded, and

  E_i(X) := Σ_k Λ_k(λ_i(·, a_X(·))).

The term k = i vanishes for every X, because |λ_i(ψ_{i,m}h, a)| ≤ (2+λ)|h_i|/(m|ψ_{i,m}h|) → 0.

  **P_i**: X ⪯_i Y iff E_i(X) < E_i(Y), or E_i(X) = E_i(Y) and B_i(X) ≤ B_i(Y).

### 2.2 The invariant's algebra

**Proposition 2.1 (PROVED).**
- (a) E_i(Y) − E_i(X) and B_i(Y) − B_i(X) depend only on rec(X, Y), and they are additive under composition of records, including cancelled-change composites.
- (b) The set P_i of records t with (E_i(t), B_i(t)) ≥ 0 lexicographically is closed under composition. It contains ι and every i-worsening record, and no non-trivial i-improving record. So P_i is an (IB) total preorder with strict (G).

*Proof.*
- (a) The integrands are λ_i(h, Y(h)) − λ_i(h, X(h)) and F_i(h, Y(h)) − F_i(h, X(h)). Both are zero where the advice agrees, and they are potential differences of the arrow elsewhere. At each point, potential differences add along composable arrows, and opposite arrows give 0. Λ_k and ∫·dμ are linear.
- (b) The lexicographically nonnegative cone of ℝ² is closed under addition. For a worsening record t, the integrand of E_i is ≥ 0, so E_i(t) ≥ 0 by positivity. The integrand of B_i is > 0 on a non-null set, so B_i(t) > 0. Hence t is accepted, and its inverse has value <_lex 0. ∎

### 2.3 Non-additivity, blindness, and T1's protection

**Proposition 2.2 (PROVED).** Fix a world i. Then:
- no bounded strictly guiding penalty λ′ and no bounded charge ν that is positive on non-null sets satisfy ∫(λ′(X) − λ′(T1)) dν ≥ 0 for every comparison T1 ⪯_i X of P_i with X regular;
- every bounded charge ν ≥ 0 that satisfies these inequalities has countably additive density zero a.e. on the local part of T1's world-i error set.

*Proof.*
1. **The pieces.** Let j ≠ i and let l be the third world. Put W_n := {h : h_i > 0 > h_j, log(h_i/|h_j|) ∈ (n, n+1)} ∖ H_N, for a fixed N. The sets W_n are pairwise disjoint, consist of mixed pairs, and satisfy ψ_{l,m}^{-1}(W_n) ⊇ W_n ∖ ψ_{l,m}^{-1}(H_N).
2. **An accepted comparison.** Let σ_n be the record that moves T1's advice to × on W_n. It is an i-worsening, and its λ_i-increment is ≥ |h_i|/|h| on W_n. Hence E_i(σ_n) ≥ Λ_l(1_{W_n}|h_i|/|h|) > 0. Let τ be a local i-improvement out of T1 on a non-null A ⊆ H_N, which exists because T1 has non-null local i-errors. Then X_n := T1 ⊕ σ_n ⊕ τ is regular, and E_i(rec(T1, X_n)) = E_i(σ_n) > 0. So T1 ⪯_i X_n in P.
3. **No positive endorser.** An endorsement would give ν(λ′-increment of σ_n) + ν(λ′-increment of τ) ≥ 0. The second term is a fixed negative number, since λ′ is strictly guiding and ν is positive on non-null sets. The first is at most 2‖λ′‖ν(W_n), which tends to 0 because the W_n are disjoint and ν is bounded. This is a contradiction.
4. **Blindness.** For a general endorsing ν ≥ 0, the same inequality forces the ν-value of τ to be ≥ 0. Since τ is an improvement, that value is ≤ 0, so it is 0. With ν = ρμ + π, both parts of the value are ≤ 0, so ∫_A ρ·(λ′-increment) dμ = 0. As A was an arbitrary non-null local piece of T1's i-error set, ρ = 0 a.e. there. ∎

So P does not add up at any world, and its endorser field is as degenerate as possible on T1's errors. Q4.2 and L4 are satisfied vacuously. (Whether the blind-target exclusions of N1/N2 apply to this pattern is not examined here. Theorem 4.1 makes it unnecessary.)

**Proposition 2.3 (PROVED; inputs CHECKED).** No model Y ≠ T1 has rec(Y, T1) ∈ P_1 ∩ P_2 ∩ P_3. Hence, by Lemma 1.1(b), T1 is undominated and untied in **every** closure A under P.

*Proof.*
1. By X2.6, C_p is the pointwise p-Bayes model of the field with attribution argmax_{j≠o} p_jh_j. At p = u that attribution is a(h), so T1 is the pointwise u-Bayes model of F. Ties occur only on the null set ±∂D_{T1}. × is strictly worst at every world.
   - CHECKED (C2): on 19 953 exact random pairs, T1's position is the unique minimiser of u·F(h, ·) over {M, S, O}.
   - CHECKED (C3): on 39 934 exact alternatives, u·(F(h, b) − F(h, T1(h))) ≥ 0.
2. **Sum of end levels.** Since Λ_k(λ_k(·, X)) = 0 for every X and k,
   Σ_i E_i(X) = Σ_k Λ_k(Σ_i λ_i(·, X)) = 3 Σ_k Λ_k(u·λ(·, X)) ≥ 3 Σ_k Λ_k(u·λ(·, T1)) = Σ_i E_i(T1).
   The inequality holds by positivity of Λ_k and pointwise u-optimality of T1.
3. Suppose rec(Y, T1) ∈ P_i at every world. Then E_i(Y) ≤ E_i(T1) at every world, so by step 2 equality holds at every world. Then B_i(Y) ≤ B_i(T1) at every world, so ∫ u·F(Y) dμ ≤ ∫ u·F(T1) dμ. Since T1 is the a.e.-unique pointwise minimiser of u·F, Y = T1 a.e. ∎

### 2.4 The design requirements, met at the level of the invariant

| Requirement (brief) | How P meets it | Label |
|---|---|---|
| no additive cover (Thm gm) | P is lexicographic with a purely finitely additive leading level; Prop 2.2 | PROVED |
| some world fails to add up (Q4.2) | every world of P fails (Prop 2.2) | PROVED |
| degenerate (blind) endorser field (L4, Q3.25) | countably additive endorser densities vanish on T1's local error set (Prop 2.2) | PROVED |
| vetoes cannot be paid (L3.4) | E_i is not a veto: it charges silence and rewards correct advice at the planes. Its general form is Lemma 2.4, which P fails; this is why A must be minimal | PROVED |
| interior locality (AUDIT_X123) | distinct interior posterior models differ at the planes, and P compares them there: E_i(C_p) is non-constant (Cor 2.5) | PROVED |
| (IB) with cancelled-change composites, transitivity | Prop 2.1, Lemma 1.1 | PROVED |
| T1 undominated | Prop 2.3 | PROVED |

### 2.5 Why P itself cannot be the ranking

**Lemma 2.4 (PROVED).** Fix a world i and a ranking whose world-i sections {q : C_q ⪯_i X} are closed for every model X. Let Φ be a real function on models and O ⊆ Δ, such that:
- (i) Φ(C_q) < Φ(X) implies C_q ⪯_i X, for all q ∈ Δ and all X;
- (ii) for every p ∈ O there is a model X_p with Φ(X_p) = Φ(C_p) and C_p ⋠_i X_p.

Then every p ∈ O has a neighbourhood V in Δ with Φ(C_q) ≥ Φ(C_p) for all q ∈ V. If O is open and connected and q ↦ Φ(C_q) is continuous on O, then it is constant on O.

*Proof.*
- By (i), the closed section S := {q : C_q ⪯_i X_p} contains {q : Φ(C_q) < Φ(C_p)}. By (ii), p ∉ S. So p is not in the closure of that sublevel set.
- Constancy: suppose φ := Φ∘C takes values φ(a) < φ(b) on O. Join a to b by a path γ in O, and take c ∈ (φ(a), φ(b)).
- The set {t : φ(γ(t)) ≥ c} is closed and does not contain 0. Its least element t₀ is a point arbitrarily close to which φ < c ≤ φ(γ(t₀)). This contradicts the first part. ∎

**Corollary 2.5 (PROVED).** With the posterior selection, P has a world i, an interior p and a model X_p whose world-i section {q : C_q ⪯_i X_p} is not closed.

*Proof.* Take Φ := E_i and O := int Δ.
- **(i)** This is lexicographic priority.
- **(ii)** For interior p, C_p has non-null local i-errors. Correcting them on a local piece gives X_p with E_i(X_p) = E_i(C_p) and X_p ≺_i C_p, by strict (G) of P.
- **Continuity on int Δ.** For interior p, K_p ⊆ int Δ. For μ-a.e. h, the point π_kh (h with h_k set to 0) is off ±∂D_{K_p}. So the advice of C_p at ψ_{k,m}h is eventually that at π_kh, and λ_i(ψ_{k,m}h, a) converges. By dominated convergence the Banach limit is an ordinary limit, and
  E_i(C_p) = Σ_{k≠i} ∫ λ_i(π_kh, a_{C_p}(π_kh)) dμ(h)
  (λ_i at π_kh is the limit value). Dominated convergence again, using Hausdorff continuity of p ↦ K_p, gives continuity in p.
- **Not constant.** As p → e_i inside int Δ, K_p → {e_i}. Then the planar advice becomes i-correct on both planes π_j and π_l, so E_i(C_p) tends to its least possible value. As p → e_j, the advice on π_l becomes "accept iff g_j > 0". That is i-wrong on {g_i g_j < 0}, a set of positive mass, with λ_i-gap at least 2|g_i|/|g|. So the limit is strictly larger.
- Lemma 2.4 then forbids closed sections at world i. ∎

*Reading.*
- Lemma 2.4 contains the mechanism of L3.3(c)/L3.4: VB's veto Φ_i(C_p) jumps up at the vertices e_j, which violates local minimality there.
- It also excludes, for continuous selections, every design that ranks lexicographically by an end level which separates selected models. This answers the second alternative of Question Q_X2 negatively for continuous selections.
- A minimal closure A ⊆ P does not satisfy (i), because it does not refine E_i. So the lemma does not bind A. This is the reason for minimal commitment.

---

## 3. Where the closure breaks: competitiveness on bounded records

**Proposition 3.1 (PROVED; Step 1 of Theorem 4.1).** Let A ⊆ P be any closure as in §1.3. If C_p is competitive on supp p in A, then C_p is a pointwise weak Bayes model of F at some weight w ∈ Δ_{supp p}: for a.e. h and every advice a,

  Σ_{i∈supp p} w_i (F_i(h, a) − F_i(h, a_{C_p}(h))) ≥ 0.   (WB)

*Proof.* For local modifications X of C_p, E_i(rec(C_p, X)) = 0. Acceptance in A ⊆ P therefore implies B_i(X) − B_i(C_p) ≥ 0. Apply Step 1 of the proof of Theorem 4.1 with ℓ = F. ∎

**Lemma 3.2 (PROVED).** Let h_1, …, h_m be distinct mixed problems with no zero coordinate. Suppose each lies in the open cell where C_p's position and the attribution a are constant. Let b_k ≠ C_p(h_k), with δ_k := F(h_k, b_k) − F(h_k, C_p(h_k)), and suppose λ_k > 0 satisfy Σλ_kδ_k < 0 in every coordinate. Then there is a local modification X of C_p with B_i(X) < B_i(C_p) and E_i(X) = E_i(C_p) at every world. Hence X ≺_i C_p in P at every world, and C_p is competitive on no set of worlds, in P or in any A ⊆ P.

*Proof.*
- On a small ball N_k around h_k, C_p's position and a(h) are constant, so δ(h) := F(h, b_k) − F(h, C_p(h)) is linear in h and δ(h) → δ_k as h → h_k.
- Choose radii with μ(N_k) = sλ_k. This is possible because r ↦ μ(B(h_k, r)) is continuous and increasing from 0. For small s the balls are disjoint and lie in some H_n.
- Let X be C_p with advice b_k on N_k. Then B(X) − B(C_p) = Σ_k ∫_{N_k} δ dμ = s(Σλ_kδ_k + o(1)) < 0 componentwise for small s. Also E(X) = E(C_p), since the change is local. ∎

**Certificates (CHECKED, `witness.py` → `witness.out`, `witness_near_u.py` → `witness_near_u.out`).** For each p below, the scripts exhibit 2 or 3 such problems with exact rational λ_k and Σλ_kδ_k ≤ −(1,1,1). They verify:
- the cell interiority (strictly positive position margins, h_j ≠ h_l);
- the inequality.

| p | certificate |
|---|---|
| (1/2, 1/4, 1/4) | 3 terms |
| (2/5, 7/20, 1/4) | 2 terms |
| (1/5, 2/5, 2/5) | 2 terms |
| (17/50, 33/100, 33/100) | 3 terms |
| (101/300, 67/200, 197/600) | 3 terms, all S→O |
| (167/500, 333/1000, 333/1000) | 3 terms; distance to u ≈ 8·10⁻⁴ |

The search uses two kinds of problem:
- points just inside and just outside C_p's M-boundary plane (p + λp_oe_o)·h = 0, which pin any Bayes weight to the direction of p;
- the "attribution mismatch" set, where argmax_{j≠o} h_j ≠ argmax_{j≠o} p_jh_j, C_p is silent and p·F(h, O) < 0.

Certificates are searched for among triples of constraint vectors, which Helly's theorem in dimension 2 and Farkas' lemma justify up to degenerate (singular) cases. Only the certificates found are used, and each is re-verified from scratch.

An untargeted random search over triples finds none (an earlier version of `ff2_checks.py`). The certificates need problems at distance about 10⁻⁸ from C_p's acceptance boundary. At p = u no certificate can exist, by (C3).

*Consequence.* With the posterior family, the closure fails competitiveness at indices arbitrarily close to u, **whatever the choices in (D) and (K)**.

*Analytic reason.*
- Matching C_p's M-boundary on Q_o forces the weight to be p.
- At weight p, the frozen attribution makes F's Bayes model reject on the mismatch set, where C_p is silent.

Theorem 4.1 shows that no other integrable body and no other continuous selection can avoid this.

---

## 4. The obstruction

**Theorem 4.1 (PROVED, modulo the import chain stated in Step 6).** Work on the full four-advice domain with three worlds, and let T1 be the ε-contamination of u for some ε ∈ (0,1). Let ⪯_1, ⪯_2, ⪯_3 be any relations on models. Assume:
- **(H1)** a selection q ↦ C_q of coherent models, continuous in measure on Δ, with C_q competitive on supp q for every q ∈ Δ (some i ∈ supp q has C_q ⪯_i X, for every X), and T1 = C_{q₀} for some q₀ ∈ Δ;
- **(H2)** an additive field ℓ = (ℓ_1, ℓ_2, ℓ_3) with measurable penalties, each ℓ_i strictly increasing in world-i rank on every pair, with ∫ max_{i,a}|ℓ_i(h,a)| dμ < ∞;
- **(H3)** an increasing sequence of measurable sets H_n with ∪_n H_n co-null, such that for every q, every i ∈ supp q, every n and every model X equal to C_q a.e. off H_n,

  C_q ⪯_i X ⟹ ∫ (ℓ_i(h, a_X(h)) − ℓ_i(h, a_{C_q}(h))) dμ ≥ 0.

Then these assumptions are inconsistent.

*Proof.*

**Step 1 (local competitiveness gives weak Bayes; localized CC1 Thm 3.1(a)).** Fix q, let J := supp q, and fix n.
- For models X equal to C_q off H_n, put z(X) := (∫(ℓ_i(X) − ℓ_i(C_q)) dμ)_{i∈J}.
- **Convexity.** These are integrals over H_n of measurable selections from the four advice values, with integrable integrands. By Lyapunov's convexity theorem their range Z_n is convex, and 0 = z(C_q) ∈ Z_n.
- **Separation.** By (H1) and (H3), each X has some i ∈ J with z_i(X) ≥ 0. So Z_n misses the open negative orthant N of ℝ^J. Separating the convex sets Z_n and N gives w_n ≥ 0, w_n ≠ 0, with sup_N w_n·v ≤ inf_{Z_n} w_n·z. The supremum is finite only if w_n ≥ 0, and it equals 0. Normalise so that w_n ∈ Δ_J.
- **Pointwise.** Suppose that on a non-null subset of H_n some advice had Σ_{i∈J} w_{n,i}(ℓ_i(h,a) − ℓ_i(h, a_{C_q}(h))) < 0. Switching to such an advice there would give w_n·z < 0. So (WB) holds a.e. on H_n at w_n.
- **Limit.** A limit point w ∈ Δ_J of (w_n) satisfies (WB) a.e. on every H_m, since H_m ⊆ H_n for n ≥ m. Hence (WB) holds a.e.

So W(q) := {w ∈ Δ : C_q is a pointwise weak w-Bayes model of ℓ} meets Δ_{supp q} for every q. Here w ranges over all of Δ.

**Step 2 (closed graph; CC1 Lemma 3.3).**
- W(q) is closed and convex, since it is defined by linear inequalities in w.
- Let q_n → q and w_n ∈ W(q_n) with w_n → w. By continuity in measure, a subsequence has a_{C_{q_n}}(h) = a_{C_q}(h) eventually, for a.e. h. The inequalities pass to the limit, so w ∈ W(q).

**Step 3 (covering; CC1 Lemma 3.4, re-derived).** Every w* ∈ int Δ lies in W(q) for some q.
1. Suppose not. Let T := {Σx = 0}. Then O(q) := {v ∈ T : v·(w − w*) > 0 for all w ∈ W(q)} is a non-empty open convex cone for every q, by separation of w* from the compact convex W(q).
2. W is upper hemicontinuous: it has closed graph with compact range. So the graph of O is open. By Browder's selection theorem there is a continuous v : Δ → T with v(q) ∈ O(q).
3. q ↦ π_Δ(q − v(q)), with π_Δ the nearest-point projection, has a fixed point q by Brouwer. Then −v(q) lies in the normal cone of Δ at q, and v(q) ≠ 0 because 0 ∉ O(q).
4. So q ∈ ∂Δ. If q is in the relative interior of the face {q_3 = 0}, then v(q) = c(e_3 − u) with c > 0. For w₀ ∈ W(q) ∩ Δ_{supp q} (Step 1), w₀,₃ = 0, so v(q)·(w₀ − w*) = −c w*_3 < 0, contradicting v(q) ∈ O(q).
5. At a vertex e_1, v(q) = c_2(e_2 − u) + c_3(e_3 − u) with c ≥ 0, c ≠ 0, and w₀ = e_1 gives v(q)·(w₀ − w*) = −c_2w*_2 − c_3w*_3 < 0. The other faces and vertices are symmetric.

**Step 4 (property (γ); CC1 Cor 3.5).**
- For a.e. h and a ≠ b, every world ranks a and b strictly (H2). So ℓ(h,a) − ℓ(h,b) is either not proportional to 𝟙, in which case its zero set in Δ is a line, or of constant strict sign, in which case it has no zero in Δ.
- By Fubini on Ω × H, for a.e. w ∈ Ω ties are μ-null, and the w-Bayes model is a.e. unique.
- For such w, Step 3 gives q with w ∈ W(q). So that unique Bayes model is C_q, which is coherent.

This is (γ): for a.e. w ∈ Ω the w-Bayes model of ℓ is a.e. unique and coherent.

**Step 5 (T1 is Bayes at an interior weight; CC1 Lemma 4.2, re-derived).** By Step 1, T1 = C_{q₀} satisfies (WB) at some w ∈ Δ.
- **Two-world weight.** Suppose w_3 = 0 and w_1, w_2 > 0. Gambles h near (1, 1, −t) with t slightly above 2c₀/(c₀+ε) form an open set outside cl D_{T1}, on which T1 is silent. There "accept h" is strictly better at worlds 1 and 2, contradicting (WB).
- **Vertex weight.** If w = e_1, (WB) makes T1 pointwise world-1 optimal, which is false.
- By symmetry, w ∈ Ω.

**Step 6 (the field contradiction; import chain).** ℓ is a strictly guiding additive field with integral penalties and integrable envelope, (γ) holds (Step 4), and D_{T1} is ℓ-Bayes at w ∈ Ω (Step 5). On the full domain, (LF) at D_{T1} and (Av) hold trivially. Then:
- Theorem D1 gives w ∉ E(ℓ), so D_{T1} is the a.e.-unique Bayes model at w.
- BB2 Thm 6.1 (M3.9, with AUDIT_BB Lemma 2.0) gives (C2) and (C3) at w.
- M3.8, with M3.7(d), gives a contradiction.

This is exactly the chain of the proof of M3.10 (M3_notes §6) and of CC1 Thm 4.1 Steps 6–8. Its standing data are properties of the field alone (M3 §5; BB2 (H1)–(H4)), not of a ranking. Recorded status: D1 refereed once (after repairs); BB2 Thm 6.1 refereed once (CC3); M3.7 and M3.8 refereed once. ∎

**What is and is not used.**
- Used: competitiveness, continuity in measure, T1 selected, and the local endorsement (H3).
- Not used: (IB), transitivity, closed sections, (C), (LA), strict (G) of the ranking, and every comparison whose record leaves the H_n.
- Relation to earlier work. This is CC1 Thm 4.1 with its envelope required only on records supported in the H_n, and with T1 assumed selected. That replaces CC1's use of KKM, closed sections and condition (P) for ties. CC1's finitely many seeds with positive (E)-margins can be added to (H3) verbatim (CC1 Thm 3.1(a), Step 8, run inside H_n). DD2 Thm 3.3 is the analogous localization to the complement of a fixed bounded or conic region; here the region is exhausted.

**Corollary 4.2 (PROVED, same status).** Let each world order lie inside an envelope of the following form:
- first a functional E_i that vanishes on records supported in the H_n of §2.1 (purely finitely additive end charges, end vetoes, end seeds, any rule at the planes);
- then, on E_i-ties, an integrable strictly guiding additive B_i.

This includes P of §2 and every minimal-commitment closure A ⊆ P. Then no selection continuous in measure through T1 is competitive. (Local acceptance implies B_i ≥ 0, which is (H3) with ℓ = B.)

**Corollary 4.3 (PROVED, same status).** Take any relations ⪯_i with a selection satisfying (H1), and any exhausting (H_n). Then **some world i admits no penalty ℓ_i** that is strictly increasing in world-i rank, has integrable envelope, and satisfies

  C_q ⪯_i X ⟹ ∫(ℓ_i(X) − ℓ_i(C_q)) dμ ≥ 0, for every q with i ∈ supp q and every X equal to C_q off some H_n.

*Proof.* If each world had such an ℓ_i, then (ℓ_1, ℓ_2, ℓ_3) would satisfy (H2) and (H3). ∎

*Reading.*
- In every cover of T1 with a selection continuous in measure, some world's accepted comparisons out of selected models, already among those confined to bounded log-ratio regions away from the coordinate planes, are endorsed by no integrable strictly guiding penalty.
- Q4.2 constrains endorsers of all relevant comparisons and needs (IB), closed sections and (NC). Corollary 4.3 constrains bounded-support comparisons, and needs only competitiveness and continuity.
- **What escapes Theorem 4.1:**
  - a selection not continuous in measure (only Step 2 uses continuity; compare V1's jump);
  - a body that is not integrable, such as the Haar-weighted levels of X2.7. These are excluded at the vertices by X2.9 when invariant, but not otherwise;
  - a world that is non-additive on bounded records, for example AUDIT_AA's lexicographic cone with a countably additive, weakly guiding leading level, or a local (M1)/(M2) structure.

---

## 5. Status, open point, files

| Item | Statement | Label |
|---|---|---|
| 1.1 | record-level invariants pass to every closure, cancelled-change composites included; inheritance of (G), (IB), transitivity, protection | PROVED |
| 2.1 | end-priority P_i is an (IB) total preorder with strict (G) | PROVED |
| 2.2 | P has no bounded positive endorser at any world; endorser densities vanish on T1's local error set | PROVED |
| 2.3 | T1 strictly protected in P, hence undominated and untied in every closure | PROVED; inputs CHECKED (C1)–(C3) |
| 2.4 | leading-level rigidity: local minimality, constancy where continuous | PROVED |
| 2.5 | P with the posterior family has a non-closed section | PROVED |
| 3.1 | competitiveness in any closure forces weak Bayes for the body | PROVED |
| 3.2 | finite Gordan witness gives a local all-world strict improvement | PROVED |
| §3 table | posterior C_p is F-Bayes at no weight, six indices, nearest ≈ 8·10⁻⁴ from u | CHECKED |
| 4.1 | locally endorsed competitive continuous selections through T1 do not exist | PROVED modulo D1, BB2 Thm 6.1 (+ AUDIT_BB Lemma 2.0), M3.7–M3.8 (each refereed once) |
| 4.2, 4.3 | end-priority envelopes excluded; some world locally non-additive in every continuous cover | PROVED, same status |
| — | T1 cover | **not obtained**; the class tried fails competitiveness |

**Most important open point.** Does Theorem 4.1 hold for selections that are not continuous in measure? Only Step 2 (closed graph) uses continuity.
- If it holds, every cover of T1 needs a world that is non-additive on bounded-support comparisons out of selected models.
- If it fails, the failure must come from jumps of the selection, which Lemma 2.4 then constrains: any leading level must be lower semicontinuous with local minima along the selection.

**Files (`ff2py/`).**
- `ff2_checks.py` → `ff2_checks.out`:
  - (C1) strict guidance of F;
  - (C2) T1 is the unique pointwise u-Bayes model of F;
  - (C3) no Gordan witness at u;
  - (C5) an unbounded stake ratio of F on Q_o, recorded for reference and not used.
- `witness.py` → `witness.out`: exact certificates at p = (1/2,1/4,1/4), (2/5,7/20,1/4), (1/5,2/5,2/5). With its untargeted mismatch points and offsets 10⁻⁴ it finds none at (17/50,33/100,33/100), at (101/300,67/200,197/600), or at u (where none can exist, by (C3)). The first two are handled by the next script.
- `witness_near_u.py` → `witness_near_u.out`: exact certificates at the three indices near u, with targeted mismatch points and offsets 10⁻⁸.
