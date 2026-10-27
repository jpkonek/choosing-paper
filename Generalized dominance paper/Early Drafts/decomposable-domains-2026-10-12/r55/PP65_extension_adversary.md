# PP65. Adversary for round 55: what the first nontrivial extension forces, where reservations can exhaust, and attacks on PP64

23 October 2026. Adversary task of Brief 55. One author; not refereed. Takes in the coordinator's relay of PP66 (two-neighbourhood diagnostic, Lemma T) and the sharper test it suggests.

**Labels.** PROVED: complete argument here, or a cited result used within its stated hypotheses. CHECKED: exact SAT/closure computation in `r9/PP65_py/` (every script ends ALL PASS). NUMERICS: none. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF55 and its binding audits (AUDIT_round55_direction, AUDIT_round55_answers); LEAD_selection_count; AUDIT_completion; BRIEF54 encodings; DESIGN_MEMO §8.23; PP62 (Thms R, P, E, Cor E.2, Lemma S); PP63 (Lemma 3.1, Lemma 4.1, Thm J, Prop 2.1, Prop 4.6); PP57 §4 (Thm Q); PP30 Thm 3.1; PP36 Prop K and Lemma E; PP29 Lemma 3.3; PP59; PP66 (Lemma T). No axiom is added. Extra hypotheses are named where they enter: (MC) in §3.3, (DR) in §5.

**PP64 status.** §4 is written against PP64 §1 (DRAFT definitions, file time 20:17); see §4 for any later additions read.

---

## 0. Verdict

1. **The first nontrivial extension is consistent, and its forced shape is determined (§2; PROVED, CHECKED).** For every non-null non-conic E inside T's silence where worlds i, j agree (class M_k), with X_E := T[E ↦ A]:
   - every model at an index of the edge [e_i, e_j] is D_K with K in that edge and equals X_E on E (PP29 Lemma 3.3), so **rec(C_p, X_E) = rec(C_p[E ↦ S], T)**: the edge defender's defence against X_E is the same record as a protection record of T (Lemma 2.1);
   - T's refusals are **uniform in E** on a large set: wherever T defends against a selected model at i, that model refuses every X_E at i (Prop 2.2);
   - on the edge there is always a defender p(E) accepting X_E at i **and** j; at every such index the axioms force C ⋠_k X_E, T ⋠_i C, T ⋠_j C, T ⪯_k C, and for every E ⊊ E′ the further literals of Prop 2.3 (CHECKED by SAT, `ext65.out`);
   - X_E's coherent dominator (it exists by KKM) is a **genuinely new model at a new index**: not T, not on [e_i, e_j], not where T defends at i or j, not answering A on all of E (Prop 2.4).
2. **The switch of defending world is always possible for each E; the reservation at T forces a "germ condition" on the models selected near T (Prop 2.6).** An explicit coherent model, D over the k-minimal edge of M, can never be selected on T's fibre's neighbourhood or wherever T defends at both i and j.
3. **Exhaustion (§3; PROVED).** Finitely many commitments never exhaust a face (Prop 3.1). Exhaustion can occur only at accumulation points of distinct committed models, and those are unavoidable on every edge (Prop 3.2). Under measure-continuity of the selection, guidance never causes it (Prop 3.3): **any exhaustion must come from non-guidance refusals ((TC) kills or committed choices)**. The brief's formalism omits one obligation that a correct invariant must carry: limit points of committed acceptances are forced acceptances at unassigned indices (§3.4).
4. **Robust (ball) refusals at two worlds exhaust (§5; PROVED, CHECKED).** Answering the coordinator: if inverse-closed d-open refusal sets at two different worlds share a member-swap record that has a strictly improving part at the third world, one member is undefended (Prop 5.1, `balls65.out`). So PP66's ball surgeries at different worlds must never overlap on such records, and along any d-continuous family of member swaps all robust refusals sit at **one** world (Cor 5.2). Source-space reservations alone do **not** transmit PP66's Lemma T, so this is a constraint on the ball architecture, not on the axioms.
5. **PP64 final (§4; PROVED, CHECKED).**
   - **Lemma 2.2 and Theorem 2.3 are correct**, including global (C) through KKM and (I4) = (C⁺), once D = Δ (§4.1).
   - **Conjecture 3.4 is false whenever its own stage-0 tameness holds** (Prop 4.1):
     - assign the precise edge model D′ = D_{(½,½,0)} at p = (½,½,0) by Prop 3.1;
     - commit T ⪯₁ D′ and T ⪯₂ D′, each legal by PP64's Prop 3.3(i) (D′ is mixed against T at every world, `edge65.out`, so rule III does not fire);
     - by (TC), D′'s defence against X_E is then dead at both edge worlds, and no revision helps.

     So **Theorem 3.5 is vacuous as stated.** The two acceptances are jointly forbidden by the axioms (Prop 2.2(b)), but H\* only sees committed refusals.
   - **(M2) is reachable by legal steps** (Prop 4.2). Three sequences of single-world acceptances accumulating at a carrier, or at three different (IB) carriers of one record, make a swap record unsettleable. This is the coordinator's sharper test (swap chosen after Σ). The conjecture holds at most as a statement about a *policy*, which must then be part of the invariant.
   - **"Each index revised finitely often" allows only countably many co-design revisions in the whole construction** (Prop 4.3), and none once D is dense.
   - **H\* is checkable and non-circular, but insufficient.** Making it sufficient by "TC-liveness for all rivals" is circular. The non-circular repair is a classified list of model-level (TC) kill patterns, with Prop 2.2 as the first entry (OPEN whether such a list can be finite).
   - PP64 is **not** caught by Theorems Q and E, since it has no endorsement.
6. **Negative route (§6).** No axiom-level conflict found. What one would have to look like is stated in §6; no architecture exclusion here is offered as progress toward it.

---

## 1. Setting and conventions

BRIEF55's setting: three worlds; Gaussian μ; four-advice domain modulo null sets; ranks correct 0 < S 1 < wrong 2 < contradictory 3; T = D_M, M = c·1 + εΔ. Coherent models are D_K (K ⊆ Δ compact convex). Axioms: reflexivity, strict (G), (IB), (TC) in implication form, (S) on the closed simplex, (LA), direct (C).

**Classes.** For mixed g, the odd world o(g) is the one whose sign differs; M_k is the class o = k. On M_k the majority answer A is correct at i and j and wrong at k; the minority answer B is correct only at k. Put **Q_k := Sil(T) ∩ M_k**, a non-null open cone.

**The default instance (brief).** E ⊆ Q_k bounded, non-null, non-conic; X_E := T[E ↦ A]. By strict (G), X_E ≺_i T, X_E ≺_j T and T ≺_k X_E. X_E is incoherent (Lemma H).

**Notation.** A_w(X) := {p : C_p ⪯_w X} (closed by (S)); R_w(X) := Δ ∖ A_w(X) (open). W_E := R_i(X_E) ∩ R_j(X_E). P_w := {p : T ⪯_w C_p}. "Y ⊵_w Z": Y is pointwise no worse than Z at w; with Y ≠ Z this gives Y ≺_w Z.

**Imported facts.** LEAD Lemma A (tie fibres closed), Lemma B (C_{e_i} = V_i), Lemma E; PP29 Lemma 3.3(2) (edge models); PP36 Lemma E(ii) (exposure of fills); PP63 Lemma 4.1 (refusals spread); PP66 Lemma T. All are derived from the axioms alone (PP59 entries 1, 2-second half, 5-inner step, 16, 18).

---

## 2. The first nontrivial extension: what is forced

### 2.1 The edge defender and its records

**Lemma 2.1 (PROVED).** Let p lie on the closed edge [e_i, e_j]. Then C_p = A a.e. on M_k (PP29 Lemma 3.3(2); for vertices, Lemma B), hence C_p = X_E on E and

  rec(C_p, X_E) = rec(C_p[E ↦ S], T),  rec(X_E, C_p) = rec(T, C_p[E ↦ S]).

*Proof.* Off E, X_E = T; on E both sides equal A. So the support of rec(C_p, X_E) is {C_p ≠ T} ∖ E, with old side C_p and new side T there. The same holds for rec(C_p[E ↦ S], T), since both sides are S on E. ∎

So **the edge defender's defence against X_E and T's protection against the incoherent model C_p[E ↦ S] are one record.** Direct (C) for T gives: for every non-conic E, some world w has C_p ⋠_w X_E. (This is PP36 Lemma E(ii) seen from the edge.)

### 2.2 T's refusals are uniform in E on P_i

**Proposition 2.2 (PROVED; (TC) and strict (G)).** For every strict i-improvement Z of T (in particular every X_E, E ⊆ Q_k or E ⊆ Q_j), R_i(Z) ⊇ P_i. Hence for all such E:
- (a) W_E ⊇ P_i ∩ P_j ⊇ Φ_T (T's all-world tie fibre);
- (b) P_i ∩ P_j ∩ [e_i, e_j] = ∅, and every edge index in P_i accepts every X_E at j.

*Proof.* T ⪯_i C_p, C_p ⪯_i Z and Z ⪯_i T (guidance) form an accepted triangle; (TC) would demand T ⪯_i Z, which strict (G) refuses. (b): an edge index must accept X_E at i or j. ∎

This is PP19 Thm 1 in general form, but the uniformity matters: **T's reservation for X_E is not just a neighbourhood of u. It contains the whole set where T is chosen to defend at i, for every E at once.** Choosing T's defence world against a new selected model is therefore never local bookkeeping.

### 2.3 The forced verdict pattern at the edge

**Proposition 2.3 (PROVED).** Fix E′ (non-null, non-conic, ⊆ Q_k).
- (a) (1-D KKM.) There is p = p(E′) ∈ [e_i, e_j] with C_p ⪯_i X_{E′} and C_p ⪯_j X_{E′}.
- (b) At every such p: C_p ⋠_k X_{E′}; T ⋠_i C_p and T ⋠_j C_p; T ⪯_k C_p.
- (c) For every E ⊆ E′ with E′ ∖ E non-null: X_E ⋠_i C_p and X_E ⋠_j C_p, and X_E ⪯_k C_p, i.e. **T ⪯_k C_p[E ↦ S]** while T ⋠_i, ⋠_j C_p[E ↦ S].
- (d) For every E″ ⊆ E′ such that E′ ∖ E″ is non-null (or E″ = E′): C_p ⋠_k X_{E″}. In particular C_p ⋠_k T.

*Proof.* (a) A_i(X_{E′}) and A_j(X_{E′}) are closed, cover the edge (competitiveness on supp p), and contain e_i and e_j respectively (V_i is i-perfect). The edge is connected.
(b) The first claim: C_p ⪯_w X_{E′} at all three worlds would be, by Lemma 2.1, an all-world acceptance of the incoherent C_p[E′ ↦ S] against T, against direct (C). The second: Prop 2.2's triangle. The third: T's defence.
(c) C_p ⪯_i X_{E′}, X_{E′} ⪯_i X_E (guidance: X_{E′} is i-better on E′ ∖ E) and X_E ⪯_i C_p would make (TC) demand X_E ⪯_i X_{E′}, which strict (G) refuses. Same at j. Then T's defence against C_p[E ↦ S] must be at k. By Lemma 2.1 (applied to E, using that C_p = A on E), rec(T, C_p[E ↦ S]) = rec(X_E, C_p).
(d) Choose E with E″ ⊊ E ⊊ E′, both differences non-null (μ is atomless). Then X_E ⪯_k C_p by (c), X_{E″} ⪯_k X_E by guidance (less k-wrong advice), and C_p ⪯_k X_{E″} would make (TC) demand X_E ⪯_k X_{E″}, refused by strict (G). For E″ = E′ use (b). ∎

**CHECKED (`ext65.py` → `ext65.out`, ALL PASS).** Abstract instance: three nested atoms P1, P2, P3 of Q_k, one M_i cell and two M_j cells, chosen so that Cp is pointwise better than T at neither i nor j. All 64 T/Cp splices; (TC) on all ordered triples at all worlds; defence, direct (C) and undominatedness for T and Cp. With hypothesis (a) at E′ = P1∪P2∪P3, every literal of (b)–(d) is forced (UNSAT of its negation). A control shows that none of them is forced without (a). The atom-level instance also shows that (d) genuinely needs an intermediate E: with E″ = P1∪P2 (no intermediate atom) the refusal is not forced.

**Reading.** The edge defender that serves X_{E′} at both i and j is pinned: it must be strictly worse than T at k against the whole lattice below E′, and T must defend against it, and against all its partial silencings, at k alone. This is the joint choice of defender and index the brief asks for. Its reservations are the open sets around p(E′) for the refusals in (b)–(d).

### 2.4 The new coherent dominator of X_E

**Proposition 2.4 (PROVED).** D(E) := ∩_w A_w(X_E) is non-empty and closed (KKM, as in AUDIT_completion §5). Every p ∈ D(E) satisfies:
- C_p strictly dominates X_E (direct (C));
- p ∉ W_E ∪ P_i ∪ P_j ∪ [e_i, e_j], and C_p ≠ T;
- C_p ≠ A on a non-null part of E (PP36 Lemma E(ii));
- T ⋠_i C_p, T ⋠_j C_p and T ⪯_k C_p.

*Proof.* p ∉ P_i ∪ P_j by Prop 2.2. Edge indices answer A on E (Lemma 2.1), so an all-world acceptance there contradicts direct (C) for T; the same argument proves the third item for every index. The last item is Prop 2.2's triangle plus T's defence. ∎

So the brief's "new coherent defender" comes in two forced pieces: an edge defender pinned by Prop 2.3, and an interior dominator that must avoid T's whole defence region at i and j and must give up some of the free i, j-correct answers on E. Both are outputs; nothing about their family is imposed.

### 2.5 The switch, for every E

∂W_E ⊆ A_k(X_E) ∩ (A_i ∪ A_j)(X_E): boundary points of the open set W_E lie in its closure, which is inside A_k, and outside W_E. Since W_E ⊇ Φ_T and misses [e_i, e_j], **∂W_E separates T's tie fibre from the edge, and the defending world switches on it.** Along [u, e_k] no switch is needed (V_k ⪯_k X_E by guidance). Along [u, e_i] the switch is from k to i.

For a single E this is pure topology, and it is always realisable. Nested and overlapping E's interact only through Props 2.2–2.3 and (TC) (e.g. C ⪯_i X_E ⇒ X_{E″} ⋠_i C for E″ ⊊ E). The **uniform** content across all E is Prop 2.2.

### 2.6 What the reservation at T forces on indices that are not yet assigned

**Proposition 2.6 (near-T exclusion; PROVED).** Let C_p ⋠_i X_E and C_p ⋠_j X_E with p interior (e.g. p ∈ P_i ∩ P_j, or p ∈ Φ_T). Let q_n → p.
- (a) Pointwise: C_p is not of the form [C = A a.e. on E, and C ⊴_k T off E].
- (b) Germ form: it is impossible that infinitely many C_{q_n} are of that form for one common E.
- (c) **Explicit excluded model.** K₀ := conv{c1 + εe_i, c1 + εe_j} (the k-minimal edge of M). D_{K₀} is a tightening of T whose new answers are all k-wrong, and it answers A on a non-null part of Q_k. It is never selected on P_i ∩ P_j, and its fibre is at positive distance from Φ_T.

*Proof.* If C has that form and C ≠ X_E, then X_E ⊵_k C, so C ⋠_k X_E by strict (G). (a): with the i and j refusals, C_p is undefended. (b): by openness, C_{q_n} refuses X_E at i and j for large n, and q_n is interior. (c) K₀ ⊆ M, so D_{K₀} answers wherever T does, with the same answer. At a new answer g, K₀·g > 0 (say) but (c1 + εe_k)·g < 0, so cΣg + εg_k < 0 < cΣg + ε min(g_i, g_j) (positivity on the segment K₀ is positivity at both ends). If g_k ≥ 0, the first inequality gives Σg < 0; the second then gives g_i, g_j > −cΣg/ε > 0, so Σg > g_k ≥ 0, a contradiction. So g_k < 0 and the answer + is k-wrong. Example of a new A-answer in Q_k (k = 3): g = (1, 1, −3/2) at ε = 3/10. Apply (a) with E inside that cone. For the fibre, apply (b) to the constant sequence. ∎

**Reading.** As q → Φ_T, the selected models must lose every fixed "k-worse with free A" region. Posterior models along a∘(1 − te_k) do this: their k-worsening layer shrinks to null. A locally finite or jumping selection near T does not. This is checkable for any explicit proposal.

---

## 3. Can reservations exhaust coherent defenders or defending worlds?

**Exhaustion** at an index q for a rival X means that every world of supp q is refused at q (reserved, or forced at whatever model is put there).

**Proposition 3.1 (finitely many commitments never exhaust; PROVED).** Let finitely many committed models C_{p_1}, …, C_{p_m}, at distinct indices, each satisfy their own obligations. Choose pairwise disjoint balls B_l ∋ p_l, and take every reservation of p_l (for every rival and world) inside B_l. On B_l the assignment C_q := C_{p_l} meets every reservation of p_l, defends on supp q ⊇ supp p_l, and introduces no new record (it is the same model).

So exhaustion is never a finite phenomenon; it lives at **accumulation points of distinct committed models**, where a reservation centred at p* must contain committed C_{p_n} → p*.

**Proposition 3.2 (accumulation is unavoidable on every edge; PROVED).** On each closed edge the selection takes infinitely many values, and uncountably many if no two are all-world tied.

*Proof.* LEAD Thm C's argument restricted to the edge: Lemma A's fibres meet the edge in closed sets, V_i and V_j lie in different tie components (Lemma B), and the edge is connected (Sierpiński for (ii)). ∎

Every edge therefore contains accumulation points of distinct defenders, at which the reservations of the limit model are forced onto the nearby ones.

**Hypothesis (MC).** The selection is continuous in measure along the sequences considered: q_n → p ⇒ μ(C_{q_n} ≠ C_p) → 0. This is not implied by (S). It holds for posterior families, precise edge models, and PP62–PP66's constructions.

**Proposition 3.3 (guidance never exhausts under (MC); PROVED).** Let q_n → p and X a rival, and suppose every world of supp q_n is refused at C_{q_n} for infinitely many n. Then for infinitely many n some refused world v at q_n is one where **C_p accepts X** and the refusal at q_n is **not** forced by strict (G) at q_n.

*Proof.* C_p defends: some v ∈ supp p ⊆ supp q_n has C_p ⪯_v X. Suppose, for infinitely many n, the refusal at v at q_n is a strict-(G) refusal: X ⊵_v C_{q_n}, X ≠ C_{q_n}. Along an a.e.-convergent subsequence (MC), X ⊵_v C_p. If X ≠ C_p, then X ≺_v C_p and C_p ⋠_v X, a contradiction. If X = C_p, then C_p ⊵_v C_{q_n} at every refused world, all of supp q_n, strictly at one. So C_{q_n} is strictly dominated (supp q_n = all worlds near interior p), or uncompetitive against C_p. Either way the axioms already fail at q_n. ∎

**Consequence.** With (MC), an exhaustion has to be built from **non-guidance** refusals at nearby committed models: (TC) kills (PP30 Thm 3.1, Prop K, Prop 2.2–2.3 here), direct-(C) world choices (balanced swaps), committed choices of disjunctions, or reservation radii committed around other centres (also a choice). This is exactly where PP63 §4.7 located any possible obstruction ("defence-tight records"). The reservation formalism adds no new source of exhaustion. It makes the existing one explicit.

### 3.4 An obligation the brief's formalism does not list

In a partial system the refusal sets are open by construction, but the acceptance sets need not yet be closed. **Every limit point p of committed acceptances (q_n, X, w) is a forced acceptance C_p ⪯_w X at p, whether or not p is assigned.** No reservation for (X, w) can ever be committed at p.

The brief's formalism records reservations for refusals and disjunctive obligations, but not these **forced acceptances at unassigned limit points**. They do two things:
- they restrict which coherent models can later be put at p (no model with X ≺_w C_p);
- through (TC) they delete options from other pending disjunctions. Example: if the committed edge defenders C_{q_n} → p accept Y at i, where Y ≺_i T, then by Prop 2.2's triangle T's defence against whatever is put at p can no longer be at i.

**A correct invariant must therefore carry the closure of committed acceptances as commitments.** This is checkable, but it is a closure over the committed set, which in a transfinite construction is uncountable.

A second omission concerns (IB) inheritance at new assignments. Suppose a record r has been committed as refused at w. When a model C_q matching r's old side is later assigned at q, the comparison C_q ⋠_w C_q ⊕ r is already decided, so it needs a reservation around q. Every already-committed C_{q_n} → q must then refuse C_q ⊕ r at w. The assignment step must check this against all committed refused records that C_q matches.

---

## 4. Attacks on PP64

**Read.** PP64 final, 43,831 bytes, 20:26: §1 definitions, §2 limits and the final system, §3 extension lemma (H\*, Props 3.1–3.3, Conj 3.4, Thm 3.5, Lemma 3.7), §4 first extension, §5 balanced swap, §6–7. An earlier draft of this section attacked the 20:17 draft of §1. Its points about continuity and (L) are revised in §4.4 to match PP64's [R] change: Ĉ is no longer required to be continuous.

**Summary.**
- **Lemma 2.2 and Theorem 2.3 are correct** (§4.1).
- **Conjecture 3.4 is false whenever its own stage-0 hypothesis holds** (§4.2, PROVED). Two legal acceptance steps inside PP64's own first-extension setting produce a tame Σ with a carried record that cannot be settled, with or without revisions. So Theorem 3.5 is vacuous as stated.
- **(M2) is reachable by legal steps** (§4.3), also across different (IB) carriers of one record.
- **"Each index revised finitely often" allows only countably many co-design revisions in the whole construction** (§4.4).
- **H\*** is checkable and not circular, but it is not sufficient. The repairs are listed in §4.6.

### 4.1 Lemma 2.2 and Theorem 2.3: correct (checked line by line)

- **Lemma 2.1.** Every clause except (I7) is witnessed by at most six acceptances, three reservations, or one reservation with one assignment. These all lie in one stage of a chain. (I7) has permanent witnesses. ✓
- **Lemma 2.2.**
  - Every record needed for (G) is decided before completion: (I1) commits **all** weak-guidance acceptances and strict-guidance refusals globally, including those of carrier-free records. ✓
  - The completion adds only refusals. Every accepted triangle already has its inverses in Acc by (I2), and every all-world acceptance into a registered model already has its reverses by (I3), so neither is disturbed.
  - (I4)/(C⁺) is unaffected, since ties consist of acceptances.
  - (I6)–(I8) concern carried records and Rz, which are unchanged. ✓
- **Theorem 2.3.**
  - With totality and (I6)–(I7), p ∈ A_w(N) ⇔ p ∉ O_w(N), so A_w(N) = F_w(N) is closed.
  - Competitiveness is (I8) together with (I7) and totality.
  - KKM on the closed simplex gives p with C_p ⪯_w N at every world. If N is undominated, the reverses hold, so N ≈ C_p ∈ P and (I4) registers N. Then X ≈ N gives X ∈ P, which is coherent by (I5) and undominated by (I3). ✓
  - This uses D = Δ. It is consistent with REFEREE_round54 §4: global (C) fails for partial unions, and PP64 discharges it only for a full selection, with (I3)–(I5) = (C⁺) at every stage.
  - **One wording fix.** The theorem needs Σ̄ total **and** D = Δ, not just total. Lemma 2.2 supplies both.

### 4.2 Conjecture 3.4 is false given its own stage-0 hypothesis (PROVED; CHECKED)

**Proposition 4.1.** Start from PP64's stage-0 system Σ₀ (T at u, (I1), reservations for T's guidance refusals), tame along Ĉ. Use Prop 3.1 to assign C_p := Ĉ_p = D′ at a point p of the open edge {1, 2}, where D′ is mixed against T at worlds 1, 2 and 3. Then commit, by two steps of type (b)/(d):

  rec(T, D′) ∈ Acc₁,  rec(T, D′) ∈ Acc₂.

Then:
- (a) each step satisfies PP64 Prop 3.3(i), so the result is tame along Ĉ;
- (b) for every non-null non-conic E ⊆ Q₃, the carried records (rec(D′, X_E), 1) and (rec(D′, X_E), 2) cannot both be settled. Either the first settlement already fails, or after it the second fails;
- (c) no revision of Ĉ helps, since every model involved is assigned.

So Conjecture 3.4 fails in a tame system. Every face-admissible Ĉ has an open-edge {1, 2} model (it is A on M₃: PP29 Lemma 3.3). Prop 3.1 assigns it for free. The precise edge model D′ = D_{(½,½,0)} is mixed against T at all three worlds (CHECKED, `edge65.out`, exact witnesses on open cones).

**Hence stage-0 tameness together with Conjecture 3.4 is contradictory, and Theorem 3.5 as stated is vacuous.**

*Proof.*
- **(a), condition r ∉ 𝓡_w.** rec(T, D′) is mixed at 1 and 2, so it is not guidance-refused. No reservation (U, D′, w) centred at u exists, since rec(T, D′) is not refused. If a guidance reservation for the rival D′ centred at some q ≠ u happens to contain u, shrink it. In Σ₀ only u is assigned, so shrinking reservation radii (keeping the centres) preserves (I6)–(I8) and (H1)–(H4): (H3) only needs some reservation at each carrier, and the other clauses only get weaker. Since Conjecture 3.4 quantifies over all tame Σ, one tame Σ₀ suffices.
- **(a), (H4)-cleanliness at world w ∈ {1, 2}.**
  - Any accepted triangle containing a copy of rec(T, D′) together with two guidance links would make that copy a weak w-improvement. It is not one, being mixed (PP21 Lemma 2.1, as in PP64 Thm 4.3).
  - The only non-guidance acceptances are the two copies of rec(T, D′). Two copies cannot be consecutive in a triangle, because a carrier of rec(T, D′) equals T on D(T, D′) and the next node equals D′ there.
  - Rule III for N = D′ needs rec(T, D′) ∈ Acc₃. That is not guidance, because D′ is 3-better than T somewhere (`edge65.out`), and it is not committed. So rule III does not fire.
  - This is where PP64's own D, which is weakly 3-worse, differs. For that D, rule III would fire and the second acceptance would be rejected.
- **(b).** Settling (rec(D′, X_E), w) as A, for w ∈ {1, 2}, closes the triangle D′ → X_E → T → D′ at w:
  - X_E ⪯_w T is guidance;
  - T ⪯_w D′ is committed;
  - so (I2) puts rec(T, X_E) in Acc_w, but it is in Ref_w by strict (G).
- So both settlements must be R. Each needs a spread system. After both, Rz_p(X_E) ⊇ {1, 2} = supp p, which violates (H2)/(I8). ∎

The two commitments are jointly impossible by the axioms (Prop 2.2(b): P₁ ∩ P₂ never meets the edge), yet H\* and Prop 3.3(i) accept them. The abstract SAT instance confirms the mechanism (`ext65.out`): T ⪯₁ Cp alone is SAT, T ⪯₂ Cp alone is SAT, and both together are UNSAT.

**What this is in PP64's taxonomy.** It is (M4), but it is not cured by co-design or carrier-freeness. It is caused by an **acceptance** step, and (H2) counts committed refusals only. A (TC) kill is a refusal that every completion contains but no committed set records. PP30 Thm 3.1, Prop K and Prop 2.2 here are all of this kind.

### 4.3 (M2) is reachable by legal steps (PROVED)

**Proposition 4.2.**
- **Setting.** Let a and b be assigned interior members and F ⊆ {C_a ≠ C_b} non-null and non-conic, mixed at every world (a balanced swap is one example; PP62 Cor 1.2). Put X := C_a[F ↦ C_b], Y := C_b[F ↦ C_a] and r := rec(C_a, X) = rec(Y, C_b).
- **The steps.** Assign by Prop 3.1 three sequences q^l_n → a (l = 1, 2, 3) of Ĉ-models, at positive distance from F's layers. Settle rec(C_{q^l_n}, X) ∈ Acc_l by Prop 3.3(i). Each record is (σ : C_q → C_a) ⊕ r, mixed at l. Only one world is committed per record, so rule III never fires.
- **The conclusion.** If each step is closure-clean (it is when no other acceptances interfere), the union is tame (PP64 Prop 3.2), and r cannot be settled at all three worlds:
  - a refusal of r at l needs a spread system with a reservation at the carrier a for (X, l), and (H1) fails at q^l_n inside it;
  - accepting r at all three worlds lets rule III for C_b make Y ≈ C_b, and rule IV then registers the incoherent Y: F2.

  Every model involved is assigned, so no revision helps. ∎

**Across carriers.**
- Replace a by three distinct assigned interior carriers a₁, a₂, a₃ of r (C_{a_l} = C_a on F), with X_l := C_{a_l}[F ↦ C_b], and let only the sequence at a_l accept X_l at world l.
- Then for every fixed (rival, world) the accepted indices accumulate at **one** carrier only, yet r is blocked at every world.
- **So a repair must record limit acceptances at record level**, letting (IB) carry them to all carriers.

**The missing invariant.** (I9) *Limit acceptances at record level.* For every rival X, world w and index p ∈ cl(D ∩ {q : rec(C_q, X) ∈ Acc_w}), enter rec(Ĉ_p, X) in Acc_w **as a record**, so that (IB), (I2)–(I4) and the F1/F2 test act on it at every carrier. Reject a step if this conflicts.
- With (I9), the third sequence in Prop 4.2 is rejected at commit time.
- (I9) is not finitely refutable: its witness is a sequence. Its closure is the non-finitary least fixed point that AUDIT_completion §6 flags.
- It depends on Ĉ_p at unassigned p, so revisions of Ĉ must respect it.

**Reply to PP64 §5 and to the coordinator's item 2.** PP64 says (M2) "arises only if earlier settlements chose acceptance at all worlds" and that Conjecture 3.4 asserts such choices can be avoided. But Conjecture 3.4 is stated for **every** tame Σ, including those produced by such choices. So the conjecture is false as stated. What remains plausible is a **policy** statement:

> There is a settling rule under which (I9) and the kill patterns are never violated.

A policy must then be part of the invariant.

**Can (M2) be avoided?** Not by tameness. It can be avoided by an invariant that records, for each record r and world w, the **limit acceptances** at carriers. This is (I9) above. With it, the acceptance step at the third sequence is rejected at commit time through rule III/IV, and the step must use another world there.

With the swap chosen after Σ (the coordinator's sharper test), the step absorbs it without revising commitments iff, for some world w, no carrier of r is a limit of committed w-acceptances of its copy rival. That is a checkable condition on the committed set, but nothing in PP64's operation maintains it.

### 4.4 Revisions: countably many at most (PROVED)

**Proposition 4.3.** Suppose each revision of Ĉ changes its value on a set with non-empty interior (as when a provisional value is replaced on an open set), and each index is revised only finitely often. Then the construction performs only **countably many** revisions.

*Proof.* Each revision set contains a ball from a countable base of Δ. If uncountably many revision sets existed, one base ball would lie in infinitely many of them, and each of its points would be revised infinitely often. ∎

**Consequences for Theorem 3.5.**
- The construction has length continuum, with continuum many settlements. So all but countably many settlements must succeed **without** co-design.
- Revisions are allowed only on open sets of **unassigned** indices. Once D is dense, no further revision is possible at all. An enumeration can postpone that moment but cannot avoid it.
- So co-design in Conjecture 3.4 is a countable resource, spent early. By PP61 Thm C, countably many choices are exactly the regime in which nothing is obstructed.

**Continuity.** PP64 dropped continuity of Ĉ, so Prop 3.2 is now correct. Continuity is genuinely not preserved under unions:
- *Example.* An unassigned p\* with assigned q_n → p\* whose committed models alternate between two coherent models at measure-distance δ₀ > 0, each Ĉ^(n) continuous and revised only on a small ball around q_n.

Consequences:
- Lemma 3.7, the only tool for stage-0 slack, needs continuity, so it cannot be reapplied after a limit stage.
- PP64's own exclusion of the second alternative of (M2) ("Ĉ_{q′} weakly w-better than the rival") also needs continuity, and so is unavailable after limit stages.

### 4.5 Smaller points

1. **Lemma 4.1(b) / Theorem 4.3: refusals at unassigned Ĉ-carriers.** Lemma 4.1(b) forces Z ⋠₁ D for **every** Z strictly 1-worse than X_E. Along the posterior Ĉ, the members Ĉ_{q′} with q′ = u∘(1 − t e₁) are such Z: they are weakly 1-worse than T, and silent on E where X_E is 1-correct. So rec(Ĉ_{q′}, D) ∈ Ref₁ at Ĉ-carriers near u. (H3) then needs reservations around those q′, which Σ₁ does not list. Theorem 4.3 proves 𝓘, but **tameness of Σ₁ is not shown**. Defence slack at those q′ looks available at worlds 2 and 3, but this is unchecked.
2. **Prop 5.1(v): "generically carrier-free".** Carrier-freeness in Prop 3.3(iii) is relative to Ĉ on **all of Δ**, not just the posterior family near u. A carrier needs Ĉ_q = C_B on F ∖ E′ and Ĉ_q = T on σ_t ∖ E′. PP63 Prop 2.1 rules out C_B and models near B. It does not rule out every q ∈ Δ. This is unproved.
3. **Prop 4.4(ii)** is correct, and agrees with my Prop 2.4: the dominator also differs from + on a non-null part of E.
4. **H\* is checkable and non-circular.** Each clause is a statement about (Σ, Ĉ), refutable by a finite witness or by a permanent one. But §4.2 shows it is **not sufficient**. The missing information is the (TC) consequences of **unassigned** records ((M4) caused by acceptances) and limit acceptances ((M2)). Adding "every assigned carrier keeps a (TC)-live defence disjunct against every rival after every future step" is circular. The non-circular route is a list of **model-level kill patterns** that the acceptance test checks, with Prop 2.2 as the first entry: never commit T ⪯_i C and T ⪯_j C for a model C that answers A on a non-null part of Q_k unless k ∈ supp C and C ⪯_k X_E stays live. That list is finite only if the (TC) kills can be classified. I do not know whether they can (OPEN).

### 4.6 The traps, applied to PP64 final

| Trap | Outcome | Label |
|---|---|---|
| Theorems Q, E (balanced swap, endorsement) | Not applicable: no field in H\*; PP64 §5 realises Cor E.2 literals | PROVED (hypotheses absent) |
| Guidance trap ((TC) kill from T's guidance refusals) | **Conj 3.4 counterexample**, Prop 4.1 | PROVED; CHECKED |
| Prop K splices, PP30 Thm 3.1 | Same mechanism as Prop 4.1: refusals forced by (TC) are invisible to (H2) | PROVED (mechanism) |
| (IB) copies to committed records | Prop 4.2 across carriers | PROVED |
| (TC) on reverses of accepted cycles | Handled by (I2) | — |
| Two-neighbourhood test, swap fixed in advance | Passes (PP64 §6, PP66) | — |
| Two-neighbourhood test, swap chosen after Σ | Absorbable iff some world is free of limit acceptances at every carrier; not maintained by the operation (Prop 4.2) | PROVED |
| Robust balls at two worlds (Prop 5.1) | Not triggered: PP64's reservations live in source space | — |

---

## 5. Robust same-world refusals: exhaustion through PP66's Lemma T

PP66's Lemma T (strict (G) + (TC)): if X′ ⪯_k Y′ is accepted and E is a non-null subset of the part of supp rec(X′, Y′) where Y′ is strictly k-better, then Y′ ⪯_k X′[E ↦ Y′] is refused. Its record is rec(X′, Y′)⁻¹ restricted off E, within d = μ(E) of the inverse.

**Hypothesis (DR) (d-robust refusal).** A set 𝒰_w of records, refused at w, is **open for the record metric d** and **closed under inversion**. PP63 Lemma 3.1 / Cor 3.2 and PP66's surgery produce exactly such sets.

**Proposition 5.1 (two robust worlds exhaust; PROVED, axiom-level given (DR)).** Let w₁ ≠ w₂, let k be the third world, and let 𝒰₁, 𝒰₂ satisfy (DR) at w₁, w₂. Suppose ρ = rec(C_a, X) ∈ 𝒰₁ ∩ 𝒰₂, with X = C_a[F ↦ C_b], C_a and C_b selected at interior indices, and X strictly k-better than C_a on a non-null part of F. Then C_b is undefended.

*Proof.*
- ρ is refused at w₁ and w₂, so defence of C_a gives C_a ⪯_k X.
- Lemma T with E inside the k-improving part, μ(E) small: X ⪯_k C_a[E ↦ X] is refused. Its record is ρ_E := (F ∖ E : C_b → C_a). This is ρ⁻¹ restricted off E, and d(ρ_E, ρ⁻¹) = μ(E).
- ρ⁻¹ ∈ 𝒰₁ ∩ 𝒰₂ by inverse-closure, and 𝒰₁ ∩ 𝒰₂ is d-open, so ρ_E ∈ 𝒰₁ ∩ 𝒰₂ for small μ(E).
- ρ_E = rec(C_b, C_b[F ∖ E ↦ C_a]) is realised out of C_b, and it is refused at w₁, w₂ and k. ∎

**CHECKED (`balls65.py` → `balls65.out`, ALL PASS).** Two-valued instance with a member pair whose swap is mixed at world 3; all 32 models; full (TC), strict (G), defence and protection of both members. The results:
- no ball: SAT;
- one ball at world 1: SAT;
- two balls both at world 1: SAT;
- balls at worlds 1 and 2 (radius 1.5): **UNSAT**;
- refusing only the two centres ρ, ρ⁻¹ at worlds 1 and 2: SAT. This shows the d-openness is what bites.

**Corollary 5.2 (one world per connected family; PROVED).** Let γ : [0, 1] → records be d-continuous, with each γ(t) a member-swap record as in Prop 5.1 (interior ends, a strictly improving part at every world). Suppose each γ(t) lies in a (DR) set 𝒰_{w(t)} refused at w(t). Then w(t) is constant.

*Proof.* If γ(s) ∈ 𝒰_{w(t)} with w(s) ≠ w(t), Prop 5.1 applies to γ(s) ∈ 𝒰_{w(s)} ∩ 𝒰_{w(t)}. By d-continuity, each t has a neighbourhood with γ(s) ∈ 𝒰_{w(t)}. So w is locally constant on the connected interval. ∎

**Answers to the coordinator.**
1. PP66 §5.3 left open whether "balls at different worlds may overlap". They may not overlap on any member-swap record with a strictly improving part at the third world. This is exactly the exhaustion of defending worlds that the coordinator asked about. On a d-connected family of balanced swaps, all ball refusals are at one world (Cor 5.2). So a ball architecture cannot choose the refusing world swap by swap, as PP66 §5.3 does (w chosen from the sign pattern of V^ψ(r)): on a d-connected family the world is forced to be common, and the sign-pattern condition for defence slack then has to hold at that one world for every swap in the family. I have not checked whether d-connected balanced families with different middle worlds exist inside the posterior family (OPEN).
2. **This does not follow from source-space reservations.** Lemma T's refused records ρ_E have the rival C_b[F ∖ E ↦ C_a], which varies with E. A reservation at (b, Y, w) concerns the fixed rival Y. Moreover rec(C_q, Y) = ρ_E would need C_q = C_b[E ↦ C_a] on the support, which is not coherent for non-conic E. So the brief's reservations do not by themselves force the two ends of one swap to be defended at different worlds, and several swaps exhaust a defending world only through (DR) or through accumulation (§3).
3. **Several swaps, source reservations only.** Exhaustion at an index needs a single rival refused at every support world. Reservations from distinct swaps concern distinct rivals unless one model is a swap out of two members (X = C_a[F ↦ C_b] = C_b[D_ab ∖ F ↦ C_a]). Even then the two reservations are centred at a ≠ b and can be chosen disjoint (Prop 3.1). So exhaustion again needs accumulation and non-guidance refusals.

---

## 6. Negative route

No axiom-level conflict was found. Collected constraints:
- Prop 2.3 (forced edge pattern);
- Prop 2.6 (near-T exclusion);
- Prop 3.3 (only non-guidance refusals can exhaust);
- Prop 5.1 (robust refusals at two worlds).

Props 2.3 and 2.6 hold in every (S)-system selecting T. Prop 3.3 needs (MC). Prop 5.1 binds only (DR) architectures.

Props 4.1–4.3 are **not** axiom-level. They refute a conjecture about PP64's invariant, and each dead state is reached through *optional* commitments. REFEREE_round54 confirms PP61 Thm C / Cor C.5: no instance fixed in advance, with any finite number of levels, is an obstruction. So an axiom-level conflict must be continuum-quantitative, with the rival chosen after the relation.

What a genuine conflict would need, by Props 3.1–3.3 and PP61 Thm C:
- an accumulation point p* of distinct selected models;
- a rival chosen after the relation;
- a non-guidance refusal at p* (a (TC) kill or a forced direct-(C) choice) whose reservation meets nearby models;
- at those nearby models, two further refusals forced by (TC) kills that hold for every admissible choice.

I could not produce such a configuration. Exclusions of particular architectures here (§4, §5) are not progress toward it.

---

## 7. Scripts (`r9/PP65_py/`; run `python3 -I -B <script>` inside the folder)

| Script | Content | Label |
|---|---|---|
| `ext65.py` → `ext65.out` | Prop 2.3: forced literals at the edge defender, nested E lattice, 64 models, full (TC); control without hypothesis; atom artefact for (d). Prop 4.1 mechanism: T ⪯₁ Cp alone SAT, T ⪯₂ Cp alone SAT, both UNSAT | CHECKED, ALL PASS (~15 s) |
| `edge65.py` → `edge65.out` | Prop 4.1: exact witnesses that D_{(½,½,0)} is mixed against T at worlds 1, 2, 3 (so rule III does not fire), and is A on class M₃ | CHECKED, ALL PASS |
| `balls65.py` → `balls65.out` | Prop 5.1: two (DR) balls at different worlds ⇒ UNSAT; same world, one ball, centres only ⇒ SAT | CHECKED, ALL PASS (~5 s) |
