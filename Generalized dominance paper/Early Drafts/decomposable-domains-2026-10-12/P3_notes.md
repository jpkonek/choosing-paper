# P3. The central extension lemma of the ordinal construction programme

14 Oct 2026 (round 11). Labels: **PROVED** (full proof here), **CHECKED** (verified against the cited sources, proof sketched), **CONJECTURE**, **NUMERICS** (script `p3py/check_examples.py`, output `p3py/check_examples.out`; run with `python3 -I`; no proof depends on it).

Sources read: BRIEF10; termfix rules; *Coverage after Neutral Abstention* §3 (Thm closure); *Vacuous Targets and Transfinite Construction* §5 (union lemma, reserved-neighbourhood invariant); *Ordinal Refinement by Slack Envelopes* (positive refinement; Prop counterexample); *Domain Closure and Extendability*; *Independent Rankings Without Additive Structure*; *Incomplete Rankings and Coverage* (summary); write-up §§2–3, 6, 7, 8; N9 (N9.4 normal form, Lemma R), N17/N19 (M1/M2, N17.B′), v3 (two-world construction).

Terminology as in TERMFIX_RULES: decomposable domain, advice range, U-domain M_U (the evaluable models are the measurable subsets of U = D_{K′}).

---

## 0. Outcome

The extension lemma, in the form suggested in *Vacuous Targets* §5 (install the missing competitiveness comparison while respecting open reservations that are compatible world-by-world), is **false**, for two independent reasons, both PROVED with explicit examples on M_U. I also give an **exact** replacement that needs no reservations, and a **positive** form under a witness hypothesis that a construction can actually check.

- **P3.1 (PROVED) Exchange normal form and transport.** Under (IB), installing C_p ⪯_i X installs one *exchange* σ = 1_{C_p} − 1_X at world i. It therefore installs C_q ⪯_i C_q − σ for every selected C_q compatible with σ, wherever q lies in Δ. Reservations are likewise per exchange, not per (p, X).
- **P3.2 (PROVED) Exact extension theorem.** Add a fifth closure rule, the *limit rule* (R5): if p_k → p and C_{p_k} ⪯_i X for all k, install C_p ⪯_i X. Fix a choice κ(p, X) ∈ supp p of a world for every competitiveness requirement. Then the least relations containing the background order and the chosen comparisons, closed under the five rules, form a successful system iff they produce no forbidden outcome. Every successful system contains such a minimal successful system. So closed sections are not an invariant that reservations must protect: they are produced by an infinitary Horn rule, and the only free data are the choices κ.
- **P3.3 (PROVED) Compactness.** If closed sections are dropped, everything else ((G), (IB), undominated competitive coherent selection, (C) for selected models) is of finite character. R5 is the only non-compact requirement, and compactness genuinely fails there (P3.6).
- **P3.4 (PROVED) Necessary conditions on every successful system.**
  - *Exchange transversality* (ET): the set of worlds accepting an exchange σ must meet supp q for every selected index q compatible with σ.
  - *Compulsory comparisons*: some world comparisons are made compulsory by the faces that Comp(σ) meets.
  - *Transported Lemma R*: a rejection near p forces competitiveness from other worlds at every compatible index, not only near p.
- **P3.5 (PROVED) Counterexample 1.** The reservation form of the lemma is false even when the reservations satisfy the covering condition (5) for every single model. A dead state can pass every per-model test, because the reservation at one world is transported to another base point. The correct compatibility condition is (ET), at the level of exchanges.
- **P3.6 (PROVED) Counterexample 2: closedness cannot be postponed.** Take an increasing ω-sequence of partial choices. Every finite stage extends to a full successful system (an explicit additive one), yet the union violates strict (G) through R5. Extendability is therefore not preserved under countable unions. Any successful transfinite construction must commit to open reservations at finite stages, with foresight that finite information does not supply.
- **P3.7 (PROVED) Witnessed extension theorem (the positive lemma).** Suppose an additive witness ψ satisfies (W1) ψ-competitiveness, (W2) ψ-Pareto optimality of the selected models, and (W3) lower semicontinuity of p ↦ ψ_i(C_p). Then every ψ-admissible choice generates relations inside ψ with no strict-(G) reversal. The only possible failure is (C), at incoherent models that share a ψ-profile with a selected model.
  - Under (W4) (no such models) the lemma holds unconditionally. It reproduces the precise, box, two-world and gauge-mixture covers (CHECKED).
  - It cannot produce an additive cover of T1 (by Thm gm, (W4) must fail), nor a cover of V under strict guidance in n ≥ 3 (by *Three Complete Rankings*, (W1)–(W3) must fail).
- **P3.8 (PROVED from P3.7 and the write-up) What the lemma gives for T1 on M_U.** A witnessed cover is an (M0) ranking with (E_ψ) and a nonempty set of atom chords. A T1 construction therefore needs two inputs:
  - (a) an additive *pre-system* through T1 (all axioms except (C)), whose existence is open and is the chord-tolerant geometric residual R-a′/R-b′ for ψ itself;
  - (b) an ordinal tie-breaking choice κ at the chords (question Q1).
  
  Without an additive witness, a T1 construction needs a world order that is closed under R5 and not additive; none is known.
- **P3.C1 (CONJECTURE) A Villegas-type theorem.** At a complete world, R5 along a measure-continuous selection forces countable additivity on the region its shells sweep. If true, complete T1 covers with continuous selections are excluded by Thm complete.

---

## 1. The problem, precisely

Fix a decomposable domain M (closed under splicing and convergence in measure), a finite set Ω of worlds, and a **coherent selection** C: Δ → M (each C_p coherent modulo null sets). A **successful system for C** is a family of preorders ⪯_i on M satisfying the following.

- **(G)** Weak and strict guidance (the background order, world by world and problem by problem).
- **(IB)** Independence across binary problems.
- **(U_sel)** Every C_p is undominated.
- **(Comp)** C_p is competitive on supp p.
- **(Cl)** Every section A_i(X) = {p : C_p ⪯_i X} is closed, for every X ∈ M.
- **(C)** A model tied everywhere with a member of C_L is in C_L.

(LA) then holds, and (S) = (Comp) + (Cl). A ranking *covers* a coherent D if D ∈ C_L and (LF) holds at D. WLOG D is selected (Coverage after NA, end of §3).

**Forbidden outcomes** (as in Thm closure):
- (a) reversal of a strict (G) comparison;
- (c) an incoherent X tied at every world with a selected C_p.

The exact-sections outcome (b) of Thm closure plays no role in P3.2.

**The four rules** (Thm closure):
- R1 reflexivity;
- R2 transitivity;
- R3 (IB)-transfer;
- R4: if X ⪯_i C_p at every i, install C_p ⪯_i X at every i.

**The natural lemma (EL_res), as posed.**
- *State.* A *state* is relations closed under R1–R4 that contain the background order, with no forbidden outcome, together with **reserved sets** R_i(X) ⊆ Δ on which C_q ⪯_i X is permanently forbidden.
  - Reserved sets must contain an open neighbourhood of each rejected index, or they do not secure closedness (Vacuous Prop). So we take them relatively open. If closed reserved sets are intended, their interiors are what matter.
  - The state respects the reservations.
  - The reservations satisfy the per-model covering condition (K_X): for every p there is i ∈ supp p with p ∉ R_i(X).
- *Claim.* If (p, X) is unmet (no i ∈ supp p has C_p ⪯_i X), then some i ∈ supp p with p ∉ R_i(X) can be installed (closing under R1–R4) with no forbidden outcome and no reservation violated.
- *Limit clause.* At limit stages, take unions. The union lemma (Vacuous Lemma union) preserves R1–R4, (U_sel) and respect of fixed reservations. The Vacuous Prop then gives closed final sections, provided every comparison is eventually decided.

**Verdict:** EL_res is false (P3.5). Its limit clause also hides a genuine failure once closedness is treated as a rule (P3.6). The exact replacement is P3.2.

---

## 2. Exchange normal form and transport (P3.1, PROVED)

**Exchanges.** On a decomposable domain, (IB) says that X ⪯_i Y depends only on the disagreement set Z = {a_X ≠ a_Y} and the two advice functions on Z. Call the triple (Z, a_X|Z, a_Y|Z) the *exchange* of (X, Y).
- On M_U every pair has one orientation in U and advice range {accept, no advice}. An exchange is then the signed function σ = 1_X − 1_Y: U → {−1, 0, 1}.
- With 𝒮_i := {1_X − 1_Y : X ⪯_i Y}, N9.4 / N17.1 give the following equivalence: (G)+(IB) at world i hold iff 𝒮_i
  - (P) contains every σ with σ·sgn_i ≥ 0 a.e. (sgn_i(h) = sign h_i);
  - (N) contains no σ ≠ 0 with σ·sgn_i ≤ 0 a.e.;
  - (Σ) is closed under every sum σ + τ that stays {−1, 0, 1}-valued (this is transitivity under cancellation).
- The *same* σ is evaluated at every world; the worlds differ only by the twist sgn_i.

**Compatibility.** A section comparison C_q ⪯_i X has exchange σ = 1_{C_q} − 1_X. Put

  Comp(σ) := {q ∈ Δ : {σ = 1} ⊆ C_q and {σ = −1} ∩ C_q = ∅ a.e.}.

These are the selected models from which "remove {σ = 1}, add {σ = −1}" is a legal change. In general domains: Comp(e) = {q : a_{C_q} = a_X on Z}, and the transported model C_q|_{Z^c} ∪ X|_Z lies in M by splicing.

**Lemma 2.1 (transport; PROVED).** For each world i and exchange σ, either C_q ⪯_i C_q − σ holds for every q ∈ Comp(σ), or it holds for none. Hence:
- A_i(X) = {q : i ∈ I(1_{C_q} − 1_X)}, where I(σ) := {i : σ ∈ 𝒮_i};
- installing C_p ⪯_i X installs C_q ⪯_i C_q − σ for every q ∈ Comp(σ);
- rejecting C_p ⪯_i X rejects it at every q ∈ Comp(σ).

*Proof.* C_q and C_q − σ agree off supp σ, and on supp σ their advice is determined by σ. So (IB) makes the comparison independent of q. ∎

Comp(σ) is not a neighbourhood of p. It is a region of Δ cut out by finitely many conic conditions; in Example 1 below it meets two edges of Δ.

**Corollary 2.2 (complete reformulation; PROVED).** For fixed C on M_U, successful systems correspond to maps I: 𝒞 → 2^Ω (𝒞 = measurable {−1, 0, 1}-functions on U modulo null sets) with:
- (P), (N), (Σ) at each world;
- **(T)** for every σ and every q ∈ Comp(σ): I(σ) ∩ supp q ≠ ∅;
- **(Und)** for every m = 1_X − 1_{C_p}: I(m) = Ω ⇒ I(−m) = Ω;
- **(C_sel)** if moreover C_p + m is incoherent, then not I(m) = I(−m) = Ω;
- **(Cl)** q ↦ [i ∈ I(1_{C_q} − 1_X)] has closed support, for every X and i.

Full (C) follows from (C_sel) by the KKM argument of Thm closure.

*Proof.* (T) is (Comp) via Lemma 2.1, (Und) is (U_sel), (C_sel) is outcome (c), and (Cl) is closedness of A_i(X). ∎

So the selection enters (T), (Und) and (C_sel) only through the map σ ↦ Comp(σ). For (T), only the family of supports {supp q : q ∈ Comp(σ)} matters.

---

## 3. The exact extension theorem (P3.2, PROVED)

**Rule R5 (limit rule).** If p_k → p in Δ and C_{p_k} ⪯_i X for all k, install C_p ⪯_i X (for every i and X).

A **choice** is a function κ assigning to each pair (p, X) ∈ Δ × M a world κ(p, X) ∈ supp p; a *partial choice* is defined on a subset. Let Cl₅(κ) be the least family of relations on M that contains the weak background comparisons and the chosen comparisons C_p ⪯_{κ(p,X)} X, and is closed under R1–R5. It exists by Knaster–Tarski: the operator is monotone on the complete lattice of families of relations. Each rule has at most countably many premises, so the iteration stabilises by stage ω₁. Call Cl₅(κ) *clean* if it has no outcome (a) and no outcome (c).

**Theorem 3.1.** Fix M and a coherent selection C.
1. If κ is total and Cl₅(κ) is clean, then Cl₅(κ) is a successful system for C.
2. Let (⪯_i) be any successful system for C, and let κ(p, X) be any i ∈ supp p with C_p ⪯_i X (one exists by (Comp)). Then Cl₅(κ) ⊆ (⪯_i), and Cl₅(κ) is clean, hence successful.
3. Consequently a successful system for C exists iff some total κ has Cl₅(κ) clean. In particular C admits a cover of a selected target iff such a κ exists.

*Proof.* (1)
- R1 and R2 give preorders, and R3 gives (IB) in both directions (the inverse replacement is also a replacement).
- The background comparisons give weak (G). Strictness follows because the reverse of a strict background comparison would be outcome (a).
- R4 gives (U_sel). The chosen comparisons give (Comp). R5 gives (Cl), since Δ is metrizable and sequences suffice.
- (C): let B ∈ C_L and let Y be tied everywhere with B. By the KKM theorem (write-up Thm kkm, which needs only (LA) and (S)), B is weakly dominated by some selected C_p. Since B is undominated, B ~ C_p at every world, hence Y ~ C_p.
  - Y is coherent, since otherwise outcome (c) would occur.
  - Y is undominated: if Z ⪯ Y everywhere with Z ≺_j Y, then Z ⪯ B everywhere, and B ⪯_j Z would give Y ⪯_j Z, so Z would dominate B.

(2)
- A successful system contains the generators. It is closed under R1–R3. It is closed under R4, since otherwise X would dominate C_p. It is closed under R5 by (Cl).
- Cl₅(κ) is least, so Cl₅(κ) ⊆ (⪯_i).
- Outcome (a) would be inherited by the system. A tie in Cl₅(κ) is a tie in the system, where (C) makes the tied model coherent, so outcome (c) cannot occur.
- Then apply (1). (3) follows from (1) and (2). ∎

**Remarks.**
- (i) Thm closure needs the exact sections to be guessed in advance, and closed. Theorem 3.1 needs no sections at all: R5 makes the generated sections closed. In particular, the open reserved neighbourhoods of the Vacuous Prop exist automatically in every Cl₅(κ). Reservations are a *device for choosing κ*, not part of the problem.
- (ii) *Minimal systems.* Every successful system contains a successful Cl₅(κ). A construction may therefore aim directly at minimal systems; incomparabilities are then whatever Cl₅(κ) leaves.
- (iii) The theorem is an equivalence. It can never manufacture a cover where none exists; this is the first required test, passed trivially. It also never completes rankings. A completion step is separate, and for V it must fail in n ≥ 3 (*Three Complete Rankings*).

---

## 4. Compactness: closedness is the only non-finitary requirement (P3.3, PROVED)

On M_U take propositional variables x_{i,σ} ("σ ∈ 𝒮_i"). The conditions (P), (N), (Σ), (T), (Und) and (C_sel) of Cor 2.2 are finite clauses:
- (T) for σ is the finite set of clauses ⋁_{i∈supp q} x_{i,σ}, one for each of the at most 2^n − 1 distinct supports of Comp(σ);
- (Σ) is x_{i,σ} ∧ x_{i,τ} → x_{i,σ+τ};
- (Und) is ⋀_i x_{i,m} → ⋀_i x_{i,−m};
- (C_sel) is ¬(⋀_i x_{i,m} ∧ ⋀_i x_{i,−m}).

**Theorem 4.1.** For a fixed coherent selection on M_U, the following are equivalent:
- (i) there exist preorders with (G), (IB), (U_sel), (Comp) and (C_sel) (everything except closed sections);
- (ii) every finite subset of these clauses is satisfiable.

*Proof.* By the compactness theorem of propositional logic and Cor 2.2. ∎

(Cl) is the family of infinitary Horn clauses ⋀_k x_{i,σ+d_k} → x_{i,σ}, with d_k = 1_{C_{p_k}} − 1_{C_p}, p_k → p (rule R5). Example 2 (P3.6) gives:
- a set of chosen literals {x_{1,σ_k}}_k, each finite subset of which is satisfiable together with *all* clauses including R5 (by a full successful system);
- yet the whole set, with R5, is unsatisfiable.

So compactness fails exactly at R5. *Consequence:* any obstruction to ordinal coverage that does not use closed sections is witnessed by finitely many exchanges. Any obstruction that uses them may be irreducibly infinitary, as the lexicographic failures (N9.6 FC, R2 Prop 8, R3 Thm L) are.

*Open (no label):* whether T1 on M_U admits a system with everything except (Cl). By Theorem 4.1 this is a finite-character question. N9.7 Design A fails only through (S) via FC. That suggests "yes", but the boundary members of a full selection were not checked, so I attach no CONJECTURE label.

---

## 5. Necessary conditions on every successful system (P3.4, PROVED)

Let N(σ) := {j : σ ≠ 0, σ·sgn_j ≤ 0 a.e.}: the worlds at which C − σ is a strict background improvement on C. By (N), j ∉ I(σ) for j ∈ N(σ).

**5.1 Exchange transversality (ET).** For every σ: I(σ) ⊆ Ω ∖ N(σ), and I(σ) ∩ supp q ≠ ∅ for every q ∈ Comp(σ). (This is (T).)

**5.2 Compulsory comparisons.** If some q ∈ Comp(σ) has supp q ∖ N(σ) = {i}, then σ ∈ 𝒮_i in every successful system. Special cases:
- q = e_i: this is (P), and gives C_{e_i} = P_i (Domain Closure Prop 1).
- q on an edge {i, j}: the edge-Pareto condition. Edge models accept U ∩ {h_i > 0, h_j > 0} and reject {h_i < 0, h_j < 0}.

More generally I(σ) is a transversal of {supp q ∖ N(σ) : q ∈ Comp(σ)}. If this family contains ∅, no system exists for C. This is a test on the selection alone.

**5.3 Transported Lemma R.** Suppose C_p ⋠_ω X for all ω ∈ S ⊊ Ω. Then p has a neighbourhood N such that, for every q ∈ N and every q′ ∈ Comp(1_{C_q} − 1_X):
- supp q′ ⊄ S;
- C_{q′} ⪯_{ω′} C_{q′} − (1_{C_q} − 1_X) for some ω′ ∈ supp q′ ∖ S.

*Proof.* The sections A_ω(X), ω ∈ S, are closed and miss p, so their union misses a neighbourhood N of p. Then ω ∉ I(1_{C_q} − 1_X) for q ∈ N and ω ∈ S; apply (ET). ∎

For q′ = q this is N9.2(b) (Lemma R). The new content is that the reserved neighbourhood around p imposes competitiveness from other worlds at indices q′ anywhere in Comp(·). This is the precise form of the "compatibility obligation" of *Vacuous Targets* §5.

*Remark (CHECKED, by direct inspection).* For continuous selections, the simplest uses of 5.2/5.3 near the target fibre (silencing T1 on one orthant of ∂T1, as in N9 Cor 3.3) reduce, at the limit, to the edge-Pareto condition, because Comp is closed under convergence in measure. So the face conditions do not give new restrictions near T1. New restrictions need (Σ) (cancellation chains) or (Und).

---

## 6. The two counterexamples

Common setting (both PROVED): n = 3 and M_U for T1 (any ε ∈ (0,1); numerics use ε = 0.3, K′ = u + 0.9(T1 − u)). Take a bounded measurable ρ > 0 and the additive ranking

  ψ_i^ρ(X) = ∫_{E_i(X)} ρ(h)|h_i| dμ = const_i − ∫_X ρ h_i dμ.

Its Bayes model at every weight q ∈ Δ is a.e. unique and equals **B_q = U ∩ {q·h > 0} = D_{conv(K′∪{q})}**, which is coherent. The common density ρ cancels from the sign of Σ q_i ρ h_i, and the tie set {q·h = 0} is null.

Hence (Ψ^ρ, q ↦ B_q) is a **successful system** for every such ρ:
- strict (G): ρ|h_i| > 0;
- (IB): additivity;
- (Comp): B_q is Bayes at q;
- (U_sel): uniqueness, including at boundary q;
- (Cl): q ↦ ψ_i^ρ(B_q) is continuous by dominated convergence;
- (C): a model with the profile of B_q is q-Bayes, hence equal to B_q a.e.

The selection C_q := B_q is the same for every ρ. Cl₅(∅) is the background order: it is closed under R4 because a coherent model is never background-dominated, and under R5 because q ↦ B_q is continuous in measure.

### 6.1 Example 1: per-model compatibility is not enough (P3.5, PROVED)

Let a = (−0.1, 1, 1) and a′ = (1, −0.1, −0.1), and let A be the union of two equal small balls around a and a′, contained in D_{T1} ⊆ U and in B_r for r = (½, ½, 0). Let σ := 1_A (the exchange "remove A"). NUMERICS: P_{T1}(a) = 0.413, P_{T1}(a′) = 0.157, r·a = r·a′ = 0.45; radius 0.05 is enough.

- **Comp(σ)** = {q : q·h > 0 on A}. It contains u and r. It meets the relative interiors of [e1,e2] and [e1,e3], and no vertex (NUMERICS; by hand: q·a′ > 0 forces q1 > 0, and q·a > 0 forces q2 + q3 > 0).
- σ·sgn_i takes both signs at every world (from a at world 1, from a′ at worlds 2 and 3). So no world accepts σ by background, and N(σ) = ∅.
- *State:* the background order with these reservations:
  - R_1(X_r) := an open neighbourhood V_r of r, where X_r = B_r − σ;
  - R_2(X_u) = R_3(X_u) := an open neighbourhood V_u of u, where X_u = B_u − σ = U ∖ A.
  - Since 1_{B_q} − 1_{X_r} still takes the value +1 on the ball around a (h1 < 0) for q near r, and 1_{B_q} − 1_{X_u} takes +1 on the ball around a′ for q near u, no reserved comparison is background. The state respects its reservations and is clean.
- *(K_X) holds for every model:*
  - for X_r: at q ∈ V_r, world 2 (or 3) is in supp q and unreserved;
  - for X_u: world 1 is unreserved at every q;
  - every other model has no reservation.
- *(u, X_u) is unmeetable.* Worlds 2 and 3 are reserved at u. World 1 would install σ ∈ 𝒮_1, which by Lemma 2.1 is B_r ⪯_1 X_r, and r ∈ R_1(X_r).
- *No successful system respects these reservations,* since (ET) demands I(σ) ∩ {1,2} ≠ ∅, I(σ) ∩ {1,3} ≠ ∅, and 1, 2, 3 are each excluded by some reservation.
- Note that Ψ^1 itself accepts σ at all three worlds (∫_A h_i > 0), so the selection is fine. The reservations are bad, and **no per-model test detects it.**

*Extracted condition (PROVED necessary).* A reservation plan can lie in the complement of the sections of some successful system only if it is **exchange-compatible**. Let Res(σ) be the set of worlds at which σ is reserved at *some* base point q ∈ Comp(σ). Then Ω ∖ (N(σ) ∪ Res(σ)) must be a transversal of {supp q : q ∈ Comp(σ)}.

### 6.2 Example 2: extendable stages, non-extendable union (P3.6, PROVED)

- Let p0 ∈ Δ° ∖ K′ (numerics: p0 = (0.6, 0.2, 0.2)) and r_k := p0 + δ_k(e1 − p0), with δ_k ↓ 0 and δ_1 small.
- Let W′ := U ∩ {h1 < 0} ∩ {r_1·h > 0}. It is non-null (NUMERICS: 17% of U), contained in B_{p0}, and contained in every B_{r_k}.
- Let X := B_{p0} ∖ W′. X is a strict background improvement on B_{p0} at world 1, because it withdraws acceptances of gambles bad at world 1. So **B_{p0} ⪯_1 X is forbidden in every system.**
- Let κ_m: (r_k, X) ↦ 1 for k ≤ m, a partial choice; world 1 ∈ supp r_k.

*Every finite stage extends to a successful system.*
- Let Sh_k := B_{p0} ∖ B_{r_k}, decreasing in k. In ψ_1^ρ the world-1 gain of moving from p0 to r_k is
  G_k = −∫_{Sh_k} ρh_1 + ∫_{B_{r_k}∖B_{p0}} ρh_1,
  and ψ_1^ρ(B_{p0}) − ψ_1^ρ(X) = ∫_{W′} ρ|h_1| =: w.
- Put ρ := M on Sh_1 ∩ {h_1 ≤ −η|h|} and ρ := 1 elsewhere (this region is disjoint from W′ ⊆ {r_1·h > 0}). Then G_k ≥ M a_k − c, with a_k := ∫_{Sh_k ∩ {h_1 ≤ −η|h|}} |h_1| ≥ a_m > 0 for k ≤ m and c a constant.
  - a_m > 0 because U ∩ p0^⊥ contains gambles with h_1 ≤ −η|h| (NUMERICS: a_k > 0 for all tested δ_k down to 0.002).
- With M ≥ (w + c)/a_m: ψ_1^ρ(B_{r_k}) ≤ ψ_1^ρ(X) for all k ≤ m. So κ_m ⊆ Ψ^{ρ_m}, which is a successful system for the same selection.
- By Thm 3.1(2), Cl₅(κ_m) is clean and extends to a successful system. (NUMERICS: the required M grows like 1/δ_m.)

*The union is dead.* κ_∞ = ⋃ κ_m installs B_{r_k} ⪯_1 X for all k. R5 at p0 installs B_{p0} ⪯_1 X, which is outcome (a). Hence no successful system for this selection contains κ_∞.

*Consequence.* "Contained in a successful system" is not preserved under unions of ω-chains, even when every stage is contained in a successful system *with the same selection*. A transfinite construction that installs choices and checks only extendability can therefore walk into a dead end at stage ω. The construction must reserve world 1 for X on a neighbourhood of p0 **before** stage ω, using information about the limit point p0 that no finite stage forces. The reservation invariant of the Vacuous Prop is thus necessary as a *commitment device*, not merely sufficient. With the reservation, use world 2 or 3 near p0, as Ψ^1 itself does: there, (r_k, X) fails at world 1 for large k.

### 6.3 What the counterexamples show

- The correct central lemma must carry open, exchange-compatible reservations as data (Examples 1 and 2). Equivalently, by Thm 3.1, it must choose κ with R5 in view.
- **EL*** (exchange-compatible open reservations ℛ, Cl₅(κ_0) clean and respecting ℛ, unmet (p, X)): some i ∈ supp p can be installed and ℛ can be enlarged, preserving all of this.
  - *Status:* open in general.
  - The simplest pairwise dead end does not occur: in n = 2 no two section exchanges σ, τ have σ + τ violating (N) at both worlds: such a sum would have to add positive gambles, but section exchanges from coherent models are ≥ 0 on positive gambles (PROVED, one line). Longer cancellation chains were not examined. So I have neither a proof nor a counterexample.
  - EL* is TRUE in the witnessed class (§7).

---

## 7. The witnessed extension theorem (P3.7, PROVED)

Let ψ be an additive ranking on M with strictly guiding integral penalties and integrable envelope, and write Ψ_i for its world preorders. Consider the hypotheses (conditions on a candidate construction, not on the framework):
- **(W1)** For every p and X, some i ∈ supp p has ψ_i(C_p) ≤ ψ_i(X). This holds if C_p is ψ-Bayes at a weight supported in supp p.
- **(W2)** No X has ψ(X) ≤ ψ(C_p) coordinatewise with ψ(X) ≠ ψ(C_p). This holds if C_p is Bayes at an interior weight, or the unique Bayes model at a boundary weight.
- **(W3)** p ↦ ψ_i(C_p) is lower semicontinuous on Δ, for each i.
- **(W4)** No incoherent X has ψ(X) = ψ(C_p) for any p.

Call κ *ψ-admissible* if ψ_{κ(p,X)}(C_p) ≤ ψ_{κ(p,X)}(X). By (W1), a total ψ-admissible κ exists.

**Theorem 7.1.** Assume (W1)–(W3), and let κ be ψ-admissible. Then:
- (a) Cl₅(κ) ⊆ Ψ, and Cl₅(κ) has no outcome (a);
- (b) Cl₅(κ) is clean iff no incoherent X with ψ(X) = ψ(C_p) is tied with C_p at every world in Cl₅(κ). By Thm 3.1, that is then a successful system;
- (c) under (W4), every ψ-admissible κ gives a successful Cl₅(κ), and Ψ itself is a successful system;
- (d) EL* holds with the reservations ℛ^ψ_i(X) := {p : ψ_i(C_p) > ψ_i(X)}. These are open by (W3) and exchange-compatible: additivity makes ψ_i(C_q) − ψ_i(C_q − σ) independent of q, and (W1) gives (ET). The only possible failure is the (C)-tie of (b).

*Proof.*
- Ψ contains the background comparisons (strictly guiding penalties).
- Ψ is closed under R1–R3 (real-valued additive).
- Ψ is closed under R4: ψ(X) ≤ ψ(C_p) forces equality by (W2).
- Ψ is closed under R5: ψ_i(C_p) ≤ liminf ψ_i(C_{p_k}) ≤ ψ_i(X) by (W3).
- Ψ contains κ, so Cl₅(κ) ⊆ Ψ. Ψ has no strict-(G) reversal. Ties in Cl₅(κ) are Ψ-ties, i.e. equal profiles.
- Under (W4), Ψ is a clean family closed under R1–R5 that contains a total choice, and the proof of Thm 3.1(1) applies to it verbatim. ∎

**Tests.**
- *Reproduces existing covers (CHECKED against the sources' statements).* The following additive constructions all have an a.e.-unique Bayes model at every p ∈ Δ, selected as C_p, with continuous profiles; uniqueness gives (W1), (W2) and (W4), and dominated convergence gives (W3):
  - the precise/Brier families (all models; M_U as in §6);
  - normalised boxes (*Coverage after NA*, Thm limit and (4): "unique minimizing advice", "dominated convergence");
  - two-world credal intervals (v3 Thm general and Prop bayes-interval, unique p-Bayes for every p);
  - gauge mixtures (R10a Thm M, refereed in R12).
  
  The lemma returns Ψ, or any minimal Cl₅(κ) inside it. N26.1 (two worlds) appears to be the case where (W4) fails at t0 and the lexicographic secondaries break the tie. Its Thm (c),(d) fit (b), but I have not re-derived (W2)–(W3) for its primary.
- *No false covers (PROVED from cited theorems).*
  - **Additive T1.** If (W1)–(W4) held with T1 selected on a decomposable domain with (LF), Ψ would be an additive cover with integral penalties. Thm gm (Thm main on M_U) excludes this. So every additive ψ satisfying (W1)–(W3) with T1 selected violates (W4), and the lemma then returns only the conditional (b).
  - **V, strict guidance, n ≥ 3.** If (W1)–(W3) held with V selected, Ψ would be complete with (G), (IB) and (S): sections are closed by (W3), competitiveness holds by (W1), and V is undominated by (W2). *Three Complete Rankings* / *Complete Rankings for Any Number of Worlds* exclude that, without (C). So the lemma never reaches V, even in form (b).

---

## 8. What the lemma gives for T1 on the U-domain, and what is missing (P3.8)

**8.1 (PROVED)** From Thm 3.1, Cor 2.2 and §5:
- T1 is covered on M_U iff there are (i) a coherent selection C with C_{e_i} = P_i, T1 = C_{p*}, p* ∈ Δ°, and the face conditions of 5.2, and (ii) a transversal family I(σ) ((T) of Cor 2.2), equivalently a total κ, whose closure under the five rules is clean.
- The only free data are κ. R5 is the only non-finitary rule (Thm 4.1). Any construction must commit to open, exchange-compatible reservations ahead of limits (P3.5, P3.6).

**8.2 (PROVED, combining Thm 7.1 with write-up §7)** Suppose a T1 cover arises from Thm 7.1(b): an additive ψ satisfying (W1)–(W3) with T1 = C_{p*}, and a ψ-admissible κ with clean Cl₅(κ). Then Cl₅(κ) satisfies (H_{M0}) with supporting assessment ψ: the weights ρ_i μ are countably additive, positive, and endorse *all* its comparisons. In particular (E_ψ) holds. Therefore:
- Prop M0 (α)–(δ) hold;
- **E(ψ) ≠ ∅** (Prop M0, last sentence, via Thm main);
- E(ψ) is a countable union of atom chords, each cutting off the vertex of its odd world, with no fan points (Thm Estructure);
- Prop Epsi applies, including: every face point is the profile of a selected t-Bayes model; ideal tie-breaking a.e. on two-dimensional faces; split-independence along chords.

So the witnessed route lands **exactly in R-a′/R-b′ under (E_ψ)**, with the extra regularity (W2)–(W3) on the selection.

**8.3 The extra input a T1 construction would need.**
1. **An additive pre-system through T1**: ψ with (W1)–(W3) and T1 selected. This is all the axioms except (C).
   - The additive no-go theorems (Thm main, Thm gm) use (C), through (BU) at every interior weighting. So they do not exclude pre-systems.
   - In a pre-system, KKM still makes the unique Bayes models at non-exceptional interior weightings coherent (a unique Bayes model is undominated, hence tied with, hence equal to, a selected one), so (γ) and Thm Estructure apply to ψ itself.
   - Its existence is therefore the chord-tolerant geometric residual R-a′/R-b′ for ψ itself (realisations allowed to fail on countably many atom chords, with T1 possibly on one). *Open.*
2. **An ordinal tie-breaking choice**: a ψ-admissible κ whose minimal closure never ties an incoherent face model Y = B_t ∪ S with the selected shell C = B_t ∪ G_θ of the same profile.
   - Locally the test is on w = 1_S − 1_{G_θ}: it is a tie at world j iff j ∈ I(w).
   - w has both signs at every world, so N(w) = ∅ and no vertex lies in Comp(w). (ET) can force at most a transversal of the edges met by Comp(w), so |I(w)| ≥ 2 at most. It never forces I(w) = Ω.
   - So (ET) does not exclude tie-breaking (PROVED). The obstruction, if any, must come from (Σ), (Und) or R5. N26.1 is the two-world existence proof of this mechanism. *Open* in three worlds (question Q1).
3. **Or a non-additive device controlling R5.** For (M1)/(M2) covers no additive witness exists, and closed sections must come from a world order 𝒮_i that is closed along every selection pencil σ + d_k (rule R5) yet not additive there.
   - Known non-additive orders fail this: lexicographic designs (N9.6 FC, R2 Prop 8, R3 Thm L; only countable staircases survive, R2 Thm 7) and the ultrafilter/KPS orders (their ultrafilters contain sets of arbitrarily small measure).
   - **P3.C1 (CONJECTURE).** Let world i be complete, and let the selection be continuous in measure, with shell exhaustions S_k ↑ S (S_k = E_i(C_{p_k}) ∖ E_i(C_{p_1}) along monotone selection paths) that generate the measure algebra of U.
     - Then R5 forces a countably additive representation of ≤_i.
     - What R5 gives (PROVED): from R5 with X chosen so that E_i(X) = E_i(C_{p_1}) ∪ (S ∖ A′) ∪ B, if A′ ∩ S_k ≤_i B ∪ ((S ∖ S_k) ∖ A′) for all k, then A′ ≤_i B. This is Villegas's monotone continuity, but only along sequences A′ ∩ S_k, not along all increasing sequences.
     - If the conjecture holds, complete T1 covers with such selections are complete (CP-a) systems, excluded by Thm complete.
     - Support: Villegas's theorem in the fully continuous case; no evidence either way for the restricted case.
   - Hence the remaining non-additive room is incomplete worlds, discontinuous selections, or orders for which P3.C1 fails.

**8.4 Bottom line for the programme.** The extension lemma is not the missing piece in the form posed. Given the selection, the order-theoretic part is exact (Thm 3.1) and compact (Thm 4.1). What a T1 construction needs is a **global commitment that controls R5**. The only known device is an additive witness. It reduces T1 to two open problems: the chord-tolerant pre-system (R-a′/R-b′ for ψ itself) and ordinal tie-breaking at the atom chords (Q1 under (E_ψ)). Example 2 shows that this commitment cannot be produced stage by stage from extendability alone.

---

## 9. Status table

| Claim | Status |
|---|---|
| 2.1 transport; 2.2 complete reformulation on M_U | PROVED |
| 3.1 exact extension theorem with R5; minimal systems | PROVED |
| 4.1 compactness of everything but (Cl); failure at R5 | PROVED (failure via 6.2) |
| 5.1–5.3 ET, compulsory comparisons, transported Lemma R | PROVED |
| Remark 5: near-T1 uses reduce to edge-Pareto for continuous selections | CHECKED |
| 6.1 Example 1 (per-model reservations insufficient); exchange-compatibility necessary | PROVED (geometry also NUMERICS) |
| 6.2 Example 2 (extendable ω-chain with dead union) | PROVED (sizes NUMERICS) |
| EL* in general | open (no counterexample; simplest dead ends excluded, PROVED) |
| 7.1 witnessed extension theorem; EL* in the witnessed class | PROVED |
| Known covers satisfy (W1)–(W4) | CHECKED (statements of the sources) |
| No false covers (T1 additive; V strict, n ≥ 3) | PROVED from Thm gm / Three Complete Rankings |
| 8.2 witnessed T1 covers are M0 with (E_ψ), E(ψ) ≠ ∅ | PROVED from write-up Prop M0, Thm Estructure, Prop Epsi |
| 8.3(1) pre-systems not excluded by Thm main/gm | PROVED (those theorems use (C) through (BU)); existence open |
| 8.3(2) ET never forces the (C)-tie at a chord | PROVED |
| P3.C1 Villegas-type rigidity along selection pencils | CONJECTURE |
| T1 system without (Cl) exists | open (finite-character question by 4.1) |

## 10. Files
- `p3py/check_examples.py` and `p3py/check_examples.out`: the geometry of Example 1 (membership of a, a′ in D_{T1}, U, B_u and B_r; the faces met by Comp(1_A); the signs), and Example 2 (W′ non-null, a_k > 0, the size of M_m). NUMERICS only.
