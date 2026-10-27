# REFEREE for round 56 (file name as briefed: REFEREE_round55): PP64–PP66, signed propagation, and the limit-closure problem

23 October 2026. Independent referee. Scope: PP64 (§1 definitions and invariant 𝓘, Lemmas 2.1–2.2, Theorem 2.3, Theorem 3.5, §4); PP65 (Lemma 2.1, Props 2.2–2.4, §2.5, Props 3.1–3.3, 4.1–4.3, 5.1); PP66 (construction, Theorem 2, Lemma T, Prop 3); the audit's signed-propagation derivation and accumulation remark (AUDIT_round56). Setting and axioms are those of Briefs 55–56. I add no axiom. Every hypothesis I need beyond the notes' own is named where it enters.

**Labels.**
- PROVED: the argument is complete here, or I checked the author's argument line by line.
- CHECKED: an exact computation in `r9/REFEREE55_py/`. Each is marked as a *re-run* (author's script, output identical) or *independent* (my own code, my own instance).

**Verdict scale.** correct / correct with repair / wrong.

**Conventions.**
- "X ⪯_w Y" means X is at least as good as Y at world w. A record is accepted at w when its old side is at least as good as its new side.
- a_i := [T ⪯_i D] and b_i := [D ⪯_i X] (audit's notation).
- A *section literal* is ℓ(p, X, w) := [C_p ⪯_w X]. At an unassigned index p, it is a constraint on whatever model is eventually put at p.

---

## 0. Verdicts

| # | Item | Verdict |
|---|---|---|
| 1a | PP64 §1: definitions and 𝓘; is each clause preserved by unions? | **correct**. (I1)–(I6) and (I8) pass to unions (fixed-set inclusion, finite Horn closure, or finitely refutable). (I7) has permanent witnesses. (§1.1) |
| 1b | PP64 Lemma 2.1 (unions of chains) | **correct** |
| 1c | PP64 Lemma 2.2 (carrier-free completion) | **correct**. Every record needed for (G), (TC), (I3) and (C⁺) is decided before the carrier-free refusals are added. |
| 1d | PP64 Thm 2.3 (final system) | **correct with repair (wording)**. The hypothesis must say "D = Δ" as well as "total". Both forms of global (C) follow. |
| 1e | PP64 Thm 3.5 | **correct as a conditional, but unusable**. Its two hypotheses contradict each other once one mild proviso holds (§1.5). PP65's stronger "vacuous whenever stage-0 tameness holds" is not proved as written. |
| 1f | PP64 §4 | Lemmas 4.1, 4.2 and 4.5 are **correct**. Thm 4.3 is **correct with repair**: one sentence is false, and the theorem covers 𝓘 only, not tameness. Prop 4.4 is **correct with repair**. What was constructed and what was only inferred is listed in §1.6. |
| 2a | PP65 Lemma 2.1 | **correct** |
| 2b | PP65 Prop 2.2 | **correct** |
| 2c | PP65 Prop 2.3 | **correct**. ext65 re-run matches; an independent SAT check on a different instance agrees. |
| 2d | PP65 Prop 2.4 | **correct**. Existence of the dominator uses KKM on all of Δ. Nothing is constructed. |
| 2e | PP65 §2.5 | **correct with repair**. The topology is right; "always realisable" is unsupported. |
| 2f | PP65 Props 3.1–3.3 | **correct**. Prop 3.1 needs a small repair: each reservation set should be the whole ball. |
| 2g | PP65 Prop 4.1 | **correct with repair**. It needs the provisional edge value to be 3-mixed; PP64's own recommended defender escapes it. A **generalised trap** (§2.4) removes the world-3 condition and catches every open-edge model except the vertex models. |
| 2h | PP65 Prop 4.2 | **correct with repair** (proviso: the accepted records must not already be promised refused) |
| 2i | PP65 Prop 4.3 | **correct as stated**. The audit's correction is right, and it applies to PP65's §0 summary line. |
| 2j | PP65 Prop 5.1, Cor 5.2 | **correct**. balls65 re-run matches; independent SAT check agrees. |
| 3 | PP66 construction, Theorem 2, Lemma T, Prop 3 (middle world) | **correct**. One §0 bullet needs the qualifier "at w = m". Re-run identical; an independent re-implementation (different middle world, both signs of s(g), a four-valued atom) agrees. |
| 4 | Audit's signed propagation | **correct**. Exact hypotheses are in §4. Unit propagation alone suffices (CHECKED). It also catches the generalised trap, but not accumulation. |
| 5 | Audit's accumulation remark | **confirmed and made precise** (§5). With full signed closure, a single new limit literal is always harmless (Prop 5.2). Two can be jointly fatal: an explicit chain has every finite stage consistent and an inconsistent limit (Prop 5.3; PROVED, CHECKED). Consistency does survive limit stages under a stated hypothesis, (H_acc) (Theorem 5.4; PROVED). |

**Bottom line.**
- **What stands.** PP64's final-system theorem stands once every index is assigned and every carried record is decided. So do PP65's forced-structure results (Props 2.2–2.4), PP66's test relation and PP65's ball-exhaustion result.
- **Prop 4.1 is too narrow, and the gap is real.** Its world-3 condition can be removed (§2.4): H\* misses a (TC) kill at *every* non-vertex edge defender, PP64's own recommended defender included.
- **Theorem 3.5 is not a route to coverage.**
- **Limit stages.** They need an invariant that keeps acceptances from accumulating at one literal of every negative "kill" clause. Signed propagation by itself is not enough.

---

## 1. PP64

### 1.1 Definitions and the invariant 𝓘 (correct)

The question is whether each clause survives the union of a chain. I sort the clauses by logical form.

- **Inclusion of a fixed set.** (I1), and "T ∈ P" in (I5). Every stage contains the set, so the union does.
- **Horn closure with finitely many premises.** (I2) has three acceptances. (I3) has three acceptances and one registration. (I4) has six acceptances and one registration. (I6) has one reservation and one assignment. All premises lie in one stage, where the conclusion is already present.
- **Finitely refutable prohibitions.**
  - Disjointness of Acc and Ref: one record at one world.
  - "P is coherent": one model.
  - (I8): a point q with supp q ⊆ Rz_q(X), witnessed by at most three reservations.
- **∀∃ with permanent witnesses.** (I7): every refused record at an assigned carrier has a reservation. A refusal and an assignment present in the union are present together at some stage. That stage supplies the reservation, and reservations are never withdrawn.

I also checked the equivalence in (I8). (F_w(X))_w is a KKM cover iff every q has some w ∈ supp q with q ∉ O_w(X), i.e. supp q ⊄ Rz_q(X). Proof: a point in the relative interior of the face Δ_J has supp = J, and boundary points are covered by smaller faces.

The acceptance test's germ condition is not part of 𝓘. It is implied by (I6), (I7) and disjointness: an assigned p carrying a refusal has a reservation U ∋ p, and every assigned q ∈ U refuses. So it adds nothing to the invariant.

**What 𝓘 does not record.**
- (TC) kills that no committed refusal records yet (PP65 Prop 4.1; §2.4 below).
- Limit acceptances (§5).

Neither is a defect of Lemma 2.1. Both are defects of 𝓘 as a test of extendibility.

### 1.2 Lemma 2.1 (correct)

The proof is exactly the classification in §1.1. The union of P, D, Acc, Ref and Res is again a partial system: the O_w(X) are unions of open sets, and committed models never change.

### 1.3 Lemma 2.2 (correct)

The brief asks whether every record needed for (G), (TC) and (C⁺) is decided before the carrier-free refusals are added. It is.

- **(G).** (I1) commits *every* weak-guidance acceptance and strict-guidance refusal, including those of carrier-free records. So no new refusal can contradict guidance.
- **(TC), (I3), (I4)/(C⁺).** These are conditions on Acc (and P) only. The completion adds refusals and nothing else. The unions of Acc and P are unchanged, so these closures still hold.
- **Undominatedness.** The record needed for C_p's undominatedness against Y is rec(C_p, Y). It is carried by C_p, so it is decided. Its inverse rec(Y, C_p) may be carrier-free and then refused, which can only help.
- **Sections and competitiveness.** Both concern rec(C_p, X), which is carried and therefore decided. (I6) and (I7) are untouched.

### 1.4 Theorem 2.3 (correct with repair: wording)

I re-derived each clause.
- Strict (G) is (I1). (TC) is (I2) together with disjointness.
- Undominatedness is (I3).
- Competitiveness: (I8) gives a free world; by (I7) that world is not refused; by totality it is accepted.
- Closed sections: by (I6) and (I7), {p : C_p ⋠_w X} = O_w(X).

**Global (C), both forms.**
- Every A_w(N) = F_w(N) is closed. Competitiveness makes them a KKM cover, so some p has C_p ⪯_w N at every w.
- If N is undominated, then N ≈ C_p, and (I4) registers N.
- **(C∃).** For incoherent X, the same p gives C_p ⪯_w X everywhere. Equality at every world would register X, which (I5) forbids. So the domination is strict somewhere.
- **(C_dir).** If X ⪯_w N at every world with N ∈ P, then (I3) gives N ⪯_w X at every world. So X ≈ N, X is registered and is coherent.

**Repair.** The theorem must assume D = Δ as well as totality, as PP65 §4.1 says. KKM is used.

### 1.5 Theorem 3.5: status (correct as a conditional, unusable)

**The proof as a conditional is sound.**
- An initial ordinal of size 𝔠 with every item recurring cofinally exists: bounded subsets have size < 𝔠.
- A record carried only after its first appearance is settled when it recurs.
- Prop 3.2 needs finitely many revisions per index, and Conjecture 3.4 supplies that.

**Status.** Conjecture 3.4 is universal over tame systems. I show that stage-0 tameness together with Conjecture 3.4 is contradictory, under the following proviso.

> **(P)** At the stage where a non-vertex model D is first assigned at an open-edge index p, the two partial-splice records r_1, r_2 of §2.4 are not in 𝓡 (not promised refused).

*Argument.*
1. Any full system produced by Theorem 3.5 satisfies (S) on Δ. So on each edge it takes infinitely many values (PP65 Prop 3.2).
2. Hence some stage assigns a model D ∉ {V_1, V_2} at an index of the open edge {1, 2}.
3. Immediately after that assignment, the system is tame (Prop 3.1).
4. By §2.4, D is mixed against T at worlds 1 and 2. Two acceptance steps, each legal by Prop 3.3(i) given (P), then produce a tame system in which (rec(D, X_E), 1) and (rec(D, X_E), 2) cannot both be settled.
5. That contradicts Conjecture 3.4.

**About (P).** I cannot discharge it in general. A Ĉ-copy reservation could in principle promise those exact records refused. But there is a continuum of choices of the partial splices (§2.4), and each would need its own coincidental reservation.

**Comparison with PP65.** PP65's "Theorem 3.5 is vacuous as stated" is right in substance. Its route ("whenever stage-0 tameness holds") is not proved as written (§2.4).

**What is needed instead.** A *policy* statement, as PP65 says: a settling rule whose choices are recorded in the invariant. §4–§5 say which consequences such an invariant must carry.

### 1.6 §4, the first extension: what is constructed and what is inferred

**Checked and correct.**
- **Lemma 4.1.** In (b), the general H′ case: Z := T[D(T, D) ∖ H′ ↦ D] has its D-part inside {D strictly w-worse} ∪ E. So X_E ⪯_w Z is guidance, and (TC) kills rec(Z, D) = rec(T, T[H′ ↦ D]). The case is non-degenerate iff H′ ≠ D(T, D) ∖ E.
- **Lemma 4.2.** CHECKED independently in `edge_ref.py` on 42,197 exact samples, with open witnesses for mixedness at worlds 1 and 2.
- **Lemma 4.5.**
  - (a) The derivative of every vertex sum along u∘(1 + te_w) is u_w m_{v,w} g_w.
  - (b) This is the carrier computation.
  - (c) Edge models answer A on E.
  - The 7/16 threshold is CHECKED independently.

**Theorem 4.3 (correct with repair).**
- (I2) holds, and more than PP64 says. Copies of D ⪯_1 X_E and D ⪯_1 T can never lie in one triangle (a carrier of one would have to equal both D and T on F′). So "every triangle containing both links" is vacuous.
- (I3), (I4), (I6) and (I8) are right as argued.
- **Repair 1 (a false sentence).** "At p itself: … guidance at 1 or 2 (Pareto) for every other rival" is false as a defence claim. Pareto says only that no rival is guidance-*refused* at both 1 and 2. That gives (I8) slack at p, which is all the proof needs. D's defence against every other rival is an open obligation, not a discharged one.
- **Repair 2 (scope).** The theorem proves 𝓘, not tameness. Lemma 4.1(b) also commits refusals rec(Ĉ_{q′}, D) ∈ Ref_1 at *unassigned* Ĉ-carriers. Example: the posterior members at u∘(1 − te_1), which are weakly 1-worse than T (by Lemma 4.5(a)'s monotonicity) and silent on E. (H3) would need reservations around them, and Σ₁ lists none (PP65 §4.5.1, confirmed).
- **Minor.** "T and D carry each other's refused records only trivially" should read: only guidance-type records on {T = D}, whose copies are guidance refusals and are covered by the guidance reservations.

**Prop 4.4 (correct with repair).**
- (i) is KKM in any total extension satisfying 𝓘.
- (ii) needs C_{q\*} strictly 1-better **and** strictly 2-better than T somewhere off E, not "or": both acceptances are required.
- (iii) is conditional on "the selection follows the ray".
- (iv) The carrier-freeness is shown only for carriers on the ray. Carrier-freeness in Prop 3.3(iii) is relative to Ĉ on all of Δ (same objection as PP65 §4.5.2).

**Constructed.**
- A two-index partial system Σ₁ (T at u, the −e₃ edge posterior D at (½, ½, 0)).
- Explicit commitments D ⪯_1 X_E and D ⪯_1 T, with the forced refusals and their reservations.
- A proof that Σ₁ satisfies 𝓘.

**Inferred only.**
- The switch, and the existence of an all-world weak dominator of X_E strictly between u and p. This holds "in every total extension"; nothing exhibits one.
- The cascade of Lemma 4.5, a consequence for future assignments.
- The joint-choice criterion of Prop 4.2, a recommendation derived from which obligations close by guidance.

**Not done.**
- The off-edge dominator of X_E, with its index, comparisons and reservations.
- D's defence against all other rivals.
- Reservations for the refusals committed at unassigned Ĉ-carriers.
- Tameness of Σ₀ and of Σ₁.
- Any family of fills: E is one fixed set.

This confirms the audit: only a **partial edge defence** exists.

---

## 2. PP65

### 2.1 Lemma 2.1, Props 2.2–2.4, §2.5

**Lemma 2.1 (correct).**
- Face-admissibility of edge models is forced by competitiveness and strict (G). Then k·g has the sign of g_i = g_j on M_k for every k ∈ K, so C_p = A a.e. on M_k (vertices: Lemma B).
- Off E, X_E = T; on E both sides equal A. The identity of records follows.

**Prop 2.2 (correct).** For p ∈ P_i, the cycle T → C_p → Z → T has the links T ⪯_i C_p, C_p ⪯_i Z (if accepted) and Z ⪯_i T (guidance). (TC) would then demand T ⪯_i Z, which strict (G) refuses. The degenerate cases C_p ∈ {T, Z} are excluded by strict (G). (a) and (b) follow.

**Prop 2.3 (correct).** I re-derived (a)–(d).
- (a) is 1-D KKM on the edge.
- (b) needs C_p[E′ ↦ S] to be incoherent. That holds because E′ is non-conic.
- (c) uses the triangle C_p → X_{E′} → X_E. The identity rec(T, C_p[E ↦ S]) = rec(X_E, C_p) holds because C_p = A on E.
- (d) needs an intermediate E. Note that the script's labels (c), (d) and (e) are the note's (d), (c), (c).

CHECKED twice.
- **Re-run.** `ext65.py` output identical.
- **Independent** (`trap_ref.py`, instance B). Own encoding. A *different* cell set: D′ is 3-mixed, and T *answers* on one cell, (−1, −1, 10)-type, where D′ gives the opposite answer. 64 splices; (TC) on all triples.
  - Every literal of (b), (c) and (d) is forced under hypothesis (a).
  - (d) is not forced without an intermediate atom.

**Prop 2.4 (correct).** It holds in any system satisfying (S) on Δ. The "C_p ≠ A on a non-null part of E" item uses the same record identity as Lemma 2.1 (which needs only C_p = A on E), together with T's direct (C).
- The note proves necessity. It constructs nothing, and says so.
- Its sentence "existence by KKM" is exactly the step the audit has now forbidden as a substitute for construction.

**§2.5 (correct with repair).**
- W_E is open, contains Φ_T, misses [e_i, e_j], and its closure lies in A_k. A point of W_E on an edge containing k must accept at k, and W_E has no points on [e_i, e_j]. So ∂W_E separates Φ_T from the edge, as claimed.
- **Repair.** "For a single E this is … always realisable" should be deleted, or labelled CONJECTURE. No selection realising it together with all the other obligations is exhibited.

**Prop 2.6 (not in scope; spot-checked).** Correct. CHECKED independently in `edge_ref.py`:
- the example g = (1, 1, −3/2);
- "all new answers of D_{K₀} are k-wrong", on 42,197 exact samples (the proof is by hand).

### 2.2 Props 3.1–3.3

**Prop 3.1 (correct with repair).** Assigning C_q := C_{p_l} on all of B_l makes every q ∈ B_l an assigned carrier of every record refused at p_l. (I7) then needs a reservation containing q. So the reservations of p_l should be **equal to** B_l (or contain it), not merely lie inside it. With that change, the conclusion ("exhaustion is never a finite phenomenon") is right. Note also that supp q ⊇ supp p_l near p_l, so face-admissibility and defence carry over.

**Prop 3.2 (correct).** This is LEAD Theorem C(i)–(ii) restricted to an edge. The tie components of V_i and V_j are different by Lemma B. Infinitely many values on a compact edge give an accumulation point of distinct defenders.

**Prop 3.3 (correct).** I checked the case split.
- If X ≠ C_p, the a.e. limit of guidance refusals gives X ⊵_v C_p strictly. That contradicts C_p ⪯_v X.
- If X = C_p, then reflexivity puts every world in the "accepted by C_p" class. So all of supp q_n would be guidance-refused against C_p, which makes C_{q_n} dominated or uncompetitive.
- (MC) is needed only for the a.e.-convergent subsequence.

**§3.4 (correct).** Limit points of committed acceptances are forced acceptances by closedness of sections. The "second omission" is handled in PP64 by (H3), copy-closure along Ĉ. So it is an omission of Brief 55's formalism, not of PP64.

### 2.3 Prop 4.1 (correct with repair) — edge65 re-run and independent check

**The mechanism is right.**
- Committing a_1 and a_2 for an open-edge D′ kills D′'s defence against X_E at both worlds, by the triangle D′ → X_E → T → D′ at each.
- The (H4) closure stays clean: at most one copy of rec(T, D′) can lie in any triangle, and rule III fails at world 3.

**CHECKED.**
- `edge65.py` re-run identical.
- **Independent** (`edge_ref.py`): open witnesses with all dot products non-zero, so the comparisons hold on open cones, at all three worlds.
- **Independent** (`trap_ref.py`, instance B):
  - a_1 alone and a_2 alone are each SAT; both together are UNSAT;
  - the (I2)–(I4) closure of {a_1, a_2} is clean.

**Repair.** Prop 4.1 assumes that the assigned edge value is mixed against T at **world 3**: "rule III does not fire". The sentence "every face-admissible Ĉ has an open-edge {1, 2} model … Prop 3.1 assigns it for free" conflates two things: *some* edge model with *a 3-mixed* one.

PP64's recommended defender (Lemma 4.2) is weakly 3-worse than T. For it, a_1 and a_2 trigger rule III and an F1, so the step is caught. CHECKED, instance C: the closure conflict appears.

So, as written, Prop 4.1 refutes Conjecture 3.4 only along a Ĉ whose edge values include a 3-mixed model. The claim "whenever stage-0 tameness holds" is not proved.

### 2.4 The generalised trap (referee; PROVED, CHECKED)

**Proposition G.**
- **Setting.** Let D = D_K be face-admissible at an open-edge index p of {1, 2}, with D ∉ {V_1, V_2}. Let E ⊆ Q_3 be non-null.
- **Choice of sets.** For w = 1, 2, let G_w be a non-null proper subset of {D strictly w-worse than T}. Choose them so that:
  - the remaining set S_w := D(T, D) ∖ G_w still contains points where D is strictly 1-worse and points where it is strictly 2-worse;
  - G_1 ≠ G_2.
- **The records.** Put Z_w := T[G_w ↦ D] and r_w := rec(Z_w, D) = (S_w : T → D).

Then:
1. Each r_w is mixed at worlds 1 and 2.
2. Committing r_1 ∈ Acc_1 and r_2 ∈ Acc_2 leaves the (I2)–(I4) closure clean, whatever D does at world 3.
3. The two commitments kill both b_1 and b_2. So D is undefended against X_E, although no committed refusal records this.

*Proof.*
- **Strictly worse parts exist.** Since K ≠ {e_1}, K contains k = (k_1, k_2, 0) with k_2 > 0. Choose g with g_1 = 1, g_2 = −R where R > k_1/k_2, and g_3 large. Then T answers +, which is 1-correct, while k·g < 0, so D is silent or answers −. This holds on an open cone, so D is strictly 1-worse on a non-null set that can be split (μ is atomless). The same argument works at world 2 for K ≠ {e_2}. On E, D answers A, so D is strictly better at 1 and 2.
- **Claim 1.** By the choice of S_w.
- **Claim 2.**
  - A triangle containing exactly one mixed link cannot be closed by two guidance links (PP21 Lemma 2.1).
  - Two copies of r_w cannot be consecutive in a triangle (a carrier would equal both T and D on S_w). In a 3-cycle, any two links are consecutive.
  - Rule III for a registered N would need one record accepted at all three worlds. But r_1 ≠ r_2, and each r_w is non-guidance at both 1 and 2.
  - No ties arise, so rule IV is idle.
- **Claim 3.** At world w, the cycle D → X_E → Z_w → D has the links D ⪯_w X_E (if accepted), X_E ⪯_w Z_w (guidance) and Z_w ⪯_w D (= r_w). Z_w ≠ X_E, so (TC) would demand Z_w ⪯_w X_E, which strict (G) refuses. ∎

CHECKED (independent, `trap_ref.py`, instance C, PP64's kind of D, weakly 3-worse than T):
- r_1@1 alone and r_2@2 alone are each SAT; both together are UNSAT;
- r_w@w forces b_w refused;
- the (I2)–(I4) closure of {r_1@1, r_2@2} is clean;
- `edge_ref.py` gives open witnesses of the strictly-worse parts for five edge models, including K close to e_1.

**Consequence.** H\* together with Prop 3.3(i) admits a dead state at every non-vertex edge defender. This makes PP65's diagnosis model-independent. It also removes the world-3 gap in §2.3, up to proviso (P) of §1.5.

### 2.5 Prop 4.2 (correct with repair)

**Checked.**
- Two of the accepted records rec(C_{q_n}, X) cannot be consecutive in a triangle: on F, a carrier would have to equal both X = C_b and C_{q_m} = C_a. So the closure is clean unless other acceptances interfere, as the note states.
- A refusal of r at l needs a reservation at a. (I6) then refuses at q^l_n ∈ U, a contradiction.
- Accepting r at all worlds registers the incoherent Y through rules III and IV.
- The across-carriers variant is right.

**Repair.** Each step must also satisfy rec(C_{q^l_n}, X) ∉ 𝓡_l. If some reservation (U, X, l) contains points near a, the acceptance is not legal. In fact r is then already refused at l (by (I6) at a), and the configuration changes. This is a proviso on the choice of X, met by a fresh X; it is not automatic.

**The proposed invariant (I9) needs one repair.** At an unassigned p, (I9) enters rec(Ĉ_p, X) as a record. That substitutes the provisional model. The audit is right that it must instead be a constraint on whatever model is assigned at p (§5).

### 2.6 Prop 4.3 (correct as stated)

- **The statement is right.** Its hypothesis ("each revision changes Ĉ on a set with non-empty interior") is in the statement. The proof is a pigeonhole over a countable base.
- **The overstatement is in PP65 §0, item 5.** "Each index revised finitely often allows only countably many co-design revisions" drops that hypothesis. The audit's correction is right: continuum many revisions at single points are compatible with finite revision per index.
- **"None once D is dense"** is correct relative to Conjecture 3.4's own wording (revisions on *open* sets of unassigned indices). It is not a fact about co-design in general. Revising a discontinuous provisional selection on a non-open set of unassigned indices is not excluded, as the audit says.

### 2.7 Prop 5.1 and Cor 5.2 (correct)

**Proof checked.**
- Defence of C_a forces C_a ⪯_k X.
- Lemma T, with E inside the k-improving part, refuses the record ρ_E = (F ∖ E : C_b → C_a) at k.
- ρ_E lies within μ(E) of ρ⁻¹. By inverse-closure and d-openness, it is refused at w₁ and w₂ as well.
- ρ_E is realised out of C_b, so C_b is undefended.
- Cor 5.2 is local constancy of w(t) on [0, 1].

**CHECKED.**
- `balls65.py` re-run identical.
- **Independent** (`balls_ref.py`), with another instance (four F-cells, one of them correct at a single world): every single ball is SAT; two balls at one world are SAT; balls at worlds 1 and 2 are UNSAT; centres only are SAT.

**A caveat the note leaves implicit.** The radius must also satisfy PP66's robust-mixing condition δ < min μ(F_w^±) at the ball's world. Otherwise a single ball already contradicts guidance. My first instance violated it at world 3, and a single ball there was UNSAT for that reason alone. balls65's instance satisfies it.

---

## 3. PP66 (correct)

**The field.**
- φ_F sums to zero over worlds, so (U2)/(U3) are unchanged.
- The rank gaps are as stated, from PP56 §4.1's rows.
  - At a Wr = {o} point: h is −|g| at a correct world, 2|g| at o, and C = 3|g|.
  - At a Cor = {o} point: h is −2|g| at o, |g| at a wrong world, and C = 5|g|. (The −h values do not border h at the relevant worlds.)
  - So a perturbation of size |g|/2 preserves strict monotonicity: (U1).
- V^ψ(r) = V(r) + Θ(e_v − e_{v′}). I re-derived both signs: s = +1 gives h → S, and s = −1 gives S → h.

**Theorem 2.** I checked each step.
- Robust mixing: δ < μ(F_w^±).
- (TC) at w by inverse-closure of 𝒰.
- Defence on the balls by the d-continuity bound 4K_ψσ√δ < κ.
- Protection, because surgery only adds refusals.
- Reservations, because d(rec(Z, X), r) ≤ μ(Z ≠ C_a).
- (Mix_w) for every w when F is balanced: each odd-world-m point improves m and worsens the others, or the reverse, and c_m = 0 forces both kinds to carry mass.

**Lemma T.** Correct, and axiom-level (strict (G) and (TC) only). The consequence that a d-robust shape must defend the two ends at different worlds is correct.

**Prop 3 (the middle-world rejection).**
- Correct under its stated hypotheses. For f with increments in multiples of ε_m, V^f(r) = cε_m has equal non-m coordinates, and the c ≠ 0 cases are immediate.
- The c = 0 case is Theorem E for f. It needs (H_Γ) for f at a, which is unconditional only for f = u¹ at a = u. PP66 lists this hypothesis.
- **Repair (wording).** PP66 §0's first "rejects" bullet must carry "at w = m". For w ≠ m a common q *passes* (CHECKED by PP66, and in my run below).

**CHECKED.**
- **Re-run.** `two_nbhd66.py` output identical, ALL PASS.
- **Independent** (`twonbhd_ref.py`): my own field code, R₀ and record metric, on a different instance.
  - Instance: middle world m = 1 (PP66 used m = 0); a balanced F with both signs s = ±1 and both odd-world-m kinds; a four-valued atom off R; w₀ ≠ w; 4,096 models.
  - For w = 0, 1, 2 with base ψ, every clause holds: (U1)–(U2), strict (G) on all pairs, (TC) on all triples, defence and protection of all four members, and the reservations. The centre verdicts are as Theorem 2.8 states.
  - Controls behave as predicted:
    - the u¹ base fails defence (Theorem E);
    - a common q fails at w = m (Prop 3) and passes at w ≠ m;
    - with no surgery, the reservations fail;
    - balls at two worlds fail (PP65 Prop 5.1).

**Scope.** As PP66 says, R₁ is a test pass for one swap fixed in advance. It keeps R₀^ψ's section failures elsewhere (PP62 Thm P), so it is not a module with closed sections.

---

## 4. The audit's signed-propagation derivation (correct)

**Exact hypotheses.**
1. **Edge model.** D = C_p with supp p ⊆ {1, 2}, and D defended on supp p against X. This is (S)-competitiveness. Nothing else about D is used: not coherence, not face-admissibility, not "D = A on E". If p = e_1, b_1 holds outright and ¬a_1 follows directly.
2. **Fill.** Any X with X ⪯_i T accepted and T ⪯_i X refused at **both** i = 1 and i = 2. Strict (G) supplies this whenever X is pointwise weakly better than T at worlds 1 and 2, and strictly better on a non-null set at each. The X_E with E ⊆ Q_3 non-null qualify.
   - Non-conicity of E is **not** needed; it matters only for incoherence and direct (C).
   - E need not lie in T's silence: any fill improving T at both edge worlds works.
   - The *same* X must improve T at both edge worlds; the derivation fails for fills that improve at one edge world only.
3. **Axioms.** Strict (G) and (TC) at worlds 1 and 2, on the literal triangle T, D, X, and D's defence disjunction. No (IB), sections, KKM or direct (C).

**Derivation (PROVED).**
- The cycle D → X → T → D at i has the links D ⪯_i X (b_i), X ⪯_i T (guidance) and T ⪯_i D (a_i). (TC) would then demand T ⪯_i X, which is refused. So ¬a_i ∨ ¬b_i.
- Defence gives b_1 ∨ b_2.
- Resolution gives ¬a_1 ∨ ¬a_2. This is PP65 Prop 2.2(b) and the inner step of LEAD Lemma E.
- **Unit propagation alone** carries out the chain a_1 ⇒ ¬b_1 ⇒ b_2 ⇒ ¬a_2. CHECKED (`trap_ref.py`): on instance B's full clause set, Glucose's propagate from a_1 returns exactly ¬b_1, b_2 and ¬a_2, and nothing is fixed without a_1.

**Scope.**
- Since a_i does not depend on X, the propagation runs for the whole fill family at once. Once a_1 is accepted, D must accept every such X at 2 and refuse it at 1.
- The same propagation catches the generalised trap of §2.4: replace a_w by [Z_w ⪯_w D] for any Z_w strictly w-worse than X.
- It does **not** catch accumulation (§5), which needs limit acceptances. It is not, by itself, an extension theorem.

---

## 5. Accumulation: the limit-closure problem

### 5.1 Precise statement

**Ingredients.**
- Let 𝒦 be the ground clause set of finitary axioms: guidance units; (TC) clauses; rule III; rule IV with the F2 prohibition; the defence disjunctions Def(p, X) at every index; and the reservation clauses ((U, X, w) with q ∈ U ⇒ ¬ℓ(q, X, w)). (IB) is built in, since literals are record–world pairs.
- **(SC) Signed closure.** Acc and Ref contain every literal entailed by the commitments together with 𝒦, and they are disjoint. Every committed refusal at an assigned carrier carries a reservation, as in (I7).
- **(I9) Limit acceptances.** For every (X, w), every p in the closure of {q ∈ D : ℓ(q, X, w) ∈ Acc} has ℓ(p, X, w) committed. At unassigned p this is a constraint on the eventual model, not a record (the audit's correction to PP65 §4.3).

**The limit-closure problem.** Let (Σ_α)_{α<λ} be an increasing chain of consistent systems, each satisfying 𝓘 + (SC) + (I9). Let Σ_λ be the least system containing ⋃Σ_α and closed under (SC) and (I9). This is a least fixed point; limit literals may generate further limit literals. **Is Σ_λ consistent?**

### 5.2 What is automatic (PROVED)

**Prop 5.1 (uncountable cofinality).** If cf(λ) > ω, then Σ_λ = ⋃Σ_α.

*Proof.* Δ is metrisable. A limit point of ⋃_α A_α is the limit of a sequence q_n ∈ A_{α_n}, and sup α_n < λ. So it is already a limit point at some stage, where (I9) committed it. Entailment is compact, so the union is closed under (SC). ∎

New limit literals therefore arise only at limits of countable cofinality.

**Prop 5.2 (one literal at a time).** Let cf(λ) = ω, and let L = ℓ(p, X, w) be a first-generation limit literal. Then ⋃Σ_α ∪ {L} is consistent.

*Proof.*
1. Otherwise, by compactness, some Σ_β entails ¬L. By (SC), ¬L is committed with a reservation U ∋ p (or, at unassigned p, a reservation (U, X, w) ∋ p).
2. The committed acceptances q_n → p eventually lie in U.
3. At the stage where both are present, (I6) refuses ℓ(q_n, X, w), which is also accepted. That stage is inconsistent, a contradiction. ∎

### 5.3 Two limit literals can be jointly fatal (counterexample; PROVED, CHECKED)

**Prop 5.3.** There is a chain of length ω in which every stage is consistent and satisfies 𝓘 + (SC) + (I9), while Σ_ω is inconsistent.

**Instance.**
- T at u. An edge defender D at p ∈ (e_1, e_2). The fill X_E.
- Interior indices q_k → u and q′_k → u carrying models Q_k = T[L_k ↦ D] and Q′_k = T[L′_k ↦ D].
- The layers L_k, L′_k are cells where T is silent and D answers, correctly at world 1 only (respectively 2 only), with masses 2^{−k}. So Q_k → T in measure.
- **Stage n** commits Q_k ⪯_1 D and Q′_k ⪯_2 D for k ≤ n.

**Each stage is consistent and decides neither a_1 nor a_2.** (I9) is vacuous at each stage, since the acceptance index sets are finite. The work is to show that (SC) commits no literal on a_1 or a_2.

- **CHECKED by SAT for n = 1** (`trap_ref.py`, instance L): the stage is SAT, stage + a_1 is SAT, stage + a_2 is SAT, and stage + a_1 + a_2 is UNSAT. The stage commitments are (I2)–(I4)-clean.
- **For every n, an explicit relation** (`limit_exact.py`). It is additive, Φ(Z) = Σ_{cells where Z = D} Δ(cell), with X ⪯_w Y iff Φ_w(X) ≤ Φ_w(Y). So reflexivity, (IB) and (TC) are automatic, and strict (G) is the sign pattern of each Δ(cell).
  - Each selected model is strictly λ-Bayes cell by cell, with λ_T = (1, 1, 10) and λ_D = (1, 1, 0). Hence each is defended on its support and strictly protected, which gives undominatedness and direct (C).
  - The separating weights of the Q_k come from tangent lines to the strictly convex curve z = 1/10 + e². The layer directions are Δ(L_k) = (−1, 1 − ε_k, z_k), with ε_k = k/(100n²).
  - The inequalities are verified by hand in the script's header. Margins are uniform in n except the separation margin ½ν_k ε², which is positive.
  - The relation contains all stage-n commitments and a_1. Its mirror (1 ↔ 2) contains a_2.
  - Exact check: n = 1–30, 50 and 100; also with mass-proportional layers and twelve unoccupied future layer cells per world, n ≤ 12.
- The instance is an abstract cell model, like REFEREE_round54 §4.3. Stagewise satisfiability is not claimed in the Gaussian domain.

**The limit is inconsistent, at the level of the axioms.**
- (I9) at Σ_ω commits a_1 = ℓ(u, D, 1) (limit of the q_k) and a_2 (limit of the q′_k).
- §4's clause ¬a_1 ∨ ¬a_2 is in 𝒦 from stage 0, so Σ_ω is inconsistent.
- In any total extension, closed sections force a_1 and a_2 anyway. So the union ⋃Σ_n is **not extendible**, although it satisfies 𝓘 + (SC) (Lemma 2.1 and compactness).
- This is the audit's remark in exact form: "harmless at each finite stage, fatal in the union".

### 5.4 Under a stated hypothesis, consistency survives (PROVED)

**Definition.** A record–world literal L = (r, w) is *isolated* at a stage if every assigned carrier q of r lies in a committed punctured reservation (U_q ∖ {q}, C_q ⊕ r, w), and every unassigned index constrained by L likewise. A punctured reservation is legal: its set is open, and q decides its own verdict.

**(H_acc).** For every negative clause ¬L_1 ∨ … ∨ ¬L_m of section literals entailed by the stage's commitments together with 𝒦, at least one L_i is committed refused (with reservation) or isolated.

The special case "committed refused" is eager resolution of every kill clause. Isolation is weaker: L_i may stay undecided at its own index, but nothing may accumulate there.

**Theorem 5.4.** Suppose every stage is consistent and satisfies 𝓘 + (SC) + (I9) + (H_acc). Then Σ_λ is consistent and satisfies (SC), (I9) and (H_acc). Every refusal newly derived at λ is of an isolated literal, so the punctured reservation plus the point is a legal reservation for it, as (I7) requires.

*Proof.*
1. **First generation.** Let N₁ be the new first-generation limit literals. Suppose ⋃Σ_α ∪ N₁ is inconsistent.
   - By compactness, some Σ_β entails ¬(L_1 ∧ … ∧ L_m) with L_i ∈ N₁, which is a negative clause.
   - By (H_acc), some L_i is refused at β with a reservation U ∋ p_i, or isolated with a punctured reservation around p_i.
   - The acceptances q_n → p_i (q_n ≠ p_i) that make L_i a limit literal eventually lie in that set. (I6) then refuses them at a finite stage, which is inconsistent. Contradiction.
2. **Later generations.** A generation-(k+1) literal is a limit of acceptances derived from ⋃Σ_α ∪ N_{≤k}.
   - If it were refused or isolated at β, the reservation would refuse some of those derived acceptances by (I6).
   - That would make ⋃Σ_α ∪ N_{≤k} inconsistent, contrary to the induction hypothesis.
   - Transfinite iteration of the closure operator is handled the same way.
3. **(H_acc) for Σ_λ.** Take a negative clause entailed by Σ_λ. By compactness, Σ_β together with a finite N₀ ⊆ N entails the clause enlarged by ¬N₀. (H_acc) at β picks a literal, and by step 1 it is not in N₀.
4. **(I7) for refusals new at λ.** Such a refusal ¬L′ is entailed by Σ_β ∪ N₀. So L′ belongs to a negative clause with N₀, and (H_acc) makes L′ refused at β (so it is not new) or isolated. ∎

The counterexample of §5.3 violates (H_acc) exactly: the clause ¬a_1 ∨ ¬a_2 has neither literal refused nor isolated at u. Isolating a_1, i.e. committing (U ∖ {u}, D, 1), blocks every q_k-acceptance near u.

**What remains OPEN.** Theorem 5.4 is a limit lemma, not an extension lemma. Whether (H_acc) can be maintained at successor steps is open. It requires isolating one literal of continuum many kill clauses, and each isolation spends defence slack on a punctured neighbourhood.

**Bearing on Brief 56.**
- For the fill family, the relevant kill clauses are ¬a_i ∨ ¬b_i(E) for all E, and ¬a_1 ∨ ¬a_2.
- PP64's Σ₁ already satisfies (H_acc) for them: it refuses T ⪯_1 D with a reservation at u and commits D ⪯_1 X_E. So T's defence world against each new edge defender must be fixed, with a neighbourhood, when the defender is installed.

---

## 6. Computations (`r9/REFEREE55_py/`; run `python3 -I -B <script>` in that folder)

| Script → output | Content | Status |
|---|---|---|
| `rerun_geom64.out` | PP64 `geom64.py` | re-run, identical, ALL PASS |
| `rerun_edge65.out`, `rerun_ext65.out`, `rerun_balls65.out` | PP65 scripts | re-run, identical, ALL PASS |
| `rerun_two_nbhd66.out` | PP66 script (101 s) | re-run, identical, ALL PASS |
| `edge_ref.py` → `.out` | own exact advice code. D′ mixed at 1, 2, 3 on open cones. PP64's D weakly 3-worse (42,197 samples) and mixed at 1, 2. Strictly-worse open parts for five edge models (constructive for K near e_1). 7/16 threshold. D_{K₀} new answers 3-wrong | independent, ALL PASS |
| `trap_ref.py` → `.out` | own SAT encoding. Instance B: Prop 2.3 (b)–(d), Prop 4.1 mechanism and clean closure, unit propagation a_1 ⇒ ¬b_1, b_2, ¬a_2. Instance C: Prop 4.1 caught for a weakly-3-worse D; generalised trap SAT/SAT/UNSAT, kills, clean closure. Instance L: one stage of §5.3 | independent, ALL PASS (24 s) |
| `balls_ref.py` → `.out` | Prop 5.1 on a new instance satisfying robust mixing | independent, ALL PASS |
| `twonbhd_ref.py` → `.out` | PP66 Theorem 2 re-implemented: m = 1, s = ±1, four-valued atom, w₀ ≠ w; controls; two-world balls | independent, ALL PASS |
| `limit_exact.py` → `.out` | §5.3: an explicit additive relation for every stage; exact check n ≤ 30, 50, 100, and with masses n ≤ 12 | independent, ALL PASS |
| `limit_lp.py` → `.out` | exploratory LP attempt, superseded by `limit_exact.py`. Its infeasibility for n ≥ 3 comes from fixed weight choices and margins, not from the axioms | superseded; kept, not deleted |
